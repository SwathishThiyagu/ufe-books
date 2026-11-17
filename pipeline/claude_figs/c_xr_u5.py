"""Claude's hand-drawn figures for c-xr-u5 (AR/VR, unit 5: 3D interaction and VR development), one per chapter, from
each chapter's worked example, plus the sentences in the chapter text that describe a figure (text_fixes)."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {}


# ---- 5.1 ray selection test ----
def f1():
    s = 250
    ox, oy = 70, 130
    Z = lambda z: ox + (-z) * s     # depth -z to the right
    X = lambda x: oy - x * s        # x upward
    o = [T(40, 28, 'Seen from above: the ray runs along −z from the controller', 15, 'start', bold=True)]
    o.append(L(Z(0), X(0), Z(-2.5), X(0), AC, 3, arrow='n')); o.append(T(Z(-2.5), X(0) + 22, 'ray, u = (0, 0, −1)', 13, 'end', AC, True))
    o.append(R(Z(0) - 26, X(0) - 10, 26, 20, ACS, AC, 4)); o.append(T(Z(0) - 4, X(0) + 34, 'p = (0, 0, 0)', 13, 'start'))
    o.append(f'<circle cx="{Z(-2):.1f}" cy="{X(0.1):.1f}" r="{0.15 * s:.1f}" style="fill:var(--live-soft);stroke:var(--live);stroke-width:2.5"/>')
    o.append(C(Z(-2), X(0.1), 5, INK)); o.append(T(Z(-2) - 46, X(0.1) - 26, 'centre c = (0.10, 0, −2.00)', 13, 'end', INK, True))
    o.append(T(Z(-2) - 46, X(0.1) - 8, 'radius R = 0.15 m', 13, 'end'))
    o.append(C(Z(-2), X(0), 6, NX)); o.append(T(Z(-2) - 10, X(0) + 24, 'q, closest point', 13, 'end', NX, True))
    o.append(L(Z(-2), X(0), Z(-2), X(0.1) + 4, NX, 2.5))
    o.append(T(Z(-2) + 8, X(0.05) + 4, 'd', 14, 'start', NX, True))
    o.append(brace(Z(0), Z(-2), X(0) + 54, INK)); o.append(T(Z(-1), X(0) + 76, 't = (c − p)·u = 2.00 m along the ray', 14))
    o += [T(40, 260, 'q = p + t u = (0, 0, −2.00);  c − q = (0.10, 0, 0);  d = 0.10 m', 14, 'start'),
          T(40, 284, 'd = 0.10 m is less than R = 0.15 m, so the ray passes through the sphere and selects it.', 14, 'start', bold=True)]
    return 302, ''.join(o)
FIG[1] = (f1, 'The ray leaves the controller along −z. The sphere centre is 2.00 m along it (t) and 0.10 m to the side (d). Because d is smaller than the 0.15 m radius, the ray hits the sphere and selects it.',
          'A top view of a ray going right from a controller, a circle of radius 0.15 m whose centre sits 0.10 m above the ray at 2 m, and the short perpendicular d from the closest point q to the centre.')


# ---- 5.2 route versus straight line ----
def f2():
    s = 60
    ox, oy = 90, 320
    X = lambda x: ox + x * s
    Y = lambda y: oy - y * s
    o = [T(40, 28, 'The walk on the campus map (metres)', 15, 'start', bold=True)]
    for x in range(0, 5):
        o.append(L(X(x), Y(0), X(x), Y(4.5), LN, 1)); o.append(T(X(x), Y(0) + 20, str(x), 13, fill=MUT))
    for y in range(0, 5):
        o.append(L(X(0), Y(y), X(4.5), Y(y), LN, 1)); o.append(T(X(0) - 10, Y(y) + 4, str(y), 13, 'end', MUT))
    o.append(L(X(0), Y(0), X(3) - 4, Y(0), AC, 4, arrow='n')); o.append(Tb(X(1.5), Y(0) - 12, '3 m east', 14, 'middle', AC, True))
    o.append(L(X(3), Y(0), X(3), Y(4) + 4, AC, 4, arrow='n')); o.append(Tb(X(3) + 10, Y(2), '4 m north', 14, 'start', AC, True))
    o.append(L(X(0), Y(0), X(3), Y(4), NX, 3, '8 6')); o.append(Tb(X(1.875) - 14, Y(2.5) + 5, '5 m straight', 14, 'end', NX, True))
    for (x, y, lab) in [(0, 0, 'Start (0, 0)'), (3, 0, 'East (3, 0)'), (3, 4, 'Final (3, 4)')]:
        o.append(C(X(x), Y(y), 8, INK))
    o.append(T(X(0) + 8, Y(0) + 40, 'Start (0, 0)', 13, 'start', INK, True)); o.append(T(X(3) + 10, Y(0) + 40, 'East (3, 0)', 13, 'start', INK, True))
    o.append(T(X(3) + 14, Y(4) - 6, 'Final (3, 4)', 13, 'start', INK, True))
    tx = 420
    o += [T(tx, 110, 'route = 3 + 4 = 7 m', 15, 'start', AC, True),
          T(tx, 146, 'straight = √(3² + 4²)', 14, 'start', NX), T(tx, 170, '= √25 = 5 m', 15, 'start', NX, True),
          T(tx, 214, 'route is 2 m longer;', 14, 'start'), T(tx, 238, '7 ÷ 5 = 1.4 times', 14, 'start'),
          T(tx, 282, 'a map shows the 5 m line,', 13, 'start', MUT), T(tx, 300, 'the walls force the 7 m route', 13, 'start', MUT)]
    return 380, ''.join(o)
FIG[2] = (f2, 'The walk goes 3 m east and then 4 m north, a 7 m route. The dashed line is the straight-line distance from start to finish, √(3² + 4²) = 5 m, which is 2 m shorter.',
          'A map grid with a solid path from Start at (0, 0) east to (3, 0) and north to Final at (3, 4), and a dashed straight line of 5 m from Start to Final.')


# ---- 5.3 weighting success by command counts ----
def f3():
    x0, x1 = 150, 690
    s = (x1 - x0) / 100
    X = lambda v: x0 + v * s
    o = [T(40, 28, '100 commands, split by channel; filled part = succeeded', 15, 'start', bold=True)]
    chans = [('voice', 70, 63, '70 × 0.90 = 63'), ('gesture', 20, 16, '20 × 0.80 = 16'), ('menu', 10, 10, '10 × 1.00 = 10')]
    y = 56
    a = 0
    for name, n, ok, how in chans:
        o.append(T(x0 - 12, y + 24, name, 14, 'end', bold=True))
        o.append(R(X(a), y, n * s, 36, 'var(--line)', L2, 3))
        o.append(R(X(a), y, ok * s, 36, ACS, AC, 3))
        o.append(T(X(a) + ok * s / 2 if ok >= 30 else X(a) + 4, y + 24, how if ok >= 30 else str(ok), 13, 'middle' if ok >= 30 else 'start', INK, ok >= 30))
        if ok < 30:
            o.append(T(X(a) - 8, y + 24, how, 13, 'end', INK, True))
        a += n
        y += 50
    o.append(L(X(0), y + 6, X(100), y + 6, INK, 1.5))
    o.append(T(x0 - 12, y + 32, 'total', 14, 'end', bold=True))
    o.append(R(X(0), y + 14, 100 * s, 30, 'var(--line)', L2, 3)); o.append(R(X(0), y + 14, 89 * s, 30, NXS, NX, 3))
    o.append(T(X(44.5), y + 34, '63 + 16 + 10 = 89 of 100 → 89%', 14, 'middle', INK, True))
    o.append(T(40, y + 82, 'Not (90% + 80% + 100%) ÷ 3 = 90%: voice carries 70 of the 100 commands, so its rate counts most.', 14, 'start', NX))
    return y + 100, ''.join(o)
FIG[3] = (f3, 'Each channel\'s successes are its command count times its own rate: 63 of 70 voice, 16 of 20 gesture, 10 of 10 menu. Together that is 89 of 100, so the app succeeds 89% of the time, not the plain average of 90%.',
          'Three bars of 70, 20 and 10 commands with their successful parts filled, 63, 16 and 10, and a total bar of 89 out of 100.')


# ---- 5.4 frames add down the tree ----
def f4():
    o = [T(40, 28, 'Scene graph', 15, 'start', bold=True)]
    o.append(boxt(110, 46, 110, 40, ['S (root)'], PANEL, AC, 13))
    o.append(boxt(40, 120, 110, 40, ['T: +2 m on x'], ACS, AC, 13))
    o.append(boxt(180, 120, 110, 40, ['Camera'], PANEL, L2, 13))
    o.append(boxt(40, 194, 110, 40, ['M: +3 m on x'], ACS, AC, 13))
    o.append(boxt(40, 268, 110, 40, ['P: local x = 1'], NXS, NX, 13))
    o.append(L(150, 88, 100, 116, AC, 2, arrow='n')); o.append(L(180, 88, 230, 116, L2, 2, arrow='m'))
    o.append(L(95, 162, 95, 190, AC, 2, arrow='n')); o.append(L(95, 236, 95, 264, AC, 2, arrow='n'))
    # world x line
    x0, s, y = 340, 52, 230
    X = lambda v: x0 + v * s
    o.append(T(340, 28, 'Where each origin lands on world x', 15, 'start', bold=True))
    o.append(L(X(0) - 10, y, X(6.6), y, L2, 2, arrow='m'))
    for v in range(0, 7):
        o.append(L(X(v), y, X(v), y + 6, L2, 1.5)); o.append(T(X(v), y + 24, str(v), 13, fill=MUT))
    hops = [(0, 2, '+2 (T)', AC, 150), (2, 5, '+3 (M)', AC, 120), (5, 6, '+1 (P)', NX, 90)]
    for a, b, lab, c, hy in hops:
        o.append(arc(X(a), y - 4, X(b), y - 4, 0.35 if b - a > 1 else 0.6, c, 2.5, 'n' if c == AC else 'x'))
        o.append(T((X(a) + X(b)) / 2, y - (b - a) * s * 0.36 - 16 if b - a > 1 else y - 46, lab, 13, 'middle', c, True))
    for v, lab in [(0, 'S'), (2, 'T'), (5, 'M')]:
        o.append(C(X(v), y, 6, AC)); o.append(T(X(v), y + 46, lab, 13, 'middle', AC, True))
    o.append(C(X(6), y, 7, NX)); o.append(T(X(6), y + 46, 'P', 13, 'middle', NX, True))
    o.append(T(340, 320, 'p_world = T_T × T_M × p_local: 2 + 3 + 1 = 6 m', 14, 'start', bold=True))
    o.append(T(340, 344, 'Camera hangs off S, so moving T does not move it.', 13, 'start', MUT))
    return 360, ''.join(o)
FIG[4] = (f4, 'Going down the tree, each frame starts where its parent\'s frame put it: T\'s origin at x = 2 m, M\'s at 5 m, and the point P at 6 m. The camera is a child of the root, so it does not move with T.',
          'A tree with root S, children T and Camera, T\'s child M and M\'s point P; beside it a world x axis with hops of 2, 3 and 1 metres landing P at 6.')


# ---- 5.5 batching cubes into draw calls ----
def f5():
    o = [T(40, 28, '60 cubes, 3 materials of 20; one batch holds at most 15 cubes', 15, 'start', bold=True)]
    cols = [(ACS, AC, 'material 1'), (LVS, LV, 'material 2'), (NXS, NX, 'material 3')]
    x0, cw = 140, 24
    for r, (fi, st, lab) in enumerate(cols):
        y = 60 + r * 74
        o.append(T(x0 - 12, y + 18, lab, 14, 'end', bold=True))
        for i in range(20):
            gx = x0 + i * cw + (14 if i >= 15 else 0)
            o.append(R(gx, y, cw - 4, 22, fi, st, 3, 1.5))
        o.append(brace(x0, x0 + 15 * cw - 4, y + 30, st))
        o.append(T(x0 + 7.5 * cw, y + 50, 'draw call', 13, 'middle', st, True))
        o.append(brace(x0 + 15 * cw + 14, x0 + 20 * cw + 10, y + 30, st))
        o.append(T(x0 + 17.5 * cw + 12, y + 50, 'draw call', 13, 'middle', st, True))
    o.append(T(40, 300, 'Batched: ceil(20 ÷ 15) = 2 per material → 3 × 2 = 6 draw calls', 14, 'start', bold=True))
    o.append(T(40, 324, 'Unbatched: one per cube → 60 draw calls', 14, 'start', NX))
    o.append(T(40, 348, 'Cubes of different materials cannot share a batch.', 13, 'start', MUT))
    return 364, ''.join(o)
FIG[5] = (f5, 'Each material\'s 20 cubes fill one batch of 15 and a second of 5, so the three materials need 6 draw calls. Without batching every cube is its own draw call, 60 in all.',
          'Three rows of 20 small squares, one row per material, each row bracketed into a group of 15 and a group of 5, each group labelled draw call.')


# ---- 5.6 impulse on the cube ----
def f6():
    o = [T(40, 28, 'From button press to a moving cube', 15, 'start', bold=True)]
    steps = [('Update', 'Fire1 down → fire = true'), ('FixedUpdate', 'AddForce 1.6 N·s, Impulse'), ('Physics', 'v = J ÷ m'), ('Display', 'cube drawn moving')]
    for i, (a, b) in enumerate(steps):
        x = 30 + i * 172
        o.append(boxt(x, 48, 156, 52, [a, b], ACS if i == 1 else PANEL, AC, 13, bold_first=True))
        if i < 3: o.append(L(x + 158, 74, x + 170, 74, AC, 2, arrow='n'))
    fy = 250
    sc = 420
    x0 = 100
    o.append(L(40, fy, 690, fy, INK, 2))
    for i in range(0, 13):
        o.append(L(40 + i * 54, fy, 30 + i * 54, fy + 10, L2, 1.2))
    o.append(R(x0 - 40, fy - 40, 40, 40, ACS, AC, 4)); o.append(T(x0 - 20, fy - 14, '0.8 kg', 12))
    o.append(R(x0 + 1.0 * sc - 40, fy - 40, 40, 40, ACS, AC, 4, 2, '5 3'))
    o.append(L(x0 + 4, fy - 20, x0 + 90, fy - 20, NX, 3, arrow='x')); o.append(T(x0 + 96, fy - 15, 'v = 1.6 ÷ 0.8 = 2.0 m/s', 14, 'start', NX, True))
    o.append(brace(x0 - 20, x0 + 1.0 * sc - 20, fy + 30, INK))
    o.append(T(x0 - 20 + 0.5 * sc, fy + 52, 's = v t = 2.0 × 0.5 = 1.0 m in 0.5 s (no friction)', 14))
    o.append(T(x0 - 20, fy - 54, 't = 0', 13, 'middle', MUT)); o.append(T(x0 + 1.0 * sc - 20, fy - 54, 't = 0.5 s', 13, 'middle', MUT))
    o.append(T(40, 346, 'Impulse J = m Δv, so from rest Δv = J ÷ m. The force is applied once, in physics time.', 14, 'start'))
    return 362, ''.join(o)
FIG[6] = (f6, 'The button press sets a flag in Update; FixedUpdate applies the 1.6 N·s impulse once. The 0.8 kg cube leaves at 2.0 m/s and, with no friction, slides 1.0 m in the next 0.5 s.',
          'Four boxes, Update, FixedUpdate, Physics and Display, in a row; below, a cube on a floor shown at the start and 1.0 m further on after 0.5 s, with a speed arrow of 2.0 m/s.')


# ---- 5.7 latency budget and session plan ----
def f7():
    x0, x1 = 140, 640
    s = (x1 - x0) / 22
    X = lambda v: x0 + v * s
    o = [T(40, 28, 'Motion-to-photon latency adds up stage by stage', 15, 'start', bold=True)]
    parts = [(0, 3, 'sensor 3', PANEL, L2), (3, 9, 'simulation 6', ACS, AC), (9, 18, 'render 9', ACS, AC), (18, 20, '2', LVS, LV)]
    y = 64
    o.append(T(x0 - 12, y + 26, 'one frame', 14, 'end', bold=True))
    for a, b, lab, fi, st in parts:
        o.append(R(X(a), y, (b - a) * s, 40, fi, st, 3)); o.append(T(X((a + b) / 2), y + 26, lab, 13))
    o.append(T(X(19), y - 8, 'display', 13, 'middle', LV))
    o.append(L(X(20), y - 20, X(20), y + 58, NX, 2.5, '5 4')); o.append(T(X(20) + 6, y - 8, 'target 20 ms', 13, 'start', NX, True))
    o.append(xaxis(x0, x1, y + 62, [0, 3, 9, 18, 20], X, 'running total (ms)'))
    o.append(T(40, 206, '3 + 6 + 9 + 2 = 20 ms: meets a "20 ms or less" target exactly, with no margin.', 14, 'start', bold=True))
    # session plan
    s2 = (x1 - x0) / 45
    X2 = lambda v: x0 + v * s2
    o.append(T(40, 248, 'A first 45-minute session', 15, 'start', bold=True))
    plan = [(0, 5, 'setup', PANEL, L2), (5, 20, 'VR 15 min', ACS, AC), (20, 25, 'break', LVS, LV), (25, 40, 'VR 15 min', ACS, AC), (40, 45, 'rest', LVS, LV)]
    for a, b, lab, fi, st in plan:
        o.append(R(X2(a), 264, (b - a) * s2, 36, fi, st, 3)); o.append(T(X2((a + b) / 2), 287, lab, 13))
    o.append(xaxis(x0, x1, 304, [0, 5, 20, 25, 40, 45], X2, 'minutes'))
    return 370, ''.join(o)
FIG[7] = (f7, 'The four delays add to 3 + 6 + 9 + 2 = 20 ms, landing exactly on the 20 ms target with nothing to spare. Below, the safe first session from the chapter: 30 minutes of VR inside 45 minutes.',
          'A bar of sensor 3, simulation 6, render 9 and display 2 milliseconds ending exactly on a dashed 20 ms target line; below, a 45 minute bar of setup, two 15 minute VR blocks, a break and rest.')


# ---- 5.8 A/B comparison with denominators ----
def f8():
    x0, y1 = 120, 300
    sc = 2.2  # px per percent
    o = [T(40, 28, 'Menu A against menu B', 15, 'start', bold=True)]
    o.append(L(x0 - 10, y1, 690, y1, L2, 1.5))
    groups = [(140, 'completion rate (of 20 users)', [('A', 80, '16 of 20 = 80%'), ('B', 90, '18 of 20 = 90%')], AC, ACS),
              (440, 'error rate (of 40 attempts)', [('A', 15, '6 of 40 = 15%'), ('B', 7.5, '3 of 40 = 7.5%')], NX, NXS)]
    for gx, title, bars, st, fi in groups:
        for i, (lab, v, txt) in enumerate(bars):
            bx = gx + i * 120
            o.append(R(bx, y1 - v * sc, 90, v * sc, fi, st, 3))
            o.append(T(bx + 45, y1 - v * sc - 10, txt, 13, 'middle', INK, True))
            o.append(T(bx + 45, y1 + 22, f'design {lab}', 14, 'middle', INK, lab == 'B'))
        o.append(T(gx + 105, y1 + 50, title, 14, 'middle', st, True))
    o.append(T(40, 382, 'B is better on both: +10 points completion and 7.5 points fewer errors.', 14, 'start', bold=True))
    o.append(T(40, 404, 'Completion counts users, errors count attempts; always give the denominator.', 13, 'start', MUT))
    return 420, ''.join(o)
FIG[8] = (f8, 'Design B wins on both measures: 90% completion against 80%, and 7.5% errors against 15%. Completion is out of 20 users and errors out of 40 attempts, so each rate keeps its own denominator.',
          'Two pairs of bars: completion 80 percent for A and 90 percent for B out of 20 users, and error rate 15 percent for A and 7.5 percent for B out of 40 attempts.')


TEXT = {
    4: [('Only a few universities teach X3D in detail; most teach the same tree idea through an engine.',
         'Most courses teach the same tree idea through an engine rather than through X3D.')],
}


def chapter_fix(k, ch):
    # chapter 5 links to scene graphs with an anchor that does not exist; point it at chapter 5.4's real id
    if k == 5:
        import json
        ch = json.loads(json.dumps(ch, ensure_ascii=False).replace('#chapter-5-4', '#vr-toolkits-and-scene-graphs'))
    return ch


def text_fixes(k):
    return TEXT.get(k, [])


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d
