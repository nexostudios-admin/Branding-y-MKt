"""Recorta el fondo blanco de las fotos de producto (relleno desde los bordes) → PNG con transparencia."""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
SRC = Path('../../web/sitio/img/productos')
OUT = Path('recortes')
def recortar(nombre):
    im = Image.open(SRC / f'{nombre}-1024-1024.webp').convert('RGBA')
    w, h = im.size
    base = im.convert('RGB')
    marca = (255, 0, 255)
    for x, y in [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1), (w // 2, 0), (w // 2, h - 1), (0, h // 2), (w - 1, h // 2)]:
        if sum(base.getpixel((x, y))) > 690:
            ImageDraw.floodfill(base, (x, y), marca, thresh=38)
    m = Image.new('L', (w, h), 255)
    px, mp = base.load(), m.load()
    for y in range(h):
        for x in range(w):
            if px[x, y] == marca: mp[x, y] = 0
    m = m.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2))
    im.putalpha(m)
    im = im.crop(im.getbbox())
    im.save(OUT / f'{nombre}.png')
    return im.size
for n in sys.argv[1:]:
    print(n[:40], recortar(n))
