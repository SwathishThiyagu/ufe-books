"""Claude's hand-drawn figures for c-ml-u1 (Machine Learning, unit 1: foundations), one per chapter, each drawn from
that chapter's worked example with its own numbers. text_fixes rewrites the two sentences that described an older or a
missing figure."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def tick(x, y, ok, s=22):
    """a small square with a tick (right) or a cross (wrong)"""
    c, f = (AC, ACS) if ok else (LV, LVS)
    o = R(x, y, s, s, f, c, 4, 1.6)
    if ok:
        o += P([(x + 5, y + s / 2), (x + s / 2 - 1, y + s - 6), (x + s - 5, y + 6)], c, 2.2)
    else:
        o += L(x + 6, y + 6, x + s - 6, y + s - 6, c, 2.2) + L(x + s - 6, y + 6, x + 6, y + s - 6, c, 2.2)
    return o


# ---- 1.1 train on 1000 emails, score on 10 test emails ----
def f1():
    o = [T(40, 24, 'Experience E trains the model; the test set only scores it', 15, 'start', bold=True)]
    o.append(boxt(30, 44, 190, 70, ['training set (E)', '1000 labelled emails', '200 spam, 800 not spam'], NXS, NX, 13))
    o.append(boxt(270, 52, 150, 54, ['learning', 'algorithm'], PANEL, L2, 14))
    o.append(boxt(470, 44, 220, 70, ['model', 'spam if “lottery”', 'appears 2 or more times'], ACS, AC, 13))
    o.append(L(222, 79, 266, 79, NX, 2.2, arrow='x'))
    o.append(L(422, 79, 466, 79, AC, 2.2, arrow='n'))
    o.append(L(580, 116, 580, 150, AC, 2.2, arrow='n'))
    o.append(T(590, 138, 'predict', 13, 'start', MUT))
    o.append(T(40, 176, 'test set: 10 emails the learner never saw', 14, 'start', bold=True))
    marks = [1, 1, 1, 0, 1, 1, 1, 1, 0, 1]
    for i, m in enumerate(marks):
        o.append(tick(330 + i * 34, 158, bool(m), 24))
    o.append(T(40, 228, 'P = accuracy = correct ÷ total = 8 ÷ 10 = 0.8 = 80%', 15, 'start', bold=True, fill=AC))
    o.append(T(40, 252, 'Two wrong labels out of ten. The training emails are never used to score the model.', 13, 'start', MUT))
    return 266, ''.join(o)
FIG[1] = (f1, 'The 1000 labelled emails are the experience E that trains the rule “spam if lottery appears 2 or more times”. The rule is then scored on 10 unseen emails: 8 right, so accuracy is 0.8, or 80%.',
          'Training set of 1000 emails flows to a learning algorithm and then to the model. The model labels 10 test emails, 8 shown with ticks and 2 with crosses, giving accuracy 8 out of 10, 80 percent.')


# ---- 1.2 six tasks sorted by the feedback they get ----
def f2():
    o = [T(40, 24, 'Sort a task by the feedback the learner gets', 15, 'start', bold=True)]
    cols = [(30, 'supervised', 'a label for each example', ACS, AC,
             [('1  house price from area', 'number: regression'), ('4  spam, 200 labelled', 'class: classification')]),
            (260, 'unsupervised', 'inputs only, no label', NXS, NX,
             [('2  group 500 customers', 'clustering by spend'), ('5  clusters in 1000 UPI', 'clustering, no labels')]),
            (490, 'reinforcement', 'a reward after actions', LVS, LV,
             [('3  robot exits a maze', 'reward +1 at the exit'), ('6  choose a cricket shot', 'reward = runs scored')])]
    for x, name, fb, f, c, items in cols:
        o.append(R(x, 42, 200, 236, 'none', c, 10, 2))
        o.append(T(x + 100, 68, name, 15, bold=True, fill=c))
        o.append(T(x + 100, 90, fb, 13, fill=MUT))
        for j, (a, b) in enumerate(items):
            y = 108 + j * 78
            o.append(R(x + 12, y, 176, 62, f, c, 8, 1.5))
            o.append(T(x + 22, y + 26, a, 13, 'start', bold=True))
            o.append(T(x + 22, y + 47, b, 13, 'start'))
    o.append(T(360, 304, 'Count: 2 supervised, 2 unsupervised, 2 reinforcement.', 14, bold=True))
    return 318, ''.join(o)
FIG[2] = (f2, 'The six tasks sorted by their feedback: labels make tasks 1 and 4 supervised, inputs alone make 2 and 5 unsupervised, and rewards make 3 and 6 reinforcement learning. House price is a number (regression); spam is a class (classification).',
          'Three columns. Supervised holds task 1 house price, a regression, and task 4 spam, a classification. Unsupervised holds tasks 2 and 5, both clustering. Reinforcement holds task 3, the maze robot, and task 6, the cricket shot. Two tasks in each column.')


# ---- 1.3 accuracy hides the 500 missed defaults ----
def f3():
    o = [T(40, 24, 'Always predict “repay” on the bank’s 5000 past loans', 15, 'start', bold=True)]
    x0, W = 40, 640
    wr = W * 4500 / 5000
    o.append(T(x0, 56, 'actual', 13, 'start', MUT))
    o.append(R(x0, 64, wr, 42, ACS, AC, 4, 1.6)); o.append(T(x0 + wr / 2, 90, '4500 repaid', 14, bold=True))
    o.append(R(x0 + wr, 64, W - wr, 42, LVS, LV, 4, 1.6)); o.append(T(x0 + wr + (W - wr) / 2, 90, '500', 14, bold=True, fill=LV))
    o.append(T(x0 + wr + (W - wr) / 2, 124, 'defaulted', 13, fill=LV))
    o.append(T(x0, 150, 'model says', 13, 'start', MUT))
    o.append(R(x0, 158, W, 42, PANEL, L2, 4, 1.6)); o.append(T(x0 + W / 2, 184, 'repay, repay, repay … for all 5000', 14))
    y = 236
    o.append(boxt(40, y, 196, 66, ['accuracy', '4500 ÷ 5000 = 90%'], ACS, AC, 14))
    o.append(boxt(262, y, 196, 66, ['recall on default', '0 ÷ 500 = 0'], LVS, LV, 14))
    o.append(boxt(484, y, 196, 66, ['cost of misses', '500 × ₹1,00,000', '= ₹5,00,00,000'], LVS, LV, 13))
    o.append(T(40, y + 100, 'The 90% looks good only because most loans repay. Fix P before building anything:', 14, 'start'))
    o.append(T(40, y + 122, 'score recall on defaults, or the rupee cost of mistakes.', 14, 'start', bold=True, fill=NX))
    return y + 138, ''.join(o)
FIG[3] = (f3, 'A model that always says repay gets 4500 of 5000 loans right, 90% accuracy, yet it catches 0 of the 500 defaults and costs ₹5,00,00,000. The performance measure P has to change before the design goes on.',
          'A bar of 5000 actual loans, 4500 repaid and 500 defaulted, above a bar where the model says repay for all 5000. Three result boxes: accuracy 90 percent, recall on default 0, cost 5 crore rupees.')


# ---- 1.4 training and validation error against degree ----
def f4():
    o = [T(40, 24, 'Training and validation error as the degree grows', 15, 'start', bold=True)]
    x0, x1, y0, y1 = 90, 560, 66, 290
    fx = lambda d: x0 + (d - 1) / 8 * (x1 - x0)
    fy = lambda e: y1 - e / 0.5 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [1, 3, 5, 7, 9], [0, 0.1, 0.2, 0.3, 0.4, 0.5], fx, fy, 'polynomial degree (model complexity)', 'error',
                  yfmt=lambda v: f'{v:.1f}'))
    deg = [1, 3, 5, 9]; tr = [0.30, 0.10, 0.04, 0.01]; va = [0.32, 0.12, 0.25, 0.45]
    o.append(P([(fx(d), fy(e)) for d, e in zip(deg, tr)], AC, 2.5))
    o.append(P([(fx(d), fy(e)) for d, e in zip(deg, va)], LV, 2.5))
    for d, e in zip(deg, tr): o.append(C(fx(d), fy(e), 5, AC))
    for d, e in zip(deg, va): o.append(C(fx(d), fy(e), 5, LV))
    o.append(Tb(fx(1) + 8, fy(0.32) - 12, '0.32', 13, 'start', LV)); o.append(Tb(fx(1) + 8, fy(0.30) + 20, '0.30', 13, 'start', AC))
    o.append(Tb(fx(3), fy(0.12) - 12, '0.12', 13, fill=LV)); o.append(Tb(fx(3), fy(0.10) + 22, '0.10', 13, fill=AC))
    o.append(Tb(fx(9) - 10, fy(0.45) - 4, '0.45', 13, 'end', LV)); o.append(Tb(fx(9) - 8, fy(0.01) - 10, '0.01', 13, 'end', AC))
    gx = fx(9) + 14
    o.append(L(gx, fy(0.45), gx, fy(0.01), INK, 1.8)); o.append(L(gx - 5, fy(0.45), gx + 5, fy(0.45), INK, 1.8))
    o.append(L(gx - 5, fy(0.01), gx + 5, fy(0.01), INK, 1.8))
    o.append(T(gx + 10, fy(0.23), 'gap 0.44', 14, 'start', bold=True))
    o.append(T(fx(1) + 34, y0 + 14, 'underfit', 13, fill=MUT)); o.append(T(fx(3) + 6, y0 + 14, 'good fit', 13, fill=AC, bold=True))
    o.append(T(fx(7), y0 + 14, 'overfit', 13, fill=LV, bold=True))
    lx = 590
    o.append(L(lx, 236, lx + 26, 236, AC, 2.5)); o.append(T(lx + 32, 241, 'training', 13, 'start'))
    o.append(L(lx, 262, lx + 26, 262, LV, 2.5)); o.append(T(lx + 32, 267, 'validation', 13, 'start'))
    return 344, ''.join(o)
FIG[4] = (f4, 'Degree 1 underfits with both errors high (0.30 and 0.32), degree 3 fits well (0.10 and 0.12), and degree 9 overfits: training error falls to 0.01 while validation error climbs to 0.45, a gap of 0.44.',
          'Line plot of error against polynomial degree. Training error falls 0.30, 0.10, 0.04, 0.01 at degrees 1, 3, 5, 9. Validation error goes 0.32, 0.12, 0.25, 0.45. A bracket at degree 9 marks the gap 0.44.')


# ---- 1.5 the Venn diagram of 1000 users ----
def f5():
    o = [T(40, 24, '1000 users: A = uses UPI, B = shops online', 15, 'start', bold=True)]
    o.append(R(30, 40, 400, 250, 'none', L2, 10, 1.6)); o.append(T(46, 62, 'all 1000 users', 13, 'start', MUT))
    o.append(f'<circle cx="185" cy="160" r="96" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2;fill-opacity:0.8"/>')
    o.append(f'<circle cx="290" cy="160" r="84" style="fill:var(--next-soft);stroke:var(--next);stroke-width:2;fill-opacity:0.8"/>')
    o.append(f'<path d="M 237.5 79.6 A 96 96 0 0 1 237.5 240.4 A 84 84 0 0 1 237.5 79.6 Z" style="fill:var(--live-soft);stroke:var(--live);stroke-width:2"/>')
    o.append(T(140, 166, '200', 18, bold=True)); o.append(T(140, 186, 'UPI only', 13))
    o.append(T(238, 166, '400', 18, bold=True, fill=LV)); o.append(T(238, 186, 'both', 13))
    o.append(T(330, 166, '100', 18, bold=True)); o.append(T(330, 186, 'online', 13))
    o.append(T(104, 92, 'A', 16, bold=True, fill=AC)); o.append(T(364, 98, 'B', 16, bold=True, fill=NX))
    o.append(T(400, 276, '300 neither', 13, 'end', MUT))
    x = 456
    rows = [('P(A) = 600 ÷ 1000 = 0.60', INK), ('P(B) = 500 ÷ 1000 = 0.50', INK), ('P(A and B) = 400 ÷ 1000 = 0.40', INK)]
    for i, (s, c) in enumerate(rows):
        o.append(T(x, 76 + i * 28, s, 14, 'start', c))
    o.append(T(x, 176, 'Given A, look only inside A:', 13, 'start', MUT))
    o.append(T(x, 202, 'P(B | A) = 400 ÷ 600 = 0.667', 15, 'start', LV, True))
    o.append(T(x, 240, '0.667 ≠ 0.50 = P(B)', 14, 'start', bold=True))
    o.append(T(x, 262, 'so A and B are not independent', 13, 'start'))
    return 304, ''.join(o)
FIG[5] = (f5, 'Of 600 UPI users, 400 also shop online, so P(B | A) = 400 ÷ 600 = 0.667. Among all 1000 users only P(B) = 0.50 shop online, so knowing A changes the chance of B: the two habits are not independent.',
          'A Venn diagram inside a box of 1000 users: 200 UPI only, 400 in the overlap, 100 online only and 300 neither. Beside it P(A) 0.60, P(B) 0.50, P(A and B) 0.40 and P(B given A) 0.667.')


# ---- 1.6 S rises, G falls, until they meet ----
def f6():
    o = [T(40, 24, 'Candidate elimination: G is pushed down, S is pulled up', 15, 'start', bold=True)]
    steps = ['start', 'P1 +', 'P2 +', 'N1 −', 'N2 −']
    G = [['(?,?,?)'], ['(?,?,?)'], ['(?,?,?)'], ['(Sunny,?,?)', '(?,Warm,?)'], ['(?,Warm,?)']]
    S = [['(∅,∅,∅)'], ['(Sunny,Warm,', 'Strong)'], ['(Sunny,Warm,?)'], ['(Sunny,Warm,?)'], ['(Sunny,Warm,?)']]
    xs = [42 + i * 136 for i in range(5)]
    w = 128
    o.append(T(30, 64, 'G', 15, 'start', NX, True)); o.append(T(30, 222, 'S', 15, 'start', AC, True))
    for i, x in enumerate(xs):
        c = LV if '−' in steps[i] else (AC if '+' in steps[i] else MUT)
        o.append(T(x + w / 2 + 6, 46, steps[i], 14, bold=True, fill=c))
        g = G[i]
        for j, s in enumerate(g):
            o.append(boxt(x + 8, 58 + j * 36, w - 4, 30, [s], NXS, NX, 13))
        o.append(boxt(x + 8, 198, w - 4, 40, S[i], ACS, AC, 13))
        if i:
            o.append(L(xs[i - 1] + w + 4, 217, x + 6, 217, L2, 1.4, arrow='m'))
    o.append(L(42 + 4 * 136 + 70, 92, 42 + 4 * 136 + 70, 196, LV, 2, dash='5 4'))
    o.append(T(648, 150, 'version space:', 13, 'end', LV, True))
    o.append(T(648, 168, 'only these two', 13, 'end', LV))
    o.append(T(40, 268, 'Positives move S up (more general); negatives move G down (more specific).', 14, 'start'))
    o.append(T(40, 290, 'Final S = (Sunny,Warm,?), the same hypothesis Find-S returns; final G = (?,Warm,?).', 14, 'start', bold=True))
    return 306, ''.join(o)
FIG[6] = (f6, 'Positive examples P1 and P2 pull the specific boundary S up to (Sunny,Warm,?); negative examples N1 and N2 push the general boundary G down to (?,Warm,?). The version space is the two hypotheses between them.',
          'Five columns: start, P1, P2, N1, N2. The G row goes from (?,?,?) to two hypotheses (Sunny,?,?) and (?,Warm,?) after N1 and to (?,Warm,?) after N2. The S row goes from all-empty to (Sunny,Warm,Strong) and then (Sunny,Warm,?).')


# ---- 1.7 same training error, different test error ----
def f7():
    o = [T(40, 24, 'Two rules fit the 20 training emails equally well', 15, 'start', bold=True)]
    x0, x1, y0, y1 = 80, 470, 50, 270
    fy = lambda e: y1 - e / 40 * (y1 - y0)
    o.append(L(x0, y1, x1, y1, L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    for v in [0, 10, 20, 30, 40]:
        o.append(L(x0, fy(v), x1, fy(v), LN, 1)); o.append(T(x0 - 8, fy(v) + 4.5, f'{v}%', 13, 'end', MUT))
    groups = [(140, 'h1: 30 conditions', 10, 35, LV), (330, 'h2: 3 conditions', 10, 20, AC)]
    for gx, name, tr, te, c in groups:
        o.append(R(gx - 54, fy(tr), 48, y1 - fy(tr), PANEL, L2, 3, 1.6)); o.append(T(gx - 30, fy(tr) - 8, f'{tr}%', 13))
        o.append(R(gx + 6, fy(te), 48, y1 - fy(te), c.replace(')', '-soft)'), c, 3, 1.8)); o.append(T(gx + 30, fy(te) - 8, f'{te}%', 13, bold=True, fill=c))
        o.append(T(gx, y1 + 22, name, 13, bold=True))
        bx = gx + 66
        o.append(L(bx, fy(te), bx, fy(tr), INK, 1.6)); o.append(L(bx - 4, fy(te), bx + 4, fy(te), INK, 1.6)); o.append(L(bx - 4, fy(tr), bx + 4, fy(tr), INK, 1.6))
        o.append(T(bx + 6, (fy(te) + fy(tr)) / 2 + 5, f'{te - tr}', 14, 'start', c, True))
    o.append(R(500, 70, 20, 16, PANEL, L2, 3, 1.6)); o.append(T(528, 83, 'training error', 13, 'start'))
    o.append(R(500, 96, 20, 16, ACS, AC, 3, 1.6)); o.append(T(528, 109, 'test error (100', 13, 'start')); o.append(T(528, 126, 'unseen emails)', 13, 'start'))
    o.append(T(500, 170, 'gap in percentage', 13, 'start', MUT)); o.append(T(500, 188, 'points: 25 vs 10', 13, 'start', MUT))
    o.append(T(500, 228, 'Preferring the', 14, 'start', bold=True)); o.append(T(500, 248, 'simpler rule is', 14, 'start', bold=True))
    o.append(T(500, 268, 'the inductive bias.', 14, 'start', bold=True, fill=AC))
    return 306, ''.join(o)
FIG[7] = (f7, 'Both rules miss 2 of 20 training emails (10%), so the data cannot choose between them. On 100 unseen emails h1 errs 35% and h2 only 20%: gaps of 25 and 10 percentage points reward the bias toward the simpler rule.',
          'Grouped bars. Rule h1 with 30 conditions: training error 10 percent, test error 35 percent, gap 25. Rule h2 with 3 conditions: training error 10 percent, test error 20 percent, gap 10.')


spec = make_spec(FIG)

TEXT = {
    4: [('The figure plots both errors against model complexity.',
         'Figure 1.4.1 plots both errors against polynomial degree, which stands for model complexity.')],
    5: [('The two curves in the figure have the same σ = 1 and different means.',
         'Two Gaussian curves with the same σ = 1 and different means have the same bell shape, shifted along the axis.')],
}


def text_fixes(k):
    return TEXT.get(k, [])
