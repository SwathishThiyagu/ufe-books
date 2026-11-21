"""Claude's hand-drawn figures for ei-sensor-u5 (chemical, gas, humidity, MEMS, smart and biosensors), one per chapter.
Every number comes from that chapter's worked example. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
AFTER = {1: 0, 2: 0, 3: 1, 4: 2, 5: 0, 6: 1, 7: 1, 8: 2, 9: 1, 10: 1}


def sb(base, s, size=11):
    return f'{base}<tspan baseline-shift="sub" font-size="{size}">{s}</tspan>'


def res_v(x, ytop, ybot, c=INK, n=6, amp=7):
    ym1, ym2 = ytop + (ybot - ytop) * 0.25, ybot - (ybot - ytop) * 0.25
    pts = [(x, ytop), (x, ym1)]
    for i in range(n):
        pts.append((x + (amp if i % 2 == 0 else -amp), ym1 + (ym2 - ym1) * (i + 0.5) / n))
    pts += [(x, ym2), (x, ybot)]
    return P(pts, c, 1.8)


def res_d(x1, y1, x2, y2, c=INK, n=6, amp=7):
    """resistor zig-zag along any line"""
    dx, dy = x2 - x1, y2 - y1
    ln = math.hypot(dx, dy); ux, uy = dx / ln, dy / ln; nx, ny = -uy, ux
    pts = [(x1, y1), (x1 + dx * 0.25, y1 + dy * 0.25)]
    for i in range(n):
        t = 0.25 + 0.5 * (i + 0.5) / n; s = amp if i % 2 == 0 else -amp
        pts.append((x1 + dx * t + nx * s, y1 + dy * t + ny * s))
    pts += [(x1 + dx * 0.75, y1 + dy * 0.75), (x2, y2)]
    return P(pts, c, 1.8)


def dot(x, y, c=INK):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" style="fill:{c}"/>'


def arrow_r(x1, x2, y, c=AC):
    return L(x1, y, x2, y, c, 2, arrow='n' if c == AC else ('l' if c == LV else ('x' if c == NX else 'm')))


# ---- chemical sensors: the biosensor chain and the two-standard calibration ----
def f1():
    o = [T(20, 26, 'A biosensor is a chain: the biology recognises, the transducer measures', 15, 'start', bold=True)]
    xs = [20, 162, 304, 446, 588]
    boxes = [['Sample', 'glucose in', 'blood'], ['Bio element', 'glucose oxidase', 'makes H₂O₂'], ['Transducer', 'Pt electrode', 'at +0.6 V'],
             ['Conditioning', 'current to', 'voltage, ADC'], ['Display', 'C = (I − I₀)/S', '7.0 mmol/L']]
    fills = [PANEL, LVS, ACS, PANEL, NXS]; strokes = [L2, LV, AC, L2, NX]
    for x, b, f, s in zip(xs, boxes, fills, strokes):
        o.append(boxt(x, 44, 120, 76, b, f, s, 13, bold_first=True))
    for x in xs[:-1]:
        o.append(L(x + 122, 82, x + 140, 82, AC, 2, arrow='n'))
    o.append(T(222, 140, 'selectivity comes from here', 12, fill=LV))
    o.append(T(364, 140, 'signal comes from here', 12, fill=AC))
    # calibration chart
    x0, x1, y0, y1 = 110, 520, 180, 400
    fx = lambda c: x0 + (x1 - x0) * c / 12; fy = lambda i: y1 - (y1 - y0) * i / 200
    o.append(axes(x0, x1, y0, y1, [0, 2, 4, 6, 8, 10, 12], [0, 50, 100, 150, 200], fx, fy, 'glucose C (mmol/L)', 'current I (nA)'))
    o.append(L(fx(0), fy(15), fx(12), fy(15 + 15 * 12), AC, 2.5))
    o.append(C(fx(2), fy(45), 6, AC)); o.append(Tb(fx(2) + 12, fy(45) + 18, 'standard 1: 2.0, 45 nA', 12, 'start', AC))
    o.append(C(fx(10), fy(165), 6, AC)); o.append(Tb(fx(10) - 10, fy(165) - 12, 'standard 2: 10.0, 165 nA', 12, 'end', AC))
    o.append(L(fx(0), fy(120), fx(7), fy(120), LV, 1.6, '5 4')); o.append(L(fx(7), fy(120), fx(7), fy(0), LV, 1.6, '5 4'))
    o.append(C(fx(7), fy(120), 6, LV))
    o.append(Tb(fx(7) + 10, fy(120) + 22, 'sample 120 nA → 7.0', 13, 'start', LV, bold=True))
    o.append(Tb(fx(0) + 8, fy(15) - 8, 'I₀ = 15 nA', 12, 'start', MUT))
    o.append(T(548, 220, 'I = I₀ + S C', 14, 'start', bold=True))
    o.append(T(548, 246, 'S = 120 / 8.0', 13, 'start'))
    o.append(T(548, 266, '= 15 nA per mmol/L', 13, 'start'))
    o.append(T(548, 292, 'I₀ = 45 − 30 = 15 nA', 13, 'start'))
    o.append(T(548, 318, 'C = 105 / 15', 13, 'start'))
    o.append(T(548, 340, '= 7.0 mmol/L', 14, 'start', LV, bold=True))
    o.append(T(548, 362, '= 126 mg/dL', 13, 'start', LV))
    return 450, ''.join(o)
FIG[1] = (f1, 'Top: the glucose sensor as a chain, where glucose oxidase gives the selectivity and the platinum electrode gives the current. Below: two standards (2.0 mmol/L at 45 nA, 10.0 mmol/L at 165 nA) fix S = 15 nA per mmol/L and I₀ = 15 nA, so a 120 nA sample reads 7.0 mmol/L.',
          'Five blocks from sample through glucose oxidase, platinum electrode and conditioning to the display, and a straight calibration line of current against glucose through two standards, with a sample at 120 nanoamperes reading 7.0 millimoles per litre.')


# ---- gas sensors: the heated zirconia cell of the worked example ----
def f2():
    o = [T(20, 26, 'Zirconia oxygen cell in a flue at 700 °C (973 K)', 15, 'start', bold=True)]
    # reference air chamber | Pt | YSZ | Pt | flue gas
    o.append(R(40, 60, 170, 200, PANEL, L2, 6))
    o.append(T(125, 100, 'reference air', 14, bold=True)); o.append(T(125, 122, sb('p', '1') + ' = 20.9 % O₂', 14))
    o.append(R(214, 60, 12, 200, INK, INK, 1, 1))
    o.append(R(226, 60, 70, 200, ACS, AC, 2, 2))
    o.append(R(296, 60, 12, 200, INK, INK, 1, 1))
    o.append(T(261, 150, 'YSZ', 14, bold=True)); o.append(T(261, 170, 'ZrO₂ +', 12)); o.append(T(261, 186, 'Y₂O₃', 12))
    o.append(T(220, 280, 'porous Pt', 12, fill=MUT)); o.append(T(302, 280, 'porous Pt', 12, fill=MUT))
    o.append(R(312, 60, 170, 200, PANEL, L2, 6))
    o.append(T(397, 100, 'flue gas', 14, bold=True)); o.append(T(397, 122, sb('p', '2') + ' = 2.0 % O₂', 14))
    # ions
    for y in (206, 230):
        o.append(L(236, y, 288, y, LV, 2, arrow='l'))
    o.append(T(261, 252, 'O²⁻', 13, fill=LV, bold=True))
    o.append(T(125, 214, 'O₂ + 4e⁻ → 2O²⁻', 12, fill=LV))
    o.append(T(397, 214, '2O²⁻ → O₂ + 4e⁻', 12, fill=LV))
    # heater
    o.append(P([(40 + 10 * i, 300 + (6 if i % 2 else -6)) for i in range(45)], NX, 2))
    o.append(T(260, 326, 'heater keeps the cell above about 350 °C (here 700 °C)', 13, fill=NX))
    # meter
    o.append(L(220, 60, 220, 44, INK, 1.8)); o.append(L(220, 44, 620, 44, INK, 1.8))
    o.append(L(302, 60, 302, 52, INK, 1.8)); o.append(L(302, 52, 560, 52, INK, 1.8))
    o.append(L(560, 52, 560, 118, INK, 1.8)); o.append(L(620, 44, 620, 118, INK, 1.8))
    o.append(f'<circle cx="590" cy="150" r="34" style="fill:var(--panel);stroke:var(--accent);stroke-width:2"/>')
    o.append(L(560, 118, 570, 126, INK, 1.8)); o.append(L(620, 118, 610, 126, INK, 1.8))
    o.append(T(590, 147, 'E', 15, bold=True)); o.append(T(590, 165, '49.2 mV', 13, fill=LV, bold=True))
    o.append(T(632, 110, '+ reference', 12, 'start', AC)); o.append(T(548, 110, '−', 14, 'end', AC, bold=True))
    o.append(T(510, 222, 'RT/4F = 20.96 mV', 13, 'start'))
    o.append(T(510, 244, 'ln(20.9 / 2.0) = 2.347', 13, 'start'))
    o.append(T(510, 268, 'E = 20.96 × 2.347', 13, 'start'))
    o.append(T(510, 290, '= 49.2 mV', 14, 'start', LV, bold=True))
    return 345, ''.join(o)
FIG[2] = (f2, 'The cell at 973 K: oxygen is reduced to O²⁻ on the air side, the ions cross the hot zirconia and give up their electrons on the flue side. The EMF is (RT/4F) ln(20.9/2.0) = 20.96 mV × 2.347 = 49.2 mV, with the reference air electrode positive.',
          'Cross-section of a zirconia cell with reference air at 20.9 percent oxygen on the left, yttria-stabilised zirconia between two porous platinum electrodes, flue gas at 2.0 percent oxygen on the right, oxide ions crossing to the right, a heater below and a voltmeter reading 49.2 millivolts with the reference side positive.')


# ---- humidity: calibration line and the vapour pressure curve ----
def psat(t):
    return 0.6109 * math.exp(17.625 * t / (t + 243.04))


def f3():
    o = [T(20, 26, 'Left: capacitive sensor calibration. Right: RH and dew point from vapour pressure', 15, 'start', bold=True)]
    x0, x1, y0, y1 = 70, 300, 70, 300
    fx = lambda r: x0 + (x1 - x0) * r / 100; fy = lambda c: y1 - (y1 - y0) * (c - 80) / 100
    o.append(axes(x0, x1, y0, y1, [0, 20, 40, 60, 80, 100], [80, 100, 120, 140, 160, 180], fx, fy, 'RH (%)', 'C (pF)'))
    o.append(L(fx(0), fy(80), fx(100), fy(180), AC, 2.5))
    for r, cc in ((20, 100), (80, 160)):
        o.append(C(fx(r), fy(cc), 5, AC))
    o.append(L(fx(0), fy(145), fx(65), fy(145), LV, 1.5, '5 4')); o.append(L(fx(65), fy(145), fx(65), fy(80), LV, 1.5, '5 4'))
    o.append(C(fx(65), fy(145), 6, LV))
    o.append(Tb(fx(65) - 6, fy(145) - 12, '145 pF → 65 %', 13, 'end', LV, bold=True))
    o.append(Tb(fx(20) + 8, fy(100) + 20, '20 %, 100 pF', 12, 'start', AC))
    o.append(Tb(fx(80) - 6, fy(160) - 12, '80 %, 160 pF', 12, 'end', AC))
    o.append(T(185, 366, 'slope 1 pF per %RH, intercept 80 pF', 13, fill=MUT))
    # vapour pressure
    X0, X1, Y0, Y1 = 400, 700, 70, 300
    gx = lambda t: X0 + (X1 - X0) * (t - 10) / 30; gy = lambda p: Y1 - (Y1 - Y0) * p / 6
    o.append(axes(X0, X1, Y0, Y1, [10, 15, 20, 25, 30, 35, 40], [0, 2, 4, 6], gx, gy, 'temperature (°C)', 'pressure (kPa)'))
    o.append(P([(gx(10 + 0.5 * i), gy(psat(10 + 0.5 * i))) for i in range(61)], AC, 2.5))
    o.append(Tb(gx(30) - 4, gy(psat(30)) - 14, sb('p', 'sat') + ' (100 % RH)', 12, 'end', AC))
    o.append(L(gx(10), gy(1.90), gx(40), gy(1.90), LV, 2))
    o.append(Tb(gx(39.5), gy(1.90) + 18, sb('p', 'v') + ' = 1.90 kPa', 12, 'end', LV))
    for t, lab in ((25, '60.0 %'), (35, '33.8 %')):
        o.append(L(gx(t), gy(1.90), gx(t), gy(psat(t)), NX, 1.5, '4 3'))
        o.append(C(gx(t), gy(1.90), 5, NX)); o.append(C(gx(t), gy(psat(t)), 4, AC))
        o.append(Tb(gx(t) + 6, gy(1.90) - 30, lab, 13, 'start', NX, bold=True))
    o.append(C(gx(16.72), gy(1.90), 6, LV))
    o.append(L(gx(16.72), gy(1.90), gx(16.72), Y1, LV, 1.5, '5 4'))
    o.append(Tb(gx(16.72) + 4, Y1 - 12, 'dew point 16.7 °C', 12, 'start', LV, bold=True))
    o.append(T(550, 366, 'RH = 100 × ' + sb('p', 'v') + ' / ' + sb('p', 'sat') + '(T): 1.90 / 3.169 and 1.90 / 5.627', 13, fill=MUT))
    return 382, ''.join(o)
FIG[3] = (f3, 'Left: the sensor reads 100 pF at 20 % RH and 160 pF at 80 % RH, so 145 pF means 65 % RH. Right: the same 1.90 kPa of vapour is 60.0 % RH at 25 °C but 33.8 % at 35 °C, because the saturation curve rises; the line meets the curve at the dew point, 16.7 °C.',
          'Left, a straight calibration line of capacitance against relative humidity with the room reading of 145 picofarads at 65 percent. Right, the rising saturation vapour pressure curve against temperature, a flat line at 1.90 kilopascals, relative humidities of 60 percent at 25 degrees and 33.8 percent at 35 degrees, and the dew point at 16.7 degrees.')


# ---- semiconductor sensors: grain depletion and surface-to-volume ----
def grains(cx, cy, shell, lab, R_lab, c):
    o = []
    for i in range(3):
        x = cx - 92 + 92 * i
        o.append(f'<circle cx="{x:.1f}" cy="{cy:.1f}" r="44" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2"/>')
        o.append(f'<circle cx="{x:.1f}" cy="{cy:.1f}" r="{44 - shell:.1f}" style="fill:var(--panel);stroke:none"/>')
        for k in range(10):
            a = 2 * math.pi * k / 10
            if shell > 10 and (abs(math.cos(a)) < 0.7 or (i == 0 and math.cos(a) < 0) or (i == 2 and math.cos(a) > 0)):
                o.append(T(x + 52 * math.cos(a), cy + 52 * math.sin(a) + 4, 'O⁻', 10, fill=NX))
    o.append(T(cx, cy - 66, lab, 14, bold=True, fill=c))
    o.append(T(cx, cy + 78, R_lab, 13, fill=c))
    return ''.join(o)


def f4():
    o = [T(20, 26, 'SnO₂ grains: adsorbed oxygen empties a shell of each grain', 15, 'start', bold=True)]
    o.append(grains(180, 130, 18, 'clean air: thick depleted shell', 'narrow necks, R high (60 kΩ)', NX))
    o.append(grains(180, 300, 6, 'CO arrives: CO + O⁻ → CO₂ + e⁻', 'electrons return, R low (4 kΩ)', LV))
    o.append(T(180, 400, 'shaded ring = depleted shell; white core conducts', 12, fill=MUT))
    # cube scaling
    o.append(T(530, 70, 'Surface-to-volume ratio A/V = 6/a', 14, bold=True))
    o.append(R(420, 100, 90, 90, ACS, AC, 2, 2)); o.append(T(465, 210, 'a = 1 mm', 13))
    o.append(T(465, 230, '6 × 10³ m⁻¹', 13, fill=AC, bold=True))
    for i in range(6):
        for j in range(6):
            o.append(R(580 + 15 * i, 100 + 15 * j, 11, 11, LVS, LV, 1, 1))
    o.append(T(625, 210, 'a = 1 µm (not to scale)', 13))
    o.append(T(625, 230, '6 × 10⁶ m⁻¹', 13, fill=LV, bold=True))
    o.append(L(515, 145, 572, 145, AC, 2, arrow='n'))
    o.append(boxt(420, 262, 280, 100, ['1000 times the ratio', 'same total volume: 10⁹ small cubes', 'and 1000 times the surface'], PANEL, L2, 13, bold_first=True))
    return 415, ''.join(o)
FIG[4] = (f4, 'Left: in clean air adsorbed O⁻ ions trap electrons and leave a thick depleted shell on every grain, so the necks between grains conduct poorly; CO burns off the oxygen and gives the electrons back, so R falls from 60 kΩ to 4 kΩ (S = 15). Right: going from 1 mm to 1 µm raises A/V from 6 × 10³ to 6 × 10⁶ m⁻¹.',
          'Two rows of three tin dioxide grains, the top row in clean air with thick depleted shells and oxygen ions around them, the bottom row in carbon monoxide with thin shells; on the right one large cube of 1 millimetre beside a grid of small cubes, with surface-to-volume ratios of 6 thousand and 6 million per metre.')


# ---- MEMS: diaphragm cross-section and the bridge ----
def f5():
    o = [T(20, 26, 'Piezoresistive pressure sensor: diaphragm, gauges and full bridge', 15, 'start', bold=True)]
    # cross-section: rim blocks and diaphragm
    o.append(R(30, 120, 70, 120, PANEL, INK, 2, 2)); o.append(R(330, 120, 70, 120, PANEL, INK, 2, 2))
    o.append(R(100, 120, 230, 16, ACS, AC, 2, 2))
    o.append(T(215, 158, 'diaphragm 5 to 25 µm thick', 12, fill=AC))
    o.append(R(30, 240, 370, 18, PANEL, L2, 2, 2)); o.append(T(215, 254, 'glass base', 11, fill=MUT))
    o.append(T(215, 192, 'sealed vacuum', 13, fill=MUT)); o.append(T(215, 210, '(absolute sensor)', 12, fill=MUT))
    o.append(T(65, 184, 'Si rim', 12)); o.append(T(365, 184, 'Si rim', 12))
    for x in (180, 215, 250):
        o.append(L(x, 60, x, 112, NX, 2, arrow='x'))
    o.append(T(266, 74, 'P', 15, 'start', NX, bold=True))
    for x, c in ((108, LV), (126, NX), (304, NX), (322, LV)):
        o.append(R(x - 7, 121, 14, 6, c, c, 1, 1))
    o.append(T(30, 66, 'gauges sit at the', 12, 'start')); o.append(T(30, 82, 'clamped edges', 12, 'start')); o.append(L(70, 88, 106, 116, MUT, 1.2, arrow='m'))
    o.append(T(215, 288, 'strain ε = 2 × 10⁻⁴, G = 120', 13, bold=True))
    o.append(T(215, 308, 'ΔR/R = G ε = 0.024, ΔR = 120 Ω on 5 kΩ', 13))
    # bridge diamond
    cx, cy, r = 570, 175, 95
    top, rt, bot, lf = (cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)
    o.append(res_d(*lf, *top, LV)); o.append(res_d(*top, *rt, NX)); o.append(res_d(*rt, *bot, LV)); o.append(res_d(*bot, *lf, NX))
    o.append(Tb(cx - 72, cy - 64, 'R + ΔR', 12, 'middle', LV)); o.append(Tb(cx + 72, cy - 64, 'R − ΔR', 12, 'middle', NX))
    o.append(Tb(cx + 72, cy + 70, 'R + ΔR', 12, 'middle', LV)); o.append(Tb(cx - 72, cy + 70, 'R − ΔR', 12, 'middle', NX))
    for p in (top, rt, bot, lf): o.append(dot(*p))
    o.append(L(cx, cy - r, cx, cy - r - 24, INK, 1.8)); o.append(T(cx, cy - r - 30, sb('V', 's') + ' = 5 V', 13, bold=True))
    o.append(L(cx, cy + r, cx, cy + r + 18, INK, 1.8)); o.append(T(cx, cy + r + 34, '0 V', 13))
    o.append(L(lf[0], cy, lf[0] + 30, cy, AC, 1.5, '4 3')); o.append(L(rt[0], cy, rt[0] - 30, cy, AC, 1.5, '4 3'))
    o.append(Tb(cx, cy + 5, sb('V', 'o'), 14, 'middle', AC, True))
    o.append(boxt(440, 330, 260, 60, ['four active: 5 × 0.024 = 120 mV', 'one active: 5 × 0.024 / 4 = 30 mV'], LVS, LV, 13))
    return 400, ''.join(o)
FIG[5] = (f5, 'Pressure bends the diaphragm; the four implanted gauges sit at its clamped edges, two rising and two falling in resistance. Wired as a full bridge on 5 V, a relative change of 0.024 gives 120 mV; a single active gauge would give only a quarter, 30 mV.',
          'Cross-section of a silicon die with a thin diaphragm between two thick rims over a sealed vacuum cavity, pressure arrows pushing down, four small gauges at the edges, and a Wheatstone bridge diamond with two arms rising and two falling, supplied at 5 volts, with outputs of 120 millivolts for four active gauges and 30 millivolts for one.')


# ---- micro-fabrication: the KOH pit of the second worked example ----
def f6():
    o = [T(20, 26, 'KOH etch from the back of a 525 µm (100) wafer (vertical scale stretched)', 15, 'start', bold=True)]
    s = 0.25  # px per µm horizontally
    xl, xr = 140, 140 + 1714 * s
    ytop, ybot = 300, 110   # back face at bottom (y=300), front face at top (y=110)
    run = 357.1 * s
    o.append(f'<polygon points="40,{ybot} 680,{ybot} 680,{ytop} {xr:.1f},{ytop} {xr - run:.1f},{ybot + 22} {xl + run:.1f},{ybot + 22} {xl:.1f},{ytop} 40,{ytop}" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2"/>')
    o.append(R(40, ytop, xl - 40, 10, NX, NX, 1, 1)); o.append(R(xr, ytop, 680 - xr, 10, NX, NX, 1, 1))
    o.append(T(80, ytop + 30, 'nitride mask', 12, fill=NX))
    o.append(T(95, 160, 'silicon', 13, fill=AC))
    # diaphragm
    o.append(Tb((xl + xr) / 2, ybot + 14, 'diaphragm 1000 µm wide, 20 µm thick', 12, 'middle', LV, True))
    # wall angle
    o.append(arc(xl + 40, ytop, xl + 40 * math.cos(math.radians(54.74)) + 0.5, ytop - 40 * math.sin(math.radians(54.74)), 0.25, INK, 1.5, None))
    o.append(T(xl + 46, ytop - 12, '54.74°', 12, 'start'))
    o.append(T(xl + run + 4, 190, '(111) wall', 12, 'start', fill=MUT))
    # dimensions
    o.append(L(xl, ytop + 46, xr, ytop + 46, INK, 1.5)); o.append(L(xl, ytop + 38, xl, ytop + 54, INK, 1.5)); o.append(L(xr, ytop + 38, xr, ytop + 54, INK, 1.5))
    o.append(Tb((xl + xr) / 2, ytop + 51, 'mask opening 1000 + 2 × 357 = 1714 µm', 13, 'middle', NX, True))
    o.append(L(xl, ytop + 70, xl + run, ytop + 70, MUT, 1.2)); o.append(T(xl + run / 2, ytop + 86, '357 µm', 12, fill=MUT))
    o.append(L(xr - run, ytop + 70, xr, ytop + 70, MUT, 1.2)); o.append(T(xr - run / 2, ytop + 86, '357 µm', 12, fill=MUT))
    o.append(L(30, ybot, 30, ytop, INK, 1.5)); o.append(Tb(64, (ybot + ytop) / 2, '525 µm', 12))
    o.append(L(xr + 8, ybot + 22, xr + 30, ybot + 22, MUT, 1)); o.append(L(xr + 22, ybot + 22, xr + 22, ytop, MUT, 1.2))
    o.append(T(xr + 30, 230, 'etch 505 µm', 13, 'start', bold=True)); o.append(T(xr + 30, 250, '505 / 1.4 =', 12, 'start')); o.append(T(xr + 30, 268, '361 min', 13, 'start', LV, bold=True))
    o.append(T(220, 70, 'front face (gauges go here)', 12, fill=MUT)); o.append(L(220, 76, 220, ybot - 4, MUT, 1.2, arrow='m'))
    return 400, ''.join(o)
FIG[6] = (f6, 'The back-side KOH etch stops on the 54.74° (111) planes, so the 505 µm deep pit grows outward by 357 µm on each side between the diaphragm and the mask. A 1000 µm diaphragm therefore needs a 1714 µm mask opening and about 361 min at 1.4 µm/min.',
          'Cross-section of a silicon wafer 525 micrometres thick with a trapezoidal pit etched from the back, sloping walls at 54.74 degrees, a 20 micrometre diaphragm 1000 micrometres wide at the front, and a mask opening of 1714 micrometres at the back.')


# ---- smart sensors: the chain and its numbers ----
def f7():
    o = [T(20, 26, 'Smart sensor chain with the numbers of both worked examples', 15, 'start', bold=True)]
    xs = [16, 156, 296, 436, 586]; w = 122
    boxes = [['Element', '10 mV/kPa'], ['Amplifier', 'gain 100'], ['12-bit ADC', '3.3 V ref'], ['µC + memory', 'offset, gain, temp'], ['Bus', 'I²C, SPI, CAN']]
    fills = [ACS, PANEL, PANEL, LVS, NXS]; st = [AC, L2, L2, LV, NX]
    for x, b, f, s_ in zip(xs, boxes, fills, st):
        o.append(boxt(x, 50, w if x != 586 else 118, 70, b, f, s_, 13, bold_first=True))
    for x in xs[:-1]:
        o.append(L(x + w + 2, 85, (xs[xs.index(x) + 1]) - 2, 85, AC, 2, arrow='n'))
    o.append(T(77, 146, '0.806 Pa', 13, fill=LV, bold=True)); o.append(T(217, 146, '8.06 µV', 13, fill=LV, bold=True)); o.append(T(357, 146, '0.806 mV', 13, fill=LV, bold=True))
    o.append(T(217, 166, 'one ADC step, referred back to each point', 12, fill=MUT))
    o.append(L(52, 154, 382, 154, LV, 1, '3 3'))
    o.append(R(436, 140, 268, 22, PANEL, L2, 4)); o.append(T(570, 156, 'TEDS: identity, range, coefficients', 12))
    # correction steps of example 2
    o.append(T(20, 206, 'Blood-pressure module, 1492 counts at 37 °C:', 14, 'start', bold=True))
    rows = [('offset', '1492 − 12 = 1480 counts'), ('gain', '1480 / 92.5 = 16.0 kPa'), ('temperature', '16.0 / 0.976 = 16.39 kPa'), ('output', '16.39 × 7.50 = 123 mmHg')]
    for i, (a, b) in enumerate(rows):
        y = 226 + 46 * i
        o.append(boxt(40, y, 150, 34, [a], LVS if i == 3 else PANEL, LV if i == 3 else L2, 13, True))
        o.append(T(210, y + 22, b, 14, 'start', LV if i == 3 else INK, bold=(i == 3)))
        if i < 3: o.append(L(115, y + 35, 115, y + 45, AC, 2, arrow='n'))
    o.append(boxt(470, 236, 230, 110, ['without the temperature step:', '16.0 kPa = 120 mmHg', '3 mmHg low'], NXS, NX, 13, True))
    return 420, ''.join(o)
FIG[7] = (f7, 'Top: one step of the 12-bit ADC is 0.806 mV at the converter, 8.06 µV at the sensing element and 0.806 Pa of pressure. Below: the processor removes the 12-count offset, divides by 92.5 counts per kPa and corrects the 2.4 % temperature loss, so 1492 counts become 123 mmHg instead of 120.',
          'Five blocks from sensing element through amplifier, analogue-to-digital converter and microcontroller with memory to a digital bus, with one converter step shown as 0.806 pascal, 8.06 microvolts and 0.806 millivolts; below, four correction steps turning 1492 counts into 123 millimetres of mercury.')


# ---- data fusion: three distributions on one axis ----
def f8():
    o = [T(20, 26, 'Inverse-variance fusion of two temperature sensors', 15, 'start', bold=True)]
    x0, x1, y1 = 60, 680, 330
    fx = lambda t: x0 + (x1 - x0) * (t - 28.5) / 3.0
    o.append(xaxis(x0, x1, y1, [28.5, 29.0, 29.5, 30.0, 30.5, 31.0, 31.5], fx, 'temperature (°C)', lambda v: f'{v:.1f}'))
    def gauss(mu, s, c, k):
        pk = 230 * 0.186 / s
        pts = [(fx(mu + s * (-4 + 8 * i / 120)), y1 - pk * math.exp(-0.5 * (-4 + 8 * i / 120) ** 2)) for i in range(121)]
        pts = [(x, y) for x, y in pts if x0 <= x <= x1]
        return P(pts, c, 2.5)
    o.append(gauss(30.0, 0.5, NX, 1)); o.append(gauss(30.8, 0.2, AC, 2)); o.append(gauss(30.69, 0.186, LV, 3))
    o.append(L(fx(30.0), y1, fx(30.0), y1 - 230 * 0.186 / 0.5, NX, 1.2, '4 3'))
    o.append(L(fx(30.8), y1, fx(30.8), y1 - 230 * 0.186 / 0.2, AC, 1.2, '4 3'))
    o.append(L(fx(30.69), y1, fx(30.69), 90, LV, 1.5, '4 3'))
    o.append(Tb(fx(30.0) - 10, y1 - 96, 'sensor 1: 30.0 °C, σ = 0.5', 13, 'end', NX, True))
    o.append(Tb(fx(30.0) - 10, y1 - 76, 'weight 1/0.5² = 4', 12, 'end', NX))
    o.append(Tb(700, 64, 'sensor 2: 30.8 °C, σ = 0.2', 13, 'end', AC, True))
    o.append(Tb(700, 84, 'weight 1/0.2² = 25', 12, 'end', AC))
    o.append(Tb(fx(30.69) - 30, 84, 'fused: 30.69 °C, σ = 0.186', 13, 'end', LV, True))
    o.append(T(60, 70, '(4 × 30.0 + 25 × 30.8) / 29', 13, 'start'))
    o.append(T(60, 90, '= 890 / 29 = 30.69 °C', 13, 'start', LV, bold=True))
    o.append(T(60, 112, 'σ = 1 / √29 = 0.186 °C', 13, 'start'))
    return 380, ''.join(o)
FIG[8] = (f8, 'Sensor 2 has the narrower spread, so its weight is 25 against 4 and the fused value, 30.69 °C, lands close to its reading rather than halfway. The fused spread, σ = 0.186 °C, is narrower than either sensor alone.',
          'Three bell curves on a temperature axis: a wide one centred at 30.0 degrees for sensor 1, a narrow one at 30.8 degrees for sensor 2, and the narrowest one at 30.69 degrees for the fused estimate.')


# ---- SAW delay line and mixer ----
def idt(x, y, n=5, c=AC):
    o = [R(x, y - 6, 80, 8, c, c, 1, 1), R(x, y + 62, 80, 8, c, c, 1, 1)]
    for i in range(n):
        o.append(R(x + 4 + 16 * i, y, 5, 52, c, c, 1, 1))
        o.append(R(x + 12 + 16 * i, y + 10, 5, 52, NX, NX, 1, 1))
    return ''.join(o)


def f9():
    o = [T(20, 26, 'SAW delay line at 100 MHz on quartz, read through a mixer', 15, 'start', bold=True)]
    o.append(R(30, 60, 640, 120, PANEL, L2, 6)); o.append(T(350, 168, 'piezoelectric quartz substrate', 12, fill=MUT))
    o.append(idt(60, 84)); o.append(idt(520, 84))
    o.append(T(100, 54, 'input IDT', 13, bold=True)); o.append(T(560, 54, 'output IDT', 13, bold=True))
    o.append(R(220, 90, 220, 54, LVS, LV, 4, 2, '5 3')); o.append(T(330, 112, 'sensing film', 13, fill=LV, bold=True)); o.append(T(330, 132, '7.4 µg/cm²', 12, fill=LV))
    for x in (160, 470):
        o.append(P([(x + 4 * i, 117 + 8 * math.sin(i)) for i in range(12)], AC, 2))
    o.append(L(150, 196, 510, 196, AC, 2, arrow='n')); o.append(T(330, 214, 'surface wave slows by 0.10 %', 13, fill=AC))
    o.append(T(114, 174, 'finger pitch λ/2', 11, 'start', MUT))
    # electronics
    o.append(boxt(30, 260, 150, 56, ['RF source', '100 MHz'], PANEL, AC, 13, True))
    o.append(L(105, 260, 105, 156, INK, 1.8))
    o.append(boxt(520, 260, 150, 56, ['Mixer', 'difference out'], PANEL, AC, 13, True))
    o.append(L(595, 180, 595, 258, INK, 1.8, arrow='m'))
    o.append(boxt(300, 260, 160, 56, ['Reference', '100 MHz'], PANEL, L2, 13, True))
    o.append(L(462, 288, 518, 288, INK, 1.8, arrow='m'))
    o.append(L(595, 318, 595, 346, LV, 2, arrow='l'))
    o.append(T(595, 368, 'Δf = 0.0010 × 100 MHz = 100 kHz', 14, 'end', LV, True))
    o.append(T(30, 368, 'mass check: 13.5 Hz per ng/cm² × 7400 = 99.9 kHz', 13, 'start'))
    return 385, ''.join(o)
FIG[9] = (f9, 'The input IDT launches the wave, the film on the path slows it by 0.10 % and the output IDT turns it back into a voltage. Mixing with a 100 MHz reference leaves the 100 kHz difference, which matches the 99.9 kHz expected from a 7.4 µg/cm² film.',
          'A quartz substrate with two interdigital comb transducers, a sensing film on the path between them, a 100 megahertz source feeding the input, and the output mixed with a 100 megahertz reference to give a 100 kilohertz difference.')


# ---- ISFET cross-section and threshold against pH ----
def f10():
    o = [T(20, 26, 'ISFET: the electrolyte is the gate, the reference electrode sets its potential', 15, 'start', bold=True)]
    # substrate
    o.append(R(30, 250, 360, 110, PANEL, L2, 4)); o.append(T(210, 345, 'p-type silicon', 13, fill=MUT))
    o.append(R(50, 250, 90, 36, ACS, AC, 4)); o.append(T(95, 274, 'n⁺ source', 12))
    o.append(R(280, 250, 90, 36, ACS, AC, 4)); o.append(T(325, 274, 'n⁺ drain', 12))
    o.append(L(140, 296, 280, 296, AC, 2.5, '6 3')); o.append(T(210, 314, 'channel', 12, fill=AC))
    o.append(R(120, 238, 180, 12, NX, NX, 1, 1)); o.append(T(210, 232, 'Si₃N₄ / SiO₂ gate insulator', 11, fill=NX))
    # electrolyte well
    o.append(R(110, 120, 200, 104, LVS, LV, 4, 2)); o.append(T(160, 214, 'blood sample', 12, 'start', LV))
    o.append(R(200, 70, 22, 110, PANEL, INK, 6, 2)); o.append(T(232, 84, 'Ag/AgCl reference', 12, 'start'))
    o.append(T(232, 100, 'electrode', 12, 'start'))
    # wiring
    o.append(L(211, 70, 211, 50, INK, 1.8)); o.append(L(211, 50, 30, 50, INK, 1.8)); o.append(L(30, 50, 30, 268, INK, 1.8)); o.append(L(30, 268, 50, 268, INK, 1.8))
    o.append(T(36, 140, sb('V', 'GS'), 13, 'start', bold=True))
    o.append(L(325, 250, 325, 230, INK, 1.5)); o.append(L(325, 230, 380, 230, INK, 1.5)); o.append(T(384, 234, sb('V', 'DS'), 13, 'start', bold=True))
    # threshold vs pH
    X0, X1, Y0, Y1 = 470, 690, 70, 300
    gx = lambda p: X0 + (X1 - X0) * (p - 6.8) / 1.0; gy = lambda v: Y1 - (Y1 - Y0) * v / 60
    o.append(axes(X0, X1, Y0, Y1, [6.8, 7.0, 7.2, 7.4, 7.6, 7.8], [0, 20, 40, 60], gx, gy, 'pH', 'ΔV_T (mV)'.replace('V_T', 'V<tspan baseline-shift="sub" font-size="10">T</tspan>'), lambda v: f'{v:.1f}'))
    v = lambda p: 55.4 * (p - 6.8)
    o.append(L(gx(6.8), gy(0), gx(7.8), gy(55.4), AC, 2.5))
    o.append(C(gx(7.3), gy(v(7.3)), 5, LV)); o.append(C(gx(7.4), gy(v(7.4)), 5, LV))
    o.append(Tb(gx(7.3) - 6, gy(v(7.3)) - 12, '7.30', 12, 'end', LV, True)); o.append(Tb(gx(7.4) + 8, gy(v(7.4)) + 20, '7.40', 12, 'start', LV, True))
    o.append(T(580, 372, 'slope 55.4 mV/pH at 37 °C', 13, fill=AC, bold=True))
    o.append(T(580, 392, '0.10 pH fall → threshold −5.54 mV', 13, fill=LV))
    return 405, ''.join(o)
FIG[10] = (f10, 'Left: the blood sample and a Ag/AgCl reference electrode take the place of the metal gate. Right: at 37 °C the device shifts 55.4 mV per pH, so a fall from pH 7.40 to 7.30 lowers the threshold by 5.54 mV.',
          'Cross-section of an n-channel ISFET with source, drain and channel in p-type silicon, a nitride gate insulator under a well of blood, a silver chloride reference electrode in the blood setting the gate voltage, and a straight line of threshold shift against pH of slope 55.4 millivolts per pH with points at 7.30 and 7.40.')


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'caption': cap, 'after_section': AFTER[k], 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
