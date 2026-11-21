"""Claude's hand-drawn figures for ae-struct-u3 (Aircraft Structures: columns, beam-columns, failure theories and fatigue), one per chapter,
drawn from each chapter's own worked example; every plotted value is computed here. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
PI2 = math.pi ** 2


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


def arrow(x1, y1, x2, y2, c=AC, w=2, k='n', dash=None):
    return L(x1, y1, x2, y2, c, w, dash, arrow=k)


def hatch_h(x0, x1, y, up=True, c=INK):
    o = [L(x0, y, x1, y, c, 3)]
    d = -8 if up else 8
    x = x0 + 3
    while x < x1:
        o.append(L(x, y, x + 7, y + d, MUT, 1.4)); x += 9
    return ''.join(o)


def pinmark(x, y, up=False, c=INK):
    s = -1 if up else 1
    return P([(x, y), (x - 9, y + s * 15), (x + 9, y + s * 15), (x, y)], c, 2)


# ---- 1 Euler: four end conditions ----
def f1():
    o = []
    cases = [('pinned-pinned', 1.0, '34.5 kN', 'pp'), ('fixed-fixed', 0.5, '138.2 kN*', 'ff'), ('fixed-pinned', 0.7, '70.5 kN', 'fp'), ('fixed-free', 2.0, '8.6 kN', 'fr')]
    top, bot = 70, 250
    H = bot - top
    for i, (name, K, Pcr, kind) in enumerate(cases):
        cx = 100 + i * 175
        o.append(arrow(cx, top - 40, cx, top - 6, LV, 2.5, 'l'))
        o.append(T(cx, top - 46, 'P', 13, 'middle', LV, True))
        o.append(L(cx, top, cx, bot, L2, 1.5, dash='4 4'))
        amp = 26
        pts = []
        for j in range(61):
            t = j / 60
            if kind == 'pp': dx = amp * math.sin(math.pi * t)
            elif kind == 'ff': dx = amp * 0.5 * (1 - math.cos(2 * math.pi * t))
            elif kind == 'fp':
                kL = 4.4934; s = 1 - t  # fixed at bottom (s=0)... shape v = sin(kx) - kx cos(kL) ... use standard mode
                x = t
                dx = amp * 0.75 * (math.sin(kL * x) - kL * x * math.cos(kL) - math.sin(kL) * x) / 1.0
            else: dx = amp * 1.2 * (1 - math.cos(math.pi * (1 - t) / 2))
            pts.append((cx + dx, top + t * H))
        o.append(P(pts, AC, 3))
        if kind in ('pp',):
            o.append(pinmark(cx, top, True)); o.append(pinmark(cx, bot))
        elif kind == 'ff':
            o.append(hatch_h(cx - 18, cx + 18, top, True)); o.append(hatch_h(cx - 18, cx + 18, bot, False))
        elif kind == 'fp':
            o.append(pinmark(cx, top, True)); o.append(hatch_h(cx - 18, cx + 18, bot, False))
        else:
            o.append(hatch_h(cx - 18, cx + 18, bot, False))
        o.append(T(cx, bot + 30, name, 13, 'middle', INK, True))
        o.append(T(cx, bot + 48, f'K = {K}, L_e = {K * 2:g} m', 13, 'middle', MUT))
        o.append(T(cx, bot + 68, 'P_cr = ' + Pcr, 13, 'middle', NX if '*' in Pcr else AC, True))
    o.append(T(360, bot + 96, '* 276 MPa, above the 200 MPa proportional limit: this Euler value is not valid', 13, 'middle', NX))
    return bot + 108, ''.join(o)


FIG[1] = (f1, 'The 2 m aluminium strut of the worked example (EI = 1.4 × 10⁴ N·m², A = 500 mm²) under four end conditions, with its first buckled shape. Free-ended it carries only 8.6 kN because L_e = 4 m. Fixed at both ends Euler gives 138.2 kN, but that is 276 MPa, past the proportional limit, so the real strut fails earlier.',
          'Four vertical struts, each with an axial load P on top and its buckled shape: pinned-pinned, a half sine wave, P critical 34.5 kilonewtons; fixed-fixed, a full cosine wave, 138.2 kilonewtons marked not valid; fixed-pinned, 70.5 kilonewtons; fixed-free, a quarter wave with the tip swinging out, 8.6 kilonewtons. Each is labelled with its K factor and effective length.')


# ---- 2 Rankine-Gordon ----
def f2():
    o = []
    X0, X1, Y0, Y1 = 80, 650, 40, 300
    fx = lin(0, 200, X0, X1); fy = lin(0, 140, Y1, Y0)
    o.append(axes(X0, X1, Y0, Y1, [0, 40, 80, 120, 160, 200], [0, 35, 70, 105, 140], fx, fy, 'slenderness λ = L_e/r', 'load (kN)'))
    A, E, sc = 400, 200000, 320
    a = sc / (PI2 * E)
    eul = lambda l: PI2 * E * A / l ** 2 / 1000
    ran = lambda l: sc * A / (1 + a * l * l) / 1000
    o.append(L(fx(0), fy(128), fx(200), fy(128), MUT, 1.5, dash='6 4'))
    o.append(T(fx(200), fy(128) - 8, 'squash load σ_c × A = 128 kN', 13, 'end', MUT))
    o.append(P([(fx(l), fy(eul(l))) for l in range(68, 201, 2)], LV, 2.2, dash='7 4'))
    o.append(P([(fx(l), fy(ran(l))) for l in range(0, 201, 2)], AC, 2.8))
    o.append(T(fx(84), fy(eul(84)) - 6, 'Euler π²EA/λ²', 13, 'start', LV, True))
    o.append(T(fx(6), fy(85), 'Rankine-Gordon', 13, 'start', AC, True))
    o.append(L(fx(120), fy(0), fx(120), fy(eul(120)), L2, 1.2, dash='3 3'))
    o.append(C(fx(120), fy(eul(120)), 5, LV)); o.append(T(fx(120) + 10, fy(eul(120)) - 6, 'P_E = 54.8 kN', 13, 'start', LV, True))
    o.append(C(fx(120), fy(ran(120)), 5, AC)); o.append(T(fx(120) - 10, fy(ran(120)) + 22, 'P_R = 38.4 kN', 13, 'end', AC, True))
    return 350, ''.join(o)


FIG[2] = (f2, 'The steel strut of worked example 1 (A = 400 mm², σ_c = 320 MPa, E = 200 GPa) at every slenderness. Rankine-Gordon starts at the 128 kN squash load, stays below Euler everywhere, and gives 38.4 kN at λ = 120, where Euler gives 54.8 kN.',
          'Load against slenderness from 0 to 200: a dashed flat line at the 128 kilonewton squash load, a dashed Euler hyperbola falling from above, and the solid Rankine-Gordon curve starting at 128 and staying below both. At slenderness 120 the Euler curve is marked at 54.8 kilonewtons and the Rankine-Gordon curve at 38.4 kilonewtons.')


# ---- 3 secant formula ----
def f3():
    o = []
    X0, X1, Y0, Y1 = 260, 660, 40, 290
    PE = 13.817
    fx = lin(0, 14, X0, X1); fy = lin(0, 200, Y1, Y0)
    o.append(axes(X0, X1, Y0, Y1, [0, 4, 8, 12], [0, 50, 100, 150, 200], fx, fy, 'axial load P (kN)', 'stress (MPa)'))
    smax = lambda p: (p / 0.2) * (1 + 0.2 / math.cos(0.5 * math.sqrt(p * 1000 / 1400)))
    o.append(P([(fx(p), fy(p / 0.2)) for p in (0, 14)], MUT, 2, dash='6 4'))
    pts = [(fx(p), fy(smax(p))) for p in [i * 0.1 for i in range(1, 121)] if smax(p) < 200]
    o.append(P([(fx(0), fy(0))] + pts, AC, 2.8))
    o.append(L(fx(PE), Y0, fx(PE), Y1, NX, 1.5, dash='4 3')); o.append(T(fx(PE) - 4, Y0 + 14, 'P_E = 13.8', 13, 'end', NX, True))
    o.append(C(fx(8), fy(61.8), 5, AC)); o.append(T(fx(8) - 10, fy(61.8) - 10, 'σ_max = 61.8', 13, 'end', AC, True))
    o.append(C(fx(8), fy(40), 5, MUT)); o.append(T(fx(8) + 10, fy(40) + 16, 'P/A = 40', 13, 'start', MUT, True))
    o.append(T(fx(12.2), fy(56) + 24, 'mean P/A', 13, 'end', MUT))
    # strut sketch
    sx, t0, t1 = 110, 70, 270
    o.append(L(sx - 24, t0, sx + 24, t0, INK, 3)); o.append(L(sx - 24, t1, sx + 24, t1, INK, 3))
    o.append(L(sx, t0, sx, t1, L2, 1.2, dash='4 4'))
    o.append(P([(sx + 10 + 34 * math.sin(math.pi * j / 40), t0 + (t1 - t0) * j / 40) for j in range(41)], AC, 3))
    o.append(arrow(sx + 10, t0 - 40, sx + 10, t0 - 4, LV, 2.5, 'l')); o.append(arrow(sx + 10, t1 + 40, sx + 10, t1 + 4, LV, 2.5, 'l'))
    o.append(T(sx + 18, t0 - 26, 'P = 8 kN', 13, 'start', LV, True))
    o.append(T(sx - 4, t0 - 10, 'e', 13, 'end', NX, True)); o.append(L(sx, t0 - 6, sx + 10, t0 - 6, NX, 2))
    o.append(T(sx + 50, (t0 + t1) / 2 + 4, 'v', 13, 'start', AC, True))
    o.append(T(sx, t1 + 60, 'e = 2 mm, L = 1 m', 13, 'middle', MUT))
    return 360, ''.join(o)


FIG[3] = (f3, 'Left: the strut of the worked example, loaded 2 mm off its axis, bows further as the load rises. Right: its peak stress by the secant formula (solid) against the mean stress P/A (dashed). At 8 kN the peak is 61.8 MPa against a mean of 40 MPa, and the curve turns upward without limit as P approaches the 13.8 kN Euler load.',
          'A pinned strut with an end load 8 kilonewtons applied at a small offset e and a bowed shape v. Beside it a graph of stress against axial load from 0 to 14 kilonewtons: a straight dashed line for the mean stress P over A, and a solid secant curve rising faster and turning up steeply towards a vertical dashed line at the Euler load 13.8 kilonewtons; at 8 kilonewtons the curve is marked at 61.8 megapascals and the mean at 40.')


# ---- 4 inelastic: Johnson and Euler ----
def f4():
    o = []
    X0, X1, Y0, Y1 = 80, 650, 40, 300
    E, sy = 70000, 320
    fx = lin(0, 120, X0, X1); fy = lin(0, 450, Y1, Y0)
    o.append(axes(X0, X1, Y0, Y1, [0, 20, 40, 60, 80, 100, 120], [0, 100, 200, 300, 400], fx, fy, 'slenderness λ', 'buckling stress (MPa)'))
    lj = math.sqrt(2 * PI2 * E / sy)
    o.append(L(fx(0), fy(sy), fx(120), fy(sy), MUT, 1.4, dash='6 4')); o.append(T(fx(120), fy(sy) - 8, 'σ_Y = 320', 13, 'end', MUT))
    eu = lambda l: PI2 * E / l ** 2
    o.append(P([(fx(l), fy(eu(l))) for l in [39.4 + i * 0.5 for i in range(int((lj - 39.4) / 0.5) + 1)]], LV, 1.8, dash='4 4'))
    o.append(P([(fx(l), fy(eu(l))) for l in [lj + i * 0.5 for i in range(int((120 - lj) / 0.5) + 1)]], LV, 2.8))
    jo = lambda l: sy - sy * sy / (4 * PI2 * E) * l * l
    o.append(P([(fx(l), fy(jo(l))) for l in [i * 0.5 for i in range(int(lj / 0.5) + 1)]], AC, 2.8))
    o.append(L(fx(lj), Y1, fx(lj), fy(160.1), NX, 1.2, dash='3 3'))
    o.append(C(fx(lj), fy(160.1), 5, NX)); o.append(T(fx(lj) + 10, fy(160.1) - 8, 'λ_J = 65.7, σ_Y/2 = 160', 13, 'start', NX, True))
    o.append(C(fx(40), fy(260.7), 5, AC)); o.append(T(fx(40) - 8, fy(260.7) + 22, 'λ = 40: 260.7', 13, 'end', AC, True))
    o.append(C(fx(40), fy(431.8), 5, LV)); o.append(T(fx(40) + 10, fy(431.8) + 4, 'Euler 431.8, not valid', 13, 'start', LV, True))
    o.append(T(fx(20), fy(150), 'Johnson parabola', 13, 'middle', AC, True))
    o.append(T(fx(100), fy(eu(100)) - 12, 'Euler', 13, 'middle', LV, True))
    return 350, ''.join(o)


FIG[4] = (f4, 'Column curve for the aluminium alloy of the worked example (E = 70 GPa, σ_Y = 320 MPa). Johnson’s parabola (solid, left) holds up to λ_J = 65.7, where it meets Euler’s curve at σ_Y/2 = 160 MPa; Euler (solid, right) holds above it. At λ = 40 the strut buckles at 260.7 MPa, while Euler (dashed, not valid) would give 431.8 MPa.',
          'Buckling stress against slenderness from 0 to 120. A dashed line at the 320 megapascal yield strength. The Johnson parabola falls from 320 at zero slenderness to 160 at slenderness 65.7, where it touches the Euler hyperbola, which continues as a solid curve to the right and is dashed to the left where it is not valid. Points mark the example at slenderness 40: Johnson 260.7 and Euler 431.8, not valid.')


# ---- 5 beam-column amplification ----
def f5():
    o = []
    X0, X1, Y0, Y1 = 80, 650, 40, 300
    fx = lin(0, 1, X0, X1); fy = lin(0, 8, Y1, Y0)
    o.append(axes(X0, X1, Y0, Y1, [0, 0.2, 0.4, 0.6, 0.8, 1.0], [0, 2, 4, 6, 8], fx, fy, 'P / P_E', 'moment amplification M_max / M₀', lambda v: f'{v:g}'))
    o.append(L(fx(0), fy(1), fx(1), fy(1), MUT, 1.5, dash='6 4')); o.append(T(fx(0.02), fy(1) + 18, 'first-order, 1', 13, 'start', MUT))
    o.append(P([(fx(a), fy(1 / (1 - a))) for a in [i * 0.005 for i in range(0, 176)]], AC, 2.8))
    ex = lambda a: math.tan(math.pi / 2 * math.sqrt(a)) / (math.pi / 2 * math.sqrt(a)) if a > 0 else 1
    o.append(P([(fx(a), fy(ex(a))) for a in [i * 0.005 for i in range(0, 181)]], LV, 2.2, dash='7 4'))
    o.append(L(fx(1), Y0, fx(1), Y1, NX, 1.2, dash='3 3')); o.append(T(fx(1) - 6, fy(1.6), 'buckling', 13, 'end', NX))
    o.append(C(fx(0.603), fy(2.52), 5, AC)); o.append(T(fx(0.603) - 10, fy(2.52) - 10, '0.603: 2.52', 13, 'end', AC, True))
    o.append(C(fx(0.603), fy(2.239), 5, LV)); o.append(T(fx(0.603) + 10, fy(2.239) + 18, 'exact 2.24', 13, 'start', LV, True))
    o.append(T(fx(0.78), fy(1 / (1 - 0.78)) - 6, '1/(1 − P/P_E)', 13, 'end', AC, True))
    o.append(T(fx(0.74), fy(2.7), 'tan u/u (exact)', 13, 'start', LV, True))
    return 350, ''.join(o)


FIG[5] = (f5, 'Moment amplification against axial load. The simple factor 1/(1 − P/P_E) (solid) and the exact factor for a central point load, tan u/u (dashed), both start at 1 and run away near the Euler load. The stringer of the worked example sits at P/P_E = 0.603: 2.52 by the simple factor, 2.24 exactly.',
          'Amplification factor against P over P E from 0 to 1. A flat dashed line at 1 for the first-order moment, a solid curve one over one minus P over P E rising steeply towards a vertical dashed line at 1, and a slightly lower dashed curve for the exact central-load factor. The worked example is marked at 0.603 with 2.52 on the solid curve and 2.24 on the dashed one.')


# ---- 6 max principal stress and strain envelopes ----
def env_axes(o, fx, fy, lim):
    o.append(L(fx(-lim), fy(0), fx(lim), fy(0), L2, 1.4)); o.append(L(fx(0), fy(-lim), fx(0), fy(lim), L2, 1.4))
    o.append(T(fx(lim), fy(0) - 8, 'σ₁ (MPa)', 13, 'end', MUT)); o.append(T(fx(0) + 8, fy(lim) + 12, 'σ₂ (MPa)', 13, 'start', MUT))


def f6():
    o = []
    cx, cy, s = 300, 200, 0.44
    fx = lambda v: cx + v * s; fy = lambda v: cy - v * s
    env_axes(o, fx, fy, 400)
    Y = 250
    o.append(P([(fx(Y), fy(Y)), (fx(-Y), fy(Y)), (fx(-Y), fy(-Y)), (fx(Y), fy(-Y)), (fx(Y), fy(Y))], LV, 2.4))
    a, b = Y / 0.7, Y / 1.3
    o.append(P([(fx(a), fy(a)), (fx(-b), fy(b)), (fx(-a), fy(-a)), (fx(b), fy(-b)), (fx(a), fy(a))], AC, 2.4))
    o.append(T(fx(250) + 6, fy(0) + 18, '250', 13, 'start', MUT)); o.append(T(fx(-250) - 6, fy(0) - 8, '−250', 13, 'end', MUT))
    o.append(C(fx(106.16), fy(-46.16), 5, NX)); o.append(T(fx(106.16), fy(-46.16) + 20, 'example', 13, 'middle', NX, True))
    o.append(T(fx(-250) + 6, fy(250) - 8, 'Rankine square ±250', 13, 'start', LV, True))
    o.append(T(fx(a) + 6, fy(a) + 4, 'St Venant (357, 357)', 13, 'start', AC, True))
    o.append(T(fx(250) + 8, fy(-b) + 4, '(192, −192)', 13, 'start', AC, True))
    xr = 560
    o.append(T(xr, 70, 'Worked example', 14, 'middle', INK, True))
    o.append(T(xr, 96, 'σ₁ = 106.2, σ₂ = −46.2 MPa', 13, 'middle', MUT))
    o.append(T(xr, 130, 'stress: 250/106.2', 13, 'middle', LV, True)); o.append(T(xr, 148, 'n = 2.35', 13, 'middle', LV, True))
    o.append(T(xr, 182, 'strain: Eε₁ = 120.0', 13, 'middle', AC, True)); o.append(T(xr, 200, 'n = 2.08 (governs)', 13, 'middle', AC, True))
    o.append(T(xr, 236, 'ν = 0.30, σ_Y = 250 MPa', 13, 'middle', MUT))
    return 390, ''.join(o)


FIG[6] = (f6, 'Safe regions in the σ₁–σ₂ plane for σ_Y = 250 MPa and ν = 0.30. Maximum principal stress gives the square; maximum principal strain gives the rhombus, which reaches out to 357 MPa in equal biaxial tension and cuts in to 192 MPa along σ₁ = −σ₂. The worked-example point lies inside both; strain gives the smaller factor, 2.08.',
          'Principal stress plane with sigma 1 across and sigma 2 up. A square with sides at plus and minus 250 megapascals for the maximum principal stress theory, and a rhombus for the maximum principal strain theory with corners at 357, 357 and minus 357, minus 357 along the diagonal and 192, minus 192 and minus 192, 192 across it. The example point 106.2, minus 46.2 sits inside both. A note gives factors 2.35 by stress and 2.08 by strain.')


# ---- 7 Tresca and von Mises ----
def f7():
    o = []
    cx, cy, s = 300, 200, 0.5
    fx = lambda v: cx + v * s; fy = lambda v: cy - v * s
    env_axes(o, fx, fy, 390)
    Y = 250
    hexa = [(Y, 0), (Y, Y), (0, Y), (-Y, 0), (-Y, -Y), (0, -Y), (Y, 0)]
    o.append(P([(fx(a), fy(b)) for a, b in hexa], LV, 2.4))
    pts = []
    for j in range(121):
        t = 2 * math.pi * j / 120
        u, v = math.sqrt(2) * Y * math.cos(t), math.sqrt(2.0 / 3.0) * Y * math.sin(t)
        pts.append(((u - v) / math.sqrt(2), (u + v) / math.sqrt(2)))
    o.append(P([(fx(a), fy(b)) for a, b in pts], AC, 2.4))
    o.append(P([(fx(144.3), fy(-144.3)), (fx(0), fy(0)), (fx(125), fy(-125))], NX, 1.2, dash='3 3'))
    o.append(C(fx(144.3), fy(-144.3), 4, AC)); o.append(C(fx(125), fy(-125), 4, LV))
    o.append(T(fx(144.3) + 8, fy(-144.3) + 14, 'pure shear: Tresca 125, von Mises 144', 13, 'start', INK, True))
    o.append(C(fx(106.16), fy(-46.16), 5, NX)); o.append(T(fx(106.16), fy(-46.16) - 10, 'example', 13, 'middle', NX, True))
    o.append(T(fx(250) + 6, fy(0) + 18, '250', 13, 'start', MUT)); o.append(T(fx(-250) - 6, fy(0) - 8, '−250', 13, 'end', MUT))
    o.append(T(fx(-250), fy(250) - 10, 'Tresca hexagon', 13, 'start', LV, True))
    o.append(T(440, 70, 'von Mises ellipse', 13, 'start', AC, True))
    xr = 600
    o.append(T(xr, 112, 'σ_x = 100, σ_y = −40,', 13, 'middle', MUT)); o.append(T(xr, 130, 'τ_xy = 30 MPa', 13, 'middle', MUT))
    o.append(T(xr, 156, 'Tresca 152.3: n = 1.64', 13, 'middle', LV, True))
    o.append(T(xr, 176, 'von Mises 135.3: n = 1.85', 13, 'middle', AC, True))
    o.append(T(xr, 196, 'principal 106.2: n = 2.36', 13, 'middle', MUT, True))
    return 380, ''.join(o)


FIG[7] = (f7, 'Yield loci for σ_Y = 250 MPa in plane stress. The Tresca hexagon lies inside the von Mises ellipse, touching it at the six corners (uniaxial and equal biaxial stress). They differ most in pure shear (σ₂ = −σ₁): Tresca yields at 125 MPa, von Mises at 144 MPa. The worked example gives factors of 1.64 by Tresca and 1.85 by von Mises.',
          'Principal stress plane with a hexagon for Tresca and an ellipse for von Mises, both passing through 250 megapascals on each axis and through 250, 250 and minus 250, minus 250. Along the pure-shear diagonal the hexagon is crossed at 125 and the ellipse at 144. The example point 106.2, minus 46.2 is inside both. A note gives the equivalent stresses 152.3 by Tresca and 135.3 by von Mises.')


# ---- 8 S-N curve ----
def f8():
    o = []
    X0, X1, Y0, Y1 = 90, 650, 40, 300
    fx = lin(3, 8, X0, X1); fy = lin(300, 700, Y1, Y0)
    o.append(L(X0, Y1, X1, Y1, L2, 1.5)); o.append(L(X0, Y0, X0, Y1, L2, 1.5))
    for k in range(3, 9):
        X = fx(k); o.append(L(X, Y1, X, Y1 + 5, L2, 1.5)); o.append(T(X, Y1 + 21, f'10<tspan baseline-shift="super" font-size="11">{k}</tspan>', 13, 'middle', MUT))
    for v in (300, 400, 500, 600, 700):
        Y = fy(v); o.append(L(X0 - 5, Y, X0, Y, L2, 1.5)); o.append(L(X0, Y, X1, Y, 'var(--line)', 1)); o.append(T(X0 - 9, Y + 4.5, str(v), 13, 'end', MUT))
    o.append(T((X0 + X1) / 2, Y1 + 42, 'cycles to failure N (log scale)', 14, 'middle', MUT)); o.append(T(X0, Y0 - 12, 'stress amplitude S (MPa)', 14, 'start', MUT))
    b = (math.log10(400) - math.log10(600)) / 3
    S = lambda lg: 900 * 10 ** (b * lg)
    o.append(P([(fx(lg), fy(S(lg))) for lg in [3 + i * 0.05 for i in range(61)]], AC, 2.8))
    o.append(P([(fx(6), fy(400)), (fx(8), fy(400))], AC, 2.8))
    o.append(P([(fx(6), fy(400)), (fx(8), fy(S(8)))], MUT, 1.4, dash='5 4'))
    o.append(T(fx(7.95), 252, 'aluminium: no flat part', 13, 'end', MUT))
    o.append(T(fx(7), fy(400) - 10, 'endurance limit 400 MPa (from 10⁶)', 13, 'middle', AC, True))
    lgN = math.log10(22335)
    o.append(L(fx(3), fy(500), fx(lgN), fy(500), NX, 1.4, dash='3 3')); o.append(L(fx(lgN), fy(500), fx(lgN), Y1, NX, 1.4, dash='3 3'))
    o.append(C(fx(lgN), fy(500), 5, NX)); o.append(T(fx(lgN) + 10, fy(500) - 8, '500 MPa: N = 2.23 × 10⁴', 13, 'start', NX, True))
    o.append(C(fx(3), fy(600), 4, AC)); o.append(T(fx(3) + 10, fy(600) - 8, '600 at 10³', 13, 'start', AC, True))
    o.append(T(fx(4.6), fy(S(4.6)) - 30, 'S = 900 N^(−0.0587)', 13, 'start', AC, True))
    return 350, ''.join(o)


FIG[8] = (f8, 'The steel of worked example 1 on log axes: Basquin’s line S = 900N<sup>−0.0587</sup> falls from 600 MPa at 10³ cycles to 400 MPa at 10⁶, then flattens at the 400 MPa endurance limit. At 500 MPa the life is 2.23 × 10⁴ cycles. An aluminium alloy has no flat part; its curve keeps falling (dashed).',
          'Stress amplitude against cycles on a log scale from ten to the 3 to ten to the 8. A straight sloping line from 600 megapascals at a thousand cycles to 400 at a million, then a flat line at 400 labelled endurance limit; a dashed line continues falling for an aluminium-like alloy. A marked point at 500 megapascals reads off a life of 2.23 times ten to the 4 cycles.')


# ---- 9 Haigh diagram ----
def f9():
    o = []
    X0, X1, Y0, Y1 = 80, 650, 40, 300
    fx = lin(0, 850, X0, X1); fy = lin(0, 650, Y1, Y0)
    o.append(axes(X0, X1, Y0, Y1, [0, 200, 400, 600, 800], [0, 200, 400, 600], fx, fy, 'mean stress σ_m (MPa)', 'alternating stress σ_a (MPa)'))
    Se, Su, Sy = 400, 800, 600
    o.append(P([(fx(0), fy(Se)), (fx(Su), fy(0))], AC, 2.8))
    o.append(P([(fx(0), fy(Se)), (fx(Sy), fy(0))], NX, 2.2))
    o.append(P([(fx(m), fy(Se * (1 - (m / Su) ** 2))) for m in range(0, 801, 10)], LV, 2.2, dash='7 4'))
    o.append(P([(fx(0), fy(Sy)), (fx(Sy), fy(0))], MUT, 1.6, dash='3 3'))
    o.append(L(fx(0), fy(0), fx(200), fy(400), L2, 1.2, dash='2 3'))
    o.append(C(fx(100), fy(200), 6, INK)); o.append(T(fx(100) + 12, fy(200) + 4, 'load (100, 200)', 13, 'start', INK, True))
    o.append(C(fx(160), fy(320), 5, AC))
    o.append(L(fx(160) - 4, fy(320) - 4, fx(55), fy(445) + 6, AC, 1.2)); o.append(T(fx(15), fy(445), 'n = 1.60', 13, 'start', AC, True))
    lx, ly = 450, 60
    for i, (col, w, d, txt) in enumerate([(AC, 2.8, None, 'Goodman, to S_u = 800'), (NX, 2.2, None, 'Soderberg, to S_y = 600'),
                                          (LV, 2.2, '7 4', 'Gerber parabola'), (MUT, 1.6, '3 3', 'Langer: σ_a + σ_m = S_y')]):
        y = ly + 22 * i
        o.append(L(lx, y - 4, lx + 30, y - 4, col, w, dash=d) if d else L(lx, y - 4, lx + 30, y - 4, col, w))
        o.append(T(lx + 38, y, txt, 13, 'start', col if col != MUT else MUT, True))
    return 350, ''.join(o)


FIG[9] = (f9, 'Constant-life lines for S_e = 400, S_u = 800 and S_y = 600 MPa. The fitting of the worked example, σ_m = 100 and σ_a = 200 MPa, lies inside all of them. Scaling it along its load line reaches the Goodman line at (160, 320), so n = 1.60; Soderberg gives 1.50 and Gerber 1.89. The Langer line marks first-cycle yield.',
          'Alternating stress against mean stress. A straight Goodman line from 400 on the vertical axis to 800 on the horizontal axis, a steeper Soderberg line to 600, a dashed Gerber parabola bulging above Goodman, and a dotted Langer yield line from 600 to 600. The load point 100, 200 sits inside, and a dotted ray from the origin through it meets the Goodman line at 160, 320, labelled n equals 1.60.')

import re as _re
_SUBRX = _re.compile(r'(?<![A-Za-z#.-])([A-Za-zα-ωΔ]{1,3})_([A-Za-z0-9]+(?:,[A-Za-z0-9]+)?)')


def _svgsub(body):
    return _re.sub(r'(<text[^>]*>)(.*?)(</text>)', lambda m: m.group(1) + _SUBRX.sub(
        lambda n: n.group(1) + '<tspan baseline-shift="sub" font-size="11">' + n.group(2) + '</tspan>', m.group(2)) + m.group(3), body, flags=_re.S)


_spec = make_spec(FIG)


def spec(k):
    d = _spec(k)
    b = _svgsub(d['spec']['body'])
    d['spec']['body'] = b.replace('N^(−0.0587)', 'N<tspan baseline-shift="super" font-size="11">−0.0587</tspan>')
    d['caption'] = _SUBRX.sub(lambda n: n.group(1) + '<sub>' + n.group(2) + '</sub>', d['caption'])
    return d
