"""Claude's hand-drawn figures for c-quantum-u2 (Quantum Computing, unit 2: qubits, postulates and entanglement),
one per chapter, each drawn from that chapter's worked example with its own numbers."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {}


def qplane(cx, cy, r, extra_axes=False):
    """real plane with |0> to the right and |1> up, quarter circle of unit states"""
    o = [L(cx - 20, cy, cx + r + 30, cy, L2, 1.5), L(cx, cy + 20, cx, cy - r - 30, L2, 1.5)]
    o.append(T(cx + r + 30, cy + 20, '|0⟩', 14, 'end', MUT, True)); o.append(T(cx - 10, cy - r - 18, '|1⟩', 14, 'end', MUT, True))
    o.append(f'<path d="M{cx + r},{cy} A{r},{r} 0 0 0 {cx},{cy - r}" style="fill:none;stroke:var(--line);stroke-width:1.2;stroke-dasharray:4 4"/>')
    return ''.join(o)

def vec(cx, cy, r, ang, c, arr, w=3.5):
    a = math.radians(ang)
    return L(cx, cy, cx + r * math.cos(a), cy - r * math.sin(a), c, w, arrow=arr)

def bars(x, y, vals, labels, colors, h=110, bw=44, gap=26, top=1.0, fmt='{:.2f}'):
    """vertical bars from baseline y upward (negative values go down)"""
    o = [L(x - 8, y, x + len(vals) * (bw + gap) - gap + 8, y, L2, 1.5)]
    for i, (v, lab, c) in enumerate(zip(vals, labels, colors)):
        bx = x + i * (bw + gap); hh = abs(v) / top * h
        soft = {AC: ACS, NX: NXS, LV: LVS}.get(c, PANEL)
        o.append(R(bx, y - hh if v >= 0 else y, bw, hh, soft, c, 3))
        o.append(T(bx + bw / 2, (y - hh - 7) if v >= 0 else (y + hh + 17), fmt.format(v).replace('-', '−'), 13, bold=True))
        o.append(T(bx + bw / 2, y + (20 if v >= 0 else -8), lab, 13, fill=MUT))
    return ''.join(o)


# ---- 2.1 the postulates on one state ----
def f1():
    cx, cy, r = 70, 300, 210
    o = [T(20, 26, '|ψ⟩ = (√3/2)|0⟩ + (1/2)|1⟩: state, gate, measurement', 15, 'start', bold=True)]
    o.append(qplane(cx, cy, r))
    o.append(L(cx, cy, cx + (r + 20) * 0.7071, cy - (r + 20) * 0.7071, LV, 2, '7 5'))
    o.append(Tb(cx + (r + 20) * 0.7071 + 4, cy - (r + 20) * 0.7071 - 8, 'X swaps across this line', 13, 'start', LV))
    o.append(vec(cx, cy, r, 30, AC, 'n')); o.append(vec(cx, cy, r, 60, NX, 'x'))
    o.append(Tb(cx + r * math.cos(math.radians(30)) + 8, cy - r * 0.5 + 4, '|ψ⟩ = (0.866, 0.5)', 14, 'start', AC, True))
    o.append(Tb(cx + r * 0.5 - 8, cy - r * 0.866 - 10, 'X|ψ⟩ = (0.5, 0.866)', 14, 'end', NX, True))
    o.append(T(cx + 110, cy + 40, 'length² = 0.75 + 0.25 = 1', 14, fill=MUT))
    X = 450
    o.append(T(X, 66, 'Measure |ψ⟩: p = amplitude²', 14, 'start', AC, True))
    o.append(bars(X + 20, 196, [0.75, 0.25], ['p(0)', 'p(1)'], [AC, AC], 100))
    o.append(T(X, 246, 'Measure X|ψ⟩', 14, 'start', NX, True))
    o.append(bars(X + 20, 372, [0.25, 0.75], ['p(0)', 'p(1)'], [NX, NX], 100))
    return 400, ''.join(o)
FIG[1] = (f1, 'The state (√3/2, 1/2) is a unit vector; measuring it gives 0 with probability 0.75 and 1 with 0.25. The gate X swaps the amplitudes to (0.5, 0.866), which swaps the probabilities.',
          'A quarter circle with the state vector at 30 degrees and X of the state at 60 degrees, mirrored across the 45 degree line, beside two pairs of probability bars: 0.75 and 0.25, then 0.25 and 0.75.')


# ---- 2.2 bit versus qubit ----
def f2():
    o = [T(20, 26, 'A bit holds one value; a qubit holds two amplitudes until it is measured', 15, 'start', bold=True)]
    o.append(boxt(20, 60, 170, 70, ['classical bit', 'either 0 or 1'], PANEL, L2, 14, True))
    o.append(T(105, 156, 'reading it gives that value back', 13, fill=MUT))
    o.append(boxt(220, 150, 210, 96, ['qubit |ψ⟩', 'α = 1/√2 on |0⟩', 'β = i/√2 on |1⟩'], ACS, AC, 14, True))
    o.append(boxt(250, 60, 150, 50, ['measure'], PANEL, AC, 14, True))
    o.append(L(325, 148, 325, 114, AC, 2, arrow='n'))
    o.append(L(400, 78, 512, 60, NX, 2.5, arrow='x')); o.append(L(400, 94, 512, 148, LV, 2.5, arrow='l'))
    o.append(Tb(456, 56, '|1/√2|² = 0.5', 13, fill=NX, bold=True)); o.append(Tb(452, 132, '|i/√2|² = 0.5', 13, fill=LV, bold=True))
    o.append(boxt(516, 34, 186, 58, ['outcome 0', 'state becomes |0⟩'], NXS, NX, 14, True))
    o.append(boxt(516, 122, 186, 58, ['outcome 1', 'state becomes |1⟩'], LVS, LV, 14, True))
    o.append(T(20, 286, 'Check: |α|² + |β|² = 0.5 + 0.5 = 1. The factor i changes no probability here,', 14, 'start'))
    o.append(T(20, 310, 'and after outcome 0 it is gone: only |0⟩ is left.', 14, 'start'))
    return 326, ''.join(o)
FIG[2] = (f2, 'A bit is one of two values; the qubit with α = 1/√2 and β = i/√2 gives 0 or 1 with probability 0.5 each when measured, and outcome 0 leaves the state |0⟩.',
          'A classical bit box beside a qubit box with amplitudes 1 over root 2 and i over root 2, feeding a measurement that branches to outcome 0 or outcome 1, each with probability 0.5.')


# ---- 2.3 H then Z: phase changes amplitudes, not probabilities ----
def f3():
    o = [T(20, 26, 'Start in |0⟩, apply H, then Z: amplitudes (top) and probabilities (bottom)', 15, 'start', bold=True)]
    st = [('|0⟩', [1, 0], [1, 0]), ('H|0⟩ = |+⟩', [0.7071, 0.7071], [0.5, 0.5]), ('Z|+⟩ = |−⟩', [0.7071, -0.7071], [0.5, 0.5])]
    cols = [L2, AC, NX]
    for i, (name, amp, pr) in enumerate(st):
        x = 40 + i * 230
        o.append(T(x + 60, 60, name, 15, fill=cols[i] if i else INK, bold=True))
        o.append(bars(x + 14, 160, amp, ['|0⟩', '|1⟩'], [cols[i]] * 2, 70, 40, 24, fmt='{:.4g}'))
        o.append(bars(x + 14, 340, pr, ['p(0)', 'p(1)'], [cols[i]] * 2, 70, 40, 24, fmt='{:.2g}'))
        if i < 2:
            o.append(L(x + 150, 150, x + 210, 150, MUT, 2, arrow='m'))
            o.append(Tb(x + 180, 140, ['H', 'Z'][i], 14, fill=MUT, bold=True))
    o.append(T(20, 400, 'Z flips the sign of the |1⟩ amplitude: 0.7071 → −0.7071, but (−0.7071)² is still 0.5.', 14, 'start'))
    return 416, ''.join(o)
FIG[3] = (f3, 'H turns |0⟩ into amplitudes 0.7071 and 0.7071, so p(0) = p(1) = 0.5; Z then flips the second amplitude to −0.7071, which leaves both probabilities at 0.5.',
          'Three stages, |0⟩, |+⟩ and |−⟩, each with amplitude bars above and probability bars below; the last stage has a negative bar for |1⟩ but the same probability bars.')


# ---- 2.4 Bloch sphere side view ----
def f4():
    cx, cy, r = 220, 220, 160
    o = [T(20, 26, 'Bloch sphere seen from the side (the x–z circle)', 15, 'start', bold=True)]
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" style="fill:none;stroke:{L2};stroke-width:2"/>')
    o.append(L(cx - r - 10, cy, cx + r + 10, cy, LN, 1.2)); o.append(L(cx, cy - r - 10, cx, cy + r + 10, LN, 1.2))
    for (x, y, lab, an, dx, dy) in ((0, 1, '|0⟩', 'middle', 0, -12), (0, -1, '|1⟩', 'middle', 0, 26), (1, 0, '|+⟩', 'start', 10, 5), (-1, 0, '|−⟩', 'end', -10, 5)):
        o.append(C(cx + x * r, cy - y * r, 5, L2)); o.append(T(cx + x * r + dx, cy - y * r + dy, lab, 14, an, MUT, True))
    px, pz = 0.866, 0.5
    P_ = (cx + px * r, cy - pz * r)
    o.append(L(P_[0], P_[1], cx, P_[1], LV, 2, '6 5'))
    o.append(L(cx, cy, P_[0], P_[1], AC, 3.5, arrow='n'))
    o.append(C(P_[0], P_[1], 6, AC))
    o.append(Tb(P_[0] - 8, P_[1] - 22, '|ψ⟩: (0.866, 0, 0.5)', 14, 'end', AC, True))
    rr = 60
    o.append(f'<path d="M{cx},{cy - rr} A{rr},{rr} 0 0 1 {cx + rr * math.sin(math.pi / 3):.1f},{cy - rr * math.cos(math.pi / 3):.1f}" style="fill:none;stroke:{NX};stroke-width:2.5"/>')
    o.append(T(cx + 14, cy - 26, 'θ', 15, 'start', NX, True))
    o.append(Tb(cx - 10, P_[1] + 5, 'z = 0.5', 13, 'end', LV, True))
    X = 440
    o.append(boxt(X, 70, 260, 64, ['cos(θ/2) = √3/2', 'so θ/2 = π/6, θ = π/3'], NXS, NX, 14, True))
    o.append(boxt(X, 148, 260, 64, ['amplitude of |1⟩ = +1/2', 'real and positive, so φ = 0'], PANEL, L2, 14, True))
    o.append(boxt(X, 226, 260, 64, ['x = sin θ = 0.866', 'z = cos θ = 0.5'], ACS, AC, 14, True))
    o.append(boxt(X, 304, 260, 64, ['p(0) = (1 + z)/2', '= (1 + 0.5)/2 = 0.75'], LVS, LV, 14, True))
    return 414, ''.join(o)
FIG[4] = (f4, 'The state (√3/2)|0⟩ + (1/2)|1⟩ sits at θ = π/3 from |0⟩ with φ = 0, the point (0.866, 0, 0.5); its height z = 0.5 gives p(0) = (1 + 0.5)/2 = 0.75.',
          'A circle with |0⟩ at the top, |1⟩ at the bottom, |+⟩ right and |−⟩ left; an arrow at 60 degrees from the top marks the state, with its height 0.5 dashed across.')


# ---- 2.5 measuring in the |+>, |-> basis ----
def f5():
    cx, cy, r = 250, 230, 170
    o = [T(20, 26, 'Measure |ψ⟩ = (√3/2, 1/2) along |+⟩ and |−⟩ instead of |0⟩ and |1⟩', 15, 'start', bold=True)]
    o.append(L(cx - r - 10, cy, cx + r + 10, cy, LN, 1.2)); o.append(L(cx, cy - r - 10, cx, cy + r - 40, LN, 1.2))
    o.append(T(cx + r + 10, cy + 20, '|0⟩', 13, 'end', MUT)); o.append(T(cx - 8, cy - r - 2, '|1⟩', 13, 'end', MUT))
    for ang, lab, c, arr in ((45, '|+⟩', NX, 'x'), (-45, '|−⟩', LV, 'l')):
        a = math.radians(ang)
        o.append(L(cx, cy, cx + (r + 10) * math.cos(a), cy - (r + 10) * math.sin(a), c, 2, '7 5'))
        o.append(T(cx + (r + 22) * math.cos(a), cy - (r + 22) * math.sin(a) + 5, lab, 15, 'middle', c, True))
    a = math.radians(30)
    P_ = (cx + r * math.cos(a), cy - r * math.sin(a))
    o.append(L(cx, cy, P_[0], P_[1], AC, 3.5, arrow='n'))
    o.append(Tb(P_[0] + 10, P_[1] + 6, '|ψ⟩', 15, 'start', AC, True))
    for ang, comp, c in ((45, 0.966, NX), (-45, 0.259, LV)):
        b = math.radians(ang)
        F = (cx + r * comp * math.cos(b), cy - r * comp * math.sin(b))
        o.append(L(P_[0], P_[1], F[0], F[1], c, 1.8, '3 4'))
        o.append(L(cx, cy, F[0], F[1], c, 6))
        o.append(C(F[0], F[1], 5, c))
    o.append(Tb(cx + 70, cy - 104, '0.966', 14, 'end', NX, True))
    o.append(Tb(cx + 46, cy + 32, '0.259', 14, 'start', LV, True))
    X = 470
    o.append(boxt(X, 70, 230, 76, ['⟨+|ψ⟩ = (√3 + 1)/(2√2)', '≈ 0.966', 'p(+) = 0.966² ≈ 0.933'], NXS, NX, 14))
    o.append(boxt(X, 160, 230, 76, ['⟨−|ψ⟩ = (√3 − 1)/(2√2)', '≈ 0.259', 'p(−) = 0.259² ≈ 0.067'], LVS, LV, 14))
    o.append(boxt(X, 250, 230, 56, ['check: 0.933 + 0.067 = 1'], PANEL, L2, 14))
    o.append(boxt(X, 320, 230, 56, ['after the outcome the state', 'is |+⟩ or |−⟩'], PANEL, AC, 14))
    return 400, ''.join(o)
FIG[5] = (f5, 'The shadow of |ψ⟩ on the |+⟩ line is 0.966 and on the |−⟩ line is 0.259; squaring gives p(+) ≈ 0.933 and p(−) ≈ 0.067, and the state left behind is |+⟩ or |−⟩.',
          'Axes |0⟩ and |1⟩ with dashed diagonal axes |+⟩ and |−⟩; the state at 30 degrees drops dotted projections onto each diagonal, of length 0.966 and 0.259.')


# ---- 2.6 partial trace of a Bell pair ----
def f6():
    o = [T(20, 26, 'ρ for |Φ+⟩ = (|00⟩ + |11⟩)/√2, then trace out B', 15, 'start', bold=True)]
    M = [[0.5, 0, 0, 0.5], [0, 0, 0, 0], [0, 0, 0, 0], [0.5, 0, 0, 0.5]]
    gx, gy, cs = 110, 80, 58
    labs = ['00', '01', '10', '11']
    for j, l in enumerate(labs):
        o.append(T(gx + j * cs + cs / 2, gy - 10, l, 13, fill=MUT))
        o.append(T(gx - 12, gy + j * cs + cs / 2 + 5, l, 13, 'end', MUT))
    blocks = {(0, 0): (ACS, AC), (1, 1): (NXS, NX), (0, 1): (PANEL, L2), (1, 0): (PANEL, L2)}
    for (bi, bj), (f, s) in blocks.items():
        o.append(R(gx + bj * 2 * cs + 2, gy + bi * 2 * cs + 2, 2 * cs - 4, 2 * cs - 4, f, s, 8))
    for i in range(4):
        for j in range(4):
            v = M[i][j]
            on_diag_block = (i // 2 == j // 2)
            o.append(T(gx + j * cs + cs / 2, gy + i * cs + cs / 2 + 6, '0.5' if v else '0', 15, bold=bool(v), fill=INK if v else MUT))
            if on_diag_block and i % 2 == j % 2:
                o.append(f'<circle cx="{gx + j * cs + cs / 2}" cy="{gy + i * cs + cs / 2}" r="19" style="fill:none;stroke:{LV};stroke-width:2;stroke-dasharray:4 3"/>')
    o.append(T(gx + 2 * cs, gy + 4 * cs + 28, 'rows and columns |AB⟩; each 2 × 2 block is one A pair', 13, fill=MUT))
    X = 480
    o.append(T(X, 84, 'trace of each block', 14, 'start', LV, True))
    o.append(T(X, 104, '(add its dashed diagonal)', 13, 'start', MUT))
    o.append(L(gx + 4 * cs + 10, gy + 2 * cs, X - 12, 190, LV, 2, arrow='l'))
    rx, ry, rc = X + 20, 140, 70
    o.append(R(rx, ry, 2 * rc, 2 * rc, PANEL, LV, 8))
    for (i, j, v, f, s) in ((0, 0, '0.5', ACS, AC), (0, 1, '0', None, None), (1, 0, '0', None, None), (1, 1, '0.5', NXS, NX)):
        if f: o.append(R(rx + j * rc + 6, ry + i * rc + 6, rc - 12, rc - 12, f, s, 6))
        o.append(T(rx + j * rc + rc / 2, ry + i * rc + rc / 2 + 6, v, 16, bold=(v != '0')))
    o.append(T(rx + rc, ry - 12, 'ρ_A = I/2', 15, bold=True))
    o.append(T(X, 320, 'trace 0.5 + 0.5 = 1', 14, 'start'))
    o.append(T(X, 344, 'purity 0.5² + 0.5² = 0.5 < 1', 14, 'start', LV, True))
    o.append(T(X, 368, 'so A alone is mixed', 14, 'start', LV, True))
    return 400, ''.join(o)
FIG[6] = (f6, 'The Bell pair has four entries of 0.5 in its 4 × 4 density matrix. Adding the diagonal of each 2 × 2 block gives ρ_A = diag(0.5, 0.5) = I/2, with purity 0.5, so qubit A on its own is mixed.',
          'A four by four grid of entries with 0.5 in the four corners, divided into four two by two blocks; the trace of each block gives the two by two matrix with 0.5 on the diagonal.')


# ---- 2.7 Bell state cannot be a product ----
def f7():
    o = [T(20, 26, 'Try |Φ+⟩ = (a|0⟩ + b|1⟩) ⊗ (c|0⟩ + d|1⟩)', 15, 'start', bold=True)]
    gx, gy, cw, chh = 120, 70, 130, 64
    o.append(T(gx + cw / 2, gy - 8, 'c', 14, fill=LV, bold=True)); o.append(T(gx + 1.5 * cw, gy - 8, 'd', 14, fill=LV, bold=True))
    o.append(T(gx - 14, gy + chh / 2 + 5, 'a', 14, 'end', AC, True)); o.append(T(gx - 14, gy + 1.5 * chh + 5, 'b', 14, 'end', AC, True))
    cells = [[('ac', '1/√2', ACS, AC), ('ad', '0', NXS, NX)], [('bc', '0', NXS, NX), ('bd', '1/√2', ACS, AC)]]
    for i in range(2):
        for j in range(2):
            p, v, f, s = cells[i][j]
            x, y = gx + j * cw, gy + i * chh
            o.append(R(x + 3, y + 3, cw - 6, chh - 6, f, s, 6))
            o.append(T(x + cw / 2, y + chh / 2 + 6, f'{p} = {v}', 15, bold=True))
    X = 420
    o.append(T(X, 70, 'ad = 0 needs a = 0 or d = 0', 14, 'start', NX, True))
    o.append(boxt(X, 84, 136, 56, ['a = 0', 'then ac = 0 ✗'], PANEL, NX, 14, True))
    o.append(boxt(X + 148, 84, 136, 56, ['d = 0', 'then bd = 0 ✗'], PANEL, NX, 14, True))
    o.append(T(X, 168, 'No a, b, c, d work: entangled.', 14, 'start', AC, True))
    o.append(T(20, 236, 'Alice measures her qubit in the 0/1 basis:', 15, 'start', bold=True))
    outs = [('00', '0.5', AC, ACS), ('01', '0', L2, PANEL), ('10', '0', L2, PANEL), ('11', '0.5', AC, ACS)]
    for i, (o_, p, s, f) in enumerate(outs):
        x = 40 + i * 168
        o.append(boxt(x, 252, 148, 56, [f'outcome {o_}', f'p = {p}'], f, s, 14, True))
    o.append(T(20, 336, 'Alice gets 0 → Bob has |0⟩; Alice gets 1 → Bob has |1⟩. Each happens half the time.', 14, 'start'))
    return 352, ''.join(o)
FIG[7] = (f7, 'A product would need ac = bd = 1/√2 and ad = bc = 0, which no numbers satisfy, so |Φ+⟩ is entangled; measuring gives 00 or 11 with probability 0.5 each, never 01 or 10.',
          'A two by two grid of products ac, ad, bc, bd with required values 1 over root 2, 0, 0, 1 over root 2, the two failing cases a = 0 and d = 0, and four outcome boxes 00, 01, 10, 11 with probabilities 0.5, 0, 0, 0.5.')


# ---- 2.8 CHSH angles ----
def f8():
    cx, cy, r = 200, 210, 140
    o = [T(20, 26, 'Measurement directions for x = 0, y = 0 (angles in the x–z plane)', 15, 'start', bold=True)]
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" style="fill:none;stroke:var(--line);stroke-width:1.5;stroke-dasharray:4 4"/>')
    dirs = [(90, 'A₀ = Z', AC, 'n', 3.5), (0, 'A₁ = X', AC, 'n', 2), (45, 'B₀ = (Z + X)/√2', NX, 'x', 3.5), (-45, 'B₁ = (Z − X)/√2', NX, 'x', 2)]
    for ang, lab, c, arr, w in dirs:
        a = math.radians(ang)
        e = (cx + r * math.cos(a), cy - r * math.sin(a))
        o.append(L(cx, cy, e[0], e[1], c, w, '7 4' if w < 3 else None, arr))
        an = 'start' if math.cos(a) > 0.1 else ('middle' if abs(math.cos(a)) <= 0.1 else 'end')
        o.append(Tb(e[0] + 10 * math.cos(a) + (8 if an == 'start' else 0), e[1] - 14 * math.sin(a) + 5 - (6 if ang == 90 else 0), lab, 14, an, c, w > 3))
    rr = 56
    o.append(f'<path d="M{cx},{cy - rr} A{rr},{rr} 0 0 1 {cx + rr * 0.7071:.1f},{cy - rr * 0.7071:.1f}" style="fill:none;stroke:{LV};stroke-width:3"/>')
    o.append(Tb(cx + 26, cy - rr - 8, '45°', 14, 'start', LV, True))
    X = 420
    o.append(boxt(X, 60, 280, 64, ['E(0,0) = cos 45°', '= (1 + 0)/√2 ≈ 0.7071'], LVS, LV, 14, True))
    o.append(boxt(X, 136, 280, 64, ['P(a = b) = (1 + E)/2', '= (2 + √2)/4 ≈ 0.8536'], NXS, NX, 14, True))
    y0 = 270
    o.append(T(X, y0 - 12, 'chance of winning the game', 14, 'start', MUT))
    s = 250
    o.append(R(X, y0, 0.75 * s, 30, PANEL, L2, 4)); o.append(T(X + 0.75 * s + 8, y0 + 21, '0.75 best local', 14, 'start'))
    o.append(R(X, y0 + 44, 0.8536 * s, 30, ACS, AC, 4)); o.append(T(X + 0.8536 * s - 8, y0 + 65, '0.8536', 14, 'end', AC, True))
    o.append(T(X, y0 + 100, 'quantum, with |Φ+⟩', 14, 'start', AC))
    return 386, ''.join(o)
FIG[8] = (f8, 'Alice’s Z axis and Bob’s B₀ axis are 45° apart, so E(0,0) = cos 45° ≈ 0.7071 and P(a = b) = (2 + √2)/4 ≈ 0.8536, above the best local winning chance of 0.75.',
          'A circle with four measurement arrows: Z up, X right, and Bob’s two axes at plus and minus 45 degrees, beside boxes for E = 0.7071 and P = 0.8536 and two bars comparing 0.75 with 0.8536.')


# ---- 2.9 Stern-Gerlach in sequence ----
def f9():
    o = [T(20, 26, 'Silver atoms through a z magnet, then an x magnet', 15, 'start', bold=True)]
    o.append(boxt(20, 130, 110, 60, ['oven', '1 beam'], PANEL, L2, 14, True))
    o.append(L(132, 160, 196, 160, AC, 3, arrow='n'))
    o.append(boxt(200, 120, 120, 80, ['z magnet', 'measures S_z'], ACS, AC, 14, True))
    o.append(L(322, 145, 410, 100, AC, 3, arrow='n')); o.append(L(322, 175, 410, 220, AC, 3, arrow='n'))
    o.append(Tb(360, 106, '½ up', 14, fill=AC, bold=True)); o.append(Tb(360, 222, '½ down', 14, fill=AC, bold=True))
    o.append(R(414, 204, 16, 34, MUT, MUT, 2)); o.append(T(422, 258, 'blocked', 13, fill=MUT))
    o.append(L(414, 98, 464, 98, AC, 3, arrow='n'))
    o.append(boxt(468, 60, 120, 80, ['x magnet', 'measures S_x'], NXS, NX, 14, True))
    o.append(L(590, 85, 670, 50, NX, 3, arrow='x')); o.append(L(590, 115, 670, 150, NX, 3, arrow='x'))
    o.append(Tb(676, 46, '¼', 16, 'start', NX, True)); o.append(Tb(676, 158, '¼', 16, 'start', NX, True))
    o.append(T(630, 196, '½ × ½ = ¼ each', 13, fill=NX))
    o.append(T(20, 300, 'Why: the up-z beam is |↑z⟩ = (|↑x⟩ + |↓x⟩)/√2, so each x outcome has probability ½.', 14, 'start'))
    o.append(T(20, 324, 'Measuring x wipes out the earlier z answer: a third z magnet would split these beams again.', 14, 'start', MUT))
    o.append(T(20, 348, 'Uncertainty: ΔSₓ ΔS_y ≥ (ħ/2)|⟨S_z⟩|; with ΔSₓ = ħ/2 and ⟨S_z⟩ = ħ/2, ΔS_y ≥ ħ/2.', 14, 'start'))
    return 364, ''.join(o)
FIG[9] = (f9, 'The z magnet sends half the atoms up and half down; blocking the lower beam and sending the upper one through an x magnet splits it again, so each x output carries ¼ of the original beam.',
          'An oven beam enters a z magnet and splits into two halves; the lower half is blocked and the upper half enters an x magnet, which splits it into two quarter beams.')


TEXT = {
    5: [('Only a few universities teach POVM details in this unit; most exam questions use projective measurements.',
         'POVM details are rarely examined in this unit; most exam questions use projective measurements.')],
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
