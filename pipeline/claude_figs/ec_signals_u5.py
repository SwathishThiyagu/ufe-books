"""Claude's hand-drawn figures for ec-signals-u5 (Sampling and discrete-time systems), one per chapter.
Every number comes from that chapter's worked example. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

sinc = lambda u: 1.0 if u == 0 else math.sin(math.pi * u) / (math.pi * u)
FIG = {}


def stem(x, y0, y1, c=AC, r=5, w=2.5):
    return L(x, y0, x, y1, c, w) + C(x, y1, r, c)


# ---- 5.1 spectrum of 3cos(2π200t) + 2cos(2π450t) sampled at 1000 Hz ----
def f1():
    x0, x1, base = 60, 690, 330
    fx = lambda f: x0 + f / 1500 * (x1 - x0)
    fy = lambda a: base - a * 120
    o = [xaxis(x0, x1, base, [0, 500, 1000, 1500], fx, 'frequency f (Hz)')]
    o.append(L(x0, base, x0, 44, L2, 1.5))
    o.append(T(x0 + 8, 40, 'X<tspan font-size="11" dy="4">s</tspan><tspan dy="-4">(f)</tspan>', 14, 'start', MUT))
    # ideal filter box 0..500
    o.append(R(fx(0), fy(2.2), fx(500) - fx(0), fy(0) - fy(2.2), ACS, AC, 2, 2, '7 5'))
    o.append(T(fx(250), fy(2.2) + 22, 'ideal low-pass filter', 14, fill=AC, bold=True))
    o.append(T(fx(250), fy(2.2) + 40, 'cutoff 500 Hz, gain T<tspan font-size="11" dy="4">s</tspan>', 14, fill=AC))
    base_lines = [(200, 1.5), (450, 1.0)]
    copy_lines = [(550, 1.0), (800, 1.5), (1200, 1.5), (1450, 1.0)]
    for f, a in base_lines:
        o.append(stem(fx(f), base, fy(a), AC)); o.append(T(fx(f), fy(a) - 12, str(f), 14, bold=True))
    for f, a in copy_lines:
        o.append(stem(fx(f), base, fy(a), NX)); o.append(T(fx(f), fy(a) - 12, str(f), 14, bold=True, fill=NX))
    o.append(L(fx(1000), base, fx(1000), 80, L2, 1.5, '4 4'))
    o.append(Tb(fx(1000), 74, 'copy centred at f<tspan font-size="11" dy="4">s</tspan><tspan dy="-4"> = 1000 Hz</tspan>', 14, fill=NX))
    o.append(brace(fx(450), fx(550), base + 50, INK, up=True))
    o.append(T(fx(500), base + 72, 'guard band 450 to 550 Hz = 100 Hz', 14))
    return 425, ''.join(o)

FIG[1] = (f1, 'The samples of 3 cos(2π·200t) + 2 cos(2π·450t) at 1000 Hz: the baseband lines at 200 and 450 Hz, and the copy around 1000 Hz with lines at 550, 800, 1200 and 1450 Hz. The ideal filter up to 500 Hz keeps only the baseband; the 100 Hz guard band is the gap it cuts in.',
          'Spectrum lines at 200 and 450 hertz inside a dashed ideal low-pass filter box up to 500 hertz, and copy lines at 550, 800, 1200 and 1450 hertz around 1000 hertz, with the guard band from 450 to 550 hertz marked.')


# ---- 5.2 cos(2π700t) and cos(2π300t) give the same samples at 1000 Hz ----
def f2():
    x0, x1, y0, y1 = 70, 690, 70, 290
    fx = lambda t: x0 + t / 10 * (x1 - x0)
    mid = (y0 + y1) / 2
    fy = lambda v: mid - v * (y1 - y0) / 2.6
    o = [L(x0, mid, x1, mid, L2, 1.5), L(x0, y0 - 10, x0, y1 + 10, L2, 1.5)]
    for v in (-1, 0, 1):
        o.append(T(x0 - 9, fy(v) + 4.5, neg(v), 13, 'end', MUT))
        if v: o.append(L(x0, fy(v), x1, fy(v), LN, 1))
    for n in range(0, 11):
        o.append(L(fx(n), y1 + 10, fx(n), y1 + 15, L2, 1.5)); o.append(T(fx(n), y1 + 32, str(n), 13, fill=MUT))
    o.append(T((x0 + x1) / 2, y1 + 54, 'time t (ms) = sample index n', 14, fill=MUT))
    o.append(P([(fx(t / 100), fy(math.cos(2 * math.pi * 0.7 * t / 100))) for t in range(0, 1001)], AC, 2))
    o.append(P([(fx(t / 100), fy(math.cos(2 * math.pi * 0.3 * t / 100))) for t in range(0, 1001)], LV, 3, '8 5'))
    for n in range(0, 11):
        o.append(C(fx(n), fy(math.cos(2 * math.pi * 0.3 * n)), 6.5, NX))
    o += [L(90, 26, 122, 26, AC, 2.5), T(130, 31, '700 Hz', 14, 'start'),
          L(220, 26, 252, 26, LV, 3, '8 5'), T(260, 31, '300 Hz alias', 14, 'start'),
          C(400, 26, 6.5, NX), T(414, 31, 'samples at f<tspan font-size="11" dy="4">s</tspan><tspan dy="-4"> = 1000 Hz</tspan>', 14, 'start')]
    return 370, ''.join(o)

FIG[2] = (f2, 'Sampled every 1 ms, the 700 Hz cosine (solid) and the 300 Hz cosine (dashed) pass through the same eleven dots, so after sampling the 700 Hz tone is read as 300 Hz.',
          'A fast 700 hertz cosine and a slower dashed 300 hertz cosine over 10 milliseconds, both passing through the same sample dots at every millisecond.')


# ---- 5.3 band-pass sampling of 5-6 kHz at 2.45 kHz, and the aperture droop ----
def f3():
    o = []
    # top panel
    x0, x1, base = 60, 690, 200
    fx = lambda f: x0 + f / 6.5 * (x1 - x0)
    o.append(T(x0, 28, 'Band 5 to 6 kHz sampled at f<tspan font-size="11" dy="4">s</tspan><tspan dy="-4"> = 2.45 kHz</tspan>', 15, 'start', bold=True))
    for k in range(1, 6):
        z = k * 1.225
        o.append(L(fx(z), base, fx(z), 70, L2, 1.2, '4 4'))
    for k, lab in ((1, '1'), (2, '2'), (3, '3'), (4, '4')):
        o.append(T(fx((k - 0.5) * 1.225), 62, f'zone {lab}', 13, fill=MUT))
    o.append(T(fx(5.5125), 62, 'zone 5', 13, fill=AC, bold=True))
    def band(a, b, up, c, fill, h=95):
        lo, hi = max(a, 0), min(b, 6.5)
        ya = lambda f: base - (25 + 70 * ((f - a) / (b - a) if up else (b - f) / (b - a)))
        pts = [(fx(lo), base), (fx(lo), ya(lo)), (fx(hi), ya(hi)), (fx(hi), base)]
        return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" style="fill:{fill};stroke:{c};stroke-width:2"/>'
    o.append(band(5, 6, True, AC, ACS))
    o.append(band(0.1, 1.1, True, LV, LVS))
    for a, b, up in ((2.55, 3.55, True), (1.35, 2.35, False), (3.8, 4.8, False), (6.25, 7.25, False)):
        o.append(band(a, b, up, NX, NXS))
    o.append(xaxis(x0, x1, base, [0, 1, 2, 3, 4, 5, 6], fx, None))
    o.append(T(fx(6.5) - 2, base + 20, 'kHz', 13, 'end', MUT))
    o.append(Tb(fx(5.5), base - 108, 'original band', 14, fill=AC))
    o.append(Tb(fx(0.6) + 10, base - 108, 'image used: 0.1–1.1 kHz', 14, 'start', LV))
    # bottom panel
    X0, X1, Y0, Y1 = 70, 690, 300, 500
    gx = lambda f: X0 + f / 8 * (X1 - X0)
    gy = lambda g: Y1 - g * (Y1 - Y0)
    o.append(T(X0 - 10, 268, 'Aperture gain |sinc(fτ)| of a flat-top sampler at f<tspan font-size="11" dy="4">s</tspan><tspan dy="-4"> = 8 kHz</tspan>', 15, 'start', bold=True))
    o.append(axes(X0, X1, Y0, Y1, [0, 2, 4, 6, 8], [0, 0.5, 1], gx, gy, 'frequency (kHz)', ''))
    o.append(P([(gx(f / 50), gy(abs(sinc(f / 50 * 0.125)))) for f in range(0, 401)], AC, 2.5))
    o.append(P([(gx(f / 50), gy(abs(sinc(f / 50 * 0.01)))) for f in range(0, 401)], LV, 2.5, '8 5'))
    for f, g, lab, dx, anc in ((3.4, sinc(0.425), '3.4 kHz: 0.728', -10, 'end'), (4, sinc(0.5), '4 kHz: 0.637', 12, 'start')):
        o.append(L(gx(f), Y1, gx(f), gy(g), L2, 1.2, '4 4')); o.append(C(gx(f), gy(g), 6, NX))
        o.append(Tb(gx(f) + dx, gy(g) + 22 if anc == 'end' else gy(g) - 8, lab, 14, anc))
    o.append(T(gx(7.9), gy(1) - 10, 'τ = 10 μs (almost flat)', 14, 'end', LV))
    o.append(T(gx(6.2), gy(0.32), 'τ = T<tspan font-size="11" dy="4">s</tspan><tspan dy="-4"> = 125 μs</tspan>', 14, 'start', AC))
    return 560, ''.join(o)

FIG[3] = (f3, 'Top: at 2.45 kHz the 5–6 kHz band fits inside zone 5, so its copies fall into the empty gaps and one image lands at 0.1–1.1 kHz the right way round; mirrored copies slope the other way. Bottom: a full-period hold (τ = 125 μs) droops to 0.728 at 3.4 kHz and 0.637 at 4 kHz, while a 10 μs pulse stays almost flat.',
          'Top panel: a band from 5 to 6 kilohertz and its copies between dashed Nyquist zone lines every 1.225 kilohertz, with the image from 0.1 to 1.1 kilohertz highlighted. Bottom panel: sinc gain curves for hold times of 125 and 10 microseconds, with points at 3.4 and 4 kilohertz.')


# ---- 5.4 3-bit mid-rise quantizer on 0..8 V and its error ----
def f4():
    o = []
    x0, x1, y0, y1 = 80, 400, 40, 360
    fx = lambda v: x0 + v / 8 * (x1 - x0)
    fy = lambda v: y1 - v / 8 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 2, 4, 6, 8], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5], fx, fy, 'input x (V)', 'output Q(x) (V)'))
    o.append(L(fx(0), fy(0), fx(8), fy(8), L2, 1.5, '6 5'))
    pts = []
    for k in range(8):
        pts += [(fx(k), fy(k + 0.5)), (fx(k + 1), fy(k + 0.5))]
    o.append(P(pts, AC, 3))
    o.append(L(fx(3.4), y1, fx(3.4), fy(3.5), NX, 1.5, '4 4'))
    o.append(C(fx(3.4), fy(3.5), 6.5, NX))
    o.append(Tb(fx(3.4) + 12, fy(3.5) - 14, 'x = 3.4 V → 3.5 V', 14, 'start'))
    o.append(T(fx(6.1), fy(4.3), 'Δ = 1 V', 14, 'start', AC, True))
    # error panel
    X0, X1, Y0, Y1 = 470, 700, 130, 290
    gx = lambda v: X0 + v / 8 * (X1 - X0)
    gy = lambda e: (Y0 + Y1) / 2 - e / 0.5 * (Y1 - Y0) / 2
    o.append(T((X0 + X1) / 2, 80, 'error e<tspan font-size="11" dy="4">q</tspan><tspan dy="-4"> = Q(x) − x</tspan>', 14, fill=MUT))
    o.append(L(X0, gy(0), X1, gy(0), L2, 1.5)); o.append(L(X0, Y0 - 10, X0, Y1 + 10, L2, 1.5))
    for e in (-0.5, 0, 0.5):
        o.append(T(X0 - 8, gy(e) + 4.5, neg(e) if e else '0', 13, 'end', MUT))
        if e: o.append(L(X0, gy(e), X1, gy(e), LN, 1))
    for v in (0, 4, 8):
        o.append(T(gx(v), Y1 + 30, str(v), 13, fill=MUT))
    o.append(T((X0 + X1) / 2, Y1 + 52, 'input x (V)', 14, fill=MUT))
    for k in range(8):
        o.append(L(gx(k), gy(0.5), gx(k + 1), gy(-0.5), AC, 2.5))
        if k: o.append(L(gx(k), gy(-0.5), gx(k), gy(0.5), AC, 1, '3 3'))
    o.append(C(gx(3.4), gy(0.1), 6, NX))
    o.append(Tb(gx(3.4), gy(0.1) - 40, '+0.1 V', 14))
    o.append(L(gx(3.4), gy(0.1) - 33, gx(3.4), gy(0.1) - 8, INK, 1.2))
    return 410, ''.join(o)

FIG[4] = (f4, 'Left: the 3-bit, 0 V to 8 V mid-rise quantizer climbs in steps of Δ = 1 V to the levels 0.5, 1.5, …, 7.5 V; the input 3.4 V is rounded to 3.5 V. Right: the error e_q = Q(x) − x saws between +0.5 V and −0.5 V on every step and is +0.1 V at 3.4 V.',
          'A staircase from 0 to 8 volts with levels at 0.5 to 7.5 volts beside a dashed ideal line, the input 3.4 volts marked at output 3.5 volts, and a sawtooth error plot between plus and minus 0.5 volts.')


# ---- 5.5 flip and slide for y[1] with x = [2,1,3], h = [1,2] ----
def f5():
    o = []
    x0, x1 = 110, 690
    ks = list(range(-2, 5))
    fx = lambda k: x0 + (k + 2) / 6 * (x1 - x0)
    def row(base, vals, c, lab, idx='k', hl=None, sc=22):
        r = [L(x0 - 20, base, x1 + 10, base, L2, 1.5), T(18, base - 22, lab, 15, 'start', bold=True)]
        for k in ks:
            r.append(T(fx(k), base + 20, neg(k), 13, fill=MUT))
        for k, v in vals.items():
            col = NX if hl == k else c
            r.append(stem(fx(k), base, base - v * sc, col, 6)); r.append(T(fx(k) + 14, base - v * sc - 2, str(v), 14, 'start', col, True))
        r.append(T(x1 + 14, base + 20, idx, 13, 'start', MUT))
        return ''.join(r)
    o.append(row(100, {0: 2, 1: 1, 2: 3}, AC, 'x[k]'))
    o.append(row(200, {0: 2, 1: 1}, LV, 'h[1 − k]'))
    o.append(Tb(fx(3), 160, 'h flipped, shifted to n = 1', 14, fill=LV))
    o.append(Tb((x0 + x1) / 2 + 40, 256, 'y[1] = x[0]h[1] + x[1]h[0] = 2·2 + 1·1 = 5', 15))
    o.append(row(400, {0: 2, 1: 5, 2: 5, 3: 6}, AC, 'y[n]', 'n', hl=1, sc=15))
    return 440, ''.join(o)

FIG[5] = (f5, 'To find y[1], flip h[k] = [1, 2] and slide it to n = 1: it overlaps x[k] at k = 0 (2 × 2) and k = 1 (1 × 1), so y[1] = 5. Repeating the slide for every n gives y[n] = [2, 5, 5, 6].',
          'Three stem plots: x of k equal to 2, 1, 3 at k 0 to 2; the flipped and shifted h of 1 minus k equal to 2 and 1 at k 0 and 1; and the output y of n equal to 2, 5, 5, 6 with y of 1 highlighted.')


# ---- 5.6 second-order recursive system and its impulse response ----
def f6():
    o = []
    # block diagram (direct form I, output side)
    o.append(T(20, 26, 'y[n] = x[n] + 0.75y[n − 1] − 0.125y[n − 2]', 15, 'start', bold=True))
    sx, sy = 150, 90
    o.append(T(30, sy + 5, 'x[n]', 15, 'start', bold=True))
    o.append(L(70, sy, sx - 22, sy, AC, 2, arrow='n'))
    o.append(f'<circle cx="{sx}" cy="{sy}" r="20" style="fill:var(--panel);stroke:var(--accent);stroke-width:2"/>' + T(sx, sy + 6, 'Σ', 18, bold=True))
    ox = 330
    o.append(L(sx + 20, sy, ox + 40, sy, AC, 2, arrow='n')); o.append(T(ox + 46, sy + 5, 'y[n]', 15, 'start', bold=True))
    o.append(C(ox, sy, 4, AC))
    # delays
    o.append(L(ox, sy, ox, 140, AC, 2, arrow='n'))
    o.append(boxt(ox - 30, 142, 60, 34, ['z⁻¹'], PANEL, AC, 15))
    o.append(L(ox, 176, ox, 236, AC, 2, arrow='n'))
    o.append(boxt(ox - 30, 238, 60, 34, ['z⁻¹'], PANEL, AC, 15))
    o.append(T(ox + 38, 213, 'y[n − 1]', 14, 'start', MUT))
    o.append(T(ox + 38, 300, 'y[n − 2]', 14, 'start', MUT))
    # taps
    t1, t2 = 205, 300
    o.append(C(ox, t1, 4, AC)); o.append(L(ox, t1, 262, t1, AC, 2, arrow='n'))
    o.append(boxt(206, t1 - 17, 54, 34, ['0.75'], LVS, LV, 14))
    o.append(P([(206, t1), (sx, t1), (sx, sy + 22)], AC, 2)); o.append(L(sx, sy + 40, sx, sy + 23, AC, 2, arrow='n'))
    o.append(L(ox, 272, ox, t2, AC, 2)); o.append(L(ox, t2, 270, t2, AC, 2, arrow='n'))
    o.append(boxt(196, t2 - 17, 72, 34, ['−0.125'], LVS, LV, 14))
    o.append(P([(196, t2), (sx - 12, t2), (sx - 12, sy + 17)], AC, 2))
    o.append(L(sx - 12, sy + 40, sx - 12, sy + 20, AC, 2, arrow='n'))
    # stem plot of h[n]
    X0, X1, B = 470, 700, 300
    h = [2 * 0.5 ** n - 0.25 ** n for n in range(7)]
    gx = lambda n: X0 + 12 + n * (X1 - X0 - 24) / 6
    gy = lambda v: B - v * 190
    o.append(T((X0 + X1) / 2, 74, 'impulse response h[n]', 14, fill=MUT))
    o.append(L(X0, B, X1, B, L2, 1.5))
    for n, v in enumerate(h):
        o.append(stem(gx(n), B, gy(v), NX if n < 4 else AC, 5)); o.append(T(gx(n), B + 20, str(n), 13, fill=MUT))
    for n, lab in ((0, '1'), (1, '0.75'), (2, '0.4375'), (3, '0.234')):
        o.append(T(gx(n) + 8, gy(h[n]) - 10, lab, 13, 'start' if n else 'middle'))
    o.append(T((X0 + X1) / 2, B + 44, 'h[n] = 2(0.5)ⁿ − (0.25)ⁿ', 14))
    return 360, ''.join(o)

FIG[6] = (f6, 'Left: the output y[n] passes through two unit delays; the taps y[n − 1] and y[n − 2] are scaled by 0.75 and −0.125 and fed back to the adder. Right: the impulse response this loop produces, 1, 0.75, 0.4375, 0.234, …, which decays because both roots, 0.5 and 0.25, are inside the unit circle.',
          'Block diagram with an adder, two unit delays and multipliers 0.75 and minus 0.125 feeding back to the adder, beside a stem plot of the impulse response decaying from 1.')

spec = make_spec(FIG)


# ---- question bank: aliasing sketch for the model answer (triangle of half-width 700 Hz sampled at 1000 Hz) ----
def bank_alias():
    x0, x1, base = 60, 690, 230
    fx = lambda f: x0 + f / 1600 * (x1 - x0)
    fy = lambda a: base - a * 150
    o = [xaxis(x0, x1, base, [0, 300, 500, 700, 1000, 1300, 1600], fx, 'frequency f (Hz)')]
    tri = lambda c: [(fx(max(c - 700, 0)), fy(max(0, 1 - abs(max(c - 700, 0) - c) / 700))), (fx(c), fy(1)), (fx(min(c + 700, 1600)), fy(max(0, 1 - abs(min(c + 700, 1600) - c) / 700)))]
    o.append(f'<polygon points="{fx(0):.1f},{base} {fx(0):.1f},{fy(1):.1f} {fx(700):.1f},{base}" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2"/>')
    o.append(f'<polygon points="{fx(300):.1f},{base} {fx(1000):.1f},{fy(1):.1f} {fx(1600):.1f},{fy(1 - 600 / 700):.1f} {fx(1600):.1f},{base}" style="fill:var(--next-soft);stroke:var(--next);stroke-width:2"/>')
    # sum outline in the overlap 300..700: 1 - f/700 + 1 - (1000 - f)/700 = (f - ... ) constant 4/7
    o.append(P([(fx(0), fy(1)), (fx(300), fy(1 - 300 / 700)), (fx(700), fy(1 - 300 / 700)), (fx(1000), fy(1))], INK, 2, '6 4'))
    o.append(L(fx(500), base, fx(500), 40, L2, 1.5, '4 4'))
    o.append(Tb(fx(500), 36, 'f_s/2 = 500 Hz'.replace('f_s', 'f<tspan font-size="11" dy="4">s</tspan><tspan dy="-4">').replace('/2 = 500 Hz', '/2 = 500 Hz</tspan>'), 14))
    o.append(T(fx(150), fy(1) - 10, 'baseband', 14, fill=AC))
    o.append(T(fx(1000), fy(1) - 10, 'copy at f<tspan font-size="11" dy="4">s</tspan><tspan dy="-4"> = 1000 Hz</tspan>', 14, fill=NX))
    o.append(Tb(fx(500), fy(0.2), 'overlap 300–700 Hz', 14))
    o.append(T(fx(1150), fy(0.55) - 20, 'dashed: the sum', 14, 'start'))
    return 290, ''.join(o)

def bank_svg(name):
    h, body = {'alias': bank_alias}[name]()
    return {'h': h, 'body': body, 'aria': 'A triangular baseband spectrum up to 700 hertz and its copy centred at 1000 hertz overlapping between 300 and 700 hertz, with the Nyquist frequency of 500 hertz marked and the dashed sum flattened in the overlap.'}
