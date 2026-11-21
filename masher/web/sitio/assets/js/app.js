/* Masherr · funciones comunes: carrito, catálogo, WhatsApp, menú. Sin dependencias. */
(function () {
  'use strict';
  const CFG = window.MASHERR;
  const ROOT = document.documentElement.dataset.root || '';
  const CLAVE = 'masherr_carrito_v1';

  const fmt = n => '$' + Math.round(n).toLocaleString('es-AR');
  const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const img = (base, tam) => ROOT + base + (tam === 'g' ? '-1024-1024.webp' : '-480-0.webp');
  const icono = (id, cls = '') => `<svg class="icono ${cls}" aria-hidden="true" focusable="false"><use href="#i-${id}"></use></svg>`;

  // ---------- Catálogo ----------
  let catalogo = null;
  async function cargarCatalogo() {
    if (!catalogo) catalogo = fetch(ROOT + 'data/productos.json').then(r => { if (!r.ok) throw new Error('catálogo ' + r.status); return r.json(); });
    return catalogo;
  }

  // ---------- Carrito (en este navegador) ----------
  let memoria = [], persistente = true;
  function leer() {
    if (!persistente) return memoria.map(i => ({ ...i }));
    try { const v = JSON.parse(localStorage.getItem(CLAVE) || '[]'); return Array.isArray(v) ? v.filter(i => Number.isInteger(i.v) && i.c > 0) : []; }
    catch (e) { persistente = false; return memoria.map(i => ({ ...i })); }
  }
  function guardar(items) {
    memoria = items;
    try { localStorage.setItem(CLAVE, JSON.stringify(items)); } catch (e) { persistente = false; /* sin almacenamiento: el carrito dura mientras la página está abierta */ }
    actualizarBurbuja();
    document.dispatchEvent(new CustomEvent('carrito', { detail: items }));
  }
  memoria = leer();
  const carrito = {
    items: () => leer(),
    agregar(vid, cant = 1) {
      const items = carrito.items(); const it = items.find(i => i.v === vid);
      if (it) it.c = Math.min(999, it.c + cant); else items.push({ v: vid, c: cant });
      guardar(items);
    },
    cambiar(vid, cant) { guardar(carrito.items().map(i => i.v === vid ? { ...i, c: Math.max(1, Math.min(999, cant)) } : i)); },
    quitar(vid) { guardar(carrito.items().filter(i => i.v !== vid)); },
    vaciar() { guardar([]); },
    cantidad: () => carrito.items().reduce((a, i) => a + i.c, 0),
  };
  function actualizarBurbuja() {
    const n = carrito.cantidad();
    document.querySelectorAll('[data-burbuja]').forEach(b => { b.textContent = n; b.hidden = !n; });
    document.querySelectorAll('[data-carrito-label]').forEach(a => a.setAttribute('aria-label', `Carrito, ${n} ${n === 1 ? 'unidad' : 'unidades'}`));
  }

  // Busca la variante en el catálogo y devuelve {producto, variante}
  function resolver(cat, vid) {
    for (const p of cat.productos) { const v = p.variantes.find(x => x.id === vid); if (v) return { p, v }; }
    return null;
  }

  // ---------- WhatsApp ----------
  const wa = texto => `https://wa.me/${CFG.whatsapp}?text=${encodeURIComponent(texto)}`;

  // ---------- Avisos ----------
  let tt;
  function toast(html) {
    let t = document.getElementById('toast');
    if (!t) { t = document.createElement('div'); t.id = 'toast'; t.className = 'toast'; t.setAttribute('role', 'status'); document.body.appendChild(t); }
    t.innerHTML = `<span>${html.replace(/ <a /, '</span><a ')}`; t.hidden = false; clearTimeout(tt); tt = setTimeout(() => (t.hidden = true), 5000);
  }

  // ---------- Tarjeta de producto ----------
  function tarjeta(p) {
    const v = p.variantes[0];
    const sinStock = !p.disponible;
    const variasVar = p.variantes.length > 1;
    const boton = sinStock
      ? `<button class="boton agregar" type="button" disabled>Sin stock</button>`
      : variasVar
        ? `<a class="boton secundario agregar" href="${ROOT}producto/${p.slug}/">Elegir opción</a>`
        : `<button class="boton agregar" type="button" data-agregar="${v.id}" data-nombre="${esc(p.nombre)}">${icono('carrito')}Agregar</button>`;
    const fav = favoritos.tiene(p.id);
    return `<article class="tarjeta">
      <div class="foto">${p.imgs[0] ? `<img src="${img(p.imgs[0])}" alt="" width="480" height="480" loading="lazy" decoding="async">` : ''}
        <button class="fav" type="button" data-fav="${p.id}" aria-pressed="${fav}" aria-label="Guardar ${esc(p.nombre)} en favoritos">${icono('corazon')}</button>
        ${sinStock ? '<span class="sello">Sin stock</span>' : ''}</div>
      <div class="cuerpo">
        ${p.marca ? `<span class="marca">${esc(p.marca)}</span>` : ''}
        <h3><a href="${ROOT}producto/${p.slug}/">${esc(p.nombre)}</a></h3>
        <span class="precio${p.precio ? '' : ' consultar'}">${p.precio ? (variasVar ? '<span style="font-size:.6em">desde </span>' : '') + fmt(p.precio) : 'Consultá precio'}</span>
        <div class="t-acciones">${boton}<a class="t-wa" href="${wa('Hola Masherr, quiero consultar por: ' + p.nombre + '.')}" target="_blank" rel="noopener" aria-label="Consultar por WhatsApp">${icono('whatsapp')}</a></div>
      </div>
    </article>`;
  }

  // ---------- Favoritos (en este navegador; se sincronizan con la cuenta cuando esté activa) ----------
  const CLAVE_F = 'masherr_favoritos_v1';
  const favoritos = {
    lista() { try { const v = JSON.parse(localStorage.getItem(CLAVE_F) || '[]'); return Array.isArray(v) ? v : []; } catch (e) { return []; } },
    tiene(id) { return favoritos.lista().includes(+id); },
    alternar(id) {
      id = +id; const l = favoritos.lista(); const i = l.indexOf(id);
      if (i >= 0) l.splice(i, 1); else l.unshift(id);
      try { localStorage.setItem(CLAVE_F, JSON.stringify(l)); } catch (e) {}
      pintarFavoritos(); document.dispatchEvent(new CustomEvent('favoritos'));
      return i < 0;
    },
  };
  function pintarFavoritos() {
    const l = favoritos.lista();
    document.querySelectorAll('[data-fav]').forEach(b => b.setAttribute('aria-pressed', l.includes(+b.dataset.fav)));
    document.querySelectorAll('[data-fav-burbuja]').forEach(b => { b.textContent = l.length; b.hidden = !l.length; });
  }
  document.addEventListener('click', e => {
    const b = e.target.closest('[data-fav]'); if (!b) return;
    e.preventDefault();
    const agregado = favoritos.alternar(b.dataset.fav);
    toast(agregado ? `Guardado en favoritos <a href="${ROOT}cuenta/#favoritos">Ver favoritos</a>` : 'Quitado de favoritos');
  });

  // ---------- Banners rotativos ----------
  function iniciarSlider() {
    const s = document.querySelector('[data-slider]'); if (!s) return;
    const slides = [...s.querySelectorAll('[data-slide]')], dots = [...s.querySelectorAll('[data-ir]')];
    let k = 0, t;
    const ir = n => { k = (n + slides.length) % slides.length; slides.forEach((x, i) => (x.hidden = i !== k)); dots.forEach((d, i) => d.setAttribute('aria-current', i === k)); };
    const auto = () => { clearInterval(t); if (!matchMedia('(prefers-reduced-motion: reduce)').matches) t = setInterval(() => ir(k + 1), 6500); };
    dots.forEach(d => d.addEventListener('click', () => { ir(+d.dataset.ir); auto(); }));
    s.addEventListener('mouseenter', () => clearInterval(t)); s.addEventListener('mouseleave', auto);
    auto();
  }
  // ---------- Flechas de los carruseles de productos ----------
  document.addEventListener('click', e => {
    const b = e.target.closest('[data-riel]'); if (!b) return;
    const r = b.closest('section').querySelector('.riel');
    r.scrollBy({ left: +b.dataset.riel * r.clientWidth * .9, behavior: 'smooth' });
  });
  // ---------- Menú de categorías (teclado / táctil) ----------
  document.addEventListener('click', e => {
    const b = e.target.closest('[data-mm]');
    document.querySelectorAll('.megamenu.abierto').forEach(m => { if (!b || !m.contains(b)) { m.classList.remove('abierto'); m.querySelector('[data-mm]').setAttribute('aria-expanded', 'false'); } });
    if (b) { const m = b.closest('.megamenu'); const a = m.classList.toggle('abierto'); b.setAttribute('aria-expanded', a); }
  });

  // Delegación: botones "Agregar" en cualquier página
  document.addEventListener('click', e => {
    const b = e.target.closest('[data-agregar]');
    if (!b) return;
    carrito.agregar(+b.dataset.agregar, 1);
    toast(`Agregaste <b>${esc(b.dataset.nombre)}</b> <a href="${ROOT}carrito/">Ver carrito</a>`);
  });

  // Menú móvil
  document.addEventListener('click', e => {
    const b = e.target.closest('[data-menu]');
    if (!b) return;
    const m = document.getElementById('menu-movil');
    const abierto = m.classList.toggle('abierto');
    b.setAttribute('aria-expanded', abierto);
    b.innerHTML = icono(abierto ? 'cerrar' : 'menu') + `<span class="sr">${abierto ? 'Cerrar menú' : 'Abrir menú'}</span>`;
  });

  // ---------- Publicaciones de redes (se cargan solo si la persona lo pide) ----------
  const SCRIPTS = { instagram: 'https://www.instagram.com/embed.js', tiktok: 'https://www.tiktok.com/embed.js' };
  function cargarScript(src) {
    return new Promise(res => { if (document.querySelector(`script[src="${src}"]`)) return res(); const s = document.createElement('script'); s.src = src; s.async = true; s.onload = res; document.body.appendChild(s); });
  }
  function htmlPublicacion(pub) {
    if (pub.red === 'instagram') return `<blockquote class="instagram-media" data-instgrm-permalink="${esc(pub.url)}" data-instgrm-version="14" style="width:100%;margin:0"></blockquote>`;
    if (pub.red === 'tiktok') { const id = (pub.url.match(/video\/(\d+)/) || [])[1]; return `<blockquote class="tiktok-embed" cite="${esc(pub.url)}" data-video-id="${id}" style="margin:0"><section></section></blockquote>`; }
    if (pub.red === 'linkedin') { const urn = (pub.url.match(/(urn:li:(?:share|activity|ugcPost):\d+)/) || [])[1]; return urn ? `<iframe src="https://www.linkedin.com/embed/feed/update/${urn}" height="560" title="Publicación de LinkedIn" loading="lazy"></iframe>` : ''; }
    return '';
  }
  function iniciarRedes() {
    const cont = document.getElementById('publicaciones');
    if (!cont) return;
    const pubs = CFG.publicaciones || [];
    if (!pubs.length) { cont.closest('[data-bloque-pubs]')?.setAttribute('hidden', ''); return; }
    cont.innerHTML = pubs.map((p, i) => `<article class="pub"><div class="pub-cab">${icono(p.red)} <b>${({ instagram: 'Instagram', tiktok: 'TikTok', linkedin: 'LinkedIn' })[p.red]}</b></div>
      <div class="pub-cuerpo" data-pub="${i}"><div><p>${esc(p.titulo || 'Publicación')}</p><button class="boton secundario" type="button" data-cargar-pub="${i}">Ver publicación</button></div></div></article>`).join('');
    cont.addEventListener('click', async e => {
      const b = e.target.closest('[data-cargar-pub]'); if (!b) return;
      const p = pubs[+b.dataset.cargarPub]; const caja = cont.querySelector(`[data-pub="${b.dataset.cargarPub}"]`);
      caja.innerHTML = htmlPublicacion(p) || `<a href="${esc(p.url)}" target="_blank" rel="noopener">Abrir publicación</a>`;
      if (SCRIPTS[p.red]) { await cargarScript(SCRIPTS[p.red]); if (p.red === 'instagram' && window.instgrm) window.instgrm.Embeds.process(); }
    });
  }

  document.addEventListener('DOMContentLoaded', () => { actualizarBurbuja(); iniciarRedes(); pintarFavoritos(); iniciarSlider(); });
  window.addEventListener('storage', e => { if (e.key === CLAVE) { memoria = leer(); actualizarBurbuja(); document.dispatchEvent(new CustomEvent('carrito')); } });

  window.M = { CFG, ROOT, fmt, esc, img, icono, cargarCatalogo, carrito, resolver, wa, toast, tarjeta, favoritos, pintarFavoritos };
})();

/* Medición de contactos: eventos a Tag Manager (dataLayer) y, si hay IDs G-/AW- en config.json, a GA4 / Google Ads. */
(function () {
  const CONV = (window.MASHERR && window.MASHERR.ads_conversion) || {};
  function evento(nombre, extra) {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push(Object.assign({ event: nombre }, extra || {}));  // para Tag Manager
    if (!(window.MASHERR && window.MASHERR.gtag) || typeof window.gtag !== 'function') return;
    window.gtag('event', nombre, extra || {});  // GA4 / Google Ads directos
    if (CONV[nombre]) window.gtag('event', 'conversion', { send_to: CONV[nombre] });
  }
  document.addEventListener('click', e => {
    const a = e.target.closest('a'); if (!a) return;
    const h = a.getAttribute('href') || '';
    if (h.startsWith('tel:')) evento('click_llamar');
    else if (h.includes('chat.whatsapp.com')) evento('unirse_comunidad');
    else if (h.includes('wa.me')) evento('click_whatsapp');
    else if (a.dataset.evento === 'como_llegar' || h.includes('maps.app.goo.gl')) evento('click_como_llegar');
  });
  document.addEventListener('submit', e => {
    if (e.target.id === 'form-pedido') evento('pedido_whatsapp');
    if (e.target.id === 'form-empresas') evento('cotizacion_empresa');
  }, true);
  document.addEventListener('click', e => { if (e.target.closest('[data-agregar], #agregar')) evento('add_to_cart'); });
})();
