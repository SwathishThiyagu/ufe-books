"""Claude's hand-drawn figures for c-block-u3 (Blockchain Technology, unit 3: peer-to-peer networks and consensus),
one per chapter, each drawn from that chapter's worked example with its own numbers."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blockkit import *

FIG = {}


# ---- 3.1 flooding with fan-out 3 and TTL 3 ----
def f1():
    o = []
    ys = [40, 120, 200, 280]
    xs27 = [40 + i * 18.5 for i in range(27)]
    xs9 = [sum(xs27[3 * i:3 * i + 3]) / 3 for i in range(9)]
    xs3 = [sum(xs9[3 * i:3 * i + 3]) / 3 for i in range(3)]
    xo = sum(xs3) / 3
    for i, x in enumerate(xs3): o.append(L(xo, ys[0] + 14, x, ys[1] - 11, AC, 1.8))
    for i, x in enumerate(xs9): o.append(L(xs3[i // 3], ys[1] + 11, x, ys[2] - 9, AC, 1.5))
    for i, x in enumerate(xs27): o.append(L(xs9[i // 3], ys[2] + 9, x, ys[3] - 7, AC, 1.2))
    o.append(node(xo, ys[0], 'O', 14, ACS, AC, 13))
    for x in xs3: o.append(C(x, ys[1], 11, AC, ACS))
    for x in xs9: o.append(C(x, ys[2], 9, AC, ACS))
    for x in xs27: o.append(C(x, ys[3], 6, LV))
    lab = [('originator keeps 1 copy', ''), ('hop 1: 3 copies', 'sent so far 3'), ('hop 2: 3 × 3 = 9', 'sent so far 12'),
           ('hop 3: 9 × 3 = 27', 'sent so far 39')]
    for i, (a, b) in enumerate(lab):
        o.append(T(560, ys[i] - 2, a, 14, 'start', LV if i == 3 else INK, True))
        if b: o.append(T(560, ys[i] + 16, b, 13, 'start', MUT))
    o.append(T(40, 314, 'TTL reaches 0: these 27 peers stop forwarding', 13, 'start', LV))
    o.append(boxt(40, 330, 640, 40, ['copies sent 3 + 9 + 27 = 39;  copies that exist 39 + 1 = 40'], ACS, AC, 14))
    return 384, ''.join(o)
FIG[1] = (f1, 'Each hop multiplies the copies by the fan-out of 3: 3, then 9, then 27. The hop limit stops the 27 peers of the last round, so peers send 39 copies in all, and 40 copies exist once the originator\'s own copy is counted.',
          'A tree from the originator O to 3 peers, then 9, then 27 at the bottom, with labels for each hop: 3 copies, 9 copies for 12 sent, 27 copies for 39 sent, and a note that 40 copies exist.')


# ---- 3.2 fee rate decides the order ----
def f2():
    sc = 680 / 1750
    o = [T(20, 28, 'Mempool: fee rate = fee ÷ size', 15, 'start', bold=True)]
    txs = [('T1', 250, 5000, 20, PANEL, AC), ('T2', 500, 15000, 30, ACS, AC), ('T3', 1000, 10000, 10, LVS, LV)]
    x = 20
    for name, size, fee, rate, f, st in txs:
        w = size * sc
        o.append(R(x, 44, w, 46, f, st, 4))
        o.append(T(x + w / 2, 64, f'{name}: {size} B', 13, bold=True))
        o.append(T(x + w / 2, 82, f'{fee:,} sat', 13, fill=MUT))
        o.append(T(x + w / 2, 110, f'{fee:,} ÷ {size} = {rate} sat/B', 13, fill=st))
        x += w
    o.append(T(20, 152, 'Block, filled highest fee rate first', 15, 'start', bold=True))
    x = 20
    for i, (name, size, fee, rate, f, st) in enumerate((txs[1], txs[0], txs[2])):
        w = size * sc
        o.append(R(x, 168, w, 46, f, st, 4))
        o.append(T(x + w / 2, 196, f'{i + 1}. {name}, {rate} sat/B', 14, bold=True))
        x += w
    o.append(brace(20, 700, 226, INK))
    o.append(T(360, 252, '250 + 500 + 1000 = 1750 bytes,  5000 + 15000 + 10000 = 30000 sat', 14, bold=True))
    o.append(T(360, 274, 'block average 30000 ÷ 1750 ≈ 17.14 sat/B', 14))
    o.append(T(360, 306, 'Ranking by total fee instead (T2, T3, T1) would put the 10 sat/B transaction second.', 13, fill=MUT))
    return 320, ''.join(o)
FIG[2] = (f2, 'Each box is as wide as its transaction. By fee rate the order is T2 (30 sat/B), T1 (20), T3 (10), even though T3 is the largest; the 1750-byte block carries 30000 satoshi, about 17.14 sat/B.',
          'Three transaction boxes sized by bytes, T1 250, T2 500, T3 1000, with their fee rates 20, 30 and 10 satoshi per byte, then a 1750-byte block filled in the order T2, T1, T3.')


# ---- 3.3 two quorums of 5 out of 7 must overlap ----
def f3():
    o = [T(20, 28, 'n = 7 validators, f = 2 may lie, quorum = 2f + 1 = 5', 15, 'start', bold=True)]
    xs = [80 + i * 80 for i in range(7)]
    y = 140
    o.append(R(xs[0] - 34, 70, xs[4] - xs[0] + 68, 44, ACS, AC, 10, 1.5))
    o.append(T(xs[0] - 26, 98, 'quorum A: V1–V5', 13, 'start', AC, True))
    o.append(R(xs[2] - 34, 166, xs[6] - xs[2] + 68, 44, NXS, NX, 10, 1.5))
    o.append(T(xs[6] + 26, 194, 'quorum B: V3–V7', 13, 'end', NX, True))
    o.append(R(xs[2] - 30, y - 30, xs[4] - xs[2] + 60, 60, LVS, LV, 12, 2.5))
    for i, x in enumerate(xs):
        o.append(node(x, y, f'V{i + 1}', 22, PANEL, LV if 2 <= i <= 4 else L2, 13))
    o.append(T(xs[3], 236, 'shared: 5 + 5 − 7 = 3 validators, more than f = 2', 14, fill=LV, bold=True))
    o.append(T(xs[3], 256, 'so at least one honest validator sits in both and will not vote for two conflicting blocks', 13, fill=MUT))
    o.append(R(20, 278, 330, 92, PANEL, LN, 10, 1.5))
    o.append(T(36, 302, 'n ≥ 3f + 1', 14, 'start', bold=True))
    o.append(T(36, 324, 'n = 7: 3f ≤ 6, so f = 2', 13, 'start'))
    o.append(T(36, 344, 'to survive f = 3: n ≥ 10', 13, 'start'))
    o.append(R(370, 278, 330, 92, PANEL, LN, 10, 1.5))
    o.append(T(386, 302, 'Proof of Work: 40 of 100 GH/s', 14, 'start', bold=True))
    o.append(R(386, 316, 300, 22, PANEL, L2, 3))
    o.append(R(386, 316, 120, 22, LVS, LV, 3))
    o.append(L(536, 310, 536, 344, INK, 2, '4 3'))
    o.append(T(446, 332, '40%', 13, bold=True))
    o.append(T(386, 360, 'dashed line = half; 40% cannot outrun', 13, 'start', MUT))
    return 384, ''.join(o)
FIG[3] = (f3, 'Any two quorums of 5 out of 7 validators share at least 3 members, and with at most 2 liars one of those 3 is honest, so two conflicting blocks cannot both be finalised. The attacker\'s 40% of hash power is below half.',
          'Seven validators in a row; quorum A covers V1 to V5, quorum B covers V3 to V7, and the three shared validators V3, V4, V5 are highlighted. Below, the rule n at least 3f plus 1 and a bar with 40 percent of hash power left of the half mark.')


# ---- 3.4 the puzzle and the retarget ----
def f4():
    o = [T(20, 28, 'One try: the hash must start with four zero hex digits', 15, 'start', bold=True)]
    digits = '0000' + 'a3f91c07e2b84d'
    for i, ch in enumerate(digits):
        x = 20 + i * 34
        o.append(R(x, 42, 30, 38, LVS if i < 4 else PANEL, LV if i < 4 else LN, 4, 1.5))
        o.append(TM(x + 15, 67, ch, 17, bold=i < 4))
    o.append(T(640, 67, '… 64 digits', 13, 'start', MUT))
    o.append(T(88, 102, 'each 1/16', 13, fill=LV))
    o.append(T(20, 134, 'p = (1/16)⁴ = 1/65,536 ≈ 1.526 × 10⁻⁵   →   expected tries = 65,536', 14, 'start', bold=True))
    o.append(T(20, 158, 'at 2 × 10¹¹ hashes per second: 65,536 ÷ (2 × 10¹¹) ≈ 3.28 × 10⁻⁷ s.  Checking a found block takes one hash.', 13, 'start', MUT))
    o.append(L(20, 178, 700, 178, LN, 1.5))
    o.append(T(20, 206, 'Retarget after 2016 blocks', 15, 'start', bold=True))
    sc = 600 / 14
    o.append(R(100, 222, 14 * sc, 32, PANEL, L2, 4)); o.append(T(90, 243, 'target', 13, 'end', MUT))
    o.append(T(100 + 7 * sc, 243, '2016 × 10 min = 20,160 min = 14 days', 13))
    o.append(R(100, 266, 12 * sc, 32, ACS, AC, 4)); o.append(T(90, 287, 'actual', 13, 'end', MUT))
    o.append(T(100 + 6 * sc, 287, '12 days = 17,280 min', 13, bold=True))
    o.append(T(100 + 13 * sc, 287, 'too fast', 13, fill=LV))
    o.append(boxt(100, 316, 600, 44, ['new difficulty = old × 20,160 ÷ 17,280 = old × 1.1667, a rise of 16.67%'], NXS, NX, 14))
    return 372, ''.join(o)
FIG[4] = (f4, 'Four leading zero hex digits happen once in 16⁴ = 65,536 tries. When 2016 blocks take 12 days instead of 14, the next difficulty is the old one × 14/12 ≈ 1.1667, a rise of about 16.67%.',
          'A row of hash digits starting with four zeros, each zero with chance one in sixteen, and the 65,536 tries; below, a 14-day target bar against a 12-day actual bar and the new difficulty factor 1.1667.')


# ---- 3.5 stake-weighted chance and B's penalty ----
def f5():
    sc = 600 / 1000
    o = [T(20, 28, 'Before: 1000 tokens staked', 15, 'start', bold=True)]
    vals = [('A', 500, ACS, AC), ('B', 300, NXS, NX), ('C', 150, PANEL, L2), ('D', 50, PANEL, L2)]
    x = 96
    for n, v, f, st in vals:
        w = v * sc
        o.append(R(x, 44, w, 44, f, st, 3))
        o.append(T(x + w / 2, 72, n if v < 100 else f'{n}: {v}', 14, bold=True))
        o.append(T(x + w / 2, 108, f'{v / 10:g}%', 13))
        o.append(T(x + w / 2, 126, f'{int(v / 10)} blocks', 13, fill=MUT))
        x += w
    o.append(T(84, 108, 'chance', 13, 'end', MUT)); o.append(T(84, 126, 'in 100', 13, 'end', MUT))
    o.append(T(20, 172, 'B double-signs: penalty 5% × 300 = 15 tokens destroyed', 15, 'start', bold=True))
    x = 96
    vals2 = [('A', 500, ACS, AC), ('B', 285, NXS, NX), ('cut', 15, LVS, LV), ('C', 150, PANEL, L2), ('D', 50, PANEL, L2)]
    for n, v, f, st in vals2:
        w = v * sc
        if n == 'cut':
            o.append(R(x, 188, w, 44, f, st, 2, 1.5, '4 3'))
            o.append(A(x + w / 2, 254, x + w / 2, 236, LV, 2, arrow='l'))
            o.append(T(x + w / 2, 270, '15 gone', 13, fill=LV, bold=True))
        else:
            o.append(R(x, 188, w, 44, f, st, 3))
            o.append(T(x + w / 2, 216, n if v < 100 else f'{n}: {v}', 14, bold=True))
        x += w
    o.append(T(40, 304, 'B against the old total:  285 ÷ 1000 = 28.5%', 14, 'start'))
    o.append(T(40, 328, 'B against the new total:  285 ÷ 985 = 28.93%', 14, 'start', NX, True))
    o.append(T(40, 352, 'total after the burn = 1000 − 15 = 985 tokens', 13, 'start', MUT))
    return 366, ''.join(o)
FIG[5] = (f5, 'Each validator\'s slice of the bar is its chance: 50%, 30%, 15% and 5%, so 50, 30, 15 and 5 blocks in 100. B\'s 15-token penalty leaves 285 out of a new total of 985, a chance of 28.93%.',
          'A bar split 500, 300, 150, 50 for validators A to D with chances 50, 30, 15 and 5 percent; below, the same bar with 15 tokens cut out of B, leaving 285 of 985, 28.93 percent.')


# ---- 3.6 PoET and round robin on time lines ----
def f6():
    o = [T(20, 28, 'PoET: each validator sleeps its random wait', 15, 'start', bold=True)]
    sc = 76
    x0 = 70
    for i, (n, w) in enumerate((('A', 4), ('B', 2), ('C', 7))):
        y = 44 + i * 36
        o.append(T(x0 - 12, y + 19, n, 14, 'end', bold=True))
        f, st = (NXS, NX) if n == 'B' else (PANEL, L2)
        o.append(R(x0, y, w * sc, 26, f, st, 4))
        o.append(T(x0 + w * sc + 8, y + 18, f'{w} s', 13, 'start', NX if n == 'B' else MUT, n == 'B'))
    o.append(L(x0 + 2 * sc, 40, x0 + 2 * sc, 160, NX, 2, '5 4'))
    o.append(Tb(x0 + 2 * sc + 6, 172, 'B wakes first at 2 s and proposes, with a signed proof', 13, 'start', NX, True))
    o.append(T(20, 214, 'Round robin: N = 3, T = 5 s, slot 1 = A', 15, 'start', bold=True))
    sw = 78
    for s in range(8):
        x = 40 + s * sw
        who = 'ABC'[s % 3]
        hit = s == 6
        o.append(R(x, 230, sw - 4, 44, LVS if hit else PANEL, LV if hit else L2, 4, 2.5 if hit else 1.5))
        o.append(T(x + (sw - 4) / 2, 250, f'slot {s + 1}', 13, fill=MUT))
        o.append(T(x + (sw - 4) / 2, 268, who, 14, bold=True))
        o.append(T(x, 292, f'{s * 5}', 13, fill=MUT))
    o.append(T(40 + 8 * sw, 292, '40 s', 13, fill=MUT))
    o.append(T(40, 324, 'slot 7: proposer = ((7 − 1) mod 3) + 1 = 1 → A;  start = (7 − 1) × 5 = 30 s, runs 30–35 s', 14, 'start', bold=True))
    return 338, ''.join(o)
FIG[6] = (f6, 'PoET: the waits are A 4 s, B 2 s and C 7 s, so B wakes first and proposes at 2 s. Round robin with 3 validators and 5 s slots gives slot 7 to A, from 30 s to 35 s.',
          'Top, three wait bars of 4, 2 and 7 seconds with B, the shortest, marked as proposer at 2 seconds. Bottom, eight 5-second slots labelled A, B, C, A, B, C, A, B with slot 7, A, highlighted from 30 to 35 seconds.')


# ---- 3.7 hard fork: two chains grow at different speeds ----
def f7():
    o = [T(20, 28, 'Split at height 100, difficulty held fixed', 15, 'start', bold=True)]
    x0, x1 = 150, 690
    sc = (x1 - x0) / 2016
    o.append(R(20, 120, 110, 40, PANEL, L2, 4)); o.append(T(75, 145, 'blocks 1–100', 13))
    o.append(P([(130, 140), (140, 140), (140, 82), (150, 82)], L2, 2))
    o.append(P([(140, 140), (140, 198), (150, 198)], L2, 2))
    o.append(R(x0, 62, 2016 * sc, 40, ACS, AC, 4))
    o.append(T(x0 + 1008 * sc, 87, 'new rules, 85% of hash power: 2016 blocks', 14, bold=True))
    o.append(T(x1 - 8, 122, 'height 100 + 2016 = 2116', 13, 'end', AC, True))
    o.append(R(x0, 178, 356 * sc, 40, LVS, LV, 4))
    o.append(T(x0 + 356 * sc + 10, 196, 'old rules, 15%: 356 blocks', 14, 'start', bold=True))
    o.append(T(x0 + 356 * sc + 10, 214, 'height 100 + 356 = 456', 13, 'start', LV, True))
    o.append(L(x1, 56, x1, 230, INK, 1.5, '4 4'))
    o.append(T(x1 - 6, 246, 'same moment', 13, 'end', MUT))
    o.append(T(20, 284, 'old : new block rate = 15 : 85 = 3 : 17,  2016 × 3 ÷ 17 = 355.76 ≈ 356 blocks', 14, 'start', bold=True))
    o.append(T(20, 308, 'Hard fork: old nodes reject new blocks, so two chains survive. Soft fork: old nodes accept them, so one chain remains.', 13, 'start', MUT))
    return 322, ''.join(o)
FIG[7] = (f7, 'After the split at height 100, the chain with 85% of the hash power mines 2016 blocks (height 2116) while the 15% chain mines about 356 (height 456) in the same time. A hard fork leaves two chains like this.',
          'A shared chain to height 100 branches into a long bar of 2016 new-rule blocks reaching height 2116 and a short bar of 356 old-rule blocks reaching height 456, with a dashed line marking the same moment.')


spec = make_spec(FIG)


def text_fixes(k):
    return {
        3: [('40% < 51%, so it', '40% < 50%, so it'),
            ('holds 40%, below 51%, so', 'holds 40%, below half (50%), so'),
            ('and 45% < 51%, so', 'and 45% < 50%, so')],
    }.get(k, [])
