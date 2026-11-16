"""Masherr · Instagram v2 (dirección de arte dinámica) · semana 17–21/11/2026.

Sistema visual:
  - "Ráfaga": líneas de velocidad horizontales con borde inclinado, tomadas de las franjas del símbolo.
  - Tipografía gigante calada (solo contorno) detrás de la información.
  - Productos recortados, girados, con sombra, que rompen el encuadre.
  - Marcas de corte en las esquinas y rótulos técnicos (lenguaje industrial).
  - Paleta del manual: azul #17256B, negro #08090B, blanco, gris #EEF0F4, celeste #9AAEFF (solo sobre oscuro).
Historias con animación de entrada (se exportan en MP4 y PNG); posteos y carruseles en PNG y PDF.

Uso: python3 generar_v2.py && node exportar_v2.js
"""
import json
from pathlib import Path

AQUI = Path(__file__).parent
F = '../../../catalogo/fonts/'
LAZ = '../../../catalogo/img/masher-logo-azul.png'
LBL = '../../../catalogo/img/masher-logo-blanco.png'
REC = '../recortes/'
SHOT = '../../dias/2026-11-17/assets/web_inicio.png'
r = lambda n: f'{REC}{n}.png'
P = {
 'corte': 'pack-x-5-discos-de-corte-de-acero-115-x-10-x-2223-a-60-t-bfbosch-s5sei-0',
 'flap40': 'disco-flap-115-mm-grano-40-y115ap40-10-pegaso-5eso2-0',
 'flap80': 'disco-flap-115-mm-grano-80-y115ap80-10pegaso-1klz1-0',
 'copa': 'copa-diamantada-35mm-para-amoladora-uso-en-seco-cda-35aliafor-1aqnl-0',
 'kit': 'kit-taladro-percutor-atornillador-y-amoladora-brushless-emtop-emteckl202564-317mg-0',
 'cinta': 'cinta-metrica-5mts-30-797-stanley-fleje-19mm-1m28x-0',
 'nivel': 'nivel-de-aluminio-profesional-400mm-7164bremen-1tza3-0',
 'medidor': 'medidor-de-distancia-laser-40mt-emdl1504emtop-1vfyx-0',
 'laser': 'nivel-laser-10mt-nv10l-8lusqtoff-uu56z-0',
 'amoladora': 'amoladora-angular-115mm-650w-11565-vanden-z9jit-0',
}

CSS = f'''
@font-face{{font-family:C;src:url({F}DejaVuSansCondensed-Bold.ttf);font-weight:700}}
@font-face{{font-family:T;src:url({F}DejaVuSans.ttf)}}
@font-face{{font-family:T;src:url({F}DejaVuSans-Bold.ttf);font-weight:700}}
:root{{--az:#17256B;--az2:#1F3192;--ne:#08090B;--ce:#9AAEFF;--gr:#EEF0F4;--gr2:#DFE3EC;--tx:#50566A;--wa:#128C3E}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{background:#444}}
body{{font-family:T,sans-serif;-webkit-font-smoothing:antialiased}}
section{{position:relative;overflow:hidden}}
.story{{width:1080px;height:1920px}} .post{{width:1080px;height:1350px}}
.az{{background:var(--az);color:#fff}} .ne{{background:var(--ne);color:#fff}} .bl{{background:#fff;color:var(--ne)}} .gr{{background:var(--gr);color:var(--ne)}}
.abs{{position:absolute}}
/* ráfaga */
.rafaga{{position:absolute;display:flex;flex-direction:column;justify-content:space-between}}
.rafaga i{{display:block;height:var(--g);background:currentColor;transform-origin:var(--o,right) center;animation:raya .9s cubic-bezier(.2,.8,.2,1) both}}
@keyframes raya{{from{{transform:scaleX(0)}}to{{transform:scaleX(1)}}}}
/* tipografía */
.C{{font-family:C;font-weight:700;letter-spacing:-.005em}}
.calado{{font-family:C;color:transparent;-webkit-text-stroke:3px currentColor;line-height:.8;letter-spacing:-.04em;white-space:nowrap}}
.rot{{font-family:C;font-size:28px;letter-spacing:.22em;text-transform:uppercase;display:flex;align-items:center;gap:18px}}
.rot::before{{content:"";width:56px;height:6px;background:currentColor}}
.lin{{display:block;overflow:hidden}} .lin>span{{display:block;animation:sube .8s cubic-bezier(.2,.8,.2,1) both}}
@keyframes sube{{from{{transform:translateY(105%)}}to{{transform:none}}}}
.fade{{animation:aparece .7s ease both}} @keyframes aparece{{from{{opacity:0;transform:translateY(24px)}}to{{opacity:1;transform:none}}}}
.entra-der{{animation:entraDer 1s cubic-bezier(.2,.8,.2,1) both}} @keyframes entraDer{{from{{opacity:0;transform:translateX(160px) rotate(var(--rot,0deg))}}to{{opacity:1;transform:rotate(var(--rot,0deg))}}}}
.pop{{animation:pop .7s cubic-bezier(.3,1.5,.5,1) both}} @keyframes pop{{from{{opacity:0;transform:scale(.6)}}to{{opacity:1;transform:none}}}}
.prod{{position:absolute;transform:rotate(var(--rot,0deg));filter:drop-shadow(0 46px 44px rgba(0,0,0,.38))}}
/* marcas */
.marca{{position:absolute;width:44px;height:44px;border-color:currentColor;border-style:solid;opacity:.55}}
.m1{{left:56px;top:56px;border-width:4px 0 0 4px}} .m2{{right:56px;top:56px;border-width:4px 4px 0 0}}
.m3{{left:56px;bottom:56px;border-width:0 0 4px 4px}} .m4{{right:56px;bottom:56px;border-width:0 4px 4px 0}}
.meta{{position:absolute;left:96px;right:96px;display:flex;justify-content:space-between;align-items:center;font-family:C;font-size:26px;letter-spacing:.2em}}
.meta img{{height:70px}}
.chip{{display:inline-flex;align-items:center;gap:16px;font-family:C;font-size:34px;letter-spacing:.04em;padding:22px 34px;border-radius:999px;white-space:nowrap}}
.chip svg{{width:42px;height:42px;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}}
.chip.wa{{background:var(--wa);color:#fff}} .chip.blanco{{background:#fff;color:var(--az)}} .chip.azul{{background:var(--az);color:#fff}}
.chip.linea{{border:3px solid currentColor}}
.sticker{{position:absolute;border:3px dashed currentColor;opacity:.4;display:grid;place-items:center;font-family:C;font-size:24px;letter-spacing:.2em;border-radius:24px}}
.pie{{position:absolute;left:96px;right:96px;bottom:110px;display:flex;justify-content:space-between;align-items:center;font-family:C;font-size:26px;letter-spacing:.18em;padding-top:30px;border-top:3px solid currentColor}}
.pie img{{height:64px}}
.post .meta{{left:72px;right:72px;top:64px}} .post .meta img{{height:56px}}
.post .marca{{width:30px;height:30px}} .post .m1{{left:26px;top:26px}} .post .m2{{right:26px;top:26px}} .post .m3{{left:26px;bottom:26px}} .post .m4{{right:26px;bottom:26px}}
.pag{{position:absolute;right:72px;bottom:60px;font-family:C;font-size:26px;letter-spacing:.2em}}
.barras{{position:absolute;left:72px;right:72px;top:150px;display:flex;gap:10px}} .barras i{{flex:1;height:6px;background:currentColor;opacity:.22}} .barras i.on{{opacity:1}}
.desliza{{position:absolute;left:72px;bottom:56px;display:flex;align-items:center;gap:16px;font-family:C;font-size:26px;letter-spacing:.2em}}
.desliza b{{display:block;width:70px;height:4px;background:currentColor;position:relative}}
.desliza b::after{{content:"";position:absolute;right:-2px;top:-9px;border:11px solid transparent;border-left:16px solid currentColor;border-right:0}}
'''
WA = '<svg viewBox="0 0 24 24"><path d="M3.5 20.5l1.4-4.2A8.5 8.5 0 1 1 8 19.3z"/><path d="M9 8.6c.2 2.9 2.6 5.4 5.6 6l1.3-1.4-2-1.1-1 .7c-.9-.4-2-1.5-2.4-2.4l.7-1-1-2z"/></svg>'
WEB = '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 2.5 15.3 0 18M12 3c-2.5 2.7-2.5 15.3 0 18"/></svg>'
STAR = '<svg viewBox="0 0 24 24" style="width:{s}px;height:{s}px;fill:{c}"><path d="M12 2.5l2.9 6.1 6.6.8-4.9 4.6 1.3 6.6L12 17.3 6.1 20.6l1.3-6.6L2.5 9.4l6.6-.8z"/></svg>'

def rafaga(x, y, w, h, n=12, color='var(--az2)', delay=0.1, origen='right', largos=None, skew=0.32, extra=''):
    """Líneas de velocidad alineadas a un lado, con largos escalonados y borde inclinado."""
    largos = largos or [1, .82, .94, .7, .88, .62, .97, .76, .9, .66, .84, .72, .95, .68][:n]
    g = h / n * 0.58
    lados = 'margin-left:auto' if origen == 'right' else 'margin-right:auto'
    filas = ''.join(f'<i style="width:{l * 100:.0f}%;{lados};animation-delay:{delay + k * .045:.2f}s"></i>' for k, l in enumerate(largos))
    pol = f'polygon({skew * 100:.0f}% 0,100% 0,100% 100%,0 100%)' if origen == 'right' else f'polygon(0 0,100% 0,{100 - skew * 100:.0f}% 100%,0 100%)'
    return f'<div class="rafaga" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;color:{color};--g:{g:.0f}px;--o:{origen};clip-path:{pol};{extra}">{filas}</div>'

def lineas(*ls, d=0.25, paso=0.12):
    return ''.join(f'<span class="lin"><span style="animation-delay:{d + k * paso:.2f}s">{l}</span></span>' for k, l in enumerate(ls))

def marcas():
    return '<i class="marca m1"></i><i class="marca m2"></i><i class="marca m3"></i><i class="marca m4"></i>'

# ====================================================================== HISTORIAS
def h_abrimos(dia, fecha, sab=False):
    return f'''<section class="story az">{marcas()}
{rafaga(380, 180, 700, 760, n=13, color='rgba(255,255,255,.10)', delay=.05)}
<div class="abs calado" style="right:-60px;top:250px;font-size:620px;color:rgba(154,174,255,.35)">08</div>
<div class="meta fade" style="top:130px;animation-delay:.1s"><img src="{LBL}" alt="Masherr"><span style="color:var(--ce)">{dia} · {fecha}</span></div>
<div class="abs" style="left:96px;top:760px"><div class="rot fade" style="color:var(--ce);animation-delay:.2s">Buen día · abrimos</div></div>
<div class="abs C" style="left:90px;top:820px;font-size:330px;line-height:.9">{lineas('8:00', d=.3)}</div>
<div class="abs C" style="left:96px;top:1150px;font-size:96px;line-height:1">{lineas(*(['Sábado', 'de arreglos.'] if sab else ['La persiana', 'ya está arriba.']), d=.55)}</div>
<p class="abs fade" style="left:96px;right:200px;top:1390px;font-size:38px;line-height:1.45;color:#D9DEF0;animation-delay:.9s">{'Hoy hasta las 12:30. Mandanos tu lista por WhatsApp y la dejamos lista.' if sab else 'Mandanos tu lista por WhatsApp y te la dejamos lista para retirar.'}</p>
<div class="abs fade" style="left:96px;top:1560px;display:flex;gap:16px;animation-delay:1.05s"><span class="chip blanco">{'8 a 12:30' if sab else '8–12 · 14–17'}</span><span class="chip linea" style="color:#fff">Calle 38 4335</span></div>
<div class="pie fade" style="color:var(--ce);animation-delay:1.2s"><span>VILLA LYNCH · SAN MARTÍN</span><span>@MASHERRFERRETERIA</span></div>
</section>'''

def h_mediodia(dia, fecha):
    reloj = '''<svg viewBox="0 0 400 400" style="width:100%;height:100%">
<circle cx="200" cy="200" r="186" fill="none" stroke="#17256B" stroke-width="10"/>''' + ''.join(
        f'<line x1="200" y1="26" x2="200" y2="{56 if k % 3 == 0 else 44}" stroke="#17256B" stroke-width="{10 if k % 3 == 0 else 5}" transform="rotate({k * 30} 200 200)"/>' for k in range(12)) + '''
<line x1="200" y1="200" x2="200" y2="96" stroke="#08090B" stroke-width="14" stroke-linecap="round"/>
<g class="aguja"><line x1="200" y1="200" x2="200" y2="62" stroke="#17256B" stroke-width="10" stroke-linecap="round"/></g>
<circle cx="200" cy="200" r="16" fill="#17256B"/></svg>'''
    return f'''<section class="story gr">{marcas()}
<style>.aguja{{transform-origin:200px 200px;animation:aguja 2.2s cubic-bezier(.5,0,.2,1) .6s both}}@keyframes aguja{{from{{transform:rotate(0)}}to{{transform:rotate(60deg)}}}}</style>
{rafaga(0, 1560, 1080, 360, n=8, color='var(--gr2)', delay=.1, origen='left')}
<div class="meta fade" style="top:130px"><img src="{LAZ}" alt="Masherr"><span style="color:var(--az)">{dia} · {fecha}</span></div>
<div class="abs pop" style="right:-140px;top:330px;width:760px;height:760px;animation-delay:.2s">{reloj}</div>
<div class="abs" style="left:96px;top:420px"><div class="rot fade" style="color:var(--az);animation-delay:.25s">Pausa de mediodía</div></div>
<div class="abs C" style="left:96px;top:1100px;font-size:120px;line-height:1">{lineas('Volvemos', 'a las', d=.4)}</div>
<div class="abs C" style="left:90px;top:1330px;font-size:250px;line-height:.9;color:var(--az)">{lineas('14:00', d=.65)}</div>
<div class="abs fade" style="left:96px;top:1620px;animation-delay:1.1s"><span class="chip wa">{WA}Escribinos: 11 3182-6166</span></div>
</section>'''

def h_volvimos(dia, fecha):
    return f'''<section class="story ne">{marcas()}
{rafaga(0, 160, 1080, 900, n=14, color='var(--az)', delay=.05)}
<div class="abs calado" style="left:-40px;top:300px;font-size:560px;color:rgba(154,174,255,.5)">14</div>
<div class="meta fade" style="top:130px"><img src="{LBL}" alt="Masherr"><span style="color:var(--ce)">{dia} · {fecha}</span></div>
<div class="abs" style="left:96px;top:1000px"><div class="rot fade" style="color:var(--ce);animation-delay:.3s">Turno tarde</div></div>
<div class="abs C" style="left:96px;top:1070px;font-size:150px;line-height:.98">{lineas('Volvimos.', d=.35)}</div>
<div class="abs C" style="left:96px;top:1240px;font-size:84px;line-height:1.05;color:var(--ce)">{lineas('Estamos hasta las 17.', d=.55)}</div>
<p class="abs fade" style="left:96px;right:120px;top:1380px;font-size:38px;line-height:1.45;color:#C9CDDA;animation-delay:.85s">¿No llegás? Armá el pedido en la web y lo cerramos por WhatsApp.</p>
<div class="abs fade" style="left:96px;top:1560px;animation-delay:1s"><span class="chip blanco">{WEB}masherrferreteria.com.ar</span></div>
<div class="pie fade" style="color:var(--ce);animation-delay:1.15s"><span>VILLA LYNCH · SAN MARTÍN</span><span>@MASHERRFERRETERIA</span></div>
</section>'''

def h_cierre(dia, fecha, sab=False):
    estrellas = ''.join(STAR.format(s=58, c='var(--ce)') for _ in range(5))
    return f'''<section class="story az">{marcas()}
{rafaga(0, 180, 760, 620, n=11, color='rgba(255,255,255,.10)', delay=.05, origen='left')}
<div class="meta fade" style="top:130px"><img src="{LBL}" alt="Masherr"><span style="color:var(--ce)">{dia} · {fecha}</span></div>
<div class="abs" style="left:96px;top:560px"><div class="rot fade" style="color:var(--ce);animation-delay:.2s">{'Buen finde' if sab else 'Hasta mañana'}</div></div>
<div class="abs C" style="left:96px;top:630px;font-size:170px;line-height:.95">{lineas('Cerramos', 'por hoy.', d=.3)}</div>
<div class="abs fade" style="left:96px;right:96px;top:1040px;display:flex;border-top:3px solid var(--ce);border-bottom:3px solid var(--ce);animation-delay:.75s">
<div style="flex:1;padding:30px 0"><div class="C" style="font-size:26px;letter-spacing:.2em;color:var(--ce)">{'EL LUNES' if sab else 'MAÑANA'}</div><div class="C" style="font-size:58px;margin-top:6px">8:00</div></div>
<div style="flex:1;padding:30px 0 30px 40px;border-left:3px solid var(--ce)"><div class="C" style="font-size:26px;letter-spacing:.2em;color:var(--ce)">LA WEB</div><div class="C" style="font-size:58px;margin-top:6px">24 h</div></div></div>
<div class="abs fade" style="left:96px;top:1300px;display:flex;gap:10px;animation-delay:.95s">{estrellas}</div>
<p class="abs fade" style="left:96px;right:96px;top:1390px;font-size:40px;line-height:1.4;animation-delay:1.05s">Si te atendimos bien, contalo en Google. Nos ayuda muchísimo.</p>
<div class="sticker" style="left:96px;right:96px;top:1560px;height:150px;color:#fff">STICKER · RESEÑA EN GOOGLE</div>
</section>'''

def h_compartir(dia, fecha, titulo, prod, rot=-8, ancho=760, top=980, tag='Nuevo posteo'):
    return f'''<section class="story bl">{marcas()}
<div class="abs" style="left:0;right:0;top:860px;height:820px;background:var(--gr)"></div>
{rafaga(300, 860, 780, 820, n=12, color='var(--gr2)', delay=.05)}
<div class="meta fade" style="top:130px"><img src="{LAZ}" alt="Masherr"><span style="color:var(--az)">{dia} · {fecha}</span></div>
<div class="abs" style="left:96px;top:340px"><div class="rot fade" style="color:var(--az)">{tag}</div></div>
<div class="abs C" style="left:96px;top:410px;font-size:118px;line-height:1">{lineas(*titulo, d=.25)}</div>
<img class="prod entra-der" src="{r(P[prod])}" style="--rot:{rot}deg;right:70px;top:{top}px;width:{ancho}px;animation-delay:.6s" alt="">
<div class="sticker" style="left:96px;right:96px;top:1720px;height:120px;color:var(--az);background:#fff">COMPARTÍ ACÁ LA PUBLICACIÓN</div>
</section>'''

def h_resenas_compartir(dia, fecha):
    return f'''<section class="story ne">{marcas()}
{rafaga(0, 160, 1080, 900, n=14, color='var(--az)', delay=.05)}
<div class="meta fade" style="top:130px"><img src="{LBL}" alt="Masherr"><span style="color:var(--ce)">{dia} · {fecha}</span></div>
<div class="abs" style="left:96px;top:560px"><div class="rot fade" style="color:var(--ce)">Gracias</div></div>
<div class="abs C" style="left:90px;top:620px;font-size:400px;line-height:.85">{lineas('4,7', d=.3)}</div>
<div class="abs fade" style="left:96px;top:980px;display:flex;gap:12px;animation-delay:.7s">{''.join(STAR.format(s=70, c='var(--ce)') for _ in range(5))}</div>
<div class="abs C" style="left:96px;top:1090px;font-size:96px;line-height:1.02">{lineas('131 opiniones', 'en Google.', d=.8)}</div>
<div class="sticker" style="left:96px;right:96px;top:1500px;height:200px;color:#fff">COMPARTÍ ACÁ LA PUBLICACIÓN</div>
</section>'''

# ====================================================================== CARRUSELES
def c_portada(n_total, titulo, sub, prods, rot):
    imgs = ''.join(f'<img class="prod entra-der" src="{r(P[p])}" style="--rot:{a}deg;left:{x}px;top:{y}px;width:{w}px" alt="">' for p, x, y, w, a in prods)
    return f'''<section class="post ne">{marcas()}
{rafaga(380, 210, 700, 760, n=12, color='var(--az)', delay=0)}
<div class="meta"><img src="{LBL}" alt="Masherr"><span style="color:var(--ce)">GUÍA · 01/{n_total:02d}</span></div>
{imgs}
<div class="abs" style="left:72px;top:690px"><div class="rot" style="color:var(--ce)">Consejo de ferretero</div></div>
<div class="abs C" style="left:72px;right:72px;top:750px;font-size:{rot}px;line-height:.98">{titulo}</div>
<p class="abs" style="left:72px;right:240px;top:1110px;font-size:30px;line-height:1.4;color:#C9CDDA">{sub}</p>
<div class="desliza" style="color:var(--ce)">DESLIZÁ<b></b></div><div class="pag" style="color:var(--ce)">01 / {n_total:02d}</div>
</section>'''

def encajar(prod, caja=(330, 535, 680, 360)):
    from PIL import Image
    iw, ih = Image.open(AQUI / 'recortes' / f'{P[prod]}.png').size
    cx, cy, cw, ch = caja
    e = min(cw / iw, ch / ih)
    w, h = iw * e, ih * e
    return round(cx + (cw - w) / 2), round(cy + (ch - h) / 2), round(w)

def c_paso(i, n_total, num, tag, titulo, prod_nombre, txt, prod, w, rot, x, y, fondo='bl'):
    x, y, w = encajar(prod)
    barras = ''.join(f'<i class="{"on" if k == i else ""}"></i>' for k in range(1, n_total + 1))
    return f'''<section class="post {fondo}">
<div class="abs" style="left:0;top:0;width:470px;height:930px;background:var(--az)"></div>
{rafaga(0, 300, 470, 560, n=10, color='rgba(255,255,255,.08)', delay=0, origen='left')}
<div class="abs calado" style="left:30px;top:250px;font-size:400px;color:var(--ce)">{num}</div>
<div class="meta"><img src="{LBL}" alt="Masherr"><span style="color:var(--az)">{tag}</span></div>
<div class="barras" style="color:var(--az)">{barras}</div>
<img class="prod" src="{r(P[prod])}" style="--rot:{rot}deg;left:{x}px;top:{y}px;width:{w}px" alt="">
<div class="abs" style="left:520px;right:72px;top:250px"><div class="rot" style="color:var(--az);font-size:24px">Paso {num}</div>
<div class="C" style="font-size:66px;line-height:1.02;margin-top:20px">{titulo}</div></div>
<div class="abs" style="left:72px;right:72px;top:975px;padding-top:28px;border-top:4px solid var(--ne)">
<div class="C" style="font-size:48px;color:var(--az)">{prod_nombre}</div>
<p style="font-size:32px;line-height:1.42;color:var(--tx);margin-top:12px">{txt}</p></div>
<div class="desliza" style="color:var(--az)">DESLIZÁ<b></b></div><div class="pag" style="color:var(--az)">{i:02d} / {n_total:02d}</div>
</section>'''

def c_cierre(n_total, titulo):
    return f'''<section class="post az">{marcas()}
{rafaga(0, 820, 1080, 530, n=10, color='rgba(255,255,255,.09)', delay=0, origen='left')}
<div class="meta"><img src="{LBL}" alt="Masherr"><span style="color:var(--ce)">{n_total:02d} / {n_total:02d}</span></div>
<div class="abs calado" style="right:-30px;top:120px;font-size:520px;color:rgba(154,174,255,.35)">?</div>
<div class="abs" style="left:72px;top:300px"><div class="rot" style="color:var(--ce)">¿No sabés cuál?</div></div>
<div class="abs C" style="left:72px;right:72px;top:370px;font-size:112px;line-height:1">{titulo}</div>
<div class="abs" style="left:72px;top:820px;display:flex;flex-direction:column;gap:20px;align-items:flex-start">
<span class="chip wa">{WA}WhatsApp 11 3182-6166</span><span class="chip blanco">{WEB}masherrferreteria.com.ar</span></div>
<div class="pag" style="color:var(--ce);left:72px;right:auto">CALLE 38 4335 · VILLA LYNCH</div>
</section>'''

def carrusel_discos():
    T = 6
    s = [c_portada(T, '¿Qué disco<br>va con cada<br>trabajo?', 'Usar el disco equivocado gasta más, corta peor y es peligroso. Guardá esta guía.',
                   [('corte', 520, 170, 420, -10), ('flap40', 700, 380, 320, 12), ('copa', 470, 470, 240, -18)], 108)]
    pasos = [('01', 'CORTE', 'Cortar<br>metal', 'Disco de corte para acero', 'Fino (1 mm): corta rápido y con menos rebaba en perfiles, caños y chapa.', 'corte', 600, -8, 360, 370),
             ('02', 'DESBASTE', 'Desbastar<br>y limpiar<br>soldadura', 'Flap grano 40 o 60', 'Saca material sin “morder” la pieza. Ideal para cordones y óxido.', 'flap40', 520, 10, 410, 470),
             ('03', 'TERMINACIÓN', 'Dejar la<br>terminación<br>lisa', 'Flap grano 80 o 120', 'Después del desbaste: emparejá y dejá la superficie lista para pintar.', 'flap80', 520, -6, 410, 470),
             ('04', 'PERFORACIÓN', 'Perforar<br>cerámica', 'Copa diamantada en seco', 'Agujeros limpios para caños y griferías, directo en la amoladora.', 'copa', 600, -14, 330, 560)]
    for k, (num, tag, tit, pn, txt, pr, w, rot, x, y) in enumerate(pasos, 2):
        s.append(c_paso(k, T, num, tag, tit, pn, txt, pr, w, rot, x, y, 'bl' if k % 2 else 'gr'))
    s.append(c_cierre(T, 'Contanos<br>qué vas a hacer.<br>Te decimos cuál.'))
    return s

def carrusel_medicion():
    T = 6
    s = [c_portada(T, 'Medí una vez.<br>Cortá una<br>sola vez.', 'La herramienta de medición correcta para cada trabajo. Guardá esta guía.',
                   [('cinta', 560, 160, 360, -10), ('medidor', 870, 280, 140, 14), ('nivel', 430, 470, 560, -16)], 104)]
    pasos = [('01', 'MEDIR', 'Medidas<br>cortas<br>y obra', 'Cinta métrica', 'Para el día a día. Elegí el largo según el trabajo: 3, 5, 8 o 10 metros.', 'cinta', 470, -8, 400, 400),
             ('02', 'NIVELAR', 'Que quede<br>derecho', 'Nivel de burbuja', 'Estantes, cuadros, aberturas y cerámicos. De 40 cm a 1,20 m.', 'nivel', 640, -20, 330, 560),
             ('03', 'LÁSER', 'Distancias<br>largas,<br>sin ayuda', 'Medidor láser', 'Mide ambientes y galpones en un segundo, sin que nadie sostenga la cinta.', 'medidor', 250, 10, 580, 380),
             ('04', 'TRAZAR', 'Líneas<br>en toda<br>la pared', 'Nivel láser', 'Marca una línea recta en paredes enteras: ideal para cerámicos y durlock.', 'laser', 330, 0, 560, 330)]
    for k, (num, tag, tit, pn, txt, pr, w, rot, x, y) in enumerate(pasos, 2):
        s.append(c_paso(k, T, num, tag, tit, pn, txt, pr, w, rot, x, y, 'bl' if k % 2 else 'gr'))
    s.append(c_cierre(T, 'Contanos<br>qué vas a medir.<br>Te asesoramos.'))
    return s

# ====================================================================== POSTEOS
def p_web():
    return f'''<section class="post ne">{marcas()}
{rafaga(300, 140, 780, 1100, n=16, color='var(--az)', delay=0)}
<div class="meta"><img src="{LBL}" alt="Masherr"><span style="color:var(--ce)">NOVEDAD</span></div>
<div class="abs" style="right:90px;top:170px;width:430px;height:900px;transform:rotate(6deg);border-radius:60px;background:#000;padding:18px;box-shadow:0 50px 80px rgba(0,0,0,.5)">
<img src="{SHOT}" style="width:100%;height:100%;object-fit:cover;object-position:top;border-radius:44px" alt="Web de Masherr"></div>
<div class="abs" style="left:72px;top:300px"><div class="rot" style="color:var(--ce)">Web nueva</div></div>
<div class="abs C" style="left:72px;top:370px;font-size:100px;line-height:.98">Toda la<br>ferretería<br>en tu<br>celular.</div>
<div class="abs" style="left:72px;top:880px;display:flex;flex-direction:column;gap:14px;font-family:C;font-size:32px">
<span><b style="color:var(--ce)">01</b>&nbsp; Buscá</span><span><b style="color:var(--ce)">02</b>&nbsp; Armá el carrito</span><span><b style="color:var(--ce)">03</b>&nbsp; Cerrá por WhatsApp</span></div>
<div class="abs" style="left:72px;bottom:90px"><span class="chip blanco" style="font-size:30px">{WEB}masherrferreteria.com.ar</span></div>
</section>'''

def p_kit():
    return f'''<section class="post gr">{marcas()}
<div class="abs calado" style="left:40px;top:110px;font-size:560px;color:var(--gr2);-webkit-text-stroke:5px var(--gr2)">20V</div>
<div class="meta"><img src="{LAZ}" alt="Masherr"><span style="color:var(--az)">PRODUCTO DE LA SEMANA</span></div>
<div class="abs" style="left:0;right:0;top:860px;height:490px;background:var(--az);clip-path:polygon(0 18%,100% 0,100% 100%,0 100%)"></div>
{rafaga(560, 940, 520, 410, n=8, color='rgba(255,255,255,.08)', delay=0)}
<img class="prod" src="{r(P['kit'])}" style="--rot:-4deg;left:110px;top:200px;width:860px" alt="">
<div class="abs" style="left:72px;top:960px;color:#fff"><span class="chip linea" style="color:var(--ce);font-size:24px;padding:12px 22px;letter-spacing:.14em">EMTOP · 20 V BRUSHLESS</span>
<div class="C" style="font-size:60px;line-height:1;margin-top:18px">Taladro percutor<br>+ amoladora</div></div>
<div class="abs" style="left:72px;top:1196px"><span class="chip blanco" style="font-size:28px;padding:16px 28px">{WA}Consultá precio y stock</span></div>
</section>'''

def p_resena():
    return f'''<section class="post az">{marcas()}
{rafaga(0, 860, 1080, 490, n=9, color='rgba(255,255,255,.08)', delay=0, origen='left')}
<div class="abs calado" style="right:40px;top:150px;font-size:560px;color:rgba(154,174,255,.32)">“</div>
<div class="meta"><img src="{LBL}" alt="Masherr"><span style="color:var(--ce)">LO QUE DICEN DE NOSOTROS</span></div>
<div class="abs" style="left:72px;top:250px;display:flex;gap:10px">{''.join(STAR.format(s=60, c='var(--ce)') for _ in range(5))}</div>
<div class="abs C" style="left:72px;right:120px;top:360px;font-size:84px;line-height:1.06">“Se tomaron el tiempo para buscar la que yo necesitaba.”</div>
<div class="abs" style="left:72px;top:800px;font-size:32px;color:var(--ce)">— Lorena, reseña en Google</div>
<div class="abs" style="left:72px;right:72px;top:960px;display:flex;align-items:center;gap:36px;border-top:3px solid var(--ce);padding-top:40px">
<div class="C" style="font-size:180px;line-height:.8">4,7</div><div style="font-size:34px;line-height:1.4;color:#D9DEF0">★ en Google<br><b class="C" style="color:#fff">131 opiniones</b></div></div>
</section>'''

def p_comprar():
    pasos = [('01', 'Entrá a', 'masherrferreteria.com.ar'), ('02', 'Armá', 'tu carrito'), ('03', 'Envialo por', 'WhatsApp')]
    tarjetas = ''.join(f'''<div class="abs" style="left:{72 + k * 40}px;right:{152 - k * 40}px;top:{640 + k * 190}px;height:170px;background:{['#fff', 'var(--az)', 'var(--wa)'][k]};color:{['var(--ne)', '#fff', '#fff'][k]};border-radius:22px;display:flex;align-items:center;gap:34px;padding:0 40px;box-shadow:0 24px 40px rgba(8,9,11,.12)">
<div class="calado" style="font-size:130px;-webkit-text-stroke:3px {['var(--az)', 'var(--ce)', '#fff'][k]}">{n}</div><div><div style="font-size:30px;opacity:.75">{a}</div><div class="C" style="font-size:46px">{b}</div></div></div>''' for k, (n, a, b) in enumerate(pasos))
    return f'''<section class="post gr">{marcas()}
{rafaga(560, 120, 520, 460, n=8, color='var(--gr2)', delay=0)}
<div class="meta"><img src="{LAZ}" alt="Masherr"><span style="color:var(--az)">COMPRÁ ONLINE</span></div>
<div class="abs" style="left:72px;top:230px"><div class="rot" style="color:var(--az)">En 3 pasos</div></div>
<div class="abs C" style="left:72px;top:300px;font-size:100px;line-height:1">Armá el pedido.<br><span style="color:var(--az)">Lo cerramos<br>por WhatsApp.</span></div>
{tarjetas}
</section>'''

# ====================================================================== SEMANA
SEMANA = []
def dia(carpeta, nombre, fecha, sab=False):
    return {'carpeta': carpeta, 'nombre': nombre, 'fecha': fecha, 'sab': sab, 'piezas': []}

d = dia('2026-11-17', 'MARTES', '17.11'); D = d['nombre'], d['fecha']
d['piezas'] = [('historia', '1 - 08.00 Abrimos', h_abrimos(*D)), ('historia', '2 - 12.00 Mediodia', h_mediodia(*D)),
               ('historia', '3 - 13.05 Compartir carrusel', h_compartir(*D, ['¿Qué disco', 'va con cada', 'trabajo?'], 'corte', -10, 640, 1000, 'Nuevo carrusel')),
               ('historia', '4 - 14.00 Volvimos', h_volvimos(*D)), ('historia', '5 - 17.00 Cerramos', h_cierre(*D)),
               ('posteo', 'Martes 17 - 19.00 - Web nueva', p_web())] + [('carrusel', f'Guia de discos/{k:02d}', s) for k, s in enumerate(carrusel_discos(), 1)]
SEMANA.append(d)
d = dia('2026-11-18', 'MIÉRCOLES', '18.11'); D = d['nombre'], d['fecha']
d['piezas'] = [('historia', '1 - 08.00 Abrimos', h_abrimos(*D)), ('historia', '2 - 12.00 Mediodia', h_mediodia(*D)),
               ('historia', '3 - 14.00 Volvimos', h_volvimos(*D)), ('historia', '4 - 17.00 Cerramos', h_cierre(*D)),
               ('historia', '5 - 19.05 Compartir posteo', h_compartir(*D, ['Producto', 'de la', 'semana.'], 'kit', -4, 760, 990)),
               ('posteo', 'Miercoles 18 - 19.00 - Producto de la semana', p_kit())]
SEMANA.append(d)
d = dia('2026-11-19', 'JUEVES', '19.11'); D = d['nombre'], d['fecha']
d['piezas'] = [('historia', '1 - 08.00 Abrimos', h_abrimos(*D)), ('historia', '2 - 12.00 Mediodia', h_mediodia(*D)),
               ('historia', '3 - 13.05 Compartir carrusel', h_compartir(*D, ['Medí una vez.', 'Cortá una', 'sola vez.'], 'cinta', -10, 600, 980, 'Nuevo carrusel')),
               ('historia', '4 - 14.00 Volvimos', h_volvimos(*D)), ('historia', '5 - 17.00 Cerramos', h_cierre(*D))] + \
              [('carrusel', f'Como medir bien/{k:02d}', s) for k, s in enumerate(carrusel_medicion(), 1)]
SEMANA.append(d)
d = dia('2026-11-20', 'VIERNES', '20.11'); D = d['nombre'], d['fecha']
d['piezas'] = [('historia', '1 - 08.00 Abrimos', h_abrimos(*D)), ('historia', '2 - 12.00 Mediodia', h_mediodia(*D)),
               ('historia', '3 - 14.00 Volvimos', h_volvimos(*D)), ('historia', '4 - 17.00 Cerramos', h_cierre(*D)),
               ('historia', '5 - 19.05 Compartir posteo', h_resenas_compartir(*D)), ('posteo', 'Viernes 20 - 19.00 - Resena', p_resena())]
SEMANA.append(d)
d = dia('2026-11-21', 'SÁBADO', '21.11', True); D = d['nombre'], d['fecha']
d['piezas'] = [('historia', '1 - 08.00 Abrimos', h_abrimos(*D, sab=True)), ('historia', '2 - 12.30 Cerramos', h_cierre(*D, sab=True)),
               ('posteo', 'Sabado 21 - 10.00 - Como comprar', p_comprar())]
SEMANA.append(d)

manifiesto = []
for d in SEMANA:
    base = AQUI / d['carpeta']; base.mkdir(exist_ok=True)
    for tipo, nombre, html in d['piezas']:
        archivo = f"{tipo}__{nombre.replace('/', '__').replace(' ', '_')}.html"
        (base / archivo).write_text(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{html}</body></html>')
        manifiesto.append({'dia': d['carpeta'], 'diaNombre': f"{d['nombre'].title()} {d['fecha'][:2]}", 'tipo': tipo, 'nombre': nombre, 'html': f"{d['carpeta']}/{archivo}"})
(AQUI / 'manifiesto.json').write_text(json.dumps(manifiesto, ensure_ascii=False, indent=1))
print(len(manifiesto), 'piezas')
