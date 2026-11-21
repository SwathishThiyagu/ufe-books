"""Claude's hand-drawn figures for ch-mass-u2 (Mass Transfer Coefficients and Interphase Transfer), one per chapter,
drawn from each chapter's own worked example. Every plotted value is computed here from the example's data. Colours are the
shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG, AFTER = {}, {}


def sb(base, s):
    return f'{base}<tspan baseline-shift="sub" font-size="11">{s}</tspan>'


def sp(base, s):
    return f'{base}<tspan baseline-shift="super" font-size="10">{s}</tspan>'


_SUBRE = __import__('re').compile(r'(?<![A-Za-z0-9_.#=])([A-Za-z]{1,2})_([A-Za-z0-9]+(?:,[A-Za-z0-9]+)?)')


def capsub(s):
    s = _SUBRE.sub(lambda m: m.group(1) + '<sub>' + m.group(2) + '</sub>', s)
    return s.replace(')lm', ')<sub>lm</sub>')


def loga(v0, v1, p0, p1):
    """log scale map from value range to pixel range"""
    a, b = math.log10(v0), math.log10(v1)
    return lambda v: p0 + (math.log10(v) - a) / (b - a) * (p1 - p0)


def logticks_x(fx, lo, hi, y, lab, x0, x1):
    o = [L(x0, y, x1, y, L2, 1.5)]
    for e in range(lo, hi + 1):
        X = fx(10 ** e)
        o += [L(X, y, X, y + 5, L2, 1.5), L(X, y, X, 50, LN, 1), T(X, y + 20, sp('10', neg(e)), 13, fill=MUT)]
    o.append(T((x0 + x1) / 2, y + 42, lab, 14, fill=MUT))
    return ''.join(o)


# ---- 2.1 the real profile and its equivalent film ----
def f1():
    o = []
    R_, Tk, kc, D = 8.314, 300, 0.020, 2.6e-5
    cAi = 3540 / (R_ * Tk); cb = 0.30 * cAi; dc = cAi - cb
    delta = D / kc * 1000  # mm
    x0, x1, y0, y1 = 150, 470, 50, 290
    fx = lambda z: x0 + z / 5.0 * (x1 - x0)
    fy = lambda c: y1 - c / 1.6 * (y1 - y0)
    o.append(R(14, y0, 58, y1 - y0, ACS, AC, 4, 1.5))
    o.append(T(43, (y0 + y1) / 2 - 6, 'water', 13, 'middle', AC, True))
    o.append(T(43, (y0 + y1) / 2 + 12, '300 K', 13, 'middle', AC))
    o.append(L(72, (y0 + y1) / 2, x0 - 40, (y0 + y1) / 2, AC, 1.4, '3 3'))
    o.append(axes(x0, x1, y0, y1, [0, 1, 2, 3, 4, 5], [0, 0.4, 0.8, 1.2, 1.6], fx, fy, 'distance from the water surface (mm)', 'water vapour in the air, C (mol/m³)', lambda v: f'{v:g}', lambda v: f'{v:.1f}'))
    zs = [i * 5 / 80 for i in range(81)]
    o.append(P([(fx(z), fy(cb + dc * math.exp(-z / delta))) for z in zs], AC, 3))
    o.append(P([(fx(0), fy(cAi)), (fx(delta), fy(cb))], LV, 2.2, '7 4'))
    o.append(L(fx(0), fy(cb), fx(5), fy(cb), NX, 1.6, '4 3'))
    o.append(L(fx(delta), fy(cb) + 8, fx(delta), y1, L2, 1.2, '3 3'))
    o.append(C(fx(0), fy(cAi), 5))
    o.append(Tb(fx(0) + 12, fy(cAi) - 10, sb('C', 'Ai') + f' = {cAi:.2f} (saturated)', 13, 'start', AC, True))
    o.append(Tb(fx(3.6), fy(cb) - 10, sb('C', 'A∞') + f' = {cb:.3f} (30 % RH)', 13, 'middle', NX, True))
    o.append(Tb(fx(delta) + 6, fy(0.12), f'δ = D/k = {delta:.1f} mm', 13, 'start', LV, True))
    o.append(T(fx(1.9), fy(1.05), 'real profile', 13, 'start', AC))
    o.append(T(fx(1.9), fy(0.92), 'film with the same wall slope', 13, 'start', LV))
    # result panel
    X = 500
    o.append(R(X, 70, 206, 200, PANEL, L2, 8, 1.5))
    rows = [('k_c (measured)', '0.020 m/s'), ('ΔC', f'{dc:.3f} mol/m³'), ('N_A = k_c ΔC', f'{kc * dc:.2e}'.replace('e-02', '×10⁻²')), ('', 'mol/(m²·s)'), ('= 1.29 kg/(m²·h)', ''), ('× P/p_Bm = 1.023', '2.03×10⁻²')]
    yy = 98
    for a, b in rows:
        a = a.replace('k_c', sb('k', 'c')).replace('N_A', sb('N', 'A')).replace('p_Bm', sb('p', 'Bm'))
        o.append(T(X + 12, yy, a, 13, 'start', INK, a.startswith('N')))
        o.append(T(X + 194, yy, b, 13, 'end', AC if b.startswith('1.99') or b.startswith('2.03') else INK, True))
        yy += 28
    return 340, ''.join(o)


FIG[1] = (f1, 'The worked example. Water vapour falls from the saturated value 1.42 mol/m³ at the surface to 0.426 mol/m³ in the 30 % humidity air. The real profile is curved; film theory replaces it by a straight line with the same slope at the wall, which reaches the bulk value at δ = D_AB/k_c = 1.3 mm. The flux is 1.99×10⁻² mol/(m²·s), or 2.03×10⁻² after the stagnant-air correction.',
          'Plot of water-vapour concentration against distance from a water surface from 0 to 5 mm: a solid curve falls from 1.42 at the surface towards 0.426; a dashed straight line from 1.42 meets 0.426 at 1.3 mm. A panel lists k_c 0.020 m/s, driving force 0.994, flux 1.99e-2 mol per square metre per second, 1.29 kg per square metre per hour, and 2.03e-2 after the correction.')
AFTER[1] = 2


# ---- 2.2 resistances in series and the composition step at the interface ----
def f2():
    o = []
    ky, kx, m = 0.050, 0.080, 1.5
    rg, rl = 1 / ky, m / kx
    o.append(T(20, 30, 'Resistances on the gas basis (m²·s/kmol)', 14, 'start', INK, True))
    x0, sc = 40, 14
    o.append(R(x0, 46, rg * sc, 34, NXS, NX, 4))
    o.append(R(x0 + rg * sc, 46, rl * sc, 34, LVS, LV, 4))
    o.append(T(x0 + rg * sc / 2, 68, sb('1/k', 'y') + ' = 20.0', 13, 'middle', NX, True))
    o.append(T(x0 + rg * sc + rl * sc / 2, 68, sb('m/k', 'x') + ' = 18.75', 13, 'middle', LV, True))
    o.append(brace(x0, x0 + (rg + rl) * sc, 92, INK))
    o.append(T(x0 + (rg + rl) * sc / 2, 116, sb('1/K', 'y') + ' = 38.75, so ' + sb('K', 'y') + ' = 0.0258 kmol/(m²·s); gas share 51.6 %', 13, 'middle', INK, True))
    # composition across the interface
    y, x = 0.10, 0.02
    Ky = 1 / (rg + rl); N = Ky * (y - m * x); yi = y - N / ky; xi = yi / m
    X0, X1, Y0, Y1 = 90, 640, 160, 360
    fy = lambda v: Y1 - v / 0.12 * (Y1 - Y0)
    xm = (X0 + X1) / 2
    o.append(L(X0, Y1, X1, Y1, L2, 1.5)); o.append(L(X0, Y0, X0, Y1, L2, 1.5))
    for v in [0, 0.04, 0.08, 0.12]:
        o += [L(X0 - 5, fy(v), X0, fy(v), L2, 1.5), T(X0 - 9, fy(v) + 4.5, f'{v:.2f}', 13, 'end', MUT)]
    o.append(T(X0, Y0 - 12, 'mole fraction of solute', 14, 'start', MUT))
    o.append(R(xm - 4, Y0, 8, Y1 - Y0, ACS, AC, 2, 1))
    o.append(T(xm, Y1 + 20, 'interface', 13, 'middle', AC, True))
    o.append(T((X0 + xm) / 2, Y1 + 20, 'gas', 13, 'middle', NX, True)); o.append(T((xm + X1) / 2, Y1 + 20, 'liquid', 13, 'middle', LV, True))
    g0 = xm - 130; l1 = xm + 130
    o.append(P([(X0, fy(y)), (g0, fy(y)), (xm - 4, fy(yi))], NX, 3))
    o.append(P([(xm + 4, fy(xi)), (l1, fy(x)), (X1, fy(x))], LV, 3))
    o.append(L(xm - 4, fy(yi), xm + 4, fy(xi), AC, 1.5, '3 2'))
    o.append(L(X0, fy(m * x), xm - 4, fy(m * x), NX, 1.4, '5 4'))
    o.append(Tb(X0 + 70, fy(y) - 12, 'bulk gas y = 0.100', 13, 'middle', NX, True))
    o.append(Tb(xm - 12, fy(yi) - 12, sb('y', 'i') + f' = {yi:.4f}', 13, 'end', NX, True))
    o.append(Tb(xm + 12, fy(xi) + 22, sb('x', 'i') + f' = {xi:.4f}', 13, 'start', LV, True))
    o.append(Tb(X1 - 70, fy(x) - 12, 'bulk liquid x = 0.020', 13, 'middle', LV, True))
    o.append(Tb(X0 + 100, fy(m * x) + 20, 'y* = 1.5x = 0.030', 13, 'middle', NX))
    o.append(T(xm + 20, Y0 + 14, sb('y', 'i') + ' = 1.5 ' + sb('x', 'i') + ': equilibrium only here', 13, 'start', AC))
    o.append(T(xm + 20, Y0 + 34, sb('N', 'A') + f' = {N * 1e3:.2f}×10⁻³ kmol/(m²·s)', 13, 'start', INK, True))
    return 390, ''.join(o)


FIG[2] = (f2, 'The worked example. Top: the gas-film resistance 20.0 and the liquid-film resistance on the gas basis, m/k_x = 18.75, add like resistors to 1/K_y = 38.75. Bottom: at y = 0.10 and x = 0.02 the solute mole fraction falls through the gas film to y_i = 0.0639, jumps to x_i = 0.0426 at the interface, where the phases are in equilibrium, and falls through the liquid film to 0.020.',
          'Top, a bar split into a gas part 20.0 and a liquid part 18.75 adding to 38.75. Bottom, a composition profile across a gas film, an interface and a liquid film: gas mole fraction 0.100 falling to 0.0639 at the interface, liquid side 0.0426 at the interface falling to 0.020, and a dashed line at y star 0.030.')
AFTER[2] = 3


# ---- 2.3 Sherwood against Reynolds for the chapter's correlations ----
def f3():
    o = []
    x0, x1, y0, y1 = 80, 650, 50, 330
    fx = loga(1e2, 1e7, x0, x1)
    fyl = loga(1, 1e4, y1, y0)
    o.append(logticks_x(fx, 2, 7, y1, 'Reynolds number Re (log scale)', x0, x1))
    o.append(L(x0, y0, x0, y1, L2, 1.5))
    for e in range(0, 5):
        Y = fyl(10 ** e); o += [L(x0 - 5, Y, x0, Y, L2, 1.5), T(x0 - 9, Y + 4.5, sp('10', e), 13, 'end', MUT)]
    o.append(T(x0, y0 - 12, 'Sherwood number Sh (log scale)', 14, 'start', MUT))
    Sc = 0.577; s3 = Sc ** (1 / 3)
    lam = lambda Re: 0.664 * Re ** 0.5 * s3
    tur = lambda Re: 0.037 * Re ** 0.8 * s3
    rs = lambda a, b, n=40: [a * (b / a) ** (i / n) for i in range(n + 1)]
    o.append(P([(fx(r), fyl(lam(r))) for r in rs(1e3, 5e5)], AC, 3))
    o.append(P([(fx(r), fyl(tur(r))) for r in rs(5e5, 1e7)], NX, 3))
    o.append(T(fx(1.1e3), fyl(300), 'plate, laminar: 0.664 Re½ Sc⅓', 13, 'start', AC, True))
    o.append(T(x1, fyl(700), 'plate, turbulent:', 13, 'end', NX, True))
    o.append(T(x1, fyl(700) + 18, '0.037 Re⁰·⁸ Sc⅓', 13, 'end', NX, True))
    Re1 = 2 * 0.5 / 1.5e-5; Sh1 = lam(Re1)
    o.append(C(fx(Re1), fyl(Sh1), 6, AC))
    o.append(Tb(fx(Re1) + 10, fyl(Sh1) + 24, 'Example 1: Re 6.67×10⁴, Sh 142.7', 13, 'start', AC, True))
    # pipe
    Sc2 = 0.615
    gs = lambda Re: 0.023 * Re ** 0.83 * Sc2 ** 0.44
    o.append(P([(fx(r), fyl(gs(r))) for r in rs(2000, 35000)], LV, 3))
    o.append(P([(fx(100), fyl(3.66)), (fx(2100), fyl(3.66))], LV, 3, '7 4'))
    o.append(T(fx(110), fyl(3.66) - 10, 'pipe, laminar: Sh = 3.66', 13, 'start', LV, True))
    o.append(T(fx(9e3), fyl(6), 'pipe, turbulent: 0.023 Re⁰·⁸³ Sc⁰·⁴⁴', 13, 'start', LV, True))
    Re2 = 3.0 * 0.025 / 1.6e-5
    o.append(C(fx(Re2), fyl(gs(Re2)), 6, LV)); o.append(C(fx(469), fyl(3.66), 6, LV))
    o.append(Tb(fx(Re2) + 12, fyl(11), 'Example 2: 3.0 m/s, Sh 20.7', 13, 'start', LV, True))
    o.append(Tb(fx(469), fyl(3.66) + 24, '0.30 m/s, Re 469', 13, 'middle', LV, True))
    return 400, ''.join(o)


FIG[3] = (f3, 'Each correlation drawn only over its fitted range, at the Schmidt numbers of the two worked examples. The flat-plate example (air at 2 m/s over 0.5 m, Re = 6.67×10⁴) sits on the laminar plate line at Sh = 142.7. The wetted-wall pipe at 3.0 m/s gives Sh = 20.7 on the Gilliland–Sherwood line; at 0.30 m/s the flow is laminar and Sh stays at 3.66.',
          'Log-log plot of Sherwood number against Reynolds number from 1e2 to 1e7. A laminar flat-plate line from 1e3 to 5e5 with the point Re 6.67e4, Sh 142.7; a turbulent flat-plate line from 5e5 to 1e7; a flat dashed pipe line at Sh 3.66 up to Re 2100 with a point at Re 469; and a turbulent pipe line from 2000 to 35000 with the point Re 4690, Sh 20.7.')
AFTER[3] = 2


# ---- 2.4 how k_L scales with D in the three theories ----
def f4():
    o = []
    kL0, D0 = 4.0e-5, 2.1e-9
    x0, x1, y0, y1 = 90, 470, 50, 300
    fx = lambda D: x0 + (D - 0.0) / 3.0e-9 * (x1 - x0)
    fy = lambda k: y1 - k / 6.0e-5 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 1e-9, 2e-9, 3e-9], [0, 2e-5, 4e-5, 6e-5], fx, fy, 'diffusivity D (×10⁻⁹ m²/s)', sb('k', 'L') + ' (×10⁻⁵ m/s)',
                  lambda v: f'{v * 1e9:g}', lambda v: f'{v * 1e5:g}'))
    Ds = [3e-9 * i / 60 for i in range(1, 61)]
    o.append(P([(fx(D), fy(kL0 * D / D0)) for D in Ds if kL0 * D / D0 <= 6e-5], LV, 3))
    o.append(P([(fx(D), fy(kL0 * math.sqrt(D / D0))) for D in Ds], AC, 3))
    o.append(T(fx(2.65e-9), fy(kL0 * 2.65 / 2.1) - 8, 'film: k ∝ D', 13, 'end', LV, True))
    o.append(T(fx(2.05e-9), fy(3.1e-5), 'penetration and', 13, 'start', AC, True))
    o.append(T(fx(2.05e-9), fy(3.1e-5) + 17, 'renewal: k ∝ √D', 13, 'start', AC, True))
    o.append(C(fx(D0), fy(kL0), 6, INK))
    o.append(T(fx(D0) - 14, fy(4.75e-5), 'oxygen, measured 4.0', 13, 'end', INK, True))
    o.append(L(fx(D0) - 12, fy(4.6e-5), fx(D0) - 4, fy(kL0) - 5, INK, 1.2))
    D2 = 1.2e-9
    for k, c in ((kL0 * D2 / D0, LV), (kL0 * math.sqrt(D2 / D0), AC)):
        o.append(C(fx(D2), fy(k), 5.5, c))
    o.append(L(fx(D2), fy(kL0 * D2 / D0), fx(D2), y1, L2, 1.2, '3 3'))
    o.append(Tb(fx(D2) + 10, fy(kL0 * math.sqrt(D2 / D0)) - 6, '3.02', 13, 'start', AC, True))
    o.append(Tb(fx(D2) + 10, fy(kL0 * D2 / D0) + 18, '2.29', 13, 'start', LV, True))
    o.append(T(fx(D2), y1 - 6, '1.2', 12, 'middle', MUT))
    # fitted parameters
    X = 500
    o.append(R(X, 60, 206, 220, PANEL, L2, 8, 1.5))
    o.append(T(X + 103, 84, 'fitted to the oxygen value', 13, 'middle', INK, True))
    rows = [('film', 'δ = D/k', '52.5 µm', LV), ('penetration', 't = 4D/(πk²)', '1.67 s', AC), ('renewal', 's = k²/D', '0.762 s⁻¹', AC)]
    for i, (a, f, v, c) in enumerate(rows):
        yy = 116 + i * 52
        o.append(T(X + 12, yy, a, 13, 'start', c, True))
        o.append(T(X + 12, yy + 20, f, 13, 'start', MUT))
        o.append(T(X + 194, yy + 20, v, 13, 'end', c, True))
    return 350, ''.join(o)


FIG[4] = (f4, 'The worked example. Each theory is fitted to the oxygen measurement, k_L = 4.0×10⁻⁵ m/s at D = 2.1×10⁻⁹ m²/s, which fixes δ, t or s. The theories then part: for a solute with D = 1.2×10⁻⁹ m²/s film theory predicts 2.29×10⁻⁵ m/s, penetration and surface renewal 3.02×10⁻⁵ m/s.',
          'Plot of liquid-film coefficient against diffusivity: a straight line through the origin for film theory and a square-root curve for penetration and surface renewal, both passing through the oxygen point 2.1e-9, 4.0e-5. At D 1.2e-9 they give 2.29e-5 and 3.02e-5. A panel lists the fitted film thickness 52.5 micrometres, exposure time 1.67 s and renewal rate 0.762 per second.')
AFTER[4] = 3


# ---- 2.5 from a pressure reading to k_c ----
def f5():
    o = []
    # pipe sketch
    o.append(R(40, 40, 640, 54, ACS, AC, 27, 2))
    o.append(R(46, 46, 628, 42, FIGBG, L2, 21, 1))
    for xx in (120, 600):
        o.append(L(xx, 40, xx, 14, INK, 2)); o.append(C(xx, 12, 4, INK))
    o.append(T(360, 24, 'Δp = 24.9 Pa over L = 3.0 m', 14, 'middle', INK, True))
    o.append(L(70, 67, 200, 67, NX, 2.5, arrow='x'))
    o.append(T(210, 72, 'air 5.0 m/s, d = 50 mm', 13, 'start', NX, True))
    o.append(T(660, 72, 'naphthalene wall', 13, 'end', AC))
    steps = [('Re = ρud/μ', '1.59×10⁴'), ('f = Δp d/(2Lρu²)', '7.03×10⁻³'), (sb('j', 'D') + ' = f/2', '3.52×10⁻³'), ('Sh = ' + sb('j', 'D') + ' Re Sc⅓', '76.8'), (sb('k', 'c') + ' = Sh D/d', '9.37×10⁻³ m/s')]
    w, gap, y = 122, 12, 130
    for i, (a, b) in enumerate(steps):
        x = 20 + i * (w + gap)
        o.append(R(x, y, w, 66, PANEL if i < 4 else ACS, AC, 8, 2))
        o.append(T(x + w / 2, y + 26, a, 13, 'middle', INK))
        o.append(T(x + w / 2, y + 50, b, 13, 'middle', AC, True))
        if i < 4: o.append(L(x + w + 1, y + 33, x + w + gap - 1, y + 33, AC, 2, arrow='n'))
    o.append(T(20 + 3 * (w + gap) + w / 2, y + 88, 'Sc = 2.57', 13, 'middle', MUT))
    # compare bars
    yb = 250
    o.append(T(20, yb, 'k_c (×10⁻³ m/s)'.replace('k_c', sb('k', 'c')), 14, 'start', INK, True))
    sc = 38
    for i, (lab, v, c, f) in enumerate([('Chilton–Colburn analogy', 9.37, AC, ACS), ('Linton–Sherwood pipe fit', 11.8, NX, NXS)]):
        yy = yb + 16 + i * 40
        o.append(T(210, yy + 19, lab, 13, 'end', c, True))
        o.append(R(220, yy, v * sc, 28, f, c, 4))
        o.append(T(220 + v * sc + 8, yy + 19, f'{v:.2f}' if v < 10 else '11.8', 13, 'start', c, True))
    return 350, ''.join(o)


FIG[5] = (f5, 'The worked example. A 24.9 Pa pressure drop over 3.0 m of smooth 50 mm tube gives the Fanning factor 7.03×10⁻³; the analogy j_D = f/2 then gives Sh = 76.8 and k_c = 9.37×10⁻³ m/s for naphthalene subliming into the air, about 20 % below the direct pipe correlation.',
          'A tube with two pressure taps 3.0 m apart reading 24.9 Pa, air at 5.0 m/s. Five boxes in a chain: Re 1.59e4, Fanning factor 7.03e-3, j_D 3.52e-3, Sh 76.8 with Sc 2.57, k_c 9.37e-3 m/s. Two bars compare the analogy 9.37 with the Linton-Sherwood correlation 11.8, in units of 1e-3 m/s.')
AFTER[5] = 2


# ---- 2.6 the y-x diagram of the worked example ----
def f6():
    o = []
    ky, kx, m, x, y = 0.05, 0.08, 2.0, 0.02, 0.10
    xi = (ky * y + kx * x) / (kx + ky * m); yi = m * xi
    x0, x1, y0, y1 = 80, 490, 40, 330
    fx = lambda v: x0 + v / 0.07 * (x1 - x0)
    fy = lambda v: y1 - v / 0.14 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.02, 0.04, 0.06], [0, 0.04, 0.08, 0.12], fx, fy, 'x, solute mole fraction in the liquid', 'y, in the gas', lambda v: f'{v:.2f}', lambda v: f'{v:.2f}'))
    o.append(P([(fx(0), fy(0)), (fx(0.07), fy(0.14))], AC, 3))
    o.append(T(fx(0.07), fy(0.082), 'equilibrium y = 2x', 13, 'end', AC, True))
    o.append(P([(fx(x), fy(y)), (fx(xi), fy(yi))], LV, 2.5))
    o.append(L(fx(x), fy(y), fx(x), fy(m * x), NX, 1.6, '5 4'))
    o.append(L(fx(x), fy(y), fx(y / m), fy(y), NX, 1.6, '5 4'))
    o.append(C(fx(x), fy(y), 6, INK)); o.append(C(fx(xi), fy(yi), 6, LV))
    o.append(C(fx(x), fy(m * x), 4.5, NX)); o.append(C(fx(y / m), fy(y), 4.5, NX))
    o.append(Tb(fx(x) - 10, fy(y) - 10, 'bulk (0.02, 0.10)', 13, 'end', INK, True))
    o.append(Tb(fx(xi) + 12, fy(yi) + 18, f'interface ({xi:.4f}, {yi:.4f})', 13, 'start', LV, True))
    o.append(Tb(fx(x) + 10, fy(m * x) + 4, 'y* = 0.04', 13, 'start', NX))
    o.append(Tb(fx(y / m) + 8, fy(y) - 10, 'x* = 0.05', 13, 'start', NX))
    o.append(T(fx(0.024), fy(0.108), 'slope −k_x/k_y = −1.6'.replace('k_x', sb('k', 'x')).replace('k_y', sb('k', 'y')), 13, 'start', LV, True))
    X = 508
    o.append(R(X, 60, 200, 200, PANEL, L2, 8, 1.5))
    N = ky * (y - yi)
    rows = [('gas drop y − ' + sb('y', 'i'), f'{y - yi:.5f}'), ('liquid drop ' + sb('x', 'i') + ' − x', f'{xi - x:.5f}'), (sb('N', 'A') + ', gas side', f'{N * 1e3:.3f}'), (sb('N', 'A') + ', liquid side', f'{kx * (xi - x) * 1e3:.3f}'), (sb('K', 'y') + '(y − y*)', f'{0.0222222 * 0.06 * 1e3:.3f}')]
    for i, (a, b) in enumerate(rows):
        yy = 88 + i * 34
        o.append(T(X + 10, yy, a, 13, 'start', INK)); o.append(T(X + 190, yy, b, 13, 'end', AC, True))
    o.append(T(X + 100, 250, 'fluxes ×10⁻³ kmol/(m²·s)', 12, 'middle', MUT))
    return 380, ''.join(o)


FIG[6] = (f6, 'The worked example on the y–x diagram. A line of slope −k_x/k_y = −1.6 from the bulk point (0.02, 0.10) meets the equilibrium line y = 2x at the interface (0.0367, 0.0733). The overall driving forces use y* = 0.04 and x* = 0.05. All three routes give 1.333×10⁻³ kmol/(m²·s).',
          'y-x diagram with the equilibrium line y = 2x, the bulk point at x 0.02, y 0.10, a line of slope minus 1.6 to the interface point 0.0367, 0.0733 on the equilibrium line, and dashed lines from the bulk point down to y star 0.04 and across to x star 0.05. A panel lists the gas and liquid drops and the flux 1.333e-3 from the gas side, the liquid side and the overall coefficient.')
AFTER[6] = 3


# ---- 2.7 stepping off the Kremser example ----
def f7():
    o = []
    m, LG, Y1, YN1 = 1.6, 2.4, 0.0025, 0.050
    XN = (YN1 - Y1) / LG
    x0, x1, y0, y1 = 90, 560, 40, 330
    fx = lambda v: x0 + v / 0.035 * (x1 - x0)
    fy = lambda v: y1 - v / 0.06 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.01, 0.02, 0.03], [0, 0.02, 0.04, 0.06], fx, fy, 'X, kmol solute per kmol solvent', 'Y, kmol solute per kmol carrier gas', lambda v: f'{v:.2f}', lambda v: f'{v:.2f}'))
    o.append(P([(fx(0), fy(0)), (fx(0.035), fy(0.056))], AC, 3))
    o.append(T(fx(0.035), fy(0.040), 'Y* = 1.6X', 13, 'end', AC, True))
    o.append(P([(fx(0), fy(Y1)), (fx(0.0225), fy(Y1 + LG * 0.0225))], NX, 3))
    o.append(T(fx(0.0105), fy(Y1 + LG * 0.0105) - 18, 'operating line, slope L/G = 2.4', 13, 'end', NX, True))
    Y = Y1; pts = [(fx(0), fy(Y1))]
    for n in range(1, 6):
        X = Y / m
        pts.append((fx(X), fy(Y)))
        Yn = Y1 + LG * X
        pts.append((fx(X), fy(min(Yn, 0.058))))
        o.append(T(fx(X) + 8, fy(Y) + 16, str(n), 13, 'start', LV, True))
        Y = Yn
    o.append(P(pts, LV, 2.2))
    o.append(L(x0, fy(YN1), x1, fy(YN1), L2, 1.4, '4 3'))
    o.append(Tb(x0 + 8, fy(YN1) - 8, sb('Y', 'N+1') + ' = 0.050 (gas in)', 13, 'start', INK, True))
    o.append(C(fx(0), fy(Y1), 5, INK))
    o.append(T(fx(0.0105), fy(0.0035), 'top (black dot): ' + sb('X', '0') + ' = 0, ' + sb('Y', '1') + ' = 0.0025, 95 % absorbed', 13, 'start', INK, True))
    o.append(C(fx(XN), fy(YN1), 5, NX))
    o.append(T(fx(XN) - 8, fy(0.053), sb('X', 'N') + f' = {XN:.4f}', 13, 'end', NX, True))
    o.append(T(x1 + 10, 120, 'A = 1.5', 14, 'start', INK, True))
    o.append(T(x1 + 10, 142, 'N = 4.91 ideal', 13, 'start', INK))
    o.append(T(x1 + 10, 162, '5 steps: 95.2 %', 13, 'start', LV, True))
    o.append(T(x1 + 10, 190, sb('E', 'o') + ' = 0.65', 13, 'start', INK))
    o.append(T(x1 + 10, 210, '8 real trays', 13, 'start', AC, True))
    return 380, ''.join(o)


FIG[7] = (f7, 'The Kremser example stepped off graphically. Starting at the top of the absorber (X_0 = 0, Y_1 = 0.0025) each step runs across to the equilibrium line Y* = 1.6X and up to the operating line of slope 2.4. The fifth step passes the inlet gas Y_N+1 = 0.050, matching the 4.91 ideal stages from the equation; at E_o = 0.65 that is 8 real trays.'.replace('Y_N+1', 'Y<sub>N+1</sub>'),
          'X-Y diagram with the equilibrium line Y = 1.6X and the operating line from 0, 0.0025 with slope 2.4. Five numbered staircase steps between the lines climb from Y 0.0025 to beyond the inlet value 0.050, ending near X 0.0198. Notes give A 1.5, 4.91 ideal stages, 95.2 percent with five steps, overall efficiency 0.65 and 8 real trays.')
AFTER[7] = 3


# ---- 2.8 operating line, equilibrium line and the tower ----
def f8():
    o = []
    y1, y2, m, LG = 0.020, 0.0010, 1.2, 2.0
    x1 = (y1 - y2) / LG
    x0, x1p, Y0, Y1 = 90, 480, 40, 330
    fx = lambda v: x0 + v / 0.012 * (x1p - x0)
    fy = lambda v: Y1 - v / 0.024 * (Y1 - Y0)
    o.append(axes(x0, x1p, Y0, Y1, [0, 0.004, 0.008, 0.012], [0, 0.008, 0.016, 0.024], fx, fy, 'x, liquid mole fraction', 'y, gas mole fraction', lambda v: f'{v:.3f}', lambda v: f'{v:.3f}'))
    o.append(P([(fx(0), fy(0)), (fx(0.012), fy(0.0144))], AC, 3))
    o.append(T(fx(0.012), fy(0.0100), 'y* = 1.2x', 13, 'end', AC, True))
    o.append(P([(fx(0), fy(y2)), (fx(x1), fy(y1))], NX, 3))
    o.append(T(fx(0.0042), fy(y2 + 2 * 0.0042) - 12, 'operating line, L/G = 2.0', 13, 'end', NX, True))
    o.append(L(fx(x1), fy(y1), fx(x1), fy(m * x1), LV, 3))
    o.append(L(fx(0) + 3, fy(y2), fx(0) + 3, fy(0), LV, 3))
    o.append(C(fx(x1), fy(y1), 5, NX)); o.append(C(fx(0), fy(y2), 5, NX))
    o.append(Tb(fx(x1) - 10, fy(y1) - 10, 'bottom (0.0095, 0.020)', 13, 'end', NX, True))
    o.append(Tb(fx(x1) + 10, fy((y1 + m * x1) / 2) + 4, 'y − y* = 0.0086', 13, 'start', LV, True))
    o.append(Tb(fx(0) + 12, fy(y2) - 12, 'top: y − y* = 0.0010', 13, 'start', LV, True))
    # tower
    X = 520
    o.append(R(X, 70, 70, 230, ACS, AC, 6, 2))
    for i in range(1, 6):
        yy = 70 + i * 230 / 5.38
        o.append(L(X, yy, X + 70, yy, AC, 1, '3 3'))
    o.append(T(X + 35, 60, 'liquid in, x = 0', 12, 'middle', LV))
    o.append(T(X + 35, 318, 'gas in, y = 0.020', 12, 'middle', NX))
    o.append(T(X + 80, 140, sb('H', 'OG') + ' = 0.40 m', 13, 'start', INK, True))
    o.append(T(X + 80, 162, sb('N', 'OG') + ' = 5.38', 13, 'start', INK, True))
    o.append(T(X + 80, 196, 'Z = 2.15 m', 14, 'start', AC, True))
    o.append(T(X + 80, 230, 'HETP 0.51 m', 13, 'start', MUT))
    o.append(T(X + 80, 250, '× 4.21 stages', 13, 'start', MUT))
    return 380, ''.join(o)


FIG[8] = (f8, 'The worked example. The operating line runs from the top (x = 0, y = 0.0010) to the bottom (x = 0.0095, y = 0.020), above the equilibrium line y* = 1.2x. The vertical gaps y − y* at the two ends, 0.0010 and 0.0086, give a log-mean driving force of 3.53×10⁻³ and N_OG = 5.38; with H_OG = 0.40 m the packed height is 2.15 m, the same as 4.21 ideal stages of HETP 0.51 m.',
          'y-x diagram with the equilibrium line y = 1.2x and an operating line from 0, 0.0010 to 0.0095, 0.020; vertical bars mark the end driving forces 0.0010 and 0.0086. Beside it, a packed tower with about five and a third transfer-unit divisions, liquid entering at the top, gas at the bottom, labelled H_OG 0.40 m, N_OG 5.38 and Z 2.15 m, and HETP 0.51 m times 4.21 stages.')
AFTER[8] = 2


# ---- 2.9 concentration across the film for three Hatta numbers ----
def f9():
    o = []
    x0, x1, y0, y1 = 90, 480, 40, 320
    fx = lambda v: x0 + v * (x1 - x0)
    fy = lambda v: y1 - v * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.25, 0.5, 0.75, 1.0], [0, 0.25, 0.5, 0.75, 1.0], fx, fy, 'distance into the liquid film, x/δ', sb('C', 'A') + '/' + sb('C', 'Ai'), lambda v: f'{v:g}', lambda v: f'{v:g}'))
    xs = [i / 100 for i in range(101)]
    cases = [(0.0, 'no reaction, E = 1', MUT, '6 4'), (1.0, 'Ha = 1, E = 1.31', NX, None), (14.14, 'Ha = 14.1, E = 14.1', AC, None)]
    for Ha, lab, c, d in cases:
        f = (lambda s: 1 - s) if Ha == 0 else (lambda s, H=Ha: math.sinh(H * (1 - s)) / math.sinh(H))
        o.append(P([(fx(s), fy(f(s))) for s in xs], c, 3, d))
    o.append(T(fx(0.62), fy(0.40) - 6, 'no reaction, E = 1', 13, 'start', MUT, True))
    o.append(T(fx(0.36), fy(0.36) + 22, 'Ha = 1, E = 1.31', 13, 'start', NX, True))
    o.append(T(fx(0.2), fy(0.09), 'Ha = 14.1 (example), E = 14.1', 13, 'start', AC, True))
    # tangent at the wall for Ha 14.14 (slope -E): show the first part
    o.append(L(fx(0), fy(1), fx(1 / 14.14), fy(0), AC, 1.4, '3 3'))
    X = 510
    o.append(R(X, 60, 196, 210, PANEL, L2, 8, 1.5))
    o.append(T(X + 98, 84, 'worked example', 13, 'middle', INK, True))
    rows = [('k', '10 s⁻¹'), (sb('D', 'A'), '2×10⁻⁹ m²/s'), (sb('k', 'L'), '1.0×10⁻⁵ m/s'), ('Ha = √(k' + sb('D', 'A') + ')/' + sb('k', 'L'), '14.14'), ('N without reaction', '5.0×10⁻⁷'), ('N with reaction', '7.07×10⁻⁶')]
    for i, (a, b) in enumerate(rows):
        yy = 110 + i * 27
        o.append(T(X + 10, yy, a, 13, 'start', INK)); o.append(T(X + 186, yy, b, 13, 'end', AC, True))
    o.append(T(X + 98, 268 + 18, 'fluxes in mol/(m²·s)', 12, 'middle', MUT))
    return 375, ''.join(o)


FIG[9] = (f9, 'Film-theory profiles of dissolved A for a first-order reaction, C_A/C_Ai = sinh[Ha(1 − x/δ)]/sinh Ha with no A in the bulk. Without reaction the profile is straight; at Ha = 1 it sags and the wall slope, which sets the flux, is 1.31 times steeper; at the example\'s Ha = 14.1 the A is used up within a tenth of the film and the flux is 14.1 times the physical value.',
          'Plot of dissolved A concentration over its interface value against distance into the liquid film: a dashed straight line for no reaction, a sagging curve for Hatta number 1, and a curve for Hatta number 14.1 that falls to near zero within the first tenth of the film, with its steep tangent at the interface. A panel lists the example data and the fluxes 5.0e-7 and 7.07e-6 mol per square metre per second.')
AFTER[9] = 2


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'caption': capsub(cap), 'after_section': AFTER[k], 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
