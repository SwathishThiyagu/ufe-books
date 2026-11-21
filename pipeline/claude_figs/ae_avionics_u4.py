"""Claude's hand-drawn figures for ae-avionics-u4 (avionics architecture, displays, data buses, transducers and electronics),
one per chapter. Every number comes from that chapter's worked example and is computed here. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
lg = math.log10


# ---- 4.1 total-loss probability of simplex, duplex and triplex channels against the 10^-9 target ----
def f1():
    lam = 2e-4
    o = [T(20, 34, 'Layout', 14, 'start', MUT, True), T(515, 34, 'Probability of losing every channel in a 1 h flight', 14, fill=MUT, bold=True)]
    x0, x1 = 330, 700
    fx = lambda e: x0 + (e + 13) / 10 * (x1 - x0)
    rows = [('Simplex', 1), ('Duplex', 2), ('Triplex', 3)]
    for i, (name, n) in enumerate(rows):
        y = 80 + i * 75
        p = lam ** n
        o.append(T(20, y + 20, name, 15, 'start', INK, True))
        for c in range(n):
            o.append(boxt(110 + c * 52, y + 2, 44, 28, ['CH'], PANEL, AC, 13))
        ok = p <= 1e-9
        col, soft = (NX, NXS) if ok else (LV, LVS)
        xe = fx(lg(p))
        o.append(R(x0, y, xe - x0, 32, soft, col, 4))
        mant = p / 10 ** math.floor(lg(p))
        lab = f'{mant:.0f} × 10<tspan font-size="13" dy="-6">{neg(int(math.floor(lg(p))))}</tspan><tspan dy="6"> </tspan>'
        verdict = 'meets target' if ok else 'fails'
        if xe > 600:
            o.append(T(xe - 8, y + 21, lab, 14, 'end', INK, True))
            o.append(T(xe - 8, y + 50, verdict, 13, 'end', col, True))
        else:
            o.append(Tb(xe + 8, y + 21, lab + '  ' + verdict, 14, 'start', col, True))
    # axis
    ya = 300
    o.append(L(x0, ya, x1, ya, L2, 1.5))
    for e in (-12, -9, -6, -3):
        X = fx(e)
        o.append(L(X, ya, X, ya + 5, L2, 1.5))
        o.append(T(X, ya + 22, f'10<tspan font-size="13" dy="-6">{neg(e)}</tspan>', 14, fill=MUT))
    o.append(T((x0 + x1) / 2, ya + 44, 'log scale: further right is more likely', 13, fill=MUT))
    xt = fx(-9)
    o.append(L(xt, 58, xt, ya, AC, 2, '6 4'))
    o.append(Tb(xt, 58, 'civil target 10<tspan font-size="13" dy="-6">−9</tspan><tspan dy="6"> </tspan>', 13, fill=AC, bold=True))
    return 356, ''.join(o)

FIG[1] = (f1, 'The worked example\'s flight-control channels, λ = 2 × 10⁻⁴ per flight hour each: one channel and two channels both miss the 10⁻⁹ target for a catastrophic failure, and only three independent channels (8 × 10⁻¹²) meet it.',
          'Three rows: simplex with one channel box, duplex with two, triplex with three. Each row has a bar on a log scale of the probability of losing every channel in a one-hour flight: 2 times 10 to the minus 4, 4 times 10 to the minus 8, and 8 times 10 to the minus 12. A dashed line marks the civil target of 10 to the minus 9. The first two bars cross it and fail; the triplex bar stays left of it and meets the target.')


# ---- 4.2 eight federated LRUs replaced by one IMA cabinet, and the cabinet module's 50 ms major frame ----
def f2():
    o = [T(155, 34, 'Federated: 8 LRUs', 15, bold=True), T(560, 34, 'IMA: 1 cabinet', 15, bold=True)]
    for i in range(8):
        r, c = divmod(i, 4)
        o.append(boxt(14 + c * 74, 52 + r * 44, 64, 34, [f'LRU {i + 1}'], PANEL, L2, 13))
    o.append(T(155, 160, '8 × (2 kg, 40 W) = 16 kg, 320 W', 13, fill=MUT))
    o.append(R(420, 48, 280, 92, ACS, AC, 10))
    for j, (a, b) in enumerate((('core', 'module 1'), ('core', 'module 2'), ('I/O', 'module'))):
        o.append(boxt(432 + j * 90, 62, 78, 64, [a, b], PANEL, AC, 13))
    o.append(T(560, 160, '3 modules: 5 kg, 90 W', 13, fill=MUT))
    o.append(L(318, 95, 412, 95, AC, 2.5, arrow='n'))
    o.append(T(365, 84, 'replaced by', 13, fill=AC))
    o.append(T(360, 196, 'saves 11 kg (68.75 %) and 230 W (71.9 %)', 15, fill=NX, bold=True))
    # partition timeline
    x0, x1, y = 40, 680, 250
    fx = lambda t: x0 + t / 50 * (x1 - x0)
    o.append(T(360, 236, 'One core module, ARINC 653 major frame of 50 ms (90 % used, every partition at 20 Hz)', 13, fill=MUT, bold=True))
    parts = [('Flight management', 0, 20, ACS, AC), ('Display', 20, 32, ACS, AC), ('Fuel', 32, 40, ACS, AC), ('Maint.', 40, 45, ACS, AC), ('spare', 45, 50, FIGBG, L2)]
    for name, a, b, f, s in parts:
        o.append(R(fx(a), y, fx(b) - fx(a), 44, f, s, 3, dash='5 4' if name == 'spare' else None))
        o.append(T((fx(a) + fx(b)) / 2, y + 19, name, 13, fill=INK if name != 'spare' else MUT, bold=name != 'spare'))
        o.append(T((fx(a) + fx(b)) / 2, y + 36, f'{b - a} ms', 13, fill=MUT))
    for t in (0, 20, 32, 40, 45, 50):
        o.append(L(fx(t), y + 44, fx(t), y + 50, L2, 1.5))
        o.append(T(fx(t), y + 66, str(t), 13, fill=MUT))
    o.append(T(360, y + 88, 'time in the major frame (ms)', 13, fill=MUT))
    return 352, ''.join(o)

FIG[2] = (f2, 'Top: the eight federated boxes of the first worked example and the IMA cabinet that hosts their functions. Bottom: the second example\'s 50 ms major frame on one core module, with 5 ms spare, too little for an 8 ms partition.',
          'Left, eight boxes labelled LRU 1 to LRU 8 totalling 16 kilograms and 320 watts. An arrow labelled replaced by points to one IMA cabinet holding two core modules and an input-output module, totalling 5 kilograms and 90 watts. The saving is 11 kilograms and 230 watts. Below, a 50 millisecond timeline divided into flight management 20 ms, display 12 ms, fuel 8 ms, maintenance 5 ms and 5 ms spare, with ticks at 0, 20, 32, 40, 45 and 50.')


# ---- 4.3 basic T dials and where their jobs sit on a PFD; battery time before and after load shedding ----
def f3():
    o = [T(150, 30, 'Analog: the basic T', 15, bold=True), T(545, 30, 'Glass: the same jobs on one PFD', 15, bold=True)]
    dials = [('ASI', 1, 60, 90), ('AI', 2, 150, 90), ('ALT', 3, 240, 90), ('TC', 4, 60, 175), ('HI', 5, 150, 175), ('VSI', 6, 240, 175)]
    badge = lambda x, y, n: f'<circle cx="{x:.1f}" cy="{y:.1f}" r="11" style="fill:var(--next);stroke:none"/>' + T(x, y + 5, str(n), 13, fill=FIGBG, bold=True)
    for name, n, x, y in dials:
        o.append(f'<circle cx="{x}" cy="{y}" r="34" style="fill:var(--panel);stroke:var(--line2);stroke-width:2"/>')
        o.append(T(x, y + 5, name, 14, bold=True))
        o.append(badge(x + 27, y - 27, n))
    # PFD
    px0, py0 = 380, 46
    o.append(R(px0, py0, 330, 186, PANEL, AC, 8))
    o.append(R(px0 + 12, py0 + 14, 46, 156, FIGBG, L2, 4)); o.append(T(px0 + 35, py0 + 96, 'SPD', 13, bold=True))
    o.append(R(px0 + 70, py0 + 14, 160, 64, ACS, LN, 0)); o.append(R(px0 + 70, py0 + 78, 160, 64, LVS, LN, 0))
    o.append(L(px0 + 70, py0 + 78, px0 + 230, py0 + 78, INK, 2))
    o.append(P([(px0 + 120, py0 + 78), (px0 + 140, py0 + 78), (px0 + 150, py0 + 88), (px0 + 160, py0 + 78), (px0 + 180, py0 + 78)], INK, 3))
    o.append(T(px0 + 150, py0 + 50, 'attitude', 13, bold=True))
    o.append(R(px0 + 242, py0 + 14, 46, 156, FIGBG, L2, 4)); o.append(T(px0 + 265, py0 + 96, 'ALT', 13, bold=True))
    o.append(R(px0 + 294, py0 + 34, 28, 116, FIGBG, L2, 4)); o.append(T(px0 + 308, py0 + 96, 'V/S', 13, bold=True))
    o.append(R(px0 + 90, py0 + 148, 120, 28, FIGBG, L2, 4)); o.append(T(px0 + 150, py0 + 167, 'heading', 13, bold=True))
    for n, x, y in ((1, px0 + 35, py0 + 30), (2, px0 + 92, py0 + 30), (3, px0 + 265, py0 + 30), (4, px0 + 150, py0 + 110),
                    (5, px0 + 196, py0 + 162), (6, px0 + 308, py0 + 48)):
        o.append(badge(x, y, n))
    o.append(T(20, 252, 'Same number = same job; 4 is the slip and turn indicator.', 13, 'start', MUT))
    # battery bars
    x0 = 250
    sc = 400 / 125
    o.append(T(20, 280, 'On battery, 192 Wh:', 14, 'start', INK, True))
    for i, (lab, w, mins, col, soft) in enumerate((('all loads 195 W', 195, 59, LV, LVS), ('shed to 95 W', 95, 121, NX, NXS))):
        y = 296 + i * 40
        o.append(T(20, y + 20, lab, 14, 'start', INK))
        o.append(R(x0 - 70, y, mins * sc, 28, soft, col, 4))
        o.append(T(x0 - 70 + mins * sc + 8, y + 19, f'{mins} min', 14, 'start', col, True))
    return 380, ''.join(o)

FIG[3] = (f3, 'Each numbered dial of the basic T keeps its job on the primary flight display; below, the worked example\'s battery lasts 59 minutes with every load on and 121 minutes after shedding the multifunction display and radios.',
          'Left, six round dials in the basic T: airspeed 1, attitude 2, altimeter 3 on top; turn coordinator 4, heading 5 and vertical speed 6 below. Right, a primary flight display with the same numbers on the speed tape, attitude picture, altitude tape, slip indicator, heading scale and vertical speed scale. Below, two bars: 195 watts gives 59 minutes on a 192 watt-hour battery, and 95 watts after load shedding gives 121 minutes.')


# ---- 4.4 PFD layout with the worked example's speed trend ----
def f4():
    o = []
    X0, Y0, X1, Y1 = 170, 20, 710, 400
    o.append(R(X0, Y0, X1 - X0, Y1 - Y0, PANEL, AC, 10))
    o.append(R(285, 32, 300, 34, FIGBG, L2, 4)); o.append(T(435, 54, 'FMA: active and armed modes', 13, fill=MUT, bold=True))
    # speed tape
    tx0, tx1, ty0, ty1 = 186, 262, 86, 334
    o.append(R(tx0, ty0, tx1 - tx0, ty1 - ty0, FIGBG, L2, 4))
    o.append(T((tx0 + tx1) / 2, 80, 'speed (kt)', 13, fill=MUT))
    vy = lambda v: 210 - (v - 250) * 4.6
    for v in range(230, 271, 10):
        if v == 250: continue
        o.append(L(tx1 - 12, vy(v), tx1, vy(v), INK, 1.5))
        o.append(T(tx0 + 8, vy(v) + 5, str(v), 13, 'start'))
    o.append(R(tx0 - 4, vy(250) - 15, tx1 - tx0 + 8, 30, PANEL, INK, 4, 2.5)); o.append(T((tx0 + tx1) / 2, vy(250) + 6, '250', 16, bold=True))
    o.append(L(tx1 - 20, vy(250) + 15, tx1 - 20, vy(238) - 2, NX, 3, arrow='x'))
    o.append(P([(tx1 + 1, vy(240) - 6), (tx1 - 9, vy(240)), (tx1 + 1, vy(240) + 6)], LV, 2, fill=LV))
    # annotations left and below
    o.append(T(160, vy(250) + 5, 'now 250 kt', 14, 'end', INK, True))
    o.append(L(164, vy(238), tx1 - 24, vy(238), NX, 1.5, '4 3'))
    o.append(T(160, vy(238) - 4, 'in 10 s:', 13, 'end', NX, True)); o.append(T(160, vy(238) + 14, '238 kt', 14, 'end', NX, True))
    o.append(P([(tx0 + 6, 346), (tx0 - 4, 352), (tx0 + 6, 358)], LV, 2, fill=LV))
    o.append(T(tx0 + 12, 357, '= bug 240 kt', 13, 'start', LV, True))
    # attitude
    ax0, ax1, ay0, ay1 = 286, 564, 86, 334
    o.append(R(ax0, ay0, ax1 - ax0, (ay1 - ay0) / 2, ACS, LN, 0)); o.append(R(ax0, (ay0 + ay1) / 2, ax1 - ax0, (ay1 - ay0) / 2, LVS, LN, 0))
    hy = (ay0 + ay1) / 2
    o.append(L(ax0, hy, ax1, hy, INK, 2))
    for d in (-1, 1):
        o.append(L(395, hy - d * 46, 455, hy - d * 46, INK, 1.5)); o.append(T(463, hy - d * 46 + 5, '10', 13, 'start'))
    o.append(P([(370, hy), (405, hy), (418, hy + 12), (431, hy), (466, hy)], INK, 4))
    o.append(T(425, ay0 + 26, 'attitude: sky above, ground below', 13, fill=MUT, bold=True))
    o.append(L(380, hy - 22, 470, hy - 22, NX, 2.5)); o.append(L(425, hy - 64, 425, hy + 30, NX, 2.5))
    o.append(T(425, ay1 - 14, 'flight director bars', 13, fill=NX, bold=True))
    # altitude tape and V/S
    lx0, lx1 = 580, 650
    o.append(R(lx0, ty0, lx1 - lx0, ty1 - ty0, FIGBG, L2, 4)); o.append(T((lx0 + lx1) / 2, 80, 'altitude', 13, fill=MUT))
    for a, yy in ((10200, 120), (10100, 165), (9900, 255), (9800, 300)):
        o.append(L(lx0, yy, lx0 + 10, yy, INK, 1.5)); o.append(T(lx0 + 14, yy + 5, str(a), 13, 'start'))
    o.append(R(lx0 - 4, hy - 15, lx1 - lx0 + 8, 30, PANEL, INK, 4, 2.5)); o.append(T((lx0 + lx1) / 2, hy + 6, '10000', 14, bold=True))
    o.append(R(660, 120, 38, 180, FIGBG, L2, 4)); o.append(T(679, 114, 'V/S', 13, fill=MUT))
    o.append(L(660, hy, 690, hy, INK, 1.5))
    # heading
    o.append(R(330, 348, 190, 40, FIGBG, L2, 4))
    for i, h in enumerate(('060', '090', '120')):
        o.append(T(365 + i * 60, 374, h, 13, bold=(h == '090')))
    o.append(T(600, 374, 'heading', 13, 'start', MUT))
    return 410, ''.join(o)

FIG[4] = (f4, 'The PFD of the first worked example: speed tape on the left, attitude in the centre, altitude and vertical speed on the right, heading below and the FMA on top. Decelerating at 1.2 kt/s from 250 kt, the trend arrow points down to 238 kt, already past the 240 kt bug.',
          'A primary flight display. Left, a speed tape from 230 to 270 knots with the current speed 250 in a box, a green trend arrow pointing down to 238 knots, and a speed bug at 240. Centre, an attitude picture with sky above and ground below, a horizon line, 10 degree pitch lines, an aircraft symbol and flight director bars. Right, an altitude tape with 10000 feet in a box and a vertical speed scale. Bottom, a heading scale with 090 selected. Top, the flight mode annunciator strip.')


# ---- 4.5 HUD side view: collimated symbols, the 3.03 degree flight path vector and the 14.25 degree IFOV ----
def f5():
    o = []
    ex, ey = 64, 150
    fpa = math.degrees(math.atan(750 / (140 * 101.27)))
    half = math.degrees(math.atan(150 / 1200))
    # outside world
    o.append(L(270, ey, 706, ey, MUT, 1.5, '6 4')); o.append(T(704, ey - 8, 'horizon', 13, 'end', MUT))
    t = math.tan(math.radians(half))
    o.append(L(ex, ey, 700, ey - t * (700 - ex), L2, 1.5, '3 4')); o.append(L(ex, ey, 700, ey + t * (700 - ex), L2, 1.5, '3 4'))
    o.append(Tb(560, ey - t * (560 - ex) - 10, 'IFOV 14.25° (±7.13°)', 13, fill=MUT, bold=True))
    yt = ey + math.tan(math.radians(fpa)) * (640 - ex)
    o.append(L(ex, ey, 640, yt, NX, 2))
    # runway
    o.append(P([(596, yt + 10), (612, yt - 4), (668, yt - 4), (684, yt + 10), (596, yt + 10)], INK, 2, fill=PANEL))
    o.append(f'<circle cx="640" cy="{yt:.1f}" r="8" style="fill:none;stroke:var(--next);stroke-width:2.5"/>')
    o.append(L(620, yt, 632, yt, NX, 2.5)); o.append(L(648, yt, 660, yt, NX, 2.5)); o.append(L(640, yt - 8, 640, yt - 16, NX, 2.5))
    o.append(Tb(470, yt + 6, 'FPV γ = 3.03° below the horizon', 13, fill=NX, bold=True))
    o.append(T(640, yt + 36, 'touchdown zone', 13, fill=MUT))
    # eye
    o.append(f'<ellipse cx="{ex}" cy="{ey}" rx="14" ry="9" style="fill:var(--panel);stroke:var(--ink);stroke-width:2"/>')
    o.append(C(ex + 4, ey, 4, INK))
    o.append(T(ex, ey + 34, "pilot's eye", 13, bold=True))
    # combiner and rays
    o.append(L(206, 126, 254, 174, AC, 5))
    o.append(T(268, 116, 'combiner', 13, 'start', AC, True))
    for dy in (-10, 0, 10):
        xs = 230 + dy
        o.append(L(xs, 262, xs, ey + dy + 1, LV, 1.8))
        o.append(L(xs - 2, ey + dy, ex + 22, ey + dy, LV, 1.8, arrow='l'))
    o.append(T(140, ey - 26, 'parallel rays: image at infinity', 13, fill=LV, bold=True))
    o.append(f'<ellipse cx="230" cy="270" rx="44" ry="9" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2"/>')
    o.append(T(284, 275, 'collimating lens (150 mm), 600 mm from the eye', 13, 'start', INK))
    o.append(R(196, 296, 68, 22, PANEL, INK, 4))
    o.append(T(284, 312, 'display source at the lens focal plane', 13, 'start', INK))
    o.append(boxt(20, 284, 150, 46, ['HUD computer', 'air data, inertial, ILS'], PANEL, L2, 13))
    o.append(L(170, 307, 194, 307, AC, 2, arrow='n'))
    return 344, ''.join(o)

FIG[5] = (f5, 'A HUD seen from the side, drawn to the worked example\'s angles: the display source sits at the focal plane of the collimating lens, so the rays reaching the eye are parallel and the symbols appear at infinity. The flight path vector sits 3.03° below the horizon on the touchdown zone, inside the 14.25° instantaneous field of view.',
          'Side view. At the bottom, a HUD computer feeds a display source under a collimating lens. Three parallel rays rise to a tilted combiner and reflect horizontally to the pilot\'s eye on the left. From the eye, a dashed horizon runs right, two dotted lines mark the instantaneous field of view of plus and minus 7.13 degrees, and a green line falls 3.03 degrees to the flight path vector symbol on the touchdown zone of a runway.')


# ---- 4.6 the scan loop and the worst-case wait for a caution ----
def f6():
    o = []
    x0, x1 = 40, 690
    fx = lambda t: x0 + t / 2.8 * (x1 - x0)
    areas = ['EICAS', 'PFD', 'ND', 'outside', 'MCP', 'overhead', 'EICAS']
    y = 60
    o.append(T(20, 40, 'Eyes dwell 0.4 s on each of six areas (one full scan 2.4 s)', 14, 'start', INK, True))
    for i, a in enumerate(areas):
        hit = a == 'EICAS'
        o.append(R(fx(i * 0.4), y, fx(0.4) - fx(0), 40, ACS if hit else PANEL, AC if hit else L2, 4))
        o.append(T(fx(i * 0.4 + 0.2), y + 25, a, 13, bold=hit))
    for i in range(8):
        t = i * 0.4
        o.append(L(fx(t), y + 40, fx(t), y + 46, L2, 1.5)); o.append(T(fx(t), y + 62, f'{t:.1f}', 13, fill=MUT))
    o.append(T(fx(1.4), y + 84, 'time (s)', 13, fill=MUT))
    # caution appears at 0.4 s, seen at 2.4 s
    o.append(L(fx(0.4), y - 12, fx(0.4), 236, LV, 2, '5 4'))
    o.append(T(fx(0.4) + 6, 172, 'caution appears on EICAS', 13, 'start', LV, True))
    o.append(T(fx(0.4) + 6, 188, 'as the eyes leave it', 13, 'start', LV))
    o.append(L(fx(2.4), y - 12, fx(2.4), 236, AC, 2, '5 4'))
    o.append(T(fx(2.4) - 6, 172, 'eyes return:', 13, 'end', AC, True)); o.append(T(fx(2.4) - 6, 188, 'caution seen', 13, 'end', AC))
    o.append(L(fx(0.4), 218, fx(2.4) - 4, 218, LV, 2.5, arrow='l'))
    o.append(Tb(fx(1.4), 222, 'worst-case wait 2.0 s', 14, fill=LV, bold=True))
    o.append(L(fx(0.4), 256, fx(1.9) - 4, 256, NX, 2.5, arrow='x'))
    o.append(T(fx(1.9) + 8, 261, 'need: seen within 1.5 s', 14, 'start', NX, True))
    o.append(T(360, 296, 'Average wait 0.83 s, but the worst case decides: add a master caution light and a chime.', 13, fill=MUT))
    return 312, ''.join(o)

FIG[6] = (f6, 'The worked example\'s scan: six areas at 0.4 s each. A caution that appears on the engine page just as the eyes leave it waits 2.0 s for the next look, longer than the 1.5 s allowed, so it needs a master caution light and a chime.',
          'A timeline from 0 to 2.8 seconds divided into seven 0.4 second dwells: EICAS, PFD, ND, outside, MCP, overhead and EICAS again. A caution appears at 0.4 seconds as the eyes leave EICAS and is seen at 2.4 seconds when they return, a worst-case wait of 2.0 seconds. A second arrow shows the need: seen within 1.5 seconds. A note gives the average wait of 0.83 seconds.')


# ---- 4.7 ARINC 429 word fields and the 1553B transmit message timeline ----
def f7():
    o = [T(20, 30, 'ARINC 429 word: 32 bits, then a 4-bit gap (36 × 10 µs = 0.36 ms at 100 kbit/s)', 14, 'start', INK, True)]
    x0, w = 40, 20
    fields = [('Label (octal)', 1, 8, ACS, AC), ('SDI', 9, 10, NXS, NX), ('Data, 19 bits', 11, 29, PANEL, INK), ('SSM', 30, 31, LVS, LV), ('P', 32, 32, NXS, NX)]
    y = 46
    for name, a, b, f, s in fields:
        xa, xb = x0 + (a - 1) * w, x0 + b * w
        o.append(R(xa, y, xb - xa, 40, f, s, 3, 2))
        o.append(T((xa + xb) / 2, y + 25, name, 13, bold=True))
        for bit in sorted({a, b}):
            o.append(T(x0 + (bit - 0.5) * w, y + 58, str(bit), 13, fill=MUT))
    for i in range(1, 32):
        o.append(L(x0 + i * w, y + 34, x0 + i * w, y + 40, L2, 1))
    o.append(T(x0 + 16 * w, y + 80, 'bit number (bit 1 is sent first); bit 32 makes the number of 1s odd', 13, fill=MUT))
    # 1553B
    o.append(T(20, 176, 'MIL-STD-1553B transmit message (RT to BC, 4 data words), 20 µs per word', 14, 'start', INK, True))
    X0, X1 = 40, 680
    fx = lambda t: X0 + t / 132 * (X1 - X0)
    yb = 192
    segs = [('Command', 'BC', 0, 20, ACS, AC), ('', '', 20, 28, None, None), ('Status', 'RT', 28, 48, NXS, NX)] + \
           [(f'Data {i + 1}', 'RT', 48 + 20 * i, 68 + 20 * i, PANEL, INK) for i in range(4)] + [('', '', 128, 132, None, None)]
    for name, who, a, b, f, s in segs:
        if f:
            o.append(R(fx(a), yb, fx(b) - fx(a), 44, f, s, 3, 2))
            o.append(T((fx(a) + fx(b)) / 2, yb + 19, name, 13, bold=True)); o.append(T((fx(a) + fx(b)) / 2, yb + 36, who, 13, fill=MUT))
    o.append(T(fx(24), yb + 27, '8', 13, fill=LV, bold=True))
    for t in (0, 20, 28, 48, 68, 88, 108, 128):
        o.append(L(fx(t), yb + 44, fx(t), yb + 50, L2, 1.5)); o.append(T(fx(t), yb + 66, str(t), 13, fill=MUT))
    o.append(T(fx(24), yb + 88, 'response gap 8 µs', 13, 'start', LV))
    o.append(T(X1, yb + 88, '+ 4 µs gap = 132 µs per message', 13, 'end', MUT, True))
    o.append(T(360, yb + 110, 'time (µs)', 13, fill=MUT))
    return 314, ''.join(o)

FIG[7] = (f7, 'Top: the five fields of an ARINC 429 word, with the bit numbers where each field starts and ends. Bottom: the second worked example\'s 1553B transmit message: command, an 8 µs response gap, the status word and four data words, 132 µs with the 4 µs gap that follows.',
          'Top, a row of 32 bit cells grouped as label bits 1 to 8, SDI bits 9 and 10, data bits 11 to 29, SSM bits 30 and 31 and parity bit 32. Bottom, a timeline in microseconds: command word from the bus controller 0 to 20, response gap to 28, status word from the remote terminal 28 to 48, then four data words ending at 128, and a 4 microsecond gap, 132 microseconds in all.')


# ---- 4.8 one frame on networks A and B, and VL1 paced at one frame per 2 ms ----
def f8():
    o = [T(20, 28, 'Every frame goes out on both networks', 14, 'start', INK, True)]
    o.append(boxt(20, 74, 150, 78, ['camera', 'end system', 'ports A and B'], PANEL, AC, 13, True))
    o.append(boxt(290, 44, 140, 44, ['switch A'], ACS, AC, 14))
    o.append(boxt(290, 140, 140, 44, ['switch B'], NXS, NX, 14))
    o.append(boxt(550, 74, 150, 78, ['display', 'end system', 'keeps first valid'], PANEL, AC, 13, True))
    o.append(P([(170, 96), (230, 96), (230, 66), (286, 66)], AC, 2.5)); o.append(L(430, 66, 490, 66, AC, 2.5)); o.append(P([(490, 66), (490, 96), (546, 96)], AC, 2.5))
    o.append(P([(170, 130), (230, 130), (230, 162), (286, 162)], NX, 2.5)); o.append(L(430, 162, 490, 162, NX, 2.5)); o.append(P([(490, 162), (490, 130), (546, 130)], NX, 2.5))
    o.append(L(540, 96, 546, 96, AC, 2.5, arrow='n')); o.append(L(540, 130, 546, 130, NX, 2.5, arrow='x'))
    o.append(T(360, 116, 'network A', 13, fill=AC, bold=True)); o.append(T(360, 206, 'network B', 13, fill=NX, bold=True))
    o.append(T(625, 176, 'duplicate dropped', 13, fill=MUT))
    o.append(T(95, 176, 'same sequence no.', 13, fill=MUT))
    # timeline
    X0, X1 = 40, 680
    fx = lambda t: X0 + t / 8 * (X1 - X0)
    y = 262
    o.append(T(20, 238, 'VL1: at most one 1000-byte frame per BAG of 2 ms = 4 Mbit/s reserved', 14, 'start', INK, True))
    o.append(L(X0, y + 30, X1, y + 30, L2, 1.5))
    for t in (0, 2, 4, 6):
        o.append(R(fx(t), y, max(fx(t + 0.0816) - fx(t), 6), 30, AC, AC, 1, 1))
    o.append(L(fx(0) + 10, y + 10, fx(2) - 4, y + 10, LV, 2, arrow='l'))
    o.append(Tb(fx(1), y + 14, 'BAG 2 ms', 13, fill=LV, bold=True))
    o.append(T(fx(4.2), y - 6, 'each frame: 81.6 µs on the wire', 13, 'start', AC))
    for t in range(0, 9, 2):
        o.append(L(fx(t), y + 30, fx(t), y + 36, L2, 1.5)); o.append(T(fx(t), y + 52, str(t), 13, fill=MUT))
    o.append(T(360, y + 74, 'time (ms)', 13, fill=MUT))
    return 346, ''.join(o)

FIG[8] = (f8, 'Top: the camera end system sends every frame on two independent networks, A and B, and the display end system keeps the first valid copy by its sequence number. Bottom: the worked example\'s VL1 sends at most one 1000-byte frame (81.6 µs on the wire) every 2 ms.',
          'Top, a camera end system with two ports. One path goes through switch A, the other through a separate switch B, and both reach a display end system that keeps the first valid copy and drops the duplicate. Bottom, a timeline from 0 to 8 milliseconds with narrow frames at 0, 2, 4 and 6 milliseconds, a bracket marking the 2 millisecond BAG, and a note that each frame lasts 81.6 microseconds on the wire.')


# ---- 4.9 the V-model with its verification pairs ----
def f9():
    o = []
    left = [('System requirements', 20, 30), ('High-level requirements', 70, 104), ('Low-level requirements', 120, 178)]
    right = [('HW/SW integration tests', 500, 30), ('Software integration tests', 450, 104), ('Unit tests', 400, 178)]
    bw, bh = 200, 44
    for name, x, y in left: o.append(boxt(x, y, bw, bh, [name], ACS, AC, 14))
    for name, x, y in right: o.append(boxt(x, y, bw, bh, [name], NXS, NX, 14))
    o.append(boxt(260, 252, 200, bh, ['Source code'], PANEL, INK, 14))
    for (n1, x1, y1), (n2, x2, y2) in zip(left, left[1:]):
        o.append(L(x1 + 60, y1 + bh, x2 + 60, y2 - 3, AC, 2, arrow='n'))
    o.append(L(180, 222, 256, 262, AC, 2, arrow='n'))
    o.append(L(462, 262, 520, 225, NX, 2, arrow='x'))
    for (n1, x1, y1), (n2, x2, y2) in zip(right[::-1], right[::-1][1:]):
        o.append(L(x1 + 140, y1, x2 + 140, y2 + bh + 3, NX, 2, arrow='x'))
    for (n1, xl, y), (n2, xr, _) in zip(left, right):
        o.append(L(xr - 4, y + bh / 2, xl + bw + 4, y + bh / 2, L2, 1.8, '6 4', 'm'))
        o.append(Tb((xl + bw + xr) / 2, y + bh / 2 + 5, 'verifies', 13, fill=MUT))
    o.append(T(130, 20, 'decompose down', 13, fill=AC, bold=True)); o.append(T(600, 20, 'verify up', 13, fill=NX, bold=True))
    o.append(T(360, 322, 'Traceability links every box to the box beside and opposite it, both ways.', 13, fill=MUT))
    o.append(T(360, 344, 'Level A unit tests need MC/DC: 4 tests for (a and b) or c, not all 8.', 13, fill=INK, bold=True))
    return 358, ''.join(o)

FIG[9] = (f9, 'The V-model: requirements are broken down on the left arm to source code at the bottom, and each level is verified on the right arm by the tests opposite it. At level A the unit tests must reach MC/DC, which the worked example meets with 4 tests instead of 8.',
          'A V shape. The left arm goes down from system requirements to high-level requirements to low-level requirements to source code at the bottom. The right arm goes up from unit tests to software integration tests to hardware and software integration tests. Dashed lines labelled verifies join each test level to the requirement level opposite it. A note says level A unit tests need MC/DC, four tests for (a and b) or c rather than all eight.')


# ---- 4.10 the full strain-gauge bridge of the pressure transducer ----
def f10():
    o = []
    top, left, right, bot = (360, 52), (200, 182), (520, 182), (360, 312)

    def arm(p, q, lab, sign, anchor, lx, ly):
        mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
        ang = math.degrees(math.atan2(q[1] - p[1], q[0] - p[0]))
        col = NX if sign == '+' else LV
        r = [L(p[0], p[1], q[0], q[1], INK, 2),
             f'<rect x="{mx - 26:.1f}" y="{my - 9:.1f}" width="52" height="18" rx="3" transform="rotate({ang:.1f} {mx:.1f} {my:.1f})" style="fill:var(--panel);stroke:{col};stroke-width:2.5"/>',
             T(lx, ly, lab, 13, anchor, col, True), T(lx, ly + 17, ('stretched, ' if sign == '+' else 'compressed, ') + ('350.70 Ω' if sign == '+' else '349.30 Ω'), 13, anchor, INK)]
        return ''.join(r)
    o.append(arm(top, left, 'R1: −1000 µε', '-', 'end', 262, 92))
    o.append(arm(top, right, 'R2: +1000 µε', '+', 'start', 458, 92))
    o.append(arm(left, bot, 'R3: +1000 µε', '+', 'end', 262, 268))
    o.append(arm(right, bot, 'R4: −1000 µε', '-', 'start', 458, 268))
    for n in (top, left, right, bot): o.append(C(n[0], n[1], 5, INK))
    # excitation
    o.append(P([(360, 52), (360, 30), (90, 30), (90, 164)], INK, 2)); o.append(P([(90, 200), (90, 336), (360, 336), (360, 312)], INK, 2))
    o.append(L(70, 164, 110, 164, INK, 3)); o.append(L(80, 176, 100, 176, INK, 3)); o.append(L(70, 188, 110, 188, INK, 3)); o.append(L(80, 200, 100, 200, INK, 3))
    o.append(T(62, 186, '10 V', 14, 'end', INK, True))
    # output meter
    o.append(L(205, 182, 336, 182, AC, 2)); o.append(L(384, 182, 515, 182, AC, 2))
    o.append(f'<circle cx="360" cy="182" r="24" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2"/>')
    o.append(T(360, 188, 'V', 16, fill=AC, bold=True))
    o.append(T(360, 228, 'output 20 mV', 14, fill=AC, bold=True)); o.append(T(360, 245, 'at 100 kPa', 13, fill=AC))
    o.append(T(560, 160, 'full bridge:', 13, 'start', MUT, True))
    o.append(T(560, 178, '100 kPa → 20 mV', 13, 'start', INK)); o.append(T(560, 196, '35 kPa → 7.0 mV', 13, 'start', INK)); o.append(T(560, 214, '0.20 mV per kPa', 13, 'start', INK))
    o.append(T(470, 362, 'ΔR = 2.0 × 0.001 × 350 Ω = 0.70 Ω;  output = 10 V × 0.70 ÷ 350 = 20 mV', 13, fill=MUT))
    return 376, ''.join(o)

FIG[10] = (f10, 'The worked example\'s pressure transducer: four 350 Ω gauges in a full bridge on 10 V. Opposite arms are strained the same way (R2 and R3 stretched, R1 and R4 compressed), so their changes add and the output is 20 mV at 100 kPa.',
          'A diamond-shaped Wheatstone bridge excited by a 10 volt battery between the top and bottom corners. The four arms are strain gauges: R1 top left compressed to 349.30 ohms, R2 top right stretched to 350.70 ohms, R3 bottom left stretched, R4 bottom right compressed. A voltmeter between the left and right corners reads 20 millivolts at 100 kilopascals. Notes give 7.0 millivolts at 35 kilopascals and 0.20 millivolts per kilopascal.')


# ---- 4.11 the signal chain from bridge to code, and the solenoid driver ----
def f11():
    o = [T(20, 26, 'Measuring: 35 kPa on the pressure transducer', 14, 'start', INK, True)]
    blocks = [(14, 'bridge', '0 to 20 mV', '7.0 mV'), (158, 'in-amp', 'gain 201.8', '1.4126 V'), (302, 'anti-alias', 'filter', '1.4126 V'), (446, '12-bit ADC', 'Q = 1 mV', 'code 1412'), (590, 'micro-', 'controller', '35.0 kPa')]
    for i, (x, a, b, v) in enumerate(blocks):
        o.append(boxt(x, 40, 116, 56, [a, b], ACS if i in (1, 3) else PANEL, AC, 13, True))
        o.append(T(x + 58, 118, v, 14, fill=NX, bold=True))
        if i < 4: o.append(L(x + 116, 68, x + 140, 68, AC, 2, arrow='n'))
    o.append(T(20, 166, 'Acting: the microcontroller switches a 28 V solenoid', 14, 'start', INK, True))
    o.append(L(648, 128, 648, 180, AC, 2, arrow='n'))
    o.append(boxt(530, 184, 176, 56, ['5 V pin, 510 Ω', 'base current 8.4 mA'], PANEL, AC, 13))
    o.append(L(530, 212, 444, 212, AC, 2, arrow='n'))
    o.append(boxt(290, 184, 150, 56, ['NPN switch', 'β ≥ 100, saturated'], ACS, AC, 13))
    o.append(L(290, 212, 210, 212, AC, 2, arrow='n'))
    o.append(boxt(20, 184, 186, 56, ['solenoid 70 Ω, 0.1 H', 'current 0.40 A'], PANEL, INK, 13))
    o.append(boxt(20, 258, 186, 44, ['flyback diode', 'across the coil'], LVS, LV, 13))
    o.append(T(220, 286, 'without it: 0.1 H × 0.40 A ÷ 1 µs = 40 kV spike', 13, 'start', LV, True))
    return 316, ''.join(o)

FIG[11] = (f11, 'The two worked examples as one chain. Top: 35 kPa gives 7.0 mV at the bridge, 1.4126 V after the gain of 201.8 and code 1412 from the 12-bit ADC. Bottom: the microcontroller pin drives the transistor through 510 Ω, the transistor switches 0.40 A through the solenoid, and the flyback diode absorbs the switch-off spike.',
          'Top row of blocks: bridge, instrumentation amplifier with gain 201.8, anti-alias filter, 12-bit ADC with 1 millivolt steps, microcontroller. Values under them: 7.0 millivolts, 1.4126 volts, 1.4126 volts, code 1412, 35.0 kilopascals. Bottom row, from right to left: a 5 volt pin with a 510 ohm base resistor giving 8.4 milliamps, an NPN transistor switch, a 70 ohm 0.1 henry solenoid carrying 0.40 amps, and a flyback diode across the coil; without it the spike would be 40 kilovolts.')

spec = make_spec(FIG)


def text_fixes(k):
    return []
