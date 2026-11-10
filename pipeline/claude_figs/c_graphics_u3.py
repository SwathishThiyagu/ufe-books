"""Claude's hand-drawn figures for c-graphics-u3 (Computer Graphics, unit 3: 3D object representation, curves,
visible surfaces, shading and ray tracing), one per chapter, from each chapter's worked example."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def table(o, x, y, widths, head, rows, rh=22, size=13, hc=AC, colc=None):
    """small table with a shaded header row; colc(i, j) -> colour of body cell"""
    W = sum(widths)
    o.append(R(x, y, W, rh, ACS, hc, 0, 1.4))
    cx = x
    for j, (w, h) in enumerate(zip(widths, head)):
        o.append(T(cx + w / 2, y + rh / 2 + size * 0.36, h, size, fill=hc, bold=True)); cx += w
    for i, r in enumerate(rows):
        yy = y + rh * (i + 1)
        o.append(R(x, yy, W, rh, 'none', LN, 0, 1))
        cx = x
        for j, (w, v) in enumerate(zip(widths, r)):
            c = colc(i, j) if colc else (INK if j == 0 else MUT)
            o.append(T(cx + w / 2, yy + rh / 2 + size * 0.36, v, size, fill=c, bold=(j == 0))); cx += w
    o.append(R(x, y, W, rh * (len(rows) + 1), 'none', L2, 0, 1.4))
    return y + rh * (len(rows) + 1)


def poly(pts, fill, c, w=2.2, dash=None, op=None):
    d = f';stroke-dasharray:{dash}' if dash else ''
    f = f';fill-opacity:{op}' if op is not None else ''
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" style="fill:{fill};stroke:{c};stroke-width:{w}{d}{f};stroke-linejoin:round"/>'


# ---- 3.1 the square pyramid and its three tables ----
def f1():
    o = []
    s, ox, oy = 72, 160, 268
    pt = lambda x, y, z: (ox + s * x + 0.45 * s * y, oy - 0.8 * s * z - 0.3 * s * y)
    V = {1: (1, 1, 0), 2: (-1, 1, 0), 3: (-1, -1, 0), 4: (1, -1, 0), 5: (0, 0, 3)}
    Q = {k: pt(*v) for k, v in V.items()}
    o.append(poly([Q[3], Q[4], Q[5]], ACS, 'none', 0))
    o.append(poly([Q[4], Q[1], Q[5]], LVS, 'none', 0))
    E = {1: (1, 2), 2: (2, 3), 3: (3, 4), 4: (4, 1), 5: (1, 5), 6: (2, 5), 7: (3, 5), 8: (4, 5)}
    hidden = {1, 2, 6}
    for k, (a, b) in E.items():
        o.append(L(*Q[a], *Q[b], L2 if k in hidden else INK, 1.6 if k in hidden else 2.2, '5 4' if k in hidden else None))
    for k, (a, b) in E.items():
        mx, my = (Q[a][0] + Q[b][0]) / 2, (Q[a][1] + Q[b][1]) / 2
        dx, dy = {1: (-40, -6), 2: (-16, 4), 3: (0, 18), 4: (16, 10), 5: (12, 0), 6: (-14, 2), 7: (-16, 0), 8: (12, 4)}[k]
        o.append(Tb(mx + dx, my + dy, f'E{k}', 13, 'middle', MUT if k in hidden else INK, True))
    lab = {1: ('V1 (1, 1, 0)', 10, -6, 'start'), 2: ('V2 (−1, 1, 0)', -6, -12, 'end'), 3: ('V3 (−1, −1, 0)', -4, 22, 'middle'),
           4: ('V4 (1, −1, 0)', 6, 22, 'middle'), 5: ('V5 (0, 0, 3)', 0, -14, 'middle')}
    for k, (t, dx, dy, an) in lab.items():
        o.append(C(*Q[k], 5.5, AC if k < 5 else NX))
        o.append(T(Q[k][0] + dx, Q[k][1] + dy, t, 13, an, NX if k == 5 else AC, True))
    c4 = [(Q[3][0] + Q[4][0] + Q[5][0]) / 3, (Q[3][1] + Q[4][1] + Q[5][1]) / 3]
    c5 = [(Q[4][0] + Q[1][0] + Q[5][0]) / 3, (Q[4][1] + Q[1][1] + Q[5][1]) / 3]
    o.append(T(c4[0] + 28, c4[1] + 46, 'P4', 14, 'middle', AC, True))
    o.append(T(c5[0] + 4, c5[1] + 16, 'P5', 14, 'middle', LV, True))
    o.append(T(ox + 20, oy + 66, 'base P1, back faces P2, P3', 13, 'middle', MUT))
    # tables
    xt = 356
    yb = table(o, xt, 20, [40, 110], ['V', 'x, y, z'], [['V1', '(1, 1, 0)'], ['V2', '(−1, 1, 0)'], ['V3', '(−1, −1, 0)'], ['V4', '(1, −1, 0)'], ['V5', '(0, 0, 3)']])
    table(o, xt, yb + 18, [40, 110], ['P', 'edges'], [['P1', 'E4 E3 E2 E1'], ['P2', 'E1 E6 E5'], ['P3', 'E2 E7 E6'], ['P4', 'E3 E8 E7'], ['P5', 'E4 E5 E8']])
    er = [[f'E{k}', f'V{a} V{b}', f] for (k, (a, b)), f in zip(E.items(), ['P1 P2', 'P1 P3', 'P1 P4', 'P1 P5', 'P2 P5', 'P2 P3', 'P3 P4', 'P4 P5'])]
    table(o, xt + 168, 20, [40, 72, 72], ['E', 'ends', 'faces'], er)
    y = 374
    o.append(T(40, y, 'V − E + F = 5 − 8 + 5 = 2, so the surface is closed', 14, 'start', NX, True))
    o.append(T(40, y + 24, 'face by face: 4 + 4 × 3 = 16 coordinate triples; vertex table: 5, each written once', 13, 'start', MUT))
    return y + 40, ''.join(o)
FIG[1] = (f1, 'The square pyramid stored as three tables: 5 vertices, 8 edges and 5 faces. Each edge names its two ends and the two faces that share it, so E1 belongs to the base P1 and the side P2, and V − E + F = 5 − 8 + 5 = 2.',
          'A wireframe square pyramid with vertices V1 to V5 and their coordinates and edges E1 to E8 labelled, hidden edges dashed, beside a vertex table, a polygon table listing each face\'s edges and an edge table listing each edge\'s two ends and two faces.')


# ---- 3.2 plane through three points ----
def f2():
    o = []
    s, ox, oy = 150, 190, 228
    pt = lambda x, y, z: (ox - 0.6 * s * x + s * y, oy + 0.42 * s * x - s * z)
    for a, lab in (((1.45, 0, 0), 'x'), ((0, 1.45, 0), 'y'), ((0, 0, 1.4), 'z')):
        X, Y = pt(*a)
        o.append(L(ox, oy, X, Y, L2, 1.8, arrow='m'))
        o.append(T(X + (-10 if lab == 'x' else 10 if lab == 'y' else -12), Y + (14 if lab == 'x' else 5), lab, 15, 'middle' if lab == 'x' else 'start' if lab == 'y' else 'end', MUT, True))
    P1, P2, P3 = pt(1, 0, 0), pt(0, 1, 0), pt(0, 0, 1)
    o.append(poly([P1, P2, P3], ACS, AC, 2.4))
    G = pt(1 / 3, 1 / 3, 1 / 3)
    Ntip = pt(1 / 3 + 0.5, 1 / 3 + 0.5, 1 / 3 + 0.5)
    o.append(L(*G, *Ntip, NX, 2.6, arrow='x'))
    o.append(C(*G, 4.5, NX))
    o.append(Tb(Ntip[0] + 10, Ntip[1] - 4, 'n = (1, 1, 1)', 14, 'start', NX, True))
    for (X, Y), t, dx, dy, an in ((P1, 'P1 (1, 0, 0)', -8, 20, 'end'), (P2, 'P2 (0, 1, 0)', 4, 22, 'middle'), (P3, 'P3 (0, 0, 1)', -10, -6, 'end')):
        o.append(C(X, Y, 6, AC)); o.append(T(X + dx, Y + dy, t, 13, an, AC, True))
    o.append(C(ox, oy, 6.5, LV))
    o.append(Tb(ox - 12, oy + 4, 'P4 (0, 0, 0)', 13, 'end', LV, True))
    o.append(Tb(ox - 12, oy + 22, '0 + 0 + 0 − 1 = −1: behind', 13, 'end', LV, True))
    xr = 452
    o.append(T(xr, 40, 'u = P2 − P1 = (−1, 1, 0)', 14, 'start', INK))
    o.append(T(xr, 64, 'v = P3 − P1 = (−1, 0, 1)', 14, 'start', INK))
    o.append(T(xr, 92, 'n = u × v = (1, 1, 1)', 14, 'start', NX, True))
    o.append(T(xr, 116, 'A = B = C = 1', 14, 'start', NX))
    o.append(T(xr, 144, 'D = −(1·1 + 1·0 + 1·0) = −1', 14, 'start', INK))
    o.append(T(xr, 176, 'x + y + z − 1 = 0', 16, 'start', AC, True))
    o.append(T(xr, 208, '|n| = √3 ≈ 1.732, unit normal', 13, 'start', MUT))
    o.append(T(xr, 228, '(0.577, 0.577, 0.577)', 13, 'start', MUT))
    o.append(T(xr, 266, 'test a point: f(x, y, z) = x + y + z − 1', 13, 'start', INK, True))
    o.append(T(xr, 288, 'f > 0 in front, f < 0 behind', 13, 'start', INK))
    o.append(T(xr, 310, 'f(P4) = −1 < 0, so P4 is behind', 13, 'start', LV, True))
    return 356, ''.join(o)
FIG[2] = (f2, 'The face through P1(1,0,0), P2(0,1,0), P3(0,0,1) has normal n = u × v = (1, 1, 1) and plane x + y + z − 1 = 0. Putting the origin P4 into the left side gives −1, a negative value, so P4 lies behind the face.',
          'Three-dimensional axes with the shaded triangle through (1,0,0), (0,1,0) and (0,0,1), its normal arrow (1,1,1) from the centre, and the origin P4 marked behind with value −1; beside it the cross product and the plane equation x + y + z − 1 = 0.')


# ---- 3.3 two blobs and the threshold ----
def f3():
    o = []
    x0, x1, y0, y1 = 70, 650, 30, 270
    fx = lambda v: x0 + (v + 2) / 8 * (x1 - x0)
    fy = lambda v: y1 - v / 1.1 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, list(range(-2, 7)), [0, 0.25, 0.5, 0.75, 1.0], fx, fy, 'x (units)', 'field f(x)', neg, lambda v: f'{v:g}'))
    r = math.sqrt(math.log(2))
    for c in (0, 4):
        o.append(R(fx(c - r), fy(1.06), fx(c + r) - fx(c - r), fy(0) - fy(1.06), ACS, 'none', 0, 0))
    xs = [i / 40 for i in range(-80, 241)]
    o.append(P([(fx(v), fy(math.exp(-v * v))) for v in xs], L2, 1.6, '5 4'))
    o.append(P([(fx(v), fy(math.exp(-(v - 4) ** 2))) for v in xs], L2, 1.6, '5 4'))
    o.append(P([(fx(v), fy(math.exp(-v * v) + math.exp(-(v - 4) ** 2))) for v in xs], AC, 2.6))
    o.append(L(x0, fy(0.5), x1, fy(0.5), LV, 2, '7 4'))
    o.append(Tb(fx(2), fy(0.5) + 5, 'threshold T = 0.5', 13, 'middle', LV, True))
    for c in (0, 4):
        for sgn in (-1, 1):
            o.append(C(fx(c + sgn * r), fy(0.5), 5, LV))
    o.append(Tb(fx(0) + 4, fy(0.5) + 26, '−0.833 to 0.833', 13, 'middle', AC, True))
    o.append(Tb(fx(4), fy(0.5) + 26, '3.167 to 4.833', 13, 'middle', AC, True))
    o.append(C(fx(2), fy(0.0366), 6, NX))
    o.append(L(fx(2), fy(0.0366) - 8, fx(2), fy(0.27), NX, 1.4))
    o.append(Tb(fx(2), fy(0.31), 'midpoint: 2 × e<tspan dy="-5" font-size="11">−4</tspan><tspan dy="5"> = 0.037</tspan>', 13, 'middle', NX, True))
    o.append(T(fx(0), fy(1.0) - 8, 'blob at 0', 13, 'middle', AC, True))
    o.append(T(fx(4), fy(1.0) - 8, 'blob at 4', 13, 'middle', AC, True))
    o.append(T(x1, y0 - 12, 'e<tspan dy="-5" font-size="11">−r²</tspan><tspan dy="5"> = 0.5 gives r = 0.833</tspan>', 13, 'end', MUT, True))
    y = 340
    o.append(T(40, y, '(a) sphere, centre (2, 3, 1), radius 5:  x² + y² + z² − 4x − 6y − 2z − 11 = 0', 13, 'start', INK, True))
    return y + 16, ''.join(o)
FIG[3] = (f3, 'Along the line through the two blob centres, each blob alone crosses T = 0.5 at 0.833 units from its centre, the shaded bands. Halfway, at x = 2, the summed field is only 2 × e⁻⁴ = 0.037, far below 0.5, so the two blobs stay apart.',
          'A graph of field against x from −2 to 6: two dashed bell curves centred at 0 and 4, their solid sum, a dashed threshold line at 0.5 crossing each bell at 0.833 units from its centre, and the midpoint value 0.037 marked at x = 2.')


# ---- 3.4 de Casteljau at t = 0.5 ----
def f4():
    o = []
    s, X0, Y0 = 118, 60, 300
    fx = lambda v: X0 + v * s
    fy = lambda v: Y0 - v * s
    o.append(axes(X0, fx(4.2), fy(2.3), Y0, [0, 1, 2, 3, 4], [0, 0.5, 1, 1.5, 2], fx, fy, 'x', 'y', str, lambda v: f'{v:g}'))
    Pp = [(0, 0), (1, 2), (3, 2), (4, 0)]
    Qp = [(0.5, 1), (2, 2), (3.5, 1)]
    Rp = [(1.25, 1.5), (2.75, 1.5)]
    S0 = (2, 1.5)
    bez = lambda t: tuple((1 - t) ** 3 * Pp[0][i] + 3 * t * (1 - t) ** 2 * Pp[1][i] + 3 * t * t * (1 - t) * Pp[2][i] + t ** 3 * Pp[3][i] for i in range(2))
    o.append(P([(fx(x), fy(y)) for x, y in Pp], L2, 1.8, '6 4'))
    o.append(P([(fx(x), fy(y)) for x, y in Qp], LV, 1.8))
    o.append(P([(fx(x), fy(y)) for x, y in Rp], NX, 1.8))
    o.append(P([(fx(bez(i / 60)[0]), fy(bez(i / 60)[1])) for i in range(61)], AC, 3))
    for k, (x, y) in enumerate(Pp):
        o.append(C(fx(x), fy(y), 6, INK))
    o.append(T(fx(0) + 10, fy(0) - 10, 'P0', 13, 'start', INK, True))
    o.append(T(fx(1) - 8, fy(2) - 10, 'P1 (1, 2)', 13, 'end', INK, True))
    o.append(T(fx(3) + 8, fy(2) - 10, 'P2 (3, 2)', 13, 'start', INK, True))
    o.append(T(fx(4) - 10, fy(0) - 10, 'P3', 13, 'end', INK, True))
    for (x, y), n, dx, an in zip(Qp, ['Q0', 'Q1', 'Q2'], [-10, 0, 10], ['end', 'middle', 'start']):
        o.append(C(fx(x), fy(y), 5.5, LV)); o.append(T(fx(x) + dx, fy(y) + (-12 if n == 'Q1' else 5), n, 13, an, LV, True))
    for (x, y), n, an, dx in zip(Rp, ['R0', 'R1'], ['end', 'start'], [-10, 10]):
        o.append(C(fx(x), fy(y), 5.5, NX)); o.append(T(fx(x) + dx, fy(y) + 5, n, 13, an, NX, True))
    o.append(C(fx(2), fy(1.5), 7.5, AC))
    o.append(Tb(fx(2), fy(1.5) + 26, 'S0 (2, 1.5)', 14, 'middle', AC, True))
    xr = 600
    lines = [('t = 0.5: halve', INK, True), ('each pair', INK, True), ('', INK, False), ('Q0 = (0.5, 1)', LV, True), ('Q1 = (2, 2)', LV, True), ('Q2 = (3.5, 1)', LV, True), ('', INK, False),
             ('R0 = (1.25, 1.5)', NX, True), ('R1 = (2.75, 1.5)', NX, True), ('', INK, False), ('S0 = (2, 1.5)', AC, True), ('on the curve', AC, False)]
    for i, (t, c, b) in enumerate(lines):
        if t: o.append(T(xr, 40 + i * 20, t, 13, 'start', c, b))
    y = 372
    o.append(T(40, y, 'Bernstein check: (P0 + 3P1 + 3P2 + P3) ÷ 8 = (16, 12) ÷ 8 = (2, 1.5)', 14, 'start', INK, True))
    o.append(T(40, y + 24, 'end tangents run along the first and last legs: B′(0) = 3(P1 − P0) = (3, 6),  B′(1) = 3(P3 − P2) = (3, −6)', 13, 'start', MUT))
    return y + 40, ''.join(o)
FIG[4] = (f4, 'De Casteljau at t = 0.5: halving the legs of P0 (0,0), P1 (1,2), P2 (3,2), P3 (4,0) gives Q0, Q1, Q2, then R0 and R1, then S0 = (2, 1.5), which is on the curve. The Bernstein sum (P0 + 3P1 + 3P2 + P3) ÷ 8 lands on the same point.',
          'A cubic Bézier curve with its dashed control polygon P0 (0,0), P1 (1,2), P2 (3,2), P3 (4,0), the first-level midpoints Q0, Q1, Q2 joined, the second-level R0 and R1 joined, and the final point S0 (2, 1.5) on the curve.')


# ---- 3.5 the knot vector ----
def f5():
    o = []
    U = [0, 0, 0, 0, 1, 2, 2, 2, 2]
    bw, X0, y = 64, 72, 54
    for i, u in enumerate(U):
        c, f = (AC, ACS) if u == 0 else (LV, LVS) if u == 1 else (NX, NXS)
        o.append(R(X0 + i * bw, y, bw, 44, f, c, 0, 1.8))
        o.append(T(X0 + i * bw + bw / 2, y + 28, str(u), 17, fill=c, bold=True))
        o.append(T(X0 + i * bw + bw / 2, y - 10, f'u<tspan dy="4" font-size="11">{i}</tspan>', 14, fill=MUT))
    o.append(T(X0 - 12, y + 28, 'U =', 15, 'end', INK, True))
    o.append(brace(X0 + 4, X0 + 4 * bw - 4, y + 54, AC))
    o.append(T(X0 + 2 * bw, y + 80, '0 four times = p + 1', 13, 'middle', AC, True))
    o.append(T(X0 + 2 * bw, y + 98, 'clamped: starts at P₀', 13, 'middle', AC))
    o.append(brace(X0 + 4 * bw + 4, X0 + 5 * bw - 4, y + 54, LV))
    o.append(T(X0 + 4.5 * bw, y + 80, '1 once', 13, 'middle', LV, True))
    o.append(T(X0 + 4.5 * bw, y + 98, 'C<tspan dy="-5" font-size="11">3−1</tspan><tspan dy="5"> = C²</tspan>', 13, 'middle', LV))
    o.append(brace(X0 + 5 * bw + 4, X0 + 9 * bw - 4, y + 54, NX))
    o.append(T(X0 + 7 * bw, y + 80, '2 four times = p + 1', 13, 'middle', NX, True))
    o.append(T(X0 + 7 * bw, y + 98, 'clamped: ends at P₄', 13, 'middle', NX))
    # counting rule
    yc = y + 140
    o.append(T(60, yc, 'p = 3, 9 knots so m = 8:   m = n + p + 1  →  8 = n + 4  →  n = 4', 14, 'start', INK, True))
    o.append(T(60, yc + 26, 'n + 1 = 5 control points:', 14, 'start', INK, True))
    for k in range(5):
        o.append(boxt(270 + k * 74, yc + 8, 60, 30, [f'P<tspan dy="4" font-size="11">{k}</tspan>'], PANEL, INK, 15, bold_first=True))
    # parameter line with stacked knots
    yl = yc + 104
    fu = lambda u: 150 + u * 200
    o.append(L(fu(0), yl, fu(2), yl, INK, 2.4))
    o.append(T(fu(1) - 100, yl + 22, 'span 1: [0, 1)', 13, 'middle', MUT))
    o.append(T(fu(1) + 100, yl + 22, 'span 2: [1, 2]', 13, 'middle', MUT))
    for u, m, c in ((0, 4, AC), (1, 1, LV), (2, 4, NX)):
        for j in range(m):
            o.append(C(fu(u), yl - j * 13, 5.5, c))
        o.append(T(fu(u), yl + 42, f'u = {u}', 13, 'middle', c, True))
    o.append(T(fu(1), yl - 30, 'stacked dots = multiplicity', 13, 'middle', MUT))
    return yl + 56, ''.join(o)
FIG[5] = (f5, 'The nine knots of U = (0,0,0,0,1,2,2,2,2) for p = 3. The four 0s and four 2s clamp the curve to P₀ and P₄, the single 1 is an interior join with C² continuity, and 9 knots = 5 + 3 + 1 gives five control points, P₀ to P₄.',
          'A row of nine knot boxes u0 to u8 holding 0, 0, 0, 0, 1, 2, 2, 2, 2, bracketed as clamped start, single interior knot with C² continuity and clamped end; below, the counting rule giving 5 control points P0 to P4 and a parameter line with 4, 1 and 4 stacked dots at u = 0, 1 and 2.')


# ---- 3.6 the depth buffer at one pixel, and a BSP order ----
def f6():
    o = []
    # depth axis
    x0, x1, y = 90, 420, 60
    fz = lambda v: x0 + v * (x1 - x0)
    o.append(L(x0, y, x1, y, L2, 2))
    for v in (0, 0.2, 0.4, 0.6, 0.8, 1.0):
        o.append(L(fz(v), y, fz(v), y + 5, L2, 1.5)); o.append(T(fz(v), y + 21, f'{v:.1f}', 13, fill=MUT))
    o.append(T(x0, y - 14, 'near (eye)', 13, 'middle', MUT, True))
    for v, n, c in ((1.0, 'start (far)', MUT), (0.6, 'A', AC), (0.4, 'B', NX)):
        o.append(C(fz(v), y, 7, c)); o.append(T(fz(v), y - 14, n, 13, 'middle', c, True))
    o.append(T(450, y + 4, 'depth at pixel (5, 5)', 13, 'start', INK, True))
    table(o, 90, y + 46, [150, 170, 130, 110], ['event', 'test', 'colour', 'depth'],
          [['start', '—', 'background', '1.0'], ['A arrives, z = 0.6', '0.6 < 1.0: pass', 'A', '0.6'], ['B arrives, z = 0.4', '0.4 < 0.6: pass', 'B', '0.4']],
          24, 13, INK, lambda i, j: [INK, AC, NX][i] if j else INK)
    o.append(T(90, y + 166, 'final pixel: B\'s colour, depth 0.4, because smaller z is nearer', 14, 'start', NX, True))
    # BSP
    yb = 300
    o.append(T(40, yb - 28, 'BSP, eye at x = 10', 14, 'start', INK, True))
    gx = lambda v: 50 + v * 36
    o.append(L(gx(-0.6), yb + 60, gx(10.8), yb + 60, L2, 1.6, arrow='m'))
    for v in (0, 2, 5, 10):
        o.append(T(gx(v), yb + 80, str(v), 13, fill=MUT))
    o.append(T(gx(10.8), yb + 80, 'x', 13, 'end', MUT, True))
    for v, n, c in ((0, 'P3', MUT), (2, 'P1', AC), (5, 'P2', NX)):
        o.append(L(gx(v), yb - 6, gx(v), yb + 60, c, 4))
        o.append(T(gx(v), yb - 14, n, 13, 'middle', c, True))
    o.append(C(gx(10), yb + 30, 7, INK)); o.append(T(gx(10), yb + 12, 'eye', 13, 'middle', INK, True))
    o.append(T(gx(1), yb + 104, '← back of P1', 13, 'middle', MUT)); o.append(T(gx(6), yb + 104, 'front of P1 →', 13, 'middle', MUT))
    # tree
    tx, ty = 560, yb - 10
    o.append(L(tx, ty + 14, tx - 70, ty + 66, L2, 1.8)); o.append(L(tx, ty + 14, tx + 70, ty + 66, L2, 1.8))
    o.append(boxt(tx - 32, ty - 10, 64, 30, ['P1'], ACS, AC, 14, True))
    o.append(boxt(tx - 102, ty + 64, 64, 30, ['P3'], PANEL, MUT, 14, True))
    o.append(boxt(tx + 38, ty + 64, 64, 30, ['P2'], NXS, NX, 14, True))
    o.append(T(tx - 100, ty + 40, 'back', 13, 'end', MUT)); o.append(T(tx + 100, ty + 40, 'front', 13, 'start', MUT))
    o.append(T(tx, ty + 124, 'eye is in front of P1:', 13, 'middle', INK))
    o.append(T(tx, ty + 144, 'draw back, root, front', 13, 'middle', INK))
    o.append(T(tx, ty + 168, 'P3, P1, P2', 15, 'middle', NX, True))
    return ty + 186, ''.join(o)
FIG[6] = (f6, 'At pixel (5, 5) the depth starts at 1.0. A at 0.6 passes and is written, then B at 0.4 passes and overwrites it, so the pixel ends with B\'s colour and depth 0.4. With P1 at x = 2 as the BSP root and the eye at x = 10 in front, the drawing order is P3, P1, P2.',
          'Top: a depth axis from 0 near to 1 far with the start value 1.0, A at 0.6 and B at 0.4, above a three-row trace table of the depth tests. Bottom: planes P3, P1 and P2 at x = 0, 2 and 5 with the eye at x = 10, and the BSP tree with root P1, back child P3 and front child P2, drawn in the order P3, P1, P2.')


# ---- 3.7 Phong intensity and Gouraud interpolation ----
def f7():
    o = []
    ox, oy, s = 120, 204, 150
    # surface (tangent line) and vectors in the y-z plane
    o.append(L(ox - 0.8 * s * 0.6, oy - 0.6 * s * 0.6, ox + 0.8 * s * 0.6, oy + 0.6 * s * 0.6, L2, 2.4))
    o.append(T(ox + 0.8 * s * 0.6 + 6, oy + 0.6 * s * 0.6 + 5, 'surface', 13, 'start', MUT))
    nx, ny = ox + 0.6 * s, oy - 0.8 * s
    o.append(L(ox, oy, nx, ny, AC, 2.6, arrow='n'))
    o.append(L(ox, oy, ox, oy - s, LV, 2.6, arrow='l'))
    o.append(T(nx + 8, ny + 2, 'N = (0, 0.6, 0.8)', 13, 'start', AC, True))
    o.append(T(ox - 8, oy - s + 6, 'L = (0, 0, 1)', 13, 'end', LV, True))
    a1, a2 = -90, -90 + math.degrees(math.atan2(0.6, 0.8))
    r = 50
    o.append(f'<path d="M{ox + r * math.cos(math.radians(a1)):.1f},{oy + r * math.sin(math.radians(a1)):.1f} A{r},{r} 0 0 1 {ox + r * math.cos(math.radians(a2)):.1f},{oy + r * math.sin(math.radians(a2)):.1f}" style="fill:none;stroke:var(--ink);stroke-width:1.6"/>')
    o.append(T(ox - 10, oy - 66, 'N·L = 0.8', 13, 'end', INK, True))
    o.append(C(ox, oy, 5, INK))
    # stacked bar
    bx, by, bwid = 340, 70, 340
    parts = [(0.2, 'ambient 0.2', PANEL, INK), (0.56, 'diffuse 0.7 × 1.0 × 0.8 = 0.56', ACS, AC), (0.054, 'specular', LVS, LV)]
    o.append(T(bx, by - 26, 'Phong intensity at the point', 14, 'start', INK, True))
    cx = bx
    for v, t, f, c in parts:
        o.append(R(cx, by, v * bwid, 40, f, c, 0, 1.8)); cx += v * bwid
    o.append(R(bx, by, bwid, 40, 'none', L2, 0, 1.2, '4 4'))
    o.append(xaxis(bx, bx + bwid, by + 40, [0, 0.2, 0.4, 0.6, 0.8, 1.0], lambda v: bx + v * bwid, None, lambda v: f'{v:g}'))
    o.append(T(bx + 0.1 * bwid, by + 25, '0.2', 13, 'middle', INK, True))
    o.append(T(bx + 0.48 * bwid, by + 25, '0.56', 13, 'middle', AC, True))
    o.append(L(bx + 0.787 * bwid, by - 4, bx + 0.787 * bwid, by - 14, LV, 1.4))
    o.append(T(bx + 0.787 * bwid, by - 18, '0.054', 13, 'middle', LV, True))
    o.append(T(bx, by + 92, 'ambient  k<tspan dy="4" font-size="11">a</tspan><tspan dy="-4">I</tspan><tspan dy="4" font-size="11">a</tspan><tspan dy="-4"> = 0.2</tspan>', 13, 'start', INK))
    o.append(T(bx, by + 114, 'diffuse  0.7 × 1.0 × 0.8 = 0.56', 13, 'start', AC))
    o.append(T(bx, by + 136, 'specular  0.5 × 0.8<tspan dy="-5" font-size="11">10</tspan><tspan dy="5"> = 0.5 × 0.1074 = 0.054</tspan>', 13, 'start', LV))
    o.append(T(bx, by + 164, 'I = 0.2 + 0.56 + 0.054 = 0.814', 15, 'start', NX, True))
    # Gouraud edge
    gy = 330
    g0, g1 = 140, 620
    o.append(T(40, gy - 34, 'Gouraud: interpolate the vertex intensities along the edge', 14, 'start', INK, True))
    o.append(L(g0, gy, g1, gy, INK, 2.4))
    for f in (0, 0.25, 0.5, 0.75, 1.0):
        o.append(L(g0 + f * (g1 - g0), gy - 5, g0 + f * (g1 - g0), gy + 5, L2, 1.5))
    o.append(C(g0, gy, 7, INK)); o.append(C(g1, gy, 7, INK))
    o.append(T(g0, gy + 26, '0.2', 14, 'middle', INK, True)); o.append(T(g1, gy + 26, '0.6', 14, 'middle', INK, True))
    q = g0 + 0.25 * (g1 - g0)
    o.append(C(q, gy, 7, NX))
    o.append(T(q, gy + 26, '0.30', 14, 'middle', NX, True))
    o.append(T(q, gy - 14, 'quarter point', 13, 'middle', NX))
    o.append(T(380, gy + 26, '0.2 + 0.25 × (0.6 − 0.2) = 0.30', 13, 'middle', MUT))
    return gy + 44, ''.join(o)
FIG[7] = (f7, 'With N·L = 0.8, the Phong sum at the point is ambient 0.2 + diffuse 0.56 + specular 0.054 = 0.814. Gouraud instead lights only the vertices and blends along the edge, giving 0.2 + 0.25 × 0.4 = 0.30 at the quarter point.',
          'Left, the normal N = (0, 0.6, 0.8) and the light direction L = (0, 0, 1) at a point on a surface with N·L = 0.8. Right, a bar from 0 to 1 split into ambient 0.2, diffuse 0.56 and specular 0.054, totalling 0.814. Below, an edge from intensity 0.2 to 0.6 with the quarter point at 0.30.')


# ---- 3.8 one eye ray against the sphere ----
def f8():
    o = []
    fz = lambda z: 70 + (-z) * 84
    ay = 170
    o.append(L(fz(0.4), ay, fz(-7.4), ay, L2, 1.4))
    for z in (0, -2, -4, -5, -6):
        o.append(L(fz(z), ay + 72, fz(z), ay + 77, L2, 1.4)); o.append(T(fz(z), ay + 94, neg(z), 13, fill=MUT))
    o.append(L(fz(0.4), ay + 72, fz(-7.2), ay + 72, L2, 1.4))
    o.append(T(fz(-7.2), ay + 94, 'z', 13, 'end', MUT, True))
    o.append(f'<circle cx="{fz(-5):.1f}" cy="{ay}" r="84" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2.4"/>')
    o.append(C(fz(-5), ay, 4, AC)); o.append(T(fz(-5), ay + 50, 'C (0, 0, −5), r = 1', 13, 'middle', AC, True))
    o.append(L(fz(0), ay, fz(-4) - 9, ay, INK, 2.6, arrow='m'))
    o.append(L(fz(-4), ay, fz(-6), ay, INK, 1.6, '5 4'))
    o.append(C(fz(0), ay, 7, INK)); o.append(T(fz(0), ay - 16, 'eye E', 13, 'middle', INK, True))
    o.append(T(fz(-2), ay - 10, 'd = (0, 0, −1)', 13, 'middle', INK))
    o.append(C(fz(-4), ay, 7, NX)); o.append(f'<circle cx="{fz(-6):.1f}" cy="{ay}" r="6" style="fill:var(--fig);stroke:var(--line2);stroke-width:2"/>')
    o.append(Tb(fz(-4) - 10, ay + 26, 't = 4, hit (0, 0, −4)', 13, 'end', NX, True))
    o.append(Tb(fz(-6) + 10, ay + 52, 't = 6, far side', 13, 'start', MUT, True))
    # secondary rays from the hit
    hx = fz(-4)
    o.append(L(hx, ay - 8, hx - 90, ay - 120, LV, 2, '6 4', 'l'))
    o.append(T(hx - 96, ay - 126, 'shadow ray to the light', 13, 'end', LV, True))
    o.append(L(hx - 6, ay - 6, fz(-1.4), ay - 36, AC, 2, None, 'n'))
    o.append(T(fz(-1.4) - 6, ay - 40, 'reflected × k<tspan dy="4" font-size="11">r</tspan><tspan dy="-4">, depth − 1</tspan>', 13, 'end', AC, True))
    o.append(L(hx + 8, ay - 4, fz(-5.3), ay - 40, NX, 2, '3 3', 'x'))
    o.append(T(fz(-5), ay - 98, 'refracted × k<tspan dy="4" font-size="11">t</tspan><tspan dy="-4"> (glass only)</tspan>', 13, 'middle', NX, True))
    y = ay + 130
    o.append(T(40, y, 'P = E + t d = (0, 0, −t):   (−t + 5)² = 1   →   t² − 10t + 24 = 0   →   (t − 4)(t − 6) = 0', 14, 'start', INK, True))
    o.append(T(40, y + 24, 'keep the smaller positive root, t = 4', 14, 'start', NX, True))
    o.append(T(40, y + 50, 'primary tests: 800 × 600 = 480,000 pixels × 3 objects = 1,440,000', 13, 'start', MUT))
    return y + 66, ''.join(o)
FIG[8] = (f8, 'The eye ray from the origin along (0, 0, −1) meets the sphere of radius 1 at C (0, 0, −5) twice: t = 4 on the near side and t = 6 on the far side. Only the near hit (0, 0, −4) is kept, and from it the shadow, reflected and refracted rays are traced.',
          'A side view along the z axis: the eye at z = 0, a ray to the sphere centred at z = −5 with radius 1, the near hit at t = 4 and the far hit at t = 6 marked, and from the near hit a dashed shadow ray up to the light, a reflected ray back toward the eye and a dotted refracted ray into the sphere.')


spec = make_spec(FIG)
