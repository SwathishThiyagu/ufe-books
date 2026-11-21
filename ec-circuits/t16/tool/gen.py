"""Write the t16 emboss (e2) block for every Circuit Theory lesson (ec-circuits).
Every value is computed here from the lesson's own worked examples (branches lesson/ec-circuits-uN-Lk,
books/ece/ec-circuits on main). The drawing follows the hook in thumbs.json (hooks are final).
Renderer: t16.py with the e2 Stage path added for Automotive Electrical (au-elec/t16/tool/t16.py), unchanged.
Usage: python3 gen.py <thumbs.json in> <thumbs.json out>"""
import json, math, cmath, sys


def C(id, x, y, text, sub=None, r=66, size=None, **kw):
    n = dict(id=id, x=x, y=y, text=text, r=r, **kw)
    if sub: n['sub'] = sub
    if size: n['size'] = size
    return n


def R(id, x, y, w, h, text, size=24, **kw):
    return dict(id=id, x=x, y=y, w=w, h=h, text=text, size=size, **kw)


def K(a, b, label=None, **kw):
    return dict(a=a, b=b, label=label, **kw)


def T(x, y, text, size=22, color='#5B7CFA', **kw):
    return dict(x=x, y=y, text=text, size=size, color=color, **kw)


def tape(cells, head, y=470, cx=360, cw=64):
    w = sum(max(cw, 26 + 17 * len(str(c))) for c in cells) + 12 * (len(cells) - 1)
    return dict(x=round(cx - w / 2), y=y, cells=cells, head=head, cw=cw)


def g(v, d=1):
    """number with d decimals, trailing zeros kept off for whole numbers"""
    s = f'{v:.{d}f}'
    if '.' in s:
        s = s.rstrip('0').rstrip('.')
    return s.replace('-', '−')


def par(*rs):
    return 1 / sum(1 / r for r in rs)


Y = 250
GREY = '#A9B4C6'
BLUE = '#5B7CFA'
OHM = 'Ω'


# ---------------------------------------------------------------- unit 1
def u1L1():          # hook: Can a capacitor's voltage jump?  (worked example 2a: 20 uF fed 10 mA for 20 ms)
    C_, I_, t_ = 20e-6, 10e-3, 20e-3
    v20 = I_ * t_ / C_
    w = 0.5 * C_ * v20 ** 2
    return dict(nodes=[C('a', 110, Y, '0 V', 'at 0⁻', r=70, size=36),
                       C('b', 345, Y, '0 V', 'at 0⁺', r=78, size=38, lit=True),
                       C('c', 590, Y, f'{g(v20)} V', 'at 20 ms', r=78, size=38, ok=True)],
                links=[K('a', 'b', 'no jump'), K('b', 'c', f'{g(I_ * 1000)} mA in')],
                texts=[T(360, 432, f'20 μF: i leaps 0 → {g(I_ * 1000)} mA, v climbs to {g(v20)} V ({g(w * 1000)} mJ)', 21, BLUE)],
                tapes=[tape(['0 mA', f'{g(I_ * 1000)} mA', f'{g(I_ * 1000)} mA', '0 mA'], 1, y=462)],
                caption='capacitor voltage cannot jump; <b>its current can</b>')


def u1L2():          # hook: Is the outer loop a mesh?  (the bridge: n = 4, b = 6)
    n, b = 4, 6
    m = b - n + 1
    return dict(nodes=[C('A', 420, 80, 'A', None, r=44, size=30),
                       C('B', 250, 255, 'B', None, r=44, size=30),
                       C('C', 590, 255, 'C', None, r=44, size=30),
                       C('D', 420, 430, 'D', None, r=44, size=30)],
                links=[K('A', 'B', '20 Ω', arrow=False, size=22, lx=-36, ly=-8),
                       K('A', 'C', '20 Ω', arrow=False, size=22, lit=True, lx=36, ly=-8),
                       K('B', 'C', '10 Ω', arrow=False, size=22, ly=-22),
                       K('B', 'D', '2 Ω', arrow=False, size=22, lx=-36, ly=8),
                       K('C', 'D', '8 Ω', arrow=False, size=22, lit=True, lx=36, ly=8),
                       K('D', 'A', '36 V', arrow=False, bend=-310, lit=True, size=22, lx=-44, ly=-4)],
                texts=[T(420, 190, 'M2', 22, GREY), T(420, 332, 'M3', 22, GREY), T(168, 262, 'M1', 22, GREY)],
                tapes=[tape([f'n {n}', f'b {b}', f'm {m}', 'loops 7'], 2, y=520)],
                caption='the outer boundary is a loop, <b>not a mesh</b>')


def u1L3():          # hook: Current divider: which R on top?  (worked example 1: 1.2 A into 12 ohm || 6 ohm)
    I, R1, R2 = 1.2, 12, 6
    I1, I2 = I * R2 / (R1 + R2), I * R1 / (R1 + R2)
    return dict(nodes=[C('s', 120, 300, f'{g(I)} A', 'in', r=74, size=38),
                       C('a', 570, 150, f'{g(I1)} A', f'{R1} Ω', r=80, size=38, subsize=20, lit=True),
                       C('b', 570, 450, f'{g(I2)} A', f'{R2} Ω', r=80, size=38, subsize=20)],
                links=[K('s', 'a', f'× {R2}/{R1 + R2}', size=24, lx=-20, ly=-18), K('s', 'b', f'× {R1}/{R1 + R2}', size=24, lx=-20, ly=26)],
                texts=[T(330, 300, f'{R1} Ω ∥ {R2} Ω', 22, GREY)],
                tapes=[], caption=f'put <b>the other R</b> on top: the larger R gets less current')


def u1L4():          # hook: How many twigs and links?  (the bridge graph: n = 4, b = 6, tree 4, 5, 6)
    n, b = 4, 6
    tw, li = n - 1, b - n + 1
    return dict(nodes=[C('n', 130, 160, f'n = {n}', 'nodes', r=70, size=30),
                       C('b', 130, 420, f'b = {b}', 'branches', r=70, size=30),
                       C('t', 580, 160, f'{tw}', 'twigs', r=76, size=44, lit=True),
                       C('l', 580, 420, f'{li}', 'links', r=76, size=44, ok=True)],
                links=[K('n', 't', 'n − 1', size=24), K('b', 'l', 'b − n + 1', size=24)],
                texts=[T(360, 555, 'the bridge: tree 4, 5, 6 and chords 1, 2, 3', 22, GREY)],
                tapes=[], caption=f'twigs = n − 1 = {tw}, <b>not n</b>')


# ---------------------------------------------------------------- unit 2
def u2L1():          # hook: When is it a supernode?  (nodal example 2)
    # supernode {2, 3}: (v2 - 12)/2 + v2/3 + v3/4 = 2, v3 = v2 + 6
    v1 = 12
    v2 = (2 + 12 / 2 - 6 / 4) / (1 / 2 + 1 / 3 + 1 / 4)
    v3 = v2 + 6
    i6 = v3 / 4 - 2
    return dict(nodes=[C('1', 110, 200, '1', f'{g(v1)} V', r=60, size=34, subsize=20),
                       C('2', 380, 200, '2', f'{g(v2)} V', r=60, size=34, subsize=20, lit=True),
                       C('3', 600, 200, '3', f'{g(v3)} V', r=60, size=34, subsize=20, lit=True),
                       C('0', 360, 450, '0 V', 'reference', r=62, size=30, subsize=16)],
                links=[K('1', '2', '2 Ω', arrow=False, size=22),
                       K('2', '3', '6 V', arrow=False, lit=True, size=24, ly=40),
                       K('0', '1', '12 V', arrow=False, size=22, lx=-30, ly=10),
                       K('2', '0', '3 Ω', arrow=False, size=22, lx=-6),
                       K('3', '0', '4 Ω', arrow=False, size=22, lx=16, ly=10)],
                svg=['<rect x="300" y="122" width="384" height="156" rx="40" fill="none" stroke="#2FB380" stroke-width="4" stroke-dasharray="12 8"/>'],
                texts=[T(492, 108, 'supernode', 24, '#2FB380'),
                       T(360, 575, f'12 V to the reference only fixes v₁; {g(i6)} A flows through the 6 V', 20, GREY)],
                tapes=[], caption='a source between two non-reference nodes: <b>supernode</b>')


def u2L2():          # hook: Rth with a dependent source?  (worked example 4)
    Voc, Isc_r, Isc_c = 9, 2, 1
    Isc = Isc_r + Isc_c
    Rth = Voc / Isc
    Rwrong = par(6, 12)
    return dict(nodes=[C('v', 120, 170, f'{Voc} V', 'open: Voc', r=70, size=36),
                       C('i', 120, 430, f'{Isc} A', 'short: Isc', r=70, size=36),
                       C('r', 560, 300, f'{g(Rth)} Ω', 'Rth = Voc ÷ Isc', r=90, size=44, subsize=17, lit=True)],
                links=[K('v', 'r', ''), K('i', 'r', '')],
                boxes=[dict(x=420, y=545, w=360, h=56, text=f'switched off: 6 ∥ 12 = {g(Rwrong)} Ω', size=22, inset=True)],
                texts=[T(330, 300, f'{Voc} V ÷ {Isc} A', 24, BLUE), T(120, 540, f'= {Isc_r} + {Isc_c} A', 22, GREY)],
                tapes=[], caption=f'keep the controlled source on: <b>Rth = {g(Rth)} Ω</b>')


def u2L3():          # hook: What is the maximum power, really?  (Vth = 24 V, Rth = 4 ohm)
    Vth, Rth = 24, 4
    P = lambda RL: (Vth / (Rth + RL)) ** 2 * RL
    return dict(nodes=[C('t', 110, Y, '24 V', 'Vth', r=70, size=36),
                       C('r', 345, Y, '4 Ω', 'Rth', r=70, size=36),
                       C('L', 590, Y, f'{g(P(4))} W', f'{g(Vth / 2)} V on 4 Ω', r=90, size=40, subsize=18, lit=True)],
                links=[K('t', 'r', ''), K('r', 'L', '')],
                texts=[T(360, 432, 'RL = 2, 4, 8 Ω: the load power peaks at RL = Rth', 21, GREY)],
                tapes=[tape([f'{g(P(2))} W', f'{g(P(4))} W', f'{g(P(8))} W'], 1, y=462)],
                caption=f'Pmax = 12² ÷ 4 = <b>{g(P(4))} W</b>, not 24² ÷ 4 = {g(Vth ** 2 / 4)} W')


def cs(z, d=0):
    """complex as a ± jb"""
    re, im = z.real, z.imag
    return f'{g(re, d)} {"+" if im >= 0 else "−"} j{g(abs(im), d)}'


def u2L4():          # hook: Zth or its conjugate for max power?  (worked example 4)
    Vth, Zth = complex(10, -10), complex(2, -2)
    ZL = Zth.conjugate()
    I = Vth / (Zth + ZL)
    P = abs(I) ** 2 * ZL.real
    return dict(nodes=[C('v', 110, 200, cs(Vth), 'Vth (V)', r=80, size=26, subsize=17),
                       C('z', 345, 200, cs(Zth), 'Zth (Ω)', r=80, size=28, subsize=17),
                       C('l', 590, 200, cs(ZL), 'load = Zth*', r=86, size=28, subsize=17, lit=True)],
                links=[K('v', 'z', ''), K('z', 'l', 'j2 − j2 = 0', size=22)],
                texts=[T(360, 360, f'|Vth|² ÷ 4R = {g(abs(Vth) ** 2)} ÷ {g(4 * ZL.real)} = {g(P)} W', 26, BLUE)],
                tapes=[tape(['load as drawn 20 W', f'Zth* {g(P)} W'], 1, y=420)],
                caption='flip the sign of the reactance: <b>the conjugate</b>')


# ---------------------------------------------------------------- unit 3
def u3L1():          # hook: Is 230 V the peak or the RMS?  (325 sin 314t)
    Vm = 325
    Vrms = Vm / math.sqrt(2)
    Vav = 2 * Vm / math.pi
    return dict(nodes=[C('p', 110, Y, f'{Vm} V', 'peak', r=76, size=34),
                       C('r', 345, Y, f'{g(Vrms)} V', 'RMS', r=88, size=34, lit=True),
                       C('a', 590, Y, f'{g(Vav)} V', 'average', r=78, size=30)],
                links=[K('p', 'r', '÷ √2'), K('r', 'a', f'÷ {g(Vrms / Vav, 2)}')],
                texts=[T(360, 432, 'v(t) = 325 sin(314t) V: the 50 Hz mains', 23, GREY)],
                tapes=[tape([f'FF {g(Vrms / Vav, 2)}', f'PF {g(Vm / Vrms, 3)}'], None, y=462)],
                caption='230 V is the RMS value: <b>peak ≈ 325 V</b>')


def u3L2():          # hook: Does the current lead or lag?  (series RLC 40 ohm, 0.15 H, 50 uF, 50 Hz)
    w = 314.16
    Rr, XL, XC = 40, w * 0.15, 1 / (w * 50e-6)
    X = XL - XC
    ang = math.degrees(math.atan2(-X, Rr))
    return dict(nodes=[C('l', 120, 160, f'{g(XL, 2)} Ω', 'XL', r=74, size=28),
                       C('c', 120, 420, f'{g(XC, 2)} Ω', 'XC', r=74, size=28),
                       C('x', 360, 290, f'{g(X, 2)} Ω', 'X = XL − XC', r=80, size=28, subsize=16, dim=True),
                       C('i', 600, 290, f'{g(ang)}°', 'I leads', r=80, size=36, lit=True)],
                links=[K('l', 'x', ''), K('c', 'x', ''), K('x', 'i', 'X < 0', size=24)],
                texts=[T(360, 560, 'R = 40 Ω, L = 0.15 H, C = 50 μF at 50 Hz', 22, GREY)],
                tapes=[], caption='X below zero is capacitive: <b>I leads V</b>')


def u3L3():          # hook: Delta load: is phase V = line V?  (400 V lines)
    VL = 400
    return dict(nodes=[C('R', 360, 90, 'R', None, r=52, size=34),
                       C('Y', 150, 400, 'Y', None, r=52, size=34),
                       C('B', 570, 400, 'B', None, r=52, size=34)],
                links=[K('R', 'Y', f'{VL} V', arrow=False, lit=True, size=26, lx=-44, ly=-6),
                       K('Y', 'B', f'{VL} V', arrow=False, lit=True, size=26, ly=-24),
                       K('B', 'R', f'{VL} V', arrow=False, lit=True, size=26, lx=44, ly=-6)],
                texts=[T(360, 290, 'each phase sits', 22, GREY), T(360, 318, 'across two lines', 22, GREY)],
                tapes=[tape([f'star {g(VL / math.sqrt(3))} V', f'delta {VL} V'], 1, y=520)],
                caption='delta: <b>phase V = line V</b>, √3 goes on the current')


def u3L4():          # hook: Where does the root 3 go?  (two wattmeters, W1 = 5.5 kW, W2 = 2.5 kW)
    W1, W2 = 5.5, 2.5
    P = W1 + W2
    phi = math.atan(math.sqrt(3) * (W1 - W2) / P)
    phiw = math.atan((W1 - W2) / P)
    return dict(nodes=[C('w1', 120, 175, f'{W1} kW', 'W₁', r=70, size=30),
                       C('w2', 120, 425, f'{W2} kW', 'W₂', r=70, size=30),
                       C('p', 360, 300, f'{g(P)} kW', 'W₁ + W₂', r=74, size=32, subsize=16, ok=True),
                       C('f', 600, 300, f'{g(math.cos(phi), 3)}', 'pf lagging', r=78, size=34, lit=True)],
                links=[K('w1', 'p', ''), K('w2', 'p', ''), K('p', 'f', '', size=22)],
                texts=[T(360, 120, f'tan φ = √3 (W₁ − W₂) ÷ (W₁ + W₂)', 22, BLUE),
                       T(360, 520, f'√3 × {g(W1 - W2)} ÷ {g(P)} = {g(math.tan(phi), 3)}', 24, BLUE)],
                tapes=[], caption=f'√3 on the difference: <b>pf {g(math.cos(phi), 3)}</b>, not {g(math.cos(phiw), 3)}')


# ---------------------------------------------------------------- unit 4
def u4L1():          # hook: At parallel resonance, is Z max or min?  (R = 1 kOhm, 10 mH, 1 uF, 10 V)
    Rr, L, Cc, V = 1e3, 10e-3, 1e-6, 10
    w0 = 1 / math.sqrt(L * Cc)
    Is, IL, IC = V / Rr, V / (w0 * L), V * w0 * Cc
    return dict(nodes=[C('s', 130, 300, f'{g(Is * 1000)} mA', 'supply: min', r=84, size=32, subsize=18, lit=True),
                       C('l', 590, 150, f'{g(IL * 1000)} mA', 'in L', r=74, size=30),
                       C('c', 590, 450, f'{g(IC * 1000)} mA', 'in C', r=74, size=30)],
                links=[K('l', 'c', 'cancel', arrow=False, dim=True, lx=-58), K('s', 'l', ''), K('s', 'c', '')],
                boxes=[dict(x=360, y=300, w=190, h=60, text=f'Z = R = {g(Rr / 1000)} kΩ', size=24, ok=True)],
                texts=[], tapes=[], caption='parallel resonance: <b>Z is maximum</b>, the supply current least')


def u4L2():          # hook: Is the -3 dB gain 0.5 or 0.707?  (RC low-pass, 1 kOhm, 100 nF)
    Rr, Cc = 1e3, 100e-9
    fc = 1 / (2 * math.pi * Rr * Cc)
    G = lambda f: 1 / math.sqrt(1 + (f / fc) ** 2)
    return dict(nodes=[C('a', 110, Y, f'{g(G(fc / 10), 3)}', f'{g(fc / 10, 0)} Hz', r=70, size=32),
                       C('b', 345, Y, f'{g(G(fc), 3)}', f'fc = {g(fc, 0)} Hz', r=82, size=36, subsize=18, lit=True),
                       C('c', 590, Y, f'{g(G(10 * fc), 3)}', f'{g(10 * fc, 0)} Hz', r=70, size=32)],
                links=[K('a', 'b', '−3 dB'), K('b', 'c', '−20 dB/dec', size=22)],
                texts=[T(360, 432, 'RC low-pass, 1 kΩ and 100 nF: gain against frequency', 21, GREY)],
                tapes=[tape(['power ½', f'gain 1/√2 = {g(G(fc), 3)}'], 1, y=462)],
                caption='−3 dB is half the power: <b>gain 0.707</b>, not 0.5')


def u4L3():          # hook: Aiding coils: plus M or plus 2M?  (L1 = 2 H, L2 = 3 H, M = 1 H in series)
    L1, L2, M = 2, 3, 1
    aid, opp = L1 + L2 + 2 * M, L1 + L2 - 2 * M
    return dict(nodes=[C('a', 110, 300, f'{L1} H', 'L₁', r=66, size=34),
                       C('b', 330, 300, f'{L2} H', 'L₂', r=66, size=34),
                       C('p', 590, 150, f'{aid} H', 'aiding', r=78, size=40, lit=True),
                       C('m', 590, 450, f'{opp} H', 'opposing', r=74, size=36, dim=True)],
                links=[K('a', 'b', f'M = {M} H', arrow=False, size=22),
                       K('b', 'p', '+ 2M', size=24, lx=-30, ly=-10), K('b', 'm', '− 2M', size=24, lx=-30, ly=20)],
                texts=[T(360, 575, f'{L1} + {L2} + 2 × {M} = {aid} H, not {L1 + L2 + M} H', 23, BLUE)],
                tapes=[], caption='both mutual voltages count: <b>L₁ + L₂ + 2M</b>')


# ---------------------------------------------------------------- unit 5
def u5L1():          # hook: What is left after one time constant?  (0.5 H, 2 A into 100 ohm)
    L, I0, Rr = 0.5, 2, 100
    tau = L / Rr
    i = lambda t: I0 * math.exp(-t / tau)
    t02 = tau * math.log(I0 / 0.2)
    return dict(nodes=[C('a', 110, Y, f'{I0} A', 't = 0', r=74, size=38),
                       C('b', 345, Y, f'{g(i(tau), 3)} A', f'τ = {g(tau * 1000)} ms', r=80, size=34, lit=True),
                       C('c', 590, Y, '0.2 A', f'{g(t02 * 1000)} ms', r=74, size=36)],
                links=[K('a', 'b', '× e⁻¹'), K('b', 'c', '')],
                texts=[T(360, 432, f'i = 2e<tspan baseline-shift="super" font-size="70%">−{g(1 / tau)}t</tspan> A,  τ = L ÷ R', 24, BLUE)],
                tapes=[tape([f'{g(i(k * tau), 3)}' for k in range(4)], 1, y=462)],
                caption='after one τ, <b>36.8 % is left</b>, not 63.2 %')


def u5L2():          # hook: Overdamped, or does it ring?  (series RLC, L = 1 H, C = 0.01 F; R = 4, 20, 40 ohm)
    L, Cc = 1, 0.01
    w0 = 1 / math.sqrt(L * Cc)
    al = lambda Rr: Rr / (2 * L)
    wd = math.sqrt(w0 ** 2 - al(4) ** 2)
    tp = math.pi / wd
    vp = 10 * (1 + math.exp(-al(4) * tp))
    case = lambda Rr: 'rings' if al(Rr) < w0 else ('critical' if al(Rr) == w0 else 'overdamped')
    return dict(nodes=[C('a', 110, Y, '4 Ω', f'α {g(al(4))}: {case(4)}', r=82, size=36, subsize=18, lit=True),
                       C('b', 345, Y, '20 Ω', f'α {g(al(20))}: {case(20)}', r=82, size=36, subsize=18),
                       C('c', 590, Y, '40 Ω', f'α {g(al(40))}: over', r=82, size=36, subsize=18, dim=True)],
                links=[K('a', 'b', ''), K('b', 'c', '')],
                texts=[T(360, 432, f'α = R ÷ 2L against ω₀ = {g(w0)} rad/s', 24, BLUE)],
                tapes=[tape([f'4 Ω: peak {g(vp, 2)} V', f'ωd = {g(wd, 2)}'], 0, y=462)],
                caption=f'series RLC: α = R ÷ 2L = 2, below 10: <b>it rings</b>')


def u5L3():          # hook: Do zeros decide stability?  (the lesson's trap: a zero at +3, poles on the left)
    return dict(nodes=[C('p1', 200, 160, '×', 'pole', r=56, size=40, subsize=17, ok=True),
                       C('p2', 200, 420, '×', 'pole', r=56, size=40, subsize=17, ok=True),
                       C('z', 560, 290, '+3', 'zero', r=60, size=34, subsize=17, dim=True)],
                links=[],
                svg=['<polyline points="400,70 400,520" fill="none" stroke="#A9B4C6" stroke-width="3" stroke-dasharray="10 8" />',
                     '<polyline points="60,290 690,290" fill="none" stroke="#A9B4C6" stroke-width="3" />'],
                texts=[T(418, 92, 'jω', 24, GREY, anchor='start'), T(200, 560, 'left half plane', 22, '#2FB380'),
                       T(560, 400, 'shapes the response only', 21, GREY)],
                tapes=[], caption='only poles decide: every pole on the left, <b>stable</b>')


# ---------------------------------------------------------------- unit 6
def u6L1():          # hook: Open or short port 2 for z11?  (T network 2, 4 (shunt), 3 ohm)
    za, zs, zb = 2, 4, 3
    z11 = za + zs
    wrong = za + par(zs, zb)
    return dict(nodes=[C('1', 110, 230, '1', 'port 1', r=62, size=34, subsize=17),
                       C('m', 360, 230, '', 'centre', r=40, size=20, subsize=15, dim=True),
                       C('2', 610, 230, '2', 'open', r=62, size=34, subsize=18, lit=True)],
                links=[K('1', 'm', f'{za} Ω', arrow=False, size=24), K('m', '2', f'{zb} Ω', arrow=False, size=24)],
                boxes=[dict(x=360, y=440, w=440, h=62, text=f'port 2 open: z₁₁ = {za} + {zs} = {z11} Ω', size=24, ok=True),
                       dict(x=360, y=530, w=440, h=56, text=f'shorted: {g(wrong, 3)} Ω = 1 / y₁₁', size=21, inset=True)],
                texts=[T(360, 330, f'{zs} Ω to the common line', 21, GREY)],
                tapes=[], caption='every Z test <b>opens</b> the other port')


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def u6L2():          # hook: Which order to multiply ABCD?  (series 2 ohm, shunt 0.25 S, series 3 ohm)
    M1, M2, M3 = [[1, 2], [0, 1]], [[1, 0], [0.25, 1]], [[1, 3], [0, 1]]
    Tm = mm(mm(M1, M2), M3)
    Tr = mm(mm(M3, M2), M1)
    return dict(nodes=[C('a', 110, Y, '2 Ω', 'series', r=66, size=32),
                       C('b', 345, Y, '0.25 S', 'shunt', r=72, size=30),
                       C('c', 590, Y, '3 Ω', 'series', r=66, size=32)],
                links=[K('a', 'b', '×', size=32), K('b', 'c', '×', size=32)],
                texts=[T(360, 120, 'source side on the left, in signal order', 22, GREY),
                       T(360, 548, f'load end first: A = {g(Tr[0][0], 2)}, D = {g(Tr[1][1], 2)}, turned round', 20, GREY)],
                tapes=[tape([f'A {g(Tm[0][0], 2)}', f'B {g(Tm[0][1], 2)}', f'C {g(Tm[1][0], 2)}', f'D {g(Tm[1][1], 2)}'], 0, y=430)],
                caption='[T] = [T₁][T₂][T₃]: <b>signal order</b>')


def u6L3():          # hook: Cascade: add or multiply ABCD?  (two T sections, [T] = [1.5 6.5; 0.25 1.75])
    Ta = [[1.5, 6.5], [0.25, 1.75]]
    P = mm(Ta, Ta)
    S = [[2 * Ta[i][j] for j in range(2)] for i in range(2)]
    det = lambda M: M[0][0] * M[1][1] - M[0][1] * M[1][0]
    return dict(nodes=[C('a', 110, 300, 'T', 'section a', r=64, size=40, subsize=16),
                       C('b', 330, 300, 'T', 'section b', r=64, size=40, subsize=16),
                       C('p', 590, 160, '×', f'AD − BC = {g(det(P), 3)}', r=84, size=44, subsize=19, lit=True),
                       C('s', 590, 440, '+', f'AD − BC = {g(det(S), 3)}', r=80, size=44, subsize=19, dim=True)],
                links=[K('a', 'b', 'cascade', arrow=False, size=22),
                       K('b', 'p', 'multiply', size=22, lx=-52, ly=-14), K('b', 's', 'add', dim=True, size=22, lx=-40, ly=22)],
                texts=[T(360, 565, f'[Ta][Tb]: A = {g(P[0][0], 3)}, B = {g(P[0][1], 3)}, C = {g(P[1][0], 4)}', 21, BLUE)],
                tapes=[], caption='cascade: <b>multiply</b>, source side on the left')


def u6L4():          # hook: Which test means reciprocal?  (the T: z11 = 6, z12 = z21 = 4, z22 = 7)
    z11, z12, z21, z22 = 6, 4, 4, 7
    A, B, Cc, D = z11 / z21, (z11 * z22 - z12 * z21) / z21, 1 / z21, z22 / z21
    return dict(nodes=[C('r', 150, 240, f'{g(A * D - B * Cc)}', 'AD − BC', r=84, size=44, subsize=18, ok=True),
                       C('s', 570, 240, f'{g(A, 2)} ≠ {g(D, 2)}', 'A vs D', r=84, size=30, subsize=18, dim=True)],
                boxes=[dict(x=150, y=420, w=240, h=56, text=f'z₁₂ = z₂₁ = {z12} Ω', size=22, inset=True),
                       dict(x=570, y=420, w=240, h=56, text=f'z₁₁ = {z11} ≠ z₂₂ = {z22}', size=22, inset=True)],
                links=[],
                texts=[T(150, 120, 'reciprocal', 26, '#2FB380'), T(570, 120, 'not symmetric', 26, GREY)],
                tapes=[], caption='reciprocal when <b>AD − BC = 1</b>; symmetric when A = D')


ALL = {'ec-circuits-u1-L1': u1L1, 'ec-circuits-u1-L2': u1L2, 'ec-circuits-u1-L3': u1L3, 'ec-circuits-u1-L4': u1L4,
       'ec-circuits-u2-L1': u2L1, 'ec-circuits-u2-L2': u2L2, 'ec-circuits-u2-L3': u2L3, 'ec-circuits-u2-L4': u2L4,
       'ec-circuits-u3-L1': u3L1, 'ec-circuits-u3-L2': u3L2, 'ec-circuits-u3-L3': u3L3, 'ec-circuits-u3-L4': u3L4,
       'ec-circuits-u4-L1': u4L1, 'ec-circuits-u4-L2': u4L2, 'ec-circuits-u4-L3': u4L3,
       'ec-circuits-u5-L1': u5L1, 'ec-circuits-u5-L2': u5L2, 'ec-circuits-u5-L3': u5L3,
       'ec-circuits-u6-L1': u6L1, 'ec-circuits-u6-L2': u6L2, 'ec-circuits-u6-L3': u6L3, 'ec-circuits-u6-L4': u6L4}

if __name__ == '__main__':
    src, dst = sys.argv[1], sys.argv[2]
    Dj = json.load(open(src, encoding='utf-8'))
    for k, L in Dj['lessons'].items():
        if k in ALL:
            e2 = ALL[k]()
            ys = {n['y'] for n in e2['nodes']}
            if ys == {Y}:                       # single row: sit it lower, nearer the middle of the picture
                for grp in ('nodes', 'texts', 'tapes', 'boxes'):
                    for it in e2.get(grp, []):
                        it['y'] += 25
            L['t16'] = {'style': 'emboss', 'e2': e2}
    json.dump(Dj, open(dst, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('t16 blocks:', sum(1 for k in Dj['lessons'] if k in ALL))
