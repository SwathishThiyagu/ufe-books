"""Claude's hand-drawn figures for ch-mass-u6 (Adsorption, ion exchange, crystallization and membranes), one per chapter.
Every number comes from that chapter's worked examples. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def sb(base, s, size=11):
    return f'{base}<tspan baseline-shift="sub" font-size="{size}">{s}</tspan>'


def sp(base, s, size=11):
    return f'{base}<tspan baseline-shift="super" font-size="{size}">{s}</tspan>'


def path(d, c=AC, w=2.5, dash=None, fill='none'):
    da = f';stroke-dasharray:{dash}' if dash else ''
    return f'<path d="{d}" style="fill:{fill};stroke:{c};stroke-width:{w}{da}"/>'


def curve(fn, x0, x1, fx, fy, n=120, ylo=None, yhi=None):
    """polyline points of y = fn(x), clipped to [ylo, yhi]"""
    pts = []
    for i in range(n + 1):
        x = x0 + (x1 - x0) * i / n
        y = fn(x)
        if ylo is not None and y < ylo: break
        if yhi is not None and y > yhi: continue
        pts.append((fx(x), fy(y)))
    return pts


# ---- 1 the path into a grain, and the batch example ----
def f1():
    o = []
    cx, cy, r = 215, 220, 125
    o.append(T(10, 24, 'One grain of activated carbon (sketch)', 14, 'start', INK, bold=True))
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r + 22}" style="fill:none;stroke:{L2};stroke-width:1.5;stroke-dasharray:6 5"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" style="fill:var(--line);stroke:{INK};stroke-width:2"/>')
    # macropore from the surface into the grain, with two branches
    o.append(path(f'M{cx - r - 2},{cy - 20} C{cx - 70},{cy - 18} {cx - 40},{cy - 4} {cx + 10},{cy}', FIGBG, 24))
    o.append(path(f'M{cx - 50},{cy - 8} C{cx - 30},{cy - 50} {cx - 5},{cy - 66} {cx + 22},{cy - 80}', FIGBG, 11))
    o.append(path(f'M{cx - 10},{cy} C{cx + 5},{cy + 34} {cx + 26},{cy + 52} {cx + 52},{cy + 68}', FIGBG, 11))
    mic = ((cx + 20, cy - 79, cx + 58, cy - 96), (cx + 16, cy - 76, cx + 44, cy - 48), (cx - 26, cy - 44, cx - 62, cy - 74),
           (cx + 50, cy + 66, cx + 88, cy + 52), (cx + 50, cy + 68, cx + 58, cy + 102), (cx + 8, cy + 26, cx + 44, cy + 10))
    for (x1, y1, x2, y2) in mic:
        o.append(L(x1, y1, x2, y2, FIGBG, 4.5))
        for t in (0.4, 0.75, 1.0):
            o.append(f'<circle cx="{x1 + (x2 - x1) * t:.1f}" cy="{y1 + (y2 - y1) * t:.1f}" r="3.4" style="fill:{AC}"/>')
    for (x, y) in ((cx - 95, cy - 33), (cx - 60, cy - 26), (cx - 25, cy - 12), (cx - 85, cy - 7), (cx - 45, cy + 6)):
        o.append(f'<circle cx="{x}" cy="{y}" r="3.4" style="fill:{AC}"/>')
    # path and labels
    o.append(L(8, cy - 20, cx - r - 6, cy - 20, LV, 2.5, arrow='l'))
    o.append(T(8, cy - 62, 'bulk', 13, 'start', LV, bold=True)); o.append(T(8, cy - 46, 'fluid', 13, 'start', LV, bold=True))
    o.append(T(8, cy + 14, '1 film', 13, 'start', INK, bold=True))
    o.append(L(46, cy + 4, cx - r - 12, cy - 12, L2, 1.2))
    o.append(T(cx - 70, cy - r - 36, '2 macropore', 13, 'middle', INK, bold=True))
    o.append(L(cx - 70, cy - r - 30, cx - 70, cy - 24, L2, 1.2))
    o.append(T(cx + 90, cy - r - 36, '3 micropores (under 2 nm)', 13, 'middle', INK, bold=True))
    o.append(L(cx + 70, cy - r - 30, cx + 52, cy - 96, L2, 1.2))
    o.append(T(cx + 40, cy + r + 46, 'adsorbed molecules on the pore walls', 13, 'middle', AC, bold=True))
    o.append(L(cx + 40, cy + r + 32, cx + 58, cy + 106, AC, 1.2))
    # numbers
    o.append(boxt(420, 40, 286, 150, ['batch test', '2.00 g carbon in 100 mL', sb('C', '0') + ' = 50 → ' + sb('C', 'e') + ' = 10 mg/L', 'removed (50 − 10) × 0.100 = 4.0 mg',
                                     'q = 4.0/2.00 = 2.0 mg/g'], ACS, AC, 14, bold_first=True))
    o.append(boxt(420, 206, 286, 104, ['scale-up', '1000 L to 10 mg/L: 40 000 mg', '40 000/2.0 = 20 kg carbon'], PANEL, L2, 14, bold_first=True))
    o.append(boxt(420, 326, 286, 80, ['1000 m²/g ≈ 4 tennis courts', 'benzene monolayer ≈ 0.32 g/g'], PANEL, L2, 14))
    return 410, ''.join(o)
FIG[1] = (f1, 'The solute crosses the fluid film round the grain (1), travels along a macropore (2) and is held on the walls of the micropores (3), where most of the area lies. The boxes give the chapter\'s worked examples: a batch test giving q = 2.0 mg/g, the 20 kg of carbon needed for 1000 L, and the monolayer estimate for 1000 m²/g.',
          'A circular grain with a dashed film around it, a wide macropore branching into narrow micropores lined with adsorbed molecules, an arrow from the bulk fluid into the grain, and three boxes with the batch-test numbers.')


# ---- 2 Langmuir and Freundlich fits ----
def f2():
    o = []
    Cs, qs = [0.5, 1.0, 2.0, 5.0], [17.1, 24.0, 30.0, 35.3]
    x0, x1, y0, y1 = 60, 400, 40, 340
    fx = lambda c: x0 + (x1 - x0) * c / 10
    fy = lambda q: y1 - (y1 - y0) * q / 50
    o.append(axes(x0, x1, y0, y1, [0, 2, 4, 6, 8, 10], [0, 10, 20, 30, 40, 50], fx, fy, 'equilibrium C (mg/L)', 'q (mg/g)'))
    o.append(L(x0, fy(40), x1, fy(40), L2, 1.5, '6 4'))
    o.append(T(x1 - 4, fy(40) - 7, sb('q', 'm') + ' = 40', 13, 'end', MUT))
    o.append(P(curve(lambda c: 40 * 1.5 * c / (1 + 1.5 * c), 0, 10, fx, fy), AC, 2.8))
    o.append(P(curve(lambda c: 22.66 * c ** 0.3106, 0.02, 10, fx, fy, yhi=50), NX, 2.4, '7 5'))
    for c, q in zip(Cs, qs): o.append(C(fx(c), fy(q), 5.5, INK))
    o.append(C(fx(2), fy(30), 7, LV)); o.append(Tb(fx(2) + 10, fy(30) + 22, '(2.0, 30)', 13, 'start', LV, bold=True))
    o.append(C(fx(0.667), fy(20), 7, LV)); o.append(Tb(fx(0.667) + 12, fy(20) + 16, '(0.667, 20)', 13, 'start', LV, bold=True))
    o.append(Tb(fx(7.2), fy(36.6) + 24, 'Langmuir', 14, 'middle', AC, bold=True))
    o.append(Tb(fx(7.6), fy(46.3) - 12, 'Freundlich 22.7' + sp('C', '0.311'), 13, 'middle', NX, bold=True))
    o.append(T(fx(10) - 4, fy(46.3) + 16, '46.3', 12, 'end', NX)); o.append(T(fx(10) - 2, fy(37.5) + 18, '37.5', 12, 'end', AC))
    # linear Langmuir plot
    X0, X1, Y0, Y1 = 470, 700, 70, 300
    gx = lambda c: X0 + (X1 - X0) * c / 6
    gy = lambda v: Y1 - (Y1 - Y0) * v / 0.16
    o.append(T((X0 + X1) / 2, 30, 'Langmuir test: C/q against C', 14, 'middle', INK, bold=True))
    o.append(axes(X0, X1, Y0, Y1, [0, 2, 4, 6], [0, 0.04, 0.08, 0.12, 0.16], gx, gy, 'C (mg/L)', 'C/q (g/L)', yfmt=lambda v: f'{v:.2f}'))
    o.append(L(gx(0), gy(0.01671), gx(6), gy(0.01671 + 0.02498 * 6), AC, 2.5))
    for c, q in zip(Cs, qs): o.append(C(gx(c), gy(c / q), 5.5, INK))
    o.append(Tb(gx(3.4), gy(0.115), 'slope 0.0250 = 1/' + sb('q', 'm'), 13, 'middle', AC))
    o.append(C(gx(0), gy(0.01671), 5, AC)); o.append(Tb(gx(0.25), gy(0.0167) + 20, 'intercept 0.0167', 13, 'start', AC))
    o.append(boxt(470, 352, 230, 58, [sb('q', 'm') + ' = 40.0 mg/g', sb('K', 'L') + ' = 0.0250/0.0167 = 1.50 L/mg'], ACS, AC, 13))
    return 420, ''.join(o)
FIG[2] = (f2, 'Left: the four measured points (black), the Langmuir fit q = 40 × 1.5C/(1 + 1.5C) levelling at 40 mg/g, and the Freundlich fit, which has no plateau and overshoots at 10 mg/L (46.3 against 37.5 mg/g). The two large points are the first worked example. Right: the straight Langmuir plot of C/q against C that gives the constants.',
          'Two graphs. Left, loading q against equilibrium concentration with four data points, a solid Langmuir curve approaching a dashed line at 40 mg/g and a dashed Freundlich curve that keeps rising. Right, C/q against C with the same four points on a straight line of slope 0.0250 and intercept 0.0167.')


# ---- 3 breakthrough curve ----
def f3():
    o = []
    t = [0, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
    r = [0, 0.01, 0.05, 0.15, 0.35, 0.60, 0.80, 0.92, 0.97, 0.99, 1.0]
    x0, x1, y0, y1 = 60, 470, 50, 340
    fx = lambda v: x0 + (x1 - x0) * v / 120
    fy = lambda v: y1 - (y1 - y0) * v / 1.0
    # area above the curve up to t_b (solute held at the break point)
    pts = [(fx(0), fy(1))] + [(fx(a), fy(1))for a in (20, 30)] + [(fx(30), fy(0.05)), (fx(20), fy(0.01)), (fx(0), fy(0))]
    o.append(f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pts)}" style="fill:{ACS}"/>')
    o.append(axes(x0, x1, y0, y1, [0, 20, 40, 60, 80, 100, 120], [0, 0.25, 0.5, 0.75, 1.0], fx, fy, 'time (min)', sb('C/C', '0') + ' at the outlet', yfmt=lambda v: f'{v:g}'))
    o.append(P([(fx(a), fy(b)) for a, b in zip(t, r)], AC, 2.8))
    for a, b in zip(t, r): o.append(C(fx(a), fy(b), 4.5, INK))
    o.append(L(fx(30), fy(0.05), fx(30), y1, LV, 2, '5 4'))
    o.append(Tb(fx(30), fy(0.05) - 16, sb('t', 'b') + ' = 30', 13, 'middle', LV, bold=True))
    o.append(L(fx(56.55), fy(1.0), fx(56.55), y1, NX, 2, '5 4'))
    o.append(Tb(fx(56.55) - 4, fy(0.86), sb('t', 's') + ' = 56.6', 13, 'end', NX, bold=True))
    o.append(L(fx(90), fy(0.97), fx(90), y1, L2, 1.5, '5 4'))
    o.append(Tb(fx(90) + 6, fy(0.6), 'exhaustion ≈ 90', 12, 'start', MUT))
    o.append(T(fx(14), fy(0.55), 'held at', 13, 'middle', AC, bold=True))
    o.append(T(fx(14), fy(0.55) + 17, 'break point', 13, 'middle', AC, bold=True))
    o.append(T(fx(14), fy(0.55) + 34, '29.6 min', 13, 'middle', AC))
    # bed sketch at the break point
    bx, bt, bw, bh = 540, 70, 70, 260
    hU = bh * (1 - 0.28 / 0.60)
    o.append(T(bx + bw / 2, 40, 'bed at ' + sb('t', 'b'), 14, 'middle', INK, bold=True))
    o.append(R(bx, bt, bw, hU, ACS, AC, 0, 2))
    o.append(f'<rect x="{bx}" y="{bt + hU:.1f}" width="{bw}" height="{bh - hU:.1f}" style="fill:{PANEL};stroke:{AC};stroke-width:2"/>')
    o.append(f'<rect x="{bx}" y="{bt + hU - 30:.1f}" width="{bw}" height="100" style="fill:{NXS};stroke:none;fill-opacity:0.8"/>')
    o.append(R(bx, bt, bw, bh, 'none', INK, 0, 2))
    o.append(T(bx + bw / 2, bt + hU / 2 - 6, 'used', 13, 'middle', AC, bold=True))
    o.append(T(bx + bw / 2, bt + hU / 2 + 10, '0.32 m', 13, 'middle', AC))
    o.append(T(bx + bw / 2, bt + hU + 30, 'MTZ', 13, 'middle', NX, bold=True))
    o.append(L(bx + bw + 10, bt + hU, bx + bw + 10, bt + bh, NX, 2))
    o.append(L(bx + bw + 6, bt + hU, bx + bw + 14, bt + hU, NX, 2)); o.append(L(bx + bw + 6, bt + bh, bx + bw + 14, bt + bh, NX, 2))
    o.append(T(bx + bw + 18, bt + hU + (bh - hU) / 2, 'LUB', 13, 'start', NX, bold=True))
    o.append(T(bx + bw + 18, bt + hU + (bh - hU) / 2 + 16, '0.28 m', 13, 'start', NX))
    o.append(T(bx - 8, bt + 4, 'feed', 12, 'end', LV)); o.append(T(bx - 8, bt + 18, '80 mg/L', 12, 'end', LV))
    o.append(T(bx - 8, bt + bh, 'H = 0.60 m', 12, 'end', MUT))
    o.append(boxt(60, 396, 640, 54, [sb('q', 'b') + ' = 80 × 2 × 29.6/1500 = 3.16 mg/g;   ' + sb('q', 'sat') + ' = 80 × 2 × 56.55/1500 = 6.03 mg/g',
                                    'LUB = 0.60 × (1 − 30/56.55) = 0.28 m;   a 1.2 m bed breaks through at 86.5 min'], PANEL, L2, 13))
    return 460, ''.join(o)
FIG[3] = (f3, 'The measured breakthrough curve of the worked example. The shaded area above the curve up to the break point (30 min) is the dye held then; the whole area above the curve gives the stoichiometric time 56.6 min. At the break point the bed is used to 0.32 m and the last 0.28 m, the length of unused bed, is still partly fresh.',
          'Outlet concentration ratio against time rising in an S-shape from zero at 20 minutes to one at 110 minutes, with the break point at 30 minutes, the stoichiometric time at 56.6 minutes and exhaustion near 90 minutes marked; beside it a column split into a used part of 0.32 metres and an unused length of 0.28 metres.')


# ---- 4 softener column and its cycle ----
def f4():
    o = []
    bx, bt, bw, bh = 130, 80, 120, 260
    o.append(R(bx, bt - 20, bw, bh + 40, PANEL, INK, 18, 2))
    zones = [(0.45, ACS, 'Ca form', '(exhausted)'), (0.20, NXS, 'exchange', 'zone'), (0.35, LVS, 'Na form', '(fresh)')]
    y = bt
    for f, col, a, b in zones:
        h = bh * f
        o.append(f'<rect x="{bx + 6}" y="{y:.1f}" width="{bw - 12}" height="{h:.1f}" style="fill:{col}"/>')
        o.append(T(bx + bw / 2, y + h / 2 - 2, a, 13, 'middle', INK, bold=True))
        o.append(T(bx + bw / 2, y + h / 2 + 14, b, 12, 'middle', MUT))
        y += h
    o.append(L(bx + bw / 2, 16, bx + bw / 2, bt - 22, LV, 2.5, arrow='l'))
    o.append(T(bx + bw / 2 + 10, 22, 'hard water 500 L/h, 4.0 meq/L ' + sp('Ca', '2+'), 13, 'start', LV, bold=True))
    o.append(L(bx + bw / 2, bt + bh + 22, bx + bw / 2, bt + bh + 60, NX, 2.5, arrow='x'))
    o.append(T(bx + bw / 2 + 10, bt + bh + 54, 'soft water, 4.0 meq/L ' + sp('Na', '+'), 13, 'start', NX, bold=True))
    o.append(T(bx - 10, bt + bh / 2, '16 L', 14, 'end', INK, bold=True))
    o.append(T(bx - 10, bt + bh / 2 + 16, 'resin', 13, 'end', MUT))
    o.append(T(bx - 10, 128, 'zone moves', 12, 'end', MUT)); o.append(L(bx - 30, 136, bx - 30, 170, MUT, 1.5, arrow='m'))
    # reaction
    o.append(R(330, 46, 376, 72, ACS, AC, 8, 2))
    o.append(T(518, 74, '2R–' + sb('SO', '3') + 'Na + ' + sp('Ca', '2+') + ' ⇌ (R–' + sb('SO', '3') + sb(')', '2') + 'Ca + 2' + sp('Na', '+'), 13))
    o.append(T(518, 104, 'one ' + sp('Ca', '2+') + ' in, two ' + sp('Na', '+') + ' out: equivalents equal', 13))
    # cycle on an ellipse
    cx, cy, rx, ry = 520, 262, 120, 92
    bw2, bh2 = 58, 22
    pos = {'service': (cx, cy - ry), 'backwash': (cx + rx, cy), 'regenerate': (cx, cy + ry), 'rinse': (cx - rx, cy)}
    o.append(arc(cx + bw2, cy - ry, cx + rx, cy - bh2 - 2, 0.3, L2, 2, arrow='m'))
    o.append(arc(cx + rx, cy + bh2 + 2, cx + bw2 + 2, cy + ry, 0.3, L2, 2, arrow='m'))
    o.append(arc(cx - bw2, cy + ry, cx - rx, cy + bh2 + 2, 0.3, L2, 2, arrow='m'))
    o.append(arc(cx - rx, cy - bh2 - 2, cx - bw2 - 2, cy - ry, 0.3, L2, 2, arrow='m'))
    sub = {'service': '8 h, 16 eq', 'backwash': 'bed lifted', 'regenerate': '2.4 kg NaCl', 'rinse': 'excess brine out'}
    for a, (X, Y) in pos.items():
        o.append(R(X - bw2, Y - bh2, 2 * bw2, 2 * bh2, ACS if a == 'regenerate' else PANEL, AC, 8, 2))
        o.append(T(X, Y - 3, a, 13, 'middle', INK, bold=True))
        o.append(T(X, Y + 13, sub[a], 12, 'middle', MUT))
    o.append(T(cx, cy - 8, '150 g NaCl per L', 12, 'middle', MUT))
    o.append(T(cx, cy + 8, 'stoich. 935 g', 12, 'middle', MUT))
    o.append(T(cx, cy + 25, 'used 2.57 ×', 12, 'middle', AC, bold=True))
    return 400, ''.join(o)
FIG[4] = (f4, 'The softener of the worked example. Hard water enters the top of 16 L of sodium-form resin; an exchange zone moves down, leaving calcium-form resin above it, and the water leaves with the same 4.0 meq/L as sodium. After the 8 h run (16 eq) the bed is backwashed, regenerated with 2.4 kg of salt, 2.57 times the stoichiometric 935 g, and rinsed.',
          'A resin column divided from top to bottom into calcium-form resin, an exchange zone and fresh sodium-form resin, with hard water entering at the top and soft water leaving at the bottom; beside it the exchange reaction and a four-step cycle of service, backwash, regenerate and rinse.')


# ---- 5 solubility curve and the cooling path ----
def f5():
    o = []
    x0, x1, y0, y1 = 70, 690, 40, 320
    fx = lambda T_: x0 + (x1 - x0) * T_ / 80
    fy = lambda c: y1 - (y1 - y0) * c / 60
    sol = lambda T_: 20 * 2 ** ((T_ - 20) / 40)
    ss = lambda T_: sol(T_ + 12)
    Tss = 20 + 40 * math.log2(3) - 12            # supersolubility reaches 60 here
    sol_pts = curve(sol, 0, 80, fx, fy, 100)
    ss_pts = curve(ss, 0, Tss, fx, fy, 100)
    poly = lambda pts: " ".join(f"{a:.1f},{b:.1f}" for a, b in pts)
    o.append(f'<polygon points="{poly(ss_pts)} {fx(0):.1f},{fy(60):.1f}" style="fill:{NXS};fill-opacity:0.7"/>')
    o.append(f'<polygon points="{poly(sol_pts)} {fx(80):.1f},{fy(60):.1f} {poly(list(reversed(ss_pts)))}" style="fill:{ACS};fill-opacity:0.7"/>')
    o.append(axes(x0, x1, y0, y1, [0, 10, 20, 30, 40, 50, 60, 70, 80], [0, 10, 20, 30, 40, 50, 60], fx, fy, 'temperature (°C)', 'g solute per 100 g water'))
    o.append(P(sol_pts, AC, 3))
    o.append(P(ss_pts, NX, 2.2, '7 5'))
    o.append(T(fx(8), fy(53), 'labile zone', 14, 'start', NX, bold=True))
    o.append(T(fx(8), fy(53) + 17, 'nuclei form on their own', 12, 'start', NX))
    o.append(T(fx(56), fy(14), 'unsaturated', 14, 'middle', MUT, bold=True))
    o.append(T(fx(64), fy(30), 'metastable zone', 13, 'start', AC, bold=True))
    o.append(T(fx(64), fy(30) + 15, '(between the curves)', 12, 'start', AC))
    o.append(L(fx(63.5), fy(31), fx(51), fy(37), AC, 1.2))
    o.append(T(fx(73), fy(46), 'solubility', 13, 'start', AC, bold=True))
    o.append(T(fx(57), fy(57.5), 'supersolubility (sketch)', 13, 'end', NX, bold=True))
    # cooling path
    o.append(L(fx(60) - 8, fy(40), fx(20) + 10, fy(40), LV, 3, arrow='l'))
    o.append(L(fx(20), fy(40) + 8, fx(20), fy(20) - 9, INK, 2.5, '6 4'))
    o.append(C(fx(60), fy(40), 7, LV)); o.append(T(fx(61), fy(36), 'A  feed at 60 °C', 13, 'start', LV, bold=True))
    o.append(C(fx(20), fy(40), 7, NX)); o.append(T(fx(20), fy(40) - 14, 'B  S = 40/20 = 2.0', 13, 'middle', NX, bold=True))
    o.append(C(fx(48), fy(40), 5, NX)); o.append(T(fx(46.5), fy(40) - 30, 'unseeded nuclei ≈ 48 °C', 12, 'end', NX)); o.append(L(fx(46.6), fy(40) - 27, fx(47.8), fy(40) - 6, NX, 1.2))
    o.append(C(fx(20), fy(20), 7, INK)); o.append(T(fx(22), fy(16.5), 'C  mother liquor, 20 °C', 13, 'start', INK, bold=True))
    o.append(T(fx(19), fy(30), 'crystals form', 13, 'end', INK, bold=True))
    o.append(boxt(70, 384, 300, 56, ['feed 1000 kg: 285.7 kg solute, 714.3 kg water', 'at 20 °C the water holds 142.9 kg'], PANEL, L2, 13))
    o.append(boxt(390, 384, 316, 56, ['crystals 142.9 kg (50 %)', 'with 100 kg evaporated 162.9 kg (57 %)'], ACS, AC, 13))
    return 450, ''.join(o)
FIG[5] = (f5, 'The worked example on the solubility diagram. The feed saturated at 60 °C (A) cools at constant composition; without crystals it would reach B at 20 °C with S = 2.0, deep in the labile zone. Crystallization brings the liquor down to the solubility curve at C, releasing 142.9 kg of crystals per 1000 kg of feed. The supersolubility curve (sketched) is not fixed; seeding keeps the path in the metastable zone.',
          'Solubility in grams per 100 grams of water against temperature, rising from 20 at 20 degrees to 40 at 60 degrees, with a dashed supersolubility curve above it and the labile and metastable zones shaded; a horizontal arrow from the feed point at 60 degrees to point B at 20 degrees, then a dashed drop to the mother liquor point C on the curve.')


# ---- 6 free energy of a cluster ----
def f6():
    o = []
    k, T_, g, vm = 1.380649e-23, 298.15, 0.030, 4.5e-29
    kT = k * T_
    def dG(r_nm, S):
        r = r_nm * 1e-9
        return (4 * math.pi * r * r * g - 4 / 3 * math.pi * r ** 3 * kT * math.log(S) / vm) / kT
    x0, x1, y0, y1 = 70, 480, 40, 360
    fx = lambda r: x0 + (x1 - x0) * r / 2.5
    fy = lambda v: y0 + (y1 - y0) * (100 - v) / 130
    o.append(axes(x0, x1, y0, y1, [0, 0.5, 1.0, 1.5, 2.0, 2.5], [-30, 0, 20, 40, 60, 80, 100], fx, fy, 'cluster radius r (nm)', 'ΔG/kT', yfmt=neg))
    o.append(L(x0, fy(0), x1, fy(0), INK, 1.5))
    cols = {1.5: AC, 2.0: NX, 4.0: LV}
    rs = {1.5: (1.618, 79.9), 2.0: (0.946, 27.3), 4.0: (0.473, 6.8)}
    for S, col in cols.items():
        o.append(P(curve(lambda r: dG(r, S), 0, 2.5, fx, fy, 200, ylo=-30), col, 2.8))
        rc, gc = rs[S]
        o.append(L(fx(rc), fy(gc), fx(rc), fy(0), col, 1.5, '4 4'))
        o.append(C(fx(rc), fy(gc), 6, col))
    o.append(T(fx(1.618), fy(79.9) - 14, 'S = 1.5', 14, 'middle', AC, bold=True))
    o.append(T(fx(0.946), fy(27.3) - 14, 'S = 2', 14, 'middle', NX, bold=True))
    o.append(T(fx(0.92), fy(-24), 'S = 4', 14, 'start', LV, bold=True))
    o.append(T(fx(1.618) + 6, fy(0) + 18, 'r*', 13, 'start', AC, bold=True))
    o.append(boxt(510, 40, 196, 120, ['γ = 0.030 J/m²', sb('v', 'm') + ' = 4.5 × ' + sp('10', '−29') + ' m³, T = 298 K', 'r* = 2γ' + sb('v', 'm') + '/(kT ln S)'], PANEL, L2, 12))
    o.append(boxt(510, 172, 196, 176, ['at the peak', 'S = 1.5: r* 1.62 nm, 79.9 kT', '394 molecules', 'S = 2: r* 0.95 nm, 27.3 kT', '79 molecules',
                                      'S = 4: r* 0.47 nm, 6.8 kT', '10 molecules'], ACS, AC, 12, bold_first=True,
                    fills=[INK, AC, AC, NX, NX, LV, LV]))
    o.append(T(510, 380, 'smaller clusters redissolve,', 12, 'start', MUT))
    o.append(T(510, 396, 'larger ones grow', 12, 'start', MUT))
    return 404, ''.join(o)
FIG[6] = (f6, 'Free energy of forming a spherical cluster, ΔG = 4πr²γ − (4/3)πr³kT ln S/v<sub>m</sub>, for the worked example at three supersaturations. Each curve peaks at the critical radius r*; the barrier falls from 79.9 kT at S = 1.5 to 27.3 kT at S = 2, which multiplies the nucleation rate by about 10<sup>23</sup>.',
          'Three curves of free energy against cluster radius, each rising to a maximum and then falling: the S equal 1.5 curve peaks at 79.9 kT at 1.62 nanometres, the S equal 2 curve at 27.3 kT at 0.95 nanometres and the S equal 4 curve at 6.8 kT at 0.47 nanometres.')


# ---- 7 cooling and vacuum crystallizers ----
def f7():
    o = []
    vx, vy, vw, vh = 130, 90, 150, 200
    o.append(T(20, 26, 'Cooling crystallizer', 15, 'start', INK, bold=True))
    o.append(R(vx - 14, vy - 14, vw + 28, vh + 28, LVS, LV, 14, 2))
    o.append(R(vx, vy, vw, vh, PANEL, INK, 10, 2))
    o.append(f'<rect x="{vx + 6}" y="{vy + 30}" width="{vw - 12}" height="{vh - 36}" rx="6" style="fill:{ACS}"/>')
    o.append(L(vx + vw / 2, vy - 30, vx + vw / 2, vy + 120, INK, 2.5))
    o.append(P([(vx + vw / 2 - 32, vy + 126), (vx + vw / 2 + 32, vy + 114)], INK, 4))
    for (dx, dy) in ((24, 150), (52, 175), (104, 160), (124, 182), (30, 92), (118, 84)):
        x, y = vx + dx, vy + dy
        o.append(f'<rect x="{x}" y="{y}" width="8" height="8" style="fill:{AC}" transform="rotate(20 {x + 4} {y + 4})"/>')
    o.append(T(vx + vw / 2, vy + 62, 'magma, 20 °C', 13, 'middle', INK, bold=True))
    o.append(L(10, vy + 10, vx - 16, vy + 10, LV, 2.5, arrow='l'))
    o.append(T(10, vy - 22, 'feed 1000 kg/h', 12, 'start', LV, bold=True)); o.append(T(10, vy - 6, '30 %, 50 °C', 12, 'start', LV))
    o.append(L(vx + vw + 60, vy + 20, vx + vw + 16, vy + 20, AC, 2, arrow='n'))
    o.append(T(vx + vw + 20, vy + 6, 'water 15 °C', 12, 'start', AC))
    o.append(L(vx - 16, vy + vh - 20, vx - 60, vy + vh - 20, AC, 2, arrow='n'))
    o.append(T(vx - 64, vy + vh - 36, 'water 25 °C', 12, 'end', AC))
    o.append(T(vx - 64, vy + vh - 2, '3187 kg/h', 12, 'end', AC))
    o.append(L(vx + vw + 16, vy + vh - 10, vx + vw + 60, vy + vh - 10, NX, 2.5, arrow='x'))
    o.append(T(vx + vw + 18, vy + vh + 14, '160 kg/h crystals', 12, 'start', NX, bold=True))
    o.append(T(vx + vw + 18, vy + vh + 29, '+ 840 kg/h liquor', 12, 'start', NX))
    o.append(boxt(20, 352, 330, 70, ['Q = 114 000 + 19 200 kJ/h = 37.0 kW', 'Δ' + sb('T', 'lm') + ' = 12.43 K, A = 5.95 m²'], ACS, AC, 13))
    # vacuum crystallizer
    o.append(T(390, 26, 'Vacuum crystallizer', 15, 'start', INK, bold=True))
    wx, wy, ww, wh = 520, 120, 150, 170
    o.append(R(wx, wy, ww, wh, PANEL, INK, 10, 2))
    o.append(f'<rect x="{wx + 6}" y="{wy + 50}" width="{ww - 12}" height="{wh - 56}" rx="6" style="fill:{ACS}"/>')
    o.append(path(f'M{wx + 35},{wy + 50} q10,-14 20,0 q10,-14 20,0 q10,-14 20,0 q10,-14 20,0', AC, 1.6))
    o.append(T(wx + ww / 2, wy + 100, 'boils at 20 °C', 13, 'middle', INK, bold=True))
    o.append(T(wx + ww / 2, wy + 118, '≈ 2.3 kPa', 12, 'middle', MUT))
    o.append(L(wx + ww / 2, wy - 2, wx + ww / 2, wy - 38, MUT, 2.5, arrow='m'))
    o.append(R(wx + ww / 2 - 72, 40, 144, 38, PANEL, L2, 8, 1.5))
    o.append(T(wx + ww / 2, 64, 'condenser + ejector', 12, 'middle', MUT))
    o.append(T(wx + ww / 2 - 8, wy - 14, 'vapour 54.8 kg/h', 12, 'end', MUT, bold=True))
    o.append(L(390, wy + 80, wx - 2, wy + 80, LV, 2.5, arrow='l'))
    o.append(T(390, wy + 66, 'same feed, 50 °C', 12, 'start', LV, bold=True))
    o.append(L(wx + ww / 2, wy + wh + 2, wx + ww / 2, wy + wh + 30, NX, 2.5, arrow='x'))
    o.append(T(wx + ww / 2 - 10, wy + wh + 26, '171.0 kg/h crystals', 12, 'end', NX, bold=True))
    o.append(boxt(376, 352, 330, 70, ['2454V = 114 000 + 120(160 + 0.20V)', 'V = 54.8 kg/h, no cooling surface'], ACS, AC, 13))
    return 430, ''.join(o)
FIG[7] = (f7, 'The two worked examples. Left: a jacketed cooling crystallizer removes 37.0 kW (sensible heat plus heat of crystallization) into 3187 kg/h of cooling water across 5.95 m², giving 160 kg/h of crystals. Right: in a vacuum crystallizer the same feed boils at 20 °C under about 2.3 kPa; 54.8 kg/h of vapour carries the heat away and the yield rises to 171.0 kg/h.',
          'Left, a stirred vessel with a cooling jacket, feed entering, cooling water entering at 15 and leaving at 25 degrees, and magma with crystals leaving. Right, a closed vessel boiling at 20 degrees with vapour going up to a condenser and ejector, feed entering from the side and crystals leaving at the bottom.')


# ---- 8 MSMPR plot and mass distribution ----
def f8():
    o = []
    Ls = [0.2, 0.4, 0.6, 0.8]
    lns = [21.333, 20.333, 19.333, 18.333]
    x0, x1, y0, y1 = 70, 340, 60, 330
    fx = lambda L_: x0 + (x1 - x0) * L_ / 1.0
    fy = lambda v: y1 - (y1 - y0) * (v - 17) / 6
    o.append(T((x0 + x1) / 2, 28, 'ln n against L', 14, 'middle', INK, bold=True))
    o.append(axes(x0, x1, y0, y1, [0, 0.2, 0.4, 0.6, 0.8, 1.0], [17, 18, 19, 20, 21, 22, 23], fx, fy, 'crystal size L (mm)', 'ln n'))
    o.append(L(fx(0), fy(22.333), fx(1.0), fy(17.333), AC, 2.5))
    for a, b in zip(Ls, lns): o.append(C(fx(a), fy(b), 5.5, INK))
    o.append(C(fx(0), fy(22.333), 6.5, LV))
    o.append(Tb(fx(0.04), fy(22.333) - 14, 'ln n° = 22.33', 13, 'start', LV, bold=True))
    o.append(Tb(fx(0.55), fy(20.9), 'slope −5.0 per mm = −1/(Gτ)', 13, 'middle', AC))
    o.append(boxt(70, 392, 270, 58, ['Gτ = 0.20 mm, G = 0.10 mm/h', 'n° = 5.0 × ' + sp('10', '9') + ' per m³ mm'], ACS, AC, 13))
    # mass distribution
    X0, X1, Y0, Y1 = 410, 700, 60, 330
    gx = lambda L_: X0 + (X1 - X0) * L_ / 2.0
    m = lambda L_: (L_ / 0.2) ** 3 * math.exp(-L_ / 0.2) / 6 / 0.2
    mmax = m(0.6)
    gy = lambda v: Y1 - (Y1 - Y0) * v / (mmax * 1.15)
    o.append(T((X0 + X1) / 2, 28, 'mass of product by size', 14, 'middle', INK, bold=True))
    o.append(xaxis(X0, X1, Y1, [0, 0.5, 1.0, 1.5, 2.0], gx, 'crystal size L (mm)', fmt=lambda v: f'{v:g}'))
    o.append(L(X0, Y0, X0, Y1, L2, 1.5))
    tail = curve(m, 1.0, 2.0, gx, gy, 60)
    o.append(f'<polygon points="{gx(1.0):.1f},{Y1} {" ".join(f"{a:.1f},{b:.1f}" for a, b in tail)} {gx(2.0):.1f},{Y1}" style="fill:{NXS}"/>')
    o.append(P(curve(m, 0, 2.0, gx, gy, 160), AC, 2.8))
    for v, lab, col, dy in ((0.6, sb('L', 'D') + ' = 3Gτ = 0.60', LV, -10), (0.734, 'median 0.73', MUT, 14)):
        o.append(L(gx(v), gy(m(v)), gx(v), Y1, col, 1.6, '5 4'))
    o.append(Tb(gx(0.6), gy(mmax) - 12, sb('L', 'D') + ' = 3Gτ = 0.60 mm', 13, 'middle', LV, bold=True))
    o.append(T(gx(1.12), gy(mmax * 0.86), '26.5 % of the mass', 12, 'start', NX, bold=True))
    o.append(T(gx(1.12), gy(mmax * 0.86) + 15, 'above 1.0 mm', 12, 'start', NX, bold=True))
    o.append(boxt(410, 392, 290, 58, ['mass median 0.73 mm (grey dashes)', 'magma density 85 kg/m³'], PANEL, L2, 13))
    return 460, ''.join(o)
FIG[8] = (f8, 'The MSMPR worked example. Left: the four measured population densities fall on a straight line of ln n against L; its slope −5.0 per mm gives Gτ = 0.20 mm and its intercept gives n°. Right: the mass distribution L³e<sup>−L/Gτ</sup> that follows, peaking at the dominant size 0.60 mm, with 26.5 % of the mass above 1.0 mm.',
          'Left, a straight line falling from ln n of 22.33 at zero size through four data points to 18.33 at 0.8 millimetres. Right, a skewed hump of product mass against size peaking at 0.60 millimetres, with the tail above 1.0 millimetre shaded.')


# ---- 9 RO module and ED stack ----
def f9():
    o = []
    o.append(T(20, 26, 'Reverse osmosis', 15, 'start', INK, bold=True))
    mx, my, mw, mh = 190, 46, 300, 112
    o.append(R(mx, my, mw, mh, PANEL, INK, 8, 2))
    o.append(T(mx + mw / 2, my + 20, 'feed side, ΔP = 15 bar', 12, 'middle', MUT))
    for i in range(6):
        X = mx + 35 + i * 46
        o.append(L(X, my + 32, X, my + 60, AC, 1.6, arrow='n'))
    o.append(L(mx + 10, my + 68, mx + mw - 10, my + 68, AC, 4, '10 4'))
    o.append(T(mx + mw / 2, my + 92, 'membrane; permeate side below', 12, 'middle', MUT))
    o.append(L(20, my + 40, mx - 2, my + 40, LV, 2.5, arrow='l'))
    o.append(T(20, my + 30, 'feed 1000 L/h', 12, 'start', LV, bold=True)); o.append(T(20, my + 60, '2000 mg/L, π 1.70 bar', 12, 'start', LV))
    o.append(L(mx + mw + 2, my + 40, mx + mw + 50, my + 40, NX, 2.5, arrow='x'))
    o.append(T(mx + mw + 8, my + 28, 'retentate 250 L/h', 12, 'start', NX, bold=True))
    o.append(T(mx + mw + 8, my + 60, '7700 mg/L, π 6.53 bar', 12, 'start', NX))
    o.append(L(mx + 60, my + mh + 2, mx + 60, my + mh + 30, AC, 2.5, arrow='n'))
    o.append(T(mx + 70, my + mh + 26, 'permeate 750 L/h, 100 mg/L (R = 95 %)', 12, 'start', AC, bold=True))
    o.append(boxt(510, 128, 196, 74, ['net 15 − 4.03 = 10.97 bar', 'J = 3.0 × 10.97 = 32.9 L/m²h', 'A = 750/32.9 = 22.8 m²'], ACS, AC, 12))
    # ED stack
    o.append(T(20, 240, 'Electrodialysis (two cell pairs shown)', 15, 'start', INK, bold=True))
    ex0, ex1, ey, eh = 100, 620, 260, 110
    o.append(R(ex0 - 54, ey, 40, eh, PANEL, INK, 4, 2)); o.append(T(ex0 - 34, ey + eh / 2 + 7, '−', 22, 'middle', INK, bold=True))
    o.append(T(ex0 - 34, ey + eh + 18, 'cathode', 12, 'middle', MUT))
    o.append(R(ex1 + 14, ey, 40, eh, PANEL, INK, 4, 2)); o.append(T(ex1 + 34, ey + eh / 2 + 7, '+', 22, 'middle', INK, bold=True))
    o.append(T(ex1 + 34, ey + eh + 18, 'anode', 12, 'middle', MUT))
    mem = ['C', 'A', 'C', 'A', 'C']
    xs = [ex0 + i * (ex1 - ex0) / 4 for i in range(5)]
    for i in range(4):
        dil = (i % 2 == 0)
        o.append(f'<rect x="{xs[i] + 3:.1f}" y="{ey}" width="{xs[i + 1] - xs[i] - 6:.1f}" height="{eh}" style="fill:{LVS if dil else NXS}"/>')
        mid = (xs[i] + xs[i + 1]) / 2
        o.append(T(mid, ey + 20, 'diluate' if dil else 'concentrate', 12, 'middle', LV if dil else NX, bold=True))
    for X, mname in zip(xs, mem):
        o.append(L(X, ey - 6, X, ey + eh + 6, AC if mname == 'C' else NX, 4))
        o.append(T(X, ey + eh + 22, mname, 13, 'middle', AC if mname == 'C' else NX, bold=True))
    for i in (0, 2):
        mid = (xs[i] + xs[i + 1]) / 2
        o.append(L(mid - 12, ey + 50, xs[i] - 16, ey + 50, AC, 2.2, arrow='n'))
        o.append(T(mid, ey + 55, sp('Na', '+'), 13, 'start', AC, bold=True))
        o.append(L(mid + 12, ey + 86, xs[i + 1] + 16, ey + 86, NX, 2.2, arrow='x'))
        o.append(T(mid, ey + 91, sp('Cl', '−'), 13, 'end', NX, bold=True))
    o.append(T(ex0 - 54, ey + eh + 44, 'C = cation membrane, A = anion membrane', 12, 'start', MUT))
    o.append(boxt(400, ey + eh + 32, 306, 30, ['100 pairs: I = 7.6 A, 120 V, 0.92 kWh/m³'], ACS, AC, 13))
    return ey + eh + 70, ''.join(o)
FIG[9] = (f9, 'Top: the RO worked example, 1000 L/h split at 75 % recovery into 750 L/h of permeate at 100 mg/L and 250 L/h of retentate at 7700 mg/L; the net driving pressure is 15 − 4.03 = 10.97 bar. Bottom: in an electrodialysis stack cations cross cation membranes towards the cathode and anions cross anion membranes towards the anode, so alternate compartments are emptied (diluate) and filled (concentrate). The worked stack of 100 pairs needs 7.6 A and 0.92 kWh/m³.',
          'Top, a membrane module with feed entering on the left, retentate leaving on the right and permeate leaving below, labelled with flows and concentrations. Bottom, an electrodialysis stack between a cathode and an anode with alternating cation and anion membranes, sodium ions moving left and chloride ions moving right out of the diluate compartments.')


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}


def drop_sources():
    """university-hosted or university-run pages the book must not list"""
    return ['ocw.mit.edu', 'nptel.ac.in', 'openstax.org']
