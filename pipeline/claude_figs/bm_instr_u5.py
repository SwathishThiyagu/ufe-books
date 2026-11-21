"""Claude's hand-drawn figures for bm-instr-u5 (therapeutic equipment), one per chapter.
Every number comes from that chapter's worked examples. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
AFTER = {1: 2, 2: 2, 3: 3, 4: 1, 5: 2, 6: 1, 7: 2, 8: 1, 9: 2}


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


def cap_v(x, ytop, ybot, c=INK, w=24):
    ym = (ytop + ybot) / 2
    return (L(x, ytop, x, ym - 5, c, 1.8) + L(x, ym + 5, x, ybot, c, 1.8)
            + L(x - w / 2, ym - 5, x + w / 2, ym - 5, c, 3) + L(x - w / 2, ym + 5, x + w / 2, ym + 5, c, 3))


def ind_h(x1, x2, y, c=INK, n=4):
    w = (x2 - x1) / n
    d = f'M{x1:.1f},{y:.1f} ' + ' '.join(f'a{w / 2:.1f},{w / 2:.1f} 0 0 1 {w:.1f},0' for _ in range(n))
    return f'<path d="{d}" style="fill:none;stroke:{c};stroke-width:1.8"/>'


def dot(x, y, c=INK):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" style="fill:{c}"/>'


def chain(x0, y, items, w, h=56, gap=22, fills=None, size=13):
    o = []
    for i, lines in enumerate(items):
        x = x0 + i * (w + gap)
        f = fills[i] if fills else PANEL
        o.append(boxt(x, y, w, h, lines, f, AC, size, bold_first=True))
        if i:
            o.append(L(x - gap, y + h / 2, x - 2, y + h / 2, AC, 2, arrow='n'))
    return ''.join(o)


# ---- 5.1 the DC defibrillator of the worked example and its discharge ----
def f1():
    o = [T(20, 24, 'DC defibrillator: 32 µF charged to 5000 V stores 400 J', 15, 'start', bold=True)]
    top, bot = 70, 190
    # charger
    o.append(boxt(20, 92, 120, 76, ['Charger', 'step-up and', 'rectifier'], PANEL, AC, 13, bold_first=True))
    o.append(L(140, top + 40, 170, top + 40, INK, 1.8)); o.append(L(170, top, 170, top + 40, INK, 1.8))
    o.append(L(170, top, 190, top, INK, 1.8)); o.append(res_h(190, 250, top)); o.append(T(220, top - 14, 'charging R', 12, fill=MUT))
    o.append(L(140, top + 80, 170, top + 80, INK, 1.8)); o.append(L(170, top + 80, 170, bot, INK, 1.8))
    o.append(L(250, top, 290, top, INK, 1.8)); o.append(dot(290, top))
    # capacitor
    o.append(cap_v(290, top, bot, AC, 30)); o.append(T(312, 126, 'C = 32 µF', 13, 'start', AC, bold=True)); o.append(T(312, 143, 'V = 5000 V', 13, 'start', AC, bold=True))
    o.append(L(170, bot, 290, bot, INK, 1.8)); o.append(dot(290, bot))
    # switch
    o.append(L(290, top, 400, top, INK, 1.8)); o.append(C(400, top, 3.5, INK))
    o.append(L(400, top, 438, top - 18, INK, 2)); o.append(C(442, top, 3.5, INK)); o.append(T(421, top - 26, 'discharge switch', 12, fill=MUT))
    # inductor + internal R
    o.append(L(442, top, 460, top, INK, 1.8)); o.append(ind_h(460, 520, top)); o.append(T(490, top - 16, 'L ≈ 50 mH', 12, fill=MUT))
    o.append(L(520, top, 530, top, INK, 1.8)); o.append(res_h(530, 590, top, NX)); o.append(T(560, top - 14, 'internal 10 Ω', 12, fill=NX, bold=True))
    o.append(L(590, top, 650, top, INK, 1.8)); o.append(L(650, top, 650, 98, INK, 1.8))
    o.append(R(620, 98, 60, 64, NXS, NX, 8)); o.append(T(650, 124, 'chest', 13, bold=True)); o.append(T(650, 142, '50 Ω', 13, bold=True))
    o.append(L(650, 162, 650, bot, INK, 1.8)); o.append(L(290, bot, 650, bot, INK, 1.8))
    o.append(T(612, 130, 'paddles', 12, 'end', MUT))
    # energy sums
    o.append(boxt(20, 214, 330, 92, ['E = ½ C V² = ½ × 32 µF × 5000² = 400 J', 'Q = C V = 0.16 C', 'to the chest: 50 ÷ (50 + 10) × 400 = 333 J'], LVS, LV, 13))
    # waveform
    x0, x1, y0, y1 = 410, 690, 222, 330
    fx = lambda t: x0 + t / 10 * (x1 - x0)
    fy = lambda i: y1 - i / 90 * (y1 - y0)
    o.append(L(x0, y1, x1, y1, L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    for t in (0, 5, 10):
        o.append(T(fx(t), y1 + 18, str(t), 12, fill=MUT))
    o.append(T((x0 + x1) / 2, y1 + 34, 'time (ms)', 12, fill=MUT))
    o.append(T(x0 + 6, y0 - 4, 'current (A)', 12, 'start', MUT))
    pts = []
    for i in range(101):
        t = i / 100 * 10
        v = 83 * math.exp(-t / 2.2) * math.sin(math.pi * min(t, 6) / 6) / 0.62 if t < 6 else 0
        pts.append((fx(t), fy(max(0, min(v, 86)))))
    o.append(P(pts, AC, 2.6))
    o.append(T(fx(4.6), fy(62), 'damped half-sine', 12, 'start', AC, bold=True))
    o.append(T(fx(4.6), fy(46), 'about 5 ms', 12, 'start', MUT))
    o.append(T(fx(4.6), fy(30), 'peak below 5000 ÷ 60 = 83 A', 12, 'start', MUT))
    return 368, ''.join(o)
FIG[1] = (f1, 'The worked example\'s defibrillator: the charger fills a 32 µF capacitor to 5000 V (400 J, 0.16 C); the switch then empties it through the inductor and 10 Ω of internal resistance into a 50 Ω chest, which receives 333 J as a damped half-sine pulse about 5 ms long.',
          'Circuit of a DC defibrillator: charger and charging resistor feed a 32 microfarad capacitor at 5000 volts; a discharge switch connects it through a 50 millihenry inductor and a 10 ohm internal resistance to a 50 ohm chest. A sum box gives 400 joules stored and 333 joules delivered, and a small graph shows the damped half-sine current pulse of about 5 milliseconds.')


# ---- 5.2 the bypass loop with the worked example's flow ----
def f2():
    o = [T(20, 24, 'Bypass loop for a 170 cm, 60 kg patient: BSA 1.68 m², flow 4.04 L/min', 15, 'start', bold=True)]
    # patient
    o.append(R(20, 120, 130, 150, NXS, NX, 14)); o.append(T(85, 150, 'Patient', 14, bold=True))
    o.append(T(85, 178, 'right atrium', 13, fill=MUT)); o.append(T(85, 244, 'aorta', 13, fill=MUT))
    o.append(T(85, 211, 'heart stopped', 12, fill=NX)); o.append(T(85, 226, 'lungs still', 12, fill=NX))
    # top row: venous side
    boxes_top = [(190, 'Venous', 'reservoir', 'level sensor'), (350, 'Roller', 'pump', '4.04 L/min'), (510, 'Membrane', 'oxygenator', 'O₂ in, CO₂ out')]
    for x, a, b, n in boxes_top:
        o.append(boxt(x, 60, 130, 60, [a, b], ACS, AC, 13, bold_first=True)); o.append(T(x + 65, 138, n, 12, fill=MUT))
    o.append(L(150, 172, 170, 172, AC, 2)); o.append(L(170, 172, 170, 90, AC, 2)); o.append(L(170, 90, 188, 90, AC, 2, arrow='n'))
    o.append(T(160, 196, 'venous cannula', 12, 'start', MUT))
    o.append(L(320, 90, 348, 90, AC, 2, arrow='n')); o.append(L(480, 90, 508, 90, AC, 2, arrow='n'))
    o.append(L(640, 90, 680, 90, AC, 2)); o.append(L(680, 90, 680, 210, AC, 2, arrow='n'))
    # bottom row: arterial side, right to left
    boxes_bot = [(510, 'Heat', 'exchanger', 'cool, then rewarm'), (350, 'Arterial', 'filter', 'bubble detector')]
    for x, a, b, n in boxes_bot:
        o.append(boxt(x, 212, 130, 60, [a, b], PANEL, AC, 13, bold_first=True)); o.append(T(x + 65, 290, n, 12, fill=MUT))
    o.append(L(680, 242, 642, 242, AC, 2, arrow='n')); o.append(L(510, 242, 482, 242, AC, 2, arrow='n'))
    o.append(L(350, 242, 152, 242, AC, 2, arrow='n')); o.append(T(250, 234, 'aortic cannula', 12, fill=MUT))
    # sums
    o.append(boxt(20, 306, 680, 52, ['BSA = √(170 × 60 ÷ 3600) = 1.6833 m²   ·   flow = 2.4 L/min/m² × 1.6833 m² = 4.04 L/min   ·   MAP 50–80 mmHg'], LVS, LV, 13))
    return 370, ''.join(o)
FIG[2] = (f2, 'Blood drains from the right atrium to the venous reservoir, is pumped at the worked example\'s 4.04 L/min (2.4 L/min/m² × 1.6833 m²) through the oxygenator and heat exchanger, passes the arterial filter and bubble detector, and returns to the aorta.',
          'Loop diagram: patient, venous cannula, venous reservoir with level sensor, roller pump at 4.04 litres per minute, membrane oxygenator, heat exchanger, arterial filter with bubble detector, and the aortic cannula back to the patient, with the body surface area and flow sums below.')


# ---- 5.3 pressure and flow waveforms of the volume-control example ----
def f3():
    o = [T(20, 24, 'Volume control: 15 breaths/min, I:E 1:2, 500 mL, PEEP 5 cmH₂O', 15, 'start', bold=True)]
    x0, x1 = 80, 640
    fx = lambda t: x0 + t / 8 * (x1 - x0)
    # pressure panel
    y0, y1 = 50, 200
    fy = lambda p: y1 - p / 32 * (y1 - y0)
    o.append(L(x0, y1, x1, y1, L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    for p in (0, 5, 20, 28):
        o.append(L(x0 - 5, fy(p), x0, fy(p), L2, 1.5)); o.append(T(x0 - 9, fy(p) + 4.5, str(p), 12, 'end', MUT))
    o.append(T(x0 + 4, y0 - 6, 'pressure (cmH₂O)', 12, 'start', MUT))
    ti = 4 / 3
    pts = []
    for cyc in (0, 4):
        pts += [(fx(cyc), fy(5)), (fx(cyc + 0.06), fy(13)), (fx(cyc + ti - 0.25), fy(28)), (fx(cyc + ti - 0.2), fy(20)), (fx(cyc + ti), fy(20)),
                (fx(cyc + ti + 0.25), fy(9)), (fx(cyc + ti + 0.7), fy(5.5)), (fx(cyc + 4), fy(5))]
    o.append(P(pts, AC, 2.6))
    o.append(L(x0, fy(5), x1, fy(5), NX, 1.4, '5 4'))
    o.append(Tb(fx(2.3), fy(5) - 6, 'PEEP 5', 12, fill=NX))
    o.append(Tb(fx(ti - 0.25), fy(28) - 8, 'peak 28', 12, fill=AC, bold=True))
    o.append(Tb(fx(ti + 0.75), fy(20) - 2, 'plateau 20', 12, 'start', AC))
    # flow panel
    z0, z1 = 236, 336
    fz = lambda f: (z0 + z1) / 2 - f / 0.6 * (z1 - z0) / 2
    o.append(L(x0, fz(0), x1, fz(0), L2, 1.5)); o.append(L(x0, z0, x0, z1, L2, 1.5))
    for f in (0.375, 0, -0.375):
        o.append(T(x0 - 9, fz(f) + 4.5, neg(str(f)) if f else '0', 12, 'end', MUT))
    o.append(T(x0 + 4, z0 - 6, 'flow (L/s)', 12, 'start', MUT))
    pts = []
    for cyc in (0, 4):
        pts += [(fx(cyc), fz(0)), (fx(cyc), fz(0.375)), (fx(cyc + ti - 0.2), fz(0.375)), (fx(cyc + ti - 0.2), fz(0)), (fx(cyc + ti), fz(0))]
        for i in range(21):
            t = i / 20 * (4 - ti)
            pts.append((fx(cyc + ti + t), fz(-0.5 * math.exp(-t / 0.45))))
    o.append(P(pts, LV, 2.4))
    o.append(T(fx(0.55), fz(0.375) - 8, '0.375 L/s', 12, fill=LV, bold=True))
    for t in (0, ti, 4, 4 + ti, 8):
        o.append(L(fx(t), z1 + 2, fx(t), z1 + 7, L2, 1.5))
    o.append(T(fx(0), z1 + 22, '0', 12, fill=MUT)); o.append(T(fx(ti), z1 + 22, '1.33', 12, fill=MUT)); o.append(T(fx(4), z1 + 22, '4 s', 12, fill=MUT)); o.append(T(fx(4 + ti), z1 + 22, '5.33', 12, fill=MUT)); o.append(T(fx(8), z1 + 22, '8', 12, fill=MUT))
    o.append(brace(fx(0), fx(ti), z1 + 34, INK, up=False)); o.append(T(fx(ti / 2), z1 + 56, sb('T', 'i') + ' = 1.33 s', 12))
    o.append(brace(fx(ti), fx(4), z1 + 34, INK, up=False)); o.append(T(fx((ti + 4) / 2), z1 + 56, sb('T', 'e') + ' = 2.67 s', 12))
    o.append(boxt(652, 60, 62, 120, ['C', '500 ÷ 15', '= 33.3', 'mL per', 'cmH₂O'], LVS, LV, 12, bold_first=True))
    o.append(boxt(652, 196, 62, 120, ['R', '8 ÷ 0.375', '= 21.3', 'per', 'L/s'], LVS, LV, 12, bold_first=True))
    return 410, ''.join(o)
FIG[3] = (f3, 'Two breaths of the worked example: constant flow of 0.375 L/s for 1.33 s delivers 500 mL, pressure climbs from PEEP 5 to a peak of 28 cmH₂O, the pause shows the plateau of 20, and passive expiration fills the remaining 2.67 s. Compliance is 500 ÷ (20 − 5) = 33.3 mL/cmH₂O and resistance (28 − 20) ÷ 0.375 = 21.3 cmH₂O per L/s.',
          'Pressure-time and flow-time waveforms of two ventilator breaths: square inspiratory flow of 0.375 litres per second for 1.33 seconds, pressure rising from 5 to a 28 peak with a 20 plateau, then exponential expiratory flow back to zero over 2.67 seconds, with compliance and resistance boxes.')


# ---- 5.4 saturation curve with the two worked examples ----
def f4():
    o = [T(20, 24, 'How much water saturated gas holds, and what the humidifier must add', 15, 'start', bold=True)]
    x0, x1, y0, y1 = 80, 440, 56, 320
    fx = lambda t: x0 + t / 40 * (x1 - x0)
    fy = lambda a: y1 - a / 50 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 10, 20, 25, 30, 37], [0, 10, 20, 30, 44], fx, fy, 'temperature (°C)', 'water (mg/L)'))
    curve = [(0, 4.8), (5, 6.8), (10, 9.4), (15, 12.8), (20, 17.3), (25, 23.0), (30, 30.4), (35, 39.6), (37, 44.0), (40, 51.1)]
    o.append(P([(fx(t), fy(min(a, 50))) for t, a in curve if a <= 50] + [(fx(39.4), fy(50))], AC, 2.6))
    o.append(T(fx(15), fy(17), 'saturated gas', 13, 'end', AC, bold=True))
    o.append(C(fx(37), fy(44), 6, AC)); o.append(Tb(fx(37) - 10, fy(44) - 10, '37 °C: 44 mg/L', 12, 'end', AC, bold=True))
    o.append(C(fx(25), fy(23), 5, INK)); o.append(T(fx(25) - 10, fy(23) - 8, '25 °C: 23', 12, 'end'))
    o.append(C(fx(25), fy(11.5), 6, NX)); o.append(T(fx(25) + 10, fy(11.5) + 16, 'room air, 50 %: 11.5', 12, 'start', NX, bold=True))
    o.append(C(fx(25), fy(0), 6, LV)); o.append(T(fx(25) + 10, fy(0) - 8, 'dry oxygen: 0', 12, 'start', LV, bold=True))
    # deficit arrows
    o.append(L(fx(35), fy(0), fx(35), fy(43), LV, 2.2, arrow='l')); o.append(Tb(fx(35) - 6, fy(22), '44', 12, 'end', LV, bold=True))
    o.append(L(fx(31), fy(11.5), fx(31), fy(43), NX, 2.2, arrow='x')); o.append(Tb(fx(31) - 6, fy(30), '32.5', 12, 'end', NX, bold=True))
    o.append(L(fx(25), fy(11.5), fx(31), fy(11.5), NX, 1.4, '4 3')); o.append(L(fx(25), fy(0), fx(35), fy(0), LV, 1.4, '4 3'))
    o.append(boxt(470, 70, 240, 112, ['Dry oxygen, 10 L/min', '44 × 10 = 440 mg/min', '440 × 60 = 26 400 mg/h', '= 26.4 g/h'], LVS, LV, 13, bold_first=True))
    o.append(boxt(470, 200, 240, 112, ['Room air, 10 L/min', '44 − 11.5 = 32.5 mg/L', '32.5 × 10 = 325 mg/min', '= 19.5 g/h'], NXS, NX, 13, bold_first=True))
    return 372, ''.join(o)
FIG[4] = (f4, 'Saturated gas holds more water as it warms: 23 mg/L at 25 °C and 44 mg/L at 37 °C. Dry oxygen at 10 L/min needs the full 44 mg/L, 26.4 g/h; room air at 50 % humidity already carries 11.5 mg/L, so it needs 32.5 mg/L, 19.5 g/h.',
          'Graph of saturated water content against temperature from 0 to 40 degrees, marking 23 milligrams per litre at 25 degrees and 44 at 37, with room air at 11.5 and dry oxygen at zero, arrows showing deficits of 32.5 and 44, and two sum boxes giving 26.4 and 19.5 grams per hour.')


# ---- 5.5 short-wave chain and the two worked examples ----
def f5():
    o = [T(20, 24, 'Short-wave diathermy: mains to tissue at 27.12 MHz', 15, 'start', bold=True)]
    o.append(chain(14, 44, [['Mains', '50 Hz'], ['Rectifier'], ['Oscillator', '27.12 MHz'], ['Power', 'amplifier'], ['Matching', 'network']], 118, 54, 24, [PANEL, PANEL, ACS, PANEL, ACS], 13))
    o.append(L(14 + 4 * 142 + 118, 71, 14 + 4 * 142 + 118 + 8, 71, AC, 2))
    # plates and limb
    cx = 360; yb = 210
    o.append(L(14 + 4 * 142 + 59, 98, 14 + 4 * 142 + 59, 130, AC, 2)); o.append(L(14 + 4 * 142 + 59, 130, cx + 150, 130, AC, 2)); o.append(L(cx + 150, 130, cx + 150, 150, AC, 2))
    o.append(R(cx - 160, 150, 320, 14, NX, NX, 3)); o.append(R(cx - 160, 268, 320, 14, NX, NX, 3))
    o.append(T(cx - 172, 162, 'plate', 12, 'end', NX)); o.append(T(cx - 172, 280, 'plate', 12, 'end', NX))
    o.append(L(cx + 150, 282, cx + 150, 300, AC, 2)); o.append(L(cx + 150, 300, cx + 200, 300, AC, 2))
    o.append(f'<ellipse cx="{cx}" cy="{yb + 6}" rx="130" ry="46" style="fill:var(--live-soft);stroke:var(--live);stroke-width:2"/>')
    o.append(f'<ellipse cx="{cx}" cy="{yb + 6}" rx="104" ry="32" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:1.6"/>')
    o.append(f'<ellipse cx="{cx}" cy="{yb + 6}" rx="28" ry="14" style="fill:var(--panel);stroke:var(--ink);stroke-width:1.6"/>')
    o.append(T(cx, yb + 11, 'bone', 12)); o.append(T(cx - 66, yb + 11, 'muscle', 12, fill=AC, bold=True)); o.append(T(cx + 118, yb - 34, 'fat and skin', 12, 'start', LV))
    o.append(T(cx - 150, 190, 'towel gap', 12, 'end', MUT))
    for xx in (cx - 100, cx - 40, cx + 40, cx + 100):
        o.append(L(xx, 166, xx, 266, MUT, 1, '3 4'))
    o.append(boxt(20, 316, 330, 74, ['λ = 3 × 10⁸ ÷ 27.12 × 10⁶ = 11.06 m', 'T = 1 ÷ f = 36.9 ns', 'limb sits in the near field'], LVS, LV, 13))
    o.append(boxt(370, 316, 340, 74, ['Ultrasound head, 5 cm² at 1.5 W/cm²', '7.5 W × 300 s = 2250 J', 'pulsed 20 %: 1.5 W, 450 J; λ = 1.54 mm'], NXS, NX, 13))
    return 402, ''.join(o)
FIG[5] = (f5, 'The chain from 50 Hz mains to a 27.12 MHz field between two plates across the limb. The worked example gives λ = 11.06 m and T = 36.9 ns, so the limb sits in the near field and the field passes through fat into muscle; the ultrasound example gives 7.5 W, 2250 J and a 1.54 mm wavelength.',
          'Block chain of mains, rectifier, 27.12 megahertz oscillator, power amplifier and matching network feeding two capacitor plates on either side of a limb cross-section of skin and fat, muscle and bone, with sum boxes for the short-wave wavelength and period and for the ultrasound power and energy.')


# ---- 5.6 the TENS pulse train of the worked example ----
def f6():
    o = [T(20, 24, 'TENS example: 20 mA, 200 µs, 100 Hz (pulse width drawn wider than scale)', 15, 'start', bold=True)]
    o.append(chain(14, 40, [['Battery'], ['Oscillator', '1–150 Hz'], ['Pulse shaper', '50–400 µs'], ['Constant-', 'current out'], ['Electrodes', '5 × 5 cm']], 118, 52, 24, [PANEL, ACS, ACS, ACS, PANEL], 13))
    x0, x1, y0, y1 = 80, 640, 128, 290
    fx = lambda ms: x0 + ms / 32 * (x1 - x0)
    fy = lambda ma: y1 - ma / 24 * (y1 - y0)
    o.append(L(x0, y1, x1 + 20, y1, L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    for v in (0, 20):
        o.append(L(x0 - 5, fy(v), x0, fy(v), L2, 1.5)); o.append(T(x0 - 9, fy(v) + 4.5, str(v), 12, 'end', MUT))
    o.append(T(x0 + 4, y0 - 6, 'current (mA)', 12, 'start', MUT))
    pw = 1.2
    pts = [(fx(0), fy(0))]
    for k in range(4):
        t = 1 + k * 10
        pts += [(fx(t), fy(0)), (fx(t), fy(20)), (fx(t + pw), fy(20)), (fx(t + pw), fy(0))]
    pts.append((fx(32), fy(0)))
    o.append(P(pts, AC, 2.6))
    for k, t in enumerate((1, 11, 21, 31)):
        o.append(T(fx(t), y1 + 18, f'{t - 1} ms' if k < 3 else '', 12, fill=MUT))
    o.append(L(fx(0), fy(0.4) - 1, fx(32), fy(0.4) - 1, LV, 2, '6 4'))
    o.append(Tb(fx(16), fy(0.4) - 8, 'average 0.4 mA', 12, fill=LV, bold=True))
    o.append(brace(fx(1), fx(11), fy(20) - 12, INK, up=False)); o.append(T(fx(6), fy(20) - 20, '10 ms (100 Hz)', 12))
    o.append(T(fx(1 + pw) + 6, fy(10), '200 µs', 12, 'start', AC, bold=True))
    o.append(T(fx(21 + pw) + 6, fy(10), '4 µC', 12, 'start', AC, bold=True))
    o.append(boxt(14, 318, 692, 54, ['Q = 0.020 A × 2 × 10⁻⁴ s = 4 µC   ·   D = 2 × 10⁻⁴ × 100 = 2 %   ·   average = 0.4 mA   ·   4 µC ÷ 25 cm² = 0.16 µC/cm²'], LVS, LV, 13))
    return 384, ''.join(o)
FIG[6] = (f6, 'The stimulator chain and the worked example\'s pulse train: 20 mA pulses 200 µs wide every 10 ms. Each pulse carries 4 µC, the duty cycle is 2 %, the average current is only 0.4 mA, and a 25 cm² electrode sees 0.16 µC/cm².',
          'Block chain of battery, oscillator, pulse shaper, constant-current output and electrodes above a current-time plot of rectangular 20 milliampere pulses every 10 milliseconds, with a dashed average line at 0.4 milliamperes and the charge sums below.')


# ---- 5.7 the ellipsoid of the second worked example ----
def f7():
    o = [T(20, 24, 'Ellipsoid reflector: a = 150 mm, b = 90 mm, so c = 120 mm', 15, 'start', bold=True)]
    s = 1.4  # px per mm
    cx, cy = 280, 196
    X = lambda mm: cx + mm * s
    Y = lambda mm: cy - mm * s
    a, b, c = 150, 90, 120
    # reflector: left half of the ellipse beyond x = 0 to the left, drawn from angle 90 to 270 (the part around F1)
    pts = [(X(a * math.cos(th)), Y(b * math.sin(th))) for th in [math.radians(d) for d in range(80, 281, 4)]]
    o.append(P(pts, INK, 4))
    full = [(X(a * math.cos(th)), Y(b * math.sin(th))) for th in [math.radians(d) for d in range(-80, 81, 4)]]
    o.append(P(full, L2, 1.4, '5 5'))
    o.append(L(X(-a) - 10, cy, X(a) + 10, cy, L2, 1.2, '3 4'))
    f1, f2 = (X(-c), cy), (X(c), cy)
    # rays
    for th in (110, 140, 220, 250):
        r = math.radians(th); px, py = X(a * math.cos(r)), Y(b * math.sin(r))
        o.append(L(f1[0], f1[1], px, py, NX, 1.6)); o.append(L(px, py, f2[0], f2[1], AC, 1.6, arrow='n'))
    o.append(C(f1[0], f1[1], 7, NX)); o.append(Tb(f1[0], f1[1] + 26, 'F₁ spark', 13, fill=NX, bold=True))
    o.append(C(f2[0], f2[1], 8, LV)); o.append(Tb(f2[0], f2[1] + 26, 'F₂ stone', 13, fill=LV, bold=True))
    o.append(T(46, 72, 'reflector', 13, 'start', INK, bold=True))
    o.append(Tb(X(95), Y(-80), 'water path to the skin', 12, fill=MUT))
    # dimensions
    o.append(brace(f1[0], f2[0], cy + 52, INK)); o.append(Tb(cx, cy + 60, 'F₁F₂ = 2c = 240 mm', 13, bold=True))
    o.append(L(cx, cy, cx, Y(b), MUT, 1.4, '4 3')); o.append(Tb(cx + 6, Y(b / 2), 'b = 90', 12, 'start', MUT))
    o.append(boxt(536, 60, 176, 112, ['every reflected path', 'P F₁ + P F₂ = 2a', '= 300 mm', '0.3 m ÷ 1500 m/s', '= 0.2 ms'], LVS, LV, 13, bold_first=True))
    o.append(boxt(536, 186, 176, 74, ['c = √(150² − 90²)', '= √14 400 = 120 mm'], PANEL, AC, 13))
    o.append(boxt(536, 274, 176, 74, ['direct wave: 240 mm', '0.16 ms, unfocused'], PANEL, NX, 13))
    return 370, ''.join(o)
FIG[7] = (f7, 'The second worked example\'s reflector: with a = 150 mm and b = 90 mm the foci are c = 120 mm from the centre, 240 mm apart. Every ray from the spark at F₁ reflects to the stone at F₂ over the same 300 mm path, 0.2 ms in water, so all the reflected energy arrives together.',
          'Cross-section of an ellipsoidal reflector with the spark at the near focus and the stone at the far focus 240 millimetres away; four rays leave the spark, reflect from the wall and converge on the stone, and boxes give the 300 millimetre path, 0.2 milliseconds and the focal distance of 120 millimetres.')


# ---- 5.8 the ice ball and the heat budget of the worked example ----
def f8():
    o = [T(20, 24, 'Cryoprobe ice ball, and the heat removed from 1 g of tissue to −40 °C', 15, 'start', bold=True)]
    cx, cy = 190, 220
    o.append(f'<circle cx="{cx}" cy="{cy}" r="120" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="82" style="fill:var(--next-soft);stroke:var(--next);stroke-width:2;stroke-dasharray:6 4"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="52" style="fill:none;stroke:var(--live);stroke-width:2.4"/>')
    o.append(R(cx - 9, 40, 18, cy - 40, PANEL, INK, 4)); o.append(T(cx + 16, 56, 'probe, tip −196 °C', 12, 'start', INK, bold=True))
    o.append(Tb(cx + 82, cy - 98, 'ice edge 0 °C', 12, 'start', AC, bold=True))
    o.append(Tb(cx + 64, cy + 74, '−40 °C line', 12, 'start', NX, bold=True))
    o.append(Tb(cx, cy + 34, 'lesion', 12, fill=LV, bold=True))
    o.append(T(cx, cy + 140, 'the −40 °C line must cover the lesion', 12, fill=MUT))
    # stacked bar
    x0, bw, y1 = 450, 70, 330
    sc = 0.5  # px per J
    parts = [('Q₁ cool 37 → 0 °C', 129.5, ACS, AC), ('Q₂ freeze the water', 267.2, NXS, NX), ('Q₃ cool 0 → −40 °C', 72.0, LVS, LV)]
    y = y1
    for lab, q, f, s in parts:
        h = q * sc
        o.append(R(x0, y - h, bw, h, f, s, 2))
        o.append(T(x0 + bw + 10, y - h / 2 + 4, f'{lab}: {q:g} J', 12, 'start', s, bold=True))
        y -= h
    o.append(L(x0 - 6, y1, x0 + bw + 6, y1, L2, 1.5))
    o.append(T(x0 + bw / 2, y - 10, '468.7 J', 13, bold=True))
    o.append(boxt(450, 344, 262, 46, ['N₂: 468.7 J ÷ 199 kJ/kg = 2.36 g'], LVS, LV, 13))
    return 400, ''.join(o)
FIG[8] = (f8, 'Left: the ice ball grows from the −196 °C tip; its edge is near 0 °C and the lethal −40 °C line lies inside it, so it must reach past the lesion. Right: the worked example\'s heat budget for 1 g of tissue, 129.5 + 267.2 + 72 = 468.7 J, needing 2.36 g of liquid nitrogen.',
          'Cross-section of a cryoprobe in tissue with three circles, the outer ice edge at 0 degrees, the minus 40 degree line and the lesion inside it; beside it a stacked bar of the heat removed: 129.5 joules cooling, 267.2 joules freezing and 72 joules cooling the frozen tissue, 468.7 joules in all and 2.36 grams of nitrogen.')


# ---- 5.9 the protection network with the chapter's numbers ----
def f9():
    o = [T(20, 24, 'ECG input protection during a 5000 V defibrillator shock', 15, 'start', bold=True)]
    ya, yb = 104, 244
    o.append(R(20, 70, 96, 210, NXS, NX, 12)); o.append(T(68, 150, 'chest', 13, bold=True)); o.append(T(68, 170, '5000 V', 13, fill=NX, bold=True)); o.append(T(68, 188, 'from paddles', 12, fill=MUT))
    for y, lab in ((ya, 'RA'), (yb, 'LA')):
        o.append(C(116, y, 6, INK)); o.append(T(128, y - 12, lab, 12, 'start', MUT))
        o.append(L(116, y, 150, y, INK, 1.8)); o.append(res_h(150, 250, y, AC)); o.append(T(200, y - 16, '20 kΩ', 13, fill=AC, bold=True))
        o.append(L(250, y, 560, y, INK, 1.8))
    # neon
    nx = 310
    o.append(dot(nx, ya)); o.append(dot(nx, yb)); o.append(L(nx, ya, nx, 150, INK, 1.8)); o.append(L(nx, 198, nx, yb, INK, 1.8))
    o.append(f'<ellipse cx="{nx}" cy="174" rx="20" ry="24" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2"/>')
    o.append(L(nx, 150, nx, 166, INK, 2)); o.append(L(nx, 182, nx, 198, INK, 2))
    o.append(T(nx - 28, 170, 'neon', 12, 'end', AC, bold=True)); o.append(T(nx - 28, 186, '60–100 V', 12, 'end', AC))
    # clamp diodes: on each line one diode to +V and one from -V (anode -> cathode)
    def diode(x, yl, yr, to_rail, lab):
        """diode between the line at yl and a rail stub at yr; to_rail: anode on the line (the +V clamp)"""
        an, ca = (yl, yr) if to_rail else (yr, yl)
        d = 1 if ca > an else -1
        ym = (yl + yr) / 2
        t1, t2 = ym - 7 * d, ym + 7 * d
        ly = yr - 8 if yr < yl else yr + 18
        return (L(x, an, x, t1, LV, 1.8) + P([(x - 8, t1), (x + 8, t1), (x, t2), (x - 8, t1)], LV, 1.8, fill='var(--live-soft)')
                + L(x - 8, t2, x + 8, t2, LV, 2.4) + L(x, t2, x, ca, LV, 1.8) + L(x - 8, yr, x + 8, yr, LV, 2) + T(x, ly, lab, 12, fill=LV, bold=True))
    o.append(dot(420, ya)); o.append(diode(420, ya, ya - 44, True, '+V'))
    o.append(dot(490, ya)); o.append(diode(490, ya, ya - 44, False, '−V'))
    o.append(dot(420, yb)); o.append(diode(420, yb, yb + 44, True, '+V'))
    o.append(dot(490, yb)); o.append(diode(490, yb, yb + 44, False, '−V'))
    o.append(T(455, 170, 'clamp diodes', 12, fill=LV, bold=True)); o.append(T(455, 186, 'to the rails', 12, fill=LV))
    # amplifier triangle
    o.append(P([(560, 90), (560, 258), (680, 174), (560, 90)], AC, 2.2, fill='var(--panel)'))
    o.append(T(600, 170, 'ECG', 13, bold=True)); o.append(T(600, 188, 'amp', 13, bold=True))
    o.append(T(574, ya + 5, '+', 14, bold=True)); o.append(T(574, yb + 5, '−', 14, bold=True))
    o.append(boxt(20, 324, 692, 54, ['series R limit: 5000 V ÷ (20 + 20) kΩ = 125 mA   ·   neon shunts the rest   ·   diodes hold the input to the rails'], LVS, LV, 13))
    return 392, ''.join(o)
FIG[9] = (f9, 'The protection network between two ECG electrodes and the amplifier. The 20 kΩ series resistors limit the current to 5000 V ÷ 40 kΩ = 125 mA, the neon lamp fires at 60–100 V and shunts the shock, and clamp diodes hold what is left within the supply rails.',
          'Circuit: two chest electrodes, each through a 20 kilohm series resistor, a neon lamp across the two lines, a clamp diode from one line to the positive rail and from the other to the negative rail, and the ECG amplifier, with the 125 milliampere current limit worked out below.')


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'caption': cap, 'after_section': AFTER[k], 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
