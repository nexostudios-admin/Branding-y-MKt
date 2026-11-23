/* Masherr · cuentas de clientes con Supabase. La librería se carga solo cuando hace falta
   (página Mi cuenta o clientes con sesión iniciada). Sincroniza favoritos y pedidos con la cuenta. */
(function () {
  'use strict';
  const S = (window.MASHERR || {}).supabase || {};
  if (!S.url || !S.key) return;
  const ROOT = document.documentElement.dataset.root || '';
  const ref = new URL(S.url).hostname.split('.')[0];
  const CLAVE = `sb-${ref}-auth-token`;
  let cliente = null;

  function cargar() {
    if (cliente) return cliente;
    cliente = new Promise((res, rej) => {
      const crear = () => res(window.supabase.createClient(S.url, S.key, { auth: { flowType: 'implicit', detectSessionInUrl: true, persistSession: true, autoRefreshToken: true } }));
      if (window.supabase && window.supabase.createClient) return crear();
      const sc = document.createElement('script');
      sc.src = ROOT + 'assets/js/vendor/supabase.js'; sc.onload = crear; sc.onerror = () => rej(new Error('No se pudo cargar el servicio de cuentas'));
      document.head.appendChild(sc);
    });
    return cliente;
  }
  function sesionGuardada() { try { return JSON.parse(localStorage.getItem(CLAVE) || 'null'); } catch (e) { return null; } }
  const haySesion = () => !!sesionGuardada();
  async function usuario() { const c = await cargar(); const { data } = await c.auth.getSession(); return data.session ? data.session.user : null; }

  // Saludo en la cabecera
  function saludo() {
    const s = sesionGuardada(); const u = s && (s.user || (s.currentSession && s.currentSession.user));
    const n = u && u.user_metadata && u.user_metadata.nombre;
    document.querySelectorAll('[data-hola]').forEach(el => (el.textContent = u ? (n ? 'Hola, ' + n.split(' ')[0] : 'Hola') : 'Ingresá'));
  }

  // Favoritos y pedidos → cuenta
  document.addEventListener('favoritos', async e => {
    if (!haySesion() || !e.detail) return;
    try {
      const c = await cargar(); const u = await usuario(); if (!u) return;
      if (e.detail.agregado) await c.from('favoritos').upsert({ usuario: u.id, producto: e.detail.id });
      else await c.from('favoritos').delete().eq('usuario', u.id).eq('producto', e.detail.id);
    } catch (err) { /* sin conexión: queda guardado en este dispositivo */ }
  });
  // Todo pedido enviado queda registrado (con o sin cuenta) para el panel de ventas.
  document.addEventListener('pedido-enviado', e => {
    const ses = sesionGuardada(); const tok = ses && ses.access_token; const uid = ses && ses.user && ses.user.id;
    const enviar = conCuenta => fetch(S.url + '/rest/v1/pedidos', { method: 'POST', keepalive: true,
      headers: Object.assign({ apikey: S.key, 'Content-Type': 'application/json', Prefer: 'return=minimal' }, conCuenta ? { Authorization: 'Bearer ' + tok } : {}),
      body: JSON.stringify(Object.assign({}, e.detail, { usuario: conCuenta ? uid : null })) });
    enviar(!!(tok && uid)).then(r => { if (!r.ok && tok) return enviar(false); }).catch(() => {});
  });

  // Al iniciar sesión: une los favoritos del dispositivo con los de la cuenta
  async function sincronizarFavoritos() {
    const c = await cargar(); const u = await usuario(); if (!u || !window.M) return;
    const locales = window.M.favoritos.lista();
    if (locales.length) await c.from('favoritos').upsert(locales.map(id => ({ usuario: u.id, producto: id })), { ignoreDuplicates: true });
    const { data } = await c.from('favoritos').select('producto').order('creado', { ascending: false });
    if (data) window.M.favoritos.reemplazar([...new Set([...data.map(x => x.producto), ...locales])]);
  }

  const ERRORES = [
    [/invalid login credentials/i, 'Email o contraseña incorrectos.'],
    [/email not confirmed/i, 'Todavía no confirmaste tu email. Revisá tu casilla (y la carpeta de spam).'],
    [/already registered|already been registered|user already exists/i, 'Ya existe una cuenta con ese email. Ingresá o recuperá tu contraseña.'],
    [/password should be at least|weak password/i, 'La contraseña es muy corta: usá al menos 8 caracteres.'],
    [/rate limit|too many|security purposes/i, 'Hiciste varios intentos seguidos. Esperá unos minutos y probá de nuevo.'],
    [/invalid email|unable to validate email/i, 'Revisá que el email esté bien escrito.'],
    [/not authorized/i, 'Por ahora no pudimos enviar el mail a esa dirección. Escribinos por WhatsApp.'],
    [/same password|should be different/i, 'La nueva contraseña tiene que ser distinta a la anterior.'],
  ];
  const traducir = err => { const m = (err && err.message) || String(err || ''); const t = ERRORES.find(([re]) => re.test(m)); return t ? t[1] : 'No pudimos completar la operación. Probá de nuevo en unos minutos.'; };

  window.MA = { cargar, haySesion, usuario, sincronizarFavoritos, traducir, saludo, url: S.url };
  saludo();
  // Una sincronización por visita (no en cada página)
  let yaSinc = false; try { yaSinc = sessionStorage.getItem('masherr_sinc') === '1'; } catch (e) {}
  if (haySesion() && !yaSinc && !document.getElementById('cuenta-app')) cargar().then(sincronizarFavoritos).then(() => { try { sessionStorage.setItem('masherr_sinc', '1'); } catch (e) {} }).catch(() => {});
})();
