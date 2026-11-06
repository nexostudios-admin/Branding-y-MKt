/* Masherr · listado de la tienda: búsqueda, filtros y orden guardados en la URL. */
(function () {
  'use strict';
  const { cargarCatalogo, tarjeta, esc, icono } = window.M;
  const POR_PAGINA = 24;
  const $ = s => document.querySelector(s);
  const norm = s => (s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]+/g, ' ').trim();

  const estado = () => {
    const u = new URLSearchParams(location.search);
    return { q: u.get('q') || '', cat: u.get('cat') || '', marca: u.getAll('marca'), stock: u.get('stock') === '1', orden: u.get('orden') || 'relevancia', p: Math.max(1, +u.get('p') || 1) };
  };
  function irA(e, reemplazar) {
    const u = new URLSearchParams();
    if (e.q) u.set('q', e.q); if (e.cat) u.set('cat', e.cat); e.marca.forEach(m => u.append('marca', m));
    if (e.stock) u.set('stock', '1'); if (e.orden !== 'relevancia') u.set('orden', e.orden); if (e.p > 1) u.set('p', e.p);
    const url = location.pathname + (u.toString() ? '?' + u : '');
    history[reemplazar ? 'replaceState' : 'pushState'](null, '', url);
    pintar();
  }

  let CAT;
  function filtrar(e, ignorar) {
    const tokens = norm(e.q).split(' ').filter(Boolean);
    return CAT.productos.filter(p => {
      if (ignorar !== 'cat' && e.cat && p.cat !== e.cat) return false;
      if (ignorar !== 'marca' && e.marca.length && !e.marca.includes(p.marca)) return false;
      if (e.stock && !p.disponible) return false;
      if (tokens.length) { const h = p._b; if (!tokens.every(t => h.includes(t))) return false; }
      return true;
    });
  }
  function ordenar(lista, e) {
    const tokens = norm(e.q).split(' ').filter(Boolean);
    const puntaje = p => tokens.reduce((a, t) => a + (norm(p.nombre).startsWith(t) ? 3 : 0) + (norm(p.marca).includes(t) ? 2 : 0) + (p._b.includes(' ' + t) ? 1 : 0), 0);
    const r = lista.slice();
    if (e.orden === 'precio-asc') r.sort((a, b) => a.precio - b.precio);
    else if (e.orden === 'precio-desc') r.sort((a, b) => b.precio - a.precio);
    else if (e.orden === 'nombre') r.sort((a, b) => a.nombre.localeCompare(b.nombre, 'es'));
    else if (tokens.length) r.sort((a, b) => puntaje(b) - puntaje(a));
    return r.sort((a, b) => (b.disponible - a.disponible)); // sin stock al final (sort estable)
  }

  function htmlFiltros(e) {
    const base = filtrar(e, 'cat'); const cuentaCat = {}; base.forEach(p => (cuentaCat[p.cat] = (cuentaCat[p.cat] || 0) + 1));
    const baseM = filtrar(e, 'marca'); const cuentaM = {}; baseM.forEach(p => p.marca && (cuentaM[p.marca] = (cuentaM[p.marca] || 0) + 1));
    const marcas = Object.keys(cuentaM).concat(e.marca.filter(m => !cuentaM[m])).sort((a, b) => a.localeCompare(b, 'es'));
    return `
      <fieldset class="filtro-grupo"><legend>Categoría</legend>
        <label class="opcion"><input type="radio" name="cat" value="" ${!e.cat ? 'checked' : ''}> Todas <span class="n">${base.length}</span></label>
        ${CAT.categorias.map(c => `<label class="opcion"><input type="radio" name="cat" value="${c.slug}" ${e.cat === c.slug ? 'checked' : ''}> ${esc(c.nombre)} <span class="n">${cuentaCat[c.slug] || 0}</span></label>`).join('')}
      </fieldset>
      <fieldset class="filtro-grupo"><legend>Marca</legend><div class="lista-marcas">
        ${marcas.map(m => `<label class="opcion"><input type="checkbox" name="marca" value="${esc(m)}" ${e.marca.includes(m) ? 'checked' : ''}> ${esc(m)} <span class="n">${cuentaM[m] || 0}</span></label>`).join('') || '<p class="ayuda">Sin marcas para esta búsqueda.</p>'}
      </div></fieldset>
      <fieldset class="filtro-grupo"><legend>Disponibilidad</legend>
        <label class="opcion"><input type="checkbox" name="stock" value="1" ${e.stock ? 'checked' : ''}> Solo con stock</label>
      </fieldset>`;
  }

  function leerFiltros(form, e) {
    const d = new FormData(form);
    return { ...e, cat: d.get('cat') || '', marca: d.getAll('marca'), stock: d.get('stock') === '1', p: 1 };
  }

  function pintar() {
    const e = estado();
    const lista = ordenar(filtrar(e), e);
    const paginas = Math.max(1, Math.ceil(lista.length / POR_PAGINA));
    const p = Math.min(e.p, paginas);
    const cat = CAT.categorias.find(c => c.slug === e.cat);

    $('#titulo-tienda').textContent = cat ? cat.nombre : e.q ? `Resultados para “${e.q}”` : 'Tienda';
    document.title = (cat ? cat.nombre : e.q ? `Buscar: ${e.q}` : 'Tienda') + ' · Masherr';
    $('#buscar-tienda').value = e.q;
    $('#orden').value = e.orden;
    $('#cuenta').textContent = `${lista.length} ${lista.length === 1 ? 'producto' : 'productos'}`;
    $('#form-filtros').innerHTML = htmlFiltros(e);
    $('#form-filtros-movil').innerHTML = htmlFiltros(e);

    const activos = [];
    if (e.q) activos.push(['q', `“${e.q}”`]);
    if (cat) activos.push(['cat', cat.nombre]);
    e.marca.forEach(m => activos.push(['marca:' + m, m]));
    if (e.stock) activos.push(['stock', 'Con stock']);
    $('#activos').innerHTML = activos.map(([k, t]) => `<button type="button" data-quitar="${esc(k)}" aria-label="Quitar filtro ${esc(t)}">${esc(t)} ${icono('cerrar')}</button>`).join('')
      + (activos.length > 1 ? `<button type="button" data-quitar="todo">Limpiar todo</button>` : '');

    const grilla = $('#resultados');
    if (!lista.length) {
      grilla.innerHTML = `<div class="vacio"><h2>No encontramos productos</h2><p>Probá con otra palabra, revisá la ortografía o quitá algún filtro. Si no lo ves, consultanos: puede que lo tengamos en el local.</p>
        <p><a class="boton wa" href="${window.M.wa(`Hola Masherr, estoy buscando: ${e.q || 'un producto'}. ¿Lo tienen?`)}" target="_blank" rel="noopener">${icono('whatsapp')}Consultar por WhatsApp</a></p></div>`;
    } else {
      grilla.innerHTML = `<ul class="grilla-prod">${lista.slice((p - 1) * POR_PAGINA, p * POR_PAGINA).map(x => `<li>${tarjeta(x)}</li>`).join('')}</ul>`;
    }
    const enlace = n => { const u = new URLSearchParams(location.search); n > 1 ? u.set('p', n) : u.delete('p'); return '?' + u; };
    $('#paginacion').innerHTML = paginas < 2 ? '' : Array.from({ length: paginas }, (_, i) => i + 1)
      .map(n => n === p ? `<li><span aria-current="page">${n}</span></li>` : `<li><a href="${enlace(n)}" data-pagina="${n}" aria-label="Página ${n}">${n}</a></li>`).join('');
  }

  function init() {
    document.addEventListener('submit', ev => {
      if (ev.target.id === 'form-buscar-tienda') { ev.preventDefault(); irA({ ...estado(), q: ev.target.q.value.trim(), p: 1 }); }
      if (ev.target.id === 'form-filtros-movil') { ev.preventDefault(); irA(leerFiltros(ev.target, estado())); $('#panel-filtros').close(); }
    });
    $('#form-filtros').addEventListener('change', ev => irA(leerFiltros(ev.currentTarget, estado())));
    $('#orden').addEventListener('change', ev => irA({ ...estado(), orden: ev.target.value, p: 1 }));
    document.addEventListener('click', ev => {
      const q = ev.target.closest('[data-quitar]');
      if (q) { const e = estado(), k = q.dataset.quitar;
        if (k === 'todo') irA({ ...e, q: '', cat: '', marca: [], stock: false, p: 1 });
        else if (k.startsWith('marca:')) irA({ ...e, marca: e.marca.filter(m => m !== k.slice(6)), p: 1 });
        else irA({ ...e, [k]: k === 'stock' ? false : '', p: 1 }); }
      const pg = ev.target.closest('[data-pagina]');
      if (pg) { ev.preventDefault(); irA({ ...estado(), p: +pg.dataset.pagina }); $('#titulo-tienda').scrollIntoView(); }
      if (ev.target.closest('[data-abrir-filtros]')) $('#panel-filtros').showModal();
      if (ev.target.closest('[data-cerrar-filtros]')) $('#panel-filtros').close();
    });
    window.addEventListener('popstate', pintar);
  }

  cargarCatalogo().then(c => {
    CAT = c;
    CAT.productos.forEach(p => (p._b = ' ' + norm([p.nombre, p.marca, p.sub, p.catNombre, ...p.variantes.map(v => (v.sku || '') + ' ' + (v.nombre || ''))].join(' '))));
    init(); pintar();
  }).catch(() => {
    $('#resultados').innerHTML = `<div class="vacio" role="alert"><h2>No pudimos cargar el catálogo</h2><p>Revisá tu conexión y volvé a intentar.</p><p><button class="boton" type="button" onclick="location.reload()">Reintentar</button></p></div>`;
  });
})();
