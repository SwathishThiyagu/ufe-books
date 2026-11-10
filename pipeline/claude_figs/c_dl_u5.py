"""Claude's hand-drawn figures for c-dl-u5 (Deep Learning, unit 5: attention, transformers and large language models),
one per chapter, from each chapter's worked example."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def grid(x, y, rows, title, c=AC, fill=ACS, cw=62, ch=34, hot=None, size=14):
    """a small matrix drawn as cells, with its name above"""
    o = [T(x + cw * len(rows[0]) / 2, y - 10, title, 13, fill=c, bold=True)]
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            f = fill if (hot is None or (i, j) in hot) else PANEL
            o.append(R(x + j * cw, y + i * ch, cw, ch, f, c, 0, 1.4))
            o.append(T(x + j * cw + cw / 2, y + i * ch + ch / 2 + 5, v, size))
    return ''.join(o)


# ---- 5.1 attention as a soft lookup ----
def f1():
    o = [T(20, 26, 'Query q = [1, 0] scores each key, softmax turns scores into weights, weights mix the values', 14, 'start', bold=True)]
    rows = [('k₁ = [1, 0]', '1', 0.4223, 'v₁ = [10, 0]', '[4.2232, 0]'),
            ('k₂ = [0, 1]', '0', 0.1554, 'v₂ = [0, 10]', '[0, 1.5536]'),
            ('k₃ = [1, 1]', '1', 0.4223, 'v₃ = [5, 5]', '[2.1116, 2.1116]')]
    cols = [(80, 'key'), (190, 'score q·k'), (300, 'weight α'), (470, 'value'), (620, 'α × value')]
    for x, h in cols:
        o.append(T(x, 62, h, 13, fill=MUT, bold=True))
    for i, (k, sc, a, v, av) in enumerate(rows):
        y = 76 + i * 50
        hot = a > 0.3
        o.append(R(20, y, 680, 42, PANEL, LN, 6, 1))
        o.append(TM(80, y + 27, k, 14, fill=AC, bold=True))
        o.append(T(190, y + 27, sc, 15, bold=True))
        o.append(R(250, y + 10, a * 200, 22, LVS if hot else ACS, LV if hot else AC, 3, 1.5))
        o.append(T(258 + a * 200, y + 27, f'{a:.3f}', 14, 'start', LV if hot else AC, True))
        o.append(TM(470, y + 27, v, 14, fill=NX, bold=True))
        o.append(T(620, y + 27, av, 14))
    o.append(T(300, 252, 'e¹ = 2.718, e⁰ = 1, sum 6.436', 13, fill=MUT))
    o.append(L(620, 236, 620, 262, NX, 2.2, arrow='x'))
    o.append(boxt(510, 268, 200, 52, ['context c = sum of rows', '= [6.335, 3.665]'], NXS, NX, 14, bold_first=True))
    o.append(T(20, 300, 'k₁ and k₃ tie at score 1,', 13, 'start', LV, True))
    o.append(T(20, 318, 'so v₁ and v₃ supply most of c.', 13, 'start', LV, True))
    return 336, ''.join(o)
FIG[1] = (f1, 'The query scores the three keys 1, 0 and 1, softmax turns those into weights 0.422, 0.155 and 0.422, and the weighted values add up to the context c = [6.335, 3.665].',
          'A table of three keys with scores 1, 0, 1, weight bars 0.422, 0.155, 0.422, their values, and the weighted values summing to the context vector [6.335, 3.665].')


# ---- 5.2 scaled dot-product self-attention on two tokens ----
def f2():
    o = [T(20, 26, 'x₁ = [1, 0], x₂ = [0, 1], W_Q = W_K = W_V = I, so Q = K = V = X and d_k = 2', 14, 'start', bold=True)]
    y = 80
    o.append(grid(20, y, [['1', '0'], ['0', '1']], 'scores QKᵀ', AC, ACS, 52))
    o.append(grid(196, y, [['0.7071', '0'], ['0', '0.7071']], 'scaled', AC, ACS, 66))
    o.append(grid(400, y, [['0.6698', '0.3302'], ['0.3302', '0.6698']], 'weights', LV, LVS, 66))
    o.append(grid(588, y, [['0.6698', '0.3302'], ['0.3302', '0.6698']], 'output = weights × V', NX, NXS, 62))
    for xa, xb, lab in ((124, 192, '÷ √2'), (332, 396, 'softmax'), (532, 584, '× V')):
        o.append(L(xa + 2, y + 34, xb - 4, y + 34, AC, 2.2, arrow='n'))
        o.append(T((xa + xb) / 2, y + 26, lab, 13, fill=INK, bold=True))
    o.append(T(196 + 66, y + 92, '√2 = 1.4142', 13, fill=MUT))
    o.append(T(400 + 66, y + 92, 'row 1: e^0.7071 = 2.0281, sum 3.0281', 13, fill=MUT))
    # the dashed branch without scaling
    yb = y + 140
    o.append(P([(72, y + 70), (72, yb + 24), (396, yb + 24)], LV, 2, '6 4'))
    o.append(L(380, yb + 24, 396, yb + 24, LV, 2, arrow='l'))
    o.append(T(80, yb + 14, 'skip the ÷ √2: softmax of row 1 = [1, 0] directly', 13, 'start', LV, True))
    o.append(R(400, yb + 6, 132, 36, PANEL, LV, 0, 1.6, '6 4'))
    o.append(T(433, yb + 29, '0.7311', 14)); o.append(T(499, yb + 29, '0.2689', 14))
    o.append(L(466, yb + 6, 466, yb + 42, LV, 1.2, '6 4'))
    o.append(T(544, yb + 22, 'sharper than', 13, 'start', LV, True))
    o.append(T(544, yb + 40, '0.6698, 0.3302', 13, 'start', LV, True))
    return yb + 60, ''.join(o)
FIG[2] = (f2, 'Two tokens through scaled dot-product attention: the scores 1 and 0 are divided by √2, softmaxed to 0.6698 and 0.3302, and used to mix the value rows. Dropping the √d_k step, the dashed branch, makes row 1 sharper at 0.7311 and 0.2689.',
          'Four 2×2 matrices left to right: scores QKᵀ, the scaled scores 0.7071, the softmax weights 0.6698 and 0.3302, and the output rows, with a dashed branch showing row 1 without scaling as 0.7311 and 0.2689.')


# ---- 5.3 loss is −ln p: masked word and GPT perplexity on one curve ----
def f3():
    x0, x1, y0, y1 = 80, 640, 40, 300
    fx = lambda p: x0 + p * (x1 - x0)
    fy = lambda l: y1 - l / 3 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [0, 0.25, 0.5, 0.75, 1.0], [0, 1, 2, 3], fx, fy,
              'probability p given to the true token', 'loss −ln p (nats)')]
    pts = [(p, -math.log(p)) for p in [0.05 + i * 0.0095 for i in range(101)]]
    o.append(P([(fx(p), fy(l)) for p, l in pts], AC, 3))
    o.append(T(fx(0.11), fy(2.6), 'loss = −ln p', 14, 'start', AC, True))
    # BERT point
    o.append(L(fx(0.5), y1, fx(0.5), fy(0.6931), LV, 1.4, '4 3'))
    o.append(C(fx(0.5), fy(0.6931), 7, LV))
    o.append(T(fx(0.5) + 14, fy(0.6931) - 30, 'BERT, masked word ‘mat’, p = 0.5', 13, 'start', LV, True))
    o.append(T(fx(0.5) + 14, fy(0.6931) - 12, 'loss 0.6931 nats = 1.0 bit', 13, 'start', LV, True))
    # GPT point
    o.append(L(fx(0.25), y1, fx(0.25), fy(1.3863), NX, 1.4, '4 3'))
    o.append(L(x0, fy(1.3863), fx(0.25), fy(1.3863), NX, 1.4, '4 3'))
    o.append(C(fx(0.25), fy(1.3863), 7, NX))
    o.append(T(fx(0.25) + 14, fy(1.3863) - 26, 'GPT, mean p = (0.5 × 0.25 × 0.125)^⅓ = 0.25', 13, 'start', NX, True))
    o.append(T(fx(0.25) + 14, fy(1.3863) - 8, 'loss 1.386 nats, perplexity 1 ÷ 0.25 = 4.0', 13, 'start', NX, True))
    return 360, ''.join(o)
FIG[3] = (f3, 'Both halves of the example sit on the curve loss = −ln p. The masked word at p = 0.5 costs 0.6931 nats, which is 1 bit; the GPT sequence’s mean probability 0.25 costs 1.386 nats, a perplexity of 1 ÷ 0.25 = 4.',
          'The curve loss = −ln p from p = 0.05 to 1, with a point at p = 0.5, loss 0.6931 for the BERT masked word, and a point at p = 0.25, loss 1.386, perplexity 4, for the GPT sequence.')


# ---- 5.4 scaling curve with diminishing returns ----
def f4():
    x0, x1, y0, y1 = 80, 640, 40, 290
    fx = lambda c: x0 + c / 100 * (x1 - x0)
    fy = lambda l: y1 - (l - 1.8) / 1.6 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [0, 16, 40, 60, 81, 100], [1.8, 2.2, 2.6, 3.0, 3.4], fx, fy,
              'training compute C (units)', 'test loss L', yfmt=lambda v: f'{v:.1f}')]
    lf = lambda c: 2.0 + 1.2 * c ** -0.25
    o.append(L(x0, fy(2.0), x1, fy(2.0), L2, 1.6, '6 4'))
    o.append(T(x1 - 4, fy(2.0) + 18, 'floor L = 2.0, never reached', 13, 'end', MUT, True))
    o.append(P([(fx(c), fy(lf(c))) for c in [1 + i * 0.99 for i in range(101)]], AC, 3))
    o.append(T(fx(30), fy(2.95), 'L = 2.0 + 1.2 C^−0.25', 14, 'start', AC, True))
    for c, l, col in ((1, 3.2, MUT), (16, 2.6, LV), (81, 2.4, NX)):
        o.append(C(fx(c), fy(l), 7, col))
    o.append(T(fx(1) + 14, fy(3.2) + 5, 'C = 1: L = 3.2', 13, 'start', MUT, True))
    o.append(T(fx(16) + 12, fy(2.6) - 12, 'C = 16: 16^0.25 = 2, L = 2.0 + 0.6 = 2.6', 13, 'start', LV, True))
    o.append(T(fx(81), fy(2.4) - 16, 'C = 81: L = 2.4', 13, 'middle', NX, True))
    o.append(T(fx(50), fy(2.3) + 4, '5× more compute after C = 16 buys only 0.2 less loss', 13, 'middle', INK, True))
    return 350, ''.join(o)
FIG[4] = (f4, 'The fitted scaling curve falls steeply and then flattens: at C = 16 it gives L = 2.6, the value from part (c) of the example, yet five times more compute, C = 81, lowers it only to 2.4.',
          'The curve L = 2.0 + 1.2 C^−0.25 for C from 1 to 100, falling from 3.2 at C = 1 to 2.6 at C = 16 and 2.4 at C = 81, above a dashed floor at 2.0.')


# ---- 5.5 reward model pair loss, then PPO with a KL leash ----
def f5():
    o = []
    def row(y, title, c, boxes):
        o.append(T(20, y - 14, title, 14, 'start', c, True))
        x = 10
        for i, (w, lines, hot) in enumerate(boxes):
            o.append(boxt(x, y, w, 58, lines, NXS if hot else PANEL, NX if hot else c, 14, bold_first=True))
            if i < len(boxes) - 1:
                o.append(L(x + w + 3, y + 29, x + w + 25, y + 29, AC, 2.2, arrow='n'))
            x += w + 30
    row(52, 'Stage 2: reward model on one human-ranked pair (A preferred)', AC,
        [(130, ['scores', 'r(A) 2.0, r(B) 1.0'], False), (120, ['gap d', '2.0 − 1.0 = 1.0'], False),
         (190, ['P(A beats B)', '1 ÷ (1 + e^−1) = 0.731'], False), (160, ['pair loss', '−ln 0.731 = 0.313'], True)])
    row(190, 'Stage 3: one PPO step with β = 0.1', LV,
        [(160, ['reward', 'r = 2.0'], False), (220, ['KL penalty', 'β × KL = 0.1 × 0.5 = 0.05'], False),
         (190, ['objective', '2.0 − 0.05 = 1.95'], True)])
    o.append(T(20, 286, 'The penalty keeps the tuned model near the reference: a larger KL would cost more reward.', 13, 'start', MUT))
    return 302, ''.join(o)
FIG[5] = (f5, 'A score gap of 1.0 gives a preference probability of 0.731 and a pair loss of 0.313 nats; in the PPO step the KL penalty 0.1 × 0.5 = 0.05 turns the reward 2.0 into an objective of 1.95. The two green boxes are the answers.',
          'Two rows of boxes: scores 2.0 and 1.0, gap 1.0, probability 0.731 and pair loss 0.313 for the reward model; then reward 2.0, KL penalty 0.05 and objective 1.95 for the PPO step.')


# ---- 5.6 temperature and top-p on three tokens ----
def f6():
    o = [T(20, 26, 'Logits z = [2, 1, 0] for tokens t₁, t₂, t₃', 14, 'start', bold=True)]
    yb = 236
    panels = [('T = 1', [0.665, 0.245, 0.090], AC, ACS, None),
              ('T = 0.5 (logits doubled to 4, 2, 0)', [0.867, 0.117, 0.016], LV, LVS, None),
              ('top-p = 0.9 at T = 1', [0.731, 0.269, 0.0], NX, NXS, True)]
    for k, (title, ps, c, cs, nuc) in enumerate(panels):
        x0 = 20 + k * 236
        o.append(T(x0 + 100, 62, title, 13, fill=c, bold=True))
        o.append(L(x0, yb, x0 + 200, yb, L2, 1.5))
        for i, p in enumerate(ps):
            x = x0 + 12 + i * 64
            h = p * 150
            if nuc and i == 2:
                o.append(R(x, yb - 0.090 * 150, 48, 0.090 * 150, PANEL, L2, 2, 1.4, '4 3'))
                o.append(L(x + 4, yb - 20, x + 44, yb + 4, LV, 2.2)); o.append(L(x + 44, yb - 20, x + 4, yb + 4, LV, 2.2))
                o.append(T(x + 24, yb - 26, 'dropped', 13, fill=LV, bold=True))
            else:
                o.append(R(x, yb - h, 48, h, cs, c, 2, 1.6))
                o.append(T(x + 24, yb - h - 8, f'{p:.3f}', 13, fill=c, bold=True))
            o.append(T(x + 24, yb + 20, f't{"₁₂₃"[i]}', 14, fill=MUT, bold=True))
    o.append(T(20, yb + 52, 'Lower T sharpens: the top token rises from 0.665 to 0.867.', 13, 'start', LV, True))
    o.append(T(20, yb + 72, 'Top-p: running total 0.665, then 0.910 ≥ 0.9, so keep t₁ and t₂ and divide by 0.910: 0.731 and 0.269.', 13, 'start', NX, True))
    return yb + 90, ''.join(o)
FIG[6] = (f6, 'The same three tokens at T = 1 and T = 0.5: halving the temperature sharpens the top probability from 0.665 to 0.867. With top-p = 0.9 the running total 0.910 crosses 0.9, so t₃ is dropped and the other two renormalise to 0.731 and 0.269.',
          'Three bar charts: probabilities 0.665, 0.245, 0.090 at T = 1; 0.867, 0.117, 0.016 at T = 0.5; and the top-p nucleus 0.731, 0.269 with the third token crossed out.')


# ---- 7 quantization FP32 to INT8 ----
def f7():
    o = [T(20, 26, 'Symmetric INT8: s = max|x| ÷ 127 = 0.9 ÷ 127 = 0.0070866, zero point 0', 14, 'start', bold=True)]
    head = ['FP32 weight x', 'x ÷ s', 'code q = round', 'back x̂ = q × s', 'error']
    xs = [80, 210, 330, 470, 610]
    for x, h in zip(xs, head):
        o.append(T(x, 62, h, 13, fill=MUT, bold=True))
    rows = [('−0.9', '−127.0', '−127', '−0.9000', '0.0000'), ('0.1', '14.11', '14', '0.0992', '0.0008'),
            ('0.7', '98.78', '99', '0.7016', '0.0016'), ('0.0', '0.0', '0', '0.0000', '0.0000')]
    for i, r in enumerate(rows):
        y = 74 + i * 42
        hot = i == 2
        o.append(R(20, y, 680, 36, LVS if hot else PANEL, LV if hot else LN, 6, 1.6 if hot else 1))
        for j, (x, v) in enumerate(zip(xs, r)):
            o.append(T(x, y + 24, v, 14, fill=(AC if j == 2 else (LV if hot and j == 4 else INK)), bold=j in (2, 4)))
    o.append(T(610, 260, 'largest error 0.0016', 13, fill=LV, bold=True))
    # storage bars
    y = 282
    o.append(T(20, y, 'Storage for the four weights', 14, 'start', bold=True))
    o.append(R(20, y + 12, 512, 26, ACS, AC, 3, 1.6)); o.append(T(30, y + 30, 'FP32: 4 × 32 = 128 bits', 13, 'start', AC, True))
    o.append(R(20, y + 46, 128, 26, NXS, NX, 3, 1.6)); o.append(T(158, y + 64, 'INT8: 4 × 8 = 32 bits, 4× smaller', 13, 'start', NX, True))
    return y + 86, ''.join(o)
FIG[7] = (f7, 'Four FP32 weights become the INT8 codes −127, 14, 99 and 0 with scale s = 0.9 ÷ 127, and turn back into values no more than 0.0016 away, while storage drops 4× from 128 bits to 32.',
          'A table of the four weights −0.9, 0.1, 0.7 and 0.0 with x ÷ s, the INT8 codes −127, 14, 99, 0, the dequantized values and errors, the 0.0016 row highlighted, and two storage bars of 128 and 32 bits.')


spec = make_spec(FIG)
