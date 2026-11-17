"""Claude's hand-drawn figures for c-mobile-u3 (Mobile Application Development, unit 3: Android user interface),
one per chapter, each drawn from that chapter's worked example with its own numbers."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def phone(x, y, w, h, title=None):
    o = R(x, y, w, h, PANEL, INK, 12, 2) + R(x + 8, y + 18, w - 16, h - 30, 'var(--fig)', L2, 4, 1)
    if title: o += T(x + w / 2, y - 10, title, 14, bold=True)
    return o


# ---- 3.1 weights 1 : 2 : 3 in a 360 dp row ----
def f1():
    o = [T(16, 24, 'A 360 dp row, three buttons with width 0dp and weights 1, 2, 3', 15, 'start', bold=True)]
    x0, x1 = 40, 680
    sc = (x1 - x0) / 360
    y = 64
    for u in range(6):
        o.append(R(x0 + u * 60 * sc, y, 60 * sc, 26, 'var(--fig)', L2, 2, 1.2, '4 3'))
        o.append(T(x0 + u * 60 * sc + 30 * sc, y + 18, '60 dp', 13, fill=MUT))
    o.append(T(x0, y - 8, 'total weight 1 + 2 + 3 = 6, so one unit = 360 ÷ 6 = 60 dp', 13, 'start', MUT))
    y = 112
    xs = x0
    for name, wgt, f, s in [('A', 1, ACS, AC), ('B', 2, LVS, LV), ('C', 3, NXS, NX)]:
        w = wgt * 60 * sc
        o.append(R(xs + 2, y, w - 4, 60, f, s, 8, 2))
        o.append(T(xs + w / 2, y + 26, f'Button {name}', 14, bold=True))
        o.append(T(xs + w / 2, y + 46, f'weight {wgt}', 13, fill=MUT))
        o.append(T(xs + w / 2, y + 92, f'{wgt * 60} dp', 15, bold=True))
        o.append(T(xs + w / 2, y + 114, f'× 3 = {wgt * 180} px', 14))
        xs += w
    o.append(xaxis(x0, x1, y + 136, [0, 60, 180, 360], lambda v: x0 + v * sc, None, lambda v: f'{v} dp'))
    o.append(T(16, y + 196, 'Check: 60 + 120 + 180 = 360 dp.   On a 480 dpi screen, density = 480 ÷ 160 = 3, so px = dp × 3.', 14, 'start'))
    return y + 212, ''.join(o)
FIG[1] = (f1, 'The weights add to 6, so each unit of the 360 dp row is 60 dp: Button A gets 60 dp, B 120 dp and C 180 dp. At density 3 (480 dpi) these are 180, 360 and 540 px.',
          'A row cut into six 60 dp units; below it three buttons, A one unit wide, B two units, C three units, labelled 60, 120 and 180 dp and 180, 360 and 540 pixels.')


# ---- 3.2 rotation: three endings ----
def f2():
    o = [T(16, 24, 'The phone rotates while the label reads "Taps: 7"', 15, 'start', bold=True)]
    o.append(phone(24, 70, 92, 150, 'before'))
    o.append(T(70, 150, 'Taps: 7', 14, bold=True))
    o.append(TM(70, 240, 'count = 7', 13))
    rows = [('(a) no saving code', 'activity destroyed, new one made', 'count = 0', 'Taps: 0', NXS, NX),
            ('(b) Bundle', 'put 7 in onSaveInstanceState, read in onCreate', 'count = 7', 'Taps: 7', LVS, LV),
            ('(c) configChanges', 'orientation|screenSize: not destroyed', 'count = 7', 'Taps: 7', LVS, LV)]
    for i, (a, b, c, lab, f, s) in enumerate(rows):
        y = 52 + i * 98
        o.append(L(124, 145, 180, y + 38, L2, 2, arrow='m'))
        o.append(R(184, y, 340, 76, PANEL, s, 8, 2))
        o.append(T(198, y + 26, a, 14, 'start', bold=True))
        o.append(T(198, y + 48, b, 13, 'start'))
        o.append(TM(198, y + 66, c, 13, 'start', MUT))
        o.append(L(526, y + 38, 562, y + 38, s, 2, arrow='x' if s == NX else 'l'))
        o.append(R(566, y + 8, 140, 60, f, s, 8, 2))
        o.append(T(636, y + 44, lab, 16, bold=True))
    o.append(T(16, 352, 'Only the Bundle copy or the configChanges declaration carries the 7 across.', 14, 'start'))
    return 368, ''.join(o)
FIG[2] = (f2, 'With no saving code the rebuilt activity starts at count = 0 and shows Taps: 0. Saving 7 in the Bundle, or declaring configChanges so the activity is not destroyed, keeps Taps: 7.',
          'A phone showing Taps: 7 branches into three outcomes: no saving code gives Taps: 0, the Bundle gives Taps: 7, and configChanges gives Taps: 7.')


# ---- 3.3 3 action slots, 5 menu items ----
def f3():
    o = [T(16, 24, 'menu.xml has five items; the Toolbar has room for 3 action slots', 15, 'start', bold=True)]
    items = [('Search', 'always', 'bar'), ('Share', 'ifRoom', 'bar'), ('Edit', 'ifRoom', 'bar'), ('Delete', 'ifRoom', 'over'), ('Settings', 'never', 'over')]
    for i, (n, m, where) in enumerate(items):
        y = 50 + i * 44
        o.append(R(16, y, 250, 34, PANEL, AC if where == 'bar' else NX, 6, 1.5))
        o.append(T(28, y + 22, n, 14, 'start', bold=True))
        o.append(TM(254, y + 22, f'showAsAction={m}', 12, 'end', MUT))
    # toolbar
    o.append(R(370, 50, 334, 52, AC, AC, 6, 2))
    o.append(T(382, 82, 'App', 15, 'start', 'var(--fig)', True))
    for i, s_ in enumerate(['Search', 'Share', 'Edit']):
        o.append(R(424 + i * 82, 60, 76, 32, ACS, ACS, 5, 1))
        o.append(T(462 + i * 82, 81, s_, 13, bold=True))
    o.append(T(688, 85, '⋮', 22, fill='var(--fig)', bold=True))
    o.append(R(560, 140, 144, 84, PANEL, NX, 6, 2))
    o.append(T(574, 170, 'Delete', 14, 'start')); o.append(T(574, 204, 'Settings', 14, 'start'))
    o.append(L(688, 100, 688, 138, NX, 2, arrow='x'))
    o.append(T(556, 250, 'overflow: 2 items', 13, 'start', NX, True))
    for i, (tag, c) in enumerate([('→ slot 1', AC), ('→ slot 2', AC), ('→ slot 3', AC), ('→ overflow', NX), ('→ overflow', NX)]):
        o.append(T(274, 72 + i * 44, tag, 13, 'start', c, True))
    o.append(T(16, 296, 'always takes a slot first; ifRoom items fill what is left (Delete finds 0 free); never always overflows.', 14, 'start'))
    return 312, ''.join(o)
FIG[3] = (f3, 'Search (always) takes slot 1, Share and Edit (ifRoom) take slots 2 and 3, and Delete finds no free slot. Delete and Settings (never) go to the overflow list: 3 items on the bar, 2 in overflow.',
          'Five menu items listed with their showAsAction values; arrows send Search, Share and Edit to three slots on a toolbar, and Delete and Settings to the overflow list under the three-dot button.')


# ---- 3.4 one adapter, a ListView and a Spinner ----
def f4():
    data = ['Fig', 'Plum', 'Pear', 'Kiwi', 'Lime']
    o = [T(16, 24, 'One ArrayAdapter feeds both views; indices start at 0', 15, 'start', bold=True)]
    for i, d in enumerate(data):
        y = 50 + i * 38
        hi = i == 2
        o.append(R(16, y, 140, 32, ACS if hi else PANEL, AC, 5, 1.5))
        o.append(T(30, y + 21, str(i), 13, 'start', MUT)); o.append(T(96, y + 21, f'"{d}"', 14, bold=hi))
    o.append(T(86, 258, 'data array', 13, fill=MUT))
    o.append(boxt(186, 118, 110, 54, ['ArrayAdapter', 'makes rows'], LVS, LV, 13, bold_first=True))
    o.append(L(158, 145, 182, 145, LV, 2, arrow='l'))
    # list view
    o.append(R(330, 46, 170, 206, PANEL, INK, 8, 2))
    for i, d in enumerate(data):
        y = 54 + i * 38
        hi = i == 2
        o.append(R(338, y, 154, 32, AC if hi else 'var(--fig)', AC if hi else L2, 4, 1))
        o.append(T(350, y + 21, d, 14, 'start', 'var(--fig)' if hi else INK, hi))
    o.append(T(415, 270, 'ListView', 13, fill=MUT))
    o.append(L(298, 140, 326, 110, LV, 2, arrow='l'))
    o.append(L(500, 145, 530, 145, AC, 2, arrow='n'))
    o.append(boxt(534, 108, 170, 74, ['tap row 3', 'position = 2', 'item → "Pear"'], ACS, AC, 13, bold_first=True))
    # spinner
    y = 300
    o.append(L(240, 172, 240, y - 2, LV, 2, arrow='l'))
    o.append(R(186, y, 170, 36, PANEL, INK, 6, 2)); o.append(T(200, y + 23, 'Kiwi', 14, 'start', bold=True)); o.append(T(340, y + 23, '▾', 14, 'end'))
    o.append(T(271, y + 54, 'Spinner', 13, fill=MUT))
    o.append(L(360, y + 18, 396, y + 18, AC, 2, arrow='n'))
    o.append(R(400, y - 8, 304, 52, ACS, AC, 8, 2))
    o.append(TM(412, y + 12, 'setSelection(3): 0 → 3', 13, 'start'))
    o.append(TM(412, y + 34, 'position 3, item "Kiwi"', 13, 'start'))
    return y + 66, ''.join(o)
FIG[4] = (f4, 'The five strings sit at indices 0 to 4. Tapping the third row reaches onItemClick with position 2, and getItemAtPosition(2) is "Pear"; the same adapter fills a Spinner, where setSelection(3) gives position 3 and "Kiwi".',
          'A data array Fig, Plum, Pear, Kiwi, Lime with indices 0 to 4 feeds an ArrayAdapter, which fills a ListView with the third row highlighted as position 2, Pear, and a Spinner set to index 3, Kiwi.')


# ---- 3.5 fitCenter against centerCrop ----
def f5():
    s = 0.3
    o = [T(16, 24, 'View 400 × 300 px, bitmap 200 × 600 px (drawn at 0.3 scale)', 15, 'start', bold=True)]
    # fitCenter
    vx, vy, vw, vh = 110, 200, 400 * s, 300 * s
    o.append(T(vx + vw / 2, 145, 'fitCenter', 15, bold=True))
    o.append(T(vx + vw / 2, 165, 'scale = min(2, 0.5) = 0.5', 13, fill=MUT))
    o.append(R(vx, vy, vw, vh, 'var(--fig)', INK, 2, 2))
    bw, bh = 100 * s, 300 * s
    o.append(R(vx + (vw - bw) / 2, vy, bw, bh, ACS, AC, 2, 2))
    o.append(T(vx + 22, vy + vh / 2 + 5, '150', 12, fill=NX, bold=True)); o.append(T(vx + vw - 22, vy + vh / 2 + 5, '150', 12, fill=NX, bold=True))
    o.append(T(vx + vw / 2, vy + vh + 26, 'image drawn 100 × 300 px, all of it shows;', 13))
    o.append(T(vx + vw / 2, vy + vh + 44, '150 px blank left and right', 13, fill=NX))
    # centerCrop
    cx, cy = 470, 200
    o.append(T(cx - 14, 90, 'centerCrop', 15, 'end', bold=True))
    o.append(T(cx - 14, 110, 'scale = max(2, 0.5) = 2', 13, 'end', MUT))
    bh2 = 1200 * s
    top = cy + vh / 2 - bh2 / 2
    # the drawn bitmap is clipped: show the cut parts faint
    o.append(R(cx, top, vw, (bh2 - vh) / 2, NXS, NX, 2, 1.5, '5 4'))
    o.append(R(cx, cy + vh, vw, (bh2 - vh) / 2, NXS, NX, 2, 1.5, '5 4'))
    o.append(R(cx, cy, vw, vh, ACS, INK, 2, 2.5))
    o.append(T(cx + vw / 2, cy + vh / 2 + 5, 'visible 400×300', 11))
    o.append(T(cx + vw + 12, top + (bh2 - vh) / 4 + 5, '450 px cut', 13, 'start', NX, True))
    o.append(T(cx + vw + 12, cy + vh + (bh2 - vh) / 4 + 5, '450 px cut', 13, 'start', NX, True))
    o.append(T(cx - 12, cy + vh / 2 - 4, 'drawn', 13, 'end', MUT)); o.append(T(cx - 12, cy + vh / 2 + 14, '400×1200', 13, 'end', MUT))
    return top + bh2 + 20, ''.join(o)
FIG[5] = (f5, 'fitCenter shrinks the 200 × 600 bitmap by 0.5 to 100 × 300 px, so the whole picture shows with 150 px blank on each side. centerCrop enlarges it by 2 to 400 × 1200 px, filling the view and cutting 450 px from the top and from the bottom.',
          'Two 400 by 300 view boxes: on the left a narrow image in the middle with blank bands of 150 pixels each side; on the right the view filled, with dashed parts of 450 pixels above and below that are cut off.')


# ---- 3.6 buttons built in Java, one listener ----
def f6():
    o = [T(16, 24, 'LinearLayout built in Java: 3 buttons, width 0, weight 1, ids 100 + i', 15, 'start', bold=True)]
    x0, x1, y = 40, 680, 56
    w = (x1 - x0) / 3
    o.append(R(x0 - 6, y - 6, x1 - x0 + 12, 72, PANEL, L2, 8, 1.5))
    for i in range(3):
        hi = i == 1
        o.append(R(x0 + i * w + 4, y, w - 8, 60, AC if hi else ACS, AC, 8, 2))
        f = 'var(--fig)' if hi else INK
        o.append(T(x0 + i * w + w / 2, y + 26, f'i = {i}, id {100 + i}', 14, fill=f, bold=True))
        o.append(T(x0 + i * w + w / 2, y + 46, '120 dp = 360 px', 13, fill=f))
    o.append(T((x0 + x1) / 2, y + 90, '360 dp ÷ 3 = 120 dp each;  120 × density 3 = 360 px', 14))
    # touch path
    y2 = 190
    o.append(T(16, y2, 'The user taps the second button. The touch travels one fixed path:', 14, 'start', bold=True))
    steps = ['dispatch-', 'onTouch-', 'perform-', 'your']
    steps2 = ['TouchEvent', 'Event', 'Click', 'onClick(v)']
    for i in range(4):
        x = 16 + i * 176
        o.append(R(x, y2 + 16, 150, 56, LVS if i == 3 else PANEL, LV if i == 3 else AC, 8, 2))
        o.append(TM(x + 75, y2 + 40, steps[i], 13)); o.append(TM(x + 75, y2 + 60, steps2[i], 13))
        if i < 3: o.append(L(x + 152, y2 + 44, x + 172, y2 + 44, AC, 2, arrow='n'))
    o.append(R(16, y2 + 92, 688, 52, ACS, AC, 8, 1.5))
    o.append(TM(30, y2 + 114, 'v.getId() = 101', 14, 'start', bold=True))
    o.append(TM(30, y2 + 134, 'index = v.getId() − 100 = 101 − 100 = 1', 14, 'start'))
    return y2 + 156, ''.join(o)
FIG[6] = (f6, 'Three weight-1 buttons share the 360 dp row, 120 dp (360 px) each. A tap on the second passes dispatchTouchEvent, onTouchEvent and performClick, and the shared listener gets the View with id 101, so the index is 1.',
          'A row of three equal buttons with ids 100, 101 and 102, each 120 dp; the middle one is tapped; four boxes show the touch path ending in onClick, which reads id 101 and index 1.')


spec = make_spec(FIG)


def text_fixes(k):
    return {
        1: [('The activity window holds exactly one root ViewGroup. Everything else is a descendant.',
             'Each layout file has one root view, usually a ViewGroup, which the window places inside its own content frame. Everything else is a descendant.'),
            ('dpi is the screen density in dots per inch.',
             'dpi is the density value Android reports for the screen (160, 320, 480 and so on), not the panel\'s measured dots per inch.'),
            ('<code>gravity</code> centres a layout\'s own children, while <code>layout_gravity</code> places that view inside its parent.',
             '<code>gravity</code> positions a view\'s own content (a layout\'s children, a button\'s text), while <code>layout_gravity</code> places that view inside its parent.')],
        2: [(' Only a few universities teach this in full.', '')],
        5: [(' Only a few universities teach this group in detail.', '')],
        6: [(' Only a few universities teach programmatic UI; it is worth knowing because it makes sizes, weights and listeners explicit.',
             ' Programmatic UI is worth knowing because it makes sizes, weights and listeners explicit.')],
    }.get(k, [])


# sentences removed outright go through chapter_fix, which is idempotent, so the module can be applied again
_tf_all = text_fixes
_cf_prev = globals().get('chapter_fix')


def text_fixes(k):
    return [(a, b) for a, b in _tf_all(k) if b]


def chapter_fix(k, ch):
    import json
    if _cf_prev: ch = _cf_prev(k, ch) or ch
    raw = json.dumps(ch, ensure_ascii=False)
    for a, b in _tf_all(k):
        if not b: raw = raw.replace(json.dumps(a, ensure_ascii=False)[1:-1], '')
    return json.loads(raw)
