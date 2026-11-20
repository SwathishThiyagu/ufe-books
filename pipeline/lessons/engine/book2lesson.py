#!/usr/bin/env python3
"""book2lesson.py: turn a University free n easy unit book into ready-to-fill lesson files.

The slow, expensive part of a lesson used to be reading the whole skill, the grammar and a reference lesson, then
hand-writing ~300 lines of scenes and redrawing every book figure. Most of a lesson is fixed in shape, and the book
already holds the content in a fixed structure, so this script does that part with no model at all:

  - splits the unit into lessons of 2-3 chapters (or --split 2.1-2.2,2.3-2.5,2.6-2.7)
  - for each lesson writes <sid>-u<N>-L<k>.js: META, the full scene list with every on-screen field it can take from the
    book already filled (part slides, the book's own figures as `bookfig` scenes built up piece by piece, worked-example
    steps, exam traps, the three exam questions with their model answers, the notes page, next-lesson card), and
    `say:'TODO'` / `TODO` markers where a writer is needed (narration, short labels, hook)
  - writes WRITE.md beside them: the short rules a filler needs (instead of the whole skill), and which scenes are
    flagged IMPROVISE (where more effort is worth spending)
  - writes videos.<sid>-u<N>.json: the unit's lessons for site/make_site.py (PDF notes, descriptions)

usage: book2lesson.py book.html outdir [--split a-b,c-d] --subject <subject id> [--next-unit "next unit's topic title"]
"""
import html, json, os, re, sys, hashlib
import xml.etree.ElementTree as ET

LV = {'remember': 'R', 'understand': 'U', 'apply': 'A', 'analyze': 'N', 'analyse': 'N', 'evaluate': 'N', 'create': 'B', 'beyond': 'B'}


UNIS = re.compile(r"\b(Anna Univ(?:ersity)?|SRM(?: IST)?|IIT ?(?:Madras|Delhi|Bombay)|IIT[MDB]|NIT (?:Trichy|Surathkal|Calicut)|NIT[TKC]|Manipal(?: \(MIT\))?|MIT Manipal|Christ(?: University)?)(?:'s)?\b")


NUMW = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

def nouni(s):
    s = re.sub(r'[;,]?\s*\b(?:%s)\b[^.;)]*' % UNIS.pattern[3:-3], '', s) if False else s
    return UNIS.sub('some syllabi', s)


def txt(s):
    s = re.sub(r'<br\s*/?>', ' ', s)
    s = re.sub(r'<[^>]+>', '', s)
    return nouni(re.sub(r'\s+', ' ', html.unescape(s)).strip())


def js(v):
    return json.dumps(v, ensure_ascii=False)


def sentences(t):
    return [x.strip() for x in re.split(r'(?<=[.!?])\s+(?=[A-Z(])', t) if x.strip()]


# ---------------- figures: split the book's SVG into top-level pieces with an x position ----------------
NUM = re.compile(r'-?\d+(?:\.\d+)?')


def piece_x(el):
    a = el.attrib
    for k in ('cx', 'x', 'x1'):
        if k in a:
            try:
                return float(NUM.findall(a[k])[0])
            except Exception:
                pass
    if 'points' in a:
        n = [float(v) for v in NUM.findall(a['points'])]
        if n:
            return min(n[0::2])
    if 'd' in a:
        n = [float(v) for v in NUM.findall(a['d'])]
        if n:
            return n[0]
    tr = a.get('transform', '')
    m = re.search(r'translate\(\s*(-?[\d.]+)', tr)
    xs = []
    for ch in el.iter():
        if ch is el:
            continue
        for k in ('cx', 'x', 'x1'):
            if k in ch.attrib:
                try:
                    xs.append(float(NUM.findall(ch.attrib[k])[0]))
                except Exception:
                    pass
    base = float(m.group(1)) if m else 0.0
    return base + (min(xs) if xs else 0.0)


def extent(el):
    """rough x/y extent of a top-level SVG element (absolute coordinates are enough for the book's figures)"""
    xs, ys = [], []
    for e in el.iter():
        a = e.attrib
        for k in ('x', 'cx', 'x1', 'x2'):
            if k in a:
                v = NUM.findall(a[k])
                if v: xs.append(float(v[0]))
        for k in ('y', 'cy', 'y1', 'y2'):
            if k in a:
                v = NUM.findall(a[k])
                if v: ys.append(float(v[0]))
        if 'width' in a and 'x' in a:
            try: xs.append(float(NUM.findall(a['x'])[0]) + float(NUM.findall(a['width'])[0]))
            except Exception: pass
        if 'r' in a and 'cx' in a:
            try:
                r = float(NUM.findall(a['r'])[0]); cx = float(NUM.findall(a['cx'])[0]); xs += [cx - r, cx + r]
            except Exception: pass
        for k in ('d', 'points'):
            if k in a and not re.search(r'[a-z]', re.sub(r'[eE][-+]?\d', '', a[k]).replace('M', '').replace('L', '').replace('H', '').replace('V', '').replace('C', '').replace('Q', '').replace('A', '').replace('Z', '')):
                n = [float(v) for v in NUM.findall(a[k])]
                xs += n[0::2]; ys += n[1::2]
    m = re.search(r'translate\(\s*(-?[\d.]+)[ ,]+(-?[\d.]+)', el.attrib.get('transform', ''))
    dx, dy = (float(m.group(1)), float(m.group(2))) if m else (0.0, 0.0)
    if not xs: xs = [0.0]
    if not ys: ys = [0.0]
    return min(xs) + dx, max(xs) + dx, min(ys) + dy, max(ys) + dy


def group_steps(items, vb, n_steps=4):
    """build order that follows the figure's parts (10 Nov 2026: rows OR columns): wide background pieces first, then the
    shapes in up to three groups split at the clearest gaps, top-to-bottom when the figure is laid out in rows and
    left-to-right when it is laid out in columns; each text joins the shape nearest to it"""
    W, H = vb[2], vb[3]
    info = []
    for it in items:
        x0, x1, y0, y1 = it['ext']
        info.append({'cx': (x0 + x1) / 2, 'cy': (y0 + y1) / 2, 'w': x1 - x0, 'x0': x0, 'x1': x1, 'y0': y0, 'y1': y1, 'text': it['tag'] == 'text'})
    step = [0] * len(items)
    shapes = [i for i, f in enumerate(info) if not f['text']]
    bg = [i for i in shapes if info[i]['w'] > 0.55 * W and (info[i]['y1'] - info[i]['y0']) > 0.55 * H]
    rest = [i for i in shapes if i not in bg]
    k = max(1, min(n_steps - (1 if bg else 0), len(rest)))
    def cuts(axis):
        lo, hi = ('x0', 'x1') if axis == 'x' else ('y0', 'y1')
        span = W if axis == 'x' else H
        iv = sorted((info[i][lo], info[i][hi]) for i in rest)
        gaps, end = [], None
        for a, b in iv:
            if end is not None and a > end:
                gaps.append((a - end, (a + end) / 2))
            end = b if end is None else max(end, b)
        gaps.sort(reverse=True)
        g = gaps[:k - 1]
        return sum(x[0] for x in g) / max(span, 1), sorted(x[1] for x in g)
    sx, cx_ = cuts('x'); sy, cy_ = cuts('y')
    axis, cs = ('y', cy_) if sy > sx else ('x', cx_)
    key = 'cy' if axis == 'y' else 'cx'
    base = 1 if bg else 0
    for i in bg: step[i] = 1
    for i in rest:
        step[i] = base + 1 + sum(1 for c in cs if info[i][key] > c)
    for i, f in enumerate(info):
        if f['text']:
            cand = [q for q in shapes if q not in bg] or shapes
            if cand:
                q = min(cand, key=lambda q: (info[q]['cx'] - f['cx']) ** 2 + (0.5 * (info[q]['cy'] - f['cy'])) ** 2)
                step[i] = step[q]
            else:
                step[i] = 1
    return [max(1, s) for s in step]


def split_svg(svg):
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', svg).group(1).split()]
    s = re.sub(r'\sxmlns(:\w+)?="[^"]*"', '', svg)
    s = s.replace('&nbsp;', '&#160;')
    s = re.sub(r'&(?!#?\w+;)', '&amp;', s)
    try:
        root = ET.fromstring(s)
    except ET.ParseError as e:
        return {'vb': vb, 'defs': '', 'items': [[0, svg, 1]], 'error': str(e), 'minfs': 14}
    defs, items = '', []
    kids = list(root)
    real = [c for c in kids if c.tag.split('}')[-1] not in ('defs', 'style', 'title', 'desc')]
    if len(real) == 1 and real[0].tag.split('}')[-1] == 'g' and len(list(real[0])) > 1 and not real[0].attrib:
        kids = [c for c in kids if c is not real[0]] + list(real[0])   # one wrapping group: use its parts
    for ch in kids:
        tag = ch.tag.split('}')[-1]
        ch.tail = None
        markup = ET.tostring(ch, encoding='unicode', short_empty_elements=True)
        markup = re.sub(r'\sxmlns(:\w+)?="[^"]*"', '', markup).replace('ns0:', '')
        if tag in ('defs', 'style', 'title', 'desc'):
            if tag in ('defs', 'style'):
                defs += markup
            continue
        items.append({'x': round(piece_x(ch), 1), 'svg': markup, 'tag': tag, 'ext': extent(ch)})
    steps = group_steps(items, vb) if items else []
    texts = [float(m) for m in re.findall(r'font-size="([\d.]+)"', svg)]
    return {'vb': vb, 'defs': defs, 'items': [[it['x'], it['svg'], st] for it, st in zip(items, steps)], 'ext': [it['ext'] for it in items], 'tags': [it['tag'] for it in items], 'minfs': min(texts) if texts else 14}



def halves(F):
    """split a tall figure in two at the empty horizontal band closest to the middle; each half keeps only the pieces
    whose middle lies in it, re-grouped into steps (10 Nov 2026)"""
    vb, ext = F['vb'], F.get('ext') or []
    y0, H = vb[1], vb[3]
    best = None
    for k in range(30, 71):
        y = y0 + H * k / 100
        crossing = sum(1 for e in ext if e[2] < y - 2 and e[3] > y + 2 and (e[1] - e[0]) < 0.9 * vb[2])
        score = (crossing, abs(k - 50))
        if best is None or score < best[0]: best = (score, y)
    cut = best[1] if best else y0 + H / 2
    out = []
    for half, lo, hi in (('top', y0, cut), ('bottom', cut, y0 + H)):
        idx = [n for n, e in enumerate(ext) if lo <= (e[2] + e[3]) / 2 < hi or (e[3] - e[2]) > 0.9 * H]
        if not ext: idx = list(range(len(F['items'])))
        if not idx: continue          # nothing in this half: the caller keeps the figure whole
        ys = [v for n in idx for v in (ext[n][2], ext[n][3])] if ext else [lo, hi]
        a, b = max(y0, min(ys) - 12), min(y0 + H, max(ys) + 12)
        items = [F['items'][n] for n in idx]
        try:
            st = group_steps([{'ext': ext[n], 'tag': F['tags'][n]} for n in idx], [vb[0], a, vb[2], b - a])
            items = [[it[0], it[1], q] for it, q in zip(items, st)]
        except Exception:
            pass
        out.append((half, [vb[0], round(a, 1), vb[2], round(b - a, 1)], {'vb': vb, 'defs': F['defs'], 'items': items}))
    return out

# ---------------- the book ----------------
def parse_book(h):
    B = {}
    t = re.search(r'<title>(.*?)</title>', h, flags=re.S)
    B['title'] = txt(t.group(1)) if t else ''
    hero = re.search(r'<h1>(.*?)<small>(.*?)</small></h1>', h, flags=re.S)
    B['subject'] = txt(hero.group(1)) if hero else ''
    um = re.match(r'Unit\s+(\d+)\s*·\s*(.*)', txt(hero.group(2))) if hero else None
    B['unit'], B['unit_name'] = (int(um.group(1)), um.group(2)) if um else (0, '')
    cr = re.search(r'<span class="crumb">(.*?)</span>', h, flags=re.S)
    B['crumb'] = txt(cr.group(1)) if cr else ''
    rt = re.search(r':root\{(.*?)\}', h, flags=re.S)
    B['vars'] = ';'.join(v.strip() for v in rt.group(1).split(';') if v.strip().startswith('--') and 'font' not in v and '--u-' not in v) if rt else ''
    mi = h.find('<main', max(0, h.find('<body')))   # the real <main> (a shell comment may contain the text "<main>")
    main = h[mi:h.find('</main>', mi)]
    B['chapters'] = []
    for m in re.finditer(r'<section class="ch" id="([^"]+)"[^>]*>(.*?)</section>', main, flags=re.S):
        cid, sec = m.group(1), m.group(2)
        hd = re.search(r'<h2>\s*<span class="num">([\d.]+)</span>\s*(.*?)</h2>', sec, flags=re.S)
        ch = {'id': cid, 'num': hd.group(1), 'title': txt(hd.group(2)), 'words': len(txt(sec).split())}
        lead = re.search(r'<p class="lead">(.*?)</p>', sec, flags=re.S)
        ch['lead'] = txt(lead.group(1)) if lead else ''
        ch['h3'] = [txt(x) for x in re.findall(r'<h3>(.*?)</h3>', sec, flags=re.S)]
        body = re.sub(r'<div class="(example|traps|quiz|beyond|prereq)">.*?</div>\s*(?=<div|<h3|<p|<figure|$)', '', sec, flags=re.S)
        ch['body'] = [txt(p) for p in re.findall(r'<p>(.*?)</p>', body, flags=re.S)][:14]
        ch['figs'] = []
        for f in re.finditer(r'<figure class="fig">(.*?)</figure>', sec, flags=re.S):
            svg = re.search(r'<svg.*?</svg>', f.group(1), flags=re.S)
            cap = re.search(r'<figcaption>(.*?)</figcaption>', f.group(1), flags=re.S)
            if svg:
                F = split_svg(svg.group(0))
                capt = txt(cap.group(1)) if cap else ''
                fm = re.match(r'(Figure\s+[\d.]+)\s*(.*)', capt)
                F['label'], F['caption'] = (fm.group(1), fm.group(2)) if fm else ('', capt)
                ch['figs'].append(F)
        ch['examples'] = []
        for ex in re.finditer(r'<div class="example">(.*?)</div>\s*(?=<div class="example"|<div class="traps"|<div class="quiz"|<h3|<p|<figure)', sec, flags=re.S):
            e = ex.group(1)
            hd4 = re.search(r'<h4>(.*?)</h4>', e, flags=re.S)
            ps = [txt(p) for p in re.findall(r'<p>(.*?)</p>', e, flags=re.S)]
            q = next((p for p in ps if p.startswith('Question')), ps[0] if ps else '')
            idea = next((p for p in ps if p.startswith('Idea')), '')
            ans = next((p for p in ps if p.startswith('Answer')), '')
            steps = [txt(x) for x in re.findall(r'<li>(.*?)</li>', e, flags=re.S)]
            ch['examples'].append({'name': txt(hd4.group(1)) if hd4 else 'Worked example', 'q': re.sub(r'^Question\.?\s*', '', q),
                                   'idea': re.sub(r'^Idea\.?\s*', '', idea), 'steps': steps, 'answer': re.sub(r'^Answer\.?\s*', '', ans),
                                   'numeric': bool(re.search(r'\d\s*(?:[×x÷/=+−-]|mm|µm|nm|mV|kJ|%|M\b|atm)', ' '.join(steps)))})
        tr = re.search(r'<div class="traps">(.*?)</div>', sec, flags=re.S)
        ch['traps'] = [txt(x) for x in re.findall(r'<li>(.*?)</li>', tr.group(1), flags=re.S)] if tr else []
        ch['quiz'] = parse_q(sec)
        bey = re.search(r'<div class="beyond">(.*?)</div>', sec, flags=re.S)
        ch['beyond'] = txt(bey.group(1)) if bey else ''
        B['chapters'].append(ch)
    qb = re.search(r'<section id="question-bank">(.*?)</section>', main, flags=re.S)
    B['bank'] = parse_q(qb.group(1)) if qb else []
    gl = re.search(r'<section id="glossary">(.*?)</section>', main, flags=re.S)
    B['glossary'] = [txt(d) for d in re.findall(r'<dt>(.*?)</dt>', gl.group(1), flags=re.S)] if gl else []
    so = re.search(r'<section id="sources">(.*?)</section>', main, flags=re.S)
    B['sources'] = [txt(x) for x in re.findall(r'<li>(.*?)</li>', so.group(1), flags=re.S)][:4] if so else []
    return B


def parse_q(s):
    out = []
    for m in re.finditer(r'<details class="q" data-level="(\w+)"[^>]*>\s*<summary>(.*?)</summary>(.*?)</details>', s, flags=re.S):
        summ = re.sub(r'<span class="lvl">.*?</span>', '', m.group(2), flags=re.S)
        mk = re.search(r'<span class="marks">(.*?)</span>', summ, flags=re.S)
        summ = re.sub(r'<span class="marks">.*?</span>', '', summ, flags=re.S)
        out.append({'lv': LV.get(m.group(1).lower(), 'U'), 'q': txt(summ), 'marks': txt(mk.group(1)) if mk else '', 'a': txt(m.group(3))})
    return out


def split_lessons(chs, spec=None):
    if spec:
        groups = []
        for part in spec.split(','):
            a, _, b = part.partition('-')
            b = b or a
            groups.append([c for c in chs if tuple(map(int, a.split('.'))) <= tuple(map(int, c['num'].split('.'))) <= tuple(map(int, b.split('.')))])
        return groups
    n = len(chs)
    best = None
    # all ways to cut into groups of 2-3 chapters (a group of 1 only when the unit has 1 chapter or a chapter is huge)
    def rec(i, acc):
        nonlocal best
        if i == n:
            w = [sum(c['words'] for c in g) for g in acc]
            score = max(w) - min(w) + 400 * len(acc)  # balanced, and as few lessons as reasonable
            if best is None or score < best[0]:
                best = (score, [list(g) for g in acc])
            return
        for k in (2, 3, 1):
            if i + k <= n and (k > 1 or n == 1 or chs[i]['words'] > 2600):
                if sum(c['words'] for c in chs[i:i + k]) <= 4300 or k == 1:
                    rec(i + k, acc + [chs[i:i + k]])
    rec(0, [])
    return best[1] if best else [chs]


# ---------------- writing the lesson file ----------------
def chip(title):
    w = re.sub(r'[:;,].*$', '', title).upper().split()
    if len(w) == 1:
        return [w[0], '']
    h = (len(w) + 1) // 2
    return [' '.join(w[:h]), ' '.join(w[h:])]


def ribbon2(chs):
    n = sum(len(c['examples']) for c in chs)
    num = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    parts = num.get(len(chs), str(len(chs)))
    ex = 'no worked example' if n == 0 else f"{num.get(n, str(n))} worked example{'s' if n > 1 else ''}"
    return f"{parts.capitalize()} parts, {ex}, and exam practice"


def pick_questions(lesson_chs, bank):
    pool = [q for c in lesson_chs for q in c['quiz']]
    nums = [c['num'] for c in lesson_chs]
    out = []
    for lv in ('U', 'A', 'N'):
        cand = [q for q in pool if q['lv'] == lv] or [q for q in bank if q['lv'] == lv and any(n in q['q'] + q['a'] for n in nums)] or [q for q in bank if q['lv'] == lv]
        cand = [q for q in cand if q not in out]
        if cand:
            out.append(sorted(cand, key=lambda q: len(q['q']))[0] if lv == 'U' else cand[0])
    return out


def lesson_js(B, k, K, chs, meta):
    sid, N = meta['sid'], B['unit']
    a, b = chs[0]['num'], chs[-1]['num']
    span = f'chapter {a}' if a == b else f'chapters {a} to {b}'
    L = []
    w = L.append
    w(f"/* ===== {B['subject']} · Unit {N} · Lesson {k} of {K} ({span}) — generated by book2lesson.py from the library book")
    w(f"   {meta['book']} (sha256 {meta['sha'][:12]}). Replace every marked field; read WRITE.md beside this file first. ===== */")
    w("/* phonemes (misaki) for every technical name the narrator says; P('X') puts it in a line. Add the names you say. */")
    w("const PR={};")
    w("const P=k=>`[${k}](/${PR[k]}/)`;")
    w(f"const BOOKVARS={js(B['vars'])};")
    parts = [c['title'] for c in chs]
    w(f"const META={{n:{k}, subject:{js(meta['subject'])}, title:'TODO short lesson title', badge:'Lesson', kick:{js(B['subject'].upper())},   /* the engine adds ' · ' + the title: no unit or lesson number */")
    w(f"  series:'University free n easy', big:'TODO ONE WORD', star:'TODO starring line',")
    w(f"  parts:{js(parts)},   // TODO shorten each to 2-4 words")
    w(f"  chips:{js([chip(p) for p in parts])}}};   // TODO two short upper-case lines per part")
    w("const RC=META.parts.length+1, QZ=RC+1, LS=RC+2, OUT=RC+3;")
    w("const SC=[")
    w("/* ---- intro ---- IMPROVISE: the hook is the one place for a fresh idea (a daily-life or engineering moment the lesson explains) */")
    w("{s:0,k:'hookArt',term:'Hook',say:'TODO',cues:{},art:[['TODO icon','a',1110,440,1.6]],caps:[['TODO','c1'],['TODO','c2'],['TODO','c3',1]],bang:['TODO question','b']},")
    w(f"{{s:0,k:'agenda',term:'Today',say:'TODO Today, … Three parts, one worked example, and exam practice.',cues:{{t:'TODO',r:'TODO',p1:'TODO',p2:'TODO'{',p3:' + js('TODO') if len(chs) > 2 else ''},q:'TODO'}},big:META.big,ribbon:'TODO',ribbon2:{js(ribbon2(chs))},star:{js(NUMW[len(chs)].capitalize() + ' chapters of your free notes' if len(chs) > 1 else 'One chapter of your free notes')}}},")
    for i, c in enumerate(chs, 1):
        w(f"/* ---- part {i}: {c['num']} {c['title']} ({c['words']} words in the book) ---- */")
        pts = [(lambda t: t if len(t) <= 46 else t[:46].rsplit(' ', 1)[0])(re.sub(r'\s*\(.*?\)', '', x)) for x in c['h3'][:3]] or ['TODO', 'TODO', 'TODO']
        w(f"{{s:{i},k:'part',n:{i},term:{js('Part ' + str(i))},say:'TODO',cues:{{p:'TODO',o:'TODO'}},pts:{js(pts)}}},   // pts are the book's sub-headings: shorten if long")
        w(f"/* book: lead: {c['lead'][:400]} */")
        for j, F in enumerate(c['figs']):
            vb = F['vb']
            scale = min(1440 / vb[2], 600 / vb[3], 2.6)
            fs = round(F.get('minfs', 13) * scale)
            w(f"/* book {F['label']}: {F['caption'][:300]} */")
            fig = js({k2: F[k2] for k2 in ('vb', 'defs', 'items')})
            hv = halves(F) if fs < 22 and vb[3] >= 260 else []
            if len(hv) == 2:
                for half, view, sub in hv:
                    w(f"{{s:{i},k:'bookfig',term:{js('Figure: ' + c['title'][:40] + ' (' + half + ')')},title:{js(c['title'])},view:{js(view)},say:'TODO walk through this half of the figure',cues:{{s1:'TODO',s2:'TODO',s3:'TODO',cap:'TODO'}},steps:4,cap:'TODO one-line takeaway',fig:{js(sub)}}},   // IMPROVISE: auto-zoomed (text would be ~{fs}px whole); cut at a clean gap with only this half's pieces; adjust view:[x,y,w,h] or merge back")
            else:
                w(f"{{s:{i},k:'bookfig',term:{js('Figure: ' + c['title'][:40])},title:{js(c['title'])},say:'TODO walk through the figure in the order it builds',cues:{{s1:'TODO',s2:'TODO',s3:'TODO',s4:'TODO',cap:'TODO'}},steps:4,cap:'TODO one-line takeaway',fig:{fig}}},   // build steps are each item's third value (1-4): change them if the order reads wrong")
        w(f"/* book: the chapter, paragraph by paragraph (first sentences):")
        for p in c['body'][:10]:
            w('   - ' + (sentences(p)[0] if sentences(p) else p)[:240].replace('*/', '* /'))
        w("*/")
        w(f"{{s:{i},k:'notebook',term:'Key ideas',title:'TODO',say:'TODO',cues:{{i1:'TODO',i2:'TODO',i3:'TODO',i4:'TODO'}},items:[['TODO','i1'],['TODO','i2'],['TODO','i3'],['TODO','i4']],vis:(c,u,b)=>'TODO picture of the points'}},   // IMPROVISE vis: a picture building item by item; or use cards/flow if the idea is a comparison or a sequence")
        for ei, e in enumerate(c['examples']):
            nm = e['name'] if len(c['examples']) > 1 else 'Worked example'
            w(f"/* book {e['name']}: Q: {e['q'][:600]}")
            if e['idea']:
                w(f"   Idea: {e['idea'][:400]}")
            for n_, s_ in enumerate(e['steps'], 1):
                w(f"   {n_}. {s_[:400]}")
            w(f"   Answer: {e['answer'][:400]} */")
            if e['numeric']:
                ns = len(e['steps'])
                steps = [[f'TODO step {n_}', 'TODO stage', f'k{n_}'] for n_ in range(1, min(4, ns) + 1)]
                more = '   // IMPROVISE: the book has %d steps; split into two calc scenes with live:[0,1,2] and live:[3,…]' % ns if ns > 4 else ''
                w(f"{{s:{i},k:'calc',term:{js(nm)},title:{js(nm)},say:'TODO',cues:{{fk:'TODO',{','.join(f'k{n_}:' + js('TODO') for n_ in range(1, len(steps) + 1))},a:'TODO'}},q:['TODO question, two short lines'],f:['TODO formula'],hint:'TODO one-line hint',fk:'fk',steps:{js(steps)},ans:['TODO answer','a']}},{more}")
            else:
                w(f"{{s:{i},k:'notebook',term:{js(nm)},title:{js(nm)},say:'TODO',cues:{{i1:'TODO',i2:'TODO',i3:'TODO'}},items:[['TODO','i1'],['TODO','i2'],['TODO','i3']],vis:(c,u,b)=>'TODO picture of the steps'}},   // IMPROVISE vis")
        if c['traps']:
            w(f"/* book exam traps: " + ' | '.join(t[:260] for t in c['traps']) + " */")
            w(f"{{s:{i},k:'trap2',term:'Exam trap',title:'Exam trap!',say:'TODO',cues:{{x:'TODO',w:'TODO',r:'TODO'}},wl:\"Don't write\",rl:'Write',wrong:['TODO'],right:['TODO'],wv:(c,u,b)=>'TODO picture of the wrong idea',rv:(c,u,b)=>'TODO picture of the right idea'}},   // the book's sharpest trap; IMPROVISE wv/rv")
    w("/* ---- recap ---- */")
    heads = [chip(c['title'])[0].title() for c in chs][:3]
    if len(heads) < 3:
        heads += ['TODO third panel (the evidence, the rule, or the key number)'] * (3 - len(heads))
    w(f"{{s:RC,k:'recap',term:'Recap',say:'TODO',cues:{{{','.join(f'r{i}:' + js('TODO') for i in range(1, 4))}}},panels:[{','.join('[' + js(h_) + ',' + js(['BLU', 'ORG', 'GRN'][i]) + ",'TODO own picture: draw it as ICON.name in EXTRA, not a built-in icon',['TODO','TODO'],'r" + str(i + 1) + "']" for i, h_ in enumerate(heads))}],live:[0,1,2]}},   // the recap always has three panels")
    w("/* ---- exam practice: the book's own questions and model answers. vis (an animated answer picture on the left) is IMPROVISE: add it where the answer can be drawn ---- */")
    for n_, q in enumerate(pick_questions(chs, B['bank']), 1):
        al = sentences(q['a'])[:4]
        w(f"{{s:QZ,k:'pq',term:'Question {n_}',lv:'{q['lv']}',n:{n_},q:{js(q['q'])},say:'TODO ask it in your own words.',cues:{{k:'TODO',q:'TODO'}},pause:3.4}},   // {q['marks']}")
        numeric = bool(re.search(r'\d\s*(?:[×x÷/=+−-]|µm|nm|mV|kJ|atm|M\b|s\b)', q['a']))
        tip = '   // the answer is a calculation: replace al with calc:{f,hint,fk,steps,live} so the working transforms on screen' if numeric else '   // shorten each line to fit; book answer above'
        w(f"{{s:QZ,k:'pa',term:'Answer {n_}',lv:'{q['lv']}',n:{n_},q:{js(q['q'])},say:'TODO',cues:{{{','.join(f'a{j}:' + js('TODO') for j in range(1, len(al) + 1))}}},al:[{','.join('[' + js(x) + ",'a" + str(j) + "']" for j, x in enumerate(al, 1))}]}},{tip}")
    tags = [['Free notes for this lesson (PDF)', 'link in the description'],   # only lesson PDFs are offered (3 Nov 2026)
            ['In this lesson', '; '.join(c['title'] for c in chs)[:120]],   # chapter titles, never numbers (they reveal the unit)
            ['Key terms and glossary', 'at the end of the notes']]
    def clip(t, n):
        return t if len(t) <= n else t[:n].rsplit(' ', 1)[0].rstrip(',;:') + '…'
    figs = [[clip(c['title'], 40), clip(F['caption'] or c['title'], 150)] for c in chs for F in c['figs']]   # named by content, never 'Figure 1.1.1' (chapter numbers reveal the unit)
    def src_short(x):
        m = re.match(r'(.+?),\s*(?:and others,|et al\.?,)?\s*(.+?)(?:,|\.\s)', x)
        a_ = x.split(',')[0]
        t_ = re.split(r',\s*(?:\d+(?:st|nd|rd|th) ed|[A-Z][a-z]+ (?:Press|Freeman|Science|Wiley|Pearson|Elsevier))', x)[0]
        t_ = t_.split(',')[-1].strip() if ',' in t_ else t_
        return f"{a_} ({t_})" if t_ and t_ != a_ else a_
    note = ''
    for x in (B['sources'] or [])[:3]:
        cand = (note + '; ' if note else 'Sources your free notes draw on: ') + src_short(x)
        if len(cand) > 200: break
        note = cand
    if B['sources'] and not note: note = 'Sources your free notes draw on: ' + src_short(B['sources'][0]).rsplit(' ', 1)[0][:170]
    w(f"{{s:LS,k:'figs',term:'Your notes',title:'For your notes',say:'TODO',cues:{{t:'TODO',f:'TODO'}},tags:{js(tags)},figs:{js(figs)},note:{js(note)}}},")
    nxt = meta['next']
    w(f"{{s:OUT,k:'outro',term:'Outro',say:'TODO So remember: … Next time, {nxt[1]}. See you there!',cues:{{f:'TODO',n:'TODO',s:'TODO'}},words:[['TODO','BLU','w1'],['TODO','ORG','w2'],['TODO','GRN','w3']],next:{js(nxt)},end:'See you there!'}}")
    w("];")
    return '\n'.join(L) + '\n'


# the bookfig kind: also added to lesson_template.html; kept here so a lesson file built against an older template still works
BOOKFIG_EXTRA = r"""/* bookfig: the book's own figure, built up piece by piece (engine kind; this fallback only runs on templates without it) */
function EXTRA(R,ICON){if(R.bookfig)return;R.bookfig=(sc,c,u)=>{let s=pageBG(u,BLU)+title(sc.title||'From your free notes');const F=sc.fig,V=sc.view||F.vb,top=sc.cap?170:180,bot=sc.cap?776:856,
 k=Math.min(1440/V[2],(bot-top)/V[3],sc.max||2.6),w=V[2]*k,h=V[3]*k,ox=80+(1440-w)/2,oy=top+(bot-top-h)/2,n=F.items.length,N=Math.max(1,Math.min(sc.steps||4,n));
 const ord=F.items.map((it,i)=>[it[0],i]).sort((a,b)=>a[0]-b[0]||a[1]-b[1]),st=[];ord.forEach(([,i],j)=>st[i]=Math.min(N-1,Math.floor(j*N/n)));
 const T=q=>c['s'+(q+1)]!=null?tk(c,'s'+(q+1)):.3+q*Math.max(.6,(c.end||8)*.7/N);let inner=F.defs||'';F.items.forEach((it,i)=>{inner+=sc.static?it[1]:g('fade',T(st[i]),it[1])});
 s+=panel(ox-28,oy-22,w+56,h+44,{fill:WHT})+`<svg x="${S(ox)}" y="${S(oy)}" width="${S(w)}" height="${S(h)}" viewBox="${V.join(' ')}"${sc.view?'':' overflow="visible"'}><g style="${typeof BOOKVARS==='string'?BOOKVARS:''}" font-family="${LF}" fill="${INK}" color="${INK}">${inner}</g></svg>`;
 if(sc.cap)s+=g('rise',tk(c,'cap'),capbox(800,bot+14,sc.cap,{fs:fit(sc.cap,30,1400),a:'middle'}));return s}}"""

WRITE_MD = r"""# Fill these lesson files (fast path of the ufe-unit-lessons skill)

The files here were generated from the library unit book by `book2lesson.py`. Everything that comes from the book is
already on screen (part slides, the book's figures, worked-example text, traps, exam questions with the book's model
answers, notes page, next card). Your job is the writing: replace every `TODO`. Do not read the whole skill or the
reference lessons unless something below is unclear; `lesson_kinds.md` has the field list of every kind.

## What to write

- `say`: one narration line per scene, warm, second person, short sentences, 20 to 40 words (pq lines shorter).
  The whole lesson 800 to 880 words (5 to 7 minutes; the check prints the count). Say only what the book says.
- The student's notes are this lesson's free notes PDF, linked in the description: say "your free notes" (hook
  `star`, notes page), never "unit book", the finder or the site. Only lesson PDFs are offered (no unit books).
- `cues`: for every key the scene uses, the first two to four words of the phrase in `say` where that thing should
  appear. The phrase must occur exactly in the line.
- Short on-screen text: titles, notebook items (under 60 characters each), trap lines, recap lines, the shortened `al`
  answer lines (keep the book's facts, cut the words), META.title/big/star/parts/chips, the hook.
- `bookfig`: narrate the figure in the order it builds (left to right, `steps` pieces, cues `s1..s4`) and give `cap`
  one takeaway line. Delete a figure scene only if it duplicates another.
- `calc`: `q` two short lines, `f` the formula(s) on the board, `hint`, then each step's `stage` as the row the
  narrator reaches (use `['τ = 1 / 0.05','τ = 20 s']` for a row that transforms). Work every number in python first.
- Two or three light jokes (not more) in hook, notebook or bookfig lines (never in definitions, traps, questions or answers).
- `agenda.ribbon2` is already counted from the book (parts, worked examples); keep it unless you cut a worked example.
- `pa.vis` (optional answer picture): drawn in a box about 620 × 510 with origin top left; it may use its own cue keys
  (add them to `cues`); keep everything inside the box.
- `calc` draws only the rows up to the last `live` index; a long example is two calc scenes (`live:[0,1,2]`, `live:[3,4]`).
- `bookfig`: each figure item is `[x, svg, step]`; the generator groups pieces into steps (background first, then up to
  three left-to-right groups, labels with their shape). If the order reads wrong, change the step numbers (1-4), not
  the drawing. Cue each step `s1..s4` to the words that name it, and cue `cap` early enough to be read (not the last word).
- The contact sheet shows each scene at 92% of its time; a caption or stamp cued at the very end will not be on it.

## Kokoro safety (the build checks these)

- No digits or symbols in `say`: write numbers and units as words ("seven point five micrometres").
- Technical names, acronyms and Greek letters go in `PR` (misaki phonemes) and are spoken as `${P('ATP')}`; copy
  existing entries from `pronunciation.json` beside the engine. Other words the dictionary lacks go in YOUR lesson's
  `<lesson>.pron.json` beside it (never edit another lesson's file; the build reads the engine's, the folder's and yours).
  A bare letter A is written `[A](/ˈA/)`.
- US spellings in `say` (the on-screen text may keep the book's spelling).
- No college or university names anywhere, and no real organisation's brand in examples.

## Text the check fails (SLOP.md rules; they run on every `say`, on the text each scene draws, and on META)

- "book" in any form ("your book", "the book's figure", "unit book"): say "your free notes"; "of your notes" without "free".
- Unit numbers or unit references ("Unit two", "this unit", "all six units", "(Unit 4)"): the syllabus is universal, so
  name the topic instead ("in the lesson on phase estimation", "next time: process scheduling").
- Bloom levels, spoken or shown ("An apply question", "at the analyze level", "Question two, apply."): say only
  "Question one / two / three".
- Caret or underscore maths on screen (`2^(n−1)`, `x_i`, `S_W`): use ² ⁻¹ ₐ or a sub/sup tspan
  (`V<tspan baseline-shift="sub" font-size="70%">in</tspan>`). Code in a monospace font is exempt.
- A site or finder line ("find this unit in your syllabus on the site"): there is no site yet.
- A real content phrase that trips a rule ("booking site", "OP_DUP", "the library issues the book") goes in
  `META.allow:['booking site']`. Warnings (printed, not failing): built-in recap icons, Indian and Western number
  grouping in one lesson, filler words (imagine, journey, crucial, amazing, delve, unlock).

## Facts (a fact review recomputes these before the subject is approved)

- Every `pq` shows all its givens on screen; its `pa` uses only those and what the lesson showed. A question that
  reuses or changes the worked example's data says so.
- A trap's "Don't write" must be wrong under every common convention, and its stated wrong result must be what that
  mistake really produces (recompute it). If the rule depends on a convention, the card names it.
- Software, protocol and kernel behaviour names its version or era on screen ("since GCC 14", "since React 17",
  "before the Merge, 2022"); keep the book's caveats ("simplified", "for every p", "sufficient, not necessary").
- Draw the end state the line states, in the colours the numbers give; a picture never contradicts its narration.
- Code on screen is complete and runs as shown, or is marked `frag:true`; output shown is what it prints.
- If you find an error in the book, write it in your hand-back; do not narrate around it.
- Recap pictures are the lesson's own (draw them in `EXTRA` as `ICON.name`), filling most of their card.

## Pictures on every list page (required)

Every `notebook` page gets `vis:(c,u,box)=>svg`: a picture of its points in the mint panel on the left (640 × 690; the list sits on the right),
each part landing on its item's cue (`g('pop', tk(c,'i1'), …)`), building one diagram as the narrator goes. Every `trap2`
gets `wv` and `rv` (640 × 330 inside each card): the wrong idea drawn (the engine strikes it through) and the right idea
drawn. Draw what the line says, exactly as the book says it: molecules, membranes, arrows, before/after, a tiny graph.
A `traps` list gets the same left panel, one small picture per trap on its cue. Trap pages are in the dull crimson `TRED`:
number any rows in a trap picture with `TRED` badges at `fill-opacity="${TOP}"` (80 %), not `RED`. Never shorten an on-screen line to fit: long lines wrap.

## Where to spend more effort (IMPROVISE)

Only the scenes marked IMPROVISE in the file: the hook, a `vis` answer picture when the answer is a mechanism or a
comparison, a figure whose text would be too small (zoom with `view:[x,y,w,h]` or split it), and a process the book
draws statically but that only makes sense moving (a cycle, a cascade): then a bespoke kind in `EXTRA` is worth it.
Everything else is filling, not designing.

## Build and check (in this order, stop at the first failure and fix it)

```bash
E=<engine dir>   # lesson_template.html, lesson_build.py, lesson_sheet.py, bumper/
python3 $E/lesson_build.py L.js out.html --check        # every TODO left fails; fix until clean
python3 $E/lesson_build.py L.js out.html                # voice + HTML
python3 $E/lesson_sheet.py out.html sheet/ --frames --play
```

The sheet must end clean: 0 page errors, 0 cue failures, 0 text outside the safe area, play-through OK. Then look
only at: `sheet/sheet.png` (once, whole lesson), every frame the report lists, the `bookfig` and `calc` frames, and
the four logo frames `B_*`, and every layout warning it prints (text over text, text past its card, small recap
pictures, book figures under half the stage or cut). Fix what is wrong and rebuild with `--reuse` (keeps the voice) when
only the drawing changed, or `--revoice` (voices only the changed lines) when some narration changed.
"""


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        sys.exit(2)
    book, out = argv[0], argv[1]
    spec = argv[argv.index('--split') + 1] if '--split' in argv else None
    if '--subject' not in argv: sys.exit('--subject is required (the subject id, e.g. c-xr): META.subject has no default')
    subject = argv[argv.index('--subject') + 1]
    next_unit = argv[argv.index('--next-unit') + 1] if '--next-unit' in argv else ''
    h = open(book, encoding='utf8').read()
    B = parse_book(h)
    sid = os.path.basename(book).rsplit('-u', 1)[0]
    N = B['unit']
    groups = split_lessons(B['chapters'], spec)
    K = len(groups)
    os.makedirs(out, exist_ok=True)
    sha = hashlib.sha256(h.encode('utf8')).hexdigest()
    vids = {'lessons': []}
    for k, chs in enumerate(groups, 1):
        if k < K:
            nx = ['NEXT TIME', 'Next lesson', ' · '.join(c['title'].split(':')[0].strip() for c in groups[k]), 'book']   # whole chapter titles, no numbers
            nxs = groups[k][0]['title'].split(':')[0].lower()
        else:
            nx = ['UP NEXT', 'Next topic', next_unit or 'TODO next topic title', 'book']   # the topic, never "Unit N"
            nxs = (next_unit or 'TODO').lower()
        meta = {'sid': sid, 'subject': subject, 'book': os.path.basename(book), 'sha': sha, 'next': nx}
        meta['next'] = nx
        src = lesson_js(B, k, K, chs, meta).replace(f"Next time, {nx[1]}.", f"Next time, {nxs}.".replace("'", "\\'"))
        p = os.path.join(out, f'{sid}-u{N}-L{k}.js')
        open(p, 'w', encoding='utf8').write(src)
        pp = os.path.join(out, f'{sid}-u{N}-L{k}.pron.json')
        if not os.path.exists(pp):
            open(pp, 'w', encoding='utf8').write('{}\n')
        a, b = chs[0]['num'], chs[-1]['num']
        vids['lessons'].append({'n': k, 'title': 'TODO', 'chapters': a if a == b else f'{a}-{b}', 'video': ''})
        print(f'  {p}: chapters {a}-{b}, {sum(c["words"] for c in chs)} book words, {sum(len(c["figs"]) for c in chs)} figures, TODOs {src.count("TODO")}')
    json.dump({f'{sid}-u{N}': vids}, open(os.path.join(out, f'videos.{sid}-u{N}.json'), 'w'), indent=1)
    open(os.path.join(out, 'WRITE.md'), 'w').write(WRITE_MD)
    pj = os.path.join(out, 'pronunciation.json')
    if not os.path.exists(pj):
        base = {}
        here = os.path.dirname(os.path.abspath(__file__))
        for f in (os.path.join(here, 'pronunciation.json'),):
            if os.path.exists(f):
                base.update(json.load(open(f, encoding='utf8')))
        json.dump(base, open(pj, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    print(f'{B["subject"]} Unit {N} ({B["unit_name"]}): {len(B["chapters"])} chapters -> {K} lessons; WRITE.md and videos json written to {out}')


if __name__ == '__main__':
    main(sys.argv[1:])
