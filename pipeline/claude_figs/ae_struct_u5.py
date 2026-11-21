"""Claude's hand-drawn figures for ae-struct-u5 (shear flow, shear centre and torsion), one per chapter. Every number is
the matching chapter's worked example, recomputed here. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def arrow(x1, y1, x2, y2, c=AC, w=2.5, kind='n', dash=None):
    return L(x1, y1, x2, y2, c, w, dash, arrow=kind)


def poly(pts, fill, stroke, sw=2, op=None):
    o = f';fill-opacity:{op}' if op is not None else ''
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" style="fill:{fill};stroke:{stroke};stroke-width:{sw}{o}"/>'


def boom(x, y, r, lab=None, c=AC, soft=ACS):
    o = f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" style="fill:{soft};stroke:{c};stroke-width:2"/>'
    if lab: o += T(x, y + 4.5, lab, 13, bold=True)
    return o


def mid_arrow(x1, y1, x2, y2, c=AC, w=2.2, frac=0.5, size=9):
    """small arrowhead in the middle of a wall from (x1,y1) to (x2,y2)"""
    mx, my = x1 + (x2 - x1) * frac, y1 + (y2 - y1) * frac
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (mx + size * math.cos(a), my + size * math.sin(a))
    p2 = (mx - size * math.cos(a) + size * 0.6 * math.sin(a), my - size * math.sin(a) - size * 0.6 * math.cos(a))
    p3 = (mx - size * math.cos(a) - size * 0.6 * math.sin(a), my - size * math.sin(a) + size * 0.6 * math.cos(a))
    return poly([p1, p2, p3], c, c, 1)


def dot(x, y, lab, c, dx=0, dy=-12, anchor='middle', r=6):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{c};stroke:var(--fig);stroke-width:2"/>' + Tb(x + dx, y + dy, lab, 13, anchor, c, True)


# ---- 1: channel shear flow and the shear centre ----
def f1():
    h, b, t, S = 120.0, 60.0, 3.0, 5000.0
    I = t * h ** 3 / 12 + 2 * b * t * (h / 2) ** 2
    qj = S / I * t * b * h / 2; qm = qj + S / I * t * (h / 2) ** 2 / 2
    e = 3 * b ** 2 / (h + 6 * b); xb = (2 * b * t * b / 2) / (2 * b * t + h * t)
    s = 1.7
    o = [T(190, 26, 'Channel 120 × 60 × 3 mm, S = 5 kN', 15, bold=True)]
    X0, Y0 = 200, 84
    Yb = Y0 + h * s; Xf = X0 + b * s; Ym = (Y0 + Yb) / 2
    for a, c in (((X0, Y0), (Xf, Y0)), ((X0, Y0), (X0, Yb)), ((X0, Yb), (Xf, Yb))):
        o.append(L(a[0], a[1], c[0], c[1], AC, 6))
    # flow directions for a downward shear: along the top flange towards the web, down the web, out along the bottom
    o.append(mid_arrow(Xf, Y0, X0, Y0, INK)); o.append(mid_arrow(X0, Y0, X0, Yb, INK)); o.append(mid_arrow(X0, Yb, Xf, Yb, INK))
    o.append(L(X0 - 60, Ym, Xf + 30, Ym, L2, 1.4, '6 5'))
    xs, xg = X0 - e * s, X0 + xb * s
    o.append(dot(xs, Ym, 'S', LV, -14, -8, 'end')); o.append(dot(xg, Ym, 'G', NX, 0, -14))
    o.append(arrow(xs, Ym - 90, xs, Ym - 10, LV, 2.5, 'l')); o.append(Tb(xs - 6, Ym - 96, '5 kN', 13, 'end', LV, True))
    # dimensions
    yd = Yb + 34
    o.append(L(xs, Yb + 8, xs, yd + 6, L2, 1.2)); o.append(L(X0, Yb + 8, X0, yd + 6, L2, 1.2)); o.append(L(xg, Yb + 8, xg, yd + 6, L2, 1.2))
    o.append(L(xs, yd, X0, yd, INK, 1.5)); o.append(L(X0, yd, xg, yd, INK, 1.5))
    o.append(T(xs - 6, yd + 5, f'e = {e:.1f} mm', 13, 'end', LV, True)); o.append(T(xg + 6, yd + 5, f'x̄ = {xb:.0f} mm', 13, 'start', NX, True))
    o.append(T(X0 - 70, Ym + 30, 'shear centre', 13, 'end', LV)); o.append(T(X0 - 70, Ym + 47, 'outside the web', 13, 'end', LV))
    o.append(T(xg + 18, Ym + 30, 'centroid', 13, 'start', NX))
    # right panel: distribution
    Q0x, k = 470, 1.25
    o.append(T(570, 26, 'Shear flow q (N/mm)', 15, bold=True))
    Y1, Y2 = Y0, Yb
    for yy in (Y1, Y2): o.append(L(Q0x, yy, Q0x + b * s, yy, AC, 5))
    o.append(L(Q0x, Y1, Q0x, Y2, AC, 5))
    o.append(poly([(Q0x + b * s, Y1), (Q0x, Y1 - qj * k), (Q0x, Y1)], ACS, AC, 1.5, 0.9))
    o.append(poly([(Q0x + b * s, Y2), (Q0x, Y2 + qj * k), (Q0x, Y2)], ACS, AC, 1.5, 0.9))
    pts = [(Q0x, Y1)]
    for i in range(41):
        yy = i / 40 * h; yv = h / 2 - yy
        qv = qj + S / I * t * ((h / 2) ** 2 - yv ** 2) / 2
        pts.append((Q0x + qv * k, Y1 + yy * s))
    pts.append((Q0x, Y2))
    o.append(poly(pts, NXS, NX, 1.5, 0.9))
    o.append(T(Q0x - 8, Y1 - qj * k + 4, f'{qj:.2f}', 13, 'end', AC, True))
    o.append(T(Q0x + b * s + 8, Y1 + 5, '0 at the tip', 13, 'start', MUT))
    o.append(T(Q0x + qm * k + 8, Ym + 5, f'{qm:.2f} at mid-web', 13, 'start', NX, True))
    o.append(T(Q0x + 30, Ym + 48, 'parabola', 13, 'start', MUT))
    o.append(T(Q0x + 30, Y2 + qj * k + 22, 'linear on each flange', 13, 'start', MUT))
    return 370, ''.join(o)

FIG[1] = (f1, 'The worked example\'s channel under a 5 kN downward shear. Left: the flow runs along the top flange to the web, down the web and out along the bottom flange; the shear centre S lies 22.5 mm outside the web and the centroid G 15 mm inside it. Right: q grows linearly along each flange to 31.25 N/mm and peaks at 46.88 N/mm at mid-web.',
          'Left: a channel drawn as three thick lines, web on the left, flanges to the right. Arrows show the flow along the top flange towards the web, down the web, and out along the bottom flange. On the dashed axis of symmetry the shear centre S is 22.5 millimetres left of the web, with the 5 kilonewton load arrow on it, and the centroid G is 15 millimetres right of the web. Right: the same channel with its shear flow drawn on it: triangles on the flanges rising from zero at the tips to 31.25 newtons per millimetre at the corners, and a parabola on the web peaking at 46.88 at mid-depth.')


# ---- 2: Z-section shear flow plotted along the wall ----
def f2():
    t, bf, hw, Sy = 2.0, 40.0, 80.0, 3000.0
    Ixx = t * hw ** 3 / 12 + 2 * bf * t * (hw / 2) ** 2; Iyy = 2 * t * bf ** 3 / 3; Ixy = 2 * bf * t * (bf / 2) * (hw / 2)
    D = Ixx * Iyy - Ixy ** 2; Kx, Ky = Sy * Ixy / D, Sy * Iyy / D
    def q(s):
        if s <= 40: return Kx * (80 * s - s * s) - Ky * 80 * s
        q0 = Kx * 1600 - Ky * 3200
        if s <= 120: u = s - 40; return q0 - Ky * (80 * u - u * u)
        qe = q0; u = s - 120; return qe - Kx * u * u + Ky * 80 * u
    o = [T(110, 26, 'Z-section, S<tspan font-size="11" dy="4">y</tspan><tspan dy="-4"> = 3 kN</tspan>', 15, bold=True)]
    s = 1.6; cx, cy = 110, 175
    Pz = lambda x, y: (cx + x * s, cy - y * s)
    for a, b2 in (((0, 40), (40, 40)), ((0, -40), (0, 40)), ((0, -40), (-40, -40))):
        (x1, y1), (x2, y2) = Pz(*a), Pz(*b2); o.append(L(x1, y1, x2, y2, AC, 6))
    o.append(T(Pz(40, 40)[0] + 4, Pz(40, 40)[1] - 10, 'start s = 0', 13, 'middle', MUT))
    o.append(T(Pz(-40, -40)[0], Pz(-40, -40)[1] + 22, 's = 160', 13, fill=MUT))
    o.append(dot(cx, cy, 'G = shear centre', LV, 8, -6, 'start', 5))
    o.append(T(cx, 290, 'web 80 mm, flanges 40 mm, t = 2 mm', 13, fill=MUT))
    # plot
    x0, x1, y0, y1 = 300, 690, 60, 280
    fx = lambda v: x0 + v / 160 * (x1 - x0)
    fy = lambda v: y0 + (20 - v) / 70 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 40, 80, 120, 160], [20, 10, 0, -10, -20, -30, -40, -50], fx, fy, 's along the wall from the top tip (mm)', 'q (N/mm)', str, neg))
    for xv, lab in ((20, 'top flange'), (80, 'web'), (140, 'bottom flange')):
        o.append(T(fx(xv), y0 + 14, lab, 13, fill=MUT))
    for xv in (40, 120): o.append(L(fx(xv), y0, fx(xv), y1, L2, 1.2, '4 4'))
    pts = [(fx(v), fy(q(v))) for v in [i * 0.5 for i in range(321)]]
    o.append(P(pts, AC, 3))
    for v in (40, 80, 120):
        o.append(C(fx(v), fy(q(v)), 4.5, NX))
    o.append(Tb(fx(40) + 6, fy(q(40)) + 18, f'{q(40):.2f}'.replace('-', '−'), 13, 'start', NX, True))
    o.append(Tb(fx(80), fy(q(80)) - 10, f'{q(80):.2f} at the neutral axis'.replace('-', '−'), 13, 'middle', NX, True))
    o.append(Tb(fx(12), fy(q(10)) - 12, f'+{q(10):.2f}', 13, 'middle', AC, True))
    return 340, ''.join(o)

FIG[2] = (f2, 'The worked Z-section\'s shear flow, unrolled along its wall from the top flange tip. Because I<sub>xy</sub> ≠ 0 the flow changes sign inside each flange (up to +5.02 N/mm, then −16.07 N/mm at the corners); it peaks at −48.21 N/mm where the web crosses the neutral axis and returns to zero at the bottom tip.',
          'Left: a Z-section with its top flange to the right and bottom flange to the left, the centroid G marked as the shear centre. Right: a graph of shear flow against distance along the wall from the top tip, 0 to 160 millimetres. The curve starts at zero, rises to about plus 5 in the top flange, falls to minus 16.07 at the corner at 40 millimetres, reaches minus 48.21 at mid-web at 80 millimetres, climbs back to minus 16.07 at the lower corner at 120, rises to about plus 5 and ends at zero at 160.')


# ---- 3: box with a thick front wall, shear centre moves forward ----
def f3():
    s = 1.9; X0, Y0 = 80, 70
    W_, H_ = 200 * s, 100 * s
    o = [T(360, 26, 'Box 200 × 100 mm: front wall 4 mm, others 2 mm', 15, bold=True)]
    o.append(L(X0, Y0, X0, Y0 + H_, AC, 9))
    for a, b2 in (((X0, Y0), (X0 + W_, Y0)), ((X0 + W_, Y0), (X0 + W_, Y0 + H_)), ((X0, Y0 + H_), (X0 + W_, Y0 + H_))):
        o.append(L(a[0], a[1], b2[0], b2[1], AC, 4.5))
    ym = Y0 + H_ / 2
    o.append(L(X0 - 30, ym, X0 + W_ + 30, ym, L2, 1.3, '6 5'))
    # cut mark
    o.append(L(X0 - 12, ym - 6, X0 + 12, ym + 6, INK, 2.5)); o.append(T(X0 - 16, ym - 10, 'cut', 13, 'end', MUT))
    # physical flows for upward S: both walls upwards
    o.append(mid_arrow(X0, Y0 + H_, X0, Y0, INK, 2, 0.25)); o.append(mid_arrow(X0 + W_, Y0 + H_, X0 + W_, Y0, INK, 2, 0.75))
    o.append(T(X0 + 14, Y0 + 30, '5.70 kN', 13, 'start', INK, True)); o.append(T(X0 + W_ - 14, Y0 + 30, '4.30 kN', 13, 'end', INK, True))
    o.append(T(X0 + 14, Y0 + 47, 'front wall', 13, 'start', MUT)); o.append(T(X0 + W_ - 14, Y0 + 47, 'rear wall', 13, 'end', MUT))
    xs, xg, xm = X0 + 78.8 * s, X0 + 85.7 * s, X0 + 100 * s
    o.append(arrow(xs, ym + 70, xs, ym + 12, LV, 2.5, 'l')); o.append(T(xs - 8, ym + 68, '10 kN', 13, 'end', LV, True))
    o.append(dot(xs, ym, 'S', LV, -10, -12, 'end')); o.append(dot(xg, ym, 'G', NX, 0, -12)); o.append(dot(xm, ym, 'mid', MUT, 10, -12, 'start', 4))
    yd = Y0 + H_ + 34
    for xx in (X0, xs, xg, xm): o.append(L(xx, Y0 + H_ + 8, xx, yd + 5, L2, 1.2))
    o.append(L(X0, yd, xs, yd, LV, 1.6)); o.append(T((X0 + xs) / 2, yd + 20, 'shear centre 78.8 mm', 13, fill=LV, bold=True))
    o.append(T(xg + 4, yd + 20, 'centroid 85.7', 13, 'start', NX, True)); o.append(T(xm + 4, yd - 6, 'uniform box: 100', 13, 'start', MUT))
    # right note
    nx = X0 + W_ + 50
    o.append(boxt(nx - 10, 90, 170, 150, ['zero twist', '∮q ds/t = 0', 'q₀ = 63.64 N/mm', 'thick wall takes', 'more shear'], PANEL, AC, 13, True))
    return 340, ''.join(o)

FIG[3] = (f3, 'The second worked example. Thickening the front wall to 4 mm makes it take 5.70 kN of the 10 kN shear in the zero-twist solution, so the shear centre S moves forward to 78.8 mm from the front wall, ahead of both the uniform-box position (100 mm) and the centroid G (85.7 mm).',
          'A rectangular box drawn with a thick left wall. A dashed horizontal axis runs through mid-depth, with a cut mark on the left wall. Both vertical walls carry upward flow, 5.70 kilonewtons in the front wall and 4.30 in the rear wall. On the axis the shear centre S is at 78.8 millimetres from the front wall with the 10 kilonewton load on it, the centroid G at 85.7, and the uniform-box position at 100. A note says zero twist, the integral of q over t is zero, q nought is 63.64 newtons per millimetre, and the thick wall takes more shear.')


# ---- 4: Bredt-Batho box ----
def f4():
    s = 0.78; X0, Y0 = 108, 80
    W_, H_ = 600 * s, 200 * s
    o = [T(360, 28, 'Single cell under T = 30 kN·m: q = T/2A = 125 N/mm', 15, bold=True)]
    o.append(L(X0, Y0, X0 + W_, Y0, AC, 3.5)); o.append(L(X0, Y0 + H_, X0 + W_, Y0 + H_, AC, 3.5))
    o.append(L(X0, Y0, X0, Y0 + H_, AC, 7)); o.append(L(X0 + W_, Y0, X0 + W_, Y0 + H_, AC, 7))
    o.append(R(X0 + 6, Y0 + 6, W_ - 12, H_ - 12, ACS, 'none', 4, 0))
    o.append(T(X0 + W_ / 2, Y0 + H_ / 2 - 4, 'A = 600 × 200 = 120,000 mm²', 14, bold=True))
    o.append(T(X0 + W_ / 2, Y0 + H_ / 2 + 18, '(area inside the mid-line)', 13, fill=MUT))
    # anticlockwise flow
    for (a, b2, f) in (((X0 + W_, Y0), (X0, Y0), 0.5), ((X0, Y0), (X0, Y0 + H_), 0.5), ((X0, Y0 + H_), (X0 + W_, Y0 + H_), 0.5), ((X0 + W_, Y0 + H_), (X0 + W_, Y0), 0.5)):
        o.append(mid_arrow(a[0], a[1], b2[0], b2[1], INK, 2, f, 10))
    o.append(T(X0 + W_ / 2, Y0 - 12, 'skin 1.5 mm: τ = 125/1.5 = 83.3 N/mm²', 13, fill=INK, bold=True))
    o.append(T(X0 + W_ / 2, Y0 + H_ + 26, 'skin 1.5 mm: τ = 83.3 N/mm²', 13, fill=INK, bold=True))
    o.append(T(X0 - 12, Y0 + H_ / 2 - 6, 'web 3 mm', 13, 'end', MUT)); o.append(T(X0 - 12, Y0 + H_ / 2 + 12, '41.7 N/mm²', 13, 'end', INK, True))
    o.append(T(X0 + W_ + 12, Y0 + H_ / 2 - 6, 'web 3 mm', 13, 'start', MUT)); o.append(T(X0 + W_ + 12, Y0 + H_ / 2 + 12, '41.7 N/mm²', 13, 'start', INK, True))
    yb = Y0 + H_ + 60
    o.append(T(360, yb, '∮ds/t = 1200/1.5 + 400/3 = 933.3;  J = 4A²/∮ds/t = 6.171 × 10⁷ mm⁴', 13, fill=MUT))
    o.append(T(360, yb + 20, 'dθ/dz = T/GJ = 1.80 × 10⁻⁵ rad/mm = 1.03° per metre (G = 27 GPa)', 13, fill=MUT))
    return 330, ''.join(o)

FIG[4] = (f4, 'The worked example\'s single-cell box. The same 125 N/mm flows round every wall, so the 1.5 mm skins carry 83.3 N/mm² and the 3 mm webs 41.7 N/mm²; the thick webs add little to ∮ds/t, and the box twists 1.03° per metre.',
          'A wide rectangle, 600 by 200 millimetres, with thin top and bottom skins and thicker side webs, shaded inside and labelled A equals 120,000 square millimetres. Arrows run anticlockwise round all four walls. Labels give the stress as 83.3 newtons per square millimetre in each 1.5 millimetre skin and 41.7 in each 3 millimetre web. Below, the integral of ds over t is 933.3, J is 6.171 times ten to the seven, and the twist rate is 1.03 degrees per metre.')


# ---- 5: two-cell box under shear ----
def f5():
    s = 0.72; X0, Y0 = 60, 110
    xs = [0, 300, 800]; H_ = 200 * s
    o = [T(360, 26, 'Two-cell box under 60 kN lift at x = 200 mm', 15, bold=True)]
    X = [X0 + v * s for v in xs]
    o.append(L(X[0], Y0, X[2], Y0, AC, 3)); o.append(L(X[0], Y0 + H_, X[2], Y0 + H_, AC, 3))
    for xx, w in zip(X, (6, 5, 4)): o.append(L(xx, Y0, xx, Y0 + H_, AC, w))
    for xx, B in zip(X, (1200, 900, 600)):
        r = 5 + B / 120
        o.append(boom(xx, Y0, r)); o.append(boom(xx, Y0 + H_, r))
    o.append(T(X[0], Y0 - 22, '1200', 13, fill=MUT)); o.append(T(X[1], Y0 - 22, '900', 13, fill=MUT)); o.append(T(X[2], Y0 - 22, '600 mm²', 13, fill=MUT))
    vals = (147.72, 100.31, 51.97)
    for xx, v, fr in zip(X, vals, (0.5, 0.28, 0.5)):
        o.append(mid_arrow(xx, Y0 + H_, xx, Y0, INK, 2, fr, 10))
    o.append(Tb(X[0] + 10, Y0 + H_ / 2 + 30, '147.72', 13, 'start', INK, True))
    o.append(Tb(X[1] + 10, Y0 + H_ - 22, '100.31', 13, 'start', INK, True))
    o.append(Tb(X[2] - 10, Y0 + H_ / 2 + 30, '51.97', 13, 'end', INK, True))
    o.append(T((X[0] + X[1]) / 2, Y0 - 10, 'skins 14.39 (clockwise)', 13, fill=MUT))
    o.append(T((X[1] + X[2]) / 2, Y0 - 10, 'skins 14.70 (clockwise)', 13, fill=MUT))
    o.append(T((X[0] + X[1]) / 2, Y0 + H_ / 2 - 22, 'cell 1', 14, bold=True)); o.append(T((X[1] + X[2]) / 2 + 40, Y0 + H_ / 2 - 22, 'cell 2', 14, bold=True))
    xl, xsc = X0 + 200 * s, X0 + 287.4 * s
    ym = Y0 + H_ / 2
    o.append(arrow(xl, Y0 + H_ + 70, xl, ym + 6, LV, 2.5, 'l')); o.append(T(xl - 6, Y0 + H_ + 66, '60 kN', 13, 'end', LV, True))
    o.append(dot(xsc, ym, 'S', LV, 10, 5, 'start'))
    o.append(T(xsc + 6, Y0 + H_ + 62, 'shear centre 287.4 mm', 13, 'start', LV, True))
    o.append(T(360, Y0 + H_ + 96, 'flows in N/mm, spars all upwards; twist 0.134° per metre, nose up', 13, fill=MUT))
    return 360, ''.join(o)

FIG[5] = (f5, 'The second worked example\'s two-cell box, booms drawn to scale. With the 60 kN lift 87 mm ahead of the shear centre the spar webs carry 147.72, 100.31 and 51.97 N/mm, the skins a small clockwise flow, and the box twists nose up at 0.134° per metre.',
          'A long rectangle divided by a middle spar into a front cell and a longer rear cell, with six circular booms at the spar ends, larger at the front: 1200, 900 and 600 square millimetres. Upward arrows on the three spars are labelled 147.72, 100.31 and 51.97 newtons per millimetre. The skins carry 14.39 in cell 1 and 14.70 in cell 2, clockwise. A 60 kilonewton upward load arrow acts at 200 millimetres; the shear centre S is marked at 287.4 millimetres. A note gives the twist as 0.134 degrees per metre, nose up.')


# ---- 6: real section to booms and panels ----
def f6():
    o = [T(180, 26, 'Real section', 15, bold=True), T(540, 26, 'Idealised: six booms', 15, bold=True)]
    s = 0.62
    for (X0, ideal) in ((40, False), (420, True)):
        Y0 = 70; W_, H_ = 400 * s, 200 * s
        if not ideal:
            o.append(R(X0, Y0, W_, H_, 'none', AC, 0, 3))
            for xx in (X0, X0 + W_):
                for yy in (Y0, Y0 + H_):
                    o.append(R(xx - 8, yy - 6 if yy == Y0 else yy - 6, 16, 12, ACS, AC, 2, 1.5))
            for yy in (Y0, Y0 + H_):
                o.append(R(X0 + W_ / 2 - 5, yy - (14 if yy == Y0 else -2), 10, 12, ACS, AC, 2, 1.5))
            o.append(T(X0 + W_ / 2, Y0 + H_ + 40, 'caps 300 mm², stringers 150 mm²', 13, fill=MUT))
            o.append(T(X0 + W_ / 2, Y0 + H_ + 58, 'skin and webs 2 mm, 400 × 200 mm', 13, fill=MUT))
            o.append(T(X0 + W_ / 2, Y0 + H_ / 2 + 5, 'I_exact = 3.3667 × 10⁷ mm⁴'.replace('I_exact', 'I<tspan font-size="11" dy="4">exact</tspan><tspan dy="-4"></tspan>'), 13, fill=INK))
        else:
            o.append(R(X0, Y0, W_, H_, 'none', L2, 0, 1.5))
            pts = [(X0, Y0, '566.7'), (X0 + W_ / 2, Y0, '550'), (X0 + W_, Y0, '566.7'), (X0, Y0 + H_, '566.7'), (X0 + W_ / 2, Y0 + H_, '550'), (X0 + W_, Y0 + H_, '566.7')]
            for x, y, lab in pts:
                o.append(boom(x, y, 11))
                o.append(T(x, y - 18 if y == Y0 else y + 30, lab, 13, fill=AC, bold=True))
            # flows for an upward shear on the axis: webs up, skins outward from the middle at the top
            o.append(mid_arrow(X0, Y0, X0 + W_ / 2, Y0, INK, 2, 0.5)); o.append(mid_arrow(X0 + W_, Y0, X0 + W_ / 2, Y0, INK, 2, 0.5))
            o.append(mid_arrow(X0 + W_ / 2, Y0 + H_, X0, Y0 + H_, INK, 2, 0.5)); o.append(mid_arrow(X0 + W_ / 2, Y0 + H_, X0 + W_, Y0 + H_, INK, 2, 0.5))
            o.append(mid_arrow(X0, Y0 + H_, X0, Y0, INK, 2, 0.5)); o.append(mid_arrow(X0 + W_, Y0 + H_, X0 + W_, Y0, INK, 2, 0.5))
            o.append(T(X0 + W_ / 4, Y0 + 22, '12.25', 13, fill=INK, bold=True)); o.append(T(X0 + 3 * W_ / 4, Y0 + 22, '12.25', 13, fill=INK, bold=True))
            o.append(T(X0 + W_ / 4, Y0 + H_ - 10, '12.25', 13, fill=INK, bold=True)); o.append(T(X0 + 3 * W_ / 4, Y0 + H_ - 10, '12.25', 13, fill=INK, bold=True))
            o.append(T(X0 - 14, Y0 + H_ / 2 + 5, '37.5', 13, 'end', INK, True)); o.append(T(X0 + W_ + 14, Y0 + H_ / 2 + 5, '37.5', 13, 'start', INK, True))
            o.append(T(X0 + W_ / 2, Y0 + H_ + 58, 'boom areas mm²; flows N/mm for S<tspan font-size="11" dy="4">y</tspan><tspan dy="-4"> = +15 kN</tspan>', 13, fill=MUT))
            o.append(T(X0 + W_ / 2, Y0 + H_ / 2 + 5, 'ΣBy² = 3.3667 × 10⁷ mm⁴', 13, fill=INK))
    o.append(arrow(305, 130, 350, 130, AC, 2.5))
    o.append(T(360, 300, 'corner: 300 + (2·200/6)(2 + 1) + (2·200/6)(2 − 1) = 566.7;   stringer: 150 + 2(2·200/6)(3) = 550', 13, fill=MUT))
    return 320, ''.join(o)

FIG[6] = (f6, 'The worked example idealised. Each corner boom takes its spar cap plus a third of the 200 mm skin panel (ratio +1) and a sixth of the web (ratio −1); the mid-stringer takes a third of each skin panel either side. The six booms give exactly the real I<sub>xx</sub>, and a 15 kN shear puts 12.25 N/mm in each skin panel and 37.5 N/mm in each web.',
          'Left: the real box 400 by 200 millimetres with four corner spar caps and a stringer at mid-width of the top and of the bottom skin; I exact is 3.3667 times ten to the seven. An arrow leads right to the idealised section: six circular booms, 566.7 square millimetres at the corners and 550 at mid-width, joined by thin panels. Flow arrows run up both webs, inward to the middle along the top skin and outward from the middle along the bottom, labelled 12.25 newtons per millimetre in each skin panel and 37.5 in each web. A line at the bottom shows the two boom-area sums.')


# ---- 7: tapered spar and web flow along the span ----
def f7():
    L_, h0, h1, W = 2000.0, 200.0, 120.0, 20000.0
    sl = (h0 - h1) / L_
    def qz(z):
        h = h0 - sl * z; M = W * (L_ - z); return (W - M * sl / h) / h
    o = [T(180, 26, 'Spar elevation (root left, 20 kN at the tip)', 15, bold=True)]
    sx, sy = 0.15, 0.6
    X0, Yc = 30, 150
    xr, xt = X0, X0 + L_ * sx
    o.append(P([(xr, Yc - h0 / 2 * sy), (xt, Yc - h1 / 2 * sy)], AC, 5)); o.append(P([(xr, Yc + h0 / 2 * sy), (xt, Yc + h1 / 2 * sy)], AC, 5))
    o.append(L(xt, Yc - h1 / 2 * sy, xt, Yc + h1 / 2 * sy, AC, 2)); o.append(L(xr, Yc - h0 / 2 * sy - 10, xr, Yc + h0 / 2 * sy + 10, INK, 4))
    o.append(arrow(xt + 14, Yc - 40, xt + 14, Yc + 10, LV, 2.5, 'l')); o.append(T(xt + 20, Yc - 44, '20 kN', 13, 'start', LV, True))
    o.append(T(xr + 8, Yc - h0 / 2 * sy - 14, 'P = 200 kN tension', 13, 'start', AC, True))
    o.append(T(xr + 8, Yc + h0 / 2 * sy + 24, 'P = 200 kN compression', 13, 'start', AC, True))
    o.append(T(xr - 4, Yc + 4, '200', 13, 'end', MUT)); o.append(T(xt - 6, Yc + 4, '120 mm', 13, 'end', MUT))
    o.append(T(170, 268, 'each boom slopes 0.02; at the root the', 13, fill=MUT))
    o.append(T(170, 286, 'booms carry 2 × 4 kN = 8 kN of the shear', 13, fill=MUT))
    # plot
    x0, x1, y0, y1 = 400, 690, 60, 260
    fx = lambda z: x0 + z / 2000 * (x1 - x0); fy = lambda v: y1 - v / 180 * (y1 - y0)
    o.append(T(545, 26, 'Web shear flow along the span', 15, bold=True))
    o.append(axes(x0, x1, y0, y1, [0, 500, 1000, 1500, 2000], [0, 50, 100, 150], fx, fy, 'distance from the root (mm)', 'q (N/mm)'))
    o.append(P([(fx(z), fy(qz(z))) for z in range(0, 2001, 20)], AC, 3))
    o.append(P([(fx(z), fy(W / (h0 - sl * z))) for z in range(0, 2001, 20)], L2, 2, '6 5'))
    for z in (0, 1000, 2000):
        o.append(C(fx(z), fy(qz(z)), 4.5, NX))
    o.append(Tb(fx(0) + 8, fy(qz(0)) + 18, '60', 13, 'start', NX, True))
    o.append(Tb(fx(1000) + 8, fy(qz(1000)) + 18, '93.75', 13, 'start', NX, True))
    o.append(Tb(fx(2000) - 8, fy(qz(2000)) - 10, '166.7', 13, 'end', NX, True))
    o.append(Tb(fx(400), fy(W / (h0 - sl * 400)) - 10, 'S/h, no taper', 13, 'middle', MUT))
    return 320, ''.join(o)

FIG[7] = (f7, 'The worked tapered spar. Left: the booms converge towards the tip, so their 200 kN root forces each lean at 0.02 and together carry 8 kN of the 20 kN shear. Right: the web flow (solid) is 60 N/mm at the root, 93.75 N/mm at mid-span and 166.7 N/mm at the tip, below the untapered S/h (dashed) wherever the moment is not zero.',
          'Left: a side view of a spar whose two booms converge from 200 millimetres apart at the root to 120 at the tip, with a 20 kilonewton downward load at the tip. The top boom carries 200 kilonewtons tension and the bottom 200 kilonewtons compression at the root. A note says each boom slopes 0.02 and at the root they carry 8 kilonewtons of the shear. Right: a graph of web shear flow against distance from the root, rising from 60 newtons per millimetre at the root through 93.75 at mid-span to 166.7 at the tip, with a dashed curve for S over h lying above it and meeting it at the tip.')


# ---- 8: cell with open trailing panels ----
def f8():
    s = 1.6; X0, Yc = 80, 175
    Pz = lambda x, y: (X0 + x * s, Yc - y * s)
    o = [T(360, 26, 'One closed cell, two open trailing panels, S = 10 kN on the front spar', 15, bold=True)]
    B = {1: (0, 50, 600), 2: (200, 50, 800), 3: (200, -50, 800), 4: (0, -50, 600), 5: (300, 25, 200), 6: (300, -25, 200)}
    for a, b2, w in ((1, 2, 3), (4, 3, 3), (1, 4, 4.5), (2, 3, 4.5), (2, 5, 2), (3, 6, 2)):
        (x1, y1), (x2, y2) = Pz(*B[a][:2]), Pz(*B[b2][:2]); o.append(L(x1, y1, x2, y2, AC, w))
    for k, (x, y, A) in B.items():
        X, Y = Pz(x, y); o.append(boom(X, Y, 6 + A / 100, str(k)))
    # flows (physical): front spar up 68.97, rear spar up 34.48, skins 27.59 clockwise, trailing 6.90
    o.append(mid_arrow(*Pz(0, -50), *Pz(0, 50), INK, 2, 0.5, 10)); o.append(Tb(Pz(0, 0)[0] - 12, Pz(0, 0)[1] - 34, '68.97', 13, 'end', INK, True))
    o.append(mid_arrow(*Pz(200, -50), *Pz(200, 50), INK, 2, 0.5, 10)); o.append(Tb(Pz(200, 0)[0] - 10, Pz(200, 0)[1] + 5, '34.48', 13, 'end', INK, True))
    o.append(mid_arrow(*Pz(0, 50), *Pz(200, 50), INK, 2, 0.5, 10)); o.append(T(Pz(100, 50)[0], Pz(100, 50)[1] - 12, '27.59', 13, fill=INK, bold=True))
    o.append(mid_arrow(*Pz(200, -50), *Pz(0, -50), INK, 2, 0.5, 10)); o.append(T(Pz(100, -50)[0], Pz(100, -50)[1] + 24, '27.59', 13, fill=INK, bold=True))
    o.append(T(Pz(250, 38)[0] + 10, Pz(250, 38)[1] - 10, '6.90', 13, fill=INK, bold=True)); o.append(T(Pz(250, -38)[0] + 10, Pz(250, -38)[1] + 22, '6.90', 13, fill=INK, bold=True))
    o.append(T(Pz(300, 0)[0] + 16, Pz(300, 0)[1] + 5, 'free edges', 13, 'start', MUT))
    o.append(L(Pz(-20, 0)[0], Yc, Pz(330, 0)[0], Yc, L2, 1.2, '6 5'))
    xs = Pz(99.06, 0)[0]
    o.append(dot(xs, Yc, 'S', LV, 10, 5, 'start'))
    o.append(arrow(X0 - 28, Yc + 60, X0 - 28, Yc - 10, LV, 2.5, 'l')); o.append(T(X0 - 34, Yc + 58, '10 kN', 13, 'end', LV, True))
    o.append(T(360, Yc + 140, 'shear centre S 99.1 mm behind the front spar (load line)', 13, 'middle', LV, True))
    o.append(T(360, Yc + 160, 'q₀ = −27.59 N/mm; twist 0.482° per metre, nose up', 13, 'middle', MUT))
    return 350, ''.join(o)

FIG[8] = (f8, 'The worked mixed section, booms drawn to scale. The trailing panels start from zero at the free booms 5 and 6 and carry 6.90 N/mm; only the closed cell gets a constant, q<sub>s,0</sub> = −27.59 N/mm, fixed by moments about the loaded front spar. The shear centre is 99.1 mm behind the front spar, so the load twists the section nose up.',
          'A rectangular cell with booms 1 and 2 on top, 4 and 3 below, and two thin trailing panels from booms 2 and 3 converging to free booms 5 and 6. Arrows show 68.97 newtons per millimetre up the front spar, 34.48 up the rear spar, 27.59 clockwise in the top and bottom skins and 6.90 in each trailing panel. A 10 kilonewton upward load acts on the front spar; the shear centre S is marked 99.1 millimetres behind it. A note gives q nought as minus 27.59 and the twist as 0.482 degrees per metre, nose up.')


# ---- 9: Wagner beam ----
def f9():
    import math as m
    ta = ((1 + 400 / 1000) / (1 + 300 / 200)) ** 0.25; al = m.atan(ta)
    o = [T(360, 26, 'Complete tension field: d = 400 mm, b = 300 mm, W = 20 kN', 15, bold=True)]
    s = 0.36; X0, Y0 = 40, 70; H_ = 400 * s; nb = 4; W_ = nb * 300 * s
    o.append(L(X0, Y0, X0, Y0 + H_, INK, 5))
    o.append(L(X0, Y0, X0 + W_, Y0, AC, 6)); o.append(L(X0, Y0 + H_, X0 + W_, Y0 + H_, AC, 6))
    for i in range(1, nb + 1):
        xx = X0 + i * 300 * s; o.append(L(xx, Y0, xx, Y0 + H_, NX, 3.5))
    # tension lines: run down to the right at angle alpha to the flanges
    dx = H_ / m.tan(al)
    o.append(f'<clipPath id="wclip"><rect x="{X0:.1f}" y="{Y0:.1f}" width="{W_:.1f}" height="{H_:.1f}"/></clipPath>')
    lines = []
    for i in range(-12, 30):
        x1 = X0 + i * 18
        lines.append(L(x1, Y0, x1 + dx, Y0 + H_, LV, 1.4))
    o.append(f'<g clip-path="url(#wclip)">{"".join(lines)}</g>')
    o.append(arrow(X0 + W_ + 10, Y0 + H_ / 2 - 40, X0 + W_ + 10, Y0 + H_ / 2 + 30, LV, 2.5, 'l')); o.append(T(X0 + W_ + 18, Y0 + H_ / 2 - 40, 'W = 20 kN', 13, 'start', LV, True))
    # angle mark at bottom-left of the second bay
    ax, ay = X0 + 300 * s + 6, Y0
    o.append(T(X0 + 300 * s * 1.5, Y0 + H_ + 26, f'α = {m.degrees(al):.1f}°', 14, fill=LV, bold=True))
    o.append(T(X0 + 300 * s * 1.5, Y0 + H_ + 44, 'tension along the wrinkles', 13, fill=MUT))
    o.append(T(X0 + W_ / 2, Y0 - 12, 'top flange: F_T = 48.4 kN at z = 1.2 m'.replace('F_T', 'F<tspan font-size="11" dy="4">T</tspan><tspan dy="-4"></tspan>'), 13, fill=AC, bold=True))
    o.append(T(X0 + 300 * s * 2.2, Y0 + H_ + 26, 'bottom flange: −71.6 kN', 13, 'start', AC, True))
    o.append(T(X0 + 300 * s * 2.2, Y0 + H_ + 64, 'stiffeners (green): 12.98 kN struts', 13, 'start', NX, True))
    # summary box
    bx = 600
    o.append(boxt(bx - 10, 70, 130, 150, ['σ<tspan font-size="11" dy="4">t</tspan><tspan dy="-4"> = 101.1</tspan>', 'N/mm²', 'flanges lose', '11.56 kN each', 'secondary M', '0.324 kN·m'], PANEL, AC, 13, True))
    return 300, ''.join(o)

FIG[9] = (f9, 'The worked Wagner beam. The buckled web carries the 20 kN shear as tension along wrinkles at 40.9° to the flanges, σ<sub>t</sub> = 101.1 N/mm². The field compresses each flange by 11.56 kN on top of its bending load and turns every stiffener into a 12.98 kN strut.',
          'A cantilever beam seen from the side: a wall on the left, top and bottom flanges, five vertical stiffeners drawn in green at 300 millimetre spacing, and the web filled with parallel diagonal lines sloping down to the right at 40.9 degrees, the tension field. A 20 kilonewton load acts down at the free end. Labels give the top flange force as 48.4 kilonewtons at 1.2 metres from the tip, the bottom as minus 71.6, and the stiffeners as 12.98 kilonewton struts. A box gives the diagonal tension as 101.1 newtons per square millimetre, the flange loss as 11.56 kilonewtons each and the secondary moment as 0.324 kilonewton metres.')


# ---- 10: open angle against closed tube from the same strip ----
def f10():
    o = [T(360, 26, 'The same 120 × 2 mm strip under T = 10 N·m', 15, bold=True)]
    # angle
    s = 2.2; ax, ay = 70, 80
    o.append(L(ax, ay, ax, ay + 60 * s, AC, 6)); o.append(L(ax, ay + 60 * s, ax + 60 * s, ay + 60 * s, AC, 6))
    o.append(T(ax + 70, ay + 20, 'open angle 60 × 60', 14, 'start', INK, True))
    o.append(T(ax + 70, ay + 40, 'J = Σbt³/3 = 320 mm⁴', 13, 'start', MUT))
    o.append(T(ax + 70, ay + 58, 'τ_max = 62.5 N/mm²'.replace('τ_max', 'τ<tspan font-size="11" dy="4">max</tspan><tspan dy="-4"></tspan>'), 13, 'start', LV, True))
    o.append(T(ax + 70, ay + 76, '66.3° per metre', 13, 'start', LV, True))
    # tube
    tx, ty, ts = 420, 90, 3.6
    o.append(R(tx, ty, 30 * ts, 30 * ts, ACS, AC, 0, 5))
    o.append(T(tx + 15 * ts, ty + 15 * ts + 5, 'A = 900', 13, fill=INK, bold=True))
    o.append(T(tx + 30 * ts + 16, ty + 20, 'closed tube 30 × 30', 14, 'start', INK, True))
    o.append(T(tx + 30 * ts + 16, ty + 40, 'J = 4A²/∮ds/t = 54,000', 13, 'start', MUT))
    o.append(T(tx + 30 * ts + 16, ty + 58, 'τ = 2.78 N/mm²', 13, 'start', NX, True))
    o.append(T(tx + 30 * ts + 16, ty + 76, '0.393° per metre', 13, 'start', NX, True))
    o.append(T(tx + 30 * ts + 16, ty + 98, '169 times stiffer', 13, 'start', INK, True))
    # through-thickness stress sketches
    y0 = 270
    o.append(T(170, y0 - 22, 'shear stress across the wall', 13, fill=MUT))
    cx = 170; th = 40
    o.append(L(cx, y0 - 4, cx, y0 + th + 4, INK, 1.5)); o.append(T(cx - 100, y0 + th / 2 - 4, 'across the', 13, 'end', MUT)); o.append(T(cx - 100, y0 + th / 2 + 12, '2 mm wall', 13, 'end', MUT))
    o.append(L(cx - 60, y0 + th / 2, cx + 60, y0 + th / 2, L2, 1, '4 4'))
    o.append(poly([(cx, y0), (cx + 45, y0), (cx - 45, y0 + th), (cx, y0 + th)], LVS, LV, 1.5, 0.9))
    o.append(T(cx + 52, y0 + 6, '+62.5', 13, 'start', LV, True)); o.append(T(cx - 52, y0 + th + 4, '−62.5', 13, 'end', LV, True))
    o.append(T(cx, y0 + th + 24, 'zero on the mid-line', 13, fill=MUT))
    cx2 = 520
    o.append(T(cx2, y0 - 22, 'shear stress across the wall', 13, fill=MUT))
    o.append(L(cx2, y0 - 4, cx2, y0 + th + 4, INK, 1.5))
    o.append(R(cx2, y0, 10, th, NXS, NX, 0, 1.5))
    o.append(T(cx2 + 18, y0 + th / 2 + 5, '2.78, uniform', 13, 'start', NX, True))
    o.append(T(cx2, y0 + th + 24, 'constant q = T/2A', 13, fill=MUT))
    return 350, ''.join(o)

FIG[10] = (f10, 'The first worked example: one 120 mm strip of 2 mm sheet, bent open into an angle or closed into a tube. Open, its stress changes sign across the 2 mm wall and reaches 62.5 N/mm² at the faces; closed, a uniform 2.78 N/mm² flows round the loop, and the tube is 169 times stiffer.',
          'Left: an equal angle 60 by 60 millimetres with J equal to 320, maximum stress 62.5 newtons per square millimetre and a twist of 66.3 degrees per metre. Right: a closed square tube 30 by 30 millimetres from the same strip, enclosing 900 square millimetres, with J equal to 54,000, stress 2.78 and twist 0.393 degrees per metre, 169 times stiffer. Below each, a sketch of stress across the wall thickness: for the angle a linear distribution from plus 62.5 to minus 62.5, zero on the mid-line; for the tube a uniform 2.78.')

spec = make_spec(FIG)


def text_fixes(k):
    return []
