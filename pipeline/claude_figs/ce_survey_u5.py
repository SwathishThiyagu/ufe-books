"""Claude's hand-drawn figures for ce-survey-u5 (Modern surveying: total station and GNSS), one per chapter.
Every number comes from that chapter's worked examples. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
rad = math.radians


def pol(cx, cy, deg, r):
    a = rad(deg)
    return cx + r * math.sin(a), cy - r * math.cos(a)


def north(x, y, n=34):
    return L(x, y + n, x, y, INK, 2, arrow='x') + T(x, y - 8, 'N', 14, bold=True)


def arcdeg(cx, cy, r, d1, d2, c, w=1.8, arrow=None):
    x1, y1 = pol(cx, cy, d1, r); x2, y2 = pol(cx, cy, d2, r)
    big = 1 if (d2 - d1) % 360 > 180 else 0
    m = f' marker-end="url(#ar-UID-{arrow})"' if arrow else ''
    return f'<path d="M{x1:.1f},{y1:.1f} A{r},{r} 0 {big} 1 {x2:.1f},{y2:.1f}" style="fill:none;stroke:{c};stroke-width:{w}"{m}/>'


# ---- 5.1 total station: plan of the shot and its side view ----
def f1():
    o = [T(20, 26, 'Plan: orient on Q, turn β, measure', 15, 'start', bold=True)]
    Px, Py = 110, 200
    o.append(north(Px, 60))
    o.append(L(Px, Py, *pol(Px, Py, 30, 150), L2, 2, '6 4'))
    qx, qy = pol(Px, Py, 30, 150); o.append(C(qx, qy, 5, INK)); o.append(T(qx + 10, qy + 4, 'Q (backsight)', 13, 'start'))
    lx, ly = pol(Px, Py, 15, 74); o.append(T(lx + 4, ly, '30°00′00″', 12, 'start', MUT))
    rx, ry = pol(Px, Py, 105.5, 200)
    o.append(L(Px, Py, rx, ry, AC, 2.5, arrow='n')); o.append(C(rx, ry, 5, AC)); o.append(T(rx - 4, ry + 24, 'R', 15, 'end', AC, bold=True))
    o.append(T((Px + rx) / 2 - 16, (Py + ry) / 2 + 36, 'd = 119.543 m', 13, 'middle', AC, True))
    o.append(arcdeg(Px, Py, 52, 0, 30, MUT, 1.5)); o.append(arcdeg(Px, Py, 70, 30, 105.5, AC, 2, 'n'))
    o.append(T(Px + 82, Py - 30, 'β = 75°30′', 13, 'start', AC, bold=True))
    o.append(C(Px, Py, 6, INK)); o.append(T(Px - 12, Py - 4, 'P', 15, 'end', bold=True)); o.append(T(20, 248, 'P = (1000.000, 2000.000)', 13, 'start'))
    o.append(T(20, 270, 'A = 30°00′ + 75°30′ = 105°30′', 13, 'start'))
    o.append(T(20, 292, 'R = (1115.196, 1968.053)', 13, 'start', AC, bold=True))
    # side view
    x0 = 380
    o.append(T(x0, 26, 'Side view: reduce S, then the level', 15, 'start', bold=True))
    gy = 250
    o.append(L(x0, gy, 710, gy, L2, 1.5))
    sx, sy = x0 + 30, gy - 40  # instrument centre (HI above P)
    o.append(L(x0 + 30, gy, sx, sy, INK, 3)); o.append(C(x0 + 30, gy, 5, INK)); o.append(T(x0 + 22, gy + 20, 'P, RL 25.000', 13, 'start'))
    o.append(Tb(x0 + 38, gy - 16, 'HI 1.550', 12, 'start', MUT))
    k = 2.05  # px per metre horizontally
    ex_, ey = sx + 119.543 * k, sy - 10.459 * 7  # vertical exaggerated 7 times
    o.append(L(sx, sy, ex_, ey, AC, 2.5, arrow='n'))
    o.append(Tb((sx + ex_) / 2 - 10, (sy + ey) / 2 - 12, 'S = 120.000 m', 13, 'middle', AC, True))
    o.append(L(sx, sy, ex_, sy, L2, 1.5, '5 4')); o.append(T((sx + ex_) / 2, sy + 18, 'd = S sin z = 119.543', 13, fill=MUT))
    o.append(L(ex_, sy, ex_, ey, LV, 2)); o.append(T(ex_ - 8, (sy + ey) / 2 + 4, 'ΔV = S cos z', 13, 'end', LV)); o.append(T(ex_ - 8, (sy + ey) / 2 + 22, '= 10.459', 13, 'end', LV))
    o.append(L(sx, sy, sx, sy - 70, MUT, 1.2, '3 3')); o.append(arcdeg(sx, sy, 40, 0, 85, MUT, 1.5)); o.append(T(sx + 14, sy - 46, 'z = 85°', 13, 'start', MUT))
    o.append(L(ex_, ey, ex_, ey + 1.8 * 7, INK, 3)); o.append(C(ex_, ey + 1.8 * 7, 4, INK))
    o.append(T(x0, 292, 'RL R = 25.000 + 1.550 + 10.459 − 1.800 = 35.209 m', 13, 'start', AC, bold=True))
    o.append(T(x0, 312, 'heights drawn 7 times larger than lengths', 12, 'start', MUT))
    return 325, ''.join(o)
FIG[1] = (f1, 'Left: oriented on Q at 30°00′00″, the instrument turns β = 75°30′ to R, so the azimuth PR is 105°30′ and R is fixed from d and A. Right: the slope distance S = 120.000 m at zenith angle 85° splits into d = 119.543 m and ΔV = 10.459 m, and HI and HT carry the level from P to R.',
          'Plan with station P, backsight Q at azimuth 30 degrees and the target R at azimuth 105 degrees 30 minutes, 119.543 metres away; side view with the slope distance, horizontal distance, vertical component, instrument and target heights and the reduced level of R, 35.209 metres.')


# ---- 5.2 GNSS: four ranges, all lengthened by the same clock error ----
def f2():
    o = [T(20, 26, 'Four satellites, four unknowns: x, y, z and the clock bias δt', 15, 'start', bold=True)]
    o.append(f'<path d="M20,300 Q200,250 380,300" style="fill:{PANEL};stroke:{L2};stroke-width:1.5"/>')
    rx, ry = 200, 276
    sats = [(60, 80), (160, 56), (270, 64), (360, 110)]
    for i, (sx, sy) in enumerate(sats):
        o.append(L(sx, sy, rx, ry, AC, 2))
        # extra length beyond the receiver, along the same line: the clock part
        dx, dy = rx - sx, ry - sy; n = math.hypot(dx, dy)
        o.append(L(rx - dx / n * 26, ry - dy / n * 26, rx, ry, LV, 4))
        o.append(R(sx - 14, sy - 9, 28, 18, NXS, NX, 4, 1.5)); o.append(T(sx, sy - 16, f'S{i + 1}', 13, bold=True))
    o.append(C(rx, ry, 6, INK)); o.append(T(rx, ry + 22, 'receiver', 13, bold=True))
    o.append(T(30, 330, 'thick end of each line: the same c δt on every range', 13, 'start', LV))
    tx = 410
    o.append(boxt(tx, 50, 300, 120, ['ρ = r + c δt', 'clock 10 µs ahead:', 'c δt = 299 792 458 × 10⁻⁵', '= 2997.925 m on every range'], PANEL, L2, 14, True))
    head = [('Method', 0), ('Data', 66), ('Accuracy', 196)]
    rows = [('SPP', 'code, one receiver', 'a few m'), ('DGPS', 'code + base', 'about 1 m'), ('RTK', 'carrier phase', '1 to 3 cm')]
    o.append(R(tx, 188, 300, 132, PANEL, L2, 8, 1.5))
    for h, dx in head: o.append(T(tx + 14 + dx, 212, h, 13, 'start', bold=True))
    for i, rw in enumerate(rows):
        for (h, dx), cell in zip(head, rw): o.append(T(tx + 14 + dx, 240 + i * 26, cell, 13, 'start', AC if dx == 196 else INK, bold=(dx == 0)))
    return 345, ''.join(o)
FIG[2] = (f2, 'Each pseudorange is the true range plus the same clock term c δt; a receiver clock 10 µs ahead adds 2997.925 m to every range, so the clock bias is solved as a fourth unknown with x, y and z. The table compares absolute (SPP) and relative (DGPS, RTK) positioning.',
          'Four satellites with lines to one receiver, each line ending in a thicker segment for the common clock error; a box with rho equals r plus c delta t and 2997.925 metres for 10 microseconds; a table of SPP, DGPS and RTK accuracy.')


# ---- 5.3 DOP: spread and bunched skyplots, and the error circles ----
def sky(cx, cy, r, pts, title, col):
    o = [T(cx, cy - r - 14, title, 14, bold=True, fill=col)]
    for e in (0, 30, 60):
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r * (90 - e) / 90:.1f}" style="fill:none;stroke:var(--line2);stroke-width:1.2"/>')
    o.append(L(cx, cy - r, cx, cy + r, LN, 1)); o.append(L(cx - r, cy, cx + r, cy, LN, 1))
    o.append(T(cx, cy - r + 13, 'N', 12, fill=MUT))
    for az, el in pts:
        x, y = pol(cx, cy, az, r * (90 - el) / 90)
        o.append(C(x, y, 6, col))
    return ''.join(o)


def f3():
    o = []
    o.append(sky(100, 120, 80, [(20, 25), (110, 40), (200, 30), (300, 35), (0, 85)], 'Spread: low DOP', AC))
    o.append(sky(290, 120, 80, [(340, 20), (355, 30), (10, 25), (20, 15), (5, 40)], 'Bunched: high DOP', LV))
    o.append(T(20, 236, 'Rings at 0°, 30° and 60° elevation; centre = zenith.', 13, 'start', MUT))
    o.append(T(20, 262, 'HDOP for two unit vectors (0, 1) and (1, 0): √2 = 1.414', 13, 'start'))
    o.append(T(20, 284, 'Both along (0, 1): HᵀH singular, HDOP infinite', 13, 'start', LV))
    # error circles, 1 m = 9 px
    cx, cy, k = 560, 150, 13
    o.append(T(560, 26, 'σ = 3.0 m, HDOP = 1.2', 14, bold=True))
    import random
    rnd = random.Random(7)
    for _ in range(60):
        x, y = rnd.gauss(0, 2.55), rnd.gauss(0, 2.55)
        if math.hypot(x, y) < 9.5: o.append(f'<circle cx="{cx + x * k:.1f}" cy="{cy + y * k:.1f}" r="2.2" style="fill:var(--muted)"/>')
    for rr, lab, col, dash in [(3.0, 'CEP 3.0 m (50 %)', NX, None), (3.6, 'DRMS 3.6 m', AC, '5 3'), (7.2, '2DRMS 7.2 m (95 %+)', LV, None)]:
        d = f';stroke-dasharray:{dash}' if dash else ''
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{rr * k:.1f}" style="fill:none;stroke:{col};stroke-width:2.2{d}"/>')
    o.append(C(cx, cy, 4, INK))
    o.append(T(cx - 60, 268, 'CEP 3.0 m: half the fixes', 13, 'start', NX, True))
    o.append(T(cx - 60, 288, 'DRMS 3.6 m = 1.2 × 3.0', 13, 'start', AC, True))
    o.append(T(cx - 60, 308, '2DRMS 7.2 m: 95 % or more', 13, 'start', LV, True))
    o.append(T(cx - 60, 328, 'vertical: ±1.96 × 6.0 = ±11.8 m', 13, 'start', MUT))
    return 340, ''.join(o)
FIG[3] = (f3, 'Left: satellites spread round the sky and in elevation give a low DOP; the same number bunched in the north give a high one. Right: with σ = 3.0 m and HDOP = 1.2, half the fixes fall inside CEP = 3.0 m, DRMS is 3.6 m and 95 % or more fall inside 2DRMS = 7.2 m.',
          'Two skyplots, one with five satellites spread in azimuth and elevation and one with five bunched low in the north; a scatter of fixes with circles for CEP 3.0 metres, DRMS 3.6 metres and 2DRMS 7.2 metres.')


# ---- 5.4 LiDAR: airborne swath, returns through a tree, and the range ----
def f4():
    o = [T(20, 26, 'Airborne LiDAR: H = 1000 m, scan ±20°', 15, 'start', bold=True)]
    ax, ay = 210, 62
    o.append(f'<path d="M{ax - 26},{ay} L{ax + 26},{ay} L{ax + 14},{ay - 8} L{ax - 14},{ay - 8} Z" style="fill:{INK}"/>')
    gy = 270; half = 150
    o.append(f'<polygon points="{ax},{ay} {ax - half},{gy} {ax + half},{gy}" style="fill:{ACS};stroke:none"/>')
    o.append(L(ax, ay, ax - half, gy, AC, 1.8, '6 4')); o.append(L(ax, ay, ax + half, gy, AC, 1.8, '6 4'))
    o.append(L(20, gy, 400, gy, INK, 2.5))
    o.append(L(ax, ay, ax, gy, L2, 1.5, '3 3')); o.append(Tb(ax - 8, 200, 'H = 1000 m', 13, 'end', MUT))
    o.append(arcdeg(ax, ay, 46, 160, 180, AC, 1.6)); o.append(T(ax - 22, ay + 64, '20°', 12, 'end', AC))
    o.append(L(ax - half, gy + 22, ax + half, gy + 22, INK, 1.5)); o.append(L(ax - half, gy + 16, ax - half, gy + 28, INK, 1.5)); o.append(L(ax + half, gy + 16, ax + half, gy + 28, INK, 1.5))
    o.append(Tb(ax, gy + 27, 'swath = 2 × 1000 × tan 20° = 728 m', 13, 'middle', INK, True))
    # a tree with two returns from one pulse
    tx = ax + 60
    o.append(L(tx, gy, tx, gy - 40, MUT, 4)); o.append(f'<ellipse cx="{tx}" cy="{gy - 62}" rx="30" ry="28" style="fill:{LVS};stroke:{LV};stroke-width:1.5"/>')
    o.append(L(ax, ay, tx - 6, gy, NX, 1.8))
    fx, fy = ax + (tx - 6 - ax) * (gy - 70 - ay) / (gy - ay), gy - 70
    o.append(C(fx, fy, 5, LV)); o.append(C(tx - 6, gy, 5, NX))
    o.append(Tb(fx - 12, fy - 30, 'first return: canopy (DSM)', 13, 'end', LV, True))
    o.append(T(tx + 14, gy - 8, 'last return: ground (DTM)', 13, 'start', NX, True))
    o.append(T(20, 330, 'density = 200 000 ÷ (60 × 728) = 4.58 points per m²', 13, 'start'))
    # range box
    o.append(boxt(440, 50, 270, 150, ['R = c t / 2', 't = 2.00 µs (out and back)', 'R = 299 792 458 × 2.00 × 10⁻⁶ / 2', '= 299.792 m', 'step 0.100° → spacing 0.523 m'], PANEL, L2, 13, True))
    return 345, ''.join(o)
FIG[4] = (f4, 'Flying 1000 m above ground with a ±20° scan, the swath is 728 m wide; at 200 000 pulses per second and 60 m/s that is about 4.6 points per m². One pulse can return twice: first from the canopy (surface model) and last from the ground (terrain model). The box converts a 2.00 µs return into a 299.792 m range.',
          'An aircraft above a triangular scan fan 728 metres wide, a tree hit by one pulse with a first return in the canopy and a last return on the ground, and a box with R equals c t over 2 giving 299.792 metres.')


# ---- 5.5 UAV: GSD by similar triangles and the photo layout ----
def f5():
    o = [T(20, 26, 'GSD by similar triangles', 15, 'start', bold=True)]
    lx, ly = 150, 120
    o.append(L(lx - 30, ly - 50, lx + 30, ly - 50, INK, 3)); o.append(T(lx + 40, ly - 46, 'sensor: pixel p = 2.4 µm', 12, 'start', MUT))
    o.append(f'<ellipse cx="{lx}" cy="{ly}" rx="26" ry="6" style="fill:{NXS};stroke:{NX};stroke-width:1.5"/>'); o.append(T(lx + 40, ly + 4, 'lens', 12, 'start', MUT))
    o.append(T(lx - 40, ly - 22, 'f = 8.8 mm', 12, 'end', MUT))
    gy = 290
    o.append(L(40, gy, 300, gy, INK, 2.5))
    o.append(L(lx - 30, ly - 50, lx + 110, gy, AC, 1.4)); o.append(L(lx + 30, ly - 50, lx - 110, gy, AC, 1.4))
    o.append(L(lx, ly, lx, gy, L2, 1.5, '3 3')); o.append(Tb(lx + 8, 210, 'H = 120 m', 13, 'start', MUT))
    o.append(L(lx - 110, gy + 14, lx + 110, gy + 14, INK, 1.5))
    o.append(T(lx, gy + 34, 'GSD = p H / f = 2.4 µm × 120 / 8.8 mm = 3.27 cm', 13, bold=True, fill=AC))
    # plan of photos, to scale: 0.9 px per metre
    x0, y0, k = 380, 70, 0.9
    o.append(T(x0, 26, 'Photo layout (plan, to scale)', 15, 'start', bold=True))
    fw, fh, sp, ss = 119.4 * k, 179.1 * k, 23.9 * k, 53.7 * k
    o.append(R(x0 + 40, y0, fw, fh, ACS, AC, 2, 1.8))
    o.append(R(x0 + 40 + sp, y0, fw, fh, 'none', AC, 2, 1.8, '6 3'))
    o.append(R(x0 + 40, y0 + ss, fw, fh, 'none', NX, 2, 1.8, '3 3'))
    o.append(L(x0 + 40, y0 - 8, x0 + 40 + sp, y0 - 8, INK, 1.5)); o.append(T(x0 + 40 + sp + 6, y0 - 4, '23.9 m to the next photo', 12, 'start'))
    o.append(L(x0 + 30, y0, x0 + 30, y0 + ss, INK, 1.5)); o.append(T(x0 + 24, y0 + ss / 2 + 4, '53.7 m', 12, 'end'))
    o.append(T(x0 + 40 + fw / 2, y0 + ss + fh + 18, 'photo 119.4 m along track', 12, fill=MUT))
    o.append(T(x0 + 50 + fw + sp, y0 + 40, 'photo 1', 12, 'start', AC, True)); o.append(T(x0 + 50 + fw + sp, y0 + 58, 'photo 2 (dashed)', 12, 'start', AC))
    o.append(T(x0 + 50 + fw + sp, y0 + 76, 'next strip (dotted)', 12, 'start', NX))
    o.append(T(x0 + 50 + fw + sp, y0 + 104, '179.1 m across', 12, 'start', MUT))
    yb = y0 + ss + fh + 44
    o.append(T(x0, yb, '80 % forward overlap: 119.4 × 0.20 = 23.9 m', 13, 'start'))
    o.append(T(x0, yb + 20, '70 % side overlap: 179.1 × 0.30 = 53.7 m', 13, 'start'))
    o.append(T(x0, yb + 40, '3.0 km: 126 intervals → 127 images', 13, 'start', AC, True))
    return yb + 56, ''.join(o)
FIG[5] = (f5, 'Left: the pixel on the sensor and its patch on the ground form similar triangles, so GSD = p H / f = 3.27 cm at 120 m. Right: each photo covers 119.4 m along track; with 80 % overlap a new photo is taken every 23.9 m, and with 70 % side overlap the strips are 53.7 m apart.',
          'Side view of a drone camera with pixel size 2.4 micrometres, focal length 8.8 millimetres and height 120 metres giving a ground sample distance of 3.27 centimetres; plan of two strips of overlapping photo footprints with spacings of 23.9 metres and 53.7 metres.')


# ---- 5.6 setting out from A with backsight B, check from B ----
def f6():
    o = [T(20, 26, 'Setting out P from A, oriented on B', 15, 'start', bold=True)]
    k = 2.2; ox, oy = 120, 170
    X = lambda e: ox + (e - 2000) * k; Y = lambda n: oy - (n - 3000) * k
    A_ = (X(2000), Y(3000)); B_ = (X(2100), Y(3050)); P_ = (X(2040), Y(2970))
    o.append(north(A_[0] - 70, 60))
    o.append(L(*A_, *B_, L2, 2, '6 4')); o.append(L(*A_, *P_, AC, 2.6, arrow='n')); o.append(L(*B_, *P_, NX, 2, '4 3'))
    o.append(L(A_[0], A_[1], A_[0], A_[1] - 80, MUT, 1.2, '3 3'))
    o.append(arcdeg(A_[0], A_[1], 40, 0, 63.435, MUT, 1.5)); o.append(T(A_[0] + 10, A_[1] - 50, '63°26′06″', 12, 'start', MUT))
    o.append(arcdeg(A_[0], A_[1], 62, 63.435, 126.87, AC, 2, 'n')); o.append(T(A_[0] + 84, A_[1] + 34, 'β = 63°26′06″', 13, 'start', AC, True))
    for (x, y), n, dx, dy, an in [(A_, 'A (2000, 3000)', -10, 20, 'end'), (B_, 'B (2100, 3050)', -8, -12, 'middle'), (P_, 'P (2040, 2970)', -8, 24, 'end')]:
        o.append(C(x, y, 6, INK)); o.append(T(x + dx, y + dy, n, 13, an, bold=True))
    o.append(Tb((A_[0] + P_[0]) / 2 - 12, (A_[1] + P_[1]) / 2 + 4, '50.000 m', 13, 'end', AC, True))
    o.append(Tb((B_[0] + P_[0]) / 2 + 30, (B_[1] + P_[1]) / 2 + 10, 'check BP = 100.000 m', 13, 'start', NX, True))
    # level panel
    tx = 470
    o.append(boxt(tx, 70, 240, 116, ['Azimuth AB = 63°26′06″', 'Azimuth AP = 126°52′12″', 'β = AP − AB = 63°26′06″', 'AP = √(40² + 30²) = 50.000 m'], PANEL, L2, 13))
    o.append(boxt(tx, 204, 240, 80, ['HI = 100.000 + 1.385 = 101.385', 'staff on peg = 101.385 − 101.250', '= 0.135 m'], PANEL, LV, 13))
    return 335, ''.join(o)
FIG[6] = (f6, 'The instrument at A is set to zero on B (azimuth 63°26′06″) and turned β = 63°26′06″ to the azimuth of P, 126°52′12″; 50.000 m is laid out and the peg is checked by measuring BP = 100.000 m. The level brings the peg top to 101.250 m with a staff reading of 0.135 m.',
          'Plan of control A and backsight B with the target P set out at 50.000 metres after turning 63 degrees 26 minutes 6 seconds, the check line B to P of 100.000 metres, and boxes with the azimuth working and the staff reading of 0.135 metres.')


# ---- 5.7 sounding reduced to chart datum, and the shaft transfer ----
def f7():
    o = [T(20, 26, 'Sounding reduced to chart datum', 15, 'start', bold=True)]
    ws = 80; tr, cd, bed = ws + 16, ws + 34, ws + 210   # drawn out of scale near the surface
    o.append(f'<path d="M20,{ws} L360,{ws} L360,{bed + 20} L20,{bed + 20} Z" style="fill:{NXS};stroke:none"/>')
    o.append(L(20, ws, 360, ws, NX, 2.2)); o.append(T(24, ws - 8, 'water surface', 13, 'start', NX))
    o.append(L(20, cd, 360, cd, LV, 2, '7 4')); o.append(T(24, cd + 18, 'chart datum, 1.20 m below the surface', 13, 'start', LV))
    o.append(f'<path d="M20,{bed + 4} Q190,{bed - 10} 360,{bed + 8}" style="fill:none;stroke:{INK};stroke-width:2.5"/>'); o.append(T(352, bed + 28, 'bed', 13, 'end'))
    bx = 300
    o.append(f'<path d="M{bx - 40},{ws - 2} L{bx + 40},{ws - 2} L{bx + 28},{ws - 20} L{bx - 28},{ws - 20} Z" style="fill:{INK}"/>')
    o.append(L(bx, ws, bx, tr, INK, 3)); o.append(C(bx, tr, 5, AC)); o.append(T(bx - 50, ws - 26, 'transducer 0.50 m down', 12, 'middle', MUT))
    xs = [bx, bx - 30, bx - 60]
    o.append(L(xs[0], tr + 4, xs[0], bed, AC, 2, arrow='n'))
    o.append(L(xs[1], ws, xs[1], bed, INK, 1.6)); o.append(L(xs[2], cd, xs[2], bed, LV, 2))
    o.append(Tb(xs[2] - 10, ws + 90, 'd = 1500 × 0.040 / 2 = 30.00 m', 13, 'end', AC, True))
    o.append(Tb(xs[2] - 10, ws + 120, 'below surface: 30.00 + 0.50 = 30.50 m', 13, 'end', INK))
    o.append(Tb(xs[2] - 10, ws + 150, 'below datum: 30.50 − 1.20 = 29.30 m', 13, 'end', LV, True))
    o.append(T(20, bed + 44, 'depths near the surface drawn larger than scale', 12, 'start', MUT))
    # shaft
    x0 = 390
    o.append(T(x0, 26, 'Shaft: two wires carry the azimuth down', 15, 'start', bold=True))
    o.append(L(x0, 80, 710, 80, INK, 2)); o.append(T(x0, 72, 'surface', 12, 'start', MUT))
    o.append(R(x0 + 40, 80, 60, 150, 'none', L2, 2, 1.5))
    for wx in (x0 + 56, x0 + 84):
        o.append(L(wx, 70, wx, 228, LV, 1.8)); o.append(C(wx, 230, 4, LV))
    o.append(T(x0 + 56, 64, 'W1', 12, 'middle', LV, True)); o.append(T(x0 + 86, 64, 'W2', 12, 'middle', LV, True))
    o.append(L(x0 + 100, 230, 710, 230, INK, 2)); o.append(L(x0 + 100, 262, 710, 262, INK, 2)); o.append(T(700, 254, 'tunnel', 12, 'end', MUT))
    o.append(L(x0 + 56, 246, x0 + 220, 246, AC, 2.4, arrow='n')); o.append(C(x0 + 220, 246, 5, AC)); o.append(T(x0 + 228, 250, 'S', 14, 'start', AC, True))
    o.append(T(x0, 298, 'W1W2 = 4.000 m at 47°15′20″; S 16.000 m from W1', 13, 'start'))
    o.append(T(x0, 318, 'S = (5011.750, 8010.860)', 13, 'start', AC, True))
    o.append(T(x0, 338, '10″ wrong → 0.097 m at 2000 m', 13, 'start', LV, True))
    return 360, ''.join(o)
FIG[7] = (f7, 'Left: the sounder measures 30.00 m from the transducer, which is 0.50 m down, so the bed is 30.50 m below the surface and, with the tide 1.20 m above chart datum, 29.30 m below datum. Right: two plumb wires 4.000 m apart carry the surface azimuth down the shaft to fix the first tunnel station S.',
          'Section of water with the boat, the transducer 0.50 metres down, the chart datum 1.20 metres below the surface and depths of 30.00, 30.50 and 29.30 metres; section of a shaft with two plumb wires W1 and W2 and the first tunnel station S.')

spec = make_spec(FIG)
