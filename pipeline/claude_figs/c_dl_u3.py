"""Claude's hand-drawn figures for c-dl-u3 (Deep Learning, unit 3: convolutional networks), one per chapter, from each
chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def grid(o, x, y, M, cw=40, hot=None, fills=None, size=15, bold_hot=True):
    """draw a matrix; hot = set of (i, j) to highlight; fills = dict (i, j) -> (fill, stroke)"""
    for i, row in enumerate(M):
        for j, v in enumerate(row):
            f, s = (fills or {}).get((i, j), (ACS, AC) if hot and (i, j) in hot else (PANEL, L2))
            o.append(R(x + j * cw, y + i * cw, cw, cw, f, s, 0, 1.4))
            h = hot and (i, j) in hot
            o.append(T(x + j * cw + cw / 2, y + i * cw + cw / 2 + size * 0.35, neg(v), size, bold=bool(h and bold_hot)))


def frame(o, x, y, w, h, c=AC, sw=3):
    o.append(R(x, y, w, h, 'none', c, 2, sw))


def shape_box(o, x, y, w, h, lines, c=AC, fill=ACS):
    o.append(boxt(x, y, w, h, lines, fill, c, 13, bold_first=True))


# ---- 3.1 one step of convolution ----
def f1():
    I = [[1, 2, 3, 0], [0, 1, 2, 3], [3, 2, 1, 0], [0, 1, 2, 1]]
    K = [[1, 0, -1], [1, 0, -1], [1, 0, -1]]
    Y = [[-2, 2], [-2, 0]]
    o = [T(100, 26, 'input 4 × 4', 14, bold=True), T(350, 26, 'kernel 3 × 3', 14, bold=True), T(560, 26, 'output 2 × 2', 14, bold=True)]
    grid(o, 20, 40, I, hot={(i, j) for i in range(3) for j in range(3)})
    frame(o, 20, 40, 120, 120)
    o.append(T(196, 128, '×', 26, fill=MUT))
    grid(o, 290, 60, K, fills={(i, j): (NXS, NX) for i in range(3) for j in range(3)})
    o.append(T(446, 128, '=', 26, fill=MUT))
    grid(o, 520, 80, Y, cw=48, hot={(0, 0)}, size=17)
    frame(o, 520, 80, 48, 48)
    o.append(T(20, 214, 'Multiply the shaded window by the kernel, cell by cell, and add:', 14, 'start', bold=True))
    rows = [('row 1:', '1·1 + 2·0 + 3·(−1)', '= −2'), ('row 2:', '0·1 + 1·0 + 2·(−1)', '= −2'), ('row 3:', '3·1 + 2·0 + 1·(−1)', '= 2')]
    for i, (a, b, c) in enumerate(rows):
        y = 242 + i * 24
        o.append(T(30, y, a, 13, 'start', MUT)); o.append(T(90, y, b, 14, 'start')); o.append(T(300, y, c, 14, 'start', bold=True))
    o.append(T(30, 322, 'total −2 − 2 + 2 = −2, the first output cell', 14, 'start', AC, True))
    o.append(T(420, 250, 'Slide one step right, then down,', 13, 'start'))
    o.append(T(420, 270, 'for the other three cells: 2, −2, 0.', 13, 'start'))
    o.append(T(420, 296, 'Size: (4 − 3) ÷ 1 + 1 = 2', 13, 'start', MUT))
    return 340, ''.join(o)
FIG[1] = (f1, 'The 3 × 3 kernel covers the top-left window of the input; multiplying cell by cell and adding gives −2, the first output value. Sliding the window right and down gives 2, −2 and 0.',
          'A 4 by 4 input with its top-left 3 by 3 window shaded, times the vertical-edge kernel, equals a 2 by 2 output whose first cell −2 is highlighted, with the row products written out.')


# ---- 3.2 max pooling ----
def f2():
    M = [[1, 3, 2, 4], [5, 6, 1, 2], [0, 2, 7, 1], [3, 1, 4, 8]]
    colours = {(0, 0): (ACS, AC), (0, 1): (LVS, LV), (1, 0): (NXS, NX), (1, 1): (PANEL, INK)}
    fills = {(i, j): colours[(i // 2, j // 2)] for i in range(4) for j in range(4)}
    maxes = {(1, 1), (0, 3), (3, 0), (3, 3)}
    o = [T(120, 26, 'input 4 × 4, windows 2 × 2, stride 2', 14, bold=True)]
    cw = 50
    for i, row in enumerate(M):
        for j, v in enumerate(row):
            f, s = fills[(i, j)]
            o.append(R(20 + j * cw, 40 + i * cw, cw, cw, f, LN, 0, 1))
            o.append(T(20 + j * cw + cw / 2, 40 + i * cw + 31, str(v), 17 if (i, j) in maxes else 15, fill=s if (i, j) in maxes else MUT, bold=(i, j) in maxes))
    for (a, b), (f, s) in colours.items():
        frame(o, 20 + b * 100, 40 + a * 100, 100, 100, s, 2.5)
    o.append(L(250, 140, 330, 140, AC, 2.5, arrow='n'))
    o.append(T(290, 128, 'keep the', 13, fill=MUT)); o.append(T(290, 166, 'largest', 13, fill=MUT))
    out = [[6, 4], [3, 8]]
    for i in range(2):
        for j in range(2):
            f, s = colours[(i, j)]
            o.append(R(350 + j * 70, 70 + i * 70, 70, 70, f, s, 0, 2.5))
            o.append(T(350 + j * 70 + 35, 70 + i * 70 + 42, str(out[i][j]), 22, fill=s, bold=True))
    o.append(T(420, 230, 'output 2 × 2', 14, bold=True))
    o.append(T(530, 90, 'Each window gives one number:', 13, 'start'))
    for k, s in enumerate(['1, 3, 5, 6 → 6', '2, 4, 1, 2 → 4', '0, 2, 3, 1 → 3', '7, 1, 4, 8 → 8']):
        c = list(colours.values())[k][1]
        o.append(T(530, 116 + k * 22, s, 13, 'start', c, True))
    o.append(T(360, 270, 'Size: (4 − 2) ÷ 2 + 1 = 2. Pooling has no weights to learn.', 14, bold=True))
    return 286, ''.join(o)
FIG[2] = (f2, 'The four 2 × 2 windows do not overlap. Each keeps only its largest value, so the output is [[6, 4], [3, 8]].',
          'A 4 by 4 feature map divided into four coloured 2 by 2 windows, with each window’s largest value 6, 4, 3 and 8 carried into a 2 by 2 output.')


# ---- 3.3 shapes through Conv, Pool, Conv, Pool ----
def f3():
    stages = [('input', '32×32×3', '', 32, 3, L2, PANEL), ('Conv A', '32×32×16', '448 params', 32, 16, AC, ACS),
              ('pool', '16×16×16', '0 params', 16, 16, NX, NXS), ('Conv B', '16×16×32', '', 16, 32, AC, ACS),
              ('pool', '8×8×32', '0 params', 8, 32, NX, NXS), ('flatten', '2048', '', 0, 0, LV, LVS)]
    o = []
    x = 20
    base = 130
    for i, (name, shp, par, hgt, ch, c, cs) in enumerate(stages):
        if name == 'flatten':
            w, h = 22, 150
        else:
            w, h = 8 + ch * 2.2, hgt * 4.2
        o.append(R(x, base - h / 2, w, h, cs, c, 3, 1.8))
        cx = x + w / 2
        o.append(T(cx, base + 100, name, 14, bold=True, fill=c if c != L2 else INK))
        o.append(TM(cx, base + 120, shp, 13))
        if par: o.append(T(cx, base + 138, par, 13, fill=c, bold=par.startswith('448')))
        if i < len(stages) - 1:
            o.append(L(x + w + 8, base, x + w + 38, base, AC, 2, arrow='n'))
        x += w + 48
    o.append(T(20, 22, 'Height of each block = image size; width = number of channels', 13, 'start', MUT))
    o.append(T(20, 312, 'Conv A: 3 × 3 × 3 × 16 = 432 weights + 16 biases = 448. Each 2 × 2 pool halves height and width.', 13, 'start'))
    o.append(T(20, 334, 'Flatten: 8 × 8 × 32 = 2048 numbers.', 13, 'start', LV, True))
    return 350, ''.join(o)
FIG[3] = (f3, 'Padding 1 keeps each convolution’s height and width, and each 2 × 2 pool halves them: 32 → 16 → 8. The final 8 × 8 × 32 map flattens to 2048 numbers, and Conv A alone has 448 parameters.',
          'Six blocks drawn to scale, input 32×32×3, Conv A 32×32×16, pool 16×16×16, Conv B 16×16×32, pool 8×8×32 and a flatten bar of 2048, with parameter counts under the convolution and pools.')


# ---- 3.4 first-layer kernels: AlexNet, ZFNet, VGG ----
def f4():
    nets = [('AlexNet', 11, 96, '11 × 11 × 3 × 96 + 96', '34,944', LV, LVS), ('ZFNet', 7, 96, '7 × 7 × 3 × 96 + 96', '14,208', AC, ACS),
            ('VGG16', 3, 64, '3 × 3 × 3 × 64 + 64', '1,792', NX, NXS)]
    o = [T(20, 26, 'First convolution of each network (kernel drawn to scale)', 14, 'start', bold=True)]
    cw = 13
    for i, (n, k, f, form, p, c, cs) in enumerate(nets):
        x0 = 30 + i * 230
        y0 = 50
        for a in range(k):
            for b in range(k):
                o.append(R(x0 + b * cw, y0 + a * cw, cw, cw, cs, c, 0, 0.8))
        o.append(T(x0 + 75, y0 + 11 * cw + 28, f'{n}: {k} × {k}', 15, fill=c, bold=True))
        o.append(T(x0 + 75, y0 + 11 * cw + 50, form, 13))
        o.append(T(x0 + 75, y0 + 11 * cw + 72, f'= {p} parameters', 14, fill=c, bold=True))
    y = 300
    o.append(T(20, y, 'VGG16 block 1 on a 224 × 224 × 3 image:', 14, 'start', bold=True))
    steps = [('conv 3×3, 64', '224×224×64'), ('conv 3×3, 64', '224×224×64'), ('max pool 2×2', '112×112×64')]
    for i, (a, b) in enumerate(steps):
        x = 30 + i * 230
        o.append(boxt(x, y + 14, 190, 50, [a, b], NXS if i < 2 else PANEL, NX if i < 2 else L2, 13, bold_first=True))
        if i < 2: o.append(L(x + 192, y + 39, x + 226, y + 39, AC, 2, arrow='n'))
    o.append(T(360, y + 92, 'Smaller kernels, more layers: padding 1 keeps 224, the pool halves it to 112.', 13))
    return y + 108, ''.join(o)
FIG[4] = (f4, 'The first kernel shrinks from 11 × 11 in AlexNet to 7 × 7 in ZFNet and 3 × 3 in VGG16, and the first layer’s parameters fall from 34,944 to 14,208 to 1,792. VGG16’s first block turns 224 × 224 × 3 into 112 × 112 × 64.',
          'Three kernels drawn to scale, 11 by 11, 7 by 7 and 3 by 3, with their parameter counts 34,944, 14,208 and 1,792, above VGG16’s first block of two 3 by 3 convolutions and a 2 by 2 pool.')


# ---- 3.5 ResNet bottleneck ----
def f5():
    o = []
    y = 170
    items = [('56×56×64', 'input x', '', PANEL, L2, 90), ('1×1, 16', '56×56×16', '1040', ACS, AC, 92), ('3×3, 16, pad 1', '56×56×16', '2320', ACS, AC, 116),
             ('1×1, 64', '56×56×64', '1088', ACS, AC, 92)]
    xs = []
    x = 20
    for i, (a, b, p, f, c, w) in enumerate(items):
        o.append(boxt(x, y - 34, w, 68, [a, b], f, c, 13, bold_first=True))
        if p: o.append(T(x + w / 2, y + 56, f'{p} params', 13, fill=AC, bold=True))
        xs.append((x, w))
        o.append(L(x + w + 4, y, x + w + 24, y, AC, 2.2, arrow='n'))
        x += w + 28
    o.append(f'<circle cx="{x + 20:.1f}" cy="{y}" r="20" style="fill:var(--next-soft);stroke:var(--next);stroke-width:2"/>')
    o.append(T(x + 20, y + 8, '+', 24, fill=NX, bold=True))
    o.append(L(x + 42, y, x + 64, y, NX, 2.2, arrow='x'))
    o.append(boxt(x + 68, y - 34, 92, 68, ['56×56×64', 'output'], NXS, NX, 13, bold_first=True))
    sx = xs[0][0] + xs[0][1] / 2
    o.append(P([(sx, y - 36), (sx, 60), (x + 20, 60), (x + 20, y - 24)], NX, 2.5, '7 5'))
    o.append(L(x + 20, y - 40, x + 20, y - 23, NX, 2.5, arrow='x'))
    o.append(T((sx + x + 20) / 2, 50, 'identity shortcut: x is added back unchanged', 13, fill=NX, bold=True))
    o.append(T(360, 290, 'Conv path: 1040 + 2320 + 1088 = 4448 parameters (weights + biases).', 14, bold=True))
    o.append(T(360, 312, 'Shapes match (56×56×64), so the addition needs no extra weights.', 13))
    return 328, ''.join(o)
FIG[5] = (f5, 'The bottleneck squeezes 64 channels to 16, works at 3 × 3, and expands back to 64, costing 1040 + 2320 + 1088 = 4448 parameters. Because the output is again 56 × 56 × 64, the shortcut can add the input back unchanged.',
          'A row of boxes from a 56×56×64 input through 1×1, 3×3 and 1×1 convolutions with their parameter counts, into an add node that also receives a dashed identity shortcut from the input.')


# ---- 3.6 transfer learning plans ----
def f6():
    o = []
    def row(y, title, train_last, lr):
        o.append(T(20, y - 14, title, 14, 'start', bold=True))
        x = 20
        for k in range(4):
            last = k == 3
            tr = last and train_last
            o.append(R(x, y, 96, 50, NXS if tr else PANEL, NX if tr else L2, 6, 1.6, None if tr else '5 4'))
            o.append(T(x + 48, y + 22, f'block {k + 1}', 13, bold=True, fill=INK if tr else MUT))
            o.append(T(x + 48, y + 40, 'trained' if tr else 'frozen', 13, fill=NX if tr else MUT))
            x += 104
        o.append(boxt(x, y, 100, 50, ['global pool', '2048'], PANEL, L2, 13))
        o.append(L(x + 102, y + 25, x + 128, y + 25, AC, 2, arrow='n'))
        o.append(boxt(x + 132, y, 140, 50, ['new head: 10', 'trained'], NXS, NX, 13, bold_first=True))
        o.append(T(700, y + 70, lr, 13, 'end', MUT))
    row(46, '2,000 images: train only the new head', False, 'pretrained base unchanged')
    row(170, '50,000 images: also unfreeze the last block', True, 'small learning rate, e.g. 1e-4')
    o.append(T(20, 300, 'New head: 10 × 2,048 weights + 10 biases = 20,480 + 10 = 20,490 parameters.', 14, 'start', bold=True))
    o.append(T(20, 322, 'Use the pretrained input size, mean and standard deviation in both plans.', 13, 'start', MUT))
    return 338, ''.join(o)
FIG[6] = (f6, 'The 1000-class head of ResNet-50 is replaced by a 10-class head of 20,490 parameters. With 2,000 images only that head is trained; with 50,000 images the last block is unfrozen too, with a small learning rate.',
          'Two rows of a ResNet-50 drawn as four blocks, global pooling and a new 10-class head: in the first only the head is trained, in the second the last block is trained as well.')


# ---- 3.7 Grad-CAM heat map ----
def f7():
    o = []
    A1 = [[1, 0], [0, 1]]; A2 = [[0, 2], [2, 0]]; S = [['0.5', '2'], ['2', '0.5']]
    def small(x, y, M, title, c=L2, cs=PANEL):
        o.append(T(x + 40, y - 10, title, 13, bold=True))
        for i in range(2):
            for j in range(2):
                o.append(R(x + j * 40, y + i * 40, 40, 40, cs, c, 0, 1.4))
                o.append(T(x + j * 40 + 20, y + i * 40 + 26, str(M[i][j]), 15, bold=True))
    small(70, 70, A1, 'A1'); o.append(T(62, 112, '0.5 ×', 15, 'end', AC, True))
    o.append(T(172, 112, '+', 22, fill=MUT))
    small(240, 70, A2, 'A2'); o.append(T(232, 112, '1.0 ×', 15, 'end', AC, True))
    o.append(T(342, 112, '=', 22, fill=MUT))
    small(366, 70, S, 'weighted sum', AC, ACS)
    o.append(L(456, 110, 516, 110, AC, 2.5, arrow='n')); o.append(T(486, 100, 'ReLU', 13, fill=MUT))
    vals = [[0.5, 2], [2, 0.5]]
    o.append(T(570, 60, 'heat map', 13, bold=True))
    for i in range(2):
        for j in range(2):
            v = vals[i][j]
            o.append(R(530 + j * 40, 70 + i * 40, 40, 40, 'var(--live)', LV, 0, 1.4).replace('fill:var(--live)', f'fill:var(--live);fill-opacity:{0.2 + 0.35 * v:.2f}'))
            o.append(T(530 + j * 40 + 20, 70 + i * 40 + 26, f'{v:g}', 15, bold=True))
    o.append(T(14, 30, 'Weight each feature map by how much it matters for the class, add, then keep positives', 13, 'start', MUT))
    o.append(T(20, 200, 'Cell by cell: (0,0) 0.5 + 0 = 0.5, (0,1) 0 + 2 = 2, (1,0) 0 + 2 = 2, (1,1) 0.5 + 0 = 0.5.', 13, 'start'))
    o.append(T(20, 224, 'All sums are positive, so ReLU changes nothing: the darker cells mark where the class evidence is.', 13, 'start', LV, True))
    return 240, ''.join(o)
FIG[7] = (f7, 'Each feature map is multiplied by its weight for the class and the results are added cell by cell, giving [[0.5, 2], [2, 0.5]]. Every entry is positive, so ReLU leaves it as the heat map.',
          'Two 2 by 2 feature maps A1 and A2 multiplied by 0.5 and 1.0, added into a weighted sum, then passed through ReLU into a shaded heat map with values 0.5, 2, 2 and 0.5.')


# ---- 3.8 YOLO output ----
def f8():
    o = [T(20, 26, 'S = 7 grid, B = 2 boxes per cell, C = 20 classes', 14, 'start', bold=True)]
    gx, gy, cw = 20, 44, 30
    for i in range(7):
        for j in range(7):
            hot = (i, j) == (3, 4)
            o.append(R(gx + j * cw, gy + i * cw, cw, cw, LVS if hot else PANEL, LV if hot else L2, 0, 2 if hot else 1))
    o.append(T(gx + 105, gy + 232, '49 cells', 13, fill=MUT))
    hx, hy = gx + 4 * cw + cw, gy + 3 * cw + cw / 2
    o.append(L(hx, hy, 296, 120, LV, 1.8, arrow='l'))
    x0, y0, s = 300, 100, 13.5
    parts = [('box 1', 5, AC, ACS), ('box 2', 5, AC, ACS), ('20 class scores', 20, NX, NXS)]
    x = x0
    for name, n, c, cs in parts:
        for k in range(n):
            o.append(R(x + k * s, y0, s, 40, cs, c, 0, 0.9))
        o.append(T(x + n * s / 2, y0 + 62, name, 13, fill=c, bold=True))
        x += n * s
    o.append(T(x0, y0 - 14, 'one cell predicts 2 × 5 + 20 = 30 numbers', 13, 'start', bold=True))
    o.append(T(x0, y0 + 84, 'each box: x, y, w, h, confidence', 13, 'start', MUT))
    o.append(T(x0, 236, 'whole output: 7 × 7 × 30 = 1470 numbers', 14, 'start', bold=True))
    o.append(T(x0, 260, 'boxes before NMS: 7 × 7 × 2 = 98', 14, 'start', bold=True))
    o.append(T(x0, 290, 'dog score = confidence × class score', 13, 'start'))
    o.append(T(x0, 310, '= 0.9 × 0.8 = 0.72', 14, 'start', LV, True))
    return 326, ''.join(o)
FIG[8] = (f8, 'Every one of the 49 grid cells predicts two boxes of 5 numbers and 20 class scores, 30 numbers in all, so the output is 7 × 7 × 30 = 1470 numbers and 98 boxes. A box with confidence 0.9 and dog score 0.8 scores 0.72 for dog.',
          'A 7 by 7 grid with one cell highlighted and its prediction drawn as a strip of 30 numbers: two boxes of five and twenty class scores, with the totals 1470 numbers and 98 boxes.')


# ---- 3.9 U-Net shapes ----
def f9():
    o = []
    def blk(x, y, w, h, top, bot, c=AC, cs=ACS):
        o.append(R(x, y, w, h, cs, c, 3, 1.8))
        o.append(TM(x + w / 2, y + h + 18, top, 13, bold=True))
        if bot: o.append(T(x + w / 2, y + h + 36, bot, 13, fill=MUT))
    blk(30, 50, 14, 160, '128×128×3', 'image', L2, PANEL)
    o.append(L(50, 130, 128, 130, AC, 2, arrow='n')); o.append(T(88, 120, 'conv', 13, fill=MUT))
    blk(134, 50, 40, 160, '128×128×64', 'encoder')
    o.append(L(154, 252, 154, 274, LV, 2, arrow='l')); o.append(T(162, 268, 'pool', 13, 'start', LV))
    blk(138, 280, 32, 80, '64×64×64', '', LV, LVS)
    o.append(L(176, 320, 350, 320, NX, 2)); o.append(L(350, 320, 350, 254, NX, 2, arrow='x')); o.append(T(262, 310, 'upsample × 2', 13, fill=NX))
    blk(330, 50, 40, 160, '128×128×64', 'upsampled', NX, NXS)
    o.append(P([(154, 46), (154, 30), (490, 30), (490, 40)], AC, 2, '6 4'))
    o.append(L(490, 34, 490, 46, AC, 2, arrow='n'))
    o.append(T(322, 22, 'skip: copy the encoder map', 13, fill=AC, bold=True))
    o.append(L(374, 130, 446, 130, AC, 2, arrow='n')); o.append(T(410, 120, 'concat', 13, fill=MUT))
    blk(450, 50, 80, 160, '128×128×128', '64 + 64 channels', AC, ACS)
    o.append(L(536, 130, 598, 130, AC, 2, arrow='n')); o.append(T(567, 120, '1×1, 5', 13, fill=MUT))
    blk(604, 50, 16, 160, '128×128×5', 'mask', LV, LVS)
    o.append(T(420, 290, 'Last 1×1 conv: 128 × 5 = 640 weights', 13, 'start', bold=True))
    o.append(T(420, 310, '+ 5 biases = 645 parameters', 13, 'start', LV, True))
    o.append(T(420, 336, '5 class scores per pixel,', 13, 'start'))
    o.append(T(420, 354, 'for all 16,384 pixels', 13, 'start'))
    return 388, ''.join(o)
FIG[9] = (f9, 'The encoder map (128 × 128 × 64) is pooled to 64 × 64 and upsampled back, then the skip joins it to the upsampled map, making 128 channels. A 1 × 1 convolution with 5 filters, only 645 parameters, gives 5 class scores per pixel.',
          'A small U-Net: the image, an encoder block of 128×128×64, a pooled 64×64×64 block, an upsampled block, a dashed skip copying the encoder map into a 128-channel concatenation, and the 128×128×5 mask.')


spec = make_spec(FIG)
