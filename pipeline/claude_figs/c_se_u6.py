"""Claude's hand-drawn figures for c-se-u6 (Software Engineering, unit 6: project management and software quality), one per
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


# ---- 6.1 four views feed one plan; spend checkpoints ----
def f1():
    o = [T(20, 24, 'Hostel mess app: 6 students, 10 weeks, ₹40,000', 15, 'start', bold=True)]
    views = [('People', '6 students,', 'named owners', 'week-1 skills check'), ('Product', '8 features:', 'keep 5, defer 3', 'review by week 5'),
             ('Process', 'weekly build', 'and review', 'week-5 review'), ('Project', '₹40,000 ÷ 10', '= ₹4,000 a week', 'checks weeks 6, 10')]
    bw, gap = 161, 12
    for i, (a, b, c, d) in enumerate(views):
        x = 20 + i * (bw + gap)
        o.append(boxt(x, 40, bw, 90, [a, b, c, d], PANEL, AC, 13, True, fills=[INK, INK, INK, NX]))
        o.append(L(x + bw / 2, 132, 360, 160, L2, 1.6, arrow='m'))
    o.append(boxt(260, 162, 200, 36, ['one-page plan'], ACS, AC, 14, True))
    X0, X1, Y0, Y1 = 90, 580, 240, 400
    fx = lambda w: X0 + w / 10 * (X1 - X0)
    fy = lambda v: Y1 - v / 40000 * (Y1 - Y0)
    o.append(axes(X0, X1, Y0, Y1, [0, 2, 4, 6, 8, 10], [0, 20000, 40000], fx, fy, 'week', 'planned spend (₹)', str, lambda v: f'{v:,}'))
    o.append(P([(fx(0), fy(0)), (fx(10), fy(40000))], AC, 3))
    for w, v, lab in ((6, 24000, 'week 6: 6 × 4,000 = ₹24,000'), (10, 40000, 'week 10: ₹40,000')):
        o.append(L(fx(w), fy(v), fx(w), Y1, NX, 1.6, '4 3')); o.append(C(fx(w), fy(v), 6, NX))
        o.append(Tb(fx(w) - 10, fy(v) - 12, lab, 13, 'end', NX, True))
    o.append(T(600, 300, 'compare actual', 13, 'start', MUT)); o.append(T(600, 318, 'spend at each', 13, 'start', MUT))
    o.append(T(600, 336, 'checkpoint; a', 13, 'start', MUT)); o.append(T(600, 354, 'miss means replan', 13, 'start', LV, True))
    return Y1 + 54, ''.join(o)
FIG[1] = (f1, 'Each of the four views adds its own control point to one plan: 5 of 8 features kept, a week-5 review, and an even ₹4,000 a week, so ₹24,000 should be spent by week 6 and ₹40,000 by week 10. A miss at a checkpoint sends the team back to replanning.',
          'Four boxes, people, product, process and project, each with a control point, feeding a one-page plan. Below, a straight planned-spend line from 0 to 40,000 rupees over 10 weeks, marked at week 6 (24,000) and week 10 (40,000).')


# ---- 6.2 three metrics, count over base ----
def f2():
    o = []
    s = 560 / 240
    x0 = 120
    o.append(T(20, 24, 'Effort variance: extra effort ÷ planned effort', 15, 'start', bold=True))
    o.append(T(x0 - 10, 58, 'planned', 13, 'end')); o.append(bar(x0, 40, 200 * s, 28, PANEL, AC, '200 person-days', 13, bold=True))
    o.append(T(x0 - 10, 96, 'actual', 13, 'end')); o.append(bar(x0, 78, 200 * s, 28, PANEL, AC)); o.append(bar(x0 + 200 * s, 78, 30 * s, 28, LVS, LV, '+30', 13, LV, True))
    o.append(T(x0 + 230 * s + 8, 97, '230', 13, 'start', bold=True))
    o.append(T(x0, 128, '30 ÷ 200 × 100% = 15% over plan', 14, 'start', LV, True))
    y = 160
    o.append(T(20, y + 4, 'DRE: defects caught before delivery ÷ all defects', 15, 'start', bold=True))
    s2 = 560 / 160
    o.append(bar(x0, y + 18, 120 * s2, 30, NXS, NX, '120 before delivery', 13, bold=True)); o.append(bar(x0 + 120 * s2, y + 18, 30 * s2, 30, LVS, LV, '30 after', 13, LV, True))
    o.append(T(x0 - 10, y + 38, '150 defects', 13, 'end'))
    o.append(T(x0, y + 72, '120 ÷ 150 × 100% = 80%: one defect in five escaped to users', 14, 'start', NX, True))
    y = 268
    o.append(T(20, y + 4, 'Defect density: the same 150 defects ÷ 25 KLOC', 15, 'start', bold=True))
    for k in range(25):
        x = x0 + k * 22.4
        o.append(R(x, y + 18, 19, 30, PANEL, L2, 2, 1.2))
    o.append(T(x0 - 10, y + 38, '25 KLOC', 13, 'end'))
    o.append(T(x0, y + 72, '150 ÷ 25 = 6 per KLOC  (120 ÷ 25 = 4.8 before release, 30 ÷ 25 = 1.2 after)', 14, 'start', AC, True))
    return y + 88, ''.join(o)
FIG[2] = (f2, 'Each metric divides one count by a base: 30 extra person-days over the 200 planned is a 15% overrun; 120 of all 150 defects caught before delivery is a DRE of 80%; the same 150 defects over 25 KLOC is a density of 6 per KLOC.',
          'Three panels. Planned 200 against actual 230 person-days with the extra 30 highlighted, 15 percent. A bar of 150 defects split 120 before and 30 after delivery, DRE 80 percent. Twenty-five KLOC cells for a density of 6 defects per KLOC.')


# ---- 6.3 basic COCOMO chain ----
def f3():
    o = [T(20, 24, 'Basic COCOMO, organic mode: a = 2.4, b = 1.05, c = 2.5, d = 0.38', 15, 'start', bold=True)]
    steps = [('size', '10 KLOC', '', PANEL, AC), ('effort', 'E = 2.4 × 10^1.05', '= 26.9 person-months', ACS, AC),
             ('duration', 'D = 2.5 × 26.9^0.38', '= 8.7 months', ACS, AC), ('average staff', 'E ÷ D = 26.9 ÷ 8.7', '≈ 3.1 people', ACS, AC),
             ('cost', '26.9 × ₹80,000', '= ₹21,54,240 ≈ ₹21.5 lakh', NXS, NX)]
    y = 44
    for i, (a, b, c, f, st) in enumerate(steps):
        o.append(R(120, y, 460, 52, f, st, 6))
        o.append(T(108, y + 31, a, 14, 'end', bold=True))
        o.append(T(136, y + 23, b, 14, 'start'))
        if c: o.append(T(136, y + 43, c, 14, 'start', st if st == NX else AC, True))
        if i < 4: o.append(L(350, y + 54, 350, y + 72, AC, 2, arrow='n'))
        y += 74
    o.append(T(600, 70, 'the sized', 13, 'start', MUT)); o.append(T(600, 88, 'input', 13, 'start', MUT))
    o.append(T(600, 366, 'the money', 13, 'start', NX)); o.append(T(600, 384, 'answer', 13, 'start', NX))
    o.append(T(20, y + 10, 'Each box is computed from the one above it; 1 lakh = ₹1,00,000.', 13, 'start', MUT))
    return y + 24, ''.join(o)
FIG[3] = (f3, 'The estimate is one chain: 10 KLOC gives 26.9 person-months of effort, which gives 8.7 months of duration and about 3.1 people on average, and 26.9 person-months at ₹80,000 cost about ₹21.5 lakh.',
          'Five stacked boxes joined by arrows: size 10 KLOC, effort 26.9 person-months, duration 8.7 months, average staff 3.1 people, and cost 21.5 lakh rupees.')


# ---- 6.4 schedule with critical path and slack ----
def f4():
    X0, X1 = 200, 600
    fx = lambda d: X0 + d / 14 * (X1 - X0)
    tasks = [('A', 0, 3, 0, 'start'), ('B', 3, 7, 0, 'after A'), ('C', 3, 5, 4, 'after A'), ('D', 7, 12, 0, 'after B'), ('E', 5, 8, 4, 'after C'), ('F', 12, 14, 0, 'after D and E')]
    o = [T(20, 24, 'Forward pass: earliest start and finish of each task (days)', 15, 'start', bold=True)]
    y = 44
    for n, es, ef, sl, dep in tasks:
        crit = sl == 0
        o.append(T(X0 - 14, y + 22, n, 15, 'end', LV if crit else INK, True))
        o.append(T(X0 - 34, y + 22, dep, 13, 'end', MUT))
        o.append(bar(fx(es), y, fx(ef) - fx(es), 32, LVS if crit else ACS, LV if crit else AC, f'{es}–{ef}', 13, bold=True))
        if sl:
            o.append(R(fx(ef), y + 8, fx(ef + sl) - fx(ef), 16, FIGBG, L2, 3, 1.5, '4 3'))
            o.append(T(fx(ef + sl) + 8, y + 21, f'slack {sl} days', 13, 'start', MUT, True))
        y += 44
    o.append(xaxis(X0, X1, y + 4, list(range(0, 15, 2)), fx, 'day'))
    o.append(L(fx(12), 44 + 3 * 44 + 32, fx(12), 44 + 5 * 44, L2, 1.4, '3 3'))
    o.append(L(fx(8), 44 + 4 * 44 + 32, fx(8), 44 + 5 * 44 + 16, L2, 1.4, '3 3'))
    o.append(T(20, y + 74, 'Critical path A → B → D → F: 3 + 4 + 5 + 2 = 14 days, zero slack. F starts at max(12, 8) = 12.', 14, 'start', LV, True))
    return y + 88, ''.join(o)
FIG[4] = (f4, 'A, B, D and F run back to back from day 0 to day 14 with no slack, so they fix the finish date. F waits for both D and E and starts at day 12, the later finish, while C and E each have 4 days of slack.',
          'A Gantt chart over 14 days: A 0 to 3, B 3 to 7, C 3 to 5 with 4 days of slack, D 7 to 12, E 5 to 8 with 4 days of slack, F 12 to 14. A, B, D and F are highlighted as the critical path.')


# ---- 6.5 risk exposure as area ----
def f5():
    o = [T(20, 24, 'Risk exposure RE = probability × impact (area of each box)', 15, 'start', bold=True)]
    X0, Y1 = 60, 290
    sx, sy = 30, 470
    risks = [('R1 key developer leaves', 0.2, 6, LVS, LV), ('R2 payment API changes', 0.4, 3, LVS, LV), ('R3 server outage', 0.1, 10, PANEL, AC)]
    x = X0
    for name, p, i, f, st in risks:
        w, h = i * sx, p * sy
        o.append(R(x, Y1 - h, w, h, f, st, 3))
        o.append(T(x + w / 2, Y1 - h - 30, name.split(' ', 1)[0], 14, fill=st, bold=True))
        o.append(T(x + w / 2, Y1 - h - 12, name.split(' ', 1)[1], 13, fill=MUT))
        o.append(T(x + w / 2, Y1 - h / 2 + 5, f'{p} × {i} = {p * i:.1f}', 13, bold=True))
        o.append(T(x + w / 2, Y1 + 20, f'impact {i} pw', 13, fill=MUT))
        x += w + 24
    o.append(L(X0 - 12, Y1, X0 - 12, Y1 - 0.4 * sy, L2, 1.4))
    o.append(T(X0 - 18, Y1 - 0.4 * sy + 5, '0.4', 13, 'end', MUT)); o.append(T(X0 - 18, Y1 - 0.2 * sy + 5, '0.2', 13, 'end', MUT))
    o.append(T(X0 - 18, Y1 - 0.1 * sy + 5, '0.1', 13, 'end', MUT))
    o.append(T(20, Y1 + 50, 'Rank: R1 = R2 = 1.2 person-weeks, then R3 = 1.0. R1 gets the full RMMM entry:', 14, 'start', bold=True))
    cols = [('mitigate', 'pair on the module,', 'written handover note'), ('monitor', 'tech lead checks', 'monthly, logs status'), ('manage', 'named backup takes', 'over within a week')]
    for i, (a, b, c) in enumerate(cols):
        o.append(boxt(20 + i * 230, Y1 + 64, 220, 66, [a, b, c], NXS, NX, 13, True))
    return Y1 + 144, ''.join(o)
FIG[5] = (f5, 'Each risk is a box with probability as height and impact as width, so its area is the exposure: R1 (0.2 × 6) and R2 (0.4 × 3) both cover 1.2 person-weeks, and R3 (0.1 × 10) covers 1.0. R1 gets the full mitigation, monitoring and management entry.',
          'Three rectangles: R1 tall-ish and 6 wide, R2 twice as tall and 3 wide, R3 short and 10 wide, labelled 1.2, 1.2 and 1.0 person-weeks. Below, three boxes of the RMMM entry for R1: mitigate, monitor, manage.')
AFTER[5] = 3


# ---- 6.6 baselines B1 and B2 ----
def f6():
    o = []
    ws = [200, 150, 150, 160]
    x0, y = 20, 56
    heads = ['configuration item', 'baseline B1', 'baseline B2', '']
    rows = [('login module', '1.0', '1.1', True), ('SRS', '1.0', '1.0', False), ('test plan', '1.0', '1.1', True)]
    x = x0
    for w, h in zip(ws[:3], heads[:3]):
        o.append(bar(x, y, w, 36, ACS, AC, h, 14, bold=True)); x += w
    for i, (n, a, b, ch) in enumerate(rows):
        yy = y + 36 + i * 44
        x = x0
        o.append(R(x, yy, ws[0], 44, PANEL, L2, 2, 1.4)); o.append(T(x + 14, yy + 27, n, 14, 'start', bold=True)); x += ws[0]
        o.append(bar(x, yy, ws[1], 44, PANEL, L2, a, 15)); x += ws[1]
        o.append(bar(x, yy, ws[2], 44, NXS if ch else PANEL, NX if ch else L2, b, 15, NX if ch else INK, ch)); x += ws[2]
        o.append(T(x + 14, yy + 27, 'changed by CR-07' if ch else 'not in the CR', 13, 'start', NX if ch else MUT, ch))
    yb = y + 36 + 3 * 44 + 30
    o.append(arc(x0 + ws[0] + ws[1] / 2, y - 4, x0 + ws[0] + ws[1] + ws[2] / 2 - 6, y - 4, 0.22, NX, 2, 'x'))
    o.append(T(x0 + ws[0] + ws[1], y - 26, 'CR-07', 13, fill=NX, bold=True))
    o.append(T(20, yb, 'Approved CR-07 → 2 of 3 items changed; B2 is frozen as the new baseline.', 14, 'start', bold=True))
    o.append(T(20, yb + 22, 'B1 stays recorded, so the old release can still be rebuilt exactly.', 13, 'start', MUT))
    return yb + 36, ''.join(o)
FIG[6] = (f6, 'Approved change CR-07 moves the login module and the test plan from 1.0 to 1.1, while the SRS stays at 1.0. Two of the three items changed, and B2 is frozen as the new baseline beside the recorded B1.',
          'A table of three configuration items against baselines B1 and B2: login module 1.0 to 1.1, SRS 1.0 to 1.0, test plan 1.0 to 1.1, with the two changed cells highlighted and labelled changed by CR-07.')


# ---- 6.7 inspection numbers ----
def f7():
    o = [T(20, 24, 'Inspection of a 4,000-line module', 15, 'start', bold=True)]
    X0, X1 = 60, 660
    fx = lambda r: X0 + r / 300 * (X1 - X0)
    y = 60
    o.append(R(fx(100), y, fx(200) - fx(100), 26, NXS, NX, 3, 1.4))
    o.append(T((fx(100) + fx(200)) / 2, y + 18, 'normal band 100–200 lines/h', 13, fill=NX))
    o.append(xaxis(X0, X1, y + 26, [0, 100, 200, 300], fx, None))
    o.append(L(fx(200), y - 10, fx(200), y + 30, AC, 3)); o.append(C(fx(200), y - 10, 6, AC))
    o.append(T(fx(200) - 10, y - 6, 'rate = 4,000 ÷ 20 h = 200 lines per hour', 13, 'end', AC, True))
    y = 150
    o.append(T(20, y, 'All 24 defects in the module', 15, 'start', bold=True))
    s = 680 / 24
    for k in range(24):
        rev = k < 20
        o.append(R(20 + k * s + 2, y + 14, s - 4, 34, ACS if rev else LVS, AC if rev else LV, 3, 1.5))
    o.append(T(20 + 10 * s, y + 70, '20 found by the inspection', 13, fill=AC, bold=True))
    o.append(T(20 + 22 * s, y + 70, '4 by testing', 13, fill=LV, bold=True))
    tiles = [('density', '24 ÷ 4 KLOC', '6 defects per KLOC', AC), ('effectiveness', '20 ÷ 24 × 100%', '83.33%', NX)]
    for i, (a, b, c, st) in enumerate(tiles):
        o.append(boxt(20 + i * 350, y + 92, 330, 70, [a, b, c], PANEL, st, 13, True, fills=[INK, MUT, st]))
    o.append(T(20, y + 190, 'Effectiveness divides by all 24 defects, not just the 20 the review found.', 13, 'start', MUT))
    return y + 204, ''.join(o)
FIG[7] = (f7, 'The review moved at 200 lines an hour, the top of the normal band. Of the module\'s 24 defects the inspection caught 20 and testing 4, so density is 24 ÷ 4 KLOC = 6 per KLOC and review effectiveness is 20 ÷ 24 = 83.33%.',
          'A scale of lines per hour with a green band from 100 to 200 and a marker at 200. Below, 24 defect cells, 20 found by inspection and 4 by testing, and two tiles: density 6 per KLOC and effectiveness 83.33 percent.')


# ---- 6.8 re-engineering payback ----
def f8():
    X0, X1, Y0, Y1 = 90, 560, 50, 330
    fx = lambda t: X0 + t / 2 * (X1 - X0)
    fy = lambda v: Y1 - v / 8000 * (Y1 - Y0)
    o = [axes(X0, X1, Y0, Y1, [0, 0.5, 1, 1.5, 2], [0, 2000, 4000, 6000, 8000], fx, fy, 'years', 'cumulative hours', lambda v: f'{v:g}', lambda v: f'{v:,}')]
    o.append(P([(fx(0), fy(0)), (fx(2), fy(8000))], LV, 3))
    o.append(P([(fx(0), fy(3000)), (fx(2), fy(4600))], AC, 3))
    o.append(C(fx(0), fy(3000), 5, AC))
    tc = 0.9375
    o.append(L(fx(tc), fy(3750), fx(tc), Y1, NX, 2, '4 3')); o.append(C(fx(tc), fy(3750), 6.5, NX))
    o.append(Tb(fx(tc) + 10, fy(1400), 'payback 0.9375 years', 13, 'start', NX, True))
    o.append(Tb(fx(tc) + 10, fy(1400) + 18, '= 11.25 months', 13, 'start', NX, True))
    X = 580
    o.append(T(X, 70, 'keep patching', 14, 'start', LV, True)); o.append(T(X, 90, '500 × 8 =', 13, 'start')); o.append(T(X, 108, '4,000 h a year', 13, 'start'))
    o.append(T(X, 160, 're-engineer', 14, 'start', AC, True)); o.append(T(X, 180, '3,000 h once,', 13, 'start')); o.append(T(X, 198, 'then 100 × 8 =', 13, 'start')); o.append(T(X, 216, '800 h a year', 13, 'start'))
    o.append(T(X, 262, 'saving', 14, 'start', bold=True)); o.append(T(X, 282, '4,000 − 800 =', 13, 'start')); o.append(T(X, 300, '3,200 h a year', 13, 'start', bold=True))
    o.append(T(20, Y1 + 76, 'Payback = 3,000 ÷ 3,200 = 0.9375 years: the lines cross just before the end of year 1.', 14, 'start', bold=True))
    return Y1 + 90, ''.join(o)
FIG[8] = (f8, 'Patching the payroll system costs 4,000 hours a year; re-engineering costs 3,000 hours once and then 800 a year. The 3,200 hours saved each year repay the 3,000 in 0.9375 years, about 11.25 months, where the lines cross.',
          'Two lines of cumulative hours over two years: patching rises 4,000 a year from zero; re-engineering starts at 3,000 and rises 800 a year. They cross at 0.9375 years.')


# ---- 6.9 semantic versioning ----
def f9():
    o = []
    x0 = 190
    cw = 90
    for j, h in enumerate(['MAJOR', 'MINOR', 'PATCH']):
        o.append(T(x0 + j * (cw + 10) + cw / 2, 26, h, 14, fill=MUT, bold=True))
    rows = [('current release', (2, 4, 1), None, ''), ('compatible feature', (2, 5, 0), 1, 'MINOR + 1, PATCH reset'),
            ('compatible bug fix', (2, 5, 1), 2, 'PATCH + 1'), ('breaking API change', (3, 0, 0), 0, 'MAJOR + 1, both reset')]
    y = 38
    for name, v, bump, note in rows:
        o.append(T(x0 - 14, y + 30, name, 14, 'end', bold=True))
        for j in range(3):
            x = x0 + j * (cw + 10)
            if bump is None: f, st, fc = PANEL, L2, INK
            elif j == bump: f, st, fc = ACS, AC, AC
            elif j > bump: f, st, fc = FIGBG, L2, MUT
            else: f, st, fc = PANEL, L2, INK
            o.append(R(x, y, cw, 46, f, st, 6, 2.5 if j == bump else 1.5, '5 4' if (bump is not None and j > bump) else None))
            o.append(T(x + cw / 2, y + 31, str(v[j]), 20, fill=fc, bold=True))
        if note: o.append(T(x0 + 3 * (cw + 10) + 4, y + 22, note, 13, 'start', MUT))
        o.append(T(x0 + 3 * (cw + 10) + 4, y + 40, '.'.join(map(str, v)), 14, 'start', AC if bump is not None else INK, True))
        if bump is not None:
            o.append(L(x0 - 120, y - 20, x0 - 120, y - 2, L2, 1.5, arrow='m'))
        y += 66
    o.append(R(x0, y + 4, 16, 14, ACS, AC, 3)); o.append(T(x0 + 22, y + 16, 'the field that changes', 13, 'start'))
    o.append(R(x0 + 200, y + 4, 16, 14, FIGBG, L2, 3, 1.5, '4 3')); o.append(T(x0 + 222, y + 16, 'reset to 0', 13, 'start'))
    return y + 30, ''.join(o)
FIG[9] = (f9, 'Each release bumps exactly one field and resets the fields to its right to 0: a compatible feature gives 2.5.0, a compatible fix 2.5.1, and a breaking API change 3.0.0.',
          'Four rows of MAJOR, MINOR and PATCH cells: 2.4.1, then 2.5.0 with MINOR highlighted and PATCH reset, then 2.5.1 with PATCH highlighted, then 3.0.0 with MAJOR highlighted and the other two reset.')


TEXT = {
    8: [('The figure adds the starting legacy system and the resulting new system, so it shows five boxes but only three re-engineering steps.',
         'A diagram of this process that adds the starting legacy system and the resulting new system shows five boxes but only three re-engineering steps.')],
    9: [('The gate is shown in the figure: freeze, candidate, sign-off, production, monitor, and a dashed failure path to rollback.',
         'The gate runs in order: freeze, candidate, sign-off, production and monitor, with a failure path back to rollback.')],
}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d


def text_fixes(k):
    return TEXT.get(k, [])
