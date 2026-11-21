"""Claude's hand-drawn figures for me-design-u7 (Machine Design: gears and gearbox design), one per chapter, drawn from
each chapter's own worked example and numbers. Colours are the shell's CSS variables."""
import os, sys, math, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

_T, _Tb, _boxt = T, Tb, boxt


def _sub(s):
    """d_1, F_t ... drawn as real subscripts, never as underscores"""
    return re.sub(r'([A-Za-zα-ωΔ])_([A-Za-z0-9]+)', r'\1<tspan baseline-shift="sub" font-size="11">\2</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)
def boxt(x, y, w, h, lines, *a, **k): return _boxt(x, y, w, h, [_sub(l) for l in lines], *a, **k)


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


def fmt(v):
    return neg(f'{v:g}')


def arcpath(cx, cy, r, a0, a1, c=AC, w=2, dash=None, n=40):
    """arc of a circle from angle a0 to a1 (degrees, 0 = +x, measured clockwise because y points down)"""
    pts = [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    return P(pts, c, w, dash)


def circ(cx, cy, r, c=AC, w=2, dash=None, fill='none'):
    d = f';stroke-dasharray:{dash}' if dash else ''
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" style="fill:{fill};stroke:{c};stroke-width:{w}{d}"/>'


def poly(pts, fill=PANEL, stroke=AC, w=2):
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" style="fill:{fill};stroke:{stroke};stroke-width:{w};stroke-linejoin:round"/>'


# ---- 7.1 the spur pair of the worked examples (m = 4, z = 20 and 60), to scale 3 px per mm ----
def f1():
    o = []
    s = 3.0
    px, py = 300, 268
    phi = math.radians(20)
    r1, r2, ra1, ra2 = 40, 120, 44, 124
    rb1, rb2 = r1 * math.cos(phi), r2 * math.cos(phi)
    o1 = (px, py - r1 * s)
    o2y = py + r2 * s
    # gear circles (only the part near the mesh)
    def garc(r, c, w, dash=None):
        lim = math.degrees(math.asin(min(0.999, 280 / (r * s))))
        return arcpath(px, o2y, r * s, -90 - lim, -90 + lim, c, w, dash)
    o.append(garc(ra2, L2, 1.5, '3 4'))
    o.append(garc(r2, AC, 2.5))
    o.append(garc(rb2, LV, 2, '7 5'))
    o.append(circ(o1[0], o1[1], ra1 * s, L2, 1.5, '3 4'))
    o.append(circ(o1[0], o1[1], r1 * s, AC, 2.5))
    o.append(circ(o1[0], o1[1], rb1 * s, LV, 2, '7 5'))
    # line of centres
    o.append(L(px, o1[1], px, 352, L2, 1.5, dash='6 5'))
    o.append(C(o1[0], o1[1], 4, INK))
    o.append(T(px + 10, o1[1] + 5, 'O_1', 14, 'start', bold=True))
    o.append(L(px, 334, px, 360, L2, 1.5, arrow='m'))
    o.append(T(px + 10, 354, 'to O_2 (a = 160 mm)', 13, 'start', fill=MUT))
    # line of action through P at 20 degrees, tangent to both base circles
    u = (math.cos(phi), math.sin(phi))
    t1 = (px - r1 * math.sin(phi) * s * u[0], py - r1 * math.sin(phi) * s * u[1])
    t2 = (px + r2 * math.sin(phi) * s * u[0], py + r2 * math.sin(phi) * s * u[1])
    e1 = (px - 175 * u[0], py - 175 * u[1])
    e2 = (px + 150 * u[0], py + 150 * u[1])
    o.append(L(e1[0], e1[1], e2[0], e2[1], NX, 2))
    o.append(T(e1[0] - 8, e1[1] + 4, 'line of action', 14, 'end', fill=NX, bold=True))
    a_ = (px - 10.537 * s * u[0], py - 10.537 * s * u[1])
    b_ = (px + 9.192 * s * u[0], py + 9.192 * s * u[1])
    o.append(L(a_[0], a_[1], b_[0], b_[1], INK, 6))
    o.append(C(t1[0], t1[1], 4, LV)); o.append(C(t2[0], t2[1], 4, LV))
    o.append(L(o1[0], o1[1], t1[0], t1[1], LV, 1.5, dash='4 4'))
    # common tangent at P and the pressure angle
    o.append(L(px - 120, py, px + 170, py, L2, 1.5, dash='4 4'))
    o.append(arcpath(px, py, 70, 0, 20, INK, 1.5))
    o.append(T(px + 80, py + 11, 'φ = 20°', 14, 'start', bold=True))
    o.append(C(px, py, 5, INK))
    o.append(Tb(px - 12, py - 12, 'P', 15, 'end', bold=True))
    # labels
    for i, (t, c, b) in enumerate((('pinion', INK, True), ('z_1 = 20, d_1 = 80 mm', INK, False), ('base d_b1 = 75.18 (dashed)', LV, False), ('tips d_a1 = 88 (dotted)', MUT, False))):
        o.append(T(16, 30 + 20 * i, t, 14 if i == 0 else 13, 'start', fill=c, bold=b))
    o.append(T(px, 398, 'gear: z_2 = 60, d_2 = 240 mm', 14, bold=True))
    o.append(T(px, 418, 'base circle d_b2 = 225.53 mm (dashed)', 13, fill=LV))
    o.append(T(470, 40, 'm = 4 mm, a = 160 mm', 14, 'start', bold=True))
    o.append(T(470, 62, 'ratio z_2/z_1 = 3', 14, 'start'))
    o.append(T(470, 150, 'path of contact (thick):', 13, 'start'))
    o.append(T(470, 170, '10.54 + 9.19 = 19.73 mm', 14, 'start', bold=True))
    o.append(T(470, 190, 'contact ratio 19.73/11.81 = 1.67', 13, 'start'))
    return 432, ''.join(o)


# ---- 7.2 case and core, and why the pinion is made harder ----
def f2():
    o = []
    # a tooth on its rim, with a hard case along the flanks
    base, top = 300, 70
    xl0, xl1, xr0, xr1 = 60, 112, 268, 216
    tooth = [(20, base + 20), (20, base), (xl0, base), (xl1, top), (xr1, top), (xr0, base), (300, base), (300, base + 20)]
    o.append(poly(tooth, ACS, AC, 2))
    case = [(xl0 - 2, base), (xl1 - 2, top - 2), (xr1 + 2, top - 2), (xr0 + 2, base), (xr0 - 12, base), (xr1 - 6, top + 8), (xl1 + 6, top + 8), (xl0 + 12, base)]
    o.append(poly(case, NX, NX, 1))
    o.append(T(164, 190, 'tough core', 14, bold=True))
    o.append(T(164, 210, '30–40 HRC', 13))
    o.append(L(286, 120, 252, 150, NX, 1.5, arrow='x'))
    o.append(T(292, 112, 'hard case 58–62 HRC', 13, 'start', fill=NX, bold=True))
    o.append(T(292, 130, '0.8–1.5 mm: resists pitting', 13, 'start', fill=NX))
    o.append(C(xl0 + 4, base - 4, 6, LV))
    o.append(L(xl0 + 2, base + 4, 44, 330, LV, 1.5))
    o.append(T(16, 344, 'root fillet: bending cracks start here', 13, 'start', fill=LV, bold=True))
    o.append(T(160, 40, 'carburised tooth', 14, bold=True))
    # cycles bar chart from worked example 2
    x0, x1, y0, y1 = 486, 704, 70, 290
    fy = lin(0, 10, y1, y0)
    o.append(axes(x0, x1, y0, y1, [], [0, 2, 4, 6, 8, 10], lambda v: v, fy, '', 'cycles in 10 000 h, × 10⁸', str, fmt))
    o.append(R(512, fy(8.64), 70, y1 - fy(8.64), NXS, NX, 3))
    o.append(R(616, fy(2.88), 70, y1 - fy(2.88), ACS, AC, 3))
    o.append(T(547, fy(8.64) - 8, '8.64', 14, bold=True))
    o.append(T(651, fy(2.88) - 8, '2.88', 14, bold=True))
    o.append(T(547, y1 + 20, 'pinion', 14))
    o.append(T(547, y1 + 38, '1440 rpm', 13, fill=MUT))
    o.append(T(651, y1 + 20, 'gear', 14))
    o.append(T(651, y1 + 38, '480 rpm', 13, fill=MUT))
    return 356, ''.join(o)


# ---- 7.3 Lewis cantilever and the checks of worked example 2 ----
def f3():
    o = []
    # tooth with load at the tip and the inscribed parabola
    base, top = 300, 80
    o.append(poly([(20, base + 18), (20, base), (60, base), (106, top), (184, top), (230, base), (270, base), (270, base + 18)], ACS, AC, 2))
    k_ = 85 / math.sqrt(base - top)
    for sg in (-1, 1):
        o.append(P([(145 + sg * k_ * math.sqrt(y - top), y) for y in range(top, base + 1, 5)], LV, 2, dash='6 4'))
    o.append(L(30, top, 100, top, NX, 3, arrow='x'))
    o.append(T(18, top - 18, 'F_t at the tip', 14, 'start', fill=NX, bold=True))
    o.append(L(60, base, 230, base, INK, 1.5))
    o.append(T(145, base + 40, 'root section: largest stress', 13, fill=INK))
    o.append(L(186, 200, 236, 200, LV, 1.5))
    o.append(T(240, 196, 'parabola of', 13, 'start', fill=LV))
    o.append(T(240, 214, 'uniform strength', 13, 'start', fill=LV))
    o.append(T(145, 362, 'S_b = σ_b b m Y', 15, bold=True))
    # bars: capacities against the required load
    x0, x1, y0, y1 = 380, 704, 60, 300
    fy = lin(0, 12000, y1, y0)
    o.append(axes(x0, x1, y0, y1, [], [0, 3000, 6000, 9000, 12000], lambda v: v, fy, '', 'load (N)', str, fmt))
    bars = [(10896, 'S_b', 'bending', ACS, AC), (6912, 'S_w', '300 BHN', NXS, NX), (11090, 'S_w', '380 BHN', ACS, AC)]
    for i, (v, nm, sub, fl, st) in enumerate(bars):
        x = 410 + i * 100
        o.append(R(x, fy(v), 70, y1 - fy(v), fl, st, 3))
        o.append(T(x + 35, fy(v) + 22, f'{v:,}'.replace(',', ' '), 13, bold=True))
        o.append(T(x + 35, fy(v) + 40, 'fails' if v < 10737 else 'passes', 13, fill=st))
        o.append(T(x + 35, y1 + 20, nm, 14, bold=True))
        o.append(T(x + 35, y1 + 38, sub, 13, fill=MUT))
    o.append(L(x0, fy(10737), x1, fy(10737), INK, 2, dash='7 5'))
    o.append(T(x1, fy(10737) - 16, 'needed: 1.5 × F_eff = 10 737 N', 13, 'end', bold=True))
    return 372, ''.join(o)


# ---- 7.4 force components on the helical pinion of the worked example ----
def f4():
    o = []
    # side view of the pinion to scale (4 px per mm): face width 45 mm across, pitch diameter 62.12 mm high
    x0, y0, w, h = 80, 70, 180, 248
    o.append(R(x0, y0, w, h, ACS, AC, 4))
    t = math.tan(math.radians(15))
    for i in range(-2, 11):
        ya = y0 + 12 + i * 26          # tooth line enters at the left edge at ya and rises to the right
        yb = ya - w * t
        a, b = (x0, ya), (x0 + w, yb)
        if ya > y0 + h:                 # clip at the bottom edge
            a = (x0 + (ya - y0 - h) / t, y0 + h)
        if yb < y0:                     # clip at the top edge
            b = (x0 + (ya - y0) / t, y0)
        if a[0] >= b[0]: continue
        o.append(L(a[0], a[1], b[0], b[1], AC, 2))
    o.append(L(x0 - 40, y0 + h / 2, x0 + w + 40, y0 + h / 2, L2, 1.5, dash='8 5'))
    o.append(T(x0 + w + 46, y0 + h / 2 + 5, 'shaft axis', 13, 'start', fill=MUT))
    ya = y0 + 12 + 4 * 26
    o.append(L(x0, ya, x0 + 110, ya, INK, 1.5, dash='4 4'))
    o.append(arcpath(x0, ya, 96, -15, 0, INK, 1.5))
    o.append(Tb(x0 + 124, ya - 6, 'ψ = 15°', 14, 'start', bold=True))
    o.append(T(x0 + w / 2, y0 - 34, 'b = 45 mm', 14, bold=True))
    o.append(T(x0 + w / 2, y0 - 14, 'pinion from the side, d_1 = 62.12 mm', 13, fill=MUT))
    # force arrows at a point of the pitch line
    cx, cy = 520, 200
    o.append(C(cx, cy, 5, INK))
    o.append(L(cx, cy, cx, cy - 120, NX, 3, arrow='x'))
    o.append(T(cx + 10, cy - 110, 'F_t = 2332 N', 14, 'start', fill=NX, bold=True))
    o.append(T(cx + 10, cy - 92, 'turns the gear', 13, 'start', fill=MUT))
    o.append(L(cx, cy, cx + 150 * 625 / 2332 * 2, cy, LV, 3, arrow='l'))
    o.append(T(cx + 10, cy + 26, 'F_a = F_t tan ψ = 625 N', 14, 'start', fill=LV, bold=True))
    o.append(T(cx + 10, cy + 44, 'pushes along the shaft', 13, 'start', fill=MUT))
    o.append(L(cx, cy, cx - 120 * 879 / 2332 * 2, cy + 60, AC, 3, arrow='n'))
    o.append(T(cx - 110, cy + 84, 'F_r = 879 N', 14, 'middle', fill=AC, bold=True))
    o.append(T(cx - 110, cy + 102, 'towards the centre', 13, 'middle', fill=MUT))
    o.append(T(560, 334, 'the thrust goes to a bearing that', 13, fill=INK))
    o.append(T(560, 352, 'can take it (angular contact, taper roller)', 13, fill=INK))
    return 366, ''.join(o)


# ---- 7.5 the pitch cones of the bevel pair, to scale (3 px per mm) ----
def f5():
    o = []
    s = 3.0
    ox, oy = 120, 180
    g1 = math.atan(0.5)
    R_ = math.sqrt(8000)
    px, py = ox + R_ * s * math.cos(g1), oy + R_ * s * math.sin(g1)
    pt = (px, 2 * oy - py)
    # pinion pitch cone (both halves) and gear cone (right half)
    o.append(poly([(ox, oy), (px, py), (pt[0], pt[1])], ACS, AC, 2))
    o.append(poly([(ox, oy), (px, py), (ox, py)], LVS, LV, 2))
    # axes
    o.append(L(ox - 10, oy, 560, oy, L2, 1.5, dash='8 5'))
    o.append(T(566, oy + 5, 'pinion axis', 13, 'start', fill=MUT))
    o.append(L(ox, oy - 120, ox, 396, L2, 1.5, dash='8 5'))
    o.append(T(ox - 8, 72, 'gear axis', 13, 'end', fill=MUT))
    o.append(C(ox, oy, 5, INK)); o.append(T(ox - 12, oy - 8, 'apex', 13, 'end', bold=True))
    # face width band along the pitch line
    ux, uy = math.cos(g1), math.sin(g1)
    a = (R_ - 25) * s
    o.append(L(ox + a * ux, oy + a * uy, px, py, NX, 7))
    am = (R_ - 12.5) * s
    mx, my = ox + am * ux, oy + am * uy
    o.append(C(mx, my, 5, NX))
    o.append(L(mx, my, mx, oy, NX, 1.5, dash='4 3'))
    o.append(T(mx - 6, (my + oy) / 2 - 8, 'r_m1 = 34.41', 13, 'end', fill=NX, bold=True))
    # back cone at the large end: perpendicular to the pitch line through P
    o.append(L(px - 60 * uy, py + 60 * ux, px + 50 * uy, py - 50 * ux, INK, 1.5, dash='5 4'))
    o.append(T(px + 56 * uy + 6, py - 56 * ux, 'back cone', 13, 'start', fill=MUT))
    o.append(C(px, py, 5, INK)); o.append(T(px + 10, py + 18, 'P', 14, 'start', bold=True))
    # angle marks
    o.append(arcpath(ox, oy, 80, 0, math.degrees(g1), INK, 1.5))
    o.append(T(ox + 92, oy + 26, 'γ_1 = 26.57°', 14, 'start', bold=True))
    o.append(arcpath(ox, oy, 50, math.degrees(g1), 90, INK, 1.5))
    o.append(T(ox + 18, oy + 92, 'γ_2 = 63.43°', 14, 'start', bold=True))
    # labels
    o.append(T(470, 236, 'cone distance R = 89.44 mm', 14, 'start', bold=True))
    o.append(T(470, 256, 'face width b = 25 mm (thick)', 13, 'start', fill=NX))
    o.append(T(470, 276, 'b ≤ R/3 = 29.81 mm', 13, 'start', fill=NX))
    o.append(T(470, 40, 'pinion: z_1 = 20, d_1 = 80 mm', 14, 'start', fill=AC, bold=True))
    o.append(T(470, 60, 'z_v1 = 20/cos γ_1 = 22.36', 13, 'start'))
    o.append(T(470, 346, 'gear: z_2 = 40, d_2 = 160 mm', 14, 'start', fill=LV, bold=True))
    o.append(T(470, 366, 'z_v2 = 40/cos γ_2 = 89.44', 13, 'start'))
    return 404, ''.join(o)


# ---- 7.6 worm efficiency against lead angle (computed), with the worked example ----
def f6():
    o = []
    x0, x1, y0, y1 = 80, 690, 40, 300
    fx = lin(0, 40, x0, x1); fy = lin(0, 100, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0, 5, 10, 15, 20, 25, 30, 35, 40], [0, 20, 40, 60, 80, 100], fx, fy,
                  'lead angle λ (degrees)', 'efficiency η (%)', fmt, fmt))
    an = math.radians(20)
    def eta(l, mu):
        l = math.radians(l)
        return 100 * (math.cos(an) - mu * math.tan(l)) / (math.cos(an) + mu / math.tan(l))
    for mu, c, dash, lab, lx in ((0.03, AC, None, 'μ = 0.03', 30), (0.10, NX, '7 5', 'μ = 0.10', 30)):
        pts = [(fx(l), fy(eta(l, mu))) for l in [0.5 + i * 0.5 for i in range(79)] if eta(l, mu) > 0]
        o.append(P(pts, c, 2.5, dash))
        o.append(Tb(fx(lx), fy(eta(lx, mu)) + 22, lab, 14, fill=c, bold=True))
    o.append(L(x0, fy(50), x1, fy(50), L2, 1.5, dash='3 4'))
    o.append(T(x1, fy(50) + 18, 'η = 50 %', 13, 'end', fill=MUT))
    lam = math.degrees(math.atan(0.1))
    o.append(C(fx(lam), fy(eta(lam, 0.03)), 6, LV))
    o.append(Tb(fx(lam) + 14, fy(eta(lam, 0.03)) + 40, 'single start, q = 10: λ = 5.71°, η = 75.6 %', 13, 'start', fill=LV, bold=True))
    l4 = math.degrees(math.atan(0.4))
    o.append(C(fx(l4), fy(eta(l4, 0.03)), 6, LV))
    o.append(Tb(fx(l4), fy(eta(l4, 0.03)) - 14, f'four starts: λ = 21.8°, η = {eta(l4, 0.03):.1f} %', 13, 'middle', fill=LV))
    return 350, ''.join(o)


# ---- 7.7 the hub reducer of worked example 2: ring fixed, sun driven, arm output ----
def f7():
    o = []
    cx, cy, k = 200, 180, 2.4
    rs, rp, rr = 24 * k, 18 * k, 60 * k
    o.append(circ(cx, cy, rr + 14, L2, 1.5, fill=FIGBG))
    o.append(circ(cx, cy, rr + 14, NX, 3, '2 6'))
    o.append(circ(cx, cy, rr, NX, 2.5))
    o.append(circ(cx, cy, rs, AC, 2.5, fill=ACS))
    for i in range(3):
        a = math.radians(-90 + 120 * i)
        px, py = cx + (rs + rp) * math.cos(a), cy + (rs + rp) * math.sin(a)
        o.append(L(cx, cy, px, py, LV, 5))
        o.append(circ(px, py, rp, INK, 2, fill=PANEL))
        o.append(C(px, py, 5, LV))
    o.append(C(cx, cy, 6, INK))
    o.append(T(cx + 28, cy + 30, 'sun', 13, 'middle', fill=AC, bold=True))
    o.append(T(cx, cy - (rs + rp) - 16, 'planet', 13, bold=True))
    o.append(T(cx - 58, cy + 2, 'arm', 13, 'end', fill=LV, bold=True))
    o.append(T(cx, cy + rr + 36, 'ring fixed (60 teeth)', 13, fill=NX, bold=True))
    # results
    rows = [('sun (input)', '24 teeth', '+600 rpm', AC), ('arm (output)', 'carries planets', '+171.4 rpm', LV),
            ('planet', '18 teeth', '−400 rpm', INK), ('ring', '60 teeth, fixed', '0 rpm', NX)]
    y = 64
    o.append(T(410, 40, 'tabular method: x = 428.6, y = 171.4', 14, 'start', bold=True))
    for nm, z, n, c in rows:
        o.append(R(410, y, 294, 46, PANEL, c, 6))
        o.append(T(422, y + 20, nm, 14, 'start', fill=c, bold=True))
        o.append(T(422, y + 38, z, 13, 'start', fill=MUT))
        o.append(T(692, y + 29, n, 14, 'end', bold=True))
        y += 56
    o.append(T(410, 312, 'ratio 600/171.4 = 1 + 60/24 = 3.5', 14, 'start'))
    o.append(T(410, 334, 'torques: sun 47.75, arm 167.1, ring 119.4 N·m', 13, 'start', fill=MUT))
    return 384, ''.join(o)


# ---- 7.8 load spectrum of worked example 1 against its equivalent, average and maximum ----
def f8():
    o = []
    x0, x1, y0, y1 = 80, 640, 40, 290
    fx = lin(0, 100, x0, x1); fy = lin(0, 12, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0, 20, 40, 60, 80, 100], [0, 2, 4, 6, 8, 10, 12], fx, fy,
                  'share of the 10 000 h life (%)', 'power (kW)', fmt, fmt))
    for a, b, p_ in ((0, 60, 10), (60, 90, 6), (90, 100, 2)):
        o.append(R(fx(a), fy(p_), fx(b) - fx(a), y1 - fy(p_), ACS, AC, 2))
        o.append(T((fx(a) + fx(b)) / 2, (fy(p_) + y1) / 2 + 5 if p_ > 3 else fy(p_) - 8, f'{p_} kW', 14, bold=True))
    o.append(L(x0, fy(8.73), x1 + 10, fy(8.73), NX, 2.5))
    o.append(T(x1 + 14, fy(8.73) + 5, 'P_eq 8.73', 14, 'start', fill=NX, bold=True))
    o.append(L(x0, fy(8.0), x1 + 10, fy(8.0), LV, 2, dash='3 4'))
    o.append(T(x1 + 14, fy(8.0) + 14, 'mean 8.0', 13, 'start', fill=LV))
    o.append(L(x0, fy(10), x1 + 10, fy(10), INK, 1.5, dash='7 5'))
    o.append(T(x1 + 14, fy(10) + 5, 'max 10', 13, 'start'))
    o.append(T(360, 368, 'P_eq = (0.6 × 10³ + 0.3 × 6³ + 0.1 × 2³)^1/3 = 665.6^1/3 = 8.73 kW', 13, bold=True)
             .replace('^1/3', '<tspan baseline-shift="super" font-size="11">1/3</tspan>'))
    return 382, ''.join(o)


# ---- 7.9 ray diagram of worked example 2: 6 = 3(1) 2(3), phi = 1.41 ----
def f9():
    o = []
    speeds = [100, 140, 200, 280, 400, 560]
    xs = {'I': 150, 'II': 360, 'III': 570}
    fy = lambda j: 330 - j * 52
    for j, n in enumerate(speeds):
        o.append(L(110, fy(j), 610, fy(j), LN, 1))
        o.append(T(98, fy(j) + 5, f'{n}', 13, 'end', fill=MUT))
    o.append(T(98, 34, 'rpm', 13, 'end', fill=MUT))
    for nm, x in xs.items():
        o.append(L(x, fy(5) - 22, x, fy(0) + 14, L2, 2))
        o.append(T(x, fy(0) + 36, f'shaft {nm}', 14, bold=True))
    # group a: from 560 on I to 560, 400, 280 on II
    ga = [(0, '36/36'), (1, '30/42'), (2, '24/48')]
    for d, lab in ga:
        o.append(L(xs['I'], fy(5), xs['II'], fy(5 - d), AC, 2.5))
    o.append(Tb(255, fy(5) - 8, '36/36', 13, fill=AC, bold=True))
    o.append(Tb(236, fy(4.4) + 8, '30/42', 13, fill=AC, bold=True))
    o.append(Tb(268, fy(3.7) + 10, '24/48', 13, fill=AC, bold=True))
    # group b: from each of 560, 400, 280 on II to the same speed and three steps lower on III
    for j in (5, 4, 3):
        o.append(L(xs['II'], fy(j), xs['III'], fy(j), LV, 2.5))
        o.append(L(xs['II'], fy(j), xs['III'], fy(j - 3), NX, 2.5))
    o.append(Tb(465, fy(5) - 8, '38/38', 13, fill=LV, bold=True))
    o.append(Tb(500, fy(1.2) - 2, '20/56', 13, fill=NX, bold=True))
    for nm, x in xs.items():
        for j in range(6):
            if (nm == 'I' and j == 5) or (nm == 'II' and j >= 3) or nm == 'III':
                o.append(C(x, fy(j), 5, INK))
    o.append(T(600, fy(1) + 24, '142.9 (2 % high)', 13, 'start', fill=NX))
    o.append(T(255, 24, 'group a: 3 ratios, x = 1', 13, fill=AC, bold=True))
    o.append(T(465, 24, 'group b: 2 ratios, x = 3', 13, fill=LV, bold=True))
    o.append(T(620, fy(5) + 5, 'φ = 1.41', 13, 'start', bold=True))
    return 384, ''.join(o)


FIG = {
    1: (f1, 'The pair of the worked examples drawn to scale near the mesh. The two pitch circles touch at the pitch point P; tooth contact always lies on the line of action, the common tangent to the two base circles, at 20° to the common tangent of the pitch circles.',
        'Pinion and gear pitch, base and addendum circles meeting at the pitch point, with the line of action at 20 degrees and the 19.73 millimetre path of contact marked.'),
    2: (f2, 'Left: a carburised tooth has a hard case on its flanks for pitting and a tough core for bending at the root. Right: in worked example 2 each pinion tooth is loaded three times as often as a gear tooth, which is why the pinion is made harder.',
        'Tooth section with a hard case and a tough core, and a bar chart of 8.64 and 2.88 hundred million cycles for pinion and gear.'),
    3: (f3, 'Left: Lewis treats the tooth as a cantilever loaded at the tip. Right: the checks of worked example 2 against the 10 737 N they must exceed. Bending passes; wear fails at 300 BHN and passes at 380 BHN.',
        'Tooth with a tip load and a parabola of uniform strength, and three bars: beam strength 10 896 newtons, wear strength 6912 at 300 BHN and 11 090 at 380 BHN, against a needed 10 737.'),
    4: (f4, 'The helical pinion of the worked example and the three components of its tooth force. The axial thrust F<sub>t</sub> tan ψ is the force a spur gear does not have.',
        'Side view of a helical pinion with teeth at 15 degrees and arrows for the tangential force 2332 newtons, axial thrust 625 newtons and radial force 879 newtons.'),
    5: (f5, 'The pitch cones of the worked example drawn to scale: they meet at one apex and their angles add to 90°. The load acts at the mean radius, in the middle of the face width.',
        'Pinion and gear pitch cones from a common apex with pitch angles 26.57 and 63.43 degrees, cone distance 89.44 millimetres, face width 25 millimetres and mean radius 34.41 millimetres.'),
    6: (f6, 'Worm efficiency computed for a normal pressure angle of 20°. Efficiency rises steeply with lead angle, so a single-start worm loses about a quarter of its power as heat while four starts lose far less.',
        'Two efficiency curves against lead angle for friction 0.03 and 0.10, with points at 5.71 degrees, 75.6 per cent and 21.8 degrees.'),
    7: (f7, 'The hub reducer of worked example 2. The sun drives three planets that roll inside the fixed ring and carry the arm round at 171.4 rpm, a reduction of 3.5.',
        'Planetary train with sun, three planets on an arm and a fixed ring, and a table of speeds: sun 600, arm 171.4, planet minus 400, ring 0 revolutions per minute.'),
    8: (f8, 'The load spectrum of worked example 1. The equivalent power 8.73 kW lies between the mean and the maximum, because contact damage grows with the cube of the load.',
        'Step chart of 10, 6 and 2 kilowatts over 60, 30 and 10 per cent of life, with lines at 8.73, 8.0 and 10 kilowatts.'),
    9: (f9, 'Ray diagram of worked example 2. Shaft I runs at 560 rpm; group a gives three speeds on shaft II, and group b doubles them to the six speeds on shaft III, each reached once.',
        'Ray diagram with three shafts and six speed lines from 100 to 560 revolutions per minute; three rays from shaft I, then two rays from each speed on shaft II.'),
}
spec = make_spec(FIG)
