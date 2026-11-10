"""Claude's hand-drawn figures for c-cv-u1 (Computer Vision, unit 1: digital image fundamentals), one per chapter,
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


def mat(x, y, M, cell=48, hot=None, size=15, f0=PANEL):
    o = []
    for i, row in enumerate(M):
        for j, v in enumerate(row):
            h = hot(i, j) if hot else None
            f, st = h if h else (f0, L2)
            o += [R(x + j * cell, y + i * cell, cell, cell, f, st, 0, 1.6 if h else 1.2), TM(x + j * cell + cell / 2, y + i * cell + cell * 0.62, str(v), size, bold=bool(h))]
    return ''.join(o)


# ---- 1.1 the size of a scanned cheque ----
def f1():
    o = [R(20, 30, 180, 120, PANEL, L2, 4, 1.5)]
    for k in range(1, 6): o.append(L(20 + k * 30, 30, 20 + k * 30, 150, LN, 1))
    for k in range(1, 4): o.append(L(20, 30 + k * 30, 200, 30 + k * 30, LN, 1))
    o += [R(140, 90, 30, 30, ACS, AC, 0, 2), T(110, 170, 'W = 1200 pixels', 13, fill=MUT, bold=True)]
    o.append(f'<text x="226" y="90" font-size="13" text-anchor="middle" transform="rotate(-90 226 90)" style="fill:{MUT}" font-weight="700">H = 800</text>')
    o += [ar(172, 104, 250, 74, AC, 1.5), boxt(252, 40, 180, 64, ['one pixel', '8 bits = 1 byte', 'value 0 to 255'], ACS, AC, 13, True)]
    o += [boxt(470, 30, 230, 50, ['1200 × 800 = 960,000 pixels'], PANEL, L2, 14, True),
          boxt(470, 96, 230, 50, ['× 8 bits = 7,680,000 bits'], PANEL, L2, 14, True),
          boxt(470, 162, 230, 50, ['÷ 8 = 960,000 bytes = 0.96 MB'], NXS, NX, 14, True),
          boxt(470, 228, 230, 50, ['× 3 copies = 2.88 MB'], LVS, LV, 15, True)]
    o += [ar(585, 80, 585, 94, L2), ar(585, 146, 585, 160, L2), ar(585, 212, 585, 226, L2)]
    o.append(T(20, 222, 'Image processing: image in, image out', 14, 'start', AC, True))
    o.append(T(20, 246, '(clean, sharpen, compress this scan).', 13, 'start', MUT))
    o.append(T(20, 280, 'Computer vision: image in, decision out', 14, 'start', NX, True))
    o.append(T(20, 304, '("cheque valid").', 13, 'start', MUT))
    return 318, ''.join(o)


FIG[1] = (f1, 'A 1200 × 800 cheque scan at 8 bits a pixel holds 960,000 pixels, 960,000 bytes or 0.96 MB, and three copies take 2.88 MB.',
          'A grid standing for the 1200 by 800 pixel cheque, with one pixel enlarged as 8 bits, 0 to 255. A column of boxes: 960,000 pixels, 7,680,000 bits, 960,000 bytes = 0.96 MB, and 3 copies = 2.88 MB.')


# ---- 1.2 the functional chain ----
def f2():
    jobs = ['acquire', 'enhance', 'restore', 'colour', 'compress', 'morphology', 'segment', 'describe', 'recognise']
    o = []
    for i, j in enumerate(jobs):
        r, c = divmod(i, 5)
        x = 20 + c * 140 if r == 0 else 20 + (8 - i) * 140 + 140
        y = 30 if r == 0 else 130
        hot = j in ('compress', 'segment', 'recognise')
        f, st = (LVS, LV) if j == 'compress' else (NXS, NX) if hot else (ACS, AC)
        o.append(boxt(x, y, 120, 44, [f'{i + 1}. {j}'], f, st, 14, True))
        if i < 4: o.append(ar(x + 120, y + 22, x + 138, y + 22, AC))
        if 5 <= i < 8: o.append(ar(x, y + 22, x - 18, y + 22, AC))
    o += [P([(580, 74), (580, 100), (630, 100), (630, 128)], AC, 2), ar(630, 120, 630, 128, AC)]
    o += [arc(220, 176, 500, 176, -0.12, NX, 1.8, 'x', '5 4'), T(360, 222, 'reject → re-split', 13, fill=NX, bold=True)]
    o.append(T(20, 252, 'one raw frame: 2048 × 2048 × 12 bits = 50,331,648 bits = 6,291,456 bytes = 6 MiB', 14, 'start', INK, True))
    bw = 600 / 683
    o += [R(20, 266, 682 * bw, 26, LVS, LV, 3, 1.5), R(20 + 682 * bw, 266, 4 * bw + 2, 26, PANEL, L2, 0, 1),
          T(20 + 341 * bw, 284, '682 frames × 6 MiB = 4092 MiB', 13, fill=LV, bold=True), T(640, 284, '4 MiB left', 13, 'start', MUT)]
    o.append(T(20, 320, 'A 4 GiB drive holds 4096 ÷ 6 = 682 whole frames, so compression comes before storage.', 13, 'start', MUT))
    return 334, ''.join(o)


FIG[2] = (f2, 'Nine jobs carry pixels to a label: segmentation turns pixels into objects and recognition names them. A raw frame is 6 MiB, so compression sits before the disk; 682 frames fill a 4 GiB drive.',
          'Nine boxes in a snake: acquire, enhance, restore, colour, compress, then morphology, segment, describe, recognise, with a dashed feedback arrow from recognise back to segment. A bar shows 682 frames of 6 MiB filling 4092 of 4096 MiB.')


# ---- 1.3 Weber's law ----
def f3():
    x0, x1, y0, y1 = 80, 460, 40, 260
    fx = lambda i: x0 + i * (x1 - x0) / 120
    fy = lambda d: y1 - d * (y1 - y0) / 5
    o = [axes(x0, x1, y0, y1, [0, 20, 40, 60, 80, 100, 120], [0, 1, 2, 3, 4, 5], fx, fy, 'background I (cd/m²)', 'just-noticeable ΔI (cd/m²)')]
    o.append(L(fx(0), fy(0), fx(120), fy(4.8), AC, 2.5))
    o.append(Tb(fx(104), fy(4.8) - 6, 'ΔI = 0.04 I', 14, fill=AC, bold=True))
    for i, d, c in [(50, 2, NX), (100, 4, LV)]:
        o += [L(fx(i), fy(d), fx(i), y1, c, 1.5, '4 4'), L(x0, fy(d), fx(i), fy(d), c, 1.5, '4 4'), C(fx(i), fy(d), 7, c)]
    o += [T(fx(50) + 10, fy(2) + 20, '(50, 2)', 13, 'start', NX, True), T(fx(100) + 10, fy(4) + 20, '(100, 4)', 13, 'start', LV, True)]
    o += [boxt(500, 50, 200, 84, ['I = 50, patch 52', 'ΔI = 52 − 50 = 2', 'ΔI ÷ I = 2 ÷ 50 = 0.04'], NXS, NX, 13, True),
          boxt(500, 150, 200, 64, ['I = 100, same fraction', 'ΔI = 0.04 × 100 = 4'], LVS, LV, 13, True)]
    o.append(T(20, 330, 'The eye notices ratios: twice the background needs twice the step.', 14, 'start', INK, True))
    return 344, ''.join(o)


FIG[3] = (f3, 'The Weber rule ΔI = 0.04 I: a step of 2 cd/m² is just visible on a background of 50, and on a background of 100 the step must grow to 4.',
          'A straight line through the origin of just-noticeable step against background intensity, slope 0.04, with points (50, 2) and (100, 4) marked by dashed guides. Side boxes give 52 − 50 = 2, 2 ÷ 50 = 0.04, and 0.04 × 100 = 4.')


# ---- 1.4 a line sensor scanning a page ----
def f4():
    o = [R(40, 40, 180, 240, PANEL, L2, 2, 1.5)]
    for k in range(1, 8): o.append(L(40, 40 + k * 30, 220, 40 + k * 30, LN, 1, '3 3'))
    o += [R(30, 150, 200, 14, ACS, AC, 3, 2), ar(130, 168, 130, 200, AC), T(130, 214, '400 lines a second', 13, fill=AC, bold=True),
          T(130, 30, '4096 elements across', 13, fill=MUT, bold=True)]
    o.append(f'<text x="250" y="160" font-size="13" text-anchor="middle" transform="rotate(-90 250 160)" style="fill:{MUT}" font-weight="700">3000 lines</text>')
    o.append(chain([(['4096 × 3000', '12,288,000 px'], PANEL, L2), (['× 12 bits', '147,456,000 bits'], PANEL, L2)], 40, 290, 190, 20))
    o.append(boxt(500, 120, 190, 56, ['÷ 8', '18,432,000 bytes'], NXS, NX, 13, True))
    o.append(ar(595, 96, 595, 118, NX))
    o += [boxt(290, 120, 190, 56, ['18.432 MB (÷ 10⁶)', '17.578 MiB (÷ 2²⁰)'], ACS, AC, 13, True), ar(500, 148, 482, 148, AC)]
    o.append(boxt(290, 206, 410, 56, ['scan time 3000 ÷ 400 = 7.5 s', 'data rate 18,432,000 ÷ 7.5 ≈ 2.46 MB/s'], LVS, LV, 14, True))
    o.append(T(20, 316, 'The same buffer is 18.432 MB in decimal units but 17.578 MiB in binary units.', 14, 'start', INK, True))
    return 330, ''.join(o)


FIG[4] = (f4, 'A 4096-element line sensor sweeps 3000 lines at 400 a second. At 12 bits a pixel the page holds 18,432,000 bytes, which is 18.432 MB or 17.578 MiB, and the scan takes 7.5 s.',
          'A page with a line sensor bar moving down at 400 lines a second over 3000 lines. Boxes: 12,288,000 pixels, 147,456,000 bits, 18,432,000 bytes, then 18.432 MB or 17.578 MiB, and a scan time of 7.5 s at about 2.46 MB/s.')


# ---- 1.5 thin-lens image ----
def f5():
    sx, sy = 1.1, 4.0
    lx, ay = 560, 150
    X = lambda mm: lx + mm * sx
    Y = lambda mm: ay - mm * sy
    o = [L(6, ay, 712, ay, L2, 1.5), L(lx, 40, lx, 260, AC, 3), T(lx, 32, 'lens, f = 50 mm', 13, fill=AC, bold=True)]
    for f in (-50, 50):
        o += [C(X(f), ay, 4, INK), T(X(f) - 6, ay + 22, 'F', 13, 'end', MUT, True)]
    o += [ar(X(-500), ay, X(-500), Y(20), NX, 3), T(X(-500) + 6, Y(20) - 6, 'object 20 mm', 13, 'start', NX, True)]
    o += [P([(X(-500), Y(20)), (lx, Y(20)), (X(55.56), Y(-2.22))], LV, 1.8),
          P([(X(-500), Y(20)), (X(55.56), Y(-2.22))], LV, 1.8, '6 3')]
    o += [ar(X(55.56), ay, X(55.56), Y(-2.22) + 1, NX, 3), T(X(55.56) + 8, Y(-2.22) + 20, 'image', 13, 'start', NX, True),
          T(X(55.56) + 8, Y(-2.22) + 38, '2.22 mm,', 13, 'start', NX, True), T(X(55.56) + 8, Y(-2.22) + 56, 'inverted', 13, 'start', NX, True)]
    o += [brace(X(-500), lx, 196, MUT), T((X(-500) + lx) / 2, 216, 'u = 500 mm', 14, fill=INK, bold=True),
          brace(lx, X(55.56), 196, MUT), T((lx + X(55.56)) / 2 + 30, 236, 'v = 55.56 mm', 13, fill=INK, bold=True)]
    o.append(T(20, 280, '1/v = 1/50 − 1/500 = 9/500, so v = 55.56 mm;  m = −v/u = −0.111;  hᵢ = −0.111 × 20 = −2.22 mm.', 13, 'start', INK, True))
    o.append(T(20, 304, 'Heights are drawn 4 times larger than distances so the small image can be seen.', 13, 'start', MUT))
    return 318, ''.join(o)


FIG[5] = (f5, 'A 20 mm object 500 mm from a 50 mm lens forms an inverted image 2.22 mm high at 55.56 mm behind it. The ray parallel to the axis bends through the focus; the ray through the centre goes straight.',
          'A ray diagram: an upright object arrow at 500 mm left of the lens, a ray parallel to the axis bending through the focal point, and a dashed ray through the lens centre. They meet at a small inverted image 55.56 mm behind the lens. Braces mark u = 500 mm and v = 55.56 mm.')


# ---- 1.6 2-bit quantization ----
def f6():
    x0, x1, y0, y1 = 80, 420, 40, 270
    fx = lambda t: x0 + (t + 0.5) * (x1 - x0) / 4
    fy = lambda v: y1 - v * (y1 - y0)
    o = [L(x0, y0, x0, y1, L2, 1.5), L(x0, y1, x1, y1, L2, 1.5)]
    for k, lv in enumerate([0, 1 / 3, 2 / 3, 1]):
        o += [L(x0, fy(lv), x1, fy(lv), MUT, 1.2, '6 4'), T(x0 - 8, fy(lv) + 5, ['0', '1/3', '2/3', '1'][k], 13, 'end', MUT),
              T(x1 + 8, fy(lv) + 5, f'code {k}', 13, 'start', AC, True)]
    xs = [0.1, 0.4, 0.7, 0.9]
    q = [0, 1 / 3, 2 / 3, 1]
    for t, (v, l) in enumerate(zip(xs, q)):
        o += [L(fx(t), y1, fx(t), fy(v), L2, 1.2), C(fx(t), fy(v), 6, NX), ar(fx(t), fy(v), fx(t), fy(l) + (4 if l < v else -4), LV, 1.8),
              R(fx(t) - 6, fy(l) - 6, 12, 12, AC, AC, 1, 1), T(fx(t) + 10, fy(v) + 5, f'{v}', 13, 'start', NX, True),
              T(fx(t), y1 + 20, f't = {t}', 13, fill=MUT)]
    rows = [('x', 'code', 'e'), ('0.1', '0', '+0.100'), ('0.4', '1', '+0.067'), ('0.7', '2', '+0.033'), ('0.9', '3', '−0.100')]
    for i, r in enumerate(rows):
        for j, (s, w) in enumerate(zip(r, [56, 56, 80])):
            x = 510 + sum([56, 56, 80][:j])
            o += [R(x, 40 + i * 32, w, 32, PANEL if i == 0 else 'var(--fig)', L2, 0, 1.2), T(x + w / 2, 61 + i * 32, s, 14, bold=i == 0, fill=LV if j == 2 and i else INK)]
    o += [T(510, 222, 'Δ = 1/3, so |e| ≤ Δ/2 = 0.167', 13, 'start', MUT), T(510, 248, 'MSE = 0.02556 ÷ 4', 14, 'start', INK, True),
          T(510, 270, '= 0.00639', 15, 'start', LV, True)]
    o.append(T(20, 316, 'Each sample moves to the nearest of the 4 levels (orange arrows); the stored number is the code.', 13, 'start'))
    return 330, ''.join(o)


FIG[6] = (f6, 'With 2 bits there are 4 levels, 0, 1/3, 2/3 and 1; each sample moves to the nearest and is stored as codes 0, 1, 2, 3. The four errors give a mean squared error of 0.00639.',
          'Four samples 0.1, 0.4, 0.7, 0.9 at t = 0 to 3, each with an orange arrow to the nearest of four dashed levels labelled codes 0 to 3. A table gives the codes and errors +0.100, +0.067, +0.033, −0.100, and MSE 0.00639.')


# ---- 1.7 neighbours and distances ----
def f7():
    g, s = 80, 80
    o = []
    for r in range(3):
        for c in range(3):
            f, st = (ACS, AC) if (r, c) == (1, 1) else (NXS, NX) if (r, c) == (2, 2) else (PANEL, L2)
            o += [R(g + c * s, 30 + r * s, s, s, f, st, 0, 1.5), T(g + c * s + s - 5, 30 + r * s + 18, f'({c},{r})', 13, 'end', MUT)]
    o += [T(g + 1.5 * s, 30 + 1.5 * s - 14, 'p', 18, fill=AC, bold=True), T(g + 2.5 * s, 30 + 2.5 * s - 14, 'q', 18, fill=NX, bold=True)]
    cx, cy = g + 1.5 * s, 30 + 1.5 * s
    qx, qy = g + 2.5 * s, 30 + 2.5 * s
    o += [P([(cx, cy + 14), (cx, qy + 14), (qx - 10, qy + 14)], LV, 2.5), ar(qx - 14, qy + 14, qx - 8, qy + 14, LV, 2.5),
          ar(cx + 10, cy + 10, qx - 10, qy - 10, NX, 2.5)]
    o += [T(cx - 8, (cy + qy) / 2 + 20, '1', 14, 'end', LV, True), T((cx + qx) / 2, qy + 36, '1', 14, fill=LV, bold=True),
          Tb((cx + qx) / 2 + 12, (cy + qy) / 2 - 8, '√2', 14, fill=NX, bold=True)]
    o += [boxt(390, 40, 310, 50, ['D4 (city block) = 1 + 1 = 2'], LVS, LV, 15, True),
          boxt(390, 104, 310, 50, ['D8 (chessboard) = max(1, 1) = 1'], NXS, NX, 15, True),
          boxt(390, 168, 310, 50, ['De = √(1² + 1²) ≈ 1.414'], ACS, AC, 15, True)]
    o.append(T(390, 252, '8-adjacent (D8 = 1), not 4-adjacent (D4 = 2)', 14, 'start', INK, True))
    o.append(T(20, 300, 'A side step costs 1 and a diagonal step √2: q is one of p\'s 8 neighbours but not one of its 4.', 13, 'start'))
    return 314, ''.join(o)


FIG[7] = (f7, 'For p = (1,1) and q = (2,2): two side steps give D4 = 2, one diagonal step gives D8 = 1, and the straight line gives De ≈ 1.414. So q is 8-adjacent to p but not 4-adjacent.',
          'A 3 by 3 pixel grid with p at the centre (1,1) and q at the corner (2,2). An orange path of two unit steps and a green diagonal of length √2 join them. Boxes give D4 = 2, D8 = 1 and De ≈ 1.414.')


# ---- 1.8 arithmetic, logical and geometric ----
def f8():
    A = [[200, 50], [10, 240]]
    B = [[100, 20], [250, 30]]
    S = [[255, 70], [255, 255]]
    N = [[64, 16], [10, 16]]
    Rr = [[10, 200], [240, 50]]
    o = [T(68, 26, 'A', 15, fill=INK, bold=True), mat(20, 36, A), T(208, 26, 'B', 15, fill=INK, bold=True), mat(160, 36, B)]
    o += [T(80, 172, 'A + B, saturated', 14, fill=AC, bold=True), mat(32, 182, S, hot=lambda i, j: (LVS, LV) if S[i][j] == 255 else None),
          T(80, 296, '300, 260, 270 → 255', 13, fill=LV, bold=True)]
    o += [T(300, 172, 'A AND B', 14, fill=AC, bold=True), mat(252, 182, N, hot=lambda i, j: (ACS, AC))]
    o += [T(520, 172, 'A rotated 90° clockwise', 14, fill=AC, bold=True), mat(472, 182, Rr, hot=lambda i, j: (NXS, NX))]
    o += [boxt(330, 30, 370, 104, ['200 = 11001000', '100 = 01100100', 'AND = 01000000 = 64'], PANEL, L2, 14, True)]
    o.append(T(472, 316, 'new[r][c] = old[1 − c][r]', 13, 'start', MUT))
    return 330, ''.join(o)


FIG[8] = (f8, 'The same A and B give three different arrays: the 8-bit sum clips 300, 260 and 270 to 255, AND works bit by bit (200 AND 100 = 64), and the rotation only moves the entries.',
          'Arrays A = [[200, 50], [10, 240]] and B = [[100, 20], [250, 30]]. Below: A + B saturated = [[255, 70], [255, 255]] with clipped cells shaded; A AND B = [[64, 16], [10, 16]]; A rotated 90° clockwise = [[10, 200], [240, 50]]. A box works 200 AND 100 in binary.')


# ---- 1.9 RGB to HSI ----
def f9():
    o = [T(20, 26, 'RGB = (255, 128, 0)', 15, 'start', INK, True)]
    for i, (nm, v) in enumerate([('R', 255), ('G', 128), ('B', 0)]):
        y = 44 + i * 40
        o += [T(36, y + 20, nm, 15, 'middle', INK, True), R(50, y, 255, 28, 'none', L2, 3, 1), R(50, y, max(v, 1), 28, ACS, AC, 3, 1.5),
              T(60 + max(v, 1), y + 19, str(v), 14, 'start', AC, True)]
    o += [T(20, 184, 'I = (255 + 128 + 0) ÷ 3 = 127.67', 14, 'start', INK, True),
          T(20, 210, 'S = 1 − 3 × min ÷ sum = 1 − 0 = 1.00', 14, 'start', INK, True),
          T(20, 236, 'H = 60° × (128 − 0) ÷ 255 = 30.1° (red case)', 14, 'start', LV, True)]
    cx, cy, r = 560, 140, 100
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" style="fill:none;stroke:{L2};stroke-width:2"/>')
    for ang, s in [(0, 'red 0°'), (120, 'green 120°'), (240, 'blue 240°')]:
        a = math.radians(ang)
        x, y = cx + r * math.cos(a), cy - r * math.sin(a)
        o += [C(x, y, 5, INK)]
        tx, ty = cx + (r + 14) * math.cos(a), cy - (r + 14) * math.sin(a)
        o.append(T(tx, ty + 5, s, 13, 'start' if ang == 0 else 'end' if ang == 120 else 'end', MUT, True))
    a = math.radians(30.1)
    hx, hy = cx + r * math.cos(a), cy - r * math.sin(a)
    o += [ar(cx, cy, hx - 6, hy + 4, LV, 3), C(hx, hy, 7, LV), T(hx + 10, hy - 6, 'H = 30.1°', 14, 'start', LV, True),
          arc(cx + 40, cy, cx + 40 * math.cos(a), cy - 40 * math.sin(a), 0.2, LV, 1.5, None), C(cx, cy, 3, INK)]
    o.append(T(20, 300, 'A fully saturated orange (S = 1) of middle brightness (I = 127.67).', 14, 'start', NX, True))
    return 314, ''.join(o)


FIG[9] = (f9, 'For RGB (255, 128, 0) the intensity is 383 ÷ 3 = 127.67 and saturation is 1 because blue is 0. Red is the largest channel, so hue is 60° × 128 ÷ 255 = 30.1°, an orange.',
          'Three bars for R 255, G 128 and B 0 with the formulas for I = 127.67, S = 1.00 and H = 30.1°. A hue circle marks red at 0°, green at 120° and blue at 240°, with an arrow at 30.1°.')

spec = make_spec(FIG)
