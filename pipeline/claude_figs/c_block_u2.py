"""Claude's hand-drawn figures for c-block-u2 (Blockchain Technology, unit 2: cryptography for blockchain), one per
chapter, each drawn from that chapter's worked example with its own numbers."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blockkit import *

FIG = {}


# ---- 2.1 brute force on a 128-bit key ----
def f1():
    o = [T(20, 28, 'Brute force on a 128-bit key at 10¹² guesses per second', 15, 'start', bold=True)]
    # keyspace bar, half shaded
    o.append(R(20, 46, 680, 34, PANEL, L2, 6))
    o.append(R(20, 46, 340, 34, ACS, AC, 6))
    o.append(T(190, 68, 'expected search: half', 13, fill=AC, bold=True))
    o.append(T(530, 68, 'other half', 13, fill=MUT))
    o.append(T(20, 100, 'all keys: 2¹²⁸', 13, 'start', MUT)); o.append(T(700, 100, 'half = 2¹²⁷ ≈ 1.70 × 10³⁸ keys', 13, 'end', MUT))
    steps = [('keys to try', '2¹²⁷ ≈ 1.70 × 10³⁸', ACS, AC),
             ('÷ 10¹² keys per second', '1.70 × 10²⁶ seconds', PANEL, AC),
             ('÷ 3.15 × 10⁷ seconds per year', '5.40 × 10¹⁸ years', NXS, NX)]
    for i, (op, res, f, st) in enumerate(steps):
        y = 124 + i * 70
        o.append(boxt(170, y, 380, 48, [res], f, st, 17, bold_first=True))
        if i:
            o.append(A(360, y - 22, 360, y - 2, AC))
            o.append(T(372, y - 8, op, 13, 'start', MUT))
    o.append(T(360, 360, 'The universe is about 1.4 × 10¹⁰ years old: the search takes roughly 400 million times longer.', 13, fill=MUT))
    o.append(T(360, 382, 'The safety comes from the key length, not from hiding the algorithm.', 13, fill=MUT))
    return 396, ''.join(o)
FIG[1] = (f1, 'The worked example in three steps: half of 2¹²⁸ keys is about 1.70 × 10³⁸, which takes 1.70 × 10²⁶ s at 10¹² guesses per second, or about 5.40 × 10¹⁸ years.',
          'A keyspace bar with the first half shaded as the expected search, then three stacked results: 1.70 times ten to the 38 keys, 1.70 times ten to the 26 seconds, and 5.40 times ten to the 18 years.')


# ---- 2.2 SHA-256 padding of a 448-bit message ----
def f2():
    x0, W = 20, 680
    sc = W / 1024
    o = [T(20, 28, 'Padding a 448-bit message to a multiple of 512 bits', 15, 'start', bold=True)]
    parts = [(0, 448, 'message, 448 bits', ACS, AC), (448, 449, '', LVS, LV), (449, 960, '511 zero bits', PANEL, L2), (960, 1024, '', NXS, NX)]
    for a, b, lab, f, st in parts:
        o.append(R(x0 + a * sc, 52, max((b - a) * sc, 3), 46, f, st, 2, 1.5))
        if lab: o.append(T(x0 + (a + b) / 2 * sc, 80, lab, 14))
    o.append(A(x0 + 448.5 * sc, 136, x0 + 448.5 * sc, 102, LV, 2, arrow='l'))
    o.append(T(x0 + 448.5 * sc, 154, 'one 1 bit (449 so far)', 13, fill=LV, bold=True))
    o.append(A(x0 + 992 * sc, 136, x0 + 992 * sc, 102, NX, 2, arrow='x'))
    o.append(T(700, 154, 'length field: 64 bits', 13, 'end', NX, True))
    o.append(T(700, 172, 'holding 448', 13, 'end', NX))
    # two blocks
    for i in range(2):
        a = x0 + i * 512 * sc
        o.append(brace(a + 2, a + 512 * sc - 2, 196, AC, up=True))
        o.append(T(a + 256 * sc, 216, f'block {i + 1}: 512 bits', 14, fill=AC, bold=True))
    o.append(T(360, 250, 'k = (448 − 449) mod 512 = 511 zeros;  448 + 1 + 511 + 64 = 1024 = 2 × 512', 14, bold=True))
    # compression chain
    y = 282
    o.append(boxt(20, y, 100, 44, ['IV'], PANEL, L2, 14))
    o.append(boxt(170, y, 170, 44, ['compress block 1', '64 rounds'], ACS, AC, 13))
    o.append(boxt(390, y, 170, 44, ['compress block 2', '64 rounds'], ACS, AC, 13))
    o.append(boxt(606, y, 100, 44, ['digest', '256 bits'], NXS, NX, 13))
    for a, b in ((120, 170), (340, 390), (560, 606)):
        o.append(A(a, y + 22, b - 2, y + 22, AC))
    return 340, ''.join(o)
FIG[2] = (f2, 'The 448-bit message gets one 1 bit, then 511 zero bits, then a 64-bit length, giving 1024 bits: exactly two 512-bit blocks, each run through the 64-round compression to make one 256-bit digest.',
          'A bar 1024 bits long split into the 448-bit message, a single 1 bit, 511 zero bits and a 64-bit length field, with brackets marking two 512-bit blocks, and below a chain from IV through two compressions to the 256-bit digest.')


# ---- 2.3 one edit breaks exactly one prev field ----
def f3():
    blocks = [('Genesis', None, '0000'), ('Block 1', '0000', '0001'), ('Block 2', '0001', '0009'), ('Block 3', '0002', '0003')]
    w, g, y = 140, 40, 60
    o = []
    for i, (name, prev, h) in enumerate(blocks):
        x = 14 + i * (w + g)
        edited = name == 'Block 2'
        rows = ([f'prev  {prev}'] if prev else ['prev  none']) + ([f'hash  0002 → 0009'] if edited else [f'hash  {h}'])
        rf = {1: LV} if edited else ({0: LV} if name == 'Block 3' else {})
        s, hh = block(x, y, w, name + (' (edited)' if edited else ''), rows, PANEL, LV if edited else AC,
                      title_fill=LVS if edited else ACS, row_fills=rf, mono=False)
        o.append(s)
        if i:
            xa = x - g
            ok = name != 'Block 3'
            o.append(A(x, y + 50, xa + 2, y + 50, NX if ok else LV, 2, None if ok else '6 4', 'x' if ok else 'l'))
            o.append(tick(x - g / 2, y + 80, 7) if ok else cross(x - g / 2, y + 80, 7))
    o.append(T(14, 172, 'Check each stored prev against the hash of its parent:', 14, 'start', bold=True))
    rows = [('Block 1', '0000 = H(genesis) 0000', True), ('Block 2', '0001 = H(block 1) 0001', True), ('Block 3', '0002 ≠ H(block 2) 0009', False)]
    for i, (b, t, ok) in enumerate(rows):
        yy = 200 + i * 28
        o.append(T(30, yy, b, 14, 'start', bold=True)); o.append(T(110, yy, t, 14, 'start', NX if ok else LV))
        o.append(tick(330, yy - 5, 6) if ok else cross(330, yy - 5, 6))
    o.append(T(380, 200, 'exactly 1 mismatch', 15, 'start', LV, True))
    o.append(boxt(14, 296, 692, 52, ['Fix block 3: prev 0002 → 0009. Its header changes, so H(block 3) leaves 0003,', 'and a block 4 holding prev 0003 breaks next. The tamper travels forward.'],
                  LVS, LV, 13))
    return 362, ''.join(o)
FIG[3] = (f3, 'Only block 2 is edited, so its hash moves from 0002 to 0009; the links into blocks 1 and 2 still match, and only block 3\'s stored prev, 0002, now fails.',
          'Four blocks in a row, genesis to block 3, each with prev and hash fields; block 2 is edited and its hash changes from 0002 to 0009, and the link from block 3, which still stores 0002, is crossed out. A check list below confirms one mismatch.')


# ---- 2.4 Merkle tree: what T3 → T3' recomputes ----
def f4():
    o = []
    leaves = {'h1': 120, 'h2': 270, 'h3': 450, 'h4': 600}
    mid = {'h12': 195, 'h34': 525}
    yR, yM, yL, yT = 60, 160, 260, 340
    for a, b in (('h12', 'h1'), ('h12', 'h2'), ('h34', 'h3'), ('h34', 'h4')):
        o.append(L(mid[a], yM + 24, leaves[b], yL - 24, LV if a == 'h34' and b == 'h3' else L2, 2.5 if b == 'h3' else 1.8))
    for m in mid:
        o.append(L(360, yR + 24, mid[m], yM - 24, LV if m == 'h34' else L2, 2.5 if m == 'h34' else 1.8))
    o.append(L(leaves['h3'], yL + 24, leaves['h3'], yT - 18, LV, 2.5))
    for k, x in leaves.items():
        if k != 'h3': o.append(L(x, yL + 24, x, yT - 18, L2, 1.8))
    o.append(R(310, yR - 24, 100, 48, LVS, LV, 24))
    o.append(T(360, yR + 6, "R′", 17, bold=True))
    o.append(T(420, yR - 2, "R′ = H(h12 || h34′)", 13, 'start', LV, True))
    o.append(T(420, yR + 16, 'new root', 13, 'start', MUT))
    for k, x in mid.items():
        if k == 'h34':
            o.append(R(x - 44, yM - 24, 88, 48, LVS, LV, 24)); o.append(T(x, yM + 6, "h34′", 16, bold=True))
            o.append(T(x + 52, yM + 6, "= H(h3′ || h4)", 13, 'start', LV))
        else:
            o.append(R(x - 44, yM - 24, 88, 48, NXS, NX, 24)); o.append(T(x, yM + 6, 'h12', 16, bold=True))
            o.append(T(x - 52, yM + 6, 'reused', 13, 'end', NX, True))
    for k, x in leaves.items():
        if k == 'h3':
            o.append(R(x - 40, yL - 24, 80, 48, LVS, LV, 24)); o.append(T(x, yL + 6, "h3′", 16, bold=True))
        else:
            o.append(R(x - 40, yL - 24, 80, 48, PANEL, L2, 24)); o.append(T(x, yL + 6, k, 16, bold=True))
        tl = "T3′" if k == 'h3' else 'T' + k[1]
        o.append(boxt(x - 34, yT - 18, 68, 34, [tl], LVS if k == 'h3' else PANEL, LV if k == 'h3' else L2, 14))
    o.append(T(20, 400, 'Recomputed: h3′, h34′, R′ (3 hashes).  Unchanged: h1, h2, h4 and h12.', 14, 'start', bold=True))
    o.append(T(20, 422, 'The hashes left as they were on the path, h4 and h12, are exactly the siblings a proof for T3 sends.', 13, 'start', MUT))
    return 436, ''.join(o)
FIG[4] = (f4, 'Replacing T3 by T3′ changes only the path from that leaf to the root: h3′, then h34′ = H(h3′ || h4), then R′ = H(h12 || h34′). The left half, h12, is reused untouched.',
          'A four-leaf Merkle tree over T1 to T4. The path T3 prime, h3 prime, h34 prime and the new root R prime is highlighted; h12 is marked reused; h1, h2 and h4 are plain.')


# ---- 2.5 doubling P = (5, 1) on y² = x³ + 2x + 2 over F17 ----
def f5():
    pts = [(0, 6), (0, 11), (3, 1), (3, 16), (5, 1), (5, 16), (6, 3), (6, 14), (7, 6), (7, 11), (9, 1), (9, 16), (10, 6), (10, 11), (13, 7), (13, 10), (16, 4), (16, 13)]
    x0, y1, s = 56, 352, 18
    fx = lambda v: x0 + v * s
    fy = lambda v: y1 - v * s
    o = [T(20, 26, 'The curve over F₁₇: 18 separate points', 14, 'start', bold=True)]
    for v in range(17):
        o.append(L(fx(v), fy(0), fx(v), fy(16), LN, 1)); o.append(L(fx(0), fy(v), fx(16), fy(v), LN, 1))
    for v in (0, 4, 8, 12, 16):
        o.append(T(fx(v), y1 + 18, str(v), 13, fill=MUT)); o.append(T(x0 - 8, fy(v) + 4, str(v), 13, 'end', MUT))
    o.append(T(fx(8), y1 + 38, 'x', 14, fill=MUT)); o.append(T(x0 - 28, fy(8), 'y', 14, fill=MUT))
    for (x, y) in pts:
        if (x, y) in ((5, 1), (6, 3)): continue
        o.append(C(fx(x), fy(y), 4.5, L2))
    o.append(C(fx(5), fy(1), 7, AC)); o.append(Tb(fx(5) - 4, fy(1) - 12, 'P (5, 1)', 13, 'end', AC, True))
    o.append(C(fx(6), fy(3), 7, NX)); o.append(Tb(fx(6) + 10, fy(3) - 12, '2P (6, 3)', 13, 'start', NX, True))
    # steps
    X = 390
    steps = [('slope', 'm = (3·5² + 2) ÷ (2·1) = 77 ÷ 2'), ('reduce', '77 mod 17 = 9'), ('inverse', '2⁻¹ = 9, since 2 × 9 = 18 ≡ 1'),
             ('slope', 'm = 9 × 9 = 81 ≡ 13'), ('x₃', '13² − 2·5 = 159 ≡ 6'), ('y₃', '13(5 − 6) − 1 = −14 ≡ 3'), ('check', '3² = 9 and 6³ + 12 + 2 = 230 ≡ 9')]
    o.append(T(X, 26, 'Point doubling, all mod 17', 14, 'start', bold=True))
    for i, (a, b) in enumerate(steps):
        y = 58 + i * 40
        f, st = (NXS, NX) if i >= 4 else (PANEL, LN)
        o.append(R(X, y - 20, 320, 32, f, st, 6, 1.5))
        o.append(T(X + 10, y + 1, a, 13, 'start', MUT)); o.append(T(X + 72, y + 1, b, 13, 'start'))
    o.append(T(X, 350, 'Answer: 2P = (6, 3)', 15, 'start', NX, True))
    return 400, ''.join(o)
FIG[5] = (f5, 'Over F₁₇ the curve y² = x³ + 2x + 2 is just 18 separate points, not a smooth line. Doubling P = (5, 1) uses 2⁻¹ = 9 in place of division, gives slope 13, and lands on another of those points, 2P = (6, 3).',
          'A 17 by 17 grid with the 18 points of the curve plotted, P at 5,1 and 2P at 6,3 highlighted; beside it seven boxes work the slope, the inverse of 2, x3 equal to 6, y3 equal to 3 and the check.')


# ---- 2.6 toy ECDSA, n = 11 ----
def f6():
    o = []
    o.append(R(14, 14, 300, 340, PANEL, AC, 10))
    o.append(R(406, 14, 300, 340, PANEL, NX, 10))
    o.append(T(164, 40, 'Signer', 15, bold=True)); o.append(T(556, 40, 'Verifier', 15, bold=True))
    o.append(boxt(30, 54, 268, 40, ['secret: d = 3, nonce k = 7'], LVS, LV, 13))
    o.append(T(556, 80, 'knows Q = dG = 3G, z = 5', 13, fill=MUT))
    sig = [('k⁻¹ mod 11', '8   (7 × 8 = 56 ≡ 1)'), ('R = 7G', 'x reduces to r = 4'), ('z + r·d', '5 + 4 × 3 = 17 ≡ 6'), ('s = k⁻¹(z + rd)', '8 × 6 = 48 ≡ 4')]
    ver = [('s⁻¹ mod 11', '3   (4 × 3 = 12 ≡ 1)'), ('u₁ = z·s⁻¹', '5 × 3 = 15 ≡ 4'), ('u₂ = r·s⁻¹', '4 × 3 = 12 ≡ 1'), ('u₁G + u₂Q', '4G + 3G = 7G = R')]
    for i, (a, b) in enumerate(sig):
        y = 124 + i * 44
        o.append(T(30, y, a, 13, 'start', MUT)); o.append(T(30, y + 18, b, 14, 'start', bold=True))
    for i, (a, b) in enumerate(ver):
        y = 124 + i * 44
        o.append(T(422, y, a, 13, 'start', MUT)); o.append(T(422, y + 18, b, 14, 'start', bold=True))
    o.append(boxt(30, 300, 268, 40, ['signature (r, s) = (4, 4)'], ACS, AC, 14))
    o.append(boxt(422, 300, 268, 40, ['x of 7G = 4 = r → accept'], NXS, NX, 14))
    o.append(A(316, 186, 404, 186, AC, 2.5))
    o.append(Tb(360, 172, 'm, (4, 4)', 13, fill=AC, bold=True))
    o.append(T(360, 210, 'only these', 13, fill=MUT)); o.append(T(360, 226, 'travel', 13, fill=MUT))
    o.append(T(360, 380, 'It works because u₁ + u₂·d = 4 + 1 × 3 = 7 = k: the verifier rebuilds R without ever seeing d or k.', 13, fill=MUT))
    return 392, ''.join(o)
FIG[6] = (f6, 'The signer keeps d = 3 and k = 7 secret and sends only the message and (r, s) = (4, 4). The verifier gets u₁ = 4 and u₂ = 1, rebuilds 4G + 3G = 7G = R, and accepts because its x-coordinate 4 equals r.',
          'Two panels, signer and verifier. The signer computes k inverse 8, r 4, z plus r d 6 and s 4; an arrow carries the message and signature 4, 4 across; the verifier computes s inverse 3, u1 4, u2 1 and 4G plus 3G equals 7G, and accepts.')


# ---- 2.7 key to address, in bytes ----
def f7():
    s = 16
    o = []
    def bar(x, y, n, f, st, lab, sub=None):
        out = [R(x, y, n * s, 34, f, st, 4, 1.5)]
        for i in range(1, n):
            out.append(L(x + i * s, y + 4, x + i * s, y + 30, st, 0.6))
        out.append(T(x + n * s / 2, y + 22, lab, 13, bold=True)) if n * s > 90 else None
        return ''.join(out)
    o.append(T(20, 26, 'private key: 32 bytes, kept secret', 13, 'start', MUT))
    o.append(bar(20, 34, 32, LVS, LV, '256-bit secret'))
    o.append(A(150, 70, 150, 94, AC)); o.append(T(160, 88, '× G (one way)', 13, 'start', MUT))
    o.append(T(20, 112, 'public key, compressed: 33 bytes', 13, 'start', MUT))
    o.append(bar(20, 120, 1, ACS, AC, '')); o.append(bar(36, 120, 32, PANEL, AC, 'x coordinate, 32 bytes'))
    o.append(T(28, 172, '02/03', 13, 'start', MUT))
    o.append(A(150, 158, 150, 194, AC)); o.append(T(160, 182, 'HASH160 = RIPEMD-160 of SHA-256 of the key', 13, 'start', MUT))
    o.append(T(20, 212, 'payload: 1 + 20 + 4 = 25 bytes', 13, 'start', MUT))
    o.append(bar(20, 220, 1, ACS, AC, '')); o.append(bar(36, 220, 20, NXS, NX, 'HASH160, 20 bytes')); o.append(bar(356, 220, 4, LVS, LV, ''))
    o.append(T(28, 272, '0x00', 13, 'start', MUT)); o.append(T(388, 272, 'checksum', 13, fill=LV))
    o.append(arc(200, 218, 380, 218, 0.3, LV, 1.8, 'l'))
    o.append(T(470, 168, 'first 4 bytes of', 13, 'start', LV)); o.append(T(470, 186, 'SHA-256(SHA-256(', 13, 'start', LV)); o.append(T(470, 204, 'version || hash160))', 13, 'start', LV))
    o.append(A(220, 258, 220, 294, AC)); o.append(T(230, 284, 'Base58Check', 13, 'start', MUT))
    o.append(boxt(20, 298, 420, 40, ['address text, starts with 1'], PANEL, AC, 14))
    o.append(T(460, 316, 'carries a hash of the key,', 13, 'start', MUT)); o.append(T(460, 334, 'never the key itself', 13, 'start', MUT))
    return 352, ''.join(o)
FIG[7] = (f7, 'Byte by byte: the 33-byte compressed public key is hashed to 20 bytes; a 1-byte version in front and a 4-byte checksum behind make the 25 bytes that Base58Check turns into the address text.',
          'Byte bars: a 32-byte private key, a 33-byte compressed public key with a one-byte prefix, and a 25-byte payload of one version byte, twenty HASH160 bytes and four checksum bytes, then an arrow to the address text starting with 1.')


spec = make_spec(FIG)


def text_fixes(k):
    return {
        2: [('Only a few universities teach the full round schedule; know that the compression function exists and that it is repeated for every block.',
             'You will rarely be asked for the full round schedule; know that the compression function exists and that it is repeated for every block.')],
        5: [('Because the arithmetic is modulo p, the curve is not the smooth drawing you see in the figure. Over a prime field the same equation produces a scattered cloud of integer points, and that scattering is what makes the discrete log hard.',
             'Because the arithmetic is modulo p, the curve is not a smooth line. Over a prime field the same equation produces a scattered cloud of integer points, as the figure shows for p = 17, and that scattering is what makes the discrete log hard.'),
            ('77/2 mod 17 is 77 × 9 = 13, not 38 and not 8.5.', '77/2 mod 17 is 77 × 9 = 693 ≡ 13, not 38 (integer division) and not 38.5.')],
        7: [('HASH160 is RIPEMD160, so its output is 160 bits = 20 bytes.',
             'HASH160 is RIPEMD-160 applied to the SHA-256 hash of the key, so its output is 160 bits = 20 bytes.')],
    }.get(k, [])
