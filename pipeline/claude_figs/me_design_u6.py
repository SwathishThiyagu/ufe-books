"""Claude's hand-drawn figures for me-design-u6 (Machine Design: belt, chain and wire rope drives), one per chapter,
drawn from each chapter's own worked example and numbers. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


def fmt(v):
    return neg(f'{v:g}')


def sub(s, i):
    return f'{s}<tspan baseline-shift="sub" font-size="11">{i}</tspan>'


def poly(pts, stroke=AC, fill=PANEL, w=2, dash=None):
    d = f';stroke-dasharray:{dash}' if dash else ''
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" style="fill:{fill};stroke:{stroke};stroke-width:{w}{d};stroke-linejoin:round"/>'


def circles(cs, stroke=AC, fill=PANEL, w=1.2):
    """many circles as one path: cs = [(x, y, r), ...]"""
    d = ''.join(f'M{x + r:.2f},{y:.2f}a{r:.2f},{r:.2f} 0 1,0 {-2 * r:.2f},0a{r:.2f},{r:.2f} 0 1,0 {2 * r:.2f},0' for x, y, r in cs)
    return f'<path d="{d}" style="fill:{fill};stroke:{stroke};stroke-width:{w}"/>'


# ---- 6.1 inside a flat belt and a V-belt; the worked example's leather belt ----
def f1():
    o = []
    o.append(T(16, 26, 'Rubber-fabric flat belt, cut across', 14, 'start', bold=True))
    x0, x1 = 40, 420
    layers = [(44, 10, ACS, 'friction cover'), (54, 18, PANEL, 'fabric plies'), (72, 16, FIGBG, 'tension cords'),
              (88, 18, PANEL, 'fabric plies'), (106, 10, ACS, 'inner cover')]
    for y, h, f, _ in layers:
        o.append(R(x0, y, x1 - x0, h, f, L2, 2, 1.5))
    o.append(R(x0, 44, x1 - x0, 72, 'none', AC, 4, 2))
    o.append(circles([(x, 80, 5) for x in range(56, 412, 19)], AC, ACS, 1.5))
    o.append(L(x0 - 10, 80, x1 + 10, 80, NX, 1.5, dash='6 4'))
    labs = [(49, 'friction cover'), (63, 'fabric plies'), (84, 'tension cords on the neutral axis'), (106, 'fabric plies, inner cover')]
    for y, s in labs:
        o.append(L(x1 + 12, y, x1 + 26, y, L2, 1.2))
        o.append(T(x1 + 32, y + 5, s, 13, 'start', fill=NX if 'neutral' in s else INK))
    o.append(T(230, 140, 'cords at the neutral axis are hardly bent, so the belt survives small pulleys', 13, fill=MUT))
    # V-belt in its groove
    o.append(T(16, 182, 'V-belt in a pulley groove', 14, 'start', bold=True))
    cx, top, bot = 180, 212, 330
    gw_top, gw_bot = 100, 22  # groove half widths
    o.append(P([(cx - 150, top), (cx - gw_top, top), (cx - gw_bot, bot + 24), (cx + gw_bot, bot + 24), (cx + gw_top, top), (cx + 150, top)], L2, 2.5))
    # belt: sides follow the groove flanks between top and bot, clear of the groove bottom
    t = lambda y: gw_top - (gw_top - gw_bot) * (y - top) / (bot + 24 - top)
    yb0, yb1 = top - 14, bot - 6
    o.append(poly([(cx - t(yb0) - 0, yb0), (cx + t(yb0), yb0), (cx + t(yb1), yb1), (cx - t(yb1), yb1)], AC, ACS, 2.5))
    o.append(T(cx, yb0 + 34, 'belt, 40°', 13, bold=True))
    o.append(T(cx, yb0 + 54, 'cords under the top', 13, fill=MUT))
    o.append(Tb(cx, bot + 14, 'clearance', 13, fill=NX))
    o.append(L(cx - t(260) - 34, 252, cx - t(260) - 4, 262, LV, 2, arrow='l'))
    o.append(L(cx + t(260) + 34, 252, cx + t(260) + 4, 262, LV, 2, arrow='l'))
    o.append(T(cx - 136, 246, 'grips', 13, fill=LV))
    o.append(T(cx + 136, 246, 'grips', 13, fill=LV))
    o.append(T(cx, 380, 'groove cut at 34° to 38°', 13, fill=MUT))
    # worked example box
    o.append(R(392, 192, 312, 196, PANEL, AC, 8))
    o.append(T(548, 218, 'Worked example: solid leather belt', 14, bold=True))
    o.append(T(548, 244, 'b = 100 mm, t = 6 mm, ρ = 1000 kg/m³', 13))
    o.append(T(548, 274, 'm = ρbt = 1000 × 0.1 × 0.006', 14))
    o.append(T(548, 294, '= 0.6 kg/m', 14, bold=True))
    o.append(T(548, 326, f'at 15 m/s: {sub("T", "c")} = 0.6 × 15² = 135 N', 14, fill=AC, bold=True))
    o.append(T(548, 352, f'at 30 m/s: {sub("T", "c")} = 540 N', 14, fill=NX, bold=True))
    o.append(T(548, 374, 'twice the speed, four times the pull', 13, fill=MUT))
    return 398, ''.join(o)


# ---- 6.2 power the 80 mm belt of the worked example can carry, against belt speed ----
K2 = math.exp(0.3 * (math.pi - 2 * math.asin(0.1)))   # 2.4166


def _p2(v, T=2000.0, m=0.8):
    return (T - m * v * v) * (1 - 1 / K2) * v / 1000


def f2():
    o = []
    x0, x1, y0, y1 = 80, 690, 40, 300
    fx = lin(0, 50, x0, x1); fy = lin(0, 25, y1, y0)
    o.append(axes(x0, x1, y0, y1, [0, 10, 20, 30, 40, 50], [0, 5, 10, 15, 20, 25], fx, fy,
                  'belt speed v (m/s)', 'power the belt can carry (kW)', fmt, fmt))
    pts = [(fx(v / 4), fy(_p2(v / 4))) for v in range(0, 201)]
    o.append(P(pts, AC, 2.5))
    o.append(L(fx(0), fy(15), fx(50), fy(15), NX, 1.5, dash='6 4'))
    o.append(Tb(fx(44), fy(15) - 8, 'needed: 15 kW', 13, fill=NX))
    vo, po = 15.08, _p2(15.08)
    vm = math.sqrt(2000 / 2.4); pm = _p2(vm)
    o.append(L(fx(vo), fy(po), fx(vo), y1, LV, 1.5, dash='4 4'))
    o.append(C(fx(vo), fy(po), 6, LV))
    o.append(Tb(fx(vo) - 10, fy(po) - 14, 'running point: 15.08 m/s, 16.07 kW', 13, 'end', fill=LV, bold=True))
    o.append(L(fx(vm), fy(pm), fx(vm), y1, AC, 1.5, dash='4 4'))
    o.append(C(fx(vm), fy(pm), 6, AC))
    o.append(Tb(fx(vm) + 10, fy(pm) - 12, f'peak 22.56 kW at 28.87 m/s, where {sub("T", "c")} = T/3', 13, 'start', bold=True))
    o.append(T(fx(30.5), fy(10), 'above the peak,', 13, 'start', fill=MUT))
    o.append(T(fx(30.5), fy(8), f'{sub("T", "c")} = m v² eats', 13, 'start', fill=MUT))
    o.append(T(fx(30.5), fy(6), 'the safe tension', 13, 'start', fill=MUT))
    o.append(T(385, 366, 'b = 80 mm, t = 10 mm: T = σbt = 2000 N, m = 0.8 kg/m, e<tspan baseline-shift="super" font-size="11">μθ</tspan> = 2.417', 13, fill=MUT))
    return 380, ''.join(o)


# ---- 6.3 the wedge, and the belt count of the worked example ----
def f3():
    o = []
    o.append(T(16, 24, 'Why the groove grips harder', 14, 'start', bold=True))
    cx, top, bot = 170, 70, 230
    b = math.radians(19)
    hw = lambda y: (bot - y) * math.tan(b) + 18
    o.append(P([(cx - 140, top), (cx - hw(top), top), (cx - hw(bot), bot), (cx + hw(bot), bot), (cx + hw(top), top), (cx + 140, top)], L2, 2.5))
    yb0, yb1 = top - 10, bot - 40
    o.append(poly([(cx - hw(yb0), yb0), (cx + hw(yb0), yb0), (cx + hw(yb1), yb1), (cx - hw(yb1), yb1)], AC, ACS, 2.5))
    o.append(L(cx, yb0 + 8, cx, yb1 + 52, INK, 2.5, arrow='m'))
    o.append(Tb(cx, yb1 + 70, 'R, the push of the belt', 13, bold=True))
    ym = (yb0 + yb1) / 2 + 10
    for s in (-1, 1):
        xf = cx + s * hw(ym)
        nx, ny = -s * math.cos(b), -math.sin(b)   # flank normal pointing into the belt
        o.append(L(xf - nx * 58, ym - ny * 58, xf - nx * 4, ym - ny * 4, LV, 2.5, arrow='l'))
        o.append(T(xf - nx * 74 + s * 4, ym - ny * 74 + 4, sub('R', 'n'), 15, fill=LV, bold=True))
    o.append(T(cx, top - 26, '2β = 38°', 14, bold=True))
    o.append(T(16, 288, f'2{sub("R", "n")} sin β = R, friction 2μ{sub("R", "n")} = μR/sin β', 13, 'start'))
    o.append(T(16, 310, 'μ′ = μ/sin 19° = 3.07μ', 14, 'start', fill=AC, bold=True))
    # belt count
    o.append(T(372, 24, 'Belt count, worked example 1', 14, 'start', bold=True))
    x0, x1 = 410, 700
    fx = lin(0, 11, x0, x1)
    per = 2.6 * 0.87 * 0.95
    for row, n, y in ((0, 4, 90), (1, 5, 170)):
        o.append(T(x0 - 8, y + 24, f'{n}', 15, 'end', bold=True))
        for i in range(n):
            o.append(R(fx(i * per), y, fx(per) - fx(0) - 2, 36, ACS if n == 5 else FIGBG, AC if n == 5 else L2, 3))
        msg = f'{n} × 2.149 = {n * per:.2f} kW, ' + ('enough' if n == 5 else 'short')
        o.append(T(x0, y + 58, msg, 13, 'start', fill=AC if n == 5 else NX, bold=True))
    o.append(T(x0 - 8, 64, 'belts', 13, 'end', fill=MUT))
    o.append(L(fx(9.0), 58, fx(9.0), 236, NX, 2, dash='6 4'))
    o.append(Tb(fx(9.0), 52, 'design power 9.0 kW', 13, fill=NX, bold=True))
    o.append(T(372, 270, 'one belt: 2.6 × 0.87 × 0.95 = 2.149 kW', 13, 'start'))
    o.append(T(372, 292, '9.0 ÷ 2.149 = 4.19, so 4 belts fall short:', 13, 'start'))
    o.append(T(372, 314, 'use 5 belts', 14, 'start', fill=AC, bold=True))
    return 330, ''.join(o)


# ---- 6.4 the chain drive of the worked example and its chordal speed ----
def f4():
    o = []
    s = 0.74                      # px per mm
    c1x, cy = 110, 120
    Cd = 503.36
    c2x = c1x + Cd * s
    r1, r2 = 77.16 / 2 * s, 153.79 / 2 * s
    def gon(cx, r, z, rot):
        return [(cx + r * math.cos(rot + 2 * math.pi * i / z), cy + r * math.sin(rot + 2 * math.pi * i / z)) for i in range(z)]
    a = math.asin((r2 - r1) / (c2x - c1x))
    # chain strands: tangents of the pitch circles
    t1 = (c1x - r1 * math.sin(a), cy - r1 * math.cos(a)); t2 = (c2x - r2 * math.sin(a), cy - r2 * math.cos(a))
    b1 = (c1x - r1 * math.sin(a), cy + r1 * math.cos(a)); b2 = (c2x - r2 * math.sin(a), cy + r2 * math.cos(a))
    o.append(poly(gon(c1x, r1, 19, 0), AC, PANEL, 2))
    o.append(poly(gon(c2x, r2, 38, 0), AC, PANEL, 2))
    o.append(L(*t1, *t2, AC, 3.5))
    sag = f'<path d="M{b1[0]:.1f},{b1[1]:.1f} Q{(b1[0] + b2[0]) / 2:.1f},{(b1[1] + b2[1]) / 2 + 22:.1f} {b2[0]:.1f},{b2[1]:.1f}" style="fill:none;stroke:{AC};stroke-width:3.5;stroke-dasharray:3 3"/>'
    o.append(sag)
    o.append(C(c1x, cy, 4, INK)); o.append(C(c2x, cy, 4, INK))
    o.append(L(c1x, cy, c2x, cy, L2, 1.2, dash='4 4'))
    o.append(Tb((c1x + c2x) / 2, cy + 5, 'C = 503.4 mm for 108 links', 13, bold=True))
    o.append(T(c1x + 20, cy + r1 + 40, f'{sub("Z", "1")} = 19, {sub("d", "1")} = 77.16 mm', 13, bold=True))
    o.append(T(c1x + 20, cy + r1 + 58, 'motor, 1000 rpm', 13, fill=MUT))
    o.append(T(c2x, cy + r2 + 22, f'{sub("Z", "2")} = 38, {sub("d", "2")} = 153.79 mm', 13, bold=True))
    o.append(T(c2x, cy + r2 + 40, 'compressor, 500 rpm', 13, fill=MUT))
    o.append(Tb((t1[0] + t2[0]) / 2, (t1[1] + t2[1]) / 2 - 10, 'tight side: F = 3000 ÷ 4.022 = 746 N', 13, fill=AC, bold=True))
    o.append(Tb((b1[0] + b2[0]) / 2, (b1[1] + b2[1]) / 2 + 40, 'slack side, sag about 2 % of C', 13, fill=MUT))
    # chordal speed plot
    y0, y1 = 300, 440
    x0, x1 = 90, 690
    fx = lin(0, 3, x0, x1); fy = lin(3.96, 4.05, y1, y0)
    o.append(T(16, 272, 'Link speed as the small sprocket turns (19 teeth, 1000 rpm)', 14, 'start', bold=True))
    o.append(axes(x0, x1, y0 + 12, y1, [0, 1, 2, 3], [3.96, 3.98, 4.00, 4.02, 4.04], fx, fy, 'sprocket turned, in tooth pitches (one pitch = 18.95°)', 'm/s', fmt, lambda v: f'{v:.2f}'))
    vmax = math.pi * 0.07716 * 1000 / 60
    pts = []
    for i in range(0, 301):
        u = i / 100
        ph = (u % 1 - 0.5) * math.radians(360 / 19)
        pts.append((fx(u), fy(vmax * math.cos(ph))))
    o.append(P(pts, AC, 2.5))
    o.append(L(x0, fy(4.022), x1, fy(4.022), LV, 1.5, dash='6 4'))
    o.append(Tb(fx(0.5), fy(vmax) - 9, '4.040 m/s', 13, fill=AC, bold=True))
    o.append(Tb(fx(1.0), fy(vmax * math.cos(math.radians(180 / 19))) + 20, '3.985 m/s', 13, fill=NX, bold=True))
    o.append(Tb(fx(2.5), fy(4.022) + 18, 'mean 4.022 m/s', 13, fill=LV))
    o.append(T(390, 498, 'swing = 1 − cos 9.474° = 1.36 % of the top speed', 13, fill=MUT))
    return 512, ''.join(o)


# ---- 6.5 a 6×19 rope, and the load budget of the goods-hoist example ----
def f5():
    o = []
    o.append(T(16, 24, '6×19 rope, cut across', 14, 'start', bold=True))
    cx, cy, Rr = 160, 180, 118
    rs = Rr / 3
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{Rr + 3}" style="fill:none;stroke:{L2};stroke-width:1.5;stroke-dasharray:4 4"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{rs - 2:.1f}" style="fill:{LVS};stroke:{LV};stroke-width:2"/>')
    w = rs / 5
    for k in range(6):
        ang = math.radians(90 + 60 * k)
        sx, sy = cx + 2 * rs * math.cos(ang), cy - 2 * rs * math.sin(ang)
        wires = [(sx, sy, w * 0.95)]
        wires += [(sx + 2 * w * math.cos(math.radians(60 * i)), sy + 2 * w * math.sin(math.radians(60 * i)), w * 0.95) for i in range(6)]
        wires += [(sx + 4 * w * math.cos(math.radians(30 * i)), sy + 4 * w * math.sin(math.radians(30 * i)), w * 0.95) for i in range(12)]
        hi = (k == 0)
        o.append(circles(wires, AC if hi else L2, ACS if hi else PANEL, 1.2))
    o.append(L(cx + 30, cy - 2 * rs - 4, 300, 58, INK, 1.2))
    o.append(T(306, 52, 'one strand:', 13, 'start', bold=True))
    o.append(T(306, 70, '1 + 6 + 12 = 19 wires', 13, 'start'))
    o.append(L(cx + 10, cy + 6, 300, 196, INK, 1.2))
    o.append(T(306, 192, 'fibre core', 13, 'start', fill=LV, bold=True))
    o.append(T(306, 210, 'holds the oil', 13, 'start', fill=MUT))
    o.append(T(cx, cy + Rr + 30, 'd = 11 mm, outer wires d/15 = 0.73 mm', 13))
    o.append(T(cx, cy + Rr + 48, 'A = 0.4d² = 48.4 mm²', 13))
    # load budget
    x0, x1 = 420, 700
    fx = lin(0, 70, x0, x1)
    o.append(T(420, 112, 'Loads on the 11 mm rope (kN)', 14, 'start', bold=True))
    o.append(R(fx(0), 130, fx(67.76) - fx(0), 34, FIGBG, L2, 3))
    o.append(R(fx(0), 130, fx(62.08) - fx(0), 34, ACS, AC, 3))
    o.append(R(fx(62.08), 130, fx(67.76) - fx(62.08), 34, NXS, NX, 2))
    o.append(T(fx(31), 152, '67.76 − 5.68 = 62.08', 13, bold=True))
    o.append(T(420, 186, f'breaking load {sub("F", "u")} = 1400 × 48.4 = 67.76', 13, 'start'))
    o.append(T(420, 205, f'bending load {sub("F", "b")} = 117.3 × 48.4 = 5.68', 13, 'start', fill=NX))
    o.append(R(fx(0), 222, fx(10.96) - fx(0), 34, LVS, LV, 3))
    o.append(T(fx(10.96) + 8, 244, f'{sub("F", "t")} = 10.96', 13, 'start', fill=LV, bold=True))
    o.append(T(420, 278, 'load + rope weight, × (1 + a/g)', 13, 'start', fill=MUT))
    o.append(R(420, 296, 280, 54, PANEL, AC, 8))
    o.append(T(560, 318, f'n = ({sub("F", "u")} − {sub("F", "b")}) ÷ {sub("F", "t")}', 14))
    o.append(T(560, 340, '= 62.08 ÷ 10.96 = 5.67', 14, fill=AC, bold=True))
    return 366, ''.join(o)


FIG = {
    1: (f1, 'Inside a flat belt and a V-belt. The pull is carried by cords on the neutral axis, and a V-belt grips on its two sides; the box works the leather belt of the worked example.',
        'Cross-section of a rubber-fabric flat belt with covers, fabric plies and tension cords on the neutral axis; a V-belt in a pulley groove gripping on its sides with clearance below; and the leather belt of the worked example with mass 0.6 kilograms per metre and centrifugal tension 135 newtons at 15 metres per second.'),
    2: (f2, 'Power the 80 mm belt of the worked example can carry at each belt speed. At 15.08 m/s it carries 16.07 kW, more than the 15 kW needed; its peak, 22.56 kW, comes at 28.87 m/s where centrifugal tension is a third of the safe tension.',
        'Curve of power against belt speed for an 80 millimetre flat belt, rising to 22.56 kilowatts at 28.87 metres per second and falling to zero at 50; the running point at 15.08 metres per second and 16.07 kilowatts is above the 15 kilowatt line.'),
    3: (f3, 'The groove multiplies friction, and the worked example rounds the belt count up. Each side pushes back with a reaction that leans at β, so the friction is μR/sin β; four belts give 8.60 kW, short of 9.0 kW, so five are used.',
        'V-belt in a 38 degree groove with the radial push R and two side reactions; beside it, bars of 4 and 5 belts at 2.149 kilowatts each against a 9.0 kilowatt design power line.'),
    4: (f4, 'The chain drive of the worked example, drawn to scale, and the link speed as the small sprocket turns. The speed dips by 1.36 % once per tooth because the chain leaves the 19-tooth sprocket as a polygon.',
        'Two sprockets with 19 and 38 teeth on a 503.4 millimetre centre distance with the tight and sagging slack strands; below, a wave of link speed between 4.040 and 3.985 metres per second around the 4.022 mean.'),
    5: (f5, 'A 6×19 rope and the load budget of the goods-hoist example. Bending over the 500 mm sheave uses 5.68 kN of the 67.76 kN breaking load, and what is left is 5.67 times the starting pull.',
        'Cross-section of a 6 by 19 rope with six strands of 19 wires round a fibre core; bars showing a breaking load of 67.76 kilonewtons less a 5.68 kilonewton bending load, against a pull of 10.96 kilonewtons, giving a factor of safety of 5.67.'),
}
spec = make_spec(FIG)
