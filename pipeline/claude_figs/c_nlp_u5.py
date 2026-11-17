"""Claude's hand-drawn figures for c-nlp-u5 (NLP, unit 5: text classification and word vectors), one per chapter,
drawn from each chapter's worked example, plus the university-hosted sources to drop. The figure sentence in 5.6
still matches the new drawing."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {}
TEXT = {}


def shade(v, vmax):
    pct = int(6 + 60 * v / vmax) if v else 0
    return f'color-mix(in srgb, var(--accent) {pct}%, var(--fig))' if v else 'var(--panel)'


# ---- 5.1 the TF-IDF matrix ----
def f1():
    terms = ['cricket', 'bat', 'ball', 'stock', 'market']
    df = [2, 1, 2, 1, 1]
    idf = ['0.18', '0.48', '0.18', '0.48', '0.48']
    W = {'D1': [0.06, 0.16, 0.06, 0, 0], 'D2': [0.09, 0, 0.09, 0, 0], 'D3': [0, 0, 0, 0.24, 0.24]}
    txt = {'D1': 'cricket bat ball', 'D2': 'cricket ball', 'D3': 'stock market'}
    x0, cw, rh = 230, 94, 44
    o = []
    for j, t in enumerate(terms):
        o.append(T(x0 + j * cw + cw / 2, 30, t, 14, bold=True))
    rows = [('df(t)', [str(d) for d in df], False), ('idf = log₁₀(3 ÷ df)', idf, False)]
    y = 44
    for lab, vals, _ in rows:
        o.append(T(x0 - 12, y + 27, lab, 13, 'end', MUT, True))
        for j, v in enumerate(vals):
            o.append(R(x0 + j * cw + 3, y + 3, cw - 6, rh - 6, PANEL, LN, 5, 1))
            o.append(T(x0 + j * cw + cw / 2, y + 28, v, 14, fill=MUT if lab == 'df(t)' else INK, bold=lab != 'df(t)'))
        y += rh
    y += 14
    o.append(T(x0 + 2.5 * cw, y + 2, 'TF-IDF weight = (count ÷ length) × idf', 13, fill=MUT))
    y += 10
    for d, ws in W.items():
        o.append(T(x0 - 12, y + 22, d, 15, 'end', INK, True))
        o.append(T(x0 - 12, y + 40, txt[d], 12, 'end', MUT))
        for j, v in enumerate(ws):
            o.append(R(x0 + j * cw + 3, y + 3, cw - 6, rh + 4, shade(v, 0.24), AC if v else LN, 5, 1.5 if v else 1))
            o.append(T(x0 + j * cw + cw / 2, y + 33, f'{v:.2f}' if v else '0', 15, bold=bool(v), fill=INK if v else MUT))
        y += rh + 8
    o.append(T(20, y + 20, 'bat, stock and market sit in one document each, so their idf is high (0.48); D3 is zero under all three cricket terms.', 13, 'start'))
    return y + 34, ''.join(o)
FIG[1] = (f1, 'The worked example\'s TF-IDF matrix. Terms found in only one document (bat, stock, market) get idf 0.48, terms in two documents get 0.18, and D3 is zero under the cricket terms, so the two topics separate.',
          'A table with the terms cricket, bat, ball, stock and market across the top, rows for document frequency and idf, then shaded rows of TF-IDF weights for D1, D2 and D3.')


# ---- 5.2 Naive Bayes with add-one ----
def f2():
    o = [T(20, 24, 'Train: positive = "good film", negative = "bad film".  Test: "good film"', 14, 'start', INK, True)]
    cols = [('positive', 'P(pos) = 0.5', [('good', 1, '2/5 = 0.4'), ('film', 1, '2/5 = 0.4')], '0.5 × 0.4 × 0.4 = 0.08', 0.08, AC, ACS),
            ('negative', 'P(neg) = 0.5', [('good', 0, '1/5 = 0.2'), ('film', 1, '2/5 = 0.4')], '0.5 × 0.2 × 0.4 = 0.04', 0.04, NX, NXS)]
    for i, (name, prior, terms, prod, score, c, cs) in enumerate(cols):
        x = 20 + i * 350
        o.append(R(x, 40, 330, 210, PANEL, c, 10, 2))
        o.append(T(x + 16, 66, name, 15, 'start', c, True)); o.append(T(x + 314, 66, prior, 14, 'end'))
        o.append(T(x + 16, 94, 'term', 12, 'start', MUT)); o.append(T(x + 150, 94, 'count', 12, 'middle', MUT)); o.append(T(x + 314, 94, '(count + 1) ÷ (2 + 3)', 12, 'end', MUT))
        for j, (t, n, p) in enumerate(terms):
            y = 120 + j * 44
            zero = n == 0
            o.append(TM(x + 16, y, t, 15, 'start', INK, True)); o.append(T(x + 150, y, str(n), 15, fill=NX if zero else INK, bold=zero))
            o.append(T(x + 314, y, p, 15, 'end', INK, True))
            if zero: o.append(T(x + 314, y + 19, 'add-one keeps it above 0', 12, 'end', NX))
        o.append(L(x + 16, 200, x + 314, 200, LN, 1))
        o.append(T(x + 165, 226, prod, 15, bold=True))
    # score bars
    y = 280
    sc = 4000
    for i, (name, _, _, _, score, c, cs) in enumerate(cols):
        yy = y + i * 44
        o.append(T(110, yy + 22, name, 14, 'end', INK, True))
        o.append(R(120, yy + 4, score * sc, 28, cs, c, 4, 1.5))
        o.append(T(128 + score * sc, yy + 23, f'{score:.2f}' + ('  ← bigger: predict positive' if i == 0 else ''), 14, 'start', c, True))
    return y + 96, ''.join(o)
FIG[2] = (f2, 'Each class multiplies its prior by the smoothed probability of every test word. good never occurs with the negative class, yet add-one gives it 1/5 instead of 0; the positive score 0.08 beats 0.04.',
          'Two panels, positive and negative, each listing counts of good and film with add-one probabilities and the product of prior and probabilities; bars compare the scores 0.08 and 0.04.')


# ---- 5.3 the confusion matrix ----
def f3():
    x0, y0, c = 190, 70, 150
    o = [T(x0 + c, 26, 'actual class', 14, fill=MUT), T(x0 + c / 2, 52, 'spam', 14, bold=True), T(x0 + 1.5 * c, 52, 'ham', 14, bold=True)]
    o.append(f'<text x="44" y="{y0 + c:.1f}" font-size="14" text-anchor="middle" transform="rotate(-90 44 {y0 + c:.1f})" style="fill:var(--muted)">predicted</text>')
    o.append(T(x0 - 14, y0 + c / 2 + 5, 'spam', 14, 'end', INK, True)); o.append(T(x0 - 14, y0 + 1.5 * c + 5, 'ham', 14, 'end', INK, True))
    cells = [(0, 0, 'TP', 80, ACS, AC), (1, 0, 'FP', 20, NXS, NX), (0, 1, 'FN', 10, NXS, NX), (1, 1, 'TN', 890, PANEL, L2)]
    for cx, cy, lab, n, f, s in cells:
        x, y = x0 + cx * c, y0 + cy * c
        o.append(R(x + 3, y + 3, c - 6, c - 6, f, s, 8, 2))
        o.append(T(x + c / 2, y + c / 2 - 6, str(n), 26, bold=True))
        o.append(T(x + c / 2, y + c / 2 + 22, lab, 14, fill=s, bold=True))
    o.append(brace(x0 + 4, x0 + 2 * c - 4, y0 - 8, AC, up=True))
    # metrics
    mx = 530
    mets = [('precision', '80 ÷ 100', 0.800), ('recall', '80 ÷ 90', 0.889), ('F1', 'harmonic mean', 0.842), ('accuracy', '970 ÷ 1000', 0.970)]
    for i, (n, f_, v) in enumerate(mets):
        y = y0 + 10 + i * 70
        o.append(T(mx, y + 14, n, 15, 'start', INK, True)); o.append(T(mx + 170, y + 14, f'{v:.3f}', 15, 'end', AC, True))
        o.append(T(mx, y + 34, f_, 13, 'start', MUT))
        o.append(R(mx, y + 42, 170, 8, PANEL, LN, 3, 1)); o.append(R(mx, y + 42, 170 * v, 8, ACS, AC, 3, 1))
    o.append(T(x0 + c, y0 + 2 * c + 30, 'precision reads across the spam row; recall reads down the spam column', 13, fill=MUT))
    return y0 + 2 * c + 44, ''.join(o)
FIG[3] = (f3, 'The 1000 test emails in four cells. Precision uses the predicted-spam row, 80 of 100; recall uses the actual-spam column, 80 of 90. F1 is 0.842, and accuracy, 970 of 1000, looks better than either.',
          'A two by two confusion matrix with TP 80, FP 20, FN 10 and TN 890, and bars for precision 0.800, recall 0.889, F1 0.842 and accuracy 0.970.')
AFTER[3] = 3


# ---- 5.4 lexicon scoring with negation, and the aspect view ----
def f4():
    toks = [('not', 'negator', NX), ('good', '+2', AC), ('but', 'neutral', L2), ('excellent', '+3', AC), ('songs', 'aspect', LV)]
    o = []
    x = 30
    xs = []
    for t, s, c in toks:
        w = tw(t, 15) + 30
        o.append(R(x, 60, w, 36, PANEL, c, 6, 1.8)); o.append(TM(x + w / 2, 84, t, 15, bold=True))
        o.append(T(x + w / 2, 116, s, 13, fill=c if c != L2 else MUT, bold=True))
        xs.append(x + w / 2); x += w + 22
    o.append(arc(xs[0], 56, xs[1], 56, 0.35, NX, 2, 'x'))
    o.append(T((xs[0] + xs[1]) / 2, 24, '× −1', 14, fill=NX, bold=True))
    o.append(T(30, 160, 'not good = +2 × −1 = −2;   excellent = +3;   total = −2 + 3 = +1 → positive', 15, 'start', INK, True))
    # number line
    x0, x1, y = 90, 650, 250
    fx = lambda v: x0 + (v + 3) / 6 * (x1 - x0)
    o.append(L(x0, y, x1, y, L2, 2))
    for v in range(-3, 4):
        o.append(L(fx(v), y - 5, fx(v), y + 5, L2, 1.5)); o.append(T(fx(v), y + 24, neg(f'{v:+d}' if v else '0'), 13, fill=MUT))
    for v, lab, c, cs in [(-2, 'film −2', NX, NXS), (3, 'songs +3', AC, ACS), (1, 'whole review +1', LV, LVS)]:
        o.append(C(fx(v), y, 8, c))
        yy = y - 38 if v != 1 else y + 44
        o.append(boxt(fx(v) - 70, yy - 16, 140, 28, [lab], cs, c, 14))
    o.append(T(360, y + 92, 'The single total hides two aspects with opposite signs.', 14, fill=MUT))
    return y + 106, ''.join(o)
FIG[4] = (f4, 'not flips good from +2 to −2, excellent adds +3, so the review totals +1 and reads as positive. On the aspect line the film sits at −2 and the songs at +3: the one total hides both.',
          'Token boxes not, good, but, excellent, songs with lexicon scores, an arrow from not flipping good; a number line from minus 3 to plus 3 with film at minus 2, songs at plus 3 and the whole review at plus 1.')


# ---- 5.5 one-hot against dense ----
def f5():
    o = [T(170, 24, 'One-hot (3 dimensions)', 15, bold=True), T(530, 24, 'Dense (2 dimensions)', 15, bold=True)]
    for r, (w, v) in enumerate([('cricket', [1, 0, 0]), ('bat', [0, 1, 0])]):
        y = 50 + r * 60
        o.append(TM(70, y + 26, w, 15, 'end', INK, True))
        for j, b in enumerate(v):
            o.append(R(84 + j * 56, y, 50, 40, ACS if b else PANEL, AC if b else LN, 5, 1.5))
            o.append(T(109 + j * 56, y + 27, str(b), 17, bold=bool(b)))
    for j, w in enumerate(['cricket', 'bat', 'ball']):
        o.append(T(109 + j * 56, 186, w, 12, fill=MUT))
    o.append(T(170, 222, 'dot = 0, so cosine = 0', 15, fill=NX, bold=True))
    o.append(T(170, 246, 'every pair of different words: 0', 13, fill=MUT))
    # dense plot
    ox, oy, s = 400, 290, 300
    o.append(L(ox, oy, ox + 290, oy, L2, 1.5, arrow='m')); o.append(L(ox, oy, ox, oy - 260, L2, 1.5, arrow='m'))
    for v in (0.2, 0.4, 0.6, 0.8):
        o.append(T(ox + v * s, oy + 20, str(v), 12, fill=MUT)); o.append(T(ox - 8, oy - v * s + 4, str(v), 12, 'end', MUT))
        o.append(L(ox + v * s, oy, ox + v * s, oy - 250, LN, 1)); o.append(L(ox, oy - v * s, ox + 280, oy - v * s, LN, 1))
    for (x, y), lab, c, ar in [((0.8, 0.2), 'cricket [0.8, 0.2]', AC, 'n'), ((0.6, 0.4), 'bat [0.6, 0.4]', NX, 'x')]:
        o.append(L(ox, oy, ox + x * s, oy - y * s, c, 3, arrow=ar))
        o.append(Tb(ox + x * s - 6, oy - y * s - 14, lab, 13, 'end', c, True) if x < 0.7 else Tb(ox + x * s + 4, oy - y * s + 28, lab, 13, 'end', c, True))
    a1, a2 = math.atan2(0.2, 0.8), math.atan2(0.4, 0.6)
    r = 70
    o.append(f'<path d="M{ox + r * math.cos(a1):.1f},{oy - r * math.sin(a1):.1f} A{r},{r} 0 0 0 {ox + r * math.cos(a2):.1f},{oy - r * math.sin(a2):.1f}" style="fill:none;stroke:var(--ink);stroke-width:1.5"/>')
    o.append(T(ox + 82, oy - 30, '≈ 19.7°', 13, 'start', INK, True))
    o.append(T(20, 330, 'dense: dot = 0.48 + 0.08 = 0.56; lengths 0.8246 and 0.7211; cosine = 0.56 ÷ (0.8246 × 0.7211) ≈ 0.94', 14, 'start', AC, True))
    return 344, ''.join(o)
FIG[5] = (f5, 'One-hot vectors of different words never share a 1, so their cosine is always 0. The dense vectors of cricket and bat point almost the same way, about 20° apart, and their cosine is about 0.94.',
          'Left, one-hot rows for cricket and bat with their 1s in different columns; right, a plot of the dense vectors 0.8, 0.2 and 0.6, 0.4 as arrows about twenty degrees apart.')


# ---- 5.6 king - man + woman ----
def f6():
    ox, oy, s = 120, 340, 140
    o = []
    o.append(L(ox, oy, ox + 2.6 * s, oy, L2, 1.5, arrow='m')); o.append(L(ox, oy, ox, oy - 2.35 * s, L2, 1.5, arrow='m'))
    for v in (1, 2):
        o.append(L(ox + v * s, oy, ox + v * s, oy - 2.2 * s, LN, 1)); o.append(L(ox, oy - v * s, ox + 2.4 * s, oy - v * s, LN, 1))
        o.append(T(ox + v * s, oy + 20, str(v), 13, fill=MUT)); o.append(T(ox - 10, oy - v * s + 5, str(v), 13, 'end', MUT))
    o.append(T(ox - 10, oy + 20, '0', 13, 'end', MUT))
    P_ = {'man': (1, 0), 'woman': (0, 1), 'king': (1, 1), 'queen': (0, 2)}
    X = lambda p: (ox + p[0] * s, oy - p[1] * s)
    # the same woman step
    (a, b), (c_, d) = X(P_['man']), X(P_['king'])
    o.append(L(a, b - 10, c_, d + 12, LV, 2.5, '7 5', 'l'))
    (a, b), (c_, d) = X(P_['woman']), X(P_['queen'])
    o.append(L(a + 10, b - 10, c_ + 10, d + 12, LV, 2.5, '7 5', 'l'))
    o.append(Tb(ox + s + 10, oy - 0.5 * s, '+ [0, 1]', 13, 'start', LV, True))
    # king - man + woman
    (a, b), (c_, d) = X(P_['king']), X(P_['queen'])
    o.append(L(a - 10, b - 6, c_ + 12, d + 8, NX, 3, arrow='x'))
    o.append(Tb((a + c_) / 2 + 30, (b + d) / 2 + 2, '− man + woman = [−1, 1]', 13, 'start', NX, True))
    for n, p in P_.items():
        x, y = X(p)
        o.append(C(x, y, 8, NX if n == 'queen' else AC))
        lab = f'{n} [{p[0]}, {p[1]}]'
        o.append(Tb(x + 14, y - 12, lab, 14, 'start', INK, True))
    o.append(boxt(420, 40, 280, 100, ['king − man + woman', '= [1,1] − [1,0] + [0,1]', '= [0, 2] = queen, cosine 1.0'], NXS, NX, 14, True))
    return oy + 34, ''.join(o)
FIG[6] = (f6, 'The four words as points. The same step [0, 1] takes man to king and woman to queen, so starting at king and going back by man and forward by woman lands exactly on queen, [0, 2], with cosine 1.0.',
          'A grid with man at 1,0, woman at 0,1, king at 1,1 and queen at 0,2; dashed arrows show the same step from man to king and woman to queen; a solid arrow from king to queen is labelled minus man plus woman.')


# ---- 5.7 k-means converges after one update ----
def f7():
    ox, oy, s = 90, 330, 90
    o = []
    o.append(L(ox, oy, ox + 3.6 * s, oy, L2, 1.5, arrow='m')); o.append(L(ox, oy, ox, oy - 3.5 * s, L2, 1.5, arrow='m'))
    for v in (1, 2, 3):
        o.append(L(ox + v * s, oy, ox + v * s, oy - 3.3 * s, LN, 1)); o.append(L(ox, oy - v * s, ox + 3.4 * s, oy - v * s, LN, 1))
        o.append(T(ox + v * s, oy + 20, str(v), 13, fill=MUT)); o.append(T(ox - 10, oy - v * s + 5, str(v), 13, 'end', MUT))
    X = lambda p: (ox + p[0] * s, oy - p[1] * s)
    D = {'D1': ((3, 0), AC), 'D2': ((2, 1), AC), 'D3': ((0, 3), NX), 'D4': ((1, 2), NX)}
    Cs = {'C1': ((2.5, 0.5), AC, ACS), 'C2': ((0.5, 2.5), NX, NXS)}
    for n, (p, c) in D.items():
        cp = Cs['C1'][0] if c == AC else Cs['C2'][0]
        (x1, y1), (x2, y2) = X(p), X(cp)
        o.append(L(x1, y1, x2, y2, c, 1.8, '4 4'))
    for n, (p, c, cs) in Cs.items():
        x, y = X(p)
        o.append(f'<rect x="{x - 9:.1f}" y="{y - 9:.1f}" width="18" height="18" transform="rotate(45 {x:.1f} {y:.1f})" style="fill:{cs};stroke:{c};stroke-width:2.5"/>')
        o.append(Tb(x - 16, y + 5, f'{n} [{p[0]}, {p[1]}]', 13, 'end', c, True) if n == 'C1' else Tb(x + 16, y - 14, f'{n} [{p[0]}, {p[1]}]', 13, 'start', c, True))
    for n, (p, c) in D.items():
        x, y = X(p)
        o.append(C(x, y, 8, c))
        o.append(Tb(x + 12, y - 12, f'{n} [{p[0]}, {p[1]}]', 13, 'start', INK, True))
    mx = 440
    o.append(T(mx, 50, 'Start: C1 = D1, C2 = D3', 14, 'start', INK, True))
    o.append(T(mx, 74, 'D2 → C1 (1.414 vs 2.828)', 14, 'start'))
    o.append(T(mx, 96, 'D4 → C2 (1.414 vs 2.828)', 14, 'start'))
    o.append(T(mx, 130, 'Update: centroid = mean', 14, 'start', INK, True))
    o.append(T(mx, 154, 'C1 = [2.5, 0.5], C2 = [0.5, 2.5]', 14, 'start'))
    o.append(T(mx, 188, 'Check: each document is', 14, 'start', INK, True))
    o.append(T(mx, 212, '0.707 from its own centroid,', 14, 'start'))
    o.append(T(mx, 234, '2.121 or more from the other', 14, 'start'))
    o.append(boxt(mx, 256, 260, 44, ['no switch: converged'], ACS, AC, 15, True))
    return oy + 34, ''.join(o)
FIG[7] = (f7, 'After one update the centroids sit at the means, C1 = [2.5, 0.5] and C2 = [0.5, 2.5]. Every document is 0.707 from its own centroid and farther from the other, so no document moves and k-means stops.',
          'A grid with D1 at 3,0 and D2 at 2,1 joined to centroid C1 at 2.5,0.5, and D3 at 0,3 and D4 at 1,2 joined to centroid C2 at 0.5,2.5; notes on the right give the assignments and the convergence check.')


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
    return ['stanford.edu']
