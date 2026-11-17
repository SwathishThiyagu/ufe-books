"""Claude's hand-drawn figures for c-quantum-u5 (Quantum Computing, unit 5: information, cryptography and error
correction), one per chapter, each drawn from that chapter's worked example with its own numbers."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {6: 1}


def bitrow(x, y, bits, label, fill=PANEL, stroke=AC, cw=46, lab_c=INK):
    o = [T(x - 12, y + 29, label, 14, 'end', lab_c, True)]
    for i, b in enumerate(bits):
        o.append(R(x + i * cw, y, cw - 6, 40, fill, stroke, 5))
        o.append(TM(x + i * cw + (cw - 6) / 2, y + 27, b, 17, bold=True))
    return ''.join(o)


# ---- 5.1 one-time pad ----
def f1():
    o = [T(20, 26, 'One-time pad: the same key k = 0110 at both ends', 15, 'start', bold=True)]
    o.append(T(200, 60, 'Alice encrypts', 14, fill=AC, bold=True)); o.append(T(560, 60, 'Bob decrypts', 14, fill=NX, bold=True))
    o.append(bitrow(130, 76, '1011', 'm', ACS, AC))
    o.append(bitrow(130, 126, '0110', '⊕ k', LVS, LV, lab_c=LV))
    o.append(L(120, 176, 310, 176, INK, 1.5))
    o.append(bitrow(130, 186, '1101', 'c', PANEL, INK))
    o.append(L(318, 206, 446, 206, MUT, 2.5, arrow='m')); o.append(Tb(382, 196, 'c = 1101 sent', 13, fill=MUT, bold=True))
    o.append(bitrow(490, 76, '1101', 'c', PANEL, INK))
    o.append(bitrow(490, 126, '0110', '⊕ k', LVS, LV, lab_c=LV))
    o.append(L(480, 176, 670, 176, INK, 1.5))
    o.append(bitrow(490, 186, '1011', 'm', NXS, NX))
    o.append(T(20, 266, 'XOR rule: equal bits give 0, different bits give 1. Applying k twice cancels: (m ⊕ k) ⊕ k = m.', 14, 'start'))
    o.append(T(20, 290, 'In decimal: 11 ⊕ 6 = 13 is sent, and 13 ⊕ 6 = 11 comes back.', 14, 'start', MUT))
    return 306, ''.join(o)
FIG[1] = (f1, 'Alice XORs m = 1011 with k = 0110 to get c = 1101; Bob XORs c with the same k and gets m = 1011 back, because applying the key twice cancels.',
          'Two XOR sums side by side: 1011 XOR 0110 = 1101 on Alice’s side, and 1101 XOR 0110 = 1011 on Bob’s side, with an arrow carrying 1101 between them.')


# ---- 5.2 BB84 sifting ----
def pol(x, y, basis, bit, c):
    """small circle with a polarisation arrow"""
    ang = {('+', 0): 0, ('+', 1): 90, ('×', 0): 45, ('×', 1): 135}[(basis, bit)]
    a = math.radians(ang); r = 15
    o = [f'<circle cx="{x}" cy="{y}" r="20" style="fill:var(--panel);stroke:{c};stroke-width:1.5"/>']
    o.append(L(x - r * math.cos(a), y + r * math.sin(a), x + r * math.cos(a), y - r * math.sin(a), c, 2.5))
    return ''.join(o)

def f2():
    o = [T(20, 26, 'BB84 sifting: keep only the positions where the bases match', 15, 'start', bold=True)]
    A = [(0, '+'), (1, '+'), (1, '×'), (0, '×')]
    B = ['+', '×', '×', '+']
    gx, cw = 230, 120
    rows = ['position', 'Alice bit', 'Alice basis', 'photon sent', 'Bob basis', 'bases match?', 'kept bit']
    for i, r in enumerate(rows): o.append(T(gx - 30, 66 + i * 46 + (10 if r == 'photon sent' else 0), r, 14, 'end', MUT, True))
    for j, ((bit, ba), bb) in enumerate(zip(A, B)):
        x = gx + j * cw + cw / 2
        keep = ba == bb
        if keep: o.append(R(x - 50, 44, 100, 322, LVS, LV, 10, 1.5))
        o.append(T(x, 66, str(j + 1), 15, bold=True))
        o.append(T(x, 112, str(bit), 16, bold=True))
        o.append(T(x, 158, ba, 20, fill=AC, bold=True))
        o.append(pol(x, 200, ba, bit, AC))
        o.append(T(x, 250, bb, 20, fill=NX, bold=True))
        o.append(T(x, 296, 'yes' if keep else 'no', 15, fill=LV if keep else MUT, bold=keep))
        o.append(T(x, 342, str(bit) if keep else '–', 17, fill=INK if keep else MUT, bold=True))
    o.append(T(20, 396, 'Sifted key: positions 1 and 3 give the bits 0 and 1, so the key is 01. Positions 2 and 4 are thrown away.', 14, 'start'))
    return 412, ''.join(o)
FIG[2] = (f2, 'Alice’s bases are +, +, ×, × and Bob’s are +, ×, ×, +; they agree only at positions 1 and 3, so Alice’s bits there, 0 and 1, form the sifted key 01.',
          'A table of four photon positions with Alice’s bit, basis and polarisation, Bob’s basis, whether the bases match, and the kept bit; positions 1 and 3 are shaded as kept.')


# ---- 5.3 binary entropy ----
def f3():
    x0, x1, y0, y1 = 80, 460, 60, 320
    fx = lambda p: x0 + p * (x1 - x0)
    fy = lambda h: y1 - h * (y1 - y0)
    H = lambda p: 0 if p in (0, 1) else -p * math.log2(p) - (1 - p) * math.log2(1 - p)
    o = [T(20, 26, 'Entropy of a two-outcome source, H₂(p), in bits', 15, 'start', bold=True)]
    o.append(axes(x0, x1, y0, y1, [0, 0.1, 0.5, 0.9, 1], [0, 0.469, 1], fx, fy, 'probability (or eigenvalue) p', 'bits', lambda v: f'{v:g}', lambda v: f'{v:g}'))
    o.append(P([(fx(i / 200), fy(H(i / 200))) for i in range(201)], AC, 3))
    o.append(L(fx(0.1), fy(0.469), fx(0.9), fy(0.469), LV, 1.5, '5 4'))
    o.append(C(fx(0.5), fy(1), 7, NX)); o.append(C(fx(0.9), fy(0.469), 7, LV)); o.append(C(fx(0.1), fy(0.469), 5, LV))
    o.append(C(fx(1), fy(0), 7, INK))
    o.append(Tb(fx(0.5), fy(1) - 14, '1.000', 14, fill=NX, bold=True)); o.append(Tb(fx(0.9) + 2, fy(0.469) - 14, '0.469', 14, fill=LV, bold=True))
    X = 490
    o.append(boxt(X, 60, 214, 58, ['fair coin, p = 0.5', '1.000 bit'], NXS, NX, 14, True))
    o.append(boxt(X, 128, 214, 58, ['I/2: eigenvalues ½, ½', '1.000 bit'], NXS, NX, 14, True))
    o.append(boxt(X, 196, 214, 58, ['diag(0.9, 0.1)', '0.469 bit'], LVS, LV, 14, True))
    o.append(boxt(X, 264, 214, 58, ['pure |+⟩: eigenvalues 1, 0', '0.000 bit'], PANEL, INK, 14, True))
    o.append(T(20, 392, 'Von Neumann entropy uses the eigenvalues of ρ: |+⟩ is pure, so S = 0 even though measuring it in 0/1 gives a coin toss.', 13, 'start', MUT))
    return 408, ''.join(o)
FIG[3] = (f3, 'The binary entropy curve peaks at 1 bit for p = 0.5, which covers the fair coin and I/2; eigenvalues 0.9 and 0.1 give 0.469 bit, and a pure state such as |+⟩, with eigenvalues 1 and 0, gives 0.',
          'A hump-shaped curve of entropy against p from 0 to 1, peaking at 1 bit at p = 0.5, with points marked at 0.469 for p = 0.9 and at 0 for p = 1, beside four boxes for the four sources.')


# ---- 5.4 Schumacher compression ----
def f4():
    o = [T(20, 26, '1000 copies of ρ with eigenvalues 0.9 and 0.1', 15, 'start', bold=True)]
    s = 0.62
    o.append(R(30, 70, 1000 * s, 50, PANEL, L2, 6)); o.append(T(30 + 500 * s, 101, 'stored naively: 1000 qubits', 14, bold=True))
    o.append(R(30, 150, 469 * s, 50, ACS, AC, 6)); o.append(T(30 + 469 * s / 2, 181, '469 qubits', 15, bold=True))
    o.append(T(30 + 469 * s + 12, 181, 'after Schumacher compression', 14, 'start', AC, True))
    o.append(L(30 + 469 * s, 130, 30 + 469 * s, 210, LV, 2, '5 4'))
    o.append(T(20, 250, 'S(ρ) = −0.9 log₂ 0.9 − 0.1 log₂ 0.1 = 0.1368 + 0.3322 = 0.469 qubit per copy', 14, 'start'))
    o.append(T(20, 276, '1000 × 0.469 = 469 qubits: they label the typical subspace, about 2⁴⁶⁹ of the 2¹⁰⁰⁰ dimensions.', 14, 'start'))
    o.append(T(20, 302, 'Fidelity → 1 as the number of copies grows; fewer than nS(ρ) qubits and it fails.', 14, 'start', LV, True))
    return 318, ''.join(o)
FIG[4] = (f4, 'Because S(ρ) = 0.469 qubit per copy, 1000 copies fit into about 469 qubits instead of 1000, the size of the typical subspace (about 2⁴⁶⁹ dimensions), with fidelity close to 1.',
          'Two horizontal bars: a long bar for 1000 qubits stored naively and a bar less than half as long for 469 qubits after compression.')


# ---- 5.5 bit-flip channel and its Holevo quantity ----
def f5():
    o = [T(20, 26, 'Bit-flip channel with p = 0.1, inputs 0 and 1 equally likely', 15, 'start', bold=True)]
    ix, ox, y0, y1 = 110, 400, 90, 230
    for y, b in ((y0, '0'), (y1, '1')):
        o.append(f'<circle cx="{ix}" cy="{y}" r="24" style="fill:{ACS};stroke:{AC};stroke-width:2"/>'); o.append(T(ix, y + 6, b, 17, bold=True))
        o.append(f'<circle cx="{ox}" cy="{y}" r="24" style="fill:{NXS};stroke:{NX};stroke-width:2"/>'); o.append(T(ox, y + 6, b, 17, bold=True))
    o.append(T(ix, 52, 'input', 14, fill=AC, bold=True)); o.append(T(ox, 52, 'output', 14, fill=NX, bold=True))
    o.append(L(ix + 26, y0, ox - 30, y0, AC, 3, arrow='n')); o.append(L(ix + 26, y1, ox - 30, y1, AC, 3, arrow='n'))
    o.append(L(ix + 24, y0 + 10, ox - 28, y1 - 14, LV, 2, '6 4', 'l')); o.append(L(ix + 24, y1 - 10, ox - 28, y0 + 14, LV, 2, '6 4', 'l'))
    o.append(Tb((ix + ox) / 2, y0 - 10, 'kept 0.9', 14, fill=AC, bold=True)); o.append(Tb((ix + ox) / 2, y1 + 24, 'kept 0.9', 14, fill=AC, bold=True))
    o.append(Tb((ix + ox) / 2 - 50, (y0 + y1) / 2 - 2, 'flip 0.1', 13, fill=LV, bold=True))
    X, W = 460, 240
    o.append(T(X, 80, 'one channel use = 1 bit sent', 14, 'start', bold=True))
    o.append(R(X, 94, 0.531 * W, 44, ACS, AC, 4)); o.append(R(X + 0.531 * W, 94, 0.469 * W, 44, LVS, LV, 4))
    o.append(T(X + 0.531 * W / 2, 121, '0.531', 14, bold=True)); o.append(T(X + 0.531 * W + 0.469 * W / 2, 121, '0.469', 14, bold=True))
    o.append(T(X, 162, 'gets through: χ', 13, 'start', AC, True)); o.append(T(X + W, 162, 'lost: H₂(0.1)', 13, 'end', LV, True))
    o.append(T(20, 290, 'H₂(0.1) = 0.1 × 3.3219 + 0.9 × 0.1520 = 0.3322 + 0.1368 = 0.469 bits', 14, 'start'))
    o.append(T(20, 314, 'χ = 1 − H₂(0.1) = 1 − 0.469 = 0.531 bits per channel use', 14, 'start', AC, True))
    return 330, ''.join(o)
FIG[5] = (f5, 'Each input bit arrives unchanged with probability 0.9 and flipped with 0.1; the noise costs H₂(0.1) = 0.469 bits, leaving χ = 0.531 bits per channel use.',
          'Two inputs 0 and 1 joined to two outputs by straight arrows for kept, 0.9, and dashed crossing arrows for flipped, 0.1; a bar splits one bit into 0.531 that gets through and 0.469 lost.')


# ---- 5.6 repetition code and majority vote ----
def f6():
    o = [T(20, 26, '3-bit repetition code: send 101, decode by majority vote', 15, 'start', bold=True)]
    msg = ['1', '0', '1']
    sent = ['111', '000', '111']
    recv = ['101', '000', '111']
    for j in range(3):
        x = 40 + j * 220
        o.append(boxt(x, 54, 60, 40, [msg[j]], PANEL, L2, 17, True))
        o.append(L(x + 30, 96, x + 30, 116, AC, 2, arrow='n'))
        o.append(boxt(x, 120, 160, 40, [sent[j]], ACS, AC, 17, True))
        o.append(L(x + 80, 162, x + 80, 186, MUT, 2, arrow='m'))
        flipped = recv[j] != sent[j]
        o.append(R(x, 190, 160, 40, NXS if flipped else ACS, NX if flipped else AC, 8))
        for k, b in enumerate(recv[j]):
            bad = b != sent[j][k]
            o.append(TM(x + 50 + k * 30, 217, b, 17, fill=NX if bad else INK, bold=True))
        o.append(L(x + 80, 232, x + 80, 256, AC, 2, arrow='n'))
        o.append(boxt(x + 50, 260, 60, 40, [msg[j]], LVS, LV, 17, True))
    for y, lab in ((74, 'message'), (140, 'sent'), (210, 'received'), (280, 'majority')):
        o.append(T(700, y + 5, lab, 13, 'end', MUT))
    o.append(T(44, 250, 'one flip', 13, 'start', NX, True))
    o.append(T(20, 336, 'Codewords 000 and 111 differ in 3 places: d_min = 3, corrects t = 1 error, detects 2, rate 1/3.', 14, 'start'))
    o.append(T(20, 360, 'Two flips in one block, such as 111 → 100, out-vote the truth: the decoder outputs 0, wrongly.', 14, 'start', NX, True))
    return 376, ''.join(o)
FIG[6] = (f6, 'Each bit of 101 is sent three times; the first block arrives as 101 with one flip, and majority vote still returns 1, so the message 101 is recovered. Two flips in a block would win the vote and give the wrong bit.',
          'Three columns, one per message bit: 1, 0, 1 encoded as 111, 000, 111, received as 101, 000, 111 with the flipped bit highlighted, and decoded by majority back to 1, 0, 1.')


# ---- 5.7 three-qubit bit-flip code ----
def f7():
    o = [T(20, 26, 'Bit-flip code: an X error on qubit 2 and its syndrome', 15, 'start', bold=True)]
    stages = [('encoded', 'α|000⟩ + β|111⟩', ACS, AC), ('X on qubit 2', 'α|010⟩ + β|101⟩', NXS, NX), ('after X on qubit 2', 'α|000⟩ + β|111⟩', LVS, LV)]
    for i, (n, s, f, c) in enumerate(stages):
        x = 20 + i * 240
        o.append(boxt(x, 50, 200, 60, [n, s], f, c, 14, True))
        if i < 2: o.append(L(x + 202, 80, x + 236, 80, MUT, 2, arrow='m'))
    o.append(T(20, 150, 'Read the parities of the |010⟩ term (the |101⟩ term gives the same):', 14, 'start'))
    cx = [180, 300, 420]
    for i, (b, x) in enumerate(zip('010', cx)):
        bad = i == 1
        o.append(f'<circle cx="{x}" cy="210" r="26" style="fill:{NXS if bad else PANEL};stroke:{NX if bad else AC};stroke-width:2"/>')
        o.append(T(x, 217, b, 18, bold=True)); o.append(T(x, 256, f'qubit {i + 1}', 13, fill=MUT))
    o.append(brace(180, 300, 176, LV, up=True)); o.append(T(240, 166, 'Z₁Z₂: differ → s₁₂ = 1', 13, fill=LV, bold=True))
    o.append(brace(300, 420, 280, LV)); o.append(T(360, 302, 'Z₂Z₃: differ → s₂₃ = 1', 13, fill=LV, bold=True))
    X = 490
    o.append(T(X, 160, 'syndrome table', 14, 'start', bold=True))
    tab = [('00', 'no error'), ('10', 'X on qubit 1'), ('11', 'X on qubit 2'), ('01', 'X on qubit 3')]
    for i, (s, g) in enumerate(tab):
        y = 172 + i * 34
        hit = s == '11'
        o.append(R(X, y, 210, 30, LVS if hit else PANEL, LV if hit else L2, 5))
        o.append(T(X + 30, y + 21, s, 14, bold=True)); o.append(T(X + 60, y + 21, g, 14, 'start', bold=hit))
    o.append(T(20, 344, 'The checks compare qubits without reading α or β, so the superposition survives the repair.', 14, 'start', MUT))
    return 360, ''.join(o)
FIG[7] = (f7, 'An X error on qubit 2 turns α|000⟩ + β|111⟩ into α|010⟩ + β|101⟩; both parity checks see a difference, giving the syndrome (1, 1), which points to qubit 2, and an X there restores the code word.',
          'Three boxes: the encoded state, the state after an X error on qubit 2, and the repaired state; below, three qubit circles 0, 1, 0 with brackets for the two parity checks, both reading 1, and a syndrome table with 11 meaning X on qubit 2.')


# ---- 5.8 fault tolerance: two failures needed ----
def f8():
    o = [T(20, 26, 'A logical gate from 3 physical gates, each failing with p = 0.001', 15, 'start', bold=True)]
    cases = [('exactly 2 fail', '3 ways × p²(1 − p)', '3 × 9.99 × 10⁻⁷ = 2.997 × 10⁻⁶', NXS, NX), ('all 3 fail', 'p³', '1 × 10⁻⁹', PANEL, L2)]
    for i, (a, b, c, f, s) in enumerate(cases):
        y = 50 + i * 80
        o.append(boxt(20, y, 680, 64, [f'{a}: {b}', c], f, s, 14, True))
    o.append(boxt(20, 214, 680, 50, ['logical failure = 2.997 × 10⁻⁶ + 1 × 10⁻⁹ = 2.998 × 10⁻⁶ ≈ 3 × 10⁻⁶'], LVS, LV, 15, True))
    # log scale comparison
    x0, x1, yb = 120, 660, 330
    fx = lambda e: x0 + (e + 7) / 5 * (x1 - x0)
    o.append(L(x0, yb, x1, yb, L2, 1.5))
    for e in range(-7, -1):
        o.append(L(fx(e), yb - 5, fx(e), yb + 5, L2, 1.5)); o.append(T(fx(e), yb + 22, f'10{"⁻" + "⁰¹²³⁴⁵⁶⁷"[-e]}', 13, fill=MUT))
    o.append(C(fx(-3), yb, 8, NX)); o.append(Tb(fx(-3), yb - 16, 'one physical gate 10⁻³', 13, fill=NX, bold=True))
    o.append(C(fx(math.log10(3e-6)), yb, 8, LV)); o.append(Tb(fx(math.log10(3e-6)), yb - 16, 'logical gate 3 × 10⁻⁶', 13, fill=LV, bold=True))
    o.append(T(20, yb + 5, 'failure rate', 13, 'start', MUT))
    o.append(T(20, 392, 'About 3p² instead of p: a gain only while p is small, which is why a threshold exists.', 14, 'start'))
    return 408, ''.join(o)
FIG[8] = (f8, 'With p = 0.001 per physical gate, the logical gate fails only when two or three fail: 2.997 × 10⁻⁶ + 1 × 10⁻⁹ = 2.998 × 10⁻⁶, about 300 times rarer than one physical failure.',
          'Two boxes for the failure cases, exactly two and all three, a total box of 2.998 times ten to the minus six, and a log-scale line placing the physical rate 10 to the minus 3 far to the right of the logical rate 3 times 10 to the minus 6.')


TEXT = {
    1: [('Only a few universities teach this as a full topic; in quantum computing it is the classical baseline.',
         'In quantum computing it is the classical baseline.')],
    5: [('Only a few universities teach this topic. Some syllabi call it', 'Some syllabi call it')],
}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d


def text_fixes(k):
    return TEXT.get(k, [])
