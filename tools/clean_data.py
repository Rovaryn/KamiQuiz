#!/usr/bin/env python3
"""Nettoie la banque de questions KamiQuiz.

Entrée  : data/questions.src.json (fichier d'origine, jamais modifié)
Sortie  : data/questions.json     (banque propre, une seule clé "q" par série)
          data/clean_report.json  (ce qui a été corrigé)
"""
import json
import re
import difflib
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / 'data' / 'questions.src.json'
OUT = ROOT / 'data' / 'questions.json'
REPORT = ROOT / 'data' / 'clean_report.json'

# Terminologie française officielle EA Sports FC (préférence du propriétaire du site)
EAFC_TERMS = [
    (r'\bSquad Building Challenges?\b', "Défi Création d'Équipe"),
    (r'\bSBCs?\b', 'DCE'),
    (r'\bTeam of the Week\b', 'Équipe de la Semaine'),
    (r'\bTOTW\b', 'EDSM'),
    (r'\bFUT Coins\b', 'Pièces FUT'),
    (r'\bCoins FUT\b', 'Pièces FUT'),
    (r'\bCoins\b', 'Pièces FUT'),
    (r'\bCoin\b', 'Pièce FUT'),
    (r'\bCareer Mode\b', 'Mode Carrière'),
    (r'\bChemistry\b', 'Chimie'),
    (r'\bChemie\b', 'Chimie'),
]

# Icônes pour les catégories ajoutées (les catégories d'origine gardent la leur)
ICON_HINTS = [
    ('citation', '💬'), ('casting', '🎬'), ('série', '📺'), ('finale', '🏁'),
    ('lieu', '🗺️'), ('géo', '🗺️'), ('créature', '🐉'), ('arme', '🗡️'),
    ('art', '🎨'), ('acteur', '🎭'), ('anim', '🎞️'), ('france', '🇫🇷'),
    ('monde', '🌍'), ('gameplay', '🎮'), ('mécanique', '⚙️'), ('licence', '📜'),
    ('économ', '💰'), ('guerre', '⚔️'), ('histoire', '📖'), ('attaque', '💥'),
    ('pokédex', '📕'), ('évolution', '🧬'), ('lore', '📜'), ('boxe', '🥊'),
    ('sport', '🏅'), ('technolog', '🔧'), ('gardien', '🚀'), ('panther', '🐾'),
    ('donjon', '🏰'), ('événement', '📅'),
]
MIN_KEEP = 3

# Questions retirées à la main : prémisse fausse, réponse contredite par l'explication,
# ou doublon d'une version mieux formulée.
DROP = {
    "Qu'est-ce qu'un DCE dans FUT (version française) ?",
    "Quel agent numérique gère l'économie de FUT selon les fans et les critiques de la communauté ?",
    "Quel est le prix en euros d'un pack Ultimate Draft dans EA Sports FC ?",
}  # une catégorie « parasite » avec moins de 3 questions va dans « Divers »


# Corrections de formulation (question ambiguë -> une seule bonne réponse possible)
REWORD = {
    "Quel est le nom du bateau de l'équipage de Luffy ?": "Quel est le nom du premier bateau de l'équipage de Luffy ?",
}


def norm(text):
    return re.sub(r'\W+', '', text.lower())


def apply_terms(text):
    for pat, rep in EAFC_TERMS:
        text = re.sub(pat, rep, text)
    # « Pièces FUT FUT » si la source disait « Coins FUT » dans un autre ordre
    return text.replace('Pièces FUT FUT', 'Pièces FUT')


def icon_for(cat):
    low = cat.lower()
    for hint, icon in ICON_HINTS:
        if hint in low:
            return icon
    return '✦'


def load_new_series():
    """Convertit content/new_series.py au format de la banque, avec un ordre de réponses mélangé de façon stable."""
    import random
    import sys
    sys.path.insert(0, str(ROOT / 'content'))
    from new_series import NEW_SERIES
    out = {}
    for serie in NEW_SERIES:
        rng = random.Random(serie['key'])
        qs = []
        for cat, d, text, answers, correct, fb in serie['q']:
            order = list(range(4))
            rng.shuffle(order)
            qs.append({'q': text, 'a': [answers[i] for i in order], 'c': order.index(correct), 'cat': cat, 'd': d, 'fb': fb})
        out[serie['key']] = {'name': serie['name'], 'color': serie['color'], 'ranks': serie['ranks'], 'sw': [],
                             'cats': {c: {'i': i} for c, i in serie['cats'].items()}, 'q': qs}
    return out


def main():
    import sys
    sys.path.insert(0, str(ROOT / 'content'))
    from corrections import FIX as CORR_ALL
    global CORR, used_fix
    CORR, used_fix = CORR_ALL, set()
    src = json.loads(SRC.read_text(encoding='utf-8'))
    for key, serie in load_new_series().items():
        assert key not in src, key
        src[key] = serie
    report = defaultdict(list)
    out = {}

    for slug, serie in src.items():
        pool = list(serie.get('q', [])) + list(serie.get('qs', []))
        if serie.get('q') and serie.get('qs'):
            report['fusion_q_qs'].append(f"{slug}: {len(serie['q'])} + {len(serie['qs'])}")

        # 1) Terminologie EAFC
        if slug == 'eafc':
            for q in pool:
                before = json.dumps(q, ensure_ascii=False)
                q['q'] = apply_terms(q['q'])
                q['a'] = [apply_terms(a) for a in q['a']]
                q['fb'] = apply_terms(q['fb'])
                if json.dumps(q, ensure_ascii=False) != before:
                    report['eafc_terminologie'].append(q['q'][:90])

        before_drop = len(pool)
        pool = [q for q in pool if q.get('q', '').strip() not in DROP]
        for _ in range(before_drop - len(pool)):
            report['retirees_manuellement'].append(slug)

        # Relecture : corrections et retraits (content/corrections.py)
        fixes = CORR.get(slug, {})
        corrected = []
        for q in pool:
            key = q.get('q', '').strip()
            if key in fixes:
                used_fix.add((slug, key))
                if fixes[key] is None:
                    report['retirees_relecture'].append(f'{slug}: {key[:90]}')
                    continue
                q = {**q, **fixes[key]}
                report['corrigees_relecture'].append(f'{slug}: {key[:90]}')
            corrected.append(q)
        pool = corrected

        for q in pool:
            if q.get('q', '').strip() in REWORD:
                q['q'] = REWORD[q['q'].strip()]
                report['reformulees'].append(f"{slug}: {q['q']}")

        # 2) Doublons (texte identique ou quasi identique)
        kept = []
        for q in pool:
            n = norm(q['q'])
            right = norm(q['a'][q['c']]) if q.get('a') and isinstance(q.get('c'), int) and 0 <= q['c'] < len(q['a']) else ''
            dup = next((k for k in kept
                        if norm(k['q']) == n
                        or (difflib.SequenceMatcher(None, norm(k['q']), n).ratio() > 0.9
                            and norm(k['a'][k['c']]) == right)), None)
            if dup:
                report['doublons_retires'].append(f"{slug}: {q['q'][:90]}")
                continue
            kept.append(q)

        # 3) Validation stricte de chaque question
        valid = []
        for q in kept:
            problems = []
            if not isinstance(q.get('a'), list) or len(q['a']) != 4:
                problems.append('pas 4 réponses')
            elif len({a.strip().lower() for a in q['a']}) < 4:
                problems.append('réponses en double')
            if not isinstance(q.get('c'), int) or not 0 <= q['c'] < 4:
                problems.append('index de bonne réponse invalide')
            if q.get('d') not in (1, 2, 3, 4):
                problems.append('difficulté invalide')
            if not q.get('q', '').strip():
                problems.append('question vide')
            if problems:
                report['questions_rejetees'].append(f"{slug}: {q.get('q','')[:80]} ({', '.join(problems)})")
                continue
            q['q'] = q['q'].strip()
            q['a'] = [a.strip() for a in q['a']]
            q['fb'] = q.get('fb', '').strip()
            valid.append(q)

        # 4) Catégories : renommer le cas Bleach, intégrer ou regrouper les catégories parasites
        cats = {}
        for name, val in serie.get('cats', {}).items():
            icon = val.get('i') if isinstance(val, dict) else val
            while isinstance(icon, dict):          # certaines séries avaient {'i': {'i': '🦸'}}
                icon = icon.get('i')
            if not isinstance(icon, str):
                icon = icon_for(name)
            if icon != (val.get('i') if isinstance(val, dict) else None):
                report['icones_reparees'].append(f'{slug}: {name}')
            cats[name] = {'i': icon}
        if slug == 'bleach' and 'Zanpakuto (Sabre Spirituel)' in cats:
            cats = {('Zanpakuto' if k == 'Zanpakuto (Sabre Spirituel)' else k): v for k, v in cats.items()}
            for q in valid:
                if q['cat'] == 'Zanpakuto (Sabre Spirituel)':
                    q['cat'] = 'Zanpakuto'
        counts = Counter(q['cat'] for q in valid)
        for cat, n in counts.items():
            if cat in cats:
                continue
            if n >= MIN_KEEP:
                cats[cat] = {'i': icon_for(cat)}
                report['categories_ajoutees'].append(f'{slug}: {cat} ({n})')
            else:
                for q in valid:
                    if q['cat'] == cat:
                        q['cat'] = 'Divers'
                report['categories_regroupees_divers'].append(f'{slug}: {cat} ({n})')
        if any(q['cat'] == 'Divers' for q in valid):
            cats['Divers'] = {'i': '🎲'}
        # On retire les catégories déclarées mais vides
        used = {q['cat'] for q in valid}
        cats = {k: v for k, v in cats.items() if k in used}

        out[slug] = {
            'name': serie['name'],
            'color': serie['color'],
            'ranks': serie.get('ranks', []),
            'sw': serie.get('sw', []),
            'cats': cats,
            'q': valid,
        }

    unused = [(s_, k) for s_, d in CORR.items() for k in d if (s_, k) not in used_fix]
    if unused:
        raise SystemExit('Corrections sans question correspondante (texte à vérifier) :\n' + '\n'.join(f'  {s_}: {k}' for s_, k in unused))
    OUT.write_text(json.dumps(out, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding='utf-8')
    total = sum(len(s['q']) for s in out.values())
    print(f'{len(out)} séries, {total} questions propres')
    for k, v in report.items():
        print(f'  {k}: {len(v)}')


if __name__ == '__main__':
    main()
