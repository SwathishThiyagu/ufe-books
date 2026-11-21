"""Claude's hand-drawn figures for au-elec-u4 (Automotive Electrical and Electronics: electronic engine control), one per
chapter, drawn from each chapter's own worked example and numbers. Colours are the shell's CSS variables."""
import os, sys, math, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

_T, _Tb, _boxt = T, Tb, boxt


def _sub(s):
    """m_air, eta_v ... drawn as real subscripts, never as underscores"""
    return re.sub(r'([A-Za-zα-ωṁη])_([A-Za-z0-9,]+)', r'\1<tspan baseline-shift="sub" font-size="11">\2</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)
def boxt(x, y, w, h, lines, *a, **k): return _boxt(x, y, w, h, [_sub(l) for l in lines], *a, **k)


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


def fmt(v):
    return neg(f'{v:g}')


# ---- 4.1 the worked example's car as a percentage of each limit ----
def f1():
    o = []
    x0, x1 = 200, 680
    fx = lin(0, 200, x0, x1)
    lab = []
    rows = [('CO, BS IV and VI', 82.0, '0.82 of 1.0 g/km', LV, LVS),
            ('HC, BS IV and VI', 70.0, '0.07 of 0.10 g/km', LV, LVS),
            ('NOx, BS IV', 137.5, '0.11 of 0.08 g/km', NX, NXS),
            ('NOx, BS VI', 183.3, '0.11 of 0.06 g/km', NX, NXS)]
    y = 40
    for name, v, note, c, cs in rows:
        o.append(T(x0 - 10, y + 15, name, 14, 'end', bold=True))
        o.append(T(x0 - 10, y + 31, note, 13, 'end', fill=MUT))
        o.append(R(x0, y, fx(v) - x0, 34, cs, c, 3))
        lab.append(T(fx(v) - 8, y + 22, f'{v:g} %', 14, 'end', fill=c, bold=True))
        y += 54
    yb = y + 4
    o.append(xaxis(x0, x1, yb, [0, 50, 100, 150, 200], fx, 'measured value as a percentage of the limit', lambda v: f'{v} %'))
    o.append(L(fx(100), 28, fx(100), yb, AC, 2.5, dash='7 5'))
    o.append(Tb(fx(100), 24, 'limit = 100 %', 13, fill=AC, bold=True))
    o += lab
    o.append(T(360, yb + 70, 'One bar past the line fails the car: it fails BS IV and BS VI on NOx.', 14, bold=True))
    return yb + 86, ''.join(o)


# ---- 4.2 pollutants against lambda (a sketch of the trend), with the worked example's rich point ----
def f2():
    o = []
    x0, x1, y0, y1 = 70, 690, 40, 300
    fx = lin(0.80, 1.20, x0, x1)
    fy = lin(0, 1.0, y1, y0)
    o.append(L(x0, y1, x1, y1, L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    for v in (0.8, 0.9, 1.0, 1.1, 1.2):
        X = fx(v); o += [L(X, y1, X, y1 + 5, L2, 1.5), T(X, y1 + 20, f'{v:.1f}', 13, fill=MUT)]
    o.append(T((x0 + x1) / 2, y1 + 42, 'λ  (rich ← 1 → lean)', 14, fill=MUT))
    o.append(T(x0 + 6, y0 - 14, 'amount in raw exhaust (trend sketch, not to scale)', 14, 'start', MUT))
    # catalyst window 0.99 to 1.01
    o.append(f'<rect x="{fx(0.99):.1f}" y="{y0:.1f}" width="{fx(1.01) - fx(0.99):.1f}" height="{y1 - y0:.1f}" style="fill:var(--accent-soft);stroke:none"/>')
    o.append(L(fx(1.0), y0, fx(1.0), y1, AC, 1.5, dash='5 4'))
    lam = [0.80 + i * 0.005 for i in range(81)]
    co = lambda l: 0.06 + 0.86 / (1 + math.exp((l - 0.93) / 0.025))
    hc = lambda l: 0.2 + 0.45 / (1 + math.exp((l - 0.92) / 0.04)) + 0.5 / (1 + math.exp(-(l - 1.17) / 0.012))
    nox = lambda l: 0.05 + 0.80 * math.exp(-((l - 1.06) / 0.075) ** 2)
    o.append(P([(fx(l), fy(co(l))) for l in lam], NX, 2.5))
    o.append(P([(fx(l), fy(min(hc(l), 0.98))) for l in lam], MUT, 2.5, dash='7 4'))
    o.append(P([(fx(l), fy(nox(l))) for l in lam], LV, 2.5))
    o.append(Tb(fx(0.835), fy(0.80), 'CO', 14, fill=NX, bold=True))
    o.append(Tb(fx(0.835), fy(hc(0.835)) - 14, 'HC', 14, fill=MUT, bold=True))
    o.append(Tb(fx(1.115), fy(0.80), 'NOx: peak near λ 1.06', 14, 'start', fill=LV, bold=True))
    o.append(Tb(fx(1.155), fy(0.50), 'HC rises again:', 13, fill=MUT))
    o.append(Tb(fx(1.155), fy(0.43), 'lean misfire', 13, fill=MUT))
    o.append(T(fx(1.0), fy(0.95), 'three-way', 13, fill=AC, bold=True))
    o.append(T(fx(1.0), fy(0.89), 'window', 13, fill=AC, bold=True))
    # worked example: AFR 13.2 -> lambda 0.90
    o.append(L(fx(0.898), y1, fx(0.898), fy(co(0.898)), AC, 1.5, dash='3 3'))
    o.append(C(fx(0.898), fy(co(0.898)), 6, AC))
    o.append(T(fx(0.898) - 8, fy(0.30), '13.2 : 1 → λ = 0.90', 13, 'end', fill=AC, bold=True))
    o.append(T(fx(0.898) - 8, fy(0.23), 'CO high, NOx low', 13, 'end', fill=AC))
    return y1 + 56, ''.join(o)


# ---- 4.3 torque and power against speed, with the worked example's point ----
SPEEDS = [1000, 2000, 3000, 4000, 5000, 6000]
TORQUE = [110, 138, 150, 145, 130, 110]


def f3():
    o = []
    x0, x1, y0, y1 = 80, 640, 50, 300
    fx = lin(1000, 6000, x0, x1)
    fT = lin(0, 160, y1, y0)
    fP = lin(0, 80, y1, y0)
    o.append(axes(x0, x1, y0, y1, SPEEDS, [0, 40, 80, 120, 160], fx, fT, 'engine speed (rpm)', 'torque (N·m)', fmt, fmt))
    o.append(L(x1, y0, x1, y1, L2, 1.5))
    for v in (0, 20, 40, 60, 80):
        Y = fP(v); o += [L(x1, Y, x1 + 5, Y, L2, 1.5), T(x1 + 9, Y + 4.5, f'{v}', 13, 'start', MUT)]
    o.append(T(x1 + 2, y0 - 12, 'power (kW)', 14, 'end', LV))
    pw = [2 * math.pi * n * t / 60 / 1000 for n, t in zip(SPEEDS, TORQUE)]
    o.append(P([(fx(n), fT(t)) for n, t in zip(SPEEDS, TORQUE)], AC, 2.5))
    o.append(P([(fx(n), fP(p)) for n, p in zip(SPEEDS, pw)], LV, 2.5, dash='8 4'))
    for n, t, p in zip(SPEEDS, TORQUE, pw):
        o.append(C(fx(n), fT(t), 4.5, AC)); o.append(C(fx(n), fP(p), 4.5, LV))
    o.append(Tb(fx(2000), fT(138) - 16, 'torque', 14, fill=AC, bold=True))
    o.append(Tb(fx(4300), fP(50), 'power = 2πNT ÷ 60', 14, fill=LV, bold=True))
    o.append(Tb(fx(6000) - 4, fP(69.1) - 14, '69.1 kW', 13, 'end', fill=LV))
    o.append(C(fx(3000), fT(150), 7, NX)); o.append(C(fx(3000), fP(pw[2]), 7, NX))
    o.append(Tb(fx(3000), fT(150) - 14, 'peak 150 N·m at 3000 rpm', 13, fill=NX, bold=True))
    o.append(Tb(fx(3000) + 12, fP(pw[2]) + 4, 'worked example: 47.12 kW', 13, 'start', fill=NX, bold=True))
    return y1 + 56, ''.join(o)


# ---- 4.4 block diagram of an engine management system ----
def f4():
    o = []
    sens = ['Crank position', 'Camshaft position', 'Manifold pressure', 'Intake air temp.', 'Throttle position',
            'Coolant temp.', 'Knock sensor']
    acts = ['Injectors', 'Ignition coils', 'Idle air valve', 'EGR valve', 'Purge valve', 'Fuel pump relay']
    o.append(T(80, 24, 'Sensors', 14, bold=True, fill=MUT)); o.append(T(640, 24, 'Actuators', 14, bold=True, fill=MUT))
    for i, s in enumerate(sens):
        y = 36 + i * 40
        o.append(boxt(10, y, 140, 30, [s], PANEL, L2, 13))
        o.append(L(150, y + 15, 196, y + 15, L2, 1.5, arrow='m'))
    yo = 36 + 7 * 40
    o.append(boxt(10, yo, 140, 30, ['Oxygen (λ) sensor'], LVS, LV, 13))
    o.append(L(150, yo + 15, 196, yo + 15, LV, 2, arrow='l'))
    for i, s in enumerate(acts):
        y = 56 + i * 44
        o.append(boxt(570, y, 140, 32, [s], PANEL, L2, 13))
        o.append(L(524, y + 16, 566, y + 16, L2, 1.5, arrow='m'))
    o.append(R(200, 36, 320, 310, ACS, AC, 10))
    o.append(T(360, 60, 'Engine ECU', 15, bold=True))
    blocks = [('Signal conditioning', 'scale, filter, protect'), ('ADC and timer inputs', '10-bit: 4.9 mV a count'),
              ('Processor + flash, RAM, EEPROM', 'maps: 2000 rpm, 46 kPa → 5.2 ms'), ('Driver stages', 'low-side switches')]
    for i, (a, b) in enumerate(blocks):
        y = 74 + i * 66
        o.append(boxt(220, y, 280, 50, [a, b], PANEL, AC, 13, True))
        if i: o.append(L(360, y - 16, 360, y - 2, AC, 2, arrow='n'))
    # exhaust feedback
    o.append(T(648, 330, 'exhaust', 13, 'start', fill=LV))
    o.append(P([(640, 316), (640, 372), (80, 372), (80, yo + 34)], LV, 2))
    o.append(f'<line x1="80" y1="{yo + 40:.1f}" x2="80" y2="{yo + 34:.1f}" style="stroke:var(--live);stroke-width:2" marker-end="url(#ar-UID-l)"/>')
    o.append(T(100, 392, 'exhaust gas → oxygen sensor:', 13, 'start', fill=LV, bold=True))
    o.append(T(100, 410, 'the fuel loop closes', 13, 'start', fill=LV, bold=True))
    # CAN
    o.append(boxt(400, 392, 240, 34, ['CAN bus → gearbox, ABS, body ECUs'], NXS, NX, 13))
    o.append(L(470, 346, 470, 388, NX, 2, arrow='x'))
    return 440, ''.join(o)


# ---- 4.5 the speed-density fuel calculation of the worked example, with the trim loop ----
def f5():
    o = []
    steps = [('Manifold sensors', 'MAP 100 kPa, 27 °C → ρ = 1.16 kg/m³'),
             ('Air mass flow', 'ṁ_air = 0.85 × 1.16 × 0.040 = 39.44 g/s'),
             ('Fuel flow', '39.44 ÷ 14.7 = 2.683 g/s'),
             ('Fuel per injection', '2.683 ÷ 100 per s = 26.83 mg'),
             ('Flow time', '26.83 mg ÷ 3.0 g/s = 8.94 ms'),
             ('Commanded pulse', '8.94 + 0.9 dead time = 9.84 ms')]
    for i, (a, b) in enumerate(steps):
        y = 14 + i * 62
        hi = i == 5
        o.append(boxt(40, y, 400, 46, [a, b], LVS if hi else PANEL, LV if hi else AC, 14, True))
        if i: o.append(L(240, y - 14, 240, y - 2, AC, 2, arrow='n'))
    # injector, engine, sensor, trim on the right
    yP = 14 + 5 * 62
    o.append(L(440, yP + 23, 486, yP + 23, LV, 2, arrow='l'))
    o.append(boxt(490, yP, 200, 46, ['Injector sprays', '24.6 % of each cycle'], PANEL, AC, 14, True))
    o.append(L(590, yP - 2, 590, 242, AC, 2, arrow='n'))
    o.append(boxt(490, 192, 200, 46, ['Engine burns', 'exhaust gas'], PANEL, AC, 14, True))
    o.append(L(590, 190, 590, 134, AC, 2, arrow='n'))
    o.append(boxt(490, 84, 200, 46, ['Oxygen sensor', 'rich 0.8 V / lean 0.1 V'], NXS, NX, 14, True))
    o.append(P([(590, 82), (590, 50), (468, 50), (468, yP + 10), (444, yP + 10)], NX, 2))
    o.append(f'<line x1="452" y1="{yP + 10:.1f}" x2="444" y2="{yP + 10:.1f}" style="stroke:var(--next);stroke-width:2" marker-end="url(#ar-UID-x)"/>')
    o.append(Tb(540, 44, 'trim ± %', 14, fill=NX, bold=True))
    return 14 + 6 * 62 + 4, ''.join(o)


# ---- 4.6 the crank-angle timeline of the worked example at 3000 and 6000 rpm ----
def f6():
    o = []
    x0, x1 = 60, 690
    fx = lin(-220, 30, x0, x1)      # crank angle: negative = before TDC
    rows = [('3000 rpm', 70, 18.0), ('6000 rpm', 190, 36.0)]
    for name, y, dpm in rows:
        o.append(T(x0, y - 30, f'{name}: {dpm:g}° per ms', 14, 'start', bold=True))
        o.append(L(x0, y + 28, x1, y + 28, L2, 1.5))
        start = -(25 + 3.0 * dpm)
        o.append(R(fx(start), y, fx(-25) - fx(start), 26, ACS, AC, 3))
        o.append(T((fx(start) + fx(-25)) / 2, y + 18, f'dwell 3.0 ms = {3.0 * dpm:g}°', 13, bold=True))
        o.append(T(fx(start), y + 46, f'{-start:g}° BTDC', 13, fill=AC))
        if name.startswith('6000'):
            prev = -205; end = prev + 1.5 * dpm
            o.append(R(fx(prev), y, fx(end) - fx(prev), 26, NXS, NX, 3))
            o.append(T((fx(prev) + fx(end)) / 2, y + 18, 'spark 1.5 ms', 13, fill=NX, bold=True))
            o.append(R(fx(end), y + 4, fx(start) - fx(end), 18, FIGBG, L2, 2, dash='3 3'))
            o.append(T((fx(end) + fx(start)) / 2, y - 6, '0.5 ms spare', 13, fill=MUT))
            o.append(T(fx(prev), y + 46, 'previous spark', 13, 'start', fill=NX))
    for y in (70, 190):
        o.append(L(fx(-25), y - 12, fx(-25), y + 32, NX, 2.5))
        o.append(T(fx(-25), y + 46, '25° BTDC', 13, fill=NX, bold=True))
        o.append(L(fx(0), y - 12, fx(0), y + 32, INK, 1.5, dash='4 3'))
        o.append(T(fx(0) + 4, y - 16, 'TDC', 13, 'start', fill=MUT))
        o.append(C(fx(12), y + 13, 6, LV))
        o.append(T(fx(12) + 2, y + 46, 'peak', 13, fill=LV))
    o.append(xaxis(x0, x1, 270, [-200, -150, -100, -50, 0], fx, 'crank angle (degrees, negative = before TDC)', fmt))
    o.append(T(360, 344, 'Same dwell time, double the angle: at 6000 rpm charging starts at 133° BTDC.', 14, bold=True))
    o.append(T(360, 366, 'Sparks of one coil are 180° (5.0 ms) apart, so dwell + spark must fit inside 5.0 ms.', 13, fill=MUT))
    return 382, ''.join(o)


FIG = {
    1: (f1, 'The car of the worked example as a percentage of each BS IV and BS VI limit. CO and HC are under the limit line, but NOx is over it for both stages, so the car fails both.',
        'Bar chart: CO 82 per cent and HC 70 per cent of their limits; NOx 137.5 per cent of the BS IV limit and 183.3 per cent of the BS VI limit, with a dashed line at 100 per cent.'),
    2: (f2, 'How CO, HC and NOx in the raw exhaust change with λ (a trend sketch). The worked example\'s 13.2 : 1 mixture sits on the rich side at λ = 0.90; the three-way catalyst works only in the narrow shaded window at λ = 1.',
        'Curves against lambda from 0.8 to 1.2: CO high when rich and falling, HC lowest slightly lean and rising at both ends, NOx peaking near lambda 1.06, a narrow window at lambda 1, and the worked example point at lambda 0.90.'),
    3: (f3, 'Torque and power of the worked example\'s engine. Torque peaks at 150 N·m at 3000 rpm, where the power is 47.12 kW; power keeps rising to 69.1 kW at 6000 rpm because speed multiplies torque.',
        'Torque curve from 110 to 150 to 110 newton metres between 1000 and 6000 rpm, and the power curve rising from 11.5 to 69.1 kilowatts, with the 3000 rpm point marked.'),
    4: (f4, 'Block diagram of an engine management system. Sensor signals are conditioned and digitised, the processor runs the maps (the worked example\'s cell gives 5.2 ms), drivers switch the actuators, and the exhaust oxygen sensor closes the fuel loop.',
        'Eight sensors on the left feed an ECU made of signal conditioning, ADC, processor with memory and driver stages; six actuators on the right; a feedback path from exhaust to the oxygen sensor; a CAN bus to other ECUs.'),
    5: (f5, 'The speed-density calculation of the worked example, from manifold pressure to a 9.84 ms injector pulse. The oxygen sensor reads the result and the trim corrects the pulse on the next injections.',
        'A chain of six boxes from manifold pressure and temperature to air density, air mass flow, fuel flow, fuel per injection, flow time and the commanded pulse, then injector, engine and oxygen sensor with a trim arrow back to the pulse.'),
    6: (f6, 'The worked example on a crank-angle scale. The 3.0 ms dwell is 54 degrees at 3000 rpm and 108 degrees at 6000 rpm, both ending at the spark 25 degrees before TDC; the dot is the pressure peak just after TDC. At 6000 rpm the previous spark and the new dwell fit inside the 5.0 ms gap with 0.5 ms spare.',
        'Two timelines of crank angle: at 3000 rpm dwell from 79 to 25 degrees before TDC; at 6000 rpm the previous spark from 205 to 151 degrees, a 0.5 ms gap, then dwell from 133 to 25 degrees; spark, TDC and pressure peak marked.'),
}
spec = make_spec(FIG)
