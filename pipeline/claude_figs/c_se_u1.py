"""Claude's hand-drawn figures for c-se-u1 (Software Engineering, unit 1: software and process models), one per chapter,
from each chapter's worked example, plus the sentences in the chapter text that describe a figure (text_fixes)."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {}


def tile(x, y, s, fill, stroke):
    return R(x, y, s, s, fill, stroke, 3, 1.5)


def kgraph(cx, cy, r, n, c=AC, nc=AC):
    pts = [(cx + r * math.cos(-math.pi / 2 + 2 * math.pi * i / n), cy + r * math.sin(-math.pi / 2 + 2 * math.pi * i / n)) for i in range(n)]
    o = []
    for i in range(n):
        for j in range(i + 1, n):
            o.append(L(*pts[i], *pts[j], c, 1.4))
    for x, y in pts:
        o.append(C(x, y, 7, nc))
    return ''.join(o)


# ---- 1.1 classify 40 applications; paths grow from 10 to 28 ----
def f1():
    o = [T(20, 26, 'The firm\'s 40 applications, one square each', 15, 'start', bold=True)]
    groups = [(25, ACS, AC), (2, LVS, LV), (8, NXS, NX), (5, PANEL, L2)]
    s, g, x0, y0 = 26, 6, 20, 44
    i = 0
    for n, f, st in groups:
        for _ in range(n):
            col, row = i % 20, i // 20
            o.append(tile(x0 + col * (s + g), y0 + row * (s + g), s, f, st))
            i += 1
    # legend rows
    ly = 130
    o += [R(20, ly - 13, 18, 16, ACS, AC, 3), T(46, ly, '25 web apps', 14, 'start'),
          R(20, ly + 13, 18, 16, LVS, LV, 3), T(46, ly + 26, '2 payroll systems, 12 years old: legacy', 14, 'start', LV, True)]
    o.append(brace(20, 20 + 16 * 0 + 380, ly + 48, AC))
    o.append(T(46, ly + 72, 'application software: 25 + 2 = 27', 14, 'start', AC, True))
    o += [R(400, ly - 13, 18, 16, NXS, NX, 3), T(426, ly, '8 meter firmware: embedded', 14, 'start'),
          R(400, ly + 13, 18, 16, PANEL, L2, 3), T(426, ly + 26, '5 payment libraries: reuse', 14, 'start')]
    o.append(T(426, ly + 72, '27 + 8 + 5 = 40', 14, 'start', bold=True))
    # paths
    y1 = 250
    o.append(L(20, y1 - 14, 700, y1 - 14, LN, 1))
    o.append(T(20, y1 + 12, 'The payroll team: every pair of people is one communication path', 15, 'start', bold=True))
    o.append(kgraph(180, y1 + 120, 70, 5))
    o.append(kgraph(520, y1 + 120, 80, 8, LV, LV))
    o.append(T(180, y1 + 232, 'n = 5: 5 × 4 ÷ 2 = 10 paths', 14, bold=True))
    o.append(T(520, y1 + 232, 'n = 8: 8 × 7 ÷ 2 = 28 paths', 14, fill=LV, bold=True))
    o.append(L(282, y1 + 120, 410, y1 + 120, L2, 2, arrow='m'))
    o.append(Tb(346, y1 + 112, 'add 3', 14, bold=True))
    o.append(T(360, y1 + 264, '18 more paths to keep in sync, so the late project gets later, not faster.', 14, fill=MUT))
    return y1 + 280, ''.join(o)
FIG[1] = (f1, 'The 40 applications sort into 27 application software (2 of them legacy payroll), 8 embedded and 5 reuse. Adding 3 people to the 5-person payroll team raises the communication paths from 10 to 28.',
          'Forty squares coloured by domain: 25 web apps and 2 legacy payroll systems make 27 application software, 8 embedded, 5 reuse. Below, a 5-node graph with 10 links next to an 8-node graph with 28 links.')
AFTER[1] = 2


# ---- 1.2 layered technology stack ----
def f2():
    x0, w = 90, 540
    o = []
    rows = [  # top to bottom
        ('Tools', 'what the team uses', 'tools'),
        ('Methods', '1 code-review checklist', None),
        ('Process', '1 sprint process: still 1', 'weak'),
        ('Quality focus', '2 defects/KLOC × 25 KLOC = 50 defects allowed', None),
    ]
    y, hgt = 30, 70
    for name, txt, kind in rows:
        fill, st = (LVS, LV) if kind == 'weak' else ((NXS, NX) if name == 'Quality focus' else (PANEL, AC))
        o.append(R(x0, y, w, hgt, fill, st, 6, 2.5 if kind == 'weak' else 2))
        o.append(T(x0 + 16, y + 26, name, 15, 'start', st if kind == 'weak' else INK, True))
        if kind == 'tools':
            for i in range(7):
                cx = x0 + 160 + i * 52
                new = i >= 2
                o.append(R(cx, y + 34, 44, 26, ACS if not new else PANEL, AC, 5, 1.6, '5 4' if new else None))
                o.append(T(cx + 22, y + 52, ['Git', 'Jira'][i] if i < 2 else 'new', 13, fill=INK if not new else MUT))
            o.append(T(x0 + 160, y + 26, '2 + 5 bought = 7 tools', 14, 'start', AC, True))
        else:
            o.append(T(x0 + 16, y + 52, txt, 14, 'start', LV if kind == 'weak' else INK, kind == 'weak'))
        y += hgt + 8
    o.append(L(x0 - 34, 30 + 4 * 78 - 12, x0 - 34, 40, L2, 2, arrow='m'))
    o.append(T(x0 - 44, 30 + 4 * 78 - 14, 'base', 13, 'end', MUT))
    o.append(T(x0 - 44, 52, 'top', 13, 'end', MUT))
    o.append(T(360, 30 + 4 * 78 + 18, 'Buying tools grows only the top layer; the process layer under them stays weak.', 14, fill=MUT))
    return 30 + 4 * 78 + 34, ''.join(o)
FIG[2] = (f2, 'The team\'s items on the four layers: 7 tools after buying 5, 1 review checklist, 1 sprint process and a quality target of 50 defects. The new tools change only the top layer, so the process layer stays the weak one.',
          'Four stacked layers, bottom to top: quality focus with 50 defects allowed, process with 1 sprint process highlighted as weak, methods with 1 checklist, tools with Git, Jira and 5 new dashed tool boxes.')


# ---- 1.3 life cycle effort split ----
def f3():
    phases = [('Requirements', 30, '15%'), ('Design', 40, '20%'), ('Construction', 80, '40%'), ('Testing', 40, '20%'), ('Deploy', 10, '5%')]
    x0, W = 20, 680
    s = W / 200
    y = 60
    o = [T(20, 30, 'Fee portal: 200 person-days split across the phases', 15, 'start', bold=True)]
    x = x0
    centers = []
    for i, (name, v, pc) in enumerate(phases):
        w = v * s
        big = name == 'Construction'
        o.append(R(x, y, w, 62, ACS if big else PANEL, AC, 4, 2.5 if big else 2))
        if v >= 30:
            o.append(T(x + w / 2, y + 27, name, 14 if v > 30 else 13, bold=True))
            o.append(T(x + w / 2, y + 48, f'{pc} → {v}', 13, fill=MUT))
        else:
            o.append(T(x + w / 2, y + 37, str(v), 14, bold=True))
        centers.append(x + w / 2)
        x += w
    o.append(T(x0 + W, y + 82, 'Deploy 5% → 10', 13, 'end', MUT))
    o.append(T(360, y + 112, '30 + 40 + 80 + 40 + 10 = 200 person-days', 14, bold=True))
    # after go-live: change loop
    yb = y + 150
    o.append(T(20, yb, 'After go-live a new fee rule arrives', 15, 'start', bold=True))
    boxes = [('new fee rule', LVS, LV), ('requirements', PANEL, AC), ('design', PANEL, AC), ('construction', PANEL, AC), ('testing', PANEL, AC), ('deploy', PANEL, AC)]
    bw, gap, by = 98, 18, yb + 22
    for i, (lab, f, st) in enumerate(boxes):
        bx = 20 + i * (bw + gap)
        o.append(boxt(bx, by, bw, 46, [lab], f, st, 14))
        if i:
            o.append(L(bx - gap, by + 23, bx - 2, by + 23, LV if i == 1 else AC, 2, arrow='l' if i == 1 else 'n'))
    o.append(T(20 + bw + gap + bw / 2, by + 72, 'starts here first', 14, fill=LV, bold=True))
    o.append(T(360, by + 100, 'The rule changes what the system must do, so maintenance re-enters the cycle at requirements.', 14, fill=MUT))
    return by + 116, ''.join(o)
FIG[3] = (f3, 'The 200 person-days of the fee portal split 30, 40, 80, 40 and 10, so construction takes the largest share. A new fee rule after go-live goes back to requirements first, then through the later phases again.',
          'A long bar divided into requirements 30, design 40, construction 80, testing 40 and deploy 10 person-days. Below, a row of boxes: new fee rule, then requirements, design, construction, testing, deploy.')


# ---- 1.4 framework activities with task counts and umbrella band ----
def f4():
    acts = [('communication', 6), ('planning', 5), ('modeling', 8), ('construction', 12), ('deployment', 4)]
    cw, gap, x0 = 124, 15, 20
    base = 200
    s = 16
    o = [T(20, 26, 'One release: tasks in each framework activity', 15, 'start', bold=True)]
    for i, (name, n) in enumerate(acts):
        x = x0 + i * (cw + gap)
        big = name == 'construction'
        o.append(R(x, 44, cw, base - 44 + 6, ACS if big else PANEL, AC, 6, 2.5 if big else 2))
        o.append(T(x + cw / 2, 66, name, 14, bold=True))
        o.append(T(x + cw / 2, 88, f'{n} tasks', 14, fill=AC if big else MUT, bold=big))
        for t in range(n):
            col, row = t % 4, t // 4
            o.append(R(x + 14 + col * 25, base - 22 - row * 22, 20, 16, PANEL if not big else FIGBG, AC, 3, 1.4))
    o.append(T(360, base + 30, 'framework tasks: 6 + 5 + 8 + 12 + 4 = 35', 14, bold=True))
    # umbrella band
    uy = base + 50
    o.append(R(x0, uy, 5 * cw + 4 * gap, 50, NXS, NX, 6))
    o.append(T(x0 + 14, uy + 21, 'umbrella activities run across all five, not as a sixth step', 14, 'start', NX, True))
    o.append(T(x0 + 14, uy + 40, '3 tasks: risk review, QA audit, configuration baseline', 14, 'start'))
    o.append(T(20, uy + 82, 'whole task set = 35 + 3 = 38', 14, 'start', bold=True))
    o.append(T(20, uy + 106, 'construction share = 12 ÷ 38 = 31.6%', 14, 'start', AC, True))
    o.append(T(380, uy + 106, '(12 ÷ 35 = 34.3% wrongly drops the umbrella)', 13, 'start', MUT))
    return uy + 122, ''.join(o)
FIG[4] = (f4, 'The five framework activities hold 6, 5, 8, 12 and 4 tasks, 35 in all, and the umbrella band adds 3 more across every activity, giving 38. Construction\'s 12 tasks are 31.6% of the whole task set.',
          'Five columns of small task boxes: communication 6, planning 5, modeling 8, construction 12 (highlighted), deployment 4. A wide band under all of them holds 3 umbrella tasks. Totals 35 plus 3 equals 38; construction share 31.6 percent.')


# ---- 1.5 waterfall vs incremental gantt ----
def f5():
    x0, x1 = 120, 696
    wk = (x1 - x0) / 16
    fx = lambda w: x0 + w * wk
    o = [T(20, 24, 'Payroll: 4 increments, each 3 weeks build + 1 week test', 15, 'start', bold=True)]
    ya, yb = 70, 160
    o.append(T(x0 - 10, ya + 22, 'Plan A', 15, 'end', bold=True)); o.append(T(x0 - 10, ya + 40, 'waterfall', 13, 'end', MUT))
    o.append(T(x0 - 10, yb + 22, 'Plan B', 15, 'end', bold=True)); o.append(T(x0 - 10, yb + 40, 'incremental', 13, 'end', MUT))
    o.append(R(fx(0), ya, fx(12) - fx(0), 44, ACS, AC, 4))
    o.append(T((fx(0) + fx(12)) / 2, ya + 27, 'build all 4 increments: weeks 1–12', 14, bold=True))
    o.append(R(fx(12), ya, fx(16) - fx(12), 44, LVS, LV, 4))
    o.append(T((fx(12) + fx(16)) / 2, ya + 27, 'test 13–16', 14, bold=True))
    for i in range(4):
        b0 = i * 4
        o.append(R(fx(b0), yb, 3 * wk, 44, ACS, AC, 4))
        o.append(T(fx(b0) + 1.5 * wk, yb + 27, f'build {i + 1}', 14, bold=True))
        o.append(R(fx(b0 + 3), yb, wk, 44, LVS, LV, 4))
        o.append(T(fx(b0 + 3.5), yb + 27, 'T', 14, bold=True))
    ay = yb + 74
    o.append(xaxis(x0, x1, ay, [0, 4, 8, 12, 16], fx, 'week'))
    o.append(L(fx(4), yb + 50, fx(4), yb - 26, NX, 2, '5 4'))
    o.append(Tb(fx(4) + 6, yb - 12, 'week 4: first tested module reaches the user', 14, 'start', NX, True))
    o.append(L(fx(16), ya - 12, fx(16), ay, INK, 1.5, '5 4'))
    o.append(T(fx(16) - 4, ya - 18, 'both end week 16', 14, 'end', bold=True))
    o.append(T(360, ay + 70, 'Same 16 weeks of work; only Plan B puts tested software in users\' hands early.', 14, fill=MUT))
    return ay + 84, ''.join(o)
FIG[5] = (f5, 'Waterfall builds for 12 weeks and then tests weeks 13 to 16; incremental builds and tests one slice every 4 weeks. Both finish testing at week 16, but incremental puts the first tested payroll module in users\' hands at week 4.',
          'Two timeline rows over 16 weeks. Plan A: one long build bar for weeks 1 to 12 then a test bar for weeks 13 to 16. Plan B: four repeats of a 3-week build bar and a 1-week test bar, with a marker at week 4.')


# ---- 1.6 sprints to finish the backlog ----
def f6():
    X0, X1, Y0, Y1 = 90, 520, 60, 330
    fy = lambda v: Y1 - v / 36 * (Y1 - Y0)
    bw = 70
    o = [T(20, 24, 'Velocity 10 × 0.80 = 8 points per 2-week sprint', 15, 'start', bold=True)]
    o.append(L(X0, Y1, X1, Y1, L2, 1.5)); o.append(L(X0, Y0, X0, Y1, L2, 1.5))
    for v in (0, 8, 16, 24, 32):
        o += [L(X0 - 5, fy(v), X0, fy(v), L2, 1.5), T(X0 - 9, fy(v) + 4.5, str(v), 13, 'end', MUT)]
    o.append(T(X0 - 60, Y0 - 16, 'points done', 14, 'start', MUT))
    cum = [8, 16, 24, 31]
    for i, c in enumerate(cum):
        x = X0 + 30 + i * (bw + 30)
        last = i == 3
        o.append(R(x, fy(c), bw, Y1 - fy(c), NXS if last else ACS, NX if last else AC, 3))
        o.append(T(x + bw / 2, fy(c) - 8, str(c), 14, bold=True))
        o.append(T(x + bw / 2, Y1 + 20, f'sprint {i + 1}', 13, fill=MUT))
        o.append(T(x + bw / 2, Y1 + 38, f'week {2 * (i + 1)}', 13, fill=MUT))
        if last: o.append(T(x + bw / 2, fy(c) + 22, '+7', 14, fill=NX, bold=True))
    o.append(L(X0, fy(31), X1, fy(31), LV, 2, '7 5'))
    o.append(Tb(X0 + 8, fy(31) - 10, 'backlog 31', 14, 'start', LV, True))
    # backlog list
    bx = 548
    o.append(T(bx, 74, 'backlog', 14, 'start', bold=True))
    items = [('login', 5), ('search', 8), ('report', 3), ('payment', 13), ('help', 2)]
    for i, (n, p) in enumerate(items):
        o.append(T(bx, 100 + i * 22, n, 14, 'start')); o.append(T(700, 100 + i * 22, str(p), 14, 'end'))
    o.append(L(bx, 100 + 5 * 22 - 12, 700, 100 + 5 * 22 - 12, L2, 1.5))
    o.append(T(bx, 100 + 5 * 22 + 6, 'total', 14, 'start', bold=True)); o.append(T(700, 100 + 5 * 22 + 6, '31', 14, 'end', bold=True))
    o.append(T(bx, 268, '31 ÷ 8 = 3.875', 14, 'start'))
    o.append(T(bx, 290, 'round up: 4 sprints', 14, 'start', AC, True))
    o.append(T(bx, 312, '= 8 weeks', 14, 'start', AC, True))
    o.append(T(360, Y1 + 72, 'After 3 sprints only 24 of 31 points are done, so 3 sprints is a promise the team cannot keep.', 14, fill=MUT))
    return Y1 + 88, ''.join(o)
FIG[6] = (f6, 'At 8 points a sprint the team has 8, 16 and 24 points done after three sprints, still short of the 31-point backlog. The fourth sprint delivers the last 7, so the work ends at week 8.',
          'A bar chart of points done after each 2-week sprint: 8, 16, 24 and 31, with a dashed line at the backlog total of 31. A list beside it gives the five stories adding to 31 and the sum 31 divided by 8 rounded up to 4 sprints.')


# ---- 1.7 failure causes grouped by area, active ones lit ----
def f7():
    o = []
    o.append(boxt(250, 18, 220, 44, ['project failure'], LVS, LV, 15, True))
    cols = [
        ('Requirements', 20, [('changing requirements', '30 of 120 changed = 25.0%', True), ('scope creep', None, False), ('unclear requirements', None, False)]),
        ('Management', 253, [('risk neglect', '2 of 8 developers left', True), ('unrealistic deadline', None, False), ('poor estimation', None, False)]),
        ('Engineering', 486, [('inadequate testing', '1 tester for 8 developers', True), ('technical debt', None, False), ('skill gaps', None, False)]),
    ]
    cw = 214
    for name, x, leaves in cols:
        o.append(L(360, 64, x + cw / 2, 96, L2, 2, arrow='m'))
        o.append(boxt(x, 100, cw, 38, [name], PANEL, AC, 15, True))
        y = 152
        for lab, num, on in leaves:
            h = 62 if on else 36
            o.append(R(x, y, cw, h, LVS if on else FIGBG, LV if on else L2, 6, 2.5 if on else 1.5))
            o.append(T(x + cw / 2, y + 23, lab, 14, fill=LV if on else MUT, bold=on))
            if num: o.append(T(x + cw / 2, y + 46, num, 13))
            y += h + 10
    yw = 152 + 62 + 36 * 2 + 30 + 14
    o.append(R(20, yw, 680, 62, NXS, NX, 8))
    o.append(T(36, yw + 25, 'Early warning: testing starts only in month 5 of 6', 14, 'start', NX, True))
    o.append(T(36, yw + 47, 'a 6 − 5 + 1 = 2-month window for one tester and a large untested build', 14, 'start'))
    return yw + 76, ''.join(o)
FIG[7] = (f7, 'Failure causes grouped by area, with the three active in the worked example lit: 25.0% of requirements changed, 2 of 8 developers left with no new plan, and one tester for eight developers. Testing that starts in month 5 of 6 is the early warning.',
          'A tree from project failure to three areas: requirements, management and engineering, each with three causes. Highlighted are changing requirements 25 percent, risk neglect with 2 of 8 developers gone, and inadequate testing with 1 tester for 8 developers. A band below names the early warning.')


TEXT = {}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d


def text_fixes(k):
    return TEXT.get(k, [])


def drop_sources():
    # university-hosted pages: the books name no universities
    return ['sei.cmu.edu', 'ocw.mit.edu']
