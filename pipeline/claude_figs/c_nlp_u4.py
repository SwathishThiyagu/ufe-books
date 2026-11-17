"""Claude's hand-drawn figures for c-nlp-u4 (NLP, unit 4: semantics and discourse), one per chapter, drawn from each
chapter's worked example, plus the university-hosted sources to drop. The figure sentence in 4.8 still matches."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {}
TEXT = {}


# ---- 4.1 the model that makes "Every student reads a book" true, and the one that makes it false ----
def f1():
    o = []
    def model(x0, title, edges, ok):
        r = [T(x0 + 170, 24, title, 15, bold=True)]
        r.append(R(x0 + 10, 40, 140, 150, ACS, AC, 10, 1.5, '6 4'))
        r.append(T(x0 + 80, 58, 'Student', 13, fill=AC, bold=True))
        r.append(R(x0 + 200, 40, 130, 150, PANEL, L2, 10, 1.5, '6 4'))
        r.append(T(x0 + 265, 58, 'Book', 13, fill=MUT, bold=True))
        P_ = {'Ravi': (x0 + 80, 92), 'Meera': (x0 + 80, 152), 'Gita': (x0 + 80, 222), 'book1': (x0 + 265, 92), 'book2': (x0 + 265, 152)}
        for a, b in edges:
            (x1, y1), (x2, y2) = P_[a], P_[b]
            r.append(L(x1 + 38, y1, x2 - 42, y2, AC, 2.5, arrow='n'))
            r.append(Tb((x1 + x2) / 2, y1 - 8, 'Reads', 12, fill=AC))
        for n, (x, y) in P_.items():
            r.append(boxt(x - 36, y - 15, 72, 30, [n], FIGBG, L2 if n == 'Gita' else AC, 14))
        r.append(T(x0 + 80, 252, 'not a student: no duty', 12, fill=MUT))
        if not ok:
            r.append(T(x0 + 172, 160, '✗', 22, fill=NX, bold=True))
        r.append(boxt(x0 + 10, 270, 320, 52, ['2 of 2 students read a book', 'formula TRUE'] if ok else ['Meera reads no book: 1 of 2', 'formula FALSE'],
                      ACS if ok else NXS, AC if ok else NX, 14, True))
        return ''.join(r)
    o.append(model(0, '(b) Reads = {(Ravi, book1), (Meera, book2)}', [('Ravi', 'book1'), ('Meera', 'book2')], True))
    o.append(model(370, '(c) Reads = {(Ravi, book1)}', [('Ravi', 'book1')], False))
    o.append(T(360, 352, '∀x(Student(x) → ∃y(Book(y) ∧ Reads(x, y)))', 16, bold=True))
    o.append(T(360, 378, 'No single book is read by both students, so the stronger ∃y∀x form is false in (b).', 13, fill=MUT))
    return 392, ''.join(o)
FIG[1] = (f1, 'The formula needs a Reads arrow from every student to some book. In model (b) Ravi and Meera each have one, so it is true; Gita is not a student and owes nothing. In (c) Meera has none, so the ∀ fails.',
          'Two models side by side: Ravi, Meera and Gita on the left, book1 and book2 on the right. In the first, Reads arrows go from Ravi to book1 and Meera to book2 and the formula is true; in the second only Ravi has an arrow and the formula is false.')
AFTER[1] = 4


# ---- 4.2 meanings built up the tree ----
def f2():
    o = []
    def node(x, y, w, cat, sem, fill=PANEL, c=AC):
        return R(x - w / 2, y - 22, w, 48, fill, c, 7, 1.6) + T(x - w / 2 + 10, y - 4, cat, 13, 'start', MUT, True) + T(x, y + 17, sem, 14, bold=True)
    edges = [((360, 42), (180, 156)), ((360, 42), (540, 156)), ((180, 156), (100, 248)), ((180, 156), (268, 248)),
             ((540, 156), (430, 248)), ((540, 156), (620, 248))]
    for (x1, y1), (x2, y2) in edges:
        o.append(L(x1, y1 + 26, x2, y2 - 22, L2, 1.5))
    o.append(node(360, 42, 440, 'S', '∀x(Student(x) → ∃y(Book(y) ∧ Reads(x,y)))', NXS, NX))
    o.append(node(180, 156, 300, 'NP', 'λQ.∀x(Student(x) → Q(x))', ACS))
    o.append(node(540, 156, 300, 'VP', 'λx.∃y(Book(y) ∧ Reads(x,y))', ACS))
    o.append(node(100, 248, 170, 'Det every', 'λP.λQ.∀x(P(x)→Q(x))'))
    o.append(node(268, 248, 150, 'N student', 'λx.Student(x)'))
    o.append(node(430, 248, 150, 'V reads', 'λy.λx.Reads(x,y)'))
    o.append(node(620, 248, 190, 'NP a book', 'λQ.∃y(Book(y) ∧ Q(y))'))
    o.append(T(20, 312, 'The subject NP is applied last, outside the VP, so ∀ takes wide scope: the surface reading.', 14, 'start'))
    o.append(T(20, 336, 'Other reading (object wide): ∃y(Book(y) ∧ ∀x(Student(x) → Reads(x,y))).', 14, 'start', MUT))
    return 350, ''.join(o)
FIG[2] = (f2, 'Each phrase node holds the meaning its rule builds from its children. The object NP joins reads to make the VP, and the subject NP is applied last, so ∀ ends up outside ∃: the surface reading.',
          'A parse tree for Every student reads a book with a lambda meaning in every node: the determiners and nouns at the bottom, the subject NP and the VP in the middle, and the final logical form at S.')


# ---- 4.3 Wu-Palmer for dog and cat ----
def f3():
    x0, dy = 120, 50
    o = [T(20, 24, 'depth', 13, 'start', MUT, True)]
    ys = {d: 50 + d * dy for d in range(7)}
    for d, y in ys.items():
        o.append(T(40, y + 5, str(d), 14, 'middle', MUT, True))
        o.append(L(60, y, 690, y, LN, 1, '2 5'))
    nodes = {'root': (360, 0, 'entity'), 'c': (360, 4, 'carnivore'), 'd5': (260, 5, ''), 'dog': (200, 6, 'dog'), 'cat': (470, 5, 'cat')}
    o.append(L(360, ys[0] + 14, 360, ys[4] - 15, L2, 2, '6 5'))
    o.append(T(372, (ys[0] + ys[4]) / 2, '4 edges', 13, 'start', MUT))
    o.append(L(360, ys[4] + 15, 260, ys[5] - 8, AC, 2.5)); o.append(L(260, ys[5] + 8, 200, ys[6] - 15, AC, 2.5))
    o.append(L(360, ys[4] + 15, 470, ys[5] - 15, NX, 2.5))
    o.append(C(260, ys[5], 7, AC))
    for k_, (x, d, lab) in nodes.items():
        if not lab: continue
        hl = k_ == 'c'
        w = tw(lab, 15) + 26
        o.append(R(x - w / 2, ys[d] - 15, w, 30, ACS if hl else PANEL, AC if k_ != 'cat' else NX, 6, 2 if hl else 1.6))
        o.append(T(x, ys[d] + 5, lab, 15, bold=True))
    o.append(T(440, ys[4] + 5, 'LCS of dog and cat', 13, 'start', AC, True))
    y = ys[6] + 44
    o.append(boxt(130, y, 460, 52, ['sim_WP = 2 × depth(LCS) ÷ (depth(dog) + depth(cat))', '= 2 × 4 ÷ (6 + 5) = 8 ÷ 11 = 0.727'], ACS, AC, 15))
    return y + 64, ''.join(o)
FIG[3] = (f3, 'dog sits at depth 6 and cat at depth 5; the deepest node above both, their lowest common subsumer, is carnivore at depth 4. Wu-Palmer gives 2 × 4 ÷ (6 + 5) = 8 ÷ 11 = 0.727.',
          'A depth ladder from 0 to 6: entity at depth 0, carnivore at depth 4, dog two levels below carnivore at depth 6 and cat one level below at depth 5; the Wu-Palmer formula below gives 0.727.')


# ---- 4.4 the toy WordNet chain ----
def f4():
    chain = [('entity', 0), ('vehicle', 1), ('motor vehicle', 2), ('car', 3), ('compact car', 4)]
    x, y0, dy = 160, 40, 64
    o = []
    for i, (n, d) in enumerate(chain):
        y = y0 + i * dy
        hl = n in ('car', 'motor vehicle')
        w = 170
        o.append(R(x - w / 2, y - 18, w, 36, ACS if hl else PANEL, AC if hl else L2, 7, 2 if hl else 1.5))
        o.append(T(x, y + 5, n, 15, bold=hl))
        o.append(T(x - w / 2 - 14, y + 5, f'depth {d}', 13, 'end', MUT))
        if i:
            o.append(L(x, y - 18, x, y - dy + 20, L2, 1.8, arrow='m'))
    o.append(T(x + 14, y0 + 2.5 * dy + 4, 'hypernym (is-a)', 12, 'start', MUT))
    # dist label
    o.append(P([(x + 92, y0 + 2 * dy), (x + 112, y0 + 2 * dy), (x + 112, y0 + 3 * dy), (x + 92, y0 + 3 * dy)], NX, 2.5))
    o.append(T(x + 120, y0 + 2.5 * dy + 5, '1 edge', 13, 'start', NX, True))
    # synset box
    sx = 400
    o.append(boxt(sx, y0 + 3 * dy - 34, 300, 68, ['synset car#1', '{car, auto, automobile, motorcar}'], PANEL, AC, 14, True))
    o.append(L(sx - 4, y0 + 3 * dy, x + 88, y0 + 3 * dy, AC, 1.5, '4 4'))
    o.append(boxt(sx, 40, 300, 56, ['path sim = 1 ÷ (1 + 1) = 0.5'], ACS, AC, 15))
    o.append(boxt(sx, 110, 300, 56, ['Wu-Palmer = 2 × 2 ÷ (3 + 2) = 0.8'], ACS, AC, 15))
    o.append(T(sx, y0 + 4 * dy + 5, 'compact car: a hyponym of car', 13, 'start', MUT))
    return y0 + 4 * dy + 30, ''.join(o)
FIG[4] = (f4, 'The toy hierarchy from entity at depth 0 down to compact car at depth 4. car and motor vehicle are 1 edge apart and motor vehicle is their common subsumer, so path similarity is 0.5 and Wu-Palmer is 2 × 2 ÷ (3 + 2) = 0.8.',
          'A vertical is-a chain entity, vehicle, motor vehicle, car, compact car with depths 0 to 4; car and motor vehicle are shaded and marked 1 edge apart; boxes give the car synset, path similarity 0.5 and Wu-Palmer 0.8.')


# ---- 4.5 simplified Lesk and the most frequent sense baseline ----
def f5():
    o = [T(20, 24, 'Context: The fisherman sat on the bank of the river.', 14, 'start', INK, True)]
    def chips(x, y, words, hit, c):
        r = []
        for w in words:
            ww = tw(w, 14) + 18
            on = w in hit
            r.append(R(x, y, ww, 30, ACS if on and c == AC else (NXS if on else PANEL), c if on else L2, 6, 2 if on else 1.2))
            r.append(T(x + ww / 2, y + 20, w, 14, bold=on))
            x += ww + 8
        return ''.join(r)
    o.append(T(150, 66, 'context', 13, 'end', MUT)); o.append(chips(160, 46, ['fisherman', 'sat', 'river'], {'river'}, AC))
    o.append(T(150, 126, 'bank1 gloss', 13, 'end', MUT)); o.append(chips(160, 106, ['financial', 'institution', 'accepts', 'deposits'], set(), AC))
    o.append(T(150, 176, 'bank2 gloss', 13, 'end', MUT)); o.append(chips(160, 156, ['sloping', 'land', 'beside', 'river'], {'river'}, AC))
    o.append(T(700, 126, 'overlap 0', 14, 'end', MUT, True))
    o.append(T(700, 176, 'overlap 1 → chosen', 14, 'end', AC, True))
    # MFS baseline
    y = 220
    o.append(T(20, y, 'Most frequent sense baseline', 15, 'start', INK, True))
    o.append(R(20, y + 14, 30 * 12, 28, PANEL, L2, 4, 1.5)); o.append(T(20 + 15 * 12, y + 33, 'finance 30', 14, bold=True))
    o.append(R(20 + 30 * 12, y + 14, 10 * 12, 28, ACS, AC, 4, 1.5)); o.append(T(20 + 35 * 12, y + 33, 'river 10', 14, bold=True))
    o.append(T(520, y + 33, '→ always say finance', 14, 'start'))
    for i, (s, ok) in enumerate([('finance', 1), ('finance', 1), ('river', 0), ('river', 0)]):
        x = 20 + i * 130
        o.append(R(x, y + 58, 120, 32, LVS if ok else NXS, LV if ok else NX, 6, 1.5))
        o.append(T(x + 60, y + 79, f'{s} {"✓" if ok else "✗"}', 14, bold=True, fill=LV if ok else NX))
    o.append(T(560, y + 79, '2 of 4 = 50%', 15, 'start', INK, True))
    return y + 104, ''.join(o)
FIG[5] = (f5, 'Lesk compares the context with each gloss: river is the only shared word, and it is in the bank2 gloss, so the river-edge sense wins 1 to 0. The most frequent sense baseline always answers finance and gets 2 of the 4 test items right.',
          'Word chips for the context and the two bank glosses with river linked between the context and the bank2 gloss; below, a bar of 30 finance and 10 river training examples and four test items, two right and two wrong.')


# ---- 4.6 the roles of broke ----
def f6():
    cx, cy = 360, 170
    o = [T(20, 24, 'Ravi broke the window with a stone yesterday in Chennai.', 15, 'start', INK, True)]
    roles = [('Ravi', 'Agent', (110, 90), False), ('the window', 'Patient', (610, 90), False), ('a stone', 'Instrument', (110, 250), False),
             ('yesterday', 'Time', (610, 250), True), ('Chennai', 'Location', (360, 300), True)]
    for w, r, (x, y), opt in roles:
        o.append(L(cx, cy, x, y, L2 if opt else AC, 2 if opt else 2.5, '6 5' if opt else None))
    o.append(R(cx - 60, cy - 22, 120, 44, NXS, NX, 22, 2)); o.append(T(cx, cy + 6, 'broke', 17, bold=True))
    for w, r, (x, y), opt in roles:
        o.append(boxt(x - 80, y - 26, 160, 52, [r, w], PANEL if opt else ACS, L2 if opt else AC, 14, True))
    o.append(T(560, 330, 'dashed: optional adjuncts', 13, 'start', MUT))
    o.append(T(20, 360, '5 roles filled. The stone ate the cake breaks the animate-subject restriction of eat; The child ate the cake does not.', 13, 'start'))
    return 374, ''.join(o)
FIG[6] = (f6, 'The predicate broke and its five role fillers: Ravi is the Agent, the window the Patient, a stone the Instrument; yesterday (Time) and Chennai (Location) are optional adjuncts, drawn dashed.',
          'The verb broke in the centre with solid links to Ravi as Agent, the window as Patient and a stone as Instrument, and dashed links to yesterday as Time and Chennai as Location.')


# ---- 4.7 the RST tree for two sentences ----
def f7():
    o = []
    o.append(boxt(260, 20, 200, 44, ['Result', ], NXS, NX, 16, True))
    o.append(L(330, 64, 170, 120, AC, 3.5)); o.append(L(390, 64, 560, 120, L2, 1.5))
    u1, u2 = (40, 120, 260, 76), (420, 120, 280, 76)
    o.append(boxt(*u1, ['U1 (nucleus, cause)', 'Ravi missed the bus.'], ACS, AC, 14, True))
    o.append(boxt(*u2, ['U2 (satellite, result)', 'As a result, he reached', 'the office late.'], PANEL, AC, 14, True))
    # satellite arc pointing to nucleus
    o.append(arc(470, 196, 290, 196, -0.3, NX, 2.5, 'x'))
    # cohesion ties
    y = 240
    o.append(T(20, y, 'Cohesive ties that the reader can see', 15, 'start', INK, True))
    o.append(boxt(20, y + 14, 330, 52, ['reference: he → Ravi'], PANEL, AC, 14))
    o.append(boxt(370, y + 14, 330, 52, ['conjunction: As a result'], PANEL, AC, 14))
    o.append(T(20, y + 94, 'Delete As a result: readers still infer Result, but nothing in the text marks it any more.', 14, 'start', MUT))
    return y + 108, ''.join(o)
FIG[7] = (f7, 'The two-sentence text as one Result relation: U1, the cause, is the nucleus; U2, the result, is the satellite, with the arrow pointing from satellite to nucleus. The visible ties are the pronoun he and the cue As a result.',
          'An RST tree with root Result over two units: U1 Ravi missed the bus as nucleus and U2 As a result he reached the office late as satellite, with an arrow from U2 to U1; boxes below name the reference and conjunction ties.')


# ---- 4.8 three coreference chains ----
def f8():
    ms = [('Ravi₁', 0), ('Meera₁', 1), ('He', 0), ('Meera₂', 1), ('Ravi₂', 0), ('report', 2), ('She', 1), ('it', 2)]
    sent = [1, 1, 2, 3, 3, 3, 4, 4]
    cols = [(AC, ACS, 'Ravi'), (NX, NXS, 'Meera'), (LV, LVS, 'report')]
    xs = [60 + i * 86 for i in range(8)]
    yb = 170
    o = []
    for s in range(1, 5):
        idx = [i for i in range(8) if sent[i] == s]
        x1, x2 = xs[idx[0]] - 38, xs[idx[-1]] + 38
        o.append(R(x1, yb + 30, x2 - x1, 24, PANEL, LN, 4, 1))
        o.append(T((x1 + x2) / 2, yb + 47, f'sentence {s}', 12, fill=MUT))
    for c in range(3):
        idx = [i for i in range(8) if ms[i][1] == c]
        col = cols[c][0]
        for a, b in zip(idx, idx[1:]):
            h = 34 + (b - a) * 16 + c * 8
            o.append(f'<path d="M{xs[a]:.1f},{yb - 18:.1f} C{xs[a]:.1f},{yb - 18 - h:.1f} {xs[b]:.1f},{yb - 18 - h:.1f} {xs[b]:.1f},{yb - 18:.1f}" style="fill:none;stroke:{col};stroke-width:2.5"/>')
    for i, (m, c) in enumerate(ms):
        col, soft, _ = cols[c]
        w = tw(m, 14) + 18
        o.append(R(xs[i] - w / 2, yb - 18, w, 32, soft, col, 6, 2))
        o.append(T(xs[i], yb + 3, m, 14, bold=True))
    o.append(T(xs[2], 40, 'He agrees with Ravi, not the nearer Meera', 13, 'middle', AC, True))
    y = 250
    for c, (col, soft, name) in enumerate(cols):
        chain = ', '.join(m for m, cc in ms if cc == c)
        o.append(R(20 + c * 236, y, 224, 34, soft, col, 6, 1.5)); o.append(T(132 + c * 236, y + 22, chain, 14, bold=True))
    o.append(T(20, y + 66, 'gold links 2 + 2 + 1 = 5; system: 3 links, 2 right', 14, 'start'))
    o.append(T(20, y + 90, 'P = 2 ÷ 3 = 0.6667, R = 2 ÷ 5 = 0.4, F1 = 0.5', 15, 'start', INK, True))
    return y + 104, ''.join(o)
FIG[8] = (f8, 'The eight mentions in reading order, with each chain drawn in its own colour: Ravi, He and Ravi; Meera, Meera and She; report and it. The three chains hold 5 gold links.',
          'Eight mention boxes in reading order across four sentences, joined by arcs into three chains: Ravi1, He and Ravi2; Meera1, Meera2 and She; report and it; below, the scores P 0.6667, R 0.4 and F1 0.5.')


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d


def text_fixes(k):
    return TEXT.get(k, [])


def drop_sources():
    # university-hosted pages: the books name no universities
    return ['stanford.edu', 'icsi.berkeley.edu']
