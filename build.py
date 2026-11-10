#!/usr/bin/env python3
"""Génère le site KamiQuiz complet dans dist/.

Usage : python3 build.py [--date AAAA-MM-JJ]
  --date : ne publie que les séries et guides datés jusqu'à ce jour (par défaut : aujourd'hui).
Source des questions : data/questions.json (produit par tools/clean_data.py)
"""
import html
import json
import re
import shutil
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'content'))
import datetime  # noqa: E402
from series import SERIES as ALL_SERIES, CATEGORIES as FR_CATEGORIES, POPULAR, NEW_FALLBACK  # noqa: E402
import dle as DLE  # noqa: E402
import i18n  # noqa: E402
from i18n import T, U, loc_date  # noqa: E402
from visuals import visual_svg  # noqa: E402
from trailers import TRAILERS  # noqa: E402

DIST = ROOT / 'dist'
SITE = 'https://kamiquiz.com'
PUB = 'ca-pub-6970710961658841'
BASE_DATE = '2026-10-16'   # date de la refonte : contenu publié d'origine
TODAY = datetime.date.today().isoformat()
if '--date' in sys.argv:
    TODAY = sys.argv[sys.argv.index('--date') + 1]
datetime.date.fromisoformat(TODAY)
VERSION = TODAY.replace('-', '')


def asset_v(path):
    """Empreinte du contenu d'un fichier statique : elle change dès que le fichier change.
    Indispensable car /assets/* est servi avec un cache d'un an (voir _headers)."""
    import hashlib
    return hashlib.sha256((ROOT / 'static' / path.lstrip('/')).read_bytes()).hexdigest()[:10]


def asset(path):
    return f'{path}?v={asset_v(path)}'
for _s in ALL_SERIES:
    _s.setdefault('date', BASE_DATE)
FR_SERIES = [s for s in ALL_SERIES if s['date'] <= TODAY]

DB = json.loads((ROOT / 'data' / 'questions.json').read_text(encoding='utf-8'))
assert {s['key'] for s in FR_SERIES} <= set(DB), {s['key'] for s in FR_SERIES} - set(DB)
for s in FR_SERIES:
    s['data'] = DB[s['key']]
    s['n'] = len(DB[s['key']]['q'])
    s['color'] = DB[s['key']]['color']

FR_MODES = [
    ('libre', '🎲', 'Mode libre', "20 questions au hasard, sans chrono. Idéal pour découvrir."),
    ('chrono', '⚡', 'Contre la montre', "15 secondes par question et un multiplicateur de points pour les plus rapides."),
    ('survie', '🛡️', 'Survie', "Trois vies. Chaque erreur en coûte une. Jusqu'où tiendrez-vous ?"),
    ('maitre', '⭐', 'Ascension', "30 questions de plus en plus dures, avec bonus de série."),
    ('expert', '💀', 'Expert', "Uniquement les questions difficiles."),
    ('categorie', '📚', 'Par thème', "Choisissez les thèmes sur lesquels vous entraîner."),
]

e = html.escape
fr_num = i18n.num


# --------------------------------------------------------------------------- langues
EN_SERIES_META = __import__('en.series', fromlist=['SERIES']).SERIES


def en_questions(s):
    """Questions traduites d'une série (content/en/questions/<clé>.json), dans l'ordre de la banque française.

    Format : {"cats": {catégorie fr: catégorie en}, "ranks": [...], "q": {id: [question, [4 réponses], explication]}}
    id = i18n.qid(texte français de la question) ; les réponses suivent l'ordre de la banque française.
    Une question française modifiée change d'id : sa traduction n'est plus utilisée (voir tools/i18n_status.py)."""
    f = ROOT / 'content' / 'en' / 'questions' / f'{s["key"]}.json'
    if not f.exists():
        return None
    tr = json.loads(f.read_text(encoding='utf-8'))
    d = s['data']
    qs = []
    for q in d['q']:
        t = tr['q'].get(i18n.qid(q['q']))
        if not t:
            continue
        text, answers, fb = t
        assert len(answers) == 4 and len(set(answers)) == 4, (s['key'], text)
        qs.append({**q, 'q': text, 'a': answers, 'fb': fb, 'cat': tr['cats'][q['cat']]})
    cats = {tr['cats'][c]: v for c, v in d['cats'].items() if c in tr['cats']}
    return {'name': EN_SERIES_META[s['key']]['name'], 'color': d['color'], 'ranks': tr.get('ranks', d.get('ranks', [])),
            'sw': [], 'cats': cats, 'q': qs, 'total_fr': len(d['q'])}


def localized_series(lang):
    if lang == 'fr':
        return FR_SERIES
    out = []
    for s in FR_SERIES:
        meta = EN_SERIES_META.get(s['key'])
        data = en_questions(s) if meta else None
        if not data or not data['q']:
            continue
        out.append({**s, 'name': meta['name'], 'tag': meta['tag'], 'intro': meta['intro'], 'data': data, 'n': len(data['q'])})
        i18n.QUIZ_SLUGS['en'][s['slug']] = meta['slug']
    return out


def setup(lang):
    """Prépare toutes les données globales dans la langue demandée."""
    global SERIES, BY_KEY, TOTAL_Q, NB_SERIES, CATEGORIES, CAT_NAME, LEVELS, MODES, NAMES_JSON, GUIDES, GUIDES_BY_SERIE
    global DLE_MODES, DLE_INFO
    i18n.set_lang(lang)
    SERIES = localized_series(lang)
    BY_KEY = {s['key']: s for s in SERIES}
    TOTAL_Q = sum(s['n'] for s in SERIES)
    NB_SERIES = len(SERIES)
    CATEGORIES = [(c, T(n), T(d)) for c, n, d in FR_CATEGORIES]
    CAT_NAME = {c[0]: c[1] for c in CATEGORIES}
    LEVELS = {1: T('Facile'), 2: T('Moyen'), 3: T('Difficile'), 4: T('Expert')}
    MODES = [(m, i, T(n), T(d)) for m, i, n, d in FR_MODES]
    NAMES_JSON = e(json.dumps({s['key']: s['name'] for s in SERIES}, ensure_ascii=False))
    GUIDES = load_guides(lang)
    GUIDES_BY_SERIE = {}
    for g in GUIDES:
        if g.get('serie') and g['serie'] in BY_KEY:
            GUIDES_BY_SERIE.setdefault(g['serie'], []).append(g)
    DLE_MODES = [(m, T(label), ico, T(desc)) for m, label, ico, desc in DLE.MODES]
    DLE_INFO = {m: (T(a), T(b)) for m, (a, b) in FR_DLE_INFO.items()}


AVAIL = {}   # langue -> chemins logiques disponibles (pour hreflang et le sélecteur de langue)
CUR_PATH = '/'


def lang_links(path):
    """Balises hreflang : seulement si la page existe dans plusieurs langues."""
    langs = [l for l in i18n.LANGS if path in AVAIL.get(l, ())]
    if len(langs) < 2:
        return ''
    out = ''.join(f'<link rel="alternate" hreflang="{l}" href="{SITE}{U(path, l)}">\n' for l in langs)
    return out + f'<link rel="alternate" hreflang="x-default" href="{SITE}{path}">\n'


def lang_switch():
    """Sélecteur FR | EN toujours visible en haut de page (la langue en cours est mise en avant)."""
    langs = [l for l in i18n.LANGS if AVAIL.get(l)]
    if len(langs) < 2:
        return ''
    names = {'fr': ('FR', 'Version française', 'Français'), 'en': ('EN', 'English version', 'English')}
    out = ''
    for l in langs:
        if l == i18n.LANG:
            out += f'<span class="lang-cur" lang="{l}" aria-current="true" title="{names[l][2]}">{names[l][0]}</span>'
        else:
            target = U(CUR_PATH, l) if CUR_PATH in AVAIL[l] else U('/', l)
            out += (f'<a href="{target}" hreflang="{l}" lang="{l}" data-lang="{l}" '
                    f'title="{names[l][1]}">{names[l][0]}</a>')
    return f'<div class="lang-sw" role="group" aria-label="{T("Langue")}">{out}</div>'


# Langue choisie automatiquement à l'arrivée sur le site : la langue principale du navigateur
# (français -> FR, toute autre langue -> EN), ou la langue choisie avec le sélecteur (mémorisée).
# Uniquement à l'arrivée depuis un autre site, jamais pour les robots (Google indexe chaque langue
# à son adresse, voir hreflang), et seulement si la page existe dans l'autre langue.
LANG_REDIRECT = ("<script>(function(){try{var d=document,h=d.documentElement.lang,n=navigator,"
                 "u=n.userAgent||'';if(/bot|crawl|spider|slurp|google|bing|yandex|baidu|duckduck|facebook|"
                 "lighthouse|headless|preview|inspect/i.test(u))return;"
                 "if(d.referrer&&d.referrer.indexOf(location.origin+'/')===0)return;"
                 "var p=null;try{p=localStorage.getItem('kq-lang')}catch(x){}"
                 "var w=p||(((n.languages&&n.languages[0])||n.language||'fr').slice(0,2).toLowerCase()==='fr'?'fr':'en');"
                 "if(w===h)return;var l=d.querySelector('link[rel=alternate][hreflang=\"'+w+'\"]');"
                 "if(l)location.replace(new URL(l.href).pathname+location.search+location.hash)}catch(x){}})()</script>\n")


# --------------------------------------------------------------------------- gabarit
LOGO = ('<svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="16" r="14.5" fill="none" stroke="#d4a843" stroke-width="2"/>'
        '<circle cx="16" cy="16" r="8.5" fill="none" stroke="#d4a843" stroke-width="1.2" opacity=".55"/>'
        '<circle cx="16" cy="16" r="3.6" fill="#d4a843"/></svg>')


def head(title, desc, path, jsonld=None, robots='index, follow', og_type='website', accent=None):
    global CUR_PATH
    CUR_PATH = path
    canonical = SITE + U(path)
    ld = ''
    for block in (jsonld or []):
        ld += '<script type="application/ld+json">' + json.dumps(block, ensure_ascii=False, separators=(',', ':')) + '</script>\n'
    style = f'<style>:root{{--accent:{accent}}}</style>\n' if accent else ''
    return f'''<!doctype html>
<html lang="{i18n.LANG}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canonical}">
{lang_links(path)}{LANG_REDIRECT if lang_links(path) else ''}<meta name="robots" content="{robots}">
<meta name="theme-color" content="#07080f">
<meta name="google-adsense-account" content="{PUB}">
<meta name="alldle-verify" content="zeH2tpvyQl3QIQMFda8JTGnZePXWWPus">
<meta property="og:site_name" content="KamiQuiz">
<meta property="og:locale" content="{i18n.LOCALES[i18n.LANG]}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/img/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/img/icon-192.png">
<link rel="manifest" href="/manifest.webmanifest">
<link rel="preload" href="/assets/fonts/bebas-neue-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{asset('/assets/css/fonts.css')}">
<link rel="stylesheet" href="{asset('/assets/css/site.css')}">
{style}<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={PUB}" crossorigin="anonymous"></script>
{ld}</head>
<body>
<a class="skip" href="#contenu">{T('Aller au contenu')}</a>
'''


CUR = ' aria-current="page"'
LETSDLE = 'https://letsdle.com/'
OK_CLS = ' class="ok"'
NAV = [('/quiz/', 'Tous les quiz'), ('/dle/', 'Kamidle'), ('/guides/', 'Guides'), ('/a-propos/', 'À propos')]


def header(current=''):
    ttl = T("Letsdle, d'autres petits jeux quotidiens (nouvel onglet)")
    letsdle = (f'<a class="nav-ext" href="{LETSDLE}" target="_blank" rel="noopener" '
               f'title="{ttl}">{T("Plus de jeux")}<span aria-hidden="true"> ↗</span></a>')
    links = ''.join(
        f'<a href="{U(href)}"{CUR if current == href else ""}>{T(label)}</a>' for href, label in NAV
        if (href != '/dle/' or dle_ready()) and (href != '/guides/' or GUIDES))
    return f'''<header class="site-head">
  <div class="wrap">
    <a class="brand" href="{U('/')}" aria-label="{T('KamiQuiz, accueil')}">{LOGO}<span>KAMI<b>QUIZ</b></span></a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">{T('Menu')}</button>
    <nav class="nav" id="nav" aria-label="{T('Navigation principale')}">{links}{letsdle}<a class="nav-cta" href="{U('/jouer/')}">{T('Jouer')}</a></nav>
    {lang_switch()}
  </div>
</header>
<main id="contenu">
'''


def footer(scripts=('/assets/js/site.js',)):
    present = {s['cat'] for s in SERIES}
    cats = ''.join(f'<li><a href="{U("/quiz/")}#{cid}">{name}</a></li>' for cid, name, _ in CATEGORIES if cid in present)
    extra = ''
    if dle_ready():
        extra += f'<li><a href="{U("/dle/")}">{T("Kamidle, jeux du jour")}</a></li>'
    if GUIDES:
        extra += f'<li><a href="{U("/guides/")}">{T("Guides")}</a></li>'
    if i18n.LANG != 'fr':
        scripts = (f'/assets/js/i18n-{i18n.LANG}.js',) + tuple(scripts)
    js = ''.join(f'<script src="{asset(s)}" defer></script>\n' for s in scripts)
    return f'''</main>
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="brand" href="{U('/')}">{LOGO}<span>KAMI<b>QUIZ</b></span></a>
        <p style="margin-top:14px;max-width:34ch">{T('Des quiz gratuits sur les animés, les séries, les films, les jeux vidéo et la culture générale. Sans inscription.')}</p>
        <a class="foot-badge" href="https://www.alldle.net/game/kamiquiz?ref=badge" target="_blank" rel="noopener" aria-label="Play on Alldle"><img src="https://www.alldle.net/badge.svg?g=eqqfouhthy68vr5qt4k7sjca&amp;variant=dark&amp;size=compact&amp;content=text" alt="Play on Alldle" width="180" height="48" loading="lazy" style="border:0" onerror="var a=this.parentNode;a.classList.add('foot-badge-txt');a.textContent='{T("Jouer sur Alldle")} ↗'"></a>
      </div>
      <div><h2>{T('Quiz')}</h2><ul>{cats}</ul></div>
      <div><h2>KamiQuiz</h2><ul>{extra}<li><a href="{U('/a-propos/')}">{T('À propos')}</a></li><li><a href="{U('/contact/')}">{T('Contact')}</a></li><li><a href="{U('/jouer/')}">{T('Quiz tout mélangé')}</a></li><li><a href="{LETSDLE}" target="_blank" rel="noopener">{T('Plus de jeux sur Letsdle ↗')}</a></li></ul></div>
      <div><h2>{T('Informations')}</h2><ul><li><a href="{U('/confidentialite/')}">{T('Confidentialité et cookies')}</a></li><li><a href="{U('/conditions/')}">{T("Conditions d'utilisation")}</a></li><li><a href="/sitemap.xml">{T('Plan du site')}</a></li></ul></div>
    </div>
    <p class="foot-note">{T('© 2026 KamiQuiz. KamiQuiz est un site indépendant, sans lien avec les ayants droit des œuvres citées. Les noms des œuvres appartiennent à leurs propriétaires respectifs.')}</p>
  </div>
</footer>
{js}<script>if('serviceWorker' in navigator){{addEventListener('load',function(){{navigator.serviceWorker.register('/sw.js').catch(function(){{}})}})}}</script>
</body>
</html>
'''


def write(path, content):
    path = U(path)
    out = DIST / path.lstrip('/')
    if path.endswith('/'):
        out = out / 'index.html'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding='utf-8')


PAGES = []  # (path, priority, changefreq) pour le sitemap


def page(path, prio='0.6', freq='monthly', lastmod=None):
    PAGES.append((i18n.LANG, path, prio, freq, lastmod or TODAY))


def crumbs_ld(items):
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': SITE + U(p)} for i, (n, p) in enumerate(items)]}


def crumbs_html(items):
    lis = ''.join(f'<li><a href="{U(p)}">{e(n)}</a></li>' if i < len(items) - 1 else f'<li aria-current="page">{e(n)}</li>'
                  for i, (n, p) in enumerate(items))
    label = T("Fil d'Ariane")
    return f'<nav class="crumbs" aria-label="{label}"><ol>{lis}</ol></nav>'


_ART = {}


def art(s):
    """URL du visuel maison de la série (SVG écrit dans dist/, empreinte de contenu pour le cache d'un an)."""
    if s['key'] not in _ART:
        import hashlib
        svg = visual_svg(s['key'], s['color'])
        out = DIST / 'assets' / 'img' / 'series' / f'{s["key"]}.svg'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(svg, encoding='utf-8')
        _ART[s['key']] = f'/assets/img/series/{s["key"]}.svg?v={hashlib.sha256(svg.encode()).hexdigest()[:10]}'
    return _ART[s['key']]


def art_img(s, cls, eager=False):
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return f'<img class="{cls}" src="{art(s)}" alt="" width="1600" height="900" decoding="async" {load}>'


def series_row(s):
    return (f'<li class="series-row"><a href="{U("/quiz/" + s["slug"] + "/")}" style="--c:{s["color"]}">'
            f'<span class="thumb">{art_img(s, "thumb-art")}</span>'
            f'<span><span class="nm">{e(s["name"])}</span><span class="ds">{e(s["tag"])}</span></span>'
            f'<span class="ct">{T("{n} questions", n=s["n"])}</span></a></li>')


def tile(s, badge='', big=False):
    b = f'<span class="badge">{e(badge)}</span>' if badge else ''
    return (f'<a class="tile{" tile-lg" if big else ""}" href="{U("/quiz/" + s["slug"] + "/")}" style="--c:{s["color"]}">'
            f'{art_img(s, "tile-art")}{b}'
            f'<span class="nm">{e(s["name"])}</span><p>{e(s["tag"])}</p></a>')


# --------------------------------------------------------------------------- guides
def md_to_html(md):
    out, para, lst = [], [], None

    def inline(t):
        t = e(t, quote=False)
        t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
        t = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', t)
        return t

    def flush():
        nonlocal para, lst
        if para:
            out.append('<p>' + inline(' '.join(para)) + '</p>')
            para = []
        if lst:
            tag, items = lst
            out.append(f'<{tag}>' + ''.join(f'<li>{inline(i)}</li>' for i in items) + f'</{tag}>')
            lst = None

    for line in md.splitlines():
        s = line.strip()
        if not s:
            flush()
        elif s.startswith('### '):
            flush(); out.append(f'<h3>{inline(s[4:])}</h3>')
        elif s.startswith('## '):
            flush(); out.append(f'<h2>{inline(s[3:])}</h2>')
        elif s.startswith('> '):
            flush(); out.append(f'<blockquote>{inline(s[2:])}</blockquote>')
        elif re.match(r'^- ', s):
            if para:
                flush()
            if not lst or lst[0] != 'ul':
                flush(); lst = ('ul', [])
            lst[1].append(s[2:])
        elif re.match(r'^\d+\. ', s):
            if para:
                flush()
            if not lst or lst[0] != 'ol':
                flush(); lst = ('ol', [])
            lst[1].append(re.sub(r'^\d+\. ', '', s))
        else:
            if lst:
                flush()
            para.append(s)
    flush()
    return '\n'.join(out)


def load_guides(lang='fr'):
    """Guides publiés. En anglais, chaque fichier de content/en/guides/ indique son guide français (fr:) ;
    le slug logique reste le slug français, U() donne le slug traduit."""
    guides = []
    folder = ROOT / 'content' / ('guides' if lang == 'fr' else f'{lang}/guides')
    for f in sorted(folder.glob('*.md')):
        raw = f.read_text(encoding='utf-8')
        meta_txt, body = raw.split('\n\n', 1)
        meta = dict(line.split(': ', 1) if ': ' in line else (line.rstrip(':'), '') for line in meta_txt.splitlines())
        meta['slug'] = f.stem
        if lang != 'fr':
            i18n.GUIDE_SLUGS[lang][meta['fr']] = f.stem
            meta['slug'] = meta['fr']
        meta['html'] = md_to_html(body)
        meta['words'] = len(re.sub(r'<[^>]+>', ' ', meta['html']).split())
        guides.append(meta)
    order = ['personnages-puissants-naruto', 'fruits-du-demon-one-piece', 'maisons-poudlard-harry-potter',
             'piliers-demon-slayer', 'neuf-titans-attack-on-titan', 'transformations-goku-dragon-ball',
             'maisons-game-of-thrones', 'regles-death-note', 'table-des-types-pokemon', 'reviser-avec-un-quiz']
    guides = [g for g in guides if g.get('date', BASE_DATE) <= TODAY]
    guides.sort(key=lambda g: order.index(g['slug']) if g['slug'] in order else 99)
    guides.sort(key=lambda g: g.get('date', BASE_DATE), reverse=True)
    return guides




# --------------------------------------------------------------------------- accueil
def build_home():
    keys = ','.join(s['key'] for s in SERIES)
    by_cat = Counter(s['cat'] for s in SERIES)
    pop = [BY_KEY[k] for k in POPULAR if k in BY_KEY]
    recent = [s['key'] for s in sorted(SERIES, key=lambda s: s['date'], reverse=True) if s['date'] > BASE_DATE]
    new = [BY_KEY[k] for k in (recent + [k for k in NEW_FALLBACK if k not in recent]) if k in BY_KEY][:3]
    cats_html = ''.join(
        f'<a class="chip" href="{U("/quiz/")}#{cid}">{name} <span class="muted">{by_cat[cid]}</span></a>' for cid, name, _ in CATEGORIES if by_cat[cid])
    modes = ''.join(f'<a class="mode" href="{U("/jouer/")}?m={m}"><span class="mode-ico" aria-hidden="true">{i}</span>'
                    f'<span class="mode-name">{n}</span><p>{d}</p></a>' for m, i, n, d in MODES)
    guides = ''.join(f'<li><a href="{U("/guides/" + g["slug"] + "/")}"><span class="gt">{e(g["title"])}</span>'
                     f'<span class="gd">{e(g["description"])}</span></a></li>' for g in GUIDES[:4])
    ld = [
        {'@context': 'https://schema.org', '@type': 'WebSite', 'name': 'KamiQuiz', 'url': SITE + U('/'), 'inLanguage': i18n.LANG},
        {'@context': 'https://schema.org', '@type': 'Organization', 'name': 'KamiQuiz', 'url': SITE + '/',
         'logo': SITE + '/assets/img/icon-512.png', 'email': 'contact@kamiquiz.com'},
    ]
    nq, ns = fr_num(TOTAL_Q), NB_SERIES
    rows = ''.join(series_row(BY_KEY[k]) for k in ['onepiece', 'jjk', 'demonslayer', 'got', 'harrypotter', 'zelda', 'histoire', 'geo'] if k in BY_KEY)
    tiles_pop = tile(pop[0], big=True) + ''.join(tile(s) for s in pop[1:5])
    tiles_new = ''.join(tile(s, T('Nouveau')) for s in new)
    guides_block = ''
    if guides:
        guides_block = f'''<div>
      <h2 class="h2">{T('Guides et dossiers')}</h2>
      <p class="muted">{T('Pour réviser avant de jouer, ou comprendre une réponse.')}</p>
      <ul class="guide-list">{guides}</ul>
      <p style="margin-top:16px"><a href="{U('/guides/')}">{T('Tous les guides')}</a></p>
    </div>'''
    body = f'''<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <h1 class="display">{T("Le quiz qui t'élève <span>au rang de Kami</span>")}</h1>
      <p class="lede">{T('{nq} questions sur {ns} univers, des shōnen aux séries cultes. Chaque réponse est expliquée, pour apprendre autant que pour jouer.', nq=nq, ns=ns)}</p>
      <div class="btn-row">
        <a class="btn btn-gold" href="{U('/quiz/')}">{T('Choisir un quiz')}</a>
        <a class="btn" href="{U('/jouer/')}">{T('Tout mélanger')}</a>
      </div>
      <div class="hero-facts">
        <div>{nq}<small>{T('questions expliquées')}</small></div>
        <div>{ns}<small>{T('univers')}</small></div>
        <div>{T('0 €')}<small>{T('sans inscription')}</small></div>
      </div>
    </div>
    <div class="qcard" id="qdj" data-keys="{keys}" data-names="{NAMES_JSON}" aria-labelledby="qdj-title">
      <div class="qcard-top"><strong id="qdj-title">{T('Question du jour')}</strong><span class="chip" data-serie><i></i>…</span></div>
      <div data-slot><p class="qtext">{T('Chargement de la question du jour…')}</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><div><h2 class="h2">{T('Les plus joués')}</h2></div><p>{T('Les univers favoris de la communauté, pour commencer en terrain connu.')}</p></div>
    <div class="tiles">{tiles_pop}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><div><h2 class="h2">{T('Nouveaux univers')}</h2></div><p>{T('Les derniers quiz arrivés sur le site.')}</p></div>
    <div class="tiles">{tiles_new}</div>
  </div>
</section>
{dle_home_section()}
<section class="section">
  <div class="wrap">
    <div class="section-head"><div><h2 class="h2">{T('Tous les univers')}</h2></div><p>{T('Cinq grandes familles, {ns} quiz.', ns=ns)}</p></div>
    <div class="cat-nav">{cats_html}</div>
    <ul class="series-list">{rows}</ul>
    <p style="margin-top:20px"><a href="{U('/quiz/')}">{T('Voir les {ns} quiz', ns=ns)}</a></p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><div><h2 class="h2">{T('Six façons de jouer')}</h2></div><p>{T('Chaque mode fonctionne avec tous les univers, ou avec toutes les questions mélangées.')}</p></div>
    <div class="modes">{modes}</div>
  </div>
</section>

<section class="section">
  <div class="wrap two-col">
    <div>
      <h2 class="h2">{T('Classement mondial')}</h2>
      <p class="muted">{T("Les meilleurs scores, toutes séries confondues. Enregistrez le vôtre à la fin d'une partie.")}</p>
      <ol class="board" data-board="global" data-names="{NAMES_JSON}"><li class="board-empty"><span class="empty">{T('Chargement du classement…')}</span></li></ol>
    </div>
    {guides_block}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="callout prose">
      <h2 class="h2">{T('Un quiz pour apprendre, pas seulement pour gagner')}</h2>
      <p class="muted">{T("KamiQuiz est né d'une idée simple : un bon quiz doit expliquer ses réponses. Chaque question est accompagnée d'une explication, chaque série a sa page de révision avec toutes ses questions classées par thème, et le jeu privilégie les questions que vous n'avez pas encore vues.")}</p>
      <a href="{U('/a-propos/')}">{T('En savoir plus sur KamiQuiz')}</a>
    </div>
  </div>
</section>
'''
    write('/', head(T('KamiQuiz — {nq} questions de quiz sur les animés, séries, films et jeux', nq=nq),
                    T('Quiz gratuits et sans inscription : {nq} questions expliquées sur {ns} univers, de Naruto à Game of Thrones. Question du jour, six modes de jeu et classement mondial.', nq=nq, ns=ns),
                    '/', ld) + header('/') + body + footer())
    page('/', '1.0', 'daily')


# --------------------------------------------------------------------------- tous les quiz
def build_index():
    blocks = ''
    for cid, name, desc in CATEGORIES:
        items = [s for s in SERIES if s['cat'] == cid]
        n = sum(s['n'] for s in items)
        if not items:
            continue
        blocks += (f'<section class="cat-block" id="{cid}"><header><h2>{name}</h2><span>{T("{a} quiz, {b} questions", a=len(items), b=fr_num(n))}</span></header>'
                   f'<p class="muted" style="margin:12px 0 4px">{e(desc)}</p><ul class="series-list">{"".join(series_row(s) for s in items)}</ul></section>')
    present = {s['cat'] for s in SERIES}
    nav = ''.join(f'<a class="chip" href="#{cid}">{name}</a>' for cid, name, _ in CATEGORIES if cid in present)
    crumbs = [(T('Accueil'), '/'), (T('Tous les quiz'), '/quiz/')]
    ld = [crumbs_ld(crumbs),
          {'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': T('Tous les quiz KamiQuiz'), 'url': SITE + U('/quiz/'),
           'hasPart': [{'@type': 'Quiz', 'name': T('Quiz {n}', n=s["name"]), 'url': SITE + U('/quiz/' + s['slug'] + '/')} for s in SERIES]}]
    body = f'''<div class="wrap">
  <div class="page-head">
    {crumbs_html(crumbs)}
    <h1 class="h1">{T('Tous les quiz')}</h1>
    <p class="lede">{T('{ns} univers et {nq} questions, rangés par famille. Chaque quiz a sa page avec les questions à réviser et six modes de jeu.', ns=NB_SERIES, nq=fr_num(TOTAL_Q))}</p>
  </div>
  <div class="cat-nav" style="margin-top:28px">{nav}<a class="chip" href="{U('/jouer/')}">{T('Tout mélanger')}</a></div>
  {blocks}
</div>
'''
    write('/quiz/', head(T('Tous les quiz : animés, séries, films, jeux vidéo et culture — KamiQuiz'),
                         T('La liste complète des {ns} quiz gratuits de KamiQuiz : Naruto, One Piece, Harry Potter, Game of Thrones, Pokémon, histoire, géographie et bien plus.', ns=NB_SERIES),
                         '/quiz/', ld) + header('/quiz/') + body + footer())
    page('/quiz/', '0.9', 'weekly')


# --------------------------------------------------------------------------- pages série
def build_serie(s):
    d = s['data']
    qs = d['q']
    cats = list(d['cats'].keys())
    by_cat = {c: [q for q in qs if q['cat'] == c] for c in cats}
    lv = Counter(q['d'] for q in qs)
    path = f'/quiz/{s["slug"]}/'
    crumbs = [(T('Accueil'), '/'), (T('Tous les quiz'), '/quiz/'), (s['name'], path)]

    groups = ''
    for c in cats:
        items = by_cat[c]
        if not items:
            continue
        lis = ''
        for q in items:
            opts = ''.join(f'<li{OK_CLS if i == q["c"] else ""}>{e(a)}</li>' for i, a in enumerate(q['a']))
            expl = f'<p class="expl">{e(q["fb"])}</p>' if q['fb'] else ''
            lis += (f'<li class="qitem"><details><summary><span>{e(q["q"])}</span><span class="lvl">{LEVELS[q["d"]]}</span></summary>'
                    f'<ul class="opts">{opts}</ul>{expl}</details></li>')
        icon = d['cats'][c].get('i', '')
        groups += f'<section class="qgroup"><h3>{e(icon)} {e(c)} <small>{T("{n} questions", n=len(items))}</small></h3><ol class="qlist">{lis}</ol></section>'

    play = U('/jouer/')
    modes = ''.join(f'<a class="mode" href="{play}?s={s["key"]}&amp;m={m}"><span class="mode-ico" aria-hidden="true">{i}</span>'
                    f'<span class="mode-name">{n}</span><p>{dsc}</p></a>' for m, i, n, dsc in MODES)

    ranks = d.get('ranks') or []
    rank_items = ''
    if ranks:
        step = 100 / len(ranks)
        rank_items = ''.join(f'<li><span>{e(r)}</span><span>{T("{p} %+", p=round(i * step))}</span></li>' for i, r in enumerate(ranks))

    related = [o for o in SERIES if o['cat'] == s['cat'] and o['key'] != s['key']][:6]
    related_html = ''.join(series_row(o) for o in related)
    guides = GUIDES_BY_SERIE.get(s['key'], [])
    guide_html = ''
    if guides:
        guide_html = (f'<h2>{T("Pour aller plus loin")}</h2><ul class="guide-list">' + ''.join(
            f'<li><a href="{U("/guides/" + g["slug"] + "/")}"><span class="gt">{e(g["title"])}</span><span class="gd">{e(g["description"])}</span></a></li>'
            for g in guides) + '</ul>')

    themes = ', '.join(cats[:-1]) + (T(' et ') + cats[-1] if len(cats) > 1 else cats[0])
    desc = T('Quiz {name} gratuit : {n} questions corrigées et expliquées sur {themes}. Jouez en ligne sans inscription ou révisez toutes les réponses.',
             name=s['name'], n=s['n'], themes=themes.lower())
    if len(desc) > 165:
        desc = T('Quiz {name} gratuit : {n} questions corrigées et expliquées. Six modes de jeu, sans inscription, avec toutes les réponses à réviser.', name=s['name'], n=s['n'])

    ld = [crumbs_ld(crumbs), {
        '@context': 'https://schema.org', '@type': 'Quiz', 'name': T('Quiz {n}', n=s['name']), 'url': SITE + U(path),
        'description': desc, 'inLanguage': i18n.LANG, 'about': {'@type': 'Thing', 'name': s['name']},
        'educationalLevel': T('Tous niveaux'), 'isAccessibleForFree': True,
        'provider': {'@type': 'Organization', 'name': 'KamiQuiz', 'url': SITE + '/'}}]

    intro = ''.join(f'<p>{e(p)}</p>' for p in s['intro'])
    trailer_html = ''
    if s['key'] in TRAILERS and i18n.LANG == 'fr':
        yt, ttl, chan = TRAILERS[s['key']]
        trailer_html = f'''<h2>La bande-annonce</h2>
      <figure class="trailer" data-yt="{e(yt)}" data-title="{e(ttl)}" style="--c:{s["color"]}">
        <button class="trailer-play" type="button" aria-label="Lire la bande-annonce : {e(ttl)} (vidéo YouTube)">
          {art_img(s, "trailer-art")}
          <span class="trailer-btn" aria-hidden="true"><svg viewBox="0 0 24 24" width="30" height="30"><path d="M8 5.5v13l11-6.5z" fill="currentColor"/></svg></span>
          <span class="trailer-cap"><span class="trailer-kicker">Bande-annonce officielle</span><span class="trailer-ttl">{e(ttl)}</span></span>
        </button>
        <figcaption>Vidéo publiée par {e(chan)} sur YouTube. Elle ne se charge que si vous lancez la lecture. <a href="https://www.youtube.com/watch?v={e(yt)}" target="_blank" rel="noopener">Ouvrir sur YouTube</a></figcaption>
      </figure>'''
    lv_items = ''.join(f'<li><span>{LEVELS[k]}</span><span>{lv[k]}</span></li>' for k in (1, 2, 3, 4) if lv[k])
    cat_items = ''.join(f'<li><span>{e(d["cats"][c].get("i", ""))} {e(c)}</span><span>{len(by_cat[c])}</span></li>' for c in cats)

    ranks_html = f"<h2 style='margin-top:22px'>{T('Rangs à décrocher')}</h2><ul class='ranks'>" + rank_items + "</ul>" if rank_items else ""
    name = e(s['name'])
    body = f'''<section class="serie-head">
  <div class="serie-art" aria-hidden="true">{art_img(s, "serie-art-img", eager=True)}</div>
  <div class="wrap">
    {crumbs_html(crumbs)}
    <h1 class="h1">{T('Quiz <em>{name}</em>', name=name)}</h1>
    <p class="lede">{e(s["tag"])}</p>
    <div class="btn-row">
      <a class="btn btn-gold" href="{play}?s={s["key"]}&amp;m=libre">{T('Jouer 20 questions')}</a>
      <a class="btn" href="{play}?s={s["key"]}">{T('Choisir un mode')}</a>
      <a class="btn" href="#questions">{T('Réviser les réponses')}</a>
    </div>
    <div class="facts">
      <span class="chip"><i></i>{T('{n} questions', n=s["n"])}</span>
      <span class="chip">{T('{n} thèmes', n=len(cats))}</span>
      <span class="chip">{T('{a} faciles ou moyennes, {b} difficiles', a=lv[1] + lv[2], b=lv[3] + lv[4])}</span>
    </div>
  </div>
</section>
<div class="wrap section" style="padding-top:48px">
  <div class="serie-body">
    <article class="article">
      <h2 style="margin-top:0">{T('À propos de ce quiz')}</h2>
      {intro}
      {trailer_html}
      <h2>{T('Les modes de jeu')}</h2>
      <div class="modes">{modes}</div>
      <h2 id="questions">{T('Les {n} questions et leurs réponses', n=s["n"])}</h2>
      <p>{T("Toutes les questions du quiz {name}, classées par thème. Cliquez sur une question pour afficher la bonne réponse et son explication, ou tentez d'abord votre chance en jouant.", name=name)}</p>
      <div class="revise-tools"><button class="btn btn-sm" type="button" data-reveal="open">{T('Afficher toutes les réponses')}</button><button class="btn btn-sm" type="button" data-reveal="close">{T('Tout masquer')}</button></div>
      {groups}
      {guide_html}
      <h2>{T('Autres quiz {cat}', cat=e(CAT_NAME[s["cat"]].lower()))}</h2>
      <ul class="series-list">{related_html}</ul>
    </article>
    <aside>
      <div class="aside-box">
        <h2>{T('Thèmes')}</h2><ul>{cat_items}</ul>
        <h2 style="margin-top:22px">{T('Difficulté')}</h2><ul>{lv_items}</ul>
        {ranks_html}
        <h2 style="margin-top:22px">{T('Meilleurs scores')}</h2>
        <ol class="board" data-board="{s["key"]}" data-names="{NAMES_JSON}" style="font-size:.9rem"><li class="board-empty"><span class="empty">{T('Chargement…')}</span></li></ol>
      </div>
    </aside>
  </div>
</div>
'''
    write(path, head(T('Quiz {name} : {n} questions avec réponses — KamiQuiz', name=s['name'], n=s['n']), desc, path, ld,
                     accent=s['color']) + header() + body + footer())
    page(path, '0.8', 'monthly', s['date'])


# --------------------------------------------------------------------------- app de jeu
def build_play():
    series_js = json.dumps({s['key']: {'name': s['name'], 'slug': U('/quiz/' + s['slug'] + '/').split('/')[-2], 'color': s['color']} for s in SERIES},
                           ensure_ascii=False, separators=(',', ':'))
    body = f'''<section class="app">
  <div class="wrap app-shell">
    <div class="app-title"><h1>{T('Quiz <em data-app-name>KamiQuiz</em>')}</h1></div>

    <div class="screen" id="s-loading"><p class="loading">{T('Chargement des questions…')}</p></div>

    <div class="screen" id="s-setup" hidden>
      <p class="lede" style="margin-bottom:24px">{T('Choisissez votre façon de jouer.')}</p>
      <div class="pick-grid" id="mode-grid"></div>
      <div class="cat-picker" id="cat-picker" hidden>
        <h2 class="h2">{T('Choisissez vos thèmes')}</h2>
        <div class="chips" id="cat-chips"></div>
        <button class="btn btn-gold" type="button" id="cat-go">{T('Lancer le quiz')}</button>
      </div>
      <div class="cat-picker" id="duel-picker" hidden>
        <h2 class="h2">{T("Qui s'affronte ?")}</h2>
        <div class="duel-names">
          <label class="sr-only" for="p1">{T('Nom du joueur 1')}</label><input id="p1" maxlength="20" placeholder="{T('Joueur 1')}" autocomplete="off">
          <label class="sr-only" for="p2">{T('Nom du joueur 2')}</label><input id="p2" maxlength="20" placeholder="{T('Joueur 2')}" autocomplete="off">
        </div>
        <button class="btn btn-gold" type="button" id="duel-go">{T('Commencer le duel')}</button>
      </div>
      <p class="muted" style="margin-top:28px">{T("Envie d'un autre univers ? <a href=\"{u}\">Voir tous les quiz</a>.", u=U('/quiz/'))}</p>
    </div>

    <div class="screen" id="s-play" hidden>
      <div class="hud"><span id="hud-left"></span><span data-mode-name></span><span id="hud-right"></span></div>
      <div class="progress" aria-hidden="true"><span id="bar"></span></div>
      <div class="timer" id="timer" hidden aria-hidden="true"><span></span></div>
      <div class="qcard">
        <div class="qcard-top" id="q-meta"></div>
        <p class="qtext" id="q-text" aria-live="polite"></p>
        <div class="answers" id="q-answers"></div>
        <div class="feedback" id="q-feedback" hidden aria-live="polite"></div>
      </div>
      <div class="app-next">
        <button class="btn btn-sm" type="button" id="quit">{T('Arrêter')}</button>
        <button class="btn btn-gold" type="button" id="next" hidden>{T('Question suivante')}</button>
      </div>
      <p class="muted" style="font-size:.82rem;margin-top:14px">{T('Astuce : répondez avec les touches A, B, C, D ou 1 à 4, puis Entrée pour continuer.')}</p>
    </div>

    <div class="screen result" id="s-result" hidden>
      <div id="result-main"></div>
      <div class="btn-row">
        <button class="btn btn-gold" type="button" id="again">{T('Rejouer')}</button>
        <button class="btn" type="button" id="other-mode">{T('Changer de mode')}</button>
        <button class="btn" type="button" id="share">{T('Partager mon score')}</button>
        <a class="btn" id="to-revise" href="{U('/quiz/')}">{T('Réviser les réponses')}</a>
      </div>
      <div class="save-score" id="save-box">
        <form id="save-form">
          <label for="save-name">{T('Entrer au classement mondial')}</label>
          <div class="row"><input id="save-name" maxlength="20" placeholder="{T('Votre pseudo')}" autocomplete="nickname"><button class="btn btn-gold btn-sm" id="save-btn" type="submit">{T('Enregistrer')}</button></div>
        </form>
        <p id="save-msg"></p>
      </div>
      <div class="review" id="review" hidden><h2>{T('Les réponses à retenir')}</h2><ol id="review-list"></ol></div>
    </div>
  </div>
</section>
<script>window.KQ_SERIES={series_js};</script>
'''
    write('/jouer/', head(T('Jouer — KamiQuiz'), T('Jouez aux quiz KamiQuiz : six modes de jeu, réponses expliquées et classement mondial.'),
                          '/jouer/', robots='noindex, follow') + header() + body + footer(('/assets/js/site.js', '/assets/js/quiz.js')))


# --------------------------------------------------------------------------- Kamidle (jeux du jour)
DLE_START = '2026-10-27'          # Kamidle n°1
DLE_DAYS = 800                    # calendrier calculé d'avance, identique dans tous les déploiements
FR_DLE_INFO = {
    'personnage': ('Devine le personnage du jour',
                   "Propose un personnage : chaque essai indique ce qu'il partage avec la cible (univers, catégorie, genre, espèce, rôle, style, âge, cheveux et année de sortie). Essais illimités, deux indices se débloquent en route."),
    'pouvoir': ('Devine le pouvoir du jour',
                "Un pouvoir ou une technique est décrit sans le moindre nom. À toi de trouver son propriétaire en six essais. Chaque erreur débloque un indice."),
    'emoji': ('Devine le personnage en emojis',
              "Un personnage est résumé en quelques emojis. Le premier est offert, chaque erreur en dévoile un nouveau. Six essais."),
    'univers': ("Devine l'univers du jour",
                "Cinq indices, du plus vague au plus précis, décrivent un animé, une série, une saga ou un jeu. Trouve-le avec le moins d'indices possible."),
    'mot': ('Le Mot mystère du jour',
            "Un mot tiré de l'univers des animés, des séries et des jeux vidéo. Six essais : chaque lettre bien placée s'affiche en vert, chaque lettre présente mais mal placée en jaune."),
}


def dle_avail():
    """Date de publication de chaque univers (les personnages suivent leur série)."""
    return {s['key']: s['date'] for s in ALL_SERIES}


def dle_schedule():
    """Calendrier fixe : même résultat quel que soit le jour de génération.

    Les pools partent de l'ordre figé DLE.SCHED_V1 ; un personnage retiré n'est plus tiré,
    un personnage ajouté vient en fin de file. Le Mot mystère a son propre tirage, fait après
    les autres jeux pour ne rien changer à leur calendrier.
    """
    import random
    avail = dle_avail()
    live = {c['id']: c for c in DLE.CHARS}
    v1_ids = {r[0] for r in DLE.SCHED_V1}
    extra = [c for c in DLE.CHARS if c['id'] not in v1_ids]
    start = datetime.date.fromisoformat(DLE_START)
    NEVER = '9999-12-31'
    pools = {
        'personnage': [(i, u) for i, u, _, _ in DLE.SCHED_V1],
        'pouvoir': [(i, u) for i, u, has_p, _ in DLE.SCHED_V1 if has_p],
        'emoji': [(i, u) for i, u, _, n in DLE.SCHED_V1 if n >= 2],
        'univers': [(k, k) for k in DLE.UNIVERS_V1],
        'mot': [(m, None) for m, _ in DLE.MOTS],
    }
    queues = {}
    for m, pool in pools.items():
        q = list(pool)
        random.Random('kamidle-' + m).shuffle(q)
        if m == 'personnage':
            q += [(c['id'], c['u']) for c in extra]
        elif m == 'pouvoir':
            q += [(c['id'], c['u']) for c in extra if c['p']]
            # pouvoirs donnés après coup à des personnages de SCHED_V1 : en fin de file, après les nouveaux personnages
            v1_no_p = {i for i, _, has_p, _ in DLE.SCHED_V1 if not has_p}
            q += [(c['id'], c['u']) for c in DLE.CHARS if c['id'] in v1_no_p and c['p']]
        elif m == 'emoji':
            q += [(c['id'], c['u']) for c in extra if len(c['emo']) >= 2]
        elif m == 'univers':
            q += [(k, k) for k in DLE.UNIVERS if k not in DLE.UNIVERS_V1]
        queues[m] = q

    def ok_date(m, iid, u, day):
        # Les personnages retirés comptent encore ici : le tirage reste identique à l'original,
        # puis on les remplace un par un plus bas.
        return m == 'mot' or avail.get(u, NEVER) <= day

    sched = {m: [] for m in pools}
    prev_u = {m: None for m in pools}
    for d in range(DLE_DAYS):
        day = (start + datetime.timedelta(days=d)).isoformat()
        used = set()
        for m in ('univers', 'personnage', 'pouvoir', 'emoji', 'mot'):
            q = queues[m]
            pick = None
            for strict in (True, False):
                for i, (iid, u) in enumerate(q):
                    if not ok_date(m, iid, u, day):
                        continue
                    if strict and m != 'mot' and (u == prev_u[m] or (m != 'univers' and iid in used)):
                        continue
                    pick = i
                    break
                if pick is not None:
                    break
            iid, u = q.pop(pick)
            q.append((iid, u))
            sched[m].append(iid)
            used.add(iid)
            prev_u[m] = u

    # Remplacement des personnages retirés, jour par jour, sans toucher aux autres jours.
    for m in ('personnage', 'pouvoir', 'emoji'):
        late = {i for i, _, has_p, _ in DLE.SCHED_V1 if not has_p} if m == 'pouvoir' else set()
        fits = [c['id'] for c in DLE.CHARS if (m != 'pouvoir' or c['p']) and (m != 'emoji' or len(c['emo']) >= 2)]
        ok = [i for i in fits if i in v1_ids and i not in late]
        random.Random('kamidle-remplacement-' + m).shuffle(ok)
        # personnages et pouvoirs ajoutés après SCHED_V1 : après le tirage d'origine, pour ne rien changer aux jours passés
        ok += [i for i in fits if i not in v1_ids] + [i for i in fits if i in late]
        k = 0
        for d, iid in enumerate(sched[m]):
            if iid in live:
                continue
            day = (start + datetime.timedelta(days=d)).isoformat()
            others = {sched[o][d] for o in ('personnage', 'pouvoir', 'emoji') if o != m}
            recent = set(sched[m][max(0, d - 60):d + 60])
            for _ in range(len(ok)):
                cand = ok[k % len(ok)]
                k += 1
                if avail[live[cand]['u']] <= day and cand not in others and cand not in recent:
                    sched[m][d] = cand
                    break
            else:
                sched[m][d] = next(c for c in ok if avail[live[c]['u']] <= day)
    return sched


def dle_cards():
    state = T("À jouer aujourd'hui")
    return ''.join(
        f'<a class="dle-card" href="{U("/dle/" + m + "/")}" data-dle-card="{m}"><span class="dle-ico" aria-hidden="true">{ico}</span>'
        f'<span class="dle-name">{label}</span><p>{e(desc)}</p><span class="dle-state" data-state>{state}</span></a>'
        for m, label, ico, desc in DLE_MODES)


def dle_ready():
    return i18n.LANG == 'fr' or (ROOT / 'content' / i18n.LANG / 'dle.py').exists()


def dle_home_section():
    if not dle_ready():
        return ''
    return f'''
<section class="section">
  <div class="wrap">
    <div class="section-head"><div><h2 class="h2">{T('Kamidle, les jeux du jour')}</h2></div><p>{T('Cinq énigmes par jour, les mêmes pour tout le monde. Trouve-les, garde ta série et partage ton résultat.')}</p></div>
    <div class="dle-modes">{dle_cards()}</div>
  </div>
</section>
'''


def dle_source():
    """Données du Kamidle dans la langue en cours : le module français, ou sa traduction (content/<langue>/dle.py)."""
    if i18n.LANG == 'fr':
        return DLE
    return __import__(f'{i18n.LANG}.dle', fromlist=['localize']).localize(DLE)


def build_dle():
    D = dle_source()
    keys = {s['key'] for s in SERIES}
    chars = [c for c in D.CHARS if c['u'] in keys]
    series = {s['key']: {'n': s['name'], 's': U('/quiz/' + s['slug'] + '/').split('/')[-2], 'c': s['cat']} for s in SERIES}
    sched = dle_schedule()
    if i18n.LANG != 'fr':
        sched['mot'] = D.word_schedule(DLE_START, DLE_DAYS)
    data = {
        'start': DLE_START,
        'cats': {cid: name for cid, name, _ in CATEGORIES},
        'series': series,
        'chars': chars,
        'univers': {k: v for k, v in D.UNIVERS.items() if k in keys},
        'mots': {m: d for m, d in D.MOTS},
        'ages': D.AGES,
        'hairNear': [sorted(g) for g in D.HAIR_NEAR],
        'sched': sched,
    }
    out = DIST / 'data' if i18n.LANG == 'fr' else DIST / 'data' / i18n.LANG
    out.mkdir(parents=True, exist_ok=True)
    # Liste des mots acceptés pour le Mot mystère : dictionnaire (licence MIT, voir data/mots-<langue>.LICENSE.txt)
    # + mots du jeu + noms d'univers et de personnages d'un seul mot
    valid = set((ROOT / 'data' / f'mots-{i18n.LANG}.txt').read_text(encoding='utf-8').split())
    valid |= {m for m, _ in D.MOTS}
    for c in chars:
        for part in re.split(r'[^A-Za-zÀ-ÿ]+', c['name'] + ' ' + ' '.join(c['alias'])):
            w = ''.join(ch for ch in __import__('unicodedata').normalize('NFD', part) if ch.isalpha() and ord(ch) < 128).upper()
            if 5 <= len(w) <= 8:
                valid.add(w)
    (out / 'mots.txt').write_text('\n'.join(sorted(valid)), encoding='utf-8')
    (out / 'dle.json').write_text(json.dumps(data, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    n_chars, n_pow = len(chars), sum(1 for c in chars if c['p'])
    n_univ = len(data['univers'])
    scripts = ('/assets/js/site.js', '/assets/js/dle.js')

    # ----- page d'accueil du Kamidle
    crumbs = [(T('Accueil'), '/'), ('Kamidle', '/dle/')]
    letsdle = T('Letsdle, un site ami, rassemble d\'autres petits jeux à une partie par jour : quiz sur les films d\'animation, associations de mots, géographie et plateformes piégées. <a href="{u}" target="_blank" rel="noopener">Découvrir Letsdle</a>.', u=LETSDLE)
    body = f'''<div class="wrap">
  <div class="page-head">
    {crumbs_html(crumbs)}
    <h1 class="h1">{T('Kamidle, les jeux du jour')}</h1>
    <p class="lede">{T('Cinq énigmes chaque jour, les mêmes pour tous les joueurs : un personnage, un pouvoir, des emojis, un univers et un mot mystère à deviner.')}</p>
  </div>
  <div class="dle-modes" style="margin-top:32px">{dle_cards()}</div>
  <p class="dle-summary" data-dle-summary></p>
  <div class="two-col" style="margin-top:56px">
    <article class="prose">
      <h2 class="h2">{T('Comment ça marche')}</h2>
      <p>{T("Le Kamidle s'inspire des jeux en « -dle » nés avec Wordle : une énigme par jour, identique pour tout le monde, qui change à minuit (heure de ton appareil). Tu as le temps de réfléchir, de revenir plus tard dans la journée, et de comparer ton résultat avec tes amis le soir.")}</p>
      <p>{T("Les jeux puisent dans les mêmes univers que nos quiz : {a} personnages, {b} pouvoirs décrits sans les nommer, {c} univers résumés en cinq indices et {d} mots du vocabulaire des animés, des séries et des jeux vidéo, chacun accompagné de sa définition. Une fois l'énigme trouvée, tu peux enchaîner sur le quiz complet de la série pour vérifier que tu la connais vraiment.", a=n_chars, b=n_pow, c=n_univ, d=len(D.MOTS))}</p>
      <h2 class="h2" style="margin-top:32px">{T('Ta série de victoires')}</h2>
      <p>{T("Chaque jeu garde ta série de jours gagnés d'affilée et ton record. Ces statistiques restent sur ton appareil : pas de compte, pas d'inscription. Si tu changes de navigateur, tu repars de zéro.")}</p>
    </article>
    <article class="prose">
      <h2 class="h2">{T('Sans spoiler majeur')}</h2>
      <p>{T("Les indices s'en tiennent à ce qu'on apprend dans les premiers arcs de chaque œuvre. Les grandes révélations, l'identité cachée d'un personnage ou la fin d'une série ne servent jamais d'indice.")}</p>
      <h2 class="h2" style="margin-top:32px">{T('Partager sans rien dévoiler')}</h2>
      <p>{T("À la fin de chaque partie, le bouton « Partager » copie une grille de carrés colorés qui montre ton parcours sans révéler la réponse. Colle-la sur Discord, X ou dans ton groupe de discussion.")}</p>
      <h2 class="h2" style="margin-top:32px">{T('Encore envie de jouer ?')}</h2>
      <p>{letsdle}</p>
    </article>
  </div>
</div>
'''
    ld = [crumbs_ld(crumbs)]
    write('/dle/', head(T("Kamidle — devine le personnage, le pouvoir et l'univers du jour | KamiQuiz"),
                        T("Cinq jeux du jour gratuits sur les animés, séries, films et jeux vidéo : devine le personnage, le pouvoir, les emojis, l'univers et le mot du jour. {n} personnages, sans inscription.", n=n_chars),
                        '/dle/', ld) + header('/dle/') + body + footer(scripts))
    page('/dle/', '0.9', 'daily')

    # ----- une page par jeu
    legend_styles = ''.join(f'<li><b>{e(k)}</b> : {e(v)}</li>' for k, v in D.STYLE_HELP.items())
    for m, label, ico, desc in DLE_MODES:
        h1, rules = DLE_INFO[m]
        crumbs = [(T('Accueil'), '/'), ('Kamidle', '/dle/'), (label, f'/dle/{m}/')]
        legend = ''
        if m == 'personnage':
            years = ', '.join(f'{e(BY_KEY[k]["name"])} {y}' + (f' ({D.YEAR_NOTES[k]})' if k in D.YEAR_NOTES else '')
                              for k, y in sorted(DLE.YEARS.items(), key=lambda kv: (kv[1], kv[0])) if k in BY_KEY)
            legend = f'''<h2 class="h2">{T('Lire les indices')}</h2>
      <p>{T("<span class=\"dle-sw ok\"></span> Vert : identique à la cible. <span class=\"dle-sw near\"></span> Jaune : en partie juste (une espèce, un style ou une couleur de cheveux en commun, ou une couleur proche comme noir et brun). <span class=\"dle-sw no\"></span> Rouge : aucun point commun. Pour l'âge et l'année, la flèche indique si la cible est plus âgée (↑) ou plus jeune (↓), plus récente (↑) ou plus ancienne (↓).")}</p>
      <p>{T("Le <b>rôle</b> décrit la place du personnage dans l'histoire : protagoniste, allié, rival, mentor, antagoniste ou neutre. Le <b>style</b> décrit sa façon principale de combattre :")}</p>
      <ul class="dle-legend">{legend_styles}</ul>
      <p>{T("L'<b>âge</b> est l'âge réel du personnage pendant l'essentiel de l'histoire, pas son apparence : enfant (12 ans ou moins), ado (13 à 19 ans), adulte (20 à 59 ans), âgé (60 ans et plus) ou sans âge (immortels, espèces à très longue vie, créatures et animaux). Les <b>cheveux</b> sont ceux de son look le plus connu ; « aucun » veut dire chauve, casqué, ou couvert de fourrure.")}</p>
      <p>{T("L'<b>année</b> est celle du début de l'œuvre originale : premier tome, premier épisode, premier film ou premier jeu. {years}.", years=years)}</p>'''
        elif m == 'mot':
            legend = f'''<h2 class="h2">{T('Règles')}</h2>
      <p>{T("Le mot du jour compte entre cinq et huit lettres, sans accent. Tape un mot de la bonne longueur au clavier ou avec les touches à l'écran, puis valide. <span class=\"dle-sw ok\"></span> Vert : la lettre est à la bonne place. <span class=\"dle-sw near\"></span> Jaune : la lettre est dans le mot, mais ailleurs. <span class=\"dle-sw no\"></span> Gris : la lettre n'y est pas.")}</p>
      <p>{T("Les essais doivent être de vrais mots français, ou des termes de l'univers des animés et des jeux vidéo. Le mot à trouver vient toujours de cet univers, et sa définition s'affiche à la fin de la partie.")}</p>'''
        others = ''.join(f'<a class="chip" href="{U("/dle/" + m2 + "/")}">{i2} {l2}</a>' for m2, l2, i2, _ in DLE_MODES if m2 != m)
        default_rules = T("<h2 class=\"h2\">Règles</h2><p>{rules}</p><p>Les réponses viennent des univers de nos quiz. Tape les premières lettres d'un nom pour voir les propositions, puis choisis dans la liste.</p>", rules=e(rules))
        body = f'''<div class="wrap">
  <div class="page-head">
    {crumbs_html(crumbs)}
    <h1 class="h1">{e(h1)}</h1>
    <p class="lede">{e(rules)}</p>
  </div>
  <section class="dle" id="dle" data-mode="{m}" aria-live="polite">
    <p class="loading">{T("Chargement de l'énigme du jour…")}</p>
  </section>
  <p class="dle-yesterday" data-dle-yesterday></p>
  <div class="two-col" style="margin-top:48px">
    <article class="prose">{legend or default_rules}</article>
    <aside class="prose">
      <h2 class="h2">{T('Les autres jeux du jour')}</h2>
      <div class="chips" style="margin-top:12px">{others}</div>
      <p class="muted" style="margin-top:20px">{T('Une nouvelle énigme arrive chaque jour à minuit. Tes séries de victoires sont enregistrées sur ton appareil.')}</p>
    </aside>
  </div>
</div>
'''
        write(f'/dle/{m}/', head(T('{h1} — Kamidle | KamiQuiz', h1=h1), T('{rules} Jeu gratuit, une énigme par jour.', rules=rules),
                                 f'/dle/{m}/', [crumbs_ld(crumbs)]) + header('/dle/') + body + footer(scripts))
        page(f'/dle/{m}/', '0.8', 'daily')


# --------------------------------------------------------------------------- guides
def build_guides():
    if not GUIDES:
        return
    items = ''.join(f'<li><a href="{U("/guides/" + g["slug"] + "/")}"><span class="gt">{e(g["title"])}</span><span class="gd">{e(g["description"])}</span></a></li>'
                    for g in GUIDES)
    crumbs = [(T('Accueil'), '/'), (T('Guides'), '/guides/')]
    ld = [crumbs_ld(crumbs)]
    body = f'''<div class="wrap">
  <div class="page-head prose">
    {crumbs_html(crumbs)}
    <h1 class="h1">{T('Guides et dossiers')}</h1>
    <p class="lede">{T("Des articles pour comprendre les univers des quiz, réviser les points qui font trébucher et mieux retenir ce que l'on apprend en jouant.")}</p>
  </div>
  <ul class="guide-list prose" style="margin-top:24px">{items}</ul>
</div>
'''
    write('/guides/', head(T('Guides et dossiers sur les animés, séries et jeux — KamiQuiz'),
                           T("Dossiers originaux pour réviser avant de jouer : les Fruits du Démon, les maisons de Poudlard, les Piliers de Demon Slayer, la table des types Pokémon et bien d'autres."),
                           '/guides/', ld) + header('/guides/') + body + footer())
    page('/guides/', '0.7', 'weekly')

    play = U('/jouer/')
    for g in GUIDES:
        path = f'/guides/{g["slug"]}/'
        crumbs = [(T('Accueil'), '/'), (T('Guides'), '/guides/'), (g['title'], path)]
        s = BY_KEY.get(g.get('serie') or '')
        accent = s['color'] if s else None
        cta = ''
        if s:
            name = e(s['name'])
            cta = (f'<div class="callout" style="margin-top:48px"><h2 class="h2">{T("Testez-vous sur {name}", name=name)}</h2>'
                   f'<p class="muted">{T("{n} questions expliquées vous attendent, de la plus simple à la plus pointue.", n=s["n"])}</p>'
                   f'<div class="btn-row"><a class="btn btn-gold" href="{play}?s={s["key"]}&amp;m=libre">{T("Jouer au quiz {name}", name=name)}</a>'
                   f'<a class="btn" href="{U("/quiz/" + s["slug"] + "/")}#questions">{T("Réviser les réponses")}</a></div></div>')
        else:
            cta = (f'<div class="callout" style="margin-top:48px"><h2 class="h2">{T("À vous de jouer")}</h2>'
                   f'<p class="muted">{T("Choisissez un univers et appliquez la méthode dès maintenant.")}</p>'
                   f'<div class="btn-row"><a class="btn btn-gold" href="{U("/quiz/")}">{T("Choisir un quiz")}</a></div></div>')
        others = ''.join(f'<li><a href="{U("/guides/" + o["slug"] + "/")}"><span class="gt">{e(o["title"])}</span></a></li>'
                         for o in GUIDES if o['slug'] != g['slug'])[:4000]
        ld = [crumbs_ld(crumbs), {
            '@context': 'https://schema.org', '@type': 'Article', 'headline': g['title'], 'description': g['description'],
            'datePublished': g['date'], 'dateModified': g['date'], 'inLanguage': i18n.LANG, 'mainEntityOfPage': SITE + U(path),
            'image': SITE + '/assets/img/og-image.png',
            'author': {'@type': 'Organization', 'name': T('La rédaction de KamiQuiz'), 'url': SITE + U('/a-propos/')},
            'publisher': {'@type': 'Organization', 'name': 'KamiQuiz', 'logo': {'@type': 'ImageObject', 'url': SITE + '/assets/img/icon-512.png'}}}]
        minutes = max(3, round(g['words'] / 220))
        meta = T('Par la rédaction de KamiQuiz, publié le {d}. Lecture : {m} minutes.', d=loc_date(g['date']), m=minutes)
        body = f'''<div class="wrap">
  <div class="page-head prose">
    {crumbs_html(crumbs)}
    <h1 class="h1" style="font-size:clamp(2.2rem,5vw,3.6rem)">{e(g["title"])}</h1>
    <p class="lede">{e(g["description"])}</p>
    <p class="meta">{meta}</p>
  </div>
  <article class="article prose" style="margin-top:32px">
    {g["html"]}
    {cta}
  </article>
  <section class="prose" style="margin-top:56px"><h2 class="h2">{T('Autres guides')}</h2><ul class="guide-list">{others}</ul></section>
</div>
'''
        write(path, head(f'{g["title"]} — KamiQuiz', g['description'], path, ld, og_type='article', accent=accent)
              + header('/guides/') + body + footer())
        page(path, '0.7', 'monthly', g['date'])


# --------------------------------------------------------------------------- pages simples
def simple(path, title, desc, h1, lede, inner, current='', prio='0.4', **kw):
    title, desc, h1, lede, inner = T(title), T(desc), T(h1), T(lede) if lede else lede, T(inner, **kw)
    crumbs = [(T('Accueil'), '/'), (h1, path)]
    body = f'''<div class="wrap">
  <div class="page-head prose">
    {crumbs_html(crumbs)}
    <h1 class="h1">{e(h1)}</h1>
    {f'<p class="lede">{lede}</p>' if lede else ''}
  </div>
  <article class="article prose" style="margin-top:32px">{inner}</article>
</div>
'''
    write(path, head(title, desc, path, [crumbs_ld(crumbs)]) + header(current) + body + footer())
    page(path, prio, 'yearly', BASE_DATE)


def build_static_pages():
    nb = {cid: sum(1 for s in SERIES if s['cat'] == cid) for cid, _, _ in CATEGORIES}
    simple('/a-propos/', 'À propos de KamiQuiz', 'KamiQuiz est un site de quiz gratuit et indépendant consacré aux animés, séries, films, jeux vidéo et à la culture générale. Notre démarche et nos engagements.',
           'À propos de KamiQuiz', 'Un site de quiz francophone, gratuit et indépendant, où chaque réponse est expliquée.', '''
<h2>Ce qu'est KamiQuiz</h2>
<p>KamiQuiz rassemble {total} questions réparties sur {ns} univers : {anime} animés et mangas, {series} séries télévisées, {films} grandes sagas du cinéma, {jeux} jeux vidéo et {culture} quiz de culture générale. Le site est gratuit, sans inscription et fonctionne aussi bien sur téléphone que sur ordinateur.</p>
<p>Le nom vient du japonais <em>kami</em>, que l'on retrouve dans de nombreux animés pour désigner une divinité. Atteindre le rang de Kami, c'est connaître un univers sur le bout des doigts.</p>
<h2>Notre démarche</h2>
<p>Nous pensons qu'un quiz réussi doit faire apprendre quelque chose, même quand on se trompe. C'est pourquoi :</p>
<ul>
<li><strong>chaque question est accompagnée d'une explication</strong>, affichée juste après la réponse ;</li>
<li><strong>chaque univers a une page de révision</strong> qui présente toutes ses questions, classées par thème, avec leurs réponses ;</li>
<li><strong>le jeu privilégie les questions que vous n'avez pas encore vues</strong>, pour que chaque partie apporte du neuf ;</li>
<li><strong>nos guides</strong> approfondissent les sujets qui reviennent le plus souvent dans les questions difficiles.</li>
</ul>
<h2>Comment les questions sont écrites</h2>
<p>Les questions sont rédigées à partir des œuvres elles-mêmes (mangas, séries, films, jeux) et de sources de référence pour les quiz de culture générale. Chacune est classée par thème et par niveau, de Facile à Expert, et relue avant publication. La banque est régulièrement nettoyée : doublons retirés, formulations ambiguës corrigées, terminologie harmonisée.</p>
<p>Malgré ce soin, une erreur peut nous échapper, surtout sur des séries encore en cours. Si vous en repérez une, écrivez-nous à <a href="mailto:contact@kamiquiz.com">contact@kamiquiz.com</a> en précisant la question concernée : nous corrigeons rapidement.</p>
<h2>Indépendance et financement</h2>
<p>KamiQuiz est un projet indépendant, sans lien avec les éditeurs, studios ou ayants droit des œuvres citées. Les noms des séries, personnages et jeux appartiennent à leurs propriétaires respectifs et sont utilisés uniquement pour désigner les œuvres dont parlent les questions.</p>
<p>Le site est financé par de la publicité diffusée par Google AdSense. Elle nous permet de garder tous les quiz gratuits et sans compte. Les détails sur les cookies et vos choix sont expliqués dans notre <a href="/confidentialite/">politique de confidentialité</a>.</p>
<h2>Nous écrire</h2>
<p>Une erreur à signaler, un univers à proposer, une idée d'amélioration ? Toutes les façons de nous joindre sont sur la <a href="/contact/">page contact</a>.</p>
''', '/a-propos/', '0.5', total=fr_num(TOTAL_Q), ns=NB_SERIES, **nb)

    simple('/contact/', 'Contact — KamiQuiz', 'Contactez KamiQuiz pour signaler une erreur dans une question, proposer un nouvel univers ou poser une question sur le site.',
           'Contact', 'Une erreur, une idée, une question : nous lisons tous les messages.', '''
<h2>Par e-mail</h2>
<p>Écrivez-nous à <a href="mailto:contact@kamiquiz.com">contact@kamiquiz.com</a>. Nous répondons généralement sous quelques jours.</p>
<h2>Signaler une erreur dans une question</h2>
<p>Pour que nous puissions corriger vite, indiquez dans votre message :</p>
<ul>
<li>le nom du quiz (par exemple « Naruto ») ;</li>
<li>le texte de la question, ou son début ;</li>
<li>ce qui vous semble faux, et si possible une source (chapitre, épisode, page officielle).</li>
</ul>
<h2>Proposer un univers</h2>
<p>Les nouveaux quiz sont choisis en fonction des demandes des joueurs. Dites-nous quelle série, quel film ou quel jeu vous aimeriez voir arriver sur KamiQuiz.</p>
<h2>Données personnelles</h2>
<p>Pour toute demande liée à vos données, notamment la suppression d'un pseudo du classement mondial, utilisez la même adresse en précisant le pseudo concerné. Les détails figurent dans la <a href="/confidentialite/">politique de confidentialité</a>.</p>
''', '', '0.4')

    simple('/confidentialite/', 'Politique de confidentialité et cookies — KamiQuiz',
           'Quelles données KamiQuiz collecte, comment fonctionne la publicité Google AdSense, la gestion du consentement et vos droits.',
           'Confidentialité et cookies', 'Dernière mise à jour : 31 octobre 2026.', '''
<h2>Qui sommes-nous</h2>
<p>KamiQuiz (kamiquiz.com) est un site de quiz gratuit et indépendant. Pour toute question sur cette politique, écrivez à <a href="mailto:contact@kamiquiz.com">contact@kamiquiz.com</a>.</p>
<h2>Ce que nous collectons</h2>
<p><strong>Rien qui vous identifie directement.</strong> Il n'y a ni compte ni inscription sur KamiQuiz. Concrètement :</p>
<ul>
<li><strong>Données enregistrées sur votre appareil.</strong> Votre progression (questions déjà vues, réponse à la question du jour) et le dernier pseudo utilisé sont stockés dans le navigateur, grâce au stockage local. Ils ne nous sont pas transmis. Vous pouvez les effacer à tout moment depuis les réglages de votre navigateur.</li>
<li><strong>Classement mondial.</strong> Si vous choisissez d'enregistrer un score, nous recevons le pseudo que vous saisissez, votre score, le quiz, le mode de jeu et la date. Ces informations sont publiques dans le classement. N'utilisez pas votre vrai nom si vous ne souhaitez pas qu'il apparaisse.</li>
<li><strong>Données techniques.</strong> Comme tout site, notre hébergeur Cloudflare traite les adresses IP et des informations techniques pour acheminer les pages et protéger le site contre les abus.</li>
</ul>
<h2>Publicité et cookies</h2>
<p>KamiQuiz est financé par la publicité diffusée par <strong>Google AdSense</strong>. Google et ses partenaires peuvent utiliser des cookies et des identifiants pour afficher des annonces, mesurer leur efficacité et, si vous l'acceptez, les personnaliser en fonction de vos visites sur ce site et sur d'autres sites.</p>
<p>Si vous vous trouvez dans l'Espace économique européen, au Royaume-Uni ou en Suisse, un message de consentement géré par Google, plateforme certifiée dans le cadre du Transparency and Consent Framework de l'IAB, vous est présenté lors de votre première visite. Vous pouvez y accepter, refuser ou paramétrer l'usage de vos données. Sans votre accord, seules des annonces non personnalisées peuvent être affichées.</p>
<p><button class="btn btn-sm" type="button" data-privacy-choices>Modifier mes choix de confidentialité</button></p>
<p>Pour en savoir plus sur la façon dont Google utilise les données, consultez la page <a href="https://policies.google.com/technologies/partner-sites" rel="noopener" target="_blank">Comment Google utilise les informations des sites qui utilisent ses services</a>. Vous pouvez aussi gérer la personnalisation des annonces sur <a href="https://myadcenter.google.com/" rel="noopener" target="_blank">Mon Centre de publicités</a>.</p>
<h2>Polices et ressources</h2>
<p>Les polices de caractères, les scripts et les visuels du site sont hébergés sur nos propres serveurs : votre navigateur ne contacte aucun service tiers pour les charger, en dehors de Google AdSense.</p>
<h2>Bandes-annonces YouTube</h2>
<p>Certaines pages de quiz proposent la bande-annonce officielle de l'œuvre. Tant que vous ne cliquez pas sur le bouton de lecture, rien n'est chargé depuis YouTube : vous voyez seulement une image hébergée chez nous. Si vous lancez la vidéo, elle est lue dans un lecteur YouTube en mode de confidentialité renforcée (youtube-nocookie.com) ; Google peut alors traiter des données de lecture selon sa propre <a href="https://policies.google.com/privacy" rel="noopener" target="_blank">politique de confidentialité</a>.</p>
<h2>Durée de conservation</h2>
<p>Les scores du classement mondial sont conservés tant que le classement existe, sauf demande de suppression. Les données techniques de l'hébergeur sont conservées pour une durée limitée, selon sa propre politique.</p>
<h2>Vos droits</h2>
<p>Selon votre lieu de résidence (notamment au titre du RGPD en Europe et de la Loi 25 au Québec), vous disposez d'un droit d'accès, de rectification, de suppression et d'opposition. Pour supprimer un score du classement ou exercer ces droits, écrivez à <a href="mailto:contact@kamiquiz.com">contact@kamiquiz.com</a> en précisant le pseudo concerné.</p>
<h2>Prestataires</h2>
<ul>
<li><a href="https://www.cloudflare.com/privacypolicy/" rel="noopener" target="_blank">Cloudflare</a> : hébergement, distribution des pages et classement mondial.</li>
<li><a href="https://policies.google.com/privacy" rel="noopener" target="_blank">Google</a> : publicité (AdSense), gestion du consentement et lecture des bandes-annonces YouTube, uniquement si vous les lancez.</li>
</ul>
<h2>Modifications</h2>
<p>Cette politique peut évoluer. La date de dernière mise à jour figure en haut de la page.</p>
''', '', '0.3')

    simple('/conditions/', "Conditions d'utilisation — KamiQuiz", "Les conditions d'utilisation du site KamiQuiz : usage du service, classement mondial, propriété intellectuelle.",
           "Conditions d'utilisation", 'Dernière mise à jour : 31 octobre 2026.', '''
<h2>Le service</h2>
<p>KamiQuiz propose gratuitement des quiz en ligne. Le site est fourni tel quel : nous faisons notre possible pour que les questions soient exactes et le service disponible, sans pouvoir le garantir en permanence.</p>
<h2>Classement mondial</h2>
<p>En enregistrant un score, vous acceptez que votre pseudo apparaisse publiquement. Les pseudos injurieux, discriminatoires, à caractère publicitaire ou reprenant l'identité d'une autre personne sont interdits et peuvent être supprimés sans préavis, tout comme les scores obtenus de manière automatisée ou frauduleuse.</p>
<h2>Propriété intellectuelle</h2>
<p>Les textes, questions, explications et guides de KamiQuiz sont protégés. Vous pouvez partager librement les liens vers le site et vos résultats ; la reproduction massive des questions ou des guides sur un autre site n'est pas autorisée sans accord écrit.</p>
<p>Les visuels des pages de quiz sont des illustrations originales créées pour KamiQuiz. Les bandes-annonces appartiennent à leurs ayants droit : elles sont intégrées avec le lecteur officiel de YouTube, depuis la chaîne du diffuseur ou de l'éditeur.</p>
<p>KamiQuiz n'est affilié à aucun des éditeurs, studios ou ayants droit des œuvres évoquées. Les marques et noms cités appartiennent à leurs propriétaires et sont utilisés à titre de référence.</p>
<h2>Contact</h2>
<p>Pour toute question sur ces conditions : <a href="mailto:contact@kamiquiz.com">contact@kamiquiz.com</a>.</p>
''', '', '0.2')

    # 404 (Cloudflare Pages sert dist/404.html pour toute URL inconnue, avec un vrai code 404)
    rows = ''.join(series_row(BY_KEY[k]) for k in POPULAR if k in BY_KEY)
    body = f'''<div class="wrap notfound">
  <p class="display">404</p>
  <h1 class="h2" style="margin-top:12px">{T("Cette page n'existe pas")}</h1>
  <p class="muted">{T('Le lien est peut-être ancien. Tous les quiz sont toujours là.')}</p>
  <div class="btn-row" style="justify-content:center;margin-top:20px"><a class="btn btn-gold" href="{U('/quiz/')}">{T('Voir tous les quiz')}</a><a class="btn" href="{U('/')}">{T('Accueil')}</a></div>
</div>
<div class="wrap" style="max-width:760px"><ul class="series-list" style="grid-template-columns:1fr">{rows}</ul></div>
'''
    out404 = DIST / '404.html' if i18n.LANG == 'fr' else DIST / i18n.LANG / '404.html'
    out404.parent.mkdir(parents=True, exist_ok=True)
    out404.write_text(head(T('Page introuvable — KamiQuiz'), T("Cette page n'existe pas."), '/404', robots='noindex')
                      + header() + body + footer(), encoding='utf-8')


# --------------------------------------------------------------------------- données et fichiers techniques
def build_data():
    out = DIST / 'data' if i18n.LANG == 'fr' else DIST / 'data' / i18n.LANG
    out.mkdir(parents=True, exist_ok=True)
    for s in SERIES:
        d = s['data']
        (out / f'{s["key"]}.json').write_text(json.dumps(
            {'name': s['name'], 'color': d['color'], 'ranks': d['ranks'], 'cats': d['cats'], 'q': d['q']},
            ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    allq = []
    for s in SERIES:
        for q in s['data']['q']:
            allq.append({**q, 'cat': s['name'], 's': s['key']})
    (out / 'all.json').write_text(json.dumps({
        'name': T('Tout mélanger'), 'color': '#d4a843', 'ranks': [],
        'cats': {s['name']: {'i': ''} for s in SERIES}, 'q': allq}, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')


def build_tech():
    def alts(p):
        langs = [l for l in i18n.LANGS if p in AVAIL.get(l, ())]
        if len(langs) < 2:
            return ''
        return ''.join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{SITE}{U(p, l)}"/>' for l in langs) + \
            f'<xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{p}"/>'
    urls = ''.join(f'<url><loc>{SITE}{U(p, l)}</loc>{alts(p)}<lastmod>{lm}</lastmod><changefreq>{f}</changefreq><priority>{pr}</priority></url>\n'
                   for l, p, pr, f, lm in PAGES)
    ns = ' xmlns:xhtml="http://www.w3.org/1999/xhtml"' if len(AVAIL) > 1 else ''
    (DIST / 'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"{ns}>\n'
                                      + urls + '</urlset>\n', encoding='utf-8')
    (DIST / 'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n', encoding='utf-8')
    (DIST / 'ads.txt').write_text('google.com, pub-6970710961658841, DIRECT, f08c47fec0942fa0\n', encoding='utf-8')

    # Redirections 301 depuis l'ancienne structure (Cloudflare Pages lit _redirects)
    red = ['# Anciennes URLs -> nouvelle structure',
           '/quiz.html /quiz/ 301', '/about.html /a-propos/ 301', '/about /a-propos/ 301',
           '/privacy.html /confidentialite/ 301', '/privacy /confidentialite/ 301', '/questions.json /data/all.json 301']
    for s in SERIES:
        for old in (f'/{s["key"]}.html', f'/{s["key"]}', f'/quiz/{s["key"]}.html'):
            red.append(f'{old} /quiz/{s["slug"]}/ 301')
        if s['key'] != s['slug']:
            red.append(f'/quiz/{s["key"]}/ /quiz/{s["slug"]}/ 301')
    (DIST / '_redirects').write_text('\n'.join(red) + '\n', encoding='utf-8')

    (DIST / '_headers').write_text('''/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: SAMEORIGIN
  Permissions-Policy: camera=(), microphone=(), geolocation=()

/assets/*
  Cache-Control: public, max-age=31536000, immutable

/data/*
  Cache-Control: public, max-age=3600

/sw.js
  Cache-Control: no-cache
''', encoding='utf-8')

    (DIST / 'manifest.webmanifest').write_text(json.dumps({
        'name': 'KamiQuiz', 'short_name': 'KamiQuiz', 'lang': 'fr', 'start_url': '/', 'scope': '/',
        'display': 'standalone', 'background_color': '#07080f', 'theme_color': '#07080f',
        'description': 'Quiz gratuits sur les animés, séries, films, jeux vidéo et la culture générale.',
        'icons': [{'src': '/assets/img/icon-192.png', 'sizes': '192x192', 'type': 'image/png'},
                  {'src': '/assets/img/icon-512.png', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'any maskable'}]},
        ensure_ascii=False, indent=1), encoding='utf-8')

    (DIST / 'favicon.svg').write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="7" fill="#07080f"/>'
        '<circle cx="16" cy="16" r="11.5" fill="none" stroke="#d4a843" stroke-width="2.2"/><circle cx="16" cy="16" r="4.2" fill="#d4a843"/></svg>\n',
        encoding='utf-8')

    import hashlib
    sw_v = hashlib.sha256(''.join(asset(x) for x in ('/assets/css/site.css', '/assets/css/fonts.css', '/assets/js/site.js',
                                                     '/assets/js/quiz.js', '/assets/js/dle.js')).encode()).hexdigest()[:10]
    (DIST / 'sw.js').write_text(f'''// KamiQuiz — service worker v{sw_v}
// Réseau d'abord pour les pages et les données (toujours à jour), cache en secours hors ligne.
const CACHE = 'kamiquiz-{sw_v}';
const CORE = ['/', '/quiz/', '/jouer/', '/dle/', '{asset('/assets/css/site.css')}', '{asset('/assets/css/fonts.css')}',
  '{asset('/assets/js/site.js')}', '{asset('/assets/js/quiz.js')}', '{asset('/assets/js/dle.js')}', '/favicon.svg'];

self.addEventListener('install', e => {{
  e.waitUntil(caches.open(CACHE).then(c => Promise.all(CORE.map(u => c.add(u).catch(() => {{}})))).then(() => self.skipWaiting()));
}});
self.addEventListener('activate', e => {{
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
}});
self.addEventListener('fetch', e => {{
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;            // AdSense, classement : jamais interceptés
  const isAsset = url.pathname.startsWith('/assets/');
  if (isAsset) {{
    e.respondWith(caches.match(req).then(hit => hit || fetch(req).then(res => {{
      if (res.ok) {{ const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); }}
      return res;
    }})));
    return;
  }}
  e.respondWith(fetch(req).then(res => {{
    if (res.ok) {{ const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); }}
    return res;
  }}).catch(() => caches.match(req).then(hit => hit || caches.match('/'))));
}});
''', encoding='utf-8')


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(ROOT / 'static', DIST)
    # Pages disponibles dans chaque langue (pour hreflang et le sélecteur de langue)
    for lang in i18n.LANGS:
        setup(lang)
        av = {'/', '/quiz/', '/jouer/', '/a-propos/', '/contact/', '/confidentialite/', '/conditions/'}
        av |= {f'/quiz/{s["slug"]}/' for s in SERIES}
        if GUIDES:
            av |= {'/guides/'} | {f'/guides/{g["slug"]}/' for g in GUIDES}
        if dle_ready():
            av |= {'/dle/'} | {f'/dle/{m}/' for m, *_ in DLE.MODES}
        AVAIL[lang] = av
    report = []
    for lang in i18n.LANGS:
        setup(lang)
        build_data()
        build_home()
        build_index()
        for s in SERIES:
            build_serie(s)
        build_play()
        build_guides()
        build_static_pages()
        if dle_ready():
            build_dle()
        part = sum(s['n'] for s in SERIES)
        report.append(f'{lang} : {NB_SERIES} séries, {fr_num(part)} questions, {len(GUIDES)} guides')
    setup('fr')
    if i18n.MISSING:
        (ROOT / 'data' / 'i18n_missing.json').write_text(json.dumps({i18n.qid(m): m for m in sorted(i18n.MISSING)}, ensure_ascii=False, indent=1), encoding='utf-8')
        raise SystemExit(f'{len(i18n.MISSING)} textes sans traduction : liste dans data/i18n_missing.json')
    (ROOT / 'data' / 'i18n_missing.json').unlink(missing_ok=True)
    build_tech()
    n_html = len(list(DIST.rglob('*.html')))
    print(f'[{TODAY}] Site généré : {n_html} pages HTML, {len(PAGES)} URLs dans le sitemap ({" ; ".join(report)})')


if __name__ == '__main__':
    main()
