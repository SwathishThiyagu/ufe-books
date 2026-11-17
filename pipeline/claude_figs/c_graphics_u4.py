"""Claude's hand-drawn figures for c-graphics-u4 (Computer Graphics and Multimedia, unit 4: multimedia elements,
systems, formats, compression, MPEG and synchronisation), one per chapter, from each chapter's worked example."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def chain(o, x, y, items, h=50, gap=26, size=13, c=AC):
    """row of boxes joined by arrows; items = [(w, lines, fill, stroke)]"""
    for i, (w, lines, f, s) in enumerate(items):
        o.append(boxt(x, y, w, h, lines, f, s, size, bold_first=True))
        if i < len(items) - 1:
            o.append(L(x + w + 3, y + h / 2, x + w + gap - 3, y + h / 2, c, 2, arrow='n'))
        x += w + gap
    return x - gap


# ---- 4.1 one play of the kiosk loop ----
def f1():
    o = []
    x0, x1 = 170, 680
    fx = lambda t: x0 + t / 37 * (x1 - x0)
    rows = [('text: train name', None, None, MUT, PANEL), ('graphics: route map', None, None, MUT, PANEL),
            ('audio, 20 s', 0, 20, AC, ACS), ('video, 15 s', 20, 35, NX, NXS), ('animation, 2 s', 35, 37, LV, LVS),
            ('touch button', None, None, INK, 'none')]
    y, rh = 40, 38
    for i, (lab, a, b, c, f) in enumerate(rows):
        yy = y + i * rh
        o.append(T(x0 - 12, yy + 23, lab, 13, 'end', c, True))
        if a is None:
            if i == 5:
                o.append(R(fx(0), yy + 6, fx(37) - fx(0), 24, 'none', INK, 6, 1.6, '6 4'))
                o.append(T(fx(18.5), yy + 23, 'control: always there, no duration', 13, 'middle', INK))
            else:
                o.append(R(fx(0), yy + 6, fx(37) - fx(0), 24, PANEL, L2, 4, 1.2))
                o.append(T(fx(18.5), yy + 23, 'on screen all the time, not timed', 13, 'middle', MUT))
        else:
            o.append(R(fx(a), yy + 6, fx(b) - fx(a), 24, f, c, 4, 2))
            if b - a > 5:
                o.append(T((fx(a) + fx(b)) / 2, yy + 23, f'{a} to {b} s', 13, 'middle', c, True))
            else:
                o.append(T(fx(a) - 8, yy + 23, f'{a} to {b} s', 13, 'end', c, True))
    ya = y + 6 * rh + 8
    o.append(xaxis(x0, x1, ya, [0, 5, 10, 15, 20, 25, 30, 35, 37], fx, 'time in one loop (s)'))
    o.append(brace(fx(0), fx(37), ya + 58, NX))
    o.append(T(fx(18.5), ya + 82, 'timed media: 20 s + 15 s + 2 s = 37 s', 14, 'middle', NX, True))
    return ya + 96, ''.join(o)
FIG[1] = (f1, 'One play of the Chennai kiosk loop: 20 s of audio, then 15 s of video, then the 2 s blinking icon, 37 s of timed media in all. The text, the map and the touch button stay on the screen the whole time and add no duration.',
          'A timeline from 0 to 37 seconds with rows for text and graphics shown across the whole loop, audio from 0 to 20 s, video from 20 to 35 s, animation from 35 to 37 s, and a dashed touch-button row marked as a control, with a brace of 37 s under the axis.')


# ---- 4.2 raw sizes of audio and video ----
def f2():
    o = []
    y = 34
    o.append(T(30, y, 'audio: one minute, stereo, 44.1 kHz, 16 bits', 14, 'start', AC, True))
    chain(o, 30, y + 14, [(150, ['44,100 samples/s', 'per channel'], PANEL, AC), (130, ['× 2 channels', '× 2 bytes'], PANEL, AC),
                          (150, ['176,400 B/s'], ACS, AC), (170, ['× 60 s = 10,584,000 B', '= 10.584 MB'], ACS, AC)])
    y = 136
    o.append(T(30, y, 'one video frame: 640 × 480, 24 bits = 3 bytes per pixel', 14, 'start', NX, True))
    chain(o, 30, y + 14, [(150, ['640 × 480', '= 307,200 pixels'], PANEL, NX), (130, ['× 3 bytes'], PANEL, NX),
                          (196, ['921,600 B', '= 0.9216 MB per frame'], NXS, NX)], c=NX)
    y = 238
    o.append(T(30, y, 'video stream: 25 frames each second', 14, 'start', LV, True))
    chain(o, 30, y + 14, [(196, ['921,600 B per frame'], PANEL, LV), (130, ['× 25 frames/s'], PANEL, LV),
                          (230, ['23,040,000 B/s', '= 23.04 MB/s'], LVS, LV)], c=LV)
    o.append(T(30, 334, 'raw size = number of units × bytes per unit; 1 MB = 10⁶ B', 13, 'start', MUT))
    o.append(T(30, 354, 'one second of raw video is about 130 times one second of CD audio', 13, 'start', MUT))
    return 370, ''.join(o)
FIG[2] = (f2, 'Raw size is the number of units times the bytes in each. Stereo 16-bit audio at 44.1 kHz runs at 176,400 B/s, 10.584 MB a minute; one 640 × 480 frame at 3 bytes a pixel is 921,600 B, and 25 of them a second make 23.04 MB/s.',
          'Three rows of boxes joined by arrows: 44,100 samples per second times 2 channels times 2 bytes gives 176,400 B/s and 10.584 MB a minute; 640 by 480 pixels times 3 bytes gives 921,600 B a frame; 921,600 B times 25 frames a second gives 23.04 MB/s.')


# ---- 4.3 the four-layer model and the 2 h raw load ----
def f3():
    o = []
    layers = [('application', 'video editor, player', PANEL, INK), ('codec / middleware', 'compresses the raw streams', LVS, LV),
              ('driver / OS', 'moves buffers, schedules', PANEL, AC), ('hardware', 'camera, mic, SSD, GPU', ACS, AC)]
    x, w, h = 30, 250, 60
    for i, (a, b, f, c) in enumerate(layers):
        yy = 30 + i * (h + 18)
        o.append(boxt(x, yy, w, h, [a, b], f, c, 14, bold_first=True))
        if i < 3:
            o.append(L(x + w / 2 - 30, yy + h + 2, x + w / 2 - 30, yy + h + 16, INK, 1.8, arrow='m'))
            o.append(L(x + w / 2 + 30, yy + h + 16, x + w / 2 + 30, yy + h + 2, INK, 1.8, arrow='m'))
    o.append(T(x + w / 2, 30 + 4 * (h + 18) + 8, 'each layer only talks to its neighbours', 13, 'middle', MUT))
    xr = 340
    lines = [('2 h = 7,200 s, 1080p30, 3 bytes a pixel', INK, True, 14),
             ('frame: 1920 × 1080 = 2,073,600 pixels', MUT, False, 13),
             ('video: 2,073,600 × 3 × 30 = 186,624,000 B/s', AC, True, 13),
             ('× 7,200 s = 1,343.6928 GB', AC, True, 13),
             ('', INK, False, 13),
             ('audio: 48,000 × 2 ch × 2 B = 192,000 B/s', NX, True, 13),
             ('× 7,200 s = 1.3824 GB', NX, True, 13),
             ('', INK, False, 13),
             ('raw total = 1,345.0752 GB ≈ 1.345 TB', LV, True, 15),
             ('store on a 2 TB SSD;', INK, False, 13),
             ('the codec layer shrinks it, with GPU encode', INK, False, 13)]
    for i, (t, c, b, sz) in enumerate(lines):
        if t: o.append(T(xr, 46 + i * 24, t, sz, 'start', c, b))
    return 30 + 4 * (h + 18) + 24, ''.join(o)
FIG[3] = (f3, 'The four layers each talk only to their neighbours: the editor asks the codec, the codec asks the driver, the driver drives the device. The codec layer is where the 2 h raw load of 1,345.0752 GB, 1080p30 video plus stereo audio, gets compressed.',
          'A stack of four boxes, application, codec or middleware, driver or OS, and hardware, with two-way arrows between neighbours; beside it the 2 hour calculation: video 1,343.6928 GB plus audio 1.3824 GB gives 1,345.0752 GB raw, stored on a 2 TB SSD.')


# ---- 4.4 a format for the photograph and for the logo ----
def f4():
    o = []
    sc = 0.2
    # photograph
    px, py = 40, 50
    o.append(T(px, py - 16, 'photograph 1200 × 800', 14, 'start', AC, True))
    o.append(f'<defs><linearGradient id="ph-UID" x1="0" y1="0" x2="1" y2="1"><stop offset="0" style="stop-color:var(--accent-soft)"/><stop offset="1" style="stop-color:var(--accent)"/></linearGradient></defs>')
    o.append(f'<rect x="{px}" y="{py}" width="{1200 * sc}" height="{800 * sc}" style="fill:url(#ph-UID);stroke:var(--accent);stroke-width:2"/>')
    o.append(T(px + 120, py + 86, 'continuous tone', 13, 'middle', INK, True))
    # logo with checkerboard
    lx, ly = 40, 260
    o.append(T(lx, ly - 16, 'logo 200 × 200, transparent', 14, 'start', NX, True))
    n, cs = 4, 200 * sc / 4
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0: o.append(R(lx + i * cs, ly + j * cs, cs, cs, LN, 'none', 0, 0))
    o.append(R(lx, ly, 200 * sc, 200 * sc, 'none', L2, 0, 1.2))
    o.append(f'<circle cx="{lx + 20}" cy="{ly + 20}" r="13" style="fill:var(--next);stroke:none"/>')
    o.append(T(lx + 54, ly + 18, 'see-through', 13, 'start', MUT)); o.append(T(lx + 54, ly + 36, 'background', 13, 'start', MUT))
    o.append(T(lx, ly + 70, 'both drawn at the same scale', 13, 'start', MUT))
    # decisions
    xd = 330
    o.append(L(px + 244, py + 80, xd - 6, py + 80, AC, 2, arrow='n'))
    o.append(boxt(xd, py + 40, 110, 80, ['JPEG', 'lossy, small', 'no alpha needed'], ACS, AC, 13, bold_first=True))
    o.append(L(xd + 112, py + 80, xd + 140, py + 80, AC, 2, arrow='n'))
    o.append(T(xd + 148, py + 56, '1200 × 800 = 960,000 px', 13, 'start', INK))
    o.append(T(xd + 148, py + 78, '× 0.5 B/px = 480,000 B', 13, 'start', INK))
    o.append(T(xd + 148, py + 104, '= 480 kB', 16, 'start', AC, True))
    o.append(L(lx + 140, ly + 20, xd - 6, ly + 2, NX, 2, arrow='x'))
    o.append(L(lx + 140, ly + 20, xd - 6, ly + 54, NX, 2, arrow='x'))
    o.append(boxt(xd, ly - 26, 150, 52, ['PNG', 'full alpha, lossless'], NXS, NX, 13, bold_first=True))
    o.append(boxt(xd, ly + 34, 150, 52, ['SVG', 'vector, any size'], NXS, NX, 13, bold_first=True))
    o.append(T(xd + 162, ly + 2, 'flat colour, sharp edges', 13, 'start', MUT))
    o.append(T(xd + 162, ly + 64, 'if the logo is simple shapes', 13, 'start', MUT))
    return ly + 92, ''.join(o)
FIG[4] = (f4, 'The continuous-tone photograph goes to lossy JPEG, and at 0.5 byte a pixel its 960,000 pixels make 480,000 bytes, 480 kB. The logo needs a see-through background, so it goes to PNG, or to SVG if it is simple shapes that must stay sharp at any size.',
          'A shaded 1200 by 800 photograph with an arrow to a JPEG box and the size 480 kB, and a small 200 by 200 logo on a checkerboard background with arrows to PNG and SVG boxes, both pictures drawn to the same scale.')


# ---- 4.5 an MP4 with two streams ----
def f5():
    o = []
    o.append(R(30, 30, 660, 150, PANEL, INK, 12, 2.2))
    o.append(T(48, 54, 'MP4 container, 180 s', 14, 'start', INK, True))
    x0, x1 = 170, 670
    o.append(R(x0, 70, x1 - x0, 40, ACS, AC, 4, 2)); o.append(T(160, 95, 'H.264 video', 13, 'end', AC, True))
    o.append(T((x0 + x1) / 2, 95, '2 Mbps for 180 s', 13, 'middle', AC, True))
    o.append(R(x0, 122, x1 - x0, 40, NXS, NX, 4, 2)); o.append(T(160, 147, 'AAC audio', 13, 'end', NX, True))
    o.append(T((x0 + x1) / 2, 147, '128 kbps for 180 s', 13, 'middle', NX, True))
    y = 218
    o.append(T(40, y, 'video: 2,000,000 × 180 = 360,000,000 bits ÷ 8 = 45,000,000 B = 45 MB', 14, 'start', AC, True))
    o.append(T(40, y + 26, 'audio: 128,000 × 180 = 23,040,000 bits ÷ 8 = 2,880,000 B = 2.88 MB', 14, 'start', NX, True))
    # size bar
    yb = y + 56
    sc = 600 / 50
    o.append(R(40, yb, 45 * sc, 34, ACS, AC, 0, 2)); o.append(R(40 + 45 * sc, yb, 2.88 * sc, 34, NXS, NX, 0, 2))
    o.append(T(40 + 22.5 * sc, yb + 22, 'video 45 MB', 13, 'middle', AC, True))
    o.append(L(40 + 46.4 * sc, yb - 2, 40 + 46.4 * sc, yb - 12, NX, 1.4)); o.append(T(40 + 46.4 * sc, yb - 16, '2.88 MB audio', 13, 'end', NX, True))
    o.append(xaxis(40, 40 + 50 * sc, yb + 34, [0, 10, 20, 30, 40, 47.88], lambda v: 40 + v * sc, 'file size (MB)', lambda v: f'{v:g}'))
    o.append(T(360, yb + 106, 'total 45 + 2.88 = 47.88 MB, ignoring container overhead', 14, 'middle', LV, True))
    return yb + 122, ''.join(o)
FIG[5] = (f5, 'The MP4 container holds two streams of the same 180 s: H.264 video at 2 Mbps and AAC audio at 128 kbps. Bits ÷ 8 gives 45 MB and 2.88 MB, so the file is 47.88 MB, almost all of it video.',
          'An MP4 box holding a long video stream bar at 2 Mbps and an audio stream bar at 128 kbps, both 180 seconds, with the size worked out below and a bar of 47.88 MB split into 45 MB of video and 2.88 MB of audio.')


# ---- 4.6 the Huffman tree ----
def f6():
    o = []
    N = {'root': (300, 40, '100'), 'A': (170, 120, 'A 45'), 'N4': (430, 120, '55'), 'N2': (330, 200, '25'), 'N3': (530, 200, '30'),
         'C': (280, 280, 'C 12'), 'B': (380, 280, 'B 13'), 'N1': (480, 280, '14'), 'D': (590, 280, 'D 16'), 'F': (430, 360, 'F 5'), 'E': (530, 360, 'E 9')}
    edges = [('root', 'A', '0'), ('root', 'N4', '1'), ('N4', 'N2', '0'), ('N4', 'N3', '1'), ('N2', 'C', '0'), ('N2', 'B', '1'),
             ('N3', 'N1', '0'), ('N3', 'D', '1'), ('N1', 'F', '0'), ('N1', 'E', '1')]
    for a, b, bit in edges:
        (x1, y1, _), (x2, y2, _) = N[a], N[b]
        o.append(L(x1, y1 + 15, x2, y2 - 15, L2, 1.8))
        o.append(Tb((x1 + x2) / 2 + (-10 if bit == '0' else 10), (y1 + y2) / 2 + 4, bit, 14, 'middle', LV, True))
    codes = {'A': '0', 'C': '100', 'B': '101', 'D': '111', 'F': '1100', 'E': '1101'}
    for k, (x, y, t) in N.items():
        leaf = k in codes
        w = 56 if leaf else 46
        o.append(boxt(x - w / 2, y - 15, w, 30, [t], ACS if leaf else PANEL, AC if leaf else INK, 14, bold_first=True, rx=15))
        if leaf:
            o.append(T(x, y + 34, codes[k], 14, 'middle', NX, True))
    o.append(T(40, 40, 'merge the two', 13, 'start', MUT)); o.append(T(40, 58, 'smallest each time:', 13, 'start', MUT))
    for i, s in enumerate(['5 + 9 = 14', '12 + 13 = 25', '14 + 16 = 30', '25 + 30 = 55', '45 + 55 = 100']):
        o.append(T(40, 84 + i * 20, s, 13, 'start', INK))
    o.append(T(660, 330, 'green: code', 13, 'end', NX, True)); o.append(T(660, 348, '0 left, 1 right', 13, 'end', LV, True))
    y = 420
    o.append(T(40, y, 'bits = 45×1 + 13×3 + 12×3 + 16×3 + 9×4 + 5×4 = 224, average 2.24 bits a symbol', 14, 'start', INK, True))
    o.append(T(40, y + 26, 'fixed 3-bit code: 300 bits;  ratio 300 ÷ 224 ≈ 1.34;  saving 76 ÷ 300 ≈ 25.3%', 14, 'start', NX, True))
    return y + 42, ''.join(o)
FIG[6] = (f6, 'The Huffman tree for A:45, B:13, C:12, D:16, E:9, F:5, built by merging the two smallest weights each time. Reading 0 for left and 1 for right, A gets 1 bit and E and F get 4, so 100 symbols cost 224 bits instead of 300.',
          'A Huffman tree with root 100 splitting into A 45 and 55, then 25 and 30, then C 12, B 13, 14 and D 16, then F 5 and E 9, edges labelled 0 left and 1 right and each leaf\'s code below it; the merge steps are listed at the left and the bit totals below.')


# ---- 4.7 motion vector and the coded block ----
def f7():
    o = []
    cs = 9
    X0, Y0 = 40, 40
    cols, rows = 26, 24
    for i in range(cols + 1):
        o.append(L(X0 + i * cs, Y0, X0 + i * cs, Y0 + rows * cs, LN, 0.8))
    for j in range(rows + 1):
        o.append(L(X0, Y0 + j * cs, X0 + cols * cs, Y0 + j * cs, LN, 0.8))
    o.append(R(X0, Y0, cols * cs, rows * cs, 'none', L2, 0, 1.4))
    bx, by = X0 + 2 * cs, Y0 + 6 * cs
    o.append(R(bx, by, 16 * cs, 16 * cs, 'none', INK, 0, 2, '6 4'))
    o.append(R(bx + 5 * cs, by - 3 * cs, 16 * cs, 16 * cs, ACS, AC, 0, 2.4))
    o.append(T(bx + 4, by + 16 * cs + 18, '(x, y): current block', 13, 'start', INK, True))
    o.append(T(bx + 5 * cs + 8 * cs, by - 3 * cs + 8 * cs, 'best match', 13, 'middle', AC, True))
    o.append(T(bx + 5 * cs + 8 * cs, by - 3 * cs + 8 * cs + 18, '(x+5, y−3)', 13, 'middle', AC, True))
    o.append(C(bx, by, 5, INK))
    o.append(L(bx, by, bx + 5 * cs - 3, by - 3 * cs + 2, LV, 2.6, arrow='l'))
    o.append(T(X0 + cols * cs / 2, Y0 - 12, 'reference frame, 1 square = 1 pixel, block 16 × 16', 13, 'middle', MUT))
    o.append(Tb(bx + 5 * cs + 10, by - 3 * cs - 10, 'v = (5, −3)', 14, 'start', LV, True))
    xr = 310
    o.append(T(xr, 50, 'motion vector: 8 + 8 = 16 bits', 14, 'start', LV, True))
    o.append(T(xr, 76, 'residual: 40 coefficients × 6 bits = 240 bits', 14, 'start', AC, True))
    o.append(T(xr, 102, 'coded: 16 + 240 = 256 bits = 32 B', 14, 'start', NX, True))
    o.append(T(xr, 128, 'raw: 16 × 16 × 8 = 2048 bits = 256 B', 14, 'start', INK, True))
    sc = 380 / 2048
    yb = 160
    o.append(R(xr, yb, 2048 * sc, 28, PANEL, INK, 0, 1.8)); o.append(T(xr + 1024 * sc, yb + 19, 'raw 2048 bits', 13, 'middle', INK, True))
    o.append(R(xr, yb + 40, 16 * sc, 28, LVS, LV, 0, 1.8)); o.append(R(xr + 16 * sc, yb + 40, 240 * sc, 28, ACS, AC, 0, 1.8))
    o.append(T(xr + 256 * sc + 8, yb + 59, 'coded 256 bits', 13, 'start', NX, True))
    o.append(T(xr, yb + 104, '2048 ÷ 256 = 8, an 8 : 1 saving', 15, 'start', NX, True))
    return Y0 + rows * cs + 40, ''.join(o)
FIG[7] = (f7, 'The 16 × 16 block at (x, y) finds its best match at (x+5, y−3) in the reference frame, so the motion vector is (5, −3). Sending 16 bits of vector and 240 bits of residual, 256 bits in all, replaces 2048 raw bits: 8 : 1.',
          'A pixel grid of the reference frame with the dashed current 16 by 16 block and the shaded matching block 5 pixels right and 3 up, joined by the vector (5, −3); beside it the bit counts and two bars, raw 2048 bits against coded 256 bits.')


# ---- 4.8 one hour of MPEG-2 on a DVD ----
def f8():
    o = []
    y = 40
    o.append(T(40, y, 'video: 6,000,000 bit/s × 3600 s ÷ 8 = 2,700,000,000 B = 2.7 GB', 14, 'start', AC, True))
    o.append(T(40, y + 26, 'audio: 448,000 bit/s × 3600 s ÷ 8 = 201,600,000 B = 0.2016 GB', 14, 'start', NX, True))
    o.append(T(40, y + 52, 'total: 2,901,600,000 B = 2.9016 GB', 15, 'start', LV, True))
    yb = y + 90
    sc = 620 / 4.7
    o.append(R(40, yb, 4.7 * sc, 46, PANEL, INK, 4, 2))
    o.append(R(40, yb, 2.7 * sc, 46, ACS, AC, 0, 2)); o.append(R(40 + 2.7 * sc, yb, 0.2016 * sc, 46, NXS, NX, 0, 2))
    o.append(T(40 + 1.35 * sc, yb + 28, 'MPEG-2 video 2.7 GB', 13, 'middle', AC, True))
    o.append(T(40 + 2.9016 * sc + 10, yb + 21, 'audio 0.2016 GB', 13, 'start', NX, True))
    o.append(T(40 + 2.9016 * sc + 10, yb + 38, '1.7984 GB still free', 13, 'start', MUT))
    o.append(xaxis(40, 40 + 4.7 * sc, yb + 46, [0, 1, 2, 2.9016, 4, 4.7], lambda v: 40 + v * sc, None, lambda v: f'{v:g}'))
    o.append(T(40 + 4.7 * sc, yb + 86, 'GB on a 4.7 GB single-layer DVD', 13, 'end', MUT, True))
    ym = yb + 112
    o.append(boxt(40, ym, 280, 64, ['MPEG-1, 2, 4: the media', 'compress and carry the streams'], ACS, AC, 13, bold_first=True))
    o.append(boxt(420, ym, 260, 64, ['MPEG-7: a description', 'who, what, when; no media bits'], LVS, LV, 13, bold_first=True))
    o.append(L(416, ym + 40, 324, ym + 40, LV, 2, '5 4', 'l'))
    o.append(T(370, ym + 28, 'describes', 13, 'middle', LV, True))
    return ym + 80, ''.join(o)
FIG[8] = (f8, 'An hour of MPEG-2 video at 6 Mbps is 2.7 GB and its 448 kbps audio adds 0.2016 GB, 2.9016 GB in all, well inside a 4.7 GB DVD. MPEG-7 sits beside the media as a description only; it never compresses or carries the streams.',
          'Three lines of calculation, then a bar for a 4.7 GB DVD filled with 2.7 GB of video and 0.2016 GB of audio up to 2.9016 GB, and two boxes: MPEG-1, 2 and 4 carry the media, MPEG-7 only describes it.')


# ---- 4.9 audio-video skew ----
def f9():
    o = []
    x0, x1 = 120, 680
    fx = lambda t: x0 + t / 260 * (x1 - x0)
    o.append(R(fx(40), 34, fx(200) - fx(40), 196, LVS, 'none', 0, 0))
    o.append(L(fx(40), 34, fx(40), 230, LV, 1.6, '6 4')); o.append(L(fx(200), 34, fx(200), 230, LV, 1.6, '6 4'))
    o.append(T(fx(120), 50, 'allowed window 120 ± 80 ms = 40 to 200 ms', 13, 'middle', LV, True))
    rows = [('video frame', 120, INK, ''), ('(a) audio', 150, NX, 'skew +30 ms: in sync'), ('(b) audio', 230, AC, 'skew +110 ms: out of sync')]
    for i, (lab, t, c, note) in enumerate(rows):
        yy = 90 + i * 48
        o.append(T(x0 - 12, yy + 5, lab, 13, 'end', c, True))
        o.append(L(x0, yy, x1, yy, LN, 1))
        o.append(C(fx(t), yy, 8, c))
        o.append(T(fx(t), yy - 13, f'{t} ms', 13, 'middle', c, True))
        if i:
            o.append(L(fx(120), yy, fx(t) - 10, yy, c, 2, '5 3', 'n' if c == AC else 'x'))
            o.append(Tb(fx(t) + 14, yy + 22, note, 13, 'end' if t > 200 else 'start', c, True))
    o.append(L(fx(120), 90, fx(120), 196, INK, 1.2, '2 3'))
    o.append(xaxis(x0, x1, 230, [0, 40, 80, 120, 160, 200, 240], fx, 'timestamp (ms)'))
    o.append(T(40, 300, '(b) audio is 110 ms late: hold the picture back, delay video by 110 ms if a buffer exists;', 13, 'start', INK, True))
    o.append(T(40, 320, 'otherwise drop audio samples or repeat one frame. Never skip video frames when audio is late.', 13, 'start', MUT))
    return 336, ''.join(o)
FIG[9] = (f9, 'The video frame at 120 ms may pair with audio anywhere from 40 to 200 ms. Audio at 150 ms is 30 ms off, inside the window; audio at 230 ms is 110 ms off, outside it, so the player delays the video by 110 ms.',
          'A timeline from 0 to 260 ms with a shaded window from 40 to 200 ms around the video frame at 120 ms; case (a) audio at 150 ms inside the window with skew +30 ms, case (b) audio at 230 ms outside with skew +110 ms.')


spec = make_spec(FIG)


def text_fixes(k):
    return {
        3: [('Only a few universities teach this chapter as a separate hardware-and-software survey. Figure 1 gives the working model.',
             'The figure gives the working model.'),
            ("List Figure 1's four layers.", 'List the four layers of the working model.')],
        7: [('The figure shows the encoder path.', 'The encoder path runs as follows.')],
        9: [(' Only a few universities teach this chapter.', '')],
    }.get(k, [])


def drop_sources():
    # university-hosted pages: the books name no universities
    return ['homepages.inf.ed.ac.uk']


def chapter_fix(k, ch):
    # cross-links the writer gave with single quotes or numeric anchors print as literal "<a href=...>" text: repair them
    import re
    anchors = {'4.5': 'digital-audio-and-video-file-formats', '4.9': 'synchronization-in-multimedia-presentations'}

    def fix(s):
        s = re.sub(r"<a href='(#[^']+)'>", r'<a href="\1">', s)
        return re.sub(r'<a href="#(4\.\d)">', lambda m: f'<a href="#{anchors.get(m.group(1), m.group(1))}">', s)

    def walk(x):
        if isinstance(x, dict): return {a: (b if a == 'figure' else walk(b)) for a, b in x.items()}
        if isinstance(x, list): return [walk(v) for v in x]
        return fix(x) if isinstance(x, str) else x
    return walk(ch)
