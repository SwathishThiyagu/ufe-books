"""Claude's hand-drawn figures for c-web-u4 (Web Technologies, unit 4: server-side scripting with PHP and Java), one per
chapter, each drawn from that chapter's worked example with its own numbers, plus the sentences that describe a figure."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
ARC = {AC: 'n', L2: 'm', LV: 'l', NX: 'x'}


def ar(x1, y1, x2, y2, c=AC, w=2, dash=None):
    return L(x1, y1, x2, y2, c, w, dash, ARC[c])


def var(x, y, name, val, w=130, f=PANEL, c=AC):
    return R(x, y, w, 56, f, c, 8) + TM(x + w / 2, y + 22, name, 14, fill=MUT) + T(x + w / 2, y + 45, val, 17, bold=True)


def cellrow(x, y, chars, w=30, h=34, fill=ACS, stroke=AC, hl=None, hlf=NXS, hlc=NX):
    o = []
    for i, ch in enumerate(chars):
        f, c = (hlf, hlc) if hl and i in hl else (fill, stroke)
        o.append(R(x + i * w, y, w - 3, h, f, c, 4, 1.5))
        o.append(TM(x + i * w + (w - 3) / 2, y + h / 2 + 5, ch if ch != ' ' else '␣', 15, bold=True))
    return ''.join(o)


# ---- 4.1 the shop bill in PHP ----
def f1():
    o = [T(20, 26, 'What each PHP line puts in a variable', 15, 'start', bold=True)]
    o.append(var(20, 50, '$price', '250'))
    o.append(var(20, 130, '$qty', '3'))
    o.append(ar(152, 78, 226, 112)); o.append(ar(152, 158, 226, 124))
    o.append(var(230, 90, '$total', '750'))
    o.append(Tb(190, 108, '×', 15, fill=AC, bold=True))
    o.append(ar(362, 118, 436, 118))
    o.append(Tb(399, 104, '× 0.18', 13, fill=AC, bold=True))
    o.append(var(440, 90, '$gst', '135'))
    o.append(ar(296, 148, 296, 236)); o.append(ar(505, 148, 330, 236))
    o.append(Tb(420, 196, '750 + 135', 13, fill=AC, bold=True))
    o.append(var(230, 240, '$pay', '885', 130, NXS, NX))
    o.append(ar(362, 268, 436, 268, NX))
    o.append(R(440, 244, 260, 48, 'var(--panel)', L2, 8, 1.5))
    o.append(TM(570, 274, 'Pay: ₹885', 18, bold=True))
    o.append(T(570, 312, 'what echo prints', 13, fill=MUT))
    o.append(T(20, 350, '18% GST is 18 ÷ 100 = 0.18 of the total, so 750 × 0.18 = 135.', 14, 'start', MUT))
    return 366, ''.join(o)
FIG[1] = (f1, 'The script multiplies $price 250 by $qty 3 to get $total 750, takes 18% of it as $gst 135, and adds the two into $pay 885, which echo prints as Pay: ₹885.',
          'Variable boxes: price 250 and qty 3 multiply into total 750; total times 0.18 gives gst 135; total plus gst gives pay 885; echo prints Pay: ₹885.')


# ---- 4.2 two servers, two ports on one laptop ----
def f2():
    o = [T(20, 26, 'One laptop, two servers, two ports', 15, 'start', bold=True)]
    o.append(boxt(20, 110, 130, 80, ['Browser', 'on the same', 'laptop'], size=14, bold_first=True))
    o.append(boxt(250, 50, 170, 70, ['Apache (XAMPP)', 'Listen 80'], size=14, bold_first=True))
    o.append(boxt(250, 180, 170, 70, ['Tomcat', 'connector 8080'], NXS, NX, 14, bold_first=True))
    o.append(ar(152, 136, 246, 86)); o.append(ar(152, 166, 246, 214, NX))
    o.append(R(470, 50, 230, 70, PANEL, L2, 8, 1.5))
    o.append(TM(484, 76, 'C:/xampp/htdocs/', 13, 'start', MUT)); o.append(TM(484, 100, '  shop/pay.php', 14, 'start', bold=True))
    o.append(R(470, 180, 230, 70, PANEL, L2, 8, 1.5))
    o.append(TM(484, 206, 'webapps/shop.war', 14, 'start', bold=True)); o.append(T(484, 230, 'becomes context /shop', 13, 'start', MUT))
    o.append(ar(422, 85, 466, 85, L2)); o.append(ar(422, 215, 466, 215, L2))
    o.append(R(20, 280, 680, 72, PANEL, L2, 8, 1.5))
    o.append(TM(36, 306, 'http://localhost/shop/pay.php', 15, 'start', AC, True))
    o.append(T(684, 306, 'port 80 is the http default: not written', 13, 'end', MUT))
    o.append(TM(36, 336, 'http://localhost:8080/shop/', 15, 'start', NX, True))
    o.append(T(684, 336, '8080 is not the default: must be written', 13, 'end', MUT))
    o.append(T(20, 384, 'Port 80 taken by another program? Stop it, or change Listen 80 in httpd.conf to a free port.', 14, 'start', LV, True))
    o.append(T(20, 406, 'Two programs can never share one port.', 13, 'start', MUT))
    return 422, ''.join(o)
FIG[2] = (f2, 'Apache listens on port 80 and serves files under htdocs, so pay.php is http://localhost/shop/pay.php; Tomcat listens on 8080 and turns shop.war into /shop, so its URL must say :8080. If port 80 is taken, Apache must move to a free port.',
          'A browser connects to Apache on port 80, which serves htdocs/shop/pay.php, and to Tomcat on port 8080, which serves the shop.war context; the two URLs are listed below.')


# ---- 4.3 fact(4) down and back up ----
def f3():
    o = [T(20, 26, 'fact(4): calls go down, results come back up', 15, 'start', bold=True)]
    calls = [('fact(4)', '4 × fact(3) = 4 × 6 = 24', 'returns 6'), ('fact(3)', '3 × fact(2) = 3 × 2 = 6', 'returns 2'),
             ('fact(2)', '2 × fact(1) = 2 × 1 = 2', 'returns 1'), ('fact(1)', 'base case: returns 1', '')]
    for i, (c, waits, ret) in enumerate(calls):
        x, y = 30 + i * 70, 50 + i * 72
        base = i == 3
        o.append(R(x, y, 250, 52, NXS if base else PANEL, NX if base else AC, 8))
        o.append(TM(x + 16, y + 22, c, 15, 'start', bold=True))
        o.append(T(x + 16, y + 42, waits, 13, 'start', MUT))
        if i < 3:
            o.append(ar(x + 40, y + 54, x + 110 - 30, y + 70, AC))
            o.append(ar(x + 70 + 230, y + 72 + 26, x + 254, y + 30, NX))
            o.append(Tb(x + 300, y + 62, ret, 13, fill=NX, bold=True))
    o.append(T(30, 68 + 4 * 72 - 10, 'fact(4) = 24.  Without the base case the calls never stop.', 14, 'start', bold=True))
    o.append(T(30, 68 + 4 * 72 + 20, 'for $i = 1 to 5 prints:', 14, 'start'))
    for j, v in enumerate([1, 2, 6, 24, 120]):
        o.append(R(200 + j * 70, 68 + 4 * 72 + 2, 60, 28, ACS, AC, 5, 1.5))
        o.append(T(230 + j * 70, 68 + 4 * 72 + 21, str(v), 14, bold=True))
    return 68 + 4 * 72 + 44, ''.join(o)
FIG[3] = (f3, 'fact(4) waits on fact(3), which waits on fact(2), down to the base case fact(1) = 1; the results then come back up as 2, 6 and 24. The loop over 1 to 5 prints 1, 2, 6, 24, 120.',
          'A staircase of calls fact(4), fact(3), fact(2), fact(1); return arrows carry 1, 2, 6 and 24 back up; below, the loop output 1, 2, 6, 24, 120.')


# ---- 4.4 clean the phone number, then match ----
def f4():
    o = [T(20, 26, "Input '98765 43210'", 15, 'start', bold=True)]
    o.append(cellrow(40, 44, list('98765 43210'), hl={5}, hlf=LVS, hlc=LV))
    o.append(T(40 + 11 * 30 + 12, 66, '11 characters, one space', 13, 'start', MUT))
    o.append(ar(110, 82, 110, 112))
    o.append(TM(124, 104, "preg_replace('/\\s+/', '', $phone)", 13, 'start', AC, True))
    o.append(cellrow(40, 118, list('9876543210'), hl={0}))
    # pattern pieces
    y = 186
    o.append(TM(20, y, "preg_match('/^[6-9]\\d{9}$/', …)", 14, 'start', bold=True))
    o.append(brace(40, 67, y + 16, NX, True)); o.append(TM(54, y + 36, '[6-9]', 13, fill=NX, bold=True))
    o.append(brace(70, 337, y + 16, AC, True)); o.append(TM(204, y + 36, '\\d{9}: nine more digits', 13, fill=AC, bold=True))
    o.append(R(470, 118, 230, 34, NXS, NX, 6)); o.append(T(585, 140, 'first digit 9: result 1', 14, bold=True))
    # second input
    y2 = 266
    o.append(T(20, y2, "Input '5876543210' (no space to remove)", 15, 'start', bold=True))
    o.append(cellrow(40, y2 + 16, list('5876543210'), hl={0}, hlf=LVS, hlc=LV))
    o.append(R(470, y2 + 16, 230, 34, LVS, LV, 6)); o.append(T(585, y2 + 38, 'first digit 5: result 0', 14, bold=True))
    o.append(T(20, y2 + 84, '^ and $ anchor the pattern, so the whole string must be exactly 10 digits starting 6 to 9.', 14, 'start', MUT))
    return y2 + 100, ''.join(o)
FIG[4] = (f4, 'preg_replace removes the space, leaving 9876543210. The anchored pattern needs a first digit from 6 to 9 and then exactly nine digits, so it returns 1 here and 0 for 5876543210, which starts with 5.',
          'Character cells for 98765 43210 with the space marked, then 9876543210 after cleaning, with the pattern parts [6-9] over the first digit and \\d{9} over the rest; the second input 5876543210 fails on its first digit.')


# ---- 4.5 the same pairs by GET and by POST ----
def f5():
    o = [T(20, 26, 'The form sends name=Anu and marks=78', 15, 'start', bold=True)]
    def req(x, title, lines, hl):
        r = [T(x, 58, title, 14, 'start', bold=True), R(x, 68, 330, 136, PANEL, L2, 8, 1.5)]
        for i, s in enumerate(lines):
            y = 94 + i * 26
            if i == hl:
                r.append(R(x + 8, y - 17, 314, 24, NXS, NX, 4, 1.5))
            r.append(TM(x + 14, y, s, 13, 'start', bold=(i == hl)))
        return ''.join(r)
    o.append(req(20, 'GET: pairs in the URL', ['GET /result.php?name=Anu&amp;marks=78', 'Host: localhost', '', '(no body)'], 0))
    o.append(req(370, 'POST: pairs in the body', ['POST /result.php', 'Content-Type: application/', '  x-www-form-urlencoded', '', 'name=Anu&amp;marks=78'], 4))
    o.append(T(20, 236, 'PHP on the server (POST):', 14, 'start', bold=True))
    steps = [("$_POST['name']", "'Anu'"), ('filter_input', '78 (an int)'), ('0 ≤ 78 ≤ 100 ?', 'true'), ('htmlspecialchars', 'name escaped')]
    for i, (a, b) in enumerate(steps):
        x = 20 + i * 172
        o.append(R(x, 250, 156, 60, PANEL, AC, 8))
        o.append(TM(x + 78, 274, a, 13))
        o.append(T(x + 78, 298, b, 15, fill=AC, bold=True))
        if i < 3: o.append(ar(x + 158, 280, x + 170, 280))
    o.append(ar(360, 312, 360, 340, NX))
    o.append(R(250, 344, 220, 40, NXS, NX, 8)); o.append(T(360, 370, 'Anu scored 78', 16, bold=True))
    return 400, ''.join(o)
FIG[5] = (f5, 'GET puts name=Anu&amp;marks=78 after ? in the URL; POST sends the same pairs as the request body. PHP reads the name, validates marks as an integer from 0 to 100, escapes the name and prints Anu scored 78.',
          'Two request listings: GET with the pairs in the request line and no body, POST with the pairs in the body; below, four PHP steps lead to the output Anu scored 78.')


# ---- 4.6 the cookie holds only the session ID ----
def f6():
    o = [T(20, 26, 'Anu logs in: what each side keeps', 15, 'start', bold=True)]
    o.append(R(20, 50, 220, 150, PANEL, AC, 10)); o.append(T(130, 74, 'Browser', 15, bold=True))
    o.append(R(36, 90, 188, 92, ACS, AC, 6, 1.5)); o.append(T(130, 112, 'cookie jar', 13, fill=MUT))
    o.append(TM(130, 140, 'PHPSESSID=abc123', 14, bold=True)); o.append(T(130, 164, 'Max-Age 1800 s', 13))
    o.append(R(480, 50, 220, 150, PANEL, NX, 10)); o.append(T(590, 74, 'Server session store', 15, bold=True))
    o.append(R(496, 90, 188, 92, NXS, NX, 6, 1.5)); o.append(TM(590, 112, 'abc123', 14, fill=MUT, bold=True))
    o.append(T(590, 140, "user = Anu", 14, bold=True)); o.append(T(590, 164, 'cart_total = 750', 14, bold=True))
    o.append(ar(476, 104, 244, 104, NX))
    o.append(Tb(360, 96, 'Set-Cookie: PHPSESSID=abc123', 13, fill=NX, bold=True))
    o.append(ar(244, 160, 476, 160))
    o.append(Tb(360, 152, 'Cookie: PHPSESSID=abc123', 13, fill=AC, bold=True))
    o.append(T(360, 186, 'next request: GET /cart', 13, fill=MUT))
    o.append(T(360, 128, 'HttpOnly, SameSite=Lax', 13, fill=MUT))
    # timeline
    X0, X1 = 60, 660
    fx = lambda s: X0 + s / 2400 * (X1 - X0)
    y = 268
    o.append(T(20, 240, 'Time after login (seconds)', 14, 'start', bold=True))
    o.append(R(fx(0), y, fx(1800) - fx(0), 26, ACS, AC, 4, 2)); o.append(T(fx(900), y + 18, 'cookie lives: 30 min × 60 = 1800 s', 13, bold=True))
    o.append(R(fx(1800), y, fx(2400) - fx(1800), 26, 'var(--fig)', LV, 4, 1.5, '4 3')); o.append(T(fx(2100), y + 18, 'cookie gone', 13, fill=LV, bold=True))
    o.append(R(fx(0), y + 36, fx(2400) - fx(0), 22, NXS, NX, 4, 1.5))
    o.append(T(fx(1200), y + 52, 'server data (Anu, 750) stays until garbage collection', 13, bold=True))
    o.append(xaxis(X0, X1, y + 70, [0, 600, 1200, 1800, 2400], fx))
    o.append(T(20, y + 124, 'After 1800 s the next visit starts a new, empty session with a new ID.', 14, 'start', MUT))
    return y + 140, ''.join(o)
FIG[6] = (f6, 'The browser keeps only the session ID abc123; Anu and the ₹750 cart stay in the server store, found by that ID on each request. After 1800 s the cookie is dropped, while the server data waits for garbage collection.',
          'Browser cookie jar holds PHPSESSID=abc123; the server store maps abc123 to user Anu and cart_total 750; Set-Cookie goes to the browser and Cookie comes back; a timeline shows the cookie lasting 1800 seconds.')


# ---- 4.7 one servlet object, three requests ----
def f7():
    o = [T(20, 26, 'GreetServlet from start-up to shutdown', 15, 'start', bold=True)]
    y = 60
    o.append(L(30, y + 60, 700, y + 60, L2, 2))
    stages = [(30, 110, ['load class', 'new object'], PANEL, AC), (160, 90, ['init()', '1 time'], ACS, AC)]
    for x, w, lines, f, c in stages:
        o.append(boxt(x, y + 30, w, 60, lines, f, c, 14, bold_first=True))
    for i in range(3):
        x = 280 + i * 120
        o.append(boxt(x, y + 30, 106, 60, [f'service()', f'request {i + 1}'], NXS, NX, 14, bold_first=True))
        o.append(ar(x + 53, y + 92, x + 53, y + 140, NX))
        o.append(R(x, y + 144, 106, 54, PANEL, L2, 6, 1.5))
        o.append(TM(x + 53, y + 164, 'doGet()', 13, bold=True)); o.append(T(x + 53, y + 186, 'Anu scored 78', 13))
        o.append(Tb(x + 53, y + 14, f'GET /greet', 13, fill=NX, bold=True))
    o.append(boxt(640, y + 30, 70, 60, ['destroy()', '1 time'], size=13, bold_first=True))
    o.append(T(30, y + 236, 'One object serves all three requests: init() 1, service() 3, destroy() 1.', 14, 'start', bold=True))
    o.append(T(30, y + 258, 'Request data stays in local variables, never in an instance field.', 13, 'start', MUT))
    return y + 274, ''.join(o)
FIG[7] = (f7, 'The container loads GreetServlet and creates one object, calls init() once, runs service() for each of the three GET requests, each printing Anu scored 78 through doGet(), and calls destroy() once at shutdown.',
          'A timeline: load and create, init once, three service calls each leading to doGet printing Anu scored 78, then destroy once.')


# ---- 4.8 the same sentence by JSP and by JSF ----
def f8():
    o = [T(20, 26, 'Two ways to print "Anu scored 78"', 15, 'start', bold=True)]
    def col(x, title, boxes, f, c):
        r = [T(x + 160, 58, title, 14, bold=True, fill=c)]
        for i, (a, b) in enumerate(boxes):
            y = 72 + i * 78
            r.append(R(x, y, 320, 58, f if i == len(boxes) - 1 else PANEL, c, 8))
            r.append(TM(x + 160, y + 24, a, 13, bold=True))
            r.append(T(x + 160, y + 46, b, 13, fill=MUT))
            if i < len(boxes) - 1: r.append(ar(x + 160, y + 60, x + 160, y + 74, c))
        return ''.join(r)
    o.append(col(20, 'JSP with EL', [('?name=Anu&amp;marks=78', 'query string in the URL'),
                                    ('param map', 'name → Anu, marks → 78'),
                                    ('${param.name} scored ${param.marks}', 'show.jsp, run as a servlet'),
                                    ('Anu scored 78', 'HTML sent to the browser')], ACS, AC))
    o.append(col(380, 'JSF with a bean', [('form: Anu, 78, Show', 'typed, then posted back'),
                                         ('setName("Anu"), setMarks(78)', 'values converted into marksBean'),
                                         ('#{marksBean.name} scored …', 'result.xhtml after navigation'),
                                         ('Anu scored 78', 'HTML sent to the browser')], NXS, NX))
    o.append(T(20, 404, 'JSP reads the request directly; JSF copies the typed values into the bean first.', 14, 'start', bold=True))
    o.append(T(20, 426, 'show.jsp is translated to a servlet and compiled once, on its first request.', 13, 'start', MUT))
    return 442, ''.join(o)
FIG[8] = (f8, 'JSP reads name and marks straight from the query string with ${param…}; JSF first copies the typed values into marksBean on postback and then reads #{marksBean…}. Both print Anu scored 78.',
          'Two columns: JSP goes from the query string to the param map to the EL line to the output; JSF goes from the form to the bean setters to the result page to the same output, Anu scored 78.')


# ---- 4.9 GET and POST through Spring ----
def f9():
    o = [T(20, 26, 'GET /api/students/1 through Spring', 15, 'start', bold=True)]
    boxes = [(20, ['@RestController', 'one(1)']), (200, ['StudentRepository', 'findById(1L)']), (380, ['Hibernate', 'writes the SQL'])]
    for x, lines in boxes:
        o.append(boxt(x, 44, 160, 56, lines, size=14, bold_first=True))
    o.append(ar(182, 72, 196, 72)); o.append(ar(362, 72, 376, 72))
    o.append(ar(542, 72, 566, 72))
    # table
    o.append(T(630, 60, 'table student', 13, fill=MUT, bold=True))
    tx, cw = 570, [36, 56, 52]
    hdr = ['id', 'name', 'marks']
    rows = [('1', 'Anu', '78'), ('2', 'Ravi', '65')]
    x = tx
    for j, h in enumerate(hdr):
        o.append(R(x, 70, cw[j], 26, ACS, AC, 0, 1.2)); o.append(T(x + cw[j] / 2, 88, h, 13, bold=True)); x += cw[j]
    for i, r in enumerate(rows):
        x = tx
        for j, v in enumerate(r):
            new = i == 1
            o.append(R(x, 96 + i * 26, cw[j], 26, NXS if new else PANEL, NX if new else AC, 0, 1.2))
            o.append(T(x + cw[j] / 2, 114 + i * 26, v, 13, bold=(i == 0)))
            x += cw[j]
    o.append(T(tx + 72, 168, 'row 2 added by POST', 13, fill=NX, bold=True))
    o.append(R(20, 130, 520, 34, 'var(--fig)', L2, 6, 1.5))
    o.append(TM(280, 152, 'SELECT * FROM student WHERE id = 1', 14, bold=True))
    o.append(ar(460, 102, 460, 126, L2))
    o.append(T(20, 202, 'Reply', 14, 'start', bold=True))
    o.append(R(20, 212, 680, 40, ACS, AC, 8))
    o.append(T(36, 238, '200', 15, 'start', AC, True))
    o.append(TM(90, 238, '{"id":1,"name":"Anu","marks":78}', 14, 'start', bold=True))
    o.append(T(684, 238, 'Jackson turns the object into JSON', 13, 'end', MUT))
    o.append(T(20, 290, 'POST /api/students  with  {"name":"Ravi","marks":65}', 14, 'start', bold=True))
    o.append(T(20, 314, '@RequestBody builds a Student → repo.save() → INSERT → IDENTITY gives id 2', 13, 'start', MUT))
    o.append(R(20, 326, 680, 40, NXS, NX, 8))
    o.append(T(36, 352, '201', 15, 'start', NX, True))
    o.append(TM(90, 352, '{"id":2,"name":"Ravi","marks":65}', 14, 'start', bold=True))
    o.append(T(684, 352, 'Created', 13, 'end', MUT))
    return 382, ''.join(o)
FIG[9] = (f9, 'The controller calls findById(1L), Hibernate runs SELECT … WHERE id = 1, and the row (1, Anu, 78) comes back as JSON with status 200. A POST of Ravi with 65 marks is saved as row 2 and answered with 201.',
          'Controller, repository and Hibernate boxes lead to the SQL SELECT and the student table with rows 1 Anu 78 and 2 Ravi 65; replies 200 with Anu as JSON and 201 with Ravi as JSON.')


spec = make_spec(FIG)


def text_fixes(k):
    return {}.get(k, [])
