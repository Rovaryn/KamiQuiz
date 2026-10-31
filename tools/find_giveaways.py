#!/usr/bin/env python3
"""Repère les questions dont la bonne réponse est (presque) écrite dans la question.

Exemple : « De quel clan est Hinata Hyûga ? » -> « Clan Hyûga ».
Usage : python3 tools/find_giveaways.py [série]
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STOP = {'clan', 'village', 'pays', 'mode', 'style', 'fruit', 'demon', 'magie', 'equipe', 'saison', 'episode', 'grand', 'grande',
        'premier', 'premiere', 'dans', 'avec', 'pour', 'sans', 'nom', 'est', 'les', 'des', 'une', 'son', 'sa', 'ses', 'the', 'and',
        'of', 'de', 'du', 'la', 'le', 'un', 'et', 'en', 'au', 'aux', 'par', 'sur', 'qui', 'que', 'quel', 'quelle', 'technique',
        'royaume', 'ile', 'guilde', 'ville', 'groupe', 'saga', 'film', 'jeu', 'serie', 'arc', 'tome', 'chapitre', 'personnage',
        'mage', 'dragon', 'slayer', 'devil', 'haki', 'no', 'mi', 'jutsu', 'tous', 'tout', 'toute', 'plus', 'tres', 'deux', 'trois'}


def words(t):
    t = unicodedata.normalize('NFD', t.lower())
    t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    return [w for w in re.findall(r"[a-z0-9]+", t) if len(w) >= 4 and w not in STOP]


def giveaways(db, only=None):
    out = []
    for key, serie in db.items():
        if only and key != only:
            continue
        for q in serie['q']:
            good = set(words(q['a'][q['c']]))
            if not good:
                continue
            qw = set(words(q['q']))
            hit = good & qw
            others = [set(words(a)) & qw for i, a in enumerate(q['a']) if i != q['c']]
            # la bonne réponse partage un mot avec la question, et aucune mauvaise réponse ne le fait autant
            if hit and len(hit) >= max((len(o) for o in others), default=0) + (0 if len(hit) == len(good) else 1):
                out.append((key, q['q'], q['a'][q['c']], sorted(hit)))
    return out


if __name__ == '__main__':
    db = json.loads((ROOT / 'data' / 'questions.json').read_text(encoding='utf-8'))
    res = giveaways(db, sys.argv[1] if len(sys.argv) > 1 else None)
    for key, q, a, hit in res:
        print(f'{key:14} | {q} -> {a}   [{", ".join(hit)}]')
    print(len(res), 'questions suspectes')
