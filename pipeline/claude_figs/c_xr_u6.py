"""Claude's hand-drawn figures for c-xr-u6 (AR/VR, unit 6: augmented reality and the metaverse), one per chapter,
from each chapter's worked example, plus the sentences in the chapter text that describe a figure (text_fixes)."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {1: 3}


def lane(o, x0, y, sc, bars, h=40):
    """a row of timeline bars: (label, start, end, fill, stroke)"""
    for lab, a, b, fi, st in bars:
        o.append(R(x0 + a * sc, y, (b - a) * sc, h, fi, st, 4))
        if lab:
            o.append(T(x0 + (a + b) / 2 * sc, y + h / 2 + 5, lab, 13, 'middle', INK, True))


# ---- 6.1 overlay slip against tracker delay ----
def f1():
    x0, x1, y0, y1 = 80, 420, 60, 300
    fx = lambda t: x0 + t / 60 * (x1 - x0)
    fy = lambda s: y1 - s / 30 * (y1 - y0)
    o = [T(40, 28, 'Slip at 2 m for a 120°/s head turn', 15, 'start', bold=True)]
    o.append(axes(x0, x1, y0, y1, [0, 10, 20, 30, 40, 50, 60], [0, 10, 20, 30], fx, fy,
                  'tracker delay (ms)', 'slip (cm)'))
    pts = [(fx(t), fy(200 * math.tan(math.radians(120 * t / 1000)))) for t in range(0, 61)]
    o.append(P(pts, AC, 3))
    o.append(L(fx(50), fy(21.0), fx(50), y1, MUT, 1.5, '4 4'))
    o.append(L(x0, fy(21.0), fx(50), fy(21.0), MUT, 1.5, '4 4'))
    o.append(C(fx(50), fy(21.0), 7, NX)); o.append(Tb(fx(50) - 12, fy(21.0) - 14, '50 ms → 21.0 cm', 14, 'end', NX, True))
    o.append(C(fx(1.19), fy(0.5), 7, LV))
    o.append(L(fx(1.19) + 8, fy(0.5) - 6, fx(8), fy(8), LV, 1.5))
    o.append(Tb(fx(8) + 4, fy(8) - 6, '1.19 ms → 0.5 cm (5 mm)', 14, 'start', LV, True))
    # geometry sketch on the right
    ex, ey, d = 474, 220, 150
    o.append(T(470, 70, 'One 50 ms update', 15, 'start', bold=True))
    o.append(C(ex, ey, 9, INK)); o.append(T(ex, ey + 28, 'eye', 13, fill=MUT))
    a = math.radians(6.0) * 4  # drawn wider so the angle can be read
    o.append(L(ex, ey, ex + d, ey, AC, 2.5))
    o.append(L(ex, ey, ex + d, ey - d * math.tan(a), NX, 2.5, '6 4'))
    o.append(C(ex + d, ey, 7, AC)); o.append(T(ex + d + 10, ey + 5, 'real point', 13, 'start', AC, True))
    o.append(C(ex + d, ey - d * math.tan(a), 7, NX)); o.append(T(ex + d + 10, ey - d * math.tan(a) + 5, 'overlay', 13, 'start', NX, True))
    o.append(L(ex + d, ey - 8, ex + d, ey - d * math.tan(a) + 8, INK, 1.5))
    o.append(T(ex + d - 8, ey - d * math.tan(a) / 2 + 5, 's', 14, 'end', INK, True))
    o.append(T(ex + 60, ey - 7, '6.0°', 13, 'start'))
    o.append(T(ex + d / 2, ey + 28, 'd = 2 m', 14, 'middle', AC))
    o.append(T(470, 290, 'Δθ = 120°/s × 0.050 s = 6.0°', 13, 'start'))
    o.append(T(470, 312, 's = 2 × tan 6° = 0.210 m', 13, 'start'))
    o.append(T(40, 360, 'Slip grows almost in a straight line with delay; 5 mm needs 1.19 ms, so the pose is predicted.', 13, 'start', MUT))
    return 376, ''.join(o)
FIG[1] = (f1, 'Overlay slip at a 2 m viewing distance against tracker delay, for a head turning at 120°/s. A 50 ms update turns the head 6.0° and the overlay slips 21.0 cm; holding slip to 5 mm allows only 1.19 ms, shorter than a normal tracker, so the pose must be predicted.',
          'A curve of slip in centimetres rising almost linearly with tracker delay from 0 to 60 milliseconds, with points at 50 ms and 21.0 cm and at 1.19 ms and 0.5 cm; beside it an eye, a real point 2 m away and the overlay drawn 6 degrees off it.')


# ---- 6.2 video against optical delay ----
def f2():
    x0, sc = 150, 7.2
    o = [T(40, 28, 'Delay from head motion to the shown frame (ms)', 15, 'start', bold=True)]
    o.append(T(x0 - 12, 86, 'video', 14, 'end', INK, True)); o.append(T(x0 - 12, 104, 'see-through', 13, 'end', MUT))
    lane(o, x0, 70, sc, [('capture 33', 0, 33, NXS, NX), ('pose 20', 33, 53, ACS, AC), ('show 15', 53, 68, PANEL, L2)])
    o.append(T(x0 + 68 * sc + 8, 95, '68', 14, 'start', INK, True))
    o.append(T(x0 - 12, 166, 'optical', 14, 'end', INK, True)); o.append(T(x0 - 12, 184, 'see-through', 13, 'end', MUT))
    lane(o, x0, 150, sc, [('track + show 20', 0, 20, ACS, AC)])
    o.append(T(x0 + 20 * sc + 8, 175, '20', 14, 'start', INK, True))
    o.append(brace(x0, x0 + 33 * sc, 124, NX, up=False))
    o.append(T(x0 + 16.5 * sc, 144, 'the extra capture the optical path never pays', 13, 'middle', NX))
    o.append(xaxis(x0, x0 + 70 * sc, 212, [0, 10, 20, 30, 40, 50, 60, 70], lambda v: x0 + v * sc))
    rows = [('video', '60°/s × 0.068 s = 4.08°', '1.5 × tan 4.08° = 10.7 cm', NX),
            ('optical', '60°/s × 0.020 s = 1.20°', '1.5 × tan 1.20° = 3.1 cm', AC)]
    o.append(T(150, 268, 'angle', 14, 'start', MUT, True)); o.append(T(420, 268, 'shift at 1.5 m', 14, 'start', MUT, True))
    for i, (n, a, s, c) in enumerate(rows):
        y = 296 + i * 28
        o.append(T(138, y, n, 14, 'end', c, True)); o.append(T(150, y, a, 14, 'start')); o.append(T(420, y, s, 14, 'start'))
    o.append(T(40, 372, 'Ratio 68 ÷ 20 = 3.4: the video view slips 3.4 times as far.', 14, 'start', bold=True))
    return 388, ''.join(o)
FIG[2] = (f2, 'The camera capture, the first bar of the top lane, is the extra 33 ms the optical path never pays. The bars end at 68 ms and 20 ms, so at a 60°/s head turn the video view misregisters 4.08° (10.7 cm at 1.5 m) against 1.20° (3.1 cm), 3.4 times worse.',
          'Two timelines: video see-through with capture 33, pose 20 and show 15 milliseconds ending at 68, and optical see-through with one 20 millisecond bar; below, the angles 4.08 and 1.20 degrees and shifts 10.7 and 3.1 centimetres.')


# ---- 6.3 marker distance from its width in pixels ----
def f3():
    x0, x1, y0, y1 = 80, 460, 60, 300
    fx = lambda w: x0 + (w - 100) / 400 * (x1 - x0)
    fy = lambda z: y1 - z / 0.7 * (y1 - y0)
    o = [T(40, 28, 'Z = f × W ÷ w = 800 × 0.08 ÷ w = 64 ÷ w', 15, 'start', bold=True)]
    o.append(axes(x0, x1, y0, y1, [100, 200, 300, 400, 500], [0, 0.2, 0.4, 0.6], fx, fy,
                  'marker width w on the image (px)', 'distance Z (m)', yfmt=lambda v: f'{v:.1f}'))
    o.append(P([(fx(w), fy(64 / w)) for w in range(100, 501, 5)], AC, 3))
    for w, z, err, c, dx in [(160, 0.4, '±2.5 mm', NX, 14), (320, 0.2, '±0.625 mm', LV, 14)]:
        o.append(L(fx(w), fy(z), fx(w), y1, MUT, 1.5, '4 4')); o.append(L(x0, fy(z), fx(w), fy(z), MUT, 1.5, '4 4'))
        o.append(C(fx(w), fy(z), 7, c))
        o.append(Tb(fx(w) + dx, fy(z) - 12, f'{w} px → {z} m, {err}', 14, 'start', c, True))
    bx = 500
    o.append(T(bx, 70, 'depth error', 15, 'start', bold=True))
    o.append(T(bx, 96, 'ΔZ = Z × (1 px ÷ w)', 14, 'start'))
    o.append(T(bx, 130, '160 px:', 14, 'start', NX, True)); o.append(T(bx, 150, '0.4 × 1/160 = 2.5 mm', 13, 'start'))
    o.append(T(bx, 184, '320 px:', 14, 'start', LV, True)); o.append(T(bx, 204, '0.2 × 1/320 = 0.625 mm', 13, 'start'))
    o.append(T(bx, 244, 'twice the pixels,', 14, 'start', INK, True)); o.append(T(bx, 264, 'a quarter of the error', 14, 'start', INK, True))
    return 360, ''.join(o)
FIG[3] = (f3, 'The curve is Z = f × W ÷ w with f = 800 px and W = 0.08 m, so Z = 64 ÷ w. Both worked markers sit on it: 160 px gives 0.4 m and 2.5 mm depth error, 320 px gives 0.2 m and 0.625 mm, so twice the pixels gives a quarter of the error.',
          'A falling curve of distance against marker width in pixels from 100 to 500, with points at 160 pixels and 0.4 metres and at 320 pixels and 0.2 metres, and a panel working the depth errors 2.5 and 0.625 millimetres.')


# ---- 6.4 one frame against the 16.67 ms budget ----
def f4():
    x0, sc = 170, 24
    o = [T(40, 28, 'One frame at 60 fps (ms)', 15, 'start', bold=True)]
    bx = x0 + 16.67 * sc
    o.append(L(bx, 50, bx, 290, LV, 2, '6 4')); o.append(Tb(bx, 46, 'budget 1000 ÷ 60 = 16.67', 13, 'middle', LV, True))
    rows = [('normal', [6.0, 8.0, 1.5], '15.5 fits'), ('dark corridor', [9.0, 8.0, 1.5], '18.5 late'), ('fix: render 6.17', [9.0, 6.17, 1.5], '16.67 fits')]
    for i, (name, (tr, rd, ap), tot) in enumerate(rows):
        y = 64 + i * 76
        o.append(T(x0 - 12, y + 26, name, 14, 'end', INK, True))
        lane(o, x0, y, sc, [(f'track {tr:g}', 0, tr, LVS if tr > 6 else ACS, LV if tr > 6 else AC),
                            (f'render {rd:g}', tr, tr + rd, NXS if rd < 8 else PANEL, NX if rd < 8 else L2),
                            ('app', tr + rd, tr + rd + ap, PANEL, MUT)])
        end = tr + rd + ap
        late = end > 16.7
        o.append(T(x0 + max(end, 17.0) * sc + 8, y + 26, tot, 14, 'start', LV if late else NX, True))
    o.append(xaxis(x0, x0 + 20 * sc, 298, [0, 4, 8, 12, 16, 20], lambda v: x0 + v * sc))
    o.append(T(40, 352, 'Normal headroom 16.67 − 15.5 = 1.17 ms. Dark: 1000 ÷ 18.5 = 54.05 fps.', 14, 'start'))
    o.append(T(40, 376, 'Render must fall to 16.67 − 9.0 − 1.5 = 6.17 ms, a cut of 1.83 ms.', 14, 'start', bold=True))
    return 392, ''.join(o)
FIG[4] = (f4, 'Each row is one frame timeline in milliseconds: a tracking bar, a rendering bar and a narrow 1.5 ms app slice. The normal frame fits the 16.67 ms budget at 15.5 ms, the dark corridor pushes tracking to 9.0 ms and the frame to 18.5 ms, and rendering must fall to 6.17 ms to get back to 60 frames per second.',
          'Three frame timelines against a dashed budget line at 16.67 milliseconds: tracking 6, rendering 8 and app 1.5 ending at 15.5; tracking 9 ending at 18.5 past the line; and rendering cut to 6.17 ending on the line.')


# ---- 6.5 the confusion matrix ----
def f5():
    o = [T(40, 28, '100 trials: rows are what the user did, columns what the system called', 15, 'start', bold=True)]
    gx, gy, cw, ch = 190, 90, 120, 60
    for j, h in enumerate(['called pinch', 'called grab', 'missed']):
        o.append(T(gx + j * cw + cw / 2, gy - 12, h, 14, 'middle', INK, True))
    data = [('did pinch', [46, 3, 1]), ('did grab', [4, 45, 1])]
    for i, (rname, vals) in enumerate(data):
        y = gy + i * ch
        o.append(T(gx - 14, y + ch / 2 + 5, rname, 14, 'end', INK, True))
        for j, v in enumerate(vals):
            ok = (i == j)
            o.append(R(gx + j * cw, y, cw, ch, ACS if ok else LVS, AC if ok else LV, 0))
            o.append(T(gx + j * cw + cw / 2, y + ch / 2 + 7, str(v), 20, 'middle', INK, True))
    o.append(T(gx + 3 * cw + 14, gy + ch / 2 + 5, '50', 14, 'start', MUT)); o.append(T(gx + 3 * cw + 14, gy + ch * 1.5 + 5, '50', 14, 'start', MUT))
    o.append(T(gx + cw / 2, gy + 2 * ch + 22, '50 called pinch', 13, 'middle', MUT))
    rx = 60
    o.append(T(rx, 270, 'accuracy', 14, 'start', INK, True)); o.append(T(rx + 150, 270, '(46 + 45) ÷ 100 = 91%', 14, 'start'))
    o.append(T(rx, 298, 'pinch precision', 14, 'start', INK, True)); o.append(T(rx + 150, 298, '46 ÷ (46 + 4) = 92%   (column)', 14, 'start'))
    o.append(T(rx, 326, 'pinch recall', 14, 'start', INK, True)); o.append(T(rx + 150, 326, '46 ÷ 50 = 92%   (row)', 14, 'start'))
    o.append(T(rx, 364, 'Orange cells are wrong actions: add a confidence check and a hover highlight before commit.', 13, 'start', LV))
    return 380, ''.join(o)
FIG[5] = (f5, 'The worked example in one matrix: 46 of 50 pinches are correct, 4 grabs are called pinch, and 4 pinches are missed or called grab. Accuracy is 91%, pinch precision 92%, recall 92%; the orange errors are why a confidence check and hover highlight come before the response.',
          'A two-by-three grid: did pinch row 46, 3, 1 and did grab row 4, 45, 1 across called pinch, called grab and missed, with correct cells blue and errors orange; below, accuracy 91 percent, precision 92 percent and recall 92 percent.')


# ---- 6.6 normalised gain ----
def f6():
    y1, sc = 300, 2.4
    o = [T(40, 28, 'Mean test score out of 100 (30 students per group)', 15, 'start', bold=True)]
    o.append(L(70, y1, 470, y1, L2, 1.5))
    for v in [0, 20, 40, 60, 80, 100]:
        y = y1 - v * sc
        o.append(L(70, y, 470, y, 'var(--line)', 1)); o.append(T(62, y + 4.5, str(v), 13, 'end', MUT))
    groups = [(110, 'AR app', 78, AC, ACS), (300, 'printed notes', 66, L2, PANEL)]
    for gx, name, post, st, fi in groups:
        o.append(R(gx, y1 - 40 * sc, 60, 40 * sc, PANEL, MUT, 2)); o.append(T(gx + 30, y1 - 40 * sc - 8, 'pre 40', 13, 'middle', MUT, True))
        o.append(R(gx + 70, y1 - post * sc, 60, post * sc, fi, st, 2)); o.append(T(gx + 100, y1 - post * sc - 8, f'post {post}', 13, 'middle', INK, True))
        o.append(T(gx + 65, y1 + 22, name, 14, 'middle', INK, True))
    o.append(L(70, y1 - 100 * sc, 470, y1 - 100 * sc, NX, 1.5, '5 4'))
    bx = 500
    o.append(T(bx, 70, 'g = (post − pre) ÷ (100 − pre)', 14, 'start', bold=True))
    o.append(T(bx, 96, 'room to grow = 100 − 40 = 60', 13, 'start'))
    o.append(T(bx, 140, 'AR app', 14, 'start', AC, True)); o.append(T(bx, 162, 'raw 78 − 40 = 38', 13, 'start')); o.append(T(bx, 184, 'g = 38 ÷ 60 = 0.63', 14, 'start', AC, True))
    o.append(T(bx, 226, 'printed notes', 14, 'start', INK, True)); o.append(T(bx, 248, 'raw 66 − 40 = 26', 13, 'start')); o.append(T(bx, 270, 'g = 26 ÷ 60 = 0.43', 14, 'start', INK, True))
    o.append(T(40, 360, 'A signal, not proof: 30 students per group and one test.', 14, 'start', MUT))
    return 376, ''.join(o)
FIG[6] = (f6, 'Both groups start from the same pre-test mean of 40, so the maximum possible gain is 60 points for each. The AR group\'s 38-point rise normalises to 0.63 and the printed-notes group\'s 26-point rise to 0.43; with 30 students per group this is a signal, not proof.',
          'Paired bars of pre-test 40 and post-test 78 for the AR group and 40 and 66 for printed notes, with a panel working the normalised gains 38 over 60 equals 0.63 and 26 over 60 equals 0.43.')


# ---- 6.7 motion-to-photon budget with a cloud renderer ----
def f7():
    x0, sc = 170, 20
    o = [T(40, 28, 'Motion-to-photon time with a cloud renderer (ms)', 15, 'start', bold=True)]
    bx = x0 + 20 * sc
    o.append(L(bx, 56, bx, 220, LV, 2, '6 4')); o.append(Tb(bx, 52, '20 ms limit', 13, 'middle', LV, True))
    rows = [('budget', 'network ≤ 8', 8, '20'), ('server 1000 km', 'network 10', 10, '22')]
    for i, (name, nl, net, tot) in enumerate(rows):
        y = 70 + i * 80
        o.append(T(x0 - 12, y + 26, name, 14, 'end', INK, True))
        lane(o, x0, y, sc, [('render 8', 0, 8, PANEL, L2), (nl, 8, 8 + net, ACS if net <= 8 else LVS, AC if net <= 8 else LV),
                            ('scan 4', 8 + net, 12 + net, PANEL, L2)])
        o.append(T(x0 + (12 + net) * sc + 8, y + 26, tot, 14, 'start', LV if net > 8 else INK, True))
    o.append(T(bx + 6, 210, '2 ms over', 13, 'start', LV, True))
    o.append(xaxis(x0, x0 + 24 * sc, 232, [0, 4, 8, 12, 16, 20, 24], lambda v: x0 + v * sc))
    o.append(T(40, 300, 'Network left: 20 − 8 − 4 = 8 ms.  Light in fibre: 2 × 10⁸ m/s.', 14, 'start'))
    o.append(T(40, 324, '8 ms round trip = 1600 km, so the server must be within 800 km one way.', 14, 'start'))
    o.append(T(40, 348, '1000 km away: 2 × 10⁶ m ÷ 2 × 10⁸ m/s = 10 ms; total 8 + 10 + 4 = 22 ms.', 14, 'start', bold=True))
    return 364, ''.join(o)
FIG[7] = (f7, 'Each lane spends the same 20 ms motion-to-photon budget, in milliseconds. Rendering takes 8 ms and the display scan 4 ms, so the network gets only 8 ms; a server 1000 km away needs 10 ms of light time, and the total becomes 22 ms, which is 2 ms over the budget.',
          'Two timelines against a dashed 20 millisecond limit: render 8, network 8 and scan 4 ending at 20, and render 8, network 10 and scan 4 ending at 22, two past the limit; below, the distance working 800 km one way.')


TEXT = {
    1: [('Every AR system follows the same loop. The figure shows the blocks in order.',
         'Every AR system follows the same loop, in this order.')],
    3: [('Only a few universities teach SLAM at this depth; keep the pipeline and ideas, not the optimisation mathematics.',
         'Keep the pipeline and ideas, not the optimisation mathematics.')],
    7: [('The figure shows the working stack. Read from the bottom.',
         'The working stack reads from the bottom up.')],
}


def text_fixes(k):
    return TEXT.get(k, [])


def drop_sources():
    return ['ocw.mit.edu']


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d
