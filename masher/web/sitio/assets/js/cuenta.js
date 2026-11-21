/* Masherr · Mi cuenta: datos guardados, historial de pedidos, favoritos y alta de cuenta empresa.
   Por ahora todo se guarda en este navegador; cuando se conecte el servicio de usuarios se sincroniza. */
(function () {
  'use strict';
  const { CFG, ROOT, esc, icono, cargarCatalogo, carrito, resolver, wa, toast, tarjeta, pintarFavoritos, favoritos } = window.M;
  const panel = document.getElementById('panel');
  const CLAVE_P = 'masherr_perfil_v1', CLAVE_H = 'masherr_pedidos_v1', CLAVE_E = 'masherr_empresa_v1';
  const leer = (k, d) => { try { return JSON.parse(localStorage.getItem(k) || 'null') ?? d; } catch (e) { return d; } };
  const guardar = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); return true; } catch (e) { return false; } };
  const AVISO = `<p class="cuenta-aviso">${icono('info')}<span>Por ahora tu cuenta se guarda en este dispositivo. Muy pronto vas a poder ingresar con usuario y contraseña desde cualquier celular o computadora.</span></p>`;
  const campo = (id, label, v, extra = '') => `<div class="campo"><label for="${id}">${label}</label><input id="${id}" name="${id}" value="${esc(v || '')}" ${extra}></div>`;

  function saludo() {
    const p = leer(CLAVE_P, {});
    document.getElementById('cuenta-hola').textContent = p.nombre ? `Hola, ${p.nombre.split(' ')[0]}.` : 'Hola.';
  }

  const vistas = {
    datos() {
      const p = leer(CLAVE_P, {});
      panel.innerHTML = `<h2>Mis datos</h2>${AVISO}
        <form id="f-perfil" class="form-grid dos">
          ${campo('nombre', 'Nombre y apellido', p.nombre, 'autocomplete="name"')}
          ${campo('telefono', 'Teléfono / WhatsApp', p.telefono, 'autocomplete="tel" inputmode="tel"')}
          ${campo('email', 'Email', p.email, 'type="email" autocomplete="email"')}
          ${campo('direccion', 'Dirección de entrega', p.direccion, 'autocomplete="street-address"')}
          ${campo('localidad', 'Localidad', p.localidad, 'autocomplete="address-level2"')}
          ${campo('cp', 'Código postal', p.cp, 'autocomplete="postal-code" inputmode="numeric"')}
          <div class="campo"><label for="pago">Forma de pago preferida</label><select id="pago" name="pago">
            ${['', 'Efectivo', 'Transferencia', 'Tarjeta', 'Mercado Pago', 'A coordinar'].map(o => `<option ${p.pago === o ? 'selected' : ''} value="${o}">${o || 'Elegí una opción'}</option>`).join('')}</select></div>
          ${campo('factura', 'Datos de factura (opcional)', p.factura, 'placeholder="Ej.: Factura A, CUIT 30-…"')}
          <div class="entero"><button class="boton" type="submit">Guardar mis datos</button>
          <p class="ayuda" style="margin-top:10px">Se completan solos cuando envíes un pedido por WhatsApp.</p></div>
        </form>`;
      panel.querySelector('#f-perfil').addEventListener('submit', e => {
        e.preventDefault();
        const ok = guardar(CLAVE_P, Object.fromEntries(new FormData(e.target)));
        toast(ok ? 'Tus datos quedaron guardados' : 'No pudimos guardar los datos en este navegador'); saludo();
      });
    },

    async pedidos() {
      const h = leer(CLAVE_H, []);
      if (!h.length) { panel.innerHTML = `<h2>Mis pedidos</h2>${AVISO}<div class="vacio-cuenta"><p>Todavía no enviaste pedidos desde este dispositivo.</p><a class="boton" href="${ROOT}tienda/">Ir a la tienda</a></div>`; return; }
      panel.innerHTML = `<h2>Mis pedidos</h2>${AVISO}` + h.map((p, i) => `<article class="pedido-item"><header><span>Pedido del ${new Date(p.fecha).toLocaleDateString('es-AR')}</span><span>${p.items.reduce((a, x) => a + x.c, 0)} productos</span></header>
        <ul>${p.items.map(x => `<li>${x.c} × ${esc(x.n)}</li>`).join('')}</ul>
        <p style="display:flex;gap:10px;flex-wrap:wrap;margin:0"><button class="boton" type="button" data-repetir="${i}">${icono('carrito')}Repetir pedido</button>
        <a class="boton wa" href="${wa('Hola Masherr, quiero consultar por mi pedido del ' + new Date(p.fecha).toLocaleDateString('es-AR') + ':\n' + p.items.map(x => '• ' + x.c + ' × ' + x.n).join('\n'))}" target="_blank" rel="noopener">${icono('whatsapp')}Consultar</a></p></article>`).join('');
      panel.addEventListener('click', async e => {
        const b = e.target.closest('[data-repetir]'); if (!b) return;
        const cat = await cargarCatalogo(); let n = 0;
        h[+b.dataset.repetir].items.forEach(x => { const r = resolver(cat, x.v); if (r && r.v.disponible) { carrito.agregar(x.v, x.c); n++; } });
        toast(n ? `Agregamos ${n} productos a tu pedido <a href="${ROOT}carrito/">Ver pedido</a>` : 'Esos productos ya no están disponibles');
      }, { once: false });
    },

    async favoritos() {
      const ids = favoritos.lista();
      if (!ids.length) { panel.innerHTML = `<h2>Favoritos</h2><div class="vacio-cuenta"><p>Tocá el corazón de un producto para guardarlo acá.</p><a class="boton" href="${ROOT}tienda/">Ir a la tienda</a></div>`; return; }
      panel.innerHTML = `<h2>Favoritos</h2><p class="ayuda">Cargando…</p>`;
      const cat = await cargarCatalogo();
      const lista = ids.map(id => cat.productos.find(p => p.id === id)).filter(Boolean);
      panel.innerHTML = `<h2>Favoritos</h2><ul class="grilla-prod">${lista.map(p => `<li>${tarjeta(p)}</li>`).join('')}</ul>`;
      pintarFavoritos();
    },

    empresa() {
      const em = leer(CLAVE_E, {});
      panel.innerHTML = `<h2>Cuenta empresa</h2>
        <p class="bajada" style="font-size:16px">Para industrias, talleres, constructoras y comercios: cotizaciones, pedidos grandes y condiciones especiales. Completá los datos y te damos el alta por WhatsApp.</p>
        ${em.estado ? `<p class="cuenta-aviso">${icono('info')}<span>Solicitud enviada el ${new Date(em.fecha).toLocaleDateString('es-AR')}. Te confirmamos el alta por WhatsApp.</span></p>` : ''}
        <form id="f-emp" class="form-grid dos">
          ${campo('razon', 'Razón social *', em.razon, 'required')}
          ${campo('cuit', 'CUIT *', em.cuit, 'required inputmode="numeric" placeholder="30-12345678-9"')}
          <div class="campo"><label for="iva">Condición frente al IVA</label><select id="iva" name="iva">${['Responsable inscripto', 'Monotributo', 'Exento', 'Consumidor final'].map(o => `<option ${em.iva === o ? 'selected' : ''}>${o}</option>`).join('')}</select></div>
          ${campo('rubro', 'Rubro', em.rubro, 'placeholder="Ej.: metalúrgica, construcción, mantenimiento"')}
          ${campo('contacto', 'Persona de contacto *', em.contacto, 'required')}
          ${campo('tel', 'Teléfono *', em.tel, 'required inputmode="tel"')}
          <div class="entero"><button class="boton wa" type="submit">${icono('whatsapp')}Solicitar alta como empresa</button></div>
        </form>`;
      panel.querySelector('#f-emp').addEventListener('submit', e => {
        e.preventDefault();
        const d = Object.fromEntries(new FormData(e.target));
        guardar(CLAVE_E, { ...d, estado: 'solicitada', fecha: Date.now() });
        const txt = ['Hola Masherr, quiero dar de alta una cuenta empresa:', '', `Razón social: ${d.razon}`, `CUIT: ${d.cuit}`, `Condición IVA: ${d.iva}`, d.rubro ? `Rubro: ${d.rubro}` : '', `Contacto: ${d.contacto}`, `Teléfono: ${d.tel}`].filter(Boolean).join('\n');
        window.open(wa(txt), '_blank', 'noopener');
        window.dataLayer && window.dataLayer.push({ event: 'solicitud_empresa' });
        vistas.empresa();
      });
    },
  };

  function mostrar() {
    const t = (location.hash || '#datos').slice(1);
    const v = vistas[t] ? t : 'datos';
    document.querySelectorAll('[data-tab]').forEach(a => { if (a.dataset.tab === v) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current'); });
    vistas[v]();
  }
  window.addEventListener('hashchange', mostrar);
  document.addEventListener('favoritos', () => { if ((location.hash || '') === '#favoritos') vistas.favoritos(); });
  saludo(); mostrar();
})();
