"""Claude's hand-drawn figures for c-sec-u1 (Cryptography and Network Security, unit 1: security concepts and threats),
one per chapter, from each chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


# ---- 1.1 availability over 30 days, and which goal each event touches ----
def f1():
    o = [T(20, 24, 'Result portal, 30 days = 30 × 24 × 60 = 43,200 minutes', 15, 'start', bold=True)]
    for d in range(30):
        r, c = divmod(d, 15)
        x, y = 40 + c * 44, 38 + r * 46
        down = d == 11
        o.append(R(x, y, 40, 40, NXS, NX, 4, 1.2))
        if down: o.append(R(x + 1, y + 1, 4, 38, LV, LV, 1, 0))
        o.append(T(x + 20, y + 25, str(d + 1), 13, fill=MUT))
    o.append(T(20, 150, 'All 108 minutes of downtime, drawn inside one day of 1,440 minutes:', 13, 'start', MUT))
    o.append(R(40, 160, 400, 28, NXS, NX, 4, 1.2)); o.append(R(40, 160, 108 / 1440 * 400, 28, LVS, LV, 4, 1.5))
    o.append(T(40 + 108 / 1440 * 400 + 8, 179, '108 min down', 13, 'start', LV, True))
    o.append(T(450, 179, '7.5% of a day, 0.25% of the month', 13, 'start', MUT))
    o.append(T(20, 222, 'A = (43,200 − 108) ÷ 43,200 = 43,092 ÷ 43,200 = 99.75%', 15, 'start', bold=True))
    chips = [(['(b) student edits his marks row', 'integrity broken'], LVS, LV), (['(c) PDF open to anyone with the link', 'confidentiality broken'], LVS, LV),
             (['(d) only staff publish, signed', 'authentication, non-repudiation'], NXS, NX)]
    for i, (lines, f, st) in enumerate(chips):
        o.append(boxt(12 + i * 236, 246, 228, 50, lines, f, st, 13, bold_first=False))
    return 310, ''.join(o)
FIG[1] = (f1, 'Over 30 days (43,200 minutes) the portal was down for 108 minutes, so its availability is 43,092 ÷ 43,200 = 99.75%. The other three events each touch one named goal.',
          'Thirty day cells with one thin red sliver, an enlarged day bar showing 108 of 1,440 minutes down, the availability formula, and three chips naming integrity, confidentiality, and authentication with non-repudiation.')


# ---- 1.2 four events, mapped to attack, service and mechanism ----
def f2():
    xs = [12, 188, 364, 540]
    w = 168
    o = [T(xs[i] + w / 2, 28, h, 14, bold=True) for i, h in enumerate(('event', 'attack class', 'service', 'mechanism'))]
    rows = [(['(a) packets copied,', 'body unreadable'], ['interception', 'passive'], ['confidentiality', 'held: encrypted'], ['encipherment,', 'traffic padding']),
            (['(b) ₹45,000 → ₹95,000', 'changed by ₹50,000'], ['modification', 'active'], ['data integrity'], ['MAC or', 'digital signature']),
            (['(c) server silent 3 h', '= 180 min = 10,800 s'], ['interruption', 'active'], ['availability'], ['redundancy,', 'rate limiting']),
            (['(d) sender denies', 'sending the file'], ['repudiation', 'not a message class'], ['non-repudiation'], ['signature with a', 'notarised time'])]
    for r, cells in enumerate(rows):
        y = 40 + r * 62
        passive = r == 0
        sty = [(PANEL, L2), (NXS, NX) if passive else (LVS, LV), (ACS, AC), (NXS, NX)]
        for i, (lines, (f, st)) in enumerate(zip(cells, sty)):
            o.append(boxt(xs[i], y, w, 50, lines, f, st, 13, bold_first=i > 0))
            if i: o.append(L(xs[i] - 7, y + 25, xs[i] - 1, y + 25, L2, 1.5))
    o.append(T(20, 306, 'Read it backwards in the exam: start from the mechanism and name the service it protects.', 14, 'start'))
    return 320, ''.join(o)
FIG[2] = (f2, 'Each event from the salary-file example in one row: what happened, the attack class, the service it attacks and the mechanism that meets it. The changed amount is ₹50,000 and the outage 10,800 seconds.',
          'A four-column grid of chips: event, attack class, service and mechanism, for packet copying, the changed amount, the 3-hour outage and the denied sending.')


# ---- 1.3 exposed servers and the risk arithmetic ----
def f3():
    o = [T(20, 30, '400 servers', 14, 'start', bold=True)]
    o.append(R(20, 42, 200, 200, NXS, NX, 2, 1))
    o.append(R(20, 42, 200, 50, LVS, LV, 2, 1.5))
    for i in range(1, 20):
        o.append(L(20 + i * 10, 42, 20 + i * 10, 242, 'var(--fig)', 1))
        o.append(L(20, 42 + i * 10, 220, 42 + i * 10, 'var(--fig)', 1))
    o.append(T(20, 264, '25% exposed: 0.25 × 400', 13, 'start', LV, True))
    o.append(T(20, 282, '= 100 servers', 13, 'start', LV, True))
    x0, s = 270, 30
    rows = [('Risk now: 0.20 × ₹50,00,000', 0, 10, LVS, LV, '₹10,00,000'), ('After the patch: 0.04 × ₹50,00,000', 0, 2, NXS, NX, '₹2,00,000'),
            ('Risk removed: ₹10,00,000 − ₹2,00,000', 2, 8, ACS, AC, '₹8,00,000'), ('Minus the patch cost', 2, 3, PANEL, L2, '− ₹3,00,000'),
            ('Net saving per year', 5, 5, NXS, NX, '₹5,00,000')]
    for r, (lab, a, v, f, st, val) in enumerate(rows):
        y = 30 + r * 62
        o.append(T(x0, y, lab, 13, 'start', bold=True))
        o.append(R(x0 + a * s, y + 8, v * s, 26, f, st, 4, 1.5, '5 3' if r == 3 else None))
        o.append(T(x0 + (a + v) * s + 8, y + 26, val, 14, 'start', st if st != L2 else INK, True))
    o.append(T(20, 346, 'The net saving is positive, so the patch project is funded on risk grounds alone.', 14, 'start'))
    return 360, ''.join(o)
FIG[3] = (f3, 'A quarter of the 400 servers (100) carry the bug. Risk = likelihood × impact: 0.20 × ₹50,00,000 = ₹10,00,000 a year, cut to ₹2,00,000 by the patch, so after its ₹3,00,000 cost the firm still saves ₹5,00,000 a year.',
          'A 20 by 20 grid of servers with the top 100 shaded; beside it, bars for the ₹10,00,000 risk, the ₹2,00,000 risk after patching, the ₹8,00,000 removed, the ₹3,00,000 patch cost and the ₹5,00,000 net saving.')


# ---- 1.4 a DDoS 500 times over capacity, and a port scan ----
def f4():
    o = [T(20, 26, 'Each square = 20,000 requests/s', 14, 'start', bold=True)]
    o.append(R(20, 40, 250, 200, LVS, LV, 2, 1))
    for i in range(1, 25): o.append(L(20 + i * 10, 40, 20 + i * 10, 240, 'var(--fig)', 1))
    for i in range(1, 20): o.append(L(20, 40 + i * 10, 270, 40 + i * 10, 'var(--fig)', 1))
    o.append(R(20, 40, 10, 10, NX, NX, 0, 0))
    o.append(L(26, 254, 26, 246, NX, 1.5))
    o.append(T(20, 268, 'green: what the server can serve', 13, 'start', NX, True))
    o.append(T(20, 286, 'all 500 squares: what arrives', 13, 'start', LV, True))
    x = 300
    lines = [('Offered load = 50,000 bots × 200 requests/s', False), ('= 10,000,000 requests/s', True), ('Capacity = 20,000 requests/s', False),
             ('Overload = 10,000,000 ÷ 20,000 = 500 times', True)]
    for i, (s, b) in enumerate(lines):
        o.append(T(x, 56 + i * 24, s, 14, 'start', LV if (b and i == 3) else INK, b))
    o.append(T(x, 172, 'Spoofed sources defeat per-IP limits: filter upstream', 13, 'start', MUT))
    o.append(T(x, 190, '(scrubbing, CDN, anycast) and use SYN cookies.', 13, 'start', MUT))
    o.append(T(x, 226, 'Port scan of the host', 14, 'start', bold=True))
    for i, (p, st) in enumerate((('22', 'open'), ('80', 'open'), ('443', 'open'), ('3306', 'filtered'))):
        op = st == 'open'
        o.append(boxt(x + i * 102, 236, 94, 42, [p, st], NXS if op else PANEL, NX if op else L2, 13, bold_first=True, dash=None if op else '5 3'))
    o.append(T(x, 300, 'filtered: no reply at all, so a firewall drops the probes', 13, 'start', MUT))
    return 314, ''.join(o)
FIG[4] = (f4, '50,000 bots at 200 requests per second offer 10,000,000 requests per second, 500 times the server\'s 20,000: one green square against five hundred. The scan shows SSH, HTTP and HTTPS answering and MySQL silently dropped by a firewall.',
          'A grid of 500 red squares with one green square for the server\'s capacity, the load arithmetic beside it, and four port chips: 22, 80 and 443 open and 3306 filtered.')


# ---- 1.5 a worm that doubles every 10 minutes ----
def f5():
    x0, x1, y0, y1 = 100, 560, 40, 300
    fx = lambda k: x0 + k * (x1 - x0) / 18
    fy = lambda k: y1 - k * (y1 - y0) / 18
    clock = lambda k: f'{9 + (k * 10) // 60:02d}:{(k * 10) % 60:02d}'
    labs = {0: '1', 4: '16', 8: '256', 12: '4,096', 16: '65,536'}
    o = [axes(x0, x1, y0, y1, [0, 3, 6, 9, 12, 15, 18], [0, 4, 8, 12, 16], fx, fy, 'time (one step = 10 minutes)', 'infected machines (each line = × 16)',
              xfmt=clock, yfmt=lambda k: labs[k])]
    th = 16.61
    o.append(L(x0, fy(th), x1, fy(th), LV, 1.5, '6 4'))
    o.append(Tb(x0 + 70, fy(th) - 2, '1,00,000 machines', 13, fill=LV, bold=True))
    o.append(P([(fx(k), fy(k)) for k in range(19)], AC, 2.5))
    for k in range(19):
        o.append(C(fx(k), fy(k), 4, AC))
    for k, lab in ((3, '09:30: 8'), (6, '10:00: 64')):
        o.append(C(fx(k), fy(k), 6, NX)); o.append(T(fx(k) + 10, fy(k) + 16, lab, 13, 'start', NX, True))
    for k, lab, ty in ((17, '11:50: 1,31,072', fy(17) - 14), (16, '11:40: 65,536', fy(16) + 30)):
        o.append(C(fx(k), fy(k), 6, LV))
        o.append(L(fx(k) + 7, fy(k), x1 + 12, ty - 4, LV, 1))
        o.append(T(x1 + 16, ty, lab, 13, 'start', LV, True))
    o.append(T(20, 370, 'Every step is a doubling, so on this scale the count climbs in a straight line: N = 2ᵏ after k steps.', 14, 'start'))
    o.append(T(20, 392, 'The worm needs no click; patching the one service it exploits stops the whole outbreak.', 14, 'start', bold=True))
    return 406, ''.join(o)
FIG[5] = (f5, 'Starting from 1 machine at 09:00 and doubling every 10 minutes, the worm infects 64 machines by 10:00 and crosses 1,00,000 between 11:40 (65,536) and 11:50 (1,31,072).',
          'Infected machines against time on a doubling scale: a straight line of points from 1 at 09:00 to 2,62,144 at 12:00, crossing a dashed 1,00,000 line between 11:40 and 11:50.')


# ---- 1.6 the phishing funnel before and after training and MFA ----
def f6():
    lanes = [(190, 'Before', [('10,000 mails', PANEL, L2), ('500 clicks', PANEL, L2), ('50 passwords typed', LVS, LV), ('50 accounts taken', LVS, LV),
                              ('loss ₹20,00,000', LVS, LV)], ['× 5% click', '× 10% type a password', 'no MFA: all work', '× ₹40,000 each']),
             (530, 'After training and MFA', [('10,000 mails', PANEL, L2), ('250 clicks', PANEL, L2), ('25 passwords typed', LVS, LV), ('0 accounts taken', NXS, NX),
                                              ('loss ₹0', NXS, NX)], ['× 2.5% click (halved)', '× 10% type a password', 'MFA refuses a password alone', '× ₹40,000 each'])]
    o = []
    for xc, title, chips, steps in lanes:
        o.append(T(xc, 26, title, 15, bold=True))
        for i, (lab, f, st) in enumerate(chips):
            y = 40 + i * 66
            o.append(boxt(xc - 110, y, 220, 38, [lab], f, st, 14, bold_first=True))
            if i < 4:
                o.append(L(xc, y + 40, xc, y + 63, L2, 1.8, arrow='m'))
                o.append(T(xc + 10, y + 56, steps[i], 13, 'start', MUT))
    o.append(T(360, 368, 'Training halves the clicks; MFA turns the remaining 25 stolen passwords into 0 taken accounts.', 14, bold=True))
    return 382, ''.join(o)
FIG[6] = (f6, 'Of 10,000 mails, 5% are clicked and 10% of those give a password: 50 accounts and ₹20,00,000 lost. Halving the clicks leaves 25 passwords, and multi-factor authentication refuses every password-only login, so the loss falls to ₹0.',
          'Two funnels of chips side by side: 10,000 mails, 500 clicks, 50 passwords, 50 accounts and ₹20,00,000 lost; and 10,000 mails, 250 clicks, 25 passwords, 0 accounts and ₹0 lost.')


# ---- 1.7 the botnet's numbers per hour ----
def f7():
    o = [boxt(20, 30, 150, 44, ['botmaster'], LVS, LV, 14, bold_first=True),
         boxt(260, 30, 170, 44, ['C2 server'], LVS, LV, 14, bold_first=True)]
    o.append(L(172, 52, 256, 52, LV, 2, arrow='l')); o.append(T(214, 44, 'command', 13, fill=MUT))
    bots = [20 + i * 86 for i in range(5)]
    for x in bots:
        o.append(boxt(x, 160, 76, 36, ['bot'], PANEL, AC, 13))
    o.append(T(bots[-1] + 90, 183, '… 20,000 bots', 14, 'start', bold=True))
    o.append(L(230, 158, 330, 80, L2, 2, '5 4', arrow='m'))
    o.append(Tb(470, 112, 'beacon every 60 s: 20,000 × 60 = 12,00,000 per hour', 13, fill=MUT, bold=True))
    o.append(boxt(470, 250, 230, 60, ['login page', '0.1% succeed: 1,000 per hour'], ACS, AC, 13, bold_first=True))
    o.append(L(300, 200, 466, 274, AC, 3, arrow='n'))
    o.append(Tb(200, 262, '50 logins/h each: 10,00,000 attempts per hour', 13, fill=AC, bold=True))
    o.append(T(20, 346, 'Blocking the C2 domain stops new commands but leaves every bot in place;', 14, 'start'))
    o.append(T(20, 368, 'rate limits and MFA at the login page take the 1,000 successes to 0.', 14, 'start', bold=True))
    return 382, ''.join(o)
FIG[7] = (f7, '20,000 bots each try 50 logins an hour, 10,00,000 attempts, of which 0.1% (1,000) succeed. Each bot also checks in with the C2 server every 60 seconds, 12,00,000 beacons an hour.',
          'A botmaster sending a command to a C2 server, a row of bots beaconing up to it with dashed arrows, and arrows from the bots to a login page where 1,000 logins an hour succeed.')


spec = make_spec(FIG)
