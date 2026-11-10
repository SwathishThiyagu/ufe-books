"""Claude's hand-drawn figures for c-cn-u4 (Computer Networks, unit 4: the network layer: addressing, subnetting, IPv4
and IPv6, helper protocols and routing), one per chapter, from each chapter's worked example."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def cell(x, y, w, h, s, c=INK, fill=PANEL, stroke=L2, size=15, bold=True, mono=True, sw=1.4, dash=None):
    o = R(x, y, w, h, fill, stroke, 3, sw, dash)
    o += (TM if mono else T)(x + w / 2, y + h / 2 + 5, s, size, fill=c, bold=bold)
    return o


# ---- 4.1 network and broadcast of 172.16.5.10/22 ----
def f1():
    o = [T(20, 26, '172.16.5.10/22: the first 22 bits name the network, the last 10 bits the host', 14, 'start', bold=True)]
    x3, x4, cw = 206, 400, 22
    o.append(T(x3 + 4 * cw, 52, 'third octet', 13, fill=MUT, bold=True)); o.append(T(x4 + 4 * cw, 52, 'fourth octet', 13, fill=MUT, bold=True))
    rows = [('address', '172.16.', '00000101', '00001010', '172.16.5.10', INK),
            ('mask', '255.255.', '11111100', '00000000', '255.255.252.0', MUT),
            ('network (AND)', '172.16.', '00000100', '00000000', '172.16.4.0', AC),
            ('broadcast', '172.16.', '00000111', '11111111', '172.16.7.255', LV)]
    for r, (name, pre, b3, b4, dec, c) in enumerate(rows):
        y = 62 + r * 46
        o.append(T(112, y + 22, name, 13, 'end', c, True))
        o.append(TM(196, y + 22, pre, 14, 'end', c, True))
        for k, b in enumerate(b3 + b4):
            host = k >= 6
            x = (x3 + k * cw) if k < 8 else (x4 + (k - 8) * cw)
            o.append(cell(x, y + 2, cw - 2, 30, b, c, LVS if host else ACS, L2, 14, sw=1))
        o.append(T(700, y + 22, dec, 14, 'end', c, True))
    o.append(brace(x3, x3 + 6 * cw - 2, 252, AC)); o.append(T(x3 + 3 * cw, 276, 'network bits 17–22', 13, fill=AC, bold=True))
    o.append(brace(x3 + 6 * cw, x4 + 8 * cw - 2, 252, LV)); o.append(T((x3 + 6 * cw + x4 + 8 * cw) / 2, 276, '10 host bits: 2¹⁰ = 1024 addresses', 13, fill=LV, bold=True))
    o.append(T(20, 312, 'usable 172.16.4.1 to 172.16.7.254 = 1024 − 2 = 1022 hosts', 14, 'start', INK, True))
    o.append(T(20, 336, 'Class B by its first octet 172; the old default /16 would have given 172.16.0.0.', 13, 'start', MUT))
    return 352, ''.join(o)
FIG[1] = (f1, 'The /22 mask keeps 22 network bits. ANDing the third octet 5 (00000101) with 252 (11111100) gives 4, so the network is 172.16.4.0; setting the 10 host bits to 1 gives broadcast 172.16.7.255, leaving 1022 usable hosts.',
          'The third and fourth octets of 172.16.5.10, its mask 255.255.252.0, the network 172.16.4.0 and the broadcast 172.16.7.255 written in binary, with the 10 host bits shaded.')


# ---- 4.2 VLSM inside 192.168.1.0/24 ----
def f2():
    o = [T(20, 26, '192.168.1.0/24 cut largest first: 100, 50, 25 and 10 hosts', 14, 'start', bold=True)]
    x0, sc, y = 40, 2.5, 60
    fx = lambda a: x0 + a * sc
    blocks = [(0, 128, '/25', '100 hosts', AC, ACS, '.0–.127', '126 usable'), (128, 64, '/26', '50 hosts', NX, NXS, '.128–.191', '62 usable'),
              (192, 32, '/27', '25', LV, LVS, '.192–.223', '30 usable'), (224, 16, '/28', '10', AC, ACS, '.224–.239', '14 usable'),
              (240, 16, 'free', '', L2, PANEL, '.240–.255', 'unused')]
    for i, (a, n, p, need, c, f, rng, use) in enumerate(blocks):
        o.append(R(fx(a), y, n * sc, 70, f, c, 2, 2, '5 4' if p == 'free' else None))
        o.append(T(fx(a + n / 2), y + 30, p, 15 if n >= 32 else 13, fill=c, bold=True))
        if need: o.append(T(fx(a + n / 2), y + 52, need, 13, fill=c, bold=True))
        yy = 168 + (i % 2) * 40 if n < 64 else 168
        o.append(L(fx(a + n / 2), y + 72, fx(a + n / 2), yy - 16, L2, 1.2))
        o.append(T(fx(a + n / 2), yy, rng, 13, fill=c if c != L2 else MUT, bold=True))
        o.append(T(fx(a + n / 2), yy + 17, use, 13, fill=MUT))
    o.append(xaxis(x0, fx(256), y + 70, [0, 128, 192, 256], fx, None, lambda v: ''))
    o.append(T(20, 270, 'Hosts need 2^h − 2 ≥ count: 126 ≥ 100, 62 ≥ 50, 30 ≥ 25, 14 ≥ 10, so h = 7, 6, 5, 4 and prefix = 32 − h.', 13, 'start', INK))
    return 288, ''.join(o)
FIG[2] = (f2, 'The /24 block is cut largest-first: a /25 for 100 hosts, a /26 for 50, a /27 for 25 and a /28 for 10 sit end to end, and 192.168.1.240–255 stays free.',
          'A bar of 256 addresses split into /25 from .0 to .127, /26 from .128 to .191, /27 from .192 to .223, /28 from .224 to .239 and a free range .240 to .255, with usable counts 126, 62, 30 and 14.')


# ---- 4.3 fragmenting a 4000-byte datagram for MTU 1500 ----
def f3():
    o = [T(20, 26, '3980 bytes of data must cross a link whose MTU is 1500 bytes', 14, 'start', bold=True)]
    x0, sc = 80, 0.15                 # 1 byte = 0.15 px, 3980 = 597 px
    fx = lambda b: x0 + b * sc
    o.append(R(x0 - 40, 46, 38, 36, LVS, LV, 2, 1.6)); o.append(T(x0 - 21, 69, '20', 13, fill=LV, bold=True))
    o.append(R(fx(0), 46, 3980 * sc, 36, PANEL, L2, 2, 1.4)); o.append(T(fx(1990), 69, 'original data 3980 bytes', 13, fill=INK, bold=True))
    frs = [(0, 1480, '1500', '0', '1'), (1480, 1480, '1500', '185', '1'), (2960, 1020, '1040', '370', '0')]
    for i, (a, n, tot, off, mf) in enumerate(frs):
        y = 116 + i * 58
        o.append(R(fx(a) - 40, y, 38, 36, LVS, LV, 2, 1.6)); o.append(T(fx(a) - 21, y + 23, '20', 13, fill=LV, bold=True))
        o.append(R(fx(a), y, n * sc, 36, NXS if mf == '0' else ACS, NX if mf == '0' else AC, 2, 1.6))
        o.append(T(fx(a + n / 2), y + 23, f'{n} bytes', 13, fill=NX if mf == '0' else AC, bold=True))
        o.append(L(fx(a), 84, fx(a), y, L2, 1, '3 3'))
        o.append(T(fx(a), y + 50, f'total {tot}, offset {a} ÷ 8 = {off}, MF = {mf}', 13, 'start' if i < 2 else 'end', MUT, True)
                 if i < 2 else T(fx(a + n), y + 50, f'total {tot}, offset {a} ÷ 8 = {off}, MF = {mf}', 13, 'end', MUT, True))
    o.append(T(20, 318, 'Each fragment repeats the 20-byte header; offsets count 8-byte units, and only the last has MF = 0.', 13, 'start', INK))
    return 334, ''.join(o)
FIG[3] = (f3, 'Each fragment carries its own 20-byte header, so total length = 20 + data: 1500, 1500 and 1040 bytes. Offsets count 8-byte units (1480 ÷ 8 = 185), and only the last fragment has MF = 0.',
          'The 3980 data bytes of the original datagram above three fragments of 1480, 1480 and 1020 bytes, each with its own 20-byte header, labelled with total length, offset 0, 185, 370 and MF 1, 1, 0.')


# ---- 4.4 compressing an IPv6 address ----
def f4():
    o = []
    full = ['2001', '0db8', '0000', '0000', '0000', 'ff00', '0042', '8329']
    short = ['2001', 'db8', '0', '0', '0', 'ff00', '42', '8329']
    x0, cw = 40, 82
    o.append(T(20, 26, 'Eight groups of four hex digits, 128 bits', 14, 'start', bold=True))
    for i in range(8):
        x = x0 + i * cw
        zero = 2 <= i <= 4
        o.append(T(x + cw / 2 - 3, 52, f'group {i + 1}', 13, fill=MUT))
        o.append(cell(x, 60, cw - 6, 36, full[i], LV if zero else INK, LVS if zero else PANEL, LV if zero else L2, 15))
        o.append(cell(x, 130, cw - 6, 36, short[i], LV if zero else INK, LVS if zero else PANEL, LV if zero else L2, 15))
    o.append(T(20, 118, 'drop leading zeros in each group', 13, 'start', MUT, True))
    o.append(brace(x0 + 2 * cw, x0 + 5 * cw - 6, 176, LV))
    o.append(T(x0 + 3.5 * cw - 3, 200, 'longest zero run, 3 groups → ::', 13, fill=LV, bold=True))
    o.append(T(20, 236, 'compressed:', 14, 'start', MUT, True))
    o.append(TM(130, 236, '2001:db8::ff00:42:8329', 17, 'start', LV, True))
    o.append(T(20, 276, '/64 LAN prefix = first 4 groups:', 14, 'start', MUT, True))
    o.append(TM(270, 276, '2001:db8:0:0::/64', 17, 'start', AC, True))
    return 294, ''.join(o)
FIG[4] = (f4, 'Groups 3, 4 and 5 are the longest run of all-zero groups, so one :: replaces them, giving 2001:db8::ff00:42:8329. The /64 LAN prefix keeps the first four groups: 2001:db8:0:0::/64.',
          'The eight groups of 2001:0db8:0000:0000:0000:ff00:0042:8329, the same groups with leading zeros dropped, groups 3 to 5 braced as the run replaced by ::, and the compressed form and /64 prefix.')


# ---- 4.5 ARP, then NAT on the way out ----
def f5():
    o = []
    xs = {'host': 90, 'router': 360, 'server': 630}
    labs = {'host': ['host', '192.168.1.10, MAC 00:11'], 'router': ['router', '192.168.1.1, MAC aa:bb'], 'server': ['server', '203.0.113.80']}
    for k, x in xs.items():
        o.append(boxt(x - 85, 14, 170, 44, labs[k], ACS if k == 'router' else PANEL, AC if k == 'router' else L2, 13, bold_first=True))
        o.append(L(x, 58, x, 296, L2, 1.4, '4 4'))
    def msg(y, a, b, top, bot, c, ar):
        xa, xb = xs[a], xs[b]
        o.append(L(xa + (4 if xb > xa else -4), y, xb - (6 if xb > xa else -6), y, c, 2.2, arrow=ar))
        o.append(Tb((xa + xb) / 2, y - 8, top, 13, fill=c, bold=True))
        if bot: o.append(T((xa + xb) / 2, y + 18, bot, 13, fill=MUT))
    msg(90, 'host', 'router', 'ARP request: who has 192.168.1.1?', 'broadcast to ff:ff:ff:ff:ff:ff', AC, 'n')
    msg(150, 'router', 'host', 'ARP reply: 192.168.1.1 is at aa:bb', 'unicast; host caches it', AC, 'n')
    msg(210, 'host', 'router', 'src 192.168.1.10:4000', 'frame sent to MAC aa:bb', NX, 'x')
    msg(260, 'router', 'server', 'src 198.51.100.5:6000', 'source rewritten by NAT', LV, 'l')
    o.append(boxt(250, 300, 220, 54, ['NAT table', '192.168.1.10:4000 ↔ 198.51.100.5:6000'], LVS, LV, 13, bold_first=True))
    return 366, ''.join(o)
FIG[5] = (f5, 'The first two messages are ARP, so the host learns the gateway’s MAC aa:bb. The host then sends from 192.168.1.10:4000, and the router rewrites the source to 198.51.100.5:6000 and records the pair in its NAT table.',
          'A sequence diagram with host, router and server: an ARP request and reply between host and router, then the packet from 192.168.1.10:4000 to the router and from 198.51.100.5:6000 to the server, with the NAT table entry.')


# ---- 4.6 summarising four /24s into one /22 ----
def f6():
    o = []
    o.append(boxt(250, 20, 220, 46, ['core: one route', '10.0.0.0/22 → edge'], ACS, AC, 14, bold_first=True))
    nets = ['10.0.0.0/24', '10.0.1.0/24', '10.0.2.0/24', '10.0.3.0/24']
    bins = ['000000 00', '000000 01', '000000 10', '000000 11']
    for i, (n, b) in enumerate(zip(nets, bins)):
        x = 30 + i * 172
        o.append(L(360, 66, x + 76, 116, L2, 1.6))
        hot = i == 2
        o.append(boxt(x, 118, 152, 40, [n], NXS if hot else PANEL, NX if hot else L2, 14, bold_first=True))
        o.append(T(x + 76, 182, 'third octet', 13, fill=MUT))
        o.append(TM(x + 46, 204, b[:6], 15, fill=AC, bold=True)); o.append(TM(x + 112, 204, b[7:], 15, fill=LV, bold=True))
    o.append(T(20, 240, '10.0 (16 bits) + six shared bits 000000 = 22 common bits → 10.0.0.0/22, 2¹⁰ = 1024 addresses', 14, 'start', AC, True))
    o.append(T(20, 266, 'Flat table: 4 entries.  Core table: 1 entry.', 14, 'start', INK, True))
    o.append(T(20, 292, 'A packet to 10.0.2.5 matches both /22 and 10.0.2.0/24; the longer prefix, /24, wins.', 14, 'start', NX, True))
    return 308, ''.join(o)
FIG[6] = (f6, 'The four /24 LANs share their first 22 bits, so the core keeps one route, 10.0.0.0/22, covering 1024 addresses, instead of four. A packet to 10.0.2.5 matches the summary and 10.0.2.0/24; the longer /24 wins.',
          'One core summary route 10.0.0.0/22 above four /24 networks 10.0.0.0 to 10.0.3.0, each with its third octet in binary, the first six bits shared and the last two differing.')


# ---- 4.7 count to infinity ----
def f7():
    o = []
    # topology
    pos = {'A': (70, 60), 'B': (190, 60), 'C': (310, 60)}
    o.append(L(94, 60, 166, 60, AC, 2.2)); o.append(L(214, 60, 286, 60, L2, 2.2, '5 4'))
    o.append(L(240, 46, 260, 74, LV, 3)); o.append(L(260, 46, 240, 74, LV, 3))
    for n, (x, y) in pos.items():
        o.append(state(x, y, n, stroke=AC if n != 'C' else L2))
    o.append(T(250, 100, 'B–C link fails', 13, fill=LV, bold=True))
    o.append(T(370, 54, 'before: B reaches C at 1,', 13, 'start', MUT))
    o.append(T(370, 72, 'A at 2 (via B)', 13, 'start', MUT))
    # bars
    x0, y1, sc = 60, 330, 12
    vals = [('B', 3), ('A', 4), ('B', 5), ('A', 6)] + [('B' if v % 2 else 'A', v) for v in range(7, 17)]
    o.append(L(40, y1, 700, y1, L2, 1.5))
    o.append(L(40, y1 - 16 * sc, 700, y1 - 16 * sc, LV, 1.8, '6 4'))
    o.append(T(40, y1 - 16 * sc - 8, '16 = infinity in RIP', 13, 'start', LV, True))
    for i, (r, v) in enumerate(vals):
        x = x0 + i * 44
        c, f = (AC, ACS) if r == 'B' else (NX, NXS)
        o.append(R(x, y1 - v * sc, 34, v * sc, f, c, 2, 1.6))
        o.append(T(x + 17, y1 - v * sc + (18 if v >= 15 else -6), str(v), 13, fill=c, bold=True))
        o.append(T(x + 17, y1 + 18, r, 13, fill=c, bold=True))
    o.append(T(60, y1 + 46, 'B: 1 + A’s stale 2 = 3,  A: 1 + 3 = 4,  B: 1 + 4 = 5,  A: 1 + 5 = 6, … each update adds 1', 13, 'start', INK, True))
    return y1 + 62, ''.join(o)
FIG[7] = (f7, 'After the B–C link fails, A’s stale cost 2 starts the loop: B computes 1 + 2 = 3, A computes 1 + 3 = 4, then B = 5 and A = 6. Each update adds 1 until the cost reaches 16, which RIP treats as infinity.',
          'Routers A, B, C in a line with the B–C link crossed out, above bars of the alternating B and A costs to C rising 3, 4, 5, 6 up to 16, with a dashed line at 16 marked infinity.')


# ---- 4.8 Dijkstra from A ----
def f8():
    o = []
    P_ = {'A': (60, 160), 'B': (180, 70), 'C': (180, 250), 'D': (300, 160)}
    edges = [('A', 'B', 1, True), ('A', 'C', 4, False), ('B', 'C', 2, True), ('B', 'D', 5, False), ('C', 'D', 1, True)]
    for a, b, w, tree in edges:
        (x1, y1), (x2, y2) = P_[a], P_[b]
        o.append(L(x1, y1, x2, y2, NX if tree else L2, 4 if tree else 1.8, None if tree else '5 4'))
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        o.append(Tb(mx + (12 if a != 'B' or b != 'C' else 12), my + 5, str(w), 14, fill=NX if tree else MUT, bold=True))
    fin = {'A': '0', 'B': '1', 'C': '3', 'D': '4'}
    for n, (x, y) in P_.items():
        o.append(state(x, y, n, stroke=NX, fill=NXS if n == 'A' else PANEL))
        o.append(T(x, y + 44 if y > 100 else y - 32, f'cost {fin[n]}', 13, fill=NX, bold=True))
    # table
    x0 = 360
    head = ['step', 'done', 'B', 'C', 'D']
    cx = [380, 450, 540, 610, 680]
    for x, h in zip(cx, head):
        o.append(T(x, 40, h, 13, fill=MUT, bold=True))
    rows = [('0', 'A', '1(A)', '4(A)', '∞'), ('1', 'A B', '1', '3(B)', '6(B)'), ('2', 'A B C', '1', '3', '4(C)'), ('3', 'A B C D', '1', '3', '4')]
    hot = {(1, 3), (2, 4)}
    for r, row in enumerate(rows):
        y = 52 + r * 44
        o.append(R(x0, y, 340, 36, PANEL, LN, 6, 1))
        for j, (x, v) in enumerate(zip(cx, row)):
            h = (r, j) in hot
            o.append(T(x, y + 24, v, 14, fill=LV if h else INK, bold=h or j == 1))
    o.append(T(x0, 250, 'C drops 4 → 3 via B; D drops 6 → 4 via C.', 13, 'start', LV, True))
    o.append(T(x0, 272, 'Tree: A–B, B–C, C–D. The direct A–C', 13, 'start', NX, True))
    o.append(T(x0, 290, 'edge of cost 4 is never used.', 13, 'start', NX, True))
    return 310, ''.join(o)
FIG[8] = (f8, 'Dijkstra from A, one row per step; 3(B) means cost 3 through B. C falls from 4 to 3 via B and D from 6 to 4 via C, so the final costs are B = 1, C = 3, D = 4 and the green tree never uses the direct A–C edge.',
          'A four-node graph with edges A–B 1, A–C 4, B–C 2, B–D 5, C–D 1 and the shortest-path tree A–B, B–C, C–D in bold, beside a Dijkstra table of the four steps.')


# ---- 4.9 BGP: AS_PATH length against LOCAL_PREF ----
def f9():
    o = []
    def asn(x, y, s, c=AC, f=PANEL):
        o.append(boxt(x - 38, y - 20, 76, 40, [s], f, c, 14, bold_first=True))
    asn(70, 140, 'AS10', AC, ACS)
    asn(230, 80, 'AS20', NX); asn(390, 80, 'AS30', NX)
    asn(230, 210, 'AS40', LV); asn(350, 210, 'AS50', LV); asn(470, 210, 'AS60', LV)
    o.append(boxt(570, 125, 140, 30, ['203.0.113.0/24'], PANEL, INK, 13, bold_first=True))
    o.append(L(192, 80, 110, 128, NX, 2.2, arrow='x')); o.append(L(352, 80, 270, 80, NX, 2.2, arrow='x')); o.append(L(570, 132, 430, 86, NX, 2.2, arrow='x'))
    o.append(L(192, 210, 110, 154, LV, 2.2, arrow='l')); o.append(L(312, 210, 270, 210, LV, 2.2, arrow='l'))
    o.append(L(432, 210, 390, 210, LV, 2.2, arrow='l')); o.append(L(600, 156, 510, 202, LV, 2.2, arrow='l'))
    o.append(T(310, 40, 'AS_PATH [20, 30]: length 2', 13, fill=NX, bold=True))
    o.append(T(350, 256, 'AS_PATH [40, 50, 60]: length 3', 13, fill=LV, bold=True))
    o.append(T(20, 294, 'Default (LOCAL_PREF equal): shorter AS_PATH, 2 < 3, so the route via AS20 wins.', 14, 'start', NX, True))
    o.append(T(20, 320, 'LOCAL_PREF 200 on the AS40 route: it is checked before AS_PATH, so the AS40 route wins.', 14, 'start', LV, True))
    return 338, ''.join(o)
FIG[9] = (f9, 'AS10 hears 203.0.113.0/24 through AS20 with AS_PATH [20, 30] and through AS40 with [40, 50, 60]. By default the shorter path wins; with LOCAL_PREF 200 on the AS40 route, that route wins, because LOCAL_PREF is compared first.',
          'AS10 on the left receiving the prefix 203.0.113.0/24 along two chains, AS30 to AS20 and AS60 to AS50 to AS40, with AS_PATH lengths 2 and 3 and the two decision rules below.')


spec = make_spec(FIG)
