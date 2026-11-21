"""Claude's hand-drawn figures for ch-thermo-u6 (Phase equilibria), one per chapter.
Every number comes from that chapter's worked examples. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def sb(base, s, size=11):
    return f'{base}<tspan baseline-shift="sub" font-size="{size}">{s}</tspan>'


def sp(base, s, size=11):
    return f'{base}<tspan baseline-shift="super" font-size="{size}">{s}</tspan>'


def curve(f, x0, x1, fx, fy, n=80, c=AC, w=2.5, dash=None):
    pts = [(fx(x0 + (x1 - x0) * i / n), fy(f(x0 + (x1 - x0) * i / n))) for i in range(n + 1)]
    return P(pts, c, w, dash)


def pcurve(pts, fx, fy, c=AC, w=2.5, dash=None):
    return P([(fx(a), fy(b)) for a, b in pts], c, w, dash)


# ---- criteria and stability: g^M/RT for A = 2.5 ----
def f1():
    o = []
    x0, x1, y0, y1 = 80, 520, 40, 360
    fx = lambda x: x0 + x * (x1 - x0)
    lo, hi = -0.12, 0.0
    fy = lambda g: y1 - (g - lo) / (hi - lo) * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.2, 0.4, 0.6, 0.8, 1.0], [-0.12, -0.10, -0.08, -0.06, -0.04, -0.02, 0.0], fx, fy,
                  'x₁', sp('g', 'M') + '/RT', lambda v: f'{v:g}', lambda v: neg(f'{v:.2f}')))
    g = lambda x: x * math.log(x) + (1 - x) * math.log(1 - x) + 2.5 * x * (1 - x)
    o.append(curve(g, 0.012, 0.988, fx, fy, c=AC, w=3))
    gb = g(0.1448)
    o.append(L(fx(0.04), fy(gb), fx(0.96), fy(gb), NX, 2, '7 4'))
    o.append(Tb(fx(0.5), fy(gb) + 22, 'common tangent', 13, 'middle', NX))
    for xb in (0.145, 0.855):
        o.append(C(fx(xb), fy(gb), 6, NX))
        o.append(L(fx(xb), fy(gb), fx(xb), y1, NX, 1.4, '3 4'))
        o.append(Tb(fx(xb), y1 - 10, f'{xb:.3f}', 13, 'middle', NX, bold=True))
    for xs in (0.2764, 0.7236):
        o.append(C(fx(xs), fy(g(xs)), 6, LV))
        o.append(L(fx(xs), fy(g(xs)), fx(xs), y1, LV, 1.4, '3 4'))
        o.append(Tb(fx(xs), y1 - 30, f'{xs:.3f}', 13, 'middle', LV, bold=True))
    o.append(C(fx(0.5), fy(g(0.5)), 6, AC))
    o.append(Tb(fx(0.5), fy(g(0.5)) - 12, '−0.068 at x₁ = 0.5', 13, 'middle', AC, bold=True))
    o.append(boxt(536, 52, 176, 150, ['A = 2.5, 300 K', 'binodal (layers):', 'x₁ = 0.145, 0.855', 'spinodal:', 'x₁ = 0.276, 0.724', 'at 0.5: curvature −1.0'], PANEL, AC, 13,
                  fills=[INK, NX, NX, LV, LV, AC]))
    o.append(boxt(536, 218, 176, 112, ['stable  |  metastable', '0–0.145 | 0.145–0.276', 'unstable', '0.276–0.724'], ACS, AC, 13))
    return 420, ''.join(o)
FIG[1] = (f1, 'The worked examples on one curve: for A = 2.5 the Gibbs energy of mixing has two minima and a hump. The common tangent touches it at x₁ = 0.145 and 0.855, the two coexisting layers; the inflection points at 0.276 and 0.724 are the spinodal, and the equimolar point (curvature −1.0) is unstable.',
          'A curve of g M over RT against x1 for A = 2.5, dipping to about minus 0.104 near x1 = 0.145 and 0.855 and rising to minus 0.068 at x1 = 0.5; a dashed horizontal common tangent joins the two minima, and dots mark the spinodal points at 0.276 and 0.724.')


# ---- phase rule and Duhem: the count ----
def f2():
    o = []
    o.append(boxt(20, 30, 210, 92, ['unknowns', 'T, P and C − 1 mole', 'fractions per phase', '2 + π(C − 1)'], PANEL, AC, 14, bold_first=True))
    o.append(boxt(255, 30, 210, 92, ['equations', 'equal μ of each', 'component in all phases', 'C(π − 1)'], PANEL, AC, 14, bold_first=True))
    o.append(boxt(490, 30, 210, 92, ['phase rule', 'unknowns − equations', 'F = C − π + 2', '(intensive only)'], ACS, AC, 14, bold_first=True))
    o.append(L(232, 76, 252, 76, AC, 2.2, arrow='n')); o.append(L(467, 76, 487, 76, AC, 2.2, arrow='n'))
    o.append(boxt(255, 150, 445, 74, ['Duhem, closed vessel: add π − 1 phase fractions,', 'add C − 1 material balances', '(C − π + 2) + (π − 1) − (C − 1) = 2'], NXS, NX, 14))
    o.append(L(595, 124, 595, 146, NX, 2, arrow='x'))
    o.append(L(253, 187, 234, 187, NX, 2, arrow='x'))
    o.append(boxt(20, 150, 210, 74, ['two variables fix', 'the state and the', 'amount of each phase'], PANEL, NX, 14))
    rows = [('System', 'C', 'π', 'F', 'what is free'),
            ('water, liquid + vapour', '1', '2', '1', 'T (P follows)'),
            ('ice + water + vapour', '1', '3', '0', 'nothing'),
            ('ethanol–water, L + V', '2', '2', '2', 'T and P'),
            ('same, at 1 atm', '2', '2', '1', 'T only'),
            ('N₂ + H₂ + NH₃, reacting', '3 − 1', '1', '3', 'T, P, one x')]
    cx = [40, 300, 365, 425, 480]
    y = 262
    o.append(R(20, 244, 680, 30, ACS, AC, 6, 1.5))
    for i, r in enumerate(rows):
        for j, s in enumerate(r):
            o.append(T(cx[j], y + i * 30, s, 14, 'start', INK if i else AC, bold=(i == 0)))
        if i: o.append(L(20, y + i * 30 + 10, 700, y + i * 30 + 10, LN, 1))
    return 440, ''.join(o)
FIG[2] = (f2, 'The count behind the phase rule (π is the number of phases): unknowns minus equations gives F = C − π + 2. Duhem\'s theorem adds the phase amounts and the material balances, which always leaves two variables for a closed vessel. The table repeats the worked example.',
          'Three boxes joined by arrows: unknowns 2 plus pi times C minus 1, equations C times pi minus 1, and the phase rule F = C minus pi plus 2; a fourth box gives Duhem\'s count of 2; a table lists water with two phases F = 1, the triple point F = 0, ethanol–water F = 2, the same at 1 atm F = 1 and the ammonia gas F = 3.')


# ---- pure components and mixtures: benzene-toluene P-x-y with a tie line ----
def f3():
    o = []
    x0, x1, y0, y1 = 80, 520, 40, 370
    fx = lambda x: x0 + x * (x1 - x0)
    fy = lambda p: y1 - (p - 60) / (190 - 60) * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.2, 0.4, 0.6, 0.8, 1.0], [60, 80, 100, 120, 140, 160, 180], fx, fy,
                  'x₁ or y₁ (benzene)', 'P (kPa) at 373.15 K', lambda v: f'{v:g}', lambda v: f'{v:g}'))
    P1, P2 = 180.1, 74.2
    o.append(curve(lambda x: P2 + (P1 - P2) * x, 0, 1, fx, fy, c=AC, w=3))
    o.append(curve(lambda y: 1 / (y / P1 + (1 - y) / P2), 0, 1, fx, fy, c=LV, w=3))
    o.append(Tb(fx(0.5), fy(P2 + (P1 - P2) * 0.5) - 14, 'bubble line (liquid x₁)', 13, 'end', AC, bold=True))
    o.append(Tb(fx(0.62), fy(1 / (0.62 / P1 + 0.38 / P2)) + 26, 'dew line (vapour y₁)', 13, 'start', LV, bold=True))
    xL, yV, z = 0.2436, 0.4388, 0.40
    o.append(L(fx(xL), fy(100), fx(yV), fy(100), NX, 2.5))
    o.append(C(fx(xL), fy(100), 6, AC)); o.append(C(fx(yV), fy(100), 6, LV)); o.append(C(fx(z), fy(100), 5, NX))
    o.append(L(fx(z), fy(100), fx(z), y1, NX, 1.3, '3 4'))
    o.append(Tb(fx(xL), fy(100) + 24, 'x₁ = 0.244', 13, 'end', AC, bold=True))
    o.append(Tb(fx(yV) + 6, fy(100) + 24, 'y₁ = 0.439', 13, 'start', LV, bold=True))
    o.append(Tb(fx(z) + 6, fy(66), 'z₁ = 0.40', 13, 'start', NX, bold=True))
    o.append(Tb(fx(0) + 8, fy(67), '74.2', 13, 'start', MUT)); o.append(Tb(fx(1) - 6, fy(186), '180.1', 13, 'end', MUT))
    o.append(T(fx(0.15), fy(170), 'liquid', 14, 'middle', MUT)); o.append(T(fx(0.78), fy(78), 'vapour', 14, 'middle', MUT))
    o.append(boxt(536, 52, 176, 150, ['first example', 'x₁ = 0.30:', 'P = 105.97, y₁ = 0.510', 'y₁ = 0.30:', 'P = 90.09, x₁ = 0.150'], PANEL, AC, 13, bold_first=True))
    o.append(boxt(536, 218, 176, 130, ['tie line at 100 kPa', 'liquid fraction', '(0.439 − 0.40)', '/(0.439 − 0.244)', '= 0.199'], NXS, NX, 13, bold_first=True))
    return 420, ''.join(o)
FIG[3] = (f3, 'Benzene–toluene at 373.15 K. The straight bubble line and the curved dew line meet the pure vapour pressures, 74.2 and 180.1 kPa. The tie line at 100 kPa joins liquid x₁ = 0.244 to vapour y₁ = 0.439, and a feed with z₁ = 0.40 is 19.9 % liquid by the lever rule.',
          'P-x-y diagram from 60 to 190 kilopascals: a straight bubble line from 74.2 to 180.1 and a curved dew line below it; a horizontal tie line at 100 kilopascals runs from x1 = 0.244 to y1 = 0.439 with the feed z1 = 0.40 marked between them.')


# ---- modified Raoult: P-x-y for A = 1.2, 60/20 kPa ----
def f4():
    o = []
    x0, x1, y0, y1 = 80, 520, 40, 370
    fx = lambda x: x0 + x * (x1 - x0)
    fy = lambda p: y1 - (p - 15) / (65 - 15) * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.2, 0.4, 0.6, 0.8, 1.0], [20, 30, 40, 50, 60], fx, fy,
                  'x₁ or y₁', 'P (kPa) at 343 K', lambda v: f'{v:g}', lambda v: f'{v:g}'))
    A, P1, P2 = 1.2, 60.0, 20.0
    def bub(x):
        g1, g2 = math.exp(A * (1 - x) ** 2), math.exp(A * x * x)
        p = x * g1 * P1 + (1 - x) * g2 * P2
        return p, x * g1 * P1 / p
    xs = [i / 100 for i in range(101)]
    o.append(curve(lambda x: P2 + (P1 - P2) * x, 0, 1, fx, fy, c=L2, w=2, dash='6 5'))
    o.append(Tb(fx(0.25), fy(P2 + 40 * 0.25) + 20, 'ideal Raoult', 13, 'middle', MUT))
    o.append(pcurve([(x, bub(x)[0]) for x in xs], fx, fy, c=AC, w=3))
    o.append(pcurve([(bub(x)[1], bub(x)[0]) for x in xs], fx, fy, c=LV, w=3))
    o.append(Tb(fx(0.18), fy(bub(0.18)[0]) - 12, 'bubble (x₁)', 13, 'middle', AC, bold=True))
    o.append(Tb(fx(0.52), fy(28), 'dew (y₁)', 13, 'start', LV, bold=True))
    p, y = bub(0.4)
    o.append(L(fx(0.4), fy(p), fx(y), fy(p), NX, 2.5))
    o.append(C(fx(0.4), fy(p), 6, AC)); o.append(C(fx(y), fy(p), 6, LV))
    o.append(Tb(fx(0.4), fy(p) + 24, 'x₁ = 0.40', 13, 'middle', AC, bold=True))
    o.append(Tb(fx(y), fy(p) + 24, 'y₁ = 0.718', 13, 'middle', LV, bold=True))
    o.append(Tb(fx(0.56), fy(p) - 10, '51.51 kPa', 13, 'middle', NX, bold=True))
    o.append(C(fx(0.4), fy(36.0), 5, L2)); o.append(Tb(fx(0.4) - 10, fy(36.0) - 8, 'ideal 36.0', 13, 'end', MUT))
    o.append(C(fx(0.958), fy(60.13), 6, NX))
    o.append(Tb(fx(0.97), fy(63.3), 'azeotrope x₁ = 0.958, 60.13 kPa', 13, 'end', NX, bold=True))
    o.append(boxt(536, 52, 176, 150, ['Margules A = 1.20', 'x₁ = 0.40:', 'γ₁ = 1.540, γ₂ = 1.212', 'P = 36.97 + 14.54', '= 51.51 kPa'], PANEL, AC, 13, bold_first=True))
    return 420, ''.join(o)
FIG[4] = (f4, 'The worked system at 343 K: positive deviation lifts the bubble curve far above the dashed Raoult line, giving 51.51 kPa instead of 36.0 at x₁ = 0.40, and the curves touch at a weak azeotrope near x₁ = 0.958.',
          'P-x-y diagram at 343 K: a dashed straight ideal line from 20 to 60 kilopascals, a bowed bubble curve well above it and a dew curve below that; a tie line at 51.51 kilopascals joins x1 = 0.40 to y1 = 0.718, and the curves meet at an azeotrope near x1 = 0.958 and 60.13 kilopascals.')


# ---- Henry's law ----
def f5():
    o = []
    x0, x1, y0, y1 = 80, 500, 40, 360
    fx = lambda x: x0 + x * (x1 - x0)
    fy = lambda p: y1 - p / 90 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.2, 0.4, 0.6, 0.8, 1.0], [0, 15, 30, 45, 60, 75, 90], fx, fy,
                  'x₁', sb('p', '1') + ' (kPa)', lambda v: f'{v:g}', lambda v: f'{v:g}'))
    A = math.log(1.5)
    o.append(curve(lambda x: 90 * x, 0, 1, fx, fy, c=NX, w=2.2, dash='7 4'))
    o.append(curve(lambda x: 60 * x, 0, 1, fx, fy, c=LV, w=2.2, dash='7 4'))
    o.append(curve(lambda x: x * math.exp(A * (1 - x) ** 2) * 60, 0, 1, fx, fy, c=AC, w=3))
    o.append(Tb(fx(0.62), fy(90 * 0.62) - 10, 'Henry: ' + sb('p', '1') + ' = 90x₁', 13, 'end', NX, bold=True))
    o.append(Tb(fx(0.7), fy(60 * 0.7) + 30, 'Raoult: ' + sb('p', '1') + ' = 60x₁', 13, 'start', LV, bold=True))
    o.append(Tb(fx(0.74), fy(0.74 * math.exp(A * 0.26 ** 2) * 60) - 12, 'real', 13, 'end', AC, bold=True))
    o.append(C(fx(1), fy(60), 6, AC)); o.append(T(fx(1) - 8, fy(60) - 14, sp('P', 'sat') + ' = 60', 13, 'end', AC))
    o.append(C(fx(0.5), fy(33.2), 6, AC)); o.append(Tb(fx(0.5) + 8, fy(33.2) + 32, '33.2 at x₁ = 0.5', 13, 'start', AC))
    o.append(boxt(530, 52, 182, 130, ['CO₂ in water, 298 K', 'H ≈ 1670 bar', 'at 3.0 bar:', 'x = 1.80 × 10⁻³', '0.0999 mol/kg'], PANEL, AC, 13, bold_first=True))
    o.append(boxt(530, 198, 182, 130, ['O₂ from air, 298 K', 'H ≈ 4.4 × 10⁴ bar', 'p = 0.213 bar:', 'x = 4.8 × 10⁻⁶', '≈ 8.6 mg/kg'], ACS, AC, 13, bold_first=True))
    return 410, ''.join(o)
FIG[5] = (f5, 'One curve, two laws: the real partial pressure leaves the origin along the Henry tangent (slope 90 kPa) and reaches x₁ = 1 along the Raoult line (slope 60 kPa), lying between them in the middle (33.2 kPa at x₁ = 0.5). The boxes give the two worked gas solubilities.',
          'Partial pressure against x1 from 0 to 1: a dashed Henry line of slope 90, a dashed Raoult line of slope 60 and a solid real curve that starts along the Henry line and ends at 60 kilopascals on the Raoult line; side boxes give carbon dioxide at 3 bar dissolving to x = 1.80 times 10 to the minus 3 and oxygen from air to 8.6 milligrams per kilogram.')


# ---- high pressure: the flash loop with the worked numbers ----
def f6():
    o = []
    bx = [(20, 30, 300, 62, ['fix T = 300 K, P = 20 bar', 'z = 0.30, 0.30, 0.40'], PANEL, AC),
          (20, 118, 300, 62, ['Wilson K: 16.70, 0.503, 0.129'], PANEL, AC),
          (20, 206, 300, 62, ['test: Σz·K = 5.21 > 1', 'Σz/K = 3.71 > 1 → two phases'], NXS, NX),
          (20, 294, 300, 62, ['Rachford-Rice → β = 0.368'], PANEL, AC),
          (20, 382, 300, 62, ['x = 0.044, 0.367, 0.589', 'y = 0.739, 0.185, 0.076'], ACS, AC)]
    for x, y, w, h, lines, fill, st in bx:
        o.append(boxt(x, y, w, h, lines, fill, st, 14))
    for y in (92, 180, 268, 356):
        o.append(L(170, y + 1, 170, y + 24, AC, 2.2, arrow='n'))
    o.append(boxt(360, 382, 340, 62, ['EOS φ at these x, y:', 'K = φ' + sp('', 'L') + '/φ' + sp('', 'V')], PANEL, LV, 14))
    o.append(L(322, 413, 357, 413, LV, 2.2, arrow='l'))
    o.append(P([(530, 380), (530, 325), (325, 325)], LV, 2.2, '7 4'))
    o.append(L(332, 325, 324, 325, LV, 2.2, arrow='l'))
    o.append(Tb(530, 352, 'repeat until K stops changing', 13, 'middle', LV, bold=True))
    # Rachford-Rice plot
    gx0, gx1, gy0, gy1 = 410, 700, 40, 280
    fx = lambda b: gx0 + b * (gx1 - gx0)
    fy = lambda f: gy1 - (f + 1) / 5.5 * (gy1 - gy0)
    o.append(axes(gx0, gx1, gy0, gy1, [0, 0.5, 1.0], [-1, 0, 1, 2, 3, 4], fx, fy, 'vapour fraction β', 'f(β)', lambda v: f'{v:g}', lambda v: neg(str(v))))
    K = [16.7025, 0.50317, 0.12901]; z = [0.3, 0.3, 0.4]
    f = lambda b: sum(zi * (Ki - 1) / (1 + b * (Ki - 1)) for zi, Ki in zip(z, K))
    o.append(curve(f, 0, 0.62, fx, lambda v: fy(max(v, -1)), c=AC, w=3))
    o.append(L(gx0, fy(0), gx1, fy(0), INK, 1.2))
    o.append(C(fx(0.3679), fy(0), 6, NX)); o.append(Tb(fx(0.3679) + 10, fy(0) - 12, 'β = 0.368', 13, 'start', NX, bold=True))
    o.append(Tb(fx(0) + 10, fy(4.213) + 4, 'f(0) = 4.21', 13, 'start', AC))
    return 460, ''.join(o)
FIG[6] = (f6, 'The second worked example on the flash loop: Wilson K-values for methane, propane and n-butane at 300 K and 20 bar, the two-phase test, the Rachford-Rice root β = 0.368 (right, where f(β) crosses zero) and the phase compositions. The phi-phi method then updates K from the EOS and repeats.',
          'A column of five boxes: feed at 300 K and 20 bar, Wilson K values 16.70, 0.503 and 0.129, the two-phase test, beta = 0.368, and the liquid and vapour compositions; a side box for the equation-of-state update with a dashed arrow looping back; a small plot of the Rachford-Rice function falling from 4.21 at beta = 0 and crossing zero at 0.368.')


# ---- LLE and SLE: ideal eutectic ----
def f7():
    o = []
    x0, x1, y0, y1 = 80, 520, 40, 370
    fx = lambda x: x0 + x * (x1 - x0)
    fy = lambda T: y1 - (T - 290) / (355 - 290) * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.2, 0.4, 0.6, 0.8, 1.0], [290, 300, 310, 320, 330, 340, 350], fx, fy,
                  sb('x', 'A') + ' in the liquid', 'T (K)', lambda v: f'{v:g}', lambda v: f'{v:g}'))
    R_ = 8.314
    xA = lambda T: math.exp(-20000 / R_ * (1 / T - 1 / 330))
    xB = lambda T: math.exp(-25000 / R_ * (1 / T - 1 / 350))
    Te = 311.70
    TA = [Te + (330 - Te) * i / 60 for i in range(61)]
    TB = [Te + (350 - Te) * i / 60 for i in range(61)]
    o.append(pcurve([(xA(T), T) for T in TA], fx, fy, c=AC, w=3))
    o.append(pcurve([(1 - xB(T), T) for T in TB], fx, fy, c=LV, w=3))
    Tx = [300 + (Te - 300) * i / 30 for i in range(31)]
    o.append(pcurve([(xA(T), T) for T in Tx], fx, fy, c=AC, w=2, dash='6 5'))
    o.append(L(fx(0), fy(Te), fx(1), fy(Te), NX, 2.2))
    o.append(C(fx(0.652), fy(Te), 7, NX))
    o.append(Tb(fx(0.652) + 14, fy(Te) + 20, 'eutectic 311.7 K, ' + sb('x', 'A') + ' = 0.652', 13, 'start', NX, bold=True))
    o.append(C(fx(1), fy(330), 6, AC)); o.append(T(fx(1) - 10, fy(330) - 10, 'A melts 330 K', 13, 'end', AC, bold=True))
    o.append(C(fx(0), fy(350), 6, LV)); o.append(T(fx(0) + 12, fy(352.6), 'B melts 350 K', 13, 'start', LV, bold=True))
    o.append(C(fx(0.4824), fy(300), 6, AC)); o.append(Tb(fx(0.4824) + 10, fy(300) - 10, '0.482 at 300 K (ideal)', 13, 'start', AC))
    o.append(C(fx(0.268), fy(300), 6, NX)); o.append(Tb(fx(0.268) - 10, fy(300) - 10, '0.268 (γ = 1.8)', 13, 'end', NX))
    o.append(T(fx(0.5), fy(342), 'liquid', 15, 'middle', MUT))
    o.append(T(fx(0.25), fy(322), 'liquid + solid B', 13, 'middle', MUT)); o.append(T(fx(0.88), fy(316.5), 'liquid + A', 13, 'middle', MUT))
    o.append(T(fx(0.3), fy(306), 'solid A + solid B', 13, 'middle', MUT))
    o.append(boxt(536, 52, 176, 128, ['A: 20.0 kJ/mol', 'B: 25.0 kJ/mol', 'eutectic where', sb('x', 'A') + ' + ' + sb('x', 'B') + ' = 1'], PANEL, AC, 13))
    return 420, ''.join(o)
FIG[7] = (f7, 'The two worked examples on one diagram. Each solid\'s ideal solubility curve falls from its melting point (A at 330 K, B at 350 K) until they cross at the eutectic, 311.7 K and x<sub>A</sub> = 0.652. Extended (dashed) to 300 K, the curve for A gives the ideal solubility 0.482, and 0.268 with γ = 1.8.',
          'Temperature against mole fraction of A: a curve from B\'s melting point at 350 kelvin falling to the right and a curve from A\'s melting point at 330 kelvin falling to the left meet at the eutectic, 311.7 kelvin and xA = 0.652, with a horizontal eutectic line; a dashed extension of A\'s curve reaches 0.482 at 300 kelvin, and 0.268 is marked for gamma 1.8.')


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
