"""Tarjeta (90x50 mm + 7 mm de sangrado) y cartel A5 para pedir reseñas, con el estilo de la tarjeta de contacto.
Uso: python3 generar.py && node exportar.js
"""
import qrcode
from pathlib import Path

AQUI = Path(__file__).parent
LINK = 'https://g.page/r/CSTh9aafPrTYEBE/review'
F = '../../catalogo/fonts/'

q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, border=0)
q.add_data(LINK); q.make(fit=True)
m = q.get_matrix(); n = len(m)
rects = ''.join(f'<rect x="{x}" y="{y}" width="1.02" height="1.02"/>' for y, r in enumerate(m) for x, v in enumerate(r) if v)
QR = f'<svg viewBox="0 0 {n} {n}" xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges"><g fill="#000">{rects}</g></svg>'
ESTRELLA = '<svg viewBox="0 0 24 24"><path d="M12 2.5l2.9 6.1 6.6.8-4.9 4.6 1.3 6.6L12 17.3 6.1 20.6l1.3-6.6L2.5 9.4l6.6-.8z" fill="#7C9ED8"/></svg>'
ESTRELLAS = '<div class="est">' + ESTRELLA * 5 + '</div>'

CSS = f'''
@font-face{{font-family:T;src:url({F}DejaVuSans.ttf)}}
@font-face{{font-family:T;src:url({F}DejaVuSans-Bold.ttf);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:T,sans-serif;background:#888;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.p{{background:#000;color:#fff;position:relative;overflow:hidden;break-after:page;margin:0 auto}}
.az{{color:#7C9ED8}} .lin{{background:#7C9ED8}}
.est{{display:flex;gap:1.2mm}} .est svg{{width:4mm;height:4mm}}
.qr{{background:#fff;border-radius:2mm}} .qr svg{{width:100%;height:100%;display:block}}
'''

TARJETA = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS}
@page{{size:104mm 64mm;margin:0}}
.p{{width:104mm;height:64mm}}
.frente img{{width:104mm;height:57.8mm;object-fit:cover;margin-top:3.1mm}}
.d .qr{{position:absolute;left:14mm;top:15mm;width:31mm;height:31mm;padding:2mm}}
.d .sep{{position:absolute;left:52mm;top:15mm;width:.25mm;height:31mm}}
.d .txt{{position:absolute;left:57mm;top:14.3mm;right:12mm}}
.d .rot{{font-weight:700;font-size:2.3mm;letter-spacing:.06em}}
.d h1{{font-size:4.6mm;line-height:1.12;margin:1.6mm 0 2.2mm}}
.d ol{{list-style:none;font-size:2.05mm;line-height:1.55;margin-top:2.4mm}}
.d ol b{{color:#7C9ED8}}
</style></head><body>
<section class="p frente"><img src="logo_frente.png" alt="Masherr"></section>
<section class="p d"><div class="qr">{QR}</div><div class="sep lin"></div>
<div class="txt"><div class="rot az">¿TE ATENDIMOS BIEN?</div><h1>DEJANOS TU<br>OPINIÓN EN<br>GOOGLE.</h1>{ESTRELLAS}
<ol><li><b>1</b>&nbsp; Escaneá el código</li><li><b>2</b>&nbsp; Elegí las estrellas</li><li><b>3</b>&nbsp; Contanos cómo te fue</li></ol></div></section>
</body></html>'''

CARTEL = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS}
@page{{size:148mm 210mm;margin:0}}
.p{{width:148mm;height:210mm}}
.logo{{position:absolute;left:0;right:0;top:4mm;height:62mm;background:url(logo_frente.png) center/cover no-repeat}}
.h{{position:absolute;left:14mm;right:14mm;height:.3mm}}
.rot{{position:absolute;left:14mm;top:75mm;font-weight:700;font-size:4.2mm;letter-spacing:.08em}}
h1{{position:absolute;left:14mm;top:83mm;font-size:9mm;line-height:1.1}}
.e{{position:absolute;left:14mm;top:110mm}} .e .est svg{{width:7mm;height:7mm}} .e .est{{gap:2mm}}
.qr{{position:absolute;right:14mm;top:75mm;width:50mm;height:50mm;padding:3mm}}
.pasos{{position:absolute;left:14mm;right:14mm;top:141mm;display:flex}}
.pasos div{{flex:1;text-align:center;padding:0 2mm;border-left:.3mm solid #7C9ED8}} .pasos div:first-child{{border:0}}
.pasos b{{display:block;font-size:9mm;color:#7C9ED8}} .pasos span{{display:block;font-size:3.6mm;line-height:1.35;margin-top:2mm}}
.pie{{position:absolute;left:14mm;right:14mm;top:181mm;display:flex;justify-content:space-between;font-size:3.4mm;line-height:1.5}}
.pie .r{{text-align:right}} .pie b.az{{font-size:3mm;letter-spacing:.06em}}
</style></head><body>
<section class="p"><div class="logo"></div><div class="h lin" style="top:68mm"></div>
<div class="rot az">¿TE ATENDIMOS BIEN?</div><h1>DEJANOS TU<br>OPINIÓN.</h1>
<div class="e">{ESTRELLAS}</div><div class="qr">{QR}</div><div class="h lin" style="top:134mm"></div>
<div class="pasos"><div><b>1</b><span>Escaneá el código con la cámara</span></div><div><b>2</b><span>Elegí las estrellas</span></div><div><b>3</b><span>Contanos cómo te fue y tocá “Publicar”</span></div></div>
<div class="h lin" style="top:174mm"></div>
<div class="pie"><div><b class="az">DIRECCIÓN</b><br>Calle 38 4335<br>Villa Lynch, San Martín</div><div class="r"><b class="az">TIENDA ONLINE</b><br>masherrferreteria.com.ar<br>@masherrferreteria</div></div>
</section></body></html>'''

(AQUI / 'tarjeta_resenas.html').write_text(TARJETA)
(AQUI / 'cartel_resenas.html').write_text(CARTEL)
print('ok', n, 'módulos')
