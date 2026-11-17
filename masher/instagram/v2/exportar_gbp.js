const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
(async () => { const b = await chromium.launch(); const out = path.join(__dirname, 'salida_gbp'); fs.mkdirSync(out, { recursive: true });
  for (const f of fs.readdirSync(path.join(__dirname, 'gbp')).filter(x => x.endsWith('.html')).sort()) {
    const p = await b.newPage({ viewport: { width: 1200, height: 900 }, deviceScaleFactor: 1 });
    await p.goto('file://' + path.join(__dirname, 'gbp', f), { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready);
    await p.evaluate(() => document.getAnimations().forEach(a => a.finish()));
    await (await p.$('section')).screenshot({ path: path.join(out, f.replace('.html', '.png')) }); await p.close(); }
  await b.close(); })();
