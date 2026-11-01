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
from series import SERIES as ALL_SERIES, CATEGORIES, POPULAR, NEW_FALLBACK  # noqa: E402
import dle as DLE  # noqa: E402
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
MONTHS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']


def fr_date(iso):
    d = datetime.date.fromisoformat(iso)
    return f'{"1er" if d.day == 1 else d.day} {MONTHS[d.month - 1]} {d.year}'


for _s in ALL_SERIES:
    _s.setdefault('date', BASE_DATE)
SERIES = [s for s in ALL_SERIES if s['date'] <= TODAY]

DB = json.loads((ROOT / 'data' / 'questions.json').read_text(encoding='utf-8'))
BY_KEY = {s['key']: s for s in SERIES}
assert set(BY_KEY) <= set(DB), set(BY_KEY) - set(DB)
for s in SERIES:
    s['data'] = DB[s['key']]
    s['n'] = len(DB[s['key']]['q'])
    s['color'] = DB[s['key']]['color']
TOTAL_Q = sum(s['n'] for s in SERIES)
NB_SERIES = len(SERIES)
CAT_NAME = {c[0]: c[1] for c in CATEGORIES}
LEVELS = {1: 'Facile', 2: 'Moyen', 3: 'Difficile', 4: 'Expert'}

MODES = [
    ('libre', '🎲', 'Mode libre', "20 questions au hasard, sans chrono. Idéal pour découvrir."),
    ('chrono', '⚡', 'Contre la montre', "15 secondes par question et un multiplicateur de points pour les plus rapides."),
    ('survie', '🛡️', 'Survie', "Trois vies. Chaque erreur en coûte une. Jusqu'où tiendrez-vous ?"),
    ('maitre', '⭐', 'Ascension', "30 questions de plus en plus dures, avec bonus de série."),
    ('expert', '💀', 'Expert', "Uniquement les questions difficiles."),
    ('categorie', '📚', 'Par thème', "Choisissez les thèmes sur lesquels vous entraîner."),
]

e = html.escape


def fr_num(n):
    return f'{n:,}'.replace(',', '\u00a0')


def plural(n, one, many):
    return f'{fr_num(n)} {one if n < 2 else many}'


# --------------------------------------------------------------------------- gabarit
LOGO = ('<svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="16" r="14.5" fill="none" stroke="#d4a843" stroke-width="2"/>'
        '<circle cx="16" cy="16" r="8.5" fill="none" stroke="#d4a843" stroke-width="1.2" opacity=".55"/>'
        '<circle cx="16" cy="16" r="3.6" fill="#d4a843"/></svg>')


def head(title, desc, path, jsonld=None, robots='index, follow', og_type='website', accent=None):
    canonical = SITE + path
    ld = ''
    for block in (jsonld or []):
        ld += '<script type="application/ld+json">' + json.dumps(block, ensure_ascii=False, separators=(',', ':')) + '</script>\n'
    style = f'<style>:root{{--accent:{accent}}}</style>\n' if accent else ''
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#07080f">
<meta name="google-adsense-account" content="{PUB}">
<meta name="alldle-verify" content="zeH2tpvyQl3QIQMFda8JTGnZePXWWPus">
<meta property="og:site_name" content="KamiQuiz">
<meta property="og:locale" content="fr_FR">
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
<a class="skip" href="#contenu">Aller au contenu</a>
'''


CUR = ' aria-current="page"'
LETSDLE = 'https://letsdle.com/'
LETSDLE_NAV = (f'<a class="nav-ext" href="{LETSDLE}" target="_blank" rel="noopener" '
               'title="Letsdle, d\'autres petits jeux quotidiens (nouvel onglet)">Plus de jeux<span aria-hidden="true"> ↗</span></a>')
OK_CLS = ' class="ok"'
NAV = [('/quiz/', 'Tous les quiz'), ('/dle/', 'Kamidle'), ('/guides/', 'Guides'), ('/a-propos/', 'À propos')]


def header(current=''):
    links = ''.join(
        f'<a href="{href}"{CUR if current == href else ""}>{label}</a>' for href, label in NAV)
    return f'''<header class="site-head">
  <div class="wrap">
    <a class="brand" href="/" aria-label="KamiQuiz, accueil">{LOGO}<span>KAMI<b>QUIZ</b></span></a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Navigation principale">{links}{LETSDLE_NAV}<a class="nav-cta" href="/jouer/">Jouer</a></nav>
  </div>
</header>
<main id="contenu">
'''


def footer(scripts=('/assets/js/site.js',)):
    cats = ''.join(f'<li><a href="/quiz/#{cid}">{name}</a></li>' for cid, name, _ in CATEGORIES)
    js = ''.join(f'<script src="{asset(s)}" defer></script>\n' for s in scripts)
    return f'''</main>
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="brand" href="/">{LOGO}<span>KAMI<b>QUIZ</b></span></a>
        <p style="margin-top:14px;max-width:34ch">Des quiz gratuits sur les animés, les séries, les films, les jeux vidéo et la culture générale. Sans inscription.</p>
      </div>
      <div><h2>Quiz</h2><ul>{cats}</ul></div>
      <div><h2>KamiQuiz</h2><ul><li><a href="/dle/">Kamidle, jeux du jour</a></li><li><a href="/guides/">Guides</a></li><li><a href="/a-propos/">À propos</a></li><li><a href="/contact/">Contact</a></li><li><a href="/jouer/">Quiz tout mélangé</a></li><li><a href="{LETSDLE}" target="_blank" rel="noopener">Plus de jeux sur Letsdle ↗</a></li></ul></div>
      <div><h2>Informations</h2><ul><li><a href="/confidentialite/">Confidentialité et cookies</a></li><li><a href="/conditions/">Conditions d'utilisation</a></li><li><a href="/sitemap.xml">Plan du site</a></li></ul></div>
    </div>
    <p class="foot-note">© 2026 KamiQuiz. KamiQuiz est un site indépendant, sans lien avec les ayants droit des œuvres citées. Les noms des œuvres appartiennent à leurs propriétaires respectifs.</p>
  </div>
</footer>
{js}<script>if('serviceWorker' in navigator){{addEventListener('load',function(){{navigator.serviceWorker.register('/sw.js').catch(function(){{}})}})}}</script>
</body>
</html>
'''


def write(path, content):
    out = DIST / path.lstrip('/')
    if path.endswith('/'):
        out = out / 'index.html'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding='utf-8')


PAGES = []  # (path, priority, changefreq) pour le sitemap


def page(path, prio='0.6', freq='monthly', lastmod=None):
    PAGES.append((path, prio, freq, lastmod or TODAY))


def crumbs_ld(items):
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': SITE + p} for i, (n, p) in enumerate(items)]}


def crumbs_html(items):
    lis = ''.join(f'<li><a href="{p}">{e(n)}</a></li>' if i < len(items) - 1 else f'<li aria-current="page">{e(n)}</li>'
                  for i, (n, p) in enumerate(items))
    return f'<nav class="crumbs" aria-label="Fil d\'Ariane"><ol>{lis}</ol></nav>'


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
    return (f'<li class="series-row"><a href="/quiz/{s["slug"]}/" style="--c:{s["color"]}">'
            f'<span class="thumb">{art_img(s, "thumb-art")}</span>'
            f'<span><span class="nm">{e(s["name"])}</span><span class="ds">{e(s["tag"])}</span></span>'
            f'<span class="ct">{s["n"]} questions</span></a></li>')


def tile(s, badge='', big=False):
    b = f'<span class="badge">{e(badge)}</span>' if badge else ''
    return (f'<a class="tile{" tile-lg" if big else ""}" href="/quiz/{s["slug"]}/" style="--c:{s["color"]}">'
            f'{art_img(s, "tile-art")}{b}'
            f'<span class="nm">{e(s["name"])}</span><p>{e(s["tag"])}</p></a>')


NAMES_JSON = e(json.dumps({s['key']: s['name'] for s in SERIES}, ensure_ascii=False))


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


def load_guides():
    guides = []
    for f in sorted((ROOT / 'content' / 'guides').glob('*.md')):
        raw = f.read_text(encoding='utf-8')
        meta_txt, body = raw.split('\n\n', 1)
        meta = dict(line.split(': ', 1) if ': ' in line else (line.rstrip(':'), '') for line in meta_txt.splitlines())
        meta['slug'] = f.stem
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


GUIDES = load_guides()
GUIDES_BY_SERIE = {}
for g in GUIDES:
    if g.get('serie'):
        GUIDES_BY_SERIE.setdefault(g['serie'], []).append(g)


# --------------------------------------------------------------------------- accueil
def build_home():
    keys = ','.join(s['key'] for s in SERIES)
    by_cat = Counter(s['cat'] for s in SERIES)
    pop = [BY_KEY[k] for k in POPULAR]
    recent = [s['key'] for s in sorted(SERIES, key=lambda s: s['date'], reverse=True) if s['date'] > BASE_DATE]
    new = [BY_KEY[k] for k in (recent + [k for k in NEW_FALLBACK if k not in recent])[:3]]
    cats_html = ''.join(
        f'<a class="chip" href="/quiz/#{cid}">{name} <span class="muted">{by_cat[cid]}</span></a>' for cid, name, _ in CATEGORIES)
    modes = ''.join(f'<a class="mode" href="/jouer/?m={m}"><span class="mode-ico" aria-hidden="true">{i}</span>'
                    f'<span class="mode-name">{n}</span><p>{d}</p></a>' for m, i, n, d in MODES)
    guides = ''.join(f'<li><a href="/guides/{g["slug"]}/"><span class="gt">{e(g["title"])}</span>'
                     f'<span class="gd">{e(g["description"])}</span></a></li>' for g in GUIDES[:4])
    ld = [
        {'@context': 'https://schema.org', '@type': 'WebSite', 'name': 'KamiQuiz', 'url': SITE + '/', 'inLanguage': 'fr'},
        {'@context': 'https://schema.org', '@type': 'Organization', 'name': 'KamiQuiz', 'url': SITE + '/',
         'logo': SITE + '/assets/img/icon-512.png', 'email': 'contact@kamiquiz.com'},
    ]
    body = f'''<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <h1 class="display">Le quiz qui t'élève <span>au rang de Kami</span></h1>
      <p class="lede">{fr_num(TOTAL_Q)} questions sur {NB_SERIES} univers, des shōnen aux séries cultes. Chaque réponse est expliquée, pour apprendre autant que pour jouer.</p>
      <div class="btn-row">
        <a class="btn btn-gold" href="/quiz/">Choisir un quiz</a>
        <a class="btn" href="/jouer/">Tout mélanger</a>
      </div>
      <div class="hero-facts">
        <div>{fr_num(TOTAL_Q)}<small>questions expliquées</small></div>
        <div>{NB_SERIES}<small>univers</small></div>
        <div>0 €<small>sans inscription</small></div>
      </div>
    </div>
    <div class="qcard" id="qdj" data-keys="{keys}" data-names="{NAMES_JSON}" aria-labelledby="qdj-title">
      <div class="qcard-top"><strong id="qdj-title">Question du jour</strong><span class="chip" data-serie><i></i>…</span></div>
      <div data-slot><p class="qtext">Chargement de la question du jour…</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><div><h2 class="h2">Les plus joués</h2></div><p>Les univers favoris de la communauté, pour commencer en terrain connu.</p></div>
    <div class="tiles">{tile(pop[0], big=True)}{''.join(tile(s) for s in pop[1:5])}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><div><h2 class="h2">Nouveaux univers</h2></div><p>Les derniers quiz arrivés sur le site.</p></div>
    <div class="tiles">{''.join(tile(s, 'Nouveau') for s in new)}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><div><h2 class="h2">Kamidle, les jeux du jour</h2></div><p>Cinq énigmes par jour, les mêmes pour tout le monde. Trouve-les, garde ta série et partage ton résultat.</p></div>
    <div class="dle-modes">{dle_cards()}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><div><h2 class="h2">Tous les univers</h2></div><p>Cinq grandes familles, {NB_SERIES} quiz.</p></div>
    <div class="cat-nav">{cats_html}</div>
    <ul class="series-list">{''.join(series_row(BY_KEY[k]) for k in ['onepiece', 'jjk', 'demonslayer', 'got', 'harrypotter', 'zelda', 'histoire', 'geo'])}</ul>
    <p style="margin-top:20px"><a href="/quiz/">Voir les {NB_SERIES} quiz</a></p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><div><h2 class="h2">Six façons de jouer</h2></div><p>Chaque mode fonctionne avec tous les univers, ou avec toutes les questions mélangées.</p></div>
    <div class="modes">{modes}</div>
  </div>
</section>

<section class="section">
  <div class="wrap two-col">
    <div>
      <h2 class="h2">Classement mondial</h2>
      <p class="muted">Les meilleurs scores, toutes séries confondues. Enregistrez le vôtre à la fin d'une partie.</p>
      <ol class="board" data-board="global" data-names="{NAMES_JSON}"><li class="board-empty"><span class="empty">Chargement du classement…</span></li></ol>
    </div>
    <div>
      <h2 class="h2">Guides et dossiers</h2>
      <p class="muted">Pour réviser avant de jouer, ou comprendre une réponse.</p>
      <ul class="guide-list">{guides}</ul>
      <p style="margin-top:16px"><a href="/guides/">Tous les guides</a></p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="callout prose">
      <h2 class="h2">Un quiz pour apprendre, pas seulement pour gagner</h2>
      <p class="muted">KamiQuiz est né d'une idée simple : un bon quiz doit expliquer ses réponses. Chaque question est accompagnée d'une explication, chaque série a sa page de révision avec toutes ses questions classées par thème, et le jeu privilégie les questions que vous n'avez pas encore vues.</p>
      <a href="/a-propos/">En savoir plus sur KamiQuiz</a>
    </div>
  </div>
</section>
'''
    write('/', head(f'KamiQuiz — {fr_num(TOTAL_Q)} questions de quiz sur les animés, séries, films et jeux',
                    f'Quiz gratuits et sans inscription : {fr_num(TOTAL_Q)} questions expliquées sur {NB_SERIES} univers, de Naruto à Game of Thrones. Question du jour, six modes de jeu et classement mondial.',
                    '/', ld) + header('/') + body + footer())
    page('/', '1.0', 'daily')


# --------------------------------------------------------------------------- tous les quiz
def build_index():
    blocks = ''
    for cid, name, desc in CATEGORIES:
        items = [s for s in SERIES if s['cat'] == cid]
        n = sum(s['n'] for s in items)
        blocks += (f'<section class="cat-block" id="{cid}"><header><h2>{name}</h2><span>{len(items)} quiz, {fr_num(n)} questions</span></header>'
                   f'<p class="muted" style="margin:12px 0 4px">{e(desc)}</p><ul class="series-list">{"".join(series_row(s) for s in items)}</ul></section>')
    nav = ''.join(f'<a class="chip" href="#{cid}">{name}</a>' for cid, name, _ in CATEGORIES)
    ld = [crumbs_ld([('Accueil', '/'), ('Tous les quiz', '/quiz/')]),
          {'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': 'Tous les quiz KamiQuiz', 'url': SITE + '/quiz/',
           'hasPart': [{'@type': 'Quiz', 'name': f'Quiz {s["name"]}', 'url': f'{SITE}/quiz/{s["slug"]}/'} for s in SERIES]}]
    body = f'''<div class="wrap">
  <div class="page-head">
    {crumbs_html([('Accueil', '/'), ('Tous les quiz', '/quiz/')])}
    <h1 class="h1">Tous les quiz</h1>
    <p class="lede">{NB_SERIES} univers et {fr_num(TOTAL_Q)} questions, rangés par famille. Chaque quiz a sa page avec les questions à réviser et six modes de jeu.</p>
  </div>
  <div class="cat-nav" style="margin-top:28px">{nav}<a class="chip" href="/jouer/">Tout mélanger</a></div>
  {blocks}
</div>
'''
    write('/quiz/', head('Tous les quiz : animés, séries, films, jeux vidéo et culture — KamiQuiz',
                         f'La liste complète des {NB_SERIES} quiz gratuits de KamiQuiz : Naruto, One Piece, Harry Potter, Game of Thrones, Pokémon, histoire, géographie et bien plus.',
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
    crumbs = [('Accueil', '/'), ('Tous les quiz', '/quiz/'), (s['name'], path)]

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
        groups += f'<section class="qgroup"><h3>{e(icon)} {e(c)} <small>{len(items)} questions</small></h3><ol class="qlist">{lis}</ol></section>'

    modes = ''.join(f'<a class="mode" href="/jouer/?s={s["key"]}&amp;m={m}"><span class="mode-ico" aria-hidden="true">{i}</span>'
                    f'<span class="mode-name">{n}</span><p>{dsc}</p></a>' for m, i, n, dsc in MODES)

    ranks = d.get('ranks') or []
    rank_items = ''
    if ranks:
        step = 100 / len(ranks)
        rank_items = ''.join(f'<li><span>{e(r)}</span><span>{round(i * step)} %+</span></li>' for i, r in enumerate(ranks))

    related = [o for o in SERIES if o['cat'] == s['cat'] and o['key'] != s['key']][:6]
    related_html = ''.join(series_row(o) for o in related)
    guides = GUIDES_BY_SERIE.get(s['key'], [])
    guide_html = ''
    if guides:
        guide_html = ('<h2>Pour aller plus loin</h2><ul class="guide-list">' + ''.join(
            f'<li><a href="/guides/{g["slug"]}/"><span class="gt">{e(g["title"])}</span><span class="gd">{e(g["description"])}</span></a></li>'
            for g in guides) + '</ul>')

    themes = ', '.join(cats[:-1]) + (' et ' + cats[-1] if len(cats) > 1 else cats[0])
    desc = (f'Quiz {s["name"]} gratuit : {s["n"]} questions corrigées et expliquées sur {themes.lower()}. '
            f'Jouez en ligne sans inscription ou révisez toutes les réponses.')
    if len(desc) > 165:
        desc = f'Quiz {s["name"]} gratuit : {s["n"]} questions corrigées et expliquées. Six modes de jeu, sans inscription, avec toutes les réponses à réviser.'

    ld = [crumbs_ld(crumbs), {
        '@context': 'https://schema.org', '@type': 'Quiz', 'name': f'Quiz {s["name"]}', 'url': SITE + path,
        'description': desc, 'inLanguage': 'fr', 'about': {'@type': 'Thing', 'name': s['name']},
        'educationalLevel': 'Tous niveaux', 'isAccessibleForFree': True,
        'provider': {'@type': 'Organization', 'name': 'KamiQuiz', 'url': SITE + '/'}}]

    intro = ''.join(f'<p>{e(p)}</p>' for p in s['intro'])
    trailer_html = ''
    if s['key'] in TRAILERS:
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

    body = f'''<section class="serie-head">
  <div class="serie-art" aria-hidden="true">{art_img(s, "serie-art-img", eager=True)}</div>
  <div class="wrap">
    {crumbs_html(crumbs)}
    <h1 class="h1">Quiz <em>{e(s["name"])}</em></h1>
    <p class="lede">{e(s["tag"])}</p>
    <div class="btn-row">
      <a class="btn btn-gold" href="/jouer/?s={s["key"]}&amp;m=libre">Jouer 20 questions</a>
      <a class="btn" href="/jouer/?s={s["key"]}">Choisir un mode</a>
      <a class="btn" href="#questions">Réviser les réponses</a>
    </div>
    <div class="facts">
      <span class="chip"><i></i>{s["n"]} questions</span>
      <span class="chip">{len(cats)} thèmes</span>
      <span class="chip">{lv[1] + lv[2]} faciles ou moyennes, {lv[3] + lv[4]} difficiles</span>
    </div>
  </div>
</section>
<div class="wrap section" style="padding-top:48px">
  <div class="serie-body">
    <article class="article">
      <h2 style="margin-top:0">À propos de ce quiz</h2>
      {intro}
      {trailer_html}
      <h2>Les modes de jeu</h2>
      <div class="modes">{modes}</div>
      <h2 id="questions">Les {s["n"]} questions et leurs réponses</h2>
      <p>Toutes les questions du quiz {e(s["name"])}, classées par thème. Cliquez sur une question pour afficher la bonne réponse et son explication, ou tentez d'abord votre chance en jouant.</p>
      <div class="revise-tools"><button class="btn btn-sm" type="button" data-reveal="open">Afficher toutes les réponses</button><button class="btn btn-sm" type="button" data-reveal="close">Tout masquer</button></div>
      {groups}
      {guide_html}
      <h2>Autres quiz {e(CAT_NAME[s["cat"]].lower())}</h2>
      <ul class="series-list">{related_html}</ul>
    </article>
    <aside>
      <div class="aside-box">
        <h2>Thèmes</h2><ul>{cat_items}</ul>
        <h2 style="margin-top:22px">Difficulté</h2><ul>{lv_items}</ul>
        {"<h2 style='margin-top:22px'>Rangs à décrocher</h2><ul class='ranks'>" + rank_items + "</ul>" if rank_items else ""}
        <h2 style="margin-top:22px">Meilleurs scores</h2>
        <ol class="board" data-board="{s["key"]}" data-names="{NAMES_JSON}" style="font-size:.9rem"><li class="board-empty"><span class="empty">Chargement…</span></li></ol>
      </div>
    </aside>
  </div>
</div>
'''
    write(path, head(f'Quiz {s["name"]} : {s["n"]} questions avec réponses — KamiQuiz', desc, path, ld,
                     accent=s['color']) + header() + body + footer())
    page(path, '0.8', 'monthly', s['date'])


# --------------------------------------------------------------------------- app de jeu
def build_play():
    series_js = json.dumps({s['key']: {'name': s['name'], 'slug': s['slug'], 'color': s['color']} for s in SERIES},
                           ensure_ascii=False, separators=(',', ':'))
    body = f'''<section class="app">
  <div class="wrap app-shell">
    <div class="app-title"><h1>Quiz <em data-app-name>KamiQuiz</em></h1></div>

    <div class="screen" id="s-loading"><p class="loading">Chargement des questions…</p></div>

    <div class="screen" id="s-setup" hidden>
      <p class="lede" style="margin-bottom:24px">Choisissez votre façon de jouer.</p>
      <div class="pick-grid" id="mode-grid"></div>
      <div class="cat-picker" id="cat-picker" hidden>
        <h2 class="h2">Choisissez vos thèmes</h2>
        <div class="chips" id="cat-chips"></div>
        <button class="btn btn-gold" type="button" id="cat-go">Lancer le quiz</button>
      </div>
      <div class="cat-picker" id="duel-picker" hidden>
        <h2 class="h2">Qui s'affronte ?</h2>
        <div class="duel-names">
          <label class="sr-only" for="p1">Nom du joueur 1</label><input id="p1" maxlength="20" placeholder="Joueur 1" autocomplete="off">
          <label class="sr-only" for="p2">Nom du joueur 2</label><input id="p2" maxlength="20" placeholder="Joueur 2" autocomplete="off">
        </div>
        <button class="btn btn-gold" type="button" id="duel-go">Commencer le duel</button>
      </div>
      <p class="muted" style="margin-top:28px">Envie d'un autre univers ? <a href="/quiz/">Voir tous les quiz</a>.</p>
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
        <button class="btn btn-sm" type="button" id="quit">Arrêter</button>
        <button class="btn btn-gold" type="button" id="next" hidden>Question suivante</button>
      </div>
      <p class="muted" style="font-size:.82rem;margin-top:14px">Astuce : répondez avec les touches A, B, C, D ou 1 à 4, puis Entrée pour continuer.</p>
    </div>

    <div class="screen result" id="s-result" hidden>
      <div id="result-main"></div>
      <div class="btn-row">
        <button class="btn btn-gold" type="button" id="again">Rejouer</button>
        <button class="btn" type="button" id="other-mode">Changer de mode</button>
        <button class="btn" type="button" id="share">Partager mon score</button>
        <a class="btn" id="to-revise" href="/quiz/">Réviser les réponses</a>
      </div>
      <div class="save-score" id="save-box">
        <form id="save-form">
          <label for="save-name">Entrer au classement mondial</label>
          <div class="row"><input id="save-name" maxlength="20" placeholder="Votre pseudo" autocomplete="nickname"><button class="btn btn-gold btn-sm" id="save-btn" type="submit">Enregistrer</button></div>
        </form>
        <p id="save-msg"></p>
      </div>
      <div class="review" id="review" hidden><h2>Les réponses à retenir</h2><ol id="review-list"></ol></div>
    </div>
  </div>
</section>
<script>window.KQ_SERIES={series_js};</script>
'''
    write('/jouer/', head('Jouer — KamiQuiz', 'Jouez aux quiz KamiQuiz : six modes de jeu, réponses expliquées et classement mondial.',
                          '/jouer/', robots='noindex, follow') + header() + body + footer(('/assets/js/site.js', '/assets/js/quiz.js')))


# --------------------------------------------------------------------------- Kamidle (jeux du jour)
DLE_START = '2026-10-27'          # Kamidle n°1
DLE_DAYS = 800                    # calendrier calculé d'avance, identique dans tous les déploiements
DLE_INFO = {
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
        'univers': [(k, k) for k in DLE.UNIVERS],
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
        elif m == 'emoji':
            q += [(c['id'], c['u']) for c in extra if len(c['emo']) >= 2]
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
        ok = [c['id'] for c in DLE.CHARS
              if (m != 'pouvoir' or c['p']) and (m != 'emoji' or len(c['emo']) >= 2)]
        random.Random('kamidle-remplacement-' + m).shuffle(ok)
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
    return ''.join(
        f'<a class="dle-card" href="/dle/{m}/" data-dle-card="{m}"><span class="dle-ico" aria-hidden="true">{ico}</span>'
        f'<span class="dle-name">{label}</span><p>{e(desc)}</p><span class="dle-state" data-state>À jouer aujourd\'hui</span></a>'
        for m, label, ico, desc in DLE.MODES)


def build_dle():
    keys = {s['key'] for s in SERIES}
    chars = [c for c in DLE.CHARS if c['u'] in keys]
    series = {s['key']: {'n': s['name'], 's': s['slug'], 'c': s['cat']} for s in SERIES}
    data = {
        'start': DLE_START,
        'cats': {cid: name for cid, name, _ in CATEGORIES},
        'series': series,
        'chars': chars,
        'univers': {k: v for k, v in DLE.UNIVERS.items() if k in keys},
        'mots': {m: d for m, d in DLE.MOTS},
        'ages': DLE.AGES,
        'hairNear': [sorted(g) for g in DLE.HAIR_NEAR],
        'sched': dle_schedule(),
    }
    # Liste des mots acceptés pour le Mot mystère : dictionnaire (licence MIT, voir data/mots-fr.LICENSE.txt)
    # + mots du jeu + noms d'univers et de personnages d'un seul mot
    valid = set((ROOT / 'data' / 'mots-fr.txt').read_text(encoding='utf-8').split())
    valid |= {m for m, _ in DLE.MOTS}
    for c in chars:
        for part in re.split(r'[^A-Za-zÀ-ÿ]+', c['name'] + ' ' + ' '.join(c['alias'])):
            w = ''.join(ch for ch in __import__('unicodedata').normalize('NFD', part) if ch.isalpha() and ord(ch) < 128).upper()
            if 5 <= len(w) <= 8:
                valid.add(w)
    (DIST / 'data' / 'mots.txt').write_text('\n'.join(sorted(valid)), encoding='utf-8')
    (DIST / 'data' / 'dle.json').write_text(json.dumps(data, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    n_chars, n_pow = len(chars), sum(1 for c in chars if c['p'])
    n_univ = len(data['univers'])

    # ----- page d'accueil du Kamidle
    crumbs = [('Accueil', '/'), ('Kamidle', '/dle/')]
    body = f'''<div class="wrap">
  <div class="page-head">
    {crumbs_html(crumbs)}
    <h1 class="h1">Kamidle, les jeux du jour</h1>
    <p class="lede">Cinq énigmes chaque jour, les mêmes pour tous les joueurs : un personnage, un pouvoir, des emojis, un univers et un mot mystère à deviner.</p>
  </div>
  <div class="dle-modes" style="margin-top:32px">{dle_cards()}</div>
  <p class="dle-summary" data-dle-summary></p>
  <div class="two-col" style="margin-top:56px">
    <article class="prose">
      <h2 class="h2">Comment ça marche</h2>
      <p>Le Kamidle s'inspire des jeux en « -dle » nés avec Wordle : une énigme par jour, identique pour tout le monde, qui change à minuit (heure de ton appareil). Tu as le temps de réfléchir, de revenir plus tard dans la journée, et de comparer ton résultat avec tes amis le soir.</p>
      <p>Les jeux puisent dans les mêmes univers que nos quiz : {n_chars} personnages, {n_pow} pouvoirs décrits sans les nommer, {n_univ} univers résumés en cinq indices et {len(DLE.MOTS)} mots du vocabulaire des animés, des séries et des jeux vidéo, chacun accompagné de sa définition. Une fois l'énigme trouvée, tu peux enchaîner sur le quiz complet de la série pour vérifier que tu la connais vraiment.</p>
      <h2 class="h2" style="margin-top:32px">Ta série de victoires</h2>
      <p>Chaque jeu garde ta série de jours gagnés d'affilée et ton record. Ces statistiques restent sur ton appareil : pas de compte, pas d'inscription. Si tu changes de navigateur, tu repars de zéro.</p>
    </article>
    <article class="prose">
      <h2 class="h2">Sans spoiler majeur</h2>
      <p>Les indices s'en tiennent à ce qu'on apprend dans les premiers arcs de chaque œuvre. Les grandes révélations, l'identité cachée d'un personnage ou la fin d'une série ne servent jamais d'indice.</p>
      <h2 class="h2" style="margin-top:32px">Partager sans rien dévoiler</h2>
      <p>À la fin de chaque partie, le bouton « Partager » copie une grille de carrés colorés qui montre ton parcours sans révéler la réponse. Colle-la sur Discord, X ou dans ton groupe de discussion.</p>
      <h2 class="h2" style="margin-top:32px">Entraînement illimité</h2>
      <p>Une fois l'énigme du jour terminée, le mode entraînement te propose des parties au hasard, autant que tu veux. Elles ne comptent pas dans tes statistiques.</p>
      <h2 class="h2" style="margin-top:32px">Encore envie de jouer ?</h2>
      <p>Letsdle, un site ami, rassemble d'autres petits jeux à une partie par jour : quiz sur les films d'animation, associations de mots, géographie et plateformes piégées. <a href="{LETSDLE}" target="_blank" rel="noopener">Découvrir Letsdle</a>.</p>
    </article>
  </div>
</div>
'''
    ld = [crumbs_ld(crumbs)]
    write('/dle/', head('Kamidle — devine le personnage, le pouvoir et l\'univers du jour | KamiQuiz',
                        f'Cinq jeux du jour gratuits sur les animés, séries, films et jeux vidéo : devine le personnage, le pouvoir, les emojis, l\'univers et le mot du jour. {n_chars} personnages, sans inscription.',
                        '/dle/', ld) + header('/dle/') + body + footer(('/assets/js/site.js', '/assets/js/dle.js')))
    page('/dle/', '0.9', 'daily')

    # ----- une page par jeu
    legend_styles = ''.join(f'<li><b>{e(k)}</b> : {e(v)}</li>' for k, v in DLE.STYLE_HELP.items())
    for m, label, ico, desc in DLE.MODES:
        h1, rules = DLE_INFO[m]
        crumbs = [('Accueil', '/'), ('Kamidle', '/dle/'), (label, f'/dle/{m}/')]
        legend = ''
        if m == 'personnage':
            years = ', '.join(f'{e(BY_KEY[k]["name"])} {y}' + (f' ({DLE.YEAR_NOTES[k]})' if k in DLE.YEAR_NOTES else '')
                              for k, y in sorted(DLE.YEARS.items(), key=lambda kv: (kv[1], kv[0])) if k in BY_KEY)
            legend = f'''<h2 class="h2">Lire les indices</h2>
      <p><span class="dle-sw ok"></span> Vert : identique à la cible. <span class="dle-sw near"></span> Jaune : en partie juste (une espèce, un style ou une couleur de cheveux en commun, ou une couleur proche comme noir et brun). <span class="dle-sw no"></span> Rouge : aucun point commun. Pour l'âge et l'année, la flèche indique si la cible est plus âgée (↑) ou plus jeune (↓), plus récente (↑) ou plus ancienne (↓).</p>
      <p>Le <b>rôle</b> décrit la place du personnage dans l'histoire : protagoniste, allié, rival, mentor, antagoniste ou neutre. Le <b>style</b> décrit sa façon principale de combattre :</p>
      <ul class="dle-legend">{legend_styles}</ul>
      <p>L'<b>âge</b> est l'âge réel du personnage pendant l'essentiel de l'histoire, pas son apparence : enfant (12 ans ou moins), ado (13 à 19 ans), adulte (20 à 59 ans), âgé (60 ans et plus) ou sans âge (immortels, espèces à très longue vie, créatures et animaux). Les <b>cheveux</b> sont ceux de son look le plus connu ; « aucun » veut dire chauve, casqué, ou couvert de fourrure.</p>
      <p>L'<b>année</b> est celle du début de l'œuvre originale : premier tome, premier épisode, premier film ou premier jeu. {years}.</p>'''
        elif m == 'mot':
            legend = f'''<h2 class="h2">Règles</h2>
      <p>Le mot du jour compte entre cinq et huit lettres, sans accent. Tape un mot de la bonne longueur au clavier ou avec les touches à l'écran, puis valide. <span class="dle-sw ok"></span> Vert : la lettre est à la bonne place. <span class="dle-sw near"></span> Jaune : la lettre est dans le mot, mais ailleurs. <span class="dle-sw no"></span> Gris : la lettre n'y est pas.</p>
      <p>Les essais doivent être de vrais mots français, ou des termes de l'univers des animés et des jeux vidéo. Le mot à trouver vient toujours de cet univers, et sa définition s'affiche à la fin de la partie.</p>'''
        others = ''.join(f'<a class="chip" href="/dle/{m2}/">{i2} {l2}</a>' for m2, l2, i2, _ in DLE.MODES if m2 != m)
        body = f'''<div class="wrap">
  <div class="page-head">
    {crumbs_html(crumbs)}
    <h1 class="h1">{e(h1)}</h1>
    <p class="lede">{e(rules)}</p>
  </div>
  <section class="dle" id="dle" data-mode="{m}" aria-live="polite">
    <p class="loading">Chargement de l'énigme du jour…</p>
  </section>
  <p class="dle-yesterday" data-dle-yesterday></p>
  <div class="two-col" style="margin-top:48px">
    <article class="prose">{legend or f'<h2 class="h2">Règles</h2><p>{e(rules)}</p><p>Les réponses viennent des univers de nos quiz. Tape les premières lettres d\'un nom pour voir les propositions, puis choisis dans la liste.</p>'}</article>
    <aside class="prose">
      <h2 class="h2">Les autres jeux du jour</h2>
      <div class="chips" style="margin-top:12px">{others}</div>
      <p class="muted" style="margin-top:20px">Une nouvelle énigme arrive chaque jour à minuit. Tes séries de victoires sont enregistrées sur ton appareil.</p>
    </aside>
  </div>
</div>
'''
        write(f'/dle/{m}/', head(f'{h1} — Kamidle | KamiQuiz', f'{rules} Jeu gratuit, une énigme par jour.',
                                 f'/dle/{m}/', [crumbs_ld(crumbs)]) + header('/dle/') + body + footer(('/assets/js/site.js', '/assets/js/dle.js')))
        page(f'/dle/{m}/', '0.8', 'daily')


# --------------------------------------------------------------------------- guides
def build_guides():
    items = ''.join(f'<li><a href="/guides/{g["slug"]}/"><span class="gt">{e(g["title"])}</span><span class="gd">{e(g["description"])}</span></a></li>'
                    for g in GUIDES)
    ld = [crumbs_ld([('Accueil', '/'), ('Guides', '/guides/')])]
    body = f'''<div class="wrap">
  <div class="page-head prose">
    {crumbs_html([('Accueil', '/'), ('Guides', '/guides/')])}
    <h1 class="h1">Guides et dossiers</h1>
    <p class="lede">Des articles pour comprendre les univers des quiz, réviser les points qui font trébucher et mieux retenir ce que l'on apprend en jouant.</p>
  </div>
  <ul class="guide-list prose" style="margin-top:24px">{items}</ul>
</div>
'''
    write('/guides/', head('Guides et dossiers sur les animés, séries et jeux — KamiQuiz',
                           'Dossiers originaux pour réviser avant de jouer : les Fruits du Démon, les maisons de Poudlard, les Piliers de Demon Slayer, la table des types Pokémon et bien d\'autres.',
                           '/guides/', ld) + header('/guides/') + body + footer())
    page('/guides/', '0.7', 'weekly')

    for g in GUIDES:
        path = f'/guides/{g["slug"]}/'
        crumbs = [('Accueil', '/'), ('Guides', '/guides/'), (g['title'], path)]
        s = BY_KEY.get(g.get('serie') or '')
        accent = s['color'] if s else None
        cta = ''
        if s:
            cta = (f'<div class="callout" style="margin-top:48px"><h2 class="h2">Testez-vous sur {e(s["name"])}</h2>'
                   f'<p class="muted">{s["n"]} questions expliquées vous attendent, de la plus simple à la plus pointue.</p>'
                   f'<div class="btn-row"><a class="btn btn-gold" href="/jouer/?s={s["key"]}&amp;m=libre">Jouer au quiz {e(s["name"])}</a>'
                   f'<a class="btn" href="/quiz/{s["slug"]}/#questions">Réviser les réponses</a></div></div>')
        else:
            cta = ('<div class="callout" style="margin-top:48px"><h2 class="h2">À vous de jouer</h2>'
                   '<p class="muted">Choisissez un univers et appliquez la méthode dès maintenant.</p>'
                   '<div class="btn-row"><a class="btn btn-gold" href="/quiz/">Choisir un quiz</a></div></div>')
        others = ''.join(f'<li><a href="/guides/{o["slug"]}/"><span class="gt">{e(o["title"])}</span></a></li>'
                         for o in GUIDES if o['slug'] != g['slug'])[:4000]
        ld = [crumbs_ld(crumbs), {
            '@context': 'https://schema.org', '@type': 'Article', 'headline': g['title'], 'description': g['description'],
            'datePublished': g['date'], 'dateModified': g['date'], 'inLanguage': 'fr', 'mainEntityOfPage': SITE + path,
            'image': SITE + '/assets/img/og-image.png',
            'author': {'@type': 'Organization', 'name': 'La rédaction de KamiQuiz', 'url': SITE + '/a-propos/'},
            'publisher': {'@type': 'Organization', 'name': 'KamiQuiz', 'logo': {'@type': 'ImageObject', 'url': SITE + '/assets/img/icon-512.png'}}}]
        minutes = max(3, round(g['words'] / 220))
        body = f'''<div class="wrap">
  <div class="page-head prose">
    {crumbs_html(crumbs)}
    <h1 class="h1" style="font-size:clamp(2.2rem,5vw,3.6rem)">{e(g["title"])}</h1>
    <p class="lede">{e(g["description"])}</p>
    <p class="meta">Par la rédaction de KamiQuiz, publié le {fr_date(g['date'])}. Lecture : {minutes} minutes.</p>
  </div>
  <article class="article prose" style="margin-top:32px">
    {g["html"]}
    {cta}
  </article>
  <section class="prose" style="margin-top:56px"><h2 class="h2">Autres guides</h2><ul class="guide-list">{others}</ul></section>
</div>
'''
        write(path, head(f'{g["title"]} — KamiQuiz', g['description'], path, ld, og_type='article', accent=accent)
              + header('/guides/') + body + footer())
        page(path, '0.7', 'monthly', g['date'])


# --------------------------------------------------------------------------- pages simples
def simple(path, title, desc, h1, lede, inner, current='', prio='0.4'):
    crumbs = [('Accueil', '/'), (h1, path)]
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
           'À propos de KamiQuiz', 'Un site de quiz francophone, gratuit et indépendant, où chaque réponse est expliquée.', f'''
<h2>Ce qu'est KamiQuiz</h2>
<p>KamiQuiz rassemble {fr_num(TOTAL_Q)} questions réparties sur {NB_SERIES} univers : {nb["anime"]} animés et mangas, {nb["series"]} séries télévisées, {nb["films"]} grandes sagas du cinéma, {nb["jeux"]} jeux vidéo et {nb["culture"]} quiz de culture générale. Le site est gratuit, sans inscription et fonctionne aussi bien sur téléphone que sur ordinateur.</p>
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
''', '/a-propos/', '0.5')

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
    rows = ''.join(series_row(BY_KEY[k]) for k in POPULAR)
    body = f'''<div class="wrap notfound">
  <p class="display">404</p>
  <h1 class="h2" style="margin-top:12px">Cette page n'existe pas</h1>
  <p class="muted">Le lien est peut-être ancien. Tous les quiz sont toujours là.</p>
  <div class="btn-row" style="justify-content:center;margin-top:20px"><a class="btn btn-gold" href="/quiz/">Voir tous les quiz</a><a class="btn" href="/">Accueil</a></div>
</div>
<div class="wrap" style="max-width:760px"><ul class="series-list" style="grid-template-columns:1fr">{rows}</ul></div>
'''
    (DIST / '404.html').write_text(head('Page introuvable — KamiQuiz', 'Cette page n\'existe pas.', '/404', robots='noindex')
                                   + header() + body + footer(), encoding='utf-8')


# --------------------------------------------------------------------------- données et fichiers techniques
def build_data():
    out = DIST / 'data'
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
        'name': 'Tout mélanger', 'color': '#d4a843', 'ranks': [],
        'cats': {s['name']: {'i': ''} for s in SERIES}, 'q': allq}, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')


def build_tech():
    urls = ''.join(f'<url><loc>{SITE}{p}</loc><lastmod>{lm}</lastmod><changefreq>{f}</changefreq><priority>{pr}</priority></url>\n'
                   for p, pr, f, lm in PAGES)
    (DIST / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
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
    build_data()
    build_home()
    build_index()
    for s in SERIES:
        build_serie(s)
    build_play()
    build_guides()
    build_static_pages()
    build_dle()
    build_tech()
    n_html = len(list(DIST.rglob('*.html')))
    print(f'[{TODAY}] Site généré : {n_html} pages HTML, {len(PAGES)} URLs dans le sitemap, {fr_num(TOTAL_Q)} questions, {len(GUIDES)} guides')


if __name__ == '__main__':
    main()
