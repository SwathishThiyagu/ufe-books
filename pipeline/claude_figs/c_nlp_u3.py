"""Claude's hand-drawn figures for c-nlp-u3 (NLP, unit 3: syntax and parsing), one per chapter, drawn from each chapter's
worked example, plus the sentences in 3.1 that described the old tree, the RIGHT-ARC definition in 3.6 (it pushed the
dependent, which is arc-eager and leaves the parse unable to finish) and the university-hosted sources to drop."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {}
TEXT = {}


def tree(nodes, edges, hl=(), size=15, leaf=()):
    """nodes: {id: (x, y, label)}; edges: [(a, b)]; hl: ids drawn shaded; leaf: ids drawn as plain words"""
    o = []
    for a, b in edges:
        (x1, y1, _), (x2, y2, _) = nodes[a], nodes[b]
        o.append(L(x1, y1 + 16, x2, y2 - 16, L2, 1.6))
    for i, (x, y, lab) in nodes.items():
        if i in leaf:
            o.append(TM(x, y + 5, lab, size, bold=True))
            continue
        w = tw(lab, size - 1) + 22
        o.append(R(x - w / 2, y - 15, w, 30, ACS if i in hl else PANEL, AC, 6, 1.6))
        o.append(T(x, y + 5, lab, size - 1, bold=True))
    return ''.join(o)


# ---- 3.1 derivation tree for "the boy ate a cake" and the count 6 x 12 = 72 ----
def f1():
    N = {'S': (360, 34, 'S → NP VP'), 'NP1': (170, 104, 'NP → Det N'), 'VP': (520, 104, 'VP → V NP'),
         'D1': (100, 174, 'Det → the'), 'N1': (240, 174, 'N → boy'), 'V': (420, 174, 'V → ate'), 'NP2': (600, 174, 'NP → Det N'),
         'D2': (530, 244, 'Det → a'), 'N2': (665, 244, 'N → cake'),
         'w1': (100, 236, 'the'), 'w2': (240, 236, 'boy'), 'w3': (420, 236, 'ate'), 'w4': (530, 306, 'a'), 'w5': (665, 306, 'cake')}
    E = [('S', 'NP1'), ('S', 'VP'), ('NP1', 'D1'), ('NP1', 'N1'), ('VP', 'V'), ('VP', 'NP2'), ('NP2', 'D2'), ('NP2', 'N2'),
         ('D1', 'w1'), ('N1', 'w2'), ('V', 'w3'), ('D2', 'w4'), ('N2', 'w5')]
    o = [tree(N, E, hl=('NP1', 'NP2'), leaf=('w1', 'w2', 'w3', 'w4', 'w5'))]
    o.append(T(20, 344, 'yield, left to right: the boy ate a cake', 14, 'start', MUT))
    y = 370
    o.append(boxt(20, y, 210, 56, ['NP: 2 Det × 3 N', '= 6 strings'], ACS, AC, 14))
    o.append(boxt(255, y, 210, 56, ['VP: 2 V × 6 NP', '= 12 strings'], PANEL, AC, 14))
    o.append(boxt(490, y, 210, 56, ['S: 6 NP × 12 VP', '= 72 sentences'], PANEL, AC, 14, True))
    return y + 68, ''.join(o)
FIG[1] = (f1, 'The parse tree of the leftmost derivation: every box is a nonterminal with the rule that rewrote it, and the leaves read left to right give the boy ate a cake. Counting choices, 6 noun phrases and 12 verb phrases give 72 sentences.',
          'A parse tree with S rewritten as NP VP, the first NP as Det N over the boy, the VP as V NP over ate a cake; below, boxes count 6 noun phrases, 12 verb phrases and 72 sentences.')
TEXT[1] = [
    ('the tree in the figure has yield “the boy ate the cake”.', 'the tree in the figure has yield “the boy ate a cake”.'),
    ('Nine steps, ten strings; the parse tree is the figure with a in place of the second the.', 'Nine steps, ten strings; the figure draws the parse tree of this derivation.'),
]


# ---- 3.2 binarising the one long rule ----
def f2():
    o = [T(180, 26, 'Before: 10 rules', 15, bold=True), T(540, 26, 'After (CNF): 11 rules', 15, bold=True)]
    a = {'S': (180, 70, 'S'), 'NP': (80, 170, 'NP'), 'VP': (180, 170, 'VP'), 'PP': (280, 170, 'PP')}
    o.append(tree(a, [('S', 'NP'), ('S', 'VP'), ('S', 'PP')]))
    o.append(boxt(70, 214, 220, 36, ['S → NP VP PP: 3 symbols'], NXS, NX, 14))
    b = {'S': (540, 70, 'S'), 'NP': (450, 170, 'NP'), 'X': (630, 140, 'X1'), 'VP': (580, 210, 'VP'), 'PP': (680, 210, 'PP')}
    o.append(tree(b, [('S', 'NP'), ('S', 'X'), ('X', 'VP'), ('X', 'PP')], hl=('X',)))
    o.append(L(320, 140, 400, 140, AC, 2.5, arrow='n'))
    o.append(T(360, 128, 'binarise', 13, fill=MUT))
    o.append(boxt(420, 250, 260, 56, ['S → NP X1', 'X1 → VP PP'], ACS, AC, 14))
    o.append(T(20, 340, 'Order kept: NP, then VP, then PP, so every sentence keeps the same words in the same order.', 14, 'start'))
    o.append(T(20, 364, 'Rules: 10 − 1 + 2 = 11. The other nine rules are already binary or lexical.', 14, 'start'))
    return 380, ''.join(o)
FIG[2] = (f2, 'The only rule with three symbols on its right, S → NP VP PP, becomes S → NP X1 and X1 → VP PP. The children stay in the order NP, VP, PP, so the grammar grows from 10 to 11 rules and makes exactly the same sentences.',
          'Left, S with three children NP, VP, PP; right, after binarising, S with children NP and a new node X1 whose children are VP and PP; rule counts 10 before and 11 after.')


# ---- 3.3 the CYK table ----
def f3():
    words = ['the', 'boy', 'ate', 'the', 'cake']
    cell = {(1, 1): 'Det', (2, 2): 'N', (3, 3): 'V', (4, 4): 'Det', (5, 5): 'N', (1, 2): 'NP', (4, 5): 'NP', (3, 5): 'VP', (1, 5): 'S'}
    x0, y0, c = 120, 50, 100
    o = []
    # row = span length (1 at bottom), column = start i
    def pos(i, j):
        L_ = j - i + 1
        return x0 + (i - 1) * c, y0 + (5 - L_) * 62
    for L_ in range(1, 6):
        o.append(T(x0 - 14, y0 + (5 - L_) * 62 + 36, f'length {L_}', 13, 'end', MUT))
        for i in range(1, 7 - L_):
            j = i + L_ - 1
            x, y = pos(i, j)
            v = cell.get((i, j), '')
            hl = (i, j) == (1, 5)
            src = (i, j) in ((1, 2), (3, 5))
            fill = NXS if hl else (ACS if src else (PANEL if v else FIGBG))
            o.append(R(x + 3, y + 3, c - 6, 56, fill, NX if hl else (AC if v else LN), 5, 2 if (hl or src) else 1))
            if v: o.append(T(x + c / 2, y + 30, v, 16, bold=True))
            o.append(T(x + c / 2, y + 50, f'({i},{j})', 12, fill=MUT))
    for i, w in enumerate(words):
        o.append(TM(x0 + i * c + c / 2, y0 + 5 * 62 + 20, w, 15, bold=True))
    xs, ys = pos(1, 5)
    o.append(T(xs + c + 12, ys + 26, 'S from NP (1,2) + VP (3,5), split k = 2', 14, 'start', NX, True))
    o.append(T(xs + c + 12, ys + 46, 'S in (1,5): the sentence is accepted', 14, 'start'))
    o.append(T(20, y0 + 5 * 62 + 56, '15 cells; split checks 4 + 6 + 6 + 4 = 20 = 5·4·6/6', 14, 'start', MUT))
    return y0 + 5 * 62 + 70, ''.join(o)
FIG[3] = (f3, 'The CYK table for the boy ate the cake, one row per span length. NP fills (1,2) and (4,5), VP fills (3,5), and S in the top cell (1,5), built from (1,2) and (3,5) at split k = 2, means the sentence is accepted.',
          'A triangular table with length-1 cells Det, N, V, Det, N above the five words, NP at (1,2) and (4,5), VP at (3,5), empty cells elsewhere, and S at the top cell (1,5) highlighted.')
AFTER[3] = 2


# ---- 3.4 two attachments, two probabilities ----
def f4():
    o = []
    def parse(x, title, nodes, edges, hl, note, c, cs):
        r = [T(x + 170, 24, title, 15, bold=True)]
        r.append(tree(nodes, edges, hl=hl, size=14))
        r.append(boxt(x + 30, 290, 280, 52, note, cs, c, 14, True))
        return ''.join(r)
    A = {'VP': (170, 60, 'VP'), 'V': (60, 130, 'V: saw'), 'NP': (220, 130, 'NP'), 'NP2': (160, 200, 'the man'), 'PP': (280, 200, 'PP'),
         'w': (280, 256, 'with the telescope')}
    o.append(parse(0, 'Parse A: the man has it', A, [('VP', 'V'), ('VP', 'NP'), ('NP', 'NP2'), ('NP', 'PP'), ('PP', 'w')], ('NP',),
                   ['uses NP → NP PP (0.2)', 'P(A) = 0.2 K'], L2, PANEL))
    B = {'VP': (530, 60, 'VP'), 'VP2': (450, 130, 'VP'), 'PP': (630, 130, 'PP'), 'V': (400, 200, 'V: saw'), 'NP': (510, 200, 'the man'),
         'w': (630, 196, 'with the telescope')}
    o.append(parse(360, 'Parse B: saw with it', B, [('VP', 'VP2'), ('VP', 'PP'), ('VP2', 'V'), ('VP2', 'NP'), ('PP', 'w')], ('VP',),
                   ['uses VP → VP PP (0.6)', 'P(B) = 0.6 K'], NX, NXS))
    o.append(T(360, 376, 'K = the product of the rules both trees share. 0.6 K ÷ 0.2 K = 3, so the PCFG picks Parse B.', 14))
    return 392, ''.join(o)
FIG[4] = (f4, 'I saw the man with the telescope has two legal trees that differ in one rule. Attaching the PP to the noun phrase scores 0.2K, attaching it to the verb phrase scores 0.6K, so the PCFG picks Parse B, three times as probable.',
          'Two verb-phrase trees side by side: in Parse A the PP with the telescope hangs under the NP the man and the tree scores 0.2 K; in Parse B it hangs under the VP and the tree scores 0.6 K.')
AFTER[4] = 3


# ---- 3.5 a tree with rule probabilities ----
def f5():
    N = {'S': (360, 34, 'S → NP VP  1.0'), 'NP1': (170, 104, 'NP → Det N  0.5'), 'VP': (520, 104, 'VP → V NP  0.6'),
         'D1': (95, 174, 'Det → the  1.0'), 'N1': (250, 174, 'N → boy  0.3'), 'V': (415, 174, 'V → ate  0.4'), 'NP2': (600, 174, 'NP → Det N  0.5'),
         'D2': (525, 244, 'Det → the  1.0'), 'N2': (665, 244, 'N → cake  0.2'),
         'w1': (95, 236, 'the'), 'w2': (250, 236, 'boy'), 'w3': (415, 236, 'ate'), 'w4': (525, 306, 'the'), 'w5': (665, 306, 'cake')}
    E = [('S', 'NP1'), ('S', 'VP'), ('NP1', 'D1'), ('NP1', 'N1'), ('VP', 'V'), ('VP', 'NP2'), ('NP2', 'D2'), ('NP2', 'N2'),
         ('D1', 'w1'), ('N1', 'w2'), ('V', 'w3'), ('D2', 'w4'), ('N2', 'w5')]
    o = [tree(N, E, hl=('NP1', 'NP2'), leaf=('w1', 'w2', 'w3', 'w4', 'w5'), size=14)]
    y = 340
    o.append(T(20, y, 'P(tree) = 1.0 × 0.5 × 1.0 × 0.3 × 0.6 × 0.4 × 0.5 × 1.0 × 0.2', 15, 'start', INK, True))
    o.append(T(20, y + 26, '= 0.0036  (nine nodes; NP → Det N is used twice, so 0.5 appears twice)', 15, 'start', AC, True))
    o.append(T(20, y + 52, 'One tree only, so the sentence probability is also 0.0036.', 14, 'start', MUT))
    return y + 66, ''.join(o)
FIG[5] = (f5, 'Each of the nine nodes carries its rule probability. Multiplying them gives 0.0036; NP → Det N is used twice, so 0.5 enters the product twice.',
          'A parse tree of the boy ate the cake with each internal node labelled with its rule and probability, and below it the nine probabilities multiplied to 0.0036.')


# ---- 3.6 gold arcs, one wrong head, UAS and LAS ----
def f6():
    words = ['The', 'boy', 'ate', 'the', 'cake', 'quickly']
    xs = [110 + i * 100 for i in range(6)]
    yw = 200
    o = []
    for x, w in zip(xs, words):
        o.append(TM(x, yw, w, 16, bold=True))
    o.append(T(30, yw, 'ROOT', 13, 'middle', MUT, True))
    def harc(i, j, lab, c=AC, dash=None, up=True, hgt=None, w=2, arrow='n'):
        x1, x2 = (30 if i is None else xs[i]), xs[j]
        y = yw - 22 if up else yw + 12
        h = hgt or (24 + abs(x2 - x1) * 0.28)
        cy = y - h if up else y + h
        d = f';stroke-dasharray:{dash}' if dash else ''
        mx = (x1 + x2) / 2
        p = f'<path d="M{x1:.1f},{y:.1f} C{x1:.1f},{cy:.1f} {x2:.1f},{cy:.1f} {x2:.1f},{y:.1f}" style="fill:none;stroke:{c};stroke-width:{w}{d}" marker-end="url(#ar-UID-{arrow})"/>'
        ty = y - h * 0.75 - 4 if up else y + h * 0.75 + 14
        return p + Tb(mx, ty, lab, 13, fill=c if c != AC else INK, bold=True)
    o.append(harc(2, 1, 'nsubj'))
    o.append(harc(1, 0, 'det'))
    o.append(harc(2, 4, 'dobj'))
    o.append(harc(4, 3, 'det'))
    o.append(harc(2, 5, 'advmod (gold)', AC, hgt=140))
    o.append(harc(None, 2, 'root', AC, hgt=175))
    # system's wrong arc, drawn below the words
    o.append(harc(4, 5, 'advmod (system: wrong head)', NX, '6 4', up=False, w=2.5, arrow='x'))
    y = 296
    o.append(T(20, y, '6 gold arcs (5 between words + 1 to ROOT). The system gets 5 right.', 14, 'start'))
    o.append(boxt(20, y + 16, 330, 44, ['UAS = 5 ÷ 6 = 0.8333'], ACS, AC, 15, True))
    o.append(boxt(370, y + 16, 330, 44, ['LAS = 5 ÷ 6 = 0.8333'], ACS, AC, 15, True))
    return y + 72, ''.join(o)
FIG[6] = (f6, 'The gold tree for The boy ate the cake quickly has 6 arcs, counting the one from ROOT. The system hangs quickly on cake instead of ate (dashed, below), so 5 of 6 arcs are right and UAS = LAS = 0.8333.',
          'The six words with gold dependency arcs drawn above them: ate to boy nsubj, boy to The det, ate to cake dobj, cake to the det, ate to quickly advmod and ROOT to ate; below, a dashed system arc from cake to quickly marked as the wrong head.')


# ---- 3.7 IOB chunk tags, labelled and unlabelled scores ----
def f7():
    words = ['The', 'boy', 'ate', 'the', 'cake', 'in', 'the', 'park']
    gold = ['B-NP', 'I-NP', 'B-VP', 'B-NP', 'I-NP', 'B-PP', 'I-PP', 'I-PP']
    pred = ['B-NP', 'I-NP', 'B-VP', 'B-NP', 'I-NP', 'B-NP', 'I-NP', 'I-NP']
    x0, cw = 100, 76
    o = [T(x0 - 12, 40, 'word', 13, 'end', MUT), T(x0 - 12, 90, 'gold', 13, 'end', MUT), T(x0 - 12, 170, 'system', 13, 'end', MUT)]
    for i, w in enumerate(words):
        o.append(TM(x0 + i * cw + cw / 2, 40, w, 15, bold=True))
    def chunks(y, spans, c_bad=None):
        r = []
        for a, b, lab, ok in spans:
            x = x0 + a * cw + 4; w = (b - a + 1) * cw - 8
            r.append(R(x, y, w, 52, PANEL if ok else NXS, AC if ok else NX, 6, 1.8))
            r.append(T(x + w / 2, y + 44, lab, 13, bold=True, fill=AC if ok else NX))
        return ''.join(r)
    o.append(chunks(68, [(0, 1, 'NP', True), (2, 2, 'VP', True), (3, 4, 'NP', True), (5, 7, 'PP', True)]))
    o.append(chunks(148, [(0, 1, 'NP', True), (2, 2, 'VP', True), (3, 4, 'NP', True), (5, 7, 'NP: wrong label', False)]))
    # re-draw the tag text on top of the boxes
    for i in range(8):
        o.append(T(x0 + i * cw + cw / 2, 90, gold[i], 13, bold=gold[i].startswith('B')))
        o.append(T(x0 + i * cw + cw / 2, 170, pred[i], 13, bold=pred[i].startswith('B'), fill=NX if pred[i] != gold[i] else INK))
    y = 228
    o.append(boxt(20, y, 330, 60, ['labelled: 3 of 4 chunks match', 'P = R = F1 = 0.75'], NXS, NX, 14, True))
    o.append(boxt(370, y, 330, 60, ['unlabelled: 4 of 4 spans match', 'P = R = F1 = 1.0'], ACS, AC, 14, True))
    return y + 72, ''.join(o)
FIG[7] = (f7, 'The IOB tag string for one sentence, gold above and system below. Every chunk boundary is right, but the last chunk is labelled NP instead of PP, so labelled scores fall to 0.75 while unlabelled scores stay at 1.0.',
          'The words The boy ate the cake in the park with gold IOB tags grouped into NP, VP, NP and PP chunks, and system tags grouped the same way except that the last chunk is labelled NP and marked wrong; labelled scores 0.75, unlabelled 1.0.')


# ---- 3.8 the shift-reduce run, stack after every action ----
def f8():
    acts = [('SHIFT', ['Det(the)']), ('SHIFT', ['Det(the)', 'N(boy)']), ('RED-R', ['NP(boy)']), ('SHIFT', ['NP(boy)', 'V(ate)']),
            ('SHIFT', ['NP(boy)', 'V(ate)', 'Det(the)']), ('SHIFT', ['NP(boy)', 'V(ate)', 'Det(the)', 'N(cake)']),
            ('RED-R', ['NP(boy)', 'V(ate)', 'NP(cake)']), ('RED-L', ['NP(boy)', 'VP(ate)']), ('RED-R', ['S(ate)']), ('FINISH', ['S(ate)'])]
    cw, x0, base = 70, 10, 220
    o = [T(20, 22, 'Stack after each action (top of stack at the top)', 14, 'start', MUT)]
    for i, (a, st) in enumerate(acts):
        x = x0 + i * cw
        red = a.startswith('RED')
        hl = a == 'RED-L'
        o.append(T(x + cw / 2, base + 26, str(i + 1), 13, fill=MUT))
        o.append(T(x + cw / 2, base + 46, a, 12, bold=True, fill=NX if hl else (AC if red else INK)))
        for j, s in enumerate(st):
            y = base - 8 - (j + 1) * 40
            new = j == len(st) - 1 and a != 'FINISH'
            fill = NXS if (hl and new) else (ACS if new else PANEL)
            o.append(R(x + 3, y, cw - 6, 34, fill, NX if (hl and new) else (AC if new else L2), 5, 1.5))
            o.append(T(x + cw / 2, y + 22, s, 11.5 if len(s) > 7 else 13, bold=new))
        o.append(L(x + 2, base - 4, x + cw - 2, base - 4, L2, 2))
    o.append(T(20, base + 76, 'RED-R / RED-L: binary reduce taking the head from the right / left child.', 13, 'start', MUT))
    o.append(T(20, base + 98, 'Step 8 takes its head from V(ate). 5 shifts + 4 reductions + 1 finish = 10 actions.', 14, 'start', INK, True))
    return base + 112, ''.join(o)
FIG[8] = (f8, 'The stack after each of the 10 actions for the boy ate the cake. The highlighted reduce builds VP(ate) with its head from the left child V(ate); the next reduce leaves S(ate), ready for FINISH.',
          'Ten columns, one per action, each showing the stack as a pile of boxes: shifts add Det(the), N(boy), V(ate) and so on, reductions merge them into NP(boy), NP(cake), VP(ate) and finally S(ate).')


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d


# RIGHT-ARC as written pushed the dependent (arc-eager without REDUCE), so the stated stop condition could never be met
TEXT[6] = [
    ('RIGHT-ARC(l): add the arc i → j with label l, then push j on the stack.',
     'RIGHT-ARC(l): add the arc i → j with label l, remove j from the buffer, then pop i and put it back at the front of the buffer so it can take more dependents. Allowed only when j already has all its own dependents.'),
    ('RIGHT-ARC makes the stack top the head of the first buffer word and pushes that buffer word on the stack.',
     'RIGHT-ARC makes the stack top the head of the first buffer word, removes that buffer word, and moves the stack top back to the front of the buffer.'),
]


def text_fixes(k):
    return TEXT.get(k, [])


def drop_sources():
    # university-hosted pages: the books name no universities
    return ['stanford.edu']
