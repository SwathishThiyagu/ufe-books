"""Claude's hand-drawn figures for ce-survey-u2 (Compass, plane table and traversing), one per chapter.
Every number comes from that chapter's worked example. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
rad = math.radians


def ray(cx, cy, deg, r, c=AC, w=2.5, dash=None, arrow='n'):
    a = rad(deg)
    return L(cx, cy, cx + r * math.sin(a), cy - r * math.cos(a), c, w, dash, arrow=arrow)


def pol(cx, cy, deg, r):
    a = rad(deg)
    return cx + r * math.sin(a), cy - r * math.cos(a)


def rose(cx, cy, r):
    o = [f'<circle cx="{cx}" cy="{cy}" r="{r}" style="fill:none;stroke:var(--line2);stroke-width:1.5"/>',
         L(cx, cy - r - 8, cx, cy + r + 8, MUT, 1.2), L(cx - r - 8, cy, cx + r + 8, cy, MUT, 1.2),
         T(cx, cy - r - 14, 'N', 14, bold=True), T(cx, cy + r + 26, 'S', 14, bold=True),
         T(cx + r + 20, cy + 5, 'E', 14, bold=True), T(cx - r - 20, cy + 5, 'W', 14, bold=True)]
    return ''.join(o)


def arcdeg(cx, cy, r, d1, d2, c, w=1.8):
    """arc clockwise from bearing d1 to d2 (degrees)"""
    x1, y1 = pol(cx, cy, d1, r); x2, y2 = pol(cx, cy, d2, r)
    large = 1 if (d2 - d1) % 360 > 180 else 0
    return f'<path d="M{x1:.1f},{y1:.1f} A{r},{r} 0 {large} 1 {x2:.1f},{y2:.1f}" style="fill:none;stroke:{c};stroke-width:{w}"/>'


# ---- 2.1 WCB 145° and 250°, their reduced and back bearings; magnetic to true ----
def f1():
    o = [T(20, 26, 'Whole circle bearings 145° and 250°', 15, 'start', bold=True)]
    cx, cy, r = 190, 180, 120
    o.append(rose(cx, cy, r))
    o.append(ray(cx, cy, 145, r, AC)); o.append(ray(cx, cy, 325, r * 0.8, AC, 1.8, '6 4'))
    o.append(ray(cx, cy, 250, r, LV)); o.append(ray(cx, cy, 70, r * 0.8, LV, 1.8, '6 4'))
    o.append(arcdeg(cx, cy, 40, 145, 180, AC)); o.append(arcdeg(cx, cy, 52, 180, 250, LV))
    x, y = pol(cx, cy, 145, r); o.append(T(x + 6, y + 18, '145°: S 35° E', 14, 'start', AC, bold=True))
    x, y = pol(cx, cy, 250, r); o.append(T(x - 4, y + 26, '250°: S 70° W', 14, 'start', LV, bold=True))
    x, y = pol(cx, cy, 325, r * 0.8); o.append(T(x - 6, y - 8, 'back 325°', 13, 'end', AC))
    x, y = pol(cx, cy, 70, r * 0.8); o.append(T(x + 6, y - 8, 'back 70°', 13, 'start', LV))
    o.append(T(cx + 18, cy + 52, '35°', 13, 'start', AC)); o.append(T(cx - 50, cy + 40, '70°', 13, 'end', LV))
    # declination panel
    px, py = 520, 200
    o.append(T(420, 26, 'Magnetic to true, 5°30′ east', 15, 'start', bold=True))
    o.append(L(px, py, px, py - 140, INK, 2.5, arrow='n')); o.append(T(px, py - 148, 'true N', 13, bold=True))
    o.append(ray(px, py, 5.5, 140, NX, 2.2)); x, y = pol(px, py, 5.5, 140); o.append(T(x + 6, y + 4, 'magnetic N', 13, 'start', NX))
    o.append(ray(px, py, 45.5, 150, AC, 2.5)); x, y = pol(px, py, 45.5, 150); o.append(T(x + 4, y + 16, 'the line', 13, 'start', AC))
    o.append(arcdeg(px, py, 60, 0, 5.5, NX)); o.append(arcdeg(px, py, 86, 5.5, 45.5, AC))
    o.append(T(px + 14, py - 64, '5°30′', 13, 'start', NX))
    o.append(T(px + 66, py - 52, '40°00′', 13, 'start', AC))
    o.append(T(420, py + 40, 'true = magnetic + east declination', 14, 'start'))
    o.append(T(420, py + 62, '= 40°00′ + 5°30′ = 45°30′', 14, 'start', bold=True))
    o.append(T(420, py + 84, 'opposite way: 225°30′', 14, 'start', MUT))
    return 340, ''.join(o)
FIG[1] = (f1, 'Left: 145° lies in the south-east quadrant, 35° from south, and 250° in the south-west, 70° from south; their back bearings (dashed) are 325° and 70°. Right: with 5°30′ east declination the magnetic bearing 40°00′ is a true bearing of 45°30′.',
          'A compass rose with lines at 145 and 250 degrees, their reduced bearings S 35 E and S 70 W, and their back bearings at 325 and 70 degrees; beside it true north, magnetic north 5 degrees 30 minutes east of it, and a line at magnetic 40 degrees, true 45 degrees 30 minutes.')


# ---- 2.2 the traverse ABCD with local attraction at D ----
def f2():
    o = [T(20, 26, 'Traverse ABCD: local attraction at D', 15, 'start', bold=True)]
    brg = {'AB': 46, 'BC': 130, 'CD': 220.5, 'DA': 310}
    lens = {'AB': 100, 'BC': 100, 'CD': 99.46, 'DA': 109.58}
    k = 1.5
    pts = {'A': (90, 160)}
    for ln, nxt in (('AB', 'B'), ('BC', 'C'), ('CD', 'D')):
        x, y = pts[ln[0]]; a = rad(brg[ln])
        pts[nxt] = (x + k * lens[ln] * math.sin(a), y - k * lens[ln] * math.cos(a))
    for ln in ('AB', 'BC', 'CD', 'DA'):
        o.append(L(*pts[ln[0]], *pts[ln[1]], AC, 2.5, arrow=None))
    for n, (x, y) in pts.items():
        o.append(C(x, y, 5, LV if n == 'D' else INK))
    lab = {'A': (-16, 6), 'B': (0, -12), 'C': (16, 6), 'D': (0, 26)}
    for n, (dx, dy) in lab.items():
        x, y = pts[n]; o.append(T(x + dx, y + dy, n, 15, bold=True, fill=(LV if n == 'D' else INK)))
    # bearing labels at mid-lines
    mid = lambda a, b: ((pts[a][0] + pts[b][0]) / 2, (pts[a][1] + pts[b][1]) / 2)
    x, y = mid('A', 'B'); o.append(T(x - 10, y - 8, 'AB 46°00′', 13, 'end'))
    x, y = mid('B', 'C'); o.append(T(x + 10, y - 8, 'BC 130°00′', 13, 'start'))
    x, y = mid('C', 'D'); o.append(T(x + 12, y + 14, 'CD 220°30′', 13, 'start'))
    x, y = mid('D', 'A'); o.append(T(x - 12, y + 16, 'DA 310°00′', 13, 'end'))
    # needle at D: magnetic north and the deflected needle
    dx, dy = pts['D']
    o.append(L(dx - 80, dy + 10, dx - 80, dy - 36, INK, 1.8, arrow='n'))
    o.append(ray(dx - 80, dy + 10, -6, 46, LV, 1.8, '4 3'))
    o.append(T(dx - 92, dy - 14, 'needle at D', 13, 'end', LV))
    o.append(T(dx - 92, dy + 2, 'reads 30′ low', 13, 'end', LV))
    # table
    tx, ty = 420, 46
    rows = [('Line', 'FB', 'BB', 'diff'), ('AB', '46°00′', '226°00′', '180°00′'), ('BC', '130°00′', '310°00′', '180°00′'),
            ('CD', '220°30′', '40°00′', '180°30′'), ('DA', '309°30′', '130°00′', '179°30′')]
    o.append(R(tx, ty, 290, 150, PANEL, L2, 8, 1.5))
    for i, row in enumerate(rows):
        y = ty + 24 + i * 28
        for j, cell in enumerate(row):
            hot = i >= 3 and j >= 1 and (row[0] == 'CD' and j in (2, 3) or row[0] == 'DA' and j in (1, 3))
            o.append(T(tx + 30 + j * 72, y, cell, 13 if i else 14, fill=(LV if hot else INK), bold=(i == 0 or hot)))
    o.append(T(tx, ty + 178, 'AB and BC pass: A, B, C are free.', 13, 'start'))
    o.append(T(tx, ty + 198, 'Correct DC = 220°30′ − 180° = 40°30′;', 13, 'start'))
    o.append(T(tx, ty + 218, 'observed 40°00′, so +30′ at D:', 13, 'start'))
    o.append(T(tx, ty + 238, 'DC 40°30′, DA 310°00′.', 13, 'start', AC, bold=True))
    return 320, ''.join(o)
FIG[2] = (f2, 'The traverse of the worked example, drawn with its corrected bearings. Lines AB and BC have fore and back bearings exactly 180° apart, so A, B and C are free; both bearings read at D are 30′ low, and adding 30′ makes DA and AD agree.',
          'A four-sided traverse A, B, C, D with its corrected bearings, a sketch of the deflected needle at D, and a table of fore and back bearings showing differences of 180 degrees except on lines CD and DA.')


# ---- 2.3 orientation by trough compass, and the three-point problem ----
def f3():
    o = [T(20, 26, 'Orienting the table: turn it 15° clockwise', 15, 'start', bold=True)]
    def board(cx, cy, rot, title, note, c):
        out = [T(cx, 62, title, 14, bold=True, fill=c)]
        w, h = 200, 150
        corners = [(-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h / 2)]
        a = rad(rot)
        pts = [(cx + x * math.cos(a) - y * math.sin(a), cy + x * math.sin(a) + y * math.cos(a)) for x, y in corners]
        out.append(f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" style="fill:var(--panel);stroke:var(--line2);stroke-width:2"/>')
        # the line pq drawn at 210° relative to the sheet's north
        px, py = cx + 30 * math.cos(a) - (-40) * math.sin(a), cy + 30 * math.sin(a) + (-40) * math.cos(a)
        qx, qy = pol(px, py, 210 + rot, 110)
        out.append(L(px, py, qx, qy, AC, 3)); out.append(C(px, py, 4, INK)); out.append(T(px + 8, py - 6, 'p', 14, 'start', bold=True)); out.append(T(qx - 10, qy + 4, 'q', 14, 'end', bold=True))
        # sheet north line
        nx, ny = pol(cx - 70 * math.cos(a), cy - 70 * math.sin(a), rot, 60)
        sx, sy = cx - 70 * math.cos(a), cy - 70 * math.sin(a)
        out.append(L(sx, sy + 0, nx, ny, MUT, 1.6, '4 3', arrow='m'))
        out.append(T(nx, ny - 8, 'sheet N', 13, fill=MUT))
        out.append(T(cx, 280, note, 13, fill=c))
        return ''.join(out)
    o.append(board(130, 170, -15, 'Before', 'needle along pq reads 195°', LV))
    o.append(board(370, 170, 0, 'After', 'needle along pq reads 210°', AC))
    o.append(L(500, 110, 500, 60, NX, 2.5, arrow='x')); o.append(T(500, 124, 'magnetic N', 13, fill=NX))
    o.append(arc(230, 96, 270, 96, 0.5, NX, 2, 'x'))
    o.append(T(250, 70, '+15°', 14, bold=True, fill=NX))
    # resection inset
    rx, ry = 560, 150
    o.append(T(540, 26, 'Three-point problem', 15, 'start', bold=True))
    A_, B_, C_ = (rx - 20, 70), (rx + 140, 90), (rx + 70, 250)
    for (x, y), n in ((A_, 'a'), (B_, 'b'), (C_, 'c')):
        o.append(C(x, y, 4, INK)); o.append(T(x + (10 if n != 'a' else -10), y - 6, n, 14, 'start' if n != 'a' else 'end', bold=True))
    tri = [(rx + 50, 160), (rx + 66, 150), (rx + 62, 172)]
    o.append(f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in tri)}" style="fill:{LVS};stroke:{LV};stroke-width:1.5"/>')
    for (x, y), t in zip((A_, B_, C_), tri):
        o.append(L(x, y, t[0], t[1], AC, 1.5, '5 3'))
    o.append(T(rx + 70, 210, 'triangle', 13, 'start', LV)); o.append(T(rx + 70, 226, 'of error', 13, 'start', LV))
    return 300, ''.join(o)
FIG[3] = (f3, 'Left: pq is plotted at 210°, but with the board as set up the needle along it reads 195°, so the sheet north lies 15° anticlockwise of magnetic north; turning the board 15° clockwise brings the reading to 210°. Right: in resection, rays back from a, b and c form a triangle of error until the orientation is right.',
          'Two plane table boards: before, rotated 15 degrees anticlockwise with the line pq reading 195 degrees; after, turned 15 degrees clockwise with pq reading 210 degrees. Beside them three plotted points a, b and c with rays forming a small triangle of error.')


# ---- 2.4 the traverse with the latitude and departure of each line ----
def f4():
    o = [T(20, 26, 'Latitude and departure of each line (A at the origin)', 15, 'start', bold=True)]
    E = [0, 141.42, 268.70, 188.70]; N = [0, 141.42, 14.14, -124.42]
    k = 0.85; ox, oy = 80, 182
    X = lambda e: ox + e * k; Y = lambda n: oy - n * k
    # components of AB and CD
    o.append(L(X(0), Y(0), X(141.42), Y(0), NX, 2, '5 4')); o.append(L(X(141.42), Y(0), X(141.42), Y(141.42), LV, 2, '5 4'))
    o.append(T(X(70), Y(0) + 18, 'dep +141.42', 13, fill=NX)); o.append(T(X(141.42) - 6, Y(80), 'lat +141.42', 13, 'end', LV))
    o.append(L(X(268.70), Y(14.14), X(268.70), Y(-124.42), LV, 2, '5 4')); o.append(L(X(268.70), Y(-124.42), X(188.70), Y(-124.42), NX, 2, '5 4'))
    o.append(T(X(268.70) + 8, Y(-60), 'lat −138.56', 13, 'start', LV)); o.append(T(X(228), Y(-124.42) + 18, 'dep −80.00', 13, fill=NX))
    names = 'ABCD'
    for i in range(4):
        j = (i + 1) % 4
        o.append(L(X(E[i]), Y(N[i]), X(E[j]), Y(N[j]), AC, 2.8, arrow=None))
    for i, n in enumerate(names):
        o.append(C(X(E[i]), Y(N[i]), 5, INK))
    o.append(T(X(0) - 14, Y(0) + 5, 'A', 15, 'end', bold=True)); o.append(T(X(141.42), Y(141.42) - 12, 'B', 15, bold=True))
    o.append(T(X(268.70) + 14, Y(14.14) + 5, 'C', 15, 'start', bold=True)); o.append(T(X(188.70), Y(-124.42) + 26, 'D', 15, bold=True))
    o.append(T(X(30), Y(60), '200 m, 45°', 13, 'end', AC)); o.append(T(X(214), Y(86), '180 m, 135°', 13, 'start', AC))
    o.append(T(X(100), Y(-58), '226 m, 303°20′', 13, 'end', AC))
    # table of the sums
    tx, ty = 420, 60
    rows = [('Line', 'Lat (m)', 'Dep (m)'), ('AB', '+141.42', '+141.42'), ('BC', '−127.28', '+127.28'), ('CD', '−138.56', '−80.00'), ('DA', '+124.19', '−188.82'), ('Sum', '−0.23', '−0.12')]
    o.append(R(tx, ty, 280, 196, PANEL, L2, 8, 1.5))
    for i, row in enumerate(rows):
        y = ty + 26 + i * 30
        for j, cell in enumerate(row):
            o.append(T(tx + 44 + j * 96, y, cell, 14 if i in (0, 5) else 13, bold=(i in (0, 5)), fill=(AC if i == 5 and j else INK)))
    o.append(L(tx + 10, ty + 158, tx + 270, ty + 158, L2, 1.2))
    o.append(T(tx, ty + 226, 'The sums are not zero: the traverse', 13, 'start'))
    o.append(T(tx, ty + 244, 'ends 0.23 m south and 0.12 m west of A.', 13, 'start'))
    return 330, ''.join(o)
FIG[4] = (f4, 'The worked traverse drawn to scale from A. Each line splits into a north–south latitude and an east–west departure (shown dashed for AB and CD); the four latitudes and four departures should each add to zero, but they add to −0.23 m and −0.12 m.',
          'The four-sided traverse A, B, C, D drawn to scale with dashed latitude and departure components for lines AB and CD, and a table of all latitudes and departures with sums of minus 0.23 and minus 0.12 metres.')


# ---- 2.5 closing error and the Bowditch shift of each station ----
def f5():
    o = [T(20, 26, 'Bowditch: each station moves in proportion to the distance to it', 15, 'start', bold=True)]
    E = [0, 141.42, 268.70, 188.70]; N = [0, 141.42, 14.14, -124.42]
    k = 0.95; ox, oy = 70, 190
    X = lambda e: ox + e * k; Y = lambda n: oy - n * k
    for i in range(4):
        j = (i + 1) % 4
        o.append(L(X(E[i]), Y(N[i]), X(E[j]), Y(N[j]), L2, 2.2))
    cum = [0, 200, 380, 540, 766]
    s = 260  # exaggeration of the shift: 0.26 m drawn as about 68 px
    ux, uy = 0.12 / 0.2594, 0.23 / 0.2594  # direction of the correction (north-east)
    for i, n in enumerate('ABCD'):
        x, y = X(E[i]), Y(N[i])
        o.append(C(x, y, 5, INK))
        f = cum[i] / 766
        if f:
            o.append(L(x, y, x + s * 0.2594 * f * ux, y - s * 0.2594 * f * uy, AC, 2.5, arrow='n'))
    o.append(T(X(0) - 14, Y(0) + 5, 'A', 15, 'end', bold=True)); o.append(T(X(141.42) - 14, Y(141.42) + 4, 'B', 15, 'end', bold=True))
    o.append(T(X(268.70) + 12, Y(14.14) + 18, 'C', 15, 'start', bold=True)); o.append(T(X(188.70), Y(-124.42) + 26, 'D', 15, bold=True))
    # closing error at A (end of the traverse lands at A', south-west)
    ax, ay = X(0) - s * 0.2594 * ux, Y(0) + s * 0.2594 * uy
    o.append(L(X(0), Y(0), ax, ay, LV, 2.2, '5 3')); o.append(C(ax, ay, 5, LV)); o.append(T(ax - 8, ay + 18, 'A′', 15, 'end', LV, bold=True))
    o.append(T(ax + 12, ay + 30, 'e = 0.259 m at 207°33′', 13, 'start', LV, bold=True))
    o.append(T(20, 372, 'Shifts drawn 260 times larger than true. B moves 200/766 of e, C 380/766, D 540/766.', 13, 'start', MUT))
    # numbers, left aligned in a panel
    tx, ty = 420, 56
    o.append(R(tx, ty, 290, 238, PANEL, L2, 8, 1.5))
    o.append(T(tx + 16, ty + 28, 'Misclosure', 14, 'start', bold=True))
    for i, s_ in enumerate(['ΣL = −0.23 m, ΣD = −0.12 m', 'e = √(0.23² + 0.12²) = 0.259 m', 'P = 766 m, precision 1 in 2950']):
        o.append(T(tx + 16, ty + 52 + i * 22, s_, 13, 'start'))
    o.append(T(tx + 16, ty + 132, 'Adjusted coordinates (m)', 14, 'start', bold=True))
    for i, s_ in enumerate(['B (1141.45, 1141.48)', 'C (1268.76, 1014.25)', 'D (1188.78, 875.74)']):
        o.append(T(tx + 16, ty + 156 + i * 22, s_, 13, 'start'))
    o.append(T(tx + 16, ty + 226, 'correction = +0.23 l/P, +0.12 l/P', 13, 'start', AC, bold=True))
    return 388, ''.join(o)
FIG[5] = (f5, 'The traverse ends at A′, 0.259 m south-west of A. Bowditch moves each station north-east by the closing error times its distance along the traverse over the perimeter, so A′ returns to A (shifts drawn 260 times true size).',
          'The traverse A, B, C, D with arrows at B, C and D pointing north-east and growing with distance along the traverse, the misclosed end A prime south-west of A, and a box with the closing error, precision and adjusted coordinates.')


# ---- 2.6 the plot ABCD on a grid and the cross-product table ----
def f6():
    o = [T(20, 26, 'Area of ABCD by coordinates', 15, 'start', bold=True)]
    k = 5.4; ox, oy = 50, 300
    X = lambda e: ox + e * k; Y = lambda n: oy - n * k
    for v in range(0, 50, 10):
        o.append(L(X(v), Y(0), X(v), Y(45), 'var(--line)', 1)); o.append(T(X(v), Y(0) + 18, str(v), 13, fill=MUT))
        o.append(L(X(0), Y(v), X(45), Y(v), 'var(--line)', 1)); o.append(T(X(0) - 8, Y(v) + 4, str(v), 13, 'end', MUT))
    o.append(T(X(45), Y(0) + 34, 'E (m)', 13, 'end', MUT)); o.append(T(X(0) + 6, Y(45) - 4, 'N (m)', 13, 'start', MUT))
    pts = [('A', 10, 10), ('B', 30, 10), ('C', 40, 30), ('D', 20, 40)]
    poly = ' '.join(f'{X(e):.1f},{Y(n):.1f}' for _, e, n in pts)
    o.append(f'<polygon points="{poly}" style="fill:{ACS};stroke:{AC};stroke-width:2.5"/>')
    off = {'A': (-8, 18, 'end'), 'B': (8, 18, 'start'), 'C': (10, 4, 'start'), 'D': (0, -12, 'middle')}
    for n, e, nn in pts:
        o.append(C(X(e), Y(nn), 5, INK)); dx, dy, an = off[n]; o.append(T(X(e) + dx, Y(nn) + dy, f'{n} ({e}, {nn})', 13, an, bold=True))
    o.append(T(X(25), Y(22), '550 m²', 15, bold=True))
    # table
    tx, ty = 362, 44
    head = ('', 'E', 'N next', 'N prev', 'E × (next − prev)')
    rows = [('A', '10', '10', '40', '−300'), ('B', '30', '30', '10', '600'), ('C', '40', '40', '10', '1200'), ('D', '20', '10', '30', '−400')]
    xs = [tx + 16, tx + 52, tx + 106, tx + 164, tx + 268]
    o.append(R(tx, ty, 346, 196, PANEL, L2, 8, 1.5))
    for j, h in enumerate(head): o.append(T(xs[j], ty + 26, h, 13, bold=True))
    for i, row in enumerate(rows):
        for j, cell in enumerate(row): o.append(T(xs[j], ty + 56 + i * 28, cell, 13, bold=(j == 0)))
    o.append(L(tx + 10, ty + 158, tx + 336, ty + 158, L2, 1.2))
    o.append(T(xs[0], ty + 182, 'sum', 13, bold=True)); o.append(T(xs[4], ty + 182, '1100 = 2A', 14, bold=True, fill=AC))
    o.append(T(tx, ty + 226, 'A = 1100 / 2 = 550 m² = 0.055 ha', 14, 'start', bold=True))
    o.append(T(tx, ty + 248, 'The order A, B, C, D runs anticlockwise,', 13, 'start', MUT))
    o.append(T(tx, ty + 266, 'so the sum is positive.', 13, 'start', MUT))
    return 345, ''.join(o)
FIG[6] = (f6, 'The four corners plotted on a 10 m grid. Each row of the table multiplies an easting by the change in northing across that corner; the products add to 1100, twice the area, so the plot is 550 m².',
          'The plot ABCD drawn on a grid with corner coordinates A 10 10, B 30 10, C 40 30, D 20 40, and a table of the products E times next N minus previous N adding to 1100, so the area is 550 square metres.')

spec = make_spec(FIG)
