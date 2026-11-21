"""Claude's hand-drawn figures for bm-instr-u2 (cardiovascular and respiratory measurements), one per chapter, each drawn
from that chapter's own worked example and numbers. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *


def sb(base, s, size=11):
    return f'{base}<tspan baseline-shift="sub" font-size="{size}">{s}</tspan>'


def sp(base, s, size=11):
    return f'{base}<tspan baseline-shift="super" font-size="{size}">{s}</tspan>'


H2O = 'cm H₂O'
FIG = {}


# ---- ch1: cuff pressure falling at 3 mmHg/s, Korotkoff phases I to V (128, 100, 82 mmHg) ----
def f1():
    x0, x1, y0, y1 = 96, 650, 40, 280
    fx = lambda t: x0 + (x1 - x0) * t / 32
    fy = lambda p: y1 - (y1 - y0) * (p - 60) / (170 - 60)
    o = [axes(x0, x1, y0, y1, [0, 4, 8, 12, 16, 20, 24, 28, 32], [60, 80, 100, 120, 140, 160], fx, fy,
              'time after deflation starts (s)', 'cuff pressure (mmHg)')]
    for p, lab, c in ((128, 'systolic 128', AC), (100, 'phase IV 100', MUT), (82, 'diastolic 82', LV)):
        o.append(L(x0, fy(p), x1, fy(p), c, 1.4, dash='6 4'))
        o.append(Tb(x1 - 4, fy(p) - 6, lab, 13, 'end', c))
    o.append(P([(fx(0), fy(160)), (fx(32), fy(64))], INK, 2.6))
    o.append(C(fx(0), fy(160), 5, INK))
    o.append(Tb(fx(0) + 12, fy(160) - 4, 'cuff pumped to 160, let down at 3 mmHg/s', 13, 'start'))
    for t, p, c in ((32 / 3, 128, AC), (20, 100, MUT), (26, 82, LV)):
        o.append(C(fx(t), fy(p), 5.5, c))
    # sound lane: one tick per beat (75 per minute), height by phase
    ly = 360
    o.append(T(x0 - 8, ly + 5, 'sound', 13, 'end', MUT))
    o.append(L(x0, ly, x1, ly, L2, 1.2))
    t = 0.8
    while t < 32:
        p = 160 - 3 * t
        if 82 < p <= 128:
            h = 20 if p > 118 else (9 if p > 108 else (26 if p > 100 else 8))
            c = AC if p > 100 else MUT
            o.append(L(fx(t), ly - h, fx(t), ly + h, c, 2.6))
        t += 0.8
    for a, b, lab in ((128, 118, 'I'), (118, 108, 'II'), (108, 100, 'III'), (100, 82, 'IV')):
        xm = (fx((160 - a) / 3) + fx((160 - b) / 3)) / 2
        o.append(T(xm, ly + 46, lab, 14, bold=True))
    o.append(T(fx(29), ly + 46, 'V: silent', 14, bold=True, fill=LV))
    o.append(T(fx(4.5), ly + 5, 'no sound: artery shut', 13, fill=MUT))
    return 420, ''.join(o)


FIG[1] = (f1, 'The cuff pressure falls in a straight line at 3 mmHg per second. Sounds start at 128 mmHg (phase I, systolic), '
              'go muffled at 100 mmHg (phase IV) and stop at 82 mmHg (phase V, diastolic); each tick is one heartbeat.',
          'Cuff pressure falling from 160 mmHg at 3 mmHg per second against time, with Korotkoff sounds from 128 to 82 mmHg '
          'drawn as one tick per beat and phases I to V marked.')


# ---- ch2: sampled ICG curve, trapezoid area, extrapolated tail, recirculation hump ----
DYE_T = [4, 6, 8, 10, 12, 14, 16]
DYE_C = [0, 3.0, 7.5, 6.0, 4.2, 3.0, 2.1]
TAU = 2 / math.log(3.0 / 2.1)


def f2():
    x0, x1, y0, y1 = 80, 660, 44, 290
    fx = lambda t: x0 + (x1 - x0) * t / 40
    fy = lambda c: y1 - (y1 - y0) * c / 8
    o = [axes(x0, x1, y0, y1, [0, 5, 10, 15, 20, 25, 30, 35, 40], [0, 2, 4, 6, 8], fx, fy,
              'time after injection (s)', 'dye concentration (mg/L)')]
    tail = [(16 + i * 0.5, 2.1 * math.exp(-(i * 0.5) / TAU)) for i in range(49)]
    area = [(fx(t), fy(c)) for t, c in zip(DYE_T, DYE_C)] + [(fx(t), fy(c)) for t, c in tail[1:]]
    area += [(fx(40), fy(0)), (fx(4), fy(0))]
    o.append(P(area, 'none', 0, fill=ACS))
    # measured curve: first pass then the recirculation hump
    rec_t = [16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
    rec_c = [2.1, 1.65, 1.55, 1.75, 1.9, 1.75, 1.45, 1.2, 1.0, 0.85, 0.72, 0.62, 0.55]
    o.append(P([(fx(t), fy(c)) for t, c in zip(rec_t, rec_c)], MUT, 2))
    o.append(P([(fx(t), fy(c)) for t, c in tail], AC, 2.2, dash='7 5'))
    o.append(P([(fx(t), fy(c)) for t, c in zip(DYE_T, DYE_C)], AC, 2.6))
    for t, c in zip(DYE_T, DYE_C):
        o.append(C(fx(t), fy(c), 4.5, AC))
    o.append(L(fx(16), fy(0), fx(16), fy(2.1), L2, 1.2, dash='3 3'))
    o.append(Tb(fx(8) + 10, fy(7.5) - 6, 'peak 7.5 mg/L at 8 s', 13, 'start'))
    o.append(Tb(fx(10), fy(1.6), 'A₁ = 49.5', 14, bold=True))
    o.append(Tb(fx(19.5), fy(0.55), 'A₂ = 11.8', 14, bold=True))
    o.append(Tb(fx(24), fy(2.6), 'recirculation hump: not counted', 13, fill=MUT))
    o.append(Tb(fx(28), fy(0.25) - 52, 'dashed: decay continued, τ = 5.6 s', 13, 'start', AC))
    o.append(boxt(fx(22), 52, 268, 58, ['A = 49.5 + 11.8 = 61.3 mg·s/L', 'CO = 60 × 5 / 61.3 = 4.9 L/min'], ACS, AC, 14))
    return 350, ''.join(o)


FIG[2] = (f2, 'The worked example\'s samples every 2 s (dots) give area A₁ by trapezoids up to 16 s; the dashed decay, continued '
              'under the recirculation hump, adds A₂. The shaded first-pass area of 61.3 mg·s/L gives 4.9 L/min.',
          'Dye concentration against time: samples rising to 7.5 mg per litre at 8 s and falling, a recirculation hump after '
          '18 s, and a dashed exponential tail; the shaded area is 61.3 mg s per litre and cardiac output 4.9 litres per minute.')


# ---- ch3: ECG and PCG lanes; S1 0.05 s and S2 0.35 s after R, RR 0.80 s ----
def f3():
    x0, x1 = 100, 670
    fx = lambda t: x0 + (x1 - x0) * (t + 0.05) / 1.05
    o = []
    ye, yp = 92, 222
    o.append(T(x0 - 14, ye + 5, 'ECG', 14, 'end', MUT, bold=True))
    o.append(T(x0 - 14, yp + 5, 'PCG', 14, 'end', MUT, bold=True))
    ecg = []
    for i in range(421):
        t = -0.05 + 1.05 * i / 420
        v = 0
        for r in (0.0, 0.80):
            v += 60 * math.exp(-((t - r) / 0.010) ** 2) - 12 * math.exp(-((t - r - 0.025) / 0.012) ** 2)
            v += 14 * math.exp(-((t - r - 0.28) / 0.045) ** 2) + 7 * math.exp(-((t - r + 0.15) / 0.03) ** 2)
        ecg.append((fx(t), ye - v))
    o.append(P(ecg, INK, 2))
    pcg = []
    for i in range(841):
        t = -0.05 + 1.05 * i / 840
        v = 0
        for s, w, a in ((0.05, 0.10, 30), (0.35, 0.07, 22), (0.85, 0.10, 30)):
            if s <= t <= s + w:
                env = math.sin(math.pi * (t - s) / w)
                v += a * env * math.sin(2 * math.pi * 60 * (t - s))
        pcg.append((fx(t), yp - v))
    o.append(P(pcg, AC, 1.8))
    for t, lab in ((0.05, 'S1'), (0.35, 'S2'), (0.85, 'S1')):
        o.append(L(fx(t), ye - 62, fx(t), yp + 40, L2, 1.2, dash='4 4'))
        o.append(T(fx(t) + 18, yp - 40, lab, 14, bold=True, fill=AC))
    for r in (0.0, 0.80):
        o.append(T(fx(r), ye - 68, 'R', 14, bold=True))
    yb = yp + 62
    o.append(L(fx(0.05), yb, fx(0.35), yb, LV, 2, arrow='l'))
    o.append(L(fx(0.35), yb, fx(0.05), yb, LV, 2, arrow='l'))
    o.append(T(fx(0.20), yb + 22, 'systole 0.30 s', 14, fill=LV, bold=True))
    o.append(L(fx(0.35), yb, fx(0.85), yb, NX, 2, arrow='x'))
    o.append(L(fx(0.85), yb, fx(0.35), yb, NX, 2, arrow='x'))
    o.append(T(fx(0.60), yb + 22, 'diastole 0.50 s', 14, fill=NX, bold=True))
    yr = 330
    o.append(L(fx(0), yr, fx(0.80), yr, INK, 1.6, arrow='m'))
    o.append(L(fx(0.80), yr, fx(0), yr, INK, 1.6, arrow='m'))
    o.append(T(fx(0.40), yr + 24, 'RR = 0.80 s → 60 / 0.80 = 75 beats per minute', 14))
    o.append(T(x1, 380, 'filter 25–400 Hz', 13, 'end', MUT))
    return 392, ''.join(o)


FIG[3] = (f3, 'The ECG gives the time reference: S1 starts 0.05 s and S2 0.35 s after the R wave, so systole lasts 0.30 s and '
              'diastole 0.50 s of the 0.80 s cycle.',
          'An ECG trace above a phonocardiogram; S1 at 0.05 s and S2 at 0.35 s after the R wave, systole 0.30 s, diastole '
          '0.50 s, RR 0.80 s and heart rate 75 beats per minute.')


# ---- ch4: a missed QRS doubles one RR interval and crosses the 1.5 s pause limit ----
def f4():
    x0, x1 = 110, 670
    fx = lambda t: x0 + (x1 - x0) * t / 4.2
    o = []
    ye = 70
    o.append(T(x0 - 14, ye + 5, 'ECG', 14, 'end', MUT, bold=True))
    o.append(L(x0, ye, x1, ye, L2, 1))
    beats = [0.1, 0.9, 1.7, 2.5, 3.3, 4.1]
    for i, b in enumerate(beats):
        c = INK if i != 3 else MUT
        pts = [(fx(b) - 9, ye), (fx(b) - 4, ye + 8), (fx(b), ye - 44), (fx(b) + 4, ye + 12), (fx(b) + 9, ye)]
        o.append(P(pts, c, 2, dash=None if i != 3 else '4 3'))
    o.append(Tb(fx(2.5), ye + 34, 'QRS missed', 13, fill=LV))
    detected = [0.1, 0.9, 1.7, 3.3, 4.1]
    # tachogram: bar height = RR interval
    y1, yt = 330, 130
    fy = lambda s: y1 - (y1 - yt) * s / 2.0
    o.append(L(x0, y1, x1, y1, L2, 1.5))
    o.append(L(x0, yt - 6, x0, y1, L2, 1.5))
    for s in (0, 0.5, 1.0, 1.5, 2.0):
        o.append(L(x0 - 5, fy(s), x0, fy(s), L2, 1.5))
        o.append(T(x0 - 9, fy(s) + 4.5, f'{s:.1f}', 13, 'end', MUT))
    o.append(T(x0 - 4, yt - 16, 'RR interval (s)', 14, 'start', MUT))
    o.append(L(x0, fy(1.5), x1, fy(1.5), LV, 1.8, dash='7 4'))
    o.append(Tb(x1 - 4, fy(1.5) - 7, 'pause limit 1.5 s', 13, 'end', LV))
    for a, b in zip(detected, detected[1:]):
        rr = b - a
        c = LV if rr > 1.5 else AC
        fill = LVS if rr > 1.5 else ACS
        xa, xb = fx(a) + 6, fx(b) - 6
        o.append(R(xa, fy(rr), xb - xa, y1 - fy(rr), fill, c, 4))
        rate = 60 / rr
        o.append(T((xa + xb) / 2, fy(rr) - 8 if rr < 1.5 else fy(rr) + 22, f'{rr * 1000:.0f} ms', 14, bold=True, fill=c))
        o.append(T((xa + xb) / 2, y1 + 22, f'{rate:g} per min', 13, fill=c))
    o.append(T((fx(1.7) + fx(3.3)) / 2, y1 - 30, 'alarm', 14, bold=True, fill=LV))
    return 362, ''.join(o)


FIG[4] = (f4, 'When the detector misses one QRS, the interval it measures is 1600 ms instead of 800 ms. That bar crosses the '
              '1.5 s pause limit and the rate drops from 75 to 37.5 per minute, though the heart never slowed.',
          'ECG beats every 0.8 s with one QRS missed, and below them bars of the measured RR intervals: 800, 800, 1600 and 800 '
          'ms; the 1600 ms bar crosses the 1.5 s pause line and reads 37.5 per minute.')


# ---- ch5: forced expiration, normal FVC 4.0 L, FEV1 3.2 L; obstructive FVC 3.0 L, FEV1 1.2 L ----
def f5():
    x0, x1, y0, y1 = 80, 640, 40, 300
    fx = lambda t: x0 + (x1 - x0) * t / 7
    fy = lambda v: y1 - (y1 - y0) * v / 5
    o = [axes(x0, x1, y0, y1, [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5], fx, fy, 'time from start of blow (s)', 'volume exhaled (L)')]
    o.append(L(fx(1), y0, fx(1), y1, L2, 1.4, dash='5 4'))
    o.append(T(fx(1) + 6, y0 + 10, '1 s', 13, 'start', MUT))
    for F, tau, c, name in ((4.0, 0.62, AC, 'normal'), (3.0, 1.96, LV, 'obstructive')):
        o.append(P([(fx(t / 20), fy(F * (1 - math.exp(-t / 20 / tau)))) for t in range(141)], c, 2.6))
        v1 = F * (1 - math.exp(-1 / tau))
        o.append(C(fx(1), fy(v1), 5, c))
    o.append(Tb(fx(1) + 12, fy(3.2) + 18, 'FEV₁ 3.2 L', 14, 'start', AC, bold=True))
    o.append(Tb(fx(1) + 12, fy(1.2) + 18, 'FEV₁ 1.2 L', 14, 'start', LV, bold=True))
    o.append(Tb(fx(4.6), fy(4.0) - 10, 'normal: FVC 4.0 L, ratio 3.2/4.0 = 0.80', 13, fill=AC))
    o.append(Tb(fx(4.6), fy(1.9), 'asthma: FVC 3.0 L, ratio 1.2/3.0 = 0.40', 13, fill=LV))
    return 350, ''.join(o)


FIG[5] = (f5, 'Both people blow out as hard as they can. At 1 s the normal curve has reached 3.2 L of its 4.0 L; the obstructed '
              'one has reached only 1.2 L of its 3.0 L, so its FEV₁/FVC is 0.40.',
          'Volume against time for two forced expirations: normal FVC 4.0 litres with FEV1 3.2 litres, obstructive FVC 3.0 '
          'litres with FEV1 1.2 litres, ratios 0.80 and 0.40.')


# ---- ch6: Fleisch head, pressure taps, differential transducer, flow and volume ----
def f6():
    o = []
    ty, th = 70, 64
    o.append(R(40, ty, 640, th, PANEL, INK, 10))
    o.append(T(70, ty + th / 2 + 5, 'mouth', 13, fill=MUT))
    o.append(T(615, ty + th / 2 + 5, 'room', 13, fill=MUT))
    o.append(L(110, ty + th / 2, 220, ty + th / 2, AC, 2.4, arrow='n'))
    o.append(T(165, ty - 10, 'flow Q = 0.5 L/s', 14, bold=True, fill=AC))
    cx0, cx1 = 300, 420
    o.append(R(cx0, ty + 4, cx1 - cx0, th - 8, ACS, AC, 4))
    for i in range(1, 9):
        y = ty + 4 + (th - 8) * i / 9
        o.append(L(cx0 + 4, y, cx1 - 4, y, AC, 1.4))
    o.append(T((cx0 + cx1) / 2, ty - 10, 'capillary bundle', 13, fill=AC))
    for x, lab in ((262, sb('P', '1')), (458, sb('P', '2'))):
        o.append(L(x, ty + th, x, 196, INK, 2))
        o.append(T(x + 10, 182, lab, 14, 'start', bold=True))
    o.append(boxt(232, 196, 256, 52, ['differential transducer', 'ΔP = P₁ − P₂ = 0.75 ' + H2O], PANEL, AC, 13))
    o.append(P([(360, 248), (360, 262), (123, 262), (123, 276)], AC, 2))
    o.append(L(123, 270, 123, 277, AC, 2, arrow='n'))
    chain = [(48, 'carrier amplifier'), (206, 'flow = ΔP / R' + '<tspan baseline-shift="sub" font-size="10">pt</tspan>'), (364, 'integrator ∫Q dt'), (522, 'volume')]
    for i, (x, lab) in enumerate(chain):
        st = LV if i == 3 else AC
        o.append(boxt(x, 280, 150, 44, [lab], LVS if i == 3 else PANEL, st, 13))
        if i < 3: o.append(L(x + 150, 302, x + 156, 302, AC, 2, arrow='n'))
    o.append(T(281, 344, '0.75 / 1.5 = 0.5 L/s', 13, fill=AC))
    o.append(T(597, 344, '0.5 L/s × 1 s = 0.5 L', 13, fill=LV))
    o.append(T(123, 344, 'R' + '<tspan baseline-shift="sub" font-size="10">pt</tspan>' + ' = 1.5 ' + H2O + ' per L/s', 13, fill=MUT))
    return 360, ''.join(o)


FIG[6] = (f6, 'Flow through the capillary bundle drops the pressure from P₁ to P₂. In the worked example 0.5 L/s gives 0.75 cm H₂O, so '
              'R<sub>pt</sub> = 1.5 cm H₂O per L/s; integrating 0.5 L/s for 1 s gives 0.5 L.',
          'A pneumotachograph tube with a capillary bundle, pressure taps P1 and P2 feeding a differential transducer, then '
          'amplifier, flow and integrator blocks; 0.75 cm water at 0.5 litres per second, volume 0.5 litre.')


# ---- ch7: red and infrared light through the finger, AC on DC, ratio of ratios 0.55 ----
def f7():
    o = []
    # finger cross-section
    o.append(R(40, 120, 150, 120, ACS, AC, 60))
    o.append(f'<ellipse cx="115" cy="180" rx="26" ry="20" style="fill:var(--panel);stroke:var(--muted);stroke-width:1.6"/>')
    o.append(T(115, 185, 'bone', 13, fill=MUT))
    o.append(R(62, 66, 40, 26, LVS, LV, 4)); o.append(T(82, 58, 'red 660 nm', 13, fill=LV))
    o.append(R(128, 66, 40, 26, NXS, NX, 4)); o.append(T(160, 40, 'infrared 940 nm', 13, fill=NX))
    o.append(L(82, 94, 96, 252, LV, 1.6, dash='5 4', arrow='l'))
    o.append(L(148, 94, 132, 252, NX, 1.6, dash='5 4', arrow='x'))
    o.append(R(90, 262, 50, 22, PANEL, INK, 4)); o.append(T(115, 304, 'photodiode', 13))
    o.append(L(146, 273, 220, 273, INK, 1.6, arrow='m'))
    # traces
    x0, x1 = 240, 690
    for i, (name, dc, ac, c, y) in enumerate((('red', 100, 2, LV, 96), ('infrared', 110, 4, NX, 220))):
        pts = []
        for j in range(301):
            t = j / 300 * 3.2
            ph = (t % 1.0)
            pulse = math.exp(-((ph - 0.25) / 0.09) ** 2) * 1.0 + 0.35 * math.exp(-((ph - 0.5) / 0.08) ** 2)
            pts.append((x0 + (x1 - x0) * j / 300, y - 14 + 6 * ac * pulse))
        o.append(L(x0, y + 24, x1, y + 24, L2, 1))
        o.append(P(pts, c, 2.2))
        o.append(T(x0, y - 44, f'{name}: DC = {dc}, AC = {ac}', 14, 'start', c, bold=True))
        o.append(T(x1, y - 44, f'AC/DC = {ac}/{dc} = {ac / dc:.4f}', 13, 'end', c))
    o.append(boxt(250, 290, 440, 58, ['R = 0.0200 / 0.0364 = 0.55', 'SpO₂ ≈ 110 − 25 R = 96 %'], ACS, AC, 14))
    return 362, ''.join(o)


FIG[7] = (f7, 'Each beat makes the transmitted light dip a little (AC) below a large steady level (DC). The red AC/DC (0.0200) divided by '
              'the infrared AC/DC (0.0364) gives R = 0.55, which the textbook straight line turns into about 96 %.',
          'A finger between red and infrared light-emitting diodes and a photodiode; the red channel has DC 100 and AC 2, the '
          'infrared channel DC 110 and AC 4; R equals 0.55 and saturation about 96 percent.')


# ---- ch8: body box, shutter, two transducers; Vtg = 3.0 L from 30 mL and 9.7 cm H2O ----
def f8():
    o = []
    o.append(R(30, 40, 300, 300, PANEL, INK, 14, sw=2.6))
    o.append(T(180, 30, 'sealed box, 600 L', 14, bold=True))
    # seated subject
    o.append(f'<circle cx="130" cy="118" r="26" style="fill:var(--fig);stroke:var(--ink);stroke-width:2"/>')
    o.append(R(98, 148, 64, 110, FIGBG, INK, 16))
    o.append(R(150, 236, 70, 22, FIGBG, INK, 8))
    o.append(R(70, 258, 160, 12, PANEL, MUT, 3))
    o.append(R(130, 170, 44, 50, LVS, LV, 14)); o.append(T(152, 200, 'lungs', 13, fill=LV))
    # mouthpiece and shutter
    o.append(L(156, 118, 236, 118, INK, 6))
    o.append(R(236, 102, 12, 32, AC, AC, 2)); o.append(T(244, 92, 'shutter', 13, fill=AC))
    o.append(L(248, 118, 300, 118, INK, 6))
    o.append(R(268, 108, 26, 20, ACS, AC, 3)); o.append(T(281, 152, 'pneumo-', 12, fill=MUT)); o.append(T(281, 165, 'tach', 12, fill=MUT))
    o.append(L(200, 118, 200, 60, INK, 1.6)); o.append(L(200, 60, 360, 60, INK, 1.6, arrow='m'))
    o.append(boxt(366, 40, 160, 40, ['mouth pressure'], PANEL, AC, 13))
    o.append(L(300, 300, 360, 300, INK, 1.6, arrow='m'))
    o.append(boxt(366, 280, 160, 40, ['box pressure'], PANEL, AC, 13))
    # numbers
    o.append(T(540, 66, 'ΔP' + '<tspan baseline-shift="sub" font-size="10">mouth</tspan>' + ' = 9.7 ' + H2O, 13, 'start', AC, bold=True))
    o.append(T(540, 306, 'ΔP' + '<tspan baseline-shift="sub" font-size="10">box</tspan>' + ' = 0.075 ' + H2O, 13, 'start', AC, bold=True))
    st = ['shutter shut, subject pants at 1 Hz',
          'ΔV = 400 mL per ' + H2O + ' × 0.075 = 30 mL',
          'Boyle: V = ΔV × (P' + '<tspan baseline-shift="sub" font-size="10">B</tspan>' + ' − 47 mmHg) / ΔP' + '<tspan baseline-shift="sub" font-size="10">mouth</tspan>',
          '= 30 mL × 970 / 9.7 = 3000 mL = FRC']
    o.append(R(352, 104, 350, 152, ACS, AC, 8))
    for i, s in enumerate(st):
        o.append(T(366, 132 + 34 * i, s, 13, 'start', INK, bold=(i == 3)))
    return 352, ''.join(o)


FIG[8] = (f8, 'With the shutter closed, the subject\'s panting squeezes the trapped lung gas. The box pressure swing (0.075 cm H₂O) '
              'gives the volume change, 30 mL; Boyle\'s law with the 9.7 cm H₂O mouth swing gives the gas volume, 3.0 L.',
          'A sealed 600 litre box with a seated subject, a mouthpiece shutter and pneumotachograph, and mouth and box pressure '
          'transducers; mouth swing 9.7 cm water, box swing 0.075, volume change 30 mL, thoracic gas volume 3.0 litres.')

AFTER = {1: 2, 2: 2, 3: 3, 4: 3, 5: 3, 6: 1, 7: 1, 8: 2}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'after_section': AFTER[k], 'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
