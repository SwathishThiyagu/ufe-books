"""Claude's hand-drawn figures for ec-optical-u4 (Optical detectors and receivers), one per chapter.
Every curve and number is computed from that chapter's own worked example; colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
q, kB, T300 = 1.602e-19, 1.38e-23, 300.0


def curve(f, a, b, fx, fy, n=200, c=AC, w=2.5, dash=None):
    return P([(fx(a + (b - a) * i / n), fy(f(a + (b - a) * i / n))) for i in range(n + 1)], c, w, dash)


def SUP(base, exp, rest=''):
    """svg text with a raised exponent; the rest of the label goes back to the base line"""
    return f'{base}<tspan dy="-6" font-size="11">{exp}</tspan><tspan dy="6">{rest}</tspan>'


def SUB(base, sub, rest=''):
    """svg text with a lowered subscript; the rest of the label goes back to the base line"""
    return f'{base}<tspan dy="4" font-size="11">{sub}</tspan><tspan dy="-4">{rest}</tspan>'


# ---- 4.1 responsivity against wavelength: the ceiling, two diodes and the two worked examples ----
def f1():
    o = []
    x0, x1, y0, y1 = 80, 690, 40, 320
    fx = lambda l: x0 + (l - 0.6) / (1.8 - 0.6) * (x1 - x0)
    fy = lambda r: y1 - r / 1.5 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8], [0, 0.5, 1.0, 1.5], fx, fy,
                  'wavelength λ (µm)', 'R (A/W)', lambda v: f'{v:.1f}', lambda v: f'{v:.1f}'))
    # ceiling eta = 1
    o.append(curve(lambda l: l / 1.24, 0.6, 1.8, fx, fy, 2, MUT, 2, '7 5'))
    o.append(Tb(fx(1.62), fy(1.62 / 1.24) - 12, 'ceiling η = 1: R = λ/1.24', 13, 'end', MUT))
    # silicon, eta = 0.8, cut off at 1.11 um
    o.append(P([(fx(0.6), fy(0.8 * 0.6 / 1.24)), (fx(1.107), fy(0.8 * 1.107 / 1.24)), (fx(1.107), fy(0))], AC, 3))
    o.append(T(fx(0.66), fy(0.8 * 0.66 / 1.24) + 30, 'Si, η = 0.8', 14, 'start', AC, True))
    o.append(Tb(fx(1.107) + 6, fy(0.18), SUB('λ', 'c', ' = 1.11 µm'), 13, 'start', AC))
    # InGaAs, eta = 0.72, cut off at 1.65 um
    o.append(P([(fx(1.0), fy(0.72 * 1.0 / 1.24)), (fx(1.653), fy(0.72 * 1.653 / 1.24)), (fx(1.653), fy(0))], LV, 3))
    o.append(T(fx(1.25), fy(0.72 * 1.25 / 1.24) + 30, 'InGaAs, η = 0.72', 14, 'start', LV, True))
    o.append(Tb(fx(1.653) + 6, fy(0.40), SUB('λ', 'c', ' = 1.65 µm'), 13, 'start', LV))
    # the two worked examples
    o.append(L(fx(0.85), fy(0), fx(0.85), fy(0.548), L2, 1.2, '3 3'))
    o.append(C(fx(0.85), fy(0.548), 6, AC))
    o.append(Tb(fx(0.85) - 2, fy(0.548) - 26, 'Example 1: 0.548 A/W', 13, 'middle', INK))
    o.append(C(fx(1.55), fy(0.90), 6, LV))
    o.append(Tb(fx(1.55) - 12, fy(0.90) - 14, 'Example 2: 0.90 A/W', 13, 'end', INK))
    return 370, ''.join(o)


FIG[1] = (f1, 'R = ηλ/1.24 rises with wavelength until the cutoff λ<sub>c</sub> = 1.24/E<sub>g</sub>, where it drops to zero. The dots are the two worked examples: '
              'silicon at 0.85 µm (0.548 A/W) and InGaAs at 1.55 µm (0.90 A/W); the dashed line is the η = 1 ceiling.',
          'Responsivity in amperes per watt against wavelength from 0.6 to 1.8 micrometres. A dashed ceiling line R equals lambda over 1.24. '
          'Silicon with efficiency 0.8 rises to 0.71 at 1.11 micrometres and drops to zero; InGaAs with efficiency 0.72 rises to 0.96 at 1.65 micrometres and drops to zero. '
          'Points mark 0.548 at 0.85 micrometres and 0.90 at 1.55 micrometres.')


# ---- 4.2 the PIN layers with the light absorbed across the i layer, and the field ----
def f2():
    o = []
    yt, yb = 96, 236
    xa, xp, xi, xn, xe = 56, 70, 112, 552, 640
    o.append(R(xa, yt, xp - xa, yb - yt, ACS, AC, 2, 1.5))
    o.append(R(xp, yt, xi - xp, yb - yt, NXS, NX, 2, 1.5))
    o.append(R(xi, yt, xn - xi, yb - yt, PANEL, L2, 2, 1.5))
    o.append(R(xn, yt, xe - xn, yb - yt, LVS, LV, 2, 1.5))
    o.append(T((xp + xi) / 2, yt - 10, 'p⁺', 15, bold=True))
    o.append(T((xi + xn) / 2, yt - 10, 'i layer (intrinsic), fully depleted', 14, bold=True))
    o.append(T((xn + xe) / 2, yt - 10, 'n⁺', 15, bold=True))
    o.append(T(xa - 2, yt - 30, 'AR coating, r = 0.03', 13, 'start', MUT))
    o.append(L(xa + 8, yt - 26, xa + 8, yt - 2, MUT, 1.2))
    # light arrow
    o.append(L(14, 166, xa - 4, 166, NX, 3, arrow='x'))
    o.append(T(16, 150, 'light', 14, 'start', NX, True))
    # power left in the i layer: 0.97 e^(-alpha x), alpha w = 4
    fx = lambda u: xi + u / 4.0 * (xn - xi)
    fy = lambda v: yb - 12 - v * (yb - yt - 30)
    o.append(curve(lambda u: 0.97 * math.exp(-u), 0, 4, fx, fy, 120, NX, 3))
    o.append(Tb(fx(0.35) + 6, fy(0.97) + 4, '0.97 P enters', 13, 'start', NX))
    o.append(Tb(fx(1.0) + 8, fy(0.357) - 8, SUP('P(x) = 0.97P e', '−αx'), 13, 'start', NX))
    o.append(Tb(fx(3.95), fy(0.018) - 14, 'left at x = w: 1.8 %', 13, 'end', MUT))
    # carriers
    o.append(C(fx(0.5), 222, 6, AC)); o.append(L(fx(0.5) + 8, 222, fx(0.5) + 70, 222, AC, 2.5, arrow='n'))
    o.append(T(fx(0.5) + 76, 227, 'electron to n⁺', 13, 'start', AC))
    o.append(C(fx(3.3), 140, 6, LV)); o.append(L(fx(3.3) - 8, 140, fx(3.3) - 70, 140, LV, 2.5, arrow='l'))
    o.append(T(fx(3.3) - 76, 145, 'hole to p⁺', 13, 'end', LV))
    # width bracket
    o.append(brace(xi, xn, 252, INK))
    o.append(T((xi + xn) / 2, 278, 'w = 4 µm: αw = 4, η = 0.97 × 0.982 = 0.952, transit 61.5 ps', 14))
    # field profile
    ye, yz = 312, 360
    o.append(L(xa, yz, xe, yz, L2, 1.5))
    o.append(P([(xa, yz), (xp + 30, yz), (xi, ye), (xn, ye), (xn + 12, yz), (xe, yz)], AC, 3))
    o.append(T(xa, ye - 6, 'field E(x)', 14, 'start', MUT))
    o.append(T((xi + xn) / 2, ye - 8, 'strong, nearly uniform field sweeps every pair out', 13, fill=AC))
    o.append(T(xe, yz + 22, SUB('reverse bias across the diode, load R', 'L', ' = 50 Ω'), 13, 'end', MUT))
    return 392, ''.join(o)


FIG[2] = (f2, 'The worked example\'s InGaAs PIN: light enters through the coating and the thin p⁺ layer, and its power falls as it is absorbed across the 4 µm i layer, '
              'so only 1.8 % is left at the far side. The field below is strong across the whole i layer, so each pair is swept out: electrons to n⁺, holes to p⁺.',
          'Layer diagram: antireflection coating, thin p plus layer, wide i layer of 4 micrometres, n plus layer. A curve inside the i layer shows the light power '
          'falling from 0.97 of the input to 1.8 percent. Below, the electric field is near zero in p plus and n plus and high and flat across the i layer.')


# ---- 4.3 the reach-through APD and SNR against gain from the worked example ----
def f3():
    o = []
    # top: the layer stack and its field
    y0, y1 = 50, 110
    xs = [40, 96, 196, 600, 680]
    names = [('n⁺', LVS, LV), ('p: gain', ACS, AC), ('π: absorption (wide, low field)', PANEL, L2), ('p⁺', NXS, NX)]
    for (nm, fl, st), a, b in zip(names, xs, xs[1:]):
        o.append(R(a, y0, b - a, y1 - y0, fl, st, 2, 1.5)); o.append(T((a + b) / 2, (y0 + y1) / 2 + 5, nm, 14, bold=True))
    o.append(L(700, 80, 684, 80, NX, 3, arrow='x')); o.append(T(704, 44, 'light', 13, 'end', NX))
    ez = 190
    o.append(L(40, ez, 680, ez, L2, 1.5))
    o.append(P([(40, ez), (96, ez), (96, 126), (196, 160), (600, 176), (640, ez), (680, ez)], AC, 3))
    o.append(T(104, 126, 'high field: impact ionisation, gain M', 13, 'start', AC))
    o.append(T(400, 146, 'moderate field: photons absorbed, one pair each', 13, 'middle', MUT))
    o.append(T(40, 210, 'field E(x) across the stack', 13, 'start', MUT))
    # bottom: SNR(dB) against M, eta = 0.8, 1.3 um, 100 nW, B = 1 GHz, RL = 1 kOhm, k = 0.3
    Ip = 0.8 * 1.3 / 1.24 * 100e-9; B = 1e9; th = 4 * kB * T300 * B / 1000.0
    snr = lambda M: 10 * math.log10((M * Ip) ** 2 / (2 * q * Ip * M * M * (0.3 * M + 0.7 * (2 - 1 / M)) * B + th))
    X0, X1, Y0, Y1 = 90, 680, 262, 500
    fx = lambda m: X0 + math.log10(m) / math.log10(200) * (X1 - X0)
    fy = lambda d: Y1 - (d + 5) / 25 * (Y1 - Y0)
    o.append(axes(X0, X1, Y0, Y1, [1, 2, 5, 10, 20, 50, 100, 200], [-5, 0, 5, 10, 15, 20], fx, fy,
                  'avalanche gain M (log scale)', 'SNR (dB)', str, neg))
    o.append(P([(fx(math.exp(math.log(200) * i / 200)), fy(snr(math.exp(math.log(200) * i / 200)))) for i in range(201)], AC, 3))
    for m, lab, anc, dx, dy in ((1, 'PIN, M = 1: −3.7 dB', 'start', 10, 6), (10, 'M = 10: 14.0 dB', 'end', -10, 6), (16, 'best M ≈ 16: 14.9 dB', 'start', 6, -14)):
        o.append(C(fx(m), fy(snr(m)), 6, LV if m == 16 else AC))
        o.append(Tb(fx(m) + dx, fy(snr(m)) + dy, lab, 13, anc))
    o.append(T(fx(60), fy(snr(60)) - 18, 'excess noise wins: SNR falls', 13, 'start', MUT))
    return 552, ''.join(o)


FIG[3] = (f3, 'Top: a reach-through APD. Light is absorbed in the wide π layer, and electrons drift into the thin high-field p layer, where impact ionisation multiplies them. '
              'Bottom: SNR of the worked example against gain. It rises from −3.7 dB at M = 1 to 14.0 dB at M = 10 and peaks near M = 16, after which excess noise wins.',
          'Top: layers n plus, p gain region, wide pi absorption region, p plus, with the field highest in the p layer. Bottom: SNR in decibels against gain M on a log scale '
          'from 1 to 200, rising from minus 3.7 dB at M equals 1 to 14.0 dB at M equals 10, peaking at 14.9 dB near M equals 16 and falling at higher gain.')


# ---- 4.4 SNR against received power for the worked example, with its two limits ----
def f4():
    o = []
    R_, Id, B, RL = 0.8, 1e-9, 1e8, 1000.0
    th = 4 * kB * T300 * B / RL
    tot = lambda d: (lambda I: 10 * math.log10(I * I / (2 * q * (I + Id) * B + th)))(R_ * 1e-3 * 10 ** (d / 10))
    thl = lambda d: (lambda I: 10 * math.log10(I * I / th))(R_ * 1e-3 * 10 ** (d / 10))
    shl = lambda d: (lambda I: 10 * math.log10(I / (2 * q * B)))(R_ * 1e-3 * 10 ** (d / 10))
    x0, x1, y0, y1 = 80, 690, 40, 330
    fx = lambda d: x0 + (d + 50) / 50 * (x1 - x0)
    fy = lambda s: y1 - (s + 20) / 100 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [-50, -40, -30, -20, -10, 0], [-20, 0, 20, 40, 60, 80], fx, fy,
                  'received power P (dBm)', 'SNR (dB)', neg, neg))
    o.append(curve(thl, -24, -5, fx, fy, 2, LV, 2, '7 5'))
    o.append(curve(shl, -36, 0, fx, fy, 2, NX, 2, '7 5'))
    o.append(curve(tot, -50, 0, fx, fy, 200, AC, 3.2))
    o.append(Tb(fx(-38), fy(thl(-38)) + 34, 'here SNR follows the thermal limit: +20 dB per 10 dB', 13, 'start', LV))
    o.append(Tb(fx(-6), fy(thl(-5)) - 2, 'thermal limit alone', 13, 'end', LV))
    o.append(Tb(fx(-29), fy(shl(-29)) + 24, 'shot limit: +10 dB per 10 dB', 13, 'start', NX))
    xc = 10 * math.log10(2 * kB * T300 / (q * RL) / R_ / 1e-3)
    o.append(L(fx(xc), fy(tot(xc)) + 8, fx(xc), y1, L2, 1.2, '3 3'))
    o.append(Tb(fx(xc) - 4, y1 - 12, f'equal at {neg(round(xc, 1))} dBm', 13, 'end', MUT))
    o.append(L(fx(-30), y1, fx(-30), fy(25.8), L2, 1.2, '3 3'))
    o.append(C(fx(-30), fy(25.8), 6, AC))
    o.append(Tb(fx(-30) - 10, fy(25.8) - 14, '1 µW (−30 dBm): 25.8 dB', 13, 'end'))
    return 380, ''.join(o)


FIG[4] = (f4, 'SNR of the worked example\'s PIN receiver (R = 0.8 A/W, B = 100 MHz, R<sub>L</sub> = 1 kΩ) as the power changes. At 1 µW it is 25.8 dB and follows the thermal limit; '
              'the shot limit takes over only above about −12 dBm, where the two noise powers are equal.',
          'SNR in decibels against received power from minus 50 to 0 dBm. The solid curve follows a dashed thermal-limit line of slope 20 dB per 10 dB at low power and bends '
          'towards a dashed shot-limit line of slope 10 dB per 10 dB near minus 12 dBm. A point marks 25.8 dB at minus 30 dBm.')


# ---- 4.5 the receiver chain with the worked example's numbers ----
def f5():
    o = []
    bw, bh = 150, 70
    r1 = [(20, 'Photodiode', 'PIN, R = 0.9 A/W'), (205, 'Preamplifier', 'TIA, σ = 40 nA'), (390, 'Main amp', '+ equaliser')]
    for x, a, b in r1:
        o.append(boxt(x, 70, bw, bh, [a, b], PANEL, AC, 14, True))
    o.append(L(170, 105, 203, 105, AC, 2.5, arrow='n')); o.append(L(355, 105, 388, 105, AC, 2.5, arrow='n'))
    o.append(boxt(570, 70, 130, bh, ['AGC', 'holds level'], PANEL, L2, 14, True))
    o.append(L(540, 105, 568, 105, L2, 2, arrow='m'))
    o.append(P([(635, 70), (635, 52), (465, 52), (465, 68)], L2, 2)); o.append(T(550, 44, 'gain set', 13, fill=MUT))
    o.append(T(95, 40, 'light in: 267 nW (−35.7 dBm)', 13, 'middle', NX, True))
    o.append(L(95, 46, 95, 68, NX, 2.5, arrow='x'))
    # second row
    o.append(P([(465, 140), (465, 172), (95, 172), (95, 198)], AC, 2.5)); o.append(f'<path d="M95,190 L95,198" style="stroke:{AC};stroke-width:2.5" marker-end="url(#ar-UID-n)"/>')
    o.append(boxt(20, 200, bw, bh, ['Low-pass filter', '≈ 0.5–0.7 × bit rate'], PANEL, AC, 14, True))
    o.append(boxt(250, 200, 180, bh, ['Decision circuit', 'threshold 240 nA'], ACS, AC, 14, True))
    o.append(L(170, 235, 248, 235, AC, 2.5, arrow='n'))
    o.append(L(430, 235, 520, 235, AC, 2.5, arrow='n')); o.append(T(530, 240, 'bits: 1 0 1 1 0', 14, 'start', INK, True))
    o.append(boxt(250, 300, 180, 56, ['Clock recovery'], PANEL, LV, 14, True))
    o.append(L(340, 300, 340, 272, LV, 2.5, arrow='l')); o.append(T(350, 290, 'sample once per bit', 13, 'start', LV))
    o.append(P([(95, 270), (95, 328), (248, 328)], LV, 2, '5 4')); o.append(f'<path d="M240,328 L248,328" style="stroke:{LV};stroke-width:2" marker-end="url(#ar-UID-l)"/>')
    o.append(T(20, 348, 'one level 480 nA, zero level 0', 13, 'start', MUT))
    return 372, ''.join(o)


FIG[5] = (f5, 'The receiver chain with the worked example\'s numbers: 267 nW gives an average current of 240 nA, so the one level is 480 nA and the threshold sits at 240 nA, '
              'six noise widths (6 × 40 nA) from each level. The recovered clock tells the decision circuit when to sample.',
          'Block diagram: light of 267 nanowatts enters a PIN photodiode with responsivity 0.9 A per W, then a transimpedance preamplifier with 40 nA noise, a main amplifier '
          'and equaliser with an automatic gain control loop, a low-pass filter of about half the bit rate, and a decision circuit with a 240 nA threshold fed by clock recovery, giving bits out.')


# ---- 4.6 the two noisy levels with the best and the halfway threshold, and BER against Q ----
def f6():
    o = []
    x0, x1, y0, y1 = 70, 690, 52, 250
    fx = lambda i: x0 + (i + 0.1) / 1.4 * (x1 - x0)
    g = lambda i, m, s: math.exp(-0.5 * ((i - m) / s) ** 2) / s
    fy = lambda v: y1 - v / 20.0 * (y1 - y0)
    o.append(xaxis(x0, x1, y1, [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2], fx, 'sampled current (µA)', lambda v: f'{v:.1f}'))
    o.append(curve(lambda i: g(i, 0.1, 0.05), -0.1, 0.45, fx, fy, 160, LV, 3))
    o.append(curve(lambda i: g(i, 1.0, 0.10), 0.5, 1.3, fx, fy, 160, AC, 3))
    o.append(T(fx(0.1), fy(20) - 8, '0 bit: I₀ = 0.10, σ₀ = 0.05', 13, 'middle', LV, True))
    o.append(T(fx(1.0), fy(10) - 10, '1 bit: I₁ = 1.0, σ₁ = 0.10', 13, 'middle', AC, True))
    o.append(L(fx(0.40), y0 + 30, fx(0.40), y1, INK, 2.5))
    o.append(L(fx(0.55), y0 + 64, fx(0.55), y1, MUT, 2, '6 4'))
    o.append(Tb(fx(0.40) + 4, y0 + 20, SUB('best I', 'D', ' = 0.40: Q = 6, BER 9.9 × 10⁻¹⁰'), 13, 'start'))
    o.append(Tb(fx(0.55) + 4, y0 + 56, 'halfway 0.55: BER 1.7 × 10⁻⁶', 13, 'start', MUT))
    # bottom: BER against Q, exact
    X0, X1, Y0, Y1 = 90, 690, 330, 560
    fX = lambda Q: X0 + (Q - 2) / 6 * (X1 - X0)
    fY = lambda e: Y0 + (-1 - e) / 15 * (Y1 - Y0)  # e = log10 BER from -1 to -16
    o.append(L(X0, Y1, X1, Y1, L2, 1.5)); o.append(L(X0, Y0, X0, Y1, L2, 1.5))
    for Q in range(2, 9):
        o.append(L(fX(Q), Y1, fX(Q), Y1 + 5, L2, 1.5)); o.append(T(fX(Q), Y1 + 20, str(Q), 13, fill=MUT))
    for e in (-1, -4, -7, -10, -13, -16):
        o.append(L(X0 - 5, fY(e), X0, fY(e), L2, 1.5)); o.append(L(X0, fY(e), X1, fY(e), LN, 1))
        o.append(T(X0 - 9, fY(e) + 4, '10' + f'<tspan dy="-6" font-size="11">{neg(e)}</tspan>', 13, 'end', MUT))
    o.append(T((X0 + X1) / 2, Y1 + 40, 'Q factor', 14, fill=MUT)); o.append(T(X0, Y0 - 12, 'BER = ½ erfc(Q/√2)', 14, 'start', MUT))
    ber = lambda Q: 0.5 * math.erfc(Q / math.sqrt(2))
    o.append(curve(lambda Q: math.log10(ber(Q)), 2, 8, fX, fY, 120, AC, 3))
    for Q, lab, dy in ((6.0, 'Q = 6: 9.9 × 10⁻¹⁰', -14), (7.03, 'Q = 7.03: 10⁻¹²', -14)):
        o.append(L(fX(Q), Y1, fX(Q), fY(math.log10(ber(Q))), L2, 1.2, '3 3'))
        o.append(C(fX(Q), fY(math.log10(ber(Q))), 6, LV))
        o.append(Tb(fX(Q) + 10, fY(math.log10(ber(Q))) + dy, lab, 13, 'start'))
    return 612, ''.join(o)


FIG[6] = (f6, 'Top: case (b) of the worked example. The 1 level is twice as noisy as the 0 level, so the best threshold, 0.40 µA, sits six noise widths from each level; '
              'leaving it halfway at 0.55 µA raises the BER from 9.9 × 10⁻¹⁰ to 1.7 × 10⁻⁶. Bottom: BER against Q; Q = 6 gives about 10⁻⁹ and Q = 7.03 gives 10⁻¹².',
          'Top: two bell curves of sampled current, a narrow one at 0.10 microamperes and a wider one at 1.0 microamperes, with a solid threshold at 0.40 and a dashed one at 0.55. '
          'Bottom: bit error rate on a log scale from 10 to the minus 1 to 10 to the minus 16 against Q from 2 to 8, falling steeply, with points at Q equals 6 and Q equals 7.03.')


spec = make_spec(FIG)
