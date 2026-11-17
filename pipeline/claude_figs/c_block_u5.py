"""Claude's hand-drawn figures for c-block-u5 (Blockchain Technology, unit 5: Ethereum and smart contracts), one per
chapter, each drawn from that chapter's worked example with its own numbers."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blockkit import *

FIG = {}


def table(x, y, cols, rows, cw, rh=34, head_fill=PANEL, marks=None):
    """a small grid: cols is the header list, rows a list of (label, cells); marks maps (r, c) to (fill, stroke)"""
    o = []
    for j, c in enumerate(cols):
        o.append(T(x + sum(cw[:j]) + cw[j] / 2, y + 22, c, 13, bold=True, fill=MUT))
    for i, row in enumerate(rows):
        yy = y + 32 + i * rh
        for j, cell in enumerate(row):
            f, s = (marks or {}).get((i, j), (PANEL, LN))
            o.append(R(x + sum(cw[:j]) + 2, yy, cw[j] - 4, rh - 4, f, s, 5, 1.3))
            o.append(T(x + sum(cw[:j]) + cw[j] / 2, yy + rh / 2 + 3, cell, 14, bold=(j == 0)))
    return ''.join(o)


# ---- 5.1 one transaction through the world state ----
def f1():
    o = [T(20, 26, 'World state before and after one 0.3 ETH transaction', 15, 'start', bold=True)]
    o.append(table(20, 36, ['account', 'balance', 'nonce'], [['user', '2 ETH', '7'], ['contract', '0 ETH', '–']], [100, 100, 70]))
    o.append(T(155, 158, 'before', 13, fill=MUT))
    o.append(table(430, 36, ['account', 'balance', 'nonce'], [['user', '1.699 ETH', '8'], ['contract', '0.3 ETH', '–']], [100, 110, 60],
                   marks={(0, 1): (NXS, NX), (0, 2): (NXS, NX), (1, 1): (NXS, NX)}))
    o.append(T(565, 158, 'after the block', 13, fill=MUT))
    o.append(A(296, 88, 426, 88, AC, 2.5))
    o.append(Tb(361, 76, 'signed tx', 13, fill=AC, bold=True))
    o.append(T(361, 108, 'nonce 7', 13, fill=MUT))
    # the money split
    o.append(T(20, 186, 'Where the 0.301 ETH that leaves the user goes', 14, 'start', bold=True))
    sc = 600 / 0.301
    o.append(R(40, 200, 0.3 * sc, 40, NXS, NX, 4)); o.append(T(40 + 0.15 * sc, 225, '0.3 ETH value → contract', 14, bold=True))
    o.append(R(40 + 0.3 * sc, 200, 0.001 * sc, 40, LVS, LV, 1, 1.5))
    o.append(A(40 + 0.3005 * sc, 268, 40 + 0.3005 * sc, 244, LV, 2, arrow='l'))
    o.append(T(660, 286, 'fee 0.001 ETH = gasUsed × gas price', 13, 'end', LV, True))
    o.append(T(660, 306, 'base fee burned, tip to the block producer; never to the contract', 13, 'end', MUT))
    o.append(T(20, 340, '2 − 0.3 − 0.001 = 1.699 ETH;  nonce 7 + 1 = 8;  contract 0 + 0.3 = 0.3 ETH', 14, 'start', bold=True))
    return 356, ''.join(o)
FIG[1] = (f1, 'The worked example as two snapshots of the world state: the user goes from 2 ETH and nonce 7 to 1.699 ETH and nonce 8, the contract from 0 to 0.3 ETH, and the 0.001 ETH fee goes to the network, not the contract.',
          'Two small tables of accounts, before with the user at 2 ETH and nonce 7 and the contract at 0, after with the user at 1.699 ETH and nonce 8 and the contract at 0.3 ETH; below, a bar splitting the 0.301 ETH into 0.3 value and a 0.001 fee.')


# ---- 5.2 gas fee in wei, gwei and ETH ----
def f2():
    o = [T(20, 26, 'Fee = gasUsed × gasPrice, in three units', 15, 'start', bold=True)]
    rows = [('wei', '21,000 × 2 × 10¹⁰', '= 4.2 × 10¹⁴ wei'), ('gwei', '21,000 × 20', '= 420,000 gwei'), ('ETH', '4.2 × 10¹⁴ ÷ 10¹⁸', '= 0.00042 ETH')]
    for i, (u, a, b) in enumerate(rows):
        y = 44 + i * 48
        o.append(boxt(20, y, 80, 38, [u], ACS, AC, 14, bold_first=True))
        o.append(T(120, y + 25, a, 14, 'start')); o.append(T(330, y + 25, b, 14, 'start', bold=True))
    o.append(T(530, 70, '1 gwei = 10⁹ wei', 13, 'start', MUT)); o.append(T(530, 92, '1 ETH = 10¹⁸ wei', 13, 'start', MUT))
    o.append(T(530, 114, '20 gwei = 2 × 10¹⁰ wei', 13, 'start', MUT))
    o.append(T(20, 222, 'Total debit = value + fee', 15, 'start', bold=True))
    sc = 600 / 0.10042
    o.append(R(40, 236, 0.1 * sc, 40, PANEL, AC, 4)); o.append(T(40 + 0.05 * sc, 261, 'value 0.1 ETH to the friend', 14, bold=True))
    o.append(R(40 + 0.1 * sc, 236, 0.00042 * sc, 40, LVS, LV, 1, 1.5))
    o.append(T(680, 300, 'fee 0.00042 ETH', 13, 'end', LV, True))
    o.append(T(20, 336, '0.1 + 0.00042 = 0.10042 ETH leaves the sender; the receipt reports the fee.', 14, 'start'))
    return 350, ''.join(o)
FIG[2] = (f2, 'The same fee in three units: 21,000 gas at 20 gwei is 420,000 gwei, 4.2 × 10¹⁴ wei or 0.00042 ETH. Added to the 0.1 ETH value, the sender is debited 0.10042 ETH.',
          'Three rows converting the fee: 4.2 times ten to the 14 wei, 420,000 gwei, 0.00042 ETH; below, a bar of 0.1 ETH value with a thin 0.00042 ETH fee sliver at the end.')


# ---- 5.3 EVM stack for 60 02 60 03 01 ----
def f3():
    o = [T(20, 26, 'Bytecode, one byte per box', 14, 'start', MUT)]
    bytes_ = [('60', 'PUSH1', ACS, AC), ('02', 'data', PANEL, L2), ('60', 'PUSH1', ACS, AC), ('03', 'data', PANEL, L2), ('01', 'ADD', NXS, NX)]
    for i, (b, lab, f, s) in enumerate(bytes_):
        x = 140 + i * 90
        o.append(R(x, 38, 80, 40, f, s, 4)); o.append(TM(x + 40, 64, b, 18, bold=True))
        o.append(T(x + 40, 96, lab, 13, fill=MUT))
    steps = [('PUSH1 0x02', ['2'], 3), ('PUSH1 0x03', ['3', '2'], 6), ('ADD', ['5'], 9)]
    for i, (op, st, gas) in enumerate(steps):
        x = 60 + i * 220
        base = 290
        o.append(L(x, base, x + 140, base, INK, 2))
        for j, v in enumerate(reversed(st)):
            y = base - (j + 1) * 44
            top = j == len(st) - 1
            o.append(boxt(x + 20, y, 100, 40, [v], NXS if op == 'ADD' else (ACS if top else PANEL), NX if op == 'ADD' else (AC if top else L2), 18))
        o.append(T(x + 70, base + 22, op, 14, bold=True))
        o.append(T(x + 70, base + 42, f'gas used {gas}', 13, fill=MUT))
        if i < 2: o.append(A(x + 150, base - 40, x + 210, base - 40, L2, 2, arrow='m'))
    o.append(T(20, 362, 'ADD pops 3 and 2 and pushes 5. Gas: 3 + 3 + 3 = 9.', 14, 'start', bold=True))
    return 376, ''.join(o)
FIG[3] = (f3, 'The five bytes 60 02 60 03 01 are two PUSH1 instructions and an ADD. The stack grows to [3, 2] and ADD leaves [5]; at 3 gas each the run uses 9 gas.',
          'Five byte boxes 60 02 60 03 01 labelled PUSH1, data, PUSH1, data, ADD; below, three stacks: 2; 3 on 2; and 5, with gas used 3, 6 and 9.')


# ---- 5.4 escrow on a day line ----
def f4():
    x0, x1 = 80, 680
    fx = lambda d: x0 + d / 8 * (x1 - x0)
    o = [xaxis(x0, x1, 250, range(0, 9), fx, 'day')]
    lanes = [('contract', [(0, 3, '1 ETH held', ACS, AC), (3, 8, '0 ETH', PANEL, L2)]), ('seller', [(0, 3, '0 ETH', PANEL, L2), (3, 8, '1 ETH received', NXS, NX)]),
             ('refund', [(0, 8, 'closed: confirm came before day 7', PANEL, LN)])]
    for i, (lab, bars) in enumerate(lanes):
        y = 60 + i * 52
        o.append(T(x0 - 10, y + 24, lab, 13, 'end', MUT))
        for a, b, t, f, s in bars:
            o.append(R(fx(a), y, fx(b) - fx(a), 36, f, s, 5, 1.5, '5 4' if lab == 'refund' else None))
            o.append(T((fx(a) + fx(b)) / 2, y + 23, t, 13, bold=(f != PANEL)))
    o.append(L(fx(3), 40, fx(3), 246, AC, 2.5))
    o.append(Tb(fx(3), 36, 'day 3: buyer calls confirm (3 ≤ 7)', 13, fill=AC, bold=True))
    o.append(L(fx(7), 50, fx(7), 246, LV, 2, '6 4'))
    o.append(T(fx(7) + 6, 228, 'deadline', 13, 'start', LV))
    o.append(T(20, 322, 'Safe order inside confirm: set the stored deposit to 0 first, then send the 1 ETH,', 13, 'start'))
    o.append(T(20, 342, 'so a re-entrant call finds nothing left to pay twice.', 13, 'start'))
    return 356, ''.join(o)
FIG[4] = (f4, 'Days 0 to 8 of the escrow: the contract holds 1 ETH until the buyer confirms on day 3, the whole deposit moves to the seller and the contract drops to 0 ETH; the day-7 refund path never opens.',
          'A day axis from 0 to 8 with three lanes: the contract holding 1 ETH until day 3 then 0; the seller at 0 until day 3 then 1 ETH; the refund lane closed. A line marks the confirm on day 3 and a dashed line the day-7 deadline.')


# ---- 5.5 the balances mapping after each call ----
def f5():
    o = [T(20, 26, 'mapping(address => uint) balances, plus the contract\'s ether', 15, 'start', bold=True)]
    rows = [['start', '0', '0', '0'], ['Alice deposits 0.5', '0.5', '0', '0.5'], ['Bob deposits 0.2', '0.5', '0.2', '0.7'], ['Alice withdraws 0.1', '0.4', '0.2', '0.6']]
    marks = {(1, 1): (ACS, AC), (2, 2): (ACS, AC), (3, 1): (LVS, LV)}
    marks.update({(3, j): (NXS, NX) for j in (2, 3)})
    o.append(table(20, 40, ['call', 'Alice (ETH)', 'Bob (ETH)', 'contract total'], rows, [220, 150, 150, 160], 42, marks=marks))
    o.append(T(20, 254, 'Each call changes one entry; the total is always the sum of the entries.', 14, 'start'))
    o.append(T(20, 278, 'withdraw checks balances[Alice] ≥ 0.1, subtracts first, then sends: 0.5 − 0.1 = 0.4.', 13, 'start', MUT))
    o.append(T(20, 306, 'Final: Alice 0.4, Bob 0.2, contract 0.4 + 0.2 = 0.6 ETH', 14, 'start', NX, True))
    return 320, ''.join(o)
FIG[5] = (f5, 'The balances mapping after each call: two deposits and one withdrawal leave Alice with 0.4 ETH, Bob with 0.2 ETH and the contract holding 0.6 ETH.',
          'A table with rows start, Alice deposits 0.5, Bob deposits 0.2 and Alice withdraws 0.1, and columns Alice, Bob and contract total, ending at 0.4, 0.2 and 0.6.')


# ---- 5.6 private net: genesis to block 1 ----
def f6():
    o = []
    st = [('genesis.json', ['chainId 1337', 'gas limit 30,000,000', 'A = 100 ETH'], PANEL, AC),
          ('geth init + start', ['networkid 1337', 'create B, unlock A'], PANEL, AC),
          ('send 1 ETH', ['21,000 gas × 1 gwei', 'pending: no change yet'], LVS, LV),
          ('block 1', ['transfer committed', 'fee 0.000021 ETH'], NXS, NX)]
    for i, (t, rows, f, s) in enumerate(st):
        x = 14 + i * 178
        svg, h = block(x, 30, 160, t, rows, PANEL, s, title_fill=f)
        o.append(svg)
        if i < 3: o.append(A(x + 161, 70, x + 176, 70, L2, 2, arrow='m'))
    o.append(T(20, 160, 'Fee = 21,000 × 0.000000001 ETH = 0.000021 ETH (21,000 gwei)', 14, 'start', bold=True))
    o.append(table(20, 176, ['account', 'genesis', 'after block 1'], [['A', '100 ETH', '98.999979 ETH'], ['B', '0 ETH', '1 ETH']], [120, 160, 200], 40,
                   marks={(0, 2): (NXS, NX), (1, 2): (NXS, NX)}))
    o.append(T(520, 230, 'A: 100 − 1 − 0.000021', 13, 'start', MUT))
    o.append(T(520, 270, 'B gets the 1 ETH only;', 13, 'start', MUT)); o.append(T(520, 288, 'the fee is not B\'s', 13, 'start', MUT))
    return 300, ''.join(o)
FIG[6] = (f6, 'On the private net, A sends 1 ETH at 21,000 gas and 1 gwei, so the fee is 0.000021 ETH. Nothing changes while the transaction is pending; once block 1 commits it, A has 98.999979 ETH and B has 1 ETH.',
          'Four steps in a row: the genesis file with chain id 1337 and A at 100 ETH, init and start, sending 1 ETH while pending, and block 1 with a 0.000021 ETH fee; below, a table of A and B before and after.')


# ---- 5.7 one click, down the DApp stack ----
def f7():
    actors = ['user', 'DApp page', 'wallet', 'RPC node', 'chain']
    xs = [70, 210, 350, 490, 640]
    o = []
    for a, x in zip(actors, xs):
        o.append(boxt(x - 58, 14, 116, 34, [a], ACS if a == 'wallet' else PANEL, AC, 14, bold_first=True))
        o.append(L(x, 50, x, 330, LN, 1.5, '4 4'))
    msgs = [(0, 1, 'click Deploy', AC, False), (1, 2, 'sign this tx', AC, False), (2, 1, 'signed tx (key stays)', AC, True),
            (1, 3, 'eth_sendRawTransaction', AC, False), (3, 1, 'tx hash, at once', L2, True), (3, 4, 'mined in a block', AC, False),
            (3, 1, 'receipt: 1,500,000 gas × 20 gwei = 0.03 ETH', NX, True)]
    for i, (a, b, lab, c, back) in enumerate(msgs):
        y = 76 + i * 38
        x1, x2 = xs[a], xs[b]
        d = 4 if x2 > x1 else -4
        o.append(A(x1 + d, y, x2 - d, y, c, 2, '6 4' if back else None, {AC: 'n', L2: 'm', NX: 'x'}[c]))
        o.append(Tb((x1 + x2) / 2, y - 7, lab, 13, fill=c if c != L2 else MUT, bold=c == NX))
    o.append(T(20, 362, 'Deployer: 5 − 0.03 = 4.97 ETH. A read with eth_call costs nothing and needs no signature.', 14, 'start', bold=True))
    return 376, ''.join(o)
FIG[7] = (f7, 'One deploy click: the page builds the transaction, the wallet signs it without the key leaving, the node returns only a transaction hash, and the receipt later shows 1,500,000 gas × 20 gwei = 0.03 ETH, leaving 4.97 ETH.',
          'A sequence across user, DApp page, wallet, RPC node and chain: click, sign request, signed transaction, send raw transaction, transaction hash returned, mined, and a receipt showing a 0.03 ETH fee.')


# ---- 5.8 GHOST weights ----
def f8():
    pos = {'A': (300, 50), 'B': (200, 140), 'U1': (420, 140), 'C': (130, 230), 'U2': (280, 230), 'D': (130, 320)}
    w = {'A': 6, 'B': 4, 'U1': 1, 'C': 2, 'U2': 1, 'D': 1}
    main = {'A', 'B', 'C', 'D'}
    o = []
    for p, c in (('A', 'B'), ('A', 'U1'), ('B', 'C'), ('B', 'U2'), ('C', 'D')):
        on = c in main
        o.append(L(*pos[p], *pos[c], AC if on else L2, 3 if on else 1.8, None if on else '6 4'))
    for k, (x, y) in pos.items():
        on = k in main
        o.append(node(x, y, k, 26, ACS if on else PANEL, AC if on else L2, 15))
        o.append(Tb(x + 34, y + 5, f'w = {w[k]}', 13, 'start', AC if on else MUT, on))
    X = 480
    o.append(T(X, 200, 'weight = 1 + weights of children', 14, 'start', bold=True))
    lines = ['D = 1,  C = 1 + 1 = 2,  U2 = 1', 'B = 1 + 2 + 1 = 4,  U1 = 1', 'A = 1 + 4 + 1 = 6', 'at A: B (4) beats U1 (1)', 'at B: C (2) beats U2 (1)']
    for i, t in enumerate(lines):
        o.append(T(X, 226 + i * 22, t, 13, 'start', INK if i < 3 else AC, i >= 3))
    o.append(T(X, 50, 'main chain A-B-C-D', 15, 'start', AC, True))
    o.append(T(X, 72, 'U1 and U2 are uncles:', 13, 'start', MUT)); o.append(T(X, 90, 'off the chain, but their', 13, 'start', MUT))
    o.append(T(X, 108, 'weight still counts', 13, 'start', MUT))
    return 354, ''.join(o)
FIG[8] = (f8, 'Weights counted bottom-up: D = 1, C = 2, B = 4, A = 6. At A the heavier child is B (4 against U1\'s 1), at B it is C (2 against U2\'s 1), so the main chain is A-B-C-D with U1 and U2 as uncles.',
          'A block tree: A with children B and U1, B with children C and U2, C with child D. The main chain A, B, C, D is solid with weights 6, 4, 2, 1; the uncles U1 and U2 are dashed with weight 1.')


spec = make_spec(FIG)


def text_fixes(k):
    return {
        8: [('Only a few universities teach this chapter; the ideas appear in DeFi governance, Ethereum\'s uncle blocks and scaling side chains.',
             'The ideas appear in DeFi governance, Ethereum\'s uncle blocks and scaling side chains.')],
    }.get(k, [])
