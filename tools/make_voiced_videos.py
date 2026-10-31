#!/usr/bin/env python3
"""Vidéos longues narrées par une voix de synthèse (Piper, voix SIWIS, CC BY 4.0).

Même contenu que make_long_videos.py, avec en plus une narration :
  quiz  : la voix lit la question, laisse 5 s de compte à rebours, puis annonce la bonne réponse
  emoji : la voix annonce chaque personnage puis révèle son nom et son univers
Sortie : social/narrees/*.mp4 et social/narrees/legendes.md
"""
import random
import re
import shutil
import sys
import wave
from pathlib import Path

import numpy as np
from piper import PiperVoice, SynthesisConfig
from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent))
import make_long_videos as LV  # noqa: E402
from make_long_videos import DB, META, DLE, SR, Track, tick, chime, whoosh, tone, render, encode  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'social' / 'narrees'
LV.TMP = TMP = OUT / '_tmp'
VOICE = ROOT / 'tools' / 'voix' / 'siwis' / 'fr_FR-siwis-medium.onnx'
_voice = PiperVoice.load(str(VOICE), config_path=str(VOICE) + '.json')
CFG = SynthesisConfig(length_scale=0.95)
GAP = 0.35


def say(text):
    """Synthèse en 44,1 kHz, renvoie le signal (numpy)."""
    chunks = []
    for ch in _voice.synthesize(text, syn_config=CFG):
        chunks.append(ch.audio_float_array)
    x = np.concatenate(chunks) if chunks else np.zeros(1)
    src = _voice.config.sample_rate
    n = int(len(x) * SR / src)
    return np.interp(np.linspace(0, len(x) - 1, n), np.arange(len(x)), x) * 0.9


def dur(sig):
    return len(sig) / SR


def spoken(t):
    """Petits ajustements pour la prononciation."""
    t = t.replace('×', 'x').replace('kamiquiz.com', 'Kami Quiz point com').replace('KamiQuiz', 'Kami Quiz')
    t = re.sub(r'\s*\(([^)]*)\)', r', \1,', t)
    return t


def quiz_video(pg, n, serie, rng):
    qs = LV.pick_questions(serie, rng)
    name = META[serie]['name']
    color = DB[serie]['color']
    base = f'quiz-{n:02d}-{META[serie]["slug"]}'
    plan = []   # (image html, durée, [(décalage, son)])
    v = say(spoken(f'{len(qs)} questions sur {name}, de la plus facile à la plus dure. Compte tes points !'))
    plan.append((LV.title_frame(f'{len(qs)} questions', name.upper(), 'Compte tes bonnes réponses. 5 secondes par question.', color),
                 max(3.0, dur(v) + 0.8), [(0, whoosh()), (0.3, v)]))
    for i, q in enumerate(qs, 1):
        vq = say(spoken(f'Question {i}. {q["q"]}'))
        plan.append((LV.q_frame(serie, q, i, len(qs)), dur(vq) + 0.6, [(0, whoosh()), (0.2, vq)]))
        for c in range(5, 0, -1):
            plan.append((LV.q_frame(serie, q, i, len(qs), c), 1.0, [(0, tick())]))
        va = say(spoken(f'Réponse {"ABCD"[q["c"]]} : {q["a"][q["c"]]} !'))
        plan.append((LV.q_frame(serie, q, i, len(qs), reveal=True), max(3.5, dur(va) + 2.2), [(0, chime()), (0.45, va)]))
    vo = say(spoken(f'Alors, combien tu en as eu sur {len(qs)} ? Dis-le en commentaire ! Le quiz complet est gratuit sur kamiquiz.com.'))
    plan.append((LV.title_frame('Alors, ton score ?', f'X<b> / {len(qs)}</b>',
                                f'Dis-le en commentaire. Le quiz complet ({len(DB[serie]["q"])} questions) est sur kamiquiz.com', color),
                 dur(vo) + 1.5, [(0, chime()), (0.5, vo)]))
    total = build(pg, base, plan)
    return base, serie, qs, total


def emoji_video(pg, n, chars):
    base = f'emoji-{n:02d}'
    plan = []
    v = say(f'Devine le personnage ! {len(chars)} personnages sont cachés derrière ces emojis. Réponds avant la révélation.')
    plan.append((LV.title_frame('Kamidle', 'DEVINE LE<br><b>PERSONNAGE</b>', f'{len(chars)} personnages cachés derrière des emojis. Combien tu en trouves ?'),
                 dur(v) + 0.8, [(0, whoosh()), (0.3, v)]))
    for i, c in enumerate(chars, 1):
        vi = say(f'Personnage numéro {i}.')
        for k in range(1, len(c['emo']) + 1):
            snd = [(0, tone(660 + 110 * k, .25, .25, 10)), (0.9, tick()), (1.7, tick())]
            if k == 1:
                snd = [(0, whoosh()), (0.1, vi)] + snd[1:]
            plan.append((LV.emoji_frame(c, k, i, len(chars)), max(2.4, dur(vi) + 0.6) if k == 1 else 2.4, snd))
        vr = say(spoken(f"C'était {c['name']}, de {META[c['u']]['name']} !"))
        plan.append((LV.emoji_frame(c, len(c['emo']), i, len(chars), reveal=True), max(3.5, dur(vr) + 1.4), [(0, chime()), (0.4, vr)]))
    vo = say(spoken('Combien tu en as trouvé ? Écris ton score en commentaire. Un nouveau personnage à deviner chaque jour sur kamiquiz.com.'))
    plan.append((LV.title_frame('Ton score en commentaire', f'X<b> / {len(chars)}</b>', 'Un nouveau personnage à deviner chaque jour sur kamiquiz.com/dle'),
                 dur(vo) + 1.5, [(0, chime()), (0.5, vo)]))
    total = build(pg, base, plan)
    return base, chars, total


def build(pg, base, plan):
    total = sum(d for _, d, _ in plan)
    tr = Track(total)
    tr.pad(total)
    frames, t = [], 0.0
    cache = {}
    for k, (html_str, d, sounds) in enumerate(plan):
        f = cache.get(html_str)
        if f is None:
            f = TMP / f'{base}-{k}.png'
            render(pg, html_str, f)
            cache[html_str] = f
        frames.append((f, round(d, 3)))
        for off, snd in sounds:
            tr.add(t + off, snd)
        t += d
    wav = TMP / f'{base}.wav'
    tr.save(wav)
    encode(frames, wav, OUT / f'{base}.mp4')
    return total


def main():
    only = sys.argv[1:]  # ex. : python3 tools/make_voiced_videos.py naruto
    if OUT.exists() and not only:
        shutil.rmtree(OUT)
    TMP.mkdir(parents=True, exist_ok=True)
    rng = random.Random(20261027 + 60)   # même tirage que les vidéos sans voix
    quiz, emo = [], []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': LV.W, 'height': LV.H})
        for n, serie in enumerate(LV.QUIZ, 1):
            if only and serie not in only:
                LV.pick_questions(serie, rng)
                continue
            quiz.append(quiz_video(pg, n, serie, rng))
            print('ok', quiz[-1][0], f'{quiz[-1][3]:.0f} s', flush=True)
        if not only:
            cands = [c for c in DLE.CHARS if len(c['emo']) >= 4 and META[c['u']].get('date', '2026-10-16') <= '2026-10-27']
            rng.shuffle(cands)
            used = set()
            for n in range(1, 5):
                pick, seen_u = [], set()
                for c in cands:
                    if c['id'] in used or c['u'] in seen_u:
                        continue
                    pick.append(c); seen_u.add(c['u']); used.add(c['id'])
                    if len(pick) == 5:
                        break
                emo.append(emoji_video(pg, n, pick))
                print('ok', emo[-1][0], f'{emo[-1][2]:.0f} s', flush=True)
        b.close()
    shutil.rmtree(TMP)
    if only:
        return
    L = ['# Vidéos narrées : légendes prêtes à publier', '',
         "Ces vidéos ont une voix de synthèse qui lit les questions et annonce les réponses. Elles dépassent toutes une minute.", '',
         "**Crédit à laisser** (la licence de la voix demande de citer sa source) : ajoute en fin de légende « Voix : SIWIS, CC BY 4.0 ». "
         "C'est déjà fait dans les légendes ci-dessous.", '',
         "**Sur TikTok**, au moment de publier, active l'option qui indique un contenu généré par IA. La voix est synthétique : TikTok demande de le signaler.", '']
    for base, serie, qs, total in quiz:
        m = META[serie]
        date = m.get('date', '2026-10-16')
        tag = m["name"].replace(" ", "").replace("×", "x").replace("-", "").lower()
        L += [f'## {base}.mp4 — {m["name"]} ({total:.0f} s)', '']
        if date > '2026-10-16':
            L += [f'**À publier à partir du {date[8:10]}/{date[5:7]}, jour de la mise en ligne du quiz.**', '']
        L += ['```', f'8 questions sur {m["name"]}, de la plus facile à la plus dure. Tu fais combien ? 👇', '',
              f'Le quiz complet ({len(DB[serie]["q"])} questions expliquées) est gratuit sur kamiquiz.com', '',
              (f'#quiz #{tag} #anime #manga #quizanime #animefr' if m['cat'] == 'anime' else f'#quiz #{tag} #culturepop #quizfr'),
              '', 'Voix : SIWIS, CC BY 4.0', '```', '',
              'Réponses : ' + ' · '.join(f'{i}. {"ABCD"[q["c"]]}' for i, q in enumerate(qs, 1)), '']
    for base, chars, total in emo:
        L += [f'## {base}.mp4 — Devine le personnage ({total:.0f} s)', '', '```',
              "5 personnages cachés derrière des emojis. Combien tu en trouves avant la révélation ? 👇", '',
              'Un nouveau personnage à deviner chaque jour sur kamiquiz.com/dle', '',
              '#kamidle #anime #devinelepersonnage #quiz #emojichallenge #animefr', '', 'Voix : SIWIS, CC BY 4.0', '```', '',
              'Réponses : ' + ' · '.join(c['name'] for c in chars), '']
    (OUT / 'legendes.md').write_text('\n'.join(L), encoding='utf-8')


if __name__ == '__main__':
    main()
