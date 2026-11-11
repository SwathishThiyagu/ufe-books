"""Claude's hand-drawn figures for c-web-u6 (Web Technologies, unit 6: Node.js, Express and databases), one per chapter,
each drawn from that chapter's worked example with its own numbers, plus the sentences that describe a figure."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
ARC = {AC: 'n', L2: 'm', LV: 'l', NX: 'x'}


def ar(x1, y1, x2, y2, c=AC, w=2, dash=None):
    return L(x1, y1, x2, y2, c, w, dash, ARC[c])


# ---- 6.1 A, B, C, D in Node ----
def f1():
    o = [T(20, 26, 'app.js: where each line goes, and when it prints', 15, 'start', bold=True)]
    src = ["console.log('A')", "setTimeout(() =&gt; log('D'), 0)", "Promise.resolve().then(() =&gt; log('C'))", "console.log('B')"]
    dest = [0, 2, 1, 0]
    boxes = [(420, 50, 'Call stack, now', 'runs at once', ACS, AC), (420, 150, 'Microtask queue', 'drained when the stack empties', NXS, NX),
             (420, 250, 'Timers phase (libuv)', 'next loop pass', LVS, LV)]
    for x, y, a, b, f, c in boxes:
        o.append(R(x, y, 280, 70, f, c, 8)); o.append(T(x + 14, y + 26, a, 14, 'start', c, True)); o.append(T(x + 14, y + 50, b, 13, 'start', MUT))
    for i, s in enumerate(src):
        y = 56 + i * 76
        o.append(R(20, y, 330, 44, PANEL, L2, 6, 1.5)); o.append(TM(32, y + 27, s, 13, 'start', bold=True))
        b = boxes[dest[i]]
        c = b[5]
        o.append(ar(352, y + 22, 416, b[1] + 35 + (i - 1.5) * 4 if dest[i] == 0 else b[1] + 35, c, 1.8))
    o.append(T(20, 372, 'Printed order', 14, 'start', bold=True))
    out = [('A', 'stack', AC, ACS), ('B', 'stack', AC, ACS), ('C', 'microtask', NX, NXS), ('D', 'timer', LV, LVS)]
    for i, (s, k, c, f) in enumerate(out):
        x = 140 + i * 145
        o.append(R(x, 350, 136, 52, f, c, 8)); o.append(TM(x + 24, 383, s, 20, bold=True))
        o.append(T(x + 46, 372, f'position {i + 1}', 13, 'start', bold=True)); o.append(T(x + 46, 392, k, 13, 'start', MUT))
    return 418, ''.join(o)
FIG[1] = (f1, 'A and B are plain lines and print at once; the promise callback C waits in the microtask queue and the 0 ms timer D waits for the timers phase. Microtasks are drained first, so the order is A, B, C, D.',
          'Four source lines with arrows: the two console.log lines go to the call stack, the promise callback to the microtask queue, the setTimeout callback to the timers phase; the printed order is A, B, C, D.')


# ---- 6.2 caret and tilde ranges on a number line ----
def f2():
    o = [T(20, 26, 'Which versions does each range allow?', 15, 'start', bold=True)]
    def line(y, title, rng, lo, hi, ticks, fx, lab_lo, lab_hi):
        r = [T(20, y - 62, title, 14, 'start', bold=True), T(700, y - 62, rng, 13, 'end', MUT)]
        r.append(L(40, y, 690, y, L2, 1.5))
        r.append(R(fx(lo), y - 12, fx(hi) - fx(lo), 24, NXS, NX, 3, 0))
        r.append(f'<circle cx="{fx(lo):.1f}" cy="{y}" r="7" style="fill:var(--next);stroke:var(--fig);stroke-width:2"/>')
        r.append(f'<circle cx="{fx(hi):.1f}" cy="{y}" r="7" style="fill:var(--fig);stroke:var(--next);stroke-width:2.5"/>')
        r.append(T(fx(lo), y + 30, lab_lo, 13, fill=NX, bold=True)); r.append(T(fx(hi), y + 30, lab_hi, 13, fill=NX, bold=True))
        for v, s, ok in ticks:
            X = fx(v)
            c = AC if ok else LV
            r.append(L(X, y - 26, X, y - 12, c, 2))
            r.append(Tb(X, y - 34, f'{s} {"✓" if ok else "✗"}', 13, fill=c, bold=True))
        return ''.join(r)
    fx1 = lambda v: 60 + (v - 4.15) / (5.1 - 4.15) * 600
    # map versions to positions on a readable, not exact, scale
    pos = {'4.17.1': 4.171, '4.18.2': 4.30, '4.19.0': 4.55, '5.0.0': 5.0}
    o.append(line(124, 'express ^4.18.2', '4.18.2 ≤ version &lt; 5.0.0', pos['4.18.2'], pos['5.0.0'],
                  [(pos['4.17.1'], '4.17.1', False), (pos['4.19.0'], '4.19.0', True)], fx1, '4.18.2 ✓', '5.0.0 ✗'))
    fx2 = lambda v: 60 + (v - 1.20) / (1.34 - 1.20) * 600
    o.append(line(270, 'tool ~1.2.3', '1.2.3 ≤ version &lt; 1.3.0', 1.223, 1.30, [(1.29, '1.2.9', True)], fx2, '1.2.3', '1.3.0 ✗'))
    o.append(T(20, 336, 'Filled end: included. Open end: excluded. ^ fixes the major number; ~ fixes major and minor.', 13, 'start', MUT))
    o.append(T(20, 364, 'Allowed: 2 for ^4.18.2 (4.18.2, 4.19.0) and 1 for ~1.2.3 (1.2.9).', 14, 'start', bold=True))
    return 380, ''.join(o)
FIG[2] = (f2, 'The caret range ^4.18.2 runs from 4.18.2 up to but not including 5.0.0, so 4.18.2 and 4.19.0 are allowed. The tilde range ~1.2.3 stops before 1.3.0, so only 1.2.9 is allowed.',
          'Two number lines: express ^4.18.2 shaded from 4.18.2 (included) to 5.0.0 (excluded), with 4.17.1 outside and 4.19.0 inside; tool ~1.2.3 shaded from 1.2.3 to 1.3.0 (excluded) with 1.2.9 inside.')


# ---- 6.3 copying 1 GB in 64 KB chunks ----
def f3():
    o = [T(20, 26, 'Copying a 1 GB video: memory used at one time', 15, 'start', bold=True)]
    o.append(T(20, 62, 'fs.readFile', 14, 'start', LV, True))
    o.append(R(160, 44, 540, 30, LVS, LV, 4, 2)); o.append(T(430, 64, 'whole file in RAM: 1024 MB', 14, bold=True))
    o.append(T(20, 112, 'createReadStream', 14, 'start', NX, True))
    o.append(R(160, 94, 4, 30, NX, NX, 1, 1)); o.append(T(174, 114, '64 KB live at a time (0.0625 MB)', 14, 'start', bold=True))
    y = 170
    o.append(boxt(20, y, 140, 60, ['video.mp4', '1 GB on disk'], size=14, bold_first=True))
    o.append(boxt(210, y, 140, 60, ['read stream', 'highWaterMark 64 KB'], size=13, bold_first=True))
    o.append(boxt(400, y, 140, 60, ['write stream', 'backup disk'], NXS, NX, 13, bold_first=True))
    o.append(ar(162, y + 30, 206, y + 30)); o.append(ar(352, y + 30, 396, y + 30))
    o.append(R(358, y + 6, 32, 20, ACS, AC, 3, 1.5)); o.append(Tb(374, y + 52, 'pipe()', 13, fill=AC, bold=True))
    o.append(T(570, y + 20, '1024 MB × 1024', 13, 'start')); o.append(T(570, y + 40, '= 1,048,576 KB', 13, 'start'))
    o.append(T(570, y + 60, '÷ 64 KB', 13, 'start'))
    o.append(T(570, y + 84, '= 16,384 chunks', 15, 'start', AC, True))
    o.append(ar(470, y + 62, 470, y + 108, LV))
    o.append(R(330, y + 112, 370, 64, LVS, LV, 8))
    o.append(T(515, y + 136, "disk full: write stream emits 'error'", 13, bold=True))
    o.append(T(515, y + 158, 'no listener → uncaught, process exits', 13))
    o.append(T(20, y + 136, "Always attach .on('error', …)", 14, 'start', LV, True))
    o.append(T(20, y + 158, 'or a half-written copy is left behind.', 13, 'start', MUT))
    return y + 190, ''.join(o)
FIG[3] = (f3, 'readFile holds the whole 1024 MB file in memory, while a read stream piped to a write stream keeps only one 64 KB chunk live and repeats 16,384 times. If the disk fills and no error listener is attached, the process exits.',
          'Two memory bars: readFile 1024 MB and a stream sliver of 64 KB; below, video file to read stream to write stream with pipe, the chunk count 16,384, and the disk-full error path.')


# ---- 6.4 GET /users/42?lang=en through the chain ----
def f4():
    o = [T(20, 26, 'GET /users/42?lang=en: functions run in registration order', 15, 'start', bold=True)]
    steps = [('logger', 'next()'), ('express.json()', 'next()'), ('checkAuth', 'token valid: next()'), ("get('/users/:id')", 'handler')]
    for i, (a, b) in enumerate(steps):
        x = 20 + i * 172
        h = i == 3
        o.append(R(x, 50, 160, 64, NXS if h else PANEL, NX if h else AC, 8))
        o.append(TM(x + 80, 76, a, 13, bold=True)); o.append(T(x + 80, 100, b, 13, fill=MUT))
        if i < 3: o.append(ar(x + 161, 82, x + 171, 82))
    o.append(brace(20, 524, 126, AC))
    o.append(T(266, 150, '3 middleware functions before the handler', 13, fill=AC, bold=True))
    o.append(R(560, 170, 140, 50, 'var(--fig)', L2, 8, 1.5, '5 4'))
    o.append(TM(630, 192, 'errorHandler', 13, fill=MUT, bold=True)); o.append(T(630, 210, 'not reached', 13, fill=MUT))
    o.append(T(20, 194, 'Inside the handler', 14, 'start', bold=True))
    rows = [("req.params.id", "'42'", 'from :id in the path'), ('req.query.lang', "'en'", 'from ?lang=en')]
    for i, (a, b, c) in enumerate(rows):
        y = 220 + i * 34
        o.append(TM(36, y, a, 14, 'start', bold=True)); o.append(TM(220, y, b, 14, 'start', NX, True)); o.append(T(320, y, c, 13, 'start', MUT))
    o.append(R(20, 290, 680, 44, NXS, NX, 8))
    o.append(T(36, 318, '200', 16, 'start', NX, True))
    o.append(TM(90, 318, "res.status(200).json({ id: 42, lang: 'en' })", 14, 'start', bold=True))
    return 350, ''.join(o)
FIG[4] = (f4, 'The request passes logger, express.json() and checkAuth, each calling next(), before the /users/:id handler runs. The handler reads id \'42\' from the path and lang \'en\' from the query and replies 200; the error handler is never reached.',
          'A chain of logger, express.json, checkAuth and the users/:id handler; below, req.params.id is 42, req.query.lang is en, and the reply is 200 with id 42 and lang en.')


# ---- 6.5 the books API ----
def f5():
    o = [T(20, 26, 'CRUD routes for /books and their success codes', 15, 'start', bold=True)]
    cols = [(20, 'Action'), (130, 'Request'), (360, 'Status'), (530, 'Safe'), (610, 'Idempotent')]
    for x, h in cols:
        o.append(T(x + 6, 58, h, 13, 'start', MUT, True))
    rows = [('Create', 'POST /books', '201 Created', 'no', 'no'), ('List', 'GET /books', '200 OK', 'yes', 'yes'),
            ('Read', 'GET /books/7', '200 OK', 'yes', 'yes'), ('Replace', 'PUT /books/7', '200 OK', 'no', 'yes'),
            ('Delete', 'DELETE /books/7', '204 No Content', 'no', 'yes'), ('Missing', 'GET /books/99', '404 Not Found', 'yes', 'yes')]
    for i, (a, rq, st, sf, idm) in enumerate(rows):
        y = 68 + i * 38
        o.append(R(20, y, 680, 32, PANEL if i % 2 == 0 else 'var(--fig)', LN, 4, 1))
        o.append(T(26, y + 21, a, 14, 'start', bold=True)); o.append(TM(136, y + 21, rq, 14, 'start'))
        c = LV if st.startswith('4') else AC
        o.append(T(366, y + 21, st, 14, 'start', c, True))
        o.append(T(556, y + 21, sf, 13, 'middle', NX if sf == 'yes' else MUT, sf == 'yes'))
        o.append(T(660, y + 21, idm, 13, 'middle', NX if idm == 'yes' else MUT, idm == 'yes'))
    y = 310
    o.append(T(20, y, 'The same POST sent twice:', 14, 'start', bold=True))
    for i, idn in enumerate((7, 8)):
        x = 20 + i * 230
        o.append(R(x, y + 14, 210, 46, NXS, NX, 8))
        o.append(TM(x + 105, y + 34, 'POST /books', 13, bold=True)); o.append(T(x + 105, y + 52, f'201, new id {idn}', 13))
    o.append(T(490, y + 42, '= 2 books: POST is', 14, 'start', LV, True))
    o.append(T(490, y + 60, 'not idempotent', 14, 'start', LV, True))
    return y + 76, ''.join(o)
FIG[5] = (f5, 'Each CRUD action has its own method and success code: 201 for create, 200 for list, read and replace, 204 for delete and 404 for a missing book. Only GET is safe; GET, PUT and DELETE are idempotent, so two identical POSTs make books 7 and 8.',
          'A table of six requests on /books with status codes and safe and idempotent columns; below, the same POST sent twice creates ids 7 and 8.')


# ---- 6.6 insert, select and update in MySQL ----
def f6():
    o = [T(20, 26, 'Table students: 10 rows already, last id = 10', 15, 'start', bold=True)]
    tx, cw = 20, [60, 120, 70]
    hdr = ['id', 'name', 'marks']
    x = tx
    for j, h in enumerate(hdr):
        o.append(R(x, 44, cw[j], 28, ACS, AC, 0, 1.2)); o.append(T(x + cw[j] / 2, 63, h, 13, bold=True)); x += cw[j]
    o.append(R(tx, 72, sum(cw), 28, 'var(--fig)', L2, 0, 1.2, '4 3')); o.append(T(tx + sum(cw) / 2, 91, 'ids 1 to 10', 13, fill=MUT))
    rows = [('11', 'Asha', '85 → 90'), ('12', 'Bala', '72'), ('13', 'Chandan', '90')]
    for i, r in enumerate(rows):
        x = tx
        y = 100 + i * 28
        for j, v in enumerate(r):
            hl = (i == 0 and j == 2)
            o.append(R(x, y, cw[j], 28, NXS, NX, 0, 1.2))
            o.append(T(x + cw[j] / 2, y + 19, v, 13, fill=LV if hl else INK, bold=hl or j == 0))
            x += cw[j]
    o.append(T(tx, 208, 'green rows: added by one INSERT', 13, 'start', NX, True))
    res = [('INSERT … VALUES ? (3 rows)', ['affectedRows = 3', 'insertId = 11 (the first new id)'], AC),
           ('SELECT name WHERE marks &gt;= ?  [80]', ["2 rows: ['Asha', 'Chandan']", 'Bala 72 fails'], AC),
           ('UPDATE marks = marks + 5 WHERE id = 11', ['affectedRows = 1', 'changedRows = 1 (85 → 90)'], NX)]
    for i, (q, lines, c) in enumerate(res):
        y = 44 + i * 96
        o.append(R(300, y, 400, 84, PANEL, c, 8))
        o.append(TM(314, y + 24, q, 13, 'start', bold=True))
        for k, s in enumerate(lines):
            o.append(T(314, y + 50 + k * 20, s, 13, 'start', c if k == 0 else MUT, k == 0))
    o.append(T(20, 250, 'Each ? is filled from the values array,', 13, 'start', MUT))
    o.append(T(20, 270, 'never pasted into the SQL text.', 13, 'start', MUT))
    return 338, ''.join(o)
FIG[6] = (f6, 'One INSERT adds Asha, Bala and Chandan as ids 11, 12 and 13, reporting affectedRows 3 and insertId 11. The SELECT with marks ≥ 80 returns 2 rows, and the UPDATE of id 11 changes 85 to 90, one row affected and changed.',
          'The students table with ids 1 to 10 collapsed and new rows 11 Asha, 12 Bala, 13 Chandan; three result cards for INSERT (affectedRows 3, insertId 11), SELECT (2 rows) and UPDATE (affectedRows 1, changedRows 1).')


# ---- 6.7 three MongoDB calls on one collection ----
def f7():
    o = [T(20, 26, 'Collection students: three documents', 15, 'start', bold=True)]
    docs = [('Asha', 85), ('Bala', 72), ('Chandan', 90)]
    def doc(x, y, name, marks, f=PANEL, c=AC, extra=None, only_name=False):
        r = [R(x, y, 200, 70 if not only_name else 44, f, c, 8)]
        r.append(TM(x + 14, y + 26, f"name: '{name}'", 13, 'start', bold=True))
        if not only_name:
            r.append(TM(x + 14, y + 50, f'marks: {marks}', 13, 'start', bold=True))
            if extra: r.append(T(x + 186, y + 50, extra, 13, 'end', LV, True))
        return ''.join(r)
    o.append(TM(20, 64, 'find({marks: {$gte: 80}})', 14, 'start', bold=True))
    for i, (n, m) in enumerate(docs):
        hit = m >= 80
        o.append(doc(20 + i * 230, 78, n, m, NXS if hit else 'var(--fig)', NX if hit else L2))
    o.append(T(700, 64, '2 match: Asha, Chandan', 13, 'end', NX, True))
    o.append(TM(20, 190, "updateOne({name: 'Asha'}, {$set: {marks: 88}})", 14, 'start', bold=True))
    o.append(doc(20, 204, 'Asha', 88, ACS, AC, '85 → 88'))
    o.append(T(250, 236, 'matchedCount = 1', 14, 'start', bold=True)); o.append(T(250, 260, 'modifiedCount = 1', 14, 'start', bold=True))
    o.append(T(440, 248, '(setting 85 again would give 0)', 13, 'start', MUT))
    o.append(TM(20, 316, 'find({}, {name: 1, _id: 0})', 14, 'start', bold=True))
    for i, (n, m) in enumerate(docs):
        o.append(doc(20 + i * 230, 330, n, m, PANEL, AC, only_name=True))
    o.append(T(20, 400, '3 documents, 1 field each: the projection keeps name and drops _id.', 14, 'start', MUT))
    return 416, ''.join(o)
FIG[7] = (f7, 'The filter marks ≥ 80 matches Asha and Chandan; updateOne finds Asha and changes 85 to 88, so matched and modified are both 1; the projection returns all 3 documents with only the name field.',
          'Three student documents: a find with marks at least 80 highlights Asha and Chandan; updateOne sets Asha to 88 with matchedCount 1 and modifiedCount 1; a projection shows three documents holding only name.')


# ---- 6.8 the JWT time window ----
def f8():
    o = [T(20, 26, 'A token is valid only while now &lt; exp', 15, 'start', bold=True)]
    X0, X1 = 60, 660
    fx = lambda t: X0 + (t - 1700000000) / 4800 * (X1 - X0)
    y = 120
    o.append(R(fx(1700000000), y - 20, fx(1700003600) - fx(1700000000), 40, NXS, NX, 4, 2))
    o.append(T((fx(1700000000) + fx(1700003600)) / 2, y + 6, 'valid: 3600 s = 60 min', 15, bold=True))
    o.append(R(fx(1700003600), y - 20, fx(1700004800) - fx(1700003600), 40, LVS, LV, 4, 1.5, '5 3'))
    o.append(T((fx(1700004200) + fx(1700004800)) / 2, y + 6, 'expired', 14, fill=LV, bold=True))
    o.append(L(X0, y + 40, X1, y + 40, L2, 1.5))
    for t, lab, c in ((1700000000, 'iat 1700000000', NX), (1700003600, 'exp 1700003600', NX), (1700004200, 'request 1700004200', LV)):
        o.append(L(fx(t), y - 34, fx(t), y + 46, c, 2, None if t != 1700004200 else '4 3'))
    o.append(T(fx(1700000000), y + 64, 'iat', 13, fill=NX, bold=True)); o.append(T(fx(1700000000), y + 82, '1700000000', 13, fill=MUT))
    o.append(T(fx(1700003600), y + 64, 'exp', 13, fill=NX, bold=True)); o.append(T(fx(1700003600), y + 82, '1700003600', 13, fill=MUT))
    o.append(T(fx(1700004200) + 6, y - 40, 'request at 1700004200', 13, 'end', LV, True))
    o.append(brace(fx(1700003600), fx(1700004200), y + 100, LV))
    o.append(T((fx(1700003600) + fx(1700004200)) / 2, y + 124, '600 s late', 13, fill=LV, bold=True))
    o.append(T(20, 280, 'Lifetime = exp − iat = 1700003600 − 1700000000 = 3600 s = 60 min', 14, 'start', bold=True))
    o.append(T(20, 304, 'Late by 1700004200 − 1700003600 = 600 s (10 min): the server returns 401.', 14, 'start', bold=True))
    return 320, ''.join(o)
FIG[8] = (f8, 'The token is valid from iat to exp, 3600 s or 60 minutes. The request arrives 600 s after exp, so the server rejects it with 401 Unauthorized.',
          'A time line with iat at 1700000000 and exp at 1700003600 marking a 3600-second valid window; a request at 1700004200 falls 600 seconds into the expired part.')


# ---- 6.9 the pipeline and the port mapping ----
def f9():
    o = [T(20, 26, 'One CI run against a manual deploy (seconds)', 15, 'start', bold=True)]
    X0, X1 = 110, 690
    fx = lambda s: X0 + s / 1200 * (X1 - X0)
    stages = [('install', 40), ('test', 25), ('build', 30), ('deploy', 15)]
    x = 0
    for i, (n, s) in enumerate(stages):
        o.append(R(fx(x), 46, fx(s) - fx(0), 34, ACS if i % 2 == 0 else NXS, AC if i % 2 == 0 else NX, 2, 1.5))
        x += s
    o.append(T(X0 - 10, 68, 'CI', 14, 'end', bold=True))
    o.append(T(fx(110) + 10, 68, 'install 40 + test 25 + build 30 + deploy 15 = 110 s', 14, 'start', AC, True))
    o.append(R(fx(0), 96, fx(1200) - fx(0), 34, LVS, LV, 2, 1.5))
    o.append(T(X0 - 10, 118, 'manual', 14, 'end', bold=True))
    o.append(T(fx(600), 118, '20 min × 60 = 1200 s', 14, bold=True))
    o.append(xaxis(X0, X1, 144, [0, 300, 600, 900, 1200], fx))
    o.append(T(20, 196, 'Saving: 1200 − 110 = 1090 s, about 18 min 10 s per deploy.', 14, 'start', bold=True))
    # port mapping
    o.append(T(20, 240, 'docker run -p 8080:3000 shop', 15, 'start', bold=True))
    o.append(R(20, 256, 300, 96, PANEL, AC, 10)); o.append(T(36, 278, 'Host machine', 14, 'start', bold=True))
    o.append(R(220, 290, 84, 40, ACS, AC, 6)); o.append(T(262, 315, ':8080', 14, bold=True))
    o.append(R(400, 256, 300, 96, NXS, NX, 10)); o.append(T(416, 278, 'Container "shop"', 14, 'start', bold=True))
    o.append(R(416, 290, 84, 40, PANEL, NX, 6)); o.append(T(458, 315, ':3000', 14, bold=True))
    o.append(T(520, 306, 'node server.js', 13, 'start')); o.append(T(520, 324, 'EXPOSE 3000', 13, 'start', MUT))
    o.append(ar(306, 310, 412, 310))
    o.append(T(36, 316, 'browser', 13, 'start', MUT))
    o.append(T(20, 380, 'Host port first, container port second.', 13, 'start', MUT))
    return 396, ''.join(o)
FIG[9] = (f9, 'The four CI stages take 40 + 25 + 30 + 15 = 110 s against 1200 s by hand, saving 1090 s. docker run -p 8080:3000 sends host port 8080 to the app listening on 3000 inside the container.',
          'Two bars to the same scale: CI stages install 40, test 25, build 30, deploy 15 totalling 110 seconds, and a manual deploy of 1200 seconds; below, host port 8080 mapped to container port 3000.')


spec = make_spec(FIG)


def text_fixes(k):
    return {
        6: [('affactedRows check: 3 rows inserted with insertId = 11', 'affectedRows = 3 (3 rows inserted) with insertId = 11')],
    }.get(k, [])
