"""Claude's hand-drawn figures for c-sec-u4 (Cryptography and Network Security, unit 4: public-key cryptography,
hashes, MACs and signatures), one per chapter, from each chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def ar(x1, y1, x2, y2, c=AC, a='n', w=2, dash=None):
    return L(x1, y1, x2, y2, c, w, dash, arrow=a)


# ---- 4.1 trapdoor one-way function ----
def f1():
    o = [T(20, 24, 'Trapdoor one-way function: f(x) = x³ mod 55', 15, 'start', bold=True)]
    o.append(f'<circle cx="100" cy="130" r="34" style="fill:{NXS};stroke:{NX};stroke-width:2"/>')
    o.append(f'<circle cx="420" cy="130" r="34" style="fill:{ACS};stroke:{AC};stroke-width:2"/>')
    o += [T(100, 138, '9', 22, bold=True), T(420, 138, '14', 22, bold=True),
          T(100, 186, 'x', 14, fill=MUT), T(420, 186, 'f(x)', 14, fill=MUT)]
    o.append(arc(134, 118, 386, 118, 0.22, AC, 2, 'n'))
    o.append(Tb(260, 82, 'easy: 9³ = 729 = 13 × 55 + 14', 14, fill=AC, bold=True))
    o.append(arc(388, 146, 132, 146, 0.17, MUT, 2, 'm', '6 5'))
    o.append(Tb(260, 174, 'without 5 × 11: no fast way back', 13, fill=MUT))
    o.append(arc(400, 160, 120, 160, 0.4, NX, 2, 'x'))
    o.append(Tb(260, 222, 'trapdoor d = 27: 14²⁷ mod 55 = 9', 14, fill=NX, bold=True))
    o.append(boxt(500, 44, 200, 168, ['14²⁷ by squaring', '14² ≡ 31', '14⁴ ≡ 31² ≡ 26', '14⁸ ≡ 26² ≡ 16',
                                      '14¹⁶ ≡ 16² ≡ 36', '27 = 16 + 8 + 2 + 1', '36·16·31·14 ≡ 9'], PANEL, L2, 14, True))
    o.append(T(20, 268, '12 people need', 14, 'start', MUT))
    o.append(R(190, 278, 66 * 6, 22, ACS, AC, 3, 1.5))
    o.append(T(190 + 66 * 6 + 10, 294, '66 shared keys', 14, 'start', AC, True))
    o.append(T(180, 294, 'symmetric', 14, 'end'))
    o.append(R(190, 310, 12 * 6, 22, NXS, NX, 3, 1.5))
    o.append(T(190 + 12 * 6 + 10, 326, '12 key pairs', 14, 'start', NX, True))
    o.append(T(180, 326, 'public key', 14, 'end'))
    return 344, ''.join(o)


FIG[1] = (f1, 'Cubing 9 mod 55 gives 14 at once, but going back from 14 needs the trapdoor: with d = 27, square and multiply returns 9. Twelve people need 66 shared keys but only 12 key pairs.',
          'Two circles, 9 and 14. An arrow from 9 to 14 is labelled 9 cubed mod 55 equals 14. A dashed return arrow says there is no fast way back without the factors, and a green return arrow says 14 to the 27 mod 55 equals 9. A side panel lists the squarings 31, 26, 16, 36 and the product 9. Bars compare 66 symmetric keys with 12 key pairs.')


# ---- 4.2 RSA end to end ----
def f2():
    o = [boxt(20, 30, 130, 56, ['p = 5', 'q = 11'], PANEL, L2, 15, True),
         boxt(180, 30, 160, 56, ['n = 5 × 11 = 55', 'φ(n) = 4 × 10 = 40'], PANEL, L2, 14),
         boxt(370, 30, 150, 56, ['e = 3', 'gcd(3, 40) = 1'], ACS, AC, 14, True),
         boxt(545, 30, 160, 56, ['d = 27', '3 × 27 = 81 ≡ 1 mod 40'], LVS, LV, 13, True)]
    o += [ar(150, 58, 178, 58, L2, 'm'), ar(340, 58, 368, 58, L2, 'm'), ar(520, 58, 543, 58, L2, 'm')]
    o.append(boxt(60, 130, 260, 52, ['public key (e, n) = (3, 55)', 'goes to everyone'], ACS, AC, 14, True))
    o.append(boxt(430, 130, 260, 52, ['private key d = 27', 'kept by the owner'], LVS, LV, 14, True))
    o += [P([(445, 86), (445, 108), (190, 108), (190, 128)], AC, 2), ar(190, 120, 190, 128, AC, 'n'),
          ar(625, 86, 625, 128, LV, 'l')]
    o.append(boxt(20, 230, 80, 46, ['m = 9'], NXS, NX, 16, True))
    o.append(boxt(300, 230, 100, 46, ['c = 14'], ACS, AC, 16, True))
    o.append(boxt(610, 230, 90, 46, ['m = 9'], NXS, NX, 16, True))
    o += [ar(100, 253, 298, 253, AC, 'n'), ar(400, 253, 608, 253, LV, 'l')]
    o += [T(200, 244, 'c = 9³ mod 55', 14, fill=AC, bold=True), T(200, 272, '729 − 715 = 14', 13, fill=MUT),
          T(505, 244, 'm = 14²⁷ mod 55', 14, fill=LV, bold=True), T(505, 272, 'with d = 27', 13, fill=MUT)]
    o.append(T(20, 316, 'Check by CRT:  14 ≡ 4 (mod 5) and 4²⁷ ≡ 4;  14 ≡ 3 (mod 11) and 3²⁷ ≡ 3² = 9.', 14, 'start'))
    o.append(T(20, 338, 'The only number below 55 that is 4 mod 5 and 9 mod 11 is 9, the message.', 14, 'start', NX, True))
    return 352, ''.join(o)


FIG[2] = (f2, 'The primes 5 and 11 give n = 55 and φ(n) = 40, so e = 3 and d = 27. The public pair (3, 55) turns 9 into 14, and only d = 27 turns 14 back into 9.',
          'Key generation boxes from p = 5 and q = 11 to n = 55, phi 40, e = 3 and d = 27. The public key (3, 55) and private key 27 split off. Below, m = 9 is encrypted to c = 14 and decrypted back to 9, with a CRT check.')


# ---- 4.3 Diffie-Hellman ----
def f3():
    o = [boxt(55, 16, 140, 38, ['Alice'], LVS, LV, 15, True), boxt(525, 16, 140, 38, ['Bob'], NXS, NX, 15, True),
         boxt(255, 16, 210, 38, ['public: p = 23, g = 5'], PANEL, L2, 14, True)]
    o += [boxt(20, 74, 210, 38, ['private a = 6'], PANEL, LV, 14, dash='5 4'),
          boxt(490, 74, 210, 38, ['private b = 15'], PANEL, NX, 14, dash='5 4')]
    o += [boxt(20, 128, 210, 50, ['A = 5⁶ mod 23 = 8', '5² ≡ 2, 5⁴ ≡ 4, 4 × 2 = 8'], PANEL, LV, 13, True),
          boxt(490, 128, 210, 50, ['B = 5¹⁵ mod 23 = 19', '16 × 4 × 2 × 5 = 640 ≡ 19'], PANEL, NX, 13, True)]
    o += [ar(230, 206, 488, 206, LV, 'l'), Tb(360, 200, 'A = 8', 14, fill=LV, bold=True),
          ar(490, 242, 232, 242, NX, 'x'), Tb(360, 236, 'B = 19', 14, fill=NX, bold=True)]
    o += [boxt(20, 268, 210, 50, ['K = 19⁶ mod 23 = 2', '19 ≡ −4, (−4)⁶ = 48 ≡ 2'], ACS, AC, 13, True),
          boxt(490, 268, 210, 50, ['K = 8¹⁵ mod 23 = 2', '4 × 2 × 18 × 8 = 1152 ≡ 2'], ACS, AC, 13, True)]
    o.append(boxt(255, 262, 210, 62, ['eavesdropper sees', '23, 5, 8 and 19', 'never 6, 15 or 2'], PANEL, L2, 13, True, dash='4 4'))
    o.append(T(20, 352, 'Both get K = 2 because (5⁶)¹⁵ = (5¹⁵)⁶ = 5⁹⁰ ≡ 5² ≡ 2 (mod 23).', 14, 'start', AC, True))
    o.append(T(20, 374, 'Finding a from 5ᵃ ≡ 8 (mod 23) is a short search here, but infeasible for a 2048-bit p.', 13, 'start', MUT))
    return 388, ''.join(o)


FIG[3] = (f3, 'Alice sends A = 8 and Bob sends B = 19; each raises the other\'s value to their own secret and both reach K = 2. The wire carries only 23, 5, 8 and 19.',
          'Two columns, Alice with private a = 6 and Bob with private b = 15. Alice computes A = 8 and Bob B = 19; arrows carry A and B across. Both compute K = 2. A middle box says the eavesdropper sees 23, 5, 8 and 19 only.')


# ---- 4.4 ElGamal ----
def f4():
    o = [boxt(80, 16, 140, 36, ['sender'], LVS, LV, 15, True), boxt(500, 16, 140, 36, ['receiver'], NXS, NX, 15, True),
         boxt(290, 16, 140, 36, ['p = 23, g = 5'], PANEL, L2, 14, True)]
    o.append(boxt(440, 66, 260, 50, ['private x = 6', 'public y = 5⁶ mod 23 = 8'], PANEL, NX, 14, True))
    o += [ar(440, 100, 282, 100, NX, 'x'), Tb(360, 94, 'y = 8', 14, fill=NX, bold=True)]
    rows = [('m = 7, random k = 15', PANEL, L2), ('C1 = 5¹⁵ mod 23 = 19', PANEL, LV), ('mask s = 8¹⁵ mod 23 = 2', LVS, LV),
            ('C2 = m × s = 7 × 2 = 14', PANEL, LV)]
    for i, (s, f, st) in enumerate(rows):
        y = 126 + i * 46
        o.append(boxt(20, y, 260, 38, [s], f, st, 14, True))
    o += [ar(280, 287, 438, 287, LV, 'l'), Tb(360, 279, '(19, 14)', 14, fill=LV, bold=True)]
    rows = [('mask s = 19⁶ mod 23 = 2', LVS, NX), ('s⁻¹ = 12, as 2 × 12 = 24 ≡ 1', PANEL, NX), ('m = 14 × 12 = 168 ≡ 7', NXS, NX)]
    for i, (s, f, st) in enumerate(rows):
        y = 268 + i * 46
        o.append(boxt(440, y, 260, 38, [s], f, st, 14, True))
    o.append(T(20, 336, 'Both masks are the same number:', 14, 'start', MUT))
    o.append(T(20, 358, '8¹⁵ = 5⁹⁰ = 19⁶ ≡ 2 (mod 23)', 14, 'start', AC, True))
    o.append(T(20, 384, 'A fresh k every message; reusing k leaks m₁ / m₂.', 13, 'start', LV))
    return 400, ''.join(o)


FIG[4] = (f4, 'The sender masks m = 7 with 8¹⁵ mod 23 = 2 and sends (19, 14). The receiver rebuilds the same mask as 19⁶ mod 23 = 2 and multiplies 14 by 2⁻¹ = 12 to get 7 back.',
          'Sender column: m = 7 and k = 15, C1 = 19, mask 2, C2 = 14. The receiver publishes y = 8 and receives (19, 14), then computes the mask 2, its inverse 12 and m = 7.')


# ---- 4.5 certificate chain ----
def f5():
    o = [boxt(20, 24, 260, 64, ['root CA (trust store)', 'public key e = 3, n = 55'], NXS, NX, 14, True),
         boxt(20, 150, 260, 72, ['intermediate CA certificate', 'signature s = 4, hash h = 9', 'its key e = 3, n = 33'], PANEL, AC, 14, True),
         boxt(20, 284, 260, 64, ['bank.example certificate', 'signature s = 5, hash h = 26'], PANEL, AC, 14, True)]
    o += [ar(150, 148, 150, 91, NX, 'x'), ar(150, 282, 150, 225, AC, 'n')]
    o += [T(300, 110, 'check with the root key: 4³ mod 55', 14, 'start'),
          T(300, 132, '= 64 − 55 = 9 = h, so it passes', 14, 'start', NX, True),
          T(300, 244, 'check with the intermediate key: 5³ mod 33', 14, 'start'),
          T(300, 266, '= 125 − 99 = 26 = h, so it passes', 14, 'start', NX, True)]
    o.append(boxt(480, 300, 220, 56, ['forged bank.example', 's = 7, h = 21'], LVS, LV, 14, True, dash='5 4'))
    o += [P([(660, 298), (660, 56), (290, 56)], LV, 2, '6 4'), ar(296, 56, 284, 56, LV, 'l'),
          Tb(660, 190, 'fails', 14, fill=LV, bold=True)]
    o += [T(700, 380, '7³ mod 55 = 343 − 330 = 13 ≠ 21', 14, 'end', LV, True),
          T(700, 402, 'signature fails: rejected, warning shown', 13, 'end', LV)]
    o += [T(20, 380, 'chain: bank → intermediate → root', 14, 'start', INK, True),
          T(20, 402, 'name and dates are also checked', 13, 'start', MUT)]
    return 416, ''.join(o)


FIG[5] = (f5, 'Each link is checked with the issuer\'s public key: 4³ mod 55 = 9 and 5³ mod 33 = 26 match, so the bank chains to the root. The forged certificate gives 13, not 21, and is rejected.',
          'Three stacked certificates, root, intermediate and bank, with upward arrows labelled 4 cubed mod 55 = 9 and 5 cubed mod 33 = 26, both passing. A dashed forged certificate on the right points to the root and fails, because 7 cubed mod 55 is 13, not 21.')


# ---- 4.6 toy iterated hash and a collision ----
def f6():
    o = []
    for x, s in [(50, 'h₀'), (190, 'after block 1'), (340, 'after block 2'), (490, 'after block 3')]:
        o.append(T(x, 28, s, 13, fill=MUT))
    pts = {'h0': (50, 170), 'a1': (190, 90), 'b1': (190, 250), 'h2': (340, 170), 'h3': (490, 110), 'x3': (490, 250)}
    o += [edge(pts['h0'], pts['a1'], 26, 0, AC), edge(pts['a1'], pts['h2'], 26, 0, AC),
          edge(pts['h0'], pts['b1'], 26, 0, LV, arrow='l'), edge(pts['b1'], pts['h2'], 26, 0, LV, arrow='l'),
          edge(pts['h2'], pts['h3'], 26, 0, NX, arrow='x'), edge(pts['h2'], pts['x3'], 26, 0, MUT, arrow='m', dash='5 4')]
    o += [Tb(112, 118, '+3', 14, fill=AC, bold=True), Tb(268, 118, '+7', 14, fill=AC, bold=True),
          Tb(112, 224, '+4', 14, fill=LV, bold=True), Tb(268, 224, '+6', 14, fill=LV, bold=True),
          Tb(415, 132, '+5', 14, fill=NX, bold=True), Tb(415, 222, '+6', 14, fill=MUT, bold=True)]
    o += [state(*pts['h0'], '2', r=26), state(*pts['a1'], '5', r=26, fill=ACS), state(*pts['b1'], '6', r=26, fill=LVS, stroke=LV),
          state(*pts['h2'], '12', r=26), state(*pts['h3'], '1', accept=True, r=26, fill=NXS, stroke=NX),
          state(*pts['x3'], '2', r=26, stroke=L2)]
    o += [T(528, 106, 'digest = 1', 15, 'start', NX, True), T(528, 126, 'for 3, 7, 5 and 4, 6, 5', 13, 'start', NX),
          T(528, 246, 'digest = 2', 15, 'start', MUT, True), T(528, 266, 'last block 6', 13, 'start', MUT)]
    o.append(T(20, 316, 'hᵢ = (hᵢ₋₁ + Bᵢ) mod 16:  2 → 5 → 12 → 17 mod 16 = 1, and 2 → 6 → 12 → 1.  Two messages, one digest.', 13, 'start'))
    o.append(T(20, 340, 'A real 256-bit hash: preimage ≈ 2²⁵⁶ tries, collision ≈ 2¹²⁸ tries (the birthday bound).', 14, 'start', AC, True))
    return 354, ''.join(o)


FIG[6] = (f6, 'Starting at 2 and adding each block mod 16, the blocks 3, 7, 5 and 4, 6, 5 both end at digest 1, a collision; changing the last block to 6 gives 2.',
          'A chain of states: start 2, then 5 on the top path after block 3 or 6 on the bottom path after block 4. Both reach 12, then adding 5 gives digest 1; a dashed branch adding 6 gives digest 2. A note gives 2 to the 256 for a preimage and 2 to the 128 for a collision.')


# ---- 4.7 HMAC with a toy adding hash ----
def f7():
    o = []
    # inner pass
    o += [T(20, 74, 'inner', 15, 'start', AC, True),
          boxt(90, 50, 130, 46, ['K ⊕ ipad = 3', '0101 ⊕ 0110'], ACS, AC, 13, True),
          ar(220, 73, 298, 73, AC), Tb(259, 66, '+7', 14, fill=AC, bold=True),
          boxt(300, 50, 70, 46, ['10'], PANEL, AC, 16, True),
          ar(370, 73, 438, 73, AC), Tb(404, 66, '+4', 14, fill=AC, bold=True),
          boxt(440, 50, 70, 46, ['14'], ACS, AC, 16, True),
          T(524, 78, 'inner digest 14', 14, 'start', AC, True)]
    # outer pass
    o += [T(20, 174, 'outer', 15, 'start', NX, True),
          boxt(90, 150, 130, 46, ['K ⊕ opad = 9', '0101 ⊕ 1100'], NXS, NX, 13, True),
          ar(220, 173, 298, 173, NX, 'x'), T(259, 194, '+14', 14, fill=NX, bold=True),
          boxt(300, 150, 150, 46, ['23 mod 16 = 7'], NXS, NX, 15, True),
          T(466, 178, 'HMAC tag 7', 15, 'start', NX, True)]
    o += [P([(475, 96), (475, 122), (259, 122), (259, 160)], AC, 1.8, '5 4'), ar(259, 156, 259, 166, AC, 'n', 1.8)]
    # naive
    o += [T(20, 266, 'naive', 15, 'start', LV, True), T(20, 284, 'H(K ‖ M)', 13, 'start', LV),
          boxt(90, 250, 60, 46, ['5'], PANEL, LV, 16, True),
          ar(150, 273, 208, 273, LV, 'l'), Tb(179, 266, '+7', 14, fill=LV, bold=True),
          boxt(210, 250, 60, 46, ['12'], PANEL, LV, 16, True),
          ar(270, 273, 328, 273, LV, 'l'), Tb(299, 266, '+4', 14, fill=LV, bold=True),
          boxt(330, 250, 140, 46, ['16 mod 16 = 0'], LVS, LV, 15, True),
          ar(470, 273, 548, 273, LV, 'l', 2, '5 4'), Tb(509, 266, '+X', 14, fill=LV, bold=True),
          boxt(550, 250, 150, 46, ['tag X', 'forged, no key'], PANEL, LV, 13, True, dash='5 4')]
    o.append(T(20, 330, 'Tag 0 for the blocks 7, 4 is the running state, so anyone can append X and predict the new tag X.', 13, 'start'))
    o.append(T(20, 352, 'HMAC hides the key inside both passes, so the tag 7 cannot be extended.', 14, 'start', NX, True))
    return 366, ''.join(o)


FIG[7] = (f7, 'With K = 5, the inner pass starts at 5 ⊕ 6 = 3 and adds 7 and 4 to reach 14; the outer pass adds 14 to 5 ⊕ 12 = 9, giving tag 7. The naive H(K ‖ M) ends at 0, which an attacker can extend.',
          'Three rows. Inner: 3, then 10, then 14. Outer: 9 plus 14 is 23 mod 16 = 7, the HMAC tag. Naive: 5, 12, then 16 mod 16 = 0, with a dashed arrow plus X to a forged tag X.')


# ---- 4.8 RSA signature and the textbook forgery ----
def f8():
    o = [T(20, 26, 'signer, private d = 27', 14, 'start', LV, True)]
    o += [boxt(20, 40, 100, 48, ['message M'], PANEL, L2, 14, True),
          boxt(150, 40, 130, 48, ['hash', 'h = 9'], PANEL, AC, 14, True),
          boxt(310, 40, 220, 48, ['s = 9²⁷ mod 55 = 4', 'sign with d = 27'], LVS, LV, 14, True),
          boxt(560, 40, 140, 48, ['send', '(M, s = 4)'], PANEL, L2, 14, True)]
    o += [ar(120, 64, 148, 64, L2, 'm'), ar(280, 64, 308, 64, L2, 'm'), ar(530, 64, 558, 64, L2, 'm')]
    o += [P([(600, 88), (600, 118), (230, 118), (230, 140)], L2, 2), ar(230, 132, 230, 148, L2, 'm'), Tb(415, 122, 'M', 14, fill=MUT, bold=True),
          ar(670, 88, 670, 148, L2, 'm'), Tb(670, 120, 's = 4', 13, fill=MUT, bold=True)]
    o += [boxt(120, 150, 220, 46, ['hash M again: h′ = 9'], PANEL, AC, 14, True),
          boxt(440, 150, 260, 46, ['s³ mod 55 = 64 − 55 = 9'], PANEL, AC, 14, True)]
    o += [ar(230, 196, 300, 228, AC), ar(570, 196, 440, 228, AC)]
    o.append(boxt(250, 230, 240, 44, ['9 = 9: accept'], NXS, NX, 15, True))
    o.append(T(20, 258, 'verifier, public (3, 55)', 14, 'start', NX, True))
    o.append(boxt(20, 300, 680, 82, ['Textbook RSA forgery: (9, 4) and (4, 49) are both valid, so their product is too',
                                     'h = 9 × 4 mod 55 = 36 and s = 4 × 49 = 196 ≡ 31; 31³ mod 55 = 36, valid with no d',
                                     'Padding such as RSA-PSS breaks this multiplication.'], LVS, LV, 14, True, dash='5 4'))
    return 396, ''.join(o)


FIG[8] = (f8, 'The signer hashes M to 9 and signs it as 9²⁷ mod 55 = 4; the verifier hashes M again and checks 4³ mod 55 = 9. Multiplying two valid textbook pairs forges (36, 31) without d.',
          'Top row: message M, hash 9, signature 9 to the 27 mod 55 = 4, send M and 4. Verifier row: hash M again to 9 and 4 cubed mod 55 = 9, both feeding an accept box. A dashed panel shows the forgery: h = 36, s = 31, 31 cubed mod 55 = 36.')


# ---- 4.9 zero knowledge 3-colouring ----
def f9():
    A, B, Cc = (150, 70), (55, 220), (245, 220)
    o = [L(*B, *Cc, L2, 2), L(*A, *Cc, L2, 2), L(*A, *B, AC, 4)]
    o.append(Tb(80, 134, 'challenge AB', 13, 'end', AC, True))
    o += [state(*A, 'A = 1', r=30, fill=ACS, stroke=AC, size=14), state(*B, 'B = 2', r=30, fill=NXS, stroke=NX, size=14),
          f'<circle cx="{Cc[0]}" cy="{Cc[1]}" r="30" style="fill:{PANEL};stroke:{L2};stroke-width:2;stroke-dasharray:5 4"/>',
          T(Cc[0], Cc[1] + 5, 'C = ?', 14, bold=True, fill=MUT)]
    o += [T(150, 278, 'only A and B are opened: 1 ≠ 2,', 13, fill=NX, bold=True),
          T(150, 296, 'so the verifier accepts; C stays sealed', 13, fill=MUT)]
    x0, x1, y0, y1 = 370, 700, 60, 240
    fx = lambda r: x0 + (r - 0.5) * 32.5
    fy = lambda v: y1 - v * (y1 - y0) / 0.75
    o.append(axes(x0, x1, y0, y1, range(1, 11), [0, 0.25, 0.5, 0.75], fx, fy, 'rounds r', 'cheater passes all r rounds: (2/3)ʳ',
                  yfmt=lambda v: f'{v:g}'))
    for r in range(1, 11):
        v = (2 / 3) ** r
        o.append(R(fx(r) - 11, fy(v), 22, y1 - fy(v), LVS if r < 10 else ACS, LV if r < 10 else AC, 2, 1.5))
    o += [T(fx(1) + 16, fy(2 / 3) + 4, '0.667', 13, 'start', LV, True),
          T(fx(10), fy((2 / 3) ** 10) - 10, '0.0173', 13, 'end', AC, True)]
    o.append(T(20, 330, 'Honest prover: every edge has two different colours, so it passes each round with probability 1.', 13, 'start'))
    o.append(T(20, 352, 'Two-colour cheat: 1 of the 3 edges is bad, so P(pass) = 2/3 a round and (2/3)¹⁰ = 0.01734 after ten.', 13, 'start', LV, True))
    return 366, ''.join(o)


FIG[9] = (f9, 'The verifier asks for edge AB and sees only colours 1 and 2, so it accepts and learns nothing about C. A two-colour cheat survives a round with probability 2/3, and ten rounds with 0.01734.',
          'A triangle A, B, C with edge AB highlighted; A shows colour 1, B colour 2 and C is sealed. A bar chart of (2/3) to the r for r = 1 to 10 falls from 0.667 to 0.0173.')

spec = make_spec(FIG)
