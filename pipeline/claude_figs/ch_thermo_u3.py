"""Claude's hand-drawn figures for ch-thermo-u3 (Second law, entropy and cycles), one per chapter, each drawn from that
chapter's own worked example. Steam curves are computed with IAPWS-IF97 and R-134a curves with CoolProp when those
(values frozen below). Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def sb(base, s, size=11):
    return f'{base}<tspan baseline-shift="sub" font-size="{size}">{s}</tspan>'


def path(pts, c=AC, w=2.5, dash=None, fill='none'):
    da = f';stroke-dasharray:{dash}' if dash else ''
    d = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts)
    return f'<path d="{d}" style="fill:{fill};stroke:{c};stroke-width:{w}{da};stroke-linejoin:round"/>'


def res(x, y, w, h, title, sub, dash=None, stroke=AC):
    return R(x, y, w, h, PANEL, stroke, 8, dash=dash) + T(x + w / 2, y + 20, title, 14, bold=True) + T(x + w / 2, y + 38, sub, 13, fill=MUT)


def eng(x, y, r, label, stroke=AC, fill=ACS):
    return f'<circle cx="{x}" cy="{y}" r="{r}" style="fill:{fill};stroke:{stroke};stroke-width:2.5"/>' + T(x, y + 6, label, 17, bold=True)


# ---- 3.1 a real engine beside the forbidden perfect engine ----
def f1():
    o = []
    for cx, W, QC, ok in ((180, '40', '60', True), (540, '100', '0', False)):
        col = AC if ok else NX
        o.append(T(cx, 22, 'Real engine: allowed' if ok else 'Perfect engine: forbidden', 15, bold=True, fill=col))
        o.append(res(cx - 120, 36, 240, 48, 'Hot reservoir', '600 K', stroke=col))
        o.append(eng(cx - 30, 180, 36, 'E', col, ACS if ok else NXS))
        o.append(L(cx - 30, 84, cx - 30, 140, col, 2.5, arrow='n' if ok else 'x'))
        o.append(T(cx - 20, 118, sb('Q', 'H') + ' = 100 kJ', 14, 'start'))
        o.append(L(cx + 6, 180, cx + 96, 180, LV, 3, arrow='l'))
        o.append(T(cx + 48, 160, 'W = ' + W + ' kJ', 14, 'middle', LV, True))
        if ok:
            o.append(L(cx - 30, 216, cx - 30, 272, col, 2.5, arrow='n'))
            o.append(T(cx - 20, 250, sb('Q', 'C') + ' = ' + QC + ' kJ', 14, 'start'))
            o.append(res(cx - 120, 276, 240, 48, 'Cold reservoir', '300 K'))
            o.append(T(cx, 350, 'η = 40/100 = 40 %', 14, bold=True))
        else:
            o.append(res(cx - 120, 276, 240, 48, 'Cold reservoir', 'gets nothing', dash='6 4', stroke=L2))
            o.append(T(cx - 20, 250, sb('Q', 'C') + ' = 0', 14, 'start', NX))
            o.append(L(cx - 58, 152, cx - 2, 208, NX, 3)); o.append(L(cx - 2, 152, cx - 58, 208, NX, 3))
            o.append(T(cx, 350, 'η = 100 %: breaks Kelvin–Planck', 14, bold=True, fill=NX))
    o.append(L(360, 30, 360, 356, 'var(--line)', 1.5, '4 4'))
    return 370, ''.join(o)
FIG[1] = (f1, 'Both engines take 100 kJ from the 600 K reservoir. The real one rejects 60 kJ to the 300 K reservoir and gives 40 kJ of work; the one on the right would turn all 100 kJ into work with nothing rejected, which the Kelvin–Planck statement forbids.',
          'Left: an engine between a 600 K and a 300 K reservoir takes 100 kJ, gives 40 kJ of work and rejects 60 kJ. Right: a crossed-out engine takes 100 kJ and gives 100 kJ of work, rejecting nothing to the cold reservoir.')


# ---- 3.2 refrigerator energy flows with the example numbers ----
def f2():
    o = []
    cx = 230
    o.append(res(cx - 140, 20, 280, 50, 'Warm space: kitchen', '32 °C = 305.15 K'))
    o.append(eng(cx, 175, 40, 'R'))
    o.append(res(cx - 140, 280, 280, 50, 'Cold space', '4 °C = 277.15 K'))
    o.append(L(cx, 280, cx, 219, AC, 3, arrow='n')); o.append(T(cx + 12, 256, sb('Q', 'C') + ' = 5 kW', 14, 'start', bold=True))
    o.append(L(cx, 135, cx, 74, AC, 4, arrow='n')); o.append(T(cx + 12, 110, sb('Q', 'H') + ' = 7 kW', 14, 'start', bold=True))
    o.append(L(40, 175, cx - 44, 175, LV, 3, arrow='l')); o.append(T(42, 164, 'W = 2 kW', 14, 'start', LV, True))
    o.append(T(42, 198, 'compressor', 13, 'start', MUT))
    o.append(boxt(440, 40, 260, 120, ['Energy balance', 'heat out = heat in + work', '7 = 5 + 2 kW'], PANEL, L2, 14, True))
    o.append(boxt(440, 180, 260, 150, ['Ratings', 'refrigerator COP 5/2 = 2.5', 'heat-pump COP 7/2 = 3.5', 'reversible limit 9.90'], ACS, AC, 14, True))
    return 350, ''.join(o)
FIG[2] = (f2, 'The worked example: 5 kW enters from the cold space and 2 kW of compressor work enters, so 7 kW leaves to the kitchen. The heat rejected is the sum of the two inputs, which is why COP as a heat pump is one more than COP as a refrigerator.',
          'A refrigerator R between a 4 degree Celsius cold space and a 32 degree kitchen: 5 kW in from the cold side, 2 kW of work in, 7 kW out to the kitchen, with COP 2.5 as a refrigerator and 3.5 as a heat pump.')


# ---- 3.3 the Carnot cycle as a rectangle on T-S axes ----
def f3():
    o = []
    x0, x1, y0, y1 = 80, 470, 40, 330
    fx = lambda s: x0 + s / 2.5 * (x1 - x0)
    fy = lambda t: y1 - t / 700 * (y1 - y0)
    o.append(L(x0, y1, x1, y1, L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    for t in (0, 300, 600):
        o.append(L(x0 - 5, fy(t), x0, fy(t), L2, 1.5)); o.append(T(x0 - 9, fy(t) + 5, str(t), 13, 'end', MUT))
    o.append(T(x0, y0 - 14, 'T (K)', 14, 'start', MUT))
    o.append(T((x0 + x1) / 2, y1 + 50, 'entropy of the gas, S (kJ/K)', 14, fill=MUT))
    s1, s2 = 0.5, 0.5 + 1000 / 600
    o.append(f'<rect x="{fx(s1):.1f}" y="{fy(300):.1f}" width="{fx(s2) - fx(s1):.1f}" height="{fy(0) - fy(300):.1f}" style="fill:var(--line);stroke:none"/>')
    o.append(f'<rect x="{fx(s1):.1f}" y="{fy(600):.1f}" width="{fx(s2) - fx(s1):.1f}" height="{fy(300) - fy(600):.1f}" style="fill:var(--accent-soft);stroke:none"/>')
    pts = [(fx(s1), fy(600)), (fx(s2), fy(600)), (fx(s2), fy(300)), (fx(s1), fy(300)), (fx(s1), fy(600))]
    o.append(path(pts, AC, 3))
    for (a, b), lab, dx, dy, anc in (((s1, 600), '1', -10, -8, 'end'), ((s2, 600), '2', 10, -8, 'start'), ((s2, 300), '3', 10, 18, 'start'), ((s1, 300), '4', -10, 18, 'end')):
        o.append(C(fx(a), fy(b), 5, AC)); o.append(T(fx(a) + dx, fy(b) + dy, lab, 15, anc, bold=True))
    o.append(T(fx((s1 + s2) / 2), fy(600) - 14, '1→2 isothermal at 600 K, takes ' + sb('Q', 'H') + ' = 1000 kJ', 13, fill=AC, bold=True))
    o.append(T(fx((s1 + s2) / 2), fy(300) + 24, '3→4 at 300 K, rejects ' + sb('Q', 'C') + ' = 500 kJ', 13, bold=True))
    o.append(T(fx((s1 + s2) / 2), fy(450) + 5, 'W = 500 kJ (area)', 15, fill=AC, bold=True))
    o.append(T(fx((s1 + s2) / 2), fy(150) + 5, sb('Q', 'C') + ' = area under 3→4', 14, fill=MUT))
    o.append(T(fx(s2) + 10, fy(450) + 5, 'adiabatic', 13, 'start', MUT))
    o.append(brace(fx(s1), fx(s2), y1 + 12, MUT))
    o.append(T(fx((s1 + s2) / 2), y1 + 30, 'ΔS = 1000/600 = 1.667 kJ/K', 13, fill=MUT))
    o.append(boxt(500, 60, 205, 230, ['Worked example', 'reservoirs 600 K, 300 K', 'η = 1 − 300/600', '= 0.50', 'W = 0.50 × 1000', '= 500 kJ'], PANEL, L2, 14, True))
    return 400, ''.join(o)
FIG[3] = (f3, 'The Carnot engine of the worked example drawn on temperature–entropy axes. Heat enters at 600 K and leaves at 300 K over the same entropy change of 1.667 kJ/K, so the cycle is a rectangle: its area is the work, 500 kJ, and the area under the bottom side is the 500 kJ rejected.',
          'A rectangle on T against S axes from 300 K to 600 K and 1.667 kJ/K wide; the top side takes 1000 kJ, the bottom side rejects 500 kJ, and the enclosed area is 500 kJ of work.')


# ---- 3.4 two paths between the same two states ----
def f4():
    o = []
    x0, x1, y0, y1 = 80, 400, 40, 300
    fx = lambda v: x0 + (v - 5) / 20 * (x1 - x0)
    fy = lambda p: y1 - p / 300 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [5, 10, 15, 20, 25], [0, 100, 200, 300], fx, fy, 'V (L)', 'P (kPa)'))
    P = lambda v: 8.314 * 300 / v
    pts = [(fx(10 + i * 0.25), fy(P(10 + i * 0.25))) for i in range(41)]
    area = pts + [(fx(20), fy(0)), (fx(10), fy(0))]
    o.append(f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in area)}" style="fill:var(--accent-soft);stroke:none"/>')
    o.append(path(pts, AC, 3))
    o.append(L(fx(10.6), fy(268), fx(19.4), fy(150), NX, 2.5, '7 5', arrow='x'))
    o.append(T(fx(16.2), fy(268), 'free expansion:', 13, 'start', NX, True))
    o.append(T(fx(16.2), fy(250), 'no path of states', 13, 'start', NX))
    for v, lab in ((10, '1'), (20, '2')):
        o.append(C(fx(v), fy(P(v)), 6, AC)); o.append(T(fx(v) - 10, fy(P(v)) - 4, lab, 15, 'end', bold=True))
    o.append(T(fx(10) - 10, fy(P(10)) + 22, '249 kPa', 13, 'end', MUT))
    o.append(T(fx(20) + 8, fy(P(20)) + 22, '125 kPa', 13, 'start', MUT))
    o.append(T(fx(15), fy(45), 'reversible: Q = W = 1729 J', 13, 'middle', AC, True))
    o.append(T(fx(15), fy(25), '1 mol, 300 K, 10 L → 20 L', 13, 'middle', MUT))
    hx = 420
    o.append(boxt(hx, 30, 290, 52, ['Same end states, so', sb('ΔS', 'gas') + ' = R ln 2 = 5.76 J/K'], PANEL, L2, 14))
    rows = [('', 'reversible', 'free'), ('∫δQ/T', '5.76', '0'), (sb('ΔS', 'gas'), '5.76', '5.76'), (sb('ΔS', 'sur'), '−5.76', '0'), (sb('S', 'gen'), '0', '5.76')]
    for i, (a, b, c) in enumerate(rows):
        y = 112 + i * 34
        if i: o.append(L(hx, y - 22, hx + 290, y - 22, 'var(--line)', 1))
        o.append(T(hx + 8, y, a, 14, 'start', bold=(i == 0 or i == 4)))
        o.append(T(hx + 160, y, b, 14, 'middle', AC, i == 0))
        o.append(T(hx + 245, y, c, 14, 'middle', NX, i == 0))
    o.append(T(hx + 145, 290, 'all in J/K', 13, 'middle', MUT))
    return 350, ''.join(o)
FIG[4] = (f4, 'The two worked examples: 1 mol of ideal gas goes from 10 L to 20 L at 300 K, once along the reversible isotherm and once by free expansion. ΔS of the gas is 5.76 J/K both times because S is a state function; only the free expansion generates entropy.',
          'Pressure against volume: a reversible isotherm from 249 kPa at 10 L to 125 kPa at 20 L with the area under it shaded, a dashed arrow for the free expansion, and a table comparing the entropy terms of the two routes.')


# ---- 3.5 the turbine control volume ----
def f5():
    o = []
    o.append(R(150, 50, 300, 250, 'none', L2, 10, 1.8, '7 5'))
    o.append(T(300, 40, 'control volume (adiabatic: Q = 0)', 13, 'middle', MUT))
    o.append(f'<polygon points="200,130 400,80 400,270 200,220" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2.5"/>')
    o.append(T(300, 170, 'turbine', 15, 'middle', INK, True))
    o.append(T(300, 194, sb('S', 'gen') + ' = 0.689 kW/K', 14, 'middle', NX, True))
    o.append(L(40, 150, 196, 150, AC, 3, arrow='n'))
    o.append(T(40, 104, 'in: 2 kg/s, 3 MPa, 400 °C', 13, 'start', bold=True))
    o.append(T(40, 124, sb('s', 'in') + ' = 6.9233 kJ/(kg·K)', 13, 'start'))
    o.append(T(40, 178, '2 × 6.9233 = 13.847 kW/K', 13, 'start', AC))
    o.append(L(404, 240, 560, 240, AC, 3, arrow='n'))
    o.append(T(470, 214, 'out: 50 kPa, x = 0.95', 13, 'start', bold=True))
    o.append(T(470, 270, sb('s', 'out') + ' = 7.2679 kJ/(kg·K)', 13, 'start'))
    o.append(T(470, 290, '2 × 7.2679 = 14.536 kW/K', 13, 'start', AC))
    o.append(L(400, 120, 560, 120, LV, 3, arrow='l'))
    o.append(T(480, 108, 'power 1403 kW', 13, 'middle', LV, True))
    o.append(boxt(150, 318, 410, 44, [sb('S', 'gen') + ' = entropy out − entropy in = 14.536 − 13.847 = 0.689 kW/K'], NXS, NX, 13))
    return 375, ''.join(o)
FIG[5] = (f5, 'The steam turbine of the first worked example with its control volume. Entropy is carried in at 13.847 kW/K and out at 14.536 kW/K; no heat crosses the boundary, so the difference, 0.689 kW/K, is generated inside by friction and other losses.',
          'A turbine inside a dashed control volume: steam enters at 3 MPa and 400 degrees with 13.847 kW/K of entropy, leaves at 50 kPa with 14.536 kW/K, gives 1403 kW of power, and generates 0.689 kW/K.')


# ---- 3.6 the absolute entropy built in four pieces ----
def f6():
    o = []
    x0, x1 = 60, 680
    fx = lambda s: x0 + s / 160 * (x1 - x0)
    parts = [(0.27, 'Debye 0–10 K', 'var(--line2)'), (60.0, 'solid 10–200 K', 'var(--accent-soft)'), (40.0, 'melting at 200 K', 'var(--next-soft)'), (47.9, 'liquid 200–298 K', 'var(--live-soft)')]
    strokes = [L2, AC, NX, LV]
    y, h = 110, 76
    s = 0
    for (v, lab, fill), st in zip(parts, strokes):
        o.append(f'<rect x="{fx(s):.1f}" y="{y}" width="{max(fx(s + v) - fx(s), 2):.1f}" height="{h}" style="fill:{fill};stroke:{st};stroke-width:2"/>')
        s += v
    labels = [(0.27 / 2, 'aT³/3 = 0.27', 'Debye part', -1), (0.27 + 30, '∫C_p/T dT = 60.0', 'solid', 1), (60.27 + 20, '8000/200 = 40.0', 'melting', 1), (100.27 + 23.95, '120 ln(298.15/200)', 'liquid', 1)]
    for xv, a, b, side in labels:
        if side < 0:
            o.append(L(fx(xv), y, fx(xv) + 30, y - 40, MUT, 1.5)); o.append(T(fx(xv) + 34, y - 44, a + ' (' + b + ')', 13, 'start', MUT))
        else:
            o.append(T(fx(xv), y + 24, b, 14, 'middle', INK, True)); o.append(T(fx(xv), y + 44, a.replace('C_p', sb('C', 'p')), 13))
            if b == 'liquid': o.append(T(fx(xv), y + 63, '= 47.9', 13))
    o.append(xaxis(x0, x1, y + h + 20, [0, 40, 80, 120, 160], fx, 'absolute entropy S (J mol⁻¹ K⁻¹), counted from S = 0 at 0 K'))
    o.append(L(fx(148.2), y - 18, fx(148.2), y + h + 10, AC, 2.5, '5 4'))
    o.append(T(fx(148.2), y - 24, 'S(298.15 K) = 148.2', 14, 'middle', AC, True))
    return 280, ''.join(o)
FIG[6] = (f6, 'The second worked example as one bar: the absolute entropy at 298.15 K is the sum of the Debye part below 10 K, the solid integral, the melting jump and the liquid integral. The tiny first piece is why the third-law zero is easy to use in practice.',
          'A horizontal bar split into four pieces: 0.27 for the Debye part, 60.0 for the solid, 40.0 for melting and 47.9 for the liquid, adding to 148.2 joules per mole per kelvin.')


# ---- 3.7 ideal, actual and lost work of the turbine ----
def f7():
    o = []
    x0, x1 = 210, 600
    fx = lambda w: x0 + w / 900 * (x1 - x0)
    rows = [('ideal output', 805.0, ACS, AC, '805.0 kJ/kg'), ('actual output', 701.6, LVS, LV, '701.6 kJ/kg'), ('lost work', 103.4, NXS, NX, '103.4 kJ/kg')]
    for i, (lab, v, fill, st, txt) in enumerate(rows):
        y = 50 + i * 70
        o.append(T(x0 - 12, y + 26, lab, 14, 'end', INK, True))
        if i == 0: o.append(T(x0 - 12, y + 44, '(−' + sb('W', 'ideal') + ')', 13, 'end', MUT))
        o.append(R(x0, y, fx(v) - x0, 40, fill, st, 4))
        o.append(T(fx(v) + 8, y + 26, txt.replace('W_ideal', sb('W', 'ideal')), 13, 'start', st, True))
    o.append(L(fx(701.6), 50, fx(701.6), 240, L2, 1.5, '4 4'))
    o.append(xaxis(x0, x1, 270, [0, 300, 600, 900], fx, 'work per kg of steam (kJ/kg)'))
    o.append(T(360, 345, 'lost work = ' + sb('T', '0') + sb('S', 'gen') + ' = 300 × 0.3446 = 103.4 kJ/kg', 14, 'middle', NX, True))
    o.append(T(360, 368, 'second-law efficiency = 701.6/805.0 = 0.872', 14, 'middle', INK))
    return 385, ''.join(o)
FIG[7] = (f7, 'The steam turbine of the second worked example with T₀ = 300 K. A reversible turbine between the same inlet and outlet states could give 805.0 kJ/kg; the real one gives 701.6 kJ/kg, and the 103.4 kJ/kg gap is exactly T₀ times the entropy generated.',
          'Three horizontal bars: ideal output 805.0, actual output 701.6 and lost work 103.4 kilojoules per kilogram, with the lost work equal to 300 kelvin times 0.3446.')


# ---- 3.8 the Rankine cycle on T-s axes (IAPWS-IF97 values) ----
# water: (T °C, s_f, s_g) on the saturation line, then the 4 MPa line (s, T) below and above boiling; IAPWS-IF97 values
DOME = [(10, 0.1511, 8.8998), (20, 0.2965, 8.6661), (30, 0.4368, 8.4521), (40, 0.5724, 8.2557), (50, 0.7038, 8.0749), (60, 0.8312, 7.9082), (70, 0.955, 7.754), (80, 1.0754, 7.611), (90, 1.1927, 7.4781), (100, 1.307, 7.3541), (110, 1.4187, 7.238), (120, 1.5278, 7.1291), (130, 1.6346, 7.0264), (140, 1.7393, 6.9293), (150, 1.842, 6.837), (160, 1.9428, 6.7491), (170, 2.0419, 6.6649), (180, 2.1395, 6.5841), (190, 2.2358, 6.506), (200, 2.3308, 6.4303), (210, 2.4248, 6.3565), (220, 2.5178, 6.2842), (230, 2.6102, 6.2131), (240, 2.7019, 6.1425), (250, 2.7934, 6.0722), (260, 2.8847, 6.0017), (270, 2.9762, 5.9304), (280, 3.0681, 5.8578), (290, 3.1608, 5.7832), (300, 3.2547, 5.7058), (310, 3.3506, 5.6243), (320, 3.4491, 5.5373), (330, 3.5516, 5.4425), (340, 3.6599, 5.3359), (350, 3.7783, 5.2109), (360, 3.9164, 5.0527), (370, 4.1142, 4.7996), (371, 4.1456, 4.7575), (373.946, 4.412, 4.412)]
LIQ4 = [(0.65, 46), (0.804, 58), (0.9526, 70), (1.0964, 82), (1.2358, 94), (1.3712, 106), (1.5028, 118), (1.631, 130), (1.7562, 142), (1.8785, 154), (1.9984, 166), (2.116, 178), (2.2317, 190), (2.3458, 202), (2.4587, 214), (2.5706, 226), (2.6819, 238)]
SUP4 = [(6.0746, 251), (6.145, 261), (6.2076, 271), (6.265, 281), (6.3184, 291), (6.3687, 301), (6.4165, 311), (6.462, 321), (6.5056, 331), (6.5477, 341), (6.5883, 351), (6.6276, 361), (6.6658, 371), (6.703, 381), (6.7393, 391)]


def f8():
    dome, liq, sup = DOME, LIQ4, SUP4
    o = []
    x0, x1, y0, y1 = 70, 470, 30, 330
    fx = lambda s: x0 + s / 9 * (x1 - x0)
    fy = lambda t: y1 - t / 450 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 2, 4, 6, 8], [0, 100, 200, 300, 400], fx, fy, 's (kJ/kg·K)', 'T (°C)'))
    left = [(fx(sf), fy(t)) for t, sf, sg in dome]
    right = [(fx(sg), fy(t)) for t, sf, sg in reversed(dome)]
    o.append(path(left + right, L2, 2))
    o.append(T(fx(3.0), fy(392), 'critical point 374 °C', 13, 'end', MUT))
    s1, s3, s4a = 0.6492, 6.7712, 7.2745
    cyc = [(fx(s1), fy(45.8)), (fx(0.6492), fy(45.94))] + [(fx(s), fy(t)) for s, t in liq] + [(fx(2.7967), fy(250.36)), (fx(6.0697), fy(250.36))] + [(fx(s), fy(t)) for s, t in sup] + [(fx(s3), fy(400))]
    o.append(path(cyc, AC, 3))
    o.append(L(fx(s3), fy(400), fx(s3), fy(45.8), LV, 3))
    o.append(L(fx(s3), fy(45.8), fx(s1), fy(45.8), AC, 3))
    o.append(L(fx(s3), fy(400), fx(s4a), fy(45.8), NX, 2, '6 4'))
    for s, t, lab, dx, dy, anc in ((s1, 45.8, '1', -10, 18, 'end'), (0.70, 52, '2', 12, -6, 'start'), (s3, 400, '3', 8, -8, 'start'), (s3, 45.8, '4', -6, 20, 'end'), (s4a, 45.8, '4a', 6, 20, 'start')):
        o.append(C(fx(s), fy(t), 5, NX if lab == '4a' else AC)); o.append(T(fx(s) + dx, fy(t) + dy, lab, 14, anc, NX if lab == '4a' else INK, True))
    o.append(T(fx(3.9), fy(262), 'boils at 250.4 °C (4 MPa)', 13, 'middle', AC))
    o.append(T(fx(3.6), fy(45.8) - 10, 'condenses at 45.8 °C', 13, 'middle', AC))
    o.append(T(fx(s3) + 8, fy(220), 'turbine', 13, 'start', LV, True))
    rows = ['Worked example (per kg)', 'pump work 4.0 kJ', 'boiler heat 3018.6 kJ', 'turbine work 1069.9 kJ', 'condenser heat 1952.7 kJ', 'η = 1065.9/3018.6 = 35.3 %', '85 % turbine (to 4a): 30.0 %']
    o.append(boxt(495, 40, 215, 270, rows, PANEL, L2, 14, True))
    return 380, ''.join(o)
FIG[8] = (f8, 'The worked example on temperature–entropy axes, with the saturation dome of water. The pump (1→2) hardly shows, the boiler line 2→3 heats, boils at 250.4 °C and superheats to 400 °C, the ideal turbine drops straight to 4 at x = 0.816, and the real 85 % turbine ends to the right at 4a: more entropy, a drier exhaust (x = 0.883) and less work.',
          'Temperature against entropy for water with the saturation dome; the Rankine cycle 1-2-3-4 between 4 MPa, 400 degrees and 10 kPa, a vertical isentropic turbine line from 3 to 4 and a dashed real expansion from 3 to 4a, with a table of the cycle energies.')


# ---- 3.9 the R-134a cycle on P-h axes ----
# R-134a saturation line (P MPa, h_f, h_g kJ/kg), CoolProp 8.0 values, IIR reference (h = 200 kJ/kg for saturated liquid at 0 °C)
RDOME = [(0.1, 165.4, 382.6), (0.14, 175.2, 387.3), (0.2, 186.6, 392.6), (0.3, 200.9, 399.0), (0.4, 212.1, 403.7), (0.5, 221.5, 407.5), (0.6, 229.7, 410.6), (0.7, 237.0, 413.2), (0.8, 243.6, 415.5), (0.9, 249.8, 417.4), (1.0, 255.5, 419.2)]


def f9():
    dome = RDOME
    o = []
    x0, x1, y0, y1 = 80, 470, 40, 320
    fx = lambda h: x0 + (h - 150) / 300 * (x1 - x0)
    fy = lambda p: y1 - p / 1.0 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [150, 250, 350, 450], [0, 0.2, 0.4, 0.6, 0.8, 1.0], fx, fy, 'h (kJ/kg)', 'P (MPa)', yfmt=lambda v: f'{v:g}'))
    o.append(path([(fx(hf), fy(p)) for p, hf, hg in dome], L2, 2))
    o.append(path([(fx(hg), fy(p)) for p, hf, hg in dome], L2, 2))
    h1, h2, h3 = 387.3, 423.5, 243.6
    o.append(L(fx(h3), fy(0.14), fx(h1), fy(0.14), AC, 3, arrow='n'))
    o.append(L(fx(h1), fy(0.14), fx(h2), fy(0.8), LV, 3, arrow='l'))
    o.append(L(fx(h2), fy(0.8), fx(h3), fy(0.8), NX, 3, arrow='m'))
    o.append(L(fx(h3), fy(0.8), fx(h3), fy(0.14), MUT, 2.5, '6 4', arrow='m'))
    for h, p, lab, dx, dy, anc in ((h1, 0.14, '1', 8, 18, 'start'), (h2, 0.8, '2', 8, -8, 'start'), (h3, 0.8, '3', -8, -8, 'end'), (h3, 0.14, '4', -8, 18, 'end')):
        o.append(C(fx(h), fy(p), 5, AC)); o.append(T(fx(h) + dx, fy(p) + dy, lab, 14, anc, bold=True))
    o.append(T(fx(315), fy(0.14) + 22, 'evaporator, −18.8 °C', 13, 'middle', AC, True))
    o.append(T(fx(330), fy(0.8) - 12, 'condenser, 31.3 °C', 13, 'middle', NX, True))
    o.append(T(fx(h3) - 10, fy(0.47), 'valve', 13, 'end', MUT, True))
    o.append(T(fx(h3) - 10, fy(0.47) + 18, 'h constant', 13, 'end', MUT))
    o.append(T(fx(382), fy(0.30), 'compressor', 13, 'end', LV, True))
    rows = ['Per kg of R-134a', 'evaporator 387.3 − 243.6', '= 143.7 kJ', 'compressor 423.5 − 387.3', '= 36.2 kJ', 'COP = 143.7/36.2 = 3.97', 'Carnot COP 5.08']
    o.append(boxt(495, 40, 215, 270, rows, PANEL, L2, 14, True))
    return 380, ''.join(o)
FIG[9] = (f9, 'The worked example on pressure–enthalpy axes, with the R-134a saturation dome. The evaporator and condenser are horizontal lines at 0.14 and 0.8 MPa, the throttle is a vertical line because h does not change, and the two enthalpy differences give COP = 143.7/36.2 = 3.97.',
          'Pressure against enthalpy for R-134a with the saturation dome; the cycle 1-2-3-4 with evaporation at 0.14 megapascal from 243.6 to 387.3 kilojoules per kilogram, compression to 423.5 at 0.8 megapascal, condensation to 243.6 and a vertical throttle back down.')


# ---- 3.10 microstates of four molecules in two halves ----
def f10():
    o = []
    x0, x1, y0, y1 = 80, 470, 40, 300
    om = [1, 4, 6, 4, 1]
    fy = lambda v: y1 - v / 7 * (y1 - y0)
    o.append(L(x0, y1, x1, y1, L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    for v in range(0, 8):
        o.append(L(x0 - 5, fy(v), x0, fy(v), L2, 1.5))
        if v % 2 == 0 or v == 7: o.append(T(x0 - 9, fy(v) + 5, str(v), 13, 'end', MUT))
    o.append(T(x0, y0 - 16, 'Ω, microstates', 14, 'start', MUT))
    bw = 50
    for n, w in enumerate(om):
        cx = x0 + 40 + n * 78
        o.append(R(cx - bw / 2, fy(w), bw, y1 - fy(w), ACS if n != 2 else NXS, AC if n != 2 else NX, 4))
        o.append(T(cx, fy(w) - 26, f'Ω = {w}', 13, 'middle', INK, True))
        o.append(T(cx, fy(w) - 10, f'ln Ω = {math.log(w):.3f}'.replace('0.000', '0'), 13, 'middle', MUT))
        o.append(T(cx, y1 + 20, str(n), 14, 'middle', INK, True))
    o.append(T((x0 + x1) / 2, y1 + 42, 'n = molecules in the left half', 14, fill=MUT))
    # two little boxes: all-left and even split
    def box(x, y, left):
        out = [R(x, y, 150, 60, PANEL, L2, 4), L(x + 75, y, x + 75, y + 60, L2, 1.5, '4 3')]
        for i, l in enumerate(left):
            px = x + 20 + (i % 2) * 28 + (0 if l else 75)
            py = y + 20 + (i // 2) * 22
            out.append(C(px, py, 7, AC))
        return ''.join(out)
    o.append(T(590, 52, 'n = 4: one way', 13, 'middle', INK, True)); o.append(box(515, 62, [1, 1, 1, 1]))
    o.append(T(590, 160, 'n = 2: six ways (one shown)', 13, 'middle', NX, True)); o.append(box(515, 170, [1, 0, 1, 0]))
    o.append(T(590, 262, 'whole box: 2⁴ = 16', 13, 'middle', INK, True))
    o.append(T(590, 282, 'S/k = ln 16 = 2.773', 13, 'middle', MUT))
    return 360, ''.join(o)
FIG[10] = (f10, 'The worked example: four labelled molecules in a box with two halves. The macrostate with n molecules on the left can be made in 1, 4, 6, 4 or 1 ways; the even split has the most microstates and so the largest entropy, S = k ln 6.',
           'A bar chart of the number of microstates for n = 0 to 4 molecules in the left half: 1, 4, 6, 4 and 1, with ln Ω above each bar, and two small boxes showing all four molecules on the left and an even split.')


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
