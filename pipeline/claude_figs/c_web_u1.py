"""Claude's hand-drawn figures for c-web-u1 (Web Technologies, unit 1: Internet, web and HTTP), one per chapter,
each drawn from that chapter's worked example with its own numbers, plus the sentences that describe a figure."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
ARC = {AC: 'n', L2: 'm', LV: 'l', NX: 'x'}


def ar(x1, y1, x2, y2, c=AC, w=2, dash=None):
    return L(x1, y1, x2, y2, c, w, dash, ARC[c])


def gauge(x, y, w, used, cap, label_used, label_spare, h=26):
    """a capacity bar: the used share filled, the spare share open"""
    u = w * used / cap
    o = R(x, y, w, h, PANEL, L2, 5, 1.5) + R(x, y, u, h, ACS, AC, 5, 2)
    if u > tw(label_used, 13) + 8:
        o += T(x + u / 2, y + h / 2 + 5, label_used, 13, bold=True)
    else:
        o += T(x + u + 8, y + h / 2 + 5, label_used, 13, 'start', bold=True)
    return o + T(x + w - 8, y + h / 2 + 5, label_spare, 13, 'end', NX, True)


# ---- 1.1 one DNS lookup for shop.example.com ----
def f1():
    o = [T(20, 26, 'Looking up shop.example.com (cache empty)', 15, 'start', bold=True)]
    o.append(boxt(20, 160, 140, 64, ['Browser', 'needs an address'], size=14, bold_first=True))
    o.append(boxt(240, 160, 150, 64, ['Resolver', 'asks for the browser'], size=14, bold_first=True))
    rows = [(52, '1  Root server', 'refers to .com servers'),
            (160, '2  .com TLD server', 'refers to ns1.example.com'),
            (268, '3  ns1.example.com', 'A 203.0.113.10, TTL 300 s')]
    for y, a, b in rows:
        last = a.startswith('3')
        o.append(boxt(480, y, 220, 64, [a, b], NXS if last else PANEL, NX if last else AC, 14, bold_first=True))
        ya = y + 24
        o.append(ar(392, 182 if y == 160 else (170 if y < 160 else 200), 476, ya - 2))
        o.append(ar(478, ya + 16, 394, 192 if y == 160 else (180 if y < 160 else 212), NX, 2, '6 4'))
    o.append(Tb(412, 112, 'ask', 13, fill=AC, bold=True))
    o.append(Tb(424, 304, 'answer', 13, fill=NX, bold=True))
    # browser <-> resolver
    o.append(ar(162, 182, 236, 182))
    o.append(ar(236, 206, 164, 206, NX, 2, '6 4'))
    o.append(T(200, 150, 'ask', 13, fill=AC, bold=True))
    o.append(T(200, 246, '203.0.113.10', 13, fill=NX, bold=True))
    o.append(T(315, 246, 'keeps it for 300 s', 13, fill=MUT))
    # then connect
    o.append(ar(90, 226, 90, 352))
    o.append(Tb(90, 300, 'TCP port 443', 13, fill=AC, bold=True))
    o.append(boxt(20, 356, 420, 58, ['Web server at 203.0.113.10', 'https, so port 443:  GET /items?id=7'], NXS, NX, 14, bold_first=True))
    o.append(T(480, 372, 'Name servers asked: 3', 14, 'start', bold=True))
    o.append(T(480, 394, 'root, TLD, authoritative', 13, 'start', MUT))
    o.append(T(480, 414, 'A cached answer skips all 3.', 13, 'start', MUT))
    return 432, ''.join(o)
FIG[1] = (f1, 'The resolver asks three name servers in turn: the root sends it to .com, the .com server sends it to ns1.example.com, and that server answers A 203.0.113.10 with TTL 300 s. The browser then opens TCP port 443 and sends GET /items?id=7.',
          'Browser asks a resolver; the resolver asks the root, the .com TLD server and ns1.example.com in turn, gets 203.0.113.10 with TTL 300 s, and the browser connects to that address on port 443.')


# ---- 1.2 an exam portal across three tiers ----
def f2():
    o = [T(20, 26, '600 students × 20 requests in 600 s = 20 requests/s', 15, 'start', bold=True)]
    # tier bands as columns
    cols = [(20, 150, 'Presentation'), (180, 360, 'Application'), (560, 140, 'Data')]
    for x, w, name in cols:
        o.append(R(x, 50, w, 300, 'var(--fig)', LN, 10, 1.5, '5 4'))
        o.append(T(x + w / 2, 72, name, 13, fill=MUT, bold=True))
    o.append(boxt(30, 170, 130, 60, ['Browsers', '600 students'], size=14, bold_first=True))
    o.append(boxt(200, 170, 120, 60, ['Load', 'balancer'], size=14, bold_first=True))
    o.append(ar(162, 200, 196, 200))
    o.append(Tb(179, 160, '20/s', 13, fill=AC, bold=True))
    for i, y in enumerate((96, 254)):
        o.append(boxt(390, y, 140, 70, [f'App server {i + 1}', 'gets 10/s', 'limit 15/s'], NXS, NX, 14, bold_first=True))
        o.append(ar(322, 200, 386, y + 35))
        o.append(Tb(350, y + 35 + (-16 if i == 0 else 24), '10/s', 13, fill=AC, bold=True))
        o.append(ar(532, y + 35, 576, 200))
    o.append(boxt(580, 170, 110, 60, ['Database', 'one copy'], size=14, bold_first=True))
    o.append(T(20, 380, 'Servers needed = ⌈20 ÷ 15⌉ = ⌈1.33⌉ = 2, so each gets 20 ÷ 2 = 10 requests/s.', 14, 'start', bold=True))
    o.append(T(20, 402, 'Both servers stay below their 15 requests/s limit.', 14, 'start', MUT))
    return 418, ''.join(o)
FIG[2] = (f2, 'The 20 requests/s from 600 students reach a load balancer, which splits them into 10 requests/s for each of two app servers, both under their 15 requests/s limit. Both servers read and write the one database in the data tier.',
          'Three tier columns: browsers in the presentation tier send 20 requests per second to a load balancer, which sends 10 per second to each of two app servers in the application tier; both use one database in the data tier.')


# ---- 1.3 Nginx serves static files and proxies the rest ----
def f3():
    o = [T(20, 26, 'Nginx receives 1,000 requests per minute', 15, 'start', bold=True)]
    o.append(boxt(20, 150, 120, 64, ['Browser', '1,000/min'], size=14, bold_first=True))
    o.append(boxt(200, 150, 130, 64, ['Nginx', 'web server'], size=14, bold_first=True))
    o.append(ar(142, 182, 196, 182))
    o.append(boxt(420, 52, 270, 64, ['Static files', '70%: 700/min = 11.7/s'], PANEL, AC, 14, bold_first=True))
    o.append(boxt(420, 248, 150, 64, ['Express app', '30%: 300/min = 5/s'], NXS, NX, 14, bold_first=True))
    o.append(boxt(610, 248, 90, 64, ['Database'], size=14, bold_first=True))
    o.append(ar(332, 168, 416, 92))
    o.append(Tb(372, 116, 'serve file', 13, fill=AC, bold=True))
    o.append(ar(332, 196, 416, 272, NX))
    o.append(Tb(372, 248, 'proxy', 13, fill=NX, bold=True))
    o.append(ar(572, 280, 606, 280))
    o.append(T(20, 362, 'Express capacity 25 requests/s', 14, 'start', bold=True))
    o.append(gauge(20, 374, 680, 5, 25, '5/s used', 'spare 25 − 5 = 20/s'))
    o.append(T(20, 424, 'Only the 300 dynamic requests a minute reach Express, so 25/s is more than enough.', 14, 'start', MUT))
    return 440, ''.join(o)
FIG[3] = (f3, 'Nginx answers 700 of every 1,000 requests a minute from static files and proxies the other 300 (5 per second) to Express. Express can take 25 per second, so 20 per second are spare.',
          'A browser sends 1,000 requests per minute to Nginx; 700 per minute go to static files and 300 per minute, 5 per second, are proxied to an Express app that uses a database; a bar shows 5 of 25 requests per second used.')


# ---- 1.4 three requests, three 2xx replies ----
def f4():
    o = [T(20, 26, 'Client and api.example.com over one HTTPS connection (port 443)', 15, 'start', bold=True)]
    xc, xs = 110, 610
    o.append(boxt(xc - 70, 44, 140, 40, ['Client'], size=14, bold_first=True))
    o.append(boxt(xs - 90, 44, 180, 40, ['api.example.com'], size=14, bold_first=True))
    o.append(L(xc, 86, xc, 410, L2, 1.5, '4 4')); o.append(L(xs, 86, xs, 410, L2, 1.5, '4 4'))
    rows = [('GET /items/7?expand=price', '200 OK  ·  body 84 bytes'),
            ('POST /items', '201 Created  ·  Location: the new item'),
            ('DELETE /items/7', '204 No Content  ·  body 0 bytes')]
    y = 118
    for req, res in rows:
        o.append(ar(xc + 2, y, xs - 4, y))
        o.append(Tb((xc + xs) / 2, y - 8, req, 14, fill=AC, bold=True))
        o.append(ar(xs - 2, y + 46, xc + 4, y + 46, NX, 2))
        o.append(Tb((xc + xs) / 2, y + 38, res, 14, fill=NX, bold=True))
        y += 100
    o.append(T(20, 430, 'First digit 2 on all three replies: every request succeeded (2xx).', 14, 'start', bold=True))
    return 446, ''.join(o)
FIG[4] = (f4, 'Three requests on one connection, each answered with a 2xx success code: GET gets 200 with an 84-byte body, POST gets 201 Created, and DELETE gets 204 No Content with no body at all.',
          'A client and api.example.com exchange three request and reply pairs: GET returns 200 OK with 84 bytes, POST returns 201 Created, DELETE returns 204 No Content with 0 bytes.')


# ---- 1.5 a MERN product page ----
def f5():
    o = [T(20, 26, 'One product page through the MERN stack', 15, 'start', bold=True)]
    boxes = [(20, ['React', 'in the browser', 'renders the list']), (260, ['Express on Node.js', 'GET /api/products', 'reads, sends JSON']),
             (520, ['MongoDB', '250 product', 'documents'])]
    for x, lines in boxes:
        o.append(boxt(x, 50, 180, 84, lines, NXS if x == 520 else PANEL, NX if x == 520 else AC, 14, bold_first=True))
    o.append(ar(202, 76, 256, 76)); o.append(ar(442, 76, 516, 76))
    o.append(ar(516, 110, 444, 110, NX)); o.append(ar(256, 110, 204, 110, NX))
    o.append(T(229, 158, '12 KB JSON', 13, fill=NX, bold=True))
    o.append(T(480, 158, '20 products', 13, fill=NX, bold=True))
    o.append(T(20, 194, 'Response size: 20 products × 0.6 KB = 12 KB', 14, 'start', bold=True))
    x0, w = 20, 600
    for i in range(20):
        o.append(R(x0 + i * 30, 206, 26, 22, ACS, AC, 3, 1.5))
    o.append(T(x0 + 600 + 10, 222, '0.6 KB each', 13, 'start', MUT))
    o.append(T(20, 272, 'Express capacity 40 requests/s at peak 8 requests/s', 14, 'start', bold=True))
    seg = 680 / 5
    o.append(R(20, 284, 680, 30, PANEL, L2, 5, 1.5))
    o.append(R(20, 284, seg, 30, ACS, AC, 5, 2))
    o.append(T(20 + seg / 2, 304, 'peak 8', 13, bold=True))
    for i in range(1, 5):
        o.append(L(20 + seg * (i + 1), 286, 20 + seg * (i + 1), 312, L2, 1.2, '3 3') if i < 4 else '')
        o.append(T(20 + seg * i + seg / 2, 304, '8', 13, fill=NX, bold=True))
    o.append(brace(20 + seg, 700, 324, NX))
    o.append(T(20 + seg + (680 - seg) / 2, 348, 'spare 40 − 8 = 32 = 4 × peak', 14, fill=NX, bold=True))
    return 364, ''.join(o)
FIG[5] = (f5, 'React asks the Express route, Express reads MongoDB and returns 20 products of 0.6 KB, a 12 KB JSON response. At a peak of 8 requests/s the 40 requests/s server has 32 spare, four times the peak.',
          'React, Express on Node.js and MongoDB in a row with request and reply arrows; below, twenty small blocks of 0.6 KB make 12 KB, and a capacity bar of 40 split into five blocks of 8, one used and four spare.')


# ---- 1.6 git places and DevTools bytes ----
def f6():
    o = [T(20, 26, 'Git: where the two changed files go', 15, 'start', bold=True)]
    places = [(20, 'Working folder', ['app.css  modified', 'logo.svg  untracked']), (200, 'Staging area', ['app.css', 'logo.svg']),
              (380, 'Local repo .git', ['new commit']), (560, 'Remote origin', ['code uploaded'])]
    for x, name, lines in places:
        remote = x == 560
        o.append(R(x, 44, 140, 98, NXS if remote else PANEL, NX if remote else AC, 8))
        o.append(T(x + 70, 66, name, 14, bold=True))
        for i, s in enumerate(lines):
            o.append(T(x + 70, 92 + i * 20, s, 13, fill=MUT if remote else INK))
    for x, cmd in ((160, 'git add'), (340, 'git commit'), (520, 'git push')):
        o.append(ar(x + 2, 104, x + 36, 104, NX if cmd == 'git push' else AC))
        o.append(Tb(x + 20, 160, cmd, 13, fill=NX if cmd == 'git push' else AC, bold=True))
    o.append(T(20, 186, '2 files to stage. Commit stays on this machine; only push uploads.', 14, 'start', MUT))
    # DevTools network panel
    y0 = 214
    o.append(T(20, y0, 'DevTools Network panel', 15, 'start', bold=True))
    o.append(R(20, y0 + 12, 680, 168, PANEL, L2, 8, 1.5))
    hdr = y0 + 36
    o.append(T(40, hdr, 'File', 13, 'start', MUT, True)); o.append(T(300, hdr, 'Status', 13, 'start', MUT, True))
    o.append(T(680, hdr, 'Transferred', 13, 'end', MUT, True))
    rows = [('index.html', '200', '4 KB', INK), ('app.css', '200 (from cache)', '0 KB', MUT), ('app.js', '200', '30 KB', INK),
            ('favicon.ico', '404 Not Found', '≈ 0 KB', LV)]
    for i, (f, s, b, c) in enumerate(rows):
        y = hdr + 26 + i * 24
        o.append(TM(40, y, f, 13, 'start', c)); o.append(T(300, y, s, 13, 'start', c, c == LV))
        o.append(T(680, y, b, 13, 'end', c, True))
    o.append(L(40, hdr + 116, 680, hdr + 116, L2, 1.2))
    o.append(T(40, hdr + 136, 'Total transferred 4 + 30 = 34 KB', 14, 'start', bold=True))
    return y0 + 196, ''.join(o)
FIG[6] = (f6, 'git add moves the 2 changed files to staging, git commit saves them in the local .git folder, and only git push uploads them. In DevTools only index.html and app.js cross the network, 4 + 30 = 34 KB, while app.css comes from cache and the favicon fails with 404.',
          'Four git places in a row joined by git add, git commit and git push; below, a DevTools network table lists index.html 4 KB, app.css from cache 0 KB, app.js 30 KB and favicon.ico 404, total 34 KB.')


spec = make_spec(FIG)


def text_fixes(k):
    return {}.get(k, [])
