#!/usr/bin/env python3
"""Generates the static multi-page site. Usage: python3 tools/build.py .  (run from repo root)
Edit content here, not in the generated *.html files."""
import sys, pathlib, json

OUT = pathlib.Path(sys.argv[1])

FB_URL = "https://www.facebook.com/p/Sylwia-Hurtownia-warzyw-i-owoc%C3%B3w-100070774976242/"
# Stock photos (img/stock-*.webp) are licensed Adobe Stock previews –
# replace with the full-resolution files under the same names.

PHONE_SVG = '<svg aria-hidden="true" viewBox="0 0 24 24"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
PIN_SVG = '<svg aria-hidden="true" viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>'
TRUCK_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 8h-3V4H3a2 2 0 0 0-2 2v11h2a3 3 0 0 0 6 0h6a3 3 0 0 0 6 0h2v-5zm-.5 1.5L21.46 12H17V9.5zM6 18.5A1.5 1.5 0 1 1 6 15.5a1.5 1.5 0 0 1 0 3zm12 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3z"/></svg>'
LEAF_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17 8C8 10 5.9 16.2 3.8 21.3l1.9.7 1-2.3c.5.2 1 .3 1.3.3C19 20 22 3 22 3c-1 2-8 2.3-13 3.3S2 11.5 2 13.5s1.8 3.8 1.8 3.8C7 8 17 8 17 8z"/></svg>'
PEOPLE_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zm-6 1a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm12 0a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM12 14c-3 0-6 1.5-6 4v2h12v-2c0-2.5-3-4-6-4zm-6.6.6C3 14.9 1 16 1 18v2h3.5v-2c0-1.3.4-2.4 1-3.4zm13.2 0c.6 1 1 2.1 1 3.4v2H23v-2c0-2-2-3.1-4.4-3.4z"/></svg>'
CHEF_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3a4.5 4.5 0 0 0-4.2 2.9A4 4 0 0 0 6 13.7V20a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1v-6.3a4 4 0 0 0-1.8-7.8A4.5 4.5 0 0 0 12 3zM8 18v-3.3h8V18z"/></svg>'
STORE_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 4h18l1 5a3 3 0 0 1-5 2.2A3 3 0 0 1 12 11a3 3 0 0 1-5 .2A3 3 0 0 1 2 9zm1 9.5a4.8 4.8 0 0 0 3-.4 4.9 4.9 0 0 0 5 0 4.9 4.9 0 0 0 5 0 4.8 4.8 0 0 0 3 .4V21H4zM9 15v4h6v-4z"/></svg>'
BOX_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21 7.5 12 3 3 7.5v9L12 21l9-4.5zM12 5.2l5.6 2.8L12 10.8 6.4 8zM5 9.6l6 3v6l-6-3zm8 9v-6l6-3v6z"/></svg>'
CAL_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M19 4h-1V2h-2v2H8V2H6v2H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 16H5V9h14zM7 11h5v5H7z"/></svg>'
FB_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.5 22v-8h2.7l.4-3.2h-3.1V8.8c0-.9.3-1.5 1.6-1.5h1.7V4.4a22 22 0 0 0-2.5-.1c-2.5 0-4.2 1.5-4.2 4.3v2.3H7.4V14h2.7v8z"/></svg>'

CUR = ' aria-current="page"'
WA_URL = "https://wa.me/48782272727"
WA_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1l-.9 1.2c-.2.2-.3.2-.6.1a8.2 8.2 0 0 1-4-3.5c-.3-.5.3-.5.9-1.6.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6a1.1 1.1 0 0 0-.8.4 3.4 3.4 0 0 0-1 2.5 5.9 5.9 0 0 0 1.2 3.1 13.4 13.4 0 0 0 5.2 4.6c1.9.8 2.7.9 3.6.7a3.1 3.1 0 0 0 2-1.4 2.5 2.5 0 0 0 .2-1.4c-.1-.1-.3-.2-.6-.3zM12 21.8a9.8 9.8 0 0 1-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 1 1 12 21.8zm8.4-18.2A11.8 11.8 0 0 0 1.8 17.8L.1 24l6.4-1.7a11.8 11.8 0 0 0 5.6 1.4A11.9 11.9 0 0 0 20.4 3.6z"/></svg>'

CITIES = ["Legnica", "Lubin", "Głogów", "Polkowice", "Jawor", "Złotoryja",
          "Prochowice", "Chojnów", "Bolesławiec", "Jelenia Góra",
          "Zielona Góra", "Gorzów Wielkopolski", "Opole", "Kędzierzyn-Koźle",
          "Łódź", "Piotrków Trybunalski"]

NAV = [
    ("asortyment.html", "Asortyment"),
    ("dostawa.html", "Dostawa"),
    ("dla-firm.html", "Oferta dla firm"),
    ("o-nas.html", "O nas"),
    ("kontakt.html", "Kontakt"),
]


def social(cls="social"):
    return f'''<div class="{cls}">
        <a href="{FB_URL}" target="_blank" rel="noopener" aria-label="Facebook – Hurtownia Sylwia">{FB_SVG}</a>
        <a href="{WA_URL}" target="_blank" rel="noopener" aria-label="WhatsApp – napisz do nas">{WA_SVG}</a>
      </div>'''


def page(file, title, desc, body, og_image="img/hero-kosz.webp"):
    nav = "\n      ".join(
        f'<a href="{href}"{CUR if href == file else ""}>{label}</a>'
        for href, label in NAV)
    foot_nav = "\n        ".join(f'<a href="{h}">{l}</a>' for h, l in NAV)
    full_title = title if file == "index.html" else f"{title} – Hurtownia Sylwia, Legnica"
    html = f'''<!doctype html>
<html lang="pl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{full_title}</title>
  <meta name="description" content="{desc}">
  <link rel="icon" href="img/favicon.svg" type="image/svg+xml">
  <meta property="og:title" content="{full_title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{og_image}">
  <link rel="preload" href="fonts/jost-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="css/style.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "GroceryStore",
    "name": "Hurtownia Sylwia – warzywa i owoce",
    "telephone": "+48 782 272 727",
    "url": "https://www.warzywaiowoce.legnica.pl",
    "sameAs": ["{FB_URL}"],
    "areaServed": {{"@type": "Country", "name": "Polska"}},
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "ul. Bydgoska 18",
      "addressLocality": "Legnica",
      "addressCountry": "PL"
    }}
  }}
  </script>
</head>
<body>

<header class="site-header">
  <div class="wrap header-inner">
    <a href="index.html" class="brand" aria-label="Hurtownia Sylwia – strona główna">
      <img src="img/logo.svg" alt="Sylwia – hurtownia warzyw i owoców z Legnicy" width="210" height="94">
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
    <nav id="nav" class="nav">
      {nav}
      <a href="tel:+48782272727" class="btn btn-red btn-sm">
        {PHONE_SVG}
        782 272 727
      </a>
    </nav>
  </div>
</header>

<main>
{body}
</main>

<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <img src="img/logo-white.svg" alt="Sylwia – hurtownia warzyw i owoców z Legnicy" class="footer-logo" width="200" height="90">
    </div>
    <div class="footer-info">
      <p class="footer-h">Kontakt</p>
      <p>Legnica, ul. Bydgoska 18</p>
      <p><a href="tel:+48782272727">+48 782 272 727</a></p>
    </div>
    <nav class="footer-nav" aria-label="Stopka">
      <p class="footer-h">Strony</p>
        {foot_nav}
        <a href="zamow/">Aplikacja do zamówień</a>
    </nav>
    <div>
      <p class="footer-h">Obserwuj nas</p>
      {social("social social-light")}
    </div>
  </div>
  <div class="wrap footer-bottom">
    <p>© <span id="year">2026</span> Hurtownia Sylwia · warzywa i owoce z Legnicy · <a href="polityka-prywatnosci.html">Polityka prywatności</a> · <a href="#" data-cookie-settings>Ustawienia cookies</a></p>
  </div>
</footer>

<div class="fabs">
  <a href="{WA_URL}" class="fab fab-wa" target="_blank" rel="noopener" aria-label="Napisz do nas na WhatsApp">
    {WA_SVG}<span class="fab-label">Napisz na WhatsApp</span>
  </a>
  <a href="tel:+48782272727" class="fab fab-call" aria-label="Zadzwoń do hurtowni">
    {PHONE_SVG}
  </a>
</div>

<script>
  const t = document.querySelector('.nav-toggle'), n = document.getElementById('nav');
  t.addEventListener('click', () => {{
    const open = n.classList.toggle('open');
    t.setAttribute('aria-expanded', open);
  }});
  document.querySelectorAll('[data-soon]').forEach(a => a.addEventListener('click', e => e.preventDefault()));
  document.getElementById('year').textContent = new Date().getFullYear();
</script>
<script src="js/cookies.js" defer></script>
</body>
</html>
'''
    (OUT / file).write_text(html, encoding="utf-8")


def page_head(hand, h1, lead, img=None):
    bg = f' style="background-image: url(img/{img})"' if img else ""
    cls = "page-hero has-img" if img else "page-hero"
    return f'''
  <section class="{cls}"{bg}>
    <div class="wrap">
      <p class="hand">{hand}</p>
      <h1>{h1}</h1>
      <p class="lead">{lead}</p>
    </div>
  </section>'''


def cities_list():
    return "\n".join(f'          <li>{PIN_SVG}{c}</li>' for c in CITIES)


def b2b_band(title="Prowadzisz restaurację? Współpracuj z nami!",
             text="Sklep, restauracja, kawiarnia czy catering – przygotujemy stałe zamówienie pod Twoją kuchnię i dowieziemy je pod drzwi.",
             link=True):
    more = '<a href="dla-firm.html" class="btn btn-outline-white">Oferta dla firm</a>' if link else ""
    return f'''
  <section class="b2b">
    <div class="wrap b2b-inner">
      <div>
        <p class="hand hand-light">Dla sklepów i gastronomii</p>
        <h2>{title}</h2>
        <p>{text}</p>
      </div>
      <div class="b2b-cta">
        <a href="tel:+48782272727" class="btn btn-white">Zadzwoń: 782 272 727</a>
        <a href="{WA_URL}" class="btn btn-wa" target="_blank" rel="noopener">{WA_SVG} WhatsApp</a>
        {more}
      </div>
    </div>
  </section>'''


CARDS = [
    ("warzywa-korzeniowe.webp", "Warzywa korzeniowe: ziemniaki, marchew, cebula, czosnek, topinambur, batat", 1080, 482,
     "Warzywa", "Ziemniaki, marchew, cebula, czosnek, buraki, kapusty, warzywa korzeniowe i sezonowe nowalijki."),
    ("miechunka.webp", "Miechunka (physalis) w opakowaniu", 803, 803,
     "Owoce", "Jabłka, cytrusy, owoce sezonowe i egzotyczne – od bananów po granaty i miechunkę."),
    ("bazylia.webp", "Świeża bazylia", 803, 501,
     "Świeże zioła", "Bazylia, mięta, tymianek, rozmaryn – cięte w pęczkach i w doniczkach."),
    ("jarmuz.webp", "Pęczek jarmużu", 802, 803,
     "Sałaty i liście", "Jarmuż, sałaty, szpinak, rukola i inne zielone liście dla kuchni restauracyjnych, barów sałatkowych i cateringu."),
    ("bakalie.webp", "Suszone owoce: morele, daktyle, śliwki, jagody goji, żurawina", 1080, 612,
     "Bakalie i suszone owoce", "Morele, daktyle, śliwki, figi, żurawina, goji i orzechy."),
    ("lawenda.webp", "Lawenda w doniczce", 802, 740,
     "Rośliny w doniczkach", "Sezonowo: lawenda i zioła doniczkowe – dla sklepów, kwiaciarni i marketów."),
]


def cards(items):
    out = []
    for img, alt, w, h, title, text in items:
        out.append(f'''        <article class="card">
          <img src="img/{img}" alt="{alt}" loading="lazy" width="{w}" height="{h}">
          <div class="card-body">
            <h3>{title}</h3>
            <p>{text}</p>
          </div>
        </article>''')
    return '<div class="cards">\n' + "\n".join(out) + "\n      </div>"


SEASON = '''
  <section class="section section-tint" id="sezon">
    <div class="wrap">
      <div class="section-head">
        <p class="hand">Teraz w sezonie</p>
        <h2>Co teraz najlepsze</h2>
        <p>Jesienią królują jabłka i śliwki, zimą cytrusy – słodkie mandarynki i soczyste pomarańcze w pełnych skrzynkach, prosto na półkę Twojego sklepu.</p>
      </div>
      <div class="promo-grid">
        <article class="promo">
          <img src="img/stock-jesien.webp" alt="Wiklinowy kosz z jabłkami, śliwkami i winogronami wśród jesiennych liści" loading="lazy" width="718" height="614">
          <div class="promo-body">
            <span class="tag tag-green">Jesień</span>
            <h3>Jabłka i śliwki z polskich sadów</h3>
            <p>Chrupiące jabłka, słodkie śliwki i winogrona – najlepsze, co daje polska jesień, prosto do Twojego sklepu i kuchni.</p>
          </div>
        </article>
        <article class="promo">
          <img src="img/mandarynki.webp" alt="Mandarynki, laski cynamonu i anyż na drewnianym stole" loading="lazy" width="940" height="425">
          <div class="promo-body">
            <span class="tag">Grudzień</span>
            <h3>Czas mandarynek i pomarańczy</h3>
            <p>Słodkie, soczyste i łatwe do obierania. Hurtowe ilości w skrzynkach – zatowaruj sklep przed świętami, kiedy cytrusy schodzą najszybciej.</p>
          </div>
        </article>
        <article class="promo">
          <img src="img/mikolajki.webp" alt="Dziecko obiera mandarynkę obok pierników" loading="lazy" width="1200" height="520">
          <div class="promo-body">
            <span class="tag tag-red">6 grudnia</span>
            <h3>Zdrowa paczka na Mikołajki</h3>
            <p>Zamiast słodyczy – owoce. Skompletujemy paczki mikołajkowe dla firm, szkół i przedszkoli – dla pracowników, ich dzieci czy klientów. Zadzwoń i ustal szczegóły.</p>
          </div>
        </article>
      </div>
    </div>
  </section>'''


SEAL_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 1 3 5v6c0 5.5 3.8 10.7 9 12 5.2-1.3 9-6.5 9-12V5zm-1.5 15.5-4-4 1.4-1.4 2.6 2.6 6.1-6.1 1.4 1.4z"/></svg>'

# Certificates: PDFs in certyfikaty/certyfikat-<key>.pdf, thumbnails in img/cert-<key>.webp
# (first page rendered from the PDF). Cards link to the PDF in a new tab.
CERT_LIST = [
    ("iso22000", "ISO<br>22000", "ISO 22000",
     "Międzynarodowy system zarządzania bezpieczeństwem żywności. Kontrolowany proces od przyjęcia towaru po dostawę do klienta."),
    ("haccp", "HACCP", "HACCP",
     "System analizy zagrożeń i krytycznych punktów kontroli. Higiena i jakość pilnowane na każdym etapie – także przy warzywach obieranych."),
]


def cert_strip():
    return '\n        <div class="cert-strip">' + "".join(
        f'\n          <a class="cert-mini" href="certyfikaty/certyfikat-{k}.pdf" target="_blank" rel="noopener">{SEAL_SVG}Certyfikat {n}</a>'
        for k, _, n, _ in CERT_LIST) + '\n        </div>'


def certs(lead="Pracujemy według uznanych standardów bezpieczeństwa żywności – to gwarancja dla Twojej kuchni, sklepu i Twoich klientów."):
    cards = []
    for key, badge, name, desc in CERT_LIST:
        if (OUT / "img" / f"cert-{key}.webp").exists():
            visual = (f'<a class="cert-photo" href="certyfikaty/certyfikat-{key}.pdf" target="_blank" rel="noopener" title="Otwórz certyfikat {name} (PDF)">'
                      f'<img src="img/cert-{key}.webp" alt="Certyfikat {name} – Hurtownia Sylwia" loading="lazy" width="480" height="679"></a>')
            link = (f'<a class="cert-link" href="certyfikaty/certyfikat-{key}.pdf" target="_blank" rel="noopener">'
                    f'Zobacz certyfikat (PDF) →</a>')
        else:
            visual = f'<div class="cert-seal"><span>{badge}</span><small>certyfikat</small></div>'
            link = ""
        cards.append(f'''
        <article class="cert-card">
          {visual}
          <div>
            <p class="cert-check">{SEAL_SVG}Certyfikowana jakość</p>
            <h3>{name}</h3>
            <p>{desc}</p>
            {link}
          </div>
        </article>''')
    return f'''
  <section class="section certs" id="certyfikaty">
    <div class="wrap">
      <div class="section-head">
        <p class="hand">Bezpieczeństwo żywności</p>
        <h2>Certyfikaty ISO 22000 i HACCP</h2>
        <p>{lead}</p>
      </div>
      <div class="cert-grid">{"".join(cards)}
      </div>
    </div>
  </section>'''


PEELED = f'''
  <section class="section" id="obierane">
    <div class="wrap split">
      <div>
        <p class="hand">Gotowe do gotowania</p>
        <h2>Warzywa obierane</h2>
        <p class="muted">Obrane ziemniaki, marchew, cebula, buraki i inne warzywa – gotowe do użycia w kuchni. Oszczędzasz czas i ręce do pracy, a my dowozimy je świeże, na konkretny dzień.</p>
        <ul class="ticks">
          <li>Dla restauracji, stołówek i cateringu</li>
          <li>Stałe zamówienia na wybrane dni</li>
          <li>Pakowane higienicznie, zgodnie z HACCP</li>
        </ul>
        <p><a href="tel:+48782272727" class="btn btn-red">Zapytaj o warzywa obierane</a></p>
      </div>
      <div class="split-photo">
        <img src="img/warzywa-obierane.webp" alt="Obrane ziemniaki – warzywa obierane z hurtowni Sylwia" width="1200" height="896" loading="lazy">
      </div>
    </div>
  </section>'''


def app_products():
    """Reads categories/products from zamow/products.js (single source of truth)."""
    import re
    js = (OUT / "zamow" / "products.js").read_text(encoding="utf-8")
    cats = re.findall(r'\{ id: "(\w+)", name: "([^"]+)", icon:', js)
    prods = []
    for line in js.splitlines():
        m = re.search(r'cat: "(\w+)", name: "([^"]+)".*?img: "([^"]+)"', line)
        if m:
            img = m.group(3)
            img = img[3:] if img.startswith("../") else "zamow/" + img
            prods.append((m.group(1), m.group(2), img, "peeled: true" in line))
    return cats, prods


def product_list():
    cats, prods = app_products()
    out = []
    for cid, cname in cats:
        items = [p for p in prods if p[0] == cid]
        if not items:
            continue
        tiles = "".join(f'''
          <figure class="pl-item"><img src="{img}" alt="{name}" loading="lazy">{'<span class="pl-badge">obrane</span>' if peeled else ""}<figcaption>{name}</figcaption></figure>''' for _, name, img, peeled in items)
        out.append(f'''
      <h3 class="pl-cat">{"Warzywa obierane" if cid == "obrane" else cname}</h3>
      <div class="pl-grid">{tiles}
      </div>''')
    return "".join(out)


def features():
    items = [
        (LEAF_SVG, "Świeży towar", "Dostawy na bieżąco – to, co trafia na półkę, jest jędrne, pachnące i gotowe do sprzedaży."),
        (TRUCK_SVG, "Dostawa w całej Polsce", "Dowozimy własnymi samochodami – codziennie po Legnicy i okolicy, a dostawy realizujemy na terenie całej Polski."),
        (PEOPLE_SVG, "Rodzinna firma od 33 lat", "Znamy naszych klientów po imieniu. Doradzimy, zarezerwujemy towar i pomożemy skompletować zamówienie."),
    ]
    return '''
  <section class="features">
    <div class="wrap features-grid">''' + "".join(f'''
      <div class="feature">
        <div class="feature-icon">{i}</div>
        <h3>{t}</h3>
        <p>{p}</p>
      </div>''' for i, t, p in items) + '''
    </div>
  </section>'''


# ---------------- HOME ----------------
home = f'''
  <section class="hero">
    <div class="wrap hero-inner">
      <div class="hero-text">
        <p class="hand">Rodzinna hurtownia z Legnicy – od 33 lat</p>
        <h1>Świeża energia<br><span>prosto z pól</span></h1>
        <p class="lead">Warzywa, owoce, warzywa obierane, świeże zioła i bakalie w hurtowych ilościach – dla sklepów, restauracji, cateringu i firm. Codziennie wybieramy towar tak, jak dla własnej rodziny.</p>
        <div class="hero-cta">
          <a href="tel:+48782272727" class="btn btn-red">Zadzwoń: 782 272 727</a>
          <a href="{WA_URL}" class="btn btn-wa" target="_blank" rel="noopener">{WA_SVG} WhatsApp</a>
          <a href="asortyment.html" class="btn btn-ghost">Zobacz asortyment</a>
        </div>
{cert_strip()}
        <p class="hero-address">
          {PIN_SVG}
          Legnica, ul. Bydgoska 18
        </p>
      </div>
      <div class="hero-photo">
        <img src="img/hero-kosz.webp" alt="Kosz pełen świeżych warzyw i owoców: brokuły, pomidory, granat, pomarańcza, marchew" width="500" height="675">
        <img class="hero-badge" src="img/favicon.svg" alt="" aria-hidden="true">
      </div>
    </div>
  </section>
{features()}
{certs()}

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <p class="hand">Co u nas znajdziesz</p>
        <h2>Asortyment</h2>
        <p>Klasyka z polskich pól i trochę egzotyki. Asortyment zmienia się z porami roku.</p>
      </div>
      {cards(CARDS[:3])}
      <p class="center-cta"><a href="asortyment.html" class="btn btn-ghost">Cały asortyment</a></p>
    </div>
  </section>
{SEASON}

  <section class="section">
    <div class="wrap split">
      <div class="split-photo">
        <img src="img/flota.webp" alt="Dwa samochody dostawcze Hurtowni Sylwia z grafiką owoców i warzyw" loading="lazy" width="960" height="720">
      </div>
      <div>
        <p class="hand">Gdzie dostarczamy</p>
        <h2>Cała Polska</h2>
        <p class="muted">Własnymi samochodami dowozimy towar na terenie całej Polski. Codziennie jeździmy m.in. do:</p>
        <ul class="cities">
{cities_list()}
        </ul>
        <a href="dostawa.html" class="btn btn-red">Szczegóły dostawy</a>
      </div>
    </div>
  </section>
{b2b_band()}

  <section class="section">
    <div class="wrap visit">
      <div>
        <p class="hand">Zapraszamy</p>
        <h2>Hurtownia przy Bydgoskiej</h2>
        <p class="muted">Legnica, ul. Bydgoska 18. Odbierz zamówienie w hurtowni albo zadzwoń i zamów z dostawą.</p>
        <div class="contact-cta">
          <a href="kontakt.html" class="btn btn-red">Kontakt i dojazd</a>
          <a href="{FB_URL}" class="btn btn-ghost" target="_blank" rel="noopener">{FB_SVG} Facebook</a>
        </div>
      </div>
    </div>
  </section>'''

page("index.html", "Hurtownia Sylwia – warzywa i owoce z Legnicy",
     "Rodzinna hurtownia warzyw i owoców w Legnicy. Świeże warzywa, owoce, warzywa obierane, zioła i bakalie dla sklepów, restauracji, cateringu i firm. Dostawa w całej Polsce. Legnica, ul. Bydgoska 18, tel. 782 272 727.",
     home)

# ---------------- ASORTYMENT ----------------
asort = page_head("Co u nas znajdziesz", "Asortyment",
                  "Klasyka z polskich pól i trochę egzotyki. Asortyment zmienia się z porami roku – jeśli czegoś szukasz, po prostu zapytaj.",
                  img="stock-owoce.webp") + f'''

  <section class="section">
    <div class="wrap">
      {cards(CARDS)}
    </div>
  </section>
{PEELED}

  <section class="section section-tint" id="produkty">
    <div class="wrap">
      <div class="section-head">
        <p class="hand">Lista produktów</p>
        <h2>Co możesz u nas zamówić</h2>
        <p>Najczęściej zamawiane produkty. Ceny ustalamy indywidualnie dla każdej firmy – zadzwoń po swój cennik.</p>
      </div>{product_list()}
    </div>
  </section>
{SEASON}

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <p class="hand">Prosto z naszej hurtowni</p>
        <h2>Tak to u nas wygląda</h2>
        <p>Bez sesji zdjęciowej i stylizacji – zdjęcia robione na miejscu, w Legnicy.</p>
      </div>
      <div class="gallery">
        <figure class="g-tall"><img src="img/rozmaryn.webp" alt="Rozmaryn w doniczce" loading="lazy"></figure>
        <figure><img src="img/tymianek.webp" alt="Świeży tymianek" loading="lazy"></figure>
        <figure><img src="img/bazylia-mix.webp" alt="Bazylia zielona i fioletowa" loading="lazy"></figure>
        <figure class="g-wide"><img src="img/mieta-doniczka.webp" alt="Mięta w doniczce" loading="lazy"></figure>
      </div>
    </div>
  </section>

  <section class="section section-tint">
    <div class="wrap ask">
      <h2>Szukasz czegoś konkretnego?</h2>
      <p class="muted">Zadzwoń – powiemy, co mamy dziś na stanie, i zarezerwujemy towar dla Twojej firmy.</p>
      <div class="contact-cta center"><a href="tel:+48782272727" class="btn btn-red">{PHONE_SVG} 782 272 727</a>
      <a href="{WA_URL}" class="btn btn-wa" target="_blank" rel="noopener">{WA_SVG} WhatsApp</a></div>
    </div>
  </section>'''
page("asortyment.html", "Asortyment",
     "Warzywa, owoce, warzywa obierane, świeże zioła, sałaty, bakalie i rośliny w doniczkach – asortyment hurtowni Sylwia w Legnicy.",
     asort)

# ---------------- DOSTAWA ----------------
steps = [
    ("1", "Zadzwoń", "Powiedz, czego potrzebujesz. Doradzimy, co jest teraz najlepsze w sezonie."),
    ("2", "Kompletujemy", "Osobiście wybieramy i pakujemy towar do skrzynek."),
    ("3", "Dowozimy", "Przywozimy zamówienie własnym samochodem – pod same drzwi."),
]
dostawa = page_head("Dowozimy własnymi samochodami", "Dostawa w całej Polsce",
                    "Nie musisz przyjeżdżać do hurtowni – przywieziemy świeży towar pod drzwi Twojego sklepu, restauracji czy firmy.",
                    img="stock-warzywa.webp") + f'''

  <section class="section">
    <div class="wrap split">
      <div>
        <p class="hand">Gdzie dostarczamy?</p>
        <h2>Cała Polska</h2>
        <p class="muted">Dostawy realizujemy na terenie całej Polski. Codzienne trasy obejmują m.in.:</p>
        <ul class="cities cities-lg">
{cities_list()}
        </ul>
        <p class="muted">Jesteś z innej części Polski? Zadzwoń – ustalimy trasę i dni dostaw.</p>
      </div>
      <div class="split-photo">
        <img src="img/flota.webp" alt="Dwa samochody dostawcze Hurtowni Sylwia z grafiką owoców i warzyw" loading="lazy" width="960" height="720">
      </div>
    </div>
  </section>

  <section class="section section-tint">
    <div class="wrap">
      <div class="section-head">
        <p class="hand">Proste jak 1, 2, 3</p>
        <h2>Jak zamówić dostawę</h2>
      </div>
      <ol class="steps">''' + "".join(f'''
        <li><span class="step-n">{n}</span><h3>{t}</h3><p>{p}</p></li>''' for n, t, p in steps) + f'''
      </ol>
      <p class="center-cta"><a href="tel:+48782272727" class="btn btn-red">{PHONE_SVG} Zamów: 782 272 727</a></p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <p class="hand">Nie tylko okolice Legnicy</p>
        <h2>Dostawy w całej Polsce</h2>
        <p>Regularnie dowozimy towar do firm w całej Polsce. Zadzwoń – ustalimy trasę, dni dostaw i warunki.</p>
        <!-- TODO: opis województw (do uzupełnienia przez właściciela) -->
      </div>
    </div>
  </section>
{b2b_band()}'''
page("dostawa.html", "Dostawa",
     "Dostawy warzyw i owoców w całej Polsce. Codzienne trasy: Legnica, Lubin, Głogów, Polkowice, Jawor, Złotoryja, Prochowice, Chojnów, Bolesławiec, Jelenia Góra.",
     dostawa, og_image="img/flota.webp")

# ---------------- DLA FIRM ----------------
who = [
    (CHEF_SVG, "Restauracje i bary", "Stałe dostawy warzyw, owoców, warzyw obieranych i świeżych ziół – w ilościach, jakich potrzebuje Twoja kuchnia."),
    (STORE_SVG, "Sklepy spożywcze", "Towar gotowy na półkę, w hurtowych cenach. Pomożemy dobrać asortyment pod Twoich klientów."),
    (BOX_SVG, "Catering i stołówki", "Duże zamówienia skompletowane na konkretny dzień – bez szukania towaru po kilku hurtowniach."),
    (CAL_SVG, "Firmy i instytucje", "Owoce do biura, paczki świąteczne i mikołajkowe dla pracowników, dzieci i klientów."),
]
firmy = page_head("Dla sklepów i gastronomii", "Prowadzisz restaurację?<br><span>Współpracuj z nami!</span>",
                  "Zaopatrujemy restauracje, sklepy, kawiarnie i catering w całej Polsce. Świeży towar, warzywa obierane, certyfikaty ISO 22000 i HACCP, uczciwe ceny.",
                  img="warzywa-stragan.webp") + certs("Dla restauracji, sklepów, stołówek i dużych placówek to podstawa współpracy. Nasze certyfikaty potwierdzają, że towar jest przechowywany, przygotowywany i dowożony zgodnie z normami bezpieczeństwa żywności.") + '''

  <section class="section section-tint">
    <div class="wrap">
      <div class="section-head">
        <p class="hand">Z kim współpracujemy</p>
        <h2>Zaopatrzymy Twój biznes</h2>
      </div>
      <div class="who-grid">''' + "".join(f'''
        <div class="who">
          <div class="feature-icon">{i}</div>
          <h3>{t}</h3>
          <p>{p}</p>
        </div>''' for i, t, p in who) + f'''
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap about">
      <div class="about-photo">
        <img src="img/stock-catering.webp" alt="Przygotowanie stołu cateringowego z wędlinami, serami i dodatkami" loading="lazy" width="963" height="294" style="aspect-ratio: 4/3">
      </div>
      <div class="about-text">
        <p class="hand">Dlaczego my</p>
        <h2>Partner, a nie tylko dostawca</h2>
        <ul class="ticks">
          <li>Certyfikaty ISO 22000 i HACCP</li>
          <li>Dostawy w całej Polsce</li>
          <li>Warzywa obierane – gotowe do użycia w kuchni</li>
          <li>Stałe zamówienia i stałe pozycje – bez dzwonienia za każdym razem</li>
          <li>Osobiście wybierany, świeży towar</li>
          <li>Uczciwe ceny hurtowe</li>
          <li>Podpowiemy, co jest teraz najlepsze w sezonie</li>
        </ul>
      </div>
    </div>
  </section>
{b2b_band("Porozmawiajmy o współpracy", "Zadzwoń – ustalimy asortyment, dni dostaw i warunki dopasowane do Twojego lokalu.", link=False)}'''
page("dla-firm.html", "Oferta dla firm",
     "Hurtowe dostawy warzyw i owoców, także obieranych, dla restauracji, sklepów, cateringu i firm w całej Polsce. ISO 22000 i HACCP.",
     firmy, og_image="img/warzywa-stragan.webp")

# ---------------- O NAS ----------------
onas = page_head("O nas", "Rodzinna hurtownia,<br><span>duże serce do warzyw</span>",
                 "Rodzinna firma z Legnicy, która od 33 lat dowozi świeże warzywa i owoce do sklepów, restauracji i firm w całej Polsce.",
                 img="stock-mix.webp") + f'''

  <section class="section">
    <div class="wrap about">
      <div class="about-photo">
        <img src="img/mieta.webp" alt="Świeża mięta trzymana w dłoni" loading="lazy" width="803" height="802">
      </div>
      <div class="about-text">
        <p class="hand">Kim jesteśmy</p>
        <h2>Rodzinnie, po sąsiedzku</h2>
        <p>Hurtownia Sylwia to rodzinna firma z Legnicy, działająca od 33 lat. Nie jesteśmy anonimową siecią – każdą skrzynkę oglądamy osobiście, a z klientami rozmawiamy jak z sąsiadami.</p>
        <p>Zaopatrujemy zarówno małe lokale, jak i duże placówki: sklepy, restauracje, stołówki, catering i firmy – w ilościach hurtowych i w hurtowych cenach.</p>
        <!-- TODO: historia firmy (do uzupełnienia przez właściciela) -->
        <ul class="ticks">
          <li>33 lata doświadczenia</li>
          <li>Certyfikaty ISO 22000 i HACCP</li>
          <li>Osobiście wybierany towar</li>
          <li>Uczciwe ceny hurtowe</li>
          <li>Doradzimy, co jest teraz najlepsze w sezonie</li>
        </ul>
      </div>
    </div>
  </section>
{certs()}

  <section class="section section-tint">
    <div class="wrap split">
      <div>
        <p class="hand">Nasza flota</p>
        <h2>Rozpoznasz nas na drodze</h2>
        <p class="muted">Nasze samochody w kolorowych barwach owoców i warzyw codziennie rozwożą towar po Legnicy i okolicy – do Lubina, Głogowa, Polkowic, Jawora, Złotoryi, Prochowic, Chojnowa, Bolesławca i Jeleniej Góry – a także dalej, w całej Polsce.</p>
        <a href="dostawa.html" class="btn btn-red">Dostawa</a>
      </div>
      <div class="split-photo">
        <img src="img/flota.webp" alt="Dwa samochody dostawcze Hurtowni Sylwia z grafiką owoców i warzyw" loading="lazy" width="960" height="720">
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <p class="hand">Prosto z naszej hurtowni</p>
        <h2>Tak to u nas wygląda</h2>
      </div>
      <div class="gallery">
        <figure class="g-tall"><img src="img/rozmaryn.webp" alt="Rozmaryn w doniczce" loading="lazy"></figure>
        <figure><img src="img/tymianek.webp" alt="Świeży tymianek" loading="lazy"></figure>
        <figure><img src="img/bazylia-mix.webp" alt="Bazylia zielona i fioletowa" loading="lazy"></figure>
        <figure class="g-wide"><img src="img/mieta-doniczka.webp" alt="Mięta w doniczce" loading="lazy"></figure>
      </div>
      <div class="follow">
        <p>Więcej zdjęć i aktualności znajdziesz na naszym profilu:</p>
        {social()}
      </div>
    </div>
  </section>'''
page("o-nas.html", "O nas",
     "Hurtownia Sylwia – rodzinna hurtownia warzyw i owoców z Legnicy, od 33 lat. Certyfikaty ISO 22000 i HACCP.",
     onas, og_image="img/flota.webp")

# ---------------- KONTAKT ----------------
kontakt = page_head("Zapraszamy", "Kontakt",
                    "Zadzwoń, napisz na WhatsApp lub Facebooku albo odbierz zamówienie w hurtowni.") + f'''

  <section class="section">
    <div class="wrap contact">
      <div class="contact-info">
        <ul class="contact-list">
          <li>
            <span class="ci-icon">{PIN_SVG}</span>
            <div><strong>Adres</strong>ul. Bydgoska 18<br>Legnica</div>
          </li>
          <li>
            <span class="ci-icon">{PHONE_SVG}</span>
            <div><strong>Telefon</strong><a href="tel:+48782272727">+48 782 272 727</a></div>
          </li>
          <li>
            <span class="ci-icon ci-wa">{WA_SVG}</span>
            <div><strong>WhatsApp</strong><a href="{WA_URL}" target="_blank" rel="noopener">Napisz do nas</a></div>
          </li>
          <li>
            <span class="ci-icon">{FB_SVG}</span>
            <div><strong>Facebook</strong><a href="{FB_URL}" target="_blank" rel="noopener">Sylwia – Hurtownia warzyw i owoców</a></div>
          </li>
          <li>
            <span class="ci-icon">{TRUCK_SVG}</span>
            <div><strong>Dostawa w całej Polsce</strong>Codzienne trasy: {", ".join(CITIES)}</div>
          </li>
        </ul>
        <div class="contact-cta">
          <a href="tel:+48782272727" class="btn btn-red">Zadzwoń</a>
          <a href="{WA_URL}" class="btn btn-wa" target="_blank" rel="noopener">{WA_SVG} WhatsApp</a>
          <a href="https://www.google.com/maps/dir/?api=1&amp;destination=Bydgoska+18,+Legnica" class="btn btn-ghost" target="_blank" rel="noopener">Wyznacz trasę</a>
        </div>
        <div class="follow follow-left">
          <p>Obserwuj nas:</p>
          {social()}
        </div>
      </div>
      <div class="map">
        <iframe title="Mapa – Hurtownia Sylwia, Legnica, ul. Bydgoska 18" src="https://www.google.com/maps?q=Bydgoska+18,+Legnica&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>
    </div>
  </section>'''
page("kontakt.html", "Kontakt",
     "Hurtownia Sylwia, Legnica, ul. Bydgoska 18, tel. +48 782 272 727. Dostawy w całej Polsce.",
     kontakt)

# ---------- Polityka prywatności ----------
# TODO: uzupełnij pełną nazwę firmy (z CEIDG/KRS), NIP i e-mail administratora.
ADMIN_NAME = "Hurtownia Sylwia"
ADMIN_ADDR = "ul. Bydgoska 18, Legnica"
POLICY_DATE = "24 listopada 2026"

polityka = page_head("Twoje dane są u nas bezpieczne", "Polityka prywatności",
    "Krótko i konkretnie: jakie dane przetwarzamy, po co i jakie masz prawa.") + f'''
  <section class="section">
    <div class="wrap legal">
      <p class="muted">Obowiązuje od {POLICY_DATE}.</p>

      <h2>1. Administrator danych</h2>
      <p>Administratorem Twoich danych osobowych jest {ADMIN_NAME}, {ADMIN_ADDR}.
      W sprawach danych osobowych skontaktuj się z nami telefonicznie: <a href="tel:+48782272727">+48 782 272 727</a> lub osobiście w hurtowni.</p>

      <h2>2. Jakie dane przetwarzamy</h2>
      <p>Strona nie zawiera formularzy i nie zbiera danych automatycznie w celach marketingowych. Przetwarzamy tylko dane, które sam nam przekażesz, kontaktując się z nami (telefon, WhatsApp, Facebook) lub składając zamówienie:</p>
      <ul>
        <li>imię i nazwisko, nazwa firmy, NIP,</li>
        <li>numer telefonu, adres dostawy,</li>
        <li>treść zamówienia i korespondencji.</li>
      </ul>

      <h2>3. Cele i podstawy prawne</h2>
      <ul>
        <li>realizacja zamówień, dostaw i umów – art. 6 ust. 1 lit. b RODO,</li>
        <li>wystawianie faktur i prowadzenie księgowości – art. 6 ust. 1 lit. c RODO,</li>
        <li>odpowiedź na pytania oraz ewentualne dochodzenie roszczeń – nasz prawnie uzasadniony interes, art. 6 ust. 1 lit. f RODO.</li>
      </ul>

      <h2>4. Komu przekazujemy dane</h2>
      <p>Tylko podmiotom, które pomagają nam prowadzić działalność: biuro rachunkowe, firma hostingowa strony, dostawcy usług IT. Dane mogą też trafić do organów państwowych, jeśli wymaga tego prawo. Nie sprzedajemy danych.</p>
      <p>Jeśli piszesz do nas przez WhatsApp lub Facebook, dane przetwarza także Meta Platforms Ireland Ltd. na zasadach opisanych w jej polityce prywatności.</p>

      <h2>5. Jak długo przechowujemy dane</h2>
      <ul>
        <li>dane z zamówień i faktur – przez okres wymagany przepisami podatkowymi (zwykle 5 lat od końca roku),</li>
        <li>korespondencję – do czasu załatwienia sprawy, a potem przez okres przedawnienia roszczeń.</li>
      </ul>

      <h2>6. Twoje prawa</h2>
      <p>Masz prawo do dostępu do swoich danych, ich sprostowania, usunięcia, ograniczenia przetwarzania, przeniesienia oraz wniesienia sprzeciwu. Możesz też złożyć skargę do Prezesa Urzędu Ochrony Danych Osobowych (ul. Stawki 2, 00-193 Warszawa).</p>
      <p>Podanie danych jest dobrowolne, ale bez nich nie zrealizujemy zamówienia.</p>

      <h2 id="cookies">7. Pliki cookie i pamięć przeglądarki</h2>
      <p>Strona nie używa narzędzi analitycznych ani reklamowych. Zapisujemy w Twojej przeglądarce tylko to, co niezbędne:</p>
      <ul>
        <li>Twój wybór w komunikacie o cookies,</li>
        <li>w <a href="zamow/">aplikacji do zamówień</a> – koszyk, ulubione produkty i historię zamówień. Te dane zostają na Twoim urządzeniu i nie są wysyłane na nasz serwer.</li>
      </ul>
      <p>Możesz je w każdej chwili usunąć w ustawieniach przeglądarki. Swój wybór możesz zmienić tutaj: <a href="#" data-cookie-settings>ustawienia cookies</a>.</p>

      <h2>8. Usługi zewnętrzne</h2>
      <ul>
        <li><strong>Mapy Google</strong> – na stronie <a href="kontakt.html">Kontakt</a> osadzamy mapę Google (Google Ireland Ltd.). Po jej wyświetleniu Google może zapisać własne pliki cookie i otrzymać Twój adres IP.</li>
        <li><strong>Facebook i WhatsApp</strong> – na stronie są tylko zwykłe linki. Meta otrzymuje dane dopiero, gdy w nie klikniesz.</li>
        <li><strong>Czcionki</strong> – są przechowywane na naszym serwerze, nie pobieramy ich od Google.</li>
      </ul>

      <h2>9. Zmiany polityki</h2>
      <p>Jeśli zmienimy sposób przetwarzania danych, zaktualizujemy tę stronę i datę na górze.</p>
    </div>
  </section>'''
page("polityka-prywatnosci.html", "Polityka prywatności",
     "Polityka prywatności i informacja o plikach cookie Hurtowni Sylwia z Legnicy.",
     polityka)

print("ok")
