"""Claude's hand-drawn figures for au-elec-u3 (Automotive Electrical and Electronics: microelectronics, sensors and actuators),
one per chapter, drawn from each chapter's own worked example and numbers. Plotted curves are computed from the examples
(MAP and TPS lines, the NTC beta curve, the wastegate force balance, the DC motor speed-torque line). Colours are the shell's
CSS variables."""
import os, sys, math, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

_T, _Tb, _boxt = T, Tb, boxt


def _sub(s):
    """V_out, R_DS ... drawn as real subscripts, never as underscores"""
    return re.sub(r'([A-Za-zα-ωΔΦ])_([A-Za-z0-9]+(?:\([a-z]+\))?)', r'\1<tspan baseline-shift="sub" font-size="11">\2</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)
def boxt(x, y, w, h, lines, *a, **k): return _boxt(x, y, w, h, [_sub(l) for l in lines], *a, **k)


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


def arrow(x1, y1, x2, y2, c=AC, w=2.5, a='n'):
    return L(x1, y1, x2, y2, c, w, arrow=a)


def resistor(x, y, h=50, label='', c=AC, side='end', lx=None):
    """vertical zig-zag resistor from (x, y) down to (x, y + h)"""
    pts = [(x, y), (x, y + 8)]
    n = 6; step = (h - 16) / n
    for i in range(n):
        pts.append((x + (9 if i % 2 == 0 else -9), y + 8 + step * (i + 0.5)))
    pts += [(x, y + h - 8), (x, y + h)]
    o = P(pts, c, 2.2)
    if label:
        o += T(lx if lx is not None else (x - 16 if side == 'end' else x + 16), y + h / 2 + 5, label, 14, side, INK, bold=True)
    return o


FIG = {}


# ---- 3.1 inside the ECU: inputs, microcontroller, drivers ----
def f1():
    o = []
    o.append(T(20, 26, 'sensors', 14, 'start', MUT, bold=True))
    ins = [('crank 60-2', 60), ('MAP', 120), ('coolant NTC', 180)]
    for lab, y in ins:
        o.append(boxt(20, y - 20, 120, 40, [lab], PANEL, L2, 14))
        o.append(arrow(140, y, 176, y, L2, 2, 'm'))
    o.append(boxt(180, 40, 80, 160, ['input', 'filter,', 'protect'], PANEL, AC, 13))
    o.append(arrow(260, 120, 284, 120, AC, 2.5))
    # microcontroller
    o.append(R(288, 36, 236, 248, ACS, AC, 10))
    o.append(T(406, 58, 'microcontroller (MCU)', 14, bold=True))
    cells = [('ADC 10/12-bit', 300, 72), ('capture timer', 412, 72), ('CPU 80 MHz', 300, 124),
             ('flash: program, maps', 300, 176), ('RAM · EEPROM', 300, 228)]
    for lab, x, y in cells:
        w = 212 if x == 300 and y >= 176 else 100
        o.append(boxt(x, y, w, 40, [lab], PANEL, AC, 13))
    o.append(boxt(412, 124, 100, 40, ['watchdog'], PANEL, NX, 13))
    o.append(arrow(524, 120, 548, 120, AC, 2.5))
    o.append(boxt(552, 60, 150, 120, ['PWM and compare', 'outputs →', 'MOSFET drivers'], LVS, LV, 13, bold_first=True))
    outs = [('injector', 230), ('ignition coil', 274), ('lamp 4.07 A', 318)]
    for lab, y in outs:
        o.append(boxt(574, y - 18, 128, 36, [lab], PANEL, LV, 13))
    o.append(L(627, 180, 627, 210, LV, 2, arrow='l'))
    o.append(boxt(288, 300, 236, 36, ['CAN · LIN to other ECUs'], PANEL, L2, 13))
    o.append(L(406, 284, 406, 300, L2, 2))
    o.append(T(20, 262, '6000 rpm: a crank tooth', 13, 'start', MUT))
    o.append(T(20, 280, 'every 166.7 µs', 13, 'start', MUT))
    o.append(T(20, 298, '= 13 333 clock cycles', 13, 'start', MUT, bold=True))
    o.append(T(360, 374, 'tooth routine 1500 cycles → 11 % of the CPU at 6000 rpm', 14, 'middle', INK, bold=True))
    return 392, ''.join(o)


FIG[1] = (f1, 'An engine ECU: sensor signals are filtered and protected, the microcontroller reads them with its ADC and capture timer, runs the program '
              'from flash, and fires the MOSFET drivers. At 6000 rpm a crank tooth arrives every 13 333 clock cycles.',
          'Block diagram. Crank, MAP and coolant sensors feed an input filter block, then a microcontroller containing ADC, capture timer, CPU at 80 megahertz, '
          'watchdog, flash, RAM and EEPROM. PWM outputs drive MOSFET drivers for an injector, an ignition coil and a 4.07 ampere lamp. A CAN and LIN block links other ECUs.')


# ---- 3.2 the coolant divider of the worked example and the signal chain ----
def f2():
    o = []
    chain = [('quantity', 'temperature'), ('element', 'NTC'), ('conditioning', 'divider, filter'), ('ADC', '10-bit, 5 V'), ('ECU', 'table → °C')]
    x = 16
    for i, (a, b) in enumerate(chain):
        o.append(boxt(x, 18, 124, 52, [a, b], ACS if i == 3 else PANEL, AC if i != 4 else NX, 13, bold_first=True))
        if i < 4: o.append(arrow(x + 124, 44, x + 142, 44, AC, 2))
        x += 142
    # divider circuit
    X = 150
    o.append(T(X, 112, '+5 V', 14, bold=True))
    o.append(L(X, 118, X, 132, AC, 2.2))
    o.append(resistor(X, 132, 60, 'R_f = 1 kΩ'))
    o.append(L(X, 192, X, 212, AC, 2.2))
    o.append(C(X, 212, 4.5, INK))
    o.append(L(X, 212, 290, 212, AC, 2.2, arrow='n'))
    o.append(boxt(294, 196, 76, 32, ['to ADC'], ACS, AC, 13))
    o.append(T(232, 204, 'V_out', 14, 'middle', INK, bold=True))
    o.append(resistor(X, 212, 60, 'NTC R_s'))
    o.append(L(X, 272, X, 292, AC, 2.2))
    o.append(L(X - 18, 292, X + 18, 292, INK, 2.5)); o.append(L(X - 11, 299, X + 11, 299, INK, 2)); o.append(L(X - 5, 306, X + 5, 306, INK, 2))
    o.append(T(X, 330, 'V_out = 5 × R_s ÷ (R_s + 1000)', 13, 'middle', MUT))
    # results table
    tx = 410
    o.append(R(tx, 104, 294, 150, PANEL, L2, 8))
    heads = ['', 'R_s', 'V_out', 'count']
    xs = [tx + 46, tx + 116, tx + 190, tx + 258]
    for h, xx in zip(heads, xs): o.append(T(xx, 130, h, 14, 'middle', MUT, bold=True))
    o.append(L(tx + 10, 140, tx + 284, 140, L2, 1.2))
    rows = [('25 °C', '2.0 kΩ', '3.333 V', '682'), ('80 °C', '0.5 kΩ', '1.667 V', '341')]
    for j, r in enumerate(rows):
        y = 168 + j * 34
        for v, xx in zip(r, xs): o.append(T(xx, y, v, 14, 'middle', INK, bold=(v == r[0])))
    o.append(T(tx + 147, 240, 'one count = 5 ÷ 1023 = 4.89 mV', 13, 'middle', MUT))
    o.append(T(tx + 147, 290, 'hotter → lower R_s → lower V_out', 14, 'middle', LV, bold=True))
    return 346, ''.join(o)


FIG[2] = (f2, 'The signal path, and the worked example\'s coolant divider: warming from 25 °C to 80 °C drops the output from 3.333 V (count 682) to 1.667 V (count 341).',
          'Five blocks: quantity, sensing element, conditioning, 10-bit ADC, ECU. Below, a divider: 1 kilo-ohm from 5 volts to the output node, NTC thermistor to ground, '
          'output to the ADC. A table gives 2 kilo-ohm, 3.333 volts, count 682 at 25 degrees and 0.5 kilo-ohm, 1.667 volts, count 341 at 80 degrees.')


# ---- 3.3 MAP transfer line and the speed-density chain ----
def f3():
    o = []
    x0, x1, y0, y1 = 70, 330, 40, 250
    fx, fy = lin(20, 100, x0, x1), lin(0, 5, y1, y0)
    o.append(axes(x0, x1, y0, y1, [20, 40, 60, 80, 100], [0, 1, 2, 3, 4, 5], fx, fy, 'manifold absolute pressure, kPa', 'MAP output, V'))
    o.append(P([(fx(p), fy(0.05 * p - 0.5)) for p in (20, 100)], AC, 3))
    o.append(L(fx(60), y1, fx(60), fy(2.5), LV, 1.8, dash='5 4')); o.append(L(x0, fy(2.5), fx(60), fy(2.5), LV, 1.8, dash='5 4'))
    o.append(C(fx(60), fy(2.5), 6, LV))
    o.append(Tb(fx(60) + 12, fy(2.5) + 22, '60 kPa → 2.5 V', 13, 'start', LV, bold=True))
    o.append(C(fx(20), fy(0.5), 5)); o.append(C(fx(100), fy(4.5), 5))
    o.append(Tb(fx(26), fy(0.5) - 12, '0.5 V', 13, 'start', AC)); o.append(Tb(fx(94), fy(4.5) + 22, '4.5 V', 13, 'end', AC))
    # speed-density chain
    bx = 380
    steps = [('MAP 60 kPa, IAT 300 K', PANEL, L2), ('ρ = 60 000 ÷ (287 × 300) = 0.697 kg/m³', PANEL, AC),
             ('per cycle: 0.697 × 1.6 L × 0.90 = 1.003 g', PANEL, AC), ('3000 rpm → 25 cycles/s', PANEL, L2), ('ṁ = 1.003 × 25 = 25.1 g/s', LVS, LV)]
    y = 30
    for i, (s, f, st) in enumerate(steps):
        o.append(boxt(bx, y, 326, 40, [s], f, st, 13, bold_first=(i == 4)))
        if i < 4: o.append(arrow(bx + 163, y + 40, bx + 163, y + 54, AC, 2))
        y += 56
    o.append(T(bx + 163, 322, 'speed-density estimate, 1.6 L engine', 13, 'middle', MUT))
    return 340, ''.join(o)


FIG[3] = (f3, 'Left: the MAP sensor\'s straight transfer line, 0.5 V at 20 kPa to 4.5 V at 100 kPa, so the worked example\'s 60 kPa reads 2.5 V. '
              'Right: the speed-density steps that turn 60 kPa and 300 K into 25.1 g/s of air for the 1.6 L engine at 3000 rpm.',
          'Graph of MAP output voltage against pressure: a straight line from 0.5 volts at 20 kilopascals to 4.5 volts at 100, with 60 kilopascals marked at 2.5 volts. '
          'Beside it, five boxes: 60 kilopascals and 300 kelvin, density 0.697, mass per cycle 1.003 grams, 25 cycles per second, mass flow 25.1 grams per second.')


# ---- 3.4 the 60-2 wheel and its pulse train at 3000 rpm ----
def f4():
    o = []
    cx, cy, r = 130, 160, 100
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r - 14}" style="fill:var(--panel);stroke:{AC};stroke-width:2"/>')
    for i in range(60):
        if i in (0, 1): continue
        a = math.radians(-90 + i * 6 + 1.5)
        a2 = math.radians(-90 + i * 6 + 4.5)
        p = [(cx + (r - 14) * math.cos(a), cy + (r - 14) * math.sin(a)), (cx + r * math.cos(a), cy + r * math.sin(a)),
             (cx + r * math.cos(a2), cy + r * math.sin(a2)), (cx + (r - 14) * math.cos(a2), cy + (r - 14) * math.sin(a2))]
        o.append(P(p, AC, 1.4, fill='var(--accent-soft)'))
    o.append(f'<circle cx="{cx}" cy="{cy}" r="14" style="fill:{PANEL};stroke:{AC};stroke-width:2"/>')
    o.append(T(cx, cy - 26, '60-2 wheel', 14, bold=True)); o.append(T(cx, cy + 40, '6° per pitch', 13, fill=MUT))
    # sensor at the top facing the gap
    o.append(R(cx - 12, cy - r - 46, 24, 30, NXS, NX, 4))
    o.append(T(cx + 20, cy - r - 30, 'sensor', 13, 'start', NX, bold=True))
    o.append(T(cx + 48, cy - r + 4, 'gap: 2 teeth missing', 13, 'start', LV, bold=True))
    o.append(L(cx + 46, cy - r, cx + 12, cy - r + 8, LV, 1.8, arrow='l'))
    # pulse train: last teeth, gap, teeth (scaled time)
    X0, Y = 280, 120
    sc = 0.17  # px per µs
    t = 0
    edges = []
    o.append(T(X0, 50, 'sensor output at 3000 rpm (time →)', 14, 'start', MUT, bold=True))
    seq = [333, 333, 333, 1000, 333, 333]
    xs = [X0]
    for d in seq: xs.append(xs[-1] + d * sc)
    pts = []
    for i in range(len(xs) - 1):
        a, b = xs[i], xs[i + 1]
        pts += [(a, Y + 40), (a, Y), (a + 28, Y), (a + 28, Y + 40), (b, Y + 40)]
    o.append(P(pts, AC, 2.2))
    for x in xs: o.append(L(x, Y + 46, x, Y + 56, L2, 1.5))
    o.append(brace(xs[0], xs[1], Y + 66)); o.append(T((xs[0] + xs[1]) / 2, Y + 92, 'T = 333 µs', 13, 'middle', INK, bold=True))
    o.append(brace(xs[3], xs[4], Y + 66, LV)); o.append(T((xs[3] + xs[4]) / 2, Y + 92, 'gap = 3T = 1.0 ms', 13, 'middle', LV, bold=True))
    o.append(T(xs[4] - 6, Y - 10, 'next tooth: counter reset', 13, 'end', NX))
    o.append(L(xs[4], Y - 4, xs[4], Y + 40, NX, 2, dash='4 3'))
    o.append(boxt(X0, 252, 420, 64, ['3000 rpm = 50 rev/s → 20 ms per turn', '20 ms ÷ 60 pitches = 0.333 ms; gap long by 3 times'], PANEL, L2, 13))
    return 330, ''.join(o)


FIG[4] = (f4, 'The worked example\'s 60-2 wheel: 58 teeth on a 6° pitch and a gap of two missing teeth. At 3000 rpm the sensor sees an edge every '
              '333 µs, and the gap gives one interval of 3T = 1.0 ms, which the ECU uses to reset its tooth counter.',
          'A toothed wheel with two teeth missing at the top, under a sensor. Beside it, a pulse train with three normal intervals of 333 microseconds, '
          'one long interval of 1.0 millisecond marked gap equals 3T, then more teeth; a dashed line marks the counter reset at the first tooth after the gap.')


# ---- 3.5 Hall plate of the worked example ----
def f5():
    o = []
    # plate drawn in perspective
    pts = [(80, 150), (330, 150), (380, 110), (130, 110)]
    o.append(P(pts + [pts[0]], AC, 2.2, fill='var(--accent-soft)'))
    o.append(P([(80, 150), (80, 166), (330, 166), (380, 126), (380, 110)], AC, 2.2))
    o.append(L(330, 150, 330, 166, AC, 2.2))
    o.append(T(392, 160, 't = 0.5 mm', 13, 'start', MUT))
    # current along the plate
    o.append(arrow(40, 138, 108, 138, LV, 3, 'l')); o.append(T(36, 128, 'I = 10 mA', 14, 'start', LV, bold=True))
    o.append(arrow(352, 136, 384, 136, LV, 3, 'l'))
    # field down through the plate
    for x in (170, 230, 290):
        o.append(L(x, 30, x, 100, NX, 2.2, arrow='x'))
    o.append(T(300, 40, 'B = 0.1 T', 14, 'start', NX, bold=True))
    # Hall voltage across the width
    o.append(C(150, 122, 4.5, INK)); o.append(C(308, 142, 4.5, INK))
    o.append(P([(150, 122), (150, 236), (206, 236)], INK, 1.6)); o.append(P([(308, 142), (308, 236), (254, 236)], INK, 1.6))
    o.append(f'<circle cx="230" cy="236" r="22" style="fill:var(--panel);stroke:{INK};stroke-width:2"/>')
    o.append(T(230, 241, 'V', 15, bold=True))
    o.append(T(230, 282, 'V_H = I B ÷ (n q t) = 1.25 mV', 14, 'middle', INK, bold=True))
    o.append(T(230, 302, 'n = 10²² m⁻³, so 1 ÷ (n q t) = 1.25 m²/C', 13, 'middle', MUT))
    # chain to the ECU
    bx = 476
    o.append(boxt(bx, 40, 230, 44, ['amplifier: 1.25 mV → volts'], PANEL, AC, 13))
    o.append(arrow(bx + 115, 84, bx + 115, 104, AC, 2))
    o.append(boxt(bx, 108, 230, 60, ['Schmitt trigger', 'operate and release points'], ACS, AC, 13, bold_first=True))
    o.append(arrow(bx + 115, 168, bx + 115, 188, AC, 2))
    o.append(boxt(bx, 192, 230, 44, ['clean edge to the ECU timer'], LVS, LV, 13))
    o.append(T(bx + 115, 270, 'works at zero speed', 13, 'middle', MUT))
    o.append(T(bx + 115, 288, '(needs a supply)', 13, 'middle', MUT))
    return 318, ''.join(o)


FIG[5] = (f5, 'The worked example\'s Hall plate: 10 mA flows along a 0.5 mm plate in a 0.1 T field and 1.25 mV appears across its width. '
              'An amplifier and a Schmitt trigger turn this into a clean edge that the ECU can time, even at zero speed.',
          'A thin plate with current of 10 milliamps flowing along it and a field of 0.1 tesla passing down through it. A voltmeter across the width reads the Hall voltage, '
          '1.25 millivolts. Beside it, a chain: amplifier, Schmitt trigger with operate and release points, clean edge to the ECU timer.')


# ---- 3.6 TPS line and NTC divider curve ----
def f6():
    o = []
    x0, x1, y0, y1 = 64, 316, 50, 250
    fx, fy = lin(0, 100, x0, x1), lin(0, 5, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0, 25, 50, 75, 100], [0, 1, 2, 3, 4, 5], fx, fy, 'throttle opening, %', 'TPS output, V'))
    o.append(P([(fx(0), fy(0.5)), (fx(100), fy(4.5))], AC, 3))
    o.append(L(fx(30), y1, fx(30), fy(1.7), LV, 1.8, dash='5 4')); o.append(L(x0, fy(1.7), fx(30), fy(1.7), LV, 1.8, dash='5 4'))
    o.append(C(fx(30), fy(1.7), 6, LV)); o.append(Tb(fx(30) + 12, fy(1.7) + 20, '30 % → 1.70 V, count 348', 13, 'start', LV, bold=True))
    # NTC curve
    X0, X1 = 420, 690
    gx, gy = lin(-20, 120, X0, X1), lin(0, 5, y1, y0)
    o.append(axes(X0, X1, y0, y1, [-20, 0, 40, 80, 120], [0, 1, 2, 3, 4, 5], gx, gy, 'coolant temperature, °C', 'divider output, V', xfmt=neg))
    def v(t):
        R = 2200 * math.exp(3500 * (1 / (t + 273.15) - 1 / 298.15)); return 5 * R / (R + 2200)
    o.append(P([(gx(t), gy(v(t))) for t in range(-20, 121, 4)], NX, 3))
    for t, lab, dx, dy, anc in ((-10, '−10 °C: 4.133 V', 14, -12, 'start'), (90, '90 °C: 0.545 V', -10, -12, 'end')):
        o.append(C(gx(t), gy(v(t)), 6, NX)); o.append(Tb(gx(t) + dx, gy(v(t)) + dy, lab, 13, anc, NX, bold=True))
    o.append(T(gx(50), gy(v(50)) - 50, 'curve, not a line', 13, 'middle', MUT))
    o.append(T(360, 318, 'TPS: straight line, two points define it. NTC (2.2 kΩ at 25 °C, B = 3500 K, 2.2 kΩ pull-up): needs a table.', 13, 'middle', MUT))
    return 334, ''.join(o)


FIG[6] = (f6, 'Left: the TPS line of the first worked example, 0.5 V closed to 4.5 V wide open, with 30 % at 1.70 V. Right: the coolant divider of the second example, computed from the '
              'thermistor equation: the voltage falls along a curve, from 4.133 V at −10 °C to 0.545 V at 90 °C, so the ECU needs a table.',
          'Two graphs. Left: throttle position sensor voltage rising in a straight line from 0.5 volts at 0 per cent to 4.5 volts at 100 per cent, with 30 per cent marked at 1.70 volts. '
          'Right: NTC divider output falling along a curve with temperature, 4.133 volts at minus 10 degrees and 0.545 volts at 90 degrees.')


# ---- 3.7 the zirconia cell and its two Nernst voltages ----
def f7():
    o = []
    # exhaust pipe band and thimble cell
    o.append(R(20, 168, 400, 120, NXS, L2, 6))
    o.append(T(36, 278, 'exhaust gas', 14, 'start', NX, bold=True))
    o.append(f'<path d="M150,60 L150,220 Q150,250 190,250 Q230,250 230,220 L230,60" style="fill:var(--panel);stroke:{AC};stroke-width:6"/>')
    o.append(f'<path d="M144,60 L144,222 Q144,258 190,258 Q236,258 236,222 L236,60" style="fill:none;stroke:{LV};stroke-width:2;stroke-dasharray:4 3"/>')
    o.append(T(190, 110, 'reference', 13, bold=True)); o.append(T(190, 128, 'air', 13, bold=True)); o.append(T(190, 146, '0.21 bar', 13, fill=MUT))
    o.append(T(260, 100, 'zirconia (ZrO₂)', 13, 'start', AC, bold=True)); o.append(T(260, 118, 'thimble, 800 °C', 13, 'start', MUT))
    o.append(T(260, 210, 'porous platinum', 13, 'start', LV)); o.append(T(260, 228, 'electrodes', 13, 'start', LV))
    o.append(L(256, 214, 238, 214, LV, 1.6))
    # voltmeter
    o.append(P([(190, 70), (190, 34), (374, 34)], INK, 1.6)); o.append(P([(236, 150), (396, 150), (396, 56)], INK, 1.6))
    o.append(f'<circle cx="396" cy="34" r="22" style="fill:var(--panel);stroke:{INK};stroke-width:2"/>'); o.append(T(396, 39, 'E', 15, bold=True))
    # two results
    bx = 450
    o.append(T(bx + 125, 34, 'E = (RT ÷ 4F) ln(pO₂ ref ÷ pO₂ exh)', 13, 'middle', INK, bold=True))
    o.append(T(bx + 125, 54, 'RT ÷ 4F = 0.02312 V at 1073 K', 13, 'middle', MUT))
    o.append(boxt(bx, 70, 250, 74, ['lean, λ > 1: 1 % O₂ (0.01 bar)', 'ln 21 = 3.045', 'E = 0.070 V: low'], PANEL, LV, 13, bold_first=True))
    o.append(boxt(bx, 158, 250, 74, ['rich, λ < 1: 10⁻²⁰ bar O₂', 'ln(2.1 × 10¹⁹) = 44.49', 'E = 1.03 V ideal (0.8–0.9 real)'], PANEL, NX, 13, bold_first=True))
    o.append(T(bx + 125, 262, 'the oxygen ratio jumps ~10¹⁸ at λ = 1,', 13, 'middle', MUT))
    o.append(T(bx + 125, 280, 'so the voltage switches there', 13, 'middle', MUT))
    return 300, ''.join(o)


FIG[7] = (f7, 'A thimble zirconia cell with reference air inside and exhaust outside. The second worked example\'s Nernst voltages: about 0.07 V when the exhaust is lean (1 % oxygen) '
              'and about 1.03 V ideal when it is rich, because the oxygen ratio jumps enormously at λ = 1.',
          'Cross-section of a zirconia thimble in the exhaust stream, reference air inside, platinum electrodes on both faces, and a voltmeter across them. '
          'Two boxes: lean, 1 per cent oxygen, 0.070 volts; rich, 10 to the minus 20 bar oxygen, 1.03 volts ideal, 0.8 to 0.9 real.')


# ---- 3.8 knock channel with the example's numbers and the crank window ----
def f8():
    o = []
    blocks = [('piezo sensor', '2 pC/N × 50 N', '= 100 pC'), ('charge amp', 'C_f = 1000 pF', '→ 0.10 V'), ('band-pass', '5–15 kHz', 'knock band'),
              ('rectify +', 'integrate', 'one value'), ('compare', 'in window', 'retard spark')]
    x = 12
    for i, (a, b, c) in enumerate(blocks):
        o.append(boxt(x, 30, 128, 80, [a, b, c], LVS if i == 4 else (ACS if i == 0 else PANEL), LV if i == 4 else AC, 13, bold_first=True))
        if i < 4: o.append(arrow(x + 128, 70, x + 142, 70, AC, 2))
        x += 142
    # crank-angle window strip
    x0, x1 = 60, 660
    fx = lin(-60, 120, x0, x1)
    Y = 244
    o.append(xaxis(x0, x1, Y, [-60, -30, 0, 30, 60, 90, 120], fx, 'crank angle, degrees after TDC', neg))
    o.append(R(fx(10), Y - 70, fx(60) - fx(10), 70, ACS, AC, 4))
    o.append(T((fx(10) + fx(60)) / 2, Y - 78, 'knock window 10°–60° ATDC', 13, 'middle', AC, bold=True))
    o.append(L(fx(-20), Y - 90, fx(-20), Y, NX, 2.5))
    o.append(T(fx(-20) - 6, Y - 76, 'spark', 13, 'end', NX, bold=True))
    # a burst of knock inside the window
    pts = []
    for i in range(0, 121):
        a = fx(14 + i * 0.35)
        amp = 34 * math.exp(-i / 50) * (1 if i > 4 else i / 4)
        pts.append((a, Y - 32 + amp * math.sin(i * 1.3)))
    o.append(P(pts, LV, 1.6))
    o.append(T(fx(90), Y - 40, 'valve noise outside', 13, 'middle', MUT)); o.append(T(fx(90), Y - 22, 'the window is ignored', 13, 'middle', MUT))
    return 310, ''.join(o)


FIG[8] = (f8, 'The knock channel of the worked example: 50 N on a 2 pC/N sensor gives 100 pC, which the 1000 pF charge amplifier turns into 0.10 V. The ECU judges '
              'only the 5–15 kHz band and only inside a crank-angle window after the spark.',
          'Five blocks: piezo sensor, 2 picocoulombs per newton times 50 newtons gives 100 picocoulombs; charge amplifier with 1000 picofarads gives 0.10 volts; band-pass 5 to 15 kilohertz; '
          'rectify and integrate; compare in window and retard spark. Below, a crank-angle axis with the spark before TDC and a knock window from 10 to 60 degrees after, holding a decaying burst.')


# ---- 3.9 low-side solenoid driver and peak-and-hold current ----
def f9():
    o = []
    X = 120
    o.append(T(X, 30, '+12 V', 14, bold=True)); o.append(L(X, 36, X, 54, AC, 2.2))
    # coil
    o.append(L(X, 54, X, 70, AC, 2.2))
    for i in range(4):
        o.append(f'<path d="M{X},{70 + i * 16} a10,8 0 0,1 0,16" style="fill:none;stroke:{AC};stroke-width:2.2"/>')
    o.append(L(X, 134, X, 160, AC, 2.2))
    o.append(T(X - 22, 106, 'coil 6 Ω', 14, 'end', INK, bold=True))
    # freewheel diode across coil
    o.append(P([(X, 60), (X + 60, 60), (X + 60, 84)], LV, 2)); o.append(P([(X, 150), (X + 60, 150), (X + 60, 120)], LV, 2))
    o.append(f'<path d="M{X + 48},120 L{X + 72},120 L{X + 60},100 Z" style="fill:var(--live-soft);stroke:{LV};stroke-width:2"/>')
    o.append(L(X + 48, 100, X + 72, 100, LV, 2.5)); o.append(L(X + 60, 84, X + 60, 100, LV, 2))
    o.append(T(X + 80, 108, 'freewheeling', 13, 'start', LV, bold=True)); o.append(T(X + 80, 124, 'diode', 13, 'start', LV, bold=True))
    # MOSFET
    o.append(L(X, 160, X, 178, AC, 2.2)); o.append(L(X - 12, 178, X - 12, 214, INK, 3)); o.append(L(X, 178, X, 214, INK, 2.5))
    o.append(L(X - 22, 196, X - 46, 196, INK, 2)); o.append(L(X - 22, 182, X - 22, 210, INK, 2.5))
    o.append(L(X, 214, X, 240, AC, 2.2))
    o.append(L(X - 16, 240, X + 16, 240, INK, 2.5)); o.append(L(X - 9, 247, X + 9, 247, INK, 2))
    o.append(T(X + 14, 202, 'MOSFET', 13, 'start', INK, bold=True))
    o.append(boxt(14, 260, 116, 44, ['ECU PWM'], ACS, AC, 13, bold_first=True))
    o.append(P([(72, 260), (72, 196), (X - 46, 196)], AC, 2))
    # current waveform
    x0, x1, y0, y1 = 330, 690, 60, 250
    fx, fy = lin(0, 10, x0, x1), lin(0, 2.4, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0, 2, 4, 6, 8, 10], [0, 0.5, 1.0, 1.5, 2.0], fx, fy, 'time, ms', 'coil current, A', yfmt=lambda v: f'{v:.1f}'))
    pts = [(fx(0), fy(0))]
    for i in range(1, 31):
        t = i * 0.05; pts.append((fx(t), fy(2.0 * (1 - math.exp(-t / 0.4)))))
    pts += [(fx(1.5), fy(1.95)), (fx(2.3), fy(0.2))]
    t = 2.3
    while t < 9.8:
        pts += [(fx(t + 0.2), fy(0.24)), (fx(t + 0.4), fy(0.18))]; t += 0.4
    o.append(P(pts, AC, 2.4))
    o.append(Tb(fx(1.6), fy(2.0) - 10, 'pull-in 2 A full on', 13, 'start', AC, bold=True))
    o.append(Tb(fx(6), fy(0.2) - 24, 'hold 0.2 A: 10 % PWM', 13, 'middle', LV, bold=True))
    o.append(T(510, 320, '1 mm gap: 15.7 N at 1 A; seated (0.2 mm): 15.7 N at only 0.2 A', 13, 'middle', MUT))
    return 336, ''.join(o)


FIG[9] = (f9, 'Left: a low-side MOSFET drives the 6 Ω coil from 12 V, with the freewheeling diode across the coil. Right: peak-and-hold drive from the worked example: '
              '2 A full on to pull the plunger in, then 10 % PWM for a 0.2 A hold, which gives the same pull once the gap has closed.',
          'Circuit: 12 volts, a 6 ohm coil with a diode across it, a MOSFET to ground switched by the ECU PWM output. Graph of coil current against time: '
          'a rise to 2 amps for pull-in, then a drop to a rippling 0.2 amp hold level.')


# ---- 3.10 wastegate actuator and its force balance ----
def f10():
    o = []
    # can and diaphragm
    o.append(R(40, 60, 200, 150, PANEL, AC, 10))
    o.append(P([(40, 126), (80, 134), (200, 134), (240, 126)], NX, 3))
    o.append(T(140, 92, 'boost side', 13, 'middle', NX, bold=True)); o.append(T(140, 118, 'diaphragm Ø 60 mm', 13, 'middle', AC, bold=True))
    # spring below
    pts = [(140, 138)]
    for i in range(8): pts.append((140 + (14 if i % 2 == 0 else -14), 146 + i * 7))
    pts.append((140, 204)); o.append(P(pts, MUT, 2))
    o.append(T(250, 196, 'spring: 90 N preload,', 13, 'start', MUT)); o.append(T(250, 214, '15 N/mm', 13, 'start', MUT)); o.append(L(246, 192, 158, 172, MUT, 1.4))
    o.append(L(140, 210, 140, 290, AC, 4))
    o.append(P([(140, 290), (210, 290), (226, 270)], AC, 4)); o.append(T(232, 296, 'to wastegate flap', 13, 'start', AC, bold=True))
    # boost line and PWM valve
    o.append(P([(40, 90), (14, 90), (14, 30), (300, 30)], NX, 2.5))
    o.append(T(300, 22, 'boost from compressor', 13, 'end', NX))
    o.append(R(260, 72, 70, 40, NXS, NX, 4)); o.append(T(295, 97, 'PWM', 13, bold=True))
    o.append(L(240, 92, 260, 92, NX, 2.5)); o.append(L(295, 112, 295, 140, NX, 2, arrow='x')); o.append(T(295, 158, 'vent', 13, fill=NX))
    o.append(T(295, 64, 'ECU valve', 13, fill=MUT))
    # force balance plot
    x0, x1, y0, y1 = 400, 690, 50, 260
    fx, fy = lin(0, 90, x0, x1), lin(0, 9, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0, 30, 60, 90], [0, 2, 4, 6, 8], fx, fy, 'boost on the diaphragm, kPa', 'rod travel, mm'))
    A = math.pi * 0.06 ** 2 / 4
    po = 90 / A / 1000; pf = 210 / A / 1000
    o.append(P([(fx(0), fy(0)), (fx(po), fy(0)), (fx(pf), fy(8)), (fx(90), fy(8))], AC, 3))
    for p, lab, dx, anc in ((po, '31.8 kPa: opens', 8, 'start'), (60, '60 kPa: 5.31 mm', 12, 'start'), (pf, '74.3 kPa: full 8 mm', -8, 'end')):
        x = max(0, (p * 1000 * A - 90) / 15); x = min(x, 8)
        o.append(C(fx(p), fy(x), 6, LV))
        o.append(Tb(fx(p) + (-8 if p == po else dx), fy(x) + (18 if p == 60 else -12), lab, 13, 'end' if p == po else anc, LV, bold=True))
    o.append(T(545, 322, 'travel = (Δp × A − 90 N) ÷ 15 N/mm, A = 2.827 × 10⁻³ m²', 13, 'middle', MUT))
    return 336, ''.join(o)


FIG[10] = (f10, 'A wastegate actuator: boost on a 60 mm diaphragm against a 90 N spring, trimmed by a PWM vent valve. It opens at 31.8 kPa, is 5.31 mm open at 60 kPa and fully open at 74.3 kPa.',
           'Left: a can split by a diaphragm, boost above it, a spring below, a rod down to the wastegate flap, and a PWM vent valve on the boost line. '
           'Right: graph of rod travel against boost: zero up to 31.8 kilopascals, then a straight rise through 5.31 millimetres at 60 kilopascals to 8 millimetres at 74.3.')


# ---- 3.11 DC motor line and duty types ----
def f11():
    o = []
    x0, x1, y0, y1 = 70, 340, 50, 250
    fx, fy = lin(0, 1.2, x0, x1), lin(0, 600, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.3, 0.6, 0.9, 1.2], [0, 200, 400, 600], fx, fy, 'torque, N·m', 'speed, rad/s', xfmt=lambda v: f'{v:g}'))
    o.append(P([(fx(0), fy(600)), (fx(1.2), fy(0))], AC, 3))
    o.append(C(fx(0.2), fy(500), 6, LV)); o.append(Tb(fx(0.2) + 12, fy(500) - 10, '10 A: 0.20 N·m, 500 rad/s, 100 W', 13, 'start', LV, bold=True))
    o.append(Tb(fx(0.9), fy(60), 'stall 60 A, 1.20 N·m', 13, 'end', AC))
    # duty bars
    bx, bw = 400, 290
    o.append(T(bx, 40, 'duty types (load against time)', 14, 'start', MUT, bold=True))
    rows = [('S1', [(0, 1)], 'continuous: fan, fuel pump'), ('S2', [(0, 0.3)], 'short-time, then rest until cold'),
            ('S3 25 %', [(i * 0.25, i * 0.25 + 0.0625) for i in range(4)], '4 s on, 12 s off: window lift')]
    for j, (lab, segs, note) in enumerate(rows):
        y = 70 + j * 66
        o.append(T(bx, y + 22, lab, 14, 'start', INK, bold=True))
        o.append(L(bx + 70, y + 30, bx + bw, y + 30, L2, 1.5))
        for a, b in segs:
            o.append(R(bx + 70 + a * (bw - 70), y + 6, (b - a) * (bw - 70), 24, ACS, AC, 2))
        o.append(T(bx + 70, y + 50, note, 13, 'start', MUT))
    o.append(T(bx + 70, 292, 'CDF = 4 ÷ (4 + 12) = 25 %', 14, 'start', LV, bold=True))
    o.append(T(205, 312, 'no load 600 rad/s (5730 rpm); T = 0.02 I', 13, 'middle', MUT))
    return 320, ''.join(o)


FIG[11] = (f11, 'The worked examples: the blower motor\'s straight speed-torque line (10 A gives 0.20 N·m at 500 rad/s), and three duty types; 4 s on, 12 s off is S3 25 %.',
           'Graph of motor speed against torque: a straight line from 600 radians per second at zero torque to zero at 1.2 newton metres, with the 10 ampere point at 0.2 newton metres and 500 radians per second. '
           'Beside it, load bars: S1 continuous, S2 one short block, S3 four short blocks each a quarter of the cycle.')


# ---- 3.12 shunt current sensing and the coulomb count ----
def f12():
    o = []
    o.append(boxt(20, 60, 110, 70, ['battery', '50 Ah'], PANEL, AC, 14, bold_first=True))
    o.append(L(130, 80, 330, 80, AC, 3)); o.append(T(230, 70, 'to the loads, 10 A', 13, 'middle', MUT))
    o.append(L(130, 112, 170, 112, AC, 3))
    o.append(R(170, 100, 90, 24, ACS, AC, 3)); o.append(T(215, 117, 'shunt', 13, bold=True))
    o.append(L(260, 112, 330, 112, AC, 3)); o.append(T(330, 128, 'return', 13, 'end', MUT))
    o.append(L(180, 124, 180, 160, LV, 2)); o.append(L(250, 124, 250, 160, LV, 2))
    o.append(T(258, 152, 'Kelvin sense', 13, 'start', LV))
    o.append(boxt(160, 164, 110, 44, ['amplifier'], PANEL, LV, 13))
    o.append(arrow(270, 186, 296, 186, LV, 2, 'l'))
    o.append(boxt(300, 164, 70, 44, ['ADC'], PANEL, LV, 13))
    o.append(arrow(370, 186, 396, 186, LV, 2, 'l'))
    o.append(boxt(400, 164, 90, 44, ['BMS'], LVS, LV, 13, bold_first=True))
    o.append(T(215, 238, '0.1 mΩ × 100 A = 10 mV', 13, 'middle', MUT))
    # SOC bars
    bx = 520
    o.append(T(bx + 90, 40, 'coulomb count', 14, 'middle', INK, bold=True))
    for j, (lab, f) in enumerate((('start 80 %', 0.8), ('after 30 min 70 %', 0.7))):
        x = bx + j * 100
        o.append(R(x + 10, 60, 60, 180, PANEL, L2, 6))
        o.append(R(x + 10, 60 + 180 * (1 - f), 60, 180 * f, LVS, LV, 6))
        o.append(T(x + 40, 262, lab.split(' ')[0] if j == 0 else 'after', 13, 'middle', MUT))
        o.append(T(x + 40, 280, '80 %' if j == 0 else '70 %', 14, 'middle', INK, bold=True))
    o.append(T(bx + 90, 306, '10 A × 0.5 h = 5 Ah = 10 % of 50 Ah', 13, 'middle', LV, bold=True))
    o.append(T(20, 290, 'SOC(t) = SOC(0) − (1 ÷ C_n) ∫ I dt', 14, 'start', INK, bold=True))
    return 320, ''.join(o)


FIG[12] = (f12, 'Left: the pack current flows through a 0.1 mΩ shunt; Kelvin sense leads take its millivolt signal to an amplifier, the ADC and the BMS. Right: the worked example\'s '
                'coulomb count: 10 A for 30 min removes 5 Ah, so a 50 Ah battery falls from 80 % to 70 % state of charge.',
           'Circuit: a 50 ampere-hour battery, current to the loads, a shunt in the return with two sense leads to an amplifier, ADC and BMS. '
           'Beside it, two charge bars: 80 per cent at the start and 70 per cent after 30 minutes at 10 amperes.')


spec = make_spec(FIG)
