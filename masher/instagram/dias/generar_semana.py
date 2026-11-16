"""Genera el contenido de Instagram de miércoles 18 a sábado 21/11/2026 con el mismo sistema visual del 17/11.
Uso: python3 generar_semana.py  → crea dias/2026-11-18 … 2026-11-21 (html + piezas.txt + PLANIFICACION.txt)
Después: node exportar.js <carpeta>  para cada día.
"""
import re
from pathlib import Path

DIAS = Path(__file__).parent
BASE = (DIAS / '2026-11-17' / 'generar.py').read_text()
# Reutiliza estilos e íconos del 17/11 (CSS, WA, WEB, foto, rutas)
CSS_EXTRA = '.tarjeta img{max-height:430px !important;max-width:80%;object-fit:contain}'
exec(BASE.split('PIEZAS = []')[0].split("DIA, FECHA = 'MARTES', '17 · 11'")[0] + BASE.split("DIA, FECHA = 'MARTES', '17 · 11'")[1].split('def top(logo):')[0])
HASH = '#ferreteria #ferreteriaindustrial #sanmartin #villalynch #herramientas #masherr'

def top(logo, dia, fecha):
    return f'<div class="top"><img src="{logo}" alt="Masherr"><div class="dia">{dia}<br>{fecha}</div></div>'

def historias_dia(dia, fecha, sabado=False, manana='Mañana abrimos 8:00'):
    h = []
    h.append(('historia_1_0800_abrimos', 'story', f'''<section class="story azul">
<div class="rayas" style="right:0;top:0;width:420px;height:760px;clip-path:polygon(32% 0,100% 0,100% 100%,0 100%)"></div>
{top(LBL, dia, fecha)}
<div class="bloque" style="top:560px"><div class="rot">BUEN DÍA · ABRIMOS</div></div>
<div class="bloque" style="top:650px"><div class="hora">8:00<small>hs</small></div></div>
<div class="bloque" style="top:1000px"><h1>{'Sábado de<br>arreglos.' if sabado else 'La persiana<br>ya está arriba.'}</h1>
<p class="txt" style="margin-top:36px">{'Hoy abrimos hasta las 12:30. Pasá temprano o mandanos tu lista por WhatsApp.' if sabado else 'Pasá por el mostrador o mandanos tu lista por WhatsApp y te la dejamos lista para retirar.'}</p></div>
<div class="bloque" style="top:1520px"><div class="linea"></div>
<div class="datos" style="margin-top:34px"><div><b>HOY</b><span>{'8 a 12:30' if sabado else '8 a 12 · 14 a 17'}</span></div><div style="text-align:right"><b>DÓNDE</b><span>Calle 38 4335</span></div></div></div>
</section>''', 'Publicar 8:00. Sticker: enlace a WhatsApp (https://wa.me/5491131826166) “Pedí por WhatsApp”.'))
    if not sabado:
        h.append(('historia_2_1200_mediodia', 'story', f'''<section class="story claro">
<div class="sol" style="width:900px;height:900px;right:-330px;top:240px;background:var(--gr)"></div>
<div class="rayas" style="left:0;right:0;bottom:0;height:300px;color:var(--gr)"></div>
{top(LAZ, dia, fecha)}
<div class="bloque" style="top:560px"><div class="rot">PAUSA DE MEDIODÍA</div></div>
<div class="bloque" style="top:650px"><h1 style="font-size:150px">Volvemos<br>a las</h1><div class="hora" style="color:var(--az);margin-top:10px">14:00</div></div>
<div class="bloque" style="top:1270px"><p class="txt">Cerramos de 12 a 14. Dejanos tu consulta por WhatsApp y te respondemos a la vuelta.</p>
<div class="boton wa" style="margin-top:44px">{WA}11 3182-6166</div></div>
</section>''', 'Publicar 12:00. Sticker: enlace a WhatsApp.'))
        h.append(('historia_3_1400_volvimos', 'story', f'''<section class="story oscuro">
<div class="rayas" style="right:0;top:0;width:420px;height:760px;clip-path:polygon(32% 0,100% 0,100% 100%,0 100%)"></div>
{top(LBL, dia, fecha)}
<div class="bloque" style="top:560px"><div class="rot">TURNO TARDE</div></div>
<div class="bloque" style="top:670px"><div class="hora" style="font-size:280px">14:00<small>hs</small></div></div>
<div class="bloque" style="top:1000px"><h1>Volvimos.<br>Estamos hasta<br>las 17.</h1>
<p class="txt" style="margin-top:36px">¿No llegás? Armá el pedido en la web y lo cerramos por WhatsApp.</p></div>
<div class="bloque" style="top:1560px"><div class="boton bl">{WEB}masherrferreteria.com.ar</div></div>
</section>''', 'Publicar 14:00. Sticker: enlace a https://masherrferreteria.com.ar “Comprá online”.'))
    h.append(('historia_4_cierre', 'story', f'''<section class="story azul">
<div class="rayas" style="left:0;right:0;bottom:0;height:420px"></div>
{top(LBL, dia, fecha)}
<div class="bloque" style="top:560px"><div class="rot">{'BUEN FINDE' if sabado else 'HASTA MAÑANA'}</div></div>
<div class="bloque" style="top:650px"><h1 style="font-size:150px">Cerramos<br>por hoy.</h1></div>
<div class="bloque" style="top:1020px"><div class="linea"></div>
<div class="datos" style="margin-top:34px"><div><b>{'EL LUNES' if sabado else 'MAÑANA'}</b><span>Abrimos 8:00</span></div><div style="text-align:right"><b>LA WEB</b><span>Abierta 24 h</span></div></div>
<p class="txt" style="margin-top:60px">Gracias por elegirnos{' esta semana' if sabado else ' hoy'}. Si te atendimos bien, dejanos tu opinión en Google ⭐</p></div>
<div class="zona-sticker" style="top:1500px">STICKER DE ENLACE A RESEÑAS</div>
</section>''', f'Publicar {"12:30" if sabado else "17:00"}. Sticker: enlace a https://g.page/r/CSTh9aafPrTYEBE/review “Dejanos tu reseña”.'))
    return h

def historia_promo(dia, fecha, titulo, img, que='NUEVO POST'):
    return ('historia_5_promo_post', 'story', f'''<section class="story gris">
{top(LAZ, dia, fecha)}
<div class="bloque" style="top:520px"><div class="rot">{que}</div><h1 style="margin-top:30px;font-size:124px">{titulo}</h1></div>
<div class="tarjeta" style="left:96px;right:96px;top:1030px;height:520px"><img src="{foto(img)}" alt=""></div>
<div class="zona-sticker" style="top:1600px">COMPARTÍ ACÁ LA PUBLICACIÓN</div>
</section>''', 'Publicar 5 minutos después del post: avión de papel → “Agregar a tu historia”, sobre el recuadro punteado.')

def cab(clase, rot):
    logo = LAZ if clase in ('claro', 'gris') else LBL
    return f'<div class="cab"><img src="{logo}" alt="Masherr"><span>{rot}</span></div>'

def slide(i, total, clase, rot, cuerpo, flecha=True):
    return f'''<section class="post {clase}">{cab(clase, rot)}{cuerpo}
{'<div class="flecha">DESLIZÁ<i></i></div>' if flecha else ''}<div class="pag">{i:02d} / {total:02d}</div></section>'''

CIERRE_BTNS = f'''<div style="display:flex;flex-direction:column;gap:22px;margin-top:60px;align-items:flex-start">
<div class="boton wa">{WA}WhatsApp 11 3182-6166</div><div class="boton bl">{WEB}masherrferreteria.com.ar</div></div>'''

# ------------------------------------------------------------------ MIÉRCOLES 18 · Post producto (sin precio)
def miercoles():
    img = 'kit-taladro-percutor-atornillador-y-amoladora-brushless-emtop-emteckl202564-317mg-0'
    post = ('post_producto_kit_emtop', 'post', f'''<section class="post claro">{cab('claro', 'PRODUCTO DE LA SEMANA')}
<div class="tarjeta" style="top:170px;height:640px;background:var(--gr)"><img src="{foto(img)}" alt=""></div>
<div style="position:absolute;left:84px;right:84px;top:845px"><span class="tag">EMTOP · 20 V BRUSHLESS</span>
<h1 style="font-size:76px;margin-top:20px">Taladro percutor<br>+ amoladora</h1>
<p class="txt" style="font-size:32px;margin-top:14px">2 baterías, cargador, discos, accesorios y maletín.</p></div>
<div style="position:absolute;left:84px;right:84px;bottom:60px;display:flex;justify-content:space-between;align-items:center;border-top:3px solid var(--az);padding-top:26px">
<span style="font-family:C;font-size:30px;color:var(--az)">Consultá precio y stock</span><div class="boton az" style="font-size:30px;padding:20px 30px">{WA}WhatsApp</div></div>
</section>''', None)
    copy = f'''Producto de la semana 🔋

Kit Emtop 20 V brushless: taladro percutor de 66 Nm + amoladora angular de 115 mm, sin cables.

✔️ 2 baterías de 4 Ah y cargador
✔️ 10 discos de corte para metal
✔️ 47 accesorios
✔️ Maletín para llevar todo ordenado

Ideal para construcción, herrería y mantenimiento: dos herramientas, una sola batería para las dos.

💬 Consultá precio y stock por WhatsApp 11 3182-6166
🛒 O miralo en masherrferreteria.com.ar (link en la bio)
📍 Calle 38 4335, Villa Lynch

{HASH} #emtop #inalambrico #taladro'''
    return [post, historia_promo('MIÉRCOLES', '18 · 11', 'Producto de<br>la semana.', img)], {'post_producto_kit_emtop': copy}, '19:00'

# ------------------------------------------------------------------ JUEVES 19 · Carrusel medición
def jueves():
    pasos = [('01', 'Medidas cortas y obra', 'Cinta métrica', 'Para el día a día. Elegí el largo según el trabajo: 3, 5, 8 o 10 metros.', 'cinta-metrica-5mts-30-797-stanley-fleje-19mm-1m28x-0', 'MEDIR'),
             ('02', 'Que quede derecho', 'Nivel de burbuja', 'Estantes, cuadros, aberturas y cerámicos. De 40 cm a 1,20 m.', 'nivel-de-aluminio-profesional-400mm-7164bremen-1tza3-0', 'NIVELAR'),
             ('03', 'Distancias largas, sin ayuda', 'Medidor láser', 'Mide ambientes y galpones en un segundo, sin que nadie sostenga la cinta.', 'medidor-de-distancia-laser-40mt-emdl1504emtop-1vfyx-0', 'LÁSER'),
             ('04', 'Líneas en toda la pared', 'Nivel láser', 'Marca una línea recta en paredes enteras: ideal para cerámicos y durlock.', 'nivel-laser-10mt-nv10l-8lusqtoff-uu56z-0', 'TRAZAR')]
    T = 2 + len(pasos); R = 'CÓMO MEDIR BIEN'
    s = [slide(1, T, 'oscuro', R, f'''<div class="rayas" style="right:0;top:170px;width:360px;height:560px;clip-path:polygon(32% 0,100% 0,100% 100%,0 100%)"></div>
<div style="position:absolute;left:84px;right:84px;top:330px"><div class="rot">CONSEJO DE FERRETERO</div>
<h1 style="font-size:118px;margin-top:34px">Medí una vez.<br>Cortá una<br>sola vez.</h1>
<p class="txt" style="margin-top:44px;font-size:40px">La herramienta de medición correcta para cada trabajo. Guardá esta guía.</p></div>''')]
    for k, (n, titulo, prod, txt, img, tag) in enumerate(pasos, 2):
        clase = 'gris' if k % 2 == 0 else 'claro'
        s.append(slide(k, T, clase, R, f'''
<div style="position:absolute;left:84px;right:84px;top:170px;display:flex;align-items:flex-end;gap:34px"><div class="num">{n}</div>
<div style="padding-bottom:14px"><span class="tag">{tag}</span><h1 style="font-size:66px;margin-top:16px">{titulo}</h1></div></div>
<div class="tarjeta" style="top:450px;height:520px{';background:var(--gr)' if clase == 'claro' else ''}"><img src="{foto(img)}" alt=""></div>
<div style="position:absolute;left:84px;right:84px;top:1010px"><div style="font-family:C;font-size:46px;color:var(--az)">{prod}</div>
<p class="txt" style="font-size:34px;margin-top:12px">{txt}</p></div>'''))
    s.append(slide(T, T, 'azul', R, f'''<div class="rayas" style="left:0;right:0;bottom:0;height:300px"></div>
<div style="position:absolute;left:84px;right:84px;top:300px"><div class="rot">¿CUÁL NECESITÁS?</div>
<h1 style="font-size:116px;margin-top:34px">Contanos qué<br>vas a medir.<br>Te asesoramos.</h1>{CIERRE_BTNS}</div>''', flecha=False))
    piezas = [(f'carrusel_{k:02d}', 'post', x, None) for k, x in enumerate(s, 1)]
    copy = f'''Medí una vez, cortá una sola vez 📏

La herramienta de medición correcta para cada trabajo:

1️⃣ Medidas cortas y obra → cinta métrica (3, 5, 8 o 10 m)
2️⃣ Que quede derecho → nivel de burbuja (40 cm a 1,20 m)
3️⃣ Distancias largas sin ayuda → medidor láser
4️⃣ Líneas en toda la pared → nivel láser

¿Cuál necesitás? Contanos qué vas a medir y te asesoramos.
📲 WhatsApp 11 3182-6166
🛒 Toda la línea de medición en masherrferreteria.com.ar
📍 Calle 38 4335, Villa Lynch

Guardá este post 🔖

{HASH} #medicion #nivel #cintametrica #obra'''
    piezas.append(historia_promo('JUEVES', '19 · 11', 'Medí una vez,<br>cortá una<br>sola vez.', 'medidor-de-distancia-laser-40mt-emdl1504emtop-1vfyx-0'))
    return piezas, {'carrusel_01': copy}, '13:00'

# ------------------------------------------------------------------ VIERNES 20 · Post reseña real
def viernes():
    post = ('post_resena', 'post', f'''<section class="post oscuro">
<div class="rayas" style="right:0;bottom:0;width:420px;height:330px;clip-path:polygon(32% 0,100% 0,100% 100%,0 100%)"></div>
{cab('oscuro', 'LO QUE DICEN DE NOSOTROS')}
<div style="position:absolute;left:84px;right:84px;top:250px">
<div style="display:flex;gap:16px">{''.join('<svg viewBox="0 0 24 24" style="width:70px;height:70px;fill:var(--ce)"><path d="M12 2.5l2.9 6.1 6.6.8-4.9 4.6 1.3 6.6L12 17.3 6.1 20.6l1.3-6.6L2.5 9.4l6.6-.8z"/></svg>' for _ in range(5))}</div>
<h1 style="font-size:96px;margin-top:50px">“Se tomaron el tiempo para buscar la que yo necesitaba.”</h1>
<div style="font-size:36px;color:var(--ce);margin-top:36px">Lorena · reseña en Google</div></div>
<div style="position:absolute;left:84px;right:84px;bottom:150px;border-top:2px solid #2A2E3A;padding-top:40px;display:flex;align-items:center;gap:30px">
<div style="font-family:C;font-size:140px;line-height:1">4,7</div><div style="font-size:34px;color:#C6CAD6;line-height:1.35">★ en Google<br>131 opiniones</div></div>
<div class="pag" style="left:84px;right:auto">GRACIAS POR ELEGIRNOS</div>
</section>''', None)
    copy = f'''Esto es lo que más nos importa ⭐

“Se tomaron el tiempo para buscar la que yo necesitaba.” — Lorena

En Masherr no te vendemos cualquier herramienta: te escuchamos, te preguntamos qué vas a hacer y te ayudamos a elegir la correcta.

Gracias a los 131 clientes que nos dejaron su opinión: somos 4,7 ★ en Google 🙌

¿Ya nos conocés? Dejanos tu reseña (link en nuestras historias destacadas) o vení a vernos a Calle 38 4335, Villa Lynch.

{HASH} #clientes #atencion #reseñas'''
    promo = ('historia_5_promo_post', 'story', f'''<section class="story oscuro">
<div class="rayas" style="right:0;top:0;width:420px;height:760px;clip-path:polygon(32% 0,100% 0,100% 100%,0 100%)"></div>
{top(LBL, 'VIERNES', '20 · 11')}
<div class="bloque" style="top:560px"><div class="rot">GRACIAS</div><div class="hora" style="margin-top:40px">4,7<small>★</small></div>
<h1 style="margin-top:30px">131 opiniones<br>en Google.</h1></div>
<div class="zona-sticker" style="top:1500px">COMPARTÍ ACÁ LA PUBLICACIÓN</div></section>''', 'Publicar 5 minutos después del post: avión de papel → “Agregar a tu historia”.')
    return [post, promo], {'post_resena': copy}, '19:00'

# ------------------------------------------------------------------ SÁBADO 21 · Post cómo comprar
def sabado():
    post = ('post_como_comprar', 'post', f'''<section class="post claro">{cab('claro', 'COMPRÁ ONLINE')}
<div style="position:absolute;left:84px;right:84px;top:230px"><div class="rot">EN 3 PASOS</div>
<h1 style="font-size:110px;margin-top:30px">Armá el pedido.<br>Lo cerramos<br>por WhatsApp.</h1></div>
<div style="position:absolute;left:84px;right:84px;top:760px">
{''.join(f'<div style="display:flex;gap:30px;align-items:center;padding:28px 0;border-bottom:2px solid var(--li)"><div style="width:84px;height:84px;border-radius:50%;background:var(--az);color:#fff;display:grid;place-items:center;font-family:C;font-size:44px;flex:none">{n}</div><div style="font-size:40px">{t}</div></div>' for n, t in [(1, 'Entrá a <b>masherrferreteria.com.ar</b>'), (2, 'Agregá lo que necesitás al carrito'), (3, 'Envialo por WhatsApp y confirmamos')])}</div>
<div class="pag" style="left:84px;right:auto">LINK EN LA BIO</div>
</section>''', None)
    copy = f'''¿Sabías que podés armar tu pedido desde el celular? 📱

1️⃣ Entrá a masherrferreteria.com.ar
2️⃣ Agregá lo que necesitás al carrito
3️⃣ Envialo por WhatsApp: te confirmamos precio, stock y retiro

Así llegás al local y está todo listo. Y si es para tu empresa o taller, también te cotizamos desde la web.

👉 Link en la bio
📍 Hoy abrimos hasta las 12:30 · Calle 38 4335, Villa Lynch

{HASH} #comprasonline #whatsapp'''
    return [post], {'post_como_comprar': copy}, '10:00'

PLAN_DIAS = [('2026-11-18', 'MIÉRCOLES', '18 · 11', miercoles, False),
             ('2026-11-19', 'JUEVES', '19 · 11', jueves, False),
             ('2026-11-20', 'VIERNES', '20 · 11', viernes, False),
             ('2026-11-21', 'SÁBADO', '21 · 11', sabado, True)]

CSS = CSS + CSS_EXTRA
for carpeta, dia, fecha, fn, sab in PLAN_DIAS:
    d = DIAS / carpeta; d.mkdir(exist_ok=True)
    piezas, copys, hora_feed = fn()
    todas = historias_dia(dia, fecha, sab) + piezas
    for nombre, tipo, html, _ in todas:
        (d / f'{nombre}.html').write_text(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{html}</body></html>')
    (d / 'piezas.txt').write_text('\n'.join(f'{n}|{t}' for n, t, _, _ in todas))
    horas = ['08:00  historia_1_0800_abrimos'] + ([] if sab else ['12:00  historia_2_1200_mediodia', '14:00  historia_3_1400_volvimos']) + [f'{"12:30" if sab else "17:00"}  historia_4_cierre']
    feed = [n for n, t, _, _ in piezas if t == 'post']
    plan = f'''PLANIFICACIÓN INSTAGRAM · MASHERR · {dia} {fecha.replace(' · ', '/')}/2026
================================================================

HISTORIAS
''' + '\n'.join(horas) + f'''

FEED ({hora_feed})
{hora_feed}  {feed[0] if len(feed) == 1 else f"CARRUSEL de {len(feed)} placas: " + ", ".join(feed)}
''' + ('' if sab else f'{hora_feed[:3]}05  historia_5_promo_post (compartir la publicación)\n') + f'''
{'-' * 64}
COPY
{'-' * 64}
{list(copys.values())[0]}

{'-' * 64}
STICKERS DE LAS HISTORIAS
{'-' * 64}
''' + '\n'.join(f'{n}: {t}' for n, tp, _, t in todas if tp == 'story')
    (d / 'PLANIFICACION.txt').write_text(plan)
    print(carpeta, len(todas), 'piezas')
