# El Motivo · Caja de herramientas

Gráfica en pantalla para el bloque 2 de El Motivo. Es una sola página 16:9 (1920×1080) que se escala a la ventana.

- **Online:** https://claude.ai/artifact/LayefcwvbcTUbwavWuoirr (privada hasta que se comparta).
- **Local / OBS:** `El_Motivo_caja_de_herramientas.html`. Se abre con doble clic en Chrome, o como fuente de navegador en OBS (archivo local, 1920×1080). No necesita login.

## Cómo se usa

1. Tecla `E`: abre el panel de producción. Se cargan el invitado y las respuestas cortas de las seis herramientas. Todo queda guardado en ese navegador.
2. Tecla `E` de nuevo: se oculta el panel y queda solo la gráfica.
3. Durante la grabación:

| Tecla | Qué hace |
| --- | --- |
| `1`–`6` | Esa herramienta en grande |
| `→` `←` | Siguiente / anterior |
| `0` | Vista general con las seis |
| `Z` | Zócalo de la herramienta actual, para ir sobre la cámara |
| `C` | Cierre del bloque: las seis + "¿Cuál es tu motivo?" |
| `X` | Pantalla limpia |
| `B` | Fondo: negro, verde chroma o transparente |
| `F` | Pantalla completa |
| `R` | Vuelve a cerrar las seis |

En el Stream Deck: acción "Tecla de acceso directo" con estas teclas, con la ventana de la caja en foco.

## Fondos

- **Negro:** para poner la caja a pantalla completa.
- **Transparente:** en OBS como fuente de navegador, el zócalo queda encima de la cámara.
- **Verde:** para capturar la ventana de Chrome y recortar con chroma.

## Pasar los datos a otra compu

Cada navegador guarda sus propios datos. Para cargar las respuestas en la compu de técnica: "Copiar datos" en una, pegarlos en el cuadro de la otra y "Cargar datos pegados".

## Editar

Se edita `fuente.html` y se corre `python3 build.py`, que arma la versión online (`caja-artifact.html`) y la local.
