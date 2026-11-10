"""Claude's hand-drawn figures for c-cn-u6 (Computer Networks, unit 6: application layer and security), one per chapter,
from each chapter's worked example."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def seg(x, y, w, h, fill, c, label, size=13, fc=None):
    o = R(x, y, w, h, fill, c, 3, 1.6)
    if label: o += T(x + w / 2, y + h / 2 + 5, label, size, fill=fc or c, bold=True)
    return o


# ---- 6.1 client-server against peer-to-peer distribution ----
def f1():
    o = [T(20, 26, 'A 10 Mbit file to 3 peers: server uploads 2 Mbps, each peer uploads 1 Mbps', 14, 'start', bold=True)]
    x0, sc = 150, 34                     # 1 s = 34 px
    fx = lambda t: x0 + t * sc
    y1, y2 = 60, 150
    o.append(T(x0 - 12, y1 + 25, 'client-server', 14, 'end', bold=True))
    for k in range(3):
        o.append(seg(fx(k * 5), y1, 5 * sc, 38, ACS, AC, f'copy {k + 1}: 10 ÷ 2 = 5 s'))
    o.append(T(fx(15) + 8, y1 + 25, '15 s', 15, 'start', AC, True))
    o.append(T(x0 - 12, y2 + 25, 'peer-to-peer', 14, 'end', bold=True))
    o.append(seg(fx(0), y2, 6 * sc, 38, NXS, NX, '30 Mbit ÷ 5 Mbps'))
    o.append(T(fx(6) + 8, y2 + 25, '6 s', 15, 'start', NX, True))
    o.append(T(fx(6) + 50, y2 + 16, 'swarm upload = 2 + 3 × 1 = 5 Mbps', 13, 'start', NX))
    o.append(T(fx(6) + 50, y2 + 34, 'peers serve each other too', 13, 'start', MUT))
    o.append(xaxis(x0, fx(16), 220, [0, 5, 6, 10, 15], fx, 'time (s)'))
    o.append(T(20, 294, 'Client-server: max(3 × 10 ÷ 2, 10 ÷ 2) = 15 s.   P2P: max(10 ÷ 2, 10 ÷ 2, 30 ÷ 5) = 6 s, 9 s sooner.', 13, 'start', INK, True))
    return 310, ''.join(o)
FIG[1] = (f1, 'The server alone must send three 10 Mbit copies at 2 Mbps, 5 s each, so client-server finishes at 15 s. In peer-to-peer the peers upload too: 30 Mbit moves at 2 + 3 × 1 = 5 Mbps and finishes at 6 s.',
          'Two timelines: client-server with three 5 s copies ending at 15 s, and peer-to-peer with one 6 s bar of 30 Mbit at 5 Mbps.')


# ---- 6.2 listening socket, connected socket and segments ----
def f2():
    o = []
    o.append(boxt(20, 40, 200, 56, ['client socket', '192.168.1.7:50000'], ACS, AC, 14, bold_first=True))
    o.append(boxt(500, 20, 200, 52, ['listening socket', '10.0.0.5:80'], PANEL, L2, 14, bold_first=True))
    o.append(boxt(500, 110, 200, 56, ['new socket from accept()', '10.0.0.5:80'], NXS, NX, 14, bold_first=True))
    o.append(L(222, 60, 496, 46, L2, 2, '5 4', arrow='m'))
    o.append(T(360, 40, 'connect()', 13, fill=MUT, bold=True))
    o.append(L(600, 74, 600, 106, NX, 2, arrow='x'))
    o.append(T(610, 96, 'accept()', 13, 'start', NX, True))
    o.append(L(222, 80, 496, 132, AC, 2.6, arrow='n'))
    o.append(T(350, 128, '5000 bytes of data', 13, fill=AC, bold=True))
    o.append(T(20, 210, 'MSS 1500: the 5000 bytes go as 4 segments', 14, 'start', bold=True))
    sc = 0.09
    x = 20
    for k, n in enumerate([1500, 1500, 1500, 500]):
        o.append(seg(x, 224, n * sc, 36, ACS if k < 3 else LVS, AC if k < 3 else LV, f'{n}'))
        x += n * sc + 4
    o.append(T(x + 6, 248, '3 × 1500 + 500 = 5000', 13, 'start', INK, True))
    o.append(T(20, 296, 'client pair (192.168.1.7:50000, 10.0.0.5:80); server pair (10.0.0.5:80, 192.168.1.7:50000)', 13, 'start', MUT, True))
    return 312, ''.join(o)
FIG[2] = (f2, 'accept() returns a new socket that keeps port 80, while the listening socket never carries data. The client’s 5000 bytes cross on the new socket as three segments of 1500 bytes and one of 500, four in all.',
          'A client socket 192.168.1.7:50000 connecting to a listening socket 10.0.0.5:80, which hands it to a new socket from accept(); below, four segments of 1500, 1500, 1500 and 500 bytes.')


# ---- 6.3 resolving www.example.com ----
def f3():
    o = []
    o.append(boxt(20, 110, 120, 50, ['host', 'empty cache'], PANEL, L2, 13, bold_first=True))
    o.append(boxt(230, 110, 130, 50, ['local resolver'], ACS, AC, 14, bold_first=True))
    servers = [('root server', 40), ('com server', 120), ('example.com', 200)]
    for i, (n, y) in enumerate(servers):
        o.append(boxt(540, y, 160, 46, [n], NXS, NX, 14, bold_first=True))
        q, a = 2 * i + 1, 2 * i + 2
        yy = y + 23
        o.append(L(362, 128 + (i - 1) * 6, 536, yy - 6, NX, 2, arrow='x'))
        o.append(L(536, yy + 6, 362, 142 + (i - 1) * 6, AC, 1.6, '5 4', arrow='n'))
        o.append(T(452, (128 + yy) / 2 - 10 + (i - 1) * 4, f'{q}, {a}', 13, fill=NX, bold=True))
    o.append(L(142, 128, 226, 128, AC, 2.2, arrow='n')); o.append(L(226, 144, 142, 144, AC, 2.2, '5 4', arrow='n'))
    o.append(T(184, 104, 'recursive', 13, fill=AC, bold=True))
    o.append(T(452, 270, 'iterative: 3 servers × (query + reply) = 6 messages', 13, fill=NX, bold=True))
    # TTL bar
    y = 300
    x0, sc = 140, 1.3
    o.append(T(20, y + 22, 'cache, TTL 300 s', 13, 'start', MUT, True))
    o.append(R(x0, y, 300 * sc, 34, ACS, AC, 3, 1.6))
    o.append(T(x0 + 150 * sc, y + 22, 'answer cached', 13, fill=AC, bold=True))
    for t, lab, c in ((200, 'ask at 200 s: 0 messages', AC), (300, 'ask at 300 s: expired, 6 again', LV)):
        o.append(L(x0 + t * sc, y - 6, x0 + t * sc, y + 46, c, 2))
    o.append(T(x0 + 200 * sc, y + 64, 'at 200 s: 100 s left, 0 messages', 13, 'end', AC, True))
    o.append(T(x0 + 300 * sc + 6, y + 64, 'at 300 s: expired, 6 again', 13, 'start', LV, True))
    return y + 80, ''.join(o)
FIG[3] = (f3, 'The host asks its resolver once, recursively; the resolver then contacts the root, com and example.com servers in turn, one query and one reply each, 6 messages. The answer is cached for 300 s: at 200 s a repeat costs nothing, at 300 s it costs 6 again.',
          'A host sending one recursive query to its resolver, which exchanges queries and replies with the root, com and example.com servers, numbered 1 to 6, above a 300 s cache bar with marks at 200 s and 300 s.')


# ---- 6.4 non-persistent against persistent HTTP ----
def f4():
    o = [T(20, 26, 'Base page + 3 images; each block is one 100 ms round trip', 14, 'start', bold=True)]
    x0, sc = 150, 0.6                   # 1 ms = 0.6 px, 800 ms = 480 px
    fx = lambda t: x0 + t * sc
    y1, y2 = 60, 150
    o.append(T(x0 - 12, y1 + 25, 'HTTP/1.0', 14, 'end', bold=True))
    o.append(T(x0 - 12, y1 + 43, 'non-persistent', 13, 'end', MUT))
    labs = ['TCP', 'base', 'TCP', 'img 1', 'TCP', 'img 2', 'TCP', 'img 3']
    for k, lab in enumerate(labs):
        t = lab == 'TCP'
        o.append(seg(fx(k * 100), y1, 100 * sc, 38, LVS if t else ACS, LV if t else AC, lab))
    o.append(T(fx(800) + 8, y1 + 25, '800 ms', 14, 'start', LV, True))
    o.append(T(x0 - 12, y2 + 25, 'HTTP/1.1', 14, 'end', bold=True))
    o.append(T(x0 - 12, y2 + 43, 'persistent', 13, 'end', MUT))
    for k, lab in enumerate(['TCP', 'base', '3 images']):
        t = lab == 'TCP'
        o.append(seg(fx(k * 100), y2, 100 * sc, 38, LVS if t else NXS, LV if t else NX, lab))
    o.append(T(fx(300) + 8, y2 + 25, '300 ms', 14, 'start', NX, True))
    o.append(T(fx(300) + 70, y2 + 25, 'images requested back to back', 13, 'start', MUT))
    o.append(xaxis(x0, fx(800), 220, [0, 100, 200, 300, 400, 500, 600, 700, 800], fx, 'time (ms)'))
    o.append(T(20, 292, '4 objects × 2 RTT = 8 RTT = 800 ms,  against 1 + 1 + 1 = 3 RTT = 300 ms', 14, 'start', INK, True))
    return 308, ''.join(o)
FIG[4] = (f4, 'Non-persistent HTTP/1.0 pays a TCP handshake before each of the 4 objects, 8 round trips or 800 ms. Persistent HTTP/1.1 with pipelining keeps one connection and brings all three images back in one round trip, 3 round trips or 300 ms.',
          'Two timelines of 100 ms blocks: HTTP/1.0 alternating TCP and object blocks for 8 blocks ending at 800 ms; HTTP/1.1 with TCP, base and one block for 3 images ending at 300 ms.')


# ---- 6.5 FTP control and data connections ----
def f5():
    o = []
    o.append(boxt(20, 40, 160, 150, ['client', '192.168.1.7'], PANEL, L2, 14, bold_first=True))
    o.append(boxt(540, 40, 160, 150, ['server', '10.0.0.5'], PANEL, L2, 14, bold_first=True))
    for x, y, p, c in ((180, 80, '50000', AC), (180, 150, '50001', NX), (540, 80, '21', AC), (540, 150, '20', NX)):
        o.append(R(x - 30, y - 14, 60, 28, ACS if c == AC else NXS, c, 4, 1.8)); o.append(T(x, y + 5, p, 13, fill=c, bold=True))
    o.append(L(212, 80, 506, 80, AC, 2.6, arrow='n'))
    o.append(T(360, 70, 'control: client 50000 → server 21', 13, fill=AC, bold=True))
    o.append(T(360, 100, 'open the whole session (USER, RETR …)', 13, fill=MUT))
    o.append(L(508, 150, 214, 150, NX, 2.6, arrow='x'))
    o.append(T(360, 140, 'data: server 20 → client 50001', 13, fill=NX, bold=True))
    o.append(T(360, 170, 'active mode: the server opens it', 13, fill=MUT))
    # timeline
    x0, sc = 150, 14
    fx = lambda t: x0 + t * sc
    o.append(T(x0 - 12, 247, 'control', 13, 'end', AC, True))
    o.append(R(fx(0), 228, 32 * sc, 28, ACS, AC, 3, 1.6))
    o.append(T(x0 - 12, 289, 'data', 13, 'end', NX, True))
    o.append(seg(fx(4), 270, 20 * sc, 28, NXS, NX, '20 MB = 160 Mbit ÷ 8 Mbps = 20 s'))
    o.append(T(fx(4), 318, 'opens for the file', 13, 'middle', NX))
    o.append(T(fx(24), 318, 'closes', 13, 'middle', NX))
    return 334, ''.join(o)
FIG[5] = (f5, 'The control connection from client port 50000 to server port 21 stays open for the whole session; the data connection from server port 20 to client port 50001 opens only for the 20 MB file, 20 s at 8 Mbps, then closes.',
          'A client and server with two connections: control from port 50000 to port 21 and data from port 20 to port 50001, and a timeline where the control bar spans the session and the data bar lasts 20 s.')


# ---- 6.6 SMTP pushes, IMAP pulls ----
def f6():
    o = []
    o.append(boxt(20, 60, 120, 50, ['sender', 'mail app'], PANEL, L2, 13, bold_first=True))
    o.append(boxt(200, 60, 130, 50, ['Chennai', 'mail server'], ACS, AC, 13, bold_first=True))
    o.append(boxt(420, 60, 130, 50, ['Delhi', 'mail server'], ACS, AC, 13, bold_first=True))
    o.append(boxt(610, 60, 100, 50, ['phone'], PANEL, L2, 14, bold_first=True))
    o.append(L(142, 85, 196, 85, AC, 2.4, arrow='n')); o.append(T(169, 50, 'SMTP', 13, fill=AC, bold=True))
    o.append(L(332, 85, 416, 85, AC, 3, arrow='n')); o.append(T(374, 50, 'SMTP push', 13, fill=AC, bold=True))
    o.append(T(374, 132, '406 KB', 14, fill=AC, bold=True))
    o.append(L(606, 85, 554, 85, NX, 2.4, arrow='x')); o.append(T(580, 50, 'IMAP', 13, fill=NX, bold=True))
    o.append(T(580, 132, 'pull', 13, fill=NX, bold=True))
    # size bars
    sc = 1.0
    y = 180
    o.append(T(20, y - 12, 'What crosses the SMTP link (7-bit text only, so the photo is base64-encoded)', 14, 'start', bold=True))
    o.append(T(130, y + 22, 'photo on disk', 13, 'end', MUT, True))
    o.append(seg(140, y, 300 * sc, 34, PANEL, L2, '300 KB', 13, INK))
    o.append(T(130, y + 66, 'over SMTP', 13, 'end', MUT, True))
    o.append(seg(140, y + 44, 6 * sc + 10, 34, NXS, NX, '', 13))
    o.append(seg(140 + 6 * sc + 10, y + 44, 400 * sc, 34, LVS, LV, 'photo × 4/3 = 400 KB'))
    o.append(T(140 + 6 * sc + 10 + 400 * sc + 8, y + 66, '+ 6 KB text = 406 KB', 13, 'start', INK, True))
    o.append(T(140, y + 100, 'headers and text, 6 KB', 13, 'start', NX, True))
    return y + 116, ''.join(o)
FIG[6] = (f6, 'Base64 makes the 300 KB photo 400 KB, so with 6 KB of headers and text the Chennai-to-Delhi SMTP hop carries 406 KB. The phone then pulls the mail from the Delhi server with IMAP, because SMTP only pushes.',
          'Sender, Chennai server, Delhi server and phone in a row with SMTP arrows pushing 406 KB to Delhi and an IMAP pull to the phone; below, the 300 KB photo growing to 400 KB, plus 6 KB of text.')


# ---- 6.7 toy RSA ----
def f7():
    o = []
    o.append(boxt(20, 20, 680, 50, ['keys: n = 3 × 11 = 33,  φ(n) = 2 × 10 = 20,  public e = 3,  private d = 7 (3 × 7 = 21 ≡ 1 mod 20)'],
                  PANEL, L2, 14, bold_first=True))
    y = 120
    o.append(boxt(20, y, 90, 56, ['M = 5'], ACS, AC, 16, bold_first=True))
    o.append(boxt(150, y - 8, 170, 72, ['encrypt (public)', '5³ = 125', '125 mod 33 = 26'], PANEL, AC, 13, bold_first=True))
    o.append(boxt(360, y, 100, 56, ['C = 26'], LVS, LV, 16, bold_first=True))
    o.append(boxt(496, y - 8, 136, 72, ['decrypt (private)', '26⁷ mod 33', '= 5'], PANEL, NX, 13, bold_first=True))
    o.append(boxt(652, y, 58, 56, ['5'], NXS, NX, 18, bold_first=True))
    o.append(L(112, y + 28, 146, y + 28, AC, 2.2, arrow='n')); o.append(L(322, y + 28, 356, y + 28, AC, 2.2, arrow='n'))
    o.append(L(462, y + 28, 492, y + 28, LV, 2.2, arrow='l')); o.append(L(634, y + 28, 648, y + 28, NX, 2.2, arrow='x'))
    o.append(T(410, y + 82, 'only 26 crosses the wire', 13, fill=LV, bold=True))
    o.append(T(20, 250, 'Decrypt by squaring: 26² = 676 ≡ 16,  26⁴ ≡ 16² = 256 ≡ 25,', 13, 'start', INK))
    o.append(T(20, 272, '26⁷ = 26⁴ × 26² × 26 ≡ 25 × 16 × 26;  25 × 16 = 400 ≡ 4;  4 × 26 = 104 ≡ 5 (mod 33)', 13, 'start', INK))
    return 290, ''.join(o)
FIG[7] = (f7, 'The public pair n = 33, e = 3 turns M = 5 into C = 26, which is all that crosses the wire; the private d = 7 turns 26 back into 5.',
          'Key values n = 33, φ = 20, e = 3, d = 7 above a chain M = 5, encrypt 5³ mod 33 = 26, ciphertext 26, decrypt 26⁷ mod 33 = 5, and the squaring steps below.')


spec = make_spec(FIG)
