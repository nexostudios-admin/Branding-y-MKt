"""Guion de rodaje (planificación de contenido del cliente) con el branding de Masherr.
Uso: python3 generar_rodaje.py && node exportar_rodaje.js
Fuente: Masherr_Ferreteria.docx (planificación de 14 videos). Textos corregidos de ortografía;
el video 3 venía con el texto del video 2 y se propone un guion nuevo a partir de la ficha del producto.
"""
import html, re
from pathlib import Path

AQUI = Path(__file__).parent
e = lambda s: html.escape(s, quote=True)
CIERRE = 'masherr.netlify.app · Calle 38 4335, Villa Lynch · @masherrferreteria'

# Marcar con [[...]] lo que hay que confirmar antes de grabar (se resalta en amarillo).
V = [
 dict(n=1, sem=1, tipo='Institucional', t='Presentación', quien='Guido a cámara', loc='Puerta del local y mostrador',
      pantalla='¿HACE CUÁNTO QUE NO ENTRÁS A UNA FERRETERÍA DE LAS DE VERDAD?',
      guion=['¿Hace cuánto que no entrás a una ferretería de las de verdad?',
             '[[Acá, desde 1973. Cincuenta y tres años]] equipando a los que trabajan: industrias, talleres, profesionales y también vos, que arreglás tus cosas en casa.',
             'Herramientas eléctricas, discos y brocas, soldadura, herramientas de mano, taller y jardín, seguridad.',
             'Más de 430 productos de 55 marcas.',
             'Masherr, Calle 38 número 4335, Villa Lynch. Venís, preguntás y te llevás lo que necesitás.'],
      tomas='Guido entra al local hablando a cámara · paneo de góndolas por categoría · fachada con el número al cierre.',
      prods=[]),
 dict(n=2, sem=1, tipo='Institucional', t='55 marcas para elegir', quien='Guido a cámara', loc='Góndolas y mostrador',
      pantalla='¿BUSCÁS UNA HERRAMIENTA? TENEMOS 55 MARCAS PARA ELEGIR.',
      guion=['Bosch, DeWalt, Stanley, Milwaukee, Karcher, Esab, Dremel, Bahco y Tyrolit, entre otras.',
             'En Masherr trabajamos con 55 marcas para que encuentres distintas opciones según lo que necesitás.',
             'Porque no existe una herramienta ideal para todo, sino la correcta para cada trabajo.',
             'Y si no sabés cuál elegir, te asesoramos para encontrar la marca y el modelo que mejor se adapten a tu necesidad y presupuesto.',
             '¿Estás buscando una herramienta? Escribinos o acercate a nuestro local en Calle 38, 4335, Villa Lynch.'],
      tomas='Un corte rápido por cada marca nombrada (caja o producto con el logo visible) · Guido señalando la góndola.',
      prods=[]),
 dict(n=3, sem=1, tipo='Producto', t='Amoladora inalámbrica Nebraska 20V con discos Bosch y Pegaso', quien='Guido a cámara', loc='Mostrador o banco de trabajo',
      pantalla='¿CORTAR, DESBASTAR Y PULIR SIN BUSCAR UN ENCHUFE?',
      nuevo=True,
      guion=['¿Cortar, desbastar y pulir sin buscar un enchufe?',
             'Te presento la amoladora inalámbrica Nebraska de 20 voltios, con motor brushless: sin carbones, más autonomía y menos mantenimiento.',
             'Tiene cuatro velocidades, hasta 8.500 vueltas por minuto, para trabajar cada material con control.',
             'Viene con batería de 4 amperes, cargador rápido y maletín.',
             'Y en este combo te llevás además cuatro discos flap Pegaso, del grano 40 al 120, y un pack de cinco discos de corte Bosch para acero.',
             'Todo, por 195 mil pesos. Escribinos o acercate al local en Calle 38, 4335, Villa Lynch.'],
      tomas='Abrir el maletín · colocar el disco · corte de un perfil y desbaste con flap (con anteojos y guantes) · discos ordenados del 40 al 120.',
      prods=[('Amoladora inalámbrica 20V Brushless 115 mm Nebraska + discos flap Pegaso + pack corte Bosch', 195000)]),
 dict(n=4, sem=1, tipo='Producto', t='Combo de herramientas Emtop', quien='Guido a cámara', loc='Mostrador',
      pantalla='¿QUERÉS ARMAR TU CAJA DE HERRAMIENTAS?',
      guion=['Si querés empezar a armar una caja de herramientas completa, no te podés perder el combo de Emtop.',
             'Tres pinzas de acero con mangos antideslizantes, un set de 43 piezas con mango de crique, puntas y tubos, y un bolso porta herramientas rígido con correa de hombro para llevar todo organizado.',
             '¡Un kit súper completo para tener distintas herramientas a mano y llevarlas donde las necesites!',
             'Y lo mejor es que tenés todo en un solo combo, listo para acompañarte en tus trabajos.',
             'Si te interesa, escribinos para consultar por el combo Emtop o acercate al local, en Calle 38, 4335, Villa Lynch.'],
      tomas='Toma cenital: bolso vacío y van entrando las pinzas, el set y el crique · Guido se cuelga el bolso al hombro al cierre.',
      prods=[('Combo de herramientas Emtop (bolso + juego de pinzas + set de puntas y tubos)', 115000)]),
 dict(n=5, sem=1, tipo='Humor', t='“El coso”', quien='Guido (ferretero) + 3 clientes', loc='Mostrador',
      pantalla='LO QUE PEDÍS VS. LO QUE TE DAMOS',
      ref='tiktok.com/@aguslafrosciarodr/video/7488048373736525061',
      dialogo=[('Cliente 1', 'Hola, buenas. ¿Tendrás el coso redondo que es así, para el cosito del agua?'),
               ('Guido', '(Abre el cajón del “coso redondo” y saca cueritos.) Sí, tome. Lleve dos por las dudas.'),
               ('Cliente 2', 'Buenas tardes, ¿tendrá el pituto gris que va con los tornillos?'),
               ('Guido', '(Abre el cajón del “pituto gris”: tarugos.) ¡Cómo no! ¿Cuántos quiere?'),
               ('Cliente 3', 'Me das el plástico de los cables.'),
               ('Guido', 'Buenas tardes. Sí. ¿De cuántos metros buscaba? (cable canal)'),
               ('Cliente 3', 'Y no sé… como para el cable de la tele.')],
      tomas='Mismo encuadre fijo del mostrador para los tres clientes · texto en pantalla con el nombre real: CUERITO, TARUGO, CABLE CANAL.',
      prods=[('Cueritos, tarugos y cable canal (utilería del sketch)', None)]),
 dict(n=6, sem=2, tipo='Institucional', t='Estamos para asesorarte', quien='Guido a cámara', loc='Mostrador',
      pantalla='¿TE PASÓ ALGUNA VEZ QUE TENÉS QUE HACER UN ARREGLO Y NO SABÉS QUÉ HERRAMIENTA NECESITÁS?',
      guion=['¿Te pasó alguna vez que tenés que hacer un arreglo y no sabés qué herramienta necesitás?',
             'Muchas veces sabemos qué queremos solucionar, pero no tenemos claro qué producto necesitamos para hacerlo.',
             'Puede ser reparar una canilla, perforar una pared de hormigón o soldar una reja. ¡Y no todas las tareas requieren las mismas herramientas ni los mismos insumos!',
             'En Masherr te ayudamos a encontrar lo que necesitás. Contanos qué trabajo vas a realizar y nuestro equipo te va a orientar para elegir la herramienta y el producto adecuados.',
             'Porque comprar bien asesorado te permite evitar gastos innecesarios y encontrar la solución correcta desde el principio.',
             '[[Hace más de 50 años]] que acompañamos a quienes trabajan y necesitan soluciones.',
             '¿Tenés un proyecto o arreglo pendiente? Escribinos o acercate a nuestro local en Calle 38, 4335, Villa Lynch. ¡Estamos para asesorarte!'],
      tomas='Guido atendiendo una consulta real (con permiso) · insertos de canilla, mecha de hormigón y soldadora.',
      prods=[]),
 dict(n=7, sem=2, tipo='Producto', t='Carro modular Milwaukee Packout', quien='Guido a cámara', loc='Pasillo o vereda (para mostrar las ruedas)',
      pantalla='NO HAY NADA MÁS IMPORTANTE QUE TENER TUS HERRAMIENTAS ORGANIZADAS Y SIEMPRE A MANO.',
      guion=['Si trabajás en un taller o te trasladás constantemente entre obras, sabés lo importante que es tener todo ordenado y listo para usar.',
             'Por eso te mostramos el carro modular Milwaukee Packout: un sistema de tres módulos apilables que te permite organizar, guardar y transportar tus herramientas de manera mucho más práctica.',
             'Cuenta con una caja inferior con ruedas todoterreno y manija telescópica, más dos módulos superiores que podés utilizar juntos o por separado.',
             'Su construcción robusta, cierres reforzados y sistema de encastre lo convierten en un gran aliado para acompañarte en cada trabajo.',
             'Dejá de complicarte trasladando tus herramientas y empezá a trabajar con todo organizado.',
             'Encontrá el Milwaukee Packout en Masherr por 800 mil pesos.'],
      tomas='Guido arrastra el carro hacia cámara · desencastra un módulo y lo levanta · detalle de cierres y manija telescópica.',
      prods=[('Carro de herramientas modular Packout 3 módulos Milwaukee', 800000)]),
 dict(n=8, sem=2, tipo='Producto', t='Kit Emtop 20V: taladro percutor y amoladora brushless', quien='Guido a cámara', loc='Banco de trabajo',
      pantalla='¿TRABAJÁS EN CONSTRUCCIÓN, HERRERÍA O MANTENIMIENTO?',
      guion=['Si trabajás en construcción, herrería o mantenimiento, este combo puede ser justo lo que necesitás.',
             'Incluye dos herramientas inalámbricas profesionales: un taladro percutor brushless de 66 Nm y una amoladora angular brushless de 115 mm, ambos de 20 voltios.',
             '¡Pero eso no es todo! También viene con dos baterías de 4 Ah, cargador, 10 discos de corte para metal, 47 accesorios y un maletín para tener todo organizado y listo para llevar.',
             'Un kit pensado para que tengas más herramientas a mano, puedas resolver distintos trabajos y no te falte nada cuando estás en pleno trabajo.',
             '¿Te gustaría tener este equipo? Encontralo en Masherr. Escribinos o acercate a nuestro local en Calle 38, 4335, Villa Lynch.'],
      tomas='Abrir el maletín y sacar pieza por pieza · perforación y corte rápidos · todo desplegado en toma cenital.',
      prods=[('Kit taladro percutor y amoladora brushless 20V Emtop', 390000)]),
 dict(n=9, sem=2, tipo='Humor', t='“Solo un tornillo”', quien='Guido (ferretero) + 1 cliente', loc='Mostrador y puerta',
      pantalla='“SOLO VENGO POR UN DESTORNILLADOR”',
      ref='vt.tiktok.com/ZSpf1WRLE',
      dialogo=[('Cliente', 'Hola, buenas. Quería un destornillador.'),
               ('Guido', 'Buenas, sí, ahí te traigo. ¿Para qué es?'),
               ('Cliente', 'Unos estantes.'),
               ('Guido', 'Ah, vas a necesitar tarugos. ¿Tenés?'),
               ('Cliente', 'Bueno, dame tarugos y el destornillador, nada más.'),
               ('Guido', 'Perfecto. ¿Y viste los combos de taladros y atornilladores que tenemos?'),
               ('Cliente', '(Se va cargado de combos.) Solo el destornillador… solo el destornillador.'),
               ('Guido', '¡Pará, flaco! Te quedó el destornillador acá.')],
      tomas='Plano fijo del mostrador · el cliente sale cargado por la puerta · remate con Guido levantando el destornillador.',
      prods=[('Destornillador, tarugos y combos de taladro (utilería)', None)]),
 dict(n=10, sem=2, tipo='Producto', t='Juego de herramientas mecánicas Stanley 150 piezas', quien='Guido a cámara', loc='Banco de trabajo',
      pantalla='SI TENÉS UN CAJÓN LLENO DE LLAVES QUE NUNCA SON DEL NÚMERO QUE NECESITÁS, ESTE VIDEO ES PARA VOS.',
      guion=['Si tenés un cajón lleno de llaves que nunca son del número que necesitás, este video es para vos.',
             'Nos pasa a todos: estás en plena reparación, te falta un tubo y ahí se frena todo el trabajo.',
             'Este juego Stanley trae ciento cincuenta piezas en un maletín de alto impacto: criques y tubos de un cuarto, tres octavos y media pulgada, tubos largos y de impacto, llaves combinadas, llaves Allen, puntas Torx, destornilladores y pinzas.',
             'Ciento cincuenta herramientas, un solo maletín, por setecientos ochenta y cuatro mil pesos.',
             'Pasá a verlo o escribinos por WhatsApp. Masherr, Calle 38, número 4335.'],
      tomas='Arranque: cajón desordenado de llaves sueltas · corte al maletín Stanley abriéndose · detalle de cada sección.',
      prods=[('Juego de herramientas mecánicas 150 piezas Stanley R99150', 784000)]),
 dict(n=11, sem=3, tipo='Consejos', t='3 consejos de ferretero', quien='Guido a cámara', loc='Mostrador',
      pantalla='3 ERRORES QUE COMETÉS EN TU CASA',
      guion=['Tres errores que cometés en tu casa y que cualquier ferretero te evitaría.',
             'Uno: usar el mismo destornillador para todo. Así se pelan los tornillos y después no hay forma de sacarlos. Tené un kit de destornilladores completo, con la punta justa para cada tornillo.',
             'Dos: medir a ojo. El metro y medio “más o menos” es el mueble que no entra. Tené siempre una cinta métrica a mano: en Masherr hay de tres, cinco, ocho y hasta diez metros.',
             'Y tres: no adivines qué necesitás. Contanos qué trabajo vas a hacer y te asesoramos.',
             '¡Mandale este video a ese amigo que usa un cuchillo de destornillador!'],
      tomas='Número grande en pantalla en cada error (1, 2, 3) · tornillo pelado en detalle · las cuatro cintas métricas en fila.',
      prods=[('Juegos de destornilladores (desde $21.000)', None), ('Cintas métricas de 3, 5, 8 y 10 m (desde $13.500)', None)]),
 dict(n=12, sem=3, tipo='Consejos', t='Taladro común, percutor o rotomartillo', quien='Guido a cámara', loc='Pared de hormigón o bloque',
      pantalla='SI TU TALADRO LARGABA HUMO Y LA PARED NO CEDÍA, NO ERA TU CULPA.',
      guion=['Si tu taladro largaba humo y la pared no cedía, no era tu culpa: era la herramienta equivocada.',
             'Imaginate que querés colgar un estante en una pared de hormigón. Probás con un taladro común, la mecha se calienta, se gasta y te queda un agujero a medias.',
             'Para hormigón hace falta percusión: un taladro percutor para trabajos livianos, o un rotomartillo si vas a perforar mucho o picar.',
             'Contanos qué trabajo querés hacer y te decimos cuál te conviene. Escribinos por WhatsApp o pasá por Masherr.'],
      tomas='Las tres herramientas sobre el banco · perforación en hormigón con percutor y con rotomartillo (anteojos, guantes y protección auditiva).',
      prods=[('Taladro percutor 1050 W 13 mm Nebraska', 86000), ('Rotomartillo SDS Plus 1200 W Braber', 130000)]),
 dict(n=13, sem=3, tipo='Institucional', t='Lo que aprendimos detrás del mostrador', quien='Guido a cámara + familia y equipo', loc='Local completo',
      pantalla='[[53 AÑOS]]: LO QUE APRENDIMOS DETRÁS DEL MOSTRADOR',
      guion=['[[Abrimos en 1973 y seguimos acá. Esto es lo que aprendimos en cincuenta y tres años.]]',
             'Abrimos en San Martín, Gran Buenos Aires, y desde entonces vimos pasar generaciones de talleres, fábricas y oficios.',
             'Aprendimos que a quien trabaja no le sirve una herramienta cualquiera: le sirve la correcta, y a tiempo.',
             'Por eso hoy tenemos más de cuatrocientos productos de cincuenta y cinco marcas, y un equipo que te dice con franqueza qué llevar y qué no.',
             'Si nunca viniste, pasá por Masherr: queremos conocerte.'],
      tomas='Jugar con planos: atención a clientes, el local, los dueños (con su permiso), los productos y Guido mirando a cámara.',
      prods=[]),
 dict(n=14, sem=3, tipo='Empresas', t='Tu proveedor del barrio para industrias y talleres', quien='Guido a cámara', loc='Mostrador y depósito',
      pantalla='SI TU TALLER SE FRENA POR UNA PIEZA QUE NO LLEGÓ, TENEMOS QUE HABLAR.',
      guion=['Si tu taller se frena por una pieza que no llegó, tenemos que hablar.',
             'En Masherr abastecemos a industrias, talleres y profesionales de la zona con herramientas, insumos y equipos para que el trabajo no se detenga: herramientas eléctricas, discos y brocas, soldadura, medición y seguridad, de marcas como Bosch, DeWalt, Milwaukee y Esab.',
             '[[Tenemos 53 años de experiencia]] trabajando con grandes clientes. Conocemos el ritmo de tu trabajo.',
             'Escribinos por WhatsApp con lo que necesitás, o pasá por Masherr, Calle 38, número 4335, y armamos tu pedido.'],
      tomas='Guido revisando un pedido largo · cajas preparadas · marcas mencionadas en góndola.',
      prods=[]),
]

def resaltar(t):
    return re.sub(r'\[\[(.+?)\]\]', r'<mark>\1</mark>', e(t))

def palabras(v):
    textos = v.get('guion') or [d for _, d in v.get('dialogo', [])]
    return len(re.sub(r'\[\[|\]\]', '', ' '.join(textos)).split())

def precio(n):
    return '$' + f'{n:,}'.replace(',', '.')

TOTAL = 3 + len(V)
def pagina(n, cab, cuerpo):
    return f'''<section class="hoja"><div class="cab"><img src="../catalogo/img/masher-logo-azul.png" alt="Masherr"><span>{e(cab)}</span></div>
<div class="cuerpo">{cuerpo}</div><div class="pie"><span>Masherr · Guion de rodaje</span><b>{n:02d} / {TOTAL:02d}</b></div></section>'''

pags = [f'''<section class="hoja oscura"><div class="barra"></div><div class="sup">MASHERR / GUION DE RODAJE</div>
<img class="logo" src="../catalogo/img/masher-logo-blanco.png" alt="Masherr máquinas - herramientas"><div class="rayas"></div>
<div class="eyebrow rotulo">Planificación de contenido · 3 semanas</div>
<h1>14 VIDEOS<br>PARA GRABAR<br>CON GUIDO.</h1>
<p class="bajada">Guiones, tomas y productos de cada video, listos para el día de rodaje.</p>
<div class="pie-t"><span>Ferretería industrial</span><b>@masherrferreteria</b></div></section>''']

orden = {'Humor': 1}
filas = ''.join(f'<li><i>{v["n"]:02d}</i><span class="t">{e(v["t"])}</span><span class="c">Semana {v["sem"]} · {v["tipo"]}</span><span class="dur">~{max(15, round(palabras(v) / 2.6 / 5) * 5)} s</span></li>' for v in V)
pags.append(pagina(2, 'Índice', f'''<div class="rotulo">Los 14 videos</div><h2>QUÉ GRABAMOS.</h2>
<ul class="indice">{filas}</ul>
<p class="ayuda">Duración estimada leyendo a ritmo natural. El texto en pantalla de cada video va en mayúsculas, como en esta guía.</p>'''))

productos = []
for v in V:
    for p, pr in v['prods']:
        if pr: productos.append(f'<li><b>{v["n"]:02d}</b> {e(p)} <span>{precio(pr)}</span></li>')
pags.append(pagina(3, 'Antes de grabar', f'''<div class="rotulo">Checklist del día</div><h2>ANTES DE GRABAR.</h2>
<div class="nota ojo"><span><b>Confirmar la antigüedad.</b> Los videos 1, 13 y 14 dicen <mark>“desde 1973 / 53 años”</mark> y el 6 dice <mark>“más de 50 años”</mark>. Antes de publicar, confirmar el año de fundación para que todas las piezas digan lo mismo (lo marcado en amarillo).</span></div>
<div class="nota" style="margin-top:10px"><span><b>Video 3, guion nuevo.</b> En el documento original tenía el mismo texto que el video 2. Se propone un guion a partir de la ficha del producto: revisarlo antes de grabar.</span></div>
<div class="rotulo" style="margin-top:16px">Productos a tener listos</div>
<ul class="prods">{''.join(productos)}</ul>
<div class="rotulo" style="margin-top:12px">Orden sugerido para grabar</div>
<ol class="pasos"><li><b>Mostrador con actores:</b> humor 05 y 09 (convocar a 3 personas como clientes).</li>
<li><b>Banco de trabajo:</b> productos 03, 04, 07, 08, 10 y la demostración del 12.</li>
<li><b>Guido a cámara:</b> 01, 02, 06, 11, 13 y 14. Cerrar con planos generales del local.</li></ol>
<p class="ayuda">Grabar vertical (9:16), con buena luz, sonido limpio y elementos de protección en cada demostración. Pedir permiso a toda persona que aparezca.</p>'''))

for i, v in enumerate(V, 4):
    if v.get('dialogo'):
        cuerpo_guion = '<div class="dialogo">' + ''.join(f'<p><b>{e(q)}:</b> {resaltar(d)}</p>' for q, d in v['dialogo']) + '</div>'
    else:
        cuerpo_guion = '<div class="guion">' + ''.join(f'<p>{resaltar(p)}</p>' for p in v['guion']) + '</div>'
    prods = ''.join(f'<tr><td>{e(p)}</td><td class="pr">{precio(pr) if pr else "—"}</td></tr>' for p, pr in v['prods'])
    dur = max(15, round(palabras(v) / 2.6 / 5) * 5)
    pags.append(pagina(i, f'Video {v["n"]:02d}', f'''<div class="meta"><span class="rotulo">Video {v["n"]:02d} · Semana {v["sem"]}</span><span class="chip {v["tipo"].lower()}">{e(v["tipo"])}</span><span class="chip gris">~{dur} s</span>{'<span class="chip nuevo">Guion nuevo: revisar</span>' if v.get('nuevo') else ''}</div>
<h2 class="idea">{e(v["t"].upper())}</h2>
<div class="ficha"><div><b>Quién</b>{e(v["quien"])}</div><div><b>Dónde</b>{e(v["loc"])}</div></div>
<div class="gancho"><b>TEXTO EN PANTALLA</b>{resaltar(v["pantalla"])}</div>
{cuerpo_guion}
{f'<table class="tabla"><tr><th>Producto</th><th>Precio</th></tr>{prods}</table>' if prods else ''}
<div class="dos"><div><b>Tomas</b>{e(v["tomas"])}</div><div><b>Placa final</b>{e(CIERRE)}{f'<br><br><b>Referencia</b>{e(v["ref"])}' if v.get('ref') else ''}</div></div>'''))

CSS = (AQUI / 'estilo.css').read_text() + '''
mark { background: #FFE58A; color: inherit; padding: 0 3px; }
.gancho mark { color: var(--negro); }
.dos > div { min-width: 0; overflow-wrap: anywhere; }
.ficha { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 12px; font-size: 16px; }
.ficha div { background: var(--gris); padding: 10px 12px; }
.ficha b { display: block; font-family: "Cond"; color: var(--azul); font-size: 14px; letter-spacing: .08em; text-transform: uppercase; }
.guion p, .dialogo p { font-size: 19px; line-height: 1.45; margin-bottom: 10px; }
.guion { border-left: 4px solid var(--azul); padding-left: 16px; margin-bottom: 12px; }
.dialogo p b { font-family: "Cond"; color: var(--azul); font-size: 19px; }
.chip.institucional { background: var(--negro); } .chip.producto { background: var(--azul); } .chip.humor { background: #B4531A; }
.chip.consejos { background: var(--verde); } .chip.empresas { background: #4A3A8C; } .chip.nuevo { background: #FFE58A; color: var(--negro); }
.indice .dur { font-family: "Cond"; font-size: 15px; color: var(--azul); width: 54px; text-align: right; }
.indice .c { width: 160px; }
.prods { list-style: none; border-top: 1px solid var(--linea); }
.prods li { display: flex; gap: 10px; padding: 7px 0; border-bottom: 1px solid var(--linea); font-size: 15px; line-height: 1.35; }
.prods li b { font-family: "Cond"; color: var(--celeste); width: 24px; flex: none; }
.prods li span { margin-left: auto; font-family: "Cond"; color: var(--azul); white-space: nowrap; }
.nota.ojo { border-left-color: #B42318; background: #FDECEA; }
'''
(AQUI / 'guion_rodaje.html').write_text(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Masherr · Guion de rodaje</title><style>{CSS}</style></head><body>{"".join(pags)}</body></html>')
print(TOTAL, 'páginas')
