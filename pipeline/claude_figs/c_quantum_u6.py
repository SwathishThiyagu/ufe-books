"""Claude's hand-drawn figures for c-quantum-u6 (Quantum Computing, unit 6: quantum machine learning and applications),
one per chapter, each drawn from that chapter's worked example with its own numbers."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {}


# ---- 6.1 VQE on one qubit ----
def f1():
    x0, x1, y0, y1 = 80, 460, 60, 330
    fx = lambda t: x0 + t / math.pi * (x1 - x0)
    fy = lambda e: y1 - (e + 1.2) / 2.4 * (y1 - y0)
    o = [T(20, 26, 'RY(θ) on |0⟩ with H = Z: measured energy ⟨H⟩ = cos θ', 15, 'start', bold=True)]
    o.append(R(fx(0), y0, fx(math.pi / 2) - fx(0), y1 - y0, LVS, LVS, 0, 0))
    o.append(T(fx(math.pi / 4), y0 + 18, 'allowed: 0 ≤ θ ≤ π/2', 13, fill=LV, bold=True))
    o.append(axes(x0, x1, y0, y1, [0, math.pi / 2, math.pi], [-1, 0, 1], fx, fy, 'angle θ', 'energy', lambda t: {0: '0', 1: 'π/2', 2: 'π'}[round(t / (math.pi / 2))], lambda e: str(e).replace('-', '−')))
    o.append(L(x0, fy(-1), x1, fy(-1), NX, 2, '7 5'))
    o.append(Tb(x0 + 10, fy(-1) + 20, 'E₀ = −1: no θ goes below', 13, 'start', NX, True))
    o.append(P([(fx(i / 100 * math.pi), fy(math.cos(i / 100 * math.pi))) for i in range(101)], AC, 3))
    o.append(C(fx(math.pi), fy(-1), 7, NX)); o.append(Tb(fx(math.pi) - 8, fy(-1) - 14, 'θ = π: |1⟩, −1', 13, 'end', NX, True))
    o.append(C(fx(math.pi / 2), fy(0), 7, LV))
    o.append(L(fx(math.pi / 2), fy(0.1), fx(math.pi / 2), fy(-0.1), LV, 2)); 
    o.append(L(fx(math.pi / 2) - 6, fy(0.1), fx(math.pi / 2) + 6, fy(0.1), LV, 2)); o.append(L(fx(math.pi / 2) - 6, fy(-0.1), fx(math.pi / 2) + 6, fy(-0.1), LV, 2))
    o.append(Tb(fx(math.pi / 2) + 12, fy(0) - 12, 'best allowed: 0 at θ = π/2', 13, 'start', LV, True))
    o.append(L(fx(math.pi / 2) - 30, fy(0), fx(math.pi / 2) - 30, fy(-1) + 3, MUT, 1.5, arrow='m'))
    o.append(Tb(fx(math.pi / 2) - 36, fy(-0.5), 'gap 1', 13, 'end', MUT, True))
    X = 490
    o.append(boxt(X, 60, 214, 66, ['⟨H⟩ = cos²(θ/2) − sin²(θ/2)', '= cos θ'], ACS, AC, 14, True))
    o.append(boxt(X, 140, 214, 66, ['upper bound', 'cos θ ≥ −1 for every θ'], NXS, NX, 14, True))
    o.append(boxt(X, 220, 214, 66, ['100 shots: noise', '≈ 1/√100 = ±0.1'], LVS, LV, 14, True))
    o.append(T(20, 392, 'More shots shrink the ±0.1 noise bar, but cannot close the gap that the restricted angle leaves.', 14, 'start'))
    return 408, ''.join(o)
FIG[1] = (f1, 'The energy ⟨H⟩ = cos θ never falls below E₀ = −1 and reaches it at θ = π; if θ is limited to [0, π/2] the best is 0 at θ = π/2, one unit above E₀, with ±0.1 of shot noise at 100 shots.',
          'A cosine curve of energy against angle from 0 to pi, a dashed floor at minus 1 touched at pi, the allowed range up to pi over 2 shaded, and the best allowed point at 0 with a small noise bar.')


# ---- 6.2 fidelity kernel ----
def f2():
    cx, cy, r = 110, 250, 170
    o = [T(20, 26, 'Feature map |φ(x)⟩ = cos x|0⟩ + sin x|1⟩ and the kernel K = cos²(x − x′)', 15, 'start', bold=True)]
    o.append(L(cx - 10, cy, cx + r + 30, cy, L2, 1.5)); o.append(L(cx, cy + 10, cx, cy - r - 30, L2, 1.5))
    o.append(T(cx + r + 30, cy - 10, '|0⟩', 13, 'end', MUT, True)); o.append(T(cx - 8, cy - r - 18, '|1⟩', 13, 'end', MUT, True))
    o.append(f'<path d="M{cx + r},{cy} A{r},{r} 0 0 0 {cx},{cy - r}" style="fill:none;stroke:var(--line);stroke-width:1.2;stroke-dasharray:4 4"/>')
    for ang, lab, c, arr in ((0, 'x = 0', AC, 'n'), (45, 'x = π/4', NX, 'x'), (90, 'x = π/2', LV, 'l')):
        a = math.radians(ang)
        e = (cx + r * math.cos(a), cy - r * math.sin(a))
        o.append(L(cx, cy, e[0], e[1], c, 3.5, arrow=arr))
        o.append(Tb(e[0] + (10 if ang < 80 else 12), e[1] + (24 if ang == 0 else -6), lab, 14, 'start', c, True))
    o.append(f'<path d="M{cx + 70},{cy} A70,70 0 0 0 {cx + 49.5:.1f},{cy - 49.5:.1f}" style="fill:none;stroke:{MUT};stroke-width:2"/>')
    o.append(T(cx + 80, cy - 24, '45°', 13, 'start', MUT, True))
    o.append(T(cx + 10, cy + 40, 'overlap cos 45° = 0.7071, so K(0, π/4) = 0.7071² = 0.5', 13, 'start'))
    X, Y, cs = 450, 80, 72
    xs = ['0', 'π/4', 'π/2']
    K = [[1, 0.5, 0], [0.5, 1, 0.5], [0, 0.5, 1]]
    o.append(T(X + 1.5 * cs, Y - 26, 'kernel matrix K', 14, bold=True))
    for i in range(3):
        o.append(T(X - 10, Y + i * cs + cs / 2 + 5, xs[i], 13, 'end', MUT, True))
        o.append(T(X + i * cs + cs / 2, Y - 6, xs[i], 13, fill=MUT, bold=True))
        for j in range(3):
            v = K[i][j]
            pct = int(6 + v * 44)
            o.append(f'<rect x="{X + j * cs + 2}" y="{Y + i * cs + 2}" width="{cs - 4}" height="{cs - 4}" rx="6" style="fill:color-mix(in srgb, var(--accent) {pct}%, var(--fig));stroke:var(--line)"/>')
            o.append(T(X + j * cs + cs / 2, Y + i * cs + cs / 2 + 6, f'{v:g}', 16, bold=True))
    o.append(T(X, Y + 3 * cs + 30, 'eigenvalues 1.71, 1.00, 0.29', 14, 'start'))
    o.append(T(X, Y + 3 * cs + 54, 'all positive: a valid SVM kernel', 14, 'start', AC, True))
    return 366, ''.join(o)
FIG[2] = (f2, 'The three data points become unit vectors at 0°, 45° and 90°; the kernel is the squared overlap, so K(0, π/4) = cos² 45° = 0.5, and the 3 × 3 matrix has positive eigenvalues 1.71, 1.00 and 0.29.',
          'Left: three state arrows on a quarter circle at 0, 45 and 90 degrees. Right: a three by three kernel matrix with 1 on the diagonal, 0.5 next to it and 0 in the corners, shaded by value.')


# ---- 6.3 amplitude encoding of a 2x2 patch ----
def f3():
    o = [T(20, 26, 'Amplitude-encode the 2 × 2 patch 3, 4, 0, 5 into 2 qubits', 15, 'start', bold=True)]
    px = [[3, 4], [0, 5]]
    lab = [['|00⟩', '|01⟩'], ['|10⟩', '|11⟩']]
    X0, Y0, cs = 40, 70, 80
    for i in range(2):
        for j in range(2):
            v = px[i][j]
            pct = int(6 + v / 5 * 60)
            o.append(f'<rect x="{X0 + j * cs}" y="{Y0 + i * cs}" width="{cs - 4}" height="{cs - 4}" rx="4" style="fill:color-mix(in srgb, var(--ink) {pct}%, var(--fig));stroke:var(--line2)"/>')
            o.append(Tb(X0 + j * cs + cs / 2 - 2, Y0 + i * cs + cs / 2 + 2, str(v), 16, bold=True))
            o.append(Tb(X0 + j * cs + cs / 2 - 2, Y0 + i * cs + cs - 12, lab[i][j], 12, fill=MUT))
    o.append(T(X0 + cs, Y0 + 2 * cs + 22, 'pixels, row by row', 13, fill=MUT))
    o.append(L(220, 150, 270, 150, MUT, 2, arrow='m')); o.append(Tb(245, 136, '÷ 7.071', 13, fill=MUT, bold=True))
    base = 230
    amps = [0.424, 0.566, 0, 0.707]
    probs = [0.18, 0.32, 0, 0.5]
    bl = ['|00⟩', '|01⟩', '|10⟩', '|11⟩']
    o.append(T(290, 60, 'amplitudes', 14, 'start', AC, True)); o.append(T(510, 60, 'probabilities', 14, 'start', LV, True))
    for k in range(4):
        for (x0, vals, f, c, top) in ((290, amps, ACS, AC, 0.8), (510, probs, LVS, LV, 0.8)):
            bx = x0 + k * 48; h = vals[k] / top * 140
            if h: o.append(R(bx, base - h, 36, h, f, c, 3))
            o.append(T(bx + 18, base - h - 7, f'{vals[k]:.3f}'.rstrip('0').rstrip('.') if vals[k] else '0', 12, bold=True))
            o.append(T(bx + 18, base + 18, bl[k], 12, fill=MUT))
    o.append(L(282, base, 482, base, L2, 1.5)); o.append(L(502, base, 702, base, L2, 1.5))
    o.append(T(20, 296, 'Norm: √(9 + 16 + 0 + 25) = √50 = 7.071. Four values need 2 qubits, since 2² = 4.', 14, 'start'))
    o.append(T(20, 320, 'Reading |11⟩ has probability 0.707² = 0.500; the zero pixel |10⟩ is never read. Check: 0.18 + 0.32 + 0 + 0.50 = 1.', 14, 'start'))
    return 336, ''.join(o)
FIG[3] = (f3, 'Dividing the pixels 3, 4, 0, 5 by the norm 7.071 gives the amplitudes 0.424, 0.566, 0 and 0.707 of a 2-qubit state; squaring them gives read-out probabilities 0.18, 0.32, 0 and 0.50.',
          'A two by two grey patch with values 3, 4, 0, 5, an arrow dividing by 7.071, and two bar charts: amplitudes and probabilities for |00⟩, |01⟩, |10⟩, |11⟩.')


# ---- 6.4 portfolio QUBO ----
def f4():
    vals = [('000', 0), ('100', -2), ('010', -3), ('001', -4), ('110', -5), ('101', -2), ('011', -7), ('111', -5)]
    o = [T(20, 26, 'Cost f(x) = −2x₁ − 3x₂ − 4x₃ + 4x₁x₃ for all 8 portfolios', 15, 'start', bold=True)]
    x0, base, s = 60, 70, 30
    o.append(L(x0 - 10, base, 700, base, L2, 1.5))
    for i, (b, v) in enumerate(vals):
        bx = x0 + i * 80
        best = v == -7
        o.append(R(bx, base, 52, -v * s, LVS if best else ACS, LV if best else AC, 3))
        o.append(T(bx + 26, base - 10, b, 13, fill=LV if best else MUT, bold=True))
        o.append(T(bx + 26, base - v * s + 18, str(v).replace('-', '−'), 14, bold=best))
    o.append(T(x0 + 6 * 80 + 26, base + 7 * s + 40, 'lowest: hold assets 2 and 3', 13, fill=LV, bold=True))
    o.append(T(20, 350, 'Substitute x = (1 − Z)/2:  f = −3.5 + 1.5 Z₂ + 1.0 Z₃ + 1.0 Z₁Z₃', 14, 'start'))
    o.append(T(20, 374, 'At Z = (+1, −1, −1): −3.5 − 1.5 − 1.0 − 1.0 = −7, the same minimum. Keep the constant −3.5.', 14, 'start', LV, True))
    return 390, ''.join(o)
FIG[4] = (f4, 'Scoring all eight holdings shows the lowest cost, −7, at x = (0, 1, 1), holding assets 2 and 3; the Ising form −3.5 + 1.5Z₂ + Z₃ + Z₁Z₃ gives the same −7 at Z = (+1, −1, −1).',
          'Eight downward bars for the bit patterns 000 to 111 with costs 0, −2, −3, −4, −5, −2, −7, −5; the bar for 011 at −7 is the deepest and highlighted.')


# ---- 6.5 security bits before and after ----
def f5():
    o = [T(20, 26, "A hospital's keys against a future quantum computer", 15, 'start', bold=True)]
    x0, s = 150, 1.5
    rows = [('AES-128', 128, 64, 'Grover halves it: too weak for long-lived records', NX),
            ('AES-256', 256, 128, 'Grover halves it: 128 bits left, safe → move records here', LV),
            ('RSA-2048', None, 0, "Shor factors it: 0 bits → replace with post-quantum key exchange", NX)]
    for i, (name, before, after, note, c) in enumerate(rows):
        y = 60 + i * 96
        o.append(T(x0 - 14, y + 30, name, 15, 'end', bold=True))
        if before:
            o.append(R(x0, y + 4, before * s, 22, PANEL, L2, 4)); o.append(T(x0 + before * s + 8, y + 20, f'{before} bits today', 13, 'start', MUT))
            o.append(R(x0, y + 30, after * s, 22, NXS if c == NX else LVS, c, 4)); o.append(T(x0 + after * s + 8, y + 46, f'{after} bits after', 13, 'start', c, True))
        else:
            o.append(T(x0, y + 20, 'secure today (factoring is hard)', 13, 'start', MUT))
            o.append(L(x0, y + 30, x0, y + 52, NX, 4)); o.append(T(x0 + 12, y + 46, '0 bits after', 13, 'start', NX, True))
        o.append(T(x0, y + 74, note, 13, 'start'))
    o.append(T(20, 362, 'Data already copied counts as exposed: re-encrypt it under the new quantum-safe keys.', 14, 'start', MUT))
    return 378, ''.join(o)
FIG[5] = (f5, 'Grover halves symmetric keys, so AES-128 drops to about 64 bits and AES-256 to 128, while Shor takes RSA-2048 to 0; the hospital moves records to AES-256 and swaps RSA for a post-quantum key exchange.',
          'Pairs of bars for AES-128 (128 bits today, 64 after) and AES-256 (256 today, 128 after), and RSA-2048 dropping to 0 bits, each with the action to take.')


TEXT = {
    3: [('Only a few universities teach this. It appears in research prototypes', 'It appears in research prototypes')],
    5: [(' Only a few universities teach this material.', '')],
}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d


def text_fixes(k):
    return TEXT.get(k, [])
