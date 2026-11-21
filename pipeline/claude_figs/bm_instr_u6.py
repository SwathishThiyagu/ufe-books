"""Claude's hand-drawn figures for bm-instr-u6 (patient safety and sensory diagnostic equipment), one per chapter.
Every number comes from that chapter's worked examples. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
AFTER = {1: 1, 2: 2, 3: 2, 4: 2, 5: 3, 6: 1, 7: 1, 8: 1}


def sb(base, s, size=11):
    return f'{base}<tspan baseline-shift="sub" font-size="{size}">{s}</tspan>'


def res_h(x1, x2, y, c=INK, n=6, amp=7):
    xm1, xm2 = x1 + (x2 - x1) * 0.25, x2 - (x2 - x1) * 0.25
    pts = [(x1, y), (xm1, y)]
    for i in range(n):
        pts.append((xm1 + (xm2 - xm1) * (i + 0.5) / n, y + (amp if i % 2 == 0 else -amp)))
    pts += [(xm2, y), (x2, y)]
    return P(pts, c, 1.8)


def res_v(x, ytop, ybot, c=INK, n=6, amp=7):
    ym1, ym2 = ytop + (ybot - ytop) * 0.25, ybot - (ybot - ytop) * 0.25
    pts = [(x, ytop), (x, ym1)]
    for i in range(n):
        pts.append((x + (amp if i % 2 == 0 else -amp), ym1 + (ym2 - ym1) * (i + 0.5) / n))
    pts += [(x, ym2), (x, ybot)]
    return P(pts, c, 1.8)


def dot(x, y, c=INK):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" style="fill:{c}"/>'


def chain(x0, y, items, w, h=56, gap=22, fills=None, strokes=None, size=13):
    o = []
    for i, lines in enumerate(items):
        x = x0 + i * (w + gap)
        f = fills[i] if fills else PANEL
        s = strokes[i] if strokes else AC
        o.append(boxt(x, y, w, h, lines, f, s, size, bold_first=True))
        if i:
            o.append(L(x - gap, y + h / 2, x - 2, y + h / 2, AC, 2, arrow='n'))
    return ''.join(o)


# ---- 6.1 the audiogram and the dB HL to pressure example ----
def f1():
    o = [T(20, 24, 'Audiogram: frequency on a log scale, 0 dB HL at the top, loss plotted downward', 15, 'start', bold=True)]
    fr = [125, 250, 500, 1000, 2000, 4000, 8000]
    lab = ['125', '250', '500', '1k', '2k', '4k', '8k']
    x0, x1, y0, y1 = 80, 440, 66, 340
    fx = lambda f: x0 + math.log2(f / 125) / 6 * (x1 - x0)
    fy = lambda d: y0 + (d + 10) / 130 * (y1 - y0)
    # normal band
    o.append(R(x0, fy(-10), x1 - x0, fy(20) - fy(-10), ACS, ACS, 0, 1))
    o.append(T(x1 - 6, fy(14), 'normal: −10 to 20 dB HL', 12, 'end', AC, bold=True))
    for d in range(-10, 121, 10):
        o.append(L(x0, fy(d), x1, fy(d), L2, 1))
        o.append(T(x0 - 8, fy(d) + 4, str(d), 11, 'end', MUT))
    for f, s in zip(fr, lab):
        o.append(L(fx(f), y0, fx(f), y1, L2, 1))
        o.append(T(fx(f), y0 - 8, s, 12, fill=MUT))
    o.append(R(x0, y0, x1 - x0, y1 - y0, 'none', INK, 0, 1.4))
    o.append(T((x0 + x1) / 2, y1 + 22, 'frequency (Hz), each step one octave', 12, fill=MUT))
    o.append(f'<text x="26" y="{(y0 + y1) / 2:.1f}" font-size="12" text-anchor="middle" style="fill:var(--muted)" transform="rotate(-90 26 {(y0 + y1) / 2:.1f})">hearing level (dB HL)</text>')
    # patient air conduction, right ear (O)
    pts = [(250, 20), (500, 35), (1000, 45), (2000, 55), (4000, 60)]
    o.append(P([(fx(f), fy(d)) for f, d in pts], LV, 2.2))
    for f, d in pts:
        o.append(f'<circle cx="{fx(f):.1f}" cy="{fy(d):.1f}" r="6" style="fill:var(--fig);stroke:var(--live);stroke-width:2.2"/>')
    o.append(T(fx(2000), fy(80), 'O = right ear, air', 12, 'middle', LV, bold=True))
    # pure tone average
    o.append(L(fx(500), fy(45), fx(2000), fy(45), NX, 1.6, '5 4'))
    o.append(Tb(x0 + 12, fy(100), 'dashed: PTA (500, 1k, 2k) = 135 ÷ 3 = 45 dB HL', 12, 'start', NX, bold=True))
    # the worked example point
    o.append(L(fx(1000), fy(60) - 6, fx(1000), fy(60) + 6, AC, 2)); o.append(L(fx(1000) - 6, fy(60), fx(1000) + 6, fy(60), AC, 2))
    o.append(Tb(fx(1000) - 10, fy(60) + 4, 'example: 60 dB HL', 12, 'end', AC, bold=True))
    # right panel
    o.append(boxt(470, 66, 240, 104, ['Symbols', 'O right air    X left air', '&lt; right bone    &gt; left bone', 'gap between air and bone = conductive'], PANEL, INK, 12, bold_first=True))
    o.append(boxt(470, 186, 240, 150, ['60 dB HL at 1 kHz', 'insert earphone, 0 dB HL = 20 µPa', '20 µPa × 10^(60/20) = 20 mPa', 'TDH-39, 0 dB HL = 7 dB SPL', '60 + 7 = 67 dB SPL', '20 µPa × 10^(67/20) = 44.8 mPa'], LVS, LV, 12, bold_first=True))
    return 374, ''.join(o)
FIG[1] = (f1, 'An audiogram with frequency in octaves from 125 Hz to 8 kHz and hearing level increasing downward. The right-ear air-conduction thresholds of the pure-tone average question (35, 45 and 55 dB HL at 500 Hz, 1 kHz and 2 kHz) average 45 dB HL; the worked example turns 60 dB HL at 1 kHz into 20 mPa for an insert earphone and 44.8 mPa for a TDH-39.',
          'Audiogram grid from minus 10 to 120 decibels hearing level downward and 125 hertz to 8 kilohertz across, a shaded normal band to 20 decibels, a right-ear air-conduction line of circles from 20 decibels at 250 hertz down to 60 decibels at 4 kilohertz, a dashed pure-tone average at 45, a cross at 60 decibels at 1 kilohertz, a symbol key and a box converting 60 decibels hearing level into 20 and 44.8 millipascals.')


# ---- 6.2 the flexible endoscope: two bundles, total internal reflection, the core area example ----
def f2():
    o = [T(20, 24, 'Flexible endoscope: an incoherent light bundle out, a coherent image bundle back', 15, 'start', bold=True)]
    o.append(boxt(20, 50, 120, 52, ['Light source', 'LED or xenon'], NXS, NX, 12, bold_first=True))
    o.append(boxt(20, 120, 120, 52, ['Eyepiece', 'or camera'], ACS, AC, 12, bold_first=True))
    # insertion tube
    o.append(R(170, 80, 440, 66, PANEL, INK, 30, 1.6))
    o.append(L(140, 76, 180, 96, NX, 3)); o.append(L(180, 96, 600, 96, NX, 5))
    o.append(L(140, 146, 180, 130, AC, 3)); o.append(L(180, 130, 600, 130, AC, 5))
    o.append(T(390, 90, 'illumination bundle: fibres in random order', 12, fill=NX, bold=True))
    o.append(T(390, 124, 'image bundle: same fibre order at both ends', 12, fill=AC, bold=True))
    o.append(T(390, 166, 'insertion tube with suction and biopsy channel, steering wires', 12, fill=MUT))
    # tip, lens, tissue
    o.append(f'<ellipse cx="616" cy="130" rx="6" ry="14" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:1.8"/>')
    o.append(T(616, 66, 'objective lens', 12, fill=MUT))
    o.append(L(616, 72, 616, 112, MUT, 1, '3 3'))
    o.append(P([(690, 60), (676, 90), (688, 120), (674, 150), (690, 180)], LV, 3))
    o.append(T(700, 194, 'tissue', 12, 'end', LV, bold=True))
    o.append(L(604, 96, 668, 104, NX, 1.6, arrow='x')); o.append(L(668, 136, 626, 132, AC, 1.6, arrow='n'))
    # inset a: total internal reflection
    ya = 220
    o.append(T(20, ya - 6, 'One fibre: total internal reflection', 13, 'start', bold=True))
    o.append(R(20, ya + 8, 250, 64, NXS, NX, 4, 1.4))
    o.append(R(20, ya + 22, 250, 36, PANEL, AC, 0, 1.4))
    o.append(T(275, ya + 44, sb('core n', '1') + ' = 1.50', 11, 'start', AC, bold=True))
    o.append(T(275, ya + 18, sb('cladding n', '2') + ' = 1.47', 11, 'start', NX))
    zz = [(26, ya + 40), (62, ya + 23), (110, ya + 57), (158, ya + 23), (206, ya + 57), (254, ya + 23)]
    o.append(P(zz, LV, 1.8))
    o.append(T(20, ya + 92, 'sin θc = 1.47 ÷ 1.50 = 0.98, θc ≈ 78°', 12, 'start'))
    o.append(T(20, ya + 110, 'rays nearly along the fibre are trapped', 12, 'start', MUT))
    # inset b: coherent versus incoherent faces
    xb = 384
    o.append(T(xb, ya - 6, 'Bundle faces: tip and handle', 13, 'start', bold=True))
    def face(x, y, order, c):
        out = []
        for i, v in enumerate(order):
            cx, cy = x + (i % 3) * 18, y + (i // 3) * 18
            out.append(R(cx, cy, 16, 16, PANEL, c, 3, 1.2)); out.append(T(cx + 8, cy + 12, str(v), 10, fill=c, bold=True))
        return ''.join(out)
    o.append(face(xb, ya + 14, range(1, 10), AC)); o.append(L(xb + 56, ya + 41, xb + 74, ya + 41, AC, 1.6, arrow='n')); o.append(face(xb + 78, ya + 14, range(1, 10), AC))
    o.append(T(xb + 66, ya + 86, 'image: order kept', 12, fill=AC, bold=True))
    o.append(face(xb + 168, ya + 14, range(1, 10), NX)); o.append(L(xb + 224, ya + 41, xb + 242, ya + 41, NX, 1.6, arrow='x')); o.append(face(xb + 246, ya + 14, [7, 3, 9, 1, 5, 8, 4, 2, 6], NX))
    o.append(T(xb + 234, ya + 86, 'light: order mixed', 12, fill=NX, bold=True))
    o.append(T(xb + 30, ya + 102, 'tip', 11, fill=MUT)); o.append(T(xb + 104, ya + 102, 'handle', 11, fill=MUT))
    o.append(T(xb + 196, ya + 102, 'tip', 11, fill=MUT)); o.append(T(xb + 274, ya + 102, 'handle', 11, fill=MUT))
    # sum box
    o.append(boxt(20, 352, 690, 50, ['Image bundle: 10,000 fibres, 30 µm cores   ·   one core π × (15 µm)² = 707 µm²   ·   all cores 707 × 10,000 µm² = 7.07 mm²',
                                     'thicker cores give more light but a coarser mosaic: points closer than one fibre merge'], LVS, LV, 12))
    return 416, ''.join(o)
FIG[2] = (f2, 'The two bundles of a flexible endoscope. The illumination bundle needs no order; the image bundle keeps every fibre in the same place at both ends, so the picture survives. Light stays in each fibre by total internal reflection (θc ≈ 78° for indices 1.50 and 1.47), and the worked example gives 707 µm² per 30 µm core and 7.07 mm² for 10,000 fibres.',
          'Diagram of a light source and an eyepiece feeding an insertion tube that holds an illumination bundle and an image bundle, ending at an objective lens facing tissue; an inset of a fibre core and cladding with a zigzag ray; two numbered three-by-three bundle faces showing the same order at both ends for the image bundle; and a box with the 707 square micrometre and 7.07 square millimetre core areas.')


# ---- 6.3 the dental tube head, cone and the inverse-square example ----
def f3():
    o = [T(20, 24, 'Dental X-ray tube head and cone, with the worked example', 15, 'start', bold=True)]
    # housing
    o.append(R(20, 44, 300, 140, PANEL, INK, 10, 3))
    o.append(T(170, 62, 'lead-lined head filled with insulating oil', 12, fill=MUT))
    o.append(f'<ellipse cx="170" cy="118" rx="118" ry="28" style="fill:var(--fig);stroke:var(--accent);stroke-width:1.8"/>')
    o.append(Tb(150, 176, 'evacuated glass tube', 11, 'middle', AC))
    # cathode filament
    o.append(P([(64, 106), (68, 130), (72, 106), (76, 130), (80, 106), (84, 130), (88, 106)], LV, 1.8))
    o.append(T(66, 160, 'filament', 11, fill=LV, bold=True))
    o.append(L(92, 118, 196, 118, LV, 2, arrow='l')); o.append(T(144, 110, 'electrons', 11, fill=LV))
    # anode
    o.append(R(222, 104, 50, 28, NXS, NX, 2, 1.6)); o.append(P([(204, 106), (222, 104), (222, 132), (214, 132), (204, 106)], NX, 1.6, fill='var(--next)'))
    o.append(T(254, 86, 'copper anode', 11, fill=NX, bold=True)); o.append(Tb(250, 160, 'tungsten target', 11, 'middle', NX))
    # beam down
    o.append(R(186, 186, 48, 6, MUT, MUT, 1, 1)); o.append(T(180, 194, 'Al filter', 11, 'end', MUT))
    o.append(R(176, 200, 68, 98, ACS, AC, 4, 1.8)); o.append(T(172, 246, 'cone', 12, 'end', AC, bold=True)); o.append(T(172, 262, '(PID)', 11, 'end', AC))
    o.append(P([(210, 126), (192, 294), (228, 294), (210, 126)], LV, 1.2, '4 3', fill='var(--live-soft)', op=0.5))
    o.append(L(140, 312, 300, 312, INK, 2.4)); o.append(T(304, 316, 'skin', 12, 'start', bold=True))
    o.append(L(192, 302, 228, 302, LV, 1.4)); o.append(T(210, 332, 'beam ≤ 6 cm at the skin', 11, fill=LV, bold=True))
    o.append(L(268, 118, 268, 312, INK, 1.2, '3 3')); o.append(L(262, 312, 274, 312, INK, 1.2))
    o.append(Tb(274, 236, 'focus to skin', 11, 'start')); o.append(Tb(274, 252, '≥ 20 cm', 11, 'start', bold=True))
    o.append(boxt(20, 214, 112, 82, ['Timer', '0.01 s steps', 'dead-man switch', 'on a long cord'], PANEL, INK, 11, bold_first=True))
    # inverse square
    sx, sy = 372, 156
    o.append(T(372, 60, 'Inverse square: double the distance, quarter the dose', 13, 'start', bold=True))
    o.append(C(sx, sy, 6, LV))
    o.append(P([(sx, sy), (692, sy - 64), (692, sy + 64), (sx, sy)], LV, 1, '4 3', fill='var(--live-soft)', op=0.4))
    o.append(R(526, sy - 32, 10, 64, ACS, AC, 2, 1.6)); o.append(R(686, sy - 64, 10, 128, NXS, NX, 2, 1.6))
    o.append(T(531, sy + 52, '20 cm', 12, fill=AC, bold=True)); o.append(T(691, sy + 82, '40 cm', 12, fill=NX, bold=True))
    o.append(T(531, sy - 40, 'area 1', 11, fill=AC)); o.append(T(676, sy - 72, 'area 4', 11, 'end', NX))
    o.append(T(470, 270, sb('I', '2') + ' / ' + sb('I', '1') + ' = (20 ÷ 40)² = 1/4', 13, 'middle', NX, bold=True))
    o.append(boxt(352, 288, 360, 88, ['70 kVp, 7 mA, 0.6 s', 'exposure 7 × 0.6 = 4.2 mAs', 'λmin = 1.24 ÷ 70 = 0.0177 nm', 'in 70 kV × 7 mA × 0.6 s = 294 J · X-rays 0.57 % = 1.7 J'], LVS, LV, 12, bold_first=True))
    return 390, ''.join(o)
FIG[3] = (f3, 'The tube head: a heated filament sends electrons to a tungsten target in a copper anode, and the beam leaves through the aluminium filter and the cone, at least 20 cm from focus to skin and no wider than 6 cm. The worked example gives 4.2 mAs, a shortest wavelength of 0.0177 nm, 294 J in and 1.7 J out as X-rays; doubling the cone length from 20 to 40 cm quarters the skin dose.',
          'Cross-section of a lead-lined oil-filled tube head with filament, electron stream and anode target, the beam passing through an aluminium filter and a cone to the skin with the 20 centimetre distance and 6 centimetre beam marked, a timer box, a point source spreading onto plates at 20 and 40 centimetres with areas 1 and 4, and a box of the exposure numbers.')


# ---- 6.4 the effects ladder on a log current scale, with the three currents of the example ----
def f4():
    o = [T(20, 24, 'Current through the body decides the harm: the effects ladder at 50 Hz', 15, 'start', bold=True)]
    ax = 100
    fy = lambda amps: 380 - 50 * (math.log10(amps) + 6)
    o.append(L(ax, fy(1), ax, fy(1e-6), INK, 2))
    for a, s in [(1e-6, '1 µA'), (1e-5, '10 µA'), (1e-4, '100 µA'), (1e-3, '1 mA'), (1e-2, '10 mA'), (1e-1, '100 mA'), (1, '1 A')]:
        o.append(L(ax - 6, fy(a), ax, fy(a), INK, 2)); o.append(T(ax - 10, fy(a) + 4, s, 12, 'end', MUT))
    o.append(f'<text x="22" y="230" font-size="12" text-anchor="middle" style="fill:var(--muted)" transform="rotate(-90 22 230)">current (log scale)</text>')
    o.append(R(ax, fy(1), 14, fy(0.1) - fy(1), LV, LV, 0, 1)); o.append(R(ax, fy(0.1), 14, fy(0.01) - fy(0.1), LVS, LV, 0, 1))
    o.append(R(ax, fy(1e-4), 14, fy(1e-5) - fy(1e-4), NXS, NX, 0, 1))
    rows = [(0.1, '100 mA hand to hand: ventricular fibrillation', LV), (0.01, '10–15 mA: let-go limit, muscles lock', LV),
            (1e-3, '1 mA: threshold of perception', INK), (1e-4, '≈ 100 µA into the heart: micro-shock fibrillation', NX),
            (1e-5, '10 µA: type CF patient-leakage limit', NX)]
    for a, s, c in rows:
        o.append(L(ax + 14, fy(a), ax + 26, fy(a), c, 1.4)); o.append(T(ax + 30, fy(a) + 4, s, 12, 'start', c, bold=True))
    o.append(T(ax + 30, fy(3e-3) + 4, 'macro-shock: current enters and leaves through the skin', 11, 'start', MUT))
    o.append(T(ax + 30, fy(3e-5) + 4, 'micro-shock: a catheter or pacing wire bypasses the skin', 11, 'start', MUT))
    # examples
    ex = [(0.23, 'Wet skin 1 kΩ', '230 V ÷ 1 kΩ = 230 mA', 'above 100 mA: fibrillation', LV),
          (0.023, 'Dry skin 10 kΩ', '230 V ÷ 10 kΩ = 23 mA', 'above let-go, below 100 mA', LV),
          (2e-4, 'Catheter 500 Ω, 0.1 V', '0.1 V ÷ 500 Ω = 200 µA', '20 × the 10 µA limit', NX)]
    by = [40, 118, 214]
    for (a, t1, t2, t3, c), y in zip(ex, by):
        o.append(P([(ax + 7, fy(a)), (452, fy(a)), (474, y + 32)], c, 1.3, '4 3'))
        o.append(f'<circle cx="{ax + 7:.1f}" cy="{fy(a):.1f}" r="6" style="fill:var(--fig);stroke:{c};stroke-width:3"/>')
        o.append(boxt(474, y, 236, 64, [t1, t2, t3], LVS if c == LV else NXS, c, 12, bold_first=True))
    return 392, ''.join(o)
FIG[4] = (f4, 'The effects of 50 Hz current on a log scale from 1 µA to 1 A, with the three currents of the worked example: 230 V across wet skin (1 kΩ) drives 230 mA, past the 100 mA fibrillation level; across dry skin (10 kΩ) 23 mA, past the let-go limit; and 0.1 V across a 500 Ω catheter path drives 200 µA straight into the heart, twenty times the 10 µA type CF limit.',
          'Vertical log scale of current from 1 microampere to 1 ampere with labelled levels at 10 microamperes, about 100 microamperes, 1 milliampere, 10 to 15 milliamperes and 100 milliamperes, and three dots at 230 milliamperes, 23 milliamperes and 200 microamperes linked to boxes working out each current from voltage and resistance.')


# ---- 6.5 the test sequence with the ventilator readings and the CF monitor on the analyser ----
def f5():
    o = [T(20, 24, 'Safety test sequence with the worked examples', 15, 'start', bold=True)]
    items = [['Inspect', 'cord, plug,', 'fuses, spills'], ['Earth', '≤ 0.1 Ω', 'read 0.35 Ω', 'FAIL'], ['Insulation', '≥ 1 MΩ at 500 V', 'read 50 MΩ', 'pass'],
             ['Earth leakage', '≤ 5 mA', 'read 0.9 mA', 'pass'], ['Patient leakage', 'normal, then', 'earth open', '(single fault)']]
    o.append(chain(12, 44, items, 124, 88, 18, [PANEL, LVS, ACS, ACS, NXS], [INK, LV, AC, AC, NX], 12))
    o.append(T(20, 156, 'Ventilator: one failure is enough; remove it, repair the earth pin, repeat every test.', 12, 'start', LV, bold=True))
    # analyser circuit
    y0 = 196
    o.append(T(20, y0, 'Patient leakage on the analyser (type CF ECG monitor)', 13, 'start', bold=True))
    o.append(boxt(20, y0 + 18, 120, 70, ['ECG monitor', 'CF applied part'], PANEL, AC, 12, bold_first=True))
    o.append(L(140, y0 + 53, 190, y0 + 53, INK, 1.8)); o.append(T(165, y0 + 70, 'leads', 11, fill=MUT))
    o.append(res_h(190, 270, y0 + 53, NX)); o.append(T(230, y0 + 36, '1 kΩ measuring device', 11, fill=NX, bold=True))
    o.append(L(270, y0 + 53, 300, y0 + 53, INK, 1.8)); o.append(L(300, y0 + 53, 300, y0 + 110, INK, 1.8))
    for i, w in enumerate([24, 16, 8]):
        o.append(L(300 - w / 2, y0 + 110 + i * 5, 300 + w / 2, y0 + 110 + i * 5, INK, 1.8))
    o.append(T(312, y0 + 120, 'earth', 11, 'start', MUT))
    o.append(L(190, y0 + 53, 190, y0 + 84, MUT, 1.2)); o.append(L(270, y0 + 53, 270, y0 + 84, MUT, 1.2))
    o.append(L(190, y0 + 84, 214, y0 + 84, MUT, 1.2)); o.append(L(246, y0 + 84, 270, y0 + 84, MUT, 1.2))
    o.append(f'<circle cx="230" cy="{y0 + 84}" r="16" style="fill:var(--panel);stroke:var(--ink);stroke-width:1.6"/>'); o.append(T(230, y0 + 89, 'mV', 11, bold=True))
    o.append(T(20, y0 + 126, 'I = V ÷ 1 kΩ: 1 mV reads 1 µA', 11, 'start', MUT))
    o.append(boxt(20, y0 + 138, 136, 50, ['normal: 8 mV', '8 µA ≤ 10 µA pass'], ACS, AC, 12, bold_first=True))
    o.append(boxt(170, y0 + 138, 160, 50, ['earth open: 62 mV', '62 µA &gt; 50 µA FAIL'], LVS, LV, 12, bold_first=True))
    # limits table
    tx, ty = 360, y0 + 16
    o.append(T(tx, y0, 'Limits (normal / single fault)', 13, 'start', bold=True))
    rows = [('Earth leakage', '5 mA / 10 mA'), ('Enclosure', '100 µA / 500 µA'), ('Patient, type B and BF', '100 µA / 500 µA'), ('Patient, type CF', '10 µA / 50 µA')]
    for i, (a, b) in enumerate(rows):
        y = ty + i * 36
        c = NX if 'CF' in a else INK
        o.append(R(tx, y, 350, 32, NXS if 'CF' in a else PANEL, L2, 4, 1))
        o.append(T(tx + 10, y + 21, a, 12, 'start', c, bold=True)); o.append(T(tx + 340, y + 21, b, 12, 'end', c, bold=True))
    o.append(T(tx, ty + 166, 'CF: parts that may touch the heart directly', 11, 'start', MUT))
    return 396, ''.join(o)
FIG[5] = (f5, 'The test sequence with the ventilator readings of the first worked example: 0.35 Ω fails the 0.1 Ω earth limit while 50 MΩ and 0.9 mA pass, so the machine is withdrawn. Below, the analyser reads patient leakage as the voltage across a 1 kΩ measuring device: 8 mV is 8 µA and passes the 10 µA CF limit, but 62 mV with the earth open is 62 µA and fails the 50 µA single-fault limit.',
          'Chain of five test boxes: inspection, earth continuity failing at 0.35 ohm, insulation passing at 50 megohm, earth leakage passing at 0.9 milliampere and patient leakage; below, a monitor connected through a 1 kilohm measuring resistor to earth with a millivoltmeter across it, results of 8 microamperes passing and 62 microamperes failing, and a table of leakage limits for normal and single-fault conditions.')


# ---- 6.6 the risk-class rule chain with the seven devices of the examples ----
def f6():
    o = [T(20, 24, 'Risk class from the rule chain: seven devices from the worked examples', 15, 'start', bold=True)]
    qs = [('Long-term implant touching the heart,', 'central circulation or CNS, or life-sustaining?', 'D'),
          ('Long-term implant', '(more than 30 days in the body)?', 'C'),
          ('Invasive, short-term (60 min to 30 days)', 'or sterile single-use through the skin?', 'B'),
          ('Non-invasive, or through a body', 'opening for under 60 minutes', 'A')]
    cls = {'D': ('Class D, rank 4', 'pacemaker, coronary stent', LV, LVS), 'C': ('Class C, rank 3', 'bone screw', NX, NXS),
           'B': ('Class B, rank 2', 'syringe, urinary catheter (7 days)', AC, ACS), 'A': ('Class A, rank 1', 'tongue depressor, oral thermometer', INK, PANEL)}
    for i, (a, b, k) in enumerate(qs):
        y = 46 + i * 80
        last = (i == 3)
        o.append(boxt(20, y, 330, 56, [a, b], PANEL, INK if not last else MUT, 12, dash=None if not last else '5 4'))
        t, d, c, f = cls[k]
        o.append(L(350, y + 28, 412, y + 28, c, 2, arrow={LV: 'l', NX: 'x', AC: 'n', INK: 'm'}[c]))
        if not last:
            o.append(T(381, y + 20, 'yes', 11, fill=c, bold=True))
            o.append(L(185, y + 56, 185, y + 78, MUT, 1.6, arrow='m')); o.append(T(193, y + 72, 'no', 11, 'start', MUT, bold=True))
        else:
            o.append(T(381, y + 20, 'else', 11, fill=MUT, bold=True))
        o.append(boxt(416, y, 294, 56, [t, d], f, c, 12, bold_first=True))
    o.append(boxt(20, 372, 690, 40, ['Ranks 1, 2, 4 (first example) and 1, 2, 3, 4 (second): sum 17, mean 17 ÷ 7 = 2.43, between class B and class C'], PANEL, AC, 12))
    return 424, ''.join(o)
FIG[6] = (f6, 'The rule chain the worked examples follow, asked from the highest risk down. A pacemaker and a coronary stent are class D, a bone screw class C, a syringe and a 7-day urinary catheter class B, and a tongue depressor and an oral thermometer class A; the seven evidence ranks sum to 17 and average 2.43.',
          'Four stacked questions from long-term implant touching the heart or nervous system, through long-term implant and short-term invasive use, to non-invasive or brief body-opening use, each with a yes arrow to class D, C, B or A and the example devices in that class, and a box giving the mean rank of 2.43.')


# ---- 6.7 the GSR trace of the worked example on a polygraph chart ----
def f7():
    o = [T(20, 24, 'Polygraph chart: the skin resistance channel of the worked example', 15, 'start', bold=True)]
    x0, x1 = 120, 560
    o.append(R(x0, 44, x1 - x0, 296, PANEL, L2, 4, 1))
    for xx in range(x0, x1 + 1, 40):
        o.append(L(xx, 44, xx, 340, L2, 0.8))
    tq = 240
    fx = lambda t: x0 + t * 20  # 20 px per second, 0..22 s
    # question marker
    o.append(L(fx(5), 44, fx(5), 340, NX, 1.6, '5 4')); o.append(Tb(fx(5), 60, 'question', 12, 'middle', NX, bold=True))
    # respiration
    yr = 100
    o.append(P([(fx(t / 4), yr + 14 * math.sin(t / 4 * 2 * math.pi / 4)) for t in range(0, 89)], AC, 1.8))
    o.append(T(x0 - 8, yr + 4, 'respiration', 12, 'end', AC, bold=True))
    # pulse / BP
    yp = 168
    pts = []
    for t in range(0, 221):
        s = t / 10
        ph = (s % 0.85) / 0.85
        v = -14 * math.exp(-((ph - 0.15) / 0.06) ** 2) - 5 * math.exp(-((ph - 0.45) / 0.08) ** 2)
        pts.append((fx(s), yp + v + (0 if s < 6 else -4)))
    o.append(P(pts, LV, 1.6)); o.append(T(x0 - 8, yp + 4, 'pulse and BP', 12, 'end', LV, bold=True))
    # GSR: resistance plot, higher resistance up
    fr = lambda k: 330 - (k - 110) * 2.4   # 110 kΩ at 330, 160 kΩ at 210
    def R_t(s):
        if s < 6.5: return 150
        if s < 9: return 150 - 30 * (s - 6.5) / 2.5
        return 120 + 30 * (1 - math.exp(-(s - 9) / 4.5))
    o.append(P([(fx(s / 10), fr(R_t(s / 10))) for s in range(0, 221)], NX, 2.6))
    o.append(T(x0 - 8, fr(140) + 4, 'GSR', 12, 'end', NX, bold=True)); o.append(T(x0 - 8, fr(140) + 20, '(resistance)', 11, 'end', MUT))
    o.append(L(fx(0), fr(150), fx(22), fr(150), MUT, 1, '3 3')); o.append(Tb(fx(1.5), fr(150) - 8, 'BSR 150 kΩ', 12, 'middle', INK, bold=True))
    o.append(L(fx(9), fr(120), fx(13), fr(120), MUT, 1, '3 3')); o.append(T(fx(13) + 4, fr(120) + 4, '120 kΩ', 12, 'start', NX, bold=True))
    o.append(L(fx(9), fr(150), fx(9), fr(123), NX, 1.6, arrow='x')); o.append(Tb(fx(9) + 8, fr(140), '30 kΩ', 11, 'start', NX, bold=True))
    o.append(brace(fx(5), fx(6.5), fr(150) - 22, MUT, True)); o.append(Tb(fx(5.75), fr(150) - 30, 'latency 1–3 s', 11, 'middle', MUT))
    o.append(T((x0 + x1) / 2, 358, 'time: one grid square = 2 s', 12, fill=MUT))
    o.append(boxt(574, 44, 138, 296, ['Worked example', 'I = 10 µA', 'rest 1.5 V', '1.5 ÷ 10 µA', '= 150 kΩ', 'after 1.2 V', '= 120 kΩ', 'fall 30 kΩ, 20 %', 'conductance', '6.67 → 8.33 µS', 'rise 1.67 µS, 25 %'], NXS, NX, 12, bold_first=True))
    return 372, ''.join(o)
FIG[7] = (f7, 'A polygraph chart with respiration, pulse and skin resistance. After the question, skin resistance stays at the 150 kΩ basal value for a latency of about 1–3 s, falls to 120 kΩ (a 30 kΩ or 20 % fall) and recovers slowly. As conductance the same response is 6.67 to 8.33 µS, a 25 % rise.',
          'Chart with three traces against time: a slow respiration wave, a pulse wave and a skin resistance line at 150 kilohms that drops to 120 kilohms a few seconds after a dashed question marker and slowly recovers, with the latency and the 30 kilohm fall marked, and a side box of the worked example from 10 microamperes and 1.5 and 1.2 volts.')


# ---- 6.8 Goldmann applanation: prism, mires and the pressure example ----
def f8():
    o = [T(20, 24, 'Goldmann applanation tonometry: pressure = force ÷ flattened area', 15, 'start', bold=True)]
    # cornea and prism
    cx, cy = 190, 220
    o.append(f'<path d="M{cx - 150},{cy + 90} Q{cx},{cy - 150} {cx + 150},{cy + 90}" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2"/>')
    o.append(L(cx - 34, cy - 30, cx + 34, cy - 30, INK, 3))
    o.append(R(cx - 34, cy - 130, 68, 100, PANEL, INK, 6, 2))
    o.append(T(cx, cy - 84, 'prism', 12, bold=True)); o.append(T(cx, cy - 68, 'tip', 12, bold=True))
    o.append(L(cx, cy - 170, cx, cy - 134, LV, 2.6, arrow='l')); o.append(T(cx + 10, cy - 154, 'F = 20 mN', 13, 'start', LV, bold=True))
    o.append(T(cx + 10, cy - 138, 'from the force knob', 11, 'start', MUT))
    o.append(L(cx - 34, cy - 14, cx + 34, cy - 14, NX, 1.4)); o.append(L(cx - 34, cy - 20, cx - 34, cy - 8, NX, 1.4)); o.append(L(cx + 34, cy - 20, cx + 34, cy - 8, NX, 1.4))
    o.append(T(cx, cy + 6, 'd = 3.06 mm', 12, fill=NX, bold=True))
    o.append(T(cx, cy + 50, 'cornea', 12, fill=AC, bold=True)); o.append(T(cx, cy + 68, 'intra-ocular pressure pushes out', 11, fill=MUT))
    o.append(T(cx - 150, cy + 108, 'fluorescein stains the tear film; blue light shows the mires', 11, 'start', MUT))
    # mires
    mx, my, r = 430, 118, 34
    o.append(T(515, 56, 'Mires seen through the prism', 13, 'middle', bold=True))
    def mires(x, dx):
        top = f'<path d="M{x - dx - r},{my} A{r},{r} 0 0 1 {x - dx + r},{my}" style="fill:none;stroke:var(--next);stroke-width:7"/>'
        bot = f'<path d="M{x + dx - r},{my} A{r},{r} 0 0 0 {x + dx + r},{my}" style="fill:none;stroke:var(--next);stroke-width:7"/>'
        return top + bot
    o.append(mires(mx, 46)); o.append(T(mx, my + 62, 'too little force: apart', 11, fill=MUT))
    o.append(mires(mx + 170, r - 3.5)); o.append(T(mx + 170, my + 62, 'inner edges touch: read', 11, fill=NX, bold=True))
    # sum
    o.append(boxt(372, 214, 338, 150, ['Worked example', 'A = π × (1.53 mm)² = 7.35 mm²', 'P = 0.020 N ÷ 7.35 × 10⁻⁶ m² = 2721 Pa', '2721 ÷ 133.3 = 20.4 mmHg', 'normal about 10–21 mmHg', 'at 3.06 mm, 1 g (9.81 mN) reads 10 mmHg'], LVS, LV, 12, bold_first=True))
    return 378, ''.join(o)
FIG[8] = (f8, 'The Goldmann prism flattens a 3.06 mm circle of cornea. At that size the bending of the cornea and the pull of the tear film cancel, so pressure is force over area: 20 mN on 7.35 mm² gives 2721 Pa, 20.4 mmHg; each 1 g of force reads 10 mmHg. The split mires are read when their inner edges just touch.',
          'Side view of a prism tip pressed on the cornea with a 20 millinewton force arrow and the 3.06 millimetre flattened diameter, two pairs of semicircular mires before and at the end point, and a box working the area, the pressure in pascals and the 20.4 millimetres of mercury reading.')


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'caption': cap, 'after_section': AFTER[k], 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
