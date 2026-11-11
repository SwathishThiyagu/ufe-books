"""Claude's hand-drawn figures for c-cloud-u2 (Cloud Computing, unit 2: cloud infrastructure, web and multitenancy,
SOA and REST, elasticity, load balancing and HA, SLAs, virtual servers and billing), one per chapter, from each chapter's
worked example, plus the sentences in the chapter text that describe a figure (text_fixes)."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def hbar(x, y, w, h, fill, c, label=None, size=13, fc=INK, bold=False):
    o = R(x, y, w, h, fill, c, 4, 2)
    if label: o += T(x + w / 2, y + h / 2 + size * 0.36, label, size, fill=fc, bold=bold)
    return o


# ---- 2.1 Chennai to the Mumbai region: delay, then power ----
def f1():
    o = [T(40, 26, 'One way from a Chennai phone to the Mumbai region', 15, 'start', bold=True)]
    nodes = ['phone', 'local ISP', 'backbone', 'Mumbai region', 'server rack']
    xs = [70, 210, 350, 500, 650]
    for x, n in zip(xs, nodes):
        o.append(boxt(x - 56, 44, 112, 36, [n], PANEL, AC, 13))
    hops = [('access', '5 ms'), ('ISP hops', '2 ms'), ('fibre 1,200 km', '6 ms'), ('switching', '0.5 ms')]
    for (a, b), x1, x2 in zip(hops, xs, xs[1:]):
        o.append(L(x1 + 58, 62, x2 - 60, 62, AC, 2, arrow='n'))
        o.append(T((x1 + x2) / 2, 100, a, 13, fill=MUT)); o.append(T((x1 + x2) / 2, 118, b, 14, bold=True))
    s = 600 / 13.5
    x = 60
    parts = [(5, LVS, LV, '5'), (2, PANEL, L2, '2'), (6, ACS, AC, 'fibre 6'), (0.5, NXS, NX, '')]
    for ms, f, c, lab in parts:
        o.append(hbar(x, 140, ms * s, 30, f, c, lab, 13)); x += ms * s
    o.append(T(x + 8, 160, '0.5', 13, 'start'))
    o.append(T(60, 194, 'one way 5 + 2 + 6 + 0.5 = 13.5 ms;  round trip 2 × 13.5 = 27 ms', 14, 'start', bold=True))
    o.append(T(60, 214, 'fibre time = 1,200,000 m ÷ 2×10⁸ m/s = 6 ms, fixed by distance', 13, 'start', MUT))
    # power
    y = 262
    o.append(T(40, y - 12, 'The same data centre’s power bill', 15, 'start', bold=True))
    o.append(boxt(40, y, 140, 50, ['IT equipment', '1.5 MW'], ACS, AC, 14))
    o.append(L(182, y + 25, 236, y + 25, AC, 2, arrow='n')); o.append(T(209, y + 16, '× 1.4', 13, bold=True))
    o.append(boxt(240, y, 140, 50, ['whole facility', '2.1 MW'], LVS, LV, 14))
    o.append(L(382, y + 25, 446, y + 25, AC, 2, arrow='n')); o.append(T(414, y + 16, '× 730 h', 13, bold=True))
    o.append(boxt(450, y, 110, 50, ['1,533 MWh'], PANEL, L2, 14))
    o.append(L(562, y + 25, 596, y + 25, AC, 2, arrow='n')); o.append(T(579, y + 16, '× ₹8', 13, bold=True))
    o.append(boxt(600, y, 90, 50, ['₹1.23', 'crore'], NXS, NX, 14))
    o.append(T(40, y + 76, 'PUE 1.4 means every 1 MW of servers costs 1.4 MW at the meter; 1,533,000 kWh × ₹8 = ₹1,22,64,000.', 13, 'start', MUT))
    return y + 92, ''.join(o)
FIG[1] = (f1, 'The four hops add 5 + 2 + 6 + 0.5 = 13.5 ms one way, so the round trip is 27 ms. Below, 1.5 MW of IT at PUE 1.4 draws 2.1 MW, which over 730 hours costs about ₹1.23 crore.',
          'A chain from phone to local ISP, backbone, Mumbai region and server rack with each hop’s delay, a bar adding them to 13.5 ms, and a row of boxes turning 1.5 MW of IT power into a monthly energy bill.')


# ---- 2.2 one request, identity then tenant then data ----
def f2():
    o = []
    steps = [('browser', 'cookie sid'), ('web server', 'passes sid'), ('application', 'sid → tenant 42'), ('tenant database', 'WHERE tenant_id = 42')]
    xs = [40, 210, 380, 550]
    for (n, sub), x in zip(steps, xs):
        o.append(R(x, 30, 140, 58, PANEL, AC, 8))
        o.append(T(x + 70, 54, n, 14, bold=True)); o.append(T(x + 70, 75, sub, 13, fill=MUT))
    for x in xs[:-1]:
        o.append(L(x + 142, 59, x + 166, 59, AC, 2, arrow='n'))
    o.append(T(110, 112, '1 identity', 13, bold=True, fill=AC)); o.append(T(450, 112, '2 tenant', 13, bold=True, fill=AC)); o.append(T(620, 112, '3 data', 13, bold=True, fill=AC))
    # scan comparison
    o.append(T(40, 156, 'Rows the database reads for one tenant’s orders (1,000,000 rows, 500 tenants)', 15, 'start', bold=True))
    o.append(T(40, 190, 'no tenant filter', 14, 'start'))
    o.append(hbar(190, 172, 490, 28, LVS, LV, 'full scan: 1,000,000 rows', 13))
    o.append(T(40, 236, 'index (tenant_id, id)', 14, 'start'))
    o.append(hbar(190, 218, 490 / 500, 28, NXS, NX))
    o.append(T(198, 237, '1,000,000 ÷ 500 = 2,000 rows: 500 times fewer', 13, 'start', bold=True))
    for i in range(50):
        o.append(R(190 + i * 9.8, 266, 8.2, 12, NXS if i == 21 else 'var(--fig)', NX if i == 21 else L2, 2, 1))
    o.append(T(40, 276, 'the table', 13, 'start', MUT)); o.append(T(190, 298, 'one box = 10 tenants; the index jumps straight to tenant 42’s range', 13, 'start', MUT))
    return 314, ''.join(o)
FIG[2] = (f2, 'The request carries identity first (cookie sid), the application turns it into tenant 42, and only then does the query touch data. With an index on (tenant_id, id) it reads 2,000 rows instead of 1,000,000.',
          'Four boxes from browser to tenant database marked identity, tenant and data, above two bars: a full scan of 1,000,000 rows and a tiny indexed read of 2,000 rows.')


# ---- 2.3 idempotency key: three tries, one debit ----
def f3():
    cx, sx = 120, 560
    o = [boxt(cx - 60, 20, 120, 34, ['client'], PANEL, AC, 14), boxt(sx - 60, 20, 120, 34, ['payment server'], PANEL, AC, 14)]
    o.append(L(cx, 54, cx, 410, L2, 1.5, '4 4')); o.append(L(sx, 54, sx, 410, L2, 1.5, '4 4'))
    rows = [(84, 'POST /payments, key K', 'debit ₹500, store reply', AC, True, '× reply lost'),
            (184, 'retry 1, key K', 'key seen: replay', NX, False, None),
            (250, 'retry 2, key K', 'key seen: replay', NX, False, None),
            (336, 'retry at 25 h, key K', 'key expired (kept 24 h): debit ₹500', LV, True, None)]
    for y, req, act, c, debit, lost in rows:
        o.append(L(cx, y, sx - 4, y + 14, AC, 2, arrow='n'))
        o.append(Tb((cx + sx) / 2 - 20, y - 2, req, 13))
        o.append(R(sx + 8, y + 2, 152 if not debit or 'expired' not in act else 152, 24, LVS if debit and c == LV else (ACS if debit else NXS), c, 5, 1.5))
        o.append(T(sx + 84, y + 19, '₹500 debit' if debit else 'no debit', 13, bold=True))
        o.append(T(sx - 10, y + 40, act, 13, 'end', MUT))
        if lost:
            o.append(L(sx - 4, y + 52, cx + 150, y + 62, L2, 2, '6 4'))
            o.append(T(cx + 140, y + 66, lost, 13, 'end', LV, True))
    o.append(L(40, 308, 690, 308, L2, 1, '2 4')); o.append(T(46, 302, '24 hours later the key is forgotten', 13, 'start', MUT))
    o.append(T(40, 440, 'Ignore the key: 3 × ₹500 = ₹1,500.  Honour it: ₹500 and 2 replays.  After expiry: at most ₹1,000.', 14, 'start', bold=True))
    return 456, ''.join(o)
FIG[3] = (f3, 'Three tries with the same key K debit ₹500 once and get two replays; a retry at 25 hours finds the 24-hour key gone and debits again, so the total can reach ₹1,000, against ₹1,500 with no key at all.',
          'A sequence diagram between client and payment server: the first POST debits ₹500 and its reply is lost, two retries with key K get replays, and a retry after 25 hours debits ₹500 again.')


# ---- 2.4 auto-scaling: 2 servers all day, 8 more for the peak ----
def f4():
    X0, X1, Y0, Y1 = 80, 520, 50, 300
    fx = lambda h: X0 + h / 24 * (X1 - X0)
    fy = lambda n: Y1 - n / 11 * (Y1 - Y0)
    o = [axes(X0, X1, Y0, Y1, [0, 6, 12, 18, 24], [0, 2, 4, 6, 8, 10], fx, fy, 'hour of the day', 'servers running')]
    o.append(R(fx(0), fy(10), fx(24) - fx(0), fy(0) - fy(10), 'none', LV, 2, 2, '7 5'))
    o.append(R(fx(0), fy(2), fx(24) - fx(0), fy(0) - fy(2), ACS, AC, 2))
    o.append(R(fx(12), fy(10), fx(16) - fx(12), fy(2) - fy(10), NXS, NX, 2))
    o.append(T(fx(6), fy(1) + 5, '2 × 24 h = 48 server-hours', 13, bold=True))
    o.append(T(fx(14), fy(6) - 8, '8 × 4 h', 13, bold=True)); o.append(T(fx(14), fy(6) + 10, '= 32', 13, bold=True))
    o.append(Tb(fx(6), fy(10) - 8, 'fixed: 10 servers all day', 13, fill=LV, bold=True))
    o.append(T(fx(14), fy(10) - 22, 'peak 600 req/s', 13, bold=True))
    x = 548
    o.append(T(x, 80, 'At ₹9 per server-hour', 14, 'start', bold=True))
    o.append(T(x, 110, 'base  2 × 24 × ₹9 = ₹432', 13, 'start'))
    o.append(T(x, 132, 'peak  8 × 4 × ₹9 = ₹288', 13, 'start'))
    o.append(L(x, 144, 712, 144, INK, 1))
    o.append(T(x, 166, 'elastic ₹720', 15, 'start', AC, True))
    o.append(T(x, 196, 'fixed 10 × 24 × ₹9', 13, 'start'))
    o.append(T(x, 216, '= ₹2,160', 15, 'start', LV, True))
    o.append(T(x, 252, 'saving ₹1,440', 15, 'start', bold=True))
    o.append(T(80, 362, '600 req/s ÷ (100 × 0.60) per server = 10 servers at the peak; the floor is 2.', 14, 'start'))
    return 380, ''.join(o)
FIG[4] = (f4, 'At 60% target, the 600 requests per second peak needs 10 servers; the elastic group runs 2 all day and adds 8 for 4 hours, ₹720 in all, against ₹2,160 for 10 servers kept all day.',
          'A chart of servers running over 24 hours: a low band of 2 servers all day and a block of 8 more during a 4-hour peak, inside a dashed outline of 10 servers all day.')


# ---- 2.5 availability: parallel servers, then the load balancer in series ----
def f5():
    o = [T(40, 26, 'The service works if the load balancer works and at least one server works', 15, 'start', bold=True)]
    o.append(boxt(30, 96, 90, 46, ['users'], PANEL, L2, 14))
    o.append(L(122, 119, 168, 119, AC, 2, arrow='n'))
    o.append(boxt(172, 90, 140, 58, ['load balancer', 'A = 0.999'], LVS, LV, 14))
    o.append(L(314, 119, 360, 119, AC, 2))
    for i, y in enumerate([70, 119, 168]):
        o.append(L(360, 119, 360, y, AC, 2)); o.append(L(360, y, 392, y, AC, 2, arrow='n'))
        o.append(boxt(396, y - 20, 150, 40, [f'server {i + 1}  A = 0.99'], ACS, AC, 13))
    o.append(R(348, 42, 214, 152, 'none', NX, 10, 1.5, '6 4')); o.append(T(570, 124, 'parallel', 13, 'start', NX, True)); o.append(T(570, 142, 'group', 13, 'start', NX, True))
    y = 232
    o.append(T(40, y, 'Server group (parallel)', 14, 'start', bold=True))
    o.append(T(40, y + 22, 'all three down: 0.01 × 0.01 × 0.01 = 0.000001', 13, 'start'))
    o.append(T(40, y + 42, 'group up: 1 − 0.000001 = 0.999999', 13, 'start', NX, True))
    o.append(T(390, y, 'Whole service (series)', 14, 'start', bold=True))
    o.append(T(390, y + 22, '0.999 × 0.999999 = 0.998999001', 13, 'start'))
    o.append(T(390, y + 42, 'down (1 − A) × 8,760 h ≈ 8.77 h a year', 13, 'start', LV, True))
    o.append(T(40, y + 84, 'The servers now fail almost never; the single load balancer is the weak link.', 14, 'start', bold=True))
    return y + 100, ''.join(o)
FIG[5] = (f5, 'Three servers at 0.99 in parallel are all down only 0.000001 of the time, so the group reaches 0.999999; the one load balancer at 0.999 in series caps the service at 0.998999001, about 8.77 hours down a year.',
          'A reliability diagram: users, one load balancer at 0.999, then three servers at 0.99 side by side in a dashed group, with the parallel and series calculations below.')


# ---- 2.6 SLO, SLA and the actual downtime on one minute scale ----
def f6():
    X0, X1 = 60, 680
    fx = lambda m: X0 + m / 70 * (X1 - X0)
    o = [T(40, 26, 'Downtime in a 43,200-minute month', 15, 'start', bold=True)]
    yb = 124
    o.append(R(fx(0), yb, fx(21.6) - fx(0), 30, NXS, NX, 4))
    o.append(R(fx(21.6), yb, fx(43.2) - fx(21.6), 30, ACS, AC, 4))
    o.append(R(fx(43.2), yb, fx(70) - fx(43.2), 30, LVS, LV, 4))
    o.append(T((fx(0) + fx(21.6)) / 2, yb + 20, 'SLO met', 13, bold=True))
    o.append(T((fx(30) + fx(43.2)) / 2 + 4, yb + 20, 'SLA met', 13, bold=True))
    o.append(T((fx(43.2) + fx(70)) / 2, yb + 20, 'SLA breached: credits', 13, bold=True))
    o.append(xaxis(X0, X1, yb + 44, [0, 10, 20, 30, 40, 50, 60, 70], fx, 'minutes of downtime'))
    for m, lab, y, c, anc in [(21.6, 'SLO 99.95%: 21.6 min', 104, NX, 'end'), (43.2, 'SLA 99.9%: 43.2 min', 104, AC, 'start'), (64.8, 'two in series: 64.8 min', 80, MUT, 'end')]:
        o.append(L(fx(m), y + 4, fx(m), yb + 30, c, 1.5, '4 4'))
        o.append(T(fx(m) + (4 if anc == 'start' else -4), y, lab, 13, anc, c, True))
    o.append(L(fx(30), 64, fx(30), yb + 34, INK, 3))
    o.append(T(fx(30), 56, 'actual 30.0 min', 14, bold=True))
    o.append(T(40, 236, 'SLO: 43,200 × 0.0005 = 21.6 min.  SLA: 43,200 × 0.001 = 43.2 min.', 13, 'start'))
    o.append(T(40, 258, '30 min breaks the SLO (freeze risky releases) but meets the SLA, so no credits are due.', 14, 'start', bold=True))
    o.append(T(40, 280, 'Two services at 99.9% and 99.95% in series: 0.999 × 0.9995 = 0.9985005, allowing 64.8 min.', 13, 'start'))
    return 296, ''.join(o)
FIG[6] = (f6, 'On one minute scale: the SLO allows 21.6 minutes and the SLA 43.2; the actual 30 minutes breaks the SLO but meets the SLA, so the error budget is spent and no credits are due. Two services in series allow 64.8 minutes.',
          'A horizontal scale of downtime minutes split into three zones at 21.6 and 43.2 minutes, with the actual 30 minutes marked in the middle zone and the two-service allowance of 64.8 minutes marked further right.')


# ---- 2.7 the usage monitor and the 10-hour bill ----
def f7():
    o = [T(40, 26, 'Usage monitor: one sample every 5 minutes for 10 hours', 15, 'start', bold=True)]
    X0, X1 = 60, 660
    for i in range(121):
        x = X0 + i * (X1 - X0) / 120
        o.append(L(x, 46, x, 58 if i % 12 else 66, AC if i % 12 else INK, 1.2))
    for h in range(0, 11, 2):
        o.append(T(X0 + h * 60, 84, f'{h} h', 13, fill=MUT))
    o.append(T(X1, 104, '10 h × 60 ÷ 5 = 120 samples', 13, 'end', bold=True))
    rows = [('CPU', '4 vCPU × 10 h = 40 vCPU-hours × ₹6', 240, '₹240'),
            ('RAM', '16 GB × 10 h = 160 GB-hours × ₹1.5', 240, '₹240'),
            ('disk', '200 GB × 10/730 month = 2.74 GB-month × ₹0.8', 2.19, '₹2.19')]
    y = 126
    s = 240 / 240
    for name, how, v, lab in rows:
        o.append(T(40, y + 18, name, 14, 'start', bold=True))
        o.append(T(100, y + 18, how, 13, 'start'))
        o.append(hbar(470, y + 2, max(v * s * 0.8, 2), 24, ACS if v > 10 else LVS, AC if v > 10 else LV))
        o.append(T(470 + max(v * 0.8, 2) + 8, y + 19, lab, 14, 'start', bold=True))
        y += 42
    o.append(L(40, y + 2, 690, y + 2, INK, 1.5))
    o.append(T(40, y + 26, 'total 240 + 240 + 2.19 = ₹482.19 for the run', 15, 'start', bold=True))
    o.append(T(40, y + 50, 'Disk is billed per GB-month, so 10 hours is only 10/730 of a month: tiny next to CPU and RAM.', 13, 'start', MUT))
    return y + 66, ''.join(o)
FIG[7] = (f7, 'The monitor takes 120 samples in 10 hours. Each resource is priced in its own unit: CPU and RAM come to ₹240 each, the disk only ₹2.19 because 10 hours is a small part of a month, ₹482.19 in all.',
          'A row of 120 sample ticks over 10 hours above three bill lines, CPU ₹240, RAM ₹240 and disk ₹2.19, adding to ₹482.19.')


spec = make_spec(FIG)


def text_fixes(k):
    return {
        2: [('Figure 1 follows a request.', 'Figure 2.2.1 follows this request from left to right.')],
    }.get(k, [])
