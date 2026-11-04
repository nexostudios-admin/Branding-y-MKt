// Uso: node render.js catalogo.html Masher_Catalogo_2026.pdf [prefijo-capturas]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 900, height: 1200 } });
  await p.goto('file://' + path.resolve(process.argv[2]));
  await p.waitForSelector('body[data-listo="1"]');
  await p.pdf({ path: process.argv[3], printBackground: true, preferCSSPageSize: true });
  if (process.argv[4]) {
    await p.emulateMedia({ media: 'print' });
    const hojas = await p.$$('.hoja');
    for (const i of [0, 1, 2, 3, hojas.length - 1]) await hojas[i].screenshot({ path: `${process.argv[4]}-${i + 1}.png` });
    console.log('hojas', hojas.length);
  }
  await b.close();
})();
