/* Masherr · Mi cuenta: ingreso / registro (Supabase), datos, pedidos, favoritos y cuenta empresa.
   Sin servicio de cuentas configurado, funciona guardando todo en este dispositivo. */
(function () {
  'use strict';
  const { ROOT, esc, icono, cargarCatalogo, carrito, resolver, wa, toast, tarjeta, pintarFavoritos, favoritos } = window.M;
  const MA = window.MA;  // null si no hay servicio de cuentas
  const panel = document.getElementById('panel');
  const tabs = document.querySelector('.cuenta-tabs');
  const CLAVE_P = 'masherr_perfil_v1', CLAVE_H = 'masherr_pedidos_v1', CLAVE_E = 'masherr_empresa_v1';
  const leer = (k, d) => { try { return JSON.parse(localStorage.getItem(k) || 'null') ?? d; } catch (e) { return d; } };
  const guardar = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); return true; } catch (e) { return false; } };
  const campo = (id, label, v, extra = '') => `<div class="campo"><label for="${id}">${label}</label><input id="${id}" name="${id}" value="${esc(v || '')}" ${extra}></div>`;
  const fecha = f => new Date(f).toLocaleDateString('es-AR', { day: 'numeric', month: 'long', year: 'numeric' });
  const msg = (t, tipo = 'info') => `<p class="cuenta-aviso ${tipo === 'error' ? 'es-error' : ''}" role="${tipo === 'error' ? 'alert' : 'status'}">${icono('info')}<span>${t}</span></p>`;
  let c = null, user = null;

  function hola() {
    const n = (user && user.user_metadata && user.user_metadata.nombre) || leer(CLAVE_P, {}).nombre;
    document.getElementById('cuenta-hola').textContent = n ? `Hola, ${n.split(' ')[0]}.` : 'Hola.';
    if (MA) MA.saludo();
    const salir = document.getElementById('cuenta-salir');
    if (user && !salir) {
      const b = document.createElement('button'); b.id = 'cuenta-salir'; b.type = 'button'; b.className = 'boton borde-claro'; b.textContent = 'Cerrar sesión';
      b.addEventListener('click', async () => { await c.auth.signOut(); try { sessionStorage.removeItem('masherr_sinc'); } catch (e) {} location.hash = '#datos'; location.reload(); });
      document.querySelector('.cuenta-cab .contenedor').appendChild(b);
    } else if (!user && salir) salir.remove();
  }

  // ---------------------------------------------------------------- Ingreso / registro
  function vistaIngreso(modo = 'ingresar', aviso = '') {
    const f = {
      ingresar: `<form id="f-auth" class="form-grid" novalidate>${campo('email', 'Email', '', 'type="email" autocomplete="email" required')}
        <div class="campo"><label for="clave">Contraseña</label><input id="clave" name="clave" type="password" autocomplete="current-password" required></div>
        <button class="boton ancho" type="submit">Ingresar</button>
        <p class="auth-links"><a href="#" data-modo="recuperar">Olvidé mi contraseña</a></p></form>`,
      registro: `<form id="f-auth" class="form-grid" novalidate>${campo('nombre', 'Nombre y apellido', '', 'autocomplete="name" required')}
        ${campo('email', 'Email', '', 'type="email" autocomplete="email" required')}
        ${campo('telefono', 'Teléfono / WhatsApp (opcional)', '', 'autocomplete="tel" inputmode="tel"')}
        <div class="campo"><label for="clave">Contraseña</label><input id="clave" name="clave" type="password" autocomplete="new-password" minlength="8" required><span class="ayuda">Al menos 8 caracteres.</span></div>
        <button class="boton ancho" type="submit">Crear mi cuenta</button>
        <p class="ayuda">Te vamos a mandar un mail para confirmar tu cuenta.</p></form>`,
      recuperar: `<form id="f-auth" class="form-grid" novalidate>${campo('email', 'Email de tu cuenta', '', 'type="email" autocomplete="email" required')}
        <button class="boton ancho" type="submit">Enviarme el enlace</button>
        <p class="auth-links"><a href="#" data-modo="ingresar">Volver a ingresar</a></p></form>`,
    };
    panel.innerHTML = `<div class="auth-caja">
      ${modo !== 'recuperar' ? `<div class="auth-tabs" role="tablist"><button type="button" role="tab" data-modo="ingresar" aria-selected="${modo === 'ingresar'}">Ingresar</button><button type="button" role="tab" data-modo="registro" aria-selected="${modo === 'registro'}">Crear cuenta</button></div>`
        : '<h2>Recuperá tu contraseña</h2><p class="ayuda">Te mandamos un enlace para elegir una nueva.</p>'}
      <div id="auth-msg">${aviso}</div>${f[modo]}</div>
      <aside class="auth-beneficios"><h2>Con tu cuenta Masherr</h2><ul>
        <li>${icono('usuario')}<span>Tus datos de entrega y factura, listos en cada pedido.</span></li>
        <li>${icono('pedido')}<span>El historial de tus pedidos para repetirlos con un toque.</span></li>
        <li>${icono('corazon')}<span>Tus favoritos en el celular y en la compu.</span></li>
        <li>${icono('empresa')}<span>Cuenta empresa con condiciones especiales.</span></li></ul></aside>`;
    panel.querySelectorAll('[data-modo]').forEach(b => b.addEventListener('click', e => { e.preventDefault(); vistaIngreso(b.dataset.modo); }));
    const form = panel.querySelector('#f-auth'), box = panel.querySelector('#auth-msg');
    form.addEventListener('submit', async e => {
      e.preventDefault();
      const d = Object.fromEntries(new FormData(form));
      const btn = form.querySelector('button[type=submit]'); btn.disabled = true;
      try {
        if (!d.email || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(d.email)) throw new Error('invalid email');
        if (modo === 'ingresar') {
          const { error } = await c.auth.signInWithPassword({ email: d.email.trim(), password: d.clave });
          if (error) throw error;
        } else if (modo === 'registro') {
          if (!d.nombre.trim()) { box.innerHTML = msg('Completá tu nombre.', 'error'); return; }
          if ((d.clave || '').length < 8) throw new Error('password should be at least');
          const { data, error } = await c.auth.signUp({ email: d.email.trim(), password: d.clave,
            options: { emailRedirectTo: location.origin + '/cuenta/', data: { nombre: d.nombre.trim(), telefono: d.telefono || '' } } });
          if (error) throw error;
          if (data.user && data.user.identities && data.user.identities.length === 0) throw new Error('already registered');
          window.dataLayer && window.dataLayer.push({ event: 'registro_cuenta' });
          if (!data.session) { vistaIngreso('ingresar', msg(`¡Listo! Te mandamos un mail a <b>${esc(d.email)}</b>. Tocá "Confirmar mi cuenta" y después ingresá acá. Si no lo ves, revisá la carpeta de spam.`)); return; }
        } else {
          const { error } = await c.auth.resetPasswordForEmail(d.email.trim(), { redirectTo: location.origin + '/cuenta/' });
          if (error) throw error;
          box.innerHTML = msg(`Si <b>${esc(d.email)}</b> tiene una cuenta, te llega un mail con el enlace para elegir una nueva contraseña.`); return;
        }
      } catch (err) { box.innerHTML = msg(MA.traducir(err), 'error'); }
      finally { btn.disabled = false; }
    });
  }

  function vistaNuevaClave() {
    tabs.hidden = true;
    panel.innerHTML = `<div class="auth-caja"><h2>Elegí tu nueva contraseña</h2><div id="auth-msg"></div>
      <form id="f-clave" class="form-grid"><div class="campo"><label for="clave">Nueva contraseña</label><input id="clave" name="clave" type="password" autocomplete="new-password" minlength="8" required><span class="ayuda">Al menos 8 caracteres.</span></div>
      <button class="boton ancho" type="submit">Guardar contraseña</button></form></div>`;
    panel.querySelector('#f-clave').addEventListener('submit', async e => {
      e.preventDefault(); const clave = e.target.clave.value;
      const box = panel.querySelector('#auth-msg');
      if (clave.length < 8) { box.innerHTML = msg(MA.traducir(new Error('password should be at least')), 'error'); return; }
      const { error } = await c.auth.updateUser({ password: clave });
      if (error) { box.innerHTML = msg(MA.traducir(error), 'error'); return; }
      toast('Tu contraseña quedó actualizada'); tabs.hidden = false; history.replaceState(null, '', '#datos'); mostrar();
    });
  }

  // ---------------------------------------------------------------- Vistas con cuenta (o locales)
  async function perfilActual() {
    if (!user) return leer(CLAVE_P, {});
    const { data } = await c.from('perfiles').select('*').eq('id', user.id).maybeSingle();
    if (data) return data;
    const local = leer(CLAVE_P, {});
    const nuevo = { id: user.id, nombre: (user.user_metadata || {}).nombre || local.nombre || null, telefono: (user.user_metadata || {}).telefono || local.telefono || null,
      direccion: local.direccion || null, localidad: local.localidad || null, cp: local.cp || null, pago: local.pago || null, factura: local.factura || null };
    await c.from('perfiles').upsert(nuevo);
    return nuevo;
  }

  const vistas = {
    async datos() {
      if (MA && !user) return vistaIngreso();
      const p = await perfilActual();
      panel.innerHTML = `<h2>Mis datos</h2>${user ? `<p class="ayuda">Cuenta: <b>${esc(user.email)}</b></p>` : msg('Tus datos se guardan en este dispositivo.')}
        <form id="f-perfil" class="form-grid dos">
          ${campo('nombre', 'Nombre y apellido', p.nombre, 'autocomplete="name"')}
          ${campo('telefono', 'Teléfono / WhatsApp', p.telefono, 'autocomplete="tel" inputmode="tel"')}
          ${campo('direccion', 'Dirección de entrega', p.direccion, 'autocomplete="street-address"')}
          ${campo('localidad', 'Localidad', p.localidad, 'autocomplete="address-level2"')}
          ${campo('cp', 'Código postal', p.cp, 'autocomplete="postal-code" inputmode="numeric"')}
          <div class="campo"><label for="pago">Forma de pago preferida</label><select id="pago" name="pago">
            ${['', 'Efectivo', 'Transferencia', 'Tarjeta', 'Mercado Pago', 'A coordinar'].map(o => `<option ${p.pago === o ? 'selected' : ''} value="${o}">${o || 'Elegí una opción'}</option>`).join('')}</select></div>
          ${campo('factura', 'Datos de factura (opcional)', p.factura, 'placeholder="Ej.: Factura A, CUIT 30-…"')}
          <div class="entero"><button class="boton" type="submit">Guardar mis datos</button>
          <p class="ayuda" style="margin-top:10px">Se completan solos cuando envíes un pedido por WhatsApp.</p></div>
        </form>`;
      panel.querySelector('#f-perfil').addEventListener('submit', async e => {
        e.preventDefault();
        const d = Object.fromEntries(new FormData(e.target));
        guardar(CLAVE_P, d);  // también en el dispositivo, para completar el pedido
        if (user) { const { error } = await c.from('perfiles').upsert({ id: user.id, ...d, actualizado: new Date().toISOString() }); if (error) { toast('No pudimos guardar tus datos. Probá de nuevo.'); return; } }
        toast('Tus datos quedaron guardados'); hola();
      });
    },

    async pedidos() {
      if (MA && !user) return vistaIngreso('ingresar', msg('Ingresá para ver tus pedidos en cualquier dispositivo.'));
      let lista = leer(CLAVE_H, []).map(p => ({ fecha: p.fecha, items: p.items }));
      if (user) {
        const { data } = await c.from('pedidos').select('creado, items').order('creado', { ascending: false }).limit(50);
        if (data && data.length) lista = data.map(p => ({ fecha: p.creado, items: p.items }));
      }
      if (!lista.length) { panel.innerHTML = `<h2>Mis pedidos</h2><div class="vacio-cuenta"><p>Todavía no enviaste pedidos.</p><a class="boton" href="${ROOT}tienda/">Ir a la tienda</a></div>`; return; }
      panel.innerHTML = `<h2>Mis pedidos</h2>` + lista.map((p, i) => `<article class="pedido-item"><header><span>Pedido del ${fecha(p.fecha)}</span><span>${p.items.reduce((a, x) => a + x.c, 0)} productos</span></header>
        <ul>${p.items.map(x => `<li>${x.c} × ${esc(x.n)}</li>`).join('')}</ul>
        <p style="display:flex;gap:10px;flex-wrap:wrap;margin:0"><button class="boton" type="button" data-repetir="${i}">${icono('carrito')}Repetir pedido</button>
        <a class="boton wa" href="${wa('Hola Masherr, quiero consultar por mi pedido del ' + fecha(p.fecha) + ':\n' + p.items.map(x => '• ' + x.c + ' × ' + x.n).join('\n'))}" target="_blank" rel="noopener">${icono('whatsapp')}Consultar</a></p></article>`).join('');
      panel.onclick = async e => {
        const b = e.target.closest('[data-repetir]'); if (!b) return;
        const cat = await cargarCatalogo(); let n = 0;
        lista[+b.dataset.repetir].items.forEach(x => { const r = resolver(cat, x.v); if (r && r.v.disponible) { carrito.agregar(x.v, x.c); n++; } });
        toast(n ? `Agregamos ${n} productos a tu pedido <a href="${ROOT}carrito/">Ver pedido</a>` : 'Esos productos ya no están disponibles');
      };
    },

    async favoritos() {
      panel.onclick = null;
      if (user) { try { await MA.sincronizarFavoritos(); } catch (e) {} }
      const ids = favoritos.lista();
      if (!ids.length) { panel.innerHTML = `<h2>Favoritos</h2><div class="vacio-cuenta"><p>Tocá el corazón de un producto para guardarlo acá.</p><a class="boton" href="${ROOT}tienda/">Ir a la tienda</a></div>`; return; }
      panel.innerHTML = `<h2>Favoritos</h2><p class="ayuda">Cargando…</p>`;
      const cat = await cargarCatalogo();
      const lista = ids.map(id => cat.productos.find(p => p.id === id)).filter(Boolean);
      panel.innerHTML = `<h2>Favoritos</h2>${!user && MA ? msg('Ingresá para tener tus favoritos en todos tus dispositivos.') : ''}<ul class="grilla-prod">${lista.map(p => `<li>${tarjeta(p)}</li>`).join('')}</ul>`;
      pintarFavoritos();
    },

    async empresa() {
      panel.onclick = null;
      if (MA && !user) return vistaIngreso('ingresar', msg('Ingresá o creá tu cuenta para solicitar el alta como empresa.'));
      let em = leer(CLAVE_E, {});
      if (user) { const { data } = await c.from('empresas').select('*').eq('usuario', user.id).maybeSingle(); em = data ? { razon: data.razon, cuit: data.cuit, iva: data.iva, rubro: data.rubro, contacto: data.contacto, tel: data.telefono, estado: data.estado, nota: data.nota, fecha: data.creado } : {}; }
      const ESTADO = { pendiente: ['Solicitud en revisión', 'Te confirmamos el alta por WhatsApp.'], solicitada: ['Solicitud enviada', 'Te confirmamos el alta por WhatsApp.'], aprobada: ['Cuenta empresa aprobada', ''], rechazada: ['Solicitud no aprobada', 'Escribinos por WhatsApp para revisarlo.'] };
      const est = em.estado && ESTADO[em.estado];
      panel.innerHTML = `<h2>Cuenta empresa</h2>
        <p class="bajada" style="font-size:16px">Para industrias, talleres, constructoras y comercios: cotizaciones, pedidos grandes y condiciones especiales.</p>
        ${est ? `<div class="estado-empresa estado-${em.estado}"><b>${est[0]}</b><span>${em.nota ? esc(em.nota) : est[1]}</span></div>` : ''}
        <form id="f-emp" class="form-grid dos">
          ${campo('razon', 'Razón social *', em.razon, 'required')}
          ${campo('cuit', 'CUIT *', em.cuit, 'required inputmode="numeric" placeholder="30-12345678-9"')}
          <div class="campo"><label for="iva">Condición frente al IVA</label><select id="iva" name="iva">${['Responsable inscripto', 'Monotributo', 'Exento', 'Consumidor final'].map(o => `<option ${em.iva === o ? 'selected' : ''}>${o}</option>`).join('')}</select></div>
          ${campo('rubro', 'Rubro', em.rubro, 'placeholder="Ej.: metalúrgica, construcción, mantenimiento"')}
          ${campo('contacto', 'Persona de contacto *', em.contacto, 'required')}
          ${campo('tel', 'Teléfono *', em.tel, 'required inputmode="tel"')}
          <div class="entero"><button class="boton wa" type="submit">${icono('whatsapp')}${em.estado ? 'Actualizar datos' : 'Solicitar alta como empresa'}</button></div>
        </form>`;
      panel.querySelector('#f-emp').addEventListener('submit', async e => {
        e.preventDefault();
        const d = Object.fromEntries(new FormData(e.target));
        if (!d.razon.trim() || !d.cuit.trim() || !d.contacto.trim() || !d.tel.trim()) { toast('Completá los campos con *'); return; }
        if (user) {
          const fila = { usuario: user.id, razon: d.razon, cuit: d.cuit, iva: d.iva, rubro: d.rubro, contacto: d.contacto, telefono: d.tel };
          const { error } = em.estado ? await c.from('empresas').update(fila).eq('usuario', user.id) : await c.from('empresas').insert(fila);
          if (error) { toast('No pudimos guardar la solicitud. Probá de nuevo.'); return; }
        } else guardar(CLAVE_E, { ...d, estado: 'solicitada', fecha: Date.now() });
        if (!em.estado) {
          const txt = ['Hola Masherr, quiero dar de alta una cuenta empresa:', '', `Razón social: ${d.razon}`, `CUIT: ${d.cuit}`, `Condición IVA: ${d.iva}`, d.rubro ? `Rubro: ${d.rubro}` : '', `Contacto: ${d.contacto}`, `Teléfono: ${d.tel}`, user ? `Email de la cuenta: ${user.email}` : ''].filter(Boolean).join('\n');
          window.open(wa(txt), '_blank', 'noopener');
          window.dataLayer && window.dataLayer.push({ event: 'solicitud_empresa' });
        } else toast('Datos de la empresa actualizados');
        vistas.empresa();
      });
    },
  };

  function mostrar() {
    const t = (location.hash || '#datos').slice(1).split('&')[0];
    const v = vistas[t] ? t : 'datos';
    document.querySelectorAll('[data-tab]').forEach(a => { if (a.dataset.tab === v) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current'); });
    panel.innerHTML = '<p class="ayuda">Cargando…</p>';
    Promise.resolve(vistas[v]()).catch(() => { panel.innerHTML = msg('No pudimos cargar esta sección. Revisá tu conexión y probá de nuevo.', 'error'); });
  }

  async function iniciar() {
    if (!MA) { hola(); mostrar(); window.addEventListener('hashchange', mostrar); return; }
    const recuperando = /type=recovery/.test(location.hash);
    const volviendo = /access_token|error_description/.test(location.hash);
    try { c = await MA.cargar(); } catch (e) { panel.innerHTML = msg('No pudimos conectar con el servicio de cuentas. Probá de nuevo en unos minutos.', 'error'); return; }
    if (/error_description/.test(location.hash)) {
      const p = new URLSearchParams(location.hash.slice(1)); history.replaceState(null, '', location.pathname + '#datos');
      vistaIngreso('ingresar', msg(/expired|invalid/i.test(p.get('error_description') || '') ? 'El enlace venció o ya se usó. Ingresá o pedí uno nuevo.' : 'No pudimos validar el enlace. Probá de nuevo.', 'error'));
      return;
    }
    const { data } = await c.auth.getSession();
    user = data.session ? data.session.user : null;
    c.auth.onAuthStateChange((ev, ses) => {
      if (ev === 'PASSWORD_RECOVERY') { user = ses && ses.user; vistaNuevaClave(); return; }
      const antes = user && user.id; user = ses ? ses.user : null;
      if (ev === 'SIGNED_IN' && !antes) { hola(); MA.sincronizarFavoritos().catch(() => {}); if (!/type=recovery/.test(location.hash)) { history.replaceState(null, '', location.pathname + '#datos'); mostrar(); } }
      if (ev === 'SIGNED_OUT') { hola(); mostrar(); }
    });
    hola();
    if (recuperando) { vistaNuevaClave(); return; }
    if (volviendo) { history.replaceState(null, '', location.pathname + '#datos'); if (user) toast('¡Tu cuenta quedó confirmada!'); }
    if (user) MA.sincronizarFavoritos().catch(() => {});
    window.addEventListener('hashchange', () => { if (!/access_token/.test(location.hash)) mostrar(); });
    mostrar();
  }
  document.addEventListener('favoritos', () => { if ((location.hash || '') === '#favoritos') vistas.favoritos(); });
  iniciar();
})();
