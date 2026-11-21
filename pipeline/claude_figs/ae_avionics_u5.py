"""Claude's hand-drawn figures for ae-avionics-u5 (Avionics: radio, inertial and satellite navigation), one per chapter.
Every number is computed here from that chapter's worked example. Colours are the shell's CSS variables."""
import os, sys, math, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

_T, _Tb, _boxt = T, Tb, boxt


def _sub(s):
    """x_s style subscripts drawn as real subscripts, never as underscores"""
    return re.sub(r'([A-Za-zα-ωΔρσ])_([A-Za-z0-9]+)', r'\1<tspan baseline-shift="sub" font-size="11">\2</tspan>', s)


def T(x, y, s, *a, **k): return _T(x, y, _sub(s), *a, **k)
def Tb(x, y, s, *a, **k): return _Tb(x, y, _sub(s), *a, **k)
def boxt(x, y, w, h, lines, *a, **k): return _boxt(x, y, w, h, [_sub(l) for l in lines], *a, **k)


def circ(cx, cy, r, c=AC, w=2.5, dash=None, fill='none'):
    d = f';stroke-dasharray:{dash}' if dash else ''
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" style="fill:{fill};stroke:{c};stroke-width:{w}{d}"/>'


def arcpts(cx, cy, r, a0, a1, n=60):
    """points on a circle (angles in degrees, y up on paper so y = cy - r sin a)"""
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy - r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]


def poly(pts, fill, stroke='none', op=1.0, w=1.5):
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" style="fill:{fill};fill-opacity:{op};stroke:{stroke};stroke-width:{w}"/>'


FIG = {}


# ---- 5.1 the two-DME fix of the worked example, and what the cut angle does to the error ----
def f1():
    o = []
    s = 2.7
    ax, ay = 150, 290
    bx = ax + 130 * s
    xa = (50**2 - 120**2 + 130**2) / 260; ha = math.sqrt(50**2 - xa**2)
    px, py = ax + xa * s, ay - ha * s
    my = ay + ha * s
    o.append(L(ax, ay, bx, ay, L2, 1.5, '6 5'))
    o.append(Tb((ax + bx) / 2, ay + 22, 'baseline AB = 130 nm', 13, fill=MUT))
    o.append(circ(ax, ay, 50 * s, AC, 2.5))
    o.append(P(arcpts(bx, ay, 120 * s, 150, 210), LV, 2.5))
    o.append(L(ax, ay, px, py, AC, 1.5, '4 4')); o.append(L(bx, ay, px, py, LV, 1.5, '4 4'))
    o.append(Tb((ax + px) / 2 - 30, (ay + py) / 2, '50 nm', 13, fill=AC, bold=True))
    o.append(Tb((bx + px) / 2 + 30, (ay + py) / 2 - 12, '120 nm', 13, fill=LV, bold=True))
    # right-angle mark at the fix
    ua = ((ax - px) / (50 * s), (ay - py) / (50 * s)); ub = ((bx - px) / (120 * s), (ay - py) / (120 * s))
    q = 12
    o.append(P([(px + ua[0] * q, py + ua[1] * q), (px + ua[0] * q + ub[0] * q, py + ua[1] * q + ub[1] * q), (px + ub[0] * q, py + ub[1] * q)], INK, 1.5))
    o.append(C(ax, ay, 6, AC)); o.append(T(ax - 14, ay + 5, 'A', 15, 'end', bold=True))
    o.append(C(bx, ay, 6, LV)); o.append(T(bx + 12, ay + 5, 'B', 15, 'start', bold=True))
    o.append(C(px, py, 7, NX)); o.append(Tb(px + 14, py - 14, 'fix: θ = 90°', 14, 'start', NX, bold=True))
    o.append(C(px, my, 6, L2, PANEL)); o.append(Tb(px + 12, my + 20, 'mirror crossing', 13, 'start', MUT))
    o.append(L(px, ay, px, py, MUT, 1.2, '2 3'))
    o.append(T(px + 6, ay - 8, f'{xa:.2f} nm', 13, 'start', MUT))
    o.append(Tb(px + 8, ay - 44, f'{ha:.2f} nm', 13, 'start', MUT))
    # inset: error box for a 90° and a 30° cut
    def cut(cx, cy, deg, lab):
        r = []
        hw, ln = 9, 62
        for ang in (0, deg):
            a = math.radians(ang)
            dx, dy = math.cos(a), -math.sin(a)
            nx, ny = -dy, dx
            for sgn in (-1, 1):
                r.append(L(cx - dx * ln + nx * hw * sgn, cy - dy * ln + ny * hw * sgn, cx + dx * ln + nx * hw * sgn, cy + dy * ln + ny * hw * sgn, L2, 1.5))
        # the overlap parallelogram
        a1, a2 = 0.0, math.radians(deg)
        d1 = (math.cos(a1), -math.sin(a1)); d2 = (math.cos(a2), -math.sin(a2))
        k1 = hw / math.sin(a2 - a1)
        pts = []
        for s1, s2 in ((1, 1), (1, -1), (-1, -1), (-1, 1)):
            pts.append((cx + d1[0] * k1 * s1 + d2[0] * k1 * s2, cy + d1[1] * k1 * s1 + d2[1] * k1 * s2))
        r.append(poly(pts, NX, NX, 0.35))
        r.append(T(cx, cy + 82, lab, 13, fill=INK, bold=True))
        return ''.join(r)
    o.append(R(560, 40, 150, 470, PANEL, L2, 8, 1.5))
    o.append(T(635, 66, 'error box', 14, bold=True)); o.append(T(635, 84, '(band ±σ each)', 13, fill=MUT))
    o.append(cut(635, 170, 90, 'cut 90°: σ'))
    o.append(cut(635, 380, 30, 'cut 30°: 2σ'))
    return 530, ''.join(o)

FIG[1] = (f1, 'The worked example: the 50 nm circle round A and the 120 nm circle round B cross at right angles, 19.23 nm along AB and 46.15 nm off it. The panel shows why the cut angle matters: the same ±σ bands give a box twice as long at 30°.',
          'Station A with a 50 nautical mile range circle and station B, 130 nautical miles away, with a 120 nautical mile range arc. They cross at the fix, marked with a right angle, 19.23 nautical miles along the baseline and 46.15 off it; a mirror crossing lies below the baseline. A side panel shows two crossing error bands: at 90 degrees they make a small square, at 30 degrees a long thin diamond twice as long.')


# ---- 5.2 the LORAN hyperbola of the worked example among its family ----
def f2():
    o = []
    cx, cy, s = 360, 250, 0.82        # px per km, origin at the baseline centre
    fk = 300.0
    mx, sx = cx - fk * s, cx + fk * s
    o.append(L(40, cy, 680, cy, L2, 1.2, '6 5'))
    o.append(L(mx, cy, sx, cy, INK, 2.5))
    for a, lab, c, w in ((0.0, 'Δr = 0', MUT, 1.8), (15.0, 'Δr = 30 km', NX, 3.2), (100.0, 'Δr = 200 km', AC, 2.2), (200.0, 'Δr = 400 km', AC, 2.2), (270.0, 'Δr = 540 km', AC, 2.2)):
        for side in (-1, 1):
            pts = []
            if a == 0:
                pts = [(cx, cy - 210), (cx, cy + 210)]
            else:
                b = math.sqrt(fk**2 - a**2)
                for i in range(-40, 41):
                    y = i / 40 * 250
                    x = a * math.sqrt(1 + (y / b) ** 2)
                    X, Y = cx + side * x * s, cy - y * s
                    if 40 <= X <= 680 and 40 <= Y <= 460: pts.append((X, Y))
            if a == 0 and side == 1: continue
            o.append(P(pts, c, w, '6 4' if a == 0 else None))
        if a == 15.0:
            o.append(Tb(cx - a * s - 24, 60, lab + ' (example):', 13, 'end', NX, bold=True))
            o.append(Tb(cx - a * s - 24, 78, 'secondary 100 µs later', 13, 'end', NX))
        elif a == 0:
            o.append(Tb(cx + 24, 450, lab, 13, 'start', MUT))
        else:
            b = math.sqrt(fk**2 - a**2); yl = {100.0: 150, 200.0: 90, 270.0: 30}[a]
            o.append(Tb(cx - a * math.sqrt(1 + (yl / b) ** 2) * s - 6, cy - yl * s - 6, lab, 13, 'end', AC))
    o.append(C(mx, cy, 7, AC)); o.append(T(mx, cy + 26, 'Master', 14, bold=True))
    o.append(C(sx, cy, 7, LV)); o.append(T(sx, cy + 26, 'Secondary', 14, bold=True))
    o.append(Tb(cx + 70, cy + 44, '600 km baseline', 13, 'middle', MUT))
    o.append(C(cx - 15 * s, cy, 5, NX)); o.append(T(cx - 15 * s - 4, cy - 10, '15 km', 13, 'end', NX))
    o.append(Tb(560, 80, 'mirror curves: the same Δr', 13, 'middle', MUT))
    o.append(Tb(560, 98, 'with the secondary nearer', 13, 'middle', MUT))
    o.append(Tb(20, cy + 50, 'baseline extension:', 13, 'start', MUT))
    o.append(Tb(20, cy + 68, 'lines far apart', 13, 'start', MUT))
    return 480, ''.join(o)

FIG[2] = (f2, 'Lines of constant range difference for the worked example\'s 600 km master–secondary pair. The example\'s Δr = 30 km gives the nearly straight hyperbola 15 km from the centre on the master\'s side; larger Δr bends the lines round the stations.',
          'A master and a secondary station 600 kilometres apart on a horizontal baseline. Hyperbolas of constant range difference are drawn on the master side: a straight dashed perpendicular bisector for zero difference, a nearly straight curve 15 kilometres from the centre for 30 kilometres (the worked example), and curves bending round the master for 200, 400 and 540 kilometres. A note marks the baseline extension, where the lines spread far apart.')


# ---- 5.3 ILS plan and side views with the two worked examples ----
def f3():
    o = []
    # plan view (top): localizer
    o.append(T(20, 28, 'Plan view: localizer (left-right), angles exaggerated', 15, 'start', bold=True))
    ly = 120
    lx = 660                         # localizer antenna, beyond the far end
    o.append(R(470, ly - 10, 170, 20, PANEL, INK, 2, 1.5))
    o.append(T(555, ly + 36, 'runway', 13, fill=MUT))
    o.append(C(lx, ly, 6, AC)); o.append(T(lx, ly - 14, 'LOC', 13, bold=True))
    o.append(L(40, ly, lx, ly, INK, 1.5, '6 5'))
    for sgn in (-1, 1):
        o.append(L(lx, ly, 40, ly + sgn * (lx - 40) * math.tan(math.radians(4.3)), L2, 1.5))
    o.append(poly([(lx, ly), (40, ly - (lx - 40) * math.tan(math.radians(4.3))), (40, ly)], ACS, 'none', 0.9))
    o.append(poly([(lx, ly), (40, ly + (lx - 40) * math.tan(math.radians(4.3))), (40, ly)], LVS, 'none', 0.9))
    o.append(L(40, ly, lx, ly, INK, 1.5, '6 5'))
    o.append(T(60, ly - 22, '90 Hz stronger (left)', 14, 'start', AC, bold=True))
    o.append(T(60, ly + 32, '150 Hz stronger (right)', 14, 'start', LV, bold=True))
    o.append(T(300, ly - 52, 'full scale, DDM 0.155', 13, fill=MUT))
    ax = lx - 340; ayy = ly - 340 * math.tan(math.radians(0.94)) * 3.0
    o.append(C(ax, ayy, 6, NX)); o.append(Tb(ax, ayy - 12, 'example 2: 0.94° left, fly right', 13, 'middle', NX, bold=True))
    # side view (bottom): glide path
    o.append(T(20, 222, 'Side view: glide path (up-down), angles exaggerated', 15, 'start', bold=True))
    gx, gy = 640, 470                  # glide path origin on the runway
    o.append(L(30, gy, 700, gy, INK, 2))
    o.append(R(540, gy - 6, 150, 6, PANEL, INK, 1, 1))
    o.append(T(615, gy + 22, 'runway', 13, fill=MUT))
    E = 5.5                            # angle exaggeration in the drawing
    ang = 3 * E; up = (3 + 0.7) * E; dn = (3 - 0.7) * E
    yat = lambda a, x: gy - (gx - x) * math.tan(math.radians(a))
    def ray(a, c, w, dash=None):
        return L(gx, gy, 30, yat(a, 30), c, w, dash)
    o.append(poly([(gx, gy), (30, yat(up, 30)), (30, yat(ang, 30))], ACS, 'none', 0.9))
    o.append(poly([(gx, gy), (30, yat(ang, 30)), (30, yat(dn, 30))], LVS, 'none', 0.9))
    o.append(ray(up, L2, 1.5)); o.append(ray(dn, L2, 1.5)); o.append(ray(ang, INK, 2.5))
    o.append(C(gx, gy, 6, AC)); o.append(T(gx, gy - 12, 'GP', 13, bold=True))
    o.append(T(40, 244, '90 Hz stronger above', 14, 'start', AC, bold=True))
    o.append(T(40, 396, '150 Hz stronger below', 14, 'start', LV, bold=True))
    o.append(Tb(520, 412, '3° path', 13, 'middle', INK, bold=True))
    o.append(T(690, 360, 'sector edges ±0.7°:', 13, 'end', MUT))
    o.append(T(690, 378, 'full scale, DDM 0.175', 13, 'end', MUT))
    px = 150
    yp, ya = yat(ang, px), yat((3 - 0.2) * E, px)
    o.append(L(px - 14, yp, px + 14, yp, NX, 2))
    o.append(C(px, ya, 6, NX))
    o.append(T(40, 428, 'example 1 (dot): 5.0 nm out, 0.20° low,', 13, 'start', NX, bold=True))
    o.append(T(40, 446, '1486 ft instead of 1592 ft: fly up', 13, 'start', NX, bold=True))
    return 500, ''.join(o)

FIG[3] = (f3, 'The two beams with the worked examples: localizer 90 Hz left and 150 Hz right; glide path 90 Hz above and 150 Hz below. Example 1 is 0.20° low, example 2 is 0.94° left.',
          'Top, a plan view: the localizer antenna beyond the runway sends a course sector, shaded 90 hertz on the left and 150 hertz on the right of the dashed centreline, with full scale at DDM 0.155; an aircraft 0.94 degrees left must fly right. Bottom, a side view: the glide path antenna beside the runway defines a 3 degree path with 90 hertz above and 150 hertz below, full scale plus or minus 0.7 degrees; an aircraft 5 nautical miles out is 0.2 degrees low, at 1486 feet instead of 1592, and must fly up.')


# ---- 5.4 free gyro in its gimbals, and the vectors of precession with the example's numbers ----
def f4():
    o = []
    cx, cy = 180, 220
    o.append(f'<ellipse cx="{cx}" cy="{cy}" rx="150" ry="150" style="fill:none;stroke:{L2};stroke-width:6"/>')
    o.append(f'<ellipse cx="{cx}" cy="{cy}" rx="38" ry="112" style="fill:none;stroke:{MUT};stroke-width:6"/>')
    o.append(f'<ellipse cx="{cx}" cy="{cy}" rx="70" ry="24" style="fill:{ACS};stroke:{AC};stroke-width:3"/>')
    o.append(L(cx, cy - 145, cx, cy - 60, INK, 2)); o.append(L(cx, cy + 60, cx, cy + 145, INK, 2))
    o.append(L(cx, cy - 24, cx, cy - 130, AC, 3.5, None, 'n'))
    o.append(T(cx + 10, cy - 118, 'spin axis, H', 14, 'start', AC, bold=True))
    o.append(L(cx - 175, cy, cx - 150, cy, INK, 3)); o.append(L(cx + 150, cy, cx + 175, cy, INK, 3))
    o.append(T(cx, cy + 46, 'rotor', 14, bold=True))
    o.append(T(cx + 44, cy + 92, 'inner gimbal', 13, 'start', MUT))
    o.append(T(24, 96, 'outer gimbal', 13, 'start', MUT))
    o.append(T(cx, 26, 'Free (TDF) gyro', 15, bold=True))
    o.append(T(cx, 424, 'caging locks the gimbals;', 13, fill=MUT))
    o.append(T(cx, 442, 'the rotor keeps spinning', 13, fill=MUT))
    # vector diagram (right): looking down the axis of precession
    ox, oy = 440, 300
    o.append(T(560, 26, 'Precession, example numbers', 15, bold=True))
    o.append(L(ox, oy, ox + 230, oy, AC, 4, None, 'n'))
    o.append(T(ox + 120, oy + 24, 'H = Iω = 0.3016 kg·m²/s', 14, 'middle', AC, bold=True))
    o.append(L(ox, oy, ox, oy - 140, LV, 3, None, 'l'))
    o.append(T(ox + 12, oy - 128, 'torque T = 5 µN·m', 14, 'start', LV, bold=True))
    o.append(T(ox + 12, oy - 110, '(friction, at right angles to H)', 13, 'start', MUT))
    a = math.radians(14)
    o.append(L(ox, oy, ox + 230 * math.cos(a), oy - 230 * math.sin(a), NX, 3, '7 5', 'x'))
    o.append(L(ox + 230, oy, ox + 230, oy - 230 * math.sin(a), LV, 2, None, 'l'))
    o.append(T(ox + 222, oy - 30, 'dH = T dt', 13, 'end', LV))
    o.append(Tb(ox + 140, oy - 66, 'H a moment later', 13, 'middle', NX))
    o.append(f'<path d="M{ox + 120:.1f},{oy:.1f} A120,120 0 0 0 {ox + 120 * math.cos(a):.1f},{oy - 120 * math.sin(a):.1f}" style="fill:none;stroke:{NX};stroke-width:2"/>')
    o.append(boxt(420, 340, 280, 84, ['Ω = T ÷ H = 1.66 × 10⁻⁵ rad/s', '= 3.42 °/h of real drift', '+ 3.38 °/h apparent at 13° N'], PANEL, NX, 14, bold_first=True))
    o.append(T(560, 448, 'the axis turns towards T', 13, fill=MUT))
    return 470, ''.join(o)

FIG[4] = (f4, 'Left, a free (TDF) gyro: the rotor spins inside an inner and an outer gimbal. Right, the first worked example as vectors: the 5 µN·m friction torque adds dH at right angles to H, so the axis precesses at 3.42 °/h.',
          'Left, a rotor inside two gimbal rings, with its spin axis and angular momentum H pointing up. Right, a vector diagram: H of 0.3016 kilogram metre squared per second points right, the friction torque of 5 micronewton metres points up at right angles, the small change dH equals T times dt, and H a moment later is turned slightly towards T. A box gives omega equals T over H, 1.66 times ten to the minus five radians per second, or 3.42 degrees per hour of real drift, plus 3.38 degrees per hour of apparent drift at 13 degrees north.')


# ---- 5.5 strapdown block diagram, and the gyro-bias error of the worked example ----
def f5():
    o = []
    o.append(T(20, 26, 'Strapdown INS: block diagram', 15, 'start', bold=True))
    y = 82
    bx = [(20, 'IMU', '3 gyros + 3 accel.'), (160, 'Attitude', 'integrate ω'), (300, 'Resolve f', 'body → NED'), (440, '+ gravity', 'a = f + g'), (580, '∫ twice', 'v, then position')]
    for i, (x, a, b) in enumerate(bx):
        o.append(boxt(x, y - 30, 120, 60, [a, b], ACS if i in (0, 4) else PANEL, AC, 13, bold_first=True))
        if i:
            o.append(L(x - 20, y, x - 2, y, AC, 2, None, 'n'))
    o.append(P([(80, y + 30), (80, y + 54), (360, y + 54), (360, y + 34)], L2, 2, '5 4'))
    o.append(T(140, y + 72, 'specific force f (body axes)', 13, fill=MUT))
    o.append(P([(640, y + 30), (640, y + 98), (262, y + 98), (262, y + 34)], NX, 2, '6 4'))
    o.append(T(450, y + 116, 'Schuler loop: position keeps the level frame level (84.4 min)', 13, fill=NX))
    # plot: position error from a 0.01 °/h gyro bias
    x0, x1, y0, y1 = 90, 690, 250, 450
    g, R = 9.81, 6.371e6; ws = math.sqrt(g / R); e = math.radians(0.01) / 3600
    fx = lambda t: x0 + t / 3.0 * (x1 - x0)
    fy = lambda p: y1 - p / 6.0 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 0.5, 1, 1.5, 2, 2.5, 3], [0, 2, 4, 6], fx, fy, 'time since alignment (h)', 'position error (km), gyro bias 0.01 °/h'))
    op = [(fx(t / 3600), fy(g * e * t**3 / 6 / 1000)) for t in range(0, 4000, 60) if g * e * t**3 / 6 / 1000 <= 6.0]
    sc = [(fx(t / 3600), fy(R * e * (t - math.sin(ws * t) / ws) / 1000)) for t in range(0, 10801, 60)]
    o.append(P(op, L2, 2.5, '7 5')); o.append(P(sc, AC, 3))
    p1 = R * e * (3600 - math.sin(ws * 3600) / ws) / 1000; p0 = g * e * 3600**3 / 6 / 1000
    o.append(C(fx(1), fy(p0), 5, L2, PANEL)); o.append(T(fx(1) + 10, fy(p0) + 5, f'open loop gεt³/6: {p0:.2f} km', 13, 'start', MUT))
    o.append(C(fx(1), fy(p1), 6, AC)); o.append(Tb(fx(1) + 10, fy(p1) + 22, f'Schuler loop: {p1:.2f} km at 1 h', 13, 'start', AC, bold=True))
    o.append(Tb(fx(2.55), fy(3.6), 'ramp about 0.6 nm per hour', 13, 'middle', AC))
    return 500, ''.join(o)

FIG[5] = (f5, 'Top, the strapdown chain with its Schuler feedback. Bottom, the worked example\'s 0.01 °/h gyro bias: the open-loop t³ curve (dashed) holds only for minutes; with the Schuler loop the error is 1.35 km at one hour.',
          'Top, five blocks in a row: IMU, attitude integration, resolving specific force into north-east-down, adding gravity, and integrating twice to velocity and position, with a dashed Schuler feedback loop from position back to attitude. Bottom, a graph of position error in kilometres against time in hours for a 0.01 degree per hour gyro bias: the dashed open-loop cubic curve reaches 3.70 kilometres at one hour, while the solid Schuler-loop curve is 1.35 kilometres at one hour and rises as a gentle ramp with a ripple to about 3.2 kilometres at three hours.')


# ---- 5.6 the clock bias in the worked example's one-dimensional model ----
def f6():
    o = []
    s = 50.0
    x0 = 60
    X = lambda km: x0 + km * s
    y = 150
    o.append(T(360, 28, 'Pseudoranges on a straight road: both too long by the same b', 15, bold=True))
    o.append(L(X(0) - 10, y, X(12) + 10, y, INK, 2))
    for k in range(0, 13, 2):
        o.append(L(X(k), y, X(k), y + 6, L2, 1.5)); o.append(T(X(k), y + 22, f'{k}', 13, fill=MUT))
    o.append(T(X(6), y + 42, 'distance from A (km)', 13, fill=MUT))
    o.append(C(X(0), y, 8, AC)); o.append(T(X(0), y - 16, 'A', 15, bold=True))
    o.append(C(X(12), y, 8, LV)); o.append(T(X(12), y - 16, 'B', 15, bold=True))
    o.append(C(X(5), y, 7, NX)); o.append(T(X(5), y - 16, 'receiver, x = 5.000', 14, bold=True, fill=NX))
    ya, yb = 220, 270
    o.append(R(X(4.7), ya - 14, (5.3 - 4.7) * s, yb - ya + 28, NXS, NX, 3, 1.5))
    o.append(L(X(0), ya, X(5.3), ya, AC, 3, None, 'n')); o.append(T(X(0), ya - 10, 'ρ_A = 5.300 km', 14, 'start', AC, bold=True))
    o.append(L(X(12), yb, X(12 - 7.3), yb, LV, 3, None, 'l')); o.append(T(X(12), yb + 24, 'ρ_B = 7.300 km', 14, 'end', LV, bold=True))
    o.append(L(X(5), 200, X(5), 300, NX, 1.5, '4 4'))
    o.append(T(X(5), 320, 'overlap 0.600 km = 2b', 14, fill=NX, bold=True))
    o.append(boxt(150, 345, 420, 76, ['ρ_A = x + b,   ρ_B = (12 − x) + b', 'add: b = 0.300 km, so δt = b ÷ c = 1.00 µs', 'subtract: x = 5.000 km'], PANEL, NX, 14, bold_first=True))
    return 440, ''.join(o)

FIG[6] = (f6, 'Worked example 2 to scale: the fast clock makes both pseudoranges 0.300 km too long, so they overlap by 0.600 km. Two readings fix x and the bias b.',
          'A straight road from beacon A at 0 to beacon B at 12 kilometres, with the receiver at 5 kilometres. An arrow from A of 5.3 kilometres and an arrow from B of 7.3 kilometres both overshoot the receiver; they overlap by 0.6 kilometres, twice the range bias b. A box gives the equations rho A equals x plus b and rho B equals 12 minus x plus b, so b is 0.3 kilometres, the clock offset is 1.00 microsecond, and x is 5.000 kilometres.')


# ---- 5.7 the two atmospheric delays of the worked example ----
def f7():
    o = []
    gy = 400
    o.append(L(20, gy, 400, gy, INK, 2)); o.append(T(30, gy + 22, 'receiver', 13, 'start', bold=True))
    o.append(R(20, 330, 380, 70, LVS, 'none', 0)); o.append(T(200, 360, 'troposphere (up to 9 to 17 km)', 13, 'start', LV, bold=True))
    o.append(R(20, 120, 380, 110, ACS, 'none', 0)); o.append(T(96, 180, 'ionosphere (60 to 1000 km)', 13, 'start', AC, bold=True))
    rx, ry = 70, gy
    o.append(L(rx, ry, rx, 60, INK, 2, None, 'n')); o.append(T(rx + 8, 72, 'zenith', 13, 'start', MUT))
    a = math.radians(30)  # drawn steeper than 10° so it fits; the numbers are for 10°
    o.append(L(rx, ry, 400, 95, NX, 2.5, '7 5', 'x'))
    o.append(T(400, 82, 'to a low satellite', 13, 'end', NX))
    o.append(T(205, 290, 'slant path: d_z ÷ sin E', 13, 'start', NX, bold=True))
    o.append(C(rx, ry, 6, INK))
    # bars (right)
    x0 = 440
    o.append(T(575, 40, 'Delays in the example (m)', 15, bold=True))
    bars = [('ionosphere, L1', 12.0, AC), ('ionosphere, L5', 21.52, AC), ('troposphere, zenith', 2.5, LV), ('troposphere, 10°', 14.40, LV), ('after L1/L5 combination', 0.0, MUT)]
    sc = 10.5
    for i, (lab, v, c) in enumerate(bars):
        yy = 70 + i * 62
        o.append(T(x0, yy + 14, lab, 13, 'start'))
        o.append(R(x0, yy + 22, max(v * sc, 2), 20, c, c, 3, 1))
        o.append(T(x0 + max(v * sc, 2) + 8, yy + 38, f'{v:.1f}' if v else '0 (first order)', 13, 'start', INK, True))
    o.append(T(575, 400, 'UERE 5.0 m × HDOP 1.8 = 9.0 m', 14, fill=NX, bold=True))
    return 430, ''.join(o)

FIG[7] = (f7, 'Left, the signal crosses the ionosphere and the troposphere, and a low satellite\'s path is longer in both. Right, the worked example: 12.0 m on L1 becomes 21.5 m on L5, the dual-frequency combination removes it, but the 14.4 m tropospheric delay at 10° stays.',
          'Left, a receiver on the ground with a vertical zenith path and a slanting path to a low satellite, both crossing a shaded troposphere layer near the ground and an ionosphere layer higher up. Right, bars: ionosphere 12.0 metres on L1 and 21.5 metres on L5, troposphere 2.5 metres at zenith and 14.4 metres at 10 degrees elevation, and zero first-order ionospheric delay after the L1 and L5 combination. A line reads UERE 5.0 metres times HDOP 1.8 equals 9.0 metres.')


# ---- 5.8 the scalar Kalman update of the worked example ----
def f8():
    o = []
    x0, x1, y0, y1 = 70, 690, 50, 330
    fx = lambda v: x0 + (v - 960) / 110 * (x1 - x0)
    pk = 1 / math.sqrt(2 * math.pi * 20)
    fy = lambda d: y1 - d / (pk * 1.08) * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [960, 980, 1000, 1020, 1040, 1060], [], fx, fy, 'position along track (m)', ''))
    gauss = lambda m, var: [(fx(960 + i * 0.5), fy(math.exp(-(960 + i * 0.5 - m) ** 2 / (2 * var)) / math.sqrt(2 * math.pi * var))) for i in range(221)]
    o.append(P(gauss(1000, 100), L2, 2.5, '7 5'))
    o.append(P(gauss(1050, 25), LV, 2.5))
    o.append(P(gauss(1040, 20), AC, 3.5))
    o.append(L(fx(1000), y1, fx(1000), fy(1 / math.sqrt(2 * math.pi * 100)), L2, 1.2, '3 3'))
    o.append(Tb(fx(1000), fy(1 / math.sqrt(2 * math.pi * 100)) - 12, 'INS 1000 m, P = 100 m²', 13, 'middle', MUT, True))
    o.append(Tb(708, fy(1 / math.sqrt(2 * math.pi * 25)) - 24, 'GPS 1050 m, R = 25 m²', 13, 'end', LV, True))
    o.append(Tb(fx(1040) - 10, fy(pk) - 10, 'blend 1040 m, P = 20 m²', 14, 'end', AC, True))
    o.append(L(fx(1000), y1 + 58, fx(1040), y1 + 58, AC, 2.5, None, 'n'))
    o.append(T(fx(1020), y1 + 76, 'K y = 0.8 × 50 = 40 m', 13, fill=AC, bold=True))
    o.append(L(fx(1050), y1 + 58, fx(1040) + 4, y1 + 58, L2, 1.5, '3 3'))
    return 420, ''.join(o)

FIG[8] = (f8, 'Worked example 1 as probability curves: the INS says 1000 m with variance 100 m², the GPS says 1050 m with variance 25 m², and the update lands at 1040 m with variance 20 m², narrower than either.',
          'Three bell curves on a position axis from 960 to 1070 metres. A wide dashed curve centred at 1000 metres for the INS with variance 100 square metres, a narrower curve at 1050 metres for the GPS with variance 25, and the tallest, narrowest curve at 1040 metres for the blend with variance 20. An arrow below shows the correction K times y equals 0.8 times 50, which is 40 metres.')


# ---- 5.9 pulse radar block diagram and the radio altimeter's FMCW sweep ----
def f9():
    o = []
    o.append(T(20, 26, 'Pulse radar', 15, 'start', bold=True))
    y = 70
    o.append(boxt(20, y, 120, 50, ['Transmitter', 'pulse τ, P_t'], PANEL, AC, 13, bold_first=True))
    o.append(boxt(200, y, 120, 50, ['Duplexer', 'T/R switch'], PANEL, AC, 13, bold_first=True))
    o.append(boxt(380, y, 120, 50, ['Antenna', 'dish or array'], ACS, AC, 13, bold_first=True))
    o.append(boxt(200, y + 90, 120, 50, ['Receiver', 'threshold'], PANEL, AC, 13, bold_first=True))
    o.append(boxt(20, y + 90, 120, 50, ['Timer', 'R = ct ÷ 2'], PANEL, AC, 13, bold_first=True))
    o.append(boxt(560, y + 45, 140, 50, ['Display', 'range, bearing'], LVS, LV, 13, bold_first=True))
    o.append(L(140, y + 25, 198, y + 25, AC, 2, None, 'n')); o.append(L(320, y + 25, 378, y + 25, AC, 2, None, 'n'))
    o.append(L(260, y + 50, 260, y + 88, AC, 2, None, 'n')); o.append(L(200, y + 115, 142, y + 115, AC, 2, None, 'n'))
    o.append(P([(80, y + 50), (80, y + 70)], L2, 1.5, '4 3'))
    o.append(T(88, y + 66, 'start', 13, 'start', MUT))
    o.append(P([(80, y + 140), (80, y + 160), (630, y + 160), (630, y + 97)], AC, 2))
    o.append(L(630, y + 104, 630, y + 97, AC, 2, None, 'n'))
    o.append(T(355, y + 154, 'range', 13, fill=MUT))
    o.append(P([(500, y + 25), (630, y + 25), (630, y + 43)], L2, 1.5, '4 3'))
    o.append(T(565, y + 17, 'bearing', 13, fill=MUT))
    o.append(T(360, y + 186, 'example 1: R_u = 150 km, ΔR = 150 m, f_d = 2.88 kHz', 13, 'middle', MUT))
    # FMCW triangle
    x0, x1, y0, y1 = 90, 690, 320, 500
    tms = 20.0
    fx = lambda t: x0 + t / tms * (x1 - x0)
    fy = lambda f: y1 - (f - 4250) / 120 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 5, 10, 15, 20], [4250, 4300, 4350], fx, fy, 'time (ms)', 'frequency (MHz)'))
    tri = lambda t: 4250 + 100 * (2 * (t % 10) / 10 if (t % 10) < 5 else 2 - 2 * (t % 10) / 10)
    o.append(P([(fx(i * 0.05), fy(tri(i * 0.05))) for i in range(0, 401)], AC, 3))
    lag = 2.4   # drawn delay (exaggerated; the real delay at 500 ft is 1.0 µs)
    o.append(P([(fx(i * 0.05), fy(tri(i * 0.05 - lag))) for i in range(int(lag / 0.05), 401)], LV, 2.5, '7 5'))
    tt = 3.6
    o.append(L(fx(tt), fy(tri(tt)), fx(tt), fy(tri(tt - lag)), NX, 2.5, None, 'x'))
    o.append(Tb(fx(tt) + 8, (fy(tri(tt)) + fy(tri(tt - lag))) / 2 + 5, 'beat f_b', 13, 'start', NX, True))
    o.append(T(fx(10.3), fy(4362), 'sent: ΔF = 100 MHz at f_m = 100 Hz', 13, 'start', AC, True))
    o.append(T(fx(14.5), fy(4282), 'echo (delay exaggerated)', 13, 'start', LV))
    o.append(T(430, 290, 'Radio altimeter (FMCW): 500 ft gives f_b = 20.3 kHz', 15, 'middle', INK, True))
    return 550, ''.join(o)

FIG[9] = (f9, 'Top, the pulse radar chain of the first worked example. Bottom, the radio altimeter of the second: the echo is a delayed copy of the triangular sweep, and the beat between them, 20.3 kHz at 500 ft, is proportional to height.',
          'Top, a block diagram: transmitter to duplexer to antenna; echoes return through the duplexer to the receiver and a timer that computes range as c t over 2; the display shows range and antenna bearing. Example values: unambiguous range 150 kilometres, resolution 150 metres, Doppler 2.88 kilohertz. Bottom, a graph of frequency from 4250 to 4370 megahertz against time over 20 milliseconds: the transmitted triangle sweeps 100 megahertz at 100 hertz, a dashed echo is the same triangle shifted later, and an arrow between them marks the beat frequency, 20.3 kilohertz at 500 feet.')


# ---- 5.10 the FLTA worked example in side view ----
def f10():
    o = []
    x0, x1, y0, y1 = 70, 690, 40, 400
    fx = lambda nm: x0 + nm / 10.0 * (x1 - x0)
    fy = lambda ft: y1 - ft / 5500 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 2, 4, 6, 8, 10], [0, 1000, 2000, 3000, 4000, 5000], fx, fy, 'distance flown (nm)', 'altitude (ft)'))
    terr = [(fx(0), fy(1000)), (fx(8), fy(1000)), (fx(8), fy(3000)), (fx(10), fy(3000)), (fx(10), fy(0)), (fx(0), fy(0))]
    o.append(poly(terr, L2, 'none', 0.35))
    o.append(P([(fx(0), fy(1000)), (fx(8), fy(1000)), (fx(8), fy(3000)), (fx(10), fy(3000))], INK, 2))
    o.append(T(fx(9), fy(3000) + 20, 'ridge 3000 ft', 13, 'middle', INK, True))
    path = [(fx(0), fy(5000)), (fx(8), fy(2000))]
    o.append(P(path, MUT, 2.5, '7 5'))
    o.append(C(fx(8), fy(2000), 6, NX)); o.append(Tb(fx(8) - 8, fy(2000) + 22, 'would hit at 120 s', 13, 'end', NX, True))
    o.append(C(fx(0), fy(5000), 6, INK)); o.append(T(fx(0) + 10, fy(5000) - 10, '5000 ft, 1500 ft/min, 240 kt', 13, 'start', INK, True))
    o.append(C(fx(4), fy(3500), 7, 'var(--accent)')); o.append(Tb(fx(4) + 10, fy(3500) - 12, 'caution, 60 s: 3500 ft', 13, 'start', AC, True))
    o.append(C(fx(6), fy(2750), 7, LV)); o.append(Tb(fx(6) - 10, fy(2750) + 26, 'warning, 30 s: 2750 ft', 13, 'end', LV, True))
    o.append(P([(fx(6), fy(2750)), (fx(8), fy(3500)), (fx(10), fy(3500))], LV, 3))
    o.append(Tb(fx(8.6), fy(3500) - 14, 'climb 1500 ft/min', 13, 'middle', LV, True))
    o.append(L(fx(8), fy(3500), fx(8), fy(3000), NX, 1.5, '3 3')); o.append(T(fx(8) + 6, fy(3250) + 5, '500 ft', 13, 'start', NX))
    o.append(T(fx(4), fy(1000) - 12, 'radio altitude falls from 4000 to 1750 ft: no reactive alert', 13, 'middle', MUT))
    return 450, ''.join(o)

FIG[10] = (f10, 'The forward-looking terrain avoidance example in side view: the descending path would meet the ridge face in 120 s, so the caution comes at 3500 ft and the warning at 2750 ft; climbing at 1500 ft/min from the warning clears the top by 500 ft.',
          'A side view with altitude up to 5000 feet against distance up to 10 nautical miles. Flat ground at 1000 feet rises as a wall to a 3000 foot ridge at 8 nautical miles. A dashed descending path from 5000 feet would strike the ridge face at 2000 feet after 120 seconds. The caution point is at 4 nautical miles and 3500 feet, the warning at 6 nautical miles and 2750 feet, and from the warning a climb of 1500 feet per minute crosses the ridge 500 feet above its top.')

spec = make_spec(FIG)
