"""Resúmenes compactos (2 videos por página, solo los videos) de las dos propuestas de videos.
Uso: python3 generar_resumenes.py && node exportar_pdf.js resumen_videos_diciembre.html Masherr_Resumen_Videos_Diciembre.pdf
     node exportar_pdf.js resumen_videos_empresas.html Masherr_Resumen_Videos_Empresas.pdf
Toma los guiones de generar_propuesta.py y generar_corporativo.py (una sola fuente de verdad).
"""
import html, re, runpy
from pathlib import Path

AQUI = Path(__file__).parent
e = lambda s: html.escape(s, quote=True)
mark = lambda t: re.sub(r'\[\[(.+?)\]\]', r'<mark>\1</mark>', e(t))

def tarjeta(v, etiqueta, dur):
    if v.get('dialogo'):
        g = ''.join(f'<p><b>{e(q)}:</b> {mark(d)}</p>' for q, d in v['dialogo'])
    else:
        g = ''.join(f'<p>{mark(p)}</p>' for p in v['guion'])
    prods = ' · '.join(e(p) for p in v['prods'])
    quien = f'{v["quien"]} · {v["loc"]}'
    return f'''<article class="v"><div class="vcab"><span class="num">{v["n"]:02d}</span><h2>{e(v["t"])}</h2>
<span class="chips"><i>{e(etiqueta)}</i><i class="g">~{dur} s</i></span></div>
<div class="info"><b>Formato:</b> {e(v["formato"])} &nbsp;·&nbsp; <b>Quién/dónde:</b> {e(quien)}</div>
<div class="pant">{e(v["pantalla"])}</div>
<div class="guion">{g}</div>
<div class="pie2"><div><b>Tomas:</b> {e(v["tomas"])}</div>{f'<div><b>Productos:</b> {prods}</div>' if prods else ''}</div></article>'''

def documento(titulo, bajada, videos, etiqueta, dur, archivo, cierre):
    pares = [videos[i:i + 2] for i in range(0, len(videos), 2)]
    total = len(pares)
    hojas = []
    for n, par in enumerate(pares, 1):
        cab = f'<div class="tit"><b>{e(titulo)}</b><span>{e(bajada)}</span></div>' if n == 1 else ''
        hojas.append(f'''<section class="hoja"><div class="cab"><img src="../catalogo/img/masher-logo-azul.png" alt="Masherr"><span>Resumen</span></div>
<div class="cuerpo">{cab}{''.join(tarjeta(v, etiqueta(v), dur(v)) for v in par)}</div>
<div class="pie"><span>{e(cierre)}</span><b>{n:02d} / {total:02d}</b></div></section>''')
    (AQUI / archivo).write_text(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{e(titulo)}</title><style>{CSS}</style></head><body>{"".join(hojas)}</body></html>')
    return total

CSS = (AQUI / 'estilo.css').read_text() + '''
.cuerpo { display: flex; flex-direction: column; gap: 14px; }
.tit { border-bottom: 2px solid var(--negro); padding-bottom: 6px; }
.tit b { display: block; font-family: "Cond"; font-size: 24px; color: var(--negro); text-transform: uppercase; }
.tit span { font-size: 13px; color: #5A6072; }
.v { flex: 1; border: 1px solid var(--linea); border-top: 4px solid var(--azul); padding: 10px 14px; display: flex; flex-direction: column; min-height: 0; }
.vcab { display: flex; align-items: center; gap: 10px; }
.vcab .num { font-family: "Cond"; font-size: 26px; color: var(--celeste); }
.vcab h2 { font-family: "Cond"; font-size: 21px; line-height: 1.1; text-transform: uppercase; flex: 1; margin: 0; }
.chips i { font-style: normal; font-family: "Cond"; font-size: 12px; background: var(--azul); color: #fff; padding: 3px 7px; margin-left: 4px; white-space: nowrap; }
.chips i.g { background: var(--gris); color: var(--negro); }
.info { font-size: 12px; color: #3A4052; margin: 5px 0 6px; line-height: 1.35; }
.pant { background: var(--negro); color: #fff; font-size: 13.5px; padding: 6px 10px; margin-bottom: 6px; }
.guion { border-left: 3px solid var(--azul); padding-left: 10px; margin-bottom: 6px; }
.guion p { font-size: 14.5px; line-height: 1.38; margin: 0 0 3px; }
.guion p b { font-family: "Cond"; color: var(--azul); }
.pie2 { font-size: 11.5px; line-height: 1.35; color: #3A4052; margin-top: auto; }
.pie2 div { margin-top: 3px; } .pie2 b { color: var(--negro); }
mark { background: #FFE58A; color: inherit; padding: 0 2px; }
'''

if __name__ == '__main__':
    p = runpy.run_path(str(AQUI / 'generar_propuesta.py'))
    a = documento('Videos de diciembre · TikTok e Instagram', '12 videos · 3 por semana · sin precios · placa final: masherrferreteria.com.ar',
                  p['V'], lambda v: f'Semana {v["sem"]} · {v["tipo"]}', p['dur'], 'resumen_videos_diciembre.html', 'Masherr · Resumen de videos')
    c = runpy.run_path(str(AQUI / 'generar_corporativo.py'))
    b = documento('Videos para empresas e industria', '01–10: grabar hoy · 11–20: semana que viene · lo marcado en amarillo se confirma antes de publicar',
                  c['V'], lambda v: f'{v["cuando"]} · {v["tipo"]}', c['dur'], 'resumen_videos_empresas.html', 'Masherr · Resumen de videos para empresas')
    print('páginas:', a, b)
