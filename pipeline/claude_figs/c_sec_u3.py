"""Claude's hand-drawn figures for c-sec-u3 (Cryptography and Network Security, unit 3: symmetric key cryptography),
one per chapter, from each chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def bitrow(x, y, bits, f=PANEL, st=L2, w=30, h=30, size=15, hot=None):
    o = []
    for i, b in enumerate(bits):
        ff, ss = (hot[i] if hot and hot[i] else (f, st))
        o.append(R(x + i * w + 1, y, w - 2, h, ff, ss, 3, 1.3))
        o.append(TM(x + i * w + w / 2, y + h * 0.68, b, size, bold=True))
    return ''.join(o)


def xor_sym(x, y, r=11, c=AC):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" style="fill:var(--panel);stroke:{c};stroke-width:2"/>'
            + L(x - r, y, x + r, y, c, 2) + L(x, y - r, x, y + r, c, 2))


# ---- 3.1 Caesar shift by 3 ----
def f1():
    x0, w = 22, 26
    A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    o = [T(20, 24, 'Caesar cipher, k = +3: each letter moves 3 places along the alphabet', 15, 'start', bold=True)]
    hot = {4: 'E', 23: 'X', 0: 'A', 12: 'M'}
    for i, ch in enumerate(A):
        x = x0 + i * w
        o.append(T(x + 13, 46, str(i), 13 if i < 10 else 13, fill=MUT) if i % 5 == 0 or i in hot or (i - 3) % 26 in hot else '')
        o.append(R(x + 1, 52, w - 2, 30, ACS if i in hot else PANEL, AC if i in hot else LN, 3, 1.2))
        o.append(TM(x + 13, 73, ch, 14, bold=i in hot))
        tgt = {(k + 3) % 26 for k in hot}
        o.append(R(x + 1, 150, w - 2, 30, NXS if i in tgt else PANEL, NX if i in tgt else LN, 3, 1.2))
        o.append(TM(x + 13, 171, ch, 14, bold=i in tgt))
    for k in hot:
        t = (k + 3) % 26
        if k == 23:
            o.append(P([(x0 + k * w + 13, 84), (x0 + k * w + 13, 110), (x0 + 25 * w + 20, 110)], LV, 2, '5 3'))
            o.append(P([(x0 - 8, 118), (x0 + t * w + 13, 118), (x0 + t * w + 13, 140)], LV, 2, '5 3'))
            o.append(L(x0 + t * w + 13, 136, x0 + t * w + 13, 147, LV, 2, arrow='l'))
            o.append(Tb(x0 + 23 * w - 30, 108, 'X: 23 + 3 = 26 ≡ 0, wraps to A', 13, fill=LV, bold=True))
        else:
            o.append(L(x0 + k * w + 13, 84, x0 + t * w + 13, 147, AC, 1.8, arrow='n'))
    o.append(T(10, 73, '', 13))
    o.append(T(20, 214, 'plaintext   E X A M  =  4, 23, 0, 12', 14, 'start'))
    o.append(T(20, 238, 'add 3 mod 26  →  7, 0, 3, 15  =  H A D P', 14, 'start', bold=True))
    o.append(T(20, 262, 'subtract 3 mod 26 from H A D P  →  4, 23, 0, 12  =  E X A M again', 14, 'start', NX))
    return 276, ''.join(o)
FIG[1] = (f1, 'Each letter of EXAM moves 3 places along the alphabet; X runs off the end and wraps round to A because 23 + 3 = 26 ≡ 0. The ciphertext is HADP, and moving back 3 places restores EXAM.',
          'Two alphabet strips with arrows from E, X, A and M in the top strip to H, A, D and P in the bottom strip, the X arrow wrapping round the end to A.')


# ---- 3.2 the one-time pad ----
def f2():
    x0 = 170
    rows = [('message m', '1011', '= 11', PANEL, L2), ('key k', '0110', '= 6', LVS, LV), ('c = m ⊕ k', '1101', '= 13', ACS, AC),
            ('c ⊕ k', '1011', '= 11 = m', NXS, NX)]
    o = [T(20, 24, 'One-time pad: XOR with a random key used only once', 15, 'start', bold=True)]
    for r, (lab, b, dec, f, st) in enumerate(rows):
        y = 44 + r * 56 + (12 if r == 3 else 0)
        o.append(T(x0 - 14, y + 25, lab, 14, 'end', bold=True))
        o.append(bitrow(x0, y, b, f, st, 50, 38, 18))
        o.append(T(x0 + 210, y + 26, dec, 15, 'start', st if st != L2 else INK, True))
        if r == 2: o.append(L(x0, y - 9, x0 + 200, y - 9, INK, 1.5))
    o.append(L(x0, 204, x0 + 200, 204, INK, 1.5, '4 3'))
    o.append(T(440, 72, 'XOR: equal bits give 0,', 13, 'start', MUT)); o.append(T(440, 90, 'different bits give 1', 13, 'start', MUT))
    o.append(T(440, 184, 'XOR with the same key twice', 13, 'start', MUT)); o.append(T(440, 202, 'undoes it: (m ⊕ k) ⊕ k = m', 13, 'start', MUT))
    o.append(T(20, 290, 'Every 4-bit message is equally likely to give 1101 under some key, so c alone says nothing about m.', 13, 'start'))
    return 304, ''.join(o)
FIG[2] = (f2, 'XORing m = 1011 with the key 0110 gives c = 1101 (13); XORing c with the same key gives back 1011 (11). Because the key is random and used once, the ciphertext reveals nothing about the message.',
          'Four rows of four bit cells: message 1011, key 0110, ciphertext 1101 and the decryption 1011, with their decimal values 11, 6, 13 and 11.')


# ---- 3.3 a stream cipher, byte by byte ----
def f3():
    x0 = 200
    o = [boxt(20, 40, 90, 40, ['seed'], LVS, LV, 14, bold_first=True), L(112, 60, 138, 60, LV, 2, arrow='l'),
         boxt(140, 34, 140, 52, ['PRG', 'stretches the seed'], PANEL, LV, 13, bold_first=True)]
    o.append(P([(282, 60), (480, 60), (480, 90)], LV, 2)); o.append(L(480, 88, 480, 100, LV, 2, arrow='l'))
    rows = [('keystream', '10110100', '180', LVS, LV), ('plaintext', '01100001', '97', PANEL, L2), ('ciphertext', '11010101', '213', ACS, AC),
            ('decrypted', '01100001', '97', NXS, NX)]
    ys = [104, 154, 214, 284]
    for (lab, b, dec, f, st), y in zip(rows, ys):
        o.append(bitrow(x0 + 120, y, b, f, st, 40, 32, 16))
        o.append(T(x0 + 120 + 8 * 40 + 12, y + 22, dec, 15, 'start', st if st != L2 else INK, True))
    o.append(T(x0 + 110, 126, 'keystream', 14, 'end', bold=True))
    o.append(T(x0 + 110, 176, 'plaintext', 14, 'end', bold=True))
    o.append(T(x0 + 110, 236, 'ciphertext', 14, 'end', bold=True))
    o.append(T(x0 + 110, 306, 'ct ⊕ keystream', 14, 'end', bold=True))
    o.append(xor_sym(x0 + 280, 200))
    o.append(L(x0 + 120, 196, x0 + 440, 196, INK, 1.2, '4 3'))
    o.append(T(20, 350, 'The same keystream decrypts: 11010101 ⊕ 10110100 = 01100001 = 97, the letter a.', 14, 'start'))
    o.append(T(20, 372, 'Never reuse it: two ciphertexts XORed together cancel the keystream and leak m₁ ⊕ m₂.', 13, 'start', LV))
    return 386, ''.join(o)
FIG[3] = (f3, 'A short seed drives the generator, whose keystream 10110100 is XORed bit by bit with the plaintext 01100001 to give 11010101 (213). XORing the ciphertext with the same keystream returns 97.',
          'A seed feeding a generator that produces the keystream 10110100; rows of eight bits for the keystream, plaintext 01100001, ciphertext 11010101 and the decrypted 01100001, with decimals 180, 97, 213 and 97.')


# ---- 3.4 one Feistel round ----
def f4():
    o = [boxt(80, 30, 180, 44, ['L₀ = 1010'], PANEL, AC, 16, bold_first=True), boxt(440, 30, 180, 44, ['R₀ = 0110'], PANEL, AC, 16, bold_first=True)]
    o.append(L(530, 76, 530, 104, AC, 2, arrow='n'))
    o.append(boxt(450, 106, 160, 44, ['F(R₀, K₁) = 0011'], ACS, AC, 14, bold_first=True))
    o.append(L(640, 128, 612, 128, LV, 2, arrow='l')); o.append(T(648, 133, 'K₁', 15, 'start', LV, True))
    o.append(L(448, 128, 183, 128, AC, 2, arrow='n'))
    o.append(L(170, 76, 170, 117, AC, 2))
    o.append(xor_sym(170, 128))
    o.append(T(300, 120, '0011', 14, fill=AC, bold=True))
    o.append(L(170, 139, 170, 160, AC, 2))
    o.append(L(530, 150, 530, 160, AC, 2))
    o.append(P([(170, 160), (530, 226)], NX, 2))
    o.append(P([(530, 160), (170, 226)], AC, 2))
    o.append(L(170, 226, 170, 244, AC, 2, arrow='n')); o.append(L(530, 226, 530, 244, NX, 2, arrow='x'))
    o.append(L(530, 150, 530, 160, AC, 2))
    o.append(boxt(80, 246, 180, 44, ['L₁ = R₀ = 0110'], NXS, NX, 15, bold_first=True))
    o.append(boxt(440, 246, 180, 44, ['R₁ = 1001'], NXS, NX, 15, bold_first=True))
    o.append(T(20, 324, 'R₁ = L₀ ⊕ F = 1010 ⊕ 0011 = 1001;  block after round 1 = 0110 1001 = 105', 14, 'start', bold=True))
    o.append(T(20, 348, 'Decryption runs the same picture with the subkeys reversed; F never has to be inverted.', 13, 'start', MUT))
    return 362, ''.join(o)
FIG[4] = (f4, 'The right half 0110 passes through F with the round key to give 0011, which is XORed into the left half 1010 to make 1001. The halves then swap, so after one round the block is 0110 1001 = 105.',
          'A Feistel round: L0 = 1010 and R0 = 0110 at the top, R0 entering F with K1 to give 0011, an XOR with L0, and crossing lines that give L1 = 0110 and R1 = 1001 at the bottom.')


# ---- 3.5 reading DES S-box S1 ----
def f5():
    o = [T(20, 24, 'S1 input 011001: outer bits pick the row, middle four bits pick the column', 15, 'start', bold=True)]
    bits = '011001'
    for i, b in enumerate(bits):
        outer = i in (0, 5)
        o.append(boxt(200 + i * 52, 40, 48, 42, [b], LVS if outer else ACS, LV if outer else AC, 18, bold_first=True))
        o.append(T(224 + i * 52, 98, f'b{i + 1}', 13, fill=MUT))
    o.append(T(190, 66, 'input', 14, 'end', bold=True))
    o.append(T(20, 130, 'row = b1 b6 = 01 = 1', 14, 'start', LV, True))
    o.append(T(260, 130, 'column = b2 b3 b4 b5 = 1100 = 12', 14, 'start', AC, True))
    row1 = [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8]
    x0, w = 70, 40
    o.append(T(60, 186, 'row 1', 13, 'end', LV, True))
    for c, v in enumerate(row1):
        hot = c == 12
        o.append(T(x0 + c * w + w / 2, 160, str(c), 13, fill=AC if hot else MUT, bold=hot))
        o.append(R(x0 + c * w + 1, 166, w - 2, 32, NXS if hot else PANEL, NX if hot else LN, 3, 1.3 if not hot else 2))
        o.append(TM(x0 + c * w + w / 2, 188, str(v), 14, bold=hot))
    o.append(L(x0 + 12 * w + w / 2, 200, x0 + 12 * w + w / 2, 222, NX, 2, arrow='x'))
    o.append(boxt(x0 + 12 * w - 50, 224, 140, 40, ['9 = 1001'], NXS, NX, 16, bold_first=True))
    o.append(T(20, 300, 'Six bits in, four bits out: S1(011001) = 9 = 1001. The S-boxes are the only non-linear step in DES.', 13, 'start'))
    return 314, ''.join(o)
FIG[5] = (f5, 'The outer bits of 011001 (0 and 1) choose row 1 of S1 and the middle bits 1100 choose column 12. The entry there is 9, so the S-box outputs the 4 bits 1001.',
          'Six input bit cells 0 1 1 0 0 1 with the outer two marked for the row and the middle four for the column; below, row 1 of S1 with columns 0 to 15 and column 12, value 9, highlighted.')


# ---- 3.6 AES SubBytes(0x53) ----
def f6():
    x0, y0, c = 300, 44, 22
    o = [T(20, 30, 'SubBytes(0x53)', 15, 'start', bold=True)]
    o.append(boxt(20, 50, 220, 44, ['0x53 = 0101 0011'], PANEL, AC, 15, bold_first=True))
    o.append(T(20, 124, 'high nibble 0101 = 5', 14, 'start', LV, True)); o.append(T(20, 146, '→ row 5', 14, 'start', LV))
    o.append(T(20, 184, 'low nibble 0011 = 3', 14, 'start', AC, True)); o.append(T(20, 206, '→ column 3', 14, 'start', AC))
    H = '0123456789ABCDEF'
    for i in range(16):
        o.append(T(x0 + (i + 1) * c + c / 2, y0 + 15, H[i], 13, fill=AC if i == 3 else MUT, bold=i == 3))
        o.append(T(x0 + c / 2, y0 + (i + 1) * c + 15, H[i], 13, fill=LV if i == 5 else MUT, bold=i == 5))
    o.append(R(x0 + c, y0 + c, 16 * c, 16 * c, PANEL, LN, 0, 1))
    for i in range(1, 16):
        o.append(L(x0 + c + i * c, y0 + c, x0 + c + i * c, y0 + 17 * c, LN, 0.8))
        o.append(L(x0 + c, y0 + c + i * c, x0 + 17 * c, y0 + c + i * c, LN, 0.8))
    o.append(R(x0 + c, y0 + 6 * c, 16 * c, c, LVS, LV, 0, 1.5))
    o.append(R(x0 + 4 * c, y0 + c, c, 16 * c, ACS, AC, 0, 1.5))
    o.append(R(x0 + 4 * c - 6, y0 + 6 * c - 6, c + 12, c + 12, NXS, NX, 3, 2.5))
    o.append(TM(x0 + 4.5 * c, y0 + 6.5 * c + 5, 'ED', 13, fill=NX, bold=True))
    o.append(T(x0 + 9 * c, y0 + 17 * c + 30, 'the 16 × 16 AES S-box', 13, fill=MUT))
    o.append(boxt(20, 250, 220, 60, ['SubBytes(0x53) = 0xED', '= 14 × 16 + 13 = 237'], NXS, NX, 14, bold_first=True))
    return 452, ''.join(o)
FIG[6] = (f6, 'SubBytes looks a byte up in a 16 × 16 table: the high nibble 5 picks the row and the low nibble 3 the column. Row 5, column 3 holds 0xED, so SubBytes(0x53) = 0xED = 237.',
          'The byte 0x53 split into nibbles 5 and 3, and an empty 16 by 16 grid with row 5 and column 3 shaded; their crossing cell holds ED.')


# ---- 3.7 CBC with the toy cipher ----
def f7():
    o = [T(20, 24, 'CBC with the toy cipher E(x) = x ⊕ 1010 and IV = 0000', 15, 'start', bold=True)]
    o.append(boxt(20, 120, 110, 40, ['IV = 0000'], PANEL, L2, 14, bold_first=True))
    for i, (p, mid, c) in enumerate((('1100', '1100', '0110'), ('0110', '0000', '1010'))):
        x = 230 + i * 250
        o.append(boxt(x - 55, 40, 110, 40, [f'P{"₁₂"[i]} = {p}'], PANEL, AC, 14, bold_first=True))
        o.append(L(x, 82, x, 128, AC, 2, arrow='n'))
        o.append(xor_sym(x, 140))
        o.append(L(x, 152, x, 178, AC, 2, arrow='n'))
        o.append(T(x + 12, 170, mid, 13, 'start', MUT, True))
        o.append(boxt(x - 55, 180, 110, 44, ['E_K', '⊕ 1010'], ACS, AC, 13, bold_first=True))
        o.append(L(x, 226, x, 252, AC, 2, arrow='n'))
        o.append(boxt(x - 55, 254, 110, 40, [f'C{"₁₂"[i]} = {c}'], NXS, NX, 14, bold_first=True))
    o.append(L(132, 140, 216, 140, L2, 2, arrow='m'))
    o.append(P([(285, 274), (340, 274), (340, 140), (467, 140)], NX, 2)); o.append(L(460, 140, 467, 140, NX, 2, arrow='x'))
    o.append(T(348, 210, 'C₁ chains', 13, 'start', NX, True)); o.append(T(348, 226, 'into block 2', 13, 'start', NX, True))
    o.append(T(20, 332, 'CBC ciphertext 0110 1010.  ECB would give 0110 1100, and two equal plaintext blocks would give', 13, 'start'))
    o.append(T(20, 350, 'two equal ciphertext blocks in ECB but not in CBC.  Decrypt: Pᵢ = D(Cᵢ) ⊕ Cᵢ₋₁ = 1100, 0110.', 13, 'start'))
    return 364, ''.join(o)
FIG[7] = (f7, 'Each plaintext block is XORed with the previous ciphertext block (the IV for the first) before encryption: 1100 gives C₁ = 0110, and 0110 ⊕ 0110 = 0000 gives C₂ = 1010. The chaining is why equal plaintext blocks no longer give equal ciphertext.',
          'Two CBC stages side by side: IV 0000 XORed with P1 1100 then encrypted to C1 0110, and C1 fed across to be XORed with P2 0110 to 0000, encrypted to C2 1010.')


# ---- 3.8 one differential through S1 ----
def f8():
    o = [T(20, 24, 'Input difference ΔX = 000001 through S1', 15, 'start', bold=True)]
    for i, (x, row, out) in enumerate((('000000', 'row 0, col 0', '1110 (14)'), ('000001', 'row 1, col 0', '0000 (0)'))):
        y = 48 + i * 80
        o.append(T(150, y + 26, 'x' if i == 0 else 'x′', 16, 'end', bold=True))
        o.append(bitrow(160, y, x, PANEL, AC, 32, 36, 16, hot=[None] * 5 + [((LVS, LV) if i else None)]))
        o.append(L(356, y + 18, 396, y + 18, AC, 2, arrow='n'))
        o.append(boxt(398, y - 2, 110, 40, ['S1', row], ACS, AC, 13, bold_first=True))
        o.append(L(510, y + 18, 540, y + 18, AC, 2, arrow='n'))
        o.append(boxt(542, y, 150, 36, [out], PANEL, NX, 15, bold_first=True))
    o.append(T(176, 230, 'ΔX = 000001', 14, 'start', LV, True))
    o.append(T(560, 230, 'ΔY = 1110 ⊕ 0000 = 1110', 14, 'middle', NX, True))
    o.append(T(20, 276, 'Try all 64 inputs x: only x = 000000 and x = 000001 give S1(x) ⊕ S1(x ⊕ 000001) = 1110.', 14, 'start'))
    o.append(T(20, 300, 'DP(000001 → 1110) = 2 ÷ 64 = 1/32 = 0.03125', 15, 'start', bold=True))
    o.append(T(20, 324, 'A trail multiplies such probabilities round by round; small ones make the attack need many pairs.', 13, 'start', MUT))
    return 338, ''.join(o)
FIG[8] = (f8, 'Two inputs that differ only in the last bit go through S1 and come out as 1110 and 0000, an output difference of 1110. Only 2 of the 64 inputs do this, so the differential probability is 1/32.',
          'Two rows: x = 000000 into S1 at row 0 column 0 giving 1110, and x prime = 000001 at row 1 column 0 giving 0000; below, the differences 000001 and 1110 and the count 2 of 64.')


# ---- 3.9 the IND-CPA game against a deterministic scheme ----
def f9():
    ax, cx = 150, 560
    o = [boxt(ax - 80, 20, 160, 40, ['adversary'], LVS, LV, 14, bold_first=True), boxt(cx - 80, 20, 160, 40, ['challenger, K = 1010'], PANEL, AC, 13, bold_first=True)]
    o.append(L(ax, 62, ax, 330, L2, 1.5, '5 4')); o.append(L(cx, 62, cx, 330, L2, 1.5, '5 4'))
    msgs = [(90, True, 'query: Enc(0000)', AC), (126, False, 'reply 0000 ⊕ 1010 = 1010', AC), (176, True, 'challenge: m₀ = 0000, m₁ = 1111', LV),
            (212, False, 'c* = E(m_b) = 1010', LV)]
    for y, right, lab, c in msgs:
        if right: o.append(L(ax + 2, y, cx - 4, y, c, 2, arrow='n' if c == AC else 'l'))
        else: o.append(L(cx - 2, y, ax + 4, y, c, 2, arrow='n' if c == AC else 'l'))
        o.append(Tb((ax + cx) / 2, y - 8, lab, 13, fill=c, bold=True))
    o.append(boxt(ax - 120, 238, 240, 64, ['c* = 1010 = the reply to m₀', 'so guess b′ = 0'], NXS, NX, 13, bold_first=True))
    o.append(boxt(cx - 130, 238, 260, 64, ['if b = 1, c* would be', '1111 ⊕ 1010 = 0101'], PANEL, L2, 13, dash='5 4'))
    o.append(T(20, 352, 'The guess is always right: Pr[b′ = b] = 1, advantage = |2 × 1 − 1| = 1, the maximum.', 14, 'start', bold=True))
    o.append(T(20, 374, 'Any deterministic scheme loses this game, so IND-CPA security needs randomised encryption.', 13, 'start', MUT))
    return 388, ''.join(o)
FIG[9] = (f9, 'Because E(m) = m ⊕ K always gives the same output for the same input, one encryption query of 0000 tells the adversary what E(m₀) looks like. The challenge 1010 matches it, so the adversary always guesses b correctly: advantage 1.',
          'A message diagram between the adversary and the challenger: the query Enc(0000) answered 1010, the challenge with m0 0000 and m1 1111 answered 1010, and the guess b prime = 0.')


spec = make_spec(FIG)
