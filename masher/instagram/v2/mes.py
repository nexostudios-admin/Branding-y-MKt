"""Masherr · Instagram · contenido del lunes 16 al lunes 30 de noviembre de 2026.

Todos los días: 1 posteo + 1 carrusel en el feed + historias.
Suma la Comunidad Masherr (grupo de WhatsApp) y las reseñas de Google. Sin precios.
Reutiliza el sistema visual de generar_v2.py (ráfaga, tipografía calada, productos recortados).

Uso: python3 mes.py && node exportar_v2.js --manifiesto manifiesto_mes.json --salida salida_mes
"""
import json
from generar_v2 import *  # noqa: F401,F403  (CSS, rafaga, lineas, marcas, historias y carruseles base)
from generar_v2 import AQUI, P, r, LAZ, LBL, WA, WEB, STAR, CSS, h_abrimos, h_mediodia, h_volvimos, h_cierre, h_compartir, \
    h_resenas_compartir, c_paso, carrusel_discos, carrusel_medicion, p_web, p_kit, p_resena, p_comprar, rafaga, lineas, marcas

# ---------------------------------------------------------------- productos nuevos (fotos reales del catálogo, recortadas)
P.update({
    'percutor': 'taladro-percutor-bosch-13mm-550w-gsb-550re-azul-marino-50-1x5ud-0',
    'atornillador': 'taladro-atornillador-a-bateria-gsr-120-li-bosch-12v-30nm-jlz83-0',
    'rotomartillo': 'rotomartillo-sds-plus-d25133k-800w-26j-dewalt-10rc5-0',
    'destornilladores': 'juego-de-destornilladores-6pzas-phpl-esst0621emtop-sg817-0',
    'pinza': 'pinza-pico-de-loro-255mmm-eplrp1011-emtop-ktr9m-0',
    'taladro12': 'taladro-atornillador-12v-nebraska-nemebta612-10mm-48cyt-0',
    'amo115': 'amoladora-angular-115mm-800w-dwe-4020-dewalt-18xn9-0',
    'amo180': 'amoladora-angular-180mm-2200w-dwe491-dewalt-w8vql-0',
    'sold140': 'soldadora-inverter-si-140pegaso-5u1ui-0',
    'sold160': 'soldadora-inverter-si-160-pro-pegaso-1kxch-0',
    'sold190': 'soldadora-inverter-si-190-pro-pegaso-11yzz-0',
    'mascara': 'mascara-fotosensible-p-soldador-edge-500sfoxtter-1ps2p-0',
    'mechas': 'juego-de-mechas-16pzas-a-rapido-madera-widia-ecdb01601-emtop-caoov-0',
    'caja_stanley': 'caja-de-herramientas-plastica-19-16-013stanley-5nd5g-0',
    'caja_lara': 'caja-de-herramientas-metalica-450-x-220-x-220-n11-lara-rd4bz-0',
    'bolso': 'bolso-de-herramientas-emtop-41-x-235-x-26-cm-c06fy-0',
    'packout': 'carro-de-herramientas-modular-packout-3-modulos-milwaukee-e3vsh-0',
    'bosch_amo': 'amoladora-angular-125mm-900w-gws-9-125-bosch-cgcvg-0',
    'karcher': 'hidrolavadora-1500w-120bar-k3-black-edition-karcher-4r30i-0',
    'bahco': 'pinza-pico-de-loro-poligrip-8224-ip-bahco-zdb8y-0',
    'hidro_neb': 'hidrolavadora-2200w-160bar-nemehl2200-nebraska-1ed68-0',
    'aspi_neb': 'aspiradora-1200w-40lts-solidos-y-liquidos-neas351200-nebraska-19my0-0',
    'amo20v': 'amoladora-angular115mm-8-500-rpm-20v-brushless-one-power-c-maletin-nebraska-1pola-0',
    'caladora20v': 'sierra-caladora-a-bateria-one-power-20v-nebraska-incluye-cargador-rapido-1-bateria-yxxiu-0',
    'sierra20v': 'sierra-de-mano-5-one-power-20v-nebraska-incluye-cargador-rapido-1-bateria-1eo9m-0',
})
import glob, os
for k, v in list(P.items()):  # los nombres largos se resuelven por prefijo contra la carpeta de recortes
    if not (AQUI / 'recortes' / f'{v}.png').exists():
        m = sorted(glob.glob(str(AQUI / 'recortes' / (v.rsplit('-', 2)[0][:40] + '*.png'))))
        if not m: raise SystemExit(f'Falta recorte: {k} → {v}')
        P[k] = os.path.basename(m[0])[:-4]

CAP = '../capturas/'
GRUPO = 'chat.whatsapp.com · Comunidad Masherr'
TEL = 'WhatsApp 11 3182-6166'

def estrellas(s, c='var(--ce)'):
    return ''.join(STAR.format(s=s, c=c) for _ in range(5))

# ====================================================================== HISTORIAS NUEVAS
def h_comunidad(dia, fecha, v=1):
    if v == 1:
        return f'''<section class="story ne">{marcas()}
{rafaga(380, 170, 700, 820, n=13, color='var(--az)', delay=.05)}
<div class="abs calado" style="right:-40px;top:300px;font-size:520px;color:rgba(154,174,255,.35)">%</div>
<div class="meta fade" style="top:130px"><img src="{LBL}" alt="Masherr"><span style="color:var(--ce)">{dia} · {fecha}</span></div>
<div class="abs" style="left:96px;top:520px"><div class="rot fade" style="color:var(--ce);animation-delay:.2s">Comunidad Masherr</div></div>
<div class="abs C" style="left:90px;top:590px;font-size:150px;line-height:1">{lineas('Descuentos.', 'Promos.', '<span style="color:var(--ce)">Rifas.</span>', d=.3, paso=.16)}</div>
<div class="abs C" style="left:96px;top:1080px;font-size:72px">{lineas('Y mucho más.', d=.85)}</div>
<p class="abs fade" style="left:96px;right:120px;top:1200px;font-size:38px;line-height:1.45;color:#C9CDDA;animation-delay:1s">Sumate gratis a nuestro grupo de WhatsApp y enterate antes que nadie.</p>
<div class="abs fade" style="left:96px;top:1390px;animation-delay:1.1s"><span class="chip wa">{WA}Unirme a la comunidad</span></div>
<div class="sticker" style="left:96px;right:96px;top:1560px;height:150px;color:#fff">STICKER · ENLACE AL GRUPO</div>
</section>'''
    return f'''<section class="story az">{marcas()}
{rafaga(0, 1180, 1080, 740, n=12, color='rgba(255,255,255,.08)', delay=.05, origen='left')}
<div class="meta fade" style="top:130px"><img src="{LBL}" alt="Masherr"><span style="color:var(--ce)">{dia} · {fecha}</span></div>
<div class="abs" style="left:96px;top:380px"><div class="rot fade" style="color:var(--ce);animation-delay:.2s">Comunidad Masherr</div></div>
<div class="abs C" style="left:90px;top:450px;font-size:136px;line-height:1">{lineas('¿Ya estás', 'en la', '<span style="color:var(--ce)">comunidad?</span>', d=.3)}</div>
<div class="abs fade" style="left:96px;right:96px;top:930px;display:flex;flex-direction:column;gap:22px;font-family:C;font-size:44px;animation-delay:.9s">
<span><b style="color:var(--ce)">01</b>&nbsp; Tocá el enlace</span><span><b style="color:var(--ce)">02</b>&nbsp; Unite al grupo</span><span><b style="color:var(--ce)">03</b>&nbsp; Recibí descuentos, promos y rifas</span></div>
<div class="sticker" style="left:96px;right:96px;top:1350px;height:160px;color:#fff">STICKER · ENLACE AL GRUPO</div>
<div class="pie fade" style="color:var(--ce);animation-delay:1.1s"><span>ES GRATIS</span><span>@MASHERRFERRETERIA</span></div>
</section>'''

def h_domingo(dia, fecha):
    return f'''<section class="story gr">{marcas()}
{rafaga(0, 1500, 1080, 420, n=8, color='var(--gr2)', delay=.1, origen='left')}
<div class="abs calado" style="right:-30px;top:220px;font-size:560px;color:var(--gr2);-webkit-text-stroke:5px var(--gr2)">D</div>
<div class="meta fade" style="top:130px"><img src="{LAZ}" alt="Masherr"><span style="color:var(--az)">{dia} · {fecha}</span></div>
<div class="abs" style="left:96px;top:520px"><div class="rot fade" style="color:var(--az)">Domingo</div></div>
<div class="abs C" style="left:90px;top:590px;font-size:132px;line-height:.98">{lineas('Hoy', 'descansamos.', d=.3)}</div>
<div class="abs fade" style="left:96px;right:96px;top:950px;display:flex;border-top:3px solid var(--az);border-bottom:3px solid var(--az);animation-delay:.7s">
<div style="flex:1;padding:30px 0"><div class="C" style="font-size:26px;letter-spacing:.2em;color:var(--az)">MAÑANA</div><div class="C" style="font-size:58px;margin-top:6px">8:00</div></div>
<div style="flex:1;padding:30px 0 30px 40px;border-left:3px solid var(--az)"><div class="C" style="font-size:26px;letter-spacing:.2em;color:var(--az)">LA WEB</div><div class="C" style="font-size:58px;margin-top:6px">24 h</div></div></div>
<p class="abs fade" style="left:96px;right:120px;top:1210px;font-size:40px;line-height:1.42;color:var(--tx);animation-delay:.9s">Armá el pedido hoy en la web y el lunes te lo confirmamos por WhatsApp.</p>
<div class="abs fade" style="left:96px;top:1390px;animation-delay:1.05s"><span class="chip azul">{WEB}masherrferreteria.com.ar</span></div>
<div class="sticker" style="left:96px;right:96px;top:1560px;height:140px;color:var(--az)">STICKER · ENLACE A LA WEB</div>
</section>'''

def h_compartir_texto(dia, fecha, titulo, tag, grande, fondo='az'):
    claro = fondo == 'gr'
    return f'''<section class="story {fondo}">{marcas()}
{rafaga(300, 860, 780, 820, n=12, color='var(--gr2)' if claro else 'rgba(255,255,255,.08)', delay=.05)}
<div class="abs calado" style="right:-30px;top:880px;font-size:520px;color:{'var(--gr2)' if claro else 'rgba(154,174,255,.35)'}">{grande}</div>
<div class="meta fade" style="top:130px"><img src="{LAZ if claro else LBL}" alt="Masherr"><span style="color:{'var(--az)' if claro else 'var(--ce)'}">{dia} · {fecha}</span></div>
<div class="abs" style="left:96px;top:340px"><div class="rot fade" style="color:{'var(--az)' if claro else 'var(--ce)'}">{tag}</div></div>
<div class="abs C" style="left:96px;top:410px;font-size:118px;line-height:1">{lineas(*titulo, d=.25)}</div>
<div class="sticker" style="left:96px;right:96px;top:1000px;height:640px;color:{'var(--az)' if claro else '#fff'}">COMPARTÍ ACÁ LA PUBLICACIÓN</div>
</section>'''

# ====================================================================== POSTEOS NUEVOS
def p_comunidad(v=1):
    if v == 1:
        return f'''<section class="post az">{marcas()}
{rafaga(420, 120, 660, 700, n=12, color='rgba(255,255,255,.09)', delay=0)}
<div class="meta"><img src="{LBL}" alt="Masherr"><span style="color:var(--ce)">NUEVO</span></div>
<div class="abs" style="left:72px;top:250px"><div class="rot" style="color:var(--ce)">Comunidad Masherr</div></div>
<div class="abs C" style="left:66px;top:320px;font-size:128px;line-height:.98">Descuentos<span style="color:var(--ce)"> |</span><br>Promos<span style="color:var(--ce)"> |</span><br>Rifas.</div>
<div class="abs C" style="left:72px;top:745px;font-size:60px;color:var(--ce)">Y mucho más.</div>
<p class="abs" style="left:72px;right:300px;top:850px;font-size:32px;line-height:1.45;color:#D9DEF0">Sumate gratis a nuestro grupo de WhatsApp y enterate antes que nadie.</p>
<div class="abs" style="left:72px;top:1040px;display:flex;flex-direction:column;gap:16px;align-items:flex-start">
<span class="chip wa">{WA}Unite: link en la bio</span><span class="chip linea" style="color:#fff;font-size:28px">masherrferreteria.com.ar/comunidad</span></div>
</section>'''
    return f'''<section class="post ne">{marcas()}
{rafaga(0, 820, 1080, 530, n=10, color='var(--az)', delay=0, origen='left')}
<div class="abs calado" style="right:30px;top:120px;font-size:520px;color:rgba(154,174,255,.32)">?</div>
<div class="meta"><img src="{LBL}" alt="Masherr"><span style="color:var(--ce)">COMUNIDAD MASHERR</span></div>
<div class="abs" style="left:72px;top:260px"><div class="rot" style="color:var(--ce)">Grupo de WhatsApp</div></div>
<div class="abs C" style="left:72px;top:330px;font-size:118px;line-height:1">¿Ya estás<br>en la<br><span style="color:var(--ce)">comunidad?</span></div>
<div class="abs" style="left:72px;right:72px;top:830px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px">
{''.join(f'<div style="background:#101219;border-top:4px solid var(--ce);padding:24px 22px"><div class="C" style="font-size:40px">{t}</div><div style="font-size:24px;color:#BFC4D3;margin-top:8px;line-height:1.35">{x}</div></div>' for t, x in [('Descuentos', 'Exclusivos del grupo'), ('Promos', 'Antes que nadie'), ('Rifas', 'Entre los miembros')])}</div>
<div class="abs" style="left:72px;top:1110px"><span class="chip wa">{WA}Sumate gratis: link en la bio</span></div>
</section>'''

def p_producto(prod, rotulo, marca_txt, titulo, calado, fondo='gr', ancho=820, x=130, y=170, rot=-4):
    return f'''<section class="post {fondo}">{marcas()}
<div class="abs calado" style="left:40px;top:110px;font-size:{560 if len(calado) <= 4 else 380}px;color:var(--gr2);-webkit-text-stroke:5px var(--gr2)">{calado}</div>
<div class="meta"><img src="{LAZ}" alt="Masherr"><span style="color:var(--az)">{rotulo}</span></div>
<div class="abs" style="left:0;right:0;top:860px;height:490px;background:var(--az);clip-path:polygon(0 18%,100% 0,100% 100%,0 100%)"></div>
{rafaga(560, 940, 520, 410, n=8, color='rgba(255,255,255,.08)', delay=0)}
<img class="prod" src="{r(P[prod])}" style="--rot:{rot}deg;left:{x}px;top:{y}px;width:{ancho}px" alt="">
<div class="abs" style="left:72px;top:960px;color:#fff"><span class="chip linea" style="color:var(--ce);font-size:24px;padding:12px 22px;letter-spacing:.14em">{marca_txt}</span>
<div class="C" style="font-size:60px;line-height:1;margin-top:18px">{titulo}</div></div>
<div class="abs" style="left:72px;top:1196px"><span class="chip blanco" style="font-size:28px;padding:16px 28px">{WA}Consultá precio y stock</span></div>
</section>'''

def p_resenas_47():
    return f'''<section class="post ne">{marcas()}
{rafaga(380, 120, 700, 760, n=13, color='var(--az)', delay=0)}
<div class="meta"><img src="{LBL}" alt="Masherr"><span style="color:var(--ce)">RESEÑAS EN GOOGLE</span></div>
<div class="abs" style="left:72px;top:250px"><div class="rot" style="color:var(--ce)">Gracias</div></div>
<div class="abs C" style="left:62px;top:300px;font-size:420px;line-height:.86">4,7</div>
<div class="abs" style="left:72px;top:680px;display:flex;gap:12px">{estrellas(64)}</div>
<div class="abs C" style="left:72px;top:790px;font-size:76px;line-height:1.02">131 clientes nos<br>dejaron su opinión.</div>
<div class="abs" style="left:72px;right:72px;top:1040px;display:flex;align-items:center;gap:30px;border-top:3px solid var(--ce);padding-top:36px">
<img src="../capturas/qr_resenas.png" style="width:170px;height:170px;border-radius:12px" alt="QR reseñas">
<p style="font-size:32px;line-height:1.4;color:#D9DEF0">¿Te atendimos bien?<br><b class="C" style="color:#fff">Escaneá y dejanos la tuya.</b></p></div>
</section>'''

def p_empresas():
    return f'''<section class="post az">{marcas()}
{rafaga(380, 120, 700, 760, n=12, color='rgba(255,255,255,.09)', delay=0)}
<div class="meta"><img src="{LBL}" alt="Masherr"><span style="color:var(--ce)">EMPRESAS · TALLERES · OBRAS</span></div>
<img class="prod" src="{r(P['packout'])}" style="--rot:6deg;right:40px;top:160px;width:250px" alt="">
<div class="abs" style="left:72px;top:250px"><div class="rot" style="color:var(--ce)">Pedidos grandes</div></div>
<div class="abs C" style="left:66px;top:320px;font-size:96px;line-height:1">¿Comprás<br>para tu<br>empresa?<br><span style="color:var(--ce)">Te cotizamos.</span></div>
<div class="abs" style="left:72px;right:72px;top:800px;display:flex;flex-direction:column;gap:14px;font-family:C;font-size:34px">
<span><b style="color:var(--ce)">01</b>&nbsp; Mandanos la lista: productos y cantidades</span><span><b style="color:var(--ce)">02</b>&nbsp; Te respondemos con la cotización</span><span><b style="color:var(--ce)">03</b>&nbsp; Retirás o coordinamos la entrega</span></div>
<div class="abs" style="left:72px;top:1080px;display:flex;gap:14px;flex-wrap:wrap"><span class="chip blanco" style="font-size:28px">{WEB}masherrferreteria.com.ar/empresas</span><span class="chip wa" style="font-size:28px">{WA}11 3182-6166</span></div>
</section>'''

def p_gracias():
    return f'''<section class="post gr">{marcas()}
{rafaga(560, 120, 520, 460, n=8, color='var(--gr2)', delay=0)}
<div class="meta"><img src="{LAZ}" alt="Masherr"><span style="color:var(--az)">CIERRE DE MES</span></div>
<div class="abs" style="left:72px;top:250px"><div class="rot" style="color:var(--az)">Gracias</div></div>
<div class="abs C" style="left:66px;top:320px;font-size:130px;line-height:.98">Gracias,<br><span style="color:var(--az)">noviembre.</span></div>
<p class="abs" style="left:72px;right:200px;top:610px;font-size:34px;line-height:1.45;color:var(--tx)">Gracias a cada cliente que pasó por el mostrador, nos escribió o armó su pedido en la web. Diciembre lo arrancamos con todo.</p>
<div class="abs" style="left:72px;right:72px;top:860px;display:grid;grid-template-columns:1fr 1fr;gap:18px">
<div style="background:var(--az);color:#fff;padding:30px"><div class="C" style="font-size:24px;letter-spacing:.18em;color:var(--ce)">RESEÑAS</div><div class="C" style="font-size:44px;margin-top:10px;line-height:1.05">Contanos cómo te fue en Google</div></div>
<div style="background:var(--wa);color:#fff;padding:30px"><div class="C" style="font-size:24px;letter-spacing:.18em">COMUNIDAD</div><div class="C" style="font-size:44px;margin-top:10px;line-height:1.05">Sumate al grupo de WhatsApp</div></div></div>
<div class="abs C" style="left:72px;bottom:70px;font-size:26px;letter-spacing:.18em;color:var(--az)">CALLE 38 4335 · VILLA LYNCH · SAN MARTÍN</div>
</section>'''

# ====================================================================== CARRUSELES: piezas genéricas
def barras(i, T):
    return ''.join(f'<i class="{"on" if k == i else ""}"></i>' for k in range(1, T + 1))

def cp(T, titulo, sub, prods, tam=104, rotulo='Consejo de ferretero', tag='GUÍA', calado=''):
    imgs = ''.join(f'<img class="prod" src="{r(P[p])}" style="--rot:{a}deg;left:{x}px;top:{y}px;width:{w}px" alt="">' for p, x, y, w, a in prods)
    return f'''<section class="post ne">{marcas()}
{rafaga(380, 210, 700, 760, n=12, color='var(--az)', delay=0)}
{f'<div class="abs calado" style="right:-20px;top:120px;font-size:520px;color:rgba(154,174,255,.32)">{calado}</div>' if calado else ''}
<div class="meta"><img src="{LBL}" alt="Masherr"><span style="color:var(--ce)">{tag} · 01/{T:02d}</span></div>
{imgs}
<div class="abs" style="left:72px;top:690px"><div class="rot" style="color:var(--ce)">{rotulo}</div></div>
<div class="abs C" style="left:72px;right:72px;top:750px;font-size:{tam}px;line-height:.98">{titulo}</div>
<p class="abs" style="left:72px;right:240px;top:1110px;font-size:30px;line-height:1.4;color:#C9CDDA">{sub}</p>
<div class="desliza" style="color:var(--ce)">DESLIZÁ<b></b></div><div class="pag" style="color:var(--ce)">01 / {T:02d}</div>
</section>'''

def ct(i, T, num, tag, titulo, txt, fondo='bl', extra='', rot_txt=None):
    """Placa de texto (sin producto): número calado gigante, título y bajada."""
    oscuro = fondo in ('az', 'ne')
    c1 = 'var(--ce)' if oscuro else 'var(--az)'
    return f'''<section class="post {fondo}">{marcas()}
{rafaga(560, 120, 520, 520, n=9, color='rgba(255,255,255,.08)' if oscuro else 'var(--gr2)', delay=0)}
<div class="abs calado" style="left:40px;top:190px;font-size:480px;color:{'rgba(154,174,255,.4)' if oscuro else 'var(--gr2)'};-webkit-text-stroke-width:5px">{num}</div>
<div class="meta"><img src="{LBL if oscuro else LAZ}" alt="Masherr"><span style="color:{c1}">{tag}</span></div>
<div class="barras" style="color:{c1}">{barras(i, T)}</div>
<div class="abs" style="left:72px;top:620px"><div class="rot" style="color:{c1}">{rot_txt or "Paso " + num}</div></div>
<div class="abs C" style="left:72px;right:72px;top:690px;font-size:92px;line-height:1">{titulo}</div>
<p class="abs" style="left:72px;right:120px;top:{960 if titulo.count('<br>') < 2 else 1010}px;font-size:36px;line-height:1.42;color:{'#C9CDDA' if oscuro else 'var(--tx)'}">{txt}</p>
{extra}
<div class="desliza" style="color:{c1}">DESLIZÁ<b></b></div><div class="pag" style="color:{c1}">{i:02d} / {T:02d}</div>
</section>'''

def cpaso(i, T, num, tag, titulo, nombre, txt, prod, rot=-6):
    return c_paso(i, T, num, tag, titulo, nombre, txt, prod, 0, rot, 0, 0, 'bl' if i % 2 else 'gr')

def ccap(i, T, num, titulo, txt, img):
    """Placa con captura real de la web dentro de un celular."""
    return f'''<section class="post {'bl' if i % 2 else 'gr'}">
<div class="abs" style="right:0;top:0;width:520px;height:1350px;background:var(--az)"></div>
{rafaga(560, 160, 520, 1030, n=16, color='rgba(255,255,255,.07)', delay=0)}
<div class="meta"><img src="{LAZ}" alt="Masherr"><span style="color:#fff">COMPRÁ ONLINE</span></div>
<div class="barras" style="color:var(--az);right:560px">{barras(i, T)}</div>
<div class="abs" style="right:70px;top:190px;width:420px;height:900px;transform:rotate(4deg);border-radius:56px;background:#000;padding:16px;box-shadow:0 50px 80px rgba(0,0,0,.45)">
<img src="{CAP}{img}" style="width:100%;height:100%;object-fit:cover;object-position:top;border-radius:42px" alt=""></div>
<div class="abs calado" style="left:50px;top:220px;font-size:300px;color:var(--gr2);-webkit-text-stroke-width:5px">{num}</div>
<div class="abs" style="left:72px;right:580px;top:560px"><div class="rot" style="color:var(--az);font-size:24px">Paso {num}</div>
<div class="C" style="font-size:72px;line-height:1;margin-top:20px">{titulo}</div>
<p style="font-size:30px;line-height:1.42;color:var(--tx);margin-top:24px">{txt}</p></div>
<div class="desliza" style="color:var(--az)">DESLIZÁ<b></b></div><div class="pag" style="color:#fff">{i:02d} / {T:02d}</div>
</section>'''

def cduo(i, T, tag, a, b):
    """Dos marcas por placa: (clave producto, marca, línea)."""
    def bloque(k, d):
        prod, marca_, linea = d
        top = 170 + k * 590
        return f'''<div class="abs" style="left:0;right:0;top:{top}px;height:560px;background:{'#fff' if k == 0 else 'var(--gr)'}"></div>
<img class="prod" src="{r(P[prod])}" style="--rot:{-6 if k == 0 else 5}deg;left:{560}px;top:{top + 40}px;width:440px;max-height:480px;object-fit:contain" alt="">
<div class="abs" style="left:72px;top:{top + 150}px;width:470px"><div class="C" style="font-size:96px;line-height:.95;color:var(--az)">{marca_}</div>
<p style="font-size:30px;line-height:1.4;color:var(--tx);margin-top:16px">{linea}</p></div>'''
    return f'''<section class="post gr">
<div class="meta"><img src="{LAZ}" alt="Masherr"><span style="color:var(--az)">{tag}</span></div>
<div class="barras" style="color:var(--az)">{barras(i, T)}</div>
{bloque(0, a)}{bloque(1, b)}
<div class="desliza" style="color:var(--az)">DESLIZÁ<b></b></div><div class="pag" style="color:var(--az)">{i:02d} / {T:02d}</div>
</section>'''

def cc(T, titulo, rotulo='¿No sabés cuál?', calado='?', chips=None, extra=''):
    chips = chips or [f'<span class="chip wa">{WA}WhatsApp 11 3182-6166</span>', f'<span class="chip blanco">{WEB}masherrferreteria.com.ar</span>']
    return f'''<section class="post az">{marcas()}
{rafaga(0, 820, 1080, 530, n=10, color='rgba(255,255,255,.09)', delay=0, origen='left')}
<div class="meta"><img src="{LBL}" alt="Masherr"><span style="color:var(--ce)">{T:02d} / {T:02d}</span></div>
<div class="abs calado" style="right:-30px;top:120px;font-size:520px;color:rgba(154,174,255,.35)">{calado}</div>
<div class="abs" style="left:72px;top:300px"><div class="rot" style="color:var(--ce)">{rotulo}</div></div>
<div class="abs C" style="left:72px;right:72px;top:370px;font-size:104px;line-height:1">{titulo}</div>
<div class="abs" style="left:72px;top:820px;display:flex;flex-direction:column;gap:20px;align-items:flex-start">{''.join(chips)}</div>
{extra}
<div class="pag" style="color:var(--ce);left:72px;right:auto">CALLE 38 4335 · VILLA LYNCH</div>
</section>'''

QR_CIERRE = '''<div class="abs" style="right:72px;top:800px;background:#fff;padding:18px;border-radius:18px;text-align:center">
<img src="../capturas/qr_resenas.png" style="width:240px;height:240px;display:block" alt="QR reseñas"><div class="C" style="font-size:22px;letter-spacing:.12em;color:var(--az);margin-top:8px">ESCANEÁ</div></div>'''
CHIP_COM = [f'<span class="chip wa">{WA}Comunidad Masherr</span>', '<span class="chip blanco" style="font-size:28px">masherrferreteria.com.ar/comunidad</span>']

# ====================================================================== CARRUSELES DEL MES
def k_comunidad():
    T = 5
    return [cp(T, 'Sumate a la<br>Comunidad<br>Masherr.', 'Descuentos, promos, rifas y mucho más, en nuestro grupo de WhatsApp. Es gratis.', [], 112, 'Nuevo', 'COMUNIDAD', '%'),
            ct(2, T, '01', 'DESCUENTOS', 'Beneficios<br>del grupo.', 'Descuentos exclusivos para los que están en la comunidad.', 'bl'),
            ct(3, T, '02', 'PROMOS Y RIFAS', 'Promos y<br>rifas.', 'Ofertas de la semana, novedades antes que nadie y sorteos entre los miembros.', 'gr'),
            ct(4, T, '03', 'CÓMO SUMARTE', 'Entrás con<br>un toque.', 'Tocá el link de la bio o de nuestras historias, unite al grupo y listo: te llega todo por WhatsApp.', 'bl'),
            cc(T, 'Es gratis.<br>Sumate hoy.', 'Comunidad Masherr', '+', CHIP_COM)]

def k_taladros():
    T = 5
    return [cp(T, '¿Percutor,<br>atornillador o<br>rotomartillo?', 'Tres máquinas que parecen iguales y no lo son. Guardá esta guía.',
               [('percutor', 470, 200, 330, -12), ('atornillador', 760, 170, 260, 10), ('rotomartillo', 560, 420, 380, -6)], 98),
            cpaso(2, T, '01', 'PERCUTOR', 'Ladrillo,<br>madera<br>y metal', 'Taladro percutor', 'Con percusión para ladrillo y mampostería; sin percusión para madera y metal. El más versátil para la casa.', 'percutor'),
            cpaso(3, T, '02', 'ATORNILLADOR', 'Armar y<br>atornillar', 'Atornillador a batería', 'Liviano y sin cable: muebles, durlock, bisagras y agujeros chicos en madera y metal.', 'atornillador', 6),
            cpaso(4, T, '03', 'ROTOMARTILLO', 'Hormigón<br>y picado', 'Rotomartillo SDS Plus', 'Perfora hormigón sin esfuerzo y, con cincel, pica revoque y cerámica.', 'rotomartillo'),
            cc(T, 'Contanos qué<br>vas a agujerear.<br>Te decimos cuál.')]

def k_resenas_como():
    T = 5
    return [cp(T, '¿Te atendimos<br>bien? Contalo<br>en Google.', 'Tu opinión ayuda a que más vecinos nos encuentren. Te mostramos cómo dejarla en 1 minuto.', [], 100, 'Reseñas', 'RESEÑAS', '★'),
            ct(2, T, '01', 'ABRÍ GOOGLE MAPS', 'Buscanos.', 'Buscá “Ferretería Industrial Masherr” en Google Maps o escaneá el QR que tenemos en el mostrador.', 'bl'),
            ct(3, T, '02', 'ESTRELLAS', 'Elegí las<br>estrellas.', 'Tocá “Escribir una opinión” y puntuá de 1 a 5.', 'gr',
               f'<div class="abs" style="left:72px;top:1080px;display:flex;gap:12px">{estrellas(72, "var(--az)")}</div>'),
            ct(4, T, '03', 'TU EXPERIENCIA', 'Contanos<br>cómo te fue.', 'Qué compraste y cómo te atendimos. Las leemos todas.', 'bl'),
            cc(T, 'Gracias por<br>tu reseña.', 'Somos 4,7 ★ · 131 opiniones', '★',
               [f'<span class="chip blanco">Escaneá el QR →</span>'], QR_CIERRE)]

def k_comprar_web():
    T = 6
    return [cp(T, 'Comprá desde<br>el celular<br>en 4 pasos.', 'Armá el pedido en la web y lo cerramos por WhatsApp: te confirmamos precio, stock y retiro.',
               [('kit', 520, 190, 500, -6)], 104, 'Compra online', 'TUTORIAL'),
            ccap(2, T, '01', 'Entrá a<br>la web.', 'masherrferreteria.com.ar: está en el link de la bio.', 'web_1_inicio.png'),
            ccap(3, T, '02', 'Buscá lo que<br>necesitás.', 'Por producto, marca o categoría.', 'web_2_tienda.png'),
            ccap(4, T, '03', 'Agregalo al<br>carrito.', 'Elegí la cantidad y seguí comprando.', 'web_3_producto.png'),
            ccap(5, T, '04', 'Envialo por<br>WhatsApp.', 'Completá tu nombre y el pedido llega armado a nuestro WhatsApp.', 'web_4_carrito.png'),
            cc(T, 'Te respondemos<br>con precio,<br>stock y retiro.', 'Así de fácil', '✓')]

def k_casa():
    T = 7
    return [cp(T, '5 herramientas<br>que no pueden<br>faltar en casa.', 'Para los arreglos de todos los días. ¿Cuántas tenés?',
               [('taladro12', 470, 170, 300, -10), ('destornilladores', 760, 200, 250, 8), ('cinta', 560, 430, 230, -14), ('pinza', 820, 420, 170, 20)], 100, 'Lo básico', 'CASA'),
            cpaso(2, T, '01', 'ATORNILLAR', 'Destorni-<br>lladores', 'Juego planos y Phillips', 'La punta justa evita pelar el tornillo. Un juego cubre casi todo en casa.', 'destornilladores'),
            cpaso(3, T, '02', 'AJUSTAR', 'Pinza pico<br>de loro', 'Pinza regulable', 'Canillas, sifones y tuercas: se adapta a distintas medidas.', 'pinza', 20),
            cpaso(4, T, '03', 'MEDIR', 'Cinta<br>métrica', 'Cinta de 5 metros', 'Para muebles, cortinas y compras: medí antes de comprar.', 'cinta'),
            cpaso(5, T, '04', 'NIVELAR', 'Nivel de<br>burbuja', 'Nivel de 40 cm', 'Estantes y cuadros derechos a la primera.', 'nivel', -16),
            cpaso(6, T, '05', 'AGUJEREAR', 'Taladro<br>atornillador', 'Atornillador a batería 12 V', 'Sin cable, liviano y con carga para varios trabajos.', 'taladro12'),
            cc(T, '¿Te falta<br>alguna?<br>La tenemos.', 'Armá tu caja')]

def k_amoladoras():
    T = 5
    return [cp(T, 'Amoladora:<br>¿115 o 180?', 'El tamaño del disco cambia todo: profundidad de corte, potencia y control.',
               [('amo115', 470, 200, 440, -10), ('amo180', 520, 430, 520, 6)], 116),
            cpaso(2, T, '01', '115 MM', 'Cortes finos y<br>terminación', 'Amoladora de 115 mm', 'Liviana y precisa: corte de perfiles, chapa, cerámica y terminaciones. Se usa con una mano y la empuñadura.', 'amo115'),
            cpaso(3, T, '02', '180 MM', 'Cortes<br>profundos y<br>desbaste', 'Amoladora de 180 mm', 'Más potencia y diámetro: cortes profundos y desbaste pesado. Para uso de taller e industria.', 'amo180', 4),
            ct(4, T, '03', 'SEGURIDAD', 'Siempre<br>protegido.', 'Usá la protección del disco, la empuñadura lateral, anteojos y guantes. Y el disco correcto para cada material.', 'ne'),
            cc(T, 'Contanos qué<br>vas a cortar.<br>Te asesoramos.')]

def k_soldadoras():
    T = 6
    return [cp(T, 'Soldadora<br>inverter:<br>¿cuál elegir?', 'Más amperes, más espesor y trabajo continuo. Te ayudamos a elegir.',
               [('sold140', 460, 200, 260, -8), ('sold190', 720, 220, 280, 6), ('mascara', 600, 420, 230, -10)], 100),
            cpaso(2, T, '01', 'PARA EMPEZAR', 'Arreglos<br>en casa', 'Soldadora SI 140', 'Para arreglos y herrería liviana: rejas, soportes y reparaciones.', 'sold140'),
            cpaso(3, T, '02', 'HERRERÍA', 'Trabajo<br>frecuente', 'Soldadora SI 160 PRO', 'Más amperaje para espesores mayores y uso más seguido.', 'sold160'),
            cpaso(4, T, '03', 'TALLER', 'Uso<br>intensivo', 'Soldadora SI 190 PRO', 'Para el taller: más potencia y electrodos más gruesos.', 'sold190'),
            cpaso(5, T, '04', 'PROTECCIÓN', 'Máscara<br>fotosensible', 'Máscara automática', 'Se oscurece sola al encender el arco: ves la pieza antes y durante la soldadura.', 'mascara', 4),
            cc(T, 'Contanos qué<br>vas a soldar.<br>Te asesoramos.')]

def k_brocas():
    T = 5
    return [cp(T, '¿Qué broca<br>uso para cada<br>material?', 'La broca equivocada no avanza, se quema o rompe la pieza. Guardá esta guía.',
               [('mechas', 450, 200, 560, -6), ('copa', 620, 450, 260, -16)], 100),
            cpaso(2, T, '01', 'METAL · MADERA · LADRILLO', 'Un juego<br>para los<br>tres', 'Juego de mechas', 'Acero rápido para metal, punta de centrado para madera y widia para ladrillo (con percutor).', 'mechas'),
            cpaso(3, T, '02', 'HORMIGÓN', 'Hormigón<br>armado', 'Rotomartillo + broca SDS', 'Con rotomartillo: perfora hormigón sin esfuerzo y sin forzar la máquina.', 'rotomartillo'),
            cpaso(4, T, '03', 'CERÁMICA', 'Cerámica y<br>porcelanato', 'Diamantada en seco', 'Agujeros limpios sin rajar la pieza. Ideal para griferías y caños.', 'copa', -14),
            cc(T, 'Contanos qué<br>vas a perforar.<br>Te decimos cuál.')]

def k_orden():
    T = 6
    return [cp(T, 'Cada cosa<br>en su lugar.', 'Cajas, bolsos y carros para el taller, la obra o la casa.',
               [('caja_stanley', 450, 230, 380, -8), ('packout', 790, 170, 230, 6), ('bolso', 520, 470, 340, 6)], 112, 'Orden', 'TALLER'),
            cpaso(2, T, '01', 'PARA LLEVAR', 'Bolso de<br>herramientas', 'Bolso reforzado', 'Boca ancha y bolsillos: ideal para el trabajo diario.', 'bolso'),
            cpaso(3, T, '02', 'LIVIANA', 'Caja<br>plástica', 'Caja de 19"', 'Con bandeja interna: liviana y resistente.', 'caja_stanley'),
            cpaso(4, T, '03', 'RESISTENTE', 'Caja<br>metálica', 'Caja metálica', 'Para el taller: aguanta peso y uso pesado.', 'caja_lara'),
            cpaso(5, T, '04', 'MODULAR', 'Carro<br>modular', 'Sistema Packout', 'Se apila, se separa y se mueve con ruedas.', 'packout', 4),
            cc(T, '¿Cuál va con<br>tu forma de<br>trabajar?', 'Te asesoramos')]

def k_porque():
    T = 5
    return [cp(T, '4,7 ★<br>en Google.', '131 clientes nos dejaron su opinión. Esto es lo que más destacan.', [], 150, 'Reseñas', 'RESEÑAS', '★'),
            ct(2, T, '“', 'LO QUE DICEN', 'Se tomaron el<br>tiempo.', '“Se tomaron el tiempo para buscar la que yo necesitaba.” — Lorena, reseña en Google.', 'az', rot_txt='Reseña real'),
            ct(3, T, '01', 'ASESORAMIENTO', 'Te preguntamos<br>antes de vender.', 'Qué vas a hacer, con qué material y cada cuánto. Así te llevás lo justo.', 'bl'),
            ct(4, T, '02', 'VARIEDAD', 'Más de 40<br>marcas.', 'Para industria, talleres, mantenimiento, obra y casa.', 'gr'),
            cc(T, '¿Ya nos<br>conocés?<br>Dejanos tu<br>reseña.', 'Escaneá el QR', '★', [f'<span class="chip blanco">Escaneá el QR →</span>'], QR_CIERRE)]

def k_marcas():
    T = 5
    return [cp(T, 'Marcas que<br>trabajamos.', 'Primeras marcas para cada trabajo, con asesoramiento en el mostrador.',
               [('bosch_amo', 450, 200, 380, -8), ('karcher', 800, 170, 220, 6), ('bahco', 520, 470, 400, -10)], 116, 'Marcas', 'MARCAS'),
            cduo(2, T, 'MARCAS', ('percutor', 'Bosch', 'Taladros, amoladoras y atornilladores.'), ('amo115', 'DeWalt', 'Amoladoras, rotomartillos y sierras.')),
            cduo(3, T, 'MARCAS', ('cinta', 'Stanley', 'Medición, cajas y herramientas de mano.'), ('packout', 'Milwaukee', 'Almacenamiento modular Packout.')),
            cduo(4, T, 'MARCAS', ('karcher', 'Kärcher', 'Hidrolavadoras y limpieza.'), ('bahco', 'Bahco', 'Pinzas y herramientas de mano.')),
            cc(T, 'Y muchas<br>más. Consultá<br>la tuya.', 'Más de 40 marcas')]

def k_limpieza():
    T = 5
    return [cp(T, 'Llega el<br>verano: dejá<br>todo limpio.', 'Hidrolavadoras y aspiradoras para la casa, el auto y el taller.',
               [('karcher', 470, 170, 300, -8), ('hidro_neb', 780, 180, 210, 6), ('aspi_neb', 600, 380, 260, -4)], 100, 'Temporada', 'VERANO'),
            cpaso(2, T, '01', 'CASA Y AUTO', 'Hidrolavadora<br>hogareña', 'Hidrolavadora 120 bar', 'Patios, veredas, autos y muebles de jardín.', 'karcher', 4),
            cpaso(3, T, '02', 'MÁS PRESIÓN', 'Trabajos<br>exigentes', 'Hidrolavadora 160 bar', 'Más presión para superficies difíciles y uso frecuente.', 'hidro_neb', 4),
            cpaso(4, T, '03', 'SÓLIDOS Y LÍQUIDOS', 'Aspiradora<br>de taller', 'Aspiradora de 40 litros', 'Para el taller, la obra y el auto: aspira sólidos y líquidos.', 'aspi_neb', 0),
            cc(T, '¿Cuál te<br>conviene?<br>Consultanos.')]

def k_inalambricas():
    T = 5
    return [cp(T, 'Una batería.<br>Varias<br>máquinas.', 'Línea One-Power 20 V: menos cables y más libertad en la obra.',
               [('amo20v', 450, 200, 380, -8), ('caladora20v', 780, 170, 230, 6), ('sierra20v', 620, 400, 190, -12)], 108, 'Inalámbricas', '20 V'),
            cpaso(2, T, '01', 'CORTE', 'Amoladora<br>a batería', 'Amoladora 115 mm 20 V', 'Brushless: corte y desbaste sin buscar un enchufe.', 'amo20v'),
            cpaso(3, T, '02', 'CURVAS', 'Sierra<br>caladora', 'Caladora 20 V', 'Cortes rectos y curvos en madera, melamina y chapa fina.', 'caladora20v', 4),
            cpaso(4, T, '03', 'PODA', 'Sierra<br>de mano', 'Sierra de mano 5" 20 V', 'Para poda y ramas en el jardín, liviana y a batería.', 'sierra20v', 0),
            cc(T, 'Armá tu<br>equipo de<br>a poco.', 'Una batería para todas')]

# ====================================================================== CALENDARIO
DIAS = ['LUNES', 'MARTES', 'MIÉRCOLES', 'JUEVES', 'VIERNES', 'SÁBADO', 'DOMINGO']
# fecha: (carrusel nombre, función, compartir carrusel (título, prod|None, tag/grande), posteo nombre, html, compartir posteo, copys)
PLAN = {
 16: ('Comunidad Masherr', k_comunidad, (['Sumate a la', 'comunidad.'], None, '%'), 'Comunidad Masherr', p_comunidad(1), (['Comunidad', 'Masherr.'], None, '%')),
 17: ('Guia de discos', carrusel_discos, (['¿Qué disco', 'va con cada', 'trabajo?'], 'corte', -10), 'Web nueva', p_web(), (['Toda la', 'ferretería en', 'tu celular.'], None, '@')),
 18: ('Percutor atornillador o rotomartillo', k_taladros, (['¿Percutor o', 'rotomartillo?'], 'rotomartillo', -6), 'Producto de la semana', p_kit(), (['Producto', 'de la', 'semana.'], 'kit', -4)),
 19: ('Como medir bien', carrusel_medicion, (['Medí una vez.', 'Cortá una', 'sola vez.'], 'cinta', -10), 'Medidor laser', p_producto('medidor', 'PRODUCTO DESTACADO', 'EMTOP · 40 METROS', 'Medidor de<br>distancia láser', '40m', ancho=300, x=390, y=150, rot=-6), (['Medí sin', 'ayuda.'], 'medidor', -6)),
 20: ('Como dejarnos una resena', k_resenas_como, (['¿Te atendimos', 'bien?'], None, '★'), 'Resena', p_resena(), 'resenas'),
 21: ('Como comprar en la web', k_comprar_web, (['Comprá desde', 'el celular.'], None, '@'), 'Como comprar', p_comprar(), (['Armá el', 'pedido.'], None, '✓')),
 22: ('5 herramientas para la casa', k_casa, (['5 que no', 'pueden faltar.'], 'destornilladores', 6), 'Ya estas en la comunidad', p_comunidad(2), (['¿Ya estás en', 'la comunidad?'], None, '?')),
 23: ('Amoladora 115 o 180', k_amoladoras, (['Amoladora:', '¿115 o 180?'], 'amo180', 6), 'Amoladora DeWalt 115', p_producto('amo115', 'PRODUCTO DESTACADO', 'DEWALT · 800 W', 'Amoladora<br>angular 115 mm', '115', ancho=860, x=110, y=250, rot=-6), (['Producto', 'destacado.'], 'amo115', -6)),
 24: ('Soldadoras inverter', k_soldadoras, (['¿Qué soldadora', 'elijo?'], 'sold160', -6), '4,7 en Google', p_resenas_47(), 'resenas'),
 25: ('Que broca usar', k_brocas, (['¿Qué broca', 'uso?'], 'mechas', -6), 'Rotomartillo DeWalt', p_producto('rotomartillo', 'PRODUCTO DESTACADO', 'DEWALT · SDS PLUS', 'Rotomartillo<br>SDS Plus 800 W', 'SDS', ancho=640, x=230, y=170, rot=-6), (['Producto', 'destacado.'], 'rotomartillo', -6)),
 26: ('Orden en el taller', k_orden, (['Cada cosa en', 'su lugar.'], 'packout', 6), 'Pedidos para empresas', p_empresas(), (['¿Comprás para', 'tu empresa?'], None, '$')),
 27: ('Por que nos eligen', k_porque, (['4,7 ★', 'en Google.'], None, '★'), 'Hidrolavadora Karcher', p_producto('karcher', 'TEMPORADA DE VERANO', 'KÄRCHER · K3', 'Hidrolavadora<br>120 bar', 'K3', ancho=520, x=300, y=150, rot=-4), (['Llega el', 'verano.'], 'karcher', -4)),
 28: ('Marcas que trabajamos', k_marcas, (['Marcas que', 'trabajamos.'], 'bosch_amo', -8), 'Soldadora Pegaso 160', p_producto('sold160', 'PRODUCTO DESTACADO', 'PEGASO · INVERTER', 'Soldadora<br>SI 160 PRO', '160', ancho=560, x=260, y=150, rot=-4), (['Producto', 'destacado.'], 'sold160', -4)),
 29: ('Limpieza para el verano', k_limpieza, (['Dejá todo', 'limpio.'], 'karcher', -4), 'Comunidad Masherr 2', p_comunidad(1), (['Sumate a la', 'comunidad.'], None, '%')),
 30: ('Inalambricas 20V', k_inalambricas, (['Una batería,', 'varias máquinas.'], 'amo20v', -8), 'Gracias noviembre', p_gracias(), (['Gracias,', 'noviembre.'], None, '♥')),
}

def compartir(D, datos, tag):
    if datos == 'resenas':
        return h_resenas_compartir(*D)
    titulo, prod, extra = datos
    if prod:
        return h_compartir(*D, titulo, prod, extra, 680, 990, tag)
    return h_compartir_texto(*D, titulo, tag, extra, 'az')

import datetime
CAL = []
for n in range(16, 31):
    f = datetime.date(2026, 11, n)
    dn = DIAS[f.weekday()]
    D = (dn, f'{n:02d}.11')
    sab, dom = f.weekday() == 5, f.weekday() == 6
    knom, kfun, kcomp, pnom, phtml, pcomp = PLAN[n]
    hc_k = compartir(D, kcomp, 'Nuevo carrusel')
    hc_p = compartir(D, pcomp, 'Nuevo posteo')
    com = h_comunidad(*D, 1 if n % 2 == 0 else 2)
    if dom:
        h = [('10.00 Domingo', h_domingo(*D)), ('11.05 Compartir carrusel', hc_k), ('19.05 Compartir posteo', hc_p), ('20.00 Comunidad', com)]
        hk, hp = '11.00', '19.00'
    elif sab:
        h = [('08.00 Abrimos', h_abrimos(*D, sab=True)), ('09.30 Comunidad', com), ('10.05 Compartir posteo', hc_p),
             ('11.35 Compartir carrusel', hc_k), ('12.30 Cerramos', h_cierre(*D, sab=True))]
        hk, hp = '11.30', '10.00'
    else:
        h = [('08.00 Abrimos', h_abrimos(*D)), ('10.00 Comunidad', com), ('12.00 Mediodia', h_mediodia(*D)), ('13.05 Compartir carrusel', hc_k),
             ('14.00 Volvimos', h_volvimos(*D)), ('17.00 Cerramos', h_cierre(*D)), ('19.05 Compartir posteo', hc_p)]
        hk, hp = '13.00', '19.00'
    piezas = [('historia', f'{k + 1} - {t}', html) for k, (t, html) in enumerate(h)]
    piezas.append(('posteo', f'Posteo {hp} - {pnom}', phtml))
    piezas += [('carrusel', f'Carrusel {hk} - {knom}/{i:02d}', s) for i, s in enumerate(kfun(), 1)]
    CAL.append({'n': n, 'fecha': f.isoformat(), 'dia': dn, 'carpeta': f'{n - 15:02d} - {dn.title()} {n}', 'piezas': piezas})

if __name__ == '__main__':
    man = []
    for d in CAL:
        base = AQUI / d['fecha']; base.mkdir(exist_ok=True)
        for tipo, nombre, html in d['piezas']:
            archivo = f"{tipo}__{nombre.replace('/', '__').replace(' ', '_')}.html"
            (base / archivo).write_text(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{html}</body></html>')
            man.append({'dia': d['fecha'], 'carpeta': d['carpeta'], 'tipo': tipo, 'nombre': nombre, 'html': f"{d['fecha']}/{archivo}"})
    (AQUI / 'manifiesto_mes.json').write_text(json.dumps(man, ensure_ascii=False, indent=1))
    from collections import Counter
    print(len(man), 'piezas', Counter(m['tipo'] for m in man))
