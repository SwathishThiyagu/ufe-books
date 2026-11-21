"""Claude's hand-drawn figures for ec-vlsi-u5 (VLSI Design: design flow, ASIC styles, Verilog, test benches, FPGAs, physical design,
IP cores), one per chapter, each drawn from that chapter's own worked example and numbers. Colours are the shell's CSS variables."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
MONO = 'font-family:var(--mono)'


def lbox(x, y, w, h, title, sub=None, fill=PANEL, stroke=AC, sub_fill=MUT, size=14):
    o = [R(x, y, w, h, fill, stroke, 8)]
    if sub:
        o.append(T(x + w / 2, y + h / 2 - 4, title, size, bold=True))
        o.append(T(x + w / 2, y + h / 2 + 15, sub, 13, fill=sub_fill))
    else:
        o.append(T(x + w / 2, y + h / 2 + 5, title, size, bold=True))
    return ''.join(o)


# ---- 5.1 the flow, snake-wise, with the worked example's hours ----
def f1():
    o = []
    W, xs = 150, [20, 196.7, 373.3, 550]
    rows = [(32, [('Specification', 'function, MHz, mW'), ('Architecture', 'blocks, clocks'), ('RTL', 'Verilog modules'), ('Synthesis', 'gate netlist · 20 h')]),
            (170, [('DFT insertion', 'scan, BIST'), ('Physical design', 'layout · 40 h'), ('Signoff', 'DRC, LVS, timing'), ('Tapeout', 'GDSII to foundry')]),
            (260, [('Fabrication', 'masks, wafers'), ('Wafer probe', 'bad dies marked'), ('Dice, package', 'bond and seal'), ('Final test', 'ATE, then ship')])]
    o.append(T(20, 22, 'Front end: ends at the gate netlist', 13, 'start', MUT, bold=True))
    o.append(T(20, 160, 'Back end: ends at tapeout', 13, 'start', MUT, bold=True))
    o.append(T(130, 250, 'After tapeout: foundry and test house', 13, 'start', MUT, bold=True))
    H = 52
    for r, (y, items) in enumerate(rows):
        order = xs if r != 1 else xs[::-1]   # the middle row runs right to left
        for i, (name, sub) in enumerate(items):
            x = order[i]
            st = NX if r == 1 and i == 0 else (LV if r == 2 else AC)
            o.append(lbox(x, y, W, H, name, sub, PANEL, st))
            if i < 3:
                xn = order[i + 1]
                if r != 1: o.append(L(x + W + 2, y + H / 2, xn - 4, y + H / 2, AC, 2, arrow='n'))
                else: o.append(L(x - 2, y + H / 2, xn + W + 4, y + H / 2, AC, 2, arrow='n'))
    o.append(L(625, 32 + H + 2, 625, 170 - 4, AC, 2, arrow='n'))
    o.append(L(95, 170 + H + 2, 95, 260 - 4, AC, 2, arrow='n'))
    # verification runs beside the flow
    o.append(R(20, 98, 570, 46, ACS, AC, 8, dash='6 4'))
    o.append(T(305, 117, 'Verification runs beside the flow, from RTL to signoff:', 13, bold=True))
    o.append(T(305, 136, 'simulation, equivalence check, static timing · 720 h of 780 h (92 %)', 13))
    return 330, ''.join(o)


FIG[1] = (f1, 'The worked example’s SoC on the flow: synthesis takes 20 h and physical design 40 h, while verification, which runs beside the flow '
              'from RTL to signoff, takes 720 of the 780 hours. Tapeout only hands the layout to the foundry; fabrication, wafer probe, packaging '
              'and final test follow it.',
          'The ASIC design flow in three rows: front end from specification to synthesis, back end from DFT insertion to tapeout, and the '
          'foundry steps after tapeout, with a verification band beside the flow.')


# ---- 5.2 three ASIC styles with the worked example's costs ----
def f2():
    o = []
    px, pw, py, ph = [20, 255, 490], 210, 40, 170
    titles = ['Full-custom', 'Standard-cell', 'Gate array']
    for x, t in zip(px, titles):
        o.append(R(x, py, pw, ph, FIGBG, L2, 6))
        o.append(T(x + pw / 2, py - 12, t, 15, bold=True))
    # full custom: shapes of every size, drawn by hand
    x0 = px[0]
    for (dx, dy, w, h, f) in [(12, 12, 90, 64, ACS), (110, 12, 88, 34, LVS), (110, 52, 40, 52, NXS), (156, 52, 42, 24, ACS),
                              (12, 84, 54, 72, LVS), (72, 84, 32, 72, NXS), (110, 112, 88, 44, ACS)]:
        o.append(R(x0 + dx, py + dy, w, h, f, AC, 3, sw=1.5))
    # standard cell: rows of equal-height cells between VDD and VSS rails
    x0 = px[1]
    for r in range(3):
        yt = py + 14 + r * 52
        widths = [[26, 16, 38, 22, 34], [20, 40, 18, 30, 28], [34, 22, 26, 20, 34]][r]
        x = x0 + 12
        for w in widths:
            o.append(R(x, yt + 4, w, 30, ACS, AC, 2, sw=1.5)); x += w + 2
        o.append(P([(x0 + 10, yt + 2), (x0 + 160, yt + 2)], LV, 3))
        o.append(P([(x0 + 10, yt + 36), (x0 + 160, yt + 36)], NX, 3))
        if r == 0:
            o.append(T(x0 + 166, yt + 7, 'VDD', 13, 'start', LV, bold=True))
            o.append(T(x0 + 166, yt + 41, 'VSS', 13, 'start', NX, bold=True))
    # gate array: identical base cells, wired by metal
    x0 = px[2]
    for r in range(4):
        for cc in range(5):
            o.append(R(x0 + 14 + cc * 38, py + 14 + r * 38, 30, 30, PANEL, L2, 3, sw=1.5))
    o.append(P([(x0 + 29, py + 44), (x0 + 29, py + 58), (x0 + 105, py + 58), (x0 + 105, py + 82)], LV, 3))
    o.append(P([(x0 + 67, py + 120), (x0 + 67, py + 134), (x0 + 181, py + 134), (x0 + 181, py + 96)], LV, 3))
    o.append(P([(x0 + 143, py + 44), (x0 + 143, py + 58), (x0 + 181, py + 58)], LV, 3))
    # what is custom and what it cost in the worked example
    notes = [('every transistor drawn', 'all masks made for it', 'NRE ₹8 crore · ₹200 a chip'),
             ('library cells in rows', 'all masks made for it', 'NRE ₹2 crore · ₹250 a chip'),
             ('base transistors pre-made', 'only metal masks made', 'NRE ₹40 lakh · ₹500 a chip')]
    for x, (a, b, cst) in zip(px, notes):
        o.append(T(x + pw / 2, py + ph + 22, a, 13))
        o.append(T(x + pw / 2, py + ph + 40, b, 13, fill=MUT))
        o.append(T(x + pw / 2, py + ph + 62, cst, 14, fill=AC, bold=True))
    o.append(T(360, py + ph + 96, 'FPGA (programmable): no masks made for the design · NRE ₹0 · ₹1,800 a chip', 13, fill=MUT))
    return 318, ''.join(o)


FIG[2] = (f2, 'Three ASIC styles with the worked example’s costs. Full-custom draws every shape; a standard-cell chip places library cells of one '
              'height in rows between VDD and VSS rails; a gate array starts from a stocked base of identical cells and adds only the metal '
              'wiring, so its NRE is lowest of the three and its cost per chip highest.',
          'Three panels: hand-drawn full-custom shapes, rows of equal-height standard cells between supply rails, and a grid of identical '
          'gate-array base cells joined by metal wires, each with its NRE and cost per chip.')


# ---- 5.3 parse tree of the worked expression ----
def node(x, y, op, val, on=True, r=21):
    st = AC if on else L2
    o = [f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{ACS if on else PANEL};stroke:{st};stroke-width:2{"" if on else ";stroke-dasharray:5 4"}"/>',
         TM(x, y + 5, op, 15, bold=True)]
    if val is not None: o.append(T(x + r + 6, y + 5, val, 14, 'start', AC if on else MUT, bold=on))
    return ''.join(o)


def leaf(x, y, s, on=True):
    return R(x - 30, y - 15, 60, 30, PANEL, AC if on else L2, 6, dash=None if on else '5 4') + TM(x, y + 5, s, 14)


def f3():
    o = []
    E = lambda a, b, on=True: L(a[0], a[1], b[0], b[1], AC if on else L2, 2, dash=None if on else '5 4')
    root, gt, sh, nt = (360, 44), (200, 126), (440, 126), (610, 126)
    pl, dd, a2, one, bb = (130, 208), (270, 208), (400, 208), (480, 208), (610, 208)
    a1, mul, b1, c1 = (80, 290), (190, 290), (150, 370), (230, 370)
    for p_, q_, on in [(root, gt, True), (root, sh, True), (root, nt, False), (gt, pl, True), (gt, dd, True), (sh, a2, True), (sh, one, True),
                       (nt, bb, False), (pl, a1, True), (pl, mul, True), (mul, b1, True), (mul, c1, True)]:
        o.append(E(p_, q_, on))
    o.append(Tb(255, 80, 'condition', 13, fill=MUT))
    o.append(Tb(412, 80, 'true: chosen', 13, fill=AC, bold=True))
    o.append(Tb(560, 72, 'false: not used', 13, fill=MUT))
    o.append(node(*root, '?:', '= 8'))
    o.append(node(*gt, '&gt;', '= 1 (10 &gt; 1)'))
    o.append(node(*sh, '&lt;&lt;', '= 8'))
    o.append(node(*nt, '~', '= 12', on=False))
    o.append(node(*pl, '+', '= 10'))
    o.append(node(*mul, '*', '= 6'))
    for pt, s, on in [(dd, 'd = 1', True), (a2, 'a = 4', True), (one, '1', True), (bb, 'b = 3', False), (a1, 'a = 4', True), (b1, 'b = 3', True), (c1, 'c = 2', True)]:
        o.append(leaf(*pt, s, on))
    o.append(T(360, 418, 'Evaluation order: * first (6), then + (10), then &gt; (1, true), then ?: picks a &lt;&lt; 1 = 8 = 4\'b1000', 13, fill=MUT))
    return 432, ''.join(o)


FIG[3] = (f3, 'The worked example’s expression y = a + b * c &gt; d ? (a &lt;&lt; 1) : ~b as a tree, with a = 4, b = 3, c = 2, d = 1. Higher '
              'precedence sits lower in the tree and is worked out first; the condition is true, so ?: takes a &lt;&lt; 1 = 8, and ~b = 12 is never used.',
          'Parse tree of the conditional expression with the value of every node: multiplication 6, addition 10, comparison true, shift 8, '
          'result 8; the unused false branch ~b = 12 is dashed.')


# ---- 5.4 one mux at three levels ----
def g_and(x, y):
    return f'<path d="M{x},{y} h20 a20,20 0 0 1 0,40 h-20 z" style="fill:var(--panel);stroke:var(--accent);stroke-width:2"/>'


def g_or(x, y):
    return (f'<path d="M{x},{y} q14,20 0,40 q34,0 50,-20 q-16,-20 -50,-20 z" style="fill:var(--panel);stroke:var(--accent);stroke-width:2"/>')


def g_not(x, y):
    return (f'<path d="M{x},{y - 12} l26,12 l-26,12 z" style="fill:var(--panel);stroke:var(--accent);stroke-width:2"/>'
            f'<circle cx="{x + 30}" cy="{y}" r="4" style="fill:var(--panel);stroke:var(--accent);stroke-width:2"/>')


def f4():
    o = []
    for x, w, t in [(20, 300, 'Gate level (one bit; four copies)'), (340, 160, 'Dataflow'), (520, 180, 'Behavioural')]:
        o.append(R(x, 34, w, 200, FIGBG, L2, 6)); o.append(T(x + w / 2, 24, t, 14, bold=True))
    W = lambda pts: P(pts, INK, 1.8)
    # gates
    o += [g_not(80, 92), g_and(150, 50), g_and(150, 130), g_or(222, 92)]
    o.append(W([(46, 60), (150, 60)]))                     # a
    o.append(W([(46, 140), (150, 140)]))                   # b
    o.append(W([(46, 196), (66, 196), (66, 92), (80, 92)]))  # sel to NOT
    o.append(W([(66, 160), (150, 160)]))                   # sel to AND2
    o.append(C(66, 160, 3.5, INK))
    o.append(W([(114, 92), (130, 92), (130, 80), (150, 80)]))  # nsel
    o.append(W([(190, 70), (206, 70), (206, 102), (226, 102)]))  # t0
    o.append(W([(190, 150), (206, 150), (206, 122), (226, 122)]))  # t1
    o.append(W([(272, 112), (300, 112)]))                  # y
    for x, y, s, a in [(40, 65, 'a', 'end'), (40, 145, 'b', 'end'), (40, 201, 'sel', 'end'), (116, 112, 'nsel', 'start'),
                       (196, 62, 't0', 'start'), (196, 170, 't1', 'start'), (304, 117, 'y', 'start')]:
        o.append(T(x, y, s, 13, a, MUT if s not in ('a', 'b', 'sel', 'y') else INK, bold=s in ('y',)))
    # dataflow: a mux symbol
    o.append(TM(420, 58, 'assign Y =', 13)); o.append(TM(420, 76, 'sel ? B : A;', 13))
    o.append(P([(390, 92), (440, 112), (440, 180), (390, 200), (390, 92)], AC, 2, fill=PANEL))
    o.append(T(400, 133, '0', 13, 'start', MUT)); o.append(T(400, 173, '1', 13, 'start', MUT))
    o.append(W([(356, 128), (390, 128)])); o.append(W([(356, 168), (390, 168)])); o.append(W([(440, 146), (470, 146)]))
    o.append(W([(415, 190), (415, 212)]))
    o.append(T(352, 123, 'A', 13, 'start', bold=True)); o.append(T(352, 163, 'B', 13, 'start', bold=True))
    o.append(T(474, 151, 'Y', 13, 'start', bold=True)); o.append(T(422, 224, 'sel', 13, 'start'))
    # behavioural: the always block
    for i, s in enumerate(['always @(*)', '  if (sel)', '    Y = B;', '  else', '    Y = A;']):
        o.append(f'<text x="534" y="{84 + i * 26}" font-size="14" style="fill:var(--ink);{MONO};white-space:pre" xml:space="preserve">{s}</text>')
    # the worked example's result
    o.append(R(20, 250, 680, 62, ACS, AC, 8))
    o.append(T(360, 275, 'A = 1010, B = 0110, sel = 1:  Y = 0110 at all three levels', 14, bold=True))
    o.append(T(360, 298, 'sel = 0:  Y = 1010 (simulated, the three models agree)', 13))
    return 326, ''.join(o)


FIG[4] = (f4, 'The worked example’s 4-bit multiplexer at three levels: gate primitives for one bit (used four times), one continuous assign, and '
              'an always block with if and else. With A = 1010 and B = 0110 all three give Y = 0110 for sel = 1 and Y = 1010 for sel = 0.',
          'A 2-to-1 multiplexer drawn as NOT, AND and OR gates, as a multiplexer symbol for the assign statement, and as an always block, with '
          'the simulated result for both values of sel.')


# ---- 5.5 the test bench's vectors and compare instants ----
def f5():
    o = []
    X = lambda t: 110 + t * 13.5
    rows = [('a', [1, 1, 0, 0]), ('b', [0, 0, 1, 1]), ('s', [0, 1, 0, 1]), ('y', [1, 0, 0, 1])]
    for i, (name, vals) in enumerate(rows):
        lo = 82 + i * 50; hi = lo - 28
        pts = []
        for k, v in enumerate(vals):
            yv = hi if v else lo
            pts += [(X(10 * k), yv), (X(10 * k + 10), yv)]
        o.append(P(pts, LV if name == 'y' else AC, 2.5))
        o.append(T(96, lo - 9, name, 15, 'end', bold=True))
    for k, v in enumerate(['1 0 0', '1 0 1', '0 1 0', '0 1 1']):
        o.append(T(X(10 * k + 5), 30, v, 13, fill=MUT))
    o.append(T(96, 30, 'a b s', 13, 'end', MUT))
    exp = ['1', '0', '0', '1']
    for k in range(4):
        x = X(10 * k + 10)
        o.append(L(x, 40, x, 240, NX, 1.6, dash='5 4'))
        o.append(T(x, 260, f'y = {exp[k]} ok', 13, fill=NX, bold=True))
    o.append(xaxis(X(0), X(40), 276, [0, 10, 20, 30, 40], X, None, lambda v: f'{v} ns'))
    o.append(T(X(0), 260, 'compare:', 13, 'end', NX))
    return 318, ''.join(o)


FIG[5] = (f5, 'The worked example’s four vectors as waveforms. Each vector is applied at 0, 10, 20 and 30 ns, and the checker compares y with '
              'the expected 1, 0, 0, 1 at the dashed lines, 10 ns later, never at the instant the inputs change.',
          'Timing diagram of a, b, s and y over 40 ns, with the input vector written above each 10 ns slot and dashed compare lines at 10, 20, '
          '30 and 40 ns showing the expected y.')


# ---- 5.6 a 4-input LUT storing f = A·B + C·D ----
def f6():
    o = []
    f = lambda i: int(((i >> 3) & 1 and (i >> 2) & 1) or ((i >> 1) & 1 and i & 1))
    y0, hh, cx = 44, 20, 150
    o.append(T(cx + 20, 30, 'bit', 13, fill=MUT, bold=True))
    o.append(T(cx - 14, 30, 'ABCD', 13, 'end', MUT, bold=True))
    stubs = []
    for i in range(16):
        y = y0 + i * hh
        on = i == 13
        o.append(R(cx, y, 40, hh - 2, ACS if on else PANEL, AC if on else L2, 3, sw=2 if on else 1.5))
        o.append(T(cx + 20, y + 14, str(f(i)), 13, bold=on, fill=AC if on else INK))
        o.append(TM(cx - 14, y + 14, format(i, '04b'), 13, 'end', AC if on else MUT, bold=on))
        if not on: stubs.append(f'M{cx + 40},{y + 9} H260')
    o.append(f'<path d="{" ".join(stubs)}" style="fill:none;stroke:var(--line2);stroke-width:1.2"/>')
    o.append(L(cx + 40, y0 + 13 * hh + 9, 260, y0 + 13 * hh + 9, AC, 2.5))
    o.append(P([(260, 44), (320, 120), (320, 284), (260, 360), (260, 44)], AC, 2, fill=PANEL))
    o.append(T(290, 206, '16:1', 13, bold=True)); o.append(T(290, 224, 'mux', 13))
    o.append(L(290, 396, 290, 328, AC, 2, arrow='n'))
    o.append(T(290, 414, 'select A B C D = 1 1 0 1', 13, bold=True))
    o.append(L(320, 202, 380, 202, AC, 2.5, arrow='n'))
    o.append(T(388, 207, 'f = 1', 15, 'start', AC, bold=True))
    for i, s in enumerate(['f = A·B + C·D', '2⁴ = 16 configuration bits', 'address 1101 = 13', 'A·B = 1, C·D = 0, so f = 1',
                           '1s stored at 3, 7, 11 (C·D = 1)', 'and at 12 to 15 (A·B = 1)']):
        o.append(T(450, 110 + i * 26, s, 14 if i == 0 else 13, 'start', INK if i < 4 else MUT, bold=i == 0))
    return 428, ''.join(o)


FIG[6] = (f6, 'The worked example’s LUT. Its 16 configuration bits hold the truth table of f = A·B + C·D, one bit per input address, and the '
              'inputs drive a 16:1 multiplexer that reads one bit out. For A = 1, B = 1, C = 0, D = 1 it reads address 1101 = 13, which holds 1.',
          'A column of 16 stored bits addressed 0000 to 1111 feeding a 16 to 1 multiplexer; address 1101 is highlighted and the output f = 1.')


# ---- 5.7 the worked example's floorplan, to scale ----
def f7():
    o = []
    s, X0, Y0 = 100, 50, 46   # 100 px per mm; core corner
    mm = lambda x, y, w, h: (X0 + x * s, Y0 + y * s, w * s, h * s)
    o.append(R(X0 - 22, Y0 - 22, 344, 344, FIGBG, L2, 4, dash='6 4'))
    o.append(T(X0 + 150, Y0 - 28, 'die with I/O ring; core 3.0 mm × 3.0 mm', 13, fill=MUT))
    o.append(R(*mm(0, 0, 3, 3), PANEL, AC, 2))
    # standard-cell rows in the middle column
    rows = ' '.join(f'M{X0 + 104},{Y0 + 8 + k * 14} H{X0 + 196}' for k in range(21))
    o.append(f'<path d="{rows}" style="fill:none;stroke:var(--live);stroke-width:5;stroke-opacity:0.55;stroke-dasharray:12 8"/>')
    for (x, y, w, h, a) in [(0, 0, 1.0, 2.0, '2.0'), (2.0, 0, 1.0, 1.5, '1.5'), (2.0, 2.0, 1.0, 1.0, '1.0'), (0, 2.5, 1.0, 0.5, '0.5')]:
        bx, by, bw, bh = mm(x, y, w, h)
        o.append(R(bx + 2, by + 2, bw - 4, bh - 4, ACS, AC, 4))
        o.append(T(bx + bw / 2, by + bh / 2 - 2 if bh > 60 else by + bh / 2 + 5, 'macro', 13, bold=True) if bh > 60 else T(bx + bw / 2, by + bh / 2 + 5, f'{a} mm²', 13, bold=True))
        if bh > 60: o.append(T(bx + bw / 2, by + bh / 2 + 16, f'{a} mm²', 13))
    o.append(Tb(X0 + 150, Y0 + 150, 'cell rows', 13, fill=LV, bold=True))
    o.append(Tb(X0 + 150, Y0 + 168, '1.8 mm²', 13, fill=LV, bold=True))
    o.append(T(X0 + 50, Y0 + 230, 'spare', 13, fill=MUT)); o.append(T(X0 + 250, Y0 + 180, 'spare', 13, fill=MUT))
    o.append(L(X0, Y0 + 336, X0 + 100, Y0 + 336, INK, 2)); o.append(T(X0 + 50, Y0 + 354, '1 mm', 13))
    lines = [('core area = 3.0 × 3.0 = 9.0 mm²', INK, False), ('macros 2.0 + 1.5 + 1.0 + 0.5 = 5.0 mm²', INK, False),
             ('standard cells 1.8 mm²', LV, False), ('used = 6.8 mm²', INK, True), ('U = 6.8 ÷ 9.0 = 75.6 %', AC, True),
             ('whitespace = 2.2 mm²', MUT, False), ('with 20 % for routing:', INK, False), ('6.8 × 1.2 = 8.16 mm² ≤ 9.0 mm²', INK, False),
             ('fits, 0.84 mm² spare', AC, True)]
    for i, (t, c, b) in enumerate(lines):
        o.append(T(418, 70 + i * 30, t, 14 if b else 13, 'start', c, bold=b))
    return 420, ''.join(o)


FIG[7] = (f7, 'The worked example’s floorplan drawn to scale: four macros of 2.0, 1.5, 1.0 and 0.5 mm² and 1.8 mm² of standard cells in rows '
              'fill 6.8 mm² of the 9.0 mm² core (75.6 %). The 2.2 mm² left over is whitespace for routing, buffers and decoupling cells.',
          'A 3 mm square core drawn to scale with four macro blocks, standard-cell rows in the middle column, spare areas, a 1 mm scale bar and '
          'the utilization worked out beside it.')


# ---- 5.8 the SoC of the worked examples: IP forms and the memory map ----
def f8():
    o = []
    by = 168
    o.append(R(20, by - 7, 680, 14, ACS, AC, 7))
    o.append(T(360, by + 32, 'on-chip bus (AXI or AHB) with its address decoder', 13, fill=MUT, bold=True))
    top = [(20, 'CPU', 'soft core (RTL)', 'bus master', None, AC),
           (195, 'Boot ROM 16 KB', 'hard macro', '0x0000_0000', 'to 0x0000_3FFF', AC),
           (370, 'SRAM 64 KB', 'hard macro', '0x2000_0000', 'to 0x2000_FFFF', AC),
           (545, 'DSP 32 KB', 'firm IP', '0x5000_0000', 'to 0x5000_7FFF', NX)]
    bot = [(20, 'UART 4 KB', 'soft IP', '0x4000_0000', 'to 0x4000_0FFF', LV),
           (195, 'Timer 4 KB', 'soft IP', '0x4000_1000', 'to 0x4000_1FFF', LV),
           (370, 'GPIO 4 KB', 'soft IP', '0x4000_2000', 'to 0x4000_2FFF', LV)]
    w, h = 155, 96
    for (x, name, kind, a1, a2, st) in top:
        y = 20
        o.append(R(x, y, w, h, PANEL, st, 8))
        o.append(T(x + w / 2, y + 22, name, 14, bold=True)); o.append(T(x + w / 2, y + 41, kind, 13, fill=MUT))
        o.append(TM(x + w / 2, y + 64, a1, 13, fill=AC if a2 else INK));
        if a2: o.append(TM(x + w / 2, y + 83, a2, 13, fill=AC))
        o.append(L(x + w / 2, y + h, x + w / 2, by - 8, st, 2))
    for (x, name, kind, a1, a2, st) in bot:
        y = 224
        o.append(R(x, y, w, h, PANEL, st, 8))
        o.append(T(x + w / 2, y + 22, name, 14, bold=True)); o.append(T(x + w / 2, y + 41, kind, 13, fill=MUT))
        o.append(TM(x + w / 2, y + 64, a1, 13, fill=AC)); o.append(TM(x + w / 2, y + 83, a2, 13, fill=AC))
        o.append(L(x + w / 2, by + 8, x + w / 2, by + 16, st, 2)); o.append(L(x + w / 2, by + 40, x + w / 2, y, st, 2))
    # a PLL: hard IP with no address, it only feeds clocks
    o.append(R(545, 224, w, h, FIGBG, L2, 8, dash='6 4'))
    o.append(T(622, 246, 'PLL', 14, bold=True)); o.append(T(622, 265, 'hard IP', 13, fill=MUT))
    o.append(T(622, 288, 'no address:', 13)); o.append(T(622, 307, 'clocks only', 13))
    return 336, ''.join(o)


FIG[8] = (f8, 'The SoC of the worked examples. A soft CPU core masters the bus; each slave answers to its own aligned address range, and the '
              'DSP block sits at 0x5000_0000 because 0x2000_8000 would overlap the top half of the SRAM. The PLL is IP too, but it has no '
              'registers and so no address.',
          'An SoC block diagram: a soft CPU, a boot ROM and SRAM as hard macros and a firm DSP block above the bus, three soft-IP peripherals '
          'and a PLL below it, each slave labelled with its address range.')


spec = make_spec(FIG)
