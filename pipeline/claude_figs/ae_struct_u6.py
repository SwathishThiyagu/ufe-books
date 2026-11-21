"""Claude's hand-drawn figures for ae-struct-u6 (plates, buckling, crippling, composites, vibration), one per chapter.
Every number is the matching chapter's worked example, recomputed here. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def arrow(x1, y1, x2, y2, c=AC, w=2.5, kind='n', dash=None):
    return L(x1, y1, x2, y2, c, w, dash, arrow=kind)


def dot(x, y, c, r=5.5):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{c};stroke:var(--fig);stroke-width:2"/>'


def curve(f, x0, x1, fx, fy, c, w=2.5, dash=None, n=120):
    return P([(fx(x0 + (x1 - x0) * i / n), fy(f(x0 + (x1 - x0) * i / n))) for i in range(n + 1)], c, w, dash)


def poly(pts, fill, stroke, sw=1.5, op=None):
    o = f';fill-opacity:{op}' if op is not None else ''
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" style="fill:{fill};stroke:{stroke};stroke-width:{sw}{o}"/>'


# ---- 1: anticlastic strip and the circle of moments ----
def f1():
    E, nu, t = 70e9, 0.3, 0.003
    D = E * t ** 3 / (12 * (1 - nu ** 2))
    kx = 0.05; Mx = D * kx * (1 - nu ** 2)
    o = [T(175, 26, 'Example 1: M_x alone, free in y'.replace('M_x', 'M<tspan baseline-shift="sub" font-size="11">x</tspan>'), 15, bold=True)]
    # along x: sagging arc; across y: hogging arc
    def arcpath(x0, x1, y, sag, c):
        mx = (x0 + x1) / 2
        return f'<path d="M{x0},{y} Q{mx},{y + 2 * sag} {x1},{y}" style="fill:none;stroke:{c};stroke-width:5"/>'
    o.append(T(40, 70, 'along x (side view)', 13, 'start', MUT))
    o.append(arcpath(50, 300, 96, 26, AC))
    o.append(arrow(62, 132, 40, 104, LV, 2.2, 'l')); o.append(arrow(288, 132, 310, 104, LV, 2.2, 'l'))
    o.append(T(175, 150, f'sags: κ<tspan baseline-shift="sub" font-size="11">x</tspan> = +0.05 m⁻¹,  M<tspan baseline-shift="sub" font-size="11">x</tspan> = {Mx:.2f} N·m/m', 13, fill=AC, bold=True))
    o.append(T(40, 196, 'across y (end view)', 13, 'start', MUT))
    o.append(arcpath(90, 260, 236, -8, NX))
    o.append(T(175, 262, f'hogs: κ<tspan baseline-shift="sub" font-size="11">y</tspan> = −νκ<tspan baseline-shift="sub" font-size="11">x</tspan> = −0.015 m⁻¹,  M<tspan baseline-shift="sub" font-size="11">y</tspan> = 0', 13, fill=NX, bold=True))
    o.append(T(175, 300, 'opposite curvatures: an anticlastic saddle', 13, fill=MUT))
    o.append(T(175, 320, f'D = {D:.1f} N·m, σ = 6M<tspan baseline-shift="sub" font-size="11">x</tspan>/t² = {6*Mx/t**2/1e6:.2f} MPa', 13, fill=MUT))
    # right: circle of moments for example 2
    Mxx, Myy, Mxy = 10.0, 4.0, 4.0
    cM, rM = 7.0, 5.0
    s = 22; X0, Y0 = 400, 175
    fx = lambda v: X0 + v * s; fy = lambda v: Y0 - v * s
    o.append(T(545, 26, 'Example 2: principal moments (N·m/m)', 15, bold=True))
    o.append(T(fx(13.5), Y0 + 40, 'M', 13, 'end', MUT))
    o.append(L(fx(-0.5), Y0, fx(13.5), Y0, L2, 1.5)); o.append(L(X0, fy(6.5), X0, fy(-6.5), L2, 1.5))
    o.append(T(X0 + 6, fy(6.3), 'M<tspan baseline-shift="sub" font-size="11">xy</tspan>', 13, 'start', MUT))
    for v in (2, 7, 12):
        o.append(L(fx(v), Y0, fx(v), Y0 + 5, L2, 1.5))
    o.append(f'<circle cx="{fx(cM):.1f}" cy="{Y0}" r="{rM * s:.1f}" style="fill:var(--accent-soft);fill-opacity:0.5;stroke:var(--accent);stroke-width:2.5"/>')
    o.append(L(fx(Mxx), fy(Mxy), fx(Myy), fy(-Mxy), INK, 1.8))
    o.append(L(fx(cM), Y0, fx(cM + rM), Y0, LV, 3))
    o.append(dot(fx(Mxx), fy(Mxy), INK)); o.append(dot(fx(Myy), fy(-Mxy), INK))
    o.append(Tb(fx(Mxx) + 8, fy(Mxy) - 8, '(10, 4)', 13, 'start', INK, True)); o.append(Tb(fx(Myy) - 8, fy(-Mxy) + 18, '(4, −4)', 13, 'end', INK, True))
    o.append(dot(fx(12), Y0, LV)); o.append(dot(fx(2), Y0, NX))
    o.append(Tb(fx(12) + 10, Y0 + 20, 'M₁ = 12', 13, 'start', LV, True)); o.append(Tb(fx(2) - 8, Y0 + 20, 'M₂ = 2', 13, 'end', NX, True))
    o.append(dot(fx(cM), Y0, AC, 4)); o.append(T(fx(cM), Y0 + 20, 'centre 7', 12, fill=AC))
    o.append(T(fx(cM) + 44, Y0 - 12, '2α = 53.1°', 13, 'start', LV, True))
    o.append(T(545, 320, 'radius √(3² + 4²) = 5;  α = 26.6° from x to M₁', 13, fill=MUT))
    return 340, ''.join(o)

FIG[1] = (f1, 'Left: M<sub>x</sub> alone makes the 3 mm plate sag along x and hog across y, a saddle. Right: the second example\'s moments lie on a circle of centre 7 and radius 5, so M₁ = 12 and M₂ = 2 N·m/m.',
          'Left: a side view of a plate strip bent into a sagging arc along x, with end moment arrows, labelled curvature plus 0.05 per metre and M x 7.88 newton metres per metre; below it an end view curving the other way, hogging, with curvature minus 0.015 per metre and M y zero. Right: a circle of moments on axes M and M x y, centre 7 and radius 5, through the points (10, 4) and (4, minus 4); it cuts the M axis at the principal moments 12 and 2, with the angle 2 alpha of 53.1 degrees marked.')


# ---- 2: centre-line deflection with and without in-plane load ----
def f2():
    a = b = 0.8; t = 0.004; D = 70e9 * t ** 3 / (12 * 0.91); q = 1000.0; N = 10000.0
    def w(x, Nc):
        s = 0.0
        for m in range(1, 41, 2):
            for n in range(1, 41, 2):
                A = 16 * q / (math.pi ** 6 * D * m * n * (m * m / a ** 2 + n * n / b ** 2) ** 2)
                Nmn = D * math.pi ** 2 * (m * m / a ** 2 + n * n / b ** 2) ** 2 / (m / a) ** 2
                s += A / (1 - Nc / Nmn) * math.sin(m * math.pi * x / a) * math.sin(n * math.pi / 2)
        return s * 1e3
    x0, x1, y0, y1 = 90, 560, 60, 290
    fx = lambda v: x0 + (x1 - x0) * v / 800; fy = lambda v: y0 + (y1 - y0) * v / 8
    o = [T(330, 26, 'Deflection along the centre line, q = 1 kPa, 800 × 800 × 4 mm plate', 15, bold=True)]
    o.append(L(x0, y0, x1, y0, L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    for v in (0, 200, 400, 600, 800):
        o.append(L(fx(v), y0, fx(v), y0 - 5, L2, 1.5)); o.append(T(fx(v), y0 - 10, str(v), 12, fill=MUT))
    for v in (2, 4, 6, 8):
        o.append(L(x0, fy(v), x1, fy(v), 'var(--line)', 1)); o.append(T(x0 - 8, fy(v) + 4, str(v), 12, 'end', MUT))
    o.append(T(x0 - 8, y0 + 4, '0', 12, 'end', MUT))
    o.append(T(x1 + 4, y0 + 4, 'x (mm)', 13, 'start', MUT)); o.append(T(x0 - 12, y1 + 24, 'w (mm, downward)', 13, 'start', MUT))
    cases = [(-N, NX, '10 kN/m tension'), (0.0, AC, 'no in-plane load'), (N, LV, '10 kN/m compression')]
    for Nc, c, lab in cases:
        pts = [(fx(800 * i / 60), fy(w(0.8 * i / 60, Nc))) for i in range(61)]
        o.append(P(pts, c, 3))
        wc = w(0.4, Nc)
        o.append(dot(fx(400), fy(wc), c))
        o.append(Tb(x1 + 10, fy(wc) + 5, f'{wc:.2f} mm', 13, 'start', c, True))
        o.append(T(x1 + 10, fy(wc) + 22, lab, 12, 'start', c))
    o.append(T(330, 344, 'compression magnifies the bulge by 1.67; tension reduces it by 29%', 13, fill=MUT))
    return 356, ''.join(o)

FIG[2] = (f2, 'The worked example\'s square plate under 1 kPa, deflection along its centre line from the Navier series. With no in-plane load the centre deflects 4.06 mm; 10 kN/m of compression (N<sub>x</sub>/N<sub>cr</sub> = 0.395) raises it to 6.76 mm, and 10 kN/m of tension lowers it to 2.89 mm.',
          'A graph of deflection w in millimetres, drawn downward, against x from 0 to 800 millimetres along the centre line of the plate. Three sine-like curves start and end at zero. The middle one, with no in-plane load, reaches 4.06 millimetres at the centre. The deepest, with 10 kilonewtons per metre compression, reaches 6.76 millimetres. The shallowest, with 10 kilonewtons per metre tension, reaches 2.89 millimetres.')


# ---- 3: buckling coefficient against aspect ratio ----
def f3():
    kf = lambda m, r: (m / r + r / m) ** 2
    x0, x1, y0, y1 = 80, 640, 50, 290
    rmin, rmax, kmin, kmax = 0.4, 4.0, 3.5, 8.0
    fx = lambda v: x0 + (x1 - x0) * (v - rmin) / (rmax - rmin); fy = lambda v: y1 - (y1 - y0) * (v - kmin) / (kmax - kmin)
    o = [T(360, 24, 'Simply supported plate in compression: k = (m/r + r/m)², r = a/b', 15, bold=True)]
    o.append(axes(x0, x1, y0, y1, [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4], [4, 5, 6, 7, 8], fx, fy, 'aspect ratio a/b', 'k', lambda v: f'{v:g}', lambda v: f'{v:g}'))
    cols = {1: AC, 2: NX, 3: LV}
    for m in (1, 2, 3):
        lo = max(rmin, m / (kmax ** 0.5 + 0.0) * 0 + 0.35 * m)
        def f(r, m=m): return min(kf(m, r), kmax)
        pts = []
        for i in range(241):
            r = rmin + (rmax - rmin) * i / 240
            v = kf(m, r)
            if v <= kmax: pts.append((fx(r), fy(v)))
        o.append(P(pts, cols[m], 2, '6 4'))
        lab_r = {1: 2.1, 2: 3.3, 3: 1.55}[m]
        o.append(Tb(fx(lab_r), fy(kf(m, lab_r)) - 8, f'm = {m}', 13, 'middle', cols[m], True))
    env = [(fx(rmin + (rmax - rmin) * i / 360), fy(min(kf(m, rmin + (rmax - rmin) * i / 360) for m in range(1, 6)))) for i in range(361)]
    o.append(P(env, INK, 3.5))
    for r in (2 ** 0.5, 6 ** 0.5):
        o.append(L(fx(r), fy(4), fx(r), fy(kf(1 if r < 2 else 2, r)), L2, 1.2, '3 3'))
    o.append(dot(fx(2), fy(4), LV)); o.append(Tb(fx(2.05), fy(3.72), 'a/b = 2: k = 4.00, m = 2', 13, 'start', LV, True))
    o.append(dot(fx(1.5), fy(kf(2, 1.5)), AC)); o.append(Tb(fx(1.45), fy(3.72), 'a/b = 1.5: k = 4.34', 13, 'end', AC, True))
    o.append(L(fx(rmin), fy(4), fx(rmax), fy(4), MUT, 1.2, '2 4'))
    return 345, ''.join(o)

FIG[3] = (f3, 'Buckling coefficient k against aspect ratio for a plate simply supported on all edges in uniaxial compression. Each dashed curve is one number of half-waves m; the plate follows the lowest (solid line), changing mode at a/b = 1.41 and 2.45. The first worked example (a/b = 2) sits on a minimum, k = 4.00 with m = 2; the second (a/b = 1.5) has k = 4.34.',
          'A graph of k from 3.5 to 8 against a over b from 0.4 to 4. Three dashed U-shaped curves for m equal to 1, 2 and 3 each dip to 4 at a over b equal to m. A solid scalloped line follows the lowest of them, touching 4 at 1, 2 and 3 and peaking slightly where the curves cross at 1.41 and 2.45. A point marks a over b of 2 with k of 4.00, and another marks 1.5 with k of 4.34. A dotted line at k equal to 4 marks the long-plate limit.')


# ---- 4: stress across buckled bays and the effective width ----
def f4():
    E, t, p = 70000.0, 1.5, 150.0
    scr = math.pi ** 2 / (12 * 0.91) * 4 * E * (t / p) ** 2
    ss = 100.0; be = 1.90 * t * math.sqrt(E / ss)
    x0, x1 = 60, 660; fx = lambda v: x0 + (x1 - x0) * v / 450
    yb, ys = 290, 1.9
    fy = lambda s: yb - s * ys
    o = [T(360, 24, 'Stringer stress 100 MPa, pitch 150 mm, skin 1.5 mm', 15, bold=True)]
    # real distribution: cosine dip between stringers, edges 100, mid-bay low
    pts = []
    for i in range(361):
        x = 450 * i / 360; u = (x % 150) / 150
        mid = 2 * scr - (100 - 2 * scr) * 0  # mid-bay stress level shown near the buckling stress
        s = scr + (ss - scr) * (0.5 + 0.5 * math.cos(2 * math.pi * u)) ** 2.2
        pts.append((fx(x), fy(s)))
    area = [(fx(0), fy(0))] + pts + [(fx(450), fy(0))]
    o.append(poly(area, LVS, LV, 1.5, 0.55))
    # effective strips
    for xs in (0, 150, 300, 450):
        for x_a, x_b in ((xs - be / 2, xs), (xs, xs + be / 2)):
            x_a, x_b = max(0, x_a), min(450, x_b)
            if x_b > x_a:
                o.append(f'<rect x="{fx(x_a):.1f}" y="{fy(ss):.1f}" width="{fx(x_b) - fx(x_a):.1f}" height="{ss * ys:.1f}" style="fill:var(--accent-soft);fill-opacity:0.7;stroke:var(--accent);stroke-width:2"/>')
    o.append(L(fx(0), fy(0), fx(450), fy(0), INK, 5))
    for xs in (0, 150, 300, 450):
        o.append(f'<rect x="{fx(xs) - 9:.1f}" y="{fy(0) - 2:.1f}" width="18" height="20" style="fill:var(--next);stroke:var(--next)"/>')
    o.append(T(fx(150), yb + 36, 'stringers (200 mm² each)', 13, fill=NX, bold=True))
    o.append(L(fx(0), fy(ss), fx(450), fy(ss), L2, 1.2, '5 4')); o.append(T(fx(450) + 4, fy(ss) + 4, '100', 12, 'start', MUT))
    o.append(L(fx(0), fy(scr), fx(450), fy(scr), L2, 1.2, '5 4')); o.append(T(fx(450) + 4, fy(scr) + 4, f'{scr:.1f}', 12, 'start', MUT))
    o.append(Tb(fx(225), fy(scr) - 8, f'σ_cr of a bay = {scr:.1f} MPa'.replace('σ_cr', 'σ<tspan baseline-shift="sub" font-size="11">cr</tspan>'), 13, 'middle', MUT))
    o.append(brace(fx(150 - be / 2), fx(150 + be / 2), fy(ss) - 12, AC, True))
    o.append(Tb(fx(150), fy(ss) - 22, f'b<tspan baseline-shift="sub" font-size="11">e</tspan> = {be:.1f} mm ({be / 2:.1f} each side)', 13, 'middle', AC, True))
    o.append(Tb(fx(375), fy(ss * 0.62), 'real skin stress', 13, 'middle', LV, True))
    o.append(brace(fx(300), fx(450), yb + 52, MUT))
    o.append(T(fx(375), yb + 74, 'pitch p = 150 mm', 13, fill=MUT))
    o.append(T(fx(60), yb + 74, f'A<tspan baseline-shift="sub" font-size="11">e</tspan> = 200 + {be:.1f} × 1.5 = {200 + be * t:.1f} mm²', 13, 'start', AC, True))
    return 380, ''.join(o)

FIG[4] = (f4, 'The worked panel at a stringer stress of 100 MPa. The real skin stress (shaded curve) stays at 100 MPa at each stringer and falls towards the bay buckling stress of 25.3 MPa at mid-bay. Von Kármán\'s effective width replaces it by strips totalling b<sub>e</sub> = 75.4 mm per stringer, 37.7 mm each side, at the full 100 MPa, so A<sub>e</sub> = 313.1 mm².',
          'A row of four stringers 150 millimetres apart under a skin line. Above the skin, a shaded curve of skin stress rises to 100 megapascals at each stringer and dips at mid-bay towards a dashed line at 25.3 megapascals, the buckling stress of a bay. Rectangles centred on each stringer, 75.4 millimetres wide in total and 100 megapascals high, show the effective width. Labels give b e of 75.4 millimetres, 37.7 each side, and the effective area of 313.1 square millimetres.')


# ---- 5: crippling stress against b'/t for an angle ----
def f5():
    E, nu, scy = 72000.0, 0.33, 300.0
    pl = math.pi ** 2 * E / (12 * (1 - nu ** 2)); rt = math.sqrt(scy * E)
    need = lambda r: min(scy, 0.316 * rt / r ** 0.75)
    ger = lambda r: min(scy, 0.56 * scy * ((1 / r) * math.sqrt(E / scy)) ** 0.85)
    el = lambda r: 0.425 * pl / r ** 2
    x0, x1, y0, y1 = 80, 560, 50, 290
    fx = lambda v: x0 + (x1 - x0) * (v - 5) / 35; fy = lambda v: y1 - (y1 - y0) * v / 350
    o = [T(330, 24, 'Equal angle, E = 72 GPa, σ<tspan baseline-shift="sub" font-size="11">cy</tspan> = 300 MPa', 15, bold=True)]
    o.append(axes(x0, x1, y0, y1, [5, 10, 15, 20, 25, 30, 35, 40], [0, 50, 100, 150, 200, 250, 300, 350], fx, fy, "b′/t", 'stress (MPa)', str, str))
    o.append(L(fx(5), fy(scy), fx(40), fy(scy), INK, 2, '7 4')); o.append(T(fx(40) - 4, fy(scy) - 13, 'cut-off σ<tspan baseline-shift="sub" font-size="11">cs</tspan> = σ<tspan baseline-shift="sub" font-size="11">cy</tspan>', 12, 'end', INK))
    o.append(curve(need, 5, 40, fx, fy, AC, 3))
    o.append(curve(ger, 5, 40, fx, fy, NX, 3))
    pts = [(fx(r), fy(el(r))) for r in [7.5 + 32.5 * i / 100 for i in range(101)] if el(r) <= 350]
    o.append(P(pts, LV, 2.2, '6 4'))
    r = 20
    for f, c, lab, dy in ((need, AC, f'Needham {need(r):.0f}', -10), (ger, NX, f'Gerard {ger(r):.0f}', 22), (el, LV, f'local buckling {el(r):.1f}', 22)):
        o.append(dot(fx(r), fy(f(r)), c))
        o.append(Tb(fx(r) + 10, fy(f(r)) + dy, lab, 13, 'start', c, True))
    o.append(L(fx(20), fy(0), fx(20), fy(need(20)), L2, 1.2, '3 3'))
    # small angle sketch
    ax, ay = 610, 110
    o.append(L(ax, ay, ax, ay + 90, AC, 6)); o.append(L(ax, ay + 90, ax + 90, ay + 90, AC, 6))
    o.append(T(ax - 10, ay + 50, '30', 13, 'end', MUT)); o.append(T(ax + 45, ay + 112, '30', 13, fill=MUT))
    o.append(T(ax + 45, ay + 134, 't = 1.5 mm', 13, fill=MUT)); o.append(T(ax + 45, ay + 154, "b′/t = 20", 13, fill=MUT, bold=True))
    return 345, ''.join(o)

FIG[5] = (f5, 'Crippling stress of an equal angle against b′/t for the worked example\'s alloy. Needham\'s curve (C<sub>e</sub> = 0.316) and Gerard\'s (g = 2) both fall as b′/t rises and are cut off at σ<sub>cy</sub> = 300 MPa. At the example\'s b′/t = 20 they give 155 and 135 MPa, about twice the 70.6 MPa at which each leg buckles locally (dashed).',
          'A graph of stress from 0 to 350 megapascals against b prime over t from 5 to 40. A horizontal dashed line at 300 marks the yield cut-off. Two falling curves, Needham and Gerard, start at the cut-off for stocky angles and fall as the ratio grows; a steeper dashed curve shows elastic local buckling of a leg. At b prime over t of 20 the points read Needham 155, Gerard 135 and local buckling 70.6 megapascals. Beside the graph a sketch of the 30 by 30 by 1.5 millimetre angle.')


# ---- 6: channel column, centroid and shear centre, and the buckling loads ----
def f6():
    h, b, t = 60.0, 30.0, 2.0
    A = t * (h + 2 * b); xb = b * b * t / A; e = 3 * b * b / (h + 6 * b)
    loads = [('P_y (Euler, minor axis)', 24.29, NX), ('P_t (torsion)', 22.90, AC), ('flexural–torsional', 21.72, LV)]
    s = 3.0; X0, Y0 = 150, 70
    o = [T(170, 26, 'Channel 60 × 30 × 2 mm, L = 800 mm', 15, bold=True)]
    Yb = Y0 + h * s; Xf = X0 + b * s; Ym = (Y0 + Yb) / 2
    for (a1, a2), (c1, c2) in (((X0, Y0), (Xf, Y0)), ((X0, Y0), (X0, Yb)), ((X0, Yb), (Xf, Yb))):
        o.append(L(a1, a2, c1, c2, AC, 6))
    o.append(L(X0 - 70, Ym, Xf + 30, Ym, L2, 1.4, '6 5')); o.append(T(Xf + 34, Ym + 4, 'x', 13, 'start', MUT))
    xs, xg = X0 - e * s, X0 + xb * s
    o.append(dot(xs, Ym, LV, 6)); o.append(Tb(xs, Ym - 14, 'S', 14, 'middle', LV, True))
    o.append(dot(xg, Ym, NX, 6)); o.append(Tb(xg + 2, Ym - 14, 'C', 14, 'middle', NX, True))
    yd = Yb + 30
    for xx in (xs, X0, xg): o.append(L(xx, Ym + 10, xx, yd + 6, L2, 1.1))
    o.append(L(xs, yd, xg, yd, INK, 1.5))
    o.append(T((xs + xg) / 2, yd + 20, f'x₀ = {xb:.1f} + {e:.2f} = {xb + e:.2f} mm', 13, fill=INK, bold=True))
    o.append(T(170, yd + 42, 'load through C, twist about S', 13, fill=MUT))
    # bars
    bx0, bx1, by = 380, 660, 80
    fxb = lambda v: bx0 + (bx1 - bx0) * v / 26
    o.append(T(520, 26, 'Buckling loads (kN)', 15, bold=True))
    for i, (lab, v, c) in enumerate(loads):
        yy = by + i * 62
        o.append(R(bx0, yy, fxb(v) - bx0, 26, c, c, 4))
        o.append(T(bx0, yy - 6, lab.replace('P_y', 'P<tspan baseline-shift="sub" font-size="11">y</tspan>').replace('P_t', 'P<tspan baseline-shift="sub" font-size="11">t</tspan>'), 13, 'start', c, True))
        o.append(T(fxb(v) + 6, yy + 18, f'{v:.1f}', 13, 'start', INK, True))
    o.append(T(bx0, by + 3 * 62 + 4, 'P<tspan baseline-shift="sub" font-size="11">x</tspan> = 155.4 kN (off the scale) couples with twist', 13, 'start', MUT))
    o.append(T(bx0, by + 3 * 62 + 24, 'the coupled root lies below both P<tspan baseline-shift="sub" font-size="11">y</tspan> and P<tspan baseline-shift="sub" font-size="11">t</tspan>', 13, 'start', MUT))
    return 350, ''.join(o)

FIG[6] = (f6, 'The first worked example\'s channel column. The centroid C lies 7.5 mm inside the web and the shear centre S 11.25 mm outside it, so x₀ = 18.75 mm. Of the separate modes, minor-axis Euler buckling (24.3 kN) and pure torsion (22.9 kN) are close; the coupled bending and twisting mode governs at 21.7 kN.',
          'Left: a channel 60 by 30 by 2 millimetres with its web vertical and the horizontal axis of symmetry dashed. The centroid C sits 7.5 millimetres to the right of the web, the shear centre S 11.25 millimetres to the left; their separation x nought is 18.75 millimetres. Right: three horizontal bars of buckling load: Euler about the minor axis 24.3 kilonewtons, pure torsion 22.9, and flexural-torsional 21.7, the shortest. A note says the major-axis Euler load is 155.4 kilonewtons.')


# ---- 7: rotated ply stiffness against angle ----
def f7():
    E1, E2, n12, G = 140.0, 10.0, 0.3, 5.0
    n21 = n12 * E2 / E1; d = 1 - n12 * n21
    Q11, Q22, Q12, Q66 = E1 / d, E2 / d, n12 * E2 / d, G
    def qb(th, key):
        m, n = math.cos(math.radians(th)), math.sin(math.radians(th))
        return {'11': Q11 * m ** 4 + 2 * (Q12 + 2 * Q66) * m * m * n * n + Q22 * n ** 4,
                '66': (Q11 + Q22 - 2 * Q12 - 2 * Q66) * m * m * n * n + Q66 * (m ** 4 + n ** 4),
                '16': (Q11 - Q12 - 2 * Q66) * m ** 3 * n + (Q12 - Q22 + 2 * Q66) * m * n ** 3}[key]
    x0, x1, y0, y1 = 270, 660, 50, 290
    fx = lambda v: x0 + (x1 - x0) * v / 90; fy = lambda v: y1 - (y1 - y0) * v / 150
    o = [T(470, 24, 'Carbon/epoxy ply: Q̄ against fibre angle θ (GPa)', 15, bold=True)]
    o.append(axes(x0, x1, y0, y1, [0, 15, 30, 45, 60, 75, 90], [0, 50, 100, 150], fx, fy, 'θ (degrees)', 'GPa', str, str))
    for key, c, lab, lx in (('11', AC, 'Q̄₁₁', 12), ('66', NX, 'Q̄₆₆', 70), ('16', LV, 'Q̄₁₆', 22)):
        o.append(curve(lambda th, k=key: qb(th, k), 0, 90, fx, fy, c, 3))
        o.append(Tb(fx(lx) + 8, fy(qb(lx, key)) - 10, lab, 14, 'start', c, True))
    for key, c in (('11', AC), ('66', NX), ('16', LV)):
        o.append(dot(fx(45), fy(qb(45, key)), c))
    o.append(Tb(fx(45) + 10, fy(qb(45, '11')) - 16, f'at 45°: {qb(45, "11"):.1f}, {qb(45, "66"):.1f}, {qb(45, "16"):.1f}', 13, 'start', INK, True))
    o.append(T(fx(0) + 6, fy(Q11) - 8, f'{Q11:.1f} at 0°', 12, 'start', AC))
    # ply sketch
    cx, cy, Rr = 125, 175, 80
    o.append(R(cx - Rr, cy - Rr, 2 * Rr, 2 * Rr, PANEL, L2, 4))
    th = math.radians(30)
    for k in range(-5, 6):
        ox, oy = -k * 15 * math.sin(th), -k * 15 * math.cos(th)
        L0 = 200
        xa, ya, xb2, yb2 = cx + ox - L0 * math.cos(th), cy + oy + L0 * math.sin(th), cx + ox + L0 * math.cos(th), cy + oy - L0 * math.sin(th)
        # clip to square
        pts = []
        for i in range(201):
            u = i / 200; X = xa + (xb2 - xa) * u; Y = ya + (yb2 - ya) * u
            if abs(X - cx) <= Rr - 3 and abs(Y - cy) <= Rr - 3: pts.append((X, Y))
        if len(pts) > 2: o.append(P([pts[0], pts[-1]], MUT, 1.3))
    o.append(arrow(cx, cy, cx + 105, cy, INK, 2, 'n')); o.append(T(cx + 108, cy + 18, 'x', 14, 'start', INK, True))
    o.append(arrow(cx, cy, cx + 95 * math.cos(th), cy - 95 * math.sin(th), AC, 2.5, 'n')); o.append(T(cx + 98 * math.cos(th) + 4, cy - 98 * math.sin(th) - 4, '1 (fibres)', 13, 'start', AC, True))
    o.append(T(cx + 48, cy - 10, 'θ', 15, 'start', AC, True))
    o.append(T(cx, cy + Rr + 22, 'fibres at θ to the load axis x', 13, fill=MUT))
    return 348, ''.join(o)

FIG[7] = (f7, 'The rotated stiffness of the worked example\'s carbon/epoxy ply. Q̄<sub>11</sub> falls from 140.9 GPa along the fibres to 44.3 GPa at 45° and 10.1 GPa at 90°; the shear stiffness Q̄<sub>66</sub> peaks at 36.2 GPa at 45°; the coupling term Q̄<sub>16</sub> is zero at 0° and 90° and largest near 30°.',
          'Left: a square ply with fibre lines drawn at 30 degrees to the x axis, the fibre direction 1 marked and the angle theta between them. Right: a graph of stiffness in gigapascals against theta from 0 to 90 degrees. Q bar 1 1 falls from 140.9 at 0 degrees to 10.1 at 90 degrees. Q bar 6 6 rises from 5 to a peak of 36.2 at 45 degrees and falls back. Q bar 1 6 starts and ends at zero and peaks near 30 degrees at about 42. Points at 45 degrees read 44.3, 36.2 and 32.7.')


# ---- 8: the [0/90]s stack and each ply's share of D11 ----
def f8():
    E1, E2, n12 = 140.0, 10.0, 0.3
    n21 = n12 * E2 / E1; d = 1 - n12 * n21; Q11, Q22 = E1 / d, E2 / d
    zs = [-0.25, -0.125, 0, 0.125, 0.25]; ang = [0, 90, 90, 0]
    contrib = [((Q11 if a == 0 else Q22) * (zs[k + 1] ** 3 - zs[k] ** 3) / 3 * 1000) for k, a in enumerate(ang)]
    contA = [((Q11 if a == 0 else Q22) * 0.125 * 1000) for a in ang]
    X0, W, Ytop, H = 70, 230, 70, 60
    o = [T(185, 26, '[0/90]s stack, plies 0.125 mm', 15, bold=True)]
    for k in range(4):
        y = Ytop + (3 - k) * H
        fill = ACS if ang[k] == 0 else NXS; c = AC if ang[k] == 0 else NX
        o.append(R(X0, y, W, H, fill, c, 0))
        if ang[k] == 0:
            for j in range(1, 8): o.append(L(X0 + 8, y + j * H / 8, X0 + W - 8, y + j * H / 8, c, 1))
        else:
            for j in range(1, 15): o.append(L(X0 + j * W / 15, y + 6, X0 + j * W / 15, y + H - 6, c, 1))
        o.append(Tb(X0 + W / 2, y + H / 2 + 5, f'{ang[k]}°', 14, 'middle', c, True))
    for k, z in enumerate(zs):
        y = Ytop + (4 - k) * H
        o.append(L(X0 - 8, y, X0, y, INK, 1.5)); o.append(T(X0 - 12, y + 4, f'{z:+.3f}'.replace('+0.000', '0').replace('-', '−'), 12, 'end', MUT))
    o.append(L(X0 - 30, Ytop + 2 * H, X0 + W + 20, Ytop + 2 * H, LV, 1.8, '6 4'))
    o.append(T(X0 + W + 24, Ytop + 2 * H + 4, 'mid-plane', 12, 'start', LV))
    o.append(T(X0 - 40, Ytop - 10, 'z (mm)', 12, 'start', MUT))
    # bars
    bx0, bx1 = 430, 660; fxb = lambda v: bx0 + (bx1 - bx0) * v / 700
    o.append(T(545, 26, 'Share of D₁₁ (N·mm)', 15, bold=True))
    for k in range(4):
        y = Ytop + (3 - k) * H + 16; c = AC if ang[k] == 0 else NX
        o.append(R(bx0, y, max(3, fxb(contrib[k]) - bx0), 28, c, c, 3))
        o.append(T(max(bx0 + 3, fxb(contrib[k])) + 6, y + 19, f'{contrib[k]:.1f}', 13, 'start', INK, True))
        o.append(L(X0 + W + 4, y + 14, bx0 - 6, y + 14, L2, 1, '2 4'))
    o.append(T(545, Ytop + 4 * H + 30, f'D₁₁ = {sum(contrib):.1f} N·mm: the outer 0° plies give {100 * (contrib[0] + contrib[3]) / sum(contrib):.0f}%', 13, fill=INK, bold=True))
    o.append(T(545, Ytop + 4 * H + 50, f'(their share of A₁₁ is only {100 * (contA[0] + contA[3]) / sum(contA):.0f}%)', 13, fill=MUT))
    return 380, ''.join(o)

FIG[8] = (f8, 'The worked [0/90]<sub>s</sub> laminate. The two outer 0° plies sit between z = ±0.125 and ±0.25 mm and give 1284.3 of the 1297.4 N·mm of D<sub>11</sub> (99%), against 93% of A<sub>11</sub>: bending stiffness is set by the outer plies, because D weights each ply by z².',
          'Left: a stack of four plies 0.125 millimetres thick, the outer two at 0 degrees with fibre lines drawn horizontally, the inner two at 90 degrees with fibre lines drawn vertically, z marked from minus 0.25 to plus 0.25 millimetres and the mid-plane dashed. Right: a bar for each ply showing its share of D 1 1: 642.1 newton millimetres for each outer ply and 6.6 for each inner ply, totalling 1297.4. A note says the outer plies give 99 percent of D 1 1 but only 93 percent of A 1 1.')


# ---- 9: resonance curve for the worked example ----
def f9():
    m, k, c = 500.0, 200e3, 4000.0
    wn = math.sqrt(k / m); z = c / (2 * math.sqrt(k * m)); Xs = 1000 / k * 1e3
    X = lambda r, zz=z: Xs / math.sqrt((1 - r * r) ** 2 + (2 * zz * r) ** 2)
    x0, x1, y0, y1 = 80, 600, 50, 290
    fx = lambda v: x0 + (x1 - x0) * v / 3; fy = lambda v: y1 - (y1 - y0) * v / 14
    o = [T(340, 24, 'Steady amplitude under a 1 kN harmonic force, ω<tspan baseline-shift="sub" font-size="11">n</tspan> = 20 rad/s', 15, bold=True)]
    o.append(axes(x0, x1, y0, y1, [0, 0.5, 1, 1.5, 2, 2.5, 3], [0, 2, 4, 6, 8, 10, 12, 14], fx, fy, 'frequency ratio r = Ω/ω<tspan baseline-shift="sub" font-size="11">n</tspan>', 'X (mm)', lambda v: f'{v:g}', str))
    o.append(curve(lambda r: min(X(r, 0.1), 14), 0, 3, fx, fy, L2, 2, '6 4', 300))
    o.append(curve(X, 0, 3, fx, fy, AC, 3.2, None, 300))
    o.append(dot(fx(1), fy(X(1)), LV)); o.append(Tb(fx(1) + 12, fy(X(1)) - 6, f'{X(1):.1f} mm at r = 1 (ζ = 0.2)', 13, 'start', LV, True))
    o.append(dot(fx(0), fy(Xs), NX)); o.append(Tb(fx(0) + 12, fy(Xs) + 22, f'static {Xs:.0f} mm', 13, 'start', NX, True))
    o.append(dot(fx(2), fy(X(2)), AC)); o.append(Tb(fx(2) + 10, fy(X(2)) - 12, f'{X(2):.2f} mm at r = 2', 13, 'start', AC, True))
    o.append(Tb(fx(1.45), fy(10), 'ζ = 0.1 (dashed): peak 25 mm, off the scale', 12, 'start', MUT))
    o.append(T(340, 372, 'the peak is 1/(2ζ) = 2.5 times the static deflection for ζ = 0.2', 13, fill=MUT))
    return 384, ''.join(o)

FIG[9] = (f9, 'The first worked example: steady amplitude of the 500 kg, 200 kN/m model under a 1 kN force against frequency ratio. The static deflection is 5 mm; at resonance (r = 1) the amplitude is 12.5 mm, 1/(2ζ) = 2.5 times larger for ζ = 0.2, and at r = 2 it has fallen to 1.61 mm. Halving the damping (dashed) doubles the peak.',
          'A graph of amplitude X in millimetres against frequency ratio r from 0 to 3. The solid curve for damping ratio 0.2 starts at 5 millimetres at r equal to 0, rises to a peak of 12.5 millimetres at r equal to 1, and falls to 1.61 millimetres at r equal to 2. A dashed curve for damping ratio 0.1 rises much higher near r equal to 1 and leaves the top of the graph.')


# ---- 10: interaction of compression and shear ----
def f10():
    Rc, Rs = 0.4514, 0.5194
    lam = 2 / (Rc + math.sqrt(Rc ** 2 + 4 * Rs ** 2))
    x0, x1, y0, y1 = 90, 450, 40, 300
    fx = lambda v: x0 + (x1 - x0) * v / 1.1; fy = lambda v: y1 - (y1 - y0) * v / 1.1
    o = [T(360, 22, 'Long flat panel: compression with shear', 15, bold=True)]
    o.append(axes(x0, x1, y0 + 20, y1, [0, 0.2, 0.4, 0.6, 0.8, 1.0], [0, 0.2, 0.4, 0.6, 0.8, 1.0], fx, fy, 'R<tspan baseline-shift="sub" font-size="11">c</tspan> = σ/σ<tspan baseline-shift="sub" font-size="11">cr</tspan>', 'R<tspan baseline-shift="sub" font-size="11">s</tspan> = τ/τ<tspan baseline-shift="sub" font-size="11">cr</tspan>', lambda v: f'{v:.1f}', lambda v: f'{v:.1f}'))
    o.append(P([(fx(math.cos(math.radians(a))), fy(math.sin(math.radians(a)))) for a in range(0, 91)], LV, 2, '7 5'))
    o.append(P([(fx(0), fy(1)), (fx(1), fy(0))], L2, 2, '2 4'))
    o.append(P([(fx(1 - s * s), fy(s)) for s in [i / 100 for i in range(101)]], AC, 3.5))
    o.append(L(fx(0), fy(0), fx(lam * Rc), fy(lam * Rs), INK, 1.4, '4 3'))
    o.append(dot(fx(Rc), fy(Rs), INK)); o.append(Tb(fx(Rc) - 10, fy(Rs) + 20, f'applied ({Rc:.2f}, {Rs:.2f})', 13, 'end', INK, True))
    o.append(dot(fx(lam * Rc), fy(lam * Rs), AC, 4.5))
    ra = math.sqrt(1 - Rc); rw = math.sqrt(1 - Rc ** 2)
    o.append(dot(fx(Rc), fy(ra), AC)); o.append(dot(fx(Rc), fy(rw), LV))
    o.append(L(fx(Rc), fy(Rs), fx(Rc), fy(rw), L2, 1.2, '3 3'))
    # legend on right
    lx = 480
    o.append(L(lx, 90, lx + 34, 90, AC, 3.5)); o.append(T(lx + 42, 95, 'R<tspan baseline-shift="sub" font-size="11">c</tspan> + R<tspan baseline-shift="sub" font-size="11">s</tspan>² = 1 (use this)', 13, 'start', AC, True))
    o.append(L(lx, 120, lx + 34, 120, LV, 2, '7 5')); o.append(T(lx + 42, 125, 'circle: unsafe here', 13, 'start', LV, True))
    o.append(L(lx, 150, lx + 34, 150, L2, 2, '2 4')); o.append(T(lx + 42, 155, 'straight line', 13, 'start', MUT))
    o.append(T(lx, 200, f'λ = {lam:.3f}, MS = {lam - 1:.2f}', 13, 'start', INK, True))
    o.append(T(lx, 222, f'allowable τ at 12 MPa:', 13, 'start', AC))
    o.append(T(lx, 242, f'R<tspan baseline-shift="sub" font-size="11">s</tspan> = {ra:.3f}, τ = 28.5 MPa', 13, 'start', AC, True))
    o.append(T(lx, 266, f'circle would give {rw:.3f}, 34.4 MPa', 13, 'start', LV))
    return 362, ''.join(o)

FIG[10] = (f10, 'The first worked example on the interaction diagram. The applied stresses (R<sub>c</sub> = 0.45, R<sub>s</sub> = 0.52) lie inside the curve R<sub>c</sub> + R<sub>s</sub>² = 1; scaling both by λ = 1.263 reaches it, a margin of 0.26. At 12 MPa compression the curve allows R<sub>s</sub> = 0.741 (28.5 MPa of shear); the circle would allow 0.892 (34.4 MPa), which is unsafe.',
          'A graph of shear ratio R s against compression ratio R c, both from 0 to 1.1. A solid curve R c plus R s squared equals 1 runs from (0, 1) to (1, 0), bulging outward. A dashed quarter circle lies outside it and a dotted straight line inside it. The applied point at 0.45, 0.52 is inside the solid curve, with a dashed ray from the origin through it reaching the curve at a factor of 1.263. Directly above the point, the solid curve is crossed at 0.741 and the circle at 0.892.')

spec = make_spec(FIG)


def text_fixes(k):
    return []
