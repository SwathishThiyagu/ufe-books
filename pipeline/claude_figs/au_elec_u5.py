"""Claude's hand-drawn figures for au-elec-u5 (Automotive Electrical and Electronics: vehicle motion control and safety),
one per chapter, drawn from each chapter's own worked example and numbers. Colours are the shell's CSS variables."""
import os, sys, math, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

_T, _Tb, _boxt = T, Tb, boxt


def _sub(s):
    """v_set, c_sky ... drawn as real subscripts, never as underscores"""
    return re.sub(r'([A-Za-zα-ωΔμλ])_([A-Za-z0-9,]+)', r'\1<tspan baseline-shift="sub" font-size="11">\2</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)
def boxt(x, y, w, h, lines, *a, **k): return _boxt(x, y, w, h, [_sub(l) for l in lines], *a, **k)


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


def fmt(v):
    return neg(f'{v:g}')


# ---- 5.1 shift map with the kickdown of the worked example, and the speed chain ----
def f1():
    o = []
    x0, x1, y0, y1 = 80, 420, 40, 250
    fx = lin(0, 120, x0, x1); fy = lin(0, 100, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0, 20, 40, 60, 80, 100, 120], [0, 20, 40, 60, 80, 100], fx, fy,
                  'vehicle speed (km/h)', 'throttle opening (%)', fmt, fmt))
    up = lambda a: 40 + 0.6 * a      # direct → top upshift line
    dn = lambda a: 30 + 0.5 * a      # top → direct downshift line
    o.append(L(fx(up(0)), fy(0), fx(up(100)), fy(100), AC, 2.5))
    o.append(L(fx(dn(0)), fy(0), fx(dn(100)), fy(100), NX, 2.5, dash='7 5'))
    o.append(Tb(fx(up(12)) + 10, fy(12), 'upshift', 13, 'start', fill=AC, bold=True))
    o.append(Tb(fx(dn(44)) - 10, fy(44), 'downshift', 13, 'end', fill=NX, bold=True))
    o.append(L(fx(60), fy(30) - 9, fx(60), fy(90) + 11, LV, 2, arrow='l'))
    o.append(C(fx(60), fy(30), 6, AC)); o.append(C(fx(60), fy(90), 6, NX))
    o.append(Tb(fx(60) + 12, fy(30) + 5, 'A: 30 %, top gear', 13, 'start'))
    o.append(Tb(fx(60) - 12, fy(90) + 5, 'B: 90 %, left of', 13, 'end', fill=NX))
    o.append(Tb(fx(60) - 12, fy(90) + 22, 'the downshift line', 13, 'end', fill=NX))
    o.append(Tb(fx(60) - 12, fy(64), 'kickdown', 13, 'end', fill=LV, bold=True))
    # the speed chain at 60 km/h
    bx = 470
    o.append(T(bx + 117, 52, 'At 60 km/h, wheel radius 0.30 m', 13, fill=MUT))
    o.append(boxt(bx, 66, 234, 46, ['Wheel', '530.5 rpm'], PANEL, AC, 14, True))
    o.append(L(bx + 117, 114, bx + 117, 136, AC, 2, arrow='n'))
    o.append(boxt(bx, 140, 234, 40, ['× final drive 3.50'], PANEL, L2, 14))
    o.append(L(bx + 60, 182, bx + 60, 204, AC, 2, arrow='n'))
    o.append(L(bx + 174, 182, bx + 174, 204, NX, 2, arrow='x'))
    o.append(boxt(bx, 208, 112, 46, ['A: top', '× 0.70'], ACS, AC, 14, True))
    o.append(boxt(bx + 122, 208, 112, 46, ['B: direct', '× 1.00'], NXS, NX, 14, True))
    o.append(L(bx + 56, 256, bx + 56, 278, AC, 2, arrow='n'))
    o.append(L(bx + 178, 256, bx + 178, 278, NX, 2, arrow='x'))
    o.append(boxt(bx, 282, 112, 46, ['engine', '1300 rpm'], PANEL, AC, 14, True))
    o.append(boxt(bx + 122, 282, 112, 46, ['engine', '1857 rpm'], PANEL, NX, 14, True))
    o.append(T(360, 352, 'The kickdown raises engine speed by 557 rpm at the same road speed.', 14, bold=True))
    return 368, ''.join(o)


# ---- 5.2 the ACC gap of the worked example and what braking does to it ----
def f2():
    o = []
    # road strip, 1 m = 9 px from x = 60
    sx = lambda m: 60 + m * 9.0
    o.append(L(40, 96, 700, 96, L2, 1.5)); o.append(L(40, 20, 700, 20, L2, 1.5))
    o.append(L(40, 58, 700, 58, L2, 1.5, dash='12 10'))
    o.append(R(sx(-4.2), 64, 38, 24, ACS, AC, 5)); o.append(T(sx(-2.1), 81, 'host', 12, bold=True))
    o.append(R(sx(60), 64, 38, 24, NXS, NX, 5)); o.append(T(sx(62.1), 81, 'lead', 12, bold=True))
    o.append(T(sx(-2.1), 116, '25 m/s', 13, fill=AC, bold=True)); o.append(T(sx(62.1), 116, '20 m/s', 13, fill=NX, bold=True))
    o.append(L(sx(0), 40, sx(60), 40, AC, 1.8, arrow='n'))
    o.append(Tb(sx(30), 45, 'measured gap d = 60 m', 13, bold=True))
    o.append(L(sx(50), 30, sx(50), 92, LV, 2, dash='5 4'))
    o.append(Tb(sx(50), 136, 'target 2.0 s × 25 m/s = 50 m', 13, 'end', fill=LV))
    o.append(T(sx(55), 32, '+10 m', 13, fill=LV, bold=True))
    # gap against time
    x0, x1, y0, y1 = 80, 690, 170, 370
    fx = lin(0, 12, x0, x1); fy = lin(0, 60, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0, 2, 4, 6, 8, 10, 12], [0, 10, 20, 30, 40, 50, 60], fx, fy,
                  'time from now (s)', 'gap d (m)', fmt, fmt))
    o.append(L(fx(0), fy(60), fx(12), fy(0), NX, 2.5, dash='7 5'))
    a = 1.25
    pts = []
    for i in range(0, 121):
        t = i / 10
        g = 60 - (5 * t - 0.5 * a * t * t) if t <= 4 else 50
        pts.append((fx(t), fy(g)))
    o.append(P(pts, AC, 2.8))
    o.append(L(fx(0), fy(50), fx(12), fy(50), LV, 1.5, dash='4 4'))
    o.append(C(fx(4), fy(50), 6, AC)); o.append(C(fx(12), fy(0), 6, NX))
    o.append(Tb(fx(4) + 10, fy(50) - 12, 'brake at 1.25 m/s²: 20 m/s and 50 m after 4 s', 13, 'start', fill=AC, bold=True))
    o.append(Tb(fx(6.4), fy(22), 'no action: gap gone at 12 s', 13, 'start', fill=NX, bold=True))
    return 424, ''.join(o)


# ---- 5.3 column EPS with the two operating points of the worked example ----
def f3():
    o = []
    o.append(boxt(16, 16, 150, 52, ['Steering wheel', 'driver 4 N·m'], PANEL, AC, 13, True))
    o.append(L(91, 68, 91, 90, AC, 2, arrow='n'))
    o.append(boxt(16, 94, 150, 52, ['Torsion bar', 'twist → torque sensor'], ACS, AC, 13, True))
    o.append(L(91, 146, 91, 168, AC, 2, arrow='n'))
    o.append(boxt(16, 172, 150, 52, ['Column and', 'worm wheel'], PANEL, AC, 13, True))
    o.append(L(91, 224, 91, 246, AC, 2, arrow='n'))
    o.append(boxt(16, 250, 150, 52, ['Pinion, 8 mm', 'drives the rack'], PANEL, AC, 13, True))
    o.append(boxt(232, 172, 160, 52, ['Motor, 0.05 N·m/A', 'worm 16 : 1'], LVS, LV, 13, True))
    o.append(L(230, 198, 170, 198, LV, 2.2, arrow='l'))
    o.append(boxt(232, 60, 160, 64, ['ECU', 'assist map:', 'torque × speed'], PANEL, NX, 13, True))
    o.append(L(170, 120, 228, 104, NX, 1.8, arrow='x'))
    o.append(T(196, 100, 'torque', 12, fill=NX))
    o.append(L(312, 126, 312, 168, NX, 2, arrow='x'))
    o.append(T(320, 152, 'current', 12, 'start', fill=NX))
    o.append(T(312, 40, 'vehicle speed in', 12, fill=MUT))
    o.append(L(312, 44, 312, 56, L2, 1.5, arrow='m'))
    o.append(L(16, 330, 400, 330, AC, 6)); o.append(T(208, 352, 'rack: 44 N·m ÷ 0.008 m = 5500 N at parking', 13))
    # table of the two cases
    tx = 430
    o.append(R(tx, 16, 274, 300, PANEL, L2, 8))
    o.append(T(tx + 137, 42, 'Worked example', 14, bold=True))
    o.append(T(tx + 80, 70, 'parking', 14, fill=AC, bold=True)); o.append(T(tx + 200, 70, '120 km/h', 14, fill=LV, bold=True))
    rows = [('assist at the pinion', '40 N·m', '4 N·m'), ('÷ 16 = motor torque', '2.5 N·m', '0.25 N·m'), ('÷ 0.05 N·m/A = current', '50 A', '5 A')]
    for i, (a, b, c) in enumerate(rows):
        y = 106 + i * 58
        o.append(L(tx + 10, y - 20, tx + 264, y - 20, LN, 1))
        o.append(T(tx + 137, y, a, 13, fill=MUT))
        o.append(T(tx + 80, y + 22, b, 15, fill=AC, bold=True))
        o.append(T(tx + 200, y + 22, c, 15, fill=LV, bold=True))
    o.append(T(tx + 137, 290, 'small motor torque, large', 13, fill=MUT))
    o.append(T(tx + 137, 307, 'assist after the gear', 13, fill=MUT))
    return 368, ''.join(o)


# ---- 5.4 μ–slip curves with the three wheel states of the worked example ----
def mu(lam, c1, c2, c3):
    return c1 * (1 - math.exp(-c2 * lam)) - c3 * lam


DRY, WET = (1.2801, 23.99, 0.52), (0.857, 33.822, 0.347)


def f4():
    o = []
    x0, x1, y0, y1 = 80, 690, 30, 300
    fx = lin(0, 1.0, x0, x1); fy = lin(0, 1.3, y1, y0)
    o.append(R(fx(0.10), y0, fx(0.20) - fx(0.10), y1 - y0, LVS, LVS, 0, sw=0))
    o.append(axes(x0, x1, y0, y1, [0, 0.2, 0.4, 0.6, 0.8, 1.0], [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2], fx, fy,
                  'slip ratio λ (0 = free rolling, 1 = locked)', 'friction coefficient μ', fmt, fmt))
    o.append(P([(fx(i / 200), fy(mu(i / 200, *DRY))) for i in range(201)], AC, 2.8))
    o.append(P([(fx(i / 200), fy(mu(i / 200, *WET))) for i in range(201)], NX, 2.5, dash='8 5'))
    o.append(Tb(fx(0.75), fy(mu(0.75, *DRY)) - 12, 'dry asphalt', 14, fill=AC, bold=True))
    o.append(Tb(fx(0.75), fy(mu(0.75, *WET)) + 26, 'wet asphalt', 14, fill=NX, bold=True))
    o.append(T(fx(0.15), y0 + 18, 'ABS band', 13, fill=LV, bold=True))
    pts = [(0.055, '0.055', 'build', 'start', 8, 0), (0.145, '0.145', 'hold', 'middle', 0, -14), (0.40, '0.40', 'release', 'start', 10, -12)]
    for lam, ls, lab, an, dx, dy in pts:
        m = mu(lam, *DRY)
        o.append(C(fx(lam), fy(m), 6, NX if lab == 'release' else (LV if lab == 'hold' else AC)))
        if lab == 'build':
            o.append(L(fx(lam) + 4, fy(m) + 6, fx(0.12), fy(0.47), L2, 1.2))
            o.append(Tb(fx(0.12) + 4, fy(0.42), f'λ = {ls}: {lab}', 13, 'start', bold=True))
        else:
            o.append(Tb(fx(lam) + dx, fy(m) + dy, f'λ = {ls}: {lab}', 13, an, bold=True))
    o.append(T(fx(0.62), fy(0.30), 'locked wheel: μ ≈ 0.76 dry, no steering', 13, fill=MUT))
    return 346, ''.join(o)


# ---- 5.5 understeer in a left turn and the rear-inner brake pulse ----
def f5():
    o = []
    cx, cy = 220, 225
    # car outline (top view), nose up
    o.append(R(cx - 50, cy - 110, 100, 220, PANEL, AC, 22))
    for (dx, dy, lab) in ((-62, -72, 'FL'), (50, -72, 'FR'), (-62, 52, 'RL'), (50, 52, 'RR')):
        br = lab == 'RL'
        o.append(R(cx + dx, cy + dy, 12, 40, NXS if br else FIGBG, NX if br else INK, 3))
        o.append(T(cx + dx + (-14 if dx < 0 else 28), cy + dy + 25, lab, 13, fill=NX if br else MUT, bold=br))
    o.append(C(cx, cy, 6, INK)); o.append(T(cx + 12, cy + 5, 'CG', 13, 'start', fill=MUT))
    o.append(L(cx, cy - 104, cx, cy + 160, L2, 1.2, dash='4 4'))
    # brake force at RL, pointing back
    o.append(L(cx - 56, cy + 72, cx - 56, cy + 146, NX, 3, arrow='x'))
    o.append(T(cx - 66, cy + 118, 'brake force', 13, 'end', fill=NX, bold=True))
    o.append(T(cx - 66, cy + 136, '2000 N', 13, 'end', fill=NX, bold=True))
    o.append(brace(cx - 56, cx, cy + 160, MUT))
    o.append(T(cx - 28, cy + 186, '0.75 m', 13, fill=MUT))
    o.append(T(cx + 10, cy + 186, '(half of the 1.5 m track)', 13, 'start', fill=MUT))
    # yaw moment arc, anticlockwise (into the left turn)
    o.append(f'<path d="M{cx + 74:.1f},{cy + 10:.1f} A 80 80 0 0 0 {cx + 30:.1f},{cy - 120:.1f}" style="fill:none;stroke:var(--live);stroke-width:3" marker-end="url(#ar-UID-l)"/>')
    o.append(T(cx + 114, cy - 30, 'yaw moment', 13, 'start', fill=LV, bold=True))
    o.append(T(cx + 114, cy - 12, 'into the turn:', 13, 'start', fill=LV, bold=True))
    o.append(T(cx + 114, cy + 6, '2000 × 0.75', 13, 'start', fill=LV))
    o.append(T(cx + 114, cy + 24, '= 1500 N·m', 13, 'start', fill=LV))
    # paths
    o.append(f'<path d="M{cx:.1f},{cy - 112:.1f} Q{cx - 10:.1f},{cy - 190:.1f} {cx - 120:.1f},{cy - 205:.1f}" style="fill:none;stroke:var(--accent);stroke-width:2.2;stroke-dasharray:7 5" marker-end="url(#ar-UID-n)"/>')
    o.append(T(cx - 126, cy - 186, 'path asked for', 13, 'end', fill=AC))
    o.append(f'<path d="M{cx + 10:.1f},{cy - 112:.1f} Q{cx + 20:.1f},{cy - 180:.1f} {cx - 30:.1f},{cy - 208:.1f}" style="fill:none;stroke:var(--line2);stroke-width:2.2" marker-end="url(#ar-UID-m)"/>')
    o.append(T(cx + 22, cy - 190, 'nose runs wide', 13, 'start', fill=MUT))
    # numbers panel
    tx = 470
    o.append(R(tx, 40, 236, 330, PANEL, L2, 8))
    o.append(T(tx + 118, 68, 'Left turn, 20 m/s', 14, bold=True))
    lines = [('desired r_des', '0.278 rad/s'), ('measured r_meas', '0.200 rad/s'), ('error e = r_des − r_meas', '+0.078 rad/s')]
    for i, (a, b) in enumerate(lines):
        y = 100 + i * 56
        o.append(T(tx + 118, y, a, 13, fill=MUT)); o.append(T(tx + 118, y + 22, b, 15, bold=True, fill=NX if i == 2 else INK))
    o.append(L(tx + 12, 274, tx + 224, 274, LN, 1))
    o.append(T(tx + 118, 302, 'e > 0: understeer', 14, fill=NX, bold=True))
    o.append(T(tx + 118, 328, 'brake the rear inner', 13))
    o.append(T(tx + 118, 346, 'wheel (left rear)', 13))
    return 422, ''.join(o)


# ---- 5.6 quarter car and the force a semi-active damper can give ----
def f6():
    o = []
    # quarter car sketch
    o.append(L(30, 24, 190, 24, L2, 2, dash='6 4')); o.append(T(110, 18, 'imaginary sky', 12, fill=MUT))
    o.append(L(110, 26, 110, 58, L2, 1.8, dash='4 4'))
    o.append(boxt(40, 62, 140, 50, ['body (sprung)', 'up 0.08 m/s'], ACS, AC, 13, True))
    o.append(P([(76, 112), (76, 120), (64, 126), (88, 134), (64, 142), (88, 150), (76, 156), (76, 166)], INK, 1.8))
    o.append(R(132, 122, 20, 34, PANEL, NX, 3)); o.append(L(142, 112, 142, 122, NX, 2)); o.append(L(142, 156, 142, 166, NX, 2))
    o.append(T(160, 146, 'damper', 12, 'start', fill=NX))
    o.append(T(56, 146, 'spring', 12, 'end', fill=MUT))
    o.append(boxt(60, 166, 100, 40, ['wheel'], PANEL, AC, 13))
    o.append(P([(110, 206), (110, 212), (100, 218), (120, 226), (100, 234), (110, 240)], INK, 1.8))
    o.append(L(70, 244, 150, 244, L2, 2)); o.append(T(110, 264, 'road', 12, fill=MUT))
    o.append(T(110, 300, 'v_rel = v_body − v_wheel', 13, bold=True))
    o.append(T(110, 320, 'force on body: up is +', 13, fill=MUT))
    # force–v_rel plane
    x0, x1, y0, y1 = 300, 700, 30, 330
    fx = lin(-0.3, 0.3, x0, x1); fy = lin(-900, 900, y1, y0)
    X0, Y0 = fx(0), fy(0)
    reg = [(fx(-0.3), fy(150)), (fx(-0.3), fy(1200 if False else 900)), (fx(-0.225), fy(900)), (X0, Y0)]
    o.append(f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in reg)}" style="fill:var(--live-soft);stroke:none"/>')
    reg2 = [(fx(0.3), fy(-150)), (fx(0.3), fy(-900)), (fx(0.225), fy(-900)), (X0, Y0)]
    o.append(f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in reg2)}" style="fill:var(--live-soft);stroke:none"/>')
    o.append(L(x0, Y0, x1, Y0, L2, 1.5)); o.append(L(X0, y0, X0, y1, L2, 1.5))
    for v in (-0.2, -0.1, 0.1, 0.2):
        o.append(L(fx(v), Y0, fx(v), Y0 + 5, L2, 1.5)); o.append(T(fx(v), Y0 + 20, fmt(v), 12, fill=MUT))
    for F in (-800, -400, 400, 800):
        o.append(L(X0 - 5, fy(F), X0, fy(F), L2, 1.5)); o.append(T(X0 - 8, fy(F) + 4, fmt(F), 12, 'end', fill=MUT))
    o.append(T(x1 - 4, Y0 - 8, 'v_rel (m/s)', 13, 'end', fill=MUT))
    o.append(T(X0 + 8, y0 + 12, 'force on body (N)', 13, 'start', fill=MUT))
    o.append(L(fx(-0.3), fy(150), fx(0.3), fy(-150), LV, 1.8))
    o.append(L(fx(-0.225), fy(900), fx(0.225), fy(-900), LV, 1.8))
    o.append(Tb(fx(-0.2), fy(780), 'c = 4000', 13, 'end', fill=LV)); o.append(Tb(fx(0.27), fy(-135) + 22, 'c = 500', 13, 'middle', fill=LV))
    o.append(C(fx(0.20), fy(-400), 6, AC))
    o.append(L(fx(0.20) - 5, fy(-400) + 5, fx(0.06), fy(-700), AC, 1.2))
    o.append(Tb(fx(0.06), fy(-700) + 16, 'case 1: v_rel = 0.20 m/s,', 13, 'end', fill=AC, bold=True))
    o.append(Tb(fx(0.06), fy(-700) + 34, '−400 N with c = 2000', 13, 'end', fill=AC, bold=True))
    o.append(C(fx(-0.10), fy(-400), 6, NX))
    o.append(Tb(fx(-0.10) - 10, fy(-400) + 5, 'case 2: wanted −400 N', 13, 'end', fill=NX, bold=True))
    o.append(L(fx(-0.10), fy(-400) - 8, fx(-0.10), fy(50) + 9, NX, 1.8, dash='4 4', arrow='x'))
    o.append(C(fx(-0.10), fy(50), 6, NX))
    o.append(Tb(fx(-0.10) - 10, fy(300), 'gets +50 N (c = 500)', 13, 'end', fill=NX, bold=True))
    o.append(T(500, 352, 'shaded: forces a damper can make (it only takes energy out)', 13, fill=LV))
    return 366, ''.join(o)


# ---- 5.7 the 50 km/h barrier crash of the worked example on one time axis ----
def f7():
    o = []
    x0, x1 = 170, 690
    fx = lin(0, 100, x0, x1)
    rows = [('car crush 0.6 m', 0, 86.4, ACS, AC), ('sensing', 0, 10, PANEL, L2), ('decide and fire', 10, 25, NXS, NX),
            ('pretensioner', 25, 35, LVS, LV), ('bag inflating', 25, 50, NXS, NX), ('bag full, venting', 50, 100, PANEL, NX),
            ('occupant ride-down', 50, 86.4, LVS, LV)]
    for i, (lab, a, b, fill, st) in enumerate(rows):
        y = 26 + i * 40
        o.append(T(x0 - 12, y + 19, lab, 13, 'end', bold=(i == 0)))
        o.append(R(fx(a), y + 2, fx(b) - fx(a), 26, fill, st, 4, dash='6 4' if b == 100 else None))
    o.append(T((fx(0) + fx(86.4)) / 2, 47, 'average 161 m/s² (16.4 g)', 13, bold=True))
    for t in (10, 25, 50, 86.4):
        o.append(L(fx(t), 24, fx(t), 312, L2, 1.2, dash='3 4'))
    o.append(xaxis(x0, x1, 312, [0, 10, 25, 50, 75, 100], fx, 'time after impact (ms)'))
    o.append(Tb(fx(86.4), 20, 'car stopped: 86 ms', 13, 'middle', fill=AC, bold=True))
    return 370, ''.join(o)


# ---- 5.8 the AEB chain and the stopping distance of the worked example ----
def f8():
    o = []
    names = ['Sensors', 'Perception', 'Fusion', 'Planning', 'Actuation']
    for i, n in enumerate(names):
        x = 16 + i * 140
        o.append(boxt(x, 20, 118, 40, [n], PANEL if i < 4 else LVS, AC if i < 4 else LV, 14, True))
        if i < 4: o.append(L(x + 120, 40, x + 138, 40, AC, 2, arrow='n'))
    o.append(brace(16, 694, 72, MUT))
    o.append(T(355, 98, 'detection to full braking: 0.5 s delay', 13, fill=MUT))
    # distance bar, 1 m = 20 px
    sx = lambda m: 40 + m * 20.0
    y = 140
    o.append(R(sx(0), y, sx(6.95) - sx(0), 36, NXS, NX, 3))
    o.append(R(sx(6.95), y, sx(19.03) - sx(6.95), 36, ACS, AC, 3))
    o.append(T((sx(0) + sx(6.95)) / 2, y + 23, 'delay 6.95 m', 13, bold=True))
    o.append(T((sx(6.95) + sx(19.03)) / 2, y + 23, 'braking at 8 m/s²: 12.08 m', 13, bold=True))
    o.append(xaxis(sx(0), sx(32), y + 60, [0, 5, 10, 15, 20, 25, 30], sx, 'distance from the car at first detection (m)'))
    o.append(T(sx(0), y - 10, '50 km/h = 13.9 m/s', 13, 'start', fill=MUT))
    o.append(L(sx(19.03), y - 6, sx(19.03), y + 60, AC, 2))
    o.append(Tb(sx(19.03), y - 12, 'stops at 19.03 m', 13, 'middle', fill=AC, bold=True))
    yo = y + 122
    o.append(T(sx(0), yo + 18, 'stopped car first seen at', 13, 'start', fill=MUT))
    for d, c in ((18, NX), (25, LV), (30, LV)):
        o.append(L(sx(d), y + 66, sx(d), yo, L2, 1.2, dash='3 4'))
        o.append(R(sx(d) - 6, yo, 12, 28, c + '-soft)' if False else FIGBG, c, 3, sw=2.5))
    o.append(T(sx(18) + 8, yo + 50, '18 m: hits at 4.05 m/s (14.6 km/h)', 13, 'end', fill=NX, bold=True))
    o.append(T(sx(25), yo + 50, '25 m: 5.97 m spare', 13, 'middle', fill=LV, bold=True))
    o.append(T(sx(30) + 8, yo + 72, '30 m: 10.97 m spare', 13, 'end', fill=LV, bold=True))
    return yo + 88, ''.join(o)


# ---- 5.9 the speed loop of the worked example and its step response ----
def f9():
    o = []
    o.append(C(70, 52, 14, PANEL)); o.append(f'<circle cx="70" cy="52" r="14" style="fill:var(--panel);stroke:var(--accent);stroke-width:2"/>')
    o.append(T(70, 57, 'Σ', 15, bold=True))
    o.append(T(18, 38, 'v_ref', 13, 'start'))
    o.append(L(16, 52, 54, 52, AC, 2, arrow='n'))
    o.append(L(84, 52, 120, 52, AC, 2, arrow='n')); o.append(T(102, 44, 'e', 13, fill=MUT))
    o.append(boxt(124, 26, 190, 52, ['PI controller', 'K_p = 500, T_i = 15 s'], ACS, AC, 13, True))
    o.append(L(316, 52, 380, 52, AC, 2, arrow='n')); o.append(T(348, 44, 'F (N)', 13, fill=MUT))
    o.append(boxt(384, 26, 196, 52, ['car: 0.01 ÷ (15s + 1)', 'm = 1500 kg, b = 100'], PANEL, AC, 13, True))
    o.append(L(582, 52, 700, 52, AC, 2, arrow='n')); o.append(T(690, 44, 'v', 13, 'end'))
    o.append(P([(640, 52), (640, 100), (70, 100), (70, 70)], L2, 2))
    o.append(L(70, 74, 70, 68, L2, 2, arrow='m')); o.append(T(58, 86, '−', 15, 'end', bold=True))
    # step response 25 → 30 m/s
    x0, x1, y0, y1 = 80, 690, 140, 360
    fx = lin(0, 15, x0, x1); fy = lin(24, 31, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0, 3, 6, 9, 12, 15], [24, 25, 26, 27, 28, 29, 30, 31], fx, fy,
                  'time after the reference steps from 25 to 30 m/s (s)', 'speed v (m/s)', fmt, fmt))
    lam = 3.0
    a = [(fx(i / 20), fy(25 + 5 * (1 - math.exp(-(i / 20) / lam)))) for i in range(301)]
    b = [(fx(i / 20), fy(25 + 5 * (1 - (1 + (i / 20) / lam) * math.exp(-(i / 20) / lam)))) for i in range(301)]
    o.append(L(fx(0), fy(30), fx(15), fy(30), L2, 1.2, dash='4 4'))
    o.append(P(a, AC, 2.8)); o.append(P(b, LV, 2.6, dash='8 5'))
    o.append(C(fx(3), fy(28.16), 6, AC)); o.append(C(fx(3), fy(26.32), 6, LV))
    o.append(Tb(fx(3) + 12, fy(28.16) + 18, '28.16 m/s at 3 s', 13, 'start', fill=AC, bold=True))
    o.append(Tb(fx(3) + 12, fy(26.32) + 18, '26.32 m/s with the reference model', 13, 'start', fill=LV, bold=True))
    o.append(Tb(fx(10.5), fy(28.6), 'no overshoot either way', 13, 'middle', fill=MUT))
    return 412, ''.join(o)


FIG = {
    1: (f1, 'The worked example on the shift map. At 60 km/h and 30 % throttle the car sits right of the downshift line, in top gear; pressing to 90 % moves it left of that line, so the TCU kicks down to direct gear and the engine speed rises from 1300 to 1857 rpm.',
        'Shift map of throttle against speed with an upshift line and a dashed downshift line; point A at 60 km/h and 30 per cent, point B at 90 per cent; beside it the speed chain from wheel 530.5 rpm through final drive 3.50 to engine 1300 or 1857 rpm.'),
    2: (f2, 'The ACC gap of the worked example. The lead car is 60 m ahead, 10 m beyond the 50 m target; if nothing changes the gap closes in 12 s, while a steady 1.25 m/s² brake settles the host at 20 m/s and 50 m after 4 s.',
        'Road strip with host at 25 metres per second and lead car at 20, gap 60 metres and target line at 50; below, a plot of gap against time with a straight line to zero at 12 seconds and a curve that levels at 50 metres after 4 seconds.'),
    3: (f3, 'Column EPS with the numbers of the worked example. The torsion bar tells the ECU how hard the driver turns; the 16 : 1 worm multiplies a small motor torque into the assist at the pinion.',
        'Steering wheel, torsion bar, column and pinion in a column; a motor with a 16 to 1 worm drives the column; the ECU reads torque and speed and sets current; a table gives 40 and 4 newton metres of assist, 2.5 and 0.25 newton metres of motor torque, 50 and 5 amperes.'),
    4: (f4, 'Friction against slip for dry and wet asphalt, with the three wheel states of the worked example. Below the band ABS builds pressure, inside it holds, and past the peak it releases.',
        'Two curves of friction coefficient against slip ratio peaking near 0.17 for dry and 0.13 for wet asphalt, with a shaded band from 0.10 to 0.20 and points at slip 0.055, 0.145 and 0.40.'),
    5: (f5, 'The understeering car of the worked example, seen from above in a left turn. Braking the left rear wheel puts a 1500 N·m yaw moment into the turn and pulls the nose back towards the path the driver asked for.',
        'Top view of a car with the left rear wheel braked by 2000 newtons at 0.75 metres from the centre line, an arrow for the yaw moment into the turn, the asked-for path and the wide path, and a panel with desired, measured and error yaw rates.'),
    6: (f6, 'One corner of the worked example. A semi-active damper can only make forces in the shaded areas, so it delivers the skyhook force of 400 N downward in case 1 but not in case 2, where it falls back to minimum damping.',
        'Quarter car with body, spring, damper, wheel and tyre, and a plot of force against relative velocity with the shaded reachable areas between damping 500 and 4000, a reachable point at 0.20 and minus 400 newtons and an unreachable point at minus 0.10.'),
    7: (f7, 'The 50 km/h barrier crash of the worked example on one time axis. The bag is full by about 50 ms, well before the car stops at 86 ms, so the belted occupant rides down on a bag that is already venting.',
        'Timeline bars from 0 to 100 milliseconds: car crush to 86, sensing to 10, decision and fire to 25, pretensioner 25 to 35, bag inflating 25 to 50, bag full from 50, occupant ride-down 50 to 86.'),
    8: (f8, 'The AEB chain and the stopping distance of the worked example at 50 km/h. The car needs 19.03 m from first detection, so it stops short of an obstacle at 25 m or 30 m but still hits one at 18 m, at 4.05 m/s.',
        'Five boxes from sensors to actuation with a 0.5 second delay, above a distance bar of 6.95 metres delay and 12.08 metres braking ending at 19.03, with obstacle marks at 18, 25 and 30 metres.'),
    9: (f9, 'The speed loop of the worked example and its response when the reference steps from 25 to 30 m/s. Lambda tuning gives a first-order rise with λ = 3 s; the reference model makes the start gentler, and neither curve overshoots.',
        'Block diagram from v ref through a summing point, PI block and car block back to the summing point; below, two rising curves of speed against time reaching 28.16 and 26.32 metres per second at 3 seconds and levelling at 30.'),
}
spec = make_spec(FIG)
