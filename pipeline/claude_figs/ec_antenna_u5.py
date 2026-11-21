"""Claude's hand-drawn figures for ec-antenna-u5 (RF circuits and transceivers), one per chapter.
Every number comes from that chapter's worked example and is computed here. Colours are the shell's CSS variables."""
import os, sys, math, cmath
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
db = lambda x: 10 * math.log10(x)
sub = lambda s: f'<tspan font-size="11" dy="4">{s}</tspan><tspan dy="-4">​</tspan>'


def arrow(x1, y1, x2, y2, c=AC, w=2, a='n', dash=None):
    return L(x1, y1, x2, y2, c, w, dash, a)


def path(pts, c=AC, w=2.5, dash=None):
    return P(pts, c, w, dash)


# ---- 5.1 the 2 nH spiral: equivalent circuit and Q against frequency ----
def f1():
    o = []
    # circuit (left): Rs and L in series, Cp across both
    o.append(T(120, 28, 'Spiral model', 15, bold=True))
    y = 90
    o.append(L(30, y, 60, y, INK, 2))
    o.append(R(60, y - 12, 50, 24, PANEL, INK, 3))
    o.append(T(85, y + 5, 'R' + sub('s'), 14))
    o.append(L(110, y, 125, y, INK, 2))
    for i in range(4):
        o.append(f'<path d="M{125 + i * 14},{y} a7,7 0 0 1 14,0" style="fill:none;stroke:{INK};stroke-width:2"/>')
    o.append(L(181, y, 210, y, INK, 2))
    o.append(T(85, y - 22, '4 Ω', 13, fill=MUT)); o.append(T(153, y - 22, 'L = 2 nH', 13, fill=MUT))
    o.append(P([(30, y), (30, y + 60), (110, y + 60)], INK, 2)); o.append(P([(130, y + 60), (210, y + 60), (210, y)], INK, 2))
    o.append(L(110, y + 46, 110, y + 74, INK, 3)); o.append(L(130, y + 46, 130, y + 74, INK, 3))
    o.append(T(120, y + 96, 'C' + sub('p') + ' = 1 pF', 13, fill=MUT))
    o.append(C(30, y, 4, INK)); o.append(C(210, y, 4, INK))
    o.append(T(120, 240, 'f' + sub('SR') + ' = 3.56 GHz', 14, bold=True, fill=NX))
    o.append(T(120, 262, 'at 2 GHz: Z = 8.50 + j36.1 Ω', 13, fill=MUT))
    o.append(T(120, 282, 'L looks like 2.87 nH', 13, fill=MUT))
    # plot (right)
    x0, x1, y0, y1 = 300, 690, 40, 300
    fx = lambda f: x0 + (f - 0) / 4.0 * (x1 - x0)
    fy = lambda q: y1 - q / 12 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 1, 2, 3, 4], [0, 4, 8, 12], fx, fy, 'frequency (GHz)', 'Q'))
    Lh, Rs, Cp = 2e-9, 4, 1e-12
    ser, eff = [], []
    for i in range(1, 161):
        f = i * 0.0225
        w = 2 * math.pi * f * 1e9
        ser.append((fx(f), fy(min(w * Lh / Rs, 12))))
        Z = 1 / (1 / (Rs + 1j * w * Lh) + 1j * w * Cp)
        q = Z.imag / Z.real
        if q >= 0: eff.append((fx(f), fy(q)))
    o.append(path([p for p in ser if p[1] >= y0], L2, 2.5, '7 5'))
    o.append(path(eff, AC, 3))
    o.append(T(fx(3.15), fy(10.6), 'ωL/R' + sub('s'), 14, 'start', fill=MUT))
    o.append(T(fx(0.75), fy(5.4), 'Q' + sub('eff') + ' with C' + sub('p'), 14, 'start', fill=AC, bold=True))
    o.append(L(fx(3.5588), y0 + 10, fx(3.5588), y1, NX, 2, '5 4'))
    o.append(Tb(fx(3.56), y0 + 6, 'f' + sub('SR'), 13, fill=NX))
    o.append(L(fx(2), fy(6.28), fx(2), y1, L2, 1.5, '3 3'))
    o.append(C(fx(2), fy(6.28), 5, L2, PANEL)); o.append(C(fx(2), fy(4.25), 5, AC))
    o.append(T(fx(2) + 10, fy(6.28) - 6, '6.28', 13, 'start', fill=MUT))
    o.append(T(fx(2) + 10, fy(4.25) + 18, '4.25', 14, 'start', fill=AC, bold=True))
    return 350, ''.join(o)

FIG[1] = (f1, 'The worked example\'s 2 nH spiral: its 1 pF shunt capacitance resonates at 3.56 GHz, so the real Q (solid) peaks near 2 GHz at 4.25 and falls to zero at self-resonance, while the simple ωL/R<sub>s</sub> (dashed) keeps rising to 6.28 and beyond.',
          'Left, the inductor model: a 4 ohm resistor in series with 2 nanohenries, with 1 picofarad across both. Right, Q against frequency from 0 to 4 gigahertz. The dashed straight line omega L over Rs reaches 6.28 at 2 gigahertz. The solid curve including Cp peaks at 4.25 near 2 gigahertz and falls to zero at the self-resonant frequency of 3.56 gigahertz.')


# ---- 5.2 Friis: the three-stage chain and each stage's share of F ----
def f2():
    o = []
    st = [('LNA', 'G 15 dB', 'NF 2 dB'), ('Mixer', 'G 10 dB', 'NF 12 dB'), ('IF amp', 'G 20 dB', 'NF 10 dB')]
    xs = [120, 330, 540]
    o.append(boxt(16, 46, 70, 56, ['Source', '290 K'], PANEL, L2, 13))
    for i, (a, b, c) in enumerate(st):
        o.append(boxt(xs[i], 34, 130, 80, [a, b, c], ACS if i == 0 else PANEL, AC, 14, bold_first=True))
        o.append(arrow((86 if i == 0 else xs[i - 1] + 130), 74, xs[i] - 4, 74))
    o.append(T(360, 152, 'Each stage\'s contribution to the noise factor F', 15, bold=True))
    bars = [('LNA: F₁', 1.585, AC), ('Mixer: (F₂ − 1)/G₁ = 14.85/31.62', 0.470, LV), ('IF amp: (F₃ − 1)/(G₁G₂) = 9/316.2', 0.0285, NX)]
    bx, sc = 40, 330
    yb = 176
    for j, (lab, v, c) in enumerate(bars):
        y = yb + j * 52
        o.append(T(bx, y + 14, lab, 14, 'start'))
        o.append(R(bx, y + 22, max(v * sc, 3), 20, c, c, 3, 1))
        o.append(T(bx + max(v * sc, 3) + 10, y + 38, {1.585: '1.585', 0.470: '0.470', 0.0285: '0.0285'}[v], 14, 'start', bold=True))
    o.append(L(bx, yb + 166, bx + 2.083 * sc, yb + 166, INK, 1.5))
    o.append(T(bx, yb + 190, 'Sum F = 2.083, so NF = 10 log₁₀ 2.083 = 3.19 dB', 15, 'start', fill=AC, bold=True))
    o.append(T(bx, yb + 212, 'Noise floor in 10 MHz: −174 + 70 + 3.19 = −100.8 dBm', 14, 'start', fill=MUT))
    return 410, ''.join(o)

FIG[2] = (f2, 'The worked example\'s chain. The LNA\'s 15 dB gain divides the mixer\'s large noise (F₂ = 15.85) by 31.6 before it is added, so the LNA itself supplies 76 % of the total F = 2.083 (3.19 dB).',
          'Three blocks in a row: LNA with gain 15 dB and noise figure 2 dB, mixer with gain 10 dB and noise figure 12 dB, IF amplifier with gain 20 dB and noise figure 10 dB. Below, bars show each stage\'s share of the noise factor: 1.585 for the LNA, 0.470 for the mixer and 0.0285 for the IF amplifier, summing to 2.083, which is 3.19 dB.')


# ---- 5.3 Pout against Pin: fundamental, IM3, compression and the intercept ----
def f3():
    x0, x1, y0, y1 = 90, 560, 30, 360
    fx = lambda p: x0 + (p + 25) / 40 * (x1 - x0)
    fy = lambda p: y1 - (p + 60) / 95 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [-25, -20, -10, 0, 10, 15], [-60, -40, -20, 0, 20], fx, fy, 'input power per tone (dBm)', 'output (dBm)', xfmt=neg, yfmt=neg)]
    G = 20
    Psat = 21.1646
    def rapp(pin):
        vin = math.sqrt(10 ** ((pin + G) / 10)); vs = math.sqrt(10 ** (Psat / 10))
        return db((vin / (1 + (vin / vs) ** 4) ** 0.25) ** 2)
    o.append(path([(fx(-25), fy(-5)), (fx(10), fy(30))], L2, 2, '7 5'))
    o.append(path([(fx(-20), fy(-60)), (fx(10), fy(30))], L2, 2, '7 5'))
    o.append(path([(fx(p / 4), fy(rapp(p / 4))) for p in range(-100, 61)], AC, 3))
    o.append(path([(fx(p / 4), fy(3 * p / 4)) for p in range(-80, -15)], NX, 3))
    o.append(C(fx(10), fy(30), 6, INK))
    o.append(Tb(fx(10) - 10, fy(30) - 12, 'IIP3 = 10 dBm, OIP3 = 30 dBm', 13, 'end', bold=True))
    o.append(C(fx(0), fy(19), 6, LV))
    o.append(L(fx(0), fy(19), fx(0), fy(20), LV, 2))
    o.append(T(fx(0) + 12, fy(19) + 22, 'P1dB: 0 dBm in, 19 dBm out', 13, 'start', fill=LV, bold=True))
    o.append(C(fx(-10), fy(10), 5, AC)); o.append(C(fx(-10), fy(-30), 5, NX))
    o.append(L(fx(-10), fy(10), fx(-10), fy(-30), INK, 1.5, '3 3'))
    o.append(Tb(fx(-10) - 8, fy(-10) + 4, '40 dB = −40 dBc', 13, 'end'))
    o.append(T(fx(-10) + 10, fy(10) + 18, '10 dBm', 13, 'start', fill=AC))
    o.append(T(fx(-10) + 10, fy(-30) + 5, '−30 dBm', 13, 'start', fill=NX))
    o.append(T(fx(-21), fy(-12), 'wanted tone, slope 1', 13, 'start', fill=AC, bold=True))
    o.append(T(fx(-15) + 6, fy(-45), 'IM3, slope 3', 13, 'start', fill=NX, bold=True))
    o.append(T(600, fy(21.2) + 4, 'saturates', 13, 'start', fill=MUT))
    o.append(T(600, fy(21.2) + 22, 'near 21 dBm', 13, 'start', fill=MUT))
    return 410, ''.join(o)

FIG[3] = (f3, 'The worked example\'s amplifier (G = 20 dB). At −10 dBm per tone the wanted output is 10 dBm and IM3 is −30 dBm, 40 dB lower; the slope-1 and slope-3 lines meet at IIP3 = 10 dBm, OIP3 = 30 dBm, far above the 1 dB compression point at 0 dBm in, 19 dBm out.',
          'Output power against input power per tone. The wanted output follows a slope-one line and bends over towards saturation near 21 dBm, crossing 19 dBm at 0 dBm input, the 1 dB compression point. The IM3 output follows a slope-three line. At minus 10 dBm input the wanted output is 10 dBm and IM3 is minus 30 dBm, a gap of 40 dB. Extended dashed lines meet at 10 dBm input and 30 dBm output, the intercept point.')


# ---- 5.4 the superheterodyne frequency plan with the preselector's response ----
def f4():
    x0, x1, y0, y1 = 80, 690, 60, 300
    fx = lambda f: x0 + (f - 840) / 200 * (x1 - x0)
    fy = lambda a: y0 + (-a) / 30 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [850, 900, 945, 990, 1040], [0, -10, -20, -30], fx, fy, 'frequency (MHz)', 'response (dB)', yfmt=neg)]
    resp = lambda f: -20 * math.log10(math.sqrt(1 + (50 * (f / 900 - 900 / f)) ** 2))
    o.append(path([(fx(f), fy(max(resp(f), -30))) for f in range(840, 1041, 2)], AC, 3))
    # markers
    o.append(L(fx(900), fy(0), fx(900), y1, AC, 2.5))
    o.append(T(fx(900) + 12, fy(-2.5), 'wanted 900', 13, 'start', bold=True, fill=AC))
    o.append(L(fx(945), y0 - 10, fx(945), y1, L2, 2, '6 4'))
    o.append(Tb(fx(945), y0 - 18, 'LO 945', 13, fill=MUT))
    a = resp(990)
    o.append(L(fx(990), fy(a), fx(990), y1, NX, 2.5))
    o.append(C(fx(990), fy(a), 6, NX))
    o.append(T(fx(996), fy(-25.5), 'image 990', 13, 'start', fill=NX, bold=True))
    o.append(T(fx(996), fy(-28), f'{a:.1f} dB'.replace('-', '−'), 13, 'start', fill=NX, bold=True))
    o.append(brace(fx(900), fx(945), y1 - 26, INK, up=False))
    o.append(T((fx(900) + fx(945)) / 2, y1 - 34, '45', 13, bold=True))
    o.append(brace(fx(945), fx(990), y1 - 26, INK, up=False))
    o.append(T((fx(945) + fx(990)) / 2, y1 - 34, '45', 13, bold=True))
    o.append(T(fx(952), fy(-4), 'one tuned circuit, Q = 50', 13, 'start', fill=MUT))
    o.append(T(fx(952), fy(-7), 'α = √(1 + (Qρ)²) = 9.60', 13, 'start', fill=MUT))
    return 350, ''.join(o)

FIG[4] = (f4, 'The worked example\'s frequency plan: a 945 MHz high-side LO puts the IF at 45 MHz and the image 2 × 45 = 90 MHz above the 900 MHz signal. A single Q = 50 preselector is only 19.6 dB down at 990 MHz, which is why more image filtering is needed.',
          'Response of a single tuned circuit with Q of 50 centred on 900 megahertz, from 840 to 1040 megahertz. The wanted signal at 900 is at 0 dB. The LO at 945 is marked by a dashed line, 45 megahertz above the signal. The image at 990, another 45 megahertz above the LO, is only 19.6 dB down.')


# ---- 5.5 direct-conversion transmitter with the worked example's levels ----
def f5():
    o = []
    # I and Q DAC + filters
    for j, (lab, y) in enumerate([('I', 40), ('Q', 112)]):
        o.append(boxt(14, y, 62, 40, ['DAC ' + lab], PANEL, AC, 13))
        o.append(arrow(76, y + 20, 92, y + 20))
        o.append(boxt(94, y, 60, 40, ['LPF'], PANEL, AC, 13))
        o.append(arrow(154, y + 20, 186, y + 20 + (36 - 20) * (1 if j == 0 else -1) * 0.0))
    # modulator
    o.append(R(188, 40, 92, 112, ACS, AC, 8))
    o.append(T(234, 82, 'I/Q', 14, bold=True)); o.append(T(234, 100, 'modulator', 13)); o.append(T(234, 120, '−5 dBm', 13, fill=AC, bold=True))
    o.append(boxt(188, 190, 92, 44, ['LO + 90°'], PANEL, L2, 13))
    o.append(arrow(234, 190, 234, 156, L2, 2, 'm'))
    chain = [('Driver', '+10 dB', '5 dBm'), ('PA', '+20 dB', '25 dBm'), ('Harmonic', 'LPF 0.5 dB', '24.5 dBm'), ('Duplexer', '1.5 dB', '23 dBm')]
    xs = [302, 398, 494, 590]
    prev = 280
    for i, (a, b, c) in enumerate(chain):
        o.append(arrow(prev, 96, xs[i] - 4, 96))
        o.append(boxt(xs[i], 66, 86, 60, [a, b], ACS if a == 'PA' else PANEL, AC, 13, bold_first=True))
        o.append(T(xs[i] + 43, 146, c, 13, fill=AC, bold=True))
        prev = xs[i] + 86
    # antenna
    o.append(L(633, 66, 633, 36, INK, 2)); o.append(P([(618, 20), (633, 36), (648, 20)], INK, 2))
    o.append(T(660, 30, '3 dBi', 13, 'start', fill=MUT))
    o.append(T(500, 196, 'EIRP = 23 + 3 = 26 dBm (0.40 W)', 14, bold=True, fill=AC))
    # receive branch
    o.append(arrow(664, 126, 664, 236, L2, 2, 'm'))
    o.append(boxt(600, 238, 106, 44, ['to LNA'], PANEL, L2, 13))
    o.append(T(560, 304, 'TX carrier at the LNA: 25 − 50 = −25 dBm', 13, fill=MUT))
    o.append(T(560, 324, 'TX noise: −130 − 45 = −175 dBm/Hz', 13, fill=MUT))
    o.append(T(170, 290, 'Peak at the PA = 25 + 8 dB PAPR', 13, fill=MUT))
    o.append(T(170, 310, '= 33 dBm = P1dB,out', 13, fill=NX, bold=True))
    return 345, ''.join(o)

FIG[5] = (f5, 'The worked examples\' transmitter: DACs and reconstruction filters feed the I/Q modulator, then the driver, PA, harmonic filter and duplexer take −5 dBm to 23 dBm at the antenna port and 26 dBm EIRP. The duplexer also lets −25 dBm of carrier and −175 dBm/Hz of transmit noise reach the receiver.',
          'Block diagram of a direct-conversion transmitter. I and Q DACs each feed a low-pass filter, both feed an I/Q modulator driven by an LO with 90 degree phase split, giving minus 5 dBm. A driver of plus 10 dB gives 5 dBm, the PA of plus 20 dB gives 25 dBm, the harmonic filter with 0.5 dB loss gives 24.5 dBm and the duplexer with 1.5 dB loss gives 23 dBm at a 3 dBi antenna, for an EIRP of 26 dBm. A branch from the duplexer to the LNA notes minus 25 dBm of carrier and minus 175 dBm per hertz of transmit noise.')


# ---- 5.6 inductively degenerated cascode LNA with the worked example's values ----
def f6():
    o = []
    gx = 300  # gate x
    # source and Lg
    o.append(C(40, 200, 22, INK, PANEL)); o.append(T(40, 205, '~', 18, bold=True))
    o.append(T(40, 244, '50 Ω source', 13, fill=MUT))
    o.append(L(62, 200, 120, 200, INK, 2))
    for i in range(4):
        o.append(f'<path d="M{120 + i * 16},{200} a8,8 0 0 1 16,0" style="fill:none;stroke:{INK};stroke-width:2"/>')
    o.append(T(152, 180, 'L' + sub('g') + ' = 14.41 nH', 13, bold=True))
    o.append(L(184, 200, gx - 14, 200, INK, 2))
    # M1
    o.append(L(gx - 14, 176, gx - 14, 224, INK, 3))
    o.append(L(gx, 172, gx, 228, INK, 3))
    o.append(L(gx, 180, gx + 30, 180, INK, 2)); o.append(L(gx, 220, gx + 30, 220, INK, 2))
    o.append(L(gx + 30, 180, gx + 30, 150, INK, 2)); o.append(L(gx + 30, 220, gx + 30, 250, INK, 2))
    o.append(T(gx + 42, 205, 'M1', 14, 'start', bold=True))
    o.append(T(gx - 22, 150, 'C' + sub('gs') + ' = 300 fF', 13, 'end', fill=MUT))
    o.append(T(gx - 22, 168, 'g' + sub('m') + ' = 60 mS', 13, 'end', fill=MUT))
    # Ls
    for i in range(3):
        o.append(f'<path d="M{gx + 30},{250 + i * 14} a7,7 0 0 1 0,14" style="fill:none;stroke:{INK};stroke-width:2"/>')
    o.append(L(gx + 30, 292, gx + 30, 312, INK, 2))
    o.append(L(gx + 14, 312, gx + 46, 312, INK, 2)); o.append(L(gx + 20, 318, gx + 40, 318, INK, 2))
    o.append(T(gx + 48, 278, 'L' + sub('s') + ' = 0.25 nH', 13, 'start', bold=True))
    # M2 cascode
    o.append(L(gx + 16, 100, gx + 16, 148, INK, 3))
    o.append(L(gx + 30, 104, gx + 30, 150, INK, 2))
    o.append(L(gx + 2, 124, gx + 16, 124, INK, 2)); o.append(T(gx - 4, 129, 'V' + sub('b'), 13, 'end', fill=MUT))
    o.append(T(gx + 42, 130, 'M2 (cascode)', 14, 'start', bold=True))
    o.append(L(gx + 30, 104, gx + 30, 80, INK, 2))
    # load
    o.append(R(gx + 14, 40, 32, 40, PANEL, AC, 4))
    o.append(T(gx + 54, 64, 'tuned load', 13, 'start', fill=MUT))
    o.append(L(gx + 30, 40, gx + 30, 24, INK, 2)); o.append(T(gx + 30, 18, 'V' + sub('DD'), 13))
    o.append(arrow(gx + 30, 90, gx + 90, 90)); o.append(T(gx + 96, 95, 'to mixer', 13, 'start', fill=MUT))
    # Zin label and equation panel
    o.append(L(220, 214, 220, 232, AC, 2)); o.append(T(220, 250, 'Z' + sub('in'), 14, bold=True, fill=AC))
    o.append(R(470, 160, 236, 150, PANEL, L2, 8))
    rows = ['ω' + sub('T') + ' = g' + sub('m') + '/C' + sub('gs') + ' = 2 × 10¹¹ rad/s', 'Re Z' + sub('in') + ' = ω' + sub('T') + 'L' + sub('s') + ' = 50 Ω',
            'L' + sub('g') + ' + L' + sub('s') + ' = 1/(ω₀²C' + sub('gs') + ') = 14.66 nH', 'Q' + sub('in') + ' = 2.21 at 2.4 GHz', 'return loss 15 dB at ±100 MHz']
    for i, r in enumerate(rows):
        o.append(T(482, 186 + i * 27, r, 13, 'start', fill=AC if i == 1 else INK, bold=(i == 1)))
    return 330, ''.join(o)

FIG[6] = (f6, 'The worked example\'s LNA: a 0.25 nH source inductor makes the 50 Ω input resistance from ω<sub>T</sub>L<sub>s</sub> with no noisy resistor, and 14.41 nH at the gate tunes out C<sub>gs</sub> at 2.4 GHz. The cascode M2 isolates the input from the load.',
          'Circuit of the LNA. A 50 ohm source feeds a 14.41 nanohenry gate inductor into the gate of transistor M1, which has Cgs of 300 femtofarads and gm of 60 millisiemens. M1\'s source goes to ground through a 0.25 nanohenry inductor. Cascode transistor M2 sits above M1 with a tuned load to the supply, and the output goes to the mixer. A panel lists omega T equals 2 times 10 to the 11 radians per second, real part of Zin equals 50 ohms, Lg plus Ls equals 14.66 nanohenries, Qin of 2.21 and return loss of 15 dB at plus and minus 100 megahertz.')


# ---- 5.7 inputs that reach the 100 MHz IF, with f_LO = 2.55 GHz ----
def f7():
    x0, x1, y = 60, 680, 250
    fx = lambda f: x0 + (f - 2.40) / 0.30 * (x1 - x0)
    o = [xaxis(x0, x1, y, [2.40, 2.45, 2.50, 2.55, 2.60, 2.65, 2.70], fx, 'input frequency at the RF port (GHz)', lambda v: f'{v:.2f}')]
    items = [(2.45, 170, AC, 'wanted', '(1, 1)'), (2.50, 120, LV, 'half-IF', '(2, 2)'), (2.5167, 80, MUT, '', '(3, 3)'),
             (2.5833, 80, MUT, '', '(3, 3)'), (2.60, 120, LV, '', '(2, 2)'), (2.65, 150, NX, 'image', '(1, 1)')]
    for f, h, c, lab, mn in items:
        X = fx(f)
        o.append(L(X, y, X, y - h, c, 4))
        o.append(C(X, y - h, 5, c))
        if lab: o.append(T(X, y - h - 30, lab, 13, fill=c, bold=True))
        o.append(T(X, y - h - 12, mn, 13, fill=c))
    X = fx(2.55)
    o.append(L(X, y, X, 46, L2, 2, '6 4'))
    o.append(Tb(X, 40, 'LO 2.55', 13, fill=MUT))
    o.append(T(360, 314, 'Each input gives |m·2.55 − n·f| = 0.10 GHz; (m, n) is shown above it.', 13, fill=MUT))
    o.append(T(360, 334, 'The half-IF spur at 2.50 GHz is only 50 MHz from the wanted 2.45 GHz.', 13, fill=MUT))
    return 345, ''.join(o)

FIG[7] = (f7, 'Worked example 2\'s spur search: besides the wanted 2.45 GHz signal and the 2.65 GHz image, the inputs at 2.50, 2.517, 2.583 and 2.60 GHz also convert to the 100 MHz IF through LO and RF harmonics. Heights only separate the kinds.',
          'A frequency axis from 2.40 to 2.70 gigahertz with the LO at 2.55 dashed. Lines mark the inputs that convert to 100 megahertz: the wanted signal at 2.45 with m and n equal to 1, the half-IF spur at 2.50 with m and n equal to 2, third-order spurs at 2.517 and 2.583, a second-order spur at 2.60 and the image at 2.65.')


# ---- 5.8 drain efficiency against back-off ----
def f8():
    x0, x1, y0, y1 = 80, 560, 40, 320
    fx = lambda b: x0 + b / 12 * (x1 - x0)
    fy = lambda e: y1 - e / 80 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [0, 3, 6, 9, 12], [0, 20, 40, 60, 80], fx, fy, 'back-off from full output (dB)', 'drain efficiency (%)')]
    cb = [(fx(b / 10), fy(78.54 * 10 ** (-b / 200))) for b in range(0, 121)]
    ca = [(fx(b / 10), fy(50 * 10 ** (-b / 100))) for b in range(0, 121)]
    cd = [(fx(b / 10), fy(45.45 * 10 ** (-b / 100))) for b in range(0, 121)]
    o.append(path(cb, LV, 3)); o.append(path(ca, AC, 3)); o.append(path(cd, AC, 2, '6 4'))
    o.append(L(fx(6), y0 + 10, fx(6), y1, L2, 1.5, '3 3'))
    for v, c in ((39.36, LV), (12.56, AC), (11.41, AC)):
        o.append(C(fx(6), fy(v), 5, c))
    o.append(T(fx(6) + 10, fy(39.36) - 8, '39.4 %', 14, 'start', fill=LV, bold=True))
    o.append(T(fx(6) + 10, fy(12.56) - 8, '12.6 %', 14, 'start', fill=AC, bold=True))
    o.append(T(x1 + 10, fy(78.54 * 10 ** (-0.6)) + 4, 'Class B', 14, 'start', fill=LV, bold=True))
    o.append(T(x1 + 10, fy(78.54 * 10 ** (-0.6)) + 22, '78.5 % × 10', 13, 'start', fill=LV))
    o.append(T(x1 + 10, fy(78.54 * 10 ** (-0.6)) + 40, 'to the −BO/20', 13, 'start', fill=LV))
    o.append(T(fx(0.3), fy(50) - 8, 'Class A ideal, 50 %', 13, 'start', fill=AC, bold=True))
    o.append(T(fx(0.3), fy(9), 'dashed: Class A design,', 13, 'start', fill=AC))
    o.append(T(fx(0.3), fy(3), '45.5 % → 11.4 % at 6 dB', 13, 'start', fill=AC))
    return 370, ''.join(o)

FIG[8] = (f8, 'Efficiency falls with back-off at two rates: Class A as the power ratio, Class B as the amplitude ratio. At 6 dB, ideal Class A is down to 12.6 % (the worked example\'s 45.5 % design to 11.4 %), while ideal Class B still gives 39.4 %.',
          'Drain efficiency in percent against back-off from 0 to 12 dB. The Class B curve starts at 78.5 percent and falls to 39.4 percent at 6 dB. The ideal Class A curve starts at 50 percent and falls to 12.6 percent at 6 dB, and a dashed curve for the worked example\'s Class A design starts at 45.5 percent and falls to 11.4 percent.')


# ---- 5.9 phase noise of the free VCO, the multiplied reference and the PLL output ----
def f9():
    x0, x1, y0, y1 = 90, 560, 40, 330
    lx = lambda d: x0 + (math.log10(d) - 3) / 4 * (x1 - x0)
    fy = lambda p: y0 + (-40 - p) / 110 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [], [-40, -60, -80, -100, -120, -140], lx, fy, '', 'phase noise (dBc/Hz)', yfmt=neg)]
    for d, lab in ((1e3, '1 kHz'), (1e4, '10 kHz'), (1e5, '100 kHz'), (1e6, '1 MHz'), (1e7, '10 MHz')):
        o.append(L(lx(d), y1, lx(d), y1 + 5, L2, 1.5)); o.append(T(lx(d), y1 + 20, lab, 13, fill=MUT))
    o.append(T((x0 + x1) / 2, y1 + 40, 'offset from the 2 GHz carrier', 14, fill=MUT))
    k, T0, F, Ps, f0, Q, fc = 1.380649e-23, 290, 2.0, 1e-3, 2e9, 8, 1e5
    vco = lambda d: db(2 * F * k * T0 / Ps * (1 + (f0 / (2 * Q * d)) ** 2) * (1 + fc / d))
    ref = lambda d: (-140 - 15 * math.log10(d / 1e3) if d < 1e4 else -155) + 20 * math.log10(200)
    ds = [10 ** (3 + i / 40) for i in range(0, 161)]
    o.append(path([(lx(d), fy(max(vco(d), -150))) for d in ds if vco(d) <= -40], NX, 2.5, '7 5'))
    o.append(path([(lx(d), fy(ref(d))) for d in ds], LV, 2.5, '7 5'))
    o.append(path([(lx(d), fy(ref(d) if d < 176e3 else vco(d))) for d in ds], AC, 4))
    o.append(L(lx(176e3), y0, lx(176e3), y1, L2, 1.5, '3 3'))
    o.append(Tb(lx(176e3), y0 + 6, 'f' + sub('L') + ' ≈ 180 kHz', 13, fill=MUT))
    o.append(C(lx(1e4), fy(-109.0), 5, AC)); o.append(C(lx(1e6), fy(-125.6), 5, AC))
    o.append(T(lx(1e4), fy(-109.0) + 22, '−109.0', 13, fill=AC, bold=True))
    o.append(T(lx(1e6) + 10, fy(-125.6) - 10, '−125.6', 13, 'start', fill=AC, bold=True))
    o.append(T(lx(1.4e4), fy(-75.6), 'free VCO (Leeson)', 13, 'start', fill=NX, bold=True))
    o.append(T(lx(3e5) + 6, fy(-105), 'reference × 200 (+46 dB)', 13, 'start', fill=LV, bold=True))
    o.append(T(lx(2.5e3), fy(-127), 'PLL output (solid)', 14, 'start', fill=AC, bold=True))
    return 390, ''.join(o)

FIG[9] = (f9, 'The worked examples\' synthesizer: inside the 180 kHz loop the output follows the reference raised by 20 log₁₀200 = 46 dB (−109.0 dBc/Hz at 10 kHz); outside it follows the free VCO (−125.6 dBc/Hz at 1 MHz). The loop bandwidth sits where the two dashed curves cross.',
          'Phase noise in dBc per hertz against offset from 1 kilohertz to 10 megahertz on a log scale. The free VCO curve falls steeply, reaching minus 75.6 at 10 kilohertz and minus 125.6 at 1 megahertz. The multiplied reference is flat at minus 109 beyond 10 kilohertz. They cross near 180 kilohertz, marked as the loop bandwidth. The PLL output, drawn solid, follows the reference below 180 kilohertz and the VCO above.')

spec = make_spec(FIG)
