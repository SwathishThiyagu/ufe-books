"""Claude's hand-drawn figures for ae-struct-u4 (bending of thin-walled beams), one per chapter. Every number comes from
that chapter's worked example and is computed here. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
rad = math.radians


def arrow(x1, y1, x2, y2, c=AC, w=2.5, kind='n', dash=None):
    return L(x1, y1, x2, y2, c, w, dash, arrow=kind)


def poly(pts, fill, stroke, sw=2, dash=None):
    d = f';stroke-dasharray:{dash}' if dash else ''
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" style="fill:{fill};stroke:{stroke};stroke-width:{sw}{d}"/>'


# ---- 4.1 T-section stress diagram and the anticlastic curl ----
def f1():
    bf, tf, tw, hw = 100, 10, 10, 90
    A1, A2 = bf * tf, tw * hw
    yt = (A1 * tf / 2 + A2 * (tf + hw / 2)) / (A1 + A2); yb = 100 - yt
    I = bf * tf ** 3 / 12 + A1 * (yt - 5) ** 2 + tw * hw ** 3 / 12 + A2 * (55 - yt) ** 2
    st, sb = -3e6 * yt / I, 3e6 * yb / I
    o = [T(180, 28, 'T-section under M', 15, bold=True),
         T(180, 46, 'M<tspan font-size="11" dy="4">x</tspan><tspan dy="-4"> = −3 kN·m (bottom in tension)</tspan>', 13, fill=MUT)]
    s = 2.3  # px per mm
    X0, Y0 = 40, 76
    # flange and web
    o.append(R(X0, Y0, bf * s, tf * s, ACS, AC, 2))
    o.append(R(X0 + (bf - tw) / 2 * s, Y0 + tf * s, tw * s, hw * s, ACS, AC, 2))
    yna = Y0 + yt * s
    o.append(L(X0 - 20, yna, X0 + bf * s + 14, yna, INK, 1.8, '7 5'))
    o.append(Tb(X0 + bf * s / 2 + 40, yna - 6, 'neutral axis', 13, 'start', INK))
    o.append(T(X0 - 24, yna + 5, 'G', 14, 'end', INK, True))
    o.append(C(X0 + bf * s / 2, yna, 5, INK))
    # dimensions
    o.append(L(X0 + bf * s + 24, Y0, X0 + bf * s + 24, yna, L2, 1.5)); o.append(T(X0 + bf * s + 30, (Y0 + yna) / 2 + 5, f'{yt:.2f}', 13, 'start', MUT))
    o.append(L(X0 + bf * s + 24, yna, X0 + bf * s + 24, Y0 + 100 * s, L2, 1.5)); o.append(T(X0 + bf * s + 30, (yna + Y0 + 100 * s) / 2 + 5, f'{yb:.2f} mm', 13, 'start', MUT))
    o.append(T(X0 + bf * s / 2, Y0 + 100 * s + 22, '100 × 10 flange, 90 × 10 web', 13, fill=MUT))
    # stress diagram
    Sx = 440; k = 0.7  # px per MPa
    yt_px, yb_px = Y0, Y0 + 100 * s
    o.append(L(Sx, yt_px - 6, Sx, yb_px + 6, L2, 1.5))
    o.append(poly([(Sx, yna), (Sx + st * k, yt_px), (Sx, yt_px)], LVS, LV))
    o.append(poly([(Sx, yna), (Sx + sb * k, yb_px), (Sx, yb_px)], NXS, NX))
    o.append(L(X0 + bf * s + 14, yna, Sx, yna, INK, 1.2, '3 4'))
    o.append(T(Sx + 6, yt_px + 16, f'{st:.1f} MPa', 14, 'start', LV, True))
    o.append(T(Sx + sb * k + 8, yb_px - 4, f'+{sb:.1f} MPa', 14, 'start', NX, True))
    o.append(T(Sx + sb * k + 8, yb_px + 13, 'tension: yields first', 13, 'start', NX))
    o.append(T(Sx + 40, 28, 'Direct stress σ = M<tspan font-size="11" dy="4">x</tspan><tspan dy="-4"> y/I</tspan>', 15, bold=True))
    # anticlastic panel
    ax, ay = 590, 150
    o.append(T(ax + 30, ay - 84, 'Anticlastic curl', 15, bold=True))
    o.append(R(ax, ay - 30, 80, 60, 'none', L2, 0, 1.5, '5 4'))
    curl = f'M{ax - 8:.1f},{ay - 32:.1f} Q{ax + 40:.1f},{ay - 46:.1f} {ax + 88:.1f},{ay - 32:.1f} L{ax + 72:.1f},{ay + 30:.1f} Q{ax + 40:.1f},{ay + 18:.1f} {ax + 8:.1f},{ay + 30:.1f} Z'
    o.append(f'<path d="{curl}" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2;fill-opacity:0.6"/>')
    o.append(T(ax + 40, ay - 52, 'compression side widens', 13, fill=LV))
    o.append(T(ax + 40, ay + 50, 'tension side narrows', 13, fill=NX))
    o.append(T(ax + 40, ay + 80, 'R′ = R/ν', 14, bold=True))
    o.append(T(ax + 40, ay + 99, 'ν: Poisson\'s ratio', 13, fill=MUT))
    o.append(T(ax + 40, ay + 118, '29.75/0.33 = 90.2 m', 13, fill=MUT))
    return 340, ''.join(o)

FIG[1] = (f1, 'The T-section of the second worked example under a sagging moment: the neutral axis sits 28.68 mm below the top, so the bottom fibre, 71.32 mm away, carries the larger stress (+118.9 MPa against −47.8 MPa). Right: the same bending makes a free cross-section curl the other way.',
          'A T-section with a 100 by 10 millimetre flange and a 90 by 10 millimetre web, its neutral axis dashed 28.68 millimetres below the top and 71.32 millimetres above the bottom. Beside it a linear stress diagram: minus 47.8 megapascals compression at the top, plus 118.9 megapascals tension at the bottom, zero at the neutral axis. On the right, a rectangle and its curled shape after bending: the compression side widens, the tension side narrows, with anticlastic radius R prime equal to R over nu, 29.75 over 0.33 equals 90.2 metres in the first example.')


# ---- 4.2 Z-section: tilted neutral axis, principal axes, stresses at the corners ----
def f2():
    s = 2.0
    cx, cy = 250, 215
    P_ = lambda x, y: (cx + x * s, cy - y * s)
    o = [T(250, 28, 'Z-section, M<tspan font-size="11" dy="4">x</tspan><tspan dy="-4"> = +1.0 kN·m</tspan>', 15, bold=True)]
    # walls (mid-lines drawn thick)
    for a, b in (((0, -50), (0, 50)), ((0, 50), (50, 50)), ((0, -50), (-50, -50))):
        (x1, y1), (x2, y2) = P_(*a), P_(*b)
        o.append(L(x1, y1, x2, y2, AC, 6))
    # axes
    o.append(arrow(cx - 150, cy, cx + 160, cy, L2, 1.5, 'm')); o.append(T(cx + 166, cy + 5, 'x', 14, 'start', MUT, True))
    o.append(arrow(cx, cy + 150, cx, cy - 150, L2, 1.5, 'm')); o.append(T(cx + 8, cy - 148, 'y', 14, 'start', MUT, True))
    # neutral axis at 56.3 deg
    a = math.atan(1.5); r = 150
    o.append(L(cx - r * math.cos(a), cy + r * math.sin(a), cx + r * math.cos(a), cy - r * math.sin(a), LV, 2.5, '9 5'))
    # principal axis u at -22.5
    th = rad(-22.5); r2 = 175
    o.append(L(cx - r2 * math.cos(th), cy + r2 * math.sin(th), cx + r2 * math.cos(th), cy - r2 * math.sin(th), NX, 1.8, '3 4'))
    o.append(C(cx, cy, 5, INK)); o.append(T(cx - 10, cy + 20, 'G', 14, 'end', INK, True))
    # points
    pts = [((0, 50), 'A +171.4', 'end', -12, -8), ((50, 50), 'B −85.7', 'start', 8, -8), ((0, -50), '−171.4', 'start', 10, 18), ((-50, -50), '+85.7', 'end', -8, 20)]
    for (x, y), lab, anc, dx, dy in pts:
        X, Y = P_(x, y)
        col = NX if '+' in lab else LV
        o.append(C(X, Y, 6, col))
        o.append(Tb(X + dx, Y + dy, lab, 14, anc, col, True))
    o.append(T(250, 420, 'web 100 mm, flanges 50 mm, t = 2 mm; stresses in MPa', 13, fill=MUT))
    # right panel: numbers
    x0 = 500
    rows = [('I<tspan font-size="11" dy="4">xx</tspan><tspan dy="-4"> = 666,667 mm⁴</tspan>', INK),
            ('I<tspan font-size="11" dy="4">yy</tspan><tspan dy="-4"> = 166,667 mm⁴</tspan>', INK),
            ('I<tspan font-size="11" dy="4">xy</tspan><tspan dy="-4"> = +250,000 mm⁴</tspan>', INK),
            ('tan α = I<tspan font-size="11" dy="4">xy</tspan><tspan dy="-4">/I</tspan><tspan font-size="11" dy="4">yy</tspan><tspan dy="-4"> = 1.5</tspan>', LV),
            ('α = 56.3°', LV),
            ('simple My/I gives 75.0', MUT),
            ('at A and at B', MUT)]
    o.append(R(x0, 70, 210, 330, PANEL, L2, 8))
    o.append(L(x0 + 14, 340, x0 + 54, 340, LV, 2.5, '9 5')); o.append(T(x0 + 62, 345, 'neutral axis', 13, 'start', LV, True))
    o.append(L(x0 + 14, 372, x0 + 54, 372, NX, 1.8, '3 4')); o.append(T(x0 + 62, 377, 'principal u, −22.5°', 13, 'start', NX, True))
    for i, (txt, col) in enumerate(rows):
        o.append(T(x0 + 14, 102 + i * 32, txt, 14, 'start', col, i in (3, 4)))
    return 432, ''.join(o)

FIG[2] = (f2, 'The worked example\'s Z-section under M<sub>x</sub> = +1.0 kN·m. The neutral axis tilts to 56.3°, so the web corners (±171.4 MPa) are the points farthest from it and carry the largest stress, while the flange tips carry only ∓85.7 MPa. The principal u axis lies at −22.5°.',
          'A Z-section drawn to scale: a vertical web of 100 millimetres with a top flange pointing right and a bottom flange pointing left. Horizontal x and vertical y axes cross at the centroid G. A dashed neutral axis passes through G at 56.3 degrees, and a dotted principal u axis at minus 22.5 degrees. Point A at the top web corner carries plus 171.4 megapascals, point B at the top flange tip minus 85.7, the bottom corner minus 171.4 and the bottom flange tip plus 85.7. A panel lists I x x 666,667, I y y 166,667 and I x y 250,000 millimetres to the fourth, tan alpha equals 1.5 and alpha 56.3 degrees.')


# ---- 4.3 tip deflection vector and the deflected shape along the span ----
def f3():
    o = [T(210, 28, 'Tip of the Z cantilever, W = 500 N down', 15, bold=True)]
    cx, cy, sc = 175, 120, 8.0   # px per mm of deflection
    u, v = 21.16, -14.11
    o.append(arrow(cx - 60, cy, cx + 215, cy, L2, 1.5, 'm')); o.append(T(cx + 221, cy + 5, 'x', 14, 'start', MUT, True))
    o.append(arrow(cx, cy + 150, cx, cy - 70, L2, 1.5, 'm')); o.append(T(cx + 8, cy - 64, 'y', 14, 'start', MUT, True))
    # load
    o.append(arrow(cx - 40, cy - 60, cx - 40, cy + 30, INK, 3)); o.append(T(cx - 48, cy - 34, 'W', 14, 'end', INK, True))
    # neutral axis
    a = math.atan(1.5)
    o.append(L(cx - 45 * math.cos(a), cy + 45 * math.sin(a), cx + 80 * math.cos(a), cy - 80 * math.sin(a), LV, 2, '8 5'))
    o.append(T(cx + 80 * math.cos(a) + 6, cy - 80 * math.sin(a) + 4, 'neutral axis 56.3°', 13, 'start', LV, True))
    # components and resultant
    X, Y = cx + u * sc, cy - v * sc
    o.append(L(cx, cy, X, cy, NX, 2, '5 4')); o.append(L(X, cy, X, Y, NX, 2, '5 4'))
    o.append(arrow(cx, cy, X, Y, AC, 3.5))
    o.append(T((cx + X) / 2, cy - 8, 'u = 21.16 mm', 13, fill=NX, bold=True))
    o.append(T(X + 8, (cy + Y) / 2 + 5, 'v = −14.11', 13, 'start', NX, True))
    o.append(Tb(cx + 80, Y + 26, '25.43 mm at −33.7°', 14, 'middle', AC, True))
    # naive
    o.append(arrow(cx + 6, cy, cx + 6, cy + 6.17 * sc, MUT, 2, 'm', '3 3'))
    o.append(T(cx - 6, cy + 6.17 * sc + 4, 'if I<tspan font-size="11" dy="4">xy</tspan><tspan dy="-4"> ignored:</tspan>', 13, 'end', MUT))
    o.append(T(cx - 6, cy + 6.17 * sc + 21, '6.17 mm down', 13, 'end', MUT))
    # right: shape along span (UDL example)
    x0, x1, y0, y1 = 470, 700, 70, 270
    fx = lambda z: x0 + z / 1200 * (x1 - x0)
    fy = lambda d: y0 + (16 - d) / 32 * (y1 - y0)
    o.append(T(585, 28, 'Uniform load 0.8 N/mm: shape', 15, bold=True))
    o.append(axes(x0, x1, y0, y1, [0, 300, 600, 900, 1200], [-12, -8, -4, 0, 4, 8, 12, 16], fx, fy, 'z along the span (mm)', 'deflection (mm)', yfmt=lambda v: neg(v)))
    E, L_, w = 70000.0, 1200.0, 0.8; Ixx, Iyy, Ixy = 666667.0, 166667.0, 250000.0; D = Ixx * Iyy - Ixy ** 2
    f = lambda z: w * (6 * L_ ** 2 * z ** 2 - 4 * L_ * z ** 3 + z ** 4) / 24
    us = [(fx(z), fy(f(z) * Ixy / (E * D))) for z in range(0, 1201, 50)]
    vs = [(fx(z), fy(-f(z) * Iyy / (E * D))) for z in range(0, 1201, 50)]
    o.append(P(us, NX, 3)); o.append(P(vs, LV, 3))
    o.append(T(x1 - 4, fy(15.23) - 8, 'u: 15.23 at tip', 13, 'end', NX, True))
    o.append(T(x1 - 4, fy(-10.16) + 20, 'v: −10.16 at tip', 13, 'end', LV, True))
    return 330, ''.join(o)

FIG[3] = (f3, 'Left: under a 500 N downward tip load the Z cantilever\'s tip moves 21.16 mm sideways and 14.11 mm down, 25.43 mm at right angles to the neutral axis; ignoring I<sub>xy</sub> would predict 6.17 mm straight down. Right: the program\'s deflected shape under the uniform load, with u = −1.5 v at every station.',
          'Left, axes x and y at the tip centroid. A load arrow W points straight down. A dashed neutral axis runs at 56.3 degrees. The deflection components are 21.16 millimetres along x and minus 14.11 along y, and their resultant arrow is 25.43 millimetres at minus 33.7 degrees, perpendicular to the neutral axis. A faint arrow shows the 6.17 millimetre downward deflection predicted if I x y is ignored. Right, a plot of deflection against distance along the 1200 millimetre span under a uniform load: the sideways deflection u rises to 15.23 millimetres and the vertical deflection v falls to minus 10.16 millimetres at the tip.')


# ---- 4.4 the angle section: centroid, wall centroids and principal axis ----
def f4():
    s = 3.2; ox, oy = 110, 300   # corner at (ox, oy)
    P_ = lambda x, y: (ox + x * s, oy - y * s)
    o = [T(310, 28, 'Unequal angle 80 × 40 × 2 mm', 15, bold=True)]
    (a, b), (c, d) = P_(0, 0), P_(0, 80); o.append(L(a, b, c, d, AC, 7))
    (a, b), (c, d) = P_(0, 0), P_(40, 0); o.append(L(a, b, c, d, AC, 7))
    gx, gy = P_(6.667, 26.667)
    o.append(L(gx - 80, gy, gx + 200, gy, L2, 1.5, '6 4')); o.append(T(gx + 204, gy + 5, 'x', 14, 'start', MUT, True))
    o.append(L(gx, gy + 110, gx, gy - 165, L2, 1.5, '6 4')); o.append(T(gx + 6, gy - 167, 'y', 14, 'start', MUT, True))
    th = rad(15.8); r = 170
    o.append(L(gx - 100 * math.cos(th), gy + 100 * math.sin(th), gx + r * math.cos(th), gy - r * math.sin(th), NX, 2, '3 4'))
    o.append(T(gx + r * math.cos(th) + 4, gy - r * math.sin(th) - 6, 'u axis 15.8°', 13, 'start', NX, True))
    o.append(C(gx, gy, 6, INK)); o.append(Tb(gx + 16, gy + 22, 'G (6.67, 26.67)', 14, 'start', INK, True))
    for (x, y), lab, anc, dx in (((0, 40), 'leg centroid (−6.67, +13.33)', 'start', 14), ((20, 0), '(+13.33, −26.67)', 'start', 14)):
        X, Y = P_(x, y); o.append(C(X, Y, 5, LV)); o.append(Tb(X + dx, Y + (5 if y else 22), lab, 13, anc, LV))
    o.append(T(ox - 16, oy - 40 * s, '80', 14, 'end', MUT)); o.append(T(ox + 20 * s, oy + 40, '40', 14, fill=MUT))
    # numbers
    x0 = 470
    o.append(R(x0, 70, 240, 230, PANEL, L2, 8))
    rows = ['A = 240 mm²', 'I<tspan font-size="11" dy="4">xx</tspan><tspan dy="-4"> = 170,667 mm⁴</tspan>', 'I<tspan font-size="11" dy="4">yy</tspan><tspan dy="-4"> = 32,000 mm⁴</tspan>',
            'I<tspan font-size="11" dy="4">xy</tspan><tspan dy="-4"> = −42,667 mm⁴</tspan>', 'I<tspan font-size="11" dy="4">u</tspan><tspan dy="-4"> = 182,743 mm⁴</tspan>', 'I<tspan font-size="11" dy="4">v</tspan><tspan dy="-4"> = 19,924 mm⁴</tspan>']
    for i, t in enumerate(rows):
        o.append(T(x0 + 16, 102 + i * 34, t, 14, 'start', NX if i > 3 else INK, i == 3))
    return 360, ''.join(o)

FIG[4] = (f4, 'The first worked example\'s angle drawn as two mid-lines. Both leg centroids lie in the second and fourth quadrants about the centroid G, which is why I<sub>xy</sub> is negative; the principal u axis is turned 15.8° from x.',
          'An L-shaped angle drawn as two thick mid-lines: a vertical leg of 80 millimetres and a horizontal leg of 40 millimetres meeting at the bottom-left corner. Dashed centroidal x and y axes cross at G, 6.67 millimetres right of and 26.67 millimetres above the corner. The vertical leg centroid sits at minus 6.67, plus 13.33 and the horizontal leg centroid at plus 13.33, minus 26.67 from G. A dotted principal u axis runs at 15.8 degrees. A panel lists area 240 square millimetres, I x x 170,667, I y y 32,000, I x y minus 42,667, I u 182,743 and I v 19,924 millimetres to the fourth.')


# ---- 4.5 four-boom wing box with unequal booms ----
def f5():
    o = [T(360, 26, 'Wing box at the station: M<tspan font-size="11" dy="4">x</tspan><tspan dy="-4"> = −30 kN·m, M</tspan><tspan font-size="11" dy="4">y</tspan><tspan dy="-4"> = −6 kN·m</tspan>', 15, bold=True)]
    s = 0.75; ox, oy = 130, 250
    P_ = lambda x, y: (ox + x * s, oy - y * s)
    (x1, y1), (x2, y2) = P_(0, 200), P_(600, 0)
    o.append(R(x1, y1, x2 - x1, y2 - y1, 'none', L2, 4, 1.5))
    gx, gy = P_(218.2, 109.1)
    o.append(L(gx - 200, gy - 200 * math.tan(rad(2.7)), gx + 330, gy + 330 * math.tan(rad(2.7)), LV, 2.2, '8 5'))
    o.append(T(gx + 250, gy - 4, 'neutral axis −2.7°', 13, 'middle', LV, True))
    o.append(C(gx, gy, 6, INK)); o.append(T(gx - 10, gy + 22, 'G', 14, 'end', INK, True))
    booms = [(0, 200, 800, 'boom 1, 800 mm²', '−111.8'), (600, 200, 400, 'boom 2, 400 mm²', '−151.3'), (600, 0, 400, 'boom 3, 400 mm²', '+126.3'), (0, 0, 600, 'boom 4, 600 mm²', '+165.8')]
    for x, y, A, lab, sg in booms:
        X, Y = P_(x, y); r = math.sqrt(A) / 2.2
        col, soft = (LV, LVS) if sg.startswith('−') else (NX, NXS)
        o.append(f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="{r:.1f}" style="fill:{soft};stroke:{col};stroke-width:2.5"/>')
        up = y > 100
        o.append(T(X, Y + (-22 - r + 8 if up else 30 + r - 8), lab, 13, fill=MUT))
        o.append(T(X + (-r - 8 if x == 0 else r + 8), Y + 5, f'{sg} MPa', 15, 'end' if x == 0 else 'start', col, True))
    o.append(T(ox + 300 * s, oy + 54, 'front ← 600 mm → rear; depth 200 mm; x aft, y up', 13, fill=MUT))
    o.append(T(ox + 300 * s, oy + 74, 'ignoring I<tspan font-size="11" dy="4">xy</tspan><tspan dy="-4"> gives −137.5 MPa at boom 2</tspan>', 13, fill=MUT))
    return 340, ''.join(o)

FIG[5] = (f5, 'The worked example\'s four unequal booms, circles drawn in proportion to their areas. The centroid G moves towards the big front booms, the neutral axis tilts slightly, and the small rear top boom 2 carries the largest compression, −151.3 MPa.',
          'A 600 by 200 millimetre rectangle with a boom at each corner: boom 1 front top 800 square millimetres at minus 111.8 megapascals, boom 2 rear top 400 at minus 151.3, boom 3 rear bottom 400 at plus 126.3, boom 4 front bottom 600 at plus 165.8. The centroid G lies towards the front, and a dashed neutral axis passes through it at minus 2.7 degrees. A note says that ignoring I x y would give minus 137.5 megapascals at boom 2.')


# ---- 4.6 spar temperature and stress profiles; heated boom ----
def f6():
    o = [T(185, 26, 'Spar held straight, free to extend', 15, bold=True)]
    y0, y1 = 70, 270   # top and bottom of the spar in px (100 mm)
    # temperature plot
    x0, x1 = 50, 170
    fT = lambda t: x0 + t / 40 * (x1 - x0)
    o.append(L(x0, y0, x0, y1, L2, 1.5)); o.append(L(x0, y1, x1, y1, L2, 1.5))
    for t in (0, 20, 40):
        o.append(T(fT(t), y1 + 20, str(t), 13, fill=MUT))
    o.append(T((x0 + x1) / 2, y1 + 40, 'temperature (°C)', 13, fill=MUT))
    o.append(P([(fT(35), y0), (fT(5), y1)], LV, 3))
    o.append(T(fT(35) + 4, y0 - 6, '35 °C top', 13, 'middle', LV, True)); o.append(T(fT(5) + 6, y1 - 8, '5 °C', 13, 'start', LV, True))
    o.append(L(x0, (y0 + y1) / 2, x1, (y0 + y1) / 2, 'var(--line)', 1, '3 3'))
    # stress plot
    sx0 = 270; k = 3.0
    o.append(L(sx0, y0, sx0, y1, L2, 1.5))
    o.append(poly([(sx0, (y0 + y1) / 2), (sx0 - 24.15 * k, y0), (sx0, y0)], LVS, LV))
    o.append(poly([(sx0, (y0 + y1) / 2), (sx0 + 24.15 * k, y1), (sx0, y1)], NXS, NX))
    o.append(T(sx0 + 6, y0 + 16, '−24.15', 13, 'start', LV, True))
    o.append(T(sx0 + 24.15 * k + 4, y1 - 4, '+24.15', 13, 'start', NX, True))
    o.append(T(sx0, y1 + 20, '0', 13, fill=MUT)); o.append(T(sx0, y1 + 40, 'stress (MPa)', 13, fill=MUT))
    o.append(T(sx0 + 16, (y0 + y1) / 2 - 6, 'zero at mid-depth', 13, 'start', MUT))
    # boom box
    o.append(T(540, 26, 'Free four-boom beam, boom 1 +50 K', 15, bold=True))
    bx0, by0, bw, bh = 430, 90, 190, 120
    o.append(R(bx0, by0, bw, bh, 'none', L2, 4, 1.5))
    B = [(bx0 + bw, by0, '1 hot', '−20.1', LV, LVS), (bx0, by0, '2', '+20.1', NX, NXS), (bx0, by0 + bh, '3', '−20.1', LV, LVS), (bx0 + bw, by0 + bh, '4', '+20.1', NX, NXS)]
    for X, Y, lab, sg, col, soft in B:
        o.append(f'<circle cx="{X}" cy="{Y}" r="15" style="fill:{soft};stroke:{col};stroke-width:2.5"/>')
        o.append(T(X, Y + 5, lab.split()[0], 13, bold=True))
        dx = 24 if X > bx0 else -24
        o.append(T(X + dx, Y + 5, sg, 15, 'start' if dx > 0 else 'end', col, True))
    o.append(T(bx0 + bw + 24, by0 - 22, 'heated', 13, 'start', LV))
    o.append(T(bx0 + bw / 2, by0 + bh + 44, 'booms at (±200, ±75) mm; stresses in MPa', 13, fill=MUT))
    o.append(T(bx0 + bw / 2, by0 + bh + 64, 'net force and both moments are zero', 13, fill=MUT))
    return 330, ''.join(o)

FIG[6] = (f6, 'Left: the first worked example\'s spar, its temperature falling linearly from 35 °C at the top to 5 °C at the bottom, and, on a separate axis, the stress when it is held straight: −24.15 MPa at the hot top, +24.15 MPa at the cool bottom. Right: the second example\'s free four-boom beam with one boom heated by 50 K: ±20.1 MPa in a chequer pattern.',
          'Two small plots share the depth of a 100 millimetre spar. The first shows temperature falling linearly from 35 degrees at the top to 5 degrees at the bottom. The second shows stress: minus 24.15 megapascals compression at the top, zero at mid-depth, plus 24.15 tension at the bottom. On the right, a rectangle with four booms: boom 1 top right is heated and carries minus 20.1, boom 2 top left plus 20.1, boom 3 bottom left minus 20.1, boom 4 bottom right plus 20.1 megapascals. A note says the net force and both moments are zero.')

spec = make_spec(FIG)


def text_fixes(k):
    return []
