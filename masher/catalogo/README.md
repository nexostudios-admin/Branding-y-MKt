# Masher · Catálogo de productos

Rediseño del `CATÁLOGO TN` (planilla exportada a PDF) con el manual de marca de Masher: azul `#17256B`, negro `#08090B`, blanco, DejaVu Sans Condensed Bold para titulares y DejaVu Sans para textos.

- **PDF:** en `pdf/` hay 6 tomos por rubro (13 a 22 páginas) y el completo (`Masherr_Catalogo_Completo.pdf`) (formato vertical 9:16 (540 × 960 pt, como el manual), 98 páginas a una columna para leer en el celular: tapa, índice, marcas, 13 categorías y contratapa).
- 436 productos, 55 marcas. Cada ficha: nombre, marca, qué incluye (si aplica), descripción corta y precio.
- En la tapa y contratapa se usa el logo blanco sobre negro; en el interior, el original azul sobre blanco.

## Cómo regenerarlo

1. `python3 extraer.py CATA_LOGO_TN.pdf` → `rows.json` (lee la tabla del PDF original).
2. `python3 limpiar.py rows.json` → `productos.json` (limpia y asigna categoría por palabras clave; ver `CATS`).
3. Pasar `productos.json` a `productos.js` (`window.PRODUCTOS = [...]`, sin `descripcion_completa`).
4. `node render.js` genera todos los PDF en `pdf/` (el HTML pagina solo; `catalogo.html?g=N` muestra un tomo, ver `TOMOS`).

Para cambiar un precio o una descripción alcanza con editar `productos.js` y correr `node render.js`.
