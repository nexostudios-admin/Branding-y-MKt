"""20 videos para TikTok e Instagram orientados a venta corporativa (industria, talleres, maquinaria)
y a explicar cómo usar masherrferreteria.com.ar. 10 para grabar hoy (solo local + celular) y 10 para la semana que viene.
Uso: python3 generar_corporativo.py && node exportar_corporativo.js
Sin precios. Lo marcado con [[...]] hay que confirmarlo con Masherr antes de publicar (se resalta en amarillo).
"""
import html, re
from pathlib import Path

AQUI = Path(__file__).parent
e = lambda s: html.escape(s, quote=True)
CIERRE = 'masherrferreteria.com.ar/empresas · WhatsApp 11 3182-6166 · Calle 38 4335, Villa Lynch'

H, S = 'Hoy', 'Semana que viene'
V = [
 # ------------------------------------------------------------------ HOY: local + celular, sin actores externos
 dict(n=1, cuando=H, tipo='Web', t='Cotizá para tu empresa en 1 minuto', formato='Tutorial con pantalla del celular',
      quien='Guido a cámara + grabación de pantalla', loc='Mostrador',
      pantalla='¿COMPRÁS PARA UNA EMPRESA? MIRÁ ESTO',
      guion=['Si comprás para una empresa o un taller, no hace falta que llames ni que vengas a preguntar uno por uno.',
             'Entrás a masherrferreteria.com.ar y tocás “Empresas”.',
             'Ponés tu nombre, la empresa y el CUIT si necesitás factura.',
             'Contás qué trabajo tienen que resolver y escribís los productos con cantidades, uno por línea.',
             'Elegís si lo retirás o te lo enviamos, y tocás “Enviar consulta por WhatsApp”.',
             'Te respondemos por WhatsApp con disponibilidad y cotización.'],
      tomas='Pantalla del celular en cada campo del formulario (escribir “20 discos de corte 115 mm”) · Guido mostrando el celular a cámara · WhatsApp abriéndose con la consulta armada.',
      porque='Le saca la fricción al comprador de una empresa: arma el pedido completo en un solo mensaje.',
      prods=[]),
 dict(n=2, cuando=H, tipo='Web', t='Tu cuenta empresa en Masherr', formato='Tutorial con pantalla del celular',
      quien='Guido a cámara + grabación de pantalla', loc='Mostrador',
      pantalla='CUENTA EMPRESA: CÓMO SE PIDE',
      guion=['Si tu empresa nos compra seguido, pedí tu cuenta empresa en la web.',
             'Te registrás en “Mi cuenta”, entrás a la pestaña “Empresa” y completás razón social, CUIT, condición frente al IVA y rubro.',
             'Nosotros la revisamos y, cuando queda aprobada, la ves en tu cuenta [[con las condiciones especiales que acordemos]].',
             'Y todos tus pedidos quedan guardados en un solo lugar.'],
      tomas='Pantalla: registro → pestaña Empresa → formulario → estado “pendiente” y “aprobada” (usar una cuenta de prueba) · Guido señalando el celular.',
      porque='Muestra que Masherr está preparado para trabajar con empresas y no solo con el cliente de mostrador.',
      prods=[]),
 dict(n=3, cuando=H, tipo='Web', t='Repetí el pedido del mes en un toque', formato='Tip rápido',
      quien='Guido + grabación de pantalla', loc='Banco con insumos',
      pantalla='¿PEDÍS LO MISMO TODOS LOS MESES?',
      guion=['Discos, lubricante, puntas… ¿pedís lo mismo todos los meses?',
             'En “Mi cuenta”, pestaña “Pedidos”, tenés todo lo que nos pediste.',
             'Tocás “Repetir pedido”, se carga el carrito igual que la vez anterior y lo mandás por WhatsApp.',
             'Lo podés ajustar antes de enviarlo: sacás algo o cambiás cantidades.'],
      tomas='Insumos apilados en el banco · pantalla con el botón “Repetir pedido” · carrito cargándose solo.',
      porque='El comprador de planta repite compras; el video le muestra cómo ahorrar tiempo cada mes.',
      prods=['Pack x 5 discos de corte de acero 115 mm Bosch', 'Lubricante multiuso WD-40 x 311 g', 'Set 250 puntas PH2 50 mm alto impacto Milwaukee']),
 dict(n=4, cuando=H, tipo='Web', t='Buscá por código, marca o producto', formato='Tip rápido',
      quien='Guido + grabación de pantalla', loc='Mostrador',
      pantalla='¿TENÉS EL CÓDIGO? BUSCALO ASÍ',
      guion=['Si en la planta te pasan el código o la marca, buscalo directo en la web.',
             'Escribís “GWS”, “Packout” o “DeWalt” en el buscador y te aparece todo lo que tenemos.',
             'Podés filtrar por categoría y marca para llegar más rápido.',
             '¿No lo encontrás? Escribinos: lo conseguimos o te recomendamos una alternativa.'],
      tomas='Pantalla: buscador con “Packout”, luego “DeWalt”, filtros por marca · Guido sosteniendo el producto real que apareció en la búsqueda.',
      porque='Los compradores industriales piden por código; mostrar que el buscador funciona así les da confianza.',
      prods=['Caja Organizador Packout Milwaukee 48-22-8430', 'Amoladora Angular 115 mm 800W DWE 4020 DeWalt']),
 dict(n=5, cuando=H, tipo='Web', t='La lista del taller, con el corazón', formato='Tip rápido',
      quien='Guido + grabación de pantalla', loc='Mostrador',
      pantalla='GUARDÁ LO QUE TU TALLER USA',
      guion=['¿Hay herramientas e insumos que tu taller usa siempre?',
             'Tocá el corazón en cada producto de la web y quedan guardados en tus favoritos.',
             'Si iniciaste sesión, los ves desde cualquier celular o computadora.',
             'Cuando necesitás reponer, entrás a favoritos y armás el pedido en segundos.'],
      tomas='Pantalla tocando corazones en 4 productos · contador de favoritos subiendo en el encabezado · lista de favoritos abierta.',
      porque='Convierte la web en la “lista de compras” del taller y hace que vuelvan a entrar.',
      prods=[]),
 dict(n=6, cuando=H, tipo='Insumos', t='5 insumos que una planta no puede quedarse sin', formato='Listado numerado',
      quien='Guido a cámara', loc='Mostrador con los productos en fila',
      pantalla='5 INSUMOS QUE TU PLANTA NO PUEDE QUEDARSE SIN',
      guion=['Cinco insumos que en una planta nunca pueden faltar.',
             'Uno: discos de corte. Si se terminan, se frena el taller.',
             'Dos: discos flap, para desbastar y terminar soldaduras.',
             'Tres: lubricante, para mantenimiento y para que nada se trabe.',
             'Cuatro: puntas de atornillar de impacto, que se gastan más de lo que pensás.',
             'Cinco: mechas, del diámetro que más usan.',
             'Pedinos tu lista por WhatsApp o desde la web y te armamos el pedido.'],
      tomas='Número grande en pantalla (1 a 5) · cada producto entra en cuadro desde un costado · cierre con todos juntos.',
      porque='Los listados numerados se guardan y se comparten entre compañeros de trabajo.',
      prods=['Pack x 5 discos de corte de acero 115 mm Bosch', 'Disco flap 115 mm grano 120 Pegaso', 'Lubricante multiuso WD-40',
             'Set 250 puntas PH2 alto impacto Milwaukee', 'Juego de mechas Bremen x 25 piezas 6498']),
 dict(n=7, cuando=H, tipo='Maquinaria', t='¿Qué soldadora necesita tu taller?', formato='Comparación de línea',
      quien='Guido a cámara', loc='Mostrador con las soldadoras en fila',
      pantalla='140, 160, 190 O 250: ¿CUÁL TE CONVIENE?',
      guion=['Cuatro soldadoras inverter Pegaso. ¿Cuál necesitás?',
             'La 140 es para mantenimiento liviano y arreglos.',
             'La 160 y la 190 PRO, para herrería de todos los días.',
             'La C250 PRO, para trabajo intensivo de taller o planta.',
             'Y con cualquiera, máscara fotosensible: no es opcional.',
             'Contanos qué soldás, con qué electrodo y cuántas horas por día, y te decimos cuál llevar.'],
      tomas='Las 4 soldadoras de menor a mayor · detalle del panel de cada una · Guido se pone la máscara al cierre.',
      porque='Ordena una decisión de compra grande y posiciona a Masherr como quien asesora.',
      prods=['Soldadora Inverter SI 140 Pegaso', 'Soldadora Inverter SI 160 PRO Pegaso', 'Soldadora Inverter SI 190 PRO Pegaso',
             'Soldadora Inverter SI C250 PRO Pegaso', 'Máscara fotosensible para soldador EDGE-500S Foxtter']),
 dict(n=8, cuando=H, tipo='Maquinaria', t='Compresor: ¿25, 50 o 100 litros?', formato='Comparación de línea',
      quien='Guido a cámara', loc='Depósito o pasillo con los compresores',
      pantalla='¿QUÉ COMPRESOR NECESITA TU TALLER?',
      guion=['¿Compresor de 25, 50 o 100 litros?',
             'El de 25 alcanza para inflar, sopletear y una clavadora chica.',
             'El de 50 ya mueve herramientas neumáticas un rato largo.',
             'Si usás neumáticas todo el día, como llave de impacto, lijadora o arenador, andá al de 100.',
             'Decinos qué herramientas vas a conectar y te recomendamos el tamaño.'],
      tomas='Los 3 compresores en fila · detalle del manómetro · herramientas neumáticas Bremen al lado del de 100.',
      porque='Responde una de las consultas más comunes de talleres con una regla fácil de recordar.',
      prods=['Compresor de aire 25 L 2HP Foxtter', 'Compresor de aire 50 L 2HP Foxtter', 'Compresor de aire 100 L 3HP Foxtter',
             'Llave de impacto neumática 1/2" uso intensivo Bremen 5921']),
 dict(n=9, cuando=H, tipo='Maquinaria', t='Equipá el banco de mantenimiento', formato='Recorrido (tour) por un banco armado',
      quien='Guido a cámara', loc='Banco de trabajo armado con las máquinas',
      pantalla='ASÍ SE ARMA UN BANCO DE MANTENIMIENTO',
      guion=['Si estás armando el sector de mantenimiento, esto es lo básico.',
             'Morsa de banco con base giratoria, para sujetar cualquier pieza.',
             'Taladro de banco, para agujeros derechos y repetidos.',
             'Amoladora de banco, para afilar y desbarbar.',
             'Y una sierra sensitiva, para cortar perfiles a medida.',
             'Te armamos el banco completo: mandanos el listado y lo cotizamos todo junto.'],
      tomas='Paneo lento de izquierda a derecha por el banco · cada máquina funcionando 2 segundos (con protección) · plano general al cierre.',
      porque='Le habla directo al jefe de mantenimiento y abre la puerta a una compra de varios equipos a la vez.',
      prods=['Morsa de banco base giratoria 3" Lusqtoff', 'Taladro de banco con morsa 16 mm 375W Nebraska',
             'Amoladora de banco 1/2HP 152 mm DW 752 DeWalt', 'Sierra sensitiva 14" 2200W Nebraska']),
 dict(n=10, cuando=H, tipo='Web', t='Retiro o envío: vos elegís', formato='Tip rápido',
      quien='Guido a cámara + grabación de pantalla', loc='Mostrador con pedidos preparados',
      pantalla='¿LO RETIRÁS O TE LO MANDAMOS?',
      guion=['Cuando hacés tu pedido en la web, elegís cómo recibirlo.',
             'Retiro en el local: te avisamos por WhatsApp cuando está listo y pasás por Calle 38 4335.',
             'Envío: cargás la dirección y [[coordinamos el envío y su costo]] por WhatsApp.',
             'Y si necesitás factura, completás los datos en el mismo pedido.'],
      tomas='Pantalla del carrito con las dos opciones · bolsas de pedidos con nombre en el mostrador · cajas listas para despachar.',
      porque='Resuelve dos dudas típicas de empresas (cómo llega y si hay factura) en un solo video.',
      prods=[]),
 # ------------------------------------------------------------------ SEMANA QUE VIENE: con clientes, demostraciones y salidas
 dict(n=11, cuando=S, tipo='Empresas', t='Así llega tu pedido a la planta', formato='Detrás de escena',
      quien='Guido + cliente real (con permiso)', loc='Local y planta del cliente',
      pantalla='DEL MOSTRADOR A TU PLANTA',
      guion=['Este pedido entró por WhatsApp a la mañana.',
             'Lo armamos, lo controlamos ítem por ítem y lo cargamos.',
             '(En la planta del cliente) Y acá está, en la planta, listo para usar.',
             'Si tu empresa necesita que no le falte nada, escribinos.'],
      tomas='Lista de pedido en el celular · armado en el mostrador · control con tilde · carga · llegada y entrega en la planta del cliente.',
      porque='Muestra el servicio completo y da prueba social con un cliente real.',
      prods=[], preparar='Coordinar con un cliente industrial una entrega real y pedir permiso para filmar (sin mostrar datos de su empresa si no quiere).'),
 dict(n=12, cuando=S, tipo='Empresas', t='Lo que dice un cliente de taller', formato='Testimonio real',
      quien='Cliente real (dueño o encargado de un taller)', loc='Taller del cliente o local',
      pantalla='¿POR QUÉ NOS COMPRA ESTE TALLER?',
      guion=['Tres preguntas, respuestas con sus palabras (no escribirlas antes):',
             '¿Qué hace tu taller?',
             '¿Qué le comprás a Masherr y por qué?',
             '¿Qué le dirías a otro taller que está buscando proveedor?'],
      tomas='Cliente en su lugar de trabajo · insertos de su taller trabajando · cierre con el cliente y Guido juntos.',
      porque='Un testimonio real convence a otras empresas más que cualquier publicidad. No se inventa ni se guioniza la respuesta.',
      prods=[], preparar='Elegir un cliente con buena relación y pedirle permiso. Publicar solo lo que diga de verdad.'),
 dict(n=13, cuando=S, tipo='Demostración', t='Cortar un perfil: sensitiva, amoladora o inalámbrica', formato='Comparación con prueba real',
      quien='Guido', loc='Banco o vereda con perfiles de hierro',
      pantalla='3 FORMAS DE CORTAR EL MISMO PERFIL',
      guion=['Mismo perfil, tres herramientas.',
             'Sierra sensitiva: corte derecho y repetible, ideal para producción.',
             'Amoladora grande: la llevás a donde está la pieza.',
             'Amoladora inalámbrica: para cortes en altura o donde no hay enchufe.',
             '¿Cuál necesitás vos? Contanos el trabajo y te asesoramos.'],
      tomas='Pantalla dividida en tres · cronómetro en cada corte · detalle de las chispas · protección visible (anteojos, guantes, protector auditivo).',
      porque='Demostración honesta que ayuda a elegir y muestra máquinas de mayor valor.',
      prods=['Sierra sensitiva 14" 2200W Nebraska', 'Amoladora angular 180 mm 2200W DWE491 DeWalt',
             'Amoladora M18 115 mm Milwaukee 2886-20']),
 dict(n=14, cuando=S, tipo='Demostración', t='Neumáticas en acción', formato='Satisfying con sonido real',
      quien='Guido (manos)', loc='Taller con el compresor de 100 L',
      pantalla='TODO ESTO FUNCIONA CON UN COMPRESOR',
      guion=['Sin voz: compresor encendido y cada herramienta funcionando unos segundos.',
             'Texto final: “¿Armás tu línea neumática? Pedí la cotización por WhatsApp.”'],
      tomas='Clavadora sobre madera · remachadora uniendo chapa · lijadora orbital · arenador sobre una pieza oxidada (antes/después) · llave de impacto aflojando un bulón.',
      porque='El sonido y el antes/después del arenador hacen que el video se mire completo.',
      prods=['Compresor de aire 100 L 3HP Foxtter', 'Clavadora neumática 15-50 mm Bremen 7264', 'Remachadora neumática Bremen 7471',
             'Lijadora roto orbital neumática 5" Bremen 7518', 'Arenador neumático Bremen 4648'],
      preparar='Tener piezas de prueba: madera, chapa y una pieza oxidada para el arenador.'),
 dict(n=15, cuando=S, tipo='Maquinaria', t='Turno noche en planta', formato='POV / historia corta',
      quien='Guido (como operario)', loc='Depósito con poca luz',
      pantalla='POV: TE TOCA EL TURNO NOCHE',
      guion=['Se corta la luz en el sector y hay que terminar el trabajo.',
             'Torre reflector a batería: la prendés y se ilumina todo.',
             'Llave de impacto de 3/4 para los bulones grandes.',
             'Rotomartillo a batería para anclar sin buscar enchufe.',
             'Todo con la misma línea de baterías M18. Consultanos por WhatsApp.'],
      tomas='Empieza a oscuras · se enciende la torre (golpe de luz) · cada herramienta trabajando · plano final con todo iluminado.',
      porque='El cambio de oscuridad a luz engancha en el primer segundo y muestra herramientas de alto valor.',
      prods=['Torre reflector LED Milwaukee M18 2131-20', 'Llave de impacto a batería Milwaukee 2864 3/4"',
             'Rotomartillo inalámbrico SDS-Plus FUEL Milwaukee 2912-20', 'Batería M18 Redlithium Forge HD12.0 Milwaukee']),
 dict(n=16, cuando=S, tipo='Consejos', t='Mantenimiento preventivo en 30 segundos', formato='Listado numerado',
      quien='Guido a cámara', loc='Banco con una máquina de muestra',
      pantalla='LAS MÁQUINAS NO SE ROMPEN DE UN DÍA PARA EL OTRO',
      guion=['Tres cosas que alargan la vida de tus máquinas.',
             'Uno: engrasar según el manual. Con una engrasadora a batería no hay excusa.',
             'Dos: lubricar mecanismos y proteger de la humedad.',
             'Tres: limpiar el polvo de las rejillas de los motores.',
             'Si tenés dudas de qué usar en cada máquina, preguntanos.'],
      tomas='Engrasadora en un punto de engrase · lubricante en un mecanismo · soplado de una rejilla con compresor (con anteojos).',
      porque='Contenido útil para el jefe de mantenimiento; posiciona a Masherr como experto.',
      prods=['Engrasadora 2 velocidades a batería 18V Milwaukee 2646-20', 'Lubricante multiuso WD-40', 'Lubricante seco WD-40']),
 dict(n=17, cuando=S, tipo='Web', t='Mandanos la lista como la tengas', formato='Tutorial corto',
      quien='Guido a cámara', loc='Mostrador',
      pantalla='¿TENÉS LA LISTA EN PAPEL? MANDALA ASÍ',
      guion=['¿Tenés el pedido anotado en un papel o en una planilla?',
             'Sacale una foto y mandala por WhatsApp, o copiala en el formulario de Empresas de la web.',
             'Nosotros la pasamos, te confirmamos disponibilidad y te mandamos la cotización.',
             'Si algo no lo tenemos, te ofrecemos una alternativa.'],
      tomas='Lista escrita a mano real · foto con el celular · mensaje enviado · Guido revisando la lista en el mostrador.',
      porque='Baja la barrera para el comprador que no quiere cargar producto por producto.',
      prods=[], preparar='Escribir una lista de ejemplo a mano (sin datos reales de clientes).'),
 dict(n=18, cuando=S, tipo='Demostración', t='¿Cuántos cortes hace un disco?', formato='Prueba real (dosis de realidad)',
      quien='Guido', loc='Banco con perfiles de hierro',
      pantalla='¿CUÁNTOS CORTES TE DURA UN DISCO?',
      guion=['Pregunta que nos hacen siempre: ¿cuántos cortes hace un disco?',
             'Lo probamos: mismo perfil, misma amoladora, contando cada corte.',
             '(Resultado real en pantalla.)',
             'Depende del material, la presión y la máquina. Contanos qué cortás y te decimos qué disco rinde más para tu trabajo.'],
      tomas='Contador en pantalla sumando cortes · disco nuevo vs. disco gastado al lado · resultado final grande.',
      porque='Para una empresa importa el rendimiento, no solo el precio. Mostrar el número real (sea cual sea) genera confianza.',
      prods=['Pack x 5 discos de corte de acero 115 mm Bosch', 'Amoladora angular 115 mm 800W DWE 4020 DeWalt'],
      preparar='Hacer la prueba de verdad y publicar el número que salga. No comparar contra otras marcas sin probarlas.'),
 dict(n=19, cuando=S, tipo='Maquinaria', t='Inalámbricas para planta: una batería para todo', formato='Explicación con productos',
      quien='Guido a cámara', loc='Mostrador con la línea M18 en fila',
      pantalla='UNA BATERÍA PARA TODAS TUS HERRAMIENTAS',
      guion=['Si tu empresa va a pasar a inalámbricas, elegí una sola línea de baterías.',
             'Con la misma batería M18 usás taladro, llave de impacto, amoladora, caladora y hasta la torre de luz.',
             'Menos cargadores, menos baterías y el operario agarra la que esté cargada.',
             'Armamos el kit según lo que usa tu equipo. Escribinos.'],
      tomas='Una batería pasando de herramienta en herramienta (clic) · fila completa de herramientas M18 · cargador con dos baterías.',
      porque='Explica un criterio de compra que le sirve a la empresa y lleva a una venta de varios equipos.',
      prods=['Taladro percutor M18 Milwaukee 3602-20', 'Llave de impacto M18 FUEL 1/2" Milwaukee 2962-20',
             'Amoladora M18 115 mm Milwaukee 2886-20', 'Sierra caladora M18 Milwaukee 2737', 'Batería M18 Redlithium Forge XC8.0 Milwaukee']),
 dict(n=20, cuando=S, tipo='Empresas', t='Por qué las empresas de la zona compran en Masherr', formato='Institucional corto',
      quien='Guido a cámara', loc='Local completo y depósito',
      pantalla='TU PROVEEDOR INDUSTRIAL EN VILLA LYNCH',
      guion=['Si tenés una industria o un taller en San Martín y alrededores, esto te interesa.',
             'Tenemos marcas de primera línea: Bosch, DeWalt, Milwaukee, Stanley, Bremen, Fischer.',
             'Te asesoramos antes de comprar y te armamos el pedido completo.',
             'Pedís por WhatsApp o desde la web, con retiro o envío, y con factura si la necesitás.',
             'Masherr, Calle 38 4335, Villa Lynch. Escribinos y armamos tu cuenta empresa.'],
      tomas='Planos del local, góndolas por marca, depósito, pedidos preparados y Guido a cámara al cierre.',
      porque='Cierra la serie resumiendo todo lo que Masherr ofrece a empresas; sirve para fijar en el perfil.',
      prods=[]),
]

def resaltar(t):
    return re.sub(r'\[\[(.+?)\]\]', r'<mark>\1</mark>', e(t))

def palabras(v):
    return len(re.sub(r'\[\[|\]\]', '', ' '.join(v['guion'])).split())

def dur(v):
    if v['n'] == 14: return 20
    if v['n'] == 12: return 40
    if v['tipo'] in ('Demostración', 'Empresas') or v['n'] == 11: return max(30, round(palabras(v) / 2.6 / 5) * 5)
    return max(15, round(palabras(v) / 2.6 / 5) * 5)

TOTAL = 4 + len(V)
def pagina(n, cab, cuerpo):
    return f'''<section class="hoja"><div class="cab"><img src="../catalogo/img/masher-logo-azul.png" alt="Masherr"><span>{e(cab)}</span></div>
<div class="cuerpo">{cuerpo}</div><div class="pie"><span>Masherr · Videos para empresas e industria</span><b>{n:02d} / {TOTAL:02d}</b></div></section>'''

pags = [f'''<section class="hoja oscura"><div class="barra"></div><div class="sup">MASHERR / VIDEOS PARA EMPRESAS</div>
<img class="logo" src="../catalogo/img/masher-logo-blanco.png" alt="Masherr máquinas - herramientas"><div class="rayas"></div>
<div class="eyebrow rotulo">TikTok + Instagram · Venta corporativa</div>
<h1>20 VIDEOS<br>PARA EMPRESAS,<br>INDUSTRIA Y TALLERES.</h1>
<p class="bajada">10 para grabar hoy y 10 para la semana que viene. Maquinaria, insumos y cómo usar la web para comprar.</p>
<div class="pie-t"><span>Ferretería industrial</span><b>@masherrferreteria</b></div></section>''']

def bloque(nombre):
    return ''.join(f'<li><i>{v["n"]:02d}</i><span class="t">{e(v["t"])}<small>{e(v["formato"])}</small></span><span class="c">{e(v["tipo"])}</span><span class="dur">~{dur(v)} s</span></li>' for v in V if v['cuando'] == nombre)
pags.append(pagina(2, 'Índice', f'''<div class="rotulo">Para grabar hoy</div>
<ul class="indice">{bloque(H)}</ul>
<div class="rotulo" style="margin-top:16px">Para grabar la semana que viene</div>
<ul class="indice">{bloque(S)}</ul>'''))

prods_hoy = ''.join(f'<li><b>{v["n"]:02d}</b> {e(p)}</li>' for v in V if v['cuando'] == H for p in v['prods'])
pags.append(pagina(3, 'Hoy', f'''<div class="rotulo">Checklist de hoy</div><h2>ANTES DE GRABAR.</h2>
<div class="nota ojo"><span><b>Confirmar antes de publicar</b> lo marcado en <mark>amarillo</mark>: si la cuenta empresa tiene condiciones especiales (video 02) y cómo se cobra el envío (video 10). Sin precios en ningún video.</span></div>
<div class="nota" style="margin-top:10px"><span><b>Grabaciones de pantalla:</b> los videos 01 a 05 y 10 usan el celular. Grabar la pantalla con la web abierta (en iPhone: Centro de control → Grabar pantalla) y una cuenta de prueba, nunca la de un cliente.</span></div>
<div class="rotulo" style="margin-top:14px">Productos a tener listos hoy</div>
<ul class="prods">{prods_hoy}</ul>
<div class="rotulo" style="margin-top:12px">Orden sugerido</div>
<ol class="pasos"><li><b>Celular y mostrador:</b> 01, 02, 03, 04, 05 y 10 (mismo encuadre, cambia la pantalla).</li>
<li><b>Productos en fila:</b> 06, 07 y 08.</li>
<li><b>Banco armado:</b> 09 (con protección al encender cada máquina).</li></ol>'''))

prep = ''.join(f'<li><b>{v["n"]:02d}</b> {e(v["preparar"])}</li>' for v in V if v.get('preparar'))
prods_sem = ''.join(f'<li><b>{v["n"]:02d}</b> {e(p)}</li>' for v in V if v['cuando'] == S for p in v['prods'])
pags.append(pagina(4, 'Semana que viene', f'''<div class="rotulo">Para organizar en la semana</div><h2>SEMANA QUE VIENE.</h2>
<div class="rotulo">Qué hay que coordinar</div>
<ul class="prods uno">{prep}</ul>
<div class="rotulo" style="margin-top:14px">Productos a tener listos</div>
<ul class="prods">{prods_sem}</ul>
<p class="ayuda" style="margin-top:12px">Vertical 9:16, buena luz y sonido limpio. Elementos de protección en cada demostración. Pedir permiso por escrito a clientes y empresas que aparezcan. Hashtags del rubro y la zona: #ferreteriaindustrial #herramientas #mantenimientoindustrial #villalynch #sanmartin.</p>'''))

for i, v in enumerate(V, 5):
    cuerpo_guion = '<div class="guion">' + ''.join(f'<p>{resaltar(p)}</p>' for p in v['guion']) + '</div>'
    prods = ''.join(f'<li>{e(p)}</li>' for p in v['prods'])
    clase = 'hoy' if v['cuando'] == H else 'sem'
    pags.append(pagina(i, f'Video {v["n"]:02d}', f'''<div class="meta"><span class="rotulo">Video {v["n"]:02d}</span><span class="chip c-{clase}">{e(v["cuando"])}</span><span class="chip gris">{e(v["tipo"])}</span><span class="chip gris">~{dur(v)} s</span></div>
<h2 class="idea">{e(v["t"].upper())}</h2>
<div class="ficha"><div><b>Formato</b>{e(v["formato"])}</div><div><b>Quién · Dónde</b>{e(v["quien"])} · {e(v["loc"])}</div></div>
<div class="gancho"><b>TEXTO EN PANTALLA (PRIMEROS 2 SEGUNDOS)</b>{e(v["pantalla"])}</div>
{cuerpo_guion}
{f'<div class="lista-prod"><b>Productos</b><ul>{prods}</ul></div>' if prods else ''}
<div class="dos"><div><b>Tomas</b>{e(v["tomas"])}</div><div><b>Por qué funciona</b>{e(v["porque"])}<br><br><b>Placa final</b>{e(CIERRE)}</div></div>'''))

CSS = (AQUI / 'estilo.css').read_text() + '''
mark { background: #FFE58A; color: inherit; padding: 0 3px; }
.dos > div { min-width: 0; overflow-wrap: anywhere; }
.ficha { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 12px; font-size: 15px; line-height: 1.35; }
.ficha div { background: var(--gris); padding: 10px 12px; }
.ficha b { display: block; font-family: "Cond"; color: var(--azul); font-size: 14px; letter-spacing: .08em; text-transform: uppercase; }
.guion p { font-size: 17.5px; line-height: 1.4; margin-bottom: 8px; }
.guion { border-left: 4px solid var(--azul); padding-left: 16px; margin-bottom: 12px; }
.chip.c-hoy { background: #1E7A3C; } .chip.c-sem { background: var(--azul); }
.indice .t small { display: block; font-family: "Sans"; font-weight: normal; font-size: 11.5px; color: #5A6072; margin-top: 0; }
.indice li { padding-top: 3px; padding-bottom: 3px; } .indice .t { font-size: 15px; line-height: 1.2; } .indice i { font-size: 15px; }
.indice .dur { font-family: "Cond"; font-size: 15px; color: var(--azul); width: 54px; text-align: right; }
.indice .c { width: 120px; }
.prods { list-style: none; border-top: 1px solid var(--linea); columns: 2; column-gap: 18px; }
.prods.uno { columns: 1; }
.prods li { break-inside: avoid; display: flex; gap: 8px; padding: 3px 0; border-bottom: 1px solid var(--linea); font-size: 13px; line-height: 1.28; }
.prods.uno li { font-size: 14.5px; padding: 6px 0; }
.prods li b { font-family: "Cond"; color: var(--celeste); width: 24px; flex: none; }
.lista-prod { background: var(--gris); padding: 10px 14px; margin-bottom: 12px; font-size: 15px; }
.lista-prod b { font-family: "Cond"; color: var(--azul); font-size: 14px; letter-spacing: .08em; text-transform: uppercase; }
.lista-prod ul { margin: 4px 0 0 18px; } .lista-prod li { margin: 2px 0; }
.nota.ojo { border-left-color: #B42318; background: #FDECEA; }
'''
(AQUI / 'videos_empresas.html').write_text(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Masherr · Videos para empresas</title><style>{CSS}</style></head><body>{"".join(pags)}</body></html>')
print(TOTAL, 'páginas')
