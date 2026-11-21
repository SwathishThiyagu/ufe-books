"""Claude's hand-drawn figures for ch-mass-u4 (Distillation), one per chapter.
Every number comes from that chapter's worked example and is computed here. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def sb(base, s, size=11):
    return f'{base}<tspan baseline-shift="sub" font-size="{size}">{s}</tspan>'


def frame(xa, xb, ya, yb, xt, yt, xlab, ylab, x0=80, x1=440, y0=50, y1=330, xf=None, yf=None):
    fx = lambda v: x0 + (x1 - x0) * (v - xa) / (xb - xa)
    fy = lambda v: y1 - (y1 - y0) * (v - ya) / (yb - ya)
    xf = xf or (lambda v: f'{v:g}')
    yf = yf or (lambda v: neg(f'{v:g}'))
    return fx, fy, axes(x0, x1, y0, y1, xt, yt, fx, fy, xlab, ylab, xf, yf)


def curve(f, a, b, fx, fy, c=AC, w=2.5, dash=None, n=60):
    return P([(fx(a + (b - a) * i / n), fy(f(a + (b - a) * i / n))) for i in range(n + 1)], c, w, dash)


eq = lambda a, x: a * x / (1 + (a - 1) * x)
xeq = lambda a, y: y / (a - (a - 1) * y)


def staircase(a, xD, xB, xF, R):
    s, b = R / (R + 1), xD / (R + 1)
    yp = s * xF + b; ss = (yp - xB) / (xF - xB)
    y = xD; pts = [(xD, xD)]; n = 0; feed = None
    while True:
        x = xeq(a, y); n += 1; pts.append((x, y))
        if x <= xB: break
        if x > xF: y = s * x + b
        else:
            feed = feed or n; y = xB + ss * (x - xB)
        pts.append((x, y))
        if n > 300: break
    return n, feed, pts


def nfrac(a, xD, xB, xF, R):
    n, feed, pts = staircase(a, xD, xB, xF, R)
    xl, xp = pts[-1][0], pts[-3][0]
    return n - 1 + (xp - xB) / (xp - xl)


# ---- 4.1 P-x-y at fixed T and the y-x curve ----
def f1():
    o = []
    PA, PB, P = 120.0, 40.0, 101.3
    x = (P - PB) / (PA - PB); y = x * PA / P
    fx, fy, ax = frame(0, 1, 0, 140, [0, 0.2, 0.4, 0.6, 0.8, 1], [0, 20, 40, 60, 80, 100, 120, 140], 'x or y, mole fraction of A', 'P, kPa', 70, 330, 62, 330)
    o.append(ax)
    o.append(curve(lambda v: PB + (PA - PB) * v, 0, 1, fx, fy, AC, 3))
    o.append(curve(lambda v: 1 / (v / PA + (1 - v) / PB), 0, 1, fx, fy, LV, 3))
    o.append(L(fx(0), fy(P), fx(1), fy(P), MUT, 1.5, '5 4'))
    o.append(L(fx(x), fy(P), fx(x), fy(0), MUT, 1.2, '4 4')); o.append(L(fx(y), fy(P), fx(y), fy(0), MUT, 1.2, '4 4'))
    o.append(C(fx(x), fy(P), 6, AC)); o.append(C(fx(y), fy(P), 6, LV))
    o.append(Tb(fx(0.03), fy(P) - 9, 'P = 101.3 kPa', 13, 'start', MUT))
    o.append(Tb(fx(0.36), fy(96), 'bubble line', 13, 'end', AC, True))
    o.append(Tb(fx(0.62), fy(56), 'dew curve', 13, 'start', LV, True))
    o.append(T(fx(0.20), fy(126), 'liquid', 13, 'middle', INK, italic=True))
    o.append(T(fx(0.28), fy(14), 'vapour', 13, 'middle', INK, italic=True))
    o.append(Tb(fx(x) - 4, fy(10), 'x = 0.766', 12, 'end', AC, True))
    o.append(Tb(fx(y) - 3, fy(26), 'y = 0.908', 12, 'end', LV, True))
    o.append(T(200, 22, 'P-x-y at fixed T: ' + sb('P°', 'A') + ' = 120, ' + sb('P°', 'B') + ' = 40 kPa', 14, bold=True))
    fx, fy, ax = frame(0, 1, 0, 1, [0, 0.2, 0.4, 0.6, 0.8, 1], [0, 0.2, 0.4, 0.6, 0.8, 1], 'x, liquid mole fraction of A', 'y', 440, 690, 62, 330)
    o.append(ax)
    o.append(L(fx(0), fy(0), fx(1), fy(1), L2, 1.5))
    o.append(curve(lambda v: eq(3, v), 0, 1, fx, fy, AC, 3))
    o.append(L(fx(x), fy(0), fx(x), fy(y), MUT, 1.2, '4 4')); o.append(L(fx(0), fy(y), fx(x), fy(y), MUT, 1.2, '4 4'))
    o.append(C(fx(x), fy(y), 6, NX))
    o.append(Tb(fx(0.70), fy(y) - 12, '(0.766, 0.908)', 12, 'end', NX, True))
    o.append(Tb(fx(0.20), fy(0.60), 'α = 3', 14, 'end', AC, True))
    o.append(Tb(fx(0.70), fy(0.55), 'y = x', 13, 'start', MUT))
    o.append(T(565, 22, 'y-x curve, y = 3x/(1 + 2x)', 14, bold=True))
    return 380, ''.join(o)
FIG[1] = (f1, 'The worked example on two diagrams. Left: at the fixed temperature the bubble line runs straight from P°<sub>B</sub> = 40 to P°<sub>A</sub> = 120 kPa and the dew curve sags below it; at P = 101.3 kPa they give x = 0.766 and y = 0.908. Right: the same pair lies on the α = 3 equilibrium curve, above the diagonal.',
          'Two plots. Left, pressure against composition: a straight bubble line from 40 to 120 kilopascals, a curved dew line below it, and a dashed line at 101.3 kilopascals cutting them at x 0.766 and y 0.908. Right, y against x: the curve y equals 3x over 1 plus 2x above the diagonal, with the point 0.766, 0.908 marked.')


# ---- 4.2 flash drum ----
def f2():
    o = []
    # feed line, heater, valve
    o.append(T(30, 236, 'feed', 14, 'start', INK, True)); o.append(T(30, 256, 'F = 100 kmol/h', 13, 'start')); o.append(T(30, 274, sb('z', 'A') + ' = 0.50', 13, 'start'))
    o.append(L(30, 220, 120, 220, INK, 2.5))
    o.append(R(120, 196, 90, 48, PANEL, NX, 6))
    o.append(P([(130, 220), (140, 206), (150, 234), (160, 206), (170, 234), (180, 206), (190, 234), (200, 220)], NX, 2))
    o.append(T(165, 186, 'heater', 13, 'middle', NX, True))
    o.append(L(210, 220, 262, 220, INK, 2.5))
    o.append(P([(262, 208), (282, 232), (282, 208), (262, 232), (262, 208)], INK, 2))
    o.append(T(272, 198, 'valve', 13, 'middle', INK, True)); o.append(T(272, 256, 'P drops', 12, 'middle', MUT))
    o.append(L(282, 220, 352, 220, INK, 2.5, arrow='x'))
    # drum
    o.append(R(356, 70, 120, 290, PANEL, INK, 50, 2.5))
    o.append(f'<rect x="368" y="98" width="96" height="18" style="fill:none;stroke:var(--muted);stroke-width:1.5;stroke-dasharray:3 3"/>')
    o.append(T(416, 132, 'mist pad', 12, 'middle', MUT))
    o.append('<path d="M358,262 H474 V310 A48,48 0 0 1 426,358 H406 A48,48 0 0 1 358,310 Z" style="fill:var(--live-soft);stroke:none"/>')
    o.append(L(358, 262, 474, 262, LV, 2))
    o.append(T(416, 300, 'liquid', 13, 'middle', LV, True))
    for xx in (380, 452):
        o.append(L(xx, 250, xx, 160, AC, 1.8, '3 4', arrow='n'))
    o.append(T(416, 214, 'vapour', 13, 'middle', AC, True))
    # products
    o.append(L(416, 70, 416, 40, AC, 2.5)); o.append(L(416, 40, 540, 40, AC, 2.5, arrow='n'))
    o.append(T(550, 36, 'vapour V = 50 kmol/h', 14, 'start', AC, True)); o.append(T(550, 56, sb('y', 'A') + ' = 0.667', 13, 'start'))
    o.append(L(416, 360, 416, 384, LV, 2.5)); o.append(L(416, 384, 540, 384, LV, 2.5, arrow='l'))
    o.append(T(550, 380, 'liquid L = 50 kmol/h', 14, 'start', LV, True)); o.append(T(550, 400, sb('x', 'A') + ' = 0.333', 13, 'start'))
    o.append(boxt(500, 130, 210, 150, ['one equilibrium stage', sb('K', 'A') + ' = 2.0, ' + sb('K', 'B') + ' = 0.5', 'Σ zK = 1.25 > 1', 'Σ z/K = 1.25 > 1', 'V/F = 0.50'], ACS, AC, 13, True))
    return 412, ''.join(o)
FIG[2] = (f2, 'The flash drum of the worked example. The heated feed (F = 100 kmol/h, z<sub>A</sub> = 0.50) drops in pressure across the valve and splits into vapour (y<sub>A</sub> = 0.667) and liquid (x<sub>A</sub> = 0.333), in equilibrium with K<sub>A</sub> = 2.0 and K<sub>B</sub> = 0.5. Here V/F happens to be 0.50; neither product has the feed composition.',
          'Flowsheet: feed line through a heater and a valve into a vertical drum with a mist pad near the top; vapour leaves the top at 50 kilomoles per hour with y 0.667 and liquid leaves the bottom at 50 kilomoles per hour with x 0.333.')


# ---- 4.3 batch still and Rayleigh curve ----
def f3():
    o = []
    # still sketch
    o.append(f'<path d="M40,250 Q40,330 110,330 Q180,330 180,250 L180,200 L40,200 Z" style="fill:var(--panel);stroke:var(--ink);stroke-width:2.2"/>')
    o.append(f'<path d="M42,262 Q46,328 110,328 Q176,328 178,262 Z" style="fill:var(--live-soft);stroke:none"/>')
    o.append(T(110, 300, 'pot liquid L, x', 12, 'middle', LV, True))
    o.append(P([(70, 346), (82, 338), (94, 346), (106, 338), (118, 346), (130, 338), (142, 346), (154, 338)], NX, 2)); o.append(T(110, 368, 'heat', 12, 'middle', NX, True))
    o.append(L(110, 200, 110, 110, AC, 2.5)); o.append(L(110, 110, 196, 110, AC, 2.5, arrow='n'))
    o.append(T(104, 150, 'vapour y', 12, 'end', AC, True))
    o.append(R(200, 92, 54, 36, PANEL, NX, 6)); o.append(T(227, 84, 'condenser', 12, 'middle', NX, True))
    o.append(L(227, 128, 227, 200, LV, 2.5, arrow='l'))
    o.append(R(203, 204, 48, 70, PANEL, INK, 4)); o.append(T(227, 292, 'distillate', 12, 'middle', LV, True)); o.append(T(227, 308, 'D, ' + sb('x', 'D,avg'), 12, 'middle'))
    o.append(T(110, 40, 'batch still, no reflux', 14, 'middle', INK, True))
    # Rayleigh curve
    a, L1 = 2.0, 100.0
    Lx = lambda x: L1 / math.exp((math.log(0.5 / x) - a * math.log(0.5 / (1 - x))) / (a - 1))
    fx, fy, ax = frame(0.1, 0.5, 0, 100, [0.1, 0.2, 0.3, 0.4, 0.5], [0, 20, 40, 60, 80, 100], 'x, pot liquid mole fraction (falls as the run goes on)', 'L, mol left in the pot', 360, 690, 50, 330)
    o.append(ax)
    o.append(curve(Lx, 0.2, 0.5, fx, fy, AC, 3))
    o.append(curve(Lx, 0.13, 0.2, fx, fy, AC, 2, '5 4', 20))
    L2_ = Lx(0.2)
    o.append(C(fx(0.5), fy(100), 6, AC)); o.append(C(fx(0.2), fy(L2_), 6, NX))
    o.append(Tb(fx(0.49), fy(100) + 22, 'charge: 100 mol, x₁ = 0.50', 12, 'end', INK))
    o.append(Tb(fx(0.215), fy(L2_) - 14, f'residue: {L2_:.1f} mol, x₂ = 0.20', 12, 'start', NX, True))
    o.append(L(fx(0.2) + 18, fy(L2_), fx(0.2) + 18, fy(100), NX, 1.5, '4 3'))
    o.append(Tb(fx(0.31), fy(68), 'distilled off', 12, 'middle', NX)); o.append(Tb(fx(0.31), fy(60), 'D = 84.4 mol', 12, 'middle', NX, True))
    o.append(Tb(fx(0.31), fy(52), sb('x', 'D,avg') + ' = 0.556', 12, 'middle', NX, True))
    o.append(T(525, 24, 'Rayleigh, α = 2.0: L against x', 14, bold=True))
    return 400, ''.join(o)
FIG[3] = (f3, 'Left: a batch still with no reflux; the vapour is condensed and collected as it forms. Right: the Rayleigh equation for the worked example (α = 2.0). As the pot liquid falls from x = 0.50 to 0.20, the charge shrinks from 100 mol to 15.6 mol; the 84.4 mol of distillate average x<sub>D</sub> = 0.556.',
          'Left, a sketch of a heated still pot, vapour line to a condenser and a distillate receiver. Right, a curve of moles left in the pot against pot mole fraction, falling from 100 at x 0.50 to 15.6 at x 0.20.')


# ---- 4.4 McCabe-Thiele staircase ----
def f4():
    a, xD, xB, xF, R = 2.5, 0.95, 0.05, 0.40, 2.0
    n, feed, pts = staircase(a, xD, xB, xF, R)
    fx, fy, ax = frame(0, 1, 0, 1, [0, 0.2, 0.4, 0.6, 0.8, 1], [0, 0.2, 0.4, 0.6, 0.8, 1], 'x, liquid mole fraction', 'y, vapour mole fraction', 70, 450, 40, 420)
    o = [ax]
    o.append(L(fx(0), fy(0), fx(1), fy(1), L2, 1.5))
    o.append(curve(lambda v: eq(a, v), 0, 1, fx, fy, AC, 3))
    yp = 2 / 3 * xF + xD / 3
    o.append(L(fx(xD), fy(xD), fx(xF), fy(yp), LV, 2.5))
    o.append(L(fx(xB), fy(xB), fx(xF), fy(yp), LV, 2.5))
    o.append(L(fx(xF), fy(xF), fx(xF), fy(0.70), MUT, 1.8, '5 4'))
    o.append(P([(fx(u), fy(v)) for u, v in pts], NX, 1.8))
    for u in (xD, xF, xB):
        o.append(C(fx(u), fy(u), 4.5, INK))
    o.append(C(fx(xF), fy(yp), 5.5, LV))
    # number stages 1, 7 and 13 at the corners
    corners = [p for i, p in enumerate(pts) if i % 2 == 1]
    for k in (1, 4, 7, 10, 13):
        u, v = corners[k - 1]
        o.append(Tb(fx(u) - 8, fy(v) - 7, str(k), 12, 'end', NX, True))
    o.append(Tb(fx(0.55), fy(0.93), 'equilibrium, α = 2.5', 13, 'end', AC, True))
    o.append(Tb(fx(0.60), fy(0.555), 'rectifying y = 0.667x + 0.317', 12, 'start', LV, True))
    o.append(Tb(fx(0.22), fy(0.15), 'stripping y = 1.524x − 0.026', 12, 'start', LV, True))
    o.append(Tb(fx(xF) + 6, fy(0.74), 'q-line, x = 0.40', 12, 'start', MUT))
    o.append(Tb(fx(xD) - 4, fy(xD) + 22, sb('x', 'D') + ' 0.95', 12, 'end', INK))
    o.append(Tb(fx(xB) + 10, fy(xB) + 4, sb('x', 'B') + ' 0.05', 12, 'start', INK))
    o.append(boxt(478, 70, 232, 196, ['saturated liquid feed', 'R = 2.0', f'{n} steps to pass ' + sb('x', 'B'), f'feed on stage {feed}', '12 ideal trays', '+ partial reboiler'], ACS, AC, 14, True))
    return 470, ''.join(o)
FIG[4] = (f4, 'The worked example stepped off by computer from the same equations: α = 2.5, x<sub>D</sub> = 0.95, x<sub>B</sub> = 0.05, saturated-liquid feed at x<sub>F</sub> = 0.40 and R = 2. The operating lines meet on the vertical q-line; stage 7 straddles it and is the feed stage, and stage 13 (the reboiler) passes x<sub>B</sub>.',
          'y against x diagram with the equilibrium curve for alpha 2.5, the diagonal, the rectifying and stripping operating lines meeting on a vertical q-line at x 0.40, and a staircase of 13 steps from x 0.95 down past 0.05, with steps 1, 4, 7, 10 and 13 numbered.')


# ---- 4.5 stages and cost against reflux ----
def f5():
    a, xD, xB, xF = 2.5, 0.95, 0.05, 0.40
    Rmin = (xD - 0.625) / (0.625 - xF); Nmin = math.log(361) / math.log(2.5)
    ks = [1.005, 1.01, 1.02, 1.03] + [1.04 + 0.02 * i for i in range(99)]
    N = {k: nfrac(a, xD, xB, xF, k * Rmin) for k in ks}
    o = []
    fx, fy, ax = frame(1, 3, 0, 30, [1, 1.5, 2, 2.5, 3], [0, 5, 10, 15, 20, 25, 30], 'R / R_min', 'theoretical stages N', 60, 330, 50, 330)
    o.append(ax.replace('R / R_min', 'R / R<tspan baseline-shift="sub" font-size="11">min</tspan>'))
    o.append(P([(fx(k), fy(N[k])) for k in ks if N[k] <= 30], AC, 3))
    o.append(L(fx(1), fy(Nmin), fx(3), fy(Nmin), MUT, 1.5, '5 4')); o.append(Tb(fx(2.95), fy(Nmin) + 18, sb('N', 'min') + ' = 6.43 (total reflux)', 12, 'end', MUT))
    o.append(L(fx(1), fy(0), fx(1), fy(30), NX, 1.5, '3 4'))
    o.append(Tb(fx(1.04), fy(28.5), sb('R', 'min') + ' = 1.444: N → ∞', 12, 'start', NX, True))
    k13 = 1.3
    o.append(C(fx(k13), fy(nfrac(a, xD, xB, xF, k13 * Rmin)), 6, LV))
    o.append(Tb(fx(1.36), fy(15.8), '1.3 ' + sb('R', 'min') + ': 13.3 → 14 stages', 12, 'start', LV, True))
    o.append(T(195, 24, 'Stages from the staircase', 14, bold=True))
    cost = {k: N[k] + 6 * (k * Rmin + 1) for k in ks}
    kbest = min(cost, key=cost.get)
    fx, fy, ax = frame(1, 3, 0, 60, [1, 1.5, 2, 2.5, 3], [0, 10, 20, 30, 40, 50, 60], 'R / R_min', 'annual cost, stage units', 420, 690, 50, 330)
    o.append(ax.replace('R / R_min', 'R / R<tspan baseline-shift="sub" font-size="11">min</tspan>'))
    o.append(P([(fx(k), fy(cost[k])) for k in ks if cost[k] <= 60], AC, 3))
    o.append(P([(fx(k), fy(N[k])) for k in ks if N[k] <= 60], NX, 2, '6 4'))
    o.append(P([(fx(k), fy(6 * (k * Rmin + 1))) for k in ks if 6 * (k * Rmin + 1) <= 60], LV, 2, '6 4'))
    o.append(C(fx(kbest), fy(cost[kbest]), 6, AC))
    o.append(Tb(fx(kbest) + 8, fy(cost[kbest]) + 22, f'lowest near {kbest:.2f} ' + sb('R', 'min'), 12, 'start', AC, True))
    o.append(Tb(fx(2.95), fy(17), 'energy 6(R + 1)', 12, 'end', LV, True))
    o.append(Tb(fx(2.95), fy(4), 'stages N', 12, 'end', NX, True))
    o.append(Tb(fx(2.3), fy(47), 'total = N + 6(R + 1)', 12, 'middle', AC, True))
    o.append(T(555, 24, 'A simple cost model', 14, bold=True))
    return 380, ''.join(o)
FIG[5] = (f5, 'Left: the stage count for the worked example, stepped off at each reflux ratio. It falls from infinity at R<sub>min</sub> = 1.444 toward N<sub>min</sub> = 6.43 and is 14 whole stages at 1.3 R<sub>min</sub>. Right: a simple annual cost, one unit per stage plus six units per unit of (R + 1); its flat minimum lies between 1.2 and 1.5 R<sub>min</sub>.',
          'Two plots against R over R min from 1 to 3. Left, theoretical stages fall steeply from very large values near 1 to about 8.5 at 3, above a dashed line at 6.43, with a point at 1.3 and 13.3 stages. Right, a U-shaped total cost curve made of a falling stage cost and a rising energy cost, lowest near 1.3.')


# ---- 4.6 enthalpy-concentration diagram ----
def f6():
    a, xD, R = 2.5, 0.95, 2.0
    H = lambda y: 50 - 10 * y; h = lambda x: 20 - 4 * x
    Hd = H(xD) + R * (H(xD) - h(xD))
    hF = h(0.40); HB = hF - (Hd - hF) / (xD - 0.40) * 0.35
    fx, fy, ax = frame(0, 1, -40, 100, [0, 0.2, 0.4, 0.6, 0.8, 1], [-40, -20, 0, 20, 40, 60, 80, 100], 'x or y, mole fraction of the light component', 'enthalpy, kJ/mol', 70, 470, 40, 400)
    o = [ax]
    o.append(curve(H, 0, 1, fx, fy, AC, 3, n=4)); o.append(curve(h, 0, 1, fx, fy, LV, 3, n=4))
    o.append(Tb(fx(0.10), fy(H(0.1)) - 10, 'saturated vapour H = 50 − 10y', 12, 'start', AC, True))
    o.append(Tb(fx(0.43), fy(h(0.43)) + 22, 'saturated liquid h = 20 − 4x', 12, 'start', LV, True))
    # D-F-B line
    o.append(L(fx(xD), fy(Hd), fx(0.05), fy(HB), MUT, 1.6, '6 4'))
    o.append(L(fx(xD), fy(Hd), fx(xD), fy(h(xD)), MUT, 1.4, '3 3'))
    o.append(C(fx(xD), fy(Hd), 6.5, NX)); o.append(C(fx(0.05), fy(HB), 6.5, NX)); o.append(C(fx(0.40), fy(hF), 5.5, INK))
    o.append(Tb(fx(xD) - 10, fy(Hd) - 4, f'Δ<tspan baseline-shift="sub" font-size="11">D</tspan> (0.95, {Hd:.1f})', 13, 'end', NX, True))
    o.append(Tb(fx(0.05) + 12, fy(HB) + 5, f'Δ<tspan baseline-shift="sub" font-size="11">B</tspan> (0.05, {neg(f"{HB:.1f}")})', 13, 'start', NX, True))
    o.append(Tb(fx(0.40) - 6, fy(hF) - 12, 'F (0.40, 18.4)', 12, 'end', INK))
    y = xD
    for n in range(3):
        x = xeq(a, y); hx = h(x)
        m = (Hd - hx) / (xD - x); y2 = (50 - hx + m * x) / (m + 10)
        o.append(L(fx(y), fy(H(y)), fx(x), fy(hx), INK, 1.8))
        o.append(L(fx(xD), fy(Hd), fx(x), fy(hx), NX, 1.4))
        o.append(C(fx(x), fy(hx), 3.5, LV)); o.append(C(fx(y2), fy(H(y2)), 3.5, AC))
        y = y2
    o.append(Tb(fx(0.74), fy(-6), 'tie lines (black) and', 12, 'middle', INK)); o.append(Tb(fx(0.74), fy(-17), 'operating lines from Δ' + '<tspan baseline-shift="sub" font-size="11">D</tspan>', 12, 'middle', NX))
    o.append(boxt(492, 60, 218, 214, ['x_D = 0.95, R = 2', 'H₁ = 40.5, h_D = 16.2', 'H_ΔD = 40.5 + 2(24.3)', '= 89.1 kJ/mol', 'L/V: 0.663, 0.658, 0.653', 'McCabe-Thiele: 0.667'], ACS, AC, 13, True)
             .replace('x_D', sb('x', 'D')).replace('h_D', sb('h', 'D')).replace('H_ΔD', sb('H', 'ΔD')))
    return 456, ''.join(o)
FIG[6] = (f6, 'The worked example on the enthalpy-composition diagram: sloping lines H = 50 − 10y and h = 20 − 4x, the difference point Δ<sub>D</sub> at (0.95, 89.1 kJ/mol), and three trays stepped from the top by alternating tie lines and operating lines through Δ<sub>D</sub>. Δ<sub>D</sub>, the feed F and Δ<sub>B</sub> = (0.05, −26.6) lie on one line.',
          'Enthalpy against composition. A falling vapour line near 40 to 50 kilojoules per mole and a falling liquid line near 16 to 20, a difference point high at x 0.95 and 89.1, another low at x 0.05 and minus 26.6, a dashed line joining them through the feed point at 0.40, and three tie lines with operating lines near the right-hand end.')


# ---- 4.7 tray column and one sieve tray ----
def f7():
    o = []
    x0, x1 = 60, 220
    o.append(R(x0, 40, x1 - x0, 380, PANEL, INK, 12, 2.2))
    ys = [100, 170, 240, 310, 380]
    for i, yy in enumerate(ys):
        if i % 2 == 0:   # downcomer on the right
            pa, pb, wx = x0, x1 - 30, x1 - 30
        else:            # downcomer on the left
            pa, pb, wx = x0 + 30, x1, x0 + 30
        o.append(f'<rect x="{pa:.0f}" y="{yy - 10}" width="{pb - pa:.0f}" height="10" style="fill:var(--live-soft);stroke:none"/>')
        o.append(L(pa, yy, pb, yy, INK, 2.5))
        o.append(L(wx, yy - 12, wx, yy + 44, INK, 2))
        if i < len(ys) - 1:
            dx = (x1 - 15) if i % 2 == 0 else (x0 + 15)
            o.append(L(dx, yy + 2, dx, yy + 50, LV, 1.8, arrow='l'))
    o.append(T(140, 30, 'tray column', 14, 'middle', INK, True))
    o.append(L(120, 226, 120, 184, AC, 2, arrow='n')); o.append(T(128, 210, 'vapour', 12, 'start', AC, True))
    o.append(T(140, 445, 'liquid falls in the downcomers', 12, 'middle', LV, True))
    # zoomed tray n
    zx0, zx1, zy = 300, 690, 250
    o.append(L(220, 170, zx0, 140, MUT, 1.2, '4 4')); o.append(L(220, 240, zx0, 330, MUT, 1.2, '4 4'))
    o.append(R(zx0, 110, zx1 - zx0, 230, FIGBG, L2, 10, 1.5))
    o.append(L(zx0 + 50, zy, zx1 - 60, zy, INK, 3))
    for i in range(11):
        xx = zx0 + 70 + i * 26
        o.append(L(xx, zy - 2, xx, zy + 2, FIGBG, 4))
        o.append(L(xx, zy + 34, xx, zy + 6, AC, 1.8, arrow='n'))
    o.append(f'<rect x="{zx0 + 50}" y="{zy - 46}" width="{zx1 - zx0 - 110}" height="44" style="fill:var(--live-soft);stroke:none"/>')
    for i in range(9):
        o.append(C(zx0 + 80 + i * 30, zy - 22 + (i % 3) * 7, 5, FIGBG).replace('stroke:var(--fig)', 'stroke:var(--accent)'))
    o.append(L(zx1 - 60, zy, zx1 - 60, zy - 58, INK, 3)); o.append(T(zx1 - 56, zy - 64, 'weir', 12, 'start', INK, True))
    o.append(L(zx0 + 50, zy - 100, zx0 + 50, zy, INK, 2.5)); o.append(T(zx0 + 44, zy - 82, 'liquid in', 12, 'end', LV, True))
    o.append(L(zx0 + 16, zy - 60, zx0 + 44, zy - 30, LV, 2, arrow='l'))
    o.append(L(zx0 + 120, zy - 30, zx1 - 120, zy - 30, LV, 2.2, arrow='l')); o.append(Tb((zx0 + zx1) / 2, zy - 54, 'froth: liquid crosses the tray', 12, 'middle', LV, True))
    o.append(L(zx1 - 40, zy - 52, zx1 - 40, zy + 70, LV, 2, arrow='l')); o.append(T(zx1 - 44, zy + 82, 'downcomer, ' + sb('x', 'n'), 12, 'end', LV, True))
    o.append(L(zx0 + 200, zy - 70, zx0 + 200, zy - 102, AC, 2.2, arrow='n')); o.append(T(zx0 + 208, zy - 92, sb('y', 'n') + ' = 0.44 leaves', 12, 'start', AC, True))
    o.append(T(zx0 + 70, zy + 56, 'sieve holes; ' + sb('y', 'n+1') + ' = 0.30 enters from below', 12, 'start', AC, True))
    o.append(boxt(zx0, 360, zx1 - zx0, 80, [sb('E', 'M') + ' = (0.44 − 0.30)/(0.50 − 0.30) = 0.70, with ' + sb('y', 'n') + '* = 0.50', sb('N', 'a') + ' = 10 / 0.60 = 16.7 → 17 trays'], ACS, AC, 13))
    return 460, ''.join(o)
FIG[7] = (f7, 'Left: a tray column; liquid crosses each tray and drops through a downcomer to the tray below while vapour rises through it. Right: one sieve tray with the worked example\'s numbers. Vapour enters at y<sub>n+1</sub> = 0.30 and leaves at 0.44, against the equilibrium 0.50: E<sub>M</sub> = 0.70.',
          'A column sketch with five trays and alternating downcomers, and an enlarged sieve tray showing vapour rising through holes into a froth, liquid crossing to an outlet weir and downcomer, labelled with y n plus 1 0.30 in and y n 0.44 out.')


# ---- 4.8 Gilliland correlation ----
def f8():
    gill = lambda X: 1 - math.exp((1 + 54.4 * X) / (11 + 117.2 * X) * (X - 1) / math.sqrt(X))
    fx, fy, ax = frame(0, 1, 0, 1, [0, 0.2, 0.4, 0.6, 0.8, 1], [0, 0.2, 0.4, 0.6, 0.8, 1], 'X = (R − Rmin)/(R + 1)', 'Y = (N − Nmin)/(N + 1)', 80, 450, 50, 350)
    o = [ax.replace('Rmin', 'R<tspan baseline-shift="sub" font-size="11">min</tspan>').replace('Nmin', 'N<tspan baseline-shift="sub" font-size="11">min</tspan>')]
    o.append(P([(fx(X), fy(gill(X))) for X in [0.002 * i for i in range(1, 500)] + [0.999]], AC, 3))
    for X, lab, c, dx, dy, anc in ((0.1429, 'ternary example: X 0.143, Y 0.512', NX, 14, -14, 'start'), (0.1852, 'binary column at R = 2: X 0.185, Y 0.473', LV, 14, 22, 'start')):
        Y = gill(X); o.append(L(fx(X), fy(0), fx(X), fy(Y), c, 1.3, '4 4')); o.append(C(fx(X), fy(Y), 6, c))
        o.append(Tb(fx(X) + dx, fy(Y) + dy, lab, 12, anc, c, True))
    o.append(Tb(fx(0.75), fy(0.22), 'Molokanov fit', 13, 'middle', AC, True))
    o.append(boxt(470, 60, 240, 230, ['N = (Nmin + Y)/(1 − Y)', 'ternary:', '(8.49 + 0.512)/0.488', '= 18.4 → 19 stages', 'binary (4.4 example):', '(6.43 + 0.473)/0.527', '= 13.1 (staircase 13)'], ACS, AC, 13, True)
             .replace('Nmin', 'N<tspan baseline-shift="sub" font-size="10">min</tspan>'))
    return 400, ''.join(o)
FIG[8] = (f8, 'The Gilliland correlation in its Molokanov form, with the two columns of this unit marked: the ternary benzene-toluene-xylene example (X = 0.143 gives Y = 0.512 and N = 18.4) and the binary McCabe-Thiele column at R = 2, where the correlation gives 13.1 stages against 13 from the staircase.',
          'A falling curve of Y against X from Y 1 at X 0 to Y 0 at X 1, with two marked points near X 0.14 and 0.19 and a box showing N equals N min plus Y over 1 minus Y worked for both.')


# ---- 4.9 extractive distillation flowsheet ----
def f9():
    o = []
    def col(x, yt, yb, w=70):
        return R(x, yt, w, yb - yt, PANEL, INK, 24, 2.2)
    o.append(col(170, 70, 380)); o.append(col(470, 120, 380))
    o.append(T(205, 405, 'extractive column', 13, 'middle', INK, True)); o.append(T(548, 250, 'recovery', 13, 'start', INK, True)); o.append(T(548, 268, 'column', 13, 'start', INK, True))
    # feed
    o.append(L(40, 270, 168, 270, INK, 2.5, arrow='x')); o.append(T(40, 258, 'feed: ethanol + water', 12, 'start', INK, True)); o.append(T(40, 290, 'near the azeotrope', 12, 'start', MUT))
    # solvent in near top
    o.append(L(330, 110, 242, 110, NX, 2.5, arrow='x')); o.append(T(250, 100, 'glycol in', 12, 'start', NX, True))
    # overhead ethanol
    o.append(L(205, 70, 205, 40, AC, 2.5)); o.append(L(205, 40, 330, 40, AC, 2.5, arrow='n')); o.append(T(338, 36, 'dry ethanol overhead', 13, 'start', AC, True))
    # bottoms to recovery
    o.append(L(205, 380, 205, 440, LV, 2.5)); o.append(L(205, 440, 420, 440, LV, 2.5)); o.append(L(420, 440, 420, 300, LV, 2.5)); o.append(L(420, 300, 468, 300, LV, 2.5, arrow='l'))
    o.append(T(300, 432, 'bottoms: glycol + water', 12, 'middle', LV, True))
    # water overhead
    o.append(L(505, 120, 505, 96, AC, 2.5)); o.append(L(505, 96, 630, 96, AC, 2.5, arrow='n')); o.append(T(638, 101, 'water', 13, 'start', AC, True))
    # glycol recycle, routed round the outside of the recovery column
    o.append(L(505, 380, 505, 460, NX, 2.5)); o.append(L(505, 460, 705, 460, NX, 2.5)); o.append(L(705, 460, 705, 66, NX, 2.5))
    o.append(L(705, 66, 620, 66, NX, 2.5)); o.append(R(580, 52, 40, 28, PANEL, NX, 6)); o.append(T(600, 46, 'cooler', 12, 'middle', NX))
    o.append(L(580, 66, 350, 66, NX, 2.5)); o.append(L(350, 66, 350, 110, NX, 2.5)); o.append(L(350, 110, 330, 110, NX, 2.5))
    o.append(T(600, 478, 'lean glycol recycled', 12, 'middle', NX, True))
    o.append(boxt(250, 200, 160, 70, ['glycol makes', 'water less volatile'], ACS, AC, 12))
    return 490, ''.join(o)
FIG[9] = (f9, 'Extractive distillation of ethanol-water with ethylene glycol. The solvent enters near the top of the first column, lowers the volatility of water and carries it down; dry ethanol leaves overhead. The second column boils the water off the glycol, and the lean glycol is cooled and recycled.',
          'Two columns. The feed enters the middle of the first column, glycol enters near its top, ethanol leaves overhead and the glycol-water bottoms go to the second column, which sends water overhead and returns glycol from its bottom through a cooler to the top of the first column.')

spec = make_spec(FIG)
