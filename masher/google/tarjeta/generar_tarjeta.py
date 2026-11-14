"""Tarjeta de contacto Masherr 90x50 mm (+7 mm de sangrado), rearmada a partir del diseño original
con el dominio corregido (masherrferreteria.com.ar). Uso: python3 generar_tarjeta.py && node ../resenas/exportar.js no: ver exportar_tarjeta.js
"""
from pathlib import Path
AQUI = Path(__file__).parent
F = '../../catalogo/fonts/'
AZ = '#7C9ED8'
# Medidas tomadas del original (1400 px = 90 mm). px -> mm dentro del área de corte.
mm = lambda px: round(px * 90 / 1400, 2)

ICONOS = {
 'tel': f'<svg viewBox="0 0 24 24" fill="none" stroke="{AZ}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M8.2 7.2c.4-.4 1-.3 1.3.1l1.1 1.6c.3.4.2.9-.1 1.2l-.7.6c.6 1.3 1.7 2.4 3 3l.6-.7c.3-.3.8-.4 1.2-.1l1.6 1.1c.4.3.5.9.1 1.3l-.7.7c-.6.6-1.5.8-2.3.4-2.5-1.1-4.5-3.1-5.6-5.6-.3-.8-.2-1.7.4-2.3z"/></svg>',
 'ig': f'<svg viewBox="0 0 24 24" fill="none" stroke="{AZ}" stroke-width="1.5"><rect x="4" y="4" width="16" height="16" rx="3.5"/><circle cx="12" cy="12" r="3.6"/><circle cx="16.6" cy="7.4" r=".6" fill="{AZ}"/></svg>',
 'tk': f'<svg viewBox="0 0 24 24" fill="none" stroke="{AZ}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12.5 2.5v13a3.6 3.6 0 1 1-3.6-3.6"/><path d="M12.5 2.5c.5 2.8 2.4 4.6 5.2 4.8"/></svg>',
}
COLS = [('tel', 'LÍNEA', '4752-5210', 2.4), ('tel', 'WHATSAPP', '11-3182-6166', 2.4),
        ('ig', 'INSTAGRAM', '@masherrferreteria', 1.72), ('tk', 'TIKTOK', 'Masherr', 2.4)]

def col(i, ic, rot, dato, tam):
    x = 7 + mm(40) + i * mm(329.3)
    return f'''<div class="col" style="left:{x}mm;width:{mm(329.3)}mm">
<div class="ic">{ICONOS[ic]}</div><div class="rot">{rot}</div><div class="dato" style="font-size:{tam}mm">{dato}</div></div>'''

seps = ''.join(f'<div class="v" style="left:{7 + mm(370 + i*330)}mm;top:{7 + mm(124)}mm;height:{mm(280)}mm"></div>' for i in range(3))
HTML = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><style>
@font-face{{font-family:T;src:url({F}DejaVuSans.ttf)}}
@font-face{{font-family:T;src:url({F}DejaVuSans-Bold.ttf);font-weight:700}}
@page{{size:104mm 64mm;margin:0}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:T,sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.p{{width:104mm;height:64mm;background:#000;color:#fff;position:relative;overflow:hidden;break-after:page}}
.frente img{{position:absolute;left:7mm;top:7mm;width:90mm;height:50mm}}
.col{{position:absolute;top:{7 + mm(140)}mm;text-align:center}}
.ic svg{{width:{mm(92)}mm;height:{mm(92)}mm}}
.rot{{font-size:1.75mm;letter-spacing:.03em;margin-top:{mm(24)}mm}}
.dato{{font-weight:700;margin-top:{mm(26)}mm;white-space:nowrap}}
.v{{position:absolute;width:.1mm;background:{AZ}}}
.h{{position:absolute;left:{7 + mm(62)}mm;width:{mm(1276)}mm;top:{7 + mm(450)}mm;height:.1mm;background:{AZ}}}
.bl{{position:absolute;top:{7 + mm(492)}mm}}
.bl b{{display:block;color:{AZ};font-size:1.75mm;letter-spacing:.03em}}
.bl p{{font-size:2.3mm;line-height:1.75;margin-top:1.4mm}}
.bl .web{{font-weight:700;font-size:2.15mm}} .bl .sub{{font-size:1.95mm}}
</style></head><body>
<section class="p frente"><img src="logo_frente.png" alt="Masherr"></section>
<section class="p">{''.join(col(i, *c) for i, c in enumerate(COLS))}{seps}<div class="h"></div>
<div class="v" style="left:{7 + mm(700)}mm;top:{7 + mm(498)}mm;height:{mm(170)}mm"></div>
<div class="bl" style="left:{7 + mm(78)}mm"><b>DIRECCIÓN</b><p>Hipólito Yrigoyen 4335<br>Villa Lynch, San Martín</p></div>
<div class="bl" style="left:{7 + mm(746)}mm"><b>TIENDA ONLINE</b><p><span class="web">masherrferreteria.com.ar</span><br><span class="sub">Máquinas y herramientas</span></p></div>
</section></body></html>'''
(AQUI / 'tarjeta.html').write_text(HTML)
print('ok')
