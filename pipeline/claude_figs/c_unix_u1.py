"""Claude's hand-drawn figures for c-unix-u1 (Linux and Shell Programming, unit 1: Unix and Linux basics), one per
chapter, from each chapter's worked example, plus text fixes (a quiz question that pointed at a figure that never showed
distribution families)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *
import unix_text

FIG = {}
AFTER = {}


# ---- 1.1 four dates on one time line ----
def f1():
    x0, x1, y = 50, 680, 170
    fx = lambda yr: x0 + (yr - 1966) / (1997 - 1966) * (x1 - x0)
    o = [T(20, 28, 'From Unix to Linux 1.0: four dates on one line', 15, 'start', bold=True)]
    o.append(L(x0, y, x1, y, L2, 2, arrow='m'))
    for yr in range(1966, 1997, 5):
        o += [L(fx(yr), y, fx(yr), y + 6, L2, 1.5), T(fx(yr), y + 24, str(yr), 13, fill=MUT)]
    ev = [(1969, 'Unix begins', 'Bell Labs', AC), (1973, 'Rewritten in C', 'portable', AC),
          (1991, 'Linux kernel', 'Torvalds', LV), (1994, 'Linux 1.0', 'first stable', LV)]
    for i, (yr, a, b, c) in enumerate(ev):
        X = fx(yr)
        up = i % 2 == 0
        ty = 74 if up else 92
        o.append(L(X, ty + 26, X, y - 7, c, 1.5, '4 3'))
        o.append(C(X, y, 7, c))
        o.append(T(X, ty, f'{yr}', 15, 'middle', c, True))
        o.append(T(X, ty + 18, a, 13, 'middle'))
    # gaps under the axis
    gaps = [(1969, 1973, '4 years'), (1973, 1991, '18 years'), (1991, 1994, '3 years')]
    for a, b, s in gaps:
        o.append(brace(fx(a), fx(b), 222, AC, up=True))
        o.append(T((fx(a) + fx(b)) / 2, 244, s, 14, bold=True))
    o.append(brace(fx(1969), fx(1994), 276, NX, up=True))
    o.append(T((fx(1969) + fx(1994)) / 2, 300, '1994 − 1969 = 25 years from first to last', 14, fill=NX, bold=True))
    return 320, ''.join(o)
FIG[1] = (f1, 'The four events in time order: Unix in 1969, the C rewrite in 1973, the Linux kernel in 1991 and Linux 1.0 in 1994. The gaps are 4, 18 and 3 years, so first to last is 25 years.',
          'A time line from 1966 to 1996 with four dots at 1969, 1973, 1991 and 1994, brackets below giving gaps of 4, 18 and 3 years, and one long bracket giving 25 years.')


# ---- 1.2 one lab server: 4 users, 90 processes, 2 cores ----
def f2():
    o = [T(20, 28, 'One lab server shared by 4 students', 15, 'start', bold=True)]
    for i in range(4):
        x = 30 + i * 172
        o.append(boxt(x, 48, 150, 56, [f'Student {i + 1}', 'own shell, own user ID'], ACS, AC, 13, True))
        o.append(L(x + 75, 106, x + 75, 138, AC, 2, arrow='n'))
    o.append(R(20, 142, 680, 58, PANEL, AC, 8, 2))
    o.append(T(36, 168, 'Kernel', 15, 'start', bold=True))
    o.append(T(36, 188, 'checks each user ID against file permissions', 13, 'start', MUT))
    o.append(T(690, 168, 'multi-user: 4 users at once', 14, 'end', AC, True))
    o.append(L(360, 202, 360, 236, LV, 2, arrow='l'))
    o.append(T(372, 226, 'scheduler gives turns', 13, 'start', MUT))
    for j in range(2):
        x = 90 + j * 300
        o.append(R(x, 242, 240, 92, LVS, LV, 8))
        o.append(T(x + 120, 264, f'core {j}', 14, bold=True))
        for r in range(3):
            for c in range(15):
                o.append(f'<rect x="{x + 14 + c * 14.4:.1f}" y="{274 + r * 16}" width="10" height="11" rx="2" style="fill:var(--live)"/>')
    o.append(T(360, 360, '90 processes ÷ 2 cores = 45 processes per core (each small square is one process)', 14))
    o.append(T(360, 384, 'multitasking: each core runs one process at a time and switches quickly', 14, fill=LV, bold=True))
    return 400, ''.join(o)
FIG[2] = (f2, 'Four students work at once because the kernel keeps their user IDs apart (multi-user), and 90 processes share 2 cores by turns (multitasking), 45 per core on average.',
          'Four student boxes with arrows into one kernel band, which feeds two core boxes each filled with 45 small squares for processes.')


# ---- 1.3 typing ls crosses the user/kernel line ----
def f3():
    o = [T(20, 28, 'Typing ls: who runs each step?', 15, 'start', bold=True)]
    yu, yk = 112, 250
    o.append(R(20, 52, 680, 106, ACS, AC, 8, 1.5))
    o.append(T(32, 72, 'user mode: bash and ls', 14, 'start', AC, True))
    o.append(R(20, 202, 680, 106, LVS, LV, 8, 1.5))
    o.append(T(32, 296, 'kernel mode: after a system call', 14, 'start', LV, True))
    o.append(L(20, 180, 700, 180, L2, 1.5, '6 4'))
    steps = [('1', 'bash calls', 'read()', 'u'), ('2', 'terminal', 'gives "ls"', 'k'), ('3', 'bash finds', '/bin/ls', 'u'),
             ('4', 'fork +', 'execve', 'k'), ('5', 'ls calls', 'open, read', 'u'), ('6', 'disk gives', 'names', 'k'),
             ('7', 'ls formats,', 'write()', 'u'), ('8', 'text to', 'terminal', 'k')]
    w = 82
    pts = []
    for i, (n, s1, s2, m) in enumerate(steps):
        x = 26 + i * 84
        y = yu if m == 'u' else yk
        c = AC if m == 'u' else LV
        o.append(R(x, y - 32, w, 64, FIGBG, c, 6, 2))
        o.append(T(x + w / 2, y - 12, n, 15, fill=c, bold=True))
        o.append(T(x + w / 2, y + 6, s1, 13))
        o.append(T(x + w / 2, y + 23, s2, 13))
        pts.append((x + w / 2, y))
    for i in range(len(pts) - 1):
        (a, b), (c, d) = pts[i], pts[i + 1]
        down = b < d
        o.append(L(a + 20, b + (34 if down else -34), c - 20, d + (-37 if down else 37), L2, 1.6, arrow='m'))
    return 320, ''.join(o)
FIG[3] = (f3, 'Typing ls zig-zags across the boundary: bash and ls parse, search and format in user mode, and every read, fork, execve and write is done by the kernel. bash and ls are the two user processes.',
          'Two horizontal bands, user mode above and kernel mode below, with eight numbered steps alternating between them and arrows zig-zagging across the dashed system-call line.')


# ---- 1.4 cost of 40 lab PCs ----
def f4():
    o = [T(20, 28, 'Operating system for 40 lab PCs', 15, 'start', bold=True)]
    x0, s = 200, 470 / 320000
    o.append(T(190, 82, 'proprietary', 14, 'end', bold=True))
    o.append(T(190, 100, '40 × ₹8,000', 13, 'end', MUT))
    o.append(R(x0, 64, 320000 * s, 44, NXS, NX, 4))
    o.append(T(x0 + 320000 * s - 10, 92, '₹3,20,000', 15, 'end', NX, True))
    o.append(T(190, 162, 'open source', 14, 'end', bold=True))
    o.append(T(190, 180, '₹0 licence + support', 13, 'end', MUT))
    o.append(R(x0, 144, 60000 * s, 44, ACS, AC, 4))
    o.append(T(x0 + 60000 * s + 10, 172, '₹60,000', 15, 'start', AC, True))
    o.append(L(x0 + 60000 * s, 210, x0 + 320000 * s, 210, LV, 2.5))
    o.append(L(x0 + 60000 * s, 202, x0 + 60000 * s, 218, LV, 2.5))
    o.append(L(x0 + 320000 * s, 202, x0 + 320000 * s, 218, LV, 2.5))
    o.append(L(x0 + 60000 * s, 112, x0 + 60000 * s, 200, L2, 1.2, '4 3'))
    o.append(L(x0 + 320000 * s, 112, x0 + 320000 * s, 200, L2, 1.2, '4 3'))
    o.append(T(x0 + (60000 + 320000) / 2 * s, 238, 'saving: ₹3,20,000 − ₹60,000 = ₹2,60,000', 15, fill=LV, bold=True))
    return 260, ''.join(o)
FIG[4] = (f4, 'The proprietary route costs 40 × ₹8,000 = ₹3,20,000 in licences; the open-source route costs ₹60,000 in support, so the saving is ₹2,60,000.',
          'Two horizontal bars, a long one of ₹3,20,000 for proprietary licences and a short one of ₹60,000 for open source, with a bracket marking the ₹2,60,000 difference.')


# ---- 1.5 install 30 PCs: one by one or clone ----
def f5():
    o = [T(20, 28, '30 lab PCs: install each one, or install once and clone', 15, 'start', bold=True)]
    x0, x1 = 170, 690
    fx = lambda m: x0 + m / 750 * (x1 - x0)
    o.append(T(160, 80, 'install each', 14, 'end', bold=True))
    for i in range(30):
        o.append(R(fx(i * 25), 62, fx(25) - x0 - 1.5, 30, PANEL, L2, 2, 1.2))
    o.append(Tb(fx(375), 82, '30 × 25 min = 750 min (12 h 30 min)', 14))
    o.append(T(160, 150, 'install + clone', 14, 'end', bold=True))
    o.append(R(fx(0), 132, fx(25) - x0, 30, ACS, AC, 2, 2))
    for i in range(29):
        o.append(R(fx(25 + i * 10), 132, fx(10) - x0 - 1, 30, LVS, LV, 2, 1.2))
    o.append(T(fx(315) + 8, 152, '25 + 29 × 10 = 315 min', 14, 'start', LV, True))
    o.append(T(fx(12), 186, 'first install', 13, 'start', AC))
    o.append(L(fx(12), 176, fx(12), 165, AC, 1.5, arrow='n'))
    o.append(L(fx(315), 210, fx(750), 210, NX, 2.5))
    o.append(L(fx(315), 202, fx(315), 218, NX, 2.5)); o.append(L(fx(750), 202, fx(750), 218, NX, 2.5))
    o.append(L(fx(315), 166, fx(315), 200, L2, 1.2, '4 3')); o.append(L(fx(750), 96, fx(750), 200, L2, 1.2, '4 3'))
    o.append(T(fx(532), 236, 'saved: 750 − 315 = 435 min = 7 h 15 min', 14, fill=NX, bold=True))
    o.append(xaxis(x0, x1, 262, [0, 150, 300, 450, 600, 750], fx, 'minutes'))
    return 320, ''.join(o)
FIG[5] = (f5, 'Installing each PC takes 30 × 25 = 750 minutes; one install plus 29 clones of 10 minutes takes 315 minutes, which saves 435 minutes (7 h 15 min).',
          'Two time bars on a minute scale: thirty 25-minute blocks reaching 750 minutes, and one 25-minute block followed by twenty-nine 10-minute blocks reaching 315 minutes, with the 435-minute gap marked.')


# ---- 1.6 seven commands and the notes directory ----
def f6():
    o = [T(20, 28, 'Seven commands, starting in /home/ravi', 15, 'start', bold=True)]
    o.append(T(40, 58, 'command', 13, 'start', MUT)); o.append(T(260, 58, 'shell is in', 13, 'start', MUT))
    o.append(T(470, 58, 'notes holds / prints', 13, 'start', MUT))
    rows = [('mkdir notes', '/home/ravi', '(empty)', None), ('cd notes', '/home/ravi/notes', '(empty)', None),
            ('pwd', '/home/ravi/notes', 'prints /home/ravi/notes', LV), ('vi a.txt, then :wq', '/home/ravi/notes', 'a.txt', None),
            ('cp a.txt b.txt', '/home/ravi/notes', 'a.txt  b.txt', None), ('ls', '/home/ravi/notes', 'prints a.txt  b.txt', LV),
            ('rm a.txt', '/home/ravi/notes', 'b.txt', AC)]
    y = 70
    for i, (c, d, f, hi) in enumerate(rows):
        fill = ACS if hi == AC else (LVS if hi == LV else PANEL)
        st = hi or L2
        o.append(R(20, y, 680, 36, fill, st, 6, 1.6 if hi else 1.2))
        o.append(T(32, y + 23, str(i + 1), 14, 'start', MUT, True))
        o.append(TM(56, y + 23, c, 14, 'start', bold=True))
        o.append(TM(260, y + 23, d, 13, 'start'))
        o.append(TM(470, y + 23, f, 13, 'start', hi if hi == LV else INK))
        y += 42
    o.append(T(360, y + 18, 'Only cd changes where the shell is; only rm takes a file away.', 14, fill=MUT))
    return y + 32, ''.join(o)
FIG[6] = (f6, 'After the seven commands the shell is still in /home/ravi/notes and only b.txt is left. pwd prints /home/ravi/notes and ls prints a.txt and b.txt.',
          'Seven rows, one per command, each showing the directory the shell is in and what the notes directory holds or what is printed; the pwd and ls rows show printed output and the last row shows only b.txt left.')


TEXT = {
    5: [('Name the four distribution families in the figure and the package manager used by each.',
         'Name the four main distribution families and the package manager used by each.')],
}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d


def text_fixes(k):
    return TEXT.get(k, [])


def chapter_fix(k, ch):
    return unix_text.clean(ch)


def drop_sources():
    # university-hosted pages: the books name no universities (none in this unit's list, kept for the rule)
    return ['.edu/', '.ac.in/', '.ac.uk/']
