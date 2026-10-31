#!/usr/bin/env python3
"""Vérifications statiques du site généré (dist/)."""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote

DIST = Path(__file__).resolve().parent.parent / 'dist'
errors, warnings = [], []
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}


class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack, self.bad, self.links, self.ids, self.ld = [], [], [], set(), []
        self.in_ld = False
        self.title = None
        self._t = False
        self.h1 = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            if a['id'] in self.ids:
                self.bad.append(f'id dupliqué: {a["id"]}')
            self.ids.add(a['id'])
        if tag == 'a' and a.get('href'):
            self.links.append(a['href'])
        if tag in ('link', 'script') and (a.get('href') or a.get('src')):
            self.links.append(a.get('href') or a.get('src'))
        if tag == 'script' and a.get('type') == 'application/ld+json':
            self.in_ld = True
        if tag == 'title':
            self._t = True
        if tag == 'h1':
            self.h1 += 1
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack or self.stack[-1] != tag:
            # HTML autorise la fermeture implicite de <li>/<p> ; on signale les vrais déséquilibres
            if tag in self.stack:
                while self.stack[-1] != tag:
                    t = self.stack.pop()
                    if t not in ('li', 'p'):
                        self.bad.append(f'<{t}> non fermé avant </{tag}>')
                self.stack.pop()
            else:
                self.bad.append(f'</{tag}> sans ouverture')
            return
        self.stack.pop()
        if tag == 'script':
            self.in_ld = False
        if tag == 'title':
            self._t = False

    def handle_data(self, data):
        if self.in_ld:
            self.ld.append(data)
        if self._t:
            self.title = (self.title or '') + data


def resolve(href):
    u = urlparse(href)
    if u.scheme or href.startswith('mailto:') or href.startswith('#'):
        return None, u.fragment
    path = unquote(u.path)
    if not path:
        return None, u.fragment
    f = DIST / path.lstrip('/')
    if path.endswith('/'):
        f = f / 'index.html'
    return f, u.fragment


pages = sorted(DIST.rglob('*.html'))
ids_by_file = {}
parsed = {}
for f in pages:
    p = P()
    p.feed(f.read_text(encoding='utf-8'))
    parsed[f] = p
    ids_by_file[f] = p.ids
    rel = '/' + str(f.relative_to(DIST))
    for b in p.bad:
        errors.append(f'{rel}: {b}')
    left = [t for t in p.stack if t not in ('html', 'body', 'head')]
    if left:
        errors.append(f'{rel}: balises non fermées {left}')
    if not p.title:
        errors.append(f'{rel}: pas de <title>')
    if p.h1 != 1 and not rel.endswith('jouer/index.html'):
        warnings.append(f'{rel}: {p.h1} balises h1')
    for block in p.ld:
        try:
            json.loads(block)
        except Exception as ex:
            errors.append(f'{rel}: JSON-LD invalide ({ex})')
    if 'adsbygoogle.js?client=ca-pub-6970710961658841' not in f.read_text(encoding='utf-8'):
        errors.append(f'{rel}: script AdSense absent')
    if re.search(r'ratingValue|aggregateRating', f.read_text(encoding='utf-8')):
        errors.append(f'{rel}: note agrégée détectée')

for f, p in parsed.items():
    rel = '/' + str(f.relative_to(DIST))
    for href in p.links:
        if '?' in href and href.startswith('/jouer/'):
            href = href.split('?')[0]
        href = href.split('?v=')[0]
        target, frag = resolve(href)
        if target is None:
            if frag and href.startswith('#') and frag not in p.ids:
                errors.append(f'{rel}: ancre interne introuvable #{frag}')
            continue
        if not target.exists():
            errors.append(f'{rel}: lien cassé {href}')
        elif frag and target.suffix == '.html' and frag not in ids_by_file.get(target, set()):
            errors.append(f'{rel}: ancre introuvable {href}')

# sitemap : chaque URL existe
sm = (DIST / 'sitemap.xml').read_text(encoding='utf-8')
for loc in re.findall(r'<loc>https://kamiquiz.com([^<]*)</loc>', sm):
    t, _ = resolve(loc)
    if not t.exists():
        errors.append(f'sitemap: {loc} introuvable')

# redirections : chaque cible existe
for line in (DIST / '_redirects').read_text().splitlines():
    if not line or line.startswith('#'):
        continue
    src, dst, code = line.split()
    t, _ = resolve(dst)
    if not t.exists():
        errors.append(f'_redirects: cible {dst} introuvable')
    if (DIST / src.lstrip('/')).exists():
        errors.append(f'_redirects: la source {src} existe encore comme fichier')

# données
for jf in (DIST / 'data').glob('*.json'):
    d = json.loads(jf.read_text(encoding='utf-8'))
    if jf.name == 'dle.json':
        ids = {c['id'] for c in d['chars']}
        for c in d['chars']:
            if c['u'] not in d['series']:
                errors.append(f"dle.json: {c['id']} renvoie vers une série non publiée")
        for k in d['univers']:
            if k not in d['series']:
                errors.append(f'dle.json: univers {k} non publié')
        for m, lst in d['sched'].items():
            if len(lst) < 365:
                errors.append(f'dle.json: calendrier {m} trop court')
        continue
    for q in d['q']:
        if len(q['a']) != 4 or not 0 <= q['c'] < 4:
            errors.append(f'{jf.name}: question invalide {q["q"][:50]}')

print(f'{len(pages)} pages HTML vérifiées')
print(f'Erreurs : {len(errors)}')
for x in errors[:40]:
    print('  ✗', x)
print(f'Avertissements : {len(warnings)}')
for x in warnings[:20]:
    print('  !', x)
sys.exit(1 if errors else 0)
