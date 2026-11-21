"""Claude's hand-drawn figures for ch-thermo-u7 (Chemical reaction equilibria), one per chapter.
Every number comes from that chapter's worked examples. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
R_ = 8.314


def sb(base, s, size=11):
    return f'{base}<tspan baseline-shift="sub" font-size="{size}">{s}</tspan>'


def sp(base, s, size=11):
    return f'{base}<tspan baseline-shift="super" font-size="{size}">{s}</tspan>'


def curve(f, x0, x1, fx, fy, n=80, c=AC, w=2.5, dash=None):
    pts = [(fx(x0 + (x1 - x0) * i / n), fy(f(x0 + (x1 - x0) * i / n))) for i in range(n + 1)]
    return P(pts, c, w, dash)


def bis(f, a, b):
    for _ in range(80):
        m = (a + b) / 2
        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m
    return (a + b) / 2


# ---- extent of reaction: the ammonia mole table ----
def f1():
    o = []
    x0, x1, y0, y1 = 70, 500, 40, 360
    fy = lambda n: y1 - n / 40 * (y1 - y0)
    o.append(L(x0, y1, x1, y1, L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    for v in (0, 10, 20, 30, 40):
        Y = fy(v)
        o.append(L(x0 - 5, Y, x0, Y, L2, 1.5)); o.append(L(x0, Y, x1, Y, LN, 1))
        o.append(T(x0 - 9, Y + 4.5, str(v), 13, 'end', MUT))
    o.append(T(x0, y0 - 12, 'moles (mol)', 14, 'start', MUT))
    groups = [('N₂', 10, 6, '−1'), ('H₂', 30, 18, '−3'), ('NH₃', 0, 8, '+2'), ('total', 40, 32, '−2')]
    bw, gap = 34, 108
    for i, (nm, a, b, nu) in enumerate(groups):
        gx = x0 + 30 + i * gap
        o.append(R(gx, fy(a), bw, y1 - fy(a), L2, L2, 3, 1)) if a else None
        o.append(R(gx + bw + 4, fy(b), bw, y1 - fy(b), ACS if nm != 'total' else NXS, AC if nm != 'total' else NX, 3, 2))
        if a:
            o.append(T(gx + bw / 2, fy(a) - 6, str(a), 13, 'middle', MUT, bold=True))
        else:
            o.append(T(gx + bw / 2, y1 - 6, '0', 13, 'middle', MUT, bold=True))
        o.append(T(gx + bw * 1.5 + 4, fy(b) - 6, str(b), 13, 'middle', AC if nm != 'total' else NX, bold=True))
        o.append(T(gx + bw + 2, y1 + 20, nm, 14, 'middle', INK, bold=True))
        o.append(T(gx + bw + 2, y1 + 40, ('ν = ' if nm != 'total' else 'Σν = ') + nu, 13, 'middle', MUT))
    o.append(R(330, 52, 14, 12, L2, L2, 2, 1)); o.append(T(350, 63, 'feed, ξ = 0', 13, 'start', MUT))
    o.append(R(330, 74, 14, 12, ACS, AC, 2, 2)); o.append(T(350, 85, 'at ξ = 4 mol', 13, 'start', AC))
    o.append(boxt(520, 40, 190, 150, ['nᵢ = nᵢ₀ + νᵢξ', 'N₂: 10 − 4 = 6', 'H₂: 30 − 12 = 18', 'NH₃: 0 + 8 = 8', 'total: 40 − 8 = 32'],
                  PANEL, AC, 13, bold_first=True))
    o.append(boxt(520, 206, 190, 150, ['two reactions:', 'steam reformer', 'ξ₁ = 0.60, ξ₂ = 0.20', 'total 4.00 → 5.20 mol', 'CH₄ conversion 0.60', 'H₂O conversion 0.267'],
                  NXS, NX, 13, bold_first=True))
    return 420, ''.join(o)
FIG[1] = (f1, 'The worked mole table for ammonia synthesis: 10 mol N₂ and 30 mol H₂ react to extent ξ = 4 mol. Each species changes by νᵢξ, so N₂ falls to 6, H₂ to 18, NH₃ rises to 8 and the total falls from 40 to 32 mol. The lower box repeats the two-reaction steam-reformer example.',
          'Bar chart of moles before and after reaction: N2 10 to 6, H2 30 to 18, NH3 0 to 8, total 40 to 32, with the stoichiometric numbers minus 1, minus 3, plus 2 and minus 2 under the bars; side boxes give n i = n i0 + nu i xi and the steam reformer totals.')


# ---- equilibrium criterion: G against extent for A ⇌ B at 500 K ----
def f2():
    o = []
    x0, x1, y0, y1 = 90, 510, 40, 360
    RT = R_ * 500
    g = lambda x: -4000 * x + RT * ((1 - x) * math.log(1 - x) + x * math.log(x))
    fx = lambda x: x0 + x * (x1 - x0)
    lo, hi = -6000, 500
    fy = lambda v: y1 - (v - lo) / (hi - lo) * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.2, 0.4, 0.6, 0.8, 1.0], [-6000, -4000, -2000, 0], fx, fy,
                  'ξ (mol), from 1 mol A', 'G − ' + sp('μ', '°') + ' of A (J)', lambda v: f'{v:g}', lambda v: neg(f'{v:g}')))
    o.append(curve(g, 0.0005, 0.9995, fx, fy, n=160, c=AC, w=3))
    for xt, s, col, dx in ((0.25, -8567, NX, 0.09), (0.90, 5134, LV, 0.07)):
        gt = g(xt)
        o.append(L(fx(xt - dx), fy(gt - s * dx), fx(xt + dx), fy(gt + s * dx), col, 2.4))
        o.append(C(fx(xt), fy(gt), 6, col))
    o.append(Tb(fx(0.27), fy(-2650), 'slope −8567 J/mol: go forward', 13, 'start', NX, bold=True))
    o.append(Tb(fx(0.90) - 4, fy(g(0.90)) - 34, 'slope +5134: go back', 13, 'end', LV, bold=True))
    xm = 0.724
    o.append(C(fx(xm), fy(g(xm)), 7, AC))
    o.append(L(fx(xm), fy(g(xm)), fx(xm), y1, AC, 1.4, '3 4'))
    o.append(Tb(fx(xm), fy(g(xm)) + 24, 'minimum: ξ = 0.724, −5345 J', 13, 'middle', AC, bold=True))
    o.append(boxt(526, 40, 186, 176, ['A ⇌ B, 500 K, 1 bar', 'ΔG° = −4.00 kJ/mol', 'RT = 4157 J/mol', 'dG/dξ = ΔG°', '+ RT ln[ξ/(1 − ξ)]', 'zero at ξ = 0.724'], PANEL, AC, 13, bold_first=True))
    o.append(boxt(526, 232, 186, 100, ['trial mixture:', 'μ of A = −12.0 kJ/mol', 'μ of B = −20.0 kJ/mol', 'reaction ΔG = −8.0 kJ/mol', 'so it goes forward'], NXS, NX, 13))
    return 420, ''.join(o)
FIG[2] = (f2, 'The worked isomerisation A ⇌ B at 500 K: total Gibbs energy against extent. The slope is −8567 J/mol at ξ = 0.25, so reaction runs forward, and +5134 J/mol at ξ = 0.90, so it runs back; both meet at the minimum, ξ = 0.724 mol and 5345 J below pure A, where ΔG<sub>r</sub> = 0.',
          'A curve of G minus the standard chemical potential of A against extent from 0 to 1 mol, falling from 0 to a minimum of minus 5345 joules at extent 0.724 and rising to minus 4000 at extent 1; tangent lines mark slope minus 8567 at 0.25 and plus 5134 at 0.90.')


# ---- standard Gibbs energy to K ----
def f3():
    o = []
    rows = [(46, ['ammonia, 298.15 K', '2 × (−16.45)'], ['ΔG° = −32.90 kJ', 'RT = 2478.8 J'], ['ln K = 13.272', 'K = 5.81 × 10⁵'], ['per mol NH₃', 'K′ = √K = 762']),
            (176, ['A ⇌ 2B, 400 K', 'tabulated'], ['ΔG° = +5.0 kJ', 'RT = 3325.6 J'], ['ln K = −1.503', 'K = 0.222'], ['all a = 1: Q = 1', 'Q > K: back'])]
    xs = [20, 196, 372, 548]
    for y, *bx in rows:
        for j, lines in enumerate(bx):
            fill = ACS if j == 2 else PANEL
            o.append(boxt(xs[j], y, 152, 80, lines, fill, AC if y == 46 else LV, 14, bold_first=(j == 0)))
            if j < 3:
                o.append(L(xs[j] + 154, y + 40, xs[j + 1] - 4, y + 40, AC if y == 46 else LV, 2.2, arrow='n' if y == 46 else 'l'))
    o.append(T(xs[1] + 76, 30, 'ΔG° = Σ νᵢ ' + sb('ΔG', 'f') + '°', 14, 'middle', MUT, bold=True))
    o.append(T(xs[2] + 76, 30, 'ln K = −ΔG°/RT', 14, 'middle', MUT, bold=True))
    o.append(boxt(20, 296, 680, 100, ['K = Π ' + sp('aᵢ', 'νᵢ') + ', with the activity set by the standard state:',
                                      'ideal gas aᵢ = yᵢP/P°;  real gas aᵢ = yᵢφᵢP/P°;',
                                      'liquid solution aᵢ = xᵢγᵢ;  pure solid or liquid a = 1'], NXS, NX, 14))
    return 420, ''.join(o)
FIG[3] = (f3, 'The two worked examples as one route from data to K. Ammonia at 298.15 K: ΔG° = −32.90 kJ/mol gives ln K = 13.272 and K = 5.81 × 10⁵, or 762 per mole of NH₃. A ⇌ 2B at 400 K: ΔG° = +5.0 kJ/mol gives K = 0.222, so at unit activities (Q = 1) the reaction runs back.',
          'Two rows of four boxes joined by arrows. Top row: ammonia data, Delta G standard minus 32.90 kilojoules, ln K 13.272 and K 5.81 times ten to the five, K prime 762. Bottom row: A to 2B at 400 kelvin, Delta G standard plus 5.0 kilojoules, ln K minus 1.503 and K 0.222, Q greater than K so backward. A lower box lists the activity for each standard state.')


# ---- temperature: van't Hoff plot for ammonia ----
def lnK_nh3(T):
    T0, dH0, dG0 = 298.15, -92220.0, -32900.0
    dA, dB, dD = -5.871, 4.181e-3, -66100.0
    H = lambda t: dH0 + R_ * (dA * (t - T0) + dB / 2 * (t * t - T0 * T0) - dD * (1 / t - 1 / T0))
    n = 400; h = (T - T0) / n; s = 0
    for i in range(n + 1):
        t = T0 + i * h
        w = 1 if i in (0, n) else (4 if i % 2 else 2)
        s += w * H(t) / (R_ * t * t)
    return -dG0 / (R_ * T0) + s * h / 3


def f4():
    o = []
    x0, x1, y0, y1 = 80, 510, 40, 360
    fx = lambda u: x0 + (u - 1.3) / (3.5 - 1.3) * (x1 - x0)
    fy = lambda v: y1 - (v + 12) / (16 + 12) * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [1.4, 1.8, 2.2, 2.6, 3.0, 3.4], [-12, -8, -4, 0, 4, 8, 12, 16], fx, fy,
                  '1000/T (1/K): hotter to the left', 'ln K, ammonia synthesis', lambda v: f'{v:.1f}', lambda v: neg(f'{v:g}')))
    lnc = lambda T: 13.272 + 11092 * (1 / T - 1 / 298.15)
    o.append(P([(fx(1000 / t), fy(lnc(t))) for t in (298.15, 720)], L2, 2.2, '7 5'))
    pts = [(298.15 + i * (720 - 298.15) / 40) for i in range(41)]
    o.append(P([(fx(1000 / t), fy(lnK_nh3(t))) for t in pts], AC, 3))
    for Tk, lab in ((400, '400 K: 3.60'), (500, '500 K: −2.30'), (600, '600 K: −6.37'), (700, '700 K: −9.37')):
        v = lnK_nh3(Tk)
        o.append(C(fx(1000 / Tk), fy(v), 6, AC))
        o.append(Tb(fx(1000 / Tk) + 12, fy(v) + 18, lab, 13, 'start', AC, bold=True))
    o.append(C(fx(1000 / 298.15), fy(13.272), 6, AC))
    o.append(Tb(fx(1000 / 298.15) - 8, fy(13.272) - 12, '298 K: 13.27', 13, 'end', AC, bold=True))
    o.append(C(fx(2.0), fy(lnc(500)), 6, MUT))
    o.append(L(fx(1.62), fy(5.6), fx(2.0) - 5, fy(lnc(500)) - 5, MUT, 1.4, '3 3'))
    o.append(Tb(fx(1.42), fy(6.6), 'constant ΔH°: −1.75', 13, 'start', MUT, bold=True))
    o.append(L(fx(1.42), fy(13), fx(1.62), fy(13), AC, 3)); o.append(T(fx(1.66), fy(13) + 5, 'with ΔCp°', 13, 'start', AC))
    o.append(L(fx(1.42), fy(10.5), fx(1.62), fy(10.5), L2, 2.2, '7 5')); o.append(T(fx(1.66), fy(10.5) + 5, 'constant ΔH°', 13, 'start', MUT))
    o.append(boxt(526, 40, 186, 170, ['ammonia at 500 K', 'constant ΔH°:', 'K = 0.174', 'with ΔCp°:', 'K = 0.100', 'slope = −ΔH°/R'], PANEL, AC, 13,
                  fills=[INK, MUT, MUT, AC, AC, INK]))
    o.append(boxt(526, 226, 186, 128, ['first example:', 'ΔH° = −50.0 kJ/mol', 'K = 10.0 at 300 K', '→ 0.571 at 350 K'], NXS, NX, 13, bold_first=True))
    return 420, ''.join(o)
FIG[4] = (f4, 'Van\'t Hoff plot for ammonia synthesis. With the heat capacities included (solid), ln K falls from 13.27 at 298 K to −2.30 at 500 K and −9.37 at 700 K. The dashed constant-ΔH° line, slope −ΔH°/R = 11 092 K, overshoots to ln K = −1.75 (K = 0.174 instead of 0.100) at 500 K. The lower box repeats the first worked example.',
          'ln K against 1000 over T for ammonia synthesis: a slightly curved solid line through points at 298, 400, 500, 600 and 700 kelvin with ln K 13.27, 3.60, minus 2.30, minus 6.37 and minus 9.37, and a dashed straight constant enthalpy line that lies above it at high temperature, reaching minus 1.75 at 500 kelvin.')


# ---- equilibrium composition: Q(ξ) meets K ----
def f5():
    o = []
    x0, x1, y0, y1 = 80, 510, 40, 360
    fx = lambda x: x0 + x / 0.5 * (x1 - x0)
    fy = lambda q: y1 - q / 1.4 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.1, 0.2, 0.3, 0.4, 0.5], [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4], fx, fy,
                  'ξ (mol), from 1 mol A at 1 bar', 'Q or K', lambda v: f'{v:g}', lambda v: f'{v:.1f}'))
    Q = lambda x: 4 * x * x / (1 - x * x)
    o.append(curve(Q, 0, 0.5, fx, fy, n=100, c=AC, w=3))
    o.append(L(x0, fy(0.222), x1, fy(0.222), NX, 2.4, '7 4'))
    o.append(Tb(fx(0.07), fy(0.222) - 10, 'K = 0.222', 13, 'middle', NX, bold=True))
    o.append(Tb(fx(0.43), fy(Q(0.43)) - 2, 'Q = 4ξ²/(1 − ξ²)', 13, 'end', AC, bold=True))
    o.append(C(fx(0.2293), fy(0.222), 7, NX))
    o.append(L(fx(0.2293), fy(0.222), fx(0.2293), y1, NX, 1.4, '3 4'))
    o.append(Tb(fx(0.2293) + 10, fy(0.222) + 30, 'ξ = 0.229', 13, 'start', NX, bold=True))
    o.append(Tb(fx(0.24), fy(0.222) + 54, sb('y', 'A') + ' = 0.627, ' + sb('y', 'B') + ' = 0.373', 13, 'start', NX))
    o.append(T(fx(0.1), fy(0.55), 'Q < K: forward', 13, 'middle', MUT))
    o.append(T(fx(0.39), fy(1.05), 'Q > K: back', 13, 'middle', MUT))
    o.append(boxt(526, 40, 186, 140, ['A ⇌ 2B, 400 K', 'moles: A 1 − ξ, B 2ξ', 'total 1 + ξ', '0.222 = 4.222ξ²', 'ξ = 0.2293 mol'], PANEL, AC, 13, bold_first=True))
    o.append(boxt(526, 196, 186, 160, ['water-gas shift', 'K = 1.00, Σν = 0', 'P cancels', 'CO:H₂O 1:1 → ξ = 0.500', 'CO:H₂O 1:2 → ξ = 0.667', 'more steam, more CO used'], NXS, NX, 13, bold_first=True))
    return 420, ''.join(o)
FIG[5] = (f5, 'The first worked example solved by eye: Q(ξ) from the mole balances rises from zero and crosses K = 0.222 at ξ = 0.229 mol, giving y<sub>A</sub> = 0.627 and y<sub>B</sub> = 0.373. Left of the crossing Q < K and the reaction runs forward; right of it, back. The lower box repeats the water-gas-shift example.',
          'Q against extent for A to 2B: a curve rising from 0 to 1.33 at extent 0.5 crosses a dashed horizontal line K = 0.222 at extent 0.229; labels show Q less than K forward on the left and Q greater than K back on the right, with boxes for the solution and the water gas shift.')


# ---- direction: ΔG = RT ln(Q/K) ----
def f6():
    o = []
    x0, x1, y0, y1 = 80, 510, 40, 360
    RT = R_ * 400
    fx = lambda x: x0 + x / 0.5 * (x1 - x0)
    fy = lambda v: y1 - (v + 12) / 18 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.1, 0.2, 0.3, 0.4, 0.5], [-12, -9, -6, -3, 0, 3, 6], fx, fy,
                  'ξ (mol)', 'ΔG = RT ln(Q/K) (kJ/mol)', lambda v: f'{v:g}', lambda v: neg(f'{v:g}')))
    o.append(L(x0, fy(0), x1, fy(0), INK, 1.6))
    dG = lambda x: RT * math.log(4 * x * x / (1 - x * x) / 0.222) / 1000
    o.append(curve(dG, 0.046, 0.5, fx, fy, n=100, c=AC, w=3))
    for xx, col, lab, dy, anc in ((0.10, NX, 'ξ = 0.10: Q = 0.0404, −5.67 kJ', 22, 'start'), (0.30, LV, 'ξ = 0.30: Q = 0.396, +1.92 kJ', -14, 'end')):
        o.append(C(fx(xx), fy(dG(xx)), 6, col))
        o.append(Tb(fx(xx) + (12 if anc == 'start' else -12), fy(dG(xx)) + dy, lab, 13, anc, col, bold=True))
    o.append(C(fx(0.2293), fy(0), 7, AC))
    o.append(Tb(fx(0.2293) + 12, fy(0) + 22, 'ΔG = 0 at ξ = 0.2293', 13, 'start', AC, bold=True))
    o.append(T(fx(0.12), fy(-10.5), 'ΔG < 0: forward', 13, 'middle', MUT))
    o.append(T(fx(0.43), fy(1.2), 'ΔG > 0: back', 13, 'middle', MUT))
    o.append(boxt(526, 40, 186, 150, ['A ⇌ 2B, 400 K', 'K = 0.222', 'RT = 3325.6 J/mol', 'conversion 0.229', 'yield 0.459 mol B', 'per mol A fed'], PANEL, AC, 13, bold_first=True))
    o.append(boxt(526, 206, 186, 150, ['A → D and A → U', '10.0 mol A fed', 'X = 0.70', 'Y = 0.50 (0.714', 'on A converted)', 'S = 2.5 mol D/mol U'], NXS, NX, 13, bold_first=True))
    return 420, ''.join(o)
FIG[6] = (f6, 'The worked direction test for A ⇌ 2B at 400 K: ΔG = RT ln(Q/K) is −5.67 kJ/mol at ξ = 0.10, so the mixture reacts forward, and +1.92 kJ/mol at ξ = 0.30, so it reacts back. ΔG crosses zero at ξ = 0.2293, conversion 0.229. The lower box repeats the yield and selectivity example.',
          'Delta G against extent: a curve rising from about minus 12 kilojoules near extent 0.05 through minus 5.67 at 0.10, zero at 0.2293 and plus 1.92 at 0.30 to about plus 6 at 0.5, with forward and back regions labelled and boxes for conversion, yield and selectivity.')


# ---- pressure and inerts ----
def f7():
    o = []
    # left: A ⇌ 2B
    x0, x1, y0, y1 = 70, 330, 50, 350
    fx = lambda p: x0 + (p - 0.4) / 1.8 * (x1 - x0)
    fy = lambda x: y1 - x / 0.4 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0.5, 1.0, 1.5, 2.0], [0, 0.1, 0.2, 0.3, 0.4], fx, fy,
                  'P (bar), A ⇌ 2B, 400 K', 'conversion of A', lambda v: f'{v:g}', lambda v: f'{v:.1f}'))
    K = 0.222
    o.append(curve(lambda p: math.sqrt(K / (4 * p + K)), 0.4, 2.2, fx, fy, c=AC, w=3))
    for p, X in ((0.5, 0.316), (1.0, 0.229), (2.0, 0.164)):
        o.append(C(fx(p), fy(X), 6, AC))
        o.append(Tb(fx(p) + 10, fy(X) - 10, f'{X:.3f}', 13, 'start', AC, bold=True))
    o.append(C(fx(1.0), fy(0.299), 6, NX))
    o.append(Tb(fx(1.0) + 10, fy(0.299) - 12, '+1 mol inert: 0.299', 13, 'start', NX, bold=True))
    o.append(T((x0 + x1) / 2, fy(0.04), 'Σν = +1: pressure lowers X', 13, 'middle', MUT))
    # right: ammonia, log P
    u0, u1 = 420, 690
    gx = lambda p: u0 + math.log10(p) / math.log10(200) * (u1 - u0)
    gy = lambda x: y1 - x * (y1 - y0)
    o.append(L(u0, y1, u1, y1, L2, 1.5)); o.append(L(u0, y0, u0, y1, L2, 1.5))
    for p in (1, 10, 50, 200):
        X = gx(p); o.append(L(X, y1, X, y1 + 5, L2, 1.5)); o.append(T(X, y1 + 20, str(p), 13, fill=MUT))
    for v in (0, 0.2, 0.4, 0.6, 0.8, 1.0):
        Y = gy(v); o.append(L(u0 - 5, Y, u0, Y, L2, 1.5)); o.append(L(u0, Y, u1, Y, LN, 1)); o.append(T(u0 - 9, Y + 4.5, f'{v:.1f}', 13, 'end', MUT))
    o.append(T((u0 + u1) / 2, y1 + 40, 'P (bar, log scale), NH₃, 500 K', 14, fill=MUT))
    o.append(T(u0, y0 - 12, 'conversion of N₂', 14, 'start', MUT))
    f = lambda P: (lambda x: 16 * x * x * (2 - x) ** 2 / (27 * (1 - x) ** 4) - 0.1 * P * P)
    ps = [10 ** (i / 40 * math.log10(200)) for i in range(41)]
    o.append(P([(gx(p), gy(bis(f(p), 1e-6, 0.9999))) for p in ps], LV, 3))
    o.append(f'<circle cx="{gx(100):.1f}" cy="{gy(0.832):.1f}" r="11" style="fill:none;stroke:{NX};stroke-width:2.5"/>')
    for p, X, dx, dy, anc in ((1, 0.158, 10, -10, 'start'), (10, 0.558, -10, -10, 'end'), (50, 0.785, -10, -10, 'end'), (100, 0.846, 12, 28, 'start'), (200, 0.890, -10, -12, 'end')):
        o.append(C(gx(p), gy(X), 6, LV))
        o.append(Tb(gx(p) + dx, gy(X) + dy, f'{X:.3f}', 13, anc, LV, bold=True))
    o.append(Tb(gx(100) - 14, gy(0.832) + 34, 'ring: 10 % Ar, 0.832', 13, 'end', NX, bold=True))
    o.append(T((u0 + u1) / 2 + 20, gy(0.12), 'Σν = −2: pressure raises X', 13, 'middle', MUT))
    return 420, ''.join(o)
FIG[7] = (f7, 'Both worked examples on pressure. Left: A ⇌ 2B makes gas, so its conversion falls from 0.316 at 0.5 bar to 0.229 at 1 bar and 0.164 at 2 bar, and an inert (1 mol at 1 bar) raises it to 0.299. Right: ammonia synthesis at 500 K (K = 0.100) loses gas, so conversion rises from 0.158 at 1 bar to 0.846 at 100 bar; 10 % argon cuts it to 0.832.',
          'Two plots. Left: conversion of A against pressure, a falling curve through 0.316 at 0.5 bar, 0.229 at 1 bar and 0.164 at 2 bar, with an extra point 0.299 for added inert. Right: conversion of nitrogen against pressure on a log scale, a rising curve through 0.158 at 1 bar, 0.558 at 10, 0.785 at 50, 0.846 at 100 and 0.890 at 200 bar, with 0.832 marked for 10 percent argon.')


# ---- multireaction, heterogeneous and the reacting phase rule ----
def f8():
    o = []
    x0, x1, y0, y1 = 70, 330, 50, 350
    fy = lambda y: y1 - y / 0.7 * (y1 - y0)
    o.append(L(x0, y1, x1, y1, L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    for v in (0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7):
        Y = fy(v); o.append(L(x0 - 5, Y, x0, Y, L2, 1.5)); o.append(L(x0, Y, x1, Y, LN, 1)); o.append(T(x0 - 9, Y + 4.5, f'{v:.1f}', 13, 'end', MUT))
    o.append(T(x0, y0 - 12, 'equilibrium mole fraction', 14, 'start', MUT))
    for i, (nm, y, n, col, fl) in enumerate((('A', 0.3166, '0.3015', AC, ACS), ('B', 0.6332, '0.6030', LV, LVS), ('C', 0.0501, '0.0477', NX, NXS))):
        bx = x0 + 25 + i * 82
        o.append(R(bx, fy(y), 56, y1 - fy(y), fl, col, 3, 2))
        o.append(T(bx + 28, fy(y) - 8, f'{y:.3f}', 13, 'middle', col, bold=True))
        o.append(T(bx + 28, y1 + 20, nm, 14, 'middle', INK, bold=True))
        o.append(T(bx + 28, y1 + 40, n + ' mol', 12, 'middle', MUT))
    o.append(boxt(360, 40, 350, 96, ['two reactions from 1 mol A at 1 bar', 'A ⇌ B, K₁ = 2.00;  2A ⇌ C, K₂ = 0.500', 'ξ₁ = 0.603 mol, ξ₂ = 0.0477 mol'], PANEL, AC, 14, bold_first=True))
    o.append(boxt(360, 148, 350, 100, ['heterogeneous: CaCO₃(s) ⇌ CaO(s) + CO₂(g)', 'both solids have activity 1, so', 'K = a(CO₂) = y(CO₂)P/P°', 'the solids never enter K'], LVS, LV, 14, bold_first=True))
    o.append(boxt(360, 260, 350, 100, ['reacting phase rule: F = N − π + 2 − r', 'steam reforming, one gas phase:', 'N = 5, π = 1, r = 2', 'F = 5 − 1 + 2 − 2 = 4'], NXS, NX, 14, bold_first=True))
    return 420, ''.join(o)
FIG[8] = (f8, 'The worked multireaction example: with K₁ = 2.00 and K₂ = 0.500, 1 mol A settles at ξ₁ = 0.603 and ξ₂ = 0.0477 mol, giving mole fractions 0.317, 0.633 and 0.050. The boxes show why solids drop out of K for calcination and how the reacting phase rule gives F = 4 for steam reforming.',
          'Bar chart of equilibrium mole fractions: A 0.317, B 0.633, C 0.050, with mole numbers below, and a box with the two equilibrium constants and extents; on the right, a box for calcium carbonate decomposition where K equals the CO2 activity, and a box for the reacting phase rule giving F = 4 for steam reforming.')


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
