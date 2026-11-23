-- Masherr · panel de administración. Ejecutar una sola vez (SQL Editor → New query → Run), después de esquema.sql.
-- 1) Todos los pedidos quedan registrados (también los de clientes sin cuenta).
-- 2) Cada pedido tiene estado y monto (lo carga Masherr al cerrar la venta, porque la web no publica precios).
-- 3) Administradores: pueden ver todo y gestionar pedidos y cuentas empresa.

alter table public.pedidos alter column usuario drop not null;
alter table public.pedidos alter column usuario drop default;
alter table public.pedidos add column if not exists nombre text;
alter table public.pedidos add column if not exists telefono text;
alter table public.pedidos add column if not exists pago text;
alter table public.pedidos add column if not exists factura text;
alter table public.pedidos add column if not exists estado text not null default 'nuevo';
alter table public.pedidos add column if not exists monto numeric(14,2);
alter table public.pedidos add column if not exists nota_interna text;
alter table public.pedidos add column if not exists actualizado timestamptz not null default now();
do $$ begin
  alter table public.pedidos add constraint pedidos_estado_ok check (estado in ('nuevo','confirmado','entregado','cancelado'));
exception when duplicate_object then null; end $$;
create index if not exists pedidos_creado_idx on public.pedidos (creado desc);

-- Administradores
create table if not exists public.admins (
  usuario uuid primary key references auth.users (id) on delete cascade,
  creado timestamptz not null default now()
);
alter table public.admins enable row level security;

create or replace function public.es_admin() returns boolean language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.admins where usuario = auth.uid());
$$;
grant execute on function public.es_admin() to anon, authenticated;

drop policy if exists "admin se ve" on public.admins;
create policy "admin se ve" on public.admins for select to authenticated using (usuario = auth.uid());

-- Pedidos: cualquiera puede registrar su pedido (con o sin cuenta); solo admins ven todos y los gestionan.
drop policy if exists "pedidos propios crear" on public.pedidos;
drop policy if exists "pedidos crear" on public.pedidos;
create policy "pedidos crear" on public.pedidos for insert to anon, authenticated
  with check ((usuario is null or usuario = auth.uid()) and estado = 'nuevo' and monto is null and nota_interna is null
              and jsonb_typeof(items) = 'array' and jsonb_array_length(items) between 1 and 200);
drop policy if exists "pedidos admin ver" on public.pedidos;
create policy "pedidos admin ver" on public.pedidos for select to authenticated using (public.es_admin());
drop policy if exists "pedidos admin editar" on public.pedidos;
create policy "pedidos admin editar" on public.pedidos for update to authenticated using (public.es_admin()) with check (public.es_admin());

drop policy if exists "perfiles admin ver" on public.perfiles;
create policy "perfiles admin ver" on public.perfiles for select to authenticated using (public.es_admin());
drop policy if exists "favoritos admin ver" on public.favoritos;
create policy "favoritos admin ver" on public.favoritos for select to authenticated using (public.es_admin());
drop policy if exists "empresas admin ver" on public.empresas;
create policy "empresas admin ver" on public.empresas for select to authenticated using (public.es_admin());
drop policy if exists "empresas admin editar" on public.empresas;
create policy "empresas admin editar" on public.empresas for update to authenticated using (public.es_admin()) with check (public.es_admin());

-- El cliente no puede aprobarse solo; el administrador sí puede cambiar estado y nota.
create or replace function public.empresas_proteger_estado() returns trigger language plpgsql as $$
begin
  if auth.role() = 'authenticated' and not public.es_admin() then
    new.estado := old.estado;
    new.nota := old.nota;
  end if;
  return new;
end $$;

-- Lista de clientes registrados con email y fecha de alta (solo para administradores).
create or replace function public.admin_clientes()
returns table (id uuid, email text, alta timestamptz, ultimo_ingreso timestamptz, nombre text, telefono text, localidad text)
language sql stable security definer set search_path = public as $$
  select u.id, u.email::text, u.created_at, u.last_sign_in_at, p.nombre, p.telefono, p.localidad
  from auth.users u left join public.perfiles p on p.id = u.id
  where public.es_admin()
  order by u.created_at desc;
$$;
revoke all on function public.admin_clientes() from public, anon;
grant execute on function public.admin_clientes() to authenticated;

-- Para dar de alta un administrador (después de que se registre en la web y confirme el mail):
-- insert into public.admins (usuario) select id from auth.users where email = 'redesmasherr@gmail.com' on conflict do nothing;
