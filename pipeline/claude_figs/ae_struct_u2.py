"""Claude's hand-drawn figures for ae-struct-u2 (Aircraft Structures: energy methods and indeterminate structures), one per chapter,
drawn from each chapter's own worked example; every plotted value is computed here. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


def arrow(x1, y1, x2, y2, c=AC, w=2, k='n', dash=None):
    return L(x1, y1, x2, y2, c, w, dash, arrow=k)


def pin(x, y, c=INK):
    return P([(x, y + 2), (x - 10, y + 18), (x + 10, y + 18), (x, y + 2)], c, 2) + L(x - 15, y + 18, x + 15, y + 18, c, 2)


def roller(x, y, c=INK):
    return P([(x, y + 2), (x - 10, y + 16), (x + 10, y + 16), (x, y + 2)], c, 2) + C(x - 5, y + 20, 3, c) + C(x + 5, y + 20, 3, c)


def wall(x, y0, y1, c=INK, left=True):
    o = [L(x, y0, x, y1, c, 3)]
    d = -10 if left else 10
    y = y0 + 4
    while y < y1:
        o.append(L(x, y, x + d, y + 8, MUT, 1.5)); y += 10
    return ''.join(o)


def udl(x0, x1, y, h=22, c=LV, n=None, lab=None):
    n = n or max(3, int((x1 - x0) / 36))
    o = [L(x0, y - h, x1, y - h, c, 2)]
    for i in range(n + 1):
        x = x0 + (x1 - x0) * i / n
        o.append(arrow(x, y - h, x, y - 4, c, 1.8, 'l'))
    if lab: o.append(T((x0 + x1) / 2, y - h - 8, lab, 13, 'middle', c, True))
    return ''.join(o)


# ---- 1 strain energy: the triangle and the three modes ----
def f1():
    o = []
    X0, X1, Y0, Y1 = 70, 330, 50, 270
    fx = lin(0, 3, X0, X1); fy = lin(0, 25, Y1, Y0)
    o.append(axes(X0, X1, Y0, Y1, [0, 1, 2, 3], [0, 10, 20], fx, fy, 'extension Δ (mm)', 'load P (kN)'))
    d = 1.371
    o.append(P([(fx(0), fy(0)), (fx(d), fy(20)), (fx(d), fy(0))], AC, 0, fill=ACS))
    o.append(P([(fx(0), fy(0)), (fx(d), fy(20))], AC, 2.5))
    o.append(P([(fx(0), fy(20)), (fx(2 * d), fy(20)), (fx(2 * d), fy(0))], LV, 1.8, dash='6 4'))
    o.append(C(fx(d), fy(20), 4, AC))
    o.append(T(fx(d) - 4, fy(20) - 10, '(1.371 mm, 20 kN)', 13, 'end', AC, True))
    o.append(T(fx(d * 0.62), fy(5), 'U = ½PΔ', 13, 'middle', AC, True))
    o.append(T(fx(d * 0.62), fy(5) + 17, '= 13.71 J', 13, 'middle', AC, True))
    o.append(T(fx(2 * d) - 4, fy(20) - 10, 'sudden 20 kN', 13, 'end', LV))
    o.append(T(fx(2 * d) + 6, fy(10), '2Δ, 4U', 13, 'start', LV, True))
    # right: three modes
    xr = 380
    o.append(T(xr, 30, 'Three loading modes', 14, 'start', INK, True))
    # axial
    y = 80
    o.append(R(xr + 10, y - 9, 120, 18, ACS, AC, 2)); o.append(arrow(xr + 130, y, xr + 170, y, LV, 2.5, 'l')); o.append(arrow(xr + 10, y, xr - 26, y, LV, 2.5, 'l'))
    o.append(T(xr + 186, y - 6, 'P²L/(2AE)', 13, 'start', INK, True)); o.append(T(xr + 186, y + 13, 'strut: 13.71 J', 13, 'start', MUT))
    # bending
    y = 160
    o.append(wall(xr + 10, y - 22, y + 22)); o.append(R(xr + 10, y - 7, 140, 14, ACS, AC, 2)); o.append(arrow(xr + 145, y - 38, xr + 145, y - 9, LV, 2.5, 'l'))
    o.append(T(xr + 186, y - 6, '∫M²dx/(2EI)', 13, 'start', INK, True)); o.append(T(xr + 186, y + 13, 'cantilever: 0.83 J', 13, 'start', MUT))
    # torsion
    y = 240
    o.append(wall(xr + 10, y - 22, y + 22)); o.append(R(xr + 10, y - 9, 140, 18, ACS, AC, 9))
    o.append(arc(xr + 150, y - 22, xr + 150, y + 22, 0.9, LV, 2.2, 'l'))
    o.append(T(xr + 186, y - 6, 'T²L/(2GJ)', 13, 'start', INK, True)); o.append(T(xr + 186, y + 13, 'control rod: 7.37 J', 13, 'start', MUT))
    return 330, ''.join(o)


FIG[1] = (f1, 'Left: the aluminium strut of worked example 1 stretches 1.371 mm under 20 kN; the shaded triangle under the straight load line is the stored energy, 13.71 J. The same load applied suddenly (dashed) gives twice the extension and four times the energy. Right: the three closed forms with the values from this chapter.',
          'Load against extension: a straight line from the origin to 20 kilonewtons at 1.371 millimetres, with the triangle under it shaded and labelled U equals half P delta equals 13.71 joules; a dashed rectangle at 20 kilonewtons out to 2.742 millimetres for a sudden load, labelled 2 delta, 4 U. On the right, three sketches: a bar pulled at both ends labelled P squared L over 2 A E, strut 13.71 joules; a cantilever with a tip load labelled integral M squared over 2 E I, cantilever 0.83 joules; a shaft with a torque arrow labelled T squared L over 2 G J, control rod 7.37 joules.')


# ---- 2 Castigliano: U(P) and its slope ----
def f2():
    o = []
    X0, X1, Y0, Y1 = 80, 640, 40, 300
    fx = lin(0, 30, X0, X1); fy = lin(0, 32, Y1, Y0)
    o.append(axes(X0, X1, Y0, Y1, [0, 5, 10, 15, 20, 25, 30], [0, 8, 16, 24, 32], fx, fy, 'axial load P (kN)', 'strain energy U (J)'))
    c = 0.0342857
    o.append(P([(fx(p), fy(c * p * p)) for p in [i * 0.5 for i in range(61)]], AC, 2.5))
    s = 2 * c * 20
    o.append(L(fx(9), fy(13.714 - s * 11), fx(28), fy(13.714 + s * 8), LV, 2, dash='7 4'))
    o.append(P([(fx(20), fy(13.714)), (fx(25), fy(13.714)), (fx(25), fy(13.714 + 5 * s))], NX, 1.8))
    o.append(T(fx(22.5), fy(13.714) + 18, '5 kN', 13, 'middle', NX, True))
    o.append(T(fx(25) + 8, fy(13.714 + 2.5 * s) + 4, '6.86 J', 13, 'start', NX, True))
    o.append(C(fx(20), fy(13.714), 5, AC))
    o.append(T(fx(20) - 10, fy(13.714) - 12, '20 kN, 13.71 J', 13, 'end', AC, True))
    o.append(Tb(fx(11), fy(24), 'slope = 6.86 J ÷ 5 kN = 1.371 J/kN', 13, 'middle', LV, True))
    o.append(Tb(fx(11), fy(24) + 20, '= 1.371 mm, the extension', 13, 'middle', LV, True))
    o.append(T(fx(26), fy(29), 'U = P²L/(2AE)', 13, 'end', AC, True))
    return 360, ''.join(o)


FIG[2] = (f2, 'Strain energy of the 1.2 m aluminium strut (A = 250 mm², E = 70 GPa) rises as P². The tangent at 20 kN climbs 6.86 J over 5 kN, a slope of 1.371 J/kN, which is the 1.371 mm extension: Castigliano’s Δ = ∂U/∂P.',
          'A parabola of strain energy against load from 0 to 30 kilonewtons, passing 13.71 joules at 20 kilonewtons. A dashed tangent touches it there; a small triangle under the tangent shows a run of 5 kilonewtons and a rise of 6.86 joules, and a label says the slope, 1.371 joules per kilonewton, equals the 1.371 millimetre extension.')


# ---- 3 unit load method on the two-bar truss ----
def f3():
    o = []
    s = 80
    def truss(ox, oy, lab, load, force, col):
        A = (ox, oy); B = (ox + 2 * s, oy); Cc = (ox + s, oy - 1.5 * s)
        out = [L(A[0], A[1], Cc[0], Cc[1], AC, 4), L(B[0], B[1], Cc[0], Cc[1], AC, 4), pin(A[0], A[1]), pin(B[0], B[1])]
        out += [C(Cc[0], Cc[1], 5, INK), T(A[0] - 14, A[1] + 4, 'A', 13, 'end', INK, True), T(B[0] + 14, B[1] + 4, 'B', 13, 'start', INK, True), T(Cc[0] + 12, Cc[1] - 6, 'C', 13, 'start', INK, True)]
        out.append(arrow(Cc[0], Cc[1] - 46, Cc[0], Cc[1] - 8, col, 2.5, 'l' if col == LV else 'x'))
        out.append(T(Cc[0], Cc[1] - 52, load, 13, 'middle', col, True))
        out.append(Tb(ox + s * 0.32, oy - 0.75 * s, force, 13, 'end', col, True))
        out.append(Tb(ox + s * 1.68, oy - 0.75 * s, force, 13, 'start', col, True))
        out.append(T(ox + s, oy + 44, lab, 14, 'middle', INK, True))
        return ''.join(out)
    o.append(truss(90, 200, 'Real loads: forces N', '10 kN', '−6009 N', LV))
    o.append(truss(450, 200, 'Unit load: forces n', '1', '−0.6009', NX))
    o.append(T(360, 60, 'L = 1.8028 m', 13, 'middle', MUT)); o.append(T(360, 78, 'AE = 1.4 × 10⁷ N', 13, 'middle', MUT))
    o.append(T(90 + s, 222, '2 m', 13, 'middle', MUT)); o.append(T(450 + s, 222, '2 m', 13, 'middle', MUT))
    o.append(R(80, 266, 560, 58, PANEL, AC, 8))
    o.append(T(360, 290, 'each bar: nNL/(AE) = (−0.6009)(−6009)(1.8028)/(1.4 × 10⁷) = 4.65 × 10⁻⁴ m', 13, 'middle', INK))
    o.append(T(360, 311, 'Δ_C = 2 × 4.65 × 10⁻⁴ m = 0.93 mm downward', 14, 'middle', AC, True))
    return 334, ''.join(o)


FIG[3] = (f3, 'Worked example 1 as two load cases on one truss. The real 10 kN puts 6009 N of compression in each bar; a unit load at the same joint puts 0.6009 in each. Multiplying, times L over AE, and adding the two bars gives the 0.93 mm drop of C.',
          'Two copies of a two-bar truss with pins A and B 2 metres apart and apex C 1.5 metres up. Left copy: 10 kilonewtons down at C, each bar labelled minus 6009 newtons. Right copy: a load of 1 down at C, each bar labelled minus 0.6009. A box below gives each bar n N L over A E equals 4.65 times ten to the minus 4 metres and the total deflection of C, 0.93 millimetres downward.')


# ---- 4 trusses: determinate triangle and the redundant three-bar ----
def f4():
    o = []
    s = 62
    A = (50, 230); B = (50 + 4 * s, 230); Cc = (50 + 2 * s, 230 - 2 * s)
    o += [L(*A, *B, AC, 4), L(*A, *Cc, LV, 4), L(*B, *Cc, LV, 4), pin(*A), roller(*B), C(*Cc, 5, INK)]
    o += [T(A[0] - 6, A[1] - 10, 'A', 13, 'end', INK, True), T(B[0] + 8, B[1] - 10, 'B', 13, 'start', INK, True), T(Cc[0] + 12, Cc[1] - 4, 'C', 13, 'start', INK, True)]
    o.append(arrow(Cc[0], Cc[1] - 44, Cc[0], Cc[1] - 8, LV, 2.5, 'l')); o.append(T(Cc[0], Cc[1] - 50, '10 kN', 13, 'middle', LV, True))
    o.append(Tb((A[0] + B[0]) / 2, A[1] - 8, 'AB +5 kN (tension)', 13, 'middle', AC, True))
    o.append(T(A[0] + s * 0.55, A[1] - s * 1.25, 'AC', 13, 'end', LV, True)); o.append(T(A[0] + s * 0.55, A[1] - s * 1.25 + 16, '−7.07 kN', 13, 'end', LV, True))
    o.append(T(B[0] - s * 0.55, B[1] - s * 1.25, 'BC', 13, 'start', LV, True)); o.append(T(B[0] - s * 0.55, B[1] - s * 1.25 + 16, '−7.07 kN', 13, 'start', LV, True))
    o.append(arrow(A[0], A[1] + 56, A[0], A[1] + 26, NX, 2, 'x')); o.append(T(A[0] + 8, A[1] + 52, '5 kN', 13, 'start', NX, True))
    o.append(arrow(B[0], B[1] + 56, B[0], B[1] + 28, NX, 2, 'x')); o.append(T(B[0] - 8, B[1] + 52, '5 kN', 13, 'end', NX, True))
    o.append(T(A[0] + 2 * s, 300, 'Determinate: D = 3 + 3 − 6 = 0', 13, 'middle', INK, True))
    o.append(T(A[0] + 2 * s, 318, 'θ = 45°, sin θ = cos θ = 0.7071', 13, 'middle', MUT))
    # right: three-bar
    cx, top, sc = 540, 50, 62
    D = (cx, top + 2 * sc)
    o.append(L(cx - 2 * sc - 20, top, cx + 2 * sc + 20, top, INK, 3))
    for i in range(16):
        x = cx - 2 * sc - 16 + i * 17; o.append(L(x, top, x + 9, top - 9, MUT, 1.5))
    for x in (cx - 2 * sc, cx, cx + 2 * sc):
        o.append(L(x, top, D[0], D[1], AC if x == cx else LV, 4)); o.append(C(x, top, 4, INK))
    o.append(C(*D, 5, INK)); o.append(T(D[0] + 12, D[1] + 4, 'D', 13, 'start', INK, True))
    o.append(arrow(D[0], D[1] + 6, D[0], D[1] + 44, LV, 2.5, 'l')); o.append(T(D[0], D[1] + 60, 'P = 50 kN', 13, 'middle', LV, True))
    o.append(Tb(cx, top + 0.8 * sc, 'X = 29.29', 13, 'middle', AC, True))
    o.append(T(cx - sc - 12, top + sc, 'F = 14.64', 13, 'end', LV, True)); o.append(T(cx + sc + 12, top + sc, 'F = 14.64', 13, 'start', LV, True))
    o.append(T(cx, 300, 'One redundant: D = 3 + 6 − 8 = 1', 13, 'middle', INK, True))
    o.append(T(cx, 318, 'outer bars at 45°; X = 2F; D drops 2.79 mm', 13, 'middle', MUT))
    return 330, ''.join(o)


FIG[4] = (f4, 'Left: worked example 1. Reactions of 5 kN at A and B; the bottom chord AB is in tension (+5 kN) and each rafter in compression (−7.07 kN). Right: worked example 2, three aluminium bars hanging D. One bar is redundant; least work gives 29.29 kN in the middle bar and 14.64 kN in each outer bar (all tension).',
          'Left: a triangular truss with pin A, roller B 4 metres apart and apex C 2 metres up, 10 kilonewtons down at C, upward reactions of 5 kilonewtons at A and B, bottom chord labelled plus 5 kilonewtons tension and both rafters minus 7.07 kilonewtons. Right: three bars from a ceiling meeting at D, the middle bar vertical and the outer bars at 45 degrees, 50 kilonewtons hanging from D, middle bar labelled X equals 29.29 and outer bars 14.64.')


# ---- 5 beam deflection: M and m diagrams ----
def f5():
    o = []
    X0, X1 = 110, 610
    fx = lin(0, 3, X0, X1)
    yb = 80
    o.append(wall(X0, yb - 26, yb + 26)); o.append(R(X0, yb - 7, X1 - X0, 14, ACS, AC, 2))
    o.append(udl(X0 + 4, X1, yb - 8, 24, LV, 10, 'w = 4 kN/m'))
    o.append(arrow(X1 + 30, yb - 30, X1 + 30, yb - 2, NX, 2.5, 'x')); o.append(T(X1 + 30, yb - 36, 'unit 1', 13, 'middle', NX, True))
    o.append(T(X0, yb + 44, 'fixed, x = 0', 13, 'start', MUT)); o.append(T(X1, yb + 44, 'free, x = 3 m', 13, 'end', MUT))
    Y0, Y1 = 172, 316
    fy = lin(0, 20, Y1, Y0)
    o.append(axes(X0, X1, Y0, Y1, [0, 1, 2, 3], [0, 6, 12, 18], fx, fy, 'x from the fixed end (m)', 'size of moment'))
    o.append(P([(fx(x), fy(2 * (3 - x) ** 2)) for x in [i * 0.05 for i in range(61)]], AC, 2.5))
    o.append(P([(fx(0), fy(3)), (fx(3), fy(0))], NX, 2.5))
    o.append(T(fx(0) + 8, fy(18) + 4, 'M: 18 kN·m', 13, 'start', AC, True))
    o.append(T(fx(0.35), fy(3) - 10, 'm: 3 m (per kN)', 13, 'start', NX, True))
    o.append(T(fx(1.7), fy(13), '∫Mm dx = ∫ 2(3 − x)³ dx = 40.5 kN·m³', 13, 'start', INK, True))
    o.append(T(fx(1.7), fy(13) + 19, 'Δ = 40.5/2400 = 16.875 mm', 13, 'start', AC, True))
    o.append(T(fx(1.7), fy(13) + 38, 'both hogging, so Mm > 0: downward', 13, 'start', MUT))
    return 364, ''.join(o)


FIG[5] = (f5, 'Worked example 1: the 3 m cantilever under 4 kN/m, with a unit load at the free end. The real moment falls as a parabola from 18 kN·m at the fixed end; the unit-load moment falls as a straight line from 3 kN·m per kN. Their product integrates to 40.5 kN·m³, and dividing by EI = 2400 kN·m² gives 16.875 mm.',
          'A cantilever fixed at the left with a uniform load of 4 kilonewtons per metre and a unit load at the free right end. Below, two moment diagrams plotted by size: a parabola falling from 18 kilonewton metres at the fixed end to zero at the tip, and a straight line falling from 3 to zero. Text gives the integral 40.5 and the deflection 16.875 millimetres.')


# ---- 6 propped cantilever ----
def f6():
    o = []
    X0, X1 = 110, 590
    fx = lin(0, 4, X0, X1)
    yb = 90
    o.append(wall(X0, yb - 28, yb + 28)); o.append(R(X0, yb - 7, X1 - X0, 14, ACS, AC, 2))
    o.append(udl(X0 + 4, X1, yb - 8, 24, LV, 12, 'w = 6 kN/m'))
    o.append(roller(X1, yb + 7))
    o.append(arrow(X1 + 34, yb + 50, X1 + 34, yb + 14, NX, 2.2, 'x')); o.append(T(X1 + 42, yb + 46, 'R = 9 kN', 13, 'start', NX, True))
    o.append(arrow(X0 + 22, yb + 52, X0 + 22, yb + 14, NX, 2.2, 'x')); o.append(T(X0 + 30, yb + 50, 'R_A = 15 kN', 13, 'start', NX, True))
    o.append(T(X0 - 16, yb - 34, 'M_A = 12 kN·m', 13, 'end', NX, True))
    o.append(T(X0 - 20, yb + 5, 'A', 13, 'end', INK, True)); o.append(T(X1 + 14, yb - 6, 'B', 13, 'start', INK, True))
    Y0, Y1 = 170, 330
    fy = lin(-12, 8, Y1, Y0)
    o.append(L(X0, fy(0), X1, fy(0), L2, 1.5))
    for v in (-12, -6, 0, 6):
        o.append(T(X0 - 10, fy(v) + 4, ('+' if v > 0 else '') + str(v).replace('-', '−'), 13, 'end', MUT))
    M = lambda x: -12 + 15 * x - 3 * x * x
    o.append(P([(fx(x), fy(M(x))) for x in [i * 0.05 for i in range(81)]], AC, 2.5))
    o.append(C(fx(0), fy(-12), 4, AC)); o.append(T(fx(0) + 10, fy(-12) + 4, '−12 (hogging)', 13, 'start', AC, True))
    o.append(C(fx(2.5), fy(6.75), 4, AC)); o.append(T(fx(2.5), fy(6.75) - 10, '+6.75 at 2.5 m', 13, 'middle', AC, True))
    o.append(C(fx(1), fy(0), 4, NX)); o.append(T(fx(1) + 4, fy(0) - 10, 'M = 0 at 1 m', 13, 'end', NX, True))
    o.append(T(fx(4) - 4, fy(0) + 20, '0 at the prop', 13, 'end', MUT))
    o.append(T((X0 + X1) / 2, 360, 'bending moment M(x) = −12 + 15x − 3x² (kN·m, sagging +)', 13, 'middle', MUT))
    return 372, ''.join(o)


FIG[6] = (f6, 'Worked example 1: the 4 m propped cantilever under 6 kN/m. Compatibility gives the prop 9 kN; then the wall carries 15 kN and a 12 kN·m hogging moment. The moment changes sign 1 m from the wall and peaks at 6.75 kN·m sagging 2.5 m from it.',
          'A beam fixed in a wall at A and resting on a roller at B, 4 metres apart, under a uniform load of 6 kilonewtons per metre. Reactions: 15 kilonewtons and 12 kilonewton metres at A, 9 kilonewtons at B. Below, the bending moment curve starts at minus 12 at A, crosses zero at 1 metre, peaks at plus 6.75 at 2.5 metres and returns to zero at B.')


# ---- 7 three-moment: two-span beam ----
def f7():
    o = []
    X0, X1 = 90, 650
    fx = lin(0, 10, X0, X1)
    yb = 80
    o.append(R(X0, yb - 6, X1 - X0, 12, ACS, AC, 2))
    o.append(udl(X0, X1, yb - 7, 22, LV, 20, 'w = 10 kN/m on both spans'))
    for x, lab in ((0, 'A'), (6, 'B'), (10, 'C')):
        o.append(pin(fx(x), yb + 6)); o.append(T(fx(x), yb + 42, lab, 13, 'middle', INK, True))
    o.append(T(fx(3), yb + 42, '6 m', 13, 'middle', MUT)); o.append(T(fx(8), yb + 42, '4 m', 13, 'middle', MUT))
    Y0, Y1 = 150, 340
    fy = lin(-40, 50, Y1, Y0)
    o.append(L(X0, fy(0), X1, fy(0), L2, 1.5))
    free1 = lambda x: 5 * x * (6 - x); free2 = lambda s: 5 * s * (4 - s)
    o.append(P([(fx(x), fy(free1(x))) for x in [i * 0.1 for i in range(61)]], MUT, 1.5, dash='5 4'))
    o.append(P([(fx(6 + s), fy(free2(4 - s))) for s in [i * 0.1 for i in range(41)]], MUT, 1.5, dash='5 4'))
    MB = -35
    o.append(L(fx(0), fy(0), fx(6), fy(MB), MUT, 1.2, dash='2 3')); o.append(L(fx(6), fy(MB), fx(10), fy(0), MUT, 1.2, dash='2 3'))
    fin = [(x, free1(x) + MB * x / 6) for x in [i * 0.1 for i in range(61)]] + [(6 + s, free2(s) + MB * (4 - s) / 4) for s in [i * 0.1 for i in range(41)]]
    o.append(P([(fx(x), fy(m)) for x, m in fin], AC, 2.5))
    o.append(T(fx(3), fy(45) - 8, 'free wL²/8 = 45', 13, 'middle', MUT)); o.append(T(fx(8), fy(20) - 8, 'free 20', 13, 'middle', MUT))
    o.append(C(fx(6), fy(MB), 4, AC)); o.append(T(fx(6) + 10, fy(MB) + 16, 'M_B = −35 kN·m', 13, 'start', AC, True))
    o.append(T(fx(2.42), fy(29.2) + 20, '+29.2', 13, 'middle', AC, True)); o.append(T(fx(8.875), fy(6.33) + 22, '+6.3', 13, 'middle', AC, True))
    o.append(T(X0 - 8, fy(30), 'sagging +', 13, 'end', MUT)); o.append(T(X0 - 8, fy(-30), 'hogging −', 13, 'end', MUT))
    o.append(T((X0 + X1) / 2, 370, 'bending moment (kN·m): free parabolas dashed, final moment solid', 13, 'middle', MUT))
    return 380, ''.join(o)


FIG[7] = (f7, 'Worked example 1: two spans, 6 m and 4 m, under 10 kN/m. The three-moment equation gives M_B = −35 kN·m. The final diagram (solid) is each span’s free parabola (dashed, peaks 45 and 20 kN·m) less the straight line through the support moments, leaving sagging peaks of 29.2 and 6.3 kN·m.',
          'A two-span beam on supports A, B and C at 0, 6 and 10 metres under a uniform load. Below, dashed free bending moment parabolas peaking at 45 and 20, a dotted closing line down to minus 35 at B, and the solid final moment diagram with sagging peaks of 29.2 in the long span and 6.3 in the short span and the hogging minus 35 at B.')


# ---- 8 moment distribution with a fixed end ----
def f8():
    o = []
    X0, X1 = 110, 610
    fx = lin(0, 10, X0, X1)
    yb = 74
    o.append(wall(X0, yb - 26, yb + 26)); o.append(R(X0, yb - 6, X1 - X0, 12, ACS, AC, 2))
    o.append(udl(X0 + 4, X1, yb - 7, 22, LV, 18, 'w = 10 kN/m'))
    o.append(pin(fx(6), yb + 6)); o.append(roller(fx(10), yb + 6))
    o.append(T(X0 - 8, yb + 34, 'A fixed', 13, 'end', INK, True)); o.append(T(fx(6), yb + 42, 'B', 13, 'middle', INK, True)); o.append(T(fx(10) + 14, yb + 34, 'C pinned', 13, 'start', INK, True))
    o.append(T(fx(3), yb + 42, '6 m', 13, 'middle', MUT)); o.append(T(fx(8), yb + 42, '4 m', 13, 'middle', MUT))
    rows = [('k (EI/m)', '', '0.667', '0.75'), ('DF', '0', '0.471', '0.529'), ('FEM', '−30.00', '+30.00', '−20.00'),
            ('Balance', '', '−4.71', '−5.29'), ('Carry-over', '−2.35', '', ''), ('Final', '−32.35', '+25.29', '−25.29')]
    cx = [170, 330, 470, 610]; y0 = 150; rh = 30
    o.append(R(90, y0 - 22, 590, rh * (len(rows) + 1) + 6, PANEL, L2, 6, 1.5))
    for x, h in zip(cx, ['End', 'AB', 'BA', 'BC']):
        o.append(T(x, y0, h, 14, 'middle', INK, True))
    for i, r in enumerate(rows):
        y = y0 + rh * (i + 1)
        o.append(L(100, y - 20, 670, y - 20, 'var(--line)', 1))
        col = AC if r[0] == 'Final' else (NX if r[0] == 'Carry-over' else INK)
        for x, v in zip(cx, r):
            o.append(T(x, y, v, 13, 'middle', col, r[0] in ('Final', 'DF')))
    yb2 = y0 + rh * 4; yc = y0 + rh * 5
    o.append(arc(cx[2] - 26, yb2 + 2, cx[1] + 30, yc - 4, -0.3, NX, 1.8, 'x'))
    o.append(T(cx[3], yc + 1, '½ × (−4.71) to A', 13, 'middle', NX))
    o.append(T(390, y0 + rh * 7 + 6, 'joint B: +25.29 − 25.29 = 0; nothing is carried to the pinned end C', 13, 'middle', MUT))
    return y0 + rh * 7 + 24, ''.join(o)


FIG[8] = (f8, 'Worked example 2: the same two spans with A fixed. At B the fixed-far-end span BA (k = 4EI/6) and the pinned-far-end span BC (k = 3EI/4) share the 10 kN·m unbalance as 0.471 and 0.529. Half of BA’s share is carried to A; nothing goes to the pin at C. The final moments are 32.35 kN·m at A and 25.29 kN·m at B, both hogging.',
          'A two-span beam fixed in a wall at A, on a pin at B 6 metres along and a roller at C 4 metres further, under 10 kilonewtons per metre. Below, a moment distribution table with columns AB, BA and BC: stiffness 0.667 and 0.75, distribution factors 0, 0.471 and 0.529, fixed end moments minus 30, plus 30 and minus 20, balance minus 4.71 and minus 5.29, a carry-over of minus 2.35 to AB shown by an arrow, and final moments minus 32.35, plus 25.29 and minus 25.29.')

import re as _re
_SUBRX = _re.compile(r'(?<![A-Za-z#.-])([A-Za-zα-ωΔ]{1,3})_([A-Za-z0-9]+(?:,[A-Za-z0-9]+)?)')


def _svgsub(body):
    return _re.sub(r'(<text[^>]*>)(.*?)(</text>)', lambda m: m.group(1) + _SUBRX.sub(
        lambda n: n.group(1) + '<tspan baseline-shift="sub" font-size="11">' + n.group(2) + '</tspan>', m.group(2)) + m.group(3), body, flags=_re.S)


_spec = make_spec(FIG)


def spec(k):
    d = _spec(k)
    d['spec']['body'] = _svgsub(d['spec']['body'])
    d['caption'] = _SUBRX.sub(lambda n: n.group(1) + '<sub>' + n.group(2) + '</sub>', d['caption'])
    return d
