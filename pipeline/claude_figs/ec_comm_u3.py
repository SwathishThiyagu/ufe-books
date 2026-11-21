"""Claude's hand-drawn figures for ec-comm-u3 (Analog Communication: angle modulation and noise performance), one per
chapter, each drawn from that chapter's own worked example with its numbers computed here. Colours are the shell's CSS
variables. The ma_* functions draw the block and circuit diagrams used in the question bank's model answers."""
import os, sys, math, cmath, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

_T, _Tb = T, Tb


def _sub(s):
    """f_c, A_m ... drawn as real subscripts, never as underscores"""
    return re.sub(r'([A-Za-zα-ωΔ)])_([A-Za-z0-9]+)', r'\1<tspan baseline-shift="sub" font-size="11">\2</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


def curve(f, a, b, fx, fy, n=240):
    return [(fx(a + (b - a) * i / n), fy(f(a + (b - a) * i / n))) for i in range(n + 1)]


def J(n, x, terms=40):
    """Bessel function of the first kind, integer order (series), signed for negative n"""
    if n < 0: return (-1) ** n * J(-n, x)
    return sum((-1) ** k * (x / 2) ** (2 * k + n) / (math.factorial(k) * math.factorial(k + n)) for k in range(terms))


def blk(x, y, w, h, lines, fill=PANEL, stroke=AC, size=14, dash=None):
    return boxt(x, y, w, h, [_sub(s) for s in lines], fill, stroke, size, dash=dash)


def arrow(x1, y1, x2, y2, c=AC, w=2, dash=None):
    return L(x1, y1, x2, y2, c, w, dash, arrow='n' if c == AC else ('m' if c == L2 else ('l' if c == LV else 'x')))


def fmt(v, d=2):
    return f'{v:.{d}f}'.replace('-', '−')


# ---- 3.1 message, and the frequency swing it gives in FM and PM (worked example 1) ----
def f1():
    o = []
    x0, x1 = 90, 680
    fx = lin(0, 0.4, x0, x1)            # time in ms, two cycles of the 5 kHz tone
    # panel A: m(t) = 2 cos(2π·5000 t) V
    yc, amp = 92, 44
    o.append(T(x0, 30, 'Message m(t) = 2 cos(2π·5000t) V', 14, 'start', bold=True))
    o.append(L(x0, yc, x1, yc, L2, 1.5)); o.append(L(x0, yc - amp - 8, x0, yc + amp + 8, L2, 1.5))
    for v, s in ((2, '2 V'), (-2, '−2 V')):
        Y = yc - v / 2 * amp; o += [L(x0 - 5, Y, x0, Y, L2, 1.5), T(x0 - 9, Y + 5, s, 13, 'end', MUT)]
    o.append(P(curve(lambda t: 2 * math.cos(2 * math.pi * 5 * t), 0, 0.4, fx, lambda v: yc - v / 2 * amp), AC, 2.5))
    # panel B: instantaneous-frequency deviation, kHz
    yb, ab = 300, 88
    fy = lambda v: yb - v / 8 * ab
    o.append(T(x0, 178, 'Instantaneous frequency f_i − f_c (kHz)', 14, 'start', bold=True))
    o.append(L(x0, yb, x1, yb, L2, 1.5)); o.append(L(x0, yb - ab - 8, x0, yb + ab + 8, L2, 1.5))
    for v in (8, 6, 0, -6, -8):
        Y = fy(v); o += [L(x0 - 5, Y, x0, Y, L2, 1.5), T(x0 - 9, Y + 5, neg(v), 13, 'end', MUT)]
        if v: o.append(L(x0, Y, x1, Y, LN, 1, '3 5'))
    o.append(P(curve(lambda t: 6 * math.cos(2 * math.pi * 5 * t), 0, 0.4, fx, fy), AC, 2.5))
    o.append(P(curve(lambda t: -8 * math.sin(2 * math.pi * 5 * t), 0, 0.4, fx, fy), NX, 2.5, '7 5'))
    for t in (0, 0.1, 0.2, 0.3, 0.4):
        X = fx(t); o += [L(X, yb + ab + 8, X, yb + ab + 13, L2, 1.5), T(X, yb + ab + 30, f'{t:.1f}', 13, fill=MUT)]
    o.append(L(x0, yb + ab + 8, x1, yb + ab + 8, L2, 1.5))
    o.append(T(x1, yb + ab + 52, 'time (ms)', 14, 'end', MUT))
    o.append(Tb(fx(0.2) + 8, fy(6) - 10, 'FM: peak +6 kHz when m is +2 V', 13, 'start', AC, True))
    o.append(Tb(fx(0.15) + 4, fy(8) - 10, 'PM: peak 8 kHz', 13, 'middle', NX, True))
    o.append(Tb(fx(0.05) + 12, fy(-8) + 6, 'PM peaks where m(t) is steepest', 13, 'start', NX))
    return 470, ''.join(o)


# ---- 3.2 line spectra: narrowband β = 0.2 and wideband β = 2 (worked example 2), A_c = 10 V ----
def f2():
    o = []
    x0, x1 = 70, 670
    fx = lin(-6, 6, x0, x1)
    def panel(y0, beta, scale, title, labels, carson=None):
        o.append(T(20, y0 - 112, title, 14, 'start', bold=True))
        o.append(L(x0, y0, x1, y0, L2, 1.5))
        for n in range(-6, 7):
            a = 10 * J(n, beta)
            X = fx(n); o.append(L(X, y0, X, y0 + 5, L2, 1.5))
            if abs(a) < 0.1: continue
            Y = y0 - abs(a) * scale
            c = AC if a > 0 else NX
            o.append(L(X, y0, X, Y, c, 4)); o.append(C(X, Y, 4.5, c))
            if n in labels:
                o.append(Tb(X, Y - 10, fmt(a, 3 if abs(a) < 1 else 2), 13, 'middle', c, True))
        for n, s in ((-4, '−20'), (-2, '−10'), (0, 'f_c'), (2, '+10'), (4, '+20')):
            o.append(T(fx(n), y0 + 22, s, 13, fill=MUT))
        if carson:
            o.append(brace(fx(-3), fx(3), y0 + 36, INK))
            o.append(Tb(fx(0), y0 + 58, carson, 13, 'middle', INK, True))
    panel(140, 0.2, 9, 'Narrowband, β = 0.2: a carrier and one sideband pair', (-1, 0, 1))
    o.append(T(x1, 66, 'green = negative line (phase reversed)', 13, 'end', NX))
    panel(380, 2, 14, 'Wideband, β = 2: lines every f_m = 5 kHz, amplitude 10 J_n(2) V', (-3, -2, -1, 0, 1, 2, 3, 4),
          'Carson band 2(β + 1)f_m = 30 kHz holds 99.8 % of the power')
    o.append(T(x1, 470, 'offset from f_c (kHz)', 13, 'end', MUT))
    return 490, ''.join(o)


# ---- 3.3 the Armstrong chain of worked example 2, with carrier and deviation at every stage ----
def f3():
    o = []
    y1, y2, h = 40, 270, 64
    o.append(blk(12, y1, 108, h, ['Audio', 'm(t)']))
    o.append(blk(150, y1, 118, h, ['Integrator']))
    o.append(blk(298, y1, 150, h, ['Narrowband', 'phase modulator']))
    o.append(blk(298, y1 + 112, 150, 52, ['Crystal 100 kHz'], ACS))
    o.append(blk(520, y1, 120, h, ['× 75'], LVS, LV, 16))
    o.append(arrow(120, y1 + 32, 148, y1 + 32)); o.append(arrow(268, y1 + 32, 296, y1 + 32))
    o.append(arrow(373, y1 + 112, 373, y1 + 66)); o.append(arrow(448, y1 + 32, 518, y1 + 32))
    o.append(Tb(484, y1 + 92, '100 kHz', 13, 'middle', INK, True)); o.append(T(484, y1 + 110, 'Δf 20 Hz', 13, fill=MUT))
    # down to the mixer
    o.append(P([(580, y1 + h), (580, y1 + 186), (130, y1 + 186), (130, y2 - 2)], AC, 2))
    o.append(L(130, y2 - 14, 130, y2 - 2, AC, 2, arrow='n'))
    o.append(Tb(600, y1 + 100, '7.5 MHz', 13, 'start', INK, True)); o.append(T(600, y1 + 118, 'Δf 1.5 kHz', 13, 'start', MUT))
    o.append(blk(70, y2, 120, h, ['Mixer']))
    o.append(blk(70, y2 + 112, 120, 52, ['LO 5.58 MHz'], ACS))
    o.append(arrow(130, y2 + 112, 130, y2 + 66))
    o.append(blk(230, y2, 120, h, ['Band-pass', 'difference']))
    o.append(blk(400, y2, 110, h, ['× 50'], LVS, LV, 16))
    o.append(blk(560, y2, 120, h, ['Power', 'amplifier']))
    o.append(arrow(190, y2 + 32, 228, y2 + 32)); o.append(arrow(350, y2 + 32, 398, y2 + 32)); o.append(arrow(510, y2 + 32, 558, y2 + 32))
    o.append(Tb(375, y2 + 92, '1.92 MHz', 13, 'middle', INK, True)); o.append(T(375, y2 + 110, 'Δf 1.5 kHz', 13, fill=MUT))
    o.append(Tb(535, y2 + 92, '96 MHz', 13, 'middle', INK, True)); o.append(T(535, y2 + 110, 'Δf 75 kHz', 13, fill=MUT))
    o.append(T(450, y2 + 196, 'The multipliers scale carrier and deviation;', 13, fill=MUT))
    o.append(T(450, y2 + 216, 'the mixer moves only the carrier.', 13, fill=MUT))
    return 500, ''.join(o)


# ---- 3.4 Foster-Seeley phasors and S-curve of worked example 2 (Q = 20, 10.7 MHz) ----
def _fs(df, Q=20, f0=10.7e6):
    x = 2 * Q * df / f0
    e = 1j / (1 + 1j * x)
    return e, abs(1 + e), abs(1 - e)


def f4():
    o = []
    # phasors at f_c + 50 kHz, e_p = 1 V
    e, V1, V2 = _fs(50e3)
    ox, oy, s = 120, 210, 120
    P0 = (ox, oy); Pp = (ox + s, oy)
    o.append(T(20, 28, 'Phasors at f_c + 50 kHz', 14, 'start', bold=True))
    tip1 = (ox + s * (1 + e.real), oy - s * e.imag)
    tip2 = (ox + s * (1 - e.real), oy + s * e.imag)
    o.append(L(ox, oy, ox + s, oy, INK, 3, arrow='m'))
    o.append(L(ox + s, oy, *tip1, AC, 2.5, arrow='n')); o.append(L(ox + s, oy, *tip2, NX, 2.5, arrow='x'))
    o.append(L(ox, oy, *tip1, AC, 2.5, '6 4')); o.append(L(ox, oy, *tip2, NX, 2.5, '6 4'))
    o.append(Tb(ox + s / 2, oy + 22, 'e_p = 1 V', 13, 'middle', INK, True))
    o.append(T(tip1[0] + 6, tip1[1] + 4, 'e_s/2: 0.98 V at 79.4°', 13, 'start', AC))
    o.append(T(tip2[0] + 8, tip2[1] + 4, '−e_s/2', 13, 'start', NX))
    o.append(Tb(ox + 18, oy - 84, f'V1 = {V1:.3f}', 13, 'start', AC, True))
    o.append(Tb(ox + 2, oy + 74, f'V2 = {V2:.3f}', 13, 'start', NX, True))
    o.append(T(20, 330, f'v_o = V1 − V2 = {V1 - V2:.3f} V', 14, 'start', INK, True))
    # S-curve, ±800 kHz
    x0, x1, yc, a = 370, 700, 190, 120
    fx = lin(-800, 800, x0, x1); fy = lambda v: yc - v * a
    o.append(T(x0 - 10, 28, 'S-curve: v_o against deviation', 14, 'start', bold=True))
    o.append(L(x0, yc, x1, yc, L2, 1.5)); o.append(L(fx(0), yc - a - 14, fx(0), yc + a + 14, L2, 1.5))
    for v in (-800, -400, 400, 800):
        X = fx(v); o += [L(X, yc, X, yc + 5, L2, 1.5), T(X, yc + 22, neg(v), 13, fill=MUT)]
    for v in (0.9, -0.9):
        Y = fy(v); o += [L(fx(0) - 5, Y, fx(0) + 5, Y, L2, 1.5), T(fx(0) - 9, Y + 5, neg(f'{v} V'), 13, 'end', MUT)]
    pts = [(fx(d), fy(_fs(d * 1e3)[1] - _fs(d * 1e3)[2])) for d in range(-800, 801, 8)]
    o.append(P(pts, AC, 2.5))
    vo = _fs(50e3)[1] - _fs(50e3)[2]
    o.append(C(fx(50), fy(vo), 5, LV)); o.append(Tb(fx(50) + 14, fy(vo) + 4, '+50 kHz: 0.259 V', 13, 'start', LV, True))
    pk = _fs(328e3)[1] - _fs(328e3)[2]
    o.append(C(fx(328), fy(pk), 5, NX)); o.append(Tb(fx(328), fy(pk) - 12, 'peak 0.894 V at 328 kHz', 13, 'middle', NX))
    o.append(T(x1, yc + a + 36, 'deviation (kHz)', 13, 'end', MUT))
    o.append(T(fx(0) - 10, yc + 22, '0', 13, 'end', MUT))
    return 350, ''.join(o)


# ---- 3.5 output SNR against channel SNR (worked example 1) ----
def f5():
    o = []
    x0, x1, y0, y1 = 90, 520, 40, 380
    fx = lin(0, 40, x0, x1); fy = lin(-10, 60, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0, 10, 20, 30, 40], [-10, 0, 10, 20, 30, 40, 50, 60], fx, fy,
                  'channel SNR (dB)', 'output SNR (dB)', neg, neg))
    lines = [('FM, β = 5', 15.74, AC, None), ('DSB-SC and SSB', 0, LV, None), ('AM, m = 0.5', -9.54, NX, None)]
    for name, g, c, d in lines:
        a = max(0, -10 - g)
        if name.startswith('FM'):
            o.append(P([(fx(0), fy(g)), (fx(20.8), fy(20.8 + g))], c, 2.5, '6 5'))
            o.append(P([(fx(20.8), fy(20.8 + g)), (fx(40), fy(40 + g))], c, 3))
        else:
            o.append(P([(fx(a), fy(a + g)), (fx(40), fy(40 + g))], c, 3))
    for v, c in ((35.74, AC), (20, LV), (10.46, NX)):
        o.append(C(fx(20), fy(v), 5.5, c))
    o.append(L(fx(20), y1, fx(20), fy(35.74), LN, 1, '3 4'))
    side = 540
    o.append(T(side, fy(55.7) + 4, 'FM, β = 5', 14, 'start', AC, True))
    o.append(T(side, fy(55.7) + 22, 'FOM 37.5 (+15.74 dB)', 13, 'start', AC))
    o.append(T(side, fy(40) + 4, 'DSB-SC, SSB', 14, 'start', LV, True))
    o.append(T(side, fy(40) + 22, 'FOM 1 (0 dB)', 13, 'start', LV))
    o.append(T(side, fy(30.46) + 4, 'AM, m = 0.5', 14, 'start', NX, True))
    o.append(T(side, fy(30.46) + 22, 'FOM 0.111 (−9.54 dB)', 13, 'start', NX))
    o.append(Tb(fx(20) + 8, fy(35.74) + 4, '35.74', 13, 'start', AC, True))
    o.append(Tb(fx(20) + 8, fy(20) + 18, '20', 13, 'start', LV, True))
    o.append(Tb(fx(20) + 8, fy(10.46) + 18, '10.46', 13, 'start', NX, True))
    o.append(T(fx(1), fy(30), 'dashed: FM below', 13, 'start', MUT))
    o.append(T(fx(1), fy(30) + 17, 'its threshold', 13, 'start', MUT))
    return 430, ''.join(o)


# ---- 3.6 output SNR against received carrier power, β = 2 and β = 5 (worked examples 1 and 2) ----
def f6():
    o = []
    x0, x1, y0, y1 = 90, 560, 40, 360
    fx = lin(-118, -100, x0, x1); fy = lin(10, 50, y1, y0)
    o.append(axes(x0, x1, y0, y1, [-118, -114, -110, -106, -102], [10, 20, 30, 40, 50], fx, fy,
                  'received carrier power C (dBm)', 'output SNR (dB)', neg, neg))
    for th, base, c, name in ((-111.43, 36.53, AC, 'β = 5, B_T = 180 kHz'), (-114.44, 25.56, LV, 'β = 2, B_T = 90 kHz')):
        o.append(P([(fx(th), fy(base)), (fx(-100), fy(base + (-100 - th)))], c, 3))
        o.append(C(fx(th), fy(base), 6, c))
        o.append(L(fx(th), fy(base), fx(th - 0.45), fy(base - 8), c, 2, '4 4', arrow='n' if c == AC else 'l'))
        o.append(T(570, fy(base + (-100 - th)) + 5, name, 13, 'start', c, True))
    o.append(Tb(fx(-111.43) + 10, fy(36.53) + 20, 'threshold −111.4 dBm, 36.5 dB', 13, 'start', AC, True))
    o.append(Tb(fx(-114.44) + 10, fy(25.56) + 20, 'threshold −114.4 dBm, 25.6 dB', 13, 'start', LV, True))
    o.append(T(x0 + 8, y1 - 14, 'dashed arrows: clicks, output falls steeply (not to scale)', 13, 'start', MUT))
    return 410, ''.join(o)


# ---- 3.7 pre-emphasis and de-emphasis gains for τ = 75 µs (worked example) ----
def f7():
    o = []
    x0, x1, y0, y1 = 90, 640, 40, 360
    lf = lambda f: math.log10(f)
    fx = lin(lf(100), lf(20000), x0, x1); fy = lin(-20, 20, y1, y0)
    f1 = 1 / (2 * math.pi * 75e-6)
    g = lambda f: 10 * math.log10(1 + (f / f1) ** 2)
    o.append(axes(x0, x1, y0, y1, [], [-20, -10, 0, 10, 20], lambda v: v, fy, '', 'gain (dB)', neg, neg))
    for f, s in ((100, '100'), (1000, '1 k'), (10000, '10 k'), (20000, '20 k')):
        X = fx(lf(f)); o += [L(X, y1, X, y1 + 5, L2, 1.5), T(X, y1 + 20, s, 13, fill=MUT)]
    for f in (200, 300, 500, 2000, 3000, 5000):
        X = fx(lf(f)); o.append(L(X, y1, X, y1 + 3, L2, 1))
    o.append(T((x0 + x1) / 2, y1 + 42, 'audio frequency (Hz, log scale)', 14, fill=MUT))
    pts = lambda s: [(fx(lf(100) + (lf(20000) - lf(100)) * i / 200), fy(s * g(10 ** (lf(100) + (lf(20000) - lf(100)) * i / 200)))) for i in range(201)]
    o.append(L(x0, fy(0), x1, fy(0), LV, 2.5, '8 5'))
    o.append(P(pts(1), AC, 3)); o.append(P(pts(-1), NX, 3))
    X1 = fx(lf(f1)); o.append(L(X1, y0, X1, y1, LN, 1, '3 4'))
    o.append(Tb(X1, y0 + 4, 'f_1 = 2122 Hz', 13, 'middle', INK, True))
    o.append(C(X1, fy(3.01), 5, AC)); o.append(C(X1, fy(-3.01), 5, NX))
    o.append(Tb(X1 - 10, fy(3.01) - 10, '+3.01 dB', 13, 'end', AC, True))
    o.append(Tb(X1 - 10, fy(-3.01) + 20, '−3.01 dB', 13, 'end', NX, True))
    X2 = fx(lf(15000)); o.append(C(X2, fy(17.07), 5, AC)); o.append(C(X2, fy(-17.07), 5, NX))
    o.append(Tb(X2 - 10, fy(17.07) - 4, '+17.07 dB at 15 kHz', 13, 'end', AC, True))
    o.append(Tb(X2 - 10, fy(-17.07) + 6, '−17.07 dB', 13, 'end', NX, True))
    o.append(T(x0 + 10, fy(10), 'pre-emphasis (transmitter)', 13, 'start', AC, True))
    o.append(T(x0 + 10, fy(-10), 'de-emphasis (receiver)', 13, 'start', NX, True))
    o.append(Tb(x0 + 150, fy(0) - 8, 'product: 0 dB, flat', 13, 'middle', LV, True))
    return 410, ''.join(o)


# ---- 3.8 composite stereo baseband of worked example 1 ----
def f8():
    o = []
    x0, x1, yb = 50, 690, 250
    fx = lin(0, 60, x0, x1)
    o.append(L(x0, yb, x1, yb, L2, 1.5))
    for v in (0, 15, 19, 23, 38, 53, 57):
        X = fx(v); o += [L(X, yb, X, yb + 5, L2, 1.5), T(X, yb + 22, str(v), 13, fill=MUT)]
    o.append(T(x1, yb + 46, 'baseband frequency (kHz)', 13, 'end', MUT))
    o.append(R(fx(0), yb - 150, fx(15) - fx(0), 150, ACS, AC, 3))
    o.append(T((fx(0) + fx(15)) / 2, yb - 120, 'L + R', 15, bold=True)); o.append(T((fx(0) + fx(15)) / 2, yb - 100, '1.5 V', 13, fill=MUT))
    o.append(T((fx(0) + fx(15)) / 2, yb - 80, 'mono', 13, fill=MUT))
    o.append(L(fx(19), yb, fx(19), yb - 46, LV, 4)); o.append(C(fx(19), yb - 46, 5, LV))
    o.append(Tb(fx(19), yb - 58, 'pilot 19', 13, 'middle', LV, True))
    for a, b, s in ((23, 38, 'lower'), (38, 53, 'upper')):
        o.append(R(fx(a), yb - 50, fx(b) - fx(a), 50, NXS, NX, 3))
        o.append(T((fx(a) + fx(b)) / 2, yb - 22, f'{s} sideband', 13))
    o.append(Tb(fx(38), yb - 70, 'L − R = 0.5 V on DSB-SC', 14, 'middle', NX, True))
    o.append(L(fx(38), yb, fx(38), yb - 118, NX, 2, '5 4'))
    o.append(Tb(fx(38), yb - 124, '38 kHz carrier suppressed', 13, 'middle', NX))
    o.append(L(fx(57), yb, fx(57), yb - 30, MUT, 2, '4 4'))
    o.append(Tb(fx(57) - 2, yb - 38, 'RDS', 13, 'middle', MUT))
    o.append(brace(fx(0), fx(53), yb + 62, INK))
    o.append(Tb((fx(0) + fx(53)) / 2, yb + 84, 'stereo baseband 0 to 53 kHz', 13, 'middle', INK, True))
    return 350, ''.join(o)


FIG = {
    1: (f1, 'Worked example 1 drawn over two cycles of the 5 kHz tone. In FM the frequency swing copies the message, peaking at 6 kHz when m(t) is at +2 V; in PM it copies the slope of the message and peaks at 1.6 rad × 5 kHz = 8 kHz where the message crosses zero.',
        'Top: a 2 volt, 5 kilohertz cosine message over 0.4 milliseconds. Bottom: the FM frequency swing, a cosine of peak 6 kilohertz, and the PM swing, a minus sine of peak 8 kilohertz.'),
    2: (f2, 'Line spectra with A_c = 10 V. For β = 0.2 there is one sideband pair and the lower line is negative, so the pair is in quadrature with the carrier; for β = 2 (worked example 2) the lines are 10 J_n(2) volts, and the Carson band of three pairs holds 99.8 % of the power.'.replace('A_c', 'A<sub>c</sub>').replace('J_n', 'J<sub>n</sub>'),
        'Two spectra. Narrowband beta 0.2: carrier 9.90 volts and sidebands plus 0.995 and minus 0.995 volts. Wideband beta 2: carrier 2.24 volts, first pair 5.77, second 3.53, third 1.29 volts, with a 30 kilohertz Carson bracket.'),
    3: (f3, 'The Armstrong chain of worked example 2. The ×75 and ×50 multipliers raise the 20 Hz deviation 3750 times to 75 kHz; the mixer between them pulls the carrier down from 7.5 MHz to 1.92 MHz so the second multiplier lands on 96 MHz.',
        'Block diagram: audio, integrator, narrowband phase modulator fed by a 100 kilohertz crystal, times 75 multiplier to 7.5 megahertz, mixer with a 5.58 megahertz oscillator, band-pass filter at 1.92 megahertz, times 50 multiplier, power amplifier at 96 megahertz with 75 kilohertz deviation.'),
    4: (f4, 'Worked example 2 in pictures. At 50 kHz above f<sub>c</sub> the secondary phasor turns to 79.4°, so the diode voltages V1 and V2 differ by 0.259 V; sweeping the frequency gives the S-curve, zero at f<sub>c</sub>, nearly straight out to about ±150 kHz and peaking at ±328 kHz.',
        'Left: phasor diagram with primary voltage 1 volt, half secondary 0.98 volt at 79.4 degrees, and resultants V1 1.526 and V2 1.267 volts. Right: computed S-curve of output against deviation from minus 800 to plus 800 kilohertz.'),
    5: (f5, 'Output SNR against channel SNR for the three cases of worked example 1. Each line sits above or below the 0 dB line of DSB-SC and SSB by its figure of merit; at 20 dB in, AM gives 10.46 dB and FM 35.74 dB. The FM line is dashed below its threshold.',
        'Three straight lines: FM beta 5 at 15.74 dB above the input, DSB-SC and SSB equal to the input, and AM m 0.5 at 9.54 dB below, with points at 35.74, 20 and 10.46 dB for a 20 dB input.'),
    6: (f6, 'The two receivers of the worked examples. Above threshold each line rises 1 dB for 1 dB of carrier power, β = 5 sitting higher; but β = 5 needs −111.4 dBm to reach threshold and β = 2 only −114.4 dBm, so the narrower system keeps working on weaker signals.',
        'Output SNR against received carrier power: beta 5 line starting at minus 111.4 dBm and 36.5 dB, beta 2 line starting at minus 114.4 dBm and 25.6 dB, with dashed arrows showing the fall below threshold.'),
    7: (f7, 'Gain of the 75 µs networks of the worked example. Pre-emphasis is +3.01 dB at the 2122 Hz corner and +17.07 dB at 15 kHz; de-emphasis is the exact mirror, so the product is flat at 0 dB.',
        'Pre-emphasis gain rising from 0 to plus 17 dB and de-emphasis falling to minus 17 dB between 100 hertz and 20 kilohertz on a log axis, with the 2122 hertz corner marked.'),
    8: (f8, 'The composite baseband of worked example 1. L + R fills 0 to 15 kHz, the 19 kHz pilot sits in the gap, and L − R rides as two sidebands around a suppressed 38 kHz carrier from 23 to 53 kHz; RDS, where used, sits at 57 kHz.',
        'Spectrum from 0 to 60 kilohertz: L plus R block to 15, pilot line at 19, L minus R sidebands from 23 to 38 and 38 to 53 kilohertz, dashed suppressed carrier at 38 and an RDS line at 57.'),
}
spec = make_spec(FIG)


# ---- diagrams for the question bank's model answers ----
def ma_direct():
    """direct FM transmitter with AFC"""
    o = []
    y = 30
    o.append(blk(12, y, 110, 60, ['Audio', 'amplifier']))
    o.append(blk(160, y, 170, 60, ['LC oscillator', 'with varactor']))
    o.append(blk(370, y, 110, 60, ['Buffer and', 'multiplier']))
    o.append(blk(520, y, 120, 60, ['Power', 'amplifier']))
    o.append(arrow(122, y + 30, 158, y + 30)); o.append(arrow(330, y + 30, 368, y + 30)); o.append(arrow(480, y + 30, 518, y + 30))
    o.append(blk(370, y + 120, 110, 60, ['Mixer']))
    o.append(blk(520, y + 120, 120, 60, ['Crystal', 'reference'], ACS))
    o.append(blk(160, y + 120, 170, 60, ['Discriminator', 'and low-pass']))
    o.append(P([(425, y + 60), (425, y + 118)], AC, 2)); o.append(L(425, y + 108, 425, y + 118, AC, 2, arrow='n'))
    o.append(arrow(518, y + 150, 482, y + 150)); o.append(arrow(368, y + 150, 332, y + 150))
    o.append(P([(245, y + 120), (245, y + 62)], LV, 2)); o.append(L(245, y + 72, 245, y + 62, LV, 2, arrow='l'))
    o.append(Tb(245, y + 98, 'AFC: slow dc', 13, 'middle', LV, True))
    o.append(T(330, y + 214, 'The loop corrects slow drift of the centre frequency, not the audio deviation.', 13, fill=MUT))
    return 260, ''.join(o)


def ma_foster():
    """Foster-Seeley discriminator schematic"""
    o = []
    def coil(x, y0, y1, c=AC):
        n = 4; h = (y1 - y0) / n; d = f'M{x},{y0} '
        for i in range(n): d += f'a {h / 2},{h / 2} 0 0 1 0,{h} '
        return f'<path d="{d}" style="fill:none;stroke:{c};stroke-width:2.2"/>'
    def coil_h(x0, x1, y, c=INK):
        n = 4; w = (x1 - x0) / n; d = f'M{x0},{y} '
        for i in range(n): d += f'a {w / 2},{w / 2} 0 0 1 {w},0 '
        return f'<path d="{d}" style="fill:none;stroke:{c};stroke-width:2.2"/>'
    def cap(x, y, vert=True, c=INK):
        if vert: return L(x - 12, y - 4, x + 12, y - 4, c, 2.5) + L(x - 12, y + 4, x + 12, y + 4, c, 2.5)
        return L(x - 4, y - 12, x - 4, y + 12, c, 2.5) + L(x + 4, y - 12, x + 4, y + 12, c, 2.5)
    def diode(x1, y, x2, c=INK):
        m = (x1 + x2) / 2
        return (L(x1, y, m - 9, y, c, 2) + f'<path d="M{m - 9},{y - 9} L{m + 7},{y} L{m - 9},{y + 9} z" style="fill:{c}"/>' +
                L(m + 7, y - 10, m + 7, y + 10, c, 2.5) + L(m + 7, y, x2, y, c, 2))
    top, bot, mid = 90, 270, 180
    # primary tank
    o.append(L(20, top, 100, top, INK, 2)); o.append(L(20, bot, 100, bot, INK, 2))
    o.append(T(20, top - 12, 'IF in', 13, 'start', MUT))
    o.append(L(60, top, 60, mid - 4, INK, 2)); o.append(cap(60, mid)); o.append(L(60, mid + 4, 60, bot, INK, 2))
    o.append(T(44, mid + 5, 'C1', 13, 'end'))
    o.append(L(100, top, 100, top + 10, INK, 2)); o.append(coil(100, top + 10, bot - 10)); o.append(L(100, bot - 10, 100, bot, INK, 2))
    o.append(T(126, mid + 5, 'L1', 13, 'start', AC))
    # secondary, centre-tapped
    o.append(coil(190, top, bot, LV)); o.append(T(178, mid - 40, 'L2', 13, 'end', LV))
    o.append(L(206, mid, 350, mid, INK, 2)); o.append(C(206, mid, 3.5, INK))
    # coupling capacitor from the primary to the centre tap, RF choke to the load midpoint
    o.append(P([(100, top), (100, 40), (340, 40)], INK, 2)); o.append(cap(350, 40, vert=False)); o.append(P([(354, 40), (370, 40), (370, mid)], INK, 2))
    o.append(T(350, 24, 'Cc', 13)); o.append(C(370, mid, 3.5, INK))
    o.append(L(350, mid, 370, mid, INK, 2)); o.append(coil_h(370, 430, mid)); o.append(L(430, mid, 470, mid, INK, 2))
    o.append(T(400, mid + 28, 'L3 (RFC)', 13))
    # diodes
    o.append(L(190, top, 230, top, INK, 2)); o.append(diode(230, top, 470))
    o.append(L(190, bot, 230, bot, INK, 2)); o.append(diode(230, bot, 470))
    o.append(T(290, top - 14, 'D1: e_p + e_s/2', 13, 'middle', AC, True))
    o.append(T(290, bot + 26, 'D2: e_p − e_s/2', 13, 'middle', NX, True))
    # loads
    for ya, yb_, lab in ((top, mid, 'V1'), (mid, bot, 'V2')):
        ym = (ya + yb_) / 2
        o.append(L(470, ya, 470, ym - 22, INK, 2)); o.append(R(461, ym - 22, 18, 44, 'none', INK, 2, 1.8)); o.append(L(470, ym + 22, 470, yb_, INK, 2))
        o.append(L(470, ya, 540, ya, INK, 2)); o.append(L(540, ya, 540, ym - 4, INK, 2)); o.append(cap(540, ym)); o.append(L(540, ym + 4, 540, yb_, INK, 2))
        o.append(T(560, ym + 5, lab, 14, 'start', INK, True))
    o.append(L(470, mid, 540, mid, INK, 2)); o.append(C(470, mid, 3.5, INK))
    o.append(L(540, top, 610, top, INK, 2)); o.append(L(540, bot, 610, bot, INK, 2))
    o.append(T(618, top + 5, 'out', 13, 'start')); o.append(T(618, bot + 5, 'out', 13, 'start'))
    o.append(T(130, bot + 56, 'primary and secondary both tuned to f_c', 13, 'start', MUT))
    o.append(T(580, bot + 56, 'v_o = V1 − V2', 14, 'middle', INK, True))
    return bot + 76, ''.join(o)


def ma_emph():
    """pre-emphasis and de-emphasis RC networks"""
    o = []
    def res(x, y, w=50, vert=False):
        return R(x, y - 9, w, 18, 'none', INK, 2, 1.8) if not vert else R(x - 9, y, 18, w, 'none', INK, 2, 1.8)
    def cap_v(x, y): return L(x - 12, y - 4, x + 12, y - 4, INK, 2.5) + L(x - 12, y + 4, x + 12, y + 4, INK, 2.5)
    def cap_h(x, y): return L(x - 4, y - 12, x - 4, y + 12, INK, 2.5) + L(x + 4, y - 12, x + 4, y + 12, INK, 2.5)
    # pre-emphasis: R1 parallel C in series, R2 shunt
    o.append(T(20, 26, 'Pre-emphasis (transmitter): τ = R1·C = 75 µs', 14, 'start', AC, True))
    y = 120
    o.append(L(20, y, 110, y, INK, 2)); o.append(res(110, y)); o.append(L(160, y, 250, y, INK, 2))
    o.append(P([(100, y), (100, y - 40), (125, y - 40)], INK, 2)); o.append(cap_h(130, y - 40)); o.append(P([(134, y - 40), (170, y - 40), (170, y)], INK, 2))
    o.append(T(135, y + 30, 'R1', 13)); o.append(T(130, y - 60, 'C', 13))
    o.append(L(250, y, 300, y, INK, 2)); o.append(res(250, y, 60, True)); o.append(L(250, y + 60, 250, y + 80, INK, 2))
    o.append(T(268, y + 36, 'R2', 13, 'start')); o.append(L(20, y + 80, 300, y + 80, INK, 2))
    o.append(T(20, y + 104, 'in', 13, 'start', MUT)); o.append(T(300, y + 104, 'out', 13, 'end', MUT))
    o.append(T(160, y + 130, 'C bypasses R1 at high f: treble rises', 13, 'middle', MUT))
    # de-emphasis: series R, shunt C
    x = 380
    o.append(T(x, 26, 'De-emphasis (receiver): τ = R·C = 75 µs', 14, 'start', NX, True))
    o.append(L(x, y, x + 80, y, INK, 2)); o.append(res(x + 80, y, 60)); o.append(L(x + 140, y, x + 300, y, INK, 2))
    o.append(T(x + 110, y - 18, 'R = 10 kΩ', 13))
    o.append(L(x + 220, y, x + 220, y + 36, INK, 2)); o.append(cap_v(x + 220, y + 40)); o.append(L(x + 220, y + 44, x + 220, y + 80, INK, 2))
    o.append(T(x + 238, y + 45, 'C = 7.5 nF', 13, 'start')); o.append(L(x, y + 80, x + 300, y + 80, INK, 2))
    o.append(T(x, y + 104, 'in', 13, 'start', MUT)); o.append(T(x + 300, y + 104, 'out', 13, 'end', MUT))
    o.append(T(x + 150, y + 130, 'C shorts the treble: −6 dB per octave above f_1', 13, 'middle', MUT))
    return 270, ''.join(o)


def ma_stereo():
    """FM stereo transmitter and receiver"""
    o = []
    o.append(T(12, 22, 'Transmitter', 14, 'start', AC, True))
    y = 40
    o.append(blk(12, y, 86, 104, ['L, R', 'with', 'pre-emph.']))
    o.append(blk(124, y, 96, 104, ['Matrix', 'L + R', 'L − R']))
    o.append(blk(250, y + 62, 110, 44, ['Balanced mod.'], NXS, NX, 13))
    o.append(blk(250, y + 128, 110, 40, ['19 kHz osc.'], LVS, LV, 13))
    o.append(blk(390, y + 128, 70, 40, ['× 2'], LVS, LV, 13))
    o.append(blk(420, y, 70, 104, ['Σ']))
    o.append(blk(530, y + 26, 160, 52, ['FM modulator', '±75 kHz']))
    o.append(arrow(98, y + 52, 122, y + 52))
    o.append(arrow(220, y + 22, 418, y + 22)); o.append(T(320, y + 16, 'L + R, 0–15 kHz', 13))
    o.append(arrow(220, y + 84, 248, y + 84)); o.append(arrow(360, y + 84, 418, y + 84))
    o.append(P([(360, y + 148), (388, y + 148)], LV, 2)); o.append(L(380, y + 148, 388, y + 148, LV, 2, arrow='l'))
    o.append(P([(425, y + 128), (425, y + 118), (305, y + 118), (305, y + 108)], LV, 2)); o.append(L(305, y + 114, 305, y + 107, LV, 2, arrow='l'))
    o.append(T(432, y + 124, '38 kHz', 13, 'start', LV))
    o.append(P([(305, y + 168), (305, y + 180), (500, y + 180), (500, y + 96), (492, y + 96)], LV, 2, '4 3'))
    o.append(L(498, y + 96, 492, y + 96, LV, 2, arrow='l'))
    o.append(T(520, y + 200, 'pilot added at 8–10 % of the modulation', 13, 'middle', LV))
    o.append(arrow(490, y + 52, 528, y + 52))
    # receiver
    y2 = 290
    o.append(T(12, y2 - 18, 'Receiver', 14, 'start', NX, True))
    o.append(blk(12, y2, 120, 56, ['Discriminator']))
    o.append(blk(170, y2 - 40, 130, 44, ['LPF 0–15 kHz'], size=13))
    o.append(blk(170, y2 + 18, 130, 44, ['BPF 23–53 kHz'], size=13))
    o.append(blk(170, y2 + 82, 130, 44, ['19 kHz filter, PLL'], LVS, LV, 13))
    o.append(blk(340, y2 + 82, 80, 44, ['× 2 → 38'], LVS, LV, 13))
    o.append(blk(340, y2 + 18, 110, 44, ['Product det.'], NXS, NX, 13))
    o.append(blk(490, y2 - 40, 90, 102, ['Matrix']))
    o.append(blk(610, y2 - 40, 98, 102, ['De-emph.', 'L and R']))
    o.append(P([(132, y2 + 28), (150, y2 + 28)], AC, 2))
    for yy in (y2 - 18, y2 + 40, y2 + 104):
        o.append(P([(150, y2 + 28), (150, yy), (168, yy)], AC, 2)); o.append(L(160, yy, 168, yy, AC, 2, arrow='n'))
    o.append(arrow(300, y2 - 18, 488, y2 - 18)); o.append(T(395, y2 - 24, 'L + R', 13))
    o.append(arrow(300, y2 + 40, 338, y2 + 40)); o.append(arrow(300, y2 + 104, 338, y2 + 104))
    o.append(P([(380, y2 + 82), (380, y2 + 64)], LV, 2)); o.append(L(380, y2 + 70, 380, y2 + 63, LV, 2, arrow='l'))
    o.append(arrow(450, y2 + 40, 488, y2 + 40)); o.append(T(469, y2 + 80, 'L − R', 13))
    o.append(arrow(580, y2 + 11, 608, y2 + 11))
    return 430, ''.join(o)


MA = {'direct': (ma_direct, 'Direct FM transmitter: varactor-tuned LC oscillator with an AFC loop to a crystal reference'),
      'foster': (ma_foster, 'Foster-Seeley discriminator: tuned primary and centre-tapped tuned secondary, coupling capacitor and RF choke, two diodes with RC loads, output V1 minus V2'),
      'emph': (ma_emph, 'Pre-emphasis network with R1 parallel to C and shunt R2, and a de-emphasis network with series 10 kilohm resistor and shunt 7.5 nanofarad capacitor'),
      'stereo': (ma_stereo, 'FM stereo transmitter and receiver block diagrams with matrix, 19 kilohertz pilot, doubler, balanced modulator, product detector and de-emphasis')}


def ma(name):
    fn, aria = MA[name]
    h, body = fn()
    return {'h': h, 'body': body, 'aria': aria}
