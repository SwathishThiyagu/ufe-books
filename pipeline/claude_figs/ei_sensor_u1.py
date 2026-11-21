"""Claude's hand-drawn figures for ei-sensor-u1 (Sensors and Measurements: sensor characteristics and errors), one per
chapter, drawn from each chapter's own worked example and numbers. Colours are the shell's CSS variables only."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
AFTER = {1: 2, 2: 1, 3: 3, 4: 3, 5: 3, 6: 2}


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


def arrow(x1, y1, x2, y2, c=AC, w=2, k='n', dash=None):
    return L(x1, y1, x2, y2, c, w, dash, arrow=k)


def sub(s):
    return f'<tspan baseline-shift="sub" font-size="11">{s}</tspan>'


def res_h(x1, x2, y, c=INK, n=6, amp=8):
    """horizontal zigzag resistor between x1 and x2"""
    pts = [(x1, y)]
    a, b = x1 + 10, x2 - 10
    for i in range(n * 2):
        pts.append((a + (b - a) * (i + 0.5) / (n * 2), y + (amp if i % 2 == 0 else -amp)))
    pts += [(b, y), (x2, y)]
    return P(pts, c, 2)


def res_v(x, y1, y2, c=INK, n=6, amp=8):
    pts = [(x, y1)]
    a, b = y1 + 10, y2 - 10
    for i in range(n * 2):
        pts.append((x + (amp if i % 2 == 0 else -amp), a + (b - a) * (i + 0.5) / (n * 2)))
    pts += [(x, b), (x, y2)]
    return P(pts, c, 2)


# ---- 1.1 where the output energy comes from: worked examples 1 and 2 ----
def f1():
    o = []
    o.append(R(14, 14, 338, 330, PANEL, NX, 10))
    o.append(R(368, 14, 338, 330, PANEL, LV, 10))
    o.append(T(183, 40, 'Active: the sensor is the source', 15, 'middle', NX, True))
    o.append(T(537, 40, 'Passive: the supply is the source', 15, 'middle', LV, True))
    # active circuit: source e with Rs, into amplifier Rin
    cx, cy = 70, 150
    o.append(f'<circle cx="{cx}" cy="{cy}" r="24" style="fill:var(--fig);stroke:var(--next);stroke-width:2"/>')
    o.append(T(cx, cy - 4, '+', 15, 'middle', NX, True)); o.append(T(cx, cy + 15, '−', 15, 'middle', NX, True))
    o.append(T(cx + 30, cy + 40, 'e = 25 mV', 13, 'start', NX, True))
    o.append(L(cx, cy - 24, cx, 92, INK, 2)); o.append(L(cx, 92, 110, 92, INK, 2))
    o.append(res_h(110, 190, 92)); o.append(T(150, 76, 'R' + sub('s') + ' = 500 Ω', 13, 'middle', INK))
    o.append(L(190, 92, 250, 92, INK, 2)); o.append(L(cx, cy + 24, cx, 232, INK, 2)); o.append(L(cx, 232, 250, 232, INK, 2))
    o.append(boxt(250, 82, 84, 160, ['amplifier', 'input', 'R' + sub('in')], ACS, AC, 13, bold_first=True))
    o.append(T(206, 166, 'V' + sub('in'), 14, 'end', AC, True))
    o.append(arrow(214, 220, 214, 104, AC, 1.5))
    o.append(T(30, 272, 'R' + sub('in') + ' = 1 MΩ: V' + sub('in') + ' = 24.99 mV, loss 0.05 %', 13, 'start', INK, True))
    o.append(T(30, 296, 'R' + sub('in') + ' = 10 kΩ: V' + sub('in') + ' = 23.81 mV, loss 4.8 %', 13, 'start', LV, True))
    o.append(T(30, 324, 'thermocouple, piezo crystal, solar cell', 13, 'start', MUT))
    # passive circuit: 1 mA current source through a Pt100
    sx, sy = 430, 160
    o.append(f'<circle cx="{sx}" cy="{sy}" r="24" style="fill:var(--fig);stroke:var(--live);stroke-width:2"/>')
    o.append(arrow(sx, sy + 13, sx, sy - 13, LV, 2.5, 'l'))
    o.append(T(sx + 30, sy + 40, 'I = 1 mA', 13, 'start', LV, True))
    o.append(L(sx, sy - 24, sx, 92, INK, 2)); o.append(L(sx, 92, 600, 92, INK, 2))
    o.append(L(sx, sy + 24, sx, 232, INK, 2)); o.append(L(sx, 232, 600, 232, INK, 2))
    o.append(res_v(600, 92, 232, AC)); o.append(T(620, 150, 'Pt100', 13, 'start', AC, True)); o.append(T(620, 170, '100.0 Ω', 13, 'start', AC, True))
    o.append(T(530, 150, 'V = IR', 13, 'middle', INK)); o.append(T(530, 170, '= 100 mV', 13, 'middle', INK, True))
    o.append(T(384, 272, 'self-heating P = I²R', 13, 'start', INK, True))
    o.append(T(384, 296, '= (10⁻³)² × 100 = 0.10 mW', 13, 'start', LV, True))
    o.append(T(384, 324, 'RTD, strain gauge, LVDT, thermistor', 13, 'start', MUT))
    return 350, ''.join(o)


FIG[1] = (f1, 'Left: the active 25 mV, 500 Ω source of worked example 2 loses 0.05 % into 1 MΩ but 4.8 % into 10 kΩ. Right: the '
              'passive Pt100 of worked example 1 gives 100 mV only because the 1 mA supply drives it, and is heated by 0.10 mW.',
          'Two circuit panels. Left, active: a 25 millivolt source with a 500 ohm source resistance feeding an amplifier input; with 1 '
          'megohm the input is 24.99 millivolts, with 10 kilohms 23.81 millivolts. Right, passive: a 1 milliamp current source driving '
          'a Pt100 of 100 ohms, giving 100 millivolts and 0.10 milliwatts of self-heating.')


# ---- 1.2 the capacitive pressure sensor of the worked example: C = 0.22135/d (pF, d in mm) ----
def f2():
    o = []
    # left: the plates before and after
    o.append(T(160, 26, 'Air-gap capacitor, A = 25 mm²', 14, 'middle', INK, True))
    for i, (d, C_, lab) in enumerate([(0.10, 2.21, 'no pressure'), (0.09, 2.46, 'pressed')]):
        y0 = 62 + i * 140
        gap = d * 400
        o.append(R(40, y0, 160, 10, ACS, AC, 2))
        o.append(R(40, y0 + 10 + gap, 160, 10, NXS, NX, 2))
        o.append(L(214, y0 + 10, 214, y0 + 10 + gap, INK, 1.5)); o.append(L(208, y0 + 10, 220, y0 + 10, INK, 1.5)); o.append(L(208, y0 + 10 + gap, 220, y0 + 10 + gap, INK, 1.5))
        o.append(T(228, y0 + 16 + gap / 2, f'd = {d:.2f} mm', 13, 'start', INK, True))
        o.append(T(120, y0 + gap + 44, f'{lab}: C = {C_:.2f} pF', 13, 'middle', AC if i == 0 else LV, True))
        if i == 1:
            for x in (80, 120, 160): o.append(arrow(x, y0 - 22, x, y0 - 3, LV, 2, 'l'))
    o.append(T(20, 330, 'C = ε₀A/d; a 10 % smaller gap gives +11.1 %', 13, 'start', MUT))
    # right: C against d
    X0, X1, Y0, Y1 = 400, 690, 50, 280
    fx = lin(0.06, 0.14, X0, X1); fy = lin(1.5, 3.7, Y1, Y0)
    o.append(axes(X0, X1, Y0, Y1, [0.06, 0.08, 0.10, 0.12, 0.14], [1.5, 2.0, 2.5, 3.0, 3.5], fx, fy, 'gap d (mm)', 'C (pF)',
                  xfmt=lambda v: f'{v:.2f}', yfmt=lambda v: f'{v:.1f}'))
    o.append(P([(fx(d), fy(0.22135 / d)) for d in [0.063 + i * 0.077 / 60 for i in range(61)]], AC, 3))
    # tangent at 0.10: slope -22.135 pF/mm
    t = lambda d: 2.2135 - 22.135 * (d - 0.10)
    o.append(L(fx(0.075), fy(t(0.075)), fx(0.135), fy(t(0.135)), MUT, 1.5, '6 4'))
    o.append(C(fx(0.10), fy(2.2135), 5, AC)); o.append(C(fx(0.09), fy(2.4594), 5, LV))
    o.append(Tb(fx(0.10) + 8, fy(2.2135) + 20, '2.21 pF at 0.10', 13, 'start', AC, True))
    o.append(Tb(fx(0.09) - 8, fy(2.4594) - 12, '2.46 pF at 0.09', 13, 'end', LV, True))
    o.append(T(X1, fy(3.45), 'dashed: tangent at 0.10 mm,', 13, 'end', MUT)); o.append(T(X1, fy(3.45) + 18, 'slope 0.022 pF/µm', 13, 'end', MUT))
    return 350, ''.join(o)


FIG[2] = (f2, 'The worked example’s sensor: 25 mm² plates, 0.10 mm of air, 2.21 pF. Pressing the gap to 0.09 mm raises C to 2.46 pF. '
              'On the right, C = ε₀A/d is a curve, so the 0.022 pF/µm tangent at the start under-predicts the rise.',
          'Left: two parallel plates drawn twice, with a 0.10 millimetre gap giving 2.21 picofarads and, under pressure arrows, a 0.09 '
          'millimetre gap giving 2.46 picofarads. Right: a plot of capacitance against gap from 0.06 to 0.14 millimetres, a falling '
          'curve, with the two points marked and a dashed tangent of 0.022 picofarads per micrometre at 0.10 millimetres.')


# ---- 1.3 the traceability chain and the calibration deviations of the worked example ----
def f3():
    o = []
    rungs = [('SI units', 'fixed constants'), ('Primary', 'national institute'), ('Secondary', 'calibration lab'),
             ('Working', 'dead-weight tester'), ('Sensor', '0–200 kPa')]
    for i, (a, b) in enumerate(rungs):
        x = 14 + i * 142
        st = (ACS, AC) if i < 4 else (LVS, LV)
        o.append(boxt(x, 18, 124, 52, [a, b], st[0], st[1], 13, bold_first=True))
        if i < 4: o.append(arrow(x + 125, 44, x + 140, 44, AC, 2))
    o.append(T(360, 92, 'each rung is calibrated against the one above, typically 4 to 10 times more accurate', 13, 'middle', MUT))
    # deviation plot
    X0, X1, Y0, Y1 = 90, 520, 130, 360
    fx = lin(0, 200, X0, X1); fy = lin(-40, 40, Y1, Y0)
    o.append(axes(X0, X1, Y0, Y1, [0, 50, 100, 150, 200], [-40, -20, 0, 20, 40], fx, fy, 'pressure (kPa)', 'deviation from end-point line (mV)',
                  yfmt=neg))
    o.append(L(X0, fy(0), X1, fy(0), INK, 1.5))
    P_ = [0, 50, 100, 150, 200]; up = [0, -5, -30, 15, 0]; dn = [10, 15, 10, 35, 0]
    o.append(P([(fx(p), fy(v)) for p, v in zip(P_, up)], AC, 2.5))
    o.append(P([(fx(p), fy(v)) for p, v in zip(P_, dn)], LV, 2.5, '6 4'))
    for p, u, d in zip(P_, up, dn):
        o.append(C(fx(p), fy(u), 5, AC)); o.append(C(fx(p), fy(d), 5, LV))
    o.append(L(fx(100) + 12, fy(-30), fx(100) + 12, fy(10), INK, 1.5, arrow=None))
    o.append(Tb(fx(100) + 18, fy(-12), 'hysteresis 40 mV', 13, 'start', INK, True))
    o.append(Tb(fx(100), fy(-30) + 22, '−30 mV at 100 kPa', 13, 'middle', AC, True))
    # legend and results
    xs = 548
    o.append(C(xs + 6, 158, 5, AC)); o.append(T(xs + 18, 163, 'up-scale', 13, 'start', INK))
    o.append(C(xs + 6, 184, 5, LV)); o.append(T(xs + 18, 189, 'down-scale', 13, 'start', INK))
    o.append(T(xs, 226, 'S = 3.98 V/200 kPa', 13, 'start', INK, True))
    o.append(T(xs, 246, '= 19.9 mV/kPa', 13, 'start', INK, True))
    o.append(T(xs, 278, 'non-linearity', 13, 'start', AC, True)); o.append(T(xs, 298, '30/3980 = 0.75 %FS', 13, 'start', AC, True))
    o.append(T(xs, 330, 'hysteresis', 13, 'start', LV, True)); o.append(T(xs, 350, '40/3980 = 1.0 %FS', 13, 'start', LV, True))
    return 410, ''.join(o)


FIG[3] = (f3, 'Top: the chain that makes the dead-weight tester’s pressures traceable to the SI. Below: the worked example’s readings '
              'minus the end-point line. The up-scale curve sags 30 mV at 100 kPa (0.75 %FS); the down-scale curve sits 40 mV above '
              'it there (1.0 %FS hysteresis).',
          'Top: five boxes in a row, SI units fixed by constants, primary standard at the national institute, secondary standard at a '
          'calibration lab, working standard the dead-weight tester, and the 0 to 200 kilopascal sensor. Below: deviation from the '
          'end-point line in millivolts against pressure; up-scale points 0, minus 5, minus 30, plus 15, 0; down-scale points 10, 15, '
          '10, 35, 0; the 40 millivolt gap at 100 kilopascals is marked as hysteresis.')


# ---- 1.4 linearity and accuracy versus precision for the 0-250 kPa sensor ----
def f4():
    o = []
    X0, X1, Y0, Y1 = 70, 330, 60, 270
    fx = lin(0, 250, X0, X1); fy = lin(-0.2, 0.8, Y1, Y0)
    o.append(T(200, 24, 'Measured − ideal line', 14, 'middle', INK, True))
    o.append(axes(X0, X1, Y0, Y1, [0, 50, 100, 150, 200, 250], [0, 0.2, 0.4, 0.6, 0.8], fx, fy, 'pressure (kPa)', 'deviation (mV)',
                  yfmt=lambda v: f'{v:.1f}'))
    o.append(L(X0, fy(0), X1, fy(0), INK, 1.5))
    o.append(P([(fx(x), fy(0.6 * math.sin(math.pi * x / 250))) for x in range(0, 251, 5)], LV, 3))
    o.append(C(fx(125), fy(0.6), 5, LV))
    o.append(Tb(fx(125), fy(0.6) - 12, '0.6 mV = 3 kPa = 1.2 %FS', 13, 'middle', LV, True))
    o.append(T(fx(125), fy(0) + 20, 'ideal line, 0.2 mV/kPa', 13, 'middle', INK))
    # right: readings at a true 100 kPa
    X0, X1 = 400, 700
    gx = lin(97.5, 102, X0, X1)
    yb = 230
    o.append(T(550, 24, 'Ten readings at a true 100 kPa', 14, 'middle', INK, True))
    o.append(R(gx(98.1), 120, gx(101.1) - gx(98.1), yb - 120, NXS, NX, 0, 1.5))
    pts = [(gx(97.6 + i * 0.05), yb - 100 * math.exp(-0.5 * ((97.6 + i * 0.05 - 99.6) / 0.5) ** 2)) for i in range(87)]
    o.append(P(pts, AC, 2.5))
    o.append(xaxis(X0, X1, yb, [98, 99, 100, 101, 102], gx, 'reading (kPa)'))
    o.append(L(gx(100), 70, gx(100), yb, INK, 2, '5 4')); o.append(T(gx(100) + 6, 84, 'true 100.0', 13, 'start', INK, True))
    o.append(L(gx(99.6), 110, gx(99.6), yb, AC, 2)); o.append(T(gx(99.6) - 6, 104, 'mean 99.6', 13, 'end', AC, True))
    o.append(arrow(gx(100), 96, gx(99.6) + 3, 96, INK, 1.5));
    o.append(T(gx(99.6), 300, '±3s band 98.1 to 101.1 kPa', 13, 'middle', NX, True))
    o.append(T(gx(99.6), 322, 'bias −0.4 kPa; s = 0.5 kPa', 13, 'middle', INK))
    return 340, ''.join(o)


FIG[4] = (f4, 'The worked example in two pictures. Left: the measured curve minus the ideal 0.2 mV/kPa line, bowing 0.6 mV (3 kPa, '
              '1.2 %FS) at mid-span. Right: readings at a true 100 kPa scatter with s = 0.5 kPa about a mean of 99.6 kPa: a small bias '
              'of −0.4 kPa, and a ±3s band from 98.1 to 101.1 kPa.',
          'Left: deviation of the measured output from the ideal line in millivolts against pressure from 0 to 250 kilopascals, a hump '
          'rising to 0.6 millivolts at 125 kilopascals. Right: a bell curve of readings centred at 99.6 kilopascals with a shaded '
          'band from 98.1 to 101.1, a dashed line at the true 100.0 and an arrow showing the bias of minus 0.4.')


# ---- 1.5 step responses of worked example 1 and the catheter frequency response of worked example 2 ----
def f5():
    o = []
    # top: thermocouple 25 -> 100 C, tau 2 s
    X0, X1, Y0, Y1 = 80, 690, 40, 220
    fx = lin(0, 10, X0, X1); fy = lin(20, 110, Y1, Y0)
    o.append(axes(X0, X1, Y0, Y1, [0, 2, 4, 6, 8, 10], [20, 40, 60, 80, 100], fx, fy, 'time (s)', 'thermocouple reading (°C), τ = 2 s'))
    o.append(L(fx(0), fy(100), fx(10), fy(100), MUT, 1.5, '5 4')); o.append(T(fx(10), fy(100) - 7, 'bath 100 °C', 13, 'end', MUT))
    o.append(P([(fx(t / 10), fy(25 + 75 * (1 - math.exp(-t / 20)))) for t in range(0, 101)], AC, 3))
    for t, v in ((2, 72.4), (6, 96.3)):
        o.append(L(fx(t), fy(v), fx(t), Y1, L2, 1.2, '4 3')); o.append(C(fx(t), fy(v), 5, AC))
    o.append(Tb(fx(2) + 10, fy(72.4) + 18, '72.4 °C at τ (63.2 %)', 13, 'start', AC, True))
    o.append(Tb(fx(6), fy(96.3) + 22, '96.3 °C at 3τ (95.0 %)', 13, 'middle', AC, True))
    # bottom left: second order step, fn 1 Hz, zeta 0.2
    X0, X1, Y0, Y1 = 80, 340, 320, 520
    gx = lin(0, 4, X0, X1); gy = lin(0, 1.6, Y1, Y0)
    o.append(axes(X0, X1, Y0, Y1, [0, 1, 2, 3, 4], [0, 0.5, 1.0, 1.5], gx, gy, 'time (s)', 'diaphragm, ζ = 0.2', yfmt=lambda v: f'{v:.1f}'))
    wn, z = 2 * math.pi, 0.2; wd = wn * math.sqrt(1 - z * z)
    y = lambda t: 1 - math.exp(-z * wn * t) * (math.cos(wd * t) + z / math.sqrt(1 - z * z) * math.sin(wd * t))
    o.append(P([(gx(t / 50), gy(y(t / 50))) for t in range(0, 201)], LV, 2.5))
    o.append(L(X0, gy(1), X1, gy(1), MUT, 1.2, '5 4'))
    o.append(C(gx(0.510), gy(1.527), 5, LV)); o.append(T(gx(0.51) + 10, gy(1.527) + 4, '1.527 at 0.51 s (52.7 %)', 13, 'start', LV, True))
    o.append(L(gx(3.18), Y1, gx(3.18), gy(0.9), L2, 1.2, '4 3')); o.append(T(gx(3.18) - 6, gy(0.78), 't' + sub('s') + ' ≈ 3.2 s', 13, 'end', INK))
    # bottom right: catheter amplitude ratio, fn 25 Hz
    X0, X1 = 430, 690
    hx = lin(0, 40, X0, X1); hy = lin(0, 3, Y1, Y0)
    o.append(axes(X0, X1, Y0, Y1, [0, 10, 20, 30, 40], [0, 1, 2, 3], hx, hy, 'frequency (Hz)', 'catheter, f' + sub('n') + ' = 25 Hz'))
    M = lambda f, zz: 1 / math.sqrt((1 - (f / 25) ** 2) ** 2 + (2 * zz * f / 25) ** 2)
    o.append(P([(hx(f / 4), hy(min(3, M(f / 4, 0.2)))) for f in range(0, 161)], LV, 2.5))
    o.append(P([(hx(f / 4), hy(M(f / 4, 0.6))) for f in range(0, 161)], AC, 2.5))
    o.append(C(hx(20), hy(2.076), 5, LV)); o.append(Tb(hx(20) - 8, hy(2.076) - 6, '2.08 at 20 Hz', 13, 'end', LV, True))
    o.append(C(hx(20), hy(0.975), 5, AC)); o.append(Tb(hx(20) + 6, hy(0.975) + 20, '0.975', 13, 'start', AC, True))
    o.append(T(hx(36), hy(2.6), 'ζ = 0.2', 13, 'middle', LV, True)); o.append(T(hx(8), hy(0.7), 'ζ = 0.6', 13, 'middle', AC, True))
    return 580, ''.join(o)


FIG[5] = (f5, 'Top: the τ = 2 s bead dipped from 25 °C into 100 °C reads 72.4 °C at 2 s and 96.3 °C at 6 s. Bottom left: the 1 Hz, '
              'ζ = 0.2 diaphragm overshoots to 1.527 at 0.51 s. Bottom right: the 25 Hz catheter doubles a 20 Hz harmonic at ζ = 0.2 '
              '(2.08) but passes it at 0.975 with ζ = 0.6.',
          'Three plots. Top: thermocouple reading against time from 0 to 10 seconds rising from 25 towards 100 degrees, with 72.4 at 2 '
          'seconds and 96.3 at 6 seconds marked. Bottom left: second order step response with damping 0.2, peaking at 1.527 at 0.51 '
          'seconds and settling by about 3.2 seconds. Bottom right: amplitude ratio against frequency up to 40 hertz for a 25 hertz '
          'catheter system; the damping 0.2 curve peaks near 24 hertz and is 2.08 at 20 hertz, the damping 0.6 curve stays near 1 and is 0.975 at 20 hertz.')


# ---- 1.6 the ten readings of the 5.000 V reference ----
def f6():
    o = []
    X0, X1 = 80, 640
    fx = lin(-40, 40, X0, X1)
    yb = 230
    o.append(T(360, 22, 'Ten readings of a 5.000 V reference, as deviations from the mean', 14, 'middle', INK, True))
    o.append(R(fx(-18.26), 60, fx(18.26) - fx(-18.26), yb - 60, NXS, NX, 0, 1.5))
    o.append(L(fx(0), 56, fx(0), yb, INK, 2, '5 4'))
    o.append(R(fx(-12.91), 140, fx(12.91) - fx(-12.91), 16, ACS, AC, 4, 2))
    o.append(Tb(360, 128, '95 % interval of the mean ±12.9 mV', 13, 'middle', AC, True))
    counts = {-30: 1, -20: 1, -10: 2, 0: 2, 10: 2, 20: 1, 30: 1}
    for v, n in counts.items():
        for j in range(n):
            o.append(C(fx(v), yb - 14 - j * 22, 8, LV if abs(v) == 30 else AC))
    o.append(xaxis(X0, X1, yb, [-40, -30, -20, -10, 0, 10, 20, 30, 40], fx, 'deviation (mV)', fmt=neg))
    o.append(T(fx(0), 50, 'mean 5.000 V', 13, 'middle', INK, True))
    o.append(T(fx(-18.26) + 6, 80, '−s', 13, 'start', NX, True)); o.append(T(fx(18.26) - 6, 80, '+s', 13, 'end', NX, True))
    o.append(T(fx(-30), yb - 44, '4.97 V', 13, 'middle', LV, True)); o.append(T(fx(30), yb - 44, '5.03 V', 13, 'middle', LV, True))
    o.append(T(80, 304, 's = √(3000/9) = 18.26 mV;   s/√10 = 5.77 mV;   resolution 5/√3 = 2.89 mV', 13, 'start', INK))
    o.append(T(80, 326, 'combined u = √(5.77² + 2.89²) = 6.46 mV;   k = 2 gives ±12.9 mV', 13, 'start', INK, True))
    return 340, ''.join(o)


FIG[6] = (f6, 'The worked example’s ten readings as deviations from their 5.000 V mean. One reading spreads ±18.3 mV (the shaded ±s '
              'band), but the mean is known far better: combined with the display resolution its 95 % interval is only ±12.9 mV.',
          'A dot plot of ten deviations in millivolts: one each at minus 30, minus 20, plus 20 and plus 30, two each at minus 10, 0 and '
          'plus 10. A shaded band shows plus and minus one standard deviation, 18.26 millivolts; a narrower box shows the 95 percent '
          'interval of the mean, plus and minus 12.9 millivolts. Formulas below give s, s over root 10, the resolution term and the combined uncertainty.')

spec = make_spec(FIG)
