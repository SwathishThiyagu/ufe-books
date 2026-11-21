"""Claude's hand-drawn figures for me-design-u1 (Machine Design: design process and stresses), one per chapter, drawn from
each chapter's own worked example. Every plotted value is computed here from the example's data. Colours are the shell's
CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def sb(base, s, size=14):
    """text with a subscript, for SVG labels"""
    return f'{base}<tspan dy="4" font-size="{size - 3}">{s}</tspan><tspan dy="-4"> </tspan>'


# ---- 1.1 the design loop ----
def f1():
    o = []
    w, h = 150, 54
    top = [('Need', 'fan must hang'), ('Specification', '8 kg, ₹250, 5 yr'), ('Concept', 'flat, angle or T'), ('Analysis', 'forces, material')]
    bot = [('Production', 'jig, inspection'), ('Prototype test', 'hang, shake'), ('Drawing', 'sizes, tolerances'), ('Design of', 'elements')]
    xs = [20, 200, 380, 560]
    for i, (a, b) in enumerate(top):
        o.append(boxt(xs[i], 40, w, h, [a, b], ACS if i == 0 else PANEL, AC, 14, True))
        if i < 3: o.append(L(xs[i] + w + 2, 67, xs[i + 1] - 4, 67, AC, 2, arrow='n'))
    for i, (a, b) in enumerate(bot):
        st = LV if a == 'Prototype test' else AC
        fl = LVS if a == 'Prototype test' else (NXS if a == 'Production' else PANEL)
        o.append(boxt(xs[i], 190, w, h, [a, b], fl, st, 14, True))
        if i > 0: o.append(L(xs[i] - 2, 217, xs[i - 1] + w + 4, 217, AC, 2, arrow='n'))
    o.append(L(635, 96, 635, 186, AC, 2, arrow='n'))
    # feedback paths
    o.append(arc(275, 188, 455, 98, -0.25, LV, 2, 'l', '6 4'))
    o.append(Tb(330, 150, 'revise concept', 13, 'middle', LV))
    o.append(arc(310, 246, 610, 246, -0.22, LV, 2, 'l', '6 4'))
    o.append(T(460, 300, 'resize after test', 13, 'middle', LV))
    o.append(T(360, 332, 'Cost check for the 200-piece order: ₹230 direct + ₹10 jig = ₹240 ≤ ₹250', 14, 'middle', INK, True))
    return 350, ''.join(o)


FIG[1] = (f1, 'The design procedure for the fan bracket of the worked example, read along the top row and back along the bottom. The dashed arrows are the feedback that makes it a loop: a failed prototype test sends the team back to the concept or to the sizes.',
          'Eight boxes in two rows: need, specification, concept, analysis, then design of elements, drawing, prototype test and production. Dashed feedback arrows run from prototype test back to concept and to design of elements. The cost line reads 230 plus 10 equals 240 rupees per bracket, within 250.')


# ---- 1.2 tie rod sized in three materials ----
def f2():
    o = []
    mats = [('Mild steel', 0.628, 37.7, 'strength'), ('Aluminium 6061-T6', 0.326, 97.8, 'stiffness'), ('Alloy steel', 0.327, 39.2, 'stiffness')]
    o.append(T(20, 26, 'Tie rod 500 mm, 20 kN, n = 2, stretch ≤ 0.6 mm', 15, 'start', INK, True))
    x0, x1 = 190, 690
    o.append(T(x0, 58, 'mass (kg)', 14, 'start', MUT, True))
    o.append(T(x0, 196, 'cost (₹)', 14, 'start', MUT, True))
    for i, (n, m, c, gov) in enumerate(mats):
        y = 72 + i * 34
        o.append(T(180, y + 17, n, 14, 'end'))
        wd = m / 0.7 * (x1 - x0 - 120)
        o.append(R(x0, y, wd, 24, ACS if i != 2 else ACS, AC, 3))
        o.append(T(x0 + wd + 8, y + 17, f'{m:.3f}  ({gov})', 13, 'start', INK))
        y2 = 210 + i * 34
        o.append(T(180, y2 + 17, n, 14, 'end'))
        wd2 = c / 100 * (x1 - x0 - 120)
        o.append(R(x0, y2, wd2, 24, NXS, NX, 3))
        o.append(T(x0 + wd2 + 8, y2 + 17, f'{c:.1f}', 13, 'start', INK))
    o.append(L(x0, 66, x0, 176, L2, 1.5)); o.append(L(x0, 204, x0, 314, L2, 1.5))
    o.append(T(360, 340, 'Alloy steel: almost the lightest at about the lowest cost', 14, 'middle', LV, True))
    return 356, ''.join(o)


FIG[2] = (f2, 'The tie rod of the first worked example sized in each material: the word in brackets is the check that set its area. Aluminium is lighter than alloy steel by only a gram, because stiffness, not strength, governs both, but it costs two and a half times as much.',
          'Two bar charts for three materials. Mass: mild steel 0.628 kg (strength governs), aluminium 0.326 kg (stiffness), alloy steel 0.327 kg (stiffness). Cost: 37.7, 97.8 and 39.2 rupees.')


# ---- 1.3 tolerance zones at 25 mm ----
def f3():
    o = []
    y0 = 200; s = 4.2  # px per micrometre
    Y = lambda um: y0 - um * s
    o.append(L(60, y0, 690, y0, INK, 2))
    o.append(T(690, y0 - 8, 'zero line: 25.000 mm', 13, 'end', MUT))
    o.append(L(60, Y(40), 60, Y(-28), L2, 1.5))
    for v in (-20, 0, 20, 40):
        o.append(L(54, Y(v), 60, Y(v), L2, 1.5)); o.append(T(48, Y(v) + 4.5, neg(v), 13, 'end', MUT))
    o.append(T(20, 22, 'μm', 13, 'start', MUT))
    # hole H7
    o.append(R(100, Y(21), 120, 21 * s, ACS, AC, 2))
    o.append(T(160, Y(21) - 8, 'hole H7: 0 to +21', 13, 'middle', AC, True))
    shafts = [('g6', -20, -7, 'clearance', NX, NXS, 290), ('k6', 2, 15, 'transition', LV, LVS, 430), ('p6', 22, 35, 'interference', AC, ACS, 570)]
    for name, lo, hi, kind, c, fl, x in shafts:
        o.append(R(x, Y(hi), 100, (hi - lo) * s, fl, c, 2))
        lab = f'shaft {name}: {neg(lo)} to {neg(hi) if hi < 0 else "+" + str(hi)}'
        if lo > 0: lab = f'shaft {name}: +{lo} to +{hi}'
        ty = Y(hi) - 8 if hi > 0 else Y(lo) + 20
        o.append(T(x + 50, ty, lab, 13, 'middle', c, True))
        o.append(T(x + 50, Y(-28) + 6 if hi > 0 else Y(lo) + 40, kind, 13, 'middle', INK))
    # clearances for g6
    o.append(L(250, Y(21), 250, Y(-20), INK, 1.5, arrow=None))
    o.append(L(244, Y(21), 256, Y(21), INK, 1.5)); o.append(L(244, Y(-20), 256, Y(-20), INK, 1.5))
    o.append(T(244, Y(-12), 'max clearance', 13, 'end', INK))
    o.append(T(244, Y(-12) + 17, '41 μm', 13, 'end', INK, True))
    return 330, ''.join(o)


FIG[3] = (f3, 'Tolerance zones at 25 mm drawn to scale about the zero line (the basic size). The H7 hole runs from 0 to +21 μm; with a g6 shaft the zones never overlap, so the fit always has clearance (0.007 to 0.041 mm, as in the second worked example); a k6 shaft overlaps the hole zone (transition) and a p6 shaft lies wholly above it (interference).',
          'Deviation scale in micrometres with the zero line at 25.000 mm. Hole H7 from 0 to plus 21. Shafts: g6 from minus 20 to minus 7 (clearance), k6 from plus 2 to plus 15 (transition), p6 from plus 22 to plus 35 (interference). Maximum clearance with g6 is 41 micrometres.')


# ---- 1.4 stresses of the tie example ----
def f4():
    o = []
    x0 = 230; s = 1.25  # px per MPa
    rows = [('Yield strength S', 'yt', 280, PANEL, MUT), ('Working stress, 250 mm²', '', 180, LVS, LV), ('Allowable = 280/2.5', '', 112, ACS, AC), ('Working stress, 25 mm bar', '', 91.7, NXS, NX)]
    for i, (lab, sub, v, fl, c) in enumerate(rows):
        y = 40 + i * 52
        txt = sb('Yield strength S', 'yt') if sub else lab
        o.append(T(x0 - 10, y + 20, txt, 14, 'end'))
        o.append(R(x0, y, v * s, 30, fl, c, 3))
        o.append(Tb(x0 + v * s + 8, y + 20, f'{v:g} MPa', 14, 'start', INK, True))
    xa = x0 + 112 * s
    o.insert(0, L(xa, 28, xa, 254, AC, 2, '6 4'))
    o.append(T(xa + 6, 272, 'limit 112 MPa', 13, 'start', AC, True))
    o.append(T(x0 + 180 * s + 80, 112, 'unsafe: n = 1.56', 13, 'start', LV, True))
    o.append(T(x0 + 91.7 * s + 84, 216, 'safe: n = 3.05', 13, 'start', NX, True))
    o.append(T(360, 304, 'n = strength ÷ working stress; safe when n ≥ 2.5', 14, 'middle', INK, True))
    return 322, ''.join(o)


FIG[4] = (f4, 'The steel tie of the first worked example on one stress scale. Dividing the yield strength by n = 2.5 sets the 112 MPa limit; the 250 mm² tie works at 180 MPa, past the limit, while the 25 mm bar works at 91.7 MPa, inside it.',
          'Horizontal bars: yield strength 280 MPa, working stress of the 250 square millimetre tie 180 MPa, allowable stress 112 MPa, working stress of the 25 mm bar 91.7 MPa. A dashed line marks the 112 MPa limit.')


# ---- 1.5 three load histories ----
def f5():
    o = []
    panels = [('Static', 30), ('Dynamic (repeated)', 262), ('Impact', 494)]
    for name, x in panels:
        o.append(T(x + 98, 28, name, 15, 'middle', INK, True))
        o.append(L(x, 210, x + 196, 210, L2, 1.5, arrow='m')); o.append(L(x, 210, x, 50, L2, 1.5, arrow='m'))
        o.append(T(x + 190, 230, 'time', 13, 'end', MUT)); o.append(T(x + 6, 60, 'load', 13, 'start', MUT))
    o.append(L(30, 150, 216, 150, AC, 3))
    o.append(T(123, 140, 'W constant', 13, 'middle', AC))
    pts = [(262 + t, 140 - 50 * math.sin(t / 186 * 4 * math.pi)) for t in range(0, 187, 3)]
    o.append(P(pts, NX, 3))
    o.append(T(355, 80, 'repeats: fatigue', 13, 'middle', NX))
    pts = [(494, 192), (530, 192), (540, 62), (550, 192), (690, 192)]
    o.append(P(pts, LV, 3))
    o.append(T(556, 86, 'σ = 88.8 MPa', 13, 'start', LV, True))
    o.append(T(574, 182, 'static 0.196 MPa', 13, 'start', MUT))
    o.append(T(360, 268, 'Falling 10 kg weight, h = 100 mm: the peak is 452 times the static stress', 14, 'middle', INK, True))
    return 286, ''.join(o)


FIG[5] = (f5, 'The three load histories, sketched (not to scale). A static load stays put, a dynamic load repeats and calls for a fatigue check, and an impact is a short, high spike: in the worked example a 10 kg weight dropped 100 mm raises the stress from 0.196 MPa to 88.8 MPa.',
          'Three small load-time sketches: a flat line for a static load, a repeating wave for a dynamic load, and a single sharp spike for an impact, labelled 88.8 MPa against a static 0.196 MPa.')


# ---- 1.6 stress patterns across the 40 mm shaft ----
def f6():
    o = []
    cy, r = 170, 100  # section from y = 70 (top) to 270 (bottom); 40 mm diameter
    cols = [(110, 'Direct  P/A', 'uniform', AC, ACS), (360, 'Bending  M/Z', 'linear', NX, NXS), (600, 'Torsion  T/Z', 'linear from axis', LV, LVS)]
    for x, t, sub, c, fl in cols:
        o.append(T(x, 30, t.replace('Z', 'Z') if 'Torsion' not in t else 'Torsion  T/Zp', 15, 'middle', INK, True))
        o.append(T(x, 50, sub, 13, 'middle', MUT))
        o.append(L(x, cy - r - 6, x, cy + r + 6, L2, 1.5))
    s = 0.9  # px per MPa
    # direct: uniform compression -23.87
    xd = 110
    o.append(P([(xd, 70), (xd - 23.87 * s * 2, 70), (xd - 23.87 * s * 2, 270), (xd, 270)], AC, 2, fill=ACS))
    o.append(T(xd - 50, cy + 5, '−23.87', 13, 'end', AC, True))
    # bending: +95.49 bottom? tension at top
    xb = 360
    o.append(P([(xb, 70), (xb + 95.49 * s, 70), (xb - 95.49 * s, 270), (xb, 270)], NX, 2, fill=NXS))
    o.append(T(xb + 95.49 * s + 6, 76, '+95.49', 13, 'start', NX, True))
    o.append(T(xb - 95.49 * s - 6, 270, '−95.49', 13, 'end', NX, True))
    o.append(T(xb + 66, cy + 5, 'neutral axis, 0', 13, 'start', MUT))
    o.append(L(xb - 60, cy, xb + 60, cy, MUT, 1.5, '4 3'))
    # torsion: 0 at axis, 35.81 at surface, both sides same sense drawn outward
    xt = 600; st = 2.0
    o.append(P([(xt, 70), (xt + 35.81 * st, 70), (xt, cy), (xt - 35.81 * st, 270), (xt, 270)], LV, 2, fill=LVS))
    o.append(T(xt + 35.81 * st + 6, 76, '35.81', 13, 'start', LV, True))
    o.append(T(xt + 8, cy + 5, 'axis, 0', 13, 'start', MUT))
    o.append(T(360, 306, 'Stresses in MPa across the 40 mm diameter: P = 30 kN, M = 600 N·m, T = 450 N·m', 14, 'middle', INK, True))
    return 322, ''.join(o)


FIG[6] = (f6, 'How each load spreads across the diameter of the 40 mm shaft in the first worked example. The axial load gives a uniform 23.87 MPa compression, bending a linear stress from +95.49 to −95.49 MPa through zero at the neutral axis, and torsion a shear stress from zero at the axis to 35.81 MPa at the surface.',
          'Three stress profiles across the shaft diameter: uniform direct compression of 23.87 MPa; bending stress varying linearly from plus 95.49 at the top to minus 95.49 at the bottom; torsional shear rising from zero at the axis to 35.81 MPa at the surface.')


# ---- 1.7 Mohr's circle of the shaft example ----
def f7():
    o = []
    sx, txy = 65.19, 19.45
    c, Rr = sx / 2, math.hypot(sx / 2, txy)
    s = 4.6
    X0, Y0 = 160, 232
    X = lambda v: X0 + v * s
    Yy = lambda v: Y0 - v * s
    o.append(L(X(-20), Y0, X(90), Y0, L2, 1.5, arrow='m')); o.append(T(X(90) - 2, Y0 - 10, 'σ (MPa)', 13, 'end', MUT))
    o.append(L(X0, Yy(-44), X0, Yy(44), L2, 1.5, arrow='m')); o.append(T(X0 + 10, Yy(44) + 12, 'τ (MPa)', 13, 'start', MUT))
    o.append(f'<circle cx="{X(c):.1f}" cy="{Y0}" r="{Rr * s:.1f}" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2.5"/>')
    o.append(L(X(sx), Yy(txy), X(0), Yy(-txy), INK, 1.8))
    o.append(C(X(sx), Yy(txy), 5, LV)); o.append(T(X(sx) + 10, Yy(txy) - 6, 'x face (65.19, 19.45)', 13, 'start', LV, True))
    o.append(C(X(0), Yy(-txy), 5, LV)); o.append(T(X(0) - 8, Yy(-txy) + 20, 'y face (0, −19.45)', 13, 'end', LV, True))
    o.append(C(X(c), Y0, 4, INK)); o.append(T(X(c), Y0 + 20, 'C 32.60', 13, 'middle', INK))
    o.append(C(X(c + Rr), Y0, 5, NX)); o.append(T(X(c + Rr) + 8, Y0 + 20, 'σ₁ = 70.55', 14, 'start', NX, True))
    o.append(C(X(c - Rr), Y0, 5, NX)); o.append(T(X(c - Rr) - 8, Y0 - 10, 'σ₂ = −5.36', 14, 'end', NX, True))
    o.append(L(X(c), Y0, X(c), Yy(Rr), MUT, 1.5, '5 4'))
    o.append(C(X(c), Yy(Rr), 4, INK)); o.append(T(X(c) + 8, Yy(Rr) - 8, 'τmax = 37.96', 13, 'start', INK, True))
    o.append(T(X(c) + 60, Y0 - 14, '2θp = 30.8°', 13, 'start', INK))
    return 450, ''.join(o)


FIG[7] = (f7, 'Mohr\'s circle for the shaft surface of the first worked example. The x face (65.19, 19.45) and the y face (0, −19.45) are the ends of a diameter; the circle, centred at 32.60 MPa with radius 37.96 MPa, cuts the σ axis at the two principal stresses.',
          'Mohr circle with centre at 32.60 megapascals and radius 37.96. The x face point is at 65.19, 19.45 and the y face point at 0, minus 19.45. The circle meets the sigma axis at 70.55 and minus 5.36; the top of the circle is the maximum shear stress, 37.96.')


# ---- 1.8 strength and stiffness against width ----
def f8():
    o = []
    x0, x1, y0, y1 = 90, 680, 40, 270
    bmin, bmax, rmax = 26, 40, 2.4
    fx = lambda b: x0 + (b - bmin) / (bmax - bmin) * (x1 - x0)
    fy = lambda r: y1 - r / rmax * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [26, 28, 30, 32, 34, 36, 38, 40], [0, 0.5, 1.0, 1.5, 2.0], fx, fy, 'width b (mm), depth h = 2b', 'actual ÷ allowed', yfmt=lambda v: f'{v:g}'))
    bs = [bmin + i * 0.1 for i in range(141)]
    st = [(fx(b), fy(4.5e6 / b ** 3 / 120)) for b in bs if 4.5e6 / b ** 3 / 120 <= rmax]
    sf = [(fx(b), fy(2.7e6 / b ** 4 / 3)) for b in bs if 2.7e6 / b ** 4 / 3 <= rmax]
    o.append(P(st, AC, 3)); o.append(P(sf, NX, 3))
    o.append(L(x0, fy(1), x1, fy(1), LV, 2, '6 4'))
    o.append(T(x1 - 4, fy(1) - 8, 'limit = 1', 13, 'end', LV, True))
    o.append(C(fx(33.47), fy(1), 5, AC)); o.append(L(fx(33.6), fy(1.04), fx(35.3), fy(1.32), AC, 1.5)); o.append(T(fx(35.4), fy(1.36), 'strength: 33.47', 13, 'start', AC, True))
    o.append(C(fx(30.80), fy(1), 5, NX)); o.append(T(fx(30.80) - 6, fy(1) + 22, 'stiffness: 30.80', 13, 'end', NX, True))
    o.append(T(fx(27.0), fy(2.05), 'σ/120', 14, 'start', AC, True))
    o.append(T(fx(29.6), fy(1.6), 'δ/3', 14, 'start', NX, True))
    o.append(L(fx(34), y0, fx(34), y1, MUT, 1.5, '3 3'))
    o.append(T(fx(34) + 6, y0 + 10, 'chosen 34 mm', 13, 'start', INK, True))
    return 330, ''.join(o)


FIG[8] = (f8, 'The beam of the first worked example: stress and deflection, each divided by its allowed value, plotted against the width. A width is acceptable only where both curves are below 1; the stiffness curve crosses at 30.80 mm and the strength curve later, at 33.47 mm, so strength governs and 34 mm is chosen.',
          'Two falling curves against width from 26 to 40 mm: stress over 120 MPa and deflection over 3 mm. They cross the limit line of 1 at 33.47 mm and 30.80 mm. A dotted line marks the chosen width of 34 mm.')


# ---- 1.9 stress across the hook section ----
def f9():
    o = []
    Ri, Ro, b, h, Pl = 40.0, 100.0, 30.0, 60.0, 20000.0
    A = b * h; R = Ri + h / 2; Rn = h / math.log(Ro / Ri); e = R - Rn; M = Pl * R; Z = b * h * h / 6
    cur = lambda r: Pl / A + M * (Rn - r) / (A * e * r)
    stra = lambda r: Pl / A + M * (R - r) / (Z * h / 2)
    x0, x1, y0, y1 = 90, 660, 40, 300
    fx = lambda r: x0 + (r - 40) / 60 * (x1 - x0)
    fy = lambda s: y0 + (130 - s) / 215 * (y1 - y0)
    o.append(L(x0, y0, x0, fy(-80), L2, 1.5))
    for v in (-50, 0, 50, 100):
        o.append(L(x0 - 5, fy(v), x0, fy(v), L2, 1.5)); o.append(T(x0 - 9, fy(v) + 4.5, neg(v), 13, 'end', MUT))
        o.append(L(x0, fy(v), x1, fy(v), LN, 1))
    o.append(L(x0, fy(0), x1, fy(0), L2, 1.5))
    for r in (40, 55, 70, 85, 100):
        o.append(T(fx(r), fy(-85) + 4, str(r), 13, 'middle', MUT))
    o.append(T((x0 + x1) / 2, fy(-85) + 26, 'radius r (mm): inner fibre 40, outer fibre 100', 13, 'middle', MUT))
    o.append(T(x0 - 4, y0 - 14, 'resultant stress (MPa)', 13, 'start', MUT))
    rs = [40 + i * 0.5 for i in range(121)]
    o.append(P([(fx(r), fy(cur(r))) for r in rs], AC, 3))
    o.append(P([(fx(r), fy(stra(r))) for r in rs], MUT, 2, '7 5'))
    o.append(C(fx(40), fy(cur(40)), 5, AC)); o.append(T(fx(40) + 10, fy(cur(40)) + 4, f'{cur(40):.1f} curved', 13, 'start', AC, True))
    o.append(C(fx(40), fy(stra(40)), 4, MUT)); o.append(T(fx(41.5), fy(38), f'{stra(40):.1f} straight', 13, 'start', MUT, True))
    o.append(C(fx(100), fy(cur(100)), 5, AC)); o.append(T(fx(100) - 8, fy(cur(100)) - 10, f'−{abs(cur(100)):.1f}', 13, 'end', AC, True))
    o.append(C(fx(100), fy(stra(100)), 4, MUT)); o.append(T(fx(98.5), fy(-75), f'−{abs(stra(100)):.1f} straight', 13, 'end', MUT, True))
    o.append(L(fx(Rn), fy(110), fx(Rn), fy(-55), NX, 1.5, '4 3'))
    o.append(T(fx(Rn) - 4, fy(118), sb('R', 'n') + '= 65.48', 13, 'end', NX, True))
    o.append(L(fx(R), fy(110), fx(R), fy(-55), LV, 1.5, '4 3'))
    o.append(T(fx(R) + 4, fy(118), 'R = 70', 13, 'start', LV, True))
    return 370, ''.join(o)


FIG[9] = (f9, 'Resultant stress across the crane-hook section of the first worked example (direct stress included). The curved-beam stress (solid) is a hyperbola that peaks at 120.8 MPa on the inner fibre; the straight-beam line (dashed) gives only 88.9 MPa there. The neutral axis of bending, at 65.48 mm, sits 4.52 mm inside the centroid.',
          'Plot of stress against radius from 40 to 100 mm. Curved-beam curve from 120.8 MPa at the inner fibre down to minus 48.3 at the outer; straight-beam dashed line from 88.9 to minus 66.7. Vertical marks at the neutral-axis radius 65.48 and the centroid 70.')


spec = make_spec(FIG)
