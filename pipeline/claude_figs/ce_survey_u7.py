"""Hand-drawn figures for ce-survey-u7 (Geographic Information Systems), drawn from each chapter's worked example."""
import math, os, sys; sys.path.insert(0, os.path.dirname(__file__)); from kit import *

FIG = {}
spec = make_spec(FIG)


def SUB(t):
    return f'<tspan dy="4" font-size="12">{t}</tspan><tspan dy="-4"> </tspan>'


# ---- 7.1 the metro-station query: buffer, streets and mains ----
def f1():
    o = []
    cx, cy, s = 300, 205, 0.6  # 0.6 px per metre
    r = 200 * s
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2;stroke-dasharray:7 5"/>')
    # streets: (name, orientation, offset m, main?)
    streets = [('Gandhi Road', 'h', 0, True), ('Temple Street', 'h', -150, True), ('Lake Road', 'h', 190, False), ('Mill Street', 'h', -240, False),
               ('Market Street', 'v', 80, False), ('School Lane', 'v', -320, True)]
    for name, ori, d, main in streets:
        inside = abs(d) < 200
        pick = inside and not main
        col = LV if pick else INK
        w = 4 if pick else 2.5
        if ori == 'h':
            y = cy + d * s
            o.append(L(70, y, 530, y, col, w))
            if main: o.append(L(70, y + 6, 530, y + 6, NX, 3, '9 5'))
            o.append(T(538, y + 5, name, 13, 'start', col, pick))
        else:
            x = cx + d * s
            o.append(L(x, 30, x, 380, col, w))
            if main: o.append(L(x + 6, 30, x + 6, 380, NX, 3, '9 5'))
            o.append(T(x + (10 if d > 0 else -8), 30, name, 13, 'start' if d > 0 else 'end', col, pick))
    o.append(f'<rect x="{cx - 8}" y="{cy - 8}" width="16" height="16" style="fill:var(--ink);stroke:var(--fig);stroke-width:2"/>')
    o.append(Tb(cx - 14, cy - 16, 'station', 13, 'end', INK, True))
    o.append(L(cx, cy + 4, cx + r * math.cos(math.radians(60)), cy + r * math.sin(math.radians(60)), AC, 1.5, arrow='n'))
    o.append(Tb(cx + 20, cy + 62, 'R = 200 m', 13, 'start', AC, True))
    # legend and result
    y = 410
    o.append(L(40, y, 80, y, NX, 3, '9 5')); o.append(T(88, y + 5, 'water main', 13, 'start'))
    o.append(L(200, y, 240, y, LV, 4)); o.append(T(248, y + 5, 'inside buffer, no main', 13, 'start'))
    o.append(T(360, y + 34, 'buffer π × 200² = 125 664 m² (12.57 ha); new pipe: Market Street 367 m + Lake Road 125 m = 492 m', 13, fill=INK, bold=True))
    return y + 50, ''.join(o)


FIG[1] = (f1, 'The worked example on the map: the 200 m buffer round the station catches four streets, two of which already carry a water main. Market Street and Lake Road, inside the buffer with no main, are the answer, with 492 m of street inside the circle.',
          'A square station at the centre of a dashed 200 metre circle. Horizontal streets: Gandhi Road through the centre and Temple Street above, both with dashed water mains; Lake Road below with no main; Mill Street above the circle. Vertical streets: Market Street right of centre with no main, School Lane far left with a main. Market Street and Lake Road are highlighted. A note gives the buffer area 125 664 square metres and 492 metres of new pipe.')


# ---- 7.2 the four wells: spatial half on a map, attribute half in a table ----
def f2():
    o = []
    x0, x1, y0, y1 = 60, 330, 40, 290
    fx = lambda e: x0 + (e - 405) / 20 * (x1 - x0)
    fy = lambda n: y1 - (n - 1322) / 14 * (y1 - y0)
    o.append(R(fx(405), fy(1336), fx(416) - fx(405), fy(1322) - fy(1336), ACS, ACS, 0, 0))
    o.append(axes(x0, x1, y0, y1, [405, 410, 415, 420, 425], [1324, 1328, 1332, 1336], fx, fy, 'easting (m)', 'northing (m)'))
    o.append(L(fx(416), y0, fx(416), y1, AC, 2.5))
    o.append(T(fx(410.5), fy(1335) + 4, 'ward 7', 14, fill=AC, bold=True))
    o.append(T(fx(420.5), fy(1335) + 4, 'ward 9', 14, fill=MUT, bold=True))
    wells = [(1, 412, 1330, 40), (2, 415, 1332, 55), (3, 418, 1328, 80), (4, 421, 1331, 65)]
    for k, e, n, d in wells:
        deep = d > 60
        o.append(C(fx(e), fy(n), 7, NX if deep else INK))
        o.append(T(fx(e) + 10, fy(n) - 9, f'W{k}', 13, 'start', INK, True))
    o.append(T(fx(416) + 4, y1 - 8, 'E = 416 m', 13, 'start', AC))
    # attribute table on the right
    tx, ty, cw = 380, 70, [52, 70, 74, 64, 70]
    head = ['Well', 'E (m)', 'Type', 'Depth', 'Ward']
    rows = [['W1', '412', 'open', '40', '7'], ['W2', '415', 'open', '55', '7'], ['W3', '418', 'bore', '80', '9'], ['W4', '421', 'bore', '65', '9']]
    x = tx
    for j, h in enumerate(head):
        o.append(T(x + cw[j] / 2, ty, h, 13, bold=True)); x += cw[j]
    o.append(L(tx, ty + 8, tx + sum(cw), ty + 8, INK, 1.5))
    for i, row in enumerate(rows):
        yy = ty + 32 + i * 30; x = tx
        if int(row[3]) > 60: o.append(R(tx + cw[0] + cw[1] + cw[2], yy - 19, cw[3], 26, NXS, NXS, 0, 0))
        for j, c in enumerate(row):
            o.append(T(x + cw[j] / 2, yy, c, 13, fill=INK)); x += cw[j]
    o.append(T(tx + sum(cw) / 2, ty + 160, 'key: Well; ward joins many-to-one', 13, fill=MUT))
    o.append(T(tx + sum(cw) / 2, ty + 186, 'depth > 60 m (attribute query): W3, W4', 13, fill=NX, bold=True))
    o.append(T(tx + sum(cw) / 2, ty + 210, 'inside ward 7 (spatial query): W1, W2', 13, fill=AC, bold=True))
    return 340, ''.join(o)


FIG[2] = (f2, 'The four wells of the worked example. On the map the ward boundary at E = 416 m puts W1 and W2 inside ward 7, a test on geometry; in the table the depth field picks W3 and W4, a test on attributes.',
          'Left: a map with easting 405 to 425 metres and northing 1324 to 1336 metres; ward 7 is shaded left of a boundary at easting 416, ward 9 is to the right. Four well points W1 to W4, with W3 and W4 marked as deep. Right: an attribute table of well, easting, type, depth and ward, with depths 80 and 65 highlighted, and the results of the two queries.')


# ---- 7.3 raster cells against a vector contour ----
def f3():
    o = []
    vals = [[22, 25, 31, 34], [24, 29, 35, 38], [27, 33, 41, 45]]
    s, x0, y0 = 72, 70, 50
    for r_, row in enumerate(vals):
        for c, v in enumerate(row):
            hi = v >= 35
            o.append(R(x0 + c * s, y0 + r_ * s, s, s, LVS if hi else PANEL, LV if hi else L2, 0, 1.5))
    # 35 m contour by linear interpolation between cell centres (vector line)
    cxy = lambda c, r_: (x0 + (c + 0.5) * s, y0 + (r_ + 0.5) * s)
    pts = [cxy(3, 0.25), cxy(2, 1.0), cxy(1.25, 2.0)]
    pts = [(pts[0][0] + 12, y0 - 2)] + pts + [(pts[-1][0] - 10, y0 + 3 * s + 2)]
    o.append(P(pts, AC, 3, '8 5'))
    # cell values on top of the contour, with a halo in the cell colour so the line never hides a digit
    for r_, row in enumerate(vals):
        for c, v in enumerate(row):
            hi = v >= 35
            t = T(x0 + c * s + s / 2, y0 + r_ * s + s / 2 + 6, str(v), 17, bold=hi)
            o.append(t.replace('style="fill:', f'style="paint-order:stroke;stroke:{LVS if hi else PANEL};stroke-width:6;stroke-linejoin:round;fill:'))
    o.append(T(x0 + 4 * s + 10, y0 - 8, '35 m contour (vector)', 13, 'end', AC, True))
    o.append(brace(x0, x0 + s, y0 + 3 * s + 12, INK))
    o.append(T(x0 + s / 2, y0 + 3 * s + 36, '20 m', 13, fill=INK, bold=True))
    # notes
    tx = 400
    o.append(T(tx, 80, 'one cell: 20 × 20 = 400 m²', 14, 'start', INK, True))
    o.append(T(tx, 108, 'grid: 3 × 4 = 12 cells = 4 800 m²', 14, 'start', INK))
    o.append(T(tx, 136, 'cells at or above 35 m: 4', 14, 'start', LV, True))
    o.append(T(tx, 164, 'high ground: 4 × 400 = 1 600 m²', 14, 'start', LV, True))
    o.append(T(tx, 206, 'raster: the edge follows whole cells', 13, 'start', MUT))
    o.append(T(tx, 228, 'vector: the contour follows coordinates', 13, 'start', MUT))
    return y0 + 3 * s + 50, ''.join(o)


FIG[3] = (f3, 'The elevation raster of the worked example with 20 m cells. The four shaded cells at or above 35 m give 1600 m² of high ground, with a stepped edge; the dashed 35 m contour, interpolated between cell centres, is the same boundary stored as a vector line.',
          'A three by four grid of elevations: 22, 25, 31, 34; 24, 29, 35, 38; 27, 33, 41, 45. The cells 35, 38, 41 and 45 are shaded. A dashed contour line crosses the grid diagonally from the top right to the bottom left. Notes give one cell 400 square metres, the grid 4800, and the high ground 1600 square metres.')


# ---- 7.4 control-point residuals of the georeferenced sheet ----
def f4():
    o = []
    x0, y0, w, h = 90, 40, 360, 270
    o.append(R(x0, y0, w, h, PANEL, INK, 4, 1.5))
    o.append(T(x0 + w / 2, y0 + h / 2 + 5, '1:50 000 toposheet', 14, fill=MUT))
    k = 12  # px per metre of residual
    pts = [('P1', x0 + 80, y0 + 70, 2.0, 1.0), ('P2', x0 + w - 80, y0 + 70, -1.0, 2.0), ('P3', x0 + w - 80, y0 + h - 70, 1.0, -2.0), ('P4', x0 + 80, y0 + h - 70, -2.0, -1.0)]
    for name, X, Y, e, n in pts:
        o.append(C(X, Y, 6, INK))
        o.append(L(X, Y, X + e * k, Y - n * k, NX, 2.5, arrow='x'))
        o.append(f'<circle cx="{X}" cy="{Y}" r="{5 * k}" style="fill:none;stroke:var(--line2);stroke-width:1.2;stroke-dasharray:4 4"/>')
        dy = -16 if n < 0 else 22
        lab = f'{name} ({e:+.1f}, {n:+.1f})'.replace('-', '−')
        o.append(T(X - 8, Y + dy, lab, 13, 'end', INK, True).replace('style="fill:', 'style="paint-order:stroke;stroke:var(--panel);stroke-width:5;stroke-linejoin:round;fill:'))
    tx = 480
    o.append(T(tx, 90, 'residual (e, n) in metres', 13, 'start', NX, True))
    o.append(T(tx, 116, 'arrows drawn 12 times larger', 13, 'start', MUT))
    o.append(T(tx, 142, 'dashed circle: 5 m tolerance', 13, 'start', MUT))
    o.append(T(tx, 184, 'Σe² = 10.0, Σn² = 10.0', 13, 'start', INK))
    o.append(T(tx, 208, 'RMS = √(20.0 ÷ 4) = 2.24 m', 14, 'start', AC, True))
    o.append(T(tx, 232, '2.24 m < 5 m: accepted', 14, 'start', LV, True))
    o.append(T(tx, 258, 'scale limit 0.25 mm × 50 000', 13, 'start', MUT))
    o.append(T(tx, 278, '= 12.5 m', 13, 'start', MUT))
    return y0 + h + 20, ''.join(o)


FIG[4] = (f4, 'The four control points of the worked example. Each arrow is a point\'s residual, drawn 12 times larger; every one is 2.24 m long, well inside the 5 m tolerance circle, so the RMS error is 2.24 m and the georeference is accepted.',
          'A rectangle for a toposheet with a control point near each corner. From each point a short arrow shows its residual: P1 plus 2 east and plus 1 north, P2 minus 1 and plus 2, P3 plus 1 and minus 2, P4 minus 2 and minus 1, each inside a dashed 5 metre circle. Notes give the sums of squares 10.0 and 10.0 and the RMS error 2.24 metres.')


# ---- 7.5 UTM zone 44 and the Chennai point ----
def f5():
    o = []
    x0, x1, y0, y1 = 120, 600, 40, 330
    fx = lambda lon: x0 + (lon - 78) / 6 * (x1 - x0)
    fy = lambda lat: y1 - (lat - 6) / 24 * (y1 - y0)
    o.append(R(x0, y0, x1 - x0, y1 - y0, ACS, AC, 0, 2))
    for lon in (78, 80, 82, 84):
        o.append(T(fx(lon), y1 + 20, f'{lon}° E', 13, fill=MUT))
    for lat in (10, 20, 30):
        o.append(L(x0 - 5, fy(lat), x0, fy(lat), L2, 1.5)); o.append(T(x0 - 9, fy(lat) + 4, f'{lat}° N', 13, 'end', MUT))
    o.append(L(fx(81), y0, fx(81), y1, NX, 2.5, '8 5'))
    o.append(Tb(fx(81), y0 + 20, 'central meridian 81° E', 13, 'middle', NX, True))
    o.append(Tb(fx(81), y0 + 44, 'k = 0.9996, E = 500 000 m', 13, 'middle', NX))
    # secant lines (k = 1) about 180 km either side, drawn at 13° N spacing
    dl = 180 / (111.32 * math.cos(math.radians(13)))
    for sgn in (-1, 1):
        o.append(L(fx(81 + sgn * dl), y0 + 60, fx(81 + sgn * dl), y1, L2, 1.5, '3 4'))
    o.append(T(fx(81 + dl) + 6, y1 - 12, 'k = 1 about 180 km out', 13, 'start', MUT))
    px, py = fx(80), fy(13)
    o.append(C(px, py, 7, LV))
    o.append(Tb(px - 12, py - 12, 'point 80° E, 13° N', 13, 'end', LV, True))
    o.append(L(px + 8, py + 22, fx(81) - 4, py + 22, LV, 2, arrow='l'))
    o.append(L(fx(81) - 4, py + 22, px + 8, py + 22, LV, 2, arrow='l'))
    o.append(Tb((px + fx(81)) / 2, py + 44, '1° ≈ 108 km', 13, 'middle', LV, True))
    o.append(T(x0 + 8, y0 + 20, 'zone 44: 78° E to 84° E', 13, 'start', AC, True))
    o.append(T(360, y1 + 46, 'zone = floor((80 + 180) ÷ 6) + 1 = 44; easting ≈ 500 000 − 108 400 ≈ 391 600 m', 13, fill=INK, bold=True))
    return y1 + 60, ''.join(o)


FIG[5] = (f5, 'UTM zone 44 runs from 78° E to 84° E with its central meridian at 81° E, where the scale factor is 0.9996 and the false easting 500 000 m. The point of the worked example, at 80° E, 13° N, lies about 108 km west of it.',
          'A tall strip from 78 to 84 degrees east and 6 to 30 degrees north. A dashed central meridian at 81 degrees east is labelled scale factor 0.9996 and easting 500 000 metres; two dotted lines about 180 kilometres either side mark scale factor 1. A point at 80 degrees east, 13 degrees north is joined to the central meridian by a double arrow labelled about 108 kilometres.')


# ---- 7.6 weighted overlay scores of the three villages ----
def f6():
    o = []
    x0, x1 = 150, 650
    fx = lambda v: x0 + v / 5 * (x1 - x0)
    o.append(xaxis(x0, x1, 300, [0, 1, 2, 3, 4, 5], fx, 'suitability S = 0.6 × population score + 0.4 × distance score'))
    rows = [('A', 5, 2), ('B', 4, 4), ('C', 2, 5)]
    for i, (v, p, d) in enumerate(rows):
        y = 60 + i * 76
        a, b = 0.6 * p, 0.4 * d
        o.append(T(x0 - 12, y + 24, f'Village {v}', 14, 'end', INK, True))
        o.append(T(x0 - 12, y + 44, f'scores {p} and {d}', 13, 'end', MUT))
        o.append(R(x0, y, fx(a) - x0, 40, ACS, AC, 3))
        o.append(R(fx(a), y, fx(a + b) - fx(a), 40, NXS, NX, 3))
        o.append(T((x0 + fx(a)) / 2, y + 26, f'{a:.1f}', 14, bold=True))
        o.append(T((fx(a) + fx(a + b)) / 2, y + 26, f'{b:.1f}', 14, bold=True))
        best = v == 'B'
        o.append(T(fx(a + b) + 10, y + 26, f'S = {a + b:.1f}' + (' best' if best else ''), 14, 'start', LV if best else INK, True))
    o.append(R(x0, 20, 18, 14, ACS, AC, 2)); o.append(T(x0 + 24, 32, 'population part (weight 0.6)', 13, 'start'))
    o.append(R(x0 + 260, 20, 18, 14, NXS, NX, 2)); o.append(T(x0 + 284, 32, 'distance part (weight 0.4)', 13, 'start'))
    return 360, ''.join(o)


FIG[6] = (f6, 'The weighted overlay of the worked example. Each bar is one village\'s suitability, split into its weighted population part and distance part; village B wins with S = 4.0 although A has the best population score.',
          'Three horizontal stacked bars on a 0 to 5 scale. Village A: 3.0 plus 0.8 equals 3.8. Village B: 2.4 plus 1.6 equals 4.0, marked best. Village C: 1.2 plus 2.0 equals 3.2.')
