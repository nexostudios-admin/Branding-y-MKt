"""Convierte las filas extraídas del CATÁLOGO TN original en productos.json, agrupados por categoría."""
import json, re, sys, unicodedata
rows = json.load(open(sys.argv[1]))

def norm(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')

CATS = [  # (categoría, palabras clave) — el orden importa
 ('Soldadura', ['soldadora','electrodo','alambre mig','mascara fotosensible','estano','pasta p/estanar']),
 ('Compresores y neumática', ['compresor','neumatic','inflador','pistola para inflar','arenador','pistola de pintar']),
 ('Taller y equipamiento', ['taladro de banco','amoladora de banco','crique carro','crique carrito','caballetes','aparejo','morsa','banqueta','calefactor']),
 ('Herramientas eléctricas', ['taladro','rotomartillo','amoladora','caladora','sierra circular','sierra sensitiva','sierra ingletadora','sierra de mano','cepillo electrico','lijadora','lustra','mini torno','minitorno','pistola de calor','atornillador inal','atornillador elec','atornillador para durlock','atornillado para durlock','multiherramienta','fresadora','termofusora','llave de impacto','llave y atornillador de impacto','combo inalambrico','bateria de litio','cargador de baterias','engrampadora electrica']),
 ('Discos, brocas y accesorios', ['disco','copa','broca','cincel','mechas','adaptador','pack puntas','set de puntas','juego 40 puntas','vasos magneticos']),
 ('Medición y nivelación', ['cinta metrica','nivel','medidor','chocla','escuadras','detector']),
 ('Almacenamiento y transporte', ['caja de herramientas','bolso','packout','carro de herramientas']),
 ('Agua, limpieza y jardín', ['bomba','hidrolavadora','aspiradora','sopladora','bordeadora','cortadora de cesped','manguera']),
 ('Construcción', ['carretilla','hormigonera','carro de carga','balde','pico ','pala ','escalera','cortadora de ceramica','cuchara de albanil','sopapa']),
 ('Seguridad e indumentaria', ['anteojo','guante','protector','casco','malla','cinta de peligro','cono','limpiamanos']),
 ('Adhesivos, lubricantes y pintura', ['adhesivo','espuma','cola ','diluyente','lubricante','aerosol','barniz','kit para pintor']),
 ('Fijaciones y ferretería', ['clavos','grampa','precinto','cable de acero','guardacabo','cadena','tensor','engrampadora']),
 ('Herramientas de mano', ['']),
]

def clean(s, quotes=True):
    s = re.sub(r'\s+', ' ', s or '').strip()
    return s.strip('"“”').strip() if quotes else s

def short(desc, n=210):
    d = clean(desc)
    m = re.match(r'(.{40,}?[.!])\s', d + ' ')
    s = m.group(1) if m and len(m.group(1)) <= n else d
    if len(s) > n:
        s = s[:n].rsplit(' ', 1)[0].rstrip(',;:-') + '…'
    return s

out = []
for r in rows:
    c = r['cells']
    name = re.sub(r'^PRODUCTO\s+', '', clean(c[0], quotes=False))
    brand = re.sub(r'^MARCA\s+', '', clean(c[1]))
    price = re.sub(r'^VALOR\s+', '', clean(c[4]))
    if not name: continue
    p = re.sub(r'[^\d,]', '', price).split(',')[0]
    n = norm(name)
    cat = next(k for k, kws in CATS if any(w in n for w in kws))
    out.append({'categoria': cat, 'producto': name, 'marca': brand,
                'incluye': clean(c[2]), 'descripcion': short(c[3]),
                'descripcion_completa': clean(c[3]),
                'precio': int(p) if p else None})
order = [k for k, _ in CATS]
out.sort(key=lambda x: order.index(x['categoria']))  # sort estable: respeta el orden original dentro de cada categoría
json.dump(out, open('productos.json', 'w'), ensure_ascii=False, indent=1)
from collections import Counter
for k, v in Counter(x['categoria'] for x in out).items(): print(v, k)
print(len(out), 'sin precio:', [x['producto'] for x in out if not x['precio']])
