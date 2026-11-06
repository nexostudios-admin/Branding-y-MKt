/* Masherr · consulta para empresas: valida y arma el mensaje para WhatsApp. */
(function () {
  'use strict';
  const f = document.getElementById('form-empresas');
  f.addEventListener('submit', e => {
    e.preventDefault();
    let primero = null;
    ['nombre', 'tarea', 'productos'].forEach(n => {
      const c = f[n], mal = !c.value.trim(), id = 'err-' + n;
      c.setAttribute('aria-invalid', mal);
      let err = document.getElementById(id);
      if (mal && !err) { err = document.createElement('span'); err.className = 'error'; err.id = id; err.textContent = 'Este campo es obligatorio.'; c.after(err); }
      if (err) err.hidden = !mal;
      c.setAttribute('aria-describedby', [mal ? id : '', c.dataset.ayuda || c.getAttribute('aria-describedby')?.split(' ').filter(x => !x.startsWith('err-')).join(' ')].filter(Boolean).join(' '));
      if (mal && !primero) primero = c;
    });
    if (primero) { primero.focus(); return; }
    const d = Object.fromEntries(new FormData(f));
    const t = ['Hola Masherr, quiero pedir una cotización para empresa:', '',
      `Nombre: ${d.nombre}`, d.empresa && `Empresa: ${d.empresa}`, d.cuit && `CUIT: ${d.cuit}`, d.email && `Email: ${d.email}`, '',
      `Tarea a resolver: ${d.tarea}`, '', 'Productos y cantidades:', d.productos, '',
      d.plazo && `Plazo: ${d.plazo}`, `Entrega: ${d.entrega}`].filter(x => x !== undefined && x !== '').join('\n');
    window.open(window.M.wa(t), '_blank', 'noopener');
  });
})();
