"""Claude's hand-drawn figures for me-ic-u3 (IC engines: combustion in SI and CI engines), one per chapter, drawn from each
chapter's own worked example and numbers. The pressure and heat-release curves are computed, not sketched: a single-zone
first-law model of the chapters' two engines (SI: bore = stroke = 86 mm, r = 9, 3000 rev/min; CI: bore 100 mm, stroke
110 mm, r = 17, 2000 rev/min) with Wiebe heat release, gamma = 1.35, 1 bar at BDC. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
import re

_T, _Tb, _boxt = T, Tb, boxt


def _sub(s):
    """R_s, V_c, p_max drawn as real subscripts, never as underscores"""
    return re.sub(r'([A-Za-z])_([A-Za-z0-9]+)', r'\1<tspan baseline-shift="sub" font-size="11">\2</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)
def boxt(x, y, w, h, lines, *a, **k): return _boxt(x, y, w, h, [_sub(l) for l in lines], *a, **k)

FIG = {}


# ---------------- the engine model ----------------
def engine(B=0.086, S=0.086, r=9.0, lam=3.5):
    Vs = math.pi / 4 * B * B * S; Vc = Vs / (r - 1); a = S / 2; l = lam * a
    def V(th):
        t = math.radians(th)
        return Vc + math.pi / 4 * B * B * (a * (1 - math.cos(t)) + l - math.sqrt(l * l - (a * math.sin(t)) ** 2))
    return V, Vs, Vc


def wiebe(th, th0, dur, a=5.0, m=2.0):
    if th <= th0: return 0.0
    z = (th - th0) / dur
    return 1 - math.exp(-a * z ** (m + 1)) if z < 1.5 else 1.0


def run(xfun, Q, B=0.086, S=0.086, r=9.0, g=1.35, step=0.1, start=-180, end=180):
    V, Vs, Vc = engine(B, S, r)
    th, p, out = start, 1.0e5, [(start, 1.0e5)]
    while th < end - 1e-9:
        V0, V1 = V(th), V(th + step)
        p += ((g - 1) * Q * (xfun(th + step) - xfun(th)) - g * p * (V1 - V0)) / ((V0 + V1) / 2)
        th = round(th + step, 4); out.append((th, p))
    return out


def si(th0, dur, Q=900.0):
    return run(lambda t: wiebe(t, th0, dur), Q)


def imep(c, B=0.086, S=0.086, r=9.0):
    V, Vs, Vc = engine(B, S, r)
    return sum((p0 + p1) / 2 * (V(t1) - V(t0)) for (t0, p0), (t1, p1) in zip(c, c[1:])) / Vs


def ci_x(soc, fp, dp=7.0, dd=55.0, md=0.9):
    return lambda t: fp * wiebe(t, soc, dp) + (1 - fp) * wiebe(t, soc + 1.0, dd, 5.0, md)


def ci(soc, fp, Q=1700.0):
    return run(ci_x(soc, fp), Q, 0.1, 0.11, 17.0)


def peak(c): return max(c, key=lambda x: x[1])


def slope(c):
    """steepest dp/dθ in bar per degree (over 1 degree) and where"""
    return max(((c[i + 10][1] - c[i][1]) / 1e5, c[i][0] + 0.5) for i in range(len(c) - 10))


def window(c, a, b, every=5):
    return [(t, p / 1e5) for i, (t, p) in enumerate(c) if a - 1e-6 <= t <= b + 1e-6 and i % every == 0]


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


def ca(v):
    """crank angle tick label"""
    return 'TDC' if v == 0 else (f'{-v}° bTDC' if v < 0 else f'{v}° aTDC')


def deg(v): return neg(v) + '°' if v else '0'


# ---- 3.1 p-θ diagram: the three SI stages ----
def f1():
    o = []
    x0, x1, y0, y1 = 80, 690, 50, 370
    fx, fy = lin(-40, 60, x0, x1), lin(0, 55, y1, y0)
    o.append(axes(x0, x1, y0, y1, [-40, -20, 0, 20, 40, 60], [0, 10, 20, 30, 40, 50], fx, fy,
                  'crank angle θ (degrees; negative = before TDC)', 'p (bar)', xfmt=deg))
    fire, mot = si(-10, 35), si(-10, 35, Q=0.0)
    # stage bands
    for a, b, lab, fill in ((-28, -10, 'I: ignition lag', ACS), (-10, 15.6, 'II: flame propagation', LVS), (15.6, 60, 'III: afterburning', NXS)):
        o.append(f'<rect x="{fx(a):.1f}" y="{y0:.1f}" width="{fx(b) - fx(a):.1f}" height="{y1 - y0:.1f}" style="fill:{fill};opacity:0.55"/>')
    o.append(T((fx(-28) + fx(-10)) / 2, y0 + 18, 'I: lag', 13, fill=AC, bold=True))
    o.append(T((fx(-10) + fx(15.6)) / 2, y0 + 18, 'II: flame propagation', 13, fill=LV, bold=True))
    o.append(T((fx(15.6) + fx(60)) / 2, y0 + 18, 'III: afterburning', 13, fill=NX, bold=True))
    o.append(P([(fx(t), fy(p)) for t, p in window(mot, -40, 60)], MUT, 2, dash='6 4'))
    o.append(P([(fx(t), fy(p)) for t, p in window(fire, -40, 60)], AC, 3))
    pA = dict(window(fire, -28, -28, 1))[-28]; pB = dict(window(fire, -10, -10, 1))[-10]
    tC, pC = peak(fire); pC /= 1e5
    o += [C(fx(-28), fy(pA), 6, AC), Tb(fx(-28) - 4, fy(pA) - 14, 'A: spark, 28° bTDC', 13, 'middle')]
    o += [C(fx(-10), fy(pB), 6, LV), Tb(fx(-10) - 8, fy(pB) - 16, 'B: 10° bTDC', 13, 'end', LV, bold=True)]
    o += [C(fx(tC), fy(pC), 6, NX), Tb(fx(tC) + 12, fy(pC) - 6, f'C: {pC:.1f} bar at {tC:.1f}° aTDC', 13, 'start', NX, bold=True)]
    o.append(Tb(fx(33), fy(8), 'motoring curve (no combustion)', 13, 'start', MUT))
    o.append(L(fx(32), fy(8.5), fx(25), fy(12.4), MUT, 1.5, arrow='m'))
    o.append(T(fx(-39), fy(46), '3000 rev/min: lag 1.0 ms = 18°', 13, 'start', MUT))
    o.append(T(fx(-39), fy(41), 'stage II: 25.6° = 1.42 ms', 13, 'start', MUT))
    return 420, ''.join(o)


FIG[1] = (f1, 'The worked example’s engine at 3000 rev/min: the spark at A (28° bTDC) is followed by 18° of ignition lag until the trace '
              'leaves the motoring curve at B (10° bTDC); flame propagation then lifts the pressure to its peak at C, and afterburning '
              'follows as the gas expands.',
          'Cylinder pressure against crank angle from 40 degrees before to 60 degrees after top dead centre. The motoring curve peaks at '
          'about 19 bar at TDC. The firing curve leaves it at 10 degrees before TDC and peaks at 50.3 bar at 15.6 degrees after TDC. '
          'Shaded bands mark ignition lag from the spark at 28 degrees before TDC, flame propagation, and afterburning.')


# ---- 3.2 three burn rates ----
def f2():
    o = []
    x0, x1, y0, y1 = 80, 690, 40, 360
    fx, fy = lin(-20, 50, x0, x1), lin(0, 65, y1, y0)
    o.append(axes(x0, x1, y0, y1, [-20, -10, 0, 10, 20, 30, 40, 50], [0, 10, 20, 30, 40, 50, 60], fx, fy,
                  'crank angle θ (degrees)', 'p (bar)', xfmt=deg))
    o.append(P([(fx(t), fy(p)) for t, p in window(si(-10, 35, 0.0), -20, 50)], MUT, 1.8, dash='6 4'))
    lab = {25: ('fast burn, 25°', LV), 35: ('normal burn, 35°', AC), 50: ('slow burn, 50°', NX)}
    for i, dur in enumerate((25, 35, 50)):
        c = si(-10, dur); t, pk = peak(c); pk /= 1e5; s_, _ = slope(c)
        name, col = lab[dur]
        o.append(P([(fx(a), fy(b)) for a, b in window(c, -20, 50)], col, 3 if dur == 35 else 2.4))
        o.append(C(fx(t), fy(pk), 5, col))
        Y = 430 + i * 22
        o.append(L(20, Y - 5, 46, Y - 5, col, 3))
        o.append(T(54, Y, f'{name}: peak {pk:.1f} bar at {t:.1f}° aTDC · steepest {s_:.1f} bar/° · IMEP {imep(c) / 1e5:.2f} bar', 13, 'start', col, bold=(dur == 35)))
    # the worked example's two points on the normal trace
    n = dict(window(si(-10, 35), -1, 11, 1))
    o += [C(fx(0), fy(n[0]), 5, INK), C(fx(10), fy(n[10]), 5, INK), L(fx(0), fy(n[0]), fx(10), fy(n[10]), INK, 1.6, dash='4 3')]
    o.append(Tb(fx(0) + 8, fy(n[0]) + 20, f'{n[0]:.1f} bar at TDC', 13, 'start'))
    o.append(Tb(fx(10) - 10, fy(n[10]) - 4, f'{n[10]:.1f} bar at 10°', 13, 'end'))
    o.append(T(fx(36), fy(2.5), 'dashed: motoring', 13, 'start', MUT))
    return 486, ''.join(o)


FIG[2] = (f2, 'The same engine with three burn lengths, all starting at 10° bTDC: a shorter burn gives a higher, earlier peak and a steeper '
              'rise. The dashed chord on the normal trace is the worked example’s average slope, 2.05 bar per degree.',
          'Three computed pressure traces. A 25 degree burn peaks at 59.8 bar at 10.5 degrees after TDC, steepest slope 3.8 bar per degree. '
          'A 35 degree burn peaks at 50.3 bar at 15.6 degrees, 2.3 bar per degree. A 50 degree burn peaks at 37.8 bar at 21.9 degrees, '
          '1.0 bar per degree. A chord joins 24.9 bar at TDC and 45.4 bar at 10 degrees on the normal trace.')


# ---- 3.3 ten consecutive cycles ----
SETS = [(-10, 35), (-11, 31), (-9, 40), (-10, 33), (-9.5, 38), (-10.5, 34), (-9, 43), (-11, 30), (-10, 36), (-9.5, 37)]


def f3():
    o = []
    x0, x1, y0, y1 = 80, 690, 40, 360
    fx, fy = lin(-20, 50, x0, x1), lin(0, 60, y1, y0)
    o.append(axes(x0, x1, y0, y1, [-20, -10, 0, 10, 20, 30, 40, 50], [0, 10, 20, 30, 40, 50, 60], fx, fy,
                  'crank angle θ (degrees)', 'p (bar)', xfmt=deg))
    cyc = [si(a, d) for a, d in SETS]
    pk = [peak(c) for c in cyc]
    hi, lo = max(range(10), key=lambda i: pk[i][1]), min(range(10), key=lambda i: pk[i][1])
    for i, c in enumerate(cyc):
        if i in (hi, lo): continue
        o.append(P([(fx(t), fy(p)) for t, p in window(c, -20, 50)], L2, 1.6))
    for j, (i, col, txt) in enumerate(((hi, LV, 'fastest'), (lo, NX, 'slowest'))):
        c = cyc[i]; t, p = pk[i]; p /= 1e5
        o.append(P([(fx(a), fy(b)) for a, b in window(c, -20, 50)], col, 3))
        o.append(C(fx(t), fy(p), 5, col))
        Y = 430 + j * 22
        o.append(L(20, Y - 5, 46, Y - 5, col, 3))
        o.append(T(54, Y, f'{txt} cycle: peak {p:.1f} bar at {t:.1f}° aTDC · IMEP {imep(c) / 1e5:.2f} bar', 13, 'start', col, bold=True))
    o.append(L(20, 469, 46, 469, L2, 2))
    o.append(T(54, 474, 'the other eight cycles', 13, 'start', MUT))
    o.append(T(fx(-19), fy(57), '10 cycles, same settings:', 13, 'start', MUT))
    o.append(T(fx(-19), fy(57) + 18, 'p_max COV 9.1 %', 13, 'start', MUT))
    o.append(T(fx(-19), fy(57) + 36, 'IMEP COV 1.3 %', 13, 'start', MUT))
    return 490, ''.join(o)


FIG[3] = (f3, 'Ten consecutive cycles of the same engine at the same speed, throttle and spark: peak pressure ranges from 42.0 to 56.3 bar, '
              'while the work per cycle (IMEP) stays within 9.14 to 9.52 bar, the values of the worked example.',
          'Ten computed pressure traces overlaid. The fastest cycle peaks at 56.3 bar at 12.3 degrees after TDC with IMEP 9.52 bar; the '
          'slowest peaks at 42.0 bar at 20.0 degrees with IMEP 9.14 bar. A note gives the coefficient of variation: 9.1 percent for peak '
          'pressure, 1.3 percent for IMEP.')


# ---- 3.4 normal, knocking and pre-ignition traces ----
def f4():
    o = []
    x0, x1, y0, y1 = 80, 690, 40, 380
    fx, fy = lin(-40, 40, x0, x1), lin(0, 90, y1, y0)
    o.append(axes(x0, x1, y0, y1, [-40, -30, -20, -10, 0, 10, 20, 30, 40], [0, 20, 40, 60, 80], fx, fy,
                  'crank angle θ (degrees)', 'p (bar)', xfmt=deg))
    o.append(L(fx(-28), y0 + 8, fx(-28), y1, INK, 1.5, dash='5 4'))
    o.append(T(fx(-29), fy(52), 'spark', 13, 'end'))
    o.append(T(fx(-29), fy(52) + 17, '28° bTDC', 13, 'end'))
    norm = window(si(-10, 35), -40, 40, 2)
    o.append(P([(fx(t), fy(p)) for t, p in norm], MUT, 2.4))
    # knock: the normal trace plus ringing from 10.8° aTDC (6.5 kHz = one cycle per 2.8° at 3000 rev/min), decaying
    kn = [(t, p + (6.0 * math.exp(-(t - 10.8) / 9.0) * math.sin(2 * math.pi * (t - 10.8) / 2.8) if t >= 10.8 else 0.0)) for t, p in window(si(-10, 35), -40, 40, 1)]
    o.append(P([(fx(t), fy(p)) for t, p in kn if t >= 0], AC, 2))
    pre = window(si(-32, 35), -40, 40, 2)
    o.append(P([(fx(t), fy(p)) for t, p in pre], NX, 2.6))
    tp, pp = peak(si(-32, 35))
    o.append(T(fx(-38), fy(84), f'pre-ignition: hot spot at 40° bTDC, {pp / 1e5:.0f} bar near TDC', 13, 'start', NX, bold=True))
    o.append(T(fx(20), fy(74), 'knock: end gas ignites', 13, 'start', AC, bold=True))
    o.append(T(fx(20), fy(74) + 17, 'at 10.8° aTDC, rings every', 13, 'start', AC))
    o.append(T(fx(20), fy(74) + 34, '2.8° (6.5 kHz)', 13, 'start', AC))
    o.append(L(fx(22), fy(74) + 40, fx(14.5), fy(56), AC, 1.5, arrow='n'))
    o.append(T(fx(-14), fy(8), 'normal cycle', 13, 'start', MUT, bold=True))
    o.append(L(fx(-8), fy(10.5), fx(-7), fy(17), MUT, 1.5, arrow='m'))
    o.append(L(fx(14.4), fy(4), fx(14.4), fy(18), LV, 2, arrow='l'))
    o.append(Tb(fx(14.4) + 6, fy(4) + 2, 'flame would arrive 14.4°', 13, 'start', LV))
    return 430, ''.join(o)


FIG[4] = (f4, 'Three cycles against one spark timing (28° bTDC): the normal burn; knock, where the end gas autoignites at 10.8° aTDC, before '
              'the flame arrives at 14.4° aTDC, and the cylinder rings; and pre-ignition, where a hot spot starts the burn before the spark.',
          'Pressure against crank angle from 40 degrees before to 40 degrees after TDC. The normal trace peaks near 50 bar at 16 degrees after '
          'TDC. The knocking trace follows it, then oscillates from 10.8 degrees after TDC with one cycle every 2.8 degrees. The pre-ignition '
          'trace rises early and peaks near 72 bar close to TDC. A dashed line marks the spark at 28 degrees before TDC.')


# ---- 3.5 the three groups of knock factors ----
def f5():
    o = []
    cols = [('Density factors', AC, ACS, [('compression ratio 8 → 10', '↑'), ('load (more charge)', '↑'), ('inlet temperature', '↑'),
                                          ('wall temperature', '↑'), ('spark advance', '↑')]),
            ('Time factors', LV, LVS, [('turbulence', '↓'), ('engine speed', '↓'), ('flame path, bore', '↑'), ('central plug', '↓'),
                                       ('compact chamber', '↓')]),
            ('Composition factors', NX, NXS, [('octane number', '↓'), ('φ near 1.1', 'worst'), ('lean, φ = 0.85', '↓'),
                                              ('humidity', '↓'), ('EGR, residual', '↓')])]
    w, gap, x = 216, 16, 16
    for title, col, soft, rows in cols:
        o.append(R(x, 16, w, 44, soft, col)); o.append(T(x + w / 2, 44, title, 15, fill=col, bold=True))
        for i, (lab, eff) in enumerate(rows):
            y = 72 + i * 50
            o.append(R(x, y, w, 40, PANEL, L2, rx=6, sw=1.5))
            o.append(T(x + 10, y + 25, lab, 13, 'start'))
            o.append(T(x + w - 10, y + 25, eff, 15 if len(eff) == 1 else 13, 'end', AC if eff == '↑' else (LV if eff == '↓' else NX), bold=True))
        x += w + gap
    o.append(T(360, 352, 'Raising the factor: ↑ knock increases, ↓ knock decreases.', 13, fill=MUT))
    o.append(T(360, 374, 'Example: r = 8 → 10 heats the charge from 683 K to 739 K before burning starts.', 13, fill=MUT))
    return 392, ''.join(o)


FIG[5] = (f5, 'The factors that decide whether the end gas autoignites, in the three textbook groups: what raises end-gas temperature '
              'and pressure, what gives the end gas more time, and what the fuel and mixture do.',
          'Three columns. Density factors: compression ratio, load, inlet temperature, wall temperature and spark advance all increase knock. '
          'Time factors: turbulence, engine speed, a central plug and a compact chamber decrease knock; a longer flame path or bigger bore '
          'increases it. Composition factors: octane number, a lean mixture, humidity and EGR decrease knock; a mixture near equivalence '
          'ratio 1.1 is the worst.')


# ---- 3.6 CI heat release rate with the four stages ----
def f6():
    o = []
    x0, x1, y0, y1 = 80, 690, 100, 400
    fx, fy = lin(-20, 60, x0, x1), lin(0, 140, y1, y0)
    o.append(axes(x0, x1, y0, y1, [-20, -10, 0, 10, 20, 30, 40, 50, 60], [0, 20, 40, 60, 80, 100, 120, 140], fx, fy,
                  'crank angle θ (degrees)', 'dQ/dθ (J per degree)', xfmt=deg))
    x = ci_x(-4.2, 0.25)
    pts = [(t / 10, 1700 * (x(t / 10 + 0.05) - x(t / 10 - 0.05)) / 0.1) for t in range(-200, 601, 2)]
    bands = ((-15, -4.2, 'delay', ACS), (-4.2, 3.5, 'premixed', LVS), (3.5, 30, 'mixing-controlled', NXS), (30, 60, 'late', 'var(--line)'))
    for a, b, lab, fill in bands:
        a2 = max(a, -20)
        o.append(f'<rect x="{fx(a2):.1f}" y="{y0:.1f}" width="{fx(b) - fx(a2):.1f}" height="{y1 - y0:.1f}" style="fill:{fill};opacity:0.5"/>')
    o.append(P([(fx(t), fy(v)) for t, v in pts], AC, 3))
    # injection bar
    o.append(R(fx(-15), 46, fx(10) - fx(-15), 14, ACS, AC, rx=4))
    o.append(T(fx(-15), 36, 'injection: 15° bTDC to 10° aTDC, 40 mg', 13, 'start', AC, bold=True))
    o.append(T(fx(-14.5), y0 + 18, 'delay', 13, 'start', AC, bold=True))
    o.append(T(fx(-14.5), y0 + 34, '10.8° = 0.9 ms', 13, 'start', AC))
    o.append(Tb(fx(1.5), fy(131) - 2, 'B to C: premixed spike', 13, 'start', LV, bold=True))
    o.append(Tb(fx(16), fy(60), 'C to D: mixing-controlled', 13, 'middle', NX, bold=True))
    o.append(Tb(fx(45), fy(30), 'after D: late burning', 13, 'middle', MUT, bold=True))
    o.append(C(fx(-4.2), fy(0), 6, LV)); o.append(Tb(fx(-4.2), fy(0) - 14, 'B', 13, 'middle', LV, bold=True))
    o.append(C(fx(-15), fy(0), 6, AC)); o.append(Tb(fx(-15) + 2, fy(0) - 14, 'A', 13, 'start', AC, bold=True))
    return 450, ''.join(o)


FIG[6] = (f6, 'Heat release rate of the worked example’s diesel at 2000 rev/min: injection starts at A (15° bTDC), nothing burns during the '
              '10.8° delay while 17.3 mg collects, that fuel feeds the premixed spike from B (4.2° bTDC), and the rest burns as it mixes.',
          'Heat release rate against crank angle. Injection runs from 15 degrees before to 10 degrees after TDC. Shaded bands mark the delay '
          'up to 4.2 degrees before TDC, a premixed spike peaking near 128 joules per degree at TDC, a mixing-controlled hump near 44 joules '
          'per degree around 12 degrees after TDC, and a late burning tail to 60 degrees.')


# ---- 3.7 long and short delay: CI pressure traces ----
def f7():
    o = []
    x0, x1, y0, y1 = 80, 690, 40, 370
    fx, fy = lin(-20, 40, x0, x1), lin(30, 90, y1, y0)
    o.append(axes(x0, x1, y0, y1, [-20, -10, 0, 10, 20, 30, 40], [30, 40, 50, 60, 70, 80, 90], fx, fy,
                  'crank angle θ (degrees)', 'p (bar)', xfmt=deg))
    mot = run(lambda t: 0.0, 0.0, 0.1, 0.11, 17.0)
    o.append(P([(fx(t), fy(p)) for t, p in window(mot, -20, 40) if p >= 30], MUT, 1.8, dash='6 4'))
    for soc, fp, col, name, an, dx in ((-4.2, 0.25, AC, 'fuel A: delay 0.9 ms, 17.3 mg waiting', 'start', 14),
                                       (-9.0, 0.14, LV, 'fuel B: delay 0.5 ms, 9.6 mg waiting', 'start', 14)):
        c = ci(soc, fp); t, p = peak(c); s, ts = slope(c)
        o.append(P([(fx(a), fy(b)) for a, b in window(c, -20, 40) if b >= 30], col, 3))
        o.append(C(fx(soc), fy(dict(window(c, soc, soc, 1))[soc]), 6, col))
    cA, cB = ci(-4.2, 0.25), ci(-9.0, 0.14)
    sA, tA = slope(cA); sB, tB = slope(cB)
    pA, pB = peak(cA), peak(cB)
    o.append(Tb(fx(16), fy(84), f'A: steepest {sA:.1f} bar/°, peak {pA[1] / 1e5:.0f} bar', 13, 'start', AC, bold=True))
    o.append(Tb(fx(16), fy(77), f'B: steepest {sB:.1f} bar/°, peak {pB[1] / 1e5:.0f} bar', 13, 'start', LV, bold=True))
    o.append(T(fx(-3), fy(38), 'A starts 4.2° bTDC', 13, 'start', AC))
    o.append(T(fx(-10), fy(52), 'B starts 9° bTDC', 13, 'end', LV))
    o.append(L(fx(-11), fy(50.5), fx(-9.3), fy(41), LV, 1.5, arrow='l'))
    o.append(T(fx(14), fy(33), 'dashed: motoring', 13, 'start', MUT))
    return 424, ''.join(o)


FIG[7] = (f7, 'The worked example’s two fuels in the same diesel: the shorter delay of fuel B lets less fuel collect, so its pressure rises '
              'less steeply, even though its earlier start gives a slightly higher peak.',
          'Two computed diesel pressure traces with a dashed motoring curve. Fuel A, delay 0.9 milliseconds, starts burning at 4.2 degrees '
          'before TDC, steepest rise 8.8 bar per degree, peak 80 bar. Fuel B, delay 0.5 milliseconds, starts at 9 degrees before TDC, '
          'steepest rise 6.3 bar per degree, peak 86 bar.')


# ---- 3.8 swirl, squish and tumble ----
def f8():
    o = []
    # swirl: top view
    cx, cy, r = 130, 190, 90
    o.append(T(cx, 30, 'Swirl (top view)', 15, fill=AC, bold=True))
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" style="fill:{PANEL};stroke:{INK};stroke-width:2"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r * 0.6:.1f}" style="fill:none;stroke:{L2};stroke-width:1.5;stroke-dasharray:5 4"/>')
    for a0 in (20, 140, 260):
        a1 = a0 + 85
        x1, y1 = cx + 70 * math.cos(math.radians(a0)), cy - 70 * math.sin(math.radians(a0))
        x2, y2 = cx + 70 * math.cos(math.radians(a1)), cy - 70 * math.sin(math.radians(a1))
        o.append(f'<path d="M{x1:.1f},{y1:.1f} A70,70 0 0,0 {x2:.1f},{y2:.1f}" style="fill:none;stroke:{AC};stroke-width:3" marker-end="url(#ar-UID-n)"/>')
    o.append(C(cx, cy, 4, INK))
    o.append(T(cx, cy + 24, 'bowl 60 mm', 13, fill=MUT))
    o.append(T(cx, 306, 'bore 100 mm, R_s = 2.2', 13))
    o.append(T(cx, 326, '4400 rev/min, 23.0 m/s at the wall', 13))
    # squish: side view
    sx = 270
    o.append(T(sx + 90, 30, 'Squish (side view, near TDC)', 15, fill=LV, bold=True))
    o.append(R(sx, 60, 180, 16, 'var(--line)', INK, rx=2, sw=1.5))  # head
    o.append(T(sx + 90, 54, 'cylinder head', 13, fill=MUT))
    o.append(f'<path d="M{sx},{100} H{sx + 50} V{150} Q{sx + 90},{176} {sx + 130},{150} V{100} H{sx + 180} V{230} H{sx} Z" style="fill:{PANEL};stroke:{INK};stroke-width:2"/>')
    o.append(T(sx + 90, 214, 'piston with bowl', 13, fill=MUT))
    for xa, xb in ((sx + 8, sx + 46), (sx + 172, sx + 134)):
        o.append(L(xa, 88, xb, 88, LV, 2.5, arrow='l'))
        o.append(L(xb + (4 if xb < xa else -4), 92, xb + (4 if xb < xa else -4), 128, LV, 2.5, arrow='l'))
    o.append(T(sx + 90, 256, 'gas squeezed out of the', 13))
    o.append(T(sx + 90, 274, '1.0 mm gap into the bowl', 13))
    o.append(T(sx + 90, 296, 'radial flow, not a rotation', 13, fill=LV, bold=True))
    # tumble: side view
    tx = 490
    o.append(T(tx + 105, 30, 'Tumble (side view)', 15, fill=NX, bold=True))
    o.append(P([(tx + 20, 70), (tx + 20, 280), (tx + 190, 280), (tx + 190, 70)], INK, 2))
    o.append(P([(tx + 20, 70), (tx + 105, 46), (tx + 190, 70)], INK, 2))
    o.append(L(tx + 105, 40, tx + 105, 62, AC, 3))
    o.append(T(tx + 98, 76, 'plug', 13, 'end', AC))
    o.append(R(tx + 20, 252, 170, 28, PANEL, INK, rx=2, sw=1.5))
    o.append(T(tx + 105, 271, 'piston', 13, fill=MUT))
    o.append(f'<ellipse cx="{tx + 105}" cy="160" rx="62" ry="70" style="fill:none;stroke:{NX};stroke-width:3;stroke-dasharray:300 40" />')
    o.append(L(tx + 167, 150, tx + 167, 175, NX, 3, arrow='x'))
    o.append(C(tx + 105, 160, 4, INK))
    o.append(T(tx + 105, 306, 'rolls about an axis', 13))
    o.append(T(tx + 105, 324, 'across the cylinder', 13))
    return 344, ''.join(o)


FIG[8] = (f8, 'The three organised motions in the worked example’s diesel and a petrol head: swirl turns about the cylinder axis, squish '
              'squeezes gas inward from the thin gap at TDC, and tumble rolls the charge about an axis across the cylinder.',
          'Three panels. Swirl, top view: a 100 millimetre bore with curved arrows round the axis and a 60 millimetre bowl; swirl ratio 2.2, '
          '4400 revolutions per minute, 23 metres per second at the wall. Squish, side view: a piston with a bowl close under the head; '
          'arrows push gas from the 1 millimetre gap inward and down into the bowl. Tumble, side view: a pent-roof cylinder with a loop '
          'turning about a horizontal axis.')


# ---- 3.9 chamber types ----
def f9():
    o = []
    def head(x, y, w): return R(x, y, w, 14, 'var(--line)', INK, rx=2, sw=1.5)
    # hemispherical
    x = 20
    o.append(T(x + 75, 26, 'Hemispherical (SI)', 14, fill=AC, bold=True))
    o.append(f'<path d="M{x},{150} V{110} A75,62 0 0,1 {x + 150},{110} V{150}" style="fill:{PANEL};stroke:{INK};stroke-width:2"/>')
    o.append(R(x, 150, 150, 40, 'var(--line)', INK, rx=2, sw=1.5)); o.append(T(x + 75, 176, 'piston', 13, fill=MUT))
    o.append(L(x + 75, 34 + 10, x + 75, 66, AC, 3)); o.append(T(x + 75, 82, 'plug', 13, fill=AC))
    o.append(L(x + 22, 74, x + 40, 98, INK, 4)); o.append(L(x + 128, 74, x + 110, 98, INK, 4))
    o.append(T(x + 75, 212, 'central plug, big valves', 13)); o.append(T(x + 75, 230, 'lowest S/V: 2.06 cm⁻¹', 13, fill=AC))
    # wedge
    x = 200
    o.append(T(x + 75, 26, 'Wedge (SI)', 14, fill=AC, bold=True))
    o.append(f'<path d="M{x},{150} V{80} L{x + 150},{138} V{150} Z" style="fill:{PANEL};stroke:{INK};stroke-width:2"/>')
    o.append(R(x, 150, 150, 40, 'var(--line)', INK, rx=2, sw=1.5)); o.append(T(x + 75, 176, 'piston', 13, fill=MUT))
    o.append(L(x + 20, 52, x + 20, 84, AC, 3)); o.append(T(x + 24, 48, 'plug', 13, 'start', AC))
    o.append(L(x + 112, 144, x + 140, 144, LV, 2.5, arrow='l'))
    o.append(T(x + 75, 212, 'squish at the thin end', 13)); o.append(T(x + 75, 230, 'longer flame path', 13, fill=MUT))
    # DI bowl
    x = 380
    o.append(T(x + 75, 26, 'DI bowl (CI)', 14, fill=LV, bold=True))
    o.append(head(x, 60, 150))
    o.append(f'<path d="M{x},{80} H{x + 40} V{120} Q{x + 75},{146} {x + 110},{120} V{80} H{x + 150} V{190} H{x} Z" style="fill:{PANEL};stroke:{INK};stroke-width:2"/>')
    o.append(L(x + 75, 40, x + 75, 72, LV, 4)); o.append(T(x + 82, 46, 'injector', 13, 'start', LV))
    o.append(L(x + 75, 76, x + 48, 110, LV, 1.8, dash='4 3')); o.append(L(x + 75, 76, x + 102, 110, LV, 1.8, dash='4 3'))
    o.append(T(x + 75, 168, 'bowl 60 × 16 mm', 13, fill=MUT))
    o.append(T(x + 75, 212, '84 % of V_c in bowl', 13)); o.append(T(x + 75, 230, 'r = 17.0', 13, fill=LV))
    # IDI swirl chamber
    x = 560
    o.append(T(x + 75, 26, 'IDI swirl chamber', 14, fill=NX, bold=True))
    o.append(R(x, 54, 150, 86, 'var(--line)', INK, rx=2, sw=1.5))
    o.append(f'<circle cx="{x + 50}" cy="94" r="28" style="fill:{PANEL};stroke:{INK};stroke-width:2"/>')
    o.append(f'<path d="M{x + 62},{116} L{x + 84},{140} L{x + 96},{140} L{x + 72},{112} Z" style="fill:{PANEL};stroke:{INK};stroke-width:1.5"/>')
    o.append(f'<path d="M{x + 50},{76} A18,18 0 1,1 {x + 33},{100}" style="fill:none;stroke:{NX};stroke-width:2.5" marker-end="url(#ar-UID-x)"/>')
    o.append(R(x, 140, 150, 10, PANEL, INK, rx=0, sw=1.5))
    o.append(R(x, 150, 150, 40, 'var(--line)', INK, rx=2, sw=1.5)); o.append(T(x + 75, 176, 'piston', 13, fill=MUT))
    o.append(L(x + 12, 60, x + 28, 76, NX, 4)); o.append(T(x + 6, 50, 'pintle nozzle', 13, 'start', NX))
    o.append(T(x + 100, 116, 'throat', 13, 'start', INK))
    o.append(T(x + 75, 212, 'quiet, low pressure', 13)); o.append(T(x + 75, 230, 'more heat loss', 13, fill=MUT))
    return 248, ''.join(o)


FIG[9] = (f9, 'Four chamber types in section. The SI shapes keep the flame path short; the DI diesel holds most of its clearance volume in '
              'the piston bowl (84 % in the worked example); the IDI diesel burns first in a swirl chamber joined by a throat.',
          'Four section sketches. Hemispherical SI chamber: a dome with a central plug and inclined valves, surface to volume ratio 2.06 per '
          'centimetre. Wedge SI chamber: a sloping head with the plug at the thick end and a squish arrow at the thin end. Direct injection '
          'diesel: a central injector spraying into a 60 by 16 millimetre bowl in the piston, compression ratio 17. Indirect injection '
          'diesel: a round swirl chamber in the head with a pintle nozzle, joined to the main chamber by a throat.')



def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}


def drop_sources():
    return ['ocw.mit.edu']
