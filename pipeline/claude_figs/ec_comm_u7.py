"""Claude's hand-drawn figures for ec-comm-u7 (Information theory and error-control coding), one per chapter.
Every number comes from that chapter's worked example. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
Hb = lambda p: -(p * math.log2(p) + (1 - p) * math.log2(1 - p))


def arrow(x1, y1, x2, y2, c=AC, w=2, a='n', dash=None):
    return L(x1, y1, x2, y2, c, w, dash, a)


# ---- 7.1 self-information of the four symbols, and the binary entropy curve ----
def f1():
    o = []
    # left panel: bars of I(x) for p = 1/2, 1/4, 1/8, 1/8
    x0, yb, sc = 60, 300, 70
    o.append(T(30, 34, 'Worked example 1: I = log₂(1/p)', 15, 'start', bold=True))
    o.append(L(x0 - 10, yb, x0 + 290, yb, L2, 1.5))
    for v in (1, 2, 3):
        o.append(L(x0 - 10, yb - v * sc, x0 + 290, yb - v * sc, LN, 1))
        o.append(T(x0 - 16, yb - v * sc + 5, str(v), 13, 'end', MUT))
    o.append(T(x0 - 16, yb + 5, '0', 13, 'end', MUT))
    for i, (p, I) in enumerate([('1/2', 1), ('1/4', 2), ('1/8', 3), ('1/8', 3)]):
        x = x0 + 14 + i * 68
        o.append(R(x, yb - I * sc, 44, I * sc, ACS, AC, 3, 1.5))
        o.append(T(x + 22, yb - I * sc - 8, f'{I} bit' + ('s' if I > 1 else ''), 13, bold=True))
        o.append(T(x + 22, yb + 20, f'p = {p}', 13, fill=MUT))
    yh = yb - 1.75 * sc
    o.append(L(x0 - 10, yh, x0 + 290, yh, NX, 2.5, '7 5'))
    o.append(Tb(x0 + 220, yh - 8, 'H = 1.75 bits', 14, fill=NX, bold=True))
    o.append(T(x0 + 140, yb + 44, 'average over the symbols = entropy', 13, fill=MUT))
    # right panel: H(p)
    X0, X1, Y0, Y1 = 420, 700, 70, 300
    fx = lambda p: X0 + p * (X1 - X0); fy = lambda h: Y1 - h * (Y1 - Y0)
    o.append(axes(X0, X1, Y0, Y1, [0, 0.5, 1], [0, 0.5, 1], fx, fy, 'probability p of one symbol', 'H(p) in bits', xfmt=lambda v: f'{v:g}', yfmt=lambda v: f'{v:g}'))
    pts = [(fx(p), fy(Hb(p))) for p in [0.001] + [i / 50 for i in range(1, 50)] + [0.999]]
    o.append(P(pts, AC, 3))
    o.append(C(fx(0.5), fy(1), 5, AC)); o.append(T(fx(0.5), fy(1) - 12, 'p = 0.5: 1 bit', 13, bold=True))
    o.append(C(fx(0.1), fy(Hb(0.1)), 5, NX)); o.append(T(fx(0.1) + 10, fy(Hb(0.1)) + 22, 'p = 0.1: 0.469', 13, 'start', fill=NX, bold=True))
    return 364, ''.join(o)

FIG[1] = (f1, 'Left: the four symbols of worked example 1 carry 1, 2, 3 and 3 bits, and their probability-weighted average is H = 1.75 bits/symbol. Right: a two-symbol source is most uncertain at p = 0.5 (1 bit) and carries only 0.469 bit at p = 0.1.',
          'Left, a bar chart of self-information: 1 bit for p one half, 2 bits for p one quarter, 3 bits for each p one eighth, with a dashed line at the entropy 1.75 bits. Right, the binary entropy curve rising from 0 to 1 bit at p = 0.5 and falling back, with p = 0.1 marked at 0.469 bit.')


# ---- 7.2 the Huffman tree of worked example 1 ----
def f2():
    o = []
    nodes = {'root': (120, 50, '1.0'), 'A': (40, 140, 'A 0.4'), 'n6': (230, 140, '0.6'), 'B': (150, 230, 'B 0.2'),
             'n4': (340, 230, '0.4'), 'C': (260, 320, 'C 0.2'), 'n2': (450, 320, '0.2'), 'D': (370, 410, 'D 0.1'), 'E': (540, 410, 'E 0.1')}
    edges = [('root', 'A', '0'), ('root', 'n6', '1'), ('n6', 'B', '0'), ('n6', 'n4', '1'), ('n4', 'C', '0'), ('n4', 'n2', '1'), ('n2', 'D', '0'), ('n2', 'E', '1')]
    for a, b, bit in edges:
        (x1, y1, _), (x2, y2, _) = nodes[a], nodes[b]
        o.append(L(x1, y1 + 18, x2, y2 - 18, L2, 2))
        o.append(Tb((x1 + x2) / 2 + (-10 if bit == '0' else 10), (y1 + y2) / 2 + 5, bit, 14, fill=AC, bold=True))
    leaves = {'A': '0', 'B': '10', 'C': '110', 'D': '1110', 'E': '1111'}
    for k, (x, y, s) in nodes.items():
        leaf = k in leaves
        o.append(boxt(x - 40, y - 18, 80, 36, [s], ACS if leaf else PANEL, AC if leaf else L2, 14, bold_first=leaf))
        if leaf: o.append(TM(x, y + 38, leaves[k], 14, fill=NX, bold=True))
    steps = ['Merges, smallest two first:', '1. D 0.1 + E 0.1 → 0.2', '2. C 0.2 + DE 0.2 → 0.4', '3. B 0.2 + CDE 0.4 → 0.6', '4. A 0.4 + 0.6 → 1.0',
             '', 'L̄ = 0.4(1) + 0.2(2) + 0.2(3)', '     + 0.1(4) + 0.1(4)', '   = 2.2 bits/symbol', 'H = 2.12, η = 96.45 %']
    for i, s in enumerate(steps):
        o.append(T(470, 44 + i * 24, s, 14, 'start', AC if i == 8 else INK, bold=(i in (0, 8))))
    return 470, ''.join(o)

FIG[2] = (f2, 'The Huffman tree of worked example 1, built bottom-up by merging the two smallest probabilities; reading 0s and 1s from the root gives the codewords under each leaf and L̄ = 2.2 bits/symbol against H = 2.12.',
          'A staircase-shaped tree. The root 1.0 splits into leaf A 0.4 on branch 0 and node 0.6 on branch 1; 0.6 splits into B 0.2 and 0.4; 0.4 into C 0.2 and 0.2; 0.2 into D 0.1 and E 0.1. Codes: A 0, B 10, C 110, D 1110, E 1111. A side list gives the four merges and the average length 2.2 bits per symbol.')


# ---- 7.3 the BSC of the worked examples, and where H(Y) goes ----
def f3():
    o = []
    xa, xb, y0, y1 = 70, 300, 80, 250
    for x, lab in ((xa, 'X'), (xb, 'Y')):
        o.append(T(x, 40, lab + (' (sent)' if lab == 'X' else ' (received)'), 15, bold=True))
    for y, b in ((y0, '0'), (y1, '1')):
        o.append(C(xa, y, 18, PANEL)); o.append(f'<circle cx="{xa}" cy="{y}" r="18" style="fill:var(--panel);stroke:var(--accent);stroke-width:2"/>')
        o.append(T(xa, y + 5, b, 15, bold=True))
        o.append(f'<circle cx="{xb}" cy="{y}" r="18" style="fill:var(--panel);stroke:var(--accent);stroke-width:2"/>')
        o.append(T(xb, y + 5, b, 15, bold=True))
    o.append(arrow(xa + 20, y0, xb - 24, y0)); o.append(arrow(xa + 20, y1, xb - 24, y1))
    o.append(arrow(xa + 18, y0 + 8, xb - 22, y1 - 10, NX, 1.8, 'x')); o.append(arrow(xa + 18, y1 - 8, xb - 22, y0 + 10, NX, 1.8, 'x'))
    o.append(Tb((xa + xb) / 2, y0 - 10, '1 − p = 0.9', 14, fill=AC, bold=True)); o.append(Tb((xa + xb) / 2, y1 + 22, '1 − p = 0.9', 14, fill=AC, bold=True))
    o.append(Tb((xa + xb) / 2 - 42, (y0 + y1) / 2 - 18, 'p = 0.1', 14, fill=NX, bold=True)); o.append(Tb((xa + xb) / 2 + 42, (y0 + y1) / 2 + 26, 'p = 0.1', 14, fill=NX, bold=True))
    # bars
    bx, sc = 400, 280
    o.append(T(bx, 40, 'H(Y) splits into noise and information', 15, 'start', bold=True))
    for j, (lab, hy, i) in enumerate([('P(X = 0) = 0.5', 1.0, 0.531), ('P(X = 0) = 0.7', 0.925, 0.456)]):
        y = 84 + j * 100
        o.append(T(bx, y - 10, lab, 14, 'start'))
        o.append(R(bx, y, i * sc, 34, ACS, AC, 3, 1.5)); o.append(R(bx + i * sc, y, (hy - i) * sc, 34, NXS, NX, 3, 1.5))
        o.append(T(bx + i * sc / 2, y + 23, f'I = {i:.3f}', 14, bold=True)); o.append(T(bx + i * sc + (hy - i) * sc / 2, y + 23, '0.469', 14))
        o.append(T(bx, y + 56, f'H(Y) = {hy:.3f} bits', 13, 'start', MUT))
    o.append(R(bx, 290, 16, 16, ACS, AC, 3, 1.5)); o.append(T(bx + 24, 303, 'I(X;Y): what the output tells', 13, 'start'))
    o.append(R(bx, 316, 16, 16, NXS, NX, 3, 1.5)); o.append(T(bx + 24, 329, 'H(Y|X) = H(0.1): noise', 13, 'start'))
    return 350, ''.join(o)

FIG[3] = (f3, 'The binary symmetric channel of the worked examples flips a bit with p = 0.1. Of the output entropy, 0.469 bit is noise whatever is sent; the rest is mutual information: 0.531 bit with equally likely inputs, only 0.456 bit when 0 is sent 70 % of the time.',
          'Left, a two-input two-output diagram: 0 to 0 and 1 to 1 with probability 0.9, crossing arrows 0 to 1 and 1 to 0 with probability 0.1. Right, two stacked bars: for equally likely inputs H(Y) = 1 bit made of I = 0.531 and noise 0.469; for P(X = 0) = 0.7, H(Y) = 0.925 bits made of I = 0.456 and noise 0.469.')


# ---- 7.4 capacity per hertz against SNR ----
def f4():
    X0, X1, Y0, Y1 = 80, 640, 50, 330
    fx = lambda d: X0 + (d + 10) / 40 * (X1 - X0); fy = lambda c: Y1 - c / 11 * (Y1 - Y0)
    o = [axes(X0, X1, Y0, Y1, [-10, 0, 10, 20, 30], [0, 2, 4, 6, 8, 10], fx, fy, 'SNR in dB', 'C/B in bit/s/Hz', xfmt=neg)]
    pts = [(fx(d), fy(math.log2(1 + 10 ** (d / 10)))) for d in [i / 2 for i in range(-20, 61)]]
    o.append(P(pts, AC, 3))
    for d, lab, dx in ((0, 'C/B = 1 at 0 dB', 12), (20, '6.66 (20 dB → 20.6 kbit/s in 3.1 kHz)', -10), (30, '9.97 (30 dB → 30.9 kbit/s)', -10)):
        c = math.log2(1 + 10 ** (d / 10))
        o.append(C(fx(d), fy(c), 5, NX))
        o.append(Tb(fx(d) + dx, fy(c) - 12, lab, 13, 'start' if dx > 0 else 'end', NX, True))
    o.append(L(fx(20), fy(6.66), fx(30), fy(6.66), L2, 1.5, '4 4')); o.append(L(fx(30), fy(6.66), fx(30), fy(9.97), L2, 1.5, '4 4'))
    o.append(T(fx(25), fy(6.66) + 20, '+10 dB', 13, fill=MUT)); o.append(T(fx(30) + 8, fy(8.3), '+3.31', 13, 'start', MUT))
    return 390, ''.join(o)

FIG[4] = (f4, 'log₂(1 + S/N) against SNR. From 20 dB to 30 dB the telephone channel of the worked example gains 3.31 bit/s/Hz, about one bit per 3 dB; below 0 dB the curve is under 1 bit/s/Hz and nearly straight in S/N, where extra power, not bandwidth, is what helps.',
          'A rising curve of capacity per hertz against SNR from minus 10 to 30 dB, passing 1 at 0 dB, 6.66 at 20 dB and 9.97 at 30 dB; a dashed step shows a gain of 3.31 bits per second per hertz for 10 dB.')


# ---- 7.5 the repetition code of the worked example, and R against C ----
def f5():
    o = []
    xs = [16, 166, 316, 466, 606]
    labs = [['message bit', '1'], ['repeat ×3', '1 1 1'], ['BSC', 'p = 0.01'], ['received', '1 0 1'], ['majority', '→ 1']]
    for i, lines in enumerate(labs):
        o.append(boxt(xs[i], 40, 104 if i < 4 else 98, 60, lines, ACS if i in (0, 4) else (NXS if i == 2 else PANEL), NX if i == 2 else AC, 14, bold_first=True))
        if i < 4: o.append(arrow(xs[i] + 104, 70, xs[i + 1] - 4, 70))
    o.append(T(360, 132, 'One copy flipped: the vote still gives 1. It fails only if 2 or 3 copies flip:', 14))
    o.append(T(360, 158, 'P_b = 3p²(1 − p) + p³ = 2.98 × 10⁻⁴, 33.6 times below p', 14, bold=True).replace('P_b', 'P<tspan font-size="11" dy="4">b</tspan><tspan dy="-4">​</tspan>'))
    # rate axis
    x0, x1, y = 60, 660, 250
    fx = lambda r: x0 + r * (x1 - x0)
    o.append(R(fx(0), y - 16, fx(0.919) - fx(0), 32, ACS, ACS, 0, 0))
    o.append(R(fx(0.919), y - 16, fx(1) - fx(0.919), 32, NXS, NXS, 0, 0))
    o.append(xaxis(x0, x1, y + 16, [0, 0.2, 0.4, 0.6, 0.8, 1], fx, 'code rate R in bits per channel use', fmt=lambda v: f'{v:g}'))
    o.append(T(fx(0.62), y + 5, 'R < C: reliable codes exist', 14, fill=AC, bold=True))
    o.append(L(fx(0.919), y - 30, fx(0.919), y + 16, NX, 2.5)); o.append(T(fx(0.919), y - 36, 'C = 0.919', 14, fill=NX, bold=True))
    o.append(L(fx(1 / 3), y - 30, fx(1 / 3), y + 16, INK, 2.5)); o.append(T(fx(1 / 3), y - 36, 'repetition R = 1/3', 14, bold=True))
    return 330, ''.join(o)

FIG[5] = (f5, 'The worked example\'s 3-fold repetition code on a BSC with p = 0.01: a single flipped copy is outvoted, so the decoded error falls to 2.98 × 10⁻⁴. Its rate 1/3 sits far below the capacity 0.919, which is the room a better long code would use.',
          'Top, five blocks in a row: message bit 1, repeat three times to 1 1 1, binary symmetric channel with p 0.01, received 1 0 1, majority vote gives 1. Bottom, a rate axis from 0 to 1 shaded up to the capacity 0.919, with the repetition rate one third marked.')


# ---- 7.6 one bit error found by the syndrome ----
def f6():
    o = []
    cw = 30
    def word(x, y, bits, hi=None, fill=PANEL):
        out = []
        for i, b in enumerate(bits):
            f = NXS if hi is not None and i == hi else fill
            out.append(R(x + i * cw, y, cw, 32, f, AC if f != NXS else NX, 2, 1.5)); out.append(TM(x + i * cw + cw / 2, y + 22, b, 15, bold=True))
        return ''.join(out)
    rows = [('message m', '1011', None, 'c = mG: rows 1, 3, 4 of G'), ('codeword c', '1011010', None, 'sent'), ('received r', '1010010', 3, 'the channel flips bit 4'),
            ('corrected r ⊕ e', '1011010', 3, 'flip bit 4 back: c restored')]
    for j, (lab, bits, hi, note) in enumerate(rows):
        y = 30 + j * 70 if j < 3 else 324
        o.append(T(130, y + 22, lab, 14, 'end', bold=True))
        o.append(word(146, y, bits, hi, ACS if j == 3 else PANEL))
        o.append(T(146 + len(bits) * cw + 12, y + 22, note, 13, 'start', MUT))
        if j in (0, 1): o.append(arrow(146 + 2 * cw, y + 36, 146 + 2 * cw, y + 66, L2, 1.8, 'm'))
    for i in range(7): o.append(T(146 + i * cw + cw / 2, 24, str(i + 1), 13, fill=MUT))
    # H columns
    hx, hy = 146, 262
    o.append(T(130, 236, 's = rHᵀ', 14, 'end', bold=True)); o.append(T(130, 256, '= 111', 14, 'end', NX, True))
    o.append(T(hx, 236, 'columns of H:', 13, 'start', MUT))
    cols = ['110', '101', '011', '111', '100', '010', '001']
    for i, c in enumerate(cols):
        f = NXS if i == 3 else PANEL
        o.append(R(hx + i * cw, hy - 20, cw, 54, f, NX if i == 3 else L2, 2, 1.5))
        for r, b in enumerate(c): o.append(TM(hx + i * cw + cw / 2, hy - 4 + r * 16, b, 13))
    o.append(arrow(146 + 3 * cw + 15, 206, 146 + 3 * cw + 15, hy - 24, NX, 1.8, 'x'))
    o.append(T(hx + 7 * cw + 12, hy + 4, 's matches column 4,', 13, 'start', NX, True)); o.append(T(hx + 7 * cw + 12, hy + 22, 'so e = 0001000', 13, 'start', NX, True))
    return 372, ''.join(o)

FIG[6] = (f6, 'Worked example 1 bit by bit: 1011 encodes to 1011010, the channel flips bit 4, and the syndrome 111 equals column 4 of H, which names the wrong bit; flipping it back restores the codeword.',
          'Rows of bit cells numbered 1 to 7: message 1011, codeword 1011010, received 1010010 with bit 4 highlighted. Below, the seven columns of H, 110, 101, 011, 111, 100, 010, 001, with column 4 highlighted as matching the syndrome 111. Last row: the corrected word 1011010.')


# ---- 7.7 the long division of worked example 1 ----
def f7():
    o = []
    cw, x0 = 26, 150
    col = lambda i: x0 + i * cw + cw / 2   # bit column 0..6 of the dividend
    o.append(T(20, 30, 'x³m(x) ÷ g(x), every subtraction an XOR', 15, 'start', bold=True))
    for i, b in enumerate('1111'): o.append(TM(col(3 + i), 62, b, 15, fill=AC, bold=True))
    o.append(T(col(6) + 30, 62, 'quotient x³ + x² + x + 1', 13, 'start', AC))
    o.append(L(x0 - 4, 72, x0 + 7 * cw + 4, 72, INK, 1.5)); o.append(TM(x0 - 14, 92, ')', 17))
    o.append(TM(x0 - 58, 92, '1011', 15, bold=True))
    for i, b in enumerate('1101000'): o.append(TM(col(i), 92, b, 15, bold=(i < 4)))
    o.append(T(col(6) + 30, 92, 'message 1101, shifted by 3', 13, 'start', MUT))
    y = 92
    for start, nxt in ((0, '1100'), (1, '1110'), (2, '1010'), (3, '001')):
        y += 26
        for i, b in enumerate('1011'): o.append(TM(col(start + i), y, b, 15, fill=NX))
        o.append(L(col(start) - 12, y + 7, col(start + 3) + 12, y + 7, L2, 1.5))
        y += 24
        last = len(nxt) == 3
        for i, b in enumerate(nxt): o.append(TM(col(start + 1 + i), y, b, 15, fill=(AC if last else INK), bold=last))
    o.append(T(col(6) + 30, y, 'remainder 001 = b(x) = 1', 14, 'start', AC, True))
    # codeword
    cy = y + 50
    o.append(T(20, cy + 22, 'codeword', 14, 'start', bold=True))
    for i, b in enumerate('1101001'):
        o.append(R(x0 + i * 34, cy, 34, 34, ACS if i < 4 else LVS, AC if i < 4 else LV, 2, 1.5)); o.append(TM(x0 + i * 34 + 17, cy + 23, b, 15, bold=True))
    o.append(brace(x0 + 2, x0 + 4 * 34 - 2, cy + 42)); o.append(T(x0 + 68, cy + 66, 'message 1101', 13, fill=MUT))
    o.append(brace(x0 + 4 * 34 + 2, x0 + 7 * 34 - 2, cy + 42)); o.append(T(x0 + 5.5 * 34, cy + 66, 'parity 001', 13, fill=LV))
    o.append(T(x0 + 7 * 34 + 20, cy + 22, '= x⁶ + x⁵ + x³ + 1, divides by g(x) exactly', 13, 'start', MUT))
    return cy + 84, ''.join(o)

FIG[7] = (f7, 'The division of worked example 1 written out: 1101000 divided by 1011 (g(x) = x³ + x + 1) with XOR in place of subtraction leaves 001, and appending it to the message gives the codeword 1101001.',
          'A binary long division: 1011 into 1101000. Four XOR steps leave 110, then 111, then 101, then the remainder 001; the quotient is 1111. Below, the codeword 1101001 drawn as seven cells, the first four marked message 1101 and the last three parity 001.')


# ---- 7.8 the Viterbi trellis of worked example 1 ----
def f8():
    o = []
    states = ['00', '10', '01', '11']
    X = lambda t: 100 + t * 96; Y = lambda s: 100 + states.index(s) * 70
    nxt = {('00', 0): ('00', '00'), ('00', 1): ('10', '11'), ('10', 0): ('01', '10'), ('10', 1): ('11', '01'),
           ('01', 0): ('00', '11'), ('01', 1): ('10', '00'), ('11', 0): ('01', '01'), ('11', 1): ('11', '10')}
    reach = [{'00'}]
    for t in range(6):
        r = set()
        for s in reach[-1]:
            for u in ((0,) if t >= 4 else (0, 1)): r.add(nxt[(s, u)][0])
        reach.append(r)
    path = ['00', '10', '01', '10', '11', '01', '00']
    rx = ['11', '10', '00', '11', '01', '11']
    metric = [{'00': 0}, {'00': 2, '10': 0}, {'00': 3, '10': 3, '01': 0, '11': 2}, {'00': 2, '10': 0, '01': 3, '11': 3},
              {'00': 3, '10': 2, '01': 1, '11': 1}, {'00': 2, '01': 1}, {'00': 1}]
    for s in states: o.append(T(40, Y(s) + 5, s, 14, bold=True))
    o.append(T(40, 52, 'state', 13, fill=MUT))
    for t in range(6):
        o.append(TM((X(t) + X(t + 1)) / 2, 58, rx[t], 15, fill=NX if t == 3 else INK, bold=True))
        for s in reach[t]:
            for u in ((0,) if t >= 4 else (0, 1)):
                ns, out = nxt[(s, u)]
                on = path[t] == s and path[t + 1] == ns
                o.append(L(X(t) + 12, Y(s), X(t + 1) - 14, Y(ns), AC if on else L2, 4 if on else 1.5, None if u == 0 else '6 4'))
    o.append(T(30, 30, 'received', 13, 'start', MUT))
    for t in range(7):
        for s in reach[t]:
            on = path[t] == s
            o.append(f'<circle cx="{X(t):.1f}" cy="{Y(s):.1f}" r="13" style="fill:{ACS if on else PANEL};stroke:{AC if on else L2};stroke-width:2"/>')
            o.append(T(X(t), Y(s) + 5, str(metric[t][s]), 13, bold=on))
        o.append(T(X(t), 390, f't = {t}', 13, fill=MUT))
    o.append(T(X(3.5), 410, 'error here: 11 received, path branch 01, cost 1', 13, fill=NX))
    o.append(L(470, 432, 500, 432, L2, 1.5)); o.append(T(508, 437, 'input 0', 13, 'start', MUT))
    o.append(L(580, 432, 610, 432, L2, 1.5, '6 4')); o.append(T(618, 437, 'input 1', 13, 'start', MUT))
    o.append(L(80, 432, 110, 432, AC, 4)); o.append(T(118, 437, 'survivor traced back: 1 0 1 1 (0 0), metric 1', 13, 'start', AC, True))
    return 454, ''.join(o)

FIG[8] = (f8, 'The trellis of worked example 1. Each circle holds the smallest path metric into that state; the thick path, traced back from 00 at the end, costs only 1 (at the fourth pair, where the channel flipped a bit) and decodes to 1011.',
          'A trellis with states 00, 10, 01, 11 down the side and times 0 to 6 across, received pairs 11, 10, 00, 11, 01, 11 on top. Solid branches are input 0 and dashed are input 1. Path metrics are written in the circles; the survivor path 00, 10, 01, 10, 11, 01, 00 is drawn thick with metrics 0, 0, 0, 0, 1, 1, 1.')


# ---- 7.9 the turbo encoder of the worked example ----
def f9():
    o = []
    o.append(T(20, 104, 'block d', 14, 'start', bold=True))
    o.append(L(90, 100, 130, 100, AC, 2.5))
    o.append(f'<circle cx="130" cy="100" r="4" style="fill:var(--accent)"/>')
    o.append(boxt(200, 130, 140, 54, ['RSC encoder 1'], PANEL, AC, 14)); o.append(boxt(170, 230, 70, 54, ['π'], NXS, NX, 17, bold_first=True))
    o.append(boxt(290, 230, 140, 54, ['RSC encoder 2'], PANEL, AC, 14))
    o.append(boxt(500, 70, 90, 214, ['MUX'], ACS, AC, 15, bold_first=True))
    o.append(L(130, 100, 130, 257, AC, 2)); o.append(arrow(130, 157, 196, 157)); o.append(arrow(130, 257, 166, 257)); o.append(arrow(240, 257, 286, 257))
    o.append(arrow(130, 100, 496, 100, AC, 2, 'n', '7 5'))
    o.append(Tb(320, 94, 'systematic d, sent once', 13, fill=MUT))
    o.append(arrow(340, 157, 496, 157)); o.append(T(420, 150, 'parity p1', 13, bold=True))
    o.append(arrow(430, 257, 496, 257)); o.append(T(462, 250, 'p2', 13, bold=True))
    o.append(T(205, 306, 'interleaver: same bits, new order', 13, fill=NX))
    o.append(arrow(590, 177, 640, 177)); o.append(T(648, 172, 'd p1 p2', 14, 'start', bold=True))
    o.append(T(20, 346, '3 bits per input bit: R = 1/3.  Puncture half of p1 and half of p2: 1 + 0.5 + 0.5 = 2 bits, R = 1/2.', 14, 'start', AC, True))
    return 372, ''.join(o)

FIG[9] = (f9, 'The turbo encoder of the worked example: the block goes out once as it is, once through encoder 1 and once, reordered by the interleaver π, through encoder 2. Three bits per input bit give R = 1/3; deleting half of each parity stream gives R = 1/2.',
          'Block diagram. The input block d splits three ways: straight to a multiplexer as the systematic bits, into recursive systematic convolutional encoder 1 giving parity p1, and through an interleaver pi into encoder 2 giving parity p2. The multiplexer sends d, p1, p2. A note gives rate one third, and one half after puncturing.')

spec = make_spec(FIG)
