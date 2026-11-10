"""Claude's hand-drawn figures for c-sec-u6 (Cryptography and Network Security, unit 6: system security, firewalls,
intrusion detection, access control and risk), one per chapter, from each chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
ARR = {AC: 'n', L2: 'm', LV: 'l', NX: 'x', MUT: 'm', INK: 'm'}


def ar(x1, y1, x2, y2, c=AC, w=2, dash=None):
    return L(x1, y1, x2, y2, c, w, dash, arrow=ARR[c])


def dot(x, y, c, filled=True, r=8):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{c if filled else PANEL};stroke:{c};stroke-width:2.2"/>'


# ---- 6.1 first-match firewall rules ----
def f1():
    cols = [(340, 36, '#'), (376, 150, 'source'), (526, 84, 'to port'), (610, 80, 'action')]
    rules = [('1', 'TCP 10.0.0.0/24', '443', 'allow'), ('2', 'TCP any', '23', 'deny'), ('3', 'TCP any', '80', 'allow'), ('4', 'all', 'any', 'deny')]
    o = [T(20, 26, 'packets to 192.168.1.10', 14, 'start', MUT, True), T(340, 26, 'rule table, read top down', 14, 'start', MUT, True)]
    for x, w, h in cols:
        o.append(boxt(x, 40, w, 30, [h], PANEL, L2, 13, True, rx=0))
    hit = {0: NXS, 1: LVS, 3: LVS}
    for i, r in enumerate(rules):
        y = 70 + i * 36
        for (x, w, _), s in zip(cols, r):
            o.append(boxt(x, y, w, 36, [s], hit.get(i, PANEL), L2, 14, False, rx=0))
    pk = [(0, '(a) 10.0.0.5 → :443', NX, 'rule 1: allow'), (1, '(b) 8.8.8.8 → :23', LV, 'rule 2: deny'), (3, '(c) 10.0.0.5 → :22', LV, 'rule 4: deny')]
    for i, s, c, res in pk:
        y = 70 + i * 36
        o.append(boxt(20, y + 3, 220, 30, [s], NXS if c == NX else LVS, c, 14, True))
        o.append(ar(240, y + 18, 338, y + 18, c))
    o.append(T(130, 228, 'port 22 fails rules 1, 2 and 3', 13, fill=LV))
    o.append(T(20, 260, 'First match wins: (a) rule 1 allows, (b) rule 2 denies, (c) falls through to rule 4, deny all.', 14, 'start', INK, True))
    return 274, ''.join(o)


FIG[1] = (f1, 'Each packet is checked against the rules from the top, and the first match decides. Packet (a) is allowed by rule 1, (b) is denied by rule 2, and (c) falls through to rule 4, deny all.',
          'A four-rule table: allow 10.0.0.0/24 to port 443, deny port 23, allow port 80, deny all. Three packets on the left point at their matching rows: port 443 to rule 1, port 23 to rule 2 and port 22 to rule 4.')


# ---- 6.2 IDS confusion matrix ----
def f2():
    o = [T(230, 30, 'alert', 14, bold=True), T(360, 30, 'no alert', 14, bold=True)]
    o += [T(150, 74, 'attack (20)', 14, 'end', LV, True), T(150, 134, 'normal (980)', 14, 'end', NX, True)]
    cells = [(165, 44, 'TP = 18', NXS, NX), (295, 44, 'FN = 2', PANEL, L2), (165, 104, 'FP = 30', LVS, LV), (295, 104, 'TN = 950', PANEL, L2)]
    for x, y, s, f, st in cells:
        o.append(boxt(x, y, 130, 60, [s], f, st, 16, True, rx=0))
    m = [('detection rate', '18 ÷ 20 = 90%', NX), ('false positive rate', '30 ÷ 980 = 3.06%', LV), ('precision', '18 ÷ 48 = 37.5%', AC)]
    for i, (a, b, c) in enumerate(m):
        o += [T(460, 52 + i * 48, a, 14, 'start', MUT, True), T(460, 72 + i * 48, b, 16, 'start', c, True)]
    o.append(T(20, 214, '48 alerts', 14, 'start', INK, True))
    o += [R(110, 196, 18 * 12, 30, NXS, NX, 3, 1.5), T(110 + 9 * 12, 216, '18 real', 14, fill=NX, bold=True),
          R(110 + 18 * 12, 196, 30 * 12, 30, LVS, LV, 3, 1.5), T(110 + 18 * 12 + 15 * 12, 216, '30 false', 14, fill=LV, bold=True)]
    o.append(T(20, 266, 'Attacks are only 20 of 1000 packets (2%), so the 30 false alerts outnumber the 18 real ones.', 14, 'start'))
    return 280, ''.join(o)


FIG[2] = (f2, 'Of 1000 packets, 20 are an attack. The sensor catches 18 of them (90%) but also alerts on 30 normal packets, so only 18 of the 48 alerts are real: precision 37.5%.',
          'A confusion matrix: TP 18, FN 2, FP 30, TN 950. Beside it the detection rate 18 / 20 = 90%, false positive rate 30 / 980 = 3.06% and precision 18 / 48 = 37.5%. A bar splits the 48 alerts into 18 real and 30 false.')


# ---- 6.3 /28 honeynet addresses ----
def f3():
    x0, w, y = 40, 40, 150
    o = [T(20, 26, '10.0.0.0/28:  32 − 28 = 4 host bits, so 2⁴ = 16 addresses', 15, 'start', bold=True)]
    for lo, hi, yb, s, c in [(0, 15, 64, '16 addresses', INK), (1, 14, 98, '14 usable hosts (16 − 2)', AC), (3, 14, 132, '12 for honeypots (14 − 2)', NX)]:
        o += [brace(x0 + lo * w + 4, x0 + (hi + 1) * w - 4, yb, c), T(x0 + (lo + hi + 1) * w / 2, yb - 7, s, 14, fill=c, bold=True)]
    for i in range(16):
        f, st = (PANEL, L2) if i in (0, 15) else (ACS, AC) if i == 1 else (LVS, LV) if i == 2 else (NXS, NX)
        o.append(R(x0 + i * w + 1, y, w - 2, 40, f, st, 3, 1.5))
        o.append(TM(x0 + i * w + w / 2, y + 26, str(i), 15, bold=True))
    o.append(T(360, 212, 'last octet of 10.0.0.x', 13, fill=MUT))
    leg = [(40, 244, PANEL, L2, 'network 10.0.0.0 and broadcast 10.0.0.15'), (420, 244, ACS, AC, 'gateway 10.0.0.1'),
           (40, 270, LVS, LV, 'IDS sensor 10.0.0.2'), (420, 270, NXS, NX, 'honeypots 10.0.0.3 to 10.0.0.14')]
    for x, yy, f, st, s in leg:
        o += [R(x, yy - 12, 16, 16, f, st, 3, 1.5), T(x + 24, yy + 1, s, 14, 'start')]
    return 286, ''.join(o)


FIG[3] = (f3, 'A /28 holds 16 addresses, 10.0.0.0 to 10.0.0.15. Dropping the network and broadcast leaves 14 hosts, and reserving the gateway and IDS sensor leaves 12 honeypot addresses.',
          'Sixteen cells numbered 0 to 15 for 10.0.0.0/28. Cells 0 and 15 are grey for network and broadcast, cell 1 is the gateway, cell 2 the IDS sensor and cells 3 to 14 are honeypots. Braces above mark 16 addresses, 14 usable and 12 for honeypots.')


# ---- 6.4 stack buffer overflow ----
def f4():
    x0, w, y = 40, 38, 96
    bytes_ = ['41'] * 8 + ['42'] * 4 + ['a0', '84', '04', '08', '00']
    o = [T(20, 26, 'strcpy(buf, input): 16 input bytes, then a null byte', 15, 'start', bold=True)]
    regs = [(0, 7, 'char buf[8]', PANEL, AC), (8, 11, 'saved EBP', PANEL, LV), (12, 15, 'return address', PANEL, NX)]
    for lo, hi, s, _, c in regs:
        o += [brace(x0 + lo * w + 3, x0 + (hi + 1) * w - 3, 80, c), T(x0 + (lo + hi + 1) * w / 2, 72, s, 14, fill=c, bold=True)]
    o.append(T(x0 + 16.5 * w, 72, 'next', 13, fill=MUT, bold=True))
    for i, b in enumerate(bytes_):
        f, st = (ACS, AC) if i < 8 else (LVS, LV) if i < 12 else (NXS, NX) if i < 16 else (PANEL, MUT)
        o.append(R(x0 + i * w + 1, y, w - 2, 38, f, st, 3, 1.5 if i < 16 else 1.5))
        o.append(TM(x0 + i * w + w / 2, y + 25, b, 14, bold=True))
        o.append(T(x0 + i * w + w / 2, y + 56, str(i), 13, fill=MUT))
    o += [ar(x0, 178, x0 + 17 * w, 178, L2), T(x0 + 17 * w, 196, 'higher addresses', 13, 'end', MUT)]
    o.append(boxt(20, 214, 400, 56, ['little-endian: bytes a0 84 04 08', 'return address 0x080484a0 = 134513824'], NXS, NX, 14, True))
    o.append(boxt(440, 214, 260, 56, ['offset 16: the extra 0x00', 'corrupts the next word'], PANEL, MUT, 14, True, dash='5 4'))
    o.append(T(20, 296, 'The 0x41 bytes fill buf, 0x42 overwrites saved EBP, and EIP jumps to 0x080484a0 on return.', 14, 'start'))
    return 310, ''.join(o)


FIG[4] = (f4, 'Sixteen bytes fill the 8-byte buffer with 41, overwrite saved EBP with 42 and the return address with a0 84 04 08, which reads as 0x080484a0. The null byte strcpy adds lands at offset 16.',
          'Seventeen byte cells at offsets 0 to 16: eight 41s under char buf[8], four 42s under saved EBP, a0 84 04 08 under return address, and 00 at offset 16. Boxes below give the address 0x080484a0 = 134513824 and note the extra null byte.')


# ---- 6.5 setuid mode 4755 ----
def f5():
    o = []
    digs = [('4', 'special', 'setuid', ACS, AC), ('7', 'owner: root', 'rwx', PANEL, L2), ('5', 'group: auditors', 'r-x', PANEL, L2),
            ('5', 'other', 'r-x', NXS, NX)]
    for i, (d, lab, perm, f, st) in enumerate(digs):
        x = 40 + i * 170
        o += [T(x + 60, 30, lab, 14, fill=st if st != L2 else INK, bold=True),
              R(x, 40, 120, 56, f, st, 8), T(x + 60, 78, d, 28, bold=True),
              TM(x + 60, 120, perm, 16, fill=st if st != L2 else INK, bold=True)]
    o.append(TM(360, 150, 'ls -l:  -rwsr-xr-x  root auditors', 14, fill=MUT))
    o.append(boxt(20, 186, 320, 56, ['setuid: the effective uid becomes', 'the file owner\'s, root = 0'], ACS, AC, 14, True))
    o.append(boxt(380, 186, 320, 56, ['alice is not root, not in auditors', 'other triad r-x: she may execute'], NXS, NX, 14, True))
    o += [P([(100, 128), (100, 184)], AC, 2), ar(100, 176, 100, 184, AC), ar(610, 128, 610, 184, NX, 2)]
    o.append(boxt(200, 288, 320, 56, ['the program runs with', 'real uid = alice, effective uid = 0'], LVS, LV, 14, True))
    o += [ar(180, 242, 260, 286, LV), ar(540, 242, 460, 286, LV)]
    o.append(T(20, 376, 'Setuid is ignored on a nosuid mount, for an interpreted script, or when execute permission is missing.', 13, 'start', MUT))
    return 390, ''.join(o)


FIG[5] = (f5, 'Mode 4755 reads as setuid, then rwx, r-x, r-x. Alice falls in the other triad, so she may execute, and because the owner is root the program runs with effective UID 0.',
          'Four digit boxes 4, 7, 5, 5 labelled special setuid, owner root rwx, group auditors r-x and other r-x. Arrows lead from the setuid digit and the other triad to a box saying the program runs with real UID alice and effective UID 0.')


# ---- 6.6 access matrix, ACL and capability list ----
def f6():
    gx, gy, cw, ch = 130, 50, 90, 44
    M = {'Alice': ['rw', 'r', '−'], 'Bob': ['r', 'rw', 'x'], 'Carol': ['−', 'r', 'rwx']}
    o = []
    for j, f in enumerate(['f1', 'f2', 'f3']):
        o.append(T(gx + j * cw + cw / 2, gy - 12, f, 15, fill=LV if j == 1 else INK, bold=True))
    for i, s in enumerate(['Alice', 'Bob', 'Carol']):
        y = gy + i * ch
        o.append(T(gx - 14, y + 28, s, 15, 'end', AC if s == 'Bob' else INK, True))
        for j in range(3):
            f = ACS if s == 'Bob' else LVS if j == 1 else PANEL
            st = LV if (s == 'Bob' and j == 1) else L2
            o.append(R(gx + j * cw, y, cw, ch, f, st, 0, 2.5 if st == LV else 1.2,
                       '4 3' if (s == 'Carol' and j == 0) else None))
            o.append(TM(gx + j * cw + cw / 2, y + 28, M[s][j], 16, bold=(s == 'Bob' or j == 1)))
    o.append(boxt(450, 30, 250, 60, ['ACL of f2 (the column)', 'Alice r, Bob rw, Carol r'], LVS, LV, 14, True))
    o.append(boxt(450, 120, 250, 60, ['Bob\'s capabilities (the row)', 'f1 r, f2 rw, f3 x'], ACS, AC, 14, True))
    o += [P([(gx + 1.5 * cw, gy + 3 * ch), (gx + 1.5 * cw, gy + 3 * ch + 18), (420, gy + 3 * ch + 18), (420, 60), (446, 60)], LV, 2),
          ar(436, 60, 448, 60, LV), ar(gx + 3 * cw, gy + ch * 1.5, 448, 150, AC)]
    o.append(T(20, 254, '(a) Bob, f2 = rw contains w, so Bob can write f2.', 14, 'start', AC, True))
    o.append(T(20, 278, '(b) Carol, f1 = − has no r, so Carol cannot read f1.', 14, 'start', MUT, True))
    o.append(T(20, 302, 'An ACL is stored with the file; a capability list travels with the user. Each has 3 entries here.', 13, 'start'))
    return 316, ''.join(o)


FIG[6] = (f6, 'Reading the f2 column gives its ACL: Alice r, Bob rw, Carol r. Reading Bob\'s row gives his capability list: f1 r, f2 rw, f3 x. The cell Bob, f2 holds rw, so Bob can write f2.',
          'A 3 by 3 access matrix with subjects Alice, Bob and Carol and objects f1, f2 and f3. The f2 column is shaded and leads to an ACL box; Bob\'s row is shaded and leads to a capability box. Carol\'s f1 cell is empty, so she cannot read f1.')


# ---- 6.7 SLE, ALE and a control that costs too much ----
def f7():
    o = [boxt(20, 30, 160, 56, ['asset value', '₹10,00,000'], PANEL, L2, 15, True),
         boxt(280, 30, 160, 56, ['SLE', '₹2,50,000'], LVS, LV, 15, True),
         boxt(540, 30, 160, 56, ['ALE', '₹50,000 a year'], LVS, LV, 15, True)]
    o += [ar(180, 58, 278, 58, LV), T(229, 50, '× EF', 14, fill=LV, bold=True), T(229, 76, '0.25', 14, fill=LV),
          ar(440, 58, 538, 58, LV), T(489, 50, '× ARO', 14, fill=LV, bold=True), T(489, 76, '0.2 / yr', 14, fill=LV)]
    k = 0.006
    bars = [('ALE now', 50000, LVS, LV), ('ALE with control', 20000, NXS, NX), ('yearly saving', 30000, NXS, NX), ('control cost', 60000, LVS, LV)]
    for i, (s, v, f, st) in enumerate(bars):
        y = 124 + i * 38
        o += [T(190, y + 18, s, 14, 'end', INK, True), R(200, y, v * k, 26, f, st, 3, 1.5),
              T(210 + v * k, y + 18, f'₹{v // 1000},000', 14, 'start', st, True)]
    o.append(T(20, 316, 'Net = 30,000 − 60,000 = −₹30,000 a year: the control costs more than it saves, so reject it.', 14, 'start', LV, True))
    return 330, ''.join(o)


FIG[7] = (f7, 'An asset of ₹10,00,000 with exposure factor 25% gives SLE ₹2,50,000, and 0.2 events a year gives ALE ₹50,000. A ₹60,000 control saves only ₹30,000, a net loss of ₹30,000 a year.',
          'A chain: asset value 10,00,000 rupees times 0.25 gives SLE 2,50,000, times 0.2 a year gives ALE 50,000. Bars compare ALE now 50,000, ALE with the control 20,000, yearly saving 30,000 and control cost 60,000.')


# ---- 6.8 SaaS shared responsibility ----
def f8():
    o = [boxt(20, 16, 330, 40, ['provider secures'], ACS, AC, 15, True), boxt(370, 16, 330, 40, ['customer secures'], LVS, LV, 15, True)]
    o += [boxt(20, 70, 330, 46, ['(a) physical security of the data centre'], PANEL, AC, 14),
          boxt(20, 126, 330, 46, ['(d) hypervisor patching'], PANEL, AC, 14),
          boxt(370, 70, 330, 46, ['(b) key policy: who can decrypt'], PANEL, LV, 14),
          boxt(370, 126, 330, 46, ['(c) roles for the 500 users'], PANEL, LV, 14)]
    o.append(T(20, 210, 'SaaS stack, bottom to top', 13, 'start', MUT, True))
    segs = [('facility', 80, ACS, AC), ('network', 80, ACS, AC), ('hypervisor', 96, ACS, AC), ('OS', 56, ACS, AC),
            ('application', 108, ACS, AC), ('data, keys', 130, LVS, LV), ('identities', 130, LVS, LV)]
    x = 20
    for s, w, f, st in segs:
        o.append(boxt(x, 220, w, 40, [s], f, st, 13, True, rx=0))
        x += w
    o.append(T(20, 296, 'Tally: provider 2, (a) and (d); customer 2, (b) and (c).', 15, 'start', INK, True))
    o.append(T(20, 320, 'Given, not results: 500 users, 3 roles, MFA and 90-day audit logs.', 13, 'start', MUT))
    return 334, ''.join(o)


FIG[8] = (f8, 'In the SaaS CRM the provider secures the data centre and patches the hypervisor, while the customer sets the key policy and assigns roles: two controls each.',
          'Two columns: provider secures (a) physical security and (d) hypervisor patching; customer secures (b) the key policy and (c) roles for 500 users. A stack bar shades facility, network, hypervisor, OS and application as provider, and data, keys and identities as customer.')


# ---- 6.9 anomaly scores, threshold and an evasion ----
def f9():
    fx = lambda s: 170 + s * 520
    o = [R(fx(0.7), 50, fx(1.0) - fx(0.7), 220, ACS, ACS, 0, 0),
         T((fx(0.7) + fx(1.0)) / 2, 66, 'flagged', 14, fill=AC, bold=True),
         L(fx(0.7), 40, fx(0.7), 270, INK, 2, '6 4'), T(fx(0.7), 34, 'threshold t = 0.70', 14, bold=True)]
    o.append(xaxis(fx(0), fx(1), 270, [0, 0.2, 0.4, 0.6, 0.8, 1.0], fx, None, lambda v: f'{v:.1f}'))
    rows = [(100, 'normal', [(0.10, NX, False), (0.20, NX, False), (0.35, NX, False), (0.55, NX, False)]),
            (156, 'attacks', [(0.65, LV, False), (0.80, LV, True), (0.90, LV, True), (0.95, LV, True)]),
            (220, 'after evasion', [(0.65, LV, False), (0.60, LV, False), (0.90, LV, True), (0.95, LV, True)])]
    for y, lab, pts in rows:
        o.append(T(20, y + 5, lab, 14, 'start', INK, True))
        o.append(L(fx(0), y, fx(1), y, LN, 1))
        for s, c, fl in pts:
            o.append(dot(fx(s), y, c, fl if c == LV else True))
            if lab == 'after evasion' and s == 0.60:
                o.append(T(fx(s) - 14, y + 5, '0.60', 13, 'end', c, True)); continue
            dy = 26 if (s == 0.95 or (lab == 'after evasion' and s == 0.65)) else -14
            o.append(T(fx(s), y + dy, f'{s:.2f}', 13, fill=c, bold=True))
    o.append(arc(fx(0.8) - 4, 166, fx(0.6) + 6, 210, -0.2, LV, 1.8, 'l', '5 4'))
    o.append(T(20, 322, 'Before: 3 of 4 attacks flagged, TPR = 3 ÷ 4 = 0.75; no normal score flagged, FPR = 0.', 14, 'start', AC, True))
    o.append(T(20, 346, 'After 0.80 is pushed to 0.60: only 0.90 and 0.95 pass the line, TPR = 2 ÷ 4 = 0.50, FPR still 0.', 14, 'start', LV, True))
    return 360, ''.join(o)


FIG[9] = (f9, 'At threshold 0.70 the attack scoring 0.65 is missed, so 3 of 4 attacks are caught: TPR 0.75 with no false alarms. Pushing the 0.80 attack down to 0.60 drops TPR to 0.50.',
          'A score line from 0 to 1 with a shaded flagged zone above the threshold 0.70. Normal scores 0.10, 0.20, 0.35 and 0.55 are all below it. Attack scores 0.65, 0.80, 0.90 and 0.95 have three flagged. After evasion the 0.80 attack moves to 0.60, leaving two flagged.')

spec = make_spec(FIG)
