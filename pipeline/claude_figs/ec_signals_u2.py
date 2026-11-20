"""Claude's hand-drawn figures for ec-signals-u2 (Signals and Systems: continuous-time LTI systems), one per chapter,
each drawn from that chapter's own worked example and numbers."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
E = math.exp


def arrow(x1, y1, x2, y2, c=AC, w=2, m='n'):
    return L(x1, y1, x2, y2, c, w, arrow=m)


def curve(f, a, b, fx, fy, n=80, c=AC, w=2.5, dash=None):
    pts = [(fx(a + (b - a) * i / n), fy(f(a + (b - a) * i / n))) for i in range(n + 1)]
    return P(pts, c, w, dash)


def area(f, a, b, fx, fy, y0, n=60, c=ACS):
    pts = [(fx(a), y0)] + [(fx(a + (b - a) * i / n), fy(f(a + (b - a) * i / n))) for i in range(n + 1)] + [(fx(b), y0)]
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" style="fill:{c};stroke:none"/>'


# ---- 2.1 the two tests on y = 3x + 2 ----
def f1():
    o = []
    bw, bh = 118, 40

    def box(x, y, lines, stroke=AC, fill=PANEL, w=bw):
        return boxt(x, y, w, bh, lines, fill, stroke, 14)

    # linearity panel
    o.append(T(20, 30, 'Linearity test: x₁ = 1, x₂ = 2, a = 2, b = 3', 15, 'start', bold=True))
    y1, y2 = 50, 108
    o.append(T(20, y1 + 25, 'combine first', 13, 'start', MUT))
    o.append(box(130, y1, ['2(1) + 3(2) = 8'], w=140))
    o.append(arrow(270, y1 + 20, 318, y1 + 20))
    o.append(box(320, y1, ['T: 3x + 2']))
    o.append(arrow(438, y1 + 20, 486, y1 + 20))
    o.append(T(500, y1 + 26, '3(8) + 2 = 26', 15, 'start', bold=True))
    o.append(T(20, y2 + 25, 'separately', 13, 'start', MUT))
    o.append(box(130, y2, ['T{1} = 5, T{2} = 8'], w=180))
    o.append(arrow(310, y2 + 20, 358, y2 + 20))
    o.append(box(360, y2, ['2(5) + 3(8)'], w=126))
    o.append(arrow(486, y2 + 20, 520, y2 + 20))
    o.append(T(528, y2 + 26, '34', 15, 'start', bold=True))
    o.append(T(700, y1 + 72, '26 ≠ 34', 16, 'end', LV, True))
    o.append(T(700, y1 + 92, 'not linear', 14, 'end', LV, True))
    o.append(L(20, 178, 700, 178, LN, 1))
    # time-invariance panel
    o.append(T(20, 210, 'Time-invariance test: x(t) = t, delay t₀ = 2 s, read at t = 5 s', 15, 'start', bold=True))
    y3, y4 = 230, 288
    o.append(T(20, y3 + 25, 'delay first', 13, 'start', MUT))
    o.append(box(130, y3, ['delay 2 s'], NX, NXS, 100))
    o.append(T(260, y3 - 6, 't − 2', 13, fill=MUT))
    o.append(arrow(230, y3 + 20, 288, y3 + 20))
    o.append(box(290, y3, ['T: 3x + 2']))
    o.append(arrow(408, y3 + 20, 456, y3 + 20))
    o.append(T(466, y3 + 26, '3t − 4 → 11', 15, 'start', bold=True))
    o.append(T(20, y4 + 25, 'system first', 13, 'start', MUT))
    o.append(box(130, y4, ['T: 3x + 2']))
    o.append(T(278, y4 - 6, '3t + 2', 13, fill=MUT))
    o.append(arrow(248, y4 + 20, 306, y4 + 20))
    o.append(box(308, y4, ['delay 2 s'], NX, NXS, 100))
    o.append(arrow(408, y4 + 20, 456, y4 + 20))
    o.append(T(466, y4 + 26, '3t − 4 → 11', 15, 'start', bold=True))
    o.append(T(700, y3 + 72, '11 = 11', 16, 'end', NX, True))
    o.append(T(700, y3 + 92, 'time-invariant', 14, 'end', NX, True))
    o.append(T(360, 362, 'One test fails, so y(t) = 3x(t) + 2 is not LTI.', 15, bold=True))
    return 380, ''.join(o)
FIG[1] = (f1, 'Each test sends the input through two paths. For y(t)=3x(t)+2 the linearity paths give 26 and 34, so the system is not linear; the delay paths both give 11 at t=5 s, so it is time-invariant, and it is not LTI.',
          'Two panels. Linearity: combining first gives 26, applying the system separately gives 34, so not linear. Time invariance: delay then system and system then delay both give 3t minus 4, which is 11 at t equals 5 s.')


# ---- 2.2 h(t) and s(t) of the RC filter, tau = 1 ms ----
def f2():
    o = []
    # left panel: h(t) in 1/s
    x0, x1, yt, yb = 80, 330, 60, 250
    fx = lambda t: x0 + (x1 - x0) * t / 5
    fy = lambda v: yb - (yb - yt) * v / 1000
    o.append(axes(x0, x1, yt, yb, [0, 1, 2, 3, 4, 5], [0, 500, 1000], fx, fy, 't (ms)', 'h(t) (s⁻¹)'))
    o.append(curve(lambda t: 1000 * E(-t), 0, 5, fx, fy, c=AC))
    o.append(L(fx(1), fy(368), fx(1), yb, L2, 1.5, '4 4'))
    o.append(C(fx(1), fy(368), 5, AC))
    o.append(Tb(fx(1) + 10, fy(368) - 12, '368 at 1 ms', 14, 'start', AC, True))
    o.append(C(fx(0), fy(1000), 5, AC))
    o.append(Tb(fx(0) + 12, fy(1000) + 6, '1000 = 1/τ', 14, 'start', AC, True))
    # right panel: s(t)
    X0, X1 = 430, 690
    gx = lambda t: X0 + (X1 - X0) * t / 5
    gy = lambda v: yb - (yb - yt) * v / 1
    o.append(axes(X0, X1, yt, yb, [0, 1, 2, 3, 4, 5], [0, 0.5, 1], gx, gy, 't (ms)', 's(t)'))
    o.append(curve(lambda t: 1 - E(-t), 0, 5, gx, gy, c=LV))
    o.append(L(gx(1), gy(0.632), gx(1), yb, L2, 1.5, '4 4'))
    for t, v, lab in [(1, 0.632, '0.632'), (3, 0.950, '0.950'), (5, 0.993, '0.993')]:
        o.append(C(gx(t), gy(v), 5, LV))
    o.append(Tb(gx(1) + 10, gy(0.632) + 20, '0.632 at τ', 14, 'start', LV, True))
    o.append(Tb(gx(3), gy(0.95) + 24, '0.950 at 3τ', 13, 'middle', LV, True))
    o.append(T(X1, gy(0.993) - 12, '0.993', 13, 'end', LV, True))
    o.append(T(380, 330, 'The slope of s(t) at any instant is h(t): steep where h is large, flat as h dies out.', 14, bold=True))
    return 348, ''.join(o)
FIG[2] = (f2, 'Impulse response and step response of the RC filter with R=1 kΩ, C=1 μF (τ=1 ms). At t=1 ms, h has fallen to 368 s⁻¹ and s has risen to 0.632; s reaches 0.950 at 3τ.',
          'Left: h(t) falls from 1000 per second at t=0 to 368 at 1 ms. Right: s(t) rises from 0 to 0.632 at 1 ms, 0.950 at 3 ms and 0.993 at 5 ms.')


# ---- 2.3 flip, slide, multiply for x = 2 s pulse and h = e^-t u(t) ----
def f3():
    o = []
    fx = lambda tau: 90 + (tau + 2) * 82          # tau from -2 to 5.5
    rows = [(1, 40, '0.632', 'overlap 0 ≤ τ ≤ 1'), (3, 200, '0.318', 'overlap 0 ≤ τ ≤ 2')]
    for t, top, val, ov in rows:
        yb, H = top + 110, 80
        fy = lambda v, yb=yb: yb - H * v
        o.append(T(20, top + 8, f't = {t} s', 15, 'start', bold=True))
        o.append(xaxis(fx(-2), fx(5.5), yb, [-2, -1, 0, 1, 2, 3, 4, 5], fx, None, neg))
        o.append(T(fx(5.5) + 8, yb + 5, 'τ', 15, 'start', MUT, True))
        lo, hi = 0, min(2, t)
        o.append(area(lambda tau, t=t: E(-(t - tau)), lo, hi, fx, fy, yb))
        o.append(P([(fx(-2), yb), (fx(0), yb), (fx(0), fy(1)), (fx(2), fy(1)), (fx(2), yb)], AC, 2.5))
        o.append(T(fx(1), fy(1) - 8, 'x(τ)', 14, fill=AC, bold=True))
        o.append(curve(lambda tau, t=t: E(-(t - tau)), -2, t, fx, fy, c=LV))
        o.append(L(fx(t), fy(1), fx(t), yb, LV, 2.5))
        o.append(T(fx(t) + 8, fy(1) + 16, f'h({t} − τ)', 14, 'start', LV, True))
        o.append(T(700, top + 8, f'{ov}: area y({t}) = {val}', 14, 'end', INK, True))
    # output panel
    yb, top = 500, 380
    gx = lambda t: 90 + t * 110
    gy = lambda v: yb - 100 * v
    o.append(axes(90, 650, top, yb, [0, 1, 2, 3, 4, 5], [0, 0.5, 1], gx, gy, 't (s)', 'y(t)'))
    y = lambda t: 1 - E(-t) if t < 2 else E(2 - t) - E(-t)
    o.append(curve(y, 0, 5, gx, gy, 120, NX))
    for t, lab, dx, dy, an in [(1, '0.632', 0, 26, 'middle'), (2, '0.865', 12, -8, 'start'), (3, '0.318', 12, -10, 'start')]:
        o.append(C(gx(t), gy(y(t)), 5, NX))
        o.append(T(gx(t) + dx, gy(y(t)) + dy, f'y({t}) = {lab}', 13, an, NX, True))
    return 560, ''.join(o)
FIG[3] = (f3, 'Graphical convolution of the 2 s pulse x(τ) with h(t−τ)=e<sup>−(t−τ)</sup> for τ ≤ t. The shaded overlap area is the output: 0.632 at t=1 s and 0.318 at t=3 s. The bottom plot joins all such areas into y(t), which peaks at 0.865 when the pulse ends at t=2 s.',
          'Two rows show the pulse from 0 to 2 and the flipped exponential ending at tau equals t, for t equals 1 and 3 seconds, with the overlap shaded. The bottom plot shows y(t) rising to 0.865 at 2 s and decaying, with y(1)=0.632 and y(3)=0.318.')


# ---- 2.4 two rectangles give a trapezoid ----
def f4():
    o = []
    # inputs
    sx = lambda t, x0: x0 + t * 40
    for x0, w, name in [(60, 2, 'x(t): width 2 s'), (300, 3, 'h(t): width 3 s')]:
        yb, yt = 120, 70
        o.append(L(x0 - 10, yb, x0 + 170, yb, L2, 1.5))
        o.append(P([(sx(0, x0), yb), (sx(0, x0), yt), (sx(w, x0), yt), (sx(w, x0), yb)], AC, 2.5))
        o.append(T(sx(0, x0), yb + 20, '0', 13, fill=MUT))
        o.append(T(sx(w, x0), yb + 20, str(w), 13, fill=MUT))
        o.append(T(sx(w / 2, x0), yt - 10, '1', 13, fill=MUT))
        o.append(T(x0 + 70, 40, name, 14, bold=True))
    o.append(T(250, 105, '*', 26, bold=True))
    o.append(T(540, 100, 'area 2 × area 3 = 6', 14, 'middle', MUT, True))
    # output
    gx = lambda t: 110 + t * 100
    yb = 370
    gy = lambda v: yb - 75 * v
    o.append(axes(110, 640, 200, yb, [0, 1, 2, 3, 4, 5], [0, 1, 2], gx, gy, 't (s)', 'y(t) = x * h'))
    o.append(area(lambda t: t if t < 2 else (2 if t < 3 else 5 - t), 0, 5, gx, gy, yb, 50))
    o.append(P([(gx(0), gy(0)), (gx(2), gy(2)), (gx(3), gy(2)), (gx(5), gy(0))], NX, 3))
    o.append(T(gx(0.95), gy(1.25) - 6, 'y = t', 14, 'end', NX, True))
    o.append(T(gx(2.5), gy(2) - 12, 'y = 2', 14, fill=NX, bold=True))
    o.append(T(gx(4.05), gy(1.25) - 6, 'y = 5 − t', 14, 'start', NX, True))
    o.append(T(gx(2.5), gy(0.6), 'area 6', 14, fill=INK, bold=True))
    o.append(T(690, 250, 'width', 13, 'end', MUT))
    o.append(T(690, 268, '2 + 3 = 5 s', 13, 'end', MUT, True))
    return 420, ''.join(o)
FIG[4] = (f4, 'A 2 s unit pulse convolved with a 3 s unit pulse. The width rule gives 2+3=5 s, the peak is 1×1×min(2, 3)=2 on the flat top from 2 s to 3 s, and the area is 2×3=6.',
          'Top: a rectangle of width 2 and a rectangle of width 3, both of height 1. Bottom: their convolution, a trapezoid rising as y equals t to 2 at t=2, flat to t=3, and falling as 5 minus t to zero at t=5, with area 6.')


# ---- 2.5 causal or not, stable or not ----
def f5():
    o = []
    cells = [
        (0, 0, lambda t: E(-2 * t) if t >= 0 else 0, 'e⁻²ᵗu(t)', 'area = 1/2'),
        (0, 1, lambda t: 1 if t >= 0 else 0, 'u(t)', 'area = ∞'),
        (1, 0, lambda t: E(2 * t) if t <= 0 else 0, 'e²ᵗu(−t)', 'area = 1/2'),
        (1, 1, lambda t: min(0.15 * E(-t), 1.2) if t <= 0 else 0, 'e⁻ᵗu(−t)', 'area = ∞'),
    ]
    o.append(T(270, 34, 'BIBO stable', 15, bold=True, fill=NX))
    o.append(T(560, 34, 'unstable', 15, bold=True, fill=LV))
    o.append(T(60, 140, 'causal', 15, bold=True))
    o.append(T(60, 330, 'noncausal', 15, bold=True))
    for r, c, f, name, ar in cells:
        x0 = 140 + c * 290; y0 = 50 + r * 190
        o.append(R(x0, y0, 270, 170, PANEL, L2, 10, 1.5))
        fx = lambda t, x0=x0: x0 + 135 + t * 40
        yb = y0 + 125
        fy = lambda v, yb=yb: yb - 70 * v
        o.append(L(fx(-3), yb, fx(3), yb, L2, 1.5))
        o.append(L(fx(0), yb + 4, fx(0), y0 + 40, L2, 1.5, '3 3'))
        o.append(T(fx(0), yb + 20, '0', 13, fill=MUT))
        o.append(T(fx(3) - 4, yb + 20, 't', 13, fill=MUT))
        col = NX if c == 0 else LV
        lo = -2.05 if (r, c) == (1, 1) else -3
        o.append(area(f, lo, 3, fx, fy, yb, 120, NXS if c == 0 else LVS))
        o.append(curve(f, lo, -0.001, fx, fy, 60, col))
        o.append(curve(f, 0.001, 3, fx, fy, 60, col))
        if f(0.001) > 0 and f(-0.001) == 0: o.append(L(fx(0), yb, fx(0), fy(f(0.001)), col, 2.5))
        if f(-0.001) > 0 and f(0.001) == 0: o.append(L(fx(0), yb, fx(0), fy(f(-0.001)), col, 2.5))
        if r == 1 and c == 1: o.append(T(x0 + 70, y0 + 56, '↑ grows without limit', 13, 'start', col, True))
        if r == 0 and c == 1: o.append(T(fx(1.5), yb - 22, 'stays at 1 forever', 13, 'middle', col, True))
        o.append(T(x0 + 12, y0 + 24, name, 15, 'start', INK, True))
        o.append(T(x0 + 258, y0 + 24, ar, 14, 'end', col, True))
    return 440, ''.join(o)
FIG[5] = (f5, 'One impulse response of each kind. The rows ask where h(t) lives (zero for t<0 means causal); the columns ask whether the area under |h(t)| is finite (BIBO stable). Neither property decides the other.',
          'Two by two grid. Causal and stable: e to the minus 2t times u(t), area one half. Causal and unstable: u(t), area infinite. Noncausal and stable: e to the 2t times u of minus t, area one half. Noncausal and unstable: e to the minus t times u of minus t, area infinite.')


# ---- 2.6 the RC circuit and its two step responses ----
def f6():
    o = []
    # circuit: source on the left, R on top, C on the right, ground at the bottom
    xl, xr, yt, ybt = 60, 250, 90, 250
    o.append(L(xl, yt, 110, yt, INK, 2))
    zz = [(110, yt)] + [(118 + 10 * i, yt + (-9 if i % 2 == 0 else 9)) for i in range(6)] + [(178, yt)]
    o.append(P(zz, INK, 2))
    o.append(L(178, yt, xr, yt, INK, 2))
    o.append(T(144, yt - 20, 'R = 1 kΩ', 14, bold=True))
    o.append(L(xr, yt, xr, 160, INK, 2))
    o.append(L(xr - 22, 160, xr + 22, 160, INK, 3))
    o.append(L(xr - 22, 172, xr + 22, 172, INK, 3))
    o.append(L(xr, 172, xr, ybt, INK, 2))
    o.append(T(xr - 30, 171, 'C = 1 μF', 14, 'end', bold=True))
    o.append(L(xl, ybt, xr, ybt, INK, 2))
    o.append(L(xl, yt, xl, 145, INK, 2))
    o.append(L(xl, 195, xl, ybt, INK, 2))
    o.append(f'<circle cx="{xl}" cy="170" r="25" style="fill:var(--panel);stroke:var(--ink);stroke-width:2"/>')
    o.append(T(xl, 165, '+', 15, bold=True)); o.append(T(xl, 187, '−', 15, bold=True))
    o.append(T(xl, 290, 'x(t) = u(t) V', 14, bold=True))
    o.append(T(xr + 28, yt + 34, '+', 15, 'start', AC, True))
    o.append(T(xr + 28, ybt - 10, '−', 15, 'start', AC, True))
    o.append(T(xr + 28, 176, 'y(t)', 15, 'start', AC, True))
    o.append(T(150, 320, 'RC dy/dt + y = x,  τ = 1 ms', 14, bold=True))
    # plot
    x0, x1, ytp, yb = 380, 690, 50, 260
    gx = lambda t: x0 + (x1 - x0) * t / 5
    gy = lambda v: yb - (yb - ytp) * v
    o.append(axes(x0, x1, ytp, yb, [0, 1, 2, 3, 4, 5], [0, 0.4, 1], gx, gy, 't (ms)', 'y(t) (V)'))
    o.append(curve(lambda t: 1 - E(-t), 0, 5, gx, gy, c=AC))
    o.append(curve(lambda t: 1 - 0.6 * E(-t), 0, 5, gx, gy, c=LV, dash='7 5'))
    o.append(L(gx(1), gy(0.779), gx(1), yb, L2, 1.5, '4 4'))
    o.append(C(gx(1), gy(0.632), 5, AC)); o.append(C(gx(1), gy(0.779), 5, LV))
    o.append(Tb(gx(1) + 10, gy(0.632) + 18, '0.632 V', 14, 'start', AC, True))
    o.append(Tb(gx(1) - 6, gy(0.779) - 12, '0.779 V', 14, 'end', LV, True))
    o.append(T(x1, gy(0.32), 'y(0) = 0 (example 1)', 13, 'end', AC, True))
    o.append(T(x1, gy(0.2), 'y(0) = 0.4 V (example 2)', 13, 'end', LV, True))
    return 340, ''.join(o)
FIG[6] = (f6, 'The series RC circuit of the worked examples and its step responses. From rest the capacitor voltage reaches 0.632 V at t=τ=1 ms; starting from 0.4 V it reaches 0.779 V. Both settle at the 1 V source.',
          'Left: a 1 V step source in series with a 1 kilohm resistor and a 1 microfarad capacitor; the output y(t) is across the capacitor. Right: y(t) rising from 0 to 0.632 V at 1 ms, and a dashed curve from 0.4 V to 0.779 V at 1 ms, both approaching 1 V.')


# ---- 2.7 block diagram of the state model of y'' + 3y' + 2y = u ----
def f7():
    o = []
    yc = 90
    o.append(T(40, yc + 5, 'u(t)', 15, 'middle', INK, True))
    o.append(arrow(62, yc, 128, yc))
    o.append(T(112, yc - 8, '+', 15, bold=True))
    o.append(f'<circle cx="150" cy="{yc}" r="20" style="fill:var(--panel);stroke:var(--accent);stroke-width:2"/>')
    o.append(T(150, yc + 6, 'Σ', 17, bold=True))
    o.append(arrow(170, yc, 238, yc))
    o.append(T(205, yc - 10, 'x₂′', 15, bold=True, fill=AC))
    o.append(boxt(240, yc - 24, 64, 48, ['∫'], PANEL, AC, 20))
    o.append(arrow(304, yc, 398, yc))
    o.append(T(350, yc - 10, 'x₂ = y′', 15, bold=True, fill=AC))
    o.append(boxt(400, yc - 24, 64, 48, ['∫'], PANEL, AC, 20))
    o.append(arrow(464, yc, 620, yc))
    o.append(T(545, yc - 10, 'x₁ = y', 15, bold=True, fill=NX))
    o.append(T(640, yc + 5, 'y(t)', 15, 'start', INK, True))
    # feedback from x2 through gain 3
    o.append(L(360, yc, 360, 170, LV, 2))
    o.append(arrow(360, 170, 302, 170, LV, 2, 'l'))
    o.append(boxt(240, 150, 60, 40, ['3'], LVS, LV, 15))
    o.append(L(240, 170, 150, 170, LV, 2))
    o.append(arrow(150, 170, 150, yc + 22, LV, 2, 'l'))
    o.append(T(162, yc + 44, '−', 17, 'start', LV, True))
    # feedback from x1 through gain 2
    o.append(L(560, yc, 560, 240, LV, 2))
    o.append(arrow(560, 240, 422, 240, LV, 2, 'l'))
    o.append(boxt(360, 220, 60, 40, ['2'], LVS, LV, 15))
    o.append(L(360, 240, 120, 240, LV, 2))
    o.append(L(120, 240, 120, yc + 30, LV, 2))
    o.append(arrow(120, yc + 30, 136, yc + 15, LV, 2, 'l'))
    o.append(T(108, yc + 46, '−', 17, 'end', LV, True))
    o.append(T(360, 300, 'x₂′ = u − 3x₂ − 2x₁   and   x₁′ = x₂', 15, bold=True))
    o.append(T(360, 326, 'A = [0 1; −2 −3],  B = [0; 1],  C = [1 0],  D = 0', 14, fill=MUT, bold=True))
    return 346, ''.join(o)
FIG[7] = (f7, 'The state model of y″+3y′+2y=u as a block diagram. Each integrator output is one state: x₂=y′ and x₁=y. The feedback gains 3 and 2 enter the summing junction with minus signs, which gives the last row [−2 −3] of A.',
          'Block diagram: u enters a summing junction, whose output x2 prime feeds an integrator giving x2 equal to y prime, then a second integrator giving x1 equal to y. x2 is fed back through gain 3 and x1 through gain 2, both with minus signs, into the summing junction.')

AFTER = {1: 2, 2: 2, 3: 2, 4: 2, 5: 3, 6: 1, 7: 2}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'after_section': AFTER[k], 'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}


def text_fixes(k):
    # the chapter text is rewritten in the state on the branch (correction pass); nothing to patch here
    return []
