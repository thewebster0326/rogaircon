"""Build the Rog Air-Conditioning & Refrigeration static site.

Run:  python build.py
Writes the .html pages, sitemap.xml and robots.txt into this folder.
All business details live in CONFIG: change them there, rebuild, redeploy.
"""
import json
from datetime import date
from html import escape
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).parent

CONFIG = {
    "name": "Rog",
    "legal_name": "Rog Air-Conditioning & Refrigeration",
    "tagline": "Cool comfort. Fresh solutions.",
    "domain": "https://rogaircon.co.za",
    # --- Contact details ------------------------------------------------
    "phone_display": "073 578 2677",
    "phone_intl": "27735782677",       # no +, no spaces
    "whatsapp_intl": "27735782677",
    "email": "",                        # optional - hidden when empty
    "street": "84 Erica Avenue",
    "suburb": "Kharwastan",
    "city": "Chatsworth, Durban",
    "locality": "Chatsworth",
    "region": "KwaZulu-Natal",
    "area": "Durban & surrounds",
    "asset_version": "1",
}

C = CONFIG
ADDRESS_ONE_LINE = f"{C['street']}, {C['suburb']}, {C['city']}"

# Equipment the client lists on the flyer under "We work on".
EQUIPMENT = [
    ("coldroom", "Cold rooms & freezer rooms",
     "Walk-in cold rooms and freezer rooms for butcheries, restaurants, supermarkets and warehouses."),
    ("counter", "Underbar counter fridges",
     "Back-bar and under-counter fridges in bars, pubs and restaurants."),
    ("bottle", "Bottle coolers",
     "Single- and double-door glass coolers in shops, spaza shops and garage forecourts."),
    ("unit", "Refrigeration units",
     "Condensing units, compressors, evaporators, fans and controllers."),
    ("display", "Display fridges",
     "Deli counters, meat displays and open-front multideck fridges."),
    ("ac", "Air-conditioning split units",
     "Wall-mounted split units and larger commercial outdoor units."),
]

SECTORS = ["Homes", "Offices", "Shops & retail outlets", "Restaurants & bars",
           "Supermarkets", "Butcheries & delis", "Pharmacies", "Industrial & commercial facilities"]

WHY = [
    ("tech", "Experienced technicians", "Refrigeration and aircon work is all we do."),
    ("clock", "Fast response, on time", "When a cooler fails your stock is at risk, so we move quickly."),
    ("badge", "Quality workmanship", "Neat installs, tested properly before we leave."),
    ("wallet", "Affordable prices", "Clear quotes before any work starts."),
    ("leaf", "Energy-efficient solutions", "Well-serviced equipment uses less power."),
]

C = CONFIG

# ---------------------------------------------------------------- icons
_S = 'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'
ICON = {
    "phone": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1l-2.3 2.2z"/></svg>',
    "wa": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.7-.8-2-.9-.3-.1-.5-.1-.7.1l-.9 1.2c-.2.2-.3.2-.6.1a8 8 0 0 1-2.4-1.5 9 9 0 0 1-1.6-2.1c-.2-.3 0-.4.1-.6l.4-.5.3-.5v-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5 2.5 1 3 .8 3.6.7.6-.1 1.7-.7 2-1.4.2-.7.2-1.2.2-1.4-.1-.1-.3-.2-.6-.3zM12 21.8a9.8 9.8 0 0 1-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 1 1 12 21.8zM12 0a12 12 0 0 0-10.3 18L0 24l6.2-1.6A12 12 0 1 0 12 0z"/></svg>',
    "mail": f'<svg viewBox="0 0 24 24" {_S} aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
    "pin": f'<svg viewBox="0 0 24 24" {_S} aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>',
    "map": f'<svg viewBox="0 0 24 24" {_S} aria-hidden="true"><path d="M9 4 3 6v14l6-2 6 2 6-2V4l-6 2-6-2zM9 4v14M15 6v14"/></svg>',
    "menu": f'<svg viewBox="0 0 24 24" {_S} aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
    "snow": f'<svg viewBox="0 0 24 24" {_S} aria-hidden="true"><path d="M12 2v20M3.3 7l17.4 10M3.3 17 20.7 7"/><path d="m9 4 3 2.5L15 4M9 20l3-2.5 3 2.5"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>',
    "arrow": f'<svg viewBox="0 0 24 24" {_S} aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    # service icons (from the flyer: installation, repairs, servicing)
    "install": f'<svg class="ico" viewBox="0 0 40 40" {_S}><path d="M26 6a7 7 0 0 0-6.6 9.3L7 27.7a3 3 0 0 0 4.3 4.3l12.4-12.4A7 7 0 0 0 33 13l-4.5 2.6-4-4L27 7z"/><path d="m8 8 9 9M6 10l4-4"/></svg>',
    "repair": f'<svg class="ico" viewBox="0 0 40 40" {_S}><circle cx="15" cy="17" r="4"/><path d="M15 7v3M15 24v3M5 17h3M22 17h3M8 10l2 2M20 22l2 2M8 24l2-2M20 12l2-2"/><circle cx="28" cy="29" r="3"/><path d="M28 22v2M28 34v2M21 29h2M33 29h2"/></svg>',
    "service": f'<svg class="ico" viewBox="0 0 40 40" {_S}><path d="M20 4 7 9v10c0 8 5.6 14.4 13 17 7.4-2.6 13-9 13-17V9z"/><path d="m14 20 4.5 4.5L27 16"/></svg>',
    # equipment icons
    "coldroom": f'<svg class="ico" viewBox="0 0 40 40" {_S}><path d="M5 35V13l15-8 15 8v22z"/><path d="M13 35V20h14v15M20 23v9M16.5 25l7 5M23.5 25l-7 5"/></svg>',
    "counter": f'<svg class="ico" viewBox="0 0 40 40" {_S}><rect x="3" y="12" width="34" height="20" rx="2"/><path d="M3 17h34M14.3 17v15M25.6 17v15M8 32v3M32 32v3"/></svg>',
    "bottle": f'<svg class="ico" viewBox="0 0 40 40" {_S}><rect x="9" y="3" width="22" height="34" rx="2"/><path d="M9 9h22M14 15v4M14 24v4M20 15v4M20 24v4M26 15v4M26 24v4"/></svg>',
    "unit": f'<svg class="ico" viewBox="0 0 40 40" {_S}><rect x="3" y="8" width="34" height="24" rx="2"/><circle cx="14" cy="20" r="7"/><path d="M14 13v14M7 20h14"/><path d="M27 14h6M27 19h6M27 24h6"/></svg>',
    "display": f'<svg class="ico" viewBox="0 0 40 40" {_S}><path d="M4 22h32v11H4zM6 22c0-8 4-12 14-12s14 4 14 12"/><path d="M9 27h22"/></svg>',
    "ac": f'<svg class="ico" viewBox="0 0 40 40" {_S}><rect x="4" y="8" width="32" height="13" rx="3"/><path d="M9 17h22M12 26c0 3-2 3-2 6M20 26c0 3-2 3-2 6M28 26c0 3-2 3-2 6"/></svg>',
    # why-choose icons
    "tech": f'<svg class="ico" viewBox="0 0 40 40" {_S}><circle cx="20" cy="14" r="6"/><path d="M12 11c0-5 3.5-7 8-7s8 2 8 7zM8 36c0-7 5-11 12-11s12 4 12 11"/></svg>',
    "clock": f'<svg class="ico" viewBox="0 0 40 40" {_S}><circle cx="20" cy="20" r="15"/><path d="M20 11v9l6 4"/></svg>',
    "badge": f'<svg class="ico" viewBox="0 0 40 40" {_S}><circle cx="20" cy="16" r="10"/><path d="m15.5 16 3 3 6-6M13 24l-3 12 10-5 10 5-3-12"/></svg>',
    "wallet": f'<svg class="ico" viewBox="0 0 40 40" {_S}><path d="M6 12h26a3 3 0 0 1 3 3v16a3 3 0 0 1-3 3H6z"/><path d="M6 12V9a3 3 0 0 1 3-3h19v6M26 20h9v6h-9a3 3 0 0 1 0-6z"/></svg>',
    "leaf": f'<svg class="ico" viewBox="0 0 40 40" {_S}><path d="M8 32C8 16 18 7 34 6c0 17-9 26-24 26z"/><path d="M8 32 22 18"/></svg>',
}

# ---------------------------------------------------------------- links

def tel():
    return f"tel:+{C['phone_intl']}"


def wa(msg="Hi Rog, I'd like a quote."):
    return f"https://wa.me/{C['whatsapp_intl']}?text={quote(msg)}"


def call_btns(extra_cls=""):
    return f"""<div class="btns {extra_cls}">
      <a class="btn btn-primary" href="{tel()}">{ICON['phone']}Call {escape(C['phone_display'])}</a>
      <a class="btn btn-wa" href="{wa()}" target="_blank" rel="noopener">{ICON['wa']}WhatsApp us</a>
    </div>"""


def head(label, title, text=""):
    return f"""<div class="section-head reveal">
      <p class="label">{ICON['snow']}{label}</p>
      <h2>{title}</h2>
      {f'<p>{text}</p>' if text else ''}
    </div>"""


def checks(items):
    return '<ul class="checks">' + "".join(f"<li>{ICON['check']}<span>{i}</span></li>" for i in items) + "</ul>"


# ---------------------------------------------------------------- layout
NAV = [("index.html", "Home"), ("commercial-refrigeration.html", "Refrigeration"),
       ("air-conditioning.html", "Air-conditioning"), ("contact.html", "Contact")]


def schema():
    data = {
        "@context": "https://schema.org",
        "@type": "HVACBusiness",
        "name": C["legal_name"],
        "alternateName": "Rog Aircon",
        "slogan": C["tagline"],
        "description": "Commercial air-conditioning and refrigeration in Durban: installation, repairs and servicing of cold rooms, bottle coolers, display fridges, underbar fridges, refrigeration units and split units.",
        "url": C["domain"] + "/",
        "logo": C["domain"] + "/assets/img/rog-logo.png",
        "image": C["domain"] + "/assets/img/samsung-condensers-on-stands.webp",
        "telephone": "+" + C["phone_intl"],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": f"{C['street']}, {C['suburb']}",
            "addressLocality": C["locality"],
            "addressRegion": C["region"],
            "addressCountry": "ZA",
        },
        "areaServed": [{"@type": "City", "name": "Durban"}, {"@type": "Place", "name": "Chatsworth"}],
        "knowsAbout": ["Commercial refrigeration", "Cold rooms", "Bottle coolers", "Display fridges",
                       "Underbar counter fridges", "Air-conditioning installation", "Air-conditioning repairs"],
    }
    if C["email"]:
        data["email"] = C["email"]
    return json.dumps(data, ensure_ascii=False)


def page(slug, title, description, body, home=False):
    v = C["asset_version"]
    current = ' aria-current="page"'
    nav = "".join(
        f'<a href="{href}"{current if href == slug else ""}>{label}</a>'
        for href, label in NAV)
    canonical = C["domain"] + "/" + ("" if slug == "index.html" else slug)
    email_li = f'<li><a href="mailto:{C["email"]}">{C["email"]}</a></li>' if C["email"] else ""
    return f"""<!doctype html>
<html lang="en-ZA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{'<base href="/">' if slug == "404.html" else ""}
<title>{escape(title)}</title>
<meta name="description" content="{escape(description)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{C['domain']}/assets/img/og-image.jpg">
<meta name="theme-color" content="#0A1F4E">
<link rel="icon" href="assets/img/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Barlow:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/styles.css?v={v}">
<script>document.documentElement.classList.add('js')</script>
{'<script type="application/ld+json">' + schema() + '</script>' if home else ''}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar">
  <div class="wrap">
    <span>{ICON['pin']}Based in Chatsworth &middot; working across {escape(C['area'])}</span>
    <a href="{tel()}">{ICON['phone']}{escape(C['phone_display'])}</a>
  </div>
</div>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="{C['legal_name']}, home">
      <img src="assets/img/rog-logo.webp" alt="" width="1525" height="489">
      <span>Air-Conditioning<br>&amp; Refrigeration</span>
    </a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="nav" aria-label="Menu">{ICON['menu']}</button>
    <nav class="nav" id="nav" aria-label="Main">{nav}</nav>
    <a class="btn btn-primary header-call" href="{tel()}">{ICON['phone']}Call now</a>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="cols">
      <div>
        <a class="footer-logo" href="index.html"><img src="assets/img/rog-logo-white.webp" alt="{C['legal_name']}" width="1525" height="489" loading="lazy"></a>
        <p class="footer-tag">{escape(C['tagline'])}</p>
        <p>Installation, repairs and servicing of commercial refrigeration and air-conditioning across Durban.</p>
      </div>
      <div>
        <h3>Services</h3>
        <ul>
          <li><a href="commercial-refrigeration.html#cold-rooms">Cold rooms &amp; freezer rooms</a></li>
          <li><a href="commercial-refrigeration.html#coolers">Bottle coolers &amp; display fridges</a></li>
          <li><a href="commercial-refrigeration.html#units">Refrigeration units</a></li>
          <li><a href="air-conditioning.html#install">Aircon installation</a></li>
          <li><a href="air-conditioning.html#repairs">Aircon repairs &amp; servicing</a></li>
        </ul>
      </div>
      <div>
        <h3>Contact</h3>
        <ul>
          <li><a href="{tel()}">{escape(C['phone_display'])}</a></li>
          <li><a href="{wa()}" target="_blank" rel="noopener">WhatsApp</a></li>
          {email_li}
          <li>{escape(C['street'])}, {escape(C['suburb'])}<br>{escape(C['city'])}</li>
        </ul>
      </div>
    </div>
    <div class="legal">
      <span>&copy; {date.today().year} {C['legal_name']}. All rights reserved.</span>
      <span>Website by <a href="https://thewebster.co.za" rel="noopener">The Webster</a></span>
    </div>
  </div>
</footer>
<div class="float">
  <a class="f-wa" href="{wa()}" target="_blank" rel="noopener" aria-label="WhatsApp Rog">{ICON['wa']}</a>
  <a class="f-call" href="{tel()}" aria-label="Call Rog">{ICON['phone']}</a>
</div>
<script src="assets/js/main.js?v={v}" defer></script>
</body>
</html>
"""


def cta_band(heading="One call. Total comfort.",
             text="Send us a photo of the unit or the fault on WhatsApp, and we'll come back to you with a quote."):
    return f"""<section class="cta-band">
  <div class="wrap">
    <div><h2>{heading}</h2><p>{text}</p></div>
    <div class="btns">
      <a class="btn btn-light" href="{tel()}">{ICON['phone']}{escape(C['phone_display'])}</a>
      <a class="btn btn-wa" href="{wa()}" target="_blank" rel="noopener">{ICON['wa']}WhatsApp a photo</a>
    </div>
  </div>
</section>"""


def equipment_section(alt=True):
    tiles = "".join(
        f'<div class="equip reveal">{ICON[ico]}<h3>{name}</h3><p>{text}</p></div>'
        for ico, name, text in EQUIPMENT)
    return f"""<section class="section {'section-alt' if alt else ''}" id="equipment">
  <div class="wrap">
    {head("We work on", "Commercial cooling equipment, installed and kept running")}
    <div class="equip-grid">{tiles}</div>
  </div>
</section>"""


def sectors_section():
    lis = "".join(f"<li>{ICON['check']}{s}</li>" for s in SECTORS)
    why = "".join(f'<li class="reveal">{ICON[i]}<div><h3>{t}</h3><p>{p}</p></div></li>' for i, t, p in WHY)
    return f"""<section class="section section-dark" id="why">
  <div class="wrap why-grid">
    <div>
      {head("Why choose Rog?", "Quality service you can trust")}
      <ul class="why">{why}</ul>
    </div>
    <div class="sectors reveal">
      <h3>We service</h3>
      <ul>{lis}</ul>
    </div>
  </div>
</section>"""


def gallery(items):
    figs = "".join(
        f'<figure class="{cls} reveal"><img src="assets/img/{f}.webp" alt="{alt}" loading="lazy"><figcaption>{cap}</figcaption></figure>'
        for f, alt, cap, cls in items)
    return f'<div class="gallery">{figs}</div>'


# ---------------------------------------------------------------- pages

def home():
    body = f"""
<section class="hero">
  <div class="hero-flakes" aria-hidden="true">{ICON['snow'] * 3}</div>
  <div class="wrap">
    <div class="hero-copy">
      <p class="label">{ICON['snow']}Commercial air-conditioning &amp; refrigeration &middot; Durban</p>
      <h1>Keeping Durban&rsquo;s businesses <span>cool.</span></h1>
      <p class="lede">Installation, repairs and servicing of cold rooms, bottle coolers, display fridges, refrigeration units and air-conditioners, for shops, restaurants, supermarkets and businesses across Durban.</p>
      {call_btns()}
      <ul class="hero-facts">
        <li>{ICON['check']}Based in Chatsworth</li>
        <li>{ICON['check']}Commercial specialists</li>
        <li>{ICON['check']}All makes &amp; models</li>
      </ul>
    </div>
    <div class="hero-photos">
      <img class="hp-main" src="assets/img/samsung-condensers-on-stands.webp" alt="Two commercial Samsung outdoor air-conditioning units installed on steel stands" width="900" height="1200" fetchpriority="high">
      <img class="hp-side" src="assets/img/bottle-coolers-convenience-store.webp" alt="Glass-door bottle coolers fully stocked with drinks in a convenience store" width="900" height="1200">
      <div class="hp-badge"><strong>Quality service</strong><span>you can trust</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    {head("Our services", "Install. Repair. Service.", "Everything from a single bottle cooler to a full cold room or a building&rsquo;s air-conditioning.")}
    <div class="services">
      <div class="service reveal">{ICON['install']}<h3>Installation</h3>
        <p>Professional installation of air-conditioning and refrigeration units. Neat, safe and efficient.</p>
        <a class="more" href="air-conditioning.html#install">Installation {ICON['arrow']}</a></div>
      <div class="service reveal">{ICON['repair']}<h3>Repairs</h3>
        <p>Fast, reliable repairs for all makes and models. We find the fault and get your system working again.</p>
        <a class="more" href="commercial-refrigeration.html#repairs">Repairs {ICON['arrow']}</a></div>
      <div class="service reveal">{ICON['service']}<h3>Servicing</h3>
        <p>Regular servicing improves performance, saves energy and extends the life of your equipment.</p>
        <a class="more" href="commercial-refrigeration.html#servicing">Servicing {ICON['arrow']}</a></div>
    </div>
  </div>
</section>

{equipment_section()}

{sectors_section()}

<section class="section">
  <div class="wrap">
    {head("Recent work", "On site around Durban")}
    {gallery([
        ("outdoor-units-commercial-building", "Three outdoor air-conditioning units mounted on the brick wall of a commercial building", "Commercial outdoor units", "tall"),
        ("condenser-install-vacuum-pump", "Outdoor unit being installed, with a vacuum pump and gauges connected", "Installation in progress", "tall"),
        ("pharmacy-display-fridge", "Upright glass-door display fridge in a pharmacy", "Pharmacy display fridge", "tall"),
        ("double-door-glass-cooler", "Double-door glass-front commercial cooler", "Double-door cooler", "tall"),
        ("condenser-pcb-repair", "Outdoor unit opened up with its control board exposed during a repair", "Control board repair", "tall"),
        ("bottle-cooler-repair", "Bottle cooler with the base panel removed and tools laid out for a repair", "Bottle cooler repair", "tall"),
    ])}
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    {head("How it works", "Getting a quote is quick")}
    <ol class="steps">
      <li class="reveal"><h3>Send us the details</h3><p>Call or WhatsApp us with what the equipment is and what it&rsquo;s doing. A photo of the unit, its sticker or the controller display helps.</p></li>
      <li class="reveal"><h3>Get your quote</h3><p>We quote for the work, or come out first if the fault has to be found on site.</p></li>
      <li class="reveal"><h3>We get you running</h3><p>We do the work, then test that the equipment is holding temperature before we leave.</p></li>
    </ol>
  </div>
</section>

{cta_band()}
"""
    return page("index.html",
                f"Commercial Air-Conditioning & Refrigeration in Durban | {C['legal_name']}",
                "Commercial refrigeration and air-conditioning in Durban, based in Chatsworth. Installation, repairs and servicing of cold rooms, bottle coolers, display fridges and split units.",
                body, home=True)


def refrigeration():
    body = f"""
<section class="page-hero">
  <div class="wrap">
    <div>
      <p class="label">{ICON['snow']}Commercial refrigeration &middot; Durban</p>
      <h1>Commercial refrigeration installation, repairs &amp; servicing</h1>
      <p class="lede">Cold rooms, freezer rooms, bottle coolers, display fridges, underbar fridges and the refrigeration units that run them. When they stop cooling, your stock is at risk, so call us as soon as the temperature starts to climb.</p>
      {call_btns()}
    </div>
    <img src="assets/img/double-door-glass-cooler.webp" alt="Double-door glass-front commercial cooler" width="765" height="1020" fetchpriority="high">
  </div>
</section>

{equipment_section(alt=False)}

<section class="section section-alt" id="cold-rooms">
  <div class="wrap split">
    <div class="reveal">
      <p class="label">{ICON['snow']}Cold rooms &amp; freezer rooms</p>
      <h2>Cold rooms that hold their temperature</h2>
      <p>For butcheries, restaurants, supermarkets and warehouses, where a cold room that won&rsquo;t hold temperature quickly turns into lost stock.</p>
      {checks(["Room not reaching or holding temperature", "Evaporators icing up, or defrost problems", "Condensing unit faults and gas leaks", "Fans, controllers, door seals and heaters"])}
      <a class="btn btn-primary" href="{wa('Hi Rog, our cold room / freezer room needs attention.')}" target="_blank" rel="noopener">Report a cold room fault</a>
    </div>
    <img class="reveal" src="assets/img/samsung-condensers-on-stands.webp" alt="Commercial outdoor units installed on steel stands" loading="lazy">
  </div>
</section>

<section class="section" id="coolers">
  <div class="wrap split flip">
    <div class="reveal">
      <p class="label">{ICON['snow']}Coolers &amp; display fridges</p>
      <h2>Bottle coolers, display fridges and underbar fridges</h2>
      <p>The fridges your customers buy from. A warm cooler means lost sales, so we fix them fast.</p>
      {checks(["Single- and double-door glass bottle coolers", "Deli counters, meat displays and multidecks", "Underbar and back-bar counter fridges", "Pharmacy and medical display fridges"])}
      <a class="btn btn-primary" href="{wa('Hi Rog, my cooler / display fridge needs a repair.')}" target="_blank" rel="noopener">Report a fridge fault</a>
    </div>
    <img class="reveal" src="assets/img/deli-display-counter.webp" alt="Curved-glass deli display counter" loading="lazy">
  </div>
</section>

<section class="section section-alt" id="units">
  <div class="wrap split">
    <div class="reveal">
      <p class="label">{ICON['snow']}Refrigeration units</p>
      <h2>Compressors, condensing units and controls</h2>
      <p>The machinery behind the cold. We diagnose and repair the unit itself, not just the cabinet.</p>
      {checks(["Compressor and condensing unit faults", "Gas leaks found, repaired and regassed", "Fans, thermostats, controllers and boards", "Electrical faults and tripping"])}
    </div>
    <img class="reveal" src="assets/img/condenser-pcb-repair.webp" alt="Outdoor unit opened up for a control board repair" loading="lazy">
  </div>
</section>

<section class="section" id="repairs">
  <div class="wrap">
    {head("Repairs &amp; servicing", "Repairs when it breaks. Servicing so it doesn&rsquo;t.")}
    <div class="two-col">
      <div class="panel reveal" id="servicing">
        <h3>Servicing</h3>
        <p>Regular servicing keeps equipment cooling properly, cuts power use and extends its life.</p>
        {checks(["Condenser and evaporator coils cleaned", "Fans, drains and door seals checked", "Gas pressures and temperatures checked", "Electrical connections and controls tested"])}
      </div>
      <div class="panel reveal">
        <h3>Before we arrive</h3>
        <p>If a cold room or fridge has stopped cooling:</p>
        {checks(["Keep the door shut to hold the cold in", "Move high-value stock to another unit if you can", "Check the plug, breaker and thermostat setting", "WhatsApp us a photo of the controller and unit sticker"])}
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <div class="section-head reveal"><p class="label">{ICON['snow']}Questions</p><h2>Refrigeration questions</h2></div>
    <div class="faq">
      <details><summary>Do you repair all makes of commercial fridge?</summary><p>Yes. We repair and service all makes and models of bottle coolers, display fridges, underbar fridges, cold rooms and refrigeration units.</p></details>
      <details><summary>How often should commercial refrigeration be serviced?</summary><p>Equipment that runs around the clock, like cold rooms and bottle coolers, does best with a service every three to six months, depending on how hard it works and how dusty the area is.</p></details>
      <details><summary>Do you work outside Chatsworth?</summary><p>Yes. We&rsquo;re based in Chatsworth and work across Durban and the surrounding areas.</p></details>
      <details><summary>Can you install a new cold room or cooler?</summary><p>Yes. We install new refrigeration equipment as well as repairing and servicing existing units. Send us the details and we&rsquo;ll quote.</p></details>
    </div>
  </div>
</section>

{cta_band("Stock at risk?", "Call now for cold room, cooler and display fridge repairs across Durban.")}
"""
    return page("commercial-refrigeration.html",
                f"Commercial Refrigeration Repairs & Installation in Durban | {C['name']}",
                "Cold room, freezer room, bottle cooler, display fridge and underbar fridge installation, repairs and servicing in Durban. Based in Chatsworth.",
                body)


def aircon():
    body = f"""
<section class="page-hero">
  <div class="wrap">
    <div>
      <p class="label">{ICON['snow']}Air-conditioning &middot; Durban</p>
      <h1>Air-conditioning installation, repairs &amp; servicing</h1>
      <p class="lede">Split units and commercial outdoor units for offices, shops, restaurants and homes. Installed neatly, serviced regularly and repaired quickly when they stop cooling.</p>
      {call_btns()}
    </div>
    <img src="assets/img/outdoor-units-commercial-building.webp" alt="Outdoor air-conditioning units mounted on a commercial building" width="675" height="1200" fetchpriority="high">
  </div>
</section>

<section class="section" id="install">
  <div class="wrap split">
    <div class="reveal">
      <p class="label">{ICON['snow']}Installation</p>
      <h2>New air-conditioning, installed properly</h2>
      <p>We help you choose the right size of unit for the space, then install it neatly and safely. If you&rsquo;ve already bought a unit, we&rsquo;ll install that one.</p>
      {checks(["Help choosing the right size for the room", "Indoor and outdoor units mounted on proper brackets or stands", "Copper piping, drainage and electrical done neatly", "System vacuumed, gassed and tested before handover"])}
      <a class="btn btn-primary" href="{wa('Hi Rog, I would like a quote to install air-conditioning.')}" target="_blank" rel="noopener">Get an installation quote</a>
    </div>
    <img class="reveal" src="assets/img/condenser-install-vacuum-pump.webp" alt="Outdoor unit installation with vacuum pump connected" loading="lazy">
  </div>
</section>

<section class="section section-alt" id="repairs">
  <div class="wrap split flip">
    <div class="reveal">
      <p class="label">{ICON['snow']}Repairs</p>
      <h2>Aircon repairs for all makes and models</h2>
      <p>Tell us what the unit is doing. If it shows an error code, send us a photo of the display.</p>
      {checks(["Blowing warm air or not cooling", "Water leaking from the indoor unit", "Won&rsquo;t switch on, or trips the power", "Error codes, noisy fans and compressor faults", "Gas leaks found and repaired"])}
      <a class="btn btn-primary" href="{wa('Hi Rog, my aircon needs a repair.')}" target="_blank" rel="noopener">Report an aircon fault</a>
    </div>
    <img class="reveal" src="assets/img/condenser-pcb-repair.webp" alt="Outdoor unit opened for a repair" loading="lazy">
  </div>
</section>

<section class="section" id="servicing">
  <div class="wrap split">
    <div class="reveal">
      <p class="label">{ICON['snow']}Servicing</p>
      <h2>Servicing that keeps the cold air coming</h2>
      <p>In Durban&rsquo;s heat and humidity, a dirty aircon cools poorly and costs more to run. A service gets it back to full performance.</p>
      {checks(["Filters, indoor coil and fan cleaned", "Outdoor unit cleaned and checked", "Drain line cleared so water doesn&rsquo;t drip inside", "Gas pressure checked and topped up where needed"])}
      <a class="btn btn-primary" href="{wa('Hi Rog, I would like to book an aircon service.')}" target="_blank" rel="noopener">Book a service</a>
    </div>
    <img class="reveal" src="assets/img/split-unit-wall-bracket.webp" alt="Split unit outdoor condenser mounted on a wall bracket" loading="lazy">
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <div class="section-head reveal"><p class="label">{ICON['snow']}Questions</p><h2>Air-conditioning questions</h2></div>
    <div class="faq">
      <details><summary>How often should an aircon be serviced?</summary><p>Units that run all day in offices, shops and restaurants do best with a service every six months. A home unit is usually fine with one service a year.</p></details>
      <details><summary>Can you install a unit I bought myself?</summary><p>Yes. Tell us the make and size, and where it&rsquo;s going, and we&rsquo;ll quote for the installation.</p></details>
      <details><summary>Do you work on homes as well as businesses?</summary><p>Yes. We specialise in commercial work, but we also install, repair and service aircons in homes.</p></details>
      <details><summary>Which areas do you cover?</summary><p>We&rsquo;re based in Chatsworth and work across Durban and the surrounding areas.</p></details>
    </div>
  </div>
</section>

{cta_band("Aircon not cooling?", "WhatsApp a photo of the unit or the error code on the display, and we&rsquo;ll tell you what it needs.")}
"""
    return page("air-conditioning.html",
                f"Air-Conditioning Installation, Repairs & Servicing in Durban | {C['name']}",
                "Air-conditioning installation, repairs and servicing for offices, shops, restaurants and homes in Durban. Based in Chatsworth. All makes and models.",
                body)


def contact():
    email_card = (f'<a class="contact-card" href="mailto:{C["email"]}">{ICON["mail"]}<div><span>Email</span><strong>{C["email"]}</strong></div></a>'
                  if C["email"] else "")
    options = "".join(f"<option>{o}</option>" for o in [
        "Cold room / freezer room", "Bottle cooler", "Display fridge", "Underbar counter fridge",
        "Refrigeration unit", "Aircon installation", "Aircon repair", "Aircon service", "Something else"])
    map_q = quote(f"{C['street']}, {C['suburb']}, Chatsworth, Durban, South Africa")
    body = f"""
<section class="page-hero page-hero-plain">
  <div class="wrap">
    <div>
      <p class="label">{ICON['snow']}Contact</p>
      <h1>Call us today</h1>
      <p class="lede">WhatsApp is the quickest way to get a quote, because you can send photos of the equipment. You&rsquo;re also welcome to call.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap contact-grid">
    <div class="contact-cards">
      <a class="contact-card big" href="{tel()}">{ICON['phone']}<div><span>Call</span><strong>{escape(C['phone_display'])}</strong></div></a>
      <a class="contact-card" href="{wa()}" target="_blank" rel="noopener">{ICON['wa']}<div><span>WhatsApp</span><strong>Send a message or photo</strong></div></a>
      {email_card}
      <a class="contact-card" href="https://www.google.com/maps/search/?api=1&query={map_q}" target="_blank" rel="noopener">{ICON['pin']}<div><span>Based at</span><strong>{escape(C['street'])}, {escape(C['suburb'])}<br>{escape(C['city'])}</strong></div></a>
      <div class="contact-card">{ICON['map']}<div><span>Area of operation</span><strong>Durban &amp; surrounds</strong></div></div>
    </div>

    <form class="quote" id="quote" data-wa="{C['whatsapp_intl']}">
      <h2>Request a quote on WhatsApp</h2>
      <div class="field-row">
        <div class="field"><label for="q-name">Your name</label><input id="q-name" name="name" autocomplete="name" required></div>
        <div class="field"><label for="q-business">Business (optional)</label><input id="q-business" name="business" autocomplete="organization"></div>
      </div>
      <div class="field-row">
        <div class="field"><label for="q-area">Suburb / area</label><input id="q-area" name="area" autocomplete="address-level2" required></div>
        <div class="field"><label for="q-service">What do you need?</label><select id="q-service" name="service">{options}</select></div>
      </div>
      <div class="field"><label for="q-msg">Details</label><textarea id="q-msg" name="msg" placeholder="Make and model if you know it, and what the equipment is doing"></textarea></div>
      <button class="btn btn-wa" type="submit">{ICON['wa']}Continue in WhatsApp</button>
      <p class="hint">This opens WhatsApp with your message filled in. Nothing is sent until you press send there.</p>
    </form>
  </div>
</section>

<section class="map-wrap">
  <iframe title="Map showing Rog in Kharwastan, Chatsworth" src="https://maps.google.com/maps?q={map_q}&z=15&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
</section>
"""
    return page("contact.html", f"Contact & Quotes | {C['legal_name']}",
                "Call or WhatsApp Rog on 073 578 2677 for commercial refrigeration and air-conditioning quotes in Durban. Based at 84 Erica Avenue, Kharwastan, Chatsworth.",
                body)


def not_found():
    body = f"""
<section class="page-hero page-hero-plain">
  <div class="wrap">
    <div>
      <p class="label">{ICON['snow']}Error 404</p>
      <h1>This page doesn&rsquo;t exist</h1>
      <p class="lede">The link may be old or mistyped. Start from the home page, or contact us directly.</p>
      <div class="btns"><a class="btn btn-primary" href="index.html">Go to the home page</a><a class="btn btn-wa" href="{wa()}" target="_blank" rel="noopener">{ICON['wa']}WhatsApp us</a></div>
    </div>
  </div>
</section>"""
    return page("404.html", f"Page not found | {C['legal_name']}", "Page not found.", body)


PAGES = {
    "index.html": home,
    "commercial-refrigeration.html": refrigeration,
    "air-conditioning.html": aircon,
    "contact.html": contact,
    "404.html": not_found,
}


def main():
    for slug, fn in PAGES.items():
        (ROOT / slug).write_text(fn(), encoding="utf-8", newline="\n")
    today = date.today().isoformat()
    urls = "".join(
        f"<url><loc>{C['domain']}/{'' if s == 'index.html' else s}</loc><lastmod>{today}</lastmod></url>"
        for s in PAGES if s != "404.html")
    (ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n',
        encoding="utf-8", newline="\n")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {C['domain']}/sitemap.xml\n",
                                     encoding="utf-8", newline="\n")
    print(f"Built {len(PAGES)} pages.")
    if not C["email"]:
        print("Note: no email set in CONFIG (hidden on the site).")


if __name__ == "__main__":
    main()
