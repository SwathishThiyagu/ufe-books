"""Claude's hand-drawn figures for c-web-u5 (Web Technologies, unit 5: React and Angular front ends), one per chapter,
each drawn from that chapter's worked example with its own numbers, plus the sentences that describe a figure."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
ARC = {AC: 'n', L2: 'm', LV: 'l', NX: 'x'}


def ar(x1, y1, x2, y2, c=AC, w=2, dash=None):
    return L(x1, y1, x2, y2, c, w, dash, ARC[c])


def panel(x, y, w, h, title, lines, f=PANEL, c=AC, mono=True, size=13, gap=22):
    o = [R(x, y, w, h, f, c, 8), T(x + 12, y + 22, title, 14, 'start', c if c != L2 else INK, True)]
    for i, s in enumerate(lines):
        o.append((TM if mono else T)(x + 12, y + 46 + i * gap, s, size, 'start'))
    return ''.join(o)


# ---- 5.1 JSX to createElement to DOM ----
def f1():
    o = [T(20, 26, 'title = "Dosa": one JSX snippet, three forms', 15, 'start', bold=True)]
    o.append(panel(20, 44, 680, 66, 'JSX you write', ['&lt;div className="card"&gt;&lt;h2&gt;{title}&lt;/h2&gt;&lt;p&gt;2 items&lt;/p&gt;&lt;/div&gt;']))
    o.append(ar(360, 112, 360, 136))
    o.append(T(372, 129, 'the compiler turns each tag into one call', 13, 'start', MUT))
    # createElement tree
    o.append(T(20, 160, 'React.createElement calls', 14, 'start', AC, True))
    o.append(R(150, 172, 420, 40, ACS, AC, 6)); o.append(TM(360, 197, 'createElement("div", {className: "card"}, …)', 13, bold=True))
    o.append(R(40, 252, 300, 40, ACS, AC, 6)); o.append(TM(190, 277, 'createElement("h2", null, "Dosa")', 13, bold=True))
    o.append(R(380, 252, 300, 40, ACS, AC, 6)); o.append(TM(530, 277, 'createElement("p", null, "2 items")', 13, bold=True))
    o.append(L(300, 214, 190, 250, L2, 1.8)); o.append(L(420, 214, 530, 250, L2, 1.8))
    o.append(T(140, 312, '{title} is the one expression: it gives "Dosa"', 13, fill=NX, bold=True))
    o.append(ar(360, 322, 360, 344))
    o.append(panel(20, 348, 680, 66, 'HTML in the browser (className becomes class)', ['&lt;div class="card"&gt;&lt;h2&gt;Dosa&lt;/h2&gt;&lt;p&gt;2 items&lt;/p&gt;&lt;/div&gt;'], NXS, NX))
    o.append(T(20, 444, 'Count: 3 elements, 3 createElement calls, 1 JavaScript expression.', 14, 'start', bold=True))
    return 460, ''.join(o)
FIG[1] = (f1, 'Each JSX tag becomes one React.createElement call, so the card is 3 calls for 3 elements, and the one expression {title} becomes "Dosa". The browser finally holds plain HTML with class="card".',
          'The JSX snippet on top, a tree of three createElement calls for div, h2 and p in the middle, and the final HTML with class card, Dosa and 2 items at the bottom.')


# ---- 5.2 three setCount calls in one click ----
def f2():
    o = [T(20, 26, 'One click calls setCount three times (count starts at 0)', 15, 'start', bold=True)]
    def lane(y, title, calls, vals, result, c, f):
        r = [T(20, y, title, 14, 'start', c, True)]
        for i, (s, v) in enumerate(zip(calls, vals)):
            x = 20 + i * 170
            r.append(R(x, y + 12, 154, 62, PANEL, c, 8))
            r.append(TM(x + 77, y + 36, s, 13, bold=True))
            r.append(T(x + 77, y + 60, v, 13, fill=MUT))
            if i < 2: r.append(ar(x + 156, y + 43, x + 168, y + 43, c))
        r.append(ar(530, y + 43, 556, y + 43, c))
        r.append(R(560, y + 12, 140, 62, f, c, 8))
        r.append(T(630, y + 36, 'one render', 13, fill=MUT)); r.append(T(630, y + 62, result, 18, bold=True))
        return ''.join(r)
    o.append(lane(60, 'Direct value: each call reads the same count = 0', ['setCount(0 + 1)'] * 3, ['queues 1', 'queues 1', 'queues 1'], 'count = 1', LV, LVS))
    o.append(lane(186, 'Updater function: each call gets the previous result', ['c =&gt; c + 1'] * 3, ['0 → 1', '1 → 2', '2 → 3'], 'count = 3', NX, NXS))
    o.append(T(20, 300, 'React batches the three updates into one render in both cases; only the updater form chains them.', 14, 'start', MUT))
    return 316, ''.join(o)
FIG[2] = (f2, 'The handler was made in the render where count = 0, so three direct calls all queue 1 and the batched render shows 1. The updater form passes each result to the next call, 0 → 1 → 2 → 3, so the render shows 3.',
          'Two lanes of three calls: setCount(0 + 1) three times queues 1 each time and renders count = 1; c => c + 1 three times goes 0 to 1 to 2 to 3 and renders count = 3.')


# ---- 5.3 the controlled-input loop ----
def f3():
    o = [T(20, 26, 'One keystroke = one trip round the loop', 15, 'start', bold=True)]
    pts = [(130, 90, ['&lt;input value={password}&gt;', 'shows the state']), (470, 90, ['onChange(e)', 'e.target.value']),
           (470, 210, ['setPassword(…)', 'state updated']), (130, 210, ['React re-renders', 'input from state'])]
    for x, y, lines in pts:
        o.append(R(x - 110, y - 30, 220, 60, PANEL, AC, 8))
        o.append(TM(x, y - 6, lines[0], 13, bold=True)); o.append(T(x, y + 16, lines[1], 13, fill=MUT))
    o.append(ar(242, 90, 358, 90)); o.append(Tb(300, 80, 'user types', 13, fill=AC, bold=True))
    o.append(ar(470, 122, 470, 178)); o.append(ar(358, 210, 242, 210)); o.append(ar(130, 178, 130, 122))
    # pass123 keystrokes
    y = 280
    o.append(T(20, y, 'Typing pass123: 7 keystrokes, so 7 onChange calls', 14, 'start', bold=True))
    for i, ch in enumerate('pass123'):
        o.append(R(20 + i * 44, y + 12, 38, 36, ACS, AC, 5, 1.5)); o.append(TM(39 + i * 44, y + 36, ch, 16, bold=True))
        o.append(T(39 + i * 44, y + 66, str(i + 1), 13, fill=MUT))
    o.append(R(350, y + 12, 350, 36, NXS, NX, 6)); o.append(T(525, y + 36, "length 7 ≥ 6: passes, error stays ''", 13, bold=True))
    o.append(R(350, y + 56, 350, 36, LVS, LV, 6)); o.append(T(525, y + 80, "'123': length 3 &lt; 6: 'Password too short'", 13, bold=True))
    o.append(T(20, y + 120, "Email ravi@example.com is 4 + 1 + 11 = 16 characters. On submit, e.preventDefault() stops the page reload.", 13, 'start', MUT))
    return y + 136, ''.join(o)
FIG[3] = (f3, 'One keystroke is one trip round the loop: onChange fires with e.target.value, the setter stores it in state, and React redraws the input from state. Typing pass123 runs the loop 7 times, and length 7 passes the ≥ 6 check.',
          'A loop of four boxes: input shows state, onChange reads the value, the setter updates state, React re-renders the input; below, the seven keystrokes of pass123 and the length checks for pass123 and 123.')


# ---- 5.4 six paths against four routes ----
def f4():
    o = [T(20, 26, 'The router matches each URL to one route', 15, 'start', bold=True)]
    routes = [('/', 'Home'), ('/posts', 'PostList'), ('/posts/:id', 'PostDetail'), ('*', 'NotFound')]
    ry = {}
    for i, (p, c) in enumerate(routes):
        y = 56 + i * 86
        ry[c] = y + 25
        hot = c in ('PostDetail', 'NotFound')
        o.append(R(430, y, 270, 50, NXS if c == 'PostDetail' else (LVS if c == 'NotFound' else PANEL), NX if c == 'PostDetail' else (LV if c == 'NotFound' else AC), 8))
        o.append(TM(446, y + 31, p, 15, 'start', bold=True)); o.append(T(684, y + 31, c, 14, 'end', bold=True))
    paths = [('/', 'Home'), ('/posts', 'PostList'), ('/posts/42', 'PostDetail'), ('/posts/abc', 'PostDetail'),
             ('/posts/42/comments', 'NotFound'), ('/blog', 'NotFound')]
    for i, (p, c) in enumerate(paths):
        y = 56 + i * 56
        col = NX if c == 'PostDetail' else (LV if c == 'NotFound' else AC)
        o.append(R(20, y, 210, 38, PANEL, col, 6, 1.5)); o.append(TM(32, y + 24, p, 14, 'start', bold=True))
        o.append(ar(232, y + 19, 426, ry[c], col, 1.8))
    o.append(T(250, 400, ":id takes exactly one segment: id = '42' or 'abc'", 13, 'start', NX, True))
    o.append(T(250, 422, 'three segments or an unknown path fall to *', 13, 'start', LV, True))
    o.append(T(20, 460, 'PostDetail: 2 paths.  NotFound: 2 paths.', 14, 'start', bold=True))
    return 476, ''.join(o)
FIG[4] = (f4, 'Each of the six URLs is matched to one route: /posts/42 and /posts/abc fill :id and render PostDetail, while /posts/42/comments (three segments) and /blog fall through to * and render NotFound.',
          'Six URLs on the left with arrows to four routes on the right: / to Home, /posts to PostList, /posts/42 and /posts/abc to PostDetail, /posts/42/comments and /blog to NotFound.')


# ---- 5.5 tsc checks the types, then erases them ----
def f5():
    o = [T(20, 26, 'tsc checks every call and object against the types', 15, 'start', bold=True)]
    o.append(panel(20, 44, 680, 76, 'TypeScript source', ['function add(a: number, b: number): number', 'interface User { id: number; name: string; email?: string }']))
    rows = [('add(2, 3)', 'compiles', 'returns 5', NX, NXS), ("add('2', 3)", 'error TS2345', "string is not number", LV, LVS),
            ("{ id: 7, name: 'Ravi' }", 'accepted', 'email is optional', NX, NXS), ("{ id: '7', name: 'Ravi' }", 'error TS2322', 'id must be number', LV, LVS)]
    for i, (code, verdict, why, c, f) in enumerate(rows):
        y = 140 + i * 50
        o.append(R(20, y, 680, 40, f, c, 6, 1.5))
        o.append(TM(36, y + 26, code, 14, 'start', bold=True))
        o.append(T(400, y + 26, verdict, 14, 'start', c, True))
        o.append(T(684, y + 26, why, 13, 'end'))
    y = 350
    o.append(ar(360, y - 6, 360, y + 18))
    o.append(T(372, y + 10, 'types erased', 13, 'start', MUT))
    o.append(panel(20, y + 22, 680, 54, 'JavaScript the browser runs', ['function add(a, b) { return a + b; }'], PANEL, L2))
    o.append(T(20, y + 106, "Without the check, plain JavaScript gives '2' + 3 = '23'.", 14, 'start', LV, True))
    return y + 122, ''.join(o)
FIG[5] = (f5, 'tsc compares each call and object with the declared types: add(2, 3) and { id: 7, name: \'Ravi\' } pass, while a string argument or a string id is rejected. The types are then erased, so the browser runs plain JavaScript.',
          'The TypeScript add function and User interface; four checks below: add(2, 3) compiles to 5, add with a string fails TS2345, the object with id 7 is accepted, the object with id string 7 fails TS2322; then the erased JavaScript.')


# ---- 5.6 Angular bindings in both directions ----
def f6():
    o = [T(20, 26, 'ProductCard: what each binding shows', 15, 'start', bold=True)]
    o.append(R(20, 44, 210, 180, PANEL, AC, 8)); o.append(T(125, 66, 'class fields', 14, bold=True))
    for i, s in enumerate(["id: 3", "name: 'Filter coffee'", 'price: 2499', 'qty: 3']):
        o.append(TM(34, 94 + i * 30, s, 13, 'start', bold=(s == 'qty: 3')))
    rows = [("{{ product.name | uppercase }}", 'FILTER COFFEE', AC), ("{{ product.price | currency:'INR' }}", '₹2,499.00', AC),
            ('[(ngModel)]="qty"', 'user types 3', NX), ('Total: {{ price * qty | currency }}', 'Total: ₹7,497.00', AC)]
    for i, (tpl, out, c) in enumerate(rows):
        y = 50 + i * 46
        o.append(R(244, y, 318, 34, 'var(--fig)', L2, 6, 1.2)); o.append(TM(254, y + 22, tpl, 13, 'start'))
        if c == NX:
            o.append(ar(580, y + 17, 566, y + 17, NX)); o.append(ar(240, y + 17, 232, 156, NX))
        else:
            o.append(ar(564, y + 17, 580, y + 17, AC))
        o.append(T(586, y + 22, out, 14, 'start', c, True))
    o.append(T(244, 252, '2499 × 3 = 7497 rupees', 13, 'start', MUT))
    o.append(R(20, 280, 236, 44, NXS, NX, 8)); o.append(TM(138, 307, '(click) → add.emit(product)', 13, bold=True))
    o.append(ar(258, 302, 286, 302, NX))
    o.append(R(290, 280, 410, 44, PANEL, NX, 8)); o.append(TM(302, 300, 'parent (add)="onAdd($event)"', 13, 'start', bold=True))
    o.append(TM(302, 317, "{id: 3, name: 'Filter coffee', price: 2499}", 13, 'start', NX))
    o.append(T(20, 352, 'Values flow down into the view with {{ }}; typing and clicks flow back up. qty is not sent by emit.', 13, 'start', MUT))
    return 368, ''.join(o)
FIG[6] = (f6, 'The class fields flow into the template: the pipes print FILTER COFFEE and ₹2,499.00, and once the user types 3 into the ngModel input the total shows ₹7,497.00. The click emits the product object up to the parent as $event.',
          'Class fields on the left, four template lines in the middle with their output on the right: FILTER COFFEE, ₹2,499.00, the typed qty 3, Total ₹7,497.00; below, the click emits the product to the parent.')


# ---- 5.7 the service worker cache ----
def f7():
    o = [T(20, 26, 'First online visit: cache.addAll stores the shell', 15, 'start', bold=True)]
    X0, s = 20, 680 / 132
    parts = [('index.html', 4), ('app.js', 120), ('style.css', 8)]
    x = X0
    for name, kb in parts:
        w = kb * s
        o.append(R(x, 44, w, 34, ACS, AC, 3, 1.5))
        if w > 90: o.append(T(x + w / 2, 66, f'{name}  {kb} KB', 13, bold=True))
        x += w
    o.append(T(X0, 98, 'index.html 4 KB', 13, 'start', MUT)); o.append(T(700, 98, 'style.css 8 KB', 13, 'end', MUT))
    o.append(T(360, 124, '4 + 120 + 8 = 132 KB in 3 files', 14, bold=True))
    o.append(T(20, 166, 'Later, in airplane mode:', 15, 'start', bold=True))
    o.append(boxt(20, 190, 110, 56, ['Page'], size=14, bold_first=True))
    o.append(boxt(200, 190, 140, 56, ['Service', 'worker'], size=14, bold_first=True))
    o.append(ar(132, 206, 196, 206)); o.append(T(164, 198, '', 13))
    o.append(boxt(420, 180, 280, 56, ['GET /index.html: cache hit', 'cached shell served, app opens'], NXS, NX, 13, bold_first=True))
    o.append(ar(342, 208, 416, 208, NX))
    o.append(ar(342, 232, 416, 284, LV))
    o.append(boxt(420, 262, 280, 56, ['GET /api/price: cache miss', 'network fails'], LVS, LV, 13, bold_first=True))
    o.append(ar(560, 320, 560, 346, LV))
    o.append(boxt(420, 350, 280, 50, ['fallback: last stored price ₹42'], PANEL, LV, 14, bold_first=True))
    o.append(T(20, 290, 'No network at all,', 13, 'start', MUT)); o.append(T(20, 308, 'yet the page opens', 13, 'start', MUT))
    o.append(T(20, 326, 'and shows a price.', 13, 'start', MUT))
    return 416, ''.join(o)
FIG[7] = (f7, 'On the first visit the worker caches the 4 + 120 + 8 = 132 KB shell in 3 files. Offline, /index.html is a cache hit and the app opens, while /api/price misses, the network fails, and the fallback shows the last stored ₹42.',
          'A bar of three cached files totalling 132 KB; below, offline requests from the page go through the service worker: index.html is a cache hit, the price request misses and fails and shows the fallback price ₹42.')


# ---- 5.8 three dispatches through the reducer ----
def f8():
    o = [T(20, 26, 'Each dispatch makes a new state object', 15, 'start', bold=True)]
    states = [('state 0', 'items []', 'count 0', 'total 0'),
              ('state 1', 'items [dosa]', 'count 1', 'total 60'),
              ('state 2', 'items [dosa, coffee]', 'count 2', 'total 100'),
              ('state 3', 'items [coffee]', 'count 1', 'total 40')]
    acts = [("ADD_ITEM dosa, price 60", '+1, +60'), ("ADD_ITEM coffee, price 40", '+1, +40'), ("REMOVE_ITEM id 1, price 60", '−1, −60')]
    for i, (n, it, c, t) in enumerate(states):
        y = 46 + i * 92
        last = i == 3
        o.append(R(20, y, 420, 54, NXS if last else PANEL, NX if last else AC, 8))
        o.append(T(36, y + 33, n, 14, 'start', MUT, True))
        o.append(TM(110, y + 33, it, 14, 'start', bold=True))
        o.append(T(330, y + 22, c, 13, 'start')); o.append(T(330, y + 42, t, 13, 'start', bold=True))
        if i < 3:
            a, d = acts[i]
            o.append(ar(230, y + 56, 230, y + 90, AC))
            o.append(R(470, y + 52, 230, 40, ACS, AC, 6, 1.5))
            o.append(T(585, y + 70, a, 13, bold=True)); o.append(T(585, y + 86, 'reducer: ' + d, 13, fill=MUT))
            o.append(L(468, y + 72, 236, y + 72, AC, 1.2, '4 3'))
    o.append(T(20, 414, 'Final: one item, Filter coffee; count 1; total 40 rupees. No state object is ever edited.', 14, 'start', bold=True))
    return 430, ''.join(o)
FIG[8] = (f8, 'Starting from an empty cart, each dispatched action goes through the reducer, which returns a new object: dosa makes count 1 and total 60, coffee makes 2 and 100, and removing the dosa leaves 1 and 40.',
          'Four state cards stacked top to bottom, joined by three actions: add dosa 60, add coffee 40, remove id 1; the totals go 0, 60, 100, 40 and the count 0, 1, 2, 1.')


# ---- 5.9 typing "dosa" on a time line ----
def f9():
    o = [T(20, 26, 'Keystrokes for "dosa" and the GET requests they cause', 15, 'start', bold=True)]
    X0, X1 = 170, 690
    fx = lambda ms: X0 + ms / 800 * (X1 - X0)
    keys = [(0, 'd'), (120, 'do'), (250, 'dos'), (400, 'dosa')]
    o.append(xaxis(X0, X1, 330, [0, 100, 200, 300, 400, 500, 600, 700, 800], fx, 'milliseconds'))
    def lane(y, label):
        return T(X0 - 12, y + 5, label, 13, 'end', bold=True) + L(X0, y, X1, y, LN, 1.2)
    y = 64
    o.append(lane(y, 'keystrokes'))
    for ms, s in keys:
        o.append(C(fx(ms), y, 7, AC)); o.append(TM(fx(ms), y - 14, s, 13, fill=AC, bold=True))
    y = 124
    o.append(lane(y, 'no operators'))
    for ms, s in keys:
        o.append(R(fx(ms) - 4, y - 12, 54, 24, PANEL, AC, 4, 1.5)); o.append(T(fx(ms) + 23, y + 5, 'GET', 13, bold=True))
    o.append(T(X1, y + 32, '4 GETs', 13, 'end', AC, True))
    y = 196
    o.append(lane(y, 'debounceTime(300)'))
    for a, b in ((0, 120), (120, 250), (250, 400)):
        o.append(L(fx(a), y, fx(b), y, LV, 2.5, '5 3'))
    o.append(L(fx(400), y, fx(700), y, NX, 3))
    o.append(R(fx(700) - 2, y - 12, 54, 24, NXS, NX, 4, 1.5)); o.append(T(fx(700) + 25, y + 5, 'GET', 13, bold=True))
    o.append(T(fx(250), y - 12, 'each gap &lt; 300 ms restarts the timer', 13, fill=LV))
    o.append(T(X1, y + 32, '1 GET at 400 + 300 = 700 ms', 13, 'end', NX, True))
    y = 268
    o.append(lane(y, 'switchMap alone'))
    for k, (ms, s) in enumerate(keys):
        last = k == 3
        o.append(R(fx(ms) - 4, y - 12, 54, 24, NXS if last else 'var(--fig)', NX if last else LV, 4, 1.5))
        o.append(T(fx(ms) + 23, y + 5, 'GET', 13, fill=INK if last else LV, bold=True))
        if not last: o.append(L(fx(ms), y + 10, fx(ms) + 46, y - 10, LV, 1.8))
    o.append(T(X1, y + 32, '4 GETs, 3 cancelled', 13, 'end', LV, True))
    o.append(T(20, 400, 'If the last GET returns 500, catchError(() =&gt; of([])) hands the list [ ]: 0 items, no error shown.', 13, 'start', MUT))
    return 416, ''.join(o)
FIG[9] = (f9, 'Four keystrokes arrive 120, 130 and 150 ms apart. With no operators each sends a GET; debounceTime(300) restarts on every keystroke and sends one GET at 700 ms; switchMap alone sends four and cancels the first three.',
          'A time line from 0 to 800 ms with keystrokes d, do, dos, dosa at 0, 120, 250 and 400 ms; lanes show 4 GETs with no operators, 1 GET at 700 ms with debounce, and 4 GETs with 3 crossed out under switchMap.')


spec = make_spec(FIG)


def text_fixes(k):
    return {}.get(k, [])
