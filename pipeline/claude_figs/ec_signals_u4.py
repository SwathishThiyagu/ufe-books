"""Claude's hand-drawn figures for ec-signals-u4 (Laplace transform analysis), one per chapter, plus the pole sketch in the
second-order model answer. Every number comes from the chapter's own worked example. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def cross(x, y, c=INK, r=7, w=3):
    return L(x - r, y - r, x + r, y + r, c, w) + L(x - r, y + r, x + r, y - r, c, w)


def ring(x, y, r=7, c=INK):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:var(--fig);stroke:{c};stroke-width:2.5"/>'


def splane(x0, x1, y0, y1, fx, ys, labels=True):
    """sigma axis at height ys, j-omega axis at sigma = 0"""
    o = [L(x0, ys, x1, ys, L2, 1.5, arrow='m'), L(fx(0), y1, fx(0), y0, L2, 1.5, arrow='m')]
    if labels:
        o += [T(x1 - 4, ys + 20, 'σ', 15, 'end', MUT, italic=True), T(fx(0) + 8, y0 + 14, 'jω', 15, 'start', MUT, italic=True)]
    return ''.join(o)


# ---- 4.1: the three ROC shapes for a = 2 and the two-sided worked example ----
def f1():
    o = []
    W, G, M = 216, 18, 18
    y0, y1, ys = 46, 196, 122
    cases = [
        ('e⁻²ᵗu(t)', [-2], (-2, None), 'ROC: Re(s) &gt; −2', 'contains the jω axis'),
        ('−e⁻²ᵗu(−t)', [-2], (None, -2), 'ROC: Re(s) &lt; −2', 'misses the jω axis'),
        ('e⁻²ᵗu(t) + e³ᵗu(−t)', [-2, 3], (-2, 3), 'ROC: −2 &lt; Re(s) &lt; 3', 'contains the jω axis'),
    ]
    for i, (title, poles, (lo, hi), roc, note) in enumerate(cases):
        x0 = M + i * (W + G); x1 = x0 + W; cx = x0 + W / 2
        fx = lambda v, cx=cx: cx + 24 * v
        a = fx(lo) if lo is not None else x0
        b = fx(hi) if hi is not None else x1
        o.append(R(x0, y0 - 6, W, y1 - y0 + 12, FIGBG, L2, 6, 1))
        o.append(f'<rect x="{a:.1f}" y="{y0:.1f}" width="{b - a:.1f}" height="{y1 - y0:.1f}" style="fill:{ACS}"/>')
        for v in (lo, hi):
            if v is not None: o.append(L(fx(v), y0, fx(v), y1, AC, 2, '6 4'))
        o.append(splane(x0 + 6, x1 - 6, y0, y1, fx, ys))
        for p in poles:
            o.append(cross(fx(p), ys, NX))
            o.append(Tb(fx(p), ys + 24, neg(p), 13, fill=INK))
        o.append(T(cx, 30, title, 15, bold=True))
        o.append(T(cx, 222, roc, 14))
        o.append(T(cx, 242, note, 13, fill=MUT))
    return 256, ''.join(o)


FIG[1] = (f1, 'Three signals and their ROCs in the s-plane (× is a pole, the shaded part is the ROC). The first two share X(s) = 1/(s + 2) but lie on opposite sides of the pole at −2; the two-sided signal of the worked example has the strip between −2 and 3, which contains the jω axis, so its Fourier transform exists.',
          's-planes for e to the minus 2t u(t) with ROC right of minus 2, minus e to the minus 2t u(minus t) with ROC left of minus 2, and the two-sided signal with ROC between minus 2 and 3.')


# ---- 4.2: shift in s, e^(-3t)cos(4t)u(t) ----
def f2():
    o = []
    # time plot
    X0, X1, Y0, Y1 = 66, 404, 40, 236
    fx = lambda t: X0 + (X1 - X0) * t / 1.6
    fy = lambda v: (Y0 + Y1) / 2 - (Y1 - Y0) / 2 * v
    o.append(axes(X0, X1, Y0, Y1, [0, 0.4, 0.8, 1.2, 1.6], [-1, 0, 1], fx, fy, 't (s)', 'x(t)', lambda v: f'{v:g}', lambda v: neg(f'{v:g}')))
    ts = [i * 0.01 for i in range(161)]
    o.append(P([(fx(t), fy(math.cos(4 * t))) for t in ts], MUT, 1.5, '5 4'))
    o.append(P([(fx(t), fy(math.exp(-3 * t))) for t in ts], LV, 1.8, '3 3'))
    o.append(P([(fx(t), fy(-math.exp(-3 * t))) for t in ts], LV, 1.8, '3 3'))
    o.append(P([(fx(t), fy(math.exp(-3 * t) * math.cos(4 * t))) for t in ts], AC, 3))
    o.append(Tb(fx(1.18), fy(0.93), 'cos(4t)', 13, fill=MUT))
    o.append(Tb(fx(0.42), fy(0.52), 'e⁻³ᵗ', 13, fill=LV))
    o.append(Tb(fx(0.55), fy(-0.42), 'e⁻³ᵗcos(4t)', 13, fill=AC, bold=True))
    # s-plane
    S0, S1, T0, T1 = 452, 706, 40, 236
    sx = lambda v: S0 + 40 + (v + 4) * 40     # sigma -4..1.2
    sy = lambda v: (T0 + T1) / 2 - v * 20     # j omega -4.6..4.6
    o.append(f'<rect x="{sx(-3):.1f}" y="{T0:.1f}" width="{S1 - sx(-3):.1f}" height="{T1 - T0:.1f}" style="fill:{ACS}"/>')
    o.append(L(sx(-3), T0, sx(-3), T1, AC, 2, '6 4'))
    o.append(L(sx(0), T0, sx(0), T1, L2, 1.5, arrow='m'))
    o.append(L(S0, sy(0), S1, sy(0), L2, 1.5, arrow='m'))
    o.append(T(S1 - 4, sy(0) + 20, 'σ', 15, 'end', MUT, italic=True))
    o.append(T(sx(0) + 8, T0 + 4, 'jω', 15, 'start', MUT, italic=True))
    for w in (4, -4):
        o.append(cross(sx(0), sy(w), MUT, 6, 2.5))
        o.append(cross(sx(-3), sy(w), AC))
        o.append(L(sx(0) - 10, sy(w), sx(-3) + 12, sy(w), NX, 2, arrow='x'))
    o.append(Tb(sx(0) + 22, sy(4) + 5, 'j4', 13, 'start', MUT))
    o.append(Tb(sx(0) + 22, sy(-4) + 5, '−j4', 13, 'start', MUT))
    o.append(Tb(sx(-3), sy(0) + 20, '−3', 13))
    o.append(Tb(sx(-1.5), sy(4) + 26, 'shift by −3', 13, fill=NX))
    o.append(T((S0 + S1) / 2, T1 + 30, 'poles −3 ± j4; ROC Re(s) &gt; −3', 14))
    return 284, ''.join(o)


FIG[2] = (f2, 'Left: multiplying cos(4t) by e⁻³ᵗ keeps the 4 rad/s oscillation inside a shrinking envelope ±e⁻³ᵗ. Right: in the s-plane the same step moves the poles from ±j4 to −3 ± j4 and the ROC edge from 0 to −3.',
          'Plot of cos 4t, the envelope e to the minus 3t and the damped cosine, and an s-plane showing poles moving from plus and minus j4 to minus 3 plus and minus j4.')


# ---- 4.3: one X(s), three ROCs ----
def f3():
    o = []
    x0, x1 = 30, 690
    fx = lambda v: x0 + (v + 5) * (x1 - x0) / 6.5     # sigma -5 .. 1.5
    y0, y1, ys = 52, 168, 118
    bands = [(-5, -3, NXS, 'Re(s) &lt; −3', 'left-sided', '−(e⁻ᵗ + 2e⁻³ᵗ)u(−t)', 'no Fourier transform'),
             (-3, -1, LVS, '−3 &lt; Re(s) &lt; −1', 'two-sided', '−e⁻ᵗu(−t) + 2e⁻³ᵗu(t)', 'no Fourier transform'),
             (-1, 1.5, ACS, 'Re(s) &gt; −1', 'right-sided', '(e⁻ᵗ + 2e⁻³ᵗ)u(t)', 'contains the jω axis')]
    for a, b, fill, roc, side, xt, note in bands:
        A, B = fx(a), fx(b); cx = (A + B) / 2
        o.append(f'<rect x="{A + 1:.1f}" y="{y0:.1f}" width="{B - A - 2:.1f}" height="{y1 - y0:.1f}" style="fill:{fill}"/>')
        o.append(Tb(cx, y0 + 22, roc, 14))
        o.append(boxt(A + 6, 190, B - A - 12, 80, [side, xt, note], PANEL, L2, 13, True))
        o.append(L(cx, y1, cx, 188, L2, 1.5, '4 3'))
    for v in (-3, -1):
        o.append(L(fx(v), y0, fx(v), y1, AC, 2, '6 4'))
    o.append(L(x0, ys, x1, ys, L2, 1.5, arrow='m'))
    o.append(L(fx(0), y1, fx(0), y0 - 14, L2, 1.5, arrow='m'))
    o.append(T(x1 - 4, ys + 22, 'σ', 15, 'end', MUT, italic=True))
    o.append(T(fx(0) + 8, y0 - 2, 'jω', 15, 'start', MUT, italic=True))
    for p in (-3, -1):
        o.append(cross(fx(p), ys, INK))
        o.append(Tb(fx(p), ys + 26, neg(p), 13))
    o.append(T(360, 26, 'X(s) = (3s + 5)/((s + 1)(s + 3)) = 1/(s + 1) + 2/(s + 3)', 15, bold=True))
    return 284, ''.join(o)


FIG[3] = (f3, 'The poles −3 and −1 cut the s-plane into three possible ROCs for the worked example. The partial fractions are the same in all three; each term is right-sided when the ROC lies to the right of its pole and left-sided when it lies to the left.',
          'An s-plane with poles at minus 3 and minus 1 and three shaded bands, each labelled with its ROC and the inverse transform x of t for that ROC.')


# ---- 4.4: pole-zero plot and the two responses ----
def f4():
    o = []
    S0, S1, T0, T1 = 20, 300, 44, 236
    sx = lambda v: S0 + 20 + (v + 3) * 62     # sigma -3 .. 1.2
    sy = lambda v: (T0 + T1) / 2 - v * 40
    ys = sy(0)
    o.append(f'<rect x="{sx(-1):.1f}" y="{T0:.1f}" width="{S1 - sx(-1):.1f}" height="{T1 - T0:.1f}" style="fill:{ACS}"/>')
    o.append(L(sx(-1), T0, sx(-1), T1, AC, 2, '6 4'))
    o.append(L(S0, ys, S1, ys, L2, 1.5, arrow='m'))
    o.append(L(sx(0), T1, sx(0), T0, L2, 1.5, arrow='m'))
    o.append(T(S1 - 4, ys + 22, 'σ', 15, 'end', MUT, italic=True))
    o.append(T(sx(0) + 8, T0 + 14, 'jω', 15, 'start', MUT, italic=True))
    for p in (-2, -1):
        o.append(cross(sx(p), ys, NX))
        o.append(Tb(sx(p), ys + 26, neg(p), 13))
    o.append(Tb((sx(0) + S1) / 2 + 2, T1 - 40, 'causal ROC', 13, fill=AC, bold=True))
    o.append(Tb((sx(0) + S1) / 2 + 2, T1 - 20, 'Re(s) &gt; −1', 13, fill=AC))
    o.append(T((S0 + S1) / 2, T1 + 28, 'H(s) = 1/((s + 1)(s + 2)), no finite zeros', 13))
    # responses
    X0, X1, Y0, Y1 = 384, 700, 44, 236
    fx = lambda t: X0 + (X1 - X0) * t / 6
    fy = lambda v: Y1 - (Y1 - Y0) * v / 1.1
    o.append(axes(X0, X1, Y0, Y1, [0, 1, 2, 3, 4, 5, 6], [0, 0.5, 1], fx, fy, 't (s)', 'y(t)', lambda v: f'{v:g}', lambda v: f'{v:g}'))
    o.append(L(fx(0), fy(0.5), X1, fy(0.5), MUT, 1.5, '5 4'))
    ts = [i * 0.05 for i in range(121)]
    zs = lambda t: 0.5 - math.exp(-t) + 0.5 * math.exp(-2 * t)
    cp = lambda t: 0.5 + math.exp(-t) - 0.5 * math.exp(-2 * t)
    o.append(P([(fx(t), fy(zs(t))) for t in ts], AC, 3))
    o.append(P([(fx(t), fy(cp(t))) for t in ts], LV, 3))
    o.append(Tb(fx(2.7), fy(0.86), 'complete, y(0) = 1', 13, fill=LV, bold=True))
    o.append(Tb(fx(1.75), fy(0.16), 'step response from rest', 13, fill=AC, bold=True))
    o.append(Tb(fx(5.1), fy(0.5) - 10, 'H(0) = 1/2', 13, fill=MUT))
    return 292, ''.join(o)


FIG[4] = (f4, 'Left: the two poles of H(s) at −1 and −2 and the causal ROC Re(s) > −1, which contains the jω axis, so the system is stable. Right: the step response from rest rises from 0 and the complete response with y(0⁻) = 1 falls from 1; both settle to H(0) = 1/2.',
          'Pole-zero plot with poles at minus 1 and minus 2 and the ROC to the right of minus 1, and a plot of the zero-state step response and the complete response, both settling to one half.')


spec = make_spec(FIG)


# ---- model answer, second-order poles for omega_n = 2 ----
def q13_svg():
    o = []
    W, G, M = 162, 10, 15
    y0, y1 = 44, 216
    cases = [('ζ = 1.25', [(-1, 0), (-4, 0)], 'overdamped'), ('ζ = 1', [(-2, 0)], 'critically damped'),
             ('ζ = 0.5', [(-1, 1.732), (-1, -1.732)], 'underdamped'), ('ζ = 0', [(0, 2), (0, -2)], 'undamped')]
    for i, (title, poles, kind) in enumerate(cases):
        x0 = M + i * (W + G); x1 = x0 + W
        fx = lambda v, x0=x0: x0 + 12 + (v + 4.5) * 28     # sigma -4.5 .. 0.8
        fy = lambda v: (y0 + y1) / 2 - v * 30
        o.append(R(x0, y0 - 6, W, y1 - y0 + 12, FIGBG, L2, 6, 1))
        o.append(L(x0 + 4, fy(0), x1 - 4, fy(0), L2, 1.5))
        o.append(L(fx(0), y1, fx(0), y0, L2, 1.5))
        o.append(T(x1 - 8, fy(0) + 18, 'σ', 14, 'end', MUT, italic=True))
        o.append(T(fx(0) - 6, y0 + 12, 'jω', 14, 'end', MUT, italic=True))
        for (a, b) in poles:
            o.append(cross(fx(a), fy(b), NX, 6, 2.5))
        o.append(T(x0 + W / 2, 28, title, 15, bold=True))
        o.append(T(x0 + W / 2, 244, kind, 13, fill=MUT))
    # value labels
    fxs = [M + i * (W + G) for i in range(4)]
    f = lambda i, v: fxs[i] + 12 + (v + 4.5) * 28
    yb = (y0 + y1) / 2
    o += [Tb(f(0, -4), yb + 26, '−4', 13), Tb(f(0, -1), yb + 26, '−1', 13),
          Tb(f(1, -2), yb - 16, '×2', 13), Tb(f(1, -2), yb + 26, '−2', 13),
          Tb(f(2, -1) - 12, yb - 52 + 5, '−1+j1.73', 13, 'end'), Tb(f(2, -1) - 12, yb + 52 + 5, '−1−j1.73', 13, 'end'),
          Tb(f(3, 0) - 12, yb - 60 + 5, 'j2', 13, 'end'), Tb(f(3, 0) - 12, yb + 60 + 5, '−j2', 13, 'end')]
    return {'h': 258, 'body': ''.join(o), 'aria': 'Four s-planes with the poles of the second-order system for damping ratio 1.25, 1, 0.5 and 0, with natural frequency 2 rad/s.'}
