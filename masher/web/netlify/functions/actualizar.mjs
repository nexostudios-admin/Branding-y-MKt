// Cada hora le pide a Netlify que vuelva a construir la web, así toma los cambios de la planilla de Google.
// Requiere la variable de entorno BUILD_HOOK_URL (Netlify > Site configuration > Build hooks).
export default async () => {
  const hook = process.env.BUILD_HOOK_URL;
  if (!hook) return new Response('Falta BUILD_HOOK_URL', { status: 200 });
  const r = await fetch(hook, { method: 'POST' });
  return new Response(`build pedido: ${r.status}`);
};
export const config = { schedule: '@hourly' };
