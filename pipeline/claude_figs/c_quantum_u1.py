"""Claude's hand-drawn figures for c-quantum-u1 (Quantum Computing, unit 1: history and linear algebra),
one per chapter, each drawn from that chapter's worked example with its own numbers."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {}
SQ = '1/√2'


# ---- 1.1 memory to store an n-qubit state ----
def f1():
    o = [T(20, 26, 'Memory for one n-qubit state: 2ⁿ amplitudes × 16 bytes', 15, 'start', bold=True)]
    ns = list(range(44, 51))
    x0, x1, y0, y1 = 80, 690, 60, 300
    bw = (x1 - x0) / len(ns)
    fy = lambda v: y1 - v / 20 * (y1 - y0)
    for v in (0, 5, 10, 15, 20):
        o += [L(x0, fy(v), x1, fy(v), LN, 1), T(x0 - 9, fy(v) + 4.5, str(v), 13, 'end', MUT)]
    o.append(L(x0, y1, x1, y1, L2, 1.5))
    for i, n in enumerate(ns):
        v = 16 * 2 ** n / 1e15
        x = x0 + i * bw + 10
        last = n == 50
        o.append(R(x, fy(v), bw - 20, y1 - fy(v), NXS if last else ACS, NX if last else AC, 3))
        o.append(T(x + (bw - 20) / 2, fy(v) - 8, f'{v:.2f}', 13, bold=last))
        o.append(T(x + (bw - 20) / 2, y1 + 20, f'n = {n}', 13, fill=MUT))
        if i:
            o.append(T(x - 10, y1 + 38, '×2', 13, fill=AC, bold=True))
    o.append(T(x0, y0 - 12, 'petabytes (1 PB = 10¹⁵ bytes)', 14, 'start', MUT))
    o.append(T(20, 372, 'n = 50: 2⁵⁰ ≈ 1.126 × 10¹⁵ amplitudes × 16 B ≈ 1.801 × 10¹⁶ B = 18.01 PB.', 14, 'start'))
    o.append(T(20, 396, 'Each extra qubit doubles the memory, so classical simulation runs out fast.', 14, 'start', MUT))
    return 412, ''.join(o)
FIG[1] = (f1, 'Storing every amplitude of an n-qubit state at 16 bytes each doubles the memory with each extra qubit, from 0.28 PB at n = 44 to 18.01 PB at n = 50.',
          'Bar chart of petabytes needed against qubit count from 44 to 50; each bar is twice the one before, ending at 18.01 petabytes for 50 qubits.')


# ---- 1.2 c = i is a quarter turn in each coordinate ----
def plane(cx, cy, r, title, a, b, la, lb):
    o = [T(cx, cy - r - 30, title, 14, bold=True)]
    o.append(L(cx - r - 14, cy, cx + r + 14, cy, L2, 1.5)); o.append(L(cx, cy + r + 14, cx, cy - r - 14, L2, 1.5))
    o.append(T(cx + r + 16, cy + 18, 'Re', 13, 'end', MUT)); o.append(T(cx + 8, cy - r - 8, 'Im', 13, 'start', MUT))
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" style="fill:none;stroke:var(--line);stroke-width:1.2;stroke-dasharray:4 4"/>')
    pa = (cx + r * math.cos(a), cy - r * math.sin(a)); pb = (cx + r * math.cos(b), cy - r * math.sin(b))
    o.append(L(cx, cy, pa[0], pa[1], AC, 3, arrow='n')); o.append(L(cx, cy, pb[0], pb[1], NX, 3, arrow='x'))
    rr = r * 0.45
    s, e = (cx + rr * math.cos(a), cy - rr * math.sin(a)), (cx + rr * math.cos(b), cy - rr * math.sin(b))
    o.append(f'<path d="M{s[0]:.1f},{s[1]:.1f} A{rr:.1f},{rr:.1f} 0 0 0 {e[0]:.1f},{e[1]:.1f}" style="fill:none;stroke:{LV};stroke-width:2.5" marker-end="url(#ar-UID-l)"/>')
    m = (a + b) / 2
    o.append(Tb(cx + (rr + 22) * math.cos(m), cy - (rr + 22) * math.sin(m) + 5, '90°', 13, fill=LV, bold=True))
    o.append(Tb(pa[0] + la[0], pa[1] + la[1], la[2], 14, la[3], AC, True))
    o.append(Tb(pb[0] + lb[0], pb[1] + lb[1], lb[2], 14, lb[3], NX, True))
    return ''.join(o)

def f2():
    o = [T(20, 26, 'v = (1, i) and w = (i, −1): multiply each entry of v by c = i', 15, 'start', bold=True)]
    o.append(plane(190, 170, 90, 'first entry: 1 → i', 0, math.pi / 2, (10, 6, 'v₁ = 1', 'start'), (10, 4, 'w₁ = i', 'start')))
    o.append(plane(520, 170, 90, 'second entry: i → −1', math.pi / 2, math.pi, (10, 4, 'v₂ = i', 'start'), (-2, 28, 'w₂ = −1', 'start')))
    o.append(T(20, 322, 'Both entries turn by the same quarter turn, so w = i·v with |c| = 1.', 14, 'start'))
    o.append(T(20, 346, 'Over C: c = i is allowed, so {v, w} is dependent.', 14, 'start', AC, True))
    o.append(T(20, 370, 'Over R: a·v + b·w = 0 forces a = b = 0, so {v, w} is independent.', 14, 'start', NX, True))
    return 386, ''.join(o)
FIG[2] = (f2, 'Multiplying by c = i turns each entry of v = (1, i) a quarter turn, giving w = (i, −1), so the pair is dependent over C but independent over R.',
          'Two complex planes. In the first, the arrow 1 turns 90 degrees to i; in the second, the arrow i turns 90 degrees to minus 1.')


# ---- 1.3 ket, bra and brackets ----
def col(x, y, vals, stroke, fill, w=92):
    o = [R(x, y, w, 96, fill, stroke)]
    for i, v in enumerate(vals): o.append(T(x + w / 2, y + 36 + i * 36, v, 15, bold=True))
    return ''.join(o)

def f3():
    o = [T(20, 26, 'From the ket |ψ⟩ to the bra ⟨ψ|, then the brackets', 15, 'start', bold=True)]
    o.append(T(76, 62, 'ket |ψ⟩ (column)', 14, fill=AC, bold=True))
    o.append(col(30, 76, ['1/√2', 'i/√2'], AC, ACS))
    o.append(L(130, 124, 230, 124, LV, 2.5, arrow='l'))
    o.append(Tb(180, 112, 'conjugate', 13, fill=LV, bold=True)); o.append(T(180, 146, 'i → −i', 13, fill=LV))
    o.append(T(390, 62, 'bra ⟨ψ| (row)', 14, fill=NX, bold=True))
    o.append(R(240, 98, 300, 52, NXS, NX))
    o.append(T(320, 130, '1/√2', 15, bold=True)); o.append(T(460, 130, '−i/√2', 15, bold=True))
    rows = [('⟨0|ψ⟩', '= 1/√2 ≈ 0.7071', 'picks the first entry'), ('⟨1|ψ⟩', '= i/√2 ≈ 0.7071 i', 'picks the second entry'),
            ('⟨ψ|ψ⟩', '= (1/√2)(1/√2) + (−i/√2)(i/√2) = 1/2 + 1/2 = 1', 'length 1: normalized')]
    for i, (a, b, c) in enumerate(rows):
        y = 196 + i * 50
        o.append(R(20, y - 22, 680, 38, PANEL if i < 2 else LVS, AC if i < 2 else LV, 6))
        o.append(T(36, y + 2, a, 15, 'start', bold=True)); o.append(T(100, y + 2, b, 14, 'start'))
        if i < 2: o.append(T(686, y + 2, c, 13, 'end', MUT))
    o.append(T(20, 352, 'Check: ⟨0|ψ⟩ and ⟨1|ψ⟩ give back the coefficients, as cᵢ = ⟨i|ψ⟩ promises.', 14, 'start', MUT))
    return 368, ''.join(o)
FIG[3] = (f3, 'Conjugating each entry of the ket (1/√2, i/√2) gives the bra (1/√2, −i/√2); pairing the bra with |ψ⟩ gives ⟨ψ|ψ⟩ = 1, and ⟨0|ψ⟩, ⟨1|ψ⟩ return the two coefficients.',
          'A column vector turned into a row vector by conjugation, then three bracket results: 1 over root 2, i over root 2, and 1.')


# ---- 1.4 eigen-directions of A = [[2,1],[1,2]] ----
def f4():
    cx, cy, s = 250, 220, 46
    P_ = lambda x, y: (cx + x * s, cy - y * s)
    o = [T(20, 26, 'A = [[2, 1], [1, 2]] acting on three vectors', 15, 'start', bold=True)]
    for g in range(-3, 4):
        a, b = P_(g, -3.6), P_(g, 3.6); o.append(L(a[0], a[1], b[0], b[1], LN, 1))
    for g in range(-3, 4):
        a, b = P_(-4.4, g), P_(4.4, g); o.append(L(a[0], a[1], b[0], b[1], LN, 1))
    a, b = P_(-4.4, 0), P_(4.4, 0); o.append(L(a[0], a[1], b[0], b[1], L2, 1.5))
    a, b = P_(0, -3.6), P_(0, 3.6); o.append(L(a[0], a[1], b[0], b[1], L2, 1.5))
    for d, lab in ((1, 'y = x'), (-1, 'y = −x')):
        a, b = P_(-3.6, -3.6 * d), P_(3.6, 3.6 * d); o.append(L(a[0], a[1], b[0], b[1], LV, 1.5, '6 5'))
    o.append(Tb(*P_(3.3, 3.75), 'y = x', 13, fill=LV)); o.append(Tb(*P_(3.3, -3.35), 'y = −x', 13, fill=LV))
    def vec(x, y, c, arr, w=3):
        e = P_(x, y); return L(cx, cy, e[0], e[1], c, w, arrow=arr)
    o.append(vec(3, 3, AC, 'n', 4)); o.append(vec(1, 1, NX, 'x', 3))
    o.append(vec(1, -1, NX, 'x', 3.5))
    o.append(vec(2, 1, AC, 'n', 2.5)); o.append(vec(1, 0, NX, 'x', 2.5))
    o.append(Tb(*[v + d for v, d in zip(P_(1, 1), (-46, 2))], '(1, 1)', 13, 'middle', NX, True))
    o.append(Tb(*[v + d for v, d in zip(P_(3, 3), (-40, 4))], '(3, 3)', 13, 'middle', AC, True))
    o.append(Tb(*[v + d for v, d in zip(P_(1, -1), (8, 22))], '(1, −1) stays', 13, 'start', NX, True))
    o.append(Tb(*[v + d for v, d in zip(P_(2, 1), (8, 0))], '(2, 1)', 13, 'start', AC, True))
    o.append(Tb(*[v + d for v, d in zip(P_(1, 0), (4, 20))], '(1, 0)', 13, 'start', NX, True))
    X = 500
    o.append(L(X, 70, X + 30, 70, NX, 3)); o.append(T(X + 38, 75, 'vector v', 14, 'start'))
    o.append(L(X, 96, X + 30, 96, AC, 3)); o.append(T(X + 38, 101, 'A v', 14, 'start'))
    o.append(boxt(X, 130, 200, 66, ['(1, 1) → (3, 3)', 'same line, λ = 3'], ACS, AC, 14, True))
    o.append(boxt(X, 210, 200, 66, ['(1, −1) → (1, −1)', 'unchanged, λ = 1'], LVS, LV, 14, True))
    o.append(boxt(X, 290, 200, 66, ['(1, 0) → (2, 1)', 'turned: not an eigenvector'], PANEL, L2, 14, True))
    return 400, ''.join(o)
FIG[4] = (f4, 'A = [[2, 1], [1, 2]] stretches (1, 1) to (3, 3) and leaves (1, −1) unchanged, so these lie on the eigen-lines with λ = 3 and λ = 1; a vector such as (1, 0) is turned off its line.',
          'A grid with the lines y = x and y = minus x dashed. The vector (1, 1) is stretched to (3, 3), the vector (1, minus 1) stays put, and (1, 0) is turned to (2, 1).')


# ---- 1.5 H as a mirror ----
def f5():
    cx, cy, r = 220, 230, 150
    pt = lambda a, rr=r: (cx + rr * math.cos(a), cy - rr * math.sin(a))
    o = [T(20, 26, 'H = (1/√2)[[1, 1], [1, −1]] is a mirror, so H applied twice is I', 15, 'start', bold=True)]
    o.append(L(cx - 40, cy, cx + r + 30, cy, L2, 1.5)); o.append(L(cx, cy + 40, cx, cy - r - 30, L2, 1.5))
    m = math.pi / 8
    a, b = pt(m + math.pi, 60), pt(m, r + 30); o.append(L(a[0], a[1], b[0], b[1], LV, 2.5, '8 5'))
    o.append(Tb(a[0] - 6, a[1] + 22, 'mirror line', 13, 'end', LV, True))
    p0, pp = pt(0), pt(math.pi / 4)
    o.append(L(cx, cy, p0[0], p0[1], AC, 3.5, arrow='n')); o.append(L(cx, cy, pp[0], pp[1], NX, 3.5, arrow='x'))
    o.append(Tb(p0[0] + 4, p0[1] + 24, '|0⟩ = (1, 0)', 14, 'middle', AC, True))
    o.append(Tb(pp[0] - 6, pp[1] - 12, '|+⟩ = (0.7071, 0.7071)', 14, 'middle', NX, True))
    s1, e1 = pt(0.06, r * 0.72), pt(math.pi / 4 - 0.06, r * 0.72)
    o.append(f'<path d="M{s1[0]:.1f},{s1[1]:.1f} A{r*0.72:.1f},{r*0.72:.1f} 0 0 0 {e1[0]:.1f},{e1[1]:.1f}" style="fill:none;stroke:{MUT};stroke-width:2" marker-end="url(#ar-UID-m)"/>')
    o.append(T(cx + 116, cy - 22, 'H', 14, 'start', MUT, True))
    X = 420
    o.append(boxt(X, 70, 280, 58, ['H|0⟩ = |+⟩', 'first row: 0.7071, 0.7071'], NXS, NX, 14, True))
    o.append(boxt(X, 140, 280, 58, ['H|+⟩ = |0⟩', '0.5 + 0.5 = 1,  0.5 − 0.5 = 0'], ACS, AC, 14, True))
    o.append(boxt(X, 210, 280, 58, ['so H² = I and H⁻¹ = H', 'H† = H as well (real, symmetric)'], PANEL, L2, 14, True))
    o.append(boxt(X, 280, 280, 58, ['eigenvalues', '+1 on the mirror, −1 across it'], LVS, LV, 14, True))
    return 360, ''.join(o)
FIG[5] = (f5, 'H swaps |0⟩ and |+⟩ like a mirror, so doing it twice returns every vector: H² = I, from 0.5 + 0.5 = 1 and 0.5 − 0.5 = 0. Vectors on the mirror keep their sign (eigenvalue +1) and those across it flip (eigenvalue −1).',
          'A plane with |0⟩ along the horizontal axis and |+⟩ at 45 degrees, and a dashed mirror line between them at 22.5 degrees. Boxes list H|0⟩ = |+⟩, H|+⟩ = |0⟩, H squared = I and the eigenvalues plus 1 and minus 1.')


# ---- 1.6 tensor product as a grid of products ----
def f6():
    o = [T(20, 26, '|v⟩ ⊗ |w⟩: multiply every entry of v by every entry of w', 15, 'start', bold=True)]
    gx, gy, cw, chh = 210, 90, 170, 70
    o.append(T(gx + cw, 58, '|w⟩ = 0.7071|0⟩ − 0.7071|1⟩', 14, fill=LV, bold=True))
    o.append(T(gx - 18, gy + chh + 5, '|v⟩', 14, 'end', AC, True))
    for j, w in enumerate(['w₀ = 0.7071', 'w₁ = −0.7071']):
        o.append(T(gx + j * cw + cw / 2, gy - 8, w, 14, fill=LV))
    vals = [[('|00⟩', '0.6 × 0.7071', '0.4243'), ('|01⟩', '0.6 × (−0.7071)', '−0.4243')],
            [('|10⟩', '0.8 × 0.7071', '0.5657'), ('|11⟩', '0.8 × (−0.7071)', '−0.5657')]]
    for i, v in enumerate(['v₀ = 0.6', 'v₁ = 0.8']):
        y = gy + i * chh
        o.append(T(gx - 60, y + chh / 2 + 5, v, 14, 'end', AC))
        for j in range(2):
            b, f, r = vals[i][j]
            x = gx + j * cw
            o.append(R(x + 3, y + 3, cw - 6, chh - 6, ACS if i == 0 else NXS, AC if i == 0 else NX, 6))
            o.append(T(x + 14, y + 26, b, 14, 'start', MUT, True))
            o.append(T(x + cw - 14, y + 26, r, 16, 'end', bold=True))
            o.append(T(x + cw / 2, y + 52, f, 13, fill=MUT))
    o.append(T(20, 266, 'Dimension: 2 × 2 = 4 amplitudes, one for each of |00⟩, |01⟩, |10⟩, |11⟩.', 14, 'start'))
    o.append(T(20, 292, 'Norm: 0.18 + 0.18 + 0.32 + 0.32 = 1, the same as (0.6² + 0.8²)(0.7071² + 0.7071²) = 1 × 1.', 14, 'start', LV, True))
    return 308, ''.join(o)
FIG[6] = (f6, 'Each amplitude of |v⟩ ⊗ |w⟩ is one entry of v times one entry of w, giving 0.4243, −0.4243, 0.5657 and −0.5657; the four squares add to 1.',
          'A two by two grid: rows v0 = 0.6 and v1 = 0.8, columns w0 = 0.7071 and w1 = minus 0.7071, each cell holding the product for |00⟩, |01⟩, |10⟩ and |11⟩.')


# ---- 1.7 e^(iA) puts each eigenvalue on the unit circle ----
def f7():
    cx, cy, r = 220, 200, 120
    o = [T(20, 26, 'e^(iA) for A = diag(0, π): apply e^(iλ) to each eigenvalue', 15, 'start', bold=True)]
    o.append(L(cx - r - 30, cy, cx + r + 30, cy, L2, 1.5)); o.append(L(cx, cy + r + 24, cx, cy - r - 24, L2, 1.5))
    o.append(T(cx + r + 30, cy - 8, 'Re', 13, 'end', MUT)); o.append(T(cx + 8, cy - r - 12, 'Im', 13, 'start', MUT))
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" style="fill:none;stroke:{AC};stroke-width:2"/>')
    o.append(Tb(cx + 70, cy - r - 4, 'unit circle |z| = 1', 13, 'start', AC))
    s = (cx + 40, cy); e = (cx - 40, cy)
    o.append(f'<path d="M{s[0]:.1f},{s[1] - 2:.1f} A40,40 0 0 0 {e[0]:.1f},{e[1] - 2:.1f}" style="fill:none;stroke:{NX};stroke-width:2.5" marker-end="url(#ar-UID-x)"/>')
    o.append(Tb(cx, cy - 50, 'turn by π', 13, fill=NX, bold=True))
    o.append(C(cx + r, cy, 8, LV)); o.append(C(cx - r, cy, 8, NX))
    o.append(Tb(cx + r + 6, cy + 30, 'e^(i·0) = 1', 14, 'middle', LV, True))
    o.append(Tb(cx - r - 6, cy + 30, 'e^(iπ) = −1', 14, 'middle', NX, True))
    X = 420
    o.append(boxt(X, 60, 280, 56, ['λ₁ = 0, eigenvector (1, 0)', 'e^(i·0) = 1'], LVS, LV, 14, True))
    o.append(boxt(X, 128, 280, 56, ['λ₂ = π, eigenvector (0, 1)', 'e^(iπ) = −1'], NXS, NX, 14, True))
    o.append(boxt(X, 196, 280, 56, ['e^(iA) = diag(1, −1)', 'eigenvectors stay the same'], PANEL, AC, 14, True))
    o.append(boxt(X, 264, 280, 56, ['|1| = |−1| = 1', 'on the circle, so unitary'], ACS, AC, 14, True))
    return 344, ''.join(o)
FIG[7] = (f7, 'Applying e^(iλ) to the eigenvalues 0 and π gives 1 and −1, so e^(iA) = diag(1, −1); both values lie on the unit circle, which is why the result is unitary.',
          'A unit circle in the complex plane with points at 1 and minus 1, an arc showing a turn by pi, and boxes for each eigenvalue and the result diag(1, minus 1).')


TEXT = {
    1: [('He also gave the first algorithm with a proven quantum speedup; see Unit 4.',
         'He also gave a first small algorithm, right only half the time, that hinted at a quantum advantage; see Unit 4.'),
        ('He also gave the first algorithm with a proven quantum speedup.',
         'He also gave a first small quantum algorithm; the first clean, proven separation came with the Deutsch–Jozsa algorithm in 1992.')],
    2: [('obeying the usual nine rules: closure;', 'obeying the usual axioms (most textbooks list ten): closure under addition and under scaling;')],
    4: [('Eigenvalues reveal the scaling directions of an operator.',
         'Eigenvectors give the directions an operator does not turn, and eigenvalues give the scale factor along each one.')],
    5: [('is unitary, because its eigenvalues 1 and i both have modulus 1, but', 'is unitary, because S†S = diag(1·1, (−i)·i) = I, but')],
}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d


def text_fixes(k):
    return TEXT.get(k, [])


def drop_sources():
    # university-hosted pages: the books name no universities
    return ['ocw.mit.edu', 'stanford.edu']
