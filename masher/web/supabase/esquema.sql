-- Masherr · cuentas de clientes (Supabase). Ejecutar una sola vez en: SQL Editor → New query → Run.
-- Cada cliente solo ve y edita sus propios datos (Row Level Security).
-- El estado de las cuentas empresa solo lo cambia Masherr desde el panel de Supabase (Table Editor → empresas).

create table if not exists public.perfiles (
  id uuid primary key references auth.users (id) on delete cascade,
  nombre text, telefono text, direccion text, localidad text, cp text, pago text, factura text,
  actualizado timestamptz not null default now()
);

create table if not exists public.pedidos (
  id bigint generated always as identity primary key,
  usuario uuid not null default auth.uid() references auth.users (id) on delete cascade,
  items jsonb not null,            -- [{ "v": id_variante, "c": cantidad, "n": "nombre" }]
  entrega text, comentarios text,
  creado timestamptz not null default now()
);

create table if not exists public.favoritos (
  usuario uuid not null default auth.uid() references auth.users (id) on delete cascade,
  producto bigint not null,
  creado timestamptz not null default now(),
  primary key (usuario, producto)
);

create table if not exists public.empresas (
  usuario uuid primary key default auth.uid() references auth.users (id) on delete cascade,
  razon text not null, cuit text not null, iva text, rubro text, contacto text, telefono text,
  estado text not null default 'pendiente' check (estado in ('pendiente', 'aprobada', 'rechazada')),
  nota text,                         -- condiciones especiales que carga Masherr
  creado timestamptz not null default now()
);

alter table public.perfiles  enable row level security;
alter table public.pedidos   enable row level security;
alter table public.favoritos enable row level security;
alter table public.empresas  enable row level security;

drop policy if exists "perfil propio" on public.perfiles;
create policy "perfil propio" on public.perfiles for all to authenticated using (id = auth.uid()) with check (id = auth.uid());

drop policy if exists "pedidos propios ver" on public.pedidos;
drop policy if exists "pedidos propios crear" on public.pedidos;
create policy "pedidos propios ver" on public.pedidos for select to authenticated using (usuario = auth.uid());
create policy "pedidos propios crear" on public.pedidos for insert to authenticated with check (usuario = auth.uid());

drop policy if exists "favoritos propios" on public.favoritos;
create policy "favoritos propios" on public.favoritos for all to authenticated using (usuario = auth.uid()) with check (usuario = auth.uid());

drop policy if exists "empresa propia ver" on public.empresas;
drop policy if exists "empresa propia crear" on public.empresas;
drop policy if exists "empresa propia editar" on public.empresas;
create policy "empresa propia ver" on public.empresas for select to authenticated using (usuario = auth.uid());
create policy "empresa propia crear" on public.empresas for insert to authenticated with check (usuario = auth.uid() and estado = 'pendiente');
create policy "empresa propia editar" on public.empresas for update to authenticated using (usuario = auth.uid()) with check (usuario = auth.uid());

-- El cliente no puede aprobarse solo: si edita sus datos, el estado y la nota quedan como estaban.
create or replace function public.empresas_proteger_estado() returns trigger language plpgsql as $$
begin
  if auth.role() = 'authenticated' then
    new.estado := old.estado;
    new.nota := old.nota;
  end if;
  return new;
end $$;
drop trigger if exists empresas_proteger_estado on public.empresas;
create trigger empresas_proteger_estado before update on public.empresas
  for each row execute function public.empresas_proteger_estado();
