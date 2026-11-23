/* Masherr · Panel de administración: pedidos, ventas, clientes, empresas y productos.
   Acceso solo para usuarios cargados en la tabla "admins" de Supabase (lo controla la base, no esta página). */
(function () {
  'use strict';
  const { ROOT, esc, icono, cargarCatalogo, toast } = window.M;
  const MA = window.MA;
  const app = document.getElementById('admin-app');
  if (!MA) { app.innerHTML = '<p class="cuenta-aviso es-error">El servicio de cuentas no está configurado.</p>'; return; }
  let c, user, pedidos = [], clientes = [], empresas = [], favs = [], cat = null;
  const $ = s => app.querySelector(s);
  const DIA = 864e5;
  const fmtN = n => Math.round(n).toLocaleString('es-AR');
  const fmtM = n => '$' + Math.round(n || 0).toLocaleString('es-AR');
  const fFecha = d => new Date(d).toLocaleDateString('es-AR', { day: '2-digit', month: '2-digit', year: '2-digit' });
  const fHora = d => new Date(d).toLocaleString('es-AR', { day: '2-digit', month: '2-digit', hour: '2-digit', minute: '2-digit' });
  const ESTADOS = { nuevo: 'Nuevo', confirmado: 'Confirmado', entregado: 'Entregado', cancelado: 'Cancelado' };
  const unidades = p => (p.items || []).reduce((a, x) => a + (+x.c || 0), 0);
  const vendido = p => p.estado === 'confirmado' || p.estado === 'entregado';

  // ---------------------------------------------------------------- acceso
  function vistaLogin(aviso = '') {
    app.innerHTML = `<div class="auth-caja" style="margin:0 auto"><h2>Panel Masherr</h2><p class="ayuda">Ingresá con la cuenta de administrador.</p><div id="auth-msg">${aviso}</div>
      <form id="f-adm" class="form-grid"><div class="campo"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required></div>
      <div class="campo"><label for="clave">Contraseña</label><input id="clave" name="clave" type="password" autocomplete="current-password" required></div>
      <button class="boton ancho" type="submit">Ingresar</button></form></div>`;
    $('#f-adm').addEventListener('submit', async e => {
      e.preventDefault(); const d = Object.fromEntries(new FormData(e.target));
      const { error } = await c.auth.signInWithPassword({ email: d.email.trim(), password: d.clave });
      if (error) { $('#auth-msg').innerHTML = `<p class="cuenta-aviso es-error">${MA.traducir(error)}</p>`; return; }
      location.reload();
    });
  }

  async function iniciar() {
    try { c = await MA.cargar(); } catch (e) { app.innerHTML = '<p class="cuenta-aviso es-error">No se pudo conectar con el servicio de cuentas.</p>'; return; }
    user = (await c.auth.getSession()).data.session?.user || null;
    if (!user) return vistaLogin();
    const { data: esAdmin, error } = await c.rpc('es_admin');
    if (error || !esAdmin) {
      app.innerHTML = `<div class="vacio-cuenta"><p><b>${esc(user.email)}</b> no tiene permiso de administrador.</p><button class="boton secundario" type="button" id="salir">Cerrar sesión</button></div>`;
      $('#salir').addEventListener('click', async () => { await c.auth.signOut(); location.reload(); });
      return;
    }
    app.innerHTML = `<div class="adm-barra"><nav class="adm-tabs" aria-label="Secciones">
        <a href="#resumen" data-t="resumen">Resumen</a><a href="#pedidos" data-t="pedidos">Pedidos</a><a href="#clientes" data-t="clientes">Clientes</a>
        <a href="#empresas" data-t="empresas">Empresas</a><a href="#productos" data-t="productos">Productos</a></nav>
        <div class="adm-sesion"><span>${esc(user.email)}</span><button class="boton secundario" type="button" id="recargar">Actualizar</button><button class="boton secundario" type="button" id="salir">Salir</button></div></div>
      <div id="adm-vista"><p class="ayuda">Cargando datos…</p></div>`;
    $('#salir').addEventListener('click', async () => { await c.auth.signOut(); location.reload(); });
    $('#recargar').addEventListener('click', async () => { await cargarDatos(); mostrar(); toast('Datos actualizados'); });
    window.addEventListener('hashchange', mostrar);
    await cargarDatos(); mostrar();
  }

  async function cargarDatos() {
    const [p, cl, em, fv, ct] = await Promise.all([
      c.from('pedidos').select('*').order('creado', { ascending: false }).limit(5000),
      c.rpc('admin_clientes'),
      c.from('empresas').select('*').order('creado', { ascending: false }),
      c.from('favoritos').select('producto, usuario'),
      cargarCatalogo().catch(() => null),
    ]);
    pedidos = p.data || []; clientes = cl.data || []; empresas = em.data || []; favs = fv.data || []; cat = ct;
    const pend = empresas.filter(x => x.estado === 'pendiente').length, nuevos = pedidos.filter(x => x.estado === 'nuevo').length;
    const t = app.querySelector('[data-t=pedidos]'); if (t) t.innerHTML = 'Pedidos' + (nuevos ? ` <span class="adm-badge">${nuevos}</span>` : '');
    const te = app.querySelector('[data-t=empresas]'); if (te) te.innerHTML = 'Empresas' + (pend ? ` <span class="adm-badge">${pend}</span>` : '');
  }

  function mostrar() {
    const t = (location.hash || '#resumen').slice(1); const v = VISTAS[t] ? t : 'resumen';
    app.querySelectorAll('[data-t]').forEach(a => a.toggleAttribute('aria-current', a.dataset.t === v));
    VISTAS[v]($('#adm-vista'));
  }

  // ---------------------------------------------------------------- gráficos (una serie, azul Masherr; tooltip al pasar el mouse)
  function barrasDias(cont, dias, valorDe, etiqueta) {
    const hoy = new Date(); hoy.setHours(0, 0, 0, 0);
    const serie = [...Array(dias)].map((_, i) => { const d = new Date(hoy - (dias - 1 - i) * DIA); return { d, v: 0 }; });
    pedidos.forEach(p => { const d = new Date(p.creado); d.setHours(0, 0, 0, 0); const i = Math.round((d - serie[0].d) / DIA); if (i >= 0 && i < dias) serie[i].v += valorDe(p); });
    const max = Math.max(1, ...serie.map(x => x.v));
    const W = 720, H = 200, pad = 54, bw = (W - pad) / dias;
    const corto = n => (etiqueta === 'Ventas' ? '$' : '') + (n >= 1e6 ? (n / 1e6).toLocaleString('es-AR', { maximumFractionDigits: 1 }) + ' M' : n >= 1e3 ? Math.round(n / 1e3) + ' k' : fmtN(n));
    const marcasY = [0, .5, 1].map(f => Math.round(max * f));
    cont.innerHTML = `<svg class="adm-graf" viewBox="0 0 ${W} ${H + 24}" role="img" aria-label="${etiqueta} por día, últimos ${dias} días">
      ${marcasY.map(m => { const y = H - (m / max) * (H - 10); return `<line x1="${pad}" x2="${W}" y1="${y}" y2="${y}" class="grid"/><text x="${pad - 6}" y="${y + 4}" class="eje" text-anchor="end">${corto(m)}</text>`; }).join('')}
      ${serie.map((x, i) => { const h = (x.v / max) * (H - 10); const xx = pad + i * bw + 1; return `<g class="barra" tabindex="0"><rect class="hit" x="${xx - 1}" y="0" width="${bw}" height="${H}" fill="transparent"/>
        <rect x="${xx}" y="${H - h}" width="${Math.max(2, bw - 2)}" height="${Math.max(0, h)}" rx="${Math.min(4, (bw - 2) / 2)}" class="${x.v ? 'v' : 'cero'}"/>
        <title>${x.d.toLocaleDateString('es-AR', { weekday: 'short', day: 'numeric', month: 'short' })}: ${etiqueta === 'Ventas' ? fmtM(x.v) : fmtN(x.v) + ' ' + etiqueta.toLowerCase()}</title></g>`; }).join('')}
      ${serie.map((x, i) => (i % 7 === 0 || (i === dias - 1 && i % 7 >= 3)) ? `<text x="${pad + i * bw + bw / 2}" y="${H + 18}" class="eje" text-anchor="middle">${x.d.getDate()}/${x.d.getMonth() + 1}</text>` : '').join('')}
    </svg>`;
  }
  function barrasH(lista, fmt = fmtN) {
    if (!lista.length) return '<p class="ayuda">Todavía no hay datos.</p>';
    const max = Math.max(...lista.map(x => x.v));
    return `<ul class="adm-hbar">${lista.map(x => `<li title="${esc(x.n)}: ${fmt(x.v)}"><span class="n">${esc(x.n)}</span><span class="b"><i style="width:${(x.v / max) * 100}%"></i></span><span class="v">${fmt(x.v)}</span></li>`).join('')}</ul>`;
  }
  function topProductos(desde) {
    const m = new Map();
    pedidos.filter(p => p.estado !== 'cancelado' && new Date(p.creado) >= desde).forEach(p => (p.items || []).forEach(x => m.set(x.n, (m.get(x.n) || 0) + (+x.c || 0))));
    return [...m].map(([n, v]) => ({ n, v })).sort((a, b) => b.v - a.v);
  }

  // ---------------------------------------------------------------- vistas
  const VISTAS = {
    resumen(v) {
      const ahora = Date.now(), hoy = new Date(); hoy.setHours(0, 0, 0, 0);
      const en = (dias) => pedidos.filter(p => new Date(p.creado) >= ahora - dias * DIA);
      const p30 = en(30), p30a = pedidos.filter(p => { const t = new Date(p.creado); return t < ahora - 30 * DIA && t >= ahora - 60 * DIA; });
      const ventas30 = p30.filter(vendido).reduce((a, p) => a + (+p.monto || 0), 0);
      const conf30 = p30.filter(vendido).length;
      const conMonto = p30.filter(p => vendido(p) && p.monto);
      const ticket = conMonto.length ? conMonto.reduce((a, p) => a + +p.monto, 0) / conMonto.length : 0;
      const delta = p30a.length ? Math.round((p30.length - p30a.length) / p30a.length * 100) : null;
      const cli30 = clientes.filter(x => new Date(x.alta) >= ahora - 30 * DIA).length;
      const conCuenta = p30.filter(p => p.usuario).length;
      const tile = (n, l, s = '') => `<div class="adm-tile"><span class="l">${l}</span><b>${n}</b>${s ? `<span class="s">${s}</span>` : ''}</div>`;
      v.innerHTML = `<div class="adm-tiles">
          ${tile(fmtN(pedidos.filter(p => new Date(p.creado) >= hoy).length), 'Pedidos hoy')}
          ${tile(fmtN(p30.length), 'Pedidos · 30 días', delta === null ? '' : `${delta >= 0 ? '▲' : '▼'} ${Math.abs(delta)}% vs. 30 días anteriores`)}
          ${tile(fmtN(pedidos.filter(p => p.estado === 'nuevo').length), 'Sin atender', 'Pedidos en estado "Nuevo"')}
          ${tile(fmtM(ventas30), 'Ventas · 30 días', `${conf30} pedidos confirmados o entregados`)}
          ${tile(ticket ? fmtM(ticket) : '—', 'Ticket promedio', 'Sobre pedidos con monto cargado')}
          ${tile(p30.length ? Math.round(conf30 / p30.length * 100) + '%' : '—', 'Conversión', 'Pedidos que se concretaron')}
          ${tile(fmtN(clientes.length), 'Clientes registrados', `+${cli30} en 30 días`)}
          ${tile(fmtN(empresas.filter(x => x.estado === 'pendiente').length), 'Empresas pendientes', `${empresas.filter(x => x.estado === 'aprobada').length} aprobadas`)}
        </div>
        <div class="adm-grid2">
          <section class="adm-card"><h3>Pedidos por día <small>últimos 30 días</small></h3><div id="g-pedidos"></div></section>
          <section class="adm-card"><h3>Ventas por día <small>monto de pedidos confirmados/entregados</small></h3><div id="g-ventas"></div></section>
          <section class="adm-card"><h3>Productos más pedidos <small>unidades · 90 días</small></h3>${barrasH(topProductos(new Date(ahora - 90 * DIA)).slice(0, 10))}</section>
          <section class="adm-card"><h3>Origen de los pedidos <small>30 días</small></h3>${barrasH([{ n: 'Clientes con cuenta', v: conCuenta }, { n: 'Sin cuenta', v: p30.length - conCuenta }].filter(x => x.v))}
            <h3 style="margin-top:22px">Entrega</h3>${barrasH(Object.entries(p30.reduce((a, p) => { const k = /^Env/.test(p.entrega || '') ? 'Envío' : 'Retiro en el local'; a[k] = (a[k] || 0) + 1; return a; }, {})).map(([n, v]) => ({ n, v })))}</section>
        </div>
        <p class="ayuda">Los montos los cargan ustedes en "Pedidos" al cerrar cada venta (la web no publica precios). Datos al ${new Date().toLocaleString('es-AR')}.</p>`;
      barrasDias($('#g-pedidos'), 30, () => 1, 'Pedidos');
      barrasDias($('#g-ventas'), 30, p => vendido(p) ? (+p.monto || 0) : 0, 'Ventas');
    },

    pedidos(v) {
      v.innerHTML = `<div class="adm-filtros"><label>Estado <select id="f-est"><option value="">Todos</option>${Object.entries(ESTADOS).map(([k, l]) => `<option value="${k}">${l}</option>`).join('')}</select></label>
        <label>Desde <input type="date" id="f-desde"></label><label>Hasta <input type="date" id="f-hasta"></label>
        <label class="crece">Buscar <input type="search" id="f-q" placeholder="Cliente, producto…"></label>
        <button class="boton secundario" type="button" id="csv">Descargar Excel (CSV)</button></div><div id="lista"></div>`;
      const filtrar = () => {
        const est = $('#f-est').value, d = $('#f-desde').value, h = $('#f-hasta').value, q = $('#f-q').value.toLowerCase();
        return pedidos.filter(p => (!est || p.estado === est) && (!d || new Date(p.creado) >= new Date(d)) && (!h || new Date(p.creado) < new Date(new Date(h).getTime() + DIA))
          && (!q || JSON.stringify([p.nombre, p.telefono, p.items]).toLowerCase().includes(q)));
      };
      const pintar = () => {
        const l = filtrar();
        $('#lista').innerHTML = l.length ? `<p class="ayuda">${l.length} pedidos · ${fmtM(l.filter(vendido).reduce((a, p) => a + (+p.monto || 0), 0))} vendidos</p>` + l.map(p => `<article class="adm-pedido est-${p.estado}" data-id="${p.id}">
          <header><b>#${p.id}</b><span>${fHora(p.creado)}</span><span>${esc(p.nombre || 'Sin nombre')}${p.usuario ? ' · con cuenta' : ''}</span><span>${unidades(p)} u.</span><span class="chip-est">${ESTADOS[p.estado]}</span></header>
          <ul>${(p.items || []).map(x => `<li>${+x.c} × ${esc(x.n)}</li>`).join('')}</ul>
          <p class="det">${esc(p.entrega || '')}${p.pago ? ' · Pago: ' + esc(p.pago) : ''}${p.factura ? ' · Factura: ' + esc(p.factura) : ''}${p.comentarios ? '<br>Comentario: ' + esc(p.comentarios) : ''}</p>
          <div class="acc"><label>Estado <select data-campo="estado">${Object.entries(ESTADOS).map(([k, l]) => `<option value="${k}" ${p.estado === k ? 'selected' : ''}>${l}</option>`).join('')}</select></label>
            <label>Monto $ <input data-campo="monto" type="number" min="0" step="1" value="${p.monto ?? ''}" placeholder="0"></label>
            <label class="crece">Nota interna <input data-campo="nota_interna" value="${esc(p.nota_interna || '')}" placeholder="Ej.: retira el viernes"></label>
            ${p.telefono ? `<a class="boton wa" href="https://wa.me/${String(p.telefono).replace(/\D/g, '').replace(/^0?/, '549')}" target="_blank" rel="noopener">${icono('whatsapp')}</a>` : ''}
            <button class="boton" type="button" data-guardar>Guardar</button></div></article>`).join('') : '<div class="vacio-cuenta"><p>No hay pedidos con esos filtros.</p></div>';
      };
      ['#f-est', '#f-desde', '#f-hasta', '#f-q'].forEach(s => $(s).addEventListener('input', pintar));
      $('#lista').addEventListener('click', async e => {
        const b = e.target.closest('[data-guardar]'); if (!b) return;
        const art = b.closest('[data-id]'); const id = +art.dataset.id; const cambios = { actualizado: new Date().toISOString() };
        art.querySelectorAll('[data-campo]').forEach(i => { cambios[i.dataset.campo] = i.dataset.campo === 'monto' ? (i.value === '' ? null : +i.value) : (i.value || null); });
        if (!cambios.estado) cambios.estado = 'nuevo';
        b.disabled = true; const { error } = await c.from('pedidos').update(cambios).eq('id', id); b.disabled = false;
        if (error) { toast('No se pudo guardar: ' + esc(error.message)); return; }
        Object.assign(pedidos.find(p => p.id === id), cambios); toast(`Pedido #${id} actualizado`); pintar(); cargarDatos();
      });
      $('#csv').addEventListener('click', () => {
        const filas = [['Pedido', 'Fecha', 'Cliente', 'Teléfono', 'Con cuenta', 'Productos', 'Unidades', 'Entrega', 'Pago', 'Factura', 'Estado', 'Monto', 'Nota interna']]
          .concat(filtrar().map(p => [p.id, new Date(p.creado).toLocaleString('es-AR'), p.nombre || '', p.telefono || '', p.usuario ? 'Sí' : 'No', (p.items || []).map(x => `${x.c} x ${x.n}`).join(' | '), unidades(p), p.entrega || '', p.pago || '', p.factura || '', ESTADOS[p.estado], p.monto ?? '', p.nota_interna || '']));
        const csv = '﻿' + filas.map(f => f.map(x => `"${String(x).replace(/"/g, '""')}"`).join(';')).join('\r\n');
        const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([csv], { type: 'text/csv;charset=utf-8' })); a.download = `pedidos-masherr-${new Date().toISOString().slice(0, 10)}.csv`; a.click();
      });
      pintar();
    },

    clientes(v) {
      const porUsuario = pedidos.reduce((m, p) => { if (p.usuario) { const x = m[p.usuario] || (m[p.usuario] = { n: 0, monto: 0, ult: null }); x.n++; if (vendido(p)) x.monto += +p.monto || 0; if (!x.ult || p.creado > x.ult) x.ult = p.creado; } return m; }, {});
      v.innerHTML = `<p class="ayuda">${clientes.length} clientes registrados.</p><div class="adm-tabla"><table><thead><tr><th>Cliente</th><th>Email</th><th>Teléfono</th><th>Localidad</th><th>Alta</th><th>Pedidos</th><th>Comprado</th><th>Último pedido</th></tr></thead><tbody>
        ${clientes.map(x => { const s = porUsuario[x.id] || { n: 0, monto: 0 }; return `<tr><td>${esc(x.nombre || '—')}</td><td><a href="mailto:${esc(x.email)}">${esc(x.email)}</a></td><td>${x.telefono ? `<a href="https://wa.me/${String(x.telefono).replace(/\D/g, '').replace(/^0?/, '549')}" target="_blank" rel="noopener">${esc(x.telefono)}</a>` : '—'}</td><td>${esc(x.localidad || '—')}</td><td>${fFecha(x.alta)}</td><td class="num">${s.n}</td><td class="num">${s.monto ? fmtM(s.monto) : '—'}</td><td>${s.ult ? fFecha(s.ult) : '—'}</td></tr>`; }).join('')}
      </tbody></table></div>`;
    },

    empresas(v) {
      const mail = Object.fromEntries(clientes.map(x => [x.id, x.email]));
      v.innerHTML = empresas.length ? empresas.map(x => `<article class="adm-pedido est-${x.estado === 'aprobada' ? 'entregado' : x.estado === 'rechazada' ? 'cancelado' : 'nuevo'}" data-u="${x.usuario}">
        <header><b>${esc(x.razon)}</b><span>CUIT ${esc(x.cuit)}</span><span>${esc(x.iva || '')}</span><span class="chip-est">${{ pendiente: 'Pendiente', aprobada: 'Aprobada', rechazada: 'Rechazada' }[x.estado]}</span></header>
        <p class="det">${esc(x.rubro || '')} · Contacto: ${esc(x.contacto || '')} · ${esc(x.telefono || '')} · ${esc(mail[x.usuario] || '')} · Solicitud: ${fFecha(x.creado)}</p>
        <div class="acc"><label class="crece">Condiciones / nota para el cliente <input data-nota value="${esc(x.nota || '')}" placeholder="Ej.: cuenta corriente 30 días"></label>
          <button class="boton" type="button" data-est="aprobada">Aprobar</button><button class="boton secundario" type="button" data-est="rechazada">Rechazar</button></div></article>`).join('')
        : '<div class="vacio-cuenta"><p>Todavía no hay solicitudes de cuenta empresa.</p></div>';
      v.onclick = async e => {
        const b = e.target.closest('[data-est]'); if (!b) return;
        const art = b.closest('[data-u]');
        const { error } = await c.from('empresas').update({ estado: b.dataset.est, nota: art.querySelector('[data-nota]').value || null }).eq('usuario', art.dataset.u);
        if (error) { toast('No se pudo guardar'); return; }
        toast(b.dataset.est === 'aprobada' ? 'Empresa aprobada' : 'Solicitud rechazada'); await cargarDatos(); VISTAS.empresas(v);
      };
    },

    productos(v) {
      const nombre = id => (cat && (cat.productos.find(p => p.id === id) || {}).nombre) || `Producto ${id}`;
      const fm = new Map(); favs.forEach(f => fm.set(f.producto, (fm.get(f.producto) || 0) + 1));
      const topFav = [...fm].map(([id, n]) => ({ n: nombre(id), v: n })).sort((a, b) => b.v - a.v).slice(0, 15);
      v.innerHTML = `<div class="adm-grid2"><section class="adm-card"><h3>Más pedidos <small>unidades · histórico</small></h3>${barrasH(topProductos(new Date(0)).slice(0, 15))}</section>
        <section class="adm-card"><h3>Más guardados en favoritos <small>clientes con cuenta</small></h3>${barrasH(topFav)}</section></div>`;
    },
  };

  iniciar();
})();
