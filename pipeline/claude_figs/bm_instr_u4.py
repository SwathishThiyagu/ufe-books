"""Claude's hand-drawn figures for bm-instr-u4 (biosensors), one per chapter, each drawn from that chapter's own worked
example and numbers. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *


def sb(base, s, size=11):
    return f'{base}<tspan baseline-shift="sub" font-size="{size}">{s}</tspan>'


FIG = {}


def chain(xs, y, w, h, labels, size=13, fills=None):
    o = []
    for i, (x, lines) in enumerate(zip(xs, labels)):
        o.append(boxt(x, y, w, h, lines, fill=(fills[i] if fills else PANEL), size=size, bold_first=True))
        if i:
            o.append(L(xs[i - 1] + w + 2, y + h / 2, x - 3, y + h / 2, AC, 2, arrow='n'))
    return ''.join(o)


# ---- ch1: the biosensor chain and the standard-addition line of worked example 1 ----
def f1():
    xs = [10 + i * 142 for i in range(5)]
    o = [chain(xs, 16, 120, 66, [['analyte', 'glucose in', 'diluted serum'], ['bioreceptor', 'glucose oxidase'], ['transducer', 'electrode:', 'current'],
                               ['conditioning', 'amplify, filter,', 'digitise'], ['display', 'mmol/L']], 12, fills=[PANEL, LVS, ACS, PANEL, PANEL])]
    x0, x1, y0, y1 = 100, 520, 140, 380
    fx = lambda a: x0 + (x1 - x0) * (a + 14) / 26
    fy = lambda i: y1 - (y1 - y0) * i / 8
    o.append(L(x0, y1, x1, y1, L2, 1.5))
    o.append(L(fx(0), y0, fx(0), y1, L2, 1.5))
    for v in (-12, -8, -4, 0, 4, 8, 12):
        o.append(L(fx(v), y1, fx(v), y1 + 5, L2, 1.5)); o.append(T(fx(v), y1 + 20, neg(v), 13, fill=MUT))
    for v in (2, 4, 6, 8):
        o.append(L(fx(0) - 5, fy(v), fx(0), fy(v), L2, 1.5)); o.append(T(fx(0) - 9, fy(v) + 4, str(v), 13, 'end', MUT))
    o.append(T((x0 + x1) / 2, y1 + 40, 'glucose added to the cell (µmol)', 14, fill=MUT))
    o.append(T(fx(0) + 8, y0 - 10, 'current scaled to 5.00 mL (µA)', 13, 'start', MUT))
    sl = 0.314
    o.append(L(fx(-12.74), y1, fx(0), fy(4.0), AC, 2, dash='6 4'))
    o.append(L(fx(0), fy(4.0), fx(11.5), fy(4.0 + sl * 11.5), AC, 2.6))
    o.append(C(fx(0), fy(4.0), 6, LV)); o.append(C(fx(10), fy(7.14), 6, LV)); o.append(C(fx(-12.74), y1, 6, AC))
    o.append(Tb(fx(0) + 12, fy(4.0) + 20, 'sample alone: 4.0 µA', 13, 'start', LV))
    o.append(Tb(fx(10) + 2, fy(7.14) + 26, '7.14 µA', 13, 'middle', LV))
    o.append(Tb(fx(-12.74) + 4, y1 - 16, '−12.7 µmol', 13, 'start', AC))
    o.append(boxt(546, 130, 164, 250, ['spike', '7.0 × 5.10/5.00', '= 7.14 µA', 'x-intercept', '12.7 µmol in', 'the 5.00 mL cell', '= 2.55 mmol/L', '× 5 dilution = 12.7'],
                  size=13, bold_first=True, fill=ACS))
    return 430, ''.join(o)


FIG[1] = (f1, 'A biosensor is a chain from analyte to display. Below, worked example 1 drawn as a standard-addition line: the spiked reading is first scaled back to '
              'the 5.00 mL volume (7.14 µA), and the line through the two points meets zero current at −12.7 µmol, so the cell held 2.55 mmol/L and the serum 12.7 mmol/L.',
          'Five boxes from analyte to bioreceptor, transducer, conditioning and display, above a plot of current against glucose added, with points at 0 and 10 '
          'micromoles and a dashed line extended back to minus 12.7 micromoles on the axis.')


# ---- ch2: Michaelis-Menten curves for Km 25 and apparent Km 60 mmol/L ----
def f2():
    x0, x1, y0, y1 = 90, 560, 40, 330
    fx = lambda s: x0 + (x1 - x0) * s / 100
    fy = lambda v: y1 - (y1 - y0) * v / 130
    o = [f'<rect x="{fx(2):.1f}" y="{y0}" width="{fx(20) - fx(2):.1f}" height="{y1 - y0}" style="fill:var(--next-soft)"/>']
    o.append(axes(x0, x1, y0, y1, [0, 20, 40, 60, 80, 100], [0, 30, 60, 90, 120], fx, fy, 'glucose S (mmol/L)', 'rate v (µmol min⁻¹ mg⁻¹)'))
    o.append(Tb(fx(11), y0 + 18, 'blood range', 12, 'middle', NX))
    o.append(L(x0, fy(120), x1, fy(120), MUT, 1.2, dash='6 4'))
    o.append(Tb(x1 - 4, fy(120) - 7, sb('V', 'max') + ' = 120', 13, 'end', MUT))
    o.append(L(x0, fy(60), fx(60), fy(60), MUT, 1.2, dash='4 4'))
    for km, c in ((25, AC), (60, LV)):
        o.append(P([(fx(s), fy(120 * s / (km + s))) for s in [i * 0.5 for i in range(201)]], c, 2.6))
        o.append(L(fx(km), fy(60), fx(km), y1, c, 1.2, dash='4 4'))
        o.append(C(fx(km), fy(60), 5, c))
    o.append(P([(fx(0), fy(0)), (fx(26), fy(120 * 26 / 25))], AC, 1.4, dash='3 4'))
    o.append(Tb(fx(26) + 6, fy(120 * 26 / 25) + 4, 'straight line ' + sb('V', 'max') + '/' + sb('K', 'm') + ' × S', 12, 'start', AC))
    o.append(Tb(fx(80), fy(120 * 80 / 105) - 12, 'in solution, ' + sb('K', 'm') + ' 25', 13, 'middle', AC))
    o.append(Tb(fx(82), fy(120 * 82 / 142) + 22, 'immobilised, apparent ' + sb('K', 'm') + ' 60', 13, 'middle', LV))
    o.append(C(fx(20), fy(120 * 20 / 45), 5, AC)); o.append(C(fx(20), fy(30), 5, LV))
    o.append(Tb(fx(20) + 8, fy(120 * 20 / 45) + 4, '53.3', 12, 'start', AC))
    o.append(Tb(fx(20) + 8, fy(30) + 4, '30.0', 12, 'start', LV))
    o.append(Tb(x0 + 6, fy(60) - 6, 'half ' + sb('V', 'max'), 12, 'start', MUT))
    o.append(boxt(578, 60, 132, 230, ['at S = 20', 'straight line', 'would give 96', sb('K', 'm') + ' 25: 53.3', '= 0.56 of it', sb('K', 'm') + ' 60: 30.0', 'vs 40 = 0.75'],
                  size=13, bold_first=True, fill=PANEL))
    return 380, ''.join(o)


FIG[2] = (f2, 'Michaelis–Menten curves for the worked example: V<sub>max</sub> = 120, K<sub>m</sub> = 25 mmol/L in solution and an apparent K<sub>m</sub> of 60 mmol/L on the electrode. '
              'Each curve reaches half of V<sub>max</sub> at its own K<sub>m</sub>; the larger apparent K<sub>m</sub> keeps the response closer to a straight line over the blood range.',
          'Two saturating curves of rate against glucose from 0 to 100 mmol/L, one reaching half of 120 at 25 and one at 60 mmol/L, with the 2 to 20 mmol/L blood range '
          'shaded and points at 20 mmol/L giving 53.3 and 30.0.')


# ---- ch3: three-electrode cell, potentiostat and transimpedance amplifier ----
def f3():
    o = [boxt(24, 14, 220, 48, ['potentiostat', 'WE at +0.7 V vs RE'], size=12, bold_first=True)]
    o.append(R(24, 110, 310, 210, NXS, NX, 8, 1.8))
    o.append(T(226, 180, 'buffer with', 12, 'middle', MUT)); o.append(T(226, 195, 'glucose', 12, 'middle', MUT))
    for x, lab, sub in ((80, 'CE', 'Pt'), (170, 'RE', 'Ag/AgCl'), (282, 'WE', 'Pt + GOx')):
        o.append(L(x, 96, x, 262, INK, 6))
        o.append(T(x, 284, lab, 13, bold=True))
        o.append(T(x, 300, sub, 12, fill=MUT))
    o.append(L(80, 62, 80, 96, AC, 2)); o.append(L(170, 62, 170, 96, AC, 2))
    o.append(R(274, 236, 16, 28, LVS, LV, 3, 1.5))
    o.append(T(268, 246, 'enzyme', 11, 'end', LV)); o.append(T(268, 259, 'layer', 11, 'end', LV))
    o.append(P([(282, 96), (282, 80), (440, 80), (440, 172), (462, 172)], AC, 2))
    o.append(Tb(360, 74, 'I = 1.93 µA', 13, 'middle', AC))
    # op-amp
    o.append(P([(462, 152), (462, 232), (548, 192), (462, 152)], INK, 2, fill=PANEL))
    o.append(T(470, 177, '−', 14, 'start', INK, True)); o.append(T(470, 218, '+', 14, 'start', INK, True))
    o.append(P([(462, 212), (440, 212), (440, 236)], INK, 2))
    o.append(L(428, 236, 452, 236, INK, 2)); o.append(L(433, 242, 447, 242, INK, 2))
    o.append(P([(450, 172), (450, 122), (482, 122)], INK, 2))
    o.append(R(482, 112, 48, 20, PANEL, INK, 2, 1.8))
    o.append(P([(530, 122), (570, 122), (570, 192), (548, 192)], INK, 2))
    o.append(T(506, 104, sb('R', 'f') + ' = 100 kΩ', 12))
    o.append(L(570, 192, 592, 192, AC, 2, arrow='n'))
    o.append(boxt(594, 150, 118, 84, ['output', '−1.93 µA × 100 kΩ', '= −0.193 V'], size=12, bold_first=True, fill=ACS))
    o.append(T(586, 262, 'with 1.0 MΩ: −1.93 V,', 12, 'middle', MUT))
    o.append(T(586, 278, 'little headroom on 3 V', 12, 'middle', MUT))
    o.append(T(24, 350, 'at the enzyme: glucose + O₂ → gluconolactone + H₂O₂', 13, 'start'))
    o.append(T(24, 372, 'at the WE: H₂O₂ → O₂ + 2H⁺ + 2e⁻, so n = 2 and I = nFJA', 13, 'start'))
    return 390, ''.join(o)


FIG[3] = (f3, 'The three-electrode cell: the potentiostat holds the working electrode at +0.7 V against the reference, and the counter electrode carries the current. '
              'The working-electrode current of worked example 1, 1.93 µA, flows into a transimpedance amplifier; with R<sub>f</sub> = 100 kΩ the output is −0.193 V.',
          'Beaker with counter, reference and enzyme-coated working electrodes, a potentiostat box wired to the counter and reference, and the working electrode wired to an '
          'op-amp with a 100 kilo-ohm feedback resistor giving minus 0.193 volts.')


# ---- ch4: ISFET cross-section with the reference electrode in the sample ----
def f4():
    o = [P([(60, 110), (520, 110), (520, 200), (390, 200), (390, 236), (190, 236), (190, 200), (60, 200), (60, 110)], 'none', 0, fill=NXS)]
    o.append(T(80, 132, 'sample electrolyte', 13, 'start', NX, True))
    o.append(R(60, 200, 130, 60, 'var(--line)', MUT, 2, 1.2))
    o.append(R(390, 200, 130, 60, 'var(--line)', MUT, 2, 1.2))
    o.append(T(125, 235, 'epoxy', 12, fill=INK)); o.append(T(455, 235, 'epoxy', 12, fill=INK))
    o.append(R(190, 236, 200, 12, LVS, LV, 0, 1.4))
    o.append(R(190, 248, 200, 12, ACS, AC, 0, 1.4))
    o.append(R(60, 260, 460, 96, PANEL, INK, 0, 1.6))
    o.append(R(80, 260, 110, 38, 'var(--accent-soft)', AC, 0, 1.4))
    o.append(R(390, 260, 110, 38, 'var(--accent-soft)', AC, 0, 1.4))
    o.append(T(135, 284, 'n⁺ source', 13, bold=True)); o.append(T(445, 284, 'n⁺ drain', 13, bold=True))
    o.append(L(192, 266, 388, 266, AC, 2, dash='5 4'))
    o.append(T(290, 284, 'channel', 12, fill=AC))
    o.append(T(290, 334, 'p-type silicon', 13, fill=MUT))
    o.append(P([(530, 242), (540, 242)], LV, 1.4)); o.append(L(392, 242, 530, 242, LV, 1))
    o.append(T(544, 246, 'Si₃N₄ or Ta₂O₅ sensing layer', 12, 'start', LV))
    o.append(L(392, 254, 540, 266, AC, 1))
    o.append(T(544, 270, 'SiO₂ gate oxide', 12, 'start', AC))
    # reference electrode and gate supply
    o.append(L(290, 28, 290, 170, INK, 6))
    o.append(C(290, 172, 5, INK))
    o.append(T(300, 92, 'Ag/AgCl reference', 12, 'start', INK, True))
    o.append(T(300, 106, 'electrode in the sample', 12, 'start', MUT))
    o.append(L(290, 28, 540, 28, AC, 2))
    o.append(boxt(540, 10, 170, 150, ['feedback sets', 'the gate voltage to', 'hold drain current', 'pH 7.4 → 7.1: shift', '59.16 × 0.3 = 17.7 mV'],
                  size=13, bold_first=True, fill=ACS))
    o.append(L(80, 279, 40, 279, INK, 2)); o.append(T(36, 284, 'S', 13, 'end', INK, True))
    o.append(L(500, 279, 528, 279, INK, 2)); o.append(T(532, 284, 'D', 13, 'start', INK, True))
    return 370, ''.join(o)


FIG[4] = (f4, 'An ISFET is a MOSFET whose metal gate is replaced by the sample: the SiO₂ gate oxide carries a Si₃N₄ or Ta₂O₅ sensing layer, and the Ag/AgCl reference '
              'electrode sits in the sample above it. With feedback holding I<sub>D</sub> fixed, a pH fall from 7.4 to 7.1 moves V<sub>G</sub> by 17.7 mV.',
          'Cross-section with p-type silicon, n-plus source and drain, a channel, a thin gate oxide and a sensing layer in a window between epoxy blocks, sample liquid '
          'above, and a reference electrode dipping into the sample wired to a gate-voltage feedback box.')


# ---- ch5: the disposable strip and the dose arithmetic of worked example 1 ----
def f5():
    o = [R(40, 50, 400, 120, PANEL, INK, 12, 2)]
    o.append(R(40, 82, 150, 56, LVS, LV, 4, 1.4))
    o.append(T(52, 76, 'capillary channel', 12, 'start', LV))
    o.append('<circle cx="26" cy="110" r="14" style="fill:var(--live);opacity:0.85"/>')
    o.append(T(26, 150, 'blood', 12, fill=LV))
    o.append(R(62, 92, 44, 36, ACS, AC, 3, 1.6))
    o.append(R(118, 92, 30, 36, PANEL, INK, 3, 1.6))
    o.append(R(160, 92, 12, 36, PANEL, MUT, 2, 1.4))
    o.append(P([(106, 100), (420, 100)], AC, 2)); o.append(P([(148, 112), (420, 112)], INK, 2)); o.append(P([(172, 124), (420, 124)], MUT, 2))
    for y in (100, 112, 124):
        o.append(R(420, y - 4, 14, 8, PANEL, INK, 1, 1.2))
    o.append(T(84, 198, 'WE: GOx +', 12, fill=AC)); o.append(T(84, 213, 'mediator', 12, fill=AC))
    o.append(T(134, 198, 'RE', 12)); o.append(T(178, 198, 'fill', 12, fill=MUT)); o.append(T(178, 213, 'detect', 12, fill=MUT))
    for x in (84, 134, 168):
        o.append(L(x, 186, x, 132, L2, 1))
    o.append(T(300, 155, 'printed carbon tracks to the meter', 12, fill=MUT))
    o.append(L(440, 112, 470, 112, AC, 2, arrow='n'))
    o.append(boxt(472, 40, 238, 150, ['meter', 'starts when the channel', 'is full, applies a fixed', 'potential, reads current', '212 mg/dL = 11.8 mmol/L'],
                  size=13, bold_first=True, fill=ACS))
    o.append(boxt(20, 240, 690, 130, ['dose for target 120 mg/dL, ISF 50 mg/dL per unit, 40 g at 10 g per unit',
                                       'correction = (212 − 120) ÷ 50 = 1.84 units; meal = 40 ÷ 10 = 4.0 units',
                                       'total = 5.84 units, given as 5.8 units',
                                       'unit mix-up: (212 − 6.67) ÷ 2.78 = 73.9 units, about 40 times too much'],
                  size=13, bold_first=True, fills=[INK, INK, INK, LV]))
    return 390, ''.join(o)


FIG[5] = (f5, 'A disposable glucose strip: blood fills the capillary channel, the fill-detect contact starts the timer, and the working electrode carries dried glucose oxidase '
              'and a mediator. The meter turns the current into 212 mg/dL (11.8 mmol/L); the box below works the doses of worked example 1 and the unit mix-up.',
          'Strip with a blood drop at the capillary end, working, reference and fill-detect electrodes printed along it to the meter contacts, a meter box reading 212 mg/dL, '
          'and below a box with the correction, meal and total insulin doses.')


# ---- ch6: probe monolayer on gold and the impedance changes of worked example 2 ----
def f6():
    o = [R(30, 270, 410, 24, 'var(--accent-soft)', AC, 3, 1.8)]
    o.append(T(235, 314, 'gold electrode', 13, fill=AC, bold=True))
    for x in (70, 150, 230, 310, 390):
        o.append(C(x, 266, 5, NX))
        o.append(L(x, 262, x, 230, MUT, 2, dash='3 3'))
        o.append(P([(x, 230)] + [(x + (5 if i % 2 else -5), 230 - 10 * (i + 1)) for i in range(8)], AC, 2))
    for x in (110, 190, 270, 350):
        for dx in (-8, 8):
            o.append(L(x + dx, 266, x + dx, 248, LV, 2))
    # hybridised target on probe at 230
    o.append(P([(244, 230)] + [(244 + (5 if i % 2 else -5), 230 - 10 * (i + 1)) for i in range(8)], LV, 2))
    for i in range(8):
        o.append(L(232, 226 - 10 * i, 240, 226 - 10 * i, INK, 1.2))
    o.append(T(70, 132, 'probe, 20 bases', 12, 'middle', AC))
    o.append(T(70, 146, 'Tm 60 °C', 12, 'middle', MUT))
    o.append(T(262, 130, 'matched target', 12, 'start', LV, True))
    o.append(T(262, 144, '(duplex)', 12, 'start', LV))
    o.append(T(316, 214, 'T10 linker', 11, 'start', MUT))
    o.append(T(110, 240, 'MCH', 11, 'middle', LV))
    o.append(T(30, 344, 'thiol (S) heads bond to gold; MCH backfill blocks bare metal', 12, 'start', MUT))
    o.append(T(30, 362, 'wash for this probe at Tm − 5 = 55 °C', 12, 'start', MUT))
    # Rct bars
    x0, y1 = 480, 300
    fy = lambda r: y1 - 70 * r
    o.append(L(x0, y1, 712, y1, L2, 1.5))
    o.append(L(x0, fy(1.20), 712, fy(1.20), MUT, 1.2, dash='5 4'))
    o.append(T(596, 72, 'dashed: probe alone, 1.20 kΩ', 12, 'middle', MUT))
    for i, (lab, r, pc, c) in enumerate((('blank', 1.26, '5 %', MUT), ('mismatch', 1.56, '30 %', LV), ('match', 3.00, '150 %', AC))):
        x = 500 + i * 72
        o.append(R(x, fy(r), 50, y1 - fy(r), 'var(--panel)', c, 2, 2))
        o.append(T(x + 25, fy(r) - 8, f'{r:.2f}', 12, fill=c, bold=True))
        o.append(T(x + 25, y1 + 18, lab, 12, fill=INK))
        o.append(T(x + 25, y1 + 34, pc, 12, fill=c))
    o.append(T(596, 50, sb('R', 'ct') + ' (kΩ) after the wash', 13, 'middle', MUT))
    return 380, ''.join(o)


FIG[6] = (f6, 'A DNA electrode: thiolated 20-base probes on gold, each lifted by a T10 linker, with MCH backfill between them; one probe holds a matched target as a duplex. '
              'Right, worked example 2: the charge-transfer resistance rises 5 % for the blank, 30 % for a one-mismatch target and 150 % for the matched target.',
          'Gold strip with five probe strands standing on thiol heads, short backfill molecules between them, one probe paired with a target strand, and beside it three bars '
          'of charge-transfer resistance, 1.26, 1.56 and 3.00 kilo-ohms, over a dashed baseline at 1.20.')


# ---- ch7: FRET efficiency against distance for R0 = 5.0 nm ----
def f7():
    x0, x1, y0, y1 = 90, 540, 40, 320
    fx = lambda r: x0 + (x1 - x0) * r / 10
    fy = lambda e: y1 - (y1 - y0) * e
    E = lambda r: 1 / (1 + (r / 5.0) ** 6)
    o = [axes(x0, x1, y0, y1, [0, 2, 4, 6, 8, 10], [0, 0.25, 0.5, 0.75, 1.0], fx, fy, 'donor–acceptor distance r (nm)', 'transfer efficiency E',
              str, lambda v: f'{v:.2f}')]
    o.append(P([(fx(r / 20), fy(E(r / 20))) for r in range(0, 201)], AC, 2.6))
    o.append(L(fx(5.0), fy(0.5), fx(5.0), y1, MUT, 1.2, dash='4 4'))
    o.append(L(x0, fy(0.5), fx(5.0), fy(0.5), MUT, 1.2, dash='4 4'))
    o.append(Tb(fx(5.0) + 8, fy(0.5) - 6, sb('R', '0') + ' = 5.0 nm, E = 0.50', 12, 'start', MUT))
    for r, lab, c, dx, anc in ((4.0, 'bound: 4.0 nm, E = 0.79', LV, -10, 'end'), (4.34, '4.34 nm, E = 0.70', NX, 12, 'start'),
                               (8.0, 'free: 8.0 nm, E = 0.056', LV, 0, 'middle')):
        o.append(C(fx(r), fy(E(r)), 6, c))
        o.append(Tb(fx(r) + dx, fy(E(r)) + (-12 if r < 8 else -16), lab, 12, anc, c))
    # quantum dot sketch
    o.append('<circle cx="635" cy="120" r="54" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2"/>')
    o.append('<circle cx="635" cy="120" r="38" style="fill:var(--live-soft);stroke:var(--live);stroke-width:2"/>')
    o.append(T(635, 116, 'CdSe', 13, bold=True)); o.append(T(635, 132, 'core', 12, fill=MUT))
    o.append(T(635, 194, 'ZnS shell 1–2 nm', 12, fill=AC))
    o.append(T(635, 212, 'core 2–10 nm', 12, fill=LV))
    o.append(T(635, 250, 'E = 1/(1 + (r/' + sb('R', '0') + ')⁶)', 13, bold=True))
    o.append(T(635, 272, 'ratio 0.79/0.056 = 14', 12, fill=MUT))
    return 370, ''.join(o)


FIG[7] = (f7, 'FRET efficiency against distance for a quantum-dot donor with R<sub>0</sub> = 5.0 nm. Bound at 4.0 nm, 79 % of the energy transfers; when the target leaves '
              'and r becomes 8.0 nm, only 5.6 % does. A measured E of 0.70 puts the acceptor at 4.34 nm. Right, a CdSe core with its ZnS shell.',
          'Steep falling curve of transfer efficiency against distance from 0 to 10 nanometres, crossing 0.5 at 5.0 nanometres, with points at 4.0, 4.34 and 8.0 '
          'nanometres, and beside it a quantum dot drawn as a core inside a shell.')


AFTER = {1: 1, 2: 1, 3: 2, 4: 1, 5: 1, 6: 1, 7: 1}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'after_section': AFTER[k], 'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
