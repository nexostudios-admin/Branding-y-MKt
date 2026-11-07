"""Lee la planilla de Google "Masherr - Productos de la web" y arma la lista de productos de la web.

La planilla manda en: nombre, precio, stock, publicado, marca, categoría, opción y código.
La descripción y las fotos se toman de la planilla si están cargadas ("Descripción nueva", "Fotos nuevas");
si no, se conservan las que la web ya tenía (copia de Tiendanube).
Cada fila se vincula con el producto que ya existía por nombre + opción, así no cambian los links ni los carritos.
"""
import csv, hashlib, io, re, sys, unicodedata, urllib.request, zlib
from collections import Counter

UA = {'User-Agent': 'Mozilla/5.0 (compatible; web-masherr/1.0)'}


def norm(s):
    s = ''.join(c for c in unicodedata.normalize('NFD', (s or '').lower()) if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()


def slugify(s):
    return norm(s).replace(' ', '-')[:80] or 'producto'


def numero(s):
    """'$16.000' -> 16000 · '' -> None."""
    s = re.sub(r'[^\d,]', '', str(s or '')).split(',')[0]
    return int(s) if s else None


def leer(fuente):
    if re.match(r'https?://', fuente):
        with urllib.request.urlopen(urllib.request.Request(fuente, headers=UA), timeout=60) as r:
            texto = r.read().decode('utf-8-sig')
        if texto.lstrip().startswith('<'):
            raise RuntimeError('la planilla no es pública: compartila como "Cualquier persona con el enlace: Lector"')
    else:
        texto = open(fuente, encoding='utf-8-sig').read()
    return [{(k or '').strip(): (v or '').strip() for k, v in f.items()} for f in csv.DictReader(io.StringIO(texto))]


def link_drive(url):
    m = re.search(r'/d/([\w-]{20,})', url) or re.search(r'[?&]id=([\w-]{20,})', url)
    return f'https://drive.google.com/uc?export=download&id={m.group(1)}' if m else url


def bajar_fotos(urls, slug, sitio):
    """Descarga las fotos (Drive o web), las guarda en 480 y 1024 px y devuelve las rutas base."""
    from PIL import Image
    salida = []
    for u in urls:
        base = f'img/productos/{slug}-{hashlib.sha1(u.encode()).hexdigest()[:8]}'
        chica, grande = sitio / (base + '-480-0.webp'), sitio / (base + '-1024-1024.webp')
        if not grande.exists():
            try:
                with urllib.request.urlopen(urllib.request.Request(link_drive(u), headers=UA), timeout=60) as r:
                    im = Image.open(io.BytesIO(r.read())).convert('RGB')
            except Exception as e:
                print(f'  ! no se pudo bajar la foto {u}: {e}', file=sys.stderr)
                continue
            grande.parent.mkdir(parents=True, exist_ok=True)
            g = im.copy(); g.thumbnail((1024, 1024)); g.save(grande, quality=85)
            c = im.copy(); c.thumbnail((480, 480)); c.save(chica, quality=82)
        salida.append(base)
    return salida


def desde_planilla(fuente, base, categorias, categoria_por_nombre, marca_por_nombre, sitio):
    filas = leer(fuente)
    if not filas or 'Producto' not in filas[0]:
        raise RuntimeError('la planilla no tiene la columna "Producto"')
    nombres_cat = {norm(n): slug for slug, n, _ in categorias}

    idx = {}
    for p in base:
        for v in p['variantes']:
            idx.setdefault((norm(p['nombre']), norm(v['nombre'] or '')), []).append((p, v))
    usados = Counter()
    grupos = {}
    avisos = []
    for n, f in enumerate(filas, start=2):
        nombre = f.get('Producto', '')
        if not nombre:
            continue
        clave = (norm(nombre), norm(f.get('Opción', '')))
        candidatos = idx.get(clave, [])
        i = usados[clave]; usados[clave] += 1
        pv = candidatos[i] if i < len(candidatos) else None
        if f.get('Publicado', 'SI').upper() in ('NO', 'N'):
            continue
        g = pv[0]['slug'] if pv else 'nuevo:' + norm(nombre)
        grupos.setdefault(g, []).append((n, f, pv))

    productos, slugs = [], set()
    for g, filas_g in grupos.items():
        _, f0, pv0 = filas_g[0]
        p0 = pv0[0] if pv0 else None
        nombre = f0['Producto']
        slug = p0['slug'] if p0 else slugify(nombre)
        while slug in slugs:
            slug += '-2'
        slugs.add(slug)
        cat_txt = norm(f0.get('Categoría', ''))
        cat = nombres_cat.get(cat_txt) or next((s for t, s in nombres_cat.items() if cat_txt and (cat_txt in t or t in cat_txt)), None)
        if not cat:
            cat = p0['cat'] if p0 else categoria_por_nombre(nombre)
            if cat_txt:
                avisos.append(f'fila {filas_g[0][0]}: categoría "{f0.get("Categoría")}" no reconocida, uso "{cat}"')
        fotos_nuevas = [u for u in re.split(r'[\s,]+', ' '.join(f.get('Fotos nuevas', '') for _, f, _ in filas_g)) if u.startswith('http')]
        imgs = bajar_fotos(fotos_nuevas, slug, sitio) if fotos_nuevas else (p0['imgs'] if p0 else [])
        desc = next((f['Descripción nueva'] for _, f, _ in filas_g if f.get('Descripción nueva')), None) or (p0['_desc'] if p0 else '')
        variantes = []
        for n, f, pv in filas_g:
            precio = numero(f.get('Precio'))
            stock = numero(f.get('Stock'))
            opcion = f.get('Opción') or None
            vid = pv[1]['id'] if pv else zlib.crc32(f'{slug}|{opcion}'.encode()) % 2_000_000_000 + 10
            if not precio:
                avisos.append(f'fila {n}: "{nombre}" sin precio, se muestra sin poder comprar')
            variantes.append({'id': vid, 'sku': f.get('Código') or (pv[1]['sku'] if pv else None), 'nombre': opcion,
                              'precio': precio or 0, 'stock': stock,
                              'disponible': bool(precio) and (stock is None or stock > 0)})
        precios = [v['precio'] for v in variantes if v['precio']]
        productos.append({
            'id': p0['id'] if p0 else zlib.crc32(slug.encode()), 'slug': slug, 'nombre': nombre,
            'marca': f0.get('Marca') or (marca_por_nombre(nombre)), 'cat': cat,
            'catNombre': next(c[1] for c in categorias if c[0] == cat), 'sub': p0['sub'] if p0 else None,
            'precio': min(precios) if precios else 0, 'imgs': imgs, 'disponible': any(v['disponible'] for v in variantes),
            'variantes': variantes, '_desc': desc, '_peso': p0['_peso'] if p0 else None, '_url_tn': p0['_url_tn'] if p0 else None,
        })
    for a in avisos:
        print('  ! ' + a, file=sys.stderr)
    return productos
