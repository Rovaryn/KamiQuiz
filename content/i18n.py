"""Langues du site.

Le français est la langue source : tous les textes de build.py sont écrits en français et passent
par T(). Pour une autre langue, T() cherche la traduction dans content/<langue>/ui.py, rangée sous
l'identifiant qid() du texte français ; une phrase sans traduction fait échouer la génération (aucun
texte français ne peut fuiter sur les pages anglaises). tools/i18n_status.py --ui liste les manques.

Les chemins sont toujours écrits en version française (« chemins logiques ») et U() les convertit :
/quiz/seigneur-des-anneaux/ -> /en/quiz/lord-of-the-rings/, /jouer/ -> /en/play/, etc.
"""
import datetime
import os
import re

LANGS = os.environ.get('KQ_LANGS', 'fr,en').split(',')   # langues générées
LANG = 'fr'                    # langue en cours de génération
MISSING = set()

LOCALES = {'fr': 'fr_FR', 'en': 'en_US'}
ROUTES = {
    'en': {'/': '/en/', '/quiz/': '/en/quiz/', '/jouer/': '/en/play/', '/dle/': '/en/dle/', '/guides/': '/en/guides/',
           '/a-propos/': '/en/about/', '/contact/': '/en/contact/', '/confidentialite/': '/en/privacy/',
           '/conditions/': '/en/terms/', '/404': '/en/404'},
}
DLE_SLUGS = {'en': {'personnage': 'character', 'pouvoir': 'power', 'emoji': 'emoji', 'univers': 'universe', 'mot': 'word'}}
QUIZ_SLUGS = {'en': {}}        # slug français -> slug traduit (rempli par build.py)
GUIDE_SLUGS = {'en': {}}

_UI = {}


def qid(text):
    """Identifiant court et stable d'une question, calculé sur son texte français."""
    import hashlib
    return hashlib.sha1(text.strip().encode('utf-8')).hexdigest()[:8]


def ui(lang):
    if lang not in _UI:
        mod = __import__(f'{lang}.ui', fromlist=['UI'])
        _UI[lang] = mod.UI
    return _UI[lang]


def set_lang(lang):
    global LANG
    LANG = lang


def T(fr, **kw):
    """Traduit un texte écrit en français (accepte des champs {nom} remplis par kw)."""
    if LANG == 'fr':
        txt = fr
    else:
        txt = ui(LANG).get(qid(fr))
        if txt is None:
            MISSING.add(fr)
            txt = fr
    return txt.format(**kw) if kw else txt


def U(path, lang=None):
    """Chemin logique (français) -> chemin réel dans la langue demandée."""
    lang = lang or LANG
    if lang == 'fr' or not path.startswith('/') or path.startswith(('/data/', '/assets/', '/sitemap')):
        return path
    m = re.match(r'^([^?#]*)(.*)$', path)
    base, rest = m.group(1), m.group(2)
    routes = ROUTES[lang]
    if base in routes:
        return routes[base] + rest
    m = re.match(r'^/quiz/([^/]+)/$', base)
    if m:
        return f'/{lang}/quiz/{QUIZ_SLUGS[lang].get(m.group(1), m.group(1))}/' + rest
    m = re.match(r'^/guides/([^/]+)/$', base)
    if m:
        return f'/{lang}/guides/{GUIDE_SLUGS[lang][m.group(1)]}/' + rest
    m = re.match(r'^/dle/([^/]+)/$', base)
    if m:
        return f'/{lang}/dle/{DLE_SLUGS[lang][m.group(1)]}/' + rest
    raise ValueError(f'chemin sans équivalent en {lang} : {path}')


def num(n):
    return f'{n:,}'.replace(',', ' ') if LANG == 'fr' else f'{n:,}'


FR_MONTHS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']
EN_MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


def loc_date(iso):
    d = datetime.date.fromisoformat(iso)
    if LANG == 'fr':
        return f'{"1er" if d.day == 1 else d.day} {FR_MONTHS[d.month - 1]} {d.year}'
    return f'{EN_MONTHS[d.month - 1]} {d.day}, {d.year}'
