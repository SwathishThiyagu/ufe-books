"""Claude's hand-drawn figures for me-design-u5 (Machine Design: bearings, lubrication, seals and gaskets), one per chapter,
drawn from each chapter's own worked example and numbers. The eccentricity curve uses the Raimondi and Boyd rows for
L/D = 1 that the chapter prints; the life curves are computed from L10 = (C/P)^p. Colours are the shell's CSS variables."""
import os, sys, math, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

_T, _Tb, _boxt = T, Tb, boxt


def _sub(s):
    """h_0, F_r ... drawn as real subscripts, never as underscores"""
    return re.sub(r'([A-Za-zα-ωΔ])_([A-Za-z0-9]+)', r'\1<tspan baseline-shift="sub" font-size="11">\2</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)
def boxt(x, y, w, h, lines, *a, **k): return _boxt(x, y, w, h, [_sub(l) for l in lines], *a, **k)


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


def circ(cx, cy, r, fill=PANEL, stroke=AC, sw=2, dash=None):
    d = f';stroke-dasharray:{dash}' if dash else ''
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" style="fill:{fill};stroke:{stroke};stroke-width:{sw}{d}"/>'


def hatch_rect(x, y, w, h, step=10):
    """a housing block with hatching lines inside"""
    o = [R(x, y, w, h, PANEL, L2, 2, 1.5)]
    clip = []
    k = 0
    while k < w + h:
        x1, y1 = x + k, y
        x2, y2 = x + k - h, y + h
        if x2 < x: y2 = y + (k); x2 = x
        if x1 > x + w: y1 = y + (x1 - x - w); x1 = x + w
        if y2 > y + h: y2 = y + h
        o.append(L(x1, y1, x2, y2, L2, 1))
        k += step
    return ''.join(o)


# ---- 5.1 the shear film of part (c): plate at 2 m/s over a 0.1 mm oil film ----
def f1():
    o = []
    x0, x1, yb, yt = 70, 470, 250, 110
    o.append(R(x0, yt - 28, x1 - x0, 28, ACS, AC, 3))
    o.append(T((x0 + x1) / 2, yt - 9, 'moving plate, area A = 0.01 m²', 14, bold=True))
    o.append(L(x1 - 60, yt - 44, x1 + 10, yt - 44, AC, 2.5, arrow='n'))
    o.append(T(x1 - 66, yt - 39, 'U = 2 m/s', 14, 'end', AC, bold=True))
    o.append(hatch_rect(x0, yb, x1 - x0, 26, 14))
    o.append(T((x0 + x1) / 2, yb + 48, 'fixed plate', 14, fill=MUT))
    o.append(R(x0, yt, x1 - x0, yb - yt, LVS, LVS, 0, 0))
    # linear velocity profile at x = 170
    px = 170
    o.append(L(px, yb, px, yt, L2, 1.5))
    for i in range(1, 6):
        yy = yb - i * (yb - yt) / 5
        ln = 230 * i / 5
        o.append(L(px, yy, px + ln, yy, LV, 2, arrow='l'))
    o.append(L(px, yb, px + 230, yt, LV, 1.5, dash='5 4'))
    o.append(T(px - 10, (yb + yt) / 2 + 5, 'h = 0.1 mm', 14, 'end', bold=True))
    o.append(T(px + 120, yb - 12, 'oil film, μ = 0.05 Pa·s', 13, 'start', MUT))
    # result boxes
    o.append(boxt(510, 70, 194, 56, ['du/dy = U/h', '= 20 000 s⁻¹'], PANEL, LV, 14, True))
    o.append(boxt(510, 140, 194, 56, ['τ = μ du/dy', '= 1000 Pa'], PANEL, AC, 14, True))
    o.append(boxt(510, 210, 194, 56, ['F = τ A', '= 10 N'], NXS, NX, 14, True))
    o.append(T(360, 320, 'Same oil: ν = μ/ρ = 0.05/900 = 5.56 × 10⁻⁵ m²/s = 55.6 cSt', 14, bold=True))
    return 336, ''.join(o)


# ---- 5.2 plain bearing and ball bearing, with the friction power of the worked example ----
def f2():
    o = []
    # plain journal bearing (left)
    cx, cy = 180, 165
    o.append(circ(cx, cy, 118, PANEL, L2, 1.5))
    o.append(circ(cx, cy, 96, NXS, NX, 2))
    o.append(circ(cx, cy, 84, LVS, LV, 1.5))
    o.append(circ(cx, cy, 80, ACS, AC, 2))
    o.append(T(cx, cy - 4, 'journal', 14, bold=True))
    o.append(T(cx, cy + 16, 'd = 100 mm', 13, fill=MUT))
    o.append(L(cx - 70, cy - 108, cx - 110, cy - 140, L2, 1.2)); o.append(T(cx - 114, cy - 140, 'housing', 13, 'end'))
    o.append(L(cx + 86, cy - 40, cx + 150, cy - 70, NX, 1.2)); o.append(T(cx + 154, cy - 68, 'bush (lining)', 13, 'start', NX))
    o.append(L(cx + 80, cy + 16, cx + 150, cy + 40, LV, 1.2)); o.append(T(cx + 154, cy + 44, 'oil film', 13, 'start', LV))
    o.append(T(cx, 320, 'Plain bearing, μ = 0.01', 14, bold=True))
    o.append(T(cx, 342, 'T = 10 N·m, P = 942.5 W', 14, fill=AC, bold=True))
    # ball bearing (right)
    bx, by = 540, 165
    o.append(circ(bx, by, 118, PANEL, AC, 2))
    o.append(circ(bx, by, 98, FIGBG, AC, 1.5))
    o.append(circ(bx, by, 62, FIGBG, AC, 1.5))
    o.append(circ(bx, by, 42, PANEL, AC, 2))
    o.append(circ(bx, by, 80, 'none', L2, 1.2, dash='4 4'))
    for i in range(10):
        a = 2 * math.pi * i / 10
        o.append(circ(bx + 80 * math.cos(a), by + 80 * math.sin(a), 16, LVS, LV, 2))
    o.append(T(bx, by + 5, 'shaft', 13, fill=MUT))
    o.append(L(bx - 100, by - 80, bx - 140, by - 126, AC, 1.2)); o.append(T(bx - 144, by - 128, 'outer ring', 13, 'end'))
    o.append(L(bx - 50, by + 20, bx - 150, by + 70, AC, 1.2)); o.append(T(bx - 150, by + 86, 'inner ring', 13, 'middle'))
    o.append(L(bx + 80, by, bx + 140, by - 120, LV, 1.2)); o.append(T(bx + 140, by - 126, 'ball', 13, 'middle', LV))
    o.append(L(bx + 52, by + 60, bx + 128, by + 120, L2, 1.2)); o.append(T(bx + 104, by + 134, 'cage (pitch circle)', 13, 'middle', MUT))
    o.append(T(bx, 320, 'Ball bearing, μ = 0.002', 14, bold=True))
    o.append(T(bx, 342, 'T = 2 N·m, P = 188.5 W', 14, fill=LV, bold=True))
    o.append(T(360, 372, 'Same shaft, W = 20 kN, 900 rpm: the plain bearing turns 754 W more into heat', 14, fill=MUT))
    return 388, ''.join(o)


# ---- 5.3 eccentric journal: c = 0.05 mm, e = 0.03 mm, h0 = 0.02 mm (gap drawn about 900 times too large) ----
def f3():
    o = []
    cx, cy, Rb = 230, 200, 150
    c = 40.0           # drawn clearance in px (stands for 0.05 mm)
    e = 0.6 * c        # eccentricity ratio 0.6
    rj = Rb - c
    ang = math.radians(50)   # line of centres, below the bush centre, displaced in the direction of rotation
    jx, jy = cx + e * math.sin(ang), cy + e * math.cos(ang)
    o.append(circ(cx, cy, Rb + 14, PANEL, L2, 1.5))
    o.append(circ(cx, cy, Rb, LVS, AC, 2))
    o.append(circ(jx, jy, rj, ACS, AC, 2))
    o.append(T(jx + 6, jy - 44, 'journal', 15, bold=True))
    # rotation arrow (clockwise)
    a0, a1 = math.radians(200), math.radians(320)
    rr = 70
    pts = [(jx + rr * math.cos(a0 + (a1 - a0) * i / 20), jy + rr * math.sin(a0 + (a1 - a0) * i / 20)) for i in range(21)]
    pts = pts[::-1]  # counter-clockwise: the bottom of the journal moves right, towards the thin film
    o.append(P(pts, AC, 2.2))
    o.append(L(pts[-2][0], pts[-2][1], pts[-1][0], pts[-1][1], AC, 2.2, arrow='n'))
    o.append(T(jx + 2, jy - 82, 'ω', 15, fill=AC, bold=True))
    # centres
    o.append(C(cx, cy, 4, INK)); o.append(C(jx, jy, 4, NX))
    o.append(L(cx, cy, jx, jy, NX, 2))
    o.append(L(cx, cy, cx, cy + 50, L2, 1.5, dash='4 4'))
    o.append(T(cx - 10, cy + 4, 'O', 14, 'end', bold=True))
    o.append(T(jx + 30, jy + 32, 'e = 0.03 mm', 13, 'start', NX, bold=True))
    o.append(T(cx + 3, cy + 30, 'φ', 14, 'start', NX))
    # minimum film point
    hx, hy = cx + Rb * math.sin(ang), cy + Rb * math.cos(ang)
    o.append(C(hx, hy, 5, NX))
    o.append(L(hx + 6, hy + 4, 430, 360, NX, 1.4))
    o.append(T(436, 364, 'h₀ = c(1 − ε) = 0.02 mm', 14, 'start', NX, bold=True))
    # maximum gap
    gx, gy = cx - Rb * math.sin(ang), cy - Rb * math.cos(ang)
    o.append(L(gx - 4, gy - 4, 420, 40, LV, 1.4))
    o.append(T(426, 44, 'widest gap c + e = 0.08 mm', 14, 'start', LV))
    # load
    o.append(L(jx - 40, jy - 20, jx - 40, jy + 70, INK, 2.5, arrow='m'))
    o.append(T(jx - 50, jy + 56, 'W', 15, 'end', bold=True))
    # notes
    o.append(T(436, 130, 'radial clearance c = 0.05 mm', 14, 'start', bold=True))
    o.append(T(436, 154, 'ε = e/c = 0.6', 14, 'start'))
    o.append(T(436, 200, 'oil dragged by the journal', 14, 'start', AC))
    o.append(T(436, 222, 'into the narrowing gap', 14, 'start', AC))
    o.append(T(436, 244, 'builds the film pressure', 14, 'start', AC))
    o.append(T(436, 280, 'O = bush centre; φ = attitude angle', 13, 'start', MUT))
    o.append(T(436, 300, 'gap drawn about 900 times', 13, 'start', MUT))
    o.append(T(436, 318, 'larger than true scale', 13, 'start', MUT))
    return 386, ''.join(o)


# ---- 5.4 projected area: L x D = 2500 mm2, not pi D L ----
def f4():
    o = []
    # side view of the journal in the bearing
    x0, y0, Lp, Dp = 150, 70, 180, 180
    o.append(R(x0 - 24, y0 + 40, 24, 100, PANEL, L2, 2))
    o.append(R(x0 + Lp, y0 + 40, 50, 100, PANEL, L2, 2))
    o.append(R(x0, y0, Lp, Dp, ACS, AC, 3))
    o.append(T(x0 + Lp / 2, y0 + Dp / 2 - 6, 'projected area', 14, bold=True))
    o.append(T(x0 + Lp / 2, y0 + Dp / 2 + 14, 'L × D = 2500 mm²', 14, bold=True))
    o.append(brace(x0, x0 + Lp, y0 - 14, INK, up=True))
    o.append(T(x0 + Lp / 2, y0 - 22, 'L = 50 mm', 14))
    o.append(P([(x0 - 44, y0), (x0 - 50, y0), (x0 - 50, y0 + Dp), (x0 - 44, y0 + Dp)], INK, 1.8))
    o.append(T(x0 - 56, y0 + Dp / 2 + 5, 'D = 50 mm', 14, 'end'))
    for i in range(5):
        xx = x0 + 18 + i * 36
        o.append(L(xx, y0 + Dp + 50, xx, y0 + Dp + 6, NX, 2, arrow='x'))
    o.append(T(x0 + Lp / 2, y0 + Dp + 70, 'W = 10 kN spread over L × D', 14, fill=NX, bold=True))
    o.append(T(x0 + Lp / 2, y0 + Dp + 92, 'side view, shaft axis across the page', 13, fill=MUT))
    # right: the two pressures and S
    o.append(boxt(400, 50, 300, 66, ['right: p = W/(LD)', '= 10 000/2500 = 4 MPa'], LVS, LV, 14, True))
    o.append(boxt(400, 132, 300, 66, ['wrong: W/(πDL) = 1.27 MPa', 'S comes out π times too big'], NXS, NX, 14, True))
    o.append(boxt(400, 214, 300, 90, ['S = (μn/p)(r/c)²', '= (0.02 × 25/4 × 10⁶) × 500²', '= 0.03125'], PANEL, AC, 14, True))
    o.append(T(550, 330, 'n = 25 rev/s, r/c = 25/0.05 = 500', 13, fill=MUT))
    return 372, ''.join(o)


# ---- 5.5 eccentricity ratio against S for L/D = 1, with the worked example ----
RBP = [(1.33, 0.1), (0.631, 0.2), (0.264, 0.4), (0.121, 0.6), (0.0446, 0.8), (0.0188, 0.9)]


def f5():
    o = []
    x0, x1, y0, y1 = 90, 690, 40, 300
    lx = lambda s: x0 + (math.log10(s) - math.log10(0.01)) / (math.log10(2) - math.log10(0.01)) * (x1 - x0)
    fy = lin(0, 1, y1, y0)
    o.append(L(x0, y1, x1, y1, L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    for s, lab in ((0.01, '0.01'), (0.02, '0.02'), (0.05, '0.05'), (0.1, '0.1'), (0.2, '0.2'), (0.5, '0.5'), (1, '1'), (2, '2')):
        X = lx(s); o += [L(X, y1, X, y1 + 5, L2, 1.5), L(X, y0, X, y1, 'var(--line)', 1), T(X, y1 + 20, lab, 13, fill=MUT)]
    for v in (0, 0.2, 0.4, 0.6, 0.8, 1.0):
        Y = fy(v); o += [L(x0 - 5, Y, x0, Y, L2, 1.5), L(x0, Y, x1, Y, 'var(--line)', 1), T(x0 - 9, Y + 4.5, f'{v:.1f}', 13, 'end', MUT)]
    o.append(T((x0 + x1) / 2, y1 + 42, 'Sommerfeld number S (log scale)', 14, fill=MUT))
    o.append(T(x0, y0 - 14, 'eccentricity ratio ε, L/D = 1', 14, 'start', MUT))
    pts = [(lx(s), fy(e)) for s, e in RBP]
    o.append(P(pts, AC, 2.5))
    for p in pts: o.append(C(p[0], p[1], 4, AC))
    # worked example S = 0.03125, eps = 0.852
    ex, ey = lx(0.03125), fy(0.852)
    o.append(L(ex, y1, ex, ey, NX, 1.5, dash='5 4'))
    o.append(L(x0, ey, ex, ey, NX, 1.5, dash='5 4'))
    o.append(C(ex, ey, 6, NX))
    o.append(Tb(ex + 12, ey - 14, 'worked example: S = 0.03125, ε = 0.85, h₀ = 7.4 μm', 14, 'start', NX, True))
    q = (lx(0.121), fy(0.6))
    o.append(Tb(q[0] + 12, q[1] - 10, 'S = 0.121, ε = 0.6 (a table row)', 13, 'start', AC))
    o.append(Tb(lx(0.6), fy(0.32), 'high S: journal near the centre', 13, 'middle', MUT))
    return 356, ''.join(o)


# ---- 5.6 life against load for C = 30 kN, ball and roller ----
def f6():
    o = []
    x0, x1, y0, y1 = 90, 690, 40, 300
    fx = lin(4, 12, x0, x1); fy = lin(0, 900, y1, y0)
    o.append(axes(x0, x1, y0, y1, [4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 150, 300, 450, 600, 750, 900], fx, fy,
                  'equivalent load P (kN)', 'L₁₀ (million revolutions), C = 30 kN'))
    for p, col, lab in ((3, AC, 'ball, p = 3'), (10 / 3, LV, 'roller, p = 10/3')):
        pts = []
        for i in range(0, 81):
            P_ = 4 + 8 * i / 80
            Lf = (30 / P_) ** p
            if Lf <= 900: pts.append((fx(P_), fy(Lf)))
        o.append(P(pts, col, 2.5))
    o.append(Tb(fx(7.0), fy(235), 'roller, p = 10/3', 14, 'start', LV, True))
    o.append(Tb(fx(4.15), fy(60), 'ball, p = 3', 14, 'start', AC, True))
    for P_, Lf, col, lab in ((6, 125, AC, '125 at 6 kN'), (6, 213.7, LV, '214'), (12, 15.6, AC, '15.6 at 12 kN')):
        o.append(C(fx(P_), fy(Lf), 6, col))
    o.append(Tb(fx(6.15), fy(330), '6 kN: 125 (ball), 214 (roller)', 13, 'start', INK, True))
    o.append(Tb(fx(12) - 10, fy(15.6) - 40, 'double the load: 15.6, one-eighth', 13, 'end', NX, True))
    return 346, ''.join(o)


# ---- 5.7 the selection of the worked example ----
def f7():
    o = []
    # half section of a deep-groove ball bearing with the two loads
    cx, cy = 130, 190
    o.append(R(60, 70, 140, 40, PANEL, AC, 6))
    o.append(R(60, 270, 140, 40, PANEL, AC, 6))
    o.append(circ(cx, 132, 24, LVS, LV, 2)); o.append(circ(cx, 248, 24, LVS, LV, 2))
    o.append(R(60, 156, 140, 68, ACS, L2, 2))
    o.append(T(cx, 196, 'shaft, 45 mm bore', 13, fill=MUT))
    o.append(T(206, 96, 'outer ring', 13, 'start', MUT)); o.append(T(160, 136, 'ball', 13, 'start', LV))
    o.append(L(cx, 40, cx, 66, NX, 2.5, arrow='x'))
    o.append(T(cx + 8, 36, 'F_r = 5 kN', 14, 'start', NX, True))
    o.append(L(20, 190, 56, 190, NX, 2.5, arrow='x'))
    o.append(T(20, 238, 'F_a = 2 kN', 14, 'start', NX, True))
    o.append(T(cx, 336, '1200 rev/min, 10 000 h', 13, fill=MUT))
    # chain of results
    boxes = [(['L₁₀ = 60 × 1200 × 10 000/10⁶', '= 720 million rev'], PANEL, L2),
             (['B: F_a/C₀ = 0.0635 → e = 0.265, Y = 1.667', 'P = 2800 + 3334 = 6134 N'], PANEL, AC),
             (['C_req = 6134 × 720^(1/3)'.replace('^(1/3)', '<tspan baseline-shift="super" font-size="11">1/3</tspan>'), '= 54 980 N ≤ C = 55 300 N'], LVS, LV),
             (['static: P₀ = 5000 N, s₀ = 31.5/5 = 6.3', 'life of B: 10 175 h'], NXS, NX)]
    y = 20
    for lines, fill, st in boxes:
        o.append(boxt(300, y, 404, 64, lines, fill, st, 14, False))
        if y > 20: o.append(L(502, y - 16, 502, y - 2, AC, 2, arrow='n'))
        y += 84
    return 360, ''.join(o)


# ---- 5.8 gasketed flange of the worked example, and the O-ring groove ----
def f8():
    o = []
    # half section of the joint: vessel inside at the left, cover on top, flange ring under it, gasket between
    o.append(R(30, 60, 320, 44, PANEL, AC, 2))            # cover
    o.append(R(140, 116, 200, 44, PANEL, AC, 2))          # flange ring
    o.append(R(140, 160, 28, 60, PANEL, AC, 2))           # shell wall
    o.append(R(170, 104, 100, 12, NXS, NX, 1))            # gasket
    o.append(R(296, 40, 22, 136, LVS, LV, 2))             # bolt
    o.append(R(288, 30, 38, 12, LV, LV, 1)); o.append(R(288, 176, 38, 12, LV, LV, 1))
    o.append(T(326, 26, 'bolt', 13, 'start', LV, True))
    o.append(T(120, 87, 'cover', 14, bold=True))
    o.append(T(230, 144, 'flange', 14, bold=True))
    o.append(L(60, 200, 60, 108, AC, 2, arrow='n')); o.append(L(100, 200, 100, 108, AC, 2, arrow='n'))
    o.append(T(80, 220, 'p = 2 MPa', 13, 'middle', AC, True))
    o.append(T(80, 238, 'inside', 13, 'middle', MUT))
    o.append(L(220, 112, 220, 196, NX, 1.2))
    o.append(T(186, 212, 'gasket 300 to 320 mm, N = 10 mm', 13, 'start', NX, True))
    o.append(T(190, 266, 'G = 310 mm, b = 5 mm', 14, bold=True))
    o.append(T(190, 288, 'W_m2 = π b G y = 53.6 kN', 14))
    o.append(T(190, 310, 'W_m1 = H + H_p = 151.0 + 39.0 = 189.9 kN', 14, fill=AC, bold=True))
    o.append(T(190, 332, '16 bolts of M14 carry it', 14))
    # O-ring in groove (right)
    gx, gy, gw, gh = 470, 110, 120, 70     # groove 4.80 mm wide, 2.80 mm deep, scaled 25 px/mm
    o.append(R(420, 70, 240, 40, PANEL, AC, 2))         # mating face (cover)
    o.append(P([(420, 110), (gx, 110), (gx, gy + gh), (gx + gw, gy + gh), (gx + gw, 110), (660, 110)], AC, 2))
    o.append(R(420, 110, gx - 420, 80, PANEL, 'none', 0, 0)); o.append(R(gx + gw, 110, 660 - gx - gw, 80, PANEL, 'none', 0, 0))
    o.append(R(gx, gy + gh, gw, 10, PANEL, 'none', 0, 0))
    o.append(f'<ellipse cx="{gx + gw / 2:.1f}" cy="{gy + gh / 2:.1f}" rx="{3.53 * 25 / 2 * 1.08:.1f}" ry="{gh / 2:.1f}" style="fill:var(--live-soft);stroke:var(--live);stroke-width:2"/>')
    o.append(T(540, 60, 'O-ring in its groove', 14, bold=True))
    o.append(P([(gx + gw + 8, gy), (gx + gw + 14, gy), (gx + gw + 14, gy + gh), (gx + gw + 8, gy + gh)], INK, 1.6))
    o.append(T(gx + gw + 20, gy + gh / 2 + 5, 'h = 2.80', 13, 'start'))
    o.append(brace(gx, gx + gw, gy + gh + 18, INK))
    o.append(T(gx + gw / 2, gy + gh + 44, 'w = 4.80 mm', 13))
    o.append(T(540, 260, 'd = 3.53 mm squeezed to 2.80 mm', 14, bold=True))
    o.append(T(540, 282, 'squeeze = 0.73/3.53 = 21 %', 14, fill=LV, bold=True))
    o.append(T(540, 304, 'fill = 9.79/13.44 = 73 %', 14, fill=LV, bold=True))
    return 348, ''.join(o)


FIG = {
    1: (f1, 'Part (c) of the worked example. The oil velocity rises in a straight line across the 0.1 mm film, so the gradient is 20 000 s⁻¹ and the shear stress 1000 Pa; dragging the 0.01 m² plate takes 10 N.',
        'A plate sliding at 2 metres per second over a 0.1 millimetre oil film with a straight-line velocity profile; boxes give the velocity gradient, a shear stress of 1000 pascals and a force of 10 newtons.'),
    2: (f2, 'The two bearing families of the worked example in cross-section. The plain bearing carries the journal on an oil film inside a bush; the ball bearing rolls on balls between two rings and loses about a fifth of the power.',
        'Cross-sections of a plain journal bearing (housing, bush, oil film, journal) and a ball bearing (outer ring, balls, cage, inner ring), with friction power 942.5 watts and 188.5 watts.'),
    3: (f3, 'The loaded journal of the worked example, with the clearance drawn far larger than life. The journal centre sits 0.03 mm from the bush centre, the narrowing gap carries the load, and the thinnest film is 0.02 mm.',
        'A journal off centre in its bush, with eccentricity 0.03 millimetres, minimum film 0.02 millimetres opposite the widest gap of 0.08 millimetres, the load W and the rotation.'),
    4: (f4, 'The load of the worked example spreads over the projected rectangle L × D, not over the curved surface. That gives p = 4 MPa and S = 0.03125; using πDL would make S look π times larger and the film safer than it is.',
        'Side view of a 50 by 50 millimetre journal with the projected area shaded, and boxes comparing 4 megapascals with the wrong 1.27 megapascals, and the Sommerfeld number 0.03125.'),
    5: (f5, 'Eccentricity ratio against S for L/D = 1, through the table rows of this chapter. The worked example at S = 0.03125 runs at ε = 0.85, with a 7.4 μm film; a larger S would lift the journal towards the centre.',
        'A falling curve of eccentricity ratio against Sommerfeld number on a log scale, through six table points, with the worked example marked at S 0.03125 and eccentricity 0.85.'),
    6: (f6, 'Rating life against load for C = 30 kN. At the worked example\'s 6 kN a ball bearing gives 125 million revolutions and a roller bearing 214; doubling the load to 12 kN cuts the ball bearing to 15.6, one-eighth.',
        'Two falling curves of L10 life against equivalent load from 4 to 12 kilonewtons, for ball and roller bearings, with points at 125, 214 and 15.6 million revolutions.'),
    7: (f7, 'The selection of the worked example. The two loads and the life fix the required rating; bearing B, with 55.3 kN, clears the required 55.0 kN and passes the static check.',
        'A deep-groove ball bearing with a radial load of 5 kilonewtons and an axial load of 2 kilonewtons, beside four boxes: life 720 million revolutions, equivalent load 6134 newtons, required rating 54 980 newtons, static factor 6.3.'),
    8: (f8, 'The two worked examples. Left, the bolted cover: the pressure case needs 189.9 kN of bolt load, more than the 53.6 kN that seats the gasket. Right, the O-ring squeezed 21 % in a groove it fills to 73 %.',
        'Half section of a bolted cover with a gasket under 2 megapascals and the bolt loads, beside an O-ring in a rectangular groove 4.80 by 2.80 millimetres with squeeze 21 per cent and fill 73 per cent.'),
}
spec = make_spec(FIG)
