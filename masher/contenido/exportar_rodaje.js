// Exporta guion_rodaje.html a PDF y avisa si algún contenido no entra en su página.
// Uso: node exportar_rodaje.js [prefijo-capturas]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.join(__dirname, 'guion_rodaje.html'));
  await p.evaluate(() => document.fonts.ready);
  const over = await p.$$eval('.cuerpo', cs => cs.map((c, i) => (c.scrollHeight > c.clientHeight + 1 ? `${i + 2} (${c.scrollHeight - c.clientHeight}px)` : null)).filter(Boolean));
  console.log('páginas que desbordan:', over.length ? over : 'ninguna');
  await p.pdf({ path: path.join(__dirname, 'Masherr_Guion_Rodaje.pdf'), printBackground: true, preferCSSPageSize: true });
  if (process.argv[2]) {
    await p.emulateMedia({ media: 'print' });
    const hs = await p.$$('.hoja');
    for (const i of [1, 2, 5, 7, 8, 15]) await hs[i].screenshot({ path: `${process.argv[2]}-${i + 1}.png` });
  }
  await b.close();
})();
