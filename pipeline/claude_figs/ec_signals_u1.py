"""Claude's hand-drawn figures for ec-signals-u1 (Signals and Systems: classification of signals and systems), one per
chapter, drawn from each chapter's own worked example and numbers. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

PI = math.pi
FIG = {}


def sup(base, s):
    """base text with a raised exponent (no caret on screen)"""
    return f'{base}<tspan dy="-7" font-size="13">{s}</tspan><tspan dy="7"> </tspan>'


def stem(x, y0, y, c=AC, r=5):
    return L(x, y0, x, y, c, 2.5) + C(x, y, r, c)


# ---- 1.1 a CT signal and its samples ----
def f1():
    o = []
    x0, x1 = 90, 690
    fx = lambda t: x0 + t / 0.1 * (x1 - x0)
    # top: x(t)
    yc = 120; fy = lambda v: yc - v * 15
    o.append(T(x0, 36, 'x(t) = 4 sin(20πt) V: a value at every real t', 14, 'start', bold=True))
    o.append(L(x0, yc, x1, yc, L2, 1.5)); o.append(L(x0, fy(4.8), x0, fy(-4.8), L2, 1.5))
    for v in (4, -4):
        o += [L(x0 - 5, fy(v), x0, fy(v), L2, 1.5), T(x0 - 9, fy(v) + 4.5, neg(v) + ' V', 13, 'end', MUT)]
    o.append(P([(fx(i / 1000), fy(4 * math.sin(20 * PI * i / 1000))) for i in range(0, 101)], AC, 2.5))
    for t in (0.025, 0.05, 0.075, 0.1):
        o += [L(fx(t), yc, fx(t), yc + 5, L2, 1.5), T(fx(t), yc + 20, str(t), 13, fill=MUT)]
    o.append(T(x1, yc + 40, 't (s)', 14, 'end', MUT))
    o.append(C(fx(0.025), fy(4), 6, NX))
    o.append(Tb(fx(0.025) + 12, fy(4) - 4, 'x(0.025 s) = 4 V', 14, 'start', NX, bold=True))
    # middle: the sampler
    o.append(L(360, 192, 360, 228, MUT, 2, arrow='m'))
    o.append(T(372, 215, 'sample every Tₛ = 10 ms:  x[n] = x(n × 0.01 s)', 14, 'start', MUT))
    # bottom: x[n]
    yc2 = 350; gy = lambda v: yc2 - v * 15
    o.append(T(x0, 262, 'x[n] = 4 sin(0.2πn) V: values only at integer n', 14, 'start', bold=True))
    o.append(L(x0, yc2, x1, yc2, L2, 1.5)); o.append(L(x0, gy(4.8), x0, gy(-4.8), L2, 1.5))
    for v in (4, -4):
        o += [L(x0 - 5, gy(v), x0, gy(v), L2, 1.5), T(x0 - 9, gy(v) + 4.5, neg(v) + ' V', 13, 'end', MUT)]
    vals = [4 * math.sin(0.2 * PI * n) for n in range(11)]
    for n, v in enumerate(vals):
        X = x0 + n * 60
        o.append(stem(X, yc2, gy(v), NX if n == 5 else LV))
        o.append(T(X, yc2 + 20 if v > -0.01 else yc2 - 9, str(n), 13, fill=MUT))
    o.append(T(x1, yc2 + 78, 'n (sample index, no unit)', 14, 'end', MUT))
    o.append(Tb(x0 + 5 * 60, yc2 + 48, 'x[5] = 4 sin(π) = 0 V', 14, 'middle', NX, bold=True))
    o.append(T(x0 + 3 * 60 + 10, gy(3.804) + 5, '3.80 V', 13, 'start', MUT))
    return 440, ''.join(o)


FIG[1] = (f1, 'The voltage x(t) = 4 sin(20πt) V has a value at every instant; sampling it every 10 ms keeps only '
              'x[n] = x(0.01n), the dots. The worked example’s two values are marked: x(0.025 s) = 4 V on the curve and x[5] = 0 V among the samples.',
          'Top: a sine curve x(t) = 4 sin(20πt) volts from t = 0 to 0.1 s, peak 4 V at t = 0.025 s. Bottom: its eleven samples x[n] '
          'for n = 0 to 10, taken every 10 ms; x[5] is 0 V.')


# ---- 1.2 even and odd parts of a short sequence ----
def f2():
    o = []
    panels = [('x[n]', {0: 1, 1: 2, 2: 3}, 'E = 1 + 4 + 9 = 14', AC),
              ('xₑ[n]', {-2: 1.5, -1: 1, 0: 1, 1: 1, 2: 1.5}, 'Eₑ = 7.5', LV),
              ('xₒ[n]', {-2: -1.5, -1: -1, 1: 1, 2: 1.5}, 'Eₒ = 6.5', NX)]
    yz = 160; sc = 30
    for i, (name, vals, en, col) in enumerate(panels):
        cx = 125 + i * 235
        fx = lambda n: cx + n * 30
        o.append(T(cx, 34, name, 15, bold=True))
        o.append(L(fx(-3.4), yz, fx(3.4), yz, L2, 1.5))
        for n in range(-3, 4):
            v = vals.get(n, 0)
            if v == 0:
                o.append(C(fx(n), yz, 3.5, MUT))
                continue
            o.append(stem(fx(n), yz, yz - v * sc, col))
            o.append(T(fx(n), yz - v * sc - 10 if v > 0 else yz - v * sc + 21, neg(v).replace('&#8722;', '−'), 13, fill=INK))
        for n in (-2, 0, 2):
            o.append(T(fx(n), yz - 9 if vals.get(n, 0) < 0 else yz + 22, str(n).replace('-', '−'), 13, fill=MUT))
        o.append(T(cx, 262, en, 14, fill=col, bold=True))
    o.append(T(360, 300, 'xₑ[n] + xₒ[n] = x[n] at every n, and 7.5 + 6.5 = 14', 14, fill=INK))
    o.append(T(360, 322, 'n runs from −3 to 3; open dots are zero samples', 13, fill=MUT))
    return 340, ''.join(o)


FIG[2] = (f2, 'The sequence x[n] = 1, 2, 3 at n = 0, 1, 2 split into its even part (mirror image about n = 0) and its odd part '
              '(mirror image with a sign change). The two parts add back to x[n], and their energies 7.5 and 6.5 add to the energy 14.',
          'Three stem plots. x[n] has values 1, 2, 3 at n = 0, 1, 2. Its even part has 1.5, 1, 1, 1, 1.5 at n = −2 to 2. '
          'Its odd part has −1.5, −1, 0, 1, 1.5 at n = −2 to 2.')


# ---- 1.3 the worked example signal and its derivative ----
def f3():
    o = []
    x0, x1 = 90, 690
    fx = lambda t: x0 + (t + 2) / 5.5 * (x1 - x0)
    # top panel
    yz = 190; fy = lambda v: yz - v * 22
    o.append(T(x0 - 20, 30, 'x(t) = 2u(t+1) − 3u(t−2) + 4' + sup('e', '−2t') + 'u(t)  V', 14, 'start', bold=True))
    o.append(L(x0, yz, x1, yz, L2, 1.5)); o.append(L(fx(0), fy(6.6), fx(0), fy(-1.6), L2, 1.5))
    for v in (2, 4):
        o += [L(fx(0) - 5, fy(v), fx(0), fy(v), L2, 1.5), T(fx(0) + 8, fy(v) + 4.5, str(v), 13, 'start', MUT)]
    pts = [(fx(-2), fy(0)), (fx(-1), fy(0)), (fx(-1), fy(2)), (fx(0), fy(2)), (fx(0), fy(6))]
    pts += [(fx(t / 50), fy(2 + 4 * math.exp(-2 * t / 50))) for t in range(1, 100)]
    pts += [(fx(2), fy(-1 + 4 * math.exp(-4))), (fx(2), fy(-1 + 4 * math.exp(-4)))]
    pts2 = [(fx(2 + t / 50), fy(-1 + 4 * math.exp(-2 * (2 + t / 50)))) for t in range(0, 76)]
    o.append(P(pts, AC, 2.5)); o.append(P([(fx(1.98), fy(2 + 4 * math.exp(-3.96)))] + pts2, AC, 2.5))
    o.append(L(fx(2), fy(2.07), fx(2), fy(-0.93), AC, 1.5, '4 4'))
    for t in (-2, -1, 1, 2, 3):
        o += [L(fx(t), yz, fx(t), yz + 5, L2, 1.5), T(fx(t), yz + 44, neg(t).replace('&#8722;', '−'), 13, fill=MUT)]
    o.append(T(fx(0), yz + 44, '0', 13, 'middle', MUT))
    o.append(T(x1, yz + 66, 't (s)', 14, 'end', MUT))
    o.append(C(fx(0), fy(6), 6, NX)); o.append(Tb(fx(0) + 12, fy(6) + 5, 'x(0) = 6 V', 14, 'start', NX, bold=True))
    o.append(C(fx(3), fy(-0.99), 6, NX)); o.append(Tb(fx(3) - 4, yz - 14, 'x(3) ≈ −0.990 V', 14, 'middle', NX, bold=True))
    o.append(Tb(fx(-1) + 4, fy(2) - 12, 'step up 2 at t = −1', 13, 'middle', MUT))
    o.append(Tb(fx(2) + 10, fy(2.07) - 10, 'step down 3 at t = 2', 13, 'start', MUT))
    # bottom panel: derivative
    yb = 410; gy = lambda v: yb - v * 13
    o.append(T(x0 - 20, 300, 'dx/dt = 2δ(t+1) + 4δ(t) − 3δ(t−2) − 8' + sup('e', '−2t') + 'u(t)  V/s', 14, 'start', bold=True))
    o.append(L(x0, yb, x1, yb, L2, 1.5))
    for t in (-2, -1, 1, 2, 3):
        o += [L(fx(t), yb, fx(t), yb + 5, L2, 1.5)]
    o.append(L(fx(-1), yb, fx(-1), gy(2) , LV, 3, arrow='l')); o.append(T(fx(-1), gy(2) - 10, 'area 2', 13, fill=LV, bold=True))
    o.append(L(fx(0), yb, fx(0), gy(4), LV, 3, arrow='l')); o.append(T(fx(0), gy(4) - 10, 'area 4', 13, fill=LV, bold=True))
    o.append(L(fx(2), yb, fx(2), gy(-3), NX, 3, arrow='x')); o.append(T(fx(2) + 8, gy(-3) + 14, 'area −3', 13, 'start', NX, bold=True))
    o.append(P([(fx(0), yb)] + [(fx(t / 50), gy(-8 * math.exp(-2 * t / 50))) for t in range(0, 176)], AC, 2.5))
    o.append(Tb(fx(0.55), gy(-6.2), '−8' + sup('e', '−2t') + ' from the decay', 13, 'start', AC))
    o.append(T(fx(0) - 6, gy(-8) + 5, '−8', 13, 'end', MUT))
    return 530, ''.join(o)


FIG[3] = (f3, 'Top: the worked example’s voltage, built from two shifted steps and a switched-on exponential, with x(0) = 6 V and x(3) ≈ −0.990 V marked. '
              'Bottom: its derivative. Each jump becomes an impulse whose area is the jump height; the smooth decay gives the curve −8e⁻²ᵗ u(t).',
          'Top plot: x(t) is 0 before t = −1, 2 from −1 to 0, jumps to 6 at t = 0 and decays towards 2, drops by 3 at t = 2 and settles near −1. '
          'Bottom plot: impulses of area 2 at t = −1, 4 at t = 0 and −3 at t = 2, and a negative exponential starting at −8.')


# ---- 1.4 shift, scale and reversal of a pulse ----
def f4():
    o = []
    x0, x1 = 215, 690
    fx = lambda t: x0 + (t + 2) / 5 * (x1 - x0)
    rows = [('x(t)', 0, 2, AC, 'width 2 s'), ('x(2t − 1)', 0.5, 1.5, LV, 'width 1 s, delay 0.5 s'),
            ('x(−t + 1)', -1, 1, NX, 'reversed, then delay 1 s')]
    for i, (name, a, b, col, note) in enumerate(rows):
        yz = 100 + i * 110
        o.append(T(20, yz - 14, name, 15, 'start', col, bold=True))
        o.append(T(20, yz + 6, note, 13, 'start', MUT))
        o.append(L(x0, yz, x1, yz, L2, 1.5))
        o.append(L(fx(0), yz + 6, fx(0), yz - 62, L2, 1.2, '3 4'))
        o.append(P([(fx(a), yz), (fx(a), yz - 50), (fx(b), yz - 50), (fx(b), yz)], col, 2.8, fill=('var(--accent-soft)' if col == AC else 'var(--live-soft)' if col == LV else 'var(--next-soft)')))
        o.append(T((fx(a) + fx(b)) / 2, yz - 58, 'height 2', 13, fill=MUT))
        for t in (a, b):
            o.append(Tb(fx(t), yz + 20, (('−' if t < 0 else '') + ('%g' % abs(t))), 13, 'middle', INK, bold=True))
    o.append(T(x1, 100 + 2 * 110 + 44, 't (s)', 14, 'end', MUT))
    o.append(T(fx(0), 30, 't = 0', 13, fill=MUT))
    return 380, ''.join(o)


FIG[4] = (f4, 'The pulse of height 2 on 0 to 2 s (top) after the two operations of the worked example. x(2t − 1) = x(2(t − 0.5)) is half as wide and '
              'starts at 0.5 s; x(−t + 1) = x(−(t − 1)) is the mirror image moved right by 1 s, on −1 to 1 s.',
          'Three rectangular pulses of height 2 on one time axis: x(t) from 0 to 2 s, x(2t − 1) from 0.5 to 1.5 s, and x(−t + 1) from −1 to 1 s.')


# ---- 1.5 a CT system and a DT system with the worked example's inputs ----
def f5():
    o = []
    # CT row
    def mini_axes(x, y, w):
        return L(x, y, x + w, y, L2, 1.5)
    yz = 130
    o.append(T(20, 30, 'CT system: signals defined for every real t', 14, 'start', bold=True))
    o.append(mini_axes(30, yz, 170)); o.append(P([(30, yz), (100, yz), (100, yz - 40), (200, yz - 40)], AC, 2.5))
    o.append(T(100, yz + 20, '0', 13, fill=MUT)); o.append(T(160, yz + 20, '1', 13, fill=MUT)); o.append(L(160, yz, 160, yz + 5, L2, 1.5))
    o.append(T(115, 70, 'x(t) = u(t)', 14, bold=True, fill=AC)); o.append(T(208, yz - 36, '1', 13, 'start', MUT))
    o.append(L(220, yz - 30, 262, yz - 30, MUT, 2, arrow='m'))
    o.append(boxt(268, yz - 70, 190, 80, ['y(t) = 3x(t) + 2', 'memoryless: uses x(t) only'], size=14))
    o.append(L(462, yz - 30, 504, yz - 30, MUT, 2, arrow='m'))
    o.append(mini_axes(512, yz, 180)); o.append(P([(512, yz - 20), (582, yz - 20), (582, yz - 50), (692, yz - 50)], NX, 2.5))
    o.append(T(582, yz + 20, '0', 13, fill=MUT)); o.append(L(642, yz, 642, yz + 5, L2, 1.5)); o.append(T(642, yz + 20, '1', 13, fill=MUT))
    o.append(C(642, yz - 50, 6, NX)); o.append(T(642, yz - 62, 'y(1) = 5', 14, fill=NX, bold=True))
    o.append(T(540, yz - 28, '2', 13, fill=MUT))
    # DT row
    yz = 330
    o.append(T(20, 210, 'DT system: signals defined only at integer n', 14, 'start', bold=True))
    xs = {n: 60 + (n + 1) * 34 for n in range(-1, 4)}
    o.append(mini_axes(40, yz, 170))
    for n in range(-1, 4):
        v = max(n, 0)
        o.append(stem(xs[n], yz, yz - v * 18, AC) if v else C(xs[n], yz, 4, AC))
        o.append(T(xs[n], yz + 20, str(n).replace('-', '−'), 13, fill=MUT))
    o.append(T(130, 250, 'x[n] = n u[n]', 14, bold=True, fill=AC))
    o.append(L(220, yz - 30, 262, yz - 30, MUT, 2, arrow='m'))
    o.append(boxt(268, yz - 70, 190, 80, ['y[n] = x[n] − x[n−1]', 'memory: needs x[n−1]'], size=14))
    o.append(L(462, yz - 30, 504, yz - 30, MUT, 2, arrow='m'))
    ys = {n: 530 + (n + 1) * 36 for n in range(-1, 4)}
    o.append(mini_axes(512, yz, 180))
    yv = {-1: 0, 0: 0, 1: 1, 2: 1, 3: 1}
    for n in range(-1, 4):
        v = yv[n]
        o.append(stem(ys[n], yz, yz - v * 30, NX if n == 2 else LV) if v else C(ys[n], yz, 4, LV))
        o.append(T(ys[n], yz + 20, str(n).replace('-', '−'), 13, fill=MUT))
    o.append(T(ys[2], yz - 44, 'y[2] = 2 − 1 = 1', 14, fill=NX, bold=True))
    return 370, ''.join(o)


FIG[5] = (f5, 'The two systems of the worked example with their inputs and outputs. The CT system only rescales and lifts the present value, '
              'so y(1) = 5; the DT system subtracts the previous sample, so the ramp n u[n] becomes 0, 1, 1, 1 and y[2] = 1.',
          'Top row: a unit step enters the block y(t) = 3x(t) + 2 and leaves as a step from 2 to 5, with y(1) = 5. Bottom row: the ramp samples '
          '0, 0, 1, 2, 3 enter y[n] = x[n] − x[n−1] and leave as 0, 0, 1, 1, 1, with y[2] = 1.')


# ---- 1.6 testing y(t) = t x(t) ----
def f6():
    o = []
    x0, x1, y0, y1 = 80, 680, 60, 330
    fx = lambda t: x0 + t / 10 * (x1 - x0)
    fy = lambda v: y1 - v / 22 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 2, 4, 6, 8, 10], [0, 5, 10, 15, 20], fx, fy, 't (s)', 'value'))
    o.append(P([(fx(0), fy(2)), (fx(10), fy(2))], MUT, 2.5, '7 5'))
    o.append(Tb(fx(6.2), fy(2) - 8, 'input x(t) = 2 V (bounded)', 13, 'middle', MUT))
    o.append(P([(fx(0), fy(0)), (fx(10), fy(20))], AC, 3))
    o.append(P([(fx(1), fy(0)), (fx(10), fy(18))], NX, 3, '9 5'))
    o.append(Tb(fx(6.9), fy(14.8) - 6, 'T{x(t − 1)} = 2t', 14, 'end', AC, bold=True))
    o.append(Tb(fx(7.5), fy(11.5) + 18, 'y(t − 1) = 2(t − 1)', 14, 'start', NX, bold=True))
    o.append(C(fx(2), fy(4), 6, AC)); o.append(C(fx(2), fy(2), 6, NX))
    o.append(Tb(fx(2) - 12, fy(4) - 6, '4 V·s', 13, 'end', AC, bold=True))
    o.append(Tb(fx(2) + 12, fy(2) + 22, '2 V·s', 13, 'start', NX, bold=True))
    o.append(Tb(fx(0.25), fy(12.5), 'at t = 2 s: 4 ≠ 2, so time-varying', 13, 'start', INK))
    o.append(C(fx(10), fy(20), 6, AC))
    o.append(Tb(fx(10) - 12, fy(20) - 2, 'y = 20 V·s at t = 10 s, still rising: not BIBO stable', 13, 'end', INK))
    return 380, ''.join(o)


FIG[6] = (f6, 'The two time-invariance results for y(t) = t x(t) with the constant input 2 V and delay 1 s. The delayed-input output 2t and the '
              'delayed output 2(t − 1) differ (4 against 2 V·s at t = 2 s), and the output keeps growing although the input stays at 2 V.',
          'A plot from t = 0 to 10 s. A dashed level line at 2 for the input. A solid line 2t and a dashed line 2(t − 1); at t = 2 s they are 4 and 2. '
          'The solid line reaches 20 at t = 10 s.')


# ---- 1.7 best approximation of a square wave by sin t ----
def f7():
    o = []
    x0, x1 = 80, 680
    fx = lambda t: x0 + t / (2 * PI) * (x1 - x0)
    yz = 190; fy = lambda v: yz - v * 95
    c = 4 / PI
    # error region between the square wave and c sin t
    for a, s in ((0, 1), (PI, -1)):
        top = [(fx(a + PI * i / 60), fy(s)) for i in range(61)]
        bot = [(fx(a + PI * i / 60), fy(c * math.sin(a + PI * i / 60))) for i in range(60, -1, -1)]
        o.append(f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in top + bot)}" style="fill:var(--next-soft);stroke:none"/>')
    o.append(L(x0, yz, x1, yz, L2, 1.5)); o.append(L(x0, fy(1.45), x0, fy(-1.45), L2, 1.5))
    for v, lab in ((1, '1'), (-1, '−1'), (c, '1.27'), (-c, '−1.27')):
        o += [L(x0 - 5, fy(v), x0, fy(v), L2, 1.5), T(x0 - 9, fy(v) + 4.5, lab, 13, 'end', MUT)]
    o.append(P([(fx(0), fy(1)), (fx(PI), fy(1)), (fx(PI), fy(-1)), (fx(2 * PI), fy(-1))], AC, 3))
    o.append(P([(fx(2 * PI * i / 200), fy(c * math.sin(2 * PI * i / 200))) for i in range(201)], LV, 3))
    for t, lab in ((PI / 2, 'π/2'), (PI, 'π'), (3 * PI / 2, '3π/2'), (2 * PI, '2π')):
        o += [L(fx(t), yz, fx(t), yz + 5, L2, 1.5), (Tb(fx(t) + 16, yz + 20, lab, 13, 'middle', MUT) if t == PI else T(fx(t), yz + 20, lab, 13, fill=MUT))]
    o.append(T(x1, yz + 40, 't', 14, 'end', MUT))
    o.append(Tb(fx(PI / 2), fy(1) - 52, 'f(t) = +1 on (0, π)', 14, 'middle', AC, bold=True))
    o.append(Tb(fx(3 * PI / 2), fy(0.35), 'f(t) = −1 on (π, 2π)', 14, 'middle', AC, bold=True))
    o.append(Tb(fx(2 * PI), fy(1.2), '(4/π) sin t ≈ 1.27 sin t', 14, 'end', LV, bold=True))
    o.append(Tb(fx(0.17 * PI) + 4, fy(0.45), 'error', 13, 'start', NX, bold=True))
    o.append(T(360, 352, 'c₁₂ = 4/π ≈ 1.273;  error energy 2π − 16/π ≈ 1.190, about 19 % of the energy 2π', 14, fill=INK))
    return 370, ''.join(o)


FIG[7] = (f7, 'The square wave f(t) and its best single-term approximation c₁₂ sin t with c₁₂ = 4/π ≈ 1.27. The shaded gap is the error signal; '
              'its energy, about 1.19 of the total 2π, is the smallest any multiple of sin t can leave.',
          'A square wave equal to +1 from 0 to π and −1 from π to 2π, with the sine curve 1.27 sin t drawn over it and the gaps between them shaded.')


# ---- 1.8 adding terms of a complete set ----
def f8():
    o = []
    x0, x1 = 80, 680
    fx = lambda t: x0 + t / (2 * PI) * (x1 - x0)
    yz = 140; fy = lambda v: yz - v * 75
    o.append(T(x0, 30, 'Square wave and its first three sine terms (n = 1, 3, 5)', 14, 'start', bold=True))
    o.append(L(x0, yz, x1, yz, L2, 1.5)); o.append(L(x0, fy(1.4), x0, fy(-1.4), L2, 1.5))
    for v, lab in ((1, '1'), (-1, '−1')):
        o += [L(x0 - 5, fy(v), x0, fy(v), L2, 1.5), T(x0 - 9, fy(v) + 4.5, lab, 13, 'end', MUT)]
    o.append(P([(fx(0), fy(1)), (fx(PI), fy(1)), (fx(PI), fy(-1)), (fx(2 * PI), fy(-1))], AC, 2.5))
    s3 = lambda t: 4 / PI * (math.sin(t) + math.sin(3 * t) / 3 + math.sin(5 * t) / 5)
    o.append(P([(fx(2 * PI * i / 400), fy(s3(2 * PI * i / 400))) for i in range(401)], LV, 2.5))
    for t, lab in ((PI, 'π'), (2 * PI, '2π')):
        o += [L(fx(t), yz, fx(t), yz + 5, L2, 1.5), T(fx(t) + 12, yz + 20, lab, 13, fill=MUT)]
    o.append(Tb(fx(1.5 * PI), fy(0.5), '(4/π)(sin t + sin 3t/3 + sin 5t/5)', 13, 'middle', LV, bold=True))
    # bars: energy captured
    by = 470; bh = 170
    o.append(T(x0, 268, 'Share of the energy 2π carried by the terms kept', 14, 'start', bold=True))
    o.append(L(x0, by, x1, by, L2, 1.5))
    o.append(L(x0, by - bh, x1, by - bh, LN, 1, '4 4')); o.append(T(x0 - 8, by - bh + 4.5, '100 %', 13, 'end', MUT))
    o.append(T(x0 - 8, by + 4.5, '0', 13, 'end', MUT))
    data = [('n = 1', 81.06), ('1, 3', 90.06), ('1, 3, 5', 93.31), ('1 to 7', 94.96), ('1 to 9', 95.96)]
    for i, (lab, pc) in enumerate(data):
        bx = 120 + i * 112
        h = bh * pc / 100
        o.append(R(bx, by - h, 70, h, ACS if i else LVS, AC if i else LV, 3))
        o.append(T(bx + 35, by - h - 8, f'{pc:.2f} %', 13, bold=True))
        o.append(T(bx + 35, by + 20, lab, 13, fill=MUT))
    o.append(T(360, by + 44, 'each new term adds |cₙ|²Kₙ; the error energy 2π minus the sum falls towards 0', 13, fill=MUT))
    return 530, ''.join(o)


FIG[8] = (f8, 'Top: three terms of the sine set already follow the square wave closely. Bottom: the share of its energy 2π that the kept terms carry, '
              'from the worked example’s table; the shares rise towards 100 %, as completeness and Parseval’s relation promise.',
          'Top: a square wave with the three-term sine sum wiggling around it. Bottom: five bars of energy share, 81.06, 90.06, 93.31, 94.96 and 95.96 percent, '
          'for 1, 2, 3, 4 and 5 odd harmonics.')


spec = make_spec(FIG)
