"""Claude's hand-drawn figures for ce-survey-u4 (Theodolite, control surveying and curves), one per chapter.
Every number comes from that chapter's worked example. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def lead(x1, y1, x2, y2):
    """thin leader line from a label to a part"""
    return L(x1, y1, x2, y2, MUT, 1.2)


def ang_arc(cx, cy, r, a1, a2, c=AC, w=1.8):
    """arc of radius r about (cx, cy) from screen angle a1 to a2 (degrees, 0 = +x, counter-clockwise on screen)"""
    p1 = (cx + r * math.cos(math.radians(a1)), cy - r * math.sin(math.radians(a1)))
    p2 = (cx + r * math.cos(math.radians(a2)), cy - r * math.sin(math.radians(a2)))
    large = 1 if abs(a2 - a1) > 180 else 0
    sweep = 0 if a2 > a1 else 1
    return f'<path d="M{p1[0]:.1f},{p1[1]:.1f} A{r},{r} 0 {large} {sweep} {p2[0]:.1f},{p2[1]:.1f}" style="fill:none;stroke:{c};stroke-width:{w}"/>'


# ---- 4.1 the theodolite's lines, and the collimation test ----
def f1():
    o = []
    cx = 190
    # tripod and plumb bob
    o.append(L(cx, 262, 105, 345, INK, 2)); o.append(L(cx, 262, 275, 345, INK, 2)); o.append(L(cx, 262, cx + 8, 345, INK, 1.4))
    o.append(L(40, 348, 330, 348, L2, 2))
    o.append(R(130, 255, 120, 8, 'var(--line)', INK, 2, 1.5))
    o.append(L(cx, 263, cx, 322, MUT, 1, '2 2')); o.append(P([(cx - 5, 322), (cx + 5, 322), (cx, 333), (cx - 5, 322)], INK, 1.5, fill=INK))
    o.append(C(cx, 348, 4, NX))
    # levelling head and foot screws
    o.append(R(140, 230, 100, 14, PANEL, INK, 3, 1.8))
    for x in (150, 230):
        o.append(R(x - 5, 244, 10, 11, 'var(--line)', INK, 2, 1.5))
    # lower plate (horizontal circle) and upper plate
    o.append(R(115, 216, 150, 14, LVS, LV, 3, 2))
    o.append(R(132, 204, 116, 12, ACS, AC, 3, 2))
    # plate level vial with bubble
    o.append(R(140, 194, 44, 10, PANEL, AC, 5, 1.5)); o.append(f'<ellipse cx="162" cy="199" rx="7" ry="3.5" style="fill:var(--accent)"/>')
    # standard
    o.append(P([(162, 204), (218, 204), (204, 128), (176, 128), (162, 204)], INK, 1.8, fill='var(--line)'))
    # vertical circle, face on
    o.append(f'<circle cx="{cx}" cy="118" r="52" style="fill:none;stroke:var(--next);stroke-width:2.2"/>')
    for k in range(0, 360, 15):
        a = math.radians(k); o.append(L(cx + 47 * math.cos(a), 118 + 47 * math.sin(a), cx + 52 * math.cos(a), 118 + 52 * math.sin(a), NX, 1.2))
    # telescope
    o.append(P([(92, 110), (270, 108), (286, 104), (286, 132), (270, 128), (92, 126), (92, 110)], INK, 2, fill=PANEL))
    o.append(R(82, 112, 12, 12, PANEL, INK, 2, 1.5))
    # axes
    o.append(L(cx, 30, cx, 262, AC, 1.8, '7 5'))
    o.append(L(70, 118, 345, 118, LV, 2, '7 5', arrow='l'))
    o.append(C(cx, 118, 6, INK)); o.append(f'<circle cx="{cx}" cy="118" r="2" style="fill:var(--fig)"/>')
    # labels
    o.append(T(cx, 22, 'vertical axis', 14, fill=AC, bold=True))
    o.append(Tb(352, 112, 'line of collimation', 14, 'start', LV, True))
    o.append(Tb(352, 132, '(to the target)', 13, 'start', MUT))
    o.append(lead(205, 122, 350, 158)); o.append(T(352, 162, 'horizontal (trunnion) axis, into the page', 14, 'start', INK))
    o.append(lead(232, 82, 350, 66)); o.append(T(352, 70, 'vertical circle, turns with the telescope', 14, 'start', NX))
    o.append(lead(184, 198, 350, 190)); o.append(T(352, 194, 'plate level (two, at right angles)', 14, 'start', INK))
    o.append(lead(248, 210, 350, 214)); o.append(T(352, 218, 'upper plate with verniers A and B', 14, 'start', AC))
    o.append(lead(265, 224, 350, 238)); o.append(T(352, 242, 'lower plate with the horizontal circle', 14, 'start', LV))
    o.append(lead(240, 250, 350, 262)); o.append(T(352, 266, 'levelling head and foot screws', 14, 'start', INK))
    o.append(lead(195, 336, 350, 312)); o.append(T(352, 316, 'plumb bob over the station mark', 14, 'start', INK))
    o.append(T(86, 100, 'eyepiece', 13, fill=MUT)); o.append(T(286, 96, 'objective', 13, fill=MUT))
    o.append(T(40, 380, 'Side view: the five relations are bubble axis ⟂ vertical axis, vertical hair ⟂ horizontal axis,', 13, 'start', MUT))
    o.append(T(40, 398, 'line of collimation ⟂ horizontal axis, horizontal axis ⟂ vertical axis, altitude level ∥ line of collimation.', 13, 'start', MUT))
    # collimation test, plan view
    y0 = 500
    o.append(T(20, 432, 'Collimation test in plan (offsets exaggerated)', 15, 'start', INK, True))
    xA, xO, xB = 50, 360, 660
    o.append(L(xA, y0, xB + 30, y0, L2, 1.2, '4 4'))
    o.append(L(xA, y0, xO, y0, AC, 2)); o.append(L(xO, y0, xB, y0 - 26, AC, 2)); o.append(L(xO, y0, xB, y0 + 26, NX, 2))
    o.append(C(xA, y0, 5, INK)); o.append(T(xA, y0 + 24, 'A', 15, bold=True))
    o.append(C(xO, y0, 6, INK)); o.append(T(xO, y0 + 26, 'O (instrument)', 14, bold=True))
    o.append(C(xB, y0 - 26, 5, AC)); o.append(T(xB - 6, y0 - 38, 'B (face left)', 14, 'end', AC, True))
    o.append(C(xB, y0 + 26, 5, NX)); o.append(T(xB - 6, y0 + 46, 'C (face right)', 14, 'end', NX, True))
    o.append(C(xB, y0 + 13, 5, LV)); o.append(T(xB + 12, y0 + 12, 'D', 14, 'start', LV, True))
    o.append(brace(xA, xO, y0 + 58, INK)); o.append(T((xA + xO) / 2, y0 + 78, 'about 100 m', 14))
    o.append(brace(xO, xB, y0 + 58, INK)); o.append(T((xO + xB) / 2, y0 + 78, 'OB = 100 m', 14))
    o.append(T(360, y0 + 104, 'BC = 24 mm = 4c × OB, so c = 0.024 ÷ 400 = 0.00006 rad ≈ 12″', 14, fill=INK, bold=True))
    o.append(T(360, y0 + 126, 'Set the vertical hair on D, BC ÷ 4 = 6 mm from C towards B.', 14, fill=LV, bold=True))
    return 642, ''.join(o)
FIG[1] = (f1, 'The theodolite seen from the side, with its lines named, and the collimation test of the worked example in plan. The face-left and face-right marks B and C, 100 m from O, are 24 mm apart, so the collimation error is about 12″ and the hair is set 6 mm from C.',
          'Side view of a transit theodolite showing the vertical axis, the horizontal axis through the standards, the telescope and line of collimation, the vertical circle, the plate level, the two plates, the levelling head and the plumb bob; below, a plan of the collimation test with A, O, the marks B and C 24 millimetres apart 100 metres beyond O, and D a quarter of BC from C.')


# ---- 4.2 horizontal angle by repetition and a vertical angle on both faces ----
def f2():
    o = []
    Q = (80, 270)
    aP, aR = 70, 70 - 42.86
    Pp = (Q[0] + 230 * math.cos(math.radians(aP)), Q[1] - 230 * math.sin(math.radians(aP)))
    Rp = (Q[0] + 260 * math.cos(math.radians(aR)), Q[1] - 260 * math.sin(math.radians(aR)))
    o.append(L(*Q, *Pp, AC, 2.2)); o.append(L(*Q, *Rp, AC, 2.2))
    o.append(ang_arc(Q[0], Q[1], 70, aP, aR, LV, 2.2))
    o.append(L(Q[0] + 70 * math.cos(math.radians(aR + 4)), Q[1] - 70 * math.sin(math.radians(aR + 4)), Q[0] + 70 * math.cos(math.radians(aR)), Q[1] - 70 * math.sin(math.radians(aR)), LV, 2, arrow='l'))
    for p, n in ((Q, 'Q'), (Pp, 'P'), (Rp, 'R')):
        o.append(C(*p, 6, INK))
    o.append(T(Q[0] - 4, Q[1] + 26, 'Q (instrument)', 14, bold=True))
    o.append(T(Pp[0], Pp[1] - 14, 'P', 15, bold=True)); o.append(T(Rp[0] + 14, Rp[1] + 5, 'R', 15, 'start', bold=True))
    o.append(Tb(Q[0] + 96, Q[1] - 56, '42°51′30″', 15, 'start', LV, True))
    o.append(T(Q[0] + 96, Q[1] - 36, 'clockwise P to R', 13, 'start', MUT))
    o.append(T(20, 318, 'Three repetitions on each face:', 14, 'start', INK, True))
    o.append(T(20, 338, 'face left 128°34′00″ ÷ 3 = 42°51′20″', 14, 'start'))
    o.append(T(20, 358, 'face right 128°35′00″ ÷ 3 = 42°51′40″', 14, 'start'))
    o.append(T(20, 378, 'mean = 42°51′30″', 14, 'start', LV, True))
    # vertical angle panel
    O = (420, 250)
    o.append(L(380, O[1], 700, O[1], L2, 1.5, '6 4')); o.append(T(698, O[1] + 20, 'horizontal', 13, 'end', MUT))
    o.append(L(O[0], O[1] + 30, O[0], 40, L2, 1.5, '6 4')); o.append(T(O[0], 32, 'zenith', 13, fill=MUT))
    a = 5.79
    E = (O[0] + 280 * math.cos(math.radians(a)), O[1] - 280 * math.sin(math.radians(a)))
    o.append(L(*O, *E, AC, 2.4, arrow='n')); o.append(T(E[0] - 6, E[1] - 12, 'to the top of the mast', 13, 'end', AC))
    o.append(ang_arc(O[0], O[1], 150, 0, a, LV, 2.2)); o.append(Tb(O[0] + 160, O[1] - 2, 'α = 5°47′30″', 14, 'start', LV, True))
    o.append(ang_arc(O[0], O[1], 80, 90, a, NX, 2)); o.append(Tb(O[0] + 54, O[1] - 92, 'z = 84°12′30″ (corrected)', 14, 'start', NX, True))
    o.append(C(*O, 6, INK)); o.append(T(O[0] - 10, O[1] + 24, 'instrument axis', 13, 'middle', MUT))
    o.append(T(390, 306, 'face left: z = 84°12′40″ → α = +5°47′20″', 14, 'start'))
    o.append(T(390, 326, 'face right: z = 275°47′40″ → α = +5°47′40″', 14, 'start'))
    o.append(T(390, 346, 'z<tspan font-size="11" dy="3">L</tspan><tspan dy="-3"> + z</tspan><tspan font-size="11" dy="3">R</tspan><tspan dy="-3"> = 360°00′20″ → index error = +10″</tspan>', 14, 'start'))
    o.append(T(390, 366, 'mean vertical angle = +5°47′30″', 14, 'start', LV, True))
    return 392, ''.join(o)
FIG[2] = (f2, 'Left: the horizontal angle PQR of the worked example, measured clockwise by three repetitions on each face and meaned to 42°51′30″. Right: the vertical angle to the mast, 5°47′30″ from the face mean, with the 10″ index error found from the sum of the two zenith readings.',
          'Plan of the angle at Q from P clockwise to R, labelled 42 degrees 51 minutes 30 seconds, with the face left and face right repetition results; and a side view of a sight rising 5 degrees 47 minutes 30 seconds above the horizontal, with the zenith distance arc and the face readings and index error listed.')


# ---- 4.3 single plane method with unequal axis levels ----
def f3():
    o = []
    sx = 2.45
    xT = 70
    X = lambda m: xT + m * sx
    Y = lambda rl: 360 - (rl - 100) * 6.6
    xP, xQ = X(165.47), X(225.47)
    o.append(L(20, Y(100), 700, Y(100), L2, 2.5))
    # tower
    o.append(R(xT - 16, Y(138.308), 32, Y(100) - Y(138.308), 'var(--line)', L2, 2, 1.5))
    o.append(C(xT, Y(138.308), 6, AC)); o.append(Tb(xT + 14, Y(138.308) - 8, 'T: RL 138.308 m', 14, 'start', AC, True))
    # instruments
    for x, ax, lab in ((xP, 101.625, 'P'), (xQ, 101.385, 'Q')):
        o.append(L(x, Y(ax) + 4, x - 10, Y(100), INK, 1.6)); o.append(L(x, Y(ax) + 4, x + 10, Y(100), INK, 1.6))
        o.append(C(x, Y(ax), 5, INK))
        o.append(L(xT, Y(ax), x, Y(ax), L2, 1.4, '5 4'))
        o.append(L(x, Y(ax), xT, Y(138.308), LV if lab == 'P' else NX, 2))
        o.append(T(x, Y(100) + 22, lab, 15, bold=True))
    o.append(Tb(xP - 40, Y(101.625) - 12, 'α₁ = 12°30′', 14, 'end', LV, True))
    o.append(Tb(xQ - 30, Y(101.385) - 32, 'α₂ = 9°18′', 14, 'end', NX, True))
    o.append(T(xP, Y(100) + 42, 'axis 101.625', 13, fill=MUT)); o.append(T(xQ + 4, Y(100) + 42, 'axis 101.385', 13, fill=MUT))
    # dimensions
    yd = Y(100) + 70
    o.append(brace(xT, xP, yd, INK)); o.append(T((xT + xP) / 2, yd + 20, 'D = 165.47 m', 14, bold=True))
    o.append(brace(xP, xQ, yd, INK)); o.append(T((xP + xQ) / 2, yd + 20, 's = 60.000 m', 14, bold=True))
    # heights
    xh = xT + 26
    o.append(L(xh, Y(101.625) - 2, xh, Y(138.308) + 8, LV, 1.6, arrow='l')); o.append(L(xh, Y(138.308) + 8, xh, Y(101.625) - 2, LV, 1.6, arrow='l'))
    o.append(Tb(xh + 8, Y(122), 'h₁ = 165.47 × 0.22169 = 36.683 m', 14, 'start', LV, True))
    o.append(Tb(xh + 8, Y(117.5), 'h₂ = 225.47 × 0.16376 = 36.923 m', 14, 'start', NX, True))
    # benchmark
    xb = 250
    o.append(R(xb - 12, Y(100) - 6, 24, 8, 'var(--line)', INK, 1, 1.5)); o.append(T(xb, Y(100) - 14, 'BM 100.000', 13, 'middle', INK, True))
    o.append(T(xb, Y(100) + 22, 'reads 1.625 from P, 1.385 from Q', 13, 'middle', MUT))
    o.append(T(20, yd + 52, 'd = 101.385 − 101.625 = −0.240 m;  D = (60 × 0.16376 − 0.240) ÷ (0.22169 − 0.16376). Heights exaggerated.', 13, 'start', MUT))
    return yd + 66, ''.join(o)
FIG[3] = (f3, 'The single plane method of the worked example in elevation. The two sights meet at the top T; the horizontal distance D = 165.47 m from P and the height above each axis give RL 138.308 m from both stations.',
          'Elevation of a water tower with two theodolite stations P and Q on a line towards it, 60 metres apart, sights rising 12 degrees 30 minutes from P and 9 degrees 18 minutes from Q to the top at RL 138.308 metres, with D 165.47 metres and the heights above the two instrument axes.')


# ---- 4.4 stadia reduction on an inclined sight ----
def f4():
    o = []
    sx = 4.0
    x0, yax = 60, 330
    th = math.radians(8.2)
    xB = x0 + 122.85 * sx
    yB = yax - 17.70 * sx
    o.append(P([(20, yax + 6), (x0 + 30, yax + 6), (xB - 40, yB + 13.4), (xB + 30, yB + 7.4), (560, yB + 5)], L2, 2.5))
    o.append(L(x0, yax, x0 - 10, yax + 8, INK, 1.6)); o.append(L(x0, yax, x0 + 10, yax + 8, INK, 1.6))
    o.append(C(x0, yax, 5, INK)); o.append(T(x0, yax + 30, 'A: RL 100.000, axis 101.450', 13, 'start', INK, True))
    # staff
    o.append(R(xB - 4, yB - 8, 8, 8 + 7.4, NXS, NX, 1, 1.5))
    o.append(L(x0, yax, xB, yB, AC, 2.2, arrow='n'))
    o.append(L(x0, yax, xB, yax, L2, 1.4, '5 4'))
    o.append(L(xB, yax, xB, yB, LV, 2, '5 3'))
    o.append(ang_arc(x0, yax, 110, 0, 8.2, AC, 1.8)); o.append(Tb(x0 + 118, yax - 28, 'θ = +8°12′', 14, 'start', AC, True))
    o.append(brace(x0, xB, yax + 46, INK)); o.append(T((x0 + xB) / 2, yax + 66, 'D = 100 × 1.250 × 0.97966 + 0.400 × 0.98978 = 122.85 m', 14, bold=True))
    o.append(Tb(xB - 8, yax - 10, 'V = 17.70 m', 14, 'end', LV, True))
    o.append(T(xB, yB - 16, 'B', 15, bold=True))
    # inset staff
    x1, y1 = 590, 60
    o.append(R(x1 - 30, y1 - 30, 150, 270, PANEL, L2, 8, 1.5))
    o.append(T(x1 + 45, y1 - 10, 'staff at B', 13, fill=MUT))
    o.append(R(x1, y1, 26, 220, NXS, NX, 1, 1.5))
    def sy(r): return y1 + 220 - r / 3.0 * 220
    for r_, lab, c in ((2.475, 'top 2.475', AC), (1.850, 'mid 1.850', LV), (1.225, 'bottom 1.225', AC)):
        o.append(L(x1 - 6, sy(r_), x1 + 32, sy(r_), c, 2)); o.append(T(x1 + 36, sy(r_) + 5, lab, 13, 'start', c, True))
    o.append(T(x1 + 45, y1 + 240, 's = 1.250 m', 13, fill=INK, bold=True))
    o.append(T(20, 40, 'K = 100, C = 0.400 m (from the 50 m and 100 m taped sights)', 14, 'start', INK, True))
    o.append(T(20, 60, 'RL of B = 101.450 + 17.70 − 1.850 = 117.30 m', 14, 'start', LV, True))
    return yax + 84, ''.join(o)
FIG[4] = (f4, 'The stadia sight of the worked example. With K = 100 and C = 0.400 m, the intercept of 1.250 m at +8°12′ gives D = 122.85 m and V = 17.70 m; from the axis at 101.450 m, B is at RL 117.30 m.',
          'Side view of an inclined sight from station A, axis RL 101.450 metres, rising 8 degrees 12 minutes to a vertical staff at B, with the horizontal distance 122.85 metres, the vertical component 17.70 metres and an enlarged staff showing hair readings 2.475, 1.850 and 1.225 metres.')


# ---- 4.5 the triangle solved and coordinated ----
def f5():
    o = []
    S = 0.62
    X = lambda e: 130 + (e - 5000) * S
    Y = lambda n: 360 - (n - 3000) * S
    A, B, Cc = (X(5000), Y(3000)), (X(5484.06), Y(3125.18)), (X(5111.43), Y(3475.11))
    o.append(P([A, B, Cc, A], AC, 2.4, fill=ACS, op=0.4))
    o.append(L(*A, *B, LV, 4))
    for p, lab, dx, dy, anc in ((A, 'A (5000.000, 3000.000)', -6, 26, 'middle'), (B, 'B (5484.06, 3125.18)', 10, 26, 'middle'), (Cc, 'C (5111.43, 3475.11)', 0, -14, 'middle')):
        o.append(C(*p, 6, INK)); o.append(Tb(p[0] + dx, p[1] + dy, lab, 14, anc, INK, True))
    o.append(Tb((A[0] + B[0]) / 2 + 50, (A[1] + B[1]) / 2 + 34, 'base 499.980 m (MSL)', 14, 'middle', LV, True))
    o.append(Tb((B[0] + Cc[0]) / 2 + 18, (B[1] + Cc[1]) / 2, 'BC = 511.17 m', 14, 'start', AC, True))
    o.append(Tb((A[0] + Cc[0]) / 2 - 12, (A[1] + Cc[1]) / 2, 'AC = 488.00 m', 14, 'end', AC, True))
    o.append(T(A[0] + 84, A[1] - 84, '62°18′05″', 13, 'start', INK))
    o.append(T(B[0] - 50, B[1] - 10, '57°42′00″', 13, 'end', INK))
    o.append(T(Cc[0] + 4, Cc[1] + 36, '59°59′55″', 13, 'middle', INK))
    # north arrow and bearing
    o.append(L(A[0], A[1], A[0], A[1] - 110, L2, 1.4, '5 4'))
    o.append(ang_arc(A[0], A[1], 46, 90, 90 - 75.5, NX, 1.8)); o.append(T(A[0] + 30, A[1] - 50, '75°30′00″', 13, 'start', NX, True))
    o.append(L(640, 120, 640, 60, INK, 2, arrow='m')); o.append(T(640, 48, 'N', 15, bold=True))
    o.append(T(20, 420, 'Angles adjusted by −5″ each (sum was 180°00′15″). Bearing AC = 13°11′55″; BC = 313°12′00″.', 13, 'start', MUT))
    o.append(T(20, 438, 'C from A: (5111.43, 3475.11); from B: (5111.43, 3475.10), agreeing within 0.01 m.', 13, 'start', MUT))
    return 454, ''.join(o)
FIG[5] = (f5, 'The triangle of the worked example drawn to scale on its grid. The base reduced to mean sea level and the adjusted angles give BC and AC by the sine rule, and C is coordinated from A and checked from B.',
          'A triangle A B C plotted from coordinates, with the base AB of 499.980 metres, sides BC 511.17 and AC 488.00 metres, the three adjusted angles, the bearing of AB of 75 degrees 30 minutes from north, and the coordinates of each station.')


# ---- 4.6 closed traverse and its closing error ----
def f6():
    o = []
    S = 0.92
    X = lambda e: 70 + (e - 1000) * S
    Y = lambda n: 380 - (n - 1831.847) * S
    pts = {'A': (1000.000, 2000.000), 'B': (1183.481, 2163.262), 'C': (1329.149, 2028.626), 'D': (1157.080, 1831.847)}
    q = {k: (X(e), Y(n)) for k, (e, n) in pts.items()}
    o.append(P([q['A'], q['B'], q['C'], q['D'], q['A']], AC, 2.4, fill=ACS, op=0.35))
    for (a, b), lab, dx, dy, anc in ((('A', 'B'), 'AB 245.60 m, 48°20′00″', 14, 12, 'start'), (('B', 'C'), 'BC 198.35 m', 10, -4, 'start'),
                                    (('C', 'D'), 'CD 261.40 m', 12, 14, 'start'), (('D', 'A'), 'DA 230.12 m', -12, 16, 'end')):
        m = ((q[a][0] + q[b][0]) / 2, (q[a][1] + q[b][1]) / 2)
        o.append(Tb(m[0] + dx, m[1] + dy, lab, 13, anc, AC, True))
    for k, (dx, dy, anc) in {'A': (-10, 5, 'end'), 'B': (0, -14, 'middle'), 'C': (12, 5, 'start'), 'D': (0, 26, 'middle')}.items():
        o.append(C(*q[k], 6, INK)); o.append(T(q[k][0] + dx, q[k][1] + dy, k, 15, anc, INK, True))
    o.append(L(40, 120, 40, 62, INK, 2, arrow='m')); o.append(T(40, 50, 'N', 15, bold=True))
    # table
    x0 = 420
    rows = [('Station', 'E (m)', 'N (m)'), ('A', '1000.000', '2000.000'), ('B', '1183.481', '2163.262'), ('C', '1329.149', '2028.626'), ('D', '1157.080', '1831.847')]
    o.append(R(x0 - 10, 34, 300, 136, PANEL, L2, 8, 1.5))
    for i, (a, b, c) in enumerate(rows):
        y = 58 + i * 25
        bold = i == 0
        o.append(T(x0 + 10, y, a, 14, 'start', INK, bold)); o.append(T(x0 + 160, y, b, 14, 'end', INK, bold)); o.append(T(x0 + 270, y, c, 14, 'end', INK, bold))
    # closing error inset
    cx, cy = 575, 300
    k = 1300
    o.append(R(410, 196, 300, 190, PANEL, L2, 8, 1.5))
    o.append(T(560, 218, 'Closing error before adjustment', 14, fill=INK, bold=True))
    A2 = (cx - 0.04 * k, cy - 0.03 * k)
    o.append(L(cx, cy, cx - 0.04 * k, cy, NX, 2)); o.append(L(cx - 0.04 * k, cy, *A2, NX, 2))
    o.append(L(*A2, cx, cy, LV, 2.4, arrow='l'))
    o.append(C(cx, cy, 5, INK)); o.append(T(cx + 10, cy + 5, 'A (true)', 13, 'start', INK, True))
    o.append(C(*A2, 5, NX)); o.append(T(A2[0] - 8, A2[1] - 10, 'computed A', 13, 'middle', NX, True))
    o.append(T(cx - 30, cy + 20, 'ΣDep = −0.04', 13, 'middle', NX)); o.append(T(A2[0] - 8, (A2[1] + cy) / 2 + 5, 'ΣLat = +0.03', 13, 'end', NX))
    o.append(T(560, 352, 'e = √(0.04² + 0.03²) = 0.05 m', 14, fill=LV, bold=True))
    o.append(T(560, 372, 'precision 935.47 ÷ 0.05 = 1 in 18 700', 13, fill=INK))
    return 420, ''.join(o)
FIG[6] = (f6, 'The closed traverse of the worked example plotted from its adjusted coordinates. Before adjustment the departures summed to −0.04 m and the latitudes to +0.03 m, a closing error of 0.05 m on 935.47 m (1 in 18 700), which Bowditch\'s rule shared out in proportion to the lengths.',
          'A four-sided traverse A B C D plotted to scale with line lengths and the bearing of AB, a table of adjusted eastings and northings for the four stations, and an inset showing the 0.05 metre closing error made up of minus 0.04 metres in departure and plus 0.03 metres in latitude.')


# ---- 4.7 weighted mean of three levelling runs ----
def f7():
    o = []
    # routes
    o.append(C(70, 100, 7, INK)); o.append(T(70, 76, 'BM 1', 14, bold=True))
    o.append(C(650, 100, 7, INK)); o.append(T(650, 76, 'BM 2', 14, bold=True))
    for dy, lab, c in ((-34, 'run 1: 2 km, 12.436 m, w = 1/2', AC), (0, 'run 2: 3 km, 12.448 m, w = 1/3', NX), (34, 'run 3: 5 km, 12.440 m, w = 1/5', LV)):
        o.append(arc(78, 100, 642, 100, -dy / 600, c, 2, None))
        o.append(Tb(360, 100 + dy * 1.0 + 5, lab, 13, 'middle', c, True))
    # number line
    x0, x1 = 80, 660
    lo, hi = 12.430, 12.452
    fx = lambda v: x0 + (v - lo) / (hi - lo) * (x1 - x0)
    yl = 290
    o.append(xaxis(x0, x1, yl, [12.430, 12.435, 12.440, 12.445, 12.450], fx, 'difference of level (m)', lambda v: f'{v:.3f}'))
    mean = 12.4406
    o.append(L(fx(mean), yl, fx(mean), 160, LV, 2.4, '6 4')); o.append(Tb(fx(mean) + 6, 176, 'weighted mean 12.4406 m', 14, 'start', LV, True))
    for v, w, c, res in ((12.436, 0.5, AC, '−4.6 mm'), (12.448, 0.3333, NX, '+7.4 mm'), (12.440, 0.2, LV, '−0.6 mm')):
        h = w * 140
        o.append(R(fx(v) - 9, yl - h, 18, h, PANEL, c, 2, 2))
        anc, dx = ('end', -12) if v == 12.440 else ('middle', 0)
        o.append(T(fx(v) + dx, yl - h - 26, f'w = {w:.2f}', 13, anc, c, True))
        o.append(T(fx(v) + dx, yl - h - 9, f'v = {res}', 13, anc, c, True))
    o.append(T(20, 360, 'Bars show the weights (∝ 1 ÷ length). Σwv² = 28.9 mm², σ₀ = √(28.9 ÷ 2) = 3.8 mm per 1 km run,', 13, 'start', MUT))
    o.append(T(20, 378, 'standard error of the mean = 3.8 ÷ √1.0333 = 3.7 mm.', 13, 'start', MUT))
    return 394, ''.join(o)
FIG[7] = (f7, 'The three levelling runs of the worked example and their weighted mean. The short run has the largest weight, so the mean, 12.4406 m, lies nearest to it; the residuals are −4.6, +7.4 and −0.6 mm.',
          'Three routes between two benchmarks of 2, 3 and 5 kilometres, and a number line from 12.430 to 12.452 metres with bars at 12.436, 12.448 and 12.440 metres whose heights show weights of one half, one third and one fifth, and a dashed line at the weighted mean of 12.4406 metres.')


# ---- 4.8 simple circular curve ----
def f8():
    o = []
    Rp, dd = 230, 70
    h = math.radians(dd / 2)
    O = (360, 360)
    T1 = (O[0] - Rp * math.sin(h), O[1] - Rp * math.cos(h))
    T2 = (O[0] + Rp * math.sin(h), O[1] - Rp * math.cos(h))
    I = (O[0], O[1] - Rp / math.cos(h))
    crown = (O[0], O[1] - Rp)
    # straights
    ext = 1.45
    back0 = (I[0] + (T1[0] - I[0]) * ext, I[1] + (T1[1] - I[1]) * ext)
    fwd1 = (I[0] + (T2[0] - I[0]) * ext, I[1] + (T2[1] - I[1]) * ext)
    o.append(L(*back0, *I, INK, 2)); o.append(L(*I, *fwd1, INK, 2))
    # back straight produced beyond I
    pr = (I[0] + (I[0] - T1[0]) * 0.55, I[1] + (I[1] - T1[1]) * 0.55)
    o.append(L(*I, *pr, L2, 1.5, '5 4'))
    # arc
    o.append(f'<path d="M{T1[0]:.1f},{T1[1]:.1f} A{Rp},{Rp} 0 0 1 {T2[0]:.1f},{T2[1]:.1f}" style="fill:none;stroke:var(--accent);stroke-width:3"/>')
    o.append(L(*T1, *T2, LV, 1.8, '6 4'))
    o.append(L(*O, *T1, L2, 1.5, '5 4')); o.append(L(*O, *T2, L2, 1.5, '5 4'))
    o.append(L(*I, *crown, NX, 1.8)); o.append(L(crown[0], crown[1], crown[0], T1[1], LV, 1.8))
    # Rankine ray to first peg
    a1 = math.radians(9)
    pk = (O[0] - Rp * math.sin(h - 2 * a1), O[1] - Rp * math.cos(h - 2 * a1))
    o.append(L(*T1, *pk, NX, 1.8, '4 3')); o.append(C(*pk, 4.5, NX))
    for p, lab, dx, dy, anc in ((T1, 'T₁  ch 2340.81', -12, 4, 'end'), (T2, 'T₂  ch 2550.25', 12, 4, 'start'), (I, 'I  ch 2450.000', -14, -6, 'end')):
        o.append(C(*p, 6, INK)); o.append(Tb(p[0] + dx, p[1] + dy, lab, 14, anc, INK, True))
    o.append(C(*O, 5, INK)); o.append(T(O[0], O[1] + 22, 'O (centre)', 13, fill=MUT))
    o.append(Tb((O[0] + T2[0]) / 2 + 10, (O[1] + T2[1]) / 2 + 4, 'R = 300 m', 14, 'start', INK, True))
    o.append(Tb((I[0] + T1[0]) / 2 - 10, (I[1] + T1[1]) / 2 - 6, 'T = 109.19 m', 14, 'end', INK, True))
    o.append(Tb(pr[0] + 6, pr[1] + 6, 'Δ = 40°', 14, 'start', AC, True))
    o.append(ang_arc(I[0], I[1], 44, math.degrees(math.atan2(-(pr[1] - I[1]), pr[0] - I[0])), math.degrees(math.atan2(-(fwd1[1] - I[1]), fwd1[0] - I[0])), AC, 1.8))
    o.append(Tb(crown[0] + 8, (I[1] + crown[1]) / 2 + 5, 'E = 19.25 m', 13, 'start', NX, True))
    o.append(Tb(crown[0] + 8, (crown[1] + T1[1]) / 2 + 8, 'M = 18.09 m', 13, 'start', LV, True))
    o.append(Tb(O[0], T1[1] + 22, 'long chord 205.21 m', 13, 'middle', LV, True))
    o.append(Tb(T1[0] - 12, T1[1] + 26, 'curve l = 209.44 m', 13, 'end', AC, True))
    o.append(T(20, 412, 'Not to scale (Δ drawn larger). Dotted: Rankine sight from T₁ to the peg at chainage 2360.', 13, 'start', MUT))
    o.append(T(20, 430, 'δ: first sub-chord 1°49′57″, each 20 m chord 1°54′35″, last sub-chord 0°58′43″.', 13, 'start', MUT))
    o.append(T(20, 448, 'Total deflection to T₂ = 20°00′00″ = Δ/2.', 13, 'start', MUT))
    return 464, ''.join(o)
FIG[8] = (f8, 'The elements of the circular curve in the worked example: tangent length, apex distance, mid-ordinate, long chord and curve length, with the chainages of I, T₁ and T₂. T₂ is reached round the curve, so its chainage is T₁ + l = 2550.25 m.',
          'A circular curve joining two straights that meet at I, chainage 2450, with tangent points T1 at chainage 2340.81 and T2 at 2550.25, radius 300 metres to the centre O, deflection angle 40 degrees, apex distance 19.25 metres, mid-ordinate 18.09 metres, long chord 205.21 metres, and a Rankine sight from T1 to the first peg.')


spec = make_spec(FIG)
