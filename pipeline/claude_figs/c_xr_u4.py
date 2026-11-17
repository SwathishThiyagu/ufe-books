"""Claude's hand-drawn figures for c-xr-u4 (AR/VR, unit 4: VR modeling and rendering), one per chapter, from each
chapter's worked example, plus the sentences in the chapter text that describe a figure (text_fixes)."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {}


# ---- 4.1 the wall mesh and its bytes ----
def f1():
    o = [T(40, 28, 'A square wall: 4 shared vertices, 2 triangles', 15, 'start', bold=True)]
    x0, y0, s = 70, 70, 200
    V = {0: (x0, y0 + s), 1: (x0 + s, y0 + s), 2: (x0 + s, y0), 3: (x0, y0)}
    o.append(f'<polygon points="{V[0][0]},{V[0][1]} {V[1][0]},{V[1][1]} {V[2][0]},{V[2][1]}" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2.5"/>')
    o.append(f'<polygon points="{V[0][0]},{V[0][1]} {V[2][0]},{V[2][1]} {V[3][0]},{V[3][1]}" style="fill:var(--live-soft);stroke:var(--live);stroke-width:2.5"/>')
    uv = {0: '(0, 0)', 1: '(1, 0)', 2: '(1, 1)', 3: '(0, 1)'}
    for k, (x, y) in V.items():
        o.append(C(x, y, 8, INK))
        dy = 26 if y > y0 else -14
        o.append(T(x, y + dy, f'v{k}  uv {uv[k]}', 13, 'middle', INK, True))
    o.append(T(x0 + s * 0.7, y0 + s * 0.72, 'tri A', 14, bold=True)); o.append(T(x0 + s * 0.3, y0 + s * 0.35, 'tri B', 14, bold=True))
    o.append(T(x0 + s / 2, y0 + s + 56, 'indices: A = (0, 1, 2), B = (0, 2, 3)', 13, fill=MUT))
    bx, by, bw = 360, 70, 320
    o.append(T(bx, 56, 'bytes stored', 14, 'start', bold=True))
    parts = [('positions', '4 × 3 floats × 4 B', 48, ACS, AC), ('UV pairs', '4 × 2 floats × 4 B', 32, ACS, AC),
             ('indices', '2 × 3 × 2 B (uint16)', 12, LVS, LV), ('diffuse colour', '3 floats × 4 B', 12, NXS, NX)]
    y = by
    for name, how, b, fi, st in parts:
        o.append(boxt(bx, y, bw - 70, 44, [name, how], fi, st, 13))
        o.append(T(bx + bw - 60, y + 28, f'{b} B', 15, 'start', bold=True))
        y += 54
    o.append(L(bx, y + 2, bx + bw, y + 2, INK, 2))
    o.append(T(bx + bw - 60, y + 26, '104 B', 16, 'start', bold=True)); o.append(T(bx, y + 26, 'total 48 + 32 + 12 + 12', 14, 'start'))
    return 360, ''.join(o)
FIG[1] = (f1, 'The wall\'s four corners are stored once, each with a position and a UV pair, and the two triangles list them by index. Positions, UVs, indices and colour add to 104 bytes.',
          'A square split by a diagonal into two triangles, its four corners labelled v0 to v3 with UV coordinates; beside it four boxes of 48, 32, 12 and 12 bytes summing to 104.')


# ---- 4.2 parent turns, child follows ----
def f2():
    o = [T(40, 28, 'Scene graph', 15, 'start', bold=True)]
    o.append(boxt(40, 50, 170, 44, ['World', 'W = I'], PANEL, AC, 13))
    o.append(boxt(40, 130, 170, 44, ['Base', 'L = T(10, 0) · Rz(90°)'], PANEL, AC, 13))
    o.append(boxt(40, 210, 170, 44, ['Arm', 'L = T(2, 0)'], NXS, NX, 13))
    o.append(L(125, 96, 125, 126, AC, 2, arrow='n')); o.append(L(125, 176, 125, 206, AC, 2, arrow='n'))
    o.append(T(40, 290, 'W_arm = W_base · L_arm', 14, 'start', bold=True))
    # world plane, zoomed to x 6..13, y -1..4
    s = 52
    X = lambda x: 300 + (x - 6) * s
    Y = lambda y: 316 - (y + 1) * s
    o.append(T(290, 28, 'World, seen from above (metres)', 15, 'start', bold=True))
    for x in range(6, 14):
        o.append(L(X(x), Y(-1), X(x), Y(4), LN, 1))
        if x % 2 == 0: o.append(T(X(x), Y(-1) + 18, str(x), 13, fill=MUT))
    for y in range(-1, 5):
        o.append(L(X(6), Y(y), X(13), Y(y), LN, 1)); o.append(T(X(6) - 8, Y(y) + 4, str(y).replace('-', '&#8722;'), 13, 'end', MUT))
    o.append(L(X(6), Y(0), X(13.2), Y(0), L2, 2, arrow='m'))
    bx, by = X(10), Y(0)
    o.append(R(bx - 14, by - 14, 28, 28, ACS, AC, 4)); o.append(T(bx + 18, by + 22, 'base (10, 0)', 13, 'start', AC, True))
    o.append(L(bx, by, bx, by - 1.5 * s, AC, 3, arrow='n')); o.append(T(bx - 8, by - 1.2 * s, 'base +x', 13, 'end', AC, True))
    o.append(L(bx, by, bx - 1.5 * s, by, AC, 2, '5 4', arrow='n')); o.append(T(bx - 1.5 * s, by - 10, 'base +y', 13, 'middle', AC))
    o.append(f'<path d="M{bx + 44:.1f},{by:.1f} A44,44 0 0 0 {bx:.1f},{by - 44:.1f}" style="fill:none;stroke:var(--ink);stroke-width:1.5"/>')
    o.append(T(bx + 36, by - 36, '90°', 13, 'start'))
    o.append(C(X(10), Y(2), 9, NX)); o.append(Tb(X(10) + 14, Y(2) + 5, 'arm at (10, 2)', 14, 'start', NX))
    o.append(C(X(12), Y(0), 7, L2)); o.append(T(X(12), Y(0) - 14, 'not (12, 0)', 13, fill=MUT))
    o.append(T(290, 368, 'local (2, 0) turned 90° → (0, 2); plus base (10, 0) → (10, 2)', 14, 'start'))
    return 384, ''.join(o)
FIG[2] = (f2, 'Left, the tree: the arm hangs under the base. Right, the base at (10, 0) is turned 90°, so its own x axis points along world +y, and the arm\'s local (2, 0) lands at world (10, 2), not (12, 0).',
          'A three-node tree World, Base, Arm beside a grid in metres where the base at (10, 0) has its x axis turned to point up and the arm sits at (10, 2), with (12, 0) shown greyed as the wrong answer.')


# ---- 4.3 two spheres overlapping ----
def f3():
    s = 300
    cy = 250
    c1, c2 = 150, 150 + 0.9 * s
    o = [T(40, 28, 'Two spheres, r = 0.5 m each, centres 0.9 m apart', 15, 'start', bold=True)]
    o.append(f'<circle cx="{c1}" cy="{cy}" r="{0.5 * s:.0f}" style="fill:var(--accent-soft);fill-opacity:0.6;stroke:var(--accent);stroke-width:2.5"/>')
    o.append(f'<circle cx="{c2:.0f}" cy="{cy}" r="{0.5 * s:.0f}" style="fill:var(--live-soft);fill-opacity:0.6;stroke:var(--live);stroke-width:2.5"/>')
    o.append(C(c1, cy, 5, INK)); o.append(C(c2, cy, 5, INK))
    o.append(T(c1 - 10, cy + 24, 'C1', 14, bold=True)); o.append(T(c2 + 10, cy + 24, 'C2', 14, bold=True))
    o.append(L(c1, cy, c2, cy, INK, 1.5, '4 3'))
    o.append(Tb((c1 + c2) / 2 - 70, cy - 10, 'd = 0.9 m', 13, bold=True))
    ox1, ox2 = c2 - 0.5 * s, c1 + 0.5 * s
    o.append(L((ox1 + ox2) / 2, cy + 60, (ox1 + ox2) / 2, cy + 86, NX, 1.5))
    o.append(Tb((ox1 + ox2) / 2, cy + 104, 'overlap x = 1.0 − 0.9 = 0.1 m', 14, 'middle', NX, True))
    o.append(L(c1 - 8, cy - 50, c1 - 108, cy - 50, AC, 3, arrow='n')); o.append(Tb(c1 - 58, cy - 62, '20 N on body 1', 13, 'middle', AC, True))
    o.append(L(c2 + 8, cy - 50, c2 + 108, cy - 50, LV, 3, arrow='l')); o.append(Tb(c2 + 58, cy - 62, '20 N on body 2', 13, 'middle', LV, True))
    o.append(T(360, 436, 'F = k x = 200 N/m × 0.1 m = 20 N, equal and opposite along the centre line', 14))
    return 452, ''.join(o)
FIG[3] = (f3, 'The sum of the radii, 1.0 m, is more than the 0.9 m between centres, so the spheres overlap by 0.1 m. The 200 N/m penalty spring pushes them apart with 20 N each, in opposite directions along the centre line.',
          'Two overlapping circles with centres 0.9 m apart and the overlapping band of 0.1 m shaded, with arrows of 20 newtons pushing each circle outward.')


# ---- 4.4 counting records ----
def f4():
    o = [T(40, 28, 'Count from object instances, then multiply', 15, 'start', bold=True)]
    for i in range(4):
        o.append(boxt(40 + i * 82, 50, 74, 50, [f'room {i + 1}', '50 obj'], PANEL, AC, 13))
    o.append(L(190, 104, 190, 136, AC, 2, arrow='n'))
    o.append(boxt(80, 140, 220, 48, ['4 × 50 = 200 objects'], ACS, AC, 15))
    # one object expanded
    ox = 390
    o.append(T(ox, 44, 'every one of the 200 objects has', 14, 'start', MUT))
    o.append(boxt(ox, 136, 110, 44, ['one object'], ACS, AC, 14))
    labs = [('LOD0 mesh', LVS, LV, 'l'), ('LOD1 mesh', LVS, LV, 'l'), ('LOD2 mesh', LVS, LV, 'l'), ('script 1', NXS, NX, 'x'), ('script 2', NXS, NX, 'x')]
    for i, (t, fi, st, ar) in enumerate(labs):
        y = 58 + i * 42
        o.append(boxt(ox + 180, y, 110, 34, [t], fi, st, 13))
        o.append(L(ox + 112, 158, ox + 176, y + 17, st, 1.5, None if ar == 'l' else '5 4', arrow=ar))
    o.append(boxt(60, 300, 280, 48, ['mesh records: 200 × 3 = 600'], LVS, LV, 15))
    o.append(boxt(380, 300, 300, 48, ['script records: 200 × 2 = 400'], NXS, NX, 15))
    o.append(T(360, 382, 'Scripts belong to the object, not to each LOD, so they are not multiplied by 3.', 14))
    return 400, ''.join(o)
FIG[4] = (f4, 'Four rooms of 50 objects give 200 object instances. Each object keeps 3 LOD meshes but only 2 scripts, so there are 600 mesh records and 400 script records.',
          'Four room boxes feeding 200 objects; one object fans out to three LOD meshes and two scripts; totals of 600 mesh records and 400 script records below.')


# ---- 4.5 perspective projection seen edge-on ----
def f5():
    x0, y0 = 70, 300
    s = 120
    Z = lambda z: x0 + z * s
    Yp = lambda y: y0 - y * s
    o = [T(40, 28, 'Edge-on view (y against depth z): camera at the origin', 15, 'start', bold=True)]
    o.append(L(x0 - 20, y0, Z(5.1), y0, L2, 2, arrow='m')); o.append(T(Z(5.1), y0 + 22, 'z (depth)', 13, 'end', MUT))
    o.append(L(x0, y0 + 20, x0, Yp(1.6), L2, 2, arrow='m')); o.append(T(x0 + 8, Yp(1.55), 'y', 13, 'start', MUT))
    o.append(C(x0, y0, 8, INK)); o.append(T(x0, y0 + 26, 'eye', 13, bold=True))
    o.append(L(Z(0.1), y0, Z(0.1), Yp(1.4), NX, 1.5, '3 3')); o.append(T(Z(0.1) + 4, Yp(1.45), 'near 0.1', 13, 'start', NX))
    o.append(L(Z(2), y0, Z(2), Yp(1.4), AC, 3)); o.append(T(Z(2), Yp(1.48), 'image plane z = f = 2', 13, fill=AC, bold=True))
    o.append(L(x0, y0, Z(4), Yp(1), LV, 2.5))
    o.append(C(Z(4), Yp(1), 8, LV)); o.append(T(Z(4) + 12, Yp(1) - 8, 'point (y = 1, z = 4)', 14, 'start', LV, True))
    o.append(C(Z(2), Yp(0.5), 7, NX)); o.append(Tb(Z(2) + 12, Yp(0.5) + 24, 'y′ = 2 × 1 ÷ 4 = 0.5', 14, 'start', NX))
    o.append(L(Z(4), Yp(1), Z(4), y0, L2, 1.5, '4 3')); o.append(T(Z(4), y0 + 22, '4', 13, fill=MUT))
    o.append(T(Z(2), y0 + 22, '2', 13, fill=MUT))
    o.append(T(40, 350, 'Similar triangles: y′ / f = y / z. The same rule gives x′ = 2 × 2 ÷ 4 = 1.0,', 14, 'start'))
    o.append(T(40, 372, 'so the image point is (1.0, 0.5); z = 4 is past the near plane, so nothing is clipped.', 14, 'start'))
    return 390, ''.join(o)
FIG[5] = (f5, 'Seen edge-on, the ray from the eye to the point (y = 1, z = 4) crosses the image plane at z = 2 at height 0.5: similar triangles give y′ = f·y/z. With x′ = 1.0 the image point is (1.0, 0.5).',
          'A side view with the eye at the origin, a near plane at 0.1, an image plane at z = 2 and a ray to the point at depth 4 and height 1, crossing the image plane at height 0.5.')


# ---- 4.6 culling and LOD cut the work ----
def f6():
    o = [T(40, 28, 'What survives each step (per eye, per frame)', 15, 'start', bold=True)]
    x0, maxw = 230, 450
    rows = [('all objects', 10000, '10,000', PANEL, L2), ('frustum keeps 30%', 3000, '3,000', ACS, AC), ('occlusion keeps 50%', 1500, '1,500 drawn', ACS, AC)]
    y = 54
    for lab, v, txt, fi, st in rows:
        o.append(T(x0 - 12, y + 24, lab, 14, 'end'))
        o.append(R(x0, y, maxw * v / 10000, 36, fi, st, 3)); o.append(T(x0 + maxw * v / 10000 + 8, y + 24, txt, 14, 'start', bold=True) if v < 8000 else T(x0 + maxw - 10, y + 24, txt, 14, 'end', bold=True))
        y += 50
    o.append(T(40, y + 18, 'objects', 13, 'start', MUT))
    y += 40
    rows = [('1,500 × 1,000', 1.5e6, '1,500,000 triangles', PANEL, L2), ('LOD keeps 40%', 0.6e6, '600,000 triangles', LVS, LV)]
    for lab, v, txt, fi, st in rows:
        o.append(T(x0 - 12, y + 24, lab, 14, 'end'))
        o.append(R(x0, y, maxw * v / 1.5e6, 36, fi, st, 3)); o.append(T(x0 + 8, y + 24, txt, 14, 'start', bold=True))
        y += 50
    o.append(T(40, y + 18, 'triangles', 13, 'start', MUT))
    o.append(T(40, y + 56, '600,000 × 90 frames per second = 54,000,000 triangles per second, for each eye', 14, 'start', bold=True))
    o.append(T(40, y + 80, 'Culling removes whole objects; LOD removes triangles inside the objects that remain.', 14, 'start', MUT))
    return y + 96, ''.join(o)
FIG[6] = (f6, 'Frustum culling keeps 3,000 of the 10,000 objects and occlusion culling keeps 1,500. LOD then keeps 40% of their 1,500,000 triangles, leaving 600,000 per eye per frame, or 54 million a second at 90 Hz.',
          'Shrinking bars: 10,000 objects to 3,000 to 1,500, then 1,500,000 triangles to 600,000, with the per-second rate of 54 million below.')


# ---- 4.7 series chain vs pipelining ----
def f7():
    x0, x1 = 120, 690
    s = (x1 - x0) / 22
    X = lambda v: x0 + v * s
    o = [T(40, 28, 'One frame in series: 2 + 3 + 5 + 2 = 12 ms', 15, 'start', bold=True)]
    st = [(0, 2, 'track', PANEL, L2), (2, 5, 'CPU', ACS, AC), (5, 10, 'GPU 5', NXS, NX), (10, 12, 'show', PANEL, L2)]

    def frame(y, off, lab):
        r = [T(x0 - 10, y + 22, lab, 13, 'end', bold=True)]
        for a, b, t, fi, sk in st:
            r.append(R(X(a + off), y, (b - a) * s, 32, fi, sk, 3)); r.append(T(X((a + b) / 2 + off), y + 21, t, 13))
        return ''.join(r)
    o.append(frame(48, 0, 'frame'))
    o.append(L(X(11.1), 38, X(11.1), 92, NX, 2.5, '5 4')); o.append(T(X(11.1) + 6, 100, '90 Hz slot 11.1 ms: missed by 0.9', 13, 'start', NX, True))
    o.append(T(40, 140, 'Pipelined: the next frame starts while the GPU is busy', 15, 'start', bold=True))
    for i in range(3):
        o.append(frame(156 + i * 42, i * 5, f'frame {i + 1}'))
    for i in range(1, 3):
        o.append(L(X(10 + 5 * (i - 1)), 290, X(10 + 5 * i), 290, AC, 2, arrow='n'))
    o.append(T(X(15), 312, 'a new frame every 5 ms (the GPU stage) → up to 200 Hz', 13, fill=AC, bold=True))
    o.append(xaxis(x0, x1, 326, [0, 5, 10, 15, 20], X, 'ms'))
    o.append(T(40, 396, 'No overlap: 1000 ÷ 12 = 83.3 fps. Overlap feeds 90 Hz on time, but each image is still 12 ms old.', 14, 'start'))
    return 414, ''.join(o)
FIG[7] = (f7, 'In series one frame takes 12 ms and misses the 11.1 ms slot of a 90 Hz panel. Pipelined, frames overlap and one leaves every 5 ms, so the panel is fed on time, yet each image still shows the head as it was 12 ms ago.',
          'A bar of four stages, track, CPU, GPU and display, ending at 12 ms past a dashed 11.1 ms line; below, three such bars staggered by 5 ms so that frames finish every 5 milliseconds.')


# ---- 4.8 quaternion rotation of (1, 0, 0) ----
def f8():
    cx, cy, s = 200, 260, 160
    o = [T(40, 28, '90° about z, looking down the z axis', 15, 'start', bold=True)]
    o.append(L(cx - 40, cy, cx + s + 40, cy, L2, 2, arrow='m')); o.append(T(cx + s + 40, cy + 22, 'x', 14, 'end', MUT))
    o.append(L(cx, cy + 40, cx, cy - s - 40, L2, 2, arrow='m')); o.append(T(cx + 10, cy - s - 30, 'y', 14, 'start', MUT))
    o.append(C(cx, cy, 6, INK)); o.append(T(cx - 10, cy + 22, 'z axis (out of page)', 13, 'end', MUT))
    o.append(L(cx, cy, cx + s, cy, AC, 3.5, arrow='n')); o.append(T(cx + s, cy - 12, 'p = (1, 0, 0)', 14, 'middle', AC, True))
    o.append(L(cx, cy, cx, cy - s, NX, 3.5, arrow='x')); o.append(T(cx + 12, cy - s + 8, 'p′ = (0, 1, 0)', 14, 'start', NX, True))
    o.append(f'<path d="M{cx + s * 0.6:.1f},{cy:.1f} A{s * 0.6:.1f},{s * 0.6:.1f} 0 0 0 {cx:.1f},{cy - s * 0.6:.1f}" style="fill:none;stroke:var(--ink);stroke-width:2" marker-end="url(#ar-UID-m)"/>')
    o.append(T(cx + s * 0.48, cy - s * 0.48, '90°', 14, bold=True))
    tx = 430
    o += [T(tx, 80, 'half angle: 90° ÷ 2 = 45°', 14, 'start', bold=True),
          T(tx, 104, 'cos 45° = sin 45° = 0.7071', 14, 'start'),
          T(tx, 140, 'q = (w, x, y, z)', 14, 'start'),
          T(tx, 164, '  = (0.7071, 0, 0, 0.7071)', 14, 'start', AC, True),
          T(tx, 188, 'length: 0.5 + 0.5 = 1', 14, 'start'),
          T(tx, 226, 'u = (0, 0, 0.7071)', 14, 'start'),
          T(tx, 250, 'u × p = (0, 0.7071, 0)', 14, 'start'),
          T(tx, 274, 'u × (u × p) = (−0.5, 0, 0)', 14, 'start'),
          T(tx, 298, 'p′ = p + 2w(u×p) + 2u×(u×p)', 13, 'start', MUT),
          T(tx, 322, '   = (0, 1, 0)', 14, 'start', NX, True),
          T(tx, 358, 'check: m₀₀ = 1 − 2(0 + 0.5) = 0', 14, 'start')]
    return 380, ''.join(o)
FIG[8] = (f8, 'The quaternion for 90° about z uses the half angle, 45°, so q = (0.7071, 0, 0, 0.7071). Applying it turns (1, 0, 0) a quarter turn to (0, 1, 0), and the matrix entry m₀₀ = 0 agrees.',
          'The x and y axes with the z axis pointing out of the page; an arrow along x labelled p turns 90 degrees to an arrow along y labelled p prime, beside the half-angle working of the quaternion.')


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d
