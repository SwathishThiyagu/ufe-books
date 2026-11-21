"""Claude's hand-drawn figures for ce-rcc-u5 (Design of Reinforced Concrete Structures: columns and footings), one per
chapter, each drawn from that chapter's own worked example and numbers. Colours are the shell's CSS variables."""
import os, sys, math, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

_T, _Tb, _boxt = T, Tb, boxt


def _sub(s):
    """l_ex, P_u ... drawn as real subscripts, never as underscores"""
    return re.sub(r'([A-Za-zα-ωΔσ])_([A-Za-z0-9]+)', r'\1<tspan baseline-shift="sub" font-size="11">\2</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)
def boxt(x, y, w, h, lines, *a, **k): return _boxt(x, y, w, h, [_sub(l) for l in lines], *a, **k)


def dim(x1, y1, x2, y2, label, side='above', size=13, c=MUT):
    """a dimension line with arrowheads at both ends and its label"""
    o = [L(x1, y1, x2, y2, c, 1.4, arrow='m'), L(x2, y2, x1, y1, c, 1.4, arrow='m')]
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    if y1 == y2:
        o.append(Tb(mx, my - 7 if side == 'above' else my + 18, label, size, fill=c))
    else:
        o.append(Tb(mx + (8 if side == 'right' else -8), my + 5, label, size, 'start' if side == 'right' else 'end', c))
    return ''.join(o)


def circ(x, y, r, fill=PANEL, stroke=AC, sw=2, dash=None):
    d = f';stroke-dasharray:{dash}' if dash else ''
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{fill};stroke:{stroke};stroke-width:{sw}{d}"/>'


def bar(x, y, r=5, c=AC):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{c}"/>'


def poly(pts, fill=PANEL, stroke=AC, sw=2, op=None):
    o = f';fill-opacity:{op}' if op is not None else ''
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" style="fill:{fill};stroke:{stroke};stroke-width:{sw}{o};stroke-linejoin:round"/>'


def hatch(x1, x2, y, down=True, c=INK):
    """a fixed support: a thick line with short hatching"""
    s = 1 if down else -1
    o = [L(x1, y, x2, y, c, 3)]
    for x in range(int(x1) + 4, int(x2), 8):
        o.append(L(x, y, x - 6, y + s * 8, c, 1.3))
    return ''.join(o)


def up_arrows(x1, x2, ytop, ybot, n, c=LV):
    """a row of upward arrows (soil pressure) from ybot up to ytop"""
    o = []
    for i in range(n):
        x = x1 + (x2 - x1) * i / (n - 1)
        o.append(L(x, ybot, x, ytop + 2, c, 1.6, arrow='l'))
    return ''.join(o)


FIG = {}


# ---- ch1: the five end conditions of Table 28 and the worked example's 300 x 450 column ----
def f1():
    o = []
    cases = [('fixed–fixed', 'braced', '0.65', 'ff'), ('fixed–pinned', 'braced', '0.80', 'fp'), ('pinned–pinned', 'braced', '1.0', 'pp'),
             ('fixed–fixed', 'sway', '1.2', 'fs'), ('fixed–free', 'cantilever', '2.0', 'fr')]
    top, bot, A = 52, 232, 26
    shape = {'ff': lambda t: (1 - math.cos(2 * math.pi * t)) / 2, 'fp': lambda t: 6.75 * t * (1 - t) ** 2 / 1.0,
             'pp': lambda t: math.sin(math.pi * t), 'fs': lambda t: (1 + math.cos(math.pi * t)) / 2, 'fr': lambda t: 1 - math.sin(math.pi * t / 2)}
    for i, (n1, n2, K, s) in enumerate(cases):
        cx = 84 + 138 * i
        o.append(L(cx, top, cx, bot, L2, 1.4, dash='5 4'))
        f = shape[s]
        o.append(P([(cx + A * f(j / 40), top + (bot - top) * j / 40) for j in range(41)], AC, 3))
        # bottom support: fixed for all but pinned–pinned
        if s == 'pp':
            o.append(poly([(cx, bot), (cx - 11, bot + 16), (cx + 11, bot + 16)], PANEL, INK, 1.8))
        else:
            o.append(hatch(cx - 18, cx + 18, bot))
        # top support
        tx = cx + A * f(0)
        if s in ('ff',):
            o.append(hatch(cx - 18, cx + 18, top, down=False))
        elif s in ('fp', 'pp'):
            o.append(poly([(cx, top), (cx - 11, top - 16), (cx + 11, top - 16)], PANEL, INK, 1.8))
        elif s == 'fs':
            o.append(hatch(tx - 18, tx + 18, top, down=False))
            o.append(L(cx - 4, top - 18, tx + 6, top - 18, NX, 2, arrow='x'))
        o.append(T(cx, 268, n1, 13, bold=True))
        o.append(T(cx, 285, n2, 13, fill=MUT))
        o.append(T(cx, 308, 'K = ' + K, 15, fill=NX, bold=True))
    o.append(T(360, 24, 'buckled shape (solid) and effective length l_e = K l', 14, fill=MUT))
    # the worked example's section
    sx, sy, sc = 70, 350, 0.2
    o.append(R(sx, sy, 300 * sc, 450 * sc, PANEL, AC, 2, 2))
    for xx in (sx + 11, sx + 60 - 11):
        for yy in (sy + 11, sy + 45, sy + 90 - 11):
            o.append(bar(xx, yy, 4))
    o.append(dim(sx, sy + 104, sx + 60, sy + 104, 'b = 300', side='below'))
    o.append(dim(sx - 12, sy, sx - 12, sy + 90, 'D = 450', side='left'))
    o.append(L(sx - 4, sy + 45, sx + 64, sy + 45, MUT, 1, dash='3 3'))
    o.append(T(sx + 70, sy + 49, 'x', 13, 'start', MUT, italic=True))
    o.append(boxt(200, 338, 500, 122, ['worked example: l = 3.6 m, pinned at both ends, K = 1.0',
                                       'l_ex/D = 3600/450 = 8.0 < 12: short about x',
                                       'l_ey/b = 3600/300 = 12.0, not < 12: slender about y',
                                       'e_min = 22.2 mm (x) and 20 mm (y)'], PANEL, L2, 14,
                  fills=[INK, INK, NX, MUT]))
    return 480, ''.join(o)


FIG[1] = (f1, 'The five end conditions of IS 456 Table 28 with their design K values and buckled shapes. Below, the worked example’s 300 mm × '
              '450 mm column, 3.6 m long: short about x (8.0), slender about y (12.0).',
          'Five small columns side by side: fixed at both ends braced with K 0.65, fixed and pinned with K 0.80, pinned at both ends with K 1.0, '
          'fixed at both ends with sway with K 1.2, and fixed at the base and free at the top with K 2.0, each with its buckled shape. Below, a 300 by '
          '450 millimetre section with six bars and a box giving slenderness ratios 8.0 about x and 12.0 about y.')


# ---- ch2: the tied 400 x 400 column with 6 bars of 25 mm, and the 400 mm helical column ----
def f2():
    o = []
    x0, y0, s = 60, 60, 0.5
    o.append(R(x0, y0, 200, 200, PANEL, AC, 2, 2))
    o.append(R(x0 + 22, y0 + 22, 156, 156, 'none', LV, 6, 2.2))
    c = 60.5 * s
    xs = [x0 + c, x0 + 100, x0 + 200 - c]
    for yy in (y0 + c, y0 + 200 - c):
        for xx in xs:
            o.append(bar(xx, yy, 6.5))
    o.append(L(x0 + 100, y0 + c - 9, x0 + 100, y0 + 200 - c + 9, NX, 2.2))
    o.append(dim(x0, y0 - 16, x0 + 200, y0 - 16, '400 mm'))
    o.append(dim(x0 + c, y0 + 228, x0 + 100, y0 + 228, '≈ 140 mm', side='below'))
    o.append(T(x0 + 100, y0 + 274, 'tied: 6 bars of 25 mm (1.84 %)', 14, bold=True))
    o.append(T(x0 + 100, y0 + 293, 'P_u = 2000 kN, capacity 2075 kN', 13, fill=MUT))
    o.append(T(x0 + 212, y0 + 78, '8 mm tie', 13, 'start', LV))
    o.append(T(x0 + 212, y0 + 96, '@ 300 c/c', 13, 'start', LV))
    o.append(T(x0 + 212, y0 + 130, 'link on the', 13, 'start', NX))
    o.append(T(x0 + 212, y0 + 148, 'middle bars', 13, 'start', NX))
    o.append(L(x0 + 210, y0 + 136, x0 + 104, y0 + 120, NX, 1.2))
    # helical column elevation
    ex, ey, w, h, pitch = 400, 50, 160, 250, 20
    o.append(R(ex, ey, w, h, PANEL, AC, 2, 0))
    kx0, kx1 = ex + 16, ex + w - 16
    for bx in (ex + 30, ex + 80, ex + 130):
        o.append(L(bx, ey + 4, bx, ey + h - 4, L2, 3))
    yy = ey + 6
    while yy + pitch <= ey + h:
        o.append(L(kx0, yy, kx1, yy + pitch / 2, AC, 2.2))
        o.append(L(kx1, yy + pitch / 2, kx0, yy + pitch, L2, 1.3, dash='3 3'))
        yy += pitch
    o.append(dim(ex, ey + h + 16, ex + w, ey + h + 16, 'D = 400', side='below'))
    o.append(dim(kx0, ey - 14, kx1, ey - 14, 'D_k = 320'))
    o.append(dim(ex - 12, ey + 186, ex - 12, ey + 186 + pitch, 's = 50', side='left'))
    # plan of the helical column
    px, py, r = 648, 110, 58
    o.append(circ(px, py, r, PANEL, AC, 2))
    o.append(circ(px, py, r - 13, 'none', LV, 2))
    for i in range(6):
        a = math.pi / 2 + 2 * math.pi * i / 6
        o.append(bar(px + (r - 21) * math.cos(a), py - (r - 21) * math.sin(a), 5))
    o.append(T(px, py + r + 20, 'plan: 6 bars', 13, fill=MUT))
    o.append(T(px, py + r + 37, 'of 20 mm', 13, fill=MUT))
    o.append(T(576, 236, '8 mm helix', 13, 'start', AC, bold=True))
    o.append(T(576, 254, 'pitch 50 mm', 13, 'start', AC))
    o.append(T(576, 272, '≤ 75, ≤ D_k/6', 13, 'start', MUT))
    o.append(T(480, 364, 'helical: P_u = 1800 kN, capacity 1850 kN', 14, bold=True))
    return 380, ''.join(o)


FIG[2] = (f2, 'The worked examples’ designs. Left: the 400 mm square tied column, 6 bars of 25 mm, 8 mm ties at 300 mm and a link on the middle '
              'bars. Right: the 400 mm helical column, 6 bars of 20 mm, 8 mm helix at 50 mm pitch.',
          'Left, a square column section 400 millimetres wide with three 25 millimetre bars on each of two opposite faces, an 8 millimetre tie and a '
          'straight link between the middle bars. Right, an elevation of a circular column 400 millimetres wide with a helix at 50 millimetre pitch '
          'inside a 320 millimetre core, and a small plan showing six bars inside the helix.')


# ---- ch3: the interaction curve of the 300 x 500 column with 8 bars of 20 mm, M20, and the design point ----
CURVE3 = [(178.5, 0.0), (200.6, 119.1), (213.6, 194.7), (226.3, 278.8), (235.6, 354.2), (242.4, 425.0), (245.4, 503.2), (244.3, 592.9),
          (238.6, 694.0), (220.9, 848.6), (199.8, 1012.3), (173.4, 1207.6), (141.7, 1423.8), (110.1, 1615.6), (82.4, 1761.6), (57.5, 1889.7),
          (35.0, 1998.6), (16.1, 2086.2), (0.0, 2110.0)]


def f3():
    o = []
    x0, x1, y0, y1 = 80, 450, 46, 356
    fx = lambda m: x0 + (x1 - x0) * m / 275
    fy = lambda p: y1 - (y1 - y0) * p / 2300
    o.append(axes(x0, x1, y0, y1, [0, 50, 100, 150, 200, 250], [0, 500, 1000, 1500, 2000], fx, fy,
                  'M_u (kN·m)', 'P_u (kN)'))
    o[-1] = _sub(o[-1])
    pts = [(fx(m), fy(p)) for m, p in CURVE3]
    o.append(P(pts + [(fx(0), fy(0))], 'none', 0, fill=ACS, op=0.6))
    o.append(P(pts, AC, 3))
    o.append(L(fx(0), fy(1879), fx(59.6), fy(1879), NX, 2, dash='6 4'))
    o.append(Tb(fx(64), fy(1879) - 4, 'axial cap 1879 kN', 13, 'start', NX))
    o.append(C(fx(0), fy(2110), 5, AC))
    o.append(Tb(fx(6), fy(2110) - 10, 'P_uz = 2110 kN', 13, 'start', AC))
    o.append(C(fx(242.8), fy(429), 5, AC))
    o.append(T(fx(236), fy(429) + 5, 'balanced: 429 kN, 243 kN·m', 13, 'end', INK))
    o.append(C(fx(178.5), fy(0), 5, AC))
    o.append(T(fx(172), fy(0) - 12, 'pure bending 178', 13, 'end', INK))
    o.append(L(fx(150), fy(1200), fx(174), fy(1200), NX, 1.6, dash='3 3'))
    o.append(C(fx(150), fy(1200), 6, NX))
    o.append(C(fx(174), fy(1200), 4, AC))
    o.append(T(fx(146), fy(1200) - 12, 'design point (150, 1200)', 13, 'end', NX))
    o.append(Tb(fx(180), fy(1200) + 4, '174', 13, 'start', AC))
    o.append(T(fx(120), fy(700), 'safe', 15, fill=MUT, bold=True))
    o.append(T(fx(205), fy(1000), 'compression', 13, 'start', MUT))
    o.append(T(fx(205), fy(1000) + 16, 'failure', 13, 'start', MUT))
    o.append(T(fx(250), fy(200), 'tension', 13, 'start', MUT))
    o.append(T(fx(250), fy(200) + 16, 'failure', 13, 'start', MUT))
    # the section
    sx, sy, sc = 560, 48, 0.24
    o.append(R(sx, sy, 300 * sc, 500 * sc, PANEL, AC, 2, 2))
    for yy in (sy + 58 * sc, sy + (500 - 58) * sc):
        for i in range(4):
            o.append(bar(sx + 12 + i * (300 * sc - 24) / 3, yy, 4.2))
    o.append(dim(sx, sy + 136, sx + 72, sy + 136, '300', side='below'))
    o.append(dim(sx - 12, sy, sx - 12, sy + 120, '500', side='left'))
    o.append(boxt(478, 214, 236, 146, ['8 bars of 20 mm, M20', 'd′ = 58 mm, A_sc = 2513 mm²', 'at P_u = 1200 kN:',
                                       'x_u = 399 mm, M_u = 174 kN·m', 'needed 150 kN·m: safe'], PANEL, L2, 14, fills=[INK, MUT, INK, AC, NX]))
    return 410, ''.join(o)


FIG[3] = (f3, 'Interaction curve of the uniaxial worked example’s 300 mm × 500 mm section with 8 bars of 20 mm (M20), by strain compatibility. '
              'The design point (150 kN·m, 1200 kN) lies inside; at that load the curve gives 174 kN·m.',
          'A graph of axial load from 0 to 2300 kilonewtons against moment from 0 to 275 kilonewton metres. A curve rises from pure bending at 178 '
          'kilonewton metres, bulges to 243 at the balanced load of 429 kilonewtons and returns to 2110 kilonewtons at zero moment. A dashed cap at '
          '1879 kilonewtons, and the design point at 150 kilonewton metres and 1200 kilonewtons inside the curve, with the curve at 174.')


# ---- ch4: the 230 mm brick wall on a 1.2 m footing, with its critical sections ----
def f4():
    o = []
    s = 0.48
    x0, B, yt, D = 50, 1200 * s, 170, 250 * s
    wc = x0 + B / 2; t = 230 * s
    o.append(R(wc - t / 2, 44, t, yt - 44, NXS, NX, 0, 2))
    for yy in range(56, yt, 18):
        o.append(L(wc - t / 2, yy, wc + t / 2, yy, NX, 0.8))
    o.append(R(x0, yt, B, D, PANEL, AC, 0, 2))
    o.append(R(x0 - 10, yt + D, B + 20, 12, LN, L2, 0, 1))
    yb = yt + D - 27
    o.append(L(x0 + 12, yb, x0 + B - 12, yb, AC, 3))
    for xx in range(int(x0 + 25), int(x0 + B - 10), 40):
        o.append(bar(xx, yb - 7, 3.5, LV))
    o.append(up_arrows(x0 + 8, x0 + B - 8, yt + D + 14, yt + D + 52, 13))
    o.append(T(x0 + B / 2, yt + D + 72, 'net factored pressure w_u = 240/1.2 = 200 kN/m²', 14, fill=LV, bold=True))
    xm = wc - t / 2 + t / 4
    o.append(L(xm, yt - 26, xm, yt + D + 6, NX, 2, dash='6 4'))
    o.append(L(wc + t / 2 + 6, yt - 30, xm + 3, yt - 30, NX, 1.2))
    o.append(T(wc + t / 2 + 10, yt - 26, 'M_u section: t/4 inside the face', 13, 'start', NX))
    xs = wc - t / 2 - 195 * s
    o.append(L(xs, yt - 6, xs, yt + D + 6, AC, 2, dash='6 4'))
    o.append(Tb(xs - 6, yt - 12, 'shear at d = 195', 13, 'end', AC))
    o.append(dim(x0, yt + 50, xm, yt + 50, '542.5 mm'))
    o.append(dim(x0, 26, x0 + B, 26, 'B = 1.2 m'))
    o.append(L(x0, 30, x0, yt, L2, 1, dash='3 3')); o.append(L(x0 + B, 30, x0 + B, yt, L2, 1, dash='3 3'))
    o.append(dim(x0 + B + 16, yt, x0 + B + 16, yt + D, 'D = 250', side='right'))
    o.append(T(wc, 90, '230 mm', 13, fill=NX, bold=True))
    o.append(T(wc, 106, 'brick', 13, fill=NX))
    o.append(T(wc - t / 2 - 8, 70, '160 kN/m service', 13, 'end', INK))
    o.append(T(x0 + B / 2 + 60, yb + 20, '10 mm @ 175 across, 8 mm @ 160 along', 13, 'middle', INK))
    o.append(boxt(x0 + B / 2 - 134, 382, 268, 86, ['M_u = 200 × 0.5425²/2 = 29.43 kN·m/m', 'τ_v = 0.297 ≤ τ_c = 0.344 N/mm²', 'L_d 470 ≤ 492.5 mm available'],
                  PANEL, L2, 13))
    return 480, ''.join(o)


FIG[4] = (f4, 'The worked example’s wall footing in section: a 230 mm brick wall on a footing 1.2 m wide and 250 mm deep. Because the wall is masonry, the '
              'moment is taken a quarter of the wall thickness inside its face, 542.5 mm from the edge (29.43 kN·m/m); one-way shear is checked 195 mm '
              '(d) out from the face.',
          'Cross-section of a brick wall standing on a reinforced footing 1.2 metres wide and 250 millimetres deep, with upward soil pressure arrows '
          'of 200 kilonewtons per square metre, a dashed moment section a quarter of the wall thickness inside the wall face and a dashed shear '
          'section 195 millimetres out from the face, and the bottom bars.')


# ---- ch5: the 2.7 m x 2.5 m pad in plan with its critical sections, and the eccentric pad's pressure ----
def f5():
    o = []
    s = 0.12
    x0, y0, Lp, Bp = 40, 64, 2700 * s, 2500 * s
    cx, cy = x0 + Lp / 2, y0 + Bp / 2
    o.append(R(x0, y0, Lp, Bp, PANEL, AC, 0, 2))
    o.append(R(cx - 150, y0, 300, Bp, LVS, 'none', 0, 0))
    o.append(R(x0, y0, Lp, Bp, 'none', AC, 0, 2))
    cw, ch = 500 * s, 300 * s
    pw, ph = (500 + 534) * s, (300 + 534) * s
    o.append(R(cx - pw / 2, cy - ph / 2, pw, ph, 'none', NX, 8, 2, dash='6 4'))
    for xx in (cx - cw / 2 - 534 * s, cx + cw / 2 + 534 * s):
        o.append(L(xx, y0, xx, y0 + Bp, AC, 2, dash='6 4'))
    o.append(R(cx - cw / 2, cy - ch / 2, cw, ch, NXS, NX, 0, 2))
    o.append(T(cx, cy + 5, '300×500', 13, fill=NX, bold=True))
    o.append(dim(x0, y0 - 16, x0 + Lp, y0 - 16, 'L = 2.7 m'))
    o.append(L(x0 + Lp + 14, y0, x0 + Lp + 14, y0 + Bp, MUT, 1.4, arrow='m') + L(x0 + Lp + 14, y0 + Bp, x0 + Lp + 14, y0, MUT, 1.4, arrow='m'))
    o.append(Tb(x0 + Lp + 14, y0 + Bp / 2 + 5, '2.5 m', 13, fill=MUT))
    o.append(Tb(cx, cy - ph / 2 - 8, 'punching at d/2', 13, fill=NX))
    o.append(Tb(cx - cw / 2 - 534 * s, y0 + Bp - 14, 'shear at d', 13, fill=AC))
    o.append(T(cx, y0 + Bp + 22, 'central band 2.5 m holds 96 % of the short-way bars', 13, fill=LV))
    o.append(T(cx, y0 + Bp + 40, 'D = 600 mm, d = 534 mm', 13, fill=MUT))
    # eccentric pad: elevation and trapezoidal pressure
    ex, ey, sc = 420, 104, 0.1
    o.append(R(ex + 120, ey - 58, 40, 58, NXS, NX, 0, 2))
    o.append(R(ex, ey, 280, 36, PANEL, AC, 0, 2))
    o.append(L(ex + 140, ey - 96, ex + 140, ey - 62, NX, 3, arrow='x'))
    o.append(T(ex + 148, ey - 82, 'P = 900 kN', 13, 'start', NX, bold=True))
    o.append(arc(ex + 112, ey - 30, ex + 112, ey - 8, -0.9, NX, 2, 'x'))
    o.append(T(ex + 104, ey - 30, 'M = 90 kN·m', 13, 'end', NX))
    k = 0.30
    base = ey + 44
    q1, q2, qf = 266.1, 172.2, 225.9
    o.append(poly([(ex, base), (ex + 280, base), (ex + 280, base + q2 * k), (ex, base + q1 * k)], LVS, LV, 2))
    o.append(L(ex + 120, base, ex + 120, base + qf * k, NX, 2, dash='5 4'))
    o.append(T(ex - 4, base + q1 * k + 16, '266.1', 13, 'end', LV, bold=True))
    o.append(T(ex + 284, base + q2 * k + 16, '172.2', 13, 'end', LV, bold=True))
    o.append(Tb(ex + 124, base + qf * k - 6, 'face: 225.9', 13, 'start', NX))
    o.append(dim(ex, ey + 132, ex + 120, ey + 132, '1.20 m', side='below'))
    o.append(T(ex + 140, base + q1 * k + 56, 'L = 2.8 m, B = 2.2 m (kN/m², factored)', 13, fill=MUT))
    o.append(T(ex + 140, base + q1 * k + 76, 'M_u at the face = 400.3 kN·m', 14, fill=NX, bold=True))
    return 420, ''.join(o)


FIG[5] = (f5, 'Left: the first worked example’s 2.7 m × 2.5 m pad with its punching perimeter at d/2 and one-way shear sections at d. Right: the '
              'eccentric footing, factored pressure 266.1 to 172.2 kN/m², 400.3 kN·m at the column face.',
          'Plan of a rectangular footing 2.7 by 2.5 metres with a 300 by 500 millimetre column, a dashed punching perimeter round it and dashed one-way '
          'shear lines on both sides. Right, an elevation of a footing 2.8 metres long under a 900 kilonewton load and a 90 kilonewton metre moment, '
          'with a trapezoidal pressure diagram from 266.1 to 172.2 kilonewtons per square metre and 225.9 at the column face.')


# ---- ch6: the combined footing, factored load, shear force and bending moment diagrams ----
def f6():
    o = []
    x0, sc = 60, 120        # px per metre
    X = lambda m: x0 + sc * m
    o.append(R(X(0), 74, sc * 5, 30, PANEL, AC, 0, 2))
    for m, P_, lab in ((0.7, 900, '900 kN'), (3.7, 1350, '1350 kN')):
        o.append(R(X(m) - 24, 40, 48, 34, NXS, NX, 0, 2))
        o.append(L(X(m), 6, X(m), 36, NX, 3, arrow='x'))
        o.append(T(X(m) + 10, 22, lab, 13, 'start', NX, bold=True))
    o.append(up_arrows(X(0) + 4, X(5) - 4, 108, 132, 21))
    o.append(T(X(2.5), 150, 'w = 225 × 2.0 = 450 kN/m', 13, fill=LV, bold=True))
    o.append(T(X(5) + 6, 92, '5.0 m', 13, 'start', MUT))
    V = lambda x: 450 * x - (900 if x > 0.7 else 0) - (1350 if x > 3.7 else 0)
    M = lambda x: 225 * x * x - 900 * max(0, x - 0.7) - 1350 * max(0, x - 3.7)
    ys, kv = 236, 0.075
    o.append(L(X(0), ys, X(5), ys, L2, 1.5))
    pts = [(X(0), ys)]
    for a, b in ((0, 0.7), (0.7, 3.7), (3.7, 5.0)):
        pts += [(X(a), ys - kv * V(a + 1e-9)), (X(b), ys - kv * V(b - 1e-9))]
    pts.append((X(5), ys))
    o.append(P(pts, AC, 2.5))
    for x, v, dy, anc in ((0.7, 315, -8, 'end'), (0.7, -585, 16, 'start'), (3.7, 765, -8, 'end'), (3.7, -585, 16, 'start')):
        o.append(Tb(X(x) + (-6 if anc == 'end' else 6), ys - kv * v + dy, f'{v:+d}'.replace('-', '−'), 13, anc, INK))
    o.append(T(X(0) - 6, ys + 5, 'V', 14, 'end', MUT, bold=True))
    o.append(C(X(2.0), ys, 4, NX))
    o.append(Tb(X(2.0) + 6, ys + 20, 'V = 0 at 2.0 m', 13, 'start', NX))
    yb, km = 386, 0.13
    o.append(L(X(0), yb, X(5), yb, L2, 1.5))
    o.append(P([(X(i / 100), yb - km * M(i / 100)) for i in range(501)], NX, 2.5))
    o.append(Tb(X(0.7), yb - km * 110.25 - 10, '+110.3', 13, fill=INK))
    o.append(Tb(X(2.0), yb + km * 270 + 18, '−270 (hogging: top steel)', 13, fill=INK))
    o.append(Tb(X(3.7), yb - km * 380.25 - 10, '+380.3', 13, fill=INK))
    o.append(T(X(0) - 6, yb + 5, 'M', 14, 'end', MUT, bold=True))
    o.append(dim(X(0), 458, X(0.7), 458, '0.7', side='below'))
    o.append(dim(X(0.7), 458, X(3.7), 458, '3.0 m', side='below'))
    o.append(dim(X(3.7), 458, X(5), 458, '1.3', side='below'))
    return 490, ''.join(o)


FIG[6] = (f6, 'The worked example’s combined footing, 5.0 m long and 2.0 m wide, under factored column loads of 900 kN and 1350 kN, with the upward '
              'line load of 450 kN/m. The shear is zero 2.0 m from the left end, where the hogging moment of 270 kN·m puts tension at the top; the '
              'sagging moments under the columns are 110.3 and 380.3 kN·m (kN and kN·m).',
          'An elevation of a long footing under two columns 3 metres apart, 0.7 metres and 1.3 metres from the ends, with uniform upward arrows of 450 '
          'kilonewtons per metre. Below it a shear force diagram with values plus 315, minus 585, plus 765 and minus 585, crossing zero at 2.0 metres, '
          'and a bending moment diagram with plus 110.3 and plus 380.3 under the columns and minus 270 between them.')


# ---- ch7: the 4.5 m cantilever retaining wall with its thrust, weights and base pressure ----
def f7():
    o = []
    s = 70                  # px per metre
    x0, yb = 110, 380       # toe edge, underside of base
    X = lambda m: x0 + s * m
    Y = lambda m: yb - s * m
    o.append(poly([(X(0), Y(0)), (X(2.7), Y(0)), (X(2.7), Y(0.35)), (X(0), Y(0.35))], PANEL, AC, 2))
    o.append(poly([(X(0.9), Y(0.35)), (X(1.2), Y(0.35)), (X(1.2), Y(4.5)), (X(1.0), Y(4.5))], PANEL, AC, 2))
    o.append(poly([(X(1.2), Y(0.35)), (X(2.7), Y(0.35)), (X(2.7), Y(4.5)), (X(1.2), Y(4.5))], NXS, 'none', 0))
    for i in range(6):
        yy = Y(0.6 + 0.65 * i)
        o.append(L(X(1.3), yy, X(2.6), yy, NX, 0.7, dash='2 6'))
    o.append(T(X(1.95), Y(2.5), 'soil on heel', 13, fill=NX, bold=True))
    o.append(T(X(1.95), Y(2.5) + 16, '112.05 kN', 13, fill=NX))
    o.append(L(X(2.7), Y(4.5), X(2.7), Y(0), L2, 1.2, dash='5 4'))
    # earth pressure triangle on the virtual back through the heel
    base_p = 27.0
    o.append(poly([(X(2.7), Y(4.5)), (X(2.7) + base_p * 3.0, Y(0)), (X(2.7), Y(0))], LVS, LV, 2))
    o.append(L(X(2.7) + 74, Y(1.5), X(2.7) + 4, Y(1.5), LV, 3, arrow='l'))
    o.append(T(X(2.7) + 84, Y(1.5) - 10, 'P_a = 60.75 kN', 13, 'start', LV, bold=True))
    o.append(T(X(2.7) + 84, Y(1.5) + 8, 'at H/3 = 1.5 m', 13, 'start', LV))
    o.append(T(X(2.7) + 84, Y(0) - 4, 'K_a γH = 27 kN/m²', 13, 'start', LV))
    # weights
    o.append(L(X(1.1), Y(3.2), X(1.1), Y(2.6), AC, 2.4, arrow='n'))
    o.append(T(X(1.1) - 22, Y(3.5), 'stem 25.94', 13, 'end', AC))
    o.append(L(X(1.35), Y(0.35) - 30, X(1.35), Y(0.2), AC, 2.4, arrow='n'))
    o.append(T(X(0.45), Y(0.35) - 14, 'base 23.62', 13, 'middle', AC))
    # base pressure
    kp = 0.75
    o.append(poly([(X(0), yb + 8), (X(2.7), yb + 8), (X(2.7), yb + 8 + 34.3 * kp), (X(0), yb + 8 + 85.4 * kp)], LVS, LV, 2))
    o.append(T(X(0) - 4, yb + 8 + 85.4 * kp + 16, '85.4 kN/m²', 13, 'start', LV, bold=True))
    o.append(T(X(2.7) + 4, yb + 8 + 34.3 * kp + 14, '34.3', 13, 'start', LV, bold=True))
    o.append(dim(X(0), Y(4.5) - 14, X(0.9), Y(4.5) - 14, 'toe 0.9'))
    o.append(dim(X(1.2), Y(4.5) - 14, X(2.7), Y(4.5) - 14, 'heel 1.5'))
    o.append(dim(X(0) - 20, Y(0), X(0) - 20, Y(4.5), 'H = 4.5 m', side='left'))
    o.append(L(X(0.9), Y(4.5) - 20, X(0.9), Y(4.5) + 2, L2, 1, dash='3 3'))
    o.append(L(X(1.2), Y(4.5) - 20, X(1.2), Y(4.5) + 2, L2, 1, dash='3 3'))
    o.append(T(X(1.1), Y(4.5) - 46, 'stem 0.2 → 0.3', 13, fill=MUT))
    o.append(boxt(486, 40, 230, 112, ['M_R = 278.2, M_O = 91.1 kN·m', 'overturning 0.9M_R ≥ 1.4M_O: safe', 'sliding 72.7 < 85.0 kN: key', 'e = 0.192 m < B/6 = 0.45 m'],
                  PANEL, L2, 13, fills=[INK, INK, NX, INK]))
    return 490, ''.join(o)


FIG[7] = (f7, 'The worked example’s cantilever wall, 4.5 m high with a 2.7 m base (toe 0.9 m, heel 1.5 m) and a stem tapering from 0.3 m to 0.2 m. '
              'The active thrust of 60.75 kN/m acts 1.5 m up on the vertical plane through the heel; the soil on the heel and the concrete hold the wall '
              'down, and the base pressure runs from 85.4 kN/m² at the toe to 34.3 kN/m² at the heel.',
          'Cross-section of an inverted T retaining wall with a toe of 0.9 metres, a heel of 1.5 metres carrying the backfill, and a stem 4.5 metres '
          'high. A triangular earth pressure diagram reaching 27 kilonewtons per square metre at the base acts on a vertical line through the heel, '
          'with the resultant of 60.75 kilonewtons at 1.5 metres. Below the base, a trapezoidal pressure from 85.4 to 34.3.')


# ---- ch8: the 6 m circular tank: water pressure on the wall and hoop tension in a ring ----
def f8():
    o = []
    s = 70
    x0, yb = 70, 340
    Y = lambda m: yb - s * m
    o.append(R(x0, Y(3.8), 14, s * 3.8, PANEL, AC, 0, 2))
    o.append(R(x0 + 14, Y(3.5), 190, s * 3.5, LVS, 'none', 0, 0))
    o.append(L(x0 + 14, Y(3.5), x0 + 204, Y(3.5), LV, 1.6))
    o.append(T(x0 + 150, Y(3.5) - 8, 'water surface', 13, fill=LV))
    o.append(R(x0 - 6, yb, 230, 16, PANEL, AC, 0, 2))
    o.append(T(x0 + 120, yb + 34, 'base slab, flexible joint at the wall', 13, fill=MUT))
    kp = 2.4
    o.append(poly([(x0 + 14, Y(3.5)), (x0 + 14, yb), (x0 + 14 + 35 * kp, yb)], 'none', LV, 2))
    for h in (1.0, 2.0, 3.0):
        w = 10 * h * kp
        o.append(L(x0 + 14 + w, Y(3.5 - h), x0 + 16, Y(3.5 - h), LV, 1.6, arrow='l'))
    o.append(Tb(x0 + 14 + 35 * kp + 4, yb - 10, 'p = 35 kN/m²', 13, 'start', LV))
    o.append(dim(x0 + 218, Y(3.5), x0 + 218, yb, 'H = 3.5 m', side='right'))
    o.append(T(x0 + 7, Y(3.8) - 8, 't = 150', 13, fill=AC))
    # plan of a ring cut in half
    cx, cy, R0 = 520, 200, 120
    o.append(f'<path d="M{cx - R0 - 12},{cy} A{R0 + 12},{R0 + 12} 0 0 1 {cx + R0 + 12},{cy} L{cx + R0},{cy} A{R0},{R0} 0 0 0 {cx - R0},{cy} Z" '
             f'style="fill:var(--panel);stroke:var(--accent);stroke-width:2"/>')
    for i in range(1, 8):
        a = math.pi * i / 8
        o.append(L(cx + 50 * math.cos(a), cy - 50 * math.sin(a), cx + (R0 - 4) * math.cos(a), cy - (R0 - 4) * math.sin(a), LV, 1.6, arrow='l'))
    o.append(L(cx - R0 - 6, cy + 8, cx - R0 - 6, cy + 54, NX, 3, arrow='x'))
    o.append(L(cx + R0 + 6, cy + 8, cx + R0 + 6, cy + 54, NX, 3, arrow='x'))
    o.append(T(cx - R0 - 14, cy + 50, 'T', 15, 'end', NX, bold=True))
    o.append(T(cx + R0 + 16, cy + 50, 'T', 15, 'start', NX, bold=True))
    o.append(dim(cx, cy + 14, cx + R0, cy + 14, 'r = 3 m', side='below'))
    o.append(T(cx, cy - 18, 'p = 35', 13, fill=LV, bold=True))
    o.append(T(cx, 40, 'a 1 m ring at the base, cut in half', 14, fill=MUT))
    o.append(boxt(392, 286, 300, 92, ['2T = p × 2r: T = 35 × 3 = 105 kN/m', 'A_s = 105 000/130 = 808 mm²/m', '12 mm rings @ 130 c/c (870 mm²/m)'],
                  PANEL, L2, 13, fills=[NX, INK, AC]))
    return 400, ''.join(o)


FIG[8] = (f8, 'The worked example’s 6 m tank. Left: water 3.5 m deep presses on the 150 mm wall with a pressure that grows from zero to 35 kN/m² at the '
              'base. Right: a 1 m high ring at the base cut in half; the water pushes on 2r = 6 m and the two cut ends pull back with 2T, so T = pr = '
              '105 kN/m, carried by 12 mm rings at 130 mm.',
          'Left, a tank wall in section with a triangular water pressure diagram reaching 35 kilonewtons per square metre at the 3.5 metre depth. '
          'Right, half of a circular ring of radius 3 metres with water pressure arrows pushing outward and a hoop tension T at each cut end, and a box '
          'giving T of 105 kilonewtons per metre and 12 millimetre rings at 130 millimetres.')


_base_spec = make_spec(FIG)
AFTER = {1: 2, 2: 2, 3: 2, 4: 1, 5: 2, 6: 1, 7: 1, 8: 2}


def spec(k):
    d = _base_spec(k)
    d['after_section'] = AFTER.get(k, 1)
    return d
