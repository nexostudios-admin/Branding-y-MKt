// Exporta tarjeta.html a PDF (imprenta, con sangrado) y PNG del dorso al corte. Uso: node exportar_tarjeta.js
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ deviceScaleFactor: 4 });
  await p.goto('file://' + path.join(__dirname, 'tarjeta.html'));
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: path.join(__dirname, 'Masherr_Tarjeta_Impresion_90x50mm.pdf'), printBackground: true, preferCSSPageSize: true });
  const hs = await p.$$('.p');
  const box = await hs[1].boundingBox();
  const mm = box.width / 104;
  await p.screenshot({ path: path.join(__dirname, 'Masherr_Tarjeta_Dorso.png'), clip: { x: box.x + 7 * mm, y: box.y + 7 * mm, width: 90 * mm, height: 50 * mm } });
  await b.close();
})();
