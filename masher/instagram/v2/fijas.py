"""Historias fijas (sin fecha): se reutilizan todos los días. Uso: python3 fijas.py && node exportar_v2.js --manifiesto manifiesto_fijas.json --salida salida_fijas"""
import json
from mes import AQUI, CSS, h_abrimos, h_mediodia, h_volvimos, h_cierre, h_comunidad, h_domingo
LV = 'LUNES A VIERNES'
FIJAS = [
    ('1 - Lunes a viernes 08.00 - Abrimos', h_abrimos(LV, '8 H')),
    ('2 - Lunes a viernes 12.00 - Cerramos al mediodia', h_mediodia(LV, '12 A 14 H')),
    ('3 - Lunes a viernes 14.00 - Volvimos (14 a 17)', h_volvimos(LV, '14 A 17 H')),
    ('4 - Lunes a viernes 17.00 - Cerramos', h_cierre(LV, '17 H')),
    ('5 - Sabados 08.00 - Abrimos', h_abrimos('SÁBADOS', '8 A 12:30 H', sab=True)),
    ('6 - Sabados 12.30 - Cerramos', h_cierre('SÁBADOS', '12:30 H', sab=True)),
    ('7 - Domingos - Hoy descansamos', h_domingo('DOMINGOS', 'CERRADO')),
    ('8 - Comunidad A (todos los dias)', h_comunidad('COMUNIDAD', 'WHATSAPP', 1)),
    ('9 - Comunidad B (todos los dias)', h_comunidad('COMUNIDAD', 'WHATSAPP', 2)),
]
if __name__ == '__main__':
    base = AQUI / 'fijas'; base.mkdir(exist_ok=True)
    man = []
    for nombre, html in FIJAS:
        a = 'historia__' + nombre.replace(' ', '_').replace('(', '').replace(')', '') + '.html'
        (base / a).write_text(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{html}</body></html>')
        man.append({'dia': 'fijas', 'carpeta': '00 - Historias fijas', 'tipo': 'historia', 'nombre': nombre, 'html': f'fijas/{a}'})
    (AQUI / 'manifiesto_fijas.json').write_text(json.dumps(man, ensure_ascii=False, indent=1))
    print(len(man))
