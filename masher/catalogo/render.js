// Uso: node render.js            → catálogo completo + un PDF por tomo en pdf/
//      node render.js capturas/  → además guarda capturas PNG de cada tapa y primera página
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const NOMBRES = ['Completo', '1_Herramientas_electricas', '2_Discos_brocas_accesorios', '3_Soldadura_neumatica',
  '4_Herramientas_de_mano_medicion', '5_Taller_obra_jardin', '6_Ferreteria_quimicos_seguridad'];
(async () => {
  const shots = process.argv[2];
  fs.mkdirSync(path.join(__dirname, 'pdf'), { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 900, height: 1200 } });
  for (let g = 0; g < NOMBRES.length; g++) {
    await p.goto('file://' + path.join(__dirname, 'catalogo.html') + (g ? `?g=${g}` : ''));
    await p.waitForSelector('body[data-listo="1"]');
    const out = path.join(__dirname, 'pdf', `Masherr_Catalogo_${NOMBRES[g]}.pdf`);
    await p.pdf({ path: out, printBackground: true, preferCSSPageSize: true });
    const hojas = await p.$$('.hoja');
    const desbordes = await p.$$eval('.cuerpo', cs => cs.filter(c => c.scrollHeight > c.clientHeight + 1).length);
    console.log(path.basename(out), hojas.length, 'páginas', desbordes ? `· ${desbordes} DESBORDES` : '');
    if (shots) for (const i of [0, 1, hojas.length - 1]) await hojas[i].screenshot({ path: path.join(shots, `g${g}-${i + 1}.png`) });
  }
  await b.close();
})();
