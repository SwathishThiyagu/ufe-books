"""Claude's hand-drawn figures for me-design-u4 (Machine Design: joints, power screws, springs and flywheels), one per
chapter, each drawn from that chapter's own worked example and numbers. Colours are the shell's CSS variables."""
import os, sys, math, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

_T, _Tb, _boxt = T, Tb, boxt


def _sub(s):
    """P_1, d_c ... drawn as real subscripts, never as underscores"""
    return re.sub(r'([A-Za-zα-ωΔ])_([A-Za-z0-9]+)', r'\1<tspan baseline-shift="sub" font-size="11">\2</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)
def boxt(x, y, w, h, lines, *a, **k): return _boxt(x, y, w, h, [_sub(l) for l in lines], *a, **k)


def dim(x1, y1, x2, y2, label, off=0, side='above', size=13, c=MUT):
    """a dimension line with arrowheads at both ends and its label"""
    o = [L(x1, y1, x2, y2, c, 1.4, arrow='m'), L(x2, y2, x1, y1, c, 1.4, arrow='m')]
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    if y1 == y2:
        o.append(Tb(mx, my - 7 if side == 'above' else my + 18, label, size, fill=c))
    else:
        o.append(Tb(mx + (8 if side == 'right' else -8), my + 5, label, size, 'start' if side == 'right' else 'end', c))
    return ''.join(o)


def vec(x, y, dx, dy, c=AC, arrow='n', w=2.6, dash=None):
    return L(x, y, x + dx, y + dy, c, w, dash=dash, arrow=arrow)


def circ(x, y, r, fill=PANEL, stroke=AC, sw=2, dash=None):
    d = f';stroke-dasharray:{dash}' if dash else ''
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{fill};stroke:{stroke};stroke-width:{sw}{d}"/>'


FIG = {}


# ---- 4.1 eccentric bolted bracket: four bolts, the load 250 mm off G, shear vectors at the two worst bolts ----
def f1():
    o = []
    gx, gy, s = 170, 215, 1.0            # G and scale (px per mm)
    k = 11.0                             # px per kN for force vectors
    o.append(P([(95, 80), (520, 80), (520, 160), (330, 395), (95, 395), (95, 80)], AC, 2, fill=PANEL))
    o.append(T(440, 106, 'bracket plate', 13, fill=MUT))
    for (bx, by) in [(50, 100), (50, -100), (-50, 100), (-50, -100)]:
        o.append(circ(gx + bx * s, gy - by * s, 9, ACS, AC, 2))
    o.append(L(gx - 8, gy, gx + 8, gy, INK, 1.5)); o.append(L(gx, gy - 8, gx, gy + 8, INK, 1.5))
    o.append(T(gx - 14, gy + 5, 'G', 15, 'end', bold=True))
    o.append(dim(gx - 50, 60, gx + 50, 60, '100 mm'))
    o.append(L(gx - 50, 64, gx - 50, 100, L2, 1.2, dash='4 3')); o.append(L(gx + 50, 64, gx + 50, 100, L2, 1.2, dash='4 3'))
    o.append(dim(72, gy - 100, 72, gy + 100, '200', side='left'))
    o.append(T(66, gy + 22, 'mm', 13, 'end', MUT))
    lx = gx + 250 * s
    o.append(L(lx, 170, lx, 250, NX, 3.5, arrow='x'))
    o.append(T(lx - 10, 182, 'P = 12 kN', 15, 'end', NX, bold=True))
    o.append(L(gx + 12, gy, lx, gy, L2, 1.2, dash='5 4'))
    o.append(T((gx + lx) / 2 + 20, gy - 8, 'e = 250 mm', 14, fill=MUT, bold=True))
    for (bx, by) in [(50, 100), (50, -100)]:
        X, Y = gx + bx * s, gy - by * s
        sx = 6.0 * (1 if by > 0 else -1)
        o.append(vec(X, Y, 0, 3.0 * k, LV, 'l'))
        o.append(vec(X, Y, sx * k, 3.0 * k, AC, 'n'))
        o.append(vec(X, Y, sx * k, 6.0 * k, NX, 'x', 3))
    X, Y = gx + 50, gy - 100
    o.append(T(X - 6, Y + 40, 'P_1', 14, 'end', LV, bold=True))
    o.append(T(X + 72, Y + 30, 'P_2', 14, 'start', AC, bold=True))
    o.append(T(X + 72, Y + 72, 'R', 15, 'start', NX, bold=True))
    X, Y = gx + 50, gy + 100
    o.append(T(X - 72, Y + 72, 'R', 15, 'end', NX, bold=True))
    o.append(boxt(545, 190, 160, 150, ['P_1 = P/n = 3.0 kN', 'r = 111.8 mm', 'P_2 = Mr/Σr²', '= 6.71 kN', 'R = 8.49 kN'], PANEL, L2, 14))
    o.append(T(625, 365, 'worst: right bolts', 13, fill=NX, bold=True))
    return 412, ''.join(o)


FIG[1] = (f1, 'The worked example’s bracket. The 12 kN load acts 250 mm to the right of the bolt centroid G. At the two right-hand bolts the '
              'primary shear P₁ (3.0 kN, down) and the secondary shear P₂ (6.71 kN, square to the radius) add to R = 8.49 kN; on the left they partly cancel.',
          'A bracket plate with four bolts at the corners of a 100 by 200 millimetre rectangle around the centroid G. A 12 kilonewton load '
          'acts 250 millimetres to the right of G. At the two right bolts, arrows show the primary shear, the secondary shear and their resultant of 8.49 kilonewtons.')


# ---- 4.2 two parallel fillet welds, load 150 mm off G, stresses at the weld ends ----
def f2():
    o = []
    s = 1.8; gx, gy = 230, 210
    xl, xr = gx - 50 * s, gx + 50 * s
    o.append(R(xl - 12, gy - 60 * s, 400, 120 * s, 'none', L2, 4, sw=1.4, dash='5 4'))
    o.append(T(xl + 360, gy - 60 * s + 20, 'bracket plate', 13, 'end', MUT))
    for x in (xl, xr):
        o.append(R(x - 7, gy - 50 * s, 14, 100 * s, NXS, NX, 3))
    o.append(L(gx - 7, gy, gx + 7, gy, INK, 1.5)); o.append(L(gx, gy - 7, gx, gy + 7, INK, 1.5))
    o.append(T(gx - 12, gy + 22, 'G', 15, bold=True))
    o.append(dim(xl, gy - 50 * s - 22, xr, gy - 50 * s - 22, '100 mm'))
    o.append(dim(xl - 60, gy - 50 * s, xl - 60, gy + 50 * s, 'L = 100', side='left'))
    lx = gx + 150 * s
    o.append(L(lx, 110, lx, 200, NX, 3.5, arrow='x'))
    o.append(T(lx + 10, 140, 'P = 10 kN', 15, 'start', NX, bold=True))
    o.append(L(gx + 10, gy, lx, gy, L2, 1.2, dash='5 4'))
    o.append(T(gx + 225, gy + 22, 'e = 150 mm', 14, fill=MUT, bold=True))
    k = 2.0
    for sy in (1, -1):
        X, Y = xr, gy - 50 * s * sy
        o.append(vec(X, Y, 0, 11.8 * k, LV, 'l'))
        o.append(vec(X, Y, 26.5 * k * sy, 26.5 * k, AC, 'n'))
        o.append(vec(X, Y, 26.5 * k * sy, 38.3 * k, NX, 'x', 3))
    Y = gy - 50 * s
    o.append(T(xr - 6, Y + 26, 'τ_1', 14, 'end', LV, bold=True))
    o.append(T(xr + 46, Y + 22, 'τ_2', 14, 'start', AC, bold=True))
    o.append(Tb(xr + 60, Y + 80, '46.6 MPa', 14, 'start', NX, bold=True))
    o.append(T(xl + 14, gy - 50 * s + 14, '30.3 MPa', 13, 'start', MUT))
    o.append(T(xl + 14, gy + 50 * s - 4, '30.3 MPa', 13, 'start', MUT))
    o.append(boxt(495, 240, 215, 160, ['h = 6 mm, throat 4.24 mm', 'A = 848.4 mm²', 'J = 2.83 × 10⁶ mm⁴', 'τ_1 = P/A = 11.8 MPa', 'τ_2 = Tr/J = 37.5 MPa', 'τ = 46.6 MPa'], PANEL, L2, 14))
    return 418, ''.join(o)


FIG[2] = (f2, 'The worked example’s two 100 mm fillet welds, 100 mm apart, with the 10 kN load 150 mm from G. At the ends of the right weld the '
              'primary shear τ₁ (11.8 MPa) and the torsional shear τ₂ (37.5 MPa) add to 46.6 MPa; the left weld’s ends reach only 30.3 MPa.',
          'Two vertical fillet welds 100 millimetres long and 100 millimetres apart, with the centroid G midway. A 10 kilonewton load acts 150 millimetres '
          'to the right. Arrows at the ends of the right weld show the primary and torsional shear adding to 46.6 megapascals; the left weld ends show 30.3.')


# ---- 4.3 knuckle joint in section through the pin, sized in the worked example ----
def f3():
    o = []
    s = 1.8; cx, cy = 380, 200
    b, a, d1, d2, d = 37.5 * s, 22.5 * s, 38 * s, 66 * s, 30 * s
    # rod with eye (left)
    o.append(R(60, cy - d / 2, cx - d2 / 2 - 60 + 4, d, PANEL, AC, 2, sw=2))
    o.append(R(cx - d2 / 2, cy - b / 2, d2, b, PANEL, AC, 4))
    # fork (right): two tines and the body
    ft = cy - b / 2 - a; fb = cy + b / 2
    o.append(R(cx - d2 / 2, ft, d2 + 70, a, ACS, AC, 4))
    o.append(R(cx - d2 / 2, fb, d2 + 70, a, ACS, AC, 4))
    o.append(R(cx + d2 / 2 + 40, ft, 50, 2 * a + b, ACS, AC, 4))
    o.append(R(cx + d2 / 2 + 88, cy - d / 2, 590 - (cx + d2 / 2 + 88) + 30, d, ACS, AC, 2))
    # pin
    o.append(R(cx - d1 / 2, ft - 22, d1, 2 * a + b + 44, NXS, NX, 4))
    o.append(R(cx - d1 / 2 - 10, ft - 30, d1 + 20, 12, NXS, NX, 3))
    # shear planes
    for y in (cy - b / 2, cy + b / 2):
        o.append(L(cx - d1 / 2 - 18, y, cx + d1 / 2 + 18, y, NX, 2.2, dash='6 4'))
    o.append(Tb(cx + d1 / 2 + 60, cy - b / 2 + 5, 'shear plane', 13, 'start', NX, bold=True))
    o.append(Tb(cx + d1 / 2 + 60, cy + b / 2 + 5, 'shear plane', 13, 'start', NX, bold=True))
    # loads
    o.append(L(56, cy, 14, cy, NX, 3.5, arrow='x')); o.append(L(624, cy, 668, cy, NX, 3.5, arrow='x'))
    o.append(T(20, cy - 36, 'P = 50 kN', 14, 'start', NX, bold=True)); o.append(T(700, cy - 22, 'P = 50 kN', 14, 'end', NX, bold=True))
    # labels
    o.append(T(170, cy + 5, 'rod d = 30 mm', 13))
    o.append(T(cx + d2 / 2 + 65, ft - 10, 'fork', 14, bold=True))
    o.append(T(cx - d2 / 2 - 26, cy - b / 2 - 10, 'eye', 14, bold=True))
    o.append(T(cx, ft - 38, 'pin d_1 = 38 mm', 14, bold=True, fill=NX))
    o.append(dim(cx - d2 / 2, cy + b / 2 + a + 34, cx + d2 / 2, cy + b / 2 + a + 34, 'eye outer d_2 = 66 mm', side='below'))
    o.append(boxt(40, 262, 230, 58, ['eye thickness b = 37.5 mm', 'each tine a = 22.5 mm'], PANEL, L2, 13))
    o.append(T(140, 120, 'pin bending: M = (P/2)(b/4 + a/3)', 13, fill=MUT))
    o.append(T(140, 138, '= 421.9 N·m', 13, fill=MUT))
    return 372, ''.join(o)


FIG[3] = (f3, 'The knuckle joint of the worked example, cut through the pin. The eye (37.5 mm thick) sits between two 22.5 mm fork tines; the 38 mm pin '
              'is sheared on the two dashed planes and bent between the eye and the tines, and bending, not shear, set its size.',
          'A section through a knuckle joint. A 30 millimetre rod ends in an eye 37.5 millimetres thick between two fork tines 22.5 millimetres thick. '
          'A 38 millimetre pin passes through all three; dashed lines mark its two shear planes. Loads of 50 kilonewtons pull the rods apart.')


# ---- 4.4 double-riveted zig-zag lap joint, plan view ----
def f4():
    o = []
    s = 1.5
    top, bot = 64, 330
    o.append(R(50, top, 400, bot - top, PANEL, AC, 2))          # plate A, left
    o.append(R(300, top, 360, bot - top, ACS, AC, 2, dash=None))  # plate B, right, on top
    o.append(T(120, top + 22, 'plate A, t = 10 mm', 13, 'start', MUT))
    o.append(T(560, top + 22, 'plate B', 13, 'middle', MUT))
    x1, x2 = 300 + 30 * s, 450 - 30 * s
    p = 67 * s
    ys1 = [95, 95 + p, 95 + 2 * p]
    ys2 = [95 + p / 2, 95 + 1.5 * p]
    for y in ys1: o.append(circ(x1, y, 10 * s, PANEL, NX, 2.2))
    for y in ys2: o.append(circ(x2, y, 10 * s, PANEL, NX, 2.2))
    o.append(L(x1, top + 4, x1, bot - 4, NX, 2, dash='7 5'))
    o.append(T(x1 - 8, bot + 22, 'tearing line', 13, 'end', NX, bold=True))
    o.append(dim(x1 - 46, ys1[0], x1 - 46, ys1[1], 'p = 67', side='left'))
    o.append(dim(300, 34, x1, 34, 'm = 30 mm'))
    o.append(L(300, 38, 300, top, L2, 1.2, dash='4 3')); o.append(L(x1, 38, x1, top, L2, 1.2, dash='4 3'))
    o.append(L(450, top + 2, 450, bot - 2, AC, 1.6, dash='6 5'))
    o.append(T(456, bot - 10, 'edge of A', 13, 'start', MUT))
    o.append(T(x2, ys2[0] - 22, 'd = 20 mm', 13, 'middle', NX))
    o.append(L(46, 195, 10, 195, NX, 3.5, arrow='x')); o.append(L(664, 195, 700, 195, NX, 3.5, arrow='x'))
    o.append(T(14, 180, 'P', 15, 'start', NX, bold=True)); o.append(T(704, 180, 'P', 15, 'end', NX, bold=True))
    o.append(boxt(70, 120, 165, 150, ['per pitch of 67 mm:', 'shear 37.7 kN', 'crushing 48.0 kN', 'tearing 37.6 kN', 'η = 70.1 %'], PANEL, L2, 14, bold_first=True))
    return 372, ''.join(o)


FIG[4] = (f4, 'Plan of the worked example’s double-riveted zig-zag lap joint: 20 mm rivet holes at 67 mm pitch in two staggered rows, 30 mm from the '
              'plate edge. Plate A tears along the dashed line through the first row; per pitch it holds 37.6 kN, just under rivet shear.',
          'Two overlapping plates pulled apart by loads P. Two staggered rows of rivet holes cross the overlap, with pitch 67 millimetres and margin 30 '
          'millimetres. A dashed line through the first row marks the tearing line. A box gives the strengths per pitch and an efficiency of 70.1 percent.')


# ---- 4.5 one turn of thread unwrapped: the inclined plane and its forces ----
def f5():
    o = []
    x0, y0, base, ht = 60, 330, 420, 110          # drawn slope steeper than the real 4.55 degrees
    o.append(P([(x0, y0), (x0 + base, y0), (x0 + base, y0 - ht), (x0, y0)], AC, 2.2, fill=PANEL))
    o.append(T(x0 + base / 2, y0 + 24, 'π d_m = π × 24 = 75.4 mm', 14, bold=True))
    o.append(T(x0 + base + 10, y0 - ht / 2, 'lead l = 6 mm', 14, 'start', bold=True))
    o.append(T(x0 + 70, y0 - 8, 'α = 4.55°', 14, 'start', AC, bold=True))
    o.append(T(x0 + base / 2, y0 + 44, '(height drawn about four times too steep)', 13, fill=MUT))
    ang = math.atan2(ht, base)
    ux, uy = math.cos(ang), -math.sin(ang)          # up the slope (screen)
    nx, ny = -math.sin(ang), -math.cos(ang)         # outward normal, up and to the left
    bx, by = x0 + 0.5 * base, y0 - 0.5 * ht
    w, h = 64, 36
    a0 = (bx - ux * w / 2, by - uy * w / 2); a1 = (bx + ux * w / 2, by + uy * w / 2)
    o.append(P([a0, a1, (a1[0] + nx * h, a1[1] + ny * h), (a0[0] + nx * h, a0[1] + ny * h), a0], NX, 2, fill=NXS))
    mx, my = bx + nx * h / 2, by + ny * h / 2
    o.append(L(mx, my, mx, my + 62, NX, 3, arrow='x')); o.append(T(mx + 8, my + 56, 'W = 20 kN', 14, 'start', NX, bold=True))
    o.append(L(mx - 130, my, mx - 40, my, LV, 3, arrow='l')); o.append(T(mx - 132, my - 10, 'P = 4.65 kN', 14, 'start', LV, bold=True))
    phi = math.radians(8.53) * 2.5                  # drawn larger, like the slope
    rx, ry = nx * math.cos(phi) - ux * math.sin(phi), ny * math.cos(phi) - uy * math.sin(phi)
    o.append(L(bx, by, bx + 100 * nx, by + 100 * ny, L2, 1.4, dash='4 3'))
    o.append(L(bx, by, bx + 110 * rx, by + 110 * ry, AC, 2.6, arrow='n'))
    o.append(T(bx + 110 * rx - 6, by + 110 * ry - 6, 'R', 15, 'end', AC, bold=True))
    o.append(T(bx + 104 * nx + 4, by + 104 * ny - 4, 'normal', 13, 'start', MUT))
    o.append(T(bx + 70 * (nx + rx) / 2 - 2, by + 70 * (ny + ry) / 2 - 14, 'φ', 15, 'middle', AC, bold=True))
    o.append(boxt(510, 60, 195, 196, ['tan α = 0.0796', 'φ = tan⁻¹ 0.15 = 8.53°', 'P = W tan(α + φ)', 'T_r = P·d_m/2', '= 55.8 N·m', 'η = 34.2 %'], PANEL, L2, 14))
    return 392, ''.join(o)


FIG[5] = (f5, 'One turn of the worked example’s thread unwrapped into a slope of base πd<sub>m</sub> = 75.4 mm and height 6 mm. Pushing the 20 kN load up it '
              'needs a horizontal effort P = W tan(α + φ) = 4.65 kN at the mean radius, a torque of 55.8 N·m.',
          'A right triangle with base pi times the mean diameter, 75.4 millimetres, and height equal to the lead, 6 millimetres, with lead angle 4.55 degrees. '
          'A block on the slope carries a 20 kilonewton load; a horizontal effort of 4.65 kilonewtons pushes it; the reaction R leans back by the friction angle.')


def coil_section(cx, ybot, height, D, d, n_t, s, fill=PANEL, stroke=AC):
    """sectional view of a compression spring: wire circles on both sides, n_t coils over the given height"""
    o = []
    r = d * s / 2
    xl, xr = cx - D * s / 2, cx + D * s / 2
    if n_t > 1:
        step = (height - 2 * r) / (n_t - 1)
    else:
        step = 0
    for i in range(n_t):
        y = ybot - r - i * step
        o.append(circ(xl, y, r, fill, stroke, 1.8))
        y2 = y - step / 2 if 0 < i < n_t else y
        if i < n_t - 1 or n_t == 1:
            o.append(circ(xr, y - step / 2 if i < n_t - 1 else y, r, fill, stroke, 1.8))
    return ''.join(o)


# ---- 4.6 the designed spring at free length, at 1000 N and solid ----
def f6():
    o = []
    s = 2.4; base = 330; D, d = 42, 7
    plate = lambda cx, y: R(cx - 75, y - 8, 150, 8, ACS, AC, 2, sw=1.6)
    states = [(110, 98.0, 'free', 'L_f = 98 mm', 'no load'), (330, 98.0 - 24.3, 'working', '73.7 mm', 'W = 1000 N'), (550, 70.0, 'solid', 'L_s = 70 mm', 'coils touch')]
    o.append(L(30, base, 700, base, L2, 1.6))
    for cx, Lh, name, lab, load in states:
        h = Lh * s
        if name == 'solid':
            r = d * s / 2
            for i in range(10):
                y = base - r - i * 2 * r
                o.append(circ(cx - D * s / 2, y, r, PANEL, AC, 1.8)); o.append(circ(cx + D * s / 2, y, r, PANEL, AC, 1.8))
        else:
            o.append(coil_section(cx, base, h, D, d, 10, s))
        o.append(plate(cx, base - h))
        o.append(T(cx, base + 22, name, 14, bold=True))
        o.append(T(cx, base + 40, load, 13, fill=MUT))
        o.append(dim(cx + D * s / 2 + 26, base - h, cx + D * s / 2 + 26, base, lab, side='right'))
        if name == 'working':
            o.append(L(cx, base - h - 48, cx, base - h - 10, NX, 3.2, arrow='x'))
    o.append(T(110, base - 98 * s - 18, 'D = 42 mm, d = 7 mm', 13, fill=MUT))
    o.append(T(330, base - 73.7 * s - 56, 'δ = 24.3 mm', 14, fill=NX, bold=True))
    o.append(T(550, base - 70 * s - 22, 'gap left: 3.9 mm', 13, fill=MUT))
    return 384, ''.join(o)


FIG[6] = (f6, 'The spring designed in the second worked example, in section: 7 mm wire on a 42 mm mean diameter with 10 coils (8 active). It is 98 mm long when '
              'free, 73.7 mm under 1000 N and 70 mm solid, so 3.9 mm of travel is kept in reserve.',
          'Three sectional views of the same compression spring standing on a base line. Free: 98 millimetres long. Working, under 1000 newtons: 73.7 millimetres, '
          'a deflection of 24.3. Solid, coils touching: 70 millimetres. Wire circles show 7 millimetre wire on a 42 millimetre mean diameter.')


# ---- 4.7 two nested springs: diameters, clearance and the load split ----
def f7():
    o = []
    s = 2.0; cx = 210; base = 330
    D1, d1, D2, d2 = 90, 15, 60, 10
    o.append(L(40, base, 380, base, L2, 1.6))
    # five outer coils, seven inner coils shown over the same height
    H = 250
    for i in range(5):
        y = base - d1 * s / 2 - i * (H - d1 * s) / 4.5
        o.append(circ(cx - D1 * s / 2, y, d1 * s / 2, ACS, AC, 2)); o.append(circ(cx + D1 * s / 2, y - (H - d1 * s) / 9, d1 * s / 2, ACS, AC, 2))
    for i in range(7):
        y = base - d2 * s / 2 - i * (H - d2 * s) / 6.5
        o.append(circ(cx - D2 * s / 2, y - (H - d2 * s) / 13, d2 * s / 2, NXS, NX, 2)); o.append(circ(cx + D2 * s / 2, y, d2 * s / 2, NXS, NX, 2))
    o.append(R(cx - 115, base - H - 10, 230, 10, PANEL, AC, 2, sw=1.6))
    o.append(L(cx, base - H - 52, cx, base - H - 14, INK, 3.2, arrow='m'))
    o.append(T(cx + 10, base - H - 30, 'W = 10 kN', 14, 'start', bold=True))
    o.append(L(cx, base - H + 4, cx, base, L2, 1, dash='6 4'))
    # clearance mark between the two right-hand columns
    xo, xi = cx + D1 * s / 2 - d1 * s / 2, cx + D2 * s / 2 + d2 * s / 2
    o.append(Tb(cx + 100, base + 24, 'clearance 2.5 mm', 13, fill=MUT))
    o.append(L(xi, base + 8, xi, base - 6, MUT, 1.4)); o.append(L(xo, base + 8, xo, base - 6, MUT, 1.4))
    o.append(T(cx - D1 * s / 2, base + 24, 'outer', 13, fill=AC, bold=True))
    o.append(T(cx - D2 * s / 2 + 6, base + 42, 'inner', 13, fill=NX, bold=True))
    # data and load split
    o.append(boxt(400, 60, 300, 72, ['outer: d₁ = 15, D₁ = 90 mm, 8 coils', 'k₁ = 88.3 N/mm, right-hand'], ACS, AC, 14))
    o.append(boxt(400, 142, 300, 72, ['inner: d₂ = 10, D₂ = 60 mm, 12 coils', 'k₂ = 39.2 N/mm, left-hand'], NXS, NX, 14))
    x0, w = 400, 300
    o.append(R(x0, 250, w * 0.6923, 36, ACS, AC, 4)); o.append(R(x0 + w * 0.6923, 250, w * 0.3077, 36, NXS, NX, 4))
    o.append(T(x0 + w * 0.6923 / 2, 274, 'P₁ = 6.92 kN', 14, bold=True)); o.append(T(x0 + w * 0.6923 + w * 0.3077 / 2, 274, '3.08 kN', 14, bold=True))
    o.append(T(x0 + w / 2, 310, 'same deflection 78.4 mm; τ = 589 MPa in both', 13, fill=MUT))
    return 384, ''.join(o)


FIG[7] = (f7, 'The concentric pair of the first worked example in section. Both springs have index 6 and are squeezed the same 78.4 mm, so the 10 kN load '
              'splits in the ratio of their rates, 6.92 kN to 3.08 kN, and both wires reach the same 589 MPa. The 2.5 mm gap keeps the coils from rubbing.',
          'A sectional view of two nested compression springs under one plate carrying 10 kilonewtons: an outer spring of 15 millimetre wire on a 90 millimetre '
          'diameter and an inner spring of 10 millimetre wire on a 60 millimetre diameter, 2.5 millimetres apart. A bar splits the load 6.92 to 3.08 kilonewtons.')


# ---- 4.8 semi-elliptic leaf spring of the worked example ----
def f8():
    o = []
    cx, s = 360, 0.62
    yl = 150; t = 9
    half = 500 * s
    # master and second full-length leaf
    o.append(R(cx - half, yl, 2 * half, t, ACS, AC, 2, sw=1.6))
    o.append(circ(cx - half - 9, yl + 1, 12, PANEL, AC, 2.4)); o.append(circ(cx + half + 9, yl + 1, 12, PANEL, AC, 2.4))
    o.append(R(cx - half + 20, yl + t, 2 * half - 40, t, ACS, AC, 2, sw=1.6))
    # six graduated leaves, shorter step by step
    band = 50 * s
    for i in range(6):
        hl = band + (450 * s) * (6 - i) / 7
        o.append(R(cx - hl, yl + (2 + i) * t, 2 * hl, t, PANEL, AC, 2, sw=1.4))
    ybot = yl + 8 * t
    # centre band
    o.append(R(cx - band, yl - 8, 2 * band, ybot - yl + 16, 'none', NX, 3, sw=2.2))
    # loads
    for x in (cx - half - 9, cx + half + 9):
        o.append(L(x, yl - 70, x, yl - 16, NX, 3.2, arrow='x'))
        o.append(T(x, yl - 78, 'W = 4.5 kN', 14, bold=True, fill=NX))
    o.append(L(cx, ybot + 70, cx, ybot + 14, LV, 3.4, arrow='l'))
    o.append(T(cx - 12, ybot + 62, 'axle: 2W = 9 kN', 14, 'end', LV, bold=True))
    # dimensions
    o.append(dim(cx - half - 9, 52, cx + half + 9, 52, 'eye to eye 2L₁ = 1000 mm'))
    o.append(dim(cx + band, ybot + 40, cx + half + 9, ybot + 40, 'L = 450 mm', side='below'))
    o.append(T(cx, yl - 16, 'band 100 mm', 13, fill=NX, bold=True))
    o.append(T(cx - half - 30, yl + 28, 'master leaf', 13, 'start', MUT))
    o.append(T(40, ybot + 28, '2 full-length + 6 graduated', 13, 'start', MUT))
    o.append(T(40, ybot + 46, 'leaves, each 75 × 10 mm', 13, 'start', MUT))
    o.append(boxt(30, 318, 660, 40, ['no nip: 270 MPa (full-length), 180 MPa (graduated)  →  with 6.6 mm nip: 202.5 MPa in all; δ = 17.6 mm'], PANEL, L2, 14))
    return 372, ''.join(o)


FIG[8] = (f8, 'The worked example’s spring: 1000 mm between eyes, a 100 mm centre band, so each cantilever is L = 450 mm with 4.5 kN at the eye. '
              'Two full-length and six graduated leaves 75 × 10 mm; nipping evens the leaf stresses from 270 and 180 MPa to 202.5 MPa.',
          'Side view of a semi-elliptic leaf spring: a master leaf with an eye at each end, a second full-length leaf and six graduated leaves getting shorter '
          'downwards, clamped by a 100 millimetre centre band. Loads of 4.5 kilonewtons act at the eyes and 9 kilonewtons at the centre.')


# ---- 4.9 shear sandwich mount and the transmissibility curve ----
def f9():
    o = []
    # mount: two vertical steel plates, rubber between, inner plate pushed down by the weight
    x0, y0, s = 60, 90, 2.4
    h, w = 20 * s, 60 * s
    o.append(R(x0, y0, 16, w + 40, PANEL, AC, 2))
    o.append(R(x0 + 16 + h, y0 + 8, 16, w + 40, PANEL, AC, 2))
    dd = 3.41 * s * 2
    o.append(P([(x0 + 16, y0 + 20), (x0 + 16 + h, y0 + 20 + dd), (x0 + 16 + h, y0 + 20 + w + dd), (x0 + 16, y0 + 20 + w), (x0 + 16, y0 + 20)], LV, 2, fill=LVS))
    o.append(L(x0 + 16 + h + 8, y0 - 30, x0 + 16 + h + 8, y0 + 4, NX, 3.2, arrow='x'))
    o.append(T(x0 + 16 + h + 20, y0 - 14, '490 N per mount', 13, 'start', NX, bold=True))
    o.append(T(x0 + 8, y0 + w + 72, 'fixed', 13, fill=MUT))
    o.append(T(x0 + 16 + h + 8, y0 + w + 72, 'machine', 13, fill=MUT))
    o.append(T(x0 + 40, y0 + w + 96, 'rubber 60 × 60, h = 20 mm', 13, fill=LV, bold=True))
    o.append(T(x0 + 40, y0 + w + 114, 'k = GA/h = 144 N/mm', 13, fill=MUT))
    # transmissibility plot
    px0, px1, py0, py1 = 300, 690, 60, 320
    fx = lambda r: px0 + (px1 - px0) * r / 4
    fy = lambda T_: py1 - (py1 - py0) * T_ / 3
    o.append(axes(px0, px1, py0, py1, [0, 1, 2, 3, 4], [0, 1, 2, 3], fx, fy, 'frequency ratio r = f/fₙ', 'transmissibility T'))
    pts = []
    for i in range(0, 401):
        r = i / 100
        if abs(r - 1) < 0.18: 
            if pts: o.append(P(pts, AC, 2.6)); pts = []
            continue
        T_ = 1 / abs(r * r - 1)
        if T_ <= 3: pts.append((fx(r), fy(T_)))
        else:
            if pts: o.append(P(pts, AC, 2.6)); pts = []
    if pts: o.append(P(pts, AC, 2.6))
    o.append(L(fx(1.414), py0, fx(1.414), py1, L2, 1.4, dash='5 4'))
    o.append(T(fx(1.414) + 4, py0 + 14, 'r = √2', 13, 'start', MUT))
    o.append(C(fx(2.81), fy(0.145), 6, NX)); o.append(T(fx(2.81) + 20, fy(0.145) - 40, '1440 rpm', 13, fill=NX, bold=True)); o.append(T(fx(2.81) + 20, fy(0.145) - 22, 'r = 2.81, T = 0.145', 13, fill=NX, bold=True))
    o.append(C(fx(1.17), fy(2.70), 6, LV)); o.append(T(fx(1.17) + 12, fy(2.70) + 5, '600 rpm: T ≈ 2.7', 13, 'start', LV, bold=True))
    return 376, ''.join(o)


FIG[9] = (f9, 'Left: one of the worked example’s shear mounts; the machine side slides 3.41 mm down (drawn larger) under its quarter of the weight. '
              'Right: transmissibility without damping. At 1440 rpm (r = 2.81) only 14.5 % of the force passes to the floor; at 600 rpm the mounts would amplify it.',
          'A rubber block bonded between a fixed steel plate and a plate on the machine, sheared downwards by the weight. Beside it, a graph of transmissibility '
          'against frequency ratio: high near ratio 1, crossing 1 at root 2, and falling to 0.145 at the operating ratio 2.81.')


# ---- 4.10 rimmed flywheel of the second worked example ----
def f10():
    o = []
    cx, cy, s = 200, 215, 0.25
    R_, t_, rh = 600 * s, 120 * s, 100 * s
    o.append(circ(cx, cy, R_ + t_ / 2, ACS, AC, 2)); o.append(circ(cx, cy, R_ - t_ / 2, 'var(--fig)', AC, 2))
    for i in range(6):
        a = math.radians(90 + 60 * i)
        x1, y1 = cx + rh * math.cos(a), cy - rh * math.sin(a)
        x2, y2 = cx + (R_ - t_ / 2) * math.cos(a), cy - (R_ - t_ / 2) * math.sin(a)
        o.append(L(x1, y1, x2, y2, AC, 12))
    o.append(circ(cx, cy, rh, ACS, AC, 2)); o.append(circ(cx, cy, 10, PANEL, AC, 2))
    o.append(L(cx + rh, cy, cx + R_, cy, NX, 2, dash='5 4'))
    o.append(Tb(cx + 90, cy - 8, 'R = 600 mm', 13, fill=NX, bold=True))
    o.append(T(cx, cy + R_ + t_ / 2 + 24, 'rim 162 × 120 mm, 528 kg', 13, fill=MUT))
    o.append(L(cx - 40, 24, cx + 40, 24, LV, 3, arrow='l'))
    o.append(T(cx + 50, 29, 'v = 37.7 m/s at the rim', 13, 'start', LV, bold=True))
    o.append(T(cx - 70, cy + 5, '6 arms', 13, fill=MUT))
    o.append(boxt(430, 50, 270, 170, ['I = 190 kg·m², 600 rpm', 'hoop σ_t = ρv² = 10.2 MPa', 'rim bending σ_b = 28.1 MPa', '0.75σ_t + 0.25σ_b', '= 14.7 MPa'], PANEL, L2, 14))
    # elliptical arm section
    ex, ey = 565, 318
    o.append(f'<ellipse cx="{ex}" cy="{ey}" rx="56" ry="28" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2"/>')
    o.append(dim(ex - 56, ey + 46, ex + 56, ey + 46, 'a = 56 mm', side='below'))
    o.append(T(ex - 70, ey + 5, 'b = 28', 13, 'end', MUT))
    o.append(T(ex, ey - 40, 'arm at the hub: M = 110.5 N·m', 13, fill=MUT))
    return 418, ''.join(o)


FIG[10] = (f10, 'The engine flywheel of the second worked example: a 528 kg cast-iron rim of 600 mm mean radius on six elliptical arms, turning at 37.7 m/s at '
                'the rim. Bending of the rim between the arms (28.1 MPa) is larger than the hoop stress (10.2 MPa).',
           'Front view of a rimmed flywheel with a hub, six arms and a rim of 600 millimetre mean radius. A box lists inertia 190 kilogram metre squared, hoop stress '
           '10.2, rim bending 28.1 and combined 14.7 megapascals. An ellipse shows the arm section, 56 by 28 millimetres.')


spec = make_spec(FIG)
