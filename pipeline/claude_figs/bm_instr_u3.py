"""Claude's hand-drawn figures for bm-instr-u3 (clinical laboratory instruments), one per chapter, each drawn from that
chapter's own worked example and numbers. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *


def sb(base, s, size=11):
    return f'{base}<tspan baseline-shift="sub" font-size="{size}">{s}</tspan>'


def sp(base, s, size=11):
    return f'{base}<tspan baseline-shift="super" font-size="{size}">{s}</tspan>'


FIG = {}


def chain(xs, y, w, h, labels, size=13, fills=None):
    """a row of boxes joined by arrows"""
    o = []
    for i, (x, lines) in enumerate(zip(xs, labels)):
        o.append(boxt(x, y, w, h, lines, fill=(fills[i] if fills else PANEL), size=size, bold_first=True))
        if i:
            o.append(L(xs[i - 1] + w + 2, y + h / 2, x - 3, y + h / 2, AC, 2, arrow='n'))
    return ''.join(o)


# ---- ch1: single-beam spectrophotometer chain and the calibration line of the worked example ----
def f1():
    xs = [14 + i * 118 for i in range(6)]
    o = [chain(xs, 24, 98, 74, [['lamp', 'W-halogen', 'or D₂'], ['grating', 'mono-', 'chromator'], ['cuvette', 'blank, then', 'sample'],
                               ['detector', 'photodiode'], ['amplifier', 'gain'], ['readout', 'A and %T']], 12,
               fills=[PANEL, PANEL, ACS, PANEL, PANEL, PANEL])]
    o.append(Tb(xs[2] - 10, 128, 'I₀ in', 13, 'middle', AC))
    o.append(Tb(xs[3] - 10, 128, 'I out', 13, 'middle', AC))
    o.append(T(xs[2] + 49, 118, 'l = 1.00 cm', 12, fill=MUT))
    o.append(T(xs[1] + 49, 118, 'one λ', 12, fill=MUT))
    # calibration line A = 1.5 c (c in mmol/L)
    x0, x1, y0, y1 = 100, 520, 190, 400
    fx = lambda c: x0 + (x1 - x0) * c / 0.40
    fy = lambda a: y1 - (y1 - y0) * a / 0.60
    o.append(axes(x0, x1, y0, y1, [0, 0.1, 0.2, 0.3, 0.4], [0, 0.15, 0.30, 0.45, 0.60], fx, fy,
                  'concentration c (mmol/L)', 'absorbance A', lambda v: f'{v:.2f}', lambda v: f'{v:.2f}'))
    o.append(L(fx(0), fy(0), fx(0.40), fy(0.60), AC, 2.6))
    o.append(L(x0, fy(0.45), fx(0.30), fy(0.45), LV, 1.6, dash='6 4'))
    o.append(L(fx(0.30), fy(0.45), fx(0.30), y1, LV, 1.6, dash='6 4', arrow='l'))
    o.append(L(x0, fy(0.30), fx(0.20), fy(0.30), MUT, 1.2, dash='4 4'))
    o.append(C(fx(0), fy(0), 5.5, INK))
    o.append(C(fx(0.20), fy(0.30), 6, AC))
    o.append(C(fx(0.30), fy(0.45), 6, LV))
    o.append(Tb(fx(0) + 12, fy(0) - 10, 'blank: A = 0', 13, 'start'))
    o.append(Tb(fx(0.20) + 12, fy(0.30) + 22, 'standard 0.20 mmol/L, A 0.30', 13, 'start', AC))
    o.append(Tb(fx(0.30) - 12, fy(0.45) - 12, 'sample A 0.45 → 0.30 mmol/L', 13, 'end', LV))
    o.append(boxt(548, 200, 160, 150, ['slope = εl', '= 1.5 per mmol/L', 'ε = 1500', 'L mol⁻¹ cm⁻¹', 'standard T = 0.50'],
                  size=13, bold_first=True))
    return 450, ''.join(o)


FIG[1] = (f1, 'A single-beam spectrophotometer: the grating picks one wavelength, the blank sets I₀, and the detector reads the light left after the sample. '
              'Below, the worked example\'s calibration line: the 0.20 mmol/L standard reads A = 0.30, so a sample reading A = 0.45 is 0.30 mmol/L.',
          'Block chain lamp, grating monochromator, cuvette, photodiode, amplifier and readout, above a straight calibration line of absorbance '
          'against concentration through the blank, the standard at 0.20 mmol/L and A 0.30, and the sample at A 0.45 and 0.30 mmol/L.')


# ---- ch2: flame photometer with lithium internal standard (worked example 2) ----
def f2():
    o = [boxt(14, 70, 112, 62, ['serum 1:50', 'in diluent', 'with lithium'], size=12, bold_first=True)]
    o.append(boxt(150, 70, 104, 62, ['nebulizer', 'fine spray'], size=12, bold_first=True))
    o.append(L(128, 101, 147, 101, AC, 2, arrow='n'))
    o.append(L(176, 178, 176, 135, L2, 1.6, arrow='m'))
    o.append(T(176, 194, 'air', 12, fill=MUT))
    o.append(L(226, 178, 226, 135, L2, 1.6, arrow='m'))
    o.append(T(226, 194, 'LPG', 12, fill=MUT))
    # burner and flame
    o.append(R(290, 120, 38, 90, PANEL, INK, 3, 1.8))
    o.append(L(256, 101, 270, 101, AC, 2))
    o.append(P([(270, 101), (270, 160), (287, 160)], AC, 2))
    o.append(f'<path d="M290,120 C286,92 300,70 309,36 C318,70 332,92 328,120 Z" style="fill:var(--live-soft);stroke:var(--live);stroke-width:2"/>')
    o.append(f'<path d="M298,120 C296,100 304,88 309,70 C314,88 322,100 320,120 Z" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:1.5"/>')
    o.append(T(309, 232, 'flame', 13, bold=True))
    o.append(T(309, 250, '≈ 1900 °C', 12, fill=MUT))
    # lens
    o.append('<ellipse cx="372" cy="90" rx="9" ry="44" style="fill:var(--panel);stroke:var(--accent);stroke-width:2"/>')
    o.append(L(334, 90, 360, 90, LV, 2, arrow='l'))
    o.append(T(372, 152, 'lens', 12, fill=MUT))
    ys = [26, 112, 198]
    lines = [('589 nm', 'Na filter', 'photodiode'), ('766 nm', 'K filter', 'red-sensitive'), ('671 nm', 'Li filter', 'photodiode')]
    for y, (lam, f, d) in zip(ys, lines):
        o.append(L(383, 90, 424, y + 25, LV, 1.8, arrow='l'))
        o.append(boxt(428, y, 96, 50, [lam, f], size=12, bold_first=True, fill=LVS, stroke=LV))
        o.append(L(526, y + 25, 545, y + 25, AC, 2, arrow='n'))
        o.append(boxt(548, y, 104, 50, ['detector', d], size=12, bold_first=True))
    # ratio box
    o.append(P([(652, 137), (700, 137), (700, 300), (560, 300)], AC, 1.8))
    o.append(P([(652, 223), (690, 223), (690, 290), (560, 290)], AC, 1.8))
    o.append(L(560, 295, 541, 295, AC, 2, arrow='n'))
    o.append(boxt(214, 266, 324, 70, ['ratio K/Li = 0.42 (standard 0.50)', '0.10 × 0.42 / 0.50 × 50 = 4.2 mmol/L'], size=13, bold_first=True, fill=ACS))
    o.append(T(214 + 162, 360, 'spray rate down 10 %: K and Li both fall 10 %, ratio stays 0.42', 12, fill=MUT))
    return 380, ''.join(o)


FIG[2] = (f2, 'A flame photometer with a lithium internal standard: the diluted serum is sprayed into an air–LPG flame, and filters split the emitted light into '
              'the sodium, potassium and lithium lines. The potassium line at 766 nm needs a red-sensitive detector. In worked example 2 the K/Li ratio '
              'of 0.42 against 0.50 for a 0.10 mmol/L standard gives 4.2 mmol/L.',
          'Diluted serum with lithium, nebulizer fed by air and LPG, burner and flame at about 1900 degrees, lens, and three filter and detector '
          'channels at 589, 766 and 671 nanometres, with the potassium and lithium signals joined into a ratio box showing 4.2 mmol/L.')


# ---- ch3: the three electrodes in the 37 °C chamber and the computed values of the worked example ----
def f3():
    o = [R(16, 30, 478, 256, 'none', L2, 10, 1.8, dash='7 5')]
    o.append(T(30, 276, 'measuring chamber held at 37 °C', 13, 'start', MUT))
    boxes = [(36, ['glass pH', 'electrode', 'vs Ag/AgCl', '61.5 mV per pH']),
             (190, ['Severinghaus', 'pH glass behind', 'CO₂ membrane', 'and HCO₃⁻ film']),
             (344, ['Clark', 'Pt cathode', 'at −0.65 V', 'O₂ membrane'])]
    for x, lines in boxes:
        o.append(boxt(x, 74, 136, 112, lines, size=12, bold_first=True))
        o.append(L(x + 68, 74, x + 68, 52, AC, 1.8))
    o.append(L(104, 52, 512, 52, AC, 1.8, arrow='n'))
    for x in (190, 344):
        o.append(L(x + 4, 186, x + 132, 186, INK, 4))
    o.append(T(124, 64, 'voltage', 11, fill=MUT))
    o.append(T(278, 64, 'voltage', 11, fill=MUT))
    o.append(T(432, 64, 'current', 11, fill=MUT))
    o.append(R(36, 206, 444, 30, LVS, LV, 6))
    o.append(T(258, 226, 'arterial blood flows past all three electrodes', 13))
    o.append(L(4, 221, 33, 221, LV, 2, arrow='l'))
    o.append(boxt(516, 40, 196, 246, ['computer', 'pH 7.32', 'pCO₂ 30 mmHg', 'pO₂ from current', 'HCO₃⁻ = 15 mmol/L', '(Henderson–', 'Hasselbalch)',
                                      'Winter: 30.5 ± 2'], size=13, bold_first=True, fill=ACS))
    return 300, ''.join(o)


FIG[3] = (f3, 'The three electrodes of a blood gas analyser share one chamber at 37 °C. The pH and Severinghaus electrodes give voltages and the Clark '
              'electrode a current; the computer turns pH 7.32 and pCO₂ 30 mmHg into HCO₃⁻ 15 mmol/L and checks the compensation against Winter\'s formula.',
          'Measuring chamber at 37 degrees with a glass pH electrode, a Severinghaus carbon dioxide electrode and a Clark oxygen electrode side by side '
          'over a blood channel, their signals joined into a computer box showing pH 7.32, pCO2 30 mmHg and bicarbonate 15 mmol/L.')


# ---- ch4: Coulter aperture and the pulse train with the platelet and red cell bands ----
def f4():
    o = [R(24, 92, 256, 236, NXS, NX, 8, 1.8)]
    o.append(T(34, 316, 'electrolyte + blood 1:50 000', 12, 'start', MUT))
    # inner tube walls with the aperture gap
    o.append(L(160, 56, 160, 262, INK, 3))
    o.append(L(160, 280, 160, 328, INK, 3))
    o.append(L(250, 56, 250, 328, INK, 3))
    o.append(L(160, 328, 250, 328, INK, 3))
    o.append(boxt(14, 10, 230, 32, ['constant current I'], size=13, bold_first=True))
    o.append(L(46, 42, 46, 120, AC, 2)); o.append(L(46, 120, 46, 250, INK, 4))
    o.append(L(205, 42, 205, 110, AC, 2)); o.append(L(205, 110, 205, 240, INK, 4))
    o.append(T(54, 140, 'outer', 12, 'start', MUT)); o.append(T(54, 155, 'electrode', 12, 'start', MUT))
    o.append(T(213, 130, 'inner', 12, 'start', MUT))
    for (x, y, r) in ((112, 250, 6), (130, 290, 6), (92, 278, 3), (136, 236, 3), (100, 222, 6)):
        o.append(C(x, y, r, LV))
    o.append(C(160, 271, 6, LV))
    o.append(L(170, 271, 196, 271, LV, 2, arrow='l'))
    o.append(Tb(150, 350, 'aperture ≈ 100 µm', 13, 'middle', INK))
    o.append(L(150, 338, 159, 284, MUT, 1.4))
    o.append(T(256, 70, 'to vacuum', 12, 'start', MUT))
    o.append(T(256, 85, '0.50 mL', 12, 'start', MUT))
    # pulse train
    x0, x1, y0, y1 = 340, 600, 60, 300
    fy = lambda v: y1 - (y1 - y0) * v / 120
    o.append(L(x0, y1, x1, y1, L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    for v in (0, 20, 36, 100):
        o.append(T(x0 - 8, fy(v) + 4, str(v), 12, 'end', MUT))
    o.append(T(x0, y0 - 14, 'pulse height ∝ cell volume (fL)', 13, 'start', MUT))
    o.append(T((x0 + x1) / 2, y1 + 22, 'time', 13, fill=MUT))
    o.append(L(x0, fy(20), x1, fy(20), MUT, 1.2, dash='5 4'))
    o.append(L(x0, fy(36), x1, fy(36), LV, 1.4, dash='7 4'))
    o.append(T(608, fy(36) - 4, 'red cells', 12, 'start', LV, True))
    o.append(T(608, fy(36) + 11, 'above 36 fL', 12, 'start', LV))
    o.append(T(608, fy(20) + 14, 'platelets', 12, 'start', MUT, True))
    o.append(T(608, fy(20) + 29, '2–20 fL', 12, 'start', MUT))
    pulses = [(360, 9), (386, 88), (412, 14), (438, 92), (464, 84), (490, 6), (516, 95), (542, 12), (568, 86), (590, 90)]
    pts = [(x0, y1)]
    for x, v in pulses:
        pts += [(x - 9, y1), (x - 3, fy(v * 0.8)), (x, fy(v)), (x + 4, fy(v * 0.6)), (x + 12, y1)]
    pts.append((x1, y1))
    o.append(P(pts, AC, 2))
    for x, v in pulses:
        o.append(C(x, fy(v), 3.5, LV if v > 36 else MUT))
    o.append(boxt(300, 334, 414, 56, ['48 000 red cell pulses in 0.50 mL at 1:50 000',
                                     '96 000 per mL × 50 000 × 1000 = 4.8 × 10¹² per litre'], size=13, bold_first=True, fill=ACS))
    return 400, ''.join(o)


FIG[4] = (f4, 'The Coulter principle: a constant current flows through a 100 µm aperture, and each cell drawn through it raises the resistance and gives one '
              'voltage pulse. Pulses of 2–20 fL count as platelets and those above 36 fL as red cells; 48 000 red cell pulses in 0.50 mL at 1:50 000 '
              'give 4.8 × 10<sup>12</sup> per litre.',
          'Beaker of diluted blood with an inner glass tube whose wall has a 100 micrometre aperture, electrodes inside and outside joined to a constant '
          'current source, and beside it a train of voltage pulses with a dashed platelet band below 20 fL and a red cell threshold at 36 fL.')


# ---- ch5: analyser blocks and the kinetic ALT readings of worked example 2 ----
def f5():
    o = [boxt(10, 14, 210, 62, ['sample probe', '20 µL, level sensing'], size=13, bold_first=True)]
    o.append(boxt(255, 14, 210, 62, ['cuvette wheel', '37 °C: mix, incubate'], size=13, bold_first=True, fill=ACS))
    o.append(boxt(500, 14, 210, 62, ['reagent probe', '200 µL reagent'], size=13, bold_first=True))
    o.append(L(222, 45, 251, 45, AC, 2, arrow='n'))
    o.append(L(498, 45, 469, 45, AC, 2, arrow='n'))
    xs = [10 + i * 142 for i in range(5)]
    o.append(chain(xs, 118, 122, 56, [['lamp'], ['filter', '340 nm'], ['cuvette', 'l = 1 cm'], ['photodiode'], ['computer', 'ΔA/min → U/L']], 13,
                   fills=[PANEL, PANEL, ACS, PANEL, PANEL]))
    o.append(L(360, 78, 360, 114, AC, 2, arrow='n'))
    o.append(T(380, 100, 'each cuvette read every turn; then washed', 12, 'start', MUT))
    # kinetic plot
    x0, x1, y0, y1 = 100, 470, 236, 440
    fx = lambda t: x0 + (x1 - x0) * t / 3.5
    fy = lambda a: y1 - (y1 - y0) * (a - 1.10) / 0.20
    o.append(axes(x0, x1, y0, y1, [0, 1, 2, 3], [1.10, 1.15, 1.20, 1.25, 1.30], fx, fy, 'time after reagent (min)', 'A at 340 nm',
                  str, lambda v: f'{v:.2f}'))
    o.append(P([(fx(t / 10), fy(1.272 - 0.022 * (t / 10) ** 2)) for t in range(0, 11)], MUT, 2, dash='5 4'))
    o.append(L(fx(1), fy(1.25), fx(3.3), fy(1.135), AC, 2.6))
    for t, a in ((1, 1.250), (2, 1.200), (3, 1.150)):
        o.append(C(fx(t), fy(a), 6, LV))
        o.append(Tb(fx(t) + 10, fy(a) - 12, f'{a:.3f}', 12, 'start', LV))
    o.append(T(fx(0.15), fy(1.285), 'lag phase', 12, 'start', MUT))
    o.append(boxt(500, 250, 212, 170, ['ALT rate', 'ΔA/min = 0.050', 'volume ratio 220/20 = 11',
                                       '0.050 × 11 × 10⁶ / 6220', '= 88 U/L'], size=13, bold_first=True, fill=ACS))
    return 492, ''.join(o)


FIG[5] = (f5, 'A discrete analyser: the probes put 20 µL of serum and 200 µL of reagent into a cuvette on the 37 °C wheel, and the photometer reads it at '
              '340 nm on every turn. Below, worked example 2: after a short lag the absorbance falls by 0.050 per minute, which gives an ALT activity of 88 U/L.',
          'Sample probe, reagent probe and cuvette wheel at 37 degrees above a lamp, 340 nanometre filter, cuvette, photodiode and computer chain, and '
          'a plot of absorbance falling in a straight line from 1.250 at 1 minute to 1.150 at 3 minutes after a lag phase.')


# ---- ch6: TLC plate with Rf values and the serum protein electrophoresis scan ----
def f6():
    o = [R(40, 40, 150, 320, PANEL, INK, 4, 1.8)]
    base = 330
    cm = 30
    fy = lambda d: base - d * cm
    o.append(L(40, base, 190, base, MUT, 1.4, dash='5 4'))
    o.append(T(115, base + 22, 'starting line', 12, fill=MUT))
    o.append(L(40, fy(8.0), 190, fy(8.0), NX, 2, dash='7 4'))
    o.append(Tb(115, fy(8.0) - 8, 'solvent front', 12, 'middle', NX))
    o.append(C(115, base, 5, INK))
    o.append('<ellipse cx="115" cy="{:.1f}" rx="16" ry="9" style="fill:var(--accent);opacity:0.8"/>'.format(fy(2.0)))
    o.append('<ellipse cx="115" cy="{:.1f}" rx="16" ry="9" style="fill:var(--live);opacity:0.8"/>'.format(fy(5.6)))
    o.append(T(80, fy(2.0) + 5, 'A', 14, 'end', AC, True))
    o.append(T(80, fy(5.6) + 5, 'B', 14, 'end', LV, True))
    for x, d, lab, c in ((228, 2.0, '2.0 cm', AC), (264, 5.6, '5.6 cm', LV), (300, 8.0, '8.0 cm', NX)):
        o.append(L(x, base, x, fy(d) + 3, c, 1.8, arrow={'var(--accent)': 'n', 'var(--live)': 'l', 'var(--next)': 'x'}[c]))
        o.append(Tb(x, fy(d) - 8, lab, 12, 'middle', c))
    o.append(T(214, 372, 'A: 2.0/8.0 = 0.25', 13, 'start', AC, True))
    o.append(T(214, 392, 'B: 5.6/8.0 = 0.70', 13, 'start', LV, True))
    o.append(T(20, 392, sb('R', 'f') + ' values', 13, 'start', INK, True))
    # electrophoresis scan
    x0, x1, yb = 330, 708, 330
    bands = [('γ', 400, 18, 33, '15 %'), ('β', 470, 10, 48, '12 %'), ('α₂', 528, 9, 40, '9 %'), ('α₁', 578, 7, 23, '4 %'), ('albumin', 646, 12, 200, '60 %')]
    pts = []
    for i in range(0, 379):
        x = x0 + i
        h = sum(a * math.exp(-((x - m) / s) ** 2 / 2) for _, m, s, a, _ in bands)
        pts.append((x, yb - h))
    o.append(P(pts + [(x1, yb), (x0, yb)], 'none', 0, fill=ACS))
    o.append(P(pts, AC, 2.4))
    o.append(L(x0, yb, x1, yb, L2, 1.5))
    for name, m, s, a, pc in bands:
        top = yb - sum(b[3] * math.exp(-((m - b[1]) / b[2]) ** 2 / 2) for b in bands)
        if name == 'albumin':
            o.append(Tb(m - 18, top - 26, 'albumin 60 %', 13, 'end', INK, True))
            o.append(Tb(m - 18, top - 8, '0.60 × 70 = 42 g/L', 12, 'end', AC))
        else:
            o.append(T(m, top - 22, name, 13, bold=True))
            o.append(T(m, top - 7, pc, 12, fill=MUT))
    o.append(T(400, yb + 40, 'γ 0.15 × 70 = 10.5 g/L', 12, fill=MUT))
    o.append(T(x0, yb + 20, '− origin', 12, 'start', MUT))
    o.append(L(560, yb + 20, x1 - 4, yb + 20, AC, 1.8, arrow='n'))
    o.append(T(560, yb + 40, 'anode (+), pH 8.6', 12, 'start', MUT))
    return 410, ''.join(o)


FIG[6] = (f6, 'Left, a TLC plate run until the solvent front is 8.0 cm up: spot A has moved 2.0 cm (R<sub>f</sub> 0.25) and spot B 5.6 cm (R<sub>f</sub> 0.70). '
              'Right, the densitometer scan of serum protein electrophoresis at pH 8.6: albumin runs furthest toward the anode and makes 60 % of the 70 g/L '
              'total, that is 42 g/L.',
          'Thin-layer plate with a starting line, two spots at 2.0 and 5.6 centimetres and the solvent front at 8.0 centimetres, beside a densitometer '
          'trace with peaks for gamma 15 percent, beta 12, alpha-2 9, alpha-1 4 and a tall albumin peak of 60 percent nearest the anode.')


# ---- ch7: swing-out rotor top view, radius to the tube bottom, and the two rotors of worked example 2 ----
def f7():
    cx, cy = 190, 200
    o = ['<circle cx="190" cy="200" r="150" style="fill:none;stroke:var(--line2);stroke-width:1.4;stroke-dasharray:6 5"/>',
         '<circle cx="190" cy="200" r="75" style="fill:none;stroke:var(--live);stroke-width:1.4;stroke-dasharray:4 4"/>']
    for ang in (0, 90, 180, 270):
        a = math.radians(ang)
        ux, uy, vx, vy = math.cos(a), math.sin(a), -math.sin(a), math.cos(a)
        r1, r2, hw = 96, 150, 12
        corners = [(cx + ux * r1 + vx * hw, cy + uy * r1 + vy * hw), (cx + ux * r2 + vx * hw, cy + uy * r2 + vy * hw),
                   (cx + ux * r2 - vx * hw, cy + uy * r2 - vy * hw), (cx + ux * r1 - vx * hw, cy + uy * r1 - vy * hw)]
        o.append(L(cx, cy, cx + ux * r1, cy + uy * r1, INK, 5))
        o.append(P(corners + [corners[0]], INK, 1.8, fill=LVS))
        rp = 132
        pel = [(cx + ux * rp + vx * hw, cy + uy * rp + vy * hw), corners[1], corners[2], (cx + ux * rp - vx * hw, cy + uy * rp - vy * hw)]
        o.append(P(pel + [pel[0]], INK, 1.2, fill=LV))
    o.append(C(cx, cy, 10, INK))
    o.append(T(cx - 14, cy + 30, 'spindle', 12, 'end', MUT))
    o.append(L(cx, cy - 20, cx + 150, cy - 20, AC, 1.8, arrow='n'))
    o.append(Tb(cx + 88, cy - 28, 'r = 15 cm', 13, 'middle', AC))
    o.append(Tb(cx + 88, cy - 46, 'to tube bottom', 12, 'middle', MUT))
    o.append(arc(cx - 106, cy - 106, cx + 106, cy - 106, 0.35, INK, 2, 'n'))
    o.append(Tb(cx, 22, '2990 rpm', 13, 'middle', INK))
    o.append(Tb(cx - 80, cy + 92, '7.5 cm rotor', 12, 'middle', LV))
    # tube side view
    tx, ty, th = 420, 60, 250
    o.append(R(tx, ty, 50, th, PANEL, INK, 6, 2))
    o.append(R(tx + 2, ty + 34, 46, 120, LVS, 'none', 0, 0))
    o.append(R(tx + 2, ty + 154, 46, 94, LV, 'none', 4, 0))
    o.append(L(tx + 2, ty + 40, tx + 48, ty + 40, NX, 4))
    o.append(T(tx + 64, ty + 44, 'fat floats (lighter)', 12, 'start', NX))
    o.append(T(tx + 64, ty + 100, 'supernatant: serum', 13, 'start', INK, True))
    o.append(T(tx + 64, ty + 196, 'pellet: clot and cells', 13, 'start', INK, True))
    o.append(T(tx + 64, ty + 214, '(denser than serum)', 12, 'start', MUT))
    o.append(L(tx + 25, ty + th + 10, tx + 25, ty + th + 34, AC, 2, arrow='n'))
    o.append(T(tx + 40, ty + th + 30, 'outward, away from the spindle', 12, 'start', MUT))
    o.append(boxt(16, 380, 334, 58, ['r = 15 cm at 2990 rpm', '1.118 × 10⁻⁵ × 15 × 2990² = 1500 × g'], size=13, bold_first=True, fill=ACS))
    o.append(boxt(370, 380, 334, 58, ['r = 7.5 cm at 2990 rpm', 'half the radius: 750 × g'], size=13, bold_first=True, fill=LVS, stroke=LV))
    return 450, ''.join(o)


FIG[7] = (f7, 'Top view of a swing-out rotor: r is measured from the spindle to the tube bottom. At 2990 rpm the 15 cm rotor gives 1500 × g, but the same speed '
              'on a 7.5 cm rotor gives only 750 × g. Right, a spun serum tube: cells and clot pellet outward, serum stays above, fat floats.',
          'Rotor seen from above with four tubes swung out to a dashed 15 centimetre circle, a smaller dashed 7.5 centimetre circle, an arrow for the '
          'radius to the tube bottom, a rotation arrow at 2990 rpm, and a side view of a tube with fat on top, serum above and the pellet at the bottom.')


# ---- ch8: GM tube counting circuit and the Geiger plateau ----
def f8():
    o = [R(40, 60, 300, 90, PANEL, INK, 44, 2.2)]
    o.append(L(40, 80, 40, 130, NX, 5))
    o.append(T(36, 172, 'thin window', 12, 'start', NX))
    o.append(L(80, 105, 330, 105, AC, 2.2))
    o.append(T(190, 96, 'anode wire (+)', 12, fill=AC))
    o.append(T(190, 140, 'argon + halogen quench gas', 12, fill=MUT))
    o.append(T(330, 172, 'cathode wall', 12, 'end', MUT))
    o.append(L(4, 80, 36, 100, LV, 2, arrow='l'))
    o.append(T(6, 70, 'γ or β', 12, 'start', LV))
    for x, y in ((120, 110), (150, 112), (165, 101), (210, 109), (240, 102)):
        o.append(T(x, y + 4, '+', 12, fill=LV, bold=True))
    o.append(L(330, 105, 380, 105, INK, 2))
    o.append(R(370, 50, 20, 40, PANEL, INK, 2, 1.8))
    o.append(L(380, 50, 380, 38, INK, 2))
    o.append(boxt(330, 10, 140, 28, ['+425 V supply'], size=12, bold_first=True))
    o.append(T(398, 74, 'R', 12, 'start', MUT))
    o.append(L(380, 90, 380, 105, INK, 2))
    o.append(L(380, 105, 420, 105, INK, 2))
    o.append(L(420, 92, 420, 118, INK, 2)); o.append(L(428, 92, 428, 118, INK, 2))
    o.append(L(428, 105, 448, 105, AC, 2, arrow='n'))
    o.append(boxt(450, 80, 122, 50, ['amplifier', 'discriminator'], size=12, bold_first=True))
    o.append(L(574, 105, 592, 105, AC, 2, arrow='n'))
    o.append(boxt(594, 80, 116, 50, ['scaler', '12 000 in 300 s'], size=12, bold_first=True, fill=ACS))
    o.append(L(190, 150, 190, 170, INK, 2)); o.append(L(176, 170, 204, 170, INK, 2)); o.append(L(182, 176, 198, 176, INK, 2))
    o.append(T(560, 160, 'one ≈ 1 V pulse per event,', 12, fill=MUT))
    o.append(T(560, 176, 'whatever its energy', 12, fill=MUT))
    # plateau
    x0, x1, y0, y1 = 100, 640, 230, 410
    fx = lambda v: x0 + (x1 - x0) * (v - 250) / 400
    fy = lambda r: y1 - (y1 - y0) * r / 60
    o.append(axes(x0, x1, y0, y1, [250, 300, 350, 400, 450, 500, 550, 600, 650], [0, 20, 40, 60], fx, fy,
                  'tube voltage (V)', 'count rate (counts/s)'))
    def rate(v):
        if v < 300: return 0
        if v < 350: return 38 * (v - 300) / 50
        if v < 500: return 38 + 3 * (v - 350) / 150
        return 41 + 0.5 * (v - 500) + 0.004 * (v - 500) ** 2
    o.append(P([(fx(v), fy(rate(v))) for v in range(250, 531, 5)], AC, 2.6))
    o.append(L(fx(350), fy(48), fx(500), fy(48), INK, 1.4))
    o.append(L(fx(350), fy(45), fx(350), fy(51), INK, 1.4)); o.append(L(fx(500), fy(45), fx(500), fy(51), INK, 1.4))
    o.append(Tb(fx(425), fy(48) - 8, 'Geiger plateau 350–500 V', 13))
    o.append(C(fx(425), fy(rate(425)), 6, LV))
    o.append(Tb(fx(425), fy(rate(425)) + 22, 'operating point 425 V', 12, 'middle', LV))
    o.append(Tb(fx(538), fy(50), 'continuous discharge', 12, 'start', MUT))
    o.append(Tb(fx(256), fy(7), 'below threshold', 12, 'start', MUT))
    return 460, ''.join(o)


FIG[8] = (f8, 'A Geiger–Müller tube: each ionising event starts an avalanche at the anode wire and gives one pulse of about 1 V, which the scaler counts '
              '(12 000 counts in 300 s in worked example 1). Below, count rate against voltage: the tube is run in the middle of the flat Geiger plateau, here 425 V.',
          'Cylindrical tube with a thin window, an axial anode wire fed from a 425 volt supply through a resistor, a capacitor to an amplifier and '
          'scaler, and below a curve of count rate against voltage rising at 300 volts, flat from 350 to 500 volts and rising again above.')


AFTER = {1: 3, 2: 2, 3: 2, 4: 2, 5: 3, 6: 2, 7: 1, 8: 1}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'after_section': AFTER[k], 'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
