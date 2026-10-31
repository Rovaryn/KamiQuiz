#!/usr/bin/env python3
"""Vidéos longues (plus d'une minute) pour TikTok, Reels et Shorts.

Deux formats, 1080x1920, avec une bande-son originale générée ici (tic-tac + carillon) :
  social/longues/quiz-NN-serie.mp4   8 questions, 5 s de réflexion chacune, puis la réponse expliquée (~77 s)
  social/longues/emoji-NN.mp4        5 personnages à deviner en emojis, révélés un par un (~75 s)
  social/longues/legendes.md         légendes prêtes à copier
"""
import html
import random
import shutil
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np
from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_social import FACES, DB, META  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'content'))
import dle as DLE  # noqa: E402

OUT = ROOT / 'social' / 'longues'
TMP = OUT / '_tmp'
W, H = 1080, 1920
SR = 44100
e = html.escape

QUIZ = ['naruto', 'onepiece', 'demonslayer', 'jjk', 'aot', 'dragonball', 'harrypotter', 'pokemon',
        'got', 'mha', 'frieren', 'chainsawman', 'spyfamily', 'hxh']
N_Q = 8
THINK, REVEAL, INTRO, OUTRO = 5, 3.5, 3.0, 5.0

CSS = f'''{FACES}
*{{margin:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;background:#07080f;color:#f2efe6;font-family:I;overflow:hidden;position:relative;
  display:flex;flex-direction:column;justify-content:center;padding:200px 80px 220px}}
.glow{{position:absolute;inset:-25% -35% auto auto;width:1200px;height:1200px;border-radius:50%;background:radial-gradient(closest-side,var(--c)55,transparent 70%)}}
.brand{{position:absolute;top:80px;left:80px;font:400 58px/1 B;letter-spacing:2px}}
.brand b{{color:#d4a843;font-weight:400}}
.step{{position:absolute;top:92px;right:80px;font:600 34px/1 I;color:#8f8c84}}
.step b{{color:#f2efe6}}
.bar{{position:absolute;top:170px;left:80px;right:80px;height:8px;border-radius:8px;background:#242839;overflow:hidden}}
.bar i{{display:block;height:100%;background:#d4a843}}
.chip{{display:inline-flex;align-items:center;gap:14px;font:600 32px/1 I;border:2px solid var(--c);border-radius:999px;padding:14px 26px;
  margin-bottom:36px;align-self:flex-start;position:relative}}
.chip i{{width:16px;height:16px;border-radius:50%;background:var(--c)}}
.q{{font:600 68px/1.22 P;margin-bottom:52px;position:relative}}
.o{{display:flex;align-items:center;gap:24px;border:2px solid #33384d;border-radius:22px;padding:26px 28px;margin-bottom:20px;
  font:500 40px/1.3 I;background:rgba(255,255,255,.03);position:relative}}
.o b{{flex:none;width:62px;height:62px;border-radius:14px;display:grid;place-items:center;background:#07080f;border:2px solid #33384d;font:600 30px/1 I;color:#8f8c84}}
.o.ok{{border-color:#4ade80;background:rgba(74,222,128,.13)}}
.o.ok b{{background:#4ade80;color:#052e14;border-color:#4ade80}}
.o.dim{{opacity:.3}}
.fb{{margin-top:26px;font:500 34px/1.45 I;color:#c9c5ba;border-left:6px solid var(--c);padding-left:26px;position:relative}}
.timer{{position:absolute;bottom:90px;left:50%;transform:translateX(-50%);width:150px;height:150px;border-radius:50%;border:8px solid #d4a843;
  display:grid;place-items:center;font:400 96px/1 B}}
.foot{{position:absolute;bottom:110px;left:80px;right:80px;text-align:center;font:600 36px/1 I;color:#d4a843}}
.big{{font:400 150px/.9 B;letter-spacing:2px;position:relative}}
.big b{{color:#d4a843;font-weight:400}}
.sub{{font:italic 400 56px/1.3 P;color:#c9c5ba;margin-top:36px;position:relative}}
.emos{{display:flex;flex-wrap:wrap;gap:26px;justify-content:center;margin:20px 0 60px;position:relative}}
.em{{width:190px;height:190px;border-radius:32px;border:3px dashed #33384d;display:grid;place-items:center;font:400 110px/1 sans-serif;color:#33384d}}
.em.on{{border-style:solid;border-color:#d4a843;background:rgba(212,168,67,.07)}}
.ans{{text-align:center;font:400 120px/1 B;color:#d4a843;position:relative}}
.ans small{{display:block;font:500 40px/1.3 I;color:#c9c5ba;margin-top:18px}}
.center{{text-align:center;align-items:center}}
'''


def page(inner, color='#d4a843', body_cls=''):
    return f'<html><head><style>{CSS}</style></head><body class="{body_cls}" style="--c:{color}"><div class="glow"></div>' \
           f'<div class="brand">KAMI<b>QUIZ</b></div>{inner}</body></html>'


def step(i, n):
    return f'<div class="step">Question <b>{i}</b> / {n}</div><div class="bar"><i style="width:{100 * i / n:.1f}%"></i></div>'


def q_frame(serie, q, i, n, count=None, reveal=False):
    color = DB[serie]['color']
    opts = ''
    for k, a in enumerate(q['a']):
        cls = (' ok' if k == q['c'] else ' dim') if reveal else ''
        opts += f'<div class="o{cls}"><b>{"ABCD"[k]}</b><span>{e(a)}</span></div>'
    extra = f'<p class="fb">{e(q["fb"])}</p>' if reveal and q.get('fb') else ''
    timer = f'<div class="timer">{count}</div>' if count is not None else ''
    return page(f'{step(i, n)}<div class="chip"><i></i>Quiz {e(META[serie]["name"])}</div>'
                f'<p class="q">{e(q["q"])}</p>{opts}{extra}{timer}', color)


def title_frame(top, big, sub, color='#d4a843'):
    return page(f'<p class="sub" style="margin:0 0 30px;color:#d4a843;font:600 40px/1 I">{e(top)}</p>'
                f'<div class="big">{big}</div><p class="sub">{e(sub)}</p>', color)


def emoji_frame(c, shown, i, n, reveal=False):
    boxes = ''.join(f'<div class="em{" on" if k < shown else ""}">{e(x) if k < shown else "?"}</div>' for k, x in enumerate(c['emo']))
    ans = (f'<div class="ans">{e(c["name"])}<small>{e(META[c["u"]]["name"])}</small></div>' if reveal
           else '<p class="sub" style="text-align:center;margin:0">Qui est-ce ?</p>')
    return page(f'{step(i, n).replace("Question", "Personnage")}<div class="chip" style="align-self:center"><i></i>Devine le personnage</div>'
                f'<div class="emos">{boxes}</div>{ans}<div class="foot">Réponds avant la révélation</div>',
                DB[c['u']]['color'], 'center')


# --------------------------------------------------------------------------- son original
def tone(freq, dur, vol=.35, decay=18):
    t = np.arange(int(SR * dur)) / SR
    return vol * np.sin(2 * np.pi * freq * t) * np.exp(-decay * t)


def tick():
    return tone(1500, .06, .25, 60) + tone(750, .06, .15, 60)


def chime():
    return np.pad(tone(880, .6, .3, 6), (0, int(SR * .2))) + np.pad(tone(1318.5, .6, .28, 6), (int(SR * .2), 0))


def whoosh():
    n = int(SR * .5)
    noise = np.random.default_rng(1).standard_normal(n) * np.linspace(0, .12, n) * np.linspace(1, 0, n) ** 2
    return noise


class Track:
    def __init__(self, seconds):
        self.a = np.zeros(int(SR * seconds) + SR)

    def add(self, at, snd):
        i = int(SR * at)
        self.a[i:i + len(snd)] += snd[:len(self.a) - i]

    def pad(self, seconds):
        """Nappe grave très discrète pour éviter le silence complet."""
        t = np.arange(len(self.a)) / SR
        self.a += .03 * np.sin(2 * np.pi * 110 * t) * (0.6 + 0.4 * np.sin(2 * np.pi * .25 * t))

    def save(self, path):
        x = np.clip(self.a, -1, 1)
        with wave.open(str(path), 'wb') as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(SR)
            w.writeframes((x * 32767).astype('<i2').tobytes())


# --------------------------------------------------------------------------- assemblage
def render(pg, html_str, path):
    pg.set_content(html_str)
    pg.evaluate('document.fonts.ready.then(() => true)')
    pg.screenshot(path=str(path))


def encode(frames, audio, out):
    lst = TMP / (out.stem + '.txt')
    lst.write_text(''.join(f"file '{f}'\nduration {d}\n" for f, d in frames) + f"file '{frames[-1][0]}'\n")
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', str(lst), '-i', str(audio),
                    '-vf', 'fps=30,format=yuv420p', '-c:v', 'libx264', '-preset', 'medium', '-crf', '21',
                    '-c:a', 'aac', '-b:a', '128k', '-shortest', '-movflags', '+faststart', str(out)], check=True)


def pick_questions(serie, rng):
    pool = [q for q in DB[serie]['q'] if q['d'] <= 3 and len(q['q']) <= 95 and max(len(a) for a in q['a']) <= 32
            and 20 <= len(q.get('fb', '')) <= 190]
    by_d = sorted(rng.sample(pool, N_Q), key=lambda q: q['d'])   # de plus en plus dur
    return by_d


def quiz_video(pg, n, serie, rng):
    qs = pick_questions(serie, rng)
    name = META[serie]['name']
    base = f'quiz-{n:02d}-{META[serie]["slug"]}'
    frames, t = [], 0.0
    total = INTRO + N_Q * (THINK + REVEAL) + OUTRO
    tr = Track(total)
    tr.pad(total)
    f = TMP / f'{base}-intro.png'
    render(pg, title_frame(f'{N_Q} questions', e(name).upper(), 'Compte tes bonnes réponses. 5 secondes par question.', DB[serie]['color']), f)
    frames.append((f, INTRO)); tr.add(0, whoosh()); t = INTRO
    for i, q in enumerate(qs, 1):
        tr.add(t, whoosh())
        for c in range(THINK, 0, -1):
            f = TMP / f'{base}-{i}-{c}.png'
            render(pg, q_frame(serie, q, i, N_Q, c), f)
            frames.append((f, 1.0)); tr.add(t, tick()); t += 1
        f = TMP / f'{base}-{i}-r.png'
        render(pg, q_frame(serie, q, i, N_Q, reveal=True), f)
        frames.append((f, REVEAL)); tr.add(t, chime()); t += REVEAL
    f = TMP / f'{base}-outro.png'
    render(pg, title_frame('Alors, ton score ?', 'X<b> / 8</b>',
                           f'Dis-le en commentaire. Le quiz complet ({len(DB[serie]["q"])} questions) est sur kamiquiz.com', DB[serie]['color']), f)
    frames.append((f, OUTRO)); tr.add(t, chime())
    wav = TMP / f'{base}.wav'
    tr.save(wav)
    encode(frames, wav, OUT / f'{base}.mp4')
    return base, serie, qs, total


def emoji_video(pg, n, chars):
    base = f'emoji-{n:02d}'
    per_emo, rev = 2.4, 3.5
    total = INTRO + sum(len(c['emo']) * per_emo + rev for c in chars) + OUTRO
    tr = Track(total)
    tr.pad(total)
    frames = []
    f = TMP / f'{base}-intro.png'
    render(pg, title_frame('Kamidle', 'DEVINE LE<br><b>PERSONNAGE</b>', f'{len(chars)} personnages cachés derrière des emojis. Combien tu en trouves ?'), f)
    frames.append((f, INTRO)); tr.add(0, whoosh()); t = INTRO
    for i, c in enumerate(chars, 1):
        tr.add(t, whoosh())
        for k in range(1, len(c['emo']) + 1):
            f = TMP / f'{base}-{i}-{k}.png'
            render(pg, emoji_frame(c, k, i, len(chars)), f)
            frames.append((f, per_emo))
            tr.add(t, tone(660 + 110 * k, .25, .25, 10))
            for s in (0.8, 1.6):
                tr.add(t + s, tick())
            t += per_emo
        f = TMP / f'{base}-{i}-r.png'
        render(pg, emoji_frame(c, len(c['emo']), i, len(chars), reveal=True), f)
        frames.append((f, rev)); tr.add(t, chime()); t += rev
    f = TMP / f'{base}-outro.png'
    render(pg, title_frame('Ton score en commentaire', 'X<b> / ' + str(len(chars)) + '</b>',
                           'Un nouveau personnage à deviner chaque jour sur kamiquiz.com/dle'), f)
    frames.append((f, OUTRO)); tr.add(t, chime())
    wav = TMP / f'{base}.wav'
    tr.save(wav)
    encode(frames, wav, OUT / f'{base}.mp4')
    return base, chars, total


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    TMP.mkdir(parents=True)
    rng = random.Random(20261027 + 60)
    quiz, emo = [], []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': W, 'height': H})
        for n, serie in enumerate(QUIZ, 1):
            quiz.append(quiz_video(pg, n, serie, rng))
            print('ok', quiz[-1][0], f'{quiz[-1][3]:.0f} s')
        # emojis : seulement les univers déjà publiés, 4 emojis minimum, univers variés
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
            print('ok', emo[-1][0], f'{emo[-1][2]:.0f} s')
        b.close()
    shutil.rmtree(TMP)

    L = ['# Vidéos longues : légendes prêtes à publier', '',
         "Toutes les vidéos dépassent une minute et ont une bande-son originale (tic-tac et carillon), libre de droits. "
         "Tu peux garder ce son ou ajouter ta voix par-dessus dans TikTok : lire les questions à voix haute rend la vidéo plus originale et plus regardée jusqu'au bout.", '']
    for base, serie, qs, total in quiz:
        m = META[serie]
        date = m.get('date', '2026-10-16')
        L += [f'## {base}.mp4 — {m["name"]} ({total:.0f} s)', '']
        if date > '2026-10-16':
            L += [f'**À publier à partir du {date[8:10]}/{date[5:7]}, jour de la mise en ligne du quiz.**', '']
        L += ['```', f'8 questions sur {m["name"]}, de la plus facile à la plus dure. Tu fais combien ? 👇', '',
              f'Le quiz complet ({len(DB[serie]["q"])} questions expliquées) est gratuit sur kamiquiz.com', '',
              f'#quiz #{m["name"].replace(" ", "").replace("×", "x").replace("-", "").lower()} #anime #manga #quizanime #animefr' if m['cat'] == 'anime'
              else f'#quiz #{m["name"].replace(" ", "").lower()} #culturepop #quizfr', '```', '',
              'Réponses : ' + ' · '.join(f'{i}. {"ABCD"[q["c"]]}' for i, q in enumerate(qs, 1)), '']
    for base, chars, total in emo:
        L += [f'## {base}.mp4 — Devine le personnage ({total:.0f} s)', '', '```',
              "5 personnages cachés derrière des emojis. Combien tu en trouves avant la révélation ? 👇", '',
              'Un nouveau personnage à deviner chaque jour sur kamiquiz.com/dle', '',
              '#kamidle #anime #devinelepersonnage #quiz #emojichallenge #animefr', '```', '',
              'Réponses : ' + ' · '.join(c['name'] for c in chars), '']
    (OUT / 'legendes.md').write_text('\n'.join(L), encoding='utf-8')


if __name__ == '__main__':
    main()
