"""Claude's hand-drawn figures for ec-circuits-u4 (resonance and coupled circuits), one per chapter. Every number comes
from that chapter's own worked example. Colours are the shell's CSS variables."""
import os, sys, math, cmath
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
PI = math.pi


# ---- circuit symbols ----
def res_h(x1, x2, y, c=INK, n=6, a=7):
    """zigzag resistor from x1 to x2 at height y, with short leads"""
    lead = (x2 - x1) * 0.2
    xs = x1 + lead; xe = x2 - lead; st = (xe - xs) / (2 * n)
    pts = [(x1, y), (xs, y)] + [(xs + st * (2 * i + 1), y + (a if i % 2 == 0 else -a)) for i in range(n)] + [(xe, y), (x2, y)]
    return P(pts, c, 2)


def res_v(x, y1, y2, c=INK, n=6, a=7):
    lead = (y2 - y1) * 0.2
    ys = y1 + lead; ye = y2 - lead; st = (ye - ys) / (2 * n)
    pts = [(x, y1), (x, ys)] + [(x + (a if i % 2 == 0 else -a), ys + st * (2 * i + 1)) for i in range(n)] + [(x, ye), (x, y2)]
    return P(pts, c, 2)


def ind_h(x1, x2, y, c=INK, n=4, up=True):
    r = (x2 - x1) / (2 * n); s = 1 if up else 0
    d = f'M{x1:.1f},{y:.1f} ' + ' '.join(f'a{r:.1f},{r:.1f} 0 0 {s} {2 * r:.1f},0' for _ in range(n))
    return f'<path d="{d}" style="fill:none;stroke:{c};stroke-width:2"/>'


def ind_v(x, y1, y2, c=INK, n=4, right=True):
    r = (y2 - y1) / (2 * n); s = 1 if right else 0
    d = f'M{x:.1f},{y1:.1f} ' + ' '.join(f'a{r:.1f},{r:.1f} 0 0 {s} 0,{2 * r:.1f}' for _ in range(n))
    return f'<path d="{d}" style="fill:none;stroke:{c};stroke-width:2"/>'


def cap_v(x, y1, y2, c=INK, gap=8, w=22):
    m = (y1 + y2) / 2
    return L(x, y1, x, m - gap / 2, c, 2) + L(x - w / 2, m - gap / 2, x + w / 2, m - gap / 2, c, 2.5) + \
        L(x - w / 2, m + gap / 2, x + w / 2, m + gap / 2, c, 2.5) + L(x, m + gap / 2, x, y2, c, 2)


def src(x, y, r=17, c=INK):
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:var(--fig);stroke:{c};stroke-width:2"/>'
            f'<path d="M{x - 9:.1f},{y:.1f} q4.5,-9 9,0 t9,0" style="fill:none;stroke:{c};stroke-width:2"/>')


def dot(x, y, c=INK, r=4.5):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{c}"/>'


def W(*pts, c=INK):
    return P(list(pts), c, 2)


def ph(x0, y0, x1, y1, c=AC, w=3, arrow='n'):
    """a phasor arrow"""
    return L(x0, y0, x1, y1, c, w, arrow=arrow)


# ---- 4.1: the current of the worked example circuit, and its phasors at resonance ----
def f1():
    o = []
    L_, C_, V = 10e-3, 1e-6, 10.0
    X0, X1, Y0, Y1 = 62, 424, 36, 236
    fx = lambda f: X0 + (X1 - X0) * (f - 1000) / 1200
    fy = lambda i: Y1 - (Y1 - Y0) * i / 1.1
    o.append(axes(X0, X1, Y0, Y1, [1000, 1300, 1600, 1900, 2200], [0, 0.5, 0.707, 1], fx, fy, 'f (Hz)', 'I (A)',
                  lambda v: f'{v:g}', lambda v: f'{v:g}'))
    fs = [1000 + i * 3 for i in range(401)]
    cur = lambda f, R: V / abs(complex(R, 2 * PI * f * L_ - 1 / (2 * PI * f * C_)))
    o.append(P([(fx(f), fy(cur(f, 20))) for f in fs], LV, 2.5))
    o.append(P([(fx(f), fy(cur(f, 10))) for f in fs], AC, 3))
    f1_, f2_ = 1513.96, 1673.11
    o.append(L(fx(f1_), fy(0.707), fx(f2_), fy(0.707), NX, 2.5))
    o += [L(fx(f), fy(0.707), fx(f), Y1, NX, 1.5, '4 3') for f in (f1_, f2_)]
    o.append(Tb(fx(1593), fy(0.707) + 22, 'BW = 159 Hz', 13, fill=NX, bold=True))
    o.append(Tb(fx(1730), fy(0.97), 'R = 10 Ω, Q = 10', 13, 'start', AC, bold=True))
    o.append(Tb(fx(1800), fy(0.50), 'R = 20 Ω, Q = 5', 13, 'start', LV, bold=True))
    o.append(Tb(fx(1591.5), fy(1.0) - 10, 'f₀ = 1591.5 Hz', 13))
    # phasors at resonance, all from one origin (1 px per volt for V_L, V_C; V_R drawn 7x)
    ox, oy = 530, 150
    sub = lambda t, b: t.replace(b, b[0] + f'<tspan baseline-shift="sub" font-size="10">{b[2:]}</tspan>')
    o.append(L(470, oy, 700, oy, L2, 1.5))
    o.append(ph(ox, oy, ox, oy - 88, NX, 3, 'x'))
    o.append(ph(ox, oy, ox, oy + 88, AC, 3, 'n'))
    o.append(ph(ox, oy, ox + 70, oy, LV, 3.5, 'l'))
    o.append(L(ox, oy + 12, ox + 120, oy + 12, MUT, 1.8, arrow='m'))
    o.append(T(ox + 126, oy + 17, 'I = 1 A', 13, 'start', MUT))
    o.append(T(ox + 10, oy - 70, sub('V_L = 100 V', 'V_L'), 13, 'start', NX, bold=True))
    o.append(T(ox + 10, oy + 82, sub('V_C = 100 V', 'V_C'), 13, 'start', AC, bold=True))
    o.append(T(ox + 76, oy - 8, sub('V_R = 10 V', 'V_R'), 13, 'start', LV, bold=True))
    o.append(T(590, 30, 'phasors at f₀', 14, bold=True))
    o.append(T(650, 116, 'equal and', 13, 'middle', MUT))
    o.append(T(650, 134, 'opposite', 13, 'middle', MUT))
    return 290, ''.join(o)


FIG[1] = (f1, 'Left: current against frequency for the worked example (L = 10 mH, C = 1 µF, 10 V). With R = 10 Ω the peak is 1 A at 1591.5 Hz and the half-power band is 159 Hz wide; doubling R to 20 Ω halves the peak and doubles the band. Right: at resonance V_L and V_C are each 100 V, ten times the source, and cancel.',
          'Resonance curves of current against frequency for R equal to 10 and 20 ohms, with the half-power band marked, and a phasor diagram of V R, V L and V C at resonance.')


# ---- 4.2: |Z| of the ideal tank, and the branch currents of the practical tank ----
def f2():
    o = []
    R, L_, C_ = 1000.0, 10e-3, 1e-6
    X0, X1, Y0, Y1 = 66, 404, 36, 236
    fx = lambda f: X0 + (X1 - X0) * (f - 1000) / 1200
    fy = lambda z: Y1 - (Y1 - Y0) * z / 1100
    o.append(axes(X0, X1, Y0, Y1, [1000, 1300, 1600, 1900, 2200], [0, 500, 707, 1000], fx, fy, 'f (Hz)', '|Z| (Ω)',
                  lambda v: f'{v:g}', lambda v: f'{v:g}'))
    fs = [1000 + i * 3 for i in range(401)]
    z = lambda f: 1 / abs(complex(1 / R, 2 * PI * f * C_ - 1 / (2 * PI * f * L_)))
    o.append(P([(fx(f), fy(z(f))) for f in fs], AC, 3))
    for f in (1513.96, 1673.11):
        o.append(L(fx(f), fy(707), fx(f), Y1, NX, 1.5, '4 3'))
    o.append(L(fx(1513.96), fy(707), fx(1673.11), fy(707), NX, 2.5))
    o.append(Tb(fx(1593), fy(707) + 22, '159 Hz', 13, fill=NX, bold=True))
    o.append(Tb(fx(1591.5), fy(1000) - 10, '1 kΩ at f₀ = 1591.5 Hz', 13))
    o.append(T(fx(1840), fy(820), 'R = 1 kΩ, Q = 10', 13, 'start', AC, bold=True))
    # phasors of the practical tank (scale 1 px per mA)
    ox, oy = 470, 150
    o.append(L(452, oy, 706, oy, L2, 1.5))
    o.append(T(700, oy - 8, 'V', 14, 'end', MUT, bold=True))
    ang = math.radians(84.26)
    o.append(ph(ox, oy, ox, oy - 99.5, NX, 3, 'x'))
    o.append(ph(ox, oy, ox + 100 * math.cos(ang), oy + 100 * math.sin(ang) - 0, LV, 3, 'l'))
    o.append(ph(ox, oy, ox + 10 * 5, oy, AC, 3.5, 'n'))
    o.append(T(ox + 12, oy - 84, 'I_C = 99.5 mA', 13, 'start', NX).replace('I_C', 'I<tspan baseline-shift="sub" font-size="10">C</tspan>'))
    o.append(T(ox + 20, oy + 90, 'I_coil = 100 mA, 84.3° lag', 13, 'start', LV).replace('I_coil', 'I<tspan baseline-shift="sub" font-size="10">coil</tspan>'))
    o.append(Tb(ox + 60, oy - 12, 'I_s = 10 mA', 13, 'start', AC).replace('I_s', 'I<tspan baseline-shift="sub" font-size="10">s</tspan>'))
    o.append(T(580, 30, 'practical tank at f₀ = 1583.6 Hz', 14, bold=True))
    o.append(T(588, 272, '(lengths: 1 px per mA; I_s drawn 5× longer)', 13, fill=MUT).replace('I_s', 'I<tspan baseline-shift="sub" font-size="10">s</tspan>'))
    return 290, ''.join(o)


FIG[2] = (f2, 'Left: the impedance of the ideal tank of the first example (R = 1 kΩ, L = 10 mH, C = 1 µF) peaks at 1 kΩ at f₀ and falls to 707 Ω at the half-power points, 159 Hz apart. Right: in the practical tank of the second example the coil and capacitor currents of about 100 mA nearly cancel, leaving 10 mA from the supply in phase with V.',
          'Impedance magnitude of a parallel RLC tank against frequency peaking at 1 kilo-ohm, and a phasor diagram with the capacitor current 99.5 milliamps leading, the coil current 100 milliamps lagging 84 degrees, and the supply current 10 milliamps in phase.')


# ---- 4.3: the effect of Q, normalised current for R = 5, 10, 20 and 40 ohms ----
def f3():
    o = []
    X0, X1, Y0, Y1 = 66, 700, 40, 250
    fx = lambda f: X0 + (X1 - X0) * (f - 1000) / 1200
    fy = lambda v: Y1 - (Y1 - Y0) * v / 1.08
    o.append(axes(X0, X1, Y0, Y1, [1000, 1200, 1400, 1600, 1800, 2000, 2200], [0, 0.5, 0.707, 1], fx, fy, 'f (Hz)', 'I / I₀',
                  lambda v: f'{v:g}', lambda v: f'{v:g}'))
    f0 = 1591.549
    fs = [1000 + i * 2 for i in range(601)]
    cols = {20: AC, 10: NX, 5: LV, 2.5: MUT}
    for Q in (2.5, 5, 10, 20):
        o.append(P([(fx(f), fy(1 / math.sqrt(1 + Q * Q * (f / f0 - f0 / f) ** 2))) for f in fs], cols[Q], 3 if Q == 10 else 2.2))
    o.append(L(X0, fy(0.707), X1, fy(0.707), MUT, 1.2, '5 4'))
    for f in (1513.96, 1673.11):
        o.append(L(fx(f), fy(0.707), fx(f), Y1, NX, 1.5, '4 3'))
    o.append(Tb(fx(1593), Y1 - 14, 'Q = 10: 1514 to 1673 Hz', 13, fill=NX, bold=True))
    o.append(Tb(fx(1592), fy(1.0) - 10, 'f₀ = 1591.5 Hz for every R', 13))
    o.append(R(80, 42, 124, 82, FIGBG, L2, 6, 1))
    for i, Q in enumerate((20, 10, 5, 2.5)):
        y = 58 + i * 19
        o.append(L(88, y - 4, 108, y - 4, cols[Q], 3))
        o.append(T(114, y, f'Q = {Q:g} ({[5, 10, 20, 40][i]} Ω)', 13, 'start', cols[Q], bold=True))
    return 300, ''.join(o)


FIG[3] = (f3, 'The same L = 10 mH and C = 1 µF with four values of R, each curve divided by its own peak I₀ = V/R. Every curve peaks at 1591.5 Hz, but the band between the half-power points widens from 80 Hz at Q = 20 to 637 Hz at Q = 2.5; the Q = 10 band is the 159 Hz of the second worked example.',
          'Four normalised resonance curves for Q equal to 20, 10, 5 and 2.5, all peaking at 1591.5 hertz, with the 0.707 line and the Q equals 10 half-power frequencies 1514 and 1673 hertz marked.')


# ---- 4.4: first-order Bode magnitudes, and the band-pass of part (c) ----
def f4():
    o = []
    fc = 1591.55
    X0, X1, Y0, Y1 = 58, 352, 58, 240
    lx = lambda f: X0 + (X1 - X0) * (math.log10(f) - 2) / 3          # 100 Hz .. 100 kHz
    fy = lambda d: Y0 + (Y1 - Y0) * (-d) / 40                        # 0 .. -40 dB
    o.append(axes(X0, X1, Y0, Y1, [100, 1000, 10000, 100000], [0, -20, -40], lx, fy, 'f (Hz), log scale', 'gain (dB)',
                  lambda v: {100: '100', 1000: '1k', 10000: '10k', 100000: '100k'}[v], lambda v: neg(f'{v:g}')))
    fs = [10 ** (2 + i * 0.01) for i in range(301)]
    lp = lambda f: -10 * math.log10(1 + (f / fc) ** 2)
    hp = lambda f: -10 * math.log10(1 + (fc / f) ** 2)
    o.append(P([(lx(f), fy(max(lp(f), -40))) for f in fs], AC, 3))
    o.append(P([(lx(f), fy(max(hp(f), -40))) for f in fs], LV, 3))
    o.append(L(lx(fc), fy(-3), lx(fc), Y1, NX, 1.5, '4 3'))
    o.append(C(lx(fc), fy(-3), 5, NX))
    o.append(Tb(lx(fc), Y1 - 12, 'f_c = 1591.5 Hz', 13, fill=NX, bold=True).replace('f_c', 'f<tspan baseline-shift="sub" font-size="10">c</tspan>'))
    o.append(Tb(lx(30000), fy(-28), 'low-pass', 13, fill=AC, bold=True))
    o.append(Tb(lx(30000), fy(-36), '−20 dB/decade', 13, fill=AC))
    o.append(Tb(lx(330), fy(-30), 'high-pass', 13, fill=LV, bold=True))
    o.append(Tb(lx(fc) + 6, fy(-3) + 18, '−3 dB', 13, 'start', NX, bold=True))
    o.append(T((X0 + X1) / 2, 22, 'RC, R = 1 kΩ, C = 100 nF', 14, bold=True))
    # band-pass, f0 = 1 kHz, Q = 10
    B0, B1 = 424, 700
    bx = lambda f: B0 + (B1 - B0) * (f - 700) / 600
    by = lambda v: Y1 - (Y1 - Y0) * v / 1.1
    o.append(axes(B0, B1, Y0, Y1, [700, 1000, 1300], [0, 0.263, 0.707, 1], bx, by, 'f (Hz)', '|H|', lambda v: f'{v:g}', lambda v: f'{v:g}'))
    bp = lambda f: 1 / math.sqrt(1 + 100 * (f / 1000 - 1000 / f) ** 2)
    o.append(P([(bx(f), by(bp(f))) for f in [700 + i * 1.5 for i in range(401)]], AC, 3))
    o.append(L(bx(951.25), by(0.707), bx(1051.25), by(0.707), NX, 2.5))
    o.append(Tb(bx(1001), by(0.707) + 20, 'BW = 100 Hz', 13, fill=NX, bold=True))
    o.append(C(bx(1200), by(0.263), 5, LV))
    o.append(Tb(bx(1200) - 4, by(0.263) + 24, '1.2 kHz: 0.263', 13, 'middle', LV, bold=True))
    o.append(T((B0 + B1) / 2, 22, 'series RLC, f₀ = 1 kHz, Q = 10', 14, bold=True))
    return 300, ''.join(o)


FIG[4] = (f4, 'Left: the RC low-pass and high-pass of the worked example on a log frequency axis; both are 3 dB down at f_c = 1591.5 Hz, and the low-pass falls 20 dB per decade above it (−1.44 dB at 1 kHz). Right: the band-pass of part (c) peaks at 1 at 1 kHz, is 100 Hz wide at the 0.707 level and passes only 0.263 at 1.2 kHz.',
          'Bode magnitude plot of an RC low-pass and high-pass crossing minus 3 decibels at 1591.5 hertz, and a series RLC band-pass response peaking at 1 kilohertz with a 100 hertz half-power band.')


# ---- 4.5: the current loci of the two worked examples ----
def f5():
    o = []
    # left: series RL, X_L = 10 ohm, R varied, V = 100 V; scale 17 px per A
    s = 17.0
    ox, oy = 70, 62
    X = lambda a: ox + a * s
    Y = lambda b: oy - b * s
    o.append(L(ox - 20, oy, ox + 230, oy, L2, 1.5, arrow='m'))
    o.append(L(ox, oy - 18, ox, Y(-10.9), L2, 1.5))
    o.append(T(ox + 226, oy - 8, 'V', 14, 'end', MUT, bold=True))
    o.append(f'<path d="M{X(0):.1f},{Y(-10):.1f} A{5 * s:.1f},{5 * s:.1f} 0 0 0 {X(0):.1f},{Y(0):.1f}" style="fill:none;stroke:{AC};stroke-width:3"/>')
    o.append(L(X(0), Y(-10), X(0), Y(0), AC, 1.2, '4 3'))
    pts = [(0, 0, -10), (5, 4, -8), (10, 5, -5), (20, 4, -2), (40, 2.353, -0.588)]
    for R, a, b in pts:
        o.append(C(X(a), Y(b), 5, NX))
    o.append(ph(X(0), Y(0), X(5) - 4, Y(-5) - 4, NX, 2.2, 'x'))
    lab = [(0, 'R = 0: 10 A', 'start', 10, 4), (5, 'R = 5: 8.94 A', 'start', 10, 4), (10, 'R = 10: 7.07 A, 500 W', 'start', 10, 4),
           (20, 'R = 20: 4.47 A', 'start', 10, 12), (40, 'R = 40: 2.43 A', 'start', 10, -6)]
    for (R, a, b), (_, t, an, dx, dy) in zip(pts, lab):
        o.append(Tb(X(a) + dx, Y(b) + dy, t, 13, an))
    o.append(Tb(X(0) - 8, Y(-5) + 4, '10 A', 13, 'end', MUT))
    o.append(T(170, 28, 'RL, X_L = 10 Ω, R varied', 14, bold=True).replace('X_L', 'X<tspan baseline-shift="sub" font-size="10">L</tspan>'))
    # right: coil R = 3 ohm with X_L varied, || X_C = 10 ohm; scale 7 px per A
    q = 6.6
    px, py = 420, 176
    U = lambda a: px + a * q
    Vv = lambda b: py - b * q
    o.append(L(px - 16, py, 708, py, L2, 1.5, arrow='m'))
    o.append(L(px, Vv(12), px, Vv(-17), L2, 1.5))
    o.append(T(704, py + 20, 'V', 14, 'end', MUT, bold=True))
    D = 100 / 3
    o.append(f'<path d="M{U(0):.1f},{Vv(0):.1f} A{D / 2 * q:.1f},{D / 2 * q:.1f} 0 0 0 {U(D):.1f},{Vv(0):.1f}" style="fill:none;stroke:{LV};stroke-width:2.2;stroke-dasharray:6 4"/>')
    o.append(f'<path d="M{U(0):.1f},{Vv(10):.1f} A{D / 2 * q:.1f},{D / 2 * q:.1f} 0 0 0 {U(D):.1f},{Vv(10):.1f}" style="fill:none;stroke:{AC};stroke-width:3"/>')
    o.append(ph(U(0), Vv(0), U(0), Vv(10) + 3, NX, 2.2, 'x'))
    o.append(T(U(0) + 8, Vv(10) + 2, 'I_C = 10 A', 13, 'start', NX).replace('I_C', 'I<tspan baseline-shift="sub" font-size="10">C</tspan>'))
    for a in (10 / 3, 30):
        o.append(C(U(a), Vv(0), 5.5, NX))
    o.append(Tb(U(10 / 3) + 4, Vv(0) + 22, '3.33 A', 13, 'start', NX, bold=True))
    o.append(Tb(U(30) - 2, Vv(0) + 22, '30 A', 13, 'middle', NX, bold=True))
    o.append(T(U(D / 2), Vv(-D / 2 + 10) + 20, 'total current', 13, fill=AC, bold=True))
    o.append(T(U(D / 2), Vv(-14), 'coil current alone', 13, fill=LV))
    o.append(T(560, 28, 'coil 3 Ω, X_L varied, X_C = 10 Ω', 14, bold=True).replace('X_L', 'X<tspan baseline-shift="sub" font-size="10">L</tspan>').replace('X_C', 'X<tspan baseline-shift="sub" font-size="10">C</tspan>'))
    o.append(T(560, 48, 'resonant where it cuts the V axis', 13, fill=MUT))
    return 300, ''.join(o)


FIG[5] = (f5, 'Left: the first worked example. With X_L = 10 Ω and 100 V, the current tip runs round a semicircle of diameter 10 A below V as R rises; the right-most point, R = 10 Ω, gives the maximum power of 500 W. Right: the second example. The coil current circle (dashed) moves up by the 10 A capacitor current and cuts the V axis at 3.33 A and 30 A, the two resonant settings.',
          'Two current locus diagrams: a semicircle of diameter 10 amps for a series RL circuit with variable resistance, with points for R equal to 0, 5, 10, 20 and 40 ohms, and a coil current circle shifted up by 10 amps that crosses the voltage axis at 3.33 and 30 amps.')


# ---- 4.6: flux of coil 1 shared with coil 2 ----
def f6():
    o = []
    # two coil blocks on one axis
    o.append(R(150, 96, 150, 100, PANEL, AC, 10))
    o.append(R(430, 96, 150, 100, PANEL, LV, 10))
    for i in range(6):
        x = 166 + i * 23
        o.append(L(x, 96, x + 12, 196, AC, 2.2))
    for i in range(3):
        x = 456 + i * 40
        o.append(L(x, 96, x + 16, 196, LV, 2.2))
    o.append(T(225, 86, 'coil 1: L₁ = 4 H', 14, bold=True, fill=AC))
    o.append(T(505, 86, 'coil 2: L₂ = 1 H', 14, bold=True, fill=LV))
    # mutual flux loop (passes through both)
    o.append(f'<path d="M120,146 L612,146" style="fill:none;stroke:{NX};stroke-width:2.5" marker-end="url(#ar-UID-x)"/>')
    o.append(f'<path d="M612,146 C690,146 690,262 560,262 L170,262 C50,262 50,146 120,146" style="fill:none;stroke:{NX};stroke-width:2.5"/>')
    o.append(Tb(365, 266, 'mutual flux Φ₂₁: links both coils', 13, fill=NX, bold=True))
    # leakage loop round coil 1 only
    o.append(f'<path d="M150,128 C120,40 330,40 300,128" style="fill:none;stroke:{MUT};stroke-width:2;stroke-dasharray:5 4" marker-end="url(#ar-UID-m)"/>')
    o.append(T(225, 40, 'leakage flux: coil 1 only', 13, fill=MUT))
    # current into coil 1
    o.append(L(70, 196, 150, 196, AC, 2.5, arrow='n'))
    o.append(Tb(24, 180, 'di₁/dt = 2 A/s', 13, 'start', AC, bold=True))
    o.append(T(215, 228, 'e₁ = L₁ di₁/dt = 8 V', 13, fill=AC))
    o.append(T(505, 228, 'e₂ = M di₁/dt = 2 V', 13, fill=LV))
    o.append(boxt(318, 204, 92, 42, ['k = 0.5', 'M = 1 H'], FIGBG, L2, 13))
    return 290, ''.join(o)


FIG[6] = (f6, 'Coil 1 (L₁ = 4 H) and coil 2 (L₂ = 1 H) with k = 0.5, so M = 1 H. Part of coil 1\'s flux links coil 2 (the mutual flux) and the rest leaks round coil 1 alone. When i₁ changes at 2 A/s, coil 1 has a self-induced 8 V and coil 2 a mutual 2 V.',
          'Two coils on one axis. A mutual flux loop passes through both coils and a leakage loop circles coil 1 only. Labels give L1 equal to 4 henry, L2 equal to 1 henry, k equal to 0.5, M equal to 1 henry, e1 equal to 8 volts and e2 equal to 2 volts.')


# ---- 4.7: series aiding and opposing, and the coupled mesh of the second example ----
def f7():
    o = []
    # left: aiding and opposing series pairs
    for row, (yy, lab, d2, val) in enumerate([(64, 'aiding: current enters both dots', 'left', 'L_eq = 2 + 3 + 2(1) = 7 H'),
                                             (196, 'opposing: enters one, leaves the other', 'right', 'L_eq = 2 + 3 − 2(1) = 3 H')]):
        o.append(T(150, yy - 34, lab, 13, fill=MUT))
        o.append(L(20, yy, 46, yy, INK, 2))
        o.append(ind_h(46, 126, yy))
        o.append(L(126, yy, 166, yy, INK, 2))
        o.append(ind_h(166, 246, yy))
        o.append(L(246, yy, 280, yy, INK, 2))
        o.append(dot(52, yy - 14))
        o.append(dot(172 if d2 == 'left' else 240, yy - 14))
        o.append(L(22, yy + 12, 44, yy + 12, AC, 2, arrow='n'))
        o.append(T(86, yy + 30, 'L₁ = 2 H', 13))
        o.append(T(206, yy + 30, 'L₂ = 3 H', 13))
        o.append(T(150, yy + 52, val, 13, bold=True, fill=AC).replace('L_eq', 'L<tspan baseline-shift="sub" font-size="10">eq</tspan>'))
    o.append(T(150, 286, 'M = 1 H for both', 13, fill=MUT))
    # right: the two-mesh circuit
    xl, xa, xb, xr, yt, yb = 338, 448, 548, 690, 66, 226
    o.append(src(xl, (yt + yb) / 2))
    o.append(W((xl, (yt + yb) / 2 - 17), (xl, yt), (360, yt)))
    o.append(res_h(360, 420, yt))
    o.append(W((420, yt), (xa, yt), (xa, 106)))
    o.append(ind_v(xa, 106, 186, right=True))
    o.append(W((xa, 186), (xa, yb), (xl, yb), (xl, (yt + yb) / 2 + 17)))
    o.append(W((xb, 106), (xb, yt), (xr, yt), (xr, 116)))
    o.append(ind_v(xb, 106, 186, right=False))
    o.append(res_v(xr, 116, 176))
    o.append(W((xr, 176), (xr, yb), (xb, yb), (xb, 186)))
    o.append(dot(xa - 14, 112))
    o.append(dot(xb - 14, 112))
    o.append(T(xl, yb + 22, '100∠0° V', 13))
    o.append(T(390, yt - 12, '5 Ω', 13))
    o.append(T(xa - 16, 158, 'j10', 13, 'end'))
    o.append(T(xb + 16, 158, 'j20', 13, 'start'))
    o.append(T(xr - 14, 150, '10 Ω', 13, 'end'))
    o.append(Tb((xa + xb) / 2, 92, 'ωM = 5 Ω', 13, fill=NX, bold=True))
    o.append(arc(380, 196, 400, 112, -0.45, AC, 2, 'n'))
    o.append(T(392, 160, 'I₁', 14, fill=AC, bold=True))
    o.append(arc(600, 112, 620, 196, -0.45, LV, 2, 'l'))
    o.append(T(616, 160, 'I₂', 14, fill=LV, bold=True))
    o.append(T(514, 256, 'I₁ = 9.48∠−58.6° A, I₂ = 2.12∠−32.0° A', 13, bold=True))
    o.append(T(514, 278, 'I₁ enters a dot, I₂ leaves one: terms −j5', 13, fill=MUT))
    return 300, ''.join(o)


FIG[7] = (f7, 'Left: the series coils of the first worked example (L₁ = 2 H, L₂ = 3 H, M = 1 H); the dots and the current entry decide between 7 H and 3 H. Right: the coupled meshes of the second example, where I₁ enters the dot of coil 1 and I₂ leaves the dot of coil 2, so both mutual terms are −j5 Ω.',
          'Two series pairs of coupled coils with dots, labelled 7 henry for aiding and 3 henry for opposing, and a two-mesh circuit with a 100 volt source, 5 ohms, coupled coils j10 and j20 with omega M equal to 5 ohms, a 10 ohm load and the mesh currents I1 and I2.')


# ---- 4.8: the ideal transformer of the worked example ----
def f8():
    o = []
    # core
    o.append(R(270, 44, 180, 196, FIGBG, MUT, 6, 10))
    o.append(R(300, 70, 120, 140, 'var(--fig)', L2, 3, 1.5))
    # windings
    for i in range(5):
        y = 82 + i * 26
        o.append(f'<path d="M262,{y:.1f} q16,-8 16,6 q0,8 -16,6" style="fill:none;stroke:{AC};stroke-width:2.4"/>')
    for i in range(3):
        y = 100 + i * 34
        o.append(f'<path d="M458,{y:.1f} q-16,-8 -16,6 q0,8 16,6" style="fill:none;stroke:{LV};stroke-width:2.4"/>')
    o.append(W((262, 82), (200, 82)))
    o.append(W((262, 194), (200, 194)))
    o.append(W((458, 100), (540, 100), (600, 100), (600, 112)))
    o.append(res_v(600, 112, 172))
    o.append(W((600, 172), (600, 180), (458, 180)))
    o.append(dot(250, 72, AC))
    o.append(dot(470, 90, LV))
    # source side
    o.append(src(180, 138))
    o.append(W((200, 82), (180, 82), (180, 121)))
    o.append(W((180, 155), (180, 194), (200, 194)))
    o.append(T(150, 142, '230 V', 13, 'end', INK, bold=True))
    o.append(L(206, 62, 246, 62, AC, 2, arrow='n'))
    o.append(T(196, 56, 'I₁ = 0.92 A', 13, 'end', AC, bold=True))
    o.append(T(360, 262, 'N₁ = 500', 13, 'end', AC, bold=True))
    o.append(T(380, 262, 'N₂ = 100', 13, 'start', LV, bold=True))
    o.append(L(490, 84, 540, 84, LV, 2, arrow='l'))
    o.append(T(548, 70, 'I₂ = 4.6 A', 13, 'start', LV, bold=True))
    o.append(T(616, 146, 'Z_L = 10 Ω', 13, 'start').replace('Z_L', 'Z<tspan baseline-shift="sub" font-size="10">L</tspan>'))
    o.append(T(520, 140, 'V₂ = 46 V', 13, 'middle', LV, bold=True))
    o.append(T(360, 24, 'n = N₂/N₁ = 0.2', 14, bold=True))
    o.append(boxt(30, 220, 220, 50, ['seen from the 230 V side:', 'Z_in = 10/0.2² = 250 Ω'], PANEL, AC, 13).replace('Z_in', 'Z<tspan baseline-shift="sub" font-size="10">in</tspan>'))
    o.append(boxt(470, 220, 220, 50, ['power check:', '230 × 0.92 = 46 × 4.6 = 211.6 W'], PANEL, LV, 13))
    return 288, ''.join(o)


FIG[8] = (f8, 'The ideal transformer of the first worked example: 500 primary turns on 230 V and 100 secondary turns, so n = 0.2. The secondary gives 46 V and drives 4.6 A into the 10 Ω load; the primary draws only 0.92 A, and the load looks like 250 Ω from the supply.',
          'A transformer core with a 500-turn primary on a 230 volt source and a 100-turn secondary feeding a 10 ohm load, with dots, currents 0.92 and 4.6 amps, secondary voltage 46 volts and the referred impedance 250 ohms.')


# ---- 4.9: the gapped core and its reluctance circuit ----
def f9():
    o = []
    # core with a gap on the right limb
    o.append(f'<path d="M300,136 V50 H60 V230 H300 V148" style="fill:none;stroke:{MUT};stroke-width:22;stroke-linejoin:miter"/>')
    for i in range(5):
        y = 92 + i * 20
        o.append(f'<path d="M44,{y:.1f} q16,-8 32,0" style="fill:none;stroke:{AC};stroke-width:2.6"/>')
    o.append(f'<path d="M180,50 H300 V96" style="fill:none;stroke:{NX};stroke-width:2.5" marker-end="url(#ar-UID-x)"/>')
    o.append(T(200, 26, 'Φ = 0.279 mWb', 13, fill=NX, bold=True))
    o.append(T(100, 140, 'N = 500', 13, 'start', AC, bold=True))
    o.append(T(100, 158, 'I = 2 A', 13, 'start', AC, bold=True))
    o.append(Tb(330, 146, 'gap 1 mm', 13, 'start', INK, bold=True))
    o.append(T(180, 270, 'iron: l = 0.4 m, μr = 500, A = 4 cm²', 13).replace('μr', 'μ<tspan baseline-shift="sub" font-size="10">r</tspan>'))
    # reluctance circuit
    x0, x1, yt, yb = 460, 680, 70, 230
    o.append(boxt(x0 - 44, 124, 88, 40, ['F = NI', '1000 A'], PANEL, AC, 13))
    o.append(W((x0, 124), (x0, yt), (530, yt)))
    o.append(res_h(530, 620, yt))
    o.append(W((620, yt), (x1, yt), (x1, 120)))
    o.append(res_v(x1, 120, 190))
    o.append(W((x1, 190), (x1, yb), (x0, yb), (x0, 164)))
    o.append(T(575, 52, 'R_core = 1.59×10⁶ A/Wb', 13).replace('R_core', 'R<tspan baseline-shift="sub" font-size="10">core</tspan>'))
    o.append(T(575, 96, 'drop 444 A', 13, fill=MUT))
    o.append(T(x1 - 14, 128, 'R_gap', 13, 'end').replace('R_gap', 'R<tspan baseline-shift="sub" font-size="10">gap</tspan>'))
    o.append(T(x1 - 14, 152, '1.99×10⁶', 13, 'end'))
    o.append(T(x1 - 14, 172, 'drop 556 A', 13, 'end', MUT))
    o.append(L(560, yb, 600, yb, NX, 2.5, arrow='x'))
    o.append(T(580, yb + 22, 'Φ = 1000/3.58×10⁶ = 0.279 mWb', 13, fill=NX, bold=True))
    return 290, ''.join(o)


FIG[9] = (f9, 'Left: the worked example core, 500 turns carrying 2 A on iron of mean length 0.4 m with a 1 mm air gap. Right: its magnetic equivalent circuit. The gap (1.99×10⁶ A/Wb) is in series with the iron (1.59×10⁶ A/Wb), so 1000 A of MMF drives 0.279 mWb, and the 1 mm gap takes 556 A of it.',
          'A rectangular iron core with a coil of 500 turns and a 1 millimetre gap, and its equivalent circuit: an MMF of 1000 ampere-turns driving 0.279 milliweber through the core reluctance 1.59 million and the gap reluctance 1.99 million ampere-turns per weber.')


def q_locus_svg():
    """question-bank sketch: series RL current loci, V = 100 V; (i) X_L = 10 ohm with R varied, (ii) R = 10 ohm with X_L varied"""
    o = []
    s = 17.0
    for ox, title, rvar in ((90, '(i) X_L = 10 Ω, R varied', True), (450, '(ii) R = 10 Ω, X_L varied', False)):
        oy = 70
        X = lambda a: ox + a * s
        Y = lambda b: oy - b * s
        o.append(L(ox - 20, oy, ox + 220, oy, L2, 1.5, arrow='m'))
        o.append(L(ox, oy - 16, ox, Y(-10.9), L2, 1.5))
        o.append(T(ox + 216, oy - 8, 'V', 14, 'end', MUT, bold=True))
        o.append(T(ox + 90, 30, title.replace('X_L', 'X<tspan baseline-shift="sub" font-size="10">L</tspan>'), 14, bold=True))
        if rvar:
            o.append(f'<path d="M{X(0):.1f},{Y(-10):.1f} A{5 * s:.1f},{5 * s:.1f} 0 0 0 {X(0):.1f},{Y(0):.1f}" style="fill:none;stroke:{AC};stroke-width:3"/>')
            o.append(L(X(0), Y(-10), X(0), Y(0), AC, 1.2, '4 3'))
            o.append(Tb(X(0) - 8, Y(-5) + 4, '10 A', 13, 'end', MUT))
            o.append(C(X(0), Y(-10), 5, NX)); o.append(Tb(X(0) + 10, Y(-10) + 14, 'R = 0', 13, 'start'))
            o.append(Tb(X(0) + 14, oy - 8, 'R → ∞', 13, 'start', MUT))
        else:
            o.append(f'<path d="M{X(10):.1f},{Y(0):.1f} A{5 * s:.1f},{5 * s:.1f} 0 0 1 {X(0):.1f},{Y(0):.1f}" style="fill:none;stroke:{AC};stroke-width:3"/>')
            o.append(Tb(X(5), oy - 8, '10 A', 13, 'middle', MUT))
            o.append(C(X(10), Y(0), 5, NX)); o.append(Tb(X(10) + 8, Y(0) + 20, 'X_L = 0'.replace('X_L', 'X<tspan baseline-shift="sub" font-size="10">L</tspan>'), 13, 'start'))
            o.append(Tb(X(0) - 8, Y(0) + 34, 'X_L → ∞'.replace('X_L', 'X<tspan baseline-shift="sub" font-size="10">L</tspan>'), 13, 'end', MUT))
        o.append(C(X(5), Y(-5), 5, NX))
        o.append(ph(X(0), Y(0), X(5) - 4, Y(-5) - 4, NX, 2.2, 'x'))
        o.append(Tb(X(5) + 10, Y(-5) + 18, '7.07 A at −45°, 500 W', 13, 'start', NX, bold=True))
    return {'h': 270, 'body': ''.join(o),
            'aria': 'Two current locus sketches for a series RL circuit on 100 volts. Left: with reactance 10 ohms and resistance varied, a semicircle of diameter 10 amps below the voltage axis, on the minus 90 degree axis. Right: with resistance 10 ohms and reactance varied, a semicircle of diameter 10 amps along the voltage axis, below it. Both pass through 7.07 amps at minus 45 degrees, the maximum power point.'}


spec = make_spec(FIG)
