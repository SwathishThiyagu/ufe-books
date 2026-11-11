"""Claude's hand-drawn figures for c-cloud-u1 (Cloud Computing, unit 1: foundations), one per chapter, from each
chapter's worked example, plus the sentences in the chapter text that describe a figure (text_fixes)."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def hbar(x, y, w, h, fill, c, label=None, size=13, fc=INK, bold=False):
    o = R(x, y, w, h, fill, c, 4, 2)
    if label: o += T(x + w / 2, y + h / 2 + size * 0.36, label, size, fill=fc, bold=bold)
    return o


# ---- 1.1 buy 300 servers or rent by the hour ----
def f1():
    o = [T(40, 26, 'One month of demand: 25 working days', 15, 'start', bold=True)]
    x0, dw, base = 40, 25.6, 150
    for d in range(25):
        peak = d < 5
        h = 90 if peak else 90 * 20 / 300
        o.append(R(x0 + d * dw, base - h, dw - 3, h, ACS, AC, 2, 1.5))
    o.append(T(x0 + 2.5 * dw, base - 98, '300 servers × 5 days', 13, bold=True))
    o.append(T(x0 + 15 * dw, base - 18, '20 servers × 20 days', 13, bold=True))
    o.append(T(x0 + 12.5 * dw, base + 22, 'rent pays 36,000 + 9,600 = 45,600 server-hours a month × ₹30 = ₹13,68,000', 13, fill=MUT))
    # 12-month cost lines
    X0, X1, Y0, Y1 = 90, 520, 220, 440
    fx = lambda m: X0 + m / 12 * (X1 - X0)
    fy = lambda v: Y1 - v / 300 * (Y1 - Y0)
    o.append(axes(X0, X1, Y0, Y1, [0, 3, 6, 9, 12], [0, 100, 200, 300], fx, fy, 'month', 'total cost (₹ lakh)'))
    o.append(P([(fx(0), fy(240)), (fx(12), fy(276))], LV, 3))
    o.append(P([(fx(0), fy(0)), (fx(12), fy(164.16))], AC, 3))
    o.append(C(fx(0), fy(240), 5, LV)); o.append(C(fx(12), fy(276), 5, LV)); o.append(C(fx(12), fy(164.16), 5, AC))
    o.append(Tb(fx(0) + 12, fy(240) + 22, 'buy: ₹2,40,00,000 on day one', 13, 'start'))
    o.append(T(fx(12) + 12, fy(276) + 5, 'buy ₹2,76,00,000', 14, 'start', LV, True))
    o.append(T(fx(12) + 12, fy(164.16) + 5, 'rent ₹1,64,16,000', 14, 'start', AC, True))
    o.append(Tb(fx(5), fy(68.4) + 26, 'rent: ₹13,68,000 a month', 13, 'start'))
    bx = fx(12) - 14
    o.append(L(bx, fy(272), bx, fy(168), INK, 1.5))
    o.append(L(bx - 6, fy(272), bx + 6, fy(272), INK, 1.5)); o.append(L(bx - 6, fy(168), bx + 6, fy(168), INK, 1.5))
    o.append(T(bx - 10, fy(220) - 4, 'saving', 13, 'end', bold=True))
    o.append(T(bx - 10, fy(220) + 14, '₹1,11,84,000', 13, 'end', bold=True))
    return 490, ''.join(o)
FIG[1] = (f1, 'Top: in a month, 300 servers are needed on only 5 of the 25 working days, and renting pays just for those hours. Bottom: over 12 months buying reaches ₹2,76,00,000 and renting ₹1,64,16,000, a saving of ₹1,11,84,000.',
          'A strip of 25 day bars, five tall and twenty short, above a line chart where the buying line starts high and the renting line starts at zero and stays below it for twelve months.')


# ---- 1.2 Amdahl's law with p = 0.8 ----
def f2():
    cases = [(1, 0.8, '1'), (4, 0.2, '4'), (16, 0.05, '16'), (1000, 0.0008, '1000')]
    X0, Y0, Y1 = 110, 84, 340
    fy = lambda t: Y1 - t * (Y1 - Y0)
    o = [L(X0, Y1, 690, Y1, L2, 1.5), L(X0, Y0, X0, Y1, L2, 1.5)]
    for t in (0, 0.2, 0.4, 0.6, 0.8, 1.0):
        o += [L(X0 - 5, fy(t), X0, fy(t), L2, 1.5), T(X0 - 9, fy(t) + 4.5, f'{t:.1f}', 13, 'end', MUT)]
    o.append(T(X0, 30, 'run time (1.0 = one processor)', 14, 'start', MUT))
    bw, gap = 92, 54
    for i, (n, par, lab) in enumerate(cases):
        x = X0 + 40 + i * (bw + gap)
        o.append(R(x, fy(0.2), bw, fy(0) - fy(0.2), NXS, NX, 3))
        if par > 0.01:
            o.append(R(x, fy(0.2 + par), bw, fy(0.2) - fy(0.2 + par), ACS, AC, 3))
        else:
            o.append(L(x, fy(0.2) - 1, x + bw, fy(0.2) - 1, AC, 3))
        tot = 0.2 + par
        S = 1 / tot
        o.append(T(x + bw / 2, fy(tot) - 12, {1: 'S = 1×', 4: 'S = 2.5×', 16: 'S = 4.0×', 1000: 'S ≈ 4.98×'}[n], 14, bold=True))
        o.append(T(x + bw / 2, Y1 + 22, f'n = {lab}', 14, bold=True))
        o.append(T(x + bw / 2, fy(0.1) + 5, '0.2', 13))
        if par >= 0.05:
            o.append(T(x + bw / 2, fy(0.2 + par / 2) + 5, f'{par:g}', 13))
    o.append(L(X0, fy(0.2), 690, fy(0.2), NX, 2, '7 5'))
    o += [R(130, 382, 18, 14, NXS, NX, 3), T(156, 394, 'serial part 1 − p = 0.2: never shrinks', 14, 'start')]
    o += [R(130, 406, 18, 14, ACS, AC, 3), T(156, 418, 'parallel part p/n = 0.8/n: shrinks as n grows', 14, 'start')]
    o.append(T(130, 448, 'Run time can never fall below 0.2, so S = 1/((1 − p) + p/n) can never pass 1/0.2 = 5×.', 14, 'start', bold=True))
    return 466, ''.join(o)
FIG[2] = (f2, 'Run time for p = 0.8 on 1, 4, 16 and 1000 processors: the parallel part 0.8/n shrinks, but the serial 0.2 stays, so the speedup goes 2.5×, 4.0×, about 4.98× and can never pass 5×.',
          'Four stacked bars of run time: a fixed bottom block of 0.2 and a top block that shrinks from 0.8 to almost nothing as the processor count grows from 1 to 1000.')


# ---- 1.3 scoring a campus server against the five characteristics ----
def f3():
    rows = [('On-demand self-service', 'accounts made by emailing a person', 0),
            ('Broad network access', 'campus Wi-Fi only', 0),
            ('Resource pooling', 'one shared server, no shifting pool', 0.5),
            ('Rapid elasticity', 'fixed capacity, cannot grow', 0),
            ('Measured service', 'flat ₹500 a year, nothing metered', 0)]
    o = [T(40, 28, 'Campus login server: one credit per characteristic', 15, 'start', bold=True)]
    y = 50
    for name, why, c in rows:
        o.append(R(40, y, 640, 50, PANEL, L2, 8, 1.5))
        o.append(T(56, y + 22, name, 14, 'start', bold=True))
        o.append(T(56, y + 40, why, 13, 'start', MUT))
        bx = 470
        o.append(R(bx, y + 15, 120, 20, 'var(--fig)', L2, 4, 1.5))
        if c: o.append(R(bx, y + 15, 120 * c, 20, ACS, AC, 4, 2))
        o.append(T(bx + 140, y + 30, f'{c:g}', 16, 'start', AC if c else LV, True))
        y += 58
    o.append(L(40, y + 4, 680, y + 4, INK, 1.5))
    o.append(T(56, y + 32, 'Total 0 + 0 + 0.5 + 0 + 0 = 0.5 out of 5 = 10 percent', 15, 'start', bold=True))
    o.append(R(470, y + 14, 210, 30, LVS, LV, 8))
    o.append(T(575, y + 34, 'verdict: not a cloud', 15, bold=True))
    return y + 60, ''.join(o)
FIG[3] = (f3, 'The campus server scored on the five characteristics: only resource pooling earns a half credit, so it gets 0.5 out of 5 (10 percent) and is a hosted facility, not a cloud.',
          'Five rows, one per essential characteristic, each with its evidence and a credit bar; only resource pooling has a half-filled bar, and the total row reads 0.5 out of 5, not a cloud.')


# ---- 1.4 the bill is mostly downloads ----
def f4():
    s = 520 / 41984
    o = [T(40, 28, 'Monthly bill of the photo startup', 15, 'start', bold=True)]
    def row(y, title, dl, dltxt, tot):
        r = [T(40, y - 10, title, 14, 'start', bold=True)]
        r.append(hbar(40, y, 2048 * s, 40, LVS, LV))
        r.append(hbar(40 + 2048 * s, y, dl * s, 40, ACS, AC, dltxt, 14))
        r.append(T(40 + (2048 + dl) * s + 10, y + 26, tot, 15, 'start', bold=True))
        return ''.join(r)
    o.append(row(80, '3 TB downloads', 19968, 'downloads ₹19,968 (90.7%)', '₹22,016'))
    o.append(row(200, '6 TB downloads: the video goes viral', 39936, 'downloads ₹39,936', '₹41,984'))
    o.append(T(40, 146, 'storage stays ₹2,048 (1 TB = 1,024 GB × ₹2)', 13, 'start', LV, True))
    o += [R(40, 270, 18, 14, LVS, LV, 3), T(66, 282, 'storage: fixed while the data stays the same', 14, 'start')]
    o += [R(40, 294, 18, 14, ACS, AC, 3), T(66, 306, 'downloads: 3,072 GB × ₹6.50, grows with every viewer', 14, 'start')]
    o.append(T(40, 338, 'Double the downloads and the bill nearly doubles: the risk sits in the line you do not control.', 14, 'start'))
    return 356, ''.join(o)
FIG[4] = (f4, 'Storage is a small fixed ₹2,048; downloads are 90.7% of the ₹22,016 bill. When downloads double to 6 TB the bill becomes ₹41,984 while storage stays the same.',
          'Two stacked bars: a small storage block and a long download block making ₹22,016, then the same small storage block with a download block twice as long making ₹41,984.')


# ---- 1.5 the student portal on the four-layer stack ----
def f5():
    o = []
    layers = [('Application', ['student portal (opened in a browser)']),
              ('Platform', ['managed database 200 GB']),
              ('Virtualisation', ['4 VMs × (4 vCPU, 8 GB)', 'load balancer', 'object store 500 GB']),
              ('Physical', ['provider’s servers, disks and switches'])]
    x0, w, y, h = 40, 482, 40, 74
    fills = [ACS, LVS, ACS, PANEL]
    for i, (name, items) in enumerate(layers):
        yy = y + i * (h + 8)
        o.append(R(x0, yy, w, h, fills[i], AC if i < 3 else L2, 8))
        o.append(T(x0 + 14, yy + 24, name + ' layer', 14, 'start', bold=True))
        bx = x0 + 14
        bws = [len(s) * 7.0 + 18 for s in items]
        for s, bw in zip(items, bws):
            o.append(R(bx, yy + 34, bw, 28, 'var(--fig)', L2, 6, 1.5))
            o.append(T(bx + bw / 2, yy + 53, s, 13))
            bx += bw + 8
    # vertical bands
    for j, b in enumerate(['security', 'management', 'governance']):
        bx = 540 + j * 54
        o.append(R(bx, 30, 44, 4 * h + 3 * 8 + 20, NXS, NX, 8))
        o.append(f'<text x="{bx + 27:.1f}" y="{40 + 2 * h + 12:.1f}" font-size="14" text-anchor="middle" transform="rotate(-90 {bx + 27:.1f} {40 + 2 * h + 12:.1f})" style="fill:{INK}" font-weight="700">{b}</text>')
    yb = 40 + 4 * h + 3 * 8 + 32
    o.append(T(40, yb, 'Totals: 7 items, 4 × 4 = 16 vCPU, 4 × 8 = 32 GB RAM, 200 + 500 = 700 GB storage.', 14, 'start', bold=True))
    o.append(T(40, yb + 22, 'The three bands run through every layer, so they apply to all 7 items.', 14, 'start'))
    return yb + 38, ''.join(o)
FIG[5] = (f5, 'The portal design on the four layers: the VMs, load balancer and object store at the virtualisation layer, the database at the platform layer, the portal at the top; security, management and governance run through all of them.',
          'Four stacked layer boxes, physical at the bottom and application at the top, with the portal items placed in them, and three vertical bands for security, management and governance running beside the whole stack.')


# ---- 1.6 rented email (SaaS) against a self-run mail server ----
def f6():
    s = 430 / 57600
    o = [T(40, 28, 'Email for 300 students: cost for one year', 15, 'start', bold=True)]
    o.append(T(40, 70, 'A: rented (SaaS)', 14, 'start', bold=True))
    o.append(hbar(190, 50, 36000 * s, 34, ACS, AC, '300 × ₹120 = ₹36,000', 13))
    o.append(T(40, 136, 'B: own mail server', 14, 'start', bold=True))
    o.append(hbar(190, 116, 28800 * s, 34, LVS, LV, 'VM 12 × ₹2,400 = ₹28,800', 13))
    o.append(hbar(190 + 28800 * s, 116, 28800 * s, 34, NXS, NX, 'admin 48 h × ₹600 = ₹28,800', 13))
    o.append(T(190 + 57600 * s + 8, 138, '₹57,600', 14, 'start', bold=True))
    xa, xb = 190 + 36000 * s, 190 + 57600 * s
    o.append(L(xa, 88, xa, 114, INK, 1.2, '4 4')); o.append(L(xa, 152, xa, 176, INK, 1.2, '4 4')); o.append(L(xb, 154, xb, 176, INK, 1.2, '4 4'))
    o.append(L(xa, 172, xb, 172, INK, 2)); o.append(L(xa, 166, xa, 178, INK, 2)); o.append(L(xb, 166, xb, 178, INK, 2))
    o.append(T((xa + xb) / 2, 196, 'SaaS wins by ₹21,600', 14, bold=True))
    o.append(T(40, 236, 'The administrator’s hours cost as much as the machine: the hidden half of running it yourself.', 14, 'start'))
    return 254, ''.join(o)
FIG[6] = (f6, 'The rented mail service costs ₹36,000 a year; running your own server costs ₹28,800 for the VM plus ₹28,800 for 48 administrator hours, ₹57,600 in all, so SaaS wins by ₹21,600.',
          'Two horizontal bars: one for the rented service at ₹36,000 and a longer one split into two equal halves, VM and administrator time, totalling ₹57,600, with the ₹21,600 gap marked.')


# ---- 1.7 hybrid cloud bursting for the health camp ----
def f7():
    o = [T(40, 28, 'Health camp peak: 2,000 requests per second', 15, 'start', bold=True)]
    X0, Y0, Y1 = 100, 60, 330
    fy = lambda r: Y1 - r / 2000 * (Y1 - Y0)
    o.append(L(X0, Y0, X0, Y1, L2, 1.5)); o.append(L(X0, Y1, 330, Y1, L2, 1.5))
    for r in (0, 500, 1000, 1500, 2000):
        o += [L(X0 - 5, fy(r), X0, fy(r), L2, 1.5), T(X0 - 9, fy(r) + 4.5, f'{r:,}', 13, 'end', MUT)]
    bx, bw = 150, 120
    o.append(R(bx, fy(300), bw, fy(0) - fy(300), NXS, NX, 3))
    o.append(T(bx + bw / 2, fy(150) + 5, 'private 300', 13, bold=True))
    sh = (fy(300) - fy(2000)) / 10
    for i in range(10):
        o.append(R(bx, fy(300) - (i + 1) * sh, bw, sh, ACS, AC, 2, 1.5))
    o.append(Tb(bx + bw / 2, fy(1150) + 5, '10 rented × 170', 13, bold=True))
    o.append(T(bx + bw / 2, fy(2000) - 10, 'gap 1,700 burst out', 13, bold=True))
    o.append(T(215, Y1 + 22, 'during the 3-day camp', 13, fill=MUT))
    # costs
    s = 330 / 800000
    o.append(T(370, 80, 'Cost of covering the gap', 14, 'start', bold=True))
    o.append(T(370, 112, 'buy 10 servers', 13, 'start'))
    o.append(hbar(370, 118, 800000 * s, 28, LVS, LV)); o.append(T(370 + 800000 * s - 8, 137, '₹8,00,000', 14, 'end', bold=True))
    o.append(T(370, 176, 'burst once: 10 × 72 h × ₹30', 13, 'start'))
    o.append(hbar(370, 182, 21600 * s, 28, ACS, AC)); o.append(T(370 + 21600 * s + 8, 201, '₹21,600', 14, 'start', bold=True))
    o.append(T(370, 240, 'burst once a year for 3 years', 13, 'start'))
    o.append(hbar(370, 246, 64800 * s, 28, ACS, AC)); o.append(T(370 + 64800 * s + 8, 265, '₹64,800', 14, 'start', bold=True))
    o.append(T(370, 310, 'saving on one camp: ₹7,78,400', 14, 'start', bold=True))
    return 360, ''.join(o)
FIG[7] = (f7, 'The private core carries 300 of the 2,000 requests per second; 10 rented servers carry the other 1,700 for 72 hours at ₹21,600, against ₹8,00,000 to buy them.',
          'A tall bar for 2,000 requests per second split into a private block of 300 and ten rented blocks of 170, beside three cost bars: buying at ₹8,00,000 and bursting at ₹21,600 once or ₹64,800 over three years.')


# ---- 1.8 the meter builds the bill ----
def f8():
    o = []
    def receipt(x, title, comp, comptxt, tot, fill, c):
        r = [R(x, 20, 300, 250, fill, c, 10)]
        r.append(T(x + 150, 48, title, 15, bold=True))
        r.append(L(x + 16, 60, x + 284, 60, c, 1.5))
        lines = [('compute', comptxt, comp), ('storage', '500 GB × ₹2', '₹1,000'), ('requests', '20 million × ₹0.5', '₹10')]
        y = 92
        for a, b, v in lines:
            r.append(T(x + 18, y, a, 14, 'start', bold=True)); r.append(T(x + 18, y + 18, b, 13, 'start', MUT))
            r.append(T(x + 282, y + 8, v, 15, 'end', bold=True)); y += 50
        r.append(L(x + 16, y - 8, x + 284, y - 8, INK, 1.5))
        r.append(T(x + 18, y + 18, 'month', 15, 'start', bold=True)); r.append(T(x + 282, y + 18, tot, 17, 'end', bold=True))
        return ''.join(r)
    o.append(receipt(40, 'On-demand', '₹17,280', '2,880 VM-hours × ₹6', '₹18,290', PANEL, L2))
    o.append(receipt(380, 'One-year reserved', '₹10,368', '₹17,280 × 0.60', '₹11,378', ACS, AC))
    o.append(L(342, 145, 376, 145, AC, 2.5, arrow='n'))
    o.append(T(359, 134, '−40%', 13, fill=AC, bold=True))
    o.append(T(380, 300, 'Only compute changes; storage and requests are the same.', 14, 'middle'))
    o.append(T(380, 324, 'Saving ₹6,912 a month, ₹6,912 × 12 = ₹82,944 a year.', 15, 'middle', bold=True))
    return 342, ''.join(o)
FIG[8] = (f8, 'The meter turns one month of use into three bill lines. A one-year contract cuts only the compute line by 40%, so ₹18,290 becomes ₹11,378, a saving of ₹6,912 a month.',
          'Two bills side by side, on-demand and reserved, each with compute, storage and requests lines; compute falls from ₹17,280 to ₹10,368 and the total from ₹18,290 to ₹11,378.')


# ---- 1.9 edge placement for toll cameras ----
def f9():
    X0, X1 = 150, 650
    fx = lambda ms: X0 + ms / 100 * (X1 - X0)
    o = [T(40, 26, 'Answer time per frame against the 50 ms limit', 15, 'start', bold=True)]
    rows = [('on camera', [(90, ACS, AC, '')], '90 ms  fails'),
            ('cloud region', [(60, PANEL, L2, ''), (20, ACS, AC, '20')], '80 ms  fails'),
            ('edge node', [(5, PANEL, L2, ''), (20, ACS, AC, 'compute 20')], '25 ms  passes')]
    y = 50
    for name, parts, verdict in rows:
        o.append(T(X0 - 12, y + 23, name, 14, 'end', bold=True))
        t = 0
        for ms, f, c, lab in parts:
            o.append(hbar(fx(t), y, fx(ms) - fx(0), 34, f, c, lab, 13)); t += ms
        o.append(T(fx(t) + 8, y + 23, verdict, 14, 'start', LV if 'fails' in verdict else NX, True))
        y += 50
    o.append(L(fx(50), 40, fx(50), y - 4, INK, 2, '6 4'))
    o.append(T(fx(70), 50 + 23, 'compute 90', 13)); o.append(T(fx(28), 100 + 23, 'network 60', 13))
    o.append(Tb(fx(50), y + 12, '50 ms limit', 13, bold=True))
    o.append(T(X0, y - 1, '↑ 5 ms network', 13, 'start', MUT))
    o.append(xaxis(X0, X1, y + 40, [0, 25, 50, 75, 100], fx, 'milliseconds'))
    # backhaul
    yb = y + 110
    o.append(T(40, yb, 'Backhaul from 1,000 cameras', 15, 'start', bold=True))
    o.append(T(40, yb + 30, 'every frame to the cloud', 14, 'start'))
    o.append(hbar(260, yb + 12, 400, 28, LVS, LV, '2,000 frames/s × 2 MB = 32 Gbit/s', 13))
    o.append(T(40, yb + 72, 'only alerts leave the edge', 14, 'start'))
    o.append(hbar(260, yb + 54, 3, 28, NXS, NX))
    o.append(T(272, yb + 73, '100 alerts/s × 50 KB = 40 Mbit/s, 800 times less', 13, 'start', bold=True))
    return yb + 96, ''.join(o)
FIG[9] = (f9, 'Only the edge node answers inside 50 ms (5 + 20 = 25 ms); the camera takes 90 ms and the cloud 60 + 20 = 80 ms. Sending only alerts cuts the backhaul from 32 Gbit/s to 40 Mbit/s, 800 times less.',
          'Three timing bars against a dashed 50 ms line: camera 90 ms and cloud 80 ms cross it, edge 25 ms stays inside; below, a long backhaul bar of 32 Gbit/s and a tiny one of 40 Mbit/s.')


spec = make_spec(FIG)


def text_fixes(k):
    return {
        8: [('The figure shows the five actors and the direction of each relationship.',
             'The figure in this chapter leaves the roles aside and follows the meter: it builds one month of the worked example’s bill, line by line.')],
    }.get(k, [])
