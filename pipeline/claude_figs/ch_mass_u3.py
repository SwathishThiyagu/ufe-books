"""Claude's hand-drawn figures for ch-mass-u3 (Gas absorption), one per chapter.
Every number comes from that chapter's worked example. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def sb(base, s, size=11):
    return f'{base}<tspan baseline-shift="sub" font-size="{size}">{s}</tspan>'


def frame(xmax, ymax, xt, yt, xlab, ylab, x0=80, x1=440, y0=50, y1=330, xf=None, yf=None):
    fx = lambda v: x0 + (x1 - x0) * v / xmax
    fy = lambda v: y1 - (y1 - y0) * v / ymax
    xf = xf or (lambda v: f'{v:g}')
    yf = yf or (lambda v: f'{v:g}')
    return fx, fy, axes(x0, x1, y0, y1, xt, yt, fx, fy, xlab, ylab, xf, yf)


def line_fn(f, a, b, fx, fy, c=AC, w=2.5, dash=None, n=40):
    return P([(fx(a + (b - a) * i / n), fy(f(a + (b - a) * i / n))) for i in range(n + 1)], c, w, dash)


def gap(x, ya, yb, fx, fy, c=NX, dx=0):
    """a thick vertical bar with end ticks showing a driving force"""
    X = fx(x) + dx
    return (L(X, fy(ya), X, fy(yb), c, 4) + L(X - 6, fy(ya), X + 6, fy(ya), c, 2) + L(X - 6, fy(yb), X + 6, fy(yb), c, 2))


# ---- 3.1 Henry's law at two pressures ----
def f1():
    fx, fy, o = frame(0.005, 0.20, [0, 0.001, 0.002, 0.003, 0.004, 0.005], [0, 0.05, 0.10, 0.15, 0.20],
                      'x, mole fraction SO₂ in the water', 'y, mole fraction SO₂ in the gas')
    o = [o]
    o.append(line_fn(lambda x: 40 * x, 0, 0.005, fx, fy, AC, 3))
    o.append(line_fn(lambda x: 20 * x, 0, 0.005, fx, fy, LV, 3))
    o.append(L(fx(0), fy(0.08), fx(0.004), fy(0.08), MUT, 1.5, '5 4'))
    for xv in (0.002, 0.004):
        o.append(L(fx(xv), fy(0.08), fx(xv), fy(0), MUT, 1.5, '5 4'))
    o.append(C(fx(0.002), fy(0.08), 6, AC)); o.append(C(fx(0.004), fy(0.08), 6, LV))
    o.append(Tb(fx(0.0042), fy(0.188), '1 atm: y* = 40x', 14, 'end', AC, True))
    o.append(Tb(fx(0.0049), fy(0.118), '2 atm: y* = 20x', 14, 'end', LV, True))
    o.append(Tb(fx(0.0021), fy(0.08) - 12, 'y = 0.08', 13, 'end', MUT))
    o.append(boxt(462, 60, 244, 200, ['SO₂ in water, H = 40 atm', 'gas: y = 0.08', '1 atm: p = 0.08 atm', 'x = 0.08 / 40 = 0.002',
                                      '2 atm: p = 0.16 atm', 'x = 0.16 / 40 = 0.004', 'm = H / P: 40 → 20'], ACS, AC, 14, True))
    return 380, ''.join(o)
FIG[1] = (f1, 'Henry\'s law for SO₂ in water (H = 40 atm per mole fraction) at 1 atm and 2 atm. The same gas, y = 0.08, leaves twice as much SO₂ in the water at the higher pressure, because m = H/P halves.',
          'Plot of gas mole fraction against liquid mole fraction with two straight lines through the origin, y star equals 40 x at 1 atmosphere and 20 x at 2 atmospheres, and points at x 0.002 and 0.004 for y 0.08.')


# ---- 3.2 operating and equilibrium lines ----
def f2():
    fx, fy, o = frame(0.025, 0.06, [0, 0.005, 0.01, 0.015, 0.02, 0.025], [0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06],
                      'X, kmol acetone per kmol water', 'Y, kmol acetone per kmol air')
    o = [o]
    o.append(line_fn(lambda x: 2 * x, 0, 0.025, fx, fy, AC, 3))
    o.append(line_fn(lambda x: 0.005025 + 2.1053 * x, 0, 0.022613, fx, fy, LV, 3))
    o.append(gap(0.0, 0.0, 0.005025, fx, fy, dx=10))
    o.append(gap(0.022613, 0.045226, 0.052632, fx, fy, dx=12))
    o.append(C(fx(0), fy(0.005025), 6, LV)); o.append(C(fx(0.022613), fy(0.052632), 6, LV))
    o.append(Tb(fx(0.0012), fy(0.0105), 'top (0, 0.00503)', 13, 'start', INK))
    o.append(Tb(fx(0.0016), fy(0.0028), 'gap 0.00503', 13, 'start', NX, True))
    o.append(Tb(fx(0.0222), fy(0.0565), 'bottom (0.0226, 0.0526)', 13, 'end', INK))
    o.append(Tb(fx(0.0214), fy(0.0470), 'gap 0.00741', 13, 'end', NX, True))
    o.append(Tb(fx(0.0105), fy(0.0335), 'operating line, slope L/G = 2.105', 13, 'end', LV, True))
    o.append(Tb(fx(0.0170), fy(0.0270), 'equilibrium Y* = 2X', 13, 'start', AC, True))
    o.append(boxt(462, 70, 244, 160, ['G = 95 kmol/h air', 'L = 200 kmol/h water', 'absorbed 4.523 kmol/h', sb('X', 'out') + ' = 4.523 / 200', '= 0.0226'], ACS, AC, 14, True))
    return 380, ''.join(o)
FIG[2] = (f2, 'The worked example on Y–X axes: the operating line runs from the top (0, 0.00503) to the bottom (0.0226, 0.0526), above the equilibrium line Y* = 2X. The vertical gap is the driving force, 0.00503 at the top and 0.00741 at the bottom.',
          'Y against X plot with the equilibrium line Y star equals 2 X and the steeper operating line from X 0, Y 0.00503 to X 0.0226, Y 0.0526, with arrows marking the vertical gaps at both ends.')


# ---- 3.3 minimum liquid rate ----
def f3():
    fx, fy, o = frame(0.03, 0.06, [0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03], [0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06],
                      'X, kmol acetone per kmol water', 'Y, kmol acetone per kmol air', x1=410)
    o = [o]
    o.append(L(fx(0), fy(0.0526), fx(0.03), fy(0.0526), MUT, 1.5, '5 4'))
    o.append(line_fn(lambda x: 2 * x, 0, 0.03, fx, fy, AC, 3))
    o.append(line_fn(lambda x: 0.00503 + 1.809 * x, 0, 0.0263, fx, fy, NX, 2.5, '7 5'))
    o.append(line_fn(lambda x: 0.00503 + 2.713 * x, 0, 0.01753, fx, fy, LV, 3))
    o.append(C(fx(0), fy(0.00503), 6, INK)); o.append(C(fx(0.0263), fy(0.0526), 7, NX)); o.append(C(fx(0.01753), fy(0.0526), 6, LV))
    o.append(Tb(fx(0.0008), fy(0.0005) - 2, 'top (0, 0.00503)', 13, 'start', INK))
    o.append(Tb(fx(0.0266), fy(0.0470), 'pinch', 13, 'start', NX, True)); o.append(Tb(fx(0.0266), fy(0.0470) + 17, 'X* = 0.0263', 13, 'start', NX))
    o.append(Tb(fx(0.0185), fy(0.0566), sb('X', 'out') + ' = 0.0175', 13, 'middle', LV, True))
    o.append(Tb(fx(0.0005), fy(0.0526) - 9, sb('Y', 'in') + ' = 0.0526', 13, 'start', MUT))
    o.append(Tb(fx(0.0075), fy(0.0335), 'design 2.713', 14, 'end', LV, True))
    o.append(Tb(fx(0.0172), fy(0.0280), 'minimum 1.809', 14, 'start', NX, True))
    o.append(Tb(fx(0.0225), fy(0.0365), 'Y* = 2X', 14, 'start', AC, True))
    o.append(boxt(474, 90, 232, 150, [sb('(L/G)', 'min') + ' = 0.04757 / 0.0263', '= 1.809', 'design = 1.5 × 1.809 = 2.713', 'L = 2.713 × 95 = 257.7 kmol/h'], ACS, AC, 14, True))
    return 380, ''.join(o)
FIG[3] = (f3, 'Rotating the operating line down about the fixed top point: at slope 1.809 it reaches the entering gas exactly on the equilibrium line, the pinch at X* = 0.0263. The design line, 1.5 times steeper, stops at X = 0.0175 and keeps a gap everywhere.',
          'Y against X plot with the equilibrium line, a dashed minimum operating line from the top point to the pinch at X 0.0263 on the line Y 0.0526, and a steeper design line ending at X 0.0175.')


# ---- 3.4 counter-current and co-current columns ----
def column(x, ytop, ybot, w=90):
    return R(x, ytop, w, ybot - ytop, PANEL, L2, 10, 2)


def f4():
    o = []
    yt, yb = 90, 320
    # counter-current
    xa = 200
    o.append(T(xa + 45, 32, 'Counter-current', 16, bold=True))
    o.append(column(xa, yt, yb))
    o.append(L(xa + 30, yb - 20, xa + 30, yt + 24, AC, 3, arrow='n')); o.append(Tb(xa + 30, yt + 128, 'gas', 13, 'middle', AC, True))
    o.append(L(xa + 62, yt + 20, xa + 62, yb - 24, LV, 3, arrow='l')); o.append(Tb(xa + 62, yt + 158, 'liquid', 13, 'middle', LV, True))
    o.append(L(xa - 86, yb - 20, xa - 4, yb - 20, AC, 2.5, arrow='n')); o.append(T(xa - 92, yb - 30, 'gas in', 13, 'end', AC)); o.append(T(xa - 92, yb - 12, sb('Y', 'in') + ' = 0.0526', 13, 'end'))
    o.append(L(xa + 30, yt, xa + 30, yt - 18, AC, 2.5)); o.append(L(xa + 30, yt - 18, xa - 60, yt - 18, AC, 2.5, arrow='n'))
    o.append(T(xa - 66, yt - 30, 'gas out', 13, 'end', AC)); o.append(T(xa - 66, yt - 12, sb('Y', 'out') + ' = 0.00503', 13, 'end'))
    o.append(L(xa + 186, yt + 20, xa + 94, yt + 20, LV, 2.5, arrow='l')); o.append(T(xa + 192, yt + 14, 'liquid in', 13, 'start', LV)); o.append(T(xa + 192, yt + 32, sb('X', 'in') + ' = 0', 13, 'start'))
    o.append(L(xa + 62, yb, xa + 62, yb + 20, LV, 2.5)); o.append(L(xa + 62, yb + 20, xa + 150, yb + 20, LV, 2.5, arrow='l'))
    o.append(T(xa + 156, yb + 14, 'liquid out', 13, 'start', LV)); o.append(T(xa + 156, yb + 32, sb('X', 'out') + ' = 0.0226', 13, 'start'))
    # co-current: both streams enter at the top and leave at the bottom
    xb = 520
    o.append(T(xb + 45, 32, 'Co-current', 16, bold=True))
    o.append(column(xb, yt, yb))
    o.append(L(xb + 30, yt + 20, xb + 30, yb - 24, AC, 3, arrow='n')); o.append(Tb(xb + 30, yt + 128, 'gas', 13, 'middle', AC, True))
    o.append(L(xb + 62, yt + 20, xb + 62, yb - 24, LV, 3, arrow='l')); o.append(Tb(xb + 62, yt + 158, 'liquid', 13, 'middle', LV, True))
    o.append(L(xb + 30, yt - 30, xb + 30, yt - 3, AC, 2.5, arrow='n')); o.append(T(xb + 22, yt - 34, 'gas in 0.0526', 13, 'end', AC))
    o.append(L(xb + 62, yt - 30, xb + 62, yt - 3, LV, 2.5, arrow='l')); o.append(T(xb + 70, yt - 34, 'liquid in X = 0', 13, 'start', LV))
    o.append(L(xb + 30, yb + 2, xb + 30, yb + 30, AC, 2.5, arrow='n')); o.append(T(xb + 22, yb + 26, 'gas out', 13, 'end', AC)); o.append(T(xb + 22, yb + 43, '0.0256', 13, 'end'))
    o.append(L(xb + 62, yb + 2, xb + 62, yb + 30, LV, 2.5, arrow='l')); o.append(T(xb + 70, yb + 26, 'liquid out', 13, 'start', LV)); o.append(T(xb + 70, yb + 43, '0.0128', 13, 'start'))
    o.append(T(xb + 100, (yt + yb) / 2 - 8, 'outlet', 13, 'start', NX, True)); o.append(T(xb + 100, (yt + yb) / 2 + 9, 'pinned at', 13, 'start', NX, True)); o.append(T(xb + 100, (yt + yb) / 2 + 26, 'Y = 2X', 13, 'start', NX, True))
    o.append(boxt(150, 392, 440, 56, ['same L/G = 2.105 and Y* = 2X:', 'co-current exit gas 0.0256 is 5.1 times richer than 0.00503'], ACS, AC, 14))
    return 464, ''.join(o)
FIG[4] = (f4, 'The worked example in both arrangements at the same L/G = 2.105. Counter-current flow sends lean gas (0.00503) out of the top past fresh liquid; co-current flow can do no better than equilibrium at the outlet, 0.0256.',
          'Two column sketches. Left, counter-current: gas enters at the bottom with Y 0.0526 and leaves at the top with 0.00503, liquid enters at the top with X 0 and leaves at the bottom with 0.0226. Right, co-current: both enter at the top, gas leaves at 0.0256 and liquid at 0.0128.')


# ---- 3.5 stepping off stages ----
def f5():
    fx, fy, o = frame(0.02, 0.06, [0, 0.005, 0.01, 0.015, 0.02], [0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06],
                      'X, kmol solute per kmol solvent', 'Y, kmol solute per kmol inert gas')
    o = [o]
    o.append(L(fx(0), fy(0.0526), fx(0.02), fy(0.0526), MUT, 1.5, '5 4'))
    o.append(line_fn(lambda x: 2 * x, 0, 0.02, fx, fy, AC, 3))
    o.append(line_fn(lambda x: 0.00526 + 2.72 * x, 0, 0.0177, fx, fy, LV, 3))
    pts = [(0, 0.00526)]; Y = 0.00526
    for n in range(4):
        X = Y / 2; pts.append((X, Y)); Y = 0.00526 + 2.72 * X; pts.append((X, Y))
    o.append(P([(fx(a), fy(b)) for a, b in pts], NX, 2.2))
    corners = [(0.00263, 0.00526), (0.006207, 0.012414), (0.011071, 0.022142), (0.017687, 0.035374)]
    for i, (a, b) in enumerate(corners, 1):
        o.append(Tb(fx(a) + 14, fy(b) + 18, str(i), 14, 'start', NX, True))
    o.append(Tb(fx(0.0004), fy(0.0526) - 10, sb('Y', 'N+1') + ' = 0.0526', 13, 'start', MUT))
    o.append(Tb(fx(0.0008), fy(0.043), 'operating Y = 0.00526 + 2.72X', 13, 'start', LV, True))
    o.append(Tb(fx(0.0145), fy(0.0205), 'Y* = 2X', 14, 'start', AC, True))
    o.append(boxt(462, 80, 244, 170, ['A = 2.72 / 2 = 1.36', 'R = 0.90', 'N + 1 = ln 4.60 / ln 1.36', 'N = 3.96 → 4 stages', 'trays = 3.96 / 0.60 → 7'], ACS, AC, 14, True))
    return 380, ''.join(o)
FIG[5] = (f5, 'Stepping off the worked example between the operating line and Y* = 2X, from the top (stage 1) down. The fourth step passes the entering gas, 0.0526, so four theoretical stages do the job, as the Kremser equation (N = 3.96) says.',
          'Y against X plot with the equilibrium line, the operating line from Y 0.00526 and a staircase of four numbered steps between them reaching above Y 0.0526.')


# ---- 3.6 packed tower and its internals ----
def f6():
    o = ['<defs><pattern id="pk-UID" width="18" height="16" patternUnits="userSpaceOnUse">'
         '<circle cx="5" cy="5" r="3.6" style="fill:none;stroke:var(--accent);stroke-width:1.4"/>'
         '<circle cx="14" cy="12" r="3.6" style="fill:none;stroke:var(--accent);stroke-width:1.4"/></pattern></defs>']
    x0, x1 = 190, 330
    o.append(R(x0, 50, x1 - x0, 410, PANEL, INK, 14, 2.2))
    # distributor
    o.append(L(x1 + 70, 92, x0 + 18, 92, LV, 4)); o.append(T(x1 + 76, 88, 'liquid in', 13, 'start', LV))
    for i in range(6):
        xx = x0 + 22 + i * 19
        o.append(L(xx, 96, xx, 108, LV, 2, arrow='l'))
    # beds
    for (ya, yb) in ((118, 238), (278, 398)):
        o.append(f'<rect x="{x0 + 3}" y="{ya}" width="{x1 - x0 - 6}" height="{yb - ya}" style="fill:url(#pk-UID);stroke:var(--accent);stroke-width:1.5"/>')
    # redistributor
    o.append(P([(x0 + 3, 246), (x0 + 50, 262), (x1 - 50, 262), (x1 - 3, 246)], LV, 3))
    # support plates
    for y in (238, 398):
        o.append(L(x0 + 3, y + 4, x1 - 3, y + 4, INK, 3, '4 3'))
    # gas in and out, liquid out
    o.append(L(x0 - 80, 430, x0 - 2, 430, AC, 3, arrow='n')); o.append(T(x0 - 84, 434, 'gas in', 13, 'end', AC))
    o.append(L(x0 + 40, 50, x0 + 40, 26, AC, 3)); o.append(L(x0 + 40, 26, x0 - 60, 26, AC, 3, arrow='n')); o.append(T(x0 - 66, 30, 'gas out', 13, 'end', AC))
    o.append(L(x1 - 40, 460, x1 - 40, 482, LV, 3)); o.append(L(x1 - 40, 482, x1 + 50, 482, LV, 3, arrow='l')); o.append(T(x1 + 56, 486, 'liquid out', 13, 'start', LV))
    # labels to the right
    lab = [(108, 'distributor'), (178, 'bed 1: 2 m of 25 mm rings'), (256, 'redistributor'), (338, 'bed 2: 2 m'), (404, 'support plate')]
    for y, s in lab:
        o.append(L(x1 + 4, y, x1 + 30, y, MUT, 1.2)); o.append(T(x1 + 36, y + 5, s, 13, 'start'))
    # dimensions
    o.append(L(x0, 506, x1, 506, MUT, 1.5)); o.append(L(x0, 500, x0, 512, MUT, 1.5)); o.append(L(x1, 500, x1, 512, MUT, 1.5))
    o.append(T((x0 + x1) / 2, 528, 'D = 1.2 m', 14, bold=True))
    o.append(T(x0 - 20, 260, '4 m of', 13, 'end', MUT)); o.append(T(x0 - 20, 277, 'packing', 13, 'end', MUT))
    o.append(boxt(520, 300, 186, 150, [sb('A', 'c') + ' = 1.131 m²', 'V = 1.131 × 4', '= 4.524 m³', 'surface 904.8 m²', 'voids 3.393 m³'], ACS, AC, 14, True))
    return 540, ''.join(o)
FIG[6] = (f6, 'The worked example\'s tower: 1.2 m across, with two 2 m beds of 25 mm rings. The distributor spreads the liquid, the redistributor collects and re-spreads it between the beds, and support plates hold each bed while letting gas through.',
          'Sketch of a packed tower with liquid entering a distributor at the top, two packed beds separated by a redistributor, support plates under each bed, gas entering at the bottom and leaving at the top, and liquid leaving at the bottom.')


# ---- 3.7 end driving forces and the height ----
def f7():
    fx, fy, o = frame(0.02, 0.06, [0, 0.005, 0.01, 0.015, 0.02], [0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06],
                      'X, kmol acetone per kmol water', 'Y, kmol acetone per kmol air')
    o = [o]
    o.append(line_fn(lambda x: 2 * x, 0, 0.02, fx, fy, AC, 3))
    o.append(line_fn(lambda x: 0.00503 + 2.72 * x, 0, 0.017489, fx, fy, LV, 3))
    o.append(gap(0.0, 0.0, 0.00503, fx, fy, dx=10))
    o.append(gap(0.017489, 0.034978, 0.0526, fx, fy, dx=12))
    o.append(Tb(fx(0.0012), fy(0.0028), sb('ΔY', '2') + ' = 0.00503 (top)', 13, 'start', NX, True))
    o.append(Tb(fx(0.0168), fy(0.0440), sb('ΔY', '1') + ' = 0.01762', 13, 'end', NX, True))
    o.append(Tb(fx(0.0168), fy(0.0440) + 18, '(bottom)', 13, 'end', NX))
    o.append(Tb(fx(0.0064), fy(0.0335), 'operating, slope 2.72', 13, 'end', LV, True))
    o.append(Tb(fx(0.0195), fy(0.0335), 'Y* = 2X', 14, 'end', AC, True))
    o.append(boxt(462, 60, 244, 210, [sb('ΔY', 'lm') + ' = 0.01259 / ln 3.503', '= 0.01004', sb('N', 'OG') + ' = 0.04757 / 0.01004', '= 4.74',
                                      sb('H', 'OG') + ' = 0.015 / 0.05 = 0.30 m', 'Z = 0.30 × 4.74 = 1.42 m'], ACS, AC, 14))
    return 380, ''.join(o)
FIG[7] = (f7, 'The worked example\'s two lines and the driving forces at the ends of the bed: 0.01762 at the bottom and 0.00503 at the top. Their log mean, 0.01004, divides the gas change 0.04757 to give 4.74 transfer units, and 4.74 × 0.30 m gives the 1.42 m bed.',
          'Y against X plot with the equilibrium line and the operating line, double arrows marking the end driving forces 0.00503 at the top and 0.01762 at the bottom, and a box with the log mean, N O G, H O G and bed height.')


# ---- 3.8 heat bends the equilibrium line ----
def f8():
    fx, fy, o = frame(0.02, 0.06, [0, 0.005, 0.01, 0.015, 0.02], [0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06],
                      'X, kmol acetone per kmol water', 'Y, kmol acetone per kmol air', x1=410)
    o = [o]
    Xo = 0.01752
    o.append(line_fn(lambda x: 2 * x, 0, 0.02, fx, fy, AC, 2.5, '7 5'))
    o.append(line_fn(lambda x: 2 * x * (1 + 0.2794 * x / Xo), 0, Xo, fx, fy, NX, 3))
    o.append(line_fn(lambda x: 0.00503 + 2.716 * x, 0, Xo, fx, fy, LV, 3))
    xb = fx(Xo)
    o.append(L(xb + 8, fy(0.0350), xb + 8, fy(0.0526) + 4, AC, 2.2, arrow='n'))
    o.append(L(xb - 8, fy(0.0448), xb - 8, fy(0.0526) + 4, NX, 2.2, arrow='x'))
    o.append(Tb(xb + 16, fy(0.0440), 'cold gap', 13, 'start', AC, True)); o.append(Tb(xb + 16, fy(0.0440) + 17, '0.0176', 13, 'start', AC))
    o.append(Tb(xb - 16, fy(0.0566), 'hot gap 0.0078', 13, 'end', NX, True))
    o.append(Tb(fx(0.0062), fy(0.0335), 'operating, slope 2.716', 13, 'end', LV, True))
    o.append(Tb(fx(0.0140), fy(0.0200), 'cold: Y* = 2X', 13, 'start', AC))
    o.append(Tb(fx(0.0115), fy(0.0335) + 6, 'warming liquid', 13, 'start', NX, True))
    o.append(boxt(486, 70, 220, 170, ['liquid warms 7.0 K', 'top: m = 2.00', 'bottom: m = 2.56', sb('N', 'OG') + ': 4.75 → 6.06', 'bed: 1.42 → 1.82 m'], ACS, AC, 14, True))
    return 380, ''.join(o)
FIG[8] = (f8, 'As the water picks up acetone it warms by up to 7.0 K, so the equilibrium line curves up from Y* = 2X at the cold top to m = 2.56 at the bottom. The operating line does not move, but the bottom driving force falls from 0.0176 to 0.0078.',
          'Y against X plot with a dashed straight cold equilibrium line, a curved warm equilibrium line rising above it, and the operating line; arrows at the bottom end show the cold and hot driving forces.')


# ---- 3.9 concentration in the liquid film ----
def f9():
    fx, fy, o = frame(1.0, 1.0, [0, 0.2, 0.4, 0.6, 0.8, 1.0], [0, 0.2, 0.4, 0.6, 0.8, 1.0],
                      'distance into the liquid film, x/δ', 'concentration / its reference value', x1=460)
    o = [o]
    o.append(line_fn(lambda x: 1 - x, 0, 1, fx, fy, AC, 3))
    o.append(line_fn(lambda x: math.sinh(3 * (1 - x)) / math.sinh(3), 0, 1, fx, fy, LV, 3, n=60))
    o.append(line_fn(lambda x: max(0.0, 1 - 6 * x), 0, 1 / 6, fx, fy, NX, 3))
    o.append(line_fn(lambda x: (x - 1 / 6) / (5 / 6), 1 / 6, 1, fx, fy, NX, 2.5, '7 5'))
    o.append(L(fx(1 / 6), fy(0), fx(1 / 6), fy(1.0), MUT, 1.2, '3 4'))
    o.append(Tb(fx(0.18), fy(0.97), 'reaction plane x/δ = 1/6', 13, 'start', MUT))
    o.append(R(478, 50, 230, 270, ACS, AC, 8, 2))
    leg = [(AC, None, 'no reaction: E = 1'), (LV, None, 'fast, Ha = 3: E = 3.0'), (NX, None, 'A, instantaneous: E = 6'), (NX, '7 5', 'reactant B')]
    for i, (col, da, s) in enumerate(leg):
        y = 78 + i * 26
        o.append(L(490, y - 5, 522, y - 5, col, 3, da)); o.append(T(530, y, s, 13, 'start'))
    for i, s in enumerate(['Ha = √(k' + sb('D', 'A') + ') / ' + sb('k', 'L'), 'slow, Ha < 0.3: E ≈ 1', 'fast: E ≈ Ha (Ha/tanh Ha)', sb('E', 'i') + ' = 1 + 5 = 6, plane at 1/6']):
        o.append(T(593, 200 + i * 26, s, 13))
    return 380, ''.join(o)
FIG[9] = (f9, 'Solute A in the liquid film, from the interface (left) to the bulk liquid (right). Without reaction it falls in a straight line; with a fast reaction (Ha = 3) it is used up inside the film; with an instantaneous reaction it meets reactant B at a plane, here at x/δ = 1/6 for E<sub>i</sub> = 6.',
          'Plot of concentration against distance through the liquid film with a straight falling line for no reaction, a curve that drops steeply for Ha 3, a steep line for A reaching zero at one sixth of the film, and a dashed rising line for reactant B beyond that plane.')

spec = make_spec(FIG)
