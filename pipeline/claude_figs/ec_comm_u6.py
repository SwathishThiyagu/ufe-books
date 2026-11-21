"""Claude's hand-drawn figures for ec-comm-u6 (Analog and Digital Communication: digital passband modulation), one per
chapter, drawn from each chapter's own worked example and numbers. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
R2 = math.radians


def sub(base, s, size=13):
    """base with a subscript, as SVG tspans (13 px subscript text keeps labels readable)"""
    return f'{base}<tspan dy="4" font-size="{size - 2}">{s}</tspan><tspan dy="-4"> </tspan>'


def curve(f, t0, t1, fx, fy, n=400, c=AC, w=2.2, dash=None):
    pts = [(fx(t0 + (t1 - t0) * i / n), fy(f(t0 + (t1 - t0) * i / n))) for i in range(n + 1)]
    return P(pts, c, w, dash)


# ---- 6.1 OOK and BFSK waveforms for the worked example ----
def f1():
    o = []
    bits = [1, 0, 1, 1, 0]
    x0, x1 = 130, 700; bw = (x1 - x0) / 5
    fx = lambda t: x0 + t * bw            # t in bit times
    rows = [('data', 62, 22), ('OOK', 150, 34), ('BFSK', 250, 34)]
    for i, b in enumerate(bits):
        o.append(T(fx(i + 0.5), 26, str(b), 15, fill=AC, bold=True))
        if i: o.append(L(fx(i), 34, fx(i), 296, LN, 1, '3 4'))
    # data NRZ
    yd = lambda v: 80 - v * 34
    pts = []
    for i, b in enumerate(bits): pts += [(fx(i), yd(b)), (fx(i + 1), yd(b))]
    o.append(P(pts, INK, 2.4))
    o.append(T(120, 52, 'data', 14, 'end', MUT)); o.append(T(120, 70, '1 / 0', 13, 'end', MUT))
    # OOK: 3 cycles per bit on 1s
    yo = lambda v: 150 - v * 32
    o.append(L(x0, 150, x1, 150, L2, 1))
    o.append(curve(lambda t: (bits[min(int(t), 4)]) * math.sin(2 * math.pi * 3 * t), 0, 5, fx, yo, 900, AC, 2))
    o.append(T(120, 146, 'OOK', 14, 'end', AC, bold=True)); o.append(T(120, 164, '30 kHz', 13, 'end', MUT))
    # BFSK: 3 cycles for 1 (30 kHz), 2 cycles for 0 (20 kHz); whole cycles keep the phase continuous
    yf = lambda v: 250 - v * 32
    o.append(L(x0, 250, x1, 250, L2, 1))
    o.append(curve(lambda t: math.sin(2 * math.pi * (3 if bits[min(int(t), 4)] else 2) * (t - int(min(t, 4.9999)))), 0, 5, fx, yf, 900, LV, 2))
    o.append(T(120, 246, 'BFSK', 14, 'end', LV, bold=True)); o.append(T(120, 264, '30 / 20 kHz', 13, 'end', MUT))
    for i, b in enumerate(bits):
        o.append(T(fx(i + 0.5), 302, ('3 cycles' if b else '2 cycles'), 13, fill=MUT))
    o.append(xaxis(x0, x1, 318, [0, 1, 2, 3, 4, 5], fx, 'time (µs), T' + '<tspan dy="4" font-size="11">b</tspan><tspan dy="-4"> = 100 µs</tspan>', fmt=lambda v: str(v * 100)))
    return 372, ''.join(o)

FIG[1] = (f1, 'The worked example’s bits 1 0 1 1 0 at 10 kb/s. OOK sends 3 cycles of a 30 kHz carrier for each 1 and nothing for each 0; '
              'BFSK sends 3 cycles (30 kHz) for a 1 and 2 cycles (20 kHz) for a 0, so its envelope never changes.',
          'Three rows against time from 0 to 500 microseconds: the data 1 0 1 1 0 as a square wave, the OOK waveform with bursts only in the 1 bits, and the BFSK waveform with three cycles in each 1 bit and two cycles in each 0 bit.')


# ---- 6.2 BPSK waveform and the correlator output ----
def f2():
    o = []
    bits = [1, 0, 1, 1, 0]
    x0, x1 = 130, 700; bw = (x1 - x0) / 5
    fx = lambda t: x0 + t * bw
    for i, b in enumerate(bits):
        o.append(T(fx(i + 0.5), 24, str(b), 15, fill=AC, bold=True))
        if i: o.append(L(fx(i), 32, fx(i), 330, LN, 1, '3 4'))
    # BPSK: 2 cycles per bit (drawn), sign from the bit
    yb = lambda v: 88 - v * 40
    o.append(L(x0, 88, x1, 88, L2, 1))
    sg = lambda t: 1 if bits[min(int(t), 4)] else -1
    o.append(curve(lambda t: sg(t) * math.cos(2 * math.pi * 2 * t), 0, 5, fx, yb, 900, AC, 2.2))
    o.append(T(120, 84, 'BPSK', 14, 'end', AC, bold=True)); o.append(T(120, 102, 's(t)', 13, 'end', MUT))
    for i in range(1, 5):
        if bits[i] != bits[i - 1]:
            o.append(Tb(fx(i), 146, '180° flip', 13, 'middle', NX))
    # correlator output: ramps to +-sqrt(Eb) in each bit, dumped at the end
    y0 = 250; amp = 70
    yc = lambda v: y0 - v * amp
    o.append(L(x0, y0, x1, y0, INK, 1.6, '7 5'))
    o.append(T(fx(2.5), y0 + 20, 'threshold 0', 13, 'middle', INK))
    for i, b in enumerate(bits):
        sgn = 1 if b else -1
        f = lambda t, i=i, sgn=sgn: sgn * ((t - i) + math.sin(4 * math.pi * 2 * (t - i)) / (4 * math.pi * 2))
        o.append(curve(f, i, i + 1, fx, yc, 120, LV, 2.4))
        o.append(C(fx(i + 1) - 1, yc(sgn), 5.5, NX))
        o.append(T(fx(i + 1) - 10, yc(sgn) + (-10 if b else 22), ('+√E' if b else '−√E') + '<tspan dy="4" font-size="11">b</tspan>', 13, 'end', NX))
    o.append(T(120, 246, 'correlator', 14, 'end', LV, bold=True)); o.append(T(120, 264, 'output y', 13, 'end', MUT))
    o.append(xaxis(x0, x1, 336, [0, 1, 2, 3, 4, 5], fx, 'time in bit periods T' + '<tspan dy="4" font-size="11">b</tspan><tspan dy="-4">  (dots: samples at the bit ends; sign of y gives the bit)</tspan>'))
    return 388, ''.join(o)

FIG[2] = (f2, 'BPSK for the bits 1 0 1 1 0 (carrier drawn with 2 cycles per bit). The carrier flips by 180° whenever the bit changes. '
              'The correlator output ramps up to +√E_b during a 1 and down to −√E_b during a 0; the sample at each bit end is compared with 0.',
          'Top: a BPSK waveform whose phase reverses at each change of bit. Bottom: the integrator output ramping to plus or minus root E b in each bit, with sample dots at the bit ends above or below a dashed zero threshold.')



EBN0 = 'E<tspan dy="4" font-size="11">b</tspan><tspan dy="-4">/N</tspan><tspan dy="4" font-size="11">0</tspan><tspan dy="-4"> (dB)</tspan>'


def Qf(x):
    return 0.5 * math.erfc(x / math.sqrt(2))


def logplot(curves, x0, x1, y0, y1, xr, yr, xlab, ylab, xt, marks=()):
    """curves: [(fn(xdB)->P, colour, dash, label, label_x, dy)] on a log10 y axis from 10^yr[0] down to 10^yr[1]"""
    o = []
    fx = lambda v: x0 + (v - xr[0]) / (xr[1] - xr[0]) * (x1 - x0)
    fy = lambda p: y0 + (yr[0] - math.log10(p)) / (yr[0] - yr[1]) * (y1 - y0)
    yt = list(range(yr[0], yr[1] - 1, -1))
    o.append(axes(x0, x1, y0, y1, xt, [10.0 ** e for e in yt], fx, fy, xlab, ylab,
                  yfmt=lambda p: '10<tspan dy="-6" font-size="11">' + neg(int(round(math.log10(p)))) + '</tspan>'))
    for fn, col, dash, lab, lx, dy in curves:
        pts = []
        for i in range(301):
            v = xr[0] + (xr[1] - xr[0]) * i / 300
            pv = fn(v)
            if pv < 10.0 ** yr[1]: break
            if pv > 10.0 ** yr[0]: continue
            pts.append((fx(v), fy(pv)))
        o.append(P(pts, col, 2.6, dash))
        o.append(Tb(fx(lx), fy(fn(lx)) + dy, lab, 13, 'start', col, bold=True))
    for v, pv, col in marks:
        o.append(C(fx(v), fy(pv), 5, col))
    return o, fx, fy


# ---- 6.3 error probability of the four binary receivers ----
def f3():
    lin = lambda d: 10 ** (d / 10)
    cs = [(lambda d: Qf(math.sqrt(2 * lin(d))), AC, None, 'coherent BPSK', 7.0, -8),
          (lambda d: 0.5 * math.exp(-lin(d)), LV, '8 5', 'DPSK', 11.25, -6),
          (lambda d: Qf(math.sqrt(lin(d))), NX, None, 'coherent BFSK', 12.2, -12),
          (lambda d: 0.5 * math.exp(-lin(d) / 2), INK, '3 4', 'non-coherent BFSK', 4.6, -12)]
    o, fx, fy = logplot(cs, 90, 690, 40, 330, (0, 14), (-1, -7), EBN0,
                        'bit error probability', [0, 2, 4, 6, 8, 10, 12, 14])
    o.append(L(fx(10), 40, fx(10), 330, L2, 1.4, '5 4'))
    for pv, col in ((3.87e-6, AC), (2.27e-5, LV), (7.83e-4, NX), (3.37e-3, INK)):
        o.append(C(fx(10), fy(pv), 5, col))
    o.append(Tb(fx(10) + 8, fy(3.37e-3) - 8, '3.37 × 10⁻³', 13, 'start', INK))
    o.append(Tb(fx(10) + 8, fy(7.83e-4) + 4, '7.83 × 10⁻⁴', 13, 'start', NX))
    o.append(Tb(fx(10) + 8, fy(2.27e-5) + 4, '2.27 × 10⁻⁵', 13, 'start', LV))
    o.append(Tb(fx(10) - 8, fy(3.87e-6) + 4, '3.87 × 10⁻⁶', 13, 'end', AC))
    return 384, ''.join(o)

FIG[3] = (f3, 'Bit error probability against E_b/N_0 for the four binary receivers. At 10 dB (dashed line, the second worked example) the order is '
              'BPSK, DPSK, coherent BFSK, non-coherent BFSK; DPSK and non-coherent BFSK each sit less than 1 dB to the right of their coherent partners.',
          'Four falling curves of bit error probability on a log scale from 0.1 to 10 to the minus 7 against Eb over N0 from 0 to 14 dB, with the values at 10 dB marked: BPSK 3.87e-6, DPSK 2.27e-5, coherent BFSK 7.83e-4, non-coherent BFSK 3.37e-3.')



# ---- 6.4 QPSK and 8-PSK constellations with Gray labels ----
def f4():
    o = []
    def panel(cx, cy, r, phases, labels, title, dlab, bounds):
        q = []
        q.append(L(cx - r - 40, cy, cx + r + 50, cy, L2, 1.4)); q.append(L(cx, cy + r + 40, cx, cy - r - 50, L2, 1.4))
        q.append(T(cx + r + 52, cy - 8, 'I', 14, 'end', MUT)); q.append(T(cx + 12, cy - r - 42, 'Q', 14, 'start', MUT))
        q.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" style="fill:none;stroke:var(--line2);stroke-width:1.2;stroke-dasharray:4 4"/>')
        for a in bounds:
            q.append(L(cx, cy, cx + (r + 34) * math.cos(R2(a)), cy - (r + 34) * math.sin(R2(a)), NX, 1.3, '6 4'))
        pts = [(cx + r * math.cos(R2(a)), cy - r * math.sin(R2(a))) for a in phases]
        # neighbour distance on the first pair
        (xa, ya), (xb, yb) = pts[0], pts[1]
        q.append(L(xa, ya, xb, yb, LV, 2.4))
        mx, my = (xa + xb) / 2, (ya + yb) / 2
        q.append(Tb(mx - 8, my - 4, dlab, 13, 'end', LV, bold=True))
        for (x, y), a, lab in zip(pts, phases, labels):
            q.append(C(x, y, 7, AC))
            lx, ly = cx + (r + 26) * math.cos(R2(a)), cy - (r + 26) * math.sin(R2(a)) + 5
            q.append(T(lx, ly, lab, 14, 'middle', INK, bold=True))
        q.append(T(cx, cy + r + 66, title, 14, 'middle', INK, bold=True))
        return q
    o += panel(180, 182, 105, [45, 135, 225, 315], ['11', '01', '00', '10'], 'QPSK: d = 1.414√E' + '<tspan dy="4" font-size="11">s</tspan>', 'd', [0, 90, 180, 270])
    o += panel(540, 182, 105, [0, 45, 90, 135, 180, 225, 270, 315], ['000', '001', '011', '010', '110', '111', '101', '100'],
               '8-PSK: d = 0.765√E' + '<tspan dy="4" font-size="11">s</tspan>', 'd', [22.5 + 45 * i for i in range(8)])
    o.append(T(360, 382, 'dashed lines: decision boundaries', 13, 'middle', MUT))
    return 396, ''.join(o)

FIG[4] = (f4, 'QPSK and 8-PSK on circles of the same symbol energy, with Gray labels: neighbours differ in one bit. '
              'The neighbour distance d falls from 1.414√E_s to 0.765√E_s, which is why 8-PSK needs more power for the same error rate.',
          'Left: four QPSK points at 45, 135, 225 and 315 degrees labelled 11, 01, 00, 10, with the I and Q axes as boundaries. Right: eight 8-PSK points labelled 000, 001, 011, 010, 110, 111, 101, 100 counterclockwise from 0 degrees, with boundaries between them. A short line between two neighbours marks the distance d in each.')



# ---- 6.5 16-QAM with Gray labels and the receiver's thresholds ----
def f5():
    o = []
    cx, cy, u = 330, 200, 40          # u pixels per a
    gx = lambda v: cx + v * u; gy = lambda v: cy - v * u
    gray = {-3: '00', -1: '01', 1: '11', 3: '10'}
    o.append(L(gx(-4.6), cy, gx(4.6), cy, L2, 1.4)); o.append(L(cx, gy(-4.4), cx, gy(4.4), L2, 1.4))
    o.append(T(gx(4.6), cy - 8, 'I', 14, 'end', MUT)); o.append(T(cx + 10, gy(4.4) + 4, 'Q', 14, 'start', MUT))
    for t in (-2, 0, 2):
        o.append(L(gx(t), gy(4.1), gx(t), gy(-4.1), NX, 1.3, '6 4'))
        o.append(L(gx(-4.1), gy(t), gx(4.1), gy(t), NX, 1.3, '6 4'))
    for v in (-3, -1, 1, 3):
        o.append(T(gx(v), gy(-4.1) + 20, f'{v:+d}a'.replace('+1a', '+a').replace('-1a', '−a').replace('-', '−'), 13, 'middle', MUT))
        o.append(T(gx(-4.1) - 8, gy(v) + 5, f'{v:+d}a'.replace('+1a', '+a').replace('-1a', '−a').replace('-', '−'), 13, 'end', MUT))
    for i in (-3, -1, 1, 3):
        for q in (-3, -1, 1, 3):
            hot = (i, q) == (3, 1)
            o.append(C(gx(i), gy(q), 7.5 if hot else 6, LV if hot else AC))
            o.append(T(gx(i), gy(q) - 11, gray[i] + gray[q], 13, 'middle', LV if hot else INK, bold=hot))
    # side notes
    o.append(T(560, 70, 'bits 1011', 14, 'start', LV, bold=True))
    o.append(T(560, 90, 'I bits 10 → +3a', 13, 'start', INK))
    o.append(T(560, 108, 'Q bits 11 → +a', 13, 'start', INK))
    o.append(L(556, 116, gx(3) + 14, gy(1) - 2, LV, 1.5, arrow='l'))
    o.append(T(560, 230, 'thresholds', 14, 'start', NX, bold=True))
    o.append(T(560, 250, 'at −2a, 0, +2a', 13, 'start', INK))
    o.append(T(560, 268, 'on each axis', 13, 'start', INK))
    o.append(T(560, 310, 'E', 13, 'start', MUT) .replace('>E<', '>E<tspan dy="4" font-size="11">s</tspan><tspan dy="-4"> = 10a²</tspan><'))
    return 410, ''.join(o)

FIG[5] = (f5, 'Gray-labelled 16-QAM: the first two bits set I and the last two set Q, so grid neighbours differ in one bit. '
              'The worked example’s bits 1011 go to the point (3a, a); the dashed lines at −2a, 0 and +2a are the receiver’s thresholds.',
          'A 4 by 4 grid of points at plus or minus a and 3a on the I and Q axes, each labelled with four bits, with dashed threshold lines at minus 2a, 0 and 2a on both axes. The point at I = 3a, Q = a, labelled 1011, is highlighted.')



# ---- 6.6 MSK phase trellis for the worked example ----
def f6():
    o = []
    bits = [1, 1, 0, 1, 0, 0, 1]
    x0, x1, yT, yB = 110, 690, 70, 320
    fx = lambda n: x0 + n * (x1 - x0) / 7
    fy = lambda d: yT + (270 - d) / 450 * (yB - yT)      # -180 .. 270 degrees
    for d in (-180, -90, 0, 90, 180, 270):
        o.append(L(x0, fy(d), x1, fy(d), LN, 1))
        o.append(T(x0 - 10, fy(d) + 5, neg(d) + '°', 13, 'end', MUT))
    # all possible paths, faint
    for n in range(7):
        for d in range(-90 * n, 90 * n + 1, 180):
            for e in (d + 90, d - 90):
                if -180 <= d <= 270 and -180 <= e <= 270:
                    o.append(L(fx(n), fy(d), fx(n + 1), fy(e), L2, 1.2, '4 4'))
    th = [0]
    for b in bits: th.append(th[-1] + (90 if b else -90))
    o.append(P([(fx(n), fy(d)) for n, d in enumerate(th)], AC, 3.4))
    for n, d in enumerate(th):
        o.append(C(fx(n), fy(d), 5.5, AC))
        if n:
            o.append(Tb(fx(n), fy(d) + (-12 if d >= th[n - 1] else 22), f'{d}°', 13, 'middle', AC, True))
    for n, b in enumerate(bits):
        o.append(T(fx(n + 0.5), 36, str(b), 15, 'middle', LV, True))
        o.append(T(fx(n + 0.5), 56, '1.025' if b else '0.975', 13, 'middle', MUT))
    o.append(T(x0 - 10, 36, 'bit', 13, 'end', LV)); o.append(T(x0 - 10, 56, 'f (MHz)', 13, 'end', MUT))
    o.append(xaxis(x0, x1, yB + 14, list(range(8)), fx, 'time (bit periods, T' + '<tspan dy="4" font-size="11">b</tspan><tspan dy="-4"> = 10 µs)</tspan>'))
    o.append(T(x1, yB - 8, 'phase θ(t)', 13, 'end', MUT))
    return 384, ''.join(o)

FIG[6] = (f6, 'The phase trellis of the worked example (R_b = 100 kb/s, f_c = 1 MHz). Each 1 sends 1.025 MHz and raises the phase by 90° in a straight ramp; '
              'each 0 sends 0.975 MHz and lowers it by 90°. The dashed lines are all the paths MSK could take; the phase never jumps.',
          'A grid of phase from minus 180 to 270 degrees against time in bit periods 0 to 7, with faint dashed lines for all possible plus or minus 90 degree steps. The highlighted path for bits 1 1 0 1 0 0 1 goes 0, 90, 180, 90, 180, 90, 0, 90 degrees.')



# ---- 6.7 power spectral densities of BPSK, QPSK and MSK at the same bit rate ----
def f7():
    o = []
    x0, x1, y0, y1 = 90, 690, 40, 320
    fx = lambda f: x0 + f / 3 * (x1 - x0)
    fy = lambda d: y0 + (5 - d) / 55 * (y1 - y0)
    sinc = lambda x: 1.0 if abs(x) < 1e-9 else math.sin(math.pi * x) / (math.pi * x)
    def msk(f):
        den = 16 * f * f - 1
        if abs(den) < 1e-6: f += 1e-4; den = 16 * f * f - 1
        return 32 / math.pi ** 2 * (math.cos(2 * math.pi * f) / den) ** 2
    curves = [(lambda f: 2 * sinc(f) ** 2, AC, None, 'BPSK'), (lambda f: 4 * sinc(2 * f) ** 2, NX, '8 5', 'QPSK'), (msk, LV, None, 'MSK')]
    o.append(axes(x0, x1, y0, y1, [0, 0.5, 0.75, 1, 1.5, 2, 2.5, 3], [0, -10, -20, -30, -40, -50], fx, fy,
                  '(f − f' + '<tspan dy="4" font-size="11">c</tspan><tspan dy="-4">) T</tspan><tspan dy="4" font-size="11">b</tspan><tspan dy="-4">   (frequency from the carrier, in multiples of R</tspan><tspan dy="4" font-size="11">b</tspan><tspan dy="-4">)</tspan>',
                  'PSD relative to the BPSK peak (dB)', xfmt=lambda v: f'{v:g}', yfmt=neg))
    for fn, col, dash, lab in curves:
        segs, cur = [], []
        for i in range(1201):
            f = 3 * i / 1200
            v = fn(f)
            d = 10 * math.log10(max(v / 2, 1e-12))
            if d < -50:
                if len(cur) > 1: segs.append(cur)
                cur = []; continue
            cur.append((fx(f), fy(d)))
        if len(cur) > 1: segs.append(cur)
        for sg in segs: o.append(P(sg, col, 2.4, dash))
    o.append(Tb(fx(0.2), fy(4.2), 'QPSK', 13, 'start', NX, True))
    o.append(Tb(fx(0.36), fy(-3.5), 'MSK', 13, 'start', LV, True))
    o.append(Tb(fx(0.6), fy(-7.5), 'BPSK', 13, 'start', AC, True))
    o.append(Tb(fx(1.43), fy(-9.5), 'BPSK side lobe −13.3 dB', 13, 'start', AC))
    o.append(T(fx(1.75), fy(1), 'MSK side lobes start 23 dB below', 13, 'start', LV))
    o.append(T(fx(1.75), fy(-2.6), 'its own peak and fall as 1/f⁴', 13, 'start', LV))
    o.append(C(fx(2.5), fy(-17.9), 5, AC)); o.append(C(fx(2.5), fy(-37.8), 5, LV))
    o.append(Tb(fx(2.5) + 8, fy(-37.8) + 18, '−37.8 dB at 2.5 R' + '<tspan dy="4" font-size="11">b</tspan>', 13, 'middle', LV))
    o.append(Tb(fx(2.5), fy(-17.9) - 10, '−17.9 dB', 13, 'middle', AC))
    return 384, ''.join(o)

FIG[7] = (f7, 'Power spectral densities at the same bit rate and E_b, against frequency from the carrier. QPSK has the narrowest main lobe (first null at 0.5R_b, so R_b null to null), '
              'MSK’s first null is at 0.75R_b, BPSK’s at R_b; but MSK’s side lobes are far lower, 37.8 dB down at 2.5R_b against 17.9 dB for BPSK (second worked example).',
          'Three curves in decibels from 5 to minus 50 against frequency offset from 0 to 3 bit rates: BPSK and QPSK sinc-squared curves with side lobes near minus 13 to minus 20 dB, and the MSK curve with a wider main lobe whose side lobes fall much faster. Points at 2.5 bit rates mark minus 17.9 dB for BPSK and minus 37.8 dB for MSK.')



# ---- 6.8 DSSS spreading with the 7-chip m-sequence ----
def f8():
    o = []
    code = [1, 1, 1, 0, 0, 1, 0]
    data = [1, 0]
    chips = code * 2
    x0, x1 = 140, 672; cw = (x1 - x0) / 14
    fx = lambda n: x0 + n * cw
    def row(vals, ymid, col, lab, sub_lab):
        q = [L(x0, ymid, x1, ymid, L2, 1)]
        yv = lambda v: ymid - (22 if v > 0 else -22)
        pts = []
        for n, v in enumerate(vals):
            pts += [(fx(n), yv(v)), (fx(n + 1), yv(v))]
        q.append(P(pts, col, 2.4))
        q.append(T(x0 - 12, ymid - 2, lab, 14, 'end', col, True)); q.append(T(x0 - 12, ymid + 16, sub_lab, 13, 'end', MUT))
        q.append(T(x1 + 6, ymid - 17, '+1', 13, 'start', MUT)); q.append(T(x1 + 6, ymid + 27, '−1', 13, 'start', MUT))
        return q
    d14 = [1] * 7 + [-1] * 7
    c14 = [1 if b else -1 for b in chips]
    o += row(d14, 70, INK, 'data d(t)', 'bits 1, 0')
    o += row(c14, 165, AC, 'code c(t)', '1110010 ×2')
    o += row([a * b for a, b in zip(d14, c14)], 260, LV, 'd(t)·c(t)', 'sent as BPSK')
    for n, b in enumerate(chips):
        o.append(T(fx(n + 0.5), 128, str(b), 13, 'middle', AC))
    for n in range(1, 14):
        o.append(L(fx(n), 40, fx(n), 290, LN, 1, '2 4'))
    o.append(L(fx(7), 34, fx(7), 296, INK, 1.6))
    o.append(T(fx(3.5), 28, 'bit 1: T' + '<tspan dy="4" font-size="11">b</tspan><tspan dy="-4"> = 7 T</tspan><tspan dy="4" font-size="11">c</tspan>', 13, 'middle', INK))
    o.append(T(fx(10.5), 28, 'bit 0', 13, 'middle', INK))
    o.append(T(406, 322, 'second bit: d = −1 inverts every chip; multiplying again by c(t) gives d(t) back, since c² = 1', 13, 'middle', MUT))
    return 336, ''.join(o)

FIG[8] = (f8, 'Spreading two data bits with the 7-chip m-sequence 1110010 from the shift-register table (G_p = 7 here, 128 in the worked example). '
              'The sent wave changes at the chip rate, so its spectrum is 7 times wider; the receiver multiplies by the same code to recover the bits.',
          'Three square waves over 14 chip periods: the data, plus 1 for 7 chips then minus 1 for 7 chips; the code 1110010 repeated twice; and their product, which equals the code in the first bit and the inverted code in the second.')



# ---- 6.9 OFDM: orthogonal subcarrier spectra and the cyclic prefix ----
def f9():
    o = []
    # top: five subcarrier spectra |sinc|, spacing 312.5 kHz
    x0, x1, yb, yt = 80, 680, 170, 40
    fx = lambda k: x0 + (k + 3) / 6 * (x1 - x0)          # k in subcarrier spacings, -3..3
    fy = lambda v: yb - v * (yb - yt)
    sinc = lambda x: 1.0 if abs(x) < 1e-9 else math.sin(math.pi * x) / (math.pi * x)
    cols = [L2, AC, NX, LV, L2]
    for i, c0 in enumerate(range(-2, 3)):
        pts = [(fx(-3 + 6 * j / 600), fy(abs(sinc(-3 + 6 * j / 600 - c0)) * 0.95)) for j in range(601)]
        o.append(P(pts, cols[i], 2.0 if c0 else 2.8, None if c0 in (-1, 0, 1) else '4 4'))
    o.append(L(x0, yb, x1, yb, L2, 1.4))
    for k in range(-3, 4):
        o.append(L(fx(k), yb, fx(k), yb + 5, L2, 1.4))
        o.append(T(fx(k), yb + 20, f'{k * 312.5:g}'.replace('-', '−'), 13, 'middle', MUT))
    o.append(L(fx(0), yt - 4, fx(0), yb, INK, 1.2, '3 3'))
    o.append(C(fx(0), fy(0.95), 5, NX)); o.append(C(fx(0), yb, 5, INK))
    o.append(Tb(fx(0) + 10, yt + 6, 'at this subcarrier’s centre the neighbours are zero', 13, 'start', INK))
    o.append(T(x1, yb + 38, 'frequency from subcarrier k (kHz), Δf = 312.5 kHz', 13, 'end', MUT))
    # bottom: one OFDM symbol with its prefix, and a delayed echo
    tx0, tx1 = 80, 680
    ft = lambda t: tx0 + (t + 1.0) / 5.4 * (tx1 - tx0)     # t in µs, -1.0 .. 4.4
    yA, h = 262, 34
    o.append(R(ft(-1.0), yA, ft(0) - ft(-1.0), h, PANEL, L2, 4, 1.5))
    o.append(T((ft(-1.0) + ft(0)) / 2, yA + 22, 'symbol k−1', 13, 'middle', MUT))
    o.append(R(ft(0), yA, ft(0.8) - ft(0), h, NXS, NX, 4, 2))
    o.append(T((ft(0) + ft(0.8)) / 2, yA + 22, 'CP 0.8 µs', 13, 'middle', NX, True))
    o.append(R(ft(0.8), yA, ft(4.0) - ft(0.8), h, ACS, AC, 4, 2))
    o.append(T((ft(0.8) + ft(4.0)) / 2, yA + 22, 'useful part T' + '<tspan dy="4" font-size="11">u</tspan><tspan dy="-4"> = 3.2 µs (FFT window)</tspan>', 13, 'middle', AC, True))
    # echo of the previous symbol, delayed by 0.6 us, ends inside the CP
    ye = yA + h + 12
    o.append(R(ft(-1.0 + 0.6), ye, ft(0.6) - ft(-0.4), 22, PANEL, L2, 4, 1.2, '4 3'))
    o.append(T((ft(-0.4) + ft(0.6)) / 2, ye + 16, 'echo of k−1', 13, 'middle', MUT))
    o.append(L(ft(0.6), ye + 22, ft(0.6), yA, LV, 2, '4 3'))
    o.append(T(ft(0.6) + 10, ye + 16, '0.6 µs late: it ends inside the CP, so the FFT window sees no ISI', 13, 'start', LV, True))
    o.append(xaxis(ft(-1.0), ft(4.4), 236, [-1, 0, 0.8, 2, 4], ft, None, fmt=lambda v: f'{v:g} µs'.replace('-', '−')))
    return 340, ''.join(o)

FIG[9] = (f9, 'Top: five neighbouring subcarriers of the worked example, 312.5 kHz apart; their spectra overlap, but at each subcarrier’s centre every other one is zero. '
              'Bottom: one 4.0 µs OFDM symbol, a 0.8 µs cyclic prefix before the 3.2 µs useful part; an echo of the previous symbol delayed less than 0.8 µs dies inside the prefix.',
          'Top: overlapping sinc-shaped spectra centred every 312.5 kilohertz, with a marker showing the neighbours pass through zero at the centre of one subcarrier. Bottom: a time line with the previous symbol, a 0.8 microsecond cyclic prefix and a 3.2 microsecond useful part, and a delayed echo of the previous symbol ending inside the prefix.')



# ---- sketches for model answers in the question bank (not chapter figures) ----
def ma_receivers():
    """coherent OOK receiver (top) and coherent BFSK receiver (bottom)"""
    o = []
    def mult(x, y):
        return (f'<circle cx="{x}" cy="{y}" r="15" style="fill:var(--panel);stroke:var(--accent);stroke-width:2"/>'
                + T(x, y + 6, '×', 18, 'middle', AC, True))
    # OOK
    y = 60
    o.append(T(20, y + 5, 'r(t)', 14, 'start', INK))
    o.append(L(56, y, 103, y, MUT, 2, arrow='m')); o.append(mult(120, y))
    o.append(L(120, y + 52, 120, y + 17, MUT, 2, arrow='m')); o.append(T(120, y + 68, '2cos(2πf' + '<tspan dy="4" font-size="11">c</tspan><tspan dy="-4">t)</tspan>', 13, 'middle', MUT))
    o.append(L(136, y, 178, y, MUT, 2, arrow='m'))
    o.append(boxt(180, y - 22, 120, 44, ['∫ over 0 to T' + '<tspan dy="4" font-size="11">b</tspan>'], PANEL, AC, 14))
    o.append(L(300, y, 348, y, MUT, 2, arrow='m')); o.append(T(324, y - 8, 'sample', 13, 'middle', MUT))
    o.append(boxt(350, y - 22, 190, 44, ['> A·T' + '<tspan dy="4" font-size="11">b</tspan><tspan dy="-4">/2 → 1, else 0</tspan>'], PANEL, NX, 14))
    o.append(L(540, y, 590, y, MUT, 2, arrow='m')); o.append(T(596, y + 5, 'OOK bit', 14, 'start', INK, True))
    # BFSK
    y1, y0 = 170, 250
    o.append(T(20, (y1 + y0) / 2 + 5, 'r(t)', 14, 'start', INK))
    o.append(L(56, (y1 + y0) / 2, 80, (y1 + y0) / 2, MUT, 2)); o.append(L(80, y1, 80, y0, MUT, 2))
    for yy, f in ((y1, '1'), (y0, '0')):
        o.append(L(80, yy, 103, yy, MUT, 2, arrow='m')); o.append(mult(120, yy))
        o.append(T(152, yy + (-22 if f == '1' else 32), 'cos(2πf' + f'<tspan dy="4" font-size="11">{f}</tspan><tspan dy="-4">t)</tspan>', 13, 'start', MUT))
        o.append(L(136, yy, 178, yy, MUT, 2, arrow='m'))
        o.append(boxt(180, yy - 20, 120, 40, ['∫ over T' + '<tspan dy="4" font-size="11">b</tspan>'], PANEL, AC, 14))
        o.append(L(300, yy, 330, yy, MUT, 2))
        o.append(T(318, yy - 8, 'l' + f'<tspan dy="4" font-size="11">{f}</tspan>', 13, 'middle', MUT))
    o.append(L(330, y1, 330, (y1 + y0) / 2 - 10, MUT, 2)); o.append(L(330, y0, 330, (y1 + y0) / 2 + 10, MUT, 2))
    o.append(L(330, (y1 + y0) / 2, 348, (y1 + y0) / 2, MUT, 2, arrow='m'))
    o.append(boxt(350, (y1 + y0) / 2 - 22, 190, 44, ['l' + '<tspan dy="4" font-size="11">1</tspan><tspan dy="-4"> − l</tspan><tspan dy="4" font-size="11">0</tspan><tspan dy="-4"> > 0 → 1</tspan>'], PANEL, NX, 14))
    o.append(L(540, (y1 + y0) / 2, 590, (y1 + y0) / 2, MUT, 2, arrow='m')); o.append(T(596, (y1 + y0) / 2 + 5, 'BFSK bit', 14, 'start', INK, True))
    return 290, ''.join(o)


def ma_bpsk_pdfs():
    """conditional pdfs of the BPSK correlator output at Eb/N0 = 0 dB, with the error tail shaded"""
    o = []
    x0, x1, yb = 60, 660, 200
    fx = lambda y: 360 + y * 150          # y in units of sqrt(Eb)
    sig = math.sqrt(0.5)                  # sigma / sqrt(Eb) at Eb/N0 = 1
    pdf = lambda y, m: math.exp(-(y - m) ** 2 / (2 * sig ** 2)) / (sig * math.sqrt(2 * math.pi))
    fy = lambda v: yb - v * 260
    tail = [(fx(-2.0), yb)] + [(fx(-2.0 + 2.0 * i / 100), fy(pdf(-2.0 + 2.0 * i / 100, 1))) for i in range(101)] + [(fx(0), yb)]
    o.append(P(tail, LV, 1, fill='var(--live-soft)'))
    for m, col, lab in ((1, AC, 'bit 1 sent'), (-1, NX, 'bit 0 sent')):
        o.append(P([(fx(-2.0 + 4.0 * i / 300), fy(pdf(-2.0 + 4.0 * i / 300, m))) for i in range(301)], col, 2.6))
        o.append(T(fx(m), fy(pdf(m, m)) - 10, lab, 13, 'middle', col, True))
    o.append(L(x0, yb, x1, yb, L2, 1.5))
    o.append(L(fx(0), 30, fx(0), yb + 6, INK, 1.8, '6 4'))
    for v, lab in ((-1, '−√E'), (0, '0'), (1, '+√E')):
        o.append(L(fx(v), yb, fx(v), yb + 6, L2, 1.5))
        o.append(T(fx(v), yb + 22, lab + ('<tspan dy="4" font-size="11">b</tspan>' if v else ''), 13, 'middle', MUT))
    o.append(T(fx(0) + 8, 40, 'threshold y = 0', 13, 'start', INK))
    o.append(T(fx(-0.25), yb - 12, 'P(e | 1)', 13, 'end', LV, True))
    o.append(T(x1, yb + 42, 'correlator output y (drawn at E' + '<tspan dy="4" font-size="11">b</tspan><tspan dy="-4">/N</tspan><tspan dy="4" font-size="11">0</tspan><tspan dy="-4"> = 0 dB so the tail shows)</tspan>', 13, 'end', MUT))
    return 254, ''.join(o)


def ma_psd_linear():
    """main lobes of BPSK, QPSK and MSK on a linear scale, same bit rate and Eb"""
    o = []
    x0, x1, y0, y1 = 80, 680, 40, 250
    fx = lambda f: x0 + f / 2 * (x1 - x0)
    fy = lambda v: y1 - v / 4.2 * (y1 - y0)
    sinc = lambda x: 1.0 if abs(x) < 1e-9 else math.sin(math.pi * x) / (math.pi * x)
    def msk(f):
        den = 16 * f * f - 1
        if abs(den) < 1e-6: f += 1e-4; den = 16 * f * f - 1
        return 32 / math.pi ** 2 * (math.cos(2 * math.pi * f) / den) ** 2
    o.append(axes(x0, x1, y0, y1, [0, 0.5, 0.75, 1, 1.5, 2], [0, 1, 2, 3, 4], fx, fy,
                  '(f − f' + '<tspan dy="4" font-size="11">c</tspan><tspan dy="-4">) / R</tspan><tspan dy="4" font-size="11">b</tspan>',
                  'S(f) in units of E' + '<tspan dy="4" font-size="11">b</tspan>', xfmt=lambda v: f'{v:g}'))
    for fn, col, dash, lab, lx, ly in ((lambda f: 2 * sinc(f) ** 2, AC, None, 'BPSK 2E_b sinc²(fT_b)', 0.62, 1.55),
                                       (lambda f: 4 * sinc(2 * f) ** 2, NX, '8 5', 'QPSK 4E_b sinc²(2fT_b)', 0.18, 3.85),
                                       (msk, LV, None, 'MSK', 0.47, 2.15)):
        o.append(P([(fx(2 * i / 600), fy(fn(2 * i / 600))) for i in range(601)], col, 2.4, dash))
        o.append(Tb(fx(lx), fy(ly), lab.replace('E_b', 'E<tspan dy="4" font-size="11">b</tspan><tspan dy="-4">').replace('(fT_b)', '(fT</tspan><tspan dy="4" font-size="11">b</tspan><tspan dy="-4">)</tspan>').replace('(2fT_b)', '(2fT</tspan><tspan dy="4" font-size="11">b</tspan><tspan dy="-4">)</tspan>'), 13, 'start', col, True))
    return 300, ''.join(o)


spec = make_spec(FIG)
