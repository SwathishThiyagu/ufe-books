"""Claude's hand-drawn figures for ei-sensor-u3 (Sensors and Measurements: inductive and capacitive transducers), one per
chapter, drawn from each chapter's own worked examples and numbers. Colours are the shell's CSS variables only."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
AFTER = {1: 3, 2: 2, 3: 3, 4: 1, 5: 1, 6: 2, 7: 3}


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


def arrow(x1, y1, x2, y2, c=AC, w=2, k='n', dash=None):
    return L(x1, y1, x2, y2, c, w, dash, arrow=k)


def sub(s):
    return f'<tspan baseline-shift="sub" font-size="11">{s}</tspan>'


def coil_v(x, y0, y1, c=AC, n=8, w=26):
    """a coil drawn as slanted turns across a vertical leg at x"""
    o = []
    for i in range(n):
        y = y0 + (y1 - y0) * (i + 0.5) / n
        o.append(L(x - w / 2, y - 4, x + w / 2, y + 4, c, 2.2))
    return ''.join(o)


# ---- 3.1 variable reluctance: worked examples 1 and 2 ----
def f1():
    o = []
    o.append(T(165, 22, 'Push-pull pair (worked example 2)', 14, 'middle', INK, True))
    # two C-cores facing a central armature
    for (x, lab, gap, Ls, col) in ((40, 'coil 1', '0.9 mm', 'L₁ = 69.81 mH', AC), (230, 'coil 2', '1.1 mm', 'L₂ = 57.12 mH', LV)):
        o.append(R(x, 50, 60, 140, PANEL, INK, 4, 2))
        o.append(R(x + (60 if x < 150 else -20), 50, 20, 30, PANEL, INK, 2, 2))
        o.append(R(x + (60 if x < 150 else -20), 160, 20, 30, PANEL, INK, 2, 2))
        o.append(coil_v(x + 30, 70, 170, col))
        o.append(T(x + 30, 210, lab, 13, 'middle', col, True))
        o.append(T(x + 30, 228, Ls, 13, 'middle', col))
    o.append(R(145, 60, 30, 120, ACS, AC, 3, 2))
    o.append(T(165, 252, 'armature moved 0.1 mm to coil 1', 13, 'middle', INK))
    o.append(T(128, 46, '0.9', 12, 'middle', AC)); o.append(T(196, 46, '1.1 mm', 12, 'middle', LV))
    o.append(T(165, 280, 'V' + sub('o') + ' = (5/2) × 12.69/126.93 = 0.250 V rms', 13, 'middle', AC, True))
    o.append(T(165, 302, 'single coil: +0.132 V and −0.119 V', 13, 'middle', MUT))
    # right: L vs g
    X0, X1, Y0, Y1 = 410, 680, 54, 260
    fx = lin(0.5, 1.5, X0, X1); fy = lin(30, 130, Y1, Y0)
    o.append(T(545, 22, 'L = μ₀AN²/g (worked example 1)', 14, 'middle', INK, True))
    o.append(axes(X0, X1, Y0, Y1, [0.5, 0.75, 1.0, 1.25, 1.5], [30, 50, 70, 90, 110, 130], fx, fy, 'air gap g (mm)', 'L (mH)'))
    o.append(P([(fx(g / 100), fy(62.83 / (g / 100))) for g in range(50, 151, 2)], AC, 3))
    for g, s, dx, dy, anc in ((1.0, '62.83 mH at 1.0 mm', 8, -12, 'start'), (1.2, '52.36 mH at 1.2 mm', -8, 24, 'end')):
        o.append(C(fx(g), fy(62.83 / g), 5, LV))
        o.append(Tb(fx(g) + dx, fy(62.83 / g) + dy, s, 13, anc, LV, True))
    o.append(T(fx(1.48), fy(118), '+20 % gap → −16.7 % L', 13, 'end', INK))
    return 320, ''.join(o)


FIG[1] = (f1, 'Right: the single-coil law L = μ₀AN²/g of worked example 1, 62.83 mH at 1.0 mm and 52.36 mH at 1.2 mm. Left: worked '
              'example 2, a push-pull pair; moving the armature 0.1 mm gives 69.81 and 57.12 mH and 0.250 V rms from a 5 V half bridge, '
              'the same size either way, where one coil gives only +0.132 and −0.119 V.',
          'Left: two coils on iron cores either side of a central armature, gaps 0.9 and 1.1 millimetres, inductances 69.81 and 57.12 '
          'millihenry, bridge output 0.250 volts. Right: graph of inductance against air gap falling as one over g, with 62.83 '
          'millihenry at 1.0 millimetre and 52.36 millihenry at 1.2 millimetres marked.')


# ---- 3.2 LVDT: worked examples ----
def f2():
    o = []
    o.append(T(350, 22, 'LVDT: core displaced toward S₁ (worked example 1)', 14, 'middle', INK, True))
    o.append(R(60, 50, 580, 60, PANEL, MUT, 6, 1.2))
    for x0, lab, col in ((70, 'S₁: V₁ = 2.00 V', LV), (260, 'primary, 5 V rms', AC), (450, 'S₂: V₂ = 1.60 V', LV)):
        for i in range(16):
            o.append(L(x0 + 8 + i * 11, 54, x0 + 13 + i * 11, 106, col, 1.6))
        o.append(T(x0 + 92, 128, lab, 13, 'middle', col, True))
    o.append(R(170, 72, 250, 16, ACS, AC, 3, 2)); o.append(T(295, 84, 'core', 12, 'middle', AC, True))
    o.append(L(420, 80, 650, 80, INK, 2))
    o.append(L(350, 140, 350, 150, INK, 1, '3 3')); o.append(arrow(350, 146, 314, 146, NX, 2, 'x'))
    o.append(T(356, 150, 'x = 0.80 mm', 13, 'start', NX, True))
    # right-bottom: output graph signed and magnitude
    X0, X1, Y0, Y1 = 90, 420, 186, 330
    fx = lin(-2.5, 2.5, X0, X1); fy = lin(-0.6, 0.6, Y1, Y0)
    o.append(L(X0, fy(0), X1, fy(0), L2, 1.5)); o.append(L(fx(0), Y0, fx(0), Y1, L2, 1.5))
    for v in (-2, -1, 1, 2): o.append(T(fx(v), fy(0) + 18, neg(v), 12, 'middle', MUT))
    o.append(T(X1, fy(0) - 8, 'x (mm)', 13, 'end', MUT))
    o.append(T(fx(0) + 6, Y0 + 4, 'output (V)', 13, 'start', MUT))
    o.append(P([(fx(-2.5), fy(1.25 * 0.24 * 2)), (fx(0), fy(0)), (fx(2.5), fy(0.6))], LV, 2, '6 4'))
    o.append(P([(fx(-2.5), fy(-0.6)), (fx(2.5), fy(0.6))], AC, 3))
    o.append(Tb(fx(-2.45), fy(0.15), '|V' + sub('out') + '| on a meter', 12, 'start', LV))
    o.append(T(fx(0.3), fy(-0.27), 'demodulated: 0.24 V/mm at 3 V', 12, 'start', AC))
    o.append(C(fx(-1.2), fy(-0.288), 5, AC)); o.append(T(fx(0.3), fy(-0.47), 'dot: −1.20 mm gives −0.288 V', 12, 'start', AC, True))
    o.append(T(470, 210, 'Worked example 1 (K = 0.50 V/mm):', 13, 'start', INK, True))
    o.append(T(470, 232, 'V₁ − V₂ = 2.00 − 1.60 = 0.40 V', 13, 'start', INK))
    o.append(T(470, 254, 'x = 0.40/0.50 = 0.80 mm to S₁', 13, 'start', AC, True))
    o.append(T(470, 284, 'Worked example 2 (tendon rig):', 13, 'start', INK, True))
    o.append(T(470, 306, '±2.5 mm → ±0.60 V; linearity ±6.25 µm', 13, 'start', INK))
    o.append(T(470, 328, '−1.20 mm → −4.80 V after demodulator', 13, 'start', AC))
    return 346, ''.join(o)


FIG[2] = (f2, 'Top: worked example 1; the core sits 0.80 mm toward S₁, so V₁ = 2.00 V beats V₂ = 1.60 V and the 0.40 V difference is '
              'in phase. Bottom: a meter sees the V-shaped magnitude, which hides the side; the demodulated output of worked example 2 '
              '(0.24 V/mm at 3 V) is a straight line through zero, −0.288 V at −1.20 mm.',
          'Top: LVDT with secondary 1, primary and secondary 2 on a former and the core shifted 0.80 millimetres toward secondary 1; '
          'secondary voltages 2.00 and 1.60 volts. Bottom: graph of output against core position from minus 2.5 to plus 2.5 '
          'millimetres; a dashed V shape for the meter reading and a straight signed line after demodulation, with minus 0.288 volts '
          'at minus 1.20 millimetres marked.')


# ---- 3.3 synchro pair: worked example 1 ----
def stator(cx, cy, r, rot, rcol, label, mirror=False):
    o = [f'<circle cx="{cx}" cy="{cy}" r="{r}" style="fill:var(--panel);stroke:var(--ink);stroke-width:2"/>']
    pts = []
    for i, ang in enumerate((90, 210, -30) if mirror else (90, -30, 210)):
        a = math.radians(ang)
        x, y = cx + r * math.cos(a), cy - r * math.sin(a)
        pts.append((x, y))
        o.append(C(x, y, 6, INK))
        lx, ly = cx + (r - 22) * math.cos(a), cy - (r - 22) * math.sin(a) + 5
        o.append(T(lx, ly, f'S{i + 1}', 12, 'middle', INK, True))
    a = math.radians(90 - rot)
    o.append(L(cx - (r - 14) * math.cos(a), cy + (r - 14) * math.sin(a), cx + (r - 14) * math.cos(a), cy - (r - 14) * math.sin(a), rcol, 6))
    o.append(C(cx, cy, 5, rcol))
    o.append(T(cx, cy + r + 34, label, 13, 'middle', rcol, True))
    return ''.join(o), pts


def f3():
    o = []
    o.append(T(350, 22, 'Synchro transmitter and control transformer (worked example 1)', 14, 'middle', INK, True))
    s1, p1 = stator(150, 140, 62, 30, AC, 'transmitter, rotor 30°')
    s2, p2 = stator(520, 140, 62, 40, LV, 'control transformer, rotor 40°', mirror=True)
    # wires: S1 over the top, S2 straight across, S3 under the bottom
    o.append(P([p1[0], (p1[0][0], 50), (p2[0][0], 50), p2[0]], MUT, 1.8))
    o.append(P([p1[1], p2[1]], MUT, 1.8))
    o.append(P([p1[2], (p1[2][0], 214), (p2[2][0], 214), p2[2]], MUT, 1.8))
    o.append(s1); o.append(s2)
    o.append(Tb(335, 55, 'S1: 5.90 V', 12, 'middle', INK, True))
    o.append(Tb(335, 175, 'S2: 0 V', 12, 'middle', INK, True))
    o.append(Tb(335, 219, 'S3: 5.90 V, antiphase', 12, 'middle', INK, True))
    o.append(T(40, 84, '26 V rms', 13, 'start', AC)); o.append(T(40, 100, 'to rotor', 13, 'start', AC))
    o.append(T(600, 84, 'rotor output', 13, 'start', LV)); o.append(T(600, 100, 'e = 1.74 V', 13, 'start', LV, True))
    o.append(T(30, 266, 'stator coils: 6.81 cos θ, 6.81 cos(θ − 120°), 6.81 cos(θ + 120°)', 13, 'start', INK))
    o.append(T(30, 288, 'error Δθ = 40° − 30° = 10°', 13, 'start', INK))
    o.append(T(30, 310, 'e = 10 sin 10° = 1.74 V rms → servo turns rotor back to 30°', 13, 'start', LV, True))
    return 324, ''.join(o)


FIG[3] = (f3, 'Worked example 1. The transmitter rotor at 30° puts 5.90 V, 0 V and 5.90 V (antiphase) on the three stator coils; the '
              'control transformer stator recreates that field, and its rotor, 10° away at 40°, gives e = 10 sin 10° = 1.74 V rms, '
              'the error that drives the servo back to zero.',
          'Two circles: a synchro transmitter with its rotor at 30 degrees and a control transformer with its rotor at 40 degrees, '
          'joined by three stator wires carrying 5.90 volts, 0 volts and 5.90 volts in antiphase; the control transformer rotor '
          'gives an error of 1.74 volts rms.')


# ---- 3.4 eddy current: worked examples 1 and 2 ----
def f4():
    o = []
    o.append(T(180, 22, 'Probe over a conducting target', 14, 'middle', INK, True))
    o.append(R(120, 44, 120, 100, PANEL, INK, 6, 2))
    o.append(coil_v(180, 96, 136, AC, 5, 80))
    o.append(T(180, 68, 'probe coil', 13, 'middle', AC, True)); o.append(T(180, 86, '100 kHz–1 MHz', 12, 'middle', MUT))
    o.append(R(60, 190, 240, 40, ACS, INK, 2, 2)); o.append(T(180, 252, 'aluminium target', 13, 'middle', INK))
    for rx in (30, 54, 78):
        o.append(f'<ellipse cx="180" cy="200" rx="{rx}" ry="7" style="fill:none;stroke:var(--live);stroke-width:1.8"/>')
    o.append(T(180, 225, 'eddy currents', 13, 'middle', LV, True))
    o.append(L(250, 144, 250, 190, NX, 1.6)); o.append(L(242, 144, 258, 144, NX, 1.6)); o.append(L(242, 190, 258, 190, NX, 1.6))
    o.append(T(258, 170, 'lift-off g', 13, 'start', NX, True))
    o.append(T(30, 282, 'skin depth δ: Al 0.259 mm at 100 kHz, 0.082 mm at 1 MHz', 12, 'start', INK))
    o.append(T(30, 302, 'a 0.5 mm Al sheet needs 1 MHz (3δ = 0.25 mm)', 12, 'start', MUT))
    X0, X1, Y0, Y1 = 420, 680, 54, 260
    fx = lin(0.5, 2.5, X0, X1); fy = lin(0, 8, Y1, Y0)
    o.append(T(550, 22, 'Calibration line (worked example 1)', 14, 'middle', INK, True))
    o.append(axes(X0, X1, Y0, Y1, [0.5, 1.0, 1.5, 2.0, 2.5], [0, 2, 4, 6, 8], fx, fy, 'gap g (mm)', 'output (V)'))
    o.append(P([(fx(0.6), fy(7.0)), (fx(2.4), fy(2.5))], AC, 3))
    for g, v, s, dx, anc in ((1.0, 6.0, '6.0 V at 1.0 mm', 10, 'start'), (1.6, 4.5, '4.5 V → 1.6 mm', 10, 'start'), (2.2, 3.0, '3.0 V at 2.2 mm', -10, 'end')):
        o.append(C(fx(g), fy(v), 5, LV)); o.append(Tb(fx(g) + dx, fy(v) - 12 if anc == 'start' else fy(v) + 24, s, 13, anc, LV, True))
    o.append(T(fx(2.4), fy(7.2), 'slope −2.5 V/mm', 13, 'end', INK))
    return 320, ''.join(o)


FIG[4] = (f4, 'Left: the probe field induces eddy currents in the target, whose opposing field changes the coil impedance; the field '
              'reaches a skin depth of 0.259 mm in aluminium at 100 kHz (worked example 2). Right: worked example 1’s calibration, '
              '6.0 V at 1.0 mm falling 2.5 V per mm, so 4.5 V means 1.6 mm and 2.2 mm gives 3.0 V.',
          'Left: a probe coil above an aluminium plate with eddy current loops in the plate and the lift-off gap marked. Right: a '
          'falling straight calibration line of output against gap, with 6.0 volts at 1.0 millimetre, 4.5 volts at 1.6 millimetres '
          'and 3.0 volts at 2.2 millimetres marked.')


# ---- 3.5 proximity: worked examples 1 and 2 ----
def f5():
    o = []
    X0, X1 = 150, 650
    fx = lin(0, 12, X0, X1)
    o.append(T(350, 22, 'Switching distances for S' + sub('n') + ' = 10 mm (worked example 1)', 14, 'middle', INK, True))
    o.append(R(X0 - 46, 50, 46, 190, PANEL, INK, 4, 2)); o.append(T(X0 - 23, 44, 'sensor face', 12, 'middle', MUT))
    rows = [('mild steel, K 1.00', 10.0, None), ('stainless, K 0.70', 7.0, 7.3), ('brass, K 0.50', 5.0, 5.2)]
    for i, (lab, s, tgt) in enumerate(rows):
        y = 74 + i * 62
        o.append(T(X0 + 6, y - 10, f'{lab}: S = {s:.1f} mm, certain within {0.9 * s:.1f} mm', 13, 'start', INK, True))
        o.append(R(fx(0), y, fx(0.9 * s) - fx(0), 18, ACS, AC, 2, 1.5))
        o.append(R(fx(0.9 * s), y, fx(1.1 * s) - fx(0.9 * s), 18, LVS, LV, 2, 1.5, '4 3'))
        o.append(L(fx(s), y - 4, fx(s), y + 22, INK, 2))
        if tgt:
            o.append(L(fx(tgt), y - 8, fx(tgt), y + 26, NX, 3)); o.append(T(fx(tgt), y + 40, f'target {tgt} mm: not sure', 12, 'middle', NX, True))
    o.append(xaxis(X0, X1, 260, [0, 2, 4, 6, 8, 10, 12], fx, 'distance from face (mm)'))
    o.append(R(40, 302, 16, 12, ACS, AC, 2, 1.5)); o.append(T(62, 313, 'always switches (≤ 0.9 S)', 12, 'start', INK))
    o.append(R(250, 302, 16, 12, LVS, LV, 2, 1.5, '4 3')); o.append(T(272, 313, 'may switch (0.9 S to 1.1 S)', 12, 'start', INK))
    o.append(T(470, 313, 'centrifuge: 4 slots, 400 Hz → 6000 rev/min', 12, 'start', MUT))
    return 330, ''.join(o)


FIG[5] = (f5, 'Worked example 1 drawn to scale. Each metal switches at S = K·S' + '<sub>n</sub>' + ', but only within 0.9 S is it certain; the '
              'brass target at 5.2 mm and the stainless one at 7.3 mm both sit in the uncertain band. Worked example 2 reads a '
              'centrifuge: 400 pulses per second from 4 slots is 6000 rev/min.',
          'Bars of switching distance from the sensor face for mild steel 10 millimetres, stainless steel 7.0 and brass 5.0, each '
          'with a certain zone up to 0.9 times and an uncertain zone up to 1.1 times; target lines at 7.3 and 5.2 millimetres fall in '
          'the uncertain zones.')


# ---- 3.6 differential capacitor: worked examples 1 and 2 ----
def f6():
    o = []
    o.append(T(170, 22, 'Three-plate sensor (worked example 2)', 14, 'middle', INK, True))
    o.append(R(40, 60, 260, 12, PANEL, INK, 2, 2)); o.append(T(170, 54, 'fixed plate 1', 12, 'middle', MUT))
    o.append(R(40, 190, 260, 12, PANEL, INK, 2, 2)); o.append(T(170, 220, 'fixed plate 2', 12, 'middle', MUT))
    o.append(R(40, 117, 260, 10, ACS, AC, 2, 2)); o.append(T(318, 126, 'moving plate', 12, 'start', AC, True))
    o.append(L(70, 72, 70, 117, LV, 1.5)); o.append(T(78, 100, 'd − x = 0.45 mm', 12, 'start', LV))
    o.append(T(200, 100, 'C₁ = 1.968 pF', 13, 'start', AC, True))
    o.append(L(70, 127, 70, 190, LV, 1.5)); o.append(T(78, 164, 'd + x = 0.55 mm', 12, 'start', LV))
    o.append(T(200, 164, 'C₂ = 1.610 pF', 13, 'start', AC, True))
    o.append(T(40, 254, '(C₁ − C₂)/(C₁ + C₂) = 0.358/3.578 = 0.100 = x/d', 13, 'start', INK))
    o.append(T(40, 276, 'bridge at 10 V: (10/2) × 0.100 = 0.500 V rms', 13, 'start', AC, True))
    o.append(T(40, 298, 'A = 100 mm², d = 0.50 mm, x = 0.05 mm', 12, 'start', MUT))
    X0, X1, Y0, Y1 = 430, 680, 54, 260
    fx = lin(-0.1, 0.1, X0, X1); fy = lin(-20, 20, Y1, Y0)
    o.append(T(555, 22, '% change against plate movement', 14, 'middle', INK, True))
    o.append(L(X0, fy(0), X1, fy(0), L2, 1.5)); o.append(L(fx(0), Y0, fx(0), Y1, L2, 1.5))
    for v in (-0.1, -0.05, 0.05, 0.1): o.append(T(fx(v), fy(0) + 18, neg(f'{v:g}'), 12, 'middle', MUT))
    for v in (-20, -10, 10, 20): o.append(T(fx(0) - 6, fy(v) + 4, neg(v), 12, 'end', MUT))
    o.append(T(X1, fy(0) - 26, 'x (mm)', 13, 'end', MUT)); o.append(T(fx(0) + 6, Y0 + 2, '%', 13, 'start', MUT))
    o.append(P([(fx(x / 1000), fy(100 * (0.5 / (0.5 - x / 1000) - 1))) for x in range(-100, 101, 5)], LV, 3))
    o.append(P([(fx(-0.1), fy(-20)), (fx(0.1), fy(20))], AC, 3, '7 4'))
    o.append(C(fx(0.05), fy(11.1), 5, LV)); o.append(Tb(fx(0.05) - 8, fy(11.1) - 12, 'single gap +11.1 %', 12, 'end', LV, True))
    o.append(C(fx(-0.05), fy(-9.1), 5, LV)); o.append(Tb(fx(-0.05) + 8, fy(-9.1) + 22, '−9.1 %', 12, 'start', LV, True))
    o.append(T(fx(0.1), 196, 'differential: ±10 %', 12, 'end', AC, True))
    return 320, ''.join(o)


FIG[6] = (f6, 'Left: worked example 2; moving the centre plate 0.05 mm gives 1.968 and 1.610 pF, and their difference over their sum is '
              'exactly x/d = 0.100, 0.500 V from a 10 V bridge. Right: a single gap (worked example 1’s 100 mm², 0.50 mm) changes '
              '+11.1 % and −9.1 % for ±0.05 mm, a curve; the differential output is a straight ±10 %.',
          'Left: a moving plate between two fixed plates with gaps 0.45 and 0.55 millimetres and capacitances 1.968 and 1.610 '
          'picofarads. Right: graph of percentage change against plate movement; the single-gap curve bends, reaching plus 11.1 '
          'percent and minus 9.1 percent at plus and minus 0.05 millimetres, while the differential line is straight.')


# ---- 3.7 microphone and ventilator pressure sensor ----
def f7():
    o = []
    o.append(T(170, 22, 'Capacitor microphone (worked example 1)', 14, 'middle', INK, True))
    o.append(L(40, 70, 300, 70, AC, 3)); o.append(T(170, 62, 'diaphragm, 25 mm²', 12, 'middle', AC, True))
    o.append(R(40, 110, 260, 16, PANEL, INK, 2, 2))
    for x in range(64, 290, 36): o.append(R(x, 110, 10, 16, FIGBG, INK, 0, 1))
    o.append(T(170, 146, 'back plate with holes', 12, 'middle', MUT))
    o.append(L(320, 70, 320, 110, LV, 1.5)); o.append(L(312, 70, 328, 70, LV, 1.5)); o.append(L(312, 110, 328, 110, LV, 1.5))
    o.append(T(326, 94, 'd = 20 µm', 12, 'start', LV, True))
    for x in (60, 96, 244, 280): o.append(arrow(x, 36, x, 64, NX, 1.6, 'x'))
    o.append(T(50, 50, 'sound', 12, 'end', NX))
    o.append(T(40, 184, '0.020 µm in: C 11.0675 → 11.0786 pF', 13, 'start', INK))
    o.append(T(40, 206, 'ΔC = 0.011 pF, a 0.10 % change', 13, 'start', AC, True))
    o.append(T(40, 236, 'charge amplifier: |V' + sub('out') + '| = V' + sub('p') + 'ΔC/C' + sub('f'), 13, 'start', INK))
    X0, X1, Y0, Y1 = 440, 680, 54, 260
    fx = lin(0, 100, X0, X1); fy = lin(6, 12, Y1, Y0)
    o.append(T(560, 22, 'Ventilator sensor (worked example 2)', 14, 'middle', INK, True))
    o.append(axes(X0, X1, Y0, Y1, [0, 25, 50, 75, 100], [6, 8, 10, 12], fx, fy, 'airway pressure (cmH₂O)', 'C (pF)'))
    o.append(P([(fx(p), fy(7.0832 * 5 / (5 - 0.02 * p))) for p in range(0, 101, 4)], LV, 3))
    o.append(P([(fx(0), fy(7.0832)), (fx(100), fy(7.0832 * 1.4))], AC, 2, '6 4'))
    o.append(C(fx(20), fy(7.699), 5, LV)); o.append(Tb(fx(20) + 8, fy(7.699) + 20, '7.70 pF: 0.31 V', 12, 'start', LV, True))
    o.append(C(fx(100), fy(11.805), 5, LV)); o.append(Tb(fx(100) - 8, fy(11.805) + 4, '11.81 pF: 2.36 V', 12, 'end', LV, True))
    o.append(T(fx(100), fy(8.3), 'small-change line', 12, 'end', AC)); o.append(T(fx(100), fy(7.9), '40 % low at 100', 12, 'end', AC))
    o.append(T(fx(2), fy(6.4), '7.08 pF at 0', 12, 'start', MUT))
    return 316, ''.join(o)


FIG[7] = (f7, 'Left: worked example 1; sound moves the 25 mm² diaphragm 0.020 µm across the 20 µm gap and C rises by only 0.011 pF '
              '(0.10 %). Right: worked example 2’s ventilator sensor; C = ε₀A/(d − x) climbs from 7.08 pF to 7.70 pF at 20 and 11.81 pF '
              'at 100 cmH₂O, well above the dashed small-change line.',
          'Left: a diaphragm above a perforated back plate with a 20 micrometre gap and sound arrows; capacitance rises from 11.0675 '
          'to 11.0786 picofarads. Right: graph of capacitance against airway pressure curving upward from 7.08 picofarads at zero to '
          '7.70 at 20 and 11.81 at 100 centimetres of water, above a dashed straight small-change line.')


spec = make_spec(FIG)
