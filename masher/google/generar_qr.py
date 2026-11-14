"""Cartel A5 con QR para pedir reseñas en Google. Uso: python3 generar_qr.py [link]"""
import sys, qrcode
from PIL import Image, ImageDraw, ImageFont
LINK = sys.argv[1] if len(sys.argv) > 1 else 'https://maps.app.goo.gl/Qj7w6C5trkfbKCCGA'
U = '/root/.claude/uploads/01849ead-b7ff-5b3e-9867-28cbc3720288/'
F = '/home/user/Branding-y-MKt/masher/catalogo/fonts/'
W, H = 1748, 2480  # A5 a 300 dpi
NEGRO, AZUL, CEL, BL = (8, 9, 11), (23, 37, 107), (154, 174, 255), (255, 255, 255)
im = Image.new('RGB', (W, H), NEGRO); d = ImageDraw.Draw(im)
cond = lambda s: ImageFont.truetype(F + 'DejaVuSansCondensed-Bold.ttf', s)
txt = lambda s: ImageFont.truetype(F + 'DejaVuSans.ttf', s)
M = 130
for y in range(0, 520, 34):
    d.rectangle([W - 560 + int(y * 0.4), y, W, y + 20], fill=AZUL)
logo = Image.open(U + 'dffb5025-image.png').convert('RGBA'); logo = logo.crop(logo.getbbox())
lw = 980; lg = logo.resize((lw, int(logo.height * lw / logo.width)), Image.LANCZOS); pad = 46
d.rectangle([M, 170, M + lw + 2 * pad, 170 + lg.height + 2 * pad], fill=BL); im.paste(lg, (M + pad, 170 + pad), lg)
d.rectangle([M, 600, M + 70, 612], fill=CEL)
d.text((M + 95, 578), '¿TE ATENDIMOS BIEN?', font=cond(52), fill=CEL)
d.text((M, 660), 'DEJANOS TU', font=cond(150), fill=BL)
d.text((M, 820), 'OPINIÓN.', font=cond(150), fill=BL)
d.text((M, 1010), 'Escaneá el código con la cámara del celular.', font=txt(46), fill=(190, 195, 210))
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=26, border=2)
qr.add_data(LINK); qr.make(fit=True)
q = qr.make_image(fill_color=AZUL, back_color='white').convert('RGB')
qs = 900; q = q.resize((qs, qs), Image.NEAREST)
qx, qy = (W - qs) // 2, 1150
d.rounded_rectangle([qx - 40, qy - 40, qx + qs + 40, qy + qs + 40], radius=24, fill=BL)
im.paste(q, (qx, qy))
pasos = ['1  Tocá “Opiniones”', '2  Tocá “Escribir una opinión”', '3  Elegí las estrellas y contanos cómo te fue']
for i, p in enumerate(pasos):
    d.text((M, 2160 + i * 66), p, font=cond(48), fill=BL)
d.text((M, H - 90), 'Ferretería Industrial Masherr · Calle 38 4335, Villa Lynch', font=txt(34), fill=(140, 146, 160))
im.save('Masherr_cartel_resenas_A5.png', dpi=(300, 300))
im.save('Masherr_cartel_resenas_A5.pdf', resolution=300)
print('ok', LINK)
