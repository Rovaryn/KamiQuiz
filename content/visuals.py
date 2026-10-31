"""Visuels originaux des séries (SVG dessinés à la main, aucune image protégée).

Chaque série reçoit une composition abstraite dans sa couleur : un fond nuit (#07080f),
un halo, une trame de points et un motif géométrique évocateur (des remparts concentriques,
un cercle de transmutation, des cartes à jouer…). Les motifs restent volontairement
génériques : aucun personnage, logo ou visuel officiel n'est reproduit.

visual_svg(key, color) renvoie le SVG complet (viewBox 1600 × 900, format 16:9).
"""
import math
import random

W, H = 1600, 900
CX, CY = 1130, 450          # centre du motif, décalé à droite pour laisser respirer le texte
GOLD, PAPER = '#d4a843', '#f2efe6'


def f(v):
    return f'{v:.1f}'.rstrip('0').rstrip('.')


def pts(seq):
    return ' '.join(f'{f(x)},{f(y)}' for x, y in seq)


def polar(r, a, cx=CX, cy=CY):
    return cx + r * math.cos(a), cy + r * math.sin(a)


def circle(r, cx=CX, cy=CY, **k):
    return f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}"{attrs(k)}/>'


def attrs(k):
    return ''.join(f' {a.replace("_", "-")}="{v}"' for a, v in k.items())


def poly(seq, closed=True, **k):
    tag = 'polygon' if closed else 'polyline'
    return f'<{tag} points="{pts(seq)}"{attrs(k)}/>'


def path(d, **k):
    return f'<path d="{d}"{attrs(k)}/>'


def star(cx, cy, r1, r2, n=5, rot=-math.pi / 2):
    return [polar(r1 if i % 2 == 0 else r2, rot + i * math.pi / n, cx, cy) for i in range(2 * n)]


def ngon(cx, cy, r, n, rot=-math.pi / 2):
    return [polar(r, rot + i * 2 * math.pi / n, cx, cy) for i in range(n)]


def sparkle(cx, cy, r):
    """Petite étoile à quatre branches."""
    return poly(star(cx, cy, r, r * .22, 4, 0))


# --------------------------------------------------------------------------- motifs
# Chaque fonction reçoit la couleur de la série et renvoie le contenu du motif (traits par défaut).

def m_spiral(c):
    seq = [polar(6 + 13 * t, t + 0.3) for t in [i / 12 for i in range(0, 12 * 21)]]
    out = poly(seq, closed=False, stroke_width=10, stroke_linecap='round')
    out += circle(330, stroke_width=2, opacity=.35) + circle(380, stroke_width=1, opacity=.2, stroke_dasharray='4 14')
    out += path(f'M{f(CX-40)},{f(CY-300)} q60,-70 140,-40 q-50,60 -140,40z', fill=GOLD, stroke='none', opacity=.9)
    return out


def m_waves(c):
    out = circle(150, cx=CX + 60, cy=CY - 70, fill=GOLD, stroke='none', opacity=.95)
    for i in range(18):
        a = math.pi + i * math.pi / 17
        x1, y1 = polar(180, a, CX + 60, CY - 70)
        x2, y2 = polar(250 + (i % 2) * 50, a, CX + 60, CY - 70)
        out += f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" stroke="{GOLD}" stroke-width="5" stroke-linecap="round" opacity=".7"/>'
    for j in range(5):
        y = CY + 60 + j * 52
        d = f'M{f(CX-480)},{y}' + ''.join(f' q50,{-34 + j * 3} 100,0 t100,0' for _ in range(5))
        out += path(d, stroke_width=9 - j, opacity=f(1 - j * .16), stroke_linecap='round')
    return out


def m_walls(c):
    out = ''
    for r, w in ((360, 26), (250, 22), (145, 18)):
        out += circle(r, stroke_width=w, stroke_dasharray=f'{f(r * .09)} {f(r * .035)}')
        out += circle(r - w, stroke_width=2, opacity=.4)
    out += circle(52, fill=GOLD, stroke='none')
    return out


def m_checker(c):
    out = ''
    n, s = 9, 62
    for i in range(n):
        for j in range(n):
            if (i + j) % 2:
                continue
            x, y = CX - n * s / 2 + i * s, CY - n * s / 2 + j * s
            dist = math.hypot(i - n / 2 + .5, j - n / 2 + .5)
            op = max(0, 1 - dist / 5.2)
            if op > .05:
                out += f'<rect x="{f(x)}" y="{f(y)}" width="{s}" height="{s}" fill="currentColor" stroke="none" opacity="{f(op * .85)}"/>'
    out += path(f'M{f(CX-420)},{f(CY+220)} C{f(CX-200)},{f(CY-260)} {f(CX+220)},{f(CY+260)} {f(CX+430)},{f(CY-210)}',
                stroke=GOLD, stroke_width=16, stroke_linecap='round')
    out += path(f'M{f(CX-380)},{f(CY+270)} C{f(CX-160)},{f(CY-190)} {f(CX+240)},{f(CY+320)} {f(CX+440)},{f(CY-140)}',
                stroke=PAPER, stroke_width=4, stroke_linecap='round', opacity=.55)
    return out


def m_crescent(c):
    out = ('<mask id="lune"><rect width="1600" height="900" fill="#fff"/>'
           f'<circle cx="{f(CX+120)}" cy="{f(CY-60)}" r="270" fill="#000"/></mask>')
    out += circle(320, fill='currentColor', stroke='none', mask='url(#lune)')
    out += circle(320, stroke=GOLD, stroke_width=3, opacity='.35', stroke_dasharray='3 12')
    for i in range(3):
        y = CY - 180 + i * 140
        out += f'<line x1="{f(CX-120)}" y1="{f(y+120)}" x2="{f(CX+420)}" y2="{f(y-90)}" stroke="{GOLD}" stroke-width="{6 - i * 1.5}" stroke-linecap="round" opacity=".8"/>'
    return out


def m_seal(c):
    out = circle(340, stroke_width=6) + circle(300, stroke_width=2, opacity=.5)
    for i in range(72):
        a = i * math.pi / 36
        r2 = 318 if i % 6 else 285
        x1, y1 = polar(340, a)
        x2, y2 = polar(r2, a)
        out += f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" stroke-width="3"/>'
    out += poly([ngon(CX, CY, 260, 5)[i * 2 % 5] for i in range(5)], stroke=GOLD, stroke_width=5)
    out += circle(110, stroke_width=4) + circle(36, fill='currentColor', stroke='none')
    return out


def m_burst(c):
    out = ''
    for i in range(28):
        a = i * math.pi / 14
        r = 400 if i % 2 else 300
        x, y = polar(r, a)
        out += f'<line x1="{f(CX)}" y1="{f(CY)}" x2="{f(x)}" y2="{f(y)}" stroke-width="{3 if i % 2 else 6}" opacity="{.5 if i % 2 else .9}"/>'
    out += poly(star(CX, CY, 190, 80), fill='#07080f', stroke=GOLD, stroke_width=10, stroke_linejoin='round')
    return out


def m_flames(c):
    out = ''
    for k, (dx, h, w, op) in enumerate(((0, 420, 190, 1), (-150, 300, 120, .7), (160, 330, 130, .75), (-60, 220, 80, .9))):
        x, y = CX + dx, CY + 230
        d = (f'M{f(x)},{f(y)} C{f(x-w)},{f(y-h*.35)} {f(x-w*.2)},{f(y-h*.7)} {f(x+w*.15)},{f(y-h)} '
             f'C{f(x+w*.1)},{f(y-h*.65)} {f(x+w)},{f(y-h*.45)} {f(x)},{f(y)}z')
        out += path(d, stroke=GOLD if k == 3 else 'currentColor', stroke_width=6, stroke_linejoin='round', opacity=f(op))
    rng = random.Random('braises')
    for _ in range(14):
        x, y = CX + rng.uniform(-300, 300), CY + rng.uniform(-320, 100)
        out += circle(rng.uniform(3, 8), cx=x, cy=y, fill=GOLD, stroke='none', opacity=f(rng.uniform(.4, .9)))
    return out


def m_suits(c):
    s = 1.0
    spade = 'M0,-90 C40,-40 90,-10 60,40 C40,70 10,55 5,35 L20,90 L-20,90 L-5,35 C-10,55 -40,70 -60,40 C-90,-10 -40,-40 0,-90z'
    heart = 'M0,80 C-60,30 -95,0 -80,-40 C-65,-80 -15,-75 0,-40 C15,-75 65,-80 80,-40 C95,0 60,30 0,80z'
    diamond = 'M0,-95 L70,0 L0,95 L-70,0z'
    club = ('M0,-90 a42,42 0 1,1 -1,0z M-50,-10 a42,42 0 1,1 -1,0z M50,-10 a42,42 0 1,1 -1,0z '
            'M-12,10 L-25,90 L25,90 L12,10z')
    out = ''
    for (dx, dy, d, col) in ((0, -190, spade, 'currentColor'), (190, 0, heart, GOLD), (0, 190, club, 'currentColor'), (-190, 0, diamond, GOLD)):
        out += f'<path transform="translate({f(CX+dx)} {f(CY+dy)}) scale({s})" d="{d}" stroke="{col}" stroke-width="7" stroke-linejoin="round"/>'
    out += circle(300, stroke_width=2, opacity=.35, stroke_dasharray='2 12')
    return out


def m_apple(c):
    out = ''
    rng = random.Random('encre')
    for i in range(9):
        x = CX - 420 + i * 105 + rng.uniform(-20, 20)
        h = rng.uniform(120, 300)
        out += f'<line x1="{f(x)}" y1="0" x2="{f(x)}" y2="{f(h)}" stroke-width="{f(rng.uniform(3, 9))}" stroke-linecap="round" opacity=".55"/>'
        out += circle(rng.uniform(6, 13), cx=x, cy=h + 22, fill='currentColor', stroke='none', opacity='.7')
    ax, ay = CX + 20, CY + 90
    out += path(f'M{f(ax)},{f(ay-150)} C{f(ax-80)},{f(ay-210)} {f(ax-230)},{f(ay-150)} {f(ax-220)},{f(ay)} '
                f'C{f(ax-210)},{f(ay+150)} {f(ax-90)},{f(ay+230)} {f(ax)},{f(ay+180)} '
                f'C{f(ax+90)},{f(ay+230)} {f(ax+210)},{f(ay+150)} {f(ax+220)},{f(ay)} '
                f'C{f(ax+230)},{f(ay-150)} {f(ax+80)},{f(ay-210)} {f(ax)},{f(ay-150)}z',
                stroke=GOLD, stroke_width=9, stroke_linejoin='round')
    out += path(f'M{f(ax)},{f(ay-150)} q-10,-60 25,-95', stroke=GOLD, stroke_width=8, stroke_linecap='round')
    out += path(f'M{f(ax+20)},{f(ay-200)} q70,-50 120,-10 q-60,45 -120,10z', fill='currentColor', stroke='none')
    return out


def m_transmute(c):
    out = circle(350, stroke_width=7) + circle(325, stroke_width=2) + circle(230, stroke_width=4)
    out += poly(ngon(CX, CY, 325, 3), stroke=GOLD, stroke_width=5) + poly(ngon(CX, CY, 325, 3, math.pi / 2), stroke=GOLD, stroke_width=5)
    for x, y in ngon(CX, CY, 325, 6, -math.pi / 2):
        out += circle(26, cx=x, cy=y, fill='#07080f', stroke_width=5)
    out += circle(90, stroke_width=5) + poly(ngon(CX, CY, 90, 4, 0), stroke_width=3, opacity=.7)
    return out


def m_orbs(c):
    out = ''
    for i in range(7):
        a = math.pi * (1.1 + i * .8 / 6)
        x, y = polar(330, a, CX + 40, CY + 330)
        y -= 120
        r = 62 if i == 3 else 50
        out += circle(r, cx=x, cy=y, fill='currentColor', stroke=GOLD, stroke_width=4, opacity='.85')
        out += circle(r * .5, cx=x - r * .28, cy=y - r * .28, fill=PAPER, stroke='none', opacity='.22')
        out += sparkle(x + r * .2, y + r * .15, r * .28).replace('/>', f' fill="{PAPER}" stroke="none" opacity=".8"/>')
    return out


def m_shock(c):
    out = ''
    for i, r in enumerate((90, 170, 260, 360)):
        out += circle(r, stroke_width=f(12 - i * 2.5), opacity=f(1 - i * .2))
    for i in range(16):
        a = i * math.pi / 8 + .2
        x1, y1 = polar(390, a)
        x2, y2 = polar(470 - (i % 3) * 30, a)
        out += f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" stroke="{GOLD}" stroke-width="6" stroke-linecap="round"/>'
    out += circle(40, fill=GOLD, stroke='none')
    return out


def m_bolt(c):
    out = circle(250, cx=CX + 40, cy=CY + 40, stroke_width=3, opacity=.4)
    for x, y in ngon(CX + 40, CY + 40, 160, 5):
        out += poly(ngon(x, y, 58, 5), stroke_width=3, opacity=.35)
    out += poly(ngon(CX + 40, CY + 40, 70, 5), stroke_width=4, opacity=.55)
    out += poly([(CX + 60, CY - 380), (CX - 150, CY + 40), (CX + 10, CY + 40), (CX - 90, CY + 380),
                 (CX + 230, CY - 90), (CX + 60, CY - 90), (CX + 170, CY - 380)],
                fill=GOLD, stroke=PAPER, stroke_width=4, stroke_linejoin='round')
    return out


def m_goal(c):
    out = ''
    gx, gy, gw, gh = CX - 330, CY - 230, 660, 330
    out += f'<rect x="{f(gx)}" y="{f(gy)}" width="{gw}" height="{gh}" stroke-width="12" stroke="{PAPER}"/>'
    for i in range(1, 12):
        out += f'<line x1="{f(gx + i * gw / 12)}" y1="{f(gy)}" x2="{f(gx + i * gw / 12)}" y2="{f(gy + gh)}" stroke-width="2" opacity=".45"/>'
    for j in range(1, 6):
        out += f'<line x1="{f(gx)}" y1="{f(gy + j * gh / 6)}" x2="{f(gx + gw)}" y2="{f(gy + j * gh / 6)}" stroke-width="2" opacity=".45"/>'
    out += f'<line x1="{f(CX-480)}" y1="{f(gy+gh)}" x2="{f(CX+480)}" y2="{f(gy+gh)}" stroke-width="5"/>'
    out += path(f'M{f(CX-200)},{f(gy+gh)} A200,120 0 0,0 {f(CX+200)},{f(gy+gh)}', stroke_width=4, opacity=.7)
    out += circle(48, cx=CX + 150, cy=CY - 80, fill=PAPER, stroke=GOLD, stroke_width=5)
    out += poly(ngon(CX + 150, CY - 80, 18, 5), fill='#07080f', stroke='none')
    return out


def m_gate(c):
    out = ''
    for i in range(7):
        out += f'<ellipse cx="{CX}" cy="{CY}" rx="{f(80 + i * 42)}" ry="{f(200 + i * 28)}" stroke-width="{f(9 - i)}" opacity="{f(1 - i * .12)}"/>'
    rng = random.Random('ombres')
    for i in range(22):
        x = CX + rng.uniform(-430, 430)
        y = CY + rng.uniform(80, 400)
        out += f'<line x1="{f(x)}" y1="{f(y)}" x2="{f(x)}" y2="{f(y - rng.uniform(60, 220))}" stroke="{GOLD if i % 5 == 0 else "currentColor"}" stroke-width="3" stroke-linecap="round" opacity=".6"/>'
    for (x, y, sx, sy) in ((CX - 470, CY - 330, 1, 1), (CX + 470, CY - 330, -1, 1), (CX - 470, CY + 330, 1, -1), (CX + 470, CY + 330, -1, -1)):
        out += poly([(x, y + sy * 70), (x, y), (x + sx * 70, y)], closed=False, stroke=PAPER, stroke_width=4, opacity=.7)
    return out


def m_frost_fire(c):
    out = ''
    for i in range(6):
        a = i * math.pi / 3 - math.pi / 2
        x, y = polar(300, a, CX - 120, CY)
        out += f'<line x1="{f(CX-120)}" y1="{CY}" x2="{f(x)}" y2="{f(y)}" stroke="{PAPER}" stroke-width="7" stroke-linecap="round" opacity=".85"/>'
        for t in (.45, .7):
            bx, by = polar(300 * t, a, CX - 120, CY)
            for s in (-1, 1):
                ex, ey = polar(70 * (1.2 - t), a + s * .9, bx, by)
                out += f'<line x1="{f(bx)}" y1="{f(by)}" x2="{f(ex)}" y2="{f(ey)}" stroke="{PAPER}" stroke-width="5" stroke-linecap="round" opacity=".7"/>'
    x, y, h, w = CX + 230, CY + 260, 520, 210
    out += path(f'M{f(x)},{f(y)} C{f(x-w)},{f(y-h*.35)} {f(x-w*.2)},{f(y-h*.7)} {f(x+w*.15)},{f(y-h)} '
                f'C{f(x+w*.1)},{f(y-h*.65)} {f(x+w)},{f(y-h*.45)} {f(x)},{f(y)}z', fill='currentColor', stroke=GOLD, stroke_width=5, opacity='.9')
    return out


def m_hexes(c):
    out = ''
    r = 64
    for q in range(-4, 5):
        for k in range(-3, 4):
            x = CX + q * r * 1.5
            y = CY + k * r * math.sqrt(3) + (q % 2) * r * math.sqrt(3) / 2
            d = math.hypot(x - CX, y - CY)
            if d > 420:
                continue
            op = 1 - d / 460
            out += poly(ngon(x, y, r * .92, 6, 0), stroke_width=4, opacity=f(op))
            if (q * 7 + k * 3) % 5 == 0:
                out += circle(9, cx=x, cy=y, fill=GOLD, stroke='none', opacity=f(op))
    return out


def m_skyline(c):
    out = ''
    base = CY + 250
    blds = [(-460, 120, 160), (-340, 90, 260), (-250, 140, 190), (-110, 70, 340), (-40, 130, 230), (90, 90, 300), (180, 150, 210), (330, 120, 280)]
    for dx, w, h in blds:
        out += f'<rect x="{f(CX+dx)}" y="{f(base-h)}" width="{w}" height="{h}" fill="#0c0e18" stroke-width="4"/>'
        for wy in range(int(base - h + 26), int(base - 20), 34):
            for wx in range(int(CX + dx + 16), int(CX + dx + w - 18), 28):
                if (wx * 3 + wy) % 7 < 2:
                    out += f'<rect x="{wx}" y="{wy}" width="10" height="14" fill="{GOLD}" stroke="none" opacity=".75"/>'
    for cx_, h in ((-70, 430), (130, 470)):
        out += f'<rect x="{f(CX+cx_)}" y="{f(base-h)}" width="26" height="{h-120}" fill="#0c0e18" stroke-width="4"/>'
        sx, sy = CX + cx_ + 13, base - h
        out += path(f'M{f(sx)},{f(sy)} c-40,-60 60,-90 20,-150 c-30,-50 70,-70 50,-130', stroke=PAPER, stroke_width=10, stroke_linecap='round', opacity=.25)
    out += f'<line x1="{f(CX-520)}" y1="{base}" x2="{f(CX+520)}" y2="{base}" stroke-width="5"/>'
    return out


def m_vault(c):
    out = circle(360, stroke_width=22) + circle(320, stroke_width=3, opacity=.5)
    for i in range(60):
        a = i * math.pi / 30
        x1, y1 = polar(300, a)
        x2, y2 = polar(270 if i % 5 else 245, a)
        out += f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" stroke="{PAPER}" stroke-width="{4 if i % 5 == 0 else 2}" opacity=".7"/>'
    for i in range(3):
        a = i * 2 * math.pi / 3 - math.pi / 2
        x, y = polar(190, a)
        out += f'<line x1="{CX}" y1="{CY}" x2="{f(x)}" y2="{f(y)}" stroke="{GOLD}" stroke-width="16" stroke-linecap="round"/>'
        out += circle(30, cx=x, cy=y, fill=GOLD, stroke='none')
    out += circle(70, fill='#07080f', stroke=GOLD, stroke_width=10)
    return out


def m_lights(c):
    out = ''
    cols = ['#ef4444', '#facc15', '#22c55e', '#3b82f6', '#f97316', '#ec4899']
    for row, (y0, amp) in enumerate(((CY - 230, 70), (CY + 10, 60), (CY + 240, 75))):
        x0, x1 = CX - 500, CX + 500
        d = f'M{x0},{y0} Q{CX},{y0 + amp * 2} {x1},{y0}'
        out += path(d, stroke=PAPER, stroke_width=3, opacity=.45)
        for i in range(11):
            t = (i + .5) / 11
            x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * CX + t * t * x1
            y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * (y0 + amp * 2) + t * t * y0
            col = cols[(i + row * 2) % len(cols)]
            out += circle(28, cx=x, cy=y + 22, fill=col, stroke='none', opacity='.22')
            out += f'<ellipse cx="{f(x)}" cy="{f(y + 22)}" rx="10" ry="15" fill="{col}" stroke="none"/>'
    rng = random.Random('envers')
    for _ in range(40):
        out += circle(rng.uniform(1.5, 4), cx=CX + rng.uniform(-520, 520), cy=CY + rng.uniform(-420, 420), fill=PAPER, stroke='none', opacity=f(rng.uniform(.15, .5)))
    return out


def m_shapes(c):
    out = circle(130, cx=CX - 320, cy=CY, stroke_width=16)
    out += poly(ngon(CX, CY + 25, 160, 3), stroke=GOLD, stroke_width=16, stroke_linejoin='round')
    out += f'<rect x="{f(CX+200)}" y="{f(CY-120)}" width="240" height="240" stroke-width="16"/>'
    out += f'<line x1="{f(CX-500)}" y1="{f(CY+230)}" x2="{f(CX+500)}" y2="{f(CY+230)}" stroke="{PAPER}" stroke-width="2" opacity=".3" stroke-dasharray="6 14"/>'
    return out


def m_cup(c):
    out = path(f'M{f(CX-170)},{f(CY-60)} L{f(CX-140)},{f(CY+200)} Q{f(CX-130)},{f(CY+250)} {f(CX-80)},{f(CY+250)} '
               f'L{f(CX+80)},{f(CY+250)} Q{f(CX+130)},{f(CY+250)} {f(CX+140)},{f(CY+200)} L{f(CX+170)},{f(CY-60)}z',
               fill='currentColor', stroke=PAPER, stroke_width=6, stroke_linejoin='round', opacity='.95')
    out += path(f'M{f(CX+160)},{f(CY+10)} c110,-10 110,150 -10,150', stroke=PAPER, stroke_width=14, stroke_linecap='round')
    out += f'<ellipse cx="{CX}" cy="{f(CY+270)}" rx="260" ry="34" stroke="{PAPER}" stroke-width="5" opacity=".6"/>'
    for dx in (-80, 0, 80):
        out += path(f'M{f(CX+dx)},{f(CY-100)} c-40,-50 40,-80 0,-140 c-30,-45 30,-70 10,-110', stroke=GOLD, stroke_width=9, stroke_linecap='round', opacity=.8)
    return out


def m_longship(c):
    out = ''
    for j in range(3):
        y = CY + 230 + j * 45
        out += path(f'M{f(CX-520)},{y}' + ''.join(' q45,-28 90,0 t90,0' for _ in range(6)), stroke_width=f(6 - j * 1.5), opacity=f(.9 - j * .25), stroke_linecap='round')
    out += path(f'M{f(CX-380)},{f(CY+150)} Q{f(CX)},{f(CY+300)} {f(CX+380)},{f(CY+150)} L{f(CX+430)},{f(CY+40)} '
                f'q-30,10 -50,60 L{f(CX-380)},{f(CY+110)} q-20,-50 -50,-70z', fill='#0c0e18', stroke=GOLD, stroke_width=7, stroke_linejoin='round')
    out += f'<line x1="{CX}" y1="{f(CY+150)}" x2="{CX}" y2="{f(CY-360)}" stroke="{PAPER}" stroke-width="8"/>'
    sail = f'M{f(CX-230)},{f(CY-320)} L{f(CX+230)},{f(CY-320)} Q{f(CX+260)},{f(CY-100)} {f(CX+230)},{f(CY+60)} L{f(CX-230)},{f(CY+60)} Q{f(CX-260)},{f(CY-100)} {f(CX-230)},{f(CY-320)}z'
    out += path(sail, fill='#0c0e18', stroke='currentColor', stroke_width=7)
    for i in range(5):
        x = CX - 230 + i * 92
        out += f'<rect x="{f(x)}" y="{f(CY-312)}" width="46" height="364" fill="currentColor" stroke="none" opacity=".75"/>'
    for i in range(6):
        x = CX - 300 + i * 120
        out += circle(32, cx=x, cy=CY + 140 - abs(i - 2.5) * 8, fill='#0c0e18', stroke=GOLD, stroke_width=5)
    return out


def m_wand(c):
    out = f'<line x1="{f(CX-330)}" y1="{f(CY+330)}" x2="{f(CX-60)}" y2="{f(CY+60)}" stroke="{PAPER}" stroke-width="16" stroke-linecap="round"/>'
    out += f'<line x1="{f(CX-330)}" y1="{f(CY+330)}" x2="{f(CX-250)}" y2="{f(CY+250)}" stroke="{GOLD}" stroke-width="22" stroke-linecap="round"/>'
    out += path(f'M{f(CX-50)},{f(CY+50)} C{f(CX+80)},{f(CY-100)} {f(CX+60)},{f(CY-260)} {f(CX+300)},{f(CY-300)}', stroke_width=5, stroke_dasharray='2 16', stroke_linecap='round')
    rng = random.Random('etincelles')
    for i in range(16):
        t = i / 15
        x = CX - 50 + t * 350 + rng.uniform(-60, 60)
        y = CY + 50 - t * 350 + rng.uniform(-60, 60)
        out += sparkle(x, y, rng.uniform(10, 34)).replace('/>', f' fill="{GOLD if i % 3 else PAPER}" stroke="none" opacity="{f(rng.uniform(.5, 1))}"/>')
    out += sparkle(CX + 300, CY - 300, 70).replace('/>', f' fill="{GOLD}" stroke="none"/>')
    return out


def m_ring(c):
    out = path(f'M{f(CX-520)},{f(CY+330)} L{f(CX-120)},{f(CY-40)} L{f(CX-60)},{f(CY-60)} L{f(CX+20)},{f(CY+20)} L{f(CX+520)},{f(CY+330)}z',
               fill='#0c0e18', stroke='currentColor', stroke_width=5, stroke_linejoin='round')
    out += circle(60, cx=CX - 90, cy=CY - 70, fill='currentColor', stroke='none', opacity='.35')
    out += f'<ellipse cx="{f(CX+60)}" cy="{f(CY-130)}" rx="200" ry="70" stroke="{GOLD}" stroke-width="30"/>'
    out += f'<ellipse cx="{f(CX+60)}" cy="{f(CY-138)}" rx="200" ry="70" stroke="{PAPER}" stroke-width="4" opacity=".4"/>'
    return out


def m_hyperspace(c):
    out = ''
    rng = random.Random('hyper')
    for i in range(70):
        a = rng.uniform(0, 2 * math.pi)
        r1 = rng.uniform(60, 260)
        r2 = r1 + rng.uniform(60, 260)
        x1, y1 = polar(r1, a)
        x2, y2 = polar(r2, a)
        out += f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" stroke="{PAPER if i % 4 else GOLD}" stroke-width="{f(rng.uniform(1.5, 4))}" stroke-linecap="round" opacity="{f(rng.uniform(.3, .9))}"/>'
    out += circle(120, cx=CX + 250, cy=CY + 210, fill='currentColor', stroke='none', opacity='.9')
    out += f'<ellipse cx="{f(CX+250)}" cy="{f(CY+210)}" rx="210" ry="38" stroke="{GOLD}" stroke-width="7" transform="rotate(-18 {f(CX+250)} {f(CY+210)})"/>'
    return out


def m_gems(c):
    out = ''
    cols = ['#a855f7', '#3b82f6', '#ef4444', '#f97316', '#22c55e', '#facc15']
    for i, col in enumerate(cols):
        a = math.pi * (1.15 + i * .7 / 5)
        x, y = polar(330, a, CX, CY + 300)
        out += circle(68, cx=x, cy=y - 80, fill=col, stroke='none', opacity='.25')
        out += poly(ngon(x, y - 80, 46, 6), fill=col, stroke=PAPER, stroke_width=3)
        out += poly(ngon(x, y - 80, 22, 6), fill=PAPER, stroke='none', opacity='.35')
    out += path(f'M{f(CX-380)},{f(CY+140)} Q{CX},{f(CY-260)} {f(CX+380)},{f(CY+140)}', stroke=GOLD, stroke_width=10, stroke_linecap='round', opacity='.5')
    return out


def m_elements(c):
    out = ''
    centers = [(CX - 280, CY + 60), (CX, CY - 160), (CX + 280, CY + 60)]
    for (x, y), col in zip(centers, ('#22c55e', '#ef4444', '#3b82f6')):
        out += circle(125, cx=x, cy=y, stroke=col, stroke_width=8) + circle(105, cx=x, cy=y, fill=col, stroke='none', opacity='.15')
    x, y = centers[0]
    out += path(f'M{f(x)},{f(y+70)} C{f(x-90)},{f(y+10)} {f(x-50)},{f(y-80)} {f(x+50)},{f(y-80)} C{f(x+70)},{f(y)} {f(x+30)},{f(y+60)} {f(x)},{f(y+70)}z M{f(x)},{f(y+70)} L{f(x+40)},{f(y-50)}', stroke='#22c55e', stroke_width=7, stroke_linejoin='round')
    x, y = centers[1]
    out += path(f'M{f(x)},{f(y+75)} C{f(x-80)},{f(y+40)} {f(x-50)},{f(y-30)} {f(x-10)},{f(y-80)} C{f(x)},{f(y-30)} {f(x+70)},{f(y-20)} {f(x)},{f(y+75)}z', stroke='#ef4444', stroke_width=7, stroke_linejoin='round')
    x, y = centers[2]
    out += path(f'M{f(x)},{f(y-80)} C{f(x+30)},{f(y-30)} {f(x+60)},{f(y)} {f(x+60)},{f(y+25)} A60,60 0 0,1 {f(x-60)},{f(y+25)} C{f(x-60)},{f(y)} {f(x-30)},{f(y-30)} {f(x)},{f(y-80)}z', stroke='#3b82f6', stroke_width=7, stroke_linejoin='round')
    return out


def m_cubes(c):
    out = ''
    s = 110

    def cube(x, y, top, left, right):
        a, b = s * math.cos(math.pi / 6), s / 2
        t = [(x, y - s), (x + a, y - s + b), (x, y), (x - a, y - s + b)]
        l = [(x - a, y - s + b), (x, y), (x, y + s), (x - a, y + b)]
        r = [(x, y), (x + a, y - s + b), (x + a, y + b), (x, y + s)]
        return (poly(t, fill=top, stroke='#07080f', stroke_width=4) + poly(l, fill=left, stroke='#07080f', stroke_width=4)
                + poly(r, fill=right, stroke='#07080f', stroke_width=4))
    a = s * math.cos(math.pi / 6)
    grass = ('#65a30d', '#7c4a1e', '#5c3716')
    stone = ('#9ca3af', '#6b7280', '#4b5563')
    for (dx, dy, kind) in ((-a, -s / 2 + 140, grass), (a, -s / 2 + 140, stone), (0, 140, grass), (-2 * a, 140, stone),
                           (2 * a, 140, grass), (-a, s / 2 + 140, grass), (a, s / 2 + 140, stone), (0, -s + 140 - s / 2 + s / 2 - 0, grass)):
        out += cube(CX + dx, CY + dy, *kind)
    out += cube(CX, CY + 140 - s, '#facc15', '#a16207', '#854d0e')
    return out


def m_sunset(c):
    sy = CY - 40
    out = circle(260, cx=CX, cy=sy, fill='url(#sun)', stroke='none')
    for i in range(6):
        y = sy + 40 + i * 38
        out += f'<rect x="{f(CX-270)}" y="{f(y)}" width="540" height="{f(6 + i * 3)}" fill="#07080f" stroke="none"/>'
    base = CY + 250
    for dx, w, h in ((-430, 70, 160), (-360, 50, 240), (-300, 80, 190), (220, 70, 220), (290, 60, 300), (350, 90, 170)):
        out += f'<rect x="{f(CX+dx)}" y="{f(base-h)}" width="{w}" height="{h}" fill="#0c0e18" stroke="none"/>'
    for px, hh, lean in ((CX - 140, 330, -1), (CX + 120, 280, 1)):
        out += path(f'M{f(px)},{base} q{lean*20},{-hh*.5} {lean*40},{-hh}', stroke='#0c0e18', stroke_width=16, stroke_linecap='round')
        tx, ty = px + lean * 40, base - hh
        for k in range(6):
            a = -math.pi + k * math.pi / 5
            ex, ey = polar(120, a + .25, tx, ty)
            out += path(f'M{f(tx)},{f(ty)} Q{f((tx+ex)/2)},{f(min(ty,ey)-40)} {f(ex)},{f(ey+40)}', stroke='#0c0e18', stroke_width=14, stroke_linecap='round')
    out += f'<rect x="{f(CX-560)}" y="{base}" width="1120" height="200" fill="#07080f" stroke="none"/>'
    for i in range(6):
        out += f'<line x1="{f(CX-560)}" y1="{f(base + 10 + i * i * 9)}" x2="{f(CX+560)}" y2="{f(base + 10 + i * i * 9)}" stroke-width="2" opacity=".5"/>'
    return out


def m_sword(c):
    out = path(f'M{f(CX-420)},{f(CY+330)} Q{f(CX-200)},{f(CY+180)} {CX},{f(CY+200)} Q{f(CX+220)},{f(CY+180)} {f(CX+420)},{f(CY+330)}z',
               fill='#0c0e18', stroke='currentColor', stroke_width=5)
    out += poly([(CX - 18, CY + 210), (CX - 18, CY - 190), (CX, CY - 230), (CX + 18, CY - 190), (CX + 18, CY + 210)], fill=PAPER, stroke='none', opacity='.92')
    out += f'<rect x="{f(CX-110)}" y="{f(CY-215)}" width="220" height="26" rx="13" fill="{GOLD}" stroke="none" transform="translate(0 -40)"/>'
    out += f'<rect x="{f(CX-14)}" y="{f(CY-350)}" width="28" height="110" rx="10" fill="currentColor" stroke="none"/>'
    out += circle(22, cx=CX, cy=CY - 360, fill=GOLD, stroke='none')
    rng = random.Random('feuilles')
    for i in range(10):
        x, y = CX + rng.uniform(-480, 480), CY + rng.uniform(-360, 120)
        a = rng.uniform(0, 180)
        out += f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="22" ry="9" fill="currentColor" stroke="none" opacity="{f(rng.uniform(.4, .9))}" transform="rotate({f(a)} {f(x)} {f(y)})"/>'
    out += path(f'M{f(CX-500)},{f(CY-120)} c120,-60 220,40 340,-20 s200,-70 300,-10', stroke=PAPER, stroke_width=4, stroke_linecap='round', opacity='.35')
    return out


def m_pipe(c):
    out = ''
    for i in range(7):
        x = CX - 420 + i * 120
        out += f'<rect x="{f(x)}" y="{f(CY-300)}" width="120" height="70" fill="#7c2d12" stroke="#07080f" stroke-width="5"/>'
        out += f'<line x1="{f(x+60)}" y1="{f(CY-300)}" x2="{f(x+60)}" y2="{f(CY-265)}" stroke="#07080f" stroke-width="4"/>'
        out += f'<line x1="{f(x)}" y1="{f(CY-265)}" x2="{f(x+120)}" y2="{f(CY-265)}" stroke="#07080f" stroke-width="4"/>'
    out += f'<rect x="{f(CX-130)}" y="{f(CY+40)}" width="260" height="70" rx="8" fill="#16a34a" stroke="#07080f" stroke-width="6"/>'
    out += f'<rect x="{f(CX-105)}" y="{f(CY+110)}" width="210" height="300" fill="#15803d" stroke="#07080f" stroke-width="6"/>'
    out += f'<rect x="{f(CX-80)}" y="{f(CY+120)}" width="26" height="280" fill="#4ade80" stroke="none" opacity=".5"/>'
    for i, (x, y) in enumerate(((CX - 330, CY - 110), (CX - 200, CY - 150), (CX + 200, CY - 150), (CX + 330, CY - 110), (CX, CY - 120))):
        out += f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="30" ry="42" fill="{GOLD}" stroke="#07080f" stroke-width="4"/>'
        out += f'<rect x="{f(x-6)}" y="{f(y-24)}" width="12" height="48" rx="4" fill="#07080f" stroke="none" opacity=".35"/>'
    return out


def m_hextech(c):
    out = ''
    for i, r in enumerate((360, 300, 210)):
        out += poly(ngon(CX, CY, r, 6), stroke=GOLD if i != 1 else 'currentColor', stroke_width=(8, 3, 6)[i], stroke_linejoin='round')
    for x, y in ngon(CX, CY, 360, 6):
        out += poly(ngon(x, y, 22, 4, 0), fill=GOLD, stroke='none')
    out += poly([(CX, CY - 130), (CX + 80, CY), (CX, CY + 130), (CX - 80, CY)], fill='currentColor', stroke=PAPER, stroke_width=4, opacity='.9')
    out += poly([(CX, CY - 60), (CX + 36, CY), (CX, CY + 60), (CX - 36, CY)], fill=PAPER, stroke='none', opacity='.5')
    return out


def m_shards(c):
    out = ''
    rng = random.Random('eclats')
    for i in range(14):
        x, y = CX + rng.uniform(-420, 420), CY + rng.uniform(-330, 330)
        a = rng.uniform(0, 2 * math.pi)
        L, w = rng.uniform(80, 240), rng.uniform(16, 50)
        p1 = polar(L, a, x, y)
        p2 = polar(w, a + math.pi / 2, x, y)
        p3 = polar(L * .3, a + math.pi, x, y)
        out += poly([p1, p2, p3], fill=PAPER if i % 4 == 0 else 'currentColor', stroke='none', opacity=f(rng.uniform(.35, .95)))
    for k in range(4):
        a = k * math.pi / 2
        tip = polar(70, a)
        l, r = polar(190, a - .32), polar(190, a + .32)
        mid = polar(140, a)
        out += poly([tip, l, mid, r], fill='#07080f', stroke=GOLD, stroke_width=6, stroke_linejoin='miter')
    out += circle(12, fill=PAPER, stroke='none')
    return out


def m_pitch(c):
    out = f'<rect x="{f(CX-480)}" y="{f(CY-300)}" width="960" height="600" stroke="{PAPER}" stroke-width="6" opacity=".85"/>'
    for i in range(6):
        out += f'<rect x="{f(CX-480+i*160)}" y="{f(CY-300)}" width="80" height="600" fill="currentColor" stroke="none" opacity=".12"/>'
    out += f'<line x1="{CX}" y1="{f(CY-300)}" x2="{CX}" y2="{f(CY+300)}" stroke="{PAPER}" stroke-width="5" opacity=".85"/>'
    out += circle(110, stroke=PAPER, stroke_width=5, opacity='.85') + circle(8, fill=PAPER, stroke='none')
    for s in (-1, 1):
        x = CX + s * 480
        out += f'<rect x="{f(min(x, x - s * 150))}" y="{f(CY-170)}" width="150" height="340" stroke="{PAPER}" stroke-width="5" opacity=".85"/>'
        out += f'<rect x="{f(min(x, x - s * 55))}" y="{f(CY-75)}" width="55" height="150" stroke="{PAPER}" stroke-width="4" opacity=".7"/>'
    out += path(f'M{f(CX-360)},{f(CY+210)} C{f(CX-150)},{f(CY+120)} {f(CX+40)},{f(CY-260)} {f(CX+300)},{f(CY-120)}', stroke=GOLD, stroke_width=5, stroke_dasharray='14 12', stroke_linecap='round')
    out += circle(34, cx=CX + 300, cy=CY - 120, fill=PAPER, stroke=GOLD, stroke_width=5)
    return out


def m_bulb(c):
    out = path(f'M{f(CX-80)},{f(CY+140)} C{f(CX-90)},{f(CY+60)} {f(CX-200)},{f(CY+10)} {f(CX-200)},{f(CY-120)} '
               f'A200,200 0 1,1 {f(CX+200)},{f(CY-120)} C{f(CX+200)},{f(CY+10)} {f(CX+90)},{f(CY+60)} {f(CX+80)},{f(CY+140)}z',
               stroke=PAPER, stroke_width=8, stroke_linejoin='round')
    for i in range(3):
        y = CY + 170 + i * 36
        out += f'<rect x="{f(CX-80)}" y="{f(y)}" width="160" height="22" rx="10" fill="{GOLD}" stroke="none" opacity="{f(1 - i * .2)}"/>'
    out += path(f'M{f(CX-50)},{f(CY+130)} L{f(CX-50)},{f(CY-40)} l25,-40 l25,40 l25,-40 l25,40 L{f(CX+50)},{f(CY+130)}', stroke=GOLD, stroke_width=6, stroke_linejoin='round')
    for i in range(3):
        out += f'<ellipse cx="{CX}" cy="{f(CY-120)}" rx="380" ry="120" stroke-width="3" opacity=".55" transform="rotate({i * 60 - 20} {CX} {f(CY-120)})"/>'
        x, y = polar(380, i * 2.1, CX, CY - 120)
    for i, a in enumerate((.4, 2.6, 4.4)):
        x, y = CX + 380 * math.cos(a) * math.cos(math.radians(i * 60 - 20)) - 120 * math.sin(a) * math.sin(math.radians(i * 60 - 20)), \
            CY - 120 + 380 * math.cos(a) * math.sin(math.radians(i * 60 - 20)) + 120 * math.sin(a) * math.cos(math.radians(i * 60 - 20))
        out += circle(16, cx=x, cy=y, fill='currentColor', stroke='none')
    return out


def m_hourglass(c):
    out = ''
    for dx in (-360, 360):
        x = CX + dx
        out += f'<rect x="{f(x-50)}" y="{f(CY-330)}" width="100" height="30" fill="{GOLD}" stroke="none" opacity=".6"/>'
        out += f'<rect x="{f(x-50)}" y="{f(CY+300)}" width="100" height="30" fill="{GOLD}" stroke="none" opacity=".6"/>'
        for k in range(4):
            out += f'<line x1="{f(x-30+k*20)}" y1="{f(CY-300)}" x2="{f(x-30+k*20)}" y2="{f(CY+300)}" stroke-width="5" opacity=".5"/>'
    out += f'<rect x="{f(CX-190)}" y="{f(CY-330)}" width="380" height="34" rx="10" fill="{GOLD}" stroke="none"/>'
    out += f'<rect x="{f(CX-190)}" y="{f(CY+296)}" width="380" height="34" rx="10" fill="{GOLD}" stroke="none"/>'
    out += path(f'M{f(CX-150)},{f(CY-296)} C{f(CX-150)},{f(CY-120)} {f(CX-20)},{f(CY-40)} {f(CX-20)},{CY} C{f(CX-20)},{f(CY+40)} {f(CX-150)},{f(CY+120)} {f(CX-150)},{f(CY+296)} '
                f'L{f(CX+150)},{f(CY+296)} C{f(CX+150)},{f(CY+120)} {f(CX+20)},{f(CY+40)} {f(CX+20)},{CY} C{f(CX+20)},{f(CY-40)} {f(CX+150)},{f(CY-120)} {f(CX+150)},{f(CY-296)}z',
                stroke=PAPER, stroke_width=7)
    out += path(f'M{f(CX-105)},{f(CY-170)} Q{CX},{f(CY-130)} {f(CX+105)},{f(CY-170)} C{f(CX+60)},{f(CY-90)} {f(CX+15)},{f(CY-40)} {CX},{f(CY-10)} C{f(CX-15)},{f(CY-40)} {f(CX-60)},{f(CY-90)} {f(CX-105)},{f(CY-170)}z', fill='currentColor', stroke='none')
    out += f'<line x1="{CX}" y1="{CY}" x2="{CX}" y2="{f(CY+220)}" stroke="currentColor" stroke-width="4" stroke-dasharray="3 9"/>'
    out += path(f'M{f(CX-140)},{f(CY+290)} Q{CX},{f(CY+150)} {f(CX+140)},{f(CY+290)}z', fill='currentColor', stroke='none')
    return out


def m_globe(c):
    out = circle(330, stroke=PAPER, stroke_width=6)
    for i in range(1, 6):
        out += f'<ellipse cx="{CX}" cy="{CY}" rx="{f(330 * math.cos(i * math.pi / 12))}" ry="330" stroke-width="3" opacity=".6"/>' if i % 2 else ''
    for k in (-2, -1, 0, 1, 2):
        y = CY + k * 110
        rx = math.sqrt(max(0, 330 ** 2 - (k * 110) ** 2))
        out += f'<ellipse cx="{CX}" cy="{f(y)}" rx="{f(rx)}" ry="{f(rx * .18)}" stroke-width="3" opacity=".6"/>'
    out += f'<ellipse cx="{CX}" cy="{CY}" rx="460" ry="120" stroke="{GOLD}" stroke-width="4" opacity=".7" transform="rotate(-20 {CX} {CY})"/>'
    px, py = CX + 120, CY - 140
    out += path(f'M{f(px)},{f(py+90)} C{f(px-30)},{f(py+40)} {f(px-60)},{f(py)} {f(px-60)},{f(py-30)} A60,60 0 1,1 {f(px+60)},{f(py-30)} C{f(px+60)},{f(py)} {f(px+30)},{f(py+40)} {f(px)},{f(py+90)}z',
                fill=GOLD, stroke='#07080f', stroke_width=5)
    out += circle(22, cx=px, cy=py - 30, fill='#07080f', stroke='none')
    return out


def m_track(c):
    out = ''
    for i in range(6):
        r = 160 + i * 52
        out += path(f'M{f(CX-520)},{f(CY+r-60)} L{f(CX)},{f(CY+r-60)} A{r},{r} 0 0,0 {f(CX)},{f(CY-r-60)} L{f(CX-520)},{f(CY-r-60)}',
                    stroke=PAPER if i in (0, 5) else 'currentColor', stroke_width=5 if i in (0, 5) else 3, opacity='.85' if i in (0, 5) else '.55')
    out += circle(110, cx=CX + 220, cy=CY + 250, fill='#07080f', stroke=GOLD, stroke_width=10)
    out += f'<rect x="{f(CX+205)}" y="{f(CY+110)}" width="30" height="28" rx="6" fill="{GOLD}" stroke="none"/>'
    out += f'<line x1="{f(CX+220)}" y1="{f(CY+250)}" x2="{f(CX+220)}" y2="{f(CY+175)}" stroke="{PAPER}" stroke-width="8" stroke-linecap="round"/>'
    out += f'<line x1="{f(CX+220)}" y1="{f(CY+250)}" x2="{f(CX+275)}" y2="{f(CY+275)}" stroke="{PAPER}" stroke-width="6" stroke-linecap="round"/>'
    return out


def m_wave(c):
    out = ''
    rng = random.Random('ondes')
    n = 34
    for i in range(n):
        x = CX - 500 + i * 1000 / (n - 1)
        h = (math.sin(i * .45) * .5 + .6) * 260 * (1 - abs(i - n / 2) / (n * .7)) + rng.uniform(0, 40)
        out += f'<line x1="{f(x)}" y1="{f(CY-h)}" x2="{f(x)}" y2="{f(CY+h)}" stroke="{GOLD if i % 7 == 3 else "currentColor"}" stroke-width="14" stroke-linecap="round" opacity="{f(.45 + .55 * (1 - abs(i - n / 2) / (n / 2)))}"/>'
    for x, y, s in ((CX - 380, CY - 300, 1), (CX + 360, CY - 260, .8)):
        out += f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(34*s)}" ry="{f(26*s)}" fill="{PAPER}" stroke="none" transform="rotate(-20 {f(x)} {f(y)})"/>'
        out += f'<line x1="{f(x+30*s)}" y1="{f(y)}" x2="{f(x+30*s)}" y2="{f(y-150*s)}" stroke="{PAPER}" stroke-width="7"/>'
        out += path(f'M{f(x+30*s)},{f(y-150*s)} q50,20 40,80', stroke=PAPER, stroke_width=7, stroke_linecap='round')
    return out


def m_film(c):
    out = ''
    for k, (rot, op) in enumerate(((-12, 1), (8, .45))):
        g = f'<g transform="rotate({rot} {CX} {CY})" opacity="{op}">'
        y0 = CY - 130 + k * 40
        g += f'<rect x="{f(CX-620)}" y="{f(y0)}" width="1240" height="260" fill="#0c0e18" stroke="currentColor" stroke-width="5"/>'
        for i in range(31):
            x = CX - 610 + i * 40
            g += f'<rect x="{f(x)}" y="{f(y0+14)}" width="20" height="26" rx="4" fill="{PAPER}" stroke="none" opacity=".7"/>'
            g += f'<rect x="{f(x)}" y="{f(y0+220)}" width="20" height="26" rx="4" fill="{PAPER}" stroke="none" opacity=".7"/>'
        for i in range(6):
            x = CX - 600 + i * 205
            g += f'<rect x="{f(x)}" y="{f(y0+58)}" width="185" height="144" fill="currentColor" stroke="none" opacity="{f(.18 + (i == 3) * .6)}"/>'
        out += g + '</g>'
    out += poly([(CX - 30, CY - 50), (CX + 60, CY), (CX - 30, CY + 50)], fill=GOLD, stroke='none', transform=f'rotate(-12 {CX} {CY}) translate(205 0)')
    return out


def m_flowers(c):
    out = ''
    rng = random.Random('fleurs')
    for _ in range(26):
        x, y = CX + rng.uniform(-500, 500), CY + rng.uniform(80, 400)
        r = rng.uniform(14, 34)
        col = rng.choice((PAPER, 'currentColor', GOLD, 'currentColor'))
        for k in range(5):
            px, py = polar(r, k * 2 * math.pi / 5, x, y)
            out += circle(r * .62, cx=px, cy=py, fill=col, stroke='none', opacity=f(rng.uniform(.5, .9)))
        out += circle(r * .4, cx=x, cy=y, fill=GOLD, stroke='none')
    for _ in range(18):
        x, y = CX + rng.uniform(-500, 500), CY + rng.uniform(-420, 20)
        out += sparkle(x, y, rng.uniform(6, 26)).replace('/>', f' fill="{PAPER}" stroke="none" opacity="{f(rng.uniform(.4, 1))}"/>')
    out += circle(180, cx=CX + 40, cy=CY - 160, stroke_width=3, opacity='.55') + circle(140, cx=CX + 40, cy=CY - 160, stroke=GOLD, stroke_width=2, opacity='.6', stroke_dasharray='3 10')
    out += poly(star(CX + 40, CY - 160, 90, 36, 6), stroke=GOLD, stroke_width=4)
    return out


def m_saw(c):
    teeth = []
    for i in range(23):
        x = CX - 560 + i * 50
        teeth += [(x, CY + 40), (x + 25, CY - 30)]
    teeth += [(CX + 590, CY + 40), (CX + 590, CY + 120), (CX - 560, CY + 120)]
    out = poly(teeth, fill='currentColor', stroke=PAPER, stroke_width=4, stroke_linejoin='miter')
    rng = random.Random('gouttes')
    for i in range(12):
        x = CX - 520 + i * 95 + rng.uniform(-15, 15)
        h = rng.uniform(40, 220)
        out += f'<line x1="{f(x)}" y1="{f(CY+120)}" x2="{f(x)}" y2="{f(CY+120+h)}" stroke="currentColor" stroke-width="{f(rng.uniform(5, 12))}" stroke-linecap="round" opacity=".7"/>'
    out += path(f'M{f(CX-520)},{f(CY-140)} L{f(CX+520)},{f(CY-260)}', stroke=GOLD, stroke_width=6, stroke_linecap='round')
    out += path(f'M{f(CX-480)},{f(CY-200)} L{f(CX+380)},{f(CY-300)}', stroke=PAPER, stroke_width=2, stroke_linecap='round', opacity='.5')
    return out


def m_scope(c):
    out = circle(310, stroke=PAPER, stroke_width=8) + circle(220, stroke_width=2, opacity='.5')
    for a in range(4):
        x1, y1 = polar(330, a * math.pi / 2)
        x2, y2 = polar(70, a * math.pi / 2)
        out += f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" stroke="{PAPER}" stroke-width="5"/>'
    for i in range(1, 6):
        for s in (-1, 1):
            out += f'<line x1="{f(CX + s * i * 40)}" y1="{f(CY-10)}" x2="{f(CX + s * i * 40)}" y2="{f(CY+10)}" stroke="{PAPER}" stroke-width="3"/>'
    out += path(f'M{CX},{f(CY+40)} C{f(CX-60)},{f(CY)} {f(CX-60)},{f(CY-50)} {f(CX-28)},{f(CY-55)} C{f(CX-10)},{f(CY-58)} {CX},{f(CY-40)} {CX},{f(CY-30)} '
                f'C{CX},{f(CY-40)} {f(CX+10)},{f(CY-58)} {f(CX+28)},{f(CY-55)} C{f(CX+60)},{f(CY-50)} {f(CX+60)},{CY} {CX},{f(CY+40)}z', fill='currentColor', stroke='none')
    for i, (x, y, r) in enumerate(((CX + 330, CY - 270, 40), (CX - 360, CY + 250, 28), (CX + 260, CY + 300, 22))):
        out += poly(star(x, y, r, r * .45), fill=GOLD, stroke='none')
    return out


MOTIFS = {
    'naruto': m_spiral, 'onepiece': m_waves, 'aot': m_walls, 'demonslayer': m_checker, 'bleach': m_crescent,
    'jjk': m_seal, 'mha': m_burst, 'fairytail': m_flames, 'hxh': m_suits, 'deathnote': m_apple,
    'fmab': m_transmute, 'dragonball': m_orbs, 'onepunchman': m_shock, 'inazuma': m_bolt, 'bluelock': m_goal,
    'soloLeveling': m_gate, 'got': m_frost_fire, 'breakingbad': m_hexes, 'peakyBlinders': m_skyline,
    'casapapel': m_vault, 'strangerthings': m_lights, 'squidgame': m_shapes, 'friends': m_cup, 'vikings': m_longship,
    'harrypotter': m_wand, 'lotr': m_ring, 'starwars': m_hyperspace, 'marvel': m_gems, 'pokemon': m_elements,
    'minecraft': m_cubes, 'gta': m_sunset, 'zelda': m_sword, 'mario': m_pipe, 'lol': m_hextech, 'valorant': m_shards,
    'eafc': m_pitch, 'culture': m_bulb, 'histoire': m_hourglass, 'geo': m_globe, 'sport': m_track,
    'musique': m_wave, 'cinema': m_film, 'frieren': m_flowers, 'chainsawman': m_saw, 'spyfamily': m_scope,
}


def visual_svg(key, color):
    motif = MOTIFS.get(key, m_seal)(color)
    rng = random.Random(key)
    dust = ''.join(circle(rng.uniform(.8, 2.2), cx=rng.uniform(0, W), cy=rng.uniform(0, H), fill=PAPER, stroke='none',
                          opacity=f(rng.uniform(.06, .3))) for _ in range(60))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<defs>
<radialGradient id="halo" cx="{f(CX / W)}" cy="{f(CY / H)}" r=".62"><stop offset="0" stop-color="{color}" stop-opacity=".55"/><stop offset=".55" stop-color="{color}" stop-opacity=".12"/><stop offset="1" stop-color="{color}" stop-opacity="0"/></radialGradient>
<radialGradient id="warm" cx=".08" cy="1" r=".6"><stop offset="0" stop-color="{GOLD}" stop-opacity=".16"/><stop offset="1" stop-color="{GOLD}" stop-opacity="0"/></radialGradient>
<radialGradient id="sun" cx=".5" cy=".2" r=".9"><stop offset="0" stop-color="{GOLD}"/><stop offset="1" stop-color="{color}"/></radialGradient>
<linearGradient id="fade" x1="0" x2="1"><stop offset="0" stop-color="#07080f"/><stop offset=".42" stop-color="#07080f" stop-opacity=".55"/><stop offset=".7" stop-color="#07080f" stop-opacity="0"/></linearGradient>
<pattern id="dots" width="28" height="28" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.3" fill="{PAPER}" opacity=".07"/></pattern>
<filter id="glow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="14"/></filter>
<g id="m" fill="none" stroke="{color}" color="{color}" stroke-width="4">{motif}</g>
</defs>
<rect width="{W}" height="{H}" fill="#07080f"/>
<rect width="{W}" height="{H}" fill="url(#halo)"/>
<rect width="{W}" height="{H}" fill="url(#warm)"/>
<rect width="{W}" height="{H}" fill="url(#dots)"/>
{dust}
<use href="#m" filter="url(#glow)" opacity=".55"/>
<use href="#m"/>
<rect width="{W}" height="{H}" fill="url(#fade)"/>
</svg>
'''
