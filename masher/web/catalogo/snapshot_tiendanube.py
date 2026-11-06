"""Copia de SOLO LECTURA del catálogo público de la tienda Tiendanube de Masherr.

No reemplaza una exportación autorizada (CSV del admin o API): sirve para diagnosticar
y prototipar. Lee el sitemap, visita cada ficha y extrae lo que la página publica.
Campos que la página no publica quedan en null (desconocido), nunca en 0 ni inferidos.

Uso: python3 snapshot_tiendanube.py salida.json
"""
import html, json, re, sys, time, urllib.request

BASE = "https://masherrferreteria.mitiendanube.com"
UA = {"User-Agent": "Mozilla/5.0 (compatible; catalogo-masherr/1.0)"}

def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r:
        return r.read().decode("utf-8", "replace")

def jsonld(page):
    out = []
    for m in re.findall(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', page, re.S):
        try: out.append(json.loads(m))
        except json.JSONDecodeError: pass
    return out

def texto(fragmento):
    t = re.sub(r"<br\s*/?>|</p>|</li>", "\n", fragmento)
    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    return re.sub(r"[ \t]+", " ", re.sub(r"\n\s*\n+", "\n", t)).strip()

def descripcion(page):
    """Contenido del div.user-content dentro del bloque de descripción, respetando divs anidados."""
    i = page.find('data-store="product-description-')
    j = page.find('class="user-content', i) if i >= 0 else -1
    if j < 0: return None
    k = page.find('>', j) + 1
    nivel, pos = 1, k
    for m in re.finditer(r'<(/?)div\b', page[k:]):
        nivel += -1 if m.group(1) else 1
        if nivel == 0: return page[k:k + m.start()]
    return None

def ficha(url):
    page = get(url)
    datos = jsonld(page)
    web = next((d for d in datos if d.get("@type") == "WebPage" and d.get("mainEntity")), {})
    prod = web.get("mainEntity") or {}
    crumbs = [i["name"] for i in web.get("breadcrumb", {}).get("itemListElement", [])][1:-1]
    m = re.search(r'data-variants="([^"]*)"', page)
    variantes = json.loads(html.unescape(m.group(1))) if m else []
    desc = descripcion(page)
    # Solo la galería de la ficha (no las imágenes de productos relacionados), en orden.
    imgs = []
    for tag in re.findall(r'<img[^>]*js-product-slide-img[^>]*>', page):
        m_src = re.search(r'\ssrc="(//[^"]+?)-\d+-\d+\.webp"', tag)
        if m_src and m_src.group(1) + "-1024-1024.webp" not in imgs:
            imgs.append(m_src.group(1) + "-1024-1024.webp")
    pid = variantes[0]["product_id"] if variantes else None
    offer = prod.get("offers") or {}
    return {
        "id_tiendanube": pid,
        "url": url,
        "slug": url.rstrip("/").split("/")[-1],
        "nombre": html.unescape(prod.get("name") or "") or None,
        "marca": (prod.get("brand") or {}).get("name") if isinstance(prod.get("brand"), dict) else None,
        "categorias": crumbs or None,
        "descripcion": texto(desc) if desc else None,
        "moneda": offer.get("priceCurrency"),
        "peso_kg": float(prod["weight"]["value"]) if prod.get("weight") else None,
        "imagenes": ["https:" + i for i in imgs],
        "variantes": [{
            "id": v.get("id"),
            "sku": v.get("sku") or None,
            "opciones": [o for o in (v.get("option0"), v.get("option1"), v.get("option2")) if o] or None,
            "precio": v.get("price_number"),
            "precio_promocional": v.get("promotional_price_number") if v.get("has_promotional_price") else None,
            "precio_comparativo": v.get("compare_at_price_number"),
            "stock": v.get("stock"),  # null en Tiendanube = sin control de stock
            "disponible": v.get("available"),
            "solo_consulta": v.get("contact"),
        } for v in variantes],
        # No publicados en la ficha: quedan como desconocidos.
        "dimensiones": None, "garantia": None, "accesorios": None, "atributos": None,
    }

def main(salida):
    sm = get(BASE + "/sitemap.xml")
    urls = sorted(set(u for u in re.findall(r"<loc>(.*?)</loc>", sm) if re.search(r"/productos/[^/]+/$", u)))
    categorias = sorted(set(u for u in re.findall(r"<loc>(.*?)</loc>", sm) if "/productos/" not in u))
    productos, errores = [], []
    for i, u in enumerate(urls, 1):
        try: productos.append(ficha(u))
        except Exception as e: errores.append({"url": u, "error": str(e)})
        if i % 25 == 0: print(f"{i}/{len(urls)}", file=sys.stderr)
        time.sleep(0.6)
    json.dump({"fuente": BASE, "fecha": time.strftime("%Y-%m-%d"), "tipo": "copia pública de solo lectura",
               "paginas_sitemap": categorias, "productos": productos, "errores": errores},
              open(salida, "w"), ensure_ascii=False, indent=1)
    print(len(productos), "productos,", len(errores), "errores")

if __name__ == "__main__":
    main(sys.argv[1])
