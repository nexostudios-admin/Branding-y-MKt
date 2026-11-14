"""Estrategia SEO local + Google Ads (SEM) para Masherr, con el branding de la marca.
Uso: python3 generar_estrategia.py && node exportar_estrategia.js
"""
import html
from pathlib import Path

AQUI = Path(__file__).parent
e = lambda s: html.escape(s, quote=True)

P = [
 ('Diagnóstico', 'POR QUÉ HOY APARECE EN EL PUESTO 28.', '''<p class="lead">“Ferretería” es una búsqueda con muchísima competencia: en el partido de San Martín hay decenas de ferreterías. Google ordena el mapa por tres factores:</p>
<table class="tabla estructura"><tr><th>Factor</th><th>Cómo está Masherr</th></tr>
<tr><td>Distancia</td><td><b>No se puede cambiar.</b> Quien busca desde San Martín centro ve primero las ferreterías de su cuadra. Por eso el puesto cambia según dónde esté cada persona.</td></tr>
<tr><td>Relevancia</td><td><b>Ya mejorada:</b> categorías, descripción, servicios, web nueva con página “Ferretería en San Martín”.</td></tr>
<tr><td>Prominencia</td><td><b>Fuerte:</b> 4,7 estrellas con 131 opiniones. Falta: fotos nuevas, publicaciones, reseñas constantes y enlaces a la web.</td></tr></table>
<div class="nota"><span><b>Importante:</b> el “puesto 28” depende de dónde se hizo la búsqueda. Para medir bien, siempre buscar desde el mismo punto (ej.: la puerta del local y la plaza de San Martín) y en modo incógnito, o con una herramienta de grilla geográfica.</span></div>'''),

 ('Objetivos', 'DÓNDE QUEREMOS LLEGAR.', '''<table class="tabla"><tr><th>Búsqueda</th><th>Hoy</th><th>Meta 90 días</th></tr>
<tr><td>“ferretería” cerca de Villa Lynch (radio 1,5 km)</td><td>a medir</td><td>Top 3 del mapa</td></tr>
<tr><td>“ferretería industrial San Martín”</td><td>a medir</td><td>Top 3 del mapa y página 1</td></tr>
<tr><td>“ferretería en San Martín” (todo el partido)</td><td>puesto ~28</td><td>Primera página orgánica + aparecer siempre con Google Ads</td></tr>
<tr><td>Productos: “soldadora / amoladora / compresor San Martín”</td><td>a medir</td><td>Página 1 con la web</td></tr></table>
<p class="lead" style="margin-top:12px">Ser primero en <b>todo</b> el partido solo con SEO no es realista para un local en Villa Lynch: quien busca a 30 cuadras ve las ferreterías cercanas. Para esas búsquedas se usa <b>Google Ads</b>, que sí permite aparecer arriba en toda la zona desde el primer día.</p>'''),

 ('Las dos vías', 'SEO + SEM: CÓMO SE COMBINAN.', '''<div class="dos-vias"><div><b>SEO LOCAL</b><span>Gratis, lento, duradero.</span><ul><li>Ficha de Google completa y activa</li><li>Reseñas todas las semanas</li><li>Web con páginas por búsqueda</li><li>Fotos y publicaciones</li><li>Mismos datos en todos lados</li></ul><i>Resultados: 2 a 6 meses</i></div>
<div><b>SEM (GOOGLE ADS)</b><span>Pago por clic, inmediato.</span><ul><li>Aparecer arriba en búsquedas y en el mapa</li><li>Elegir zona, horario y palabras</li><li>Medir llamadas y WhatsApp</li><li>Se apaga cuando se quiera</li></ul><i>Resultados: desde el día 1</i></div></div>
<div class="nota"><span>La recomendación es <b>las dos a la vez</b>: Ads trae clientes ya, mientras el SEO crece. Cuando la ficha y la web suben solas, se baja el presupuesto de Ads.</span></div>'''),

 ('SEO · Ficha', 'LA FICHA DE GOOGLE: SEMANA A SEMANA.', '''<p class="lead">La base ya está hecha (categorías, descripción, web, WhatsApp, horario, servicios, logo y portada). Lo que mueve el ranking ahora es la <b>actividad</b>.</p>
<table class="tabla"><tr><th>Acción</th><th>Frecuencia</th></tr>
<tr><td><b>Pedir reseñas</b> con la tarjeta, el cartel y el mensaje de WhatsApp. Meta: 3 a 5 nuevas por semana.</td><td>Cada venta</td></tr>
<tr><td><b>Responder todas las reseñas</b> mencionando el producto y “San Martín” cuando sea natural.</td><td>48 h</td></tr>
<tr><td><b>Subir fotos reales</b>: fachada, interior, Guido, productos.</td><td>3 a 5 por semana</td></tr>
<tr><td><b>Publicar una novedad</b> (reutilizar los reels).</td><td>1 por semana</td></tr>
<tr><td><b>Preguntas y respuestas</b>: cargar 5 preguntas frecuentes en la ficha y responderlas.</td><td>Una vez</td></tr>
<tr><td><b>Horario especial</b> en feriados.</td><td>Cada feriado</td></tr></table>
<div class="nota ojo"><span><b>No hacer:</b> agregar “San Martín” o “herramientas” al nombre de la ficha, comprar reseñas o pedirlas a cambio de descuentos. Google lo detecta y puede suspender la ficha.</span></div>'''),

 ('SEO · Web', 'LA WEB: YA HECHO Y PRÓXIMO.', '''<div class="rotulo">Ya hecho</div>
<ol class="pasos"><li>Página <b>masherrferreteria.com.ar/ferreteria-san-martin/</b> con dirección, horario, mapa, categorías y preguntas frecuentes.</li>
<li>10 páginas de categoría (“Herramientas eléctricas en San Martín”…) y 244 fichas de producto.</li>
<li>Datos del negocio para Google, mapa del sitio y títulos con la ubicación.</li>
<li>Medición de clics en Llamar, WhatsApp, Cómo llegar y pedidos (falta conectar Google Analytics).</li></ol>
<div class="rotulo" style="margin-top:10px">Próximo</div>
<ol class="pasos"><li><b>Search Console</b>: verificar la web y enviar el mapa del sitio (necesito el código).</li>
<li><b>Enlaces locales</b>: aparecer en guías y sitios de la zona con link a la web (Cámara de comercio, municipio, proveedores, Páginas Amarillas).</li>
<li><b>Contenido útil</b>: 1 nota por mes en la web a partir de los reels (ej.: “¿Amoladora de 115 o 180?”).</li>
<li><b>Fotos propias</b> en las fichas de producto, en lugar de las de fábrica.</li></ol>'''),

 ('SEM · Campañas', 'GOOGLE ADS: ESTRUCTURA.', '''<table class="tabla"><tr><th>Campaña</th><th>Para qué</th><th>Presupuesto</th></tr>
<tr><td><b>1. Búsqueda local</b></td><td>Aparecer arriba cuando buscan “ferretería en San Martín”, “ferretería industrial”, “ferretería cerca”. Anuncio con dirección, llamada y WhatsApp.</td><td>60 %</td></tr>
<tr><td><b>2. Búsqueda productos</b></td><td>“soldadora inverter San Martín”, “amoladora”, “compresor”, “hidrolavadora”. Lleva a la categoría de la web.</td><td>30 %</td></tr>
<tr><td><b>3. Máximo rendimiento (local)</b></td><td>Opcional, desde el mes 2: aparece en Maps con el pin destacado y en YouTube con los reels.</td><td>10 %</td></tr></table>
<table class="tabla cols" style="margin-top:6px"><tr><td>Zona</td><td>Radio de 4 a 5 km desde el local (San Martín, Villa Lynch, Villa Ballester, San Andrés, Villa Maipú, Caseros, Santos Lugares, Villa Devoto). Opción “Presencia”: personas que están en la zona.</td></tr>
<tr><td>Horario</td><td>Lunes a viernes 8 a 17 y sábados 8 a 12:30, como el local (las llamadas se atienden).</td></tr>
<tr><td>Objetivo</td><td>Conversiones: llamadas, clics en WhatsApp, Cómo llegar y pedidos desde la web.</td></tr></table>'''),

 ('SEM · Palabras', 'PALABRAS CLAVE.', '''<div class="dos-vias"><div><b>BUSCAR (frase o exacta)</b><ul class="kw"><li>ferretería san martín</li><li>ferretería en san martín</li><li>ferretería villa lynch</li><li>ferretería industrial</li><li>ferretería industrial san martín</li><li>ferretería cerca de mí</li><li>ferretería abierta</li><li>soldadora inverter</li><li>amoladora / amoladora 115</li><li>compresor de aire</li><li>hidrolavadora</li><li>disco de corte / disco flap</li><li>taladro percutor / rotomartillo</li><li>herramientas bosch / dewalt</li></ul></div>
<div><b>EXCLUIR (negativas)</b><ul class="kw neg"><li>gratis</li><li>usado / usada / segunda mano</li><li>mercado libre</li><li>trabajo / empleo / sueldo</li><li>alquiler</li><li>reparación / service</li><li>manual / pdf / cómo funciona</li><li>easy / sodimac / pinturerías</li><li>mayorista online / importador</li><li>san martín de los andes / mendoza / san juan</li></ul></div></div>
<div class="nota"><span>Las negativas evitan pagar clics de quien no va a comprar. Revisar cada semana el informe de “términos de búsqueda” y sumar las que no sirvan.</span></div>'''),

 ('SEM · Anuncios', 'ANUNCIOS LISTOS PARA CARGAR.', '''<div class="rotulo">Títulos (hasta 30 caracteres)</div>
<div class="copiar">Ferretería en San Martín · Ferretería Industrial Masherr · Herramientas & Máquinas · Asesoramiento Técnico · Bosch, DeWalt, Stanley · Soldadoras e Inverter · Comprá Online y Retirá · Pedí por WhatsApp · Villa Lynch, Calle 38 4335 · 4,7 ★ en Google · Para Talleres e Industrias · Cotizá tu Pedido Hoy</div>
<div class="rotulo" style="margin-top:12px">Descripciones (hasta 90 caracteres)</div>
<div class="copiar">Ferretería industrial en Villa Lynch. Herramientas, máquinas e insumos con asesoramiento.<br><br>Armá tu pedido en la web y cerralo por WhatsApp. Retiro en el local, Calle 38 4335.<br><br>Soldadoras, amoladoras, compresores, discos y brocas. Marcas líderes. Consultanos.<br><br>¿Comprás para tu taller o empresa? Cotizamos tu pedido. Lunes a sábado.</div>
<div class="rotulo" style="margin-top:12px">Extensiones</div>
<p class="ayuda" style="font-size:16px;color:var(--tinta)">Ubicación (vincular la ficha de Google) · Llamada 011 4752-5210 · Mensaje/WhatsApp · Vínculos: Tienda, Empresas, Soldadura, Herramientas eléctricas · Textos destacados: Asesoramiento técnico, Retiro en el local, +40 marcas.</p>'''),

 ('SEM · Presupuesto', 'PRESUPUESTO Y PRUEBA.', '''<ol class="pasos"><li><b>Mes 1 · prueba:</b> definir un presupuesto diario fijo y no tocarlo 30 días. Google necesita datos para aprender.</li>
<li><b>Puja:</b> empezar con “Maximizar clics” con límite de costo por clic; cuando haya 15 a 30 conversiones, pasar a “Maximizar conversiones”.</li>
<li><b>Revisión semanal:</b> términos de búsqueda (agregar negativas), anuncios con mejor tasa de clics, horas y barrios que más convierten.</li>
<li><b>Mes 2:</b> mover presupuesto hacia lo que trae llamadas y WhatsApp; apagar lo que no.</li></ol>
<div class="nota"><span><b>Costo por clic:</b> lo fija la competencia en cada momento y cambia por palabra y por mes. No se puede saber de antemano: el mes de prueba muestra cuánto cuesta cada llamada o WhatsApp, y con eso se decide si conviene subir o bajar.</span></div>
<div class="nota ojo" style="margin-top:10px"><span><b>Cuidado:</b> Google Ads suele ofrecer “crédito de regalo” al crear la cuenta con condiciones de gasto mínimo. Leerlas antes de aceptar. Configurar la cuenta en pesos y con la zona horaria de Argentina: no se puede cambiar después.</span></div>'''),

 ('Medición', 'CÓMO SABER SI FUNCIONA.', '''<table class="tabla"><tr><th>Qué medir</th><th>Dónde</th></tr>
<tr><td>Llamadas, “Cómo llegar”, clics a la web desde la ficha</td><td>Perfil de Negocio → Rendimiento</td></tr>
<tr><td>Búsquedas con las que aparecés y posición</td><td>Search Console y búsquedas de control desde el local</td></tr>
<tr><td>Clics en WhatsApp, Llamar, Cómo llegar, pedidos</td><td>Google Analytics 4 (ya preparado en la web)</td></tr>
<tr><td>Costo por llamada / WhatsApp</td><td>Google Ads → Conversiones</td></tr>
<tr><td>Ventas reales</td><td>Mostrador: “¿Cómo nos conociste?”</td></tr></table>
<div class="rotulo" style="margin-top:12px">Para activar la medición necesito</div>
<ol class="pasos"><li>Crear <b>Google Analytics 4</b> con redesmasherr@gmail.com y pasarme el ID (empieza con <b>G-</b>).</li>
<li>Crear la cuenta de <b>Google Ads</b> y pasarme el ID de conversión (empieza con <b>AW-</b>).</li>
<li>Código de verificación de <b>Search Console</b>.</li></ol>
<p class="ayuda">Con eso los conecto a la web en minutos: ya está todo programado, solo falta cargar los IDs.</p>'''),

 ('Plan 90 días', 'CALENDARIO.', '''<table class="tabla"><tr><th>Cuándo</th><th>Qué</th></tr>
<tr><td><b>Semana 1</b></td><td>Search Console + Analytics + cuenta de Ads. Búsquedas de control (puesto actual). Imprimir tarjeta y cartel de reseñas. Subir 10 fotos reales.</td></tr>
<tr><td><b>Semana 2</b></td><td>Lanzar campañas 1 y 2 de Google Ads. Preguntas y respuestas en la ficha.</td></tr>
<tr><td><b>Semanas 3–4</b></td><td>Primera revisión de Ads (negativas). 1 publicación semanal en la ficha. Alta en guías locales.</td></tr>
<tr><td><b>Mes 2</b></td><td>Ajuste de presupuesto según conversiones. Primera nota en la web. Fotos propias en productos destacados.</td></tr>
<tr><td><b>Mes 3</b></td><td>Medir de nuevo el puesto. Decidir campaña de Máximo rendimiento. Comparar costo por cliente de Ads vs. crecimiento orgánico.</td></tr></table>
<div class="nota"><span>Meta realista a 90 días: <b>Top 3 del mapa cerca del local</b>, primera página en “ferretería industrial San Martín” y presencia constante arriba de todo con Ads en el resto del partido.</span></div>'''),
]

TOTAL = 1 + len(P)
def pagina(n, cab, tit, cuerpo):
    return f'''<section class="hoja"><div class="cab"><img src="../catalogo/img/masher-logo-azul.png" alt="Masherr"><span>{e(cab)}</span></div>
<div class="cuerpo"><div class="rotulo">{e(cab)}</div><h2>{e(tit)}</h2>{cuerpo}</div>
<div class="pie"><span>Masherr · Estrategia SEO + SEM</span><b>{n:02d} / {TOTAL:02d}</b></div></section>'''

pags = ['''<section class="hoja oscura"><div class="barra"></div><div class="sup">MASHERR / ESTRATEGIA DIGITAL</div>
<img class="logo" src="../catalogo/img/masher-logo-blanco.png" alt="Masherr máquinas - herramientas"><div class="rayas"></div>
<div class="eyebrow rotulo">SEO local + Google Ads · 90 días</div>
<h1>PRIMEROS<br>CUANDO<br>BUSCAN<br>FERRETERÍA.</h1>
<p class="bajada">Plan para subir en Google Maps y en el buscador en San Martín, con acciones semanales y campañas listas para cargar.</p>
<div class="pie-t"><span>Ferretería industrial</span><b>masherrferreteria.com.ar</b></div></section>''']
for i, (cab, tit, cuerpo) in enumerate(P, 2):
    pags.append(pagina(i, cab, tit, cuerpo))

CSS = (AQUI / 'estilo.css').read_text() + '''
.cols td:first-child { font-family: "Cond"; font-size: 17px; color: var(--azul); white-space: nowrap; width: 90px; }
.estructura td:first-child { width: 130px; }
.copiar { background: var(--gris); border: 2px dashed var(--azul); padding: 12px 14px; font-size: 15.5px; line-height: 1.5; }
.nota.ojo { border-left-color: #B42318; background: #FDECEA; }
.nota + .nota { margin-top: 10px; }
.oscura h1 { font-size: 70px; }
.dos-vias { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 14px; }
.dos-vias > div { border: 2px solid var(--azul); padding: 14px; }
.dos-vias b { display: block; font-family: "Cond"; color: var(--azul); font-size: 18px; letter-spacing: .06em; }
.dos-vias span { display: block; font-size: 15px; color: var(--texto2); margin: 4px 0 8px; }
.dos-vias ul { padding-left: 18px; font-size: 15.5px; line-height: 1.5; }
.dos-vias i { display: block; font-style: normal; font-family: "Cond"; margin-top: 10px; color: var(--negro); }
ul.kw { list-style: none; padding: 0; } ul.kw li { padding: 4px 0; border-bottom: 1px solid var(--linea); font-size: 15px; }
ul.neg li { color: #B42318; }
'''
(AQUI / 'estrategia_seo_sem.html').write_text(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Masherr · Estrategia SEO + SEM</title><style>{CSS}</style></head><body>{"".join(pags)}</body></html>')
print(TOTAL, 'páginas')
