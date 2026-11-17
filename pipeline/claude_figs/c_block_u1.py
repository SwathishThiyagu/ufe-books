"""Claude's hand-drawn figures for c-block-u1 (Blockchain Technology, unit 1: foundations), one per chapter,
each drawn from that chapter's worked example with its own numbers."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blockkit import *

FIG = {}


# ---- 1.1 the three dates on one year line ----
def f1():
    x0, x1 = 150, 690
    fx = lambda yr: x0 + (yr - 2007) / 14 * (x1 - x0)
    o = [xaxis(x0, x1, 310, range(2007, 2022, 2), fx, 'year')]
    lanes = [('1.0 currency', 2008, 2015, ACS, AC, 'Bitcoin'), ('2.0 contracts', 2015, 2017.6, NXS, NX, 'Ethereum'),
             ('3.0 wider use', 2017, 2021, LVS, LV, 'consortium chains')]
    for i, (lab, a, b, f, s, name) in enumerate(lanes):
        y = 182 + i * 40
        o.append(R(fx(a), y, fx(b) - fx(a), 28, f, s, 6))
        o.append(T(fx(a) + 8, y + 19, name, 13, 'start'))
        o.append(T(14, y + 19, lab, 13, 'start', MUT))
    pins = [(2008, '2008', 'whitepaper (Oct)', 34, 'end'), (2009, '2009', 'genesis block (3 Jan)', 34, 'start'), (2015, '2015', 'Ethereum launch', 34, 'middle')]
    for yr, top, sub, y, anc in pins:
        X = fx(yr)
        o.append(L(X, y + 30, X, 306, L2, 1.5, '4 4'))
        o.append(C(X, y + 30, 6, INK))
        dx = {'end': 6, 'start': -6, 'middle': 0}[anc]
        o.append(T(X + dx, y, top, 14, anc, bold=True))
        o.append(T(X + dx, y + 16, sub, 13, anc, MUT))
    o.append(brace(fx(2008), fx(2015), 120, AC, up=False))
    o.append(Tb((fx(2008) + fx(2015)) / 2, 112, '2015 − 2008 = 7 years', 14, fill=AC, bold=True))
    o.append(brace(fx(2009), fx(2015), 158, MUT, up=False))
    o.append(Tb((fx(2009) + fx(2015)) / 2, 150, '2015 − 2009 = 6 years', 13, fill=MUT))
    return 360, ''.join(o)
FIG[1] = (f1, 'The three dates students mix up, on one line: the 2008 whitepaper, the 2009 genesis block and the 2015 Ethereum launch. Blockchain did not begin in 2015; that launch came 7 years after the whitepaper.',
          'A year axis from 2007 to 2021 with pins at 2008 whitepaper, 2009 genesis block and 2015 Ethereum launch, a bracket marking 7 years from 2008 to 2015, and three wave bars: Bitcoin from 2008, Ethereum from 2015, consortium chains from 2017.')


# ---- 1.2 replicated database vs shared validation ----
def f2():
    o = [T(180, 26, 'Replicated database, reconcile later', 15, bold=True), T(540, 26, 'Distributed ledger, shared validation', 15, bold=True)]
    o.append(L(360, 12, 360, 400, LN, 1.5))
    # left: two sites accept at once
    for i, (site, w) in enumerate((('Site 1', 'W1'), ('Site 2', 'W2'))):
        x = 16 + i * 172
        o.append(boxt(x, 48, 160, 52, [site, 'copy shows ₹10,000'], PANEL, AC, 13, bold_first=True))
        o.append(A(x + 80, 102, x + 80, 128, AC))
        o.append(boxt(x, 132, 160, 52, [f'{w} ₹8,000: accepted', 'copy now shows ₹2,000'], NXS, NX, 13))
        o.append(A(x + 80, 186, 180 + (i * 2 - 1) * 20, 232, L2, 2, arrow='m'))
    o.append(T(30, 216, 'at the same time', 13, 'start', MUT))
    o.append(boxt(60, 238, 240, 52, ['reconcile both', '10,000 − 8,000 − 8,000'], PANEL, L2, 13))
    o.append(A(180, 292, 180, 318, LV, 2, arrow='l'))
    o.append(boxt(60, 322, 240, 56, ['−₹6,000', 'overdrawn by ₹6,000'], LVS, LV, 15, bold_first=True))
    # right: one order, each checked against the latest balance
    o.append(boxt(400, 48, 280, 52, ['one agreed order', 'W1 first, then W2'], ACS, AC, 13, bold_first=True))
    o.append(A(540, 102, 540, 128, AC))
    o.append(boxt(400, 132, 280, 52, ['W1 ₹8,000 vs ₹10,000', 'accepted → balance ₹2,000'], NXS, NX, 13))
    o.append(A(540, 186, 540, 234, AC))
    o.append(boxt(400, 238, 280, 52, ['W2 ₹8,000 vs ₹2,000', '2,000 < 8,000 → rejected'], LVS, LV, 13))
    o.append(cross(664, 252, 7))
    o.append(A(540, 292, 540, 318, NX, 2, arrow='x'))
    o.append(boxt(400, 322, 280, 56, ['₹2,000', 'final balance, no overdraft'], NXS, NX, 15, bold_first=True))
    return 396, ''.join(o)
FIG[2] = (f2, 'Left: two sites each check their own copy of ₹10,000, both accept ₹8,000, and reconciling leaves −₹6,000. Right: shared validation puts W1 before W2, so W2 is checked against ₹2,000 and rejected.',
          'Two columns. Left, sites 1 and 2 each accept an 8,000 rupee withdrawal from a copy showing 10,000, and reconciliation gives minus 6,000. Right, the withdrawals are ordered, W1 is accepted leaving 2,000 and W2 is rejected.')


# ---- 1.3 the firm before and after ----
def f3():
    o = []
    for p, (cx, title) in enumerate(((180, 'Before: head office writes'), (540, 'After: all 7 validate'))):
        o.append(T(cx, 26, title, 15, bold=True))
        cy, rr = 168, 104
        pts = [(cx + rr * math.cos(math.radians(-90 + 60 * i)), cy + rr * math.sin(math.radians(-90 + 60 * i))) for i in range(6)]
        if p == 0:
            for (x, y) in pts:
                o.append(A(cx, cy, x - (x - cx) * 0.23, y - (y - cy) * 0.23, AC, 2))
            o.append(node(cx, cy, 'HO', 26, ACS, AC))
            for i, (x, y) in enumerate(pts):
                o.append(node(x, y, f'B{i + 1}', 22, PANEL, L2, 13))
        else:
            allp = [(cx, cy)] + pts
            for i in range(7):
                for j in range(i + 1, 7):
                    o.append(L(*allp[i], *allp[j], NX, 1.2))
            o.append(node(cx, cy, 'HO', 26, NXS, NX))
            for i, (x, y) in enumerate(pts):
                o.append(node(x, y, f'B{i + 1}', 22, NXS, NX, 13))
    o.append(T(180, 314, 'writers 1 of 7 = 1/7 ≈ 14.3%', 14, bold=True))
    o.append(T(180, 334, '7 copies, 6 of them read-only', 13, fill=MUT))
    o.append(T(180, 354, 'centralized control, distributed storage', 13, fill=MUT))
    o.append(T(540, 314, 'validators 7 of 7 = 100%', 14, bold=True))
    o.append(T(540, 334, '7 ledger copies, shared validation', 13, fill=MUT))
    o.append(T(540, 354, 'membership and upgrades may stay central', 13, fill=MUT))
    o.append(L(360, 12, 360, 360, LN, 1.5))
    return 372, ''.join(o)
FIG[3] = (f3, 'The same 7 sites, 1 head office and 6 branches. Before, only the head office writes (1/7 ≈ 14.3%) even though all 7 hold copies; after, all 7 validate on a shared ledger (7/7 = 100%).',
          'Left, a hub and spoke: the head office HO sends writes to six branch copies B1 to B6. Right, the same seven sites all linked to each other and all shaded as validators.')


# ---- 1.4 three claims tested ----
def f4():
    o = []
    cols = [(20, 'Claim 1: unhackable'), (256, 'Claim 2: anonymous'), (492, 'Claim 3: free')]
    for x, t in cols:
        o.append(R(x, 14, 208, 312, PANEL, LN, 10, 1.5))
        o.append(T(x + 104, 40, t, 14, bold=True))
        o.append(R(x + 44, 282, 120, 30, LVS, LV, 15, 1.5))
        o.append(T(x + 104, 302, 'fails', 14, fill=LV, bold=True))
    shares = [45, 25, 15, 10, 5]
    x, y0, hgt = 44, 60, 200
    fy = lambda p: y0 + p / 100 * hgt
    acc = 0
    for i, s in enumerate(shares):
        f, st = (LVS, LV) if i < 2 else (PANEL, L2)
        o.append(R(x, fy(acc), 52, fy(acc + s) - fy(acc), f, st, 2, 1.5))
        if s >= 15: o.append(T(x + 26, (fy(acc) + fy(acc + s)) / 2 + 5, f'{s}%', 13))
        acc += s
    o.append(T(x + 58, fy(97) + 4, '10%, 5%', 13, 'start', MUT))
    o.append(L(x - 8, fy(50), x + 160, fy(50), INK, 2, '6 4'))
    o.append(T(x + 62, fy(50) + 18, '50% line', 13, 'start'))
    o.append(P([(x + 56, fy(0) + 1), (x + 62, fy(0) + 1), (x + 62, fy(70) - 1), (x + 56, fy(70) - 1)], LV, 2.5))
    o.append(T(x + 70, fy(12), 'top two', 13, 'start', LV, True))
    o.append(T(x + 70, fy(12) + 17, '45 + 25 = 70%', 13, 'start', LV, True))
    o.append(T(x + 70, fy(68) + 6, 'one pool alone:', 13, 'start', MUT))
    o.append(T(x + 70, fy(68) + 23, '45% < 50%', 13, 'start', MUT))
    ax = 300
    o.append(T(360, 62, 'every address is public', 13, fill=MUT))
    for i, a in enumerate(('addr 1', 'addr 2', 'addr 3')):
        yy = 74 + i * 54
        o.append(boxt(ax, yy, 120, 34, [a], ACS, AC, 13))
        if i: o.append(A(ax + 60, yy - 18, ax + 60, yy - 2, AC))
    o.append(boxt(270, 228, 180, 44, ['KYC names addr 1', '→ whole history exposed'], LVS, LV, 13))
    fx0 = 521
    for r in range(10):
        for c in range(10):
            o.append(R(fx0 + c * 15, 58 + r * 15, 12, 12, LVS, LV, 2, 1))
    o.append(T(596, 230, '100 transactions', 13, fill=MUT))
    o.append(T(596, 254, '100 × ₹40 = ₹4,000', 14, bold=True))
    o.append(boxt(150, 340, 420, 40, ['Still real: tamper-evidence and availability'], NXS, NX, 14))
    return 392, ''.join(o)
FIG[4] = (f4, 'Each claim against the example\'s numbers: no single pool passes 50%, but the top two hold 45% + 25% = 70%; every address is public, so one KYC link exposes a history; 100 transactions at ₹40 cost ₹4,000.',
          'Three panels. A stacked bar of pool shares 45, 25, 15, 10 and 5 percent with a 50 percent line and the top two pools bracketed at 70 percent; a chain of three public addresses with a KYC link; a grid of 100 transactions costing 4,000 rupees. Each panel says fails.')


# ---- 1.5 read / write / validate table ----
def f5():
    cols = ['type', 'read', 'write', 'validate', 'example']
    xs = [14, 140, 268, 396, 548]
    ws = [122, 124, 124, 148, 160]
    o = []
    for i, c in enumerate(cols):
        o.append(T(xs[i] + ws[i] / 2, 30, c, 14, bold=True, fill=(AC if c == 'validate' else INK)))
    o.append(R(xs[3] - 3, 40, ws[3] + 6, 3 * 72 + 6, 'none', AC, 8, 2.5))
    rows = [('Public', ['anyone'], ['anyone'], ['anyone'], ['Bitcoin'], PANEL, L2),
            ('Private', ['citizens'], ['registry', 'offices only'], ['13 offices of', 'one department'], ['land registry', '1 + 12 = 13'], ACS, AC),
            ('Consortium', ['member banks'], ['3 banks'], ['3 banks,', 'separate firms'], ['trade finance'], NXS, NX)]
    for r, (name, rd, wr, va, ex, f, st) in enumerate(rows):
        y = 46 + r * 72
        o.append(boxt(xs[0], y, ws[0], 62, [name], f, st, 14, bold_first=True))
        for i, cell in enumerate((rd, wr, va, ex), start=1):
            o.append(boxt(xs[i], y, ws[i], 62, cell, PANEL, LN, 13))
    o.append(T(xs[3] + ws[3] / 2, 284, 'the deciding column', 13, fill=AC, bold=True))
    o.append(T(14, 314, 'Citizens reading the land records does not make that chain public: write and validate stay closed.', 13, 'start'))
    return 328, ''.join(o)
FIG[5] = (f5, 'The type follows from who may write and validate. The land registry\'s 13 validating offices belong to one department, so it is private; the 3 separate banks share validation, so theirs is a consortium chain.',
          'A table with rows public, private and consortium and columns read, write, validate and example; the validate column is outlined. The private row holds the land registry with 13 offices, the consortium row the trade-finance chain with 3 banks.')


# ---- 1.6 the edit that breaks the next block ----
def f6():
    o = []
    s, h = block(14, 40, 170, 'Block 19', ['header', 'hash = 0000a1'], PANEL, L2, title_fill=PANEL)
    o.append(s)
    s, h20 = block(234, 40, 210, 'Block 20', ['prev  0000a1', 'root  7c2e → 7d5f', 'nonce 18 → must re-mine', 'Tx 1', 'Tx 2  (edited)', 'Tx 3'],
                   PANEL, AC, row_fills={1: LV, 2: LV, 4: LV})
    o.append(s)
    o.append(L(240, 40 + 30 + 3 * 19 + 2, 438, 40 + 30 + 3 * 19 + 2, LN, 1.5))
    s, h21 = block(520, 40, 186, 'Block 21', ['prev  old H(20)', 'root, nonce', 'its own txs'], PANEL, LV, title_fill=LVS, row_fills={0: LV})
    o.append(s)
    o.append(A(234, 70, 186, 70, L2, 2, arrow='m'))
    o.append(T(210, 60, 'prev', 13, fill=MUT))
    o.append(A(520, 70, 446, 70, LV, 2, '6 4', arrow='l'))
    o.append(cross(482, 70, 7))
    o.append(T(482, 102, 'no longer', 13, fill=LV)); o.append(T(482, 118, 'matches', 13, fill=LV))
    o.append(T(14, 228, 'What one edit to Tx 2 forces', 15, 'start', bold=True))
    steps = [('1', 'Tx 2 changes, so the Merkle root changes (7c2e → 7d5f).'),
             ('2', 'Block 20\'s header changes: its old hash is invalid, find a new nonce.'),
             ('3', 'Block 21 still stores the old H(20): update prev, re-mine Block 21.'),
             ('4', 'Every later block repeats step 3: re-mine them all.'),
             ('5', 'The edited chain wins only if it beats the honest chain (more total work).')]
    for i, (n, t) in enumerate(steps):
        y = 252 + i * 30
        o.append(C(28, y, 11, LV if i < 4 else AC)); o.append(T(28, y + 5, n, 13, fill='var(--fig)', bold=True))
        o.append(T(48, y + 5, t, 14, 'start'))
    return 404, ''.join(o)
FIG[6] = (f6, 'Editing Tx 2 changes Block 20\'s Merkle root from 7c2e to 7d5f, so Block 20 needs a new nonce and gets a new hash, and Block 21\'s stored previous hash no longer matches. Block 21 and every later block must be re-mined.',
          'Three blocks in a row. Block 20 lists prev 0000a1, root 7c2e changing to 7d5f, nonce 18 and transactions with Tx 2 edited; the link from Block 21, which stores the old hash of Block 20, is crossed out. Five numbered steps below.')


# ---- 1.7 one transaction through a small network ----
def f7():
    pos = {'L1': (70, 120), 'F1': (220, 120), 'F2': (400, 60), 'F3': (400, 220), 'F4': (560, 120), 'L2': (680, 120)}
    o = []
    for a, b in (('F2', 'F3'), ('F2', 'F4'), ('F3', 'F4')):
        o.append(L(*pos[a], *pos[b], L2, 2))
    o.append(L(*pos['F4'], *pos['L2'], L2, 2))
    o.append(edge(pos['L1'], pos['F1'], 28, c=LV, w=3, arrow='l'))
    o.append(Tb(145, 108, 'tx1', 13, fill=LV, bold=True))
    for t in ('F2', 'F3', 'F4'):
        o.append(edge(pos['F1'], pos[t], 30, c=AC, w=2.5))
    o.append(Tb(300, 76, 'relay', 13, fill=AC)); o.append(Tb(300, 186, 'relay', 13, fill=AC)); o.append(Tb(330, 136, 'relay', 13, fill=AC))
    for f, miner in (('F1', True), ('F2', True), ('F3', True), ('F4', False)):
        x, y = pos[f]
        o.append(R(x - 30, y - 22, 60, 44, ACS, AC, 8))
        o.append(T(x, y + 5, f, 15, bold=True))
        o.append(T(x, y + 38, 'full + miner' if miner else 'full', 13, fill=MUT))
    for l in ('L1', 'L2'):
        x, y = pos[l]
        o.append(R(x - 24, y - 20, 48, 40, LVS, LV, 14))
        o.append(T(x, y + 5, l, 14, bold=True))
        o.append(T(x, y + 36, 'light', 13, fill=MUT))
    # counts
    o.append(R(20, 286, 680, 86, PANEL, LN, 10, 1.5))
    rows = [('validate and store the full block', '4', 'F1, F2, F3, F4'), ('store headers only', '2', 'L1, L2'),
            ('if all 4 full nodes stop', '0', 'L1 and L2 cannot confirm tx1')]
    for i, (a, n, b) in enumerate(rows):
        y = 310 + i * 24
        o.append(T(36, y, a, 14, 'start')); o.append(T(330, y, n, 15, bold=True)); o.append(T(356, y, b, 13, 'start', MUT))
    return 384, ''.join(o)
FIG[7] = (f7, 'Light wallet L1 hands tx1 to its full node F1, which checks it and relays it to F2, F3 and F4. All 4 full nodes validate and store the block, the 2 light wallets keep headers only, and without the full nodes they cannot confirm anything.',
          'A network: light wallet L1 linked to full node F1, F1 relaying to full nodes F2, F3 and F4, which are linked to each other, and light wallet L2 linked to F4. F1 to F3 are marked miner. A table below counts 4 full stores, 2 header-only wallets.')


spec = make_spec(FIG)


def text_fixes(k):
    return {
        3: [('Most real systems are partial. The figure shows the common route.',
             'Most real systems are partial. The figure shows the firm from the worked example before and after it takes this route.')],
    }.get(k, [])


def drop_sources():
    # university-hosted pages: the books name no universities
    return ['ocw.mit.edu', 'princeton.edu']
