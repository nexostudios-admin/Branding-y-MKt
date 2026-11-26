"""Guion de rodaje · nuevos videos (noviembre semana 4 + diciembre semanas 1 y 2) con el branding de Masherr.
Uso: python3 generar_rodaje2.py && node exportar_pdf.js guion_rodaje2.html Masherr_Guion_Rodaje_Nuevos.pdf
Fuente: Masherr_Ferreteria.pdf (planificación del cliente). Textos corregidos de ortografía y puntuación, sin precios.
Lo marcado con [[...]] hay que confirmarlo antes de publicar (se resalta en amarillo).
"""
import html, re
from pathlib import Path

AQUI = Path(__file__).parent
e = lambda s: html.escape(s, quote=True)
CIERRE = 'masherrferreteria.com.ar · Calle 38 4335, Villa Lynch · @masherrferreteria'
DETALLE = 'Grabar video detalle de cada producto (planos cerrados, girando, con el logo visible).'

V = [
 # ----------------------------------------------------------------- NOVIEMBRE · SEMANA 4
 dict(id='15', mes='Noviembre', sem=4, tipo='Humor', t='“¿Venden cinta?”', quien='Cliente + 2 empleados', loc='Mostrador',
      pantalla='¿VENDEN CINTA? 🤨',
      ref='tiktok.com/@inversiones_joa55/video/7466497854119349509',
      dialogo=[('Escena', 'Entra un cliente y se acerca al mostrador, donde hay dos empleados. Detrás del Empleado 1 se ven bien las cintas métricas exhibidas.'),
               ('Cliente', '¡Hola, buenas! ¿Venden cinta?'),
               ('Empleado 1', 'Nooo, ¿no ves que acá solamente vendemos…'),
               ('Empleado 2', '(Lo interrumpe.) ¡Sí, claro! Tenemos varias marcas y modelos. ¿Buscabas alguna en particular?')],
      tomas='Plano fijo del mostrador. Las cintas tienen que quedar visibles detrás del Empleado 1 para reforzar el remate. '
            'La interrupción del Empleado 2 tiene que ser rápida, sin dejar terminar la frase al primero.',
      prods=['Cintas métricas Stanley, Bremen y Evel (exhibidas detrás del mostrador)']),
 dict(id='16', mes='Noviembre', sem=4, tipo='Producto', t='¿Vas a soldar? Elegí bien el equipo', quien='Guido a cámara', loc='Mostrador con las soldadoras en fila',
      pantalla='¿VAS A SOLDAR? ELEGÍ BIEN EL EQUIPO',
      guion=['Si trabajás con hierro, la soldadora que elegís define cómo te va a salir el trabajo, y también cuánto vas a tardar en terminarlo.',
             'En Masherr tenemos soldadoras inverter Pegaso en cuatro modelos: la SI 140, la SI 160 PRO, la SI 190 PRO y la C250 PRO, para que elijas según la exigencia de tu trabajo.',
             'Además, tenemos la soldadora inverter Braber de 130 amperes, que trabaja con electrodo, TIG y MIG Flux.',
             'Y no todo se trata de la máquina: para soldar tenés que proteger bien la vista. Por eso también tenemos máscaras fotosensibles Foxtter, en dos modelos: la EDGE-500S y la OPERA-400S.',
             'Si es tu primera soldadora, o la tenés que cambiar porque ya no rinde para tu trabajo, escribinos y te ayudamos a elegir la tuya.'],
      tomas='Las 5 soldadoras en fila, de menor a mayor · detalle del panel de cada una · las dos máscaras · Guido se pone la máscara al cierre.',
      prods=['Soldadora Inverter SI 140 Pegaso', 'Soldadora Inverter SI 160 PRO Pegaso', 'Soldadora Inverter SI 190 PRO Pegaso',
             'Soldadora Inverter SI C250 PRO Pegaso', 'Soldadora Inverter 130 A MMA/TIG/MIG Flux Braber',
             'Máscara fotosensible EDGE-500S Foxtter', 'Máscara fotosensible OPERA-400S Foxtter']),
 dict(id='17', mes='Noviembre', sem=4, tipo='Producto', t='Aspiradoras para sólidos y líquidos', quien='Guido a cámara', loc='Taller o depósito',
      pantalla='ASPIRADORAS PARA SÓLIDOS Y LÍQUIDOS: ELEGÍ EL TAMAÑO',
      guion=['Hay limpiezas que una escoba no resuelve: el polvo del taller, el agua derramada, los restos de obra.',
             'Para eso tenemos aspiradoras Nebraska de sólidos y líquidos, en dos tamaños.',
             'La de 15 litros y 1100 watts, práctica para espacios chicos y fácil de guardar. Y la de 40 litros y 1200 watts, para trabajos más grandes o de más duración.',
             'Las dos aspiran sólidos y líquidos, tienen base con ruedas para moverlas fácil y vienen con boquillas para distintas superficies.',
             'Contanos dónde la vas a usar y te decimos cuál te conviene. Consultá por WhatsApp o pasá por Masherr.'],
      tomas='Las dos aspiradoras lado a lado · aspirar aserrín o polvo · aspirar agua derramada · detalle de ruedas y boquillas.',
      prods=['Aspiradora 1100W 15 L sólidos y líquidos NEAS101100 Nebraska', 'Aspiradora 1200W 40 L sólidos y líquidos NEAS351200 Nebraska']),
 dict(id='18', mes='Noviembre', sem=4, tipo='Producto', t='Hidrolavadora Nebraska 2200 W · 160 bar', quien='Guido a cámara', loc='Vereda o patio',
      pantalla='LLEGA EL CALOR: PATIO, VEREDA Y AUTO EN MINUTOS',
      guion=['Llega el calor y es momento de limpiar el patio, la vereda o el auto. Te presento una máquina que te va a ahorrar horas: la hidrolavadora Nebraska de 2200 watts.',
             'Tiene una presión máxima de 160 bar y [[un caudal de 6,5 litros]], para limpiar bien sin gastar de más.',
             'Trae sistema Auto-Stop, manguera de alta presión de 5 metros, dosificador de detergente, lanza turbo y boquilla regulable. Y viene con ruedas y carrete para la manguera, así la movés y la guardás fácil.',
             'Sirve para vehículos, patios, veredas, herramientas y otras superficies. Es ideal para uso doméstico intensivo y también profesional.',
             'Y si buscás otra opción, en el local tenemos más modelos, de distintas marcas y potencias. Vení a conocerlos y te ayudamos a elegir.',
             'Masherr, Calle 38 4335, Villa Lynch, o consultá por WhatsApp.'],
      tomas='Antes/después en una franja de vereda (cámara fija) · detalle de lanza turbo, dosificador y carrete · cierre con otras hidrolavadoras del local.',
      prods=['Hidrolavadora 2200W 160 bar NEMEHL2200 Nebraska']),
 dict(id='19', mes='Noviembre', sem=4, tipo='Consejos', t='¿Taladro con cable o inalámbrico?', quien='Guido a cámara', loc='Banco de trabajo',
      pantalla='¿TALADRO CON CABLE O INALÁMBRICO?',
      guion=['¿Estás buscando un taladro y no sabés si elegir uno con cable o inalámbrico? Te mostramos dos opciones que tenemos en Masherr.',
             'Si querés trabajar sin preocuparte por la batería y tenés un enchufe cerca, el taladro percutor Bosch de 550 watts es una buena alternativa: mandril de 13 mm, velocidad variable y percusión, ideal para madera, metal y mampostería.',
             'Si necesitás más libertad de movimiento y no depender de un enchufe, tenemos el taladro percutor atornillador inalámbrico Stanley de 20 V y 45 Nm: dos velocidades, 22 posiciones de torque y luz LED. Viene con dos baterías, cargador rápido y maletín.',
             'Dos opciones diferentes para distintas necesidades.',
             'En Masherr tenemos estos y muchos modelos más. Escribinos o pasá por el local y te ayudamos a elegir el que mejor se adapte a tu trabajo.'],
      tomas='Pantalla dividida: cable a la izquierda, inalámbrico a la derecha · perforación con cada uno · detalle del selector de torque y la luz LED.',
      prods=['Taladro percutor Bosch 13 mm 550W GSB 550 RE', 'Taladro percutor atornillador inalámbrico Stanley 20V 45 Nm SCH201C2K']),
 dict(id='20', mes='Noviembre', sem=4, tipo='Humor', t='“Si hace este ruido… necesitás”', quien='2 empleados', loc='Local (Empleado 2 de fondo)',
      pantalla='SI HACE ESTE RUIDO… NECESITÁS ESTO',
      ref='tiktok.com/@sos.ferreteria/video/7677591297867271444',
      dialogo=[('Empleado 1', 'Si las puertas de tu casa hacen…'),
               ('Empleado 2', '(De fondo, haciendo otra cosa: imita el chirrido de una bisagra.)'),
               ('Empleado 1', '…vas a necesitar WD-40.'),
               ('Empleado 1', 'Si las canillas de tu casa hacen…'),
               ('Empleado 2', '(Imita el goteo de una canilla.)'),
               ('Empleado 1', '…vas a necesitar cambiar los cueritos.'),
               ('Empleado 1', 'Si los muebles de tu casa hacen…'),
               ('Empleado 2', '(Imita el crujido de un mueble flojo.)'),
               ('Empleado 1', '…vas a necesitar ajustar los tornillos (muestra el destornillador), o tal vez cambiarlos.'),
               ('Empleado 1', 'Para cada problema, una solución. En Masherr tenemos lo que necesitás. ¡Consultanos!')],
      tomas='Empleado 1 a cámara en primer plano, Empleado 2 desenfocado de fondo · cada producto en primer plano al nombrarlo · texto en pantalla con el nombre del producto.',
      prods=['Lubricante multiuso WD-40', 'Cueritos para canilla', 'Juego de destornilladores']),
 # ----------------------------------------------------------------- DICIEMBRE · SEMANA 1
 dict(id='01', mes='Diciembre', sem=1, tipo='Empresas', t='¿Comprás para tu empresa? Cotizá con Masherr', quien='Guido a cámara', loc='Mostrador y depósito',
      pantalla='¿COMPRÁS PARA TU EMPRESA? COTIZÁ CON MASHERR',
      guion=['¿Tenés una empresa, un taller o una industria y necesitás comprar herramientas e insumos en cantidad?',
             'En Masherr te ayudamos a cotizar tus pedidos para que resuelvas tus compras de manera más práctica.',
             'Solo tenés que mandarnos tu lista de productos y cantidades por WhatsApp, o cargarla en masherrferreteria.com.ar, en la sección Empresas, y nuestro equipo prepara la cotización.',
             'Trabajamos con distintas marcas y categorías: herramientas eléctricas y manuales, discos, brocas, soldadura, seguridad industrial y mucho más.',
             'Además, [[tenemos más de 53 años de experiencia]] acompañando a empresas, talleres y profesionales.',
             'Si necesitás abastecer tu negocio, escribinos y pedí tu cotización.'],
      tomas='Guido revisando una lista larga · pantalla del formulario de Empresas · pedidos armados en el mostrador · góndolas por categoría.',
      prods=[]),
 dict(id='02', mes='Diciembre', sem=1, tipo='Producto', t='¿Sos soldador? En Masherr tenés todo', quien='Guido a cámara', loc='Mostrador con todo el equipo de soldadura',
      pantalla='¿SOS SOLDADOR? EN MASHERR TENÉS TODO PARA TRABAJAR',
      guion=['Si trabajás en herrería o soldadura, sabés que no alcanza con tener una buena máquina: también necesitás los insumos y accesorios para trabajar.',
             'En Masherr tenemos distintas opciones para equiparte: soldadoras inverter, electrodos, discos de corte, accesorios y elementos de protección.',
             'También tenemos máscaras fotosensibles Foxtter, para proteger tu vista mientras soldás.',
             'Ya sea que estés empezando, tengas tu propio taller o trabajes profesionalmente, vas a encontrar alternativas según lo que necesitás.',
             '¿Buscás algún insumo o querés equipar tu taller? Escribinos y te ayudamos a encontrarlo.'],
      tomas=DETALLE + ' Armar un “kit del soldador” sobre el mostrador: soldadora, electrodos, discos, máscara y guantes.',
      prods=['Soldadoras inverter Pegaso y Braber', 'Electrodos', 'Discos de corte', 'Máscaras fotosensibles Foxtter (EDGE-500S y OPERA-400S)']),
 dict(id='03', mes='Diciembre', sem=1, tipo='Consejos', t='3 cosas que no pueden faltar en tu taller', quien='Guido a cámara', loc='Mostrador y góndolas',
      pantalla='3 COSAS QUE NO PUEDEN FALTAR EN TU TALLER',
      guion=['Si tenés un taller, hay tres cosas que te facilitan mucho el trabajo y que no deberían faltar.',
             'Primero: organización. Tener tus herramientas ordenadas y a mano te ahorra tiempo y evita que se pierdan. En Masherr tenemos cajas, bolsos y sistemas de almacenamiento.',
             'Segundo: consumibles. No esperes a quedarte sin discos, mechas o puntas para reponerlos. Los usás todo el tiempo, y tener variedad y stock te permite seguir trabajando sin interrupciones.',
             'Tercero: protección. Guantes, antiparras, protección auditiva y los elementos adecuados para cada tarea son fundamentales para trabajar seguro.',
             'En Masherr encontrás todo esto y mucho más para equipar tu taller.',
             '¿Qué es lo que nunca puede faltar en tu espacio de trabajo? ¡Contanos en los comentarios!'],
      tomas='Número grande en pantalla (1, 2, 3) · 1: detalle de organizadores · 2: detalle de kits con variedad de discos, mechas o puntas · 3: detalle de guantes, antiparras y protección auditiva.',
      prods=['Cajas y organizadores (Packout Milwaukee, Stanley)', 'Kits de discos, mechas y puntas', 'Guantes, antiparras y protección auditiva']),
 dict(id='05', mes='Diciembre', sem=1, tipo='Humor', t='Video humor: “estamos grabando”', quien='Equipo de Masherr', loc='Local',
      pantalla='[[DEFINIR SEGÚN LA REFERENCIA]]',
      ref='tiktok.com/@sos.ferreteria/video/7692554732593876245',
      guion=['Recrear la referencia con el equipo de Masherr.',
             'Aprovechar la situación para que, al enfocar, se vea que están grabando con un producto destacado (un combo, una máquina o un organizador) que genere interés.',
             'Cierre: “En Masherr tenemos lo que necesitás. Consultanos por WhatsApp.”'],
      tomas='Mirar la referencia antes de grabar y repetir su ritmo · el producto destacado tiene que verse claro cuando la cámara “descubre” la grabación.',
      prods=['Un producto destacado: combo, máquina u organizador (por ejemplo, Combo Milwaukee 3697-259A o carro Packout)']),
 # ----------------------------------------------------------------- DICIEMBRE · SEMANA 2
 dict(id='06', mes='Diciembre', sem=2, tipo='Producto', t='Combo rotomartillo SDS Plus + cinceles', quien='Guido a cámara', loc='Banco de trabajo o pared de hormigón',
      pantalla='¿TENÉS QUE PERFORAR, PICAR O DEMOLER?',
      guion=['¿Tenés que perforar, picar o hacer trabajos de demolición? Este combo puede ser justo lo que necesitás.',
             'En Masherr tenemos este combo de rotomartillo SDS Plus Electroneum de 850 watts y 3 joules de impacto.',
             'Tiene velocidad variable y tres funciones: perforación con percusión, rotación simple y demolición liviana.',
             '¡Y eso no es todo! También trae un cincel de punta y uno plano de 250 milímetros, ideales para picar, remover material y abrir canaletas.',
             'Además viene con brocas, accesorios y maletín para tener todo organizado.',
             'Una solución muy completa para obra, reformas e instalaciones. ¿Te interesa? Escribinos por WhatsApp y consultá disponibilidad y precio.'],
      tomas=DETALLE + ' Perforación y picado de una canaleta con los cinceles (anteojos, guantes y protección auditiva).',
      prods=['Combo Rotomartillo SDS Plus + Cincel Punta + Cincel Plano Electroneum']),
 dict(id='07', mes='Diciembre', sem=2, tipo='Producto', t='Combo Milwaukee: dos herramientas para equiparte', quien='Guido a cámara', loc='Banco de trabajo',
      pantalla='DOS HERRAMIENTAS MILWAUKEE EN UN SOLO COMBO',
      guion=['Si estás buscando equipar tu taller con herramientas profesionales, mirá este combo Milwaukee que tenemos en Masherr.',
             'Incluye dos herramientas fundamentales: un taladro percutor y una llave de impacto.',
             'El taladro percutor es para perforar. La llave de impacto, para ajustar y aflojar fijaciones con mucha menos fuerza.',
             'Dos herramientas que se complementan y te permiten resolver distintas tareas con más practicidad.',
             'Si trabajás en mantenimiento, mecánica o construcción, este combo puede ser una gran incorporación para tu equipo.',
             '¿Querés conocer más? Escribinos por WhatsApp y consultá precio y disponibilidad.'],
      tomas=DETALLE + ' Perforación en madera con el taladro · aflojar un bulón con la llave de impacto · todo guardado en el bolso al cierre.',
      prods=['Combo Taladro Percutor + Llave de Impacto Milwaukee 3697-259A']),
 dict(id='08', mes='Diciembre', sem=2, tipo='Producto', t='¿Todavía llevás tus herramientas así?', quien='Guido a cámara', loc='Mostrador y góndola de almacenamiento',
      pantalla='¿TODAVÍA LLEVÁS TUS HERRAMIENTAS ASÍ?',
      guion=['¿Todavía llevás todas tus herramientas sueltas o mezcladas en cualquier bolso?',
             'Si trabajás trasladándote entre obras, talleres o distintos lugares, sabés lo importante que es tener todo organizado y a mano.',
             'En Masherr tenemos mochilas, cajas y bolsos para transportar y guardar tus herramientas.',
             'Elegís según la cantidad de herramientas que llevás, el espacio que tenés y el tipo de trabajo que hacés.',
             'Trabajamos con marcas como Milwaukee, Stanley y Emtop, entre otras.',
             'Dejá de perder tiempo buscando tus herramientas y empezá a llevar todo organizado. Escribinos o pasá por el local y te ayudamos a elegir.'],
      tomas='Arranque: herramientas sueltas en una bolsa de supermercado · corte a las mochilas, cajas y bolsos · ' + DETALLE,
      prods=['Mochilas Milwaukee (48-22-8200, 48-22-8202, Packout 48-22-8301)', 'Cajas Packout Milwaukee', 'Cajas de herramientas Stanley', 'Bolsos Emtop']),
 dict(id='09', mes='Diciembre', sem=2, tipo='Humor', t='“Dale, confiá”', quien='2 empleados', loc='Local',
      pantalla='HOY ESTÁ DIFÍCIL ENCONTRAR ALGUIEN DE CONFIANZA',
      ref='tiktok.com/@sos.ferreteria/video/7627578220526849300',
      dialogo=[('Empleado 1', 'Dale, confiá.'),
               ('Empleado 2', '(Se deja caer de espaldas… y nadie lo agarra. Caída simulada y segura.)'),
               ('Empleado 1', '(A cámara.) Hoy en día está difícil encontrar a alguien de confianza. Por eso tenés que venir a Masherr.'),
               ('Empleado 1', '[[Tenemos más de 53 años de experiencia]] y trabajamos con más de 55 marcas. ¡Vení a visitarnos!')],
      tomas='Plano fijo para la caída (usar colchoneta fuera de cuadro) · después Empleado 1 habla caminando y recorriendo el local · cierre en la puerta.',
      prods=[]),
]

# Los videos de diciembre se numeran D01…D09 para no confundirlos con los de noviembre.
for v in V:
    if v['mes'] == 'Diciembre': v['id'] = 'D' + v['id']

def resaltar(t):
    return re.sub(r'\[\[(.+?)\]\]', r'<mark>\1</mark>', e(t))

def palabras(v):
    textos = v.get('guion') or [d for _, d in v.get('dialogo', [])]
    return len(re.sub(r'\[\[|\]\]', '', ' '.join(textos)).split())

def dur(v):
    return max(15, round(palabras(v) / 2.6 / 5) * 5)

TOTAL = 3 + len(V)
def pagina(n, cab, cuerpo):
    return f'''<section class="hoja"><div class="cab"><img src="../catalogo/img/masher-logo-azul.png" alt="Masherr"><span>{e(cab)}</span></div>
<div class="cuerpo">{cuerpo}</div><div class="pie"><span>Masherr · Guion de rodaje · nuevos videos</span><b>{n:02d} / {TOTAL:02d}</b></div></section>'''

pags = [f'''<section class="hoja oscura"><div class="barra"></div><div class="sup">MASHERR / GUION DE RODAJE</div>
<img class="logo" src="../catalogo/img/masher-logo-blanco.png" alt="Masherr máquinas - herramientas"><div class="rayas"></div>
<div class="eyebrow rotulo">Noviembre semana 4 · Diciembre semanas 1 y 2</div>
<h1>{len(V)} VIDEOS<br>NUEVOS PARA<br>GRABAR.</h1>
<p class="bajada">Guiones, tomas y productos de cada video, listos para el día de rodaje.</p>
<div class="pie-t"><span>Ferretería industrial</span><b>@masherrferreteria</b></div></section>''']

def fila(v):
    return f'<li><i>{v["id"]}</i><span class="t">{e(v["t"])}</span><span class="c">{e(v["mes"])} S{v["sem"]} · {e(v["tipo"])}</span><span class="dur">~{dur(v)} s</span></li>'
pags.append(pagina(2, 'Índice', f'''<div class="rotulo">Los {len(V)} videos</div><h2>QUÉ GRABAMOS.</h2>
<div class="rotulo" style="margin-top:6px">Noviembre · semana 4</div><ul class="indice">{''.join(fila(v) for v in V if v['mes'] == 'Noviembre')}</ul>
<div class="rotulo" style="margin-top:12px">Diciembre · semanas 1 y 2</div><ul class="indice">{''.join(fila(v) for v in V if v['mes'] == 'Diciembre')}</ul>
<p class="ayuda">Duración estimada leyendo a ritmo natural. El texto en pantalla de cada video va en mayúsculas. En la planificación de diciembre no hay video 4.</p>'''))

prods = ''.join(f'<li><b>{v["id"]}</b> {e(p)}</li>' for v in V for p in v['prods'])
pags.append(pagina(3, 'Antes de grabar', f'''<div class="rotulo">Checklist del día</div><h2>ANTES DE GRABAR.</h2>
<div class="nota ojo"><span><b>Confirmar la antigüedad.</b> Los videos D01 y D09 dicen <mark>“más de 53 años”</mark>. Confirmar el año de fundación antes de publicar (Google dice 1969, los videos ya grabados dicen 1973 y el posteo fijado de Instagram, 56 años).</span></div>
<div class="nota" style="margin-top:10px"><span><b>Sin precios</b> en ningún video: todo cierra con “consultanos por WhatsApp”. Tapar etiquetas de precio en góndola. Confirmar también el caudal de la hidrolavadora (video 18) y definir el guion del video D05 a partir de su referencia.</span></div>
<div class="rotulo" style="margin-top:14px">Productos a tener listos</div>
<ul class="prods">{prods}</ul>
<div class="rotulo" style="margin-top:12px">Orden sugerido para grabar</div>
<ol class="pasos"><li><b>Humor (2 empleados + cliente):</b> 15, 20, D05 y D09.</li>
<li><b>Mostrador y banco:</b> 16, 19, D02, D03, D06, D07 y D08.</li>
<li><b>Guido a cámara:</b> D01. <b>Taller o depósito:</b> 17. <b>Vereda:</b> 18.</li></ol>'''))

for i, v in enumerate(V, 4):
    if v.get('dialogo'):
        cuerpo = '<div class="dialogo">' + ''.join(f'<p><b>{e(q)}:</b> {resaltar(d)}</p>' for q, d in v['dialogo']) + '</div>'
    else:
        cuerpo = '<div class="guion">' + ''.join(f'<p>{resaltar(p)}</p>' for p in v['guion']) + '</div>'
    lista = ''.join(f'<li>{e(p)}</li>' for p in v['prods'])
    ref = f'<br><br><b>Referencia</b>{e(v["ref"])}' if v.get('ref') else ''
    pags.append(pagina(i, f'Video {v["id"]}', f'''<div class="meta"><span class="rotulo">Video {v["id"]} · {e(v["mes"])} · Semana {v["sem"]}</span><span class="chip {v["tipo"].lower()}">{e(v["tipo"])}</span><span class="chip gris">~{dur(v)} s</span></div>
<h2 class="idea">{e(v["t"].upper())}</h2>
<div class="ficha"><div><b>Quién</b>{e(v["quien"])}</div><div><b>Dónde</b>{e(v["loc"])}</div></div>
<div class="gancho"><b>TEXTO EN PANTALLA</b>{resaltar(v["pantalla"])}</div>
{cuerpo}
{f'<div class="lista-prod"><b>Productos</b><ul>{lista}</ul></div>' if lista else ''}
<div class="dos"><div><b>Tomas</b>{e(v["tomas"])}</div><div><b>Placa final</b>{e(CIERRE)}{ref}</div></div>'''))

CSS = (AQUI / 'estilo.css').read_text() + '''
mark { background: #FFE58A; color: inherit; padding: 0 3px; }
.gancho mark { color: var(--negro); }
.dos > div { min-width: 0; overflow-wrap: anywhere; }
.ficha { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 12px; font-size: 16px; }
.ficha div { background: var(--gris); padding: 10px 12px; }
.ficha b { display: block; font-family: "Cond"; color: var(--azul); font-size: 14px; letter-spacing: .08em; text-transform: uppercase; }
.guion p, .dialogo p { font-size: 18px; line-height: 1.42; margin-bottom: 9px; }
.guion { border-left: 4px solid var(--azul); padding-left: 16px; margin-bottom: 12px; }
.dialogo { margin-bottom: 12px; }
.dialogo p b { font-family: "Cond"; color: var(--azul); font-size: 18px; }
.chip.producto { background: var(--azul); } .chip.humor { background: #B4531A; } .chip.consejos { background: var(--verde); } .chip.empresas { background: #4A3A8C; }
.indice .dur { font-family: "Cond"; font-size: 15px; color: var(--azul); width: 54px; text-align: right; }
.indice .c { width: 190px; } .indice li { padding-top: 6px; padding-bottom: 6px; } .indice i { width: 44px; flex: none; }
.prods { list-style: none; border-top: 1px solid var(--linea); columns: 2; column-gap: 18px; }
.prods li { break-inside: avoid; display: flex; gap: 8px; padding: 3px 0; border-bottom: 1px solid var(--linea); font-size: 13px; line-height: 1.28; }
.prods li b { font-family: "Cond"; color: var(--celeste); width: 24px; flex: none; }
.lista-prod { background: var(--gris); padding: 10px 14px; margin-bottom: 12px; font-size: 15px; }
.lista-prod b { font-family: "Cond"; color: var(--azul); font-size: 14px; letter-spacing: .08em; text-transform: uppercase; }
.lista-prod ul { margin: 4px 0 0 18px; } .lista-prod li { margin: 2px 0; }
.nota.ojo { border-left-color: #B42318; background: #FDECEA; }
'''
(AQUI / 'guion_rodaje2.html').write_text(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Masherr · Guion de rodaje · nuevos videos</title><style>{CSS}</style></head><body>{"".join(pags)}</body></html>')
print(TOTAL, 'páginas')
