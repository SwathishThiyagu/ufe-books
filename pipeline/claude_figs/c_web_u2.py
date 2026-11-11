"""Claude's hand-drawn figures for c-web-u2 (Web Technologies, unit 2: HTML5 and CSS3), one per chapter,
each drawn from that chapter's worked example with its own numbers, plus the sentences that describe a figure."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
ARC = {AC: 'n', L2: 'm', LV: 'l', NX: 'x'}


def ar(x1, y1, x2, y2, c=AC, w=2, dash=None):
    return L(x1, y1, x2, y2, c, w, dash, ARC[c])


def node(x, y, name, void=False, w=None):
    w = w or max(64, tw(name, 15) + 26)
    return (R(x - w / 2, y - 17, w, 34, NXS if void else PANEL, NX if void else AC, 8, 2, '5 3' if void else None)
            + TM(x, y + 5, name, 15, bold=True))


# ---- 2.1 the element tree of the notice page ----
def f1():
    o = [T(20, 26, 'The element tree of the "Notices" page', 15, 'start', bold=True)]
    P0 = {'html': (360, 70), 'head': (190, 160), 'body': (530, 160), 'title': (80, 250), 'meta': (190, 250), 'link': (300, 250),
          'h1': (460, 250), 'p': (600, 250), 'em': (600, 336)}
    for a, b in (('html', 'head'), ('html', 'body'), ('head', 'title'), ('head', 'meta'), ('head', 'link'), ('body', 'h1'), ('body', 'p'), ('p', 'em')):
        (x1, y1), (x2, y2) = P0[a], P0[b]
        o.append(L(x1, y1 + 17, x2, y2 - 17, L2, 1.8))
    for k, (x, y) in P0.items():
        o.append(node(x, y, k, k in ('meta', 'link')))
    o.append(T(80, 286, '"Notices"', 13, fill=MUT)); o.append(T(460, 286, '"Notices"', 13, fill=MUT))
    o.append(T(600, 372, '"today"', 13, fill=MUT))
    o.append(T(190, 300, 'void: no end tag', 13, fill=NX, bold=True))
    o.append(T(20, 410, 'Count: 9 elements = 7 non-void + 2 void (meta, link). The doctype is not an element.', 14, 'start', bold=True))
    return 426, ''.join(o)
FIG[1] = (f1, 'The browser builds this tree: html at the root, head and body as its children, title, meta and link under head, h1 and p under body, and em inside p. That is 9 elements, of which meta and link are void.',
          'Element tree: html has children head and body; head has title, meta and link; body has h1 and p; p has em. meta and link are marked void. Total 9 elements, 2 void.')


# ---- 2.2 the bill table and its colspan ----
def f2():
    o = [T(20, 26, 'Stationery bill: 4 rows × 3 columns', 15, 'start', bold=True)]
    x0, cw, y0, rh = 140, [160, 130, 130], 60, 46
    xs = [x0, x0 + cw[0], x0 + cw[0] + cw[1], x0 + sum(cw)]
    rows = [('thead', ['Item', 'Qty', 'Rs'], ACS), ('tbody', ['Pen', '2', '20'], PANEL), ('tbody', ['Ink', '1', '50'], PANEL)]
    for i, (sec, cells, f) in enumerate(rows):
        y = y0 + i * rh
        for j, c in enumerate(cells):
            o.append(R(xs[j], y, cw[j], rh, f, AC, 0, 1.5))
            o.append(T(xs[j] + cw[j] / 2, y + 29, c, 15, bold=(i == 0)))
        o.append(TM(x0 - 14, y + 29, sec, 13, 'end', MUT))
    y = y0 + 3 * rh
    o.append(R(xs[0], y, cw[0] + cw[1], rh, NXS, NX, 0, 2))
    o.append(T(xs[0] + (cw[0] + cw[1]) / 2, y + 29, 'Sum', 15, bold=True))
    o.append(R(xs[2], y, cw[2], rh, NXS, NX, 0, 2))
    o.append(T(xs[2] + cw[2] / 2, y + 29, '70', 15, bold=True))
    o.append(TM(x0 - 14, y + 29, 'tfoot', 13, 'end', MUT))
    o.append(brace(xs[0], xs[2], y + rh + 12, NX))
    o.append(T((xs[0] + xs[2]) / 2, y + rh + 36, 'colspan=2: one cell covers columns 1 and 2', 13, fill=NX, bold=True))
    for j in range(3):
        o.append(T(xs[j] + cw[j] / 2, y0 - 10, f'column {j + 1}', 13, fill=MUT))
    o.append(T(xs[3] + 18, y0 + rh + 29, '20', 14, 'start', AC, True))
    o.append(T(xs[3] + 18, y0 + 2 * rh + 29, '+ 50', 14, 'start', AC, True))
    o.append(L(xs[3] + 14, y0 + 2 * rh + 38, xs[3] + 70, y0 + 2 * rh + 38, AC, 1.5))
    o.append(T(xs[3] + 18, y0 + 3 * rh + 29, '= 70', 14, 'start', AC, True))
    return y + rh + 56, ''.join(o)
FIG[2] = (f2, 'Every row covers 3 columns: the footer has only 2 cells, but Sum spans columns 1 and 2. The Rs column is already the line amount, so the total is 20 + 50 = 70.',
          'A 4-row, 3-column table: header Item, Qty, Rs; rows Pen 2 20 and Ink 1 50; footer cell Sum spans two columns, then 70.')


# ---- 2.3 a GET form becomes a URL ----
def f3():
    o = [T(20, 26, 'form action="/search" method="get": the user clicks Search', 15, 'start', bold=True)]
    ctr = [('input name="q"', 'typed: html', 'q=html', AC), ('select name="lang"', 'chosen: English (value en)', 'lang=en', AC),
           ('button (no name)', 'Search', 'adds nothing', L2)]
    for i, (a, b, pair, c) in enumerate(ctr):
        y = 50 + i * 74
        o.append(R(20, y, 290, 56, PANEL, c, 8))
        o.append(TM(36, y + 23, a, 14, 'start', bold=True))
        o.append(T(36, y + 44, b, 13, 'start', MUT))
        o.append(ar(314, y + 28, 400, y + 28, c, 2, None if c == AC else '5 4'))
        o.append(TM(410, y + 33, pair, 15, 'start', AC if c == AC else MUT, bold=(c == AC)))
    y = 290
    o.append(T(20, y, 'Join the pairs with &amp;, put ? after the path:', 14, 'start'))
    o.append(R(20, y + 14, 680, 50, NXS, NX, 8))
    o.append(TM(360, y + 46, 'GET /search?q=html&amp;lang=en HTTP/1.1', 17, fill=INK, bold=True))
    o.append(T(20, y + 92, 'The pairs travel in the URL query string, inside the request line.', 14, 'start', MUT))
    return y + 108, ''.join(o)
FIG[3] = (f3, 'The browser walks the named controls in order: q gives q=html, lang gives lang=en, and the button with no name gives nothing. For a GET form the pairs go after ? in the URL: GET /search?q=html&amp;lang=en.',
          'Three form controls on the left map to pairs: input q to q=html, select lang to lang=en, the unnamed button to nothing; the joined request line is GET /search?q=html&lang=en HTTP/1.1.')


# ---- 2.4 the news page in source order ----
def f4():
    o = [T(20, 26, 'The news page: five blocks in source order', 15, 'start', bold=True)]
    def blk(x, y, w, h, n, tag, sub, land=True):
        r = [R(x, y, w, h, PANEL if land else 'var(--fig)', AC if land else L2, 8, 2, None if land else '5 4')]
        r.append(C(x + 18, y + 18, 11, AC)); r.append(T(x + 18, y + 23, str(n), 13, fill='var(--fig)', bold=True))
        r.append(TM(x + 38, y + 24, tag, 15, 'start', bold=True))
        r.append(T(x + 38 + tw(tag, 15) + 10, y + 24, sub, 13, 'start', MUT))
        return ''.join(r)
    o.append(blk(20, 44, 680, 46, 1, 'header', 'h1 with the site name'))
    o.append(blk(20, 100, 680, 46, 2, 'nav', 'ul of 4 links'))
    o.append(blk(20, 156, 470, 214, 3, 'main', ''))
    o.append(R(40, 196, 430, 160, 'var(--fig)', L2, 8, 1.5, '5 4'))
    o.append(TM(56, 220, 'article', 14, 'start', bold=True)); o.append(T(124, 220, 'not a landmark', 13, 'start', MUT))
    for i, s in enumerate(['h2 headline', 'p', 'p']):
        o.append(R(56, 232 + i * 26, 190, 20, ACS, AC, 3, 1.2)); o.append(T(64, 247 + i * 26, s, 13, 'start'))
    o.append(R(270, 232, 184, 104, NXS, NX, 6))
    o.append(TM(362, 256, 'video', 14, bold=True))
    for i, s in enumerate(['90 s, controls, poster', 'MP4 + WebM sources', '1 captions track']):
        o.append(T(362, 278 + i * 18, s, 13))
    o.append(blk(500, 156, 200, 214, 4, 'aside', ''))
    o.append(T(530, 204, '3 related links', 13, 'start', MUT))
    o.append(blk(20, 380, 680, 46, 5, 'footer', 'copyright line'))
    o.append(T(20, 456, 'Landmarks: header, nav, main, aside, footer. Links: 4 + 3 = 7.', 14, 'start', bold=True))
    return 472, ''.join(o)
FIG[4] = (f4, 'The five blocks in source order, header, nav, main, aside, footer, each a landmark; the article inside main is not one. The story carries a 90-second video with a poster, two sources and one caption track.',
          'A page wireframe numbered in source order: 1 header, 2 nav with 4 links, 3 main holding an article with a heading, two paragraphs and a video, 4 aside with 3 links, 5 footer.')


# ---- 2.5 specificity counters ----
def f5():
    o = [T(20, 26, 'Which colour does the paragraph get?', 15, 'start', bold=True)]
    xc = [330, 410, 490, 570]
    heads = ['inline', 'ids', 'classes', 'elements']
    for x, h in zip(xc, heads):
        o.append(T(x, 60, h, 13, fill=MUT, bold=True))
    rows = [('#intro p', 'blue', (0, 1, 0, 1)), ('p.note', 'red', (0, 0, 1, 1)), ('style="color: green"', 'green', (1, 0, 0, 0))]
    y = 76
    for sel, col, cnt in rows:
        o.append(R(20, y, 680, 40, PANEL, L2, 6, 1.5))
        o.append(TM(36, y + 26, sel, 14, 'start', bold=True))
        o.append(T(250, y + 26, col, 14, 'start', MUT))
        for x, v in zip(xc, cnt):
            o.append(T(x, y + 26, str(v), 16, bold=True))
        y += 48
    o.append(R(xc[1] - 32, 72, 64, 96, 'none', AC, 6, 2.5))
    o.append(R(xc[0] - 32, 72, 64, 144, 'none', NX, 6, 2.5, '6 4'))
    # three stages
    y = 248
    stages = [('Step 1: the two rules', '(0,1,0,1) beats (0,0,1,1) in the ids column', 'blue', AC),
              ('Step 2: add the style attribute', '(1,0,0,0) wins in the first column', 'green', NX),
              ('Step 3: red rule gets !important', 'importance is checked before counters', 'red', LV)]
    for i, (a, b, col, c) in enumerate(stages):
        x = 20 + i * 232
        o.append(R(x, y, 216, 110, PANEL, c, 8))
        o.append(T(x + 108, y + 24, a, 13, bold=True))
        words = b.split(' ')
        l1, l2 = ' '.join(words[:len(words) // 2]), ' '.join(words[len(words) // 2:])
        o.append(T(x + 108, y + 48, l1, 13, fill=MUT)); o.append(T(x + 108, y + 66, l2, 13, fill=MUT))
        o.append(T(x + 108, y + 96, f'paints {col}', 16, fill=c, bold=True))
        if i < 2: o.append(ar(x + 218, y + 55, x + 230, y + 55, c))
    return y + 126, ''.join(o)
FIG[5] = (f5, 'Read the counters left to right: the id rule beats the class rule in the ids column, so the text is blue; the style attribute wins in the first column, so it turns green; !important is checked before any counter, so the red rule finally wins.',
          'A table of specificity counters: #intro p is 0,1,0,1, p.note is 0,0,1,1, the style attribute is 1,0,0,0; below, three steps paint blue, then green, then red after !important.')


# ---- 2.6 the box model to scale ----
def f6():
    s, x0 = 1.75, 40
    o = [T(20, 26, 'width 300 + padding 20 + border 5 + margin 10 (content-box)', 15, 'start', bold=True)]
    def box(y, h, layers, labels):
        r = []
        x = x0
        m, b, p, c = layers  # widths to scale; heights use fixed bands bv, pv
        bv, pv = 6, 20
        r.append(R(x, y, (2 * m + 2 * b + 2 * p + c) * s, h, 'var(--fig)', L2, 0, 1.2, '4 4'))
        r.append(R(x + m * s, y + 10, (2 * b + 2 * p + c) * s, h - 20, INK, INK, 0, 0))
        r.append(R(x + (m + b) * s, y + 10 + bv, (2 * p + c) * s, h - 20 - 2 * bv, ACS, AC, 0, 0))
        r.append(R(x + (m + b + p) * s, y + 10 + bv + pv, c * s, h - 20 - 2 * (bv + pv), PANEL, AC, 0, 1.5))
        r.append(T(x + (m + b + p + c / 2) * s, y + h / 2 + 5, labels, 15, bold=True))
        return ''.join(r)
    y = 56
    o.append(box(y, 130, (10, 5, 20, 300), 'content 300'))
    o.append(T(x0 + (10 + 5 + 10) * s, y + 68, '20', 13, bold=True))
    o.append(T(x0 + (10 + 5 + 20 + 300 + 10) * s, y + 68, '20', 13, bold=True))
    def dim(xa, xb, yy, text, c):
        return (L(xa, yy, xb, yy, c, 1.5) + L(xa, yy - 6, xa, yy + 6, c, 1.5) + L(xb, yy - 6, xb, yy + 6, c, 1.5)
                + Tb((xa + xb) / 2, yy + 5, text, 13, fill=c, bold=True))
    o.append(dim(x0 + 10 * s, x0 + 360 * s, y + 150, 'rendered width 300 + 40 + 10 = 350', AC))
    o.append(dim(x0, x0 + 370 * s, y + 178, 'space blocked out 350 + 10 + 10 = 370', MUT))
    o += [R(40, y + 200, 16, 14, INK, INK, 2, 0), T(62, y + 212, 'border 5', 13, 'start'),
          R(150, y + 200, 16, 14, ACS, AC, 2, 1), T(172, y + 212, 'padding 20', 13, 'start'),
          R(270, y + 200, 16, 14, 'var(--fig)', L2, 2, 1.2, '3 3'), T(292, y + 212, 'margin 10 (transparent)', 13, 'start')]
    y2 = y + 250
    o.append(T(20, y2, 'Same card with box-sizing: border-box (width 300 now includes padding and border)', 15, 'start', bold=True))
    o.append(box(y2 + 14, 110, (10, 5, 20, 250), 'content 300 − 40 − 10 = 250'))
    o.append(dim(x0 + 10 * s, x0 + 310 * s, y2 + 144, 'rendered width 300', AC))
    return y2 + 160, ''.join(o)
FIG[6] = (f6, 'With the default content-box, 300px of content plus 40px of padding and 10px of border draws a card 350px wide, and the margins make it block out 370px. With border-box the 300px includes padding and border, so the content shrinks to 250px.',
          'Two nested-rectangle box models drawn to scale: content 300, padding 20, border 5, margin 10 giving 350 rendered and 370 blocked; below, border-box with width 300 and content 250.')


# ---- 2.7 one colour in three notations ----
def f7():
    o = [T(20, 26, '#FF6347 split into three channels', 15, 'start', bold=True)]
    X0, X1 = 200, 660
    fx = lambda v: X0 + v / 255 * (X1 - X0)
    rows = [('FF', '16×15 + 15', 255, 'R'), ('63', '16×6 + 3', 99, 'G'), ('47', '16×4 + 7', 71, 'B')]
    for i, (hx, how, v, ch) in enumerate(rows):
        y = 52 + i * 46
        o.append(TM(30, y + 22, hx, 16, 'start', bold=True))
        o.append(T(62, y + 22, how, 13, 'start', MUT))
        o.append(R(X0, y + 4, fx(v) - X0, 26, ACS if v != 255 else NXS, AC if v != 255 else NX, 4, 1.5))
        o.append(T(fx(v) + 8, y + 22, f'{ch} = {v}', 14, 'start', bold=True))
    o.append(xaxis(X0, X1, 196, [0, 71, 99, 255], fx))
    o.append(L(fx(71), 50, fx(71), 196, LV, 1.5, '5 4')); o.append(L(fx(255), 50, fx(255), 196, LV, 1.5, '5 4'))
    o.append(brace(fx(71), fx(255), 236, LV))
    o.append(T((fx(71) + fx(255)) / 2, 260, 'range = max − min = 255 − 71 = 184', 13, fill=LV, bold=True))
    lines = [('rgb', 'rgb(255, 99, 71)', 'the three channels in decimal'),
             ('L', '(255 + 71) ÷ 510 = 64%', 'average of max and min'),
             ('S', '184 ÷ (510 − 255 − 71) = 100%', 'L is above 50%'),
             ('H', '60 × (99 − 71) ÷ 184 ≈ 9°', 'red is the largest channel'),
             ('hsl', 'hsl(9, 100%, 64%)', 'H, S and L together'),
             ('60% opacity', 'rgba(255, 99, 71, 0.6)', 'alpha is 0.6, not 60')]
    y = 296
    for a, b, c in lines:
        if a == 'hsl':
            o.append(R(140, y - 19, 300, 28, NXS, NX, 6))
        o.append(T(30, y, a, 14, 'start', AC, True))
        o.append(TM(150, y, b, 14, 'start', bold=True))
        o.append(T(470, y, c, 13, 'start', MUT))
        y += 28
    return y, ''.join(o)
FIG[7] = (f7, 'The hex pairs FF, 63 and 47 are 255, 99 and 71, so the colour is rgb(255, 99, 71). Max 255 and min 71 give L = 64% and S = 100%, the green and blue channels give H ≈ 9°, and 60% opacity is the alpha value 0.6.',
          'Three bars for the red, green and blue channels at 255, 99 and 71 on a 0 to 255 scale, with the range 184 marked; below, the steps to rgb(255, 99, 71), hsl(9, 100%, 64%) and rgba(255, 99, 71, 0.6).')


# ---- 2.8 flex 1 : 2 : 1 in a 600 px container ----
def f8():
    s, x0 = 1.1, 30
    o = [T(20, 26, 'Container 600 px, items flex 1, 2, 1 (shares 1/4, 2/4, 1/4)', 15, 'start', bold=True)]
    def row(y, parts, title):
        r = [T(x0, y - 10, title, 14, 'start', bold=True)]
        x = x0
        for lab, w, gap in parts:
            if gap:
                r.append(R(x, y, w * s, 50, 'var(--fig)', LV, 0, 1.5, '4 3'))
                r.append(T(x + w * s / 2, y + 30, str(w), 13, fill=LV, bold=True))
            else:
                r.append(R(x, y, w * s, 50, NXS if lab == 'B' else ACS, NX if lab == 'B' else AC, 4, 2))
                r.append(T(x + w * s / 2, y + 31, f'{lab}  {w} px', 15, bold=True))
            x += w * s
        return ''.join(r)
    o.append(row(70, [('A', 150, 0), ('B', 300, 0), ('C', 150, 0)], 'gap 0: free space 600'))
    o.append(T(x0, 146, '600 × 1/4 = 150,  600 × 2/4 = 300,  600 × 1/4 = 150', 13, 'start', MUT))
    o.append(row(200, [('A', 135, 0), ('', 30, 1), ('B', 270, 0), ('', 30, 1), ('C', 135, 0)], 'gap 30 px: free space 600 − 2 × 30 = 540'))
    o.append(T(x0, 276, '540 × 1/4 = 135,  540 × 2/4 = 270,  540 × 1/4 = 135', 13, 'start', MUT))
    o.append(T(x0, 304, 'Check: 135 + 270 + 135 + 60 = 600. B stays twice A in both rows.', 14, 'start', bold=True))
    o.append(brace(x0, x0 + 600 * s, 320, MUT))
    o.append(T(x0 + 300 * s, 342, '600 px', 13, fill=MUT))
    return 356, ''.join(o)
FIG[8] = (f8, 'The same 600 px container drawn to scale twice. With no gap the items get 150, 300 and 150 px; a 30 px gap takes 2 × 30 = 60 px first, so the 540 px left splits into 135, 270 and 135 px.',
          'Two rows 600 px wide: A 150, B 300, C 150 with no gap; then A 135, gap 30, B 270, gap 30, C 135.')


# ---- 2.9 the Bootstrap 12-column grid ----
def f9():
    s, x0 = 0.7, 40
    u = 80 * s
    o = [T(20, 26, 'Content width 960 px ÷ 12 = 80 px per column unit', 15, 'start', bold=True)]
    for i in range(13):
        o.append(L(x0 + i * u, 44, x0 + i * u, 300, LN, 1, '3 4'))
    for i in range(12):
        o.append(T(x0 + i * u + u / 2, 58, str(i + 1), 13, fill=MUT))
    def row(y, label, spans, wrap=False):
        r = []
        x = x0
        for cls, sp in spans:
            w = sp * u
            r.append(R(x + 2, y, w - 4, 38, ACS, AC, 5, 2))
            r.append(TM(x + w / 2, y + 17, cls, 13, bold=True))
            r.append(T(x + w / 2, y + 33, f'{sp * 80} px', 13))
            x += w
        return ''.join(r)
    o.append(row(70, 'A', [('col-md-4', 4)] * 3))
    o.append(row(120, 'B', [('col-md-8', 8), ('col-md-4', 4)]))
    o.append(row(170, 'C', [('col-12', 12)]))
    for y, lab in ((70, 'A'), (120, 'B'), (170, 'C')):
        o.append(T(x0 - 10, y + 25, lab, 14, 'end', bold=True))
    # wrapping row
    y = 236
    o.append(T(x0, y - 8, 'Row A as three col-md-6: 6 + 6 + 6 = 18 > 12', 14, 'start', LV, True))
    for i in range(2):
        o.append(R(x0 + i * 6 * u + 2, y + 4, 6 * u - 4, 30, ACS, AC, 5, 2))
        o.append(TM(x0 + i * 6 * u + 3 * u, y + 24, 'col-md-6', 13, bold=True))
    o.append(R(x0 + 2, y + 44, 6 * u - 4, 30, LVS, LV, 5, 2))
    o.append(TM(x0 + 3 * u, y + 64, 'col-md-6', 13, bold=True))
    o.append(T(x0 + 6 * u + 14, y + 64, '← the third column wraps to a new line', 13, 'start', LV, True))
    return y + 90, ''.join(o)
FIG[9] = (f9, 'Each column unit is 960 ÷ 12 = 80 px, so span 4 is 320 px, span 8 is 640 px and span 12 is 960 px. Three col-md-6 columns need 18 units, so the third wraps onto a new line.',
          'A 12-column grid with rows of col-md-4 ×3 (320 px each), col-md-8 and col-md-4 (640 and 320 px), col-12 (960 px); below, three col-md-6 where the third wraps to a second line.')


spec = make_spec(FIG)


def text_fixes(k):
    return {}.get(k, [])
