"""Claude's hand-drawn figures for c-cn-u3 (Computer Networks, unit 3: data link layer and medium access), one per
chapter, from each chapter's worked example."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def cell(x, y, w, h, s, c=INK, fill=PANEL, stroke=L2, size=15, bold=True, mono=True, sw=1.4, dash=None):
    o = R(x, y, w, h, fill, stroke, 3, sw, dash)
    o += (TM if mono else T)(x + w / 2, y + h / 2 + 5, s, size, fill=c, bold=bold)
    return o


# ---- 3.1 bit stuffing ----
def f1():
    o = []
    inp = '111111011111100'
    out = '11111010111110100'
    ins = {5, 13}
    x0, cw = 140, 33
    o.append(T(20, 26, 'After five 1s in a row the sender inserts a 0, so the data can never look like the flag 01111110', 14, 'start', bold=True))
    rows = [('input, 15 bits', 56), ('on the wire, 17 bits', 140), ('receiver output', 224)]
    for name, y in rows:
        o.append(T(x0 - 12, y + 22, name, 13, 'end', MUT, True))
    k = 0
    for j, b in enumerate(out):
        x = x0 + j * cw
        if j in ins:
            o.append(cell(x, 140, cw - 3, 34, b, LV, LVS, LV, 15, sw=2))
            o.append(T(x + cw / 2 - 1.5, 196, 'added', 13, fill=LV, bold=True))
        else:
            o.append(cell(x, 56, cw - 3, 34, inp[k], INK))
            o.append(L(x + cw / 2 - 1.5, 92, x + cw / 2 - 1.5, 138, LN, 1))
            o.append(cell(x, 140, cw - 3, 34, b, INK))
            o.append(cell(x, 224, cw - 3, 34, inp[k], NX, NXS, NX))
            k += 1
    for a in (0, 8):
        o.append(brace(x0 + a * cw, x0 + (a + 5) * cw - 3, 132, AC, up=True))
        o.append(T(x0 + (a + 2.5) * cw, 126, 'five 1s', 13, fill=AC, bold=True))
    o.append(T(20, 290, '15 bits + 2 inserted zeros = 17 bits. The receiver deletes the 0 after each five 1s and gets the 15 bits back.', 13, 'start', MUT))
    return 306, ''.join(o)
FIG[1] = (f1, 'After every run of five 1s the sender inserts a 0, so the 15 input bits become 17 on the wire; the two orange zeros are the inserted bits, and the receiver deletes them to recover the original 15.',
          'Three rows of bit cells: the 15 input bits spaced out, the 17 stuffed bits with two inserted zeros highlighted after each run of five 1s, and the receiver output equal to the input.')


# ---- 3.2 CRC by modulo-2 long division ----
def f2():
    o = []
    x0, cw, y0, rh = 150, 26, 60, 26
    def bits(y, start, s, c=INK, hot=None):
        for i, b in enumerate(s):
            col = c if not (hot and start + i in hot) else LV
            o.append(TM(x0 + (start + i) * cw, y, b, 17, fill=col, bold=True))
    o.append(T(20, 28, 'Divide 1001 with three 0s appended by G = 1011, using XOR', 14, 'start', bold=True))
    o.append(TM(x0 - 60, y0, '1011', 17, fill=AC, bold=True)); o.append(L(x0 - 30, y0 - 18, x0 - 30, y0 + 6, INK, 1.6))
    o.append(L(x0 - 30, y0 - 18, x0 + 7 * cw - 10, y0 - 18, INK, 1.6))
    bits(y0, 0, '1001000', INK, {4, 5, 6})
    steps = [(0, '1011', 'top bit 1: XOR 1011'), (1, '0000', 'top bit 0: XOR 0000'), (2, '1011', 'top bit 1: XOR 1011'), (3, '0000', 'top bit 0: XOR 0000')]
    rems = [(1, '0100'), (2, '1000'), (3, '0110')]
    y = y0
    for i, (st, g, note) in enumerate(steps):
        y += rh
        bits(y, st, g, AC)
        o.append(T(x0 + 7 * cw + 10, y, note, 13, 'start', AC))
        o.append(L(x0 + st * cw - 10, y + 7, x0 + (st + 4) * cw - 12, y + 7, INK, 1.4))
        y += rh
        if i < 3:
            s, r = rems[i]
            bits(y, s, r, INK)
            o.append(T(x0 + 7 * cw + 10, y, 'bring down the next bit', 13, 'start', MUT))
        else:
            bits(y, 4, '110', LV)
            o.append(T(x0 + 7 * cw + 10, y, 'remainder 110 = CRC', 14, 'start', LV, True))
    o.append(T(x0 + 7 * cw + 10, y0, 'three 0s appended', 13, 'start', LV, True))
    yb = y + 40
    o.append(T(20, yb, 'frame = data 1001 + CRC 110 =', 14, 'start'))
    for i, b in enumerate('1001110'):
        o.append(cell(232 + i * 28, yb - 20, 26, 28, b, LV if i >= 4 else INK, LVS if i >= 4 else PANEL, LV if i >= 4 else L2, 15))
    o.append(T(20, yb + 34, 'The receiver divides 1001110 by 1011: remainder 000, so it accepts the frame.', 14, 'start', NX, True))
    return yb + 52, ''.join(o)
FIG[2] = (f2, 'Three zeros are appended to 1001 and the result is divided by 1011 with XOR in place of subtraction. The remainder 110 is the CRC, so the frame is 1001110; dividing that by 1011 leaves 000 and the receiver accepts it.',
          'A modulo-2 long division of 1001000 by 1011, with XOR rows 1011, 0000, 1011, 0000 and remainder 110, followed by the frame 1001110 with its CRC bits highlighted.')


# ---- 3.3 Hamming(7,4) syndrome ----
def f3():
    o = []
    x0, cw = 170, 52
    names = ['p1', 'p2', 'd1', 'p4', 'd2', 'd3', 'd4']
    sent = '0110011'
    recv = '0110111'
    o.append(T(x0 - 12, 34, 'position', 13, 'end', MUT, True))
    for i in range(7):
        x = x0 + i * cw
        o.append(T(x + cw / 2 - 2, 34, f'{i + 1}', 14, fill=MUT, bold=True))
        o.append(T(x + cw / 2 - 2, 52, names[i], 13, fill=AC if names[i][0] == 'p' else MUT, bold=True))
    def row(y, label, s, hot=None):
        o.append(T(x0 - 12, y + 23, label, 13, 'end', INK, True))
        for i, b in enumerate(s):
            p = names[i][0] == 'p'
            if hot == i:
                o.append(cell(x0 + i * cw, y, cw - 4, 34, b, LV, LVS, LV, 16, sw=2.2))
            else:
                o.append(cell(x0 + i * cw, y, cw - 4, 34, b, AC if p else INK, ACS if p else PANEL, AC if p else L2, 16))
    row(62, 'sent', sent)
    row(104, 'received', recv, 4)
    o.append(T(x0 + 4 * cw + cw / 2 - 2, 158, 'flipped', 13, fill=LV, bold=True))
    checks = [('s1: 1, 3, 5, 7', [0, 2, 4, 6], '0+1+1+1 = 3, odd → 1'), ('s2: 2, 3, 6, 7', [1, 2, 5, 6], '1+1+1+1 = 4, even → 0'),
              ('s4: 4, 5, 6, 7', [3, 4, 5, 6], '0+1+1+1 = 3, odd → 1')]
    for r, (lab, cov, res) in enumerate(checks):
        y = 172 + r * 36
        o.append(T(x0 - 12, y + 19, lab, 13, 'end', NX, True))
        for i in range(7):
            if i in cov:
                o.append(R(x0 + i * cw + 8, y + 4, cw - 20, 22, NXS, NX, 11, 1.6))
                o.append(TM(x0 + i * cw + cw / 2 - 2, y + 20, recv[i], 14, fill=NX, bold=True))
        o.append(T(x0 + 7 * cw + 8, y + 20, res, 13, 'start', NX, True))
    o.append(T(20, 300, 'syndrome s4 s2 s1 = 1 0 1 = 5, so flip bit 5 back: 0110011, data 1011', 15, 'start', LV, True))
    return 318, ''.join(o)
FIG[3] = (f3, 'Data 1011 is sent as 0110011, with check bits at positions 1, 2 and 4. Bit 5 flips on the way; the three checks give s1 = 1, s2 = 0, s4 = 1, and the syndrome 101 = 5 names the bit to flip back.',
          'A seven-position table with the sent word 0110011 and the received word 0110111, bit 5 highlighted, and three parity-check rows over positions 1 3 5 7, 2 3 6 7 and 4 5 6 7 giving 1, 0, 1.')


# ---- 3.4 stop-and-wait against sliding windows ----
def f4():
    o = []
    x0, sc = 140, 5.0                 # 1 ms = 5 px
    fx = lambda t: x0 + t * sc
    lanes = [('stop-and-wait', 1, '20%'), ('window W = 3', 3, '60%'), ('window W = 5', 5, '100%')]
    for r, (name, W, u) in enumerate(lanes):
        y = 50 + r * 64
        o.append(T(x0 - 12, y + 24, name, 14, 'end', bold=True))
        o.append(R(fx(0), y, 100 * sc, 36, PANEL, LN, 2, 1))
        n = 0
        for start in (0, 50):
            for k in range(W):
                t = start + k * 10
                o.append(cell(fx(t), y, 10 * sc, 36, str(n), AC, ACS, AC, 14, mono=False))
                n += 1
        if W < 5:
            o.append(T(fx(W * 10 + (50 - W * 10) / 2), y + 24, 'idle', 13, fill=LV, bold=True))
        o.append(T(fx(100) + 10, y + 24, u, 15, 'start', NX if W == 5 else (LV if W == 1 else INK), True))
    o.append(L(fx(50), 40, fx(50), 248, LV, 1.8, '6 4'))
    o.append(T(fx(50), 32, 'ACK 0 arrives: 10 + 20 + 20 = 50 ms', 13, fill=LV, bold=True))
    o.append(xaxis(x0, fx(100), 250, [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], fx, 'time at the sender (ms)'))
    o.append(T(20, 324, 'Each frame takes 10 ms to send; a = 20 ÷ 10 = 2, so W = 1 + 2a = 5 frames keep the link busy.', 14, 'start', NX, True))
    return 340, ''.join(o)
FIG[4] = (f4, 'Frames take 10 ms and the one-way delay is 20 ms, so ACK 0 reaches the sender at 50 ms. Stop-and-wait sends one frame and idles 40 ms (20% use), W = 3 idles 20 ms (60%), and W = 5 never idles.',
          'Three sender timelines from 0 to 100 ms: stop-and-wait sending one 10 ms frame per 50 ms, a window of 3 sending three then idling, and a window of 5 sending continuously, with a dashed line at 50 ms for ACK 0.')


# ---- 3.5 Go-Back-N against Selective Repeat ----
def f5():
    o = []
    x0, cw = 170, 44
    seqs = [('Go-Back-N', [0, 1, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6], 7, '7 + 5 = 12 sends'),
            ('Selective Repeat', [0, 1, 2, 3, 4, 5, 2, 6], 6, '7 + 1 = 8 sends')]
    o.append(T(20, 26, 'Seven frames 0 to 6; frame 2 is damaged the first time', 14, 'start', bold=True))
    for r, (name, seq, first_re, tot) in enumerate(seqs):
        y = 60 + r * 110
        o.append(T(x0 - 12, y + 25, name, 14, 'end', bold=True))
        for i, f in enumerate(seq):
            x = x0 + i * cw
            if i == 2:
                o.append(cell(x, y, cw - 4, 38, str(f), MUT, PANEL, L2, 15, mono=False, dash='4 3'))
                o.append(L(x + 6, y + 6, x + cw - 10, y + 32, LV, 2)); o.append(L(x + cw - 10, y + 6, x + 6, y + 32, LV, 2))
            elif i >= first_re and not (name == 'Selective Repeat' and f == 6):
                o.append(cell(x, y, cw - 4, 38, str(f), LV, LVS, LV, 15, mono=False, sw=2))
            else:
                o.append(cell(x, y, cw - 4, 38, str(f), AC, ACS, AC, 15, mono=False))
        n_re = len(seq) - 7
        o.append(T(x0 - 12, y + 46, tot, 14, 'end', LV if n_re > 1 else NX, True))
        if name == 'Go-Back-N':
            o.append(brace(x0 + 7 * cw, x0 + 12 * cw - 4, y + 48, LV))
            o.append(T(x0 + 9.5 * cw, y + 72, 'timer for 2 expires: resend 2 to 6', 13, fill=LV, bold=True))
        else:
            o.append(T(x0 + 6.5 * cw - 2, y + 58, 'NAK 2: resend 2 only', 13, fill=LV, bold=True))
            o.append(T(x0 + 7.5 * cw - 2, y - 10, 'new', 13, fill=AC, bold=True))
    o.append(T(20, 300, 'Go-Back-N throws away 3 to 6 because its receiver keeps no buffer; Selective Repeat buffers them.', 13, 'start', MUT))
    return 316, ''.join(o)
FIG[5] = (f5, 'Frame 2 is damaged. Go-Back-N resends frames 2 to 6, 5 extra sends and 12 in all, while Selective Repeat resends only frame 2, 1 extra and 8 in all. Each cell is one frame sent; orange cells are resends.',
          'Two rows of frame cells: Go-Back-N sending 0 to 6 then 2 to 6 again, 12 cells; Selective Repeat sending 0 to 5, then 2 again, then 6, 8 cells; the damaged first copy of frame 2 crossed out.')


# ---- 3.6 PPP byte stuffing ----
def f6():
    o = []
    pay = [('7E', 'flag value', True, ['7D', '5E']), ('8A', 'ordinary byte', False, ['8A']),
           ('7D', 'escape value', True, ['7D', '5D']), ('11', 'below 0x20', True, ['7D', '31'])]
    o.append(T(20, 26, 'Escape rule: send 7D, then the byte XOR 20', 14, 'start', bold=True))
    o.append(T(100, 70, 'payload', 13, 'end', MUT, True)); o.append(T(100, 190, 'on the line', 13, 'end', MUT, True))
    xl = 112
    for i, (b, why, esc, outb) in enumerate(pay):
        xp = 130 + i * 150
        o.append(cell(xp, 50, 56, 34, b, LV if esc else INK, LVS if esc else PANEL, LV if esc else L2, 16))
        o.append(T(xp + 28, 104, why, 13, fill=LV if esc else MUT, bold=esc))
        w = 56 * len(outb) + 4 * (len(outb) - 1)
        o.append(L(xp + 28, 112, xl + w / 2, 166, L2, 1.6, arrow='m'))
        for j, ob in enumerate(outb):
            hot = esc and j == 0
            o.append(cell(xl + j * 60, 170, 56, 34, ob, NX if hot else INK, NXS if hot else PANEL, NX if hot else L2, 16))
        if esc:
            o.append(T(xl + w / 2, 226, f'{b} ⊕ 20 = {outb[1]}', 13, fill=NX, bold=True))
        xl += w + 22
    o.append(T(20, 270, '4 payload bytes + 3 escape bytes = 7 bytes on the line; overhead 7 ÷ 4 = 1.75', 14, 'start', NX, True))
    return 288, ''.join(o)
FIG[6] = (f6, 'The payload 7E 8A 7D 11 becomes seven bytes on the line: 7E, 7D and 11 are each sent as the escape 7D followed by the byte XOR 0x20, while 8A passes untouched, an overhead ratio of 7 ÷ 4 = 1.75.',
          'Four payload bytes 7E, 8A, 7D, 11 with arrows down to the line bytes 7D 5E, 8A, 7D 5D, 7D 31, the escape bytes highlighted and each XOR noted.')


# ---- 3.7 ALOHA throughput ----
def f7():
    x0, x1, y0, y1 = 80, 640, 40, 290
    fx = lambda g: x0 + g / 3 * (x1 - x0)
    fy = lambda s: y1 - s / 0.4 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [0, 0.5, 1, 1.5, 2, 2.5, 3], [0, 0.1, 0.2, 0.3, 0.4], fx, fy,
              'offered load G (frames per frame time)', 'throughput S', yfmt=lambda v: f'{v:.1f}')]
    gs = [i * 0.03 for i in range(101)]
    o.append(P([(fx(g), fy(g * math.exp(-g))) for g in gs], NX, 3))
    o.append(P([(fx(g), fy(g * math.exp(-2 * g))) for g in gs], LV, 3))
    o.append(C(fx(1), fy(0.3679), 7, NX)); o.append(C(fx(0.5), fy(0.1839), 7, LV))
    o.append(T(fx(1) + 12, fy(0.3679) - 8, 'slotted, G = 1: S = 1 × e⁻¹ = 0.368', 13, 'start', NX, True))
    o.append(T(fx(0.5) + 12, fy(0.1839) - 12, 'pure, G = 0.5: S = 0.5 × e⁻¹ = 0.184', 13, 'start', LV, True))
    o.append(T(fx(2.2), fy(0.29), 'S = G e^(−G)', 13, 'start', NX, True))
    o.append(T(fx(2.2), fy(0.06), 'S = G e^(−2G)', 13, 'start', LV, True))
    return 350, ''.join(o)
FIG[7] = (f7, 'Throughput against offered load for the two ALOHA rules. Pure ALOHA peaks at 0.184 when G = 0.5; slotted ALOHA, which halves the time a frame is open to collision, peaks at 0.368 when G = 1, exactly double.',
          'Two hump-shaped curves of throughput S against load G from 0 to 3: slotted ALOHA peaking at 0.368 at G = 1 and pure ALOHA peaking at 0.184 at G = 0.5.')


# ---- 3.8 the Ethernet frame, untagged and tagged ----
def f8():
    o = []
    def frame(y, fields):
        x = 20
        for name, size, c, f, w in fields:
            o.append(R(x, y, w, 48, f, c, 2, 1.6))
            o.append(T(x + w / 2, y + 20, name, 13, fill=c, bold=True))
            o.append(T(x + w / 2, y + 38, size, 13, fill=INK))
            x += w
        return x
    base = [('preamble', '7', L2, PANEL, 76), ('SFD', '1', L2, PANEL, 40), ('dest', '6', AC, ACS, 60), ('source', '6', AC, ACS, 66)]
    tail = [('type', '2', AC, ACS, 50), ('payload', '1500', NX, NXS, 230), ('FCS', '4', AC, ACS, 48)]
    o.append(T(20, 28, 'Untagged frame carrying a 1500-byte IP packet (sizes in bytes)', 14, 'start', bold=True))
    xe = frame(40, base + tail)
    o.append(brace(136, xe, 98, AC)); o.append(T((136 + xe) / 2, 122, 'frame: 6 + 6 + 2 + 1500 + 4 = 1518', 13, fill=AC, bold=True))
    o.append(T(20, 122, 'wire: 1526', 13, 'start', MUT, True))
    o.append(T(20, 166, 'With an 802.1Q VLAN tag after the source address', 14, 'start', bold=True))
    xe = frame(178, base + [('tag', '4', LV, LVS, 44)] + tail)
    o.append(T((136 + xe) / 2, 260, 'frame 1518 + 4 = 1522 (1530 on the wire)', 13, fill=LV, bold=True))
    o.append(T(20, 300, 'A 10-byte payload is padded with 36 bytes up to 46, so the shortest frame is 6 + 6 + 2 + 46 + 4 = 64 bytes.', 13, 'start', MUT, True))
    return 316, ''.join(o)
FIG[8] = (f8, 'The 1500-byte packet gives a 1518-byte frame, 1526 bytes on the wire with the preamble and SFD. The 4-byte 802.1Q tag goes after the source address and makes the frame 1522 bytes; a 10-byte payload is padded to the 64-byte minimum.',
          'Two Ethernet frame bars of fields preamble 7, SFD 1, destination 6, source 6, type 2, payload 1500, FCS 4, the second with a 4-byte VLAN tag inserted after the source, with totals 1518 and 1522.')


# ---- 3.9 802.11 DCF timing ----
def f9():
    o = []
    x0, sc = 30, 0.72                     # 1 us = 0.72 px
    fx = lambda t: x0 + t * sc
    y = 110
    o.append(T(20, 26, 'The medium goes idle at 0 μs; the station has a 1000-byte frame at 11 Mbps', 14, 'start', bold=True))
    o.append(R(fx(0), y, 50 * sc, 44, PANEL, L2, 2, 1.6))
    for k in range(5):
        o.append(R(fx(50 + k * 20), y, 20 * sc, 44, LVS, LV, 1, 1.4))
    o.append(R(fx(150), y, 727.27 * sc, 44, ACS, AC, 2, 1.6))
    o.append(T(fx(150 + 727.27 / 2), y + 20, 'data frame', 14, fill=AC, bold=True))
    o.append(T(fx(150 + 727.27 / 2), y + 38, '8000 bits ÷ 11 Mbps = 727.27 μs', 13, fill=AC))
    o.append(R(fx(877.27), y, 10 * sc, 44, PANEL, L2, 1, 1.4))
    o.append(R(fx(887.27), y, 12, 44, NXS, NX, 1, 1.6))
    o.append(T(fx(0), y - 10, 'DIFS 50', 13, 'start', MUT, True))
    o.append(T(fx(50), y - 34, 'backoff 5 × 20 = 100', 13, 'start', LV, True))
    o.append(T(fx(882), y - 34, 'SIFS 10', 13, 'end', MUT, True))
    o.append(L(fx(882), y - 28, fx(882), y - 2, L2, 1.4))
    o.append(T(fx(887.27) + 16, y + 26, 'ACK', 13, 'start', NX, True))
    o.append(xaxis(x0, fx(900), y + 64, [0, 150, 300, 450, 600, 750, 887.27], fx, 'time since the medium went idle (μs)',
                   lambda v: '887.27' if v > 887 else str(v)))
    o.append(T(20, y + 144, 'wait 50 + 100 = 150 μs;  ACK starts at 150 + 727.27 + 10 = 887.27 μs', 14, 'start', NX, True))
    return y + 162, ''.join(o)
FIG[9] = (f9, 'The station waits DIFS 50 μs plus 5 backoff slots of 20 μs, 150 μs in all, then sends its 727.27 μs frame; the ACK starts one SIFS of 10 μs later, at 887.27 μs.',
          'A timeline from 0 to about 900 μs: DIFS 50 μs, five 20 μs backoff slots, a 727.27 μs data frame, a 10 μs SIFS and the ACK starting at 887.27 μs.')


spec = make_spec(FIG)
