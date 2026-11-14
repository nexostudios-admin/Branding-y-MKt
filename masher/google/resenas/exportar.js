// Exporta la tarjeta y el cartel de reseñas a PDF (imprenta) y PNG (vista / WhatsApp). Uso: node exportar.js
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ deviceScaleFactor: 4 });
  const piezas = [['tarjeta_resenas.html', 'Masherr_Tarjeta_Resenas_90x50mm'], ['cartel_resenas.html', 'Masherr_Cartel_Resenas_A5']];
  for (const [html, nombre] of piezas) {
    await p.emulateMedia({ media: 'screen' });
    await p.goto('file://' + path.join(__dirname, html));
    await p.evaluate(() => document.fonts.ready);
    await p.pdf({ path: path.join(__dirname, nombre + '.pdf'), printBackground: true, preferCSSPageSize: true });
    await p.emulateMedia({ media: 'print' });
    const hs = await p.$$('.p');
    for (let i = 0; i < hs.length; i++) {
      const suf = hs.length > 1 ? (i ? '_dorso' : '_frente') : '';
      await hs[i].screenshot({ path: path.join(__dirname, nombre + suf + '.png') });
    }
  }
  await b.close();
})();
