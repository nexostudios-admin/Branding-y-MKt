"""Placas de Instagram con el branding de Masherr (posts 1080x1350 y stories 1080x1920).
Uso: python3 generar_placas.py && node exportar_placas.js
Estilo: minimalista, humanizado (voz de Guido, reseñas reales), sin precios (se consultan en la web o por WhatsApp), con llamado a la venta.
"""
from pathlib import Path

AQUI = Path(__file__).parent
IMG = '../web/sitio/img/productos/'
F = '../catalogo/fonts/'
LOGO_AZ = '../catalogo/img/masher-logo-azul.png'
LOGO_BL = '../catalogo/img/masher-logo-blanco.png'
WEB = 'masherrferreteria.com.ar'
foto = lambda base: f'{IMG}{base.split("/")[-1]}-1024-1024.webp'
precio = lambda n: '$' + f'{n:,}'.replace(',', '.')
ESTRELLA = '<svg viewBox="0 0 24 24"><path d="M12 2.5l2.9 6.1 6.6.8-4.9 4.6 1.3 6.6L12 17.3 6.1 20.6l1.3-6.6L2.5 9.4l6.6-.8z"/></svg>'
WA = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3.5 20.5l1.4-4.2A8.5 8.5 0 1 1 8 19.3z"/><path d="M9 8.6c.2 2.9 2.6 5.4 5.6 6l1.3-1.4-2-1.1-1 .7c-.9-.4-2-1.5-2.4-2.4l.7-1-1-2z"/></svg>'

def pie(oscuro=False, cta='Comprá en la web · link en la bio'):
    return f'''<div class="pie{' osc' if oscuro else ''}"><img src="{LOGO_BL if oscuro else LOGO_AZ}" alt="Masherr"><span>{cta}</span></div>'''

def producto(n, rot, nombre, marca, p, img, bajada, sello=''):
    return ('post', n, f'''<section class="post claro">
<div class="rotulo">{rot}</div>
<div class="foto"><img src="{foto(img)}" alt="">{f'<span class="sello">{sello}</span>' if sello else ''}</div>
<div class="info"><div><span class="marca">{marca}</span><h2>{nombre}</h2><p>{bajada}</p></div>
<div class="cta">Consultá precio<br>y stock →</div></div>
{pie()}</section>''')

PLACAS = [
 # 1 · Humanizado: presentación de Guido (foto real a reemplazar)
 ('post', '01_guido', f'''<section class="post oscuro">
<div class="rayas"></div>
<div class="hueco"><span>FOTO REAL DE GUIDO<br>en el mostrador</span></div>
<div class="txt-abajo"><div class="rotulo az">FERRETERÍA INDUSTRIAL · VILLA LYNCH</div>
<h1>“Soy Guido.<br>Te ayudo a elegir<br>la herramienta justa.”</h1></div>
{pie(True, 'Escribinos o vení al local')}</section>'''),
 # 2 · Producto
 producto('02_amoladora', 'PRODUCTO DE LA SEMANA', 'Amoladora angular 115 mm · 650 W', 'VANDEN', 46000,
          'img/productos/amoladora-angular-115mm-650w-11565-vanden-z9jit-0', 'Para cortes y terminaciones en hierro, chapa y cerámica.'),
 # 3 · Comparativa
 ('post', '03_comparativa', f'''<section class="post claro">
<div class="rotulo">¿CUÁL TE CONVIENE?</div><h1 class="t-osc">115 o 180.</h1>
<div class="vs"><div><img src="{foto('amoladora-angular-115mm-650w-11565-vanden-z9jit-0')}" alt=""><b>115 mm</b><span>Cortes finos, chapa, terminaciones. Liviana.</span><em>Para el día a día</em></div>
<div><img src="{foto('amoladora-angular-180mm-2000w-nemea180200-nebraska-15559-0')}" alt=""><b>180 mm</b><span>Cortes profundos y desbaste pesado.</span><em>Para trabajo pesado</em></div></div>
{pie(cta='¿Dudas? Te asesoramos por WhatsApp')}</section>'''),
 # 4 · Reseña real
 ('post', '04_resena', f'''<section class="post oscuro">
<div class="estrellas">{ESTRELLA * 5}</div>
<blockquote>“Se tomaron el tiempo para buscar la que yo necesitaba.”</blockquote>
<div class="firma">Lorena · reseña en Google</div>
<div class="dato"><b>4,7</b><span>★ en Google<br>131 opiniones</span></div>
{pie(True, 'Gracias por elegirnos')}</section>'''),
 # 5 · Combo
 producto('05_combo', 'COMBO', 'Bolso + 3 pinzas + set de 43 piezas', 'EMTOP', 115000,
          'img/productos/combo-de-herramientas-emtop-bolso-juego-de-pinzas-set-de-puntas-y-tubos-go0pz-0', 'Para armar tu primera caja de herramientas, completa.', 'TODO EN UNO'),
 # 6 · Consejo
 ('post', '06_consejo', f'''<section class="post azul">
<div class="rayas"></div><div class="rotulo az">CONSEJO DE FERRETERO</div>
<div class="numero">01</div>
<h1>No uses el mismo destornillador para todo.</h1>
<p class="bajada">La punta justa evita pelar el tornillo. Tenemos juegos para cada tipo de tornillo.</p>
{pie(True, 'Guardá este post')}</section>'''),
 # 7 · Producto soldadura
 producto('07_soldadora', 'SOLDADURA', 'Soldadora inverter SI 140', 'PEGASO', 182000,
          'img/productos/soldadora-inverter-si-140pegaso-5u1ui-0', 'Compacta y portátil, para electrodo. Ideal para empezar.'),
 # 8 · Cómo comprar
 ('post', '08_como_comprar', f'''<section class="post claro">
<div class="rotulo">CÓMO COMPRAR</div><h1 class="t-osc">Armá el pedido.<br>Lo cerramos<br>por WhatsApp.</h1>
<ol class="pasos"><li><b>1</b>Entrá a {WEB}</li><li><b>2</b>Agregá al carrito</li><li><b>3</b>Envialo por WhatsApp y confirmamos</li></ol>
{pie(cta='Link en la bio')}</section>'''),
 # 9 · Empresas
 ('post', '09_empresas', f'''<section class="post oscuro">
<div class="rayas"></div><div class="rotulo az">INDUSTRIAS · TALLERES · OBRA</div>
<h1>¿Tu taller no puede frenar?</h1>
<p class="bajada">Mandanos la lista de lo que necesitás y te cotizamos. Herramientas, insumos y equipos de las mejores marcas.</p>
<div class="chip-wa">{WA}<span>11 3182-6166</span></div>
{pie(True, 'Pedí tu cotización')}</section>'''),
 # Stories
 ('story', 's1_producto', f'''<section class="story claro">
<div class="rotulo">NUEVO EN LA WEB</div>
<div class="foto grande"><img src="{foto('kit-taladro-percutor-atornillador-y-amoladora-brushless-emtop-emteckl202564-317mg-0')}" alt=""></div>
<span class="marca">EMTOP · 20 V BRUSHLESS</span><h2>Kit taladro percutor + amoladora</h2>
<p>2 baterías de 4 Ah, cargador, 10 discos y 47 accesorios.</p>
<div class="cta grande">Precio y stock en la web →</div>
<div class="sticker">ACÁ VA EL STICKER DE ENLACE ↗</div>
<img class="logo-st" src="{LOGO_AZ}" alt="Masherr"></section>'''),
 ('story', 's2_encuesta', f'''<section class="story oscuro">
<div class="rayas"></div><div class="rotulo az">ENCUESTA</div>
<h1>¿Con cable o a batería?</h1>
<div class="sticker osc">ACÁ VA EL STICKER DE ENCUESTA</div>
<p class="bajada">Mañana te cuento cuál conviene según tu trabajo.<br>— Guido</p>
<img class="logo-st" src="{LOGO_BL}" alt="Masherr"></section>'''),
 ('story', 's3_resenas', f'''<section class="story azul">
<div class="rayas"></div><div class="estrellas">{ESTRELLA * 5}</div>
<h1>¿Te atendimos bien?</h1><p class="bajada">Dejanos tu opinión en Google. Nos ayuda a que más vecinos nos encuentren.</p>
<div class="sticker osc">ACÁ VA EL STICKER DE ENLACE A LA RESEÑA</div>
<img class="logo-st" src="{LOGO_BL}" alt="Masherr"></section>'''),
]

CSS = f'''
@font-face{{font-family:C;src:url({F}DejaVuSansCondensed-Bold.ttf);font-weight:700}}
@font-face{{font-family:T;src:url({F}DejaVuSans.ttf)}}
@font-face{{font-family:T;src:url({F}DejaVuSans-Bold.ttf);font-weight:700}}
:root{{--az:#17256B;--ne:#08090B;--ce:#9AAEFF;--gr:#EEF0F4;--tx:#50566A}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#666;font-family:T,sans-serif;display:flex;flex-wrap:wrap;gap:30px;padding:30px}}
section{{position:relative;overflow:hidden;padding:84px 80px}}
.post{{width:1080px;height:1350px}} .story{{width:1080px;height:1920px;padding:150px 90px}}
.claro{{background:#fff;color:var(--ne)}} .oscuro{{background:var(--ne);color:#fff}} .azul{{background:var(--az);color:#fff}}
.rayas{{position:absolute;right:0;top:0;width:300px;height:520px;background:repeating-linear-gradient(to bottom,var(--az) 0 18px,transparent 18px 30px);clip-path:polygon(30% 0,100% 0,100% 100%,0 100%)}}
.azul .rayas{{background:repeating-linear-gradient(to bottom,rgba(255,255,255,.08) 0 18px,transparent 18px 30px)}}
.rotulo{{font-family:C;font-size:30px;letter-spacing:.12em;color:var(--az);display:flex;align-items:center;gap:18px;position:relative}}
.rotulo::before{{content:"";width:56px;height:8px;background:currentColor}}
.az{{color:var(--ce)}}
h1{{font-family:C;font-size:104px;line-height:1.02;margin-top:30px;position:relative}}
.t-osc{{color:var(--ne)}}
h2{{font-family:C;font-size:58px;line-height:1.08;margin-top:10px}}
.bajada{{font-size:38px;line-height:1.45;color:#C6CAD6;margin-top:36px;max-width:860px;position:relative}}
.claro .bajada{{color:var(--tx)}} .azul .bajada{{color:#DDE2F5}}
.foto{{position:relative;margin-top:44px;height:600px;background:var(--gr);border-radius:16px;display:grid;place-items:center;overflow:hidden}}
.foto img{{max-width:86%;max-height:88%;mix-blend-mode:multiply}}
.foto.grande{{height:700px}}
.sello{{position:absolute;left:28px;bottom:28px;background:var(--az);color:#fff;font-family:C;font-size:30px;letter-spacing:.08em;padding:12px 22px}}
.info{{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-top:40px}}
.info p,.story p{{font-size:32px;line-height:1.4;color:var(--tx);margin-top:14px}}
.marca{{font-family:C;font-size:28px;letter-spacing:.1em;color:var(--az);border:3px solid var(--az);padding:6px 14px;display:inline-block}}
.precio{{font-family:C;font-size:92px;color:var(--az);white-space:nowrap;line-height:1}}
.precio small{{font-size:52px;vertical-align:.5em;margin-right:4px}}
.cta{{font-family:C;font-size:36px;line-height:1.2;color:#fff;background:var(--az);padding:22px 28px;border-radius:10px;white-space:nowrap;text-align:left}}
.cta.grande{{display:inline-block;font-size:44px;margin-top:40px;padding:28px 36px}}
.pie{{position:absolute;left:80px;right:80px;bottom:64px;display:flex;justify-content:space-between;align-items:center;border-top:3px solid var(--az);padding-top:30px}}
.pie.osc{{border-color:var(--ce)}}
.pie img{{height:64px}} .pie span{{font-family:C;font-size:30px;color:var(--az)}} .pie.osc span{{color:var(--ce)}}
.hueco{{position:absolute;left:0;right:0;top:0;height:760px;background:#1C1F27;display:grid;place-items:center;text-align:center;border-bottom:8px solid var(--az)}}
.hueco span{{font-family:C;font-size:40px;letter-spacing:.08em;color:#5A6070;line-height:1.4;border:4px dashed #3A3F4D;padding:40px 60px}}
.txt-abajo{{position:absolute;left:80px;right:80px;top:820px}} .txt-abajo h1{{font-size:76px}}
.vs{{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:44px}}
.vs div{{background:var(--gr);border-radius:16px;padding:30px;display:flex;flex-direction:column;gap:10px}}
.vs img{{height:300px;object-fit:contain;mix-blend-mode:multiply}}
.vs b{{font-family:C;font-size:64px;color:var(--az)}} .vs span{{font-size:30px;line-height:1.35;color:var(--tx)}} .vs em{{font-style:normal;font-family:C;font-size:38px;margin-top:6px}}
.estrellas{{display:flex;gap:16px;margin-top:40px}} .estrellas svg{{width:76px;height:76px;fill:var(--ce)}}
blockquote{{font-family:C;font-size:86px;line-height:1.12;margin-top:70px}}
.firma{{font-size:36px;color:var(--ce);margin-top:40px}}
.dato{{display:flex;align-items:center;gap:28px;margin-top:90px;border-top:2px solid #2A2E3A;padding-top:44px}}
.dato b{{font-family:C;font-size:150px;line-height:1}} .dato span{{font-size:36px;color:#C6CAD6;line-height:1.35}}
.numero{{font-family:C;font-size:300px;line-height:.9;color:var(--ce);margin-top:60px;position:relative}}
.azul h1{{font-size:96px}}
.pasos{{list-style:none;margin-top:70px}} .pasos li{{display:flex;gap:30px;align-items:center;font-size:42px;padding:30px 0;border-bottom:2px solid #DDE0E7}}
.pasos b{{font-family:C;width:84px;height:84px;border-radius:50%;background:var(--az);color:#fff;display:grid;place-items:center;font-size:44px;flex:none}}
.chip-wa{{display:inline-flex;align-items:center;gap:20px;margin-top:60px;background:#128C3E;padding:24px 36px;border-radius:12px;position:relative}}
.chip-wa svg{{width:56px;height:56px}} .chip-wa span{{font-family:C;font-size:46px}}
.story h1{{font-size:120px}} .story h2{{font-size:72px;margin-top:26px}}
.story .precio{{font-size:130px;margin-top:30px}} .story .precio small{{font-size:70px}}
.story .marca{{margin-top:44px}}
.sticker{{margin-top:60px;border:4px dashed var(--az);color:var(--az);font-family:C;font-size:34px;letter-spacing:.06em;padding:40px;text-align:center}}
.sticker.osc{{border-color:var(--ce);color:var(--ce)}}
.logo-st{{position:absolute;left:90px;bottom:120px;height:90px}}
.story.oscuro,.story.azul{{padding-top:460px}}
.story .sticker{{margin-top:50px}}
'''
html = f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS}</style></head><body>' + ''.join(
    h.replace('<section class="', f'<section data-n="{n}" data-t="{t}" class="', 1) for t, n, h in PLACAS) + '</body></html>'
(AQUI / 'placas.html').write_text(html)
print(len(PLACAS), 'placas')
