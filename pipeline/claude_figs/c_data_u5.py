"""Claude's hand-drawn figures for c-data-u5 (Data Science, unit 5: machine learning basics), one per chapter, from
each chapter's worked example."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
ARR = {AC: 'n', L2: 'm', LV: 'l', NX: 'x', MUT: 'm', INK: 'm'}


def ar(x1, y1, x2, y2, c=AC, w=2, dash=None):
    return L(x1, y1, x2, y2, c, w, dash, arrow=ARR[c])


def sq(x, y, c, filled=True, s=11):
    return f'<rect x="{x - s / 2:.1f}" y="{y - s / 2:.1f}" width="{s}" height="{s}" style="fill:{c if filled else PANEL};stroke:{c};stroke-width:2"/>'


def cross(x, y, c, s=8):
    return L(x - s, y - s, x + s, y + s, c, 3) + L(x - s, y + s, x + s, y - s, c, 3)


# ---- 5.1 hold-out test set and 5-fold cross-validation ----
def f1():
    o = [T(20, 26, '2,000 customer records', 14, 'start', INK, True)]
    W = 600
    o += [R(80, 36, W * 0.8, 34, PANEL, L2, 0, 1.5), T(80 + W * 0.4, 58, 'training + validation: 1,600', 14, bold=True),
          R(80 + W * 0.8, 36, W * 0.2, 34, LVS, LV, 0, 1.5), T(80 + W * 0.9, 58, 'test: 400', 14, fill=LV, bold=True)]
    acc = ['0.81', '0.78', '0.84', '0.80', '0.77']
    fw = W * 0.8 / 5
    o.append(T(80, 100, '5 folds of 320 rows: each round trains on 4 folds (1,280 rows) and validates on 1', 13, 'start', MUT, True))
    for r in range(5):
        y = 110 + r * 32
        o.append(T(70, y + 20, f'round {r + 1}', 13, 'end', MUT))
        for k in range(5):
            v = k == r
            o.append(R(80 + k * fw + 1, y, fw - 2, 26, NXS if v else ACS, NX if v else AC, 2, 1.2))
            o.append(T(80 + k * fw + fw / 2, y + 18, 'validate' if v else 'train', 13, fill=NX if v else AC, bold=v))
        o.append(T(80 + W * 0.8 + 24, y + 19, acc[r], 14, 'start', NX, True))
    o.append(T(80 + W * 0.8 + 24, 284, 'mean 0.80', 15, 'start', NX, True))
    o.append(L(80 + W * 0.8 + 20, 270, 80 + W * 0.8 + 100, 270, NX, 1.5))
    o.append(T(20, 316, 'Trees: A 72% / 70% underfits; C 99% / 74% overfits (25 points lost); B 86% / 83% is the one to pick.', 13, 'start', INK, True))
    return 330, ''.join(o)


FIG[1] = (f1, 'The store keeps 400 rows aside as a test set and splits the other 1,600 into five folds of 320. Each round validates on a different fold, and the five accuracies average 0.80.',
          'A bar of 2,000 records split into 1,600 for training and validation and 400 for testing. Below, five rounds of five folds; in each round a different fold is marked validate, with accuracies 0.81, 0.78, 0.84, 0.80, 0.77 and mean 0.80.')


# ---- 5.2 least-squares line and residuals ----
def f2():
    pts = [(2, 50), (4, 58), (6, 66), (8, 70), (10, 81)]
    x0, x1, y0, y1 = 80, 460, 40, 270
    fx = lambda x: x0 + x * (x1 - x0) / 12
    fy = lambda y: y1 - (y - 45) * (y1 - y0) / 45
    line = lambda x: 42.8 + 3.7 * x
    o = [axes(x0, x1, y0, y1, range(0, 13, 2), [50, 60, 70, 80, 90], fx, fy, 'study hours x', 'marks y')]
    o.append(L(fx(1), fy(line(1)), fx(11.5), fy(line(11.5)), AC, 2.5))
    for x, y in pts:
        o += [L(fx(x), fy(y), fx(x), fy(line(x)), LV, 2.5), C(fx(x), fy(y), 6, NX)]
    for x, y, e in [(2, 50, '−0.2'), (6, 66, '+1.0'), (8, 70, '−2.4'), (10, 81, '+1.2')]:
        o.append(T(fx(x) + 9, (fy(y) + fy(line(x))) / 2 + 5, e, 13, 'start', LV, True))
    o += [L(fx(7), fy(line(7)), fx(7), y1, NX, 1.5, '4 4'), L(x0, fy(68.7), fx(7), fy(68.7), NX, 1.5, '4 4'), sq(fx(7), fy(68.7), NX, True, 11),
          T(x0 + 6, fy(68.7) - 6, '68.7', 13, 'start', NX, True)]
    o.append(Tb(fx(9.6), fy(line(11.2)) - 8, 'ŷ = 42.8 + 3.7x', 14, fill=AC, bold=True))
    o.append(boxt(500, 40, 200, 196, ['b₁ = 148 ÷ 40 = 3.7', 'b₀ = 65 − 3.7 × 6 = 42.8', 'SSE = 8.40, SST = 556', 'R² = 0.985',
                                       's_e = √(8.40 ÷ 3) = 1.67', 't = 3.7 ÷ 0.265 = 13.98', '> 3.182: slope significant'], PANEL, AC, 13, True))
    o.append(T(20, 330, 'For 7 hours: ŷ = 42.8 + 3.7 × 7 = 68.7 marks. The orange residuals add to 0.', 14, 'start', NX, True))
    return 344, ''.join(o)


FIG[2] = (f2, 'The least-squares line ŷ = 42.8 + 3.7x through the five students; each orange segment is a residual, and their squares add to 8.40. Seven hours of study predicts 68.7 marks.',
          'A scatter of marks against study hours, (2, 50) to (10, 81), with the fitted line and short orange residual segments labelled −0.2, +1.0, −2.4 and +1.2. Dashed lines mark the prediction 68.7 at 7 hours. A side box lists the slope 3.7, intercept 42.8, R² 0.985 and t = 13.98.')


# ---- 5.3 the sigmoid of revision hours ----
def f3():
    x0, x1, y0, y1 = 80, 520, 40, 260
    fx = lambda x: x0 + x * (x1 - x0) / 12
    fy = lambda p: y1 - p * (y1 - y0)
    sig = lambda x: 1 / (1 + math.exp(-(-4 + 0.8 * x)))
    o = [axes(x0, x1, y0, y1, range(0, 13, 2), [0, 0.25, 0.5, 0.75, 1], fx, fy, 'revision hours x', 'P(pass)', yfmt=lambda v: f'{v:g}')]
    o.append(L(x0, fy(0.5), x1, fy(0.5), MUT, 1.5, '5 4'))
    o.append(P([(fx(12 * i / 160), fy(sig(12 * i / 160))) for i in range(161)], AC, 2.5))
    o += [L(fx(5), fy(0.5), fx(5), y1, NX, 1.8, '5 4'), Tb(fx(5) + 6, y1 - 12, 'boundary x = 5', 13, 'start', NX, True)]
    for x, p, s, dx, anc in [(3, 0.168, '0.168', 8, 'start'), (5, 0.5, '0.5', -10, 'end'), (7, 0.832, '0.832', -10, 'end'), (7.75, 0.9, '0.9 at 7.75 h', 12, 'start')]:
        o += [C(fx(x), fy(p), 6, LV), T(fx(x) + dx, fy(p) + (16 if x in (3, 7.75) else -8), s, 13, anc, LV, True)]
    o.append(boxt(550, 40, 150, 150, ['z = −4 + 0.8x', 'p = 1 ÷ (1 + e⁻ᶻ)', '', 'each hour × odds', 'e^0.8 = 2.23'], PANEL, AC, 13, True))
    o.append(T(20, 330, 'p = 0.9 needs odds 9, so z = ln 9 = 2.197 and x = (4 + 2.197) ÷ 0.8 = 7.75 hours.', 14, 'start', INK, True))
    return 344, ''.join(o)


FIG[3] = (f3, 'The fitted S-curve p = σ(−4 + 0.8x) crosses 0.5 at 5 hours, the decision boundary. Three hours gives 0.168, seven hours 0.832, and 0.9 needs 7.75 hours.',
          'A sigmoid curve of P(pass) against revision hours from 0 to 12, with a dashed threshold at 0.5 and a dashed boundary at x = 5. Orange points mark 0.168 at 3 hours, 0.5 at 5, 0.832 at 7 and 0.9 at 7.75.')


# ---- 5.4 the ID3 tree ----
def f4():
    o = [boxt(250, 20, 180, 50, ['Weather?', '10 rows: 5 Yes, 5 No'], ACS, AC, 13, True)]
    o += [boxt(40, 140, 180, 50, ['Exam next day?', '4 rows: 2 Yes, 2 No'], ACS, AC, 13, True),
          boxt(250, 140, 180, 50, ['Play', '3 Yes, 0 No'], NXS, NX, 14, True),
          boxt(460, 140, 180, 50, ['No play', '0 Yes, 3 No'], LVS, LV, 14, True),
          boxt(20, 262, 100, 50, ['Play', '2 Yes'], NXS, NX, 14, True),
          boxt(140, 262, 110, 50, ['No play', '2 No'], LVS, LV, 14, True)]
    o += [ar(300, 70, 130, 138, INK, 2.5), ar(340, 70, 340, 138, INK), ar(380, 70, 550, 138, INK),
          Tb(200, 102, 'Sunny', 13, fill=INK, bold=True), Tb(340, 104, 'Cloudy', 13, fill=INK, bold=True), Tb(470, 102, 'Rainy', 13, fill=INK, bold=True),
          ar(100, 190, 70, 260, INK), ar(160, 190, 195, 260, INK, 2.5), Tb(76, 226, 'No', 13, fill=INK, bold=True), Tb(186, 226, 'Yes', 13, fill=INK, bold=True)]
    o.append(boxt(300, 216, 400, 96, ['information gain', 'root: Weather 0.600, Exam 0.125, Ground 0.000',
                                      'inside Sunny: Exam 1.000, Ground 0.311', 'Ground is never asked'], PANEL, L2, 13, True))
    o.append(T(20, 344, 'New evening (Sunny, Wet, Exam = Yes): Sunny → Exam Yes → No play (the thick path).', 14, 'start', LV, True))
    return 358, ''.join(o)


FIG[4] = (f4, 'Weather has the largest gain, 0.600, so it is the root; Cloudy and Rainy are pure leaves. Inside Sunny, Exam splits the four rows perfectly, so a Sunny evening before an exam is No play.',
          'A tree: root Weather with 10 rows; Sunny leads to Exam next day with 4 rows, Cloudy to a Play leaf with 3, Rainy to a No play leaf with 3. Exam No gives Play (2) and Yes gives No play (2). A panel lists the gains 0.600, 0.125, 0.000 at the root and 1.000, 0.311 inside Sunny.')


# ---- 5.5 one training step of a 2-2-1 network ----
def f5():
    X = [(80, 90), (80, 230)]
    H = [(330, 90), (330, 230)]
    Ot = (580, 160)
    o = []
    ws = [(0, 0, '0.4', -18), (1, 0, '0.3', -40), (0, 1, '−0.2', 40), (1, 1, '0.6', 18)]
    for i, j, w, dy in ws:
        (a, b), (c, d) = X[i], H[j]
        o.append(L(a + 30, b, c - 32, d, L2, 2))
        o.append(Tb((a + c) / 2 + (-30 if i != j else 0), (b + d) / 2 + (dy if i != j else -6), f'w = {w}', 13, fill=MUT, bold=True))
    for j, v in enumerate(['0.7', '−0.5']):
        (a, b), (c, d) = H[j], Ot
        o += [L(a + 32, b, c - 34, d, L2, 2), Tb((a + c) / 2, (b + d) / 2 + (-10 if j == 0 else 22), f'v = {v}', 13, fill=MUT, bold=True)]
    for (x, y), s in zip(X, ['x₁ = 0.5', 'x₂ = 1.0']):
        o += [f'<circle cx="{x}" cy="{y}" r="30" style="fill:{PANEL};stroke:{L2};stroke-width:2"/>', T(x, y + 5, s, 13, bold=True)]
    for (x, y), s, d in zip(H, ['0.6225', '0.6225'], ['δ₁ = −0.0192', 'δ₂ = +0.0137']):
        o += [f'<circle cx="{x}" cy="{y}" r="32" style="fill:{ACS};stroke:{AC};stroke-width:2"/>', T(x, y + 5, s, 14, bold=True),
              T(x, y + 52 if y > 150 else y - 42, d, 13, fill=LV, bold=True)]
    o += [f'<circle cx="{Ot[0]}" cy="{Ot[1]}" r="34" style="fill:{NXS};stroke:{NX};stroke-width:2"/>', T(Ot[0], Ot[1] + 5, 'o = 0.5311', 13, bold=True),
          T(Ot[0], Ot[1] - 46, 'δₒ = −0.1168', 13, fill=LV, bold=True), T(Ot[0], Ot[1] + 54, 'target t = 1', 13, fill=MUT)]
    o += [T(330, 30, 'hidden h = σ(0.5)', 13, fill=AC, bold=True)]
    o.append(T(20, 304, 'Forward: E = ½(1 − 0.5311)² = 0.1099. Backward with η = 0.5: v₁ 0.7 → 0.7363, v₂ −0.5 → −0.4637, w₁₁ 0.4 → 0.4048.', 13, 'start'))
    o.append(T(20, 328, 'A new forward pass gives o = 0.5431 and E = 0.1044, down from 0.1099.', 14, 'start', NX, True))
    return 342, ''.join(o)


FIG[5] = (f5, 'One step on the 2-2-1 network: the forward pass gives o = 0.5311, the deltas (orange) say how each net input should change, and after the update the error falls from 0.1099 to 0.1044.',
          'Two inputs 0.5 and 1.0 joined by weights 0.4, 0.3, −0.2 and 0.6 to two hidden nodes, each 0.6225, joined by weights 0.7 and −0.5 to the output 0.5311. Orange deltas: −0.0192, +0.0137 and −0.1168. Text gives the error falling from 0.1099 to 0.1044.')


# ---- 5.6 k-means on six customers ----
def f6():
    P_ = {'A': (1, 1), 'B': (2, 1), 'C': (1, 2), 'D': (5, 4), 'E': (6, 5), 'F': (5, 6)}

    def panel(x0, title, c1, c2, cl):
        x1, y0, y1 = x0 + 280, 50, 280
        fx = lambda x: x0 + x * (x1 - x0) / 7
        fy = lambda y: y1 - y * (y1 - y0) / 7
        o = [T(x0, 30, title, 14, 'start', INK, True), axes(x0, x1, y0, y1, range(0, 8), range(0, 8), fx, fy, '', '')]
        for k, (x, y) in P_.items():
            c = AC if k in cl else LV
            o += [C(fx(x), fy(y), 7, c), T(fx(x) - 10, fy(y) - 9, k, 13, 'end', c, True)]
        o += [cross(fx(c1[0]), fy(c1[1]), AC), cross(fx(c2[0]), fy(c2[1]), LV)]
        return o, fx, fy
    o1, fx, fy = panel(60, 'after iteration 1', (1, 1.5), (4.5, 4), 'AC')
    o2, gx, gy = panel(420, 'final (iteration 2, then no change)', (1.33, 1.33), (5.33, 5), 'ABC')
    o = o1 + o2
    o += [Tb(fx(4.5) + 12, fy(4) + 22, 'c₂ (4.5, 4)', 13, 'start', LV, True), Tb(fx(1) + 14, fy(2.6), 'c₁ (1, 1.5)', 13, 'start', AC, True),
          arc(fx(2) + 4, fy(1) - 6, fx(4.5) - 8, fy(4) + 8, -0.15, LV, 1.5, 'l', '4 3'), T(fx(3.3), fy(1.2), 'B joins the far group', 13, 'start', LV)]
    o += [Tb(gx(5.33) + 12, gy(5) + 22, 'c₂ (5.33, 5)', 13, 'start', LV, True), Tb(gx(1.33) + 14, gy(0.45), 'c₁ (1.33, 1.33)', 13, 'start', AC, True)]
    o.append(T(20, 336, 'B is nearer the new c₁ (1.12 against 3.91), so it switches. WCSS falls from 23.5 to 4.0.', 14, 'start', INK, True))
    return 350, ''.join(o)


FIG[6] = (f6, 'Starting from A and B, the first pass puts B with the far points and c₂ jumps to (4.5, 4). In the second pass B is nearer c₁ and switches, giving {A, B, C} and {D, E, F} with WCSS 4.0.',
          'Two scatter panels of six customers A to F. After iteration 1, A and C are blue and B, D, E, F orange, with centroids (1, 1.5) and (4.5, 4). In the final panel A, B, C are blue around (1.33, 1.33) and D, E, F orange around (5.33, 5).')


# ---- 5.7 PCA on five students ----
def f7():
    pts = [(2, 1), (3, 3), (4, 2), (5, 5), (6, 4)]
    sc = ['−2.83', '−0.71', '−0.71', '2.12', '2.12']
    x0, x1, y0, y1 = 80, 380, 30, 290
    fx = lambda x: x0 + x * (x1 - x0) / 7
    fy = lambda y: y1 - y * (y1 - y0) / 7
    o = [axes(x0, x1, y0, y1, range(0, 8), range(0, 8), fx, fy, 'maths', 'physics')]
    o += [L(fx(0.6), fy(-0.4), fx(6.9), fy(5.9), AC, 2.5), L(fx(2.2), fy(4.8), fx(5.8), fy(1.2), LV, 2, '6 4'),
          T(fx(6.6), fy(6.1), 'PC1', 14, fill=AC, bold=True), T(fx(2.0), fy(5.0), 'PC2', 14, fill=LV, bold=True)]
    for (x, y), s in zip(pts, sc):
        t = ((x - 4) + (y - 3)) / 2
        px, py = 4 + t, 3 + t
        o += [L(fx(x), fy(y), fx(px), fy(py), MUT, 1.2, '3 3'), sq(fx(px), fy(py), AC, True, 9), C(fx(x), fy(y), 6, NX)]
        o.append(T(fx(x) + (10 if x - 4 > y - 3 else -10), fy(y) + (16 if x - 4 > y - 3 else -6), s, 13, 'start' if x - 4 > y - 3 else 'end', AC, True))
    o.append(C(fx(4), fy(3), 4, INK))
    o += [T(420, 46, 'C = [[2.5, 2.0], [2.0, 2.5]]', 14, 'start', INK, True), T(420, 70, 'λ₁ = 4.5,  λ₂ = 0.5', 14, 'start')]
    o += [R(460, 110, 4.5 * 40, 34, ACS, AC, 3, 1.5), T(470 + 4.5 * 40, 132, '90%', 14, 'start', AC, True), T(450, 132, 'PC1', 13, 'end', AC, True),
          R(460, 154, 0.5 * 40, 34, LVS, LV, 3, 1.5), T(470 + 0.5 * 40, 176, '10%', 14, 'start', LV, True), T(450, 176, 'PC2', 13, 'end', LV, True)]
    o += [T(420, 226, 'PC1 = (0.707, 0.707)', 14, 'start', AC, True), T(420, 250, 'score = 0.707(x₁ − 4) + 0.707(x₂ − 3)', 13, 'start'),
          T(420, 274, 'one number keeps 90% of the spread', 13, 'start', MUT)]
    return 342, ''.join(o)


FIG[7] = (f7, 'PC1 runs along the diagonal through the mean (4, 3), where the scores spread most; each point drops onto it to give its one-number score. The eigenvalues 4.5 and 0.5 mean PC1 keeps 90%.',
          'A scatter of five students\' maths and physics scores with the PC1 line along the diagonal and the dashed PC2 line across it. Dotted drops land on PC1 at squares labelled with scores −2.83, −0.71, −0.71, 2.12, 2.12. Bars show 90% for PC1 and 10% for PC2.')


# ---- 5.8 confusion matrix for a fraud model ----
def f8():
    o = [T(210, 30, 'predicted fraud', 14, bold=True), T(350, 30, 'predicted genuine', 14, bold=True),
         T(130, 74, 'actual fraud', 14, 'end', LV, True), T(130, 92, '(50)', 13, 'end', LV), T(130, 144, 'actual genuine', 14, 'end', NX, True), T(130, 162, '(950)', 13, 'end', NX)]
    for x, y, s, f, st in [(140, 44, 'TP = 40', NXS, NX), (280, 44, 'FN = 10', LVS, LV), (140, 114, 'FP = 20', LVS, LV), (280, 114, 'TN = 930', NXS, NX)]:
        o.append(boxt(x, y, 140, 70, [s], f, st, 17, True, rx=0))
    m = [('accuracy', '970 ÷ 1,000 = 97.0%'), ('precision', '40 ÷ 60 = 0.667'), ('recall', '40 ÷ 50 = 0.800'),
         ('specificity', '930 ÷ 950 = 0.979'), ('F1', '1.067 ÷ 1.467 = 0.727')]
    for i, (a, b) in enumerate(m):
        o += [T(440, 52 + i * 30, a, 13, 'start', MUT, True), T(530, 52 + i * 30, b, 13, 'start', INK, True)]
    for i, (nm, acc, rec, c, f) in enumerate([('this model', 97.0, 0.8, NX, NXS), ('flags nothing', 95.0, 0.0, LV, LVS)]):
        y = 236 + i * 38
        o += [T(150, y + 20, nm, 14, 'end', c, True), R(160, y, acc * 2.4, 28, f, c, 3, 1.5), T(166 + acc * 2.4, y + 19, f'accuracy {acc:g}%', 13, 'start', c, True),
              T(520, y + 19, f'recall {rec:.1f}', 14, 'start', c, True)]
    o.append(T(20, 330, 'Accuracy differs by 2 points, but only this model catches any fraud: 40 of 50.', 14, 'start', INK, True))
    return 344, ''.join(o)


FIG[8] = (f8, 'Of 1,000 transactions, 50 are fraud; the model flags 60 and catches 40. Accuracy is 97%, but a model that flags nothing still scores 95%, so recall (0.800) and precision (0.667) tell the real story.',
          'A 2 by 2 confusion matrix: TP 40, FN 10, FP 20, TN 930. Beside it accuracy 97.0%, precision 0.667, recall 0.800, specificity 0.979 and F1 0.727. Bars compare accuracy 97% with recall 0.8 for this model against 95% with recall 0 for a model that flags nothing.')


# ---- 5.9 moving average and exponential smoothing forecasts ----
def f9():
    Y = [120, 132, 128, 140, 152, 148, 160, 170]
    MA = [None, None, None, 126.67, 133.33, 140.00, 146.67, 153.33, 159.33]
    SES = [None, 120.00, 123.60, 124.92, 129.44, 136.21, 139.75, 145.82, 153.08]
    mon = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
    x0, x1, y0, y1 = 80, 520, 40, 270
    fx = lambda i: x0 + (i + 0.5) * (x1 - x0) / 9
    fy = lambda v: y1 - (v - 110) * (y1 - y0) / 70
    o = [axes(x0, x1, y0, y1, [], [110, 120, 130, 140, 150, 160, 170, 180], fx, fy, '', 'payments (₹ thousand)')]
    for i, m in enumerate(mon): o.append(T(fx(i), y1 + 20, m, 13, fill=MUT))
    o.append(P([(fx(i), fy(v)) for i, v in enumerate(Y)], INK, 2.5))
    for i, v in enumerate(Y): o.append(C(fx(i), fy(v), 5, INK))
    o.append(P([(fx(i), fy(v)) for i, v in enumerate(MA) if v], AC, 2.2, '7 4'))
    for i, v in enumerate(MA):
        if v: o.append(sq(fx(i), fy(v), AC, True, 9))
    o.append(P([(fx(i), fy(v)) for i, v in enumerate(SES) if v], LV, 2.2, '3 3'))
    for i, v in enumerate(SES):
        if v: o.append(f'<path d="M{fx(i):.1f},{fy(v) - 6:.1f} L{fx(i) + 6:.1f},{fy(v) + 5:.1f} L{fx(i) - 6:.1f},{fy(v) + 5:.1f} Z" style="fill:{LV}"/>')
    o += [T(fx(8) + 8, fy(159.33) - 2, '159.33', 13, 'start', AC, True), T(fx(8) + 8, fy(153.08) + 12, '153.08', 13, 'start', LV, True)]
    o += [C(556, 54, 5, INK), T(568, 59, 'actual', 13, 'start', INK, True), sq(556, 80, AC, True, 9), T(568, 85, 'MA(3)', 13, 'start', AC, True),
          f'<path d="M556,100 L562,111 L550,111 Z" style="fill:{LV}"/>', T(568, 111, 'SES, α = 0.3', 13, 'start', LV, True)]
    o.append(boxt(550, 136, 150, 90, ['MAE, Apr to Aug', 'MA(3): 14.0', 'SES: 18.8'], PANEL, L2, 14, True))
    o.append(T(20, 330, 'Every error is positive: with a rising trend of about 7 a month, both forecasts lag, SES with α = 0.3 the most.', 13, 'start', INK, True))
    return 344, ''.join(o)


FIG[9] = (f9, 'Both one-month-ahead forecasts run below the rising series. The 3-month average misses by 14.0 on average and exponential smoothing with α = 0.3 by 18.8; for September they give 159.33 and 153.08.',
          'A line of monthly payments rising from 120 in January to 170 in August, with a dashed blue 3-month moving average from April and a dotted orange smoothed forecast from February, both below the actual line. September forecasts 159.33 and 153.08; a box gives MAE 14.0 and 18.8.')

spec = make_spec(FIG)
