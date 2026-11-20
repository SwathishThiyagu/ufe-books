"""Claude's hand-drawn figures for me-thermo-u3 (Engineering Thermodynamics: second law and entropy), one per chapter,
drawn from each chapter's own worked example and numbers. Colours are the shell's CSS variables only.
Chapter 9 (entropy generation in control volumes) was added in the correction pass; chapter 10 is the third law."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def sub(base, s, size=11):
    """base text with a lowered subscript (no underscore on screen)"""
    return f'{base}<tspan dy="4" font-size="{size}">{s}</tspan><tspan dy="-4"> </tspan>'


def sup(base, s, size=11):
    return f'{base}<tspan dy="-7" font-size="{size}">{s}</tspan><tspan dy="7"> </tspan>'


def arrow(x1, y1, x2, y2, c=AC, w=2.5, m=None):
    m = m or {AC: 'n', LV: 'l', NX: 'x'}.get(c, 'm')
    return L(x1, y1, x2, y2, c, w, arrow=m)


def device(x, y, r, name, stroke=AC):
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:var(--panel);stroke:{stroke};stroke-width:2.5"/>'
            + T(x, y + 5, name, 15, bold=True))


def curve(f, a, b, fx, fy, n=120, c=AC, w=2.5, dash=None):
    return P([(fx(a + (b - a) * i / n), fy(f(a + (b - a) * i / n))) for i in range(n + 1)], c, w, dash)


# ---- 3.1 the engine and the refrigerator of the worked example ----
def f1():
    o = []
    def panel(x0, title, top, bot, up, lab_top, lab_bot, name, note1, note2):
        cx = x0 + 150
        o.append(T(cx, 26, title, 15, bold=True))
        o.append(boxt(x0 + 20, 40, 260, 44, [top], ACS, AC, 14))
        o.append(boxt(x0 + 20, 262, 260, 44, [bot], LVS, LV, 14))
        o.append(device(cx, 173, 34, name))
        if not up:
            o.append(arrow(cx, 86, cx, 135, AC)); o.append(arrow(cx, 209, cx, 258, LV))
        else:
            o.append(arrow(cx, 260, cx, 211, LV)); o.append(arrow(cx, 137, cx, 88, AC))
        o.append(Tb(cx - 12, 117, lab_top, 14, 'end', INK, True))
        o.append(Tb(cx - 12, 240, lab_bot, 14, 'end', INK, True))
        if not up:
            o.append(arrow(cx + 36, 173, cx + 128, 173, NX)); o.append(T(cx + 84, 162, 'W = 300 kJ', 14, fill=NX, bold=True))
            o.append(T(cx + 84, 192, 'out', 13, fill=MUT))
        else:
            o.append(arrow(cx + 128, 173, cx + 38, 173, NX)); o.append(T(cx + 84, 162, 'W = 300 kJ', 14, fill=NX, bold=True))
            o.append(T(cx + 84, 192, 'in', 13, fill=MUT))
        o.append(T(cx, 334, note1, 14, bold=True)); o.append(T(cx, 356, note2, 13, fill=MUT))
    panel(0, 'Heat engine', 'Source at 600 K', 'Sink at 300 K', False, 'Q₁ = 800 kJ', 'Q₂ = 500 kJ', 'E',
          'η = 300 / 800 = 0.375', 'work out ÷ heat in')
    panel(360, 'Refrigerator (arrows reversed)', 'Room at 300 K', 'Cold store at 270 K', True, 'Q₁ = 800 kJ', 'Q₂ = 500 kJ', 'R',
          sub('COP', 'R') + ' = 500 / 300 = 1.67', sub('COP', 'HP') + ' = 800 / 300 = 2.67')
    o.append(L(360, 30, 360, 350, LN, 1.5, '5 5'))
    return 372, ''.join(o)


FIG[1] = (f1, 'Left: the engine of the worked example takes 800 kJ at 600 K, gives 300 kJ of work and rejects 500 kJ at 300 K. '
              'Right: the refrigerator moves the same 500 kJ uphill from a 270 K store with 300 kJ of work and puts 800 kJ into the room.',
          'Two energy-flow diagrams. A heat engine between 600 K and 300 K: 800 kJ in, 300 kJ of work out, 500 kJ rejected, efficiency 0.375. '
          'A refrigerator between a 270 K cold store and a 300 K room: 500 kJ taken from the store, 300 kJ of work in, 800 kJ to the room, COP 1.67 as a refrigerator and 2.67 as a heat pump.')


# ---- 3.2 the claimed engine plus reversible devices moves heat uphill for free ----
def f2():
    o = []
    o.append(boxt(30, 30, 660, 44, ['Hot reservoir at 500 K: gains 500 kJ in all'], ACS, AC, 14))
    o.append(boxt(30, 300, 660, 44, ['Cold reservoir at 300 K: loses 200 + 300 = 500 kJ'], LVS, LV, 14))
    # the pair that acts as a PMM2
    o.append(R(40, 104, 300, 172, 'none', MUT, 10, 1.6, '6 5'))
    o.append(T(190, 124, 'claim + reversed reversible engine', 13, fill=MUT))
    o.append(device(190, 190, 34, 'PMM2'))
    o.append(T(190, 262, 'net: one reservoir, all heat → work', 13, fill=MUT))
    o.append(arrow(190, 298, 190, 226, LV)); o.append(Tb(140, 292, '200 kJ', 14, 'end', LV, True))
    o.append(T(190, 146, 'hot side: −1000 + 1000 = 0', 13, fill=MUT))
    # the refrigerator
    o.append(device(530, 190, 34, 'R'))
    o.append(T(574, 186, 'reversible', 13, 'start', MUT)); o.append(T(574, 204, 'refrigerator', 13, 'start', MUT))
    o.append(T(574, 222, sub('COP', 'R') + ' = 1.5', 13, 'start', MUT))
    o.append(arrow(530, 298, 530, 226, LV)); o.append(Tb(518, 270, '300 kJ', 14, 'end', LV, True))
    o.append(arrow(530, 154, 530, 78, AC)); o.append(Tb(542, 120, '500 kJ', 14, 'start', AC, True))
    # work link
    o.append(arrow(226, 190, 492, 190, NX, 3)); o.append(Tb(360, 180, 'W = 200 kJ', 14, 'middle', NX, True))
    o.append(T(360, 376, 'Net effect: 500 kJ climbs from 300 K to 500 K with no work from outside. Clausius is broken.', 14, bold=True))
    return 392, ''.join(o)


FIG[2] = (f2, 'The worked example’s chain. The 600 kJ claim and a reversed reversible engine together take 200 kJ from the 300 K body and give 200 kJ of work, '
              'a PMM2; that work drives a reversible refrigerator, and the whole set moves 500 kJ from 300 K to 500 K with nothing else changing.',
          'Block diagram: a hot reservoir at 500 K on top, a cold one at 300 K below. On the left the claimed engine plus a reversed reversible engine act as one machine that takes 200 kJ from the cold reservoir and gives 200 kJ of work. '
          'The work drives a reversible refrigerator of COP 1.5 that takes 300 kJ from the cold reservoir and delivers 500 kJ to the hot one.')


# ---- 3.3 reversible isotherm against free expansion, on p-V axes ----
def f3():
    o = []
    x0, x1, y0, y1 = 100, 660, 50, 330
    fx = lambda v: x0 + (v - 0.15) / 0.3 * (x1 - x0)
    fy = lambda p: y1 - p / 250 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45], [0, 50, 100, 150, 200, 250], fx, fy,
                  'V, m³', 'p, kPa', lambda v: f'{v:.2f}'))
    p = lambda v: 43.05 / v
    pts = [(fx(0.2 + 0.2 * i / 80), fy(p(0.2 + 0.2 * i / 80))) for i in range(81)]
    poly = [(fx(0.2), fy(0))] + pts + [(fx(0.4), fy(0))]
    o.append(f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in poly)}" style="fill:var(--accent-soft);stroke:none"/>')
    o.append(P(pts, AC, 3))
    o.append(C(fx(0.2), fy(p(0.2)), 6, AC)); o.append(C(fx(0.4), fy(p(0.4)), 6, AC))
    o.append(T(fx(0.2) + 12, fy(p(0.2)) - 6, '1: 0.2 m³, 215.3 kPa', 14, 'start', bold=True))
    o.append(T(fx(0.4) + 4, fy(p(0.4)) + 26, '2: 0.4 m³, 107.6 kPa', 14, 'end', bold=True))
    o.append(Tb(fx(0.3), fy(40), 'area = W_rev = 29.84 kJ'.replace('W_rev', sub('W', 'rev')), 15, 'middle', AC, True))
    o.append(Tb(fx(0.29), fy(110), 'reversible isotherm, pV = 43.05 kJ', 13, 'middle', AC, True))
    # free expansion: same end states, no path
    o.append(L(fx(0.2) + 8, fy(p(0.2)) + 8, fx(0.4) - 8, fy(p(0.4)) - 4, LV, 2, '3 6'))
    o.append(Tb(fx(0.22), fy(238), 'free expansion: no path through equilibrium states, W = 0', 13, 'start', LV, True))
    return 380, ''.join(o)


FIG[3] = (f3, 'The worked example on p-V axes: 0.5 kg of air at 300 K. The reversible isotherm from 0.2 m³ to 0.4 m³ delivers the shaded 29.84 kJ; '
              'free expansion joins the same two states without passing through equilibrium states (dotted), so it does no work at all.',
          'Pressure against volume. A falling isotherm from 215.3 kPa at 0.2 cubic metres to 107.6 kPa at 0.4 cubic metres with the area under it shaded, 29.84 kJ. '
          'A dotted line joins the same end states for the free expansion, which does zero work.')


# ---- 3.4 Carnot cycle: p-V sketch with the computed states, and the T-S rectangle to scale ----
def f4():
    o = []
    # left: p-V sketch (shape not to scale), states from the worked example
    o.append(T(170, 26, 'p-V (shape only, not to scale)', 14, bold=True))
    ox, oy = 50, 300
    o.append(L(ox, oy, 320, oy, L2, 1.5, arrow='m')); o.append(L(ox, oy, ox, 48, L2, 1.5, arrow='m'))
    o.append(T(316, oy + 20, 'V', 14, 'end', MUT)); o.append(T(ox + 8, 56, 'p', 14, 'start', MUT))
    # shape drawn from the real laws (isotherms pV = const, adiabats pV^1.4 = const) for a milder 1.3 temperature ratio
    g = 1.4; V1, V2 = 1.0, 1.6; V4 = V1 * 1.3 ** 2.5; V3 = V2 * 1.3 ** 2.5
    fx = lambda v: ox + 10 + (v - 0.8) / 2.6 * 250
    fy = lambda pp: oy - 10 - (pp - 0.2) / 0.85 * 220
    iso1 = lambda v: V1 / v; iso2 = lambda v: (V4 / v) * (V1 / V4) ** g
    ad1 = lambda v: (V2 / v) ** g * (V1 / V2); ad2 = lambda v: (V1 / v) ** g
    o.append(curve(iso1, V1, V2, fx, fy, 40, AC, 3))
    o.append(curve(ad1, V2, V3, fx, fy, 40, MUT, 2.5))
    o.append(curve(iso2, V4, V3, fx, fy, 40, LV, 3))
    o.append(curve(ad2, V1, V4, fx, fy, 40, MUT, 2.5))
    S = {1: (fx(V1), fy(1)), 2: (fx(V2), fy(iso1(V2))), 3: (fx(V3), fy(iso2(V3))), 4: (fx(V4), fy(iso2(V4)))}
    for k, (x, y) in S.items():
        o.append(C(x, y, 5, INK))
    o.append(T(S[1][0] - 8, S[1][1] + 4, '1', 14, 'end', bold=True)); o.append(T(S[2][0] + 8, S[2][1] - 4, '2', 14, 'start', bold=True))
    o.append(T(S[3][0], S[3][1] + 22, '3', 14, 'middle', bold=True)); o.append(T(S[4][0] - 8, S[4][1] + 14, '4', 14, 'end', bold=True))
    o.append(T(S[1][0] + 30, S[1][1] - 10, sub('Q', '1') + ' in at 900 K', 13, 'start', AC))
    o.append(T(S[3][0] + 14, S[3][1] + 5, sub('Q', '2') + ' out at 300 K', 13, 'start', LV))
    rows = ['1: 0.100 m³, 2583 kPa', '2: 0.200 m³, 1292 kPa', '3: 3.118 m³, 27.6 kPa', '4: 1.559 m³, 55.2 kPa']
    for i, r in enumerate(rows):
        o.append(T(50, 330 + i * 20, r, 13, 'start', MUT))
    # right: T-S rectangle to scale
    x0, x1, y0, y1 = 420, 680, 50, 300
    fs = lambda s: x0 + 30 + s / 0.2 * 180
    fT = lambda t: y1 - t / 1000 * (y1 - y0)
    o.append(T(550, 26, 'T-S (to scale)', 14, bold=True))
    o.append(L(x0, y1, x1, y1, L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    for t in (0, 300, 900):
        o += [L(x0 - 5, fT(t), x0, fT(t), L2, 1.5), T(x0 - 9, fT(t) + 4.5, f'{t}', 13, 'end', MUT)]
    o.append(T(x0 - 9, y0 - 8, 'T, K', 13, 'end', MUT))
    o.append(f'<rect x="{fs(0):.1f}" y="{fT(300):.1f}" width="{fs(0.1989) - fs(0):.1f}" height="{fT(0) - fT(300):.1f}" style="fill:var(--live-soft);stroke:none"/>')
    o.append(f'<rect x="{fs(0):.1f}" y="{fT(900):.1f}" width="{fs(0.1989) - fs(0):.1f}" height="{fT(300) - fT(900):.1f}" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2.5"/>')
    o.append(T((fs(0) + fs(0.1989)) / 2, fT(620), 'W = 119.4 kJ', 14, bold=True))
    o.append(T((fs(0) + fs(0.1989)) / 2, fT(150) + 5, sub('Q', '2') + ' = 59.7 kJ', 13, fill=LV, bold=True))
    o.append(T((fs(0) + fs(0.1989)) / 2, fT(900) - 8, '1 → 2 at 900 K', 13, fill=AC))
    for lab, sx, tt, an in (('1', 0, 900, 'end'), ('2', 0.1989, 900, 'start'), ('3', 0.1989, 300, 'start'), ('4', 0, 300, 'end')):
        o.append(C(fs(sx), fT(tt), 5, INK)); o.append(T(fs(sx) + (8 if an == 'start' else -8), fT(tt) + (16 if tt == 300 else -4), lab, 14, an, bold=True))
    o.append(brace(fs(0), fs(0.1989), y1 + 14, MUT))
    o.append(T((fs(0) + fs(0.1989)) / 2, y1 + 38, 'ΔS = 179.0 / 900 = 0.199 kJ/K', 13, fill=MUT))
    o.append(T(550, y1 + 60, sub('Q', '1') + ' = whole area = 179.0 kJ', 13, fill=AC, bold=True))
    return 414, ''.join(o)


FIG[4] = (f4, 'The worked example’s Carnot cycle on 1 kg of air between 900 K and 300 K. Left: the four states it passes through (the p-V shape is a sketch, '
              'because the volume grows thirtyfold). Right: the same cycle on T-S axes is a rectangle 0.199 kJ/K wide; its parts are W = 119.4 kJ and Q₂ = 59.7 kJ.',
          'Left: a p-V sketch of the Carnot cycle with states 1 to 4 and their volumes and pressures, heat in along 1 to 2 at 900 K and out along 3 to 4 at 300 K. '
          'Right: a temperature-entropy rectangle from 300 K to 900 K and 0.199 kJ/K wide, the upper part labelled work 119.4 kJ and the lower part heat rejected 59.7 kJ.')


# ---- 3.5 two reversible engines in series fix two temperatures ----
def f5():
    o = []
    ys = [40, 210, 380]
    labs = ['Source at T₁ = 468.75 K', 'Middle reservoir at T₂ = 375 K', 'Sink at 300 K']
    fills = [(ACS, AC), (NXS, NX), (LVS, LV)]
    for y, lab, (f, s) in zip(ys, labs, fills):
        o.append(boxt(150, y, 420, 42, [lab], f, s, 14))
    for (ya, yb, name, qin, qout, w, eta) in [(82, 210, 'A', '100 kJ', '80 kJ', '20 kJ', '20 %'),
                                            (252, 380, 'B', '80 kJ', '64 kJ', '16 kJ', '20 %')]:
        cy = (ya + yb) / 2
        o.append(device(360, cy, 30, name))
        o.append(arrow(360, ya + 2, 360, cy - 32, AC)); o.append(arrow(360, cy + 32, 360, yb - 2, LV))
        o.append(Tb(348, ya + 26, qin, 14, 'end', INK, True)); o.append(Tb(348, yb - 10, qout, 14, 'end', INK, True))
        o.append(arrow(392, cy, 470, cy, NX)); o.append(T(480, cy + 5, f'W = {w}', 14, 'start', NX, True))
        o.append(T(320, cy + 5, f'η = {eta}', 13, 'end', MUT))
    o.append(T(360, 450, 'Together: work 36 kJ from 100 kJ, η = 0.36 = 1 − 300 / 468.75', 14, bold=True))
    return 466, ''.join(o)


FIG[5] = (f5, 'The worked example with 100 kJ taken from the source: engine A keeps 20 kJ as work and passes 80 kJ down to the 375 K reservoir; engine B keeps 16 kJ '
              'and rejects 64 kJ at 300 K. Each heat ratio is a temperature ratio (80/100 = 375/468.75), and the pair works like one reversible engine of 36 %.',
          'Three reservoirs stacked: 468.75 K, 375 K and 300 K, with reversible engine A between the top two and engine B between the bottom two. '
          'A takes 100 kJ, gives 20 kJ of work and rejects 80 kJ; B takes 80 kJ, gives 16 kJ and rejects 64 kJ. Overall efficiency 0.36.')


# ---- 3.6 the cycle's two heat terms and the sign of the sum ----
def f6():
    o = []
    o.append(boxt(30, 34, 230, 44, ['Source at 600 K'], ACS, AC, 14))
    o.append(boxt(30, 258, 230, 44, ['Sink at 300 K'], LVS, LV, 14))
    o.append(device(145, 168, 32, 'cycle'))
    o.append(arrow(145, 80, 145, 134, AC)); o.append(Tb(133, 110, 'Q = +500 kJ', 14, 'end', AC, True))
    o.append(arrow(145, 202, 145, 254, LV)); o.append(Tb(133, 232, 'Q = −300 kJ', 14, 'end', LV, True))
    o.append(arrow(179, 168, 250, 168, NX)); o.append(T(214, 156, 'W = 200 kJ', 13, fill=NX, bold=True))
    # number line
    x0, x1 = 300, 690; fx = lambda v: x0 + (v + 1.2) / 2.2 * (x1 - x0)
    y = 200
    o.append(T(495, 40, 'Each term Q/T, in kJ/K', 14, bold=True))
    o.append(R(fx(0), 60, fx(0.8333) - fx(0), 26, ACS, AC, 3)); o.append(T(fx(0.8333) + 6, 79, '+500/600 = +0.833', 13, 'end', INK, True))
    o.append(R(fx(-1), 96, fx(0) - fx(-1), 26, LVS, LV, 3)); o.append(T(fx(-1) + 6, 115, '−300/300 = −1.000', 13, 'start', INK, True))
    o.append(L(fx(0), 52, fx(0), y + 8, MUT, 1.5, '4 4'))
    o.append(L(x0, y, x1, y, L2, 1.5))
    for v in (-1, -0.5, 0, 0.5, 1):
        o += [L(fx(v), y, fx(v), y + 5, L2, 1.5), T(fx(v), y + 20, neg(f'{v:g}'), 13, fill=MUT)]
    o.append(C(fx(-0.1667), y, 8, NX)); o.append(T(fx(-0.1667) - 12, y - 14, 'sum = −0.167', 14, 'end', NX, True))
    o.append(T(x0, y + 48, '< 0: irreversible', 14, 'start', LV, True))
    o.append(T(x1, y + 48, '> 0: impossible', 14, 'end', MUT, True))
    o.append(T(fx(0), y + 72, '= 0: reversible', 14, 'middle', AC, True))
    o.append(T(495, y + 104, 'η = 200/500 = 40 %, below the Carnot 50 %', 13, fill=MUT))
    return 330, ''.join(o)


FIG[6] = (f6, 'The worked example’s cycle: +500 kJ enters at 600 K and 300 kJ leaves at 300 K. Its two Q/T terms, +0.833 and −1.000 kJ/K, add to −0.167 kJ/K, '
              'which falls in the irreversible part of the line.',
          'Left: a cycle taking 500 kJ from a 600 K source, rejecting 300 kJ to a 300 K sink and giving 200 kJ of work. Right: two bars for the terms plus 0.833 and minus 1.000 kJ/K, '
          'and a number line with the sum minus 0.167 marked in the region labelled irreversible; zero is reversible and positive is impossible.')


# ---- 3.7 the worked example on T-s axes: constant p versus constant v then isothermal ----
def f7():
    o = []
    x0, x1, y0, y1 = 100, 660, 40, 320
    fx = lambda s: x0 + s / 0.8 * (x1 - x0)
    fy = lambda t: y1 - (t - 250) / 400 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.2, 0.4, 0.6, 0.8], [300, 400, 500, 600], fx, fy,
                  's − s₁, kJ/(kg·K)', 'T, K', lambda v: f'{v:g}'))
    sp = lambda t: 1.005 * math.log(t / 300)
    sv = lambda t: 0.718 * math.log(t / 300)
    pts = [(fx(sp(300 + 300 * i / 80)), fy(300 + 300 * i / 80)) for i in range(81)]
    poly = [(fx(0), y1)] + pts + [(fx(sp(600)), y1)]
    o.append(f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in poly)}" style="fill:var(--accent-soft);stroke:none"/>')
    o.append(P(pts, AC, 3))
    o.append(P([(fx(sv(300 + 300 * i / 80)), fy(300 + 300 * i / 80)) for i in range(81)], LV, 3, '7 5'))
    o.append(L(fx(sv(600)), fy(600), fx(sp(600)), fy(600), LV, 3, '7 5'))
    o.append(C(fx(0), fy(300), 6, INK)); o.append(C(fx(sp(600)), fy(600), 6, INK)); o.append(C(fx(sv(600)), fy(600), 5, LV))
    o.append(T(fx(0) + 10, fy(300) + 18, '1: 300 K', 14, 'start', bold=True))
    o.append(T(fx(sp(600)) + 10, fy(600) + 5, '2: 600 K, 0.697', 14, 'start', bold=True))
    o.append(T(fx(sv(600)) - 8, fy(600) - 12, 'v = const to 0.498', 13, 'end', LV, True))
    o.append(T(fx(0.6) - 6, fy(600) - 12, 'T = const', 13, 'end', LV))
    o.append(T(fx(0.5) + 6, fy(470), 'p = const', 14, 'start', AC, True))
    o.append(Tb(fx(0.45), fy(328), 'area = heat = 1.005 × 300 = 301.5 kJ/kg', 13, 'middle', AC, True))
    o.append(T(380, 394, 'For 2 kg: ΔS = 2 × 0.6966 = 1.393 kJ/K by either route', 14, bold=True))
    return 406, ''.join(o)


FIG[7] = (f7, 'The worked example per kilogram of air. Heating at constant pressure from 300 K to 600 K (solid) and the check route, constant volume then isothermal (dashed), '
              'end at the same entropy, 0.697 kJ/(kg·K) above the start. The constant-volume line is the steeper one; the shaded area under the solid path is the heat.',
          'Temperature against entropy for air. A solid constant-pressure curve rises from 300 K to 600 K over 0.697 kJ/(kg·K), with the area under it shaded, 301.5 kJ/kg. '
          'A steeper dashed constant-volume curve reaches 600 K at 0.498, then a dashed horizontal isotherm reaches the same end point.')


# ---- 3.8 mixing hot and cold water: two entropy changes and their sum ----
def f8():
    o = []
    x0, x1 = 90, 650; fx = lambda t: x0 + (t - 285) / 75 * (x1 - x0)
    y = 70
    o.append(T(360, 26, 'Temperatures, K', 14, bold=True))
    o.append(L(x0, y, x1, y, L2, 1.5))
    for t in (290, 300, 310, 320, 330, 340, 350, 360):
        o += [L(fx(t), y, fx(t), y + 5, L2, 1.5), T(fx(t), y + 20, str(t), 13, fill=MUT)]
    o.append(C(fx(353), y, 7, AC)); o.append(T(fx(353), y - 12, '2 kg at 353 K', 13, 'middle', AC, True))
    o.append(C(fx(293), y, 7, LV)); o.append(T(fx(293), y - 12, '3 kg at 293 K', 13, 'middle', LV, True))
    o.append(C(fx(317), y, 7, NX)); o.append(T(fx(317), y - 12, 'mix 317 K', 13, 'middle', NX, True))
    o.append(arrow(fx(350), y + 36, fx(320), y + 36, AC)); o.append(arrow(fx(296), y + 36, fx(314), y + 36, LV))
    o.append(T(fx(335), y + 58, 'hot water cools', 13, fill=AC)); o.append(T(fx(305), y + 58, 'cold warms', 13, fill=LV))
    # entropy bars
    bx0 = 360; sc = 300  # px per kJ/K
    yb = 200
    o.append(T(360, yb - 14, 'Entropy changes, kJ/K', 14, bold=True))
    o.append(L(bx0, yb - 2, bx0, yb + 120, MUT, 1.5, '4 4'))
    o.append(R(bx0 - 0.9008 * sc, yb + 6, 0.9008 * sc, 26, ACS, AC, 3)); o.append(T(bx0 - 8, yb + 24, 'hot water −0.9008', 13, 'end', INK, True))
    o.append(R(bx0, yb + 42, 0.9889 * sc, 26, LVS, LV, 3)); o.append(T(bx0 + 8, yb + 60, 'cold water +0.9889', 13, 'start', INK, True))
    o.append(R(bx0, yb + 82, 0.0882 * sc, 26, NXS, NX, 3)); o.append(T(bx0 + 0.0882 * sc + 8, yb + 100, 'sum = S_gen = +0.0882 > 0'.replace('S_gen', sub('S', 'gen')), 14, 'start', NX, True))
    o.append(T(bx0, yb + 142, '0', 13, fill=MUT))
    return 360, ''.join(o)


FIG[8] = (f8, 'The worked example: 2 kg of water at 353 K and 3 kg at 293 K settle at 317 K. The hot water loses 0.9008 kJ/K, the cold water gains 0.9889 kJ/K, '
              'and the difference, 0.0882 kJ/K, is the entropy generated by mixing.',
          'Top: a temperature scale with the hot water at 353 K and the cold water at 293 K moving to the mixed temperature 317 K. '
          'Below: a bar of minus 0.9008 kJ/K for the hot water, a longer bar of plus 0.9889 kJ/K for the cold water and a short bar for their sum, plus 0.0882 kJ/K.')


# ---- 3.9 entropy account of the air compressor (control volume) ----
def f9():
    o = []
    # compressor as a trapezoid
    o.append('<polygon points="250,90 430,130 430,230 250,270" style="fill:var(--panel);stroke:var(--accent);stroke-width:2.5"/>')
    o.append(T(340, 176, 'compressor', 14, bold=True)); o.append(T(340, 196, 'steady flow', 13, fill=MUT))
    o.append(R(232, 70, 216, 220, 'none', MUT, 10, 1.6, '6 5')); o.append(T(226, 300, 'control volume', 13, 'end', MUT))
    o.append(arrow(40, 180, 246, 180, AC, 3)); o.append(T(40, 160, 'in: 0.5 kg/s', 14, 'start', AC, True))
    o.append(T(40, 206, '100 kPa, 300 K', 13, 'start', MUT))
    o.append(arrow(434, 180, 690, 180, AC, 3)); o.append(T(690, 160, 'out: 400 kPa, 480 K', 14, 'end', AC, True))
    o.append(T(690, 206, 'Δs = +0.0745 kJ/(kg·K)', 13, 'end', MUT))
    o.append(arrow(340, 24, 340, 104, NX, 3)); o.append(T(352, 44, 'power in 95 kW', 14, 'start', NX, True))
    o.append(arrow(340, 252, 340, 330, LV, 3)); o.append(T(358, 324, 'heat out 4.55 kW to air at 300 K', 14, 'start', LV, True))
    # account
    y = 360
    o.append(T(40, y + 6, 'Entropy account, kW/K:', 14, 'start', bold=True))
    rows = [('carried out by the air  ṁ(s₂ − s₁)', '+0.0372', AC), ('carried by the heat lost  Q̇/T₀', '+0.0152', LV),
            ('generated inside  Ṡ', '+0.0524', NX)]
    for i, (a, b, c) in enumerate(rows):
        yy = y + 32 + i * 26
        o.append(T(60, yy, a.replace('Ṡ', sub('Ṡ', 'gen')), 14, 'start', c))
        o.append(T(470, yy, b, 14, 'end', c, True))
    o.append(L(380, y + 92, 480, y + 92, MUT, 1.5))
    o.append(T(60, y + 122, 'lost work T₀Ṡ = 300 × 0.0524 = 15.7 kW'.replace('Ṡ', sub('Ṡ', 'gen')), 14, 'start', MUT))
    return 500, ''.join(o)


FIG[9] = (f9, 'The worked example’s air compressor as a control volume. Air leaves with 0.0372 kW/K more entropy than it brought in, and the heat it loses carries '
              '0.0152 kW/K to the surroundings, but no entropy comes in with the 95 kW of work, so 0.0524 kW/K must be generated inside.',
          'A compressor inside a dashed control volume: air enters at 0.5 kg/s, 100 kPa and 300 K and leaves at 400 kPa and 480 K; 95 kW of power goes in and 4.55 kW of heat leaves to air at 300 K. '
          'An entropy account below lists 0.0372 kW/K carried out by the air, 0.0152 kW/K carried by the heat and 0.0524 kW/K generated.')


# ---- 3.10 absolute entropy from the Debye law, against the constant-cp formula ----
def f10():
    o = []
    x0, x1, y0, y1 = 100, 660, 40, 330
    fx = lambda t: x0 + t / 10 * (x1 - x0)
    fy = lambda s: y0 + (1.0 - s) / 5.0 * (y1 - y0)
    o.append(L(x0, fy(0), x1, fy(0), L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    for t in (0, 2, 4, 6, 8, 10):
        o += [L(fx(t), fy(0), fx(t), fy(0) + 5, L2, 1.5), T(fx(t), fy(0) + 20, str(t), 13, fill=MUT)]
    for s in (1, 0, -1, -2, -3, -4):
        o += [L(x0 - 5, fy(s), x0, fy(s), L2, 1.5), T(x0 - 9, fy(s) + 4.5, neg(s), 13, 'end', MUT)]
    o.append(T(x1, fy(0) + 40, 'T, K', 14, 'end', MUT)); o.append(T(x0, y0 - 14, 'S, J/(mol·K)', 14, 'start', MUT))
    o.append(curve(lambda t: 0.002 * t ** 3 / 3, 0, 10, fx, fy, 100, AC, 3))
    o.append(curve(lambda t: 2 / 3 + 2 * math.log(t / 10), 1.25, 10, fx, fy, 100, LV, 2.5, '7 5'))
    o.append(C(fx(10), fy(2 / 3), 6, AC))
    o.append(T(fx(10) - 10, fy(2 / 3) - 12, 'S(10 K) = 0.667', 14, 'end', AC, True))
    o.append(T(fx(1.0), fy(0.55), 'Debye solid: S = aT³/3, starts at 0', 14, 'start', AC, True))
    o.append(T(fx(1.6), fy(-3.3), 'constant c = 2 J/(mol·K):', 13, 'start', LV, True))
    o.append(T(fx(1.6), fy(-3.3) + 18, 'S = 0.667 + 2 ln(T/10) falls without limit', 13, 'start', LV))
    return 380, ''.join(o)


FIG[10] = (f10, 'The worked example’s solid, with c = 0.002T³ J/(mol·K): its entropy rises from zero to 0.667 J/(mol·K) at 10 K. If c stayed at its 10 K value of 2 J/(mol·K), '
                'the dashed curve would fall below zero and without limit as T falls, which the third law forbids.',
           'Entropy against temperature from 0 to 10 K. A solid curve S equals a T cubed over 3 starts at zero and reaches 0.667 J/(mol K) at 10 K. '
           'A dashed curve for constant heat capacity, 0.667 plus 2 ln(T/10), drops below minus 3 near 1 K.')


spec = make_spec(FIG)
