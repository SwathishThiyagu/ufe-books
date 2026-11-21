"""Claude's hand-drawn figures for ec-vlsi-u6 (VLSI Design: VLSI testing and design for testability), one per chapter,
drawn from each chapter's own worked example and numbers. Colours are the shell's CSS variables."""
import os, sys, math, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

_T, _Tb, _boxt = T, Tb, boxt


def _sub(s):
    """W_64, D_1 ... drawn as real subscripts, never as underscores"""
    return re.sub(r'([A-Za-zα-ω])_([A-Za-z0-9]+)', r'\1<tspan baseline-shift="sub" font-size="11">\2</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)
def boxt(x, y, w, h, lines, *a, **k): return _boxt(x, y, w, h, [_sub(l) for l in lines], *a, **k)


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


def nand_gate(x, y, h=56, c=AC, label=None, fill=PANEL):
    """NAND body with its left edge at x, centred at y; returns (svg, output x)"""
    w = h * 0.55
    d = (f'M{x:.1f},{y - h / 2:.1f} H{x + w:.1f} A{h / 2:.1f},{h / 2:.1f} 0 0 1 {x + w:.1f},{y + h / 2:.1f} H{x:.1f} Z')
    o = [f'<path d="{d}" style="fill:{fill};stroke:{c};stroke-width:2"/>',
         f'<circle cx="{x + w + h / 2 + 6:.1f}" cy="{y:.1f}" r="6" style="fill:{fill};stroke:{c};stroke-width:2"/>']
    if label: o.append(T(x + w * 0.75, y + 5, label, 13, bold=True))
    return ''.join(o), x + w + h / 2 + 12


def and_gate(x, y, h=50, c=AC, label=None, fill=PANEL):
    w = h * 0.55
    d = (f'M{x:.1f},{y - h / 2:.1f} H{x + w:.1f} A{h / 2:.1f},{h / 2:.1f} 0 0 1 {x + w:.1f},{y + h / 2:.1f} H{x:.1f} Z')
    o = [f'<path d="{d}" style="fill:{fill};stroke:{c};stroke-width:2"/>']
    if label: o.append(T(x + w * 0.8, y + 5, label, 13, bold=True))
    return ''.join(o), x + w + h / 2


def xor_gate(cx, cy, r=15, c=AC):
    return (f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" style="fill:{PANEL};stroke:{c};stroke-width:2"/>'
            + L(cx - r + 3, cy, cx + r - 3, cy, c, 2) + L(cx, cy - r + 3, cx, cy + r - 3, c, 2))


# ---- 6.1 defect level against fault coverage (worked example: Y = 0.90, T = 0.95 and 0.99) ----
def f1():
    o = []
    x0, x1, y0, y1 = 92, 600, 40, 300
    fx = lin(0.90, 1.00, x0, x1); fy = lin(0, 12000, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0.90, 0.92, 0.94, 0.96, 0.98, 1.00], [0, 2000, 4000, 6000, 8000, 10000, 12000], fx, fy,
                  'fault coverage T', 'defect level (DPM)', lambda v: f'{v:.2f}', lambda v: f'{v:,}'))
    for Y, c, lab in ((0.90, AC, 'Y = 0.90'), (0.95, LV, 'Y = 0.95')):
        pts = [(fx(t), fy((1 - Y ** (1 - t)) * 1e6)) for t in [0.90 + 0.0025 * i for i in range(41)]]
        o.append(P(pts, c, 2.5))
        o.append(T(fx(0.90) + 10, pts[0][1] - 8 if Y == 0.90 else pts[0][1] + 34, lab, 14, 'start', fill=c, bold=True))
    for t, dpm, lab, dx, anc in ((0.95, 5254, 'T = 0.95: 5254 DPM', 14, 'start'), (0.99, 1053, 'T = 0.99: 1053 DPM', -12, 'end')):
        o.append(L(fx(t), fy(dpm), fx(t), y1, L2, 1.5, dash='4 4'))
        o.append(C(fx(t), fy(dpm), 6, NX))
        o.append(Tb(fx(t) + dx, fy(dpm) - 14, lab, 14, anc, fill=NX, bold=True))
    o.append(T(612, fy(1053) - 30, 'about', 13, 'start', fill=MUT))
    o.append(T(612, fy(1053) - 12, '5 × fewer', 13, 'start', fill=MUT))
    o.append(T(612, fy(1053) + 6, 'bad parts', 13, 'start', fill=MUT))
    o.append(T(360, 368, 'DL = 1 − Y^(1 − T); every point of coverage near the top cuts escapes steeply'.replace('^(1 − T)', '<tspan baseline-shift="super" font-size="11">(1 − T)</tspan>'), 14))
    return 384, ''.join(o)


# ---- 6.2 the NAND gate and its six faults (worked example 1) ----
def f2():
    o = []
    g, zx = nand_gate(70, 120, 64)
    o.append(g)
    o.append(L(36, 100, 70, 100, INK, 2)); o.append(L(36, 140, 70, 140, INK, 2)); o.append(L(zx, 120, zx + 30, 120, INK, 2))
    o.append(T(14, 105, 'A', 15, 'start', bold=True)); o.append(T(14, 145, 'B', 15, 'start', bold=True))
    o.append(T(zx + 34, 125, 'Z', 15, 'start', bold=True))
    o.append(T(100, 200, 'Z = NOT (A·B)', 14, fill=MUT))
    cols = ['00', '01', '10', '11']
    rows = [('good', [1, 1, 1, 0], None), ('A/0', [1, 1, 1, 1], 'c1'), ('B/0', [1, 1, 1, 1], 'c1'), ('Z/1', [1, 1, 1, 1], 'c1'),
            ('A/1', [1, 0, 1, 0], 'c2'), ('B/1', [1, 1, 0, 0], 'c3'), ('Z/0', [0, 0, 0, 0], 'c4')]
    tx, ty, cw, rh = 260, 40, 62, 36
    o.append(T(tx + 40, ty + 4, 'AB =', 14, 'middle', fill=MUT))
    for j, c in enumerate(cols):
        o.append(T(tx + 110 + j * cw, ty + 4, c, 14, bold=True))
    good = rows[0][1]
    for i, (name, vals, cls) in enumerate(rows):
        y = ty + 22 + i * rh
        if i == 1: o.append(L(tx, y - 2, tx + 110 + 3 * cw + 34, y - 2, L2, 1.5))
        o.append(T(tx + 40, y + 22, name, 14, bold=(i == 0)))
        for j, v in enumerate(vals):
            diff = i > 0 and v != good[j]
            if diff: o.append(R(tx + 110 + j * cw - 22, y + 4, 44, 28, NXS, NX, 6))
            o.append(T(tx + 110 + j * cw, y + 23, str(v), 14, bold=diff, fill=NX if diff else INK))
    bx = tx + 110 + 3 * cw + 44
    y1, y2 = ty + 22 + rh + 6, ty + 22 + 4 * rh - 6
    o.append(P([(bx, y1), (bx + 8, y1), (bx + 8, y2), (bx, y2)], AC, 2))
    o.append(T(bx + 16, (y1 + y2) / 2 - 4, 'one class,', 13, 'start', fill=AC))
    o.append(T(bx + 16, (y1 + y2) / 2 + 14, 'test 11', 13, 'start', fill=AC))
    o.append(T(bx + 16, ty + 22 + 4 * rh + 23, 'test 01', 13, 'start', fill=MUT))
    o.append(T(bx + 16, ty + 22 + 5 * rh + 23, 'test 10', 13, 'start', fill=MUT))
    o.append(T(bx + 16, ty + 22 + 6 * rh + 23, 'dominates A/1', 13, 'start', fill=MUT))
    o.append(T(360, 340, 'Shaded cells: the faulty output differs from the good one. Tests {01, 10, 11} catch all six faults.', 14))
    return 356, ''.join(o)


# ---- 6.3 D-algorithm values on Z = A·(B + C) for A stuck-at-0 (worked example 1) ----
def f3():
    o = []
    g1, o1 = nand_gate(300, 90, 60, label='G1')
    g2, o2 = nand_gate(300, 230, 60, label='G2')
    g3, o3 = nand_gate(500, 160, 60, label='G3')
    o += [g1, g2, g3]
    # inputs
    o.append(L(40, 160, 200, 160, NX, 2.5)); o.append(L(200, 75, 200, 215, NX, 2.5))
    o.append(L(200, 75, 300, 75, NX, 2.5)); o.append(L(200, 215, 300, 215, NX, 2.5))
    o.append(C(200, 160, 5, NX))
    o.append(L(40, 105, 300, 105, INK, 2)); o.append(L(40, 245, 300, 245, INK, 2))
    o.append(T(20, 165, 'A', 15, 'start', bold=True)); o.append(T(20, 110, 'B', 15, 'start', bold=True)); o.append(T(20, 250, 'C', 15, 'start', bold=True))
    o.append(Tb(100, 150, 'A = 1 good, 0 faulty: D', 13, 'middle', fill=NX, bold=True))
    o.append(T(66, 98, '1', 14, bold=True)); o.append(T(66, 238, '0', 14, bold=True))
    o.append(R(150, 166, 40, 22, NXS, NX, 4)); o.append(T(170, 182, 'SA0', 12, fill=NX, bold=True))
    # G1, G2 outputs into G3
    o.append(L(o1, 90, 440, 90, NX, 2.5)); o.append(L(440, 90, 440, 145, NX, 2.5)); o.append(L(440, 145, 500, 145, NX, 2.5))
    o.append(L(o2, 230, 440, 230, INK, 2)); o.append(L(440, 230, 440, 175, INK, 2)); o.append(L(440, 175, 500, 175, INK, 2))
    o.append(Tb(380, 76, 'G1 = 0 / 1: D̄', 13, 'start', fill=NX, bold=True))
    o.append(Tb(380, 252, 'G2 = 1 in both', 13, 'start'))
    o.append(L(o3, 160, 690, 160, NX, 2.5))
    o.append(Tb(640, 150, 'Z = 1 / 0: D', 14, 'middle', fill=NX, bold=True))
    o.append(T(360, 300, 'Values are good / faulty. The difference (D, D̄) travels A → G1 → Z; C = 0 holds G2 at 1.', 14))
    o.append(T(360, 324, 'Test vector ABC = 110', 15, bold=True))
    return 340, ''.join(o)


# ---- 6.4 three-cell scan chain of worked example 1 ----
def f4():
    o = []
    xs = [180, 380, 580]
    y = 190
    for i, x in enumerate(xs):
        o.append(f'<path d="M{x - 70},{y - 34} L{x - 46},{y - 22} L{x - 46},{y + 22} L{x - 70},{y + 34} Z" style="fill:{PANEL};stroke:{AC};stroke-width:2"/>')
        o.append(T(x - 62, y - 10, '0', 12, fill=MUT)); o.append(T(x - 62, y + 20, '1', 12, fill=MUT))
        o.append(L(x - 46, y, x - 20, y, AC, 2, arrow='n'))
        o.append(R(x - 18, y - 30, 64, 60, ACS, AC, 6))
        o.append(T(x + 14, y + 5, f'FF{i + 1}', 14, bold=True))
        o.append(T(x + 14, y + 52, f'Q_{i + 1}', 13, fill=MUT))
    o.append(L(16, y + 18, xs[0] - 72, y + 18, LV, 2.5, arrow='l'))
    o.append(T(16, y + 44, 'SI = 1, 1, 0', 14, 'start', fill=LV, bold=True))
    for a, b in ((xs[0], xs[1]), (xs[1], xs[2])):
        o.append(P([(a + 46, y + 10), (a + 64, y + 10), (a + 64, y + 18), (b - 72, y + 18)], LV, 2.5))
    o.append(L(xs[2] + 46, y, 704, y, LV, 2.5, arrow='l'))
    o.append(T(704, y - 10, 'SO', 14, 'end', fill=LV, bold=True))
    o.append(L(60, 290, 620, 290, L2, 1.5, dash='5 4'))
    for x in xs: o.append(L(x - 58, 290, x - 58, y + 28, L2, 1.5, dash='5 4'))
    o.append(T(60, 310, 'SE: 1 = shift (SI), 0 = capture (D)', 13, 'start', fill=MUT))
    o.append(R(60, 20, 580, 70, PANEL, NX, 8, dash='6 4'))
    o.append(T(350, 46, 'combinational logic', 14, bold=True, fill=NX))
    for x, eq in zip(xs, ('D_1 = Q_2 AND Q_3', 'D_2 = Q_1 XOR Q_3', 'D_3 = NOT Q_1')):
        o.append(T(x - 40, 74, eq, 14))
    for i, x in enumerate(xs):
        o.append(L(x - 90, 90, x - 90, y - 18, NX, 2)); o.append(L(x - 90, y - 18, x - 72, y - 18, NX, 2, arrow='x'))
        o.append(T(x - 96, 128, f'D_{i + 1}', 13, 'end', fill=NX))
    o.append(T(360, 348, 'Loaded 0 1 1 → captured 1 1 1 (good) or 0 1 1 (D_1 stuck-at-0)', 14, bold=True))
    o.append(T(360, 372, 'SO shows Q_3, Q_2, Q_1: good 1, 1, 1; faulty 1, 1, 0', 14))
    return 388, ''.join(o)


# ---- 6.5 TAP controller state diagram with the path of the worked example ----
def f5():
    o = []
    W, H = 140, 34
    XL, XD, XI = 120, 345, 590
    st = {'TLR': (XL, 46, 'Test-Logic-Reset'), 'RTI': (XL, 130, 'Run-Test/Idle')}
    names = ['Select', 'Capture', 'Shift', 'Exit1', 'Pause', 'Exit2', 'Update']
    for col, x in (('DR', XD), ('IR', XI)):
        for i, n in enumerate(names):
            st[n + col] = (x, 130 + i * 72, f'{n}-{col}')
    path = {'TLR', 'RTI', 'SelectDR', 'SelectIR', 'CaptureIR', 'ShiftIR', 'Exit1IR', 'UpdateIR', 'CaptureDR', 'ShiftDR', 'Exit1DR', 'UpdateDR'}
    for k, (x, y, lab) in st.items():
        hot = k in path
        o.append(R(x - W / 2, y - H / 2, W, H, ACS if hot else PANEL, AC if hot else L2, 8))
        o.append(T(x, y + 5, lab, 13, bold=hot))

    def run(pts, lab, lx, ly, hot, anchor='middle'):
        c = AC if hot else L2
        o.append(P(pts[:-1] + [pts[-1]], c, 2.2 if hot else 1.8))
        (xa, ya), (xb, yb) = pts[-2], pts[-1]
        o.append(f'<line x1="{xa:.1f}" y1="{ya:.1f}" x2="{xb:.1f}" y2="{yb:.1f}" style="stroke:{c};stroke-width:{2.2 if hot else 1.8}" marker-end="url(#ar-UID-{'n' if hot else 'm'})"/>')
        o.append(Tb(lx, ly, lab, 13, anchor, fill=c, bold=hot))

    def down(a, b, lab, hot):
        x, y1, _ = st[a]; _, y2, _ = st[b]
        run([(x, y1 + H / 2), (x, y2 - H / 2 - 3)], lab, x + 12, (y1 + y2) / 2 + 5, hot, 'start')

    def loop(k, lab, hot):
        x, y, _ = st[k]; c = AC if hot else L2
        o.append(f'<path d="M{x - W / 2:.1f},{y - 8:.1f} C{x - W / 2 - 34:.1f},{y - 28:.1f} {x - W / 2 - 34:.1f},{y + 28:.1f} {x - W / 2 - 3:.1f},{y + 9:.1f}" '
                 f'style="fill:none;stroke:{c};stroke-width:2" marker-end="url(#ar-UID-{'n' if hot else 'm'})"/>')
        o.append(T(x - W / 2 - 30, y + 5, lab, 13, 'end', fill=c, bold=hot))

    down('TLR', 'RTI', '0', True)
    loop('TLR', '1', False); loop('RTI', '0', False)
    for col, X in (('DR', XD), ('IR', XI)):
        down('Select' + col, 'Capture' + col, '0', True)
        down('Capture' + col, 'Shift' + col, '0', True)
        down('Shift' + col, 'Exit1' + col, '1', True)
        down('Exit1' + col, 'Pause' + col, '0', False)
        down('Pause' + col, 'Exit2' + col, '1', False)
        down('Exit2' + col, 'Update' + col, '1', False)
        loop('Shift' + col, '0', True); loop('Pause' + col, '0', False)
        yc, ys, ye1, ye2, yu = (st[n + col][1] for n in ('Capture', 'Shift', 'Exit1', 'Exit2', 'Update'))
        r = X + W / 2
        run([(r, yc), (r + 12, yc), (r + 12, ye1 - 8), (r + 3, ye1 - 8)], '1', r + 16, (yc + ye1) / 2 - 20, False, 'start')
        run([(r, ye1 + 8), (r + 26, ye1 + 8), (r + 26, yu - 6), (r + 3, yu - 6)], '1', r + 30, (ye1 + yu) / 2 + 30, True, 'start')
        lft = X - W / 2
        run([(lft, ye2), (lft - 46, ye2), (lft - 46, ys + 10), (lft - 3, ys + 10)], '0', lft - 24, ye2 - 8, False)
    yu = st['UpdateDR'][1]
    # Update states with TMS = 1 go to Select-DR through the channel between the columns (the example leaves Update-IR this way)
    xc = 462
    o.append(P([(XD + W / 2, yu + 8), (xc, yu + 8)], L2, 1.8))
    o.append(Tb(XD + W / 2 + 14, yu + 26, '1', 13, 'start', fill=L2))
    run([(XI - W / 2, yu + 8), (xc, yu + 8), (xc, 130 + 26), (XD + 40, 130 + 26), (XD + 40, 130 + H / 2 + 3)], '1', XI - W / 2 - 14, yu + 26, True, 'end')
    # Update states with TMS = 0 go to Run-Test/Idle
    run([(XD - W / 2, yu), (XL, yu), (XL, 130 + H / 2 + 3)], '0', XD - W / 2 - 60, yu - 6, True)
    o.append(P([(XI, yu + H / 2), (XI, yu + 44), (XL, yu + 44), (XL, yu)], L2, 1.8))
    o.append(Tb(XI - 30, yu + 40, '0', 13, fill=L2))
    # across the top row
    run([(XL + W / 2, 130), (XD - W / 2 - 3, 130)], '1', (XL + XD) / 2 + 4, 124, True)
    run([(XD + W / 2, 130), (XI - W / 2 - 3, 130)], '1', (XD + XI) / 2 + 10, 124, True)
    run([(XI + W / 2, 130), (704, 130), (704, 18), (XL, 18), (XL, 46 - H / 2 - 3)], '1', 560, 22, False)
    o.append(T(360, yu + 82, 'Arrows carry the TMS value. Bold: load EXTEST (13 IR bits), then shift one 70-bit pattern, 94 TCK cycles.', 13))
    return yu + 98, ''.join(o)


# ---- 6.6 the 4-bit LFSR of worked example 1 and its 15-state cycle ----
def f6():
    o = []
    xs = [110, 230, 350, 470]
    y = 70
    for i, x in enumerate(xs):
        o.append(R(x - 40, y - 26, 80, 52, ACS, AC, 6))
        o.append(T(x, y - 4, f'b_{3 - i}', 15, bold=True))
        o.append(T(x, y + 16, '0001'[i], 14, fill=NX, bold=True))
    for a, b in zip(xs, xs[1:]):
        o.append(L(b - 40, y, a + 43, y, AC, 2, arrow='n'))
    # feedback: XOR of b3 and b0 into b0
    o.append(xor_gate(590, y, 16))
    o.append(L(xs[3] + 40, y, 571, y, AC, 2, arrow='n'))
    o.append(P([(xs[0], y - 26), (xs[0], y - 46), (590, y - 46), (590, y - 19)], AC, 2))
    o.append(f'<line x1="590" y1="{y - 30}" x2="590" y2="{y - 19}" style="stroke:{AC};stroke-width:2" marker-end="url(#ar-UID-n)"/>')
    o.append(P([(606, y), (650, y), (650, y + 50), (xs[3], y + 50), (xs[3], y + 29)], LV, 2.5))
    o.append(f'<line x1="{xs[3]}" y1="{y + 40}" x2="{xs[3]}" y2="{y + 29}" style="stroke:{LV};stroke-width:2.5" marker-end="url(#ar-UID-l)"/>')
    o.append(T(570, y + 72, 'feedback f = b_3 XOR b_0 enters b_0', 14, 'middle', fill=LV, bold=True))
    o.append(T(290, y - 54, 'shift left each clock; seed 0001', 13, fill=MUT))
    # the cycle of states on a ring
    seq = ['0001', '0011', '0111', '1111', '1110', '1101', '1010', '0101', '1011', '0110', '1100', '1001', '0010', '0100', '1000']
    cx, cy, r = 360, 330, 140
    for i, s in enumerate(seq):
        a = -math.pi / 2 + 2 * math.pi * i / 15
        x, yy = cx + r * math.cos(a) * 1.9, cy + r * math.sin(a)
        o.append(R(x - 28, yy - 14, 56, 26, NXS if i == 0 else PANEL, NX if i == 0 else L2, 6))
        o.append(TM(x, yy + 5, s, 13, bold=(i == 0)))
    o.append(T(cx, cy - 6, '15 states, then repeat', 15, bold=True))
    o.append(T(cx, cy + 16, 'period = 2⁴ − 1 = 15', 14))
    o.append(T(cx, cy + 36, '0000 never appears', 13, fill=MUT))
    return 500, ''.join(o)


# ---- 6.7 March C− on a 4-cell memory with the coupling fault of worked example 2 ----
def f7():
    o = []
    rows = [('⇕(w0)', ['0', '0', '0', '0'], None, ['all cells written 0']),
            ('⇑(r0, w1)', ['0', '1', '1', '1'], 0, ['cell 2 goes 0 → 1 and flips', 'cell 0 from 1 back to 0']),
            ('⇑(r1, w0)', ['fail', '', '', ''], None, ['r1 at cell 0 reads 0:', 'fault detected'])]
    x0, cw, y0, rh = 150, 72, 64, 72
    o.append(T(70, y0 - 16, 'element', 14, fill=MUT))
    for j in range(4):
        o.append(T(x0 + j * cw + cw / 2, y0 - 16, f'cell {j}', 14, bold=True, fill=NX if j in (0, 2) else INK))
    o.append(T(x0 + 0 * cw + cw / 2, y0 - 36, 'victim', 13, fill=NX))
    o.append(T(x0 + 2 * cw + cw / 2, y0 - 36, 'aggressor', 13, fill=NX))
    for i, (el, vals, flip, note) in enumerate(rows):
        y = y0 + i * rh
        o.append(T(70, y + 40, el, 15, bold=True))
        for j, v in enumerate(vals):
            hot = v == 'fail' or flip == j
            if v != '':
                o.append(R(x0 + j * cw + 5, y + 8, cw - 10, rh - 20, NXS if hot else PANEL, NX if hot else L2, 6))
                o.append(T(x0 + j * cw + cw / 2, y + 40, v, 15, bold=(v == 'fail'), fill=NX if v == 'fail' else INK))
        for n, line in enumerate(note):
            o.append(T(x0 + 4 * cw + 18, y + 34 + n * 18 - (9 if len(note) > 1 else 0), line, 13, 'start', fill=NX if i else MUT))
    y = y0 + rh
    o.append(arc(x0 + 2 * cw + cw / 2, y + 10, x0 + cw / 2 + 10, y + 10, -0.35, NX, 2, 'x'))
    o.append(T(360, 296, 'Fault: when cell 2 goes 0 → 1, cell 0 is inverted. March C− finds it at the next read of cell 0.', 14))
    o.append(T(360, 320, 'March C−: 10 operations per cell, 10n accesses in all', 14, fill=MUT))
    return 336, ''.join(o)


# ---- 6.8 two cores sharing an 8-wire TAM (worked example 2) ----
def f8():
    o = []
    o.append(R(20, 20, 680, 226, FIGBG, L2, 10, dash='6 5'))
    o.append(T(40, 44, 'SoC', 14, 'start', bold=True, fill=MUT))
    o.append(boxt(40, 80, 110, 90, ['TAM in', '8 wires'], PANEL, AC, 14, True))
    for k, (y, name, sub) in enumerate(((60, 'Core A', '4 chains × 200 cells, 500 patterns'), (140, 'Core B', '4 chains × 150 cells, 800 patterns'))):
        o.append(R(250, y, 300, 64, ACS, AC, 8))
        o.append(R(244, y - 6, 312, 76, 'none', LV, 10, dash='4 4'))
        o.append(T(400, y + 26, name, 15, bold=True))
        o.append(T(400, y + 48, sub, 13))
        for w in range(4):
            yy = y + 12 + w * 13
            o.append(L(150, 125 + (w - 1.5) * 5 + (k * 22 - 11), 244, yy, AC, 1.6))
            o.append(L(556, yy, 600, 125 + (w - 1.5) * 5 + (k * 22 - 11), AC, 1.6))
    o.append(boxt(600, 80, 90, 90, ['TAM', 'out'], PANEL, AC, 14, True))
    o.append(T(400, 236, 'dashed ring: the wrapper around each core', 13, fill=LV))
    # time bars
    x0, sc = 120, 560 / 221650
    o.append(T(20, 296, 'one after', 13, 'start', fill=MUT)); o.append(T(20, 312, 'the other', 13, 'start', fill=MUT))
    o.append(R(x0, 282, 100700 * sc, 34, ACS, AC, 4)); o.append(T(x0 + 100700 * sc / 2, 304, 'A: 100,700', 13, bold=True))
    o.append(R(x0 + 100700 * sc, 282, 120950 * sc, 34, LVS, LV, 4)); o.append(T(x0 + 100700 * sc + 120950 * sc / 2, 304, 'B: 120,950', 13, bold=True))
    o.append(T(20, 356, 'together', 13, 'start', fill=MUT)); o.append(T(20, 372, '4 + 4 wires', 13, 'start', fill=MUT))
    o.append(R(x0, 338, 100700 * sc, 18, ACS, AC, 4)); o.append(R(x0, 360, 120950 * sc, 18, LVS, LV, 4))
    o.append(T(x0 + 120950 * sc + 10, 366, '120,950 clocks', 13, 'start', bold=True))
    o.append(T(x0 + 560 - 4, 332, '221,650 clocks', 13, 'end', bold=True))
    o.append(T(360, 410, 'Sharing the TAM saves 45.4 %, because neither core can use more than 4 wires.', 14))
    return 426, ''.join(o)


# ---- 6.9 ADC transfer staircase near codes 64 and 65 (worked example) ----
def f9():
    o = []
    x0, x1, y0, y1 = 100, 640, 30, 300
    fx = lin(625, 670, x0, x1); fy = lin(62.5, 66.5, y1, y0)
    o.append(axes(x0, x1, y0, y1, [630, 640, 650, 660, 670], [63, 64, 65, 66], fx, fy, 'input voltage (mV)', 'output code'))
    # ideal edges every 10 mV: code k between (k*10 - 5) ... use edges at 635, 645, 655, 665
    ideal = [(625, 63), (635, 64), (645, 65), (655, 66), (665, 66)]
    pts = []
    for (v, c), (vn, _) in zip(ideal, ideal[1:]):
        pts += [(fx(v), fy(c)), (fx(vn), fy(c))]
    o.append(P(pts, L2, 2, dash='6 5'))
    meas = [(625, 63), (635, 64), (649, 65), (655, 66), (670, 66)]
    pts = []
    for (v, c), (vn, _) in zip(meas, meas[1:]):
        pts += [(fx(v), fy(c)), (fx(vn), fy(c))]
    o.append(P(pts, AC, 3))
    # widths
    for a, b, c, lab, col in ((635, 649, 64, 'W_64 = 14 mV', NX), (649, 655, 65, 'W_65 = 6 mV', NX)):
        yb = fy(c) + 22
        o.append(L(fx(a), yb, fx(b), yb, col, 1.6, arrow='x')); o.append(L(fx(b), yb, fx(a), yb, col, 1.6, arrow='x'))
        o.append(Tb((fx(a) + fx(b)) / 2, yb + 22, lab, 13, fill=col, bold=True))
    o.append(T(fx(642), fy(64) - 12, 'DNL +0.4', 14, fill=NX, bold=True))
    o.append(T(fx(652), fy(65) - 12, 'DNL −0.4', 14, fill=NX, bold=True))
    o.append(T(fx(644), fy(65.2), 'INL_64 = +0.4 LSB', 13, 'end', bold=True)); o.append(T(fx(644), fy(65.2) + 17, '(edge 4 mV late)', 13, 'end', fill=MUT))
    o.append(T(fx(662), fy(66) + 44, 'INL_65 = 0.4 − 0.4 = 0', 13, fill=MUT))
    o.append(T(370, 372, 'Solid: measured codes. Dashed: ideal codes, 1 LSB = 10 mV wide.', 14))
    return 388, ''.join(o)


FIG = {
    1: (f1, 'Defect level against fault coverage for the yields of the worked example and the quiz. At Y = 0.90, raising coverage from 0.95 to 0.99 cuts the escapes from 5254 to 1053 parts per million.',
        'Two falling curves of defective parts per million against fault coverage from 0.90 to 1.00, for yields 0.90 and 0.95, with points at 5254 and 1053 DPM.'),
    2: (f2, 'The two-input NAND gate and the output of each faulty version for every input. A/0, B/0 and Z/1 give the same faulty table, so they are one class; three vectors catch all six faults.',
        'NAND gate with inputs A and B and output Z, beside a table of the good output and the six stuck-at faults for inputs 00, 01, 10 and 11, with differing cells shaded.'),
    3: (f3, 'The D-algorithm test for A stuck-at-0. Each line shows its good and faulty value; the difference passes through G1 and reaches Z while C = 0 keeps G2 steady.',
        'Three NAND gates computing Z equals A times B plus C, with A marked stuck at 0, B equal 1, C equal 0, G1 carrying D bar, G2 equal 1 and Z carrying D.'),
    4: (f4, 'The three-cell scan chain of the worked example. SE = 1 links the cells from SI to SO; SE = 0 lets each cell capture its output of the logic block.',
        'Three multiplexer and flip-flop scan cells in a chain from SI to SO, below a logic block that computes D1, D2 and D3 from Q1, Q2 and Q3, with the pattern and the captured values.'),
    5: (f5, 'The 16 states of the TAP controller. Arrows carry the value of TMS; the bold boxes are the path the worked example takes to load EXTEST and shift one pattern.',
        'State diagram of the JTAG TAP controller with Test-Logic-Reset, Run-Test/Idle, and the seven DR and seven IR states, with TMS values on each arrow and the worked-example path highlighted.'),
    6: (f6, 'The 4-bit LFSR of the worked example and the order of its states. The feedback b3 XOR b0 enters b0 on the right, and from seed 0001 the register visits all 15 non-zero words.',
        'Four flip-flops b3 to b0 holding 0001 with an XOR of b3 and b0 feeding b0, above a ring of the 15 states from 0001 to 1000.'),
    7: (f7, 'March C− on the 4-cell memory of worked example 2. The write that raises cell 2 also flips cell 0, and the next element finds cell 0 holding the wrong value.',
        'Grid of four memory cells after each March C minus element: all zeros, then 0 1 1 1 after the coupling fault flips cell 0, then a fail at the read of cell 0.'),
    8: (f8, 'The two cores of worked example 2 on an 8-wire TAM, and their test times. Each core has only 4 scan chains, so testing them side by side on 4 wires each nearly halves the time.',
        'An SoC with an 8-wire test access mechanism feeding core A and core B through wrappers, and two time bars: 221,650 clocks one after the other and 120,950 clocks together.'),
    9: (f9, 'Part of the ADC transfer curve of the worked example. Code 64 is 14 mV wide and code 65 only 6 mV, so their DNLs are +0.4 and −0.4 LSB and the INL returns to zero.',
        'Staircase plot of output code against input voltage from 625 to 670 millivolts, with the measured steps for codes 64 and 65 at 14 and 6 millivolts wide against dashed ideal 10 millivolt steps.'),
}
AFTER = {1: 3, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'caption': cap, 'after_section': AFTER[k], 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
