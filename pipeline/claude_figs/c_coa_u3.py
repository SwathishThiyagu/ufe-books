"""Claude's hand-drawn figures for c-coa-u3 (Computer Organization and Architecture, unit 3: computer arithmetic and ALU
design), one per chapter, from each chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


# ---- 3.1 one byte, two readings, then sign extension ----
def f1():
    x0, w = 170, 60
    bits = '11010011'
    o = [T(20, 26, 'The byte 1101 0011 read two ways', 15, 'start', bold=True)]
    for i, b in enumerate(bits):
        o.append(boxt(x0 + i * w + 2, 44, w - 4, 40, [b], ACS if b == '1' else PANEL, AC if b == '1' else L2, 17, bold_first=True))
    o.append(T(160, 69, 'bits', 14, 'end', bold=True))
    for r, (lab, ws) in enumerate((('unsigned', ['128', '64', '32', '16', '8', '4', '2', '1']),
                                   ('signed', ['−128', '64', '32', '16', '8', '4', '2', '1']))):
        y = 108 + r * 44
        o.append(T(160, y + 21, lab + ' weights', 13, 'end', bold=True))
        for i, wt in enumerate(ws):
            on = bits[i] == '1'
            st = LV if (r == 1 and i == 0) else (AC if on else LN)
            o.append(R(x0 + i * w + 2, y, w - 4, 32, ACS if on else PANEL, st, 5, 1.5))
            o.append(TM(x0 + i * w + w / 2, y + 21, wt, 14, fill=(LV if r == 1 and i == 0 else (INK if on else MUT)), bold=on))
    o.append(T(20, 224, 'unsigned: 128 + 64 + 16 + 2 + 1 = 211', 14, 'start', AC, True))
    o.append(T(20, 246, 'signed: −128 + 64 + 16 + 2 + 1 = −45   (check: 211 − 256 = −45)', 14, 'start', LV, True))
    o.append(T(20, 290, 'Widen to 16 bits: copy the sign bit into the eight new bits', 15, 'start', bold=True))
    bx, bw = 90, 36
    for i, b in enumerate('1111111111010011'):
        new = i < 8
        o.append(R(bx + i * bw + 1, 304, bw - 2, 34, LVS if new else (ACS if b == '1' else PANEL), LV if new else (AC if b == '1' else L2), 4, 1.5))
        o.append(TM(bx + i * bw + bw / 2, 326, b, 15, bold=True))
    o.append(brace(bx + 2, bx + 8 * bw - 2, 348, LV))
    o.append(T(bx + 4 * bw, 372, 'copies of the sign bit', 13, fill=LV))
    o.append(T(bx + 12 * bw, 372, 'the original byte', 13, fill=MUT))
    o.append(T(20, 404, '0xFFD3 = 65,491 unsigned, and 65,491 − 65,536 = −45: the value is unchanged.', 14, 'start'))
    return 418, ''.join(o)
FIG[1] = (f1, 'The same bits 1101 0011 give 211 when the top bit weighs +128 and −45 when it weighs −128 (two\'s complement). Copying the sign bit into eight new bits widens it to 0xFFD3, which is still −45.',
          'Eight bit cells 1 1 0 1 0 0 1 1 over two rows of weights, 128 down to 1 and −128 down to 1, with the weights of the 1 bits shaded; below, the 16-bit sign-extended pattern 1111 1111 1101 0011.')


# ---- 3.2 three additions and their overflow flag ----
def f2():
    cases = [('(a) 75 − 33', [('A (+75)', '0100 1011'), ('B inverted', '1101 1110'), ('carry-in', '1')], '1', '0010 1010', 'c8 = 1, c7 = 1', 'V = 1 ⊕ 1 = 0', '+42, correct', False),
             ('(b) 100 + 50', [('A (+100)', '0110 0100'), ('B (+50)', '0011 0010'), ('carry-in', '0')], '0', '1001 0110', 'c8 = 0, c7 = 1', 'V = 0 ⊕ 1 = 1', 'reads −106: overflow', True),
             ('(c) (−100) + (−50)', [('A (−100)', '1001 1100'), ('B (−50)', '1100 1110'), ('carry-in', '0')], '1', '0110 1010', 'c8 = 1, c7 = 0', 'V = 1 ⊕ 0 = 1', 'reads +106: overflow', True)]
    o = []
    for i, (title, rows, c8, s, cc, v, verdict, bad) in enumerate(cases):
        x = 8 + i * 238
        o.append(R(x, 14, 228, 272, PANEL, LN, 10, 1.2))
        o.append(T(x + 114, 40, title, 15, bold=True))
        for r, (lab, val) in enumerate(rows):
            y = 74 + r * 28
            o.append(T(x + 12, y, lab, 13, 'start', MUT))
            o.append(TM(x + 214, y, val, 15, 'end'))
        o.append(L(x + 120, 142, x + 216, 142, INK, 1.5))
        o.append(TM(x + 214, 166, s, 15, 'end', bold=True))
        o.append(TM(x + 122, 166, c8, 15, 'end', LV if c8 == '1' else MUT, bold=True))
        o.append(T(x + 12, 166, 'sum', 13, 'start', MUT))
        o.append(T(x + 114, 198, cc, 14))
        o.append(T(x + 114, 222, v, 14, bold=True, fill=LV if bad else NX))
        o.append(boxt(x + 14, 238, 200, 34, [verdict], LVS if bad else NXS, LV if bad else NX, 14, bold_first=True))
    o.append(T(360, 314, 'V = c8 ⊕ c7: overflow when the carry into the sign bit differs from the carry out of it.', 14, bold=True))
    o.append(T(360, 336, 'The carry out c8 (left of the sum) is dropped; for signed numbers it is not the overflow signal.', 13, fill=MUT))
    return 350, ''.join(o)
FIG[2] = (f2, 'Three 8-bit additions on the same adder. 75 − 33 adds the inverted B plus 1 and gives +42 with V = 0; 100 + 50 and (−100) + (−50) set V = 1 because the carry into the sign bit differs from the carry out.',
          'Three panels of binary column additions, each with the carries c8 and c7, the overflow flag V and a verdict: +42 correct, then two overflows reading −106 and +106.')


# ---- 3.3 the carry-lookahead example bit by bit ----
def f3():
    col = lambda i: 220 + (3 - i) * 112
    o0 = T(20, 26, 'Adding A = 1011 (11) and B = 0110 (6) with carry lookahead, c0 = 0', 15, 'start', bold=True)
    rows = [('a', '1011', None), ('b', '0110', None), ('g = a · b', '0010', 'g'), ('p = a ⊕ b', '1101', 'p'),
            ('carry in c', '1100', 'c'), ('s = p ⊕ c', '0001', None)]
    o = []
    for i in range(4):
        o.append(T(col(i) + 48, 44, f'bit {i}', 13, fill=MUT))
    for r, (lab, v, kind) in enumerate(rows):
        y = 56 + r * 44
        o.append(T(206, y + 22, lab, 14, 'end', bold=True))
        for i in range(4):
            d = v[3 - i]
            hot = (kind == 'g' and i == 1) or (kind == 'p' and i in (2, 3)) or (kind == 'c' and i in (2, 3))
            f, st = (NXS, NX) if (hot and kind in ('g', 'c')) else ((ACS, AC) if hot else (PANEL, L2))
            o.append(R(col(i), y, 96, 34, f, st, 5, 1.5))
            o.append(TM(col(i) + 48, y + 23, d, 16, bold=hot))
    o.append(o0)
    o.append(boxt(96, 232, 112, 34, ['c4 = 1'], NXS, NX, 14, bold_first=True))
    o.append(T(20, 342, 'c4 = g3 + p3·g2 + p3·p2·g1 + p3·p2·p1·g0 + … = 0 + 0 + 1·1·1 + 0 = 1', 14, 'start'))
    o.append(T(20, 366, 'Sum = 1 0001 = 17 (11 + 6). Group: G = 1, P = p3·p2·p1·p0 = 0.', 14, 'start', bold=True))
    o.append(T(20, 390, 'Bit 1 generates a carry (green) and bits 2 and 3 propagate it (blue), so every carry is known at once.', 13, 'start', MUT))
    return 404, ''.join(o)
FIG[3] = (f3, 'Adding 1011 + 0110 with lookahead: bit 1 generates a carry and bits 2 and 3 propagate it, so c2, c3 and c4 are all 1 and can be computed at the same time from g and p. The sum is 1 0001 = 17.',
          'A grid with bits 3 to 0 across and rows a, b, generate, propagate, carry in and sum; generate at bit 1 and the carries into bits 2 and 3 and out of bit 3 are shaded green, propagate at bits 2 and 3 blue.')


# ---- 3.4 13 x 11 as shifted partial products ----
def f4():
    cx = lambda j: 470 - j * 34
    def num(y, bits, shift, fill=INK, size=18):
        o = []
        for k, b in enumerate(reversed(bits)):
            o.append(TM(cx(k + shift), y, b, size, fill=fill, bold=True))
        return ''.join(o)
    o = [T(20, 26, 'Multiply M = 1101 (13) by Q = 1011 (11)', 15, 'start', bold=True)]
    o.append(T(40, 62, 'multiplicand M', 13, 'start', MUT)); o.append(num(62, '1101', 0)); o.append(T(510, 62, '13', 14, 'start', MUT))
    o.append(T(40, 94, 'multiplier Q', 13, 'start', MUT)); o.append(TM(cx(4), 94, '×', 18, fill=MUT)); o.append(num(94, '1011', 0))
    o.append(T(510, 94, '11', 14, 'start', MUT))
    o.append(L(cx(7) - 14, 108, cx(0) + 14, 108, INK, 1.5))
    pps = [('1101', 0, 'q0 = 1: copy M'), ('1101', 1, 'q1 = 1: M shifted 1'), ('0000', 2, 'q2 = 0: zero'), ('1101', 3, 'q3 = 1: M shifted 3')]
    for r, (b, sh, note) in enumerate(pps):
        y = 136 + r * 32
        zero = b == '0000'
        o.append(num(y, b, sh, MUT if zero else AC))
        o.append(T(510, y, note, 13, 'start', MUT if zero else AC))
    o.append(T(40, 152, 'partial products', 13, 'start', MUT))
    o.append(L(cx(7) - 14, 248, cx(0) + 14, 248, INK, 1.5))
    o.append(num(278, '10001111', 0, INK, 18))
    o.append(T(40, 278, 'product', 13, 'start', MUT))
    o.append(T(510, 278, '128 + 15 = 143', 14, 'start', bold=True))
    o.append(T(20, 322, 'The sequential multiplier adds one of these rows per cycle and shifts right; after 4 cycles', 14, 'start'))
    o.append(T(20, 344, 'A and Q together hold 1000 1111. The extra bit C catches the adder\'s carry in cycles 2 and 4.', 14, 'start'))
    return 358, ''.join(o)
FIG[4] = (f4, 'Each 1 bit of the multiplier 1011 contributes a copy of 1101 shifted to its place, and the 0 bit contributes nothing. The four rows add to 1000 1111 = 143 = 13 × 11.',
          'Binary long multiplication of 1101 by 1011: four partial product rows, three of them shifted copies of 1101 and one of zeros, adding to 10001111.')


# ---- 3.5 Booth recoding of Q = 1101 ----
def f5():
    x0, w = 130, 112
    labs = ['Q3', 'Q2', 'Q1', 'Q0', 'Q−1']
    bits = ['1', '1', '0', '1', '0']
    o = [T(20, 26, 'Booth looks at each bit with the bit to its right (a 0 is added after Q0)', 15, 'start', bold=True)]
    for i, (l, b) in enumerate(zip(labs, bits)):
        o.append(T(x0 + i * w + 52, 54, l, 13, fill=MUT))
        o.append(boxt(x0 + i * w, 62, 104, 40, [b], PANEL if i == 4 else ACS, L2 if i == 4 else AC, 18, bold_first=True, dash='5 4' if i == 4 else None))
    o.append(T(120, 87, 'Q = −3', 14, 'end', bold=True))
    acts = [('11', 'nothing', '0', PANEL, L2), ('10', '−M × 4', '−28', LVS, LV), ('01', '+M × 2', '+14', NXS, NX), ('10', '−M × 1', '−7', LVS, LV)]
    o.append(T(120, 136, 'pair', 13, 'end', MUT)); o.append(T(120, 182, 'action', 13, 'end', MUT))
    for i, (p, a, v, f, st) in enumerate(acts):
        x = x0 + i * w
        o.append(TM(x + 52, 136, p, 15, bold=True))
        o.append(boxt(x, 152, 104, 50, [a, v], f, st, 14, bold_first=False))
    o.append(T(360, 238, 'M = +7:   −7 + 14 − 28 + 0 = −21', 16, bold=True))
    o.append(T(360, 266, 'Registers after 4 cycles: A Q = 1110 1011 = −21 = 7 × (−3)', 14))
    o.append(T(360, 296, 'Pair 10 starts a run of 1s (subtract), 01 ends it (add); 00 and 11 cost only a shift.', 13, fill=MUT))
    return 310, ''.join(o)
FIG[5] = (f5, 'Booth\'s algorithm reads Q = 1101 in overlapping pairs: 10 means subtract M, 01 means add M and 11 means do nothing, each at its bit\'s weight. For M = 7 that is −7 + 14 − 28 = −21 = 7 × (−3).',
          'The bits of Q = 1101 with an extra 0 on the right; under each bit its pair with the next bit and the action, nothing, minus 4M, plus 2M and minus M, summing to minus 21.')


# ---- 3.6 operations of restoring and non-restoring division ----
def f6():
    x0, w = 176, 106
    o = [T(x0 + c * w + 48, 36, f'cycle {c + 1}' if c < 4 else 'end', 13, fill=MUT) for c in range(5)]
    rest = [(['A − M < 0', 'restore'], '0'), (['A − M < 0', 'restore'], '0'), (['A − M ≥ 0'], '1'), (['A − M < 0', 'restore'], '0')]
    o += [T(20, 70, 'Restoring', 15, 'start', bold=True), T(20, 90, '4 subtracts', 13, 'start', MUT), T(20, 106, '+ 3 restores = 7', 13, 'start', LV, True)]
    for c, (ops, q) in enumerate(rest):
        x = x0 + c * w
        for j, op in enumerate(ops):
            undo = op == 'restore'
            ok = '≥' in op
            o.append(boxt(x, 48 + j * 34, 98, 28, [op], LVS if undo else (NXS if ok else PANEL), LV if undo else (NX if ok else AC), 13, rx=5, dash='5 3' if undo else None))
        o.append(T(x + 49, 132, 'q = ' + q, 13, fill=MUT))
    o.append(T(x0 + 4 * w + 49, 70, '—', 14, fill=MUT))
    o.append(L(20, 150, 700, 150, LN, 1))
    nonr = [('A − M', '0'), ('A + M', '0'), ('A + M', '1'), ('A − M', '0'), ('A + M', 'fix')]
    o += [T(20, 184, 'Non-restoring', 15, 'start', bold=True), T(20, 204, '4 operations', 13, 'start', MUT), T(20, 220, '+ 1 correction = 5', 13, 'start', NX, True)]
    for c, (op, q) in enumerate(nonr):
        x = x0 + c * w
        fix = q == 'fix'
        o.append(boxt(x, 170, 98, 28, [op], NXS if fix else PANEL, NX if fix else AC, 13, rx=5))
        o.append(T(x + 49, 220, 'fix remainder' if fix else 'q = ' + q, 13, fill=MUT))
    o.append(T(20, 266, 'Both give 11 ÷ 4: quotient 0010 = 2 and remainder 00011 = 3 (check: 2 × 4 + 3 = 11).', 14, 'start', bold=True))
    o.append(T(20, 290, 'Non-restoring never undoes a step: a negative A is fixed by adding M in the next cycle instead.', 14, 'start'))
    return 304, ''.join(o)
FIG[6] = (f6, 'Dividing 11 by 4 in four cycles. Restoring division subtracts every cycle and adds M back three times (7 operations); non-restoring does one add or subtract per cycle plus one final remainder fix (5 operations).',
          'Two rows of cycle boxes: restoring has a subtract in each of 4 cycles and a dashed restore in cycles 1, 2 and 4; non-restoring has subtract, add, add, subtract and a final add to fix the remainder.')


# ---- 3.7 -6.75 in IEEE 754 single precision ----
def f7():
    x0, bw = 40, 20
    bits = '1' + '10000001' + '1011' + '0' * 19
    o = [T(20, 26, '−6.75 = −110.11 (binary) = −1.1011 × 2²', 15, 'start', bold=True)]
    fields = [(0, 1, 'S = 1', LVS, LV), (1, 9, 'E = 2 + 127 = 129', ACS, AC), (9, 32, 'F = 1011 then 19 zeros (the 1 before the point is not stored)', NXS, NX)]
    for a, b, lab, f, st in fields:
        o.append(R(x0 + a * bw, 64, (b - a) * bw, 34, f, st, 4))
        o.append(T(x0 + (a + b) / 2 * bw, 56, lab, 13, fill=st, bold=True) if b - a > 1 else T(x0 + 10, 56, lab, 13, fill=st, bold=True))
    for i, b in enumerate(bits):
        o.append(TM(x0 + i * bw + 10, 86, b, 14, bold=True))
        if i: o.append(L(x0 + i * bw, 66 if i in (1, 9) else 88, x0 + i * bw, 96, st if False else L2, 1 if i not in (1, 9) else 2))
    for g, h in enumerate('C0D80000'):
        o.append(brace(x0 + g * 80 + 3, x0 + g * 80 + 77, 106, MUT))
        o.append(TM(x0 + g * 80 + 40, 132, h, 16, fill=AC, bold=True))
    o.append(T(x0 + 640, 160, '= 0xC0D80000', 15, 'end', AC, True))
    o.append(T(20, 200, 'Value = (−1)¹ × 1.1011 × 2^(129 − 127) = −1.1011 × 2² = −110.11 = −6.75', 14, 'start'))
    o.append(T(20, 236, 'Reading back 0x41200000: S = 0, E = 130 so e = 3, F = 01…, value = 1.01 × 2³ = 1010 = 10.0', 14, 'start'))
    o.append(T(20, 260, 'Double precision keeps the plan but biases the exponent by 1023: E = 2 + 1023 = 1025.', 13, 'start', MUT))
    return 274, ''.join(o)
FIG[7] = (f7, 'The 32 bits of −6.75: sign 1, exponent 2 stored as 129, and fraction 1011 from the significand 1.1011, whose leading 1 is not stored. Grouped in fours the bits read 0xC0D80000.',
          'A 32-cell bit strip divided into a 1-bit sign, an 8-bit exponent 10000001 and a 23-bit fraction 1011 followed by zeros, with the hex digits C 0 D 8 0 0 0 0 under groups of four bits.')


# ---- 3.8 aligning 9.75 + 0.5625 ----
def f8():
    pt = 300
    fx = lambda j: pt + 8 + (j - 0.5) * 26
    def row(y, ip, frac, fill, size=18):
        o = [TM(pt - 16, y, ip, size, fill=fill, bold=True), TM(pt, y, '.', size, fill=fill, bold=True)]
        for j, d in enumerate(frac, 1):
            o.append(TM(fx(j), y, d, size, fill=fill, bold=True))
        return ''.join(o)
    o = [T(20, 26, '9.75 + 0.5625: make the exponents equal, then add the significands', 15, 'start', bold=True)]
    o += [T(40, 74, 'A = 9.75', 14, 'start', bold=True), row(74, '1', '0011100', AC), T(520, 74, '× 2³   (E = 130)', 14, 'start', AC)]
    o += [T(40, 124, 'B = 0.5625', 14, 'start', bold=True), row(124, '1', '001', NX), T(520, 124, '× 2⁻¹   (E = 126)', 14, 'start', NX)]
    o.append(L(pt - 14, 132, fx(4) - 2, 160, NX, 2, arrow='x'))
    o.append(T(40, 150, 'shift right 130 − 126 = 4 places', 13, 'start', NX, True))
    o += [T(40, 178, 'B aligned', 14, 'start', bold=True), row(178, '0', '0001001', NX), T(520, 178, '× 2³', 14, 'start', NX)]
    o.append(L(pt - 30, 196, fx(7) + 16, 196, INK, 1.5))
    o += [T(40, 226, 'sum', 14, 'start', bold=True), row(226, '1', '0100101', INK), T(520, 226, '× 2³ = 10.3125', 14, 'start', bold=True)]
    o.append(T(20, 270, 'Normalise: already 1.xxx, so E stays 130. Round: 7 fraction bits fit in 23, nothing is lost.', 14, 'start'))
    o.append(T(20, 294, 'Result: 0 10000010 0100101 then 16 zeros = 0x41250000', 14, 'start', bold=True))
    return 308, ''.join(o)
FIG[8] = (f8, 'To add 9.75 and 0.5625 the smaller number is shifted right until both are × 2³, then the significands are added like integers. The sum 1.0100101 × 2³ is already normalised and exact: 10.3125 = 0x41250000.',
          'Binary significands lined up on their binary points: 1.0011100 times 2 cubed, 1.001 times 2 to the minus 1 shifted right four places to 0.0001001, and their sum 1.0100101 times 2 cubed.')


# ---- 3.9 the 4-bit arithmetic circuit for A = 6, B = 3 ----
def f9():
    o = [T(95, 40, 'S1 S0 picks Y', 13, fill=MUT, bold=True)]
    ys = [('00', 'Y = B = 0011'), ('01', 'Y = B̄ = 1100'), ('10', 'Y = 0000'), ('11', 'Y = 1111')]
    for i, (s, lab) in enumerate(ys):
        y = 54 + i * 42
        o.append(R(20, y, 150, 34, ACS if s == '01' else PANEL, AC, 6))
        o.append(TM(32, y + 22, s, 14, 'start', bold=True))
        o.append(TM(158, y + 22, lab.split(' = ', 1)[1] if s in ('10', '11') else lab[4:], 13, 'end'))
        o.append(L(172, y + 17, 198, y + 17, L2, 1.5, arrow='m'))
    o.append(P([(200, 50), (240, 76), (240, 196), (200, 222), (200, 50)], AC, 2, fill=PANEL))
    o.append(T(220, 141, 'mux', 13, bold=True))
    o.append(L(242, 136, 288, 136, AC, 2, arrow='n'))
    o.append(T(265, 128, 'Y', 13, fill=MUT))
    o.append(boxt(290, 96, 140, 80, ['adder', 'A + Y + Cin'], ACS, AC, 14, bold_first=True))
    o.append(T(360, 50, 'A = 0110 (6)', 14, bold=True)); o.append(L(360, 58, 360, 93, AC, 2, arrow='n'))
    o.append(T(360, 232, 'Cin = 0 or 1', 14, bold=True)); o.append(L(360, 216, 360, 179, AC, 2, arrow='n'))
    o.append(L(432, 136, 470, 136, AC, 2, arrow='n'))
    o += [T(566, 40, 'Cin = 0', 13, fill=MUT, bold=True), T(662, 40, 'Cin = 1', 13, fill=MUT, bold=True)]
    outs = [('1001 = 9', '1010 = 10'), ('0010 = 2', '0011 = 3'), ('0110 = 6', '0111 = 7'), ('0101 = 5', '0110 = 6')]
    for r, (a, b) in enumerate(outs):
        y = 54 + r * 42
        o.append(TM(510, y + 22, ys[r][0], 13, 'end', MUT))
        for c, v in enumerate((a, b)):
            hot = (r == 1 and c == 1) or (r == 0 and c == 0)
            o.append(R(520 + c * 96, y, 90, 34, NXS if hot else PANEL, NX if hot else L2, 5, 1.5))
            o.append(TM(565 + c * 96, y + 22, v, 13, bold=hot))
    o.append(T(20, 270, 'S = 01 with Cin = 1 computes A + B̄ + 1 = A − B: 6 − 3 = 3. S = 00 with Cin = 0 is plain A + B = 9.', 14, 'start'))
    o.append(T(20, 294, 'Y = 1111 is −1, so S = 11 with Cin = 0 gives A − 1 = 5; the same adder does all eight jobs.', 14, 'start'))
    return 308, ''.join(o)
FIG[9] = (f9, 'The select bits choose what the adder adds to A: B, its inverse, all 0s or all 1s, and Cin adds one more. For A = 6 and B = 3 the eight codes give 9, 10, 2, 3, 6, 7, 5 and 6, including A + B and A − B.',
          'Four choices for Y (B 0011, inverted B 1100, 0000 and 1111) feed a multiplexer and then an adder with A = 0110 and Cin; a table on the right gives the eight outputs for Cin 0 and 1.')


spec = make_spec(FIG)
