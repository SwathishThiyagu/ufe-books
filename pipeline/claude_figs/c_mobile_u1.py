"""Claude's hand-drawn figures for c-mobile-u1 (Mobile Application Development, unit 1: mobile computing and wireless
networks), one per chapter, each drawn from that chapter's worked example with its own numbers."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def chain(y, boxes, x0=16, w=120, gap=24, h=58, labels=None, fills=None):
    o = []
    for i, lines in enumerate(boxes):
        x = x0 + i * (w + gap)
        f, s = (fills[i] if fills else (PANEL, AC))
        o.append(boxt(x, y, w, h, lines, f, s, 14, bold_first=True))
        if i < len(boxes) - 1:
            o.append(L(x + w + 2, y + h / 2, x + w + gap - 3, y + h / 2, AC, 2, arrow='n'))
    return ''.join(o)


# ---- 1.1 three parts, and where the 43.2768 ms goes ----
def f1():
    o = [T(16, 24, 'The 2 KB UPI request travels through the three parts of every mobile system', 15, 'start', bold=True)]
    o.append(chain(52, [['Mobile host', 'phone + app'], ['Radio link', '4G, 5 Mbps'], ['Base station', 'first hop'],
                        ['Middleware', 'location, sync'], ['Server', 'fixed network']], w=124, gap=18,
                   fills=[(ACS, AC), (PANEL, AC), (PANEL, AC), (LVS, LV), (NXS, NX)]))
    o.append(brace(16, 16 + 124, 124, MUT, up=False))
    o.append(T(78, 150, 'part 1', 13, fill=MUT))
    o.append(brace(158, 16 + 3 * 142 - 18, 124, MUT))
    o.append(T((158 + 16 + 3 * 142 - 18) / 2, 150, 'part 2: radio access network', 13, fill=MUT))
    o.append(brace(16 + 3 * 142, 16 + 5 * 142 - 18, 124, MUT))
    o.append(T((16 + 3 * 142 + 16 + 5 * 142 - 18) / 2, 150, 'part 3: fixed network', 13, fill=MUT))
    # time bar to scale
    x0, x1, y = 40, 680, 214
    sc = (x1 - x0) / 43.2768
    o.append(T(16, 192, 'One-way time, drawn to scale', 15, 'start', bold=True))
    o.append(R(x0, y, 3.2768 * sc, 34, ACS, AC, 3))
    o.append(R(x0 + 3.2768 * sc, y, 40 * sc, 34, NXS, NX, 3))
    o.append(T(x0 + 3.2768 * sc + 20 * sc, y + 22, 'one-way delay 40 ms', 14, bold=True))
    o.append(L(x0 + 1.6 * sc, y + 36, x0 + 30, y + 62, AC, 1.5))
    o.append(T(x0 + 34, y + 70, 'transmission: 16 384 bits ÷ 5 000 000 bit/s = 3.2768 ms', 14, 'start', AC))
    o.append(xaxis(x0, x1, y + 92, [0, 10, 20, 30, 40], lambda v: x0 + v * sc, None, lambda v: f'{v} ms'))
    o.append(L(x1, y - 6, x1, y + 92, INK, 1.5, '4 3'))
    o.append(Tb(x1 - 4, y - 12, 'arrives at 43.2768 ms', 14, 'end', bold=True))
    return 350, ''.join(o)
FIG[1] = (f1, 'The request leaves the phone, crosses the radio link to the base station and passes the middleware to the server. Of its 43.2768 ms, only 3.2768 ms is pushing bits onto the 5 Mbps link; the 40 ms delay sets the wait.',
          'Five boxes in a row, phone, radio link, base station, middleware and server, grouped into the three parts; below, a time bar where a thin 3.2768 ms transmission slice is followed by a long 40 ms delay, ending at 43.2768 ms.')


# ---- 1.2 generations on a timeline and one 5 MB song ----
def f2():
    gens = [('1G', '1980s', ['analog', 'voice'], None), ('2G', '1991', ['digital voice', '+ SMS'], ('9.6 kbps', '4167 s', '69.4 min')),
            ('2.5G', '2000', ['packet data', '(GPRS)'], None), ('3G', '2001', ['higher rates', '(UMTS)'], ('384 kbps', '104.2 s', '1.7 min')),
            ('4G', '2009', ['all-IP', '(LTE)'], ('20 Mbps', '2.0 s', '')), ('5G', '2019', ['low delay,', 'slicing'], None)]
    o = [T(16, 24, 'Each generation adds one capability', 15, 'start', bold=True)]
    x0, w, gap, y = 16, 106, 12, 70
    o.append(L(10, y, 712, y, L2, 2, arrow='m'))
    for i, (g, yr, cap, dl) in enumerate(gens):
        x = x0 + i * (w + gap); cx = x + w / 2
        o.append(C(cx, y, 6, AC))
        o.append(T(cx, y - 14, yr, 13, fill=MUT))
        o.append(boxt(x, y + 18, w, 76, [g] + cap, PANEL, AC, 14, bold_first=True))
        if dl:
            o.append(L(cx, y + 96, cx, y + 132, AC, 2, arrow='n'))
            o.append(boxt(x - 4, y + 136, w + 8, 82, [dl[0], dl[1], dl[2]] if dl[2] else [dl[0], dl[1]], NXS if g == '2G' else (ACS if g == '4G' else PANEL),
                          NX if g == '2G' else AC, 14, bold_first=False))
    o.append(T(16, y + 250, 'Download time for one 5 MB song = 40,000,000 bits ÷ rate:', 14, 'start'))
    o.append(T(16, y + 272, '2G waits over an hour, 3G under two minutes, 4G two seconds.', 14, 'start', MUT))
    return y + 290, ''.join(o)
FIG[2] = (f2, 'The generations in order, each adding one capability. Under 2G, 3G and 4G is the time to download the same 40,000,000-bit song: 4167 s (69.4 min), 104.2 s (1.7 min) and 2.0 s.',
          'A timeline from 1G to 5G with one box per generation naming what it added; under 2G, 3G and 4G, boxes give the rate and the time to download a 5 MB song: 69.4 minutes, 1.7 minutes and 2 seconds.')


# ---- 1.3 one GSM cell: 4 carriers x 8 slots ----
def f3():
    o = [T(16, 24, 'One GSM cell: 4 carriers, each cut into 8 time slots per 4.615 ms frame', 15, 'start', bold=True)]
    x0, y0, cw, ch = 150, 70, 64, 40
    for s in range(8):
        o.append(T(x0 + s * cw + cw / 2, y0 - 10, f'slot {s}', 13, fill=MUT))
    for c in range(4):
        o.append(T(x0 - 12, y0 + c * ch + ch / 2 + 5, f'carrier {c + 1}', 14, 'end'))
        for s in range(8):
            ctrl = (c == 0 and s == 0)
            o.append(R(x0 + s * cw + 2, y0 + c * ch + 2, cw - 4, ch - 4, NXS if ctrl else ACS, NX if ctrl else AC, 4, 1.5))
            o.append(T(x0 + s * cw + cw / 2, y0 + c * ch + ch / 2 + 5, 'control' if ctrl else 'call', 13, bold=ctrl))
    yb = y0 + 4 * ch
    o.append(brace(x0 + 2, x0 + cw - 2, yb + 8))
    o.append(T(x0 + cw / 2, yb + 32, '576.875 µs', 13))
    o.append(T(x0 + cw / 2, yb + 48, '= 4.615 ms ÷ 8', 13, fill=MUT))
    o.append(brace(x0 + cw + 2, x0 + 8 * cw - 2, yb + 8))
    o.append(T(x0 + 4.5 * cw, yb + 32, 'one frame = 4.615 ms, repeating 1 ÷ 4.615 ms = 216.7 times a second', 13))
    o.append(T(16, yb + 90, 'Slots: 4 × 8 = 32.   One is the control channel.   Calls at once: 32 − 1 = 31.', 15, 'start', bold=True))
    return yb + 108, ''.join(o)
FIG[3] = (f3, 'Four carriers with 8 slots each give 4 × 8 = 32 slots; one carries the control channel, so 31 calls run at once. Each slot is 4.615 ms ÷ 8 = 576.875 µs, and frames repeat 216.7 times a second.',
          'A grid of 4 rows (carriers) by 8 columns (time slots); one cell is marked control and the other 31 are calls; braces show one slot of 576.875 microseconds and one frame of 4.615 milliseconds.')


# ---- 1.4 seven-cell cluster and reuse distance ----
def hexagon(cx, cy, r, fill, stroke, sw=2, dash=None):
    pts = ' '.join(f'{cx + r * math.cos(math.radians(60 * k + 30)):.1f},{cy + r * math.sin(math.radians(60 * k + 30)):.1f}' for k in range(6))
    d = f';stroke-dasharray:{dash}' if dash else ''
    return f'<polygon points="{pts}" style="fill:{fill};stroke:{stroke};stroke-width:{sw}{d}"/>'


def f4():
    r = 36
    # pointy-top hexes, axial coordinates (q, s): centre = (sqrt3 r (q + s/2), 1.5 r s)
    pos = lambda q, s: (cx0 + math.sqrt(3) * r * (q + s / 2), cy0 + 1.5 * r * s)
    cx0, cy0 = 150, 180
    o = [T(16, 24, 'Cluster N = 7 (i = 2, j = 1): each letter is one channel group', 15, 'start', bold=True)]
    nb = [(1, 0, 'B'), (0, 1, 'C'), (-1, 1, 'D'), (-1, 0, 'E'), (0, -1, 'F'), (1, -1, 'G')]
    # path to the co-channel cell: 2 steps along q, then 1 step turned 60 degrees
    path = [(2, 0), (2, 1)]
    for q, s in [(2, -1), (3, -1), (3, 0)]:
        x, y = pos(q, s); o.append(hexagon(x, y, r, 'var(--fig)', 'var(--line)', 1.5))
    x, y = pos(2, 0); o.append(hexagon(x, y, r, 'var(--fig)', L2, 1.5, '5 4'))
    x, y = pos(2, 1); o.append(hexagon(x, y, r, ACS, AC, 2.5))
    o.append(T(x, y + 6, 'A', 18, bold=True))
    o.append(T(x, y + 24, 'reuses', 12, fill=MUT))
    x, y = pos(0, 0); o.append(hexagon(x, y, r, ACS, AC, 2.5)); o.append(T(x, y + 6, 'A', 18, bold=True))
    for q, s, n in nb:
        x, y = pos(q, s); o.append(hexagon(x, y, r, PANEL, AC, 2)); o.append(T(x, y + 6, n, 17, bold=True))
    (ax, ay), (bx, by) = pos(0, 0), pos(2, 1)
    dx, dy = bx - ax, by - ay; dl = math.hypot(dx, dy)
    o.append(L(ax + dx / dl * 18, ay + dy / dl * 18, bx - dx / dl * 22, by - dy / dl * 22, NX, 2.5, arrow='x'))
    o.append(Tb((ax + bx) / 2 + 14, (ay + by) / 2 + 22, 'D', 15, fill=NX, bold=True))
    # step labels along the path
    # numbers panel
    X = 420
    rows = [('N = i² + ij + j²', '= 4 + 2 + 1 = 7 cells'), ('D = R √(3N)', '= √21 × 1 km = 4.58 km'), ('Q = D ÷ R', '= 4.58'),
            ('SIR = Q⁴ ÷ 6', '= 441 ÷ 6 = 73.5 → 18.66 dB'), ('channels per cell', '= 350 ÷ 7 = 50')]
    o.append(R(X - 12, 56, 304, 240, PANEL, L2, 8, 1.5))
    for i, (a, b) in enumerate(rows):
        o.append(T(X, 86 + i * 44, a, 14, 'start', bold=True))
        o.append(T(X + 8, 106 + i * 44, b, 14, 'start'))
    o.append(T(16, 330, 'Touching cells never share a group; the next A sits D = 4.58 km away (R = 1 km).', 14, 'start'))
    return 346, ''.join(o)
FIG[4] = (f4, 'Cell A and its six neighbours B to G make the seven-cell cluster. Two steps along a row and one step turned 60° reach the next cell that reuses group A, D = √21 R = 4.58 km away, which gives SIR 73.5 (18.66 dB) and 350 ÷ 7 = 50 channels per cell.',
          'A cluster of seven hexagons, A in the centre and B to G around it; an arrow labelled D reaches a second A hexagon outside the cluster; a panel lists N = 7, D = 4.58 km, Q = 4.58, SIR = 18.66 dB and 50 channels per cell.')


# ---- 1.5 hard handover messages, and the cost over one call ----
def f5():
    cols = [('MS', 'phone'), ('old BSS', ''), ('MSC + VLR', ''), ('new BSS', '')]
    xs = [80, 260, 450, 640]
    o = []
    for (n, s), x in zip(cols, xs):
        o.append(boxt(x - 62, 10, 124, 34, [n], PANEL, AC, 14, bold_first=True))
        o.append(L(x, 44, x, 360, L2, 1.5, '5 4'))
    msgs = [(0, 1, '1 measurement report', AC), (1, 2, '2 handover required', AC), (2, 3, '3 handover request', AC),
            (3, 2, '4 channel ready (ack)', AC), (2, 1, '5 handover command', NX), (1, 0, '5 handover command', NX),
            (0, 3, '6 handover access', LV), (3, 2, '7 handover complete', AC), (2, 1, '8 release old channel', MUT)]
    for i, (a, b, lab, c) in enumerate(msgs):
        y = 70 + i * 33
        sgn = 1 if b > a else -1
        arr = {AC: 'n', NX: 'x', LV: 'l', MUT: 'm'}[c]
        o.append(L(xs[a] + sgn * 3, y, xs[b] - sgn * 6, y, c if c != MUT else L2, 2, arrow=arr))
        mx = (xs[a] + xs[b]) / 2 if abs(b - a) == 1 else (xs[1] + xs[2]) / 2
        o.append(Tb(mx, y - 6, lab, 13))
    # the call
    y = 400
    o.append(T(16, y - 14, 'One 120 s call, crossing a cell boundary every 15 s', 15, 'start', bold=True))
    x0, x1 = 40, 680
    fx = lambda t: x0 + t / 120 * (x1 - x0)
    o.append(R(x0, y, x1 - x0, 22, ACS, AC, 3, 1.5))
    for k in range(1, 9):
        t = 15 * k if k < 8 else 119.4
        o.append(R(fx(t) - 2.5, y - 4, 5, 30, NX, NX, 1, 1))
        o.append(T(fx(t), y + 44, str(k), 13, fill=NX, bold=True))
    o.append(T(16, y + 70, '8 breaks × 60 ms = 480 ms = 0.48 s lost;  0.48 ÷ 120 = 0.004 = 0.4 % of the call', 14, 'start'))
    o.append(T(16, y + 90, '(the breaks are drawn wider than to scale so they can be seen)', 13, 'start', MUT))
    return y + 102, ''.join(o)
FIG[5] = (f5, 'The switch runs the handover: it reserves a channel in the new cell, sends the command through the old one, and releases the old channel once the phone reports in. Over a 120 s call with a crossing every 15 s, 8 breaks of 60 ms lose 480 ms, 0.4 % of the call.',
          'A message diagram with four columns, phone, old base station, switch with visitor register, and new base station, showing eight numbered handover messages; below, a 120 second call bar with eight marked breaks.')


# ---- 1.6 Mobile IP tunnel: 120 B becomes 140 B ----
def pkt(x, y, parts, sc, h=30):
    o = []
    for lab, n, f, s in parts:
        w = n * sc
        o.append(R(x, y, w, h, f, s, 3, 1.5)); o.append(T(x + w / 2, y + h / 2 + 5, lab, 13, bold=True)); x += w
    return ''.join(o), x


def f6():
    o = [T(16, 24, 'A packet for the home address, followed through the tunnel (bars to scale, 1 byte = 3 px)', 14, 'start', bold=True)]
    nodes = [(16, 'Correspondent', 'any host'), (178, 'Home agent', 'adds outer header'), (420, 'Foreign agent', 'removes it'),
             (582, 'Mobile node', 'gets 120 B')]
    for x, a, b in nodes:
        o.append(boxt(x, 44, 130, 52, [a, b], LVS if a == 'Mobile node' else PANEL, LV if a == 'Mobile node' else AC, 13, bold_first=True))
    o.append(L(148, 70, 174, 70, AC, 2, arrow='n'))
    o.append(R(310, 54, 108, 32, NXS, NX, 16, 2, '6 4'))
    o.append(L(314, 70, 414, 70, NX, 3, arrow='x'))
    o.append(T(364, 112, 'tunnel: 140 B', 13, fill=NX, bold=True))
    o.append(L(552, 70, 578, 70, AC, 2, arrow='n'))
    sc = 3
    y = 150
    o.append(T(16, y + 20, 'before', 14, 'start', MUT))
    s, e = pkt(100, y, [('IP 20', 20, PANEL, AC), ('payload 100 B', 100, ACS, AC)], sc)
    o.append(s); o.append(T(e + 10, y + 20, '120 B', 14, 'start', bold=True))
    y = 206
    o.append(T(16, y + 20, 'in tunnel', 14, 'start', NX))
    s, e = pkt(100, y, [('outer 20', 20, NXS, NX), ('IP 20', 20, PANEL, AC), ('payload 100 B', 100, ACS, AC)], sc)
    o.append(s); o.append(T(e + 10, y + 20, '140 B', 14, 'start', NX, True))
    y = 262
    o.append(T(16, y + 20, 'delivered', 14, 'start', LV))
    s, e = pkt(100, y, [('IP 20', 20, PANEL, AC), ('payload 100 B', 100, ACS, AC)], sc)
    o.append(s); o.append(T(e + 10, y + 20, '120 B', 14, 'start', bold=True))
    o.append(T(16, 330, 'Overhead = 20 ÷ 120 = 16.7 %.   On a 2 Mbps link: 140 × 8 = 1120 bits ÷ 2 000 000 bit/s = 0.56 ms.', 14, 'start'))
    return 346, ''.join(o)
FIG[6] = (f6, 'The home agent wraps the 120-byte datagram in a 20-byte outer header, so 140 bytes cross the tunnel; the foreign agent strips it and the mobile node gets the original 120 bytes. The overhead is 16.7 %, and 140 bytes take 0.56 ms at 2 Mbps.',
          'Four boxes, correspondent, home agent, foreign agent and mobile node, with a tunnel between the agents; below, three bars to scale: 120 bytes before, 140 bytes with an outer header in the tunnel, 120 bytes delivered.')


# ---- 1.7 airtime of one 802.11b frame ----
def f7():
    o = [T(16, 24, 'Airtime of one 1500-byte frame at 11 Mbps (to scale)', 15, 'start', bold=True)]
    x0, x1, y = 40, 680, 70
    sc = (x1 - x0) / 1.59
    o.append(R(x0, y, 1.09 * sc, 50, ACS, AC, 4))
    o.append(T(x0 + 1.09 * sc / 2, y + 22, 'DATA: 12 000 bits', 14, bold=True))
    o.append(T(x0 + 1.09 * sc / 2, y + 40, '12 000 ÷ 11 000 000 = 1.09 ms', 14))
    o.append(R(x0 + 1.09 * sc, y, 0.50 * sc, 50, NXS, NX, 4))
    o.append(T(x0 + 1.09 * sc + 0.25 * sc, y + 22, 'overhead', 14, bold=True))
    o.append(T(x0 + 1.09 * sc + 0.25 * sc, y + 40, '0.50 ms', 14))
    o.append(T(x0 + 1.09 * sc + 0.25 * sc, y + 72, 'preamble, ACK,', 13, fill=MUT))
    o.append(T(x0 + 1.09 * sc + 0.25 * sc, y + 88, 'DIFS, backoff', 13, fill=MUT))
    o.append(xaxis(x0, x1, y + 108, [0, 0.5, 1.0, 1.5], lambda v: x0 + v * sc, None, lambda v: f'{v} ms'))
    o.append(brace(x0, x1, y - 8, INK, up=True))
    o.append(Tb((x0 + x1) / 2, y - 14, 'one frame on air: 1.09 + 0.50 = 1.59 ms', 14, bold=True))
    # efficiency meter
    y2 = 240
    o.append(T(16, y2, 'Efficiency = useful time ÷ total time = 1.09 ÷ 1.59 = 68.6 %', 15, 'start', bold=True))
    o.append(R(x0, y2 + 16, x1 - x0, 26, PANEL, L2, 4, 1.5))
    o.append(R(x0, y2 + 16, 0.686 * (x1 - x0), 26, AC, AC, 4, 1.5))
    o.append(T(x0 + 0.686 * (x1 - x0) - 8, y2 + 34, '68.6 % carries data', 14, 'end', 'var(--fig)', True))
    o.append(T(x0 + 0.686 * (x1 - x0) + 8, y2 + 34, '31.4 % overhead', 14, 'start', NX, True))
    return y2 + 60, ''.join(o)
FIG[7] = (f7, 'The 1500-byte frame needs 1.09 ms of data time and 0.50 ms of preamble, ACK, DIFS and backoff, 1.59 ms in all, so only 68.6 % of the airtime carries data.',
          'A time bar to scale: a long data block of 1.09 ms followed by a shorter overhead block of 0.50 ms, total 1.59 ms; below, an efficiency bar filled to 68.6 percent.')


# ---- 1.8 route discovery A to D ----
def f8():
    P_ = {'A': (90, 190), 'B': (290, 100), 'C': (290, 280), 'D': (500, 100), 'E': (500, 280)}
    links = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E')]
    o = [T(16, 24, 'Route request floods out; the reply comes back by unicast', 15, 'start', bold=True)]
    for a, b in links:
        (x1, y1), (x2, y2) = P_[a], P_[b]
        o.append(L(x1, y1, x2, y2, 'var(--line)', 6))
    # RREQ arrows (dashed, next colour), numbered by transmission
    def off(a, b, d):
        (x1, y1), (x2, y2) = P_[a], P_[b]
        ln = math.hypot(x2 - x1, y2 - y1); nx, ny = -(y2 - y1) / ln * d, (x2 - x1) / ln * d
        ux, uy = (x2 - x1) / ln, (y2 - y1) / ln
        return x1 + nx + ux * 30, y1 + ny + uy * 30, x2 + nx - ux * 34, y2 + ny - uy * 34
    for a, b, n in [('A', 'B', '1'), ('A', 'C', '1'), ('B', 'D', '2'), ('C', 'E', '3')]:
        x1, y1, x2, y2 = off(a, b, -12)
        o.append(L(x1, y1, x2, y2, NX, 2, '6 4', 'x'))
    for a, b in [('A', 'B'), ('B', 'D')]:
        x1, y1, x2, y2 = off(b, a, -12)
        o.append(L(x1, y1, x2, y2, LV, 3, None, 'l'))
    # E's copy goes back to C and is dropped
    x1, y1, x2, y2 = off('E', 'C', -12)
    o.append(L(x1, y1, x2, y2, NX, 2, '6 4', 'x'))
    o.append(Tb(395, 316, 'E rebroadcasts; only C hears it and drops the duplicate', 13, fill=NX))
    for n, (x, y) in P_.items():
        dest = n == 'D'
        o.append(f'<circle cx="{x}" cy="{y}" r="26" style="fill:{ACS if n in "ABD" else PANEL};stroke:{LV if n in "ABD" else AC};stroke-width:{3 if n in "ABD" else 2}"/>')
        o.append(T(x, y + 6, n, 18, bold=True))
    o.append(T(90, 236, 'source', 13, fill=MUT)); o.append(T(500, 146, 'destination', 13, fill=MUT))
    o.append(Tb(180, 126, 'RREQ', 13, fill=NX, bold=True))
    o.append(Tb(395, 78, 'RREQ', 13, fill=NX, bold=True))
    o.append(Tb(395, 136, 'RREP', 13, fill=LV, bold=True))
    o.append(Tb(205, 182, 'RREP', 13, fill=LV, bold=True))
    # tally
    X = 566
    o.append(R(X - 8, 160, 160, 128, PANEL, L2, 8, 1.5))
    o.append(T(X, 184, 'broadcasts', 14, 'start', bold=True))
    o.append(T(X, 204, 'A, B, C, E = 4', 14, 'start', NX))
    o.append(T(X, 230, 'reply unicasts', 14, 'start', bold=True))
    o.append(T(X, 250, 'D→B, B→A = 2', 14, 'start', LV))
    o.append(T(X, 276, 'route A→B→D: 2 hops', 14, 'start', bold=True))
    return 336, ''.join(o)
FIG[8] = (f8, 'A, B, C and E each broadcast the route request once, 4 broadcasts in all; D hears it from B and answers by unicast to B, which forwards to A. The route found, A→B→D, is 2 hops, and C and E stay off it.',
          'Five nodes A to E; dashed arrows show the route request spreading from A to B and C, from B to D and from C to E; solid arrows show the reply from D to B to A; a box tallies 4 broadcasts, 2 unicasts and a 2-hop route.')


spec = make_spec(FIG)


def text_fixes(k):
    return {
        2: [('The figure places the main standards on a timeline.',
             'The figure puts the generations on a timeline and times one 5 MB song on 2G, 3G and 4G.')],
        4: [(' Only a few universities teach the Erlang and CDMA capacity comparison.', '')],
        6: [(' Only a few universities teach this chapter.', '')],
        8: [(' Only a few universities teach this chapter; the aim is route discovery, not the full protocol suite.',
             ' The aim here is route discovery, not the full protocol suite.')],
    }.get(k, [])


def drop_sources():
    # university-hosted pages: the books name no universities (NPTEL is hosted by the IITs)
    return ['nptel.ac.in']
