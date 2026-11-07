"""Claude's hand-drawn figures for c-os-u6 (Operating Systems, unit 6: protection, security and distributed systems),
one per chapter, from each chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def cross(x, y, r=7, c=LV):
    return L(x - r, y - r, x + r, y + r, c, 2.5) + L(x - r, y + r, x + r, y - r, c, 2.5)


def chip(x, y, w, h, s, kind):
    """kind: 'need' (green), 'extra' (orange), 'off' (empty)"""
    fill, st, col = {'need': (NXS, NX, NX), 'extra': (LVS, LV, LV), 'off': (PANEL, L2, MUT)}[kind]
    return R(x, y, w, h, fill, st, 4, 1.5) + T(x + w / 2, y + h / 2 + 4.5, s, 13, fill=col, bold=kind != 'off')


# ---- 6.1 least privilege: 2 rights needed, 24 granted ----
def f1():
    o = [T(30, 30, 'What check_marks really needs', 15, 'start', bold=True)]
    o.append(chip(30, 44, 190, 32, 'read  results.dat', 'need'))
    o.append(chip(232, 44, 190, 32, 'append  audit.log', 'need'))
    o.append(T(440, 66, '= 2 rights (least privilege)', 14, 'start', NX, True))
    o.append(L(20, 100, 700, 100, LN, 1))
    o.append(T(30, 130, 'What the wide grant gives: read + write on all 12 files', 15, 'start', bold=True))
    names = ['results.dat', 'audit.log'] + [f'marks-{c}' for c in 'ABCDEFGHIJ']
    for i, n in enumerate(names):
        x, y = 30 + (i % 6) * 112, 146 + (i // 6) * 72
        o.append(R(x, y, 104, 62, PANEL, L2, 6, 1.5))
        o.append(T(x + 52, y + 20, n, 13, bold=i < 2))
        o.append(chip(x + 8, y + 30, 40, 24, 'r', 'need' if i == 0 else 'extra'))
        o.append(chip(x + 56, y + 30, 40, 24, 'w', 'need' if i == 1 else 'extra'))
    o.append(chip(30, 304, 26, 20, '', 'need')); o.append(T(64, 319, 'used by the program', 13, 'start', MUT))
    o.append(chip(230, 304, 26, 20, '', 'extra')); o.append(T(264, 319, 'granted but never used', 13, 'start', MUT))
    o.append(T(360, 356, '2 × 12 = 24 rights granted, 24 − 2 = 22 of them excess.', 15, bold=True, fill=LV))
    return 372, ''.join(o)
FIG[1] = (f1, 'check_marks only reads results.dat and appends to audit.log, so least privilege gives it 2 rights. Read and write on all 12 files is 24 rights, 22 of which it never uses.',
          'Two green rights the program needs, above a grid of 12 files each with read and write chips: two chips green, the other 22 orange as excess.')


# ---- 6.2 setuid switches the domain ----
def f2():
    o = []
    def dom(x, title, sub, rows, c, cs):
        o.append(R(x, 20, 270, 196, PANEL, c, 10))
        o.append(R(x, 20, 270, 50, cs, c, 10)); o.append(L(x, 70, x + 270, 70, c, 2))
        o.append(T(x + 135, 42, title, 15, bold=True)); o.append(T(x + 135, 61, sub, 13, fill=MUT))
        for i, (obj, rt, kind) in enumerate(rows):
            y = 100 + i * 38
            o.append(T(x + 14, y, obj, 14, 'start'))
            o.append(T(x + 256, y, rt, 14, 'end', {0: INK, 1: NX, 2: MUT}[kind], kind == 1))
            if i < len(rows) - 1: o.append(L(x + 10, y + 14, x + 260, y + 14, LN, 1))
    dom(20, 'Domain D1', 'shell and its children, uid 1000', [('notes.txt', 'read, write', 0), ('/usr/bin/passwd', 'read, execute', 0),
                                                            ('/etc/shadow', 'nothing', 2), ('other files', 'uid 1000 rights', 0)], AC, ACS)
    dom(430, 'Domain D2', 'passwd running, effective uid 0', [('notes.txt', 'read, write', 0), ('/usr/bin/passwd', 'read, execute', 0),
                                                            ('/etc/shadow', 'read, write', 1), ('other files', 'root rights', 0)], NX, NXS)
    o.append(L(294, 92, 426, 92, NX, 2.5, arrow='x'))
    o.append(T(360, 82, 'exec passwd', 13, fill=NX, bold=True))
    o.append(T(360, 112, 'setuid bit: uid → 0', 13, fill=NX))
    o.append(L(426, 172, 294, 172, AC, 2.5, '6 4', arrow='n'))
    o.append(T(360, 162, 'setuid(1000)', 13, fill=AC, bold=True))
    o.append(T(360, 192, 'saved uid = 1000', 13, fill=AC))
    o.append(boxt(110, 238, 500, 48, ['The shell forks a child and only the child execs passwd,', 'so the shell itself never leaves D1.'], PANEL, L2, 13, dash='6 4'))
    return 300, ''.join(o)
FIG[2] = (f2, 'Running passwd moves the child from D1 (uid 1000) to D2 (uid 0), where it may write /etc/shadow. The saved uid 1000 lets it drop back with setuid(1000); the shell stays in D1 throughout.',
          'Two domain boxes, D1 for uid 1000 with no right on /etc/shadow and D2 for uid 0 with read and write on it, joined by an exec arrow one way and a dashed setuid(1000) arrow back.')


# ---- 6.3 access matrix, 7 of 12 cells filled ----
def f3():
    M = [['r', 'rw', '', 'x'], ['', 'r', 'rw', ''], ['r', '', '', 'rw']]
    x0, y0, cw, ch = 70, 60, 64, 46
    o = [T(x0 + 2 * cw, 30, 'Access matrix: 3 domains × 4 files = 12 cells', 14, bold=True)]
    for j in range(4): o.append(T(x0 + j * cw + cw / 2, y0 - 8, f'F{j + 1}', 14, bold=True))
    for i, row in enumerate(M):
        y = y0 + i * ch
        o.append(T(x0 - 12, y + ch / 2 + 5, f'D{i + 1}', 14, 'end', bold=True))
        for j, v in enumerate(row):
            o.append(R(x0 + j * cw, y, cw, ch, ACS if v else PANEL, AC if v else LN, 0, 1.5))
            o.append(T(x0 + j * cw + cw / 2, y + ch / 2 + 5, v or '—', 15 if v else 13, fill=AC if v else MUT, bold=bool(v)))
    o.append(T(x0 + 2 * cw, y0 + 3 * ch + 26, '7 filled, 5 empty (—)', 14, fill=AC, bold=True))
    o.append(T(x0 + 2 * cw, y0 + 3 * ch + 46, 'Only the filled cells need storing.', 13, fill=MUT))
    # access lists: one per column
    xa = 390
    o.append(T(xa, 34, 'Access lists (one per file)', 14, 'start', bold=True))
    al = ['F1: D1 r, D3 r', 'F2: D1 rw, D2 r', 'F3: D2 rw', 'F4: D1 x, D3 rw']
    for i, s in enumerate(al): o.append(T(xa + 10, 58 + i * 22, s, 14, 'start'))
    o.append(T(700, 58 + 3 * 22, '= 7', 14, 'end', AC, True))
    o.append(L(xa, 160, 700, 160, LN, 1))
    o.append(T(xa, 186, 'Capability lists (one per domain)', 14, 'start', bold=True))
    cl = ['D1: F1 r, F2 rw, F4 x', 'D2: F2 r, F3 rw', 'D3: F1 r, F4 rw']
    for i, s in enumerate(cl): o.append(T(xa + 10, 210 + i * 22, s, 14, 'start'))
    o.append(T(700, 210 + 2 * 22, '= 7', 14, 'end', AC, True))
    o.append(L(x0 + 4 * cw + 14, 128, xa - 12, 100, L2, 1.5, '4 4', arrow='m'))
    o.append(L(x0 + 4 * cw + 14, 152, xa - 12, 220, L2, 1.5, '4 4', arrow='m'))
    o.append(T(360, 300, 'Read by column or by row, the same 7 entries are kept instead of 12.', 14))
    return 316, ''.join(o)
FIG[3] = (f3, 'Cell (D1, F1) holds r, so a process in D1 may read F1. Only 7 of the 12 cells are filled, so a real system stores just those 7, either per file as access lists or per domain as capability lists.',
          'A 3 by 4 matrix of domains D1 to D3 against files F1 to F4 with 7 filled cells, and the same 7 entries written out as access lists per file and as capability lists per domain.')


# ---- 6.4 revoking bob's read: four schemes ----
def f4():
    o = []
    procs = ['P1', 'P4', 'P9', 'P12']
    def panel(x, y, title, steps):
        o.append(R(x, y, 340, 178, PANEL, L2, 10, 1.5))
        o.append(T(x + 14, y + 24, title, 14, 'start', bold=True))
        o.append(f'<rect x="{x + 262:.1f}" y="{y + 9:.1f}" width="66" height="22" rx="11" style="fill:var(--live)"/>')
        o.append(T(x + 295, y + 25, f'{steps} step' + ('s' if steps > 1 else ''), 13, fill='var(--fig)', bold=True))
    def prow(x, y, crossed=False, note=None):
        for i, p in enumerate(procs):
            px = x + i * 74
            o.append(boxt(px, y, 60, 30, [p], PANEL, L2, 13, rx=5))
            if crossed: o.append(cross(px + 54, y + 4, 6))
        return [x + i * 74 + 30 for i in range(4)]
    # (a) access list
    panel(10, 10, '(a) Access list', 1)
    acl = [('raj rw', False), ('bob r', True), ('hr r', False), ('root rw', False)]
    for i, (s, hot) in enumerate(acl):
        cx = 26 + i * 76
        o.append(boxt(cx, 48, 68, 30, [s], LVS if hot else ACS, LV if hot else AC, 13, rx=4))
        if hot: o.append(cross(cx + 64, 50, 6))
    o.append(T(26, 102, 'delete bob’s entry: later checks fail', 13, 'start', NX))
    prow(26, 116)
    o.append(T(26, 170, 'copies already in these 4 stay live', 13, 'start', LV, True))
    # (b) back-pointers
    panel(370, 10, '(b) Back-pointers', 4)
    o.append(boxt(486, 44, 108, 30, ['bob r'], LVS, LV, 13, rx=4))
    xs = prow(386, 126, crossed=True)
    for X in xs: o.append(L(540, 74, X, 124, AC, 1.8, arrow='n'))
    o.append(T(386, 176, 'follow each pointer, delete each copy', 13, 'start', MUT))
    # (c) shared handle
    panel(10, 200, '(c) One shared handle', 1)
    xs = prow(26, 236)
    for X in xs: o.append(L(X, 266, 180, 300, AC, 1.8, arrow='n'))
    o.append(boxt(146, 302, 68, 30, ['h7'], LVS, LV, 14, bold_first=True, rx=4)); o.append(cross(210, 304, 6))
    o.append(T(232, 322, 'delete h7: all 4 fail', 13, 'start', NX))
    # (d) private handles
    panel(370, 200, '(d) One handle per copy', 4)
    xs = prow(386, 236)
    for i, X in enumerate(xs):
        o.append(L(X, 266, X, 296, AC, 1.8, arrow='n'))
        o.append(boxt(X - 30, 300, 60, 30, [f'h{7 + i}'], LVS, LV, 13, rx=4)); o.append(cross(X + 26, 302, 6))
    o.append(T(386, 360, 'delete h7, h8, h9 and h10', 13, 'start', MUT))
    return 392, ''.join(o)
FIG[4] = (f4, 'Bob’s read right sits in four processes. Deleting his access-list entry or one shared handle takes 1 step; back-pointers or one handle per copy take 4. Only the access list leaves the copies already handed out still working.',
          'Four panels for revoking bob’s read right: the access list with bob’s entry crossed, back-pointers to four process copies, four processes sharing one handle h7, and four processes each with its own handle.')


# ---- 6.5 capability check: 2 comparisons ----
def f5():
    o = [boxt(20, 108, 170, 64, ['request from P', 'write on F2'], LVS, LV, 14, bold_first=True)]
    x0, w = 250, 300
    o.append(T(x0 + w / 2, 30, 'P’s capability list', 15, bold=True))
    o.append(T(x0 + 60, 54, 'ticket', 13, fill=MUT)); o.append(T(x0 + 150, 54, 'object', 13, fill=MUT)); o.append(T(x0 + 245, 54, 'rights', 13, fill=MUT))
    rows = [('C1', 'F1', 'read', 1), ('C2', 'F2', 'read-write', 2), ('C3', 'printer', 'write', 0)]
    for i, (c, ob, rt, st) in enumerate(rows):
        y = 64 + i * 52
        hot = st == 2
        o.append(R(x0, y, w, 44, NXS if hot else PANEL, NX if hot else L2, 6, 2 if hot else 1.5))
        o.append(T(x0 + 60, y + 27, c, 14, bold=True)); o.append(T(x0 + 150, y + 27, ob, 14, bold=hot)); o.append(T(x0 + 245, y + 27, rt, 14, bold=hot))
        lab, col = {1: ('1: F1 ≠ F2, go on', MUT), 2: ('2: F2 = F2, match', NX), 0: ('not looked at', MUT)}[st]
        o.append(T(x0 + w + 16, y + 27, lab, 13, 'start', col, st == 2))
    o.append(L(190, 132, 246, 132, LV, 2.5, arrow='l'))
    o.append(T(x0 + 150, 236, 'rights of C2', 13, fill=MUT))
    for j, (b, v) in enumerate((('read', 1), ('write', 1))):
        bx = x0 + 60 + j * 100
        o.append(boxt(bx, 244, 80, 44, [b, str(v)], ACS if j else PANEL, AC if j else L2, 14, fills=[MUT, AC if j else INK]))
    o.append(T(x0 + w + 16, 272, 'write bit = 1: allowed,', 14, 'start', NX, True))
    o.append(T(x0 + w + 16, 290, 'no access list read', 13, 'start', MUT))
    o.append(T(360, 330, 'Handing C2 to a child is legal only if C2 also carries the copy right.', 14))
    return 346, ''.join(o)
FIG[5] = (f5, 'The kernel scans P’s capability list: C1 names F1 and is passed over, C2 names F2 and matches on the second comparison, and its write bit is 1, so the write is allowed without reading any access list.',
          'A request for write on F2 checked against three capabilities: C1 is skipped, C2 for F2 read-write matches on the second comparison, and its write bit of 1 allows the request.')


# ---- 6.6 password space: same recipe, two alphabets ----
def f6():
    o = []
    cols = [(10, 150), (196, 170), (402, 150), (588, 124)]
    heads = ['alphabet, length', 'passwords A⁸', 'average: half', 'at 10⁹ per second']
    for (x, w), h in zip(cols, heads): o.append(T(x + w / 2, 30, h, 13, fill=MUT))
    def row(y, name, cells, tc, ts):
        o.append(T(14, y - 10, name, 14, 'start', bold=True))
        for i, ((x, w), lines) in enumerate(zip(cols, cells)):
            last = i == 3
            o.append(boxt(x, y, w, 56, lines, ts if last else PANEL, tc if last else L2, 14, bold_first=last))
            if i < 3: o.append(L(x + w + 4, y + 28, cols[i + 1][0] - 4, y + 28, AC, 2, arrow='n'))
    row(70, 'Case 1: lowercase only', [['26 letters', '8 long'], ['26⁸ =', '2.09 × 10¹¹'], ['1.04 × 10¹¹', 'guesses'], ['104.4 s', 'under 2 min']], AC, ACS)
    row(184, 'Case 2: a–z, A–Z, 0–9', [['62 characters', '8 long'], ['62⁸ =', '2.18 × 10¹⁴'], ['1.09 × 10¹⁴', 'guesses'], ['109,170 s', '30.3 hours']], LV, LVS)
    o.append(L(650, 130, 650, 180, LV, 2.5, arrow='l'))
    o.append(T(640, 160, '× 1046', 15, 'end', LV, True))
    o.append(T(360, 280, 'Same length, wider alphabet: about 1000 times more guesses to try.', 14, bold=True))
    return 296, ''.join(o)
FIG[6] = (f6, 'Both cases follow the same steps: count A⁸ passwords, halve for the average, divide by 10⁹ guesses a second. Going from 26 to 62 characters turns 104.4 s into 109,170 s (30.3 hours), 1046 times longer.',
          'Two rows of four boxes: 26 letters giving 2.09 × 10¹¹ passwords and 104.4 seconds, and 62 characters giving 2.18 × 10¹⁴ passwords and 30.3 hours, with a × 1046 arrow between the times.')


# ---- 6.7 Lamport clocks ----
def f7():
    ys = {'P1': 80, 'P2': 180, 'P3': 280}
    o = [R(84, 44, 52, 262, NXS, NXS, 8, 0)]
    for p, y in ys.items():
        o.append(T(40, y + 5, p, 15, 'end', bold=True))
        o.append(L(56, y, 700, y, L2, 2, arrow='m'))
    ev = [('P1', 110, 'a', 1, 'c'), ('P1', 210, 'send m1', 2, 'n'), ('P1', 650, 'receive m3', 7, 'r'),
          ('P2', 110, 'd', 1, 'c'), ('P2', 300, 'receive m1', 3, 'n'), ('P2', 420, 'send m2', 4, 'n'),
          ('P3', 110, 'g', 1, 'c'), ('P3', 510, 'receive m2', 5, 'n'), ('P3', 600, 'send m3', 6, 'n')]
    pos = {}
    for p, x, lab, ts, kind in ev:
        y = ys[p]; pos[lab] = (x, y)
        c = {'c': NX, 'n': AC, 'r': LV}[kind]
        o.append(C(x, y, 7, c))
        below = lab.startswith('receive')
        o.append(Tb(x, y + 28 if below else y - 14, f'{lab}: {ts}', 13, fill=c, bold=True))
    for a, b, m, side in (('send m1', 'receive m1', 'm1 carries 2', 1), ('send m2', 'receive m2', 'm2 carries 4', 1), ('send m3', 'receive m3', 'm3 carries 6', -1)):
        (x1, y1), (x2, y2) = pos[a], pos[b]
        k = 9 / ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        c = LV if m[1] == '3' else AC
        o.append(L(x1, y1, x2 - (x2 - x1) * k, y2 - (y2 - y1) * k, c, 2, arrow='l' if m[1] == '3' else 'n'))
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        o.append(Tb(mx + 12 * side, my + 4, m, 13, 'start' if side > 0 else 'end', fill=c))
    o.append(T(110, 330, 'a, d and g: all 1, no message links them, so concurrent', 13, 'start', NX, True))
    o.append(T(700, 360, 'P1 still holds 2 when m3 arrives: max(2, 6) + 1 = 7', 14, 'end', LV, True))
    return 376, ''.join(o)
FIG[7] = (f7, 'Each event adds 1 to its own process’s counter, and a message carries the sender’s value. When m3 reaches P1 its counter is still 2, so the receive gets max(2, 6) + 1 = 7.',
          'Three process timelines P1, P2 and P3 with events labelled by Lamport timestamps 1 to 7, and messages m1, m2 and m3 drawn as arrows from sender to receiver.')


# ---- 6.8 client cache: average read time vs hit ratio ----
def f8():
    x0, x1, y0, y1 = 80, 680, 60, 300
    fx = lambda h: x0 + h * (x1 - x0)
    fy = lambda t: y1 - t / 20 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [0, 0.2, 0.4, 0.6, 0.8, 1.0], [0, 5, 10, 15, 20], fx, fy, 'cache hit ratio h', 'average time per block (ms)', lambda v: f'{v:g}')]
    o.append(P([(fx(0), fy(20)), (fx(1), fy(0.1))], AC, 3))
    o.append(L(fx(0.9), fy(2.09), fx(0.9), y1, INK, 1.5, '4 4')); o.append(L(x0, fy(2.09), fx(0.9), fy(2.09), INK, 1.5, '4 4'))
    o.append(C(fx(0.9), fy(2.09), 6, AC)); o.append(C(fx(0), fy(20), 6, LV))
    o.append(T(fx(0) + 16, fy(20) + 2, 'no cache: 20 ms a block, 1000 blocks = 20 s', 13, 'start', LV, True))
    o.append(T(fx(0.66), fy(17.4), 'h = 0.9:', 14, 'start', AC, True))
    o.append(T(fx(0.66), fy(16.2), '0.9 × 0.1 + 0.1 × 20', 14, 'start'))
    o.append(T(fx(0.66), fy(15.0), '= 2.09 ms a block', 14, 'start', AC, True))
    o.append(T(fx(0.66), fy(13.8), '1000 blocks = 2.09 s', 14, 'start', AC))
    o.append(L(fx(0.9), fy(12.8), fx(0.9), fy(2.09) - 9, AC, 1.5))
    o.append(T(380, 382, 'The 10% of misses cost 2.0 of the 2.09 ms, so misses decide the average.', 14))
    return 396, ''.join(o)
FIG[8] = (f8, 'The average time per block falls in a straight line from 20 ms with no cache to 0.1 ms when every read hits. At hit ratio 0.9 it is 2.09 ms, so 1000 blocks take 2.09 s instead of 20 s.',
          'A falling line of average read time from 20 ms at hit ratio 0 to 0.1 ms at hit ratio 1, with the point h = 0.9, 2.09 ms marked.')


# ---- 6.9 mode 754 for bob ----
def f9():
    o = [T(360, 30, 'mode 754, owner alice, group exam', 15, bold=True)]
    fields = [('7', 'owner (alice)', [1, 1, 1], '4 + 2 + 1'), ('5', 'group (exam)', [1, 0, 1], '4 + 0 + 1'), ('4', 'others', [1, 0, 0], '4 + 0 + 0')]
    for i, (d, who, bits, sm) in enumerate(fields):
        x = 40 + i * 230
        hot = i == 1
        c = AC if hot else L2
        o.append(R(x, 46, 180, 196, ACS if hot else PANEL, c, 10, 2.5 if hot else 1.5))
        o.append(T(x + 90, 92, d, 34, fill=AC if hot else MUT, bold=True))
        o.append(T(x + 90, 116, who, 14, fill=INK if hot else MUT, bold=hot))
        for j, (b, on) in enumerate(zip('rwx', bits)):
            bx = x + 12 + j * 54
            o.append(R(bx, 130, 48, 44, (NXS if on else PANEL) if hot else PANEL, (NX if on else L2) if hot else LN, 6, 1.5))
            o.append(T(bx + 24, 158, b if on else '-', 17, fill=(NX if on else MUT) if hot else MUT, bold=on))
        o.append(T(x + 90, 198, sm, 13, fill=MUT))
        o.append(T(x + 90, 224, ['rwx', 'r-x', 'r--'][i], 15, fill=AC if hot else MUT, bold=hot))
    o.append(T(130, 270, 'bob is not alice: skip', 13, fill=MUT))
    o.append(T(590, 270, 'not reached', 13, fill=MUT))
    o.append(boxt(240, 290, 240, 40, ['bob, in group exam'], PANEL, INK, 14, bold_first=True))
    o.append(L(360, 288, 360, 248, AC, 2.5, arrow='n'))
    o.append(T(360, 360, 'Group field r-x: bob may read and execute, but not write.', 15, bold=True, fill=AC))
    return 376, ''.join(o)
FIG[9] = (f9, 'Mode 754 splits into owner 7 (rwx), group 5 (r-x) and others 4 (r--). Bob is not the owner but is in group exam, so the group field decides: he may read and execute the file, not write it.',
          'Three boxes for the digits 7, 5 and 4 of mode 754, each split into r, w and x bits, with the group box 5 = r-x highlighted and an arrow from bob, a member of group exam, to it.')


spec = make_spec(FIG)
