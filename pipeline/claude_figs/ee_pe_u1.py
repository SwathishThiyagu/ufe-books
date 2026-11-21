"""Claude's hand-drawn figures for ee-pe-u1 (Power Electronics: power semiconductor devices), one per chapter, drawn from
each chapter's own worked example and numbers, plus two sketches used in model answers. Colours are the shell's CSS
variables."""
import os, sys, math, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

_T, _Tb, _boxt = T, Tb, boxt


def _sub(s):
    """V_GS, Rθ_JC ... drawn as real subscripts, never as underscores"""
    return re.sub(r'([A-Za-zθα-ω\)])_([A-Za-z0-9,]+(?:\([a-z]+\))?)', r'\1<tspan baseline-shift="sub" font-size="11">\2</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)
def boxt(x, y, w, h, lines, *a, **k): return _boxt(x, y, w, h, [_sub(l) for l in lines], *a, **k)


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


def fmt(v):
    return neg(f'{v:g}')


def wire(*pts, c=INK, w=2):
    return P(list(pts), c, w)


def dot(x, y, c=INK):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" style="fill:{c}"/>'


def res_v(x, y1, y2, c=AC, n=6, amp=8):
    """vertical zigzag resistor from y1 to y2 with 14 px leads"""
    a, b = y1 + 14, y2 - 14
    pts = [(x, y1), (x, a)]
    for i in range(n):
        pts.append((x + (amp if i % 2 == 0 else -amp), a + (b - a) * (i + 0.5) / n))
    pts += [(x, b), (x, y2)]
    return P(pts, c, 2)


def res_h(x1, x2, y, c=AC, n=6, amp=8):
    a, b = x1 + 12, x2 - 12
    pts = [(x1, y), (a, y)]
    for i in range(n):
        pts.append((a + (b - a) * (i + 0.5) / n, y + (amp if i % 2 == 0 else -amp)))
    pts += [(b, y), (x2, y)]
    return P(pts, c, 2)


def cap_v(x, y1, y2, c=AC, gap=8, w=30):
    m = (y1 + y2) / 2
    return (L(x, y1, x, m - gap / 2, INK, 2) + L(x - w / 2, m - gap / 2, x + w / 2, m - gap / 2, c, 3) +
            L(x - w / 2, m + gap / 2, x + w / 2, m + gap / 2, c, 3) + L(x, m + gap / 2, x, y2, INK, 2))


def diode_v(x, y, up=False, c=AC, s=14, fill=None):
    """diode symbol centred at (x, y), conducting downwards (anode on top) unless up"""
    d = -1 if up else 1
    tri = f'<polygon points="{x - s:.1f},{y - d * s * 0.7:.1f} {x + s:.1f},{y - d * s * 0.7:.1f} {x:.1f},{y + d * s * 0.7:.1f}" style="fill:{fill or c};stroke:{c};stroke-width:2"/>'
    return tri + L(x - s, y + d * s * 0.7, x + s, y + d * s * 0.7, c, 3)


# ---- 1.1 reverse recovery of the worked example: 10 A, di/dt = 8 A/µs, I_RRM = 8 A, t_rr = 2 µs ----
def f1():
    o = []
    x0, x1, y0, y1 = 80, 690, 40, 350
    fx = lin(0, 4.5, x0, x1); fy = lin(-13, 12, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5], [-12, -8, -4, 0, 4, 8, 12], fx, fy, 'time t (µs)', _sub('diode current i_D (A)'), fmt, fmt))
    o.append(L(x0, fy(0), x1, fy(0), INK, 1.5))
    tri = [(fx(1.75), fy(0)), (fx(2.75), fy(-8)), (fx(3.75), fy(0))]
    o.append(f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in tri)}" style="fill:var(--next-soft);stroke:none"/>')
    o.append(P([(fx(0), fy(10)), (fx(0.5), fy(10)), (fx(2.75), fy(-8)), (fx(3.75), fy(0)), (fx(4.5), fy(0))], AC, 3))
    o.append(Tb(fx(0.3), fy(10) - 12, 'I_F = 10 A', 14, 'start', bold=True))
    o.append(Tb(fx(1.2), fy(4.6), 'falls at di/dt = 8 A/µs', 14, 'start'))
    o.append(L(fx(2.75), fy(-8), fx(1.9), fy(-8), NX, 1.5, dash='4 4'))
    o.append(Tb(fx(1.85), fy(-8) + 5, 'I_RRM = 8 A', 14, 'end', fill=NX, bold=True))
    o.append(Tb(fx(2.75), fy(-3.4), 'Q_rr = 8 µC', 14, fill=NX, bold=True))
    yb = fy(0) - 14
    o.append(brace(fx(1.75), fx(2.75), yb, INK, up=False))
    o.append(Tb(fx(2.25), yb - 7, 't_a = 1 µs', 13))
    o.append(brace(fx(2.75), fx(3.75), yb, INK, up=False))
    o.append(Tb(fx(3.25), yb - 7, 't_b = 1 µs', 13))
    yb2 = fy(-9.4)
    o.append(brace(fx(1.75), fx(3.75), yb2, LV, up=True))
    o.append(Tb(fx(2.75), yb2 + 22, 't_rr = 2 µs, softness S = t_b / t_a = 1', 14, fill=LV, bold=True))
    o.append(Tb(fx(4.15), fy(1.6), 'blocks 300 V', 13, fill=MUT))
    return 404, ''.join(o)


# ---- 1.2 SCR static V–I characteristic (sketch) with the example's latching current ----
def f2():
    o = []
    ox, oy = 330, 250
    o.append(L(40, oy, 700, oy, L2, 1.5, arrow='m')); o.append(L(ox, 400, ox, 30, L2, 1.5, arrow='m'))
    o.append(T(690, oy - 10, 'V_AK', 14, 'end', MUT)); o.append(T(ox + 10, 40, 'I_A', 14, 'start', MUT))
    # forward blocking with I_G = 0, breakover at V_BO
    vbo, vb1 = 640, 520
    o.append(P([(ox, oy), (vbo - 40, oy - 6), (vbo, oy - 14)], AC, 2.5))
    o.append(P([(vbo, oy - 14), (ox + 22, oy - 64)], AC, 1.8, dash='6 5'))
    o.append(P([(ox, oy), (vb1 - 30, oy - 7), (vb1, oy - 16)], LV, 2.5))
    o.append(P([(vb1, oy - 16), (ox + 22, oy - 64)], LV, 1.8, dash='6 5'))
    # on-state branch
    o.append(P([(ox + 14, oy - 50), (ox + 22, oy - 64), (ox + 34, oy - 120), (ox + 48, oy - 210)], AC, 3))
    o.append(L(ox, oy - 64, ox + 250, oy - 64, NX, 1.5, dash='4 4'))
    o.append(T(ox + 256, oy - 60, 'I_L = 50 mA (latching)', 13, 'start', NX))
    o.append(L(ox, oy - 50, ox + 14, oy - 50, NX, 1.5, dash='4 4'))
    o.append(T(ox - 8, oy - 44, 'I_H', 13, 'end', NX))
    o.append(T(ox + 58, oy - 170, 'forward conduction: 1–2 V drop', 14, 'start', bold=True))
    o.append(T(vbo, oy + 22, 'V_BO', 14, bold=True)); o.append(T(vbo, oy + 40, '(I_G = 0)', 13, fill=AC)); o.append(L(vbo, oy - 14, vbo, oy + 6, AC, 1.5, dash='3 3'))
    o.append(T(vb1, oy + 22, 'lower breakover', 13, fill=LV)); o.append(T(vb1, oy + 40, '(I_G > 0)', 13, fill=LV)); o.append(L(vb1, oy - 16, vb1, oy + 6, LV, 1.5, dash='3 3'))
    o.append(T(480, oy - 92, 'forward blocking', 14, bold=True))
    # reverse blocking and breakdown
    o.append(P([(ox, oy), (120, oy + 8), (90, oy + 16), (80, oy + 130)], AC, 2.5))
    o.append(T(90, oy - 12, 'V_BR', 14, bold=True)); o.append(L(90, oy + 16, 90, oy - 4, AC, 1.5, dash='3 3'))
    o.append(T(210, oy + 44, 'reverse blocking', 14, bold=True))
    o.append(T(210, oy + 64, '(leakage only)', 13, fill=MUT))
    o.append(T(100, oy + 150, 'reverse breakdown', 13, 'start', fill=NX))
    return 420, ''.join(o)


# ---- 1.3 UJT relaxation oscillator of worked example 2 ----
def f3():
    o = []
    top, bot = 50, 330
    o.append(wire((40, top), (300, top))); o.append(wire((40, bot), (300, bot)))
    o.append(T(40, top - 14, '+V_BB = 20 V', 14, 'start', bold=True)); o.append(T(40, bot + 24, '0 V', 14, 'start', MUT))
    o.append(res_v(90, top, 190)); o.append(T(104, 124, 'R = 10 kΩ', 14, 'start'))
    o.append(cap_v(90, 190, bot)); o.append(T(112, 266, 'C = 0.1 µF', 14, 'start'))
    o.append(dot(90, 190))
    # UJT: base bar, emitter arrow
    bx = 220
    o.append(L(bx, 150, bx, 230, INK, 4))
    o.append(L(90, 190, 150, 190, INK, 2)); o.append(L(150, 190, bx - 2, 210, INK, 2, arrow='x'))
    o.append(T(160, 182, 'E', 13, fill=MUT))
    o.append(wire((bx, 150), (bx, 120))); o.append(res_v(bx, top, 120, MUT, 4, 6))
    o.append(T(bx + 8, 150, 'B2', 13, 'start', MUT))
    o.append(wire((bx, 230), (bx, 250))); o.append(res_v(bx, 250, bot, AC, 4, 6))
    o.append(T(bx + 8, 236, 'B1', 13, 'start', MUT)); o.append(T(bx + 16, 296, 'R1', 14, 'start'))
    o.append(dot(bx, 250)); o.append(L(bx, 250, 290, 250, NX, 2, arrow='x'))
    o.append(T(294, 254, 'to gate', 13, 'start', NX))
    o.append(T(170, 376, 'V_P = η V_BB + V_D = 13.3 V', 14, bold=True)); o.append(T(bx + 16, 90, 'R2', 13, 'start', MUT))
    # waveform
    gx0, gx1, gy0, gy1 = 400, 700, 60, 250
    fx = lin(0, 3, gx0, gx1); fy = lin(0, 16, gy1, gy0)
    o.append(axes(gx0, gx1, gy0, gy1, [0, 1, 2, 3], [0, 2, 13.3], fx, fy, 'time (ms)', _sub('v_C (V)'), fmt, lambda v: f'{v:g}'))
    T_ = 0.988; pts = []
    vv, vp, tau = 2.0, 13.3, 1.0
    t0 = 0.0; v0 = 0.0
    while t0 < 3:
        tt = -tau * math.log((20 - vp) / (20 - v0))
        n = 24
        for i in range(n + 1):
            t = t0 + tt * i / n
            if t > 3: break
            pts.append((fx(t), fy(20 - (20 - v0) * math.exp(-(t - t0) / tau))))
        t0 += tt; v0 = vv
        if t0 < 3: pts.append((fx(t0), fy(vv)))
    o.append(P(pts, AC, 2.5))
    o.append(L(fx(0), fy(13.3), fx(3), fy(13.3), NX, 1.5, dash='4 4'))
    t1 = math.log(20 / 6.7)
    o.append(Tb(fx(0.45), fy(14.8), 'fires at V_P', 13, fill=NX))
    o.append(brace(fx(t1), fx(t1 + T_), 50, LV, up=False))
    o.append(Tb(fx(t1 + T_ / 2), 44, 'T ≈ 0.99 ms, f ≈ 1 kHz', 14, fill=LV, bold=True))
    # pulses across R1
    py = 340
    for k in range(3):
        tk = t1 + k * T_
        if tk > 3: break
        X = fx(tk)
        o.append(P([(X - 3, py), (X, py - 34), (X + 7, py)], NX, 2.5))
    o.append(L(gx0, py, gx1, py, L2, 1.5))
    o.append(T(gx0, py + 22, 'v across R1: one gate pulse per cycle', 13, 'start', MUT))
    return 392, ''.join(o)


# ---- 1.4 impulse commutation of worked example 1: 1 µF at 200 V, 5 A, t_q = 30 µs ----
def f4():
    o = []
    x0, x1 = 90, 690
    fx = lin(-20, 100, x0, x1)
    # current panel
    ya0, ya1 = 40, 120
    fa = lin(0, 6, ya1, ya0)
    o.append(L(x0, ya1, x1, ya1, L2, 1.5)); o.append(L(x0, ya0, x0, ya1, L2, 1.5))
    o.append(T(x0 - 9, fa(5) + 4.5, '5', 13, 'end', MUT)); o.append(T(x0 - 9, ya1 + 4.5, '0', 13, 'end', MUT))
    o.append(T(x0, ya0 - 12, _sub('SCR current i_T (A)'), 14, 'start', MUT))
    o.append(P([(fx(-20), fa(5)), (fx(0), fa(5)), (fx(0), fa(0)), (fx(100), fa(0))], AC, 3))
    o.append(Tb(fx(14), fa(3.2), 'auxiliary SCR fires: current moves to C', 13, 'start'))
    # voltage panel
    yb0, yb1 = 170, 400
    fv = lin(-250, 250, yb1, yb0)
    o.append(axes(x0, x1, yb0, yb1, [-20, 0, 20, 40, 60, 80, 100], [-200, -100, 0, 100, 200], fx, fv, 'time from the auxiliary SCR firing (µs)', _sub('SCR voltage v_T (V)'), fmt, fmt))
    o.append(L(x0, fv(0), x1, fv(0), INK, 1.2))
    shade = [(fx(0), fv(0)), (fx(0), fv(-200)), (fx(40), fv(0))]
    o.append(f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in shade)}" style="fill:var(--live-soft);stroke:none"/>')
    o.append(P([(fx(-20), fv(1)), (fx(0), fv(1)), (fx(0), fv(-200)), (fx(80), fv(200)), (fx(100), fv(200))], AC, 3))
    o.append(Tb(fx(30), fv(-150), 'rises at I/C = 5 V/µs', 14, 'start'))
    o.append(brace(fx(0), fx(40), fv(0) - 16, LV, up=False))
    o.append(Tb(fx(20), fv(0) - 24, 't_c = CV/I = 40 µs', 14, fill=LV, bold=True))
    o.append(brace(fx(0), fx(30), fv(-200) + 22, NX, up=True))
    o.append(Tb(fx(15), fv(-200) + 42, 't_q = 30 µs', 14, fill=NX, bold=True))
    o.append(T(fx(-18), fv(150), 'forward voltage returns after 40 µs > 30 µs: the SCR stays off', 13, 'start', MUT))
    return 448, ''.join(o)


# ---- 1.5 DIAC-TRIAC dimmer and the load voltage at α = 90° ----
def f5():
    o = []
    top, bot = 60, 320
    xs, xr, xt = 50, 110, 290
    # source
    o.append(f'<circle cx="{xs}" cy="190" r="24" style="fill:var(--panel);stroke:var(--live);stroke-width:2"/>')
    o.append(P([(xs - 12, 190), (xs - 6, 180), (xs, 190), (xs + 6, 200), (xs + 12, 190)], LV, 2))
    o.append(wire((xs, 166), (xs, top), (110, top))); o.append(wire((xs, 214), (xs, bot), (xt, bot)))
    o.append(T(xs + 10, 240, '230 V', 13, 'start')); o.append(T(xs + 10, 256, '50 Hz', 13, 'start', MUT))
    # lamp
    o.append(f'<circle cx="140" cy="{top}" r="20" style="fill:var(--panel);stroke:var(--accent);stroke-width:2"/>')
    o.append(L(126, top - 14, 154, top + 14, AC, 2)); o.append(L(126, top + 14, 154, top - 14, AC, 2))
    o.append(T(140, top - 28, 'lamp 100 Ω', 13))
    o.append(wire((160, top), (xt, top)))
    # TRIAC
    o.append(wire((xt, top), (xt, 160))); o.append(wire((xt, 220), (xt, bot)))
    o.append(L(xt - 18, 160, xt + 18, 160, AC, 3)); o.append(L(xt - 18, 220, xt + 18, 220, AC, 3))
    o.append(f'<polygon points="{xt - 18},162 {xt + 1},162 {xt - 8},218" style="fill:var(--accent);stroke:var(--accent);stroke-width:1"/>')
    o.append(f'<polygon points="{xt - 1},218 {xt + 18},218 {xt + 8},162" style="fill:var(--accent);stroke:var(--accent);stroke-width:1"/>')
    o.append(L(xt - 8, 220, xt - 26, 240, AC, 2))
    o.append(T(xt + 22, 156, 'MT2', 13, 'start', MUT)); o.append(T(xt + 22, 232, 'MT1', 13, 'start', MUT))
    o.append(T(xt + 22, 196, 'TRIAC', 14, 'start', bold=True))
    # R-C network and DIAC
    o.append(wire((xt, 100), (xr + 70, 100))); o.append(dot(xt, 100))
    o.append(res_v(xr + 70, 100, 200)); o.append(L(xr + 52, 180, xr + 88, 128, NX, 2, arrow='x'))
    o.append(T(xr + 42, 140, 'R', 14, 'end'))
    o.append(cap_v(xr + 70, 200, bot)); o.append(T(xr + 50, 268, 'C', 14, 'end')); o.append(dot(xr + 70, bot)); o.append(dot(xr + 70, 200))
    o.append(wire((xr + 70, 200), (xr + 82, 200)))
    o.append(f'<polygon points="{xr + 82},190 {xr + 82},210 {xr + 98},200" style="fill:var(--next);stroke:var(--next)"/>')
    o.append(f'<polygon points="{xr + 114},190 {xr + 114},210 {xr + 98},200" style="fill:var(--next);stroke:var(--next)"/>')
    o.append(L(xr + 98, 188, xr + 98, 212, NX, 2))
    o.append(wire((xr + 114, 200), (xt - 38, 200), (xt - 38, 240), (xt - 26, 240)))
    o.append(T(xt - 30, 262, 'G', 13, 'start', MUT))
    o.append(T(xr + 98, 230, 'DIAC', 13, fill=NX)); o.append(T(xr + 98, 246, '≈ 30 V', 13, fill=NX))
    # waveform
    gx0, gx1, gy0, gy1 = 400, 700, 60, 300
    fx = lin(0, 360, gx0, gx1); fy = lin(-340, 340, gy1, gy0)
    o.append(axes(gx0, gx1, gy0, gy1, [0, 90, 180, 270, 360], [-325, 0, 325], fx, fy, 'ωt (degrees)', 'load voltage (V)', lambda v: f'{v:g}°', fmt))
    o.append(L(gx0, fy(0), gx1, fy(0), INK, 1.2))
    sine = [(fx(a), fy(325 * math.sin(math.radians(a)))) for a in range(0, 361, 6)]
    o.append(P(sine, L2, 1.8, dash='5 5'))
    for a0 in (90, 270):
        seg = [(fx(a), fy(325 * math.sin(math.radians(a)))) for a in range(a0, a0 + 91, 5)]
        poly = [(fx(a0), fy(0))] + seg + [(fx(a0 + 90), fy(0))]
        o.append(f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in poly)}" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2.5"/>')
    o.append(Tb(fx(45), fy(250), 'α = 90°', 14, bold=True, fill=NX))
    o.append(T(550, 360, 'V_rms = 162.6 V, P = 264.5 W', 14, bold=True))
    return 380, ''.join(o)


# ---- 1.6 MOSFET turn-on waveforms of worked example 2 ----
def _vgs(t):
    tau1, tau2, t1, t2 = 23.33, 30.0, 16.17, 46.17
    if t <= t1: return 12 * (1 - math.exp(-t / tau1))
    if t <= t2: return 6.0
    return 12 - 6 * math.exp(-(t - t2) / tau2)


def f6():
    o = []
    x0, x1 = 100, 690
    fx = lin(0, 100, x0, x1)
    td, tr, tf = 9.46, 16.17, 46.17
    panels = [(30, 130, 'v_GS (V)', 0, 12, [0, 4, 6, 12]), (170, 250, 'i_D (A)', 0, 10, [0, 10]), (290, 370, 'v_DS (V)', 0, 200, [0, 200])]
    for k, (ya, yb, lab, lo, hi, ticks) in enumerate(panels):
        fy = lin(lo, hi, yb, ya)
        o.append(L(x0, yb, x1, yb, L2, 1.5)); o.append(L(x0, ya - 6, x0, yb, L2, 1.5))
        for v in ticks:
            o.append(T(x0 - 9, fy(v) + 4.5, f'{v:g}', 13, 'end', MUT))
        o.append(T(16, (ya + yb) / 2 + 5, lab, 14, 'start', MUT))
        if k == 0:
            o.append(P([(fx(t), fy(_vgs(t))) for t in [i * 0.5 for i in range(201)]], AC, 2.5))
            o.append(Tb(fx((tr + tf) / 2), fy(6) - 10, 'Miller plateau 6 V', 13, fill=NX, bold=True))
        if k == 1:
            o.append(P([(fx(0), fy(0)), (fx(td), fy(0)), (fx(tr), fy(10)), (fx(100), fy(10))], LV, 2.5))
        if k == 2:
            o.append(P([(fx(0), fy(200)), (fx(tr), fy(200)), (fx(tf), fy(2)), (fx(100), fy(2))], NX, 2.5))
    for t in (td, tr, tf):
        o.append(L(fx(t), 24, fx(t), 372, L2, 1.2, dash='4 4'))
    o.append(brace(fx(0), fx(td), 382, INK, up=True)); o.append(brace(fx(td), fx(tr), 382, LV, up=True)); o.append(brace(fx(tr), fx(tf), 382, NX, up=True))
    o.append(T(fx(td / 2), 404, 't_d(on)', 13)); o.append(T(fx(td / 2), 422, '9.5 ns', 13, fill=MUT))
    o.append(T(fx(td) + 2, 446, 't_ri = 6.7 ns', 13, 'start', LV))
    o.append(T(fx((tr + tf) / 2), 404, 't_fv = 30 ns', 14, fill=NX, bold=True))
    o.append(T(fx(74), 404, 'gate charges to 12 V', 13, fill=MUT))
    o.append(T(390, 474, 'plateau: I_g = (12 − 6) V ÷ 10 Ω = 0.6 A, t_fv = Q_gd ÷ I_g = 18 nC ÷ 0.6 A', 13, fill=MUT))
    o.append(T(fx(100), 446, 'time 0 to 100 ns', 13, 'end', MUT))
    return 486, ''.join(o)


# ---- 1.7 the snubber and gate drive of the worked examples ----
def f7():
    o = []
    top, bot = 50, 360
    o.append(wire((60, top), (500, top))); o.append(wire((60, bot), (500, bot)))
    o.append(T(60, top - 14, '+400 V DC link', 14, 'start', bold=True)); o.append(T(60, bot + 24, '0 V', 14, 'start', MUT))
    # load inductor and freewheel diode
    xl = 160
    o.append(wire((xl, top), (xl, 80)))
    pts = []
    for i in range(4):
        cy = 92 + i * 18
        pts += [(xl + 12 * math.cos(math.radians(a)), cy + 9 * math.sin(math.radians(a))) for a in range(-90, 91, 30)]
    o.append(P([(xl, 80)] + [(xl + (p[0] - xl), p[1]) for p in pts] + [(xl, 164)], AC, 2))
    o.append(wire((xl, 164), (xl, 190)))
    o.append(T(xl - 22, 124, 'load', 13, 'end')); o.append(T(xl - 22, 140, '10 A', 13, 'end', MUT))
    o.append(wire((xl, 80), (240, 80), (240, 108))); o.append(diode_v(240, 125, up=True, c=MUT)); o.append(wire((240, 142), (240, 190), (xl, 190)))
    o.append(T(256, 128, 'D_f', 13, 'start', MUT)); o.append(dot(xl, 190))
    o.append(wire((xl, 190), (330, 190)))
    # IGBT
    xs = 330
    o.append(wire((xs, 190), (xs, 228))); o.append(L(xs, 228, xs - 20, 244, INK, 2))
    o.append(L(xs - 22, 236, xs - 22, 290, INK, 3)); o.append(L(xs - 30, 240, xs - 30, 286, INK, 2))
    o.append(L(xs - 20, 282, xs, 298, INK, 2, arrow='x')); o.append(wire((xs, 298), (xs, bot)))
    o.append(T(xs + 12, 266, 'IGBT', 14, 'start', bold=True))
    # snubber
    xn = 430
    o.append(dot(xs, 190)); o.append(wire((xs, 190), (xn, 190)))
    o.append(cap_v(xn, 190, 250)); o.append(T(xn + 22, 224, 'C_s = 20 nF', 14, 'start'))
    o.append(res_v(xn, 250, bot)); o.append(T(xn + 22, 312, 'R_s = 200 Ω', 14, 'start'))
    o.append(dot(xn, bot))
    o.append(T(xn + 22, 160, 'dv/dt = I/C_s = 500 V/µs', 13, 'start', fill=NX))
    o.append(T(xn + 22, 340, 'P = ½C_sV²f_s = 32 W', 13, 'start', fill=NX))
    # gate driver
    o.append(res_h(xs - 120, xs - 30, 263, AC, 5, 6)); o.append(T(xs - 75, 240, 'R_g = 10 Ω', 13))
    o.append(boxt(40, 226, 150, 74, ['gate driver', '+15 V / −5 V'], PANEL, LV, 14, True))
    o.append(wire((190, 263), (xs - 120, 263)))
    o.append(L(30, 316, 200, 316, L2, 2, dash='6 4'))
    o.append(T(115, 336, 'isolation barrier', 13, fill=MUT))
    o.append(T(115, 352, 'PWM from controller', 13, fill=MUT))
    return 400, ''.join(o)


# ---- 1.8 the thermal path of worked example 1 ----
def f8():
    o = []
    xs = [80, 270, 460, 650]
    temps = [124, 84, 64, 40]
    names = ['junction', 'case', 'heat sink', 'ambient']
    rs = ['Rθ_JC 1.0 °C/W', 'Rθ_CS 0.5 °C/W', 'Rθ_SA 0.6 °C/W']
    drops = ['40 W × 1.0 = 40 °C', '40 W × 0.5 = 20 °C', '40 W × 0.6 = 24 °C']
    y = 80
    for i in range(3):
        o.append(res_h(xs[i], xs[i + 1], y, AC, 6, 9))
        o.append(T((xs[i] + xs[i + 1]) / 2, y - 22, rs[i], 14, bold=True))
        o.append(T((xs[i] + xs[i + 1]) / 2, y + 36, drops[i], 13, fill=MUT))
    for x, n in zip(xs, names):
        o.append(C(x, y, 7, INK)); o.append(T(x, y + 64, n, 14))
    o.append(L(110, 184, 620, 184, NX, 2.5, arrow='x'))
    o.append(Tb(365, 189, 'heat flow P = 30 W switching + 10 W conduction = 40 W', 14, fill=NX, bold=True))
    # temperature bars
    yb, fy = 430, lin(0, 140, 430, 222)
    o.append(L(40, yb, 700, yb, L2, 1.5))
    o.append(L(40, fy(125), 700, fy(125), NX, 1.5, dash='5 4'))
    o.append(T(696, fy(125) - 8, 'limit 125 °C', 13, 'end', NX))
    for x, t in zip(xs, temps):
        o.append(R(x - 32, fy(t), 64, yb - fy(t), ACS, AC, 3))
        o.append(T(x, fy(t) - 8, f'{t} °C', 14, bold=True))
    return 446, ''.join(o)


# ---- 1.9 drift layer for 1200 V (worked example 2) ----
def f9():
    o = []
    rows = [('Silicon', '1.1 eV', '0.3 MV/cm', 80.0, L2, FIGBG), ('SiC', '3.3 eV', '2.2 MV/cm', 10.9, AC, ACS), ('GaN', '3.4 eV', '3 MV/cm', 8.0, LV, LVS)]
    o.append(T(40, 40, 'material', 14, 'start', MUT)); o.append(T(160, 40, 'E_g', 14, 'middle', MUT)); o.append(T(260, 40, 'E_c', 14, 'middle', MUT))
    o.append(T(340, 40, 'drift layer to block 1200 V: W = 2V_B / E_c', 14, 'start', MUT))
    fx = lin(0, 80, 340, 660)
    for i, (n, eg, ec, w, c, fill) in enumerate(rows):
        y = 80 + i * 74
        o.append(T(40, y + 24, n, 15, 'start', bold=True)); o.append(T(160, y + 24, eg, 14)); o.append(T(260, y + 24, ec, 14))
        o.append(R(340, y, fx(w) - 340, 36, fill, c, 4))
        lab = f'{w:g} µm'
        o.append(T(fx(w) + 10 if w < 60 else fx(w) - 10, y + 24, lab, 14, 'start' if w < 60 else 'end', bold=True))
    o.append(T(360, 316, 'thinner and more heavily doped layer → much lower R_DS(on)', 14, 'middle', NX, bold=True))
    return 336, ''.join(o)


# ---- model-answer sketches ----
def ma_diode_vi():
    o = []
    ox, oy = 360, 170
    o.append(L(30, oy, 700, oy, L2, 1.5, arrow='m')); o.append(L(ox, 330, ox, 20, L2, 1.5, arrow='m'))
    o.append(T(690, oy - 10, 'v_D', 14, 'end', MUT)); o.append(T(ox + 10, 30, 'i_D', 14, 'start', MUT))
    vto = ox + 90
    fwd = [(ox, oy), (vto - 30, oy - 2), (vto, oy - 10), (vto + 30, oy - 50), (vto + 60, oy - 100), (vto + 90, oy - 150)]
    o.append(P(fwd, AC, 3))
    o.append(L(vto, oy - 10, vto, oy + 8, AC, 1.5, dash='3 3')); o.append(T(vto, oy + 26, 'V_TO ≈ 0.8 V', 13))
    o.append(T(vto + 70, oy - 80, 'slope 1/r_d', 13, 'start', NX))
    o.append(T(480, oy + 60, 'v_D = V_TO + i_D r_d', 14, 'start', bold=True))
    rev = [(ox, oy), (160, oy + 10), (110, oy + 16), (96, oy + 140)]
    o.append(P(rev, AC, 3))
    o.append(T(250, oy + 40, 'leakage I_R (enlarged)', 13, 'middle', MUT))
    o.append(L(110, oy + 16, 110, oy - 6, AC, 1.5, dash='3 3')); o.append(T(110, oy - 12, 'V_BR', 14, bold=True))
    o.append(L(170, oy + 10, 170, oy - 6, LV, 1.5, dash='3 3')); o.append(T(186, oy - 12, 'V_RRM', 13, fill=LV))
    o.append(T(110, oy + 155, 'avalanche', 13, 'start', fill=NX))
    return 340, ''.join(o)


def _bjt(x, y, npn=True, flip=False):
    """vertical-bar transistor: base on the left at (x - 40, y), collector up, emitter down (or reversed by flip)"""
    o = [L(x - 40, y, x - 8, y, INK, 2), L(x - 8, y - 22, x - 8, y + 22, INK, 4)]
    s = -1 if flip else 1
    o.append(L(x - 8, y - 10 * s, x + 16, y - 30 * s, INK, 2))
    if npn:
        o.append(L(x - 8, y + 10 * s, x + 16, y + 30 * s, INK, 2, arrow='x'))
    else:
        o.append(L(x + 16, y + 30 * s, x - 6, y + 12 * s, INK, 2, arrow='x'))
    return ''.join(o)


def ma_two_transistor():
    o = []
    # T1 p-n-p: emitter at top (anode), base on the right, collector down
    o.append(T(360, 26, 'anode A', 14, bold=True)); o.append(L(360, 34, 360, 60, INK, 2))
    o.append(L(360, 60, 384, 80, INK, 2, arrow='x'))
    o.append(L(388, 74, 388, 118, INK, 4)); o.append(L(388, 106, 360, 126, INK, 2)); o.append(L(360, 126, 360, 220, INK, 2))
    o.append(T(330, 100, 'T1 p-n-p', 14, 'end', bold=True)); o.append(T(330, 118, '(P1 N1 P2)', 13, 'end', MUT))
    o.append(L(388, 96, 470, 96, INK, 2)); o.append(L(470, 96, 470, 200, INK, 2))
    o.append(T(480, 150, 'I_C2 = base of T1', 13, 'start', LV))
    # T2 n-p-n: collector up to T1 base, base from T1 collector, emitter to cathode
    o.append(L(470, 200, 470, 222, INK, 2)); o.append(L(470, 222, 444, 242, INK, 2))
    o.append(L(440, 236, 440, 280, INK, 4))
    o.append(L(444, 274, 470, 294, INK, 2, arrow='x')); o.append(L(470, 294, 470, 330, INK, 2))
    o.append(L(360, 220, 360, 258, INK, 2)); o.append(L(360, 258, 440, 258, INK, 2))
    o.append(T(256, 186, 'I_C1 = base of T2', 13, 'start', LV))
    o.append(T(490, 270, 'T2 n-p-n', 14, 'start', bold=True)); o.append(T(490, 288, '(N1 P2 N2)', 13, 'start', MUT))
    o.append(dot(360, 258)); o.append(L(200, 258, 356, 258, NX, 2))
    o.append(T(200, 250, 'gate G, I_G', 14, 'start', NX, bold=True))
    o.append(T(470, 350, 'cathode K', 14, bold=True))
    return 362, ''.join(o)


FIG = {
    1: (f1, 'Turn-off of the worked example\'s diode. The current falls at 8 A/µs, passes zero, reaches −8 A after t_a = 1 µs and recovers in t_b = 1 µs; the shaded triangle is the 8 µC recovery charge.',
        'Diode current against time: 10 A, falling at 8 amperes per microsecond through zero to minus 8 amperes, then back to zero; the triangle of recovery charge is shaded with t_a, t_b and t_rr marked.'),
    2: (f2, 'Static V–I characteristic of an SCR (a sketch, not to scale). Gate current lowers the breakover voltage; once the anode current passes the latching current the device stays on the steep conduction line.',
        'SCR characteristic with reverse blocking and breakdown on the left, forward blocking with breakover for zero and positive gate current, and the on-state line with latching and holding currents marked.'),
    3: (f3, 'The UJT trigger circuit of worked example 2 and its capacitor voltage. C charges through R until 13.3 V, the UJT fires, and each discharge puts one pulse across R1 for the SCR gate, about once a millisecond.',
        'UJT relaxation oscillator with 20 V supply, 10 kilohm resistor and 0.1 microfarad capacitor, next to a sawtooth of capacitor voltage between 2 and 13.3 volts and a train of pulses.'),
    4: (f4, 'Impulse commutation in worked example 1. When the auxiliary SCR fires, the main SCR\'s current drops to zero and the capacitor holds it at −200 V; the voltage rises at 5 V/µs, giving 40 µs of reverse bias against the 30 µs the SCR needs.',
        'Upper trace: SCR current 5 A dropping to zero. Lower trace: SCR voltage jumping to minus 200 volts and rising linearly through zero at 40 microseconds; t_c 40 microseconds and t_q 30 microseconds marked.'),
    5: (f5, 'A DIAC-TRIAC lamp dimmer and the lamp voltage of worked example 1. The R-C network delays the DIAC\'s breakover to α = 90°, so the TRIAC conducts only the second half of each half-cycle.',
        'Circuit with 230 volt source, 100 ohm lamp, TRIAC, variable resistor, capacitor and DIAC to the gate; beside it a sine wave with conduction shaded from 90 to 180 and 270 to 360 degrees.'),
    6: (f6, 'MOSFET turn-on in worked example 2. The drain current rises while v_DS is still 200 V; then the gate voltage stays on the 6 V Miller plateau for 30 ns while v_DS falls.',
        'Three traces against time: gate voltage rising to a 6 volt plateau then to 12 volts, drain current rising to 10 amperes, drain voltage falling from 200 volts during the plateau.'),
    7: (f7, 'The switch of the snubber example on its 400 V link. C_s takes the 10 A load current at turn-off, so the voltage rises at 500 V/µs; R_s limits the discharge at the next turn-on and burns 32 W.',
        'DC link with inductive load and freewheeling diode, an IGBT with an R-C snubber of 20 nanofarads and 200 ohms across it, and an isolated gate driver with plus 15 and minus 5 volts feeding a 10 ohm gate resistor.'),
    8: (f8, 'Thermal path of worked example 1. 40 W flows through three thermal resistances in series, so the temperature falls 40 °C, 20 °C and 24 °C from the 124 °C junction to the 40 °C air.',
        'Three thermal resistors in series between junction, case, heat sink and ambient, with temperature bars of 124, 84, 64 and 40 degrees Celsius against a 125 degree limit.'),
    9: (f9, 'Drift-layer thickness needed to block 1200 V, from worked example 2. The higher critical field of SiC and GaN lets the layer be about seven to ten times thinner than in silicon.',
        'Table of band gap and critical field for silicon, SiC and GaN with bars of drift thickness 80, 10.9 and 8 micrometres.'),
}
spec = make_spec(FIG)
