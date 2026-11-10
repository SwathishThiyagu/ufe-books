"""Claude's hand-drawn figures for c-data-u1 (Data Science, unit 1: introduction to data science), one per chapter,
from each chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
ARR = {AC: 'n', L2: 'm', LV: 'l', NX: 'x', MUT: 'm', INK: 'm'}


def ar(x1, y1, x2, y2, c=AC, w=2, dash=None):
    return L(x1, y1, x2, y2, c, w, dash, arrow=ARR[c])


def rs(v):
    """Indian digit grouping: 210000 -> 2,10,000"""
    s = str(v)
    if len(s) <= 3: return '₹' + s
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2: parts.insert(0, head[-2:]); head = head[:-2]
    if head: parts.insert(0, head)
    return '₹' + ','.join(parts + [tail])


# ---- 1.1 mass SMS against a targeted list ----
def f1():
    k = 0.001
    o = [R(130, 14, 16, 16, PANEL, L2, 3, 1.5), T(152, 27, 'message all 1,00,000', 14, 'start'),
         R(330, 14, 16, 16, ACS, AC, 3, 1.5), T(352, 27, 'message the top 20,000', 14, 'start', AC, True)]
    rows = [('SMS cost', 200000, 40000), ('margin', 300000, 210000), ('net gain', 100000, 170000)]
    for i, (lab, a, b) in enumerate(rows):
        y = 52 + i * 86
        o.append(T(118, y + 36, lab, 15, 'end', INK, True))
        o += [R(130, y, a * k, 28, PANEL, L2, 3, 1.5), T(140 + a * k, y + 19, rs(a), 14, 'start', MUT, True),
              R(130, y + 34, b * k, 28, ACS, AC, 3, 1.5), T(140 + b * k, y + 53, rs(b), 14, 'start', AC, True)]
    o.append(boxt(520, 52, 180, 76, ['lift', '7% ÷ 2% = 3.5'], NXS, NX, 16, True))
    o.append(boxt(520, 150, 180, 92, ['margin per ₹1 spent', 'all: ₹1.50', 'top 20,000: ₹5.25'], PANEL, AC, 14, True))
    o.append(T(20, 316, 'The targeted plan gets 600 fewer orders but earns ₹70,000 more.', 14, 'start', NX, True))
    return 330, ''.join(o)


FIG[1] = (f1, 'Messaging everyone costs ₹2,00,000 and nets ₹1,00,000; messaging only the model\'s top 20,000 costs ₹40,000 and nets ₹1,70,000. Those customers order 3.5 times as often.',
          'Paired bars for SMS cost, margin and net gain: messaging all customers gives 2,00,000, 3,00,000 and 1,00,000 rupees; messaging the top 20,000 gives 40,000, 2,10,000 and 1,70,000. Side boxes give lift 3.5 and margin per rupee 1.50 against 5.25.')


# ---- 1.2 structure, and what self-description costs ----
def f2():
    cols = [('structured', ['IRCTC bookings table'], NXS, NX), ('semi-structured', ['weather API JSON', 'email (headers + body)'], ACS, AC),
            ('unstructured', ['30 s voice note', 'CCTV footage'], LVS, LV)]
    o = []
    for i, (h, items, f, st) in enumerate(cols):
        x = 20 + i * 232
        o.append(boxt(x, 14, 216, 34, [h], f, st, 15, True))
        for j, s in enumerate(items):
            o.append(T(x + 108, 72 + j * 22, s, 14))
    o.append(T(20, 140, 'one booking, two ways to store it', 14, 'start', MUT, True))
    o.append(T(20, 172, 'CSV', 15, 'start', NX, True))
    o.append(TM(80, 172, '4512367890,Priya S,12657,845', 14, 'start'))
    o.append(T(20, 214, 'JSON', 15, 'start', AC, True))
    o.append(TM(80, 214, '{"pnr":"4512367890","name":"Priya S","train":12657,"fare":845}', 13, 'start'))
    bw = 8.6
    o += [R(80, 244, 29 * bw, 26, NXS, NX, 3, 1.5), T(90 + 29 * bw, 262, '29 bytes', 14, 'start', NX, True),
          R(80, 280, 29 * bw, 26, ACS, AC, 3, 1.5), R(80 + 29 * bw, 280, 34 * bw, 26, LVS, LV, 3, 1.5),
          T(80 + 29 * bw / 2, 298, 'values', 13, fill=AC, bold=True), T(80 + 29 * bw + 17 * bw, 298, '+34 key names and quotes', 13, fill=LV, bold=True),
          T(90 + 63 * bw, 298, '63 bytes', 14, 'start', AC, True)]
    o.append(T(20, 340, 'For 10 lakh bookings: CSV 29 MB, JSON 63 MB, about 2.17 times as much.', 14, 'start', INK, True))
    return 354, ''.join(o)


FIG[2] = (f2, 'The five sources sorted by structure, and one booking stored as CSV and as JSON. JSON repeats its 34 bytes of keys and quotes in every record, so 10 lakh bookings take 63 MB against 29 MB.',
          'Three headed columns: structured holds the IRCTC table; semi-structured holds the weather JSON and email; unstructured holds the voice note and CCTV. Below, the CSV line and the JSON line for one booking, with bars of 29 bytes and 63 bytes, the extra 34 bytes marked as key names and quotes.')


# ---- 1.3 the mess forecast tested on week 2 ----
def f3():
    x0, x1, y0, y1 = 80, 500, 40, 270
    fx = lambda i: x0 + (i + 0.5) * (x1 - x0) / 7
    fy = lambda v: y1 - (v - 150) * (y1 - y0) / 160
    o = [axes(x0, x1, y0, y1, [], [150, 175, 200, 225, 250, 275, 300], fx, fy, '', 'dinners eaten')]
    for i, d in enumerate(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']):
        o.append(T(fx(i), y1 + 20, d, 13, fill=MUT))
    o += [L(x0, fy(300), x1, fy(300), LV, 2, '7 5'), T(x1 - 4, fy(300) - 8, 'old rule: always 300', 13, 'end', LV, True)]
    o += [L(fx(0) - 20, fy(246), fx(4) + 20, fy(246), AC, 2.5), L(fx(5) - 20, fy(175), fx(6) + 20, fy(175), AC, 2.5),
          Tb(fx(2), fy(246) + 22, 'forecast 246', 13, fill=AC, bold=True), Tb(fx(5.5), fy(175) + 26, 'forecast 175', 13, fill=AC, bold=True)]
    w1 = [250, 246, 254, 248, 232, 178, 172]
    w2 = [252, None, 250, 244, 228, 182, 176]
    for i, v in enumerate(w1):
        o.append(C(fx(i) - 7, fy(v), 6, NX))
    for i, v in enumerate(w2):
        if v is None: continue
        o.append(f'<rect x="{fx(i) + 1:.1f}" y="{fy(v) - 6:.1f}" width="12" height="12" style="fill:var(--panel);stroke:{LV};stroke-width:2"/>')
    o.append(T(fx(1), fy(225), 'blank', 13, fill=MUT))
    o += [C(530, 52, 6, NX), T(544, 57, 'week 1 (builds it)', 13, 'start'),
          f'<rect x="524" y="70" width="12" height="12" style="fill:var(--panel);stroke:{LV};stroke-width:2"/>', T(544, 81, 'week 2 (tests it)', 13, 'start')]
    o.append(boxt(520, 104, 180, 52, ['Thu 2480 → 248', 'typing error fixed'], PANEL, L2, 13, True))
    o.append(boxt(520, 168, 180, 60, ['test error (MAE)', 'forecast 6.3', 'always 300: 78'], NXS, NX, 13, True))
    o.append(T(20, 322, 'Cook 259 on weekdays and 184 at weekends (5% buffer): 1,663 plates a week instead of 2,100,', 14, 'start'))
    o.append(T(20, 344, 'saving 437 plates, ₹17,480 a week, and no day in week 2 runs short.', 14, 'start', NX, True))
    return 358, ''.join(o)


FIG[3] = (f3, 'Week 1 sets the forecast, 246 on weekdays and 175 at weekends; week 2 tests it with an average error of 6.3 plates, against 78 for always cooking 300.',
          'A chart of dinners eaten by day: green dots for week 1, orange squares for week 2 (Tuesday blank), a forecast line at 246 for weekdays and 175 for weekends, and a dashed line at 300 for the old rule. Side boxes note the typing error fixed and the errors 6.3 against 78.')


# ---- 1.4 the bakery decision (descriptive, predictive, prescriptive) ----
def f4():
    o = []
    steps = [('descriptive', 'what happened?', 'total 804, mean 134', PANEL, L2),
             ('predictive', 'what will happen?', 'ŷ = 115.8 + 5.2x → 152', ACS, AC),
             ('prescriptive', 'what should we do?', 'bake 152 puffs', NXS, NX)]
    for i, (a, b, c, f, st) in enumerate(steps):
        x = 20 + i * 236
        o.append(boxt(x, 20 + (2 - i) * 18, 208, 76, [a, b, c], f, st, 14, True))
        if i < 2: o.append(ar(x + 208, 58 + (2 - i) * 18 - 9, x + 234, 58 + (1 - i) * 18 - 9, st if st != L2 else AC))
    o.append(T(20, 150, 'profit for each choice (₹)', 14, 'start', MUT, True))
    cols = [(150, 'demand 147', 'p = 0.25'), (280, 'demand 152', 'p = 0.5'), (410, 'demand 157', 'p = 0.25'), (560, 'expected', '')]
    for x, a, b in cols:
        o.append(T(x, 172, a, 14, bold=True))
        if b: o.append(T(x, 190, b, 13, fill=MUT))
    rows = [('bake 147', [1176, 1176, 1176], 1176), ('bake 152', [1116, 1216, 1216], 1191), ('bake 157', [1056, 1156, 1256], 1156)]
    for i, (lab, vs, e) in enumerate(rows):
        y = 200 + i * 40
        best = i == 1
        if best: o.append(R(20, y, 680, 36, NXS, NX, 6, 1.5))
        o.append(T(30, y + 24, lab, 15, 'start', NX if best else INK, True))
        for (x, _, _), v in zip(cols, vs):
            o.append(T(x, y + 24, f'{v:,}', 15))
        o.append(T(560, y + 24, f'{e:,}', 16, fill=NX if best else INK, bold=True))
    o.append(T(20, 344, 'Baking 152 gives the highest expected profit, ₹1,191.', 14, 'start', NX, True))
    return 358, ''.join(o)


FIG[4] = (f4, 'The same sales data answers three questions: the mean was 134, the line forecasts 152 for day 7, and the payoff table shows that baking 152 gives the best expected profit, ₹1,191.',
          'Three rising boxes: descriptive, total 804 and mean 134; predictive, y-hat = 115.8 + 5.2x giving 152; prescriptive, bake 152. Below, a payoff table for baking 147, 152 or 157 against demand 147, 152 or 157, with expected profits 1,176, 1,191 and 1,156; the 152 row is highlighted.')


# ---- 1.5 sensor completeness ----
def f5():
    gx, gy, cw, ch = 70, 40, 14, 10
    o = [T(gx + 15 * cw, 28, '30 days, 144 readings a day', 13, fill=MUT, bold=True)]
    for s in range(20):
        if s in (0, 6, 19): o.append(T(gx - 8, gy + s * ch + 9, str(s + 1), 13, 'end', LV if s == 6 else MUT, s == 6))
        for d in range(30):
            miss = s == 6 and d >= 15
            o.append(R(gx + d * cw + 0.5, gy + s * ch + 0.5, cw - 1, ch - 1, LV if miss else NXS, LV if miss else NX, 1, 0.6))
    o.append(f'<text x="30" y="{gy + 100}" font-size="13" text-anchor="middle" transform="rotate(-90 30 {gy + 100})" style="fill:{MUT}">sensor</text>')
    o.append(T(gx, gy + 20 * ch + 18, 'day 1', 13, 'start', MUT)); o.append(T(gx + 30 * cw, gy + 20 * ch + 18, 'day 30', 13, 'end', MUT))
    o += [ar(528, gy + 6 * ch + 5, gx + 30 * cw + 6, gy + 6 * ch + 5, LV)]
    o.append(boxt(530, 30, 170, 76, ['sensor 7 silent', 'for 15 days', '144 × 15 = 2,160 rows'], LVS, LV, 13, True))
    o.append(boxt(530, 120, 170, 100, ['expected 86,400 rows', 'arrived 84,240', 'complete 97.5%', '3.46 MB at 40 B a row'], NXS, NX, 13, True))
    o.append(T(20, 290, 'API: 2,62,800 records ÷ 500 a request = 526 requests; at 100 a minute that takes 6 minutes.', 14, 'start'))
    o.append(T(20, 314, 'Survey: 216 replies from 1,200 = 18%; those with breathing problems are more likely to reply.', 14, 'start'))
    o.append(T(20, 338, 'Sensors and survey are primary data; the government API is secondary.', 14, 'start', AC, True))
    return 352, ''.join(o)


FIG[5] = (f5, 'Twenty sensors over 30 days should send 86,400 rows; 84,240 arrive, 97.5%. The 2,160 missing rows are exactly 15 days of one sensor, so look for a sensor that went offline.',
          'A grid of 20 sensors by 30 days, all green except sensor 7 from day 16 to day 30, shaded orange. Side boxes say sensor 7 was silent for 15 days, 2,160 rows, and that 84,240 of 86,400 rows arrived, 97.5%. Lines below give 526 API requests in 6 minutes and an 18% survey response.')

spec = make_spec(FIG)
