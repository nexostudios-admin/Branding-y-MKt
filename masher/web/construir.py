"""Genera el sitio estático de Masherr en ./sitio a partir del catálogo y de config.json.

Uso: python3 construir.py
Entradas: catalogo/snapshot_tiendanube.json (o un CSV convertido al mismo formato), config.json,
          ../catalogo/productos.json (solo para la lista de marcas conocidas).
Salidas: sitio/index.html, sitio/tienda/, sitio/producto/<slug>/, sitio/carrito/, sitio/empresas/,
         sitio/nosotros/, sitio/404.html, sitio/data/productos.json, sitio/assets/js/config.js, sitemap.
"""
import html, json, os, re, shutil, unicodedata
from pathlib import Path

AQUI = Path(__file__).parent
SITIO = AQUI / 'sitio'
CFG = json.load(open(AQUI / 'config.json'))
SNAP = json.load(open(AQUI / 'catalogo' / 'snapshot_tiendanube.json'))
MARCAS_PDF = json.load(open(AQUI.parent / 'catalogo' / 'productos.json'))
e = lambda s: html.escape(str(s or ''), quote=True)

def norm(s):
    s = ''.join(c for c in unicodedata.normalize('NFD', (s or '').lower()) if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()

def precio(n):
    return '$' + f'{round(n):,}'.replace(',', '.')

# ---------------------------------------------------------------- Catálogo
CATEGORIAS = [
    ('herramientas-electricas', 'Herramientas eléctricas', 'Taladros, amoladoras, sierras, rotomartillos y más'),
    ('inalambricas', 'Inalámbricas a batería', 'Taladros, atornilladores y llaves de impacto'),
    ('herramientas-manuales', 'Herramientas manuales', 'Llaves, pinzas, destornilladores y sets'),
    ('medicion', 'Medición y nivelación', 'Niveles, cintas y medidores láser'),
    ('accesorios', 'Discos, brocas y puntas', 'Corte, perforación y atornillado'),
    ('maquinas', 'Soldadura y compresores', 'Soldadoras, compresores y máquinas'),
    ('agua-jardin', 'Agua, limpieza y jardín', 'Bombas, hidrolavadoras, aspiradoras'),
    ('adhesivos', 'Adhesivos y selladores', 'Adhesivos de contacto, colas y espumas'),
    ('almacenamiento', 'Cajas y almacenamiento', 'Cajas, bolsos y sistemas modulares'),
    ('otros', 'Otros productos', 'Escaleras, calefacción y más'),
]
POR_CRUMB = {
    'herramientas electricas': 'herramientas-electricas', 'inalambricas a bateria': 'inalambricas',
    'herramientas manuales': 'herramientas-manuales', 'de medicion': 'medicion', 'cajas de herramientas': 'almacenamiento',
    'bolsos': 'almacenamiento', 'puntas y adaptadores': 'accesorios', 'discos de corte': 'accesorios', 'mechas brocas': 'accesorios',
    'cinceles': 'accesorios', 'maquinas': 'maquinas', 'agua limpieza': 'agua-jardin', 'jardin': 'agua-jardin',
    'adhesivos y selladores': 'adhesivos', 'espumas': 'adhesivos', 'escaleras': 'otros', 'equipos de pintar': 'otros',
    'calefactor': 'otros', 'muebles para el hogar': 'otros',
}
PALABRAS = [  # para productos cargados solo en "Productos", "Ofertas" o "Herramientas"
    ('inalambricas', ['inalambric', 'bateria', 'one power']),
    ('maquinas', ['soldadora', 'compresor', 'electrodo', 'alambre mig', 'hormigonera']),
    ('accesorios', ['disco', 'broca', 'mecha', 'punta', 'copa', 'cincel', 'adaptador']),
    ('medicion', ['nivel', 'cinta metrica', 'medidor', 'escuadra']),
    ('agua-jardin', ['bomba', 'hidrolavadora', 'aspiradora', 'cesped', 'bordeadora', 'sopladora', 'manguera']),
    ('adhesivos', ['adhesivo', 'espuma', 'cola ', 'sellador', 'diluyente']),
    ('almacenamiento', ['caja de herramientas', 'bolso', 'packout', 'carro de herramientas']),
    ('herramientas-electricas', ['taladro', 'amoladora', 'sierra', 'rotomartillo', 'lijadora', 'cepillo', 'minitorno', 'mini torno', 'pistola de calor', 'atornillador', 'fresadora', 'lustra', 'termofusora']),
    ('herramientas-manuales', ['llave', 'pinza', 'destornillador', 'juego', 'set ', 'alicate', 'martillo', 'morsa', 'remachadora', 'crimpeadora', 'lima']),
]

def categoria(p):
    crumbs = [norm(c) for c in (p['categorias'] or [])]
    for c in reversed(crumbs):
        if c in POR_CRUMB: return POR_CRUMB[c]
    n = norm(p['nombre'])
    for slug, kws in PALABRAS:
        if any(k in n for k in kws): return slug
    return 'otros'

MARCAS = sorted({re.sub(r'\s*\(.*\)$', '', x['marca']) for x in MARCAS_PDF} | {'Aliafor', 'Venturo', 'Milwaukee', 'Makita', 'Gamma', 'Einhell'}, key=len, reverse=True)
def marca(nombre):
    n = ' ' + norm(nombre) + ' '
    for m in MARCAS:
        if ' ' + norm(m) + ' ' in n: return m
    return None

import urllib.request
FOTOS = SITIO / 'img' / 'productos'
def base_img(u, slug, i):
    """Descarga la foto (480 y 1024 px) una sola vez y devuelve la ruta local sin sufijo."""
    remoto = re.sub(r'-\d+-\d+\.webp$', '', u)
    local = f'img/productos/{slug}-{i}'
    for suf in ('-480-0.webp', '-1024-1024.webp'):
        dest = SITIO / (local + suf)
        if not dest.exists():
            dest.parent.mkdir(parents=True, exist_ok=True)
            req = urllib.request.Request(remoto + suf, headers={'User-Agent': 'Mozilla/5.0 (compatible; sitio-masherr/1.0)'})
            dest.write_bytes(urllib.request.urlopen(req, timeout=40).read())
    return local

def resumen(t, n=160):
    t = re.sub(r'\s+', ' ', t or '').strip()
    if len(t) <= n: return t
    return t[:n].rsplit(' ', 1)[0].rstrip(',;:') + '…'

productos = []
for p in SNAP['productos']:
    vs = [{
        'id': v['id'], 'sku': v['sku'], 'nombre': ' / '.join(v['opciones'] or []) or None,
        'precio': v['precio'], 'stock': v['stock'],
        'disponible': bool(v['disponible']) and (v['stock'] is None or v['stock'] > 0) and bool(v['precio']),
    } for v in p['variantes']]
    if not vs: continue
    cat = categoria(p)
    sub = (p['categorias'] or [None])[-1] if p['categorias'] and len(p['categorias']) > 1 else None
    productos.append({
        'id': p['id_tiendanube'], 'slug': p['slug'], 'nombre': p['nombre'], 'marca': p['marca'] or marca(p['nombre']),
        'cat': cat, 'catNombre': next(c[1] for c in CATEGORIAS if c[0] == cat), 'sub': sub,
        'precio': min(v['precio'] for v in vs if v['precio']), 'imgs': [base_img(u, p['slug'], i) for i, u in enumerate(p['imagenes'])],
        'disponible': any(v['disponible'] for v in vs), 'variantes': vs,
        '_desc': p['descripcion'] or '', '_peso': p['peso_kg'], '_url_tn': p['url'],
    })
cats_usadas = [c for c in CATEGORIAS if any(p['cat'] == c[0] for p in productos)]

# ---------------------------------------------------------------- Plantillas
SPRITE = """<svg width="0" height="0" style="position:absolute" aria-hidden="true">
<symbol id="i-buscar" viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="M16.5 16.5 21 21"/></symbol>
<symbol id="i-carrito" viewBox="0 0 24 24"><path d="M3 4h2l2.4 11.2a1 1 0 0 0 1 .8h9.2a1 1 0 0 0 1-.8L21 8H6.2"/><circle cx="9" cy="20" r="1.4"/><circle cx="18" cy="20" r="1.4"/></symbol>
<symbol id="i-menu" viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16"/></symbol>
<symbol id="i-cerrar" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6 6 18"/></symbol>
<symbol id="i-mas" viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></symbol>
<symbol id="i-menos" viewBox="0 0 24 24"><path d="M5 12h14"/></symbol>
<symbol id="i-papelera" viewBox="0 0 24 24"><path d="M4 7h16M9 7V4h6v3M6 7l1 13h10l1-13"/></symbol>
<symbol id="i-flecha" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></symbol>
<symbol id="i-anterior" viewBox="0 0 24 24"><path d="M15 6l-6 6 6 6"/></symbol>
<symbol id="i-siguiente" viewBox="0 0 24 24"><path d="M9 6l6 6-6 6"/></symbol>
<symbol id="i-filtro" viewBox="0 0 24 24"><path d="M4 6h16M7 12h10M10 18h4"/></symbol>
<symbol id="i-lupa" viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="M16.5 16.5 21 21M11 8v6M8 11h6"/></symbol>
<symbol id="i-ubicacion" viewBox="0 0 24 24"><path d="M12 21s-7-6.2-7-12a7 7 0 0 1 14 0c0 5.8-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/></symbol>
<symbol id="i-telefono" viewBox="0 0 24 24"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/></symbol>
<symbol id="i-info" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/></symbol>
<symbol id="i-whatsapp" viewBox="0 0 24 24"><path d="M3.5 20.5l1.4-4.2A8.5 8.5 0 1 1 8 19.3z"/><path d="M9 8.6c.2 2.9 2.6 5.4 5.6 6l1.3-1.4-2-1.1-1 .7c-.9-.4-2-1.5-2.4-2.4l.7-1-1-2z"/></symbol>
<symbol id="i-instagram" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5h.01"/></symbol>
<symbol id="i-facebook" viewBox="0 0 24 24"><path d="M14 8h3V4h-3a4 4 0 0 0-4 4v3H7v4h3v6h4v-6h3l1-4h-4V8z"/></symbol>
<symbol id="i-linkedin" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M8 10v7M8 7v.01M12 17v-4a2 2 0 0 1 4 0v4M12 10v7"/></symbol>
<symbol id="i-tiktok" viewBox="0 0 24 24"><path d="M14 3v11.5a3.5 3.5 0 1 1-3.5-3.5"/><path d="M14 3c.5 2.6 2.4 4.5 5 4.8"/></symbol>
<symbol id="i-empresa" viewBox="0 0 24 24"><path d="M3 21h18M5 21V9l5-3v15M10 21V4l9 4v13M14 10h2M14 14h2M7 12h1M7 16h1"/></symbol>
</svg>"""

def ic(i):
    return f'<svg class="icono" aria-hidden="true" focusable="false"><use href="#i-{i}"></use></svg>'

REDES = [('instagram', 'Instagram'), ('tiktok', 'TikTok'), ('linkedin', 'LinkedIn'), ('facebook', 'Facebook')]
redes_activas = [(k, n, CFG['redes'][k]) for k, n in REDES if CFG['redes'].get(k, {}).get('url')]

def pagina(ruta, titulo, desc, cuerpo, actual='', jsonld=None, scripts=(), indexar=True):
    prof = ruta.count('/')
    r = '../' * prof
    canon = (CFG['dominio'].rstrip('/') + '/' + ruta.replace('index.html', '')) if CFG['dominio'] else ''
    nav = [('', 'Inicio'), ('tienda/', 'Tienda'), ('empresas/', 'Empresas'), ('nosotros/', 'Nosotros')]
    navhtml = lambda: ''.join(f'<a href="{r}{h}"{" aria-current=\"page\"" if actual == h else ""}>{t}</a>' for h, t in nav)
    ld = f'<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>' if jsonld else ''
    redes_pie = ''.join(f'<a href="{e(x["url"])}" target="_blank" rel="noopener" aria-label="{n}">{ic(k)}</a>' for k, n, x in redes_activas)
    doc = f"""<!doctype html>
<html lang="es-AR" data-root="{r}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(titulo)}</title>
<meta name="description" content="{e(desc)}">
{'' if indexar else '<meta name="robots" content="noindex">'}
{f'<link rel="canonical" href="{e(canon)}">' if canon else ''}
<meta property="og:title" content="{e(titulo)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:locale" content="es_AR">
<meta name="theme-color" content="#08090B">
<link rel="icon" href="{r}assets/img/favicon.png">
<link rel="preload" href="{r}assets/fonts/DejaVuSansCondensed-Bold.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{r}assets/css/estilos.css">
{ld}
</head>
<body>
{SPRITE}
<a class="saltar" href="#contenido">Saltar al contenido</a>
<header class="cabecera">
  <div class="contenedor">
    <div class="cab-fila">
      <a class="marca-logo" href="{r}" aria-label="Masherr, ir al inicio"><img src="{r}assets/img/masher-logo-azul.webp" alt="Masherr máquinas - herramientas" width="473" height="97"></a>
      <nav class="cab-nav" aria-label="Principal">{navhtml()}</nav>
      <form class="cab-buscar" action="{r}tienda/" role="search"><div class="buscador"><label class="sr" for="q-cab">Buscar productos</label>
        <input id="q-cab" name="q" type="search" placeholder="Buscá por producto o marca" autocomplete="off"><button type="submit" aria-label="Buscar">{ic('buscar')}</button></div></form>
      <div class="cab-acciones">
        <a class="icono-boton" href="{r}carrito/" data-carrito-label aria-label="Carrito">{ic('carrito')}<span class="burbuja" data-burbuja hidden>0</span></a>
        <button class="icono-boton solo-movil" type="button" data-menu aria-expanded="false" aria-controls="menu-movil">{ic('menu')}<span class="sr">Abrir menú</span></button>
      </div>
    </div>
    <form class="cab-buscar solo-movil" action="{r}tienda/" role="search"><div class="buscador"><label class="sr" for="q-movil">Buscar productos</label>
      <input id="q-movil" name="q" type="search" placeholder="Buscá por producto o marca" autocomplete="off"><button type="submit" aria-label="Buscar">{ic('buscar')}</button></div></form>
    <nav id="menu-movil" class="menu-movil solo-movil" aria-label="Menú">{navhtml()}<a href="#contacto">Contacto</a></nav>
  </div>
</header>
<main id="contenido">
{cuerpo}
</main>
<footer class="pie" id="contacto">
  <div class="contenedor">
    <div class="pie-grid">
      <div>
        <a class="logo-bloque" href="{r}"><img src="{r}assets/img/masher-logo-azul.webp" alt="Masherr máquinas - herramientas" width="473" height="97" loading="lazy"></a>
        <p>Ferretería industrial en San Martín. Herramientas, máquinas e insumos para industria, talleres, mantenimiento y obra.</p>
        <div class="redes-pie">{redes_pie}</div>
      </div>
      <div>
        <h2>Contacto</h2>
        <ul>
          <li><a href="{e(CFG['mapa'])}" target="_blank" rel="noopener">{e(CFG['direccion'])}<br>{e(CFG['localidad'])}</a></li>
          <li>Teléfono: <a href="tel:+541147525210">{e(CFG['telefono'])}</a></li>
          <li>WhatsApp: <a href="https://wa.me/{CFG['whatsapp']}" target="_blank" rel="noopener">{e(CFG['whatsapp_visible'])}</a></li>
          {f'<li>{e(CFG["horarios"])}</li>' if CFG['horarios'] else ''}
        </ul>
      </div>
      <div>
        <h2>Comprar</h2>
        <ul>
          <li><a href="{r}tienda/">Tienda</a></li>
          <li><a href="{r}carrito/">Mi carrito</a></li>
          <li><a href="{r}empresas/">Pedidos para empresas</a></li>
          <li><a href="{r}nosotros/#como-comprar">Cómo comprar</a></li>
        </ul>
      </div>
    </div>
    <div class="pie-legal"><span>© Masherr Ferretería Industrial</span><span>Precios en pesos argentinos, publicados al {e(CFG['fecha_precios'])}. Se confirman por WhatsApp antes de cobrar.</span></div>
  </div>
</footer>
<a class="wa-flotante" href="https://wa.me/{CFG['whatsapp']}" target="_blank" rel="noopener" aria-label="Escribinos por WhatsApp">{ic('whatsapp')}</a>
<script src="{r}assets/js/config.js"></script>
<script src="{r}assets/js/app.js"></script>
{''.join(f'<script src="{r}assets/js/{s}"></script>' for s in scripts)}
</body>
</html>
"""
    destino = SITIO / ruta
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(re.sub(r'\n\s*\n', '\n', doc))

def tarjeta(p, r):
    v = p['variantes'][0]
    img = f'<img src="{r}{p["imgs"][0]}-480-0.webp" alt="" width="480" height="480" loading="lazy" decoding="async">' if p['imgs'] else ''
    if not p['disponible']:
        boton = '<button class="boton agregar" type="button" disabled>Sin stock</button>'
    elif len(p['variantes']) > 1:
        boton = f'<a class="boton secundario agregar" href="{r}producto/{p["slug"]}/">Elegir opción</a>'
    else:
        boton = f'<button class="boton agregar" type="button" data-agregar="{v["id"]}" data-nombre="{e(p["nombre"])}">{ic("carrito")}Agregar</button>'
    return f"""<article class="tarjeta"><div class="foto">{img}</div><div class="cuerpo">
      {f'<span class="marca">{e(p["marca"])}</span>' if p['marca'] else ''}
      <h3><a href="{r}producto/{p['slug']}/">{e(p['nombre'])}</a></h3>
      <span class="precio">{'<span style="font-size:.6em">desde </span>' if len(p['variantes']) > 1 else ''}{precio(p['precio'])}</span>
      <span class="estado {'stock-ok' if p['disponible'] else 'stock-no'}">{'Disponible' if p['disponible'] else 'Sin stock'}</span>
      {boton}</div></article>"""

def bloque_redes(r):
    tarjetas = ''.join(f"""<li><a class="red" href="{e(x['url'])}" target="_blank" rel="noopener">{ic(k)}<span><b>{n}</b><span>{e(x['usuario'])}</span></span></a></li>"""
                       for k, n, x in redes_activas if k != 'facebook')
    return f"""<section class="seccion suave" aria-labelledby="t-redes">
  <div class="contenedor">
    <div class="cabeza-seccion"><div><p class="rotulo">Redes</p><h2 class="titulo-seccion" id="t-redes">Lo que mostramos en el mostrador, también online.</h2></div>
      <p class="bajada">Demostraciones, comparativas y consejos para elegir bien. Seguinos y escribinos cuando quieras.</p></div>
    <ul class="redes-grid">{tarjetas}</ul>
    <div data-bloque-pubs>
      <div id="publicaciones" class="publicaciones"></div>
      <p class="aviso-terceros">Las publicaciones se cargan desde cada red social solo cuando tocás “Ver publicación”.</p>
    </div>
  </div>
</section>"""

# ---------------------------------------------------------------- Limpiar y copiar
for sub in ['tienda', 'producto', 'carrito', 'empresas', 'nosotros', 'data']:  # img/ se conserva como caché
    shutil.rmtree(SITIO / sub, ignore_errors=True)
(SITIO / 'data').mkdir(parents=True)

publico = [{k: v for k, v in p.items() if not k.startswith('_')} for p in productos]
json.dump({'actualizado': CFG['fecha_precios'], 'categorias': [{'slug': c[0], 'nombre': c[1]} for c in cats_usadas], 'productos': publico},
          open(SITIO / 'data' / 'productos.json', 'w'), ensure_ascii=False, separators=(',', ':'))
cfg_pub = {k: CFG[k] for k in ['whatsapp', 'whatsapp_visible', 'telefono', 'direccion', 'localidad', 'fecha_precios', 'redes', 'publicaciones']}
(SITIO / 'assets' / 'js' / 'config.js').write_text('window.MASHERR = ' + json.dumps(cfg_pub, ensure_ascii=False, indent=1) + ';\n')

# ---------------------------------------------------------------- Inicio
r = ''
conteo = {c[0]: sum(1 for p in productos if p['cat'] == c[0]) for c in cats_usadas}
destacados = []
for c in cats_usadas:  # uno o dos por categoría, con stock y foto
    destacados += [p for p in productos if p['cat'] == c[0] and p['disponible'] and p['imgs']][:1]
destacados = destacados[:8]
inicio = f"""
<section class="hero oscuro" aria-labelledby="t-hero">
  <div class="rayas" aria-hidden="true"></div>
  <div class="contenedor">
    <p class="rotulo">Ferretería industrial · San Martín</p>
    <h1 id="t-hero">Herramientas y máquinas para trabajar bien.</h1>
    <p class="bajada">Una ferretería con historia, con asesoramiento técnico para industria, mantenimiento, talleres, profesionales y obra.</p>
    <form action="tienda/" role="search"><div class="buscador"><label class="sr" for="q-hero">Buscar productos</label>
      <input id="q-hero" name="q" type="search" placeholder="¿Qué necesitás? Ej.: amoladora, disco 115, nivel" autocomplete="off"><button type="submit" aria-label="Buscar">{ic('buscar')}</button></div></form>
    <ul class="chips" aria-label="Categorías más buscadas">{''.join(f'<li><a href="tienda/?cat={c[0]}">{e(c[1])}</a></li>' for c in cats_usadas[:6])}</ul>
  </div>
</section>
<section class="seccion" aria-labelledby="t-cat">
  <div class="contenedor">
    <div class="cabeza-seccion"><div><p class="rotulo">Categorías</p><h2 class="titulo-seccion" id="t-cat">Elegí por tipo de trabajo.</h2></div>
      <a class="boton secundario" href="tienda/">Ver toda la tienda {ic('flecha')}</a></div>
    <ul class="grilla-cat">{''.join(f'<li><a class="tile-cat" href="tienda/?cat={c[0]}"><b>{e(c[1])}</b><span>{conteo[c[0]]} productos {ic("flecha")}</span></a></li>' for c in cats_usadas)}</ul>
  </div>
</section>
<section class="seccion suave" aria-labelledby="t-dest">
  <div class="contenedor">
    <div class="cabeza-seccion"><div><p class="rotulo">Selección</p><h2 class="titulo-seccion" id="t-dest">Para equipar el taller.</h2></div></div>
    <ul class="grilla-prod">{''.join(f'<li>{tarjeta(p, r)}</li>' for p in destacados)}</ul>
  </div>
</section>
<section class="seccion" aria-labelledby="t-como" id="como-comprar">
  <div class="contenedor">
    <p class="rotulo">Cómo comprar</p><h2 class="titulo-seccion" id="t-como">Armá el pedido online, lo cerramos por WhatsApp.</h2>
    <ol class="pasos">
      <li><b>Elegí</b><p>Buscá en la tienda y agregá al carrito lo que necesitás, con la cantidad.</p></li>
      <li><b>Envianos el pedido</b><p>Desde el carrito, el pedido llega armado a nuestro WhatsApp.</p></li>
      <li><b>Confirmamos y cerramos</b><p>Te confirmamos precio, stock, entrega y forma de pago antes de cobrar.</p></li>
    </ol>
  </div>
</section>
<section class="seccion oscuro" aria-labelledby="t-hist">
  <div class="contenedor dos-col">
    <div><p class="rotulo">Masherr</p><h2 class="titulo-seccion" id="t-hist">Una ferretería con historia.</h2>
      <p class="bajada">Somos una ferretería industrial de San Martín. Escuchamos qué tenés que resolver y te ayudamos a elegir la herramienta o el insumo correcto.</p>
      <p><a class="boton borde-claro" href="nosotros/">Conocenos {ic('flecha')}</a></p></div>
    <ul class="valores">
      <li><b>Criterio técnico</b><span>Comparamos opciones según el material, la tarea y la intensidad de uso.</span></li>
      <li><b>Atención cercana</b><span>Consultanos antes de comprar: te respondemos personas del equipo.</span></li>
      <li><b>Para cada trabajo</b><span>Industria, mantenimiento, talleres, profesionales y obra.</span></li>
    </ul>
  </div>
</section>
{bloque_redes(r)}
<section class="seccion azul banda" aria-labelledby="t-emp">
  <div class="rayas" aria-hidden="true"></div>
  <div class="contenedor">
    <div><p class="rotulo">Empresas</p><h2 class="titulo-seccion" id="t-emp">¿Comprás para una empresa o una obra?</h2>
      <p class="bajada">Contanos la tarea, los productos, las cantidades y el plazo. Te respondemos con una cotización.</p></div>
    <a class="boton claro" href="empresas/">{ic('empresa')}Pedir cotización</a>
  </div>
</section>"""
pagina('index.html', 'Masherr · Ferretería industrial en San Martín', 'Herramientas, máquinas e insumos industriales en Villa Lynch, San Martín. Comprá online y cerrá tu pedido por WhatsApp.', inicio, actual='',
       jsonld={'@context': 'https://schema.org', '@type': 'HardwareStore', 'name': 'Masherr Ferretería Industrial', 'telephone': '+54 11 4752-5210',
               'address': {'@type': 'PostalAddress', 'streetAddress': CFG['direccion'], 'addressLocality': 'Villa Lynch, San Martín', 'addressRegion': 'Buenos Aires', 'addressCountry': 'AR'},
               'sameAs': [x['url'] for _, _, x in redes_activas]})

# ---------------------------------------------------------------- Tienda
tienda = f"""
<div class="contenedor">
  <nav class="migas" aria-label="Ruta"><ol><li><a href="../">Inicio</a></li><li aria-current="page">Tienda</li></ol></nav>
  <div class="tienda-cab"><h1 id="titulo-tienda">Tienda</h1>
    <form id="form-buscar-tienda" role="search"><div class="buscador" style="max-width:640px"><label class="sr" for="buscar-tienda">Buscar en la tienda</label>
      <input id="buscar-tienda" name="q" type="search" placeholder="Buscá por producto, marca o código" autocomplete="off"><button type="submit" aria-label="Buscar">{ic('buscar')}</button></div></form></div>
  <div class="tienda-layout">
    <aside class="filtros" aria-labelledby="t-filtros"><h2 id="t-filtros">Filtrar</h2><form id="form-filtros"></form></aside>
    <section aria-labelledby="titulo-tienda">
      <div class="barra-resultados">
        <span class="cuenta" id="cuenta" aria-live="polite">Cargando…</span>
        <button class="boton secundario boton-filtros" type="button" data-abrir-filtros>{ic('filtro')}Filtrar</button>
        <label class="select-orden">Ordenar <select id="orden"><option value="relevancia">Relevancia</option><option value="precio-asc">Menor precio</option><option value="precio-desc">Mayor precio</option><option value="nombre">Nombre A-Z</option></select></label>
      </div>
      <div id="activos" class="activos"></div>
      <div id="resultados"><ul class="grilla-prod" aria-hidden="true">{'<li><div class="esqueleto" style="aspect-ratio:.62"></div></li>' * 8}</ul></div>
      <ul id="paginacion" class="paginacion"></ul>
      <noscript><h2>Todos los productos</h2><ul>{''.join(f'<li><a href="../producto/{p["slug"]}/">{e(p["nombre"])}</a> · {precio(p["precio"])}</li>' for p in productos)}</ul></noscript>
    </section>
  </div>
</div>
<dialog id="panel-filtros" class="panel-filtros" aria-labelledby="t-panel">
  <div class="panel-cab"><h2 id="t-panel" style="margin:0">Filtrar</h2><button class="icono-boton" type="button" data-cerrar-filtros aria-label="Cerrar filtros">{ic('cerrar')}</button></div>
  <form id="form-filtros-movil"><div class="panel-cuerpo"></div></form>
  <div class="panel-pie"><button class="boton ancho" type="submit" form="form-filtros-movil">Ver resultados</button></div>
</dialog>"""
pagina('tienda/index.html', 'Tienda · Masherr', 'Catálogo de herramientas, máquinas e insumos de Masherr. Buscá por producto o marca y armá tu pedido.', tienda, actual='tienda/', scripts=['tienda.js'])

# ---------------------------------------------------------------- Fichas
for p in productos:
    r = '../../'
    v0 = p['variantes'][0]
    imgs = p['imgs']
    principal = f'<img id="foto-principal" src="{r}{imgs[0]}-1024-1024.webp" srcset="{r}{imgs[0]}-480-0.webp 480w, {r}{imgs[0]}-1024-1024.webp 1024w" sizes="(min-width:1024px) 600px, 100vw" alt="{e(p["nombre"])}" width="640" height="640">' if imgs else ''
    minis = ''.join(f'<li><button type="button" data-foto="{i}" aria-label="Ver foto {i + 1}" {"aria-current=\"true\"" if i == 0 else ""}><img src="{r}{u}-480-0.webp" alt="" width="72" height="72" loading="lazy"></button></li>' for i, u in enumerate(imgs)) if len(imgs) > 1 else ''
    selector = ''
    if len(p['variantes']) > 1:
        selector = '<div class="campo"><label for="variante">Opción</label><select id="variante">' + ''.join(
            f'<option value="{v["id"]}" {"disabled" if not v["disponible"] else ""}>{e(v["nombre"])} · {precio(v["precio"])}{" · sin stock" if not v["disponible"] else ""}</option>' for v in p['variantes']) + '</select></div>'
    stock_txt = ('Sin stock' if not v0['disponible'] else ('Disponible' if v0['stock'] is None else f'Disponible · {v0["stock"]} en stock' if v0['stock'] <= 5 else 'Disponible'))
    relacionados = [x for x in productos if x['cat'] == p['cat'] and x['slug'] != p['slug'] and x['disponible']]
    relacionados = sorted(relacionados, key=lambda x: (x['sub'] != p['sub'], x['marca'] != p['marca']))[:4]
    consulta = f'Hola Masherr, quiero consultar por: {p["nombre"]} ({precio(p["precio"])}). '
    datos_js = json.dumps({'nombre': p['nombre'], 'variantes': p['variantes'], 'imgs': imgs}, ensure_ascii=False)
    ficha = f"""
<div class="contenedor">
  <nav class="migas" aria-label="Ruta"><ol><li><a href="{r}">Inicio</a></li><li><a href="{r}tienda/">Tienda</a></li><li><a href="{r}tienda/?cat={p['cat']}">{e(p['catNombre'])}</a></li><li aria-current="page">{e(p['nombre'])}</li></ol></nav>
  <div class="ficha">
    <div class="galeria">
      <button class="galeria-principal" type="button" data-ampliar aria-label="Ampliar foto">{principal}<span class="lupa">{ic('lupa')}</span></button>
      <ul class="miniaturas">{minis}</ul>
    </div>
    <div class="ficha-info">
      {f'<p class="rotulo">{e(p["marca"])}</p>' if p['marca'] else f'<p class="rotulo">{e(p["catNombre"])}</p>'}
      <h1>{e(p['nombre'])}</h1>
      <div class="ficha-meta">{f'<span>Marca: {e(p["marca"])}</span>' if p['marca'] else ''}<span>Categoría: {e(p['sub'] or p['catNombre'])}</span><span id="sku">{f'SKU: {e(v0["sku"])}' if v0['sku'] else ''}</span></div>
      <p class="ficha-precio" id="precio">{precio(v0['precio'])}</p>
      <p class="nota-precio">Precio publicado al {e(CFG['fecha_precios'])}. Te lo confirmamos por WhatsApp antes de cobrar.</p>
      <div class="compra">
        {selector}
        <p id="stock" class="{'stock-ok' if v0['disponible'] else 'stock-no'}" style="margin:0;font-weight:700">{stock_txt}</p>
        <div class="fila-compra">
          <div class="cantidad"><button type="button" data-cant="-1" aria-label="Restar uno">{ic('menos')}</button><label class="sr" for="cant">Cantidad</label><input id="cant" type="number" inputmode="numeric" min="1" max="999" value="1"><button type="button" data-cant="1" aria-label="Sumar uno">{ic('mas')}</button></div>
          <button class="boton" type="button" id="agregar" {'disabled' if not p['disponible'] else ''}>{ic('carrito')}{'Agregar al carrito' if p['disponible'] else 'Sin stock'}</button>
        </div>
        <a class="boton wa" href="https://wa.me/{CFG['whatsapp']}?text={e(__import__('urllib.parse').parse.quote(consulta))}" target="_blank" rel="noopener">{ic('whatsapp')}Consultar por WhatsApp</a>
      </div>
      <div class="aviso">{ic('info')}<span>El pedido se cierra por WhatsApp: confirmamos stock, entrega y forma de pago. Retiro en {e(CFG['direccion'])}, {e(CFG['localidad'])}.</span></div>
      <section class="ficha-seccion" aria-labelledby="t-desc"><h2 id="t-desc">Descripción</h2><div class="descripcion">{e(p['_desc'])}</div></section>
    </div>
  </div>
  {f'<section class="seccion" style="padding-top:0" aria-labelledby="t-rel"><h2 class="titulo-seccion" id="t-rel" style="font-size:32px">También te puede servir</h2><ul class="grilla-prod">' + ''.join(f'<li>{tarjeta(x, r)}</li>' for x in relacionados) + '</ul></section>' if relacionados else ''}
</div>
<dialog class="lightbox" id="lightbox" aria-label="Foto ampliada"><img id="lb-img" alt="{e(p['nombre'])}"><button class="icono-boton cerrar" type="button" data-cerrar-lb aria-label="Cerrar">{ic('cerrar')}</button>
  {f'<button class="icono-boton nav-lb ant" type="button" data-lb="-1" aria-label="Foto anterior">{ic("anterior")}</button><button class="icono-boton nav-lb sig" type="button" data-lb="1" aria-label="Foto siguiente">{ic("siguiente")}</button>' if len(imgs) > 1 else ''}</dialog>
<script>window.PRODUCTO = {datos_js};</script>"""
    oferta = {'@type': 'Offer', 'price': str(v0['precio']), 'priceCurrency': 'ARS',
              'availability': 'https://schema.org/' + ('InStock' if p['disponible'] else 'OutOfStock')}
    if CFG['dominio']: oferta['url'] = CFG['dominio'].rstrip('/') + f'/producto/{p["slug"]}/'
    ld = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'Product', 'name': p['nombre'], 'image': [((CFG['dominio'].rstrip('/') + '/') if CFG['dominio'] else '') + u + '-1024-1024.webp' for u in imgs], 'description': resumen(p['_desc'], 300),
         **({'brand': {'@type': 'Brand', 'name': p['marca']}} if p['marca'] else {}), **({'sku': v0['sku']} if v0['sku'] else {}), 'offers': oferta},
        {'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Tienda', 'item': (CFG['dominio'].rstrip('/') + '/tienda/') if CFG['dominio'] else 'tienda/'},
            {'@type': 'ListItem', 'position': 2, 'name': p['catNombre']}, {'@type': 'ListItem', 'position': 3, 'name': p['nombre']}]}]}
    pagina(f'producto/{p["slug"]}/index.html', f'{p["nombre"]} · Masherr', resumen(p['_desc']) or p['nombre'], ficha, actual='tienda/', jsonld=ld, scripts=['producto.js'])

# ---------------------------------------------------------------- Carrito
carrito = f"""
<div class="contenedor">
  <nav class="migas" aria-label="Ruta"><ol><li><a href="../">Inicio</a></li><li aria-current="page">Carrito</li></ol></nav>
  <div class="tienda-cab"><h1>Tu carrito</h1></div>
  <div id="carrito-app"><p class="cargando">Cargando tu carrito…</p></div>
</div>"""
pagina('carrito/index.html', 'Carrito · Masherr', 'Revisá tu pedido y envialo por WhatsApp a Masherr.', carrito, scripts=['carrito.js'], indexar=False)

# ---------------------------------------------------------------- Empresas
empresas = f"""
<section class="hero oscuro" style="padding-bottom:56px" aria-labelledby="t-emp">
  <div class="rayas" aria-hidden="true"></div>
  <div class="contenedor"><p class="rotulo">Empresas, industria y obra</p><h1 id="t-emp" style="font-size:clamp(36px,7vw,64px)">Contanos qué tenés que resolver.</h1>
    <p class="bajada">Completá el pedido y te respondemos por WhatsApp con disponibilidad y cotización. Cada cotización se confirma según stock y condiciones vigentes.</p></div>
</section>
<section class="seccion"><div class="contenedor" style="max-width:860px">
  <form id="form-empresas" class="form-grid dos" novalidate>
    <div class="campo"><label for="emp-nombre">Nombre y apellido *</label><input id="emp-nombre" name="nombre" autocomplete="name" required></div>
    <div class="campo"><label for="emp-empresa">Empresa</label><input id="emp-empresa" name="empresa" autocomplete="organization"></div>
    <div class="campo"><label for="emp-cuit">CUIT (si necesitás factura)</label><input id="emp-cuit" name="cuit" inputmode="numeric"></div>
    <div class="campo"><label for="emp-mail">Email</label><input id="emp-mail" name="email" type="email" autocomplete="email"></div>
    <div class="campo entero"><label for="emp-tarea">¿Qué tarea o trabajo tienen que resolver? *</label><textarea id="emp-tarea" name="tarea" required aria-describedby="emp-tarea-ayuda"></textarea><span class="ayuda" id="emp-tarea-ayuda">Ej.: mantenimiento de planta, corte de perfiles, obra en seco.</span></div>
    <div class="campo entero"><label for="emp-productos">Productos y cantidades *</label><textarea id="emp-productos" name="productos" required aria-describedby="emp-prod-ayuda"></textarea><span class="ayuda" id="emp-prod-ayuda">Uno por línea. Ej.: 20 discos de corte 115 mm.</span></div>
    <div class="campo"><label for="emp-plazo">¿Para cuándo lo necesitás?</label><input id="emp-plazo" name="plazo" placeholder="Ej.: esta semana"></div>
    <div class="campo"><label for="emp-entrega">Entrega</label><select id="emp-entrega" name="entrega"><option>Retiro en el local</option><option>Envío (a coordinar)</option></select></div>
    <div class="entero"><button class="boton wa" type="submit">{ic('whatsapp')}Enviar consulta por WhatsApp</button>
      <p class="ayuda" style="margin-top:10px">Se abre WhatsApp con tu consulta armada. No guardamos estos datos en la web.</p></div>
  </form>
</div></section>"""
pagina('empresas/index.html', 'Empresas · Masherr', 'Cotizaciones para empresas, industria y obra. Contanos la tarea, los productos y el plazo.', empresas, actual='empresas/', scripts=['empresas.js'])

# ---------------------------------------------------------------- Nosotros
nosotros = f"""
<section class="hero oscuro" aria-labelledby="t-nos">
  <div class="rayas" aria-hidden="true"></div>
  <div class="contenedor"><p class="rotulo">Nosotros</p><h1 id="t-nos">Una ferretería con historia.</h1>
    <p class="bajada">Masherr es una ferretería industrial de Villa Lynch, San Martín. Abastecemos a industrias, talleres, profesionales y particulares con herramientas, máquinas e insumos, y con el criterio para elegirlos.</p></div>
</section>
<section class="seccion"><div class="contenedor dos-col">
  <div><p class="rotulo">Cómo trabajamos</p><h2 class="titulo-seccion">Primero entendemos el trabajo. Después elegimos la herramienta.</h2>
    <p class="bajada">Preguntamos qué material vas a trabajar, con qué frecuencia y en qué condiciones. Con eso comparamos opciones y te recomendamos la que conviene, no la más cara.</p></div>
  <ul class="pasos" style="grid-template-columns:1fr">
    <li><b>Escuchamos</b><p>Qué tenés que resolver, en qué material y con qué intensidad de uso.</p></li>
    <li><b>Comparamos</b><p>Opciones por potencia, prestaciones, repuestos y presupuesto.</p></li>
    <li><b>Acompañamos</b><p>Antes y después de la compra, en el local o por WhatsApp.</p></li>
  </ul>
</div></section>
<section class="seccion suave" id="como-comprar" aria-labelledby="t-cc"><div class="contenedor">
  <p class="rotulo">Cómo comprar</p><h2 class="titulo-seccion" id="t-cc">Del carrito a WhatsApp.</h2>
  <ol class="pasos">
    <li><b>Armá tu carrito</b><p>Elegí productos y cantidades en la tienda.</p></li>
    <li><b>Envialo por WhatsApp</b><p>Desde el carrito, completá tus datos y enviá el pedido armado al {e(CFG['whatsapp_visible'])}.</p></li>
    <li><b>Confirmamos</b><p>Revisamos precio y stock, coordinamos retiro o envío y la forma de pago.</p></li>
  </ol>
</div></section>
{bloque_redes('../')}
<section class="seccion" aria-labelledby="t-local"><div class="contenedor dos-col">
  <div><p class="rotulo">El local</p><h2 class="titulo-seccion" id="t-local">Vení a vernos.</h2>
    <p class="bajada">{e(CFG['direccion'])}<br>{e(CFG['localidad'])}</p>
    <p><a class="boton" href="{e(CFG['mapa'])}" target="_blank" rel="noopener">{ic('ubicacion')}Cómo llegar</a></p></div>
  <ul class="valores" style="border-color:var(--linea)">
    <li style="border-color:var(--linea)"><b>Teléfono</b><a href="tel:+541147525210">{e(CFG['telefono'])}</a></li>
    <li style="border-color:var(--linea)"><b>WhatsApp</b><a href="https://wa.me/{CFG['whatsapp']}" target="_blank" rel="noopener">{e(CFG['whatsapp_visible'])}</a></li>
    {f'<li style="border-color:var(--linea)"><b>Horarios</b>{e(CFG["horarios"])}</li>' if CFG['horarios'] else ''}
  </ul>
</div></section>"""
pagina('nosotros/index.html', 'Nosotros · Masherr', 'Masherr, ferretería industrial de Villa Lynch, San Martín. Asesoramiento técnico para elegir bien.', nosotros, actual='nosotros/')

# ---------------------------------------------------------------- 404, sitemap
pagina('404.html', 'Página no encontrada · Masherr', 'No encontramos esta página.', f"""<section class="seccion"><div class="contenedor"><h1>No encontramos esta página.</h1>
<p class="bajada">Puede que el producto ya no esté publicado. Buscalo en la tienda o consultanos.</p>
<p><a class="boton" href="/tienda/">Ir a la tienda</a></p></div></section>""", indexar=False)
if CFG['dominio']:
    d = CFG['dominio'].rstrip('/')
    urls = ['', 'tienda/', 'empresas/', 'nosotros/'] + [f'producto/{p["slug"]}/' for p in productos]
    (SITIO / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{d}/{u}</loc></url>\n' for u in urls) + '</urlset>\n')
    (SITIO / 'robots.txt').write_text(f'User-agent: *\nDisallow: /carrito/\nSitemap: {d}/sitemap.xml\n')
print(f'{len(productos)} productos · {len(cats_usadas)} categorías · {sum(1 for p in productos if p["marca"])} con marca detectada')
