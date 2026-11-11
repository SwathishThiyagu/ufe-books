"""Claude's hand-drawn figures for c-se-u4 (Software Engineering, unit 4: testing strategies and techniques), one per
chapter, from each chapter's worked example, plus the sentences in the chapter text that describe a figure (text_fixes)."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {}


def row3(x, y, ws, cells, fills=None, bold=False, h=34):
    o = []
    cx = x
    for i, (w, c) in enumerate(zip(ws, cells)):
        f, st = (fills[i] if fills else (PANEL, L2))
        o.append(R(cx, y, w, h, f, st, 3, 1.4))
        o.append(T(cx + 10, y + h / 2 + 5, c, 13, 'start', bold=bold))
        cx += w
    return ''.join(o)


# ---- 4.1 one test case: expected vs actual ----
def f1():
    o = [T(20, 24, 'TC1: withdraw ₹2,000 from a balance of ₹5,000', 15, 'start', bold=True)]
    o.append(T(20, 48, 'rule check: 2,000 ≤ 5,000 and the ATM has cash, so the withdrawal is allowed', 13, 'start', MUT))
    ws = [170, 170, 170, 170]
    y = 64
    o.append(row3(20, y, ws, ['', 'expected', 'actual', 'verdict'], [(ACS, AC)] * 4, True))
    o.append(row3(20, y + 34, ws, ['cash out', '₹2,000', '₹2,000', 'match'], [(PANEL, L2)] * 3 + [(NXS, NX)]))
    o.append(row3(20, y + 68, ws, ['new balance', '5,000 − 2,000 = ₹3,000', '₹3,500', '₹500 too high'], [(PANEL, L2), (PANEL, L2), (LVS, LV), (LVS, LV)]))
    o.append(row3(20, y + 102, ws, ['receipt', 'printed', 'printed', 'match'], [(PANEL, L2)] * 3 + [(NXS, NX)]))
    yv = y + 156
    o.append(R(20, yv, 680, 56, LVS, LV, 8, 2.5))
    o.append(T(36, yv + 24, 'TC1 FAILS: one expected value differs', 15, 'start', LV, True))
    o.append(T(36, yv + 44, 'the dispenser is fine; look at the balance update or its display', 13, 'start'))
    o.append(R(20, yv + 74, 680, 56, FIGBG, L2, 8, 1.5, '6 4'))
    o.append(T(36, yv + 98, 'TC2: withdraw ₹6,000 from ₹5,000 → expect "Insufficient balance", cash ₹0, balance ₹5,000', 13, 'start'))
    o.append(T(36, yv + 118, 'not run yet: TC1\'s failure says nothing about TC2', 13, 'start', MUT, True))
    return yv + 144, ''.join(o)
FIG[1] = (f1, 'TC1 compares each expected value with what the ATM did: cash and receipt match, but the balance shows ₹3,500 instead of ₹3,000, ₹500 too high, so TC1 fails. TC2 keeps its own status until it is run.',
          'A table for TC1 with rows cash out, new balance and receipt, and columns expected, actual and verdict. The new balance row is highlighted: expected 3,000, actual 3,500, 500 too high. Below, a fail banner for TC1 and a dashed box for TC2, not yet run.')


# ---- 4.2 verification, validation, QA, QC ----
def f2():
    o = []
    W, H = 336, 178
    boxes = [(20, 16, 'Verification: nothing runs', AC, ACS), (364, 16, 'Validation: real users, real need', LV, LVS),
             (20, 206, 'QA: the process rule', NX, NXS), (364, 206, 'QC: the built release', AC, PANEL)]
    for x, y, h, st, f in boxes:
        o.append(R(x, y, W, H, FIGBG, st, 8, 2))
        o.append(R(x, y, W, 34, f, st, 8, 2))
        o.append(T(x + 14, y + 23, h, 14, 'start', st, True))
    x, y = 20, 16
    for i, (a, n) in enumerate([('(i) SRS review, 60 requirements', 9), ('(ii) design review', 6), ('(iii) code review, 2400 lines', 15)]):
        o.append(T(x + 14, y + 62 + i * 24, a, 13, 'start')); o.append(T(x + W - 14, y + 62 + i * 24, str(n), 14, 'end', bold=True))
    o.append(L(x + 14, y + 128, x + W - 14, y + 128, L2, 1.4))
    o.append(T(x + 14, y + 150, 'defects found before any test', 13, 'start', bold=True)); o.append(T(x + W - 14, y + 150, '30', 15, 'end', AC, True))
    # validation dot strip
    x, y = 364, 16
    s0, s1, v0, v1 = x + 24, x + W - 24, 20, 46
    fx = lambda t: s0 + (t - v0) / (v1 - v0) * (s1 - s0)
    yl = y + 92
    o.append(L(s0, yl, s1, yl, L2, 1.4))
    for t in (20, 30, 40):
        o.append(L(fx(t), yl, fx(t), yl + 5, L2, 1.4)); o.append(T(fx(t), yl + 20, f'{t} s', 13, fill=MUT))
    o.append(L(fx(30), y + 46, fx(30), yl + 4, LV, 2, '5 4'))
    times = [21, 23, 25, 27, 22, 24, 26, 24]
    seen = {}
    for t in times:
        k = seen.get(t, 0); seen[t] = k + 1
        o.append(C(fx(t), yl - 9 - k * 13, 5.5, NX))
    for t in (38, 45):
        o.append(C(fx(t), yl - 9, 5.5, LV))
    o.append(T(fx(30) + 6, y + 56, 'target', 13, 'start', LV))
    o.append(T(x + 14, y + 138, '8 of 10 under 30 s = 80.0%, mean 192 ÷ 8 = 24.0 s', 13, 'start'))
    o.append(T(x + 14, y + 160, '38 s and 45 s miss the need: not accepted', 13, 'start', LV, True))
    x, y = 20, 206
    o.append(T(x + 14, y + 66, '(v) review every code change before merge', 13, 'start'))
    o.append(T(x + 14, y + 96, '114 ÷ 120 = 95.0% coverage', 15, 'start', NX, True))
    o.append(T(x + 14, y + 126, '6 changes merged unreviewed:', 13, 'start', MUT))
    o.append(T(x + 14, y + 146, 'a gap in the process to fix', 13, 'start', MUT))
    x, y = 364, 206
    o.append(T(x + 14, y + 66, '(vi) 40 payment tests on the release build', 13, 'start'))
    o.append(T(x + 14, y + 96, '37 ÷ 40 = 92.5% pass', 15, 'start', AC, True))
    o.append(T(x + 14, y + 126, '3 failures go back to QA', 13, 'start', MUT))
    o.append(T(x + 14, y + 146, 'as process feedback', 13, 'start', MUT))
    o.append(arc(364 + 40, 206 + 160, 20 + W - 40, 206 + 160, -0.25, NX, 2, 'x', '6 4'))
    return 400, ''.join(o)
FIG[2] = (f2, 'The six records sort into four boxes. Reviews find 30 defects without running anything; 8 of 10 users finish under 30 s with a mean of 24.0 s, but two do not, so the release is not accepted; review coverage is 95.0% and the test pass rate 92.5%, with the 3 failures fed back to QA.',
          'Four boxes. Verification lists three reviews finding 9, 6 and 15 defects, 30 in all. Validation shows ten user times as dots against a 30-second line, eight under it and two at 38 and 45 seconds. QA shows 114 of 120 changes reviewed, 95 percent. QC shows 37 of 40 tests passed, 92.5 percent, with a dashed arrow back to QA.')


# ---- 4.3 control flow graph ----
def f3():
    o = []
    P = {1: (200, 36), 2: (200, 106), 3: (110, 176), 5: (290, 176), 6: (200, 246), 7: (110, 316), 9: (290, 316), 10: (200, 386)}
    E = [(1, 2, ''), (2, 3, 'T'), (2, 5, 'F'), (3, 6, ''), (5, 6, ''), (6, 7, 'T'), (6, 9, 'F'), (7, 10, ''), (9, 10, '')]
    for a, b, lab in E:
        o.append(edge(P[a], P[b], 20, 0, AC, 2, 'n'))
        if lab:
            mx, my = (P[a][0] + P[b][0]) / 2, (P[a][1] + P[b][1]) / 2
            o.append(Tb(mx + (-14 if P[b][0] < P[a][0] else 14), my - 4, lab, 13, fill=NX if lab == 'T' else LV, bold=True))
    for n, (x, y) in P.items():
        dec = n in (2, 6)
        o.append(f'<circle cx="{x}" cy="{y}" r="20" style="fill:{ACS if dec else PANEL};stroke:{AC};stroke-width:2"/>')
        o.append(T(x, y + 5, str(n), 14, bold=True))
    notes = {1: 'read n', 2: 'n > 0 ?', 3: 's = n + 1', 5: 's = −n', 6: 's > 10 ?', 7: 'print large', 9: 'print small', 10: 'end'}
    for n, t in notes.items():
        x, y = P[n]
        if n in (3, 7):
            o.append(T(x - 26, y + 5, t, 13, 'end', MUT))
        else:
            o.append(T(x + 26, y + 5, t, 13, 'start', MUT))
    X = 420
    o.append(T(X, 40, 'N = 8 nodes, E = 9 edges, P = 1', 14, 'start', bold=True))
    o.append(T(X, 64, 'V(G) = E − N + 2P', 14, 'start'))
    o.append(T(X, 88, '= 9 − 8 + 2 = 3 basis paths', 14, 'start', AC, True))
    paths = [('1-2-3-6-7-10', 'n = 12', 's = 13 → large'), ('1-2-5-6-9-10', 'n = −5', 's = 5 → small'), ('1-2-3-6-9-10', 'n = 5', 's = 6 → small')]
    for i, (p, n, r) in enumerate(paths):
        y = 128 + i * 82
        o.append(R(X, y, 280, 66, PANEL, AC, 6))
        o.append(TM(X + 12, y + 24, p, 14, 'start', AC, True))
        o.append(T(X + 12, y + 48, f'input {n}:  {r}', 13, 'start'))
    o.append(T(X, 384, 'Numbers 4 and 8 are not used.', 13, 'start', MUT))
    return 410, ''.join(o)
FIG[3] = (f3, 'The control flow graph has 8 nodes and 9 edges in one component, so V(G) = 9 − 8 + 2 = 3. The inputs n = 12, n = −5 and n = 5 drive the three basis paths through the T and F branches of the two decisions.',
          'A control flow graph of nodes 1, 2, 3, 5, 6, 7, 9 and 10, with decisions at 2 (n greater than 0) and 6 (s greater than 10) splitting into true and false branches. Beside it, V(G) = 9 − 8 + 2 = 3 and three boxes for the basis paths with inputs 12, minus 5 and 5.')


# ---- 4.4 equivalence classes and boundaries ----
def f4():
    o = [T(20, 24, 'Age field: integer 1 to 120; senior discount from 60', 15, 'start', bold=True)]
    seg = [('C1 below 1', 'rejected', 20, 140, LVS, LV), ('C2 1 to 59', 'accepted, no discount', 140, 360, PANEL, AC),
           ('C3 60 to 120', 'accepted with discount', 360, 580, NXS, NX), ('C4 above 120', 'rejected', 580, 700, LVS, LV)]
    y = 60
    for a, b, x0, x1, f, st in seg:
        o.append(R(x0, y, x1 - x0, 64, f, st, 4))
        o.append(T((x0 + x1) / 2, y + 26, a, 14, fill=st if st != AC else INK, bold=True))
        o.append(T((x0 + x1) / 2, y + 46, b, 13, fill=MUT))
    yl = y + 104
    o.append(L(20, yl, 700, yl, L2, 1.6))
    pts = [(0, 106), (1, 140), (2, 174), (59, 326), (60, 360), (61, 394), (119, 546), (120, 580), (121, 614)]
    for v, x in pts:
        bad = v in (0, 121)
        disc = 60 <= v <= 120
        c = LV if bad else (NX if disc else AC)
        o.append(L(x, y + 64, x, yl, c, 1.2, '3 3'))
        o.append(C(x, yl, 7, c))
        o.append(T(x, yl + 26, str(v), 14, fill=c, bold=True))
    o.append(T(140, yl + 54, '1 − 1, 1, 1 + 1', 13, fill=MUT))
    o.append(T(360, yl + 54, '60 − 1, 60, 60 + 1', 13, fill=MUT))
    o.append(T(580, yl + 54, '120 − 1, 120, 120 + 1', 13, fill=MUT))
    o.append(T(20, yl + 94, '4 classes; 9 boundary values, 9 test cases: 0 and 121 rejected; 1, 2, 59 accepted;', 14, 'start', bold=True))
    o.append(T(20, yl + 116, '60, 61, 119, 120 accepted with the senior discount.', 14, 'start', bold=True))
    return yl + 132, ''.join(o)
FIG[4] = (f4, 'The age range splits into four equivalence classes, and behaviour changes at 1, 60 and 120. Testing just below, on and just above each edge gives nine cases: 0 and 121 are rejected, and the discount starts exactly at 60.',
          'A band split into four classes: below 1 rejected, 1 to 59 accepted, 60 to 120 accepted with discount, above 120 rejected. Under it a line with dots at 0, 1, 2, 59, 60, 61, 119, 120 and 121.')
AFTER[4] = 3


# ---- 4.5 driver, stub, unit vs integration ----
def f5():
    o = []
    o.append(T(20, 24, 'Unit test: calculateGST alone', 15, 'start', bold=True))
    o.append(boxt(20, 44, 150, 50, ['test driver'], PANEL, L2, 14, True))
    o.append(boxt(400, 44, 220, 50, ['calculateGST', 'unit under test'], ACS, AC, 13, True))
    o.append(L(172, 62, 398, 62, AC, 2, arrow='n')); o.append(T(285, 56, 'calculateGST(1000, 18)', 13))
    o.append(L(398, 80, 172, 80, L2, 2, '6 4', 'm')); o.append(T(285, 100, '1,000 × 18 ÷ 100 = ₹180', 13, fill=NX, bold=True))
    y = 134
    o.append(L(20, y, 700, y, LN, 1))
    o.append(T(20, y + 26, 'Top-down integration: Billing with an Invoice stub', 15, 'start', bold=True))
    o.append(boxt(20, y + 48, 150, 50, ['test driver'], PANEL, L2, 14, True))
    o.append(boxt(270, y + 48, 160, 50, ['Billing', 'unit under test'], ACS, AC, 13, True))
    o.append(boxt(530, y + 48, 170, 50, ['Invoice stub', 'returns ₹1,180'], LVS, LV, 13, True, dash='6 4'))
    o.append(boxt(530, y + 168, 170, 50, ['calculateGST'], PANEL, AC, 14, True))
    o.append(L(172, y + 73, 268, y + 73, AC, 2, arrow='n'))
    o.append(L(432, y + 66, 528, y + 66, AC, 2, arrow='n')); o.append(L(528, y + 84, 432, y + 84, LV, 2, '6 4', 'l'))
    o.append(T(480, y + 106, '₹1,180', 13, fill=LV, bold=True))
    o.append(L(400, y + 100, 528, y + 182, AC, 2, arrow='n')); o.append(Tb(420, y + 150, 'calculateGST(1180, 18)', 13))
    o.append(L(528, y + 204, 350, y + 104, L2, 2, '6 4', 'm')); o.append(Tb(470, y + 202, '₹212.40', 13, fill=NX, bold=True))
    o.append(R(20, y + 236, 680, 50, NXS, NX, 6))
    o.append(T(36, y + 258, 'GST = 1,180 × 18 ÷ 100 = ₹212.40;  total = 1,180 + 212.40 = ₹1,392.40', 14, 'start', NX, True))
    o.append(T(36, y + 278, 'a driver calls the unit; a stub is called by it', 13, 'start'))
    return y + 300, ''.join(o)
FIG[5] = (f5, 'In the unit test a driver calls calculateGST(1000, 18) and expects ₹180. In top-down integration the driver calls Billing, which gets ₹1,180 from the Invoice stub and calls calculateGST(1180, 18) for ₹212.40, a total of ₹1,392.40.',
          'Top: a test driver calls calculateGST with 1000 and 18 and gets 180. Bottom: a driver calls Billing; Billing gets 1,180 from a dashed Invoice stub, calls calculateGST with 1180 and 18, gets 212.40, and the total is 1,392.40.')
AFTER[5] = 2


# ---- 4.6 system test, acceptance gate, debugging loop ----
def f6():
    o = [T(20, 24, 'System test: transfer ₹500 from A to B', 15, 'start', bold=True)]
    def acct(x, y, name, before, after):
        return (boxt(x, y, 150, 50, [name, f'₹{before} → ₹{after}'], PANEL, AC, 13, True))
    o.append(acct(20, 40, 'A', '2,000', '1,500')); o.append(acct(250, 40, 'B', '1,000', '1,500'))
    o.append(L(172, 65, 248, 65, AC, 2, arrow='n')); o.append(T(210, 58, '₹500', 13, bold=True))
    o.append(T(420, 60, 'total stays 1,500 + 1,500', 13, 'start')); o.append(T(420, 80, '= ₹3,000', 13, 'start', NX, True))
    y = 118
    o.append(T(20, y + 4, 'Acceptance gate: 20 users × 3 transfers = 60 attempts', 15, 'start', bold=True))
    for i in range(20):
        c = NX if i < 18 else L2
        o.append(f'<circle cx="{30 + i * 22}" cy="{y + 28}" r="7" style="fill:{NXS if i < 18 else FIGBG};stroke:{c};stroke-width:1.6"/>')
    o.append(T(480, y + 33, 'pass needs 18 ÷ 20 = 90%', 14, 'start', NX, True))
    yb = y + 64
    o.append(R(20, yb, 680, 42, LVS, LV, 6))
    o.append(T(36, yb + 26, 'Reported failure: the app says success, but B still shows ₹1,000', 14, 'start', LV, True))
    # loop
    steps = [('reproduce', 'same balances,', 'same ₹500'), ('diagnose', 'debit commits,', 'credit does not'), ('repair', 'debit and credit in', 'one transaction'), ('regression', 'rerun old tests', 'and the new case')]
    bw, gap = 158, 16
    ys = yb + 72
    for i, (a, b, c) in enumerate(steps):
        x = 20 + i * (bw + gap)
        o.append(boxt(x, ys, bw, 66, [a, b, c], PANEL, AC, 13, True))
        if i: o.append(L(x - gap, ys + 33, x - 2, ys + 33, AC, 2, arrow='n'))
    o.append(L(360, yb + 44, 99, ys - 2, LV, 2, arrow='l'))
    xr = 20 + 3 * (bw + gap) + bw / 2
    o.append(P([(xr, ys + 68), (xr, ys + 92), (99, ys + 92)], L2, 2, '6 4'))
    o.append(L(99, ys + 92, 99, ys + 70, L2, 2, '6 4', 'm'))
    o.append(T(360, ys + 86, 'still failing? go round again', 13, fill=MUT))
    o.append(T(360, ys + 120, 'once fixed, rerun the system test before acceptance resumes', 13, fill=MUT))
    return ys + 134, ''.join(o)
FIG[6] = (f6, 'The ₹500 transfer passes system testing when A goes from ₹2,000 to ₹1,500 and B from ₹1,000 to ₹1,500, keeping ₹3,000 in total; acceptance needs 18 of 20 users, 90%. The failed credit seen in acceptance enters the debugging loop: reproduce, diagnose, repair, regression test.',
          'Account A 2,000 to 1,500 and B 1,000 to 1,500 with a 500 transfer arrow. A row of 20 user dots with 18 filled for the 90 percent gate. A red band for the failure where B stays 1,000, leading into four boxes: reproduce, diagnose, repair, regression.')


# ---- 4.7 regression scope ----
def f7():
    o = [T(20, 24, 'GST rate on invoices changes from 18% to 12%', 15, 'start', bold=True)]
    s = 300 / math.sqrt(500)
    x0, y0 = 20, 44
    a500, a80, a12 = 300, s * math.sqrt(80), s * math.sqrt(12)
    o.append(R(x0, y0, a500, a500, FIGBG, L2, 4, 1.5))
    o.append(T(x0 + 12, y0 + 24, 'full suite: 500 tests', 14, 'start', MUT, True))
    o.append(T(x0 + 12, y0 + 44, '(retest-all, the fallback)', 13, 'start', MUT))
    o.append(R(x0 + a500 - a80 - 14, y0 + a500 - a80 - 14, a80, a80, PANEL, AC, 4))
    o.append(T(x0 + a500 - a80 - 6, y0 + a500 - a80 + 6, 'regression', 13, 'start', AC, True))
    o.append(T(x0 + a500 - a80 - 6, y0 + a500 - a80 + 24, 'suite: 80', 13, 'start', AC, True))
    o.append(R(x0 + a500 - a12 - 22, y0 + a500 - a12 - 22, a12, a12, LVS, LV, 3, 2.5))
    o.append(L(x0 + 172, y0 + a500 - 45, x0 + a500 - a12 - 26, y0 + a500 - a12 / 2 - 22, LV, 1.6))
    o.append(T(x0 + 12, y0 + a500 - 40, '12 selected by impact', 13, 'start', LV, True))
    X = 350
    o.append(T(X, 60, 'Run order', 14, 'start', bold=True))
    for i, t in enumerate(['1  the 12 selected, GST invoice first', '2  then the 80, if they pass and time allows', '3  all 500 only if risk is high']):
        o.append(T(X, 84 + i * 22, t, 13, 'start', LV if i == 0 else INK, i == 0))
    o.append(T(X, 168, '500 ÷ 12 = 41.7 times fewer tests', 14, 'start', AC, True))
    o.append(T(X, 210, 'Update the invoice test first', 14, 'start', bold=True))
    ws = [130, 110, 110]
    o.append(row3(X, 224, ws, ['', 'old (18%)', 'new (12%)'], [(ACS, AC)] * 3, True, 30))
    o.append(row3(X, 254, ws, ['tax on ₹1,000', '₹180', '₹120'], [(PANEL, L2), (PANEL, L2), (NXS, NX)], False, 30))
    o.append(row3(X, 284, ws, ['invoice total', '₹1,180', '₹1,120'], [(PANEL, L2), (PANEL, L2), (NXS, NX)], False, 30))
    o.append(T(X, 334, 'A failure that expects 18% is the planned', 13, 'start', MUT))
    o.append(T(X, 352, 'change, not a defect.', 13, 'start', MUT))
    return 364, ''.join(o)
FIG[7] = (f7, 'Squares sized by test count: the 12 impact-selected tests sit inside the 80-test regression suite inside the 500-test full suite, so running the 12 first is 41.7 times cheaper than retest-all. The invoice test\'s expected tax changes from ₹180 to ₹120 with the rate.',
          'Three nested squares sized by count: 500 full suite, 80 regression suite, 12 selected tests highlighted. Beside them the run order, the ratio 500 divided by 12 equals 41.7, and a small table: tax on 1,000 old 180 new 120, total old 1,180 new 1,120.')


# ---- 4.8 load test curve ----
def f8():
    X0, X1, Y0, Y1 = 80, 640, 50, 330
    fx = lambda u: X0 + u / 20000 * (X1 - X0)
    fy = lambda t: Y1 - t / 6 * (Y1 - Y0)
    o = [axes(X0, X1, Y0, Y1, [0, 5000, 10000, 15000, 20000], [0, 1, 2, 3, 4, 5, 6], fx, fy, 'virtual users',
              '95th-percentile response time (s)', lambda v: f'{v:,}', str)]
    o.append(L(X0, fy(3), X1, fy(3), LV, 2, '7 5'))
    o.append(Tb(X0 + 8, fy(3) - 12, 'target 3 s', 13, 'start', LV, True))
    pts = [(5000, 1.4), (10000, 2.8), (15000, 4.2), (20000, 5.6)]
    o.append(P([(fx(u), fy(t)) for u, t in pts], AC, 3))
    for u, t in pts:
        o.append(C(fx(u), fy(t), 5.5, AC))
        o.append(T(fx(u) - 10, fy(t) + (22 if t == 2.8 else -10), f'{t} s', 13, 'end', bold=True))
    xc = fx(10714.29)
    o.append(L(xc, fy(3), xc, Y1, NX, 2, '4 3'))
    o.append(C(xc, fy(3), 6, NX))
    o.append(Tb(xc + 10, fy(1.2), '≈ 10,714 users', 13, 'start', NX, True))
    o.append(T(xc + 10, fy(0.6), '10,000 + 0.2 ÷ 0.00028', 13, 'start', MUT))
    o.append(T(fx(20000), fy(5.6) + 26, 'stress point', 13, 'end', LV, True))
    o.append(T(20, Y1 + 76, 'Throughput at peak: 10,000 searches ÷ 50 s = 200 searches per second.', 14, 'start', bold=True))
    return Y1 + 90, ''.join(o)
FIG[8] = (f8, 'Response time grows with load: 2.8 s at 10,000 users meets the 3 s target, and the line crosses it at about 10,714 users. The 20,000-user stress run reaches 5.6 s; throughput at peak is 200 searches a second.',
          'A line chart of 95th-percentile response time against virtual users, through 1.4 s at 5,000, 2.8 at 10,000, 4.2 at 15,000 and 5.6 at 20,000. A dashed line at 3 seconds is crossed at about 10,714 users.')


# ---- 4.9 OO, web and mobile test counts ----
def f9():
    o = []
    cw, gap = 220, 20
    for i, hd in enumerate(['OO: one case per actual type', 'Web: browsers × form cases', 'Mobile: devices × network loss']):
        x = 20 + i * (cw + gap)
        o.append(R(x, 16, cw, 330, FIGBG, L2, 8, 1.5)); o.append(T(x + cw / 2, 40, hd, 13, fill=AC, bold=True))
    x = 20
    o.append(boxt(x + 50, 58, 120, 36, ['Payment'], PANEL, AC, 14, True))
    o.append(boxt(x + 12, 140, 92, 36, ['UPI'], ACS, AC, 14, True)); o.append(boxt(x + 116, 140, 92, 36, ['Card'], ACS, AC, 14, True))
    for cx in (x + 58, x + 162):
        o.append(L(cx, 138, x + 110, 104, AC, 2))
    o.append(f'<polygon points="{x + 110},{95} {x + 102},{107} {x + 118},{107}" style="fill:{FIGBG};stroke:{AC};stroke-width:2"/>')
    o.append(T(x + 14, 210, 'case 1: p[0].pay(₹500)', 13, 'start')); o.append(T(x + 14, 228, 'must run UPI.pay', 13, 'start', MUT))
    o.append(T(x + 14, 256, 'case 2: p[1].pay(₹500)', 13, 'start')); o.append(T(x + 14, 274, 'must run Card.pay', 13, 'start', MUT))
    o.append(T(x + cw / 2, 322, '2 cases', 15, fill=AC, bold=True))
    x = 20 + cw + gap
    cols, rows = ['Chrome', 'Firefox'], ['valid login', 'wrong password']
    o.append(T(x + 136, 74, cols[0], 13, bold=True)); o.append(T(x + 190, 74, cols[1], 13, bold=True))
    for r, rn in enumerate(rows):
        yy = 90 + r * 60
        o.append(T(x + 12, yy + 28, rn, 13, 'start'))
        for c in range(2):
            ok = r == 0
            o.append(R(x + 114 + c * 54, yy + 6, 44, 40, NXS if ok else LVS, NX if ok else LV, 4))
            o.append(T(x + 136 + c * 54, yy + 31, '✓' if ok else '✗', 15, fill=NX if ok else LV, bold=True))
    o.append(T(x + 12, 236, 'valid: session cookie made', 13, 'start', MUT))
    o.append(T(x + 12, 256, 'wrong: no session', 13, 'start', MUT))
    o.append(T(x + cw / 2, 322, '2 × 2 = 4 cases', 15, fill=AC, bold=True))
    x = 20 + 2 * (cw + gap)
    for d in range(4):
        dx = x + 22 + d * 48
        o.append(R(dx, 70, 34, 60, PANEL, AC, 6)); o.append(R(dx + 12, 122, 10, 3, AC, AC, 1, 1))
        o.append(T(dx + 17, 104, str(d + 1), 14, bold=True))
    o.append(T(x + 12, 162, 'pay ₹500, cut the network', 13, 'start'))
    o.append(T(x + 12, 182, 'after the request', 13, 'start'))
    o.append(T(x + 12, 210, 'expect: error or retry,', 13, 'start', MUT))
    o.append(T(x + 12, 230, 'and exactly one debit', 13, 'start', LV, True))
    o.append(T(x + cw / 2, 322, '4 × 1 = 4 cases', 15, fill=AC, bold=True))
    o.append(T(360, 372, 'Total concrete test cases: 2 + 4 + 4 = 10', 15, bold=True))
    return 386, ''.join(o)
FIG[9] = (f9, 'Each kind of system has its own test axis: one case per actual type for Payment\'s subclasses UPI and Card, browsers × form cases for the web login, devices × network loss for the mobile payment. That gives 2 + 4 + 4 = 10 test cases.',
          'Three panels. OO: Payment with subclasses UPI and Card, cases 1 and 2. Web: a 2 by 2 grid of Chrome and Firefox against valid login and wrong password. Mobile: four phones, each with the network cut during a 500 rupee payment. Total 10 cases.')


TEXT = {}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d


def text_fixes(k):
    return TEXT.get(k, [])
