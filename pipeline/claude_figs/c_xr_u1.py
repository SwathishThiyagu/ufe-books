"""Claude's hand-drawn figures for c-xr-u1 (AR/VR, unit 1: foundations of VR, AR and XR), one per chapter, from each
chapter's worked example, plus the sentences in the chapter text that describe a figure (text_fixes)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {}


# ---- 1.1 the reality-virtuality continuum with the four products ----
def f1():
    x0, x1, y = 70, 650, 150
    o = [T(360, 30, 'How much of what you see is computed?', 15, bold=True)]
    o.append(L(x0, y, x1, y, L2, 4))
    pts = [(x0, 'Real', 'environment'), (250, 'AR', 'virtual added'), (470, 'Augmented', 'virtuality'), (x1, 'VR', 'all virtual')]
    for x, a, b in pts:
        o.append(C(x, y, 9, AC if a in ('AR', 'VR') else L2))
        o.append(T(x, y - 42, a, 15, bold=True)); o.append(T(x, y - 22, b, 13, fill=MUT))
    o.append(brace(250, 470, y + 26))
    o.append(T(360, y + 50, 'the middle span is often called mixed reality', 13, fill=MUT))
    o.append(T(x0, y + 26, '0 % virtual', 13, 'start', MUT)); o.append(T(x1, y + 26, '100 % virtual', 13, 'end', MUT))
    # the products
    cards = [(170, '(i) sofa on your wall', 'AR', 250), (360, '(iii) ball behind real leg', 'MR', 330), (560, '(ii) cockpit, room hidden', 'VR', x1)]
    for cx, s, lab, px in cards:
        o.append(boxt(cx - 95, 238, 190, 50, [s, lab], ACS, AC, 13, fills=[INK, INK]))
    o.append(boxt(200, 318, 320, 46, ['(iv) 360° video you drag: not on the line,', 'a fixed panorama, no tracked world'], NXS, NX, 13))
    return 380, ''.join(o)
FIG[1] = (f1, 'The four products from the worked example placed by how much of the view is computed: the sofa on your wall is AR, the ball hidden by the real table leg is MR, the cockpit is VR, and the dragged 360° video is not on the line at all.',
          'A horizontal line from real environment through AR and augmented virtuality to VR, with the sofa, the hidden ball and the cockpit placed on it, and the 360-degree video shown in a box below, off the line.')


# ---- 1.2 timeline of four landmarks ----
def f2():
    x0, x1, y = 60, 680, 170
    fx = lambda yr: x0 + (yr - 1955) / (2020 - 1955) * (x1 - x0)
    o = [T(360, 30, 'Four landmarks on one time line', 15, bold=True)]
    o.append(L(x0, y, x1, y, L2, 3))
    for yr in range(1960, 2021, 10):
        o += [L(fx(yr), y, fx(yr), y + 6, L2, 1.5), T(fx(yr), y + 24, str(yr), 13, fill=MUT)]
    lm = [(1962, 'Sensorama', 'many senses'), (1968, 'Tracked HMD', 'head drives view'), (1992, 'CAVE', 'shared room'), (2012, 'Rift campaign', 'low cost')]
    ups = [True, False, True, True]
    for (yr, a, b), up in zip(lm, ups):
        X = fx(yr)
        o.append(C(X, y, 8, AC))
        if up:
            o += [L(X, y - 10, X, y - 50, AC, 1.5), T(X, y - 78, f'{a} {yr}', 14, bold=True), T(X, y - 60, b, 13, fill=MUT)]
        else:
            o += [L(X, y + 10, X, y + 46, AC, 1.5), T(X + 4, y + 64, f'{a} {yr}', 14, 'start', bold=True), T(X + 4, y + 82, b, 13, 'start', MUT)]
    gaps = [(1962, 1968, '6 yr', INK), (1968, 1992, '24 years, the widest gap', NX), (1992, 2012, '20 years', INK)]
    yb = 290
    for a, b, s, c in gaps:
        o.append(brace(fx(a), fx(b), yb, c, up=True))
        o.append(T((fx(a) + fx(b)) / 2 + (10 if a == 1962 else 0), yb + 22, s, 14 if c == NX else 13, fill=c, bold=(c == NX)))
    o.append(T(360, 352, '1968 − 1962 = 6,  1992 − 1968 = 24,  2012 − 1992 = 20', 14))
    return 370, ''.join(o)
FIG[2] = (f2, 'The four landmarks from the worked example on one time line. The gaps are 6, 24 and 20 years; the widest runs from the 1968 tracked display to the 1992 CAVE.',
          'A time line from 1955 to 2020 with Sensorama 1962, the tracked head-mounted display 1968, the CAVE 1992 and the Rift campaign 2012, and brackets giving the gaps of 6, 24 and 20 years.')


# ---- 1.3 three I's in the surgical trainer and the lag bar ----
def f3():
    o = [T(360, 26, 'The surgical trainer, sorted into the three I\'s', 15, bold=True)]
    boxes = [(30, 'Immersion', ['110° view, stereo', 'stereo sound'], AC, ACS), (260, 'Interaction', ['tracked gloves,', 'cut → bleeding'], NX, NXS),
             (490, 'Imagination', ['surgery scenario,', 'no live patient'], AC, ACS)]
    for x, h, ls, st, fi in boxes:
        o.append(boxt(x, 44, 200, 84, [h] + ls, fi, st, 14, bold_first=True))
    o.append(T(360, 152, 'interaction fails first', 14, fill=NX, bold=True))
    o.append(L(360, 158, 360, 182, NX, 2, arrow='x'))
    # lag bar
    x0, x1, y = 90, 650, 230
    s = (x1 - x0) / 100
    o.append(T(x1, 212, 'head-tracking lag, ms', 13, 'end', MUT))
    o.append(R(x0, y, 20 * s, 40, ACS, AC, 3))
    o.append(R(x0 + 20 * s, y, 80 * s, 40, NXS, NX, 3))
    o.append(T(x0 + 10 * s, y + 26, '20', 14, bold=True))
    o.append(T(x0 + 60 * s, y + 26, 'excess 100 − 20 = 80 ms', 14, bold=True))
    o.append(xaxis(x0, x1, y + 50, [0, 20, 40, 60, 80, 100], lambda v: x0 + v * s))
    o.append(L(x0 + 20 * s, y - 14, x0 + 20 * s, y + 54, AC, 2.5, '5 4'))
    o.append(T(x0 + 20 * s + 6, y - 2, 'limit 20 ms', 13, 'start', AC))
    o.append(T(360, 340, 'measured 100 ms = 5 × the limit: eyes and inner ear disagree, the user gets dizzy', 14))
    return 360, ''.join(o)
FIG[3] = (f3, 'Each part of the surgical trainer sorted into one of the three I\'s. The measured 100 ms lag is 80 ms over the 20 ms limit, five times the limit, so interaction fails first.',
          'Three boxes for immersion, interaction and imagination filled with the trainer\'s parts, the interaction box picked out, and a bar of 100 milliseconds split into 20 inside the limit and 80 of excess.')


# ---- 1.4 frame budget 90 Hz vs 120 Hz, and the latency sum ----
def f4():
    x0, x1 = 160, 680
    s = (x1 - x0) / 20
    X = lambda v: x0 + v * s
    o = [T(40, 28, 'One frame: simulation 2 ms + rendering 7 ms = 9 ms of work', 15, 'start', bold=True)]
    rows = [(60, '90 Hz frame', 11.1, True), (140, '120 Hz frame', 8.3, False)]
    for y, lab, bud, fits in rows:
        o.append(T(x0 - 12, y + 30, lab, 14, 'end', bold=True))
        o.append(R(X(0), y, bud * s, 46, 'none', L2, 3, 2, '6 4'))
        o.append(R(X(0) + 3, y + 8, 2 * s, 30, ACS, AC, 3)); o.append(T(X(1) + 3, y + 28, 'sim 2', 13))
        o.append(R(X(2) + 3, y + 8, 7 * s, 30, ACS, AC, 3)); o.append(T(X(5.5) + 3, y + 28, 'render 7', 13))
        o.append(T(X(bud), y - 6, f'budget {bud} ms', 13, 'middle', MUT))
        if fits:
            o.append(T(X(bud) + 8, y + 28, 'fits, 2.1 ms spare', 14, 'start', AC, bold=True))
        else:
            o.append(R(X(bud), y + 8, (9 - bud) * s + 3, 30, NXS, NX, 3))
            o.append(T(X(9.3) + 6, y + 28, 'overruns by 0.7 ms → dropped frame', 14, 'start', NX, bold=True))
    o.append(T(40, 238, 'Motion-to-photon latency at 90 Hz', 15, 'start', bold=True))
    y = 254
    o.append(T(x0 - 12, y + 26, 'latency', 14, 'end', bold=True))
    parts = [(0, 2, 'sim 2'), (2, 9, 'render 7'), (9, 13, '+ 4')]
    for a, b, lab in parts:
        o.append(R(X(a), y, (b - a) * s, 38, LVS if a == 9 else ACS, LV if a == 9 else AC, 3)); o.append(T(X((a + b) / 2), y + 24, lab, 13))
    o.append(T(X(11), y - 6, 'tracker + display', 13, fill=LV))
    o.append(L(X(20), y - 12, X(20), y + 50, NX, 2.5, '5 4')); o.append(T(X(20) - 6, y - 16, 'target 20 ms', 13, 'end', NX))
    o.append(T(X(13) + 8, y + 24, '= 13 ms, under target', 14, 'start', bold=True))
    o.append(xaxis(x0, x1, y + 52, [0, 5, 10, 15, 20], X, 'milliseconds'))
    return 360, ''.join(o)
FIG[4] = (f4, 'At 90 Hz the 9 ms of simulation and rendering fit inside the 11.1 ms frame; at 120 Hz the frame is only 8.3 ms, so the work overruns and frames drop. Adding the 4 ms tracker-to-display path gives 13 ms of latency, under the 20 ms target.',
          'Two frame boxes, 11.1 ms and 8.3 ms, each holding 2 ms of simulation and 7 ms of rendering; the second overruns. Below, a latency bar of 2 plus 7 plus 4 equals 13 ms against a 20 ms target line.')


# ---- 1.5 the four parts as one loop ----
def f5():
    o = [T(360, 26, 'The student\'s ₹17,500 setup as the four-part loop', 15, bold=True)]
    W, H = 230, 74
    pos = {'in': (40, 60), 'sw': (450, 60), 'out': (450, 230), 'hu': (40, 230)}
    data = {'in': ['Input devices', 'gamepad ₹1,500', 'phone sensor, 3 DoF'], 'sw': ['Computer and software', 'phone ₹15,000'],
            'out': ['Output devices', 'viewer ₹1,000', 'narrow phone screen'], 'hu': ['Human', 'the student']}
    for k, (x, y) in pos.items():
        weak = k == 'out'
        o.append(boxt(x, y, W, H, data[k], NXS if weak else PANEL, NX if weak else AC, 14, bold_first=True))
    o.append(L(40 + W + 4, 97, 446, 97, AC, 2.5, arrow='n')); o.append(Tb(360, 90, 'head pose, buttons', 13))
    o.append(L(565, 60 + H + 4, 565, 226, AC, 2.5, arrow='n')); o.append(Tb(565, 186, 'images, sound', 13))
    o.append(L(446, 267, 40 + W + 4, 267, AC, 2.5, arrow='n')); o.append(Tb(360, 260, 'sight, sound', 13))
    o.append(L(155, 226, 155, 60 + H + 4, AC, 2.5, arrow='n')); o.append(Tb(155, 186, 'turn, press', 13))
    o.append(T(565, 330, 'weak link: narrow view, no haptics', 13, fill=NX, bold=True))
    o.append(T(40, 336, '₹1,000 + ₹15,000 + ₹1,500 = ₹17,500', 14, 'start'))
    o.append(T(40, 358, 'tracking 3 of 6 DoF: the 3 position axes are missing, so leaning does nothing', 14, 'start'))
    return 376, ''.join(o)
FIG[5] = (f5, 'The worked example as one loop: the gamepad and the phone\'s sensor are input, the phone is the computer, the viewer and screen are output, and the student closes the loop. The parts cost ₹17,500 and the output side is the weak link.',
          'Four boxes in a loop, input devices, computer and software, output devices and the human, labelled with the gamepad, phone and viewer and their prices; the output box is picked out as the weak link.')


# ---- 1.6 three tests decide, then the sofa clearance ----
def f6():
    o = [T(40, 26, 'Three tests decide', 15, 'start', bold=True)]
    tests = [(50, 'Test 1: real world needed?'), (140, 'Test 2: register to it?'), (230, 'Test 3: real hides virtual?')]
    for y, s in tests:
        o.append(boxt(40, y, 220, 50, [s], PANEL, AC, 14))
    o.append(L(150, 102, 150, 136, AC, 2, arrow='n')); o.append(T(158, 124, 'yes', 13, 'start', MUT))
    o.append(L(150, 192, 150, 226, AC, 2, arrow='n')); o.append(T(158, 214, 'yes', 13, 'start', MUT))
    o.append(L(262, 75, 300, 75, AC, 2, arrow='n')); o.append(T(281, 68, 'no', 13, fill=MUT))
    o.append(boxt(304, 56, 110, 40, ['VR (a) knee'], ACS, AC, 13))
    o.append(L(262, 245, 300, 220, AC, 2, arrow='n')); o.append(T(272, 222, 'no', 13, fill=MUT))
    o.append(boxt(304, 196, 110, 40, ['AR (b) engine'], ACS, AC, 13))
    o.append(L(262, 265, 300, 290, NX, 2, arrow='x')); o.append(T(272, 296, 'yes', 13, fill=MUT))
    o.append(boxt(304, 272, 110, 40, ['MR (c) sofa'], NXS, NX, 13))
    # top view of the wall
    gx = 440
    o.append(T(gx, 26, 'Case (c), seen from above', 15, 'start', bold=True))
    sc = 250 / 2.7
    wx = gx + 15
    o.append(R(wx, 60, 2.7 * sc, 12, 'var(--line2)', L2, 1))
    o.append(T(wx + 1.35 * sc, 52, 'wall 2.7 m', 13))
    sx = wx + 0.15 * sc
    o.append(R(sx, 74, 2.4 * sc, 50, ACS, AC, 6)); o.append(T(sx + 1.2 * sc, 104, 'sofa 2.4 m', 14, bold=True))
    o.append(T(wx + 2, 146, '0.15', 13, 'start')); o.append(T(wx + 2.7 * sc - 2, 146, '0.15', 13, 'end'))
    o.append(L(wx, 128, sx, 128, INK, 1.5)); o.append(L(sx + 2.4 * sc, 128, wx + 2.7 * sc, 128, INK, 1.5))
    o.append(R(wx + 0.75 * sc, 178, 1.2 * sc, 32, LVS, LV, 4)); o.append(T(wx + 1.35 * sc, 199, 'coffee table', 13))
    o.append(L(wx + 2.05 * sc, 126, wx + 2.05 * sc, 194, MUT, 1.5, '4 3'))
    o.append(T(wx + 2.05 * sc + 6, 176, '0.6 m', 13, 'start', MUT))
    o.append(T(wx + 1.35 * sc, 232, '▲ you look from here', 13, fill=MUT))
    o.append(T(gx, 262, 'spare width 2.7 − 2.4 = 0.3 m', 14, 'start'))
    o.append(T(gx, 284, 'centred: 0.3 ÷ 2 = 0.15 m each side', 14, 'start'))
    o.append(T(gx, 308, 'the table is nearer than the sofa,', 13, 'start', MUT))
    o.append(T(gx, 326, 'so it must hide it: occlusion → MR', 13, 'start', MUT))
    return 340, ''.join(o)
FIG[6] = (f6, 'The three tests sort the three cases; the sofa needs MR because the real coffee table in front must hide part of it. It leaves 0.15 m each side.',
          'Left, three test boxes in a column with yes and no branches to VR, AR and MR. Right, a top view of a 2.7 m wall, a 2.4 m sofa with 0.15 m each side, and a coffee table in front.')


TEXT = {
    6: [('a coffee table 0.6 m in front of that wall', 'a coffee table 0.6 m in front of the sofa')],
    5: [('The figure shows the layers from application down to hardware.',
         'The figure draws the four parts as this loop, using the student\'s phone setup from the worked example.')],
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
