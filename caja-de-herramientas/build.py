# Arma las dos versiones a partir de fuente.html:
#  - caja-artifact.html: contenido para publicar como Artifact (el skeleton lo agrega la plataforma)
#  - El_Motivo_caja_de_herramientas.html: documento completo para abrir local o en OBS
import base64, sys, os
aqui = os.path.dirname(os.path.abspath(__file__))
logo = "data:image/jpeg;base64," + base64.b64encode(open(os.path.join(aqui, "logo.jpg"), "rb").read()).decode()
src = open(os.path.join(aqui, "fuente.html")).read().replace("{{LOGO}}", logo)
open(os.path.join(aqui, "caja-artifact.html"), "w").write(src)
head = '<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
e = src.index("</style>") + len("</style>")
open(os.path.join(aqui, "El_Motivo_caja_de_herramientas.html"), "w").write(head + src[:e] + "\n</head>\n<body>\n" + src[e:] + "\n</body>\n</html>\n")
