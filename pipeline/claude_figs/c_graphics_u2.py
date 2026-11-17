"""Claude's hand-drawn figures for c-graphics-u2 (Computer Graphics, unit 2: 2D and 3D transformations, viewing,
clipping and projection), one per chapter, from each chapter's worked example."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def grid(o, fx, fy, xs, ys, xlab=True, ylab=True):
    """light integer grid with the two axes through the origin and tick numbers on the outer frame"""
    for x in xs:
        o.append(L(fx(x), fy(ys[0]), fx(x), fy(ys[-1]), LN, 1))
    for y in ys:
        o.append(L(fx(xs[0]), fy(y), fx(xs[-1]), fy(y), LN, 1))
    if xs[0] <= 0 <= xs[-1]: o.append(L(fx(0), fy(ys[0]), fx(0), fy(ys[-1]), L2, 1.6))
    if ys[0] <= 0 <= ys[-1]: o.append(L(fx(xs[0]), fy(0), fx(xs[-1]), fy(0), L2, 1.6))
    if xlab:
        for x in xs:
            o.append(T(fx(x), fy(ys[0]) + 19, neg(x), 13, fill=MUT))
    if ylab:
        for y in ys:
            o.append(T(fx(xs[0]) - 9, fy(y) + 4.5, neg(y), 13, 'end', MUT))


def poly(pts, fill, c, w=2.4, dash=None):
    d = f';stroke-dasharray:{dash}' if dash else ''
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" style="fill:{fill};stroke:{c};stroke-width:{w}{d};stroke-linejoin:round"/>'


def mat(o, x, y, rows, cw=40, rh=30, size=15, col=None):
    """bracketed matrix with top-left corner (x, y); col(i, j) -> (colour, bold); returns the right edge"""
    m, n = len(rows), len(rows[0])
    W, H = n * cw + 8, m * rh + 6
    o.append(P([(x + 8, y), (x, y), (x, y + H), (x + 8, y + H)], INK, 2))
    o.append(P([(x + W - 8, y), (x + W, y), (x + W, y + H), (x + W - 8, y + H)], INK, 2))
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            c, b = col(i, j) if col else (INK, False)
            o.append(T(x + 4 + cw * j + cw / 2, y + 3 + rh * i + rh / 2 + size * 0.35, neg(v), size, fill=c, bold=b))
    return x + W


def arcpath(cx, cy, r, a1, a2, c=AC, w=2, arrow='n', dash=None, ry=None):
    """arc of a circle (or ellipse with ry) about (cx, cy) from angle a1 to a2 in degrees, counter-clockwise on screen"""
    ry = ry or r
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy - ry * math.sin(math.radians(a1))
    x2, y2 = cx + r * math.cos(math.radians(a2)), cy - ry * math.sin(math.radians(a2))
    d = f';stroke-dasharray:{dash}' if dash else ''
    m = f' marker-end="url(#ar-UID-{arrow})"' if arrow else ''
    big = 1 if abs(a2 - a1) > 180 else 0
    return f'<path d="M{x1:.1f},{y1:.1f} A{r:.1f},{ry:.1f} 0 {big} 0 {x2:.1f},{y2:.1f}" style="fill:none;stroke:{c};stroke-width:{w}{d}"{m}/>'


# ---- 2.1 rotate the triangle 90 degrees about the origin ----
def f1():
    o = []
    s = 55
    fx = lambda v: 215 + v * s
    fy = lambda v: 200 - v * s
    grid(o, fx, fy, list(range(-3, 4)), list(range(-1, 4)))
    A, B, Cc = (0, 0), (2, 0), (0, 2)
    Bp, Cp = (0, 2), (-2, 0)
    o.append(poly([(fx(x), fy(y)) for x, y in (A, B, Cc)], ACS, AC))
    o.append(poly([(fx(x), fy(y)) for x, y in (A, Bp, Cp)], NXS, NX))
    # right-angle marks
    q = 0.28 * s
    o.append(P([(fx(0) + q, fy(0)), (fx(0) + q, fy(0) - q), (fx(0), fy(0) - q)], AC, 1.6))
    o.append(P([(fx(0) - q, fy(0)), (fx(0) - q, fy(0) - q), (fx(0), fy(0) - q)], NX, 1.6))
    # B swings to B'
    o.append(arcpath(fx(0), fy(0), 2.45 * s, 2, 86, LV, 2.2, 'l', '6 4'))
    o.append(Tb(fx(1.93), fy(1.93) - 4, 'B turns 90°', 13, 'start', LV, True))
    for (x, y), c in ((A, INK), (B, AC), (Cc, AC), (Cp, NX)):
        o.append(C(fx(x), fy(y), 6, c))
    o.append(Tb(fx(0) + 8, fy(0) + 20, 'A = A′ (0, 0)', 13, 'start', INK, True))
    o.append(Tb(fx(2), fy(0) + 20, 'B (2, 0)', 13, 'middle', AC, True))
    o.append(Tb(fx(-2), fy(0) + 20, 'C′ (−2, 0)', 13, 'middle', NX, True))
    o.append(Tb(fx(0) - 8, fy(2) - 12, 'C = B′ (0, 2)', 13, 'end', INK, True))
    # side lengths
    o.append(T(fx(1.1), fy(1.1) - 2, '2√2', 14, 'start', AC, True))
    o.append(T(fx(-1.1), fy(1.1) - 2, '2√2', 14, 'end', NX, True))
    o.append(T(fx(1), fy(0) - 8, '2', 14, 'middle', AC, True))
    o.append(T(fx(-1), fy(0) - 8, '2', 14, 'middle', NX, True))
    o.append(T(fx(0) + 8, fy(1) + 5, '2', 14, 'start', INK, True))
    xr = 420
    o.append(T(xr, 46, 'θ = 90°: cos θ = 0, sin θ = 1', 14, 'start', INK, True))
    o.append(T(xr, 70, 'x′ = −y,  y′ = x', 14, 'start', INK, True))
    o.append(T(xr, 106, 'A (0, 0) → A′ (0, 0)', 14, 'start', INK))
    o.append(T(xr, 130, 'B (2, 0) → B′ (0, 2)', 14, 'start', NX))
    o.append(T(xr, 154, 'C (0, 2) → C′ (−2, 0)', 14, 'start', NX))
    o.append(T(xr, 192, 'sides before: 2, 2, 2√2', 14, 'start', AC, True))
    o.append(T(xr, 216, 'sides after:  2, 2, 2√2', 14, 'start', NX, True))
    o.append(T(xr, 252, 'A′B′ · A′C′ = (0, 2) · (−2, 0) = 0', 13, 'start', MUT))
    o.append(T(xr, 272, 'so the right angle at A stays 90°', 13, 'start', MUT))
    return 290, ''.join(o)
FIG[1] = (f1, 'Rotating A(0,0), B(2,0), C(0,2) by 90° counter-clockwise with x′ = −y, y′ = x gives A′(0,0), B′(0,2), C′(−2,0). A stays put, B swings round to where C was, and the sides are still 2, 2 and 2√2 with the right angle at A.',
          'A grid with the blue triangle A(0,0), B(2,0), C(0,2) and the green rotated triangle A′(0,0), B′(0,2), C′(−2,0), a dashed arc showing B turning 90°, side lengths 2, 2 and 2√2 marked on both, and the rule x′ = −y, y′ = x beside.')


# ---- 2.2 translation as one 3x3 multiply ----
def f2():
    o = []
    y0, rh, cw = 56, 40, 44
    o.append(T(40, 30, 'T(5, 3)', 14, 'start', INK, True))

    def tcol(i, j):
        if j == 2 and i < 2: return AC, True
        if i == 2: return MUT, False
        return INK, False
    xe = mat(o, 40, y0, [[1, 0, 5], [0, 1, 3], [0, 0, 1]], cw, rh, 17, tcol)
    o.append(T(xe + 18, y0 + 3 + 1.5 * rh + 6, '×', 18, fill=INK, bold=True))
    o.append(T(xe + 36 + 26, 30, 'P', 14, 'middle', INK, True))
    xe2 = mat(o, xe + 36, y0, [[2], [1], [1]], cw, rh, 17, lambda i, j: (LV, True) if i == 2 else (INK, False))
    o.append(T(xe2 + 18, y0 + 3 + 1.5 * rh + 6, '=', 18, fill=INK, bold=True))
    o.append(T(xe2 + 36 + 26, 30, 'P′', 14, 'middle', NX, True))
    xe3 = mat(o, xe2 + 36, y0, [[7], [4], [1]], cw, rh, 17, lambda i, j: (NX, True))
    xr = xe3 + 34
    rows = [('x′ = 1×2 + 0×1 + <tspan style="fill:var(--accent)">5</tspan>×<tspan style="fill:var(--live)">1</tspan> = 7', INK),
            ('y′ = 0×2 + 1×1 + <tspan style="fill:var(--accent)">3</tspan>×<tspan style="fill:var(--live)">1</tspan> = 4', INK),
            ('W′ = 0×2 + 0×1 + 1×1 = 1', MUT)]
    for i, (s_, c) in enumerate(rows):
        o.append(T(xr, y0 + 3 + rh * i + rh / 2 + 5, s_, 14, 'start', c, True))
    yb = y0 + 3 * rh + 6
    o.append(brace(40 + 4 + 2 * cw + 4, 40 + 4 + 3 * cw - 4, yb + 10, AC))
    o.append(T(40 + 3 * cw + 4, yb + 36, 'tx = 5, ty = 3', 14, 'end', AC, True))
    o.append(T(40 + 3 * cw + 4, yb + 54, 'sit in the last column', 13, 'end', MUT))
    xp = xe + 36 + 4 + cw / 2
    o.append(L(xp, yb + 24, xp, yb + 6, LV, 2, arrow='l'))
    o.append(T(xp - 14, yb + 42, 'W = 1 picks up', 13, 'start', LV, True))
    o.append(T(xp - 14, yb + 60, 'the shift', 13, 'start', LV, True))
    o.append(T(xr, yb + 36, 'last row 0 0 1 keeps W′ = 1,', 13, 'start', MUT))
    o.append(T(xr, yb + 54, 'so P′ = (7, 4) needs no division', 13, 'start', MUT))
    # small picture of the move
    s, X0, Y0 = 24, 120, yb + 220
    fx = lambda v: X0 + v * s
    fy = lambda v: Y0 - v * s
    grid(o, fx, fy, list(range(0, 9)), list(range(0, 6)))
    o.append(L(fx(2), fy(1), fx(7), fy(1), AC, 2, '5 4'))
    o.append(L(fx(7), fy(1), fx(7), fy(4), AC, 2, '5 4'))
    o.append(L(fx(2), fy(1), fx(7) - 5, fy(4) + 3.5, LV, 2.2, arrow='l'))
    o.append(C(fx(2), fy(1), 6, INK)); o.append(C(fx(7), fy(4), 6, NX))
    o.append(T(fx(2) - 4, fy(1) - 12, 'P (2, 1)', 13, 'end', INK, True))
    o.append(T(fx(7) + 10, fy(4) - 8, 'P′ (7, 4)', 13, 'start', NX, True))
    o.append(T(fx(4.5), fy(1) + 16, '+5', 13, 'middle', AC, True))
    o.append(T(fx(7) + 8, fy(2.5) + 5, '+3', 13, 'start', AC, True))
    o.append(T(fx(9) + 40, fy(3.4), 'one multiply moves', 13, 'start', MUT))
    o.append(T(fx(9) + 40, fy(3.4) + 18, 'the point 5 right and 3 up', 13, 'start', MUT))
    return Y0 + 32, ''.join(o)
FIG[2] = (f2, 'The shift tx = 5, ty = 3 sits in the last column of the 3×3 matrix, and the point\'s third cell W = 1 multiplies it in, so P(2, 1) becomes P′(7, 4). The fixed last row 0 0 1 keeps W′ = 1.',
          'The matrix product [1 0 5; 0 1 3; 0 0 1] times the column (2, 1, 1) equals (7, 4, 1), with each row worked out beside it, and below a small grid showing P(2,1) moving 5 right and 3 up to P′(7,4).')


# ---- 2.3 rotation about the pivot (1, 1) ----
def f3():
    o = []
    s = 52
    fx = lambda v: 80 + (v + 1) * s
    fy = lambda v: 290 - (v + 1) * s
    grid(o, fx, fy, list(range(-1, 5)), list(range(-1, 5)))
    # direct rotation about the pivot
    o.append(arcpath(fx(1), fy(1), 2 * s, 3, 87, NX, 2, 'x', '2 4'))
    # the three steps
    o.append(L(fx(3) - 4, fy(1) + 4, fx(2) + 5, fy(0) - 5, L2, 2.2, arrow='m'))
    o.append(arcpath(fx(0), fy(0), 2 * s, 4, 86, LV, 2.2, 'l'))
    o.append(L(fx(0) + 4, fy(2) - 4, fx(1) - 5, fy(3) + 5, L2, 2.2, arrow='m'))
    o.append(T(fx(2.6) + 6, fy(0.4) + 8, '1', 15, 'start', INK, True))
    o.append(T(fx(1.62), fy(1.62) + 2, '2', 15, 'middle', LV, True))
    o.append(T(fx(0.5) - 10, fy(2.5) - 4, '3', 15, 'end', INK, True))
    o.append(f'<circle cx="{fx(1):.1f}" cy="{fy(1):.1f}" r="7" style="fill:var(--fig);stroke:var(--ink);stroke-width:2.2"/>')
    o.append(T(fx(1) - 12, fy(1) + 20, 'pivot (1, 1)', 13, 'end', INK, True))
    for (x, y), c in (((3, 1), AC), ((2, 0), L2), ((0, 2), L2), ((1, 3), NX)):
        o.append(C(fx(x), fy(y), 6, c))
    o.append(Tb(fx(3) + 10, fy(1) + 5, '(3, 1)', 13, 'start', AC, True))
    o.append(Tb(fx(2) + 10, fy(0) + 18, '(2, 0)', 13, 'start', MUT, True))
    o.append(Tb(fx(0) - 10, fy(2) + 5, '(0, 2)', 13, 'end', MUT, True))
    o.append(Tb(fx(1) + 10, fy(3) - 8, '(1, 3)', 13, 'start', NX, True))
    xr = 410
    o.append(T(xr, 40, '1  T(−1, −1): (3, 1) → (2, 0)', 14, 'start', INK, True))
    o.append(T(xr, 64, '2  R(90°):  (2, 0) → (0, 2)', 14, 'start', LV, True))
    o.append(T(xr, 88, '3  T(1, 1):  (0, 2) → (1, 3)', 14, 'start', INK, True))
    o.append(T(xr, 126, 'M = T(1, 1) · R(90°) · T(−1, −1)', 14, 'start', NX, True))
    o.append(T(xr, 146, 'right to left = the order applied', 13, 'start', MUT))
    xe = mat(o, xr + 28, 164, [[0, -1, 2], [1, 0, 0], [0, 0, 1]], 40, 30, 15, lambda i, j: (NX, True))
    o.append(T(xr, 164 + 3 + 45 + 5, 'M =', 14, 'start', NX, True))
    o.append(T(xr, 290, 'M · (3, 1, 1) = (0 − 1 + 2, 3, 1)', 13, 'start', INK, True))
    o.append(T(xr, 310, '= (1, 3, 1): the dotted arc, in one step', 13, 'start', NX, True))
    return 330, ''.join(o)
FIG[3] = (f3, 'Rotating (3, 1) by 90° about the pivot (1, 1) in three moves: shift to (2, 0), turn to (0, 2), shift back to (1, 3). Multiplied together right to left, T(1,1) · R(90°) · T(−1,−1) is one matrix M that does the same turn, the dotted arc, in one multiply.',
          'A grid with the pivot (1,1) circled and the point (3,1) moving through (2,0) and (0,2) to (1,3) in three numbered arrows, a dotted arc about the pivot from (3,1) to (1,3), and the matrix M = [0 −1 2; 1 0 0; 0 0 1] beside it.')


# ---- 2.4 3D: rotate about z, then translate along z ----
def f4():
    o = []
    s = 52
    ox, oy = 200, 330
    ux, uy = (-0.62 * s, 0.42 * s)  # one unit along x (out of the page, drawn down-left)
    pt = lambda x, y, z: (ox + x * ux + y * s, oy + x * uy - z * s)
    # axes
    o.append(L(*pt(0, 0, 0), *pt(2.2, 0, 0), L2, 1.8, arrow='m'))
    o.append(L(*pt(0, 0, 0), *pt(0, 2.6, 0), L2, 1.8, arrow='m'))
    o.append(L(*pt(0, 0, 0), *pt(0, 0, 5.8), L2, 1.8, arrow='m'))
    X, Y, Z = pt(2.2, 0, 0), pt(0, 2.6, 0), pt(0, 0, 5.8)
    o.append(T(X[0] - 8, X[1] + 12, 'x', 15, 'end', MUT, True))
    o.append(T(Y[0] + 10, Y[1] + 5, 'y', 15, 'start', MUT, True))
    o.append(T(Z[0] - 12, Z[1] + 6, 'z', 15, 'end', MUT, True))
    for z in range(1, 6):
        a, b = pt(0, 0, z)
        o.append(L(a - 5, b, a, b, L2, 1.5)); o.append(T(a - 9, b + 4.5, str(z), 13, 'end', MUT))
    # rotation about z in the xy plane: quarter of the unit circle (x=cos, y=sin)
    pts = [pt(math.cos(t), math.sin(t), 0) for t in [i / 30 * math.pi / 2 for i in range(31)]]
    o.append(P(pts[:-2] + [((pts[-2][0] + pts[-1][0]) / 2 - 4, (pts[-2][1] + pts[-1][1]) / 2)], LV, 2.2, '6 4'))
    o.append(L(pts[-3][0], pts[-3][1], pts[-1][0] - 7, pts[-1][1], LV, 2.2, arrow='l'))
    P0, P1, P2 = pt(1, 0, 0), pt(0, 1, 0), pt(0, 1, 5)
    o.append(L(P1[0], P1[1] - 8, P2[0], P2[1] + 10, AC, 2.4, '6 4', 'n'))
    for (a, b), c in ((P0, INK), (P1, LV), (P2, NX)):
        o.append(C(a, b, 6.5, c))
    o.append(Tb(P0[0] - 12, P0[1] + 6, 'P (1, 0, 0)', 13, 'end', INK, True))
    o.append(Tb(P1[0] + 12, P1[1] + 20, '(0, 1, 0)', 13, 'start', LV, True))
    o.append(Tb(P2[0] + 12, P2[1] + 5, '(0, 1, 5)', 14, 'start', NX, True))
    o.append(T((P0[0] + P1[0]) / 2 + 2, P0[1] + 34, 'Rz(90°)', 13, 'middle', LV, True))
    o.append(T(P1[0] + 12, (P1[1] + P2[1]) / 2, 'T(0, 0, 5)', 13, 'start', AC, True))
    xr = 400
    o.append(T(xr, 36, 'Rz(90°), cos 90° = 0, sin 90° = 1', 14, 'start', LV, True))
    xe = mat(o, xr, 50, [[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], 30, 26, 14, lambda i, j: (LV, True) if i < 2 and j < 2 else (INK, False))
    o.append(T(xe + 14, 50 + 3 + 52 + 5 + 6, '×', 16, fill=INK, bold=True))
    xe2 = mat(o, xe + 28, 50, [[1], [0], [0], [1]], 30, 26, 14)
    o.append(T(xe2 + 14, 50 + 3 + 52 + 5 + 6, '=', 16, fill=INK, bold=True))
    mat(o, xe2 + 28, 50, [[0], [1], [0], [1]], 30, 26, 14, lambda i, j: (LV, True))
    o.append(T(xr, 192, 'x′ = −y = 0,  y′ = x = 1,  z′ = z = 0', 13, 'start', INK))
    o.append(T(xr, 230, 'T(0, 0, 5): add 5 to z only', 14, 'start', AC, True))
    o.append(T(xr, 254, '(0, 1, 0) → (0, 1, 0 + 5) = (0, 1, 5)', 13, 'start', INK))
    o.append(T(xr, 292, 'Rz never changes z, so only', 13, 'start', MUT))
    o.append(T(xr, 312, 'the translation lifts the point', 13, 'start', MUT))
    return 402, ''.join(o)
FIG[4] = (f4, 'P(1, 0, 0) turns 90° about the z axis to (0, 1, 0), staying in the floor plane z = 0, then T(0, 0, 5) lifts it straight up to (0, 1, 5). Rz leaves z alone, so only the translation changes it.',
          'Three-dimensional x, y and z axes with P(1,0,0) on the x axis, a dashed quarter arc about z to (0,1,0) on the y axis, and a dashed arrow up 5 units to (0,1,5); beside it the 4 by 4 Rz(90°) matrix times (1,0,0,1) giving (0,1,0,1).')


# ---- 2.5 window to viewport ----
def f5():
    o = []
    # world window
    s = 24
    wx = lambda v: 34 + v * s
    wy = lambda v: 230 - v * s
    o.append(L(wx(0), wy(0), wx(11), wy(0), L2, 1.5)); o.append(L(wx(0), wy(0), wx(0), wy(6.3), L2, 1.5))
    for v in (0, 5, 10):
        o.append(L(wx(v), wy(0), wx(v), wy(0) + 5, L2, 1.5)); o.append(T(wx(v), wy(0) + 20, str(v), 13, fill=MUT))
    for v in (0, 2.5, 5):
        o.append(L(wx(0) - 5, wy(v), wx(0), wy(v), L2, 1.5)); o.append(T(wx(0) - 9, wy(v) + 4.5, str(v), 13, 'end', MUT))
    o.append(R(wx(0), wy(5), 10 * s, 5 * s, ACS, AC, 0, 2.2))
    o.append(L(wx(5), wy(0), wx(5), wy(5), AC, 1, '3 4')); o.append(L(wx(0), wy(2.5), wx(10), wy(2.5), AC, 1, '3 4'))
    o.append(C(wx(5), wy(2.5), 6.5, AC))
    o.append(Tb(wx(5) + 10, wy(2.5) - 10, '(5, 2.5)', 13, 'start', AC, True))
    o.append(T(wx(5), 40, 'window in world units', 14, 'middle', AC, True))
    o.append(T(wx(5), 60, '10 wide, 5 high', 13, 'middle', MUT))
    # device
    d = 0.88
    dx = lambda v: 420 + v * d
    dy = lambda v: 230 - v * d
    o.append(L(dx(0), dy(0), dx(320), dy(0), L2, 1.5)); o.append(L(dx(0), dy(0), dx(0), dy(178), L2, 1.5))
    for v in (0, 100, 200, 300):
        o.append(L(dx(v), dy(0), dx(v), dy(0) + 5, L2, 1.5)); o.append(T(dx(v), dy(0) + 20, str(v), 13, fill=MUT))
    for v in (0, 50, 100, 160):
        o.append(L(dx(0) - 5, dy(v), dx(0), dy(v), L2, 1.5)); o.append(T(dx(0) - 9, dy(v) + 4.5, str(v), 13, 'end', MUT))
    o.append(R(dx(0), dy(100), 200 * d, 100 * d, ACS, AC, 0, 2.2))
    o.append(R(dx(100), dy(160), 200 * d, 100 * d, NXS, NX, 0, 2.2, '7 4'))
    o.append(C(dx(100), dy(50), 6.5, AC)); o.append(C(dx(200), dy(110), 6.5, NX))
    o.append(Tb(dx(100) - 10, dy(50) + 22, '(a) (100, 50)', 13, 'end', AC, True))
    o.append(Tb(dx(200) + 10, dy(110) - 8, '(b) (200, 110)', 13, 'start', NX, True))
    o.append(T(dx(150), 40, 'viewports in device units', 14, 'middle', INK, True))
    # mapping arrow
    o.append(arc(wx(10) + 6, wy(5) - 4, dx(0) - 4, dy(100) - 4, 0.22, LV, 2.2, 'l'))
    o.append(T(332, 66, 'sx = 200 ÷ 10 = 20', 13, 'middle', LV, True))
    o.append(T(332, 84, 'sy = 100 ÷ 5 = 20', 13, 'middle', LV, True))
    y = 290
    o.append(T(50, y, 'xv = xvmin + (xw − xwmin) × sx,   yv = yvmin + (yw − ywmin) × sy', 14, 'start', INK, True))
    o.append(T(50, y + 28, '(a) viewport (0, 0) to (200, 100):', 14, 'start', AC, True))
    o.append(T(360, y + 28, '0 + 5 × 20 = 100,  0 + 2.5 × 20 = 50', 14, 'start', AC))
    o.append(T(50, y + 52, '(b) viewport (100, 60) to (300, 160):', 14, 'start', NX, True))
    o.append(T(360, y + 52, '100 + 5 × 20 = 200,  60 + 2.5 × 20 = 110', 14, 'start', NX))
    o.append(T(50, y + 80, 'aspect 10 ÷ 5 = 2 equals 200 ÷ 100 = 2, so sx = sy and nothing stretches', 13, 'start', MUT))
    return y + 96, ''.join(o)
FIG[5] = (f5, 'The window is 10 by 5 world units and each viewport is 200 by 100, so sx = sy = 20. The window centre (5, 2.5) lands on (100, 50) in viewport (a); shifting the viewport to start at (100, 60) moves the same point to (200, 110) with the same scale.',
          'Left, the world window from (0,0) to (10,5) with its centre (5,2.5) marked; right, device axes with viewport (a) from (0,0) to (200,100) and dashed viewport (b) from (100,60) to (300,160), the point at (100,50) and (200,110); an arrow between them labelled sx = sy = 20, and the two mappings worked below.')


# ---- 2.6 line clipping ----
def f6():
    o = []
    s = 38
    fx = lambda v: 80 + (v + 3) * s
    fy = lambda v: 330 - v * s
    xs, ys = list(range(-3, 12)), list(range(0, 9))
    grid(o, fx, fy, xs, ys)
    o.append(R(fx(2), fy(6), 6 * s, 4 * s, ACS, AC, 0, 2.2))
    for x in (2, 8):
        o.append(L(fx(x), fy(0), fx(x), fy(8), AC, 1.2, '6 5'))
    for y in (2, 6):
        o.append(L(fx(-3), fy(y), fx(11), fy(y), AC, 1.2, '6 5'))
    codes = {(0, 2): '1001', (1, 2): '1000', (2, 2): '1010', (0, 1): '0001', (1, 1): '0000', (2, 1): '0010', (0, 0): '0101', (1, 0): '0100', (2, 0): '0110'}
    cxs, cys = (-2.4, 5, 10.0), (0.45, 4, 7.6)
    spot = {(2, 2): (10.5, 6.4), (0, 0): (-2.4, 1.6)}
    for (i, j), cd in codes.items():
        cx_, cy_ = spot.get((i, j), (cxs[i], cys[j]))
        o.append(Tb(fx(cx_), fy(cy_) + 5, cd, 13, 'middle', MUT, True))
    o.append(L(fx(-2), fy(1), fx(10), fy(7), L2, 2, '6 4'))
    o.append(L(fx(2), fy(3), fx(8), fy(6), LV, 4.5))
    for (x, y), c in (((-2, 1), INK), ((10, 7), INK), ((2, 3), LV), ((8, 6), LV)):
        o.append(C(fx(x), fy(y), 6.5, c))
    o.append(Tb(fx(-2) + 10, fy(1) + 22, 'P1 (−2, 1)', 13, 'start', INK, True))
    o.append(Tb(fx(10) - 12, fy(7) - 12, 'P2 (10, 7)', 13, 'end', INK, True))
    o.append(Tb(fx(2) + 12, fy(3) + 18, '(2, 3)  u = 1/3', 13, 'start', LV, True))
    o.append(Tb(fx(8) + 10, fy(6) + 20, '(8, 6)  u = 5/6', 13, 'start', LV, True))
    o.append(T(fx(5), fy(6) + 18, 'window x 2 to 8, y 2 to 6', 13, 'middle', AC, True))
    y = 384
    o.append(T(40, y, 'Cohen–Sutherland: 0101 AND 1010 = 0000, so cut P1 at x = 2 and P2 at y = 6', 14, 'start', INK, True))
    o.append(T(40, y + 24, 'Liang–Barsky: u1 = max(0, 1/3, 1/6) = 1/3,  u2 = min(1, 5/6, 5/6) = 5/6', 14, 'start', LV, True))
    o.append(T(40, y + 46, 'both keep the thick segment (2, 3) to (8, 6)', 13, 'start', MUT))
    return y + 62, ''.join(o)
FIG[6] = (f6, 'The line from P1(−2, 1), code 0101, to P2(10, 7), code 1010, crosses the window x 2 to 8, y 2 to 6. Cutting at x = 2 and y = 6, or at u = 1/3 and u = 5/6, keeps the same thick piece from (2, 3) to (8, 6).',
          'A grid with the shaded window from x 2 to 8 and y 2 to 6, its edges extended as dashed lines with the nine region codes, the dashed line from (−2,1) to (10,7), and its thick visible part from (2,3) to (8,6) marked u = 1/3 and u = 5/6.')


# ---- 2.7 Sutherland-Hodgman, four passes ----
def f7():
    o = []
    s, pw = 27, 176
    passes = [('left: x = 1', 'x', 1, [(0, 0), (4, 0), (4, 4), (0, 4)], [(1, 0), (4, 0), (4, 4), (1, 4)]),
              ('right: x = 3', 'x', 3, [(1, 0), (4, 0), (4, 4), (1, 4)], [(1, 0), (3, 0), (3, 4), (1, 4)]),
              ('bottom: y = 1', 'y', 1, [(1, 0), (3, 0), (3, 4), (1, 4)], [(1, 1), (3, 1), (3, 4), (1, 4)]),
              ('top: y = 3', 'y', 3, [(1, 1), (3, 1), (3, 4), (1, 4)], [(1, 1), (3, 1), (3, 3), (1, 3)])]
    for k, (title, ax, v, pin, pout) in enumerate(passes):
        X0 = 14 + k * pw + 32
        fx = lambda x, X0=X0: X0 + x * s
        fy = lambda y: 56 + (4 - y) * s
        o.append(T(14 + k * pw + pw / 2, 30, f'pass {k + 1}, {title}', 13, 'middle', LV, True))
        grid(o, fx, fy, list(range(0, 5)), list(range(0, 5)), True, k == 0)
        o.append(R(fx(1), fy(3), 2 * s, 2 * s, 'none', MUT, 0, 1.2, '3 3'))
        last = k == 3
        o.append(poly([(fx(x), fy(y)) for x, y in pin], 'none', L2, 1.6, '5 4'))
        o.append(poly([(fx(x), fy(y)) for x, y in pout], NXS if last else ACS, NX if last else AC, 2.2))
        if ax == 'x':
            o.append(L(fx(v), fy(-0.3), fx(v), fy(4.3), LV, 2.6))
        else:
            o.append(L(fx(-0.3), fy(v), fx(4.3), fy(v), LV, 2.6))
        for x, y in pout:
            o.append(C(fx(x), fy(y), 4.5, NX if last else AC))
        c = NX if last else AC
        yl = fy(0) + 44
        o.append(T(14 + k * pw + pw / 2, yl, ', '.join(f'({x},{y})' for x, y in pout[:2]) + ',', 13, 'middle', c, True))
        o.append(T(14 + k * pw + pw / 2, yl + 18, ', '.join(f'({x},{y})' for x, y in pout[2:]), 13, 'middle', c, True))
    yb = fy(0) + 104
    o.append(T(360, yb, 'dashed grey: the list handed in; shaded: the list handed down; thin dashed square: window 1 to 3', 13, 'middle', MUT))
    o.append(T(360, yb + 24, 'input (0,0), (4,0), (4,4), (0,4) → output (1,1), (3,1), (3,3), (1,3)', 14, 'middle', NX, True))
    return yb + 40, ''.join(o)
FIG[7] = (f7, 'The square (0,0), (4,0), (4,4), (0,4) goes through four passes, left x = 1, right x = 3, bottom y = 1 and top y = 3. Each pass trims the list it is handed against one boundary and passes the new list on, ending at (1,1), (3,1), (3,3), (1,3).',
          'Four small grids side by side, one per clipping pass, each with the boundary line drawn bold, the incoming polygon dashed, the outgoing polygon shaded and its vertex list underneath, ending with the square (1,1), (3,1), (3,3), (1,3).')


# ---- 2.8 perspective against parallel projection ----
def f8():
    o = []
    sz, sy = 42, 46
    fz = lambda v: 70 + v * sz
    fy = lambda v: 270 - v * sy
    o.append(L(fz(0), fy(0), fz(13.6), fy(0), L2, 1.6, arrow='m'))
    o.append(L(fz(0), fy(-0.4), fz(0), fy(5), L2, 1.6))
    for v in (0, 3, 6, 12):
        o.append(L(fz(v), fy(0), fz(v), fy(0) + 5, L2, 1.5)); o.append(T(fz(v), fy(0) + 20, str(v), 13, fill=MUT))
    o.append(T(fz(13.6), fy(0) + 20, 'z (depth)', 13, 'end', MUT, True))
    for v in (1, 2, 4):
        o.append(L(fz(0) - 5, fy(v), fz(0), fy(v), L2, 1.5)); o.append(T(fz(0) - 9, fy(v) + 4.5, str(v), 13, 'end', MUT))
    o.append(T(fz(0) - 9, fy(5) + 4, 'y', 13, 'end', MUT, True))
    # projection plane
    o.append(L(fz(3), fy(-0.3), fz(3), fy(4.9), AC, 3))
    o.append(T(fz(3), fy(5) - 2, 'plane z = d = 3', 13, 'middle', AC, True))
    # parallel projection lines
    o.append(L(fz(12), fy(4), fz(3), fy(4), MUT, 1.6, '3 4'))
    o.append(Tb(fz(8.4), fy(4) + 18, 'parallel: y′ = 4 at every depth', 13, 'middle', MUT, True))
    # perspective rays
    o.append(L(fz(0), fy(0), fz(6), fy(4), LV, 2))
    o.append(L(fz(0), fy(0), fz(12), fy(4), NX, 2))
    o.append(C(fz(0), fy(0), 7, INK))
    o.append(T(fz(0) + 4, fy(0) + 40, 'eye at the origin', 13, 'start', INK, True))
    for (z, y), c in (((6, 4), LV), ((12, 4), NX), ((3, 2), LV), ((3, 1), NX), ((3, 4), MUT)):
        o.append(C(fz(z), fy(y), 6.5, c))
    o.append(T(fz(6), fy(4) - 14, 'P (2, 4, 6)', 14, 'middle', LV, True))
    o.append(T(fz(12), fy(4) - 14, 'Q (2, 4, 12)', 14, 'middle', NX, True))
    o.append(Tb(fz(3) - 12, fy(2) - 4, 'P′ y′ = 2', 13, 'end', LV, True))
    o.append(Tb(fz(3) + 12, fy(1) + 20, 'Q′ y′ = 1', 13, 'start', NX, True))
    y = 340
    o.append(T(40, y, 'x′ = x · d / z,   y′ = y · d / z', 14, 'start', INK, True))
    o.append(T(40, y + 26, 'P: 2 × 3 / 6 = 1,   4 × 3 / 6 = 2    →  P′ = (1, 2)', 14, 'start', LV, True))
    o.append(T(40, y + 50, 'Q: 2 × 3 / 12 = 0.5,  4 × 3 / 12 = 1  →  Q′ = (0.5, 1)', 14, 'start', NX, True))
    o.append(T(40, y + 76, 'Q is twice as far as P, so its image is half as far from the centre: size falls as 1/z', 13, 'start', MUT))
    return y + 92, ''.join(o)
FIG[8] = (f8, 'Seen from the side with the plane at d = 3: the ray from the eye to P(2, 4, 6) crosses the plane at y′ = 2, and the ray to Q(2, 4, 12), twice as deep, crosses at y′ = 1. Parallel projection keeps y′ = 4 for both.',
          'A side view with depth z across and height y up: the eye at the origin, the projection plane at z = 3, points P at depth 6 and Q at depth 12 both at height 4, rays from the eye crossing the plane at heights 2 and 1, and a dashed horizontal line showing parallel projection at height 4.')


spec = make_spec(FIG)


def text_fixes(k):
    return {
        1: [('The order in the figure is scale, then rotate, then translate; changing the order changes the final point.',
             'When transforms are combined, a common order is scale, then rotate, then translate; changing the order changes the final point.')],
        3: [(' Only a few universities teach this composition step in detail.', '')],
        4: [('The figure marks the three shift entries and the final 1.',
             'The three shift entries sit in the last column, above the final 1.')],
        7: [(' Only a few universities teach this algorithm in depth.', '')],
    }.get(k, [])
