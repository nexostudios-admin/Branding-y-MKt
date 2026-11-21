"""Foto de producto con marco Masherr (1024 y 480 px).

Recorta el fondo blanco de la foto del catálogo, la apoya sobre el fondo de marca (gris con la "ráfaga"
del logo) con sombra suave y agrega el logo de Masherr. Si la foto no tiene fondo blanco, la presenta
en una tarjeta blanca dentro del mismo marco. Solo usa Pillow (disponible en el build de Netlify).
"""
from pathlib import Path
from PIL import Image, ImageChops, ImageDraw, ImageFilter

T = 1024
GRIS, GRIS2, AZUL = (241, 243, 247), (226, 230, 239), (23, 37, 107)

def _fondo(logo):
    im = Image.new('RGB', (T, T), GRIS)
    d = ImageDraw.Draw(im)
    # ráfaga: líneas horizontales de largo escalonado, alineadas a la derecha y con el borde inclinado
    largos = [1, .82, .94, .7, .88, .62, .97, .76, .9, .66]
    alto, paso, x0, y0, ancho = 15, 30, 560, 70, 464
    for k, l in enumerate(largos):
        y = y0 + k * paso
        w = int(ancho * l)
        inclin = int((y - y0) * .32)
        d.rectangle([T - w + inclin, y, T, y + alto], fill=GRIS2)
    # base: franja azul fina
    d.rectangle([0, T - 10, T, T], fill=AZUL)
    lw = 190
    lg = logo.resize((lw, round(logo.height * lw / logo.width)), Image.LANCZOS)
    im.paste(lg, (54, T - 54 - lg.height), lg)
    return im

def _fondo_blanco(foto):
    w, h = foto.size
    pts = [(2, 2), (w - 3, 2), (2, h - 3), (w - 3, h - 3), (w // 2, 2), (w // 2, h - 3), (2, h // 2), (w - 3, h // 2)]
    return sum(1 for p in pts if min(foto.getpixel(p)) > 232) >= 6

def _recorte(foto):
    base = foto.copy()
    w, h = base.size
    for p in [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1), (w // 2, 0), (w // 2, h - 1), (0, h // 2), (w - 1, h // 2)]:
        if min(base.getpixel(p)) > 232:
            ImageDraw.floodfill(base, p, (255, 0, 255), thresh=34)
    r, g, b = base.split()
    fondo = ImageChops.multiply(ImageChops.multiply(r.point(lambda v: 255 if v == 255 else 0), g.point(lambda v: 255 if v == 0 else 0)),
                                b.point(lambda v: 255 if v == 255 else 0))
    alfa = ImageChops.invert(fondo).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1))
    out = foto.convert('RGBA'); out.putalpha(alfa)
    caja = out.getbbox()
    return out.crop(caja) if caja else out

def generar(origen, destino_base, logo_path):
    """origen: ruta a la foto 1024. destino_base: ruta sin sufijo. Crea -1024-1024.webp y -480-0.webp."""
    logo = Image.open(logo_path).convert('RGBA')
    foto = Image.open(origen).convert('RGB')
    lienzo = _fondo(logo)
    caja_w, caja_h, cy = 780, 700, 470
    if _fondo_blanco(foto):
        obj = _recorte(foto)
        if obj.width < 40 or obj.height < 40:
            obj = foto.convert('RGBA')
        esc = min(caja_w / obj.width, caja_h / obj.height)
        obj = obj.resize((max(1, round(obj.width * esc)), max(1, round(obj.height * esc))), Image.LANCZOS)
        x, y = (T - obj.width) // 2, cy - obj.height // 2
        sombra = Image.new('RGBA', obj.size, (8, 9, 11, 0))
        sombra.putalpha(obj.split()[3].point(lambda v: int(v * .28)))
        sombra = sombra.filter(ImageFilter.GaussianBlur(18))
        lienzo.paste(sombra, (x + 10, y + 26), sombra)
        lienzo.paste(obj, (x, y), obj)
    else:  # foto con fondo de color: tarjeta blanca
        lado = 720
        f = foto.copy(); f.thumbnail((lado - 40, lado - 40), Image.LANCZOS)
        tarjeta = Image.new('RGB', (lado, lado), (255, 255, 255))
        tarjeta.paste(f, ((lado - f.width) // 2, (lado - f.height) // 2))
        x, y = (T - lado) // 2, cy - lado // 2
        sh = Image.new('RGBA', (lado + 60, lado + 60), (0, 0, 0, 0))
        ImageDraw.Draw(sh).rectangle([30, 30, lado + 30, lado + 30], fill=(8, 9, 11, 45))
        sh = sh.filter(ImageFilter.GaussianBlur(16))
        lienzo.paste(sh, (x - 30 + 8, y - 30 + 20), sh)
        lienzo.paste(tarjeta, (x, y))
    Path(destino_base).parent.mkdir(parents=True, exist_ok=True)
    lienzo.save(f'{destino_base}-1024-1024.webp', quality=86, method=5)
    lienzo.resize((480, 480), Image.LANCZOS).save(f'{destino_base}-480-0.webp', quality=84, method=5)
