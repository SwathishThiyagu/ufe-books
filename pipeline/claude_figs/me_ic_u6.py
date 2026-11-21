"""Claude's hand-drawn figures for me-ic-u6 (Internal Combustion Engines: emissions, alternative fuels and advanced combustion),
one per chapter, drawn from each chapter's own worked example and numbers. Curves that are trends (emission against air-fuel
ratio, the φ–T map) are marked as sketches; the NEDC speed trace is the published profile (its distance is checked to
11.0 km in the correction notes); storage energies are computed (CoolProp densities for CNG and hydrogen).
Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


def sub(a, b, size=11):
    """a with subscript b, as svg text content"""
    return f'{a}<tspan baseline-shift="sub" font-size="{size}">{b}</tspan>'


def smooth(fn, a, b, n=60):
    return [(a + (b - a) * i / n, fn(a + (b - a) * i / n)) for i in range(n + 1)]


# ---- 6.1 engine-out CO, HC and NO against air-fuel ratio (sketch of the standard trends) ----
def f1():
    o = []
    x0, x1, y0, y1 = 80, 690, 50, 330
    fx = lin(10, 20, x0, x1); fy = lin(0, 1, y1, y0)
    o.append(axes(x0, x1, y0, y1, [10, 12, 14, 16, 18, 20], [], fx, fy, 'air–fuel ratio (petrol)', 'relative level (sketch)'))
    # catalyst window and the two marked mixtures
    o.append(R(fx(14.6), y0, fx(14.8) - fx(14.6), y1 - y0, ACS, ACS, 0, 0))
    o.append(L(fx(14.7), y0, fx(14.7), y1, AC, 1.5, dash='5 4'))
    o.append(L(fx(16.33), y0 + 20, fx(16.33), y1, NX, 1.5, dash='5 4'))
    co = lambda a: 0.02 + 0.98 / (1 + math.exp((a - 12.6) * 1.5))
    hc = lambda a: 0.10 + 0.55 / (1 + math.exp((a - 12.8) * 1.2)) + 0.30 / (1 + math.exp(-(a - 19.0) * 2.2))
    no = lambda a: 0.03 + 0.94 * math.exp(-((a - 16.33) / (1.55 if a < 16.33 else 1.9)) ** 2)
    o.append(P([(fx(a), fy(co(a))) for a, _ in smooth(lambda a: 0, 10, 20)], AC, 3))
    o.append(P([(fx(a), fy(hc(a))) for a, _ in smooth(lambda a: 0, 10, 20)], LV, 3, dash='8 5'))
    o.append(P([(fx(a), fy(no(a))) for a, _ in smooth(lambda a: 0, 10, 20)], NX, 3))
    o.append(Tb(fx(10.9), fy(0.93), 'CO', 14, 'start', AC, bold=True))
    o.append(Tb(fx(10.4), fy(0.50), 'HC', 14, 'start', LV, bold=True))
    o.append(Tb(fx(19.3), fy(0.47), 'HC (misfire)', 13, 'middle', LV))
    o.append(Tb(fx(17.6), fy(0.62), 'NO', 14, 'start', NX, bold=True))
    o.append(Tb(fx(14.6) - 6, y0 + 14, 'λ = 1 (14.7)', 13, 'end', AC, bold=True))
    o.append(Tb(fx(16.33) + 4, y0 + 10, 'φ = 0.9, 16.3: NO peak', 13, 'start', NX, bold=True))
    o.append(Tb(fx(14.7), y1 - 14, 'catalyst window', 13, 'middle', AC))
    o.append(T(fx(11.0), y1 + 58, '← rich (φ > 1)', 13, 'start', MUT))
    o.append(T(fx(19.6), y1 + 58, 'lean (φ < 1) →', 13, 'end', MUT))
    return 400, ''.join(o)


FIG[1] = (f1, 'A sketch of the standard trends. CO and HC are high on the rich side and fall as the mixture leans out; NO peaks near φ = 0.9 '
              '(air–fuel ratio 16.3), the worked example’s mixture, and HC climbs again when a very lean charge misfires. The shaded '
              'band near 14.7 is where a three-way catalyst converts all three gases.',
          'Engine-out CO, HC and NO against air-fuel ratio from 10 to 20. CO falls steeply from the rich side, HC falls and rises again '
          'beyond 18 where misfire starts, NO peaks at 16.3, which is equivalence ratio 0.9. A narrow band at 14.7 marks the catalyst window.')


# ---- 6.2 soot growth steps, and the partial-flow dilution sample of the worked example ----
def f2():
    o = []
    steps = [('pyrolysis', 'C₂H₂, PAH'), ('nucleation', '≈ 1–2 nm'), ('surface', 'growth'), ('coagulation', '10–30 nm'),
             ('agglomeration', 'chains'), ('oxidation', 'burn-out')]
    w, gap, x = 106, 9, 14
    o.append(T(14, 26, 'Inside the rich spray core (φ > 2), then the oxidation zone', 14, 'start', bold=True))
    for i, (a, b) in enumerate(steps):
        X = x + i * (w + gap)
        st = NX if i == 5 else AC
        o.append(boxt(X, 40, w, 52, [a, b], NXS if i == 5 else PANEL, st, 13, bold_first=True))
        if i < 5: o.append(L(X + w + 1, 66, X + w + gap - 1, 66, L2, 2, arrow='m'))
    # dilution sample
    y = 160
    o.append(T(14, y - 14, 'Measuring PM: a partial-flow dilution sample (worked example)', 14, 'start', bold=True))
    o.append(R(14, y + 20, 200, 34, PANEL, L2, 6))
    o.append(T(114, y + 42, 'exhaust pipe 0.05 m³/s', 13))
    o.append(L(114, y + 54, 114, y + 92, AC, 2, arrow='n'))
    o.append(T(122, y + 78, 'probe', 13, 'start', MUT))
    o.append(R(40, y + 96, 360, 44, ACS, AC, 8))
    o.append(T(220, y + 123, 'dilution tunnel: 1 part exhaust + 7 parts air', 13))
    o.append(boxt(420, y + 18, 150, 48, ['filtered air', '(dilution ratio 8)'], PANEL, LV, 13))
    o.append(L(495, y + 66, 400, y + 104, LV, 2, arrow='l'))
    o.append(L(400, y + 118, 470, y + 118, AC, 2, arrow='n'))
    o.append(R(472, y + 92, 120, 52, NXS, NX, 6))
    o.append(T(532, y + 114, 'filter, 47 °C', 13, bold=True)); o.append(T(532, y + 132, '+0.90 mg', 13))
    o.append(L(592, y + 118, 620, y + 118, AC, 2, arrow='n'))
    o.append(boxt(622, y + 92, 86, 52, ['gas meter', '0.30 m³'], PANEL, L2, 13))
    o.append(Tb(360, y + 182, '0.90 mg ÷ 0.30 m³ = 3.0 mg/m³ diluted × 8 = 24 mg/m³ raw', 14, 'middle', INK, bold=True))
    o.append(T(360, y + 206, '24 mg/m³ × 0.05 m³/s = 1.2 mg/s  →  4.32 g/h ÷ 40 kW = 0.108 g/kWh', 14, 'middle', MUT))
    return 384, ''.join(o)


FIG[2] = (f2, 'Top: the six steps from fuel in the rich core to the particle that leaves; the last step, oxidation, burns most of the soot '
              'formed. Bottom: the worked example’s sample. The filter sees exhaust diluted eight times, so its concentration is multiplied '
              'by 8 before it is applied to the whole exhaust flow.',
          'Six boxes in a row: pyrolysis, nucleation, surface growth, coagulation, agglomeration, oxidation. Below, a dilution system: '
          'exhaust at 0.05 cubic metres per second, a probe, a tunnel with seven parts filtered air, a 47 degree filter gaining 0.90 '
          'milligrams and a gas meter reading 0.30 cubic metres, giving 24 milligrams per cubic metre raw and 0.108 grams per kilowatt hour.')


# ---- 6.3 EGR loop with the CO2 readings, and the diesel after-treatment line with the SCR numbers ----
def f3():
    o = []
    o.append(boxt(270, 40, 150, 70, ['diesel engine', '200 kW'], PANEL, AC, 14, bold_first=True))
    # intake
    o.append(L(30, 75, 268, 75, LV, 2.5, arrow='l'))
    o.append(Tb(60, 66, 'fresh air: CO₂ 0.04 %', 13, 'start', LV))
    o.append(C(240, 75, 6, LV)); o.append(Tb(236, 100, 'intake: CO₂ 1.80 %', 13, 'end', LV, bold=True))
    # exhaust out and EGR loop
    o.append(L(420, 75, 700, 75, AC, 2.5, arrow='n'))
    o.append(C(450, 75, 6, AC)); o.append(Tb(456, 100, 'exhaust: CO₂ 12.0 %', 13, 'start', AC, bold=True))
    o.append(P([(470, 75), (470, 150), (240, 150), (240, 84)], NX, 2.5))
    o.append(L(240, 112, 240, 86, NX, 2.5, arrow='x'))
    o.append(R(318, 136, 74, 28, NXS, NX, 6)); o.append(T(355, 155, 'cooler', 13))
    o.append(Tb(355, 182, 'EGR = (1.80 − 0.04) ÷ (12.0 − 0.04) = 14.7 % of the intake charge', 13, 'middle', NX, bold=True))
    # after-treatment line
    y = 228
    o.append(T(14, y, 'Lean diesel exhaust, in order', 14, 'start', bold=True))
    boxes = [('DOC', ['CO, HC → CO₂, H₂O', 'NO → NO₂']), ('DPF', ['traps soot', 'regenerates']),
             ('urea', ['AdBlue 32.5 %', '2.17 kg/h']), ('SCR', ['NOx + NH₃ → N₂', '6 → 0.6 g/kWh']), ('ASC', ['oxidises', 'NH₃ slip'])]
    w, gap = 126, 16
    for i, (h, ls) in enumerate(boxes):
        X = 14 + i * (w + gap)
        fill, st = (NXS, NX) if h == 'urea' else ((LVS, LV) if h == 'SCR' else (PANEL, AC))
        o.append(R(X, y + 16, w, 82, fill, st, 8))
        o.append(T(X + w / 2, y + 40, h, 15, bold=True))
        o.append(T(X + w / 2, y + 62, ls[0], 13)); o.append(T(X + w / 2, y + 82, ls[1], 13))
        if i < 4: o.append(L(X + w + 1, y + 57, X + w + gap - 1, y + 57, AC, 2, arrow='n'))
    o.append(T(360, y + 126, 'engine-out NOx 6 g/kWh; SCR removes 90 %; tailpipe 0.6 g/kWh', 13, 'middle', MUT))
    return 368, ''.join(o)


FIG[3] = (f3, 'Top: the worked example’s EGR loop. Exhaust taken before the turbine is cooled and mixed into the fresh air, so the intake CO₂ '
              'rises from 0.04 to 1.80 % and the charge is 14.7 % exhaust. Bottom: the after-treatment order on a lean diesel, with the '
              'second example’s SCR duty and its urea flow.',
          'An engine with fresh air entering at 0.04 percent CO2, an EGR loop with a cooler from the exhaust at 12.0 percent back to the '
          'intake at 1.80 percent, giving 14.7 percent EGR. Below, five boxes in order: DOC, DPF, urea dosing at 2.17 kilograms per hour, '
          'SCR from 6 to 0.6 grams per kilowatt hour, and an ammonia slip catalyst.')


# ---- 6.4 the exhaust bench of the worked example ----
def f4():
    o = []
    o.append(boxt(14, 30, 170, 56, ['probe in the', 'exhaust pipe'], ACS, AC, 13, bold_first=True))
    o.append(L(184, 58, 230, 58, AC, 2, arrow='n'))
    o.append(boxt(232, 30, 200, 56, ['heated line 190 °C', 'and soot filter'], PANEL, AC, 13, bold_first=True))
    o.append(L(99, 86, 99, 278, MUT, 2, arrow='m'))
    o.append(Tb(105, 180, 'raw', 13, 'start', MUT))
    o.append(boxt(14, 280, 170, 66, ['smoke meter', 'opacity or Bosch', 'raw, unfiltered'], PANEL, MUT, 13, bold_first=True))
    # hot branch
    o.append(L(432, 58, 520, 58, AC, 2, arrow='n'))
    o.append(boxt(522, 30, 186, 56, ['heated FID', 'HC as ppmC, wet'], LVS, LV, 13, bold_first=True))
    # cooler branch
    o.append(L(332, 86, 332, 120, AC, 2, arrow='n'))
    o.append(boxt(232, 122, 200, 50, ['cooler / water trap', 'dry sample'], PANEL, AC, 13, bold_first=True))
    o.append(L(282, 172, 282, 200, AC, 2, arrow='n')); o.append(L(382, 172, 382, 200, AC, 2, arrow='n'))
    o.append(boxt(214, 202, 128, 56, ['NDIR', 'CO, CO₂'], LVS, LV, 13, bold_first=True))
    o.append(boxt(352, 202, 128, 56, ['paramagnetic', 'O₂'], LVS, LV, 13, bold_first=True))
    o.append(L(432, 147, 520, 147, AC, 2, arrow='n'))
    # CLD with converter
    o.append(R(522, 112, 186, 234, PANEL, NX, 8))
    o.append(T(615, 134, 'CLD for NOx', 14, bold=True))
    o.append(boxt(536, 150, 158, 44, ['NO₂ → NO converter', 'η = 0.92'], NXS, NX, 13))
    o.append(T(615, 222, 'bypass: NO = 380 ppm', 13))
    o.append(T(615, 244, 'in line: 420 ppm', 13))
    o.append(T(615, 270, 'NO₂ = 40 ÷ 0.92', 13, bold=True, fill=NX))
    o.append(T(615, 290, '= 43.5 ppm', 13, bold=True, fill=NX))
    o.append(T(615, 318, 'true NOx 423.5 ppm', 13, bold=True))
    o.append(T(346, 300, 'every channel logs', 13, 'middle', MUT))
    o.append(T(346, 318, 'to one data system', 13, 'middle', MUT))
    return 360, ''.join(o)


FIG[4] = (f4, 'The bench of the worked example. The smoke meter takes raw exhaust because soot is what it measures; the FID takes the hot, '
              'wet sample; NDIR and the oxygen cell take dried gas. The CLD reads 380 ppm with its converter bypassed and 420 ppm through it, '
              'and the converter efficiency of 0.92 turns the 40 ppm difference into 43.5 ppm of NO₂.',
          'Exhaust bench: a probe feeds a raw smoke meter and a heated line at 190 degrees with a soot filter. The heated line feeds a heated '
          'FID for hydrocarbons and a cooler; the dry sample feeds NDIR for CO and CO2, a paramagnetic oxygen cell and a chemiluminescence '
          'detector whose converter has efficiency 0.92, reading 380 parts per million bypassed and 420 in line, so true NOx is 423.5.')


# ---- 6.5 the NEDC trace (base of India's MIDC for cars) ----
ECE = [(0, 0), (11, 0), (15, 15), (23, 15), (25, 10), (28, 0), (49, 0), (54, 15), (56, 15), (61, 32), (85, 32), (93, 10), (96, 0),
       (117, 0), (122, 15), (124, 15), (133, 35), (135, 35), (143, 50), (155, 50), (163, 35), (176, 35), (178, 35), (185, 10), (188, 0), (195, 0)]
EUDC = [(0, 0), (20, 0), (25, 15), (27, 15), (36, 35), (38, 35), (50, 50), (52, 50), (61, 70), (111, 70), (119, 50), (188, 50), (201, 70),
        (251, 70), (286, 100), (316, 100), (336, 120), (346, 120), (362, 80), (370, 50), (380, 0), (400, 0)]


def f5():
    o = []
    x0, x1, y0, y1 = 70, 700, 90, 320
    fx = lin(0, 1180, x0, x1); fy = lin(0, 120, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0, 200, 400, 600, 780, 1000, 1180], [0, 30, 60, 90, 120], fx, fy, 'time (s)', 'speed (km/h)'))
    pts = []
    for r in range(4): pts += [(t + 195 * r, v) for t, v in ECE]
    pts += [(t + 780, v) for t, v in EUDC]
    o.append(R(fx(0), y0, fx(60) - fx(0), y1 - y0, NXS, NXS, 0, 0))
    o.append(P([(fx(t), fy(v)) for t, v in pts], AC, 2.2))
    o.append(brace(fx(0) + 2, fx(780) - 2, y0 - 30, MUT, up=False))
    o.append(T((fx(0) + fx(780)) / 2, y0 - 38, 'urban part: 4 × 195 s, 4 × 1.01 km, top 50 km/h', 13, 'middle', MUT))
    o.append(brace(fx(780) + 2, fx(1180) - 2, y0 - 30, MUT))
    o.append(T((fx(780) + fx(1180)) / 2, y0 - 38, 'extra-urban: 400 s, 6.96 km', 13, 'middle', MUT))
    o.append(Tb(fx(64), fy(64), 'cold start: CO and HC', 13, 'start', NX, bold=True))
    o.append(Tb(fx(64), fy(64) + 18, 'before catalyst light-off', 13, 'start', NX))
    o.append(Tb(fx(1126), fy(108), '120', 13, 'end', AC, bold=True))
    o.append(T(385, 392, 'whole trace: 1180 s, 11.0 km, average 33.6 km/h; bag NOx 0.66 g ÷ 11.0 km = 0.060 g/km', 13, 'middle', INK, bold=True))
    return 406, ''.join(o)


FIG[5] = (f5, 'The NEDC speed trace, on which India’s Modified Indian Driving Cycle for cars is built: four urban parts and one extra-urban '
              'part, 11.0 km in 1180 s. The shaded first minute is the cold start, where most of the cycle’s CO and HC come out. The worked '
              'example divides the bag mass by these 11.0 km.',
          'Vehicle speed against time from 0 to 1180 seconds. Four identical urban parts reach 15, 32 and 50 kilometres per hour with idle '
          'between them; the extra-urban part climbs to 70, 50, 70, 100 and 120 kilometres per hour before stopping. The first 60 seconds '
          'are shaded as the cold start.')


# ---- 6.6 energy carried per litre of storage, and CO2 per MJ of the worked example ----
def f6():
    o = []
    rows = [('diesel, liquid', 35.7), ('petrol, liquid', 32.6), ('LPG, liquid ≈ 8 bar', 25.3), ('ethanol, liquid', 21.3),
            ('CNG, 200 bar, 15 °C', 8.4), ('hydrogen, 700 bar', 4.8)]
    x0, x1 = 200, 520
    fx = lin(0, 40, x0, x1)
    o.append(T(14, 26, 'Energy per litre of tank (LHV, MJ/L)', 14, 'start', bold=True))
    for i, (n, v) in enumerate(rows):
        y = 44 + i * 40
        c, cs = (AC, ACS) if v > 20 else (NX, NXS)
        o.append(T(x0 - 10, y + 20, n, 13, 'end'))
        o.append(R(x0, y + 4, fx(v) - x0, 24, cs, c, 4))
        o.append(T(fx(v) + 8, y + 21, f'{v:.1f}', 13, 'start', c, bold=True))
    o.append(L(x0, 40, x0, 290, L2, 1.5))
    # CO2 per MJ
    bx = 590
    o.append(T(bx + 50, 26, 'kg CO₂ per MJ', 14, 'middle', bold=True))
    fy = lin(0, 0.08, 280, 60)
    for j, (n, v) in enumerate((('petrol', 0.0701), ('methane', 0.0549))):
        X = bx + j * 56
        o.append(R(X, fy(v), 40, 280 - fy(v), ACS if j == 0 else LVS, AC if j == 0 else LV, 4))
        o.append(T(X + 20, fy(v) - 8, f'{v:.4f}', 13, 'middle', AC if j == 0 else LV, bold=True))
        o.append(T(X + 20, 298, n, 13))
    o.append(L(bx - 6, 280, bx + 104, 280, L2, 1.5))
    o.append(T(bx + 50, 322, '22 % less', 13, 'middle', LV, bold=True))
    o.append(T(14, 322, 'A 60 L CNG cylinder holds 10.1 kg of methane: 503 MJ, the energy of 15.5 L of petrol.', 13, 'start', MUT))
    return 340, ''.join(o)


FIG[6] = (f6, 'Left: energy per litre of tank, from density × LHV (CNG and hydrogen at 15 °C, real-gas densities 168 and 40 kg/m³). Gas fuels '
              'win on carbon, right, but lose four to seven times on tank volume, which is why the worked example’s 22 % CO₂ saving comes '
              'with a short range.',
          'Horizontal bars of energy per litre: diesel 35.7, petrol 32.6, LPG 25.3, ethanol 21.3, CNG at 200 bar 8.4 and hydrogen at 700 bar '
          '4.8 megajoules per litre. Two vertical bars on the right: petrol 0.0701 and methane 0.0549 kilograms of CO2 per megajoule.')


# ---- 6.7 dual-fuel engine with the worked example's flows ----
def f7():
    o = []
    o.append(boxt(14, 40, 150, 56, ['CNG 200 bar', '6.6 kg/h'], ACS, AC, 13, bold_first=True))
    o.append(L(164, 68, 206, 68, AC, 2, arrow='n'))
    o.append(boxt(208, 40, 150, 56, ['regulator +', 'gas injector'], PANEL, AC, 13, bold_first=True))
    o.append(L(283, 96, 283, 134, AC, 2, arrow='n'))
    o.append(L(14, 160, 250, 160, LV, 2.5, arrow='l')); o.append(T(20, 150, 'air', 13, 'start', LV, bold=True))
    o.append(R(252, 136, 190, 48, PANEL, AC, 8)); o.append(T(347, 157, 'intake port:', 13)); o.append(T(347, 175, 'lean gas–air charge', 13))
    o.append(L(442, 160, 478, 160, AC, 2.5, arrow='n'))
    # cylinder
    o.append(R(480, 100, 130, 170, PANEL, INK, 4))
    o.append(R(490, 220, 110, 40, ACS, AC, 3)); o.append(T(545, 245, 'piston', 13))
    o.append(L(545, 52, 545, 118, NX, 3, arrow='x'))
    o.append(boxt(470, 14, 150, 40, ['diesel pilot 2.5 kg/h'], NXS, NX, 13))
    o.append(T(545, 160, 'pilot fires', 13, 'middle', NX, bold=True)); o.append(T(545, 178, 'near TDC', 13, 'middle', NX))
    o.append(L(610, 180, 700, 180, MUT, 2.5, arrow='m')); o.append(T(655, 170, 'exhaust', 13, 'middle', MUT))
    # energy bar
    y = 300
    o.append(T(14, y, 'Fuel energy per hour in dual-fuel mode (40 kW)', 14, 'start', bold=True))
    fx = lin(0, 436.25, 14, 706)
    o.append(R(fx(0), y + 14, fx(106.25) - fx(0), 34, NXS, NX, 3)); o.append(T((fx(0) + fx(106.25)) / 2, y + 36, 'diesel 106 MJ/h', 13, bold=True))
    o.append(R(fx(106.25), y + 14, fx(436.25) - fx(106.25), 34, ACS, AC, 3)); o.append(T((fx(106.25) + fx(436.25)) / 2, y + 36, 'gas 330 MJ/h = 75.6 % of the energy', 13, bold=True))
    o.append(T(360, y + 74, 'diesel saved: (10 − 2.5) ÷ 10 = 75 % by mass; efficiency 33.9 % on diesel, 33.0 % dual fuel', 13, 'middle', MUT))
    return 390, ''.join(o)


FIG[7] = (f7, 'The worked example’s engine. Gas is metered into the intake air and never passes the injection pump; the 2.5 kg/h diesel pilot '
              'is the only ignition source. The bar splits the 436 MJ/h of fuel energy: gas carries 75.6 % of it.',
          'A CNG supply at 6.6 kilograms per hour feeds a regulator and gas injector in the intake port, where it mixes with air into a lean '
          'charge. A diesel pilot injector of 2.5 kilograms per hour fires into the cylinder near top dead centre. A bar shows 106 megajoules '
          'per hour from diesel and 330 from gas.')


# ---- 6.8 divided-chamber stratified charge engine with the worked example's mixtures ----
def f8():
    o = []
    # cylinder and head
    o.append(R(120, 120, 300, 230, PANEL, INK, 4))
    o.append(R(130, 290, 280, 52, ACS, AC, 3)); o.append(T(270, 322, 'piston', 14))
    o.append(R(100, 92, 340, 28, PANEL, INK, 2))
    o.append(T(380, 112, 'cylinder head', 13, 'middle', MUT))
    # prechamber
    o.append(R(220, 22, 100, 70, NXS, NX, 10))
    o.append(T(270, 50, 'pre-chamber', 13, bold=True)); o.append(T(270, 70, 'AFR 12, rich', 13, 'middle', NX, bold=True))
    o.append(L(300, 30, 340, 6, INK, 2)); o.append(T(346, 14, 'spark plug', 13, 'start'))
    o.append(L(232, 36, 180, 10, NX, 2)); o.append(T(176, 14, 'small valve, rich mixture', 13, 'end', NX))
    # torch
    o.append(R(262, 92, 16, 28, NXS, NX, 2))
    for dx in (-60, 0, 60):
        o.append(L(270, 124, 270 + dx, 190, NX, 3, arrow='x'))
    o.append(T(270, 214, 'flame jets (torch)', 13, 'middle', NX, bold=True))
    o.append(T(270, 250, 'main chamber: AFR 22, lean', 14, 'middle', LV, bold=True))
    o.append(L(140, 80, 160, 118, LV, 2, arrow='l')); o.append(T(100, 72, 'main valve, lean', 13, 'middle', LV))
    # side panel: numbers
    bx = 460
    o.append(T(bx, 40, 'Per cycle (worked example)', 14, 'start', bold=True))
    lines = [('pre-chamber', '0.05 g air + 0.0042 g fuel', NX), ('main chamber', '0.50 g air + 0.0227 g fuel', LV),
             ('whole charge', '0.55 g ÷ 0.0269 g = 20.4', AC)]
    for i, (a, b, c) in enumerate(lines):
        y = 72 + i * 58
        o.append(T(bx, y, a, 13, 'start', c, bold=True)); o.append(T(bx, y + 20, b, 13, 'start'))
    o.append(T(bx, 252, 'λ = 20.4 ÷ 14.7 = 1.39', 14, 'start', AC, bold=True))
    o.append(T(bx, 282, 'lean overall, yet the plug', 13, 'start', MUT))
    o.append(T(bx, 300, 'fires a rich, easy mixture', 13, 'start', MUT))
    return 360, ''.join(o)


FIG[8] = (f8, 'A divided-chamber stratified charge engine, the CVCC type. A small valve fills the pre-chamber with a rich mixture that the plug '
              'lights easily; jets of flame then burn the lean main charge. With the worked example’s masses the whole charge is lean, '
              'λ = 1.39, while the plug still sees an air–fuel ratio of 12.',
          'Cross-section of a cylinder with a small pre-chamber in the head. The pre-chamber has its own small valve, a spark plug and a '
          'rich mixture at air-fuel ratio 12; three flame jets pass through a nozzle into the main chamber, which holds a lean mixture at 22. '
          'A side panel gives 0.05 grams of air in the pre-chamber, 0.50 in the main chamber, and an overall ratio of 20.4, lambda 1.39.')


# ---- 6.9 the φ–T map (sketch) with conventional diesel, PCCI and HCCI/RCCI ----
def f9():
    o = []
    x0, x1, y0, y1 = 80, 690, 40, 330
    fx = lin(1000, 3000, x0, x1); fy = lin(0, 6, y1, y0)
    o.append(axes(x0, x1, y0, y1, [1000, 1500, 2000, 2500, 3000], [0, 1, 2, 3, 4, 5, 6], fx, fy, 'local temperature (K)', 'local φ (sketch)'))
    # soot island: ellipse-ish
    pts = []
    for i in range(61):
        a = 2 * math.pi * i / 60
        pts.append((fx(2050 + 520 * math.cos(a)), fy(3.6 + 1.45 * math.sin(a))))
    o.append(P(pts, AC, 2.5, fill=ACS))
    o.append(T(fx(2050), fy(3.7), 'soot', 15, 'middle', AC, bold=True))
    o.append(T(fx(2050), fy(3.3), 'φ > 2, 1600–2600 K', 13, 'middle', AC))
    # NOx region
    o.append(f'<path d="M{fx(2200):.1f},{y1:.1f} L{fx(2200):.1f},{fy(1.1):.1f} Q{fx(2400):.1f},{fy(1.6):.1f} {fx(3000):.1f},{fy(1.7):.1f} L{fx(3000):.1f},{y1:.1f} Z" '
             f'style="fill:var(--next-soft);stroke:var(--next);stroke-width:2.5"/>')
    o.append(T(fx(2620), fy(0.6), 'NOx', 15, 'middle', NX, bold=True))
    o.append(T(fx(2620), fy(0.3), 'T > 2200 K', 13, 'middle', NX))
    # LTC window
    o.append(R(fx(1150), fy(1.0), fx(2000) - fx(1150), fy(0) - fy(1.0) - 1, LVS, LV, 6, dash='6 4'))
    o.append(T(fx(1575), fy(0.62), 'HCCI, RCCI: lean, < 2000 K', 13, 'middle', LV, bold=True))
    o.append(T(fx(1575), fy(0.27), 'low NOx and low soot', 13, 'middle', LV))
    # conventional diesel path and PCCI
    o.append(arc(fx(1150), fy(5.6), fx(2750), fy(0.95), -0.18, MUT, 2.5, 'm'))
    o.append(Tb(fx(1180), fy(5.75), 'conventional diesel spray: crosses both', 13, 'start', MUT, bold=True))
    o.append(arc(fx(1250), fy(2.4), fx(1800), fy(1.15), -0.15, LV, 2.5, 'l', dash='6 4'))
    o.append(Tb(fx(1150), fy(2.65), 'PCCI: premixed early', 13, 'start', LV))
    return 400, ''.join(o)


FIG[9] = (f9, 'A sketch of the φ–T map of local gas states. Soot forms in the rich island, NOx in the hot band; a conventional diesel spray passes '
              'through both. HCCI and RCCI keep every parcel lean and below about 2000 K, so both stay low; PCCI moves the spray partway there.',
          'Map with local temperature from 1000 to 3000 kelvin across and local equivalence ratio from 0 to 6 up. A shaded soot island sits at '
          'equivalence ratio above 2 between 1600 and 2600 kelvin; a NOx region fills temperatures above 2200 kelvin at lean mixtures. A '
          'dashed box at lean mixtures below 2000 kelvin is labelled HCCI and RCCI. A curved path for a conventional diesel spray crosses both regions.')


# ---- 6.10 optical engine (Bowditch piston) with a laser sheet and the worked example's two flame frames ----
def f10():
    o = []
    # cylinder with liner window
    o.append(R(150, 40, 200, 150, PANEL, INK, 3))
    o.append(R(150, 70, 14, 60, ACS, AC, 2)); o.append(R(336, 70, 14, 60, ACS, AC, 2))
    o.append(T(250, 34, 'cylinder head, spark plug', 13, 'middle', MUT))
    # flame circles
    o.append(f'<circle cx="250" cy="100" r="24" style="fill:none;stroke:var(--next);stroke-width:2;stroke-dasharray:5 4"/>')
    o.append(f'<circle cx="250" cy="100" r="36" style="fill:none;stroke:var(--next);stroke-width:2.5"/>')
    o.append(T(250, 160, 'flame radius 8 → 12 mm', 13, 'middle', NX, bold=True))
    # laser sheet
    o.append(boxt(14, 80, 100, 40, ['laser 532 nm'], NXS, NX, 13))
    o.append(L(114, 100, 148, 100, NX, 3, arrow='x'))
    o.append(T(40, 146, 'sheet through', 13, 'start', NX)); o.append(T(40, 164, 'liner window', 13, 'start', NX))
    # extended piston with crown window and mirror
    o.append(R(190, 190, 120, 150, PANEL, AC, 4))
    o.append(R(196, 190, 108, 12, LVS, LV, 2)); o.append(T(250, 222, 'quartz crown window', 13, 'middle', LV))
    o.append(L(200, 320, 300, 246, AC, 4))
    o.append(T(184, 300, '45° mirror', 13, 'end', AC, bold=True))
    o.append(L(250, 205, 250, 280, LV, 2, dash='5 4', arrow='l'))
    o.append(L(252, 282, 380, 282, LV, 2, dash='5 4', arrow='l'))
    o.append(boxt(382, 258, 140, 48, ['high-speed camera'], PANEL, LV, 13))
    o.append(T(250, 360, 'extended (Bowditch) piston', 13, 'middle', MUT))
    # numbers panel
    bx = 545
    o.append(T(bx, 60, 'Two frames 0.1 ms apart', 14, 'start', bold=True))
    o.append(T(bx, 88, 'Δr = 12 − 8 = 4 mm', 13, 'start'))
    o.append(T(bx, 112, 'S = 4 mm ÷ 0.1 ms', 13, 'start'))
    o.append(T(bx, 136, '= 40 m/s', 13, 'start', NX, bold=True))
    o.append(T(bx, 168, 'at 1500 rev/min,', 13, 'start'))
    o.append(T(bx, 192, '0.1 ms = 0.9° crank', 13, 'start', AC, bold=True))
    return 380, ''.join(o)


FIG[10] = (f10, 'An optical engine of the Bowditch type. A laser sheet enters through the liner window; light from the chamber goes down through '
                'the quartz crown, and the 45° mirror in the extended piston turns it sideways to a camera beside the engine. The two flame '
                'outlines are the worked example’s frames, 0.1 ms apart.',
           'Cylinder with liner windows and a laser sheet at 532 nanometres entering from the left. Two flame circles of 8 and 12 millimetres '
           'radius. Below, an extended piston with a quartz crown window and a 45 degree mirror reflecting light sideways to a high-speed '
           'camera. A side panel computes 40 metres per second and 0.9 degrees of crank angle at 1500 revolutions per minute.')

spec = make_spec(FIG)
