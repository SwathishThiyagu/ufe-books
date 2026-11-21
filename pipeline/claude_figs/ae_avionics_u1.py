"""Claude's hand-drawn figures for ae-avionics-u1 (Avionics and Aircraft Systems: flight control systems), one per chapter,
drawn from each chapter's own worked example and numbers. Colours are the shell's CSS variables only."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def lin(a0, a1, b0, b1):
    return lambda v: b0 + (v - a0) * (b1 - b0) / (a1 - a0)


def arrow(x1, y1, x2, y2, c=AC, w=2, k='n', dash=None):
    return L(x1, y1, x2, y2, c, w, dash, arrow=k)


def sup(s):
    return f'<tspan baseline-shift="super" font-size="10">{s}</tspan>'


def sub(s):
    return f'<tspan baseline-shift="sub" font-size="11">{s}</tspan>'


# ---- 1.1 the elevator chain of the worked example: 120 mm, 25°, 60 N, 80 mm horn ----
def f1():
    o = []
    o.append(T(20, 24, '← nose', 13, 'start', MUT)); o.append(T(700, 24, 'tail →', 13, 'end', MUT))
    o.append(L(30, 290, 250, 290, L2, 2)); o.append(T(36, 308, 'cabin floor', 13, 'start', MUT))
    # column, pivot on the floor, grip at the top
    px, py, gy = 80, 284, 104
    o.append(L(px, py, px, gy, INK, 5)); o.append(C(px, py, 6, INK))
    o.append(R(px - 20, gy - 12, 40, 14, PANEL, INK, 5, 2))
    o.append(T(px - 4, gy - 22, 'control column', 13, 'start', INK, True))
    o.append(arrow(px + 26, gy + 10, px + 86, gy + 10, AC, 2.5))
    o.append(T(px + 30, gy + 30, 'pull back', 13, 'start', AC, True)); o.append(T(px + 30, gy + 47, '60 N, 120 mm', 13, 'start', AC, True))
    # push-pull rod to the bell crank's lower arm
    bx, by = 210, 205
    o.append(L(px, 230, bx, 238, INK, 4)); o.append(C(px, 230, 4, INK)); o.append(C(bx, 238, 4, INK))
    o.append(T(140, 258, 'push-pull rod', 13, 'middle', MUT))
    # bell crank: vertical lever pivoted at its centre, arms to the two cables
    yt, yb = 165, 245
    o.append(L(bx, yt, bx, yb, INK, 5)); o.append(C(bx, by, 6, AC))
    o.append(T(bx + 12, by + 5, 'bell crank', 13, 'start', MUT))
    # stabilizer, hinge, horn and elevator (25° trailing edge up)
    hx, hy = 580, 205
    o.append(R(470, hy - 6, hx - 474, 12, PANEL, INK, 6, 2)); o.append(T(520, hy + 26, 'stabilizer', 13, 'middle', MUT))
    o.append(L(hx, yt, hx, yb, INK, 4))
    a = math.radians(25); ex, ey = hx + 92 * math.cos(a), hy - 92 * math.sin(a)
    o.append(f'<path d="M{hx},{hy - 5} L{ex:.1f},{ey:.1f} L{hx},{hy + 5} Z" style="fill:{ACS};stroke:{AC};stroke-width:2"/>')
    o.append(C(hx, hy, 5, AC))
    o.append(L(hx + 18, hy, hx + 92, hy, L2, 1.5, dash='5 4'))
    o.append(f'<path d="M{hx + 66},{hy} A66,66 0 0 0 {hx + 66 * math.cos(a):.1f},{hy - 66 * math.sin(a):.1f}" style="fill:none;stroke:{AC};stroke-width:1.8"/>')
    o.append(T(hx + 80, hy - 14, '25°', 13, 'start', AC, True))
    o.append(T(hx + 70, hy + 28, 'elevator', 13, 'middle', INK, True)); o.append(T(hx + 70, hy + 45, 'trailing edge up', 13, 'middle', MUT))
    o.append(T(hx + 8, yt - 14, 'horn arm 80 mm', 13, 'start', INK))
    # the two cables, turnbuckles and pulleys
    o.append(L(bx, yt, hx, yt, LV, 2.5)); o.append(L(bx, yb, hx, yb, L2, 2, dash='7 5'))
    o.append(arrow(286, yt - 18, 236, yt - 18, LV, 2, 'l'))
    o.append(T(294, yt - 14, 'up cable pulls the upper horn: 206.3 N', 13, 'start', LV, True))
    o.append(T(300, yb + 22, 'down cable (slack side, kept under pre-tension)', 13, 'start', MUT))
    for x in (300,):
        o.append(R(x - 14, yt - 5, 28, 10, PANEL, INK, 3, 1.5)); o.append(R(x - 14, yb - 5, 28, 10, PANEL, INK, 3, 1.5))
    o.append(T(300, yt + 24, 'turnbuckles', 13, 'middle', MUT))
    for x in (430,):
        o.append(f'<circle cx="{x}" cy="{yt + 9}" r="9" style="fill:{PANEL};stroke:{INK};stroke-width:1.5"/>')
        o.append(f'<circle cx="{x}" cy="{yb - 9}" r="9" style="fill:{PANEL};stroke:{INK};stroke-width:1.5"/>')
    o.append(T(430, by + 5, 'pulleys', 13, 'middle', MUT))
    # the numbers
    o.append(T(360, 336, 'gearing G = 120 mm ÷ 25° = 4.8 mm/deg = 0.2750 m/rad', 14, 'middle', AC, True))
    o.append(T(360, 358, 'hinge moment held H = F × G = 60 × 0.2750 = 16.50 N·m', 14, 'middle', AC, True))
    o.append(T(360, 380, 'cable force = 16.50 ÷ 0.080 = 206.3 N', 14, 'middle', AC, True))
    return 398, ''.join(o)


FIG[1] = (f1, 'The elevator chain of the worked example. Pulling the column back 120 mm with 60 N turns the bell crank, the up cable pulls the upper horn '
              'with 206.3 N, and the elevator rises 25°; the pilot holds a hinge moment of 16.50 N·m. The down cable goes slack but stays pre-tensioned.',
          'Side view of a light aircraft elevator control: control column pivoted on the floor, a push-pull rod to a bell crank, two cables with turnbuckles '
          'over pulleys to the upper and lower arms of the elevator horn, and the elevator deflected 25 degrees trailing edge up. The gearing 4.8 mm per degree, '
          'hinge moment 16.50 newton-metres and cable force 206.3 newtons are written below.')


# ---- 1.2 the same 3 m run as a cable loop and as a guided rod ----
def f2():
    o = []
    o.append(T(20, 26, 'Cable loop, 3 m, 6 mm² steel', 14, 'start', INK, True))
    y1, y2 = 62, 112
    o.append(boxt(20, 50, 92, 74, ['pedal', 'quadrant'], PANEL, AC, 13))
    o.append(boxt(600, 50, 100, 74, ['rudder', 'horn'], PANEL, AC, 13))
    o.append(L(112, y1, 600, y1, LV, 3)); o.append(L(112, y2, 600, y2, L2, 2, dash='7 5'))
    o.append(R(196, y1 - 6, 30, 12, PANEL, INK, 3, 1.5)); o.append(R(196, y2 - 6, 30, 12, PANEL, INK, 3, 1.5))
    o.append(T(211, 92, 'turnbuckles', 13, 'middle', MUT))
    for x in (400,):
        o.append(f'<circle cx="{x}" cy="{y1 + 10}" r="10" style="fill:{PANEL};stroke:{INK};stroke-width:1.5"/>')
        o.append(f'<circle cx="{x}" cy="{y2 - 10}" r="10" style="fill:{PANEL};stroke:{INK};stroke-width:1.5"/>')
    o.append(T(400, 134, 'pulleys', 13, 'middle', MUT))
    o.append(arrow(300, y1 - 10, 250, y1 - 10, LV, 2, 'l'))
    o.append(T(310, y1 - 6, 'loaded cable 1.5 kN', 13, 'start', LV, True))
    o.append(T(560, y2 + 22, 'return cable, pre-tension only', 13, 'middle', MUT))
    o.append(T(360, 158, 'stretch ΔL = FL ÷ (AE) = 1500 × 3 ÷ (1.2 × 10' + sup('6') + ') = 3.75 mm', 14, 'middle', AC, True))
    # rod panel
    o.append(L(20, 180, 700, 180, 'var(--line)', 1))
    o.append(T(20, 208, 'Push-pull rod, 3 m, aluminium tube 20/18 mm', 14, 'start', INK, True))
    x0, x1 = 90, 630
    def rod(y, bays, col, label, pcr, ok):
        o.append(arrow(x0 - 46, y, x0 - 6, y, INK, 2.5, 'n')); o.append(arrow(x1 + 46, y, x1 + 6, y, INK, 2.5, 'n'))
        o.append(T(x0 - 50, y - 10, '1.5 kN', 13, 'start', INK)); o.append(T(x1 + 50, y - 10, '1.5 kN', 13, 'end', INK))
        o.append(L(x0, y, x1, y, INK, 5))
        w = (x1 - x0) / bays
        pts = [(x0 + i * (x1 - x0) / 120, y - (12 if bays > 1 else 26) * abs(math.sin(math.pi * bays * i / 120))) for i in range(121)]
        o.append(P(pts, col, 2, dash='5 4'))
        for i in range(bays + 1):
            gx = x0 + i * w
            o.append(f'<path d="M{gx - 8:.1f},{y + 16} L{gx:.1f},{y + 4} L{gx + 8:.1f},{y + 16} Z" style="fill:{PANEL};stroke:{INK};stroke-width:1.5"/>')
        o.append(T(360, y + 38, label, 13, 'middle', MUT))
        o.append(T(360, y + 56, pcr, 13, 'middle', col, True))
    rod(262, 1, LV, 'pinned ends only: one 3000 mm bay', 'P' + sub('cr') + ' = π²EI ÷ L² = 207 N, far below 1500 N: buckles', False)
    rod(370, 4, AC, 'three guides: four bays of 750 mm', 'P' + sub('cr') + ' = 207 × 4² = 3317 N ≥ 1.5 × 1500 = 2250 N: safe', True)
    o.append(T(360, 452, 'stress is only 1500 ÷ 59.7 mm² = 25.1 MPa: buckling, not stress, sizes the rod', 13, 'middle', MUT))
    return 470, ''.join(o)


FIG[2] = (f2, 'The worked example’s 3 m run both ways. The cable carries only pull, so a return cable completes the loop; 1.5 kN stretches it 3.75 mm. '
              'The rod carries push and pull, but over 3 m its Euler load is only 207 N; three guides cut it into four 750 mm bays and raise that to 3317 N.',
          'Top: a cable loop from a pedal quadrant to a rudder horn, with the loaded cable, the dashed return cable, turnbuckles and pulleys, and the stretch '
          'of 3.75 mm. Bottom: the same 3 m as a push-pull rod in compression, once with pinned ends only and a dashed buckled shape, buckling load 207 N, '
          'and once with three guides making four 750 mm bays, buckling load 3317 N.')


# ---- 1.3 the power-assisted loop of the worked example ----
def f3():
    o = []
    o.append(boxt(20, 60, 130, 56, ['control column', '200 N'], ACS, AC, 13, bold_first=True))
    o.append(boxt(200, 60, 130, 56, ['input linkage', 'G = 0.30 m/rad'], PANEL, AC, 13, bold_first=True))
    o.append(boxt(380, 60, 130, 56, ['servo valve', 'spool meters flow'], PANEL, AC, 13, bold_first=True))
    o.append(boxt(560, 60, 140, 56, ['actuator', '8.6 cm² piston'], LVS, LV, 13, bold_first=True))
    o.append(arrow(150, 88, 198, 88)); o.append(arrow(330, 88, 378, 88)); o.append(arrow(510, 88, 558, 88))
    o.append(boxt(380, 2, 130, 34, ['3000 psi = 20.7 MPa'], PANEL, L2, 13))
    o.append(arrow(445, 36, 445, 58, MUT, 2, 'm'))
    # surface
    o.append(boxt(470, 196, 230, 60, ['elevator', 'H = 1837.5 N·m at 100 m/s'], ACS, AC, 14, bold_first=True))
    o.append(arrow(630, 116, 630, 194, LV, 2.5, 'l'))
    o.append(T(620, 150, 'hydraulic share', 13, 'end', LV, True)); o.append(T(620, 167, '1777.5 N·m', 13, 'end', LV, True))
    # mechanical path in parallel
    o.append(P([(265, 116), (265, 226), (466, 226)], AC, 2.5)); o.append(arrow(440, 226, 467, 226))
    o.append(T(275, 150, 'mechanical rod stays:', 13, 'start', AC, True)); o.append(T(275, 167, 'pilot share 60 N·m', 13, 'start', AC, True))
    # follow-up linkage
    o.append(P([(585, 256), (585, 290), (420, 290), (420, 120)], NX, 2, dash='6 4'))
    o.append(arrow(420, 130, 420, 118, NX, 2, 'x'))
    o.append(T(410, 312, 'follow-up linkage: surface position recentres the spool', 13, 'middle', NX, True))
    # share bar
    y = 352; x0, x1 = 60, 660; tot = 1837.5
    xp = x0 + (x1 - x0) * 60 / tot
    o.append(R(x0, y, xp - x0, 26, ACS, AC, 0, 1.5)); o.append(R(xp, y, x1 - xp, 26, LVS, LV, 0, 1.5))
    o.append(T((xp + x1) / 2, y + 18, 'hydraulics 1777.5 N·m (96.7 %)', 13, 'middle', INK, True))
    o.append(T(x0, y - 8, 'pilot 60 N·m (3.3 %)', 13, 'start', AC, True))
    o.append(T(x1, y - 8, 'boost ratio = 1837.5 ÷ 60 = 30.6', 13, 'end', INK, True))
    return 394, ''.join(o)


FIG[3] = (f3, 'The boosted elevator of the worked example. The pilot’s 200 N through 0.30 m/rad still reaches the surface as 60 N·m; the servo valve sends '
              '20.7 MPa fluid to an 8.6 cm² actuator for the other 1777.5 N·m, and the follow-up linkage closes the valve when the surface arrives.',
          'Block diagram: control column, input linkage, servo valve fed from a 3000 psi supply, and actuator, driving the elevator with 1777.5 newton-metres, '
          'while a mechanical rod from the input linkage carries the pilot share of 60 newton-metres to the same elevator. A dashed follow-up linkage runs from '
          'the elevator back to the servo valve. A bar shows the split: pilot 3.3 percent, hydraulics 96.7 percent, boost ratio 30.6.')


# ---- 1.4 Q-feel force from the 75 m/s trim, and the two tab senses ----
def f4():
    o = []
    X0, X1, Y0, Y1 = 70, 430, 40, 300
    fx = lin(75, 250, X0, X1); fy = lin(0, 120, Y1, Y0)
    q1 = 0.5 * 1.225 * 75 ** 2
    F = lambda v: 3 * (0.5 * 1.225 * v * v - q1) / 1000
    o.append(axes(X0, X1, Y0, Y1, [75, 100, 150, 200, 250], [0, 30, 60, 90, 120], fx, fy, 'airspeed V (m/s)', 'stick force above trim (N)'))
    o.append(P([(fx(v), fy(F(v))) for v in range(75, 251, 5)], AC, 3))
    for v, lab in ((75, 'trim: 0 N'), (150, '31.0 N'), (250, '104.5 N')):
        o.append(C(fx(v), fy(F(v)), 6, LV))
    o.append(T(fx(75) + 8, fy(14), 'trim: 0 N', 13, 'start', LV, True))
    o.append(T(fx(150) - 8, fy(F(150)) - 14, '150 m/s: 31.0 N', 13, 'end', LV, True))
    o.append(T(fx(250) - 10, fy(F(250)) + 4, '250 m/s: 104.5 N', 13, 'end', LV, True))
    o.append(T(fx(165), fy(70), 'F = 3 N/kPa × (q − q' + sub('trim') + ')', 13, 'middle', AC, True))
    # tabs panel
    o.append(L(462, 30, 462, 340, 'var(--line)', 1))
    def tab(y, title, note1, note2, same):
        hx = 490
        o.append(T(480, y - 30, title, 14, 'start', INK, True))
        a = math.radians(12)
        ex, ey = hx + 120 * math.cos(a), y + 120 * math.sin(a)
        o.append(L(hx, y, ex, ey, AC, 7)); o.append(C(hx, y, 5, INK))
        b = math.radians(12 + (18 if same else -45))
        tx, ty = ex + 40 * math.cos(b), ey + 40 * math.sin(b)
        o.append(L(ex, ey, tx, ty, LV, 5))
        o.append(T(hx + 4, y - 10, 'hinge', 13, 'start', MUT))
        o.append(T(tx + 6, ty + (16 if same else -4), 'tab', 13, 'start', LV, True))
        o.append(T(480, y + 62, note1, 13, 'start', MUT)); o.append(T(480, y + 79, note2, 13, 'start', MUT))
    tab(84, 'Servo tab', 'tab up, surface down:', 'the tab drives the surface', False)
    tab(250, 'Anti-servo tab', 'tab moves with the surface:', 'more hinge moment, more feel', True)
    return 352, ''.join(o)


FIG[4] = (f4, 'Left: the Q-feel force of the worked example, counted from zero at the 75 m/s trim: 31.0 N at 150 m/s and 104.5 N at 250 m/s, because force '
              'follows dynamic pressure. Right: a servo tab deflects opposite to its surface and drives it; an anti-servo tab moves with the surface and adds feel.',
          'Plot of stick force above trim against airspeed from 75 to 250 metres per second, rising as a parabola from 0 newtons at 75 to 31.0 at 150 and '
          '104.5 at 250. Beside it two sketches of a surface with a trailing-edge tab: the servo tab deflected opposite to the surface, the anti-servo tab '
          'deflected the same way.')


# ---- 1.5 a quadruplex digital FBW chain and the lane numbers of the worked example ----
def f5():
    o = []
    o.append(boxt(20, 40, 130, 50, ['sidestick', 'pilot demand'], ACS, AC, 13, bold_first=True))
    o.append(boxt(20, 210, 130, 64, ['sensors', 'gyros, accel.,', 'air data'], PANEL, AC, 13, bold_first=True))
    lanes = 'ABCD'
    for i, n in enumerate(lanes):
        y = 30 + i * 62
        o.append(boxt(220, y, 120, 44, [f'FCC lane {n}'], LVS if i < 3 else PANEL, LV, 13, bold_first=True))
        o.append(arrow(150, 65, 218, y + 22, AC, 1.6)); o.append(arrow(150, 242, 218, y + 22, MUT, 1.4, 'm'))
        o.append(arrow(340, y + 22, 398, 145, LV, 1.6, 'l'))
    o.append(boxt(400, 115, 110, 60, ['voter', 'middle value'], ACS, AC, 13, bold_first=True))
    o.append(boxt(570, 30, 130, 56, ['actuators', 'hydraulic or EHA'], PANEL, AC, 13, bold_first=True))
    o.append(boxt(570, 125, 130, 44, ['surfaces'], PANEL, AC, 13, bold_first=True))
    o.append(boxt(570, 210, 130, 56, ['aircraft', 'motion'], NXS, NX, 13, bold_first=True))
    o.append(P([(510, 145), (540, 145), (540, 58), (566, 58)], AC, 2)); o.append(arrow(556, 58, 568, 58))
    o.append(arrow(635, 86, 635, 123)); o.append(arrow(635, 169, 635, 208))
    o.append(P([(635, 266), (635, 296), (85, 296), (85, 278)], NX, 2, dash='6 4')); o.append(arrow(85, 284, 85, 276, NX, 2, 'x'))
    o.append(T(360, 314, 'motion feedback to the sensors', 13, 'middle', NX, True))
    # numbers
    rows = [('one lane', 'p = 1 × 10' + sup('−4') + ' per hour', MUT),
            ('triplex, all three fail', 'p³ = 1.0 × 10' + sup('−12'), INK),
            ('triplex, majority lost (2 of 3 fail)', '≈ 3p² = 3.0 × 10' + sup('−8') + '   misses 10' + sup('−9'), LV),
            ('quadruplex, majority lost (3 of 4)', '≈ 4p³ = 4.0 × 10' + sup('−12') + '   meets 10' + sup('−9'), AC)]
    for i, (a, b, c) in enumerate(rows):
        y = 350 + i * 24
        o.append(T(30, y, a, 13, 'start', INK, i > 1)); o.append(T(330, y, b, 13, 'start', c, True))
    return 434, ''.join(o)


FIG[5] = (f5, 'A quadruplex digital fly-by-wire chain: pilot demand and sensor signals go to four computer lanes, a voter passes the middle value to the '
              'actuators, and the aircraft’s motion returns through the sensors. The worked example’s numbers show why a fourth lane is added.',
          'Block diagram: sidestick and sensors each feed four flight control computer lanes A to D; the lanes feed a voter, which drives the actuators, '
          'the surfaces and the aircraft; a dashed path returns the motion to the sensors. Below, a table: one lane 1 times 10 to the minus 4; triplex all '
          'fail 1 times 10 to the minus 12; triplex majority lost 3 times 10 to the minus 8; quadruplex majority lost 4 times 10 to the minus 12.')


# ---- 1.6 outer heading loop around the inner roll loop, with both examples' numbers ----
def f6():
    o = []
    o.append(T(20, 22, 'outer loop: heading select', 14, 'start', NX, True))
    o.append(R(10, 32, 700, 232, 'none', NX, 10, 1.5, dash='6 4'))
    o.append(boxt(24, 60, 120, 56, ['selected 110°', 'now 070°'], ACS, AC, 13, bold_first=True))
    o.append(boxt(184, 60, 140, 56, ['bank command', '1.0 × 40° → 25°'], PANEL, AC, 13, bold_first=True))
    o.append(arrow(144, 88, 182, 88)); o.append(T(163, 80, 'e', 13, 'middle', MUT))
    # inner loop box
    o.append(R(344, 46, 356, 132, 'none', LV, 10, 1.5, dash='4 3'))
    o.append(T(352, 194, 'inner loop: roll', 14, 'start', LV, True))
    o.append(boxt(356, 64, 150, 64, ['roll law', 'δ' + sub('a') + ' = 3e − 0.8p', '12 − 1.6 = 10.4°'], LVS, LV, 13, bold_first=True))
    o.append(boxt(540, 64, 146, 48, ['aileron servo'], PANEL, AC, 13, bold_first=True))
    o.append(arrow(324, 88, 354, 88)); o.append(arrow(506, 88, 538, 88))
    o.append(boxt(540, 196, 146, 52, ['aircraft', 'turns at 2.18°/s'], NXS, NX, 13, bold_first=True))
    o.append(arrow(613, 112, 613, 194))
    o.append(P([(540, 220), (430, 220), (430, 130)], LV, 2)); o.append(arrow(430, 140, 430, 130, LV, 2, 'l'))
    o.append(T(446, 212, 'φ, p', 13, 'start', LV, True))
    o.append(P([(540, 240), (84, 240), (84, 118)], NX, 2)); o.append(arrow(84, 128, 84, 118, NX, 2, 'x'))
    o.append(T(100, 258, 'heading ψ', 13, 'start', NX))
    # auto-throttle row
    y = 300
    o.append(T(20, y - 12, 'auto-throttle: a separate speed loop on thrust', 14, 'start', AC, True))
    items = [('selected speed', ACS), ('auto-throttle', PANEL), ('thrust levers', PANEL), ('engine control', PANEL), ('thrust', NXS)]
    for i, (s, f) in enumerate(items):
        x = 20 + i * 140
        o.append(boxt(x, y, 120, 40, [s], f, AC, 13, bold_first=(i == 1)))
        if i: o.append(arrow(x - 20, y + 20, x - 2, y + 20))
    o.append(T(360, y + 66, 'turn rate = g tan φ ÷ V = 9.81 × 0.4663 ÷ 120 = 0.0381 rad/s = 2.18°/s', 13, 'middle', MUT))
    return 384, ''.join(o)


FIG[6] = (f6, 'The two worked examples as loops. Heading select turns a 40° heading error into a bank command limited to 25°; the inner roll law turns the '
              'bank error into aileron (10.4° in the first example); bank and rate feed back fast, heading slowly. The auto-throttle runs its own loop on thrust.',
          'Nested loop diagram. Outer dashed box: selected heading 110 and present heading 070 give an error to a bank command box, 1.0 times 40 degrees limited to 25. '
          'Inner box: roll law delta a equals 3 e minus 0.8 p, giving 12 minus 1.6 equals 10.4 degrees, then the aileron servo and the aircraft, turning at 2.18 degrees '
          'per second. Bank and roll rate feed back to the roll law, heading to the start. Below, a separate row: selected speed, auto-throttle, thrust levers, engine control, thrust.')


# ---- 1.7 a gust response with and without load alleviation: peaks 2.5 g and 2.0 g ----
def f7():
    o = []
    X0, X1, Y0, Y1 = 70, 470, 40, 300
    fx = lin(0, 5, X0, X1); fy = lin(0, 3, Y1, Y0)
    def resp(peak, zeta):
        w = 2 * math.pi * 1.0; wd = w * math.sqrt(1 - zeta ** 2)
        g = lambda t: math.exp(-zeta * w * t) * math.sin(wd * t)
        m = max(g(i / 1000) for i in range(1, 1500))
        return lambda t: 1.0 if t < 1 else 1.0 + (peak - 1.0) * g(t - 1) / m
    o.append(axes(X0, X1, Y0, Y1, [0, 1, 2, 3, 4, 5], [0, 1, 2, 3], fx, fy, 'time (s)', 'load factor n (g)'))
    o.append(L(fx(0), fy(1), fx(5), fy(1), MUT, 1.2, dash='3 4'))
    a, b = resp(2.5, 0.15), resp(2.0, 0.35)
    o.append(P([(fx(i / 100), fy(a(i / 100))) for i in range(0, 501)], LV, 2.5))
    o.append(P([(fx(i / 100), fy(b(i / 100))) for i in range(0, 501)], AC, 3))
    o.append(L(fx(1), fy(0.1), fx(1), fy(0.5), INK, 1.5)); o.append(T(fx(1) - 6, fy(0.25), 'gust at 1 s', 13, 'end', INK))
    # peaks
    tp_a = 1 + max(range(1, 1000), key=lambda i: a(1 + i / 1000)) / 1000
    tp_b = 1 + max(range(1, 1000), key=lambda i: b(1 + i / 1000)) / 1000
    o.append(C(fx(tp_a), fy(2.5), 5, LV)); o.append(C(fx(tp_b), fy(2.0), 5, AC))
    o.append(T(fx(tp_a) + 10, fy(2.5) - 4, 'no ACT: 2.5 g', 13, 'start', LV, True))
    o.append(L(fx(tp_b) + 6, fy(2.0), fx(1.52), fy(2.0), AC, 1.2)); o.append(T(fx(1.55), fy(2.0) + 4, 'with GLA: 2.0 g', 13, 'start', AC, True))
    o.append(T(fx(3.4), fy(0.3), 'steady 1 g', 13, 'middle', MUT))
    # numbers panel
    xs = 500
    o.append(T(xs, 70, 'ultimate = 1.5 × limit', 14, 'start', INK, True))
    o.append(T(xs, 100, 'no ACT: 1.5 × 2.5 = 3.75 g', 13, 'start', LV, True))
    o.append(T(xs, 120, 'GLA: 1.5 × 2.0 = 3.0 g', 13, 'start', AC, True))
    o.append(T(xs, 156, 'root bending, ultimate', 14, 'start', INK, True))
    o.append(T(xs, 186, '2.0 MN·m × 3.75 = 7.5 MN·m', 13, 'start', LV, True))
    o.append(T(xs, 206, '2.0 MN·m × 3.0 = 6.0 MN·m', 13, 'start', AC, True))
    o.append(T(xs, 242, 'design load cut', 14, 'start', INK, True))
    o.append(T(xs, 272, '0.75 ÷ 3.75 = 20 %', 13, 'start', INK, True))
    return 352, ''.join(o)


FIG[7] = (f7, 'Wing load factor after a gust at 1 s (computed damped responses, period 1 s). Without active control the peak is 2.5 g; with gust load '
              'alleviation it is 2.0 g and the ringing dies faster. Multiplying by 1.5 gives the ultimate design loads of the worked example.',
          'Plot of load factor against time from 0 to 5 seconds. Both curves sit at 1 g until a gust at 1 second; the curve without active control peaks at '
          '2.5 g and rings for several cycles, the curve with gust load alleviation peaks at 2.0 g and settles quickly. A side panel gives ultimate load factors '
          '3.75 and 3.0 g, root bending 7.5 and 6.0 meganewton-metres, and a 20 percent cut.')


# ---- 1.8 the FADEC loop and the corrected-speed numbers of the worked example ----
def f8():
    o = []
    o.append(boxt(20, 40, 130, 56, ['thrust lever', 'rating: take-off'], ACS, AC, 13, bold_first=True))
    o.append(R(190, 30, 150, 116, PANEL, LV, 8, 2))
    o.append(T(265, 54, 'FADEC', 14, 'middle', INK, True))
    o.append(boxt(202, 66, 126, 30, ['channel A: active'], LVS, LV, 13))
    o.append(boxt(202, 104, 126, 30, ['channel B: standby'], PANEL, L2, 13))
    o.append(arrow(150, 68, 188, 68))
    outs = ['fuel metering valve', 'variable stator vanes', 'bleed valves', 'ignition']
    for i, s in enumerate(outs):
        y = 30 + i * 32
        o.append(boxt(380, y, 170, 26, [s], PANEL, AC, 13))
        o.append(arrow(340, 88, 378, y + 13, AC, 1.5))
    o.append(boxt(590, 40, 110, 80, ['engine', 'fan N1,', 'core N2'], NXS, NX, 13, bold_first=True))
    for i in range(4): o.append(arrow(550, 43 + i * 32, 588, 80, MUT, 1.4, 'm'))
    o.append(P([(645, 120), (645, 172), (265, 172), (265, 148)], NX, 2, dash='6 4')); o.append(arrow(265, 156, 265, 148, NX, 2, 'x'))
    o.append(T(455, 192, 'sensors: N1, N2, EGT, fuel flow, P1, T1', 13, 'middle', NX, True))
    # bar chart of physical N1
    X0, X1, Y0, Y1 = 90, 690, 236, 400
    fy = lin(88, 104, Y1, Y0)
    o.append(L(X0, Y1, X1, Y1, L2, 1.5)); o.append(L(X0, Y0, X0, Y1, L2, 1.5))
    for v in (88, 92, 96, 100, 104):
        o.append(L(X0 - 5, fy(v), X0, fy(v), L2, 1.5)); o.append(T(X0 - 9, fy(v) + 4.5, str(v), 13, 'end', MUT))
    o.append(T(X0, Y0 - 12, 'physical N1 (%) for N1' + sub('c') + ' = 97.0 %', 14, 'start', MUT))
    o.append(L(X0, fy(100), X1, fy(100), LV, 2, dash='7 4')); o.append(T(X0 + 8, fy(100) - 6, 'N1 limit 100.0 %', 13, 'start', LV, True))
    bars = [('−10 °C', 92.7, '92.7 %', AC), ('15 °C', 97.0, '97.0 %', AC), ('40 °C', 100.0, '100.0 % (101.1 asked)', LV)]
    for i, (lab, v, txt, c) in enumerate(bars):
        x = 150 + i * 190
        o.append(R(x, fy(v), 80, Y1 - fy(v), ACS if c == AC else LVS, c, 0, 1.5))
        o.append(T(x + 40, Y1 + 20, lab, 13, 'middle', INK, True))
        o.append(T(x + 40, fy(101.1 if v == 100.0 else v) - 8, txt, 13, 'middle', c, True))
    o.append(R(150 + 2 * 190, fy(101.1), 80, fy(100) - fy(101.1), 'none', LV, 0, 1.5, dash='4 3'))
    return 432, ''.join(o)


FIG[8] = (f8, 'The FADEC loop, and the worked example’s take-off rating held as corrected fan speed 97.0 %. The physical N1 needed is 92.7 % at −10 °C and '
              '97.0 % at 15 °C; at 40 °C the schedule asks for 101.1 %, so the FADEC holds the 100.0 % limit and thrust falls.',
          'Top: block diagram from the thrust lever to a FADEC with an active channel A and a standby channel B, outputs to the fuel metering valve, variable '
          'stator vanes, bleed valves and ignition, the engine, and a dashed sensor path back to the FADEC. Bottom: bar chart of physical N1 for three inlet '
          'temperatures: 92.7 percent at minus 10 degrees, 97.0 at 15, and 100.0 at 40, where 101.1 was asked, under a dashed 100 percent limit line.')

spec = make_spec(FIG)
