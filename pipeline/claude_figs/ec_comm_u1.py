"""Claude's hand-drawn figures for ec-comm-u1 (Communication: signals, noise and random processes), one per chapter.
Every number comes from that chapter's own worked example; colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
FC = 'f<tspan baseline-shift="sub" font-size="13">c</tspan>'
AFTER = {1: 3, 2: 4, 3: 2, 4: 3, 5: 3, 6: 2, 7: 3}


def sinc(u):
    return 1.0 if abs(u) < 1e-12 else math.sin(math.pi * u) / (math.pi * u)


def curve(f, a, b, fx, fy, n=300, c=AC, w=2.5, dash=None):
    return P([(fx(a + (b - a) * i / n), fy(f(a + (b - a) * i / n))) for i in range(n + 1)], c, w, dash)


def area(f, a, b, fx, fy, y0, fill, n=120):
    pts = [(fx(a), y0)] + [(fx(a + (b - a) * i / n), fy(f(a + (b - a) * i / n))) for i in range(n + 1)] + [(fx(b), y0)]
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" style="fill:{fill};stroke:none"/>'


def arrowv(x, y1, y2, c=AC):
    return L(x, y1, x, y2, c, 2.5, arrow='n' if c == AC else ('l' if c == LV else 'x'))


# ---- 1.1 the chain of blocks, and the antenna lengths of the worked example ----
def f1():
    o = []
    bw, gap, y, h = 106, 38, 92, 64
    xs = [16 + i * (bw + gap) for i in range(5)]
    names = [('Source', 'microphone'), ('Transmitter', 'modulates'), ('Channel', 'free space'), ('Receiver', 'demodulates'), ('Destination', 'loudspeaker')]
    for i, (x, (a, b)) in enumerate(zip(xs, names)):
        st = AC if i != 2 else NX
        o.append(boxt(x, y, bw, h, [a, b], fill=PANEL, stroke=st, size=14, bold_first=True))
    sig = ['m(t)', 's(t)', 'r(t)', 'm̂(t)']
    for i in range(4):
        x1, x2 = xs[i] + bw, xs[i + 1]
        o.append(L(x1 + 2, y + h / 2, x2 - 3, y + h / 2, AC, 2.5, arrow='n'))
        o.append(T((x1 + x2) / 2, y + h / 2 + 24, sig[i], 14, fill=INK, bold=True))
    cx = xs[2] + bw / 2
    o.append(boxt(cx - 62, 16, 124, 40, ['noise n(t)'], fill=NXS, stroke=NX, size=14))
    o.append(L(cx, 56, cx, y - 3, NX, 2.5, '6 4', arrow='x'))
    o.append(T(360, 186, 'r(t) = s(t) + n(t): the channel adds noise to what the transmitter sent', 14, fill=MUT))
    # antenna lengths on a log scale, 0.1 m to 100 km
    x0, x1 = 150, 690
    fx = lambda m: x0 + (math.log10(m) + 1) / 6 * (x1 - x0)
    o.append(T(16, 222, 'Quarter-wave antenna λ/4 = c/(4f), log scale', 14, 'start', INK, True))
    rows = [(250, 75e3, '1 kHz tone', 'λ/4 = 75 km', NX, NXS), (290, 0.75, '100 MHz carrier', 'λ/4 = 0.75 m', AC, ACS)]
    for yy, val, lab, txt, c, s in rows:
        o.append(T(x0 - 10, yy + 5, lab, 14, 'end'))
        o.append(R(x0, yy - 11, fx(val) - x0, 22, s, c, 4))
        o.append(T(fx(val) + 8, yy + 5, txt, 14, 'start', INK, True) if val < 1e3 else T(fx(val) - 8, yy + 5, txt, 14, 'end', INK, True))
    ticks = [(0.1, '0.1 m'), (1, '1 m'), (10, '10 m'), (100, '100 m'), (1e3, '1 km'), (1e4, '10 km'), (1e5, '100 km')]
    o.append(L(x0, 318, x1, 318, L2, 1.5))
    for v, s in ticks:
        o += [L(fx(v), 318, fx(v), 323, L2, 1.5), T(fx(v), 338, s, 13, fill=MUT)]
    o.append(T(420, 364, 'Modulation onto 100 MHz shortens the antenna 10⁵ times', 14, fill=MUT))
    return 378, ''.join(o)
FIG[1] = (f1, 'The five blocks of a communication system, with noise entering at the channel. Below, the worked example on a log scale: a quarter-wave antenna for the 1 kHz tone is 75 km long, but for the 100 MHz carrier it is 0.75 m.',
          'Block chain source, transmitter, channel, receiver, destination with signals m(t), s(t), r(t) and the estimate, noise feeding the channel; below, bars of 75 km and 0.75 m on a log scale.')


# ---- 1.2 the pulse spectrum and its band-pass copy ----
def f2():
    o = []
    y0, y1 = 100, 300
    # left: baseband |X(f)|, f in kHz from -3 to 3, height mV/Hz 0..2.2
    a0, a1 = 70, 330
    fxa = lambda f: a0 + (f + 3) / 6 * (a1 - a0)
    fy = lambda v: y1 - v / 2.2 * (y1 - y0)
    o.append(axes(a0, a1, y0, y1, [-3, -2, -1, 0, 1, 2, 3], [0, 1, 2], fxa, fy, 'f (kHz)', '|X(f)| (mV/Hz)', neg))
    o.append(area(lambda f: 2 * abs(sinc(f)), -1, 1, fxa, fy, y1, ACS))
    o.append(curve(lambda f: 2 * abs(sinc(f)), -3, 3, fxa, fy, 400, AC, 2.5))
    o.append(L(fxa(-0.443), fy(1.414), fxa(0.443), fy(1.414), LV, 2))
    o.append(C(fxa(-0.443), fy(1.414), 4, LV)); o.append(C(fxa(0.443), fy(1.414), 4, LV))
    o.append(Tb(fxa(0.5) + 6, fy(1.414) - 8, '3 dB at ±443 Hz', 13, 'start'))
    o.append(Tb(fxa(0) + 8, fy(2) - 8, '2 mV/Hz', 13, 'start'))
    o.append(Tb(fxa(1.05), fy(0.8), 'null at 1 kHz', 13, 'start'))
    o.append(L(fxa(1.15), fy(0.8) + 5, fxa(1.0), y1 - 4, L2, 1.5, arrow='m'))
    o.append(T((a0 + a1) / 2, 24, 'baseband pulse: 2 V, T = 1 ms', 14, bold=True))
    # right: |Y(f)| near +10 kHz, f from 7 to 13 kHz
    b0, b1 = 420, 690
    fxb = lambda f: b0 + (f - 7) / 6 * (b1 - b0)
    o.append(axes(b0, b1, y0, y1, [7, 8, 9, 10, 11, 12, 13], [0, 1, 2], fxb, fy, 'f (kHz)', '|Y(f)| (mV/Hz)'))
    o.append(curve(lambda f: 2 * abs(sinc(f - 10)), 7, 13, fxb, fy, 300, L2, 1.5, '6 4'))
    o.append(area(lambda f: abs(sinc(f - 10)), 9, 11, fxb, fy, y1, LVS))
    o.append(curve(lambda f: abs(sinc(f - 10)), 7, 13, fxb, fy, 400, LV, 2.5))
    o.append(Tb(fxb(10) + 8, fy(1) - 8, '1 mV/Hz', 13, 'start'))
    o.append(brace(fxb(9), fxb(11), y1 + 46, INK, up=True))
    o.append(T(fxb(10), y1 + 64, '9 to 11 kHz: 2 kHz null to null', 13))
    o.append(T((b0 + b1) / 2, 24, 'after × cos(2π·10 kHz·t)', 14, bold=True))
    o.append(T((b0 + b1) / 2, 44, 'dashed: baseband shape, for comparison', 13, fill=MUT))
    o.append(T((b0 + b1) / 2, 62, 'a mirror copy sits at −10 kHz', 13, fill=MUT))
    return 382, ''.join(o)
FIG[2] = (f2, 'Worked examples 1 and 2. Left: the 2 V, 1 ms pulse has a sinc spectrum of peak 2 mV/Hz, first nulls at ±1 kHz and half-power points at ±443 Hz. Right: on a 10 kHz carrier each copy has half the height, 1 mV/Hz, and fills 9 to 11 kHz.',
          'Left, the sinc magnitude spectrum of the pulse with peak 2 millivolt per hertz, nulls at plus and minus 1 kilohertz and half-power points at 443 hertz. Right, the copy centred on 10 kilohertz with peak 1 millivolt per hertz between nulls at 9 and 11 kilohertz.')


# ---- 1.3 spectra of x, the analytic signal and the complex envelope ----
def f3():
    o = []
    x0, x1 = 200, 700
    fx = lambda f: x0 + (f + 1.4) / 2.8 * (x1 - x0)
    rows = [(130, 'X(f)', [(-1, 1, '1∠−30°'), (1, 1, '1∠30°')], 'spectrum of x(t)'),
            (290, 'Xₐ(f)', [(1, 2, '2∠30°')], 'analytic signal x + j x̂'),
            (450, 'X̃(f)', [(0, 2, '2∠30° = 1.732 + j1')], 'complex envelope')]
    sc = 40
    for yb, name, stems, note in rows:
        o.append(L(x0, yb, x1 - 10, yb, L2, 1.5))
        for f, lab in ((-1, '−' + FC), (0, '0'), (1, FC)):
            o.append(L(fx(f), yb, fx(f), yb + 5, L2, 1.5))
            o.append(T(fx(f), yb + 22, lab, 15, fill=MUT))
        o.append(T(16, yb - 30, name, 17, 'start', INK, True))
        o.append(T(16, yb - 8, note, 14, 'start', MUT))
        for f, hgt, lab in stems:
            c = AC if name == 'X(f)' else (LV if name.startswith('Xₐ') else NX)
            o.append(L(fx(f), yb, fx(f), yb - hgt * sc, c, 3, arrow='n' if c == AC else ('l' if c == LV else 'x')))
            o.append(Tb(fx(f) + 10, yb - hgt * sc + 8, lab, 14, 'start', INK, True))
    o.append(T(16, 30, 'x(t) = 2 cos(2π' + FC + 't + 30°) V, worked example 1', 15, 'start', INK, True))
    o.append(T(fx(0), 190, '↓ × [1 + sgn f]: the negative half goes, the positive half doubles', 14, fill=MUT))
    o.append(T(fx(0), 350, '↓ × e<tspan baseline-shift="super" font-size="13">−j2πfct</tspan>: everything slides down by ' + FC, 14, fill=MUT))
    return 484, ''.join(o)
FIG[3] = (f3, 'Worked example 1 in frequency. x(t) has two half-size impulses at ±f<sub>c</sub>; the analytic signal keeps only the positive one, doubled to 2∠30°; the complex envelope moves it to 0 Hz, where it reads 1.732 + j1, so I = 1.732 V and Q = 1 V.',
          'Three stacked spectra: two impulses of weight 1 at minus and plus fc; one impulse of weight 2 at plus fc; one impulse of weight 2 at zero labelled 1.732 plus j1.')


# ---- 1.4 Gaussian noise: the tail beyond 4 mV and the band within 2 mV ----
def f4():
    o = []
    x0, x1, y0, y1 = 70, 690, 70, 290
    sg = 2.0
    pdf = lambda v: math.exp(-v * v / (2 * sg * sg)) / (sg * math.sqrt(2 * math.pi))
    fx = lambda v: x0 + (v + 8) / 16 * (x1 - x0)
    fy = lambda p: y1 - p / 0.22 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [-8, -6, -4, -2, 0, 2, 4, 6, 8], [0, 0.1, 0.2], fx, fy, 'noise voltage v (mV)', 'PDF (per mV)', neg))
    o.append(area(pdf, -2, 2, fx, fy, y1, ACS))
    o.append(area(pdf, 4, 8, fx, fy, y1, NXS))
    o.append(curve(pdf, -8, 8, fx, fy, 400, AC, 2.5))
    for v in (-2, 2):
        o.append(L(fx(v), y1, fx(v), fy(pdf(v)), AC, 1.5, '4 3'))
    o.append(L(fx(4), y1, fx(4), fy(pdf(4)) - 30, NX, 2))
    o.append(Tb(fx(0), fy(0.08), 'area 0.6827', 14, bold=True))
    o.append(Tb(fx(0), fy(0.055), '(−2 to 2 mV)', 13))
    o.append(T(fx(4) + 8, fy(pdf(4)) - 34, 'threshold 4 mV = 2σ', 14, 'start', INK, True))
    o.append(L(fx(5.6), fy(0.012), fx(5.2), y1 - 6, NX, 1.5, arrow='x'))
    o.append(Tb(fx(5.2), fy(0.035), 'tail = Q(2) = 0.0228', 14, 'start', INK, True))
    o.append(T(fx(-8), 40, 'μ = 0, σ = 2 mV; the peak is 1/(σ√(2π)) = 0.199 per mV', 14, 'start', INK))
    return 340, ''.join(o)
FIG[4] = (f4, 'Worked example 1: Gaussian noise with σ = 2 mV. The shaded tail beyond 4 mV (z = 2) has area Q(2) = 0.0228; the band from −2 to 2 mV has area 0.6827. Probability is always an area under the curve, never its height.',
          'A Gaussian PDF of noise voltage with standard deviation 2 millivolts; the central band from minus 2 to 2 millivolts is shaded with area 0.6827 and the tail beyond 4 millivolts with area 0.0228.')


# ---- 1.5 band-limited white noise: PSD rectangle and the sinc autocorrelation ----
def f5():
    o = []
    y0, y1 = 70, 290
    a0, a1 = 70, 320
    fxa = lambda f: a0 + (f + 20) / 40 * (a1 - a0)
    fya = lambda s: y1 - s / 1.3 * (y1 - y0)
    o.append(axes(a0, a1, y0, y1, [-20, -10, 0, 10, 20], [0, 0.5, 1], fxa, fya, 'f (kHz)', 'S<tspan baseline-shift="sub" font-size="13">Y</tspan>(f) (µW/Hz)', neg))
    o.append(R(fxa(-10), fya(1), fxa(10) - fxa(-10), fya(0) - fya(1), ACS, AC, 0))
    o.append(Tb(fxa(0), fya(0.5), 'area 20 mW', 14, bold=True))
    o.append(T(fxa(0), fya(1) - 10, '1 µW/Hz from −10 to 10 kHz', 13))
    o.append(T((a0 + a1) / 2, 26, 'output PSD', 14, bold=True))
    b0, b1 = 420, 690
    fxb = lambda t: b0 + (t + 200) / 400 * (b1 - b0)
    fyb = lambda r: y1 - (r + 6) / 30 * (y1 - y0)
    yz = fyb(0)
    o.append(L(b0, yz, b1, yz, L2, 1.5)); o.append(L(fxb(0), y0 - 4, fxb(0), y1, L2, 1.5))
    for t in (-200, -100, 0, 100, 200):
        o += [L(fxb(t), yz, fxb(t), yz + 5, L2, 1.5)]
    o.append(L(b0, y1, b1, y1, 'var(--line)', 1))
    for t in (-200, -100, 0, 100, 200):
        o.append(L(fxb(t), y1, fxb(t), y1 + 5, L2, 1.5))
        o.append(T(fxb(t), y1 + 20, neg(t), 13, fill=MUT))
    for r in (10, 20):
        o += [L(b0 - 4, fyb(r), b0, fyb(r), L2, 1.5), T(b0 - 8, fyb(r) + 4.5, str(r), 13, 'end', MUT)]
    o.append(L(b0, y0, b0, y1, L2, 1.5))
    o.append(T((b0 + b1) / 2, y1 + 40, 'τ (µs)', 14, fill=MUT))
    o.append(T(b0, y0 - 12, 'R<tspan baseline-shift="sub" font-size="13">Y</tspan>(τ) (mW)', 14, 'start', MUT))
    o.append(curve(lambda t: 20 * sinc(2e4 * t * 1e-6), -200, 200, fxb, fyb, 500, LV, 2.5))
    for t in (-150, -100, -50, 50, 100, 150):
        o.append(C(fxb(t), yz, 4, NX))
    o.append(T(b0 - 8, yz + 4.5, '0', 13, 'end', MUT))
    o.append(Tb(fxb(0) + 8, fyb(20) + 4, '20 mW at τ = 0', 13, 'start'))
    o.append(T((b0 + b1) / 2, 26, 'its autocorrelation', 14, bold=True))
    o.append(T(360, 366, 'Fourier pair: rectangle of half-width B = 10 kHz ↔ 2SB sinc(2Bτ), zeros every 1/(2B) = 50 µs', 13, fill=MUT))
    return 380, ''.join(o)
FIG[5] = (f5, 'Worked example 1: white noise through the 10 kHz low-pass filter. The output PSD is a 1 µW/Hz rectangle of area 20 mW; its transform, R<sub>Y</sub>(τ) = 20 mW × sinc(2×10<sup>4</sup>τ), peaks at the power and is zero every 50 µs.',
          'Left, a rectangular power spectral density of height 1 microwatt per hertz between minus and plus 10 kilohertz. Right, a sinc-shaped autocorrelation peaking at 20 milliwatts with zeros every 50 microseconds.')


# ---- 1.6 thermal noise of the 1 kOhm resistor: model and power in the band ----
def f6():
    o = []
    # circuit: noise source in series with R, feeding a matched load
    y_top, y_bot = 50, 170
    xs, xr, xl = 80, 200, 400
    o.append(f'<circle cx="{xs}" cy="{(y_top + y_bot) / 2}" r="22" style="fill:var(--panel);stroke:var(--next);stroke-width:2"/>')
    o.append(T(xs, (y_top + y_bot) / 2 + 6, '~', 20, bold=True))
    o.append(T(xs - 30, (y_top + y_bot) / 2 + 5, 'vₙ', 15, 'end', INK, True))
    o.append(L(xs, y_top, xs, (y_top + y_bot) / 2 - 22, INK, 2)); o.append(L(xs, (y_top + y_bot) / 2 + 22, xs, y_bot, INK, 2))
    o.append(L(xs, y_top, xr - 40, y_top, INK, 2))
    zz = [(xr - 40, y_top)] + [(xr - 40 + 10 * i, y_top + (-8 if i % 2 else 8)) for i in range(1, 8)] + [(xr + 40, y_top)]
    o.append(P(zz, INK, 2))
    o.append(T(xr, y_top - 16, 'R = 1 kΩ, 290 K', 14, bold=True))
    o.append(L(xr + 40, y_top, xl, y_top, INK, 2))
    o.append(L(xs, y_bot, xl, y_bot, INK, 2))
    o.append(R(xl - 16, y_top + 20, 32, y_bot - y_top - 40, PANEL, AC, 3))
    o.append(L(xl, y_top, xl, y_top + 20, INK, 2)); o.append(L(xl, y_bot - 20, xl, y_bot, INK, 2))
    o.append(T(xl + 26, (y_top + y_bot) / 2 - 4, 'matched load 1 kΩ', 14, 'start', INK, True))
    o.append(T(xl + 26, (y_top + y_bot) / 2 + 16, 'sees vₙ/2 = 2.0 µV', 14, 'start'))
    o.append(T(xs + 6, y_bot + 26, 'noiseless R with vₙ = √(4kTRB) = 4.0 µV rms in series', 13, 'start', MUT))
    # PSD: flat N0/2 with the band shaded
    x0, x1, yb, yl = 70, 690, 340, 270
    fx = lambda f: x0 + (f + 3) / 6 * (x1 - x0)
    o.append(L(x0, yb, x1, yb, L2, 1.5))
    for f in (-3, -2, -1, 0, 1, 2, 3):
        o += [L(fx(f), yb, fx(f), yb + 5, L2, 1.5), T(fx(f), yb + 20, neg(f), 13, fill=MUT)]
    o.append(T(x1, yb + 40, 'f (MHz)', 14, 'end', MUT))
    o.append(R(fx(-1), yl, fx(1) - fx(-1), yb - yl, ACS, AC, 0))
    o.append(L(x0, yl, x1, yl, LV, 2.5))
    o.append(T(fx(-3), yl - 12, 'S(f) = N₀/2 = 2.0×10⁻²¹ W/Hz at every f', 14, 'start', INK, True))
    o.append(Tb(fx(0), yl + 28, 'low-pass band', 13))
    o.append(Tb(fx(0), yl + 48, '|f| ≤ B = 1 MHz', 13))
    o.append(T(fx(1) + 14, yl + 24, 'area = (N₀/2)(2B) = N₀B', 14, 'start', INK, True))
    o.append(T(fx(1) + 14, yl + 46, '= 4.0×10⁻¹⁵ W = −114 dBm', 14, 'start', INK, True))
    return 386, ''.join(o)
FIG[6] = (f6, 'Worked example 1. Top: the 1 kΩ resistor as a noiseless resistor in series with a 4.0 µV rms noise source; a matched load receives kTB. Bottom: the flat two-sided PSD N<sub>0</sub>/2; the shaded receiver band holds N<sub>0</sub>B = 4.0×10<sup>−15</sup> W, that is −114 dBm.',
          'A noise voltage source in series with a 1 kilohm resistor drives a matched 1 kilohm load; below, a flat power spectral density with the band from minus 1 to plus 1 megahertz shaded, holding 4 femtowatts.')


# ---- 1.7 order of stages: noise temperature contributions ----
def f7():
    o = []
    rows = [(70, '(a) cable first', [('cable', '2 dB loss'), ('LNA', 'NF 1 dB'), ('mixer', 'NF 8 dB')], [169.6, 119.0, 24.4], 313.0, 363.0),
            (210, '(b) LNA first', [('LNA', 'NF 1 dB'), ('cable', '2 dB loss'), ('mixer', 'NF 8 dB')], [75.1, 1.7, 24.4], 101.2, 151.2)]
    colour = {'cable': (NX, NXS), 'LNA': (AC, ACS), 'mixer': (LV, LVS)}
    bx0 = 330
    sc = 0.8
    for y, title, st, terms, te, ts in rows:
        o.append(T(16, y - 22, title, 15, 'start', INK, True))
        for i, (n, note) in enumerate(st):
            x = 16 + i * 102
            c, s = colour[n]
            o.append(boxt(x, y - 4, 86, 48, [n, note], fill=s, stroke=c, size=13, bold_first=True))
            if i < 2: o.append(L(x + 87, y + 20, x + 101, y + 20, L2, 2, arrow='m'))
        x = bx0
        for (n, _), v in zip(st, terms):
            c, s = colour[n]
            wdt = v * sc
            o.append(R(x, y, max(wdt, 2), 40, s, c, 2))
            if wdt > 45: o.append(T(x + wdt / 2, y + 26, f'{v:.1f}', 14, bold=True))
            x += wdt
        o.append(T(x + 8, y + 18, f'Tₑ = {te:.1f} K', 14, 'start', INK, True))
        o.append(T(x + 8, y + 37, 'T<tspan baseline-shift="sub" font-size="13">sys</tspan> = ' + f'{ts:.1f} K', 13, 'start', MUT))
    o.append(T(bx0, 210 + 72, 'with the LNA first, the cable adds only 1.7 K', 13, 'start', MUT))
    o.append(L(bx0, 310, bx0 + 300 * sc, 310, L2, 1.5))
    for v in (0, 100, 200, 300):
        o += [L(bx0 + v * sc, 310, bx0 + v * sc, 315, L2, 1.5), T(bx0 + v * sc, 330, str(v), 13, fill=MUT)]
    o.append(T(bx0 + 150 * sc, 352, 'noise temperature referred to the input (K)', 14, fill=MUT))
    return 366, ''.join(o)
FIG[7] = (f7, 'Worked example 2: each bar splits the receiver noise temperature into the share of each stage. With the cable first the LNA term grows to 119.0 K and T<sub>e</sub> = 313.0 K; with the LNA first the cable adds only 1.7 K and T<sub>e</sub> = 101.2 K.',
          'Two receiver chains, cable then LNA then mixer, and LNA then cable then mixer, each with a stacked bar of noise temperature contributions: 169.6, 119.0 and 24.4 kelvin totalling 313.0; and 75.1, 1.7 and 24.4 kelvin totalling 101.2.')


spec = make_spec(FIG)
