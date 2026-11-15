"""Arma el paquete de descarga: una carpeta por pieza con la imagen en alta calidad y su texto.
Uso: python3 empaquetar.py  →  Masherr_Instagram_alta_calidad.zip
"""
import re, shutil, zipfile
from pathlib import Path
AQUI = Path(__file__).parent
src = (AQUI / 'generar_estrategia_ig.py').read_text()
COPYS = {n: (t, c) for n, t, c in re.findall(r"\('(post_\w+)', '([^']+)', '((?:[^'\\]|\\.)*)'\)", src)}
HASH = '\n\n#ferreteria #ferreteriaindustrial #sanmartin #villalynch #herramientas #masherr'
USO = {
 'story_s1_producto': 'Agregá el sticker de ENLACE a la ficha del producto en masherrferreteria.com.ar, tapando el recuadro punteado.',
 'story_s2_encuesta': 'Agregá el sticker de ENCUESTA (opciones: “Con cable” / “A batería”) tapando el recuadro punteado.',
 'story_s3_resenas': 'Agregá el sticker de ENLACE a https://g.page/r/CSTh9aafPrTYEBE/review tapando el recuadro punteado.',
 'story_h1_horarios': 'Publicar los lunes y fijar en Destacadas → “Horarios”.',
 'story_h2_abrimos': 'Publicar al abrir (8:00). Opcional: sumar una foto o video corto del local abriendo.',
 'story_h3_cerramos': 'Publicar al cerrar (17:00; sábados 12:30 cambiando el texto de apertura del día siguiente si hace falta).',
 'story_h4_mediodia': 'Publicar a las 12:00 de lunes a viernes.',
 'story_h5_contacto': 'Fijar en Destacadas → “Contacto”. Sumar sticker de enlace a WhatsApp: https://wa.me/5491131826166',
 'story_h6_pagos': 'Fijar en Destacadas → “Pagos”. CONFIRMAR que estos medios de pago son los vigentes antes de publicar.',
 'story_h7_como_llegar': 'Agregá el sticker de UBICACIÓN (Ferretería Industrial Masherr) o un enlace a https://maps.app.goo.gl/DFGesHfBCZgQHgJY6',
 'story_h8_feriado': 'Escribí la fecha del feriado con la herramienta de texto de Instagram sobre “__ / __”.',
 'story_h9_como_comprar': 'Agregá el sticker de ENLACE a https://masherrferreteria.com.ar y fijá en Destacadas → “Comprar”.',
}
out = AQUI / 'descarga'
shutil.rmtree(out, ignore_errors=True)
for png in sorted((AQUI / 'png').glob('Masherr_*.png')):
    clave = png.stem.replace('Masherr_', '')
    tipo = 'Posts' if clave.startswith('post') else 'Historias'
    d = out / tipo / clave; d.mkdir(parents=True)
    shutil.copy(png, d / png.name)
    if clave in COPYS:
        t, c = COPYS[clave]
        (d / 'copy.txt').write_text(f'{t}\n\n{c}{HASH}\n')
    else:
        (d / 'como_usar.txt').write_text(USO.get(clave, '') + '\n')
z = AQUI / 'Masherr_Instagram_alta_calidad.zip'
with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED) as f:
    for p in sorted(out.rglob('*')):
        if p.is_file(): f.write(p, p.relative_to(out))
print(len(COPYS), 'copys ·', z.stat().st_size // 1024, 'KB')
