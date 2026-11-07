"""Crea la planilla inicial de productos (xlsx) a partir de los datos actuales de la web.
Uso: python3 crear_planilla.py salida.xlsx
Una fila por producto; si un producto tiene opciones (tamaños, medidas), una fila por opción con el mismo "Producto".
"""
import json, sys
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.worksheet.datavalidation import DataValidation

WEB = Path(__file__).resolve().parent.parent
datos = json.load(open(WEB / 'sitio' / 'data' / 'productos.json'))
snap = {p['slug']: p for p in json.load(open(WEB / 'catalogo' / 'snapshot_tiendanube.json'))['productos']}
CATS = [c['nombre'] for c in datos['categorias']]
COLS = ['Producto', 'Precio', 'Stock', 'Publicado', 'Marca', 'Categoría', 'Opción', 'Código', 'Descripción nueva', 'Fotos nuevas', 'Dirección web']
ANCHOS = [46, 12, 9, 11, 16, 26, 14, 14, 50, 40, 40]

wb = Workbook()
ws = wb.active; ws.title = 'Productos'
ws.append(COLS)
for p in datos['productos']:
    for v in p['variantes']:
        ws.append([p['nombre'], v['precio'], v['stock'], 'SI', p['marca'] or '', p['catNombre'], v['nombre'] or '', v['sku'] or '',
                   '', '', p['slug']])
azul = PatternFill('solid', fgColor='17256B')
for i, c in enumerate(ws[1]):
    c.font = Font(bold=True, color='FFFFFF'); c.fill = azul; c.alignment = Alignment(vertical='center')
    ws.column_dimensions[c.column_letter].width = ANCHOS[i]
ws.freeze_panes = 'B2'
ws.row_dimensions[1].height = 24
n = ws.max_row
dv = DataValidation(type='list', formula1='"SI,NO"', allow_blank=False); ws.add_data_validation(dv); dv.add(f'D2:D2000')
dc = DataValidation(type='list', formula1='=Categorías!$A$2:$A$30', allow_blank=False); ws.add_data_validation(dc); dc.add(f'F2:F2000')
for col in ('B', 'C'):
    for r in range(2, n + 1): ws[f'{col}{r}'].number_format = '#,##0' if col == 'B' else '0'

cs = wb.create_sheet('Categorías')
cs.append(['Categoría']); cs['A1'].font = Font(bold=True, color='FFFFFF'); cs['A1'].fill = azul
for c in CATS: cs.append([c])
cs.column_dimensions['A'].width = 34

ins = wb.create_sheet('Instrucciones', 0)
texto = [
    ('CÓMO USAR ESTA PLANILLA', True),
    ('La web masherr.netlify.app lee la hoja "Productos" y se actualiza sola (puede tardar hasta una hora).', False),
    ('', False),
    ('CAMBIAR UN PRECIO O EL STOCK', True),
    ('Buscá el producto y cambiá la columna Precio o Stock. Precio sin puntos ni $ (ej.: 16000).', False),
    ('Stock en 0 = aparece "Sin stock" y no se puede agregar al carrito. Stock vacío = sin control de stock.', False),
    ('', False),
    ('OCULTAR UN PRODUCTO', True),
    ('Poné NO en la columna Publicado. Para volver a mostrarlo, poné SI.', False),
    ('', False),
    ('AGREGAR UN PRODUCTO NUEVO', True),
    ('Agregá una fila al final. Completá Producto, Precio, Stock, Publicado (SI), Marca, Categoría y Descripción.', False),
    ('Dejá vacía la columna Dirección web: la web la genera sola.', False),
    ('Fotos: subí la foto a la carpeta "Masherr - Fotos de productos" de Drive, tocá Compartir > Copiar vínculo y pegalo en la columna Fotos nuevas. Varias fotos: separalas con un espacio.', False),
    ('', False),
    ('CAMBIAR LA DESCRIPCIÓN O LAS FOTOS DE UN PRODUCTO EXISTENTE', True),
    ('Escribí el texto en Descripción nueva o pegá los vínculos en Fotos nuevas. Si las dejás vacías, la web mantiene la descripción y las fotos que ya tiene.', False),
    ('', False),
    ('PRODUCTOS CON OPCIONES (tamaños, medidas)', True),
    ('Una fila por opción, con el mismo texto en Producto y la opción en la columna Opción (ej.: 1 Kg., 1/2 Kg.).', False),
    ('', False),
    ('NO TOCAR', True),
    ('La columna Dirección web de los productos existentes (sirve para que no se rompan los links ni los carritos).', False),
    ('Los nombres de las columnas de la fila 1.', False),
]
for t, b in texto:
    ins.append([t])
    if b: ins.cell(row=ins.max_row, column=1).font = Font(bold=True, color='17256B', size=12)
ins.column_dimensions['A'].width = 120
wb.save(sys.argv[1])
print(n - 1, 'filas')
