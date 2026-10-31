#!/usr/bin/env python3
"""Tests de bout en bout dans Chromium headless contre http://localhost:8765."""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = 'http://localhost:8765'
SHOTS = Path(sys.argv[1] if len(sys.argv) > 1 else '/tmp/claude-0/shots')
SHOTS.mkdir(parents=True, exist_ok=True)
fails = []


def check(cond, msg):
    if not cond:
        fails.append(msg)
        print('  ✗', msg)
    else:
        print('  ✓', msg)


def block_external(route):
    # AdSense et le Worker ne sont pas joignables depuis le bac à sable : on simule un échec réseau
    route.abort()


def play_through(page, max_q=40, wrong_every=0):
    n = 0
    while n < max_q and page.is_visible('#s-play'):
        page.wait_for_selector('#q-answers .answer:not([disabled])', timeout=5000)
        idx = 0 if not wrong_every or n % wrong_every else 1
        page.click(f'#q-answers .answer >> nth={idx}')
        page.wait_for_selector('#next:not([hidden])', timeout=3000)
        page.click('#next')
        n += 1
    return n


with sync_playwright() as p:
    b = p.chromium.launch()
    ctx = b.new_context(viewport={'width': 1366, 'height': 900})
    ctx.route('**/pagead2.googlesyndication.com/**', block_external)
    ctx.route('**/*.workers.dev/**', block_external)
    page = ctx.new_page()
    console_errors = []
    page.on('pageerror', lambda e: console_errors.append(str(e)))

    print('Accueil')
    page.goto(BASE + '/')
    page.wait_for_selector('#qdj .answer', timeout=5000)
    check(page.locator('#qdj .answer').count() == 4, 'la question du jour affiche 4 réponses')
    page.screenshot(path=str(SHOTS / 'home-desktop.png'), full_page=False)
    page.click('#qdj .answer >> nth=2')
    check(page.is_visible('#qdj .feedback'), 'la question du jour affiche une explication après réponse')
    check(page.locator('#qdj .is-right').count() == 1, 'la bonne réponse est mise en évidence')
    page.wait_for_selector('[data-board] .empty')
    check('indisponible' in page.inner_text('[data-board]'), 'classement indisponible : message clair')
    page.screenshot(path=str(SHOTS / 'home-desktop-full.png'), full_page=True)

    print('Tous les quiz')
    page.goto(BASE + '/quiz/')
    n_series = page.locator('.series-row').count()
    check(n_series >= 42, f'{n_series} séries listées')
    page.screenshot(path=str(SHOTS / 'quiz-index.png'))

    print('Page série')
    page.goto(BASE + '/quiz/naruto/')
    check(page.locator('.qitem').count() >= 70, 'les questions de révision sont dans le HTML')
    page.click('[data-reveal="open"]')
    check(page.locator('.qitem details[open]').count() == page.locator('.qitem').count(), '« Afficher toutes les réponses » ouvre tout')
    page.screenshot(path=str(SHOTS / 'serie-desktop.png'))
    page.click('[data-reveal="close"]')

    for mode, label in [('libre', 'mode libre'), ('maitre', 'ascension'), ('expert', 'expert')]:
        print('Jeu :', label)
        page.goto(f'{BASE}/jouer/?s=onepiece&m={mode}')
        page.wait_for_selector('#s-play:not([hidden])', timeout=5000)
        if mode == 'libre':
            check(page.is_hidden('#next'), 'le bouton « Question suivante » est caché avant de répondre')
            check(page.is_hidden('#q-feedback'), 'l\'explication est cachée avant de répondre')
            page.screenshot(path=str(SHOTS / 'play-desktop.png'))
        n = play_through(page, 40, wrong_every=3)
        check(page.is_visible('#s-result'), f'{label} : écran de résultat atteint après {n} questions')
        txt = page.inner_text('#result-main')
        check('%' in txt or '/' in txt, f'{label} : score affiché ({txt.splitlines()[0] if txt else "vide"})')
        if mode == 'libre':
            check(n == 20, 'mode libre : 20 questions')
            check(page.is_visible('#review'), 'récapitulatif des erreurs affiché')
            page.screenshot(path=str(SHOTS / 'result-desktop.png'), full_page=True)
            page.fill('#save-name', 'TestBot')
            page.click('#save-btn')
            page.wait_for_function("document.querySelector('#save-msg').textContent.includes('ne répond pas')", timeout=4000)
            check(True, 'échec du classement géré proprement')
            page.click('#again')
            check(page.is_visible('#s-play'), 'Rejouer relance une partie')

    print('Nouveaux univers')
    for slug, key, n in [('frieren', 'frieren', 58), ('chainsaw-man', 'chainsawman', 54), ('spy-x-family', 'spyfamily', 54)]:
        if not Path(f'dist/data/{key}.json').exists():
            print(f'  · {slug} : pas encore publié à cette date, ignoré')
            continue
        page.goto(f'{BASE}/quiz/{slug}/')
        check(page.locator('.qitem').count() == n, f'{slug} : {n} questions de révision')
        page.goto(f'{BASE}/jouer/?s={key}&m=libre')
        page.wait_for_selector('#s-play:not([hidden])', timeout=5000)
        played = play_through(page, 30)
        check(page.is_visible('#s-result') and played == 20, f'{slug} : partie complète')
    if Path('dist/data/frieren.json').exists():
        page.goto(BASE + '/quiz/frieren/')
        page.screenshot(path=str(SHOTS / 'frieren-desktop.png'))

    print('Jeu : survie')
    page.goto(f'{BASE}/jouer/?s=geo&m=survie')
    page.wait_for_selector('#s-play:not([hidden])')
    n = 0
    while page.is_visible('#s-play') and n < 200:
        page.wait_for_selector('#q-answers .answer:not([disabled])')
        # on cherche volontairement une mauvaise réponse pour perdre les vies
        page.evaluate("document.querySelectorAll('#q-answers .answer')[0].click()")
        page.wait_for_selector('#next:not([hidden])')
        page.click('#next')
        n += 1
    check(page.is_visible('#s-result'), f'survie : partie terminée après {n} questions (3 vies)')

    print('Jeu : contre la montre (le temps s\'écoule)')
    page.goto(f'{BASE}/jouer/?s=sport&m=chrono')
    page.wait_for_selector('#s-play:not([hidden])')
    page.wait_for_selector('#next:not([hidden])', timeout=20000)
    check('Temps écoulé' in page.inner_text('#q-feedback'), 'chrono : la question expire au bout de 15 s')

    print('Jeu : par thème')
    page.goto(f'{BASE}/jouer/?s=harrypotter')
    page.wait_for_selector('#s-setup:not([hidden])')
    page.click('[data-mode="categorie"]')
    page.click('#cat-chips .chip >> nth=0')
    page.click('#cat-go')
    page.wait_for_selector('#s-play:not([hidden])')
    first_cat = page.inner_text('#q-meta')
    check(len(first_cat) > 0, f'par thème : partie lancée ({first_cat.splitlines()[0]})')

    print('Jeu : duel')
    page.goto(f'{BASE}/jouer/?s=friends')
    page.wait_for_selector('#s-setup:not([hidden])')
    page.click('[data-mode="duel"]')
    page.fill('#p1', 'Ross')
    page.fill('#p2', 'Rachel')
    page.click('#duel-go')
    check('Ross' in page.inner_text('#hud-left'), 'duel : le premier joueur a la main')
    n = play_through(page, 30)
    check(page.is_visible('#s-result') and n == 20, 'duel : 20 questions puis résultat')
    check(page.is_hidden('#save-box'), 'duel : pas d\'enregistrement au classement')

    print('Jeu : tout mélanger')
    page.goto(f'{BASE}/jouer/?m=libre')
    page.wait_for_selector('#s-play:not([hidden])', timeout=8000)
    check(page.inner_text('[data-app-name]') == 'Tout mélanger', 'mode mélangé chargé')

    print('Clavier')
    page.goto(f'{BASE}/jouer/?s=zelda&m=libre')
    page.wait_for_selector('#s-play:not([hidden])')
    check(page.is_hidden('#next'), 'clavier : rien n\'est validé avant la touche')
    page.keyboard.press('b')
    check(page.is_visible('#next'), 'la touche B répond')
    page.keyboard.press('Enter')
    check('2' in page.inner_text('#hud-left'), 'Entrée passe à la question suivante')

    print('Guide et pages légales')
    page.goto(BASE + '/guides/table-des-types-pokemon/')
    check(page.locator('article h2').count() >= 5, 'le guide a ses intertitres')
    page.screenshot(path=str(SHOTS / 'guide-desktop.png'))
    page.goto(BASE + '/confidentialite/')
    check(page.locator('[data-privacy-choices]').count() == 1, 'bouton de choix de confidentialité présent')

    print('Lien Letsdle')
    page.goto(BASE + '/')
    ext = page.locator('#nav a.nav-ext')
    check(ext.count() == 1 and ext.get_attribute('href') == 'https://letsdle.com/' and ext.get_attribute('target') == '_blank',
          'menu : lien « Plus de jeux » vers Letsdle, nouvel onglet')
    for w in (1366, 1024, 800):
        page.set_viewport_size({'width': w, 'height': 900})
        tops = page.evaluate("[...document.querySelectorAll('#nav a')].map(a => Math.round(a.getBoundingClientRect().top))")
        sw = page.evaluate('document.documentElement.scrollWidth')
        check(len(set(tops)) == 1 and sw <= w, f'menu sur une seule ligne à {w}px')
        page.screenshot(path=str(SHOTS / f'header-{w}.png'), clip={'x': 0, 'y': 0, 'width': w, 'height': 80})
    page.set_viewport_size({'width': 1366, 'height': 900})

    print('Kamidle')
    import json as _j
    D = _j.loads(Path('dist/data/dle.json').read_text(encoding='utf-8'))
    page.goto(BASE + '/dle/')
    check(page.locator('[data-dle-card]').count() == 4, 'hub Kamidle : 4 jeux')
    page.screenshot(path=str(SHOTS / 'dle-hub.png'), full_page=True)
    for mode in ('personnage', 'pouvoir', 'emoji', 'univers'):
        page.goto(f'{BASE}/dle/{mode}/')
        page.wait_for_selector('#dle-in', timeout=5000)
        tid = page.evaluate("""(m) => fetch('/data/dle.json').then(r=>r.json()).then(d=>{
            const p=d.start.split('-'), n=new Date();
            const i=Math.max(0,Math.round((Date.UTC(n.getFullYear(),n.getMonth(),n.getDate())-Date.UTC(+p[0],+p[1]-1,+p[2]))/864e5));
            return d.sched[m][i % d.sched[m].length];})""", mode)
        tname = D['series'][tid]['n'] if mode == 'univers' else next(c['name'] for c in D['chars'] if c['id'] == tid)
        # deux mauvais essais puis la bonne réponse
        wrong = [c['name'] for c in D['chars'] if c['id'] != tid][:2] if mode != 'univers' else \
                [D['series'][k]['n'] for k in D['univers'] if k != tid][:2]
        for w in wrong:
            page.fill('#dle-in', w)
            page.wait_for_selector('#dle-list li[role=option]')
            page.keyboard.press('Enter')
        if mode == 'personnage':
            check(page.locator('.dle-table tbody tr').count() == 2, 'personnage : 2 lignes de comparaison')
            page.screenshot(path=str(SHOTS / 'dle-personnage.png'), full_page=True)
        else:
            check(page.locator('.dle-guesses li').count() == 2, f'{mode} : 2 essais affichés')
        if mode == 'emoji':
            check(page.locator('.dle-e.on').count() == min(3, len(next(c for c in D['chars'] if c['id'] == tid)['emo'])), 'emoji : un emoji révélé par erreur')
        if mode == 'univers':
            check(page.locator('.dle-clues li.on').count() == 3, 'univers : un indice de plus par erreur')
        page.fill('#dle-in', tname)
        page.wait_for_selector('#dle-list li[role=option]')
        page.click('#dle-list li[role=option] >> nth=0')
        page.wait_for_selector('.dle-result.win', timeout=3000)
        check(tname in page.inner_text('.dle-answer'), f'{mode} : victoire sur « {tname} »')
        check('1' in page.inner_text('.dle-stats'), f'{mode} : statistiques enregistrées')
        page.screenshot(path=str(SHOTS / f'dle-{mode}-fin.png'), full_page=True)
        page.reload()
        page.wait_for_selector('.dle-result.win')
        check(page.is_hidden('#dle-in'), f'{mode} : la partie du jour reste terminée après rechargement')
        page.click('[data-act=practice]')
        check(page.is_visible('#dle-in') and 'Entraînement' in page.inner_text('.dle-top'), f'{mode} : entraînement lancé')
    page.goto(BASE + '/dle/')
    check(page.locator('.dle-card.is-won').count() == 4, 'hub : les 4 jeux marqués trouvés')
    check('quatre' in page.inner_text('[data-dle-summary]'), 'hub : message de fin de journée')

    check(not console_errors, 'aucune erreur JavaScript' + (f' ({console_errors[:3]})' if console_errors else ''))

    print('Mobile')
    m = b.new_context(viewport={'width': 390, 'height': 844}, device_scale_factor=2, is_mobile=True, has_touch=True)
    m.route('**/pagead2.googlesyndication.com/**', block_external)
    m.route('**/*.workers.dev/**', block_external)
    mp = m.new_page()
    for path, name in [('/dle/personnage/', 'dle-mobile'), ('/', 'home-mobile'), ('/quiz/naruto/', 'serie-mobile'), ('/jouer/?s=naruto&m=libre', 'play-mobile'), ('/quiz/', 'index-mobile')]:
        mp.goto(BASE + path)
        mp.wait_for_timeout(600)
        sw = mp.evaluate('document.documentElement.scrollWidth')
        check(sw <= 390, f'{path} : pas de défilement horizontal sur mobile ({sw}px)')
        mp.screenshot(path=str(SHOTS / f'{name}.png'))
    mp.goto(BASE + '/')
    mp.click('.menu-btn')
    check(mp.is_visible('#nav a[href="/guides/"]'), 'le menu mobile s\'ouvre')
    check(mp.is_visible('#nav a.nav-ext'), 'menu mobile : lien Letsdle visible')
    b.close()

print()
print('ÉCHECS :', len(fails))
sys.exit(1 if fails else 0)
