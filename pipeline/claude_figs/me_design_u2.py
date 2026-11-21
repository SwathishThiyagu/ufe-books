"""Claude's hand-drawn figures for me-design-u2 (Machine Design: failure theories and fatigue design), one per chapter,
drawn from each chapter's own worked example and numbers. Colours are the shell's CSS variables."""
import os, sys, math, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

_T, _Tb, _boxt = T, Tb, boxt


def _sub(s):
    """S_ut, sigma_a ... drawn as real subscripts, never as underscores"""
    return re.sub(r'([A-Za-zα-ωδ])_([A-Za-z0-9,]+)', r'\1<tspan baseline-shift="sub" font-size="11">\2</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)
def boxt(x, y, w, h, lines, *a, **k): return _boxt(x, y, w, h, [_sub(l) for l in lines], *a, **k)


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


def fmt(v):
    return neg(f'{v:g}')


def poly(pts, c, w=2.5, dash=None, fill='none'):
    d = f';stroke-dasharray:{dash}' if dash else ''
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" style="fill:{fill};stroke:{c};stroke-width:{w}{d};stroke-linejoin:round"/>'


# ---- 2.1 Tresca hexagon and von Mises ellipse, S_yt = 400 MPa, worked example point (137.1, 2.9) ----
def f1():
    o = []
    S = 400.0
    cx, cy, sc = 250, 250, 0.40          # origin of the sigma1-sigma2 plane, px per MPa
    X = lambda a: cx + a * sc
    Y = lambda b: cy - b * sc
    # von Mises ellipse
    pts = []
    for i in range(121):
        t = 2 * math.pi * i / 120
        u, v = math.sqrt(2) * S * math.cos(t), math.sqrt(2 / 3) * S * math.sin(t)
        pts.append((X((u + v) / math.sqrt(2)), Y((u - v) / math.sqrt(2))))
    o.append(P(pts, LV, 2.5))
    # Tresca hexagon
    hexa = [(S, 0), (S, S), (0, S), (-S, 0), (-S, -S), (0, -S)]
    o.append(poly([(X(a), Y(b)) for a, b in hexa], AC, 2.5, fill=ACS))
    # axes (drawn over the shaded regions)
    o.append(L(X(-560), Y(0), X(560), Y(0), L2, 1.5, arrow='m'))
    o.append(L(X(0), Y(-560), X(0), Y(560), L2, 1.5, arrow='m'))
    o.append(T(X(560) + 8, Y(0) + 5, 'σ_1 (MPa)', 14, 'start', MUT))
    o.append(T(X(0) + 10, Y(560) + 6, 'σ_2 (MPa)', 14, 'start', MUT))
    for v in (-400, 400):
        o.append(L(X(v), Y(0) - 5, X(v), Y(0) + 5, INK, 1.5)); o.append(Tb(X(v) + (-22 if v < 0 else 24), Y(0) + 20, fmt(int(v)), 13, 'middle', MUT))
        o.append(L(X(0) - 5, Y(v), X(0) + 5, Y(v), INK, 1.5)); o.append(Tb(X(0) - 12, Y(v) + (-8 if v > 0 else 18), fmt(int(v)), 13, 'end', MUT))
    # pure shear line and its two yield points
    o.append(L(X(-300), Y(300), X(300), Y(-300), NX, 1.6, dash='6 5'))
    o.append(C(X(200), Y(-200), 5, AC)); o.append(C(X(230.9), Y(-230.9), 5, LV))
    # worked example point and its load line
    s1, s2 = 137.08, 2.92
    o.append(L(X(0), Y(0), X(404.3), Y(404.3 * s2 / s1), INK, 1.6))
    o.append(C(X(s1), Y(s2), 6, NX))
    o.append(Tb(X(s1) + 4, Y(s2) - 14, 'A (137.1, 2.9)', 14, 'start', NX, bold=True))
    # legend and notes, right side
    lx = 500
    o.append(L(lx, 64, lx + 34, 64, AC, 3)); o.append(T(lx + 42, 69, 'Tresca hexagon', 14, 'start'))
    o.append(L(lx, 92, lx + 34, 92, LV, 3)); o.append(T(lx + 42, 97, 'von Mises ellipse', 14, 'start'))
    o.append(T(lx, 132, 'Boundary for S_yt = 400 MPa,', 13, 'start', MUT))
    o.append(T(lx, 150, 'plane stress (σ_3 = 0)', 13, 'start', MUT))
    o.append(T(lx, 300, 'Point A, scaled out', 14, 'start', NX, bold=True))
    o.append(T(lx, 320, 'to the boundary:', 14, 'start', NX))
    o.append(T(lx, 342, 'n = 2.92 (Tresca)', 14, 'start'))
    o.append(T(lx, 362, 'n = 2.95 (von Mises)', 14, 'start'))
    o.append(T(lx, 420, 'Pure shear (dashed):', 14, 'start', NX, bold=True))
    o.append(T(lx, 440, 'Tresca τ = 200 MPa', 14, 'start'))
    o.append(T(lx, 460, 'von Mises τ = 231 MPa', 14, 'start'))
    return 500, ''.join(o)


# ---- 2.2 stepped shaft d = 40, D = 50, r = 4 under M = 300 N m, surface stress along the shaft ----
def f2():
    o = []
    # shaft drawn to scale 3 px per mm, axis at y = 120
    ya, s = 128, 3.0
    xs, xf, xe = 70, 300, 650           # left end, shoulder face, right end
    r = 4 * s
    top_big, top_small = ya - 25 * s, ya - 20 * s
    bot_big, bot_small = ya + 25 * s, ya + 20 * s
    path = (f'M{xs},{top_big} L{xf},{top_big} L{xf},{top_small - r} Q{xf},{top_small} {xf + r},{top_small} L{xe},{top_small} '
            f'L{xe},{bot_small} L{xf + r},{bot_small} Q{xf},{bot_small} {xf},{bot_small + r} L{xf},{bot_big} L{xs},{bot_big} Z')
    o.append(f'<path d="{path}" style="fill:var(--panel);stroke:var(--accent);stroke-width:2.2"/>')
    o.append(L(xs - 10, ya, xe + 10, ya, L2, 1.2, dash='10 4 2 4'))
    o.append(T(185, ya + 5, 'D = 50 mm', 14, bold=True))
    o.append(T(475, ya + 5, 'd = 40 mm', 14, bold=True))
    o.append(L(xf + r + 2, top_small - 2, xf + 46, top_small - 34, NX, 1.6))
    o.append(Tb(xf + 50, top_small - 38, 'fillet r = 4 mm (r/d = 0.10)', 14, 'start', NX, bold=True))
    o.append(T(xs + 6, bot_big + 24, 'M = 300 N·m bends the shaft', 13, 'start', MUT))
    o.append(T(xe, bot_big + 24, 'D/d = 1.25 → K_t = 1.6', 13, 'end', MUT))
    # stress along the top surface
    x0, x1, y0, y1 = 70, 650, 296, 480
    fy = lin(0, 100, y1, y0)
    o.append(L(x0, y1, x1, y1, L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    for v in (0, 25, 50, 75, 100):
        o.append(L(x0 - 5, fy(v), x0, fy(v), L2, 1.5)); o.append(T(x0 - 9, fy(v) + 4.5, str(v), 13, 'end', MUT))
        o.append(L(x0, fy(v), x1, fy(v), LN, 1))
    o.append(T(x0, y0 - 12, 'surface bending stress (MPa)', 14, 'start', MUT))
    o.append(T((x0 + x1) / 2, y1 + 24, 'position along the shaft (the shoulder is at the dashed line)', 13, fill=MUT))
    o.append(L(xf, y0 - 2, xf, y1, L2, 1.4, dash='5 4'))
    # stress curve: 24.4 in the big section, peak 76.4 just past the fillet, settles to 47.75
    pts = [(x0, fy(24.4)), (xf - 30, fy(24.4))]
    for i in range(0, 41):
        x = xf - 30 + i * 3
        if x < xf + r:
            v = 24.4 + (76.39 - 24.4) * math.exp(-((x - (xf + r)) / 14.0) ** 2)
        else:
            v = 47.75 + (76.39 - 47.75) * math.exp(-((x - (xf + r)) / 22.0) ** 2)
        pts.append((x, fy(v)))
    pts += [(x1, fy(47.75))]
    o.append(P(pts, AC, 2.6))
    o.append(L(xf + 40, fy(71.82), x1, fy(71.82), NX, 2, dash='7 5'))
    o.append(C(xf + r, fy(76.39), 5, LV))
    o.append(L(xf + r + 4, fy(76.39) - 4, xf + 40, fy(93) + 4, LV, 1.4))
    o.append(Tb(xf + 44, fy(93), 'peak K_t σ_nom = 1.6 × 47.75 = 76.4', 14, 'start', LV, bold=True))
    o.append(Tb(x1 - 4, fy(71.82) + 18, 'fatigue check: K_f σ_nom = 71.8', 13, 'end', NX))
    o.append(Tb(x1 - 4, fy(47.75) + 20, 'nominal σ_nom = 32M/(πd³) = 47.75', 13, 'end'))
    o.append(Tb(x0 + 10, fy(24.4) - 10, 'large section 24.4', 13, 'start', MUT))
    return 520, ''.join(o)


# ---- 2.3 S-N line on log-log axes: (10^3, 540) to (10^6, 230), then flat; worked examples 1 and 2 ----
def f3():
    o = []
    x0, x1, y0, y1 = 96, 690, 40, 330
    fx = lin(3, 8, x0, x1)
    fy = lin(math.log10(180), math.log10(620), y1, y0)
    Y = lambda S: fy(math.log10(S))
    o.append(L(x0, y1, x1, y1, L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    for e in range(3, 9):
        o.append(L(fx(e), y1, fx(e), y1 + 5, L2, 1.5)); o.append(T(fx(e), y1 + 22, f'10<tspan baseline-shift="super" font-size="10">{e}</tspan>', 13, fill=MUT))
    for v in (200, 300, 400, 500, 600):
        o.append(L(x0 - 5, Y(v), x0, Y(v), L2, 1.5)); o.append(T(x0 - 9, Y(v) + 4.5, str(v), 13, 'end', MUT))
        o.append(L(x0, Y(v), x1, Y(v), LN, 1))
    o.append(T((x0 + x1) / 2, y1 + 44, 'cycles to failure N (log scale)', 14, fill=MUT))
    o.append(T(x0, y0 - 14, 'stress amplitude S (MPa, log scale)', 14, 'start', MUT))
    b = math.log10(230 / 540) / 3
    o.append(L(fx(3), Y(540), fx(6), Y(230), AC, 3))
    o.append(L(fx(6), Y(230), fx(8), Y(230), AC, 3))
    o.append(C(fx(3), Y(540), 6, AC)); o.append(C(fx(6), Y(230), 6, AC))
    o.append(Tb(fx(3) + 14, Y(540) - 8, '0.9 S_ut = 540 MPa at 10³', 14, 'start', AC, bold=True))
    o.append(Tb(fx(6) + 10, Y(230) - 14, 'knee: S_e = 230 MPa at 10⁶', 14, 'start', AC, bold=True))
    o.append(Tb(fx(7.0), Y(230) + 24, 'no failure below S_e', 13, 'middle', MUT))
    for S, col, lab in ((300, NX, '300 MPa → 1.16 × 10⁵ cycles'), (260, LV, '260 MPa → 3.71 × 10⁵ cycles')):
        lg = 3 + math.log10(S / 540) / b
        o.append(L(x0, Y(S), fx(lg), Y(S), col, 1.8, dash='6 4'))
        o.append(L(fx(lg), Y(S), fx(lg), y1, col, 1.8, dash='6 4'))
        o.append(C(fx(lg), Y(S), 5, col))
        o.append(Tb(x0 + 8, Y(S) + (-8 if S == 300 else 18), lab, 13, 'start', col, bold=True))
    o.append(T(fx(6.9), Y(420), 'sloping part: b = −0.1236 per decade', 13, 'middle', MUT))
    o.append(T(fx(6.9), Y(420) + 18, '(finite life, 10³ to 10⁶ cycles)', 13, 'middle', MUT))
    return 384, ''.join(o)


# ---- 2.4 Haigh diagram: S_e = 230, S_yt = 400, S_ut = 600; working point (80, 40) ----
def f4():
    o = []
    x0, x1, y0, y1 = 80, 690, 40, 380
    fx = lin(0, 640, x0, x1); fy = lin(0, 420, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0, 100, 200, 300, 400, 500, 600], [0, 100, 200, 300, 400], fx, fy,
                  'mean stress σ_m (MPa)', 'alternating stress σ_a (MPa)', lambda v: {400: _sub('400 = S_yt'), 600: _sub('600 = S_ut')}.get(v, fmt(v)), fmt).replace('σ_m', 'σ<tspan baseline-shift="sub" font-size="11">m</tspan>').replace('σ_a', 'σ<tspan baseline-shift="sub" font-size="11">a</tspan>'))
    Se, Syt, Sut = 230, 400, 600
    o.append(L(fx(0), fy(Syt), fx(Syt), fy(0), MUT, 2, dash='3 4'))                 # Langer
    o.append(L(fx(0), fy(Se), fx(Syt), fy(0), NX, 2.5))                              # Soderberg
    o.append(L(fx(0), fy(Se), fx(Sut), fy(0), AC, 2.5))                              # Goodman
    o.append(P([(fx(m), fy(Se * (1 - (m / Sut) ** 2))) for m in range(0, 601, 15)], LV, 2.5))  # Gerber
    # labels on the lines
    o.append(Tb(fx(112), fy(318), 'Langer (yield): σ_a + σ_m = 400', 13, 'start', MUT))
    o.append(Tb(fx(538), fy(118), 'Gerber', 14, 'start', LV, bold=True))
    o.append(Tb(fx(470), fy(28), 'Goodman', 14, 'middle', AC, bold=True))
    o.append(Tb(fx(250), fy(60), 'Soderberg', 14, 'middle', NX, bold=True))
    o.append(T(fx(0) + 8, fy(Se) - 8, 'S_e = 230', 13, 'start', INK, bold=True))
    # working point and load line
    o.append(L(fx(0), fy(0), fx(330), fy(165), INK, 1.4, dash='5 4'))
    o.append(C(fx(80), fy(40), 6, INK))
    o.append(Tb(fx(80) + 10, fy(40) + 20, 'working point (80, 40)', 13, 'start', INK, bold=True))
    for m, a, col in ((213.95, 106.98, NX), (260.38, 130.19, AC), (266.67, 133.33, MUT)):
        o.append(C(fx(m), fy(a), 5, col))
    o.append(T(fx(395), fy(392), 'along the dashed line:', 13, 'start', INK))
    o.append(T(fx(395), fy(370), 'Soderberg n = 2.67', 13, 'start', NX, bold=True))
    o.append(T(fx(395), fy(350), 'Goodman n = 3.25', 13, 'start', AC, bold=True))
    o.append(T(fx(395), fy(330), 'yield n = 3.33 (caps Gerber 4.06)', 13, 'start', MUT, bold=True))
    return 440, ''.join(o)


# ---- 2.5 the dropped weight of the worked examples and the stresses it causes ----
def f5():
    o = []
    # left: ceiling, rod, collar, weight ring above the collar
    o.append(R(30, 20, 150, 14, FIGBG, L2, 2))
    for i in range(8): o.append(L(36 + i * 18, 20, 48 + i * 18, 8, L2, 1.4))
    o.append(R(100, 34, 10, 300, PANEL, AC, 1))
    o.append(R(80, 334, 50, 14, ACS, AC, 3))
    o.append(T(126, 364, 'collar', 13, 'start', MUT))
    o.append(R(72, 210, 66, 40, NXS, NX, 6))
    o.append(T(105, 235, 'W', 15, 'middle', NX, bold=True))
    o.append(L(150, 250, 150, 332, INK, 1.6, arrow='l')); o.append(L(150, 300, 150, 252, INK, 1.6, arrow='l'))
    o.append(T(158, 296, 'h = 50 mm', 13, 'start'))
    o.append(T(120, 110, 'steel rod', 13, 'start', MUT))
    o.append(T(120, 128, 'd = 20, L = 1000 mm', 13, 'start', MUT))
    o.append(T(20, 392, 'W = 500 N, E = 200 GPa', 13, 'start', MUT))
    # right: horizontal bars to scale, 0 to 200 MPa
    x0, x1 = 330, 690
    fx = lin(0, 200, x0, x1)
    rows = [('hung slowly', 1.59, '1.59', LN), ('applied suddenly', 3.18, '3.18 (× 2)', LN),
            ('dropped 50 mm', 180.0, '180 (× 113)', NX), ('dropped on a 2000 N/mm spring', 32.97, '33.0 (× 20.7)', LV)]
    soft = {NX: NXS, LV: LVS}
    o.append(T(x0, 30, 'maximum stress in the rod (MPa)', 14, 'start', MUT))
    for i, (lab, v, txt, col) in enumerate(rows):
        y = 60 + i * 78
        o.append(T(x0, y, lab, 14, 'start', INK, bold=True))
        w = max(3, fx(v) - x0)
        o.append(R(x0, y + 10, w, 26, soft.get(col, FIGBG), col if col != LN else L2, 3))
        tx = x0 + w + 8 if w < 250 else x0 + w - 8
        o.append(T(tx, y + 29, txt, 14, 'start' if w < 250 else 'end', INK, bold=True))
    for v in (0, 50, 100, 150, 200):
        o.append(L(fx(v), 362, fx(v), 368, L2, 1.5)); o.append(T(fx(v), 384, str(v), 13, fill=MUT))
    o.append(L(x0, 362, x1, 362, L2, 1.5))
    return 400, ''.join(o)


FIG = {
    1: (f1, 'Safe regions in plane stress for S<sub>yt</sub> = 400 MPa. Point A of the worked example can be scaled out 2.92 times before it reaches the Tresca hexagon and 2.95 times before the von Mises ellipse; the two differ most in pure shear.',
        'Tresca hexagon inside the von Mises ellipse on sigma-one sigma-two axes, with the worked example point at 137.1 and 2.9 MPa and its line to the boundary.'),
    2: (f2, 'The stepped shaft of the worked example and the bending stress along its surface. The stress jumps from 24.4 MPa in the large section to a peak of 76.4 MPa at the fillet; the fatigue check uses K<sub>f</sub>σ<sub>nom</sub> = 71.8 MPa.',
        'Stepped shaft 50 to 40 millimetres with a 4 millimetre fillet, above a plot of surface stress rising to a peak at the fillet.'),
    3: (f3, 'The S–N line of the worked examples on log scales. It falls from 540 MPa at 10³ cycles to the endurance limit 230 MPa at 10⁶ and stays flat; the dashed lines read off the lives at 300 MPa and 260 MPa.',
        'Log-log S-N line from 540 MPa at a thousand cycles to 230 MPa at a million cycles, flat after, with read-offs at 300 and 260 MPa.'),
    4: (f4, 'The four lines for the worked example\'s steel. The working point (80, 40) is scaled along the dashed line until it meets each line; Gerber lies outside the yield line here, so yield limits it to 3.33.',
        'Mean against alternating stress with Soderberg, Goodman, Gerber and Langer lines, the working point at 80 and 40 MPa and the points where its line meets them.'),
    5: (f5, 'The rod and dropped weight of the worked examples, and the stress in the rod for four ways the same 500 N arrives. A 50 mm drop raises the stress 113 times; a soft spring on the collar cuts it to about 33 MPa.',
        'A vertical rod with a collar and a weight 50 millimetres above it, beside four bars of maximum rod stress: 1.59, 3.18, 180 and 33 MPa.'),
}
spec = make_spec(FIG)


def text_fixes(k):
    return []
