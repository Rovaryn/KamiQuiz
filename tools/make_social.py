#!/usr/bin/env python3
"""Kit réseaux sociaux KamiQuiz.

Génère dans social/ :
  posts/NN-serie-question.png et NN-serie-reponse.png  (1080x1350, Instagram / Facebook)
  videos/NN-serie.mp4                                   (1080x1920, TikTok / Reels / Shorts, 9 s, sans son)
  legendes.md                                           (texte à copier pour chaque publication)
"""
import html
import json
import random
import shutil
import subprocess
import sys
from pathlib import Path
import base64
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'content'))
from series import SERIES  # noqa: E402

OUT = ROOT / 'social'
FONTS = ROOT / 'static' / 'assets' / 'fonts'


def F(name):
    return base64.b64encode((FONTS / name).read_bytes()).decode()

DB = json.loads((ROOT / 'data' / 'questions.json').read_text(encoding='utf-8'))
META = {s['key']: s for s in SERIES}
e = html.escape

PICK = ['frieren', 'naruto', 'onepiece', 'demonslayer', 'chainsawman', 'harrypotter', 'jjk', 'pokemon',
        'spyfamily', 'got', 'aot', 'dragonball', 'bluelock', 'breakingbad', 'zelda', 'deathnote']
VIDEOS = {'frieren', 'naruto', 'onepiece', 'chainsawman', 'jjk', 'pokemon', 'spyfamily', 'demonslayer'}

FACES = f'''
@font-face{{font-family:B;src:url(data:font/woff2;base64,{F('bebas-neue-latin-400-normal.woff2')})}}
@font-face{{font-family:P;font-weight:600;src:url(data:font/woff2;base64,{F('playfair-display-latin-600-normal.woff2')})}}
@font-face{{font-family:I;font-weight:500;src:url(data:font/woff2;base64,{F('inter-latin-500-normal.woff2')})}}
@font-face{{font-family:I;font-weight:600;src:url(data:font/woff2;base64,{F('inter-latin-600-normal.woff2')})}}
'''


def card(serie, q, w, h, reveal=False, count=None):
    color = DB[serie]['color']
    name = META[serie]['name']
    tall = h > 1500
    opts = ''
    for i, a in enumerate(q['a']):
        cls = ''
        if reveal:
            cls = ' ok' if i == q['c'] else ' dim'
        opts += f'<div class="o{cls}"><b>{"ABCD"[i]}</b><span>{e(a)}</span></div>'
    foot_extra = ''
    if reveal and q.get('fb'):
        foot_extra = f'<p class="fb">{e(q["fb"])}</p>'
    timer = ''
    if count is not None:
        timer = f'<div class="timer"><span>{count}</span></div>'
    top = 'La réponse' if reveal else 'Tu connais la réponse ?'
    return f'''<html><head><style>{FACES}
*{{margin:0;box-sizing:border-box}}
body{{width:{w}px;height:{h}px;background:#07080f;color:#f2efe6;font-family:I;overflow:hidden;position:relative;
  display:flex;flex-direction:column;justify-content:center;padding:{140 if tall else 80}px 80px}}
.glow{{position:absolute;inset:-30% -30% auto auto;width:1100px;height:1100px;border-radius:50%;
  background:radial-gradient(closest-side,{color}55,transparent 70%)}}
.brand{{position:absolute;top:{70 if tall else 56}px;left:80px;font:400 54px/1 B;letter-spacing:2px}}
.brand b{{color:#d4a843;font-weight:400}}
.chip{{display:inline-flex;align-items:center;gap:14px;font:600 30px/1 I;color:#f2efe6;border:2px solid {color}99;
  border-radius:999px;padding:14px 26px;margin-bottom:34px;align-self:flex-start;position:relative}}
.chip i{{width:16px;height:16px;border-radius:50%;background:{color}}}
.kicker{{font:600 30px/1 I;color:#d4a843;margin-bottom:22px;position:relative}}
.q{{font:600 {66 if tall else 58}px/1.25 P;margin-bottom:{52 if tall else 40}px;position:relative}}
.o{{display:flex;align-items:center;gap:24px;border:2px solid #33384d;border-radius:22px;padding:24px 28px;
  margin-bottom:18px;font:500 {38 if tall else 34}px/1.3 I;background:rgba(255,255,255,.03);position:relative}}
.o b{{flex:none;width:58px;height:58px;border-radius:14px;display:grid;place-items:center;background:#07080f;
  border:2px solid #33384d;font:600 28px/1 I;color:#8f8c84}}
.o.ok{{border-color:#4ade80;background:rgba(74,222,128,.12)}}
.o.ok b{{background:#4ade80;color:#052e14;border-color:#4ade80}}
.o.dim{{opacity:.35}}
.fb{{margin-top:22px;font:500 {32 if tall else 28}px/1.45 I;color:#c9c5ba;border-left:5px solid {color};padding-left:24px;position:relative}}
.foot{{position:absolute;bottom:{80 if tall else 56}px;left:80px;right:80px;display:flex;justify-content:space-between;
  align-items:center;font:600 32px/1 I;color:#8f8c84}}
.foot strong{{color:#d4a843}}
.timer{{position:absolute;top:{60 if tall else 46}px;right:80px;width:110px;height:110px;border-radius:50%;
  border:6px solid #d4a843;display:grid;place-items:center;font:400 72px/1 B;color:#f2efe6}}
</style></head><body><div class="glow"></div><div class="brand">KAMI<b>QUIZ</b></div>{timer}
<div class="chip"><i></i>Quiz {e(name)}</div><div class="kicker">{top}</div>
<p class="q">{e(q["q"])}</p>{opts}{foot_extra}
<div class="foot"><span>Réponds en commentaire</span><strong>kamiquiz.com</strong></div></body></html>'''


def choose(serie, rng):
    pool = [q for q in DB[serie]['q'] if q['d'] <= 2 and len(q['q']) <= 85 and max(len(a) for a in q['a']) <= 30
            and 20 <= len(q.get('fb', '')) <= 170]
    return rng.choice(pool)


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / 'posts').mkdir(parents=True)
    (OUT / 'videos').mkdir()
    tmp = OUT / '_frames'
    tmp.mkdir()
    rng = random.Random(20261027)
    items = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        post = b.new_page(viewport={'width': 1080, 'height': 1350})
        vert = b.new_page(viewport={'width': 1080, 'height': 1920})
        for n, serie in enumerate(PICK, 1):
            q = choose(serie, rng)
            slug = META[serie]['slug']
            base = f'{n:02d}-{slug}'
            for reveal, suffix in ((False, 'question'), (True, 'reponse')):
                post.set_content(card(serie, q, 1080, 1350, reveal))
                post.evaluate('document.fonts.ready.then(() => true)')
                post.screenshot(path=str(OUT / 'posts' / f'{base}-{suffix}.png'))
            if serie in VIDEOS:
                frames = []
                for c in (5, 4, 3, 2, 1):
                    f = tmp / f'{base}-{c}.png'
                    vert.set_content(card(serie, q, 1080, 1920, False, c))
                    vert.evaluate('document.fonts.ready.then(() => true)')
                    vert.screenshot(path=str(f))
                    frames.append((f, 1.2))
                f = tmp / f'{base}-r.png'
                vert.set_content(card(serie, q, 1080, 1920, True))
                vert.evaluate('document.fonts.ready.then(() => true)')
                vert.screenshot(path=str(f))
                frames.append((f, 3.0))
                lst = tmp / f'{base}.txt'
                lst.write_text(''.join(f"file '{fr}'\nduration {d}\n" for fr, d in frames) + f"file '{frames[-1][0]}'\n")
                subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', str(lst),
                                '-vf', 'fps=30,format=yuv420p', '-c:v', 'libx264', '-preset', 'medium', '-crf', '20',
                                '-movflags', '+faststart', str(OUT / 'videos' / f'{base}.mp4')], check=True)
            items.append((base, serie, q))
        b.close()
    shutil.rmtree(tmp)

    tags = {
        'anime': '#anime #manga #animefr #quiz #quizanime #otaku',
        'series': '#series #seriestv #quiz #netflix #seriesaddict',
        'films': '#cinema #film #quiz #saga',
        'jeux': '#jeuxvideo #gaming #quiz #gamer',
        'culture': '#culturegenerale #quiz #apprendre',
    }
    lines = ['# Légendes prêtes à publier', '',
             "Chaque publication a deux images : la question, puis la réponse (à poster en carrousel, réponse en 2e image). "
             "Les vidéos durent 9 secondes : 6 secondes de compte à rebours, puis la réponse. Elles sont muettes : ajoute un son tendance directement dans TikTok ou Instagram.", '']
    for base, serie, q in items:
        m = META[serie]
        has_video = serie in VIDEOS
        lines += [f'## {base} — {m["name"]}', '',
                  (f'**À publier à partir du {m["date"][8:10]}/{m["date"][5:7]}, jour de la mise en ligne du quiz.**\n\n' if m.get('date', '2026-10-16') > '2026-10-16' else '') +
                  f'Fichiers : `posts/{base}-question.png`, `posts/{base}-reponse.png`' + (f', `videos/{base}.mp4`' if has_video else ''), '',
                  '```',
                  f'{q["q"]}',
                  '',
                  'A, B, C ou D ? Réponds en commentaire avant de regarder la suite 👇',
                  '',
                  f'Le quiz {m["name"]} complet ({len(DB[serie]["q"])} questions expliquées) est sur kamiquiz.com, gratuit et sans inscription.',
                  '',
                  f'{tags[m["cat"]]} #{m["name"].replace(" ", "").replace("×", "x").replace("-", "").lower()}',
                  '```', '',
                  f'Bonne réponse : {"ABCD"[q["c"]]}, {q["a"][q["c"]]}.', '']
    (OUT / 'legendes.md').write_text('\n'.join(lines), encoding='utf-8')
    print(f'{len(items)} publications, {len(VIDEOS)} vidéos')


if __name__ == '__main__':
    main()
