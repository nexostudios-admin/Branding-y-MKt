"""Imágenes 1200x900 para las publicaciones de la ficha de Google (Perfil de Empresa). Uso: python3 gbp.py && node exportar_gbp.js"""
from mes import AQUI, CSS, P, r, LAZ, LBL, WA, WEB, STAR, rafaga, marcas
CSS2 = CSS + '.gbp{width:1200px;height:900px}'
def g(fondo, rot, titulo, sub, prods, chip, calado='', tam=80):
    osc = fondo in ('az', 'ne')
    c1 = 'var(--ce)' if osc else 'var(--az)'
    imgs = ''.join(f'<img class="prod" src="{r(P[p])}" style="--rot:{a}deg;left:{x}px;top:{y}px;width:{w}px" alt="">' for p, x, y, w, a in prods)
    return f'''<section class="gbp {fondo}">{marcas()}
{rafaga(560, 90, 640, 720, n=12, color='var(--az)' if fondo == 'ne' else ('rgba(255,255,255,.09)' if osc else 'var(--gr2)'), delay=0)}
{f'<div class="abs calado" style="right:30px;top:60px;font-size:560px;color:{"rgba(154,174,255,.32)" if osc else "var(--gr2)"}">{calado}</div>' if calado else ''}
<img class="abs" src="{LBL if osc else LAZ}" style="left:80px;top:80px;height:64px" alt="Masherr">
{imgs}
<div class="abs" style="left:80px;top:250px;width:560px"><div class="rot" style="color:{c1}">{rot}</div>
<div class="C" style="font-size:{tam}px;line-height:1;margin-top:22px">{titulo}</div>
<p style="font-size:28px;line-height:1.42;margin-top:22px;color:{'#C9CDDA' if osc else 'var(--tx)'}">{sub}</p></div>
<div class="abs" style="left:80px;bottom:80px"><span class="chip {'wa' if 'WhatsApp' in chip else ('blanco' if osc else 'azul')}" style="font-size:30px">{WA if 'WhatsApp' in chip else WEB}{chip}</span></div>
<div class="abs C" style="right:80px;bottom:92px;font-size:22px;letter-spacing:.18em;color:{c1}">VILLA LYNCH · SAN MARTÍN</div>
</section>'''
GBP = [
 ('01 - Semana 1 - Guia de discos', g('ne', 'Consejo de ferretero', '¿Qué disco va<br>con cada trabajo?', 'Corte, desbaste, terminación y perforación: te asesoramos en el mostrador o por WhatsApp.', [('corte', 700, 170, 380, -10), ('flap40', 880, 400, 260, 12), ('copa', 690, 520, 200, -18)], 'Consultá por WhatsApp')),
 ('02 - Semana 1 - Comunidad', g('az', 'Comunidad Masherr', 'Descuentos.<br>Promos.<br>Rifas.', 'Sumate gratis a nuestro grupo de WhatsApp y enterate antes que nadie.', [], 'Unite por WhatsApp', '%')),
 ('03 - Semana 2 - Amoladoras', g('gr', 'Amoladoras', '¿115 o 180?<br>Te ayudamos<br>a elegir.', 'Bosch, DeWalt, Nebraska y más, en Villa Lynch.', [('amo115', 640, 170, 480, -8), ('amo180', 660, 430, 500, 6)], 'Consultá por WhatsApp')),
 ('04 - Semana 2 - Compra online', g('bl', 'Comprá online', 'Armá el pedido.<br>Lo cerramos<br>por WhatsApp.', 'Elegí en la web, envialo y te confirmamos precio, stock y retiro.', [('kit', 650, 200, 500, -6)], 'masherrferreteria.com.ar', tam=66)),
 ('05 - Semana 3 - Soldadoras', g('ne', 'Soldadura', 'Soldadoras<br>inverter.', 'Para arreglos en casa, herrería y uso intensivo en el taller. Máscaras fotosensibles.', [('sold140', 640, 210, 260, -8), ('sold190', 880, 230, 270, 6), ('mascara', 770, 470, 220, -10)], 'Consultá por WhatsApp')),
 ('06 - Semana 3 - Empresas', g('az', 'Empresas y talleres', '¿Comprás para<br>tu empresa?<br>Te cotizamos.', 'Mandanos la lista y te respondemos con la cotización.', [('packout', 820, 170, 280, 6)], 'Pedí cotización por WhatsApp', tam=64)),
 ('07 - Semana 4 - Hidrolavadoras', g('gr', 'Llega el verano', 'Dejá todo<br>limpio.', 'Hidrolavadoras y aspiradoras de sólidos y líquidos para la casa, el auto y el taller.', [('karcher', 660, 180, 300, -6), ('hidro_neb', 930, 200, 200, 6), ('aspi_neb', 780, 420, 240, -4)], 'Consultá por WhatsApp')),
 ('08 - Semana 4 - Resenas', g('ne', 'Gracias', '4,7 ★<br>en Google.', '131 clientes nos dejaron su opinión. ¿Te atendimos bien? Contalo en Google.', [], 'masherrferreteria.com.ar', '★')),
]
if __name__ == '__main__':
    import json
    d = AQUI / 'gbp'; d.mkdir(exist_ok=True)
    for n, h in GBP:
        (d / f'{n}.html').write_text(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS2}</style></head><body>{h}</body></html>')
    print(len(GBP))
