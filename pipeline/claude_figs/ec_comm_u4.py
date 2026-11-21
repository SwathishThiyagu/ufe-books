"""Claude's hand-drawn figures for ec-comm-u4 (Sampling and Pulse Modulation), one per chapter, plus the line-code
waveforms in one model answer. Every number comes from the chapter's own worked example. Colours are the shell's CSS
variables; arrowheads are url(#ar-UID-n|m|l|x)."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
pi, sin, cos, log, log10, sqrt = math.pi, math.sin, math.cos, math.log, math.log10, math.sqrt


def num(v, d=1):
    s = f'{v:.{d}f}'
    return s.replace('-', '−')


def legend(x, y, items, size=13, gap=18):
    """items: (colour, dash, label); a short line sample then the label, laid out left to right"""
    o = []
    for c, dash, lab in items:
        o.append(L(x, y - 4, x + 26, y - 4, c, 3, dash))
        o.append(T(x + 32, y, lab, size, 'start', INK))
        x += 32 + tw(lab, size) + gap
    return ''.join(o)


# ---- 4.1: aliasing at fs = 7 kHz, in time and in frequency ----
def f1():
    o = []
    fs = 7000.0
    # top: time, 0 .. 1 ms
    X0, X1, Y0, Y1 = 70, 690, 48, 188
    fx = lambda t: X0 + (X1 - X0) * t / 1e-3
    fy = lambda v: (Y0 + Y1) / 2 - (Y1 - Y0) / 2 * v / 2.2
    o.append(L(X0, fy(0), X1, fy(0), L2, 1.5))
    o.append(L(X0, Y0 - 6, X0, Y1 + 4, L2, 1.5))
    for v in (-2, 0, 2):
        o.append(T(X0 - 9, fy(v) + 4.5, neg(v), 13, 'end', MUT))
    o.append(T(X0, Y0 - 16, 'volts', 13, 'start', MUT))
    ts = [i * 1e-6 for i in range(0, 1001, 4)]
    o.append(P([(fx(t), fy(2 * cos(2 * pi * 4000 * t))) for t in ts], AC, 2.2))
    o.append(P([(fx(t), fy(2 * cos(2 * pi * 3000 * t))) for t in ts], LV, 2.2, '7 4'))
    for n in range(8):
        t = n / fs
        o.append(L(fx(t), fy(0), fx(t), fy(2 * cos(2 * pi * 4000 * t)), L2, 1.2, '2 3'))
        o.append(C(fx(t), fy(2 * cos(2 * pi * 4000 * t)), 5.5, INK))
    for n, lab in ((0, '0'), (7, '1 ms')):
        o.append(T(fx(n / fs), Y1 + 22, lab, 13, fill=MUT))
    o.append(T(fx(3.5 / fs), Y1 + 22, 'samples every Tₛ = 1/7000 s = 143 µs', 13, fill=MUT))
    o.append(legend(150, 24, [(AC, None, '4 kHz sent'), (LV, '7 4', '3 kHz alias')]))
    o.append(C(452, 20, 5.5, INK)); o.append(T(464, 24, 'the samples they share', 13, 'start', INK))
    # bottom: spectrum of the samples, 0 .. 12 kHz
    S0, S1, B0, B1 = 70, 690, 262, 418
    gx = lambda f: S0 + (S1 - S0) * f / 12.0
    gy = lambda a: B1 - (B1 - B0 - 20) * a / 3.0
    o.append(f'<rect x="{gx(0):.1f}" y="{B0 - 4:.1f}" width="{gx(3.5) - gx(0):.1f}" height="{B1 - B0 + 4:.1f}" style="fill:{ACS}"/>')
    o.append(T(gx(2), B1 - 40, 'filter', 13, fill=AC, bold=True)); o.append(T(gx(2), B1 - 22, 'passband', 13, fill=AC, bold=True))
    o.append(xaxis(S0, S1, B1, list(range(0, 13)), gx, 'frequency (kHz)', lambda v: str(v)))
    o.append(L(gx(3.5), B0 - 4, gx(3.5), B1, INK, 1.6, '5 4'))
    o.append(Tb(gx(3.5) + 4, B0 + 34, 'fₛ/2 = 3.5', 13, 'start', INK))
    o.append(L(gx(7), B0 + 40, gx(7), B1, L2, 1.4, '3 4'))
    o.append(Tb(gx(7), B0 + 34, 'fₛ = 7', 13, 'middle', MUT))
    for f, a, c in ((1, 3, AC), (6, 3, AC), (8, 3, AC), (4, 2, LV), (3, 2, LV), (10, 2, LV), (11, 2, LV)):
        o.append(L(gx(f), B1, gx(f), gy(a), c, 4))
        o.append(C(gx(f), gy(a), 4, c))
    o.append(Tb(gx(1), gy(3) - 10, '1 kHz', 13, fill=AC, bold=True))
    o.append(Tb(gx(3), gy(2) - 26, 'alias 3', 13, fill=LV, bold=True))
    o.append(Tb(gx(4) + 4, gy(2) - 10, '4', 13, fill=LV))
    o.append(Tb(gx(7), gy(3) - 10, '6 and 8: 7 ∓ 1', 13, fill=AC))
    o.append(Tb(gx(10.5), gy(2) - 10, '10 and 11: 14 − 4, 7 + 4', 13, fill=LV))
    return 470, ''.join(o)


FIG[1] = (f1, 'Top: at 7000 samples/s the 4 kHz cosine and a 3 kHz cosine pass through the very same samples. Bottom: the spectrum of the samples repeats every 7 kHz, so the 4 kHz family (lines 3, 4, 10, 11) puts a line at 3 kHz inside the 3.5 kHz reconstruction filter.',
          'Time plot of a 4 kilohertz and a 3 kilohertz cosine through the same samples at 7000 samples per second, and the sampled spectrum with lines at 1, 3, 4, 6, 8, 10 and 11 kilohertz and a filter passband to 3.5 kilohertz.')


# ---- 4.2: PAM, PWM and PPM for the samples +2, +1, -1, -3 V ----
def f2():
    o = []
    m = [2, 1, -1, -3]
    X0, X1 = 120, 700
    fx = lambda t: X0 + (X1 - X0) * t / 400.0     # t in µs
    rows = [('samples', 36, 112), ('PAM', 144, 222), ('PWM', 252, 312), ('PPM', 346, 402)]
    for name, top, bot in rows:
        o.append(T(16, (top + bot) / 2 + 5, name, 15, 'start', INK, True))
    for k in range(5):
        o.append(L(fx(100 * k), 30, fx(100 * k), 412, L2, 1, '3 4'))
    # samples: stems on a zero line
    z = 74; sc = 11.5
    o.append(L(X0, z, X1, z, L2, 1.5))
    for k, v in enumerate(m):
        x = fx(100 * k + 10)
        o.append(L(x, z, x, z - sc * v, INK, 2)); o.append(C(x, z - sc * v, 5, INK))
        o.append(Tb(x + 14, z - sc * v + (5 if v > 0 else 9), f'{neg(f"{v:+d}")} V', 13, 'start', INK))
    # PAM: flat-top 20 µs pulses, height = sample
    z = 183; sc = 12
    o.append(L(X0, z, X1, z, L2, 1.5))
    for k, v in enumerate(m):
        a, b = fx(100 * k), fx(100 * k + 20)
        y = z - sc * v
        o.append(f'<rect x="{a:.1f}" y="{min(y, z):.1f}" width="{b - a:.1f}" height="{abs(z - y):.1f}" style="fill:{ACS};stroke:{AC};stroke-width:2"/>')
    o.append(T(fx(60), 160, 'height = sample, 20 µs wide', 13, 'start', MUT))
    # PWM: leading edge fixed, width 50 + 10 m µs
    lo, hi = 306, 262
    pts = []
    for k, v in enumerate(m):
        s, e = 100 * k, 100 * k + 50 + 10 * v
        pts += [(fx(s), lo), (fx(s), hi), (fx(e), hi), (fx(e), lo)]
        o.append(T((fx(s) + fx(e)) / 2, hi - 6, f'{50 + 10 * v} µs', 13, fill=LV, bold=True))
    o.append(P([(fx(0), lo)] + pts + [(fx(400), lo)], LV, 2.5))
    # PPM: 5 µs pulse at each trailing edge, nominal position dashed
    lo, hi = 396, 352
    pts = []
    for k, v in enumerate(m):
        e = 100 * k + 50 + 10 * v
        pts += [(fx(e), lo), (fx(e), hi), (fx(e + 5), hi), (fx(e + 5), lo)]
        o.append(L(fx(100 * k + 50), hi - 2, fx(100 * k + 50), lo, NX, 1.6, '4 3'))
        sh = 10 * v
        o.append(Tb((fx(e) + fx(100 * k + 50)) / 2 + 2, hi - 8, f'{neg(f"{sh:+d}")} µs', 13, 'middle', NX, True))
    o.append(P([(fx(0), lo)] + pts + [(fx(400), lo)], AC, 2.5))
    for k in range(5):
        o.append(T(fx(100 * k), 428, f'{100 * k}', 13, fill=MUT))
    o.append(T(16, 428, 'time (µs)', 13, 'start', MUT))
    o.append(T(fx(200), 446, 'dashed: unmodulated PPM position (50 µs into each slot); numbers: shift in µs', 13, 'middle', MUT))
    return 456, ''.join(o)


FIG[2] = (f2, 'The samples +2, +1, −1 and −3 V of the worked example as PAM (pulse height), PWM (width 50 + 10m µs, trailing edge moving) and PPM (a fixed 5 µs pulse placed at each PWM trailing edge, shifted +20, +10, −10 and −30 µs).',
          'Four rows over 400 microseconds: sample stems of plus 2, plus 1, minus 1 and minus 3 volts; flat-top PAM pulses of those heights; PWM pulses 70, 60, 40 and 20 microseconds wide; PPM pulses shifted plus 20, plus 10, minus 10 and minus 30 microseconds from dashed nominal positions.')


# ---- 4.3: the two compressor curves, and what they do to SQNR ----
MU, AA = 255.0, 87.6
def mu_c(x): return log(1 + MU * x) / log(1 + MU)
def a_c(x): return AA * x / (1 + log(AA)) if x <= 1 / AA else (1 + log(AA * x)) / (1 + log(AA))
def sq_unif(a, n=8): return 10 * log10((a * a / 2) / ((2 / 2 ** n) ** 2 / 12))
def sq_mu(a, n=8):
    E = 1 + 2 * MU * (2 * a / pi) + MU * MU * a * a / 2
    return 10 * log10((a * a / 2) / ((2 / 2 ** n) ** 2 / 12 * (log(1 + MU) / MU) ** 2 * E))


def f3():
    o = []
    # left: curves
    X0, X1, Y0, Y1 = 64, 320, 40, 296
    fx = lambda v: X0 + (X1 - X0) * v; fy = lambda v: Y1 - (Y1 - Y0) * v
    o.append(axes(X0, X1, Y0, Y1, [0, 0.5, 1], [0, 0.5, 1], fx, fy, 'input |x|/V', 'output y', lambda v: f'{v:g}', lambda v: f'{v:g}'))
    xs = [i / 400 for i in range(401)]
    o.append(P([(fx(0), fy(0)), (fx(1), fy(1))], MUT, 1.8, '6 4'))
    o.append(P([(fx(x), fy(a_c(x))) for x in xs], LV, 2.5, '8 4'))
    o.append(P([(fx(x), fy(mu_c(x))) for x in xs], AC, 2.8))
    for x in (0.01, 0.1, 0.5):
        o.append(C(fx(x), fy(mu_c(x)), 5, AC))
    o.append(Tb(fx(0.01) + 10, fy(mu_c(0.01)) + 4, '0.01 → 0.229', 13, 'start', AC, True))
    o.append(Tb(fx(0.1) + 10, fy(mu_c(0.1)) + 14, '0.1 → 0.591', 13, 'start', AC, True))
    o.append(Tb(fx(0.5), fy(mu_c(0.5)) - 14, '0.5 → 0.876', 13, 'middle', AC, True))
    o.append(Tb(fx(0.74), fy(0.58), 'no companding', 13, 'middle', MUT))
    o.append(legend(150, 276, [(AC, None, 'μ = 255'), (LV, '8 4', 'A = 87.6')], 13, 12))
    # right: SQNR against input level
    S0, S1 = 420, 700
    lv = [-50 + i * 0.5 for i in range(101)]
    gx = lambda d: S0 + (S1 - S0) * (d + 50) / 50; gy = lambda s: Y1 - (Y1 - Y0) * s / 60
    o.append(axes(S0, S1, Y0, Y1, [-50, -40, -30, -20, -10, 0], [0, 20, 40, 60], gx, gy, 'sine peak re full scale (dB)', 'SQNR (dB)',
                  lambda v: neg(f'{v:g}'), lambda v: f'{v:g}'))
    o.append(P([(gx(d), gy(max(0, sq_unif(10 ** (d / 20))))) for d in lv if sq_unif(10 ** (d / 20)) >= 0], MUT, 2.4, '6 4'))
    o.append(P([(gx(d), gy(sq_mu(10 ** (d / 20)))) for d in lv], AC, 2.8))
    o.append(C(gx(0), gy(sq_unif(1)), 5, MUT)); o.append(C(gx(-40), gy(sq_unif(0.01)), 5, MUT))
    o.append(C(gx(0), gy(sq_mu(1)), 5, AC)); o.append(C(gx(-40), gy(sq_mu(0.01)), 5, AC))
    o.append(Tb(gx(-1), gy(sq_unif(1)) - 12, 'uniform 49.9', 13, 'end', MUT, True))
    o.append(Tb(gx(-1), gy(sq_mu(1)) + 22, 'μ-law 38.0', 13, 'end', AC, True))
    o.append(Tb(gx(-40) + 8, gy(sq_unif(0.01)) + 4, '9.9', 13, 'start', MUT, True))
    o.append(Tb(gx(-40), gy(sq_mu(0.01)) - 14, '34.4', 13, 'middle', AC, True))
    o.append(T((S0 + S1) / 2, 20, '8 bits, ±1 V range', 13, fill=MUT))
    return 350, ''.join(o)


FIG[3] = (f3, 'Left: the μ-law and A-law compressors lift small inputs (the worked example’s points 0.01, 0.1 and 0.5 on the μ-law curve). Right: with 8 bits, uniform SQNR falls 6 dB for every halving of the input, while μ-law stays between 34 and 38 dB from full scale down to −40 dB.',
          'Left plot: mu-law and A-law compression curves against the straight no-companding line, with points 0.01 to 0.229, 0.1 to 0.591 and 0.5 to 0.876. Right plot: SQNR against input level for uniform and mu-law 8-bit quantizers.')


# ---- 4.4: the 3-bit PCM trace ----
def f4():
    o = []
    X0, X1, Y0, Y1 = 60, 600, 36, 300
    fx = lambda t: X0 + (X1 - X0) * t / 1.0        # t in ms
    fy = lambda v: (Y0 + Y1) / 2 - (Y1 - Y0) / 8 * v
    for i in range(8):
        lvl = -3.5 + i
        o.append(L(X0, fy(lvl), X1, fy(lvl), 'var(--line)', 1))
        o.append(T(X1 + 12, fy(lvl) + 4.5, format(i, '03b'), 13, 'start', MUT))
        o.append(T(X0 - 8, fy(lvl) + 4.5, neg(f'{lvl:+.1f}'), 13, 'end', MUT))
    for b in range(-4, 5):
        o.append(L(X0 - 3, fy(b), X0, fy(b), L2, 1.2))
    o.append(L(X0, Y0 - 4, X0, Y1 + 4, L2, 1.5))
    o.append(T(X0 - 8, Y0 - 12, 'volts', 13, 'end', MUT))
    o.append(T(X1 + 12, Y0 - 12, 'code', 13, 'start', MUT, True))
    ts = [i / 400 for i in range(401)]
    o.append(P([(fx(t), fy(3.5 * sin(2 * pi * t))) for t in ts], LV, 2.2))
    for k in range(8):
        t = (k + 0.5) / 8
        x = 3.5 * sin(2 * pi * t); q = math.floor(x) + 0.5
        o.append(L(fx(t), fy(x), fx(t), fy(q), INK, 1.4, '2 2'))
        o.append(L(fx(t) - 20, fy(q), fx(t) + 20, fy(q), AC, 4))
        o.append(C(fx(t), fy(x), 4.5, LV))
        idx = int(q + 3.5)
        o.append(T(fx(t), Y1 + 26, format(idx, '03b'), 14, fill=AC, bold=True))
    o.append(T(X0 - 8, Y1 + 26, 'sent', 13, 'end', MUT))
    for t, lab in ((0, '0'), (0.5, '0.5'), (1, '1 ms')):
        o.append(T(fx(t), Y1 + 48, lab, 13, fill=MUT))
    o.append(legend(150, 18, [(LV, None, 'x(t) = 3.5 sin(2π·1000t)'), (AC, None, 'level sent')]))
    return 360, ''.join(o)


FIG[4] = (f4, 'Three-bit PCM of the second worked example: each sample (dot) is rounded to the nearest of eight levels (bar), and the level’s number is sent as a 3-bit code, 101 111 111 101 010 000 000 010 for one cycle.',
          'A 3.5 volt, 1 kilohertz sine over one millisecond with eight quantization levels from minus 3.5 to plus 3.5 volts labelled 000 to 111; eight samples are rounded to levels and their codes are written below.')


# ---- 4.5: DPCM transmitter and receiver ----
def summer(x, y, signs, r=17):
    o = [f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{PANEL};stroke:{AC};stroke-width:2"/>', T(x, y + 6, 'Σ', 17, bold=True)]
    for dx, dy, s in signs:
        o.append(T(x + dx, y + dy, s, 15, fill=INK, bold=True))
    return ''.join(o)


def f5():
    o = []
    o.append(R(8, 26, 470, 296, FIGBG, L2, 10, 1.2, '6 4')); o.append(T(20, 48, 'transmitter', 14, 'start', MUT, True))
    o.append(R(492, 26, 220, 296, FIGBG, L2, 10, 1.2, '6 4')); o.append(T(504, 48, 'receiver', 14, 'start', MUT, True))
    y = 100
    o.append(T(24, y - 10, 'x[n]', 14, 'start', INK, True)); o.append(L(24, y, 78, y, AC, 2, arrow='n'))
    o.append(summer(96, y, [(-16, -18, '+'), (10, 34, '−')]))
    o.append(L(113, y, 160, y, AC, 2, arrow='n')); o.append(T(136, y - 10, 'e[n]', 14, bold=True))
    o.append(boxt(160, y - 24, 104, 48, ['quantizer'], PANEL, AC, 14))
    o.append(L(264, y, 312, y, AC, 2, arrow='n')); o.append(T(288, y - 10, 'q[n]', 14, bold=True))
    o.append(boxt(312, y - 24, 90, 48, ['encoder'], PANEL, AC, 14))
    o.append(L(402, y, 540, y, AC, 2.5, arrow='n')); o.append(Tb(450, y - 10, 'code, N bits', 13, fill=MUT))
    # local decoder in transmitter
    o.append(C(288, y, 4, AC)); o.append(L(288, y, 288, 170, AC, 2, arrow='n'))
    o.append(summer(288, 188, [(-30, -8, '+'), (12, -20, '+')]))
    o.append(L(288, 205, 288, 250, AC, 2, arrow='n')); o.append(T(298, 232, 'x̃[n]', 14, 'start', INK, True))
    o.append(boxt(206, 250, 164, 48, ['predictor', 'stores x̃'], PANEL, NX, 13, True))
    o.append(P([(206, 274), (96, 274), (96, 120)], NX, 2)); o.append(L(96, 130, 96, 121, NX, 2, arrow='x'))
    o.append(T(104, 254, 'x̂[n]', 14, 'start', NX, True))
    o.append(P([(96, 188), (266, 188)], NX, 2)); o.append(L(258, 188, 270, 188, NX, 2, arrow='x'))
    o.append(T(150, 180, 'x̂[n]', 14, 'middle', NX, True))
    o.append(T(380, 192, 'local decoder:', 13, 'start', MUT)); o.append(T(380, 210, 'same sum as', 13, 'start', MUT)); o.append(T(380, 228, 'the receiver', 13, 'start', MUT))
    # receiver
    o.append(boxt(540, y - 24, 90, 48, ['decoder'], PANEL, AC, 14))
    o.append(L(585, y + 24, 585, 170, AC, 2, arrow='n')); o.append(T(553, 146, 'q[n]', 14, 'start', INK, True))
    o.append(summer(585, 188, [(-30, -8, '+'), (12, -20, '+')]))
    o.append(L(602, 188, 690, 188, AC, 2.5, arrow='n')); o.append(T(646, 178, 'x̃[n]', 14, bold=True))
    o.append(T(668, 210, 'to filter', 13, fill=MUT))
    o.append(C(616, 188, 4, AC)); o.append(L(616, 188, 616, 250, AC, 2, arrow='n'))
    o.append(boxt(530, 250, 120, 48, ['predictor', 'same rule'], PANEL, NX, 13, True))
    o.append(P([(530, 274), (512, 274), (512, 188), (560, 188)], NX, 2)); o.append(L(556, 188, 566, 188, NX, 2, arrow='x'))
    o.append(T(520, 232, 'x̂', 14, 'start', NX, True))
    return 336, ''.join(o)


FIG[5] = (f5, 'DPCM in full: the transmitter holds its own copy of the receiver (the lower Σ and predictor), so both ends predict x̂[n] from the same reconstructed samples x̃ and only the N-bit code of q[n] crosses the channel.',
          'Block diagram. Transmitter: x of n minus the prediction gives e of n, quantizer gives q of n, encoder sends the code; q of n plus the prediction gives the reconstructed sample, which feeds the predictor. Receiver: decoder gives q of n, which is added to the same prediction to give the reconstructed sample.')


# ---- 4.6: DM staircase on sin(2π·500t), fs = 8 kHz, Δ = 0.3 V ----
def dm_trace(N=17, fs=8000, D=0.3):
    out, xt = [], 0.0
    for n in range(N):
        x = sin(2 * pi * 500 * n / fs); b = 1 if x >= xt - 1e-12 else 0; xt += D if b else -D
        out.append((n, x, b, xt))
    return out


def f6():
    o = []
    tr = dm_trace()
    X0, X1, Y0, Y1 = 70, 690, 40, 280
    fx = lambda n: X0 + (X1 - X0) * n / 16.0
    fy = lambda v: (Y0 + Y1) / 2 - (Y1 - Y0) / 2 * v / 1.3
    o.append(f'<rect x="{fx(2.6):.1f}" y="{Y0:.1f}" width="{fx(6.4) - fx(2.6):.1f}" height="{fy(0.62) - Y0:.1f}" style="fill:{NXS}"/>')
    o.append(f'<rect x="{fx(8.6):.1f}" y="{fy(0.25):.1f}" width="{fx(11.4) - fx(8.6):.1f}" height="{fy(-1.05) - fy(0.25):.1f}" style="fill:{LVS}"/>')
    o.append(T(fx(4.5), Y0 - 8, 'granular: hunting ±Δ', 13, fill=NX, bold=True))
    o.append(T(fx(10), fy(-1.05) + 18, 'slope overload', 13, fill=LV, bold=True))
    o.append(L(X0, fy(0), X1, fy(0), L2, 1.5)); o.append(L(X0, Y0 - 4, X0, Y1 + 4, L2, 1.5))
    for v in (-1, 0, 1):
        o.append(T(X0 - 9, fy(v) + 4.5, neg(v), 13, 'end', MUT))
    o.append(T(X0, Y0 - 14, 'volts', 13, 'start', MUT))
    ns = [i / 50 for i in range(16 * 50 + 1)]
    o.append(P([(fx(n), fy(sin(2 * pi * 500 * n / 8000))) for n in ns], LV, 2.2))
    pts, prev = [], 0.0
    for n, x, b, xt in tr:
        pts += [(fx(n), fy(prev)), (fx(n), fy(xt))]
        if n < 16: pts.append((fx(n + 1), fy(xt)))
        prev = xt
    o.append(P(pts, AC, 2.6))
    for n, x, b, xt in tr:
        o.append(C(fx(n), fy(x), 4, LV))
        o.append(T(fx(n), Y1 + 26, str(b), 14, fill=AC, bold=True))
        if n % 4 == 0: o.append(T(fx(n), Y1 + 46, f'n = {n}', 13, fill=MUT))
    o.append(T(X0 - 9, Y1 + 26, 'bits', 13, 'end', MUT))
    o.append(legend(330, 22, [(LV, None, 'x(t), 500 Hz, 1 V'), (AC, None, 'staircase, Δ = 0.3 V')]))
    return 340, ''.join(o)


FIG[6] = (f6, 'Delta modulation of the second worked example (8000 samples/s, Δ = 0.3 V): at the peak the bits alternate and the staircase hunts by ±Δ, while near the falling zero crossing the input drops 0.38 V per sample and the staircase, limited to 0.3 V, falls behind.',
          'A 1 volt, 500 hertz sine with sample dots and the delta-modulation staircase of step 0.3 volts over 16 samples, the bit sent at each sample written below; a shaded region at the peak marks granular noise and one near the falling zero crossing marks slope overload.')


# ---- 4.7: commutator and the 4-channel frame ----
def f7():
    o = []
    cx, cy, r = 150, 128, 62
    for i in range(4):
        a = -3 * pi / 4 + i * pi / 2
        px, py = cx + r * cos(a), cy + r * sin(a)
        o.append(C(px, py, 6, AC))
        lx, ly = cx + (r + 30) * cos(a), cy + (r + 26) * sin(a)
        o.append(Tb(lx, ly + 5, f'CH{i + 1}', 14, 'middle', INK, True))
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" style="fill:none;stroke:{L2};stroke-width:1.5;stroke-dasharray:4 4"/>')
    o.append(L(cx, cy, cx + r * cos(-3 * pi / 4) * 0.9, cy + r * sin(-3 * pi / 4) * 0.9, NX, 3, arrow='x'))
    o.append(C(cx, cy, 6, NX))
    a1, a2 = -110 * pi / 180, -70 * pi / 180
    o.append(arc(cx + 84 * cos(a1), cy + 84 * sin(a1), cx + 84 * cos(a2), cy + 84 * sin(a2), 0.3, MUT, 1.6, 'm'))
    o.append(T(cx, cy - r - 44, 'turns clockwise', 13, fill=MUT))
    o.append(T(cx, cy + r + 58, 'one turn per 125 µs', 13, fill=MUT))
    o.append(L(cx, cy, 300, cy, AC, 2, arrow='n')); o.append(T(262, cy - 10, 'to line', 13, fill=MUT))
    # frame timeline
    X0, X1, y0, h = 316, 700, 92, 56
    fx = lambda t: X0 + (X1 - X0) * t / 125.0
    slots = [('CH1', 0, 30.3, ACS), ('CH2', 30.3, 60.6, PANEL), ('CH3', 60.6, 90.9, ACS), ('CH4', 90.9, 121.2, PANEL)]
    for lab, a, b, fill in slots:
        o.append(R(fx(a), y0, fx(b) - fx(a), h, fill, AC, 2))
        o.append(T((fx(a) + fx(b)) / 2, y0 + 25, lab, 14, bold=True))
        o.append(T((fx(a) + fx(b)) / 2, y0 + 44, '8 bits', 13, fill=MUT))
    o.append(R(fx(121.2), y0, fx(125) - fx(121.2), h, LVS, LV, 2, 2))
    o.append(T(fx(123.1), y0 - 10, 'S', 14, fill=LV, bold=True))
    o.append(brace(fx(0), fx(30.3), y0 + h + 12, INK))
    o.append(T(fx(15.15), y0 + h + 36, 'slot 30.3 µs', 13))
    o.append(brace(fx(0), fx(125), y0 + h + 52, INK))
    o.append(T(fx(62.5), y0 + h + 76, 'frame 125 µs = 33 bits → 264 kbit/s', 13, bold=True))
    o.append(T(fx(62.5), y0 + h + 96, 'one bit 3.79 µs; S = 1 sync bit', 13, fill=MUT))
    o.append(T(fx(62.5), y0 - 30, 'the frame repeats 8000 times a second', 13, fill=MUT))
    return 290, ''.join(o)


FIG[7] = (f7, 'Left: a commutator takes one sample from each of the four channels per turn. Right: the first worked example’s frame, four 8-bit slots and one sync bit S in 125 µs, which gives 33 bits per frame and 264 kbit/s.',
          'A four-position commutator feeding a line, and a 125 microsecond frame with slots CH1 to CH4 of 30.3 microseconds each and a 3.79 microsecond sync bit.')


# ---- 4.8: waveforms of 10110 and the four spectra ----
def sincf(x): return 1.0 if abs(x) < 1e-12 else sin(pi * x) / (pi * x)
PSD = [('polar NRZ', AC, None, lambda f: sincf(f) ** 2),
       ('polar RZ', MUT, '3 3', lambda f: 0.25 * sincf(f / 2) ** 2),
       ('AMI', LV, '8 4', lambda f: 0.25 * sincf(f / 2) ** 2 * sin(pi * f) ** 2),
       ('Manchester', NX, None, lambda f: sincf(f / 2) ** 2 * sin(pi * f / 2) ** 2)]


def levels(bits, code):
    """two half-bit levels per bit, values in {-1, 0, 1}"""
    out, last = [], -1
    for b in bits:
        if code == 'nrz': out += [1 if b else -1] * 2
        elif code == 'rz': out += [1 if b else -1, 0]
        elif code == 'ami':
            if b: last = -last; out += [last, 0]
            else: out += [0, 0]
        elif code == 'man': out += [-1, 1] if b else [1, -1]
        elif code == 'unrz': out += [1 if b else 0] * 2
        elif code == 'dman':
            # differential Manchester: transition at the start for 0, none for 1; always one at the centre
            if not out: cur = 1
            else: cur = out[-1]
            first = -cur if b == 0 else cur
            out += [first, -first]
    return out


def wave(x0, x1, yc, a, lv, c, w=2.4):
    n = len(lv); dx = (x1 - x0) / n; pts = []
    for i, v in enumerate(lv):
        pts += [(x0 + i * dx, yc - a * v), (x0 + (i + 1) * dx, yc - a * v)]
    return P(pts, c, w)


def f8():
    o = []
    bits = [1, 0, 1, 1, 0]
    X0, X1 = 130, 700
    bw = (X1 - X0) / 5
    for i, b in enumerate(bits):
        o.append(T(X0 + (i + 0.5) * bw, 26, str(b), 16, bold=True))
    for i in range(6):
        o.append(L(X0 + i * bw, 34, X0 + i * bw, 330, L2, 1, '3 4'))
    rows = [('polar NRZ', 'nrz', AC), ('polar RZ', 'rz', MUT), ('AMI', 'ami', LV), ('Manchester', 'man', NX)]
    for j, (name, code, c) in enumerate(rows):
        yc = 70 + j * 74
        o.append(L(X0, yc, X1, yc, 'var(--line)', 1))
        o.append(T(16, yc + 5, name, 14, 'start', INK, True))
        o.append(T(X0 - 8, yc - 18, '+V', 13, 'end', MUT)); o.append(T(X0 - 8, yc + 27, '−V', 13, 'end', MUT))
        o.append(wave(X0, X1, yc, 24, levels(bits, code), c))
    o.append(T(X0 + 2.5 * bw, 350, 'one bit = Tb; dashed lines mark the bit boundaries', 13, fill=MUT))
    # spectra
    S0, S1, B0, B1 = 80, 700, 400, 600
    gx = lambda f: S0 + (S1 - S0) * f / 3.0
    gy = lambda v: B1 - (B1 - B0) * v
    o.append(axes(S0, S1, B0, B1, [0, 0.5, 1, 1.5, 2, 2.5, 3], [0, 0.5, 1], gx, gy, 'frequency f, in multiples of Rb', 'S(f)/(V²Tb)',
                  lambda v: f'{v:g}', lambda v: f'{v:g}'))
    fs_ = [i / 200 for i in range(601)]
    for name, c, dash, g in PSD:
        o.append(P([(gx(f), gy(g(f))) for f in fs_], c, 2.6 if dash is None else 2.2, dash))
    o.append(Tb(gx(0.3), gy(0.93), 'polar NRZ', 13, 'start', AC, True))
    o.append(Tb(gx(0.74), gy(0.525) - 10, 'Manchester', 13, 'middle', NX, True))
    o.append(Tb(gx(0.12), gy(0.34), 'polar RZ', 13, 'start', MUT, True))
    o.append(Tb(gx(0.5), gy(0.17) + 30, 'AMI', 13, 'middle', LV, True))
    o.append(L(gx(1), gy(0.33), gx(1), B1, INK, 1.2, '2 3')); o.append(Tb(gx(1) - 4, gy(0.30), 'null at Rb', 13, 'end', INK))
    o.append(L(gx(2), gy(0.2), gx(2), B1, INK, 1.2, '2 3')); o.append(Tb(gx(2), gy(0.2) - 6, 'null at 2Rb', 13, 'middle', INK))
    return 660, ''.join(o)


FIG[8] = (f8, 'Top: the bits 1 0 1 1 0 of the worked example in four line codes (Manchester with 1 = low-to-high). Bottom: their power spectral densities for random bits; polar NRZ and AMI reach their first null at Rb, polar RZ and Manchester at 2Rb, and only AMI and Manchester have no power at DC.',
          'Waveforms of bits 1 0 1 1 0 in polar NRZ, polar RZ, AMI and Manchester, and a plot of the four power spectral densities from 0 to 3 times the bit rate.')


spec = make_spec(FIG)


# ---- model-answer sketch: 1 0 1 1 0 0 1 in NRZ-L, polar RZ, Manchester and differential Manchester ----
def answer_waves():
    o = []
    bits = [1, 0, 1, 1, 0, 0, 1]
    X0, X1 = 200, 700
    bw = (X1 - X0) / 7
    for i, b in enumerate(bits):
        o.append(T(X0 + (i + 0.5) * bw, 24, str(b), 15, bold=True))
    for i in range(8):
        o.append(L(X0 + i * bw, 32, X0 + i * bw, 316, L2, 1, '3 4'))
    rows = [('NRZ-L', 'nrz', AC), ('polar RZ', 'rz', MUT), ('Manchester', 'man', NX), ('diff. Manchester', 'dman', LV)]
    for j, (name, code, c) in enumerate(rows):
        yc = 66 + j * 72
        o.append(L(X0, yc, X1, yc, 'var(--line)', 1))
        o.append(T(14, yc + 5, name, 14, 'start', INK, True))
        o.append(wave(X0, X1, yc, 22, levels(bits, code), c))
    o.append(T((X0 + X1) / 2, 340, 'Manchester: 1 = low-to-high; differential: a 0 has a transition at the start of the bit', 13, fill=MUT))
    return {'h': 352, 'body': o and ''.join(o), 'aria': 'Waveforms of the bits 1 0 1 1 0 0 1 in NRZ-L, polar RZ, Manchester and differential Manchester.'}


# ---- model-answer sketch: μ-law and A-law compressor curves with the identity line ----
def answer_curves():
    o = []
    X0, X1, Y0, Y1 = 70, 430, 36, 276
    fx = lambda v: X0 + (X1 - X0) * v; fy = lambda v: Y1 - (Y1 - Y0) * v
    o.append(axes(X0, X1, Y0, Y1, [0, 0.25, 0.5, 0.75, 1], [0, 0.5, 1], fx, fy, 'input |x|/V', 'output y', lambda v: f'{v:g}', lambda v: f'{v:g}'))
    xs = [i / 400 for i in range(401)]
    o.append(P([(fx(0), fy(0)), (fx(1), fy(1))], MUT, 1.8, '6 4'))
    o.append(P([(fx(x), fy(a_c(x))) for x in xs], LV, 2.5, '8 4'))
    o.append(P([(fx(x), fy(mu_c(x))) for x in xs], AC, 2.8))
    o.append(Tb(fx(0.78), fy(0.62), 'uniform (no companding)', 13, 'middle', MUT))
    o.append(T(470, 90, 'μ-law, μ = 255:', 14, 'start', AC, True))
    o.append(T(470, 110, 'y = ln(1 + μ|x|/V)/ln(1 + μ)', 13, 'start', INK))
    o.append(T(470, 130, 'slope at 0: 46.0 (33.3 dB)', 13, 'start', MUT))
    o.append(T(470, 172, 'A-law, A = 87.6:', 14, 'start', LV, True))
    o.append(T(470, 192, 'linear up to |x|/V = 1/A,', 13, 'start', INK))
    o.append(T(470, 212, 'logarithmic above', 13, 'start', INK))
    o.append(T(470, 232, 'slope at 0: 16.0 (24.1 dB)', 13, 'start', MUT))
    return {'h': 330, 'body': ''.join(o), 'aria': 'Mu-law and A-law compression curves rising steeply from zero and bending over, compared with the straight uniform line.'}
