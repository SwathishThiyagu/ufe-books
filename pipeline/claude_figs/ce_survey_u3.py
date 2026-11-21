"""Claude's hand-drawn figures for ce-survey-u3 (Levelling and Contouring), one per chapter.
Every number comes from that chapter's worked example. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def staff(x, yfoot, ytop, w=10, c=NX):
    """a levelling staff standing on yfoot, drawn up to ytop"""
    return R(x - w / 2, min(ytop, yfoot), w, abs(yfoot - ytop), NXS, c, 1, 1.5)


def level(x, ygr, yhi):
    """a level on a tripod: tripod from the ground to just under the line of sight"""
    o = [L(x, yhi + 8, x - 16, ygr, INK, 1.8), L(x, yhi + 8, x + 16, ygr, INK, 1.8), L(x, yhi + 8, x, ygr, INK, 1.2)]
    o.append(R(x - 17, yhi - 6, 34, 12, PANEL, INK, 3, 1.8))
    return ''.join(o)


def brk(x, y):
    """a break mark on a vertical dimension (not to scale)"""
    return L(x - 7, y + 4, x + 7, y - 2, 'var(--fig)', 6) + L(x - 7, y + 1, x + 7, y - 5, INK, 1.5) + L(x - 7, y + 7, x + 7, y + 1, INK, 1.5)


# ---- 3.1 the height chain: datum, BM, HI, readings, RLs ----
def f1():
    o = []
    y = lambda rl: 300 - (rl - 119.5) * 70
    HI = 122.315
    yd = 372
    o.append(L(20, yd, 700, yd, INK, 2.5))
    o.append(T(360, yd + 22, 'Datum: mean sea level (RL 0.000 m)', 14, fill=MUT))
    # ground line
    gpts = [(20, y(120.30)), (110, y(120.30)), (160, y(120.55)), (250, y(120.70)), (330, y(121.25)), (440, y(121.15)),
            (480, y(120.10)), (520, y(119.90)), (560, y(120.30)), (640, y(121.065)), (700, y(121.10))]
    o.append(P(gpts, L2, 2.5))
    # culvert with BM
    o.append(R(50, y(120.45), 70, y(120.30) - y(120.45) + 26, 'var(--line)', L2, 2, 1.5))
    o.append(T(85, y(120.30) + 18, 'culvert', 13, fill=MUT))
    # building on a raised plinth
    o.append(R(345, y(121.68), 95, y(121.20) - y(121.68), 'var(--line)', L2, 0, 1.5))
    o.append(R(372, y(121.68) - 34, 66, 34, PANEL, L2, 0, 1.2))
    o.append(T(405, y(121.68) - 12, 'building', 13, fill=MUT))
    # line of collimation
    yh = y(HI)
    o.append(L(75, yh, 690, yh, AC, 2, '7 5'))
    o.append(T(400, yh - 30, 'line of collimation: HI = 120.450 + 1.865 = 122.315 m', 14, fill=AC, bold=True))
    o.append(level(250, y(120.70), yh))
    o.append(T(250, y(120.70) + 22, 'level', 13, fill=MUT))
    pts = [(85, 120.450, '1.865', 'BS', 'BM 120.450'), (360, 121.680, '0.635', 'IS', 'plinth 121.680'),
           (520, 119.905, '2.410', 'IS', 'road 119.905'), (640, 121.065, '1.250', 'FS', 'TBM 121.065')]
    for x, rl, rd, kind, lab in pts:
        o.append(staff(x, y(rl), yh - 14))
        o.append(C(x, y(rl), 4.5, INK))
        left = kind == 'IS' and rl > 121
        o.append(Tb(x + (-10 if left else 10), (y(rl) + yh) / 2 + 5, f'{kind} {rd}', 13, 'end' if left else 'start', NX, True))
        if lab.startswith(('road', 'TBM')): o.append(Tb(x, y(rl) + 22, lab, 13, fill=INK, bold=True))
        if lab.startswith('plinth'): o.append(Tb(x - 6, y(121.20) + 22, lab, 13, fill=INK, bold=True))
    o.append(Tb(160, y(120.45) - 4, 'BM 120.450', 13, fill=INK, bold=True))
    # RL dimension from datum to BM, with a break
    o.append(L(38, yd, 38, y(120.45) + 3, LV, 2, arrow='l'))
    o.append(brk(38, 338))
    o.append(T(46, 300, 'RL of BM', 13, 'start', LV, True))
    o.append(T(46, 318, '120.450 m', 13, 'start', LV, True))
    return 404, ''.join(o)
FIG[1] = (f1, 'The worked example in section. The backsight on the benchmark lifts the height to the line of collimation (HI 122.315 m); each staff reading is then subtracted from the HI. The RLs are heights above mean sea level, which is drawn with a break because it is far below.',
          'Section through the site: a benchmark on a culvert at RL 120.450 m, a level whose line of collimation is at 122.315 m, and staffs on a building plinth, a road edge and a temporary benchmark with their readings and reduced levels above the mean sea level datum.')


# ---- 3.2 two-peg test ----
def f2():
    o = []
    sx, vy = 4.5, 60          # px per m along the line, px per m vertically
    xA, xB = 150, 150 + 100 * sx
    tilt = 24                 # drawn rise of the line of sight over 100 m (exaggerated; really 0.018 m)
    def ground(g0):
        gB = g0 + 0.49 * vy
        o.append(L(30, g0, xA + 30, g0, L2, 2)); o.append(L(xA + 30, g0, xB - 30, gB, L2, 2)); o.append(L(xB - 30, gB, 700, gB, L2, 2))
        return gB
    gy = lambda g0, x: g0 if x <= xA + 30 else (g0 + 0.49 * vy if x >= xB - 30 else g0 + 0.49 * vy * (x - xA - 30) / (xB - xA - 60))
    # panel 1: midway
    g0 = 176
    o.append(T(20, 22, 'Level midway at C: both sights 50 m, so both readings carry the same error', 14, 'start', bold=True))
    gB = ground(g0)
    xc = (xA + xB) / 2; yh = g0 - 1.616 * vy
    o.append(L(xA - 20, yh, xB + 20, yh, L2, 1.5, '6 5'))
    o.append(level(xc, gy(g0, xc), yh))
    hitA, hitB = yh - tilt / 2, yh - tilt / 2
    o.append(L(xc, yh, xA, hitA, AC, 2.2)); o.append(L(xc, yh, xB, hitB, AC, 2.2))
    o.append(staff(xA, g0, hitA - 16)); o.append(staff(xB, gB, hitB - 16))
    o.append(T(xA, g0 + 20, 'A', 15, bold=True)); o.append(T(xB, gB + 20, 'B', 15, bold=True)); o.append(T(xc, gy(g0, xc) + 20, 'C', 15, bold=True))
    o.append(Tb(xA + 12, hitA - 8, 'reads 1.625', 13, 'start', AC, True))
    o.append(Tb(xB - 12, hitB - 8, 'reads 2.115', 13, 'end', AC, True))
    o.append(Tb(xc, gB + 44, 'true difference = 2.115 − 1.625 = 0.490 m (B lower)', 14, 'middle', INK, True))
    # panel 2: level at D, 10 m beyond A
    g0 = 462
    o.append(T(20, 290, 'Level at D, 10 m beyond A: sights 10 m and 110 m', 14, 'start', bold=True))
    gB = ground(g0)
    xd = xA - 10 * sx - 20; yh = g0 - 1.433 * vy
    o.append(L(xd - 10, yh, xB + 20, yh, L2, 1.5, '6 5'))
    o.append(level(xd, g0, yh))
    hitA = yh - tilt * 10 / 110; hitB = yh - tilt
    o.append(L(xd, yh, xB, hitB, AC, 2.2))
    o.append(staff(xA, g0, hitA - 16)); o.append(staff(xB, gB, hitB - 16))
    o.append(T(xA, g0 + 20, 'A', 15, bold=True)); o.append(T(xB, gB + 20, 'B', 15, bold=True)); o.append(T(xd, g0 + 20, 'D', 15, bold=True))
    o.append(Tb(xA + 12, hitA - 26, 'reads 1.435 (should be 1.433)', 13, 'start', AC, True))
    o.append(Tb(xB - 12, hitB - 8, 'reads 1.943', 13, 'end', AC, True))
    o.append(Tb(xB - 12, yh + 18, 'should read 1.923', 13, 'end', INK, True))
    o.append(L(xB + 14, yh, xB + 14, hitB, LV, 2))
    o.append(L(xB + 9, yh, xB + 19, yh, LV, 2)); o.append(L(xB + 9, hitB, xB + 19, hitB, LV, 2))
    o.append(T(xB + 24, yh - 8, '0.020 m', 13, 'start', LV, True))
    o.append(Tb(380, gB + 44, 'apparent 0.508 − true 0.490 = 0.018 m in 100 m: e = 0.00018 per m (37″, upward)', 13, 'middle', INK, True))
    o.append(T(20, gB + 72, 'Dashed: true horizontal through the instrument. Solid: actual line of sight (tilt exaggerated).', 13, 'start', MUT))
    return gB + 86, ''.join(o)
FIG[2] = (f2, 'The two-peg test of the worked example. From the midpoint C both readings carry the same error, so they give the true difference of 0.490 m. From D the far sight is 100 m longer, so its extra 0.018 m is the collimation error: the staff on B should read 1.923 m.',
          'Two side views of pegs A and B 100 metres apart. Top: a level midway reads 1.625 on A and 2.115 on B. Bottom: a level 10 metres beyond A reads 1.435 and 1.943, and the correct reading on B is 1.923, showing a line of sight inclined upward by 0.018 metres in 100 metres.')


# ---- 3.3 longitudinal section with formation, cut and fill ----
def f3():
    o = []
    ch = [0, 20, 40, 60, 80, 100, 120]
    g = [84.805, 84.360, 83.725, 83.390, 82.715, 82.150, 81.595]
    f = [84.200 - c / 50 for c in ch]
    x0, x1, yt, yb = 150, 680, 40, 290
    fx = lambda c: x0 + (c / 120) * (x1 - x0)
    fy = lambda r: yb - (r - 81.0) / 4.0 * (yb - yt)
    o.append(axes(x0, x1, yt, yb, [], [81, 82, 83, 84, 85], fx, fy, '', 'RL (m)', yfmt=lambda v: f'{v:.0f}'))
    zx = 93.94
    zr = 82.715 + (82.150 - 82.715) * (zx - 80) / 20
    # cut area (ground above formation) from 0 to zero point; fill area after
    cut = [(fx(c), fy(r)) for c, r in zip(ch[:5], g[:5])] + [(fx(zx), fy(zr))] + [(fx(zx), fy(zr))] + [(fx(c), fy(r)) for c, r in reversed(list(zip(ch[:5], f[:5])))]
    o.append(f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in cut)}" style="fill:var(--live-soft);stroke:none"/>')
    fil = [(fx(zx), fy(zr)), (fx(100), fy(82.200)), (fx(120), fy(81.800)), (fx(120), fy(81.595)), (fx(100), fy(82.150))]
    o.append(f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in fil)}" style="fill:var(--next-soft);stroke:none"/>')
    o.append(P([(fx(c), fy(r)) for c, r in zip(ch, g)], INK, 2.5))
    o.append(P([(fx(c), fy(r)) for c, r in zip(ch, f)], AC, 2.5, '8 5'))
    for c, r in zip(ch, g):
        o.append(C(fx(c), fy(r), 4.5, INK))
        o.append(L(fx(c), yb, fx(c), yb + 4, L2, 1))
    o.append(Tb(fx(32), fy(84.55) - 14, 'ground', 14, fill=INK, bold=True))
    o.append(T(fx(12), fy(83.0) + 50, 'formation, falling 1 in 50', 14, 'start', AC, True))
    o.append(T(fx(5), fy(84.42) + 5, 'cutting', 14, 'start', LV, True))
    o.append(Tb(fx(112), fy(81.95) - 22, 'filling', 14, fill=NX, bold=True))
    o.append(L(fx(zx), fy(zr) + 8, fx(zx), fy(zr) + 52, LV, 1.8))
    o.append(Tb(fx(zx), fy(zr) + 68, 'zero point 93.94 m', 13, fill=INK, bold=True))
    o.append(T(fx(60), fy(83.39) - 14, 'CP', 13, fill=MUT, bold=True))
    # data strip like an L-section sheet
    rows = [('Chainage (m)', [str(c) for c in ch]), ('Ground RL', [f'{v:.3f}' for v in g]), ('Formation RL', [f'{v:.3f}' for v in f]),
            ('Cut / fill (m)', ['+0.605', '+0.560', '+0.325', '+0.390', '+0.115', '−0.050', '−0.205'])]
    ys = yb + 30
    for i, (lab, vals) in enumerate(rows):
        yy = ys + i * 22
        o.append(T(14, yy, lab, 13, 'start', MUT, True))
        for c, v in zip(ch, vals):
            col = INK if i < 3 else (LV if v.startswith('+') else NX)
            o.append(T(fx(c), yy, v, 13, fill=col, bold=(i == 3)))
    o.append(T(14, ys + 4 * 22, '+ cut, − fill. Vertical scale exaggerated about 30 times.', 13, 'start', MUT))
    return ys + 4 * 22 + 14, ''.join(o)
FIG[3] = (f3, 'The longitudinal section of the worked example. The road is in cutting where the ground line is above the formation line and in filling where it is below; the two lines cross at chainage 93.94 m.',
          'Longitudinal section from chainage 0 to 120 metres showing the ground line falling from 84.805 to 81.595 metres, a formation line falling at 1 in 50 from 84.200 metres, cutting shaded up to the zero point at 93.94 metres and filling beyond it, with a table of the ground and formation levels.')


# ---- 3.4 field sketch of the booking example ----
def f4():
    o = []
    y = lambda rl: 330 - (rl - 93.3) * 33
    st = [('BM', 40, 100.000), ('P1', 105, 99.365), ('P2', 170, 98.590), ('CP1', 245, 97.825), ('P3', 372, 96.940),
          ('CP2', 505, 95.455), ('P4', 590, 94.330), ('TBM', 680, 93.695)]
    gpts = [(20, y(100.0)), (40, y(100.0)), (105, y(99.365)), (170, y(98.590)), (245, y(97.825)), (330, y(97.55)),
            (362, y(96.94)), (372, y(96.94)), (392, y(96.35)), (420, y(96.45)), (446, y(96.70)), (505, y(95.455)),
            (590, y(94.330)), (680, y(93.695)), (705, y(93.6))]
    o.append(P(gpts, L2, 2.5))
    # bridge deck over the stream
    ys = y(100.130)
    o.append(R(330, ys - 20, 125, 20, 'var(--line)', INK, 0, 1.8))
    o.append(T(462, ys - 6, 'bridge deck', 13, 'start', MUT))
    o.append(T(425, y(96.35) + 30, 'stream', 13, fill=MUT))
    def gyx(x):
        for (xa, ya), (xb, yb) in zip(gpts, gpts[1:]):
            if xa <= x <= xb: return ya + (yb - ya) * (x - xa) / (xb - xa)
        return gpts[-1][1]
    setups = [(72, 101.235, 40, 245, 'HI 101.235'), (345, 98.405, 245, 505, 'HI 98.405'), (548, 96.560, 505, 680, 'HI 96.560')]
    for xi, hi, xa, xb, lab in setups:
        yh = y(hi)
        o.append(L(xa, yh, xb, yh, AC, 1.8, '6 4'))
        o.append(level(xi, gyx(xi), yh))
        o.append(Tb(xi, yh - 14, lab, 13, fill=AC, bold=True))
    reads = {'BM': ('1.235', 101.235), 'P1': ('1.870', 101.235), 'P2': ('2.645', 101.235), 'P3': ('1.465', 98.405),
             'P4': ('2.230', 96.560), 'TBM': ('2.865', 96.560)}
    for name, x, rl in st:
        o.append(C(x, y(rl), 4, INK))
        if name in reads:
            r, hi = reads[name]
            o.append(staff(x, y(rl), y(hi) - 6, 8))
        o.append(T(x, y(rl) + 20, name, 13, bold=True))
        o.append(T(x, y(rl) + 36, f'{rl:.3f}', 13, fill=MUT))
    # change points: staff up to the higher HI of the two set-ups
    o.append(staff(245, y(97.825), y(101.235) - 6, 8)); o.append(staff(505, y(95.455), y(98.405) - 6, 8))
    lab = [(40, 101.235, '1.235', 'start', 18), (105, 101.235, '1.870', 'start', 18), (170, 101.235, '2.645', 'start', 18),
           (372, 98.405, '1.465', 'start', 18), (590, 96.560, '2.230', 'start', 40), (680, 96.560, '2.865', 'end', 18)]
    for x, hi, r, a, dy in lab:
        o.append(Tb(x + (8 if a == 'start' else -8), y(hi) + dy, r, 13, a, NX, True))
    o.append(Tb(253, y(101.235) + 18, 'FS 3.410', 13, 'start', NX, True))
    o.append(Tb(253, y(98.405) + 18, 'BS 0.580', 13, 'start', NX, True))
    o.append(Tb(497, y(98.405) + 18, 'FS 2.950', 13, 'end', NX, True))
    o.append(Tb(513, y(96.560) + 18, 'BS 1.105', 13, 'start', NX, True))
    # inverted staff from the soffit down to the line of sight
    o.append(staff(404, y(98.405) + 4, ys, 8, LV))
    o.append(Tb(414, (ys + y(98.405)) / 2 + 4, '−1.725', 13, 'start', LV, True))
    o.append(Tb(468, ys + 30, 'S: 98.405 + 1.725 = 100.130', 13, 'start', LV, True))
    o.append(T(20, 380, 'Dashed: line of sight of each set-up. Readings beside each staff; RLs (m) under each station.', 13, 'start', MUT))
    return 392, ''.join(o)
FIG[4] = (f4, 'The level run of the worked example seen from the side: three set-ups, two change points, and the staff held upside down against the bridge soffit, which is why that reading is booked as −1.725 and added to the HI.',
          'Side view of ground falling from a benchmark at RL 100.000 metres to a temporary benchmark at 93.695 metres, with three level set-ups at heights of instrument 101.235, 98.405 and 96.560 metres, change points CP1 and CP2, and an inverted staff under a bridge soffit at 100.130 metres.')


# ---- 3.5 curvature and refraction; reciprocal levelling ----
def f5():
    o = [T(20, 24, 'Curvature and refraction on a long sight', 15, 'start', bold=True)]
    xa, Rr = 60, 900
    cy = 175 + Rr                           # earth centre directly below A, so the horizontal line touches the level line at A
    surf = lambda x, r: cy - math.sqrt(r * r - (x - xa) ** 2)
    o.append(P([(x, surf(x, Rr)) for x in range(30, 345, 5)], L2, 2.5))
    yi = 145
    o.append(level(xa, 175, yi))
    o.append(T(xa, 197, 'A', 14, bold=True))
    xb = 300
    o.append(L(xa, yi, 345, yi, AC, 2.2))
    rl = Rr + (175 - yi)
    o.append(P([(x, surf(x, rl)) for x in range(xa, 345, 5)], MUT, 1.6, '6 4'))
    yl = surf(xb, rl)
    yr = yi + 10
    o.append(f'<path d="M{xa:.1f},{yi:.1f} Q{(xa + xb) / 2:.1f},{yi - 2:.1f} {xb:.1f},{yr:.1f}" style="fill:none;stroke:{LV};stroke-width:2.2"/>')
    o.append(staff(xb, surf(xb, Rr), yi - 18, 10))
    o.append(T(xb, surf(xb, Rr) + 22, 'B', 14, bold=True))
    xd = xb + 18
    for (y1, y2, lab, c, dx) in ((yi, yl, 'C', INK, 0), (yi, yr, 'C', LV, 22)):
        o.append(L(xd + dx, y1, xd + dx, y2, c, 1.6)); o.append(L(xd + dx - 4, y1, xd + dx + 4, y1, c, 1.6)); o.append(L(xd + dx - 4, y2, xd + dx + 4, y2, c, 1.6))
    o.append(T(xd + 4, (yi + yl) / 2 + 26, 'C<tspan baseline-shift="sub" font-size="11">c</tspan>', 13, 'start', INK, True))
    o.append(T(xd + 26, yi - 6, 'C<tspan baseline-shift="sub" font-size="11">r</tspan>', 13, 'start', LV, True))
    ly = 238
    for i, (lab, c, d) in enumerate((('horizontal line', AC, None), ('level line', MUT, '6 4'), ('refracted ray', LV, None))):
        lx = 20 + i * 122
        o.append(L(lx, ly - 5, lx + 18, ly - 5, c, 2.2, d)); o.append(T(lx + 24, ly, lab, 13, 'start', c, True))
    o.append(T(20, 266, 'C<tspan baseline-shift="sub" font-size="11">c</tspan> = 0.0785 d² (curvature), C<tspan baseline-shift="sub" font-size="11">r</tspan> = 0.0112 d² (refraction)', 13, 'start', INK))
    o.append(T(20, 286, 'Net C = 0.0673 d², subtracted (d in km, C in m)', 13, 'start', INK, True))
    o.append(T(20, 306, 'At d = 0.8 km: C = 0.0673 × 0.64 = 0.043 m', 13, 'start', INK))
    # right panel: reciprocal levelling
    x0 = 400
    o.append(T(x0, 24, 'Reciprocal levelling across 800 m', 15, 'start', bold=True))
    gy = 176
    xA, xB = x0 + 34, x0 + 262
    o.append(L(x0, gy, x0 + 60, gy, L2, 2.5)); o.append(L(x0 + 240, gy + 8, 712, gy + 8, L2, 2.5))
    o.append(f'<path d="M{x0 + 60},{gy} Q{x0 + 150},{gy + 40} {x0 + 240},{gy + 8}" style="fill:var(--accent-soft);stroke:{L2};stroke-width:2"/>')
    o.append(T(x0 + 150, gy + 20, 'river', 13, fill=MUT))
    o.append(staff(xA, gy, gy - 110, 10)); o.append(staff(xB, gy + 8, gy - 110, 10))
    o.append(T(xA, gy + 22, 'A', 14, bold=True)); o.append(T(xB, gy + 30, 'B', 14, bold=True))
    o.append(level(x0 + 12, gy, gy - 58)); o.append(L(x0 + 12, gy - 58, xB, gy - 58, AC, 1.8, '6 4'))
    o.append(level(xB + 26, gy + 8, gy - 88)); o.append(L(xA, gy - 88, xB + 26, gy - 88, LV, 1.8, '6 4'))
    o.append(Tb(x0 + 150, gy - 64, 'near A: A 1.428, B 2.365', 13, fill=AC, bold=True))
    o.append(Tb(x0 + 150, gy - 94, 'near B: B 1.815, A 0.980', 13, fill=LV, bold=True))
    o.append(T(x0, 266, 'h = ½(0.937 + 0.835) = 0.886 m, B lower', 13, 'start', INK, True))
    o.append(T(x0, 286, 'far-sight error e = ½(0.937 − 0.835)', 13, 'start', INK))
    o.append(T(x0, 306, '= 0.051 m = 0.043 (C) + 0.008 (collimation)', 13, 'start', INK))
    o.append(T(20, 334, 'Curvature and refraction drawn much larger than real; over 0.8 km C is only 43 mm.', 13, 'start', MUT))
    return 346, ''.join(o)
FIG[5] = (f5, 'Left: the far staff is read where the horizontal line meets it, above the level line by C = 0.0785 d²; refraction bends the ray down by about a seventh of that, so the net correction is 0.0673 d². Right: the two set-ups of the worked example, whose average cancels the far-sight error of 0.051 m.',
          'Left, a curved earth surface with a level at A, the horizontal line of sight, the curved level line and a refracted ray meeting a staff at B, with the curvature correction marked. Right, reciprocal levelling across a river with readings from a level near each bank and the computed difference of 0.886 metres.')


# ---- 3.6 contours interpolated on a grid ----
def f6():
    o = []
    G = [[101.6, 102.4, 103.5], [100.8, 101.7, 102.6], [100.2, 100.9, 101.8]]
    nm = ['A', 'B', 'C']
    x0, y0, s = 90, 64, 6.0   # 6 px per m, 20 m squares = 120 px
    X = lambda j: x0 + j * 20 * s
    Y = lambda r: y0 + r * 20 * s
    for r in range(3):
        o.append(L(X(0), Y(r), X(2), Y(r), L2, 1.5))
    for j in range(3):
        o.append(L(X(j), Y(0), X(j), Y(2), L2, 1.5))

    def cr(c):
        pts = {}
        for r in range(3):
            for j in range(2):
                z1, z2 = G[r][j], G[r][j + 1]
                if (z1 - c) * (z2 - c) < 0: pts[('h', r, j)] = (X(j) + (c - z1) / (z2 - z1) * 20 * s, Y(r))
        for j in range(3):
            for r in range(2):
                z1, z2 = G[r][j], G[r + 1][j]
                if (z1 - c) * (z2 - c) < 0: pts[('v', r, j)] = (X(j), Y(r) + (c - z1) / (z2 - z1) * 20 * s)
        return pts
    paths = {101: [('v', 0, 0), ('h', 1, 0), ('v', 1, 1), ('h', 2, 1)], 102: [('h', 0, 0), ('v', 0, 1), ('h', 1, 1), ('v', 1, 2)],
             103: [('h', 0, 1), ('v', 0, 2)]}
    for r in range(3):
        for j in range(3):
            o.append(C(X(j), Y(r), 5, INK))
            lab = f'{nm[r]}{j + 1} {G[r][j]:.1f}'
            if r == 0: o.append(T(X(j) + 6, Y(r) - 14, lab, 13, 'start', INK, True))
            elif r == 2: o.append(T(X(j) + 6, Y(r) + 22, lab, 13, 'start', INK, True))
            elif j == 0: o.append(T(X(j) - 10, Y(r) + 5, lab, 13, 'end', INK, True))
            elif j == 1: o.append(T(X(j) - 8, Y(r) - 10, lab, 13, 'end', INK, True))
            else: o.append(T(X(j) + 10, Y(r) + 5, lab, 13, 'start', INK, True))
    for c, seq in paths.items():
        p = cr(c)
        line = [p[k] for k in seq]
        o.append(P(line, AC, 2.6))
        for q in line:
            o.append(C(q[0], q[1], 3.5, AC))
    o.append(Tb(X(0) + 54, Y(1) + 52, '101', 14, fill=AC, bold=True))
    o.append(Tb(X(1) + 30, Y(0) + 86, '102', 14, fill=AC, bold=True))
    o.append(Tb(X(2) - 40, Y(0) + 40, '103', 14, fill=AC, bold=True))
    o.append(T(X(1), Y(2) + 48, '20 m squares (block levelling)', 13, fill=MUT))
    # crossing table
    tx = 420
    o.append(T(tx, 40, 'Where each contour crosses', 14, 'start', bold=True))
    rows = [('101 m', '15.0 m from A1 on A1–B1'), ('', '4.4 m from B1 on B1–B2'), ('', '17.5 m from B2 on B2–C2'), ('', '2.2 m from C2 on C2–C3'),
            ('102 m', '10.0 m from A1 on A1–A2'), ('', '11.4 m from A2 on A2–B2'), ('', '6.7 m from B2 on B2–B3'), ('', '15.0 m from B3 on B3–C3'),
            ('103 m', '10.9 m from A2 on A2–A3'), ('', '11.1 m from A3 on A3–B3')]
    for i, (c_, t_) in enumerate(rows):
        if c_: o.append(T(tx, 66 + i * 21, c_, 13, 'start', AC, True))
        o.append(T(tx + 50, 66 + i * 21, t_, 13, 'start', INK))
    o.append(T(tx, 66 + 10 * 21 + 8, 'x = 20 × (H − H₁) ÷ (H₂ − H₁) m', 13, 'start', MUT, True))
    o.append(T(tx, 66 + 10 * 21 + 28, 'ground rises to the north-east (A3)', 13, 'start', MUT))
    return 364, ''.join(o)
FIG[6] = (f6, 'The grid of the worked example with its spot levels and the 101 m, 102 m and 103 m contours joined through the interpolated crossing points. The lines are evenly spaced, so the slope is fairly uniform, rising towards A3.',
          'A three by three grid of points at 20 metre spacing with reduced levels from 100.2 to 103.5 metres, and the 101, 102 and 103 metre contours drawn through points interpolated along the grid lines, with a list of the crossing distances.')


# ---- 3.7 capacity-elevation curve ----
def f7():
    o = []
    lev = [99.2, 100, 102, 104, 106, 108, 110, 112]
    cap = [0, 0.933, 15.433, 46.933, 99.433, 177.433, 284.433, 423.933]  # thousand m3
    x0, x1, yt, yb = 90, 640, 40, 330
    fx = lambda v: x0 + v / 450 * (x1 - x0)
    fy = lambda e: yb - (e - 99) / 13.5 * (yb - yt)
    o.append(axes(x0, x1, yt, yb, [0, 100, 200, 300, 400], [100, 102, 104, 106, 108, 110, 112], fx, fy,
                  'capacity (thousand m³)', 'water level, RL (m)', yfmt=lambda v: f'{v}'))
    # dead storage band and FSL
    o.append(L(x0, fy(102), x1, fy(102), NX, 1.8, '6 4'))
    o.append(Tb(x1 - 4, fy(102) - 8, 'outlet sill 102.0', 13, 'end', NX, True))
    o.append(L(x0, fy(110), x1, fy(110), LV, 1.8, '6 4'))
    o.append(Tb(x0 + 40, fy(110) + 18, 'full reservoir level 110.0', 13, 'start', LV, True))
    o.append(P([(fx(c), fy(e)) for c, e in zip(cap, lev)], AC, 2.8))
    for c, e in zip(cap[1:], lev[1:]):
        o.append(C(fx(c), fy(e), 4.5, AC))
    for c, e, lab, pos in [(46.933, 104, '46 933', 'rb'), (99.433, 106, '99 433', 'rb'), (177.433, 108, '177 433', 'la'), (284.433, 110, '284 433', 'rb'), (423.933, 112, '423 933', 'rb')]:
        if pos == 'rb': o.append(Tb(fx(c) + 10, fy(e) + 18, lab, 13, 'start', INK, True))
        else: o.append(Tb(fx(c) - 10, fy(e) - 8, lab, 13, 'end', INK, True))
    ya = fy(110) - 16
    o.append(L(fx(15.433) + 2, ya, fx(284.433) - 8, ya, LV, 1.8, arrow='l'))
    o.append(L(fx(284.433) - 2, ya, fx(15.433) + 8, ya, LV, 1.8, arrow='l'))
    o.append(L(fx(15.433), fy(102), fx(15.433), ya - 6, NX, 1.2, '3 3'))
    o.append(Tb((fx(15.433) + fx(284.433)) / 2, ya - 10, 'live storage = 284 433 − 15 433 = 269 000 m³', 13, 'middle', LV, True))
    o.append(Tb(fx(15.433) + 10, fy(102) + 18, 'dead storage 15 433 m³', 13, 'start', NX, True))
    o.append(T(20, yb + 62, 'Capacities by the trapezoidal rule, including the 933 m³ cone below the 100 m contour (deepest point 99.2 m).', 13, 'start', MUT))
    return yb + 76, ''.join(o)
FIG[7] = (f7, 'The capacity–elevation curve of the worked example. Read across from a water level to the curve and down to the capacity; the storage between the outlet sill and the full reservoir level is the live storage of 269 000 m³.',
          'A capacity against water level curve rising from zero at RL 99.2 metres to 284 433 cubic metres at the full reservoir level of 110 metres and 423 933 at 112 metres, with the outlet sill at 102 metres marking the dead storage of 15 433 cubic metres and a bracket for the live storage.')


spec = make_spec(FIG)
