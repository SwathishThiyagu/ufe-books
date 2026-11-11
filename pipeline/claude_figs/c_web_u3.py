"""Claude's hand-drawn figures for c-web-u3 (Web Technologies, unit 3: JavaScript, DOM, AJAX and XML), one per chapter,
each drawn from that chapter's worked example with its own numbers, plus the sentences that describe a figure."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
ARC = {AC: 'n', L2: 'm', LV: 'l', NX: 'x'}


def ar(x1, y1, x2, y2, c=AC, w=2, dash=None):
    return L(x1, y1, x2, y2, c, w, dash, ARC[c])


def cells(x, y, vals, w=56, h=36, fill=ACS, stroke=AC, size=15, mono=False, dim=()):
    o = []
    for i, v in enumerate(vals):
        d = i in dim
        o.append(R(x + i * w, y, w - 6, h, 'var(--fig)' if d else fill, L2 if d else stroke, 5, 1.5 if d else 2, '4 3' if d else None))
        f = TM if mono else T
        o.append(f(x + i * w + (w - 6) / 2, y + h / 2 + size * 0.36, str(v), size, fill=MUT if d else INK, bold=not d))
    return ''.join(o)


def diamond(x, y, w, h, s, fill=PANEL, stroke=AC):
    pts = f'{x:.1f},{y - h / 2:.1f} {x + w / 2:.1f},{y:.1f} {x:.1f},{y + h / 2:.1f} {x - w / 2:.1f},{y:.1f}'
    return f'<polygon points="{pts}" style="fill:{fill};stroke:{stroke};stroke-width:2"/>' + TM(x, y + 5, s, 14, bold=True)


# ---- 3.1 marks = 72 through the else-if ladder ----
def f1():
    o = [T(20, 26, 'marks = 72 through the else-if ladder', 15, 'start', bold=True)]
    tests = [('72 >= 90', 'A'), ('72 >= 75', 'B'), ('72 >= 60', 'C')]
    x, y = 140, 80
    o.append(boxt(80, 44, 120, 30, ['start'], size=13))
    o.append(ar(x, 76, x, 92))
    for i, (t, g) in enumerate(tests):
        yy = 122 + i * 92
        hit = g == 'C'
        o.append(diamond(x, yy, 170, 58, t, NXS if hit else PANEL, NX if hit else AC))
        # yes branch to the right
        o.append(ar(x + 86, yy, x + 146, yy, NX if hit else L2, 2, None if hit else '5 4'))
        o.append(T(x + 116, yy - 8, 'true' if hit else '', 13, fill=NX, bold=True))
        o.append(boxt(x + 150, yy - 20, 110, 40, [f'print {g}'], NXS if hit else 'var(--fig)', NX if hit else L2, 14, bold_first=hit))
        if not hit:
            o.append(ar(x, yy + 30, x, yy + 60, AC))
            o.append(Tb(x + 32, yy + 48, 'false', 13, fill=AC, bold=True))
    o.append(L(x, 122 + 2 * 92 + 30, x, 122 + 2 * 92 + 54, L2, 1.5, '5 4'))
    o.append(T(x, 122 + 2 * 92 + 72, 'else: print D (skipped)', 13, fill=MUT))
    # loop trace
    o.append(TM(470, 70, 'for i = 1 … 5: sum += i', 13, 'start', bold=True))
    vals = [(1, 1), (2, 3), (3, 6), (4, 10), (5, 15)]
    for j, (i, s) in enumerate(vals):
        yy = 92 + j * 38
        o.append(T(490, yy + 20, f'i = {i}', 13, 'start', MUT))
        o.append(R(550, yy + 2, 140, 28, NXS if i == 5 else ACS, NX if i == 5 else AC, 5, 1.5))
        o.append(T(620, yy + 21, f'sum = {s}', 14, bold=True))
    o.append(T(490, 300, 'i = 6: 6 &lt;= 5 false, stop', 13, 'start', MUT))
    o.append(T(470, 340, 'Outputs: C, C (switch), 15', 14, 'start', bold=True))
    return 410, ''.join(o)
FIG[1] = (f1, 'With marks = 72 the first two tests are false and 72 >= 60 is true, so the ladder prints C and skips the rest; the switch(true) form takes the same path. The loop adds 1 to 5, so sum ends at 15.',
          'Flowchart: start, test 72 >= 90 false, test 72 >= 75 false, test 72 >= 60 true leading to print C. Beside it the loop trace sum = 1, 3, 6, 10, 15.')


# ---- 3.2 average, filter and map on one array ----
def f2():
    o = [T(20, 26, 'marks = [45, 72, 90, 38]', 15, 'start', bold=True)]
    x0 = 170
    o.append(T(20, 66, 'original', 14, 'start', bold=True))
    o.append(cells(x0, 44, [45, 72, 90, 38], 76))
    o.append(T(x0 + 4 * 76 + 10, 66, 'never changes', 13, 'start', MUT))
    y = 120
    o.append(T(20, y + 22, 'loop: average', 14, 'start', bold=True))
    o.append(T(x0, y + 22, '45 + 72 + 90 + 38 = 245,   245 ÷ 4 = 61.25', 14, 'start'))
    y = 176
    o.append(T(20, y + 22, 'filter(m >= 60)', 14, 'start', bold=True))
    o.append(cells(x0, y, [45, 72, 90, 38], 76, dim=(0, 3)))
    o.append(ar(x0 + 4 * 76 + 4, y + 18, x0 + 4 * 76 + 52, y + 18))
    o.append(cells(x0 + 4 * 76 + 60, y, [72, 90], 76, fill=NXS, stroke=NX))
    o.append(T(x0, y + 56, '45 and 38 are below 60: dropped', 13, 'start', MUT))
    y = 266
    o.append(T(20, y + 22, 'map(m + 5)', 14, 'start', bold=True))
    o.append(cells(x0, y, [50, 77, 95, 43], 76, fill=NXS, stroke=NX))
    for i in range(4):
        o.append(T(x0 + i * 76 + 35, y - 6, '+5', 13, fill=AC, bold=True))
    o.append(T(x0 + 4 * 76 + 10, y + 22, 'a new array, same length', 13, 'start', MUT))
    o.append(T(20, 344, 'Results: average 61.25,  [72, 90],  [50, 77, 95, 43]', 14, 'start', bold=True))
    return 360, ''.join(o)
FIG[2] = (f2, 'From one array of four marks: a loop adds them to 245 and divides by 4 for an average of 61.25, filter keeps [72, 90], and map makes the new array [50, 77, 95, 43]. The original array never changes.',
          'The array 45, 72, 90, 38; below it the average 61.25, a filter row where 45 and 38 are greyed out giving 72, 90, and a map row giving 50, 77, 95, 43.')


# ---- 3.3 a click through capture and bubble ----
def f3():
    o = [T(20, 26, 'Click on the Pay ₹500 button: the event path', 15, 'start', bold=True)]
    path = ['window', 'document', 'body', 'div#outer', 'button#b']
    x, w = 130, 140
    for i, n in enumerate(path):
        y = 50 + i * 62
        tgt = i == 4
        o.append(boxt(x, y, w, 40, [n], NXS if tgt else PANEL, NX if tgt else AC, 14, bold_first=True))
        if i < 4:
            o.append(ar(x - 30, y + 30, x - 30, y + 72, AC))
            o.append(ar(x + w + 30, y + 72, x + w + 30, y + 30, NX))
    o.append(T(x - 44, 180, 'capture', 13, 'end', AC, True)); o.append(T(x - 44, 198, '(down)', 13, 'end', AC))
    o.append(T(x + w + 44, 180, 'bubble', 13, 'start', NX, True)); o.append(T(x + w + 44, 198, '(up)', 13, 'start', NX))
    o.append(T(x + w / 2, 352, 'target', 13, fill=NX, bold=True))
    cases = [('(a) ordinary listeners', 'button, then div', '2 lines'),
             ('(b) button calls stopPropagation()', 'button only', '1 line'),
             ('(c) div listener {capture: true}', 'div, then button', '2 lines')]
    for i, (a, b, c) in enumerate(cases):
        y = 50 + i * 100
        o.append(R(400, y, 300, 84, PANEL, L2, 8, 1.5))
        o.append(T(416, y + 24, a, 13, 'start', bold=True))
        o.append(T(416, y + 50, 'logs: ' + b, 14, 'start', AC, True))
        o.append(T(416, y + 72, c, 13, 'start', MUT))
    return 368, ''.join(o)
FIG[3] = (f3, 'The click travels down from window to the button (capture) and back up (bubble). Ordinary listeners log button then div; stopPropagation() stops it at the button; a capture listener on the div runs first, on the way down.',
          'A vertical path window, document, body, div#outer, button#b with a downward capture arrow and an upward bubble arrow; three cards give the logs: button then div, button only, div then button.')


# ---- 3.4 the DOM tree the script changes ----
def f4():
    o = [T(20, 26, 'The script walks the tree and changes three things', 15, 'start', bold=True)]
    def nd(x, y, s, c=AC, f=PANEL, w=None, dash=None):
        w = w or tw(s, 14) + 28
        return R(x - w / 2, y - 16, w, 32, f, c, 7, 2, dash) + TM(x, y + 5, s, 14, bold=True)
    pts = {'document': (120, 66), 'html': (120, 130), 'body': (120, 194), 'h1#t': (90, 270), 'ul#items': (250, 270),
           'li1': (190, 346), 'li2': (330, 346)}
    for a, b in (('document', 'html'), ('html', 'body'), ('body', 'h1#t'), ('body', 'ul#items'), ('ul#items', 'li1'), ('ul#items', 'li2')):
        (x1, y1), (x2, y2) = pts[a], pts[b]
        o.append(L(x1, y1 + 16, x2, y2 - 16, NX if b == 'li2' else L2, 2 if b == 'li2' else 1.8, '5 4' if b == 'li2' else None))
    for k in ('document', 'html', 'body', 'h1#t', 'ul#items'):
        o.append(nd(*pts[k], k))
    o.append(nd(*pts['li1'], 'li.red'))
    o.append(nd(*pts['li2'], 'li', NX, NXS, 60, '5 3'))
    o.append(T(20, 306, '"Cart" → "Cart: 2 items"', 13, 'start', AC, True))
    o.append(T(190, 380, '"Pen"', 13, fill=MUT)); o.append(T(330, 380, '"Tea"  (new)', 13, fill=NX, bold=True))
    steps = [('1', 'count #items li', '→ 1'),
             ('2', "h1 text = 'Cart: 2 items'", ''),
             ('3', "append new li 'Tea'", ''),
             ('4', "first li gets class 'red'", ''),
             ('5', 'count #items li', '→ 2')]
    for i, (n, s, v) in enumerate(steps):
        y = 64 + i * 56
        o.append(C(440, y, 12, AC)); o.append(T(440, y + 5, n, 13, fill='var(--fig)', bold=True))
        o.append(T(462, y + 5, s, 14, 'start'))
        if v: o.append(T(700, y + 5, v, 15, 'end', NX, True))
    o.append(T(440, 352, 'Output: 1 2', 15, 'start', bold=True))
    return 396, ''.join(o)
FIG[4] = (f4, 'The tree runs document → html → body, which holds h1#t and ul#items. The script renames the heading, appends a new li "Tea" (dashed) and marks the first li red, so the li count goes from 1 to 2.',
          'DOM tree: document, html, body, then h1#t and ul#items; ul#items has li.red "Pen" and a new dashed li "Tea". Five numbered steps beside it; the counts printed are 1 and 2.')


# ---- 3.5 one var binding against three let bindings ----
def f5():
    o = [T(20, 26, 'Three setTimeout callbacks read the loop variable later', 15, 'start', bold=True)]
    o.append(TM(20, 62, 'for (var i = 0; i &lt; 3; i++)', 14, 'start', bold=True))
    o.append(R(100, 120, 120, 50, LVS, LV, 8))
    o.append(TM(160, 151, 'i = 3', 16, bold=True))
    o.append(T(160, 192, 'one binding,', 13, fill=MUT)); o.append(T(160, 209, 'final value 3', 13, fill=MUT))
    for j in range(3):
        y = 84 + j * 50
        o.append(boxt(250, y, 90, 36, [f'cb {j + 1}'], size=13))
        o.append(ar(248, y + 18, 224, 145 + (j - 1) * 10, LV))
    o.append(TM(20, 272, 'prints 3 3 3', 15, 'start', LV, True))
    # let
    X = 380
    o.append(L(360, 44, 360, 290, LN, 1.5))
    o.append(TM(X + 10, 62, 'for (let j = 0; j &lt; 3; j++)', 14, 'start', bold=True))
    for j in range(3):
        y = 84 + j * 50
        o.append(R(X + 30, y, 100, 36, NXS, NX, 8))
        o.append(TM(X + 80, y + 23, f'j = {j}', 15, bold=True))
        o.append(boxt(X + 200, y, 90, 36, [f'cb {j + 1}'], size=13))
        o.append(ar(X + 198, y + 18, X + 134, y + 18, NX))
    o.append(T(X + 80, 252, 'a fresh j each pass', 13, fill=MUT))
    o.append(TM(X + 10, 272, 'prints 0 1 2', 15, 'start', NX, True))
    o.append(L(20, 296, 700, 296, LN, 1.5))
    o.append(TM(20, 326, 'const add = (a, b) =&gt; a + b;   add(2, 3) → 5', 14, 'start', bold=True))
    return 342, ''.join(o)
FIG[5] = (f5, 'With var there is one i for the whole function, and all three callbacks read it after the loop ends at 3, so they print 3 3 3. With let each pass gets its own j, so the callbacks print 0 1 2.',
          'Left: three callbacks all point to one var binding i = 3 and print 3 3 3. Right: each callback points to its own let binding j = 0, 1, 2 and prints 0 1 2. Below: add(2, 3) returns 5.')


# ---- 3.6 the event loop orders A, D, C, B ----
def f6():
    o = [T(20, 26, 'Where each callback waits, and the order it prints', 15, 'start', bold=True)]
    o.append(R(20, 44, 200, 190, PANEL, AC, 8))
    o.append(T(120, 66, 'Call stack', 14, bold=True))
    for i, s in enumerate(["log('A')", 'setTimeout(…)', 'Promise…then(…)', "log('D')"]):
        o.append(R(36, 80 + i * 36, 168, 28, ACS if 'log' in s else 'var(--fig)', AC if 'log' in s else L2, 4, 1.5))
        o.append(TM(120, 99 + i * 36, s, 13, bold='log' in s))
    o.append(boxt(270, 44, 170, 56, ['Timer Web API', '0 ms'], size=14, bold_first=True))
    o.append(ar(206, 130, 266, 78, L2))
    o.append(R(500, 44, 200, 80, NXS, NX, 8)); o.append(T(600, 66, 'Microtask queue', 14, bold=True))
    o.append(R(540, 80, 120, 30, PANEL, NX, 4, 1.5)); o.append(TM(600, 100, "log('C')", 13, bold=True))
    o.append(R(500, 150, 200, 80, LVS, LV, 8)); o.append(T(600, 172, 'Timer (task) queue', 14, bold=True))
    o.append(R(540, 186, 120, 30, PANEL, LV, 4, 1.5)); o.append(TM(600, 206, "log('B')", 13, bold=True))
    o.append(ar(206, 166, 496, 96, NX))
    o.append(ar(442, 80, 496, 196, LV))
    o.append(T(20, 270, 'Empty the stack, then every microtask, then one timer task:', 14, 'start'))
    out = [('A', 'sync', AC, ACS), ('D', 'sync', AC, ACS), ('C', 'microtask', NX, NXS), ('B', 'timer', LV, LVS)]
    for i, (s, k, c, f) in enumerate(out):
        x = 40 + i * 170
        o.append(R(x, 288, 130, 54, f, c, 8))
        o.append(TM(x + 65, 314, s, 20, bold=True)); o.append(T(x + 65, 334, k, 13, fill=MUT))
        if i < 3: o.append(ar(x + 134, 315, x + 166, 315, AC))
    o.append(T(20, 374, '2 sync + 1 microtask + 1 timer = 4 logs', 14, 'start', bold=True))
    return 390, ''.join(o)
FIG[6] = (f6, 'A and D run on the call stack first. The promise callback C waits in the microtask queue and the 0 ms timer callback B in the timer queue; microtasks are drained first, so the output is A, D, C, B.',
          'The call stack holds log A, setTimeout, Promise then and log D; the timer callback B goes to the timer queue and C to the microtask queue; the output row reads A, D, C, B.')


# ---- 3.7 readyState from 0 to 4 ----
def f7():
    o = [T(20, 26, 'One XMLHttpRequest for /api/marks.json', 15, 'start', bold=True)]
    st = [('0', 'UNSENT', 'new XMLHttpRequest()'), ('1', 'OPENED', "open('GET', …)"), ('2', 'HEADERS', 'status line arrives'),
          ('3', 'LOADING', 'body streams in'), ('4', 'DONE', 'body complete')]
    for i, (n, name, why) in enumerate(st):
        x = 20 + i * 140
        last = n == '4'
        o.append(R(x, 50, 120, 70, NXS if last else PANEL, NX if last else AC, 8))
        o.append(T(x + 60, 78, n, 22, bold=True)); o.append(T(x + 60, 104, name, 13, fill=MUT, bold=True))
        o.append(T(x + 60, 140, why, 13, fill=MUT))
        if i < 4: o.append(ar(x + 122, 85, x + 138, 85))
    o.append(brace(160, 580, 160, AC))
    o.append(T(370, 184, 'each change fires onreadystatechange; the guard returns on 1, 2 and 3', 13, fill=AC, bold=True))
    o.append(ar(640, 154, 640, 214, NX))
    o.append(R(470, 218, 230, 46, PANEL, NX, 8)); o.append(T(585, 246, 'readyState 4: check status', 14, bold=True))
    o.append(ar(520, 266, 360, 300, NX)); o.append(ar(650, 266, 650, 300, LV))
    o.append(R(140, 304, 380, 92, NXS, NX, 8))
    o.append(T(330, 326, 'status 200', 14, fill=NX, bold=True))
    o.append(TM(330, 350, 'JSON.parse → data[0]', 13))
    o.append(TM(330, 378, '&lt;div id="out"&gt; Asha: 72', 15, bold=True))
    o.append(R(540, 304, 160, 92, LVS, LV, 8))
    o.append(T(620, 326, 'status 404', 14, fill=LV, bold=True))
    o.append(T(620, 350, 'no parsing', 13))
    o.append(TM(620, 378, 'Error 404', 15, bold=True))
    return 412, ''.join(o)
FIG[7] = (f7, 'The request moves through readyState 0 to 4; the callback ignores 1, 2 and 3. At 4 it checks the status: 200 parses the JSON and writes Asha: 72, while 404 writes Error 404 and parses nothing.',
          'Five boxes for readyState 0 UNSENT, 1 OPENED, 2 HEADERS_RECEIVED, 3 LOADING, 4 DONE; at 4 the status check splits into 200, which shows Asha: 72, and 404, which shows Error 404.')


# ---- 3.8 the book record against DTD and XSD ----
def f8():
    o = [T(20, 26, 'The record as a tree, and three checks on &lt;price&gt;₹350&lt;/price&gt;', 15, 'start', bold=True)]
    def nd(x, y, s, w=150, f=PANEL, c=AC):
        return R(x - w / 2, y - 18, w, 36, f, c, 7) + TM(x, y + 5, s, 14, bold=True)
    o.append(nd(170, 70, 'bookstore'))
    o.append(nd(170, 150, 'book', 110)); o.append(T(240, 155, 'id="b1"', 13, 'start', NX, True))
    o.append(nd(90, 236, 'title', 100)); o.append(nd(250, 236, 'price', 100, NXS, NX))
    o.append(L(170, 88, 170, 132, L2, 1.8)); o.append(L(160, 168, 100, 218, L2, 1.8)); o.append(L(180, 168, 240, 218, L2, 1.8))
    o.append(T(90, 274, '"Web Tech"', 13, fill=MUT)); o.append(T(250, 274, '"₹350"', 13, fill=NX, bold=True))
    o.append(T(182, 114, 'book+ (one or more)', 13, 'start', MUT))
    o.append(T(170, 300, 'children in order: title, then price', 13, fill=MUT))
    rows = [('Well-formed?', 'yes', 'one root, tags match; ₹ is fine in UTF-8', NX),
            ('DTD-valid?', 'yes', 'price is #PCDATA: any text passes', NX),
            ('XSD-valid?', 'no', 'xs:integer allows a sign and digits only', LV)]
    for i, (q, a, why, c) in enumerate(rows):
        y = 52 + i * 78
        o.append(R(360, y, 340, 64, NXS if c == NX else LVS, c, 8))
        o.append(T(376, y + 26, q, 14, 'start', bold=True))
        o.append(T(684, y + 26, a, 16, 'end', c, True))
        o.append(T(376, y + 50, why, 13, 'start'))
    o.append(T(20, 336, 'Writing &lt;price&gt;350&lt;/price&gt; passes all three.', 14, 'start', bold=True))
    return 352, ''.join(o)
FIG[8] = (f8, 'The record is a tree: bookstore holds book (id="b1"), which holds title then price. With ₹350 as the price it is well-formed and DTD-valid, because #PCDATA takes any text, but not XSD-valid, because xs:integer allows digits only.',
          'Tree of bookstore, book with id b1, title Web Tech and price ₹350; three result cards: well-formed yes, DTD-valid yes, XSD-valid no.')


# ---- 3.9 one jQuery chain ----
def f9():
    o = [T(20, 26, 'Each call returns a set, so the next call can follow', 15, 'start', bold=True)]
    steps = [("$('#items li')", ['Pen', 'Book', 'Bag'], (0, 1, 2), '', 3),
             (".addClass('sel')", ['Pen', 'Book', 'Bag'], (0, 1, 2), 'sel', 3),
             ('.first()', ['Pen', 'Book', 'Bag'], (0,), 'sel', 1),
             (".text('Pen (new)')", ['Pen (new)', 'Book', 'Bag'], (0,), 'sel', 1)]
    for i, (call, items, sel, cls, n) in enumerate(steps):
        y = 46 + i * 70
        o.append(TM(20, y + 30, call, 15, 'start', bold=True))
        for j, it in enumerate(items):
            x = 230 + j * 130
            on = j in sel
            o.append(R(x, y + 8, 118, 36, NXS if on else 'var(--fig)', NX if on else L2, 6, 2 if on else 1.2, None if on else '4 3'))
            o.append(T(x + 59, y + 31, it + (f'  .{cls}' if cls else ''), 13, fill=INK if on else MUT, bold=on))
        o.append(T(700, y + 31, f'{n} in set', 13, 'end', AC, True))
        if i < 3: o.append(ar(60, y + 40, 60, y + 70 - 2, AC, 1.6))
    y = 46 + 4 * 70 + 10
    o.append(TM(20, y, "$('#items li').each(…)  console:", 14, 'start', bold=True))
    for j, s in enumerate(['Pen (new)', 'Book', 'Bag']):
        o.append(TM(380 + j * 120, y, s, 14, 'start', NX, True))
    return y + 18, ''.join(o)
FIG[9] = (f9, 'The chain starts with a set of 3 items, adds class sel to all 3, narrows to the first, and sets its text to Pen (new). A separate .each() loop then prints Pen (new), Book and Bag.',
          'Four rows for the chain: select 3 items, add class sel to all 3, first narrows to Pen, text sets Pen (new); the console prints Pen (new), Book, Bag.')


spec = make_spec(FIG)


def text_fixes(k):
    return {}.get(k, [])
