"""Claude's hand-drawn figures for c-se-u2 (Software Engineering, unit 2: requirements engineering and analysis), one per
chapter, from each chapter's worked example, plus the sentences in the chapter text that describe a figure (text_fixes)."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {}


def card(x, y, w, h, head, sub, fill=PANEL, st=AC, sub2=None):
    o = R(x, y, w, h, fill, st, 6)
    o += T(x + 12, y + 22, head, 14, 'start', bold=True)
    o += T(x + 12, y + 42, sub, 13, 'start', MUT)
    if sub2: o += T(x + 12, y + 62, sub2, 13, 'start', st, True)
    return o


def actor(x, y, name, c=INK):
    o = [f'<circle cx="{x}" cy="{y}" r="9" style="fill:none;stroke:{c};stroke-width:2"/>',
         L(x, y + 9, x, y + 34, c, 2), L(x - 14, y + 18, x + 14, y + 18, c, 2),
         L(x, y + 34, x - 11, y + 52, c, 2), L(x, y + 34, x + 11, y + 52, c, 2), T(x, y + 72, name, 14, bold=True)]
    return ''.join(o)


def oval(cx, cy, rx, ry, label, fill=ACS, st=AC):
    return (f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" style="fill:{fill};stroke:{st};stroke-width:2"/>' + T(cx, cy + 5, label, 14, bold=True))


# ---- 2.1 sort R1 to R5 ----
def f1():
    o = [T(20, 26, 'Library app: five statements sorted', 15, 'start', bold=True)]
    o.append(R(20, 44, 216, 236, FIGBG, AC, 8, 1.5, '6 4')); o.append(T(128, 66, 'Functional: what it does', 14, fill=AC, bold=True))
    o.append(R(252, 44, 448, 236, FIGBG, LV, 8, 1.5, '6 4')); o.append(T(476, 66, 'Non-functional: how well, within what limits', 14, fill=LV, bold=True))
    o.append(card(34, 84, 188, 70, 'R1 search catalogue', 'sees matching books'))
    o.append(card(266, 84, 206, 86, 'R2 performance', 'results within 2 s', LVS, LV, '20/s × 2 s = 40 at once'))
    o.append(card(480, 84, 206, 86, 'R3 capacity', '50,000 × 4 KB = 200,000 KB', LVS, LV, '÷ 1024 = 195.31 MB'))
    o.append(card(266, 182, 206, 70, 'R4 platform', 'Android 8 and above', LVS, LV))
    o.append(R(20, 296, 680, 64, NXS, NX, 8))
    o.append(T(36, 320, 'R5 interface requirement, with a security constraint', 14, 'start', NX, True))
    o.append(T(36, 342, 'payments go to the outside gateway, and only over HTTPS', 13, 'start'))
    o.append(T(360, 386, 'R1 can be shown on a screen; R2 and R3 have to be measured.', 14, fill=MUT))
    return 400, ''.join(o)
FIG[1] = (f1, 'R1 is the only functional statement. R2, R3 and R4 limit how well and where it runs (40 searches in progress at peak, 195.31 MB of metadata), and R5 is an interface requirement that also carries a security constraint.',
          'Two dashed regions: functional holds R1 search catalogue; non-functional holds R2 performance with 20 per second times 2 seconds equals 40, R3 capacity with 195.31 MB, and R4 platform. A band below holds R5, the interface with a security constraint.')


# ---- 2.2 fee portal economics ----
def f2():
    o = [T(20, 26, 'Fee portal: 16,000 payments a year (8,000 students × 2)', 15, 'start', bold=True)]
    x0, s = 210, 470 / 360000
    rows = [
        ('manual overtime today', [(360000, LVS, LV, '₹3,60,000')], '16,000 × 9 min × ₹2.50'),
        ('portal running cost', [(96000, PANEL, AC, ''), (16000, PANEL, AC, ''), (40000, PANEL, AC, '')], 'gateway ₹96,000 + SMS ₹16,000 + upkeep ₹40,000'),
        ('cash saving', [(208000, ACS, AC, '₹2,08,000')], '₹3,60,000 − ₹1,52,000'),
        ('capital share', [(200000, PANEL, L2, '₹2,00,000')], '₹6,00,000 ÷ 3 years'),
        ('net benefit', [(8000, NXS, NX, '')], '₹2,08,000 − ₹2,00,000 = ₹8,000 a year'),
    ]
    y = 50
    for name, segs, note in rows:
        o.append(T(x0 - 12, y + 22, name, 14, 'end', bold=True))
        x = x0
        for v, f, st, lab in segs:
            w = max(v * s, 4)
            o.append(R(x, y, w, 32, f, st, 3))
            if lab: o.append(T(x + w / 2, y + 21, lab, 13, bold=True))
            x += w
        o.append(T(x0, y + 50, note, 13, 'start', MUT))
        y += 66
    o.append(T(x0 + 12, y - 66 + 21, '₹8,000', 14, 'start', NX, True))
    o.append(T(x0 + 152000 * s + 10, 50 + 66 + 21, '₹1,52,000', 13, 'start', bold=True))
    yb = y + 4
    o.append(T(20, yb + 4, 'Payback = ₹6,00,000 ÷ ₹2,08,000 = 2.88 years of a 3-year life', 14, 'start', bold=True))
    checks = [('technical', 'pass: 5 per minute', NXS, NX), ('economic', 'marginal', LVS, LV), ('schedule', 'risky: 3 months', LVS, LV),
              ('operational and legal', 'SMS receipts, audit rules', PANEL, AC)]
    cw = 164
    for i, (a, b, f, st) in enumerate(checks):
        x = 20 + i * (cw + 8)
        o.append(boxt(x, yb + 20, cw, 50, [a, b], f, st, 13, True))
    o.append(T(20, yb + 98, 'Verdict: start with minimum scope (login, payment, receipt, reconciliation); SMS can follow.', 14, 'start', MUT))
    return yb + 112, ''.join(o)
FIG[2] = (f2, 'The portal saves ₹3,60,000 of overtime a year but costs ₹1,52,000 to run, and the ₹6,00,000 budget spread over 3 years eats almost all of the rest, leaving ₹8,000 a year. With a payback of 2.88 years the study calls it marginal and starts with minimum scope.',
          'Five horizontal bars on one rupee scale: manual overtime 3.6 lakh, running cost 1.52 lakh in three parts, cash saving 2.08 lakh, capital share 2 lakh and a tiny net benefit of 8,000. Below, four verdict boxes: technical pass, economic marginal, schedule risky, operational and legal checks.')


# ---- 2.3 workshop agenda ----
def f3():
    blocks = [('welcome', 10, False), ('first questions', 20, True), ('conflict listing', 30, True), ('resolution', 20, True), ('recap', 10, False)]
    x0, s = 20, 680 / 90
    y = 60
    o = [T(20, 26, '90-minute workshop, 12 participants', 15, 'start', bold=True)]
    x = x0
    for name, m, el in blocks:
        w = m * s
        o.append(R(x, y, w, 56, ACS if el else PANEL, AC if el else L2, 4))
        o.append(T(x + w / 2, y + 24, name if m > 10 else name[:7], 14 if m > 10 else 13, bold=el))
        o.append(T(x + w / 2, y + 44, f'{m} min', 13, fill=MUT))
        x += w
    e0, e1 = x0 + 10 * s, x0 + 80 * s
    o.append(brace(e0, e1, y + 70, AC))
    o.append(T((e0 + e1) / 2, y + 96, 'elicitation = 20 + 30 + 20 = 70 min;  70 ÷ 90 = 77.78%', 14, fill=AC, bold=True))
    # resolution split
    r0 = x0 + 60 * s
    yr = y + 132
    o.append(T(20, yr + 4, 'The 20-minute resolution block, shared by 5 groups', 14, 'start', bold=True))
    groups = ['passengers', 'clerks', 'finance', 'IT ops', 'access']
    gw = 128
    for i, g in enumerate(groups):
        gx = 20 + i * (gw + 10)
        o.append(boxt(gx, yr + 18, gw, 44, [g, '4 min'], NXS, NX, 13, True))
    o.append(T(20, yr + 90, '20 ÷ 5 = 4 minutes per group', 14, 'start', NX, True))
    # participant-minutes
    yp = yr + 120
    o.append(T(20, yp, 'Participant-minutes: 12 people × 90 min = 1080', 14, 'start', bold=True))
    for i in range(12):
        o.append(f'<circle cx="{30 + i * 22}" cy="{yp + 22}" r="7" style="fill:{ACS};stroke:{AC};stroke-width:1.5"/>')
    o.append(T(30 + 12 * 22 + 6, yp + 27, '4 passengers, 3 clerks, 2 finance, 2 IT ops, 1 accessibility', 13, 'start', MUT))
    return yp + 42, ''.join(o)
FIG[3] = (f3, 'The three elicitation blocks fill 70 of the 90 minutes, which is 77.78% of the workshop, and the 20-minute resolution block gives each of the five stakeholder groups 4 minutes. Twelve people for 90 minutes is 1080 participant-minutes.',
          'A 90-minute timeline: welcome 10, first questions 20, conflict listing 30, resolution 20 and recap 10, with the middle three bracketed as 70 minutes of elicitation. Below, five boxes of 4 minutes each and a row of 12 participant dots.')


# ---- 2.4 inspection and change request ----
def f4():
    o = [T(20, 26, 'Inspection of 40 requirements', 15, 'start', bold=True)]
    s, g = 26, 6
    kinds = ['amb'] * 6 + ['con'] * 4 + ['ok'] * 30
    for i, k in enumerate(kinds):
        col, row = i % 20, i // 20
        x, y = 20 + col * (s + g), 42 + row * (s + g)
        f, st = {'amb': (LVS, LV), 'con': (LVS, LV), 'ok': (NXS, NX)}[k]
        o.append(R(x, y, s, s, f, st, 3, 1.5))
        if k == 'con': o.append(T(x + s / 2, y + 18, '≠', 14, fill=LV, bold=True))
        if k == 'amb': o.append(T(x + s / 2, y + 18, '?', 14, fill=LV, bold=True))
    ym = 42 + 2 * (s + g) + 8
    for i in range(3):
        x = 20 + i * (s + g)
        o.append(R(x, ym, s, s, PANEL, AC, 3, 1.5, '4 3')); o.append(T(x + s / 2, ym + 18, '+', 14, fill=AC, bold=True))
    o.append(T(20 + 3 * (s + g) + 4, ym + 18, '3 missing requirements to add', 13, 'start', AC))
    yl = ym + 54
    o.append(T(20, yl, '6 ambiguous (?) + 3 missing (+) + 2 conflicting pairs (≠) = 11 defects', 14, 'start', LV, True))
    o.append(T(20, yl + 22, '6 + 4 = 10 old requirements carry a defect, so 30 of 40 are clean', 14, 'start'))
    o.append(T(20, yl + 44, 'fix and re-inspect to zero, then baseline v1.0 with 40 + 3 = 43 requirements', 14, 'start', NX, True))
    # CR-01 flow
    yc = yl + 74
    o.append(L(20, yc - 12, 700, yc - 12, LN, 1))
    o.append(T(20, yc + 12, 'Change request CR-01: add a cancellation fee', 15, 'start', bold=True))
    steps = [('log CR-01', 'ID, requester, reason'), ('impact analysis', '5 design modules, T-13'), ('change board', 'approve or reject'), ('release v1.1', 'add row R13')]
    bw, gap = 160, 13
    for i, (a, b) in enumerate(steps):
        x = 20 + i * (bw + gap)
        o.append(boxt(x, yc + 28, bw, 52, [a, b], ACS if i == 1 else PANEL, AC, 13, True))
        if i: o.append(L(x - gap, yc + 54, x - 2, yc + 54, AC, 2, arrow='n'))
    return yc + 96, ''.join(o)
FIG[4] = (f4, 'The inspection marks 6 ambiguous requirements and 2 conflicting pairs among the 40, and finds 3 missing: 11 defects, with 30 requirements clean. After the fixes v1.0 holds 43, and CR-01 reaches v1.1 only through impact analysis on 5 modules and a board decision.',
          'Forty small squares: 6 marked with a question mark, 4 marked as conflicting, 30 clean, plus 3 dashed squares for missing requirements. Below, a row of four boxes: log CR-01, impact analysis on 5 modules and test T-13, change board, release v1.1 with row R13.')


# ---- 2.5 SRS sections and five numbered lines ----
def f5():
    o = []
    x, w = 20, 680
    o.append(R(x, 20, w, 50, PANEL, L2, 6)); o.append(T(x + 16, 41, '1  Scope', 14, 'start', bold=True))
    o.append(T(x + 16, 60, 'alert app for 20,000 Chennai residents, fed by the electricity board\'s outage messages', 13, 'start', MUT))
    o.append(R(x, 78, w, 36, PANEL, L2, 6)); o.append(T(x + 16, 101, '2  Overall description', 14, 'start', bold=True))
    o.append(R(x, 122, w, 262, FIGBG, AC, 6, 2)); o.append(T(x + 16, 145, '3  Specific requirements: the five lines a tester checks', 14, 'start', AC, True))
    lines = [('FR-01', 'The app shall show an alert within 30 s of receiving an official outage message.', True),
             ('NFR-01', 'The app shall cache the last 10 outage records for offline viewing.', False),
             ('NFR-02', 'The app shall run on Android 9 or later and iOS 14 or later.', False),
             ('FR-02', 'The app shall let a user select exactly two areas.', False),
             ('FR-03', 'The app shall log every alert with its time and area.', False)]
    y = 160
    for tag, txt, hot in lines:
        o.append(R(x + 14, y, w - 28, 34, LVS if hot else PANEL, LV if hot else AC, 5, 2 if hot else 1.4))
        o.append(T(x + 26, y + 22, tag, 13, 'start', LV if hot else AC, True))
        o.append(T(x + 88, y + 22, txt, 13, 'start'))
        y += 42
    o.append(T(x, 410, 'FR-01 names when the clock starts (message received) and the limit (30 s), so a test can pass or fail it.', 13, 'start', MUT))
    return 422, ''.join(o)
FIG[5] = (f5, 'The SRS runs scope, overall description and specific requirements, and all five numbered lines of the alert app sit in section 3. FR-01 states when the clock starts and the 30 s limit, so a tester can pass or fail it.',
          'A document outline with three sections. Section 3 is enlarged and lists FR-01 alert within 30 seconds (highlighted), NFR-01 cache 10 outages, NFR-02 Android 9 and iOS 14, FR-02 two areas and FR-03 log time and area.')


# ---- 2.6 ATM withdraw cash, two customers ----
def f6():
    o = []
    o.append(actor(60, 30, 'Customer'))
    o.append(R(150, 22, 420, 96, FIGBG, L2, 8, 1.5)); o.append(T(160, 40, 'ATM system', 13, 'start', MUT))
    o.append(oval(360, 74, 120, 28, 'Withdraw cash'))
    o.append(actor(660, 30, 'Bank'))
    o.append(L(78, 62, 238, 74, INK, 1.6)); o.append(L(482, 74, 642, 62, INK, 1.6))
    o.append(T(360, 144, 'Both ask for ₹5,000; daily limit ₹25,000; card valid, ATM has cash', 14, bold=True))
    cols = [(20, 'Customer A: balance ₹12,000', True), (370, 'Customer B: balance ₹4,200', False)]
    for x, head, ok in cols:
        st = NX if ok else LV
        fl = NXS if ok else LVS
        w = 330
        o.append(T(x + w / 2, 176, head, 14, bold=True))
        o.append(boxt(x + 40, 188, w - 80, 34, ['card and PIN checked'], PANEL, AC, 13))
        o.append(L(x + w / 2, 222, x + w / 2, 240, AC, 2, arrow='n'))
        o.append(boxt(x + 20, 242, w - 40, 40, ['12,000 ≥ 5,000 ✓' if ok else '4,200 < 5,000 ✗'], fl, st, 15, True))
        o.append(L(x + w / 2, 282, x + w / 2, 300, st, 2, arrow='x' if ok else 'l'))
        if ok:
            o.append(boxt(x + 20, 302, w - 40, 52, ['debit ₹5,000, dispense, receipt', 'balance 12,000 − 5,000 = ₹7,000'], NXS, NX, 13))
        else:
            o.append(boxt(x + 20, 302, w - 40, 52, ['"insufficient balance", eject card', 'short by 5,000 − 4,200 = ₹800'], LVS, LV, 13))
        o.append(T(x + w / 2, 376, 'main success scenario' if ok else 'exception: no debit, no cash', 13, fill=st, bold=True))
    o.append(T(360, 404, 'Alternate flow: a wrong PIN once or twice only asks for re-entry.', 13, fill=MUT))
    return 416, ''.join(o)
FIG[6] = (f6, 'One use case, Withdraw cash, with two scenarios: Customer A passes the balance check and ₹12,000 becomes ₹7,000; Customer B\'s ₹4,200 is ₹800 short, so the exception path debits nothing and returns the card.',
          'A use case diagram with the Customer actor, the Withdraw cash oval inside the ATM system and the Bank actor. Below, two flows: Customer A passes 12,000 at least 5,000 and is left with 7,000; Customer B fails 4,200 less than 5,000, short by 800, and gets no cash.')


# ---- 2.7 classes and appointment states ----
def cls(x, y, w, name, attrs, fill=PANEL):
    h = 30 + 18 * len(attrs) + 8
    o = R(x, y, w, h, fill, AC, 4) + L(x, y + 28, x + w, y + 28, AC, 1.5) + T(x + w / 2, y + 20, name, 14, bold=True)
    for i, a in enumerate(attrs):
        o += T(x + 10, y + 46 + i * 18, a, 13, 'start', MUT)
    return o, h


def f7():
    o = [T(20, 24, 'Classes and multiplicities', 15, 'start', bold=True)]
    a, h = cls(20, 44, 130, 'Patient', ['name', 'phone']); o.append(a)
    b, _ = cls(220, 44, 140, 'Appointment', ['state']); o.append(b)
    c, _ = cls(20, 214, 130, 'Doctor', ['name']); o.append(c)
    d, _ = cls(220, 214, 140, 'Slot', ['date, time']); o.append(d)
    o.append(L(150, 74, 220, 74, AC, 2)); o.append(T(158, 66, '1', 13, 'start')); o.append(T(214, 66, '0..*', 13, 'end'))
    o.append(L(150, 240, 220, 240, AC, 2)); o.append(T(158, 232, '1', 13, 'start')); o.append(T(214, 232, '0..*', 13, 'end'))
    o.append(L(290, 214, 290, 98, AC, 2)); o.append(T(298, 206, '1', 13, 'start')); o.append(T(298, 114, '0..1', 13, 'start'))
    o.append(T(20, 320, '3 doctors × 30 slots each', 14, 'start', bold=True))
    o.append(T(20, 342, '= 90 Slot objects a day', 14, 'start', AC, True))
    o.append(T(20, 364, 'so at most 90 appointments a day', 13, 'start', MUT))
    # state machine
    X = 392
    o.append(L(X, 16, X, 380, LN, 1))
    o.append(T(X + 20, 24, 'Appointment: 4 states, 4 transitions', 15, 'start', bold=True))
    st = {'requested': (470, 90), 'confirmed': (630, 90), 'cancelled': (470, 290), 'completed': (630, 290)}
    for n, (x, y) in st.items():
        o.append(R(x - 62, y - 22, 124, 44, LVS if n == 'cancelled' else (NXS if n == 'completed' else PANEL), LV if n == 'cancelled' else (NX if n == 'completed' else AC), 20))
        o.append(T(x, y + 5, n, 14, bold=True))
    o.append(C(420, 50, 7, INK)); o.append(L(426, 56, 446, 66, INK, 2, arrow='n'))
    o.append(L(532, 90, 566, 90, AC, 2, arrow='n')); o.append(T(549, 120, 'doctor', 13, fill=MUT)); o.append(T(549, 136, 'accepts', 13, fill=MUT))
    o.append(L(470, 112, 470, 266, LV, 2, arrow='l')); o.append(Tb(470, 190, 'either cancels', 13))
    o.append(L(630, 112, 630, 266, NX, 2, arrow='x')); o.append(Tb(630, 175, 'visit', 13)); o.append(Tb(630, 193, 'done', 13))
    o.append(L(600, 110, 500, 268, LV, 2, arrow='l')); o.append(Tb(556, 232, 'doctor cancels', 13))
    return 380, ''.join(o)
FIG[7] = (f7, 'Left: Patient and Doctor each link to many appointments or slots, and a slot holds at most one appointment; 3 doctors with 30 slots each give 90 slots a day. Right: an appointment moves through 4 states by 4 allowed transitions.',
          'Four class boxes, Patient, Appointment, Doctor and Slot, joined with multiplicities 1 to 0..*, 1 to 0..* and 1 to 0..1. Beside them a state diagram: requested to confirmed, requested to cancelled, confirmed to completed and confirmed to cancelled.')


# ---- 2.8 level-1 DFD: 12 boundary flows + 7 internal ----
def pair(p, q, r1, r2, c=AC, off=5, dash=None, arrow='n'):
    (x1, y1), (x2, y2) = p, q
    a = math.atan2(y2 - y1, x2 - x1)
    nx, ny = -math.sin(a) * off, math.cos(a) * off
    sx, sy = x1 + r1 * math.cos(a), y1 + r1 * math.sin(a)
    ex, ey = x2 - r2 * math.cos(a), y2 - r2 * math.sin(a)
    return L(sx + nx, sy + ny, ex + nx, ey + ny, c, 2, dash, arrow) + L(ex - nx, ey - ny, sx - nx, sy - ny, c, 2, dash, arrow)


def one(p, q, r1, r2, c=L2, dash='6 4', arrow='m'):
    (x1, y1), (x2, y2) = p, q
    a = math.atan2(y2 - y1, x2 - x1)
    return L(x1 + r1 * math.cos(a), y1 + r1 * math.sin(a), x2 - r2 * math.cos(a), y2 - r2 * math.sin(a), c, 2, dash, arrow)


def f8():
    o = []
    proc = {'1': (250, 110, 'Enquiry'), '2': (250, 270, 'Booking'), '3': (250, 430, 'Cancel'), '4': (600, 110, 'Maintain')}
    ent = {'P': (70, 270, 'Passenger'), 'A': (600, 24, 'Railway Admin'), 'G': (600, 330, 'Payment Gateway')}
    sto = {'S': (430, 190, 'Train Schedule'), 'T': (440, 490, 'Ticket')}
    R_P = 40
    # boundary flows (solid, pairs)
    o.append(pair(ent['P'][:2], proc['1'][:2], 60, R_P + 3))
    o.append(pair(ent['P'][:2], proc['2'][:2], 66, R_P + 3))
    o.append(pair(ent['P'][:2], proc['3'][:2], 60, R_P + 3))
    o.append(pair(ent['A'][:2], proc['4'][:2], 22, R_P + 3, off=7))
    o.append(pair(ent['G'][:2], proc['2'][:2], 80, R_P + 3))
    o.append(pair(ent['G'][:2], proc['3'][:2], 80, R_P + 3))
    # internal (dashed)
    o.append(one(proc['4'][:2], (500, 190), R_P + 2, 4))
    o.append(one((380, 186), proc['1'][:2], 2, R_P + 3))
    o.append(one((380, 194), proc['2'][:2], 2, R_P + 3))
    o.append(one(proc['2'][:2], (400, 474), R_P + 2, 4))
    o.append(L(250, 312, 250, 386, L2, 2, '6 4', 'm'))
    o.append(one((388, 484), (250, 430), 2, R_P + 3))
    o.append(one((250, 430), (388, 496), R_P + 3, 4).replace('stroke-dasharray', 'stroke-dashoffset:3;stroke-dasharray'))
    for k, (x, y, n) in proc.items():
        o.append(f'<circle cx="{x}" cy="{y}" r="{R_P}" style="fill:{PANEL};stroke:{AC};stroke-width:2"/>')
        o.append(T(x, y - 4, k, 14, fill=AC, bold=True)); o.append(T(x, y + 15, n, 13, bold=True))
    for k, (x, y, n) in ent.items():
        w = 120 if k == 'P' else 150
        o.append(R(x - w / 2, y - 18, w, 36, ACS, AC, 2)); o.append(T(x, y + 5, n, 13, bold=True))
    for k, (x, y, n) in sto.items():
        o.append(R(x - 52, y - 16, 104, 32, FIGBG, FIGBG, 0, 0))
        o.append(L(x - 52, y - 16, x + 52, y - 16, INK, 1.8)); o.append(L(x - 52, y + 16, x + 52, y + 16, INK, 1.8)); o.append(L(x - 52, y - 16, x - 52, y + 16, INK, 1.8))
        o.append(T(x + 2, y + 5, n, 13, bold=True))
    o.append(Tb(250, 352, 'confirmation', 13))
    # legend
    ly = 548
    o.append(L(20, ly, 60, ly, AC, 2, arrow='n')); o.append(T(68, ly + 5, '12 boundary flows: the same 12 as the context diagram', 13, 'start'))
    o.append(L(20, ly + 22, 60, ly + 22, L2, 2, '6 4', 'm')); o.append(T(68, ly + 27, '7 internal flows, new at this level', 13, 'start'))
    o.append(T(700, ly + 5, '12 + 7 = 19 flows', 14, 'end', bold=True))
    o.append(T(700, ly + 27, 'balanced: 12 = 12', 14, 'end', NX, True))
    return ly + 40, ''.join(o)
FIG[8] = (f8, 'Level-1 DFD for rail booking. The solid arrows are the 12 boundary flows, the same 12 that cross the context diagram, so the levels balance; the 7 dashed arrows are new internal flows to and from the stores, giving 19 in all.',
          'A data flow diagram with entities Passenger, Railway Admin and Payment Gateway, processes 1 Enquiry, 2 Booking, 3 Cancel and 4 Maintain, and stores Train Schedule and Ticket. Pairs of solid arrows join entities to processes, 12 in all; 7 dashed arrows link processes and stores.')
AFTER[8] = 2


# ---- 2.9 QFD matrix ----
def f9():
    o = [T(20, 26, 'Hostel mess: what customers want against how the mess can act', 15, 'start', bold=True)]
    x0, y0 = 20, 50
    cw0, cw = 220, 150
    rows = [('tasty food', 5, 9, 1), ('quick service', 3, 1, 9), ('low price', 4, 3, 3)]
    rh = 52
    o.append(R(x0 + cw0, y0, cw, 44, ACS, AC, 4)); o.append(T(x0 + cw0 + cw / 2, y0 + 27, 'menu cycle', 14, bold=True))
    o.append(R(x0 + cw0 + cw, y0, cw, 44, PANEL, AC, 4)); o.append(T(x0 + cw0 + cw * 1.5, y0 + 27, 'counters', 14, bold=True))
    o.append(T(x0 + 10, y0 + 27, 'need (weight)', 14, 'start', MUT))
    y = y0 + 52
    for name, w, m, c in rows:
        o.append(R(x0, y, cw0, rh - 6, PANEL, L2, 4)); o.append(T(x0 + 12, y + 29, f'{name} ({w})', 14, 'start', bold=True))
        for j, v in enumerate((m, c)):
            x = x0 + cw0 + j * cw
            strong = v == 9
            o.append(R(x + 4, y, cw - 8, rh - 6, ACS if strong else FIGBG, AC if strong else L2, 4, 2 if strong else 1.4))
            o.append(T(x + cw / 2, y + 20, str(v), 15, bold=True))
            o.append(T(x + cw / 2, y + 38, f'{w} × {v} = {w * v}', 13, fill=MUT))
        y += rh
    o.append(R(x0, y + 6, cw0, 48, NXS, NX, 4)); o.append(T(x0 + 12, y + 36, 'priority score', 14, 'start', NX, True))
    o.append(R(x0 + cw0 + 4, y + 6, cw - 8, 48, NXS, NX, 4, 2.5)); o.append(T(x0 + cw0 + cw / 2, y + 37, '60', 18, fill=NX, bold=True))
    o.append(R(x0 + cw0 + cw + 4, y + 6, cw - 8, 48, PANEL, L2, 4)); o.append(T(x0 + cw0 + cw * 1.5, y + 37, '44', 18, bold=True))
    xr = x0 + cw0 + 2 * cw + 24
    o.append(T(xr, y0 + 90, 'menu cycle', 14, 'start', bold=True))
    o.append(T(xr, y0 + 112, '45 + 3 + 12 = 60', 14, 'start'))
    o.append(T(xr, y0 + 150, 'counters', 14, 'start', bold=True))
    o.append(T(xr, y0 + 172, '5 + 27 + 12 = 44', 14, 'start'))
    o.append(T(xr, y + 28, 'rank 1: menu cycle', 14, 'start', NX, True))
    o.append(T(xr, y + 48, 'rank 2: counters', 14, 'start'))
    return y + 72, ''.join(o)
FIG[9] = (f9, 'Each cell multiplies a need\'s weight by its strength rating, and each column adds up its cells: the menu cycle scores 5×9 + 3×1 + 4×3 = 60 and ranks first, ahead of the counters at 44.',
          'A matrix with three needs as rows (tasty food weight 5, quick service 3, low price 4) and two responses as columns (menu cycle, counters). Cells hold 9, 1, 3 and 1, 9, 3 with the products. The bottom row gives scores 60 and 44.')


TEXT = {
    2: [('Why is the requirements engineering process drawn as a loop?', 'Why is the requirements engineering process described as a loop?')],
}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d


def text_fixes(k):
    return TEXT.get(k, [])
