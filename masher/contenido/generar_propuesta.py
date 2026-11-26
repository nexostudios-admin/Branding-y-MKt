"""Propuesta de videos para TikTok e Instagram (diciembre) con el branding de Masherr.
Uso: python3 generar_propuesta.py && node exportar_propuesta.js
Formatos tomados de lo que hoy funciona en TikTok/Reels (series repetibles, demostraciones honestas,
POV, ASMR, antes/después, respuesta a comentarios, guías de regalo de fin de año) aplicados a productos
publicados en masherrferreteria.com.ar. Sin precios: todo cierra por WhatsApp. Sin año de fundación hasta confirmarlo.
"""
import html, re
from pathlib import Path

AQUI = Path(__file__).parent
e = lambda s: html.escape(s, quote=True)
CIERRE = 'masherrferreteria.com.ar · Calle 38 4335, Villa Lynch · @masherrferreteria'

V = [
 dict(n=1, sem=1, tipo='Compra online', formato='Tutorial POV en 4 pasos', red='TikTok + Reels',
      t='Comprá online y retirá en el local', quien='Cliente (actor) + Guido', loc='Casa del cliente (celular) y mostrador',
      pantalla='CÓMO COMPRAR EN MASHERR SIN HACER FILA',
      guion=['¿Sabías que podés armar tu pedido desde el celular y pasar solo a retirarlo?',
             'Uno: entrás a masherrferreteria.com.ar y buscás lo que necesitás.',
             'Dos: lo agregás al carrito y elegís “Retiro en el local”.',
             'Tres: tocás “Enviar pedido por WhatsApp”. Te respondemos por WhatsApp para confirmar stock, precio y forma de pago.',
             'Cuatro: pasás por Calle 38 4335, decís tu nombre y tu pedido ya está listo.',
             '(Guido entrega la bolsa) — Listo, ¿algo más? — No, esto era todo. ¡Gracias!',
             'Comprá online, retirá en Masherr. El link está en nuestro perfil.'],
      tomas='Grabación de pantalla del celular en cada paso (buscador, carrito, opción “Retiro en el local”, botón verde de WhatsApp) · '
            'mensaje de confirmación llegando · el cliente entra al local · bolsa con el nombre del cliente lista en el mostrador · entrega y saludo.',
      porque='Responde la duda número uno de quien llega a la web (“¿cómo compro si no hay precio?”) y muestra que el retiro es rápido.',
      prods=['Cualquier producto chico y visible (por ejemplo, Juego de 6 destornilladores Milwaukee 48-22-2706)']),
 dict(n=2, sem=1, tipo='ASMR', formato='Satisfying / ASMR sin voz', red='TikTok + Reels',
      t='Armando un Packout pieza por pieza', quien='Solo manos (Guido)', loc='Banco de trabajo con fondo limpio',
      pantalla='SONIDO ACTIVADO 🔊',
      guion=['Sin voz: solo el sonido real de cada encastre, traba y cierre.',
             'Texto final en pantalla: “¿Lo querés para tu obra? Escribinos por WhatsApp.”'],
      tomas='Plataforma dolly en el piso · se apoya la caja con ruedas: clic · encima la caja mediana: clic · organizador arriba: clic · '
            'abrir el organizador y acomodar puntas y tornillos · tirar de la manija telescópica y llevarlo rodando. Micrófono cerca, sin música.',
      porque='Los videos de “sonido satisfactorio” se miran completos y se repiten, y eso los empuja en el algoritmo.',
      prods=['Carro de Herramientas Modular Packout – 3 Módulos Milwaukee',
             'Caja Organizador Herramientas Packout Milwaukee 48-22-8430',
             'Milwaukee Packout Plataforma Dolly Base Rodante 48-22-8410']),
 dict(n=3, sem=1, tipo='Comunidad', formato='Adiviná para qué sirve (pide comentarios)', red='TikTok',
      t='¿Para qué sirve esto?', quien='Guido a cámara', loc='Mostrador',
      pantalla='SI ADIVINÁS PARA QUÉ SIRVE, SOS DEL OFICIO',
      guion=['Te muestro tres herramientas. Si sabés para qué sirven, dejalo en los comentarios.',
             'Número uno… (muestra la remachadora sin decir el nombre).',
             'Número dos… (muestra la multiherramienta oscilante).',
             'Número tres… (muestra la engrampadora).',
             'Las respuestas, en el próximo video. ¿Cuántas sacaste?'],
      tomas='Plano medio fijo · cada herramienta en primer plano girando · número grande en pantalla · en la segunda parte, '
            'Guido responde usando “Responder comentario” y hace una demostración corta de cada una.',
      porque='Pedir comentarios genera más conversación que pedir “me gusta”, y la respuesta se convierte en un segundo video.',
      prods=['Remachadora Inalámbrica Milwaukee 2550-20 M12',
             'Multiherramienta Oscilante Sierra Milwaukee M12 2426-159',
             'Engrapadora Milwaukee M12 Batería Con Kit Completo 2447-159']),
 dict(n=4, sem=2, tipo='Esto vs. esto', formato='Comparación con prueba real', red='TikTok + Reels',
      t='Taladro percutor vs. rotomartillo', quien='Guido a cámara', loc='Bloque o pared de hormigón',
      pantalla='MISMO AGUJERO, DOS HERRAMIENTAS. MIRÁ LA DIFERENCIA.',
      guion=['Mismo bloque de hormigón, misma medida de mecha. Taladro percutor de este lado, rotomartillo de este otro.',
             '(Perfora con el percutor.) Entra, pero cuesta y hace fuerza.',
             '(Perfora con el rotomartillo.) Entra solo, sin apretar.',
             '¿Entonces? Si hacés algunos agujeros en casa, el percutor te sobra. Si perforás todo el día o tenés que picar, rotomartillo.',
             'Contanos qué trabajo vas a hacer y te decimos cuál te conviene.'],
      tomas='Pantalla dividida con cronómetro en cada perforación · detalle del polvo saliendo · anteojos, guantes y protección auditiva a la vista.',
      porque='Las demostraciones honestas (“dosis de realidad”) generan confianza y ayudan a decidir la compra.',
      prods=['Taladro Bosch Con Percusión GSB 13 RE 750W 13mm',
             'Rotomartillo Bosch Professional GBH 2-26 DRE 800W']),
 dict(n=5, sem=2, tipo='Consejos', formato='Serie “Error de ferretero” (capítulo 1)', red='TikTok + Reels',
      t='El tarugo equivocado', quien='Guido a cámara', loc='Mostrador con tres tipos de pared (ladrillo, hormigón, durlock)',
      pantalla='POR ESTO SE TE CAEN LOS ESTANTES',
      guion=['Si se te cayó un estante, el problema casi nunca es el tornillo: es el tarugo.',
             'Para ladrillo y hormigón, tarugo de nylon como el Fischer SX.',
             'Si no sabés bien qué pared tenés, el DuoPower se adapta a casi todas.',
             'Y para durlock, uno que se abra detrás de la placa, como el DuoTec.',
             'Traé una foto de tu pared y te decimos cuál llevar. Error de ferretero, capítulo uno. ¿Qué error querés que expliquemos en el próximo?'],
      tomas='Tarugo cortado al medio para mostrar cómo se abre · prueba de colgar peso en cada pared · placa “ERROR DE FERRETERO · CAP. 1”.',
      porque='Las series con el mismo formato hacen que la gente vuelva a buscar el próximo capítulo y siga la cuenta.',
      prods=['Tarugo Fischer Universal SX 8', 'Tarugo Nylon Taco DuoPower 10x80', 'Tarugos DuoTec 10 mm Fischer']),
 dict(n=6, sem=2, tipo='POV', formato='POV: sos herrero y entrás a Masherr', red='TikTok + Reels',
      t='POV: sos herrero', quien='Cliente (actor, herrero) + Guido', loc='Puerta, góndolas y mostrador',
      pantalla='POV: SOS HERRERO Y ENTRÁS A MASHERR',
      dialogo=[('Herrero', '(Entra con ropa de trabajo.) Buenas. Me agarró una reja grande y la soldadora me dejó tirado.'),
               ('Guido', 'Para eso, esta inverter: liviana, la llevás a la obra y te banca electrodo de los gruesos.'),
               ('Herrero', 'Y necesito cortar y emparejar sin estar buscando enchufe.'),
               ('Guido', 'Amoladora inalámbrica con discos de corte y flap. Y para escuadrar rápido, estas magnéticas.'),
               ('Herrero', '¿Todo eso me lo puedo pedir por WhatsApp la próxima?'),
               ('Guido', 'Desde la web, y pasás a retirar. Te lo dejamos listo.')],
      tomas='Cámara en primera persona (desde los ojos del herrero) al entrar · cortes rápidos a cada producto sobre el mostrador · '
            'cierre con el herrero saliendo cargado.',
      porque='El formato POV pone al cliente adentro de la escena y se identifica con su oficio; se puede repetir con electricista, plomero, mecánico.',
      prods=['Soldadora Inverter SI 160 PRO Pegaso',
             'Amoladora Inalámbrica 20V Brushless 115 mm Nebraska + set de discos flap + pack corte',
             'Juego de escuadras magnéticas 4 piezas Emtop EMWH4002']),
 dict(n=7, sem=3, tipo='Unboxing', formato='Unboxing en primera persona', red='TikTok + Reels',
      t='Abrimos el combo Milwaukee M18', quien='Guido (manos y voz)', loc='Banco de trabajo',
      pantalla='ESTO ES TODO LO QUE TRAE',
      guion=['Abrimos el combo Milwaukee M18: te muestro todo lo que trae.',
             'Taladro atornillador, atornillador de impacto, dos baterías, cargador y bolso.',
             'Las dos herramientas usan la misma batería, y la batería sirve para toda la línea M18.',
             'Primera prueba: tornillo largo en madera, de una.',
             'Si lo querés, escribinos por WhatsApp o armá el pedido desde la web.'],
      tomas='Cenital: caja cerrada, se abre y se va sacando pieza por pieza · cada pieza se apoya en fila · prueba rápida en madera · '
            'cierre con todo guardado en el bolso.',
      porque='El unboxing responde “¿qué trae?” antes de que pregunten y es de los formatos más buscados para herramientas.',
      prods=['Combo Taladro Atornillador Impacto 18V Milwaukee 2691-259A']),
 dict(n=8, sem=3, tipo='Antes/después', formato='Transformación antes/después', red='Reels + TikTok',
      t='Del cajón desordenado al maletín', quien='Solo manos (Guido)', loc='Banco de trabajo',
      pantalla='TU CAJÓN DE HERRAMIENTAS HOY VS. MAÑANA',
      guion=['Antes: llaves sueltas, tubos que nunca aparecen y el número que necesitás, perdido.',
             '(Corte con chasquido.)',
             'Después: 150 piezas, cada una en su lugar, en un solo maletín.',
             'Texto final: “¿Cuál es tu cajón? ¿El de antes o el de después? Comentá.”'],
      tomas='Cajón real desordenado, tirado sobre el banco · transición en un golpe de mano · maletín abierto en toma cenital · '
            'detalle de cada sección.',
      porque='Las transformaciones se entienden sin sonido y se comparten; Reels las recomienda mucho.',
      prods=['Juego de herramientas mecánicas 150 piezas R99150 Stanley']),
 dict(n=9, sem=3, tipo='Detrás de escena', formato='Un día en Masherr', red='TikTok + Reels + Historias',
      t='Un día en Masherr', quien='Guido y equipo', loc='Todo el local',
      pantalla='UN DÍA EN UNA FERRETERÍA INDUSTRIAL DE VILLA LYNCH',
      guion=['8 de la mañana: subimos la persiana.',
             'Primeros clientes: el que viene por un tornillo y se lleva tres cosas.',
             'Pedidos que entraron por la web: los preparamos y les ponemos el nombre.',
             'Una consulta difícil: ¿qué disco va para este material?',
             'Mediodía, cortamos. A la tarde, de nuevo.',
             'Así es un día en Masherr. Si nunca viniste, te esperamos en Calle 38 4335. Y si querés enterarte primero de promos y rifas, sumate a la comunidad de WhatsApp.'],
      tomas='Tomas cortas de 1–2 segundos con la hora en pantalla · persiana · mostrador · bolsas de pedidos web con nombre · '
            'cierre del día. Pedir permiso a cada cliente que aparezca.',
      porque='Lo cotidiano y real genera cercanía; muestra al equipo y que la web funciona de verdad.',
      prods=[]),
 dict(n=10, sem=4, tipo='Respuesta', formato='Responder un comentario con video', red='TikTok',
      t='“¿Tienen medidor láser?”', quien='Guido a cámara', loc='Mostrador',
      pantalla='RESPUESTA A: “¿TIENEN MEDIDOR LÁSER?”',
      guion=['Nos preguntaron si tenemos medidor láser. Tenemos de cuarenta, sesenta y cien metros.',
             'Para medir ambientes de una casa, el de cuarenta te sobra.',
             'Para obra, galpones o terrenos, el de cien.',
             'Apuntás, apretás y listo: sin cinta y sin pedirle a nadie que te sostenga la punta.',
             '¿Qué querés que te mostremos ahora? Dejalo en los comentarios.'],
      tomas='Usar la función “Responder comentario” de TikTok (aparece el comentario en pantalla) · medición real de pared a pared · '
            'los tres medidores en fila. Si todavía no hay ese comentario, usar una pregunta real que llegue por WhatsApp.',
      porque='Responder comentarios con video hace sentir escuchada a la audiencia y genera nuevas preguntas.',
      prods=['Medidor de distancia láser 40 m Emtop EMDL1504', 'Medidor de distancia láser 60 m Emtop EMDL1516',
             'Medidor de distancia láser 100 m Emtop EMDL1520']),
 dict(n=11, sem=4, tipo='Fin de año', formato='Guía de regalos', red='TikTok + Reels + Historias',
      t='Regalos para el que tiene todo', quien='Guido a cámara', loc='Mostrador con los productos en fila',
      pantalla='REGALOS PARA EL QUE “YA TIENE TODO”',
      guion=['¿Tenés que regalarle a alguien que dice que ya tiene todo? Te doy cinco ideas.',
             'Para el que trabaja de noche: linterna de casco recargable.',
             'Para el que siempre pide destornilladores prestados: juego de seis, con punta magnética.',
             'Para el que mide a ojo: medidor láser.',
             'Para el que anda con todo encima: mochila para herramientas con 22 bolsillos.',
             'Y para el que tiene taller: una caja Packout.',
             'Escribinos por WhatsApp y te lo dejamos listo para retirar. Las promos de fin de año, en la comunidad de WhatsApp.'],
      tomas='Producto por producto, con número en pantalla (1 a 5) · Guido lo levanta y lo nombra · cierre con todos en fila con un moño.',
      porque='En diciembre las guías de regalo se buscan y se guardan mucho; se pueden reciclar en historias con encuesta.',
      prods=['Linterna de casco recargable USB Milwaukee 2116-21', 'Juego 6 destornilladores Milwaukee 48-22-2706 punta magnética',
             'Medidor de distancia láser 40 m Emtop EMDL1504', 'Mochila para herramientas Milwaukee 22 bolsillos 48-22-8202',
             'Caja Organizador Packout Milwaukee 48-22-8430']),
 dict(n=12, sem=4, tipo='Antes/después', formato='Satisfying antes/después (temporada de verano)', red='TikTok + Reels',
      t='La vereda antes del verano', quien='Guido o alguien del equipo', loc='Vereda del local o patio',
      pantalla='¿TU VEREDA TAMBIÉN ESTÁ ASÍ?',
      guion=['Sin voz: una franja de vereda sucia y la hidrolavadora pasando de una punta a la otra.',
             'Texto en pantalla al final: “Antes del verano: vereda, patio, pileta y auto. Consultanos por WhatsApp.”'],
      tomas='Cámara fija en trípode, plano cenital de la franja · una sola pasada lenta que deja la línea limpia · repetir con baldosas del patio · '
            'cierre mostrando las dos hidrolavadoras.',
      porque='Los videos de limpieza con hidrolavadora son de los más “satisfactorios” y en diciembre coinciden con la limpieza de patios y piletas.',
      prods=['Hidrolavadora 1500W 120 bar K3 Black Edition Kärcher', 'Hidrolavadora 2200W 160 bar Nebraska NEMEHL2200']),
]


def palabras(v):
    textos = v.get('guion') or [d for _, d in v.get('dialogo', [])]
    return len(' '.join(textos).split())

def dur(v):
    if v['tipo'] in ('ASMR',) or v['n'] == 12: return 20
    return max(15, round(palabras(v) / 2.6 / 5) * 5)

TOTAL = 4 + len(V)
def pagina(n, cab, cuerpo):
    return f'''<section class="hoja"><div class="cab"><img src="../catalogo/img/masher-logo-azul.png" alt="Masherr"><span>{e(cab)}</span></div>
<div class="cuerpo">{cuerpo}</div><div class="pie"><span>Masherr · Videos para TikTok e Instagram</span><b>{n:02d} / {TOTAL:02d}</b></div></section>'''

pags = [f'''<section class="hoja oscura"><div class="barra"></div><div class="sup">MASHERR / PROPUESTA DE VIDEOS</div>
<img class="logo" src="../catalogo/img/masher-logo-blanco.png" alt="Masherr máquinas - herramientas"><div class="rayas"></div>
<div class="eyebrow rotulo">TikTok + Instagram · Diciembre</div>
<h1>12 VIDEOS<br>CON LO QUE<br>HOY FUNCIONA.</h1>
<p class="bajada">Formatos en tendencia, productos que tenemos en la web y un video para explicar la compra online con retiro en el local.</p>
<div class="pie-t"><span>Ferretería industrial</span><b>@masherrferreteria</b></div></section>''']

filas = ''.join(f'<li><i>{v["n"]:02d}</i><span class="t">{e(v["t"])}<small>{e(v["formato"])}</small></span><span class="c">Semana {v["sem"]} · {e(v["red"])}</span><span class="dur">~{dur(v)} s</span></li>' for v in V)
pags.append(pagina(2, 'Índice', f'''<div class="rotulo">Los 12 videos</div><h2>QUÉ GRABAMOS.</h2>
<ul class="indice">{filas}</ul>
<p class="ayuda">3 videos por semana durante diciembre. El mismo video se sube a TikTok y a Reels (sin la marca de agua de la otra red).</p>'''))

TEND = [('Series con el mismo formato', 'Capítulos que se repiten (“Error de ferretero”, “POV: sos…”). La gente vuelve a buscar el próximo.'),
        ('Dosis de realidad', 'Demostraciones honestas, con la herramienta funcionando de verdad y sin promesas exageradas.'),
        ('Satisfying y ASMR', 'Sonidos reales de encastres, cortes y limpieza. Se miran completos y se repiten.'),
        ('Pedir comentarios, no “me gusta”', 'Preguntas al final y respuestas en video a los comentarios.'),
        ('POV y antes/después', 'El cliente se ve en la escena; las transformaciones se entienden sin sonido.'),
        ('Temporada', 'Diciembre: guías de regalo de fin de año y preparar patio, vereda y pileta para el verano.')]
pags.append(pagina(3, 'Tendencias', f'''<div class="rotulo">Por qué estos formatos</div><h2>LO QUE HOY FUNCIONA.</h2>
<ul class="tend">{''.join(f'<li><b>{e(a)}</b><span>{e(b)}</span></li>' for a, b in TEND)}</ul>
<div class="nota" style="margin-top:14px"><span><b>Hashtags.</b> Evitar los genéricos (#fyp, #viral, #parati), que no suman. Usar 3 a 5 del rubro y de la zona:
#ferreteria #herramientas #villalynch #sanmartin #herreria (según el video).</span></div>
<div class="nota" style="margin-top:10px"><span><b>Audio.</b> En TikTok, elegir un sonido en tendencia de la biblioteca comercial (los de música de artistas no se pueden usar en cuentas de empresa). En ASMR, solo sonido real.</span></div>'''))

prods_lista = ''.join(f'<li><b>{v["n"]:02d}</b> {e(p)}</li>' for v in V for p in v['prods'])
pags.append(pagina(4, 'Antes de grabar', f'''<div class="rotulo">Checklist del día</div><h2>ANTES DE GRABAR.</h2>
<div class="nota ojo"><span><b>Sin precios.</b> Ningún video dice ni muestra precios: todo cierra con “consultanos por WhatsApp”. Tapar etiquetas de precio en góndola.</span></div>
<div class="nota" style="margin-top:10px"><span><b>Confirmar stock</b> de cada producto de la lista el día anterior. Están todos publicados en la web, pero el stock real lo confirma el local.</span></div>
<div class="rotulo" style="margin-top:14px">Productos a tener listos</div>
<ul class="prods">{prods_lista}</ul>
<div class="rotulo" style="margin-top:12px">Orden sugerido para grabar</div>
<ol class="pasos"><li><b>Banco de trabajo:</b> 02, 05, 07, 08 y la prueba del 04.</li>
<li><b>Mostrador:</b> 03, 06 (con actor), 10 y 11.</li>
<li><b>Con cliente y celular:</b> 01. <b>Vereda:</b> 12. <b>Durante todo un día:</b> 09.</li></ol>
<p class="ayuda">Vertical 9:16, buena luz, sonido limpio y elementos de protección en cada demostración. Pedir permiso a toda persona que aparezca.</p>'''))

for i, v in enumerate(V, 5):
    if v.get('dialogo'):
        cuerpo_guion = '<div class="dialogo">' + ''.join(f'<p><b>{e(q)}:</b> {e(d)}</p>' for q, d in v['dialogo']) + '</div>'
    else:
        cuerpo_guion = '<div class="guion">' + ''.join(f'<p>{e(p)}</p>' for p in v['guion']) + '</div>'
    prods = ''.join(f'<li>{e(p)}</li>' for p in v['prods'])
    clase = re.sub(r'[^a-z]', '', v['tipo'].lower().replace('é', 'e').replace('ó', 'o').replace('ñ', 'n'))
    pags.append(pagina(i, f'Video {v["n"]:02d}', f'''<div class="meta"><span class="rotulo">Video {v["n"]:02d} · Semana {v["sem"]}</span><span class="chip t-{clase}">{e(v["tipo"])}</span><span class="chip gris">~{dur(v)} s</span><span class="chip gris">{e(v["red"])}</span></div>
<h2 class="idea">{e(v["t"].upper())}</h2>
<div class="ficha"><div><b>Formato</b>{e(v["formato"])}</div><div><b>Quién · Dónde</b>{e(v["quien"])} · {e(v["loc"])}</div></div>
<div class="gancho"><b>TEXTO EN PANTALLA (PRIMEROS 2 SEGUNDOS)</b>{e(v["pantalla"])}</div>
{cuerpo_guion}
{f'<div class="lista-prod"><b>Productos</b><ul>{prods}</ul></div>' if prods else ''}
<div class="dos"><div><b>Tomas</b>{e(v["tomas"])}</div><div><b>Por qué funciona</b>{e(v["porque"])}<br><br><b>Placa final</b>{e(CIERRE)}</div></div>'''))

CSS = (AQUI / 'estilo.css').read_text() + '''
.dos > div { min-width: 0; overflow-wrap: anywhere; }
.ficha { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 12px; font-size: 15px; line-height: 1.35; }
.ficha div { background: var(--gris); padding: 10px 12px; }
.ficha b { display: block; font-family: "Cond"; color: var(--azul); font-size: 14px; letter-spacing: .08em; text-transform: uppercase; }
.guion p, .dialogo p { font-size: 17.5px; line-height: 1.4; margin-bottom: 8px; }
.guion { border-left: 4px solid var(--azul); padding-left: 16px; margin-bottom: 12px; }
.dialogo { margin-bottom: 12px; }
.dialogo p b { font-family: "Cond"; color: var(--azul); font-size: 18px; }
.chip.t-compraonline { background: #1E7A3C; } .chip.t-asmr { background: #4A3A8C; } .chip.t-comunidad { background: #B4531A; }
.chip.t-estovsesto, .chip.t-consejos { background: var(--azul); } .chip.t-pov, .chip.t-respuesta { background: var(--negro); }
.chip.t-unboxing, .chip.t-antesdespues { background: #2D5FA8; } .chip.t-detrasdeescena { background: #6B4E2E; } .chip.t-findeano { background: #B42318; }
.indice .t small { display: block; font-family: "Sans"; font-weight: normal; font-size: 13px; color: #5A6072; margin-top: 2px; }
.indice .dur { font-family: "Cond"; font-size: 15px; color: var(--azul); width: 54px; text-align: right; }
.indice .c { width: 190px; }
.prods { list-style: none; border-top: 1px solid var(--linea); columns: 2; column-gap: 18px; }
.prods li { break-inside: avoid; display: flex; gap: 8px; padding: 3px 0; border-bottom: 1px solid var(--linea); font-size: 13px; line-height: 1.28; }
.prods li b { font-family: "Cond"; color: var(--celeste); width: 24px; flex: none; }
.lista-prod { background: var(--gris); padding: 10px 14px; margin-bottom: 12px; font-size: 15px; }
.lista-prod b { font-family: "Cond"; color: var(--azul); font-size: 14px; letter-spacing: .08em; text-transform: uppercase; }
.lista-prod ul { margin: 4px 0 0 18px; } .lista-prod li { margin: 2px 0; }
.tend { list-style: none; border-top: 2px solid var(--negro); }
.tend li { padding: 11px 0; border-bottom: 1px solid var(--linea); }
.tend b { display: block; font-family: "Cond"; font-size: 19px; color: var(--azul); }
.tend span { font-size: 16px; line-height: 1.4; }
.nota.ojo { border-left-color: #B42318; background: #FDECEA; }
'''
(AQUI / 'propuesta_videos.html').write_text(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Masherr · Videos para TikTok e Instagram</title><style>{CSS}</style></head><body>{"".join(pags)}</body></html>')
print(TOTAL, 'páginas')
