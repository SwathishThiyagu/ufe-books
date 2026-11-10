"""Claude's hand-drawn figures for c-cn-u1 (Computer Networks, unit 1: data communication, network types, topologies,
protocols and models, switching and devices), one per chapter, from each chapter's worked example."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def seg(x, y, w, h, fill, c, label, size=13, fc=INK, bold=True):
    o = R(x, y, w, h, fill, c, 3, 1.6)
    if label: o += T(x + w / 2, y + h / 2 + 5, label, size, fill=fc, bold=bold)
    return o


# ---- 1.1 half-duplex against full-duplex on the teller link ----
def f1():
    o = []
    x0, sc = 140, 1.5                      # 1 ms = 1.5 px, 340 ms = 510 px
    fx = lambda t: x0 + t * sc
    lanes = [('half-duplex', 70, [(0, 200, 'request 200', ACS, AC), (200, 220, '', LVS, LV), (220, 320, 'reply 100', NXS, NX), (320, 340, '', LVS, LV)]),
             ('full-duplex', 170, [(0, 200, 'request 200', ACS, AC), (200, 300, 'reply 100', NXS, NX)])]
    for name, y, bars in lanes:
        o.append(T(x0 - 12, y + 25, name, 14, 'end', bold=True))
        for a, b, lab, f, c in bars:
            o.append(seg(fx(a), y, (b - a) * sc, 38, f, c, lab, 13, c))
        end = bars[-1][1]
        o.append(T(fx(end) + 8, y + 25, f'{end} ms', 14, 'start', INK, True))
    for t in (200, 320):
        o.append(T(fx(t + 10), 62, 'turn 20', 13, fill=LV, bold=True))
    o.append(xaxis(x0, fx(360), 250, [0, 100, 200, 300, 340], fx, 'time (ms)'))
    o.append(brace(fx(300), fx(340), 232, LV, up=True))
    o.append(T(fx(340) + 8, 236, '40 ms lost', 13, 'start', LV, True))
    o.append(T(20, 320, 'Half-duplex loses 340 − 300 = 40 ms to turnarounds: 40 ÷ 340 = 11.8% of its time.', 14, 'start', LV, True))
    return 336, ''.join(o)
FIG[1] = (f1, 'The same 200 ms request and 100 ms reply on both lines. Half-duplex adds two 20 ms turnarounds and takes 340 ms; full-duplex needs none and takes 300 ms, so 40 ms, about 11.8%, is lost.',
          'Two time bars: half-duplex with request 200 ms, turnaround 20 ms, reply 100 ms and turnaround 20 ms ending at 340 ms; full-duplex with request and reply only, ending at 300 ms.')


# ---- 1.2 MAN, WAN and the internetwork ----
def f2():
    o = []
    o.append(R(14, 30, 692, 240, 'none', L2, 14, 1.6, '8 5'))
    o.append(T(30, 52, 'internetwork: everything joined by routers', 13, 'start', MUT, True))
    o.append(f'<ellipse cx="200" cy="160" rx="160" ry="82" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2"/>')
    o.append(T(200, 72, 'MAN: one provider’s metro Ethernet', 13, fill=AC, bold=True))
    for x, y, n in ((120, 150, 'Office 1'), (280, 150, 'Office 2'), (200, 206, 'Office 3')):
        o.append(boxt(x - 44, y - 18, 88, 36, [n], PANEL, AC, 13, bold_first=True))
    o.append(L(164, 150, 236, 150, AC, 2)); o.append(L(130, 168, 170, 190, AC, 2)); o.append(L(270, 168, 230, 190, AC, 2))
    o.append(T(200, 132, 'Chennai', 13, fill=AC))
    o.append(boxt(560, 132, 120, 44, ['Dubai office'], NXS, NX, 14, bold_first=True))
    o.append(L(326, 150, 556, 154, NX, 3, arrow='x'))
    o.append(T(462, 140, 'WAN link, 34 Mbps', 14, fill=NX, bold=True))
    o.append(T(462, 176, 'across countries on carrier fibre', 13, fill=MUT))
    o.append(T(20, 300, '68 MB file = 68 × 8 = 544 Mbit', 14, 'start'))
    o.append(T(20, 324, 'time = 544 Mbit ÷ 34 Mbps = 16 s', 14, 'start', NX, True))
    return 340, ''.join(o)
FIG[2] = (f2, 'Three Chennai offices on one provider’s metro Ethernet form a MAN, the 34 Mbps link to Dubai is a WAN, and all of it joined by routers is an internetwork. A 68 MB file takes 544 ÷ 34 = 16 s to Dubai.',
          'Three Chennai offices inside an ellipse marked MAN, a 34 Mbps WAN arrow to a Dubai office, and a dashed outer box marked internetwork, with the 16 s file-time calculation below.')


# ---- 1.3 full mesh against star for 8 PCs ----
def f3():
    o = []
    def ring(cx, cy, r):
        return [(cx + r * math.cos(2 * math.pi * i / 8 - math.pi / 2), cy + r * math.sin(2 * math.pi * i / 8 - math.pi / 2)) for i in range(8)]
    m = ring(180, 160, 110)
    for i in range(8):
        for j in range(i + 1, 8):
            o.append(L(*m[i], *m[j], LV, 1.3))
    for x, y in m:
        o.append(R(x - 15, y - 12, 30, 24, PANEL, LV, 4, 2))
    s = ring(540, 160, 110)
    for x, y in s:
        o.append(L(540, 160, x, y, NX, 2))
    for x, y in s:
        o.append(R(x - 15, y - 12, 30, 24, PANEL, NX, 4, 2))
    o.append(R(510, 142, 60, 36, NXS, NX, 6, 2)); o.append(T(540, 165, 'switch', 13, fill=NX, bold=True))
    o.append(T(180, 26, 'Full mesh', 15, fill=LV, bold=True)); o.append(T(540, 26, 'Star', 15, fill=NX, bold=True))
    o.append(T(180, 310, '8 × 7 ÷ 2 = 28 cables, 7 ports per PC', 14, fill=LV, bold=True))
    o.append(T(180, 332, '28 × 20 m = 560 m → ₹16,800', 14, fill=LV))
    o.append(T(180, 354, 'survives any one cable cut', 13, fill=MUT))
    o.append(T(540, 310, '8 cables, 8 switch ports', 14, fill=NX, bold=True))
    o.append(T(540, 332, '8 × 20 m = 160 m → ₹4,800', 14, fill=NX))
    o.append(T(540, 354, 'switch fails → whole lab is down', 13, fill=MUT))
    return 370, ''.join(o)
FIG[3] = (f3, 'The same 8-PC lab built two ways: a full mesh needs 28 cables, 560 m costing ₹16,800, while a star needs only 8 cables, 160 m costing ₹4,800, but stops entirely if its switch fails.',
          'Left, eight PCs with every pair joined, 28 lines; right, eight PCs each wired to one central switch, with cable counts, lengths and costs below each.')


# ---- 1.4 headers on the way down, and what they cost ----
def f4():
    o = [T(20, 26, 'Each layer wraps what it is given in its own header', 14, 'start', bold=True)]
    rows = [('application', [], 1460), ('TCP', [('TCP 20', AC)], 1480), ('IP', [('IP 20', NX), ('TCP 20', AC)], 1500),
            ('Ethernet', [('Eth 14', LV), ('IP 20', NX), ('TCP 20', AC)], 1518)]
    y = 46
    for name, hs, tot in rows:
        o.append(T(116, y + 23, name, 13, 'end', MUT, True))
        x = 126
        for lab, c in hs:
            o.append(seg(x, y, 66, 34, {AC: ACS, NX: NXS, LV: LVS}[c], c, lab, 13, c)); x += 68
        o.append(seg(x, y, 230, 34, PANEL, L2, 'data 1,460 bytes', 13, INK))
        x += 232
        if name == 'Ethernet':
            o.append(seg(x, y, 50, 34, LVS, LV, 'FCS 4', 13, LV)); x += 52
        o.append(T(x + 8, y + 23, f'{tot:,} B', 14, 'start', INK, True))
        y += 46
    o.append(T(20, 254, 'overhead 20 + 20 + 14 + 4 = 58 bytes', 14, 'start', LV, True))
    # efficiency bars
    for i, (lab, eff, txt) in enumerate((('1,460-byte message', 0.962, '1,460 ÷ 1,518 = 96.2%'), ('10-byte message', 0.147, '10 ÷ 68 = 14.7%'))):
        yy = 274 + i * 40
        o.append(T(150, yy + 21, lab, 13, 'end', MUT, True))
        o.append(R(160, yy, 360, 30, PANEL, L2, 3, 1.2))
        o.append(R(160, yy, 360 * eff, 30, NXS, NX, 3, 1.6))
        o.append(T(530, yy + 21, txt, 14, 'start', NX, True))
    return 360, ''.join(o)
FIG[4] = (f4, 'Going down the stack each layer adds a header, so 1,460 bytes of data leave as a 1,518-byte frame: 58 bytes of overhead and 96.2% user data. The same 58 bytes make a 10-byte message only 14.7% efficient.',
          'Four rows showing the data wrapped by a TCP header, then an IP header, then an Ethernet header and FCS trailer, growing from 1,460 to 1,518 bytes, and two efficiency bars of 96.2% and 14.7%.')


# ---- 1.5 sizes at each OSI layer ----
def f5():
    o = [T(20, 26, 'Host A sends 1200 bytes of user data down the seven layers', 14, 'start', bold=True)]
    layers = [('7 Application', '—', '1200 bytes'), ('6 Presentation', 'adds 0', '1200 bytes'), ('5 Session', 'adds 0', '1200 bytes'),
              ('4 Transport', '+ 20 header', '1220 bytes (segment)'), ('3 Network', '+ 20 header', '1240 bytes (packet)'),
              ('2 Data link', '+ 14 header, + 4 trailer', '1258 bytes (frame)'), ('1 Physical', 'sends the bits', '1258 bytes on the wire')]
    y = 44
    for i, (n, add, size) in enumerate(layers):
        adds = add.startswith('+')
        o.append(R(20, y, 170, 34, ACS if adds else PANEL, AC if adds else L2, 4, 1.6))
        o.append(T(32, y + 22, n, 14, 'start', AC if adds else INK, True))
        o.append(T(206, y + 22, add, 13, 'start', LV if adds else MUT, adds))
        o.append(T(700, y + 22, size, 14, 'end', NX if adds else INK, adds))
        if i < 6:
            o.append(L(105, y + 34, 105, y + 41, L2, 1.5))
        y += 41
    o.append(T(20, y + 22, 'overhead 1258 − 1200 = 58 bytes;  efficiency 1200 ÷ 1258 = 95.39%', 14, 'start', NX, True))
    return y + 40, ''.join(o)
FIG[5] = (f5, 'Going down the seven layers, only transport, network and data link add bytes: the 1200 bytes of data become a 1220-byte segment, a 1240-byte packet and a 1258-byte frame, 95.39% useful.',
          'The seven OSI layers stacked from application to physical, with the bytes each adds and the size after it: 1200, 1200, 1200, 1220, 1240, 1258 and 1258.')


# ---- 1.6 twelve protocols in four layers ----
def f6():
    o = []
    rows = [('Application', ['HTTP', 'DNS', 'SMTP', 'FTP', 'DHCP'], 'e'), ('Transport', ['TCP', 'UDP'], 'e'),
            ('Internet', ['IP', 'ICMP', 'ARP'], None), ('Network access', ['Ethernet', 'Wi-Fi'], 'h')]
    kind = {'IP': 'h', 'ICMP': 'h', 'ARP': 'b'}
    col = {'e': (AC, ACS), 'h': (LV, LVS), 'b': (NX, NXS)}
    y = 20
    for name, ps, k in rows:
        o.append(R(20, y, 680, 52, PANEL, L2, 6, 1.2))
        o.append(T(36, y + 31, name, 14, 'start', INK, True))
        x = 176
        for p in ps:
            kk = k or kind[p]
            c, f = col[kk]
            w = tw(p, 14) + 26
            o.append(R(x, y + 10, w, 32, f, c, 16, 2)); o.append(T(x + w / 2, y + 31, p, 14, fill=c, bold=True))
            x += w + 10
        o.append(T(684, y + 31, f'{len(ps)}', 16, 'end', INK, True))
        y += 60
    o.append(T(684, y + 14, 'total 5 + 2 + 3 + 2 = 12', 13, 'end', MUT, True))
    y += 34
    for i, (k, txt) in enumerate((('e', 'end to end: 7 (only in the two hosts)'), ('h', 'hop by hop: 4 (every device on the path)'), ('b', 'boundary: ARP, 1'))):
        c, f = col[k]
        xx = 20 + i * 240
        o.append(R(xx, y, 22, 18, f, c, 9, 2)); o.append(T(xx + 30, y + 14, txt.split(' (')[0], 13, 'start', c, True))
    return y + 34, ''.join(o)
FIG[6] = (f6, 'The twelve captured protocols sorted into the four TCP/IP layers, 5 + 2 + 3 + 2 = 12. The colours split the same twelve another way: 7 work end to end, 4 hop by hop, and ARP alone sits on the boundary.',
          'Four layer rows holding protocol chips: HTTP, DNS, SMTP, FTP, DHCP; TCP, UDP; IP, ICMP, ARP; Ethernet, Wi-Fi; coloured as end to end, hop by hop or boundary, with counts 5, 2, 3, 2.')


# ---- 1.7 circuit against packet switching for a 1 MB file ----
def f7():
    o = []
    x0, sc = 150, 56                      # 1 s = 56 px
    fx = lambda t: x0 + t * sc
    y1, y2 = 60, 150
    o.append(T(x0 - 12, y1 + 25, 'circuit', 14, 'end', bold=True))
    o.append(seg(fx(0), y1, 0.5 * sc, 38, LVS, LV, '', 13))
    o.append(seg(fx(0.5), y1, 8 * sc, 38, ACS, AC, 'data 8 Mbit at 1 Mbps = 8 s', 13, AC))
    o.append(seg(fx(8.5), y1, 0.5 * sc, 38, LVS, LV, '', 13))
    o.append(T(fx(0.25), y1 - 8, 'setup 0.5', 13, fill=LV, bold=True)); o.append(T(fx(8.75), y1 - 8, 'teardown 0.5', 13, fill=LV, bold=True))
    o.append(T(fx(9) + 8, y1 + 25, '9 s', 14, 'start', LV, True))
    o.append(T(x0 - 12, y2 + 25, 'packet', 14, 'end', bold=True))
    o.append(seg(fx(0), y2, 8 * sc, 38, NXS, NX, '1,000 packets × 8 ms = 8 s', 13, NX))
    o.append(R(fx(8), y2, 6, 38, NX, NX, 1, 1))
    o.append(T(fx(8) + 12, y2 + 25, '8.016 s', 14, 'start', NX, True))
    o.append(xaxis(x0, fx(9.4), 220, [0, 2, 4, 6, 8, 9], fx, 'time (s)'))
    # zoom box on the last 16 ms
    o.append(L(fx(8) + 3, y2 + 40, 470, 290, NX, 1.4, '4 3'))
    o.append(R(250, 290, 450, 60, PANEL, NX, 6, 1.6))
    o.append(T(266, 312, 'zoom on the end: the last packet still has two hops', 13, 'start', NX, True))
    o.append(seg(266, 320, 80, 22, NXS, NX, 'hop 2: 8 ms', 13, NX)); o.append(seg(350, 320, 80, 22, NXS, NX, 'hop 3: 8 ms', 13, NX))
    o.append(T(440, 336, '→ only 16 ms after 8 s', 13, 'start', NX, True))
    o.append(T(20, 380, 'Setup and teardown cost the circuit 1 s; packets pay just 16 ms extra.', 14, 'start', bold=True))
    return 396, ''.join(o)
FIG[7] = (f7, 'The circuit pays 0.5 s of setup before its 8 s of data and 0.5 s of teardown after, ending at 9 s. Packets start at once, all 1,000 leave in 8 s, and the last one’s two remaining hops add only 16 ms, ending at 8.016 s.',
          'Two timelines: circuit switching with setup 0.5 s, data 8 s and teardown 0.5 s ending at 9 s; packet switching with 8 s of packets ending at 8.016 s, and a zoom box showing two 8 ms hops.')


# ---- 1.8 a switch learning its MAC table ----
def f8():
    o = []
    xs = [170, 230, 290, 350]
    o.append(T(80, 34, 'frame', 13, fill=MUT, bold=True))
    for i, x in enumerate(xs):
        o.append(T(x, 34, f'port {i + 1}', 13, fill=MUT, bold=True))
    o.append(T(390, 34, 'what the switch does', 13, 'start', MUT, True))
    o.append(T(700, 34, 'table after', 13, 'end', MUT, True))
    frames = [('A → B', 1, [2, 3, 4], 'B unknown: flood 3', 'A 1'), ('B → A', 2, [1], 'A known: forward 1', 'A 1, B 2'),
              ('A → C', 1, [2, 3, 4], 'C unknown: flood 3', 'A 1, B 2'), ('C → A', 3, [1], 'A known: forward 1', 'A 1, B 2, C 3')]
    for r, (f, src, outs, act, tab) in enumerate(frames):
        y = 48 + r * 50
        o.append(T(80, y + 26, f'{r + 1}. {f}', 14, fill=INK, bold=True))
        for i, x in enumerate(xs):
            p = i + 1
            if p == src:
                o.append(R(x - 26, y + 4, 52, 34, ACS, AC, 4, 2)); o.append(T(x, y + 26, 'in', 13, fill=AC, bold=True))
            elif p in outs:
                o.append(R(x - 26, y + 4, 52, 34, LVS, LV, 4, 2)); o.append(T(x, y + 26, 'out', 13, fill=LV, bold=True))
            else:
                o.append(R(x - 26, y + 4, 52, 34, PANEL, LN, 4, 1))
        o.append(T(390, y + 26, act, 14, 'start', LV, True))
        o.append(T(700, y + 26, tab, 14, 'end', AC, True))
    o.append(R(20, 260, 22, 16, ACS, AC, 3, 2)); o.append(T(50, 274, 'in: arrives here, so the sender is learned on this port', 13, 'start', AC))
    o.append(R(470, 260, 22, 16, LVS, LV, 3, 2)); o.append(T(500, 274, 'out: sent out here', 13, 'start', LV))
    return 292, ''.join(o)
FIG[8] = (f8, 'One row per frame: the switch learns each sender’s port from where the frame arrives, floods to the 3 other ports when the destination is unknown, and forwards to 1 port once it is known. It ends with A on 1, B on 2, C on 3.',
          'A table of four frames A to B, B to A, A to C and C to A across ports 1 to 4, marking the arrival port and the ports sent out, with flood 3 or forward 1 and the MAC table growing to A 1, B 2, C 3.')


spec = make_spec(FIG)
