// Exporta cada pieza a PNG en alta calidad (2x) y a PDF vectorial (editable en Illustrator). Uso: node exportar.js
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
(async () => {
  const out = path.join(__dirname, 'salida');
  fs.mkdirSync(out, { recursive: true });
  const piezas = fs.readFileSync(path.join(__dirname, 'piezas.txt'), 'utf8').trim().split('\n').map(l => l.split('|'));
  const b = await chromium.launch();
  for (const [nombre, tipo] of piezas) {
    const w = 1080, h = tipo === 'story' ? 1920 : 1350;
    const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 2 });
    await p.goto('file://' + path.join(__dirname, nombre + '.html'), { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    const s = await p.$('section');
    await s.screenshot({ path: path.join(out, `Masherr_${nombre}.png`) });
    await p.pdf({ path: path.join(out, `Masherr_${nombre}.pdf`), width: `${w}px`, height: `${h}px`, printBackground: true, pageRanges: '1' });
    await p.close();
  }
  await b.close();
})();
