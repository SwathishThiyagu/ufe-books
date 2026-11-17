"""Claude's hand-drawn figures for c-xr-u2 (AR/VR, unit 2: input devices and tracking), one per chapter, from each
chapter's worked example, plus the sentences in the chapter text that describe a figure (text_fixes)."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {}


# ---- 2.1 tracker samples per display frame ----
def f1():
    x0, x1 = 150, 690
    s = (x1 - x0) / 34
    X = lambda v: x0 + v * s
    o = [T(40, 28, 'Tracker samples landing in display frames', 15, 'start', bold=True)]

    def row(y, lab, frame, samp, counts):
        r = [T(x0 - 12, y + 24, lab, 14, 'end', bold=True)]
        t, i = 0.0, 0
        while t + frame <= 34.01:
            r.append(R(X(t), y, frame * s, 36, ACS if i % 2 == 0 else PANEL, AC, 3))
            t += frame; i += 1
        t = 0.0
        while t <= 33.5:
            r.append(L(X(t), y + 44, X(t), y + 62, NX, 3)); r.append(C(X(t), y + 66, 4, NX))
            t += samp
        for k, c in enumerate(counts):
            if (k + 1) * frame <= 34.01: r.append(T(X(k * frame + frame / 2), y + 24, c, 13))
        return ''.join(r)
    o.append(row(56, '60 fps', 1000 / 60, 1000 / 120, ['frame 16.7 ms: 2 samples', 'next frame: 2 samples']))
    o.append(T(x0, 152, 'tracker 120 Hz: a sample every 8.3 ms → 120 ÷ 60 = 2.0 per frame, always', 13, 'start', MUT))
    o.append(row(186, '72 fps', 1000 / 72, 1000 / 90, ['2', '1', '1']))
    o.append(T(x0, 282, 'tracker 90 Hz: a sample every 11.1 ms → 90 ÷ 72 = 1.25 per frame on average,', 13, 'start', MUT))
    o.append(T(x0, 300, 'so frames get 1 or 2 samples and the motion looks uneven', 13, 'start', MUT))
    o.append(xaxis(x0, x1, 322, [0, 10, 20, 30], X, 'milliseconds'))
    return 382, ''.join(o)
FIG[1] = (f1, 'At 60 frames per second each 16.7 ms frame catches exactly two 120 Hz tracker samples. With a 90 Hz tracker and a 72 fps display the ratio is 1.25, so some frames get two samples and some only one.',
          'Two timelines. Top, 16.7 ms frames each holding two tracker ticks. Bottom, 13.9 ms frames holding two, one and one ticks from a 90 Hz tracker.')


# ---- 2.2 ultrasonic time of flight and temperature ----
def f2():
    o = [T(40, 28, 'The same 2.9 ms echo, read at two temperatures', 15, 'start', bold=True)]
    ex, mx = 90, 640
    sc = (mx - ex) / 1.05
    for y, v, d, c, fi in [(90, 343, 0.995, AC, ACS), (190, 349, 1.012, NX, NXS)]:
        o.append(boxt(30, y - 22, 56, 44, ['emit'], PANEL, INK, 13))
        o.append(L(ex, y, ex + d * sc, y, c, 3, arrow='n' if c == AC else 'x'))
        o.append(R(ex + d * sc + 4, y - 22, 40, 44, fi, c, 6)); o.append(T(ex + d * sc + 24, y + 5, 'mic', 13))
        o.append(Tb(ex + d * sc / 2, y - 12, f'{"20" if v == 343 else "30"} °C: d = {v} × 0.0029 = {d:.3f} m', 14))
    o.append(L(ex + 0.995 * sc, 112, ex + 0.995 * sc, 214, MUT, 1.5, '4 3'))
    o.append(T(ex + 0.995 * sc - 6, 250, '17.4 mm longer, though nothing moved', 14, 'end', NX, bold=True))
    o.append(brace(ex + 0.995 * sc, ex + 1.012 * sc, 226, NX))
    o.append(T(40, 296, 'distance = speed of sound × time of flight; a warm room looks like a moved sensor', 14, 'start'))
    return 316, ''.join(o)
FIG[2] = (f2, 'One time of flight of 2.9 ms gives 0.995 m at 20 °C but 1.012 m at 30 °C, because sound is faster in warm air: 17.4 mm of error with no movement at all.',
          'Two arrows from an emitter to a microphone for the same 2.9 millisecond echo: 0.995 m at 20 degrees and 1.012 m at 30 degrees, with the 17.4 mm difference marked.')


# ---- 2.3 Go-Go mapping ----
def f3():
    x0, x1, y0, y1 = 80, 520, 50, 330
    fx = lambda d: x0 + d / 1.2 * (x1 - x0)
    fy = lambda v: y1 - v / 2.2 * (y1 - y0)
    g = lambda d: d if d <= 0.25 else 0.25 + 2 * (d - 0.25)
    o = [axes(x0, x1, y0, y1, [0, 0.25, 0.5, 0.75, 1.0], [0, 0.5, 1.0, 1.5, 2.0], fx, fy, 'real hand distance d (m)', 'virtual hand (m)')]
    o.append(P([(fx(0), fy(0)), (fx(1.2), fy(1.2))], L2, 2, '6 5'))
    o.append(T(fx(0.95), fy(0.95) + 24, 'one-to-one', 13, 'start', MUT))
    o.append(P([(fx(0), fy(0)), (fx(0.25), fy(0.25)), (fx(1.2), fy(g(1.2)))], AC, 3))
    o.append(L(fx(0.25), fy(0) , fx(0.25), fy(0.25), MUT, 1.5, '3 3'))
    pts = [(0.15, 0.15), (0.40, 0.55), (0.80, 1.35), (1.125, 2.0)]
    for d, v in pts:
        o.append(C(fx(d), fy(v), 6, NX if v == 2.0 else AC))
        o.append(Tb(fx(d) - 10, fy(v) - 8, f'{d} → {v:.2f}', 13, 'end'))
    o.append(L(fx(1.125), fy(2.0), fx(1.125), fy(0), NX, 1.5, '4 3'))
    o += [T(548, 70, 'Go-Go, D = 0.25 m, k = 2', 14, 'start', bold=True),
          T(548, 100, 'd ≤ 0.25: virtual = d', 14, 'start'),
          T(548, 124, 'd > 0.25: virtual =', 14, 'start'),
          T(560, 146, '0.25 + 2(d − 0.25)', 14, 'start'),
          T(548, 196, 'shelf at 2 m needs', 14, 'start', NX, bold=True),
          T(548, 218, 'd = 1.125 m: longer', 14, 'start', NX),
          T(548, 240, 'than a seated reach', 14, 'start', NX)]
    return 380, ''.join(o)
FIG[3] = (f3, 'Up to 0.25 m the virtual hand follows the real hand one-to-one; beyond that it moves twice as far. The dots are the worked example: 0.40 m gives 0.55 m, 0.80 m gives 1.35 m, and the 2 m shelf needs a 1.125 m reach.',
          'A graph of virtual hand distance against real hand distance: a line of slope one up to 0.25 m, then slope two, with points at 0.15, 0.40, 0.80 and 1.125 metres.')


# ---- 2.4 glove reading with one threshold vs hysteresis ----
def f4():
    x0, x1, y0, y1 = 80, 690, 64, 300
    fy = lambda b: y1 - (b - 120) / 40 * (y1 - y0)
    N = 60
    fx = lambda i: x0 + i / (N - 1) * (x1 - x0)
    jit = [0, 2.6, -2.4, 1.8, -2.9, 2.2, -1.6, 2.9, -2.5, 1.2]
    sig = []
    for i in range(N):
        base = 124 + 16 * min(i, 20) / 20 if i < 40 else 140 - 16 * (i - 40) / 19
        sig.append(base + (jit[i % 10] if 18 <= i <= 42 else 0))
    o = [T(40, 26, 'One held fist, bend reading every 10 ms (jitter ±3°)', 15, 'start', bold=True)]
    o.append(axes(x0, x1, y0, y1, [], [125, 135, 140, 145, 155], fx, fy, 'time →', 'bend (°)'))
    o.append(L(x0, fy(140), x1, fy(140), MUT, 1.5, '4 4'))
    o.append(L(x0, fy(145), x1, fy(145), NX, 2, '8 4')); o.append(L(x0, fy(135), x1, fy(135), AC, 2, '8 4'))
    o.append(Tb(x1 - 4, fy(145) - 6, 'enter 145°', 13, 'end', NX)); o.append(Tb(x1 - 4, fy(135) + 16, 'leave 135°', 13, 'end', AC))
    o.append(Tb(x0 + 8, fy(140) - 6, 'one threshold 140°', 13, 'start', MUT))
    o.append(P([(fx(i), fy(b)) for i, b in enumerate(sig)], INK, 2))
    single = sum(1 for a, b in zip(sig, sig[1:]) if a < 140 <= b)
    # hysteresis events
    state, ev = False, 0
    for i, b in enumerate(sig):
        if not state and b >= 145: state, ev = True, ev + 1
        if state and b <= 135: state = False
    o.append(T(40, 362, f'One threshold at 140°: the reading crosses it {single} times → {single} fist events.', 14, 'start'))
    o.append(T(40, 386, 'Hysteresis: fire above 145°, release below 135° → one fist, one event.', 14, 'start', bold=True))
    o.append(T(40, 414, '8-bit ADC over 180°: 180 ÷ 256 = 0.70° per count;  10 sensors × 100 Hz = 1000 bytes per second', 13, 'start', MUT))
    return 428, ''.join(o)
FIG[4] = (f4, 'A finger held near 140° jitters by ±3°, so a single 140° threshold fires again and again. Entering at 145° and leaving at 135° makes a band wider than the jitter, so one fist gives one event.',
          'A noisy bend reading rising to about 140 degrees, holding, then falling, with a dotted 140 degree line it crosses many times and two dashed lines at 145 and 135 degrees forming a hysteresis band.')


# ---- 2.5 optical motion capture stage ----
def f5():
    cx, cy, r = 170, 200, 130
    o = [T(40, 28, 'The 10-second take', 15, 'start', bold=True)]
    o.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="{r * 0.9:.0f}" style="fill:none;stroke:var(--line2);stroke-width:1.5;stroke-dasharray:5 5"/>')
    for i in range(12):
        a = 2 * math.pi * i / 12
        x, y = cx + r * math.cos(a), cy + r * 0.9 * math.sin(a)
        o.append(R(x - 9, y - 7, 18, 14, NXS, NX, 3, 1.5))
    o.append(T(cx, cy + r * 0.9 + 30, '12 cameras at 120 fps', 13, fill=MUT))
    # stick figure
    hx, hy = cx, cy - 62
    o.append(f'<circle cx="{hx}" cy="{hy}" r="14" style="fill:none;stroke:var(--ink);stroke-width:2.5"/>')
    o.append(P([(cx, hy + 14), (cx, cy + 22)], INK, 3))
    o.append(P([(cx - 44, cy - 28), (cx, cy - 34), (cx + 44, cy - 28)], INK, 3))
    o.append(P([(cx - 26, cy + 76), (cx, cy + 22), (cx + 26, cy + 76)], INK, 3))
    for x, y in [(cx - 44, cy - 28), (cx + 44, cy - 28), (cx, cy - 34), (cx, cy + 22), (cx - 26, cy + 76), (cx + 26, cy + 76), (cx - 22, cy - 31), (cx + 22, cy - 31), (cx, cy - 6), (cx - 13, cy + 49), (cx + 13, cy + 49), (hx, hy - 14)]:
        o.append(C(x, y, 5, AC))
    o.append(T(cx + 54, cy - 24, '40 markers', 13, 'start', AC))
    lx = 360
    rows = [('marker samples', '40 × 120 × 10 = 48,000'), ('coordinates', '48,000 × 3 = 144,000'), ('raw size', '144,000 × 4 B = 576 kB'),
            ('lost to occlusion', '5 × 120 × 0.5 = 300')]
    for i, (a, b) in enumerate(rows):
        y = 84 + i * 62
        lost = i == 3
        o.append(boxt(lx, y, 320, 48, [a, b], NXS if lost else ACS, NX if lost else AC, 14))
    o.append(T(lx, 352, 'triangulate markers → fit skeleton (IK)', 13, 'start', MUT))
    o.append(T(lx, 372, '→ joint angles; the 300 gaps are bridged', 13, 'start', MUT))
    return 384, ''.join(o)
FIG[5] = (f5, 'Twelve cameras ring the actor and see 40 markers 120 times a second. A 10 s take holds 48,000 marker samples, 576 kB raw, and the 300 samples hidden when the actor turns must be bridged by the solver.',
          'A ring of twelve cameras around a stick figure dotted with markers, beside four boxes working out 48,000 samples, 144,000 coordinates, 576 kilobytes and 300 lost samples.')


# ---- 2.6 gyro drift vs magnetometer offset, and tilt from gravity ----
def f6():
    x0, x1, y0, y1 = 80, 450, 50, 300
    fx = lambda t: x0 + t / 60 * (x1 - x0)
    fy = lambda e: y1 - e / 35 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [0, 20, 40, 60], [0, 10, 20, 30], fx, fy, 'time at rest (s)', 'angle error (°)')]
    o.append(P([(fx(0), fy(0)), (fx(60), fy(30))], AC, 3))
    o.append(P([(fx(0), fy(10)), (fx(60), fy(10))], NX, 3, '8 5'))
    o.append(C(fx(60), fy(30), 6, AC)); o.append(Tb(fx(60) - 10, fy(30) - 8, 'gyro: 0.5 × 60 = 30°', 13, 'end', AC))
    o.append(L(x0 + 12, fy(26), x0 + 40, fy(26), NX, 3, '8 5')); o.append(T(x0 + 48, fy(26) + 5, 'magnetometer near steel: 10°, flat', 13, 'start', NX))
    # tilt inset
    bx, by = 590, 190
    o.append(T(590, 40, 'tilt from gravity', 14, bold=True))
    o.append(L(bx, by - 120, bx, by + 20, L2, 1.5, '4 4'))
    th = math.radians(30)
    ax, ay = bx + 120 * math.sin(th), by - 120 * math.cos(th)
    o.append(L(bx, by, ax, ay, AC, 3, arrow='n')); o.append(T(ax + 6, ay, 'z axis', 13, 'start', AC))
    o.append(L(bx, by - 120, bx, by - 10, NX, 2.5, arrow='x'))
    o.append(T(bx - 8, by - 100, 'g', 15, 'end', NX, bold=True))
    o.append(f'<path d="M{bx:.1f},{by - 50:.1f} A50,50 0 0 1 {bx + 50 * math.sin(th):.1f},{by - 50 * math.cos(th):.1f}" style="fill:none;stroke:var(--ink);stroke-width:1.5"/>')
    o.append(T(bx + 16, by - 58, 'θ', 14))
    o.append(T(590, by + 50, 'a_z = g cos θ', 14))
    o.append(T(590, by + 72, 'cos θ = 8.50 ÷ 9.81', 14))
    o.append(T(590, by + 94, 'θ ≈ 29.9°, about 30°', 14, bold=True))
    return 352, ''.join(o)
FIG[6] = (f6, 'Left: a 0.5°/s gyro bias adds up to 30° of error after 60 s at rest, while a steel desk shifts the magnetometer by a fixed 10°. Right: reading 8.50 m/s² on the up axis means the axis is tilted about 30° from gravity.',
          'A graph of angle error against time with a rising gyro line reaching 30 degrees at 60 seconds and a flat magnetometer line at 10 degrees; beside it, a z axis tilted 30 degrees from the gravity arrow.')


# ---- 2.7 lighthouse sweep order and the fan angle ----
def f7():
    x0, x1 = 60, 680
    s = (x1 - x0) / 16.67
    X = lambda v: x0 + v * s
    o = [T(40, 28, 'One 60 Hz frame (16.67 ms): four sweeps in turn', 15, 'start', bold=True)]
    sl = [(0, 4.17, 'A sweeps X'), (4.17, 8.33, 'A sweeps Y'), (8.33, 12.5, 'B sweeps X'), (12.5, 16.67, 'B sweeps Y')]
    for i, (a, b, lab) in enumerate(sl):
        o.append(R(X(a), 44, (b - a) * s, 40, ACS if i < 2 else NXS, AC if i < 2 else NX, 3))
        o.append(T(X((a + b) / 2), 69, lab, 14))
    o.append(xaxis(x0, x1, 92, [0, 4.17, 8.33, 12.5, 16.67], X))
    # zoom into first sweep
    o.append(L(X(0), 120, 80, 150, MUT, 1, '3 3')); o.append(L(X(4.17), 120, 420, 150, MUT, 1, '3 3'))
    gx0, gx1, gy0, gy1 = 80, 420, 160, 360
    fx = lambda t: gx0 + t / 4.17 * (gx1 - gx0)
    fy = lambda a: gy1 - a / 120 * (gy1 - gy0)
    o.append(axes(gx0, gx1, gy0, gy1, [0, 1, 2, 3, 4.17], [0, 30, 60, 90, 120], fx, fy, 'time into sweep A-X (ms)', 'beam angle (°)'))
    o.append(P([(fx(0), fy(0)), (fx(4.17), fy(120))], AC, 3))
    a1 = 1.0 / 4.17 * 120
    o.append(L(fx(1), gy1, fx(1), fy(a1), NX, 1.8, '4 3')); o.append(L(gx0, fy(a1), fx(1), fy(a1), NX, 1.8, '4 3'))
    o.append(C(fx(1), fy(a1), 6, NX))
    o.append(Tb(fx(1) + 10, fy(a1) + 4, 'hit at 1.00 ms → 28.8°', 14, 'start', NX))
    tx = 460
    o += [T(tx, 190, 'fan 120° in 4.17 ms', 14, 'start', bold=True),
          T(tx, 214, 'rate = 120 ÷ 0.00417', 14, 'start'),
          T(tx, 236, '≈ 28,777° per second', 14, 'start'),
          T(tx, 270, 'angle = (1.00 ÷ 4.17) × 120', 14, 'start'),
          T(tx, 292, '≈ 28.8°', 14, 'start', bold=True),
          T(tx, 330, 'timing gives an angle,', 13, 'start', MUT),
          T(tx, 348, 'not a distance', 13, 'start', MUT)]
    return 410, ''.join(o)
FIG[7] = (f7, 'Top: within one 16.67 ms frame, station A sweeps X then Y, then station B does the same. Bottom: during one 4.17 ms sweep the 120° fan turns at a steady rate, so a hit 1.00 ms in means the photodiode is 28.8° into the fan.',
          'A bar split into four sweeps, A X, A Y, B X and B Y, over one frame; below it a straight line of beam angle against time for the first sweep, with a hit at 1 millisecond read off as 28.8 degrees.')


TEXT = {
    6: [('θ = arccos(0.8665) = 30.0°.', 'θ = arccos(0.8665) ≈ 29.9°, about 30°.'),
        ('The tilt is 30.0°, the gyro-only angle drifts', 'The tilt is about 29.9° (roughly 30°), the gyro-only angle drifts')],
    7: [('several photodiodes give full 6-DOF pose. Only a few universities teach this.', 'several photodiodes give full 6-DOF pose.')],
}


def text_fixes(k):
    return TEXT.get(k, [])


def drop_sources():
    return ['ocw.mit.edu']


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d
