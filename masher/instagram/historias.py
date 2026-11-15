"""Historias institucionales de Masherr (horarios, apertura, cierre, contacto, pagos…). Las importa generar_placas.py."""

IC = {
 'reloj': '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
 'tel': '<svg viewBox="0 0 24 24"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/></svg>',
 'wa': '<svg viewBox="0 0 24 24"><path d="M3.5 20.5l1.4-4.2A8.5 8.5 0 1 1 8 19.3z"/><path d="M9 8.6c.2 2.9 2.6 5.4 5.6 6l1.3-1.4-2-1.1-1 .7c-.9-.4-2-1.5-2.4-2.4l.7-1-1-2z"/></svg>',
 'ig': '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5h.01"/></svg>',
 'tk': '<svg viewBox="0 0 24 24"><path d="M14 3v11.5a3.5 3.5 0 1 1-3.5-3.5"/><path d="M14 3c.5 2.6 2.4 4.5 5 4.8"/></svg>',
 'web': '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 2.5 15.3 0 18M12 3c-2.5 2.7-2.5 15.3 0 18"/></svg>',
 'pin': '<svg viewBox="0 0 24 24"><path d="M12 21s-7-6.2-7-12a7 7 0 0 1 14 0c0 5.8-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/></svg>',
 'cash': '<svg viewBox="0 0 24 24"><rect x="2.5" y="6" width="19" height="12" rx="2"/><circle cx="12" cy="12" r="2.6"/><path d="M6 9.5v5M18 9.5v5"/></svg>',
 'banco': '<svg viewBox="0 0 24 24"><path d="M3 9l9-5 9 5M5 9v8M9.5 9v8M14.5 9v8M19 9v8M3 20h18"/></svg>',
 'card': '<svg viewBox="0 0 24 24"><rect x="2.5" y="5" width="19" height="14" rx="2"/><path d="M2.5 10h19M6 15h4"/></svg>',
 'qr': '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><path d="M14 14h3v3M21 14v7h-4M14 18v3"/></svg>',
 'carrito': '<svg viewBox="0 0 24 24"><path d="M3 4h2l2.4 11.2a1 1 0 0 0 1 .8h9.2a1 1 0 0 0 1-.8L21 8H6.2"/><circle cx="9" cy="20" r="1.4"/><circle cx="18" cy="20" r="1.4"/></svg>',
}

def filas(items):
    return '<ul class="lista-st">' + ''.join(
        f'<li><i>{IC[i]}</i><div><b>{t}</b><span>{d}</span></div></li>' for i, t, d in items) + '</ul>'

def historias(LOGO_AZ, LOGO_BL):
    def hist(n, clase, rot, titulo, cuerpo):
        logo = LOGO_AZ if clase == 'claro' else LOGO_BL
        az = '' if clase == 'claro' else ' az'
        return ('story', n, f'<section class="story inst {clase}"><div class="rayas"></div><div class="rotulo{az}">{rot}</div>'
                            f'<h1>{titulo}</h1>{cuerpo}<div class="pie-st"><img src="{logo}" alt="Masherr">'
                            f'<span>Calle 38 4335 · Villa Lynch</span></div></section>')
    return [
     hist('h1_horarios', 'oscuro', 'HORARIOS', 'Te esperamos<br>en el local.',
          '<div class="horario"><div><b>Lunes a viernes</b><span>8:00 a 12:00</span><span>14:00 a 17:00</span></div>'
          '<div><b>Sábados</b><span>8:00 a 12:30</span></div>'
          '<div class="cerrado"><b>Domingos y feriados</b><span>Cerrado</span></div></div>'),
     hist('h2_abrimos', 'azul', 'BUEN DÍA', '¡Ya abrimos!',
          '<div class="hora-grande">8:00</div><p class="bajada">Pasá por el mostrador o hacé tu pedido por WhatsApp: '
          'te lo dejamos listo para retirar.</p>'),
     hist('h3_cerramos', 'oscuro', 'HASTA MAÑANA', 'Cerramos<br>por hoy.',
          '<p class="bajada">Mañana abrimos a las 8:00.<br>Mientras tanto, armá tu pedido en la web y te respondemos a primera hora.</p>'
          '<div class="chip-st">masherrferreteria.com.ar</div>'),
     hist('h4_mediodia', 'claro', 'MEDIODÍA', 'Volvemos<br>a las 14:00.',
          '<p class="bajada">Cerramos de 12:00 a 14:00. Dejanos tu consulta por WhatsApp y te respondemos a la vuelta.</p>'
          '<div class="chip-st wa">WhatsApp 11 3182-6166</div>'),
     hist('h5_contacto', 'oscuro', 'CONTACTO', 'Hablemos.', filas([
          ('tel', 'Teléfono', '011 4752-5210'), ('wa', 'WhatsApp', '11 3182-6166'),
          ('web', 'Tienda online', 'masherrferreteria.com.ar'), ('ig', 'Instagram', '@masherrferreteria'),
          ('tk', 'TikTok', '@masherrferreteria'), ('pin', 'Local', 'Calle 38 4335, Villa Lynch')])),
     hist('h6_pagos', 'claro', 'MEDIOS DE PAGO', '¿Cómo pagás?', filas([
          ('cash', 'Efectivo', 'En el local'), ('banco', 'Transferencia', 'Te pasamos los datos por WhatsApp'),
          ('card', 'Débito y crédito', 'Consultá cuotas vigentes'), ('qr', 'Mercado Pago', 'QR o link de pago')])),
     hist('h7_como_llegar', 'azul', 'CÓMO LLEGAR', 'Calle 38 4335,<br>Villa Lynch.',
          '<p class="bajada">Ex Hipólito Yrigoyen 4335, partido de General San Martín.</p>'
          '<div class="sticker osc">ACÁ VA EL STICKER DE UBICACIÓN</div>'),
     hist('h8_feriado', 'oscuro', 'AVISO', 'Feriado:<br>cerrado.',
          '<div class="fecha-hueco">__ / __</div><p class="bajada">Volvemos el día hábil siguiente en el horario de siempre. '
          'Podés dejar tu pedido en la web.</p>'),
     hist('h9_como_comprar', 'claro', 'COMPRÁ ONLINE', 'Del carrito<br>a WhatsApp.', filas([
          ('web', '1 · Entrá a la web', 'masherrferreteria.com.ar'), ('carrito', '2 · Armá tu carrito', 'Elegí productos y cantidades'),
          ('wa', '3 · Envialo por WhatsApp', 'Confirmamos precio, stock y retiro')])),
    ]

CSS_HIST = '''
section.story.inst{padding:300px 90px 0} .inst h1{font-size:124px;margin-top:40px}
.inst .bajada{font-size:44px;color:#DDE0E7;margin-top:50px} .inst.claro .bajada{color:#50566A}
.inst .rayas{width:360px;height:640px}
.claro .rayas{background:repeating-linear-gradient(to bottom,#EEF0F4 0 18px,transparent 18px 30px)}
.horario{margin-top:70px;border-top:3px solid var(--ce);position:relative}
.horario div{padding:40px 0;border-bottom:2px solid #2A2E3A;display:flex;flex-direction:column;gap:10px}
.horario b{font-family:C;font-size:44px;color:var(--ce);letter-spacing:.04em}
.horario span{font-family:C;font-size:84px;line-height:1.05}
.horario .cerrado span{color:#8C92A3;font-size:64px}
.hora-grande{font-family:C;font-size:300px;line-height:1;color:var(--ce);margin-top:80px;position:relative}
.chip-st{display:inline-block;margin-top:70px;font-family:C;font-size:46px;padding:30px 40px;border:4px solid var(--ce);color:#fff;position:relative}
.claro .chip-st{border-color:var(--az);color:var(--az)} .chip-st.wa{background:#128C3E;border-color:#128C3E;color:#fff}
.lista-st{list-style:none;margin-top:70px;position:relative}
.lista-st li{display:flex;gap:36px;align-items:center;padding:26px 0;border-bottom:2px solid #2A2E3A}
.claro .lista-st li{border-color:#DDE0E7}
.lista-st i{width:108px;height:108px;border-radius:50%;border:4px solid var(--ce);display:grid;place-items:center;flex:none}
.claro .lista-st i{border-color:var(--az)}
.lista-st svg{width:56px;height:56px;fill:none;stroke:var(--ce);stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.claro .lista-st svg{stroke:var(--az)}
.lista-st b{display:block;font-family:C;font-size:50px} .lista-st span{display:block;font-size:36px;color:#B9BDC8;margin-top:6px}
.claro .lista-st span{color:var(--tx)}
.fecha-hueco{font-family:C;font-size:200px;color:var(--ce);margin-top:70px;letter-spacing:.06em}
.pie-st{position:absolute;left:90px;right:90px;bottom:120px;display:flex;justify-content:space-between;align-items:center;border-top:3px solid var(--ce);padding-top:40px}
.claro .pie-st{border-color:var(--az)}
.pie-st img{height:84px} .pie-st span{font-family:C;font-size:32px;color:var(--ce)} .claro .pie-st span{color:var(--az)}
'''
