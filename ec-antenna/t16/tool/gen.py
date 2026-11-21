"""Write the t16 emboss (e2) block for every Antennas, RF and Microwave Engineering lesson (ec-antenna).
Every value is computed here from the lesson's own worked examples and exam traps (branches lesson/ec-antenna-uN-Lk,
books/ece/ec-antenna on main). The drawing follows the hook in thumbs.json (hooks are final).
Renderer: t16.py with the e2 Stage path (as on deliver/ec-circuits), plus 'ec-antenna': 'emboss' in STYLE_OF.
Usage: python3 gen.py <thumbs.json in> <thumbs.json out>"""
import json, math, sys


def C(id, x, y, text, sub=None, r=66, size=None, **kw):
    n = dict(id=id, x=round(x), y=round(y), text=text, r=r, **kw)
    if sub: n['sub'] = sub
    if size: n['size'] = size
    return n


def K(a, b, label=None, **kw):
    return dict(a=a, b=b, label=label, **kw)


def T(x, y, text, size=22, color='#5B7CFA', **kw):
    return dict(x=x, y=y, text=text, size=size, color=color, **kw)


def tape(cells, head, y=470, cx=360, cw=64):
    w = sum(max(cw, 26 + 17 * len(str(c))) for c in cells) + 12 * (len(cells) - 1)
    return dict(x=round(cx - w / 2), y=y, cells=cells, head=head, cw=cw)


def g(v, d=1):
    """number with d decimals, trailing zeros dropped, true minus sign"""
    s = f'{v:.{d}f}'
    if '.' in s:
        s = s.rstrip('0').rstrip('.')
    return s.replace('-', '−')


def db(x):
    return 10 * math.log10(x)


c0 = 3e8
Y = 250
GREY = '#A9B4C6'
BLUE = '#5B7CFA'
GREEN = '#2FB380'


# ---------------------------------------------------------------- unit 1: lines, Smith chart, waveguides
def u1L1():          # Can VSWR ever be below 1?  (worked example 3: 50 ohm line, ZL = 100 + j50)
    Z0, ZL = 50, 100 + 50j
    G = abs((ZL - Z0) / (ZL + Z0))
    S = (1 + G) / (1 - G)
    wrong = (1 - G) / (1 + G)
    return dict(nodes=[C('z', 110, Y, f'{g(ZL.real)} + j{g(ZL.imag)}', 'on 50 Ω', r=72, size=26, subsize=18),
                       C('g', 345, Y, f'{g(G, 3)}', '|Γ|', r=70, size=38, subsize=20),
                       C('s', 590, Y, f'{g(S, 2)}', 'VSWR', r=80, size=46, subsize=20, lit=True)],
                links=[K('z', 'g', '(Z − Z₀)/(Z + Z₀)', size=20), K('g', 's', '(1 + |Γ|)/(1 − |Γ|)', size=20)],
                texts=[T(360, 418, f'flipped, (1 − |Γ|)/(1 + |Γ|) = {g(wrong, 2)}: impossible', 21, GREY)],
                tapes=[tape(['matched 1', f'this load {g(S, 2)}', 'short ∞'], 1, y=448)],
                caption='VSWR runs from 1 to ∞: <b>never below 1</b>')


def u1L2():          # Does a lambda/4 line match any load?  (70.71 ohm section: 100 ohm vs 100 + j50 ohm)
    Zq = math.sqrt(50 * 100)
    Zr = Zq ** 2 / 100
    Zc = Zq ** 2 / (100 + 50j)
    return dict(nodes=[C('q', 130, 300, f'{g(Zq, 2)} Ω', 'λ/4 section', r=82, size=32, subsize=18, lit=True),
                       C('a', 560, 140, f'{g(Zr)} Ω', 'ZL = 100 Ω', r=80, size=40, subsize=18, ok=True),
                       C('b', 560, 450, f'{g(Zc.real)} − j{g(-Zc.imag)}', 'ZL = 100 + j50', r=84, size=28, subsize=17, dim=True)],
                links=[K('q', 'a', 'real load', size=22, lx=-36, ly=-30), K('q', 'b', 'complex load', dim=True, size=22, lx=-46, ly=36)],
                texts=[T(150, 450, 'Zin = Z₀′² / ZL', 24, BLUE)],
                tapes=[], caption='λ/4 matches a <b>real load</b>; cancel the j part first')


def u1L3():          # How far does lambda/4 turn the Smith chart?  (zL = 2 + j1 turns to 0.4 - j0.2)
    z = (100 + 50j) / 50
    G = (z - 1) / (z + 1)
    y = 1 / z
    S = (1 + abs(G)) / (1 - abs(G))
    ang = math.atan2(G.imag, G.real)           # 26.57 deg
    cx, cy, R = 360, 285, 170
    zx, zy = cx + R * math.cos(ang), cy - R * math.sin(ang)
    yx, yy = cx - R * math.cos(ang), cy + R * math.sin(ang)
    turn = 2 * 360 * 0.25                       # 2 beta d in degrees for d = lambda/4
    # clockwise (towards the generator) along the circle, from just past the load node to just before y
    sz = -ang                                   # screen angle of the load point (y axis points down)
    pt = lambda t: (cx + R * math.cos(t), cy + R * math.sin(t))
    a0 = pt(sz + 2 * math.asin(80 / (2 * R)))
    a1 = pt(sz + math.radians(turn) - 2 * math.asin(92 / (2 * R)))
    return dict(nodes=[C('z', zx, zy, f'{g(z.real)} + j{g(z.imag)}', 'load', r=70, size=30, subsize=18),
                       C('y', yx, yy, f'{g(y.real)} − j{g(-y.imag)}', 'after λ/4', r=76, size=26, subsize=18, lit=True),
                       C('o', cx, cy, '1', 'match', r=44, size=30, subsize=14, dim=True)],
                svg=[f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="#A9B4C6" stroke-width="3" stroke-dasharray="8 10"/>',
                     f'<path d="M{a0[0]:.0f},{a0[1]:.0f} A{R},{R} 0 0 1 {a1[0]:.0f},{a1[1]:.0f}" fill="none" stroke="#FFD666" stroke-width="5" '
                     f'stroke-linecap="round" marker-end="url(#my)" filter="url(#sh)"/>'],
                links=[],
                texts=[T(cx, 70, f'VSWR {g(S, 2)} circle', 22, GREY), T(cx + 20, cy + 100, f'λ/4 = {g(turn)}°', 26, BLUE)],
                tapes=[tape(['λ/8: 90°', f'λ/4: {g(turn)}°', 'λ/2: 360°'], 1, y=500)],
                caption='2βd: one full turn is <b>λ/2</b>, not λ')


def u1L4():          # Which wall sets the waveguide cutoff?  (WR-90: a = 2.286 cm, b = 1.016 cm)
    a, b = 0.02286, 0.01016
    f10, f01, f20 = c0 / (2 * a), c0 / (2 * b), c0 / a
    return dict(nodes=[C('a', 130, 150, f'a = {g(a * 100, 3)}', 'broad wall, cm', r=80, size=26, subsize=16, lit=True),
                       C('fa', 560, 150, f'{g(f10 / 1e9, 2)} GHz', 'TE₁₀ cutoff', r=84, size=28, subsize=17, ok=True),
                       C('b', 130, 410, f'b = {g(b * 100, 3)}', 'narrow wall, cm', r=76, size=26, subsize=15, dim=True),
                       C('fb', 560, 410, f'{g(f01 / 1e9, 2)} GHz', 'TE₀₁ cutoff', r=84, size=26, subsize=16, dim=True)],
                links=[K('a', 'fa', 'c / 2a', lit=True, size=26), K('b', 'fb', 'c / 2b', dim=True, size=26)],
                texts=[T(360, 560, f'single mode: {g(f10 / 1e9, 2)} to {g(f20 / 1e9, 2)} GHz', 22, BLUE)],
                tapes=[], caption='TE₁₀ cutoff is set by <b>the broad wall a</b>')


# ---------------------------------------------------------------- unit 2: radiation, wire antennas, link budget
def u2L1():          # Half power: field 0.5 or 0.707?  (Hertzian dipole, F = sin theta)
    e = 1 / math.sqrt(2)
    t1 = math.degrees(math.asin(e))
    t2 = 180 - t1
    w1 = math.degrees(math.asin(0.5))
    return dict(nodes=[C('a', 120, 150, f'{g(t1)}°', f'sin θ = {g(e, 3)}', r=70, size=38, subsize=16),
                       C('b', 120, 420, f'{g(t2)}°', f'sin θ = {g(e, 3)}', r=70, size=38, subsize=16),
                       C('h', 520, 285, f'{g(t2 - t1)}°', 'HPBW', r=88, size=52, subsize=20, lit=True)],
                links=[K('a', 'h', '', size=22), K('b', 'h', '', size=22)],
                texts=[T(470, 440, 'field 0.707 = power 0.5 (−3 dB)', 22, BLUE),
                       T(470, 474, f'field 0.5 gives {g(180 - 2 * w1)}°: wrong', 21, GREY)],
                tapes=[], caption='half power is <b>field 0.707</b>, not 0.5')


def u2L2():          # Where does the far field begin?  (0.6 m dish at 12 GHz and 24 GHz)
    D = 0.6
    lam = c0 / 12e9
    near = 0.62 * math.sqrt(D ** 3 / lam)
    far = 2 * D ** 2 / lam
    far24 = 2 * D ** 2 / (c0 / 24e9)
    return dict(nodes=[C('d', 110, Y, f'{g(D)} m', f'dish, {g(D / lam)}λ', r=66, size=34, subsize=16),
                       C('n', 345, Y, f'{g(near, 2)} m', 'reactive edge', r=72, size=32, subsize=15),
                       C('ff', 590, Y, f'{g(far, 1)} m', 'far field', r=82, size=36, subsize=18, lit=True)],
                links=[K('d', 'n', '0.62√(D³/λ)', size=21), K('n', 'ff', '2D²/λ', size=24, lit=True)],
                texts=[T(360, 418, f'at 12 GHz λ = {g(lam * 100, 1)} cm; a 20 m test range is too close', 20, GREY)],
                tapes=[tape([f'12 GHz: {g(far, 1)} m', f'24 GHz: {g(far24, 1)} m'], 0, y=448)],
                caption='far field from <b>2D²/λ</b>: higher f, farther out')


def u2L3():          # Why is a folded dipole 300 ohm?  (two arms, same current: field x 2, power x 4)
    Rd = 73
    Rf = 4 * Rd
    return dict(nodes=[C('d', 100, Y, f'{Rd} Ω', 'dipole', r=62, size=34, subsize=17),
                       C('e', 272, Y, '× 2', 'field', r=60, size=36, subsize=17),
                       C('p', 448, Y, '× 4', 'power', r=60, size=36, subsize=17),
                       C('f', 625, Y, f'{Rf} Ω', 'folded', r=70, size=34, subsize=17, lit=True)],
                links=[K('d', 'e', 'same I', size=20), K('e', 'p', 'squared', size=20), K('p', 'f', '', lit=True)],
                texts=[T(360, 418, f'not 2 × {Rd} = {2 * Rd} Ω: two arms double the field', 21, GREY)],
                tapes=[tape([f'{Rd} Ω', '× 4', f'{Rf} Ω ≈ 300 Ω'], 2, y=448)],
                caption='same current in both arms: <b>4 × 73 Ω</b>')


def u2L4():          # Does this link have fade margin?  (Wi-Fi 2.4 GHz, 100 mW, 100 m, 2 dB cables, -90 dBm)
    f, Pt, d, Lc, sens = 2.4e9, 0.1, 100, 2.0, -90
    lam = c0 / f
    Ptd = db(Pt / 1e-3)
    fspl = 20 * math.log10(4 * math.pi * d / lam)
    Pr = Ptd - fspl - Lc
    M = Pr - sens
    return dict(nodes=[C('t', 110, Y, f'{g(Ptd)} dBm', '100 mW out', r=70, size=30, subsize=17),
                       C('r', 345, Y, f'{g(Pr, 2)}', 'dBm received', r=78, size=34, subsize=16),
                       C('s', 590, Y, f'+{g(M, 1)} dB', 'fade margin', r=82, size=34, subsize=18, ok=True)],
                links=[K('t', 'r', f'− {g(fspl, 2)} − {g(Lc)} dB', size=21), K('r', 's', f'− ({g(sens)} dBm)', size=21, lit=True)],
                texts=[T(360, 418, f'FSPL at {d} m, λ = {g(lam, 3)} m; sensitivity {g(sens)} dBm', 20, GREY)],
                tapes=[tape(['M = Pr − Psens', f'+{g(M, 1)} dB'], 1, y=448)],
                caption='received minus sensitivity: <b>+28 dB to fade</b>')


# ---------------------------------------------------------------- unit 3: arrays and aperture antennas
def u3L1():          # Two antennas: twice or 4x the power?  (two equal in-phase elements, broadside)
    E = 1
    Et = E + E
    return dict(nodes=[C('a', 120, 150, 'E', 'antenna 1', r=64, size=44, subsize=16),
                       C('b', 120, 420, 'E', 'antenna 2', r=64, size=44, subsize=16),
                       C('s', 360, 285, f'{Et}E', 'fields add', r=70, size=42, subsize=16),
                       C('p', 600, 285, f'{Et ** 2}E²', 'power', r=76, size=40, subsize=18, lit=True)],
                links=[K('a', 's', 'in phase', size=21, lx=30, ly=-30), K('b', 's', 'in phase', size=21, lx=30, ly=34),
                       K('s', 'p', 'square', size=22, lit=True)],
                texts=[T(520, 440, f'not P₁ + P₁ = 2P₁', 22, GREY), T(520, 474, f'4 × one element, broadside', 21, BLUE)],
                tapes=[], caption='add the <b>fields</b>, then square')


def u3L2():          # Do more directors widen a Yagi's band?  (3-element Yagi at 500 MHz, band 2 to 5 %)
    f = 500
    lam = c0 / (f * 1e6) * 1000
    refl, drv, dirc = 0.50 * lam, 0.47 * lam, 0.45 * lam
    b1, b2 = 0.02 * f, 0.05 * f
    return dict(nodes=[C('r', 110, 230, f'{g(refl)}', 'reflector, mm', r=68, size=36, subsize=15),
                       C('d', 345, 230, f'{g(drv)}', 'driven, mm', r=70, size=36, subsize=15),
                       C('f', 590, 230, f'{g(dirc)}', 'director, mm', r=68, size=36, subsize=15, lit=True)],
                links=[K('r', 'd', f'{g(0.25 * lam)} mm', size=22), K('d', 'f', f'{g(0.20 * lam)} mm', size=22)],
                texts=[T(360, 360, 'more directors: more gain, a narrower band', 22, BLUE),
                       T(360, 396, 'for a wide band, use a log-periodic array', 20, GREY)],
                tapes=[tape(['2 to 5 %', f'{g(b1)} to {g(b2)} MHz', '≈ 490–510 MHz'], 0, y=440)],
                caption='a Yagi is <b>narrowband</b> at 500 MHz')


def u3L3():          # How long is a 2.4 GHz patch?  (FR-4, er 4.4, h 1.6 mm)
    f, er, h = 2.4e9, 4.4, 1.6e-3
    lam = c0 / f
    W = lam / 2 * math.sqrt(2 / (er + 1))
    ee = (er + 1) / 2 + (er - 1) / 2 * (1 + 12 * h / W) ** -0.5
    dL = 0.412 * h * (ee + 0.3) * (W / h + 0.264) / ((ee - 0.258) * (W / h + 0.8))
    L = lam / (2 * math.sqrt(ee)) - 2 * dL
    return dict(nodes=[C('w', 100, Y, f'{g(W * 1000, 2)}', 'W, mm', r=62, size=30, subsize=16),
                       C('e', 272, Y, f'{g(ee, 3)}', 'εeff', r=62, size=30, subsize=17),
                       C('d', 448, Y, f'{g(dL * 1000, 3)}', 'ΔL, mm', r=62, size=30, subsize=16),
                       C('l', 625, Y, f'{g(L * 1000, 1)}', 'L, mm', r=72, size=36, subsize=17, lit=True)],
                links=[K('w', 'e', ''), K('e', 'd', ''), K('d', 'l', '', lit=True)],
                texts=[T(360, 400, f'not λ₀/2 = {g(lam / 2 * 1000, 1)} mm: the board slows the wave', 21, GREY)],
                tapes=[tape(['FR-4', 'εr 4.4', 'h 1.6 mm', 'L = λg/2 − 2ΔL'], 3, y=440)],
                caption=f'a 2.4 GHz patch is <b>{g(L * 1000, 1)} mm</b> long')


# ---------------------------------------------------------------- unit 4: microwave components and sources
def u4L1():          # Which S-parameter is port 1 to 2?  (S11 = 0.2, S21 = 0.9 at -30 deg, S12 = 0)
    S11, S21 = 0.2, 0.9
    IL = -20 * math.log10(S21)
    return dict(nodes=[C('p1', 110, 300, 'port 1', 'a₁ in', r=70, size=28, subsize=18),
                       C('d', 360, 300, 'DUT', '10 GHz', r=76, size=36, subsize=18),
                       C('p2', 610, 300, 'port 2', 'b₂ out', r=70, size=28, subsize=18, lit=True)],
                links=[K('p1', 'd', '', size=24), K('d', 'p2', 'S₂₁ 0.9∠−30°', size=24, lit=True),
                       K('d', 'p1', f'S₁₁ {g(S11)}', bend=-70, size=22, ly=8),
                       K('p2', 'd', 'S₁₂ = 0', bend=-70, dim=True, size=22, ly=8)],
                texts=[],
                tapes=[tape(['S₂₁ = b₂ / a₁', f'IL {g(IL, 2)} dB'], 0, y=520)],
                caption='S₂₁: <b>out at 2, in at 1</b>')


def u4L2():          # 20 dBm + 20 dBm = 40 dBm?
    p1 = p2 = 10 ** (20 / 10)
    pt = p1 + p2
    return dict(nodes=[C('a', 120, 150, '20 dBm', f'{g(p1)} mW', r=72, size=30, subsize=18),
                       C('b', 120, 420, '20 dBm', f'{g(p2)} mW', r=72, size=30, subsize=18),
                       C('s', 560, 285, f'{g(db(pt))} dBm', f'{g(pt)} mW', r=86, size=36, subsize=20, lit=True)],
                links=[K('a', 's', 'mW add', size=22, lx=-14, ly=-28), K('b', 's', 'mW add', size=22, lx=-14, ly=36)],
                texts=[T(520, 450, 'not 40 dBm (10 W)', 24, GREY), T(520, 486, 'twice the power = +3 dB', 22, BLUE)],
                tapes=[], caption='add <b>milliwatts</b>, not dBm')


def u4L3():          # Does a Gunn diode need a junction?  (GaAs: v 1e5 m/s, 10 GHz, 3.2 kV/cm, 8 V, 0.5 A, 100 mW)
    v, f, Eth = 1e5, 10e9, 3.2e5
    L = v / f
    Vth = Eth * L
    return dict(nodes=[C('v', 110, Y, '8 V', f'Vth {g(Vth, 1)} V', r=66, size=38, subsize=16),
                       C('s', 345, Y, f'{g(L * 1e6)} μm', 'bulk n-GaAs', r=78, size=36, subsize=17, lit=True),
                       C('f', 590, Y, f'{g(f / 1e9)} GHz', 'f = v / L', r=76, size=34, subsize=17, ok=True)],
                links=[K('v', 's', '8 kV/cm', size=22), K('s', 'f', 'domains', size=22)],
                texts=[T(360, 418, 'no p–n junction: electrons drop into the slow valley', 21, GREY)],
                tapes=[tape(['v 10⁵ m/s', f'L {g(L * 1e6)} μm', f'f {g(f / 1e9)} GHz'], 1, y=448)],
                caption='a bulk slab, <b>no junction</b>')


# ---------------------------------------------------------------- unit 5: RF circuits
def u5L1():          # Do noise figures just add in dB?  (LNA 15/2 dB, mixer 10/12 dB, IF 20/10 dB)
    G1, F1 = 10 ** 1.5, 10 ** 0.2
    G2, F2 = 10 ** 1.0, 10 ** 1.2
    F3 = 10 ** 1.0
    F = F1 + (F2 - 1) / G1 + (F3 - 1) / (G1 * G2)
    return dict(nodes=[C('l', 110, Y, 'LNA', 'G 15 · NF 2', r=70, size=34, subsize=15, lit=True),
                       C('m', 345, Y, 'mixer', 'G 10 · NF 12', r=70, size=30, subsize=15),
                       C('i', 590, Y, 'IF', 'G 20 · NF 10', r=70, size=36, subsize=15)],
                links=[K('l', 'm', f'/ {g(G1, 2)}', size=22), K('m', 'i', f'/ {g(G1 * G2, 1)}', size=22)],
                texts=[T(360, 418, f'F = {g(F1, 3)} + {g((F2 - 1) / G1, 3)} + {g((F3 - 1) / (G1 * G2), 4)} = {g(F, 3)}', 22, BLUE)],
                tapes=[tape([f'NF {g(db(F), 2)} dB', 'not 2 + 12 = 14 dB'], 0, y=448)],
                caption='Friis: <b>linear F, divided by gain</b>')


def u5L2():          # Where does the image frequency sit?  (900 MHz RF, 45 MHz IF, high-side LO)
    rf, fi = 900, 45
    lo = rf + fi
    im = lo + fi
    return dict(nodes=[C('r', 110, 160, f'{rf}', 'RF, MHz', r=66, size=36, subsize=16, ok=True),
                       C('l', 345, 160, f'{lo}', 'LO, MHz', r=66, size=36, subsize=16),
                       C('m', 590, 160, f'{im}', 'image, MHz', r=74, size=36, subsize=16, lit=True),
                       C('i', 345, 420, f'{fi}', 'IF, MHz', r=66, size=36, subsize=16)],
                links=[K('r', 'i', f'{lo} − {rf}', size=21, lx=-50, ly=10), K('m', 'i', f'{im} − {lo}', size=21, lx=50, ly=10),
                       K('l', 'i', '', dim=True)],
                texts=[T(360, 548, f'image = LO + IF = RF + 2 × IF', 22, BLUE)],
                tapes=[], caption=f'the image sits <b>2 × IF above</b> the signal')


def u5L3():          # PLL x200: 23 dB or 46 dB more noise?  (N = 200 multiplies phase)
    N = 200
    up = 20 * math.log10(N)
    wrong = 10 * math.log10(N)
    return dict(nodes=[C('r', 110, Y, 'φ', 'reference', r=66, size=44, subsize=17),
                       C('o', 345, Y, f'{N}φ', 'output phase', r=74, size=40, subsize=16),
                       C('n', 590, Y, f'+{g(up)} dB', 'phase noise', r=82, size=36, subsize=18, lit=True)],
                links=[K('r', 'o', f'PLL × {N}', size=22), K('o', 'n', 'power ∝ φ²', size=22, lit=True)],
                texts=[T(360, 418, f'10 log {N} = {g(wrong)} dB counts power, not phase', 21, GREY)],
                tapes=[tape([f'20 log {N}', f'{g(up, 2)} dB'], 0, y=448)],
                caption='multiply the phase by N: <b>noise × N²</b>')


# ---------------------------------------------------------------- unit 6: radar
def u6L1():          # Why does radar range divide by 2?  (echo 124 us after a 1 us pulse)
    t = 124e-6
    R = c0 * t / 2
    return dict(nodes=[C('r', 120, Y, 'radar', f'{g(t * 1e6)} μs', r=72, size=34, subsize=20),
                       C('t', 590, Y, f'{g(R / 1000, 1)} km', 'target', r=84, size=32, subsize=18, lit=True)],
                links=[K('r', 't', 'out', size=24, bend=-24), K('t', 'r', 'back', size=24, bend=-24)],
                texts=[T(355, 418, f'c t = {g(c0 * t / 1000, 1)} km is there and back', 22, GREY)],
                tapes=[tape([f't {g(t * 1e6)} μs', '× c', '÷ 2', f'{g(R / 1000, 1)} km'], 2, y=448)],
                caption='R = c t / 2: <b>out and back</b>')


def u6L2():          # Why is Doppler shift 2v/lambda, not v/lambda?  (10.525 GHz police radar, 100 km/h)
    f, v = 10.525e9, 100 / 3.6
    lam = c0 / f
    one = v / lam
    return dict(nodes=[C('r', 120, 180, 'radar', f'{g(f / 1e9, 3)} GHz', r=72, size=32, subsize=16),
                       C('c', 590, 180, 'car', f'{g(v, 2)} m/s', r=72, size=36, subsize=17),
                       C('d', 355, 440, f'{g(2 * one, 0)} Hz', 'fd = 2v/λ', r=84, size=32, subsize=18, lit=True)],
                links=[K('r', 'c', f'out: +{g(one, 0)} Hz', size=22, bend=-26), K('c', 'r', f'back: +{g(one, 0)} Hz', size=22, bend=-26),
                       K('r', 'd', '', lit=True)],
                texts=[T(600, 440, f'λ = {g(lam * 100, 2)} cm', 22, GREY)],
                tapes=[], caption='shifted going out <b>and again coming back</b>')


def u6L3():          # Does monopulse mean one beam?  (delta 1.2 V, sigma 10 V, k 1.8 per degree, 20 km)
    d, s, k, R = 1.2, 10, 1.8, 20000
    th = d / s / k
    off = R * math.radians(th)
    return dict(nodes=[C('a', 120, 150, 'beam A', 'squinted', r=68, size=28, subsize=16),
                       C('b', 120, 420, 'beam B', 'squinted', r=68, size=28, subsize=16),
                       C('c', 360, 285, 'Δ / Σ', 'comparator', r=72, size=34, subsize=15),
                       C('t', 600, 285, f'{g(th, 4)}°', 'one pulse', r=78, size=32, subsize=17, lit=True)],
                links=[K('a', 'c', '', size=22), K('b', 'c', '', size=22), K('c', 't', f'{g(d)} / {g(s)}', size=22, lit=True)],
                texts=[T(520, 440, f'{g(off, 1)} m off at 20 km', 22, BLUE), T(520, 474, 'several beams, parallel receivers', 20, GREY)],
                tapes=[], caption='mono<b>pulse</b>: one pulse, several beams')


ALL = {f'ec-antenna-{k}': fn for k, fn in {
    'u1-L1': u1L1, 'u1-L2': u1L2, 'u1-L3': u1L3, 'u1-L4': u1L4,
    'u2-L1': u2L1, 'u2-L2': u2L2, 'u2-L3': u2L3, 'u2-L4': u2L4,
    'u3-L1': u3L1, 'u3-L2': u3L2, 'u3-L3': u3L3,
    'u4-L1': u4L1, 'u4-L2': u4L2, 'u4-L3': u4L3,
    'u5-L1': u5L1, 'u5-L2': u5L2, 'u5-L3': u5L3,
    'u6-L1': u6L1, 'u6-L2': u6L2, 'u6-L3': u6L3}.items()}

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
    print('t16 blocks:', sum(1 for k in Dj['lessons'] if k in ALL), 'of', len(Dj['lessons']))
