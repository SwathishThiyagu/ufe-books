"""Claude's hand-drawn figures for c-quantum-u4 (Quantum Computing, unit 4: quantum algorithms),
one per chapter, each drawn from that chapter's worked example with its own numbers."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {}


def sbars(x, base, vals, labels, h=70, bw=46, gap=20, fmt=None, colors=None):
    """signed bars around a baseline"""
    o = [L(x - 8, base, x + len(vals) * (bw + gap) - gap + 8, base, L2, 1.5)]
    for i, (v, lab) in enumerate(zip(vals, labels)):
        bx = x + i * (bw + gap); hh = abs(v) * h
        c, f = colors[i] if colors else ((AC, ACS) if v >= 0 else (NX, NXS))
        if hh: o.append(R(bx, base - hh if v >= 0 else base, bw, hh, f, c, 3))
        txt = fmt(v) if fmt else f'{v:+g}'.replace('-', '−')
        o.append(T(bx + bw / 2, (base - hh - 7) if v >= 0 else (base + hh + 17), txt, 13, bold=True))
        o.append(T(bx + bw / 2, base + (20 if v >= 0 else -8) if hh == 0 or v > 0 else base - 8, lab, 13, fill=MUT))
    return ''.join(o)


# ---- 4.1 phase kickback with the parity oracle ----
def f1():
    o = [T(20, 26, 'Parity oracle f(x) = x₁ ⊕ x₂ with the ancilla in |−⟩', 15, 'start', bold=True)]
    labs = ['|00⟩', '|01⟩', '|10⟩', '|11⟩']
    o.append(T(40, 64, 'after H on both inputs', 14, 'start', AC, True))
    o.append(sbars(60, 150, [0.5] * 4, labs, 120, 48, 22))
    o.append(L(372, 120, 420, 120, MUT, 2, arrow='m')); o.append(Tb(396, 108, 'U_f', 14, fill=MUT, bold=True))
    o.append(T(440, 64, 'after one call of U_f', 14, 'start', NX, True))
    o.append(sbars(450, 150, [0.5, -0.5, -0.5, 0.5], labs, 120, 48, 22))
    o.append(T(440, 254, 'f(x):', 14, 'end', MUT, True))
    for i, (lab, fv) in enumerate(zip(labs, [0, 1, 1, 0])):
        o.append(T(474 + i * 70, 254, f'f = {fv}', 13, fill=MUT))
    o.append(T(20, 292, 'Each amplitude is multiplied by (−1)^f(x): signs +, −, −, + . The probabilities stay ¼ each.', 14, 'start'))
    o.append(T(20, 316, 'The ancilla stays |−⟩: the value f(x) has been kicked back into a sign on the input.', 14, 'start', MUT))
    return 332, ''.join(o)
FIG[1] = (f1, 'After the Hadamards every input |00⟩ … |11⟩ has amplitude 1/2; one call of the parity oracle with the ancilla in |−⟩ flips the signs of |01⟩ and |10⟩, giving +1/2, −1/2, −1/2, +1/2.',
          'Two bar charts over the four inputs: before the oracle all four bars are plus one half; after it the bars for 01 and 10 point down to minus one half.')


# ---- 4.2 Deutsch-Jozsa: the 00 amplitude is the average sign ----
def f2():
    o = [T(20, 26, 'Deutsch–Jozsa, n = 2: amplitude of 00 = (sum of the four signs) ÷ 4', 15, 'start', bold=True)]
    def row(y, title, signs, c, f, res):
        p = [T(20, y - 14, title, 14, 'start', c, True)]
        for i, (x_, s) in enumerate(zip(['00', '01', '10', '11'], signs)):
            bx = 30 + i * 96
            p.append(boxt(bx, y, 80, 52, [f'x = {x_}', '+1' if s > 0 else '−1'], f if s > 0 else NXS, c if s > 0 else NX, 14, True))
            if i < 3: p.append(T(bx + 88, y + 32, '+', 16, fill=MUT, bold=True))
        p.append(T(420, y + 32, '→', 18, fill=MUT, bold=True))
        p.append(boxt(450, y, 250, 52, res, f, c, 14, True))
        return ''.join(p)
    o.append(row(70, 'the given f: 0, 1, 1, 0 (balanced)', [1, -1, -1, 1], AC, ACS, ['sum 0 → a₀₀ = 0/4 = 0', 'P(00) = 0: balanced']))
    o.append(row(180, 'for comparison, f = 0 everywhere (constant)', [1, 1, 1, 1], LV, LVS, ['sum 4 → a₀₀ = 4/4 = 1', 'P(00) = 1: constant']))
    o.append(T(20, 272, 'Sign of input x is (−1)^f(x). One query decides: 00 never appears for a balanced f,', 14, 'start'))
    o.append(T(20, 296, 'and always appears for a constant one.', 14, 'start'))
    return 312, ''.join(o)
FIG[2] = (f2, 'For f = 0, 1, 1, 0 the signs +1, −1, −1, +1 add to 0, so the amplitude of 00 is 0 and P(00) = 0: f is balanced. A constant f would give 4/4 = 1.',
          'Two rows of four sign boxes: the given balanced function with signs plus, minus, minus, plus summing to 0, and a constant function with four plus signs summing to 4.')


# ---- 4.3 Bernstein-Vazirani, s = 101 ----
def f3():
    o = [T(20, 26, 'Bernstein–Vazirani, s = 101: signs after the oracle, then the output', 15, 'start', bold=True)]
    xs = ['000', '001', '010', '011', '100', '101', '110', '111']
    signs = [1, -1, 1, -1, -1, 1, -1, 1]
    o.append(T(20, 58, 'sign (−1)^(s·x), with s·x = x₁ ⊕ x₃', 14, 'start', MUT))
    o.append(sbars(40, 130, [s * 0.3536 for s in signs], xs, 130, 60, 26, fmt=lambda v: '+' if v > 0 else '−'))
    o.append(T(20, 216, 'after the final H on all three qubits: probability of each output', 14, 'start', MUT))
    base = 340
    for i, x_ in enumerate(xs):
        bx = 40 + i * 86
        v = 1 if x_ == '101' else 0
        if v: o.append(R(bx, base - 100, 60, 100, LVS, LV, 3))
        o.append(T(bx + 30, base - (108 if v else 8), '1' if v else '0', 13 if not v else 15, bold=True, fill=INK if v else MUT))
        o.append(T(bx + 30, base + 20, x_, 13, fill=LV if v else MUT, bold=bool(v)))
    o.append(L(32, base, 700, base, L2, 1.5))
    o.append(T(20, 388, 'At y = 101 all eight signs line up (8/8 = 1); every other output cancels to 0. One query finds s.', 14, 'start'))
    return 404, ''.join(o)
FIG[3] = (f3, 'With s = 101 the oracle puts a minus sign on the four inputs with x₁ ⊕ x₃ = 1; the final Hadamards make every output cancel except 101, which is measured with probability 1.',
          'Top: eight amplitude bars for inputs 000 to 111, four up and four down. Bottom: the output probabilities, 0 everywhere except a bar of height 1 at 101.')


# ---- 4.4 QFT|01> on the complex plane ----
def f4():
    cx, cy, r = 215, 210, 135
    o = [T(20, 26, 'QFT|01⟩ for N = 4: amplitude of |k⟩ is ½·e^(iπk/2)', 15, 'start', bold=True)]
    o.append(L(cx - r - 30, cy, cx + r + 30, cy, L2, 1.5)); o.append(L(cx, cy + r + 24, cx, cy - r - 24, L2, 1.5))
    o.append(T(cx + r + 30, cy - 8, 'Re', 13, 'end', MUT)); o.append(T(cx - 10, cy - r - 12, 'Im', 13, 'end', MUT))
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" style="fill:none;stroke:var(--line);stroke-width:1.2;stroke-dasharray:4 4"/>')
    o.append(T(cx + r * 0.72, cy - r * 0.72 - 8, 'length ½', 13, 'start', MUT))
    pts = [(0, '|00⟩: ½', 'middle', (-10, 26)), (90, '|01⟩: i/2', 'start', (10, 0)), (180, '|10⟩: −½', 'middle', (16, 26)), (270, '|11⟩: −i/2', 'start', (10, 6))]
    cols = [AC, NX, LV, AC]
    for (ang, lab, an, (dx, dy)), c in zip(pts, cols):
        a = math.radians(ang)
        e = (cx + r * math.cos(a), cy - r * math.sin(a))
        o.append(L(cx, cy, e[0], e[1], c, 3.5, arrow={AC: 'n', NX: 'x', LV: 'l'}[c]))
        o.append(Tb(e[0] + dx, e[1] + dy, lab, 14, an, c, True))
    o.append(f'<path d="M{cx + 50},{cy - 4} A50,50 0 0 0 {cx + 4},{cy - 50}" style="fill:none;stroke:{MUT};stroke-width:2" marker-end="url(#ar-UID-m)"/>')
    o.append(Tb(cx + 46, cy - 46, '+90°', 13, 'start', MUT, True))
    X = 420
    rows = [('k = 0', 'e⁰ = 1', '0.5 + 0.0i'), ('k = 1', 'e^(iπ/2) = i', '0.0 + 0.5i'), ('k = 2', 'e^(iπ) = −1', '−0.5 + 0.0i'), ('k = 3', 'e^(i3π/2) = −i', '0.0 − 0.5i')]
    for i, (k, e, v) in enumerate(rows):
        o.append(boxt(X, 60 + i * 72, 280, 58, [f'{k}: {e}', f'amplitude {v}'], ACS if i % 2 == 0 else NXS, AC if i % 2 == 0 else NX, 14, True))
    o.append(T(20, 400, 'Each step in k turns the amplitude a quarter turn; all four have size ½, so every outcome has probability ¼.', 14, 'start'))
    return 416, ''.join(o)
FIG[4] = (f4, 'QFT|01⟩ gives the amplitudes ½, i/2, −½ and −i/2 on |00⟩, |01⟩, |10⟩ and |11⟩: the same size, each a quarter turn further round the circle.',
          'A complex plane with four arrows of length one half pointing right, up, left and down, labelled with the four basis states, beside a list of the four amplitudes.')


# ---- 4.5 phase estimation recovers the order of 2 mod 15 ----
def f5():
    o = [T(20, 26, 'N = 15, a = 2, t = 3 phase qubits, measured y = 2', 15, 'start', bold=True)]
    cx, cy, r = 150, 190, 90
    vals = [1, 2, 4, 8]
    o.append(T(cx, 72, 'multiply by 2 (mod 15)', 13, fill=MUT))
    for i, v in enumerate(vals):
        a = math.pi / 2 - i * math.pi / 2
        p = (cx + r * math.cos(a), cy - r * math.sin(a))
        b = math.pi / 2 - (i + 1) * math.pi / 2
        q = (cx + r * math.cos(b), cy - r * math.sin(b))
        o.append(arc(p[0] + 20 * math.cos(a - 1.2), p[1] - 20 * math.sin(a - 1.2), q[0] + 26 * math.cos(b + 1.2), q[1] - 26 * math.sin(b + 1.2), -0.25, AC, 2, 'n'))
        o.append(f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="22" style="fill:{ACS};stroke:{AC};stroke-width:2"/>')
        o.append(T(p[0], p[1] + 6, str(v), 16, bold=True))
    o.append(T(cx, cy + 6, 'r = 4', 16, fill=NX, bold=True))
    o.append(T(cx, cy + r + 48, '2⁴ = 16 ≡ 1 (mod 15)', 14, fill=NX, bold=True))
    # number line of y
    x0, x1, yl = 320, 690, 120
    fx = lambda y: x0 + y / 8 * (x1 - x0)
    o.append(L(x0, yl, x1, yl, L2, 2))
    for y in range(9):
        o.append(L(fx(y), yl - 6, fx(y), yl + 6, L2, 1.5)); o.append(T(fx(y), yl + 24, str(y), 13, fill=MUT))
    o.append(C(fx(2), yl, 8, LV))
    o.append(Tb(fx(2), yl - 18, 'y = 2', 14, fill=LV, bold=True))
    o.append(T((x0 + x1) / 2, yl + 46, 'possible outcomes y = 0 … 7, out of 2³ = 8', 13, fill=MUT))
    steps = [['y / 2³ = 2/8 = 1/4'], ['continued fraction → 1/4, q = 4'], ['check 2⁴ mod 15 = 1: r = 4'], ['s/r = 1/4, eigenphase φ = 0.25']]
    for i, s in enumerate(steps):
        y = 196 + i * 50
        o.append(boxt(330, y, 360, 40, s, NXS if i == 2 else PANEL, NX if i == 2 else AC, 14, i == 2))
        if i < 3: o.append(L(510, y + 41, 510, y + 49, AC, 2))
    return 410, ''.join(o)
FIG[5] = (f5, 'Repeated multiplication by 2 modulo 15 cycles 1 → 2 → 4 → 8 → 1, so the order is 4; phase estimation with 3 qubits returns y = 2, and 2/8 = 1/4 gives that denominator 4 directly.',
          'Left: a cycle of four circles 1, 2, 4, 8 joined by arrows, with r = 4 in the middle. Right: a number line from 0 to 8 with y = 2 marked, and four steps from 2/8 to the order 4.')


# ---- 4.6 Shor post-processing for N = 15 ----
def f6():
    o = [T(20, 26, "Shor's classical steps for N = 15 with base a = 2", 15, 'start', bold=True)]
    o.append(T(20, 60, 'powers of 2 modulo 15', 14, 'start', MUT))
    for i, (e, v) in enumerate(((1, 2), (2, 4), (3, 8), (4, 1))):
        x = 30 + i * 120
        o.append(boxt(x, 72, 104, 50, [f'2{"¹²³⁴"[e - 1]} → {v}'], NXS if v == 1 else PANEL, NX if v == 1 else AC, 15, True))
    o.append(T(530, 102, 'first 1 at power 4: r = 4', 14, 'start', NX, True))
    steps = [('r = 4 is even', 'half power 2² = 4', ACS, AC), ('4 is not −1', 'mod 15 (−1 ≡ 14)', ACS, AC),
             ('gcd(4 − 1, 15)', '= gcd(3, 15) = 3', LVS, LV), ('gcd(4 + 1, 15)', '= gcd(5, 15) = 5', LVS, LV)]
    for i, (a, b, f, s) in enumerate(steps):
        x = 30 + i * 170
        o.append(boxt(x, 170, 150, 66, [a, b], f, s, 14, True))
        if i < 3: o.append(L(x + 152, 203, x + 166, 203, s, 2, arrow='n' if s == AC else 'l'))
    o.append(boxt(180, 272, 360, 54, ['15 = 3 × 5'], LVS, LV, 17, True))
    o.append(T(20, 356, 'If r were odd or the half power were ≡ −1, pick a new base and try again.', 14, 'start', MUT))
    return 372, ''.join(o)
FIG[6] = (f6, 'The powers of 2 modulo 15 run 2, 4, 8, 1, so r = 4; the half power 2² = 4 passes the check, and gcd(3, 15) = 3 and gcd(5, 15) = 5 give 15 = 3 × 5.',
          'A row of powers of 2 modulo 15 ending at 1 for the fourth power, then four boxes: r is even with half power 4, 4 is not minus 1, gcd 3 and gcd 5, and the result 15 = 3 × 5.')


# ---- 4.7 Grover success probability for N = 16 ----
def f7():
    th = math.asin(0.25)
    P = [math.sin((2 * k + 1) * th) ** 2 for k in range(6)]
    o = [T(20, 26, 'Grover with N = 16 and one marked item: P(success) after k iterations', 15, 'start', bold=True)]
    x0, x1, y0, y1 = 80, 690, 70, 320
    fy = lambda p: y1 - p * (y1 - y0)
    for v in (0, 0.25, 0.5, 0.75, 1):
        o += [L(x0, fy(v), x1, fy(v), LN, 1), T(x0 - 9, fy(v) + 4.5, f'{v:g}', 13, 'end', MUT)]
    o.append(L(x0, y1, x1, y1, L2, 1.5))
    bw = (x1 - x0) / 6
    for k, p in enumerate(P):
        x = x0 + k * bw + 18
        best = k == 3
        f, s = (LVS, LV) if best else ((ACS, AC) if k < 3 else (PANEL, L2))
        o.append(R(x, fy(p), bw - 36, y1 - fy(p), f, s, 3))
        o.append(T(x + (bw - 36) / 2, fy(p) - 8, f'{p:.4f}', 13, bold=best))
        o.append(T(x + (bw - 36) / 2, y1 + 20, f'k = {k}', 13, fill=MUT))
    o.append(T(x0 + 3.5 * bw, 52, 'best: k = 3 ≈ (π/4)√16', 13, fill=LV, bold=True))
    o.append(T(x0 + 5 * bw, fy(0.6) - 40, 'too many: falls', 13, fill=MUT))
    o.append(T(20, 376, 'θ = arcsin(1/4) = 0.2527 rad and P = sin²((2k + 1)θ): 0.0625, 0.4727, 0.9084, 0.9613, then down.', 14, 'start'))
    return 392, ''.join(o)
FIG[7] = (f7, 'With θ = arcsin(1/4), the success probability sin²((2k + 1)θ) climbs 0.0625, 0.4727, 0.9084 to 0.9613 at k = 3, then falls if more iterations are run.',
          'Bar chart of success probability against iteration count k from 0 to 5; the bars rise to 0.9613 at k = 3 and then drop to about 0.58 and 0.13.')


# ---- 4.8 quantum counting ----
def f8():
    o = [T(20, 26, 'Quantum counting: N = 100, M = 9 marked, t = 8 phase qubits', 15, 'start', bold=True)]
    x0, x1, yl = 80, 660, 110
    fx = lambda y: x0 + (y - 22) / 6 * (x1 - x0)
    o.append(T(20, 64, 'phase register reads y close to 256θ/π = 24.83', 14, 'start', MUT))
    o.append(L(x0, yl, x1, yl, L2, 2))
    for y in range(22, 29):
        o.append(L(fx(y), yl - 7, fx(y), yl + 7, L2, 1.5)); o.append(T(fx(y), yl + 26, str(y), 13, fill=MUT))
    o.append(L(fx(24.83), yl - 30, fx(24.83), yl + 4, NX, 2, '4 3')); o.append(Tb(fx(24.83) - 6, yl - 34, 'ideal 24.83', 13, 'end', NX, True))
    o.append(C(fx(25), yl, 8, AC)); o.append(Tb(fx(25) + 8, yl - 16, 'measured y = 25', 14, 'start', AC, True))
    o.append(T(fx(24.4), yl + 50, '0.17 from 25, 0.83 from 24', 13, fill=MUT))
    steps = [['angle = π × 25/256', '= 0.3068 rad'], ['estimate = 100 sin²(angle)', '= 100 × 0.0912 = 9.12'], ['round', 'M = 9']]
    for i, s in enumerate(steps):
        x = 30 + i * 230
        o.append(boxt(x, 184, 200, 60, s, LVS if i == 2 else ACS, LV if i == 2 else AC, 14, True))
        if i < 2: o.append(L(x + 202, 214, x + 226, 214, AC, 2, arrow='n'))
    yl2 = 310
    gx = lambda m: 120 + (m - 8) / 2 * 480
    o.append(L(gx(8), yl2, gx(10), yl2, L2, 2))
    for m in (8, 8.5, 9, 9.5, 10):
        o.append(L(gx(m), yl2 - 6, gx(m), yl2 + 6, L2, 1.5)); o.append(T(gx(m), yl2 + 24, f'{m:g}', 13, fill=MUT))
    o.append(R(gx(9.12 - 0.7), yl2 - 10, gx(9.82) - gx(8.42), 20, LVS, LV, 4, 1.5))
    o.append(C(gx(9.12), yl2, 7, AC)); o.append(L(gx(9), yl2 - 22, gx(9), yl2 + 8, NX, 2.5))
    o.append(Tb(gx(9) - 6, yl2 - 26, 'true 9', 13, 'end', NX, True)); o.append(Tb(gx(9.12) + 6, yl2 - 26, 'estimate 9.12', 13, 'start', AC, True))
    o.append(T(gx(10) + 20, yl2 + 5, 'error band ±0.7', 13, 'start', LV, True))
    return 350, ''.join(o)
FIG[8] = (f8, 'The ideal reading 256θ/π = 24.83 rounds to y = 25, which gives an estimate of 100 sin²(π·25/256) = 9.12; that is within the error band of about ±0.7 and rounds to the true count of 9.',
          'A number line from 22 to 28 with the ideal value 24.83 and the measured value 25 marked, three boxes converting 25 into 9.12 and then 9, and a second number line showing 9.12 inside a band of plus or minus 0.7 around 9.')


# ---- 4.9 complexity classes ----
def f9():
    o = [T(20, 26, 'Where the problems sit (proved inclusions only)', 15, 'start', bold=True)]
    o.append(f'<ellipse cx="230" cy="210" rx="210" ry="160" style="fill:{PANEL};stroke:{L2};stroke-width:2"/>')
    o.append(T(230, 72, 'PSPACE', 15, fill=MUT, bold=True))
    o.append(f'<ellipse cx="170" cy="225" rx="120" ry="100" style="fill:{NXS};fill-opacity:0.6;stroke:{NX};stroke-width:2"/>')
    o.append(f'<ellipse cx="290" cy="225" rx="120" ry="100" style="fill:{ACS};fill-opacity:0.6;stroke:{AC};stroke-width:2"/>')
    o.append(T(100, 160, 'NP', 16, fill=NX, bold=True)); o.append(T(360, 160, 'BQP', 16, fill=AC, bold=True))
    o.append(f'<ellipse cx="230" cy="270" rx="46" ry="32" style="fill:{LVS};stroke:{LV};stroke-width:2"/>')
    o.append(T(230, 276, 'P', 16, fill=LV, bold=True))
    o.append(C(230, 190, 6, INK)); o.append(Tb(230, 176, 'factoring', 13, bold=True))
    o.append(C(110, 240, 6, NX)); o.append(T(110, 262, 'SAT', 13, fill=NX, bold=True)); o.append(T(110, 278, '(NP-complete)', 13, fill=NX))
    o.append(T(230, 352, 'whether SAT is in BQP: unknown', 13, fill=MUT))
    X = 470
    o.append(T(X, 70, 'SAT with n = 50 variables', 14, 'start', bold=True))
    o.append(boxt(X, 84, 230, 70, ['brute force: 2⁵⁰ checks', '≈ 1.13 × 10¹⁵'], NXS, NX, 14, True))
    o.append(boxt(X, 166, 230, 70, ['Grover: (π/4)·2²⁵ calls', '≈ 2.6 × 10⁷'], ACS, AC, 14, True))
    o.append(boxt(X, 248, 230, 70, ['2ⁿ against 2^(n/2)', 'still exponential in n'], PANEL, L2, 14, True))
    return 380, ''.join(o)
FIG[9] = (f9, 'P sits inside both NP and BQP, and both sit inside PSPACE; factoring is in NP and in BQP, while for SAT with 50 variables Grover cuts 2⁵⁰ ≈ 1.13 × 10¹⁵ checks only to about 2.6 × 10⁷, still exponential.',
          'Nested ovals: PSPACE around two overlapping ovals NP and BQP, with P in their overlap; a dot for factoring in the overlap and a dot for SAT inside NP. Boxes compare 2 to the 50 checks with about 26 million Grover calls.')


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d
