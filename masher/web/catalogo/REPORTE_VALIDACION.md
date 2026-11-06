# Reporte de validación del catálogo

Fuente: https://masherrferreteria.mitiendanube.com · copia pública de solo lectura del 2026-11-06.
No es una exportación autorizada: confirmar conteos con el admin de Tiendanube antes de importar.

## Conteos

| Dato | Cantidad |
| --- | --- |
| Productos publicados (sitemap) | 244 |
| Variantes | 249 |
| Productos con más de una variante | 2 |
| Errores de lectura | 0 |
| Páginas de categoría e institucionales | 75 |
| Productos en el PDF CATÁLOGO TN | 436 |
| Del PDF encontrados en la tienda (por nombre) | 215 |
| Del PDF sin coincidencia en la tienda | 221 |

Monedas: {'ARS': 244}

## Problemas que bloquean o afectan la importación

| Control | Productos | Qué hacer |
| --- | --- | --- |
| Sin SKU en alguna variante | 244 | Cargar SKU único: es la clave para búsqueda, importación y redirecciones. |
| SKU repetido | 0 | Corregir antes de importar. |
| Nombre repetido | 2 | Revisar si son duplicados o variantes de un mismo producto. |
| Sin imagen | 0 | Pedir foto oficial o propia. |
| Imagen con nombre de generador de IA | 2 | Reemplazar por foto real del producto (el brief no admite imágenes sintéticas). |
| Sin precio o precio 0 | 0 | Desactivar compra hasta tener precio. |
| Sin stock / no disponible | 0 | Mostrar “Sin stock” y bloquear compra. |
| Stock sin controlar (null) | 3 | Definir si se controla stock; si no, riesgo de sobreventa. |
| Solo consulta (sin precio visible) | 0 | Mantener como “Consultar”. |
| Sin descripción | 0 | Completar. |
| Sin marca como dato propio | 243 | La marca está solo en el nombre; cargarla como campo para poder filtrar. |

### Sin SKU
- Adaptador – M14 a Mandril - AD-CDA Aliafor
- Adhesivo de contacto x 1/2lt. Fortex
- Adhesivo de contacto x 1lt. Fortex
- Adhesivo de contacto x 4lt. Fortex
- Amoladora angular 115mm. - 650W. - 11565 Vanden
- Amoladora Angular 115mm. - 700W. - DWE 4010 DeWalt
- Amoladora Angular 115mm. - 750W. - DWE 750 DeWalt
- Amoladora Angular 115mm. - 800W. - DWE 4020 DeWalt
- Amoladora Angular 115mm. - 950W. - NEMEA11115 Nebraska
- Amoladora angular 125mm. - 900W. - GWS 9-125 Bosch
- Amoladora Angular 180mm. - 2000W. - NEMEA180200 Nebraska
- Amoladora Angular 180mm. - 2200W. - DWE491 DeWalt
- Amoladora Angular 180mm. - 2700W. - DWE4577N DeWalt
- Amoladora Inalámbrica 20V Brushless 115mm Nebraska 4.0Ah + Set Discos Flap + Pack Corte Bosch
- Amoladora angular inalambrica Brushless 115mm. - 20V. - c/cargador y 2 baterias 4Ah. - 85031 Isard
- … y 229 más

### Nombres repetidos
- espuma de poliuretano x 500ml homey: 2 fichas
- pistola de pintar hvlp con compresor esgn50001 4 emtop: 2 fichas

### Imágenes con nombre de generador de IA
- Cola Sintética Vinílica A-20 Fortex – 1/4 kg, 1/2 kg, 1 kg y 6 kg
- Pack de Puntas Phillips para Atornillar Venturo (Aliafor) – PH1, PH2 y PH3 x 50 mm – 10 Unidades

### Sin stock o no disponibles

### Precio distinto entre el PDF y la tienda
- Taladro Percutor 13mm. - 1050W. - NEMETP1050: PDF $90.000 · tienda $93.000
- Lustrapulidora 180mm. - 1400W. - NEMELP09180: PDF $172.500 · tienda $172.000
- Carro de Herramientas Modular Packout – 3 Módulos: PDF $680.000 · tienda $800.000
- Bomba de agua periferica 1/2HP: PDF $54.000 · tienda $53.000
- Bomba de agua centrifuga 1/2HP: PDF $120.000 · tienda $161.500
- Bomba de agua centrifuga 3/4HP: PDF $140.000 · tienda $137.000
- Adhesivo de contacto x 4lt.: PDF $58.000 · tienda $56.000
- Adhesivo de contacto x 1/2lt.: PDF $10.000 · tienda $9.000
- Lubricante seco WD-40 x 226grs.: PDF $23.500 · tienda $235.000

### Del PDF sin coincidencia en la tienda (muestra)
- Alambre MIG 0,90mm. x 1kg. - B43F91 (Foxtter)
- Alambre MIG 0,90mm. x 5kgs. - B43F09 (Foxtter)
- Alambre MIG 0,90mm. x 15kgs. - B4309 (Foxtter)
- Alambre MIG 0,80mm. x 1kg. - B43F81 (Foxtter)
- Alambre MIG 0,80mm. x 5kgs. - B43F08 (Foxtter)
- Alambre MIG 0,80mm. x 15kgs. - B4308 (Foxtter)
- Alambre MIG Flux 0,80mm. sin gas x 1kg. - 80-722 (Isard)
- Alambre MIG Flux 0,90mm. sin gas x 1kg. - 80-723 (Isard)
- Electrodo E6013 2,00mm. x 1kg. (Esab OK)
- Electrodo E6013 2,00mm. x cajon de 20kg. (Esab OK)
- Electrodo E6013 2,50mm. x 1kg. (Esab OK)
- Electrodo E6013 2,50mm. x cajon de 20kg. (Esab OK)
- Electrodo E6013 3,25mm. x 1kg. (Esab OK)
- Electrodo E6013 3,25mm. x cajon 20kg. (Esab OK)
- Electrodo 13-A - E6013 2,00mm. x 1kg. (Conarco)
- … y 206 más

## Categorías en la tienda

| Categoría | Productos |
| --- | --- |
| Adhesivos y Selladores | 7 |
| Agua Limpieza > Aspiradoras | 3 |
| Agua Limpieza > Bombas | 5 |
| Agua Limpieza > Hidrolavadoras | 3 |
| Bolsos | 1 |
| Calefactor | 2 |
| Cinceles | 2 |
| Discos de corte | 5 |
| Espumas | 3 |
| Herramientas | 2 |
| Herramientas > Cajas de herramientas | 8 |
| Herramientas > De medición | 18 |
| Herramientas > De medición > Niveles | 1 |
| Herramientas > Equipos de pintar | 1 |
| Herramientas > Escaleras | 2 |
| Herramientas > Herramientas Electricas > Amoladoras | 16 |
| Herramientas > Herramientas Electricas > Atornilladores | 3 |
| Herramientas > Herramientas Electricas > Cepilladoras | 3 |
| Herramientas > Herramientas Electricas > Equipos de pintar e infladores | 4 |
| Herramientas > Herramientas Electricas > Lijadoras | 3 |
| Herramientas > Herramientas Electricas > Minitornos | 5 |
| Herramientas > Herramientas Electricas > Pistolas de calor | 2 |
| Herramientas > Herramientas Electricas > Pulidoras Eléctricas | 2 |
| Herramientas > Herramientas Electricas > Rotomartillos | 3 |
| Herramientas > Herramientas Electricas > Sierras | 12 |
| Herramientas > Herramientas Electricas > Taladros | 14 |
| Herramientas > Herramientas Electricas > Termofusoras | 1 |
| Herramientas > Herramientas manuales | 14 |
| Herramientas > Herramientas manuales > Alicates y Pinzas | 12 |
| Herramientas > Herramientas manuales > Bocallaves y Accesorios | 1 |
| Herramientas > Herramientas manuales > Destornilladores | 3 |
| Herramientas > Herramientas manuales > Llaves | 7 |
| Herramientas > Herramientas manuales > Morsas | 1 |
| Herramientas > Herramientas manuales > Sets de herramientas | 2 |
| Herramientas > Herramientas manuales > Sets de herramientas > Set de pinzas | 3 |
| Herramientas > Herramientas manuales > Sets de herramientas > Sets de llaves | 9 |
| Herramientas > Herramientas manuales > Sets de herramientas > Sets destornillador | 3 |
| Herramientas > Inalámbricas a bateria | 1 |
| Herramientas > Inalámbricas a bateria > Atornilladores | 1 |
| Jardin > Cortadoras de cesped | 2 |
| Maquinas > Compresores | 4 |
| Maquinas > Soldadoras | 7 |
| Mechas - Brocas | 4 |
| Muebles para el hogar | 1 |
| Ofertas | 3 |
| Productos | 21 |
| Puntas y adaptadores | 14 |

## Campos que la tienda no publica (quedan como desconocidos)

Dimensiones, garantía, accesorios incluidos y atributos técnicos estructurados. Pedirlos en la exportación del admin o cargarlos en Tiendanube; no inferirlos.
