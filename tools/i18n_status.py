#!/usr/bin/env python3
"""Traductions des questions : avancement par série, et export des questions à traduire.

  python3 tools/i18n_status.py              # tableau d'avancement (langue : en)
  python3 tools/i18n_status.py naruto       # questions de Naruto encore à traduire (id | question | réponses | explication)
  python3 tools/i18n_status.py --lang en naruto
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'content'))
from i18n import qid  # noqa: E402

args = sys.argv[1:]
lang = 'en'
if '--lang' in args:
    i = args.index('--lang')
    lang = args[i + 1]
    del args[i:i + 2]
DB = json.loads((ROOT / 'data' / 'questions.json').read_text(encoding='utf-8'))


def load(key):
    f = ROOT / 'content' / lang / 'questions' / f'{key}.json'
    return json.loads(f.read_text(encoding='utf-8')) if f.exists() else {'cats': {}, 'ranks': [], 'q': {}}


if not args:
    tot = done = 0
    for key, s in DB.items():
        tr = load(key)
        ids = {qid(q['q']) for q in s['q']}
        n = len(ids & set(tr['q']))
        orphans = len(set(tr['q']) - ids)
        tot += len(ids)
        done += n
        flag = '' if n == len(ids) else ' ←'
        print(f'{key:15} {n:4}/{len(ids):<4}' + (f'  ({orphans} orphelines)' if orphans else '') + flag)
    print(f'TOTAL {done}/{tot}')
else:
    for key in args:
        s, tr = DB[key], load(key)
        print(f'# {key} — catégories : {list(s["cats"])} — rangs : {s.get("ranks")}')
        for q in s['q']:
            i = qid(q['q'])
            if i not in tr['q']:
                print(f'{i} | {q["cat"]} | {q["q"]} | {" ¦ ".join(q["a"])} | {q["fb"]}')
