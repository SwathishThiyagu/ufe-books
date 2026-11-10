"""Claude's hand-drawn figures for c-sec-u2 (Cryptography and Network Security, unit 2: number theory for cryptography),
one per chapter, from each chapter's worked example."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


# ---- 2.1 square and multiply for 7^23 mod 13 ----
def f1():
    o = [T(20, 26, '7²³ mod 13, with 23 = 16 + 4 + 2 + 1 (binary 10111)', 15, 'start', bold=True),
         T(20, 48, 'each cell is the square of the one before, reduced mod 13', 13, 'start', MUT)]
    cells = [('7¹', '7', 1), ('7²', '49 ≡ 10', 1), ('7⁴', '100 ≡ 9', 1), ('7⁸', '81 ≡ 3', 0), ('7¹⁶', '9² = 81 ≡ 9', 1)]
    for i, (p, v, b) in enumerate(cells):
        x = 30 + i * 136
        o.append(boxt(x, 62, 116, 56, [p, v], ACS if b else PANEL, AC if b else L2, 14, bold_first=True))
        if i: o.append(L(x - 18, 90, x - 3, 90, L2, 1.8, arrow='m'))
        o.append(boxt(x + 28, 134, 60, 30, [f'bit {b}'], NXS if b else PANEL, NX if b else LN, 13, bold_first=bool(b), rx=5))
    o.append(T(20, 206, 'Multiply the cells whose bit is 1: 9 × 9 × 10 × 7, reducing after each step', 14, 'start', bold=True))
    steps = ['9 × 9 = 81 ≡ 3', '3 × 10 = 30 ≡ 4', '4 × 7 = 28 ≡ 2']
    for i, s in enumerate(steps):
        x = 30 + i * 224
        o.append(boxt(x, 222, 196, 40, [s], NXS if i == 2 else PANEL, NX if i == 2 else AC, 14, bold_first=i == 2))
        if i: o.append(L(x - 26, 242, x - 3, 242, AC, 2, arrow='n'))
    o.append(T(20, 300, '7²³ ≡ 2 (mod 13) after 4 squarings and 3 multiplications, never a number above 100.', 14, 'start', bold=True))
    return 314, ''.join(o)
FIG[1] = (f1, 'Squaring 7 again and again gives 7, 10, 9, 3, 9 for the powers 1, 2, 4, 8 and 16. The 1 bits of 23 pick 7¹⁶, 7⁴, 7² and 7¹, and their product reduces to 2.',
          'Five cells for 7 to the powers 1, 2, 4, 8 and 16 mod 13, each with the bit of 23 below it; four have bit 1 and are multiplied in three steps to give 2.')


# ---- 2.2 Euclid on 252 and 105 ----
def f2():
    x0, s = 150, 2.2
    o = []
    rows = [('252 = 2 × 105 + 42', [(105, ACS, AC), (105, ACS, AC), (42, LVS, LV)]),
            ('105 = 2 × 42 + 21', [(42, LVS, LV), (42, LVS, LV), (21, NXS, NX)]),
            ('42 = 2 × 21 + 0', [(21, NXS, NX), (21, NXS, NX)])]
    for r, (eq, parts) in enumerate(rows):
        y = 50 + r * 62
        o.append(TM(x0 - 10, y + 23, eq, 13, 'end', bold=True))
        c = 0
        for v, f, st in parts:
            o.append(boxt(x0 + c * s + 1, y, v * s - 2, 36, [str(v)], f, st, 14, bold_first=True, rx=3)); c += v
    o.append(T(20, 26, 'Each remainder becomes the next divisor; the last nonzero one is the gcd', 15, 'start', bold=True))
    cols = ['i', 'q', 'r', 's', 't']
    tx = 40
    for c, h in enumerate(cols):
        o.append(T(tx + c * 72 + 30, 258, h, 14, fill=MUT, bold=True))
    data = [('0', '', '252', '1', '0'), ('1', '', '105', '0', '1'), ('2', '2', '42', '1', '−2'), ('3', '2', '21', '−2', '5'), ('4', '2', '0', '5', '−12')]
    for r, row in enumerate(data):
        y = 266 + r * 26
        hot = r == 3
        o.append(R(tx - 6, y, 5 * 72, 24, NXS if hot else (PANEL if r % 2 == 0 else FIGBG), NX if hot else LN, 3, 1.2))
        for c, v in enumerate(row):
            o.append(TM(tx + c * 72 + 30, y + 17, v, 14, bold=hot))
    o.append(boxt(440, 266, 260, 126, ['gcd = 21, x = −2, y = 5', 'check:', '252 × (−2) + 105 × 5', '= −504 + 525 = 21'], NXS, NX, 14, bold_first=True))
    return 402, ''.join(o)
FIG[2] = (f2, 'Each division cuts the previous number into copies of the divisor plus a remainder: 42, then 21, then 0, so gcd(252, 105) = 21. The s and t columns in row 3 give the coefficients: 252 × (−2) + 105 × 5 = 21.',
          'Three bars: 252 split into 105, 105 and 42; 105 split into 42, 42 and 21; 42 split into 21 and 21. Below, the extended Euclid table with row 3 (r = 21, s = −2, t = 5) highlighted and the check.')


# ---- 2.3 the multiplication table of Z_7 ----
def f3():
    x0, y0, c = 40, 46, 40
    o = [T(20, 26, 'a × b mod 7: every row holds exactly one 1', 15, 'start', bold=True)]
    o.append(T(x0 + c / 2, y0 + 26, '×', 15, fill=MUT, bold=True))
    for i in range(1, 7):
        o.append(T(x0 + i * c + c / 2, y0 + 26, str(i), 14, fill=MUT, bold=True))
        o.append(T(x0 + c / 2, y0 + i * c + 26, str(i), 14, fill=MUT, bold=True))
        for j in range(1, 7):
            v = i * j % 7
            one = v == 1
            o.append(R(x0 + j * c + 1, y0 + i * c + 1, c - 2, c - 2, NXS if one else PANEL, NX if one else LN, 3, 1.2))
            o.append(TM(x0 + j * c + c / 2, y0 + i * c + 26, str(v), 14, fill=NX if one else INK, bold=one))
    x = 340
    o.append(T(x, 72, 'The 1 in each row is the inverse:', 14, 'start', bold=True))
    for k, (a, b) in enumerate(((1, 1), (2, 4), (3, 5), (4, 2), (5, 3), (6, 6))):
        o.append(TM(x + (k % 3) * 120, 100 + (k // 3) * 26, f'{a}⁻¹ = {b}', 14, 'start', fill=AC if a == 3 else INK, bold=a == 3))
    o.append(T(x, 170, '3⁻¹ = 5, because 3 × 5 = 15 = 2 × 7 + 1', 14, 'start', AC, True))
    o.append(T(x, 206, 'Z₇ is a field: 7 is prime, so every', 13, 'start'))
    o.append(T(x, 224, 'nonzero a has gcd(a, 7) = 1.', 13, 'start'))
    o.append(T(x, 260, 'Contrast Z₆: 2 × b mod 6 gives 2, 4, 0, 2, 4,', 13, 'start', LV))
    o.append(T(x, 278, 'never 1, so 2 has no inverse there.', 13, 'start', LV))
    return 334, ''.join(o)
FIG[3] = (f3, 'Each row of Z₇ has one 1, so every nonzero element has an inverse: 3 × 5 ≡ 1, so 3⁻¹ = 5.',
          'A 6 by 6 multiplication table modulo 7 with the single 1 in each row highlighted, next to the list of inverse pairs and the contrast with Z6.')


# ---- 2.4 Miller-Rabin on 341 with base 2 ----
def f4():
    o = [T(20, 26, 'Miller-Rabin: is 341 prime? Base a = 2', 15, 'start', bold=True)]
    boxes = [['n − 1 = 340', '= 2² × 85', 's = 2, d = 85'], ['x = 2⁸⁵ mod 341', '2¹⁰ = 1024 ≡ 1', 'so x = 2⁵ = 32'],
             ['x = 32', 'not 1, not 340:', 'keep squaring'], ['x² = 1024 ≡ 1', 'reached 1 from 32,', 'not from 340']]
    for i, lines in enumerate(boxes):
        x = 14 + i * 176
        o.append(boxt(x, 44, 160, 84, lines, LVS if i == 3 else PANEL, LV if i == 3 else AC, 13, bold_first=True))
        if i: o.append(L(x - 14, 86, x - 3, 86, AC, 2, arrow='n'))
    o.append(L(624, 130, 624, 160, LV, 2, arrow='l'))
    o.append(boxt(420, 162, 280, 44, ['composite: 341 = 11 × 31'], LVS, LV, 15, bold_first=True))
    o.append(T(20, 246, 'Why this proves it: modulo a prime p, the only square roots of 1 are 1 and p − 1.', 14, 'start'))
    o.append(T(20, 268, 'So squaring can reach 1 only from 1 or from 340. Here it came from 32: 32² ≡ 1 but 32 ≢ ±1.', 14, 'start'))
    o.append(T(20, 290, 'A prime would have shown x = 1 or x = 340 by this point.', 14, 'start', bold=True))
    return 304, ''.join(o)
FIG[4] = (f4, 'Write 340 = 2² × 85 and start from x = 2⁸⁵ ≡ 32 (mod 341). Squaring gives 1 from a value that is neither 1 nor 340, which cannot happen modulo a prime, so 341 = 11 × 31 is composite.',
          'Four boxes in a row: 340 = 4 × 85, x = 2 to the 85 = 32, 32 is neither 1 nor 340, and 32 squared is 1; an arrow leads to the verdict composite, 341 = 11 × 31.')


# ---- 2.5 powers of 3 mod 7 go round in a cycle of 6 ----
def f5():
    cx, cy, Rr = 190, 196, 120
    vals = {1: 3, 2: 2, 3: 6, 4: 4, 5: 5, 6: 1}
    pos = {k: (cx + Rr * math.cos(math.radians(-90 + k * 60)), cy + Rr * math.sin(math.radians(-90 + k * 60))) for k in range(1, 7)}
    o = [T(380, 70, 'Powers of 3 modulo 7', 15, 'start', bold=True)]
    for k in range(1, 7):
        nk = k % 6 + 1
        o.append(edge(pos[k], pos[nk], 26, -0.12, L2, 1.8, 'm'))
    for k in range(1, 7):
        x, y = pos[k]
        hot = k == 4
        o.append(state(x, y, str(vals[k]), r=26, fill=NXS if hot else (ACS if k == 6 else PANEL), stroke=NX if hot else AC, size=16))
        dx, dy = (x - cx) / Rr, (y - cy) / Rr
        o.append(T(x + dx * 46, y + dy * 46 + 5, f'3{"¹²³⁴⁵⁶"[k - 1]}', 14, fill=NX if hot else MUT, bold=True))
    o.append(T(cx, cy + 5, '× 3 each step', 13, fill=MUT))
    x = 380
    lines = [('3⁶ ≡ 1 (mod 7), so the powers repeat every 6 steps.', False, INK), ('100 = 6 × 16 + 4', True, INK),
             ('Go round the circle 16 times, then 4 more:', False, INK), ('3¹⁰⁰ = (3⁶)¹⁶ × 3⁴ ≡ 1 × 3⁴', False, INK),
             ('3⁴ = 81 = 11 × 7 + 4', False, INK), ('3¹⁰⁰ mod 7 = 4', True, NX)]
    for i, (s, b, f) in enumerate(lines):
        o.append(T(x, 110 + i * 30, s, 14 if not b else 15, 'start', f, b))
    return 378, ''.join(o)
FIG[5] = (f5, 'Multiplying by 3 modulo 7 walks round six values and returns to 1 after six steps, as Fermat\'s theorem promises. Since 100 = 6 × 16 + 4, 3¹⁰⁰ lands where 3⁴ does: on 4.',
          'Six circles on a ring holding 3, 2, 6, 4, 5 and 1, the values of 3 to the powers 1 to 6 modulo 7, with arrows round the ring; 3 to the 4, value 4, is highlighted.')


# ---- 2.6 Chinese remainder theorem for 3, 5, 7 ----
def f6():
    o = [T(20, 26, 'x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7);  M = 3 × 5 × 7 = 105', 15, 'start', bold=True)]
    cols = [('mod 3: a₁ = 2', ['M₁ = 105 ÷ 3 = 35', '35 ≡ 2 (mod 3)', 'y₁ = 2⁻¹ = 2'], '2 × 35 × 2 = 140'),
            ('mod 5: a₂ = 3', ['M₂ = 105 ÷ 5 = 21', '21 ≡ 1 (mod 5)', 'y₂ = 1'], '3 × 21 × 1 = 63'),
            ('mod 7: a₃ = 2', ['M₃ = 105 ÷ 7 = 15', '15 ≡ 1 (mod 7)', 'y₃ = 1'], '2 × 15 × 1 = 30')]
    for i, (h, lines, term) in enumerate(cols):
        x = 20 + i * 232
        o.append(boxt(x, 44, 216, 36, [h], ACS, AC, 14, bold_first=True))
        for j, s in enumerate(lines):
            o.append(T(x + 108, 104 + j * 22, s, 13))
        o.append(boxt(x + 18, 164, 180, 34, [term], PANEL, AC, 14))
        o.append(L(x + 108, 200, 360, 236, L2, 1.5, arrow='m'))
    o.append(boxt(200, 240, 320, 56, ['140 + 63 + 30 = 233', '233 mod 105 = 23'], NXS, NX, 15))
    o.append(T(360, 330, 'Check: 23 mod 3 = 2,  23 mod 5 = 3,  23 mod 7 = 2.  So x ≡ 23 (mod 105).', 14, bold=True))
    return 344, ''.join(o)
FIG[6] = (f6, 'Each congruence contributes one term aᵢ × Mᵢ × yᵢ, built so that it is right modulo its own number and 0 modulo the other two. The terms 140, 63 and 30 add to 233, which is 23 modulo 105.',
          'Three columns for the moduli 3, 5 and 7, each working out M, its inverse y and its term (140, 63 and 30); arrows lead to a sum box giving 233 and then 23 modulo 105.')


# ---- 2.7 squares modulo 11 ----
def f7():
    x0, w = 40, 64
    sq = [a * a % 11 for a in range(1, 11)]
    o = [T(20, 24, 'Square every a from 1 to 10, modulo 11', 15, 'start', bold=True)]
    o.append(T(30, 66, 'a', 14, 'end', bold=True)); o.append(T(30, 146, 'a²', 14, 'end', bold=True))
    for i in range(10):
        x = x0 + i * w
        o.append(boxt(x, 42, w - 8, 36, [str(i + 1)], PANEL, L2, 15))
        o.append(L(x + 28, 80, x + 28, 118, L2, 1.5, arrow='m'))
        o.append(boxt(x, 122, w - 8, 36, [str(sq[i])], ACS, AC, 15, bold_first=True))
    o.append(T(20, 186, 'a and 11 − a give the same square (1 and 10, 2 and 9, …), so only five values appear.', 13, 'start', MUT))
    o.append(T(20, 224, 'Which numbers are squares modulo 11?', 14, 'start', bold=True))
    res = {1, 3, 4, 5, 9}
    for i in range(10):
        x = x0 + i * w
        v = i + 1
        r = v in res
        o.append(boxt(x, 236, w - 8, 36, [str(v)], NXS if r else PANEL, NX if r else (LV if v == 2 else LN), 15, bold_first=r, dash=None if (r or v == 2) else '4 3'))
    o.append(T(x0 + 28, 292, 'residues: 1, 3, 4, 5, 9 (green)', 13, 'start', NX, True))
    o.append(T(x0 + 64 + 28, 310, '2 is missing', 13, 'middle', LV, True))
    o.append(T(20, 346, 'Euler: (2/11) ≡ 2^((11 − 1)/2) = 2⁵ = 32 = 2 × 11 + 10 ≡ −1, so (2/11) = −1.', 14, 'start', bold=True))
    return 360, ''.join(o)
FIG[7] = (f7, 'Squaring 1 to 10 modulo 11 gives only 1, 3, 4, 5 and 9, each twice. 2 is not among them, and Euler\'s criterion agrees: 2⁵ ≡ −1 (mod 11), so (2/11) = −1.',
          'Ten cells a = 1 to 10 with arrows to their squares mod 11 (1, 4, 9, 5, 3, 3, 5, 9, 4, 1); below, the numbers 1 to 10 with the residues 1, 3, 4, 5 and 9 shaded and 2 marked as missing.')


spec = make_spec(FIG)
