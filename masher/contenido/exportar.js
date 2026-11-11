// Exporta plan_videos.html a PDF y avisa si algún contenido no entra en su página.
// Uso: node exportar.js [prefijo-capturas]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.join(__dirname, 'plan_videos.html'));
  await p.evaluate(() => document.fonts.ready);
  const over = await p.$$eval('.cuerpo', cs => cs.map((c, i) => (c.scrollHeight > c.clientHeight + 1 ? i + 2 : null)).filter(Boolean));
  console.log('páginas que desbordan:', over.length ? over : 'ninguna');
  await p.pdf({ path: path.join(__dirname, 'Masherr_Plan_15_Reels.pdf'), printBackground: true, preferCSSPageSize: true });
  if (process.argv[2]) {
    await p.emulateMedia({ media: 'print' });
    const hs = await p.$$('.hoja');
    for (const i of [0, 1, 2, 3, 6, 18, 19]) await hs[i].screenshot({ path: `${process.argv[2]}-${i + 1}.png` });
  }
  await b.close();
})();
