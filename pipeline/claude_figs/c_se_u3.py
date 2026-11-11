"""Claude's hand-drawn figures for c-se-u3 (Software Engineering, unit 3: design, architecture and UML), one per chapter,
from each chapter's worked example, plus the sentences in the chapter text that describe a figure or need a fix (text_fixes)."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {}


def cls(x, y, w, name, rows=(), fill=PANEL, st=AC, size=14):
    h = 30 + (18 * len(rows) + 10 if rows else 0)
    o = R(x, y, w, h, fill, st, 4) + T(x + w / 2, y + 20, name, size, bold=True)
    if rows:
        o += L(x, y + 30, x + w, y + 30, st, 1.4)
        for i, r in enumerate(rows):
            o += T(x + 10, y + 47 + i * 18, r, 13, 'start', MUT)
    return o, h


def diamond(x, y, ang, c=AC, filled=True, s=9):
    """diamond whose far tip is at (x,y), pointing in direction ang (radians) away from the line"""
    ca, sa = math.cos(ang), math.sin(ang)
    pts = [(x, y), (x + s * ca - s * 0.6 * sa, y + s * sa + s * 0.6 * ca), (x + 2 * s * ca, y + 2 * s * sa), (x + s * ca + s * 0.6 * sa, y + s * sa - s * 0.6 * ca)]
    return f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pts)}" style="fill:{c if filled else FIGBG};stroke:{c};stroke-width:2"/>'


# ---- 3.1 quality attributes need named design decisions ----
def f1():
    o = [T(20, 26, 'Ticket site: 99.9 % availability over a 365-day year', 15, 'start', bold=True)]
    x0, w = 20, 680
    o.append(R(x0, 44, w, 40, NXS, NX, 4))
    o.append(T(x0 + w / 2 - 20, 69, 'up: 99.9 % of 365 × 24 = 8760 h', 14, bold=True))
    o.append(R(x0 + w - 6, 44, 6, 40, LVS, LV, 0, 2))
    o.append(L(x0 + w - 3, 86, x0 + w - 3, 104, LV, 1.6))
    o.append(T(x0 + w, 122, 'down: 0.001 × 8760 h = 8.76 h ≈ 8 h 46 min a year', 14, 'end', LV, True))
    # two attributes -> decisions
    yy = 150
    items = [('availability', 'a dependability attribute', 'run two copies of the booking', 'service behind a load balancer', 'one server can fail and bookings go on'),
             ('40,000 users at 10 a.m.', 'a performance attribute', 'keep the seat map in a cache', 'and the seat lock in memory', 'a page view does not hit the database')]
    for i, (a, b, d1, d2, why) in enumerate(items):
        y = yy + i * 104
        o.append(boxt(20, y, 250, 76, [a, b], LVS if i == 0 else ACS, LV if i == 0 else AC, 14, True))
        o.append(L(274, y + 38, 330, y + 38, AC, 2, arrow='n'))
        o.append(boxt(334, y, 366, 76, [d1, d2, why], PANEL, AC, 13))
    o.append(T(20, yy + 222, 'Each quality attribute is bought by a named design decision, and each decision has a cost.', 13, 'start', MUT))
    return yy + 236, ''.join(o)
FIG[1] = (f1, '99.9 % availability leaves 0.001 of the 8760-hour year for downtime, 8.76 h or about 8 h 46 min. Each attribute is then met by a named design decision: two copies behind a load balancer, and a cached seat map.',
          'A long green bar for the 8760 hours of a year with a thin red sliver at the end for 8.76 hours of allowed downtime. Below, availability leads to two copies behind a load balancer, and 40,000 users at 10 a.m. leads to a cached seat map.')


# ---- 3.2 cohesion and coupling of Billing ----
def f2():
    o = [T(20, 24, 'Before: one class, four unrelated jobs', 15, 'start', bold=True)]
    a, h = cls(20, 40, 250, 'Billing', ['computeGst()', 'printReceipt()', 'writeRowToMySQL()', 'sendSms()'], LVS, LV)
    o.append(a)
    o.append(T(290, 80, 'cohesion 1', 15, 'start', LV, True))
    o.append(T(290, 102, 'coincidental: the jobs share', 13, 'start', MUT))
    o.append(T(290, 120, 'no data and no order', 13, 'start', MUT))
    y = 40 + h + 28
    o.append(L(20, y - 12, 700, y - 12, LN, 1))
    o.append(T(20, y + 12, 'After: 4 single-job classes + Billing as controller = 5 classes', 15, 'start', bold=True))
    ctrl_y = y + 30
    o.append(boxt(270, ctrl_y, 180, 40, ['Billing (controller)'], PANEL, AC, 14, True))
    kids = [('GstCalculator', 'data: amount', '5', NX), ('ReceiptPrinter', '', '', None), ('BillRepository', 'stamp: whole Bill', '4', LV), ('SmsNotifier', '', '', None)]
    kw, gap = 158, 16
    ky = ctrl_y + 130
    for i, (n, lab, sc, c) in enumerate(kids):
        kx = 20 + i * (kw + gap)
        o.append(boxt(kx, ky, kw, 52, [n, 'cohesion 7'], NXS, NX, 13, True))
        x1 = 360 + (i - 1.5) * 40
        o.append(L(x1, ctrl_y + 42, kx + kw / 2, ky - 2, c or L2, 2, arrow={NX: 'x', LV: 'l'}.get(c, 'm')))
        if lab:
            lx = (x1 + kx + kw / 2) / 2
            o.append(Tb(lx, ctrl_y + 84, f'{lab}, coupling {sc}', 13, fill=c, bold=True))
    o.append(R(20, ky + 72, 680, 44, LVS, LV, 6))
    o.append(T(36, ky + 99, 'Fix: pass only billId and amount to BillRepository, and stamp coupling 4 becomes data coupling 5.', 13, 'start'))
    return ky + 130, ''.join(o)
FIG[2] = (f2, 'Billing doing four unrelated jobs has cohesion 1. Split into four single-job classes plus Billing as controller, it becomes 5 classes with cohesion 7 each; the call to GstCalculator passes simple data (coupling 5), while passing the whole Bill to BillRepository is stamp coupling 4 until only billId and amount go across.',
          'Top: one Billing class with four unrelated operations, labelled cohesion 1. Bottom: Billing as a controller with arrows to GstCalculator (data coupling 5), ReceiptPrinter, BillRepository (stamp coupling 4) and SmsNotifier, each class labelled cohesion 7.')


# ---- 3.3 pipe and filter bottleneck ----
def f3():
    o = [T(20, 24, 'Log pipeline: records arrive at 100 per second', 15, 'start', bold=True)]
    filt = [('parse', 4, '250 /s'), ('validate', 6, '166.7 /s'), ('format', 2, '500 /s')]
    s = 22
    x, y = 40, 60
    o.append(L(4, y + 30, x - 2, y + 30, AC, 2, arrow='n'))
    for i, (n, ms, cap) in enumerate(filt):
        w = ms * s + 40
        hot = n == 'validate'
        o.append(R(x, y, w, 60, LVS if hot else PANEL, LV if hot else AC, 6, 2.5 if hot else 2))
        o.append(T(x + w / 2, y + 26, n, 14, fill=LV if hot else INK, bold=True))
        o.append(T(x + w / 2, y + 46, f'{ms} ms', 13, fill=MUT))
        o.append(T(x + w / 2, y + 84, f'1 ÷ 0.00{ms} s = {cap}', 13, fill=LV if hot else MUT, bold=hot))
        x += w
        o.append(L(x + 2, y + 30, x + 50, y + 30, AC, 2, arrow='n'))
        x += 54
    o.append(T(20, y + 124, 'Latency of one record (empty pipeline) = 4 + 6 + 2 = 12 ms', 14, 'start', bold=True))
    o.append(T(20, y + 148, 'Capacity = slowest filter = 166.7 records/s; arrivals are 100/s, so throughput = 100/s', 14, 'start', LV, True))
    # second copy
    y2 = y + 186
    o.append(L(20, y2 - 14, 700, y2 - 14, LN, 1))
    o.append(T(20, y2 + 10, 'Add a second validate filter', 15, 'start', bold=True))
    xs = 40
    o.append(boxt(xs, y2 + 48, 128, 50, ['parse', '250 /s'], LVS, LV, 13, True))
    o.append(boxt(xs + 190, y2 + 22, 140, 44, ['validate', ''], PANEL, AC, 13, True))
    o.append(boxt(xs + 190, y2 + 80, 140, 44, ['validate', ''], PANEL, AC, 13, True))
    o.append(T(xs + 260, y2 + 146, '2 ÷ 0.006 s = 333.3 /s', 13, fill=MUT, bold=True))
    o.append(boxt(xs + 392, y2 + 48, 110, 50, ['format', '500 /s'], PANEL, AC, 13, True))
    o.append(L(xs + 130, y2 + 66, xs + 188, y2 + 46, AC, 2, arrow='n')); o.append(L(xs + 130, y2 + 80, xs + 188, y2 + 100, AC, 2, arrow='n'))
    o.append(L(xs + 332, y2 + 46, xs + 390, y2 + 66, AC, 2, arrow='n')); o.append(L(xs + 332, y2 + 100, xs + 390, y2 + 80, AC, 2, arrow='n'))
    o.append(T(xs + 530, y2 + 62, 'now parse is', 13, 'start', LV, True))
    o.append(T(xs + 530, y2 + 80, 'the bottleneck:', 13, 'start', LV, True))
    o.append(T(xs + 530, y2 + 98, 'capacity 250 /s', 13, 'start', LV, True))
    return y2 + 162, ''.join(o)
FIG[3] = (f3, 'Each filter can pass 1 ÷ (its time) records a second, so validate at 6 ms caps the pipeline at 166.7 records per second, and one record needs 4 + 6 + 2 = 12 ms. A second validate copy gives validate 333.3 per second, and parse at 250 per second becomes the new limit.',
          'Three filter boxes in a row: parse 4 ms (250 per second), validate 6 ms (166.7 per second, highlighted) and format 2 ms (500 per second). Below, two validate boxes in parallel giving 333.3 per second, with parse at 250 per second marked as the new bottleneck.')
AFTER[3] = 2


# ---- 3.4 observer, adapter, facade ----
def f4():
    o = []
    cw, gap = 220, 20
    heads = ['(a) observer', '(b) adapter', '(c) facade']
    for i, hd in enumerate(heads):
        x = 20 + i * (cw + gap)
        o.append(R(x, 16, cw, 360, FIGBG, L2, 8, 1.5))
        o.append(T(x + cw / 2, 42, hd, 15, fill=AC, bold=True))
    # observer
    x = 20
    o.append(boxt(x + 50, 60, 120, 40, ['price feed'], ACS, AC, 14, True))
    for j in range(5):
        cx = x + 30 + j * 40
        o.append(L(x + 110, 102, cx, 148, AC, 1.6, arrow='n'))
        o.append(R(cx - 14, 150, 28, 22, PANEL, AC, 3))
    o.append(T(x + cw / 2, 194, '500 clients', 13, fill=MUT))
    o.append(T(x + 12, 226, 'push: 20 changes/s × 500', 13, 'start'))
    o.append(T(x + 12, 246, '= 10,000 updates/s', 14, 'start', NX, True))
    o.append(T(x + 12, 280, 'poll every 0.1 s: 10/s × 500', 13, 'start'))
    o.append(T(x + 12, 300, '= 5,000 requests/s,', 14, 'start', LV, True))
    o.append(T(x + 12, 320, 'even when nothing changed', 13, 'start', MUT))
    # adapter
    x = 20 + cw + gap
    o.append(boxt(x + 30, 60, 160, 50, ['new app', 'pays ₹250.75'], PANEL, AC, 13, True))
    o.append(L(x + 110, 112, x + 110, 140, AC, 2, arrow='n'))
    o.append(boxt(x + 30, 142, 160, 62, ['adapter', '250.75 × 100', '= 25,075 paise'], ACS, AC, 13, True))
    o.append(L(x + 110, 206, x + 110, 234, AC, 2, arrow='n'))
    o.append(boxt(x + 20, 236, 180, 50, ['old bank API', 'debitAcct(acct, 25075)'], PANEL, L2, 13, True))
    o.append(T(x + cw / 2, 320, 'converts; adds no function', 13, fill=MUT))
    # facade
    x = 20 + 2 * (cw + gap)
    o.append(boxt(x + 40, 60, 140, 40, ['dashboard screen'], PANEL, AC, 13, True))
    o.append(L(x + 110, 102, x + 110, 126, AC, 2, arrow='n'))
    o.append(boxt(x + 30, 128, 160, 40, ['DashboardFacade'], ACS, AC, 13, True))
    for j in range(30):
        cx, cy = x + 22 + (j % 10) * 18, 196 + (j // 10) * 18
        o.append(R(cx, cy, 12, 12, PANEL, L2, 2, 1.2))
    o.append(L(x + 110, 170, x + 110, 192, L2, 1.6, arrow='m'))
    o.append(T(x + cw / 2, 270, '30 subsystems hidden', 13, fill=MUT))
    o.append(T(x + cw / 2, 300, 'one method per panel,', 13))
    o.append(T(x + cw / 2, 320, 'e.g. loadSalesPanel()', 13))
    return 392, ''.join(o)
FIG[4] = (f4, 'Observer pushes each of 20 price changes a second to 500 clients, 10,000 updates, where polling every 100 ms costs 5,000 requests a second even when nothing changes. The adapter turns ₹250.75 into 25,075 paise for the old API, and one facade hides 30 subsystems.',
          'Three panels. Observer: a price feed with arrows to many clients, push 10,000 per second against polling 5,000 per second. Adapter: new app, adapter converting 250.75 rupees to 25,075 paise, old bank API. Facade: a screen calling one facade in front of 30 small subsystem boxes.')


# ---- 3.5 bill payment form before and after ----
def field(x, y, w, label, val, mem=False, ro=False):
    o = T(x, y, label, 13, 'start', LV if mem else MUT, mem)
    if ro:
        o += T(x, y + 24, val, 15, 'start', INK, True)
    else:
        o += R(x, y + 6, w, 30, PANEL, LV if mem else L2, 4, 2 if mem else 1.5) + T(x + 10, y + 26, val, 13, 'start', MUT)
    return o


def f5():
    o = []
    for i, hd in enumerate(['Before: 4 boxes, 3 things to remember', 'After: 1 box, 1 thing to remember']):
        x = 20 + i * 350
        o.append(T(x, 24, hd, 14, 'start', bold=True))
        o.append(R(x, 36, 330, 330, FIGBG, L2, 10, 1.5))
    x = 36
    o.append(field(x, 64, 296, 'Consumer number (12 digits)  memory 1', '', True))
    o.append(field(x, 124, 296, 'Amount  memory 2', '₹', True))
    o.append(field(x, 184, 296, 'Amount again', '₹'))
    o.append(field(x, 244, 296, 'Bill ID from this morning\'s SMS  memory 3', '', True))
    o.append(R(x, 304, 120, 34, LVS, LV, 6)); o.append(T(x + 60, 326, 'Pay', 14, fill=LV, bold=True))
    o.append(T(x + 136, 326, 'no bill shown, no cancel', 13, 'start', LV))
    x = 386
    o.append(field(x, 64, 296, 'Consumer number  memory 1', '', True))
    o.append(R(x, 116, 140, 30, ACS, AC, 6)); o.append(T(x + 70, 136, 'Fetch bill', 13, fill=AC, bold=True))
    o.append(R(x, 160, 296, 104, PANEL, NX, 6))
    o.append(T(x + 12, 184, 'Bill fetched', 13, 'start', NX, True))
    o.append(T(x + 12, 206, 'bill ID arrives with it', 13, 'start', MUT))
    o.append(T(x + 12, 228, 'Amount (read-only)', 13, 'start', MUT))
    o.append(T(x + 12, 250, '₹ shown, not typed', 14, 'start', bold=True))
    o.append(R(x, 304, 90, 34, NXS, NX, 6)); o.append(T(x + 45, 326, 'Pay', 14, fill=NX, bold=True))
    o.append(R(x + 104, 304, 100, 34, PANEL, L2, 6)); o.append(T(x + 154, 326, 'Cancel', 14, bold=True))
    o.append(T(20, 392, 'Boxes 4 → 1 (3 removed); memory items 3 → 1 (2 removed); the user sees the bill and can cancel.', 14, 'start', bold=True))
    return 406, ''.join(o)
FIG[5] = (f5, 'Before, the payment form has 4 input boxes and makes the user remember 3 things. After the redesign the consumer number fetches the bill, the amount is shown read-only and the bill ID comes with the bill: 1 box, 1 thing to remember, and a Cancel button.',
          'Two phone forms side by side. Before: consumer number, amount, amount again and bill ID boxes, three of them marked as memory items, and a Pay button. After: one consumer number box, a Fetch bill button, a read-only bill panel, and Pay and Cancel buttons.')
AFTER[5] = 2


# ---- 3.6 bank class diagram ----
def f6():
    o = []
    a, ha = cls(270, 30, 180, 'Account', ['accountNo', 'balance'], ACS, AC); o.append(a)
    b, hb = cls(20, 30, 160, 'Customer', ['customerId', 'name']); o.append(b)
    c, hc = cls(540, 30, 160, 'Branch', ['branchCode']); o.append(c)
    d, hd = cls(270, 236, 180, 'Transaction', ['txnId', 'amount']); o.append(d)
    o.append(L(180, 70, 270, 70, AC, 2)); o.append(T(186, 62, '1..*', 13, 'start', bold=True)); o.append(T(264, 62, '1..*', 13, 'end', bold=True))
    o.append(L(450, 70, 540, 70, AC, 2)); o.append(T(456, 62, '0..*', 13, 'start', bold=True)); o.append(T(534, 62, '1', 13, 'end', bold=True))
    o.append(L(360, 30 + ha + 18, 360, 236, LV, 2.5)); o.append(diamond(360, 30 + ha, math.pi / 2, LV))
    o.append(T(368, 30 + ha + 34, '1', 13, 'start', bold=True)); o.append(T(368, 228, '0..*', 13, 'start', bold=True))
    o.append(T(380, 178, 'composition: a transaction', 13, 'start', LV))
    o.append(T(380, 196, 'dies with its account', 13, 'start', LV))
    o.append(R(20, 160, 220, 58, FIGBG, L2, 4, 1.4, '4 3'))
    o.append(T(30, 182, '{joint accounts have', 13, 'start', MUT)); o.append(T(30, 202, ' 2..* holders}', 13, 'start', MUT))
    o.append(L(130, 160, 220, 74, L2, 1.4, '4 3'))
    o.append(T(20, 336, 'Read each number at the far end: one customer holds 1..* accounts; one account has 1..* holders.', 13, 'start', MUT))
    o.append(T(20, 358, '4 classes · Customer 1..* — 1..* Account · Branch 1 — 0..* Account · Account 1 — 0..* Transaction', 13, 'start', bold=True))
    return 372, ''.join(o)
FIG[6] = (f6, 'The bank has 4 classes. Customer and Account are 1..* at both ends, a Branch holds 0..* accounts, and the filled diamond on Account–Transaction is composition: a transaction cannot outlive its account. The joint-account rule is a constraint, not a multiplicity.',
          'Class boxes Customer, Account, Branch and Transaction. Customer to Account is 1..* to 1..*, Branch to Account is 1 to 0..*, and Account to Transaction is 1 to 0..* with a filled diamond at Account. A dashed note carries the constraint joint accounts have 2..* holders.')


# ---- 3.7 sequence and collaboration views ----
def f7():
    o = [T(20, 24, 'Sequence diagram', 15, 'start', bold=True), T(430, 24, 'Collaboration diagram', 15, 'start', bold=True)]
    xs = {'User': 60, 'ATM': 200, 'Bank': 330}
    for n, x in xs.items():
        o.append(boxt(x - 44, 38, 88, 32, [n], PANEL, AC, 14, True))
        o.append(L(x, 70, x, 400, L2, 1.4, '5 4'))
    msgs = [('User', 'ATM', 'insert card', False), ('ATM', 'Bank', 'verify PIN', False), ('Bank', 'ATM', 'OK', True),
            ('User', 'ATM', 'withdraw ₹2,000', False), ('ATM', 'Bank', 'debit ₹2,000', False), ('Bank', 'ATM', 'approved', True), ('ATM', 'User', 'cash', True)]
    y = 104
    for a, b, lab, ret in msgs:
        x1, x2 = xs[a], xs[b]
        d = 1 if x2 > x1 else -1
        o.append(L(x1 + d * 5, y, x2 - d * 6, y, L2 if ret else AC, 2, '6 4' if ret else None, 'm' if ret else 'n'))
        o.append(T((x1 + x2) / 2, y - 7, lab, 13, fill=MUT if ret else INK))
        y += 42
    o.append(T(20, 420, 'time runs down the page: 7 arrows', 13, 'start', MUT))
    o.append(L(400, 16, 400, 420, LN, 1))
    # collaboration
    pos = {'User': (480, 110), 'ATM': (600, 220), 'Bank': (600, 360)}
    o.append(L(500, 128, 580, 202, AC, 2)); o.append(L(600, 240, 600, 340, AC, 2))
    for n, (x, y) in pos.items():
        o.append(boxt(x - 44, y - 16, 88, 32, [n], PANEL, AC, 14, True))
    o.append(T(430, 166, '1: insert card', 13, 'start')); o.append(T(430, 184, '2: withdraw ₹2,000', 13, 'start'))
    o.append(T(430, 202, '2 (return): cash', 13, 'start', MUT))
    o.append(T(612, 266, '1.1: verify PIN', 13, 'start')); o.append(T(612, 284, '1.1 (return): OK', 13, 'start', MUT))
    o.append(T(612, 302, '2.1: debit ₹2,000', 13, 'start')); o.append(T(612, 320, '2.1 (return)', 13, 'start', MUT))
    o.append(T(430, 400, '2 links: User–ATM 3 messages,', 13, 'start', bold=True))
    o.append(T(430, 418, 'ATM–Bank 4; 3 + 4 = 7', 13, 'start', bold=True))
    return 432, ''.join(o)
FIG[7] = (f7, 'The same ATM scenario in both views. The sequence diagram puts time down the page, 4 calls and 3 dashed returns; the collaboration diagram puts the same 7 messages on 2 links and keeps the order in the numbers 1, 1.1, 2, 2.1.',
          'Left: a sequence diagram with lifelines User, ATM and Bank and seven arrows from insert card down to cash, returns dashed. Right: a collaboration diagram with User linked to ATM and ATM linked to Bank, the messages numbered 1, 1.1, 2 and 2.1.')


# ---- 3.8 food-order state chart ----
def f8():
    o = []
    names = ['Placed', 'Accepted', 'Preparing', 'Out for delivery', 'Delivered']
    xs = [94, 224, 356, 502, 648]
    y = 90
    ws = [100, 110, 114, 148, 104]
    o.append(C(14, y, 8, INK)); o.append(L(22, y, xs[0] - ws[0] / 2 - 3, y, INK, 2, arrow='n'))
    for i, (n, x, w) in enumerate(zip(names, xs, ws)):
        st = NX if n == 'Delivered' else AC
        o.append(R(x - w / 2, y - 22, w, 44, NXS if n == 'Delivered' else PANEL, st, 20))
        o.append(T(x, y + 5, n, 14 if len(n) < 12 else 13, bold=True))
        if i < 4:
            o.append(L(x + w / 2 + 2, y, xs[i + 1] - ws[i + 1] / 2 - 3, y, AC, 2, arrow='n'))
    o.append(f'<circle cx="{xs[4]}" cy="{y + 74}" r="10" style="fill:none;stroke:{INK};stroke-width:2"/>' + C(xs[4], y + 74, 6, INK))
    o.append(L(xs[4], y + 22, xs[4], y + 61, INK, 2, arrow='n'))
    cy = 300
    o.append(R(224 - 70, cy - 22, 140, 44, LVS, LV, 20)); o.append(T(224, cy + 5, 'Cancelled', 14, fill=LV, bold=True))
    for x in xs[:3]:
        o.append(L(x, y + 22, 224 + (x - 224) * 0.35, cy - 24, LV, 2, arrow='l'))
    o.append(Tb(224, 200, 'cancel', 13, fill=LV))
    o.append(L(502, y + 30, 502, cy - 30, L2, 1.5, '5 4'))
    o.append(T(510, 210, 'no cancel arrow here,', 13, 'start', LV, True))
    o.append(T(510, 228, 'so a late cancel is impossible', 13, 'start', LV))
    o.append(T(20, 360, '6 named states; 4 forward + 3 cancel = 7 transitions. The start dot and end bullseye are not states.', 13, 'start', bold=True))
    return 374, ''.join(o)
FIG[8] = (f8, 'A food order\'s six named states and seven transitions: four forward along the top and three cancel arrows into Cancelled. There is no cancel arrow from Out for delivery, so a late cancellation cannot happen.',
          'A state chart: start dot, then Placed, Accepted, Preparing, Out for delivery and Delivered joined by forward arrows, ending in a bullseye. Three red arrows lead from Placed, Accepted and Preparing down to Cancelled; Out for delivery has none.')


TEXT = {
    2: [('The figure splits a payroll system into three functions, with deductions split once more into PF and income tax.',
         'A payroll system, for example, splits into three functions, and its deductions function splits once more into PF and income tax.')],
    3: [('The bottleneck is validate. Two copies of validate working in parallel give 2 ÷ 0.006 s = 333.3 records per second of capacity.',
         'The bottleneck is validate. Two copies of validate working in parallel give validate 2 ÷ 0.006 s = 333.3 records per second, so parse (1 ÷ 0.004 s = 250 records per second) becomes the new bottleneck and the pipeline\'s capacity rises to 250 records per second.'),
        ('The bottleneck is validate; a second validate filter raises capacity to about 333.3 records per second.',
         'The bottleneck is validate; a second validate filter lifts validate to about 333.3 records per second, so parse becomes the bottleneck and the pipeline\'s capacity rises to 250 records per second.')],
}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d


def text_fixes(k):
    return TEXT.get(k, [])
