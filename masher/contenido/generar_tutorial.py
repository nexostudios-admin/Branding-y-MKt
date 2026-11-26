"""Guion del video tutorial de la web, explicado por Guido (versión larga + cortes para Reels/TikTok).
Uso: python3 generar_tutorial.py && node exportar_pdf.js tutorial_web.html Masherr_Tutorial_Web_Guido.pdf
Los textos de botones y pantallas son los reales de masherrferreteria.com.ar (revisados en el código de la web).
"""
import html, re
from pathlib import Path

AQUI = Path(__file__).parent
e = lambda s: html.escape(s, quote=True)
mark = lambda t: re.sub(r'\[\[(.+?)\]\]', r'<mark>\1</mark>', e(t))

# (título, lo que dice Guido, lo que se ve en pantalla / tomas)
ESC = [
 ('Gancho', [
   'Te voy a mostrar cómo comprar en Masherr desde el celular, sin hacer fila y sin llamar.',
   'En tres minutos te explico todo: cómo crear tu usuario, cómo armar el pedido y cómo pedir como empresa.'],
  'Guido a cámara en el mostrador, con el celular en la mano. Texto en pantalla: “CÓMO COMPRAR EN MASHERR DESDE TU CELULAR”.'),
 ('1. Entrar a la web', [
   'Entrás a masherrferreteria.com.ar. Arriba tenés el buscador, las categorías y los botones de tu cuenta, favoritos y carrito.',
   'Podés buscar por producto, por marca o por código. Por ejemplo, escribo “Packout”.',
   'Y si preferís recorrer, entrás por categoría y filtrás por marca.'],
  'Grabación de pantalla: inicio de la web → buscador con “Packout” → resultados → una categoría con el filtro de marca.'),
 ('2. Crear tu usuario', [
   'Para crear tu usuario tocás el muñequito de arriba, donde dice “Ingresá”.',
   'Elegís “Crear cuenta” y completás tu nombre, tu WhatsApp, tu email y una contraseña de al menos 8 caracteres.',
   'Tocás “Crear mi cuenta” y te llega un mail de Masherr.',
   'Abrís el mail, tocás “Confirmar mi cuenta”, y listo: vuelve a la web con tu cuenta confirmada.',
   'Si no te llega, mirá en spam o en promociones.'],
  'Pantalla: ícono de cuenta (“Ingresá”) → pestaña “Crear cuenta” → formulario → botón “Crear mi cuenta” → mensaje “¡Listo! Te mandamos un mail…” → '
  'mail “Confirmá tu cuenta de Masherr” en Gmail → botón “Confirmar mi cuenta” → aviso “¡Tu cuenta quedó confirmada!”. Usar un mail de prueba.'),
 ('3. Guardar tus datos', [
   'En “Mis datos” cargás una sola vez tu dirección, los datos de factura y la forma de pago que preferís.',
   'Tocás “Guardar mis datos” y en cada pedido ya aparecen completos.'],
  'Pantalla: Mi cuenta → Mis datos → campos de dirección, factura y pago → “Guardar mis datos”.'),
 ('4. Favoritos', [
   'Lo que usás siempre, guardalo con el corazón.',
   'Lo ves en “Favoritos” desde el celular o la compu, y desde ahí lo agregás al carrito.'],
  'Pantalla: tocar el corazón en 3 productos → contador del corazón arriba → Mi cuenta → Favoritos.'),
 ('5. Armar el pedido', [
   'Agregás los productos al carrito y elegís la cantidad.',
   'Elegís “Retiro en el local” o “Envío”, que se coordina por WhatsApp.',
   'Tocás “Enviar pedido por WhatsApp” y te llega a nuestro WhatsApp con todo el detalle.',
   'Nosotros te confirmamos stock, precio y forma de pago. Si es retiro, te avisamos cuando está listo.'],
  'Pantalla: “Agregar al carrito” → carrito con cantidades → opciones “Retiro en el local” / “Envío (costo a coordinar)” → botón verde “Enviar pedido por WhatsApp” → WhatsApp con el pedido armado.'),
 ('6. Retirar en el local', [
   '(A cámara) Y cuando venís, decís tu nombre y el pedido ya está preparado. Así de simple.'],
  'Cliente (o alguien del equipo) entra al local · bolsa con el nombre en el mostrador · Guido la entrega.'),
 ('7. Repetir un pedido', [
   'Todos tus pedidos quedan en “Mis pedidos”.',
   'Si comprás lo mismo seguido, tocás “Repetir pedido”, se carga el carrito igual que la vez anterior, lo ajustás si hace falta y lo mandás.'],
  'Pantalla: Mi cuenta → Mis pedidos → botón “Repetir pedido” → carrito cargado.'),
 ('8. Cuenta empresa', [
   'Si comprás para una empresa o un taller, entrás a la pestaña “Empresa” de tu cuenta.',
   'Completás razón social, CUIT, condición frente al IVA, rubro, persona de contacto y teléfono.',
   'Tocás “Solicitar alta como empresa”. Nosotros la revisamos y te confirmamos el alta por WhatsApp.',
   'Cuando queda aprobada, lo ves en tu cuenta [[con las condiciones especiales que acordemos]].'],
  'Pantalla: Mi cuenta → Empresa → formulario → botón “Solicitar alta como empresa” → estado “Solicitud en revisión” → (cuenta de prueba aprobada) “Cuenta empresa aprobada”.'),
 ('9. Pedidos grandes sin cuenta', [
   '¿Tenés una lista larga y no querés crear usuario? Entrás a “Empresas” en el menú.',
   'Contás qué trabajo tienen que resolver, escribís los productos con cantidades, uno por línea, y para cuándo lo necesitás.',
   'Tocás “Enviar consulta por WhatsApp” y te respondemos con disponibilidad y cotización.'],
  'Pantalla: menú → Empresas → formulario (escribir “20 discos de corte 115 mm”) → “Enviar consulta por WhatsApp”.'),
 ('10. Si te olvidaste la contraseña', [
   'Si te olvidaste la contraseña, tocás “Olvidé mi contraseña”, te mandamos un enlace al mail y elegís una nueva.'],
  'Pantalla: Ingresar → “Olvidé mi contraseña” → “Enviarme el enlace” → mail “Restablecé tu contraseña de Masherr”.'),
 ('11. Comunidad Masherr', [
   'Y si querés enterarte primero de descuentos, promos y rifas, sumate a la Comunidad Masherr de WhatsApp. El link está en la web.'],
  'Pantalla: sección Comunidad de la web → botón para unirse.'),
 ('Cierre', [
   'Eso es todo: entrás, armás tu pedido, lo mandás por WhatsApp y lo retirás o te lo enviamos.',
   'Masherr, Calle 38 4335, Villa Lynch. Y si tenés dudas, escribinos: te ayudamos a hacer tu primer pedido.'],
  'Guido a cámara · placa final: masherrferreteria.com.ar · WhatsApp 11 3182-6166 · Calle 38 4335, Villa Lynch · @masherrferreteria.'),
]

CORTES = [('Cómo crear tu usuario en Masherr', 'Escenas 2 y 3', '~35 s'),
          ('Cómo hacer tu pedido y retirarlo', 'Escenas 5 y 6', '~30 s'),
          ('Favoritos y repetir pedido', 'Escenas 4 y 7', '~25 s'),
          ('Cuenta empresa', 'Escena 8', '~25 s'),
          ('Pedidos grandes para empresas', 'Escena 9', '~20 s'),
          ('Olvidé mi contraseña + Comunidad', 'Escenas 10 y 11', '~20 s')]

palabras = sum(len(' '.join(g).split()) for _, g, _ in ESC)
minutos = round(palabras / 2.6 / 60 + 0.5, 1)  # + margen para pantallas sin voz

def hoja(n, total, cuerpo):
    return f'''<section class="hoja"><div class="cab"><img src="../catalogo/img/masher-logo-azul.png" alt="Masherr"><span>Tutorial de la web</span></div>
<div class="cuerpo">{cuerpo}</div><div class="pie"><span>Masherr · Tutorial con Guido</span><b>{n:02d} / {total:02d}</b></div></section>'''

def escena(t, g, p):
    return f'''<article class="esc"><h3>{e(t)}</h3><div class="cols"><div class="dice"><b>Guido dice</b>{''.join(f'<p>{mark(x)}</p>' for x in g)}</div>
<div class="ve"><b>Se ve en pantalla</b><p>{e(p)}</p></div></div></article>'''

intro = f'''<div class="rotulo">Video tutorial · YouTube, Instagram y TikTok</div><h2>CÓMO COMPRAR EN MASHERR.</h2>
<p class="lead">Guido explica la web de punta a punta: crear el usuario, armar el pedido, retirarlo y pedir como empresa.
Versión completa de ~{minutos} minutos, más 6 cortes cortos para Reels y TikTok.</p>
<div class="nota ojo"><span><b>Antes de grabar.</b> Usar una cuenta de prueba (nunca la de un cliente) y un mail de prueba para mostrar el mail de confirmación.
Grabar la pantalla del celular (iPhone: Centro de control → Grabar pantalla) y a Guido aparte, después se combinan.
Confirmar lo marcado en <mark>amarillo</mark> antes de publicar. Sin precios.</span></div>'''

grupos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11, 12]]
total = 1 + len(grupos) + 1
hojas = [hoja(1, total, intro + escena(*ESC[0]))]
grupos = [[1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11, 12]]
for i, g in enumerate(grupos, 2):
    hojas.append(hoja(i, total, ''.join(escena(*ESC[k]) for k in g)))
filas = ''.join(f'<li><i>{n:02d}</i><span class="t">{e(a)}</span><span class="c">{e(b)}</span><span class="dur">{e(c)}</span></li>' for n, (a, b, c) in enumerate(CORTES, 1))
hojas.append(hoja(total, total, f'''<div class="rotulo">Para Reels y TikTok</div><h2>6 CORTES CORTOS.</h2>
<p class="lead">Del mismo material salen 6 videos cortos, uno por tema. Cada uno arranca con su propio texto en pantalla y termina con la placa final.</p>
<ul class="indice">{filas}</ul>
<p class="ayuda" style="margin-top:14px">La versión completa va a YouTube y como video destacado en Instagram; los cortes se publican de a uno durante dos semanas.
También sirven para mandar por WhatsApp a un cliente que pregunta “¿cómo compro por la web?”.</p>'''))

CSS = (AQUI / 'estilo.css').read_text() + '''
.lead { font-size: 17px; line-height: 1.45; margin: 6px 0 12px; }
.esc { border-top: 3px solid var(--azul); padding-top: 8px; margin-bottom: 14px; }
.esc h3 { font-family: "Cond"; font-size: 21px; text-transform: uppercase; margin-bottom: 6px; }
.cols { display: grid; grid-template-columns: 1.25fr 1fr; gap: 14px; }
.cols b { display: block; font-family: "Cond"; color: var(--azul); font-size: 13px; letter-spacing: .08em; text-transform: uppercase; margin-bottom: 3px; }
.dice p { font-size: 15.5px; line-height: 1.4; margin-bottom: 5px; }
.dice { border-left: 3px solid var(--azul); padding-left: 10px; }
.ve { background: var(--gris); padding: 8px 10px; }
.ve p { font-size: 13px; line-height: 1.4; color: #3A4052; }
.indice .c { width: 150px; } .indice .dur { font-family: "Cond"; color: var(--azul); width: 54px; text-align: right; }
mark { background: #FFE58A; color: inherit; padding: 0 2px; }
.nota.ojo { border-left-color: #B42318; background: #FDECEA; }
'''
(AQUI / 'tutorial_web.html').write_text(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Masherr · Tutorial de la web</title><style>{CSS}</style></head><body>{"".join(hojas)}</body></html>')
print(total, 'páginas ·', palabras, 'palabras · ~', minutos, 'min')
