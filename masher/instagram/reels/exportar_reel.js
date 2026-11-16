// Exporta un reel HTML a MP4 1080x1920 cuadro por cuadro.
// Uso: node exportar_reel.js <archivo.html> <salida.mp4> <segundos> <fps> [css|js] [portada_seg]
//  css: controla las animaciones CSS (document.getAnimations) · js: llama a window.cuadro(n)
const { chromium } = require('playwright');
const path = require('path'), fs = require('fs');
const { execFileSync } = require('child_process');
const [html, mp4, seg, fps, modo = 'css', portada] = process.argv.slice(2);
const N = Math.round(+seg * +fps);
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await p.goto('file://' + path.resolve(html), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  if (modo === 'css') await p.evaluate(() => document.getAnimations().forEach(a => a.pause()));
  const tmp = fs.mkdtempSync(path.join(path.dirname(path.resolve(mp4)), '.cuadros-'));
  const sec = await p.$('section');
  const ir = async (f) => modo === 'css'
    ? p.evaluate(t => document.getAnimations().forEach(a => { a.currentTime = t; }), f / +fps * 1000)
    : p.evaluate(n => window.cuadro(n), f);
  for (let f = 0; f < N; f++) {
    await ir(f);
    await sec.screenshot({ path: path.join(tmp, `f${String(f).padStart(4, '0')}.png`) });
  }
  if (portada) {
    const p2 = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 2 });
    await p2.goto('file://' + path.resolve(html), { waitUntil: 'networkidle' });
    await p2.evaluate(() => document.fonts.ready);
    const f = Math.round(+portada * +fps);
    if (modo === 'css') await p2.evaluate(t => document.getAnimations().forEach(a => { a.pause(); a.currentTime = t; }), +portada * 1000);
    else await p2.evaluate(n => window.cuadro(n), f);
    await (await p2.$('section')).screenshot({ path: mp4.replace(/\.mp4$/, ' (portada).png') });
  }
  await b.close();
  execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-framerate', String(fps), '-i', path.join(tmp, 'f%04d.png'),
    '-r', '30', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '17', '-preset', 'slow', '-movflags', '+faststart', mp4]);
  fs.rmSync(tmp, { recursive: true, force: true });
  console.log('ok', mp4, N, 'cuadros');
})();
