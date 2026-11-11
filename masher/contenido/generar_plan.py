"""Genera plan_videos.html (plan de 15 reels) y lo exporta a PDF con render en Playwright.
Uso: python3 generar_plan.py && node exportar.js
Precios tomados de la planilla/web al 11/11/2026: verificarlos antes de publicar cada video.
"""
import html
from pathlib import Path

AQUI = Path(__file__).parent
WEB = 'masherr.netlify.app'
e = lambda s: html.escape(s, quote=True)

IDEAS = [
  dict(t='¿115 o 180? La amoladora que necesitás', tipo='Comparativa', obj='Web', dur='30–40 s',
       gancho='Guido, con una amoladora en cada mano: “Si comprás la amoladora equivocada, tirás la plata.”',
       guion=['Mostrar las dos lado a lado: 115 mm y 180 mm.', 'Para qué sirve cada una: cortes finos y terminaciones vs. cortes profundos y desbaste pesado.', 'Pregunta clave: “¿Qué vas a cortar y cuántas horas por día?”'],
       prods=[('Amoladora angular 115 mm 650 W Vanden', 46000), ('Amoladora angular 180 mm 2000 W Nebraska', 195000)],
       cta='“Las dos están en la web. Buscá “amoladora” y elegí la tuya.”', link='tienda/?q=amoladora',
       grabar='Plano medio en el mostrador · detalle de los discos de cada una · corte real sobre un perfil.',
       por_que='Las comparativas se guardan y se comparten con el que “está por comprar una”.'),
  dict(t='El disco correcto para cada material', tipo='Demostración', obj='Web', dur='25–35 s',
       gancho='“Este disco en hierro dura 2 minutos.” (disco equivocado sacando chispas)',
       guion=['Tres materiales en la mesa: hierro, cerámica y madera.', 'Para cada uno, el disco que va: corte de acero, diamantado y flap para desbastar.', 'Cierre con los tres discos en mano.'],
       prods=[('Pack x 5 discos de corte de acero 115 mm Bosch', 4000), ('Disco flap 115 mm grano 40 Pegaso', 3000), ('Broca diamantada Ø 6 mm Aliafor', 14300)],
       cta='“Guardá este video y comprá los discos en la web.”', link='tienda/?cat=accesorios',
       grabar='Cámara fija lateral, cortes en cámara lenta, texto en pantalla con el nombre de cada disco.',
       por_que='Contenido útil y corto: se guarda como referencia. El sonido del corte retiene.'),
  dict(t='¿Con cable o a batería?', tipo='Comparativa', obj='Web', dur='30–45 s',
       gancho='Guido a cámara: “La pregunta que más me hacen en el mostrador: ¿con cable o a batería?”',
       guion=['Taladro percutor con cable vs. atornillador a batería.', 'Con cable: potencia y uso continuo. A batería: movilidad y atornillado.', 'Regla simple: “Si perforás hormigón todo el día, cable. Si atornillás y te movés, batería.”'],
       prods=[('Taladro percutor 1050 W 13 mm Nebraska', 86000), ('Taladro atornillador 12 V Nebraska', 55000), ('Atornillador GSR 120-LI 12 V Bosch', 190000)],
       cta='“Contanos qué vas a hacer y te decimos cuál. Escribinos o comprá en la web.”', link='tienda/?q=taladro',
       grabar='Dos manos, dos herramientas. Prueba rápida: perforar ladrillo y atornillar una placa.',
       por_que='Responde una duda masiva y genera comentarios (“yo uso…”).'),
  dict(t='La caja del que recién arranca', tipo='Combo con precio', obj='Web', dur='30–40 s',
       gancho='“Con $121.900 armás tu primera caja de herramientas.”',
       guion=['Bolso vacío sobre el mostrador.', 'Se van sumando herramientas una por una con su precio en pantalla.', 'Bolso lleno, total final.'],
       prods=[('Bolso de herramientas Emtop', 46000), ('Cinta métrica 5 m Stanley', 23900), ('Juego de destornilladores 6 pzas Emtop', 21000), ('Nivel de aluminio 400 mm Bremen', 17000), ('Pinza pico de loro 300 mm Emtop', 14000)],
       cta='“Armá el mismo carrito en la web y mandalo por WhatsApp.”', link='tienda/',
       grabar='Toma cenital (desde arriba). Cada herramienta entra con un golpe de sonido. Contador de precio.',
       por_que='Formato “armando el kit” con contador: retiene hasta el final y se comparte a quien empieza.'),
  dict(t='¿Qué soldadora necesitás?', tipo='Comparativa', obj='Local', dur='35–45 s',
       gancho='Guido, con la máscara en la mano: “No compres una soldadora sin saber esto.”',
       guion=['Dos inverter: 140 A y 190 A.', 'Qué espesor y qué electrodo soporta cada una, uso hogareño vs. taller.', 'Recordar la máscara: “la vista no se repone”.'],
       prods=[('Soldadora inverter SI 140 Pegaso', 182000), ('Soldadora inverter SI 190 PRO Pegaso', 280000), ('Máscara fotosensible EDGE-500S Foxtter', 79000)],
       cta='“Vení a verlas al local: te mostramos cómo sueldan.”', link='nosotros/',
       grabar='Cordón de soldadura real (con protección) · detalle de las perillas · máscara oscureciendo.',
       por_que='La soldadura en cámara es muy visual; la duda de amperaje es frecuente.'),
  dict(t='Cinta métrica vs. medidor láser', tipo='Desafío', obj='Web', dur='20–30 s',
       gancho='“¿Quién mide más rápido un galpón de 30 metros?”',
       guion=['Dos personas, una con cinta y otra con láser.', 'Cronómetro en pantalla.', 'Resultado y cuándo conviene cada uno.'],
       prods=[('Medidor de distancia láser 40 m Emtop', 64000), ('Cinta métrica 5 m Stanley', 23900)],
       cta='“El láser está en la web. Buscá “medidor”.”', link='tienda/?q=medidor',
       grabar='Plano general del espacio + pantalla del láser en primer plano. Humor permitido.',
       por_que='Desafío con resultado al final: alta retención y comentarios.'),
  dict(t='¿Cuántos BAR necesita tu hidrolavadora?', tipo='Demostración', obj='Web', dur='30–40 s',
       gancho='“Antes / después de 10 segundos de hidrolavadora.” (vereda sucia)',
       guion=['Limpieza real de una baldosa o un auto.', 'Explicar qué son los BAR y para qué alcanza cada potencia.', 'Comparar uso de casa vs. uso intensivo.'],
       prods=[('Hidrolavadora 1400 W 105 BAR Klugan', 120000), ('Hidrolavadora K3 Black Edition 120 BAR Karcher', 415000)],
       cta='“Elegí la tuya en la web y te la tenemos lista para retirar.”', link='tienda/?q=hidrolavadora',
       grabar='Antes/después en el mismo encuadre. Cámara lenta del agua.',
       por_que='El antes/después de limpieza es de los formatos más compartidos.'),
  dict(t='Comprá en la web en 30 segundos', tipo='Tutorial', obj='Web', dur='20–30 s',
       gancho='Guido: “Soy Guido, de Masherr. Así nos comprás sin moverte del taller.”',
       guion=['Grabación de pantalla del celular: buscar “disco”, agregar al carrito.', 'Completar nombre y entrega.', 'Tocar “Enviar pedido por WhatsApp” y mostrar el mensaje armado.'],
       prods=[('Cualquier producto del catálogo', None)],
       cta='“Probalo ahora: link en la bio.”', link='',
       grabar='Grabación de pantalla vertical + cara de quien habla en un recuadro.',
       por_que='Explica el canal nuevo. Fijarlo arriba del perfil.'),
  dict(t='Llegó al local', tipo='Abrimos la caja', obj='Local', dur='20–30 s',
       gancho='“Llegó y no lo podemos creer.” (caja cerrada)',
       guion=['Abrir la caja frente a cámara.', 'Mostrar las piezas y lo que lo hace distinto.', 'Precio y disponibilidad en pantalla.'],
       prods=[('Carro de herramientas modular Packout 3 módulos Milwaukee', 800000), ('Kit taladro percutor, atornillador y amoladora Brushless Emtop', 390000)],
       cta='“Vení a verlo al local o pedilo por la web.”', link='tienda/?q=packout',
       grabar='Mesa limpia, buena luz, detalles en macro. Mostrar el local de fondo.',
       por_que='Abrir una caja genera curiosidad; sirve para cada ingreso de mercadería.'),
  dict(t='Taladro vs. rotomartillo en hormigón', tipo='Desafío', obj='Web', dur='20–30 s',
       gancho='“Mismo agujero, misma pared. ¿Quién gana?”',
       guion=['Taladro percutor y rotomartillo SDS Plus contra el mismo bloque.', 'Cronómetro en pantalla.', 'Explicar por qué gana el rotomartillo y cuándo alcanza el taladro.'],
       prods=[('Rotomartillo SDS Plus 1200 W Braber', 130000), ('Broca SDS Plus Ø 8 × 160 mm Venturo', 3600), ('Taladro percutor 1050 W Nebraska', 86000)],
       cta='“Rotomartillo y brocas, en la web. Buscá “SDS”.”', link='tienda/?q=sds',
       grabar='Pantalla dividida con las dos perforaciones al mismo tiempo. Polvo en cámara lenta.',
       por_que='Las “batallas” de herramientas tienen alta retención y discusión en comentarios.'),
  dict(t='Mito o verdad, con Guido', tipo='Serie de mitos', obj='Local', dur='15–25 s',
       gancho='Guido, con dos carteles: “Mito o verdad: más watts siempre es mejor.”',
       guion=['Plantear el mito en pantalla y pausa de 1 segundo.', 'Respuesta con un ejemplo real del local.', 'Invitar a mandar el próximo mito por comentarios.'],
       prods=[('Según el mito elegido', None)],
       cta='“¿Tenés dudas? Vení al mostrador y te asesoramos.”', link='nosotros/',
       grabar='Guido a cámara, con carteles de MITO / VERDAD en la mano.',
       por_que='Serie repetible (un capítulo por semana); los comentarios alimentan los próximos.'),
  dict(t='El error con el adhesivo de contacto', tipo='Demostración', obj='Web', dur='25–35 s',
       gancho='“Si pegás así, se despega mañana.”',
       guion=['Pegado mal: sin esperar el oreo.', 'Pegado bien: capa fina en ambas caras, esperar y presionar.', 'Prueba de fuerza al final.'],
       prods=[('Adhesivo de contacto x 1 lt Fortex', 16000), ('Diluyente para adhesivo D-10 x 1 lt Fortex', 12500)],
       cta='“Adhesivo y diluyente en la web. Buscá “Fortex”.”', link='tienda/?q=fortex',
       grabar='Primeros planos de la aplicación, reloj en pantalla, tirón final.',
       por_que='Tip práctico con prueba visual: alto guardado.'),
  dict(t='Un día con Guido en Masherr', tipo='Detrás de escena', obj='Local', dur='30–45 s',
       gancho='Guido, abriendo la persiana: “7:58. Así arranca un día en la ferretería de mi familia.”',
       guion=['Guido abre el local y presenta a la familia y al equipo (con su permiso).', 'Primeras consultas: un cliente real (con permiso) resolviendo algo con Guido.', 'Cierre con la fachada y la dirección.'],
       prods=[('El local, la familia y el equipo', None)],
       cta='“Te esperamos en Calle 38 4335, Villa Lynch.”', link='nosotros/',
       grabar='Tomas cortas de 1–2 s con música; voz en off o textos. Pedir autorización a quien aparezca.',
       por_que='Muestra que es una empresa familiar: “una ferretería con historia” con caras reales.'),
  dict(t='Equipá tu compresor', tipo='Combo con precio', obj='Web', dur='25–35 s',
       gancho='“Compraste el compresor… ¿y ahora qué le conectás?”',
       guion=['Compresor solo.', 'Se suma el kit de accesorios: pistola de aire, inflador, manguera.', 'Mostrar tres usos en 3 segundos cada uno.'],
       prods=[('Compresor 25 lts 2 HP Foxtter', 252000), ('Kit para compresores 20 piezas Bremen', 79000)],
       cta='“Compresor + kit, en la web. Agregalos al carrito.”', link='tienda/?q=compresor',
       grabar='Toma cenital del kit desplegado + tres usos rápidos.',
       por_que='Responde la siguiente compra lógica: venta cruzada.'),
  dict(t='Pedido para empresas en 1 minuto', tipo='Caso empresas', obj='Ambos', dur='30–45 s',
       gancho='Guido, con una lista en la mano: “Mantenimiento de planta: 20 productos, resuelto antes del mediodía.”',
       guion=['Mostrar una lista de compra real (sin datos del cliente).', 'Cómo se arma el pedido y se cotiza.', 'Mostrar la página Empresas de la web.'],
       prods=[('Juego de herramientas mecánicas 150 pzas Stanley', 784000), ('Juego de llaves combinadas 12 pzas Emtop', 57400)],
       cta='“¿Comprás para una empresa? Pedí cotización en la web.”', link='empresas/',
       grabar='Manos con la lista, mostrador, celular con la página Empresas.',
       por_que='Llega a compradores de empresas y talleres, el público de mayor ticket.'),
]

def precio(n):
    return '$' + f'{n:,}'.replace(',', '.')

def pagina(n, total, cab, cuerpo, oscura=False):
    if oscura:
        return f'<section class="hoja oscura">{cuerpo}</section>'
    return f'''<section class="hoja"><div class="cab"><img src="../catalogo/img/masher-logo-azul.png" alt="Masherr"><span>{e(cab)}</span></div>
<div class="cuerpo">{cuerpo}</div><div class="pie"><span>Masherr · Plan de contenido Instagram</span><b>{n:02d} / {total:02d}</b></div></section>'''

total = 4 + len(IDEAS) + 2
pags = []
pags.append(pagina(1, total, '', f'''<div class="barra"></div><div class="sup">MASHERR / PLAN DE CONTENIDO</div>
<img class="logo" src="../catalogo/img/masher-logo-blanco.png" alt="Masherr máquinas - herramientas"><div class="rayas"></div>
<div class="eyebrow rotulo">Instagram · 15 reels con Guido · 5 semanas</div>
<h1>VIDEOS QUE<br>TERMINAN EN<br>UNA VENTA.</h1>
<p class="bajada">Guido presenta productos reales, con precio y una invitación a comprar en la web o en el local.</p>
<div class="pie-t"><span>Ferretería industrial</span><b>@masherrferreteria</b></div>''', oscura=True))

pags.append(pagina(2, total, 'La estrategia', f'''<div class="rotulo">Cómo funciona cada video</div>
<h2>MOSTRAR, EXPLICAR, VENDER.</h2>
<p class="lead">Cada reel resuelve una duda real del mostrador con un producto que tenemos, y termina con un paso concreto para comprar.</p>
<table class="tabla estructura"><tr><th>Segundos</th><th>Qué pasa</th></tr>
<tr><td>0 – 3</td><td><b>Gancho:</b> una frase o imagen que hace frenar a quien está mirando. Problema, desafío o precio.</td></tr>
<tr><td>3 – 25</td><td><b>Demostración:</b> la herramienta funcionando, en manos de Guido.</td></tr>
<tr><td>25 – 35</td><td><b>Criterio + llamado:</b> cuál conviene y dónde comprarla.</td></tr></table>
<div class="rotulo" style="margin-top:22px">Tres llamados a la acción</div>
<div class="ctas"><div><b>WEB</b><span>“Buscá “amoladora” en la web” · link en la bio a {WEB}</span></div>
<div><b>LOCAL</b><span>“Vení a verla: Calle 38 4335, Villa Lynch”</span></div>
<div><b>WHATSAPP</b><span>“Escribinos y te decimos cuál te conviene”</span></div></div>
<div class="nota"><span><b>Regla:</b> cada video muestra un producto real del catálogo, con el precio vigente de la planilla. Verificar precio y stock el día que se publica.</span></div>'''))

pags.append(pagina(3, total, 'Quién sale en cámara', f'''<div class="rotulo">La cara de la marca</div>
<h2>GUIDO, DE MASHERR.</h2>
<p class="lead">Guido, uno de los hijos del dueño, es quien aparece en todos los videos. Una persona real de la familia que atiende el mostrador genera más confianza que cualquier publicidad.</p>
<ol class="pasos"><li><b>Presentación fija:</b> arrancar los primeros videos con “Soy Guido, de Masherr”. Después alcanza con “Guido, de Masherr” en el texto de pantalla.</li>
<li><b>Hablar como en el mostrador:</b> en primera persona y con vos (“te recomiendo”, “elegí”, “vení”). Sin guion leído: puntos clave y que lo cuente con sus palabras.</li>
<li><b>Siempre con la herramienta en la mano:</b> que se vea usándola, con anteojos, guantes o máscara cuando corresponde.</li>
<li><b>Misma ropa de trabajo</b> en todos los videos (remera o chaleco con el logo, si hay), para que se lo reconozca.</li>
<li><b>Responder comentarios</b> como Guido: “Te lo explico en el próximo video” genera ideas nuevas para grabar.</li></ol>
<div class="nota"><span><b>Familia y equipo:</b> si aparecen el dueño u otros integrantes, pedirles permiso antes de publicar. No publicar años de antigüedad hasta confirmar la fecha de fundación: usar “la ferretería de mi familia” o “una ferretería con historia”.</span></div>'''))

filas = ''.join(f'<li><i>{i:02d}</i><span class="t">{e(d["t"])}</span><span class="c">{e(d["tipo"])}</span><b class="obj {d["obj"].lower()}">{d["obj"]}</b></li>' for i, d in enumerate(IDEAS, 1))
pags.append(pagina(4, total, 'Las 15 ideas', f'''<div class="rotulo">Índice</div><h2>15 REELS.</h2>
<ul class="indice">{filas}</ul>
<p class="ayuda">Web: invita a comprar en la web · Local: invita a venir al local · Ambos: las dos cosas.</p>'''))

for i, d in enumerate(IDEAS, 1):
    prods = ''.join(f'<tr><td>{e(p)}</td><td class="pr">{precio(v) if v else "—"}</td></tr>' for p, v in d['prods'])
    link = f'{WEB}/{d["link"]}' if d['link'] else f'{WEB} (link en la bio)'
    pags.append(pagina(4 + i, total, f'Idea {i:02d}', f'''<div class="meta"><span class="rotulo">Idea {i:02d} · {e(d["tipo"])}</span><span class="chip {d["obj"].lower()}">Llamado: {d["obj"]}</span><span class="chip gris">{d["dur"]}</span></div>
<h2 class="idea">{e(d["t"].upper())}</h2>
<div class="gancho"><b>GANCHO 0–3 s</b>{e(d["gancho"])}</div>
<ol class="pasos">{''.join(f'<li>{e(g)}</li>' for g in d["guion"])}</ol>
<table class="tabla"><tr><th>Producto en el video</th><th>Precio</th></tr>{prods}</table>
<div class="cta"><b>LLAMADO A LA ACCIÓN</b>{e(d["cta"])}<span>{e(link)}</span></div>
<div class="dos"><div><b>Qué grabar</b>{e(d["grabar"])}</div><div><b>Por qué funciona</b>{e(d["por_que"])}</div></div>'''))

sem = [IDEAS[i:i + 3] for i in range(0, 15, 3)]
cal = ''.join(f'<tr><td class="s">Semana {k}</td>' + ''.join(f'<td><b>{(k - 1) * 3 + j + 1:02d}</b> {e(d["t"])}</td>' for j, d in enumerate(s)) + '</tr>' for k, s in enumerate(sem, 1))
pags.append(pagina(5 + len(IDEAS), total, 'Calendario', f'''<div class="rotulo">Publicación</div><h2>3 REELS POR SEMANA.</h2>
<table class="tabla cal"><tr><th></th><th>Lunes</th><th>Miércoles</th><th>Viernes</th></tr>{cal}</table>
<div class="rotulo" style="margin-top:18px">Todas las semanas</div>
<ol class="pasos"><li><b>Historias 4 días:</b> el producto del reel con el sticker de enlace a la web, una encuesta y “¿Tenés dudas? Escribinos”.</li>
<li><b>Fijar 3 reels en el perfil:</b> “Comprá en la web en 30 segundos” (08), “Un día con Guido en Masherr” (13) y “Pedido para empresas” (15).</li>
<li><b>Link en la bio:</b> {WEB}</li></ol>'''))

pags.append(pagina(6 + len(IDEAS), total, 'Medición', f'''<div class="rotulo">Cómo sabemos si vende</div><h2>MEDIR CADA SEMANA.</h2>
<table class="tabla"><tr><th>Qué mirar</th><th>Dónde</th></tr>
<tr><td>Reproducciones, retención y guardados</td><td>Estadísticas de cada reel en Instagram</td></tr>
<tr><td>Clics en el link de la bio y en las historias</td><td>Estadísticas del perfil</td></tr>
<tr><td>Pedidos que llegan desde el carrito de la web</td><td>WhatsApp: mensajes que empiezan con “Hola Masherr, quiero hacer este pedido”</td></tr>
<tr><td>Consultas y ventas en el local</td><td>Preguntar en el mostrador: “¿Cómo nos conociste?”</td></tr></table>
<div class="rotulo" style="margin-top:18px">Antes de grabar</div>
<ol class="pasos"><li>Confirmar precio y stock en la planilla.</li><li>Grabar vertical, con buena luz y sonido limpio.</li>
<li>Usar elementos de protección en cada demostración (anteojos, guantes, máscara).</li>
<li>Pedir permiso a clientes o personas que aparezcan.</li><li>Texto en pantalla grande y corto: muchos miran sin sonido.</li></ol>
<div class="nota"><span>Primeras 2 semanas: registrar los números como punto de partida. Después, repetir los formatos que más guardados y pedidos generen.</span></div>'''))

CSS = (AQUI / 'estilo.css').read_text()
(AQUI / 'plan_videos.html').write_text(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Masherr · Plan de 15 reels</title><style>{CSS}</style></head><body>{"".join(pags)}</body></html>')
print(total, 'páginas')
