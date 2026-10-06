# El Motivo · Caja de herramientas

Una sola página con tres modos, según cómo termina el link:

| Link | Para quién | Qué muestra |
| --- | --- | --- |
| sin nada al final | El público | La caja de cada invitado: sus seis herramientas, el top 3 y el cierre ("¿Cuál es tu motivo?", su yo del pasado y del futuro). Solo aparecen los invitados marcados como "Mostrar en la página pública". |
| `#control` | Producción | La gráfica de TV y el panel para cargar todo. |
| `#salida` | vMix | Solo la gráfica 16:9, sin panel ni mouse. |

- **Online:** https://claude.ai/artifact/LayefcwvbcTUbwavWuoirr (privada hasta que se comparta desde el menú Compartir).
- **Archivo local de respaldo:** `El_Motivo_caja_de_herramientas.html` (sin guardado online).

## Cargar un invitado y guardarlo online

1. Abrir el link con `#control`. En "Invitado": elegirlo o tocar "Nuevo invitado".
2. Completar las seis herramientas (título, guía, respuesta corta, datos), el top 3 y el cierre.
3. Tildar "Mostrar en la página pública" cuando ya se pueda ver.
4. **Guardar en la página.** La página pública y las otras ventanas se actualizan solas.

No guardar durante la grabación: la ventana de salida se recarga.

Lo que se edita y no se guarda queda como borrador en ese navegador ("Hay cambios sin guardar"). "Descartar cambios" vuelve a lo guardado.

Si guardar no está disponible (archivo local, o el link compartido como público), "Copiar datos" y pasárselos a Claude para publicarlos.

## Armado con vMix

En la compu de vMix, dos ventanas de Chrome con el mismo link: una con `#control` y otra con `#salida`. Se sincronizan solas. En vMix: Add Input → Desktop Capture → la ventana o el monitor de salida.

- Pantalla completa: fondo **negro**.
- Zócalo sobre la cámara: fondo **verde** y Chroma Key en ese input.

## Teclas (en `#control` o `#salida`)

| Tecla | Qué hace |
| --- | --- |
| `1`–`6` | Esa herramienta en grande |
| `→` `←` | Siguiente / anterior |
| `0` | Vista general con las seis |
| `Z` | Zócalo de la herramienta actual |
| `T` | Top 3: abre la placa y cada toque descubre uno, del 3 al 1 |
| `C` | Cierre de la caja: las seis + "¿Cuál es tu motivo?" |
| `Y` | Qué le diría a su yo del pasado y del futuro |
| `X` | Pantalla limpia |
| `B` | Fondo: negro, verde o transparente |
| `E` | Panel de producción (solo en `#control`) |
| `F` | Pantalla completa |
| `R` | Vuelve a cerrar las seis |

## Editar el código

Se edita `fuente.html` y se corre `python3 build.py`, que arma la versión online (`caja-artifact.html`), el archivo local y `index.html`. Los datos publicados viven en `datos/caja.json`.
