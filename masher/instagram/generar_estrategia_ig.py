"""Estrategia de contenido para Instagram (PDF vertical con branding Masherr).
Uso: python3 generar_estrategia_ig.py && node exportar_estrategia_ig.js
"""
import html
from pathlib import Path

AQUI = Path(__file__).parent
e = lambda s: html.escape(s, quote=True)
CONT = AQUI.parent / 'contenido'

def placa(n):
    return f'<img class="mini" src="png/Masherr_{n}.png" alt="">'

COPYS = [
 ('post_01_guido', 'Presentación de Guido', 'Soy Guido, de Masherr. Desde el mostrador de la ferretería de mi familia, en Villa Lynch, te ayudo a elegir la herramienta justa para tu trabajo. Contame qué tenés que hacer y lo resolvemos. 📍 Calle 38 4335 · 💬 WhatsApp en la bio'),
 ('post_02_amoladora', 'Producto de la semana', 'Amoladora angular 115 mm Vanden, 650 W: liviana y precisa para cortes y terminaciones en hierro, chapa y cerámica. Precio y stock en la web (link en la bio) o consultanos por WhatsApp.'),
 ('post_03_comparativa', 'Comparativa', '¿115 o 180? La de 115 es para cortes finos y terminaciones; la de 180, para cortes profundos y desbaste pesado. ¿Cuál necesitás? Contanos qué vas a cortar y te recomendamos. Guardá este post 🔖'),
 ('post_04_resena', 'Reseña real', 'Lo que más nos importa: que te vayas con lo que necesitás. Gracias Lorena por tu reseña ⭐ Somos 4,7 en Google con 131 opiniones. ¿Ya nos dejaste la tuya?'),
 ('post_05_combo', 'Combo', 'Tu primera caja de herramientas, completa: bolso rígido Emtop + 3 pinzas + set de 43 piezas con crique, puntas y tubos. Todo junto en un solo combo. Consultá el precio en la web o por WhatsApp.'),
 ('post_06_consejo', 'Consejo de ferretero', 'Consejo de ferretero #01: no uses el mismo destornillador para todo. La punta justa evita pelar el tornillo (y renegar después). Tenemos juegos para cada tipo de tornillo. Mandale este post a quien usa un cuchillo de destornillador 😅'),
 ('post_07_soldadora', 'Producto', 'Soldadora inverter Pegaso SI 140: compacta, portátil y simple para empezar a soldar con electrodo. Consultá precio por WhatsApp o vení a verla al local y te explicamos cómo usarla. Siempre con máscara 👀'),
 ('post_08_como_comprar', 'Cómo comprar', 'Comprar en Masherr es así: 1) entrá a masherrferreteria.com.ar 2) agregá lo que necesitás al carrito 3) envialo por WhatsApp. Te confirmamos precio, stock y retiro. Link en la bio.'),
 ('post_09_empresas', 'Empresas', '¿Tu taller no puede frenar? Mandanos la lista de lo que necesitás y te cotizamos: herramientas, insumos y equipos para industrias, talleres y obra. WhatsApp 11 3182-6166.'),
]

P = []
P.append(('La idea', 'VENDER CON CARA Y CRITERIO.', '''<p class="lead">Instagram de Masherr no es un catálogo: es el mostrador abierto. Cada publicación muestra un producto real, una persona real (Guido) o un cliente real, y termina con un paso para comprar.</p>
<table class="tabla estructura"><tr><th>Principio</th><th>Cómo se ve</th></tr>
<tr><td>Humanizado</td><td>Guido habla en primera persona, la familia, el local, las reseñas de clientes.</td></tr>
<tr><td>Minimalista</td><td>Fondo blanco, gris claro o negro; una sola idea por placa; mucho aire. Sin precios en las placas.</td></tr>
<tr><td>Orientado a venta</td><td>Producto grande y siempre un llamado: “Consultá precio y stock” en la web, WhatsApp o el local.</td></tr>
<tr><td>Coherente</td><td>Mismos colores, tipografía, logo y pie en todas las piezas.</td></tr></table>'''))
P.append(('Pilares', 'CINCO TIPOS DE CONTENIDO.', '''<table class="tabla"><tr><th>Pilar</th><th>Para qué</th><th>% del mes</th></tr>
<tr><td><b>Producto con precio</b></td><td>Vender: producto de la semana, combos, ingresos.</td><td>35 %</td></tr>
<tr><td><b>Asesoramiento</b></td><td>Mostrar criterio: comparativas, consejos de ferretero, mitos.</td><td>25 %</td></tr>
<tr><td><b>Personas</b></td><td>Generar confianza: Guido, la familia, el local, detrás de escena.</td><td>15 %</td></tr>
<tr><td><b>Prueba social</b></td><td>Reseñas reales de Google y clientes contentos (con permiso).</td><td>15 %</td></tr>
<tr><td><b>Cómo comprar / empresas</b></td><td>Explicar la web, el pedido por WhatsApp y las cotizaciones.</td><td>10 %</td></tr></table>
<div class="nota"><span>Los <b>reels</b> del plan de 15 videos y del guion de rodaje alimentan los mismos pilares: una placa y un reel del mismo tema se refuerzan entre sí.</span></div>'''))
P.append(('Diseño', 'REGLAS DE DISEÑO.', '''<table class="tabla cols"><tr><td>Formatos</td><td>Post 1080 × 1350 (4:5, ocupa más pantalla) · Story 1080 × 1920.</td></tr>
<tr><td>Colores</td><td>Azul #17256B, negro #08090B, blanco y gris #EEF0F4. Celeste #9AAEFF solo sobre fondo oscuro.</td></tr>
<tr><td>Tipografía</td><td>DejaVu Sans Condensed Bold para títulos, DejaVu Sans para textos.</td></tr>
<tr><td>Producto</td><td>Sobre gris claro, grande, sin sombras ni efectos. Sin precio: botón azul “Consultá precio y stock”.</td></tr>
<tr><td>Rótulo</td><td>Línea + palabra en mayúsculas arriba: PRODUCTO DE LA SEMANA, CONSEJO, COMBO.</td></tr>
<tr><td>Pie</td><td>Logo + llamado a la acción, siempre en el mismo lugar.</td></tr>
<tr><td>Fotos</td><td>Reales: Guido, el local, productos en el mostrador. Sin imágenes generadas.</td></tr>
<tr><td>Grilla</td><td>Alternar claro / oscuro / azul para que el perfil se vea ordenado.</td></tr></table>
<div class="nota"><span>Evitar: fondos con degradados, muchas tipografías, textos largos en la placa, estrellas de “oferta” y colores fuera de la paleta.</span></div>'''))
P.append(('Grilla', 'LAS 9 PLACAS DEL PRIMER MES.', '<div class="grilla">' + ''.join(placa(n) for n, _, _ in COPYS) + '</div><p class="ayuda">Así se ve el perfil: claro, oscuro y azul alternados. La placa 01 lleva una foto real de Guido en el mostrador (el espacio está marcado).</p>'))
for i in range(0, len(COPYS), 3):
    bloque = ''.join(f'<div class="copy">{placa(n)}<div><b>{e(t)}</b><p>{e(c)}</p></div></div>' for n, t, c in COPYS[i:i + 3])
    P.append(('Textos', 'TEXTOS PARA PUBLICAR.' if i == 0 else 'TEXTOS (CONTINUACIÓN).', bloque))
P.append(('Stories', 'STORIES TODOS LOS DÍAS.', '<div class="grilla st">' + ''.join(placa(n) for n in ['story_s1_producto', 'story_s2_encuesta', 'story_s3_resenas']) + '''</div>
<ol class="pasos"><li><b>Producto con sticker de enlace</b> a la ficha en la web (reemplazar el recuadro punteado por el sticker).</li>
<li><b>Encuesta o pregunta</b> para generar conversación; responder al día siguiente con un video de Guido.</li>
<li><b>Reseñas</b> con sticker de enlace a g.page/r/CSTh9aafPrTYEBE/review.</li>
<li>Destacadas: <b>Productos · Cómo comprar · Reseñas · Empresas · El local</b>.</li></ol>'''))
P.append(('Calendario', 'RITMO SEMANAL.', '''<table class="tabla"><tr><th>Día</th><th>Feed</th><th>Stories</th></tr>
<tr><td><b>Lunes</b></td><td>Producto de la semana (placa)</td><td>Producto + enlace</td></tr>
<tr><td><b>Martes</b></td><td>—</td><td>Encuesta / pregunta</td></tr>
<tr><td><b>Miércoles</b></td><td>Reel (asesoramiento o humor)</td><td>Respuesta de Guido</td></tr>
<tr><td><b>Jueves</b></td><td>—</td><td>Detrás de escena del local</td></tr>
<tr><td><b>Viernes</b></td><td>Placa: consejo, reseña o combo</td><td>Reseñas + enlace</td></tr>
<tr><td><b>Sábado</b></td><td>—</td><td>“Abrimos hasta las 12:30”</td></tr></table>
<p class="lead" style="margin-top:12px">Total: 2 placas + 1 reel por semana en el feed y stories todos los días hábiles. Es un ritmo sostenible para un comercio.</p>'''))
P.append(('Venta', 'DE LA PUBLICACIÓN A LA VENTA.', '''<ol class="pasos"><li><b>Link en la bio:</b> masherrferreteria.com.ar (la tienda y el carrito).</li>
<li><b>Botón de WhatsApp</b> en el perfil (perfil de empresa → Botones de acción).</li>
<li><b>Sin precios en las placas:</b> el botón “Consultá precio y stock” lleva a la web o al WhatsApp. A cada “¿precio?” en comentarios, responder por mensaje privado con el link del producto: abre la conversación de venta.</li>
<li><b>Responder comentarios y mensajes</b> en el día, como Guido, con el link del producto.</li>
<li><b>Etiquetas de producto</b> de Instagram Shopping: opcional más adelante.</li></ol>
<table class="tabla" style="margin-top:8px"><tr><th>Qué medir cada mes</th><th>Dónde</th></tr>
<tr><td>Guardados, compartidos y alcance de cada placa</td><td>Estadísticas de Instagram</td></tr>
<tr><td>Clics en el link y en WhatsApp</td><td>Instagram + Google Analytics (origen: instagram)</td></tr>
<tr><td>Pedidos que llegan desde el carrito</td><td>WhatsApp</td></tr></table>'''))
P.append(('Producción', 'CÓMO SEGUIR CREANDO PLACAS.', '''<ol class="pasos"><li><b>Fotos de Guido:</b> una sesión de 30 minutos en el local, con luz de día. 15 fotos alcanzan para 2 meses (mostrador, góndolas, con herramienta en mano, con clientes con permiso).</li>
<li><b>Producto nuevo:</b> me pasás el nombre (o lo cargás en la planilla) y genero la placa con el mismo diseño.</li>
<li><b>Reseñas:</b> elegir las mejores de Google; usar solo el nombre de pila.</li>
<li><b>Precios:</b> no van en las placas; mantenerlos actualizados en la planilla para que la web muestre el valor correcto.</li></ol>
<div class="nota"><span>Las placas se generan automáticamente a partir de los datos de la web, así que sumar un producto lleva minutos y siempre respeta el branding.</span></div>'''))

TOTAL = 1 + len(P)
def pagina(n, cab, tit, cuerpo):
    return f'''<section class="hoja"><div class="cab"><img src="../catalogo/img/masher-logo-azul.png" alt="Masherr"><span>{e(cab)}</span></div>
<div class="cuerpo"><div class="rotulo">{e(cab)}</div><h2>{e(tit)}</h2>{cuerpo}</div>
<div class="pie"><span>Masherr · Instagram</span><b>{n:02d} / {TOTAL:02d}</b></div></section>'''
pags = ['''<section class="hoja oscura"><div class="barra"></div><div class="sup">MASHERR / INSTAGRAM</div>
<img class="logo" src="../catalogo/img/masher-logo-blanco.png" alt="Masherr"><div class="rayas"></div>
<div class="eyebrow rotulo">Estrategia de contenido · placas y stories</div>
<h1>EL MOSTRADOR,<br>ABIERTO EN<br>INSTAGRAM.</h1>
<p class="bajada">Contenido humano, minimalista y pensado para vender: placas listas, textos y calendario.</p>
<div class="pie-t"><span>@masherrferreteria</span><b>masherrferreteria.com.ar</b></div></section>''']
for i, (cab, tit, cuerpo) in enumerate(P, 2):
    pags.append(pagina(i, cab, tit, cuerpo))
CSS = (CONT / 'estilo.css').read_text().replace('../catalogo/', '../catalogo/') + '''
.cols td:first-child { font-family: "Cond"; font-size: 17px; color: var(--azul); white-space: nowrap; width: 110px; }
.estructura td:first-child { width: 150px; }
.grilla { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin: 6px 0 12px; }
.grilla .mini { width: 100%; display: block; }
.grilla.st .mini { width: 100%; }
.copy { display: grid; grid-template-columns: 150px 1fr; gap: 16px; padding: 12px 0; border-bottom: 1px solid var(--linea); }
.copy .mini { width: 150px; }
.copy b { font-family: "Cond"; color: var(--azul); font-size: 18px; }
.copy p { font-size: 15.5px; line-height: 1.5; margin-top: 4px; }
.oscura h1 { font-size: 72px; }
'''
(AQUI / 'estrategia_instagram.html').write_text(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Masherr · Instagram</title><style>{CSS}</style></head><body>{"".join(pags)}</body></html>')
print(TOTAL, 'páginas')
