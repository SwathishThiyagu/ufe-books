"""Claude's hand-drawn figures for c-block-u6 (Blockchain Technology, unit 6: Hyperledger, applications and emerging
trends), one per chapter, each drawn from that chapter's worked example with its own numbers."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blockkit import *

FIG = {}


# ---- 6.1 endorsement policy: 1 of Org A AND 1 of Org B ----
def f1():
    o = []
    o.append(boxt(20, 150, 100, 50, ['client', 'proposal'], PANEL, AC, 13, bold_first=True))
    orgs = [('Org A', 30, [('A1', True), ('A2', True)]), ('Org B', 210, [('B1', True), ('B2', False)])]
    for name, y, peers in orgs:
        o.append(R(170, y, 220, 130, PANEL, L2, 12))
        o.append(T(184, y + 22, name, 14, 'start', bold=True))
        for i, (p, e) in enumerate(peers):
            x = 230 + i * 100
            o.append(node(x, y + 72, p, 26, NXS if e else PANEL, NX if e else L2, 14))
            o.append(T(x, y + 116, 'endorses' if e else 'not asked', 13, fill=NX if e else MUT))
            if e: o.append(A(122, 175, x - 28, y + 72, AC, 1.6))
    o.append(R(430, 70, 270, 120, PANEL, AC, 10))
    o.append(T(565, 96, 'policy: 1 of Org A AND 1 of Org B', 13, bold=True))
    o.append(T(450, 124, 'Org A: A1, A2 → 2 ≥ 1', 13, 'start')); o.append(tick(670, 119, 6))
    o.append(T(450, 150, 'Org B: B1 → 1 ≥ 1', 13, 'start')); o.append(tick(670, 145, 6))
    o.append(T(450, 176, '2 distinct organisations: met', 13, 'start', NX, True))
    o.append(A(392, 160, 428, 140, AC))
    steps = [('orderer', 'orders', PANEL, AC), ('committer', 'checks', PANEL, AC), ('ledger', 'written', NXS, NX)]
    for i, (a, b, f, s) in enumerate(steps):
        x = 430 + i * 92
        o.append(boxt(x, 234, 86, 58, [a, b], f, s, 13, bold_first=True))
        if i: o.append(A(x - 6, 263, x - 1, 263, AC, 2))
    o.append(A(565, 192, 565, 230, AC))
    o.append(T(20, 372, 'An extra endorsement from Org A (A2) is allowed: the policy sets a minimum, not a maximum.', 13, 'start', MUT))
    return 386, ''.join(o)
FIG[1] = (f1, 'A1, A2 and B1 endorse. The rule needs at least one peer from Org A and one from Org B; both organisations are present, so the policy is met and the extra A2 signature does no harm. The orderer only orders; the committer checks.',
          'Org A with peers A1 and A2 and Org B with B1 and B2; the client sends proposals to A1, A2 and B1, which endorse. A policy box shows Org A 2 at least 1 and Org B 1 at least 1, met, then orderer, committer and ledger.')


# ---- 6.2 TransferAsset with two and with one endorsement ----
def f2():
    o = [T(20, 26, 'TransferAsset(CAR1, Ravi) under AND(Org A, Org B): r = 2 endorsements needed', 14, 'start', bold=True)]
    o.append(boxt(20, 44, 160, 66, ['CAR1', 'owner Asha', '₹5,00,000'], PANEL, AC, 13, bold_first=True))
    for i, (title, e, ok) in enumerate((('Org A and Org B endorse', 2, True), ('only Org A endorses', 1, False))):
        y = 140 + i * 110
        o.append(T(20, y + 4, title, 14, 'start', bold=True))
        o.append(boxt(20, y + 16, 120, 56, ['simulate', f'e = {e}'], PANEL, AC, 13))
        o.append(A(142, y + 44, 178, y + 44, AC))
        o.append(boxt(180, y + 16, 140, 56, [f'e = {e} {"≥" if ok else "<"} r = 2', 'pass' if ok else 'fail'], NXS if ok else LVS, NX if ok else LV, 13))
        o.append(A(322, y + 44, 358, y + 44, NX if ok else LV, 2, arrow='x' if ok else 'l'))
        if ok:
            o.append(boxt(360, y + 16, 150, 56, ['ordered, validated', 'committed'], PANEL, AC, 13))
            o.append(A(512, y + 44, 548, y + 44, AC))
            o.append(boxt(550, y + 16, 150, 56, ['owner = Ravi', 'QueryAsset → Ravi'], NXS, NX, 13, bold_first=True))
        else:
            o.append(boxt(360, y + 16, 150, 56, ['marked invalid', 'at commit'], LVS, LV, 13))
            o.append(A(512, y + 44, 548, y + 44, LV, 2, arrow='l'))
            o.append(boxt(550, y + 16, 150, 56, ['owner stays Asha'], PANEL, L2, 13, bold_first=True))
    return 340, ''.join(o)
FIG[2] = (f2, 'With both organisations endorsing, e = 2 meets r = 2, the transfer commits and CAR1 belongs to Ravi. With only Org A, e = 1 < 2, the commit check marks it invalid and the owner stays Asha.',
          'An asset card CAR1, owner Asha. Two rows: both organisations endorse, e equals 2, pass, committed, owner Ravi; only Org A endorses, e equals 1, fail, marked invalid, owner stays Asha.')


# ---- 6.3 one claim, then the same bill again ----
def f3():
    sc = 640 / 500000
    o = [T(20, 26, 'Sum insured ₹5,00,000, deductible ₹10,000 per claim', 15, 'start', bold=True)]
    o.append(R(40, 44, 500000 * sc, 40, PANEL, L2, 4))
    o.append(R(40, 44, 110000 * sc, 40, NXS, NX, 4))
    o.append(T(40 + 55000 * sc, 69, '₹1,10,000 paid', 13, bold=True))
    o.append(T(40 + 310000 * sc, 69, '₹3,90,000 left', 13, fill=MUT, bold=True))
    o.append(T(20, 124, 'Claim 1: bill ₹1,20,000, document hash H', 14, 'start', bold=True))
    chk = [('policy active', True), ('₹1,20,000 ≤ ₹5,00,000 cap', True), ('H not in paid-claims log', True)]
    for i, (t, ok) in enumerate(chk):
        x = 20 + i * 230
        o.append(R(x, 138, 220, 34, NXS, NX, 6, 1.5)); o.append(T(x + 12, 160, t, 13, 'start')); o.append(tick(x + 204, 155, 6))
    o.append(T(20, 202, 'payout = 1,20,000 − 10,000 = ₹1,10,000;  left = 5,00,000 − 1,10,000 = ₹3,90,000;  store H', 14, 'start', bold=True))
    o.append(T(20, 246, 'Claim 2: the identical bill, same hash H', 14, 'start', bold=True))
    o.append(R(20, 260, 220, 34, LVS, LV, 6, 1.5)); o.append(T(32, 282, 'H already in the log', 13, 'start')); o.append(cross(224, 277, 6))
    o.append(A(242, 277, 290, 277, LV, 2, arrow='l'))
    o.append(boxt(292, 260, 200, 34, ['rejected: pays ₹0'], LVS, LV, 14))
    o.append(T(20, 330, 'The ledger catches the copy; whether the first bill is genuine still needs a person to check.', 13, 'start', MUT))
    return 344, ''.join(o)
FIG[3] = (f3, 'The first claim passes all three checks and pays ₹1,20,000 − ₹10,000 = ₹1,10,000, leaving ₹3,90,000 of cover. The same bill sent again carries the same hash H, which is already logged, so it pays ₹0.',
          'A bar of the 5,00,000 rupee cover with 1,10,000 paid and 3,90,000 left; three ticked checks for claim one; for the repeated bill, a crossed hash check and a rejection paying nothing.')


# ---- 6.4 batch B001 through four handovers ----
def f4():
    st = [('Farm', 100), ('Transporter', 98), ('Warehouse', 98), ('Retailer', 95)]
    o = [T(20, 26, 'Batch B001, mangoes: each event stores the hash of the one before', 14, 'start', bold=True)]
    base = 250
    for i, (n, q) in enumerate(st):
        x = 30 + i * 175
        h = q * 1.6
        o.append(R(x, base - h, 120, h, ACS, AC, 4))
        o.append(T(x + 60, base - h + 26, f'{q} kg', 16, bold=True))
        o.append(T(x + 60, base + 22, n, 14, bold=True))
        o.append(T(x + 60, base + 42, f'q{i} = {q}', 13, fill=MUT))
        if i:
            loss = st[i - 1][1] - q
            xm = x - 28
            o.append(A(x - 52, 60, x - 4, 60, L2, 1.8, arrow='m'))
            o.append(T(xm, 50, 'prev hash', 13, fill=MUT))
            col = LV if loss else NX
            o.append(R(xm - 26, 92, 52, 30, LVS if loss else NXS, col, 15, 1.5))
            o.append(T(xm, 112, f'−{loss}', 14, fill=col, bold=True))
    o.append(T(20, 324, 'Losses 2 + 0 + 3 = 5 kg = 100 − 95, that is 5 ÷ 100 = 5.0% of the dispatch.', 14, 'start', bold=True))
    o.append(T(20, 348, 'Audit leg 1 (farm → transporter) and leg 3 (warehouse → retailer); leg 2 matches.', 13, 'start', MUT))
    return 362, ''.join(o)
FIG[4] = (f4, 'The four custody events of batch B001 record 100, 98, 98 and 95 kg, so the legs lose 2, 0 and 3 kg: 5 kg in all, 5.0% of what the farm dispatched. The two legs with a loss are the ones to audit.',
          'Four bars for farm 100 kg, transporter 98, warehouse 98 and retailer 95, linked by previous-hash arrows, with loss badges minus 2, minus 0 and minus 3 between them.')


# ---- 6.5 144 readings, one root, an 8-hash proof ----
def f5():
    o = [T(20, 26, 'One vaccine fridge, one day: a reading every 10 min = 6 × 24 = 144', 14, 'start', bold=True)]
    hot = {50, 51, 52}
    for i in range(144):
        r, c = divmod(i, 72)
        x, y = 20 + c * 9.5, 40 + r * 22
        o.append(R(x, y, 8, 18, LV if i in hot else ACS, LV if i in hot else AC, 1, 0.8))
    o.append(T(20, 106, '3 readings above 8 °C: 3 ÷ 144 = 2.08%', 13, 'start', LV, True))
    # proof path: 8 levels
    X0, Y0 = 60, 130
    o.append(T(20, 140, 'Merkle tree over 144 leaves: 2⁷ = 128 < 144 ≤ 256 = 2⁸, so 8 levels', 13, 'start', MUT))
    for lv in range(9):
        y = 330 - lv * 21
        x = X0 + lv * 18
        o.append(C(x, y, 6, LV if lv == 0 else (NX if lv == 8 else AC)))
        if lv < 8:
            o.append(L(x, y, x + 18, y - 21, AC, 2))
            o.append(R(x + 30, y - 8, 16, 16, PANEL, L2, 3, 1.5))
    o.append(T(X0 - 8, 354, 'one reading', 13, 'start', LV))
    o.append(T(X0 + 8 * 18 + 12, 167, 'root', 13, 'start', NX, True))
    o.append(T(250, 250, '8 sibling hashes', 14, 'start', bold=True))
    o.append(T(250, 270, '(the grey squares) prove one reading', 13, 'start', MUT))
    o.append(boxt(480, 160, 220, 52, ['blockchain', '1 root, 32 bytes'], NXS, NX, 13, bold_first=True))
    o.append(boxt(480, 280, 220, 52, ['hospital database', '144 raw readings'], PANEL, L2, 13, bold_first=True))
    o.append(A(X0 + 8 * 18 + 50, 176, 476, 186, NX, 2, arrow='x'))
    return 366, ''.join(o)
FIG[5] = (f5, 'All 144 readings stay in the hospital database; only one 32-byte Merkle root goes on the ledger. Because 144 needs 8 tree levels, one reading is proved with 8 sibling hashes. Three readings above 8 °C are 2.08% of the day.',
          'A strip of 144 reading cells with three highlighted above 8 degrees; a climbing path of 8 levels from one reading to the root with a grey sibling square at each level; boxes for the 32-byte root on the blockchain and the raw readings in the hospital database.')


# ---- 6.6 a 2 ETH virtual land sale ----
def f6():
    o = []
    o.append(boxt(20, 40, 130, 52, ['buyer', 'pays 2 ETH'], PANEL, AC, 13, bold_first=True))
    o.append(R(220, 30, 200, 160, PANEL, AC, 10))
    o.append(T(320, 56, 'marketplace contract', 13, bold=True))
    o.append(T(320, 82, 'fee 2 × 2.5%', 13)); o.append(T(320, 100, '= 0.05 ETH', 13, bold=True))
    o.append(T(320, 130, 'seller gets', 13)); o.append(T(320, 148, '2 − 0.05 = 1.95 ETH', 13, bold=True))
    o.append(A(150, 66, 218, 66, AC))
    o.append(boxt(500, 30, 200, 44, ['seller: 1.95 ETH'], NXS, NX, 14))
    o.append(boxt(500, 90, 200, 44, ['platform: 0.05 ETH'], LVS, LV, 14))
    o.append(A(422, 70, 498, 54, NX, 2, arrow='x')); o.append(A(422, 100, 498, 110, LV, 2, arrow='l'))
    o.append(boxt(500, 150, 200, 44, ['land NFT → buyer'], ACS, AC, 14))
    o.append(A(422, 160, 498, 170, AC))
    o.append(L(20, 220, 700, 220, INK, 1.5, '6 4'))
    o.append(T(20, 210, 'on-chain', 13, 'start', NX, True)); o.append(T(20, 240, 'off-chain', 13, 'start', MUT, True))
    o.append(T(20, 268, 'The ledger holds the NFT (who owns the land), the sale record and both payments.', 13, 'start'))
    o.append(boxt(20, 284, 300, 44, ['3D scene, textures, models'], PANEL, L2, 13))
    o.append(T(340, 311, 'stay on the platform\'s or a file network\'s servers', 13, 'start', MUT))
    return 342, ''.join(o)
FIG[6] = (f6, 'A 2 ETH land sale: the contract takes the 2.5% fee of 0.05 ETH and passes 1.95 ETH to the seller as the land NFT moves to the buyer. Those records are on-chain; the 3D scene itself stays off-chain.',
          'The buyer pays 2 ETH into a marketplace contract, which sends 1.95 ETH to the seller, 0.05 ETH to the platform and the land NFT to the buyer; a dashed line separates these on-chain records from the off-chain 3D scene files.')


# ---- 6.7 Tendermint: 5 of 7 precommits ----
def f7():
    o = [T(20, 26, 'n = 7 equal validators: f = ⌊(7 − 1) ÷ 3⌋ = 2, quorum = ⌊14 ÷ 3⌋ + 1 = 5', 14, 'start', bold=True)]
    for i in range(7):
        x = 70 + i * 92
        ok = i < 5
        o.append(node(x, 90, str(i + 1), 26, NXS if ok else PANEL, NX if ok else L2, 15))
        o.append(tick(x, 140, 7) if ok else cross(x, 140, 6))
        o.append(T(x, 172, 'precommit' if ok else 'silent', 13, fill=NX if ok else MUT))
    sc = 644 / 7
    o.append(R(40, 200, 644, 30, PANEL, L2, 4))
    o.append(R(40, 200, 5 * sc, 30, NXS, NX, 4))
    o.append(T(40 + 2.5 * sc, 220, '5 votes = 71% of the power', 13, bold=True))
    x23 = 40 + 644 * 2 / 3
    o.append(L(x23, 192, x23, 240, LV, 2.5, '5 4'))
    o.append(T(x23, 256, 'two-thirds = 4.67 votes', 13, fill=LV, bold=True))
    o.append(T(20, 292, '5 > 4.67, so the block commits; 4 votes (57%) would not. The 2 silent validators are exactly', 13, 'start'))
    o.append(T(20, 312, 'the f = 2 faults the network tolerates.', 13, 'start'))
    return 326, ''.join(o)
FIG[7] = (f7, 'Five of the seven validators precommit the same block, which is more than two-thirds (4.67) of the voting power, so it commits; four would not be enough. The two that stay silent are the f = 2 faults the network can tolerate.',
          'Seven validator circles, five ticked as precommitting and two crossed as silent; a bar with five of seven sevenths filled past a dashed two-thirds line at 4.67 votes.')


# ---- 6.8 throughput and ledger growth ----
def f8():
    o = [T(20, 26, 'One block every 12 s: 1,000 transactions × 500 bytes', 15, 'start', bold=True)]
    o.append(boxt(20, 46, 200, 60, ['1 block', '1,000 tx, 500,000 B'], ACS, AC, 13, bold_first=True))
    o.append(A(222, 76, 278, 76, AC)); o.append(T(250, 66, '÷ 12 s', 13, fill=MUT))
    o.append(boxt(280, 46, 180, 60, ['83.33 tx/s', '1,000 ÷ 12'], LVS, LV, 14, bold_first=True))
    o.append(A(120, 108, 120, 146, AC)); o.append(T(130, 132, '86,400 s ÷ 12 s', 13, 'start', MUT))
    o.append(boxt(20, 148, 200, 60, ['7,200 blocks', 'per day'], PANEL, AC, 14, bold_first=True))
    o.append(A(222, 178, 278, 178, AC)); o.append(T(250, 168, '× 0.5 MB', 13, fill=MUT))
    o.append(boxt(280, 148, 180, 60, ['3.6 GB', 'per day'], LVS, LV, 14, bold_first=True))
    o.append(T(470, 172, '7,200 × 500,000', 13, 'start', MUT)); o.append(T(470, 190, '= 3,600,000,000 B', 13, 'start', MUT))
    o.append(R(20, 236, 680, 92, PANEL, LV, 10, 1.5))
    o.append(T(36, 262, 'The two highlighted numbers pull against decentralisation:', 14, 'start', LV, True))
    o.append(T(36, 286, 'a faster chain adds more bytes, and every full node must store them (about 1.3 TB a year here),', 13, 'start'))
    o.append(T(36, 308, 'so fewer people can afford to run one. Rollups, sharding and channels try to escape this.', 13, 'start'))
    return 340, ''.join(o)
FIG[8] = (f8, 'A block of 1,000 transactions of 500 bytes every 12 s gives 83.33 transactions per second; 7,200 blocks a day add 3.6 GB to every full node. Those two numbers are the ones that pull against decentralisation.',
          'Boxes: one block of 1,000 transactions and 500,000 bytes, divided by 12 seconds gives 83.33 per second; 7,200 blocks a day times 500,000 bytes gives 3.6 GB a day; a note on the cost to full nodes.')


# ---- 6.9 the 30-day AI hash log ----
def f9():
    o = []
    o.append(boxt(20, 30, 150, 50, ['raw input'], PANEL, L2, 14)); o.append(boxt(20, 110, 150, 50, ['AI model'], PANEL, L2, 14))
    o.append(T(95, 186, 'both stay off-chain', 13, fill=MUT))
    o.append(A(172, 55, 228, 55, AC)); o.append(A(172, 135, 228, 135, AC))
    o.append(T(200, 46, 'hash', 13, fill=MUT)); o.append(T(200, 126, 'hash', 13, fill=MUT))
    o.append(R(230, 34, 128, 42, ACS, AC, 4)); o.append(T(294, 60, 'input 32 B', 13, bold=True))
    o.append(R(230, 114, 128, 42, ACS, AC, 4)); o.append(T(294, 140, 'model 32 B', 13, bold=True))
    o.append(A(360, 55, 418, 88, AC)); o.append(A(360, 135, 418, 104, AC))
    o.append(boxt(420, 70, 140, 52, ['one log entry', '32 + 32 = 64 B'], NXS, NX, 13, bold_first=True))
    o.append(T(580, 90, 'an auditor', 13, 'start', MUT)); o.append(T(580, 108, 're-hashes both', 13, 'start', MUT))
    sc = 600 / 1920
    o.append(T(20, 236, 'Storage on the ledger', 14, 'start', bold=True))
    o.append(R(80, 250, 64 * sc, 32, NXS, NX, 2)); o.append(T(80 + 64 * sc + 8, 271, '1 day: 1,000 × 64 B = 64,000 B = 64 kB', 13, 'start'))
    o.append(R(80, 296, 1920 * sc, 32, ACS, AC, 4)); o.append(T(80 + 960 * sc, 317, '30 days: 64 kB × 30 = 1,920 kB = 1.92 MB', 13, bold=True))
    for d in range(1, 30):
        x = 80 + d * 64 * sc
        o.append(L(x, 298, x, 304, AC, 1))
    return 342, ''.join(o)
FIG[9] = (f9, 'Each prediction puts two 32-byte hashes on the ledger, 64 bytes in all, while the raw input and the model stay off-chain. 1,000 logs a day use 64 kB, and 30 days use 1.92 MB.',
          'A raw input and an AI model, both off-chain, are hashed to 32 bytes each and combined into a 64-byte log entry; below, a short bar for one day of 64 kB and a long bar for 30 days of 1.92 MB.')


spec = make_spec(FIG)


def text_fixes(k):
    return {
        2: [('through a shim API. Only a few universities teach its lifecycle in detail.', 'through a shim API.')],
        6: [('Games, social worlds and virtual property markets use this. Only a few universities teach the full value-chain view.',
             'Games, social worlds and virtual property markets use this.')],
        7: [('and Bitcoin compatibility. Only a few universities teach this set. Each is a design choice.', 'and Bitcoin compatibility. Each is a design choice.')],
        8: [('It then covers regulation, energy, interoperability and quantum risk. Only a few universities teach this as a separate topic; most mention it in passing.',
             'It then covers regulation, energy, interoperability and quantum risk.')],
        9: [('Integration means the ledger talks to ERP, payment and AI systems. Only a few universities teach this as a full unit.',
             'Integration means the ledger talks to ERP, payment and AI systems.')],
    }.get(k, [])


def drop_sources():
    # university-hosted pages: the books name no universities
    return ['ocw.mit.edu']
