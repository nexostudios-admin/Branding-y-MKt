# Masherr web + ecommerce · Diagnóstico técnico y elección del motor

Fecha: 6 de noviembre de 2026. Estado: **diagnóstico, sin integración**. Nada de lo que hay en esta carpeta cobra ni modifica la tienda.

## 1. Qué hay hoy

| Tema | Hallazgo | Cómo se verificó |
| --- | --- | --- |
| Motor | Tiendanube, tienda `masherrferreteria.mitiendanube.com` | Lectura pública del sitio |
| Tema actual | **Brasilia** (plantilla de Tiendanube) | Rutas de assets `themes/brasilia/` |
| Catálogo publicado | 244 productos, 249 variantes, todo en ARS, 0 errores de lectura | Copia pública de solo lectura (`catalogo/REPORTE_VALIDACION.md`) |
| Calidad de datos | Ningún producto publica SKU; la marca solo figura en el nombre; 18 productos tienen imágenes con nombre de generador de IA; 2 nombres duplicados; 3 con stock sin controlar | Mismo reporte |
| Catálogo PDF del cliente | 436 productos | `../catalogo/productos.json` |
| Familias | Herramientas (eléctricas, inalámbricas, manuales, insumos, medición, cajas, escaleras, equipos de pintar), Máquinas (aparejos y zorras, compresores, construcción, soldadoras, torno), Jardín, Agua y limpieza, Adhesivos y selladores, Espumas, Bolsos, Calefactor, Discos de corte, Mechas y brocas, Cinceles, Puntas y adaptadores, Muebles para el hogar | Sitemap |
| Pagos visibles en la ficha | Pago Nube y Mercado Pago (con cuotas calculadas por la plataforma) | Datos de variantes en la ficha |
| Datos estructurados | La plataforma ya publica `Product`, `Offer` (precio, moneda, stock) y `BreadcrumbList` | JSON-LD de las fichas |
| Institucional | “Quiénes somos” dice “más de 50 años”; el cliente informó 53; la agencia vio “más de 54” en otra página | `/quienessomos/` |

Diferencias a resolver con el negocio: el PDF tiene 436 productos y la tienda 244 (215 coinciden por nombre, 221 del PDF no aparecen publicados), y hay precios que no coinciden (detalle en el reporte). La fuente de verdad debe ser **una sola**: el admin de Tiendanube.

## 2. Elección del motor: seguir en Tiendanube

Se conserva Tiendanube para catálogo, stock, precios, pedidos, pagos, envíos y cuentas. Ya está operando, tiene los medios de pago configurados y el equipo lo administra sin código. Migrar implicaría un segundo inventario sin necesidad.

### Ruta recomendada (A): tema a medida + checkout nativo

Construir un tema propio sobre Tiendanube editando el código del diseño (FTP), con el checkout, pagos, envíos y notificaciones nativos.

- **Ventajas:** un solo inventario; el monto y el stock los valida Tiendanube en su servidor; los pedidos pagados los confirma la plataforma (no una URL de retorno); el equipo sigue cargando productos, fotos y precios desde el admin.
- **Requisitos a verificar con la cuenta:** la ayuda oficial indica que la edición por FTP está disponible **desde el Plan Impulso** y que algunas plantillas (por ejemplo Patagonia) no permiten acceso al código. Hay que confirmar el plan actual y si Brasilia, o la plantilla base que elijamos, lo permite.
- **Límite:** el checkout es de Tiendanube; se puede ajustar su apariencia dentro de lo que la plataforma permita, pero no reemplazarlo.

### Ruta alternativa (B): frontend desacoplado con Storefront API

Solo si el diseño no se puede lograr con un tema. Según la ayuda de Tiendanube, la Storefront API no viene habilitada por defecto (se pide por tienda), no tiene endpoint de carrito (el carrito lo arma el frontend) y la compra se deriva al checkout alojado de Tiendanube. Implica hosting propio, más mantenimiento y límites de solicitudes. **No se elige hasta verificar con la documentación oficial y la habilitación real para esta tienda.**

## 3. Qué se entrega en esta etapa

1. Este diagnóstico.
2. `catalogo/snapshot_tiendanube.py`: copia pública de solo lectura del catálogo, con campos no publicados en `null` (desconocido).
3. `catalogo/validar.py` y `catalogo/REPORTE_VALIDACION.md`: duplicados, SKU faltantes, imágenes faltantes o sintéticas, precios, stock y cruce con el PDF.
4. `catalogo/ESQUEMA.md`: mapeo de campos para la importación.

Lo que **no** está hecho todavía: diseño visual (faltan los tres SVG), tema, integraciones, pruebas de compra, dominio.

## 4. Qué hace falta para avanzar

| Bloquea | Pedido |
| --- | --- |
| Diseño fiel | Los tres SVG: `Masherr_Web_Desktop.svg`, `Masherr_Web_Mobile.svg`, `Masherr_Ficha_Producto.svg` (no llegaron en el mensaje). |
| Ruta A | Plan de Tiendanube vigente y acceso al admin (usuario colaborador con permiso de diseño), o confirmación de que el plan incluye FTP. |
| Importación | Exportación CSV de productos desde el admin (Productos → Exportar), con imágenes. |
| Fotos | Fotos reales del local, del equipo y de productos, con permiso de uso. |
| Textos | Fecha de fundación, políticas de cambios, envíos y pagos vigentes, horarios. |
| Dominio | Más adelante: nombre, proveedor y acceso DNS. No se toca nada sin autorización. |

## Fuentes

- Ayuda Tiendanube, personalización del diseño (CSS en todos los planes, FTP desde Plan Impulso): https://ayuda.tiendanube.com/es_AR/diseno/guia-personalizar-el-diseno-de-tu-tiendanube
- Ayuda Tiendanube, qué es la Storefront API: https://ayuda.tiendanube.com/es_AR/socios-tecnologicos/que-es-la-storefront-api-de-tiendanube-y-para-que-sirve
