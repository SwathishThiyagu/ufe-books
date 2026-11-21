"""Claude's hand-drawn figures for me-ic-u2 (Internal Combustion Engines: fuel supply and ignition systems), one per chapter, drawn from each
chapter's own worked example and numbers. Colours are the shell's CSS variables."""
import os, sys, math, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

_T, _Tb, _boxt = T, Tb, boxt


def _sub(s):
    """t_b, A_t ... drawn as real subscripts, never as underscores"""
    return re.sub(r'([A-Za-zα-ωΔ])_([A-Za-z0-9]+)', r'\1<tspan baseline-shift="sub" font-size="11">\2</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)
def boxt(x, y, w, h, lines, *a, **k): return _boxt(x, y, w, h, [_sub(l) for l in lines], *a, **k)


def poly(pts, c=AC, w=2, fill='none', dash=None):
    d = f';stroke-dasharray:{dash}' if dash else ''
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" style="fill:{fill};stroke:{c};stroke-width:{w}{d};stroke-linejoin:round"/>'


def path(d, c=AC, w=2, fill='none', dash=None, arrow=None):
    da = f';stroke-dasharray:{dash}' if dash else ''
    m = f' marker-end="url(#ar-UID-{arrow})"' if arrow else ''
    return f'<path d="{d}" style="fill:{fill};stroke:{c};stroke-width:{w}{da}"{m}/>'


def coil(x, y0, y1, n=5, r=9, c=AC, side=1):
    """a winding drawn as n bumps along a vertical line at x (bumps to the right if side=1)"""
    h = (y1 - y0) / n
    d = f'M{x:.1f},{y0:.1f}'
    for i in range(n):
        d += f' a{r},{h / 2:.1f} 0 0 {1 if side > 0 else 0} 0,{h:.1f}'
    return path(d, c, 2)


FIG = {}


# ---- 2.1 a simple carburettor with the worked example's numbers ----
def f1():
    o = []
    cx, top, bot, thr = 300, 86, 430, 205
    lw = [(cx - 80, top), (cx - 80, thr - 62), (cx - 36, thr), (cx - 80, thr + 62), (cx - 80, bot)]
    rw = [(cx + 80, top), (cx + 80, thr - 62), (cx + 36, thr), (cx + 80, thr + 62), (cx + 80, bot)]
    o.append(boxt(cx - 110, 18, 220, 46, ['air filter (paper element)'], fill=PANEL, stroke=MUT, size=14))
    o.append(L(cx, 66, cx, 104, LV, 2.5, arrow='l'))
    o.append(T(cx + 96, 92, 'air 0.030 kg/s', 13, 'start', LV, bold=True))
    o.append(P(lw, INK, 3)); o.append(P(rw, INK, 3))
    # choke (open: plate edge-on) and throttle (part open)
    o.append(L(cx, 112, cx, 140, MUT, 4)); o.append(C(cx, 126, 4, MUT))
    o.append(T(cx - 96, 131, 'choke (open)', 13, 'end', MUT))
    o.append(L(cx - 62, 392, cx + 62, 362, AC, 4)); o.append(C(cx, 377, 4, AC))
    o.append(T(cx - 96, 382, 'throttle', 13, 'end', AC, bold=True))
    o.append(T(cx - 96, 400, '(sets the power)', 13, 'end', MUT))
    o.append(L(cx, 405, cx, 446, LV, 2.5, arrow='l'))
    o.append(T(cx + 14, 446, 'mixture to inlet manifold, A/F = 15', 13, 'start', LV))
    # throat labels
    o.append(L(cx - 38, thr, cx - 96, thr, L2, 1.2, dash='3 3'))
    o.append(T(cx - 100, thr - 8, 'venturi throat', 13, 'end', INK, bold=True))
    o.append(T(cx - 100, thr + 10, 'd = 19.1 mm, 105 m/s', 13, 'end'))
    o.append(T(cx - 100, thr + 28, 'depression 0.065 bar', 13, 'end', NX, bold=True))
    # float chamber
    fx0, fx1, fy0, fy1, lev = 500, 696, 150, 340, 225
    o.append(R(fx0, lev, fx1 - fx0, fy1 - lev, ACS, 'none', 0, 0))
    o.append(R(fx0, fy0, fx1 - fx0, fy1 - fy0, 'none', INK, 6, 3))
    o.append(T((fx0 + fx1) / 2, fy0 - 50, 'float chamber', 14, 'middle', INK, bold=True))
    o.append(T((fx0 + fx1) / 2, fy0 - 32, '(vented: atmospheric)', 13, 'middle', MUT))
    o.append(R(560, lev - 18, 64, 34, PANEL, INK, 6))
    o.append(T(592, lev + 4, 'float', 13))
    o.append(L(592, lev - 18, 592, fy0 + 16, INK, 2)); o.append(poly([(584, fy0 + 16), (600, fy0 + 16), (592, fy0 + 2)], INK, 2, PANEL))
    o.append(T(604, fy0 + 40, 'needle valve', 13, 'start', MUT))
    o.append(L(fx1 + 18, fy0 + 8, 600, fy0 + 8, AC, 2, arrow='n')); o.append(T(712, fy0 - 8, 'petrol in', 13, 'end', AC))
    o.append(L(fx0, lev, cx - 4, lev, AC, 1.5, dash='5 4'))
    o.append(T(fx0 + 8, lev + 44, 'petrol level', 13, 'start', AC))
    # main jet and nozzle
    o.append(P([(fx0 + 30, fy1 - 16), (fx0 - 6, fy1 - 16), (cx + 6, fy1 - 16), (cx + 6, 214)], AC, 5))
    o.append(R(fx0 - 26, fy1 - 26, 18, 20, AC, AC, 2))
    o.append(T(fx0 - 17, fy1 + 20, 'main jet d = 1.08 mm', 13, 'middle', AC, bold=True))
    o.append(T(fx0 - 17, fy1 + 38, 'petrol 0.002 kg/s', 13, 'middle', AC))
    o.append(C(cx + 6, 211, 4, AC))
    o.append(T(cx + 6, 194, 'nozzle tip', 13, 'middle', AC))
    o.append(L(cx + 96, 211, cx + 96, lev, NX, 1.6)); o.append(L(cx + 90, 211, cx + 102, 211, NX, 1.6)); o.append(L(cx + 90, lev, cx + 102, lev, NX, 1.6))
    o.append(T(cx + 106, 222, 'z = 5 mm', 13, 'start', NX, bold=True))
    return 470, ''.join(o)


FIG[1] = (f1, 'The simple carburettor of the second worked example. Air passing the 19.1 mm throat at 105 m/s makes a 0.065 bar depression, which lifts '
              'petrol from the float chamber through the 1.08 mm main jet and out of the nozzle tip, 5 mm above the petrol level; the throttle below sets how much mixture enters.',
          'Section through a simple downdraught carburettor: air filter, open choke, venturi throat of 19.1 millimetres, fuel nozzle tip 5 millimetres above the '
          'petrol level in a float chamber with float and needle valve, main jet of 1.08 millimetres, and a throttle butterfly below the venturi.')


# ---- a crank-angle strip (used for 2.2 and 2.11) ----
def strip(rows, lo, hi, x0=150, x1=690, y0=70, gap=96, ticks=5, top_note=None):
    o = []
    fx = lin(lo, hi, x0, x1)
    yb = y0 + gap * len(rows) - 30
    for v in range(lo, hi + 1, ticks):
        X = fx(v)
        o.append(L(X, y0 - 22, X, yb, LN, 1))
        lab = 'TDC' if v == 0 else f'{abs(v)}°'
        o.append(T(X, yb + 20, lab, 13, 'middle', INK if v == 0 else MUT, bold=(v == 0)))
    o.append(L(fx(0), y0 - 30, fx(0), yb, INK, 2))
    o.append(T(fx(lo), yb + 42, '← before TDC', 13, 'start', MUT)); o.append(T(fx(hi), yb + 42, 'after TDC →', 13, 'end', MUT))
    for i, r in enumerate(rows):
        y = y0 + i * gap
        o.append(T(x0 - 14, y + 18, r['name'], 14, 'end', INK, bold=True))
        if r.get('sub'): o.append(T(x0 - 14, y + 36, r['sub'], 13, 'end', MUT))
        for a, b, col, lab, dash in r['bars']:
            X0, X1 = fx(a), fx(b)
            o.append(R(X0, y + 4, X1 - X0, 24, col if not dash else 'none', col, 4, 2, dash))
            if lab: o.append(Tb((X0 + X1) / 2, y + 48, lab, 13, 'middle', col, bold=True))
        for v, lab in r.get('marks', []):
            o.append(L(fx(v), y - 6, fx(v), y + 34, INK, 2)); o.append(T(fx(v), y - 10, lab, 13, 'middle', INK))
    return yb + 54, ''.join(o)


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


# ---- 2.2 injection timing, lag and duration at two speeds ----
def f2():
    rows = [{'name': '2000 rpm', 'sub': '12 000 °/s', 'marks': [(-20, 'delivery starts')],
             'bars': [(-20, -14, NX, 'lag 6°', True), (-14, 4, AC, 'nozzle open 18° (1.5 ms)', False)]},
            {'name': '3000 rpm', 'sub': '18 000 °/s', 'marks': [(-20, 'delivery starts')],
             'bars': [(-20, -11, NX, 'lag 9°', True), (-11, 16, AC, 'nozzle open 27° (1.5 ms)', False)]}]
    h, body = strip(rows, -25, 20, y0=56, gap=104)
    return h, body


FIG[2] = (f2, 'The second worked example on a crank-angle scale. The pump starts delivery 20° before TDC at both speeds, but the 0.5 ms pressure-wave lag '
              'costs 6° at 2000 rpm and 9° at 3000 rpm, so the spray starts later and ends later as speed rises unless the timing is advanced.',
          'Two horizontal crank-angle bars. At 2000 rpm a 6 degree lag from 20 to 14 degrees before TDC is followed by an 18 degree injection ending 4 degrees '
          'after TDC. At 3000 rpm a 9 degree lag is followed by a 27 degree injection ending 16 degrees after TDC.')


# ---- 2.3 jerk pump element: start and end of delivery ----
def f3():
    o = []
    def panel(x, lift, title, sub, end):
        bx0, bx1, port = x + 70, x + 190, 250
        base = port - lift
        # barrel walls with ports
        for X in (bx0, bx1):
            o.append(L(X, 96, X, port - 9, INK, 4)); o.append(L(X, port + 9, X, 420, INK, 4))
        o.append(T(bx0 - 10, port + 5, 'inlet port', 13, 'end', MUT))
        o.append(T(bx1 + 10, port + 5, 'spill port', 13, 'start', NX if end else MUT, bold=end))
        # delivery valve at top
        o.append(R(bx0, 82, bx1 - bx0, 14, PANEL, INK, 3))
        o.append(poly([(x + 118, 82), (x + 142, 82), (x + 130, 64)], INK, 2, PANEL))
        o.append(L(x + 130, 62, x + 130, 34, AC if not end else L2, 2.5, arrow='n' if not end else None))
        o.append(T(x + 140, 44, 'to injector' if not end else 'delivery valve shuts', 13, 'start', AC if not end else MUT))
        # fuel above the plunger
        o.append(R(bx0 + 2, 96, bx1 - bx0 - 4, base - 96, ACS, 'none', 0, 0))
        # plunger with vertical groove and helix
        o.append(R(bx0 + 3, base, bx1 - bx0 - 6, 420 - base, PANEL, AC, 2))
        o.append(L(bx0 + 40, base, bx0 + 40, base + 30, AC, 2)); o.append(L(bx0 + 52, base, bx0 + 52, base + 30, AC, 2))
        hx0, hy0, hx1, hy1 = bx0 + 52, base + 30, bx1 - 3, base + (60 if end else 78)
        o.append(poly([(bx0 + 40, base + 30), (hx0, hy0), (hx1, hy0 + (hy1 - hy0)), (hx1, hy1 + 34), (bx0 + 40, base + 64)], AC, 2, ACS))
        o.append(T(x + 130, 404, 'plunger', 13, 'middle', INK, bold=True))
        o.append(T(x + 150, base + (112 if end else 128), 'helix', 13, 'middle', AC, bold=True))
        if end:
            o.append(L(bx1 - 2, port, bx1 + 2, port, NX, 6))
            o.append(L(bx1 + 6, port + 22, bx1 + 54, port + 46, NX, 2, arrow='x'))
            o.append(T(bx1 + 10, port + 66, 'fuel spills back', 13, 'start', NX))
        o.append(T(x + 130, 456, title, 14, 'middle', INK, bold=True))
        o.append(T(x + 130, 474, sub, 13, 'middle', MUT))
        return base
    b1 = panel(20, 0, '1. Top edge covers the ports', 'delivery starts', False)
    b2 = panel(370, 60, '2. Helix uncovers the spill port', 'delivery ends', True)
    # effective stroke bracket between the two plunger tops
    X = 350
    o.append(L(X - 10, b1, X + 10, b1, NX, 2)); o.append(L(X - 10, b2, X + 10, b2, NX, 2)); o.append(L(X, b2, X, b1, NX, 2))
    o.append(T(X, b2 - 26, 'effective', 13, 'middle', NX, bold=True)); o.append(T(X, b2 - 10, 'stroke 3 mm', 13, 'middle', NX, bold=True))
    o.append(T(360, 500, 'd = 8 mm:  V = π × 8² ÷ 4 × 3 = 150.8 mm³ per injection; turning the plunger moves the helix', 13, 'middle', INK))
    return 512, ''.join(o)


FIG[3] = (f3, 'One element of an in-line jerk pump at the start and the end of delivery. Delivery runs only while the plunger rises the 3 mm effective '
              'stroke from covering the ports to its helix uncovering the spill port, which gives the first worked example’s 150.8 mm³.',
          'Two side-by-side sections of a jerk pump barrel and plunger. Left: the plunger top has just covered the inlet and spill ports and fuel flows up '
          'through the delivery valve to the injector. Right: the plunger has risen 3 millimetres and its helix has uncovered the spill port, so fuel spills back.')


# ---- 2.4 common rail layout with the example's numbers ----
def f4():
    o = []
    o.append(boxt(20, 40, 110, 50, ['fuel tank'], fill=PANEL, stroke=MUT))
    o.append(boxt(160, 40, 120, 50, ['lift pump', 'and filter'], fill=PANEL, stroke=MUT, size=13))
    o.append(boxt(310, 34, 160, 62, ['high-pressure', 'pump (engine)'], fill=PANEL, stroke=AC, size=13))
    o.append(L(130, 65, 158, 65, MUT, 2, arrow='m')); o.append(L(280, 65, 308, 65, MUT, 2, arrow='m'))
    o.append(T(220, 112, 'a few bar', 13, 'middle', MUT))
    # rail
    o.append(R(150, 160, 440, 30, ACS, AC, 14, 3))
    o.append(T(370, 181, 'common rail: 1200 bar (raised to 1800 bar)', 13, 'middle', INK, bold=True))
    o.append(L(390, 96, 390, 158, AC, 3, arrow='n'))
    # sensor and pressure control valve
    o.append(boxt(600, 150, 106, 50, ['pressure', 'sensor'], fill=PANEL, stroke=NX, size=13))
    o.append(L(590, 175, 600, 175, NX, 2))
    o.append(boxt(14, 150, 120, 50, ['pressure', 'control valve'], fill=PANEL, stroke=MUT, size=13))
    o.append(L(150, 175, 134, 175, MUT, 2)); o.append(L(74, 150, 74, 92, MUT, 2, arrow='m', dash='5 4'))
    o.append(T(80, 126, 'return', 13, 'start', MUT))
    # injectors
    xs = [210, 310, 410, 510]
    for i, X in enumerate(xs):
        o.append(L(X, 190, X, 238, AC, 3))
        o.append(R(X - 14, 238, 28, 58, PANEL, AC, 5))
        o.append(poly([(X - 8, 296), (X + 8, 296), (X, 310)], AC, 2, AC))
        o.append(T(X, 272, f'{i + 1}', 13, 'middle', AC, True))
    o.append(T(190, 272, 'injectors', 13, 'end', AC, True))
    o.append(T(360, 474, 'open 1.0 ms → 30 mm³ at 1200 bar;  0.81 ms → 30 mm³ at 1800 bar', 13, 'middle', AC, bold=True))
    # ECU
    o.append(boxt(250, 392, 220, 56, ['ECU'], fill=NXS, stroke=NX, size=16, bold_first=True))
    o.append(path('M653,200 L653,420 L472,420', NX, 2, dash='6 4', arrow='x'))
    o.append(T(646, 300, 'rail pressure', 13, 'end', NX)); o.append(T(646, 318, 'signal', 13, 'end', NX))
    o.append(path('M248,420 L60,420 L60,202', NX, 2, dash='6 4', arrow='x'))
    o.append(T(66, 300, 'pressure', 13, 'start', NX)); o.append(T(66, 318, 'command', 13, 'start', NX))
    for X in xs:
        o.append(L(X, 314, X, 360, NX, 1.4, dash='3 4'))
    o.append(L(210, 360, 510, 360, NX, 1.4, dash='3 4')); o.append(L(360, 390, 360, 360, NX, 1.4, dash='3 4'))
    o.append(T(370, 380, 'opens each injector', 13, 'start', NX))
    o.append(T(360, 494, 'speed, pedal, air mass and coolant temperature also go to the ECU', 13, 'middle', MUT))
    return 508, ''.join(o)


FIG[4] = (f4, 'A four-cylinder common rail. The pump keeps the rail at the pressure the ECU sets, the sensor reports it, and the ECU opens each injector '
              'for a time: 1.0 ms gives 30 mm³ at 1200 bar, but at 1800 bar the same fuel needs only 0.81 ms, as the second worked example shows.',
          'Block layout of a common rail system: fuel tank, lift pump and filter, engine-driven high-pressure pump, a rail at 1200 bar with a pressure sensor and '
          'a pressure control valve returning to the tank, four injectors under the rail, and an ECU linked by dashed signal lines to the sensor, the valve and each injector.')


# ---- 2.5 MPFI layout and one cylinder's pulse ----
def f5():
    o = []
    # air path along the top
    o.append(boxt(14, 40, 104, 46, ['air filter'], fill=PANEL, stroke=MUT, size=13))
    o.append(boxt(140, 40, 116, 46, ['air-flow sensor'], fill=PANEL, stroke=NX, size=13))
    o.append(boxt(278, 40, 112, 46, ['throttle + TPS'], fill=PANEL, stroke=NX, size=13))
    o.append(boxt(412, 40, 126, 46, ['inlet port'], fill=PANEL, stroke=LV, size=13))
    o.append(boxt(560, 30, 146, 66, ['cylinder', '0.35 g air/cycle'], fill=PANEL, stroke=INK, size=13))
    for a, b in ((118, 140), (256, 278), (390, 412), (538, 560)):
        o.append(L(a, 63, b - 2, 63, LV, 2, arrow='l'))
    # injector into port
    o.append(R(460, 110, 30, 50, PANEL, AC, 5)); o.append(poly([(468, 110), (482, 110), (475, 90)], AC, 2, AC))
    o.append(T(452, 140, 'injector', 13, 'end', AC, bold=True))
    # fuel line
    o.append(boxt(14, 170, 130, 46, ['tank pump'], fill=PANEL, stroke=MUT, size=13))
    o.append(boxt(200, 170, 200, 46, ['rail + regulator, 3 bar'], fill=ACS, stroke=AC, size=13))
    o.append(L(144, 193, 198, 193, AC, 2, arrow='n')); o.append(path('M400,193 L475,193 L475,162', AC, 2, arrow='n'))
    # ECU and sensors
    o.append(boxt(250, 262, 220, 54, ['ECU'], fill=NXS, stroke=NX, size=16, bold_first=True))
    for i, s_ in enumerate(('air mass, throttle', 'coolant temperature', 'crank and cam position', 'exhaust oxygen')):
        o.append(T(40, 254 + i * 18, s_, 13, 'start', MUT))
    o.append(L(210, 282, 248, 282, NX, 1.4, dash='5 4', arrow='x'))
    o.append(path('M470,289 L520,289 L520,140 L492,140', NX, 2, arrow='x'))
    o.append(T(528, 230, 'pulse', 13, 'start', NX, bold=True))
    # pulse strip: 40 ms cycle at 3000 rpm
    x0, x1, y = 60, 660, 372
    fx = lin(0, 40, x0, x1)
    o.append(L(x0, y + 30, x1, y + 30, L2, 1.5))
    for v in range(0, 41, 10):
        o.append(L(fx(v), y + 30, fx(v), y + 36, L2, 1.5)); o.append(T(fx(v), y + 52, f'{v} ms', 13, 'middle', MUT))
    o.append(R(fx(0), y, fx(0.8) - fx(0), 30, 'none', NX, 2, 2, '4 3'))
    o.append(R(fx(0.8), y, fx(10.32) - fx(0.8), 30, AC, AC, 2, 2))
    o.append(T(fx(10.32) + 8, y + 20, 'open 10.32 ms = 0.8 ms dead time + 9.52 ms fuel (0.0238 g)', 13, 'start', INK))
    o.append(T(x0, y - 12, 'one cycle at 3000 rpm = 40 ms; the injector is open 26 % of it', 13, 'start', INK, bold=True))
    return 440, ''.join(o)


FIG[5] = (f5, 'Multi-point injection: sensors feed the ECU, which opens each port injector on a 3 bar rail. For the second worked example the ECU turns 0.35 g '
              'of air per cylinder into 0.0238 g of petrol and a 10.32 ms pulse, about a quarter of the 40 ms cycle at 3000 rpm.',
          'Layout of multi-point fuel injection with the air path, a port injector fed by a 3 bar rail and regulator, an ECU reading air mass, throttle, coolant, '
          'crank, cam and oxygen signals, and below it a 40 millisecond timeline with a 0.8 millisecond dead time and a 9.52 millisecond fuel pulse.')


# ---- 2.6 GDI: homogeneous and stratified injection ----
def f6():
    o = []
    def cyl(x, piston_y, mode):
        cx = x + 170
        o.append(L(x + 60, 86, x + 60, 400, INK, 3)); o.append(L(x + 280, 86, x + 280, 400, INK, 3))
        o.append(P([(x + 60, 86), (x + 120, 60), (x + 220, 60), (x + 280, 86)], INK, 3))
        # spark plug in the centre
        o.append(R(cx - 8, 30, 16, 32, PANEL, INK, 3)); o.append(L(cx, 62, cx, 74, INK, 3))
        o.append(T(cx + 14, 40, 'spark plug', 13, 'start', MUT))
        # side injector
        o.append(poly([(x + 52, 104), (x + 30, 92), (x + 30, 120)], AC, 2, AC))
        o.append(T(x + 2, 146, 'injector', 13, 'start', AC, bold=True))
        # piston with bowl
        o.append(path(f'M{x + 62},{piston_y} L{cx - 50},{piston_y} Q{cx},{piston_y + 40} {cx + 50},{piston_y} L{x + 278},{piston_y} L{x + 278},{piston_y + 60} L{x + 62},{piston_y + 60} Z', INK, 2, PANEL))
        o.append(T(cx, piston_y + 48, 'piston', 13, 'middle', MUT))
        if mode == 'h':
            for dy in (-14, 0, 14, 28):
                o.append(L(x + 54, 106, x + 200, 160 + dy * 3, AC, 1.6, dash='2 5'))
            o.append(R(x + 66, 150, 208, piston_y - 158, ACS, 'none', 0, 0))
            o.append(Tb(cx, 214, 'uniform mixture, A/F ≈ 14.7', 13, 'middle', INK, True))
            o.append(L(x + 318, 300, x + 318, 360, LV, 2.5, arrow='l')); o.append(T(x + 318, 380, 'piston', 13, 'middle', LV)); o.append(T(x + 318, 396, 'down', 13, 'middle', LV))
        else:
            o.append(path(f'M{x + 54},{106} Q{cx - 40},{piston_y + 30} {cx},{piston_y + 16}', AC, 3, arrow='n'))
            o.append(f'<ellipse cx="{cx + 4}" cy="{(76 + piston_y) / 2 + 8:.1f}" rx="44" ry="{(piston_y - 76) / 2 + 2:.1f}" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:1.5;stroke-dasharray:4 3"/>')
            o.append(T(cx + 4, 112, 'rich', 13, 'middle', AC, bold=True)); o.append(T(cx + 4, 128, 'cloud', 13, 'middle', AC, bold=True))
            o.append(T(x + 250, 150, 'lean', 13, 'middle', MUT))
            o.append(L(x + 318, 290, x + 318, 230, LV, 2.5, arrow='l')); o.append(T(x + 318, 198, 'piston', 13, 'middle', LV)); o.append(T(x + 318, 214, 'up', 13, 'middle', LV))
    cyl(0, 330, 'h')
    cyl(370, 170, 's')
    o.append(T(170, 430, 'Homogeneous: inject in the intake stroke', 14, 'middle', INK, True))
    o.append(T(170, 448, 'medium and full load', 13, 'middle', MUT))
    o.append(T(540, 430, 'Stratified: inject late in compression', 14, 'middle', INK, True))
    o.append(T(540, 448, '12 mg in 1.2 ms = 14.4°, from 49° to 35° before TDC', 13, 'middle', MUT))
    o.append(T(360, 476, 'rail 50 to 200 bar; evaporation in the cylinder cools the charge by up to about 21 K', 13, 'middle', INK))
    return 490, ''.join(o)


FIG[6] = (f6, 'The two GDI charge modes. Injected during the intake stroke, the fuel spreads into a uniform mixture; injected late in compression, as in '
              'the second worked example, it forms a rich cloud at the plug while the rest of the cylinder stays lean.',
          'Two cylinder sections with a side injector and a central spark plug. Left: the piston is low in the intake stroke and the spray fills the cylinder '
          'with a uniform mixture. Right: the piston is near top dead centre, the spray is turned by the piston bowl into a rich cloud around the spark plug, with lean air elsewhere.')


# ---- 2.7 five jets in a bowl at 0.5 ms ----
def f7():
    o = []
    cx, cy, sc = 250, 240, 4.0
    rb = 35 * sc
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{rb}" style="fill:var(--panel);stroke:var(--ink);stroke-width:3"/>')
    o.append(T(cx, cy + rb + 24, 'piston bowl, radius 35 mm (top view)', 13, 'middle', MUT))
    S = 44.1 * sc
    half = math.radians(6)
    for i in range(5):
        a = math.radians(-90 + 72 * i)
        tip = (cx + S * math.cos(a), cy + S * math.sin(a))
        l = (cx + S * math.cos(a - half), cy + S * math.sin(a - half)); r = (cx + S * math.cos(a + half), cy + S * math.sin(a + half))
        o.append(poly([(cx, cy), l, tip, r], AC, 1.5, ACS))
        w = (cx + rb * math.cos(a), cy + rb * math.sin(a))
        o.append(C(*w, 5, NX))
    o.append(C(cx, cy, 7, INK))
    o.append(T(cx, cy + 34, 'nozzle', 13, 'middle', INK, bold=True))
    # dimension along the top jet
    o.append(L(cx - 40, cy, cx - 40, cy - S, NX, 1.6)); o.append(L(cx - 48, cy - S, cx - 32, cy - S, NX, 1.6)); o.append(L(cx - 48, cy, cx - 32, cy, NX, 1.6))
    o.append(Tb(cx - 52, cy - S * 0.8, 'S = 44 mm', 13, 'end', NX, True))
    # data panel
    x = 470
    lines = [('5 holes × 0.25 mm', INK, True), ('total area 0.245 mm²', MUT, False), ('Δp = 700 − 60 = 640 bar', INK, True),
             ('flow 0.056 kg/s, jet 275 m/s', MUT, False), ('56 mg in 1.0 ms', MUT, False), ('break-up after 0.166 ms', MUT, False),
             ('at 0.5 ms the tips are', INK, True), ('44 mm out: past the wall', NX, True), ('fix: smaller holes, more', INK, False), ('holes or more swirl', INK, False)]
    for i, (s, c, b) in enumerate(lines):
        o.append(T(x, 80 + i * 26, s, 14 if b else 13, 'start', c, b))
    return 430, ''.join(o)


FIG[7] = (f7, 'The worked example’s five jets seen from above, drawn to scale. Half a millisecond after injection starts, each tip has travelled about 44 mm, '
              'beyond the 35 mm bowl wall, so the liquid would wet the wall and smoke; smaller holes or more swirl shorten the jets.',
          'Top view of a circular piston bowl of 35 millimetre radius with a five-hole nozzle at its centre. Five narrow spray cones radiate at 72 degree '
          'spacing and each reaches 44 millimetres, past the bowl wall. A panel lists the hole size, pressure difference, flow and penetration.')


# ---- 2.8 centrifugal governor ----
def f8():
    o = []
    cx = 230
    o.append(L(cx, 50, cx, 420, INK, 4))
    o.append(R(cx - 40, 412, 80, 18, PANEL, MUT, 3)); o.append(T(cx, 452, 'driven from the pump camshaft', 13, 'middle', MUT))
    o.append(C(cx, 80, 6, INK))
    r = 120
    by = 170
    for s in (-1, 1):
        bx = cx + s * r
        o.append(L(cx, 80, bx, by, INK, 3))
        o.append(L(bx, by, cx + s * 14, 250, INK, 2.5))
        o.append(f'<circle cx="{bx}" cy="{by}" r="24" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:3"/>')
    o.append(L(cx - 100, by + 40, cx + 100, by + 40, LV, 2, arrow='l')); o.append(L(cx + 100, by + 40, cx - 100, by + 40, LV, 2, arrow='l'))
    o.append(T(cx - 160, by + 4, 'ball 0.1 kg', 13, 'end', AC, True))
    # radius dimension
    o.append(L(cx, by - 40, cx + r, by - 40, NX, 1.6)); o.append(L(cx + r, by - 48, cx + r, by - 32, NX, 1.6))
    o.append(Tb(cx + r / 2, by - 46, 'r = 50 mm', 13, 'middle', NX, True))
    # sleeve and spring
    o.append(R(cx - 22, 246, 44, 30, PANEL, AC, 4))
    o.append(T(cx - 30, 266, 'sleeve', 13, 'end', AC, True))
    zz = [(cx - 24, 300)]
    for i in range(1, 8):
        zz.append((cx + (24 if i % 2 else -24), 300 + i * 12))
    o.append(L(cx - 30, 276, cx + 30, 276, INK, 2)); o.append(P([(cx, 276), (cx, 300)] , INK, 2))
    o.append(P(zz, MUT, 2)); o.append(L(cx - 34, 388, cx + 34, 388, INK, 4))
    o.append(T(cx - 34, 340, 'spring', 13, 'end', MUT, True))
    # lever to rack
    o.append(L(cx + 22, 261, 420, 261, AC, 3)); o.append(C(420, 261, 6, INK))
    o.append(L(420, 261, 470, 340, AC, 3))
    o.append(R(440, 340, 240, 22, PANEL, INK, 4))
    o.append(T(560, 382, 'fuel rack of the pump', 13, 'middle', INK, True))
    o.append(L(470, 351, 420, 351, NX, 2.5, arrow='x')); o.append(T(560, 330, 'pulled to less fuel', 13, 'middle', NX))
    lines = [('1200 rpm: F = 79.0 N', INK, True), ('1260 rpm: F = 87.1 N', INK, True), ('5 % faster → 10.25 % more force', MUT, False),
             ('balls fly out, sleeve rises', MUT, False), ('against the spring', MUT, False)]
    for i, (s, c, b) in enumerate(lines):
        o.append(T(430, 70 + i * 24, s, 14 if b else 13, 'start', c, b))
    return 466, ''.join(o)


FIG[8] = (f8, 'A centrifugal governor with the worked example’s numbers. Each 0.1 kg ball on a 50 mm path radius pulls outward with 79.0 N at 1200 rpm; '
              'if the load drops and the speed rises to 1260 rpm the force grows to 87.1 N, the sleeve rises against the spring and the lever pulls the rack to less fuel.',
          'A vertical spindle carries two flyballs on hinged arms. Links from the balls lift a sleeve against a spring; a lever from the sleeve moves the fuel rack '
          'of the injection pump. Labels give the ball mass, path radius 50 millimetres and the forces at 1200 and 1260 rpm.')


# ---- 2.9 battery-coil ignition circuit ----
def f9():
    o = []
    # battery
    o.append(L(60, 160, 60, 300, INK, 2))
    o.append(L(40, 214, 80, 214, INK, 3)); o.append(L(50, 228, 70, 228, INK, 3)); o.append(L(40, 242, 80, 242, INK, 3)); o.append(L(50, 256, 70, 256, INK, 3))
    o.append(T(96, 236, '12 V', 13, 'start', INK, True)); o.append(T(96, 254, 'battery', 13, 'start', MUT))
    o.append(T(88, 210, '+', 14, 'start', INK, True))
    o.append(L(60, 300, 60, 330, INK, 2)); o.append(L(46, 330, 74, 330, INK, 2)); o.append(L(52, 336, 68, 336, INK, 2))
    # ignition switch
    o.append(L(60, 160, 60, 100, INK, 2)); o.append(L(60, 100, 120, 100, INK, 2))
    o.append(C(124, 100, 4, INK)); o.append(L(126, 98, 160, 84, INK, 2)); o.append(C(164, 100, 4, INK))
    o.append(T(144, 74, 'ignition switch', 13, 'middle', MUT))
    o.append(L(168, 100, 240, 100, INK, 2))
    # coil: primary and secondary
    o.append(L(240, 100, 240, 130, INK, 2))
    o.append(coil(240, 130, 250, 5, 10, AC))
    o.append(L(276, 120, 276, 260, INK, 2)); o.append(L(284, 120, 284, 260, INK, 2))
    o.append(coil(320, 120, 260, 9, 8, LV, -1))
    o.append(T(232, 300, 'primary', 13, 'end', AC, True)); o.append(T(232, 318, '6 mH, 3 Ω', 13, 'end', AC))
    o.append(T(330, 290, 'secondary', 13, 'start', LV, True)); o.append(T(330, 308, '≈ 100 × turns', 13, 'start', LV))
    o.append(T(280, 112, 'core', 13, 'middle', MUT))
    # primary to contact breaker
    o.append(L(240, 250, 240, 380, INK, 2)); o.append(L(240, 380, 330, 380, INK, 2))
    o.append(C(334, 380, 4, INK)); o.append(L(336, 378, 372, 368, INK, 2)); o.append(C(378, 380, 4, INK))
    o.append(L(382, 380, 420, 380, INK, 2)); o.append(L(420, 380, 420, 400, INK, 2)); o.append(L(406, 400, 434, 400, INK, 2)); o.append(L(412, 406, 428, 406, INK, 2))
    o.append(T(356, 352, 'contact breaker', 13, 'middle', AC, True))
    # cam
    o.append(f'<rect x="337" y="414" width="40" height="40" rx="10" transform="rotate(45 357 434)" style="fill:var(--panel);stroke:var(--muted);stroke-width:2"/>')
    o.append(T(390, 446, '4-lobe cam, 54° dwell', 13, 'start', MUT))
    # condenser across the points
    o.append(L(300, 380, 300, 410, INK, 2)); o.append(L(286, 410, 314, 410, INK, 3)); o.append(L(286, 418, 314, 418, INK, 3))
    o.append(L(300, 418, 300, 444, INK, 2)); o.append(L(286, 444, 314, 444, INK, 2))
    o.append(T(280, 432, 'condenser', 13, 'end', MUT))
    # secondary to distributor
    o.append(L(320, 120, 320, 100, LV, 2)); o.append(L(320, 100, 470, 100, LV, 2.5))
    o.append(f'<circle cx="520" cy="210" r="60" style="fill:var(--panel);stroke:var(--live);stroke-width:2"/>')
    o.append(L(470, 100, 520, 100, LV, 2.5)); o.append(L(520, 100, 520, 200, LV, 2.5))
    o.append(L(520, 210, 560, 180, LV, 4)); o.append(C(520, 210, 5, LV))
    o.append(T(520, 296, 'distributor', 13, 'middle', LV, True)); o.append(T(520, 314, '(rotor)', 13, 'middle', MUT))
    for i, (a, lab) in enumerate(((-40, '1'), (0, '3'), (40, '4'), (80, '2'))):
        rad = math.radians(a)
        sx, sy = 520 + 60 * math.cos(rad), 210 + 60 * math.sin(rad)
        ex, ey = 640, 140 + i * 50
        o.append(L(sx, sy, ex, ey, LV, 1.8))
        o.append(R(ex, ey - 10, 30, 20, PANEL, INK, 4)); o.append(T(ex + 40, ey + 5, f'plug {lab}', 13, 'start', INK))
    o.append(T(470, 380, 'at break: 4 A, E = ½LI² = 48 mJ', 13, 'start', INK, True))
    o.append(T(470, 400, 'at 6000 rpm only 3.11 A, 29 mJ', 13, 'start', NX))
    return 470, ''.join(o)


FIG[9] = (f9, 'Battery-coil ignition with the worked examples’ values. While the cam keeps the points shut, current builds in the 6 mH primary; when they open, '
              'the field collapses, the secondary’s many turns give the high voltage, and the rotor sends it to the plug that is due to fire.',
          'Circuit of battery-coil ignition: 12 volt battery, ignition switch, coil primary of 6 millihenry and 3 ohms on an iron core, contact breaker opened '
          'by a four-lobe cam with a condenser across it, secondary winding to the distributor rotor and four spark plug leads.')


# ---- 2.10 breakerless electronic ignition and laser ignition ----
def f10():
    o = []
    o.append(T(20, 28, 'Breakerless (transistorised) ignition', 14, 'start', INK, True))
    o.append(boxt(20, 50, 140, 64, ['Hall trigger', 'vane + magnet'], fill=PANEL, stroke=NX, size=13))
    o.append(boxt(200, 50, 150, 64, ['ignition module', 'transistor, dwell'], fill=NXS, stroke=NX, size=13))
    o.append(boxt(390, 50, 120, 64, ['coil'], fill=PANEL, stroke=AC, size=14))
    o.append(boxt(550, 50, 150, 64, ['spark plug'], fill=PANEL, stroke=LV, size=14))
    o.append(L(160, 82, 198, 82, NX, 2, arrow='x')); o.append(L(350, 82, 388, 82, AC, 2, arrow='n')); o.append(L(510, 82, 548, 82, LV, 2.5, arrow='l'))
    o.append(T(180, 132, 'square wave', 13, 'middle', MUT)); o.append(T(370, 132, 'switches', 13, 'middle', MUT))
    o.append(T(370, 148, 'primary', 13, 'middle', MUT)); o.append(T(530, 132, 'high voltage', 13, 'middle', MUT))
    o.append(L(20, 172, 700, 172, LN, 1))
    # laser ignition
    o.append(T(20, 200, 'Laser ignition', 14, 'start', INK, True))
    o.append(boxt(20, 230, 150, 64, ['pulsed laser', '30 mJ in 6 ns'], fill=PANEL, stroke=AC, size=13))
    o.append(L(170, 262, 300, 262, AC, 4))
    o.append(f'<ellipse cx="310" cy="262" rx="10" ry="34" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2"/>')
    o.append(T(310, 316, 'lens', 13, 'middle', MUT))
    o.append(R(360, 222, 14, 80, ACS, INK, 2)); o.append(T(367, 316, 'window', 13, 'middle', MUT))
    o.append(poly([(320, 232), (500, 262), (320, 292)], AC, 1.5, ACS))
    o.append(path('M374,216 L696,216 L696,356 L374,356', INK, 3))
    o.append(T(560, 344, 'combustion chamber', 13, 'middle', MUT))
    o.append(f'<circle cx="500" cy="262" r="9" style="fill:var(--next);stroke:var(--next);stroke-width:1"/>')
    o.append(f'<circle cx="508" cy="262" r="30" style="fill:none;stroke:var(--live);stroke-width:2;stroke-dasharray:4 3"/>')
    o.append(T(548, 290, 'plasma at the focus', 13, 'start', NX, True)); o.append(T(548, 306, 'then a flame kernel', 13, 'start', LV))
    o.append(T(20, 330, 'peak power 5 MW', 13, 'start', INK, True))
    o.append(T(20, 348, '50 μm spot: 2.5×10¹¹ W/cm²', 13, 'start', INK, True))
    o.append(T(380, 380, 'no electrodes: the focus can sit in the middle of the charge', 13, 'middle', MUT))
    return 398, ''.join(o)


FIG[10] = (f10, 'Top: in breakerless ignition a Hall trigger tells the module when to switch the coil, so no points wear. Bottom: in laser ignition the '
                'second worked example’s 30 mJ, 6 ns pulse is focused through a window to a 50 μm spot, where 2.5×10¹¹ W/cm² breaks the gas down into a plasma that lights the charge.',
           'Two panels. Top: block chain of a breakerless ignition system, Hall trigger to ignition module to coil to spark plug. Bottom: a pulsed laser beam '
           'passes a lens and a window into a combustion chamber and focuses to a point where a plasma forms and starts a flame.')


# ---- 2.11 spark advance at two speeds ----
def f11():
    rows = [{'name': '1500 rpm', 'sub': '4.0 ms burn', 'marks': [(-22, 'spark 22°'), (14, 'peak')],
             'bars': [(-22, 14, AC, '36° from spark to peak', False)]},
            {'name': '3000 rpm', 'sub': '2.5 ms burn', 'marks': [(-31, 'spark 31°'), (14, 'peak')],
             'bars': [(-31, 14, LV, '45° from spark to peak', False)]},
            {'name': '3000 rpm', 'sub': 'if still 4.0 ms', 'marks': [(-58, 'spark 58°')],
             'bars': [(-58, 14, NX, '72°: impossible advance', True)]}]
    h, body = strip(rows, -60, 20, x0=160, y0=56, gap=96, ticks=10)
    return h, body


FIG[11] = (f11, 'The worked example on a crank-angle scale. With peak pressure held at 14° after TDC, the 4.0 ms burn at 1500 rpm needs a spark at 22°; '
                'at 3000 rpm turbulence cuts the burn to 2.5 ms, so 31° is enough, while a burn that stayed at 4.0 ms would need 58°.',
           'Three crank-angle bars ending at 14 degrees after TDC. At 1500 rpm the spark is 22 degrees before TDC; at 3000 rpm with a 2.5 millisecond burn it is '
           '31 degrees; a dashed bar shows that a 4.0 millisecond burn at 3000 rpm would need 58 degrees.')


spec = make_spec(FIG)
