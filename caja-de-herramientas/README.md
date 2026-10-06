# El Motivo · Caja de herramientas

Gráfica en pantalla para el bloque 2 de El Motivo. Es una sola página 16:9 (1920×1080) que se escala a la ventana.

- **Página web:** https://nexostudios-admin.github.io/Branding-y-MKt/caja-de-herramientas/ (cuando GitHub Pages esté activado: Settings → Pages → Deploy from a branch → `master` / root).
- **Online en Claude:** https://claude.ai/artifact/LayefcwvbcTUbwavWuoirr (privada hasta que se comparta).
- **En el estudio:** `El_Motivo_caja_de_herramientas.html`, abierto en Chrome en la compu de vMix. No necesita login.

## Armado con vMix: dos ventanas

Se abre el mismo archivo dos veces en Chrome. Las dos ventanas se sincronizan solas.

1. **Ventana de salida:** el link termina en `#salida` (por ejemplo `file:///C:/.../El_Motivo_caja_de_herramientas.html#salida`). Muestra solo la gráfica, sin panel ni mouse. Se pone a pantalla completa (`F`) en un monitor libre, o se deja en una ventana de 1920×1080.
2. **Ventana de control:** el link termina en `#control`. Tiene el panel abierto para cargar las respuestas y los botones para cambiar lo que se ve.
3. **En vMix:** Add Input → Desktop Capture, y se elige la ventana o el monitor de salida.
   - Caja a pantalla completa: fondo **negro**, input directo al programa.
   - Zócalo sobre la cámara de Fede: fondo **verde** y, en las opciones del input, Colour Key / Chroma Key en verde. Se usa como overlay.

Las teclas funcionan en cualquiera de las dos ventanas, la que esté en foco.

## Teclas

| Tecla | Qué hace |
| --- | --- |
| `1`–`6` | Esa herramienta en grande |
| `→` `←` | Siguiente / anterior |
| `0` | Vista general con las seis |
| `Z` | Zócalo de la herramienta actual |
| `C` | Cierre del bloque: las seis + "¿Cuál es tu motivo?" |
| `X` | Pantalla limpia |
| `B` | Fondo: negro, verde o transparente |
| `E` | Panel de producción (no se abre en la ventana de salida) |
| `F` | Pantalla completa |
| `R` | Vuelve a cerrar las seis |

Con el Stream Deck: acción "Tecla de acceso directo", con la ventana de control en foco. Si el Stream Deck ya maneja vMix, conviene dejar estas teclas en una página aparte.

## Un invitado por programa

En el panel (`E`), en "Invitado":

- **Nuevo invitado:** arranca una caja vacía. Cada invitado queda guardado en la lista.
- **Invitado en pantalla:** se elige de la lista cuál sale.
- **Copiar link de este invitado** (solo en la página web): un link con todas las respuestas adentro. Se abre en la compu de vMix y el invitado queda cargado ahí.
- **Borrar este invitado:** pide tocar dos veces.

## Pasar los datos a otra compu

Cada navegador guarda sus propios datos. Para cargar las respuestas en la compu de técnica: "Copiar datos" en una, pegarlos en el cuadro de la otra y "Cargar datos pegados".

## Editar

Se edita `fuente.html` y se corre `python3 build.py`, que arma la versión online (`caja-artifact.html`) y la local.
