"""Contenido de Instagram para el martes 17/11/2026 (Masherr).
Historias de apertura, cierre de mediodía, reapertura y cierre; carrusel educativo; post de la web nueva.
Uso: python3 generar.py && node exportar.js   → salida/ (PNG 2x + PDF vectorial por pieza + copys)
"""
from pathlib import Path

AQUI = Path(__file__).parent
R = '../../../'                       # hasta masher/
IMG = R + 'web/sitio/img/productos/'
F = R + 'catalogo/fonts/'
LAZ = R + 'catalogo/img/masher-logo-azul.png'
LBL = R + 'catalogo/img/masher-logo-blanco.png'
DIA, FECHA = 'MARTES', '17 · 11'
foto = lambda n: f'{IMG}{n}-1024-1024.webp'

CSS = f'''
@font-face{{font-family:C;src:url({F}DejaVuSansCondensed-Bold.ttf);font-weight:700}}
@font-face{{font-family:T;src:url({F}DejaVuSans.ttf)}}
@font-face{{font-family:T;src:url({F}DejaVuSans-Bold.ttf);font-weight:700}}
:root{{--az:#17256B;--ne:#08090B;--ce:#9AAEFF;--gr:#EEF0F4;--tx:#50566A;--li:#DDE0E7}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{background:#555}}
body{{font-family:T,sans-serif;-webkit-font-smoothing:antialiased}}
section{{position:relative;overflow:hidden}}
.story{{width:1080px;height:1920px;padding:0 96px}}
.post{{width:1080px;height:1350px;padding:0 84px}}
.claro{{background:#fff;color:var(--ne)}} .oscuro{{background:var(--ne);color:#fff}} .azul{{background:var(--az);color:#fff}} .gris{{background:var(--gr);color:var(--ne)}}
/* franjas del símbolo */
.rayas{{position:absolute;background:repeating-linear-gradient(to bottom,currentColor 0 16px,transparent 16px 28px)}}
.oscuro .rayas{{color:var(--az)}} .azul .rayas{{color:rgba(255,255,255,.09)}} .claro .rayas,.gris .rayas{{color:var(--gr)}}
.gris .rayas{{color:#E1E4EC}}
/* barra superior de historia */
.top{{position:absolute;left:96px;right:96px;top:150px;display:flex;justify-content:space-between;align-items:center}}
.top img{{height:72px}}
.top .dia{{font-family:C;font-size:30px;letter-spacing:.18em;color:var(--ce);text-align:right;line-height:1.3}}
.claro .top .dia,.gris .top .dia{{color:var(--az)}}
.rot{{font-family:C;font-size:32px;letter-spacing:.16em;color:var(--ce);display:flex;align-items:center;gap:20px}}
.rot::before{{content:"";width:64px;height:8px;background:currentColor}}
.claro .rot,.gris .rot{{color:var(--az)}}
.hora{{font-family:C;font-size:330px;line-height:.86;letter-spacing:-.02em}}
.hora small{{font-size:120px;letter-spacing:0;margin-left:10px;color:var(--ce)}}
.claro .hora small{{color:var(--az)}}
h1{{font-family:C;font-size:116px;line-height:1.0}}
.txt{{font-size:44px;line-height:1.42;color:#D5D9E4}} .claro .txt,.gris .txt{{color:var(--tx)}}
.bloque{{position:absolute;left:96px;right:96px}}
.linea{{height:3px;background:var(--ce)}} .claro .linea,.gris .linea{{background:var(--az)}}
.datos{{display:flex;justify-content:space-between;gap:30px}}
.datos div{{flex:1}} .datos b{{display:block;font-family:C;font-size:28px;letter-spacing:.14em;color:var(--ce);margin-bottom:10px}}
.claro .datos b{{color:var(--az)}}
.datos span{{font-family:C;font-size:44px;line-height:1.15}}
.boton{{display:inline-flex;align-items:center;gap:22px;font-family:C;font-size:44px;padding:30px 44px;border-radius:999px}}
.boton.wa{{background:#128C3E;color:#fff}} .boton.bl{{background:#fff;color:var(--az)}} .boton.az{{background:var(--az);color:#fff}}
.boton svg{{width:52px;height:52px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}}
.zona-sticker{{position:absolute;left:96px;right:96px;height:170px;border:3px dashed currentColor;opacity:.35;display:grid;place-items:center;font-family:C;font-size:28px;letter-spacing:.12em}}
.sol{{position:absolute;border-radius:50%}}
/* post / carrusel */
.cab{{position:absolute;left:84px;right:84px;top:70px;display:flex;justify-content:space-between;align-items:center}}
.cab img{{height:56px}} .cab span{{font-family:C;font-size:26px;letter-spacing:.14em;color:var(--az)}}
.oscuro .cab span,.azul .cab span{{color:var(--ce)}}
.pag{{position:absolute;right:84px;bottom:64px;font-family:C;font-size:26px;letter-spacing:.14em;color:var(--az)}}
.oscuro .pag,.azul .pag{{color:var(--ce)}}
.flecha{{position:absolute;left:84px;bottom:58px;display:flex;align-items:center;gap:16px;font-family:C;font-size:28px;letter-spacing:.1em;color:var(--az)}}
.oscuro .flecha,.azul .flecha{{color:var(--ce)}}
.flecha i{{display:block;width:80px;height:4px;background:currentColor;position:relative}}
.flecha i::after{{content:"";position:absolute;right:-2px;top:-9px;border:11px solid transparent;border-left:16px solid currentColor;border-right:0}}
.num{{font-family:C;font-size:200px;line-height:.8;color:var(--ce)}}
.claro .num,.gris .num{{color:var(--az)}}
.tarjeta{{position:absolute;left:84px;right:84px;top:560px;height:470px;background:#fff;border-radius:22px;display:grid;place-items:center}}
.tarjeta img{{max-height:84%;max-width:80%;mix-blend-mode:multiply}}
.tag{{display:inline-block;font-family:C;font-size:26px;letter-spacing:.12em;padding:10px 18px;border:3px solid var(--az);color:var(--az)}}
.oscuro .tag,.azul .tag{{border-color:var(--ce);color:var(--ce)}}
.tel{{position:absolute;width:520px;height:1060px;border-radius:70px;background:#000;padding:22px;box-shadow:0 40px 80px rgba(0,0,0,.35)}}
.tel img{{width:100%;height:100%;object-fit:cover;object-position:top;border-radius:50px}}
.tel::before{{content:"";position:absolute;left:50%;top:40px;transform:translateX(-50%);width:130px;height:34px;border-radius:20px;background:#000;z-index:2}}
'''
WA = '<svg viewBox="0 0 24 24"><path d="M3.5 20.5l1.4-4.2A8.5 8.5 0 1 1 8 19.3z"/><path d="M9 8.6c.2 2.9 2.6 5.4 5.6 6l1.3-1.4-2-1.1-1 .7c-.9-.4-2-1.5-2.4-2.4l.7-1-1-2z"/></svg>'
WEB = '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 2.5 15.3 0 18M12 3c-2.5 2.7-2.5 15.3 0 18"/></svg>'

def top(logo):
    return f'<div class="top"><img src="{logo}" alt="Masherr"><div class="dia">{DIA}<br>{FECHA}</div></div>'

PIEZAS = []  # (archivo, tipo, html, texto)

# ------------------------------------------------------------------ HISTORIAS DEL DÍA
PIEZAS.append(('historia_1_0800_abrimos', 'story', f'''<section class="story azul">
<div class="rayas" style="right:0;top:0;width:420px;height:760px;clip-path:polygon(32% 0,100% 0,100% 100%,0 100%)"></div>
{top(LBL)}
<div class="bloque" style="top:560px"><div class="rot">BUEN DÍA · ABRIMOS</div></div>
<div class="bloque" style="top:650px"><div class="hora">8:00<small>hs</small></div></div>
<div class="bloque" style="top:1000px"><h1>La persiana<br>ya está arriba.</h1>
<p class="txt" style="margin-top:36px">Pasá por el mostrador o mandanos tu lista por WhatsApp y te la dejamos lista para retirar.</p></div>
<div class="bloque" style="top:1520px"><div class="linea"></div>
<div class="datos" style="margin-top:34px"><div><b>HOY</b><span>8 a 12 · 14 a 17</span></div><div style="text-align:right"><b>DÓNDE</b><span>Calle 38 4335</span></div></div></div>
</section>''', 'Publicar 8:00. Sticker sugerido: enlace a WhatsApp (https://wa.me/5491131826166) con el texto “Pedí por WhatsApp”.'))

PIEZAS.append(('historia_2_1200_mediodia', 'story', f'''<section class="story claro">
<div class="sol" style="width:900px;height:900px;right:-330px;top:240px;background:var(--gr)"></div>
<div class="rayas" style="left:0;right:0;bottom:0;height:300px;color:var(--gr)"></div>
{top(LAZ)}
<div class="bloque" style="top:560px"><div class="rot">PAUSA DE MEDIODÍA</div></div>
<div class="bloque" style="top:650px"><h1 style="font-size:150px">Volvemos<br>a las</h1>
<div class="hora" style="color:var(--az);margin-top:10px">14:00</div></div>
<div class="bloque" style="top:1270px"><p class="txt">Cerramos de 12 a 14. Dejanos tu consulta por WhatsApp y te respondemos a la vuelta.</p>
<div class="boton wa" style="margin-top:44px">{WA}11 3182-6166</div></div>
</section>''', 'Publicar 12:00. Sticker sugerido: enlace a WhatsApp. Opcional: encuesta “¿Qué estás arreglando esta semana?”.'))

PIEZAS.append(('historia_3_1400_volvimos', 'story', f'''<section class="story oscuro">
<div class="rayas" style="right:0;top:0;width:420px;height:760px;clip-path:polygon(32% 0,100% 0,100% 100%,0 100%)"></div>
{top(LBL)}
<div class="bloque" style="top:560px"><div class="rot">TURNO TARDE</div></div>
<div class="bloque" style="top:670px"><div class="hora" style="font-size:280px">14:00<small>hs</small></div></div>
<div class="bloque" style="top:1000px"><h1>Volvimos.<br>Estamos hasta<br>las 17.</h1>
<p class="txt" style="margin-top:36px">¿No llegás? Armá el pedido en la web y lo cerramos por WhatsApp.</p></div>
<div class="bloque" style="top:1560px"><div class="boton bl">{WEB}masherrferreteria.com.ar</div></div>
</section>''', 'Publicar 14:00. Sticker sugerido: enlace a https://masherrferreteria.com.ar con el texto “Comprá online”.'))

PIEZAS.append(('historia_4_1700_cerramos', 'story', f'''<section class="story azul">
<div class="rayas" style="left:0;right:0;bottom:0;height:420px"></div>
{top(LBL)}
<div class="bloque" style="top:560px"><div class="rot">HASTA MAÑANA</div></div>
<div class="bloque" style="top:650px"><h1 style="font-size:150px">Cerramos<br>por hoy.</h1></div>
<div class="bloque" style="top:1020px"><div class="linea"></div>
<div class="datos" style="margin-top:34px"><div><b>MAÑANA</b><span>Abrimos 8:00</span></div><div style="text-align:right"><b>LA WEB</b><span>Abierta 24 h</span></div></div>
<p class="txt" style="margin-top:60px">Gracias por elegirnos hoy. Si te atendimos bien, dejanos tu opinión en Google ⭐</p></div>
<div class="zona-sticker" style="top:1500px">STICKER DE ENLACE A RESEÑAS</div>
</section>''', 'Publicar 17:00. Sticker de enlace a https://g.page/r/CSTh9aafPrTYEBE/review (texto: “Dejanos tu reseña”) tapando el recuadro.'))

PIEZAS.append(('historia_5_promo_carrusel', 'story', f'''<section class="story gris">
{top(LAZ)}
<div class="bloque" style="top:520px"><div class="rot">NUEVO POST</div><h1 style="margin-top:30px;font-size:124px">¿Qué disco<br>va con cada<br>trabajo?</h1></div>
<div class="tarjeta" style="left:96px;right:96px;top:1030px;height:520px"><img src="{foto('disco-flap-115-mm-grano-40-y115ap40-10-pegaso-5eso2-0')}" alt=""></div>
<div class="zona-sticker" style="top:1600px">COMPARTÍ ACÁ EL CARRUSEL</div>
</section>''', 'Publicar después del carrusel: tocá el avión de papel del carrusel → “Agregar a tu historia” y ubicalo sobre el recuadro punteado.'))

# ------------------------------------------------------------------ CARRUSEL (6 placas)
def car(i, total, clase, cuerpo, flecha=True):
    logo = LAZ if clase in ('claro', 'gris') else LBL
    return f'''<section class="post {clase}"><div class="cab"><img src="{logo}" alt="Masherr"><span>GUÍA DE DISCOS</span></div>{cuerpo}
{'<div class="flecha">DESLIZÁ<i></i></div>' if flecha else ''}<div class="pag">{i:02d} / {total:02d}</div></section>'''

PASOS = [
 ('01', 'Cortar metal', 'Disco de corte para acero', 'Fino (1 mm): corta rápido y con menos rebaba en perfiles, caños y chapa.', 'pack-x-5-discos-de-corte-de-acero-115-x-10-x-2223-a-60-t-bfbosch-s5sei-0', 'CORTE'),
 ('02', 'Desbastar y limpiar soldadura', 'Disco flap grano 40 o 60', 'Saca material sin “morder” la pieza. Ideal para cordones y óxido.', 'disco-flap-115-mm-grano-40-y115ap40-10-pegaso-5eso2-0', 'DESBASTE'),
 ('03', 'Dejar la terminación lisa', 'Disco flap grano 80 o 120', 'Después del desbaste: emparejá y dejá la superficie lista para pintar.', 'disco-flap-115-mm-grano-80-y115ap80-10pegaso-1klz1-0', 'TERMINACIÓN'),
 ('04', 'Perforar cerámica', 'Copa diamantada en seco', 'Agujeros limpios para caños y griferías, directo en la amoladora.', 'copa-diamantada-35mm-para-amoladora-uso-en-seco-cda-35aliafor-1aqnl-0', 'PERFORACIÓN'),
]
T = 2 + len(PASOS)
slides = [car(1, T, 'oscuro', f'''<div class="rayas" style="right:0;top:170px;width:360px;height:560px;clip-path:polygon(32% 0,100% 0,100% 100%,0 100%)"></div>
<div style="position:absolute;left:84px;right:84px;top:330px"><div class="rot">CONSEJO DE FERRETERO</div>
<h1 style="font-size:132px;margin-top:34px">¿Qué disco<br>va con cada<br>trabajo?</h1>
<p class="txt" style="margin-top:44px;font-size:40px">Usar el disco equivocado gasta más, corta peor y es peligroso. Guardá esta guía.</p></div>''')]
for k, (n, titulo, disco, txt, img, tag) in enumerate(PASOS, 2):
    clase = 'gris' if k % 2 == 0 else 'claro'
    slides.append(car(k, T, clase, f'''
<div style="position:absolute;left:84px;right:84px;top:170px;display:flex;align-items:flex-end;gap:34px"><div class="num">{n}</div>
<div style="padding-bottom:14px"><span class="tag">{tag}</span><h1 style="font-size:70px;margin-top:16px">{titulo}</h1></div></div>
<div class="tarjeta" style="top:450px;height:520px{';background:var(--gr)' if clase == 'claro' else ''}"><img src="{foto(img)}" alt=""></div>
<div style="position:absolute;left:84px;right:84px;top:1010px"><div style="font-family:C;font-size:46px;color:var(--az)">{disco}</div>
<p class="txt" style="font-size:34px;margin-top:12px">{txt}</p></div>'''))
slides.append(car(T, T, 'azul', f'''<div class="rayas" style="left:0;right:0;bottom:0;height:300px"></div>
<div style="position:absolute;left:84px;right:84px;top:300px"><div class="rot">¿NO SABÉS CUÁL?</div>
<h1 style="font-size:116px;margin-top:34px">Contanos qué<br>vas a hacer.<br>Te decimos cuál.</h1>
<div style="display:flex;flex-direction:column;gap:22px;margin-top:60px;align-items:flex-start">
<div class="boton wa">{WA}WhatsApp 11 3182-6166</div><div class="boton bl">{WEB}masherrferreteria.com.ar</div></div></div>''', flecha=False))
for k, s in enumerate(slides, 1):
    PIEZAS.append((f'carrusel_{k:02d}', 'post', s, None))

COPY_CARRUSEL = '''¿Qué disco va con cada trabajo? 🔧

Usar el disco equivocado gasta más, corta peor y es peligroso. Te dejamos la guía rápida:

1️⃣ Cortar metal → disco de corte fino para acero
2️⃣ Desbastar y limpiar soldadura → flap grano 40 o 60
3️⃣ Terminación lisa → flap grano 80 o 120
4️⃣ Perforar cerámica y porcelanato → copa diamantada

¿No sabés cuál te sirve? Contanos qué vas a hacer y te asesoramos.
📲 WhatsApp 11 3182-6166
🛒 Mirá todos los discos en masherrferreteria.com.ar (link en la bio)
📍 Calle 38 4335, Villa Lynch

Guardá este post para tenerlo a mano 🔖

#ferreteria #ferreteriaindustrial #sanmartin #villalynch #amoladora #discosdecorte #herrería #consejosdeferretero #masherr'''

# ------------------------------------------------------------------ POST: web nueva
PIEZAS.append(('post_web_nueva', 'post', f'''<section class="post oscuro">
<div class="rayas" style="right:0;top:0;width:520px;height:1350px;clip-path:polygon(40% 0,100% 0,100% 100%,0 100%)"></div>
<div class="cab"><img src="{LBL}" alt="Masherr"><span>NOVEDAD</span></div>
<div style="position:absolute;left:84px;top:300px;width:470px"><div class="rot">WEB NUEVA</div>
<h1 style="font-size:84px;margin-top:30px">Toda la<br>ferretería<br>en tu<br>celular.</h1>
<p class="txt" style="font-size:32px;margin-top:36px;width:440px">Buscá, armá tu carrito y cerrá el pedido por WhatsApp.</p>
<div style="font-family:C;font-size:30px;color:var(--ce);margin-top:44px">masherrferreteria.com.ar</div></div>
<div class="tel" style="right:70px;top:190px;width:440px;height:900px"><img src="assets/web_inicio.png" alt="Web de Masherr"></div>
</section>''', None))
COPY_WEB = '''¡Estrenamos web! 🚀

Ahora tenés toda la ferretería en el celular:
🔎 Buscá por producto o marca
🛒 Armá tu carrito con lo que necesitás
💬 Envialo por WhatsApp y cerramos el pedido: te confirmamos stock y retiro

Herramientas eléctricas, discos, soldadura, medición y mucho más.

👉 masherrferreteria.com.ar (link en la bio)
📍 Y como siempre, te esperamos en Calle 38 4335, Villa Lynch.

#ferreteria #ferreteriaindustrial #sanmartin #villalynch #herramientas #comprasonline #masherr'''

# ------------------------------------------------------------------ salida
for nombre, tipo, html, _ in PIEZAS:
    (AQUI / f'{nombre}.html').write_text(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{html}</body></html>')
(AQUI / 'piezas.txt').write_text('\n'.join(f'{n}|{t}' for n, t, _, _ in PIEZAS))
PLAN = f'''PLANIFICACIÓN INSTAGRAM · MASHERR · {DIA} {FECHA.replace(" · ", "/")}/2026
================================================================

HISTORIAS
08:00  historia_1_0800_abrimos      → sticker enlace WhatsApp
12:00  historia_2_1200_mediodia     → sticker enlace WhatsApp (+ encuesta opcional)
13:00  CARRUSEL “¿Qué disco va con cada trabajo?” (6 placas) → ver copy abajo
13:05  historia_5_promo_carrusel    → compartir el carrusel encima del recuadro
14:00  historia_3_1400_volvimos     → sticker enlace web
17:00  historia_4_1700_cerramos     → sticker enlace reseñas

POST (19:00, horario de más uso)
19:00  post_web_nueva                → ver copy abajo. Después: fijarlo arriba del perfil.

ANTES DE PUBLICAR
- Cambiar el link de la bio: hoy apunta a masherrferreteria.mitiendanube.com → poner https://masherrferreteria.com.ar
- Responder en el día cada comentario y mensaje (como Guido).
- Las historias de horario se reutilizan todos los días: solo cambia la fecha.

{'-' * 64}
COPY · CARRUSEL (13:00)
{'-' * 64}
{COPY_CARRUSEL}

{'-' * 64}
COPY · POST WEB NUEVA (19:00)
{'-' * 64}
{COPY_WEB}

{'-' * 64}
STICKERS DE LAS HISTORIAS
{'-' * 64}
''' + '\n'.join(f'{n}: {t}' for n, tp, _, t in PIEZAS if tp == 'story')
(AQUI / 'PLANIFICACION.txt').write_text(PLAN)
print(len(PIEZAS), 'piezas')
