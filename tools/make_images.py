#!/usr/bin/env python3
"""Génère og-image.png et les icônes PWA dans static/assets/img/ (rendu Chromium headless)."""
from pathlib import Path
import base64
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / 'static' / 'assets' / 'fonts'


def F(name):
    return base64.b64encode((FONTS / name).read_bytes()).decode()

OUT = ROOT / 'static' / 'assets' / 'img'
OUT.mkdir(parents=True, exist_ok=True)

FACES = f'''
@font-face{{font-family:B;src:url(data:font/woff2;base64,{F('bebas-neue-latin-400-normal.woff2')})}}
@font-face{{font-family:P;font-style:italic;src:url(data:font/woff2;base64,{F('playfair-display-latin-400-italic.woff2')})}}
@font-face{{font-family:I;font-weight:500;src:url(data:font/woff2;base64,{F('inter-latin-500-normal.woff2')})}}
'''

OG = f'''<html><head><style>{FACES}
*{{margin:0}}body{{width:1200px;height:630px;background:#07080f;color:#f2efe6;overflow:hidden;position:relative;font-family:I}}
.glow{{position:absolute;right:-220px;top:-260px;width:900px;height:900px;border-radius:50%;background:radial-gradient(closest-side,rgba(212,168,67,.28),transparent 70%)}}
.ring{{position:absolute;right:70px;top:170px;width:290px;height:290px;border-radius:50%;border:6px solid #d4a843}}
.ring:after{{content:"";position:absolute;inset:62px;border-radius:50%;border:3px solid rgba(212,168,67,.5)}}
.dot{{position:absolute;right:187px;top:287px;width:56px;height:56px;border-radius:50%;background:#d4a843}}
.t{{position:absolute;left:84px;top:150px;font:400 168px/0.86 B;letter-spacing:2px}}
.t b{{color:#d4a843;font-weight:400}}
.s{{position:absolute;left:88px;top:340px;font:italic 400 40px/1.3 P;color:#c9c5ba;width:620px}}
.f{{position:absolute;left:88px;bottom:70px;font:500 26px/1 I;color:#8f8c84}}
</style></head><body><div class="glow"></div><div class="ring"></div><div class="dot"></div>
<div class="t">KAMI<b>QUIZ</b></div><div class="s">Le quiz qui t'élève au rang de Kami</div>
<div class="f">Animés, séries, films, jeux vidéo et culture générale</div></body></html>'''

ICON = '''<html><head><style>*{margin:0}body{width:512px;height:512px;background:#07080f;display:grid;place-items:center}
.r{width:330px;height:330px;border-radius:50%;border:30px solid #d4a843;box-sizing:border-box;display:grid;place-items:center}
.d{width:110px;height:110px;border-radius:50%;background:#d4a843}</style></head>
<body><div class="r"><div class="d"></div></div></body></html>'''

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 1200, 'height': 630})
    pg.set_content(OG)
    pg.evaluate('document.fonts.ready.then(() => true)')
    pg.screenshot(path=str(OUT / 'og-image.png'))
    pg = b.new_page(viewport={'width': 512, 'height': 512})
    pg.set_content(ICON)
    pg.screenshot(path=str(OUT / 'icon-512.png'))
    pg = b.new_page(viewport={'width': 512, 'height': 512}, device_scale_factor=0.375)
    pg.set_content(ICON)
    pg.screenshot(path=str(OUT / 'icon-192.png'))
    b.close()
print('images ok')
