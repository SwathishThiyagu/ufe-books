"""Claude's hand-drawn figures for c-nlp-u6 (NLP, unit 6: neural models, transformers and applications), one per chapter,
drawn from each chapter's worked example, plus the one sentence in 6.6 that pointed at a pipeline figure the chapter
does not have, and the university-hosted sources to drop."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {}
TEXT = {}


def bars(x0, y0, vals, labels, scale, c=AC, cs=ACS, h=26, gap=10, fmt='{:.3f}', lw=120, hl=None):
    o = []
    for i, (v, lab) in enumerate(zip(vals, labels)):
        y = y0 + i * (h + gap)
        on = hl is not None and i == hl
        o.append(T(x0 - 10, y + h * 0.7, lab, 14, 'end', INK, True))
        if v > 0: o.append(R(x0, y, max(v * scale, 3), h, NXS if on else cs, NX if on else c, 4, 1.5))
        o.append(T(x0 + v * scale + 8, y + h * 0.7, fmt.format(v), 14, 'start', NX if on else INK, True))
    return ''.join(o)


# ---- 6.1 one convolution filter over "food was great" ----
def f1():
    words = [('food', [1, 0, 1]), ('was', [0, 1, 0]), ('great', [1, 1, 0])]
    o = []
    x0, cw = 70, 46
    for i, (w, v) in enumerate(words):
        x = x0 + i * 150
        o.append(TM(x + 1.5 * cw, 30, w, 15, bold=True))
        for j, b in enumerate(v):
            o.append(R(x + j * cw, 42, cw - 4, 36, ACS if b else PANEL, AC if b else LN, 4, 1.4))
            o.append(T(x + j * cw + (cw - 4) / 2, 66, str(b), 15, bold=bool(b)))
    # windows
    o.append(R(x0 - 8, 36, 150 + 3 * cw + 12, 48, 'none', NX, 8, 2.5, '7 5'))
    o.append(R(x0 + 150 - 12, 90, 150 + 3 * cw + 16, 10, 'none', LV, 4, 2.5))
    o.append(T(x0 + 120, 112, 'window 1', 13, fill=NX, bold=True))
    o.append(T(x0 + 150 + 120, 124, 'window 2', 13, fill=LV, bold=True))
    o.append(T(20, 160, 'filter w = [1, −1, 0, 0, 1, −1], bias 0, width 2', 14, 'start', INK, True))
    rows = [('window 1: [1,0,1,0,1,0] · w = 1 + 1 = 2', 'ReLU(2) = 2', NX, NXS), ('window 2: [0,1,0,1,1,0] · w = −1 + 1 = 0', 'ReLU(0) = 0', LV, LVS)]
    for i, (a, b, c, cs) in enumerate(rows):
        y = 176 + i * 50
        o.append(R(20, y, 450, 40, cs, c, 6, 1.5)); o.append(T(34, y + 26, a, 14, 'start'))
        o.append(T(500, y + 26, b, 15, 'start', c, True))
    o.append(L(600, 196, 636, 214, L2, 2, arrow='m')); o.append(L(600, 246, 636, 228, L2, 2, arrow='m'))
    o.append(boxt(640, 196, 70, 52, ['max', '2'], ACS, AC, 15, True))
    o.append(T(20, 300, 'Max-pooling keeps one number per filter, whatever the sentence length.', 14, 'start', MUT))
    return 314, ''.join(o)
FIG[1] = (f1, 'The three word vectors side by side. A width-2 filter slides over the two windows: (food, was) scores ReLU(2) = 2 and (was, great) scores ReLU(0) = 0, and max-pooling keeps 2, one feature for this filter.',
          'Three 3-dimensional word vectors for food, was and great, two overlapping windows of width 2, the dot products 2 and 0 after ReLU, and a max box giving 2.')
AFTER[1] = 2


# ---- 6.2 the scalar RNN unrolled ----
def f2():
    xs = [0.0, 1.0, 0.5, -1.0]
    hs = [0.0, 0.762, 0.707, -0.570]
    sums = ['', '0.5×0 + 1 = 1', '0.5×0.762 + 0.5 = 0.881', '0.5×0.707 − 1 = −0.647']
    o = []
    bx = [30, 200, 380, 560]
    o.append(boxt(bx[0], 70, 120, 50, ['h₀ = 0'], PANEL, L2, 15, True))
    for t in (1, 2, 3):
        x = bx[t]
        last = t == 3
        o.append(L(bx[t - 1] + (120 if t == 1 else 150), 95, x - 4, 95, AC, 2.5, arrow='n'))
        o.append(T((bx[t - 1] + (120 if t == 1 else 150) + x) / 2, 52, '× 0.5', 12, fill=MUT, bold=True))
        o.append(boxt(x, 64, 150, 62, [f'h{"₁₂₃"[t - 1]} = tanh(·)', f'= {neg(f"{hs[t]:.3f}")}'], NXS if last else ACS, NX if last else AC, 14, True))
        o.append(L(x + 75, 170, x + 75, 130, L2, 2, arrow='m'))
        o.append(T(x + 75, 190, f'x{"₁₂₃"[t - 1]} = {neg(xs[t])}', 15, bold=True))
        o.append(T(x + 75, 214, neg(sums[t]), 12, fill=MUT))
    # value strip
    x0, x1, y = 80, 660, 290
    fx = lambda v: x0 + (v + 1) / 2 * (x1 - x0)
    o.append(L(x0, y, x1, y, L2, 2))
    for v in (-1, -0.5, 0, 0.5, 1):
        o.append(L(fx(v), y - 5, fx(v), y + 5, L2, 1.5)); o.append(T(fx(v), y + 22, neg(v), 13, fill=MUT))
    for t in (1, 2, 3):
        c = NX if t == 3 else AC
        o.append(C(fx(hs[t]), y, 7, c))
        o.append(T(fx(hs[t]), y - 14 - (12 if t == 2 else 0), f'h{"₁₂₃"[t - 1]}', 14, fill=c, bold=True))
    o.append(T(20, y + 52, 'tanh keeps every hidden state between −1 and 1; the −1 input pulls h₃ below zero.', 14, 'start', MUT))
    return y + 66, ''.join(o)
FIG[2] = (f2, 'The same cell applied three times: each step multiplies the previous hidden state by 0.5, adds the new input and takes tanh. h₁ ≈ 0.762, h₂ ≈ 0.707, and the input −1 pulls h₃ down to about −0.570.',
          'Three RNN boxes in a row fed by inputs 1, 0.5 and minus 1, with the hidden state passed right times 0.5; below, a line from minus 1 to 1 marking h1 0.762, h2 0.707 and h3 minus 0.570.')


# ---- 6.3 attention weights and the context vector, with and without a mask ----
def f3():
    o = [T(20, 24, 'Encoder states h₁ = [1, 0], h₂ = [0, 1], h₃ = [1, 1]; scores e = [1, 2, 3]', 14, 'start', INK, True)]
    o.append(T(20, 56, 'no mask', 15, 'start', AC, True))
    o.append(bars(80, 70, [0.090, 0.245, 0.665], ['α₁', 'α₂', 'α₃'], 300, hl=None))
    o.append(boxt(470, 74, 240, 82, ['c = 0.090 h₁ + 0.245 h₂', '+ 0.665 h₃', '= [0.755, 0.910]'], ACS, AC, 14, True))
    y = 196
    o.append(T(20, y, 'h₃ is a pad: its score is set to −1e9 before softmax', 15, 'start', NX, True))
    o.append(bars(80, y + 14, [0.269, 0.731, 0.0], ['α₁', 'α₂', 'α₃'], 300))
    o.append(T(130, y + 14 + 2 * 36 + 18, '(masked: exp(−1e9) = 0)', 13, 'start', NX))
    o.append(boxt(470, y + 18, 240, 82, ['c = 0.269 h₁ + 0.731 h₂', '+ 0 · h₃', '= [0.269, 0.731]'], NXS, NX, 14, True))
    o.append(T(20, y + 136, 'exp(1), exp(2), exp(3) = 2.718, 7.389, 20.086; sum 30.193. With the mask the sum is 10.108.', 13, 'start', MUT))
    return y + 150, ''.join(o)
FIG[3] = (f3, 'Softmax turns the scores 1, 2, 3 into weights 0.090, 0.245, 0.665, and the context is the weighted average of the encoder states, [0.755, 0.910]. Masking h₃ as a pad sets its weight to 0, and the rest share 1: [0.269, 0.731].',
          'Two sets of three weight bars: without a mask 0.090, 0.245 and 0.665 giving context 0.755, 0.910; with position 3 masked 0.269, 0.731 and 0 giving context 0.269, 0.731.')


# ---- 6.4 scaled dot-product attention for one query ----
def f4():
    o = []
    steps = [('scores q·k', ['q·k₁ = 1', 'q·k₂ = 0']), ('÷ √2', ['0.707', '0']), ('softmax', ['0.670', '0.330']), ('mix values', ['0.670 × [1, 1]', '0.330 × [0, 1]'])]
    xs = [20, 190, 330, 470]
    ws = [150, 120, 120, 180]
    for i, ((title, vals), x, w) in enumerate(zip(steps, xs, ws)):
        o.append(T(x + w / 2, 30, title, 14, fill=MUT, bold=True))
        for j, v in enumerate(vals):
            y = 44 + j * 60
            o.append(R(x, y, w, 44, ACS if j == 0 else PANEL, AC, 6, 1.6))
            o.append(T(x + w / 2, y + 28, v, 15, bold=True))
        if i < 3:
            o.append(L(x + w + 4, 96, xs[i + 1] - 6, 96, L2, 2, arrow='m'))
    o.append(T(20, 194, 'q = [1, 0];  k₁ = [1, 0];  k₂ = [0, 1];  v₁ = [1, 1];  v₂ = [0, 1];  dₖ = 2', 14, 'start', MUT))
    # output stacked bars
    y = 222
    o.append(T(20, y + 20, 'output', 15, 'start', INK, True))
    sc = 380
    for d, (a, b) in enumerate([(0.670, 0.0), (0.670, 0.330)]):
        yy = y + d * 44
        o.append(T(140, yy + 21, f'dim {d + 1}', 13, 'end', MUT))
        o.append(R(150, yy + 2, a * sc, 28, ACS, AC, 4, 1.5)); o.append(T(150 + a * sc / 2, yy + 21, 'from v₁ 0.670', 13, bold=True))
        if b: o.append(R(150 + a * sc, yy + 2, b * sc, 28, PANEL, AC, 4, 1.5)); o.append(T(150 + a * sc + b * sc / 2, yy + 21, 'v₂ 0.330', 13, bold=True))
        o.append(T(150 + (a + b) * sc + 10, yy + 21, f'= {a + b:.3f}', 14, 'start', AC, True))
    return y + 96, ''.join(o)
FIG[4] = (f4, 'One query against two keys: the dot products 1 and 0 are divided by √2, softmax turns them into weights 0.670 and 0.330, and the output mixes the value rows to [0.670, 1.000].',
          'Four columns from scores 1 and 0, to scaled 0.707 and 0, to weights 0.670 and 0.330, to the weighted values; stacked bars show the output 0.670 and 1.000.')


# ---- 6.5 temperature and top-2 ----
def f5():
    o = [T(20, 24, 'Logits A 2.0, B 1.0, C 0.5, D −1.0; divide by T = 0.5 → 4.0, 2.0, 1.0, −2.0', 14, 'start', INK, True)]
    o.append(T(20, 60, 'after softmax', 15, 'start', AC, True))
    o.append(bars(70, 74, [0.842, 0.114, 0.042, 0.002], ['A', 'B', 'C', 'D'], 300))
    o.append(L(70, 74 + 2 * 36 - 5, 450, 74 + 2 * 36 - 5, NX, 2, '6 4'))
    o.append(T(450, 74 + 2 * 36 - 11, 'top-2 cut', 13, 'end', NX, True))
    o.append(T(470, 60, 'top-2, renormalised', 15, 'start', NX, True))
    o.append(bars(500, 74, [0.881, 0.119], ['A', 'B'], 160, NX, NXS))
    o.append(T(470, 172, '0.842 ÷ 0.956 = 0.881', 13, 'start', MUT)); o.append(T(470, 192, '0.114 ÷ 0.956 = 0.119', 13, 'start', MUT))
    o.append(T(20, 236, 'T below 1 sharpens the distribution; top-k then throws away the tail and rescales what is left to sum to 1.', 13, 'start', MUT))
    return 250, ''.join(o)
FIG[5] = (f5, 'Dividing the logits by T = 0.5 sharpens the softmax to 0.842, 0.114, 0.042, 0.002. Top-2 keeps A and B and rescales them by their sum 0.956 to 0.881 and 0.119.',
          'Four probability bars A 0.842, B 0.114, C 0.042, D 0.002 with a dashed cut after B; two renormalised bars A 0.881 and B 0.119.')


# ---- 6.6 BLEU-2 ----
def f6():
    cand = ['the', 'cat', 'sat', 'on', 'the', 'mat']
    ref = ['the', 'cat', 'is', 'on', 'the', 'mat']
    x0, cw = 130, 86
    o = [T(x0 - 14, 46, 'candidate', 13, 'end', MUT), T(x0 - 14, 106, 'reference', 13, 'end', MUT)]
    for i, (a, b) in enumerate(zip(cand, ref)):
        x = x0 + i * cw
        ok = a != 'sat'
        o.append(R(x + 4, 24, cw - 8, 34, ACS if ok else NXS, AC if ok else NX, 6, 1.6)); o.append(TM(x + cw / 2, 46, a, 15, bold=True))
        o.append(R(x + 4, 84, cw - 8, 34, PANEL, L2, 6, 1.2)); o.append(TM(x + cw / 2, 106, b, 15))
    # bigrams
    bg = [('the cat', 1), ('cat sat', 0), ('sat on', 0), ('on the', 1), ('the mat', 1)]
    o.append(T(x0 - 14, 162, 'bigrams', 13, 'end', MUT))
    for i, (b, ok) in enumerate(bg):
        x = x0 + i * cw + cw / 2
        o.append(R(x + 4, 144, cw - 8, 30, ACS if ok else NXS, AC if ok else NX, 6, 1.4)); o.append(T(x + cw / 2, 164, b, 13, bold=True))
    y = 204
    o.append(boxt(20, y, 160, 56, ['p₁ = 5 ÷ 6', '= 0.8333'], ACS, AC, 14, True))
    o.append(boxt(195, y, 160, 56, ['p₂ = 3 ÷ 5', '= 0.6'], ACS, AC, 14, True))
    o.append(boxt(370, y, 130, 56, ['c = r = 6', 'BP = 1'], PANEL, AC, 14, True))
    o.append(boxt(515, y, 190, 56, ['BLEU-2 = √(0.8333 × 0.6)', '= 0.7071'], NXS, NX, 14, True))
    o.append(T(20, y + 82, 'shaded = found in the reference (clipped); the two precisions are multiplied, then square-rooted', 13, 'start', MUT))
    return y + 96, ''.join(o)
FIG[6] = (f6, 'Candidate against reference: 5 of 6 words and 3 of 5 word pairs are found in the reference, and the lengths are equal, so BP = 1 and BLEU-2 = √(0.8333 × 0.6) = 0.7071.',
          'The candidate the cat sat on the mat above the reference the cat is on the mat, matched words shaded and sat marked; five bigrams below with the cat, on the and the mat matched; boxes give p1, p2, BP and BLEU-2 0.7071.')
AFTER[6] = 3
TEXT[6] = [('made this parallel and strong. The figure shows the pipeline.', 'made this parallel and strong.')]


# ---- 6.7 exact match against token F1 ----
def f7():
    o = []
    o.append(T(140, 50, 'predicted', 14, 'end', MUT)); o.append(T(140, 120, 'gold', 14, 'end', MUT))
    o.append(R(160, 28, 110, 36, PANEL, L2, 6, 1.5)); o.append(TM(215, 52, 'the', 16, bold=True))
    o.append(R(280, 28, 110, 36, ACS, AC, 6, 2)); o.append(TM(335, 52, 'cat', 16, bold=True))
    o.append(R(280, 98, 110, 36, ACS, AC, 6, 2)); o.append(TM(335, 122, 'cat', 16, bold=True))
    o.append(L(335, 66, 335, 96, AC, 2.5))
    o.append(T(345, 86, 'shared: 1', 13, 'start', AC, True))
    o.append(T(215, 86, 'extra', 13, fill=MUT))
    o.append(boxt(440, 28, 260, 106, ['"the cat" ≠ "cat"', 'exact match = 0'], NXS, NX, 15, True))
    y = 170
    for i, (lab, f, v) in enumerate([('precision', '1 shared ÷ 2 predicted', 0.5), ('recall', '1 shared ÷ 1 gold', 1.0), ('F1', '2 × 0.5 × 1.0 ÷ 1.5', 0.667)]):
        yy = y + i * 44
        o.append(T(110, yy + 20, lab, 14, 'end', INK, True))
        o.append(R(120, yy, 300 * v, 28, ACS, AC, 4, 1.5))
        o.append(T(130 + 300 * v, yy + 20, f'{v:.1f}' if v != 0.667 else '0.667', 14, 'start', AC, True))
        o.append(T(470, yy + 20, f, 13, 'start', MUT))
    return y + 140, ''.join(o)
FIG[7] = (f7, 'The predicted span the cat and the gold answer cat share one token. Exact match is 0 because the strings differ, while token F1 gives partial credit: precision 0.5, recall 1.0, F1 0.667.',
          'The predicted tokens the and cat above the gold token cat, with cat linked as shared; exact match 0; bars for precision 0.5, recall 1.0 and F1 0.667.')
AFTER[7] = 3


# ---- 6.8 inverted index and TF-IDF ranking ----
def f8():
    o = [T(20, 24, 'Query: neural network.  N = 3 documents', 15, 'start', INK, True)]
    terms = [('neural', 'df 2, idf 0.1761', 80), ('network', 'df 1, idf 0.4771', 170)]
    docs = [('d1', 'neural network model', 60, 0.6532), ('d2', 'neural machine translation', 150, 0.1761), ('d3', 'cricket match', 240, 0.0)]
    for t, s, y in terms:
        o.append(boxt(20, y - 26, 170, 52, [t, s], ACS, AC, 14, True))
    for d, txt, y, sc in docs:
        o.append(boxt(330, y - 24, 200, 48, [d, txt], PANEL, L2 if not sc else AC, 13, True))
    for (ty, dy) in [(80, 60), (80, 150), (170, 60)]:
        o.append(L(194, ty, 326, dy, AC, 2, arrow='n'))
        o.append(Tb(194 + 0.72 * 132, ty + 0.72 * (dy - ty) - 4, 'tf 1', 12, fill=MUT))
    o.append(T(560, 32, 'score', 14, 'start', MUT, True))
    for d, txt, y, sc in docs:
        o.append(R(560, y - 12, max(sc * 200, 2), 24, NXS if d == 'd1' else ACS, NX if d == 'd1' else AC, 4, 1.5))
    o.append(T(560, 60 + 34, '0.1761 + 0.4771 = 0.6532', 12, 'start', NX, True))
    o.append(T(560 + 0.1761 * 200 + 8, 150 + 5, '0.1761', 13, 'start', INK, True))
    o.append(T(568, 240 + 5, '0', 13, 'start', MUT, True))
    o.append(T(20, 296, 'Ranking: d1 (0.6532), d2 (0.1761), d3 (0). The rarer term network carries most of the weight.', 14, 'start'))
    return 310, ''.join(o)
FIG[8] = (f8, 'Each query term points to the documents that contain it. network is in one document, so its idf (0.4771) is larger than that of neural (0.1761); d1 holds both terms and ranks first at 0.6532.',
          'The query terms neural and network with their df and idf, arrows to the documents that contain them, and score bars: d1 0.6532, d2 0.1761, d3 0.')


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
