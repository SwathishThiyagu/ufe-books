"""Claude's hand-drawn figures for ec-signals-u3 (Fourier series and Fourier transform), one per chapter.
Every curve is computed from the chapter's own worked example; colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def curve(f, a, b, fx, fy, n=240, c=AC, w=2.5, dash=None):
    pts = [(fx(a + (b - a) * i / n), fy(f(a + (b - a) * i / n))) for i in range(n + 1)]
    return P(pts, c, w, dash)


def stem(x, y0, y, c=AC, w=3):
    return L(x, y0, x, y, c, w) + C(x, y, 5, c)


def frame(x0, x1, y0, y1):
    """light panel behind a plot"""
    return R(x0 - 6, y0 - 6, x1 - x0 + 12, y1 - y0 + 12, 'none', 'var(--line)', 6, 1)


# ---- 3.1 periodic pulse and its line spectrum ----
def f1():
    o = []
    # top: x(t), T0 = 4 s, high for |t| < 1
    x0, x1, yb, yt = 60, 690, 130, 60
    fx = lambda t: x0 + (t + 6) / 12 * (x1 - x0)
    o.append(L(x0, yb, x1, yb, L2, 1.5))
    o.append(L(fx(0), yb + 6, fx(0), yt - 18, L2, 1.5))
    for t in range(-6, 7, 1):
        o.append(L(fx(t), yb, fx(t), yb + 5, L2, 1.5))
        if t % 2 == 1 or t in (-6, 6) or t % 2 == -1:
            o.append(T(fx(t), yb + 20, neg(t), 13, fill=MUT))
    pts = []
    for k in (-2, -1, 0, 1, 2):
        c = 4 * k
        if c - 1 < -6 and c + 1 < -6: continue
        a, b = max(c - 1, -6), min(c + 1, 6)
        if a >= b: continue
        pts += [(fx(a), yb), (fx(a), yt), (fx(b), yt), (fx(b), yb)]
    o.append(P([(fx(-6), yb)] + pts + [(fx(6), yb)], AC, 2.5))
    o.append(T(fx(1) + 8, yt + 4, 'height 1', 13, 'start', MUT))
    o.append(T(x0, 30, 'x(t): high for 2 s in every T₀ = 4 s', 14, 'start', INK, True))
    o.append(T(x1, yb + 40, 't (s)', 14, 'end', MUT))
    # bracket for one period
    o.append(brace(fx(-1), fx(3), yt - 14, INK, up=True))
    o.append(Tb((fx(-1) + fx(3)) / 2, yt - 20, 'one period, T₀ = 4 s', 13))
    # bottom: c_n against n·ω0
    X0, X1, Y0 = 60, 690, 330
    sc = 230  # pixels per unit of c_n
    fX = lambda n: X0 + (n + 8) / 16 * (X1 - X0)
    fY = lambda c: Y0 - c * sc
    o.append(L(X0, Y0, X1, Y0, L2, 1.5))
    o.append(T(X0, 190, 'cₙ = sin(nπ/2)/(nπ), lines every ω₀ = π/2 rad/s', 14, 'start', INK, True))
    env = lambda x: 0.5 if abs(x) < 1e-9 else math.sin(math.pi * x / 2) / (math.pi * x)
    o.append(curve(env, -7.6, 7.6, fX, fY, 300, L2, 1.5, '5 4'))
    for n in range(-7, 8):
        c = env(n)
        if abs(c) < 1e-9:
            o.append(C(fX(n), Y0, 4, MUT))
        else:
            o.append(stem(fX(n), Y0, fY(c), AC if c > 0 else NX))
        o.append(T(fX(n), Y0 + 44, neg(n), 13, fill=MUT))
    o.append(Tb(fX(0) + 10, fY(0.5) - 4, 'c₀ = 0.5', 14, 'start'))
    o.append(Tb(fX(1) + 10, fY(0.3183) - 6, 'c₁ = 0.318', 14, 'start'))
    o.append(Tb(fX(3) + 10, fY(-0.1061) + 5, 'c₃ = −0.106', 14, 'start'))
    o.append(Tb(fX(5) + 4, fY(0.0637) - 14, 'c₅ = 0.064', 14))
    o.append(Tb(fX(-6), Y0 - 42, 'even n: cₙ = 0', 13, fill=MUT))
    o.append(T(X1, Y0 + 66, 'harmonic number n (frequency nω₀)', 14, 'end', MUT))
    return 410, ''.join(o)


FIG[1] = (f1, 'The pulse of the worked example (top) and its two-sided line spectrum (bottom). Every even harmonic is zero, '
              'and the lines follow the dashed sinc-shaped envelope; a line below the axis means a cosine term with a minus sign.',
          'A rectangular pulse train of height 1 and width 2 s repeating every 4 s, and its Fourier coefficients c_n plotted against n from minus 7 to 7: c0 = 0.5, c1 = 0.318, c3 = minus 0.106, c5 = 0.064, even ones zero.')


# ---- 3.2 magnitude and phase of 1/(2 + jw) ----
def f2():
    o = []
    x0, x1, y0, y1 = 70, 410, 60, 300
    fx = lambda w: x0 + (w + 10) / 20 * (x1 - x0)
    fy = lambda m: y1 - m / 0.6 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [-10, -6, -2, 0, 2, 6, 10], [0, 0.2, 0.4, 0.6], fx, fy, 'ω (rad/s)', '|X(ω)|', neg, lambda v: f'{v:.1f}'))
    o.append(curve(lambda w: 1 / math.sqrt(4 + w * w), -10, 10, fx, fy))
    for w in (0, 2, -2):
        m = 1 / math.sqrt(4 + w * w); o.append(C(fx(w), fy(m), 5, NX))
    o.append(Tb(fx(0), fy(0.5) - 12, '|X(0)| = 0.5', 14))
    o.append(Tb(fx(2) + 12, fy(0.354) + 4, '|X(2)| = 0.354', 14, 'start'))
    # phase
    X0, X1, Y0, Y1 = 470, 690, 60, 300
    fX = lambda w: X0 + (w + 10) / 20 * (X1 - X0)
    fY = lambda p: (Y0 + Y1) / 2 - p / 90 * (Y1 - Y0) / 2
    o.append(L(X0, (Y0 + Y1) / 2, X1, (Y0 + Y1) / 2, L2, 1.5))
    o.append(L(X0, Y0, X0, Y1, L2, 1.5))
    for p in (-90, -45, 45, 90):
        o.append(L(X0 - 4, fY(p), X0, fY(p), L2, 1.5))
        o.append(T(X0 - 8, fY(p) + 4.5, neg(p) + '°', 13, 'end', MUT))
    for w in (-10, 10):
        o.append(T(fX(w), (Y0 + Y1) / 2 + 20, neg(w), 13, fill=MUT))
    o.append(curve(lambda w: -math.degrees(math.atan(w / 2)), -10, 10, fX, fY, 200, LV))
    o.append(C(fX(2), fY(-45), 5, NX))
    o.append(Tb(fX(2) + 10, fY(-45) + 22, '−45° at ω = 2', 14, 'start'))
    o.append(T(X0, Y0 - 12, '∠X(ω) = −tan⁻¹(ω/2)', 14, 'start', MUT))
    o.append(T((X0 + X1) / 2, Y1 + 40, 'ω (rad/s)', 14, fill=MUT))
    return 360, ''.join(o)


FIG[2] = (f2, 'Spectrum of x(t) = e<sup>−2t</sup>u(t) from the worked example. The magnitude is even and falls from 0.5 at ω = 0 to 0.354 at ω = 2 rad/s; '
              'the phase is odd and reaches −45° at ω = 2 rad/s, where ω equals the decay rate a = 2.',
          'Left: magnitude 1 over root of 4 plus omega squared, for omega from minus 10 to 10, with 0.5 at zero and 0.354 at 2. Right: phase minus arctan of omega over 2, minus 45 degrees at omega 2.')


# ---- 3.3 modulation: baseband spectrum and the two shifted copies ----
def f3():
    o = []
    x0, x1, y0, y1 = 70, 690, 64, 310
    fx = lambda w: x0 + (w + 20) / 40 * (x1 - x0)
    fy = lambda m: y1 - m / 0.55 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [-20, -10, 0, 10, 20], [0, 0.25, 0.5], fx, fy, 'ω (rad/s)', 'magnitude', neg, lambda v: f'{v:g}'))
    G = lambda w: 1 / math.sqrt(4 + w * w)
    Xm = lambda w: abs(0.5 * (1 / (2 + 1j * (w - 10)) + 1 / (2 + 1j * (w + 10))))
    o.append(curve(G, -20, 20, fx, fy, 320, L2, 2.2, '7 5'))
    o.append(curve(Xm, -20, 20, fx, fy, 400, AC, 2.8))
    o.append(Tb(fx(0) + 12, fy(0.5) + 4, '|G(ω)|: peak 0.5 at ω = 0', 14, 'start', MUT))
    o.append(Tb(fx(10), fy(Xm(10)) - 14, 'copy at +10, peak ≈ 0.25', 14))
    o.append(Tb(fx(-10), fy(Xm(-10)) - 14, 'copy at −10, peak ≈ 0.25', 14))
    o.append(C(fx(0), fy(Xm(0)), 5, NX))
    o.append(Tb(fx(0), fy(Xm(0)) - 16, 'X(0) = 1/52 ≈ 0.019', 14))
    o.append(L(fx(0) + 6, 34, fx(10) - 2, 34, AC, 2, arrow='n'))
    o.append(L(fx(0) - 6, 34, fx(-10) + 2, 34, AC, 2, arrow='n'))
    o.append(T(fx(0), 22, '× cos 10t moves the spectrum to ±10', 14, bold=True))
    return 362, ''.join(o)


FIG[3] = (f3, 'Modulation theorem on the worked example: multiplying g(t) = e<sup>−2t</sup>u(t) by cos 10t moves its spectrum (dashed) to ±10 rad/s at half height. '
              'Between the copies only a small value is left, X(0) = 1/52 V·s.',
          'Dashed curve: magnitude of 1 over 2 plus j omega, peak 0.5 at zero. Solid curve: two half-height copies centred at plus and minus 10 rad per second, with X(0) about 0.019.')


# ---- 3.4 energy spectral density and the 90 % energy band ----
def f4():
    o = []
    x0, x1, y0, y1 = 80, 690, 60, 300
    fx = lambda w: x0 + (w + 30) / 60 * (x1 - x0)
    fy = lambda v: y1 - v / 0.125 * (y1 - y0)
    S = lambda w: 1 / (9 + w * w)
    B = 18.94
    pts = [(fx(-B), fy(0))] + [(fx(-B + 2 * B * i / 200), fy(S(-B + 2 * B * i / 200))) for i in range(201)] + [(fx(B), fy(0))]
    o.append(P(pts, 'none', 0, fill=ACS))
    o.append(axes(x0, x1, y0, y1, [-30, -18.94, -9, 0, 9, 18.94, 30], [0, 0.05, 0.1], fx, fy, 'ω (rad/s)', '|X(ω)|²  (J per rad/s)',
                  lambda v: neg(f'{v:g}'), lambda v: f'{v:g}'))
    o.append(curve(S, -30, 30, fx, fy, 400))
    o.append(L(fx(-B), fy(0), fx(-B), fy(S(B)) - 40, NX, 2, '6 4'))
    o.append(L(fx(B), fy(0), fx(B), fy(S(B)) - 40, NX, 2, '6 4'))
    o.append(Tb(fx(0) + 12, fy(1 / 9) + 2, 'peak 1/9 = 0.111 at ω = 0', 14, 'start'))
    o.append(Tb(fx(0), fy(0.03), 'shaded area ÷ 2π = 0.15 J = 90% of E', 14))
    o.append(Tb(fx(B) + 8, fy(S(B)) - 34, 'B = 18.94 rad/s', 14, 'start', NX))
    o.append(T(x1, 40, 'total E = 1/6 J', 14, 'end', MUT))
    return 360, ''.join(o)


FIG[4] = (f4, 'Energy spectral density of x(t) = e<sup>−3t</sup>u(t), drawn on both sides of ω = 0. The whole area divided by 2π is E = 1/6 J; '
              'the shaded band |ω| ≤ 18.94 rad/s holds 90% of it.',
          'Curve 1 over 9 plus omega squared from minus 30 to 30 rad per second, peak 0.111, with the band between minus 18.94 and 18.94 shaded as 90 percent of the energy.')


# ---- 3.5 RC low-pass: magnitude and phase with the two example frequencies ----
def f5():
    o = []
    x0, x1, y0, y1 = 70, 380, 60, 290
    fx = lambda w: x0 + w / 5000 * (x1 - x0)
    fy = lambda m: y1 - m * (y1 - y0)
    H = lambda w: 1 / complex(1, w * 1e-3)
    o.append(axes(x0, x1, y0, y1, [0, 1000, 2000, 3000, 5000], [0, 0.5, 1], fx, fy, 'ω (rad/s)', '|H(ω)|', str, lambda v: f'{v:g}'))
    o.append(curve(lambda w: abs(H(w)), 0, 5000, fx, fy))
    o.append(C(fx(1000), fy(0.7071), 5, NX)); o.append(C(fx(2000), fy(0.4472), 5, NX))
    o.append(Tb(fx(1000) + 10, fy(0.7071) - 10, '0.707', 14, 'start'))
    o.append(Tb(fx(2000) + 10, fy(0.4472) - 10, '0.447', 14, 'start'))
    X0, X1, Y0, Y1 = 450, 690, 60, 290
    fX = lambda w: X0 + w / 5000 * (X1 - X0)
    fY = lambda p: Y0 + (-p) / 90 * (Y1 - Y0)
    o.append(L(X0, Y0, X1, Y0, L2, 1.5)); o.append(L(X0, Y0, X0, Y1, L2, 1.5))
    for p in (0, -45, -90):
        o.append(L(X0 - 5, fY(p), X0, fY(p), L2, 1.5)); o.append(T(X0 - 9, fY(p) + 4.5, neg(p) + '°', 13, 'end', MUT))
    for w in (0, 2000, 5000):
        o.append(T(fX(w), Y0 - 10, str(w), 13, fill=MUT))
    o.append(curve(lambda w: math.degrees(math.atan2(-w * 1e-3, 1)), 0, 5000, fX, fY, 200, LV))
    o.append(C(fX(1000), fY(-45), 5, NX)); o.append(C(fX(2000), fY(-63.43), 5, NX))
    o.append(Tb(fX(1000) + 10, fY(-45) - 4, '−45°', 14, 'start'))
    o.append(Tb(fX(2000) + 10, fY(-63.43) + 18, '−63.4°', 14, 'start'))
    o.append(T((X0 + X1) / 2, Y1 + 24, '∠H(ω) = −tan⁻¹(ωRC)', 14, fill=MUT))
    o.append(T((X0 + X1) / 2, Y1 + 44, 'ω (rad/s)', 14, fill=MUT))
    return 350, ''.join(o)


FIG[5] = (f5, 'The RC low-pass of the worked examples (RC = 1 ms) on linear axes. At ω = 1000 rad/s the gain is 0.707 and the phase −45°; '
              'at ω = 2000 rad/s they are 0.447 and −63.4°, so a higher input frequency comes out smaller and later.',
          'Left: magnitude 1 over root of 1 plus omega RC squared from 0 to 5000 rad per second, with 0.707 at 1000 and 0.447 at 2000. Right: phase from 0 to minus 90 degrees, minus 45 at 1000 and minus 63.4 at 2000.')


# ---- 3.6 ideal filter of the worked example: brick wall, phase line and the delayed output ----
def f6():
    o = []
    td = 't<tspan font-size="10" baseline-shift="sub">d</tspan>'
    x0, x1, y0, y1 = 60, 330, 66, 160
    fx = lambda w: x0 + (w + 3000) / 6000 * (x1 - x0)
    fy = lambda m: y1 - m / 2.4 * (y1 - y0)
    o.append(L(x0, y1, x1, y1, L2, 1.5)); o.append(L(fx(0), y0 - 10, fx(0), y1, L2, 1.5))
    o.append(P([(x0, y1), (fx(-2000), y1), (fx(-2000), fy(2)), (fx(2000), fy(2)), (fx(2000), y1), (x1, y1)], AC, 2.8))
    for w in (-2000, 2000):
        o.append(T(fx(w), y1 + 20, neg(w), 13, fill=MUT))
    o.append(T(x0, 36, 'gain |H(ω)|: K = 2 in the pass band', 14, 'start', INK, True))
    o.append(T(x1, y1 + 20, 'ω', 14, 'end', MUT))
    # phase line below
    Y0, Y1 = 250, 350
    fP = lambda p: (Y0 + Y1) / 2 - p / 2.4 * (Y1 - Y0) / 2
    o.append(L(x0, (Y0 + Y1) / 2, x1, (Y0 + Y1) / 2, L2, 1.5)); o.append(L(fx(0), Y0 - 8, fx(0), Y1 + 8, L2, 1.5))
    o.append(L(fx(-2000), fP(2), fx(2000), fP(-2), LV, 2.8))
    o.append(C(fx(1000), fP(-1), 5, NX))
    o.append(Tb(fx(1000) - 10, fP(-1) + 26, '−1 rad at ω = 1000', 14))
    o.append(T(x0, 214, 'phase ∠H(ω) = −ω' + td + ', ' + td + ' = 1 ms', 14, 'start', INK, True))
    o.append(T(x1, (Y0 + Y1) / 2 - 8, 'ω', 14, 'end', MUT))
    # time panel
    X0, X1, TY0, TY1 = 390, 690, 66, 340
    fT = lambda t: X0 + t / 8 * (X1 - X0)      # t in ms
    fV = lambda v: (TY0 + TY1) / 2 + 20 - v / 2.4 * (TY1 - TY0) / 2
    o.append(L(X0, fV(0), X1, fV(0), L2, 1.5)); o.append(L(X0, fV(2.3), X0, fV(-2.3), L2, 1.5))
    for v in (-2, -1, 1, 2):
        o.append(L(X0 - 4, fV(v), X0, fV(v), L2, 1.5)); o.append(T(X0 - 8, fV(v) + 4.5, neg(v), 13, 'end', MUT))
    for t in (2, 4, 6, 8):
        o.append(T(fT(t), fV(0) + 18, str(t), 13, fill=MUT))
    o.append(curve(lambda t: math.cos(t), 0, 8, fT, fV, 200, L2, 2.4, '7 5'))
    o.append(curve(lambda t: 2 * math.cos(t - 1), 0, 8, fT, fV, 200, AC, 2.8))
    o.append(L(fT(0), fV(2.15), fT(1), fV(2.15), NX, 2, arrow='x'))
    o.append(Tb(fT(1) + 8, fV(2.15) + 5, '1 ms delay', 14, 'start', NX))
    o.append(Tb(fT(6.6), fV(1.05) - 6, 'x(t) = cos 1000t', 13, fill=MUT))
    o.append(Tb(fT(4.2), fV(-2) + 22, 'y(t) = 2 cos(1000t − 1)', 14))
    o.append(T((X0 + X1) / 2, TY1 + 40, 't (ms)', 14, fill=MUT))
    o.append(C(fT(0), fV(1.0806), 5, NX))
    o.append(Tb(fT(0) + 12, fV(1.0806) + 22, 'y(0) = 1.08 V', 13, 'start'))
    return 400, ''.join(o)


FIG[6] = (f6, 'The ideal filter of the worked example: gain 2 inside |ω| ≤ 2000 rad/s, zero outside, and a straight phase line through the origin. '
              'The 1000 rad/s input comes out twice as tall and 1 ms later, with its shape unchanged.',
          'Top left: brick-wall magnitude 2 between minus and plus 2000 rad per second. Bottom left: phase line through the origin, minus 1 radian at 1000. Right: input cos 1000t dashed and output 2 cos(1000t minus 1) solid over 0 to 8 ms, shifted by 1 ms.')


# ---- 3.7 autocorrelation and its transform ----
def f7():
    o = []
    x0, x1, y0, y1 = 70, 370, 60, 290
    fx = lambda t: x0 + (t + 3) / 6 * (x1 - x0)
    fy = lambda v: y1 - v / 0.3 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [-3, -2, -1, 0, 1, 2, 3], [0, 0.1, 0.2, 0.3], fx, fy, 'lag τ (s)', 'Rₓ(τ)', neg, lambda v: f'{v:g}'))
    o.append(curve(lambda t: math.exp(-2 * abs(t)) / 4, -3, 3, fx, fy, 300))
    for t in (0, 1, 2):
        o.append(C(fx(t), fy(math.exp(-2 * t) / 4), 5, NX))
    o.append(Tb(fx(0) + 10, fy(0.25) - 2, 'Rₓ(0) = E = 0.25', 14, 'start'))
    o.append(Tb(fx(1) + 8, fy(0.0338) - 14, 'Rₓ(1) = 0.0338', 14, 'start'))
    X0, X1 = 420, 690
    fX = lambda w: X0 + (w + 10) / 20 * (X1 - X0)
    o.append(axes(X0, X1, y0, y1, [-10, -5, 0, 5, 10], [0, 0.1, 0.2, 0.3], fX, fy, 'ω (rad/s)', '|X(ω)|² = 1/(4 + ω²)', neg, lambda v: f'{v:g}'))
    o.append(curve(lambda w: 1 / (4 + w * w), -10, 10, fX, fy, 300, LV))
    o.append(C(fX(2), fy(0.125), 5, NX))
    o.append(Tb(fX(2) + 10, fy(0.125) - 6, '0.125 at ω = 2', 14, 'start'))
    o.append(L(x1 - 20, 30, X0 + 20, 30, AC, 2, arrow='n'))
    o.append(T((x1 + X0) / 2, 22, 'Fourier transform', 13, fill=MUT))
    return 350, ''.join(o)


FIG[7] = (f7, 'Worked example: the autocorrelation of e<sup>−2t</sup>u(t) (left) is even with its peak, the energy 0.25, at zero lag. '
              'Its Fourier transform (right) is 1/(4 + ω²), the same as |X(ω)|², as the Wiener–Khinchin relation says.',
          'Left: e to the minus 2 absolute tau over 4 for tau from minus 3 to 3, peak 0.25 at zero, 0.0338 at 1. Right: 1 over 4 plus omega squared, 0.25 at zero and 0.125 at omega 2.')


# ---- 3.8 cosine and its Hilbert transform, with the -j sgn(w) phase ----
def f8():
    o = []
    x0, x1, y0, y1 = 70, 690, 64, 240
    fx = lambda t: x0 + t / 6.4 * (x1 - x0)
    fy = lambda v: (y0 + y1) / 2 - v * (y1 - y0) / 2.4
    o.append(L(x0, fy(0), x1, fy(0), L2, 1.5)); o.append(L(x0, fy(1.15), x0, fy(-1.15), L2, 1.5))
    for v in (-1, 1):
        o.append(L(x0 - 4, fy(v), x0, fy(v), L2, 1.5)); o.append(T(x0 - 8, fy(v) + 4.5, neg(v), 13, 'end', MUT))
    for t in (1, 2, 3, 4, 5, 6):
        o.append(L(fx(t), fy(1.15), fx(t), fy(1.15) + 5, L2, 1.5)); o.append(T(fx(t), fy(1.15) - 6, str(t), 13, fill=MUT))
    o.append(curve(lambda t: math.cos(2 * t), 0, 6.3, fx, fy, 300, L2, 2.4, '7 5'))
    o.append(curve(lambda t: math.sin(2 * t), 0, 6.3, fx, fy, 300, AC, 2.8))
    o.append(L(fx(1), fy(-0.416), fx(1), fy(0.909), NX, 1.5, '4 3'))
    o.append(C(fx(1), fy(0.909), 5, NX)); o.append(C(fx(1), fy(-0.416), 5, MUT))
    o.append(Tb(fx(1) + 10, fy(0.909) - 8, 'x̂(1) = sin 2 = 0.909', 14, 'start'))
    o.append(Tb(fx(1) + 10, fy(-0.416) + 6, 'x(1) = cos 2 = −0.416', 13, 'start', MUT))
    o.append(Tb(fx(4.05) + 8, fy(0.55), 'x̂(t) = sin 2t', 14, 'start', AC))
    o.append(Tb(fx(5.3), fy(-1.0) + 22, 'x(t) = cos 2t', 13, 'middle', MUT))
    o.append(T(x1, fy(1.15) - 6, 't (s)', 14, 'end', MUT))
    # phase of H_H(w)
    X0, X1, Y0, Y1 = 170, 550, 290, 390
    fX = lambda w: X0 + (w + 5) / 10 * (X1 - X0)
    fY = lambda p: (Y0 + Y1) / 2 - p / 90 * (Y1 - Y0) / 2
    o.append(L(X0, fY(0), X1, fY(0), L2, 1.5)); o.append(L(fX(0), Y0 - 6, fX(0), Y1 + 6, L2, 1.5))
    o.append(L(X0, fY(90), fX(0) - 3, fY(90), LV, 3)); o.append(L(fX(0) + 3, fY(-90), X1, fY(-90), LV, 3))
    o.append(T(X0 - 8, fY(90) + 5, '+90°', 13, 'end', MUT)); o.append(T(X1 + 8, fY(-90) + 5, '−90°', 13, 'start', MUT))
    o.append(T(X1 + 8, fY(0) + 5, 'ω', 14, 'start', MUT))
    o.append(T(fX(-2.5), fY(90) - 10, 'ω < 0: × (+j)', 14))
    o.append(T(fX(2.5), fY(-90) + 22, 'ω > 0: × (−j)', 14))
    o.append(T(fX(0) + 8, Y0 - 12, 'phase of −j sgn(ω), gain 1', 14, 'start', MUT))
    return 420, ''.join(o)


FIG[8] = (f8, 'Worked example: the Hilbert transform of cos 2t (dashed) is sin 2t (solid), the same wave a quarter period later. '
              'The lower plot is the reason: every positive frequency is turned by −90° and every negative frequency by +90°, with gain 1.',
          'Top: cos 2t dashed and sin 2t solid for t from 0 to 6.3 s, with values at t = 1 s of minus 0.416 and 0.909. Bottom: phase plus 90 degrees for negative omega and minus 90 degrees for positive omega.')


spec = make_spec(FIG)
