"""Guía de SEO local (web + ficha de Google) con el branding de Masherr.
Uso: python3 generar_seo.py && node exportar_seo.js
"""
import html
from pathlib import Path

AQUI = Path(__file__).parent
e = lambda s: html.escape(s, quote=True)

DESCRIPCION = ('Masherr es una ferretería industrial de Villa Lynch, San Martín. Abastecemos a industrias, talleres, '
               'profesionales del mantenimiento y la construcción, y también a particulares. Trabajamos herramientas eléctricas '
               'e inalámbricas, herramientas de mano, soldadoras y compresores, discos, brocas, medición, adhesivos y artículos de '
               'ferretería, de marcas como Bosch, DeWalt, Stanley, Milwaukee y Emtop. Te asesoramos para elegir la herramienta '
               'correcta según el trabajo. Podés ver el catálogo en nuestra web, armar tu pedido y cerrarlo por WhatsApp, o pasar por el local.')
assert len(DESCRIPCION) <= 750, len(DESCRIPCION)

PAGINAS = [
 ('Cómo funciona', 'QUE TE ENCUENTREN CERCA.', f'''<p class="lead">Cuando alguien busca “ferretería industrial”, “amoladora” o “soldadora” cerca de San Martín, Google muestra primero un mapa con 3 negocios y después las webs. Para aparecer ahí cuentan tres cosas:</p>
<table class="tabla estructura"><tr><th>Factor</th><th>Qué significa</th></tr>
<tr><td>Relevancia</td><td>Que la ficha y la web digan claramente qué vendés: categorías, productos y descripción.</td></tr>
<tr><td>Distancia</td><td>Qué tan cerca está el local de quien busca. No se cambia, pero la dirección tiene que estar perfecta.</td></tr>
<tr><td>Prominencia</td><td>Reseñas, fotos, publicaciones y que el negocio aparezca igual en todos lados.</td></tr></table>
<div class="rotulo" style="margin-top:14px">Ya hecho en la web</div>
<ol class="pasos"><li>Títulos con la ubicación: “Ferretería industrial en Villa Lynch, San Martín”.</li>
<li>10 páginas de categoría: “Herramientas eléctricas en San Martín”, “Soldadura y compresores en San Martín”…</li>
<li>Datos del negocio para Google (dirección, teléfono, WhatsApp, redes, zona).</li>
<li>Zona de atención y mapa en “Nosotros”, y mapa del sitio con 258 páginas.</li></ol>'''),

 ('Paso 1 · La ficha', 'CREAR O RECLAMAR LA FICHA.', '''<ol class="pasos"><li>Entrá a <b>business.google.com</b> con <b>redesmasherr@gmail.com</b>.</li>
<li>Buscá “Masherr”. Si la ficha <b>ya existe</b> (la creó un cliente o Google), tocá <b>Reclamar este negocio</b>. Si <b>no existe</b>, tocá <b>Agregar negocio</b>.</li>
<li>Tipo de negocio: <b>local físico</b> que recibe clientes. Marcá también que hacés envíos si los hacen.</li>
<li>Completá los datos de la página siguiente <b>exactamente igual</b> en todos lados.</li>
<li><b>Verificación:</b> Google elige el método (video del local y del cartel, llamada, SMS o mail). El video suele pedir: cartel con el nombre, la calle, el interior y algo que pruebe que es tuyo (abrir la caja o la persiana).</li></ol>
<div class="nota"><span><b>Importante:</b> hasta que la ficha esté verificada, los cambios no se publican. Si aparece una ficha duplicada (por ejemplo con el número 4349), se pide unificar desde la misma ficha con <b>Sugerir un cambio → Cerrado o eliminado → Duplicado</b>.</span></div>'''),

 ('Paso 2 · Datos', 'LOS MISMOS DATOS EN TODOS LADOS.', '''<p class="lead">Google confía más en un negocio cuando el nombre, la dirección y el teléfono coinciden en la ficha, la web y las redes.</p>
<table class="tabla cols"><tr><td>Nombre</td><td>El del cartel del local, sin agregar palabras (ej.: <b>Masherr Ferretería Industrial</b>). Agregar “San Martín” o “herramientas” al nombre está prohibido por Google.</td></tr>
<tr><td>Dirección</td><td>Calle 38 (ex Hipólito Yrigoyen) 4335, Villa Lynch, Buenos Aires. <mark>Confirmar el número:</mark> algunas guías dicen 4349.</td></tr>
<tr><td>Teléfono</td><td>011 4752-5210 (principal) · WhatsApp +54 9 11 3182-6166 (adicional)</td></tr>
<tr><td>Sitio web</td><td>https://masherrferreteria.com.ar</td></tr>
<tr><td>Horario</td><td><mark>A confirmar.</mark> Cargar el real y los feriados. Un horario mal cargado genera reseñas negativas.</td></tr>
<tr><td>Atributos</td><td>Retiro en el local, envíos (si hay), medios de pago aceptados.</td></tr></table>'''),

 ('Paso 3 · Categorías', 'CATEGORÍAS Y DESCRIPCIÓN.', f'''<div class="rotulo">Categorías</div>
<ol class="pasos"><li><b>Principal:</b> <b>Ferretería</b>. Es la que más pesa: elegí una sola.</li>
<li><b>Secundarias</b> (hasta 9): tienda de herramientas, proveedor de suministros industriales, tienda de equipos de soldadura. Escribí y elegí la opción más parecida que ofrezca Google.</li></ol>
<div class="rotulo" style="margin-top:10px">Descripción para copiar ({len(DESCRIPCION)} de 750 caracteres)</div>
<div class="copiar">{e(DESCRIPCION)}</div>
<p class="ayuda">Google no permite links ni promociones en la descripción: por eso dice “nuestra web” y no la dirección.</p>'''),

 ('Paso 4 · Productos', 'PRODUCTOS Y SERVICIOS.', '''<p class="lead">En la ficha hay una sección de productos. Cargá una por categoría, con foto, “Desde $” y el botón <b>Más información</b> apuntando a la página de esa categoría en la web.</p>
<table class="tabla"><tr><th>Producto en la ficha</th><th>Link</th></tr>
<tr><td>Herramientas eléctricas</td><td>masherrferreteria.com.ar/categoria/herramientas-electricas/</td></tr>
<tr><td>Inalámbricas a batería</td><td>…/categoria/inalambricas/</td></tr>
<tr><td>Soldadura y compresores</td><td>…/categoria/maquinas/</td></tr>
<tr><td>Discos, brocas y puntas</td><td>…/categoria/accesorios/</td></tr>
<tr><td>Herramientas manuales</td><td>…/categoria/herramientas-manuales/</td></tr>
<tr><td>Medición y nivelación</td><td>…/categoria/medicion/</td></tr>
<tr><td>Agua, limpieza y jardín</td><td>…/categoria/agua-jardin/</td></tr></table>
<div class="rotulo">Servicios</div>
<p class="ayuda" style="font-size:17px;color:var(--tinta)">Asesoramiento técnico · Pedidos y cotizaciones para empresas · Retiro en el local · Pedidos por WhatsApp</p>'''),

 ('Paso 5 · Fotos', 'FOTOS REALES, SEGUIDO.', '''<p class="lead">Las fichas con fotos reales y nuevas reciben más visitas y llamados. Subí desde el celular, con buena luz.</p>
<ol class="pasos"><li><b>Fachada y cartel</b> (de día, desde la vereda): sirve para que te encuentren al llegar.</li>
<li><b>Interior</b>: mostrador, góndolas, depósito.</li>
<li><b>Equipo</b>: Guido y la familia atendiendo (con su permiso).</li>
<li><b>Productos</b>: los mismos de los reels, en el local.</li>
<li><b>Logo</b> (el original) y <b>portada</b>.</li></ol>
<div class="nota"><span><b>Ritmo:</b> 3 a 5 fotos por semana. Nada de fotos de internet ni imágenes generadas: Google las puede quitar.</span></div>'''),

 ('Paso 6 · Novedades', 'PUBLICAR CADA SEMANA.', '''<p class="lead">La ficha permite publicar novedades, como en Instagram. Reutilizá los reels del plan: mismo producto, mismo mensaje.</p>
<ol class="pasos"><li><b>Una publicación por semana</b>: foto o video corto + 2 o 3 líneas.</li>
<li><b>Botón:</b> “Más información” a la categoría o el producto en la web, o “Llamar”.</li>
<li><b>Temas:</b> producto de la semana, comparativa (amoladora 115 vs 180), llegó al local, consejo de ferretero, pedidos para empresas.</li></ol>
<div class="copiar"><b>Ejemplo:</b> ¿Amoladora de 115 o de 180? La de 115 es para cortes finos y terminaciones; la de 180, para desbaste pesado. Vení a verlas a Villa Lynch o mirá todas en la web. → Más información</div>'''),

 ('Paso 7 · Reseñas', 'PEDIR RESEÑAS.', '''<p class="lead">Las reseñas son lo que más ayuda a subir en el mapa. La clave es pedirlas siempre, en el momento justo.</p>
<ol class="pasos"><li>En la ficha, tocá <b>Pedir reseñas</b> y copiá el link corto.</li>
<li><b>QR en el mostrador</b> con ese link (te lo armo con el branding).</li>
<li><b>Por WhatsApp</b>, después de cada venta que cerró bien:</li></ol>
<div class="copiar">¡Gracias por comprar en Masherr! Si te atendimos bien, ¿nos dejás una reseña en Google? Nos ayuda mucho a que otros nos encuentren: [link]</div>
<div class="nota ojo" style="margin-top:12px"><span><b>Prohibido por Google:</b> ofrecer descuentos o regalos a cambio de reseñas, pedir solo reseñas positivas o que las escriba el equipo. Pueden borrar las reseñas o suspender la ficha.</span></div>'''),

 ('Paso 7 · Respuestas', 'RESPONDER TODAS.', '''<p class="lead">Responder todas las reseñas, buenas y malas, en menos de 48 horas. Firmar como “Guido, de Masherr”.</p>
<div class="rotulo">Reseña positiva</div>
<div class="copiar">¡Gracias, [nombre]! Nos alegra que la [amoladora / soldadora] te haya servido. Cualquier duda con el uso, escribinos. Te esperamos en el local. Guido, de Masherr.</div>
<div class="rotulo" style="margin-top:12px">Reseña negativa</div>
<div class="copiar">Hola, [nombre]. Lamentamos que la experiencia no haya sido buena. Queremos entender qué pasó y resolverlo: escribinos al WhatsApp +54 9 11 3182-6166 o pasá por el local y lo vemos juntos. Guido, de Masherr.</div>
<p class="ayuda">Nunca discutir en público ni dar datos del cliente. Si una reseña es falsa o de alguien que nunca compró, se puede denunciar desde la ficha.</p>'''),

 ('Paso 8 · Coherencia', 'EL MISMO NEGOCIO EN TODOS LADOS.', '''<table class="tabla"><tr><th>Dónde</th><th>Qué revisar</th></tr>
<tr><td>Instagram y TikTok</td><td>Link en la bio: masherrferreteria.com.ar · categoría “Ferretería” · dirección y teléfono.</td></tr>
<tr><td>Facebook</td><td>Mismos datos y link a la web.</td></tr>
<tr><td>WhatsApp Business</td><td>Perfil con dirección, horario, web y catálogo.</td></tr>
<tr><td>Bing Places</td><td>Se puede importar la ficha de Google (bingplaces.com).</td></tr>
<tr><td>Apple (Mapas de iPhone)</td><td>Apple Business Connect: mismos datos.</td></tr>
<tr><td>Guías online</td><td>Páginas Amarillas y similares: corregir la dirección donde diga 4349 o “Hipólito Yrigoyen 38”.</td></tr></table>'''),

 ('Paso 9 · Search Console', 'AVISARLE A GOOGLE DE LA WEB.', '''<p class="lead">Google Search Console muestra qué buscan las personas antes de entrar a la web y avisa si hay problemas. Es gratis.</p>
<ol class="pasos"><li>Entrá a <b>search.google.com/search-console</b> con redesmasherr@gmail.com.</li>
<li>Elegí <b>Prefijo de URL</b> y escribí <b>https://masherrferreteria.com.ar</b>.</li>
<li>En “Otros métodos de verificación”, elegí <b>Etiqueta HTML</b> y copiá solo el código que va entre comillas en <b>content="…"</b>.</li>
<li><b>Mandámelo</b>: lo agrego a la web y te aviso para tocar <b>Verificar</b>.</li>
<li>Después, en <b>Sitemaps</b>, enviá: <b>sitemap.xml</b></li></ol>
<div class="nota"><span>En la ficha de Google, cargá la misma web. Así la ficha y la web se refuerzan entre sí.</span></div>'''),

 ('Rutina', 'UNA RUTINA SIMPLE.', '''<table class="tabla"><tr><th>Cuándo</th><th>Qué hacer</th></tr>
<tr><td>Cada venta</td><td>Pedir la reseña por WhatsApp o con el QR.</td></tr>
<tr><td>Cada semana</td><td>1 publicación en la ficha · 3 a 5 fotos · responder reseñas.</td></tr>
<tr><td>Cada mes</td><td>Revisar en la ficha: llamadas, “cómo llegar” y clics a la web. En Search Console: búsquedas y clics.</td></tr>
<tr><td>Cada cambio</td><td>Horario, feriados o teléfono: actualizar ficha, web y redes el mismo día.</td></tr></table>
<div class="rotulo" style="margin-top:14px">Qué falta confirmar</div>
<ol class="pasos"><li>Número exacto de la dirección (4335 o 4349).</li><li>Horario de atención y si hacen envíos.</li>
<li>Si la ficha de Google ya existe y quién la administra.</li><li>Código de verificación de Search Console.</li></ol>
<p class="ayuda">Los resultados del SEO local se ven en semanas o meses, no en días: depende de las reseñas, de la competencia de la zona y de la constancia.</p>'''),
]

TOTAL = 1 + len(PAGINAS)
def pagina(n, cab, rotulo, titulo, cuerpo):
    return f'''<section class="hoja"><div class="cab"><img src="../catalogo/img/masher-logo-azul.png" alt="Masherr"><span>{e(cab)}</span></div>
<div class="cuerpo"><div class="rotulo">{e(rotulo)}</div><h2>{e(titulo)}</h2>{cuerpo}</div>
<div class="pie"><span>Masherr · SEO local</span><b>{n:02d} / {TOTAL:02d}</b></div></section>'''

pags = ['''<section class="hoja oscura"><div class="barra"></div><div class="sup">MASHERR / SEO LOCAL</div>
<img class="logo" src="../catalogo/img/masher-logo-blanco.png" alt="Masherr máquinas - herramientas"><div class="rayas"></div>
<div class="eyebrow rotulo">Web + Google Maps</div>
<h1>QUE TE<br>ENCUENTREN<br>EN SAN<br>MARTÍN.</h1>
<p class="bajada">Guía paso a paso para la ficha de Google y la web, con textos listos para copiar.</p>
<div class="pie-t"><span>Ferretería industrial</span><b>masherrferreteria.com.ar</b></div></section>''']
for i, (cab, tit, cuerpo) in enumerate(PAGINAS, 2):
    pags.append(pagina(i, cab, cab, tit, cuerpo))

CSS = (AQUI / 'estilo.css').read_text() + '''
mark { background: #FFE58A; color: inherit; padding: 0 3px; }
.cols td:first-child { font-family: "Cond"; font-size: 18px; color: var(--azul); white-space: nowrap; width: 120px; }
.copiar { background: var(--gris); border: 2px dashed var(--azul); padding: 14px 16px; font-size: 17px; line-height: 1.5; }
.copiar b { font-family: "Cond"; color: var(--azul); }
.nota.ojo { border-left-color: #B42318; background: #FDECEA; }
.oscura h1 { font-size: 72px; }
'''
(AQUI / 'guia_seo.html').write_text(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Masherr · SEO local</title><style>{CSS}</style></head><body>{"".join(pags)}</body></html>')
print(TOTAL, 'páginas ·', len(DESCRIPCION), 'caracteres de descripción')
