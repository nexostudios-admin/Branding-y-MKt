# Arma la gráfica a partir de fuente.html, con las imágenes de assets/ adentro:
#  - grafica-artifact.html: para publicar online (la plataforma agrega el esqueleto del documento)
#  - El_Motivo_grafica.html: documento completo para abrir en la compu de vMix
import base64, os, re
aqui = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(aqui, "fuente.html")).read()
def dato(m):
    nombre = m.group(1)
    tipo = "image/png" if nombre.endswith(".png") else "image/jpeg"
    return "data:%s;base64,%s" % (tipo, base64.b64encode(open(os.path.join(aqui, "assets", nombre), "rb").read()).decode())
src = re.sub(r"\{\{IMG:([^}]+)\}\}", dato, src)
open(os.path.join(aqui, "grafica-artifact.html"), "w").write(src)
head = '<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
e = src.index("</style>") + len("</style>")
open(os.path.join(aqui, "El_Motivo_grafica.html"), "w").write(head + src[:e] + "\n</head>\n<body>\n" + src[e:] + "\n</body>\n</html>\n")
