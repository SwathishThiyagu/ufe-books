"""Claude's hand-drawn figures for ee-pe-u5 (Power Electronics: AC-AC converters), one per chapter, drawn from each
chapter's own worked example and numbers (computed here, not sketched). Colours are the shell's CSS variables."""
import os, sys, math, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

_T, _Tb = T, Tb


def _sub(s):
    """V_o, S_Aa ... drawn as real subscripts, never as underscores"""
    return re.sub(r'([A-Za-zα-ω])_([A-Za-z0-9]+)', r'\1<tspan baseline-shift="sub" font-size="11">\2</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


def curve(f, a, b, fx, fy, n=240):
    return [(fx(a + (b - a) * i / n), fy(f(a + (b - a) * i / n))) for i in range(n + 1)]


def dashes(xs, y0, y1):
    return ''.join(L(x, y0, x, y1, L2, 1, '3 4') for x in xs)


def wave_axes(x0, x1, yc, amp, ticks, fx, vlab, unit_lab, top_lab):
    o = [L(x0, yc, x1, yc, L2, 1.5), L(x0, yc - amp - 8, x0, yc + amp + 8, L2, 1.5)]
    for v, s in ticks:
        X = fx(v); o += [L(X, yc, X, yc + 5, L2, 1.5), T(X, yc + amp + 26, s, 13, fill=MUT)]
    o += [L(x0 - 5, yc - amp, x0, yc - amp, L2, 1.5), T(x0 - 8, yc - amp + 5, vlab, 13, 'end', MUT),
          L(x0 - 5, yc + amp, x0, yc + amp, L2, 1.5), T(x0 - 8, yc + amp + 5, '−' + vlab, 13, 'end', MUT)]
    o.append(T(x0 + 6, yc - amp - 16, top_lab, 14, 'start', bold=True))
    if unit_lab: o.append(T(x1, yc + amp + 26, unit_lab, 13, 'end', MUT))
    return ''.join(o)


# ---- 5.1 waveforms of the two worked examples ----
def f1():
    o = []
    x0, x1 = 80, 690
    fx = lin(0, 360, x0, x1)
    s = lambda d: math.sin(math.radians(d))
    tk = [(0, '0'), (90, '90°'), (180, '180°'), (270, '270°'), (360, '360°')]
    # (a) R load, alpha 90
    yc, A = 130, 78
    fy = lin(-325, 325, yc + A, yc - A)
    o.append(wave_axes(x0, x1, yc, A, tk, fx, '325 V', '', '(a) 20 Ω resistor, α = 90°'))
    o.append(P(curve(lambda d: 325 * s(d), 0, 360, fx, fy), L2, 1.6, '6 5'))
    for a0 in (90, 270):
        o.append(P([(fx(a0), yc)] + curve(lambda d: 325 * s(d), a0, a0 + 90, fx, fy) + [(fx(a0 + 90), yc)], AC, 2.5, fill=ACS))
        o.append(C(fx(a0), yc, 6, NX))
    o.append(T(fx(90) - 8, yc - 8, 'T1 fired', 13, 'end', NX, bold=True))
    o.append(T(fx(270) - 8, yc + 20, 'T2 fired', 13, 'end', NX, bold=True))
    o.append(T(fx(140), yc - A + 4, 'v_o', 14, 'start', AC, bold=True))
    o.append(T(fx(20), yc - 40, 'v_s', 14, 'start', MUT))
    o.append(T(fx(315), yc - 40, '162.6 V RMS, 1322.5 W', 13, 'middle', MUT))
    # (b) RL load, alpha 60, phi 45, beta 224.2
    yc, A = 360, 78
    fy = lin(-325, 325, yc + A, yc - A)
    o.append(wave_axes(x0, x1, yc, A, tk, fx, '325 V', '', '(b) 10 Ω + 31.83 mH, α = 60°, β = 224.2°'))
    o.append(P(curve(lambda d: 325 * s(d), 0, 360, fx, fy), L2, 1.6, '6 5'))
    al, be = 60, 224.155
    o.append(P([(fx(al), yc)] + curve(lambda d: 325 * s(d), al, be, fx, fy) + [(fx(be), yc)], AC, 2.5, fill=ACS))
    o.append(P([(fx(al + 180), yc)] + curve(lambda d: 325 * s(d), al + 180, 360, fx, fy) + [(fx(360), yc)], AC, 2.5, fill=ACS))
    o.append(P([(fx(0), yc)] + curve(lambda d: 325 * s(d), 0, be - 180, fx, fy) + [(fx(be - 180), yc)], AC, 2.5, fill=ACS))

    def i(d):  # current in A, period 360
        d %= 360
        if al <= d <= be: t = math.radians(d); return 23.0 * (math.sin(t - math.pi / 4) - math.sin(math.radians(15)) * math.exp(-(t - math.radians(al))))
        if d >= al + 180 or d <= be - 180: return -i(d - 180 if d >= 180 else d + 180)
        return 0.0
    k = 325 / 23.0 * 0.75
    o.append(P([(fx(d), fy(k * i(d))) for d in [x * 0.75 for x in range(481)]], LV, 2.5))
    o.append(L(fx(be), yc - A - 4, fx(be), yc + A + 4, NX, 1.5, '4 3'))
    o.append(Tb(fx(be) + 6, yc - A + 10, 'β = 224.2°', 13, 'start', NX, bold=True))
    o.append(T(fx(122), yc - A - 2, 'v_o', 14, 'middle', AC, bold=True))
    o.append(T(fx(318), yc - 40, 'i, peak 21.4 A', 13, 'middle', LV, bold=True))
    o.append(T(fx(318), yc - 20, '217.1 V RMS, 14.60 A RMS', 13, 'middle', MUT))
    return 492, ''.join(o)


# ---- 5.2 the RC-DIAC dimmer of the worked examples ----
def f2():
    o = []
    # circuit
    yt, yb = 50, 230
    xs, xl, xt, xr = 80, 250, 440, 600
    o.append(L(xs, yt, xt, yt, INK, 2)); o.append(L(xs, yb, xr, yb, INK, 2))
    o.append(L(xt, yt, xr, yt, INK, 2))
    # source
    o.append(L(xs, yt, xs, 112, INK, 2)); o.append(L(xs, 168, xs, yb, INK, 2))
    o.append(f'<circle cx="{xs}" cy="140" r="28" style="fill:var(--panel);stroke:var(--ink);stroke-width:2"/>')
    o.append(P([(xs - 16, 140), (xs - 8, 128), (xs, 140), (xs + 8, 152), (xs + 16, 140)], INK, 2))
    o.append(T(xs + 36, 136, '230 V', 14, 'start', bold=True)); o.append(T(xs + 36, 154, '50 Hz', 13, 'start', MUT))
    # lamp on top wire
    o.append(R(xl - 50, yt - 16, 100, 32, ACS, AC, 6)); o.append(T(xl, yt + 5, 'lamp 529 Ω', 13, bold=True))
    # TRIAC between top node (xt) and bottom
    o.append(L(xt, yt, xt, 112, INK, 2)); o.append(L(xt, 168, xt, yb, INK, 2))
    o.append(P([(xt - 18, 112), (xt + 18, 112)], INK, 2.5)); o.append(P([(xt - 18, 168), (xt + 18, 168)], INK, 2.5))
    o.append(P([(xt - 18, 112), (xt - 2, 112), (xt - 10, 168), (xt - 18, 112)], INK, 2, fill=PANEL))
    o.append(P([(xt + 2, 168), (xt + 18, 168), (xt + 10, 112), (xt + 2, 168)], INK, 2, fill=PANEL))
    o.append(T(xt - 26, 108, 'MT2', 13, 'end', MUT)); o.append(T(xt - 26, 182, 'MT1', 13, 'end', MUT))
    o.append(T(xt - 26, 145, 'TRIAC', 14, 'end', bold=True))
    # RC branch at xr
    o.append(L(xr, yt, xr, 74, INK, 2)); o.append(R(xr - 12, 74, 24, 52, PANEL, INK, 2, 2)); o.append(L(xr, 126, xr, 172, INK, 2))
    o.append(T(xr + 20, 96, 'R = 100 kΩ', 13, 'start', bold=True)); o.append(T(xr + 20, 113, '(pot + fixed)', 13, 'start', MUT))
    o.append(L(xr - 16, 172, xr + 16, 172, INK, 3)); o.append(L(xr - 16, 182, xr + 16, 182, INK, 3)); o.append(L(xr, 182, xr, yb, INK, 2))
    o.append(T(xr + 22, 182, 'C = 0.1 µF', 13, 'start', bold=True))
    # DIAC from node between R and C to gate
    yg = 150
    o.append(C(xr, yg, 4, INK))
    o.append(L(xr, yg, 548, yg, INK, 2)); o.append(L(492, yg, xt + 12, 160, INK, 2))
    o.append(L(548, yg - 14, 548, yg + 14, INK, 2.5)); o.append(L(492, yg - 14, 492, yg + 14, INK, 2.5))
    o.append(P([(548, yg - 12), (520, yg), (548, yg + 12)], INK, 2, fill=PANEL))
    o.append(P([(492, yg - 12), (520, yg), (492, yg + 12)], INK, 2, fill=PANEL))
    o.append(T(520, yg - 20, 'DIAC 30 V', 13, bold=True)); o.append(T(472, 176, 'G', 13, 'middle', MUT))
    o.append(T(xr + 12, yg + 5, 'v_C', 14, 'start', LV, bold=True))
    # waveform of v_C
    x0, x1, yc, A = 80, 690, 370, 80
    fx = lin(0, 360, x0, x1); fy = lin(-100, 100, yc + A, yc - A)
    tk = [(0, '0'), (90, '90°'), (180, '180°'), (270, '270°'), (360, '360°')]
    o.append(wave_axes(x0, x1, yc, A, tk, fx, '100 V', '', 'Capacitor voltage: 98.7 V peak, lagging the supply by 72.3°'))
    o.append(P(curve(lambda d: 98.66 * math.sin(math.radians(d)), 0, 360, fx, fy), L2, 1.6, '6 5'))
    o.append(P(curve(lambda d: 98.66 * math.sin(math.radians(d - 72.34)), 0, 360, fx, fy), LV, 2.5))
    for v in (30, -30):
        o.append(L(x0, fy(v), x1, fy(v), NX, 1.5, '4 4'))
    o.append(T(x0 - 8, fy(30) + 5, '+30 V', 13, 'end', NX)); o.append(T(x0 - 8, fy(-30) + 5, '−30 V', 13, 'end', NX))
    for a0 in (90.05, 270.05):
        y = fy(30 if a0 < 180 else -30)
        o.append(C(fx(a0), y, 6, NX))
    o.append(Tb(fx(90) + 10, fy(30) + 20, 'fires at α = 90.0°', 13, 'start', NX, bold=True))
    o.append(Tb(fx(270) + 8, fy(-30) + 22, 'fires at 270.0°', 13, 'start', NX, bold=True))
    o.append(T(fx(10), fy(92), 'supply', 13, 'start', MUT))
    return 486, ''.join(o)


# ---- 5.3 three-wire star output against alpha ----
def _r3(a):
    a = math.radians(a)
    if a <= math.pi / 3: return math.sqrt(1 - 3 * a / (2 * math.pi) + 3 * math.sin(2 * a) / (4 * math.pi))
    if a <= math.pi / 2: return math.sqrt(6 / math.pi * (math.pi / 12 + 3 * math.sin(2 * a) / 16 + math.sqrt(3) * math.cos(2 * a) / 16))
    if a < 5 * math.pi / 6: return math.sqrt(max(0, 6 / math.pi * (5 * math.pi / 24 - a / 4 + math.sin(2 * a) / 16 + math.sqrt(3) * math.cos(2 * a) / 16)))
    return 0.0


def _r1(a):
    a = math.radians(a)
    return math.sqrt(max(0.0, (math.pi - a + math.sin(2 * a) / 2) / math.pi))


def f3():
    o = []
    x0, x1, y0, y1 = 80, 680, 92, 352
    fx = lin(0, 180, x0, x1); fy = lin(0, 1, y1, y0)
    for a, b, fill in ((0, 60, ACS), (60, 90, LVS), (90, 150, NXS)):
        o.append(R(fx(a), y0, fx(b) - fx(a), y1 - y0, fill, 'none', 0, 0))
    o.append(T(fx(30), y0 - 10, '3 and 2 SCRs', 13, fill=MUT)); o.append(T(fx(75), y0 - 10, '2 SCRs', 13, fill=MUT))
    o.append(T(fx(120), y0 - 10, '2, then none', 13, fill=MUT))
    o.append(axes(x0, x1, y0, y1, [0, 30, 60, 90, 120, 150, 180], [0, 0.25, 0.5, 0.75, 1.0], fx, fy,
                  'firing angle α in degrees', '', lambda v: f'{v}°' if v else '0', lambda v: f'{v:g}'))
    o.append(T(x0, 40, 'V_o / V_ph', 14, 'start', MUT))
    o.append(P(curve(_r1, 0, 180, fx, fy), MUT, 2.2, '7 5'))
    o.append(P(curve(_r3, 0, 180, fx, fy, 360), AC, 3))
    o.append(L(fx(8), fy(0.6), fx(22), fy(0.6), AC, 3)); o.append(T(fx(24), fy(0.6) + 5, 'three-wire star', 13, 'start', AC, bold=True))
    o.append(L(fx(8), fy(0.5), fx(22), fy(0.5), MUT, 2.2, '7 5')); o.append(T(fx(24), fy(0.5) + 5, 'one phase with a neutral,', 13, 'start', MUT))
    o.append(T(fx(24), fy(0.5) + 23, 'or a branch inside a delta', 13, 'start', MUT))
    o.append(C(fx(60), fy(_r3(60)), 6, AC)); o.append(Tb(fx(60) - 12, fy(_r3(60)) + 22, '0.841 → 201.4 V', 13, 'end', AC, bold=True))
    o.append(C(fx(120), fy(_r3(120)), 6, AC)); o.append(Tb(fx(120) + 12, fy(_r3(120)) - 10, '0.208 → 49.8 V', 13, 'start', AC, bold=True))
    o.append(C(fx(120), fy(_r1(120)), 6, MUT)); o.append(Tb(fx(120) + 12, fy(_r1(120)) - 10, '0.442 → 105.9 V', 13, 'start', MUT, bold=True))
    o.append(T(fx(150), y1 - 10, 'zero at 150°', 13, 'middle', NX, bold=True))
    return 400, ''.join(o)


# ---- 5.4 one cycle of the chopper of the worked example (pulses drawn at 1 kHz) ----
def f4():
    o = []
    x0, x1, yc, A = 80, 690, 200, 140
    fx = lin(0, 20, x0, x1); fy = lin(-325, 325, yc + A, yc - A)
    tk = [(0, '0'), (5, '5 ms'), (10, '10 ms'), (15, '15 ms'), (20, '20 ms')]
    o.append(wave_axes(x0, x1, yc, A, tk, fx, '325 V', '', 'Load voltage for D = 0.6 (pulses drawn at 1 kHz; the example uses 10 kHz)'))
    vs = lambda t: 325.3 * math.sin(2 * math.pi * 50 * t / 1000)
    o.append(P(curve(vs, 0, 20, fx, fy), L2, 1.6, '6 5'))
    for k in range(20):
        a, b = k, k + 0.6
        o.append(P([(fx(a), yc)] + curve(vs, a, b, fx, fy, 12) + [(fx(b), yc)], AC, 1.6, fill=ACS))
    o.append(P(curve(lambda t: 0.6 * vs(t), 0, 20, fx, fy), LV, 3))
    o.append(T(fx(12.2), fy(250), 'dashed: v_s, 325 V peak', 13, 'start', MUT))
    o.append(Tb(fx(1.2), fy(0.6 * 325 * 0.8) - 4, 'D·v_s: 138.0 V RMS', 13, 'end' if False else 'start', LV, bold=True))
    o.append(Tb(fx(13.2), fy(-250), 'chopped output: 178.2 V RMS', 13, 'start', AC, bold=True))
    # zoom bracket of one period
    o.append(brace(fx(2), fx(3), yc + A + 44, INK, up=True))
    o.append(T(fx(2.5), yc + A + 62, 'one period T: on 0.6T, shorted 0.4T', 13, 'start', MUT))
    return 420, ''.join(o)


# ---- 5.5 cycloconverter output, f_o = f_s/3, alpha = 60 deg, R load ----
def f5():
    o = []
    x0, x1, yc, A = 80, 690, 214, 120
    fx = lin(0, 60, x0, x1); fy = lin(-325, 325, yc + A, yc - A)
    tk = [(0, '0'), (10, '10'), (20, '20'), (30, '30'), (40, '40'), (50, '50'), (60, '60 ms')]
    o.append(wave_axes(x0, x1, yc, A, tk, fx, '325 V', '', ''))
    o.append(T(x0, 28, 'Output of worked example 1: 16.67 Hz from 50 Hz, α = 60°', 14, 'start', bold=True))
    vs = lambda t: 325.3 * math.sin(2 * math.pi * 50 * t / 1000)
    o.append(P(curve(vs, 0, 60, fx, fy, 480), L2, 1.6, '6 5'))
    for k in range(6):
        a, b = k * 10 + 60 / 18, k * 10 + 10
        sg = 1 if k < 3 else -1
        f = lambda t, sg=sg: sg * abs(vs(t))
        o.append(P([(fx(a), yc)] + curve(f, a, b, fx, fy, 40) + [(fx(b), yc)], AC if k < 3 else LV, 2.5, fill=ACS if k < 3 else LVS))
    o.append(R(fx(0), 42, fx(30) - fx(0) - 4, 26, ACS, AC, 6)); o.append(T(fx(15), 60, 'P group fired (positive half)', 13, bold=True))
    o.append(R(fx(30) + 4, 42, fx(30) - fx(0) - 4, 26, LVS, LV, 6)); o.append(T(fx(45), 60, 'N group fired (negative half)', 13, bold=True))
    o.append(brace(fx(0), fx(60), yc + A + 46, INK, up=True))
    o.append(T(fx(30), yc + A + 66, 'one output period T_o = 60 ms: 206.3 V RMS into 10 Ω', 13, fill=MUT))
    o.append(T(fx(1.2), yc - 70, 'v_s', 13, 'start', MUT))
    return 414, ''.join(o)


# ---- 5.6 the nine-switch array and the duty cycles of output A ----
def f6():
    o = []
    ys = {'a': 80, 'b': 140, 'c': 200}
    xo = {'A': 300, 'B': 440, 'C': 580}
    o.append(R(40, 60, 120, 160, PANEL, L2, 8)); o.append(T(100, 132, 'LC filter', 14, bold=True)); o.append(T(100, 152, '415 V, 50 Hz', 13, fill=MUT))
    for n, y in ys.items():
        o.append(L(160, y, 640, y, INK, 2)); o.append(T(178, y - 8, f'input {n}', 13, 'start', MUT))
    for n, x in xo.items():
        o.append(L(x, 56, x, 262, INK, 2))
        o.append(R(x - 44, 262, 88, 30, ACS if n == 'A' else PANEL, AC, 6)); o.append(T(x, 282, f'output {n}', 13, bold=True))
        for m, y in ys.items():
            hot = n == 'A'
            o.append(f'<circle cx="{x}" cy="{y}" r="14" style="fill:{"var(--live-soft)" if hot else "var(--panel)"};stroke:{"var(--live)" if hot else "var(--accent)"};stroke-width:2"/>')
            o.append(T(x + 18, y + 22, f'S_{n}{m}', 13, 'start', LV if hot else INK, bold=hot))
    o.append(T(370, 316, 'load (star, 20 Ω per phase), 30 Hz output', 13, fill=MUT))
    # duty bar for output A
    y = 360; X0, X1 = 80, 680; fx = lin(0, 100, X0, X1)
    o.append(T(X0, y - 12, 'Output A over one 100 µs switching period (worked example 2)', 14, 'start', bold=True))
    for a, b, lab, fill in ((0, 53.0, 'on input a: 53.0 µs', LVS), (53.0, 76.5, 'b: 23.5 µs', ACS), (76.5, 100, 'c: 23.5 µs', NXS)):
        o.append(R(fx(a), y, fx(b) - fx(a), 36, fill, AC, 3)); o.append(T((fx(a) + fx(b)) / 2, y + 23, lab, 13, bold=True))
    o.append(T(380, y + 64, '0.530 × 338.9 V + 0.470 × (−169.4 V) = 100.0 V average', 13, fill=MUT))
    return 444, ''.join(o)


FIG = {
    1: (f1, 'Load voltage of the two worked examples. With the resistor each SCR conducts from α to the voltage zero; with the R-L load the current lags, so each SCR conducts on to β = 224.2° and the load sees part of the negative half wave.',
        'Two waveform panels: a 20 ohm load fired at 90 degrees, and an R-L load fired at 60 degrees whose current ends at 224.2 degrees.'),
    2: (f2, 'The dimmer of the worked examples. The capacitor voltage lags the supply by 72.3° and reaches the 30 V DIAC breakover at 90°, so the TRIAC fires at α = 90° in both half cycles.',
        'Circuit of a 230 volt lamp dimmer with lamp, TRIAC, 100 kilohm resistor, 0.1 microfarad capacitor and DIAC, above the capacitor voltage crossing plus and minus 30 volts at 90 and 270 degrees.'),
    3: (f3, 'RMS output of a three-wire star controller with a resistive load, as a fraction of the supply phase voltage. It falls to zero at 150°; the dashed curve is one phase with a neutral, which reaches zero only at 180°.',
        'Plot of output ratio against firing angle with three shaded ranges, marked at 60 degrees (0.841) and 120 degrees (0.208), and a dashed single-phase curve.'),
    4: (f4, 'One supply cycle of the chopper of the worked example with D = 0.6. Each period passes 0.6 of the supply wave and shorts the load for the rest; the 50 Hz part of the output is 0.6 times the supply.',
        'Chopped load voltage pulses under a 50 hertz sine, with the smooth 0.6 times supply curve drawn through them.'),
    5: (f5, 'Output of worked example 1. The P group gives three positive humps, the N group three negative ones, so one output cycle spans three supply cycles: 60 ms, or 16.67 Hz.',
        'Three positive and three negative phase-controlled humps over 60 milliseconds under a dashed 50 hertz supply wave.'),
    6: (f6, 'The nine switches of a matrix converter. The three that feed output A are shaded; in worked example 2 they share each 100 µs period as 53.0, 23.5 and 23.5 µs to make an average of 100 V.',
        'Grid of three input lines and three output lines with a switch at each crossing, and a bar dividing 100 microseconds among inputs a, b and c.'),
}
spec = make_spec(FIG)
