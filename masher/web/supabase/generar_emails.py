"""Plantillas de mail de Supabase Auth con la marca Masherr (HTML de tablas con estilos en línea, compatible con Gmail/Outlook)."""
from pathlib import Path
SITIO = 'https://masherrferreteria.com.ar'
WA = 'https://wa.me/5491131826166'

def mail(preheader, rotulo, titulo, texto, boton, nota):
    return f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Masherr</title></head>
<body style="margin:0;padding:0;background:#EEF0F4;">
<div style="display:none;max-height:0;overflow:hidden;opacity:0;">{preheader}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#EEF0F4;">
<tr><td align="center" style="padding:24px 12px;">
  <table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="width:100%;max-width:600px;background:#FFFFFF;border-radius:14px;overflow:hidden;">
    <tr><td style="background:#08090B;"><a href="{SITIO}"><img src="{SITIO}/assets/img/email/cabecera.png" width="600" alt="Masherr · máquinas - herramientas" style="display:block;width:100%;max-width:600px;height:auto;border:0;"></a></td></tr>
    <tr><td style="padding:40px 40px 8px;font-family:Arial,Helvetica,sans-serif;">
      <p style="margin:0 0 12px;font-size:12px;letter-spacing:2px;text-transform:uppercase;color:#17256B;font-weight:bold;">&#8212;&nbsp;{rotulo}</p>
      <h1 style="margin:0 0 16px;font-size:30px;line-height:1.1;color:#08090B;font-weight:bold;">{titulo}</h1>
      <p style="margin:0 0 28px;font-size:16px;line-height:1.6;color:#50566A;">{texto}</p>
      <table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" bgcolor="#17256B" style="border-radius:999px;">
        <a href="{{{{ .ConfirmationURL }}}}" style="display:inline-block;padding:15px 32px;font-family:Arial,Helvetica,sans-serif;font-size:16px;font-weight:bold;color:#FFFFFF;text-decoration:none;border-radius:999px;">{boton}</a>
      </td></tr></table>
      <p style="margin:24px 0 0;font-size:13px;line-height:1.6;color:#50566A;">Si el botón no funciona, copiá y pegá este enlace en tu navegador:<br><a href="{{{{ .ConfirmationURL }}}}" style="color:#17256B;word-break:break-all;">{{{{ .ConfirmationURL }}}}</a></p>
      <p style="margin:20px 0 0;font-size:13px;line-height:1.6;color:#8A90A2;">{nota}</p>
    </td></tr>
    <tr><td style="padding:28px 40px 36px;font-family:Arial,Helvetica,sans-serif;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-top:1px solid #D9DCE4;"><tr><td style="padding-top:22px;font-size:14px;line-height:1.6;color:#50566A;">
        ¿Dudas? Escribinos por <a href="{WA}" style="color:#128C3E;font-weight:bold;text-decoration:none;">WhatsApp 11 3182-6166</a>
      </td></tr></table>
    </td></tr>
    <tr><td style="background:#17256B;padding:20px 40px;font-family:Arial,Helvetica,sans-serif;font-size:12px;line-height:1.6;color:#C9CDDA;">
      <b style="color:#FFFFFF;">Ferretería Industrial Masherr</b><br>
      Calle 38 (ex Hipólito Yrigoyen) 4335 · Villa Lynch, San Martín<br>
      <a href="{SITIO}" style="color:#9AAEFF;text-decoration:none;">masherrferreteria.com.ar</a>
    </td></tr>
  </table>
</td></tr></table>
</body></html>
'''

PLANTILLAS = {
  'confirmar_registro': ('Confirmá tu cuenta de Masherr', 'Confirmá tu cuenta en Masherr',
      mail('Un paso más para activar tu cuenta.', 'Bienvenido a Masherr', '¡Ya casi tenés tu cuenta!',
           'Gracias por registrarte en Masherr. Confirmá tu email para guardar tus datos, ver tus pedidos y tus favoritos desde cualquier dispositivo.',
           'Confirmar mi cuenta', 'Si no creaste una cuenta en Masherr, ignorá este mensaje.')),
  'recuperar_contrasena': ('Restablecé tu contraseña de Masherr', 'Restablecé tu contraseña',
      mail('Pediste cambiar tu contraseña.', 'Tu cuenta Masherr', 'Restablecé tu contraseña',
           'Recibimos un pedido para cambiar la contraseña de tu cuenta en Masherr. Tocá el botón para elegir una nueva.',
           'Elegir nueva contraseña', 'Si no pediste el cambio, ignorá este mensaje: tu contraseña sigue igual.')),
  'cambio_email': ('Confirmá tu nuevo email en Masherr', 'Confirmá tu nuevo email',
      mail('Confirmá el cambio de email de tu cuenta.', 'Tu cuenta Masherr', 'Confirmá tu nuevo email',
           'Pediste cambiar el email de tu cuenta en Masherr. Confirmá que este es tu nuevo correo.',
           'Confirmar nuevo email', 'Si no pediste el cambio, escribinos por WhatsApp.')),
  'enlace_ingreso': ('Tu enlace para ingresar a Masherr', 'Ingresá a tu cuenta',
      mail('Tu enlace de ingreso.', 'Tu cuenta Masherr', 'Ingresá a tu cuenta',
           'Tocá el botón para ingresar a tu cuenta de Masherr. El enlace vence en un rato.',
           'Ingresar a Masherr', 'Si no pediste ingresar, ignorá este mensaje.')),
}
d = Path(__file__).parent / 'emails'
for k, (asunto, _, html) in PLANTILLAS.items():
    (d / f'{k}.html').write_text(html)
    print(k, '·', asunto)
