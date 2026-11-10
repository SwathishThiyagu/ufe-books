"""Claude's hand-drawn figures for c-cn-u5 (Computer Networks, unit 5: transport layer: ports, UDP, TCP, flow and
congestion control, QoS and SCTP), one per chapter, from each chapter's worked example."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def cell(x, y, w, h, s, c=INK, fill=PANEL, stroke=L2, size=14, bold=True, sw=1.4, dash=None):
    return R(x, y, w, h, fill, stroke, 3, sw, dash) + T(x + w / 2, y + h / 2 + 5, s, size, fill=c, bold=bold)


# ---- 5.1 demultiplexing on the four-tuple ----
def f1():
    o = []
    o.append(R(20, 40, 210, 190, PANEL, L2, 10, 1.6))
    o.append(T(125, 62, 'client 203.0.113.7', 14, fill=INK, bold=True))
    o.append(boxt(40, 80, 170, 52, ['browser 1', 'source port 52000'], ACS, AC, 13, bold_first=True))
    o.append(boxt(40, 160, 170, 52, ['browser 2', 'source port 52001'], NXS, NX, 13, bold_first=True))
    o.append(R(490, 40, 210, 190, PANEL, L2, 10, 1.6))
    o.append(T(595, 62, 'server 192.0.2.10:80', 14, fill=INK, bold=True))
    o.append(boxt(510, 80, 170, 52, ['socket for', 'connection 1'], ACS, AC, 13, bold_first=True))
    o.append(boxt(510, 160, 170, 52, ['socket for', 'connection 2'], NXS, NX, 13, bold_first=True))
    o.append(L(212, 106, 506, 106, AC, 2.4, arrow='n')); o.append(L(212, 186, 506, 186, NX, 2.4, arrow='x'))
    o.append(T(360, 98, 'to 192.0.2.10:80', 13, fill=AC, bold=True)); o.append(T(360, 178, 'to 192.0.2.10:80', 13, fill=NX, bold=True))
    o.append(T(20, 266, 'Four-tuple (source IP, source port, destination IP, destination port):', 14, 'start', bold=True))
    o.append(TM(40, 292, '(203.0.113.7, 52000, 192.0.2.10, 80)', 15, 'start', AC, True))
    o.append(TM(40, 318, '(203.0.113.7, 52001, 192.0.2.10, 80)', 15, 'start', NX, True))
    o.append(T(470, 305, '← only the source', 13, 'start', LV, True)); o.append(T(486, 323, 'port differs', 13, 'start', LV, True))
    return 338, ''.join(o)
FIG[1] = (f1, 'Both browsers on 203.0.113.7 send to the same server address 192.0.2.10:80, so the destination half of the four-tuple is the same. The server tells the two connections apart only by the source ports 52000 and 52001.',
          'A client host with two browsers on source ports 52000 and 52001 sending to the server 192.0.2.10 port 80, which hands each segment to its own socket, with the two four-tuples written below.')


# ---- 5.2 the UDP header and the MTU budget ----
def f2():
    o = [T(20, 26, 'UDP header: four 16-bit fields, 8 bytes, then the data', 14, 'start', bold=True)]
    x0, w = 60, 300
    o.append(cell(x0, 44, w, 40, 'source port (16 bits)', INK, PANEL, L2, 13))
    o.append(cell(x0 + w, 44, w, 40, 'destination port 53 (DNS)', AC, ACS, AC, 13))
    o.append(cell(x0, 84, w, 40, 'length = 8 + 40 = 48', LV, LVS, LV, 14))
    o.append(cell(x0 + w, 84, w, 40, 'checksum (16 bits)', INK, PANEL, L2, 13))
    o.append(cell(x0, 124, 2 * w, 40, 'DNS query data: 40 bytes', NX, NXS, NX, 14))
    o.append(T(x0 - 10, 90, '8 bytes', 13, 'end', MUT, True))
    o.append(T(20, 202, 'Largest payload in one 1500-byte MTU, without IP fragmentation', 14, 'start', bold=True))
    sc = 0.38
    x = 40
    for lab, n, c, f, show in (('IP 20', 20, MUT, PANEL, True), ('UDP 8', 8, LV, LVS, True), ('UDP payload 1472 bytes', 1472, NX, NXS, True)):
        wpx = max(n * sc, 40)
        o.append(cell(x, 216, wpx, 40, lab, c, f, c if c != MUT else L2, 13))
        x += wpx
    o.append(brace(40, x, 266, INK))
    o.append(T((40 + x) / 2, 290, 'MTU 1500 = 20 + 8 + 1472', 14, fill=INK, bold=True))
    return 306, ''.join(o)
FIG[2] = (f2, 'The length field of the 40-byte DNS query reads 48, because it counts the 8-byte header too. In a 1500-byte MTU the IPv4 header takes 20 bytes and the UDP header 8, leaving 1472 bytes of payload.',
          'The UDP header as four fields, source port, destination port 53, length 48 and checksum, over 40 bytes of data; below, a 1500-byte MTU bar split into IP 20, UDP 8 and payload 1472.')


# ---- 5.3 sequence numbers count bytes ----
def f3():
    o = [T(20, 26, 'The sender’s bytes are numbered from 5000; each segment’s sequence number is its first byte', 14, 'start', bold=True)]
    x0, sc = 40, 0.24                     # 1 byte = 0.24 px, 2500 = 600 px
    fx = lambda b: x0 + (b - 5000) * sc
    segs = [(5000, 1000, AC, ACS), (6000, 1000, NX, NXS), (7000, 500, LV, LVS)]
    for i, (a, n, c, f) in enumerate(segs):
        o.append(R(fx(a), 60, n * sc, 46, f, c, 2, 2))
        o.append(T(fx(a + n / 2), 80, f'segment {i + 1}', 13, fill=c, bold=True))
        o.append(T(fx(a + n / 2), 98, f'{n} bytes', 13, fill=c))
        o.append(L(fx(a), 110, fx(a), 128, c, 1.8))
        o.append(T(fx(a), 146, f'seq {a}', 14, 'start', c, True))
    o.append(L(fx(7500), 56, fx(7500), 112, INK, 1.8, '4 3'))
    o.append(T(fx(7500), 50, 'ACK 7500 = next byte expected', 13, 'end', INK, True))
    o.append(T(20, 202, '5000 + 1000 = 6000,  5000 + 2000 = 7000,  5000 + 2500 = 7500', 14, 'start', INK, True))
    o.append(T(20, 240, 'Header with a 4-byte MSS option:', 14, 'start', bold=True))
    for k in range(6):
        o.append(cell(270 + k * 66, 222, 62, 30, f'word {k + 1}', AC if k < 5 else LV, ACS if k < 5 else LVS, AC if k < 5 else LV, 13))
    o.append(T(20, 280, '20 fixed bytes + 4 option bytes = 24 bytes = 6 words of 4 bytes, so data offset = 6', 14, 'start', LV, True))
    return 298, ''.join(o)
FIG[3] = (f3, 'Sequence numbers count bytes: the three segments of 1000, 1000 and 500 bytes start at 5000, 6000 and 7000, and the receiver’s ACK 7500 names the next byte it expects. A 24-byte header gives data offset 6.',
          'A byte line from 5000 split into segments of 1000, 1000 and 500 bytes labelled seq 5000, 6000 and 7000, with ACK 7500 at the end, and a header of six 4-byte words.')


# ---- 5.4 handshake, data and close ----
def f4():
    o = []
    xc, xs = 140, 580
    o.append(boxt(xc - 70, 14, 140, 34, ['client'], ACS, AC, 14, bold_first=True))
    o.append(boxt(xs - 70, 14, 140, 34, ['server'], NXS, NX, 14, bold_first=True))
    msgs = [('c', 'SYN  seq 2000', AC), ('s', 'SYN+ACK  seq 5000, ack 2001', NX), ('c', 'ACK  ack 5001', AC),
            ('c', 'data  seq 2001, 1000 bytes', AC), ('s', 'ACK  ack 3001', NX), ('c', 'FIN  seq 3001', LV),
            ('s', 'ACK  ack 3002', NX), ('s', 'FIN  seq 5001', LV), ('c', 'ACK  ack 5002', AC)]
    y = 66
    dy = 34
    o.append(L(xc, 48, xc, 66 + 9 * dy + 12, L2, 1.4, '4 4')); o.append(L(xs, 48, xs, 66 + 9 * dy + 12, L2, 1.4, '4 4'))
    for who, lab, c in msgs:
        a, b = (xc, xs) if who == 'c' else (xs, xc)
        ar = {AC: 'n', NX: 'x', LV: 'l'}[c]
        o.append(L(a, y, b + (-6 if b > a else 6), y + 22, c, 2, arrow=ar))
        o.append(Tb((xc + xs) / 2, y + 8, lab, 13, fill=c, bold=True))
        y += dy
    o.append(T(xc - 14, 66 + 11, 'uses 1 number', 13, 'end', LV, True))
    o.append(T(xc - 14, 66 + 5 * dy + 11, 'uses 1 number', 13, 'end', LV, True))
    o.append(T(xc - 14, 66 + 3 * dy + 11, '2001–3000', 13, 'end', AC, True))
    return 66 + 9 * dy + 22, ''.join(o)
FIG[4] = (f4, 'The client’s SYN uses sequence number 2000, so the server acknowledges 2001; 1000 data bytes take 2001 to 3000; the FIN at 3001 is acknowledged with 3002. SYN and FIN each use up one number though they carry no data.',
          'A two-column sequence diagram of nine segments between client and server: SYN 2000, SYN+ACK 5000/2001, ACK 5001, data 2001, ACK 3001, FIN 3001, ACK 3002, FIN 5001, ACK 5002.')


# ---- 5.5 the advertised window ----
def f5():
    o = [T(20, 26, 'The receiver’s 8000-byte buffer at three moments; rwnd = free space, sent in every ACK', 14, 'start', bold=True)]
    sc = 0.055                                      # 8000 bytes = 440 px
    rows = [('(a)', 3000, 'rwnd = 8000 − 3000 = 5000', AC, 'sender may send 5000 more'),
            ('(b)', 8000, 'rwnd = 0', LV, 'sender stops, persist timer, 1-byte probe'),
            ('(c)', 0, 'rwnd = 8000', NX, 'app read everything: window update, resume')]
    for r, (tag, used, lab, c, note) in enumerate(rows):
        y = 50 + r * 84
        o.append(T(32, y + 24, tag, 14, 'middle', INK, True))
        o.append(R(60, y, 8000 * sc, 36, PANEL, L2, 3, 1.6))
        if used:
            o.append(R(60, y, used * sc, 36, ACS if used < 8000 else LVS, AC if used < 8000 else LV, 3, 1.6))
            o.append(T(60 + used * sc / 2, y + 23, f'{used} waiting', 13, fill=AC if used < 8000 else LV, bold=True))
        if used < 8000:
            o.append(T(60 + (used + 8000) * sc / 2, y + 23, f'{8000 - used} free', 13, fill=MUT, bold=True))
        o.append(T(512, y + 23, lab, 14, 'start', c, True))
        o.append(T(60, y + 56, note, 13, 'start', MUT))
    return 300, ''.join(o)
FIG[5] = (f5, 'The window travels in every ACK: with 3000 bytes waiting the receiver advertises 5000; once the buffer is full it advertises 0 and the sender stops and probes; after the application reads all 8000 bytes it advertises 8000 again.',
          'Three buffer bars of 8000 bytes: 3000 waiting and 5000 free with rwnd 5000; full with rwnd 0; empty with rwnd 8000.')


# ---- 5.6 Reno congestion window ----
def f6():
    x0, x1, y0, y1 = 70, 640, 40, 290
    fx = lambda r: x0 + (r - 0.5) / 12 * (x1 - x0)
    fy = lambda c: y1 - c / 14 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, list(range(1, 13)), [0, 2, 4, 6, 8, 10, 12, 14], fx, fy, 'round trip', 'cwnd (MSS)')]
    cw = [1, 2, 4, 8, 9, 10, 11, 12, 6, 7, 8, 9]
    o.append(P([(fx(0.5), fy(8)), (fx(8.5), fy(8))], LV, 2, '6 4'))
    o.append(P([(fx(8.5), fy(6)), (fx(12.5), fy(6))], LV, 2, '6 4'))
    o.append(T(fx(0.7), fy(8) - 8, 'ssthresh 8', 13, 'start', LV, True))
    o.append(T(fx(12.4), fy(6) + 18, 'ssthresh 12 ÷ 2 = 6', 13, 'end', LV, True))
    o.append(P([(fx(r + 1), fy(c)) for r, c in enumerate(cw[:8])], AC, 3))
    o.append(P([(fx(r + 9), fy(c)) for r, c in enumerate(cw[8:])], AC, 3))
    o.append(L(fx(8), fy(12), fx(9), fy(6), LV, 1.8, '3 3', arrow='l'))
    for r, c in enumerate(cw):
        o.append(C(fx(r + 1), fy(c), 6, AC))
        o.append(T(fx(r + 1) + (12 if r == 8 else 0), fy(c) + (22 if r == 8 else -12), str(c), 13, fill=AC, bold=True))
    o.append(T(fx(2.5), fy(11), 'slow start: doubles', 13, 'middle', AC, True))
    o.append(T(fx(6.5), fy(13.6), '+1 per round', 13, 'middle', AC, True))
    o.append(T(fx(9.2), fy(11.2), '3 duplicate ACKs: halve to 6', 13, 'start', LV, True))
    return 350, ''.join(o)
FIG[6] = (f6, 'The congestion window doubles from 1 to 8 MSS, then grows by one MSS a round to 12. Three duplicate ACKs after round 8 halve it to 6 MSS instead of restarting at 1, and the threshold falls from 8 to 6.',
          'A plot of cwnd over rounds 1 to 12: 1, 2, 4, 8, then 9, 10, 11, 12, a drop to 6, then 7, 8, 9, with dashed ssthresh lines at 8 and then 6.')


# ---- 5.7 token bucket ----
def f7():
    o = []
    # bucket
    o.append(P([(60, 80), (60, 220), (200, 220), (200, 80)], AC, 3))
    o.append(R(62, 120, 136, 98, ACS, ACS, 0, 0))
    o.append(T(130, 175, '16 000 bits', 14, fill=AC, bold=True)); o.append(T(130, 194, 'full at t = 0', 13, fill=AC))
    o.append(T(130, 46, 'tokens in at r = 2 Mbps', 13, fill=NX, bold=True))
    o.append(L(130, 54, 130, 108, NX, 2.2, '4 3', arrow='x'))
    o.append(T(130, 244, 'depth b = 16 000 bits', 13, fill=AC, bold=True))
    o.append(T(130, 262, '= largest burst, 2000 bytes', 13, fill=MUT))
    # zoomed plot of bits allowed over the first 16 ms
    x0, x1, y0, y1 = 300, 660, 50, 250
    fx = lambda t: x0 + t / 16 * (x1 - x0)
    fy = lambda b: y1 - b / 50000 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 4, 8, 12, 16], [0, 16000, 32000, 48000], fx, fy, 'time t (ms), first 16 ms', 'bits the flow may send',
                  yfmt=lambda v: f'{v:,}'.replace(',', ' ')))
    o.append(L(fx(0), fy(16000), fx(16), fy(48000), AC, 3))
    o.append(L(fx(0), fy(0), fx(16), fy(32000), L2, 2.4, '6 4'))
    o.append(T(fx(9), fy(37000), 'bucket: b + r t', 13, 'end', AC, True))
    o.append(T(fx(10), fy(15000), 'plain 2 Mbps: r t', 13, 'start', MUT, True))
    o.append(L(fx(16) + 10, fy(48000), fx(16) + 10, fy(32000), LV, 2))
    o.append(T(fx(16) + 16, fy(40000) + 5, '16 000', 13, 'start', LV, True))
    o.append(T(20, 316, 'At t = 4 s: 16 000 + 2 000 000 × 4 = 8 016 000 bits, exactly 16 000 more than the plain limiter’s 8 000 000.', 13, 'start', INK, True))
    return 332, ''.join(o)
FIG[7] = (f7, 'The bucket starts full, so the flow can send 16 000 bits at once, then earns tokens at 2 Mbps. Its line stays 16 000 bits above a plain 2 Mbps limiter, so at t = 4 s it may have sent 8 016 000 bits against 8 000 000.',
          'Left, a bucket of depth 16 000 bits filling at 2 Mbps; right, the first 16 ms of allowed bits, a bucket line starting at 16 000 parallel to a dashed plain-limiter line starting at 0.')


# ---- 5.8 SCTP chunks and failover ----
def f8():
    o = [T(20, 26, 'Room per packet: 1500 − 20 IP − 12 common header − 16 DATA chunk header = 1452 bytes', 14, 'start', bold=True)]
    o.append(cell(30, 46, 660, 32, 'one 3000-byte message', INK, PANEL, L2, 13))
    sc = 0.2
    xs = [30, 30 + 1452 * sc, 30 + 2904 * sc]
    for i, (n, x) in enumerate(zip([1452, 1452, 96], xs)):
        o.append(cell(x, 96, max(n * sc, 80) - 2, 32, f'TSN {i + 1}: {n}', LV if i == 1 else AC, LVS if i == 1 else ACS, LV if i == 1 else AC, 13))
    o.append(boxt(20, 190, 120, 70, ['sender'], PANEL, INK, 14, bold_first=True))
    o.append(boxt(580, 190, 120, 70, ['receiver'], PANEL, INK, 14, bold_first=True))
    o.append(L(142, 206, 576, 206, AC, 2.2, arrow='n')); o.append(T(300, 198, 'primary path 10.0.0.1', 13, fill=AC, bold=True))
    o.append(L(142, 246, 576, 246, NX, 2.2, arrow='x')); o.append(T(360, 272, 'backup path 10.0.0.2', 13, fill=NX, bold=True))
    o.append(T(250, 232, 'TSN 1 ✓', 13, fill=AC, bold=True))
    o.append(L(470, 196, 490, 216, LV, 3)); o.append(L(490, 196, 470, 216, LV, 3)); o.append(T(480, 232, 'TSN 2 lost', 13, 'middle', LV, True))
    o.append(T(360, 240, 'TSN 2 resent', 13, 'end', NX, True))
    o.append(T(20, 306, 'Three chunks: 1452 + 1452 + 96 = 3000. After the loss 10.0.0.1 is marked inactive until heartbeats get answered.', 13, 'start', MUT, True))
    return 322, ''.join(o)
FIG[8] = (f8, 'The 3000-byte message splits into DATA chunks of 1452, 1452 and 96 bytes. TSN 2 is lost on the primary path 10.0.0.1, so SCTP resends it on the backup 10.0.0.2 and marks the primary inactive.',
          'A 3000-byte message cut into three chunks TSN 1, 2, 3 of 1452, 1452 and 96 bytes, and a sender and receiver joined by a primary path where TSN 2 is lost and a backup path that carries it again.')


spec = make_spec(FIG)
