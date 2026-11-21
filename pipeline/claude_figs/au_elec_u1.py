"""Claude's hand-drawn figures for au-elec-u1 (Automotive Electrical and Electronics: vehicle power supply, EMC, batteries,
charging, alternator, starting and power distribution), one per chapter, drawn from each chapter's own worked example and
numbers. Curves are computed from the chapter models (alternator I = Imax(1 - n0/n), straight-line torque curves,
reserve-capacity discharge curves that cross 10.5 V at the stated times). Colours are the shell's CSS variables."""
import os, sys, math, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

_T, _Tb, _boxt = T, Tb, boxt


def _sub(s):
    return re.sub(r'([A-Za-zα-ωΔ])_([A-Za-z0-9]+)', r'\1<tspan baseline-shift="sub" font-size="11">\2</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)
def boxt(x, y, w, h, lines, *a, **k): return _boxt(x, y, w, h, [_sub(l) for l in lines], *a, **k)


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


# ---- circuit symbols ----
def gnd(x, y, c=INK):
    return L(x, y, x, y + 8, c, 2) + L(x - 12, y + 8, x + 12, y + 8, c, 2) + L(x - 7, y + 13, x + 7, y + 13, c, 2) + L(x - 3, y + 18, x + 3, y + 18, c, 2)


def batt(x, y, c=INK):
    """vertical battery: long plate (+) on top at y, short plate below"""
    return (L(x - 16, y, x + 16, y, c, 3) + L(x - 9, y + 9, x + 9, y + 9, c, 5) + L(x - 16, y + 18, x + 16, y + 18, c, 3) + L(x - 9, y + 27, x + 9, y + 27, c, 5))


def fuse_h(x, y, w=36):
    return R(x - w / 2, y - 7, w, 14, PANEL, AC, 3) + L(x - w / 2, y, x + w / 2, y, AC, 1.5)


def lamp(x, y, r=13, c=AC):
    d = r * 0.7
    return (f'<circle cx="{x}" cy="{y}" r="{r}" style="fill:var(--panel);stroke:{c};stroke-width:2"/>' + L(x - d, y - d, x + d, y + d, c, 1.8) + L(x - d, y + d, x + d, y - d, c, 1.8))


def switch_h(x1, x2, y, c=INK, closed=False):
    """horizontal switch between x1 and x2"""
    o = C(x1, y, 3.5, c) + C(x2, y, 3.5, c)
    o += L(x1, y, x2 - 2, y if closed else y - 14, c, 2)
    return o


def diode_v(x, y, up=True, c=AC, s=10):
    """diode on a vertical wire, pointing up (anode below) or down"""
    if up:
        return f'<path d="M{x - s},{y + s * 0.8} L{x + s},{y + s * 0.8} L{x},{y - s * 0.8} Z" style="fill:{c};stroke:{c};stroke-width:1"/>' + L(x - s, y - s * 0.8, x + s, y - s * 0.8, c, 2.5)
    return f'<path d="M{x - s},{y - s * 0.8} L{x + s},{y - s * 0.8} L{x},{y + s * 0.8} Z" style="fill:{c};stroke:{c};stroke-width:1"/>' + L(x - s, y + s * 0.8, x + s, y + s * 0.8, c, 2.5)


def motor(x, y, r=20, c=AC):
    return f'<circle cx="{x}" cy="{y}" r="{r}" style="fill:var(--panel);stroke:{c};stroke-width:2.5"/>' + T(x, y + 6, 'M', 17, bold=True, fill=c)


FIG = {}


# ---- 1.1 evolution timeline ----
def f1():
    o = []
    x0, x1, y = 50, 680, 120
    o.append(L(x0 - 20, y, x1 + 20, y, L2, 3, arrow='m'))
    ms = [(1912, 'electric', 'self-starter'), ('1950s', '6 V → 12 V', 'systems'), (1960, 'alternator', 'replaces dynamo'),
          ('1970s', 'electronic', 'ignition'), ('1980s', 'fuel injection', 'and ECU'), (1991, 'CAN bus', 'in a car'), ('2010s', 'ADAS,', '48 V, EVs')]
    xs = [x0 + i * (x1 - x0) / (len(ms) - 1) for i in range(len(ms))]
    for X, (yr, a, b) in zip(xs, ms):
        o.append(C(X, y, 7, AC))
        o.append(T(X, y - 18, str(yr), 15, bold=True))
        o.append(T(X, y + 30, a, 13)); o.append(T(X, y + 47, b, 13, fill=MUT))
    # what pushed each step
    bands = [(0, 2, 'more electrical loads', AC, ACS), (3, 4, 'emission laws', LV, LVS), (5, 6, 'safety, comfort, networks', NX, NXS)]
    for i0, i1, lab, c, fill in bands:
        a, b = xs[i0] - 40, xs[i1] + 40
        o.append(R(a, 190, b - a, 34, fill, c, 6))
        o.append(T((a + b) / 2, 212, lab, 14, bold=True))
    o.append(T(360, 36, 'each step solved a load or a law and made the next one possible', 14, fill=MUT))
    return 240, ''.join(o)


FIG[1] = (f1, 'From hand cranking to networked control. Growing loads pushed the early steps (12 V, the alternator); emission laws pushed engine electronics; safety and comfort pushed networks and driver assistance.',
          'A timeline from 1912 to the 2010s: electric self-starter, 6 V to 12 V, the alternator in 1960, electronic ignition, fuel injection and ECU, CAN bus in 1991, ADAS and 48 V. Bands below show the pressure behind each group of steps.')


# ---- 1.2 headlamp circuit diagram with the sized feed wire ----
def f2():
    o = []
    top, bot = 60, 300
    o.append(T(30, 30, '30 (battery +, always live)', 14, 'start', bold=True))
    o.append(L(60, top, 470, top, INK, 2.5))
    # battery at left
    o.append(L(60, top, 60, 150, INK, 2)); o.append(batt(60, 150)); o.append(L(60, 177, 60, bot - 8, INK, 2)); o.append(gnd(60, bot - 8))
    o.append(T(84, 168, '12 V', 14, 'start', bold=True))
    # fuse and relay contact on the load branch
    xb = 470
    o.append(L(xb, top, xb, 92, INK, 2)); o.append(f'<g transform="rotate(90 {xb} 107)">{fuse_h(xb, 107, 30)}</g>'); o.append(T(xb + 16, 112, 'fuse 15 A', 13, 'start', MUT))
    o.append(L(xb, 122, xb, 140, INK, 2))
    # relay box
    o.append(R(270, 132, 250, 70, 'none', L2, 8, 1.5, dash='5 4')); o.append(T(395, 222, 'relay', 13, fill=MUT))
    o.append(C(xb, 142, 3.5, INK)); o.append(L(xb, 142, xb - 12, 178, INK, 2)); o.append(C(xb, 182, 3.5, INK))
    o.append(T(xb + 10, 150, '30', 13, 'start', MUT)); o.append(T(xb + 10, 190, '87', 13, 'start', MUT))
    # coil
    o.append(R(300, 150, 36, 30, PANEL, AC, 3)); o.append(L(300, 180, 336, 150, AC, 1.5))
    o.append(T(296, 146, '86', 13, 'end', MUT)); o.append(T(296, 194, '85', 13, 'end', MUT))
    o.append(L(318, 150, 318, 108, INK, 1.5)); o.append(switch_h(200, 240, 108)); o.append(L(240, 108, 318, 108, INK, 1.5))
    o.append(L(140, 108, 200, 108, INK, 1.5)); o.append(T(140, 98, '15', 13, 'start', MUT)); o.append(T(220, 130, 'lamp switch', 13, fill=MUT))
    o.append(L(318, 180, 318, bot - 8, INK, 1.5)); o.append(gnd(318, bot - 8))
    # feed wire to two lamps
    o.append(L(xb, 186, xb, 236, LV, 4)); o.append(L(xb, 236, 640, 236, LV, 4))
    for X in (580, 640):
        o.append(L(X, 236, X, 247, LV, 3)); o.append(lamp(X, 260)); o.append(L(X, 273, X, bot - 8, INK, 2)); o.append(gnd(X, bot - 8))
    o.append(T(610, 222, '56b: 2 × 55 W', 13, bold=True))
    o.append(Tb(540, 260, '2.5 mm², 4.0 m', 13, 'end', LV, bold=True))
    o.append(T(510, 280, 'I = 9.17 A', 13, 'end', LV))
    o.append(T(30, 335, '31 (ground): every return goes to the body and battery −. The feed drops 9.17 A × 0.0275 Ω = 0.25 V.', 13, 'start', MUT))
    return 350, ''.join(o)


FIG[2] = (f2, 'The worked example as a circuit diagram: the lamp switch on terminal 15 works the relay coil (86, 85), and the relay contact (30, 87) feeds both low beams through the 2.5 mm² wire.',
          'Circuit diagram of a headlamp relay circuit: battery, 15 A fuse, relay coil 86-85 switched from terminal 15, relay contact 30-87 feeding two 55 W lamps through a 2.5 mm² wire 4 m long, all returns to ground.')


# ---- 1.3 EMC: source, path, sink ----
def f3():
    o = []
    cols = [(20, 'Source', ['ignition spark', 'commutator motors', 'relay and injector coils', 'alternator diodes'], 'fix at source: diode on coils,', 'capacitors, resistor plugs', AC, ACS),
            (260, 'Coupling path', ['conducted (shared ground)', 'capacitive (dv/dt)', 'inductive (di/dt, loops)', 'radiated (wire as aerial)'], 'on the path: short routes,', 'twisted pairs, screens, straps', LV, LVS),
            (500, 'Sink', ['radio and GPS', 'ECU inputs', 'sensor lines', 'data buses'], 'at the sink: filters,', 'metal housings, plausibility', NX, NXS)]
    for x, title, items, r1, r2, c, fill in cols:
        o.append(R(x, 40, 200, 196, fill, c, 10))
        o.append(T(x + 100, 66, title, 15, bold=True))
        for i, it in enumerate(items):
            o.append(R(x + 12, 80 + i * 37, 176, 30, PANEL, c, 6)); o.append(T(x + 100, 100 + i * 37, it, 13))
        o.append(T(x + 100, 262, r1, 13, fill=MUT)); o.append(T(x + 100, 279, r2, 13, fill=MUT))
    o.append(L(222, 138, 256, 138, AC, 3, arrow='n')); o.append(L(462, 138, 496, 138, LV, 3, arrow='l'))
    # worked example strip
    o.append(R(20, 296, 680, 52, PANEL, L2, 8))
    o.append(T(360, 318, 'relay coil 0.20 H, 0.141 A: unsuppressed it tries for 14 kV; a diode clamps it to 12.7 V', 13))
    o.append(T(360, 338, 'fan filter 5 µH + 1 µF: cut-off 71.2 kHz, about 46 dB less noise at 1 MHz', 13))
    return 360, ''.join(o)


FIG[3] = (f3, 'Every EMC problem is a source, a coupling path and a sink; suppression is applied at all three. The strip repeats the two worked examples.',
          'Three columns: sources (ignition, motors, coils, alternator), coupling paths (conducted, capacitive, inductive, radiated) and sinks (radio, ECU inputs, sensors, buses), with the remedy under each. A strip at the bottom gives the relay-coil and filter numbers.')


# ---- 1.4 lead-acid cell ----
def f4():
    o = []
    # case of one cell
    o.append(R(40, 70, 330, 230, 'none', INK, 6, 2.5))
    o.append(R(42, 110, 326, 188, LVS, 'none', 4, 0))
    o.append(L(42, 110, 368, 110, LV, 1.5, dash='6 4')); o.append(T(380, 114, 'acid level', 13, 'start', LV))
    xs = [70, 110, 150, 190, 230, 270, 310]
    for i, x in enumerate(xs):
        pos = i % 2 == 1
        o.append(R(x - 7, 92, 14, 190, ACS if pos else PANEL, AC if pos else INK, 2, 2))
        if i < len(xs) - 1:
            o.append(L(x + 20, 100, x + 20, 282, L2, 1.5, dash='3 3'))
    # straps and posts
    o.append(L(63, 86, 317, 86, INK, 3)); o.append(L(103, 80, 283, 80, AC, 3))
    for x in (70, 150, 230, 310): o.append(L(x, 86, x, 92, INK, 3))
    for x in (110, 190, 270): o.append(L(x, 82, x, 90, 'var(--fig)', 7)); o.append(L(x, 80, x, 92, AC, 3))
    o.append(L(103, 80, 103, 50, AC, 4)); o.append(L(317, 86, 317, 50, INK, 4))
    o.append(T(103, 42, '+', 18, bold=True, fill=AC)); o.append(T(317, 42, '−', 18, bold=True))
    o.append(T(205, 330, 'one cell: plates alternate, separators between', 13, fill=MUT))
    # labels to the right
    lab = [(110, 150, 'positive plate: PbO₂', AC), (150, 200, 'negative plate: spongy Pb', INK), (170, 250, 'separator (porous)', MUT), (300, 290, 'dilute H₂SO₄, SG 1.28', LV)]
    for x, yy, s, c in lab:
        o.append(L(x + 9, yy, 420, yy, c, 1.2)); o.append(T(428, yy + 5, s, 13, 'start', c))
    # six cells in series
    o.append(T(40, 375, 'six cells in series:', 14, 'start', bold=True))
    for i in range(6):
        x = 190 + i * 50
        o.append(R(x, 354, 42, 30, PANEL, AC, 4)); o.append(T(x + 21, 374, '2.1 V', 13))
        if i < 5: o.append(L(x + 42, 369, x + 50, 369, INK, 2))
    o.append(T(500, 375, '= 12.6 V at rest', 14, 'start', bold=True, fill=AC))
    o.append(T(428, 120 - 40, 'cell V ≈ SG + 0.84', 13, 'start', MUT))
    return 400, ''.join(o)


FIG[4] = (f4, 'One cell of the battery: positive plates of lead dioxide and negative plates of spongy lead alternate with porous separators in dilute sulfuric acid. Six such cells in series give 12.6 V at rest.',
          'Cutaway of one lead-acid cell with alternating positive and negative plates joined by straps to the + and − posts, separators between them and the acid level marked; beside it six 2.1 V cells in series making 12.6 V.')


# ---- 1.5 reserve capacity discharge curves ----
def f5():
    o = []
    x0, x1, y0, y1 = 80, 680, 50, 290
    fx = lin(0, 120, x0, x1); fy = lin(9.5, 13.0, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0, 20, 40, 60, 80, 100, 120], [10, 10.5, 11, 12, 13], fx, fy, 'time at 25 A (min)', 'terminal voltage (V)', yfmt=lambda v: f'{v:g}'))
    o.append(L(x0, fy(10.5), x1, fy(10.5), NX, 1.8, dash='6 4')); o.append(Tb(x0 + 8, fy(10.5) + 20, 'end voltage 10.5 V', 13, 'start', NX))

    def curve(A, B, tau, T0):
        Cc = (A - B * T0 - 10.5) / math.exp(T0 / tau)
        pts = []
        t = 0.0
        while t <= 120:
            v = A - B * t - Cc * math.exp(t / tau)
            if v < 9.6: break
            pts.append((fx(t), fy(v))); t += 1
        return pts
    o.append(P(curve(12.5, 0.008, 12, 100), AC, 3)); o.append(P(curve(12.3, 0.012, 10, 72), LV, 3))
    o.append(C(fx(100), fy(10.5), 6, AC)); o.append(C(fx(72), fy(10.5), 6, LV))
    o.append(T(fx(100), y1 + 56, '', 13))
    o.append(Tb(fx(100) - 6, fy(10.5) - 14, '100 min: rated RC', 13, 'end', AC, bold=True))
    o.append(Tb(fx(72) - 8, fy(10.5) + 26, 'battery B: 72 min = 30 Ah', 13, 'end', LV, bold=True))
    o.append(T(fx(30), fy(12.35) - 10, 'good battery', 13, fill=AC, bold=True)); o.append(T(fx(30), fy(11.75) + 22, 'battery B', 13, fill=LV, bold=True))
    return 345, ''.join(o)


FIG[5] = (f5, 'The reserve-capacity test of the worked example at 25 A: a battery that meets its 100 min rating reaches 10.5 V at 100 min; battery B gets there after 72 min, having delivered only 30 Ah.',
          'Two discharge curves at 25 A on a voltage-time plot: the good battery stays above 10.5 V until 100 minutes; battery B falls to 10.5 V at 72 minutes.')


# ---- 1.6 charging circuit ----
def f6():
    o = []
    # alternator box
    o.append(R(40, 60, 330, 250, 'none', AC, 10, 2.5)); o.append(T(205, 50, 'alternator', 15, bold=True, fill=AC))
    o.append(boxt(60, 80, 100, 50, ['stator', '3 phases'], PANEL, AC, 13))
    o.append(boxt(200, 80, 150, 50, ['6 power diodes'], PANEL, AC, 13))
    o.append(boxt(200, 150, 150, 50, ['3 exciter diodes'], PANEL, AC, 13))
    o.append(boxt(200, 230, 150, 56, ['regulator', 'senses voltage'], LVS, LV, 13))
    o.append(boxt(60, 230, 100, 56, ['field', 'winding (DF)'], PANEL, AC, 13))
    o.append(L(160, 105, 200, 105, AC, 2, arrow='n')); o.append(L(160, 118, 200, 168, AC, 2, arrow='n'))
    o.append(L(200, 258, 160, 258, LV, 2, arrow='l'))
    o.append(L(275, 200, 275, 230, AC, 2, arrow='n'))
    # terminals
    o.append(L(350, 105, 470, 105, AC, 4)); o.append(T(380, 96, 'B+', 14, bold=True))
    o.append(L(350, 175, 395, 175, AC, 2)); o.append(T(372, 166, 'D+', 14, bold=True))
    # battery and loads
    o.append(L(470, 105, 540, 105, AC, 4)); o.append(Tb(462, 128, '10 mm², 1.2 m', 13, 'middle', AC))
    o.append(L(540, 105, 540, 160, INK, 2)); o.append(batt(540, 160)); o.append(L(540, 187, 540, 300, INK, 2)); o.append(gnd(540, 300))
    o.append(T(566, 180, '12.4 V', 13, 'start', bold=True))
    o.append(L(540, 105, 660, 105, INK, 2)); o.append(R(630, 120, 60, 40, PANEL, INK, 6)); o.append(T(660, 145, 'loads', 13)); o.append(L(660, 105, 660, 120, INK, 2))
    o.append(L(660, 160, 660, 300, INK, 2)); o.append(gnd(660, 300))
    # ignition switch and lamp to D+
    o.append(L(600, 105, 600, 60, INK, 1.5)); o.append(L(600, 60, 560, 60, INK, 1.5)); o.append(switch_h(520, 560, 60)); o.append(T(540, 40, 'ignition 15', 13, fill=MUT))
    o.append(L(520, 60, 470, 60, INK, 1.5)); o.append(lamp(450, 60, 12, NX)); o.append(L(438, 60, 395, 60, INK, 1.5)); o.append(L(395, 60, 395, 175, INK, 1.5))
    o.append(T(450, 36, 'charge lamp', 13, fill=NX))
    # sense wire
    o.append(P([(350, 270), (500, 270), (500, 200), (528, 200)], LV, 2, dash='6 4')); o.append(T(440, 292, 'sense wire (no current)', 13, fill=LV))
    o.append(T(20, 336, 'key on: battery → key → lamp → D+ → field; running: the exciter diodes feed the field', 13, 'start', MUT))
    return 350, ''.join(o)


FIG[6] = (f6, 'Inside the alternator, six power diodes feed B+ and three exciter diodes feed D+ and the field through the regulator. At key-on the charge lamp gives the first field current; the dashed sense wire lets the regulator see the true battery voltage.',
          'Charging circuit: alternator box with stator, six power diodes to B+, three exciter diodes to D+, regulator and field winding; B+ cable 10 mm² 1.2 m to the battery and loads; ignition switch and charge lamp feeding D+; a dashed sense wire from the regulator to the battery.')


# ---- 1.7 alternator current curve ----
def f7():
    o = []
    x0, x1, y0, y1 = 80, 680, 50, 290
    fx = lin(0, 10000, x0, x1); fy = lin(0, 160, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0, 2000, 4000, 6000, 8000, 10000], [0, 40, 80, 120, 160], fx, fy, 'alternator speed (rpm)', 'output current at 14 V (A)'))
    o.append(L(x0, fy(144), x1, fy(144), L2, 1.5, dash='6 4')); o.append(Tb(x1 - 4, fy(144) - 8, 'I_max = 144 A', 13, 'end', MUT))
    pts = [(fx(n), fy(144 * (1 - 1000 / n))) for n in range(1000, 10001, 100)]
    o.append(L(x0, fy(0), fx(1000), fy(0), AC, 3)); o.append(P(pts, AC, 3))
    o.append(L(x0, fy(70), x1, fy(70), NX, 1.8, dash='6 4')); o.append(Tb(fx(9000), fy(70) + 20, 'loads 70 A', 13, 'middle', NX, bold=True))
    for n, lab, dx, dy, anc in [(1000, 'n₀ = 1000 rpm', 10, -12, 'start'), (2000, 'idle 2000 rpm: 72 A', 12, 4, 'start'), (6000, 'rated 6000 rpm: 120 A', 0, -16, 'middle')]:
        I = 144 * (1 - 1000 / n)
        o.append(C(fx(n), fy(I), 6, AC if n != 2000 else LV))
        o.append(Tb(fx(n) + dx, fy(I) + dy, lab, 13, anc, LV if n == 2000 else INK, bold=True))
    return 345, ''.join(o)


FIG[7] = (f7, 'The worked example\'s alternator, I = 144(1 − 1000 ÷ n): nothing below 1000 rpm, 72 A at the 2000 rpm idle, 120 A at the rated 6000 rpm, and never more than 144 A, because the stator reactance grows with speed.',
          'Output current against alternator speed: zero up to 1000 rpm, then rising steeply to 72 A at 2000 rpm and 120 A at 6000 rpm, flattening below a dashed 144 A line; a dashed 70 A load line crosses the curve just below the idle point.')


# ---- 1.8 loss budget and field PWM ----
def f8():
    o = []
    x0, W = 40, 640
    parts = [('output 980 W', 980, ACS, AC), ('diodes 126', 126, NXS, NX), ('iron, brush, fan 77.5', 77.5, PANEL, L2), ('stator Cu 68.5', 68.5, LVS, LV), ('field Cu 48', 48, LVS, LV)]
    o.append(T(40, 34, 'input 1300 W at the pulley (14.0 V, 70 A out)', 14, 'start', bold=True))
    x = x0
    for lab, v, fill, c in parts:
        w = W * v / 1300
        o.append(R(x, 48, w, 44, fill, c, 3))
        if v == 980: o.append(T(x + w / 2, 76, '980 W out (75.4 %)', 14, bold=True))
        x += w
    # loss labels below with leaders
    x = x0 + W * 980 / 1300
    labs = [('diodes 126 W', 126), ('iron, brush, bearings, fan 77.5 W', 77.5), ('stator copper 68.5 W', 68.5), ('field copper 48 W', 48)]
    ly = 116
    for i, (lab, v) in enumerate(labs):
        w = W * v / 1300
        cx = x + w / 2
        yy = ly + i * 20
        o.append(L(cx, 92, cx, yy - 4, L2, 1.2)); o.append(T(cx - 6, yy + 1, lab, 13, 'end', MUT))
        x += w
    o.append(T(40, 116, 'losses 320 W:', 13, 'start', bold=True))
    # PWM waveform
    by, top = 312, 250
    o.append(T(40, 206, 'field PWM: on 85.7 % of each period', 14, 'start', bold=True))
    xs0, per = 60, 150
    pts = [(xs0 - 20, by)]
    for i in range(4):
        a = xs0 + i * per
        pts += [(a, by), (a, top), (a + per * 0.857, top), (a + per * 0.857, by)]
    pts.append((xs0 + 4 * per, by))
    o.append(P(pts, AC, 2.5))
    o.append(L(xs0 - 20, by, xs0 + 4 * per + 10, by, L2, 1))
    o.append(T(xs0 - 26, top + 5, '14 V', 13, 'end', MUT)); o.append(T(xs0 - 26, by + 5, '0', 13, 'end', MUT))
    o.append(brace(xs0, xs0 + per * 0.857, top - 10, INK, up=True)); o.append(T(xs0 + per * 0.43, top - 20, 'D = 0.857', 13, bold=True))
    o.append(T(xs0 + 2 * per, by + 26, 'average field current = 0.857 × 14.0 V ÷ 3.0 Ω = 4.0 A', 13, fill=MUT))
    return 352, ''.join(o)


FIG[8] = (f8, 'Where the 1300 W of the worked examples goes: 980 W reaches the bus and 320 W becomes heat, the diodes taking the largest share. Below, the regulator switches the field on for 85.7 % of each period to give 4.0 A.',
          'A bar split into 980 W output and losses of 126 W in the diodes, 77.5 W iron and mechanical, 68.5 W stator copper and 48 W field copper; below, a PWM waveform with duty cycle 0.857 giving a 4.0 A average field current.')


# ---- 1.9 stable cranking point, warm and cold ----
def f9():
    o = []
    x0, x1, y0, y1 = 80, 680, 50, 290
    fx = lin(0, 320, x0, x1); fy = lin(0, 70, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0, 40, 80, 120, 160, 200, 240, 280, 320], [0, 10, 20, 30, 40, 50, 60, 70], fx, fy, 'cranking speed (rpm)', 'torque at the crankshaft (N·m)'))
    o.append(f'<rect x="{x0:.1f}" y="{y0:.1f}" width="{fx(80) - x0:.1f}" height="{y1 - y0:.1f}" style="fill:var(--next-soft);fill-opacity:0.6"/>')
    o.append(T(fx(40), fy(26), 'below 80 rpm:', 13, fill=NX)); o.append(T(fx(40), fy(26) + 16, 'no start', 13, fill=NX))
    o.append(P([(fx(0), fy(65)), (fx(320), fy(33))], AC, 3)); o.append(P([(fx(0), fy(10)), (fx(320), fy(42))], AC, 3, dash='7 4'))
    o.append(P([(fx(0), fy(55)), (fx(320), fy(23))], LV, 3)); o.append(P([(fx(0), fy(30)), (fx(266), fy(69.9))], LV, 3, dash='7 4'))
    o.append(C(fx(275), fy(37.5), 7, AC)); o.append(Tb(fx(275), fy(37.5) + 26, 'warm: 275 rpm, 37.5 N·m, 1080 W', 13, 'end', AC, bold=True))
    o.append(C(fx(100), fy(45), 7, LV)); o.append(Tb(fx(100) + 12, fy(45) - 14, 'cold: 100 rpm, 45 N·m, 471 W', 13, 'start', LV, bold=True))
    o.append(T(fx(300), fy(30) - 6, 'starter', 13, 'end', AC)); o.append(T(fx(230), fy(62), 'cold resistance', 13, 'end', LV))
    o.append(T(fx(160), fy(14), 'solid: starter torque; dashed: engine resistance', 13, fill=MUT))
    return 345, ''.join(o)


FIG[9] = (f9, 'The two cranking points of the worked example. Thick cold oil lifts the resistance line and the weak battery lowers the starter line, so the meeting point falls from 275 rpm to 100 rpm, still just above the 80 rpm this engine needs.',
          'Torque against cranking speed: warm starter and resistance lines meet at 275 rpm and 37.5 N·m; cold lines meet at 100 rpm and 45 N·m; the band below 80 rpm is marked no start.')


# ---- 1.10 starter control and power circuits ----
def f10():
    o = []
    # battery and the heavy power circuit
    o.append(L(60, 70, 60, 150, LV, 5)); o.append(batt(60, 150)); o.append(L(60, 177, 60, 320, INK, 3)); o.append(gnd(60, 320))
    o.append(T(84, 170, '12.6 V', 13, 'start', bold=True))
    o.append(L(60, 70, 470, 70, LV, 5)); o.append(T(260, 60, 'terminal 30: heavy cable', 13, fill=LV, bold=True))
    # solenoid main contacts
    o.append(C(470, 70, 5, LV)); o.append(C(560, 70, 5, LV)); o.append(L(474, 84, 556, 84, LV, 5)); o.append(T(515, 52, 'main contacts', 13, fill=MUT))
    o.append(L(560, 70, 640, 70, LV, 5)); o.append(L(640, 70, 640, 190, LV, 5)); o.append(motor(640, 210, 22, LV)); o.append(L(640, 232, 640, 320, INK, 3)); o.append(gnd(640, 320))
    o.append(T(672, 150, '250 A', 15, 'start', LV, bold=True)); o.append(T(672, 215, 'motor', 13, 'start', MUT))
    # control: ignition switch terminal 50 -> relay coil
    o.append(L(110, 70, 110, 130, INK, 1.5)); o.append(switch_h(110, 150, 130)); o.append(T(130, 152, 'key START', 13, fill=MUT))
    o.append(L(150, 130, 200, 130, INK, 1.5)); o.append(R(200, 118, 34, 24, PANEL, AC, 3)); o.append(T(217, 112, 'relay coil 0.2 A', 13, fill=AC))
    o.append(L(234, 130, 250, 130, INK, 1.5)); o.append(L(250, 130, 250, 320, INK, 1.5)); o.append(gnd(250, 320))
    # relay contact from 30 to terminal 50 via neutral switch
    o.append(L(300, 70, 300, 175, INK, 2)); o.append(switch_h(300, 340, 175, closed=True)); o.append(T(320, 200, 'relay contact', 13, fill=MUT))
    o.append(L(340, 175, 360, 175, INK, 2)); o.append(switch_h(360, 400, 175, closed=True)); o.append(T(380, 160, 'neutral', 13, fill=MUT))
    o.append(L(400, 175, 440, 175, NX, 3)); o.append(T(420, 196, '50', 14, bold=True, fill=NX))
    # solenoid coils
    o.append(R(440, 150, 150, 110, 'none', NX, 8, 1.5, dash='5 4')); o.append(T(515, 280, 'solenoid', 13, fill=NX, bold=True))
    o.append(L(440, 175, 470, 175, NX, 2)); o.append(L(470, 175, 470, 190, NX, 2)); o.append(R(456, 190, 28, 40, NXS, NX, 3)); o.append(T(470, 248, 'hold-in', 13, fill=NX))
    o.append(L(470, 230, 470, 320, INK, 1.5)); o.append(gnd(470, 320))
    o.append(L(470, 175, 560, 175, NX, 2)); o.append(R(546, 190, 28, 40, NXS, NX, 3)); o.append(T(560, 248, 'pull-in', 13, fill=NX))
    o.append(L(560, 175, 560, 190, NX, 2)); o.append(L(560, 230, 600, 230, NX, 2)); o.append(L(600, 230, 600, 150, NX, 2)); o.append(L(600, 150, 640, 150, NX, 2))
    o.append(T(524, 140, '40 A, then 10 A', 13, 'start', NX, bold=True))
    o.append(L(515, 150, 515, 92, NX, 1.5, dash='4 3', arrow='x'))
    return 345, ''.join(o)


FIG[10] = (f10, 'The two circuits of a pre-engaged starter. The key works a relay coil (0.2 A); its contact feeds terminal 50 and the solenoid coils (40 A, then 10 A once the pull-in coil is shorted out); the plunger closes the main contacts, and 250 A flows from terminal 30 through the motor.',
          'Starter circuits: battery and heavy terminal-30 cable through the solenoid main contacts to the motor and ground carrying 250 A; key switch and relay coil at 0.2 A; relay contact and neutral switch feeding terminal 50; hold-in coil to ground and pull-in coil to the motor terminal, 40 A then 10 A.')


# ---- 1.11 power distribution and the voltage domains ----
def f11():
    o = []
    o.append(boxt(20, 40, 110, 50, ['battery', '12.6 V'], PANEL, INK, 13))
    o.append(L(130, 65, 160, 65, LV, 4)); o.append(boxt(160, 45, 90, 40, ['main fuse'], PANEL, LV, 13))
    o.append(L(250, 65, 280, 65, LV, 4)); o.append(boxt(280, 30, 150, 70, ['power', 'distribution box'], ACS, AC, 13))
    rows = [(140, 'fuse 20 A', 'heater 15 A', '1.5 mm²'), (200, 'fuse 15 A + relay', 'headlamps 9.2 A', '2.5 mm²'), (260, 'terminal 15', 'ignition coil', 'primary')]
    for y, a, b, w in rows:
        o.append(P([(355, 100), (355, y), (380, y)], AC, 2))
        o.append(boxt(380, y - 18, 140, 36, [a], PANEL, AC, 13))
        o.append(L(520, y, 545, y, AC, 2, arrow='n')); o.append(boxt(548, y - 18, 150, 36, [b], PANEL, INK, 13))
        o.append(T(532, y - 24, w, 13, fill=MUT))
    # ignition secondary
    o.append(L(623, 278, 623, 304, NX, 3, arrow='x')); o.append(boxt(548, 306, 150, 40, ['secondary up to', '35 kV → plugs'], NXS, NX, 13))
    # EV domain
    o.append(R(20, 130, 300, 216, 'none', L2, 10, 1.5, dash='6 4')); o.append(T(170, 152, 'electric vehicle only', 13, fill=MUT, bold=True))
    o.append(boxt(36, 166, 120, 44, ['traction battery', 'about 400 V'], PANEL, L2, 13))
    o.append(boxt(180, 166, 124, 44, ['contactors,', 'pre-charge'], PANEL, L2, 13))
    o.append(L(156, 188, 178, 188, L2, 2, arrow='m'))
    o.append(boxt(180, 236, 124, 40, ['inverter, motor'], PANEL, L2, 13)); o.append(L(242, 210, 242, 234, L2, 2, arrow='m'))
    o.append(boxt(36, 236, 120, 40, ['DC-DC to 12 V'], PANEL, L2, 13)); o.append(L(96, 210, 96, 234, L2, 2, arrow='m'))
    o.append(T(170, 308, 'orange cables, isolation monitor,', 13, fill=MUT)); o.append(T(170, 326, 'service disconnect', 13, fill=MUT))
    return 360, ''.join(o)


FIG[11] = (f11, 'The 12 V tree from the battery through the main fuse and the distribution box to fused, relay-switched loads, with the heater of the fuse example; the ignition coil makes its own kilovolt domain, and an electric vehicle adds a separate traction domain.',
           'Power distribution: battery, main fuse and distribution box feeding a 20 A fuse to a 15 A heater on 1.5 mm² wire, a fuse and relay to the headlamps, and terminal 15 to the ignition coil whose secondary gives up to 35 kV; a dashed box shows the EV traction battery, contactors with pre-charge, inverter and DC-DC converter.')

spec = make_spec(FIG)
