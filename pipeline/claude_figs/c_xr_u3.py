"""Claude's hand-drawn figures for c-xr-u3 (AR/VR, unit 3: output devices, visual, audio and haptic), one per chapter,
from each chapter's worked example, plus the sentences in the chapter text that describe a figure (text_fixes)."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {}


# ---- 3.1 fitting the lab set into the budget ----
def f1():
    x0, x1 = 40, 600
    s = (x1 - x0) / 6.5  # lakh rupees
    X = lambda v: x0 + v * s
    o = [T(40, 28, 'Fitting the lab into ₹5,00,000 (bars in lakh rupees)', 15, 'start', bold=True)]
    y = 60
    o.append(R(X(0), y, 5 * s, 44, 'none', INK, 4, 2.5))
    o.append(R(X(0) + 3, y + 6, 1.5 * s - 3, 32, ACS, AC, 4)); o.append(T(X(0.75), y + 27, 'monitor 1.5', 13))
    o.append(R(X(1.5) + 3, y + 6, 3 * s - 3, 32, ACS, AC, 4)); o.append(T(X(3), y + 27, 'head display 3.0', 13))
    o.append(T(X(5) + 8, y + 27, '₹50,000 left', 13, 'start', MUT))
    o.append(T(X(5), y - 8, 'budget 5.0', 13, 'middle', INK, True))
    y = 140
    o.append(R(X(0), y, 5 * s, 44, 'none', INK, 4, 2.5))
    o.append(R(X(0) + 3, y + 6, 4.5 * s - 3, 32, PANEL, L2, 4)); o.append(T(X(2.25), y + 27, 'monitor + head display 4.5', 13))
    o.append(R(X(4.5) + 3, y + 6, 2 * s - 3, 32, NXS, NX, 4)); o.append(T(X(5.5), y + 27, '+ arm 2.0', 13))
    o.append(L(X(5), y - 6, X(5), y + 54, NX, 2.5, '5 4'))
    o.append(T(X(6.5) + 8, y + 18, '6.5: 1.5', 13, 'start', NX, True)); o.append(T(X(6.5) + 8, y + 36, 'over', 13, 'start', NX, True))
    o.append(T(40, 236, 'CAVE ₹40,00,000 = 8 budgets:', 14, 'start', bold=True))
    for i in range(8):
        o.append(R(270 + i * 50, 220, 44, 22, NXS if i else ACS, NX if i else AC, 3))
    o.append(T(40, 286, 'Buy: stereo monitor (desk stereo, need b) + head display (head motion, part of c).', 14, 'start'))
    o.append(T(40, 310, 'Defer: the force arm (₹1,50,000 over) and group viewing for six (only the CAVE does it).', 14, 'start'))
    return 328, ''.join(o)
FIG[1] = (f1, 'The monitor and head display together cost ₹4,50,000 and fit the ₹5,00,000 budget with ₹50,000 left. Adding the force arm overshoots by ₹1,50,000, and the CAVE alone costs eight budgets, so both are deferred.',
          'Two budget bars of five lakh rupees: one holding the monitor and head display with half a lakh left, one where adding the arm runs 1.5 lakh past the line; below, eight budget-sized blocks for the CAVE.')


# ---- 3.2 crossed and uncrossed disparity ----
def f2():
    o = []
    def panel(ox, Z, title, crossed):
        r = [T(ox + 160, 26, title, 15, bold=True)]
        ye, ys = 380, 380 - 200 * 0.8  # 0.8 px per cm along depth
        yo = 380 - Z * 0.8
        ex = 50  # half eye separation drawn (exaggerated)
        cx = ox + 160
        r.append(L(ox + 20, ys, ox + 300, ys, L2, 4)); r.append(T(ox + 300, ys - 8, 'screen, 2 m', 13, 'end', MUT))
        for sx in (-1, 1):
            r.append(C(cx + sx * ex, ye, 9, INK))
        r.append(T(cx - ex, ye + 26, 'L eye', 13)); r.append(T(cx + ex, ye + 26, 'R eye', 13))
        r.append(C(cx, yo, 8, NX)); r.append(T(cx + 14, yo + 5, f'object {Z // 100} m', 13, 'start', NX, True))
        k = 1 - 200 / Z  # screen hit for eye at x=e: x = e + (0 - e) * (200 / Z) -> e*(1 - 200/Z)
        for sx, c in ((-1, AC), (1, LV)):
            hx = cx + sx * ex * k
            r.append(L(cx + sx * ex, ye, hx if crossed else cx, ys if crossed else yo, c, 2))
            r.append(C(hx, ys, 6, c))
            r.append(T(hx, ys + (24 if crossed else -12), 'L img' if sx < 0 else 'R img', 13, fill=c, bold=True))
        return ''.join(r)
    o.append(panel(20, 100, '(a) object at 1 m', True))
    o.append(panel(380, 400, '(b) object at 4 m', False))
    o.append(T(180, 440, 's = 6.5 × (200/100 − 1) = +6.5 cm, crossed', 14))
    o.append(T(540, 440, 's = 6.5 × (200/400 − 1) = −3.25 cm, uncrossed', 14))
    return 456, ''.join(o)
FIG[2] = (f2, 'Seen from above, with the eye gap exaggerated: for an object at 1 m, in front of the 2 m screen, the lines of sight cross before the screen and the images swap sides (+6.5 cm). For an object at 4 m they meet behind it and the images keep their order (−3.25 cm).',
          'Two top views of two eyes, a screen at 2 m and an object. In the first the object is at 1 m and the sight lines cross before the screen; in the second it is at 4 m and the sight lines reach the screen before meeting.')


# ---- 3.3 HMD lens: virtual image ----
def f3():
    ya = 220
    sc = 26
    lx = 620
    X = lambda cm: lx + cm * sc
    o = [T(40, 28, 'Head-mounted display lens: f = 5 cm, panel 4 cm behind it', 15, 'start', bold=True)]
    o.append(L(40, ya, 700, ya, L2, 1.5))
    o.append(f'<ellipse cx="{lx}" cy="{ya}" rx="9" ry="120" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:2"/>')
    o.append(T(lx, ya - 128, 'lens', 13, fill=AC))
    ph, ih = 22, 110
    o.append(L(X(-4), ya, X(-4), ya - ph, INK, 3, arrow='m')); o.append(T(X(-4), ya + 22, 'panel', 13)); o.append(T(X(-4), ya + 40, 'u = −4 cm', 13, fill=MUT))
    o.append(L(X(-20), ya, X(-20), ya - ih, NX, 3, '6 4', arrow='x')); o.append(T(X(-20), ya + 22, 'virtual image', 13, fill=NX, bold=True)); o.append(T(X(-20), ya + 40, 'v = −20 cm', 13, fill=MUT))
    # ray 1: parallel then through F on the right (beyond picture: slope)
    o.append(L(X(-4), ya - ph, lx, ya - ph, AC, 2))
    sl = ph / (5 * sc)
    o.append(L(lx, ya - ph, 700, ya - ph + sl * (700 - lx), AC, 2))
    o.append(L(lx, ya - ph, X(-20), ya - ph - sl * (lx - X(-20)), AC, 1.5, '4 4'))
    # ray 2: through the centre
    sl2 = ph / (4 * sc)
    o.append(L(X(-4), ya - ph, 700, ya - ph + sl2 * (700 - X(-4)), LV, 2))
    o.append(L(X(-4), ya - ph, X(-20), ya - ph - sl2 * (X(-4) - X(-20)), LV, 1.5, '4 4'))
    o.append(C(X(5) if X(5) < 700 else 700, ya, 0.1))
    o.append(T(660, ya + 22, 'eye', 13, bold=True))
    o.append(L(X(-20), ya + 56, lx, ya + 56, INK, 1.5)); o.append(T((X(-20) + lx) / 2, ya + 74, '20 cm', 13))
    o += [T(40, 330, '1/v = 1/5 + 1/(−4) = −0.05, so v = −20 cm: virtual, same side as the panel', 14, 'start'),
          T(40, 354, 'm = v/u = (−20)/(−4) = 5: a 10 μm pixel looks 50 μm wide at 20 cm', 14, 'start'),
          T(40, 378, 'angle = 50 × 10⁻⁶ ÷ 0.20 = 2.5 × 10⁻⁴ rad ≈ 0.86 arcmin, just under the eye\'s 1 arcmin', 14, 'start')]
    return 396, ''.join(o)
FIG[3] = (f3, 'Rays from the panel 4 cm behind the lens spread out after it, so the eye traces them back to an upright virtual image 20 cm away and 5 times larger. One 10 μm pixel then subtends about 0.86 arcmin.',
          'An optical axis with a lens, a small panel arrow 4 cm to its left and a dashed virtual image arrow 20 cm to its left, five times taller; two rays leave the panel, bend at the lens and their dashed extensions meet at the image top.')


# ---- 3.4 shutter glasses timing ----
def f4():
    x0, x1 = 150, 690
    s = (x1 - x0) / 33.33
    X = lambda v: x0 + v * s
    o = [T(40, 28, '120 Hz panel with shutter glasses', 15, 'start', bold=True)]
    slots = ['L1', 'R1', 'L2', 'R2']
    rows = [(46, 'screen'), (96, 'left shutter'), (146, 'right shutter')]
    for y, lab in rows: o.append(T(x0 - 12, y + 22, lab, 14, 'end', bold=True))
    for i, sl in enumerate(slots):
        a = i * 8.33
        left = sl[0] == 'L'
        o.append(R(X(a), 46, 8.33 * s, 34, ACS if left else LVS, AC if left else LV, 3)); o.append(T(X(a + 4.17), 68, sl, 14, bold=True))
        o.append(R(X(a), 96 if left else 146, 8.33 * s, 34, ACS if left else LVS, AC if left else LV, 3))
        o.append(T(X(a + 4.17), (96 if left else 146) + 22, 'open', 13))
        o.append(R(X(a), 146 if left else 96, 8.33 * s, 34, 'var(--line)', L2, 3)); o.append(T(X(a + 4.17), (146 if left else 96) + 22, 'dark', 13, fill=MUT))
    o.append(xaxis(x0, x1, 190, [0, 8.33, 16.67, 25, 33.33], X, 'ms'))
    o.append(brace(X(0), X(16.67), 250, AC, up=True)); o.append(T(X(8.33), 270, 'left eye: a new frame every 16.67 ms = 60 per second', 13, fill=AC, bold=True))
    o.append(T(40, 310, 'Each slot = 1/120 s = 8.33 ms. Each eye gets 120 ÷ 2 = 60 frames per second.', 14, 'start'))
    o.append(T(40, 334, 'At 60 Hz: slots of 16.67 ms and only 30 frames per eye → visible flicker, more ghosting.', 14, 'start', NX))
    return 350, ''.join(o)
FIG[4] = (f4, 'On a 120 Hz panel the left and right frames take turns in 8.33 ms slots, and only the matching shutter is open. Each eye sees a new frame every 16.67 ms, which is 60 frames per second.',
          'A timeline of four 8.33 millisecond slots, L1, R1, L2, R2, with rows for the left and right shutters showing open only during their own frames, and a bracket of 16.67 ms between two left frames.')


# ---- 3.5 interaural time difference ----
def f5():
    cx, cy, r = 190, 230, 70
    o = [T(40, 28, 'A click 30° to the right reaches the right ear first', 15, 'start', bold=True)]
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" style="fill:var(--panel);stroke:var(--ink);stroke-width:2"/>')
    o.append(P([(cx - 10, cy - r + 2), (cx, cy - r - 14), (cx + 10, cy - r + 2)], INK, 2))
    o.append(T(cx, cy + 6, 'head', 13, fill=MUT))
    le, re = (cx - r, cy), (cx + r, cy)
    o.append(C(*le, 7, NX)); o.append(C(*re, 7, AC))
    o.append(T(le[0] - 10, le[1] + 24, 'left ear', 13, 'end', NX)); o.append(T(re[0] + 12, re[1] - 12, 'right ear', 13, 'start', AC))
    th = math.radians(30)
    ux, uy = math.sin(th), -math.cos(th)  # direction towards the source
    o.append(L(cx, cy, cx + 160 * ux, cy + 160 * uy, L2, 1.5, '5 4'))
    o.append(L(cx, cy, cx, cy - 160, L2, 1.5, '3 4'))
    o.append(T(cx + 18, cy - 118, '30°', 13))
    sx, sy = cx + 175 * ux, cy + 175 * uy
    o.append(C(sx, sy, 8, AC)); o.append(T(sx + 12, sy + 4, 'click', 13, 'start', AC, True))
    # wavefront through the right ear, perpendicular to u
    px, py = -uy, ux
    o.append(L(re[0] - 190 * px, re[1] - 190 * py, re[0] + 40 * px, re[1] + 40 * py, AC, 2, '8 5'))
    # extra path from left ear along u to the wavefront: length = 2r sin(30)
    d = 2 * r * math.sin(th)
    o.append(L(le[0], le[1], le[0] + d * ux, le[1] + d * uy, NX, 3))
    o.append(Tb(le[0] - 12, le[1] - 44, 'extra path', 13, 'end', NX))
    o.append(Tb(le[0] - 12, le[1] - 26, '0.175 × sin 30°', 13, 'end', NX))
    o.append(Tb(le[0] - 12, le[1] - 8, '= 0.0875 m', 13, 'end', NX))
    # right: arrival times
    x0, x1 = 420, 690
    tsc = (x1 - x0) / 0.4
    o.append(T(x0, 90, 'arrival time (ms)', 13, 'start', MUT))
    for y, lab, t, c in [(140, 'right ear', 0, AC), (210, 'left ear', 0.255, NX)]:
        o.append(L(x0, y, x1, y, L2, 1.5)); o.append(T(x0 + 12, y - 26, lab, 14, 'start', c, True))
        o.append(L(x0 + t * tsc, y, x0 + t * tsc, y - 40, c, 4))
    o.append(L(x0, 222, x0 + 0.255 * tsc, 222, NX, 2, arrow='x')); o.append(T(x0 + 0.255 * tsc + 8, 227, '0.255 ms', 13, 'start', NX, True))
    o.append(xaxis(x0, x1, 250, [0, 0.1, 0.2, 0.3, 0.4], lambda v: x0 + v * tsc))
    o += [T(x0, 320, 'ITD = 0.0875 ÷ 343', 14, 'start'), T(x0, 342, '= 0.255 ms', 14, 'start'),
          T(x0, 364, '× 44,100 Hz = 11.25 ≈ 11 samples', 14, 'start', bold=True)]
    return 384, ''.join(o)
FIG[5] = (f5, 'Seen from above, the click 30° to the right must travel an extra 0.0875 m to reach the left ear, so the left ear hears it 0.255 ms later: about 11 samples at 44.1 kHz.',
          'Top view of a head with a click 30 degrees to the right, a dashed wavefront touching the right ear and the extra path to the left ear marked; beside it two time lines with the left-ear arrival 0.255 ms after the right.')


# ---- 3.6 wall force with motor saturation ----
def f6():
    x0, x1, y0, y1 = 80, 500, 50, 320
    fx = lambda mm: x0 + mm / 3.2 * (x1 - x0)
    fy = lambda n: y1 - n / 5 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [0, 1, 2, 2.2, 3], [0, 1, 2, 3, 4, 5], fx, fy, 'penetration into the wall (mm)', 'force (N)')]
    o.append(P([(fx(0), fy(0)), (fx(3.2), fy(4.8))], L2, 2, '6 5'))
    o.append(T(fx(3.15), fy(4.72) - 8, 'wall asks F = 1500 x', 13, 'end', MUT))
    o.append(P([(fx(0), fy(0)), (fx(2.2), fy(3.3)), (fx(3.2), fy(3.3))], AC, 3.5))
    o.append(C(fx(2), fy(3), 6, AC)); o.append(Tb(fx(2) - 10, fy(3) + 4, '2 mm → 3.0 N', 14, 'end', AC))
    o.append(C(fx(2.2), fy(3.3), 6, NX)); o.append(Tb(fx(2.2) + 4, fy(3.3) + 24, 'saturates at 2.2 mm', 13, 'start', NX))
    o.append(C(fx(3), fy(4.5), 5, L2)); o.append(L(fx(3), fy(4.5) + 6, fx(3), fy(3.3) - 6, NX, 1.5, arrow='x'))
    o.append(T(fx(3) - 8, fy(3.95), '4.5 → 3.3', 13, 'end', NX))
    o += [T(530, 90, 'k = 1500 N/m', 14, 'start', bold=True), T(530, 114, 'motors max 3.3 N', 14, 'start', bold=True),
          T(530, 160, 'F = 1500 × 0.002', 14, 'start'), T(530, 182, '= 3.0 N (fits)', 14, 'start'),
          T(530, 226, 'x_sat = 3.3 ÷ 1500', 14, 'start'), T(530, 248, '= 0.0022 m = 2.2 mm', 14, 'start'),
          T(530, 290, 'deeper: force stays', 13, 'start', NX), T(530, 308, '3.3 N, wall feels soft', 13, 'start', NX)]
    return 380, ''.join(o)
FIG[6] = (f6, 'The pen gives the force the virtual spring asks for, 3.0 N at 2 mm, until the motors reach 3.3 N at 2.2 mm. Deeper than that the force stays flat, so at 3 mm the user feels 3.3 N instead of 4.5 N and the wall feels soft.',
          'A graph of force against penetration: a dashed line of slope 1500 newtons per metre and a solid line that follows it to 3.3 N at 2.2 mm and then stays flat, with the 2 mm, 3.0 N point marked.')


# ---- 3.7 pin arrays at two pitches ----
def f7():
    o = [T(40, 28, 'The same 10 mm × 10 mm patch at two pin pitches', 15, 'start', bold=True)]
    sz = 220
    for ox, p, lab, c, fi in [(60, 2, 'fingertip, 2 mm pitch', AC, ACS), (400, 5, 'palm, 5 mm pitch', NX, NXS)]:
        oy = 70
        o.append(R(ox, oy, sz, sz, 'var(--panel)', L2, 4, 1.5))
        n = 10 // p + 1
        for i in range(n):
            for j in range(n):
                o.append(C(ox + i * p / 10 * sz, oy + j * p / 10 * sz, 7, c))
        for i in range(n):
            o.append(T(ox + i * p / 10 * sz, oy + sz + 24, str(i * p), 13, fill=MUT))
        o.append(T(ox + sz / 2, oy + sz + 44, 'mm along one side', 13, fill=MUT))
        o.append(T(ox + sz / 2, oy + sz + 74, lab, 14, bold=True))
        o.append(T(ox + sz / 2, oy + sz + 96, f'10 ÷ {p} = {10 // p} gaps → {n} pins per side → {n} × {n} = {n * n}', 14))
    o.append(T(360, 418, '36 ÷ 9 = 4 times fewer pins on the palm patch', 14, bold=True))
    return 434, ''.join(o)
FIG[7] = (f7, 'Along each 10 mm side there is one more pin than there are gaps: 6 pins at 2 mm pitch give 36 in the square, 3 pins at 5 mm give 9, four times fewer.',
          'Two 10 millimetre squares of pins: a six by six grid at 2 mm pitch for the fingertip and a three by three grid at 5 mm pitch for the palm, with the positions 0 to 10 marked under each.')


# ---- 3.8 minimum damping against loop period ----
def f8():
    x0, x1, y0, y1 = 80, 480, 50, 320
    fx = lambda t: x0 + t / 12 * (x1 - x0)
    fy = lambda b: y1 - b / 12 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [0, 1, 2, 4, 6, 8, 10, 12], [0, 2, 4, 6, 8, 10, 12], fx, fy, 'loop period T (ms)', 'damping b (N·s/m)')]
    o.append(f'<polygon points="{fx(0)},{fy(0)} {fx(12)},{fy(12)} {fx(0)},{fy(12)}" style="fill:var(--accent-soft);stroke:none"/>')
    o.append(P([(fx(0), fy(0)), (fx(12), fy(12))], AC, 3))
    o.append(T(fx(2.5), fy(9), 'stable: b above kT/2', 14, 'start', AC, True))
    o.append(T(fx(7), fy(2.5), 'buzzes', 14, 'start', NX, True))
    for t, lab in [(1, '1 ms → b > 1'), (10, '10 ms → b > 10')]:
        o.append(C(fx(t), fy(t), 6, NX))
        o.append(Tb(fx(t) + 10, fy(t) + 20, lab, 13, 'start', NX))
    o += [T(510, 90, 'wall k = 2000 N/m', 14, 'start', bold=True),
          T(510, 130, 'T = 0.001 s:', 14, 'start'), T(510, 152, '2000 × 0.001 ÷ 2 = 1', 14, 'start'),
          T(510, 192, 'T = 0.01 s:', 14, 'start'), T(510, 214, '2000 × 0.01 ÷ 2 = 10', 14, 'start'),
          T(510, 258, '10 times the damping:', 13, 'start', MUT), T(510, 276, 'the wall feels like treacle,', 13, 'start', MUT),
          T(510, 294, 'so haptics runs at 1 kHz', 13, 'start', MUT)]
    return 372, ''.join(o)
FIG[8] = (f8, 'For a wall of stiffness 2000 N/m the damping must lie above the line b = kT/2. A 1 ms loop needs more than 1 N·s/m; a 10 ms loop needs more than 10, which makes the wall feel thick.',
          'A graph of minimum damping against loop period: a straight line from the origin with the region above it shaded as stable, and points at 1 ms and 10 ms marked.')


TEXT = {
    4: [('One slot lasts t = 1/120 s = 0.008333 s = 8.33 ms; the figure rounds this to 8 ms and 9 ms across four slots.',
         'One slot lasts t = 1/120 s = 0.008333 s = 8.33 ms.')],
    3: [('the viewer must accept larger pixels per degree, or use a denser panel',
         'the viewer must accept larger pixels, meaning fewer pixels per degree, or use a denser panel')],
    8: [('Uses: surgical trainers, simulators, remote robot arms. Only a few universities teach this chapter.',
         'Uses: surgical trainers, simulators, remote robot arms.')],
}


def text_fixes(k):
    return TEXT.get(k, [])


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d
