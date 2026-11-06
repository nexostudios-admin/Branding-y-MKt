# Esquema de catálogo (mapeo para importación)

Regla general: un dato que no existe queda **desconocido (`null`)**. Nunca 0, nunca inferido del nombre o de otro producto.

| Campo | Tipo | Obligatorio para vender | Origen en Tiendanube (admin / CSV) | Origen en la copia pública | Notas |
| --- | --- | --- | --- | --- | --- |
| `sku` | texto único por variante | Sí | SKU | `variantes[].sku` | Clave de búsqueda e importación. Hoy falta en muchos productos. |
| `id_tiendanube` | número | — | ID de producto | `id_tiendanube` | Conservar para no romper enlaces. |
| `nombre` | texto | Sí | Nombre | `nombre` | Sin la marca pegada al final cuando exista campo marca. |
| `slug` | texto | Sí | URL | `slug` | Si cambia, preparar redirección 301. |
| `marca` | texto | No | Marca | `marca` (casi siempre vacío) | Hoy la marca está en el nombre. Cargarla como campo para filtrar. |
| `categoria` / `subcategoria` | lista | Sí | Categorías | `categorias` (breadcrumb) | Usar las familias existentes de la tienda. |
| `descripcion` | texto | No | Descripción | `descripcion` | Revisar copias erróneas (ej. adhesivo 1 lt con texto de 4 kg). |
| `atributos` | clave/valor | No | Propiedades / variantes | `null` | Potencia, encastre, diámetro, etc. Pedir al negocio. |
| `variantes` | lista | Sí | Variantes (hasta 3 propiedades) | `variantes[].opciones` | |
| `precio` | número + moneda | Sí | Precio | `variantes[].precio`, `moneda` | Si falta, desactivar compra. |
| `precio_promocional` | número | No | Precio promocional | `variantes[].precio_promocional` | Solo si el negocio lo cargó. |
| `stock` | número o `null` | Sí | Stock | `variantes[].stock` | `null` = sin control de stock (riesgo de sobreventa). |
| `peso_kg` | número | Para envíos | Peso | `peso_kg` | Necesario para cotizar envío. |
| `dimensiones` | alto/ancho/profundidad | Para envíos | Dimensiones | `null` | No publicadas. |
| `imagenes` | lista de URL | Sí | Imágenes | `imagenes` | Reemplazar las sintéticas por fotos reales con permiso. |
| `accesorios` | texto | No | — | `null` | En el PDF figura como “Incluye”. |
| `garantia` | texto | No | — | `null` | No publicar sin dato del negocio. |
| `publicado` | sí/no | — | Mostrar en tienda | (todo lo del sitemap está publicado) | |

## Procedimiento de importación

1. Exportar CSV desde el admin de Tiendanube (fuente de verdad).
2. Correr la validación (`validar.py`) y revisar el reporte con el negocio.
3. Corregir en el admin: SKU, duplicados, precios, stock, fotos y marca.
4. Importación de prueba con 20 productos variados (con y sin variantes, sin stock, solo consulta); revisar conteos y muestras.
5. Importación total. Guardar el reporte de importación y errores.
6. Con la ruta A (tema a medida), el tema lee el catálogo directo de Tiendanube: no hay segundo inventario que sincronizar.
