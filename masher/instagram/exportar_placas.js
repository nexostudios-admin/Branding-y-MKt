// Exporta cada placa de placas.html a PNG (1080 px de ancho). Uso: node exportar_placas.js
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
(async () => {
  const out = path.join(__dirname, 'png');
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 2000 } });
  await p.goto('file://' + path.join(__dirname, 'placas.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  for (const s of await p.$$('section')) {
    const n = await s.getAttribute('data-n');
    const t = await s.getAttribute('data-t');
    await s.screenshot({ path: path.join(out, `Masherr_${t === 'story' ? 'story' : 'post'}_${n}.png`) });
  }
  await b.close();
})();
