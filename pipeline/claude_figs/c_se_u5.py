"""Claude's hand-drawn figures for c-se-u5 (Software Engineering, unit 5: test management, automation and DevOps), one per
chapter, from each chapter's worked example, plus the sentences in the chapter text that describe a figure (text_fixes)."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {}


def bar(x, y, w, h, fill, st, lab=None, size=13, fc=INK, bold=False, dash=None):
    o = R(x, y, w, h, fill, st, 3, 2, dash)
    if lab: o += T(x + w / 2, y + h / 2 + size * 0.36, lab, size, fill=fc, bold=bold)
    return o


# ---- 5.1 does the test plan fit 18 days? ----
def f1():
    o = [T(20, 24, '45 requirements × 3 = 135 cases; 40 automated, 95 run by hand at 6 a day', 14, 'start', bold=True)]
    X0, X1 = 150, 640
    fx = lambda d: X0 + d / 30 * (X1 - X0)
    rows = [('3 full cycles', [15.833 / 2, 15.833 / 2, 15.833 / 2], ['cycle 1', 'cycle 2', 'cycle 3'], '23.8 days'),
            ('cycle 3 = smoke', [15.833 / 2, 15.833 / 2, 4.167 / 2], ['cycle 1', 'cycle 2', 'smoke'], '17.9 days (last box: smoke)')]
    y = 60
    for i, (name, ds, labs, tot) in enumerate(rows):
        o.append(T(X0 - 12, y + 26, name, 14, 'end', bold=True))
        d0 = 0
        for j, (d, lab) in enumerate(zip(ds, labs)):
            smoke = lab == 'smoke'
            o.append(bar(fx(d0), y, fx(d0 + d) - fx(d0), 40, NXS if smoke else ACS, NX if smoke else AC, lab if not smoke else '', 13, bold=True))
            d0 += d
        over = d0 > 18
        o.append(T(fx(d0) + 8, y + 26, tot, 14, 'start', LV if over else NX, True))
        y += 74
    o.append(xaxis(X0, X1, y, [0, 5, 10, 15, 20, 25, 30], fx, 'days with 2 testers'))
    o.append(L(fx(18), 44, fx(18), y, LV, 2, '6 4'))
    o.append(Tb(fx(18), 44, '18-day window', 13, fill=LV, bold=True))
    yb = y + 64
    lines = [('one full cycle', '95 ÷ 6 = 15.8 person-days', INK),
             ('three full cycles', '3 × 15.8 = 47.5 person-days ÷ 2 = 23.8 days: misses', LV),
             ('with a 25-case smoke cycle', '15.8 + 15.8 + 4.2 = 35.8 person-days ÷ 2 = 17.9 days: fits', NX)]
    for i, (a, b, c) in enumerate(lines):
        o.append(T(20, yb + i * 24, a, 13, 'start', bold=True)); o.append(T(230, yb + i * 24, b, 13, 'start', c, c != INK))
    o.append(T(20, yb + 84, 'Record the risk: cycle 3 no longer runs the full regression set.', 13, 'start', MUT))
    return yb + 96, ''.join(o)
FIG[1] = (f1, 'With two testers each full manual cycle of 95 cases takes about 7.9 days, so three full cycles end at 23.8 days, past the 18-day window. Swapping cycle 3 for the 25-case smoke subset ends at 17.9 days, inside it.',
          'Two timelines in days. Top: three full cycles reaching 23.8 days, past a dashed 18-day line. Bottom: two full cycles and a short smoke cycle reaching 17.9 days, inside the line. Below, the person-day arithmetic.')


# ---- 5.2 test group and summary report ----
def f2():
    o = [T(20, 24, 'Reporting line: 13 staff', 15, 'start', bold=True)]
    o.append(boxt(90, 40, 150, 36, ['test manager'], ACS, AC, 13, True))
    o.append(boxt(20, 120, 140, 36, ['functional lead'], PANEL, AC, 13, True))
    o.append(boxt(180, 120, 140, 36, ['automation lead'], PANEL, AC, 13, True))
    o.append(L(165, 78, 90, 118, AC, 2)); o.append(L(165, 78, 250, 118, AC, 2))
    o.append(T(250, 98, 'span 1:2', 13, 'start', MUT))
    for j in range(8):
        cx, cy = 34 + (j % 4) * 32, 186 + (j // 4) * 32
        o.append(R(cx - 12, cy - 12, 24, 24, PANEL, AC, 3, 1.4))
    o.append(L(90, 158, 90, 172, AC, 2)); o.append(T(90, 266, '8 test engineers, 1:8', 13, fill=MUT))
    for j in range(2):
        cx = 226 + j * 48
        o.append(R(cx - 12, 174, 24, 24, PANEL, AC, 3, 1.4))
    o.append(L(250, 158, 250, 172, AC, 2)); o.append(T(250, 220, '2 automation', 13, fill=MUT)); o.append(T(250, 238, 'engineers, 1:2', 13, fill=MUT))
    o.append(R(20, 286, 300, 36, FIGBG, L2, 6, 1.4, '5 4')); o.append(T(170, 309, 'domain expert: consults, not in the line', 13, fill=MUT))
    X = 352
    o.append(L(X - 14, 16, X - 14, 330, LN, 1))
    o.append(T(X, 24, 'Release 2.3 summary report', 15, 'start', bold=True))
    s = 340 / 480
    o.append(bar(X, 40, 456 * s, 30, NXS, NX, '456 passed', 13, bold=True))
    o.append(bar(X + 456 * s, 40, 18 * s, 30, LVS, LV)); o.append(bar(X + 474 * s, 40, 6 * s, 30, PANEL, L2))
    o.append(T(X, 92, 'pass rate 456 ÷ 480 = 95.0%', 13, 'start', NX, True))
    o.append(T(X, 112, '18 failed; blocked 6 ÷ 480 = 1.25%', 13, 'start'))
    o.append(T(X, 146, '30 defects = 18 failures + 12 exploratory', 13, 'start', bold=True))
    sv = [('sev 1–2', 12, LVS, LV), ('sev 3', 14, ACS, AC), ('sev 4', 4, PANEL, L2)]
    x = X; s2 = 340 / 30
    for n, v, f, st in sv:
        o.append(bar(x, 158, v * s2, 30, f, st, f'{n}: {v}' if v > 5 else str(v), 13, bold=True)); x += v * s2
    o.append(T(X, 210, '27 closed, 3 deferred (sev 3–4, accepted)', 13, 'start'))
    o.append(T(X, 236, 'leakage = 2 ÷ (30 + 2) = 6.25%', 13, 'start', LV, True))
    o.append(R(X, 256, 340, 66, NXS, NX, 6))
    o.append(T(X + 12, 278, 'Exit criteria met: ≥ 95% pass, ≤ 2% blocked,', 13, 'start'))
    o.append(T(X + 12, 296, 'no open severity 1 or 2 defect', 13, 'start'))
    o.append(T(X + 12, 314, 'Recommend: release 2.3, deferred fixes in 2.4', 13, 'start', NX, True))
    return 336, ''.join(o)
FIG[2] = (f2, 'Left: one test manager over two leads, 8 test engineers and 2 automation engineers, 13 staff, with the domain expert outside the line. Right: the release 2.3 numbers: 95.0% pass, 1.25% blocked, 30 defects with none open at severity 1 or 2, and leakage of 6.25%.',
          'An org chart: test manager over a functional lead with 8 engineers and an automation lead with 2 engineers, a dashed domain expert box outside. Beside it, a bar of 456 passed, 18 failed and 6 blocked cases, a bar of 30 defects by severity, leakage 6.25 percent and a green release recommendation.')
AFTER[2] = 2


# ---- 5.3 automation break-even ----
def f3():
    X0, X1, Y0, Y1 = 80, 640, 50, 340
    fx = lambda r: X0 + r / 40 * (X1 - X0)
    fy = lambda v: Y1 - v / 240 * (Y1 - Y0)
    o = [axes(X0, X1, Y0, Y1, [0, 10, 20, 30, 40], [0, 60, 120, 180, 240], fx, fy, 'runs of the suite', 'person-hours')]
    o.append(P([(fx(0), fy(0)), (fx(40), fy(240))], LV, 3))
    o.append(P([(fx(0), fy(60)), (fx(40), fy(140))], AC, 3))
    o.append(T(fx(31), fy(186) - 18, 'manual: 6 per run', 14, 'end', LV, True))
    o.append(T(fx(19), fy(98) + 34, 'automated: 60 + 2 per run', 14, 'start', AC, True))
    o.append(L(fx(15), fy(90), fx(15), Y1, NX, 2, '4 3')); o.append(C(fx(15), fy(90), 6.5, NX))
    o.append(Tb(fx(15) - 10, fy(90) - 18, 'break-even: 60 ÷ (6 − 2) = 15 runs, 90 h', 13, 'end', NX, True))
    for r, a, b in ((12, 72, 84), (36, 216, 132)):
        o.append(L(fx(r), fy(min(a, b)), fx(r), fy(max(a, b)), INK, 1.5, '3 3'))
        o.append(C(fx(r), fy(a), 4.5, LV)); o.append(C(fx(r), fy(b), 4.5, AC))
    o.append(Tb(fx(12) + 8, fy(70) + 22, 'year 1 (12 runs): 72 vs 84', 13, 'start'))
    o.append(Tb(fx(36) - 8, fy(174), '3 years: 216 − 132', 13, 'end', bold=True))
    o.append(Tb(fx(36) - 8, fy(174) + 18, '= 84 h saved', 13, 'end', NX, True))
    o.append(T(20, Y1 + 76, 'At 12 runs a year, 15 runs is 15 months: automation loses in year 1 and wins after.', 14, 'start', MUT))
    return Y1 + 90, ''.join(o)
FIG[3] = (f3, 'Manual effort grows 6 person-hours a run; automation starts at 60 and grows 2, so the lines cross at 15 runs and 90 person-hours. At 12 runs a year automation costs 84 against 72 in year 1, and over three years it saves 216 − 132 = 84 person-hours.',
          'Two straight lines of person-hours against runs: manual from 0 rising 6 per run, automated from 60 rising 2 per run. They cross at 15 runs and 90 hours. Markers at 12 runs (72 against 84) and 36 runs (216 against 132).')


# ---- 5.4 test metrics ----
def f4():
    o = [T(20, 24, 'Where the 100 defects were found', 15, 'start', bold=True)]
    s = 680 / 100
    o.append(bar(20, 40, 90 * s, 40, NXS, NX, '90 found in test', 14, bold=True))
    o.append(bar(20 + 90 * s, 40, 10 * s, 40, LVS, LV, '10', 14, LV, True))
    o.append(T(700, 100, 'found after release', 13, 'end', LV))
    o.append(T(20, 122, 'DRE = 90 ÷ 100 = 90%', 14, 'start', NX, True))
    o.append(T(260, 122, 'leakage = 10 ÷ 100 = 10%: raise this at go/no-go', 14, 'start', LV, True))
    o.append(T(20, 166, 'Test execution: 1140 of 1200 planned cases', 15, 'start', bold=True))
    s2 = 680 / 1200
    x = 20
    for v, f, st, lab in ((900, NXS, NX, '900 passed'), (180, LVS, LV, '180 failed'), (60, PANEL, L2, ''), (60, FIGBG, L2, '')):
        o.append(R(x, 182, v * s2, 40, f, st, 3, 2, '4 3' if f == FIGBG else None))
        if lab: o.append(T(x + v * s2 / 2, 207, lab, 13, bold=True))
        x += v * s2
    o.append(T(700, 242, 'then 60 blocked, 60 not run', 13, 'end', MUT))
    o.append(T(20, 246, 'progress = 1140 ÷ 1200 = 95%', 14, 'start', bold=True))
    tiles = [('defect density', '90 ÷ 15 KLOC', '6 per KLOC'), ('MTBF', '5000 h ÷ 8 failures', '625 h'), ('progress', '1140 ÷ 1200', '95%')]
    tw_, gap = 216, 16
    for i, (a, b, c) in enumerate(tiles):
        x = 20 + i * (tw_ + gap)
        o.append(boxt(x, 274, tw_, 70, [a, b, c], PANEL, AC, 13, True, fills=[INK, MUT, AC]))
    return 356, ''.join(o)
FIG[4] = (f4, 'Of 100 defects, 90 were found in test and 10 after release, so DRE is 90% and leakage 10%, the number to raise at the go/no-go meeting. 1140 of 1200 planned cases ran, 95% progress; density is 6 per KLOC and MTBF 625 hours.',
          'A bar of 100 defects split 90 found in test and 10 after release. A bar of 1200 planned cases split 900 passed, 180 failed, 60 blocked and 60 not run. Three tiles: density 6 per KLOC, MTBF 625 hours, progress 95 percent.')


# ---- 5.5 merge with one conflict ----
def f5():
    o = [T(20, 24, 'Commit graph (arrows point to parents)', 15, 'start', bold=True)]
    P_ = {'B': (60, 126), 'C': (220, 82), 'E': (220, 172), 'M': (380, 126)}
    o.append(edge(P_['C'], P_['B'], 22, 0, AC, 2, 'n')); o.append(edge(P_['E'], P_['B'], 22, 0, AC, 2, 'n'))
    o.append(edge(P_['M'], P_['C'], 22, 0, NX, 2, 'x')); o.append(edge(P_['M'], P_['E'], 22, 0, NX, 2, 'x'))
    for n, (x, y) in P_.items():
        f = NXS if n == 'M' else PANEL
        o.append(f'<circle cx="{x}" cy="{y}" r="22" style="fill:{f};stroke:{NX if n == "M" else AC};stroke-width:2"/>')
        o.append(T(x, y + 5, n, 15, bold=True))
    o.append(T(60, 166, 'base', 13, fill=MUT)); o.append(T(260, 76, 'main tip', 13, 'start', MUT)); o.append(T(260, 186, 'feature/pay tip', 13, 'start', MUT))
    o.append(T(410, 120, 'M has 2 parents:', 13, 'start', NX, True)); o.append(T(410, 138, 'C and E', 13, 'start', NX, True))
    # file strips
    y0 = 252
    o.append(L(20, y0 - 14, 700, y0 - 14, LN, 1))
    o.append(T(20, y0 + 8, 'app.py, one cell per line', 15, 'start', bold=True))
    cw, ch = 24, 9
    cols = [('B: 20 lines', 20, {}), ('C (main)', 20, {4: 'L', 15: 'A'}), ('E (feature)', 26, {4: 'L', **{k: 'N' for k in range(11, 17)}}),
            ('M: 26 lines', 26, {4: 'X', 21: 'A', **{k: 'N' for k in range(11, 17)}})]
    for j, (lab, n, marks) in enumerate(cols):
        x = 40 + j * 170
        o.append(T(x, y0 + 36, lab, 13, 'start', bold=True))
        for i in range(n):
            m = marks.get(i + 1)
            f, st = {'L': (LVS, LV), 'A': (ACS, AC), 'N': (NXS, NX), 'X': (LV, LV)}.get(m, (PANEL, L2))
            o.append(R(x, y0 + 46 + i * (ch + 2), 60, ch, f, st, 1.5, 1.2))
        if j:
            o.append(T(x + 70, y0 + 46 + 3 * (ch + 2) + 8, 'line 4', 13, 'start', LV, True))
    o.append(T(x + 70, y0 + 46 + 3 * (ch + 2) + 26, '1 conflict', 13, 'start', LV, True))
    o.append(T(450, y0 + 46 + 12 * (ch + 2) + 6, '6 inserted', 13, 'start', NX, True))
    o.append(T(450, y0 + 46 + 12 * (ch + 2) + 24, 'after line 10', 13, 'start', NX))
    o.append(T(620, y0 + 46 + 20 * (ch + 2) + 8, 'main\'s line 15', 13, 'start', AC))
    o.append(T(210 + 70, y0 + 46 + 14 * (ch + 2) + 8, 'line 15', 13, 'start', AC, True))
    o.append(T(20, y0 + 46 + 26 * (ch + 2) + 26, '20 + 6 = 26 lines; only line 4 changed on both sides, so Git stops on 1 conflict region.', 13, 'start', MUT))
    return y0 + 46 + 26 * (ch + 2) + 40, ''.join(o)
FIG[5] = (f5, 'Main tip C and feature tip E both change line 4, so the merge stops on that one conflict; the 6 lines inserted after line 10 and main\'s change at line 15 join cleanly. Merge commit M has 26 lines and two parents, C and E.',
          'A commit graph: base B with children C on main and E on feature/pay, both pointing back to B, and merge commit M pointing to both. Below, four strips of line cells for B, C, E and M: line 4 changed in C and E, six new lines after line 10 in E, line 15 changed in C, and M with 26 lines and one conflict at line 4.')


# ---- 5.6 pipeline timings ----
def f6():
    X0, X1 = 150, 640
    fx = lambda m: X0 + m / 42 * (X1 - X0)
    stages = ['build', 'unit', 'integration', 'package', 'staging', 'smoke']
    runs = [('all in series', [5, 8, 20, 3, 2, 3], '41 min'), ('4 integration shards', [5, 8, 5, 3, 2, 3], '26 min'),
            ('+ 2 unit shards', [5, 4, 5, 3, 2, 3], '22 min')]
    o = []
    y = 30
    for name, ts, tot in runs:
        o.append(T(X0 - 12, y + 25, name, 13, 'end', bold=True))
        m = 0
        for st, t in zip(stages, ts):
            smoke = st == 'smoke'
            hot = (st == 'integration' and t == 5) or (st == 'unit' and t == 4)
            f, c = (LVS, LV) if smoke else ((NXS, NX) if hot else (ACS if st in ('unit', 'integration') else PANEL, AC))
            w = fx(m + t) - fx(m)
            o.append(R(fx(m), y, w, 40, f, c, 3, 1.6))
            lab = {('integration', 20): 'integration', ('integration', 5): 'int ×4', ('unit', 8): 'unit', ('unit', 4): 'unit', ('build', 5): 'build'}.get((st, t), '')
            if lab and w > tw(lab, 13) + 6:
                o.append(T(fx(m) + w / 2, y + 25, lab, 13))
            m += t
        o.append(T(fx(m) + 8, y + 25, tot, 14, 'start', bold=True))
        y += 62
    o.append(xaxis(X0, X1, y - 6, [0, 10, 20, 30, 40], fx, 'minutes'))
    yk = y + 62
    o.append(R(20, yk, 16, 14, PANEL, AC, 3)); o.append(T(42, yk + 12, 'the two short boxes: package 3 min, staging 2 min', 13, 'start', MUT))
    o.append(R(20, yk + 24, 16, 14, LVS, LV, 3)); o.append(T(42, yk + 36, 'smoke 3 min: the release gate, never removed', 13, 'start', LV, True))
    o.append(R(380, yk, 16, 14, NXS, NX, 3)); o.append(T(402, yk + 12, 'a stage split into parallel shards', 13, 'start', NX))
    o.append(T(20, yk + 70, 'Deleting smoke instead would save 3 min (26 → 23), less than the 4 min the unit shards win, and lose the gate.', 13, 'start'))
    return yk + 84, ''.join(o)
FIG[6] = (f6, 'The same six stages run three ways. In series they take 41 min; four integration shards cut 20 min to 5 for 26 min in all; two unit shards cut 8 to 4 for 22 min. The 3-minute smoke gate stays in every run.',
          'Three horizontal pipeline bars of six stages: 41 minutes in series, 26 minutes with integration cut to 5, 22 minutes with unit tests also cut to 4. The smoke stage at the end of each bar is highlighted.')
AFTER[6] = 2


# ---- 5.7 incremental build ----
def f7():
    o = [T(20, 24, '40 modules; this commit touches 3', 15, 'start', bold=True)]
    for i in range(40):
        x, y = 20 + (i % 20) * 34, 40 + (i // 20) * 34
        hot = i in (5, 17, 26)
        o.append(R(x, y, 28, 28, LVS if hot else PANEL, LV if hot else L2, 4, 2 if hot else 1.3))
    y = 130
    X0, s = 150, 540 / 1800
    o.append(T(X0 - 12, y + 25, 'full build', 14, 'end', bold=True))
    o.append(bar(X0, y, 1800 * s, 40, PANEL, L2, '30 min = 1800 s', 14, bold=True))
    o.append(T(X0 - 12, y + 85, 'incremental', 14, 'end', bold=True))
    o.append(bar(X0, y + 60, 135 * s, 40, LVS, LV)); o.append(bar(X0 + 135 * s, y + 60, 60 * s, 40, ACS, AC))
    o.append(T(X0 + 195 * s + 10, y + 78, '3 × 45 s compile + 60 s link and package', 13, 'start'))
    o.append(T(X0 + 195 * s + 10, y + 96, '= 195 s = 3 min 15 s', 13, 'start', bold=True))
    o.append(T(20, y + 140, '1800 ÷ 195 = 9.23 times shorter, about one-ninth of the full build', 14, 'start', NX, True))
    yt = y + 172
    o.append(T(20, yt, 'The published artifact', 15, 'start', bold=True))
    o.append(R(20, yt + 14, 260, 44, NXS, NX, 6)); o.append(TM(150, yt + 43, '2.3.0-231', 20, fill=NX, bold=True))
    o.append(L(110, yt + 60, 110, yt + 80, L2, 1.5)); o.append(T(110, yt + 96, 'release version 2.3.0', 13, fill=MUT))
    o.append(L(222, yt + 60, 222, yt + 80, L2, 1.5)); o.append(T(232, yt + 96, 'build number 231', 13, fill=MUT))
    o.append(T(330, yt + 32, 'published once, then the same artifact', 13, 'start'))
    o.append(T(330, yt + 50, 'is promoted to test, staging and production', 13, 'start'))
    return yt + 110, ''.join(o)
FIG[7] = (f7, 'Only 3 of the 40 modules changed, so the incremental build compiles them in 3 × 45 = 135 s and links and packages in 60 s: 195 s, 9.23 times shorter than the 1800 s full build. It publishes artifact 2.3.0-231 once.',
          'A grid of 40 module squares with 3 highlighted. A long bar for the 1800-second full build and a short bar of 135 plus 60 seconds for the incremental build. A tag 2.3.0-231 split into release version 2.3.0 and build number 231.')


# ---- 5.8 Ansible runs across 12 hosts ----
def f8():
    o = []
    rows = [('first run, all reachable', [3] * 12, '12 × 3 = 36 changes'),
            ('second run, nothing drifted', [0] * 12, '0 changes; handler not notified'),
            ('first run, host 9 down', [3] * 8 + [None] + [3] * 3, 'recap: 11 ok, 1 failed'),
            ('rerun after the fix', [0] * 8 + [3] + [0] * 3, '1 host changed, 3 changes')]
    X0, cw = 20, 32
    o.append(T(X0, 24, 'Each square is one web server; the number is the changes the play made there', 14, 'start', bold=True))
    for j in range(12):
        o.append(T(X0 + j * (cw + 4) + cw / 2, 50, str(j + 1), 13, fill=MUT))
    y = 60
    for name, vals, note in rows:
        for j, v in enumerate(vals):
            x = X0 + j * (cw + 4)
            if v is None:
                o.append(R(x, y, cw, 34, LVS, LV, 4, 2.5)); o.append(T(x + cw / 2, y + 23, '✗', 15, fill=LV, bold=True))
            else:
                f, st = (ACS, AC) if v else (FIGBG, L2)
                o.append(R(x, y, cw, 34, f, st, 4, 1.6)); o.append(T(x + cw / 2, y + 23, str(v), 14, fill=INK if v else MUT, bold=bool(v)))
        o.append(T(X0 + 12 * (cw + 4) + 8, y + 15, name, 13, 'start', bold=True))
        o.append(T(X0 + 12 * (cw + 4) + 8, y + 32, note, 13, 'start', LV if 'failed' in note else (NX if note.startswith('0') else AC)))
        y += 52
    o.append(T(X0, y + 14, '3 changes on a fresh host: install nginx, write nginx.conf, start and enable the service.', 13, 'start', MUT))
    o.append(T(X0, y + 34, 'Idempotent: running the same playbook again changes only what differs.', 13, 'start', MUT))
    return y + 48, ''.join(o)
FIG[8] = (f8, 'Twelve hosts, four runs of the same playbook: a full first run makes 3 changes on each host, 36 in all, and a second run makes 0, so the reload handler is not notified. With host 9 down the recap is 11 ok and 1 failed, and the rerun after the fix changes only host 9.',
          'Four rows of 12 host squares. Row 1: all 3s, 36 changes. Row 2: all 0s. Row 3: 3s with host 9 marked failed, 11 ok and 1 failed. Row 4: 0s except host 9 with 3.')


TEXT = {}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d


def text_fixes(k):
    return TEXT.get(k, [])
