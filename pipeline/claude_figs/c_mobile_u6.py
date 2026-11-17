"""Claude's hand-drawn figures for c-mobile-u6 (Mobile Application Development, unit 6: iOS with Swift and UIKit),
one per chapter, each drawn from that chapter's worked example with its own numbers."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def mono_box(x, y, w, h, lines, fill=PANEL, stroke=AC, size=13, title=None):
    o = [R(x, y, w, h, fill, stroke, 8, 2)]
    yy = y + 22
    if title:
        o.append(T(x + 12, yy, title, 14, 'start', bold=True)); yy += 22
    for i, s in enumerate(lines):
        o.append(TM(x + 12, yy + i * 20, s, size, 'start'))
    return ''.join(o)


# ---- 6.1 Int and Double in one fare ----
def f1():
    o = [T(16, 24, 'Cab fare for 8 km: ₹20 booking fee + ₹9.0 per km', 15, 'start', bold=True)]
    decl = [('let baseFare: Double = 20.0', 'Double'), ('let rate = 9.0', 'Double (inferred)'), ('let km = 8', 'Int (inferred)')]
    for i, (c, t) in enumerate(decl):
        y = 46 + i * 44
        o.append(R(16, y, 300, 34, PANEL, AC if i < 2 else NX, 6, 1.5))
        o.append(TM(28, y + 22, c, 13, 'start'))
        o.append(T(326, y + 22, t, 13, 'start', AC if i < 2 else NX, True))
    # wrong path
    o.append(R(470, 46, 234, 78, NXS, NX, 8, 2, '6 4'))
    o.append(TM(484, 72, 'km * rate', 14, 'start', bold=True))
    o.append(T(484, 94, 'Int × Double:', 13, 'start'))
    o.append(T(484, 112, 'compile error, build stops', 13, 'start', NX, True))
    # right path
    y = 200
    steps = [('Double(km)', '8 → 8.0'), ('× rate', '8.0 × 9.0 = 72.0'), ('+ baseFare', '20.0 + 72.0 = 92.0')]
    for i, (a, b) in enumerate(steps):
        x = 16 + i * 236
        o.append(R(x, y, 210, 62, ACS if i < 2 else LVS, AC if i < 2 else LV, 8, 2))
        o.append(TM(x + 105, y + 26, a, 14, bold=True)); o.append(T(x + 105, y + 48, b, 14))
        if i < 2: o.append(L(x + 212, y + 31, x + 232, y + 31, AC, 2, arrow='n'))
    o.append(L(110, 182, 110, 196, AC, 2, arrow='n'))
    o.append(T(16, 296, 'Total fare: 92.0 rupees.   Int("8") gives Optional(8); Int("eight") gives nil.', 14, 'start'))
    return 312, ''.join(o)
FIG[1] = (f1, 'rate is a Double and km an Int, so km * rate stops the build. Converting first, Double(8) = 8.0, gives 8.0 × 9.0 = 72.0 and a total of 20.0 + 72.0 = 92.0 rupees.',
          'Three declarations, two Doubles and one Int; a dashed box shows km times rate failing to compile; a row of three boxes converts 8 to 8.0, multiplies to 72.0 and adds 20.0 to reach 92.0.')


# ---- 6.2 two calls through one branch ----
def f2():
    o = [T(16, 24, 'fareLabel(km:) traced for 8 km and 12 km', 15, 'start', bold=True)]
    o.append(TM(16, 52, 'rate = km <= 10 ? 9.0 : 11.5     fare = 20 + km * rate', 13, 'start', MUT))
    for j, (km, ok, rate, fare, lab, c, cs) in enumerate([(8, True, '9.0', '20 + 8 × 9.0 = 92.0', 'Short trip: ₹92.0', ACS, AC),
                                                           (12, False, '11.5', '20 + 12 × 11.5 = 158.0', 'Long trip: ₹158.0', LVS, LV)]):
        y = 76 + j * 112
        o.append(boxt(16, y, 110, 70, [f'call {j + 1}', f'km = {km}'], PANEL, cs, 14, bold_first=True))
        o.append(L(128, y + 35, 154, y + 35, cs, 2, arrow='n' if cs == AC else 'l'))
        o.append(f'<polygon points="{158},{y + 35} {228},{y} {298},{y + 35} {228},{y + 70}" style="fill:var(--panel);stroke:{cs};stroke-width:2"/>')
        o.append(T(228, y + 32, f'{km} ≤ 10?', 14, bold=True)); o.append(T(228, y + 50, 'true' if ok else 'false', 13, fill=cs, bold=True))
        o.append(L(300, y + 35, 326, y + 35, cs, 2, arrow='n' if cs == AC else 'l'))
        o.append(boxt(330, y + 4, 110, 62, ['rate', rate], c, cs, 14, bold_first=True))
        o.append(L(442, y + 35, 462, y + 35, cs, 2, arrow='n' if cs == AC else 'l'))
        o.append(R(466, y + 4, 238, 62, c, cs, 8, 2))
        o.append(T(585, y + 28, fare, 14)); o.append(T(585, y + 52, f'"{lab}"', 14, bold=True))
    o.append(T(16, 318, 'The same function, two inputs: the condition alone picks the rate.', 14, 'start'))
    return 334, ''.join(o)
FIG[2] = (f2, 'For 8 km the test 8 ≤ 10 is true, so the rate is 9.0 and the label reads Short trip: ₹92.0; for 12 km it is false, so the rate is 11.5 and the label reads Long trip: ₹158.0.',
          'Two rows, one per call: km 8 goes through a diamond 8 ≤ 10 true to rate 9.0 and fare 92.0; km 12 goes through false to rate 11.5 and fare 158.0.')


# ---- 6.3 copy, share and override ----
def f3():
    o = [T(16, 24, 'struct copies, class shares', 15, 'start', bold=True)]
    o.append(TM(16, 52, 'var b = a;  b.km = 12', 13, 'start', MUT))
    for i, (n, v) in enumerate([('a', '8'), ('b', '12')]):
        y = 66 + i * 64
        o.append(T(30, y + 30, n, 16, 'start', bold=True))
        o.append(L(48, y + 25, 80, y + 25, AC, 2, arrow='n'))
        o.append(R(84, y, 150, 50, ACS if i == 0 else LVS, AC if i == 0 else LV, 8, 2))
        o.append(TM(159, y + 31, f'Trip km = {v}', 14, bold=True))
    o.append(T(16, 210, 'two separate copies: a.km stays 8', 13, 'start', AC))
    o.append(TM(16, 246, 'let c1 = Cab();  let c2 = c1', 13, 'start', MUT))
    o.append(T(30, 282, 'c1', 15, 'start', bold=True)); o.append(T(30, 324, 'c2', 15, 'start', bold=True))
    o.append(L(56, 277, 120, 292, NX, 2, arrow='x')); o.append(L(56, 319, 120, 306, NX, 2, arrow='x'))
    o.append(R(124, 272, 110, 50, NXS, NX, 8, 2)); o.append(T(179, 302, 'one Cab', 14, bold=True))
    o.append(T(16, 352, 'one shared object: a change via c1 shows via c2', 13, 'start', NX))
    # override
    X = 300
    o.append(T(X, 24, 'Cab overrides Ride.fare(km:)', 15, 'start', bold=True))
    o.append(R(X, 46, 404, 112, PANEL, AC, 8, 2))
    o.append(T(X + 14, 70, 'class Ride', 14, 'start', bold=True))
    o.append(TM(X + 14, 96, 'fare(km: 8) = 20 + 8 × 9.0', 13, 'start'))
    o.append(T(X + 390, 140, '₹92.0', 18, 'end', AC, True))
    o.append(L(X + 200, 160, X + 200, 190, L2, 2, arrow='m'))
    o.append(T(X + 210, 182, 'subclass', 12, 'start', MUT))
    o.append(R(X, 194, 404, 112, NXS, NX, 8, 2))
    o.append(T(X + 14, 218, 'class Cab: Ride', 14, 'start', bold=True))
    o.append(TM(X + 14, 244, 'override fare(km: 8)', 13, 'start'))
    o.append(TM(X + 14, 264, '  = super.fare(km: 8) + 15', 13, 'start'))
    o.append(T(X + 390, 290, '92.0 + 15 = ₹107.0', 18, 'end', NX, True))
    return 366, ''.join(o)
FIG[3] = (f3, 'Copying the struct gives b its own Trip, so b.km = 12 leaves a.km at 8, while two variables holding one Cab share it. Ride charges 20 + 8 × 9.0 = ₹92.0 for 8 km; Cab overrides fare to add ₹15, giving ₹107.0.',
          'Left, a and b point to two separate Trip boxes with km 8 and km 12, and c1 and c2 point to one Cab box; right, a Ride box computing 92.0 and a Cab subclass box adding 15 for 107.0.')


# ---- 6.4 build, install, run, crash ----
def f4():
    o = [T(16, 24, 'The build succeeds; the crash comes only when the bad line runs', 15, 'start', bold=True)]
    st = [('edit', 'PANEL'), ('build', 'ok'), ('install', 'ok'), ('run', 'ok'), ('crash', 'x')]
    for i, (s, k) in enumerate(st):
        x = 16 + i * 140
        bad = k == 'x'
        o.append(boxt(x, 44, 120, 44, [s], NXS if bad else (ACS if k == 'ok' else PANEL), NX if bad else AC, 14, bold_first=True))
        if i < 4: o.append(L(x + 122, 66, x + 136, 66, AC, 2, arrow='n'))
    o.append(T(76 + 140, 106, 'compile errors stop here', 12, fill=MUT))
    o.append(T(76 + 4 * 140, 106, 'runtime, not build', 12, fill=NX, bold=True))
    o.append(TM(16, 148, 'let fares = [92, 158, 65]', 14, 'start'))
    o.append(TM(16, 170, 'for i in 0...fares.count { print(fares[i]) }', 14, 'start'))
    x0, y = 60, 200
    for i in range(4):
        x = x0 + i * 110
        bad = i == 3
        o.append(R(x, y, 96, 48, NXS if bad else ACS, NX if bad else AC, 6, 2, '6 4' if bad else None))
        o.append(T(x + 48, y + 30, '?' if bad else str([92, 158, 65][i]), 17, fill=NX if bad else INK, bold=True))
        o.append(T(x + 48, y + 70, f'[{i}]', 14, fill=NX if bad else MUT, bold=bad))
    o.append(brace(x0, x0 + 3 * 110 - 14, y + 82, AC))
    o.append(T(x0 + 160, y + 104, 'valid indices 0, 1, 2 (count = 3)', 13, fill=AC))
    o.append(T(x0 + 3 * 110 + 48, y + 104, 'i = 3', 13, fill=NX, bold=True))
    o.append(R(500, y - 4, 204, 120, NXS, NX, 8, 1.5))
    o.append(T(512, y + 20, 'debugger stops:', 13, 'start', bold=True))
    o.append(TM(512, y + 42, 'Fatal error: Index', 12, 'start', NX)); o.append(TM(512, y + 60, 'out of range', 12, 'start', NX))
    o.append(TM(512, y + 84, '(lldb) po fares', 12, 'start')); o.append(TM(512, y + 102, '[92, 158, 65]', 12, 'start'))
    o.append(T(16, y + 146, 'Fix: 0..&lt;fares.count stops at 2, or write for fare in fares.', 14, 'start', bold=True))
    return y + 162, ''.join(o)
FIG[4] = (f4, 'The code builds and installs, so the error is not a build error. At run time the closed range 0...fares.count asks for index 3 of a 3-element array, and the debugger stops with Index out of range; 0..<fares.count fixes it.',
          'Five steps, edit, build, install, run and crash; below, an array of 92, 158 and 65 at indices 0 to 2 and a dashed empty slot at index 3 where the loop crashes, with the debugger message beside it.')


# ---- 6.5 outlet, action, label ----
def f5():
    o = [T(16, 24, 'One tap, from the storyboard to the label', 15, 'start', bold=True)]
    o.append(R(16, 46, 150, 230, PANEL, INK, 14, 2)); o.append(R(26, 66, 130, 190, 'var(--fig)', L2, 4, 1))
    o.append(R(40, 92, 102, 36, LVS, LV, 4, 2)); o.append(T(91, 116, '₹92.00', 16, bold=True))
    o.append(T(91, 146, 'fareLabel', 12, fill=MUT))
    o.append(R(40, 176, 102, 36, AC, AC, 18, 2)); o.append(T(91, 199, 'Show fare', 13, fill='var(--fig)', bold=True))
    o.append(T(91, 296, 'was ₹0 before the tap', 12, fill=MUT))
    o.append(mono_box(220, 46, 484, 70, ['@IBOutlet weak var fareLabel: UILabel!'], PANEL, LV, 13, 'outlet: connected once, when the scene loads'))
    o.append(L(218, 92, 146, 108, LV, 2, arrow='l'))
    o.append(mono_box(220, 150, 484, 110, ['@IBAction func showFare(_ sender: UIButton) {', '  let fare = 8 * 11.50     // 92.0',
                                           '  fareLabel.text = String(format: "₹%.2f", fare)'][:3], PANEL, AC, 12, 'action: runs on every tap'))
    o.append(L(146, 194, 218, 196, AC, 2, arrow='n'))
    o.append(T(220, 290, 'Before viewDidLoad the outlet is still nil; use it only after the scene has loaded.', 13, 'start', NX))
    return 306, ''.join(o)
FIG[5] = (f5, 'The outlet links fareLabel to the label once, when the scene loads. Each tap calls the showFare action, which works out 8 × ₹11.50 = ₹92.00 and writes it into the label through the outlet.',
          'A phone screen with a fare label and a Show fare button; an outlet box connects to the label and an action box is called by the button, computing 8 times 11.50 and writing 92.00 into the label.')


# ---- 6.6 table rows from the fares array ----
def f6():
    trips = [('8 km city', '20 + 8 × 9.0', 92), ('12 km outstation', '20 + 12 × 11.5', 158), ('5 km city', '20 + 5 × 9.0', 65)]
    o = [T(16, 24, 'Three trips become the model array, and the table asks for rows', 15, 'start', bold=True)]
    for i, (a, b, f) in enumerate(trips):
        y = 48 + i * 46
        o.append(T(16, y + 22, a, 13, 'start')); o.append(T(150, y + 22, f'{b} = {f}', 13, 'start', MUT))
        o.append(R(300, y, 70, 36, ACS if i == 1 else PANEL, AC, 4, 1.5)); o.append(T(335, y + 23, str(f), 15, bold=True))
        o.append(T(380, y + 23, f'[{i}]', 13, 'start', MUT))
    o.append(T(335, 196, 'fares', 13, fill=MUT))
    o.append(R(430, 44, 274, 40, PANEL, L2, 6, 1.5))
    o.append(TM(442, 69, 'numberOfRowsInSection → 3', 13, 'start'))
    o.append(R(470, 100, 200, 150, PANEL, INK, 10, 2))
    for i, f in enumerate([92, 158, 65]):
        o.append(R(480, 112 + i * 44, 180, 38, AC if i == 1 else 'var(--fig)', AC if i == 1 else L2, 4, 1.5))
        o.append(T(570, 137 + i * 44, f'₹{f}', 15, fill='var(--fig)' if i == 1 else INK, bold=True))
    o.append(L(372, 112, 476, 156, AC, 2, arrow='n'))
    o.append(T(410, 278, 'cellForRowAt row 1 → ₹158', 13, 'start', AC, True))
    o.append(R(16, 220, 380, 76, LVS, LV, 8, 2))
    o.append(T(30, 244, 'tap → didSelectRowAt', 14, 'start', bold=True))
    o.append(TM(30, 266, 'section 0, row 1', 13, 'start'))
    o.append(TM(30, 286, 'fares[1] = 158 → next screen', 13, 'start', LV, True))
    return 304, ''.join(o)
FIG[6] = (f6, 'The three fares, 92, 158 and 65, form the model array, so the table has 3 rows. The cell for row 1 shows ₹158, and a tap on it passes just fares[1] = 158 to the next screen.',
          'Three trips worked out to 92, 158 and 65 in an array with indices 0 to 2; a table view with three rows, the middle one highlighted showing 158; a box shows the tap passing 158 onward.')


# ---- 6.7 fillEqually on two widths ----
def f7():
    o = [T(16, 24, 'Stack view: 3 buttons, spacing 8, 16 from each edge, fillEqually', 15, 'start', bold=True)]
    for j, (W, bw, lab) in enumerate([(360, 104, '104'), (320, 272 / 3, '90.67')]):
        sc = 1.8
        y = 60 + j * 140
        x0 = 30
        o.append(T(x0, y - 6, f'screen {W} points', 14, 'start', bold=True))
        o.append(R(x0, y, W * sc, 60, 'var(--fig)', INK, 6, 2))
        x = x0 + 16 * sc
        o.append(R(x0, y + 4, 16 * sc, 52, NXS, NXS, 2, 0))
        o.append(R(x0 + (W - 16) * sc, y + 4, 16 * sc, 52, NXS, NXS, 2, 0))
        for i in range(3):
            o.append(R(x, y + 8, bw * sc, 44, ACS, AC, 6, 2))
            o.append(T(x + bw * sc / 2, y + 36, lab, 14, bold=True))
            x += bw * sc
            if i < 2:
                o.append(R(x, y + 8, 8 * sc, 44, LVS, LVS, 1, 0)); x += 8 * sc
        o.append(T(x0 + 8 * sc, y + 80, '16', 12, fill=NX, bold=True))
        o.append(T(x0 + (16 + bw + 4) * sc, y + 80, '8', 12, fill=LV, bold=True))
        o.append(T(x0 + W * sc / 2, y + 100, f'{W} − 16 − 16 − 2 × 8 = {W - 48};  {W - 48} ÷ 3 = {lab} points each', 14))
    return 320, ''.join(o)
FIG[7] = (f7, 'Margins and gaps come off first: on 360 points, 360 − 32 − 16 = 312, so each button is 104 points; the same rules on 320 points give 272 ÷ 3 ≈ 90.67 points.',
          'Two screen bars drawn to scale, 360 and 320 points wide, each with 16 point margins, two 8 point gaps and three equal buttons of 104 and 90.67 points.')


# ---- 6.8 one push on the navigation stack ----
def f8():
    o = [T(16, 24, 'Tap row 1 of [92, 158, 65]: the show segue showDetail pushes Detail', 15, 'start', bold=True)]
    def stack(x, items, lab):
        r = [T(x + 80, 330, lab, 14, bold=True)]
        for i, (n, f, s) in enumerate(items):
            y = 290 - (i + 1) * 60
            r.append(boxt(x, y, 160, 52, n, f, s, 14, bold_first=True))
        r.append(L(x - 10, 296, x + 170, 296, INK, 2))
        return ''.join(r)
    o.append(stack(16, [(['Fare List', 'root'], PANEL, AC)], 'before: 1 controller'))
    o.append(R(214, 120, 280, 110, ACS, AC, 8, 2))
    o.append(T(228, 144, 'prepare(for:sender:)', 14, 'start', bold=True))
    o.append(TM(228, 168, 'fare = fares[1]  // 158', 13, 'start'))
    o.append(TM(228, 190, 'detail.fare = 158', 13, 'start'))
    o.append(T(228, 214, 'then push', 13, 'start', MUT))
    o.append(L(186, 230, 210, 190, AC, 2, arrow='n'))
    o.append(L(496, 175, 528, 175, AC, 2.5, arrow='n'))
    o.append(stack(544, [(['Fare List', 'root'], PANEL, AC), (['Detail', 'fare ₹158'], LVS, LV)], 'after: 2 controllers'))
    o.append(T(214, 258, 'Back pops Detail; the list is unchanged.', 13, 'start', NX))
    o.append(T(214, 278, 'Modal instead: no back button, add Close → dismiss.', 13, 'start', MUT))
    return 346, ''.join(o)
FIG[8] = (f8, 'Tapping row 1 runs prepare, which sets detail.fare to fares[1] = ₹158, and the push grows the stack from one controller to two. Back pops Detail and returns to the same list; a modal Detail would need its own Close button.',
          'A stack with one Fare List box, a prepare box setting fare 158, and a second stack with Fare List at the bottom and Detail with fare 158 on top.')


spec = make_spec(FIG)


def text_fixes(k):
    return {
        1: [(' Only a few universities teach Swift itself as a language unit, so this chapter stays short and moves to real code.',
             ' This chapter stays short and moves to real code.')],
        2: [(' Only a few universities teach Swift at this depth, so treat this as working vocabulary for the rest of the unit.',
             ' Treat this as working vocabulary for the rest of the unit.')],
        3: [(' Only a few universities teach this topic at this depth.', '')],
        4: [(' Only a few universities teach these tools in depth, so exams often test the order of steps and the meaning of a crash message.',
             ' Exams often test the order of steps and the meaning of a crash message.'),
            ('The figure shows this order. Only a few universities teach these tools in depth; exams often ask the order.',
             'The figure shows this order, then the crash.')],
        5: [('Only a few universities teach storyboards now; some syllabi have moved to SwiftUI instead.',
             'Many courses now teach SwiftUI beside or instead of storyboards.'),
            ('@IBAction func showFare(_ sender: UIButton) {\n    fareLabel.text = "₹92"\n}',
             '@IBAction func showFare(_ sender: UIButton) {\n    let fare = 8 * 11.50\n    fareLabel.text = String(format: "₹%.2f", fare)\n}'),
            ('Inside the action write one line: fareLabel.text = "₹92".',
             'Inside the action work out the fare and write it: let fare = 8 * 11.50, then fareLabel.text = String(format: "₹%.2f", fare), which shows ₹92.00.'),
            ('Put the connection check nowhere else: before viewDidLoad the outlet is still nil, so any use in an initializer or an early property observer crashes.',
             'Use the outlet only after the scene has loaded: before viewDidLoad it is still nil, so any use in an initializer or an early property observer crashes.'),
            ('written by fareLabel.text = "₹92" when the button is tapped.',
             'written by fareLabel.text = String(format: "₹%.2f", fare) when the button is tapped.')],
        7: [(' Only a few universities teach priorities at this depth.', '')],
        8: [(' Only a few universities teach segues in detail.', '')],
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
