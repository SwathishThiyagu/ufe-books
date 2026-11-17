"""Claude's hand-drawn figures for c-nlp-u2 (NLP, unit 2: language models and sequence labelling), one per chapter,
drawn from each chapter's worked example, plus the sentence in 2.3 that described the old figure and the
university-hosted sources to drop."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {}
TEXT = {}


# ---- 2.1 counting bigrams after cat ----
def f1():
    toks = ['⟨s⟩', 'the', 'cat', 'sat', 'on', 'the', 'mat', 'the', 'cat', 'sat', '⟨/s⟩']
    o = [T(20, 24, 'The corpus with boundary markers: 11 tokens, 10 bigrams', 14, 'start', MUT)]
    x, y, w = 20, 40, 58
    pos = []
    for i, t in enumerate(toks):
        isc = t == 'cat'
        nxt = i > 0 and toks[i - 1] == 'cat'
        fill, st = (ACS, AC) if isc else ((LVS, LV) if nxt else (PANEL, L2))
        o.append(R(x + i * 62, y, w, 36, fill, st, 6, 2 if isc or nxt else 1.2))
        o.append(TM(x + i * 62 + w / 2, y + 23, t, 14, bold=isc))
        pos.append(x + i * 62 + w / 2)
    for i in (2, 8):
        o.append(arc(pos[i] + 8, y + 40, pos[i + 1] - 8, y + 40, -0.35, LV, 2, 'l'))
    o.append(T(pos[2], y + 74, 'cat sat', 13, fill=LV, bold=True))
    o.append(T(pos[8], y + 74, 'cat sat', 13, fill=LV, bold=True))
    # the estimate
    cx, cy = 150, 250
    o.append(boxt(cx - 80, cy - 30, 160, 60, ['context cat', 'c(cat) = 2'], ACS, AC, 15, True))
    o.append(L(cx + 82, cy - 10, 420, cy - 50, LV, 3, arrow='l'))
    o.append(L(cx + 82, cy + 10, 420, cy + 50, L2, 2, '7 5', arrow='m'))
    o.append(boxt(424, cy - 80, 270, 58, ['P(sat | cat) = 2 ÷ 2 = 1.00', 'c(cat sat) = 2'], LVS, LV, 15, True))
    o.append(boxt(424, cy + 22, 270, 58, ['P(on | cat) = 0 ÷ 2 = 0.00', 'c(cat on) = 0: never seen'], PANEL, L2, 15, True, dash='6 4'))
    return cy + 96, ''.join(o)
FIG[1] = (f1, 'cat appears twice in the corpus and is followed by sat both times, so P(sat | cat) = 2 ÷ 2 = 1.00. cat on never occurs, so P(on | cat) = 0, the zero that smoothing must repair.',
          'The eleven-token corpus with both cat tokens shaded and arrows to the sat that follows each; below, the context cat with count 2 branches to P sat given cat equals 1 and a dashed branch P on given cat equals 0.')


# ---- 2.2 smoothing and interpolation ----
def f2():
    o = [T(20, 24, 'Unigram estimates (N = 10 tokens, V = 6 types)', 15, 'start', INK, True)]
    x0, sc = 230, 900  # px per unit probability
    rows = [('the, MLE 4/10', 0.40, '0.40', PANEL, L2), ('the, add-one 5/16', 0.3125, '0.3125', ACS, AC),
            ('dog, MLE 0/10', 0.0, '0', PANEL, L2), ('dog, add-one 1/16', 0.0625, '0.0625', ACS, AC)]
    y = 42
    for lab, v, s, f, c in rows:
        o.append(T(x0 - 12, y + 19, lab, 14, 'end'))
        if v: o.append(R(x0, y, v * sc, 26, f, c, 4, 1.5))
        else: o.append(L(x0, y, x0, y + 26, NX, 3))
        o.append(T(x0 + v * sc + 10, y + 19, s, 14, 'start', INK, True))
        y += 36
    o.append(T(x0 + 0.0625 * sc + 80, 42 + 3 * 36 + 19, '← add-one lifts the unseen word off zero', 13, 'start', AC))
    # interpolation
    y += 20
    o.append(T(20, y + 4, 'Interpolated P(dog | the)', 15, 'start', INK, True))
    y += 22
    o.append(boxt(20, y, 200, 56, ['bigram (MLE)', 'c(the dog) = 0 → 0'], PANEL, L2, 14))
    o.append(boxt(20, y + 72, 200, 56, ['unigram (add-one)', '1/16 = 0.0625'], ACS, AC, 14))
    o.append(L(224, y + 28, 300, y + 28, L2, 2, arrow='m')); o.append(Tb(262, y + 22, '× 0.7', 14, bold=True))
    o.append(L(224, y + 100, 300, y + 100, AC, 2, arrow='n')); o.append(Tb(262, y + 94, '× 0.3', 14, bold=True))
    o.append(boxt(306, y + 8, 120, 40, ['0'], PANEL, L2, 15))
    o.append(boxt(306, y + 80, 120, 40, ['0.01875'], ACS, AC, 15))
    o.append(L(430, y + 28, 492, y + 58, L2, 2, arrow='m'))
    o.append(L(430, y + 100, 492, y + 72, AC, 2, arrow='n'))
    o.append(boxt(498, y + 36, 200, 56, ['P(dog | the)', '= 0.01875 ≈ 0.019'], ACS, AC, 15, True))
    return y + 140, ''.join(o)
FIG[2] = (f2, 'Add-one moves a little mass to the unseen word: dog goes from 0 to 1/16 while the word the drops from 0.40 to 0.3125. Mixing the zero bigram (weight 0.7) with that unigram (weight 0.3) gives P(dog | the) = 0.01875.',
          'Four bars comparing maximum likelihood and add-one estimates for the and dog; below, the zero bigram times 0.7 and the add-one unigram 0.0625 times 0.3 add to 0.01875.')


# ---- 2.3 perplexity of "the cat" ----
def f3():
    o = [T(20, 24, 'Bigram model on ⟨s⟩ the cat ⟨/s⟩: three predictions, m = 3', 15, 'start', INK, True)]
    ps = [('P(the | ⟨s⟩)', '0.5'), ('P(cat | the)', '0.4'), ('P(⟨/s⟩ | cat)', '0.5')]
    for i, (lab, v) in enumerate(ps):
        x = 20 + i * 150
        o.append(boxt(x, 40, 130, 56, [lab, v], ACS, AC, 14, False))
        if i < 2: o.append(T(x + 140, 74, '×', 18, bold=True))
    o.append(T(470, 74, '= 0.1', 18, 'start', INK, True))
    o.append(T(20, 130, 'PP = 0.1^(−1/3) = 2.15', 16, 'start', AC, True))
    o.append(T(20, 168, 'Uniform model over {the, cat, dog, ⟨/s⟩}: each prediction 1/4', 15, 'start', INK, True))
    for i in range(3):
        x = 20 + i * 150
        o.append(boxt(x, 184, 130, 44, ['0.25'], PANEL, L2, 15))
        if i < 2: o.append(T(x + 140, 212, '×', 18, bold=True))
    o.append(T(470, 212, '= 0.015625', 18, 'start', INK, True))
    o.append(T(20, 262, 'PP = 0.015625^(−1/3) = 4.00', 16, 'start', MUT, True))
    # bars
    y = 296
    sc = 120
    o.append(T(20, y - 8, 'perplexity: lower means less surprised', 14, 'start', MUT))
    o.append(T(110, y + 22, 'bigram', 14, 'end', INK, True)); o.append(R(120, y + 4, 2.15 * sc, 26, ACS, AC, 4, 1.5)); o.append(T(128 + 2.15 * sc, y + 22, '2.15', 15, 'start', AC, True))
    o.append(T(110, y + 60, 'uniform', 14, 'end', INK, True)); o.append(R(120, y + 42, 4.0 * sc, 26, PANEL, L2, 4, 1.5)); o.append(T(128 + 4.0 * sc, y + 60, '4.00', 15, 'start', MUT, True))
    return y + 82, ''.join(o)
FIG[3] = (f3, 'The bigram model multiplies its three predictions to 0.1, so its perplexity is 0.1^(−1/3) = 2.15; the uniform model gives every word 1/4 and scores 4.00. Lower perplexity means the model is less surprised.',
          'Three probability boxes 0.5, 0.4 and 0.5 multiply to 0.1 and perplexity 2.15; three boxes of 0.25 multiply to 0.015625 and perplexity 4.00; two bars compare 2.15 with 4.00.')
TEXT[3] = [('The figure shows the usual picture. The unigram model', 'The usual picture is a U shape. The unigram model')]


# ---- 2.4 baseline, rule and the Brill gain ----
def f4():
    o = [T(20, 24, 'They/PRP want/VBP to/TO fly/?', 15, 'start', INK, True)]
    o.append(R(20, 40, 7 * 40, 30, PANEL, L2, 4, 1.5)); o.append(T(20 + 3.5 * 40, 60, 'NN 7', 14, bold=True))
    o.append(R(20 + 7 * 40, 40, 3 * 40, 30, ACS, AC, 4, 1.5)); o.append(T(20 + 8.5 * 40, 60, 'VB 3', 14, bold=True))
    o.append(T(440, 52, 'baseline: fly/NN, P = 0.70', 14, 'start'))
    o.append(T(440, 72, 'rule "after TO, a verb is VB": fly/VB', 14, 'start', AC, True))
    # dev set grids
    def grid(x0, y0, title, wrong, fixed=(), broke=()):
        g = [T(x0, y0 - 10, title, 14, 'start', INK, True)]
        for i in range(50):
            r, c = divmod(i, 10)
            x, y = x0 + c * 30, y0 + r * 30
            if i in fixed: f, s = LVS, LV
            elif i in broke or i in wrong: f, s = NXS, NX
            else: f, s = ACS, AC
            g.append(R(x, y, 26, 26, f, s, 4, 1.5))
            if i in fixed: g.append(T(x + 13, y + 18, '✓', 14, fill=LV, bold=True))
            elif i in broke or i in wrong: g.append(T(x + 13, y + 18, '✗', 14, fill=NX, bold=True))
        return ''.join(g)
    wrong = set(range(42, 50))
    o.append(grid(20, 130, 'Baseline: 42 of 50 right = 84.0%', wrong))
    o.append(grid(380, 130, 'After the rule: 44 of 50 = 88.0%', wrong - {42, 43, 44} | {5}, fixed={42, 43, 44}, broke={5}))
    o.append(L(332, 200, 368, 200, AC, 2.5, arrow='n'))
    y = 300
    o.append(R(380, y, 18, 16, LVS, LV, 3, 1.5)); o.append(T(404, y + 13, 'fixed by the rule: 3', 13, 'start'))
    o.append(R(560, y, 18, 16, NXS, NX, 3, 1.5)); o.append(T(584, y + 13, 'wrong', 13, 'start'))
    o.append(T(20, y + 13, 'net gain = 3 fixed − 1 broken = +2', 14, 'start', INK, True))
    return y + 26, ''.join(o)
FIG[4] = (f4, 'fly is NN 7 times and VB 3 times, so the baseline tags it NN; the TO rule gives VB. On the 50-token development set the Brill rule fixes 3 and breaks 1, so 42 right (84.0%) becomes 44 right (88.0%).',
          'A bar split NN 7 and VB 3 for fly; two grids of 50 squares, the first with 8 wrong, the second after the rule with 3 fixed and 1 newly broken, 44 right.')
AFTER[4] = 3


# ---- 2.5 Viterbi on fish sleep ----
def f5():
    xs, xc = 70, [230, 470]
    yN, yV = 110, 290
    o = [T(xc[0], 30, 'fish', 16, bold=True), T(xc[1], 30, 'sleep', 16, bold=True)]
    o.append(T(xc[0], 50, 't = 1', 13, fill=MUT)); o.append(T(xc[1], 50, 't = 2', 13, fill=MUT))
    S = (xs, 200)
    # start edges
    o.append(edge(S, (xc[0], yN), 30, 0, NX, 3.5, 'x')); o.append(edge(S, (xc[0], yV), 30, 0, L2, 2, 'm'))
    o.append(Tb(140, 138, '0.6 × 0.5', 13)); o.append(Tb(140, 268, '0.4 × 0.2', 13))
    # middle edges
    o.append(edge((xc[0], yN), (xc[1], yN), 30, 0, AC, 2))           # N->N kept 0.12
    o.append(edge((xc[0], yV), (xc[1], yN), 30, 0, L2, 1.5, 'm', '6 5'))  # V->N lost 0.056
    o.append(edge((xc[0], yN), (xc[1], yV), 30, 0, NX, 3.5, 'x'))    # N->V kept 0.18 best
    o.append(edge((xc[0], yV), (xc[1], yV), 30, 0, L2, 1.5, 'm', '6 5'))  # V->V lost 0.024
    o.append(Tb(350, yN - 10, '0.12 kept', 13, bold=True, fill=AC))
    o.append(Tb(403, 162, '0.056', 13, fill=MUT))
    o.append(Tb(403, 244, '0.18 kept', 13, bold=True, fill=NX))
    o.append(Tb(350, yV + 22, '0.024', 13, fill=MUT))
    o.append(state(*S, 'start', r=30, size=13))
    for x, (dn, dv) in zip(xc, [('0.30', '0.08'), ('0.012', '0.108')]):
        o.append(state(x, yN, 'N', r=30, fill=PANEL))
        o.append(state(x, yV, 'V', r=30, fill=NXS if dv == '0.108' else PANEL, stroke=NX if dv == '0.108' else AC))
    o.append(T(xc[0], yN - 40, 'δ = 0.30', 14, bold=True)); o.append(T(xc[0], yV + 52, 'δ = 0.08', 14, bold=True))
    o.append(T(xc[1] + 40, yN - 3, 'δ = 0.12 × 0.1', 14, 'start')); o.append(T(xc[1] + 40, yN + 17, '= 0.012', 14, 'start'))
    o.append(T(xc[1] + 40, yV + 5, 'δ = 0.18 × 0.6', 14, 'start', NX, True))
    o.append(T(xc[1] + 40, yV + 25, '= 0.108 (best)', 14, 'start', NX, True))
    o.append(T(20, 380, 'Backtrace from V: its backpointer is N, so the path is fish/N sleep/V with probability 0.108.', 14, 'start'))
    return 396, ''.join(o)
FIG[5] = (f5, 'Viterbi on fish sleep. Each node keeps only its best incoming score (0.12 into N, 0.18 into V); the thick path start → N → V ends at δ₂(V) = 0.108, so the tags are fish/N sleep/V.',
          'A trellis with a start node, tags N and V under fish and under sleep, four edges between the columns with scores 0.12 and 0.18 kept and 0.056 and 0.024 dashed as lost; the path start, N, V is thick and ends at 0.108.')


# ---- 2.6 MEMM local probabilities ----
def f6():
    o = [T(20, 24, 'Token flies after tag N: two features fire for each tag', 15, 'start', INK, True)]
    sc = 150
    rows = [('tag V', 1.5, 0.2, '1.7', '5.474', 0.60, NXS, NX), ('tag N', 0.8, 0.5, '1.3', '3.669', 0.40, ACS, AC)]
    y = 50
    for lab, w1, w2, s, e, p, f, c in rows:
        o.append(T(80, y + 24, lab, 15, 'end', INK, True))
        o.append(R(92, y + 4, w1 * sc, 28, f, c, 4, 1.5)); o.append(T(92 + w1 * sc / 2, y + 23, f'word=flies {w1}', 13))
        o.append(R(92 + w1 * sc, y + 4, max(w2 * sc, 4), 28, PANEL, c, 4, 1.5))
        o.append(T(92 + (w1 + w2) * sc + 8, y + 23, f'+ prev=N {w2} = {s}', 13, 'start', INK, True))
        o.append(L(505, y + 18, 538, y + 18, c, 2, arrow='x' if c == NX else 'n'))
        o.append(boxt(544, y + 2, 170, 34, [f'exp({s}) = {e}'], f, c, 14))
        y += 62
    o.append(T(629, y + 18, 'Z = 5.474 + 3.669 = 9.143', 14, 'middle', INK, True))
    y += 50
    o.append(T(20, y, 'Divide by Z: the two probabilities at this position sum to 1', 14, 'start', MUT))
    y += 14
    W = 600
    o.append(R(60, y, W * 0.5987, 40, NXS, NX, 4, 1.5)); o.append(T(60 + W * 0.3, y + 26, 'P(V | N, flies) = 0.60', 15, bold=True))
    o.append(R(60 + W * 0.5987, y, W * 0.4013, 40, ACS, AC, 4, 1.5)); o.append(T(60 + W * 0.8, y + 26, 'P(N | N, flies) = 0.40', 15, bold=True))
    return y + 56, ''.join(o)
FIG[6] = (f6, 'Each tag adds up the weights of its firing features (1.7 for V, 1.3 for N), takes the exponential, and divides by Z = 9.143, so P(V | N, flies) = 0.60 and P(N | N, flies) = 0.40 at this one position.',
          'Two rows of weight bars: tag V gets 1.5 plus 0.2, tag N gets 0.8 plus 0.5; their exponentials 5.474 and 3.669 add to Z 9.143; a bar split 0.60 for V and 0.40 for N.')


# ---- 2.7 CRF: one pool for the whole sequence ----
def f7():
    o = [T(20, 24, 'All 2³ = 8 label sequences put their exp(score) into one pool', 15, 'start', INK, True)]
    W, x0, y = 660, 30, 48
    parts = [('N, V, N', 12.18, NXS, NX), ('N, N, N', 6.05, ACS, AC), ('the other six', 11.77, PANEL, L2)]
    x = x0
    for lab, v, f, c in parts:
        w = v / 30 * W
        o.append(R(x, y, w, 52, f, c, 4, 2 if c == NX else 1.5))
        o.append(T(x + w / 2, y + 22, lab, 14, bold=True)); o.append(T(x + w / 2, y + 42, f'{v:.2f}', 14))
        x += w
    o.append(brace(x0, x0 + W, y + 64, INK))
    o.append(T(x0 + W / 2, y + 92, 'Z(x) = 12.18 + 6.05 + 11.77 = 30.00', 15, bold=True))
    w1 = 12.18 / 30 * W
    y2 = 190
    o.append(boxt(150, y2, 420, 60, ['P(N, V, N | x) = 12.18 ÷ 30.00 = 0.406'], NXS, NX, 16))
    o.append(T(360, y2 + 92, 'one normaliser for the whole sentence, not one per position', 14, fill=MUT))
    return y2 + 108, ''.join(o)
FIG[7] = (f7, 'Every complete label sequence adds its exponential into one sum, Z(x) = 30.00; the sequence N, V, N holds 12.18 of it, so its probability is 0.406. No single position is normalised on its own.',
          'One long bar split into N V N 12.18, N N N 6.05 and the other six sequences 11.77, bracketed as Z equals 30; below, P of N V N equals 12.18 over 30 equals 0.406.')


# ---- 2.8 BIO tags and exact-span scoring ----
def f8():
    toks = ['Mr', 'Rao', 'of', 'TCS', 'met', 'the', 'team', 'in', 'Pune']
    gold = ['O', 'B-PER', 'O', 'B-ORG', 'O', 'O', 'O', 'O', 'B-LOC']
    cw, x0 = 72, 70
    o = []
    o.append(T(x0 - 10, 50, 'token', 13, 'end', MUT)); o.append(T(x0 - 10, 96, 'gold', 13, 'end', MUT)); o.append(T(x0 - 10, 158, 'system', 13, 'end', MUT))
    for i, (t, g) in enumerate(zip(toks, gold)):
        x = x0 + i * cw
        o.append(TM(x + cw / 2, 50, t, 15, bold=True))
        ent = g != 'O'
        o.append(R(x + 4, 74, cw - 8, 32, ACS if ent else PANEL, AC if ent else LN, 5, 1.5))
        o.append(T(x + cw / 2, 95, g, 13, bold=ent, fill=INK if ent else MUT))
    # system spans
    def span(i0, i1, lab, ok):
        x = x0 + i0 * cw + 4; w = (i1 - i0 + 1) * cw - 8
        return R(x, 138, w, 32, LVS if ok else NXS, LV if ok else NX, 5, 2) + T(x + w / 2, 159, lab, 14, bold=True)
    o.append(span(1, 1, 'PER', True)); o.append(span(3, 3, 'ORG', True)); o.append(span(6, 8, 'LOC: team in Pune', False))
    o.append(T(x0 + 1.5 * cw, 192, '✓ match', 13, fill=LV, bold=True)); o.append(T(x0 + 3.5 * cw, 192, '✓ match', 13, fill=LV, bold=True))
    o.append(T(x0 + 7.5 * cw, 192, '✗ wrong boundary', 13, fill=NX, bold=True))
    y = 222
    o.append(boxt(20, y, 220, 64, ['false positive:', 'team in Pune (LOC)'], NXS, NX, 14))
    o.append(boxt(250, y, 220, 64, ['false negative:', 'Pune (LOC) missed'], NXS, NX, 14))
    o.append(boxt(480, y, 220, 64, ['C = 2, N = 3, G = 3', 'P = R = F1 = 0.67'], ACS, AC, 14, True))
    return y + 76, ''.join(o)
FIG[8] = (f8, 'Gold BIO tags against the system\'s spans. Rao and TCS match exactly; the system\'s LOC span covers team in Pune where gold has only Pune, so one wrong boundary costs a false positive and a false negative, and P = R = F1 = 0.67.',
          'Nine tokens with their gold BIO tags; under them the system spans PER on Rao and ORG on TCS marked as matches, and one LOC span over team in Pune marked as a wrong boundary; boxes give the false positive, the false negative and the scores 0.67.')
AFTER[8] = 4
# the quiz answer tagged the title inside the span, against the convention of the worked example
TEXT[8] = [("Ms/B-PER Iyer/I-PER flew/O from/O Delhi/B-LOC to/O Wipro/B-ORG office/O in/O Bengaluru/B-LOC. The title 'Ms' begins the person span here because it is inside the gold span.",
            "Ms/O Iyer/B-PER flew/O from/O Delhi/B-LOC to/O Wipro/B-ORG office/O in/O Bengaluru/B-LOC. As with 'Mr' in the worked example, the title 'Ms' stays outside the person span, so it is O.")]


# ---- 2.9 triples from one sentence, and scoring a pattern ----
def f9():
    o = [T(20, 24, 'Rao joined TCS in Pune last Monday', 15, 'start', INK, True)]
    R0 = (110, 140)
    tg = [((480, 60), 'TCS', 'ORG', 'works_for'), ((480, 140), 'Pune', 'LOC', 'works_in'), ((480, 220), 'Monday', 'DATE', 'joined_on')]
    o.append(boxt(R0[0] - 70, R0[1] - 28, 140, 56, ['Rao', 'PER'], ACS, AC, 15, True))
    for (x, y), name, typ, rel in tg:
        o.append(L(R0[0] + 72, R0[1], x - 74, y, AC, 2, arrow='n'))
        o.append(boxt(x - 70, y - 26, 140, 52, [name, typ], PANEL, AC, 14, True))
        o.append(Tb((R0[0] + 72 + x - 74) / 2 + 10, (R0[1] + y) / 2 - 6, rel, 14, bold=True))
        o.append(T(x + 82, y + 5, f'({"Rao"}, {rel}, {name})', 13, 'start', MUT))
    y = 290
    o.append(T(20, y, 'Pattern PER joined ORG in LOC on held-out text with 5 true relations', 14, 'start', INK, True))
    y += 14
    for i in range(5):
        x = 20 + i * 64
        ok = i < 2
        o.append(R(x, y, 56, 34, LVS if ok else PANEL, LV if ok else L2, 5, 1.5, None if ok else '5 4'))
        o.append(T(x + 28, y + 23, 'found' if ok else 'missed', 13, fill=LV if ok else MUT, bold=ok))
    o.append(R(360, y, 56, 34, NXS, NX, 5, 1.5)); o.append(T(388, y + 23, 'wrong', 13, fill=NX, bold=True))
    for i, t in enumerate(['P = 2 ÷ 3 = 0.67', 'R = 2 ÷ 5 = 0.40', 'F1 = 0.50']):
        o.append(T(20 + i * 180, y + 58, t, 15, 'start', INK, True))
    return y + 72, ''.join(o)
FIG[9] = (f9, 'One sentence gives three triples, all hanging off the shared entity Rao. The pattern fires 3 times with 2 right, out of 5 true relations, so precision is 0.67, recall 0.40 and F1 0.50.',
          'Rao, a person, joined by arrows works_for to TCS, works_in to Pune and joined_on to Monday; below, five true relations of which two are found and three missed, plus one wrong output, with precision 0.67, recall 0.40 and F1 0.50.')


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d
TEXT[1] = [('The reverse is P(the | cat)=c(the cat)/c(cat)=2/2=1.00. They are not equal, so the direction matters.',
            'Reading the same count the other way round gives c(the cat)/c(cat)=2/2=1.00, but that is not a probability the model defines: the real P(the | cat)=c(cat the)/c(cat)=0/2=0. The numbers differ, so the direction matters.')]


def text_fixes(k):
    return TEXT.get(k, [])


def drop_sources():
    # university-hosted pages: the books name no universities
    return ['stanford.edu']
