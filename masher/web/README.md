# Masherr · web propia (institucional + tienda con pedido por WhatsApp)

Sitio estático, sin servidor ni base de datos. La tienda arma el carrito en el navegador y el pedido se envía armado al WhatsApp oficial (+54 9 11 3182-6166), donde se confirma precio, stock, entrega y pago. **La web no cobra**: la operación se cierra por WhatsApp.

## Qué tiene

| Página | Ruta | Qué hace |
| --- | --- | --- |
| Inicio | `sitio/index.html` | Buscador, categorías, selección de productos, cómo comprar, historia, redes, acceso empresas |
| Tienda | `sitio/tienda/` | Búsqueda por nombre/marca/código, filtros (categoría, marca, con stock), orden y paginación. Los filtros quedan en la URL |
| Ficha | `sitio/producto/<slug>/` | Foto ampliable, precio, stock, opciones (variantes), cantidad, agregar al carrito, consultar por WhatsApp, relacionados. Una página por producto con datos estructurados `Product` |
| Carrito | `sitio/carrito/` | Editar cantidades, quitar, total estimado, datos de entrega y pago, **Enviar pedido por WhatsApp** |
| Empresas | `sitio/empresas/` | Formulario de cotización (tarea, productos, cantidades, plazo) que se envía por WhatsApp |
| Nosotros | `sitio/nosotros/` | Institucional, cómo trabajamos, cómo comprar, redes y el local |

Las redes se configuran en `config.json`: perfiles (Instagram, TikTok, LinkedIn, Facebook) y publicaciones a mostrar. Las publicaciones se cargan desde cada red solo cuando la persona toca “Ver publicación” (no se cargan scripts de terceros de entrada).

## Actualizar productos y precios (planilla de Google)

La fuente de verdad es la planilla **Masherr - Productos de la web** (Google Sheets, compartida con redesmasherr@gmail.com; id en `config.json` → `planilla_id`). Instrucciones para el equipo: documento **Masherr - Cómo usar la planilla de productos**. Fotos nuevas: carpeta **Masherr - Fotos de productos**.

- Netlify ejecuta `python3 construir.py` en cada publicación: lee la planilla (exportación CSV) y regenera la web. Si no la puede leer, publica con los datos anteriores.
- La función programada `netlify/functions/actualizar.mjs` dispara una publicación cada hora (necesita la variable `BUILD_HOOK_URL` en Netlify).
- Requisitos: la planilla y la carpeta de fotos compartidas como “Cualquier persona con el enlace: Lector” (planilla: hecho el 08/11/2026).
- Probar con un CSV local: `PLANILLA_CSV=archivo.csv python3 construir.py`.

## Copia desde Tiendanube (histórico)

Hoy el catálogo sale de la tienda Tiendanube publicada (copia del 06/11/2026: 244 productos):

```bash
python3 catalogo/snapshot_tiendanube.py catalogo/snapshot_tiendanube.json   # vuelve a leer la tienda
python3 construir.py                                                       # regenera sitio/
```

Antes de publicar, actualizar `fecha_precios` en `config.json`. Las fotos se descargan una vez a `sitio/img/productos/` (borrar la carpeta para forzar la descarga).

## Cambiar datos del negocio o redes

Editar `config.json` (WhatsApp, teléfono, dirección, horarios, redes, publicaciones) y correr `python3 construir.py`.

## Probar localmente

```bash
cd sitio && python3 -m http.server 8000   # abrir http://localhost:8000
```

## Publicar

Cualquier hosting estático sirve la carpeta `sitio/` tal cual (Netlify, Cloudflare Pages, GitHub Pages o el hosting del dominio). Con el dominio definido, completar `dominio` en `config.json` y volver a construir: genera `sitemap.xml`, `robots.txt` y URLs canónicas.

## Probado (06/11/2026)

- 360, 390, 768, 1024 y 1440 px: sin scroll horizontal, sin errores de JavaScript.
- Búsqueda, filtro por categoría desde el panel móvil, variante con otro precio, agregar, cambiar cantidades, validación de nombre y dirección, mensaje de WhatsApp con productos, cantidades, subtotales, total, entrega y datos.
- Teclado: “Saltar al contenido” es el primer foco; foco visible en todos los controles.

## Pendiente / límites

- Precios y stock son una copia: no se actualizan solos. Definir quién y cómo se actualiza (ver arriba).
- El carrito vive en el navegador de cada cliente; los pedidos quedan registrados solo en WhatsApp.
- LinkedIn: la cuenta se va a crear; cuando exista, cargar la URL en `config.json` (aparece sola). No hay publicaciones cargadas todavía.
- Fotos reales del local y del equipo; horarios; políticas de cambios y envíos.
- 2 productos tienen imagen con nombre de generador de IA (ver `catalogo/REPORTE_VALIDACION.md`).
- No se midió rendimiento (LCP, INP, CLS) en condiciones reales: hacerlo con el sitio publicado.
