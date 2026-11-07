/* Masherr · ficha de producto: variantes, cantidad, galería y agregar al carrito. */
(function () {
  'use strict';
  const { carrito, fmt, toast, esc, ROOT } = window.M;
  const P = window.PRODUCTO;
  const $ = s => document.querySelector(s);
  const sel = $('#variante'), cant = $('#cant'), btn = $('#agregar');

  const variante = () => P.variantes.find(v => String(v.id) === (sel ? sel.value : String(P.variantes[0].id))) || P.variantes[0];
  function pintar() {
    const v = variante();
    $('#precio').textContent = v.precio ? fmt(v.precio) : 'Consultar precio';
    $('#sku').textContent = v.sku ? 'SKU: ' + v.sku : '';
    const st = $('#stock');
    st.className = v.disponible ? 'stock-ok' : 'stock-no';
    st.textContent = !v.disponible ? 'Sin stock' : v.stock != null && v.stock <= 5 ? `Disponible · ${v.stock} en stock` : 'Disponible';
    btn.disabled = !v.disponible;
    btn.lastChild.textContent = v.disponible ? 'Agregar al carrito' : 'Sin stock';
    if (v.stock != null) cant.max = Math.max(1, v.stock);
    if (+cant.value > +cant.max) cant.value = cant.max;
  }
  if (sel) { const primera = P.variantes.find(v => v.disponible); if (primera) sel.value = primera.id; sel.addEventListener('change', pintar); }
  pintar();

  document.querySelectorAll('[data-cant]').forEach(b => b.addEventListener('click', () => {
    cant.value = Math.max(1, Math.min(+cant.max || 999, (+cant.value || 1) + +b.dataset.cant));
  }));
  cant.addEventListener('change', () => { cant.value = Math.max(1, Math.min(+cant.max || 999, Math.floor(+cant.value) || 1)); });

  btn.addEventListener('click', () => {
    const v = variante(); if (!v.disponible) return;
    const n = Math.max(1, Math.floor(+cant.value) || 1);
    carrito.agregar(v.id, n);
    toast(`Agregaste ${n} × <b>${esc(P.nombre)}</b> <a href="${ROOT}carrito/">Ver carrito</a>`);
  });

  // Galería
  let actual = 0;
  const principal = $('#foto-principal');
  function verFoto(i) {
    if (!P.imgs.length) return;
    actual = (i + P.imgs.length) % P.imgs.length;
    const b = ROOT + P.imgs[actual];
    if (principal) { principal.src = b + '-1024-1024.webp'; principal.srcset = `${b}-480-0.webp 480w, ${b}-1024-1024.webp 1024w`; }
    document.querySelectorAll('[data-foto]').forEach(x => x.setAttribute('aria-current', +x.dataset.foto === actual));
    const lb = $('#lb-img'); if (lb) lb.src = b + '-1024-1024.webp';
  }
  document.querySelectorAll('[data-foto]').forEach(b => b.addEventListener('click', () => verFoto(+b.dataset.foto)));
  const dlg = $('#lightbox');
  $('[data-ampliar]')?.addEventListener('click', () => { if (!P.imgs.length) return; verFoto(actual); dlg.showModal(); });
  $('[data-cerrar-lb]')?.addEventListener('click', () => dlg.close());
  document.querySelectorAll('[data-lb]').forEach(b => b.addEventListener('click', () => verFoto(actual + +b.dataset.lb)));
  dlg?.addEventListener('keydown', e => { if (e.key === 'ArrowRight') verFoto(actual + 1); if (e.key === 'ArrowLeft') verFoto(actual - 1); });
  dlg?.addEventListener('click', e => { if (e.target === dlg) dlg.close(); });
})();
