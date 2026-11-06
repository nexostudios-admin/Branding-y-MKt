"""Reporte de validación de la copia del catálogo Tiendanube (y cruce con el PDF CATÁLOGO TN).

Uso: python3 validar.py snapshot.json ../../catalogo/productos.json reporte.md
"""
import json, re, sys, unicodedata
from collections import Counter, defaultdict

def norm(s):
    s = ''.join(c for c in unicodedata.normalize('NFD', (s or '').lower()) if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()

snap = json.load(open(sys.argv[1]))
pdf = json.load(open(sys.argv[2]))
P = snap['productos']
V = [(p, v) for p in P for v in p['variantes']]

def lista(items, n=15):
    items = list(items)
    out = ''.join(f'- {x}\n' for x in items[:n])
    return out + (f'- … y {len(items) - n} más\n' if len(items) > n else '')

sin_sku = [p for p in P if any(not v['sku'] for v in p['variantes'])]
skus = Counter(v['sku'] for _, v in V if v['sku'])
sku_dup = [s for s, n in skus.items() if n > 1]
nombres = defaultdict(list)
for p in P: nombres[norm(p['nombre'])].append(p['url'])
nom_dup = {k: v for k, v in nombres.items() if len(v) > 1}
sin_img = [p for p in P if not p['imagenes']]
img_ia = [p for p in P if any(re.search(r'gemini|chatgpt|dall-?e|midjourney|ai[-_]generated', i, re.I) for i in p['imagenes'])]
sin_precio = [p for p in P if any(v['precio'] in (None, 0) for v in p['variantes'])]
sin_stock = [p for p in P if all(v['stock'] == 0 or v['disponible'] is False for v in p['variantes'])]
stock_ilim = [p for p in P if any(v['stock'] is None for v in p['variantes'])]
consulta = [p for p in P if any(v['solo_consulta'] for v in p['variantes'])]
con_var = [p for p in P if len(p['variantes']) > 1]
sin_desc = [p for p in P if not p['descripcion']]
sin_marca = [p for p in P if not p['marca']]
monedas = Counter(p['moneda'] for p in P)
cats = Counter(' > '.join(p['categorias'] or ['(sin categoría)']) for p in P)

# Cruce con el PDF: por nombre normalizado
tn_idx = {norm(p['nombre']): p for p in P}
en_ambos, solo_pdf, dif_precio = [], [], []
for x in pdf:
    k = norm(x['producto'] + ' ' + x['marca'])
    p = tn_idx.get(k) or tn_idx.get(norm(x['producto']))
    if not p: solo_pdf.append(x); continue
    en_ambos.append(x)
    precios = {v['precio'] for v in p['variantes']}
    if x['precio'] not in precios:
        dif_precio.append((x['producto'], x['precio'], sorted(precios)))

def m(n): return f'{n:,}'.replace(',', '.')

r = f"""# Reporte de validación del catálogo

Fuente: {snap['fuente']} · copia pública de solo lectura del {snap['fecha']}.
No es una exportación autorizada: confirmar conteos con el admin de Tiendanube antes de importar.

## Conteos

| Dato | Cantidad |
| --- | --- |
| Productos publicados (sitemap) | {len(P)} |
| Variantes | {len(V)} |
| Productos con más de una variante | {len(con_var)} |
| Errores de lectura | {len(snap['errores'])} |
| Páginas de categoría e institucionales | {len(snap['paginas_sitemap'])} |
| Productos en el PDF CATÁLOGO TN | {len(pdf)} |
| Del PDF encontrados en la tienda (por nombre) | {len(en_ambos)} |
| Del PDF sin coincidencia en la tienda | {len(solo_pdf)} |

Monedas: {dict(monedas)}

## Problemas que bloquean o afectan la importación

| Control | Productos | Qué hacer |
| --- | --- | --- |
| Sin SKU en alguna variante | {len(sin_sku)} | Cargar SKU único: es la clave para búsqueda, importación y redirecciones. |
| SKU repetido | {len(sku_dup)} | Corregir antes de importar. |
| Nombre repetido | {len(nom_dup)} | Revisar si son duplicados o variantes de un mismo producto. |
| Sin imagen | {len(sin_img)} | Pedir foto oficial o propia. |
| Imagen con nombre de generador de IA | {len(img_ia)} | Reemplazar por foto real del producto (el brief no admite imágenes sintéticas). |
| Sin precio o precio 0 | {len(sin_precio)} | Desactivar compra hasta tener precio. |
| Sin stock / no disponible | {len(sin_stock)} | Mostrar “Sin stock” y bloquear compra. |
| Stock sin controlar (null) | {len(stock_ilim)} | Definir si se controla stock; si no, riesgo de sobreventa. |
| Solo consulta (sin precio visible) | {len(consulta)} | Mantener como “Consultar”. |
| Sin descripción | {len(sin_desc)} | Completar. |
| Sin marca como dato propio | {len(sin_marca)} | La marca está solo en el nombre; cargarla como campo para poder filtrar. |

### Sin SKU
{lista(p['nombre'] for p in sin_sku)}
### Nombres repetidos
{lista(f"{k}: {len(v)} fichas" for k, v in nom_dup.items())}
### Imágenes con nombre de generador de IA
{lista(p['nombre'] for p in img_ia)}
### Sin stock o no disponibles
{lista(p['nombre'] for p in sin_stock)}
### Precio distinto entre el PDF y la tienda
{lista(f"{a}: PDF ${m(b)} · tienda {', '.join('$' + m(c) for c in cs if c)}" for a, b, cs in dif_precio)}
### Del PDF sin coincidencia en la tienda (muestra)
{lista(f"{x['producto']} ({x['marca']})" for x in solo_pdf)}
## Categorías en la tienda

| Categoría | Productos |
| --- | --- |
""" + ''.join(f'| {k} | {v} |\n' for k, v in sorted(cats.items())) + """
## Campos que la tienda no publica (quedan como desconocidos)

Dimensiones, garantía, accesorios incluidos y atributos técnicos estructurados. Pedirlos en la exportación del admin o cargarlos en Tiendanube; no inferirlos.
"""
open(sys.argv[3], 'w').write(r)
print(r[:1800])
