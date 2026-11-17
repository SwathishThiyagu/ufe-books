"""Claude's hand-drawn figures for c-quantum-u3 (Quantum Computing, unit 3: quantum gates and circuits),
one per chapter, each drawn from that chapter's worked example with its own numbers."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {}


# ---- circuit helpers ----
def wire(y, x0, x1, lab=None):
    o = [L(x0, y, x1, y, L2, 2)]
    if lab: o.append(T(x0 - 10, y + 5, lab, 14, 'end', INK, True))
    return ''.join(o)

def cwire(y, x0, x1):
    return L(x0, y - 2.5, x1, y - 2.5, L2, 1.5) + L(x0, y + 2.5, x1, y + 2.5, L2, 1.5)

def gate(x, y, name, fill=ACS, stroke=AC, w=40, size=16):
    return R(x - w / 2, y - 20, w, 40, fill, stroke, 6) + T(x, y + 6, name, size, bold=True)

def cnot(x, yc, yt, c=AC):
    r = 13
    o = [L(x, yc, x, yt + (r if yt > yc else -r), c, 2)]
    o.append(f'<circle cx="{x}" cy="{yc}" r="6" style="fill:{c}"/>')
    o.append(f'<circle cx="{x}" cy="{yt}" r="{r}" style="fill:var(--fig);stroke:{c};stroke-width:2"/>')
    o.append(L(x - r, yt, x + r, yt, c, 2)); o.append(L(x, yt - r, x, yt + r, c, 2))
    return ''.join(o)

def meter(x, y, c=INK):
    o = [R(x - 20, y - 18, 40, 36, PANEL, c, 5)]
    o.append(f'<path d="M{x - 12},{y + 8} A13,13 0 0 1 {x + 12},{y + 8}" style="fill:none;stroke:{c};stroke-width:1.8"/>')
    o.append(L(x, y + 8, x + 9, y - 9, c, 1.8))
    return ''.join(o)


# ---- 3.1 H, Z, H on |0> ----
def f1():
    o = [T(20, 26, 'One qubit through H, Z, H: the state after each gate', 15, 'start', bold=True)]
    y = 90
    o.append(wire(y, 70, 690, '|0⟩'))
    xs = [190, 370, 550]
    for x, g in zip(xs, 'HZH'): o.append(gate(x, y, g, NXS if g == 'Z' else ACS, NX if g == 'Z' else AC))
    st = [(110, '(1, 0)', '|0⟩'), (280, '(0.7071, 0.7071)', '|+⟩'), (460, '(0.7071, −0.7071)', '|−⟩'), (630, '(0, 1)', '|1⟩')]
    for x, v, n in st:
        o.append(T(x, y - 30, n, 15, fill=AC, bold=True)); o.append(T(x, y + 42, v, 13))
    # amplitude bars under each state
    amps = [(1, 0), (0.7071, 0.7071), (0.7071, -0.7071), (0, 1)]
    base = 220
    for (x, _, _), (a, b) in zip(st, amps):
        for j, v in enumerate((a, b)):
            bx = x - 30 + j * 34; h = abs(v) * 60
            c, f = (NX, NXS) if v < 0 else (AC, ACS)
            if h: o.append(R(bx, base - h if v > 0 else base, 26, h, f, c, 3))
            o.append(T(bx + 13, base + 62, '|0⟩' if j == 0 else '|1⟩', 13, fill=MUT))
        o.append(L(x - 38, base, x + 38, base, L2, 1.5))
    o.append(T(20, 152, 'amplitudes', 13, 'start', MUT))
    o.append(T(20, 336, 'Z only flips the sign of the |1⟩ amplitude; the last H turns that sign into a different answer:', 14, 'start'))
    o.append(T(20, 360, 'first entry 1/2 − 1/2 = 0, second entry 1/2 + 1/2 = 1, so P(0) = 0 and P(1) = 1.', 14, 'start', AC, True))
    return 376, ''.join(o)
FIG[1] = (f1, 'H turns |0⟩ into (0.7071, 0.7071), Z flips the sign of the second amplitude, and the final H gives (0, 1) = |1⟩, so the qubit reads 1 with certainty.',
          'A single wire with gates H, Z and H; above and below each stage the state and its two amplitude bars, ending in |1⟩.')


# ---- 3.2 three CNOTs swap ----
def f2():
    o = [T(20, 26, 'Three CNOTs swap two qubits: follow the input |01⟩', 15, 'start', bold=True)]
    y1, y2 = 110, 190
    o.append(wire(y1, 120, 680, 'q1')); o.append(wire(y2, 120, 680, 'q2'))
    gx = [250, 400, 550]
    o.append(cnot(gx[0], y1, y2)); o.append(cnot(gx[1], y2, y1, NX)); o.append(cnot(gx[2], y1, y2))
    labs = ['CNOT(1→2)', 'CNOT(2→1)', 'CNOT(1→2)']
    for x, l, c in zip(gx, labs, (AC, NX, AC)): o.append(T(x, 72, l, 13, fill=c, bold=True))
    vals = [(160, 0, 1), (325, 0, 1), (475, 1, 1), (630, 1, 0)]
    for x, a, b in vals:
        o.append(Tb(x, y1 - 10, str(a), 16, bold=True)); o.append(Tb(x, y2 - 10, str(b), 16, bold=True))
    notes = [(325, 'q1 = 0: no flip'), (475, 'q2 = 1: flip q1'), (630, 'q1 = 1: flip q2')]
    for x, n in notes: o.append(T(x, 236, n, 13, fill=MUT))
    o.append(boxt(40, 262, 300, 50, ['in: (q1, q2) = (0, 1) = |01⟩'], PANEL, L2, 14))
    o.append(L(344, 287, 376, 287, AC, 2, arrow='n'))
    o.append(boxt(380, 262, 300, 50, ['out: (q1, q2) = (1, 0) = |10⟩'], ACS, AC, 14, True))
    o.append(T(20, 344, 'On any bits (a, b): (a, a⊕b) → (b, a⊕b) → (b, a). The bits change places.', 14, 'start'))
    return 360, ''.join(o)
FIG[2] = (f2, 'Following |01⟩ through CNOT(1→2), CNOT(2→1), CNOT(1→2), the bits go (0, 1) → (0, 1) → (1, 1) → (1, 0), so the three gates swap the qubits.',
          'Two wires with three CNOT gates, the middle one pointing the other way; the bit values 0 and 1 are written on each wire between gates, ending as 1 and 0.')


# ---- 3.3 H TTTT H = X ----
def f3():
    o = [T(20, 26, 'The six gates H, T, T, T, T, H build X exactly', 15, 'start', bold=True)]
    y = 100
    o.append(wire(y, 60, 690, '|ψ⟩'))
    xs = [110, 210, 290, 370, 450, 560]
    for x, g in zip(xs, ['H', 'T', 'T', 'T', 'T', 'H']):
        o.append(gate(x, y, g, NXS if g == 'T' else ACS, NX if g == 'T' else AC))
    o.append(brace(185, 475, 140, NX))
    o.append(T(330, 166, 'T⁴ = Z', 15, fill=NX, bold=True))
    o.append(brace(85, 585, 190, AC))
    o.append(T(335, 216, 'H Z H = X', 15, fill=AC, bold=True))
    o.append(boxt(30, 250, 200, 76, ['T = diag(1, e^(iπ/4))', 'T² = diag(1, i) = S'], NXS, NX, 14))
    o.append(boxt(250, 250, 200, 76, ['T⁴ = diag(1, i²)', '= diag(1, −1) = Z'], NXS, NX, 14))
    o.append(boxt(470, 250, 220, 76, ['H Z H = [[0, 1], [1, 0]]', '= X, global phase +1'], ACS, AC, 14, True))
    o.append(L(232, 288, 246, 288, NX, 2, arrow='x')); o.append(L(452, 288, 466, 288, AC, 2, arrow='n'))
    o.append(T(20, 356, 'No approximation: a finite product of H and T gives X exactly.', 14, 'start', MUT))
    return 372, ''.join(o)
FIG[3] = (f3, 'Four T gates in a row multiply to Z, because T² = S = diag(1, i) and S² = diag(1, −1); with H on each side the six gates give H Z H = X exactly.',
          'A single wire with gates H, T, T, T, T, H; a bracket under the four T gates reads T to the fourth equals Z, and a wider bracket reads H Z H equals X.')


# ---- 3.4 Bell circuit ----
def f4():
    o = [T(20, 26, 'H on q0, then CNOT(q0 → q1), then measure', 15, 'start', bold=True)]
    y0, y1 = 80, 150
    o.append(wire(y0, 70, 560, 'q0: |0⟩')); o.append(wire(y1, 70, 560, 'q1: |0⟩'))
    o.append(gate(200, y0, 'H')); o.append(cnot(340, y0, y1))
    o.append(meter(500, y0)); o.append(meter(500, y1))
    o.append(T(600, y0 + 5, 'bit 0', 13, 'start', MUT)); o.append(T(600, y1 + 5, 'bit 1', 13, 'start', MUT))
    for x, l in ((130, 'start'), (270, 'after H'), (420, 'after CNOT')):
        o.append(L(x, 50, x, 180, LV, 1.5, '4 4')); o.append(T(x, 198, l, 13, fill=LV, bold=True))
    # amplitude table
    rows = ['|00⟩', '|01⟩', '|10⟩', '|11⟩']
    data = [['1', '0', '0', '0'], ['0.7071', '0', '0.7071', '0'], ['0.7071', '0', '0', '0.7071'], ['0.5', '0', '0', '0.5']]
    heads = ['start', 'after H', 'after CNOT', 'probability']
    tx, ty, cw, rh = 140, 236, 135, 30
    for j, h in enumerate(heads): o.append(T(tx + j * cw + cw / 2, ty, h, 13, fill=LV if j < 3 else NX, bold=True))
    for i, r in enumerate(rows):
        y = ty + 14 + i * rh
        o.append(T(tx - 14, y + 20, r, 14, 'end', bold=True))
        for j in range(4):
            v = data[j][i]
            nz = v != '0'
            if nz: o.append(R(tx + j * cw + 18, y + 2, cw - 36, rh - 4, NXS if j == 3 else ACS, NX if j == 3 else AC, 5))
            o.append(T(tx + j * cw + cw / 2, y + 20, v, 14, bold=nz, fill=INK if nz else MUT))
    o.append(T(20, 400, 'The bits always agree: 00 or 11, each half the time. This is the Bell state |Φ⁺⟩.', 14, 'start'))
    return 416, ''.join(o)
FIG[4] = (f4, 'H puts amplitude 0.7071 on |00⟩ and |10⟩; CNOT moves the |10⟩ amplitude to |11⟩, so measuring gives 00 or 11 with probability 0.5 each and never 01 or 10.',
          'A two-wire circuit with H, a CNOT and two meters, and a table of the four amplitudes at the start, after H and after CNOT, with probabilities 0.5, 0, 0, 0.5.')


# ---- 3.5 no-cloning ----
def f5():
    o = [T(20, 26, 'Copying |+⟩: what linearity gives versus what a clone needs', 15, 'start', bold=True)]
    labs = ['|00⟩', '|01⟩', '|10⟩', '|11⟩']
    def panel(x, title, vals, c, f):
        p = [T(x + 140, 64, title, 14, fill=c, bold=True)]
        base = 200
        p.append(L(x, base, x + 280, base, L2, 1.5))
        for i, v in enumerate(vals):
            bx = x + 14 + i * 68; h = v * 140
            if h: p.append(R(bx, base - h, 46, h, f, c, 3))
            p.append(T(bx + 23, base - h - 7, f'{v:g}', 13, bold=True))
            p.append(T(bx + 23, base + 20, labs[i], 13, fill=MUT))
        return ''.join(p)
    o.append(panel(30, 'U|+⟩|0⟩ by linearity = (|00⟩ + |11⟩)/√2', [0.7071, 0, 0, 0.7071], NX, NXS))
    o.append(panel(400, 'true clone |+⟩|+⟩', [0.5, 0.5, 0.5, 0.5], AC, ACS))
    o.append(T(20, 264, 'Overlap: only |00⟩ and |11⟩ appear in both.', 14, 'start'))
    o.append(T(20, 290, '⟨clone | output⟩ = 0.7071 × 0.5 + 0.7071 × 0.5 = 0.7071', 15, 'start', bold=True))
    o.append(T(20, 316, 'Equal states would give 1. Since 0.7071 ≠ 1, no machine copies every state.', 14, 'start', NX, True))
    return 332, ''.join(o)
FIG[5] = (f5, 'A cloner that copies |0⟩ and |1⟩ must send |+⟩ to (|00⟩ + |11⟩)/√2, but a true copy |+⟩|+⟩ has 0.5 on all four terms; their overlap is 0.7071, not 1.',
          'Two amplitude bar charts over |00⟩, |01⟩, |10⟩, |11⟩: on the left 0.7071, 0, 0, 0.7071, on the right 0.5 on all four.')


# ---- 3.6 teleportation ----
def f6():
    o = [T(20, 26, 'Teleporting |ψ⟩ = 0.6|0⟩ + 0.8|1⟩', 15, 'start', bold=True)]
    ys = [80, 150, 220]
    labs = ['q0: |ψ⟩', 'q1: |0⟩', 'q2: |0⟩']
    o.append(wire(ys[0], 90, 470, labs[0])); o.append(wire(ys[1], 90, 470, labs[1])); o.append(wire(ys[2], 90, 640, labs[2]))
    o.append(R(120, 120, 130, 120, 'none', LV, 8, 1.5, '5 4')); o.append(T(185, 258, 'Bell pair |Φ⁺⟩', 13, fill=LV, bold=True))
    o.append(gate(150, ys[1], 'H', LVS, LV)); o.append(cnot(215, ys[1], ys[2], LV))
    o.append(R(268, 50, 160, 120, 'none', AC, 8, 1.5, '5 4')); o.append(T(348, 44, 'Alice', 13, fill=AC, bold=True))
    o.append(cnot(300, ys[0], ys[1])); o.append(gate(380, ys[0], 'H'))
    o.append(meter(470, ys[0])); o.append(meter(470, ys[1]))
    o.append(cwire(ys[0], 490, 600)); o.append(cwire(ys[1], 490, 530))
    o.append(L(600, ys[0] + 3, 600, ys[2] - 22, L2, 1.5)); o.append(L(604, ys[0] + 3, 604, ys[2] - 22, L2, 1.5))
    o.append(L(530, ys[1] + 3, 530, ys[2] - 22, L2, 1.5)); o.append(L(534, ys[1] + 3, 534, ys[2] - 22, L2, 1.5))
    o.append(gate(532, ys[2], 'X', NXS, NX)); o.append(gate(602, ys[2], 'Z', NXS, NX))
    o.append(T(498, ys[0] - 10, 'm1', 13, 'start', MUT)); o.append(T(498, ys[1] - 10, 'm2', 13, 'start', MUT))
    o.append(T(660, ys[2] + 5, '|ψ⟩', 15, 'start', NX, True)); o.append(T(567, 270, 'Bob', 13, fill=NX, bold=True))
    rows = [('00', 'I'), ('01', 'X'), ('10', 'Z'), ('11', 'X then Z ... XZ')]
    tx, ty = 40, 300
    o.append(T(tx, ty, 'Alice reads m1m2, each pair with probability 0.25; Bob fixes his qubit:', 14, 'start'))
    for i, (m, g) in enumerate([('00', 'I'), ('01', 'X'), ('10', 'Z'), ('11', 'XZ')]):
        o.append(boxt(tx + i * 165, ty + 14, 150, 44, [f'{m} → {g}'], NXS if g != 'I' else PANEL, NX, 14, True))
    o.append(T(tx, ty + 86, 'Every branch ends with 0.6|0⟩ + 0.8|1⟩, so Bob reads 0 with probability 0.6² = 0.36.', 14, 'start', NX, True))
    return 402, ''.join(o)
FIG[6] = (f6, 'Alice entangles |ψ⟩ = 0.6|0⟩ + 0.8|1⟩ with her half of a Bell pair and measures two bits; each pair has probability 0.25, and Bob’s matching correction I, X, Z or XZ leaves him with |ψ⟩, which reads 0 with probability 0.36.',
          'A three-wire teleportation circuit: a Bell pair made from H and CNOT on q1 and q2, Alice’s CNOT and H on q0 and q1 and two measurements, and double classical lines controlling X and Z on Bob’s q2.')


# ---- 3.7 superdense coding, message 10 ----
def f7():
    o = [T(20, 26, 'Superdense coding: Alice sends the two bits 10 with one qubit', 15, 'start', bold=True)]
    y1, y2 = 100, 170
    o.append(wire(y1, 110, 660, 'qubit 1')); o.append(wire(y2, 110, 660, 'qubit 2'))
    o.append(gate(150, y1, 'H', LVS, LV)); o.append(cnot(210, y1, y2, LV))
    o.append(gate(320, y1, 'Z', NXS, NX))
    o.append(cnot(450, y1, y2)); o.append(gate(530, y1, 'H'))
    o.append(meter(620, y1)); o.append(meter(620, y2))
    o.append(T(600, y1 - 26, '1', 16, fill=AC, bold=True)); o.append(T(600, y2 + 42, '0', 16, fill=AC, bold=True))
    o.append(T(180, 52, 'shared pair', 13, fill=LV, bold=True)); o.append(T(320, 52, 'Alice: 10 → Z', 13, fill=NX, bold=True))
    o.append(T(530, 52, 'Bob decodes', 13, fill=AC, bold=True))
    o.append(L(385, 62, 385, 196, MUT, 1.5, '4 4')); o.append(T(392, 76, 'qubit 1 travels to Bob', 13, 'start', MUT))
    states = [(265, '(|00⟩ + |11⟩)/√2', '|Φ⁺⟩, shared', LV, LVS), (385, '(|00⟩ − |11⟩)/√2', '|Φ⁻⟩, after Z', NX, NXS),
              (490, '(|00⟩ − |10⟩)/√2', 'after CNOT', AC, ACS), (660, '|1⟩|0⟩ = |10⟩', 'after H', AC, ACS)]
    for i, (x, s_, n, c, f) in enumerate(states):
        o.append(f'<circle cx="{x}" cy="{y2 + 36}" r="11" style="fill:{f};stroke:{c};stroke-width:1.5"/>')
        o.append(T(x, y2 + 41, str(i + 1), 13, fill=c, bold=True))
        bx = 20 + i * 172
        o.append(boxt(bx, 246, 160, 60, [f'{i + 1}. {n}', s_], f, c, 14, True))
        if i < 3: o.append(L(bx + 162, 276, bx + 170, 276, c, 2))
    o.append(T(20, 340, 'Code book: 00 → I, 01 → X, 10 → Z, 11 → XZ. Bob reads qubit 1 = 1, qubit 2 = 0: the message 10.', 14, 'start'))
    return 356, ''.join(o)
FIG[7] = (f7, 'Alice’s Z turns the shared |Φ⁺⟩ into |Φ⁻⟩; after her qubit reaches Bob, his CNOT gives (|00⟩ − |10⟩)/√2 and his H gives |10⟩, so he reads the two bits 1 and 0.',
          'A two-wire circuit: H and CNOT make a Bell pair, Alice applies Z to qubit 1, then Bob applies CNOT and H and measures 1 and 0; the state after each stage is written below.')


# ---- 3.8 Qiskit Bell circuit and its counts ----
def f8():
    o = [T(20, 26, 'The Bell circuit in Qiskit and its expected counts in 1024 shots', 15, 'start', bold=True)]
    o.append(R(20, 50, 330, 170, PANEL, L2, 8))
    code = ['qc = QuantumCircuit(2, 2)', 'qc.h(0)', 'qc.cx(0, 1)', 'qc.measure([0, 1], [0, 1])', 'run with shots = 1024']
    for i, c in enumerate(code):
        o.append(TM(36, 82 + i * 30, c, 14, 'start', INK if i < 4 else MUT))
    o.append(T(36, 248, 'h(0): (|0⟩ + |1⟩)/√2 on q0', 13, 'start', MUT))
    o.append(T(36, 270, 'cx(0, 1): (|00⟩ + |11⟩)/√2', 13, 'start', MUT))
    x0, base, top = 410, 260, 70
    fy = lambda v: base - v / 600 * (base - top)
    for v in (0, 256, 512):
        o += [L(x0, fy(v), 700, fy(v), LN, 1), T(x0 - 8, fy(v) + 4.5, str(v), 13, 'end', MUT)]
    for i, (b, v) in enumerate((('00', 512), ('01', 0), ('10', 0), ('11', 512))):
        bx = x0 + 16 + i * 70
        if v: o.append(R(bx, fy(v), 46, base - fy(v), ACS, AC, 3))
        o.append(T(bx + 23, fy(v) - 8, f'≈ {v}' if v else '0', 13, bold=True))
        o.append(T(bx + 23, base + 20, b, 14, fill=MUT, bold=True))
    o.append(T(x0, 56, 'counts', 13, 'start', MUT))
    o.append(T(20, 312, 'Expected: 1024 × ½ = 512 for 00 and for 11, none for 01 or 10. A real run wobbles, e.g. 498 and 526.', 14, 'start'))
    return 328, ''.join(o)
FIG[8] = (f8, 'Four lines of Qiskit build and measure the Bell circuit; with 1024 shots the ideal counts are 512 for 00 and 512 for 11, and a real run varies around these.',
          'A code box with QuantumCircuit, h, cx and measure, beside a histogram of counts with two bars of about 512 at 00 and 11 and none at 01 and 10.')


TEXT = {
    3: [('Solovay-Kitaev is a name for bounds on how the gate count grows; only a few universities teach its proof in detail.',
         'Solovay–Kitaev is the name of the result that bounds how the gate count grows; its proof is rarely examined.')],
    8: [('Only a few universities teach hardware job submission in detail. ', '')],
}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d


def text_fixes(k):
    return TEXT.get(k, [])
