"""Claude's hand-drawn figures for ee-pe-u2 (Power Electronics: controlled and uncontrolled rectifiers), one per chapter,
drawn from each chapter's own worked example and numbers. Every waveform is computed point by point from the circuit
equations (no sketches); colours are the shell's CSS variables only."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
D2R = math.pi / 180
VM = 230 * math.sqrt(2)          # 325.27 V, the 230 V supply peak used throughout the unit


# ---------------------------------------------------------------- circuit symbols
def _frame(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    n = math.hypot(dx, dy)
    ux, uy = dx / n, dy / n
    return n, (lambda s, t: (x1 + ux * s - uy * t, y1 + uy * s + ux * t))


def wire(*pts, c=INK, w=2):
    return P(list(pts), c, w)


def res(x1, y1, x2, y2, c=AC, body=44):
    n, pt = _frame(x1, y1, x2, y2)
    a = (n - body) / 2
    zz = [pt(0, 0), pt(a, 0)]
    for i in range(6):
        zz.append(pt(a + (2 * i + 1) * body / 12, -7 if i % 2 == 0 else 7))
    zz += [pt(a + body, 0), pt(n, 0)]
    return P(zz, c, 2.2)


def ind(x1, y1, x2, y2, c=AC, body=48):
    n, pt = _frame(x1, y1, x2, y2)
    a = (n - body) / 2
    w = body / 4
    d = f'M{pt(0, 0)[0]:.1f},{pt(0, 0)[1]:.1f} L{pt(a, 0)[0]:.1f},{pt(a, 0)[1]:.1f}'
    for i in range(4):
        e = pt(a + (i + 1) * w, 0)
        d += f' A{w / 2:.1f},{w / 2:.1f} 0 0 1 {e[0]:.1f},{e[1]:.1f}'
    e = pt(n, 0)
    d += f' L{e[0]:.1f},{e[1]:.1f}'
    return f'<path d="{d}" style="fill:none;stroke:{c};stroke-width:2.2"/>'


def cap(x1, y1, x2, y2, c=AC, gap=9, plate=28):
    n, pt = _frame(x1, y1, x2, y2)
    m = n / 2
    o = [L(*pt(0, 0), *pt(m - gap / 2, 0), INK, 2), L(*pt(m + gap / 2, 0), *pt(n, 0), INK, 2)]
    o += [L(*pt(m - gap / 2, -plate / 2), *pt(m - gap / 2, plate / 2), c, 3), L(*pt(m + gap / 2, -plate / 2), *pt(m + gap / 2, plate / 2), c, 3)]
    return ''.join(o)


def diode(x1, y1, x2, y2, c=AC, body=22, gate=None, wc=INK):
    """diode from anode (x1,y1) to cathode (x2,y2); gate='l' or 'r' adds a thyristor gate on that side"""
    n, pt = _frame(x1, y1, x2, y2)
    a = (n - body) / 2
    h = body * 0.55
    o = [L(*pt(0, 0), *pt(a, 0), wc, 2), L(*pt(a + body, 0), *pt(n, 0), wc, 2)]
    tri = [pt(a, -h), pt(a, h), pt(a + body, 0), pt(a, -h)]
    o.append(P(tri, c, 2.2, fill=c, op=0.25))
    o.append(L(*pt(a + body, -h), *pt(a + body, h), c, 3))
    if gate:
        s = -1 if gate == 'l' else 1
        g0 = pt(a + body * 0.85, s * h * 0.4)
        g1 = pt(a + body * 0.85 + 10, s * (h + 10))
        o.append(L(*g0, *g1, c, 2))
    return ''.join(o)


def vsrc_ac(cx, cy, r=18, c=LV):
    o = [f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" style="fill:var(--fig);stroke:{c};stroke-width:2.4"/>']
    pts = [(cx - r * 0.6 + i * r * 1.2 / 20, cy - r * 0.35 * math.sin(i / 20 * 2 * math.pi)) for i in range(21)]
    o.append(P(pts, c, 2))
    return ''.join(o)


def dot(x, y, c=INK, r=4):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{c}"/>'


def iarrow(x, y, d, c=AC, size=7):
    dx, dy = {'up': (0, -1), 'down': (0, 1), 'left': (-1, 0), 'right': (1, 0)}[d]
    tip = (x + dx * size, y + dy * size)
    b1 = (x - dx * size - dy * size * 0.8, y - dy * size + dx * size * 0.8)
    b2 = (x - dx * size + dy * size * 0.8, y - dy * size - dx * size * 0.8)
    return f'<polygon points="{tip[0]:.1f},{tip[1]:.1f} {b1[0]:.1f},{b1[1]:.1f} {b2[0]:.1f},{b2[1]:.1f}" style="fill:{c}"/>'


def area(pts, base_y, c, op=0.22):
    """filled region between a curve and a horizontal line"""
    poly = [(pts[0][0], base_y)] + pts + [(pts[-1][0], base_y)]
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in poly)}" style="fill:{c};fill-opacity:{op};stroke:none"/>'


def curve(f, a, b, fx, fy, n=240):
    return [(fx(a + (b - a) * i / n), fy(f(a + (b - a) * i / n))) for i in range(n + 1)]


# ---------------------------------------------------------------- 2.1 bridge rectifier and its output
def f1():
    o = []
    A, Pp, B, N = (52, 150), (162, 58), (272, 150), (162, 242)
    # diodes: D1 A->P, D3 B->P, D4 N->A, D2 N->B ; D1, D2 conduct in the positive half (accent), D3, D4 muted
    o.append(diode(*A, *Pp, AC))
    o.append(diode(*B, *Pp, L2))
    o.append(diode(*N, *A, L2))
    o.append(diode(*N, *B, AC))
    o.append(T(88, 92, 'D1', 14, bold=True, fill=AC)); o.append(T(240, 92, 'D3', 14, bold=True, fill=MUT))
    o.append(T(86, 218, 'D4', 14, bold=True, fill=MUT)); o.append(T(240, 218, 'D2', 14, bold=True, fill=AC))
    # load inside the diamond, P to N
    o.append(res(162, 58, 162, 242, LV))
    o.append(T(178, 146, 'R', 14, 'start', bold=True)); o.append(T(178, 164, '100 Ω', 13, 'start', MUT))
    o.append(iarrow(162, 102, 'down', LV))
    o.append(T(176, 50, 'DC+', 13, 'start', MUT)); o.append(T(176, 262, 'DC−', 13, 'start', MUT))
    # source below, wired to A and B
    o.append(wire(A, (52, 300), (140, 300))); o.append(wire((184, 300), (272, 300), B))
    o.append(vsrc_ac(162, 300))
    o.append(T(162, 334, '230 V, 50 Hz', 13, fill=MUT))
    for p in (A, Pp, B, N): o.append(dot(*p))
    o.append(T(38, 145, 'A', 14, 'end', bold=True)); o.append(T(286, 145, 'B', 14, 'start', bold=True))
    # output waveform, two cycles
    x0, x1, y0, y1 = 372, 700, 48, 288
    fx = lambda t: x0 + (x1 - x0) * t / 40
    fy = lambda v: y1 - (y1 - y0) * v / 350
    o.append(axes(x0, x1, y0, y1, [0, 10, 20, 30, 40], [0, 100, 200, 300], fx, fy, 't (ms)', 'vo (V)'))
    pts = curve(lambda t: abs(VM * math.sin(2 * math.pi * 50 * t / 1000)), 0, 40, fx, fy, 320)
    o.append(area(pts, y1, LV, 0.12))
    o.append(P(pts, LV, 2.6))
    o.append(L(x0, fy(207.07), x1, fy(207.07), AC, 2, dash='7 5'))
    o.append(Tb(560, fy(207.07) + 18, 'Vdc = 2Vm/π = 207.1 V', 13, fill=AC, bold=True))
    o.append(Tb(478, fy(VM) - 8, 'Vm = 325.3 V', 13, bold=True))
    o.append(brace(fx(10), fx(20), fy(0) - 30, MUT, up=True))
    o.append(Tb(fx(15), fy(0) - 38, '10 ms: ripple at 100 Hz', 13, fill=MUT))
    return 352, ''.join(o)


FIG[1] = (f1, 'The bridge of the worked example. In the positive half-cycle D1 and D2 carry the current down through the 100 Ω load; '
              'in the negative half D3 and D4 take over, so the output has two pulses per cycle averaging 207.1 V.',
          'A diode bridge with D1 from A to DC plus, D3 from B to DC plus, D4 from DC minus to A and D2 from DC minus to B, a 100 ohm load '
          'between DC plus and DC minus and a 230 volt source between A and B. Beside it the output: full-wave half-sines of peak 325.3 volts '
          'repeating every 10 milliseconds, with a dashed average line at 207.1 volts.')


# ---------------------------------------------------------------- 2.2 capacitor filter: output and diode current
def f2():
    o = []
    RL, Cf, w = 157.63, 1000e-6, 2 * math.pi * 50
    # simulate 3 half-cycles in steady state from the peak at 5 ms (ideal diodes)
    dt = 2e-6; t = 0.0; vc = VM; ts, vcs, ids = [], [], []
    while t < 0.030:
        vr = abs(VM * math.sin(w * t))
        if t > 0.005 and vr >= vc:
            # conducting: capacitor follows the rectified sine; diode current = C dv/dt + v/R
            dv = VM * w * math.cos(w * t) * (1 if math.sin(w * t) >= 0 else -1)
            vc = vr; idd = Cf * dv + vc / RL
        else:
            vc = vc - vc / (RL * Cf) * dt if t > 0.005 else vr
            idd = 0.0 if t > 0.005 else Cf * VM * w * math.cos(w * t) + vr / RL
        ts.append(t * 1000); vcs.append(vc); ids.append(max(idd, 0))
        t += dt
    x0, x1 = 80, 690
    fx = lambda tm: x0 + (x1 - x0) * (tm - 5) / 25
    # upper panel: voltages, axis from 240 V to 335 V
    y0, y1 = 40, 230
    fy = lambda v: y1 - (y1 - y0) * (v - 240) / 95
    o.append(axes(x0, x1, y0, y1, [], [250, 275, 300, 325], fx, fy, '', 'voltage (V), axis starts at 240 V'))
    rect = [(fx(tm), fy(abs(VM * math.sin(w * tm / 1000)))) for tm in [5 + i * 25 / 500 for i in range(501)] if abs(VM * math.sin(w * tm / 1000)) >= 240]
    seg, segs = [], []
    for tm in [5 + i * 25 / 500 for i in range(501)]:
        v = abs(VM * math.sin(w * tm / 1000))
        if v >= 240: seg.append((fx(tm), fy(v)))
        elif seg: segs.append(seg); seg = []
    if seg: segs.append(seg)
    for s in segs: o.append(P(s, L2, 2, dash='6 4'))
    sel = [(fx(ts[i]), fy(vcs[i])) for i in range(0, len(ts), 25) if ts[i] >= 5]
    o.append(P(sel, AC, 2.8))
    o.append(L(x0, fy(315.27), x1, fy(315.27), LV, 1.6, dash='4 4'))
    o.append(Tb(fx(19.5), fy(315.27) + 18, 'Vdc ≈ 315.3 V', 13, fill=LV, bold=True))
    o.append(T(fx(15), fy(VM) - 10, 'Vm = 325.3 V', 13, bold=True))
    o.append(Tb(258, fy(307.4) + 18, 'dips to 307.4 V: about 18 V of ripple', 13, fill=AC))
    o.append(T(fx(10), fy(250), 'rectified sine', 13, fill=MUT))
    # lower panel: diode current
    z0, z1 = 268, 378
    fi = lambda i: z1 - (z1 - z0) * i / 40
    o.append(L(x0, z1, x1, z1, L2, 1.5)); o.append(L(x0, z0 - 6, x0, z1, L2, 1.5))
    for v in (0, 20, 40):
        o.append(L(x0 - 5, fi(v), x0, fi(v), L2, 1.5)); o.append(T(x0 - 9, fi(v) + 4.5, str(v), 13, 'end', MUT))
    for tm in (5, 10, 15, 20, 25, 30):
        o.append(L(fx(tm), z1, fx(tm), z1 + 5, L2, 1.5)); o.append(T(fx(tm), z1 + 20, str(tm), 13, fill=MUT))
    o.append(T(385, z1 + 40, 't (ms)', 14, fill=MUT))
    o.append(T(x0, z0 - 14, 'diode current (A)', 14, 'start', MUT))
    cur = [(fx(ts[i]), fi(ids[i])) for i in range(0, len(ts), 10) if ts[i] >= 5]
    o.append(P(cur, NX, 2.4))
    o.append(T(fx(13.6), fi(33), 'pulse peak ≈ 35 A', 13, 'end', NX, bold=True))
    o.append(T(fx(19), fi(10), 'load current only 2 A', 13, fill=MUT))
    return 430, ''.join(o)


FIG[2] = (f2, 'The worked example’s 1000 µF filter with a 2 A load, computed step by step. The capacitor voltage sags only about 18 V between peaks, '
              'but it is recharged in about 19° before each peak, so the diodes pass pulses of about 35 A.',
          'Upper plot, axis from 240 to 335 volts: a dashed rectified sine of peak 325.3 volts and a solid capacitor voltage that falls linearly '
          'to 307.4 volts between peaks, with a dashed average at 315.3 volts. Lower plot: diode current pulses about 35 amperes high, each lasting '
          'about one millisecond before each voltage peak.')


# ---------------------------------------------------------------- 2.3 full-wave doubler and the three-phase bridge output
def f3():
    o = []
    o.append(T(170, 22, '(a) full-wave voltage doubler', 14, bold=True))
    X, M = (90, 160), (230, 160)
    top, bot = 60, 260
    o.append(diode(90, 160, 90, top, AC, gate=None)); o.append(diode(90, bot, 90, 160, NX))
    o.append(T(76, 114, 'D1', 14, 'end', bold=True, fill=AC)); o.append(T(76, 214, 'D2', 14, 'end', bold=True, fill=NX))
    o.append(wire((90, top), (310, top))); o.append(wire((90, bot), (310, bot)))
    o.append(cap(230, top, 230, 160, AC)); o.append(cap(230, 160, 230, bot, NX))
    o.append(T(250, 105, 'C1', 14, 'start', bold=True, fill=AC)); o.append(T(250, 123, '→ Vm', 13, 'start', MUT))
    o.append(T(250, 205, 'C2', 14, 'start', bold=True, fill=NX)); o.append(T(250, 223, '→ Vm', 13, 'start', MUT))
    o.append(wire(X, (138, 160))); o.append(wire((178, 160), M))
    o.append(vsrc_ac(158, 160)); o.append(T(158, 194, '12 V rms', 13, fill=MUT))
    o.append(res(310, top, 310, bot, LV)); o.append(T(298, 150, 'load', 13, 'end', MUT)); o.append(T(298, 168, '50 mA', 13, 'end', MUT))
    for p in (X, M, (90, top), (230, top), (310, top), (90, bot), (230, bot), (310, bot)): o.append(dot(*p))
    o.append(T(170, 292, 'Vo = 2Vm = 33.9 V at no load', 13, bold=True))
    o.append(T(170, 312, '32.9 V with 50 mA (1.0 V ripple)', 13, fill=MUT))
    # (b) three-phase bridge output at 415 V
    o.append(T(530, 22, '(b) 3-phase diode bridge, 415 V', 14, bold=True))
    VLm = 415 * math.sqrt(2)
    x0, x1, y0, y1 = 400, 700, 50, 270
    fx = lambda th: x0 + (x1 - x0) * th / 360
    fy = lambda v: y1 - (y1 - y0) * (v - 450) / 150
    o.append(axes(x0, x1, y0, y1, [0, 90, 180, 270, 360], [500, 550, 600], fx, fy, 'θ (degrees)', 'vo (V)'))
    lines = [lambda th, k=k: VLm * math.sin((th + 30 - 60 * k) * D2R) for k in range(6)]
    for f in lines:
        # split into contiguous pieces
        pieces, cur = [], []
        for t in [i * 0.5 for i in range(721)]:
            if f(t) >= 496: cur.append((fx(t), fy(f(t))))
            elif cur: pieces.append(cur); cur = []
        if cur: pieces.append(cur)
        for pc in pieces: o.append(P(pc, L2, 1.4))
    env = [(fx(t), fy(max(f(t) for f in lines))) for t in [i * 0.5 for i in range(721)]]
    o.append(P(env, AC, 2.8))
    o.append(L(x0, fy(560.45), x1, fy(560.45), LV, 1.8, dash='6 4'))
    o.append(Tb(fx(180), fy(560.45) + 4, 'Vdc = 560.4 V', 13, fill=LV, bold=True))
    o.append(T(x1, fy(VLm) - 8, 'VLm = 586.9 V', 13, 'end', bold=True))
    o.append(Tb(fx(300), fy(508.3) + 26, 'dips to 508.3 V', 13, fill=MUT))
    pairs = ['D6D1', 'D1D2', 'D2D3', 'D3D4', 'D4D5', 'D5D6']
    for k, pr in enumerate(pairs):
        c = 60 + 60 * k
        o.append(L(fx(c - 30), y1, fx(c - 30), y1 - 6, MUT, 1))
        o.append(T(fx(c), fy(470), pr, 13, fill=MUT))
    return 336, ''.join(o)


FIG[3] = (f3, 'Left: the worked example’s full-wave doubler; D1 charges C1 and D2 charges C2, each to Vm, and the load sees both in series. '
              'Right: the 415 V three-phase bridge output, the top of the six line voltages, swinging between 508 and 587 V six times per cycle.',
          'Panel a: a full-wave doubler with a 12 volt source between the diode junction and the capacitor midpoint, D1 to the top rail, D2 from '
          'the bottom rail, capacitors C1 and C2 in series and the load across both; 33.9 volts at no load. Panel b: six line voltages and their '
          'upper envelope between 508.3 and 586.9 volts with a dashed average at 560.4 volts, and the conducting diode pairs D6D1, D1D2, D2D3, '
          'D3D4, D4D5 and D5D6 under each 60 degree cap.')


# ---------------------------------------------------------------- 2.4 single-phase full bridge at alpha = 60
def f4():
    o = []
    x0, x1 = 80, 690
    fx = lambda th: x0 + (x1 - x0) * th / 360
    a = 60

    def panel(y0, y1, title, vo, vdc, lab):
        fy = lambda v: (y0 + y1) / 2 - (y1 - y0) / 2 * v / 340
        o.append(T(x0, y0 - 10, title, 14, 'start', bold=True))
        o.append(L(x0, fy(0), x1, fy(0), L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
        for v in (-300, 0, 300):
            o.append(L(x0 - 5, fy(v), x0, fy(v), L2, 1.5)); o.append(T(x0 - 9, fy(v) + 4.5, neg(v), 13, 'end', MUT))
        vs = [(fx(t), fy(VM * math.sin(t * D2R))) for t in [i * 1.0 for i in range(361)]]
        o.append(P(vs, L2, 1.4, dash='5 4'))
        pts = [(fx(t), fy(vo(t))) for t in [i * 0.5 for i in range(721)]]
        o.append(area(pts, fy(0), AC, 0.16))
        o.append(P(pts, AC, 2.6))
        o.append(L(x0, fy(vdc), x1, fy(vdc), LV, 2, dash='7 5'))
        o.append(Tb(fx(300), fy(vdc) - 8, lab, 13, fill=LV, bold=True))
        return fy

    def vo_r(t):
        s = VM * math.sin(t * D2R)
        if a <= t < 180: return s
        if 180 + a <= t < 360: return -s
        return 0.0

    def vo_c(t):
        s = VM * math.sin(t * D2R)
        return s if a <= t < 180 + a else -s

    fy1 = panel(40, 190, '(a) R load: current stops at 180°', vo_r, 155.31, 'Vdc = 155.3 V')
    fy2 = panel(250, 400, '(b) large L: current continuous', vo_c, 103.54, 'Vdc = 103.5 V')
    for t in (0, 60, 180, 240, 360):
        o.append(L(fx(t), 400, fx(t), 405, L2, 1.5)); o.append(T(fx(t), 420, f'{t}°', 13, fill=MUT))
    o.append(T(385, 446, 'ωt', 14, fill=MUT))
    for t, lab in ((60, 'T1, T2 fired'), (240, 'T3, T4 fired')):
        o.append(L(fx(t), 40, fx(t), 400, NX, 1.4, dash='3 4'))
        o.append(Tb(fx(t) + 4, 226, lab, 13, 'start', NX, bold=True))
    o.append(Tb(fx(210), fy2(-140) + 4, 'negative slice', 13, fill=AC))
    o.append(Tb(fx(30), fy1(-170), 'vs (dashed)', 13, fill=MUT))
    return 456, ''.join(o)


FIG[4] = (f4, 'The worked example’s bridge at α = 60° on 230 V. With R alone (a) the output is zero until each firing, averaging 155.3 V; '
              'with a large inductance (b) T1 and T2 carry the current on until T3 and T4 fire at 240°, adding a negative slice and pulling the average down to 103.5 V.',
          'Two plots against angle from 0 to 360 degrees with the supply sine dashed. Panel a, R load: output zero from 0 to 60 degrees, '
          'then the sine to 180, zero to 240, then the inverted sine; average 155.3 volts. Panel b, continuous current: the output follows '
          'the sine from 60 to 240 degrees including a negative slice after 180, then the inverted sine; average 103.5 volts. Firing marks at 60 and 240 degrees.')


# ---------------------------------------------------------------- 2.5 six-pulse bridge output at alpha = 30
def f5():
    o = []
    VLm = 400 * math.sqrt(2)
    x0, x1, y0, y1 = 70, 590, 50, 330
    fx = lambda th: x0 + (x1 - x0) * th / 360
    fy = lambda v: y1 - (y1 - y0) * v / 620
    o.append(axes(x0, x1, y0, y1, [0, 60, 120, 180, 240, 300, 360], [0, 200, 400, 600], fx, fy, 'θ (degrees), with va = Vm sin θ', 'vo (V)'))
    names = ['vab', 'vac', 'vbc', 'vba', 'vca', 'vcb']
    lines = [lambda th, k=k: VLm * math.sin((th + 30 - 60 * k) * D2R) for k in range(6)]
    for f in lines:
        pieces, cur = [], []
        for t in [i * 1.0 for i in range(361)]:
            if f(t) >= 0: cur.append((fx(t), fy(f(t))))
            elif cur: pieces.append(cur); cur = []
        if cur: pieces.append(cur)
        for pc in pieces: o.append(P(pc, L2, 1.3))
    a = 30

    def vo(t):
        k = int(((t - 30 - a) % 360) // 60)
        return lines[k](t)
    pts = [(fx(t), fy(vo(t))) for t in [i * 0.5 for i in range(721)]]
    o.append(P(pts, AC, 2.8))
    o.append(L(x0, fy(467.82), x1, fy(467.82), LV, 2, dash='7 5'))
    o.append(T(x1 + 8, fy(467.82) + 5, 'Vdc = 467.8 V', 13, 'start', LV, bold=True))
    o.append(L(x0, fy(540.19), x1, fy(540.19), MUT, 1.2, dash='2 4'))
    o.append(T(x1 + 8, fy(540.19) - 4, 'Vd0 = 540.2 V', 13, 'start', MUT)); o.append(T(x1 + 8, fy(540.19) + 13, '(α = 0)', 13, 'start', MUT))
    order = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6']
    pairs = ['T6T1', 'T1T2', 'T2T3', 'T3T4', 'T4T5', 'T5T6']
    for k in range(6):
        tf = 60 + 60 * k
        if tf < 360:
            o.append(L(fx(tf), fy(0), fx(tf), fy(560), NX, 1.2, dash='3 4'))
            o.append(Tb(fx(tf), fy(600), order[k], 13, fill=NX, bold=True))
        o.append(T(fx(tf + 30 if tf + 30 < 360 else tf + 30 - 360), fy(250), pairs[k], 13, fill=AC))
    o.append(L(fx(30), fy(80), fx(60), fy(80), INK, 1.6, arrow='n'))
    o.append(L(fx(30), fy(30), fx(30), fy(120), INK, 1.4))
    o.append(T(fx(64), fy(80) + 5, 'α = 30°, counted from 30°', 13, 'start', INK))
    return 384, ''.join(o)


FIG[5] = (f5, 'The worked example’s six-pulse bridge on 400 V at α = 30°: each firing comes 30° after the crossing where a diode would start. '
              'The output (solid) is the line voltage of the conducting pair, a new pair every 60°, averaging 467.8 V.',
          'Six line voltages drawn thin against angle, and the bridge output drawn thick: segments of the line voltages starting 30 degrees '
          'after each natural crossing. Firing marks T1 to T5 at 60, 120, 180, 240 and 300 degrees, the conducting pairs T6T1 to T5T6 written '
          'under each segment, a dashed average at 467.8 volts and a dotted line at 540.2 volts, the value at zero firing angle.')


# ---------------------------------------------------------------- 2.6 square input current, its fundamental and harmonics
def f6():
    o = []
    Id, a = 10, 30
    x0, x1, y0, y1 = 60, 440, 40, 300
    fx = lambda th: x0 + (x1 - x0) * th / 360
    fyi = lambda i: (y0 + y1) / 2 - (y1 - y0) / 2 * i / 14
    o.append(L(x0, fyi(0), x1, fyi(0), L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    for v in (-10, 0, 10):
        o.append(L(x0 - 5, fyi(v), x0, fyi(v), L2, 1.5)); o.append(T(x0 - 9, fyi(v) + 4.5, neg(v), 13, 'end', MUT))
    for t in (0, 90, 180, 270, 360):
        o.append(L(fx(t), fyi(0), fx(t), fyi(0) + 5, L2, 1.5))
    o.append(T(x0, y0 - 14, 'current (A); supply voltage to scale', 13, 'start', MUT))
    vs = [(fx(t), fyi(12.0 * math.sin(t * D2R))) for t in range(361)]
    o.append(P(vs, L2, 1.6, dash='5 4'))
    sq = [(fx(0), fyi(-Id)), (fx(a), fyi(-Id)), (fx(a), fyi(Id)), (fx(180 + a), fyi(Id)), (fx(180 + a), fyi(-Id)), (fx(360), fyi(-Id))]
    o.append(P(sq, AC, 2.6))
    i1 = [(fx(t), fyi(4 * Id / math.pi * math.sin((t - a) * D2R))) for t in range(361)]
    o.append(P(i1, LV, 2.4))
    o.append(Tb(fx(120), fyi(Id) - 8, 'is = ±10 A', 13, fill=AC, bold=True))
    o.append(Tb(fx(300), fyi(-12.73) + 22, 'i1: peak 12.73 A, 9.00 A rms', 13, fill=LV, bold=True))
    o.append(Tb(fx(150), fyi(5), 'vs (dashed)', 13, fill=MUT))
    o.append(L(fx(0), fyi(-12.4), fx(30), fyi(-12.4), INK, 1.6, arrow='n'))
    o.append(T(fx(34), fyi(-12.4) + 5, 'φ1 = α = 30°', 13, 'start', INK, bold=True))
    o.append(T(fx(0), fyi(0) + 20, '0', 13, fill=MUT)); o.append(T(fx(180), fyi(0) + 20, '180°', 13, fill=MUT)); o.append(T(fx(360), fyi(0) + 20, '360°', 13, fill=MUT))
    # harmonic bars
    bx0, bx1, by0, by1 = 500, 700, 60, 280
    o.append(T(600, 28, 'RMS of each harmonic (A)', 13, fill=MUT))
    o.append(L(bx0, by1, bx1, by1, L2, 1.5))
    hs = [1, 3, 5, 7, 9, 11]
    vals = [9.00, 3.00, 1.80, 1.29, 1.00, 0.82]
    bw = (bx1 - bx0) / len(hs)
    for j, (h, v) in enumerate(zip(hs, vals)):
        hgt = (by1 - by0) * v / 9.5
        x = bx0 + j * bw + 5
        o.append(R(x, by1 - hgt, bw - 10, hgt, ACS if h > 1 else LVS, AC if h > 1 else LV, 2))
        o.append(T(x + (bw - 10) / 2, by1 - hgt - 7, f'{v:.2f}', 13, bold=h == 1))
        o.append(T(x + (bw - 10) / 2, by1 + 19, str(h), 13, fill=MUT))
    o.append(T(600, by1 + 40, 'harmonic order h', 13, fill=MUT))
    return 330, ''.join(o)


FIG[6] = (f6, 'The worked example’s bridge at α = 30° with Id = 10 A. The supply current is a square wave lagging the voltage by 30°; '
              'its fundamental (solid curve) has 9.00 A rms, and the odd harmonics fall as 1/h.',
          'Left: a dashed supply sine, a square current of plus and minus 10 amperes switching at 30 and 210 degrees, and its fundamental, '
          'a sine of peak 12.73 amperes lagging the voltage by 30 degrees. Right: bars for harmonic orders 1, 3, 5, 7, 9 and 11 with RMS '
          'values 9.00, 3.00, 1.80, 1.29, 1.00 and 0.82 amperes.')


# ---------------------------------------------------------------- 2.7 single-phase bridge with overlap
def f7():
    o = []
    Ls, Id, a = 5e-3, 20, 30
    w = 2 * math.pi * 50
    Xs = w * Ls
    mu = math.degrees(math.acos(math.cos(a * D2R) - 2 * Xs * Id / VM)) - a       # 17.71 degrees
    x0, x1 = 80, 690
    fx = lambda th: x0 + (x1 - x0) * th / 360
    # output voltage
    y0, y1 = 40, 200
    fy = lambda v: (y0 + y1) / 2 - (y1 - y0) / 2 * v / 340

    def vo(t):
        s = VM * math.sin(t * D2R)
        t1 = t % 180
        if a <= t1 < a + mu: return 0.0
        return s if a + mu <= t < 180 + a else -s

    def vo_ideal(t):
        s = VM * math.sin(t * D2R)
        return s if a <= t < 180 + a else -s
    o.append(T(x0, y0 - 12, 'vo (V)', 14, 'start', MUT))
    o.append(L(x0, fy(0), x1, fy(0), L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    for v in (-300, 0, 300):
        o.append(L(x0 - 5, fy(v), x0, fy(v), L2, 1.5)); o.append(T(x0 - 9, fy(v) + 4.5, neg(v), 13, 'end', MUT))
    for start in (a, 180 + a):
        lost = [(fx(t), fy(abs(VM * math.sin(t * D2R)))) for t in [start + mu * i / 40 for i in range(41)]]
        o.append(area(lost, fy(0), NX, 0.35))
    pts = [(fx(t), fy(vo(t))) for t in [i * 0.25 for i in range(1441)]]
    o.append(P(pts, AC, 2.6))
    o.append(L(x0, fy(159.33), x1, fy(159.33), LV, 2, dash='7 5'))
    o.append(Tb(fx(95), fy(159.33) - 12, 'Vdc = 159.3 V', 13, fill=LV, bold=True))
    o.append(T(fx(a + mu) + 14, fy(-150), 'shaded: lost area, μ = 17.7°', 13, 'start', NX, bold=True))
    # supply current
    z0, z1 = 250, 380
    fi = lambda i: (z0 + z1) / 2 - (z1 - z0) / 2 * i / 26

    def isrc(t):
        t1 = t % 360
        if a <= t1 < a + mu: return -Id + VM / Xs * (math.cos(a * D2R) - math.cos(t1 * D2R))
        if a + mu <= t1 < 180 + a: return Id
        if 180 + a <= t1 < 180 + a + mu: return Id - VM / Xs * (math.cos(a * D2R) - math.cos((t1 - 180) * D2R))
        return -Id
    o.append(T(x0, z0 - 14, 'is (A)', 14, 'start', MUT))
    o.append(L(x0, fi(0), x1, fi(0), L2, 1.5)); o.append(L(x0, z0, x0, z1, L2, 1.5))
    for v in (-20, 0, 20):
        o.append(L(x0 - 5, fi(v), x0, fi(v), L2, 1.5)); o.append(T(x0 - 9, fi(v) + 4.5, neg(v), 13, 'end', MUT))
    cur = [(fx(t), fi(isrc(t))) for t in [i * 0.25 for i in range(1441)]]
    o.append(P(cur, NX, 2.6))
    for t in (0, 90, 180, 270, 360):
        o.append(L(fx(t), z1, fx(t), z1 + 5, L2, 1.5)); o.append(T(fx(t), z1 + 20, f'{t}°', 13, fill=MUT))
    o.append(T(385, z1 + 42, 'ωt', 14, fill=MUT))
    for t in (a, a + mu):
        o.append(L(fx(t), y0, fx(t), z1, MUT, 1, dash='2 4'))
    o.append(Tb(fx(a + mu) + 6, fi(-10), 'all four thyristors on: vo = 0', 13, 'start', MUT))
    return 436, ''.join(o)


FIG[7] = (f7, 'The second worked example: 230 V, Ls = 5 mH, Id = 20 A, α = 30°. For μ = 17.7° after each firing the supply current swings from '
              '−20 A to +20 A while all four thyristors conduct and the output is zero; the shaded slices are the 20 V of average output lost.',
          'Upper plot: the bridge output at 30 degrees firing, zero for 17.7 degrees after each firing, with the missing slices shaded and a '
          'dashed average at 159.3 volts. Lower plot: the supply current, which rises from minus 20 to plus 20 amperes during each overlap '
          'and is flat in between.')


# ---------------------------------------------------------------- 2.8 output voltage against alpha, with the inverter limit
def f8():
    o = []
    Vd0 = 3 * math.sqrt(2) * 400 / math.pi
    w = 2 * math.pi * 50
    x0, x1, y0, y1 = 80, 690, 40, 330
    fx = lambda al: x0 + (x1 - x0) * al / 180
    fy = lambda v: (y0 + y1) / 2 - (y1 - y0) / 2 * v / 600
    o.append(L(x0, fy(0), x1, fy(0), L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    for v in (-600, -300, 0, 300, 600):
        o.append(L(x0 - 5, fy(v), x0, fy(v), L2, 1.5)); o.append(T(x0 - 9, fy(v) + 4.5, neg(v), 13, 'end', MUT))
        if v: o.append(L(x0, fy(v), x1, fy(v), LN, 1))
    for al in (0, 30, 60, 90, 120, 150, 180):
        o.append(L(fx(al), fy(0), fx(al), fy(0) + 5, L2, 1.5))
        if al: o.append(T(fx(al), fy(-600) + 20, f'{al}°', 13, fill=MUT))
    o.append(T(385, y1 + 40, 'firing angle α', 14, fill=MUT))
    o.append(T(x0, y0 - 14, 'Vdc (V), 400 V bridge, Ls = 1 mH', 13, 'start', MUT))
    o.append(R(fx(148.7), y0, fx(180) - fx(148.7), y1 - y0, NXS, NX, 0, 1, dash='4 4'))
    ideal = [(fx(al), fy(Vd0 * math.cos(al * D2R))) for al in range(181)]
    o.append(P(ideal, L2, 1.6, dash='5 4'))
    for Id, c, ly in ((20, LV, 540), (100, AC, 470)):
        X = 2 * w * 1e-3 * Id / (math.sqrt(2) * 400)
        amax = math.degrees(math.acos(X - math.cos(15 * D2R)))
        dV = 3 * w * 1e-3 * Id / math.pi
        pts = [(fx(al), fy(Vd0 * math.cos(al * D2R) - dV)) for al in [amax * i / 200 for i in range(201)]]
        o.append(P(pts, c, 2.6))
        vend = Vd0 * math.cos(amax * D2R) - dV
        o.append(C(fx(amax), fy(vend), 5, c))
        o.append(T(fx(98), fy(ly), f'{Id} A: stops at {amax:.1f}°', 13, 'start', c, bold=True))
    # forbidden zone beyond the 100 A limit (drawn first, under the curves)
    o.append(T(fx(165), fy(420), 'commutation', 13, fill=NX, bold=True)); o.append(T(fx(165), fy(360), 'failure', 13, fill=NX, bold=True))
    o.append(T(fx(165), fy(300), 'at 100 A', 13, fill=NX))
    o.append(T(fx(45), fy(-200), 'rectifier: power to DC', 14, fill=MUT))
    o.append(T(fx(122), fy(220), 'inverter: power to AC', 14, fill=MUT))
    o.append(T(fx(98), fy(400), 'dashed: no overlap', 13, 'start', MUT))
    return 384, ''.join(o)


FIG[8] = (f8, 'The second worked example’s bridge with γ0 = 15°. Overlap lowers the output by 6 V at 20 A and 30 V at 100 A, and each curve must stop '
              'where α + μ reaches 165°: at 160.7° for 20 A but already at 148.7° for 100 A.',
          'Plot of average output voltage against firing angle from 0 to 180 degrees. A dashed cosine for no overlap, a curve 6 volts lower for '
          '20 amperes ending at 160.7 degrees, and a curve 30 volts lower for 100 amperes ending at 148.7 degrees, beyond which a shaded '
          'band is marked commutation failure. The left half is labelled rectifier, the right half inverter.')


# ---------------------------------------------------------------- 2.9 dual converter and its quadrants
def bridge_box(x, y, w, h, name, c, flip=False):
    o = [R(x, y, w, h, PANEL, c, 8)]
    o.append(T(x + w / 2, y + 22, name, 14, bold=True, fill=c))
    if flip: o.append(diode(x + w / 2, y + h - 12, x + w / 2, y + 34, c, gate='r'))
    else: o.append(diode(x + w / 2, y + 34, x + w / 2, y + h - 12, c, gate='r'))
    return ''.join(o)


def f9():
    o = []
    o.append(vsrc_ac(240, 34)); o.append(T(270, 30, '415 V, 3-phase', 13, 'start', MUT))
    o.append(wire((222, 34), (110, 34), (110, 90))); o.append(wire((258, 34), (370, 34), (370, 90)))
    o.append(bridge_box(70, 90, 80, 190, 'P', AC, flip=True))
    o.append(bridge_box(330, 90, 80, 190, 'N', NX))
    # top rail: P+ - Lr - A - Lr - N- ; bottom rail: P- - B - N+
    o.append(wire((150, 120), (176, 120))); o.append(ind(176, 120, 234, 120, MUT)); o.append(ind(246, 120, 304, 120, MUT)); o.append(wire((304, 120), (330, 120)))
    o.append(wire((234, 120), (246, 120)))
    o.append(T(205, 104, 'Lr/2', 13, fill=MUT)); o.append(T(275, 104, 'Lr/2', 13, fill=MUT))
    o.append(wire((150, 260), (330, 260)))
    o.append(wire((240, 120), (240, 170))); o.append(wire((240, 210), (240, 260)))
    o.append(f'<circle cx="240" cy="190" r="20" style="fill:var(--fig);stroke:{LV};stroke-width:2.4"/>')
    o.append(T(240, 195, 'M', 15, bold=True, fill=LV))
    o.append(T(214, 195, 'motor', 13, 'end', MUT))
    for p in ((240, 120), (240, 260)): o.append(dot(*p))
    o.append(T(158, 140, '+', 15, bold=True, fill=AC)); o.append(T(158, 252, '−', 15, bold=True, fill=AC))
    o.append(T(322, 140, '−', 15, bold=True, fill=NX)); o.append(T(322, 252, '+', 15, bold=True, fill=NX))
    # quadrant diagram
    qx0, qy0 = 590, 180
    o.append(L(450, qy0, 712, qy0, L2, 1.6, arrow='m')); o.append(L(qx0, 320, qx0, 30, L2, 1.6, arrow='m'))
    o.append(T(708, qy0 + 22, 'Id', 14, 'end', MUT, bold=True)); o.append(T(598, 42, 'Vt', 14, 'start', MUT, bold=True))
    fxq = lambda i: qx0 + i * 2.0
    fyq = lambda v: qy0 - v * 0.3
    o.append(C(fxq(50), fyq(425), 6, AC)); o.append(C(fxq(-50), fyq(375), 6, NX))
    o.append(T(700, 85, 'I: P rectifies', 13, 'end', AC, bold=True))
    o.append(T(700, 102, '425 V, +50 A', 13, 'end', AC)); o.append(T(700, 119, 'α1 = 40.7°', 13, 'end', AC))
    o.append(T(490, 100, 'II: N inverts', 13, fill=NX, bold=True))
    o.append(T(490, 117, '375 V, −50 A', 13, fill=NX)); o.append(T(490, 134, 'αN = 132.0°', 13, fill=NX))
    o.append(T(520, 262, 'III: N rectifies', 13, fill=MUT)); o.append(T(655, 262, 'IV: P inverts', 13, fill=MUT))
    return 336, ''.join(o)


FIG[9] = (f9, 'Left: converters P and N in inverse parallel on the motor, the intergroup reactor split into two halves Lr/2 between them. Right: the second worked example '
              'on the V–I plane: motoring through P at α1 = 40.7° (quadrant I) and braking at the same speed through N at αN = 132° (quadrant II).',
          'Two thyristor bridges P and N fed from one three-phase supply. The positive terminal of P and the negative terminal of N are joined through two reactor halves, whose midpoint feeds the motor; the other motor terminal joins the remaining terminals of P and N. '
          'Beside them axes of terminal voltage against current with two points: 425 volts and plus 50 amperes, P rectifying at 40.7 degrees; '
          '375 volts and minus 50 amperes, N inverting at 132 degrees; and labels for quadrants III and IV.')


# ---------------------------------------------------------------- 2.10 boost PFC: circuit and inductor current
def f10():
    o = []
    # circuit row
    o.append(vsrc_ac(40, 85)); o.append(T(40, 26, '230 V', 13, fill=MUT))
    o.append(wire((40, 67), (40, 45), (90, 45))); o.append(wire((40, 103), (40, 125), (90, 125)))
    o.append(R(90, 30, 90, 110, PANEL, MUT, 6)); o.append(T(135, 78, 'diode', 13, bold=True)); o.append(T(135, 95, 'bridge', 13, bold=True))
    o.append(wire((180, 45), (205, 45))); o.append(ind(205, 45, 285, 45, AC)); o.append(T(245, 30, 'L = 1 mH', 13, bold=True, fill=AC))
    o.append(wire((285, 45), (320, 45))); o.append(diode(320, 45, 380, 45, NX)); o.append(T(350, 30, 'D', 14, bold=True, fill=NX))
    o.append(wire((380, 45), (520, 45)))
    o.append(wire((180, 125), (520, 125)))
    o.append(R(296, 70, 28, 34, PANEL, AC, 4)); o.append(T(310, 92, 'S', 14, bold=True, fill=AC))
    o.append(wire((310, 45), (310, 70))); o.append(wire((310, 104), (310, 125)))
    o.append(T(334, 112, '65 kHz', 13, 'start', MUT))
    o.append(cap(430, 45, 430, 125, LV)); o.append(T(446, 82, '330 µF', 13, 'start', MUT))
    o.append(res(520, 45, 520, 125, INK)); o.append(T(534, 76, 'load', 13, 'start', MUT)); o.append(T(534, 94, '500 W', 13, 'start', MUT))
    o.append(T(610, 66, 'bus', 13, 'start', MUT)); o.append(T(610, 84, '400 V', 14, 'start', bold=True))
    for p in ((310, 45), (310, 125), (430, 45), (430, 125)): o.append(dot(*p))
    # waveform row
    Vo, L_, fs, Re = 400.0, 1e-3, 65e3, 230 ** 2 / 500
    x0, x1, y0, y1 = 70, 690, 180, 360
    fx = lambda th: x0 + (x1 - x0) * th / 180
    fyi = lambda i: y1 - (y1 - y0) * i / 4
    o.append(L(x0, y1, x1, y1, L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    for v in (0, 1, 2, 3, 4):
        o.append(L(x0 - 5, fyi(v), x0, fyi(v), L2, 1.5)); o.append(T(x0 - 9, fyi(v) + 4.5, str(v), 13, 'end', MUT))
    for t in (0, 45, 90, 135, 180):
        o.append(L(fx(t), y1, fx(t), y1 + 5, L2, 1.5)); o.append(T(fx(t), y1 + 20, f'{t}°', 13, fill=MUT))
    o.append(T(x0, y0 - 12, 'inductor current (A) over one half-cycle of the mains', 13, 'start', MUT))
    ths = [i * 0.5 for i in range(361)]
    vin = lambda t: VM * math.sin(t * D2R)
    iav = lambda t: vin(t) / Re
    dI = lambda t: vin(t) * (1 - vin(t) / Vo) / (L_ * fs)
    hi = [(fx(t), fyi(iav(t) + dI(t) / 2)) for t in ths]
    lo = [(fx(t), fyi(max(iav(t) - dI(t) / 2, 0))) for t in ths]
    band = hi + lo[::-1]
    o.append(f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in band)}" style="fill:var(--accent-soft);stroke:none"/>')
    o.append(P(hi, AC, 1.2)); o.append(P(lo, AC, 1.2))
    o.append(P([(fx(t), fyi(iav(t))) for t in ths], AC, 2.8))
    vsc = [(fx(t), fyi(vin(t) / 100)) for t in ths]
    o.append(P(vsc, L2, 1.6, dash='5 4'))
    o.append(Tb(fx(90), fyi(3.92), 'average: 3.07 A peak = Vm / Re', 13, fill=AC, bold=True))
    o.append(Tb(fx(28), fyi(1.95), 'ripple band ΔiL', 13, fill=AC))
    o.append(Tb(fx(150), fyi(3.3), '|vs| ÷ 100 (dashed)', 13, fill=MUT))
    o.append(Tb(fx(90), fyi(1.2), 'at the peak ΔiL = 0.94 A, D = 0.19', 13, fill=MUT))
    return 396, ''.join(o)


FIG[10] = (f10, 'The worked example’s 500 W boost PFC stage. The switch keeps the average inductor current proportional to the rectified mains '
                'voltage, peaking at 3.07 A, so the supply sees a 105.8 Ω resistor; the switching ripple band is widest where |vs| = 200 V.',
           'Top: a 230 volt source, a diode bridge, a 1 millihenry inductor, switch S at 65 kilohertz, diode D, a 330 microfarad bus capacitor and '
           'the 500 watt load at 400 volts. Bottom: over one half-cycle, the average inductor current follows a half-sine peaking at 3.07 amperes, '
           'inside a shaded ripple band that is 0.94 amperes wide at the peak; the scaled mains voltage is dashed.')

spec = make_spec(FIG)
