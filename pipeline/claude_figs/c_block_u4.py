"""Claude's hand-drawn figures for c-block-u4 (Blockchain Technology, unit 4: Bitcoin and cryptocurrencies), one per
chapter, each drawn from that chapter's worked example with its own numbers."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blockkit import *

FIG = {}
AFTER = {1: 1}


# ---- 4.1 what the wallet holds, and what it is worth ----
def f1():
    o = []
    o.append(R(20, 20, 200, 300, PANEL, AC, 22))
    o.append(R(90, 32, 60, 6, LN, LN, 3, 0))
    o.append(T(120, 70, 'phone wallet', 14, bold=True))
    o.append(T(120, 90, 'shows 0.05 BTC', 13, fill=MUT))
    o.append(boxt(40, 110, 160, 46, ['private keys'], LVS, LV, 14))
    o.append(boxt(40, 168, 160, 46, ['addresses'], ACS, AC, 14))
    o.append(T(120, 248, 'no coins inside', 14, fill=LV, bold=True))
    o.append(T(120, 268, 'lose the keys,', 13, fill=MUT)); o.append(T(120, 286, 'lose the coins', 13, fill=MUT))
    o.append(R(300, 20, 400, 200, PANEL, L2, 10))
    o.append(T(500, 46, 'the blockchain (every full node)', 14, bold=True))
    o.append(boxt(320, 62, 360, 60, ['unspent outputs locked to', 'those addresses: total 0.05 BTC'], NXS, NX, 14))
    o.append(T(500, 148, '1 BTC = 10,00,00,000 satoshi', 13, fill=MUT))
    o.append(T(500, 170, '0.05 BTC = 50,00,000 satoshi', 14, bold=True))
    o.append(T(500, 196, 'the balance is a sum the wallet reads', 13, fill=MUT))
    o.append(A(200, 133, 318, 98, LV, 2, '6 4', 'l'))
    o.append(Tb(258, 104, 'can spend', 13, fill=LV, bold=True))
    o.append(A(500, 222, 500, 250, AC))
    o.append(boxt(300, 254, 400, 66, ['value = 0.05 × ₹40,00,000 = ₹2,00,000', 'a price times a holding, not a stored number'], ACS, AC, 14, bold_first=True))
    return 336, ''.join(o)
FIG[1] = (f1, 'The wallet holds keys and addresses; the 0.05 BTC sits on the blockchain as unspent outputs those keys can spend. At ₹40,00,000 per bitcoin it is worth ₹2,00,000.',
          'A phone wallet containing private keys and addresses, linked to a blockchain panel holding unspent outputs worth 0.05 BTC, that is 50,00,000 satoshi, and the value calculation 0.05 times 40,00,000 rupees equals 2,00,000 rupees.')


# ---- 4.2 one input, two outputs, fee as the gap ----
def f2():
    sc = 600
    o = [T(20, 28, 'Inputs', 14, 'start', MUT)]
    o.append(R(80, 40, 1.0 * sc, 44, ACS, AC, 4))
    o.append(T(80 + sc / 2, 67, 'Alice\'s UTXO 1.0 BTC = 100,000,000 sat', 14, bold=True))
    o.append(T(20, 128, 'Outputs', 14, 'start', MUT))
    o.append(R(80, 140, 0.3 * sc, 44, PANEL, AC, 4))
    o.append(T(80 + 0.15 * sc, 160, 'to Bob', 13, bold=True)); o.append(T(80 + 0.15 * sc, 177, '0.3 BTC', 13))
    o.append(R(80 + 0.3 * sc, 140, 0.6999 * sc - 2, 44, NXS, NX, 4))
    o.append(T(80 + 0.65 * sc, 160, 'change back to Alice', 13, bold=True)); o.append(T(80 + 0.65 * sc, 177, '0.6999 BTC = 69,990,000 sat', 13))
    o.append(L(80 + sc, 34, 80 + sc, 196, LV, 1.5, '4 3'))
    # zoom on the gap
    o.append(R(560, 214, 140, 82, PANEL, LV, 8, 1.5))
    o.append(L(678, 190, 640, 214, LV, 1.2, '3 3'))
    o.append(R(574, 232, 56, 30, NXS, NX, 2, 1.5)); o.append(R(630, 232, 6, 30, 'none', LV, 0, 1.5, '3 2'))
    o.append(T(630, 284, 'gap 0.0001 BTC', 13, fill=LV, bold=True))
    o.append(T(20, 236, 'fee = inputs − outputs', 15, 'start', bold=True))
    o.append(T(20, 262, '1.0 − (0.3 + 0.6999) = 0.0001 BTC = 10,000 sat', 14, 'start'))
    o.append(T(20, 288, 'The fee is not written as an output: the miner claims the gap.', 13, 'start', MUT))
    return 310, ''.join(o)
FIG[2] = (f2, 'The 1.0 BTC input is spent whole: 0.3 BTC to Bob and 0.6999 BTC change back to Alice. The missing 0.0001 BTC is not an output; it is the gap the miner claims as the fee.',
          'A 1.0 BTC input bar above an output bar split into 0.3 BTC to Bob and 0.6999 BTC change, with a zoomed box showing the tiny 0.0001 BTC gap labelled as the fee.')


# ---- 4.3 the P2PKH stack, step by step ----
def f3():
    states = [('scriptSig', ['sig', 'pub']), ('OP_DUP', ['sig', 'pub', 'pub']), ('OP_HASH160', ['sig', 'pub', 'Hpk']),
              ('push h', ['sig', 'pub', 'Hpk', 'h']), ('OP_EQUALVERIFY', ['sig', 'pub']), ('OP_CHECKSIG', ['TRUE'])]
    o = [T(20, 26, 'Stack after each step (bottom to top), P2PKH spend', 15, 'start', bold=True)]
    cw, base = 112, 250
    for i, (op, st) in enumerate(states):
        x = 20 + i * (cw + 4)
        for j, item in enumerate(st):
            y = base - (j + 1) * 38
            f, s = PANEL, L2
            if item == 'TRUE': f, s = NXS, NX
            elif i == 3 and j == 3: f, s = ACS, AC
            elif item == 'Hpk': f, s = ACS, AC
            o.append(boxt(x + 8, y, cw - 16, 34, [item], f, s, 14))
        o.append(L(x + 2, base + 2, x + cw - 2, base + 2, INK, 2))
        o.append(T(x + cw / 2, base + 22, op, 13, bold=True))
        o.append(T(x + cw / 2, base + 40, f'depth {len(st)}', 13, fill=LV if len(st) == 4 else MUT, bold=len(st) == 4))
    o.append(T(20 + 3 * (cw + 4) + cw / 2, 60, 'peak: 4 items', 13, fill=AC, bold=True))
    o.append(T(20, 316, 'Hpk = HASH160(pub) equals h, so EQUALVERIFY passes; CHECKSIG verifies sig and leaves a single TRUE.', 13, 'start', MUT))
    o.append(T(20, 344, 'Value: 0.25 BTC in − 0.00012 BTC fee = 0.24988 BTC to the new output', 14, 'start', bold=True))
    return 358, ''.join(o)
FIG[3] = (f3, 'The stack after each opcode of the worked example: it peaks at 4 items when h is pushed and ends with a single TRUE, so the spend is valid; the 0.25 BTC input less the 0.00012 BTC fee leaves 0.24988 BTC.',
          'Six small stacks side by side: sig pub; sig pub pub; sig pub Hpk; sig pub Hpk h, the peak of four; sig pub; and TRUE, each labelled with its opcode and depth.')


# ---- 4.4 the halving staircase and the block reward ----
def f4():
    x0, x1, y0, y1 = 70, 460, 50, 300
    fx = lambda h: x0 + h / 1050000 * (x1 - x0)
    fy = lambda b: y1 - b / 50 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [0, 210000, 420000, 630000, 840000], [0, 12.5, 25, 37.5, 50], fx, fy, 'block height', '',
              lambda v: f'{v // 1000}k', lambda v: f'{v:g}')]
    pts = []
    for n in range(5):
        b = 50 / 2 ** n
        pts += [(fx(n * 210000), fy(b)), (fx((n + 1) * 210000), fy(b))]
    o.append(P(pts, AC, 3))
    o.append(T(20, 24, 'subsidy (BTC) by block height', 14, 'start', MUT))
    for n, lab in enumerate(('50', '25', '12.5', '6.25', '3.125')):
        o.append(T(fx(n * 210000 + 105000), fy(50 / 2 ** n) - 8, lab, 13, fill=AC if n < 4 else LV, bold=n == 4))
    o.append(C(fx(840000), fy(3.125), 6, LV))
    X = 490
    o.append(T(X, 60, 'Height 840,000', 15, 'start', bold=True))
    o.append(T(X, 84, 'halvings n = 840,000 ÷ 210,000 = 4', 13, 'start'))
    o.append(boxt(X, 100, 210, 40, ['subsidy 50 ÷ 2⁴ = 3.125'], LVS, LV, 14))
    o.append(T(X + 105, 162, '+', 18, bold=True))
    o.append(boxt(X, 172, 210, 40, ['fees 0.4'], PANEL, L2, 14))
    o.append(T(X + 105, 234, '=', 18, bold=True))
    o.append(boxt(X, 244, 210, 40, ['reward 3.525 BTC'], ACS, AC, 15, bold_first=True))
    o.append(T(X + 105, 308, '× ₹60,00,000 = ₹2,11,50,000', 13, bold=True))
    return 350, ''.join(o)
FIG[4] = (f4, 'The subsidy halves every 210,000 blocks: 50, 25, 12.5, 6.25, then 3.125 BTC from height 840,000. Adding the block\'s 0.4 BTC of fees gives 3.525 BTC, worth ₹2,11,50,000.',
          'A staircase of the block subsidy against height, stepping from 50 down to 3.125 BTC at 840,000, and beside it the sum 3.125 plus 0.4 fees equals 3.525 BTC, times 60,00,000 rupees.')


# ---- 4.5 confirmations on a time line ----
def f5():
    o = [T(20, 26, 'Payment of 0.0102 BTC = ₹50,000 item + ₹1,000 fee', 15, 'start', bold=True)]
    o.append(boxt(20, 46, 120, 52, ['mempool', '0 conf'], LVS, LV, 13, bold_first=True))
    bw, gap = 76, 12
    for i in range(6):
        x = 160 + i * (bw + gap)
        name = 'h' if i == 0 else f'h+{i}'
        f, s = (ACS, AC) if i == 0 else (PANEL, L2)
        if i == 5: f, s = NXS, NX
        o.append(boxt(x, 46, bw, 52, [f'block {name}', f'{i + 1} conf'], f, s, 13, bold_first=True))
        o.append(A(x + bw + 1, 72, x + bw + gap - 1, 72, L2, 1.5, arrow='m')) if i < 5 else None
        o.append(T(x + bw / 2, 122, f'≈ {(i + 1) * 10} min', 13, fill=MUT))
    o.append(A(140, 72, 158, 72, AC))
    o.append(T(160 + bw / 2, 150, 'merchant ships', 13, fill=AC, bold=True))
    o.append(T(160 + 5 * (bw + gap) + bw / 2, 150, 'six deep', 13, fill=NX, bold=True))
    o.append(T(20, 194, 'The block that includes the payment is the first confirmation; each block on top adds one.', 13, 'start', MUT))
    o.append(T(20, 216, 'Mean wait: 1 × 10 = 10 min for 1 confirmation, 6 × 10 = 60 min for 6.', 14, 'start', bold=True))
    o.append(R(20, 236, 680, 70, PANEL, LN, 10, 1.5))
    o.append(T(36, 262, 'To reverse a payment with 6 confirmations an attacker must secretly mine 6 blocks', 13, 'start'))
    o.append(T(36, 284, 'and then overtake the honest chain: far harder than winning one race at 0 or 1 confirmation.', 13, 'start'))
    return 320, ''.join(o)
FIG[5] = (f5, 'The payment waits in the mempool, gets its first confirmation in block h after about 10 minutes, when the merchant ships, and its sixth in block h+5 after about 60 minutes.',
          'A mempool box followed by six blocks h to h+5 labelled 1 to 6 confirmations at about 10 to 60 minutes; the merchant ships at the first and the sixth is marked six deep.')


# ---- 4.6 choosing UTXOs for a 0.6 BTC payment ----
def f6():
    o = [T(20, 26, 'Need 0.6 + 0.0005 fee = 0.6005 BTC from UTXOs 0.4, 0.3, 0.2', 15, 'start', bold=True)]
    rows = [('0.4 + 0.3 = 0.7', 'change 0.7 − 0.6005 = 0.0995', True), ('0.4 + 0.2 = 0.6', 'change 0.6 − 0.6005 = −0.0005', False),
            ('0.3 + 0.2 = 0.5', 'below 0.6, fails at once', False)]
    for i, (a, b, ok) in enumerate(rows):
        y = 44 + i * 46
        o.append(R(20, y, 440, 38, NXS if ok else PANEL, NX if ok else L2, 6, 1.5))
        o.append(T(36, y + 25, a, 14, 'start', bold=True)); o.append(T(170, y + 25, b, 13, 'start', NX if ok else LV))
        o.append(tick(440, y + 19, 7) if ok else cross(440, y + 19, 6))
    y = 200
    o.append(boxt(20, y, 110, 40, ['UTXO 0.4'], ACS, AC, 14)); o.append(boxt(20, y + 56, 110, 40, ['UTXO 0.3'], ACS, AC, 14))
    o.append(boxt(20, y + 112, 110, 40, ['UTXO 0.2'], PANEL, LN, 14))
    o.append(T(140, y + 137, 'kept for later', 13, 'start', MUT))
    o.append(R(200, y + 20, 160, 72, PANEL, AC, 10))
    o.append(T(280, y + 50, 'transaction', 14, bold=True)); o.append(T(280, y + 70, 'inputs 0.7 BTC', 13, fill=MUT))
    o.append(A(130, y + 20, 198, y + 46, AC)); o.append(A(130, y + 76, 198, y + 66, AC))
    outs = [('merchant 0.6', PANEL, AC), ('change 0.0995', NXS, NX), ('fee 0.0005', LVS, LV)]
    for i, (t, f, s) in enumerate(outs):
        yy = y - 4 + i * 50
        o.append(boxt(440, yy, 170, 40, [t], f, s, 14))
        o.append(A(360, y + 56, 438, yy + 20, s, 2, '6 4' if i == 2 else None, {AC: 'n', NX: 'x', LV: 'l'}[s]))
    o.append(T(620, y + 71, 'fresh change', 13, 'start', NX)); o.append(T(620, y + 89, 'address', 13, 'start', NX))
    o.append(T(440, y + 160, '0.4 + 0.3 = 0.6 + 0.0995 + 0.0005', 14, 'start', bold=True))
    return 372, ''.join(o)
FIG[6] = (f6, 'Only the pair 0.4 + 0.3 = 0.7 BTC covers 0.6 BTC plus the 0.0005 BTC fee. The transaction pays 0.6 BTC to the merchant, leaves 0.0005 BTC as fee and returns 0.0995 BTC to a fresh change address.',
          'Three candidate pairs: 0.4 plus 0.3 ticked with change 0.0995, 0.4 plus 0.2 crossed at minus 0.0005, 0.3 plus 0.2 crossed. Below, UTXOs 0.4 and 0.3 feed a transaction that pays 0.6 to the merchant, 0.0995 change and a 0.0005 fee.')


# ---- 4.7 Zcash: what the ledger shows ----
def f7():
    o = [T(20, 26, 'The same 1.5 ZEC payment, as the public ledger records it', 15, 'start', bold=True)]
    for i, (title, cells, f, s) in enumerate((('transparent: t-addr to t-addr', [('sender', 't1Ab…'), ('receiver', 't1Xy…'), ('amount', '1.5 ZEC')], PANEL, AC),
                                              ('shielded: z-addr to z-addr', [('sender', None), ('receiver', None), ('amount', None)], PANEL, NX))):
        y = 48 + i * 132
        o.append(R(20, y, 680, 112, f, s, 10))
        o.append(T(36, y + 26, title, 14, 'start', bold=True))
        for j, (lab, val) in enumerate(cells):
            x = 36 + j * 150
            o.append(T(x, y + 52, lab, 13, 'start', MUT))
            if val:
                o.append(boxt(x, y + 60, 136, 36, [val], LVS, LV, 14))
            else:
                o.append(R(x, y + 60, 136, 36, 'var(--ink)', INK, 6, 1))
                o.append(T(x + 68, y + 83, 'hidden', 13, fill='var(--fig)', bold=True))
        if val:
            o.append(T(500, y + 84, 'all three public', 14, 'start', LV, True))
        else:
            o.append(boxt(490, y + 60, 194, 36, ['valid proof + pool change'], NXS, NX, 13))
    o.append(T(20, 330, '1.5 ZEC × ₹4,000 = ₹6,000 moves in both cases; the rupee figure is your own conversion, not ledger data.', 13, 'start', MUT))
    return 344, ''.join(o)
FIG[7] = (f7, 'The same 1.5 ZEC (₹6,000 at ₹4,000 per ZEC) through the two address types: the transparent record shows sender, receiver and amount; the shielded record shows only a valid proof and a change in the shielded pool.',
          'Two ledger rows. Transparent: sender, receiver and 1.5 ZEC all shown. Shielded: the three fields are blacked out as hidden and only a valid proof and pool change are shown.')


# ---- 4.8 the common-input heuristic ----
def f8():
    o = []
    o.append(R(150, 60, 270, 210, 'none', LV, 30, 2, '7 5'))
    o.append(T(285, 292, 'one cluster: likely one owner', 13, fill=LV, bold=True))
    o.append(boxt(20, 80, 110, 58, ['Exchange', 'KYC: a name'], ACS, AC, 13, bold_first=True))
    o.append(node(200, 110, 'A1', 26, PANEL, AC)); o.append(node(200, 220, 'A2', 26, PANEL, AC))
    o.append(A(130, 110, 172, 110, AC)); o.append(Tb(151, 100, '0.8', 13, fill=AC))
    o.append(R(320, 135, 80, 60, LVS, LV, 8)); o.append(T(360, 162, 'tx D', 14, bold=True)); o.append(T(360, 180, 'spends both', 13, fill=MUT))
    o.append(A(226, 118, 318, 152, AC)); o.append(Tb(276, 128, '0.8', 13, fill=AC))
    o.append(A(226, 212, 318, 180, LV)); o.append(Tb(276, 212, '0.3', 13, fill=LV))
    o.append(node(560, 165, 'E', 26, PANEL, L2))
    o.append(A(400, 165, 532, 165, AC)); o.append(Tb(466, 155, '1.09', 13, fill=AC))
    o.append(T(466, 190, 'fee 0.01', 13, fill=MUT))
    o.append(T(20, 34, 'inputs 0.8 + 0.3 = 1.1 BTC = output 1.09 + fee 0.01', 14, 'start', bold=True))
    o.append(T(20, 320, 'The exchange already knows who owns A1; the co-spend lets it attach the same name to A2,', 13, 'start'))
    o.append(T(20, 340, 'and it can see that 1.09 BTC went to E.', 13, 'start'))
    return 354, ''.join(o)
FIG[8] = (f8, 'A1 came from a KYC exchange; one transaction spends A1 and A2 together, so the common-input heuristic puts both in one cluster and the exchange\'s name for A1 now covers A2. Inputs 1.1 BTC = 1.09 BTC to E + 0.01 BTC fee.',
          'A KYC exchange pays 0.8 BTC to A1; A1 and A2 with 0.3 BTC both feed transaction D, which pays 1.09 BTC to E with a 0.01 fee. A dashed outline groups A1 and A2 as one likely owner.')


# ---- 4.9 why the base layer settles about 6.7 tx per second ----
def f9():
    o = [T(20, 26, 'One block: 1,000,000 bytes ÷ 250 bytes = 4,000 transactions', 15, 'start', bold=True)]
    o.append(T(20, 50, '4,000 transactions every 600 s = 6.67 ≈ 6.7 per second', 14, 'start'))
    o.append(T(20, 86, '100,000 payments ÷ 4,000 per block = 25 blocks', 14, 'start', bold=True))
    bw = 22
    for i in range(25):
        x = 20 + i * (bw + 1.2)
        o.append(R(x, 100, bw, 34, ACS, AC, 3, 1.2))
    for i in range(0, 26, 5):
        x = 20 + i * (bw + 1.2)
        o.append(L(x, 138, x, 146, L2, 1.5)); o.append(T(x, 162, f'{i * 10}', 13, fill=MUT))
    o.append(T(612, 116, '250 min', 14, 'start', bold=True)); o.append(T(612, 136, '≈ 4 h 10 min', 13, 'start', MUT)); o.append(T(642, 162, 'minutes', 13, 'start', MUT))
    o.append(R(20, 186, 680, 112, PANEL, LV, 10, 1.5))
    o.append(T(36, 212, 'The trade-off', 14, 'start', LV, True))
    o.append(T(36, 236, 'Bigger or faster blocks raise the 6.7, but every full node must store every block.', 13, 'start'))
    o.append(T(36, 258, 'Higher disk and bandwidth costs mean fewer independent full nodes,', 13, 'start'))
    o.append(T(36, 280, 'and fewer nodes make the network easier to influence.', 13, 'start'))
    return 312, ''.join(o)
FIG[9] = (f9, 'A 1 MB block of 250-byte transactions holds 4,000, and one block every 600 s gives about 6.7 transactions per second, so 100,000 payments need 25 blocks, about 4 h 10 min. Raising that number costs every full node more disk and bandwidth.',
          'A row of 25 blocks on a time scale from 0 to 250 minutes for 100,000 payments, with the arithmetic 4,000 transactions per block and 6.7 per second, and a box explaining that bigger blocks cost every full node more.')


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d


def text_fixes(k):
    return {
        4: [('This chapter does the revenue-minus-cost arithmetic that decides whether a rig switches on. Only a few universities teach it at this depth.',
             'This chapter does the revenue-minus-cost arithmetic that decides whether a rig switches on.')],
        5: [('Each extra block on top of the payment block is a confirmation.',
             'The block that includes the payment is its first confirmation, and each block built on top adds one more.'),
            ('A <b>confirmation</b> is one block on top of the block that contains your transaction. If a transaction is in block height h, then after blocks h+1, h+2, ... h+k exist on the same chain, it has k confirmations.',
             'A transaction gets its first <b>confirmation</b> when a block includes it, and one more for every block built on top of that block. If a transaction is in block height h, then once blocks h+1, ... h+k−1 exist on the same chain, it has k confirmations.'),
            ('A block on top of the block that contains the transaction. k confirmations means k such later blocks on the same chain.',
             'The block that includes the transaction is its first confirmation, and each block built on top adds one, so k confirmations means the including block plus k − 1 later blocks on the same chain.')],
        7: [('Only a few syllabi list Primecoin, so learn its one-line idea and spend your time on Namecoin and Zcash.',
             'For Primecoin, learn its one-line idea; spend your time on Namecoin and Zcash.')],
    }.get(k, [])
