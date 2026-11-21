"""Claude's hand-drawn figures for ec-comm-u5 (Baseband data transmission and detection), one per chapter.
Every number comes from that chapter's worked example and is computed here. Colours are the shell's CSS variables."""
import os, sys, math, itertools
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

sub = lambda s: f'<tspan font-size="11" dy="4">{s}</tspan><tspan dy="-4">​</tspan>'


def sinc(x):
    return 1.0 if abs(x) < 1e-12 else math.sin(math.pi * x) / (math.pi * x)


def rc(t, a):
    den = 1 - (2 * a * t) ** 2
    if abs(den) < 1e-9:
        return (math.pi / 4) * sinc(1 / (2 * a))
    return sinc(t) * math.cos(math.pi * a * t) / den


def path(pts):
    return 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts)


def stem(x, y0, y1, c=AC, r=5):
    return L(x, y0, x, y1, c, 2.5) + C(x, y1, r, c)


FIG = {}


# ---- 5.1 three pulses and the sample they build (worked example 1) ----
def f1():
    x0, x1, yt, yb = 70, 690, 40, 330
    fx = lambda t: x0 + (t + 3.5) / 7 * (x1 - x0)
    fy = lambda v: yt + (1.4 - v) / 2.8 * (yb - yt)
    o = [axes(x0, x1, yt, yb, [-3, -2, -1, 0, 1, 2, 3], [-1, -0.5, 0, 0.5, 1], fx, fy, 'time t/T (sampling instants are the integers)', 'value at the sampler',
              xfmt=lambda v: neg(v), yfmt=lambda v: neg(v))]
    o.append(L(fx(-3.5), fy(0), fx(3.5), fy(0), L2, 1.5, '6 5'))
    p = lambda t: sinc(t) + 0.25 * sinc(t - 1) + 0.25 * sinc(t + 1)
    ts = [-3.5 + i * 0.05 for i in range(141)]
    syms = [(-1, 1, NX), (0, -1, LV), (1, 1, NX)]
    for c0, a, col in syms:
        o.append(P([(fx(t), fy(a * p(t - c0))) for t in ts], col, 2, '5 4'))
    o.append(P([(fx(t), fy(sum(a * p(t - c0) for c0, a, _ in syms))) for t in ts], AC, 3))
    # contributions at t = 0
    o.append(C(fx(0), fy(0.25), 5, NX)); o.append(C(fx(0), fy(-1), 5, LV)); o.append(C(fx(0), fy(-0.5), 7, AC))
    o.append(Tb(fx(0) + 14, fy(0.25) - 14, 'each neighbour adds +0.25', 13, 'start', NX))
    o.append(Tb(fx(0) + 14, fy(-1) + 22, 'own pulse a' + sub('k') + 'p(0) = −1', 13, 'start', LV))
    o.append(Tb(fx(0) + 14, fy(-0.5) + 4, 'sample y(kT) = −1 + 0.5 = −0.5', 14, 'start', AC, True))
    o.append(T(fx(-1), fy(1.08) - 6, 'a' + sub('k−1') + ' = +1', 13, fill=NX))
    o.append(T(fx(1), fy(1.08) - 6, 'a' + sub('k+1') + ' = +1', 13, fill=NX))
    o.append(T(fx(-2.05), fy(0) + 20, 'threshold 0', 13, 'start', MUT))
    return 390, ''.join(o)

FIG[1] = (f1, 'The worked example\'s three symbols, +1, −1, +1, each with p(0) = 1 and p(±T) = 0.25 (dashed), and their sum (solid). At t = kT the two neighbours add +0.25 each, so the sample is −0.5 instead of −1: half the margin to the threshold is gone.',
          'Plot of three pulses centred at minus one, zero and plus one symbol periods, with heights plus one, minus one and plus one, and their sum. At time zero the sum is minus 0.5, made of minus 1 from the own pulse and plus 0.25 from each neighbour.', 2)


# ---- 5.2 raised cosine spectra for the 4800 baud example, and the alpha = 0.5 eye ----
def f2():
    o = []
    # left: spectra
    x0, x1, yt, yb = 64, 340, 48, 280
    fx = lambda f: x0 + f / 5000 * (x1 - x0)
    fy = lambda v: yt + (1.15 - v) / 1.15 * (yb - yt)
    o.append(T(x0 - 40, 24, 'Spectrum, R' + sub('s') + ' = 4800 baud', 14, 'start', bold=True))
    o.append(xaxis(x0, x1, yb, [0, 2400, 3600, 4800], fx, 'frequency (Hz)'))
    o.append(L(x0, yt, x0, yb, L2, 1.5))
    W = 2400
    def P_rc(f, a):
        if a == 0: return 1.0 if f <= W else 0.0
        f1, f2 = (1 - a) * W, (1 + a) * W
        if f <= f1: return 1.0
        if f >= f2: return 0.0
        return 0.5 * (1 + math.cos(math.pi * (f - f1) / (f2 - f1)))
    fs = [i * 12.5 for i in range(401)]
    for a, col, lab, ly in ((0, L2, 'α = 0', 0.88), (0.5, AC, 'α = 0.5', 0.55), (1.0, NX, 'α = 1', 0.22)):
        pts = [(fx(f), fy(P_rc(f, a))) for f in fs]
        if a == 0: pts = [(fx(0), fy(1)), (fx(W), fy(1)), (fx(W), fy(0)), (fx(5000), fy(0))]
        o.append(P(pts, col, 3 if a == 0.5 else 2, '6 4' if a == 0 else None))
    o.append(T(fx(2400) + 6, fy(1) - 6, 'α = 0: 2400 Hz', 13, 'start', MUT))
    o.append(Tb(fx(3000) + 4, fy(0.5) - 4, 'α = 0.5: 3600 Hz', 13, 'start', AC))
    o.append(Tb(fx(3900), fy(0.18) + 4, 'α = 1: 4800 Hz', 13, 'start', NX))
    # right: eye diagram, binary, alpha = 0.5, every pattern of 6 neighbours
    ex0, ex1, eyt, eyb = 410, 690, 48, 280
    gx = lambda t: ex0 + (t + 1) / 2 * (ex1 - ex0)
    gy = lambda v: eyt + (1.6 - v) / 3.2 * (eyb - eyt)
    o.append(T(ex0 - 20, 24, 'Eye pattern, α = 0.5', 14, 'start', bold=True))
    o.append(R(ex0, eyt, ex1 - ex0, eyb - eyt, FIGBG, L2, 4, 1.5))
    ts = [-1 + i * 0.05 for i in range(41)]
    d = []
    for pat in itertools.product([-1, 1], repeat=6):
        for a0 in (-1, 1):
            seq = dict(zip([-3, -2, -1, 1, 2, 3], pat)); seq[0] = a0
            d.append(path([(gx(t), gy(sum(a * rc(t - n, 0.5) for n, a in seq.items()))) for t in ts]))
    o.append(f'<path d="{" ".join(d)}" style="fill:none;stroke:var(--accent);stroke-width:1;stroke-opacity:0.35"/>')
    o.append(L(gx(0), eyt, gx(0), eyb, LV, 2, '5 4'))
    o.append(T(gx(0), eyb + 20, 'sampling instant', 13, fill=LV))
    o.append(T(gx(-1), eyb + 20, '−T', 13, fill=MUT)); o.append(T(gx(1), eyb + 20, '+T', 13, fill=MUT))
    o.append(L(gx(0) + 12, gy(1) + 4, gx(0) + 12, gy(-1) - 4, INK, 2, None, 'm'))
    o.append(L(gx(0) + 12, gy(-1) - 4, gx(0) + 12, gy(1) + 4, INK, 2, None, 'm'))
    o.append(Tb(gx(0) + 20, gy(0) + 5, 'opening 2 (noise margin)', 13, 'start'))
    wc = 0.785
    o.append(C(gx(0.1), gy(wc), 4, NX)); o.append(C(gx(-0.1), gy(wc), 4, NX))
    o.append(Tb(gx(-0.1) - 8, gy(wc) + 4, '0.785 at ±0.1T', 13, 'end', NX))
    o.append(T((ex0 + ex1) / 2, eyb + 42, 'time from the sampling instant', 14, fill=MUT))
    return 330, ''.join(o)

FIG[2] = (f2, 'Left: the raised cosine spectra of the 4800 baud example. α = 0.5 needs 3600 Hz, between the 2400 Hz brick wall and the 4800 Hz of α = 1. Right: the α = 0.5 eye for binary data. At the centre every trace passes through ±1; 0.1T away the worst +1 trace has fallen to 0.785.',
          'Left, three spectra: a rectangle to 2400 hertz, a cosine roll-off ending at 3600 hertz and one ending at 4800 hertz. Right, an eye diagram of all data patterns: wide open at the sampling instant with opening 2, and worst sample 0.785 at a tenth of a symbol period away.', 3)


# ---- 5.3 the three-tap ZF equalizer and the sampled response before and after ----
def f3():
    o = []
    y0 = 40
    o.append(T(18, 50, 'x(n)', 14, 'start', bold=True))
    xs = [110, 320, 530]
    o.append(L(52, 46, xs[0] - 4, 46, AC, 2, None, 'n'))
    for i in range(2):
        o.append(boxt(xs[i] + 70, 26, 64, 40, ['T'], PANEL, AC, 15, True))
        o.append(L(xs[i], 46, xs[i] + 66, 46, AC, 2, None, 'n'))
        o.append(L(xs[i] + 134, 46, xs[i + 1] - 2, 46, AC, 2))
    taps = [('c' + sub('−1') + ' = −0.227', xs[0]), ('c' + sub('0') + ' = 1.136', xs[1]), ('c' + sub('1') + ' = −0.341', xs[2])]
    for lab, x in taps:
        o.append(C(x, 46, 4, AC))
        o.append(L(x, 50, x, 88, AC, 2, None, 'n'))
        o.append(f'<circle cx="{x}" cy="104" r="14" style="fill:var(--panel);stroke:var(--accent);stroke-width:2"/>' + T(x, 109, '×', 16, bold=True))
        o.append(T(x + 22, 92, lab, 13, 'start'))
        o.append(L(x, 118, x, 148, AC, 2, None, 'n'))
    o.append(L(xs[0], 152, xs[2], 152, AC, 2))
    o.append(boxt(xs[1] - 24, 160, 48, 34, ['Σ'], ACS, AC, 16, True))
    o.append(L(xs[1], 152, xs[1], 158, AC, 2))
    o.append(L(xs[1] + 24, 177, 450, 177, AC, 2, None, 'n'))
    o.append(boxt(454, 160, 90, 34, ['slicer'], PANEL, AC, 14))
    o.append(L(544, 177, 600, 177, AC, 2, None, 'n'))
    o.append(T(606, 182, 'â(n)', 14, 'start', bold=True))
    o.append(T(392, 170, 'y(n)', 13, fill=MUT))
    # stems
    def stems(xa, title, vals, col, note):
        out = [T(xa, 232, title, 14, 'start', bold=True)]
        base, sc = 330, 70
        out.append(L(xa, base, xa + 290, base, L2, 1.5))
        for j, (m, v) in enumerate(vals):
            x = xa + 25 + j * 60
            out.append(stem(x, base, base - v * sc, col) if abs(v) > 1e-9 else C(x, base, 4, L2))
            out.append(T(x, base + 22, neg(m), 13, fill=MUT))
            if v > 0.5: out.append(T(x, base - v * sc - 10, f'{v:g}', 13))
            elif v > 0: out.append(T(x + 14, base - v * sc - 6, f'{v:g}', 13, 'start'))
            elif v < 0: out.append(T(x - 10, base - 12, f'{v:g}'.replace('-', '−'), 13, 'end'))
        out.append(T(xa + 145, base + 44, note, 14, fill=col, bold=True))
        return ''.join(out)
    o.append(stems(30, 'Channel h' + sub('m'), [(-2, 0), (-1, 0.2), (0, 1), (1, 0.3), (2, 0)], NX, 'peak distortion 0.5'))
    o.append(stems(390, 'After the equalizer v' + sub('m'), [(-2, -0.045), (-1, 0), (0, 1), (1, 0), (2, -0.102)], AC, 'peak distortion 0.148'))
    o.append(T(360, 400, 'm (in symbol periods)', 13, fill=MUT))
    return 412, ''.join(o)

FIG[3] = (f3, 'The worked example\'s three-tap equalizer. It forces v<sub>±1</sub> = 0 exactly, but leaves small new ISI at m = ±2 (−0.045 and −0.102), so the peak distortion falls from 0.5 to 0.148 rather than to zero.',
          'A delay line with two T delays and three taps, weights minus 0.227, 1.136 and minus 0.341, summed and fed to a slicer. Below, stems of the channel response 0.2, 1, 0.3 and of the equalized response minus 0.045, 0, 1, 0, minus 0.102.', 3)


# ---- 5.4 three waveforms and their points ----
def f4():
    o = []
    waves = [('s' + sub('1'), [1, 1]), ('s' + sub('2'), [2, 0]), ('s' + sub('3'), [0, 2])]
    for i, (name, lev) in enumerate(waves):
        yb = 92 + i * 108; x0 = 70; w = 220; sc = 28
        o.append(L(x0, yb, x0 + w + 10, yb, L2, 1.5)); o.append(L(x0, yb + 6, x0, yb - 66, L2, 1.5))
        pts = [(x0, yb), (x0, yb - lev[0] * sc), (x0 + w / 2, yb - lev[0] * sc), (x0 + w / 2, yb - lev[1] * sc), (x0 + w, yb - lev[1] * sc), (x0 + w, yb)]
        o.append(P(pts, AC, 3))
        o.append(T(30, yb - 24, name, 15, bold=True))
        for j, v in enumerate(lev):
            o.append(T(x0 + w / 4 + j * w / 2, yb - v * sc - 8 if v else yb - 8, f'{v} V', 13, fill=MUT))
        o.append(T(x0, yb + 18, '0', 13, fill=MUT)); o.append(T(x0 + w / 2, yb + 18, '0.5', 13, fill=MUT)); o.append(T(x0 + w, yb + 18, '1 ms', 13, fill=MUT))
    # plane
    cx, cy, u = 470, 196, 110
    fx = lambda a: cx + a * u; fy = lambda b: cy - b * u
    o.append(L(cx - 40, cy, cx + 1.75 * u, cy, L2, 1.5, None, 'm')); o.append(L(cx, cy + 1.45 * u, cx, cy - 1.5 * u, L2, 1.5, None, 'm'))
    o.append(T(cx + 1.75 * u, cy + 22, 'φ' + sub('1'), 15, 'end', bold=True)); o.append(T(cx - 12, cy - 1.45 * u + 6, 'φ' + sub('2'), 15, 'end', bold=True))
    pts = {1: (1, 0), 2: (1, 1), 3: (1, -1)}
    o.append(L(fx(1), fy(1), fx(1), fy(-1), NX, 2, '5 4'))
    o.append(L(cx, cy, fx(1), fy(1), L2, 1.2, '3 4')); o.append(L(cx, cy, fx(1), fy(-1), L2, 1.2, '3 4'))
    for k, (a, b) in pts.items():
        o.append(C(fx(a), fy(b), 7, AC))
    o.append(T(fx(1) + 14, fy(1) + 5, 's' + sub('2') + ' = (1, 1)', 14, 'start'))
    o.append(T(fx(1) + 14, fy(0) - 8, 's' + sub('1') + ' = (1, 0)', 14, 'start'))
    o.append(T(fx(1) + 14, fy(-1) + 5, 's' + sub('3') + ' = (1, −1)', 14, 'start'))
    o.append(Tb(fx(1) - 10, fy(0.5) + 5, 'd = 1', 13, 'end', NX)); o.append(Tb(fx(1) - 10, fy(-0.5) + 5, 'd = 1', 13, 'end', NX))
    o.append(T(fx(1) + 14, fy(-0.45) + 5, 'd' + sub('23') + ' = 2', 13, 'start', NX))
    o.append(T(cx - 8, cy + 20, '0', 13, 'end', MUT)); o.append(T(fx(1), cy + 1.45 * u + 4, 'units: V·√ms', 13, fill=MUT))
    return 378, ''.join(o)

FIG[4] = (f4, 'Left: the three waveforms of the worked example. Right: their points on the two Gram-Schmidt axes. s<sub>3</sub> = 2s<sub>1</sub> − s<sub>2</sub> adds no third axis, and the distances 1, 1 and 2 V·√ms can be read straight off the plane.',
          'Three waveforms: s1 is 1 volt for 1 millisecond, s2 is 2 volts for the first half, s3 is 2 volts for the second half. On the right, a plane with axes phi 1 and phi 2 and points s1 at (1, 0), s2 at (1, 1) and s3 at (1, minus 1); neighbouring distances 1 and the distance from s2 to s3 is 2.', 2)


# ---- 5.5 the two receivers and the matched-filter output for the 1 V, 1 ms pulse ----
def f5():
    o = []
    # top: two receivers
    o.append(T(18, 50, 'r(t)', 14, 'start', bold=True))
    o.append(L(56, 46, 90, 46, AC, 2)); o.append(L(90, 26, 90, 92, AC, 2))
    o.append(L(90, 26, 126, 26, AC, 2, None, 'n')); o.append(boxt(130, 8, 170, 36, ['h(t) = s(T − t)'], PANEL, AC, 14))
    o.append(L(300, 26, 360, 26, AC, 2, None, 'n')); o.append(T(366, 31, 'sample at t = T → y(T)', 14, 'start'))
    o.append(L(90, 92, 126, 92, AC, 2, None, 'n'))
    o.append(f'<circle cx="144" cy="92" r="14" style="fill:var(--panel);stroke:var(--accent);stroke-width:2"/>' + T(144, 97, '×', 16, bold=True))
    o.append(T(144, 132, 's(t)', 13, fill=MUT)); o.append(L(144, 120, 144, 108, AC, 2, None, 'n'))
    o.append(L(158, 92, 196, 92, AC, 2, None, 'n')); o.append(boxt(200, 74, 100, 36, ['∫ from 0 to T'], PANEL, AC, 14))
    o.append(L(300, 92, 360, 92, AC, 2, None, 'n')); o.append(T(366, 97, 'sample at t = T → z(T) = y(T)', 14, 'start'))
    # bottom: output plot
    x0, x1, yt, yb = 80, 660, 176, 372
    fx = lambda t: x0 + t / 2 * (x1 - x0)
    fy = lambda v: yt + (1.15 - v) / 1.15 * (yb - yt)
    o.append(axes(x0, x1, yt, yb, [0, 0.5, 1, 1.5, 2], [0, 0.5, 1], fx, fy, 'time (ms)', 'matched-filter output (× 10⁻³ V²·s)'))
    o.append(P([(fx(0), fy(0)), (fx(1), fy(1)), (fx(2), fy(0))], AC, 3))
    o.append(C(fx(1), fy(1), 6, AC)); o.append(T(fx(1) + 12, fy(1) + 4, 'peak E = 1 × 10⁻³ at t = T: SNR 1000 (30 dB)', 13, 'start', AC, True))
    o.append(L(fx(0.8), fy(0), fx(0.8), fy(0.8), NX, 1.5, '4 4')); o.append(C(fx(0.8), fy(0.8), 5, NX))
    o.append(Tb(fx(0.8) - 10, fy(0.8) + 4, '0.8E at 0.8T: −1.94 dB', 13, 'end', NX))
    return 418, ''.join(o)

FIG[5] = (f5, 'Top: the matched filter and the correlator give the same number at t = T. Bottom: the matched-filter output for the worked example\'s 1 V, 1 ms rectangle is a triangle that peaks at E = 1 × 10⁻³ V²·s at t = T; sampling at 0.8T reads only 0.8E, a 1.94 dB loss.',
          'Two receiver chains, a filter h of t equal to s of T minus t and a multiplier with integrator, both sampled at T. Below, a triangle rising from zero at 0 ms to a peak of 1 at 1 ms and back to zero at 2 ms, with a lower sample of 0.8 marked at 0.8 ms.', 1)


# ---- 5.6 decision regions of the three-point set and the received point ----
def f6():
    o = []
    cx, cy, u = 250, 200, 118
    fx = lambda a: cx + a * u; fy = lambda b: cy - b * u
    # regions
    o.append(R(fx(-0.15), fy(1.45), 1.95 * u, 0.95 * u, ACS, ACS, 0, 0))
    o.append(R(fx(-0.15), fy(-0.5), 1.95 * u, 0.95 * u, NXS, NXS, 0, 0))
    o.append(L(fx(-0.15), fy(0.5), fx(1.8), fy(0.5), INK, 2, '7 5')); o.append(L(fx(-0.15), fy(-0.5), fx(1.8), fy(-0.5), INK, 2, '7 5'))
    o.append(L(cx, cy + 1.5 * u, cx, cy - 1.5 * u, L2, 1.5, None, 'm')); o.append(L(cx - 0.15 * u, cy, fx(1.85), cy, L2, 1.5, None, 'm'))
    o.append(T(fx(1.85), cy + 22, 'φ' + sub('1'), 15, 'end', bold=True)); o.append(T(cx - 10, cy - 1.42 * u, 'φ' + sub('2'), 15, 'end', bold=True))
    pts = {1: (1, 0), 2: (1, 1), 3: (1, -1)}
    r = (1.4, 0.3)
    dists = {1: 0.500, 2: 0.806, 3: 1.360}
    for k, (a, b) in pts.items():
        o.append(L(fx(r[0]), fy(r[1]), fx(a), fy(b), LV if k == 1 else L2, 2 if k == 1 else 1.5, None if k == 1 else '4 4'))
    for k, (a, b) in pts.items():
        o.append(C(fx(a), fy(b), 7, AC)); o.append(T(fx(a) - 14, fy(b) + 5, 's' + sub(str(k)), 15, 'end', bold=True))
    o.append(C(fx(r[0]), fy(r[1]), 7, LV)); o.append(T(fx(r[0]) + 12, fy(r[1]) - 8, 'r = (1.4, 0.3)', 14, 'start', LV, True))
    o.append(Tb(fx(1.1), fy(0.3), '0.500', 13, 'middle', LV))
    o.append(Tb(fx(1.2), fy(0.65) - 2, '0.806', 13, 'middle', MUT))
    o.append(Tb(fx(1.32), fy(-0.55) + 4, '1.360', 13, 'middle', MUT))
    # right legend
    lx = 520
    o.append(T(lx, 56, 'decide s' + sub('2') + ' above φ' + sub('2') + ' = 0.5', 14, 'start'))
    o.append(T(lx, 200, 'decide s' + sub('1') + ' between', 14, 'start'))
    o.append(T(lx, 220, 'the two lines', 14, 'start'))
    o.append(T(lx, 344, 'decide s' + sub('3') + ' below φ' + sub('2') + ' = −0.5', 14, 'start'))
    o.append(T(lx, 270, 'r is nearest to s' + sub('1') + ': decide s' + sub('1'), 14, 'start', LV, True))
    return 392, ''.join(o)

FIG[6] = (f6, 'Decision regions of the worked example: the boundaries are the perpendicular bisectors φ<sub>2</sub> = ±0.5. The received point r = (1.4, 0.3) is 0.500 from s<sub>1</sub>, 0.806 from s<sub>2</sub> and 1.360 from s<sub>3</sub>, so the receiver decides s<sub>1</sub>, though s<sub>2</sub> has the larger correlation.',
          'Signal plane with points s1 at (1, 0), s2 at (1, 1) and s3 at (1, minus 1). Dashed horizontal boundaries at plus and minus 0.5 split the plane into three bands. A received point at (1.4, 0.3) has distances 0.500, 0.806 and 1.360 to s1, s2 and s3 and lies in the s1 band.', 2)


# ---- 5.7 the precoded duobinary trace ----
def f7():
    o = []
    b = [1, 0, 1, 1, 0, 0, 1, 0]
    p = [0]
    for bk in b: p.append(bk ^ p[-1])
    a = [2 * x - 1 for x in p]
    c = [a[k] + a[k - 1] for k in range(1, 9)]
    bh = [1 if abs(x) < 1 else 0 for x in c]
    x0, cw = 150, 66
    xc = lambda k: x0 + (k - 0.5) * cw  # k = 1..8 centre
    o.append(T(20, 40, 'bit b' + sub('k'), 14, 'start', bold=True))
    for k in range(1, 9):
        o.append(T(xc(k), 40, str(b[k - 1]), 15, bold=True))
        o.append(L(x0 + k * cw, 20, x0 + k * cw, 360, 'var(--line)', 1))
    o.append(T(20, 66, 'precoded p' + sub('k'), 14, 'start'))
    for k in range(1, 9): o.append(T(xc(k), 66, str(p[k]), 14, fill=MUT))
    # polar waveform
    ya, sc = 120, 22
    o.append(T(20, ya + 5, 'polar a' + sub('k'), 14, 'start'))
    o.append(L(x0 - cw, ya, x0 + 8 * cw, ya, L2, 1))
    pts = []
    for k in range(0, 9):
        xl = x0 + (k - 1) * cw
        pts += [(xl, ya - a[k] * sc), (xl + cw, ya - a[k] * sc)]
    o.append(P(pts, NX, 2.5))
    o.append(T(x0 - cw / 2, ya + 36, 'a' + sub('0') + ' = −1', 13, fill=MUT))
    # c levels
    yc, s2 = 250, 34
    fy = lambda v: yc - v * s2
    o.append(T(20, fy(0) + 5, 'c' + sub('k') + ' = a' + sub('k') + ' + a' + sub('k−1'), 14, 'start'))
    for v in (-2, 0, 2): o.append(T(x0 - 10, fy(v) + 5, f'{v:+d}'.replace('+0', '0').replace('-', '−'), 13, 'end', MUT))
    for v in (1, -1): o.append(L(x0, fy(v), x0 + 8 * cw, fy(v), LV, 1.5, '6 4'))
    o.append(T(x0 + 8 * cw + 6, fy(1) + 5, '+1', 13, 'start', LV)); o.append(T(x0 + 8 * cw + 6, fy(-1) + 5, '−1', 13, 'start', LV))
    o.append(L(x0, fy(0), x0 + 8 * cw, fy(0), L2, 1))
    for k in range(1, 9):
        v = c[k - 1]
        o.append(stem(xc(k), fy(0), fy(v), AC, 6) if v else C(xc(k), fy(0), 6, AC))
    o.append(T(20, 346, 'decoded b̂' + sub('k'), 14, 'start', bold=True))
    for k in range(1, 9): o.append(T(xc(k), 346, str(bh[k - 1]), 15, fill=AC, bold=True))
    o.append(T(x0 + 4 * cw, 378, 'thresholds ±1: |c' + sub('k') + '| below 1 means 1, ±2 means 0', 13, fill=MUT))
    return 392, ''.join(o)

FIG[7] = (f7, 'The worked example traced: bits 1 0 1 1 0 0 1 0 are precoded, sent as polar levels and summed with the previous level. Each c<sub>k</sub> is −2, 0 or +2, and the two thresholds at ±1 give back every bit from the current sample alone.',
          'Eight columns. Rows: the bits 1 0 1 1 0 0 1 0, the precoded bits 1 1 0 1 1 1 0 0, a polar staircase waveform, the duobinary levels 0, plus 2, 0, 0, plus 2, plus 2, 0, minus 2 drawn as stems with dashed thresholds at plus and minus 1, and the decoded bits matching the input.', 1)


def spec(k):
    fn, cap, aria, after = FIG[k]
    h, body = fn()
    return {'after_section': after, 'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
