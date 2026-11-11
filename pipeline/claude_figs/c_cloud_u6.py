"""Claude's hand-drawn figures for c-cloud-u6 (Cloud Computing, unit 6: cloud security), one per chapter, from each
chapter's worked example. The chapter text already describes these drawings (an attack path, the log timeline, the
policy gates, the response timeline), so no sentence needs rewriting."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def hbar(x, y, w, h, fill, c, label=None, size=13, fc=INK, bold=False):
    o = R(x, y, w, h, fill, c, 4, 2)
    if label: o += T(x + w / 2, y + h / 2 + size * 0.36, label, size, fill=fc, bold=bold)
    return o


def chain(xs, y, w, h, items, gap_arrow=True):
    o = []
    for x, (lines, f, c) in zip(xs, items):
        o.append(boxt(x, y, w, h, lines, f, c, 13))
    if gap_arrow:
        for x, nx in zip(xs, xs[1:]):
            o.append(L(x + w + 2, y + h / 2, nx - 4, y + h / 2, AC, 2, arrow='n'))
    return ''.join(o)


# ---- 6.1 the attack path and its expected loss ----
def f1():
    o = [T(40, 24, 'Attack path: a threat uses a vulnerability to reach the asset', 15, 'start', bold=True)]
    xs = [30, 205, 380, 555]
    o.append(chain(xs, 44, 140, 66, [(['stolen key', '(attack vector)'], LVS, LV), (['looks like a valid', 'authenticated user'], PANEL, L2),
                                    (['bucket policy: any', 'authenticated user', 'can read'], LVS, LV), (['10,000 customer', 'records (asset)'], ACS, AC)]))
    o.append(T(450, 132, 'the vulnerability', 13, fill=LV, bold=True))
    y = 176
    o.append(T(40, y, 'Expected loss', 15, 'start', bold=True))
    o.append(boxt(40, y + 16, 160, 50, ['asset value AV', '₹50,00,000'], PANEL, L2, 13))
    o.append(L(202, y + 41, 248, y + 41, AC, 2, arrow='n')); o.append(T(225, y + 32, '× 0.4', 13, bold=True))
    o.append(boxt(252, y + 16, 160, 50, ['SLE (one incident)', '₹20,00,000'], LVS, LV, 13))
    o.append(L(414, y + 41, 470, y + 41, AC, 2, arrow='n')); o.append(T(442, y + 32, '× 2 / yr', 13, bold=True))
    o.append(boxt(474, y + 16, 180, 50, ['ALE (per year)', '₹40,00,000'], LVS, LV, 13))
    o.append(T(40, y + 100, 'EF 0.4: one incident loses 40% of the asset. λ = 2 incidents a year.', 13, 'start'))
    o.append(T(40, y + 122, 'Fixing the policy (read only for named roles) breaks the path even if a key leaks again.', 14, 'start', bold=True))
    return y + 138, ''.join(o)
FIG[1] = (f1, 'A stolen key passes as an authenticated user, and the loose bucket policy lets it read 10,000 records. With AV ₹50,00,000 and EF 0.4, one incident costs ₹20,00,000; two a year make ₹40,00,000.',
          'A chain from stolen key to authenticated user to a loose bucket policy to 10,000 customer records, above a row turning asset value into single and annual loss expectancy.')


# ---- 6.2 the MAC catches the rewritten amount ----
def f2():
    o = []
    o.append(boxt(30, 30, 180, 80, ['UPI app', 'A = ₹10,000, N = 4321', 'MAC = 266'], ACS, AC, 13))
    o.append(boxt(270, 30, 180, 80, ['logging sidecar', 'rewrites A to ₹1,000', 'MAC still 266'], LVS, LV, 13))
    o.append(boxt(510, 30, 180, 80, ['bank', 'recomputes from A = 1,000', 'gets 426 ≠ 266'], NXS, NX, 13))
    o.append(L(212, 70, 266, 70, AC, 2.5, arrow='n')); o.append(L(452, 70, 506, 70, LV, 2.5, arrow='l'))
    o.append(Tb(600, 140, 'rejected', 15, bold=True, fill=NX))
    o.append(T(40, 184, 'MAC = (31A + N) mod 997', 14, 'start', bold=True))
    o.append(T(40, 208, 'sent:  31 × 10,000 + 4,321 = 314,321;  314,321 − 997 × 315 = 266', 13, 'start'))
    o.append(T(40, 230, 'bank:  31 × 1,000 + 4,321 = 35,321;  35,321 − 997 × 35 = 426', 13, 'start'))
    o.append(T(40, 266, 'Integrity failed and the MAC caught it. Encryption alone would hide the amount from an', 14, 'start'))
    o.append(T(40, 286, 'eavesdropper, but it would not notice a changed ciphertext.', 14, 'start'))
    return 302, ''.join(o)
FIG[2] = (f2, 'The app sends ₹10,000 with MAC 266; the sidecar changes the amount to ₹1,000, the bank recomputes 426, and the mismatch rejects the payment. Integrity is what failed.',
          'Three boxes left to right, UPI app, logging sidecar and bank, showing the amount changed in the middle and the bank’s MAC 426 not matching 266, so the payment is rejected.')


# ---- 6.3 rotating the KEK touches only the wrapped DEKs ----
def f3():
    o = [T(40, 24, 'Envelope encryption for one tenant bucket', 15, 'start', bold=True)]
    o.append(boxt(260, 40, 200, 46, ['tenant KEK (rotated)'], LVS, LV, 14))
    for i in range(6):
        x = 116 + i * 96
        lab = '…' if i == 4 else ('DEK 1,000' if i == 5 else f'DEK {i + 1}')
        o.append(L(360, 88, x + 40, 118, L2, 1.2))
        o.append(boxt(x, 120, 80, 34, [lab], NXS, NX, 13))
        o.append(L(x + 40, 156, x + 40, 178, L2, 1.2, arrow='m'))
        o.append(boxt(x, 180, 80, 44, ['object', '4 MB' if i != 4 else '…'], PANEL, L2, 13))
    o.append(T(20, 134, 'wrapped', 13, 'start', NX, True)); o.append(T(20, 152, '60 B each', 13, 'start', NX, True))
    o.append(T(40, 262, 'KEK rotation: rewrap 1,000 × 60 B = 60,000 B; 0 objects re-encrypted.', 14, 'start', bold=True, fill=NX))
    o.append(T(40, 286, 'Full DEK rotation: re-encrypt 1,000 × 4 MB = 4,000,000,000 B (4 GB).', 14, 'start', bold=True, fill=LV))
    o.append(T(40, 310, '4,000,000,000 ÷ 60,000 ≈ 66,667 times less work, because only the small wrapped keys change.', 13, 'start'))
    return 326, ''.join(o)
FIG[3] = (f3, 'One tenant KEK wraps 1,000 data keys, each protecting one 4 MB object. Rotating the KEK rewrites only the 60,000 bytes of wrapped keys; rotating the data keys would rewrite 4 GB, about 66,667 times more.',
          'A key hierarchy: one tenant KEK at the top, a row of data keys under it, and a row of 4 MB objects under those, with the rewrap cost and the full re-encryption cost below.')


# ---- 6.4 the log timeline: active, archive, purge ----
def f4():
    X0, X1 = 60, 660
    fx = lambda d: X0 + d / 400 * (X1 - X0)
    o = [T(40, 24, 'Logs at 10 GB a day', 15, 'start', bold=True)]
    o.append(hbar(fx(0), 50, fx(90) - fx(0), 44, ACS, AC, 'active', 13, bold=True))
    o.append(hbar(fx(90), 50, fx(365) - fx(90), 44, NXS, NX, 'archive, 10:1 compressed', 13, bold=True))
    o.append(hbar(fx(365), 50, fx(395) - fx(365), 44, LVS, LV))
    o.append(T((fx(365) + fx(395)) / 2, 112, 'purge', 13, fill=LV, bold=True))
    o.append(T(fx(45), 116, '10 × 90 = 900 GB', 13, bold=True))
    o.append(T(fx(227), 116, '10 × 275 = 2,750 GB raw → 275 GB', 13, bold=True))
    o.append(xaxis(X0, X1, 136, [0, 90, 180, 270, 365, 395], fx, 'day'))
    # stored volume
    s = 150 / 1175
    o.append(T(40, 216, 'Stored at day 364', 14, 'start', bold=True))
    o.append(hbar(200, 198, 900 * s * 2, 30, ACS, AC, '900', 13))
    o.append(hbar(200 + 900 * s * 2, 198, 275 * s * 2, 30, NXS, NX, '275', 13))
    o.append(T(200 + 1175 * s * 2 + 10, 219, '= 1,175 GB', 14, 'start', bold=True))
    o.append(T(40, 262, 'After purge', 14, 'start', bold=True))
    o.append(T(200, 262, '0 GB for the log set written up to day 365', 14, 'start', bold=True))
    o.append(T(40, 298, 'Counting the raw 2,750 GB instead of the compressed 275 GB is the common slip.', 13, 'start', MUT))
    return 314, ''.join(o)
FIG[4] = (f4, 'Logs stay active for 90 days (900 GB), are archived at 10:1 from day 90 to 365 (2,750 GB raw, 275 GB stored), then purged by day 395. At day 364 the store holds 1,175 GB.',
          'A timeline from day 0 to 395 split into active, archive and purge bars, above a stacked bar of 900 GB active plus 275 GB archive making 1,175 GB.')


# ---- 6.5 three requests through the policy gates ----
def f5():
    o = []
    gx = [180, 330, 480]
    gates = ['MFA present?', 'IP in 10.0.0.0/8?', 'role allows read?']
    for x, g in zip(gx, gates):
        o.append(T(x + 55, 30, g, 13, bold=True))
    reqs = [('A', ['yes', '10.1.2.3 yes', 'yes'], 3, 'Allow'),
            ('B', ['yes', '192.168.1.5 no', ''], 1, 'Deny'),
            ('C', ['no', '', ''], 0, 'Deny')]
    y = 50
    for name, ans, passed, verdict in reqs:
        o.append(boxt(30, y, 110, 44, [f'request {name}'], PANEL, L2, 14))
        x_prev = 142
        for i, (x, a) in enumerate(zip(gx, ans)):
            if i > passed: break
            ok = i < passed
            o.append(L(x_prev, y + 22, x - 4, y + 22, AC if ok or i == passed else L2, 2, arrow='n'))
            o.append(boxt(x, y, 110, 44, [a], NXS if ok else LVS, NX if ok else LV, 13))
            x_prev = x + 112
        if passed == 3:
            o.append(L(x_prev, y + 22, 626, y + 22, AC, 2, arrow='n'))
            o.append(boxt(630, y, 70, 44, ['Allow'], NXS, NX, 14))
        else:
            o.append(L(gx[passed] + 112, y + 22, 626, y + 22, LV, 2, '5 4', arrow='l'))
            o.append(boxt(630, y, 70, 44, ['Deny'], LVS, LV, 14))
        y += 64
    o.append(T(40, y + 20, 'Every condition must hold; the first one that fails ends in Deny. Allowed 1, denied 2.', 14, 'start', bold=True))
    return y + 36, ''.join(o)
FIG[5] = (f5, 'Each request meets the gates in turn: A passes MFA, the 10.0.0.0/8 check and the role check, so it is allowed; B fails the IP check and C fails MFA, so allowed = 1 and denied = 2.',
          'Three rows, requests A, B and C, passing through gates for MFA, source IP and role; A reaches Allow, B stops at the IP gate and C at the MFA gate, both ending in Deny.')


# ---- 6.6 one login, three signed assertions ----
def f6():
    o = []
    o.append(boxt(30, 120, 110, 54, ['user'], PANEL, L2, 15))
    o.append(boxt(230, 106, 170, 82, ['identity provider', 'password + 6-digit TOTP', 'session 8 h'], ACS, AC, 13))
    o.append(L(142, 147, 226, 147, AC, 2.5, arrow='n')); o.append(Tb(184, 138, 'log in once', 13, bold=True))
    for i, y in enumerate([40, 125, 210]):
        o.append(boxt(540, y, 150, 44, [f'SaaS app {i + 1}'], NXS, NX, 14))
        o.append(L(402, 147, 536, y + 22, NX, 2, arrow='x'))
    o.append(Tb(470, 140, 'signed assertion', 13, fill=NX, bold=True))
    o.append(T(40, 296, 'Workday 8 h ÷ session 8 h = 1 login, so 1 TOTP entry. Assertions = 3 apps × 1 session = 3.', 14, 'start', bold=True))
    o.append(T(40, 320, 'The apps get a signed statement about the user, never the password or the one-time code.', 13, 'start'))
    return 336, ''.join(o)
FIG[6] = (f6, 'The user logs in to the identity provider once with a password and a 6-digit TOTP; that 8-hour session sends a signed assertion to each of the 3 apps, which never see the password or code.',
          'A user logging in once to an identity provider, which sends three signed assertions to three SaaS apps.')


# ---- 6.7 three packets from A-web ----
def f7():
    o = []
    o.append(R(20, 30, 420, 120, ACS, AC, 10, 1.5)); o.append(T(36, 52, 'tenant A 10.1.0.0/24', 13, 'start', AC, True))
    o.append(boxt(40, 70, 140, 56, ['A-web', '10.1.0.12'], PANEL, AC, 13))
    o.append(boxt(280, 70, 140, 56, ['A-db', '10.1.0.20'], PANEL, AC, 13))
    o.append(R(20, 190, 420, 110, LVS, LV, 10, 1.5)); o.append(T(36, 212, 'tenant B 10.2.0.0/24', 13, 'start', LV, True))
    o.append(boxt(280, 228, 140, 56, ['B', '10.2.0.5'], PANEL, LV, 13))
    o.append(L(182, 98, 276, 98, NX, 2.5, arrow='x')); o.append(Tb(229, 90, '1: 443', 13, bold=True))
    o.append(L(140, 128, 278, 238, LV, 2, '6 4')); o.append(L(110, 128, 276, 268, LV, 2, '6 4'))
    o.append(Tb(160, 186, '2: 22', 13, bold=True)); o.append(Tb(140, 230, '3: 443', 13, bold=True))
    o.append(T(330, 172, '× blocked at the tenant boundary', 13, 'middle', LV, True))
    # rule table
    x = 470
    o.append(T(x, 52, 'Rules, first match wins', 14, 'start', bold=True))
    rows = [('R1', 'allow TCP 443', '10.1.0.12 → 10.1.0.20'), ('R2', 'deny all', '10.1.0.0/24 → 10.2.0.0/24'), ('—', 'default', 'deny')]
    y = 70
    for r, a, b in rows:
        o.append(R(x, y, 230, 50, PANEL, L2, 6, 1.5))
        o.append(T(x + 12, y + 21, r, 13, 'start', bold=True)); o.append(T(x + 44, y + 21, a, 13, 'start', bold=True)); o.append(T(x + 44, y + 40, b, 13, 'start', MUT))
        y += 56
    o.append(T(x, 260, 'packet 1 → R1: allowed', 13, 'start', NX, True))
    o.append(T(x, 280, 'packets 2, 3 → R2: denied', 13, 'start', LV, True))
    o.append(T(20, 334, 'Allowed 1, denied 2: R2 denies every port to tenant B, so changing 22 to 443 does not help.', 14, 'start', bold=True))
    return 350, ''.join(o)
FIG[7] = (f7, 'From A-web, packet 1 to A-db on port 443 matches allow rule R1; packets 2 and 3 to tenant B match deny rule R2 whatever the port. One is allowed and two are denied.',
          'Tenant A’s web and database VMs and tenant B’s VM, with an allowed arrow from A-web to A-db and two dashed blocked arrows to B, beside a table of rules R1, R2 and default deny.')


# ---- 6.8 bursting the overflow through the broker ----
def f8():
    o = [T(40, 24, 'Cricket final: 150 requests/s for 2 hours', 15, 'start', bold=True)]
    o.append(boxt(30, 110, 110, 54, ['users', '150 req/s'], PANEL, L2, 13))
    o.append(L(142, 137, 206, 137, AC, 2.5, arrow='n'))
    o.append(boxt(210, 104, 130, 66, ['broker', 'splits at 100'], ACS, AC, 14))
    o.append(L(342, 124, 446, 74, NX, 2.5, arrow='x')); o.append(Tb(390, 88, '100 req/s', 13, bold=True))
    o.append(L(342, 150, 446, 200, LV, 2.5, arrow='l')); o.append(Tb(394, 196, '50 req/s', 13, bold=True))
    o.append(boxt(450, 44, 240, 60, ['private cloud', 'sized for 100 req/s'], NXS, NX, 13))
    o.append(boxt(450, 170, 240, 60, ['public cloud', 'over mTLS via the gateway'], LVS, LV, 13))
    o.append(T(40, 276, 'overflow 150 − 100 = 50 req/s × 7,200 s (2 h) = 360,000 requests', 14, 'start', bold=True))
    o.append(T(40, 300, 'cost 360,000 × ₹0.001 = ₹360', 14, 'start', bold=True))
    o.append(T(40, 324, 'The broker decides the split; the public side only ever sees the overflow, over a mutually authenticated link.', 13, 'start'))
    return 340, ''.join(o)
FIG[8] = (f8, 'The broker keeps 100 requests per second in the private cloud and sends the 50 overflow to the public cloud over mTLS for 2 hours: 360,000 requests costing ₹360.',
          'Users send 150 requests per second to a broker, which sends 100 to the private cloud and 50 over mTLS to the public cloud.')


# ---- 6.9 the response timeline ----
def f9():
    X0, X1 = 60, 660
    fx = lambda m: X0 + m / 180 * (X1 - X0)
    o = [T(40, 24, 'Incident at 09:00, service back at 12:00', 15, 'start', bold=True)]
    ph = [(0, 10, 'detect', LVS, LV), (10, 30, 'contain', ACS, AC), (30, 90, 'eradicate', NXS, NX), (90, 180, 'recover', PANEL, L2)]
    for a, b, n, f, c in ph:
        o.append(hbar(fx(a), 50, fx(b) - fx(a), 44, f, c, n if b - a >= 20 else '', 13, bold=True))
        o.append(T((fx(a) + fx(b)) / 2, 116, f'{b - a} min', 13, bold=True))
    o.append(T(fx(5), 42, 'detect', 13, fill=LV, bold=True))
    o.append(xaxis(X0, X1, 134, [0, 10, 30, 60, 90, 120, 150, 180], fx, 'minutes after 09:00'))
    o.append(T(fx(10), 200, '09:10 alert', 13, fill=MUT)); o.append(T(fx(30) + 30, 200, '09:30 contained', 13, fill=MUT)); o.append(T(fx(180), 200, '12:00 recovered', 13, 'end', MUT))
    o.append(L(fx(0), 222, fx(180), 222, INK, 2)); o.append(L(fx(0), 216, fx(0), 228, INK, 2)); o.append(L(fx(180), 216, fx(180), 228, INK, 2))
    o.append(Tb((fx(0) + fx(180)) / 2, 227, 'downtime 180 min = 3 h', 14, bold=True))
    o.append(T(40, 266, 'Detection 10 min; time to containment 30 min, of which the contain phase is 20.', 14, 'start'))
    o.append(T(40, 288, 'Containment stops the spread early, yet the service stays down until recovery ends.', 14, 'start', bold=True))
    return 304, ''.join(o)
FIG[9] = (f9, 'Detect 0 to 10 minutes, contain 10 to 30, eradicate 30 to 90, recover 90 to 180: containment is reached at 30 minutes, but the service is down for the full 180 minutes.',
          'A timeline bar from 09:00 to 12:00 cut into detect 10 minutes, contain 20, eradicate 60 and recover 90, with the total downtime of 180 minutes marked below.')


spec = make_spec(FIG)


def text_fixes(k):
    return []
