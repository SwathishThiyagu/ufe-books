# Glass t16 drawings for Analog and Digital Communication (ec-comm). Every value is computed here from the lesson's own numbers.
from dhelp import *
import math, cmath
D = {}


# ---------------- unit 1 ----------------
def u1L1():
    # 2 V, 1 ms pulse: X(0) = A T = 2 mV/Hz, nulls at +-1 kHz; times cos(2 pi 10 kHz t): two half-height copies at +-10 kHz
    A, T, fc = 2, 1e-3, 10
    X0 = A * T * 1e3                                    # mV/Hz
    Xb = lambda f: X0 * sinc(f)                         # f in kHz, so fT = f
    Xm = lambda f: X0 / 2 * (sinc(f - fc) + sinc(f + fc))
    s = defs()
    p = Plot(-14, 14, -0.5, 2.3, L=50, T=26, Wd=420, H=110)
    s += sax(p, xt=(-1, 1), yt=(0, 2), yl='baseband pulse, mV/Hz')
    s += area(p, Xb, -1, 1, MUT, op=.18) + p.curve(Xb, -14, 14, n=700, c=MUT, w=4)
    s += tag(p.X(0) + 30, p.Y(X0) + 8, f'{g(X0)} at 0', MUT, 13, 'start')
    q = Plot(-14, 14, -0.3, 1.25, L=50, T=200, Wd=420, H=110)
    s += sax(q, xt=(-10, 0, 10), yt=(0, 1), xl='f (kHz) →')
    s += area(q, Xm, -11, -9, B, op=.2) + area(q, Xm, 9, 11, B, op=.2) + q.curve(Xm, -14, 14, n=900, c=B, w=4.5)
    s += tag(q.X(-fc), q.Y(1) - 12, f'{g(X0 / 2)} at −{fc}', B, 13) + tag(q.X(fc), q.Y(1) - 12, f'{g(X0 / 2)} at +{fc}', B, 13)
    s += line(p.X(0) - 40, p.Y(0) + 30, q.X(-fc) + 62, q.Y(1) - 30, O, 3, '6 5', arrow=True) + line(p.X(0) + 40, p.Y(0) + 30, q.X(fc) - 62, q.Y(1) - 30, O, 3, '6 5', arrow=True)
    s += txt(q.X(0), q.Y(1) + 4, f'× cos 2π·{fc} kHz·t', 14, O, 900)
    return 'One pulse, two half copies', s
D['ec-comm-u1-L1'] = (u1L1, '2 mV/Hz → 1 at ±10 kHz', '1.2.1')


def u1L2():
    # Gaussian noise, sigma = 2 mV: at 4 mV the height is 0.027 per mV (a density); the tail area Q(2) = 0.0228 is the probability
    sg, th = 2, 4
    pdf = lambda x: math.exp(-x * x / (2 * sg * sg)) / (sg * math.sqrt(2 * math.pi))
    p = Plot(-8, 8, 0, 0.23, L=60, T=24, Wd=420, H=240)
    s = defs()
    for v in (0.1, 0.2):
        s += line(p.L, p.Y(v), p.L + p.W, p.Y(v), GRID, 1.5) + txt(p.L - 10, p.Y(v) + 5, g(v), 13, MUT, 700, 'end')
    s += txt(p.L - 10, p.Y(0) + 5, '0', 13, MUT, 700, 'end')
    s += line(p.L, p.T + p.H, p.L + p.W + 8, p.T + p.H, MUT, 2.5, arrow=True) + line(p.L, p.T + p.H, p.L, p.T - 8, MUT, 2.5, arrow=True)
    for v in (-4, -2, 0, 2, 4):
        s += txt(p.X(v), p.T + p.H + 22, g(v), 13, MUT, 700)
    s += txt(p.L + p.W + 8, p.T + p.H + 44, 'noise (mV) →', 13, MUT, 700, 'end') + txt(p.L + 8, p.T - 10, 'density, per mV', 13, MUT, 700, 'start')
    s += area(p, pdf, -sg, sg, G, op=.25) + area(p, pdf, th, 8, O, op=.6)
    s += p.curve(pdf, -8, 8, n=200, c=INK, w=4)
    s += line(p.X(th), p.Y(0), p.X(th), p.Y(pdf(th)), B, 3, '5 4') + dot(*p.P(th, pdf(th)), 8, B)
    s += tag(p.X(th) + 30, p.Y(0.115), f'height {pdf(th):.3f} /mV: a density', B, 13, 'middle')
    s += line(p.X(5.4), p.Y(0.006), p.X(5.9), p.Y(0.045), O, 2.5)
    s += tag(p.X(5.9), p.Y(0.045) - 6, f'area Q(2) = {Qf(2):.4f}', O, 13)
    s += tag(p.X(0), p.Y(0.07), f'{(1 - 2 * Qf(1)) * 100:.2f} %', G, 13)
    s += txt(p.L, p.T + p.H + 64, f'σ = {sg} mV: only an area is a probability', 14, INK, 900, 'start')
    return 'Height or area?', s
D['ec-comm-u1-L2'] = (u1L2, 'only an area counts', '1.4.1')


def u1L3():
    # 20 kOhm and 50 kOhm in series, T = 290 K, B = 100 kHz: 5.66 and 8.95 uV add in mean square -> 10.59, not 14.61
    k, T, Bw = 1.38e-23, 290, 1e5
    v = lambda R: math.sqrt(4 * k * T * R * Bw) * 1e6
    v1, v2 = v(20e3), v(50e3)
    rs = math.hypot(v1, v2)
    s = defs()
    sc = 22
    x0, y0 = 120, 300
    xa, yb = x0 + v1 * sc, y0 - v2 * sc
    s += poly([(x0, y0), (xa, y0), (xa, yb)], MUT, 2, fill=MINT, close=True)
    s += line(x0, y0, xa, y0, B, 7) + line(xa, y0, xa, yb, G, 7) + line(x0, y0, xa, yb, O, 7)
    s += rect(xa - 18, y0 - 18, 18, 18, 'none', MUT, 2, 0)
    s += tag((x0 + xa) / 2, y0 + 34, f'20 kΩ: {v1:.2f} µV', B, 14)
    s += tag(xa + 14, (y0 + yb) / 2 + 6, f'50 kΩ: {v2:.2f} µV', G, 14, 'start')
    s += tag((x0 + xa) / 2 - 30, (y0 + yb) / 2 - 16, f'{rs:.2f} µV', O, 16, 'end')
    s += txt(20, 40, f'√({v1:.2f}² + {v2:.2f}²) = {rs:.2f}', 16, INK, 900, 'start')
    s += txt(20, 68, f'not {v1:.2f} + {v2:.2f} = {round(v1, 2) + round(v2, 2):.2f}', 15, O, 900, 'start')
    s += txt(500, 362, f'4kTRB, {T} K, {Bw / 1e3:g} kHz', 12, MUT, 800, 'end')
    return 'Noise voltages add in squares', s
D['ec-comm-u1-L3'] = (u1L3, '√(5.66² + 8.95²) = 10.59', '1.6.1')


# ---------------- unit 2 ----------------
def u2L1():
    # AM: envelope 12 V and 4 V -> m = 0.5, Ac = 8; lines 8 V at 1000 kHz and m Ac / 2 = 2 V at 995 and 1005
    Emax, Emin = 12, 4
    m = (Emax - Emin) / (Emax + Emin); Ac = (Emax + Emin) / 2
    env = lambda t: Ac * (1 + m * math.cos(2 * math.pi * t))
    p = Plot(0, 2, -13, 13, L=50, T=14, Wd=430, H=150)
    s = defs() + sax(p, yt=(-12, -4, 0, 4, 12), yl='volts')
    s += p.curve(lambda t: env(t) * math.cos(2 * math.pi * 16 * t), 0, 2, n=900, c=B, w=3)
    s += p.curve(env, 0, 2, n=120, c=O, w=3.5, dash='8 6') + p.curve(lambda t: -env(t), 0, 2, n=120, c=O, w=3.5, dash='8 6')
    s += tag(p.X(1.0), p.Y(12) + 2, f'{Emax} V', O, 13) + tag(p.X(0.5), p.Y(4) - 2, f'{Emin} V', O, 13)
    s += txt(p.L + p.W, p.T + p.H + 20, 'time → (carrier drawn slowed)', 12, MUT, 700, 'end')
    yb, k = 352, 16
    xs = {995: 150, 1000: 260, 1005: 370}
    s += line(80, yb, 450, yb, MUT, 2.5, arrow=True)
    for f, x in xs.items():
        a = Ac if f == 1000 else m * Ac / 2
        s += line(x, yb, x, yb - k * a, G if f == 1000 else O, 8, cap='butt') + txt(x + 9, yb - k * a + 5, f'{g(a)} V', 15, INK, 900, 'start')
        s += txt(x, yb + 20, g(f), 13, MUT, 700)
    s += txt(450, yb + 20, 'kHz', 13, MUT, 700, 'end')
    s += tag(150, yb - 52, 'mAc/2', O, 13) + tag(370, yb - 52, 'mAc/2', O, 13)
    return 'Each sideband is mAc/2', s
D['ec-comm-u2-L1'] = (u2L1, f'm = 0.5: 2 V each, not 4', '2.1.1')


def u2L2():
    # speech 0.3-3.4 kHz on 100 kHz: DSB-SC 6.8, SSB 3.4, VSB = 3.4 + 0.5 vestige = 3.9 kHz
    fc, lo, hi, ves = 100, 0.3, 3.4, 0.5
    p = Plot(95.5, 104.5, 0, 1.3, L=30, T=30, Wd=460, H=130)
    s = defs()
    lsb = [p.P(fc - hi, 0), p.P(fc - hi, 1), p.P(fc - lo, 0.45), p.P(fc - lo, 0)]
    usb = [p.P(fc + lo, 0), p.P(fc + lo, 0.45), p.P(fc + hi, 1), p.P(fc + hi, 0)]
    s += poly(lsb, MUT, 2.5, '6 5', fill='#EEF1F6', close=True) + poly(usb, B, 3, fill=BS, close=True)
    # VSB filter edge: rolls off from fc - 0.5 to fc + 0.5, exactly 1/2 at fc
    edge = [p.P(fc - ves - 0.4, 0)] + [p.P(fc - ves + i / 20, 1.15 * (0.5 - 0.5 * math.cos(math.pi * i / 20))) for i in range(21)] + [p.P(fc + hi + 0.4, 1.15)]
    s += poly(edge, O, 3, '8 6')
    s += rect(p.X(fc - ves), p.Y(0.22), p.X(fc - lo) - p.X(fc - ves), p.Y(0) - p.Y(0.22), OS, O, 2, 2)
    s += line(p.X(fc), p.Y(0), p.X(fc), p.Y(1.22), MUT, 2, '4 5') + txt(p.X(fc), p.T - 10, 'fc 100', 12, MUT, 800)
    s += line(p.L, p.Y(0), p.L + p.W + 8, p.Y(0), MUT, 2.5, arrow=True)
    for f in (fc - hi, fc - ves, fc + hi):
        s += txt(p.X(f), p.Y(0) + 20, f'{f:g}', 13, MUT, 700)
    s += txt(p.L + p.W, p.Y(0) + 38, 'kHz', 12, MUT, 700, 'end')
    s += txt(p.X(fc - 2.2), p.Y(1.12), 'LSB', 13, MUT, 800) + txt(p.X(fc + 2.2), p.Y(1.12) - 6, 'USB kept', 13, B, 900)
    s += tag(p.X(fc - ves) - 8, p.Y(0.5), 'vestige 0.5', O, 12, 'end')
    rows = [('DSB-SC', 2 * hi, MUT), ('SSB', hi, B), ('VSB', hi + ves, O)]
    X = lambda v: 120 + v / 7.2 * 340
    for i, (n, v, c) in enumerate(rows):
        y = 240 + i * 42
        s += txt(110, y + 21, n, 15, INK, 900, 'end') + rect(120, y, X(v) - 120, 30, c, W, 2, 8)
        s += txt(X(v) + 10, y + 21, f'{v:g} kHz', 15, INK, 900, 'start')
    return 'SSB plus a sliver', s
D['ec-comm-u2-L2'] = (u2L2, '3.4 + 0.5 = 3.9 kHz', '2.3.1')


def u2L3():
    # diode detector, m = 0.6, fm = 5 kHz: clip limit sqrt(1 - m^2)/(2 pi fm m) = 42.4 us; RC = 20 us follows, RC = 2 x 42.4 us clips
    m, fm, RC = 0.6, 5e3, 20e-6
    tlim = math.sqrt(1 - m * m) / (2 * math.pi * fm * m)
    Tt, ncar = 1.0, 24
    env = lambda t: 1 + m * math.cos(2 * math.pi * t / Tt)
    wav = lambda t: env(t) * math.cos(2 * math.pi * ncar * t / Tt)
    p = Plot(0, 1.6, 0, 1.75, L=40, T=14, Wd=450, H=230)
    s = defs() + sax(p, yt=(0, 0.4, 1, 1.6), yl='× Ac')
    s += poly([p.P(1.6 * i / 2400, max(0, wav(1.6 * i / 2400))) for i in range(2401)], '#DCE2EA', 1.5)
    def det(rc_s):
        rc = rc_s * fm * Tt
        out, v, dt = [], 0, 1.6 / 6000
        for i in range(6001):
            t = i * dt
            v = max(wav(t), v * math.exp(-dt / rc))
            if t > 0.03: out.append(p.P(t, v))
        return out
    s += p.curve(env, 0, 1.6, n=120, c=G, w=3, dash='8 6')
    s += poly(det(2 * tlim), O, 4.5) + poly(det(RC), B, 3.5)
    s += tag(p.X(0.72), p.Y(0.62) - 4, 'RC too large: lags the envelope', O, 13)
    s += tag(p.X(1.3), p.Y(1.72), 'envelope', G, 12)
    s += txt(40, 312, f'diagonal clipping once RC > {tlim * 1e6:.1f} µs', 14, O, 900, 'start')
    s += txt(40, 338, f'RC = {RC * 1e6:g} µs (blue) follows; orange: 2 × {tlim * 1e6:.1f} µs', 13, INK, 800, 'start')
    s += txt(490, 362, 'm = 0.6, 5 kHz tone, carrier drawn slowed', 12, MUT, 700, 'end')
    return 'Too slow to fall', s
D['ec-comm-u2-L3'] = (u2L3, 'RC > 42.4 µs clips', '2.5.1')


def u2L4():
    # superhet tuned to 1000 kHz, IF 455: LO 1455, image 1910; RF Q = 100 -> alpha 138.6, 42.8 dB, before the mixer
    fs, fi_, Q = 1000, 455, 100
    flo, fim = fs + fi_, fs + 2 * fi_
    rho = lambda f: f / fs - fs / f
    G_ = lambda f: -10 * math.log10(1 + (Q * rho(f)) ** 2)
    a = math.sqrt(1 + (Q * rho(fim)) ** 2)
    p = Plot(800, 2050, -50, 0, L=50, T=40, Wd=430, H=230)
    s = defs() + sax(p, xt=(1000, 1455, 1910), yt=(0, -10, -20, -30, -40, -50), xl='f (kHz) →', yl='RF stage gain (dB)')
    s += area(p, G_, 800, 2050, B, n=300, op=.15, base=-50)
    s += p.curve(G_, 800, 2050, n=300, c=B, w=4.5)
    s += line(p.X(flo), p.Y(0), p.X(flo), p.Y(-50), G, 3, '7 6') + tag(p.X(flo), p.Y(-3), 'LO', G, 13)
    s += dot(*p.P(fs, 0), 9, B) + tag(p.X(fs) + 14, p.Y(-7), 'signal', B, 13, 'start')
    s += dot(*p.P(fim, G_(fim)), 10, O) + tag(p.X(fim) - 6, p.Y(G_(fim)) - 18, f'image {G_(fim):.1f} dB', O, 13, 'end')
    yA = p.Y(-46)
    s += arrow2(p.X(fs) + 4, yA, p.X(flo) - 4, yA, INK, 2) + txt((p.X(fs) + p.X(flo)) / 2, yA - 8, f'{fi_}', 13, INK, 900)
    s += arrow2(p.X(flo) + 4, yA, p.X(fim) - 4, yA, INK, 2) + txt((p.X(flo) + p.X(fim)) / 2, yA - 8, f'{fi_}', 13, INK, 900)
    s += txt(p.L, p.T + p.H + 70, f'after the mixer both sit at {fi_} kHz: reject it here', 13, MUT, 800, 'start')
    return 'Only the RF stage can', s
D['ec-comm-u2-L4'] = (u2L4, 'only the RF stage', '2.7.1')


# ---------------- unit 3 ----------------
def J(n, x, terms=30):
    n = abs(n)
    return sum((-1) ** k / (math.factorial(k) * math.factorial(k + n)) * (x / 2) ** (2 * k + n) for k in range(terms))


def u3L1():
    # broadcast FM: delta f 75 kHz, fm 15 kHz -> beta 5; lines Jn(5) every 15 kHz; Carson 2(75 + 15) = 180 kHz, not 2 delta f = 150
    df, fm = 75, 15
    beta = df / fm; BT = 2 * (df + fm)
    amp = {n: J(n, beta) * (-1 if n < 0 and n % 2 else 1) for n in range(-8, 9)}
    keep = sum(J(n, beta) ** 2 for n in range(-6, 7))
    p = Plot(-130, 130, -0.45, 0.45, L=40, T=24, Wd=450, H=240)
    s = defs()
    s += rect(p.X(-BT / 2), p.T, p.X(BT / 2) - p.X(-BT / 2), p.H, MINT, 'none', 0, 10)
    s += line(p.X(-df), p.T, p.X(-df), p.T + p.H, O, 2.5, '6 6') + line(p.X(df), p.T, p.X(df), p.T + p.H, O, 2.5, '6 6')
    s += sax(p, xt=(-90, 0, 90), yt=(-0.4, 0, 0.4), yaxis=False, yl='Jn(5)')
    for n, a in amp.items():
        x = p.X(n * fm); c = B if a >= 0 else G
        s += line(x, p.Y(0), x, p.Y(a), c, 7, cap='butt')
    s += txt(p.L + p.W + 8, p.T + p.H + 44, 'offset from fc (kHz) →', 13, MUT, 700, 'end')
    s += tag(p.X(0), p.T + 16, f'Carson {BT:g} kHz: {keep * 100:.1f} % of power', G, 13)
    s += tag(p.X(-df) - 4, p.Y(-0.36), f'2Δf = {2 * df} only', O, 12, 'end')
    s += txt(p.L + 4, p.T + p.H + 44, f'β = {beta:g}: six pairs', 12, MUT, 800, 'start')
    return 'Six pairs of sidebands', s
D['ec-comm-u3-L1'] = (u3L1, '2(75 + 15) = 180 kHz', '3.2.1')


def u3L2():
    # single slope detector: peak 465 kHz, Q 50 (9.3 kHz bandwidth); carrier 455 on the flank: 0.422 V, 460: 0.681, 450: 0.296
    f0, Q = 465, 50
    V = lambda f: 1 / math.sqrt(1 + (2 * Q * (f - f0) / f0) ** 2)
    fc = 455
    p = Plot(430, 500, 0, 1.1, L=50, T=24, Wd=430, H=230)
    s = defs() + sax(p, xt=(450, 465, 480), yt=(0, 0.5, 1), xl='f (kHz) →', yl='output (V)')
    s += area(p, V, 430, 500, B, n=200, op=.1) + p.curve(V, 430, 500, n=200, c=B, w=5)
    for f, c in ((450, MUT), (460, MUT)):
        s += dot(*p.P(f, V(f)), 8, c) + txt(p.X(f) + (-10 if f < fc else 10), p.Y(V(f)) + (18 if f < fc else -8), f'{V(f):.3f}', 13, INK, 800, 'end' if f < fc else 'start')
    s += line(p.X(fc), p.Y(0), p.X(fc), p.Y(V(fc)), O, 3, '6 5') + dot(*p.P(fc, V(fc)), 11, O)
    s += tag(p.X(fc) - 14, p.Y(V(fc)) - 18, f'carrier {fc}: {V(fc):.3f} V', O, 14, 'end')
    s += tag(p.X(f0), p.Y(1.0) - 16, 'peak 465', B, 12)
    s += txt(p.L, p.T + p.H + 64, 'balanced detectors read 0 at the carrier', 13, MUT, 800, 'start')
    return 'Parked on the flank', s
D['ec-comm-u3-L2'] = (u3L2, '0.422 V at fc, not 0', '3.4.1')


def u3L3():
    # FM threshold: N0 = 4e-21 W/Hz, W = 15 kHz; beta 5 (BT 180 kHz) and beta 2 (BT 90 kHz); threshold CNR 10 dB
    N0, W = 4e-21, 15e3
    dbm = lambda w: 10 * math.log10(w / 1e-3)
    lines = []
    for beta, c in ((5, B), (2, G)):
        BT = 2 * (beta + 1) * W
        Cth = dbm(N0 * BT) + 10
        gain = db(1.5 * beta * beta)
        out = lambda C, gain=gain: C - dbm(N0 * W) + gain
        lines.append((beta, BT, Cth, out, c))
    p = Plot(-120, -100, 0, 55, L=50, T=24, Wd=430, H=240)
    s = defs() + sax(p, xt=(-118, -114, -110, -106, -102), yt=(10, 20, 30, 40, 50), xl='received carrier C (dBm) →', yl='output SNR (dB)')
    for beta, BT, Cth, out, c in lines:
        s += p.curve(out, Cth, -100.5, n=4, c=c, w=5)
        y0 = out(Cth)
        s += f'<path d="M{p.X(Cth):.1f},{p.Y(y0):.1f} C{p.X(Cth - 0.6):.1f},{p.Y(y0 - 4):.1f} {p.X(Cth - 1.6):.1f},{p.Y(y0 - 12):.1f} {p.X(Cth - 2.1):.1f},{p.Y(y0 - 24):.1f}" fill="none" stroke="{c}" stroke-width="4" stroke-dasharray="6 6" marker-end="url(#a{mk(c)})"/>'
        s += dot(*p.P(Cth, y0), 9, c)
        s += tag(p.X(Cth) - 14, p.Y(y0) - 8, f'{Cth:.1f} dBm', c, 12, 'end')
        s += txt(p.X(-101), p.Y(out(-101)) + (-12 if beta == 5 else 24), f'β = {beta}, {BT / 1e3:g} kHz', 13, c, 900, 'end')
    s += txt(p.X(-119.5), p.Y(52), 'below the knee: clicks,', 13, O, 800, 'start') + txt(p.X(-119.5), p.Y(52) + 18, 'output falls fast', 13, O, 800, 'start')
    return 'Clean, until the knee', s
D['ec-comm-u3-L3'] = (u3L3, 'threshold at CNR 10 dB', '3.6.1')


def u3L4():
    # 75 us pre-emphasis before the modulator, de-emphasis after the discriminator: corner 2122 Hz (+3.01 dB), +17.07 dB at 15 kHz
    tau = 75e-6; f1 = 1 / (2 * math.pi * tau)
    H = lambda f: 10 * math.log10(1 + (f / f1) ** 2)
    lx = lambda f: math.log10(f)
    s = defs()
    y = 8; bw = 92; gap = 13
    blocks = [('pre-emph', O, OS), ('FM mod', INK, W), ('channel', MUT, '#EEF1F6'), ('discrim.', INK, W), ('de-emph', B, BS)]
    for i, (n, c, f) in enumerate(blocks):
        x = 6 + i * (bw + gap)
        s += box(x, y, bw, 48, n, c, 14, fill=f)
        if i: s += line(x - gap, y + 24, x - 2, y + 24, MUT, 2.5, arrow=True)
    s += txt(6 + 2 * (bw + gap) + bw / 2, y + 68, '+ flat noise', 12, MUT, 800)
    p = Plot(2, lx(15000), -20, 20, L=50, T=110, Wd=420, H=180)
    for v in (-17, 0, 17):
        s += line(p.L, p.Y(v), p.L + p.W, p.Y(v), GRID if v else MUT, 1.5 if v else 2.5)
        s += txt(p.L - 10, p.Y(v) + 5, g(v), 13, MUT, 700, 'end')
    s += line(p.L, p.T + p.H, p.L, p.T - 6, MUT, 2.5, arrow=True) + txt(p.L + 8, p.T + 2, 'dB', 13, MUT, 700, 'start')
    for f, lab in ((100, '100 Hz'), (f1, f'{f1:.0f} Hz'), (15000, '15 kHz')):
        s += txt(p.X(lx(f)), p.T + p.H + 20, lab, 13, MUT, 700)
    s += line(p.X(lx(f1)), p.T, p.X(lx(f1)), p.T + p.H, MUT, 2, '5 6')
    s += p.curve(lambda u: H(10 ** u), 2, lx(15000), n=120, c=O, w=5) + p.curve(lambda u: -H(10 ** u), 2, lx(15000), n=120, c=B, w=5)
    s += tag(p.X(lx(15000)) - 6, p.Y(H(15000)) + 30, f'pre: +{H(15000):.1f}', O, 13, 'end')
    s += tag(p.X(lx(15000)) - 6, p.Y(-H(15000)) - 18, f'de: −{H(15000):.1f}', B, 13, 'end')
    s += tag(p.X(lx(f1)) - 8, p.Y(H(f1)) - 14, f'+{H(f1):.2f} dB', O, 12, 'end')
    s += txt(p.X(2.05), p.Y(0) + 24, 'product: flat for the music', 13, G, 900, 'start')
    s += txt(p.L, 362, 'swapped, the noise power rises 31 times', 13, O, 900, 'start')
    return 'Boost before, cut after', s
D['ec-comm-u3-L4'] = (u3L4, 'before the modulator', '3.7.1')


# ---------------- unit 4 ----------------
def u4L1():
    # 4 kHz tone sampled at 7 kS/s: the same samples as a 3 kHz tone (fold at 3.5 kHz)
    fsa, f, fa = 7, 4, 7 - 4
    p = Plot(0, 1.0, -1.25, 1.25, L=46, T=20, Wd=440, H=220)
    s = defs() + sax(p, xt=[i / 7 for i in range(8)], yt=(-1, 0, 1), xfmt=lambda v: f'{v * 1000:.0f}', yl='x(t)')
    s += p.curve(lambda t: math.cos(2 * math.pi * f * t), 0, 1, n=500, c=B, w=4)
    s += p.curve(lambda t: math.cos(2 * math.pi * fa * t), 0, 1, n=500, c=O, w=4, dash='9 7')
    for n in range(8):
        t = n / fsa
        s += line(p.X(t), p.Y(0), p.X(t), p.Y(math.cos(2 * math.pi * f * t)), INK, 2, '3 4')
        s += dot(*p.P(t, math.cos(2 * math.pi * f * t)), 9, INK)
    s += txt(p.L + p.W + 8, p.T + p.H + 44, 't (µs) →', 13, MUT, 700, 'end')
    s += tag(70, 320, f'{f} kHz sent', B, 14, 'start') + tag(205, 320, f'{fa} kHz seen', O, 14, 'start')
    s += txt(500, 362, f'one sample every {1000 / fsa:.0f} µs, Nyquist needs {2 * f} kS/s', 13, MUT, 800, 'end')
    return 'Same dots, two tones', s
D['ec-comm-u4-L1'] = (u4L1, '4 kHz at 7 kS/s → 3 kHz', '4.1.1')


def u4L2():
    # 8-bit uniform PCM: full-scale sine 6.02n + 1.76 = 49.9 dB; speech with 4-sigma peaks 40.9 dB; mu-law (255) holds steady
    n = 8; L_ = 2 ** n
    def sqnr(level_db, comp):
        A = 10 ** (level_db / 20); mu = 255
        N = 4000; num = den = 0.0
        for i in range(N):
            x = A * math.sin(2 * math.pi * (i + 0.37) / N)
            y = math.copysign(math.log(1 + mu * abs(x)) / math.log(1 + mu), x) if comp else x
            q = (math.floor(y * L_ / 2) + 0.5) / (L_ / 2)
            q = max(-1 + 1 / L_, min(1 - 1 / L_, q))
            xr = math.copysign(((1 + mu) ** abs(q) - 1) / mu, q) if comp else q
            num += x * x; den += (x - xr) ** 2
        return 10 * math.log10(num / den)
    p = Plot(-40, 0, 0, 55, L=50, T=24, Wd=430, H=230)
    s = defs() + sax(p, xt=(-40, -30, -20, -10, 0), yt=(0, 10, 20, 30, 40, 50), xl='sine level below full scale (dB) →', yl='SQNR (dB)')
    lv = [-40 + i for i in range(41)]
    s += poly([p.P(v, 6.02 * n + 1.76 + v) for v in lv], O, 4.5)
    s += poly([p.P(v, sqnr(v, True)) for v in lv[::2]], B, 4.5)
    full = 6.02 * n + 1.76; sp = 6.02 * n + 4.77 - 20 * math.log10(4)
    s += dot(*p.P(0, full), 9, O) + tag(p.X(0) - 12, p.Y(full) - 14, f'full-scale sine {full:.1f}', O, 13, 'end')
    s += line(p.X(0) - 4, p.Y(sp), p.X(0) - 4, p.Y(17), G, 2.5, '4 4') + dot(*p.P(0, sp), 9, G) + tag(p.X(0) + 4, p.Y(15), f'speech, 4σ peaks: {sp:.1f}', G, 13, 'end')
    s += txt(p.X(-39), p.Y(31), 'μ-law', 14, B, 900, 'start') + txt(p.X(-37), p.Y(4), 'uniform', 14, O, 900, 'start')
    return 'SQNR depends on the signal', s
D['ec-comm-u4-L2'] = (u4L2, 'speech: 40.9 dB', '4.3.1')


def u4L3():
    # delta modulation: 500 Hz, 1 V tone at 8 kS/s, step 0.3 V: slope 3142 V/s against 2400 V/s
    f, A, fs, d = 500, 1.0, 8000, 0.3
    smax, sdm = 2 * math.pi * f * A, d * fs
    N = 20
    xs = [A * math.sin(2 * math.pi * f * n / fs) for n in range(N + 1)]
    st, bits, v = [], [], 0.0
    for n in range(N):
        b = 1 if xs[n] >= v else 0
        v += d if b else -d
        bits.append(b); st.append(v)
    p = Plot(0, N, -1.6, 1.6, L=46, T=14, Wd=450, H=230)
    s = defs() + sax(p, yt=(-1.5, -1, 0, 1, 1.5), yl='volts', fmt=lambda v: g(v))
    s += p.curve(lambda n: A * math.sin(2 * math.pi * f * n / fs), 0, N, n=200, c=B, w=4.5)
    pts = [p.P(0, 0)]
    for n in range(N):
        pts += [p.P(n, st[n]), p.P(n + 1, st[n])]
    s += poly(pts, O, 3.5)
    # granular region near the peak, overload on the falling slope
    s += rect(p.X(3) - 4, p.Y(1.55), p.X(6) - p.X(3) + 8, p.Y(0.4) - p.Y(1.55), 'none', G, 2.5, 10, '6 5')
    s += txt(p.X(6) + 10, p.Y(1.45), 'hunting', 13, G, 900, 'start')
    s += tag(p.X(10.5), p.Y(0.85), 'overload: lags', O, 13)
    for n, b in enumerate(bits):
        s += txt(p.X(n + 0.5), p.T + p.H + 24, str(b), 14, INK if b else MUT, 900)
    s += txt(p.L - 8, p.T + p.H + 24, 'bits', 12, MUT, 800, 'end')
    s += txt(p.L, p.T + p.H + 62, f'tone slope 2πfA = {smax:.0f} V/s, staircase Δ·fs = {sdm:.0f} V/s', 13, MUT, 800, 'start')
    return 'A staircase chasing a sine', s
D['ec-comm-u4-L3'] = (u4L3, 'slope 2πfA > Δ·fs', '4.6.1')


def u4L4():
    # bits 1 0 1 1 0 in polar NRZ and Manchester (1 = low-to-high); PSDs: NRZ first null at Rb, Manchester at 2Rb
    bits = [1, 0, 1, 1, 0]
    s = defs()
    x0, bw = 120, 70
    for r, (name, c) in enumerate((('polar NRZ', B), ('Manchester', O))):
        yc = 40 + r * 62; a = 20
        s += txt(x0 - 12, yc + 5, name, 14, c, 900, 'end')
        pts = []
        for i, b in enumerate(bits):
            xa, xm, xb = x0 + bw * i, x0 + bw * i + bw / 2, x0 + bw * (i + 1)
            if r == 0: pts += [(xa, a if b else -a), (xb, a if b else -a)]
            else: pts += [(xa, -a), (xm, -a), (xm, a), (xb, a)] if b else [(xa, a), (xm, a), (xm, -a), (xb, -a)]
        s += poly([(x, yc - y) for x, y in pts], c, 4)
        if r == 0:
            for i, b in enumerate(bits):
                s += txt(x0 + bw * i + bw / 2, yc - 28, str(b), 14, INK, 900)
    nrz = lambda f: sinc(f) ** 2
    man = lambda f: sinc(f / 2) ** 2 * math.sin(math.pi * f / 2) ** 2
    p = Plot(0, 3, 0, 1.05, L=50, T=160, Wd=430, H=150)
    s += sax(p, xt=(0, 1, 2, 3), yt=(0, 0.5, 1), xfmt=lambda v: {0: '0', 1: 'Rb', 2: '2Rb', 3: '3Rb'}[v], xl='f →', yl='PSD')
    s += p.curve(nrz, 0, 3, n=200, c=B, w=4) + p.curve(man, 0, 3, n=200, c=O, w=4.5)
    s += dot(*p.P(1, 0), 8, B) + dot(*p.P(2, 0), 9, O)
    s += tag(p.X(2), p.Y(0.42), 'Manchester null: 2Rb', O, 13) + tag(p.X(0.75), p.Y(0.88), 'NRZ null: Rb', B, 13)
    return 'Half-bit pulses, double width', s
D['ec-comm-u4-L4'] = (u4L4, 'first null at 2Rb', '4.8.1')


# ---------------- unit 5 ----------------
def u5L1():
    # 4800 baud: Nyquist 2400 Hz; raised cosine B = (Rs/2)(1 + alpha): alpha 0.5 -> 3600 Hz, alpha 1 -> 4800 Hz
    Rs = 4800; W0 = Rs / 2
    def rc(f, al):
        f = abs(f)
        if al == 0: return 1.0 if f <= W0 else 0.0
        f1 = W0 * (1 - al); f2 = W0 * (1 + al)
        if f <= f1: return 1.0
        if f >= f2: return 0.0
        return 0.5 * (1 + math.cos(math.pi * (f - f1) / (f2 - f1)))
    p = Plot(0, 5600, 0, 1.25, L=50, T=24, Wd=430, H=220)
    s = defs() + sax(p, xt=(0, 1200, 2400, 3600, 4800), yt=(0, 0.5, 1), xl='f (Hz) →', yl='P(f)')
    s += poly([p.P(0, 1), p.P(W0, 1), p.P(W0, 0)], MUT, 3, '7 6')
    s += p.curve(lambda f: rc(f, 1), 0, 5600, n=300, c=G, w=4)
    s += p.curve(lambda f: rc(f, 0.5), 0, 5600, n=300, c=B, w=5)
    s += dot(*p.P(W0, 0.5), 8, B)
    for al, c, yy in ((0, MUT, 1.15), (0.5, B, 0.93), (1, G, 0.71)):
        f2 = W0 * (1 + al)
        if al: s += dot(*p.P(f2, 0), 9, c)
        s += tag(p.X(5550), p.Y(yy), f'α = {g(al)}: {f2:g} Hz', c, 13, 'end')
    s += txt(p.L, p.T + p.H + 64, f'B = (Rs/2)(1 + α): {W0:g} × 1.5 = {W0 * 1.5:g} Hz at {Rs} baud', 13, INK, 900, 'start')
    return 'Roll-off widens the band', s
D['ec-comm-u5-L1'] = (u5L1, '2400 × 1.5 = 3600 Hz', '5.2.1')


def u5L2():
    # channel 0.2, 1, 0.3; 3-tap zero-forcing equalizer
    x = {-1: 0.2, 0: 1.0, 1: 0.3}
    # solve exactly: v(-1)=c-1 x0 + c0 x-1 = 0 ; v(1)=c0 x1 + c1 x0 = 0 ; v(0)=c-1 x1 + c0 x0 + c1 x-1 = 1
    cm1f, c1f = -x[-1], -x[1]
    c0 = 1 / (cm1f * x[1] + 1 + c1f * x[-1])
    c = {-1: cm1f * c0, 0: c0, 1: c1f * c0}
    v = {n: sum(c[k] * x.get(n - k, 0) for k in c) for n in range(-2, 3)}
    pd0 = (x[-1] + x[1]) / x[0]
    pd1 = sum(abs(v[n]) for n in v if n) / v[0]
    s = defs()
    for row, (vals, col, head, y0) in enumerate(((x, O, f'channel: peak ISI {pd0:g}', 150), (v, B, f'equalized: peak ISI {pd1:.3f}', 330))):
        s += txt(20, y0 - 122, head, 16, col, 900, 'start')
        s += line(40, y0, 490, y0, MUT, 2.5, arrow=True)
        for n in range(-2, 3):
            xx = 265 + n * 90; val = vals.get(n, 0)
            s += txt(xx, y0 + 22, g(n), 13, MUT, 700)
            if abs(val) < 1e-9:
                s += f'<circle cx="{xx}" cy="{y0}" r="7" fill="{W}" stroke="{col}" stroke-width="3"/>'
                continue
            yy = y0 - 90 * val
            s += line(xx, y0, xx, yy, col, 5) + f'<circle cx="{xx}" cy="{yy:.1f}" r="8" fill="{col}"/>'
            lab = f'{val:.4f}'.rstrip('0').rstrip('.') if n else '1'
            if val > 0: s += txt(xx + 12, yy - 8, lab, 14, INK, 900, 'start')
            else: s += txt(xx - 12 if n < 0 else xx + 12, yy - 6, lab.replace('-', '−'), 14, INK, 900, 'end' if n < 0 else 'start')
    s += txt(500, 372, f'taps {c[-1]:.3f}, {c[0]:.3f}, {c[1]:.3f}'.replace('-', '−'), 13, MUT, 800, 'end')
    return 'Zero the two neighbours', s
D['ec-comm-u5-L2'] = (u5L2, 'ISI 0.5 → 0.148', '5.3.1')


def u5L3():
    # matched filter for a 1 V, 1 ms rectangle: output a triangle peaking at E = A^2 T = 1 mJ at t = T
    A, T = 1, 1e-3
    E = A * A * T
    N0 = 2e-6
    snr = 2 * E / N0
    tri = lambda t: E * 1e3 * max(0, 1 - abs(t - 1))             # t in units of T, y in mJ
    p = Plot(0, 2.2, 0, 1.2, L=50, T=26, Wd=430, H=230)
    s = defs() + sax(p, xt=(0, 0.8, 1, 2), yt=(0, 0.8, 1), xfmt=lambda v: {0: '0', 0.8: '0.8T', 1: 'T', 2: '2T'}[v], yl='output (mJ)')
    s += area(p, tri, 0, 2, B, op=.15) + p.curve(tri, 0, 2.2, n=220, c=B, w=5)
    s += line(p.X(1), p.Y(0), p.X(1), p.Y(1), G, 2.5, '6 6') + line(p.X(0.8), p.Y(0), p.X(0.8), p.Y(0.8), O, 2.5, '6 6')
    s += dot(*p.P(1, 1), 11, G) + dot(*p.P(0.8, 0.8), 9, O)
    s += tag(p.X(1) + 16, p.Y(1) + 6, f'E = {E * 1e3:g} mJ at T', G, 14, 'start')
    s += tag(p.X(0.8) - 14, p.Y(0.8) + 6, '0.8E: too early', O, 13, 'end')
    # the input and the filter, small
    s += rect(p.X(1.62), p.Y(0.82), 30, 30, BS, B, 2, 3) + txt(p.X(1.62) + 38, p.Y(0.82) + 21, f's(t): {A} V, {T * 1e3:g} ms', 13, B, 800, 'start')
    s += txt(p.L, p.T + p.H + 62, f'max SNR = 2E/N0 = {snr:g}, which is {db(snr):.0f} dB', 14, INK, 900, 'start')
    return 'The peak lands at t = T', s
D['ec-comm-u5-L3'] = (u5L3, '2E/N₀ = 1000 = 30 dB', '5.5.1')


# ---------------- unit 6 ----------------
def u6L1():
    # BER against Eb/N0: BPSK Q(sqrt(2x)), DPSK 0.5 e^-x, coherent BFSK Q(sqrt(x)), non-coherent BFSK 0.5 e^-x/2
    curves = [('BPSK', lambda x: Qf(math.sqrt(2 * x)), B), ('DPSK', lambda x: 0.5 * math.exp(-x), G),
              ('BFSK', lambda x: Qf(math.sqrt(x)), O), ('NC-BFSK', lambda x: 0.5 * math.exp(-x / 2), '#9B7BEA')]
    p = Plot(0, 16, -8, 0, L=60, T=20, Wd=420, H=250)
    s = defs()
    for e in range(-8, 0):
        s += line(p.L, p.Y(e), p.L + p.W, p.Y(e), GRID, 1.5)
        if e % 2 == 0: s += rtxt(p.L - 8, p.Y(e) + 5, f'10^{{{e}}}'.replace('-', '−'), 13, MUT, 700, 'end')
    s += line(p.L, p.T + p.H, p.L + p.W + 8, p.T + p.H, MUT, 2.5, arrow=True) + line(p.L, p.T + p.H, p.L, p.T - 6, MUT, 2.5, arrow=True)
    for v in (0, 4, 8, 10, 12, 16):
        s += txt(p.X(v), p.T + p.H + 20, g(v), 13, MUT, 700)
    s += txt(p.L + p.W, p.T + p.H + 40, 'Eb/N0 (dB) →', 13, MUT, 700, 'end') + txt(p.L + 8, p.T - 6, 'bit error rate', 13, MUT, 700, 'start')
    for n, f, c in curves:
        pts = []
        for i in range(161):
            d = 16 * i / 160; pb = f(10 ** (d / 10))
            if pb > 1e-8: pts.append(p.P(d, math.log10(pb)))
        s += poly(pts, c, 4.5 if n == 'BPSK' else 3.5)
        i = [c_[0] for c_ in curves].index(n)
        s += line(p.X(0.6), p.Y(-5.6 - 0.62 * i), p.X(1.8), p.Y(-5.6 - 0.62 * i), c, 5) + txt(p.X(2.1), p.Y(-5.6 - 0.62 * i) + 5, n, 13, c, 900, 'start')
    pb = Qf(math.sqrt(20))
    s += dot(*p.P(10, math.log10(pb)), 9, B) + rtag(p.X(10) - 14, p.Y(math.log10(pb)) + 6, f'{sci(pb)} at 10 dB', B, 12, 'end')
    return 'Furthest left wins', s
D['ec-comm-u6-L1'] = (u6L1, 'BPSK makes the fewest', '6.3.1')


def u6L2():
    # Gray 16-QAM: first two bits pick I, last two pick Q (00 -3a, 01 -a, 11 +a, 10 +3a); 1011 -> (3a, a); log2 16 = 4 bits
    gray = {'00': -3, '01': -1, '11': 1, '10': 3}
    M = 16; kbits = int(math.log2(M))
    s = defs()
    cx, cy, u = 185, 190, 44
    s += line(cx - 4.3 * u, cy, cx + 4.3 * u, cy, MUT, 2, arrow=True) + line(cx, cy + 4.1 * u, cx, cy - 4.1 * u, MUT, 2, arrow=True)
    s += txt(cx + 4.3 * u, cy + 22, 'I', 15, MUT, 900) + txt(cx + 14, cy - 3.9 * u, 'Q', 15, MUT, 900)
    for t in (-2, 2):
        s += line(cx + t * u, cy - 3.9 * u, cx + t * u, cy + 3.9 * u, GRID, 2, '6 6') + line(cx - 4.1 * u, cy - t * u, cx + 4.1 * u, cy - t * u, GRID, 2, '6 6')
    for bi, iv in gray.items():
        for bq, qv in gray.items():
            x, y = cx + iv * u, cy - qv * u
            hit = bi + bq == '1011'
            s += dot(x, y, 10 if hit else 7, O if hit else B)
            s += txt(x, y + 22, bi + bq, 11 if not hit else 13, O if hit else INK, 900)
    for v in (-3, -1, 1, 3):
        s += txt(cx + v * u, cy + 4.1 * u + 6, {-3: '−3a', -1: '−a', 1: 'a', 3: '3a'}[v], 12, MUT, 800)
    s += txt(500, 60, f'{M} points', 18, INK, 900, 'end') + txt(500, 90, f'log₂ {M} = {kbits} bits', 18, B, 900, 'end')
    s += txt(500, 150, 'I bits 10 → +3a', 14, INK, 800, 'end') + txt(500, 174, 'Q bits 11 → +a', 14, INK, 800, 'end')
    s += txt(500, 230, '20 Mb/s →', 13, MUT, 800, 'end') + txt(500, 250, '5 Msymbol/s', 13, MUT, 800, 'end')
    return 'Sixteen points, four bits', s
D['ec-comm-u6-L2'] = (u6L2, 'log₂ 16 = 4 bits', '6.5.1')


def u6L3():
    # OFDM (802.11a): 20 MHz / 64 = 312.5 kHz spacing, Tu 3.2 us, CP 16 x 50 ns = 0.8 us -> 4 us, 20 % overhead; 384 bits / 4 us = 96 Mb/s, not 120
    B_, N = 20e6, 64
    df = B_ / N; Tu = 1 / df; Tcp = 16 / B_; Ts = Tu + Tcp
    bits = N * 6
    p = Plot(-3.2, 3.2, -0.3, 1.1, L=30, T=16, Wd=460, H=150)
    s = defs()
    s += line(p.L, p.Y(0), p.L + p.W + 8, p.Y(0), MUT, 2.5, arrow=True)
    for k, c in zip(range(-2, 3), [G, B, O, B, G]):
        s += p.curve(lambda f, k=k: sinc(f - k), -3.2, 3.2, n=400, c=c, w=3.5 if k else 5)
    s += arrow2(p.X(0), p.Y(-0.2), p.X(1), p.Y(-0.2), INK, 2) + txt(p.X(0.5), p.Y(-0.2) + 22, f'{df / 1e3:g} kHz', 13, INK, 900)
    y = 230; X = lambda t: 40 + t / 4.4 * 440
    s += rect(X(0), y, X(Tcp * 1e6) - X(0), 46, OS, O, 2.5, 6) + rect(X(Tcp * 1e6), y, X(Ts * 1e6) - X(Tcp * 1e6), 46, BS, B, 2.5, 6)
    s += txt((X(0) + X(Tcp * 1e6)) / 2, y + 29, f'{Tcp * 1e6:g}', 15, O, 900) + txt((X(Tcp * 1e6) + X(Ts * 1e6)) / 2, y + 29, f'useful {Tu * 1e6:g} µs', 15, B, 900)
    s += txt(X(0), y - 10, f'prefix: {Tcp / Ts * 100:.0f} % of {Ts * 1e6:g} µs', 14, O, 900, 'start')
    s += txt(X(0), y + 80, f'{bits} bits / {Ts * 1e6:g} µs = {bits / Ts / 1e6:g} Mb/s', 16, INK, 900, 'start')
    s += txt(X(0), y + 108, f'not / {Tu * 1e6:g} µs = {bits / Tu / 1e6:g} Mb/s', 15, O, 900, 'start')
    return 'The prefix is paid air time', s
D['ec-comm-u6-L3'] = (u6L3, '0.8 of 4 µs = 20 %', '6.9.1')


# ---------------- unit 7 ----------------
def u7L1():
    # Huffman, A 0.4, B 0.2, C 0.2, D 0.1, E 0.1: two tie-breaks give lengths 1,2,3,4,4 and 2,2,2,3,3; both average 2.2 bits
    P = {'A': 0.4, 'B': 0.2, 'C': 0.2, 'D': 0.1, 'E': 0.1}
    c1 = {'A': '0', 'B': '10', 'C': '110', 'D': '1110', 'E': '1111'}
    c2 = {'B': '00', 'C': '01', 'A': '10', 'D': '110', 'E': '111'}
    L1 = sum(P[k] * len(c1[k]) for k in P); L2 = sum(P[k] * len(c2[k]) for k in P)
    s = defs()
    def node(x, y, lab):
        return f'<circle cx="{x}" cy="{y}" r="15" fill="{MINT}" stroke="{G}" stroke-width="3"/>' + txt(x, y + 5, lab, 11, INK, 900)
    def leaf(x, y, k, code):
        return box(x - 20, y - 15, 40, 30, k, O, 15, fill=OS) + txt(x, y + 32, code, 13, INK, 900)
    def edge(x1, y1, x2, y2, b):
        return line(x1, y1 + 15, x2, y2 - 15, G if b == '0' else B, 3)
    # tree 1: spine
    sp = [(40, 40), (90, 100), (140, 160), (190, 220)]
    lv = [('A', 15, 110), ('B', 65, 170), ('C', 115, 230), ('D', 160, 290), ('E', 225, 290)]
    for i, (x, y) in enumerate(sp):
        nx, ny = sp[i + 1] if i < 3 else (lv[4][1], lv[4][2])
        s += edge(x, y, lv[i][1], lv[i][2], '0') + edge(x, y, nx, ny, '1')
    for (x, y), pr in zip(sp, ('1.0', '0.6', '0.4', '0.2')):
        s += node(x, y, pr)
    for k, x, y in lv:
        s += leaf(x, y, k, c1[k])
    # tree 2: minimum variance
    r = (390, 40); n4 = (330, 120); n6 = (450, 120); nde = (480, 200)
    l2 = {'B': (300, 200), 'C': (360, 200), 'A': (420, 200), 'D': (450, 280), 'E': (510, 280)}
    s += edge(*r, *n4, '0') + edge(*r, *n6, '1') + edge(*n4, *l2['B'], '0') + edge(*n4, *l2['C'], '1')
    s += edge(*n6, *l2['A'], '0') + edge(*n6, *nde, '1') + edge(*nde, *l2['D'], '0') + edge(*nde, *l2['E'], '1')
    for (x, y), pr in ((r, '1.0'), (n4, '0.4'), (n6, '0.6'), (nde, '0.2')):
        s += node(x, y, pr)
    for k, (x, y) in l2.items():
        s += leaf(x, y, k, c2[k])
    s += line(262, 30, 262, 330, GRID, 2, '6 6')
    s += txt(130, 362, f'lengths 1,2,3,4,4: L = {L1:.1f}', 13, B, 900) + txt(400, 362, f'lengths 2,2,2,3,3: L = {L2:.1f}', 13, B, 900)
    return 'Two trees, one average', s
D['ec-comm-u7-L1'] = (u7L1, 'both average 2.2 bits', '7.2.1')


def u7L2():
    # C/B = log2(1 + S/N): 0 dB -> 1, 20 dB -> 6.66, 30 dB -> 9.97; 3.1 kHz at 30 dB -> 30.9 kb/s; above the curve no code works
    Bw = 3100
    cap = lambda d: math.log2(1 + 10 ** (d / 10))
    p = Plot(-10, 40, 0, 14, L=50, T=26, Wd=430, H=240)
    s = defs() + sax(p, xt=(-10, 0, 10, 20, 30, 40), yt=(0, 2, 4, 6, 8, 10, 12, 14), xl='SNR (dB) →', yl='bits per hertz')
    up = [p.P(-10, 14)] + [p.P(-10 + 50 * i / 100, cap(-10 + 50 * i / 100)) for i in range(101)] + [p.P(40, 14)]
    s += f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in up)}" fill="{O}" fill-opacity=".14" stroke="none"/>'
    s += area(p, cap, -10, 40, G, op=.14) + p.curve(cap, -10, 40, n=200, c=B, w=5)
    for d, c in ((0, G), (20, G), (30, B)):
        s += dot(*p.P(d, cap(d)), 9, c) + tag(p.X(d) + 12, p.Y(cap(d)) + 26, f'{cap(d):.2f}' if d else '1', c, 13, 'start')
    s += txt(p.X(-8), p.Y(12.4), 'no code works here', 15, O, 900, 'start')
    s += txt(p.X(24), p.Y(1.2), 'reliable codes exist', 14, G, 900)
    s += tag(p.X(39.5), p.Y(3.7), f'× {Bw / 1e3:g} kHz = {Bw * cap(30) / 1e3:.1f} kb/s', B, 13, 'end')
    return 'Below the curve, or not at all', s
D['ec-comm-u7-L2'] = (u7L2, 'C = B log₂(1 + S/N)', '7.4.1')


def u7L3():
    # K = 3, rate 1/2, g = 111, 101: 2^(K-1) = 4 states; input 1011 + two flush zeros: 00 -> 10 -> 01 -> 10 -> 11 -> 01 -> 00
    K = 3; ns = 2 ** (K - 1)
    states = ['00', '10', '01', '11']
    nxt = lambda st, u: str(u) + st[0]
    def out(st, u):
        r = [u, int(st[0]), int(st[1])]
        return f'{r[0] ^ r[1] ^ r[2]}{r[0] ^ r[2]}'
    msg = [1, 0, 1, 1, 0, 0]
    path = ['00']
    for u in msg: path.append(nxt(path[-1], u))
    outs = [out(path[i], msg[i]) for i in range(len(msg))]
    s = defs()
    x0, dx, y0, dy = 80, 72, 40, 70
    X = lambda t: x0 + t * dx; Y = lambda st: y0 + states.index(st) * dy
    reach = [{'00'}]
    for t in range(len(msg)):
        nr = set()
        for st in reach[-1]:
            for u in ((0, 1) if t < len(msg) - 2 else (0,)):
                n2 = nxt(st, u); nr.add(n2)
                s += line(X(t), Y(st), X(t + 1), Y(n2), '#CBD5E1', 2.5, '5 5' if u else None)
        reach.append(nr)
    for t in range(len(msg)):
        s += line(X(t), Y(path[t]), X(t + 1), Y(path[t + 1]), O, 6)
        rx = outs[t] if t != 3 else '11'
        s += txt((X(t) + X(t + 1)) / 2, y0 + 4 * dy - 2, rx, 15, O if t == 3 else INK, 900)
    for t in range(len(msg) + 1):
        for st in states:
            if st in reach[t]: s += f'<circle cx="{X(t)}" cy="{Y(st)}" r="9" fill="{W}" stroke="{B}" stroke-width="3"/>'
    for st in states:
        s += txt(x0 - 22, Y(st) + 5, st, 15, B, 900, 'end')
    s += txt(x0 - 22, y0 + 4 * dy - 2, 'rx', 13, MUT, 800, 'end')
    s += tag(X(3.5), y0 + 4 * dy + 26, 'one flipped bit', O, 12)
    s += txt(20, 372, f'state = K − 1 = {K - 1} bits: {ns} states, decoded 1011', 13, INK, 900, 'start')
    return 'Four states, one survivor', s
D['ec-comm-u7-L3'] = (u7L3, '2ᴷ⁻¹ = 4 states', '7.8.1')
