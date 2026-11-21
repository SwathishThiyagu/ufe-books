"""Claude's hand-drawn figures for ec-antenna-u1 (Antennas, RF and Microwave Engineering: transmission lines, waveguides
and matching), one per chapter, each drawn from that chapter's own worked example and numbers, plus two sketches used in
model answers. The Smith chart is drawn to scale from the real r and x circles. Colours are the shell's CSS variables."""
import os, sys, math, re, cmath
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

_T, _Tb, _boxt = T, Tb, boxt


def _sub(s):
    """Z_0, f_c, l_s ... drawn as real subscripts, never as underscores"""
    return re.sub(r'([A-Za-zθα-ωΓ\)])_([A-Za-z0-9,]+)', r'\1<tspan baseline-shift="sub" font-size="11">\2</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)
def boxt(x, y, w, h, lines, *a, **k): return _boxt(x, y, w, h, [_sub(l) for l in lines], *a, **k)


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


def fmt(v):
    return neg(f'{v:g}')


def dot(x, y, c=INK, r=4):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{c}"/>'


def circ(x, y, r, c=L2, w=1.2, dash=None, fill='none'):
    d = f';stroke-dasharray:{dash}' if dash else ''
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" style="fill:{fill};stroke:{c};stroke-width:{w}{d}"/>'


def res_h(x1, x2, y, c=AC, n=6, amp=7):
    a, b = x1 + 8, x2 - 8
    pts = [(x1, y), (a, y)]
    for i in range(n):
        pts.append((a + (b - a) * (i + 0.5) / n, y + (amp if i % 2 == 0 else -amp)))
    pts += [(b, y), (x2, y)]
    return P(pts, c, 2)


def res_v(x, y1, y2, c=AC, n=6, amp=7):
    a, b = y1 + 8, y2 - 8
    pts = [(x, y1), (x, a)]
    for i in range(n):
        pts.append((x + (amp if i % 2 == 0 else -amp), a + (b - a) * (i + 0.5) / n))
    pts += [(x, b), (x, y2)]
    return P(pts, c, 2)


def coil_h(x1, x2, y, c=AC, n=4):
    """series inductor: n bumps between x1 and x2"""
    w = (x2 - x1) / n
    d = f'M{x1:.1f},{y:.1f}' + ''.join(f' a{w / 2:.1f},{w / 2:.1f} 0 0 1 {w:.1f},0' for _ in range(n))
    return f'<path d="{d}" style="fill:none;stroke:{c};stroke-width:2"/>'


def cap_v(x, y1, y2, c=AC, gap=8, w=28):
    m = (y1 + y2) / 2
    return (L(x, y1, x, m - gap / 2, INK, 2) + L(x - w / 2, m - gap / 2, x + w / 2, m - gap / 2, c, 3) +
            L(x - w / 2, m + gap / 2, x + w / 2, m + gap / 2, c, 3) + L(x, m + gap / 2, x, y2, INK, 2))


# ---- 1.1 one slice Δz of a line, with worked example 2's per-metre values ----
def f1():
    o = []
    yt, yb = 70, 190
    o.append(L(40, yt, 110, yt, INK, 2)); o.append(res_h(110, 200, yt))
    o.append(L(200, yt, 230, yt, INK, 2)); o.append(coil_h(230, 330, yt))
    o.append(L(330, yt, 680, yt, INK, 2)); o.append(L(40, yb, 680, yb, INK, 2))
    o.append(T(155, yt - 18, 'R Δz', 15, bold=True)); o.append(T(280, yt - 22, 'L Δz', 15, bold=True))
    o.append(dot(420, yt)); o.append(dot(420, yb)); o.append(dot(540, yt)); o.append(dot(540, yb))
    o.append(res_v(420, yt, yb)); o.append(T(436, 135, 'G Δz', 15, 'start', bold=True))
    o.append(cap_v(540, yt, yb)); o.append(T(562, 135, 'C Δz', 15, 'start', bold=True))
    o.append(dot(40, yt)); o.append(dot(40, yb)); o.append(dot(680, yt)); o.append(dot(680, yb))
    o.append(L(52, 100, 52, 160, NX, 2, arrow='x')); o.append(T(62, 136, 'v(z)', 14, 'start', NX))
    o.append(L(668, 100, 668, 160, NX, 2, arrow='x')); o.append(T(658, 136, 'v(z + Δz)', 14, 'end', NX))
    o.append(L(60, yt - 14, 98, yt - 14, LV, 2, arrow='l')); o.append(T(62, yt - 22, 'i(z)', 14, 'start', LV))
    o.append(L(600, yt - 14, 650, yt - 14, LV, 2, arrow='l')); o.append(T(648, yt - 22, 'i(z + Δz)', 14, 'end', LV))
    o.append(brace(40, 680, yb + 16, MUT, up=False)); o.append(T(360, yb + 42, 'one slice of length Δz; let Δz → 0', 14, fill=MUT))
    o.append(boxt(40, 250, 300, 88, ['Worked example 2, 10 MHz', 'R + jωL = 0.1 + j15.71 Ω/m', 'G + jωC = 10 µS + j6.28 mS/m'], ACS, AC, 14, True))
    o.append(boxt(380, 250, 300, 88, ['Secondary constants', 'Z_0 = 50.0∠−0.14° Ω', 'γ = 0.00125 + j0.3142 m⁻¹'], LVS, LV, 14, True))
    o.append(L(342, 294, 376, 294, INK, 2, arrow='n'))
    return 352, ''.join(o)


# ---- 1.2 standing wave of the worked example: |Γ| = 0.447 at 26.57° ----
def f2():
    o = []
    m, th = 0.4472136, math.radians(26.565)
    x0, x1, y0, y1 = 80, 690, 40, 300
    fx = lin(0, 0.75, x0, x1); fy = lin(0, 1.6, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75], [0, 0.4, 0.8, 1.2, 1.6], fx, fy,
                  'distance from the load d/λ (towards the generator →)', '|V(d)| / |V+|', fmt, fmt))
    pts = [(fx(x), fy(math.sqrt(1 + m * m + 2 * m * math.cos(th - 4 * math.pi * x)))) for x in [i * 0.75 / 240 for i in range(241)]]
    o.append(P(pts, AC, 3))
    for xm in (0.0369, 0.5369):
        o.append(L(fx(xm), fy(1.447), fx(xm), y1, NX, 1.4, dash='4 4')); o.append(C(fx(xm), fy(1.447), 5, NX))
    for xn in (0.2869,):
        o.append(L(fx(xn), fy(0.553), fx(xn), y1, LV, 1.4, dash='4 4')); o.append(C(fx(xn), fy(0.553), 5, LV))
    o.append(Tb(fx(0.0369) + 10, fy(1.447) - 12, 'Vmax = 1.447 at 0.037λ', 14, 'start', NX, True))
    o.append(Tb(fx(0.2869), fy(0.553) + 24, 'Vmin = 0.553 at 0.287λ', 14, fill=LV, bold=True))
    yb = fy(1.52)
    o.append(L(fx(0.0369), fy(0.15), fx(0.2869), fy(0.15), INK, 1.5, arrow='x')); o.append(L(fx(0.2869), fy(0.15), fx(0.0369), fy(0.15), INK, 1.5, arrow='x'))
    o.append(Tb(fx(0.162), fy(0.15) - 7, 'λ/4', 14))
    o.append(L(fx(0.5369), fy(1.25), fx(0.0369), fy(1.25), MUT, 1.5, arrow='m'))
    o.append(Tb(fx(0.42), fy(1.25) - 8, 'pattern repeats every λ/2', 13, fill=MUT))
    o.append(Tb(x1, fy(0.25), 'VSWR = 1.447 / 0.553 = 2.62', 14, 'end', bold=True))
    return 352, ''.join(o)


# ---- 1.3 reactance of shorted and open 50 Ω stubs, with worked example 2's 3 cm stub at 1 GHz ----
def f3():
    o = []
    x0, x1, y0, y1 = 80, 690, 34, 330
    fx = lin(0, 0.5, x0, x1); fy = lin(-4, 4, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5], [-4, -2, 0, 2, 4], fx, fy, 'stub length d/λ', _sub('X_in / Z_0'), fmt, fmt))
    o.append(L(x0, fy(0), x1, fy(0), INK, 1.5))
    sh = [(fx(x), fy(math.tan(2 * math.pi * x))) for x in [i * 0.5 / 400 for i in range(401)] if abs(math.tan(2 * math.pi * x)) <= 4.05 and x != 0.25]
    a = [p for p in sh if p[0] < fx(0.25)]; b = [p for p in sh if p[0] > fx(0.25)]
    o.append(P(a, AC, 3)); o.append(P(b, AC, 3))
    op = [(fx(x), fy(-1 / math.tan(2 * math.pi * x))) for x in [i * 0.5 / 400 for i in range(1, 400)] if abs(1 / math.tan(2 * math.pi * x)) <= 4.05]
    o.append(P(op, NX, 3, dash='8 5'))
    o.append(L(fx(0.25), y0, fx(0.25), y1, MUT, 1.2, dash='3 5'))
    o.append(L(fx(0.15), y0 + 14, fx(0.15), y1, MUT, 1.2, dash='3 5'))
    o.append(C(fx(0.15), fy(1.376), 6, AC)); o.append(C(fx(0.15), fy(-0.727), 6, NX))
    o.append(boxt(402, 36, 196, 62, ['at 0.15λ (3 cm, 1 GHz):', 'short: +j68.8 Ω, 10.95 nH', 'open: −j36.3 Ω, 4.38 pF'], PANEL, L2, 13, fills=[INK, AC, NX]))
    o.append(Tb(fx(0.25), fy(-3.4), 'λ/4: short ↔ open', 13, fill=MUT))
    o.append(Tb(fx(0.06), fy(1.2), 'inductive', 13, fill=MUT)); o.append(Tb(fx(0.06), fy(-1.2), 'capacitive', 13, fill=MUT))
    o.append(T(fx(0.07), fy(3.4), 'solid: shorted', 13, 'start', AC, True)); o.append(T(fx(0.07), fy(2.8), 'dashed: open', 13, 'start', NX, True))
    return 382, ''.join(o)


# ---- 1.4 quarter-wave transformer of the worked example and its |Γ| against frequency ----
def f4():
    o = []
    y = 70
    o.append(boxt(40, y - 26, 170, 52, ['50 Ω line'], PANEL, L2, 14))
    o.append(boxt(230, y - 30, 250, 60, ['λ/4 section, Z_0′ = 70.71 Ω', 'l = 2.08 cm at 2.4 GHz'], ACS, AC, 14))
    o.append(boxt(500, y - 26, 180, 52, ['load R_L = 100 Ω'], PANEL, L2, 14))
    o.append(L(210, y, 228, y, INK, 2)); o.append(L(480, y, 498, y, INK, 2))
    o.append(T(355, y + 50, 'Z_in = 70.71² / 100 = 50 Ω', 14, fill=LV, bold=True))
    x0, x1, y0, y1 = 80, 690, 150, 370
    fx = lin(0, 3.2, x0, x1); fy = lin(0, 0.4, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.5, 1, 1.5, 2, 2.5, 3], [0, 0.1, 0.2, 0.3, 0.4], fx, fy, _sub('f / f_0'), '|Γ| at the input', fmt, fmt))
    lo, hi = 0.6082, 1.3918
    o.append(f'<rect x="{fx(lo):.1f}" y="{y0:.1f}" width="{fx(hi) - fx(lo):.1f}" height="{y1 - y0:.1f}" style="fill:var(--live-soft);stroke:none"/>')
    o.append(f'<rect x="{fx(3 - (hi - 1)):.1f}" y="{y0:.1f}" width="{x1 - fx(3 - (hi - 1)):.1f}" height="{y1 - y0:.1f}" style="fill:var(--live-soft);stroke:none"/>')
    zp = math.sqrt(5000)
    def g(x):
        t = math.tan(math.pi / 2 * x)
        zi = zp * (100 + 1j * zp * t) / (zp + 1j * 100 * t)
        return abs((zi - 50) / (zi + 50))
    pts = [(fx(x), fy(g(x))) for x in [i * 3.2 / 320 for i in range(321)] if abs(math.cos(math.pi / 2 * x)) > 1e-9]
    o.append(P(pts, AC, 3))
    o.append(L(x0, fy(0.2), x1, fy(0.2), NX, 1.5, dash='6 4'))
    o.append(T(x0 + 8, fy(0.2) + 18, '|Γ| = 0.2 limit', 13, 'start', NX))
    o.append(Tb(fx(1), fy(0.36), 'VSWR ≤ 1.5 from 0.61 f_0 to 1.39 f_0', 14, fill=LV, bold=True))
    o.append(Tb(fx(1), fy(0.3), '1.46 to 3.34 GHz', 13, fill=LV))
    o.append(Tb(x1, fy(0.36), 'matched again at 3f_0', 13, 'end', MUT))
    return 428, ''.join(o)


# ---- 1.5 a Smith chart drawn to scale with a single shunt-stub match ----
def smith(zl, d_lab, ls_lab, which=0, cx=250, cy=226, rad=180):
    """zl: normalized load. Draws the impedance chart (used for admittance after the 180° turn), the VSWR circle,
    the turn to g = 1 and the shorted stub. which: 0 for the first crossing of g = 1."""
    o = []
    X = lambda g: cx + g.real * rad
    Y = lambda g: cy - g.imag * rad
    o.append(f'<clipPath id="UID-sc"><circle cx="{cx}" cy="{cy}" r="{rad}"/></clipPath>')
    o.append(circ(cx, cy, rad, INK, 2, fill='var(--panel)'))
    g_ = ['<g clip-path="url(#UID-sc)">']
    for r in (0.2, 0.5, 2, 5):
        g_.append(circ(X(r / (1 + r)), cy, rad / (1 + r), L2, 1.1))
    for x in (0.2, 0.5, 1, 2, 5):
        for s in (1, -1):
            g_.append(circ(X(1), Y(1j * s / x), rad / x, L2, 1.1))
    g_.append('</g>')
    o.append(''.join(g_))
    o.append(L(cx - rad, cy, cx + rad, cy, L2, 1.2))
    o.append(circ(X(0.5), cy, rad / 2, LV, 2.5))   # g = 1 circle
    # scale labels on the real axis (r values)
    for r in (0.2, 0.5, 1, 2, 5):
        xx = X((r - 1) / (r + 1))
        o.append(T(xx + 3, cy + 15, fmt(r), 13, 'start', MUT))
    # wavelengths-toward-generator marks on the rim
    for w, lab, dx, dy, an in ((0.0, '0, 0.5λ', -8, 5, 'end'), (0.125, '0.125λ', 0, -10, 'middle'), (0.25, '0.25λ', 8, 5, 'start'), (0.375, '0.375λ', 0, 22, 'middle')):
        ang = math.pi - 4 * math.pi * w
        gx, gy = X(cmath.exp(1j * ang)), Y(cmath.exp(1j * ang))
        o.append(T(gx + dx, gy + dy, lab, 13, an, MUT))
    GL = (zl - 1) / (zl + 1); m = abs(GL)
    yl = 1 / zl; GY = (yl - 1) / (yl + 1)
    o.append(circ(cx, cy, m * rad, NX, 2, dash='7 5'))
    # crossings of the |Γ| circle with g = 1: Γ = u + jv with (u − 0.5)² + v² = 0.25 and u² + v² = m²  ->  u = m²
    u = m * m; v = math.sqrt(max(m * m - u * u, 0))
    crs = [complex(u, v), complex(u, -v)]
    tgt = crs[which]
    a0, a1 = cmath.phase(GY), cmath.phase(tgt)
    if a1 > a0: a1 -= 2 * math.pi
    arcpts = [(X(m * cmath.exp(1j * (a0 + (a1 - a0) * t / 60))), Y(m * cmath.exp(1j * (a0 + (a1 - a0) * t / 60)))) for t in range(61)]
    o.append(P(arcpts[:-3], AC, 3.5)); o.append(L(*arcpts[-4], *arcpts[-2], AC, 3.5, arrow='n'))
    # stub: from the short (Γ = +1) clockwise along the rim to the point b = −b(d)
    b = ((1 + tgt) / (1 - tgt)).imag  # normalized susceptance at the crossing, read as admittance
    ys = complex(0, -b); Gs = (ys - 1) / (ys + 1)
    s0, s1 = 0.0, cmath.phase(Gs)
    if s1 > s0: s1 -= 2 * math.pi
    sp = [(X(1.0 * cmath.exp(1j * (s0 + (s1 - s0) * t / 50))), Y(1.0 * cmath.exp(1j * (s0 + (s1 - s0) * t / 50)))) for t in range(51)]
    o.append(P(sp[:-3], LV, 4)); o.append(L(*sp[-4], *sp[-2], LV, 4, arrow='l'))
    o.append(dot(X(GL), Y(GL), INK, 5)); o.append(dot(X(GY), Y(GY), AC, 6)); o.append(dot(X(tgt), Y(tgt), LV, 6))
    o.append(dot(X(1), cy, LV, 6)); o.append(dot(X(Gs), Y(Gs), LV, 6))
    return o, dict(GL=GL, GY=GY, tgt=tgt, Gs=Gs, X=X, Y=Y, m=m, b=b)


def f5():
    o, q = smith(complex(2, 1), '0.199λ', '0.125λ')
    X, Y = q['X'], q['Y']
    o.append(Tb(X(q['GL']) + 10, Y(q['GL']) - 10, 'z_L = 2 + j1', 14, 'start', INK, True))
    o.append(Tb(X(q['GY']) - 10, Y(q['GY']) + 22, 'y_L = 0.4 − j0.2', 14, 'end', AC, True))
    o.append(Tb(X(q['tgt']) + 12, Y(q['tgt']) - 10, 'y = 1 + j1', 14, 'start', LV, True))
    o.append(Tb(X(q['Gs']) + 12, Y(q['Gs']) + 6, 'stub: −j1', 14, 'start', LV, True))
    o.append(Tb(X(1) - 8, Y(0) + 30, 'short', 13, 'end', LV))
    o.append(Tb(X(-0.6), Y(0.3j), 'd = 0.199λ', 14, fill=AC, bold=True))
    o.append(Tb(X(0.42), Y(-0.6j), 'l_s = 0.125λ', 14, 'start', LV, True))
    px = 486
    lines = [(0, '100 + j50 Ω on a 50 Ω line', INK, True), (0, '1. z_L = 2 + j1, |Γ| = 0.447', INK, False),
             (1, 'dashed circle: VSWR 2.62', NX, False), (0, '2. y_L opposite: WTG 0.463λ', AC, False),
             (0, '3. clockwise to g = 1:', LV, False), (1, 'y = 1 + j1 at WTG 0.162λ', LV, False),
             (1, 'd = 0.037λ + 0.162λ', AC, True), (2, '= 0.199λ', AC, True), (0, '4. stub must add −j1:', LV, False),
             (1, 'short 0.250λ → 0.375λ', LV, False), (1, 'l_s = 0.125λ', LV, True),
             (0, 'Formula answer: d = 0.1988λ', MUT, False), (0, 'and l_s = λ/8. They agree.', MUT, False)]
    for i, (ind, t, c, bb) in enumerate(lines):
        o.append(T(px + 16 * ind, 40 + i * 26, t, 13, 'start', c, bb))
    return 450, ''.join(o)


# ---- 1.6 microstrip of the worked example, to scale (60 px per mm) ----
def f6():
    o = []
    s = 60; cx = 300; yg = 250; h = 1.6 * s; W = 3 * s
    ys = yg - h
    o.append(R(40, ys, 520, h, NXS, 'none', 0, 0))
    o.append(R(40, yg, 520, 12, INK, INK, 0, 0))
    o.append(R(cx - W / 2, ys - 10, W, 10, AC, AC, 0, 0))
    # field lines from the strip to the ground
    for xs, xe, bend in ((cx - 60, cx - 60, 0), (cx, cx, 0), (cx + 60, cx + 60, 0)):
        o.append(L(xs, ys + 2, xe, yg - 4, LV, 1.8, arrow='l'))
    for sgn in (1, -1):
        for k_, (xe, top) in enumerate(((160, 60), (230, 38))):
            x_s = cx + sgn * (W / 2 - 4)
            xe_ = cx + sgn * xe
            o.append(f'<path d="M{x_s:.1f},{ys - 8:.1f} C{x_s + sgn * top:.1f},{ys - top - 6:.1f} {xe_:.1f},{ys - 20:.1f} {xe_:.1f},{yg - 4:.1f}" style="fill:none;stroke:var(--live);stroke-width:1.8" marker-end="url(#ar-UID-l)"/>')
    o.append(L(cx - W / 2, ys - 32, cx + W / 2, ys - 32, INK, 1.5, arrow='x'))
    o.append(L(cx + W / 2, ys - 32, cx - W / 2, ys - 32, INK, 1.5, arrow='x'))
    o.append(Tb(cx, ys - 40, 'W = 3 mm', 14, bold=True))
    o.append(L(580, ys, 580, yg, INK, 1.5, arrow='x')); o.append(L(580, yg, 580, ys, INK, 1.5, arrow='x'))
    o.append(T(590, (ys + yg) / 2 + 5, 'h = 1.6 mm', 14, 'start', INK, True))
    o.append(T(48, yg + 34, 'substrate (shaded): ε_r = 4.4', 14, 'start', INK, True))
    o.append(T(100, ys - 60, 'air, ε_r = 1', 14, 'start', MUT))
    o.append(T(560, yg + 34, 'ground plane', 14, 'end', MUT))
    o.append(T(cx, 36, 'E-field lines: most in the substrate, some fringe through the air', 13, fill=LV))
    o.append(boxt(40, 310, 640, 54, ['W/h = 1.875  →  ε_eff = 3.32,  Z_0 = 50.8 Ω,  λ_g = 6.86 cm at 2.4 GHz'], ACS, AC, 15))
    return 376, ''.join(o)


# ---- 1.7 cutoff frequencies of the worked example's guide, a = 2.286 cm, b = 1.016 cm ----
def f7():
    o = []
    x0, x1 = 150, 690
    fx = lin(0, 22, x0, x1)
    modes = [('TE10', 6.56), ('TE20', 13.12), ('TE01', 14.76), ('TE11, TM11', 16.16), ('TE30', 19.69), ('TE21, TM21', 19.75)]
    y0 = 52; dy = 38
    yb = y0 + dy * len(modes) + 4
    o.append(f'<rect x="{fx(6.56):.1f}" y="{y0 - 20:.1f}" width="{fx(13.12) - fx(6.56):.1f}" height="{yb - y0 + 20:.1f}" style="fill:var(--live-soft);stroke:none"/>')
    o.append(T((fx(6.56) + fx(13.12)) / 2, y0 - 26, 'single-mode band', 13, fill=LV, bold=True))
    for i, (nm, fcv) in enumerate(modes):
        y = y0 + i * dy + 10
        o.append(T(x0 - 12, y + 5, nm, 14, 'end', INK, True))
        o.append(L(fx(0), y, fx(fcv), y, L2, 2, dash='3 5'))
        o.append(R(fx(fcv), y - 8, x1 - fx(fcv), 16, ACS, AC, 4, 1.5))
        o.append(dot(fx(fcv), y, AC, 5))
        o.append(Tb(fx(fcv) - 8, y - 12, f'{fcv:.2f}', 13, 'end', MUT))
    o.append(xaxis(x0, x1, yb + 8, [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22], fx, 'frequency (GHz): a bar shows where the mode propagates', fmt))
    for f, lab, c in ((10, '10 GHz: TE10 only', NX), (18, '18 GHz: five modes', NX)):
        o.append(L(fx(f), y0 - 8, fx(f), yb + 8, c, 2, dash='6 4'))
    o.append(Tb(fx(10), yb - 4, '10 GHz: TE10 only', 13, fill=NX, bold=True))
    o.append(Tb(fx(18), yb - 4, '18 GHz: 5 modes', 13, fill=NX, bold=True))
    return yb + 60, ''.join(o)


# ---- 1.8 response of worked example 1 (f0 = 2 GHz, QL = 100) and the same resonator critically coupled ----
def f8():
    o = []
    x0, x1, y0, y1 = 80, 690, 40, 300
    fx = lin(1.96, 2.04, x0, x1); fy = lin(0, 1, y1, y0)
    o.append(axes(x0, x1, y0, y1, [1.96, 1.98, 1.99, 2.0, 2.01, 2.02, 2.04], [0, 0.25, 0.5, 0.707, 1], fx, fy, 'frequency (GHz)', 'response / peak', fmt, fmt))
    def resp(f, Q): return 1 / math.sqrt(1 + (Q * (f / 2.0 - 2.0 / f)) ** 2)
    fs = [1.96 + i * 0.08 / 400 for i in range(401)]
    o.append(P([(fx(f), fy(resp(f, 100))) for f in fs], AC, 3))
    o.append(P([(fx(f), fy(resp(f, 250))) for f in fs], NX, 2.5, dash='8 5'))
    o.append(L(x0, fy(0.7071), x1, fy(0.7071), MUT, 1.2, dash='3 5'))
    a, b = 2.0 - 0.01, 2.0 + 0.01
    o.append(L(fx(a), fy(0.7071), fx(a), y1, AC, 1.2, dash='3 4')); o.append(L(fx(b), fy(0.7071), fx(b), y1, AC, 1.2, dash='3 4'))
    o.append(L(fx(a), fy(0.48), fx(b), fy(0.48), AC, 1.8, arrow='n')); o.append(L(fx(b), fy(0.48), fx(a), fy(0.48), AC, 1.8, arrow='n'))
    o.append(Tb(fx(2.0), fy(0.48) - 9, 'BW = 20 MHz', 14, fill=AC, bold=True))
    for i, (t, c, bb) in enumerate((('solid: Q_L = 100', AC, True), ('Q_e = 125, overcoupled', AC, False), ('dashed: Q_L = 250, BW 8 MHz', NX, True), ('Q_e = Q_0 = 500, critical', NX, False))):
        o.append(T(fx(2.0165), fy(0.985) + i * 19, t, 13, 'start', c, bb))
    return 352, ''.join(o)


# ---- model-answer sketches ----
def ma_smith_25_40():
    o, q = smith(complex(0.5, 0.8), '0.302λ', '0.102λ')
    X, Y = q['X'], q['Y']
    o.append(Tb(X(q['GL']) - 10, Y(q['GL']) - 10, 'z_L = 0.5 + j0.8', 14, 'end', INK, True))
    o.append(Tb(X(q['GY']) + 10, Y(q['GY']) + 22, 'y_L = 0.56 − j0.90', 14, 'start', AC, True))
    o.append(Tb(X(q['tgt']) + 12, Y(q['tgt']) - 10, 'y = 1 + j1.33', 14, 'start', LV, True))
    o.append(Tb(X(q['Gs']) + 10, Y(q['Gs']) + 18, 'stub: −j1.33', 14, 'start', LV, True))
    px = 486
    lines = [(0, '25 + j40 Ω on 50 Ω, 1 GHz', INK, True), (0, '|Γ| = 0.555, VSWR = 3.49', NX, False),
             (0, 'y_L at WTG 0.370λ', AC, False), (0, 'to y = 1 + j1.33 at 0.172λ', LV, False),
             (0, 'd = 0.130λ + 0.172λ', AC, True), (1, '= 0.302λ', AC, True), (0, 'stub −j1.33:', LV, False),
             (1, '0.250λ → 0.352λ', LV, False), (1, 'l_s = 0.102λ', LV, True),
             (0, 'λ = 30 cm: d = 9.07 cm', MUT, False), (1, 'and l_s = 3.07 cm', MUT, False)]
    for i, (ind, t, c, bb) in enumerate(lines):
        o.append(T(px + 16 * ind, 46 + i * 26, t, 13, 'start', c, bb))
    return 450, ''.join(o)


def ma_te10():
    o = []
    x0, y0, a, b = 120, 70, 480, 210
    o.append(R(x0, y0, a, b, PANEL, INK, 2, 3))
    for i in range(1, 16):
        x = x0 + a * i / 16
        e = math.sin(math.pi * i / 16)
        w = 0.8 + 3.2 * e
        o.append(L(x, y0 + b - 6, x, y0 + 8, AC, w, arrow='n' if e > 0.35 else None))
    # H loops seen in cross-section: dashed loops near the side walls are not visible here; show |E| profile above
    pts = [(x0 + a * t / 100, y0 - 12 - 40 * math.sin(math.pi * t / 100)) for t in range(101)]
    o.append(P(pts, NX, 2.5))
    o.append(T(x0 + a / 2, y0 - 60, '|E_y| = E_0 sin(πx/a): zero at the side walls, largest at the centre', 13, fill=NX))
    o.append(L(x0, y0 + b + 22, x0 + a, y0 + b + 22, INK, 1.5, arrow='x')); o.append(L(x0 + a, y0 + b + 22, x0, y0 + b + 22, INK, 1.5, arrow='x'))
    o.append(Tb(x0 + a / 2, y0 + b + 27, 'broad wall a', 14, bold=True))
    o.append(L(x0 + a + 22, y0, x0 + a + 22, y0 + b, INK, 1.5, arrow='x')); o.append(L(x0 + a + 22, y0 + b, x0 + a + 22, y0, INK, 1.5, arrow='x'))
    o.append(T(x0 + a + 32, y0 + b / 2 + 5, 'b', 15, 'start', INK, True))
    o.append(T(x0 - 10, y0 + b / 2 + 5, 'E', 15, 'end', AC, True))
    o.append(T(x0 + a / 2, y0 + b + 62, 'centre line x = a/2: wall current runs only along the guide', 13, fill=LV))
    o.append(L(x0 + a / 2, y0 - 4, x0 + a / 2, y0 + b + 4, LV, 1.5, dash='5 4'))
    return y0 + b + 76, ''.join(o)


FIG = {
    1: (f1, 'One slice Δz of a line: series R Δz and L Δz, shunt G Δz and C Δz. With the per-metre values of worked example 2 at 10 MHz the two ratios give Z0 = 50.0∠−0.14° Ω and γ = 0.00125 + j0.3142 per metre.',
        'Ladder section with a series resistor and inductor on the top wire and a shunt conductance and capacitor to the return wire; boxes give the example values and the resulting Z0 and gamma.'),
    2: (f2, 'Voltage along the line of the worked example (|Γ| = 0.447 at 26.57°). The first maximum, 1.447, sits 0.037λ from the load, the minimum 0.553 sits λ/4 further on, and the ratio is the VSWR, 2.62.',
        'Standing-wave curve of voltage magnitude against distance from the load, with the maximum 1.447 at 0.037 wavelength, minimum 0.553 at 0.287 wavelength, and VSWR 2.62.'),
    3: (f3, 'Input reactance of a shorted stub (solid) and an open stub (dashed) on a 50 Ω line. At 0.15λ, the 3 cm stub of worked example 2, the short gives +j68.8 Ω and the open −j36.3 Ω; at λ/4 the two swap to open and short.',
        'Plot of normalized input reactance against stub length: tangent curve for the shorted stub, minus cotangent for the open stub, with points at 0.15 wavelength.'),
    4: (f4, 'The quarter-wave transformer of the worked example and its input |Γ| against frequency. The match is perfect at f0 and 3f0 and stays inside VSWR 1.5 from 0.61f0 to 1.39f0.',
        'Block layout of a 50 ohm line, a 70.71 ohm quarter-wave section and a 100 ohm load, above a plot of reflection magnitude against normalized frequency with the VSWR 1.5 band shaded.'),
    5: (f5, 'The shunt-stub match of the worked example on a Smith chart drawn to scale. The admittance point is turned clockwise on the VSWR circle to the g = 1 circle, and the short-circuit stub is read along the rim; both lengths agree with the formula answer.',
        'Smith chart with resistance circles and reactance arcs, the load point 2 plus j1, its admittance point, a dashed VSWR circle, an arc to the point 1 plus j1 on the g equals 1 circle, and the stub path along the rim from the short to minus j1.'),
    6: (f6, 'The microstrip of the worked example drawn to scale: a 3 mm strip on 1.6 mm of εr = 4.4. Part of the field runs through the air, so the wave sees εeff = 3.32, between 1 and 4.4.',
        'Cross-section of a microstrip: strip on top of a substrate over a ground plane, field lines from strip to ground with some fringing through the air, and W and h dimension arrows.'),
    7: (f7, 'Where each mode of the worked example\'s guide propagates. Only TE10 travels between 6.56 and 13.12 GHz, so 10 GHz is single-mode; at 18 GHz five modes travel, as worked example 2 finds.',
        'Bar chart of modes TE10, TE20, TE01, TE11 and TM11, TE30, TE21 and TM21, each bar starting at its cutoff frequency, with the single-mode band shaded and dashed lines at 10 and 18 gigahertz.'),
    8: (f8, 'The resonator of worked example 1: QL = 100 gives a 20 MHz band at 2 GHz. Loosened to critical coupling (Qe = Q0 = 500) the same resonator has QL = 250 and an 8 MHz band.',
        'Two resonance curves centred on 2 gigahertz, a wider one for loaded Q 100 with its 20 megahertz half-power band marked, and a narrower dashed one for loaded Q 250.'),
}
spec = make_spec(FIG)


def ma(name):
    """{'h', 'body', 'aria'} for a model-answer sketch"""
    fn, aria = {'smith': (ma_smith_25_40, 'Smith chart solution of a shunt stub match for a 25 plus j40 ohm load'),
                'te10': (ma_te10, 'TE10 electric field across a rectangular guide cross-section with its sine profile')}[name]
    h, body = fn()
    return {'h': h, 'body': body, 'aria': aria}
