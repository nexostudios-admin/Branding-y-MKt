// Exporta un HTML de hojas (.hoja) a PDF y avisa si algún contenido no entra en su página.
// Uso: node exportar_pdf.js entrada.html salida.pdf [prefijo-capturas]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [entrada, salida, capturas] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.join(__dirname, entrada));
  await p.evaluate(() => document.fonts.ready);
  const over = await p.$$eval('.cuerpo', cs => cs.map((c, i) => (c.scrollHeight > c.clientHeight + 1 ? `${i + 1} (${c.scrollHeight - c.clientHeight}px)` : null)).filter(Boolean));
  console.log(entrada, '→ páginas que desbordan:', over.length ? over : 'ninguna');
  await p.pdf({ path: path.join(__dirname, salida), printBackground: true, preferCSSPageSize: true });
  if (capturas) {
    await p.emulateMedia({ media: 'print' });
    const hs = await p.$$('.hoja');
    for (const i of [0, 1, hs.length - 1]) await hs[i].screenshot({ path: `${capturas}-${i + 1}.png` });
  }
  await b.close();
})();
