"""Claude's hand-drawn figures for ce-rcc-u3 (Design of Reinforced Concrete Structures: shear, torsion and bond), one per
chapter, drawn from each chapter's own worked example and numbers. Colours are the shell's CSS variables."""
import os, sys, math, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

_T, _Tb, _boxt = T, Tb, boxt


def _sub(s):
    """V_us, tau_c,max ... drawn as real subscripts, never as underscores"""
    return re.sub(r'([A-Za-zα-ωτσφ])_([A-Za-z0-9,]+)', r'\1<tspan baseline-shift="sub" font-size="11">\2</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)
def boxt(x, y, w, h, lines, *a, **k): return _boxt(x, y, w, h, [_sub(l) for l in lines], *a, **k)


def dim(x1, y1, x2, y2, label, side=-1, size=13, c=MUT, off=16):
    """dimension line with end ticks and a label on a background patch"""
    o = [L(x1, y1, x2, y2, c, 1.3)]
    if y1 == y2:
        o += [L(x1, y1 - 6, x1, y1 + 6, c, 1.3), L(x2, y2 - 6, x2, y2 + 6, c, 1.3)]
        o.append(Tb((x1 + x2) / 2, y1 + (5 if side > 0 else -6) + (off - 4 if side > 0 else 0), label, size, fill=INK))
    else:
        o += [L(x1 - 6, y1, x1 + 6, y1, c, 1.3), L(x2 - 6, y2, x2 + 6, y2, c, 1.3)]
    return ''.join(o)


def bar(x, y, r, c=INK):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" style="fill:{c};stroke:var(--fig);stroke-width:1"/>'


# ---- 3.1 a cracked beam end as a free body, and the tau scale of worked example 2 ----
def f1():
    o = []
    top, bot = 60, 240
    o.append(R(40, top, 640, bot - top, PANEL, L2, 4, 1.5))
    # the free body left of the crack, tinted
    crack = [(300, bot), (318, 208), (352, 172), (408, 136), (468, 112)]
    poly = [(40, top), (468, top)] + list(reversed(crack)) + [(40, bot)]
    o.append(f'<polygon points="{" ".join(f"{x},{y}" for x, y in poly)}" style="fill:var(--accent-soft);stroke:none"/>')
    o.append(R(40, top, 640, bot - top, 'none', AC, 4, 2))
    # support
    o.append(f'<polygon points="100,{bot} 84,{bot + 24} 116,{bot + 24}" style="fill:var(--panel);stroke:{INK};stroke-width:1.6"/>')
    o.append(L(100, bot + 62, 100, bot + 30, NX, 2.5, arrow='x'))
    o.append(T(112, bot + 58, 'V (reaction)', 13, 'start', NX))
    # main bar and stirrups
    o.append(L(46, bot - 20, 674, bot - 20, INK, 3))
    o.append(T(660, bot - 28, 'main bars', 13, 'end', MUT))
    for x in range(160, 661, 60):
        o.append(L(x, top + 10, x, bot - 14, L2, 2))
    o.append(T(640, top + 26, 'stirrups', 13, 'end', MUT))
    # crack
    o.append(P(crack, NX, 3))
    o.append(Tb(520, 104, 'inclined crack', 13, 'start', NX))
    o.append(L(516, 100, 474, 112, NX, 1.2))
    # compression zone at the crack tip: C and V_cz
    o.append(L(468, top, 468, 112, INK, 1.2, '4 3'))
    o.append(L(462, 80, 410, 80, AC, 2.5, arrow='n'))
    o.append(T(404, 85, 'C', 14, 'end', AC, bold=True))
    o.append(L(478, 74, 478, 104, AC, 2.5, arrow='n'))
    o.append(T(486, 90, 'V_cz', 14, 'start', AC, bold=True))
    # aggregate interlock along the crack
    o.append(L(394, 134, 366, 152, LV, 2.5, arrow='l'))
    o.append(Tb(360, 132, 'V_a', 14, 'end', LV, bold=True))
    # dowel and tension at the bar
    o.append(L(304, bot - 20, 304, bot + 6, LV, 2.5, arrow='l'))
    o.append(Tb(292, bot + 14, 'V_d', 14, 'end', LV, bold=True))
    o.append(L(306, bot - 32, 352, bot - 32, AC, 2.5, arrow='n'))
    o.append(Tb(360, bot - 36, 'T', 14, 'start', AC, bold=True))
    # stirrup forces where the crack crosses them
    for x, y in ((340, 182), (400, 140), (460, 114)):
        o.append(C(x, y, 4.5, NX))
        o.append(L(x, y + 8, x, y + 34, AC, 2.5, arrow='n'))
    o.append(Tb(420, 196, 'V_s (stirrups crossing the crack)', 13, 'start', AC))
    o.append(T(60, top - 14, 'Free body between the support and the crack:  V = V_cz + V_a + V_d + V_s', 14, 'start'))
    # tau scale (worked example 2)
    y0 = 360
    fx = lambda v: 60 + v / 3.5 * 620
    o.append(R(fx(0), y0 - 14, fx(0.61) - fx(0), 28, LVS, LV, 0, 1))
    o.append(R(fx(0.61), y0 - 14, fx(3.1) - fx(0.61), 28, ACS, AC, 0, 1))
    o.append(R(fx(3.1), y0 - 14, fx(3.5) - fx(3.1), 28, NXS, NX, 0, 1))
    o.append(T(fx(0.30), y0 + 32, 'minimum', 13, fill=LV))
    o.append(T(fx(0.30), y0 + 48, 'stirrups', 13, fill=LV))
    o.append(T(fx(2.0), y0 + 5, 'design stirrups for V_us = V_u − τ_c b d', 13))
    o.append(T(fx(3.3), y0 + 32, 'enlarge', 13, fill=NX))
    o.append(T(fx(3.3), y0 + 48, 'section', 13, fill=NX))
    for v, lab in ((0.61, 'τ_c = 0.61'), (1.09, 'τ_v = 1.09'), (3.1, 'τ_c,max = 3.1')):
        o.append(L(fx(v), y0 - 22, fx(v), y0 + 16, INK, 2))
        o.append(T(fx(v), y0 - 28, lab, 13, 'middle' if v > 1 else 'start'))
    o.append(C(fx(1.09), y0, 6, INK))
    o.append(T(fx(0), y0 + 70, 'Worked example 2, M25, p_t = 0.89 %: shear stress in N/mm²', 13, 'start', MUT))
    return 450, ''.join(o)


# ---- 3.2 shear diagram over half the span and the stirrup zones (worked example 2) ----
def f2():
    o = []
    x0, x1, yb, yt = 90, 690, 270, 50
    fx = lambda m: x0 + m / 3.0 * (x1 - x0)
    fy = lambda v: yb - v / 260 * (yb - yt)
    o.append(axes(x0, x1, yt, yb, [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0], [0, 50, 100, 150, 200, 250], fx, fy,
                  'distance from the support face (m)', 'shear V (kN)', lambda v: f'{v:g}'))
    o.append(P([(fx(0), fy(240)), (fx(3), fy(0))], AC, 3))
    o.append(L(fx(0), fy(100.65), fx(3), fy(100.65), LV, 1.8, '6 4'))
    o.append(Tb(fx(2.15), fy(100.65) - 7, 'concrete τ_c b d = 100.65', 13, 'start', LV))
    o.append(L(fx(0), fy(167.2), fx(3), fy(167.2), NX, 1.8, '6 4'))
    o.append(Tb(fx(1.55), fy(167.2) - 7, 'with stirrups at 300 mm: 167.2', 13, 'start', NX))
    o.append(C(fx(0.55), fy(196), 6, AC))
    o.append(Tb(fx(0.55) + 12, fy(196) - 10, 'critical section: 196 kN at d = 0.55 m', 13, 'start'))
    o.append(C(fx(0.91), fy(167.2), 6, NX))
    o.append(L(fx(0.91), fy(167.2), fx(0.91), yb, NX, 1.3, '3 3'))
    o.append(Tb(fx(0.91) - 8, fy(120), '0.91 m', 13, 'end', NX))
    o.append(Tb(fx(0) + 10, fy(240) - 4, '240 kN at the face', 13, 'start'))
    # beam strip with stirrups
    by, bh = 340, 70
    o.append(R(fx(0) - 40, by, fx(3) - fx(0) + 40, bh, PANEL, L2, 2, 1.5))
    o.append(R(fx(0) - 40, by, 40, bh + 18, 'var(--line)', INK, 0, 1.2))
    o.append(T(fx(0) - 20, by + bh + 34, 'support', 13, fill=MUT))
    xs = [0.05 + 0.2 * i for i in range(6)] + [1.05 + 0.3 * i for i in range(1, 7)]
    for m in xs:
        o.append(L(fx(m), by + 6, fx(m), by + bh - 6, AC if m <= 1.06 else LV, 2.2))
    o.append(L(fx(0), by + bh - 12, fx(3), by + bh - 12, INK, 2.5))
    o.append(brace(fx(0.05), fx(1.0), by - 10, INK, up=True))
    o.append(T((fx(0.05) + fx(1.0)) / 2, by - 18, '8 mm @ 200 to 1.0 m', 13, fill=AC, bold=True))
    o.append(brace(fx(1.0), fx(3.0), by - 10, INK, up=True))
    o.append(T((fx(1.0) + fx(3.0)) / 2, by - 18, '8 mm @ 300 to midspan', 13, fill=LV, bold=True))
    o.append(T(fx(3) - 4, by + bh + 34, 'midspan', 13, 'end', MUT))
    o.append(T(fx(0.05), by + bh + 34, 'first stirrup 50 mm from the face', 13, 'start', MUT))
    return 460, ''.join(o)


# ---- 3.3 torsion: the section with its closed stirrup and the side face with spiral cracks ----
def f3():
    o = []
    s = 0.5                      # px per mm
    X, Y = 90, 50                # top-left of the section
    W, H = 300 * s, 600 * s
    o.append(R(X, Y, W, H, PANEL, INK, 2, 2))
    c = (30 + 5) * s             # stirrup centreline
    o.append(R(X + c, Y + c, W - 2 * c, H - 2 * c, 'none', AC, 6, 3))
    # corner bars: bottom 20 mm at 50 mm, top 12 mm at 46 mm
    for xx in (X + 50 * s, X + W - 50 * s):
        o.append(bar(xx, Y + H - 50 * s, 10 * s + 1))
        o.append(bar(xx, Y + 46 * s, 6 * s + 1))
    for xx in (X + 50 * s + 200 * s / 3, X + 50 * s + 400 * s / 3):
        o.append(bar(xx, Y + H - 50 * s, 10 * s + 1))
    # shear flow round the section
    m = 16
    o.append(L(X + W / 2 - 30, Y - m + 4, X + W / 2 + 30, Y - m + 4, NX, 2.5, arrow='x'))
    o.append(L(X + W + m, Y + H / 2 - 40, X + W + m, Y + H / 2 + 40, NX, 2.5, arrow='x'))
    o.append(L(X + W / 2 + 30, Y + H + m - 2, X + W / 2 - 30, Y + H + m - 2, NX, 2.5, arrow='x'))
    o.append(L(X - m, Y + H / 2 + 40, X - m, Y + H / 2 - 40, NX, 2.5, arrow='x'))
    o.append(T(X + W + m + 8, Y + H / 2 + 5, 'shear flow', 13, 'start', NX))
    # dimensions b1, d1
    o.append(dim(X + 50 * s, Y + H + 40, X + W - 50 * s, Y + H + 40, 'b_1 = 200', 1))
    o.append(dim(X - 46, Y + 46 * s, X - 46, Y + H - 50 * s, ''))
    o.append(Tb(X - 46, Y + H / 2 + 60, 'd_1 = 504', 13))
    o.append(T(X + W / 2, Y + H + 92, '300 × 600 section, 30 mm cover', 13, fill=MUT))
    o.append(T(X + W / 2, Y + H + 110, '10 mm closed stirrup (230 × 530)', 13, fill=MUT))
    # side face with spiral cracks and stirrups
    sx, sy, sw, sh = 330, 70, 360, H - 40
    o.append(R(sx, sy, sw, sh, PANEL, INK, 2, 2))
    for i in range(9):
        xx = sx + 20 + i * 40
        o.append(L(xx, sy + 8, xx, sy + sh - 8, AC, 2))
    for i in range(5):
        x0 = sx + 30 + i * 70
        o.append(P([(x0, sy + sh - 10), (x0 + sh - 20, sy + 10)] if x0 + sh - 20 < sx + sw - 10 else
                   [(x0, sy + sh - 10), (sx + sw - 10, sy + sh - 10 - (sx + sw - 10 - x0))], NX, 2.2))
    o.append(arc(sx + 10, sy - 20, sx + 60, sy - 20, 0.45, LV, 2.5, 'l'))
    o.append(T(sx + 70, sy - 18, 'T_u = 30 kN·m', 14, 'start', LV, bold=True))
    o.append(Tb(sx + sw / 2, sy + sh + 26, 'side face: 45° cracks, stirrups at 140 mm', 13, fill=INK))
    o.append(T(sx, sy + sh + 60, 'V_e = 120 + 1.6 × 30/0.3 = 280 kN', 14, 'start'))
    o.append(T(sx, sy + sh + 82, 'τ_ve = 1.70 N/mm²  (τ_c = 0.57, τ_c,max = 3.1)', 14, 'start'))
    o.append(T(sx, sy + sh + 104, 's_v = 144.4 mm, provide 140 mm', 14, 'start', AC, bold=True))
    return 470, ''.join(o)


# ---- 3.4 the edge beam: from the three actions to the final section ----
def f4():
    o = []
    o.append(boxt(20, 30, 150, 50, ['M_u = 150 kN·m'], PANEL, INK, 14))
    o.append(boxt(20, 110, 150, 50, ['T_u = 30 kN·m'], LVS, LV, 14))
    o.append(boxt(20, 190, 150, 50, ['V_u = 120 kN'], PANEL, INK, 14))
    o.append(boxt(220, 70, 190, 50, ['M_t = 30 × 3/1.7', '= 52.94 kN·m'], LVS, LV, 13))
    o.append(boxt(220, 160, 190, 50, ['V_e = 120 + 160', '= 280 kN'], LVS, LV, 13))
    o.append(boxt(220, 250, 190, 50, ['τ_ve = 1.70 N/mm²', '< τ_c,max = 3.1'], PANEL, AC, 13))
    o.append(boxt(220, 332, 190, 70, ['M_e1 = 150 + 52.94', '= 202.94 kN·m', 'A_st = 1157 mm²'], ACS, AC, 13))
    o.append(L(170, 135, 218, 100, LV, 2, arrow='l'))
    o.append(L(170, 135, 218, 182, LV, 2, arrow='l'))
    o.append(L(170, 215, 218, 190, INK, 2, arrow='n'))
    o.append(L(315, 210, 315, 248, AC, 2, arrow='n'))
    o.append(P([(170, 55), (195, 55), (195, 368), (218, 368)], AC, 2))
    o.append(L(410, 95, 432, 95, AC, 1.5))
    o.append(P([(432, 95), (432, 368), (412, 368)], AC, 1.5))
    # final section, 0.45 px/mm
    s = 0.45
    X, Y = 462, 40
    W, H = 300 * s, 600 * s
    o.append(R(X, Y, W, H, PANEL, INK, 2, 2))
    c = 35 * s
    o.append(R(X + c, Y + c, W - 2 * c, H - 2 * c, 'none', AC, 6, 3))
    yb = Y + H - 50 * s
    for i in range(4):
        o.append(bar(X + 50 * s + i * 200 * s / 3, yb, 10 * s + 1))
    for xx in (X + 46 * s, X + W - 46 * s):
        o.append(bar(xx, Y + 46 * s, 6 * s + 1))
        o.append(bar(xx, Y + H / 2, 6 * s + 1, LV))
    o.append(T(X + W + 12, yb + 5, '4 × 20 (1257)', 13, 'start'))
    o.append(T(X + W + 12, Y + 46 * s + 5, '2 × 12', 13, 'start'))
    o.append(T(X + W + 12, Y + H / 2 + 5, '1 × 12', 13, 'start', LV))
    o.append(T(X + W + 12, Y + H / 2 + 21, 'each face', 13, 'start', LV))
    o.append(T(X + W / 2, Y + H + 26, '10 mm closed stirrups @ 140', 13, fill=AC, bold=True))
    o.append(T(X + W / 2, Y + H + 46, '135° hooks, cover 30 mm', 13, fill=MUT))
    o.append(L(434, 200, X - 6, 200, AC, 2, arrow='n'))
    return 410, ''.join(o)


# ---- 3.5 anchorage check at the simple support (worked example 2) ----
def f5():
    o = []
    s = 0.5
    face = 230                      # x of the support face (span side)
    wall0 = face - 300 * s          # outer face of the wall
    cl = face - 150 * s             # support centre line
    bot = 200
    o.append(R(wall0, bot, 300 * s, 120, 'var(--line)', INK, 0, 1.5))
    o.append(T(wall0 + 36, bot + 60, '300 mm', 13, fill=MUT))
    o.append(T(wall0 + 36, bot + 78, 'wall', 13, fill=MUT))
    o.append(R(wall0, 60, 700 - wall0, bot - 60, PANEL, L2, 2, 1.5))
    end = wall0 + 30 * s
    yb = bot - 50 * s
    o.append(L(end, yb, 700, yb, AC, 5))
    o.append(T(690, yb - 10, '2 bars of 20 mm', 13, 'end', AC, bold=True))
    o.append(L(cl, 40, cl, bot + 130, INK, 1.2, '6 4'))
    o.append(T(cl, 34, 'support centre', 13, fill=MUT))
    o.append(L(cl, bot + 2, cl, bot + 0, INK, 1))
    for xx in range(int(face) + 30, 690, 40):
        o.append(L(xx, 72, xx, bot - 14, L2, 1.6))
    o.append(L(cl, bot + 170, cl, bot + 140, NX, 2.5, arrow='x'))
    o.append(T(cl + 10, bot + 165, 'V = 180 kN', 13, 'start', NX))
    # dimension rows
    r1 = 90
    o.append(dim(end, r1, cl, r1, ''))
    o.append(Tb((end + cl) / 2, r1 - 10, 'L_0 = 120', 13))
    x13 = cl + 843.9 * s
    o.append(dim(cl, r1, x13, r1, '1.3 M_1/V = 844 mm'))
    o.append(dim(end, 130, end + 805.9 * s, 130, 'L_d = 806 mm ≤ 120 + 844 = 964 mm', -1))
    o.append(dim(end, bot - 8, face, bot - 8, ''))
    o.append(Tb(end + 2, bot + 18, 'L_d/3 = 269 ≤ 270 into the support', 13, 'start'))
    o.append(T(wall0, bot + 220, 'M_1 = 116.84 kN·m for the two bars, so 1.3 M_1/V = 1.3 × 116.84 × 10⁶/(180 × 10³) = 844 mm', 13, 'start', MUT))
    return 440, ''.join(o)


# ---- 3.6 curtailment: moment diagram, bar capacities and the cut-off points (worked example 1) ----
def f6():
    o = []
    x0, x1, yb, yt = 80, 680, 280, 50
    fx = lambda m: x0 + m / 6.0 * (x1 - x0)
    fy = lambda v: yb - v / 130 * (yb - yt)
    o.append(axes(x0, x1, yt, yb, [0, 1, 2, 3, 4, 5, 6], [0, 25, 50, 75, 100, 125], fx, fy,
                  'distance from the left support (m)', 'M (kN·m)', lambda v: f'{v:g}'))
    o.append(P([(fx(t / 20), fy(110 * 4 * (t / 20) * (6 - t / 20) / 36)) for t in range(0, 121)], AC, 3))
    o.append(L(fx(0), fy(117.7), fx(6), fy(117.7), INK, 1.6, '6 4'))
    o.append(Tb(fx(0.15), fy(117.7) - 8, '4 bars: M_R = 117.7', 13, 'start'))
    o.append(L(fx(0), fy(62.1), fx(6), fy(62.1), LV, 1.8, '6 4'))
    o.append(Tb(fx(2.15), fy(62.1) + 20, '2 bars: M_R = 62.1', 13, 'start', LV))
    o.append(Tb(fx(3), fy(110) + 22, 'M_u = 110 kN·m', 13))
    for xc in (1.02, 4.98):
        o.append(C(fx(xc), fy(62.1), 6, LV))
        o.append(L(fx(xc), fy(62.1), fx(xc), yb, LV, 1.3, '3 3'))
    o.append(Tb(fx(1.02) + 8, fy(40), '1.02 m', 13, 'start', LV))
    o.append(Tb(fx(4.98) - 8, fy(40), '4.98 m', 13, 'end', LV))
    # bars below
    y2, y4 = 360, 390
    o.append(L(fx(0) + 4, y2, fx(6) - 4, y2, INK, 4))
    o.append(T(fx(6), y2 - 10, '2 bars of 16 mm run full length', 13, 'end', MUT))
    o.append(L(fx(0.57), y4, fx(5.43), y4, AC, 4))
    o.append(T(fx(3), y4 + 24, '2 bars of 16 mm, 0.57 m to 5.43 m', 13, fill=AC, bold=True))
    for a, b in ((0.57, 1.02), (4.98, 5.43)):
        o.append(L(fx(a), y4 - 14, fx(b), y4 - 14, NX, 1.4))
        o.append(L(fx(a), y4 - 20, fx(a), y4 - 8, NX, 1.4)); o.append(L(fx(b), y4 - 20, fx(b), y4 - 8, NX, 1.4))
    o.append(Tb(fx(0.6), y4 + 24, 'd = 450', 13, 'middle', NX))
    o.append(Tb(fx(5.4), y4 + 24, 'd = 450', 13, 'middle', NX))
    return 430, ''.join(o)


# ---- 3.7 section detail of the edge beam (worked example 1) ----
def f7():
    o = []
    s = 0.62
    X, Y = 150, 40
    W, H = 300 * s, 600 * s
    o.append(R(X, Y, W, H, PANEL, INK, 2, 2))
    c = 35 * s
    o.append(R(X + c, Y + c, W - 2 * c, H - 2 * c, 'none', AC, 7, 10 * s))
    yb = Y + H - 50 * s
    xs = [X + 50 * s + i * (200 / 3) * s for i in range(4)]
    for xx in xs:
        o.append(bar(xx, yb, 10 * s))
    for xx in (X + 46 * s, X + W - 46 * s):
        o.append(bar(xx, Y + 46 * s, 6 * s))
        o.append(bar(xx, Y + H / 2, 6 * s, LV))
    # cover and stirrup dims on the left bottom corner (zoomed labels)
    o.append(T(X + W / 2, Y + H + 26, 'nominal cover 30 mm to the stirrup', 13, fill=MUT))
    # clear gap between bars 1 and 2
    gx1, gx2 = xs[0] + 10 * s, xs[1] - 10 * s
    o.append(L(gx1, yb - 16, gx2, yb - 16, NX, 1.6))
    o.append(L(gx1, yb - 22, gx1, yb - 10, NX, 1.4)); o.append(L(gx2, yb - 22, gx2, yb - 10, NX, 1.4))
    o.append(T((gx1 + gx2) / 2 + 4, yb - 52, 'clear gap', 13, 'start', NX, bold=True))
    o.append(T((gx1 + gx2) / 2 + 4, yb - 36, '46.7 mm', 13, 'start', NX, bold=True))
    o.append(L((gx1 + gx2) / 2 + 2, yb - 34, (gx1 + gx2) / 2, yb - 18, NX, 1.2))
    # effective depth
    o.append(dim(X + W + 40, Y, X + W + 40, yb, ''))
    o.append(Tb(X + W + 40, Y + H / 2 - 40, 'd = 550', 13))
    o.append(L(X + W + 34, yb, xs[-1] + 8, yb, MUT, 1, '3 3'))
    # side-face gaps
    o.append(dim(X + W + 100, Y + 46 * s, X + W + 100, Y + H / 2, ''))
    o.append(Tb(X + W + 100, Y + H / 4 + 23 * s, '254', 13))
    o.append(dim(X + W + 100, Y + H / 2, X + W + 100, yb, ''))
    o.append(Tb(X + W + 100, Y + 3 * H / 4 - 25 * s, '250', 13))
    # labels on the left
    o.append(T(X - 14, Y + 46 * s + 5, '2 × 12 top', 13, 'end'))
    o.append(T(X - 14, Y + H / 2 + 5, '1 × 12 side bar', 13, 'end', LV))
    o.append(T(X - 14, yb - 26, '4 × 20 bottom', 13, 'end'))
    o.append(T(X - 14, Y + 120, '10 mm stirrup', 13, 'end', AC))
    o.append(L(X - 10, Y + 116, X + c - 2, Y + 116, AC, 1.2))
    # checks
    tx = X + W + 150
    for i, (t, col) in enumerate((('Checks', INK), ('clear gap 46.7 mm:', INK), ('  ≥ 25 (20 mm + 5)', MUT), ('  ≤ 180 (Fe415)', MUT),
                                  ('steel 1257 mm²:', INK), ('  ≥ 338, ≤ 7200', MUT), ('side gaps ≤ 300', INK), ('main bar cover', INK), ('  30 + 10 = 40 mm', MUT))):
        o.append(T(tx, Y + 30 + i * 24, t, 14 if i == 0 else 13, 'start', col, bold=(i == 0)))
    return 470, ''.join(o)


FIG = {
    1: (f1, 'The piece of beam between the support and an inclined crack, held by the four shear forces, and the shear stresses of worked example 2. τ_v = 1.09 N/mm² lies between τ_c and τ_c,max, so stirrups must be designed.',
        'Elevation of a beam end with an inclined crack, showing the reaction V, compression zone force C and V_cz, aggregate interlock V_a, dowel force V_d, bar tension T and stirrup forces V_s; below, a scale of shear stress with tau_c 0.61, tau_v 1.09 and tau_c,max 3.1.'),
    2: (f2, 'Shear over half the 6 m span of worked example 2 against the capacity of concrete alone and of stirrups at 300 mm. The shear falls to 167.2 kN at 0.91 m, so the 200 mm zone runs to 1.0 m.',
        'Falling straight line of shear from 240 kN at the support face to zero at midspan, with dashed lines at 100.65 and 167.2 kN, the critical section at 0.55 m and the change at 0.91 m; below, a beam strip with stirrups at 200 mm to 1.0 m and at 300 mm beyond.'),
    3: (f3, 'The edge beam of the worked example: the closed stirrup and corner bars that carry the shear flow, and the side face with 45° spiral cracks crossed by stirrups at 140 mm.',
        'Cross-section 300 by 600 mm with a closed stirrup, four bottom and two top corner bars, shear flow arrows round it and dimensions b1 200 and d1 504 mm; beside it the side face with stirrups and inclined cracks, and the values Ve 280 kN, tau ve 1.70 and spacing 140 mm.'),
    4: (f4, 'How M_u, T_u and V_u of the edge beam become M_e1 and V_e, and the section that results: four 20 mm bars, two 12 mm top bars, a 12 mm bar on each side face and closed stirrups at 140 mm.',
        'Flow boxes from Mu 150, Tu 30 and Vu 120 to Mt 52.94, Ve 280, tau ve 1.70 and Me1 202.94 with Ast 1157 mm2, pointing to a cross-section with four bottom bars, two top bars, two side bars and a closed stirrup.'),
    5: (f5, 'The two 20 mm bars at the simple support of worked example 2. L_d = 806 mm fits within L_0 + 1.3 M_1/V = 964 mm, and the 270 mm inside the support exceeds L_d/3.',
        'Elevation of a beam end resting on a 300 mm wall, with two bottom bars ending 30 mm from the outer face and dimension lines for L0 120 mm, 1.3 M1/V 844 mm, Ld 806 mm and Ld/3 269 mm.'),
    6: (f6, 'The moment diagram of worked example 1 with the capacities of four and of two 16 mm bars. Two bars stop where M falls to 62.1 kN·m, at 1.02 m, and are carried d = 450 mm further, to 0.57 m.',
        'Parabolic bending moment diagram over a 6 m span peaking at 110 kN·m, with dashed lines at 117.7 and 62.1 kN·m, theoretical cut-off points at 1.02 and 4.98 m, and below it the full-length bars and the curtailed bars from 0.57 to 5.43 m.'),
    7: (f7, 'The detailed section of the edge beam: 30 mm cover to the 10 mm stirrup, a 46.7 mm clear gap between the 20 mm bars, d = 550 mm and side bars at mid-depth.',
        'Cross-section 300 by 600 mm with a closed stirrup, four bottom bars, two top bars and a side bar on each face, with the cover, the clear gap of 46.7 mm, effective depth 550 mm and side gaps of 254 and 250 mm marked, and a list of the checks.'),
}
AFTER = {1: 2, 2: 1, 3: 3, 4: 2, 5: 3, 6: 2, 7: 2}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    cap = re.sub(r'([A-Za-zτσφ])_([A-Za-z0-9]+(?:,max)?)', r'\1<sub>\2</sub>', cap)
    return {'caption': cap, 'after_section': AFTER[k], 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
