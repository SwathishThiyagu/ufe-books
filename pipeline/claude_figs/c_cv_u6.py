"""Claude's hand-drawn figures for c-cv-u6 (Computer Vision, unit 6: recognition and deep vision), one per chapter,
from each chapter's worked example."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
ARR = {AC: 'n', L2: 'm', LV: 'l', NX: 'x', MUT: 'm', INK: 'm'}


def ar(x1, y1, x2, y2, c=AC, w=2, dash=None):
    return L(x1, y1, x2, y2, c, w, dash, arrow=ARR[c])


def chain(items, y, x0=20, w=124, gap=18, h=56, size=13):
    o = []
    for i, (lines, f, st) in enumerate(items):
        x = x0 + i * (w + gap)
        o.append(boxt(x, y, w, h, lines, f, st, size, True))
        if i < len(items) - 1: o.append(ar(x + w, y + h / 2, x + w + gap - 2, y + h / 2, st if st != L2 else AC))
    return ''.join(o)


def tab(x, y, widths, rows, rh=30, head=True, fills=None):
    o = []
    for i, row in enumerate(rows):
        cx = x
        for j, (w, s) in enumerate(zip(widths, row)):
            f = fills(i, j) if fills else None
            o.append(R(cx, y + i * rh, w, rh, f or (ACS if head and i == 0 else PANEL), L2, 0, 1.2))
            o.append(T(cx + w / 2, y + i * rh + rh * 0.66, s, 13, bold=(head and i == 0) or j == 0))
            cx += w
    return ''.join(o)


def curve(f, a, b, fx, fy, c, w=2.5, dash=None, n=160):
    return P([(fx(a + (b - a) * i / n), fy(f(a + (b - a) * i / n))) for i in range(n + 1)], c, w, dash)


def sq(x, y, s, c, fill):
    return R(x - s / 2, y - s / 2, s, s, fill, c, 1, 2.2)


# ---- 6.1 tomatoes in the (R, A) plane ----
def f1():
    fx = lambda r: 70 + (r - 100) * 4.1
    fy = lambda a: 250 - (a - 36) * 22
    o = [axes(70, 480, 52, 250, [100, 125, 150, 175, 200], [36, 38, 40, 42, 44], fx, fy, 'mean red intensity R', 'area A (pixels)')]
    o.append(P([(fx(100), fy(39)), (fx(200), fy(39)), (fx(200), fy(42)), (fx(100), fy(42))], L2, 0.1, None, LVS, 0.5))
    o.append(L(fx(147.5), fy(36), fx(147.5), fy(45), LV, 2.5, '7 4'))
    o.append(Tb(fx(147.5), 44, 'R = 147.5', 13, fill=LV, bold=True))
    for r, a in ((180, 40), (190, 42), (175, 38)):
        o += [C(fx(r), fy(a), 7, NX), T(fx(r) + 10, fy(a) + 5, f'({r}, {a})', 13, 'start', NX, True)]
    for r, a in ((110, 41), (120, 39), (105, 43)):
        o += [C(fx(r), fy(a), 7, AC), T(fx(r) + 10, fy(a) + 5, f'({r}, {a})', 13, 'start', AC, True)]
    o += [T(fx(108), fy(36) - 10, 'unripe', 14, 'start', AC, True), T(fx(192), fy(36) - 10, 'ripe', 14, 'end', NX, True)]
    o += [boxt(510, 52, 200, 66, ['T = (120 + 175) ÷ 2', '= 147.5'], LVS, LV, 14, True),
          boxt(510, 132, 200, 66, ['ripe if R > 147.5', 'all 6 samples right'], NXS, NX, 14, True)]
    o += [T(510, 226, 'Shaded: areas 39–42 px', 13, 'start', INK, True), T(510, 246, 'hold both classes, so A', 13, 'start', INK, True),
          T(510, 266, 'adds nothing here.', 13, 'start', INK, True)]
    return 310, ''.join(o)


FIG[1] = (f1, 'The six tomatoes in the (R, A) plane. The vertical line R = 147.5, midway between 120 and 175, puts every ripe sample on the right and every unripe one on the left; the areas of both classes share the band 39 to 42 pixels.',
          'A scatter of red intensity R against area A: unripe points at (105, 43), (110, 41), (120, 39) and ripe points at (175, 38), (180, 40), (190, 42). A dashed vertical line at R = 147.5 separates them, and a shaded band from A = 39 to 42 shows the overlap in area.')


# ---- 6.2 minimum distance and 3-NN ----
def f2():
    fx = lambda x: 60 + x * 52
    fy = lambda y: 270 - y * 38
    o = [axes(60, 476, 42, 270, range(0, 9), range(0, 7), fx, fy, 'feature 1', 'feature 2')]
    o.append(f'<circle cx="{fx(4):.1f}" cy="{fy(3):.1f}" r="{2 * 52:.1f}" style="fill:none;stroke:{LV};stroke-width:1.5;stroke-dasharray:5 4"/>')
    o.append(L(fx(2.833), fy(6), fx(5.833), fy(0), INK, 2, '8 4'))
    m1, m2, x = (2, 2.6667), (6, 4.6667), (4, 3)
    o += [L(fx(x[0]), fy(x[1]), fx(m1[0]), fy(m1[1]), AC, 1.8, '3 3'), L(fx(x[0]), fy(x[1]), fx(m2[0]), fy(m2[1]), NX, 1.8, '3 3')]
    for p in ((1, 2), (2, 3), (3, 3)):
        o.append(C(fx(p[0]), fy(p[1]), 6, AC))
    for p in ((5, 4), (6, 5), (7, 5)):
        o.append(C(fx(p[0]), fy(p[1]), 6, NX))
    o += [sq(fx(m1[0]), fy(m1[1]), 14, AC, ACS), sq(fx(m2[0]), fy(m2[1]), 14, NX, NXS), C(fx(4), fy(3), 7, LV)]
    o += [Tb(fx(m1[0]) + 10, fy(m1[1]) + 30, 'm₁ (2, 2.67)', 13, 'start', AC, True), Tb(fx(m2[0]) + 12, fy(m2[1]) + 20, 'm₂ (6, 4.67)', 13, 'start', NX, True),
          Tb(fx(4) + 10, fy(3) + 22, 'x (4, 3)', 13, 'start', LV, True), Tb(fx(3) - 2, fy(3) - 14, '2.03', 13, 'middle', AC, True), Tb(fx(5.35), fy(3.4), '2.60', 13, 'middle', NX, True),
          Tb(fx(2.833) + 4, fy(6) + 4, 'bisector', 13, 'start', INK, True)]
    o += [boxt(500, 42, 210, 76, ['minimum distance', 'd₁ = 2.03 < d₂ = 2.60', 'so ω₁'], ACS, AC, 14, True),
          boxt(500, 132, 210, 96, ['3-NN (dashed circle)', '(3,3) 1.00  ω₁', '(5,4) 1.41  ω₂', '(2,3) 2.00  ω₁'], LVS, LV, 14, True),
          T(500, 252, 'votes 2 : 1, so ω₁', 14, 'start', LV, True)]
    o.append(T(20, 324, 'Dots are training samples (blue ω₁, green ω₂), squares their means.', 13, 'start', MUT))
    return 338, ''.join(o)


FIG[2] = (f2, 'The means are m₁ = (2, 2.67) and m₂ = (6, 4.67). The test point x = (4, 3) is 2.03 from m₁ and 2.60 from m₂, so it falls on the ω₁ side of the bisector; its three nearest samples vote 2 to 1 for ω₁ as well.',
          'Six training points, three of ω₁ around (2, 3) and three of ω₂ around (6, 5), with their means as squares. The test point (4, 3) has dashed lines of length 2.03 and 2.60 to the means, a dashed bisector between them, and a dashed circle of radius 2 holding its three nearest neighbours.')


# ---- 6.3 AlexNet layer 1 sizes ----
def f3():
    def slab(x, y, s, n, f, c):
        o = []
        for k in range(n - 1, -1, -1):
            o.append(R(x + k * 6, y - k * 6, s, s, f, c, 0, 1.4))
        return ''.join(o)
    o = [slab(30, 60, 120, 3, PANEL, L2), R(48, 74, 22, 22, NXS, NX, 0, 2), T(90, 210, '227 × 227 × 3', 14, fill=INK, bold=True)]
    o += [ar(186, 120, 292, 120, NX, 2.2), T(239, 100, '96 filters', 13, fill=NX, bold=True), T(239, 144, '11 × 11, stride 4', 13, fill=NX, bold=True)]
    o += [slab(304, 92, 60, 6, ACS, AC), T(349, 210, '55 × 55 × 96', 14, fill=AC, bold=True)]
    o += [ar(406, 120, 504, 120, LV, 2.2), T(455, 100, 'max pool 3 × 3', 13, fill=LV, bold=True), T(455, 144, 'stride 2', 13, fill=LV, bold=True)]
    o += [slab(516, 108, 30, 6, LVS, LV), T(546, 210, '27 × 27 × 96', 14, fill=LV, bold=True)]
    o.append(TM(20, 250, '(227 − 11) ÷ 4 + 1 = 216 ÷ 4 + 1 = 55', 14, 'start', AC, True))
    o.append(TM(20, 274, '⌊(55 − 3) ÷ 2⌋ + 1 = 26 + 1 = 27', 14, 'start', LV, True))
    o.append(TM(20, 298, '(11 × 11 × 3 + 1) × 96 = 364 × 96 = 34,944 weights', 14, 'start', NX, True))
    return 314, ''.join(o)


FIG[3] = (f3, 'A 227 × 227 × 3 image through 96 filters of 11 × 11 at stride 4 gives (227 − 11) ÷ 4 + 1 = 55, so 55 × 55 × 96. A 3 × 3 pool at stride 2 gives 27 × 27 × 96, and the layer holds only 364 × 96 = 34,944 weights.',
          'Three stacks of maps: the 227 by 227 by 3 input with a small 11 by 11 filter marked, the 55 by 55 by 96 convolution output, and the 27 by 27 by 96 pooled map, joined by arrows labelled 96 filters 11 × 11 stride 4 and max pool 3 × 3 stride 2. Below are the three size and weight sums.')


# ---- 6.4 IoU and non-maximum suppression ----
def f4():
    X = lambda x: x * 1.6 - 10
    Y = lambda y: y * 1.5 - 20
    o = [R(X(30), Y(40), 80 * 1.6, 100 * 1.5, ACS, AC, 0, 2.2), R(X(50), Y(60), 80 * 1.6, 100 * 1.5, 'none', NX, 0, 2.2),
         R(X(50), Y(60), 60 * 1.6, 80 * 1.5, LVS, LV, 0, 1.6)]
    o += [Tb(X(30) + 4, Y(40) - 6, 'predicted (30,40)–(110,140)', 13, 'start', AC, True), Tb(X(130), Y(160) + 18, 'truth (50,60)–(130,160)', 13, 'end', NX, True),
          T(X(80), Y(100) + 5, '60 × 80', 13, fill=LV, bold=True), T(X(80), Y(100) + 23, '= 4800', 13, fill=LV, bold=True)]
    for i, s in enumerate(['each box 80 × 100 = 8000 px²', 'overlap 60 × 80 = 4800 px²', 'union 8000 + 8000 − 4800', '= 11,200 px²']):
        o.append(T(250, 60 + i * 24, s, 13, 'start', INK, True))
    o.append(T(250, 174, 'IoU = 4800 ÷ 11,200 = 0.43', 14, 'start', LV, True))
    o.append(T(250, 196, 'a weak match', 13, 'start', MUT))
    o += [T(600, 36, 'NMS, threshold 0.5', 13, fill=INK, bold=True),
          R(530, 54, 110, 90, NXS, NX, 0, 2.2), R(570, 80, 120, 96, 'none', MUT, 0, 2, '6 4'),
          Tb(536, 72, '0.90 kept', 13, 'start', NX, True), Tb(690, 196, '0.85 removed', 13, 'end', MUT, True),
          L(600, 120, 660, 160, MUT, 2), L(660, 120, 600, 160, MUT, 2)]
    o.append(T(530, 226, 'IoU 0.6 > 0.5, so the', 13, 'start', INK, True))
    o.append(T(530, 246, 'lower score goes.', 13, 'start', INK, True))
    o.append(T(20, 266, 'Boxes are (x₁, y₁)–(x₂, y₂) in pixels; the shaded part is the overlap.', 13, 'start', MUT))
    return 282, ''.join(o)


FIG[4] = (f4, 'The predicted and true boxes, 8000 px² each, overlap in a 60 × 80 = 4800 px² patch, so IoU = 4800 ÷ 11,200 = 0.43. In NMS the 0.85 box overlaps the 0.90 box with IoU 0.6 > 0.5, so only the 0.90 box survives.',
          'Two 80 by 100 pixel boxes offset by 20 pixels each way with their 60 by 80 overlap shaded. Text gives the union 11,200 px² and IoU 0.43. On the right, a kept box scored 0.90 and a crossed-out dashed box scored 0.85.')


# ---- 6.5 the YOLO output tensor ----
def f5():
    g, cs = 30, 30
    o = [R(g, 40, 7 * cs, 7 * cs, PANEL, L2, 0, 1.5)]
    for k in range(1, 7):
        o += [L(g + k * cs, 40, g + k * cs, 40 + 7 * cs, LN, 1), L(g, 40 + k * cs, g + 7 * cs, 40 + k * cs, LN, 1)]
    o += [R(g + 2 * cs + 8, 40 + 2 * cs + 6, 3 * cs, 2.6 * cs, 'none', LV, 3, 2.4), R(g + 3 * cs, 40 + 3 * cs, cs, cs, NXS, NX, 0, 2.4), C(g + 3.5 * cs + 2, 40 + 3.4 * cs, 5, NX)]
    o += [T(g + 2 * cs + 12, 40 + 2 * cs - 2, 'dog', 13, 'start', LV, True), T(g + 3.5 * cs, 40 + 7 * cs + 20, '448 × 448 image, 7 × 7 grid', 13, fill=MUT, bold=True)]
    x0, w = 290, 13
    segs = [(0, 5, 'box 1', ACS, AC), (5, 10, 'box 2', ACS, AC), (10, 30, '20 class probabilities', LVS, LV)]
    for a, b, lab, f, c in segs:
        for k in range(a, b):
            o.append(R(x0 + k * w, 60, w, 30, f, c, 0, 1))
        o.append(T(x0 + (a + b) / 2 * w, 50, lab, 13, fill=c, bold=True))
    o.append(T(x0, 112, '30 numbers: 2 boxes of x, y, w, h, conf + 20 classes', 13, 'start', NX, True))
    o.append(ar(g + 4 * cs + 2, 40 + 3.5 * cs, x0 - 4, 90, NX, 2))
    for i, (s, c) in enumerate((('depth = 5B + C = 5 × 2 + 20 = 30', INK), ('tensor = 7 × 7 × 30 = 1470 numbers', INK),
                               ('boxes = 7 × 7 × 2 = 98', INK), ('dog score = 0.8 × 0.9 = 0.72', NX))):
        o.append(T(x0, 150 + i * 26, s, 14, 'start', c, True))
    o.append(T(20, 290, 'Then the confidence threshold and NMS keep the strong, distinct boxes.', 13, 'start', MUT))
    return 304, ''.join(o)


FIG[5] = (f5, 'One pass turns the 448 × 448 image into a 7 × 7 × 30 tensor: 1470 numbers and 98 boxes. The cell that holds the dog\'s centre carries 30 numbers, and its dog score is 0.8 × 0.9 = 0.72.',
          'A 7 by 7 grid over the image with a dog box and the cell holding its centre shaded. An arrow leads to a strip of 30 cells split into box 1, box 2 and 20 class probabilities. Text gives depth 30, 1470 numbers, 98 boxes and the dog score 0.72.')


# ---- 6.6 FCN upsampling back to 224 ----
def f6():
    o = [chain([(['input', '224 × 224 × 3'], PANEL, L2), (['VGG, 5 pools', 'stride 2⁵ = 32'], ACS, AC),
                (['deepest map', '7 × 7 × 512'], ACS, AC), (['1 × 1 conv', '7 × 7 × 21'], NXS, NX)], 34, 20, 155, 20, 60, 14)]
    o.append(P([(20 + 3 * 175 + 77, 94), (20 + 3 * 175 + 77, 128), (120, 128), (120, 150)], NX, 2))
    o.append(ar(120, 146, 120, 152, NX))
    o += [boxt(20, 154, 200, 60, ['×2 upsample', '14 × 14 × 21'], NXS, NX, 14, True), ar(220, 184, 248, 184, NX),
          boxt(250, 154, 200, 60, ['+ pool4 scores', '14 × 14 × 21'], LVS, LV, 14, True), ar(450, 184, 478, 184, LV),
          boxt(480, 154, 220, 60, ['×16 upsample', '224 × 224 × 21'], LVS, LV, 14, True)]
    o.append(T(20, 252, '×2 then ×16 is ×32, exactly the encoder stride, so every pixel gets 21 class scores.', 13, 'start', INK, True))
    o.append(TM(20, 280, 'one step: (7 − 1) × 32 − 2 × 16 + 64 = 224', 14, 'start', AC, True))
    o.append(T(20, 304, 'with a 64 × 64 transposed convolution, stride 32, padding 16.', 13, 'start', MUT))
    return 318, ''.join(o)


FIG[6] = (f6, 'Five stride-2 pools shrink 224 to 7, and a 1 × 1 convolution turns 7 × 7 × 512 into 7 × 7 × 21 scores. Upsampling ×2, adding pool4, then ×16 returns 224 × 224 × 21; one 64 × 64 transposed convolution at stride 32 does it in one step.',
          'Top row: input 224 × 224 × 3, VGG with stride 32, deepest map 7 × 7 × 512, 1 × 1 conv to 7 × 7 × 21. Bottom row: ×2 upsample to 14 × 14 × 21, add the pool4 scores, ×16 upsample to 224 × 224 × 21. Text gives (7 − 1) × 32 − 2 × 16 + 64 = 224.')


# ---- 6.7 clips and late fusion ----
def f7():
    x0, cw = 40, 21
    o = [T(x0, 36, '300 frames, every 10th kept: 30 sampled frames', 14, 'start', INK, True)]
    for k in range(30):
        f = ACS if k < 16 else PANEL
        o += [R(x0 + k * cw, 48, cw, 26, f, L2, 0, 1), T(x0 + k * cw + cw / 2, 66, str(k), 11 if k > 9 else 12, fill=MUT)]
    o += [brace(x0, x0 + 16 * cw, 84, AC), T(x0 + 8 * cw, 104, 'clip 1: frames 0–15', 13, fill=AC, bold=True),
          brace(x0 + 8 * cw, x0 + 24 * cw, 118, NX), T(x0 + 16 * cw, 138, 'clip 2: frames 8–23', 13, fill=NX, bold=True)]
    o.append(T(x0 + 25 * cw, 104, '⌊(30 − 16) ÷ 8⌋ + 1 = 2', 13, 'start', INK, True))
    rows = [['', 'action 1', 'action 2', 'action 3'], ['spatial stream', '0.7', '0.2', '0.1'], ['temporal stream', '0.4', '0.5', '0.1'], ['average', '0.55', '0.35', '0.1']]
    o.append(tab(x0, 160, [150, 90, 90, 90], rows, 30, fills=lambda i, j: NXS if (i, j) == (3, 1) else LVS if (i, j) == (2, 2) else None))
    o += [T(480, 214, 'Fusion picks action 1 at 0.55.', 14, 'start', NX, True), T(480, 240, 'The temporal stream alone', 13, 'start', LV, True),
          T(480, 260, 'would pick action 2 at 0.5.', 13, 'start', LV, True)]
    return 300, ''.join(o)


FIG[7] = (f7, 'A 10 s clip at 30 frames/s has 300 frames; keeping every 10th leaves 30, which give 2 clips of 16 at stride 8. Averaging the two streams gives [0.55, 0.35, 0.1], so action 1 wins.',
          'A strip of 30 sampled frames numbered 0 to 29 with brackets for clip 1 over frames 0 to 15 and clip 2 over frames 8 to 23. A table gives spatial scores 0.7, 0.2, 0.1, temporal scores 0.4, 0.5, 0.1 and their average 0.55, 0.35, 0.1 with action 1 highlighted.')


# ---- 6.8 soft attention for visual QA ----
def f8():
    ox, oy, s = 70, 250, 160
    X = lambda x: ox + x * s
    Y = lambda y: oy - y * s
    o = [ar(X(0), Y(0), X(1.25), Y(0), INK, 1.5), ar(X(0), Y(0), X(0), Y(1.25), INK, 1.5)]
    for (a, b), lab, w in (((1, 0), 'v₁ (1, 0)', '0.5'), ((0, 1), 'v₂ (0, 1)', '0.3'), ((1, 1), 'v₃ (1, 1)', '0.2')):
        o += [ar(X(0), Y(0), X(a) - (6 if a and not b else 4 if a else 0), Y(b) + (6 if b and not a else 4 if b else 0), MUT, 1.6, '5 4'), C(X(a), Y(b), 7, AC)]
        o.append(T(X(a) + (10 if a else 12), Y(b) - 10, f'{lab}, α = {w}', 13, 'start', AC, True))
    o += [ar(X(0), Y(0), X(0.7) - 5, Y(0.5) + 4, NX, 3), C(X(0.7), Y(0.5), 7, NX), Tb(X(0.7) + 12, Y(0.5) + 20, 'c = (0.7, 0.5)', 13, 'start', NX, True)]
    o += [T(20, 296, 'c = 0.5 (1, 0) + 0.3 (0, 1) + 0.2 (1, 1) = (0.7, 0.5);  0.5 + 0.3 + 0.2 = 1.0', 13, 'start', INK, True)]
    o += [boxt(440, 30, 270, 46, ['image: 49 regions × 2048'], ACS, AC, 14, True), boxt(440, 92, 270, 46, ['question: 1024 numbers'], LVS, LV, 14, True),
          ar(575, 76, 575, 90, AC), ar(575, 138, 575, 152, LV),
          boxt(440, 154, 270, 46, ['joined: 2048 + 1024 = 3072'], NXS, NX, 14, True), ar(575, 200, 575, 214, NX),
          boxt(440, 216, 270, 46, ['softmax over 1000 answers'], PANEL, L2, 14, True)]
    return 312, ''.join(o)


FIG[8] = (f8, 'Attention weights 0.5, 0.3 and 0.2 on the regions (1, 0), (0, 1) and (1, 1) give the context c = (0.7, 0.5). In the full model a 2048-number region context joins the 1024-number question to make 3072 numbers for a softmax over 1000 answers.',
          'A plane with three region vectors v₁ (1, 0), v₂ (0, 1) and v₃ (1, 1) labelled with weights 0.5, 0.3 and 0.2, and a context arrow to (0.7, 0.5). On the right a column of boxes: image 49 × 2048, question 1024, joined 3072, softmax over 1000 answers.')


# ---- 6.9 VAE sampling and GAN losses ----
def f9():
    o = [T(20, 30, 'VAE', 14, 'start', AC, True)]
    o.append(chain([(['encoder', 'μ = 0.5, log σ² = −2'], ACS, AC), (['σ² = e⁻² = 0.135', 'σ = 0.368'], ACS, AC),
                    (['z = μ + σε, ε = 1.2', '= 0.5 + 0.368 × 1.2 = 0.942'], NXS, NX)], 40, 20, 210, 25, 56, 13))
    o.append(T(20, 122, 'KL = −½ (1 − 2 − 0.25 − 0.135) = 0.693', 14, 'start', AC, True))
    o.append(T(20, 168, 'GAN', 14, 'start', LV, True))
    for i, s in enumerate(['D(real) = 0.9, D(fake) = 0.1', 'objective = ln 0.9 + ln(1 − 0.1)', '= −0.105 − 0.105 = −0.211', 'generator loss = −ln 0.1 = 2.303']):
        o.append(T(20, 194 + i * 24, s, 14 if i == 3 else 13, 'start', NX if i == 3 else INK, True))
    fx = lambda d: 440 + d * 260
    fy = lambda v: 222 - v * 24
    o += [L(fx(0), fy(0), fx(1), fy(0), L2, 1.5), L(fx(0), fy(4.2), fx(0), fy(-2.6), L2, 1.5)]
    for v in (-2, 0, 2, 4):
        o.append(T(fx(0) - 8, fy(v) + 4, neg(v), 13, 'end', MUT))
    for d in (0, 0.5, 1):
        o.append(T(fx(d), fy(-2.6) + 18, f'{d:g}', 13, fill=MUT))
    o.append(T(fx(0.75), fy(-2.6) + 18, 'D(fake)', 13, fill=MUT))
    o += [curve(lambda d: -math.log(d), 0.0185, 1, fx, fy, NX, 2.6), curve(lambda d: math.log(1 - d), 0, 0.92, fx, fy, LV, 2.4, '6 4')]
    o += [C(fx(0.1), fy(2.303), 6, NX), C(fx(0.1), fy(-0.105), 6, LV)]
    o += [Tb(fx(0.1) + 12, fy(2.303) - 4, '−ln D: 2.303 at 0.1', 13, 'start', NX, True), Tb(fx(0.05), fy(-1.9), 'ln(1 − D): −0.105, flat', 13, 'start', LV, True)]
    o.append(T(440, 112, 'generator signal when D(fake) is small', 13, 'start', INK, True))
    return 316, ''.join(o)


FIG[9] = (f9, 'The VAE turns μ = 0.5 and log σ² = −2 into σ = 0.368 and z = 0.942, with KL = 0.693. In the GAN, D(fake) = 0.1 makes −ln D(fake) = 2.303, a strong signal, while ln(1 − D(fake)) is only −0.105 and nearly flat there.',
          'Top: three boxes from μ = 0.5, log σ² = −2 to σ² = 0.135, σ = 0.368 and z = 0.942, with KL = 0.693 below. Bottom left: the GAN numbers, objective −0.211 and generator loss 2.303. Bottom right: the curves −ln D and ln(1 − D) against D(fake), with dots at D = 0.1.')

spec = make_spec(FIG)
