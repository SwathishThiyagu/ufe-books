"""Claude's hand-drawn figures for ce-survey-u1 (Surveying principles and distances), one per chapter.
Every number comes from that chapter's worked example. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def sb(base, s, size=11):
    return f'{base}<tspan baseline-shift="sub" font-size="{size}">{s}</tspan>'


def dim_h(x1, x2, y, label, size=14, c=MUT, fill=INK):
    return (L(x1, y, x2, y, c, 1.5) + L(x1, y - 6, x1, y + 6, c, 1.5) + L(x2, y - 6, x2, y + 6, c, 1.5)
            + Tb((x1 + x2) / 2, y - 7, label, size, fill=fill))


# ---- 1.1 plane or geodetic: the curvature correction, and the three ways of classifying ----
def f1():
    o = [T(20, 26, 'Does the curvature matter? c = d² / 2R', 15, 'start', bold=True)]
    # tangent (horizontal line) and the level line curving away from it
    xa, ya, xb = 50, 70, 430
    o.append(L(xa, ya, xb, ya, AC, 2.5))
    pts = [(xa + t * (xb - xa), ya + 70 * t * t) for t in [i / 30 for i in range(31)]]
    o.append(P(pts, LV, 2.5))
    o.append(C(xa, ya, 5, INK))
    o.append(T(xa, ya - 12, 'A', 14, bold=True))
    o.append(Tb(240, ya - 10, 'horizontal line, d = 10 km', 14, fill=AC))
    o.append(T(160, ya + 36, 'level line (the earth’s curve)', 14, fill=LV))
    o.append(L(xb, ya, xb, ya + 70, INK, 1.8, arrow=None))
    o.append(L(xb - 6, ya, xb + 6, ya, INK, 1.5) + L(xb - 6, ya + 70, xb + 6, ya + 70, INK, 1.5))
    o.append(T(xb + 10, ya + 32, 'c = 7.85 m', 14, 'start', bold=True))
    o.append(T(xb + 10, ya + 50, '(not to scale)', 13, 'start', MUT))
    # table of c
    tx, ty = 560, 46
    o.append(R(tx, ty, 150, 128, PANEL, L2, 8, 1.5))
    o.append(T(tx + 45, ty + 22, 'd', 14, bold=True) + T(tx + 110, ty + 22, 'c', 14, bold=True))
    for i, (d, c) in enumerate([('1 km', '0.08 m'), ('5 km', '1.96 m'), ('10 km', '7.85 m'), ('30 km', '70.6 m')]):
        y = ty + 46 + i * 22
        o.append(T(tx + 45, y, d, 14) + T(tx + 110, y, c, 14, fill=(AC if d == '10 km' else INK), bold=(d == '10 km')))
    o.append(T(20, 172, 'R = 6371 km; 10 000² / (2 × 6 371 000) = 7.85 m', 14, 'start', MUT))
    # three bases of classification
    y0 = 200
    o.append(T(20, y0, 'Three ways to classify a survey', 15, 'start', bold=True))
    cols = [('By purpose', ['topographic', 'cadastral', 'engineering', 'control', 'hydrographic', 'astronomical'], ACS, AC),
            ('By instrument', ['chain or tape', 'compass', 'theodolite', 'total station', 'GNSS'], LVS, LV),
            ('By curvature', ['plane: earth flat,', 'up to about 250 km²', '(town of 96 km²)', 'geodetic: spheroid', '(600 km baseline)'], NXS, NX)]
    for i, (h, items, f, s) in enumerate(cols):
        x = 20 + i * 232
        o.append(R(x, y0 + 14, 216, 186, f, s, 8, 2))
        o.append(T(x + 108, y0 + 38, h, 15, bold=True))
        for j, it in enumerate(items):
            o.append(T(x + 108, y0 + 66 + j * 22, it, 14))
    return y0 + 214, ''.join(o)
FIG[1] = (f1, 'Over a 10 km sight the level line falls 7.85 m below the horizontal line, and the fall grows with the square of the distance. The town of 96 km² can be surveyed as a plane survey; the 600 km baseline needs geodetic work.',
          'A horizontal line and the curved level line from point A drawn over 10 kilometres with the 7.85 metre gap at the end, a table of the curvature correction for 1, 5, 10 and 30 kilometres, and three boxes classifying surveys by purpose, by instrument and by curvature.')


# ---- 1.2 precise but not accurate: the five readings on a number line ----
def f2():
    o = [T(20, 26, 'Five readings of a line whose true length is 100.00 m', 15, 'start', bold=True)]
    x0, x1, v0, v1 = 60, 680, 99.98, 100.07
    fx = lambda v: x0 + (v - v0) / (v1 - v0) * (x1 - x0)
    ya = 170
    o.append(xaxis(x0, x1, ya, [99.98, 100.00, 100.02, 100.04, 100.06], fx, 'length (m)', lambda v: f'{v:.2f}'))
    # band of ±s about the mean
    m, s = 100.03, 0.016
    o.append(R(fx(m - s), 60, fx(m + s) - fx(m - s), ya - 60, LVS, LV, 0, 1, '5 4'))
    o.append(T(fx(m), 76, '± s = ± 0.016 m', 13, fill=LV, bold=True))
    # true value
    o.append(L(fx(100.00), 50, fx(100.00), ya, NX, 2.5))
    o.append(Tb(fx(100.00), 46, 'true 100.00', 14, fill=NX, bold=True))
    # readings as dots, stacked lightly to avoid touching
    for v, dy in [(100.01, 0), (100.02, 0), (100.03, 0), (100.04, 0), (100.05, 0)]:
        o.append(C(fx(v), ya - 32 + dy, 7, AC))
    o.append(T(fx(100.01), ya - 48, '100.01', 13, fill=MUT))
    o.append(T(fx(100.05), ya - 48, '100.05', 13, fill=MUT))
    # mean marker
    o.append(L(fx(m), 92, fx(m), ya - 42, INK, 2))
    o.append(Tb(fx(m), 108, 'mean 100.03', 14, bold=True))
    # bias arrow below the axis
    yb = ya + 62
    o.append(L(fx(100.00), yb, fx(m) - 2, yb, AC, 2.5, arrow='n'))
    o.append(T((fx(100.00) + fx(m)) / 2, yb + 22, 'bias +0.03 m', 14, fill=AC, bold=True))
    o.append(boxt(440, yb - 20, 260, 58, ['precise: small scatter', 'not accurate: mean 30 mm high'], PANEL, L2, 14))
    o.append(T(20, yb + 62, 'Averaging shrinks the scatter of the mean (0.016/√5 = 0.007 m) but leaves the 0.03 m bias.', 14, 'start', MUT))
    return yb + 80, ''.join(o)
FIG[2] = (f2, 'The five readings sit close together (s = 0.016 m) but all lie above the true 100.00 m; their mean is 0.03 m high. The set is precise but not accurate, and the bias must be found by calibration and removed by a correction.',
          'A number line from 99.98 to 100.07 metres with the true value at 100.00, five readings from 100.01 to 100.05, their mean at 100.03 with a band of one standard deviation, and an arrow showing the bias of 0.03 metres.')


# ---- 1.3 reading 6.4 cm on a plain scale of 1:25 000 ----
def f3():
    o = [T(20, 26, 'Plain scale for RF 1:25 000 (1 km is drawn 4 cm long)', 15, 'start', bold=True)]
    cm = 40  # px per cm in this drawing
    zero = 40 + 4 * cm
    fx = lambda km: zero + km * 4 * cm
    y, hgt = 120, 20
    # bar: left division -1..0 subdivided, then 0..3 km
    o.append(R(fx(-1), y, fx(3) - fx(-1), hgt, PANEL, INK, 0, 1.5))
    for km in (0, 1, 2):
        o.append(R(fx(km), y, 4 * cm, hgt, (ACS if km % 2 == 0 else PANEL), INK, 0, 1.5))
    for i in range(10):
        o.append(R(fx(-1) + i * 0.4 * cm, y, 0.4 * cm, hgt / 2, (LVS if i % 2 == 0 else PANEL), INK, 0, 1))
    for km in (1, 2, 3):
        o.append(T(fx(km), y + hgt + 20, f'{km} km', 14))
    o.append(T(fx(0), y + hgt + 20, '0', 14, bold=True))
    o.append(T(fx(-1), y + hgt + 20, '1 km', 14))
    o.append(T((fx(-1) + fx(0)) / 2, y + hgt + 40, '10 parts of 100 m', 13, fill=LV))
    # divider from the 1 km mark to the 600 m sub-division
    xa, xb = fx(1), fx(-0.6)
    yd = y - 12
    o.append(L(xb, yd, xa, yd, AC, 2.5))
    o.append(L(xb, yd - 8, xb, y + hgt, AC, 2) + L(xa, yd - 8, xa, y + hgt, AC, 2))
    o.append(Tb((xa + xb) / 2, yd - 14, 'divider set to 6.4 cm on the map', 14, fill=AC, bold=True))
    o.append(T(xb, yd - 44, '600 m', 14, fill=AC))
    o.append(T(xa, yd - 44, '1 km', 14, fill=AC))
    o.append(T(20, y + hgt + 78, 'Reading: 1 km + 600 m = 1.6 km. Check: 6.4 cm × 25 000 = 160 000 cm = 1.6 km.', 14, 'start'))
    # road 3.5 km
    yr = y + hgt + 128
    o.append(T(20, yr - 18, 'The 3.5 km road on the same map', 15, 'start', bold=True))
    o.append(L(fx(-1), yr, fx(-1) + 14 * cm, yr, NX, 4))
    o.append(dim_h(fx(-1), fx(-1) + 14 * cm, yr + 26, '350 000 cm ÷ 25 000 = 14 cm', fill=NX))
    return yr + 50, ''.join(o)
FIG[3] = (f3, 'The plain scale of 1:25 000 has its first kilometre split into ten parts of 100 m. Set to the 6.4 cm between the two points, the divider spans 1 km plus 600 m, so they are 1.6 km apart; the 3.5 km road is drawn 14 cm long.',
          'A plain scale for 1 to 25000 with a subdivided left kilometre, a divider spanning from the 1 kilometre mark to the 600 metre subdivision, reading 1.6 kilometres, and a line 14 centimetres long for a 3.5 kilometre road.')


# ---- 1.4 h, H and N at the pillar, and the UTM zone of the second point ----
def f4():
    o = [T(20, 26, 'Heights at the survey pillar', 15, 'start', bold=True)]
    # surfaces: terrain, ellipsoid, geoid 82 m below
    o.append(P([(20, 92), (120, 70), (220, 80), (300, 66), (420, 74)], INK, 2))
    o.append(T(60, 64, 'ground', 13, fill=MUT))
    ye, yg = 150, 240
    o.append(L(20, ye, 420, ye, AC, 2.5)); o.append(T(30, ye - 8, 'ellipsoid', 13, 'start', AC))
    o.append(P([(20, yg + 6), (140, yg - 4), (260, yg + 2), (420, yg - 6)], LV, 2.5, '7 5'))
    o.append(T(30, yg + 26, 'geoid (mean sea level)', 13, 'start', LV))
    px, py = 300, 66
    o.append(C(px, py, 6, AC)); o.append(T(px + 12, py - 8, 'P', 14, 'start', bold=True))
    o.append(L(px - 30, py, px - 30, ye, INK, 2) + L(px - 36, py, px - 24, py, INK, 1.5) + L(px - 36, ye, px - 24, ye, INK, 1.5))
    o.append(T(px - 38, (py + ye) / 2 + 5, 'h = 52.3 m', 14, 'end', bold=True))
    o.append(L(px + 30, py, px + 30, yg, LV, 2) + L(px + 24, yg, px + 36, yg, LV, 1.5))
    o.append(T(px + 38, (py + yg) / 2 + 30, 'H = 134.3 m', 14, 'start', LV, bold=True))
    o.append(L(150, ye, 150, yg - 2, NX, 2) + L(144, ye, 156, ye, NX, 1.5) + L(144, yg - 2, 156, yg - 2, NX, 1.5))
    o.append(T(158, (ye + yg) / 2 + 5, 'N = −82.0 m', 14, 'start', NX, bold=True))
    o.append(T(20, yg + 56, 'H = h − N = 52.3 − (−82.0) = 134.3 m', 14, 'start', bold=True))
    # UTM zone panel
    zx, zw, zy, zh = 470, 230, 50, 220
    o.append(T(zx, 26, 'UTM zone 44N (78° E to 84° E)', 15, 'start', bold=True))
    o.append(R(zx, zy, zw, zh, PANEL, L2, 4, 1.5))
    cm_x = zx + zw / 2
    o.append(L(cm_x, zy, cm_x, zy + zh, AC, 2.5))
    o.append(Tb(cm_x, zy + 20, '81° E', 14, fill=AC, bold=True))
    o.append(T(zx + 4, zy + zh + 20, '78°', 13, 'start', MUT) + T(zx + zw - 4, zy + zh + 20, '84°', 13, 'end', MUT))
    qx = cm_x - zw / 6 * 0.73
    qy = zy + 120
    o.append(C(qx, qy, 6, LV))
    o.append(T(qx - 10, qy - 12, '80.27° E', 13, 'end', LV, bold=True))
    o.append(L(qx, qy + 18, cm_x - 3, qy + 18, LV, 2, arrow='l'))
    o.append(T(zx + 8, qy + 44, '0.73° west of the', 13, 'start') + T(zx + 8, qy + 62, 'central meridian', 13, 'start'))
    o.append(T(cm_x + 8, zy + zh - 30, 'easting', 13, 'start', AC) + T(cm_x + 8, zy + zh - 12, '500 000 m', 13, 'start', AC))
    o.append(T(zx, zy + zh + 44, 'so its easting is less than 500 000 m', 13, 'start'))
    return max(yg + 76, zy + zh + 60), ''.join(o)
FIG[4] = (f4, 'Left: here the geoid lies 82.0 m below the ellipsoid, so the pillar stands 134.3 m above the geoid although GNSS gives only 52.3 m above the ellipsoid. Right: the second point lies 0.73° west of the central meridian of zone 44, so its easting is below the 500 000 m given to that meridian.',
          'Left, a point above the ground line with the ellipsoid below it and the geoid 82 metres lower, showing h of 52.3 metres, N of minus 82 metres and H of 134.3 metres. Right, UTM zone 44 from 78 to 84 degrees east with the central meridian at 81 degrees and a point at 80.27 degrees east to its west.')


# ---- 1.5 the chain-survey frame, and the slope correction of the worked example ----
def f5():
    o = [T(20, 26, 'The frame of a chain survey', 15, 'start', bold=True)]
    A_, C_, B_, D_ = (60, 150), (500, 150), (280, 50), (220, 250)
    E_ = (170, 100)  # a point on AB
    o.append(L(*A_, *C_, AC, 3.5))
    o.append(L(*A_, *B_, INK, 2) + L(*B_, *C_, INK, 2) + L(*A_, *D_, INK, 2) + L(*D_, *C_, INK, 2))
    o.append(L(*B_, *D_, LV, 2.2, '7 5'))
    o.append(L(*D_, *E_, NX, 2.2, '2 4'))
    for (x, y), n, dx, dy in [(A_, 'A', -14, 5), (C_, 'C', 14, 5), (B_, 'B', 0, -12), (D_, 'D', 0, 24), (E_, 'E', -14, -4)]:
        o.append(C(x, y, 5, INK)); o.append(T(x + dx, y + dy, n, 14, bold=True))
    # a house near AC, fixed by two perpendicular offsets
    o.append(R(360, 114, 50, 20, PANEL, INK, 0, 1.5))
    o.append(L(360, 134, 360, 150, MUT, 1.5) + L(410, 134, 410, 150, MUT, 1.5))
    o.append(T(385, 129, 'house', 13))
    # key
    kx = 556
    for i, (c, d, t) in enumerate([(AC, None, 'base line AC'), (INK, None, 'triangle sides'), (LV, '7 5', 'check line BD'), (NX, '2 4', 'tie line DE')]):
        y = 70 + i * 30
        o.append(L(kx, y, kx + 34, y, c, 3 if c == AC else 2.2, d)); o.append(T(kx + 42, y + 5, t, 13, 'start'))
    # slope panel
    y0 = 300
    o.append(T(20, y0, 'The worked example: slope correction', 15, 'start', bold=True))
    x1, y1, x2, y2 = 60, y0 + 120, 360, y0 + 40
    o.append(L(x1, y1, x2, y2, AC, 2.5))
    o.append(L(x1, y1, x2, y1, INK, 2) + L(x2, y1, x2, y2, NX, 2))
    o.append(T((x1 + x2) / 2 - 10, (y1 + y2) / 2 - 10, 'slope 20.000 m', 14, 'end', AC, bold=True))
    o.append(T(x2 + 8, (y1 + y2) / 2 + 5, 'h = 1.200 m', 14, 'start', NX))
    o.append(T((x1 + x2) / 2, y1 + 22, 'horizontal √(20.000² − 1.200²) = 19.964 m', 14))
    o.append(boxt(470, y0 + 20, 230, 104, ['slope correction', '19.964 − 20.000 = −0.036 m', 'temperature, 35 °C (std 20 °C)', '30 × 11.2 × 10⁻⁶ × 15 = +5.04 mm'], ACS, AC, 13))
    return y0 + 160, ''.join(o)
FIG[5] = (f5, 'Top: the base line AC carries the survey; the check line BD tests the two triangles built on it, the tie line DE fixes detail far from the base, and short perpendicular offsets fix the house. Bottom: the 20.000 m slope length with a 1.200 m rise is 19.964 m in plan, a correction of −0.036 m.',
          'A chain survey frame with stations A, B, C, D and E, the base line AC, the check line BD, the tie line DE and two offsets to a house, with a key, and below it a right triangle with a 20 metre slope, a 1.2 metre rise and a 19.964 metre horizontal side.')


# ---- 1.6 phase EDM: coarse and fine readings ----
def f6():
    o = [T(20, 26, 'Phase EDM: the fine unit is λ/2 = 10 m', 15, 'start', bold=True)]
    ix, px, y = 60, 640, 110
    # instrument and prism
    o.append(R(ix - 30, y - 22, 52, 44, PANEL, INK, 6, 2)); o.append(T(ix - 4, y + 44, 'EDM', 14, bold=True))
    o.append(f'<polygon points="{px},{y - 22} {px + 34},{y} {px},{y + 22}" style="fill:{ACS};stroke:{AC};stroke-width:2"/>')
    o.append(T(px + 10, y + 44, 'prism', 14, bold=True))
    # outgoing and returning beams
    o.append(L(ix + 24, y - 8, px - 4, y - 8, AC, 2, arrow='n'))
    o.append(L(px - 4, y + 8, ix + 26, y + 8, LV, 2, arrow='l'))
    o.append(Tb((ix + px) / 2, y - 16, 'outgoing wave', 13, fill=AC))
    o.append(Tb((ix + px) / 2, y + 26, 'returning wave: compared in phase', 13, fill=LV))
    # ruler of fine units
    ry = 214
    o.append(T(20, ry - 14, 'The distance counted in fine units', 15, 'start', bold=True))
    x = ix
    w = 46
    for i in range(3):
        o.append(R(x, ry, w, 26, (ACS if i % 2 == 0 else PANEL), AC, 0, 1.5)); o.append(T(x + w / 2, ry + 18, '10 m', 13)); x += w
    o.append(T(x + 40, ry + 18, '…', 16, bold=True)); x += 80
    for i in range(2):
        o.append(R(x, ry, w, 26, (PANEL if i % 2 == 0 else ACS), AC, 0, 1.5)); o.append(T(x + w / 2, ry + 18, '10 m', 13)); x += w
    o.append(R(x, ry, 0.307 * w, 26, LVS, LV, 0, 2))
    o.append(T(x + 0.307 * w + 8, ry + 18, '0.307 × 10 = 3.07 m', 13, 'start', LV, bold=True))
    o.append(brace(ix, x, ry + 40, INK))
    o.append(T((ix + x) / 2, ry + 62, 'N = 42 whole units = 420 m', 14, bold=True))
    # the three readings
    ty = ry + 100
    o.append(T(20, ty, 'coarse unit 1000 m: 152.3° / 360° × 1000 = 423.1 m, so N = 42', 14, 'start'))
    o.append(T(20, ty + 22, 'fine unit 10 m: 110.52° / 360° = 0.307, so d = 10 × (42 + 0.307) = 423.070 m', 14, 'start'))
    o.append(T(20, ty + 44, 'prism constant −30 mm: 423.040 m;  × cos 3° = 422.460 m horizontal', 14, 'start', AC, bold=True))
    return ty + 60, ''.join(o)
FIG[6] = (f6, 'The fine frequency measures only the last part of a 10 m unit (3.07 m); the coarse frequency, with a 1000 m unit, gives 423.1 m and so fixes the whole number of 10 m units at 42. Together they give 423.070 m, which the prism constant and the vertical angle turn into 422.460 m horizontal.',
          'An EDM sending a wave to a prism and receiving it back, a ruler of 10 metre units with 42 whole units and a part unit of 3.07 metres, and the coarse and fine readings that give 423.070 metres.')

spec = make_spec(FIG)
