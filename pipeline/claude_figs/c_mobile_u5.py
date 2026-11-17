"""Claude's hand-drawn figures for c-mobile-u5 (Mobile Application Development, unit 5: messaging, maps, location,
security, publishing and m-commerce), one per chapter, each drawn from that chapter's worked example with its own numbers."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


# ---- 5.1 a 320-character SMS in parts ----
def f1():
    o = [T(16, 24, 'A 320-character SMS, 7-bit GSM: one part carries 160, a joined part only 153', 15, 'start', bold=True)]
    x0, x1 = 40, 680
    sc = (x1 - x0) / 320
    y = 64
    o.append(R(x0, y, 320 * sc, 34, PANEL, L2, 4, 1.5))
    o.append(T((x0 + x1) / 2, y + 22, 'message: 320 characters', 14, bold=True))
    o.append(T(x0, y + 56, 'divideMessage()', 13, 'start', MUT))
    y = 136
    xs = x0
    sc = (x1 - x0 - 12) / 341
    for i, n in enumerate([153, 153, 14]):
        w = n * sc
        o.append(R(xs + 2, y, 7 * sc, 34, NXS, NX, 3, 1.5))
        o.append(R(xs + 2 + 7 * sc, y, w - 4, 34, ACS, AC, 3, 1.5))
        o.append(T(xs + 7 * sc + w / 2, y + 22, f'{n}' if n < 20 else f'part {i + 1}: {n} chars', 13, bold=True))
        o.append(T(xs + 7 * sc + w / 2, y + 56, '₹0.20', 14, fill=NX if False else INK))
        xs += w + 7 * sc + 6
    o.append(T(x0, y + 82, 'Each part also carries a 6-byte header that takes the room of 7 characters (narrow block).', 13, 'start', MUT))
    o.append(T(16, y + 120, 'Parts = ⌈320 ÷ 153⌉ = ⌈2.09⌉ = 3.     Cost = 3 × ₹0.20 = ₹0.60.', 15, 'start', bold=True))
    o.append(T(16, y + 144, 'The phone at the other end joins the 3 parts back into one message.', 14, 'start'))
    return y + 158, ''.join(o)
FIG[1] = (f1, 'A joined SMS part carries 153 characters, because its header takes the room of 7. So 320 characters need ⌈320 ÷ 153⌉ = 3 parts, 153 + 153 + 14, billed at ₹0.20 each for ₹0.60.',
          'A bar of 320 characters split into three parts of 153, 153 and 14 characters, each with a small header block and a price of 0.20 rupees, totalling 0.60 rupees.')


# ---- 5.2 three markers and the camera centre ----
def f2():
    o = [T(16, 24, 'Three shop markers; where should the camera look?', 15, 'start', bold=True)]
    x0, x1, y0, y1 = 120, 520, 60, 380
    fx = lambda lon: x0 + (lon - 76.95) / 0.3 * (x1 - x0)
    fy = lambda lat: y1 - (lat - 11.85) / 0.3 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [77.0, 77.1, 77.2], [11.9, 12.0, 12.1], fx, fy, 'longitude (°E)', 'latitude (°N)', lambda v: f'{v:.1f}', lambda v: f'{v:.1f}'))
    o.append(R(fx(77.0), fy(12.1), fx(77.2) - fx(77.0), fy(11.9) - fy(12.1), ACS, AC, 2, 2, '7 5'))
    for lat, lon in [(12.0, 77.0), (12.1, 77.2), (11.9, 77.1)]:
        X, Y = fx(lon), fy(lat)
        o.append(f'<path d="M{X:.1f},{Y:.1f} l-9,-18 a10,10 0 1,1 18,0 z" style="fill:{NX};stroke:var(--fig);stroke-width:1.5"/>')
        o.append(Tb(X + (14 if lon < 77.2 else -14), Y + 8, f'({lat}, {lon})', 13, 'start' if lon < 77.2 else 'end', bold=True))
    cx, cy = fx(77.1), fy(12.0)
    o.append(L(cx - 12, cy, cx + 12, cy, LV, 3)); o.append(L(cx, cy - 12, cx, cy + 12, LV, 3))
    o.append(Tb(cx + 16, cy - 10, 'camera (12.0, 77.1)', 13, 'start', LV, True))
    # side panel
    X = 548
    o.append(R(X - 6, 70, 168, 210, PANEL, L2, 8, 1.5))
    rows = [('lat centre', '(12.1 + 11.9) ÷ 2', '= 12.0'), ('lon centre', '(77.2 + 77.0) ÷ 2', '= 77.1'), ('spans', '0.2° by 0.2°', '≈ 22 km tall')]
    for i, (a, b, c) in enumerate(rows):
        o.append(T(X + 6, 96 + i * 66, a, 14, 'start', bold=True))
        o.append(T(X + 6, 116 + i * 66, b, 13, 'start'))
        o.append(T(X + 6, 134 + i * 66, c, 13, 'start', AC, True))
    return 430, ''.join(o)
FIG[2] = (f2, 'The three markers fit a box from 11.9° to 12.1° north and 77.0° to 77.2° east, 0.2° each way (about 22 km north to south). The camera goes to the box centre, LatLng(12.0, 77.1).',
          'A small latitude-longitude plot with three map pins at (12.0, 77.0), (12.1, 77.2) and (11.9, 77.1), a dashed box around them, and a cross at the centre (12.0, 77.1) marking the camera.')


# ---- 5.3 20 s ticks and 100 m steps ----
def f3():
    o = [T(16, 24, 'Request: every 20 s, minimum 100 m. The rider moves at 18 km/h = 5 m/s.', 15, 'start', bold=True)]
    x0, x1 = 60, 660
    fx = lambda t: x0 + t / 60 * (x1 - x0)
    y = 120
    o.append(L(x0 - 20, y, x1 + 30, y, L2, 6))
    for i, t in enumerate([0, 20, 40, 60]):
        X = fx(t)
        o.append(C(X, y, 10, AC if i else L2))
        if i:
            o.append(T(X, y - 22, f'fix {i}', 14, fill=AC, bold=True))
            o.append(P([(fx(t - 20) + 14, y + 26), (fx(t - 20) + 14, y + 34), (X - 14, y + 34), (X - 14, y + 26)], LV, 2))
            o.append(T((fx(t - 20) + X) / 2, y + 54, '5 m/s × 20 s = 100 m', 13, fill=LV, bold=True))
        else:
            o.append(T(X, y - 22, 'start', 14, fill=MUT))
    o.append(xaxis(x0, x1, 210, [0, 20, 40, 60], fx, 'time (s)', lambda v: f'{v} s'))
    o.append(xaxis(x0, x1, 280, [0, 20, 40, 60], fx, None, lambda v: f'{v * 5} m'))
    o.append(T(x0 - 10, 274, 'distance', 13, 'end', MUT))
    o.append(T(16, 344, '100 m is not less than the 100 m filter, so the distance test passes at every tick:', 14, 'start'))
    o.append(T(16, 366, 'the 20 s timer decides, and a minute holds at most 60 ÷ 20 = 3 updates.', 14, 'start', bold=True))
    return 380, ''.join(o)
FIG[3] = (f3, 'At 5 m/s the rider covers exactly 100 m in each 20 s tick, so the distance filter never holds a fix back. The 20 s timer decides, giving at most 60 ÷ 20 = 3 updates a minute.',
          'A road with the rider at 0, 100, 200 and 300 metres at 0, 20, 40 and 60 seconds, a fix at each tick, and brackets of 100 m between them; two scales give time and distance.')


# ---- 5.4 4-digit PIN with and without lockout ----
def f4():
    o = [T(16, 24, 'Trying all 10⁴ = 10,000 four-digit PINs at 10 guesses per second', 15, 'start', bold=True)]
    x0, x1 = 160, 680
    sc = (x1 - x0) / 61000
    y = 60
    o.append(T(x0 - 12, y + 22, 'no lockout', 14, 'end', bold=True))
    o.append(R(x0, y, max(1000 * sc, 6), 32, ACS, AC, 3, 2))
    o.append(T(x0 + 18, y + 22, '1,000 s = 16 min 40 s', 14, 'start', AC, True))
    y = 120
    o.append(T(x0 - 12, y + 22, 'lock 30 s', 14, 'end', bold=True))
    o.append(T(x0 - 12, y + 40, 'every 5 wrong', 13, 'end', MUT))
    o.append(R(x0, y, 1000 * sc, 32, ACS, AC, 3, 2))
    o.append(R(x0 + 1000 * sc, y, 60000 * sc, 32, NXS, NX, 3, 2))
    o.append(T(x0 + 30000 * sc, y + 22, 'locked: 2,000 × 30 s = 60,000 s', 14, bold=True))
    o.append(xaxis(x0, x1, y + 50, [0, 20000, 40000, 61000], lambda v: x0 + v * sc, None, lambda v: f'{v:,} s'))
    o.append(T(x1, y + 104, 'total 61,000 s ≈ 16.94 h', 15, 'end', NX, True))
    # one cycle zoom
    y = 270
    o.append(T(16, y, 'One cycle, repeated 10,000 ÷ 5 = 2,000 times:', 14, 'start', bold=True))
    for i in range(5):
        o.append(R(16 + i * 44, y + 14, 38, 30, ACS, AC, 4, 1.5)); o.append(T(35 + i * 44, y + 34, '0.1 s', 12))
    o.append(R(240, y + 14, 300, 30, NXS, NX, 4, 1.5)); o.append(T(390, y + 34, 'wait 30 s', 13, bold=True))
    o.append(T(556, y + 34, '5 guesses, then a lock', 13, 'start', MUT))
    o.append(T(16, y + 72, 'The lockout adds no guesses, only waiting: guessing time stays 1,000 s.', 14, 'start'))
    return y + 86, ''.join(o)
FIG[4] = (f4, 'With no lockout, 10,000 guesses at 10 a second take 1,000 s (16 min 40 s). A 30 s lock after every 5 wrong guesses adds 2,000 × 30 = 60,000 s of waiting, 61,000 s ≈ 16.94 h in all.',
          'Two bars on one time scale: a thin 1,000 second bar with no lockout, and a long bar of 1,000 seconds guessing plus 60,000 seconds locked; below, one cycle of five quick guesses and a 30 second wait.')


# ---- 5.5 a patch release ----
def f5():
    o = [T(16, 24, 'One patch update: two bug fixes, nothing new', 15, 'start', bold=True)]
    o.append(R(16, 44, 330, 120, PANEL, AC, 8, 2))
    o.append(T(30, 68, 'versionCode (machine counter)', 14, 'start', bold=True))
    o.append(T(30, 104, '7', 26, 'start', MUT, True)); o.append(L(60, 96, 110, 96, AC, 2.5, arrow='n')); o.append(T(120, 104, '8', 26, 'start', AC, True))
    o.append(T(160, 102, 'must rise on every upload', 13, 'start', MUT))
    o.append(R(374, 44, 330, 120, PANEL, AC, 8, 2))
    o.append(T(388, 68, 'versionName (label users see)', 14, 'start', bold=True))
    o.append(TM(388, 104, '1.2.3', 22, 'start', MUT, True)); o.append(L(468, 96, 506, 96, AC, 2.5, arrow='n')); o.append(TM(514, 104, '1.2.', 22, 'start', INK, True))
    o.append(TM(570, 104, '4', 22, 'start', AC, True))
    o.append(T(388, 146, 'a patch raises only the last number', 13, 'start', MUT))
    steps = [('build', 'release'), ('shrink', 'R8'), ('sign', 'release key'), ('test', 'signed APK'), ('deploy', 'store')]
    y = 196
    for i, (a, b) in enumerate(steps):
        x = 16 + i * 140
        o.append(boxt(x, y, 120, 54, [a, b], ACS if a in ('sign', 'test') else PANEL, AC, 14, bold_first=True))
        if i < 4: o.append(L(x + 122, y + 27, x + 136, y + 27, AC, 2, arrow='n'))
    o.append(T(16, y + 80, 'Sign before test: the bytes you test are the bytes you ship.', 14, 'start'))
    o.append(R(16, y + 98, 688, 50, NXS, NX, 8, 1.5))
    o.append(T(30, y + 120, 'Upload with versionCode 7 again: rejected, the store already holds 7 for this package;', 14, 'start', NX, True))
    o.append(T(30, y + 140, 'a phone on 7 would never see it as an update.', 14, 'start', NX))
    return y + 160, ''.join(o)
FIG[5] = (f5, 'The patch raises versionCode 7 → 8 and versionName 1.2.3 → 1.2.4, then the app is built, shrunk, signed and tested as signed before it ships. Re-uploading versionCode 7 is rejected because a code must be greater than every code already accepted.',
          'Two boxes showing versionCode going from 7 to 8 and versionName from 1.2.3 to 1.2.4; a row of five steps, build, shrink, sign, test and deploy; a warning that versionCode 7 cannot be uploaded again.')


# ---- 5.6 one ₹1,200 order, card against UPI ----
def f6():
    o = [T(16, 24, 'A ₹1,200 order travels the payment chain', 15, 'start', bold=True)]
    parties = [('Customer', 'taps Pay'), ('Merchant app', 'creates order'), ('Gateway', 'forwards'), ('Bank', 'approves')]
    for i, (a, b) in enumerate(parties):
        x = 16 + i * 176
        o.append(boxt(x, 44, 150, 54, [a, b], PANEL, AC, 14, bold_first=True))
        if i < 3:
            o.append(L(x + 152, 62, x + 172, 62, AC, 2, arrow='n'))
            o.append(L(x + 172, 82, x + 152, 82, LV, 2, arrow='l'))
    o.append(T(16, 122, 'request goes right, the answer comes back left', 13, 'start', MUT))
    x0, x1 = 120, 680
    sc = (x1 - x0) / 1200
    for j, (lab, fee, note) in enumerate([('card', 27, '2% + ₹3 = ₹24 + ₹3 = ₹27'), ('UPI', 0, '0%: fee ₹0')]):
        y = 156 + j * 76
        o.append(T(x0 - 12, y + 24, lab, 15, 'end', bold=True))
        o.append(R(x0, y, (1200 - fee) * sc, 36, LVS, LV, 3, 2))
        o.append(T(x0 + 12, y + 24, f'merchant keeps ₹{1200 - fee:,}', 14, 'start', bold=True))
        if fee:
            o.append(R(x0 + (1200 - fee) * sc, y, fee * sc, 36, NXS, NX, 3, 2))
            o.append(T(x1, y + 54, f'gateway fee {note}', 13, 'end', NX, True))
        else:
            o.append(T(x1, y + 54, note, 13, 'end', MUT))
    o.append(T(16, 330, '500 card orders × ₹27 = ₹13,500 in gateway fees.', 15, 'start', bold=True))
    return 346, ''.join(o)
FIG[6] = (f6, 'The order passes customer, merchant app, gateway and bank, and the answer returns the same way. On a card the gateway keeps 2% + ₹3 = ₹27, leaving ₹1,173; on UPI the merchant keeps all ₹1,200, and 500 card orders cost ₹13,500 in fees.',
          'Four boxes, customer, merchant app, gateway and bank, with arrows each way; below, two bars of 1,200 rupees: the card bar ends in a small 27 rupee fee slice, the UPI bar is all kept by the merchant.')


spec = make_spec(FIG)


def text_fixes(k):
    return {
        1: [(' Only a few universities teach this chapter; some syllabi call it SMS messaging and sending e-mail.',
             ' Some syllabi call it SMS messaging and sending e-mail.')],
        2: [('new LatLng(77.0, 12.0) puts a Chennai shop near the North Pole and the map still draws',
             'new LatLng(77.0, 12.0) moves a shop near Bengaluru (12.0° N, 77.0° E) into the Arctic, and the map still draws')],
    }.get(k, [])


DROP = {2: [' Only a few universities teach this.'], 3: [' Only a few universities teach this chapter.']}


def chapter_fix(k, ch):
    # sentences removed outright (idempotent, so the module can be applied again)
    import json
    raw = json.dumps(ch, ensure_ascii=False)
    for d in DROP.get(k, []):
        raw = raw.replace(json.dumps(d, ensure_ascii=False)[1:-1], '')
    return json.loads(raw)
