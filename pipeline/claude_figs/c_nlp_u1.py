"""Claude's hand-drawn figures for c-nlp-u1 (NLP, unit 1: text processing and morphology), one per chapter, drawn from
each chapter's worked example, plus text fixes (wrong step reasons in 1.5 and 1.6) and the university-hosted sources to drop."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {}
TEXT = {}


# ---- 1.1 four strings, four ambiguity types ----
def f1():
    cards = [
        ('(a)', 'He sat by the bank.', 'lexical', 'one word, two senses', ['bank = river edge', 'bank = money place'], AC, ACS),
        ('(b)', 'Visiting relatives can be troublesome.', 'syntactic', 'one string, two structures', ['relatives who visit', 'the act of visiting them'], NX, NXS),
        ('(c)', 'Can you pass the salt?', 'pragmatic', 'clear words, unclear act', ['question: are you able?', 'request: please pass it'], LV, LVS),
        ('(d)', 'She saw the man with the binoculars.', 'syntactic', 'two places to attach', ['she used the binoculars', 'the man had them'], NX, NXS),
    ]
    o = []
    W, H = 340, 190
    for i, (tag, s, typ, why, reads, c, cs) in enumerate(cards):
        x = 14 + (i % 2) * (W + 12)
        y = 12 + (i // 2) * (H + 14)
        o.append(R(x, y, W, H, PANEL, c, 10, 2))
        o.append(T(x + 14, y + 26, tag, 14, 'start', MUT, True))
        o.append(T(x + 44, y + 26, s, 14 if len(s) < 34 else 13, 'start', INK, True))
        o.append(R(x + 14, y + 40, W - 28, 30, cs, c, 6, 1.5))
        o.append(T(x + W / 2, y + 60, f'{typ}: {why}', 14, fill=INK, bold=True))
        cx = x + W / 2
        for j, r in enumerate(reads):
            bx = x + 14 + j * (W - 28) / 2
            o.append(L(cx, y + 72, bx + (W - 28) / 4, y + 112, c, 2, arrow='n' if c == AC else ('x' if c == NX else 'l')))
            o.append(boxt(bx + 4, y + 118, (W - 28) / 2 - 8, 56, r.split(': ') if ': ' in r else [r], FIGBG, L2, 13))
    return 2 * H + 40, ''.join(o)
FIG[1] = (f1, 'The four strings of the worked example: each one splits into two readings, and the kind of split names the ambiguity. (a) is lexical, (b) and (d) are syntactic, (c) is pragmatic.',
          'Four cards. Each card shows one sentence that branches into two readings: bank as river edge or money place; visiting relatives as relatives who visit or the act of visiting; pass the salt as a question or a request; with the binoculars attached to saw or to the man.')


# ---- 1.2 the five layers for one sentence ----
def f2():
    rows = [  # top to bottom
        ('Pragmatics', 'utterance in context', 'a report of a past event; which bank? near Anna Salai'),
        ('Semantics', 'word and sentence meaning', 'bill = amount owed, bank = money place'),
        ('Syntax', 'phrase and sentence', '2 prepositional phrases: at the bank, near Anna Salai'),
        ('Morphology', 'morpheme', 'paid = pay + past: 2 morphemes'),
        ('Phonology', 'phoneme, syllable', 'Ravi: Ra-vi, 2 syllables'),
    ]
    o = [T(360, 26, 'Ravi paid the bill at the bank near Anna Salai.', 15, bold=True)]
    y0, h, gap = 44, 62, 8
    for i, (name, unit, note) in enumerate(rows):
        y = y0 + i * (h + gap)
        inset = (4 - i) * 0
        fill = ACS if i == 3 or i == 2 else PANEL
        o.append(R(60, y, 600, h, fill, AC, 8, 2))
        o.append(T(78, y + 26, name, 15, 'start', INK, True))
        o.append(T(78, y + 47, unit, 13, 'start', MUT))
        o.append(L(250, y + 10, 250, y + h - 10, LN, 1))
        o.append(T(268, y + 37, note, 14, 'start'))
    # arrow: lower layers feed higher ones
    yb, yt = y0 + 4 * (h + gap) + h - 6, y0 + 6
    o.append(L(36, yb, 36, yt, L2, 2.5, arrow='m'))
    o.append(f'<text x="24" y="{(yb + yt) / 2:.1f}" font-size="13" text-anchor="middle" transform="rotate(-90 24 {(yb + yt) / 2:.1f})" style="fill:var(--muted)">each layer uses the one below</text>')
    return y0 + 5 * (h + gap) + 4, ''.join(o)
FIG[2] = (f2, 'The worked sentence annotated layer by layer, from sound at the bottom to context at the top. The two counts asked for are shaded: paid has 2 morphemes, and the syntax has 2 prepositional phrases.',
          'Five stacked bands, phonology at the bottom to pragmatics at the top, each with its unit and the note for the sentence Ravi paid the bill at the bank near Anna Salai; an arrow up the side shows each layer uses the one below.')


# ---- 1.3 the DFA for ^baa+!$ and three traces ----
def f3():
    ys = 110
    xs = [90, 220, 350, 480, 620]
    o = []
    for i, x in enumerate(xs):
        o.append(state(x, ys, f'q{i}', accept=(i == 4), start=(i == 0)))
    for i, lab in enumerate(['b', 'a', 'a', '!']):
        o.append(edge((xs[i], ys), (xs[i + 1], ys), 24))
        o.append(Tb((xs[i] + xs[i + 1]) / 2, ys - 10, lab, 16, bold=True))
    o.append(loop(xs[3], ys, 24, AC, True))
    o.append(T(xs[3], ys - 66, 'a', 16, bold=True))
    o.append(T(xs[3], ys - 84, 'any extra a', 13, fill=MUT))
    o.append(T(xs[4], ys + 48, 'final', 13, fill=MUT))
    o.append(T(xs[0], ys + 48, 'start', 13, fill=MUT))
    # q2 has no ! arc
    o.append(L(xs[2], ys + 26, xs[2], ys + 62, NX, 2, '5 4'))
    o.append(T(xs[2], ys + 78, 'no ! arc from q2', 13, fill=NX, bold=True))
    # traces
    tr = [('baa!', 'q0 → q1 → q2 → q3 → q4', 'accepted', AC, ACS),
          ('baaa!', 'q0 → q1 → q2 → q3 → q3 → q4', 'accepted', AC, ACS),
          ('ba!', 'q0 → q1 → q2, then ! has nowhere to go', 'rejected', NX, NXS)]
    y = 214
    for s, path, res, c, cs in tr:
        o.append(R(40, y, 640, 40, cs, c, 6, 1.5))
        o.append(TM(60, y + 26, s, 16, 'start', INK, True))
        o.append(T(150, y + 26, path, 14, 'start'))
        o.append(T(664, y + 26, res, 14, 'end', c, True))
        y += 50
    return y + 4, ''.join(o)
FIG[3] = (f3, 'The automaton for ^baa+!$: b, a, a reach q3, the loop at q3 takes any extra a, and ! reaches the final state q4. baa! and baaa! end in q4; ba! stops at q2, which has no ! arc.',
          'Five states q0 to q4 in a row joined by b, a, a and exclamation mark, with a loop on a at q3 and q4 final; three trace bars below show baa and baaa accepted and ba rejected at q2.')
AFTER[3] = 3


# ---- 1.4 fourteen tokens, twelve types ----
def f4():
    toks = ['Dr.', 'Rao', 'paid', '₹1,250.50', 'on', '3/5/24', 'in', 'Chennai', ';', 'email', 'rao@site.in', 'in', 'Chennai', '.']
    prot = {0, 3, 5, 10}
    rep = {11, 12}
    o = [T(20, 24, 'Dr. Rao paid ₹1,250.50 on 3/5/24 in Chennai; email rao@site.in in Chennai.', 14, 'start', INK, True),
         T(20, 46, 'one sentence: the dots in Dr. and rao@site.in do not end it', 13, 'start', MUT)]
    x, y, rowh = 20, 66, 66
    for i, t in enumerate(toks):
        w = max(40, tw(t, 14) + 20)
        if x + w > 700:
            x, y = 20, y + rowh
        fill, st, dash = (ACS, AC, None) if i in prot else ((NXS, NX, '5 4') if i in rep else (PANEL, L2, None))
        o.append(R(x, y, w, 34, fill, st, 6, 2 if i in prot or i in rep else 1.5, dash))
        o.append(TM(x + w / 2, y + 22, t, 14))
        o.append(T(x + w / 2, y + 50, str(i + 1), 13, fill=MUT))
        x += w + 8
    y += rowh + 10
    o.append(R(20, y, 20, 16, ACS, AC, 4, 2)); o.append(T(48, y + 13, 'protected pattern, kept whole (4)', 13, 'start'))
    o.append(R(330, y, 20, 16, NXS, NX, 4, 2, '4 3')); o.append(T(358, y + 13, 'repeat of an earlier token (2)', 13, 'start'))
    y += 40
    o.append(boxt(20, y, 210, 44, ['1 sentence'], PANEL, AC, 15))
    o.append(boxt(255, y, 210, 44, ['14 tokens'], PANEL, AC, 15))
    o.append(boxt(490, y, 210, 44, ['14 − 2 = 12 types'], ACS, AC, 15))
    return y + 56, ''.join(o)
FIG[4] = (f4, 'The worked sentence cut into 14 tokens: the four protected patterns stay whole, and the second in and second Chennai are repeats, so the 14 tokens give 12 types.',
          'The sentence as fourteen numbered token boxes; Dr., the rupee amount, the date and the e-mail address are shaded as protected, and the second in and second Chennai are dashed as repeats; totals 1 sentence, 14 tokens, 12 types.')


# ---- 1.5 stop words, stems and lemmas ----
def f5():
    toks = ['cats', 'cat', 'ran', 'run', 'the', 'was', 'lies', 'lie']
    stems = ['cat', 'cat', 'ran', 'run', '', '', 'li', 'lie']
    lem = ['cat', 'cat', 'run', 'run', '', '', 'lie', 'lie']
    cut = ['1', '0', '0', '0', '', '', '2', '0']
    x0, cw = 120, 74
    rows = [('token', 44), ('stem', 108), ('lemma', 160), ('cut', 212)]
    o = []
    for lab, y in rows:
        o.append(T(x0 - 14, y + 24, lab, 14, 'end', MUT, True))
    for i, t in enumerate(toks):
        x = x0 + i * cw
        stop = t in ('the', 'was')
        o.append(R(x + 3, 44, cw - 6, 36, NXS if stop else PANEL, NX if stop else L2, 6, 1.5))
        o.append(TM(x + cw / 2, 68, t, 15, bold=not stop, fill=MUT if stop else INK))
        if stop:
            o.append(L(x + 12, 62, x + cw - 12, 62, NX, 2.5))
            o.append(T(x + cw / 2, 136, 'stop word,', 13, fill=NX))
            o.append(T(x + cw / 2, 154, 'dropped', 13, fill=NX))
            continue
        bad = stems[i] == 'li'
        o.append(L(x + cw / 2, 82, x + cw / 2, 104, L2, 1.5, arrow='m'))
        o.append(R(x + 3, 108, cw - 6, 36, NXS if bad else ACS, NX if bad else AC, 6, 2 if bad else 1.5))
        o.append(TM(x + cw / 2, 132, stems[i], 15))
        o.append(R(x + 3, 160, cw - 6, 36, PANEL, AC, 6, 1.5))
        o.append(TM(x + cw / 2, 184, lem[i], 15))
        o.append(T(x + cw / 2, 236, cut[i], 16, bold=cut[i] != '0', fill=INK if cut[i] != '0' else MUT))
    o.append(T(x0 + 6.5 * cw, 266, 'li is not a word', 13, fill=NX, bold=True))
    y = 290
    o.append(boxt(30, y, 210, 50, ['6 tokens survive'], PANEL, AC, 15))
    o.append(boxt(255, y, 210, 50, ['5 stems, 3 lemmas'], PANEL, AC, 15))
    o.append(boxt(480, y, 210, 50, ['1 + 2 = 3 characters cut'], ACS, AC, 15))
    return y + 62, ''.join(o)
FIG[5] = (f5, 'The eight tokens of the worked example: the and was are dropped as stop words, and the six survivors give 5 stems and 3 lemmas. Stemming cuts 3 characters in all, and turns lies into li, which is not a word.',
          'Eight token columns with rows for stem, lemma and characters cut; the and was are struck out as stop words; cats loses 1 character, lies loses 2 and becomes li, marked as not a word.')


# ---- 1.6 the plural transducer ----
def f6():
    q0, q1, q3, q2 = (110, 190), (340, 80), (340, 300), (580, 190)
    o = []
    o.append(edge(q0, q1, 26, 0, AC, 2))
    o.append(edge(q1, q2, 26, 0, AC, 2))
    o.append(edge(q0, q3, 26, 0, NX, 3.5, 'x'))
    o.append(edge(q3, q2, 26, 0, NX, 3.5, 'x'))
    o.append(edge(q0, q2, 26, 0, L2, 2, 'm', '7 5'))
    o.append(Tb(180, 120, 'cat : cat', 15, bold=True))
    o.append(Tb(500, 126, 'ε : s', 15, bold=True))
    o.append(Tb(180, 268, 'fox : fox', 15, bold=True, fill=NX))
    o.append(Tb(500, 262, 'ε : es', 15, bold=True, fill=NX))
    o.append(Tb(345, 183, 'goose : geese', 15, bold=True))
    o.append(T(345, 206, 'irregular, stored whole', 13, fill=MUT))
    o.append(state(*q0, 'q0', start=True, r=26))
    o.append(state(*q1, 'q1', r=26))
    o.append(state(*q3, 'q3', r=26))
    o.append(state(*q2, 'q2', accept=True, r=26))
    o.append(T(q0[0], q0[1] + 46, 'start', 13, fill=MUT))
    o.append(T(q2[0], q2[1] + 46, 'final', 13, fill=MUT))
    o.append(T(630, 40, 'label = upper : lower', 13, 'end', MUT))
    y = 352
    o.append(R(20, y, 330, 58, NXS, NX, 8, 1.5))
    o.append(T(36, y + 24, 'Generate: fox', 14, 'start', INK, True))
    o.append(T(36, y + 45, 'q0 → q3 → q2 writes fox + es = foxes', 14, 'start'))
    o.append(R(370, y, 330, 58, ACS, AC, 8, 1.5))
    o.append(T(386, y + 24, 'Analyse: cats (read lower : upper)', 14, 'start', INK, True))
    o.append(T(386, y + 45, 'q0 → q1 → q2 gives cat + plural', 14, 'start'))
    return y + 68, ''.join(o)
FIG[6] = (f6, 'The transducer of the worked example: 4 states, 5 arcs, 3 paths from q0 to the final state q2. The thick path generates foxes from fox; the dashed arc stores goose : geese as one irregular piece.',
          'A transducer with start q0 and final q2: cat:cat then epsilon:s through q1, fox:fox then epsilon:es through q3 drawn thick, and one dashed arc goose:geese straight from q0 to q2; boxes below show generating foxes and analysing cats.')


# ---- 1.7 edit distance table cat -> cart ----
def f7():
    s, t = 'cat', 'cart'
    D = [[0, 1, 2, 3, 4], [1, 0, 1, 2, 3], [2, 1, 0, 1, 2], [3, 2, 1, 1, 1]]
    path = {(0, 0), (1, 1), (2, 2), (2, 3), (3, 4)}
    x0, y0, c = 150, 60, 64
    o = [T(x0 + 2.5 * c + c / 2, 24, 'target: cart (across)', 14, fill=MUT), ]
    o.append(f'<text x="40" y="{y0 + 2.5 * c:.1f}" font-size="14" text-anchor="middle" transform="rotate(-90 40 {y0 + 2.5 * c:.1f})" style="fill:var(--muted)">source: cat (down)</text>')
    for j, ch in enumerate('ε' + t):
        o.append(T(x0 + (j + 1) * c + c / 2, y0 + 26, ch, 16, bold=True))
    for i, ch in enumerate('ε' + s):
        o.append(T(x0 + c / 2, y0 + (i + 1) * c + c / 2 + 6, ch, 16, bold=True))
    for i in range(4):
        for j in range(5):
            x, y = x0 + (j + 1) * c, y0 + (i + 1) * c
            on = (i, j) in path
            fill = ACS if on else PANEL
            if (i, j) == (3, 4): fill = NXS
            o.append(R(x + 2, y + 2, c - 4, c - 4, fill, AC if on else LN, 4, 2 if on else 1))
            o.append(T(x + c / 2, y + c / 2 + 7, str(D[i][j]), 18, bold=on))
    # backtrace arrows (from the answer back to the start)
    ctr = lambda i, j: (x0 + (j + 1) * c + c / 2, y0 + (i + 1) * c + c / 2)
    for (a, b), lab in [(((3, 4), (2, 3)), None), (((2, 3), (2, 2)), None), (((2, 2), (1, 1)), None), (((1, 1), (0, 0)), None)]:
        (x1, y1), (x2, y2) = ctr(*a), ctr(*b)
        f = 0.36
        o.append(L(x1 + (x2 - x1) * f, y1 + (y2 - y1) * f, x2 - (x2 - x1) * f, y2 - (y2 - y1) * f, NX, 2, arrow='x'))
    o.append(T(x0 + 5 * c + c + 8, y0 + 4 * c + c / 2 + 6, 'distance 1', 14, 'start', NX, True))
    y = y0 + 5 * c + 26
    al = [('c', 'c', 'copy'), ('a', 'a', 'copy'), ('–', 'r', 'insert r'), ('t', 't', 'copy')]
    o.append(T(130, y + 22, 'cat', 15, 'end', MUT)); o.append(T(130, y + 56, 'cart', 15, 'end', MUT))
    for k, (a, b, op) in enumerate(al):
        x = 150 + k * 130
        ins = op != 'copy'
        o.append(R(x, y, 110, 68, NXS if ins else PANEL, NX if ins else L2, 6, 2 if ins else 1.2))
        o.append(TM(x + 55, y + 24, a, 17, bold=True)); o.append(TM(x + 55, y + 56, b, 17, bold=True))
        o.append(T(x + 55, y + 90, op + (' (+1)' if ins else ' (+0)'), 13, fill=NX if ins else MUT))
    return y + 104, ''.join(o)
FIG[7] = (f7, 'The prefix table from cat to cart. The shaded cells are the backtrace from the bottom-right answer 1: copy c, copy a, insert r, copy t, so only the insertion costs anything.',
          'A four by five table with source cat down and target cart across; shaded cells and arrows trace back from the bottom-right value 1 through copy t, insert r, copy a and copy c; below, the alignment of cat and cart with r inserted.')
AFTER[7] = 2


# ---- 1.8 a corpus before and after cleaning ----
def f8():
    o = []
    o.append(boxt(20, 20, 200, 60, ['400 pages', '× 650 words'], PANEL, L2, 15))
    o.append(L(224, 50, 266, 50, AC, 2.5, arrow='n'))
    o.append(boxt(270, 20, 200, 60, ['260,000 tokens', '× 6 characters'], PANEL, AC, 15))
    o.append(L(474, 50, 516, 50, AC, 2.5, arrow='n'))
    o.append(boxt(520, 20, 180, 60, ['1,560,000 chars', '= 1.56 MB'], ACS, AC, 15))
    # bars
    x0, W = 120, 560
    y = 130
    o.append(T(x0 - 12, y + 26, 'raw', 15, 'end', INK, True))
    o.append(R(x0, y, W, 40, ACS, AC, 4, 1.5))
    o.append(T(x0 + W / 2, y + 26, '260,000 tokens · 1.56 MB', 15, bold=True))
    y2 = 220
    o.append(T(x0 - 12, y2 + 26, 'cleaned', 15, 'end', INK, True))
    o.append(R(x0, y2, W * 0.8, 40, ACS, AC, 4, 1.5))
    o.append(R(x0 + W * 0.8, y2, W * 0.2, 40, NXS, NX, 4, 1.5, '5 4'))
    o.append(T(x0 + W * 0.4, y2 + 26, '208,000 tokens · 1.248 MB', 15, bold=True))
    o.append(T(x0 + W * 0.9, y2 + 26, '20% cut', 14, fill=NX, bold=True))
    o.append(L(x0 + W * 0.8, y + 44, x0 + W * 0.8, y2 - 4, L2, 1.5, '4 4'))
    o.append(T(x0 + W * 0.9, y2 - 12, 'menus, footers', 13, fill=MUT))
    o.append(T(x0, 300, 'kept = 0.80 × 260,000 = 208,000 tokens; 208,000 × 6 = 1,248,000 characters = 1.248 MB', 14, 'start'))
    return 316, ''.join(o)
FIG[8] = (f8, 'The worked example end to end: 400 pages of 650 words give 260,000 tokens and 1.56 MB; cutting the 20 percent boilerplate leaves 208,000 tokens and 1.248 MB.',
          'A chain from 400 pages times 650 words to 260,000 tokens to 1.56 megabytes, then two bars: the raw corpus, and the cleaned corpus 80 percent as long with the 20 percent boilerplate cut off dashed.')


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d


# wrong reasons in worked steps and answers
TEXT[5] = [
    ('cats → cat: the s follows the vowel a, so it is deleted, 1 character removed.',
     'cats → cat: the part before the s, cat, contains the vowel a, which is not directly before the s, so the s is deleted, 1 character removed.'),
    ('lie keeps its final e because its measure is 0, not greater than 1, so 0 removed.',
     'lie has no final s and does not end in ies, so step 1a leaves it as it is, 0 removed.'),
]
TEXT[6] = [
    ('Analysing cats runs from q2 in reverse: arc q1→q2 becomes s:ε, then arc q0→q1 becomes cat:cat; the machine reaches q0 and returns cat plus plural.',
     'Analysing cats uses the same machine with each label read the other way round (lower : upper), still from q0: cat:cat reads cat and moves to q1, then s:ε reads s and reaches the final state q2; the path taken is the plural path, so the machine returns cat plus plural.'),
    ('In the figure, trace the path for goose and the reverse path for cats.',
     'In the figure, trace the generation path for goose and the analysis path for cats.'),
    ('cats runs q2→q1 by reversing ε:s to s:ε, then q1→q0 by reversing cat:cat to cat:cat; the result is cat plus plural.',
     'For cats the labels are read lower : upper from q0: cat:cat takes q0→q1, then s:ε takes q1→q2, the final state; the result is cat plus plural.'),
]


def text_fixes(k):
    return TEXT.get(k, [])


def drop_sources():
    # university-hosted pages: the books name no universities
    return ['stanford.edu']
