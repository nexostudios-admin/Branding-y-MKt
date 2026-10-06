// Exporta los PNG transparentes 1920×1080 y las vistas previas.
// Uso: node exportar.js [css con las fuentes, si la compu no tiene internet]
const path = require('path'), fs = require('fs');
const { chromium } = require(process.env.PLAYWRIGHT || '/opt/node-tools/node_modules/playwright');
const aqui = __dirname;
const slug = s => s.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  await p.goto('file://' + path.join(aqui, 'El_Motivo_grafica.html') + '#png');
  if (process.argv[2]) await p.addStyleTag({ path: process.argv[2] });
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(800);
  const salida = path.join(aqui, 'png'); fs.mkdirSync(salida, { recursive: true });
  const toma = async (nombre, o) => { await p.evaluate(o => window.__mostrar(o), o); await p.waitForTimeout(150); await p.screenshot({ path: path.join(salida, nombre), omitBackground: true }); };
  const n = await p.evaluate(() => ({ z: document.querySelectorAll('#p-personas .item').length, o: document.querySelectorAll('#p-overs .item').length }));
  const nombres = await p.evaluate(() => ({
    z: Array.from(document.querySelectorAll('[id^=pn-]')).map(i => i.value),
    o: Array.from(document.querySelectorAll('[id^=ot-]')).map(i => i.value.replace(/\*/g, ''))
  }));
  await toma('mosca-sin-hora.png', { mosca: true, relojes: false });
  for (let i = 0; i < n.z; i++) await toma(`zocalo-${i + 1}-${slug(nombres.z[i])}.png`, { mosca: false, zocalo: i });
  for (let i = 0; i < n.o; i++) await toma(`oversize-${i + 1}-${slug(nombres.o[i]).slice(0, 40)}.png`, { mosca: false, over: i });
  await b.close();
  console.log('PNG listos en', salida);
})();
