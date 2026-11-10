"""Claude's hand-drawn figures for c-sec-u5 (Cryptography and Network Security, unit 5: authentication and network
security protocols), one per chapter, from each chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
ARR = {AC: 'n', L2: 'm', LV: 'l', NX: 'x', MUT: 'm', INK: 'm'}


def ar(x1, y1, x2, y2, c=AC, a=None, w=2, dash=None):
    return L(x1, y1, x2, y2, c, w, dash, arrow=a or ARR[c])


def msg(y, xa, xb, label, c=AC, dash=None, size=14, below=None):
    d = 1 if xb > xa else -1
    o = [L(xa, y, xb - d * 2, y, c, 2, dash, ARR[c]), Tb((xa + xb) / 2, y - 8, label, size, fill=c, bold=True)]
    if below: o.append(Tb((xa + xb) / 2, y + 20, below, 13, fill=c))
    return ''.join(o)


def life(x, y0, y1):
    return L(x, y0, x, y1, L2, 1.5, '5 5')


# ---- 5.1 challenge-response with a nonce ----
def f1():
    cx, sx = 140, 560
    o = [life(cx, 56, 384), life(sx, 56, 384),
         boxt(40, 16, 200, 40, ['client (knows kite)'], LVS, LV, 14, True),
         boxt(460, 16, 200, 40, ['server (knows kite)'], NXS, NX, 14, True)]
    o.append(msg(92, sx, cx, 'fresh nonce R = 913', AC))
    o.append(boxt(20, 108, 240, 52, ['H(kite913) = (429 + 157) mod 1000', '= 586'], PANEL, LV, 13, True))
    o.append(msg(190, cx, sx, 'answer 586', NX))
    o.append(boxt(440, 204, 260, 52, ['expects H(kite913) = 586', '586 = 586: accept'], NXS, NX, 14, True))
    o.append(boxt(20, 278, 240, 52, ['attacker replays 581', 'recorded when R was 512'], LVS, LV, 13, True, dash='5 4'))
    o.append(msg(304, 260, sx, 'replayed 581', LV, '6 4'))
    o.append(boxt(440, 324, 260, 44, ['581 ≠ 586: reject'], LVS, LV, 15, True))
    o.append(T(20, 410, 'H(s) = sum of ASCII codes mod 1000:  kite = 107 + 105 + 116 + 101 = 429,  "913" = 157,  "512" = 152.', 13, 'start', MUT))
    return 424, ''.join(o)


FIG[1] = (f1, 'The server sends the fresh nonce 913 and the client answers H("kite913") = 586, which the server accepts. The answer 581 recorded under the old nonce 512 does not match and is rejected.',
          'Sequence diagram: the server sends nonce 913, the client computes 429 + 157 mod 1000 = 586 and sends it, and the server accepts. An attacker replays 581 from an old nonce 512 and the server rejects it.')


# ---- 5.2 Kerberos clock skew window ----
def f2():
    fx = lambda m: 60 + (m - 593) * 44
    o = [T(20, 26, 'Kerberos AP exchange: the file server checks the authenticator\'s timestamp', 15, 'start', bold=True)]
    o.append(R(fx(595), 84, fx(605) - fx(595), 66, NXS, NX, 4, 1.5))
    o.append(T((fx(595) + fx(600)) / 2, 122, 'accepted window', 14, fill=NX, bold=True))
    o.append(T((fx(595) + fx(600)) / 2, 140, '10:00 ± 5 min', 13, fill=NX))
    o.append(L(60, 150, fx(607), 150, L2, 1.5))
    for m in range(593, 608):
        o.append(L(fx(m), 150, fx(m), 156, L2, 1.5))
    for m in (595, 600, 604, 605, 606):
        o.append(T(fx(m), 174, f'{m // 60:02d}:{m % 60:02d}', 13, fill=MUT if m != 600 else INK, bold=m == 600))
    o += [L(fx(600), 62, fx(600), 150, INK, 2), T(fx(600), 56, 'server clock 10:00', 14, bold=True)]
    o += [C(fx(604), 112, 8, NX), T(fx(604) - 14, 104, 'accept', 14, 'end', NX, True),
          C(fx(606), 112, 8, LV), T(fx(606) + 14, 104, 'reject', 14, 'start', LV, True)]
    o.append(T(20, 214, '(a) 10:04:  |604 − 600| = 4 min ≤ 5, so the authenticator is accepted', 14, 'start', NX, True))
    o.append(T(20, 238, '(b) 10:06:  |606 − 600| = 6 min > 5, so the server returns a clock skew error', 14, 'start', LV, True))
    o.append(T(20, 262, '(c) latest accepted client time:  600 + 5 = 605 min = 10:05', 14, 'start', AC, True))
    return 278, ''.join(o)


FIG[2] = (f2, 'With the server clock at 10:00 and a 5-minute limit, timestamps from 09:55 to 10:05 pass. The authenticator stamped 10:04 is accepted and the one stamped 10:06 is rejected.',
          'A time line from 09:53 to 10:07 with a shaded window 09:55 to 10:05 around the server clock 10:00. A green dot at 10:04 is inside and accepted; an orange dot at 10:06 is outside and rejected.')


# ---- 5.3 ESP tunnel mode ----
def f3():
    o = [boxt(20, 30, 100, 50, ['host A', '10.1.1.5'], PANEL, L2, 14, True),
         boxt(160, 30, 130, 50, ['gateway', '203.0.113.2'], ACS, AC, 14, True),
         boxt(430, 30, 130, 50, ['gateway', '198.51.100.9'], ACS, AC, 14, True),
         boxt(600, 30, 100, 50, ['host B', '10.2.2.7'], PANEL, L2, 14, True)]
    o += [L(120, 55, 160, 55, L2, 2), L(560, 55, 600, 55, L2, 2),
          L(290, 49, 430, 49, AC, 2), L(290, 61, 430, 61, AC, 2),
          Tb(360, 60, 'ESP tunnel', 13, fill=AC, bold=True), T(360, 100, 'an Internet router reads', 13, fill=MUT),
          T(360, 118, 'only the outer header', 13, fill=MUT)]
    segs = [('outer IP header', '203.0.113.2 →', '198.51.100.9', 130, PANEL, L2),
            ('ESP', 'header', '', 70, ACS, AC), ('inner IP', '10.1.1.5 →', '10.2.2.7', 120, LVS, LV),
            ('TCP 443', '+ data', '', 100, LVS, LV), ('ESP', 'trailer', '', 80, LVS, LV), ('ESP', 'auth', '', 80, NXS, NX)]
    x, xs, y = 60, [], 166
    for a, b, c, w, f, st in segs:
        xs.append(x)
        o.append(boxt(x, y, w, 64, [s for s in (a, b, c) if s], f, st, 13, True, rx=3))
        x += w
    xs.append(x)
    o += [brace(xs[2], xs[5], 156, LV), T((xs[2] + xs[5]) / 2, 148, 'encrypted', 14, fill=LV, bold=True),
          brace(xs[1], xs[5], 240, NX, up=True), T((xs[1] + xs[5]) / 2, 262, 'covered by the integrity check in ESP auth', 13, fill=NX, bold=True)]
    o.append(T(20, 296, 'Seen: 203.0.113.2 → 198.51.100.9.  Hidden: 10.1.1.5 → 10.2.2.7 and port 443.', 14, 'start', INK, True))
    return 310, ''.join(o)


FIG[3] = (f3, 'In tunnel mode the whole inner packet 10.1.1.5 → 10.2.2.7, port 443, is encrypted behind a new outer header. A router on the Internet sees only 203.0.113.2 → 198.51.100.9.',
          'Top: host A, gateway 203.0.113.2, an ESP tunnel, gateway 198.51.100.9 and host B. Below: the packet as outer IP header, ESP header, inner IP header, TCP 443 data, ESP trailer and ESP auth, with the inner part braced as encrypted and the ESP header to trailer braced as integrity protected.')


# ---- 5.4 TLS 1.2 handshake with RSA key exchange ----
def f4():
    cx, sx = 120, 600
    o = [life(cx, 56, 390), life(sx, 56, 390),
         boxt(40, 16, 160, 40, ['client'], LVS, LV, 15, True), boxt(520, 16, 160, 40, ['server'], NXS, NX, 15, True)]
    rows = [(cx, sx, 'ClientHello, random C = 0x11', AC), (sx, cx, 'ServerHello, random S = 0x22', AC),
            (sx, cx, 'Certificate (server RSA public key)', AC), (sx, cx, 'ServerHelloDone', AC),
            (cx, sx, 'ClientKeyExchange: 48-byte PMS under RSA', LV),
            (cx, sx, 'ChangeCipherSpec, Finished', NX), (sx, cx, 'ChangeCipherSpec, Finished', NX)]
    for i, (a, b, s, c) in enumerate(rows):
        o.append(msg(92 + i * 40, a, b, s, c))
    o += [L(cx + 2, 376, sx - 2, 376, NX, 3), Tb(360, 368, 'encrypted HTTPS records', 14, fill=NX, bold=True),
          f'<line x1="{cx + 4}" y1="376" x2="{cx + 2}" y2="376" style="stroke:{NX};stroke-width:3" marker-end="url(#ar-UID-x)"/>',
          f'<line x1="{sx - 4}" y1="376" x2="{sx - 2}" y2="376" style="stroke:{NX};stroke-width:3" marker-end="url(#ar-UID-x)"/>']
    o.append(boxt(20, 404, 680, 54, ['the server decrypts the 48-byte PMS with its RSA private key; then both compute',
                                     'master_secret = PRF(PMS, "master secret", C ‖ S), fixed at 48 bytes'], ACS, AC, 14))
    return 470, ''.join(o)


FIG[4] = (f4, 'The client sends random 0x11 and the server answers with 0x22 and its certificate. The client sends a 48-byte pre-master secret under the server\'s RSA key, and both sides derive the 48-byte master secret.',
          'Sequence diagram between client and server: ClientHello with C = 0x11, ServerHello with S = 0x22, Certificate, ServerHelloDone, ClientKeyExchange with a 48-byte PMS, ChangeCipherSpec and Finished each way, then encrypted records. A note gives master_secret = PRF(PMS, master secret, C and S), 48 bytes.')


# ---- 5.5 PGP sign then encrypt ----
def f5():
    o = [T(20, 26, 'Alice sends', 15, 'start', LV, True)]
    boxes = [(['Pay ₹500'], 86, PANEL, L2), (['hash + sign', 'Alice private key'], 130, LVS, LV), (['compress'], 80, PANEL, L2),
             (['encrypt body', 'Ks = 0x7A = 122'], 120, ACS, AC), (['wrap Ks', 'Bob public key'], 110, NXS, NX), (['radix-64'], 80, PANEL, L2)]
    x = 20
    for i, (ls, w, f, st) in enumerate(boxes):
        o.append(boxt(x, 40, w, 52, ls, f, st, 13, True))
        if i < 5: o.append(ar(x + w, 66, x + w + 14, 66))
        x += w + 16
    xr = x - 16 - 40
    o += [P([(xr, 92), (xr, 142), (140, 142), (140, 186)], L2, 2), ar(140, 180, 140, 194, L2),
          Tb((xr + 140) / 2, 147, 'email over SMTP', 14, fill=MUT, bold=True)]
    o.append(T(20, 186, 'Bob reads', 15, 'start', NX, True))
    bob = [(['step 1: Bob private key', 'unwrap: Ks = 122'], 200, NXS, NX), (['step 2: Ks = 122', 'decrypt the body'], 180, ACS, AC),
           (['step 3: Alice public key', 'decompress, verify'], 200, LVS, LV)]
    x = 40
    for i, (ls, w, f, st) in enumerate(bob):
        o.append(boxt(x, 196, w, 54, ls, f, st, 14, True))
        if i < 2: o.append(ar(x + w, 223, x + w + 26, 223))
        x += w + 30
    o.append(T(20, 290, 'Bob must decrypt before he can verify, because the signature sits inside the encrypted body.', 14, 'start'))
    o.append(T(20, 314, 'Three key operations: Bob\'s private key, the session key Ks, and Alice\'s public key.', 14, 'start', AC, True))
    return 328, ''.join(o)


FIG[5] = (f5, 'Alice signs, compresses, encrypts under Ks = 122 and wraps Ks with Bob\'s public key. Bob uses three keys in order: his private key, then Ks, then Alice\'s public key to verify.',
          'Top row: Pay 500 rupees, hash and sign with Alice private key, compress, encrypt body with Ks = 0x7A = 122, wrap Ks with Bob public key, radix-64. A line marked email over SMTP leads to Bob\'s row: step 1 unwrap Ks with his private key, step 2 decrypt the body, step 3 verify with Alice public key.')


# ---- 5.6 DNSSEC validation and TTL ----
def f6():
    chain = [(['root', 'trust anchor'], 110), (['.in', 'DS + DNSKEY'], 120), (['bank.in', 'DS + DNSKEY'], 130),
             (['www A 203.0.113.7', 'RRSIG checks'], 190)]
    x, o = 30, []
    for i, (ls, w) in enumerate(chain):
        o.append(boxt(x, 30, w, 52, ls, NXS if i == 3 else PANEL, NX, 14, True))
        if i < 3: o.append(ar(x + w, 56, x + w + 28, 56, NX, 'x'))
        x += w + 30
    o.append(T(30, 112, 'reply A: every link verifies, so it is cached', 14, 'start', NX, True))
    o.append(boxt(470, 98, 230, 52, ['reply B: www A 6.6.6.6', 'no RRSIG: bogus, discarded'], LVS, LV, 13, True, dash='5 4'))
    fx = lambda t: 60 + t * 1.9
    o.append(R(fx(0), 196, fx(300) - fx(0), 30, NXS, NX, 3, 1.5))
    o.append(T((fx(0) + fx(240)) / 2, 216, 'cached: 203.0.113.7, TTL 300 s', 13, fill=NX, bold=True))
    o += [brace(fx(240), fx(300), 186, AC), T((fx(240) + fx(300)) / 2, 178, '60 s left', 14, fill=AC, bold=True),
          L(fx(240), 186, fx(240), 232, AC, 2), L(fx(300), 186, fx(300), 232, LV, 2)]
    o.append(xaxis(fx(0), fx(330), 232, [0, 60, 120, 180, 240, 300], fx, 'seconds since the replies arrived'))
    o.append(T(20, 306, 'At t = 240 s: 300 − 240 = 60 s remain.  At t = 300 s the entry expires and the resolver asks again.', 13, 'start'))
    return 320, ''.join(o)


FIG[6] = (f6, 'Reply A verifies link by link from the root down to the RRSIG on 203.0.113.7 and is cached for 300 s; reply B has no RRSIG and is discarded. At 240 s the entry has 60 s left.',
          'A chain of boxes from the root trust anchor through .in and bank.in to the signed record www A 203.0.113.7. A dashed box shows reply B, 6.6.6.6, discarded as bogus. A time bar from 0 to 300 seconds marks 60 seconds left at 240.')


# ---- 5.7 WPA2 four-way handshake ----
def f7():
    cx, sx = 130, 590
    o = [life(cx, 56, 330), life(sx, 56, 330),
         boxt(40, 16, 180, 40, ['client'], LVS, LV, 15, True), boxt(500, 16, 180, 40, ['access point'], NXS, NX, 15, True),
         T(360, 76, 'both already hold the PMK', 13, fill=MUT)]
    o.append(msg(108, sx, cx, 'M1: ANonce = 0xA1 = 161', AC))
    o.append(boxt(20, 122, 250, 40, ['PTK = PRF(PMK, 161, 178, MACs)'], ACS, AC, 13, True))
    o.append(msg(190, cx, sx, 'M2: SNonce = 0xB2 = 178, MIC', AC))
    o.append(boxt(450, 204, 250, 40, ['same PTK from 161 and 178'], ACS, AC, 13, True))
    o.append(msg(272, sx, cx, 'M3: GTK, install keys, MIC', NX))
    o.append(msg(312, cx, sx, 'M4: ACK', NX))
    o.append(boxt(20, 344, 680, 62, ['replay: an attacker resends M1 with ANonce = 161',
                                     'the client picks a fresh SNonce, not 178, so the PTK changes and the old MIC fails'], LVS, LV, 14, True, dash='5 4'))
    return 418, ''.join(o)


FIG[7] = (f7, 'The AP\'s ANonce 0xA1 = 161 and the client\'s SNonce 0xB2 = 178 feed the PRF that makes the PTK. A replayed ANonce meets a fresh SNonce, so the PTK changes and an old MIC fails.',
          'Sequence diagram between client and access point: M1 with ANonce 161, the client computes the PTK, M2 with SNonce 178 and a MIC, M3 with the GTK, M4 ACK. A dashed box below explains that a replayed M1 meets a fresh SNonce.')


# ---- 5.8 802.1X with RADIUS VLAN assignment ----
def f8():
    sx, wx, rx = 100, 360, 620
    o = [life(sx, 56, 340), life(rx, 56, 340),
         boxt(20, 16, 160, 40, ['alice (supplicant)'], LVS, LV, 14, True),
         boxt(240, 16, 240, 40, ['switch port Fa0/10'], ACS, AC, 14, True),
         boxt(540, 16, 160, 40, ['RADIUS server'], NXS, NX, 14, True)]
    o += [R(wx - 7, 56, 14, 238, LVS, LV, 3, 1.5), R(wx - 7, 294, 14, 46, NXS, NX, 3, 1.5)]
    o.append(msg(90, sx, wx - 8, 'EAPOL-Start', AC))
    o.append(msg(126, wx - 8, sx, 'EAP-Request / Identity', AC))
    o.append(msg(162, sx, wx - 8, 'EAP-Response: alice', AC))
    o.append(msg(198, wx + 8, rx, 'RADIUS Access-Request', AC))
    o.append(L(rx, 230, sx + 2, 230, L2, 2, '6 4', 'm'))
    o.append(Tb(230, 222, 'EAP method, relayed', 13, fill=MUT, bold=True))
    o.append(msg(272, rx, wx + 8, 'Access-Accept', NX, below='Tunnel-Private-Group-ID = 20'))
    o.append(msg(322, wx - 8, sx, 'EAP-Success', NX))
    o.append(boxt(20, 358, 330, 52, ['before: port unauthorized', 'EAPOL only; normal data in 0 VLANs'], LVS, LV, 14, True))
    o.append(boxt(370, 358, 330, 52, ['after Access-Accept: authorized', 'alice\'s traffic enters VLAN 20'], NXS, NX, 14, True))
    return 422, ''.join(o)


FIG[8] = (f8, 'The switch only relays EAP to RADIUS and keeps Fa0/10 closed to normal data. Access-Accept carries Tunnel-Private-Group-ID = 20, so the port opens into VLAN 20.',
          'Sequence diagram between alice, the switch port Fa0/10 and the RADIUS server: EAPOL-Start, identity request and response, Access-Request, the relayed EAP method, Access-Accept with group ID 20, EAP-Success. The port bar turns from unauthorized to authorized, and two boxes give 0 VLANs before and VLAN 20 after.')


# ---- 5.9 SQL injection ----
def sq(x, y, parts, size=14):
    sp = ''.join(f'<tspan style="fill:{c}">{s}</tspan>' for s, c in parts)
    return f'<text x="{x}" y="{y}" font-size="{size}" style="fill:{INK};font-family:var(--mono);white-space:pre" xml:space="preserve">{sp}</text>'


def f9():
    o = [T(20, 26, 'query template', 13, 'start', MUT),
         TM(20, 50, "SELECT * FROM users WHERE user='$u' AND pass='$p'", 14, 'start'),
         T(20, 84, 'attacker input:', 13, 'start', MUT),
         TM(130, 84, "u = ' OR '1'='1' --", 14, 'start', LV, True), TM(340, 84, "p = x", 14, 'start', LV, True),
         T(20, 118, 'resulting query', 13, 'start', MUT),
         sq(20, 144, [('SELECT * FROM users WHERE ', INK), ("user=''", MUT), (" OR '1'='1'", AC), (" -- ' AND pass='x'", LV)])]
    for i, (s, c) in enumerate([("user='' is false for every row", MUT), ("OR '1'='1' is true for every row, so the whole WHERE is true", AC),
                                ("-- starts a comment: the password test is never run", LV)]):
        y = 176 + i * 22
        o += [R(20, y - 11, 12, 12, c, c, 2, 1), T(40, y, s, 14, 'start', c, True)]
    cols = [(20, 60, 'row'), (80, 150, 'user'), (230, 190, 'WHERE result')]
    y0 = 254
    for x, w, h in cols:
        o.append(boxt(x, y0, w, 30, [h], PANEL, L2, 13, True, rx=0))
    for r, u in enumerate(['admin', 'asha', 'vikram']):
        y = y0 + 30 + r * 30
        f = NXS if r == 0 else PANEL
        for (x, w, _), s in zip(cols, [str(r + 1), u, 'true']):
            o.append(boxt(x, y, w, 30, [s], f, L2, 14, r == 0, rx=0))
    o.append(T(20, 396, '3 rows returned', 14, 'start', AC, True))
    o += [ar(420, 299, 478, 310, NX, 'x'), boxt(480, 286, 220, 56, ['app takes the first row', '1 login as admin'], NXS, NX, 14, True)]
    return 410, ''.join(o)


FIG[9] = (f9, 'The input closes the quote, adds OR \'1\'=\'1\', which is true for all 3 rows, and comments out the password test with --. The query returns 3 rows and the app logs in as the first.',
          'The query template, the attacker input and the resulting query with user equals empty in grey, OR 1 equals 1 in blue and the commented-out password test in orange. A table of 3 rows all marked true, and an arrow from row 1 to a box saying 1 login as admin.')

spec = make_spec(FIG)
