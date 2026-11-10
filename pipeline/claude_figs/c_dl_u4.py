"""Claude's hand-drawn figures for c-dl-u4 (Deep Learning, unit 4: sequence models), one per chapter, from each chapter's
worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def node(x, y, s, c=AC, fill=ACS, w=96, h=50, sub=None):
    o = [R(x - w / 2, y - h / 2, w, h, fill, c, 10, 2), T(x, y + (5 if not sub else -3), s, 15, bold=True)]
    if sub: o.append(T(x, y + 15, sub, 13, fill=c, bold=True))
    return ''.join(o)


# ---- 4.1 sliding windows over a series ----
def f1():
    xs = [2, 4, 6, 8, 10]
    o = [T(20, 26, 'Series x at t = 1 … 5, window length 3', 14, 'start', bold=True)]
    x0, cw, y = 90, 100, 70
    for i, v in enumerate(xs):
        x = x0 + i * cw
        o.append(R(x, y, 80, 50, PANEL, L2, 6, 1.6))
        o.append(T(x + 40, y + 32, str(v), 18, bold=True))
        o.append(T(x + 40, y - 8, f't = {i + 1}', 13, fill=MUT))
    def win(row, a, c, cs, label):
        yy = y + 80 + row * 90
        o.append(R(x0 + a * cw - 6, yy, 3 * cw - 8, 40, cs, c, 8, 2))
        o.append(T(x0 + a * cw + 1.5 * cw - 10, yy + 26, label, 14, fill=c, bold=True))
        tx = x0 + (a + 3) * cw + 40
        o.append(L(x0 + (a + 3) * cw - 10, yy + 20, tx - 26, yy + 20, c, 2.5, arrow='n' if c == AC else 'x'))
        o.append(R(tx - 22, yy, 44, 40, cs, c, 8, 2)); o.append(T(tx, yy + 26, str(xs[a + 3]), 16, fill=c, bold=True))
        o.append(L(tx, yy - 2, tx, y + 54, c, 1.4, '3 3'))
    win(0, 0, AC, ACS, 'input [2, 4, 6]')
    win(1, 1, NX, NXS, 'input [4, 6, 8]')
    o.append(T(20, 150, 'pair 1', 13, 'start', AC, True)); o.append(T(20, 240, 'pair 2', 13, 'start', NX, True))
    o.append(T(360, 310, 'A third window would need x₆, which does not exist: N − w = 5 − 3 = 2 pairs.', 14, bold=True))
    return 326, ''.join(o)
FIG[1] = (f1, 'A window of 3 values predicts the next one: [2, 4, 6] → 8, then one step later [4, 6, 8] → 10. Five values give only 5 − 3 = 2 pairs.',
          'The series 2, 4, 6, 8, 10 in five cells, with two overlapping windows of three values below it, each pointing at its target 8 and 10.')


# ---- 4.2 RNN unfolded for two steps ----
def f2():
    o = []
    yh, yx, yy = 150, 280, 40
    o.append(node(80, yh, 'h₀ = 0', L2, PANEL))
    o.append(node(330, yh, 'h₁ = 0.76', AC, ACS, 120))
    o.append(node(590, yh, 'h₂ = 0.98', AC, ACS, 120))
    o.append(node(330, yx, 'x₁ = 1', L2, PANEL)); o.append(node(590, yx, 'x₂ = 2', L2, PANEL))
    o.append(node(590, yy, 'y₂ = 0.98', NX, NXS, 120))
    for xa, xb in ((128, 270), (390, 530)):
        o.append(L(xa, yh, xb - 4, yh, LV, 2.5, arrow='l')); o.append(Tb((xa + xb) / 2, yh - 12, '× 0.5 (W_hh)', 13, fill=LV, bold=True))
    for x in (330, 590):
        o.append(L(x, yx - 25, x, yh + 29, AC, 2.2, arrow='n')); o.append(T(x + 8, (yx + yh) / 2 + 30, '× 1', 13, 'start', AC, True))
    o.append(L(590, yh - 25, 590, yy + 29, NX, 2.2, arrow='x')); o.append(T(598, 102, '× 1', 13, 'start', NX, True))
    o.append(T(318, 206, 'tanh(1 × 1 + 0.5 × 0)', 13, 'end', MUT)); o.append(T(318, 222, '= tanh(1.000)', 13, 'end', MUT))
    o.append(T(578, 206, 'tanh(1 × 2 + 0.5 × 0.76)', 13, 'end', MUT)); o.append(T(578, 222, '= tanh(2.381)', 13, 'end', MUT))
    o.append(T(20, 336, 'Both orange arrows are the same weight W_hh = 0.5, so the second step adds no new parameters.', 13, 'start', LV, True))
    return 352, ''.join(o)
FIG[2] = (f2, 'Unfolded for two steps, h₁ = tanh(1) = 0.76 and h₂ = tanh(2 + 0.5 × 0.76) = 0.98, which is also the output y₂. The two orange arrows share one recurrent weight, 0.5.',
          'Two unfolded RNN steps: h₀ = 0 and x₁ = 1 give h₁ = 0.76, then h₁ and x₂ = 2 give h₂ = 0.98 and output y₂ = 0.98, with the shared recurrent weight 0.5 on both horizontal arrows.')


# ---- 4.3 BPTT: two paths into the shared weight ----
def f3():
    o = []
    y = 120
    o.append(node(70, y, 'h₀', L2, PANEL, 80, 50, '0.2'))
    o.append(node(250, y, 'h₁', AC, ACS, 90, 50, '0.604'))
    o.append(node(450, y, 'h₂', AC, ACS, 90, 50, '0.802'))
    o.append(node(640, y, 'L', LV, LVS, 90, 50, '0.020'))
    o.append(L(110, y, 202, y, AC, 2.4, arrow='n')); o.append(Tb(156, y - 12, 'u = 1', 13, fill=AC, bold=True))
    o.append(L(295, y, 402, y, AC, 2.4, arrow='n')); o.append(Tb(348, y - 12, 'u = 1', 13, fill=AC, bold=True))
    o.append(L(495, y, 592, y, AC, 2.4, arrow='n')); o.append(Tb(544, y - 12, '½(h₂ − 1)²', 13, fill=MUT))
    o.append(T(20, 40, 'forward: h = tanh(0.5 + u × previous h)', 14, 'start', AC, True))
    o.append(T(250, 74, 'x₁ = 0.5', 13, fill=MUT)); o.append(T(450, 74, 'x₂ = 0.5', 13, fill=MUT))
    # backward paths, both bulging below the chain
    o.append(arc(630, y + 26, 462, y + 26, 0.3, LV, 2.4, 'l', '6 4'))
    o.append(arc(640, y + 30, 262, y + 30, 0.3, NX, 2.4, 'x', '2 4'))
    o.append(T(545, y + 132, 'direct path: u in the h₁ → h₂ step', 13, fill=LV, bold=True))
    o.append(T(545, y + 150, '−0.198 × 0.357 × 0.604 = −0.043', 13, fill=LV))
    o.append(T(200, y + 132, 'through h₁: u in the h₀ → h₁ step', 13, fill=NX, bold=True))
    o.append(T(200, y + 150, '−0.198 × 0.357 × 1 × 0.127 = −0.009', 13, fill=NX))
    o.append(boxt(235, y + 172, 250, 50, ['∂L/∂u = −0.043 − 0.009', '= −0.052'], PANEL, INK, 14, bold_first=True))
    return y + 236, ''.join(o)
FIG[3] = (f3, 'The same weight u is used in both steps, so its gradient has two parts: −0.043 from its use in the step into h₂, and −0.009 from its use in the step into h₁, carried back through h₂. Together ∂L/∂u = −0.052.',
          'A chain h₀ = 0.2, h₁ = 0.604, h₂ = 0.802 and loss L = 0.020 with u = 1 on both steps, and two dashed backward paths giving −0.043 and −0.009.')


# ---- 4.4 one LSTM cell update ----
def f4():
    o = []
    yc = 70
    o.append(T(20, 30, 'cell state line', 13, 'start', MUT))
    o.append(node(70, yc, 'c(t−1)', L2, PANEL, 90, 46, '0.500'))
    o.append(L(115, yc, 640, yc, AC, 3))
    def op(x, s, c=AC):
        o.append(f'<circle cx="{x}" cy="{yc}" r="18" style="fill:var(--fig);stroke:{c};stroke-width:2.2"/>')
        o.append(T(x, yc + 7, s, 20, fill=c, bold=True))
    op(220, '×', LV); op(420, '+', AC)
    o.append(T(320, yc - 12, '0.3655', 13, fill=LV, bold=True))
    o.append(node(220, 180, 'forget f', LV, LVS, 110, 46, '0.731'))
    o.append(L(220, 157, 220, yc + 20, LV, 2.2, arrow='l'))
    o.append(T(232, 120, '0.731 × 0.5', 13, 'start', LV))
    o.append(node(380, 250, 'input i', NX, NXS, 100, 46, '0.622'))
    o.append(node(500, 250, 'candidate', NX, NXS, 110, 46, '0.762'))
    o.append(f'<circle cx="440" cy="170" r="16" style="fill:var(--fig);stroke:var(--next);stroke-width:2"/>'); o.append(T(440, 177, '×', 18, fill=NX, bold=True))
    o.append(L(390, 227, 430, 184, NX, 2, arrow='x')); o.append(L(490, 227, 452, 184, NX, 2, arrow='x'))
    o.append(L(436, 154, 424, yc + 20, NX, 2.2, arrow='x'))
    o.append(T(452, 130, '0.4740', 13, 'start', NX, True))
    o.append(node(660, yc, 'c(t)', AC, ACS, 80, 46, '0.839'))
    o.append(L(660, yc + 23, 660, 150, AC, 2, arrow='n'))
    o.append(boxt(610, 152, 100, 34, ['tanh → 0.686'], PANEL, AC, 13))
    o.append(L(660, 186, 660, 222, AC, 2, arrow='n'))
    o.append(f'<circle cx="660" cy="240" r="16" style="fill:var(--fig);stroke:var(--accent);stroke-width:2"/>'); o.append(T(660, 247, '×', 18, fill=AC, bold=True))
    o.append(node(660, 320, 'h(t)', AC, ACS, 80, 46, '0.343'))
    o.append(L(660, 256, 660, 294, AC, 2, arrow='n'))
    o.append(T(632, 244, 'output o = 0.5', 13, 'end', AC, True))
    o.append(T(20, 330, 'c(t) = 0.3655 + 0.4740 = 0.839', 14, 'start', bold=True))
    o.append(T(20, 352, 'h(t) = 0.5 × tanh(0.839) = 0.5 × 0.686 = 0.343', 14, 'start', bold=True))
    return 368, ''.join(o)
FIG[4] = (f4, 'Along the cell-state line the forget gate keeps 0.731 × 0.5 = 0.3655 of the old state and the input gate adds 0.622 × 0.762 = 0.474, so c(t) = 0.839. The output gate then lets 0.5 × tanh(0.839) = 0.343 out as h(t).',
          'An LSTM cell drawn as a cell-state line from c(t−1) = 0.5 through a forget multiply and an add to c(t) = 0.839, with the input gate and candidate feeding the add, and tanh and the output gate giving h(t) = 0.343.')


# ---- 4.5 greedy decoding ----
def f5():
    o = [T(20, 26, 'Decoder from context c = [1, 0]: take the largest logit at each step', 14, 'start', bold=True)]
    vocab = ['a', 'b', 'c', 'end']
    steps = [[2, 1, 0, -1], [0, 1, 2, -1]]
    yb = 180
    for s, lg in enumerate(steps):
        x0 = 40 + s * 360
        o.append(T(x0, 60, f'step {s + 1}' + (': fed a' if s else ''), 14, 'start', bold=True))
        o.append(L(x0, yb, x0 + 280, yb, L2, 1.5))
        best = lg.index(max(lg))
        for i, v in enumerate(lg):
            x = x0 + 14 + i * 68
            h = v * 40
            hot = i == best
            o.append(R(x, yb - max(h, 0), 46, abs(h) if v else 2, LVS if hot else ACS, LV if hot else AC, 2, 1.6))
            o.append(T(x + 23, yb - max(h, 0) - 8 if v >= 0 else yb - h + 18, neg(v), 13, bold=True, fill=LV if hot else INK))
            o.append(TM(x + 23, yb + 82, vocab[i], 15, bold=hot, fill=LV if hot else MUT))
            o.append(T(x + 23, yb + 100, f'index {i}', 13, fill=MUT))
    o.append(L(326, 104, 392, 104, LV, 2.2, '6 4', arrow='l'))
    o.append(T(360, 92, 'feed a', 13, fill=LV, bold=True))
    o.append(T(360, yb + 140, 'Output: [a, c], token indices [0, 2]', 16, bold=True, fill=LV))
    return yb + 158, ''.join(o)
FIG[5] = (f5, 'Greedy decoding picks the largest logit each time: at step 1 that is a (index 0); a is fed back, and at step 2 the largest is c (index 2). The output is [a, c].',
          'Two bar charts of logits over the tokens a, b, c and end: step 1 with a highest at 2, step 2 with c highest at 2, and a dashed arrow feeding a back into step 2.')


# ---- 4.6 CBOW softmax over three words ----
def f6():
    cx, cy, s = 170, 170, 100
    o = [L(cx - 110, cy, cx + 140, cy, L2, 1.2), L(cx, cy - 130, cx, cy + 110, L2, 1.2)]
    vecs = [('cat', (1, 0), NX), ('dog', (0, 1), AC), ('fish', (-1, 0), LV)]
    for n, (a, b), c in vecs:
        o.append(L(cx, cy, cx + a * s * 0.97, cy - b * s * 0.97, c, 3, arrow={'cat': 'x', 'dog': 'n', 'fish': 'l'}[n]))
        o.append(T(cx + a * s + (14 if a > 0 else (-14 if a < 0 else 10)), cy - b * s + (5 if b == 0 else -6), f'v_{n}', 14, 'start' if a > 0 or a == 0 else 'end', c, True))
    o.append(L(cx, cy + 14, cx + s * 0.97, cy + 14, INK, 2, '5 4', arrow=None))
    o.append(T(cx + 50, cy + 34, 'h = [1, 0]', 14, fill=INK, bold=True))
    o.append(T(cx, 300, 'score = v · h', 13, fill=MUT))
    rows = [('cat', '1', '2.718', '0.665', NX), ('dog', '0', '1.000', '0.245', AC), ('fish', '−1', '0.368', '0.090', LV)]
    x0 = 360
    for j, h in enumerate(['word', 'score', 'exp', 'P(word | h)']):
        o.append(T(x0 + [30, 100, 170, 270][j], 50, h, 13, fill=MUT, bold=True))
    for i, (w, sc, e, p, c) in enumerate(rows):
        y = 66 + i * 44
        o.append(R(x0, y, 340, 38, PANEL, LN, 6, 1))
        o.append(TM(x0 + 30, y + 25, w, 14, fill=c, bold=True))
        o.append(T(x0 + 100, y + 25, sc, 14)); o.append(T(x0 + 170, y + 25, e, 14))
        o.append(R(x0 + 222, y + 8, float(p) * 100, 22, NXS if w == 'cat' else PANEL, c, 3, 1.4))
        o.append(T(x0 + 230 + float(p) * 100, y + 25, p, 14, 'start', c, True))
    o.append(T(x0, 222, 'Z = 2.718 + 1.000 + 0.368 = 4.086', 13, 'start'))
    o.append(T(x0, 246, 'P(cat | h) = 2.718 ÷ 4.086 = 0.665', 14, 'start', NX, True))
    o.append(T(x0, 270, 'h points at cat, so cat wins.', 13, 'start'))
    return 316, ''.join(o)
FIG[6] = (f6, 'Each word’s score is the dot product of its output vector with h = [1, 0]: cat 1, dog 0, fish −1. After exponentiating and dividing by Z = 4.086, cat, the true centre word, gets probability 0.665.',
          'Left, the output vectors of cat, dog and fish drawn from the origin with h = [1, 0] along cat; right, a table of scores, exponentials and softmax probabilities 0.665, 0.245 and 0.090.')


# ---- 4.7 language model: probability, loss and perplexity ----
def f7():
    words = [('the', '0.5', 0.6931, 'P(the)'), ('cat', '0.4', 0.9163, 'P(cat | the)'), ('sat', '0.2', 1.6094, 'P(sat | the cat)')]
    o = [T(20, 26, 'An RNN language model scores “the cat sat” one word at a time', 14, 'start', bold=True)]
    yb = 270
    for i, (w, p, l, lab) in enumerate(words):
        x = 60 + i * 170
        o.append(boxt(x, 44, 130, 40, [w], ACS, AC, 16, bold_first=True))
        o.append(T(x + 65, 104, f'{lab} = {p}', 13, fill=AC))
        h = l * 70
        o.append(R(x + 35, yb - h, 60, h, LVS, LV, 2, 1.6))
        o.append(T(x + 65, yb + 20, f'−ln {p} = {l:.3f}', 13, fill=LV, bold=True))
        if i < 2: o.append(L(x + 132, 64, x + 166, 64, AC, 2, arrow='n'))
    o.append(L(40, yb, 560, yb, L2, 1.5))
    ya = yb - 1.073 * 70
    o.append(L(40, ya, 560, ya, INK, 1.6, '6 4'))
    o.append(T(566, ya + 5, 'average 1.073', 13, 'start', bold=True))
    o.append(T(20, yb + 52, 'P(sentence) = 0.5 × 0.4 × 0.2 = 0.04', 14, 'start', AC, True))
    o.append(T(20, yb + 76, 'loss = (0.693 + 0.916 + 1.609) ÷ 3 = 1.073 nats per word', 14, 'start', LV, True))
    o.append(T(20, yb + 100, 'perplexity = e^1.073 = 2.92, as if choosing among about 3 words each time', 14, 'start', bold=True))
    return yb + 116, ''.join(o)
FIG[7] = (f7, 'The sentence probability is the product 0.5 × 0.4 × 0.2 = 0.04. Each word’s loss is −ln of its probability, the average is 1.073 nats, and the perplexity e^1.073 = 2.92.',
          'Three word boxes the, cat and sat with their probabilities 0.5, 0.4 and 0.2, above bars of their losses 0.693, 0.916 and 1.609 with a dashed average line at 1.073.')


spec = make_spec(FIG)
