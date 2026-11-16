// Exporta las piezas v2: PNG en alta calidad (estado final de la animación), PDF vectorial y,
// para las historias, MP4 animado (1080x1920, 30 fps, 6 s) cuadro por cuadro.
// Uso: node exportar_v2.js [--sin-video] [filtro]
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const { execFileSync } = require('child_process');
const sinVideo = process.argv.includes('--sin-video');
const arg = (n, d) => { const i = process.argv.indexOf(n); return i > 0 ? process.argv[i + 1] : d; };
const libres = process.argv.slice(2).filter((a, i, v) => !a.startsWith('--') && !(i > 0 && ['--manifiesto', '--salida', '--parte'].includes(v[i - 1])));
const filtro = libres[0] || '';
const [parte, partes] = (arg('--parte', '1/1')).split('/').map(Number);
const M = JSON.parse(fs.readFileSync(path.join(__dirname, arg('--manifiesto', 'manifiesto.json')), 'utf8'))
  .filter(p => p.html.includes(filtro)).filter((p, i) => i % partes === parte - 1);
const OUT = path.join(__dirname, arg('--salida', 'salida'));
const sinPdf = process.argv.includes('--sin-pdf');
const FPS = 30, DUR = 6;

(async () => {
  const b = await chromium.launch();
  for (const p of M) {
    const h = p.tipo === 'historia' ? 1920 : 1350;
    const carpeta = p.carpeta
      ? path.join(OUT, p.carpeta, p.tipo === 'historia' ? '1 - Historias' : p.tipo === 'posteo' ? '' : p.nombre.split('/')[0])
      : path.join(OUT, p.tipo === 'historia' ? '1 - Historias' : p.tipo === 'carrusel' ? '2 - Carruseles' : '3 - Posteos',
        p.tipo === 'posteo' ? '' : p.tipo === 'carrusel' ? `${p.diaNombre} - ${p.nombre.split('/')[0]}` : p.diaNombre);
    fs.mkdirSync(carpeta, { recursive: true });
    const base = path.join(carpeta, p.tipo === 'carrusel' ? p.nombre.split('/')[1] : p.nombre);
    const url = 'file://' + path.join(__dirname, p.html);

    // PNG + PDF del estado final
    const pg = await b.newPage({ viewport: { width: 1080, height: h }, deviceScaleFactor: 2 });
    await pg.goto(url, { waitUntil: 'networkidle' });
    await pg.evaluate(() => document.fonts.ready);
    await pg.evaluate(() => document.getAnimations().forEach(a => a.finish()));
    await (await pg.$('section')).screenshot({ path: base + '.png' });
    if (!sinPdf) await pg.pdf({ path: base + '.pdf', width: '1080px', height: `${h}px`, printBackground: true, pageRanges: '1' });
    await pg.close();

    // MP4 animado de las historias
    if (p.tipo === 'historia' && !sinVideo) {
      const tmp = fs.mkdtempSync(path.join(OUT, '.frames-'));
      const v = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
      await v.goto(url, { waitUntil: 'networkidle' });
      await v.evaluate(() => document.fonts.ready);
      await v.evaluate(() => document.getAnimations().forEach(a => a.pause()));
      const sec = await v.$('section');
      for (let f = 0; f < FPS * DUR; f++) {
        await v.evaluate(t => document.getAnimations().forEach(a => { a.currentTime = t; }), (f / FPS) * 1000);
        await sec.screenshot({ path: path.join(tmp, `f${String(f).padStart(4, '0')}.png`) });
      }
      await v.close();
      execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-framerate', String(FPS), '-i', path.join(tmp, 'f%04d.png'),
        '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-movflags', '+faststart', base + '.mp4']);
      fs.rmSync(tmp, { recursive: true, force: true });
    }
    console.log('ok', p.dia, p.tipo, p.nombre);
  }
  await b.close();
})();
