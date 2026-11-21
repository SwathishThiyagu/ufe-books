"""Claude's hand-drawn figures for ec-antenna-u6 (Radar systems), one per chapter.
Every number comes from that chapter's worked example. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
sub = lambda s: f'<tspan font-size="11" dy="4">{s}</tspan><tspan dy="-4">​</tspan>'
sup = lambda s: f'<tspan font-size="11" dy="-6">{s}</tspan><tspan dy="6">​</tspan>'


def arrow(x1, y1, x2, y2, c=AC, w=2, a='n', dash=None):
    return L(x1, y1, x2, y2, c, w, dash, a)


# ---- 6.1 pulse radar block diagram and the 124 µs echo ----
def f1():
    o = []
    W, H = 128, 58
    top, bot = 34, 150
    xs = [16, 176, 336, 496]
    names = [('Synchronizer', 'PRF timer'), ('Modulator', 'HV pulse, τ'), ('Transmitter', 'kW to MW'), ('Duplexer', 'TR and ATR')]
    for x, (a, b) in zip(xs, names):
        o.append(boxt(x, top, W, H, [a, b], ACS if a == 'Duplexer' else PANEL, AC, 13, bold_first=True))
    for i in range(3):
        o.append(arrow(xs[i] + W, top + H / 2, xs[i + 1] - 4, top + H / 2))
    bnames = [(176, 'Display', 'PPI'), (336, 'Signal processor', 'MTI, CFAR'), (496, 'Receiver', 'LNA, mixer, IF')]
    for x, a, b in bnames:
        o.append(boxt(x, bot, W, H, [a, b], LVS if a == 'Receiver' else PANEL, LV if a == 'Receiver' else AC, 13, bold_first=True))
    o.append(arrow(496, bot + H / 2, 464 + 4, bot + H / 2, LV, 2, 'l'))
    o.append(arrow(336, bot + H / 2, 304 + 4, bot + H / 2, LV, 2, 'l'))
    o.append(arrow(560, top + H, 560, bot - 4, LV, 2, 'l'))
    o.append(T(568, 128, 'echo', 13, 'start', fill=LV))
    # antenna: a dish to the right of the duplexer
    ax = 666
    o.append(f'<path d="M{ax + 22},{top - 8} Q{ax - 14},{top + H / 2} {ax + 22},{top + H + 8}" style="fill:none;stroke:{AC};stroke-width:3"/>')
    o.append(L(624, top + H / 2 - 6, ax + 2, top + H / 2 - 6, AC, 2, None, 'n'))
    o.append(L(ax + 2, top + H / 2 + 8, 628, top + H / 2 + 8, LV, 2, '6 4', 'l'))
    o.append(T(ax + 6, top + H + 30, 'Antenna', 13, bold=True))
    # range zero from the synchronizer to the display
    o.append(P([(80, top + H), (80, bot + H / 2), (172, bot + H / 2)], MUT, 2, '6 4'))
    o.append(f'<polygon points="172,{bot + H / 2 - 5} 176,{bot + H / 2} 172,{bot + H / 2 + 5}" style="fill:{MUT}"/>')
    o.append(T(88, bot + H / 2 + 22, 'range zero', 13, 'start', fill=MUT))
    # timing strip
    y = 300
    fx = lambda t: 60 + t * 4.0
    o.append(xaxis(60, 660, y, [0, 50, 100, 150], fx, 'time after the pulse leaves (µs)', lambda v: f'{v}'))
    o.append(R(fx(0), y - 56, 6, 56, AC, AC, 1, 1))
    o.append(T(fx(0) + 12, y - 42, 'pulse, τ = 1 µs', 13, 'start', fill=AC, bold=True))
    o.append(R(fx(124), y - 22, 6, 22, LV, LV, 1, 1))
    o.append(T(fx(124) + 3, y - 30, 'echo', 13, fill=LV, bold=True))
    o.append(brace(fx(0) + 3, fx(124) + 3, y - 66, INK, up=False))
    o.append(Tb(fx(62), y - 74, 't = 124 µs  →  R = ct/2 = 18.6 km', 14, bold=True))
    return 358, ''.join(o)

FIG[1] = (f1, 'The pulse travels along the top row to the antenna; its echo comes back through the duplexer to the receiver, processor and display. Below, the worked example: an echo 124 µs after a 1 µs pulse puts the target at 18.6 km.',
          'Block diagram. Top row: synchronizer, modulator, transmitter, duplexer, then a dish antenna. The echo returns from the antenna to the duplexer and down to the receiver, then left to the signal processor and the display. A dashed line from the synchronizer to the display marks range zero. Below, a time axis from 0 to 150 microseconds shows the 1 microsecond pulse at zero and the echo at 124 microseconds, giving 18.6 km.')


# ---- 6.2 echo power against range, for 1 and 100 m² ----
def f2():
    x0, x1, y0, y1 = 90, 600, 40, 340
    lx = lambda r: x0 + (math.log10(r) - 1) / (math.log10(200) - 1) * (x1 - x0)   # 10 .. 200 km
    ly = lambda p: y0 + (-100 - p) / 60 * (y1 - y0)                              # -100 .. -160 dBW
    o = [L(x0, y1, x1, y1, L2, 1.5), L(x0, y0, x0, y1, L2, 1.5)]
    for r in (10, 20, 50, 100, 200):
        o += [L(lx(r), y1, lx(r), y1 + 5, L2, 1.5), T(lx(r), y1 + 20, str(r), 13, fill=MUT)]
    for p in (-100, -110, -120, -130, -140, -150, -160):
        o += [L(x0 - 5, ly(p), x0, ly(p), L2, 1.5), L(x0, ly(p), x1, ly(p), LN, 1), T(x0 - 9, ly(p) + 4.5, neg(p), 13, 'end', MUT)]
    o.append(T((x0 + x1) / 2, y1 + 42, 'range R (km), log scale', 14, fill=MUT))
    o.append(T(x0, y0 - 16, 'echo power P' + sub('r') + ' (dBW)', 14, 'start', MUT))
    k = 5e5 * 1e6 * 9e-4 / (4 * math.pi) ** 3
    for sg, c, lab, lr in ((1, AC, 'σ = 1 m²', 14), (100, NX, 'σ = 100 m²', 28)):
        pts = []
        for i in range(101):
            r = 10 ** (1 + i / 100 * (math.log10(200) - 1))
            p = 10 * math.log10(k * sg / (r * 1e3) ** 4)
            if -160 <= p <= -100: pts.append((lx(r), ly(p)))
        o.append(P(pts, c, 3))
        p = 10 * math.log10(k * sg / (lr * 1e3) ** 4)
        o.append(T(lx(lr) + 12, ly(p) - 6, lab, 14, 'start', fill=c, bold=True))
    o.append(L(x0, ly(-130), x1, ly(-130), LV, 2.5, '8 5'))
    o.append(Tb(lx(10.6), ly(-130) + 22, 'S' + sub('min') + ' = 10⁻¹³ W = −130 dBW', 13, 'start', fill=LV, bold=True))
    for r, c in ((38.8, AC), (122.7, NX)):
        o.append(L(lx(r), ly(-130), lx(r), y1, c, 1.5, '3 4'))
        o.append(C(lx(r), ly(-130), 6, c))
    o.append(Tb(lx(38.8), ly(-136) + 4, '38.8 km', 13, fill=AC, bold=True))
    o.append(Tb(lx(122.7), ly(-136) + 4, '122.7 km', 13, fill=NX, bold=True))
    o.append(T(lx(10.6), ly(-150), 'slope: 40 dB per tenfold', 13, 'start', fill=MUT))
    o.append(T(lx(10.6), ly(-150) + 18, 'range (1/R⁴)', 13, 'start', fill=MUT))
    return 400, ''.join(o)

FIG[2] = (f2, 'Echo power of the first worked example (500 kW, 30 dB, 10 GHz) falls 40 dB for every tenfold increase in range. It meets the −130 dBW minimum detectable signal at 38.8 km for 1 m²; a target 100 times larger reaches only 122.7 km, 3.16 times farther.',
          'Log graph of echo power in dBW against range from 10 to 200 km. Two straight falling lines, for cross sections of 1 and 100 square metres, cross a dashed line at minus 130 dBW at 38.8 km and 122.7 km.')


# ---- 6.3 exact RCS of a metal sphere against ka ----
def _mie(x):
    # PEC sphere, monostatic, sigma / (pi a^2); spherical Bessel functions by upward recurrence
    N = int(x + 4 * x ** (1 / 3) + 8)
    j = [math.sin(x) / x, math.sin(x) / x ** 2 - math.cos(x) / x]
    y = [-math.cos(x) / x, -math.cos(x) / x ** 2 - math.sin(x) / x]
    for n in range(1, N + 1):
        j.append((2 * n + 1) / x * j[n] - j[n - 1]); y.append((2 * n + 1) / x * y[n] - y[n - 1])
    s = 0
    for n in range(1, N + 1):
        h = complex(j[n], y[n]); hm = complex(j[n - 1], y[n - 1])
        xj = x * j[n - 1] - n * j[n]; xh = x * hm - n * h           # [x f_n(x)]' = x f_(n-1) - n f_n
        a = j[n] / h; b = xj / xh
        s += (-1) ** n * (2 * n + 1) * (b - a)
    return abs(s) ** 2 / x ** 2

def f3():
    x0, x1, y0, y1 = 90, 600, 40, 330
    lx = lambda k: x0 + (math.log10(k) - math.log10(0.05)) / (math.log10(20) - math.log10(0.05)) * (x1 - x0)
    ly = lambda s: y0 + (1 - math.log10(s)) / 6 * (y1 - y0)          # 10 .. 1e-5
    o = [L(x0, y1, x1, y1, L2, 1.5), L(x0, y0, x0, y1, L2, 1.5)]
    for k, s in ((0.1, '0.1'), (1, '1'), (10, '10')):
        o += [L(lx(k), y1, lx(k), y1 + 5, L2, 1.5), T(lx(k), y1 + 20, s, 13, fill=MUT)]
    for e in range(-5, 2):
        s = 10.0 ** e
        o += [L(x0 - 5, ly(s), x0, ly(s), L2, 1.5), L(x0, ly(s), x1, ly(s), LN, 1), T(x0 - 9, ly(s) + 4.5, '10' + sup(neg(e)) if e not in (0, 1) else ('1' if e == 0 else '10'), 13, 'end', MUT)]
    o.append(T((x0 + x1) / 2, y1 + 42, 'sphere size ka = 2πa/λ, log scale', 14, fill=MUT))
    o.append(T(x0, y0 - 16, 'σ / πa², log scale', 14, 'start', MUT))
    # region bands
    o.append(R(lx(1), y0, lx(10) - lx(1), y1 - y0, ACS, 'none', 0, 0))
    o.append(T((lx(0.05) + lx(1)) / 2 + 60, y1 - 14, 'Rayleigh', 14, fill=MUT, bold=True))
    o.append(T((lx(1) + lx(10)) / 2, y1 - 14, 'resonance', 14, fill=AC, bold=True))
    o.append(T((lx(10) + lx(20)) / 2, y1 - 14, 'optical', 14, fill=MUT, bold=True))
    ks = [10 ** (math.log10(0.05) + i / 400 * (math.log10(20) - math.log10(0.05))) for i in range(401)]
    o.append(P([(lx(k), ly(9 * k ** 4)) for k in ks if 0.3 < k and 9 * k ** 4 < 10], NX, 2, '7 5'))
    o.append(P([(lx(k), ly(_mie(k))) for k in ks], AC, 3))
    o.append(T(lx(0.72) - 6, ly(4.0), '9(ka)⁴', 13, 'end', fill=NX, bold=True))
    o.append(C(lx(1.02), ly(3.65), 6, AC)); o.append(T(lx(1.02) + 10, ly(3.65) - 8, 'peak 3.65 at ka ≈ 1', 13, 'start', bold=True))
    o.append(L(lx(10), ly(1), x1, ly(1), L2, 1.5, '4 4'))
    for k, lab in ((0.0628, 'raindrop, 3 GHz'), (0.2094, 'raindrop, 10 GHz')):
        v = 9 * k ** 4
        o.append(C(lx(k), ly(v), 6, LV)); o.append(T(lx(k) + 10, ly(v) + 18, lab, 13, 'start', fill=LV, bold=True))
    o.append(T(x1 + 8, ly(1) + 5, 'σ = πa²', 13, 'start', bold=True))
    o.append(T(x1 + 8, ly(1) + 24, '(ka = 118:', 13, 'start', fill=MUT))
    o.append(T(x1 + 8, ly(1) + 42, 'first example)', 13, 'start', fill=MUT))
    return 390, ''.join(o)

FIG[3] = (f3, 'The exact cross section of a metal sphere, divided by πa². Small spheres follow 9(ka)⁴, so the raindrop of the second example is 123 times brighter at 10 GHz than at 3 GHz; near ka = 1 the curve peaks at 3.65; above ka ≈ 10 it settles at πa², where the first example\'s sphere (ka = 118) sits.',
          'Log-log graph of sphere radar cross section over pi a squared against ka from 0.05 to 20. The curve rises steeply along a dashed 9 ka to the fourth line, peaks at 3.65 near ka equals 1, ripples in the shaded resonance band from 1 to 10 and settles at 1 in the optical region. Two points mark a 1 mm raindrop at 3 and 10 GHz.')


# ---- 6.4 a 200 km target at two PRFs ----
def f4():
    o = []
    fx = lambda t: 70 + t * 290.0        # 0 .. 2 ms
    rows = [(130, 1.0, '1000 Hz', '150 km', '0.333 ms → 50 km'), (270, 0.8, '1250 Hz', '120 km', '0.533 ms → 80 km')]
    te = 2 * 200e3 / 3e8 * 1e3           # 1.333 ms
    for y, T_, prf, ru, app in rows:
        o.append(L(fx(0), y, fx(2.0), y, L2, 1.5))
        o.append(T(16, y - 52, f'PRF {prf}: pulses every {T_:g} ms, R' + sub('unamb') + f' = {ru}', 14, 'start', bold=True))
        n = 0
        while n * T_ <= 2.0 + 1e-9:
            o.append(R(fx(n * T_) - 3, y - 40, 6, 40, AC, AC, 1, 1)); n += 1
        o.append(R(fx(te) - 3, y - 18, 6, 18, LV, LV, 1, 1))
        last = math.floor(te / T_) * T_
        o.append(brace(fx(last), fx(te), y + 14, LV, up=True))
        o.append(T((fx(last) + fx(te)) / 2, y + 34, app, 13, fill=LV, bold=True))
        o.append(T(fx(te), y - 24, 'echo', 13, fill=LV))
        for t in (0, 0.5, 1.0, 1.5, 2.0):
            o.append(L(fx(t), y, fx(t), y + 5, L2, 1.5))
        o.append(T(fx(2.0) + 8, y + 5, 'ms', 13, 'start', fill=MUT))
    for t in (0, 0.5, 1.0, 1.5, 2.0):
        o.append(T(fx(t), 270 + 50, f'{t:g}', 13, fill=MUT))
    o.append(L(fx(te), 46, fx(te), 288, LV, 1.5, '3 4'))
    o.append(Tb(fx(te), 36, 'true delay 2R/c = 1.333 ms (200 km)', 13, fill=LV, bold=True))
    o.append(T(360, 362, 'Only 200 km fits both: 50 + 150n and 80 + 120n', 14, bold=True, fill=AC))
    return 382, ''.join(o)

FIG[4] = (f4, 'The worked examples\' target at 200 km returns 1.333 ms after its pulse. At 1000 Hz the radar times it from the latest pulse and shows 50 km; at 1250 Hz it shows 80 km. Only 200 km fits both readings.',
          'Two time lines from 0 to 2 milliseconds. Top: pulses every 1 millisecond; the echo at 1.333 milliseconds is 0.333 milliseconds after the second pulse, read as 50 km. Bottom: pulses every 0.8 milliseconds; the same echo is 0.533 milliseconds after the second pulse, read as 80 km. A dashed line marks the true delay of 1.333 milliseconds for 200 km.')


# ---- 6.5 triangular FMCW sweep and the two beats ----
def f5():
    o = []
    x0, x1 = 90, 610
    fx = lambda t: x0 + t / 2.0 * (x1 - x0)            # 0 .. 2 ms
    # top: frequency sweep (schematic delay)
    ya, yb = 46, 170                                     # 150 MHz .. 0
    fy = lambda f: yb - f / 150 * (yb - ya)
    o.append(L(x0, yb, x1, yb, L2, 1.5)); o.append(L(x0, ya - 6, x0, yb, L2, 1.5))
    o.append(T(x0 - 9, fy(150) + 4.5, '+150', 13, 'end', MUT)); o.append(T(x0 - 9, fy(0) + 4.5, '0', 13, 'end', MUT))
    o.append(T(x0, ya - 18, 'transmit frequency above 77 GHz (MHz)', 14, 'start', MUT))
    o.append(P([(fx(0), fy(0)), (fx(1), fy(150)), (fx(2), fy(0))], AC, 3))
    d, s = 0.08, 16                                       # drawn delay (ms) and shift (MHz), enlarged
    o.append(P([(fx(d), fy(s / 4)), (fx(1 + d), fy(150 + s / 4)), (fx(2), fy(150 * d + s / 4))], LV, 2.5, '7 5'))
    o.append(T(fx(0.52), fy(118), 'sent', 14, 'end', fill=AC, bold=True))
    o.append(T(fx(0.62), fy(66), 'echo', 14, 'start', fill=LV, bold=True))
    o.append(T(fx(0.5), fy(30), 'delay 2R/c = 0.4 µs and the Doppler', 13, 'start', fill=MUT))
    o.append(T(fx(0.5), fy(12), 'shift are drawn enlarged', 13, 'start', fill=MUT))
    # bottom: beat frequency, to scale
    yc, yd = 230, 380                                    # 80 kHz .. 0
    gy = lambda f: yd - f / 80 * (yd - yc)
    o.append(L(x0, yd, x1, yd, L2, 1.5)); o.append(L(x0, yc - 6, x0, yd, L2, 1.5))
    for f in (0, 20, 40, 60, 80):
        o += [L(x0 - 5, gy(f), x0, gy(f), L2, 1.5), L(x0, gy(f), x1, gy(f), LN, 1), T(x0 - 9, gy(f) + 4.5, str(f), 13, 'end', MUT)]
    o.append(T(x0, yc - 18, 'beat frequency (kHz)', 14, 'start', MUT))
    for t in (0, 1, 2):
        o += [L(fx(t), yd, fx(t), yd + 5, L2, 1.5), T(fx(t), yd + 20, str(t), 13, fill=MUT)]
    o.append(T((x0 + x1) / 2, yd + 40, 'time (ms)', 14, fill=MUT))
    o.append(L(fx(0.03), gy(49.73), fx(0.98), gy(49.73), LV, 4))
    o.append(L(fx(1.03), gy(70.27), fx(1.98), gy(70.27), LV, 4))
    o.append(L(x0, gy(60), x1, gy(60), AC, 2, '7 5'))
    o.append(Tb(fx(0.5), gy(49.73) + 22, 'up-sweep: f' + sub('R') + ' − f' + sub('d') + ' = 49.73', 13, fill=LV, bold=True))
    o.append(Tb(fx(1.5), gy(70.27) - 10, 'down-sweep: f' + sub('R') + ' + f' + sub('d') + ' = 70.27', 13, fill=LV, bold=True))
    o.append(Tb(fx(1.5), gy(60) + 18, 'f' + sub('R') + ' = 60 kHz → R = 60 m', 13, fill=AC, bold=True))
    return 432, ''.join(o)

FIG[5] = (f5, 'Top: the transmitted triangle sweeps 150 MHz up in 1 ms and back down; the echo returns late (enlarged here) and shifted by the Doppler. Bottom, to scale: the beat is 49.73 kHz on the up-sweep and 70.27 kHz on the down-sweep; their mean, 60 kHz, gives 60 m and half their gap, 10.27 kHz, gives 20 m/s.',
          'Top graph: a solid triangle wave of transmit frequency rising 150 megahertz in 1 millisecond and falling back, with a dashed echo copy slightly later. Bottom graph: beat frequency against time, a level line at 49.73 kilohertz during the first millisecond and at 70.27 kilohertz during the second, with a dashed line at 60 kilohertz for the range part.')


# ---- 6.6 canceller response against speed at two PRFs ----
def f6():
    x0, x1, y0, y1 = 80, 620, 40, 270
    fx = lambda v: x0 + v / 80 * (x1 - x0)
    fy = lambda h: y1 - h / 2.2 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [0, 15, 30, 45, 60, 75], [0, 1, 2], fx, fy, 'radial speed v (m/s), λ = 3 cm', 'canceller output |H|')]
    for prf, c, dash in ((1000, AC, None), (1250, NX, '7 5')):
        pts = [(fx(v), fy(2 * abs(math.sin(math.pi * (2 * v / 0.03) / prf)))) for v in [i * 0.2 for i in range(401)]]
        o.append(P(pts, c, 2.5, dash))
    o.append(C(fx(15), fy(1.176), 6, NX)); o.append(C(fx(75), fy(0), 7, LV))
    ly0 = y1 + 66
    o.append(L(x0, ly0 - 5, x0 + 34, ly0 - 5, AC, 2.5)); o.append(T(x0 + 42, ly0, 'PRF 1000 Hz: blind every 15 m/s', 13, 'start', fill=AC, bold=True))
    o.append(L(x0 + 300, ly0 - 5, x0 + 334, ly0 - 5, NX, 2.5, '7 5')); o.append(T(x0 + 342, ly0, 'PRF 1250 Hz: blind every 18.75 m/s', 13, 'start', fill=NX, bold=True))
    o.append(C(x0 + 17, ly0 + 19, 6, NX)); o.append(T(x0 + 42, ly0 + 24, '15 m/s: zero at 1000 Hz, but 1.18 at 1250 Hz', 13, 'start', fill=NX))
    o.append(C(x0 + 317, ly0 + 19, 6, LV)); o.append(T(x0 + 342, ly0 + 24, '75 m/s: zero at both, the first', 13, 'start', fill=LV, bold=True))
    o.append(T(x0 + 342, ly0 + 42, 'staggered blind speed', 13, 'start', fill=LV, bold=True))
    return 390, ''.join(o)

FIG[6] = (f6, 'Single-canceller response 2|sin(πf<sub>d</sub>T<sub>r</sub>)| for the worked examples at λ = 3 cm. At 1000 Hz the blind speeds are 15, 30, 45 m/s and so on; at 1250 Hz they are 18.75, 37.5 m/s and so on. Staggering the two leaves 75 m/s as the first speed blind in both, and at 15 m/s the 1250 Hz interval still passes 1.18.',
          'Graph of canceller output from 0 to 2 against radial speed from 0 to 80 metres per second. A solid sine-arch curve for 1000 hertz touches zero at 15, 30, 45, 60 and 75; a dashed curve for 1250 hertz touches zero at 18.75, 37.5, 56.25 and 75. A point marks 1.18 on the dashed curve at 15, and another marks the common zero at 75.')


# ---- 6.7 monopulse horns, comparator and the error curve ----
def f7():
    o = []
    hx, hy, s = 24, 70, 54
    for (lab, i, j) in (('A', 0, 0), ('C', 1, 0), ('B', 0, 1), ('D', 1, 1)):
        o.append(boxt(hx + i * (s + 6), hy + j * (s + 6), s, s, [lab], ACS, AC, 18, bold_first=True))
    o.append(T(hx + s + 3, hy - 14, 'four horns, from behind', 13, fill=MUT))
    cx = 176
    o.append(boxt(cx, 66, 112, 122, ['Comparator', 'magic tees'], PANEL, AC, 13, bold_first=True))
    o.append(arrow(hx + 2 * s + 6, hy + s / 2, cx - 4, hy + s / 2))
    o.append(arrow(hx + 2 * s + 6, hy + s + 6 + s / 2, cx - 4, hy + s + 6 + s / 2))
    outs = [('Σ = A+B+C+D', 86), ('Δaz = (A+B)−(C+D)', 127), ('Δel = (A+C)−(B+D)', 168)]
    for lab, y in outs:
        o.append(arrow(cx + 112, y, cx + 128, y))
    o.append(T(cx + 132, 90, 'Σ', 14, 'start', bold=True))
    o.append(T(cx + 132, 131, 'Δ' + sub('az'), 14, 'start', bold=True))
    o.append(T(cx + 132, 172, 'Δ' + sub('el'), 14, 'start', bold=True))
    o.append(T(24, 236, 'Σ = A + B + C + D', 13, 'start'))
    o.append(T(24, 256, 'Δ' + sub('az') + ' = (A + B) − (C + D)', 13, 'start'))
    o.append(T(24, 276, 'Δ' + sub('el') + ' = (A + C) − (B + D)', 13, 'start'))
    # error curve
    x0, x1, y0, y1 = 400, 690, 50, 290
    fx = lambda th: x0 + (th + 0.2) / 0.4 * (x1 - x0)
    fy = lambda r: (y0 + y1) / 2 - r / 0.4 * (y1 - y0) / 2
    o.append(L(x0, fy(0), x1, fy(0), L2, 1.5)); o.append(L(fx(0), y0, fx(0), y1, L2, 1.5))
    for th in (-0.2, -0.1, 0.1, 0.2):
        o += [L(fx(th), fy(0), fx(th), fy(0) + 5, L2, 1.5), T(fx(th), fy(0) + 20, neg(f'{th:g}'), 13, fill=MUT)]
    for r in (-0.36, 0.36):
        o += [L(fx(0) - 5, fy(r), fx(0), fy(r), L2, 1.5)]
    o.append(T(fx(0) - 8, fy(0.36) + 4, '0.36', 13, 'end', MUT)); o.append(T(fx(0) - 8, fy(-0.36) + 4, neg('-0.36'), 13, 'end', MUT))
    o.append(T(fx(0) + 8, y0 - 12, 'Δ/Σ', 14, 'start', MUT))
    o.append(T((x0 + x1) / 2, y1 + 28, 'θ off boresight (degrees)', 14, fill=MUT))
    o.append(L(fx(-0.2), fy(-0.36), fx(0.2), fy(0.36), AC, 3))
    th = 0.12 / 1.8
    o.append(L(fx(th), fy(0), fx(th), fy(0.12), LV, 1.5, '3 4')); o.append(L(fx(0), fy(0.12), fx(th), fy(0.12), LV, 1.5, '3 4'))
    o.append(C(fx(th), fy(0.12), 6, LV))
    o.append(Tb(fx(th) + 10, fy(0.12) + 4, '0.12 → 0.0667°', 13, 'start', fill=LV, bold=True))
    o.append(T(fx(0.13), fy(-0.2), 'slope k = 1.8 per degree', 13, fill=AC, bold=True))
    return 330, ''.join(o)

FIG[7] = (f7, 'Four squinted horns feed a comparator that forms the sum and two differences on the same pulse. The error Δ/Σ grows in proportion to the angle off boresight; the worked example\'s 0.12 at a slope of 1.8 per degree is 0.0667°.',
          'Left: a two by two block of horns, A and C on top, B and D below, feeding a comparator box with three outputs, sum, azimuth difference and elevation difference, with their formulas below. Right: a straight line of difference over sum against angle from minus 0.2 to 0.2 degrees, passing through zero at boresight; a point marks 0.12 at 0.0667 degrees.')


# ---- 6.8 cell-averaging CFAR window ----
def f8():
    o = []
    w, x0, y = 32, 56, 60
    kinds = ['t'] * 8 + ['g', 'c', 'g'] + ['t'] * 8
    for i, kd in enumerate(kinds):
        fill, st = {'t': (PANEL, AC), 'g': ('none', L2), 'c': (LVS, LV)}[kd]
        o.append(R(x0 + i * w, y, w - 4, 44, fill, st, 4, 2, '4 3' if kd == 'g' else None))
    o.append(T(x0 + 9 * w + 14, y + 27, 'CUT', 12, fill=LV, bold=True))
    o.append(brace(x0, x0 + 8 * w - 4, y + 56, AC))
    o.append(brace(x0 + 11 * w, x0 + 19 * w - 4, y + 56, AC))
    o.append(T(x0 + 4 * w, y + 82, '8 training cells', 13, fill=AC, bold=True))
    o.append(T(x0 + 15 * w, y + 82, '8 training cells', 13, fill=AC, bold=True))
    o.append(T(x0 + 9.5 * w, y - 12, 'guard · cell under test · guard', 13, fill=MUT))
    o.append(T(x0, y - 12, 'range cells →', 13, 'start', fill=MUT))
    # processing chain
    by = 196
    o.append(boxt(150, by, 170, 56, ['Average of N = 16', 'training cells: Z'], PANEL, AC, 13, bold_first=True))
    o.append(boxt(360, by, 110, 56, ['× α = 12.45', 'threshold αZ'], ACS, AC, 13, bold_first=True))
    o.append(boxt(510, by, 170, 56, ['Compare', 'CUT > αZ → target'], LVS, LV, 13, bold_first=True))
    o.append(arrow(x0 + 4 * w, y + 90, 210, by - 4)); o.append(arrow(x0 + 15 * w, y + 90, 270, by - 4))
    o.append(arrow(320, by + 28, 356, by + 28)); o.append(arrow(470, by + 28, 506, by + 28))
    o.append(P([(x0 + 9.5 * w, y + 48), (x0 + 9.5 * w, 150), (640, 150), (640, by - 4)], LV, 2))
    o.append(f'<polygon points="635,{by - 9} 640,{by - 1} 645,{by - 9}" style="fill:{LV}"/>')
    o.append(T(360, 292, 'P' + sub('fa') + ' = (1 + α/16)' + sup('−16') + ' = 10⁻⁴  gives  α = 16(10' + sup('4/16') + ' − 1) = 12.45', 14, bold=True, fill=AC))
    return 312, ''.join(o)

FIG[8] = (f8, 'A cell-averaging CFAR window as in the second worked example: 8 training cells on each side of the cell under test, with one guard cell either side kept out of the average. Their mean Z times α = 12.45 is the threshold that holds P<sub>fa</sub> at 10⁻⁴ whatever the background.',
          'A row of 19 range cells: 8 training cells, a dashed guard cell, the cell under test, a guard cell and 8 more training cells. Arrows from both groups of training cells go to an averaging box, then to a box multiplying by alpha equals 12.45, then to a comparator that also receives the cell under test. The formula at the bottom gives alpha from the false alarm probability.')


# ---- 6.9 duplexer and the power levels it separates ----
def f9():
    o = []
    o.append(boxt(16, 40, 150, 58, ['Transmitter', '100 kW = +80 dBm'], PANEL, AC, 13, bold_first=True))
    o.append(f'<circle cx="262" cy="69" r="34" style="fill:{ACS};stroke:{AC};stroke-width:2"/>')
    o.append(T(262, 66, 'duplexer', 13, bold=True)); o.append(T(262, 83, '70 dB', 13, fill=AC, bold=True))
    o.append(arrow(166, 69, 224, 69))
    o.append(arrow(296, 69, 352, 69))
    o.append(f'<path d="M376,36 Q350,69 376,102" style="fill:none;stroke:{AC};stroke-width:3"/>')
    o.append(T(380, 124, 'Antenna', 13, bold=True))
    o.append(arrow(262, 103, 262, 150, LV, 2, 'l'))
    o.append(boxt(192, 154, 140, 46, ['Limiter'], PANEL, LV, 13, bold_first=True))
    o.append(arrow(262, 200, 262, 236, LV, 2, 'l'))
    o.append(boxt(172, 240, 180, 58, ['Receiver', 'safe up to 10 mW'], LVS, LV, 13, bold_first=True))
    o.append(T(272, 128, 'leakage', 13, 'start', fill=LV))
    o.append(T(16, 336, 'Isolation = 10 log₁₀(10⁵ W ÷ 10⁻² W) = 70 dB', 14, 'start', bold=True, fill=AC))
    # level ladder
    x0, y0, y1 = 470, 40, 320
    fy = lambda d: y0 + (90 - d) / 200 * (y1 - y0)        # +90 .. -110 dBm
    o.append(L(x0, fy(90), x0, fy(-110), L2, 1.5))
    for d in (80, 40, 0, -40, -80):
        o += [L(x0 - 5, fy(d), x0, fy(d), L2, 1.5), T(x0 - 9, fy(d) + 4.5, ('+' if d > 0 else '') + neg(d), 13, 'end', MUT)]
    o.append(T(x0 - 40, y0 - 16, 'level (dBm)', 14, 'start', MUT))
    for d, lab, c in ((80, 'pulse +80 dBm', AC), (10, 'leak +10 dBm (after 70 dB)', LV), (-100, 'echo −100 dBm (10⁻¹³ W)', NX)):
        o.append(L(x0, fy(d), x0 + 26, fy(d), c, 3)); o.append(T(x0 + 32, fy(d) + 5, lab, 13, 'start', fill=c, bold=True))
    o.append(L(x0 + 14, fy(80) + 6, x0 + 14, fy(10) - 6, AC, 1.5, None, 'n'))
    return 352, ''.join(o)

FIG[9] = (f9, 'The first worked example\'s duplexer: the 100 kW (+80 dBm) pulse goes to the antenna, and only +10 dBm, the 10 mW the receiver can take, may leak through, so it must isolate by 70 dB, with a limiter for the spike. On the right, the same levels against a typical echo of −100 dBm.',
          'Left: a transmitter box at 100 kilowatts feeds a duplexer circle marked 70 dB, which feeds a dish antenna; a leakage path goes down through a limiter to a receiver safe up to 10 milliwatts. Right: a vertical scale in dBm marks the pulse at plus 80, the leakage after 70 dB at plus 10 and a typical echo at minus 100.')

spec = make_spec(FIG)
