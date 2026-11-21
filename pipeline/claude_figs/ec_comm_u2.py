"""Claude's hand-drawn figures for ec-comm-u2 (Amplitude Modulation Systems), one per chapter.
Every curve and value is computed from that chapter's own worked example; colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def curve(f, a, b, fx, fy, n=400, c=AC, w=2.2, dash=None):
    return P([(fx(a + (b - a) * i / n), fy(f(a + (b - a) * i / n))) for i in range(n + 1)], c, w, dash)


def stem(x, y0, y, c=AC, w=3):
    return L(x, y0, x, y, c, w) + C(x, y, 4.5, c)


def poly(pts, fill, stroke, w=1.8, op=None):
    o = f';fill-opacity:{op}' if op is not None else ''
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" style="fill:{fill};stroke:{stroke};stroke-width:{w}{o}"/>'


# ---- 2.1 envelope 12 V / 4 V and the three-line spectrum ----
def f1():
    o = []
    x0, x1, yc, sc = 80, 560, 130, 7.5          # top: time plot, 1 V = 7.5 px
    fx = lambda t: x0 + t / 400 * (x1 - x0)      # t in microseconds, two message periods of 200 us
    fy = lambda v: yc - v * sc
    o.append(L(x0, yc, x1, yc, L2, 1.2))
    o.append(L(x0, fy(14), x0, fy(-14), L2, 1.5))
    for v in (12, 4, -4, -12):
        o.append(L(x0 - 5, fy(v), x0, fy(v), L2, 1.5)); o.append(T(x0 - 9, fy(v) + 4.5, neg(v), 13, 'end', MUT))
    env = lambda t: 8 * (1 + 0.5 * math.cos(2 * math.pi * t / 200))
    o.append(curve(lambda t: env(t) * math.cos(2 * math.pi * t / 10), 0, 400, fx, fy, 800, AC, 1.4))
    o.append(curve(env, 0, 400, fx, fy, 200, NX, 2.2, '6 4'))
    o.append(curve(lambda t: -env(t), 0, 400, fx, fy, 200, NX, 2.2, '6 4'))
    o.append(L(fx(400), fy(12), x1 + 14, fy(12), L2, 1, '3 3'))
    o.append(T(x1 + 18, fy(12) + 5, 'V<tspan baseline-shift="sub" font-size="10">max</tspan> = 12 V', 14, 'start'))
    o.append(L(fx(300), fy(4), x1 + 14, fy(4), L2, 1, '3 3'))
    o.append(T(x1 + 18, fy(4) + 5, 'V<tspan baseline-shift="sub" font-size="10">min</tspan> = 4 V', 14, 'start'))
    o.append(T(x1 + 18, fy(-4) + 5, 'envelope', 13, 'start', NX))
    o.append(T(x1 + 18, fy(-4) + 22, '(dashed)', 13, 'start', NX))
    o.append(T(x0, 26, 'AM wave, carrier drawn slowed: m = (12 − 4)/(12 + 4) = 0.5', 14, 'start', INK, True))
    o.append(T(x1, fy(-14) + 40, 't (µs); one message cycle = 200 µs', 13, 'end', MUT))
    for t in (0, 100, 200, 300, 400):
        o.append(L(fx(t), fy(-14), fx(t), fy(-14) + 5, L2, 1.2)); o.append(T(fx(t), fy(-14) + 19, str(t), 13, fill=MUT))
    # bottom: line spectrum
    X0, X1, Y0 = 120, 640, 430
    fX = lambda f: X0 + (f - 990) / 20 * (X1 - X0)
    fY = lambda v: Y0 - v * 16
    o.append(T(x0, 310, 'Line spectrum: m = 0.5, A<tspan baseline-shift="sub" font-size="10">c</tspan> = 8 V, f<tspan baseline-shift="sub" font-size="10">m</tspan> = 5 kHz', 14, 'start', INK, True))
    o.append(L(X0 - 10, Y0, X1 + 10, Y0, L2, 1.5))
    for f in (990, 995, 1000, 1005, 1010):
        o.append(L(fX(f), Y0, fX(f), Y0 + 5, L2, 1.2)); o.append(T(fX(f), Y0 + 20, str(f), 13, fill=MUT))
    o.append(T(X1 + 10, Y0 + 40, 'f (kHz)', 13, 'end', MUT))
    o.append(stem(fX(1000), Y0, fY(8), AC)); o.append(T(fX(1000), fY(8) - 12, 'carrier 8 V', 14))
    for f, lab in ((995, 'LSB 2 V'), (1005, 'USB 2 V')):
        o.append(stem(fX(f), Y0, fY(2), LV)); o.append(T(fX(f), fY(2) - 12, lab, 14))
    o.append(brace(fX(995), fX(1005), Y0 + 52, INK, up=True))
    o.append(T(fX(1000), Y0 + 72, 'bandwidth 2f<tspan baseline-shift="sub" font-size="10">m</tspan> = 10 kHz', 14))
    return 512, ''.join(o)


FIG[1] = (f1, 'Worked example 1: the envelope (dashed) swings between V_max = 12 V and V_min = 4 V, so m = 8/16 = 0.5 and A_c = 8 V. '
              'Below, the same wave as three lines: an 8 V carrier at 1000 kHz and 2 V sidebands at 995 and 1005 kHz, 10 kHz apart.',
          'Top: an AM wave with dashed envelope peaking at 12 V and dipping to 4 V. Bottom: line spectrum with an 8 V carrier at 1000 kHz and 2 V lines at 995 and 1005 kHz; bandwidth 10 kHz.')


# ---- 2.2 DSB-SC wave with phase reversals, and its two lines ----
def f2():
    o = []
    x0, x1, yc, sc = 80, 690, 140, 4.5
    fx = lambda t: x0 + t / 2000 * (x1 - x0)     # t in microseconds, two cycles of the 1 kHz tone
    fy = lambda v: yc - v * sc
    o.append(L(x0, yc, x1, yc, L2, 1.2)); o.append(L(x0, fy(24), x0, fy(-24), L2, 1.5))
    for v in (20, -20):
        o.append(L(x0 - 5, fy(v), x0, fy(v), L2, 1.5)); o.append(T(x0 - 9, fy(v) + 4.5, neg(v), 13, 'end', MUT))
    m = lambda t: 20 * math.cos(2 * math.pi * t / 1000)
    o.append(curve(lambda t: m(t) * math.cos(2 * math.pi * t / 62.5), 0, 2000, fx, fy, 1000, AC, 1.4))
    o.append(curve(lambda t: abs(m(t)), 0, 2000, fx, fy, 300, NX, 2.2, '6 4'))
    o.append(curve(lambda t: -abs(m(t)), 0, 2000, fx, fy, 300, NX, 2.2, '6 4'))
    for t in (250, 750, 1250, 1750):
        o.append(L(fx(t), fy(23), fx(t), fy(-23), LV, 1.5, '3 3'))
    o.append(Tb(fx(250), fy(-23) + 18, '180° phase jump', 13, 'middle', LV))
    o.append(Tb(fx(1250), fy(-23) + 18, '180° phase jump', 13, 'middle', LV))
    o.append(Tb(fx(500), fy(15), 'envelope |20 cos 2π1000t|', 13, 'middle', NX))
    o.append(T(x0, 28, 's(t) = 20 cos 2π1000t · cos 2π100000t V (carrier drawn slowed)', 14, 'start', INK, True))
    o.append(T(x1, fy(-24) + 36, 't: two cycles of the 1 kHz tone (2 ms)', 13, 'end', MUT))
    X0, X1, Y0 = 140, 620, 410
    fX = lambda f: X0 + (f - 97) / 6 * (X1 - X0)
    fY = lambda v: Y0 - v * 8
    o.append(T(x0, 290, 'Spectrum: two 10 V lines, no carrier', 14, 'start', INK, True))
    o.append(L(X0 - 10, Y0, X1 + 10, Y0, L2, 1.5))
    for f in (97, 98, 99, 100, 101, 102, 103):
        o.append(L(fX(f), Y0, fX(f), Y0 + 5, L2, 1.2)); o.append(T(fX(f), Y0 + 20, str(f), 13, fill=MUT))
    o.append(T(X1 + 10, Y0 + 40, 'f (kHz)', 13, 'end', MUT))
    for f, lab in ((99, 'LSB 10 V'), (101, 'USB 10 V')):
        o.append(stem(fX(f), Y0, fY(10), AC)); o.append(T(fX(f), fY(10) - 12, lab, 14))
    o.append(L(fX(100), Y0, fX(100), fY(7), L2, 1.5, '4 4'))
    o.append(Tb(fX(100), fY(7) - 8, 'no line at 100 kHz', 13, 'middle', MUT))
    return 470, ''.join(o)


FIG[2] = (f2, 'The worked example: the DSB-SC wave follows 20 cos 2π1000t, so its envelope (dashed) is the rectified tone and the carrier flips phase at every zero. '
              'Its spectrum is just two 10 V lines at 99 and 101 kHz.',
          'Top: a DSB-SC wave with dashed envelope equal to the magnitude of a 20 V tone, with phase reversals marked at each zero of the tone. Bottom: two 10 volt lines at 99 and 101 kHz and no line at 100 kHz.')


# ---- 2.3 DSB-SC, USB and VSB of the 0.3-3.4 kHz speech band on 100 kHz ----
def f3():
    o = []
    X0, X1 = 90, 680
    fX = lambda f: X0 + (f - 96) / 8 * (X1 - X0)
    rows = [('DSB-SC', 80, 'B = 6.8 kHz'), ('USB', 200, 'B = 3.4 kHz'), ('VSB', 320, 'B = 3.9 kHz')]
    hb = 56
    def band_up(y, a, b, col):     # upper sideband: grows with audio frequency
        return poly([(fX(a), y), (fX(a), y - 14), (fX(b), y - hb), (fX(b), y)], col, AC, 1.8, 0.9)
    def band_dn(y, a, b, col):     # lower sideband: mirror image
        return poly([(fX(a), y), (fX(a), y - hb), (fX(b), y - 14), (fX(b), y)], col, AC, 1.8, 0.9)
    for name, y, bw in rows:
        o.append(L(X0 - 6, y, X1 + 6, y, L2, 1.5))
        o.append(L(fX(100), y + 4, fX(100), y - hb - 10, L2, 1.2, '4 4'))
        o.append(T(16, y - 20, name, 14, 'start', INK, True))
        o.append(T(16, y - 2, bw, 13, 'start', MUT))
    y = rows[0][1]
    o.append(band_dn(y, 96.6, 99.7, ACS)); o.append(band_up(y, 100.3, 103.4, ACS))
    o.append(T(fX(98.15), y - hb - 8, 'LSB', 13, fill=MUT)); o.append(T(fX(101.85), y - hb - 8 + 0, 'USB', 13, fill=MUT))
    o.append(T(fX(100), y + 18, '0.6 kHz gap at 100 kHz', 13, 'middle', LV))
    y = rows[1][1]
    o.append(band_up(y, 100.3, 103.4, ACS))
    o.append(T(fX(98.2), y - 20, 'LSB filtered off', 13, 'middle', MUT))
    y = rows[2][1]
    o.append(band_up(y, 100.3, 103.4, ACS))
    o.append(poly([(fX(99.5), y), (fX(99.5), y - 4), (fX(99.7), y - 9), (fX(99.7), y)], LVS, LV, 1.5))
    # VSB filter edge: gain 0 at 99.5, 0.5 at 100, 1 at 100.5
    o.append(P([(fX(99.0), y), (fX(99.5), y), (fX(100.5), y - 70), (fX(103.8), y - 70)], NX, 2.4, '7 4'))
    o.append(T(fX(100.65), y - 74, 'filter gain 1', 13, 'start', NX))
    o.append(C(fX(100), y - 35, 4, NX))
    o.append(T(fX(99.8), y - 40, 'gain 0.5 at 100 kHz', 13, 'end', NX))
    o.append(T(fX(97.6), y - 8, 'vestige 0.5 kHz', 13, 'middle', LV))
    for f in (96, 97, 98, 99, 100, 101, 102, 103, 104):
        o.append(L(fX(f), y, fX(f), y + 5, L2, 1.2)); o.append(T(fX(f), y + 20, str(f), 13, fill=MUT))
    o.append(T(X1 + 6, y + 40, 'f (kHz), carrier 100 kHz', 13, 'end', MUT))
    return 370, ''.join(o)


FIG[3] = (f3, 'Worked example 1, the 0.3 to 3.4 kHz speech band on a 100 kHz carrier. DSB-SC has two mirror-image sidebands with a 0.6 kHz gap at the carrier; '
              'the USB signal keeps the upper one (3.4 kHz); VSB keeps it plus a vestige below 100 kHz, with a filter edge (dashed) that is 0.5 at the carrier.',
          'Three spectra on a 96 to 104 kHz axis: DSB-SC with bands 96.6 to 99.7 and 100.3 to 103.4 kHz; USB with only 100.3 to 103.4 kHz; VSB with the upper band, a small vestige near 99.5 kHz and a dashed filter edge rising from 99.5 to 100.5 kHz.')


# ---- 2.4 every output line of the square-law device i = 10v + 2v^2 mA ----
def f4():
    o = []
    Y0 = 300; sc = 10.5                          # 1 mA = 10.5 px
    fY = lambda v: Y0 - v * sc
    segs = [(60, 220, 0, 3, [0, 1, 2, 3]), (270, 520, 98, 102, [98, 99, 100, 101, 102]), (570, 690, 199, 201, [199, 200, 201])]
    def fx(seg, f):
        a, b, f0, f1_, _ = seg; return a + (f - f0) / (f1_ - f0) * (b - a)
    for seg in segs:
        a, b, f0, f1_, ticks = seg
        o.append(L(a, Y0, b, Y0, L2, 1.5))
        for f in ticks:
            o.append(L(fx(seg, f), Y0, fx(seg, f), Y0 + 5, L2, 1.2)); o.append(T(fx(seg, f), Y0 + 20, str(f), 13, fill=MUT))
    for xb in (245, 545):                        # axis breaks
        o.append(L(xb - 10, Y0 + 8, xb - 2, Y0 - 8, L2, 1.5)); o.append(L(xb + 2, Y0 + 8, xb + 10, Y0 - 8, L2, 1.5))
    s0, s1, s2 = segs
    # band-pass window 99 to 101 kHz
    o.append(R(fx(s1, 98.8), fY(23.5), fx(s1, 101.2) - fx(s1, 98.8), Y0 - fY(23.5), ACS, AC, 6, 1.5, '6 4'))
    o.append(T(fx(s1, 100), fY(23.5) - 10, 'band-pass filter keeps 99 to 101 kHz', 14, 'middle', AC, True))
    lines = [(s0, 0, 4.25, MUT, '4.25'), (s0, 1, 5, MUT, '5'), (s0, 2, 0.25, MUT, '0.25'),
             (s1, 99, 2, LV, '2'), (s1, 100, 20, AC, '20 carrier'), (s1, 101, 2, LV, '2'), (s2, 200, 4, MUT, '4')]
    for seg, f, v, c, lab in lines:
        x = fx(seg, f); o.append(stem(x, Y0, fY(v), c)); o.append(T(x, fY(v) - 11, lab, 13))
    o.append(T(fx(s0, 1.5), fY(9.5), 'message and DC', 13, 'middle', MUT))
    o.append(T(fx(s0, 1.5), fY(9.5) + 17, '(from a_1v and a_2v²)'.replace('a_1', 'a<tspan baseline-shift="sub" font-size="10">1</tspan>').replace('a_2', 'a<tspan baseline-shift="sub" font-size="10">2</tspan>'), 13, 'middle', MUT))
    o.append(T(fx(s1, 100) + 110, fY(4.5), 'sidebands 2 mA', 13, 'start', LV))
    o.append(T(fx(s2, 200), fY(9.5), '2f<tspan baseline-shift="sub" font-size="10">c</tspan> harmonic', 13, 'middle', MUT))
    o.append(T(690, Y0 + 42, 'f (kHz), axis broken twice', 13, 'end', MUT))
    o.append(T(40, 24, 'Output current lines in mA for v = 2 cos ω<tspan baseline-shift="sub" font-size="10">c</tspan>t + 0.5 cos ω<tspan baseline-shift="sub" font-size="10">m</tspan>t', 14, 'start', INK, True))
    return 360, ''.join(o)


FIG[4] = (f4, 'Worked example 1: every line in the current of i = 10v + 2v² mA. Only the 20 mA carrier and the 2 mA sidebands at 99 and 101 kHz pass the filter, so m = 2 × 2/20 = 0.2; '
              'DC, the 1 and 2 kHz terms and the 4 mA line at 200 kHz are rejected.',
          'Line spectrum on a broken frequency axis: 4.25 mA DC, 5 mA at 1 kHz, 0.25 mA at 2 kHz; 2 mA at 99 kHz, 20 mA at 100 kHz, 2 mA at 101 kHz inside a dashed filter window; 4 mA at 200 kHz.')


# ---- 2.5 envelope detector circuit and its output ----
def f5():
    o = []
    # circuit: source, diode, R parallel C, coupling capacitor, R_i
    y1, y2 = 70, 190
    o.append(L(40, y2, 640, y2, INK, 2))                                     # ground rail
    o.append(f'<circle cx="60" cy="{(y1 + y2) / 2}" r="20" style="fill:var(--panel);stroke:var(--ink);stroke-width:2"/>')
    o.append(T(60, (y1 + y2) / 2 + 5, 'AM', 13, bold=True))
    o.append(L(60, y1, 60, (y1 + y2) / 2 - 20, INK, 2)); o.append(L(60, (y1 + y2) / 2 + 20, 60, y2, INK, 2))
    o.append(L(60, y1, 150, y1, INK, 2))
    o.append(poly([(150, y1 - 13), (150, y1 + 13), (176, y1)], 'var(--panel)', INK, 2)); o.append(L(177, y1 - 13, 177, y1 + 13, INK, 2.5))
    o.append(T(163, y1 - 22, 'diode', 13, fill=MUT))
    o.append(L(177, y1, 400, y1, INK, 2))
    # C (vertical) at x=240, R at x=320
    o.append(L(240, y1, 240, 118, INK, 2)); o.append(L(222, 118, 258, 118, INK, 2.5)); o.append(L(222, 128, 258, 128, INK, 2.5)); o.append(L(240, 128, 240, y2, INK, 2))
    o.append(T(266, 128, 'C = 2 nF', 13, 'start'))
    o.append(L(330, y1, 330, 100, INK, 2)); o.append(R(320, 100, 20, 50, 'var(--panel)', INK, 2, 2)); o.append(L(330, 150, 330, y2, INK, 2))
    o.append(T(348, 130, 'R = 10 kΩ', 13, 'start'))
    o.append(L(420, y1 - 14, 420, y1 + 14, INK, 2.5)); o.append(L(430, y1 - 14, 430, y1 + 14, INK, 2.5))
    o.append(L(400, y1, 420, y1, INK, 2)); o.append(L(430, y1, 560, y1, INK, 2))
    o.append(T(425, y1 - 22, 'C<tspan baseline-shift="sub" font-size="10">c</tspan> blocks DC', 13, fill=MUT))
    o.append(L(560, y1, 560, 100, INK, 2)); o.append(R(550, 100, 20, 50, 'var(--panel)', INK, 2, 2)); o.append(L(560, 150, 560, y2, INK, 2))
    o.append(T(578, 120, 'R<tspan baseline-shift="sub" font-size="10">i</tspan> = 40 kΩ', 13, 'start'))
    o.append(T(578, 140, 'next stage', 13, 'start', MUT))
    o.append(T(285, y2 + 22, 'RC = 20 µs', 14, 'middle', AC, True))
    o.append(T(440, y2 + 22, 'R<tspan baseline-shift="sub" font-size="10">ac</tspan> = 10 ∥ 40 = 8 kΩ', 13, 'start', MUT))
    # waveform: positive half of AM and the capacitor voltage (carrier slowed, 16 cycles per tone cycle)
    x0, x1, yb, sc = 60, 690, 420, 7.0
    Tm = 16.0; m = 0.6; Ac = 10
    fx = lambda t: x0 + t / (2 * Tm) * (x1 - x0)
    fy = lambda v: yb - v * sc
    o.append(L(x0, yb, x1, yb, L2, 1.2))
    s = lambda t: Ac * (1 + m * math.cos(2 * math.pi * t / Tm)) * math.cos(2 * math.pi * t)
    o.append(curve(lambda t: max(0.0, s(t)), 0, 2 * Tm, fx, fy, 1600, L2, 1.2))
    o.append(curve(lambda t: Ac * (1 + m * math.cos(2 * math.pi * t / Tm)), 0, 2 * Tm, fx, fy, 300, NX, 2, '6 4'))
    # ideal diode + RC, RC = 3 carrier periods here so the ripple is visible
    RC, dt, v, pts = 3.0, 0.002, 0.0, []
    t = 0.0
    while t <= 2 * Tm:
        v = max(s(t), v * math.exp(-dt / RC)); pts.append((fx(t), fy(v))); t += dt
    o.append(P(pts[::12], AC, 2.4))
    o.append(T(x0, 250, 'Detector output (solid) rides the carrier peaks and follows the envelope (dashed)', 14, 'start', INK, True))
    o.append(Tb(fx(1.2 * Tm), fy(15.2), 'envelope 10[1 + 0.6 cos 2πf<tspan baseline-shift="sub" font-size="10">m</tspan>t]', 13, 'middle', NX))
    o.append(T(x1, yb + 22, 'carrier drawn slowed; ripple exaggerated', 13, 'end', MUT))
    return 450, ''.join(o)


FIG[5] = (f5, 'Worked example 1: the diode charges C on each carrier peak and R discharges it between peaks; RC = 20 µs is 20 carrier periods and under the 42.4 µs clipping limit. '
              'C_c passes the audio to the 40 kΩ next stage, so the AC load is 8 kΩ and m up to 0.8 is not clipped.',
          'A diode feeds a 2 nF capacitor in parallel with a 10 kilohm resistor, then a coupling capacitor and a 40 kilohm next stage. Below, the rectified AM wave, its dashed envelope and the detector output following the peaks with a small sawtooth ripple.')


# ---- 2.6 low-level and high-level chains with the example powers ----
def f6():
    o = []
    def chain(y, boxes, title):
        o.append(T(20, y - 44, title, 14, 'start', INK, True))
        xs = []
        for i, (x, w, lines, fill) in enumerate(boxes):
            o.append(boxt(x, y - 28, w, 56, lines, fill, AC, 13))
            xs.append((x, w))
        for (xa, wa), (xb, wb) in zip(xs, xs[1:]):
            o.append(L(xa + wa, y, xb - 4, y, AC, 2, arrow='n'))
        return xs
    y = 90
    xs = chain(y, [(20, 96, ['crystal', 'oscillator'], PANEL), (140, 80, ['buffer'], PANEL), (244, 130, ['modulator', '2 W carrier'], ACS),
                   (398, 150, ['linear amplifier', '20 dB, 50 %'], PANEL), (572, 128, ['output', '264 W'], LVS)], 'Low-level: modulate at 2 W, then amplify linearly')
    o.append(boxt(244, y + 52, 130, 40, ['audio (small)'], NXS, NX, 13))
    o.append(L(309, y + 52, 309, y + 32, NX, 2, arrow='l'))
    o.append(T(473, y + 52, 'DC in 528 W', 13, 'middle', MUT))
    y = 290
    xs = chain(y, [(20, 96, ['crystal', 'oscillator'], PANEL), (140, 80, ['buffer'], PANEL), (244, 110, ['class C', 'driver'], PANEL),
                   (378, 170, ['class C final', 'η = 75 %'], ACS), (572, 128, ['output', '13.2 kW'], LVS)], 'High-level: amplify the carrier, modulate the final stage')
    o.append(boxt(378, y + 62, 170, 56, ['audio modulator', '4.27 kW to final'], NXS, NX, 13))
    o.append(L(463, y + 62, 463, y + 32, NX, 2, arrow='l'))
    o.append(T(463, y + 140, 'final stage supply V<tspan baseline-shift="sub" font-size="10">CC</tspan>[1 + 0.8 cos 2πf<tspan baseline-shift="sub" font-size="10">m</tspan>t]', 13, 'middle', MUT))
    o.append(T(463, y - 40, 'DC in 13.33 kW', 13, 'middle', MUT))
    return 446, ''.join(o)


FIG[6] = (f6, 'The two worked examples. Low-level: a 2 W carrier is modulated, then a 20 dB linear amplifier gives 264 W from 528 W of DC. '
              'High-level: class C stages amplify the bare carrier and the audio modulator varies the final stage supply, giving 13.2 kW at m = 0.8.',
          'Two block chains. Top: crystal oscillator, buffer, modulator at 2 W with audio input, linear amplifier of 20 dB, output 264 W. Bottom: crystal oscillator, buffer, class C driver, class C final at 75 percent efficiency fed by a 4.27 kW audio modulator, output 13.2 kW.')


# ---- 2.7 superhet chain, and the signal, LO and image on one axis ----
def f7():
    o = []
    y = 70
    boxes = [(14, 92, ['RF stage', '1000 kHz'], PANEL), (128, 84, ['mixer'], ACS), (234, 108, ['IF amp', '455 kHz'], PANEL),
             (364, 96, ['detector'], PANEL), (482, 84, ['audio'], PANEL)]
    for x, w, lines, fill in boxes:
        o.append(boxt(x, y - 26, w, 52, lines, fill, AC, 13))
    for (xa, wa, *_), (xb, *_r) in zip(boxes, boxes[1:]):
        o.append(L(xa + wa, y, xb - 4, y, AC, 2, arrow='n'))
    o.append(boxt(118, y + 58, 104, 44, ['LO 1455 kHz'], NXS, NX, 13))
    o.append(L(170, y + 58, 170, y + 30, NX, 2, arrow='l'))
    o.append(P([(412, y + 26), (412, y + 46), (60, y + 46), (60, y + 30)], MUT, 1.6, '5 4'))
    o.append(T(300, y + 64 - 4, 'AGC', 13, 'middle', MUT))
    o.append(L(584, y, 610, y, AC, 2, arrow='n'))
    o.append(T(616, y + 5, 'speaker', 13, 'start', MUT))
    # frequency axis
    X0, X1, Y0 = 60, 690, 380
    fX = lambda f: X0 + (f - 800) / 1200 * (X1 - X0)
    o.append(L(X0, Y0, X1, Y0, L2, 1.5))
    for f in (800, 1000, 1200, 1400, 1600, 1800, 2000):
        o.append(L(fX(f), Y0, fX(f), Y0 + 5, L2, 1.2)); o.append(T(fX(f), Y0 + 20, str(f), 13, fill=MUT))
    o.append(T(X1, Y0 + 40, 'f (kHz)', 13, 'end', MUT))
    # RF tuned-circuit response, Q = 100, scaled to 120 px
    resp = lambda f: 1 / math.sqrt(1 + (100 * (f / 1000 - 1000 / f)) ** 2)
    o.append(curve(lambda f: resp(f), 800, 2000, fX, lambda r: Y0 - 120 * r, 600, L2, 2))
    o.append(stem(fX(1000), Y0, Y0 - 120, AC)); o.append(T(fX(1000) + 8, Y0 - 112, 'signal f<tspan baseline-shift="sub" font-size="10">s</tspan> 1000', 13, 'start'))
    o.append(stem(fX(1455), Y0, Y0 - 80, NX)); o.append(T(fX(1455), Y0 - 92, 'LO 1455', 13))
    o.append(stem(fX(1910), Y0, Y0 - 120, LV)); o.append(T(fX(1910), Y0 - 132, 'image 1910', 13))
    o.append(L(fX(1000), Y0 - 50, fX(1452), Y0 - 50, MUT, 1.5, arrow='m')); o.append(L(fX(1458), Y0 - 50, fX(1907), Y0 - 50, MUT, 1.5, arrow='m'))
    o.append(Tb(fX(1227), Y0 - 50, '455', 13, 'middle', MUT)); o.append(Tb(fX(1683), Y0 - 50, '455', 13, 'middle', MUT))
    o.append(T(X0, Y0 + 42, 'the image reaches the mixer 138.6 times weaker (42.8 dB)', 13, 'start', LV))
    o.append(T(X0, 200, 'The RF tuning curve (Q = 100) is high at f<tspan baseline-shift="sub" font-size="10">s</tspan>, tiny at the image', 14, 'start', INK, True))
    return 430, ''.join(o)


FIG[7] = (f7, 'The worked example: tuned to 1000 kHz, the LO runs at 1455 kHz and the mixer gives the 455 kHz IF. The image at 1910 kHz also lies 455 kHz from the LO; '
              'only the RF tuned circuit (Q = 100, solid curve) can weaken it, by 138.6 times.',
          'Block chain: RF stage at 1000 kHz, mixer fed by a 1455 kHz local oscillator, IF amplifier at 455 kHz, detector, audio, with an AGC path back to the RF stage. Below, a frequency axis from 800 to 2000 kHz with the signal at 1000, LO at 1455 and image at 1910 kHz, 455 kHz apart, under the narrow tuning curve of the RF stage.')


# ---- 2.8 the 12-channel basic group, 60 to 108 kHz, and a zoom on the top two channels ----
def f8():
    o = []
    X0, X1, Y0 = 50, 690, 150
    fX = lambda f: X0 + (f - 58) / 52 * (X1 - X0)
    o.append(L(X0, Y0, X1, Y0, L2, 1.5))
    for i in range(12):
        fc = 64 + 4 * i
        a, b = fc - 3.4, fc - 0.3
        o.append(poly([(fX(a), Y0), (fX(a), Y0 - 52), (fX(b), Y0 - 12), (fX(b), Y0)], ACS if i % 2 else LVS, AC if i % 2 else LV, 1.4))
        o.append(L(fX(fc), Y0 + 2, fX(fc), Y0 - 64, MUT, 1.2, '3 3'))
    for f in (60, 64, 72, 80, 88, 96, 104, 108):
        o.append(L(fX(f), Y0, fX(f), Y0 + 5, L2, 1.2)); o.append(T(fX(f), Y0 + 20, str(f), 13, fill=MUT))
    o.append(T(X1, Y0 + 40, 'f (kHz); carriers dashed', 13, 'end', MUT))
    o.append(brace(fX(60), fX(108), Y0 - 76, INK, up=True))
    o.append(T(fX(84), Y0 - 84, 'basic group: 12 channels × 4 kHz = 48 kHz', 14, 'middle', INK, True))
    # zoom on 100 to 108 kHz
    Z0, Z1, ZY = 90, 650, 330
    fZ = lambda f: Z0 + (f - 100) / 8 * (Z1 - Z0)
    o.append(L(Z0, ZY, Z1, ZY, L2, 1.5))
    for a, b, fc, c, cs in ((100.6, 103.7, 104, AC, ACS), (104.6, 107.7, 108, LV, LVS)):
        o.append(poly([(fZ(a), ZY), (fZ(a), ZY - 70), (fZ(b), ZY - 16), (fZ(b), ZY)], cs, c, 1.8))
        o.append(L(fZ(fc), ZY + 2, fZ(fc), ZY - 86, MUT, 1.4, '3 3'))
        o.append(T(fZ(fc), ZY - 92, f'carrier {fc}', 13, 'middle', MUT))
        o.append(T(fZ((a + b) / 2), ZY + 40, f'{a} to {b}', 13, 'middle'))
    for f in (100, 101, 102, 103, 104, 105, 106, 107, 108):
        o.append(L(fZ(f), ZY, fZ(f), ZY + 5, L2, 1.2)); o.append(T(fZ(f), ZY + 20, str(f), 13, fill=MUT))
    o.append(brace(fZ(103.7), fZ(104.6), ZY - 26, INK, up=True))
    o.append(Tb(fZ(104.15), ZY - 34, 'guard 0.9', 13, 'middle', INK))
    o.append(T(Z0 - 40, 212, 'Zoom: the channels on the 104 and 108 kHz carriers (lower sidebands, kHz)', 14, 'start', INK, True))
    return 390, ''.join(o)


FIG[8] = (f8, 'Worked example 2: twelve 0.3 to 3.4 kHz voice channels sent as lower sidebands of the carriers 64 to 108 kHz fill 60 to 108 kHz. '
              'The zoom shows the two top channels, 100.6 to 103.7 and 104.6 to 107.7 kHz, with a 0.9 kHz guard band between them.',
          'Top: twelve sloped voice bands side by side from 60 to 108 kHz, each just below a dashed carrier line, total 48 kHz. Bottom: zoom on 100 to 108 kHz with bands 100.6 to 103.7 and 104.6 to 107.7 kHz and a 0.9 kHz guard band between.')


spec = make_spec(FIG)
