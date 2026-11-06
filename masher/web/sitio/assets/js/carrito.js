/* Masherr · carrito: edita cantidades, recalcula con el catálogo vigente y arma el pedido para WhatsApp. */
(function () {
  'use strict';
  const { carrito, cargarCatalogo, resolver, fmt, esc, icono, wa, img, CFG, ROOT } = window.M;
  const app = document.getElementById('carrito-app');
  let CAT, datos = { nombre: '', entrega: 'retiro', direccion: '', localidad: '', cp: '', pago: '', factura: '', comentarios: '' };
  try { datos = { ...datos, ...JSON.parse(sessionStorage.getItem('masherr_datos') || '{}') }; } catch (e) {}

  function lineas() {
    return carrito.items().map(i => ({ ...i, r: resolver(CAT, i.v) }));
  }

  function pintar() {
    const ls = lineas();
    const validas = ls.filter(l => l.r && l.r.v.disponible);
    const invalidas = ls.filter(l => !l.r || !l.r.v.disponible);
    if (!ls.length) {
      app.innerHTML = `<div class="vacio"><h2>Tu carrito está vacío</h2><p>Buscá lo que necesitás en la tienda y agregalo para armar tu pedido.</p><p><a class="boton" href="${ROOT}tienda/">Ir a la tienda</a></p></div>`;
      return;
    }
    const total = validas.reduce((a, l) => a + l.r.v.precio * l.c, 0);
    app.innerHTML = `<div class="carrito-layout">
      <section aria-labelledby="t-items"><h2 id="t-items" class="sr">Productos</h2>
        ${invalidas.length ? `<div class="aviso" role="alert" style="margin-bottom:16px">${icono('info')}<span>${invalidas.length === 1 ? 'Un producto ya no está' : invalidas.length + ' productos ya no están'} disponible${invalidas.length === 1 ? '' : 's'}. No se incluye${invalidas.length === 1 ? '' : 'n'} en el pedido.</span></div>` : ''}
        <ul class="items">${ls.map(l => {
          if (!l.r) return `<li class="item"><div></div><div><h2>Producto no disponible</h2><button class="quitar" type="button" data-quitar="${l.v}">${icono('papelera')}Quitar</button></div></li>`;
          const { p, v } = l.r;
          const max = v.stock != null ? v.stock : 999;
          return `<li class="item">
            ${p.imgs[0] ? `<img src="${img(p.imgs[0])}" alt="" width="84" height="84" loading="lazy">` : '<div></div>'}
            <div>
              <h2><a href="${ROOT}producto/${p.slug}/">${esc(p.nombre)}</a></h2>
              ${v.nombre ? `<div class="ayuda">Opción: ${esc(v.nombre)}</div>` : ''}
              <div class="ayuda">${fmt(v.precio)} c/u${!v.disponible ? ' · <span class="stock-no">Sin stock</span>' : v.stock != null && l.c > v.stock ? ` · <span class="stock-no">Hay ${v.stock} en stock</span>` : ''}</div>
              <div class="controles">
                <div class="cantidad"><button type="button" data-mod="${v.id}" data-d="-1" aria-label="Restar uno de ${esc(p.nombre)}">${icono('menos')}</button>
                  <label class="sr" for="c-${v.id}">Cantidad de ${esc(p.nombre)}</label><input id="c-${v.id}" type="number" inputmode="numeric" min="1" max="${max}" value="${l.c}" data-cant="${v.id}">
                  <button type="button" data-mod="${v.id}" data-d="1" aria-label="Sumar uno de ${esc(p.nombre)}">${icono('mas')}</button></div>
                <button class="quitar" type="button" data-quitar="${v.id}">${icono('papelera')}Quitar</button>
                <span class="subtotal">${v.disponible ? fmt(v.precio * l.c) : '—'}</span>
              </div>
            </div></li>`;
        }).join('')}</ul>
        <p style="margin-top:16px"><a href="${ROOT}tienda/">${icono('anterior')} Seguir comprando</a></p>
      </section>
      <aside class="resumen" aria-labelledby="t-res">
        <h2 id="t-res">Tu pedido</h2>
        <div class="total"><span>Total estimado</span><span>${fmt(total)}</span></div>
        <p class="ayuda" style="margin:0">Precios publicados al ${esc(CFG.fecha_precios)}. Envío no incluido. Confirmamos precio, stock y forma de pago por WhatsApp antes de cobrar.</p>
        <form id="form-pedido" class="form-grid" novalidate>
          <div class="campo"><label for="f-nombre">Nombre y apellido *</label><input id="f-nombre" name="nombre" autocomplete="name" required value="${esc(datos.nombre)}"><span class="error" id="e-nombre" hidden>Completá tu nombre.</span></div>
          <fieldset class="radio-grupo"><legend class="campo" style="font-weight:700;font-size:14px;margin-bottom:6px">Entrega</legend>
            <label><input type="radio" name="entrega" value="retiro" ${datos.entrega !== 'envio' ? 'checked' : ''}> Retiro en el local</label>
            <label><input type="radio" name="entrega" value="envio" ${datos.entrega === 'envio' ? 'checked' : ''}> Envío (costo a coordinar)</label>
          </fieldset>
          <div id="campos-envio" class="form-grid" ${datos.entrega === 'envio' ? '' : 'hidden'}>
            <div class="campo"><label for="f-dir">Dirección *</label><input id="f-dir" name="direccion" autocomplete="street-address" value="${esc(datos.direccion)}"><span class="error" id="e-dir" hidden>Completá la dirección de envío.</span></div>
            <div class="campo"><label for="f-loc">Localidad</label><input id="f-loc" name="localidad" autocomplete="address-level2" value="${esc(datos.localidad)}"></div>
            <div class="campo"><label for="f-cp">Código postal</label><input id="f-cp" name="cp" autocomplete="postal-code" inputmode="numeric" value="${esc(datos.cp)}"></div>
          </div>
          <div class="campo"><label for="f-pago">Forma de pago preferida</label><select id="f-pago" name="pago">
            ${['', 'Efectivo', 'Transferencia', 'Tarjeta', 'Mercado Pago', 'A coordinar'].map(o => `<option value="${o}" ${datos.pago === o ? 'selected' : ''}>${o || 'Elegí una opción'}</option>`).join('')}</select>
            <span class="ayuda">Te confirmamos las opciones disponibles por WhatsApp.</span></div>
          <div class="campo"><label for="f-fac">Factura (opcional)</label><input id="f-fac" name="factura" placeholder="Ej.: Factura A, CUIT 30-…" value="${esc(datos.factura)}"></div>
          <div class="campo"><label for="f-com">Comentarios</label><textarea id="f-com" name="comentarios">${esc(datos.comentarios)}</textarea></div>
          <button class="boton wa ancho" type="submit" ${validas.length ? '' : 'disabled'}>${icono('whatsapp')}Enviar pedido por WhatsApp</button>
          <p class="ayuda" style="margin:0">Se abre WhatsApp con el pedido armado para ${esc(CFG.whatsapp_visible)}. El pedido queda confirmado cuando te respondemos.</p>
          <button class="quitar" type="button" data-vaciar>Vaciar carrito</button>
        </form>
      </aside></div>`;
  }

  function mensaje(f) {
    const ls = lineas().filter(l => l.r && l.r.v.disponible);
    const total = ls.reduce((a, l) => a + l.r.v.precio * l.c, 0);
    const d = Object.fromEntries(new FormData(f));
    const r = [`Hola Masherr, quiero hacer este pedido:`, ''];
    ls.forEach(l => r.push(`• ${l.c} × ${l.r.p.nombre}${l.r.v.nombre ? ' (' + l.r.v.nombre + ')' : ''}${l.r.v.sku ? ' [SKU ' + l.r.v.sku + ']' : ''} — ${fmt(l.r.v.precio)} c/u = ${fmt(l.r.v.precio * l.c)}`));
    r.push('', `Total estimado: ${fmt(total)} (precios web al ${CFG.fecha_precios}, envío no incluido)`, '', `Nombre: ${d.nombre}`);
    r.push(d.entrega === 'envio' ? `Entrega: envío a ${d.direccion}${d.localidad ? ', ' + d.localidad : ''}${d.cp ? ' (CP ' + d.cp + ')' : ''}` : 'Entrega: retiro en el local');
    if (d.pago) r.push(`Pago preferido: ${d.pago}`);
    if (d.factura) r.push(`Factura: ${d.factura}`);
    if (d.comentarios) r.push(`Comentarios: ${d.comentarios}`);
    r.push('', '¿Me confirman stock, precio final y cómo seguimos?');
    return r.join('\n');
  }

  function guardarDatos(f) {
    datos = { ...datos, ...Object.fromEntries(new FormData(f)) };
    try { sessionStorage.setItem('masherr_datos', JSON.stringify(datos)); } catch (e) {}
  }

  app.addEventListener('click', e => {
    const m = e.target.closest('[data-mod]');
    if (m) { const it = carrito.items().find(i => i.v === +m.dataset.mod); const r = resolver(CAT, +m.dataset.mod);
      const max = r && r.v.stock != null ? r.v.stock : 999; if (it) carrito.cambiar(it.v, Math.min(max, it.c + +m.dataset.d)); }
    const q = e.target.closest('[data-quitar]'); if (q) carrito.quitar(+q.dataset.quitar);
    if (e.target.closest('[data-vaciar]') && confirm('¿Vaciar el carrito?')) carrito.vaciar();
  });
  app.addEventListener('change', e => {
    if (e.target.dataset.cant) { const r = resolver(CAT, +e.target.dataset.cant); const max = r && r.v.stock != null ? r.v.stock : 999;
      carrito.cambiar(+e.target.dataset.cant, Math.min(max, Math.floor(+e.target.value) || 1)); }
    if (e.target.name === 'entrega') { document.getElementById('campos-envio').hidden = e.target.value !== 'envio'; }
    if (e.target.form && e.target.form.id === 'form-pedido') guardarDatos(e.target.form);
  });
  app.addEventListener('submit', e => {
    if (e.target.id !== 'form-pedido') return;
    e.preventDefault();
    const f = e.target; guardarDatos(f);
    const nom = f.nombre, dir = f.direccion, envio = f.entrega.value === 'envio';
    let ok = true;
    const marcar = (campo, err, mal) => { campo.setAttribute('aria-invalid', mal); campo.setAttribute('aria-describedby', mal ? err : ''); document.getElementById(err).hidden = !mal; if (mal && ok) campo.focus(); ok = ok && !mal; };
    marcar(nom, 'e-nombre', !nom.value.trim());
    marcar(dir, 'e-dir', envio && !dir.value.trim());
    if (!ok) return;
    window.open(wa(mensaje(f)), '_blank', 'noopener');
  });
  document.addEventListener('carrito', () => CAT && pintar());
  document.querySelector('.wa-flotante')?.remove();  // en el carrito el botón de WhatsApp es el del pedido
  app.addEventListener('input', e => { if (e.target.getAttribute('aria-invalid') === 'true' && e.target.value.trim()) {
    e.target.setAttribute('aria-invalid', 'false'); const id = e.target.getAttribute('aria-describedby'); if (id) document.getElementById(id).hidden = true; } });

  cargarCatalogo().then(c => { CAT = c; pintar(); }).catch(() => {
    app.innerHTML = `<div class="vacio" role="alert"><h2>No pudimos cargar los precios</h2><p>Revisá tu conexión y volvé a intentar.</p><button class="boton" type="button" onclick="location.reload()">Reintentar</button></div>`;
  });
})();
