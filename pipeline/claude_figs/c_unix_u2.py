"""Claude's hand-drawn figures for c-unix-u2 (Linux and Shell Programming, unit 2: files, directories and permissions),
one per chapter, from each chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *
import unix_text

FIG = {}
AFTER = {}


def node(x, y, w, name, note=None, fill=PANEL, st=AC, h=None):
    h = h or (50 if note else 34)
    o = R(x - w / 2, y, w, h, fill, st, 6, 2)
    o += TM(x, y + (20 if note else 22), name, 14, bold=True)
    if note: o += T(x, y + 39, note, 13, fill=MUT)
    return o


# ---- 2.1 the tree under /home/ravi and the path ../latest ----
def f1():
    o = [T(20, 28, 'Standing in /home/ravi/lab, follow ../latest', 15, 'start', bold=True)]
    o.append(node(360, 48, 70, '/'))
    o.append(L(360, 82, 360, 102, L2, 2))
    o.append(node(360, 102, 90, 'home'))
    o.append(L(360, 136, 360, 156, L2, 2))
    o.append(node(360, 156, 90, 'ravi', fill=ACS))
    xs = [100, 270, 450, 620]
    items = [('notes.txt', 'regular, 2148 B', LVS, LV), ('lab', 'directory', PANEL, AC),
             ('latest', 'symlink, 9 B', PANEL, NX), ('tty1', 'char device 4,1', PANEL, L2)]
    o.append(L(xs[0], 214, xs[-1], 214, L2, 2)); o.append(L(360, 190, 360, 214, L2, 2))
    for x, (n, d, f, s) in zip(xs, items):
        o.append(L(x, 214, x, 236, L2, 2))
        o.append(node(x, 236, 140, n, d, f, s))
    # the walk: lab -> .. (ravi) -> latest -> notes.txt
    o.append(arc(270, 236, 330, 180, 0.25, AC, 2.5, 'n'))
    o.append(Tb(250, 196, '1  ..  goes up to ravi', 13, 'end', AC, True))
    o.append(arc(390, 180, 440, 234, 0.25, AC, 2.5, 'n'))
    o.append(Tb(470, 196, '2  then latest', 13, 'start', AC, True))
    o.append(arc(440, 288, 110, 290, 0.14, NX, 2.5, 'x', '7 5'))
    o.append(Tb(270, 352, '3  latest stores the text notes.txt, read in ravi', 13, 'middle', NX, True))
    o.append(R(20, 372, 680, 44, LVS, LV, 6))
    o.append(TM(360, 400, 'result: /home/ravi/notes.txt, a regular file', 14, bold=True))
    return 430, ''.join(o)
FIG[1] = (f1, 'From /home/ravi/lab, .. climbs to /home/ravi, latest is found there, and its stored text notes.txt is read in that same directory, so the path ends at /home/ravi/notes.txt, the 2148-byte regular file.',
          'A tree from / through home and ravi to four entries: notes.txt, lab, latest and tty1. Arrows go from lab up to ravi, down to latest, and a dashed arrow from latest across to notes.txt.')


# ---- 2.2 ls -lah and less on big.log ----
def f2():
    o = [T(20, 28, 'ls -lah in /home/ravi/lab, then less big.log', 15, 'start', bold=True)]
    o.append(R(20, 42, 360, 236, FIGBG, L2, 8, 1.5))
    lines = [('total 5.0M', MUT, None), ('drwxr-xr-x  .', INK, 'h'), ('drwxr-xr-x  ..', INK, 'h'), ('-rw-r--r--  .profile', INK, 'h'),
             ('-rw-r--r--  5.0M big.log', LV, None), ('-rw-r--r--  2.1K notes.txt', INK, None), ('drwxr-xr-x  reports', INK, None)]
    for i, (s, c, h) in enumerate(lines):
        y = 70 + i * 28
        if h: o.append(R(28, y - 18, 344, 24, ACS, ACS, 4, 1))
        o.append(TM(36, y, s, 13, 'start', c, c == LV))
        o.append(T(368, y, str(i + 1), 13, 'end', MUT))
    o.append(T(200, 300, '7 lines: 6 entries + total', 14, bold=True))
    o.append(T(200, 320, 'shaded rows appear only with -a', 13, fill=AC))
    # size sum
    o.append(T(560, 64, 'why 5.0M?', 14, bold=True))
    o.append(T(560, 86, '5,242,880 ÷ 1024 = 5120 K', 13))
    o.append(T(560, 106, '5120 ÷ 1024 = 5 M', 13))
    # less keys on a file strip
    o.append(T(560, 150, 'less big.log', 14, bold=True))
    o.append(R(470, 162, 180, 150, PANEL, L2, 4, 1.5))
    for i in range(1, 7):
        o.append(L(480, 162 + i * 21, 640, 162 + i * 21, LN, 1))
    o.append(R(470, 162, 180, 22, ACS, AC, 4, 1.5)); o.append(T(560, 178, 'first screen', 13))
    o.append(R(470, 290, 180, 22, LVS, LV, 4, 1.5)); o.append(T(560, 306, 'last line', 13))
    o.append(R(470, 226, 180, 22, NXS, NX, 4, 1.5)); o.append(T(560, 242, 'ERROR', 13, fill=NX, bold=True))
    o.append(arc(660, 176, 660, 296, -0.4, LV, 2, 'l')); o.append(T(694, 240, 'G', 15, 'middle', LV, True))
    o.append(arc(462, 298, 462, 240, -0.5, NX, 2, 'x')); o.append(TM(428, 274, '?ERROR', 13, 'end', NX, True))
    o.append(T(560, 334, 'n: next match, q: quit', 13, fill=MUT))
    return 350, ''.join(o)
FIG[2] = (f2, 'ls -lah prints 6 entries plus a total line, 7 lines in all, and big.log shows as 5.0M because 5,242,880 ÷ 1024 ÷ 1024 = 5. In less, G jumps to the last line and ?ERROR searches back up.',
          'A terminal listing of seven lines with the three hidden entries shaded, a note working out 5.0M, and a file strip with an arrow G down to the last line and an arrow ?ERROR back up to a match.')


# ---- 2.3 names, inodes and link counts ----
def f3():
    o = [T(20, 28, 'Names point to inodes; the data goes when the count reaches 0', 15, 'start', bold=True)]
    cols = [('after step 1: ln', [('notes.txt', 'i'), ('hard.txt', 'i')], 2, False),
            ('after step 2: ln -s', [('notes.txt', 'i'), ('hard.txt', 'i'), ('soft.txt', 's')], 2, False),
            ('after step 3: rm notes.txt', [('hard.txt', 'i'), ('soft.txt', 's')], 1, True)]
    for c, (title, names, cnt, dang) in enumerate(cols):
        x = 20 + c * 232
        o.append(R(x, 44, 220, 330, FIGBG, L2, 8, 1.2, '5 4'))
        o.append(T(x + 110, 66, title, 13, bold=True))
        yi = 230
        o.append(R(x + 112, yi, 98, 58, LVS, LV, 6))
        o.append(T(x + 161, yi + 22, 'inode 1042', 13, bold=True))
        o.append(T(x + 161, yi + 44, f'links = {cnt}', 14, fill=LV, bold=True))
        o.append(T(x + 161, yi + 82, '300 bytes of data', 13, fill=MUT))
        o.append(L(x + 161, yi + 58, x + 161, yi + 68, LV, 2))
        for j, (n, kind) in enumerate(names):
            y = 88 + j * 46
            st = AC if kind == 'i' else NX
            o.append(R(x + 10, y, 96, 30, PANEL, st, 5))
            o.append(TM(x + 58, y + 20, n, 13, bold=True))
            if kind == 'i':
                o.append(L(x + 106, y + 15, x + 158, yi - 4, AC, 2, arrow='n'))
            else:
                o.append(R(x + 10, y + 44, 92, 36, NXS, NX, 5, 1.5))
                o.append(T(x + 56, y + 59, 'inode 2011', 13))
                o.append(TM(x + 56, y + 74, '"notes.txt"', 13, fill=NX))
                o.append(L(x + 58, y + 30, x + 58, y + 42, NX, 1.6))
        if dang:
            o.append(T(x + 56, 230, 'notes.txt gone:', 13, fill=NX, bold=True))
            o.append(T(x + 56, 248, 'dangling', 13, fill=NX, bold=True))
    o.append(T(360, 396, 'cat hard.txt still prints the 300 bytes; cat soft.txt fails: No such file or directory', 14))
    return 410, ''.join(o)
FIG[3] = (f3, 'Each hard link is another name for inode 1042, so the link count goes 2, 2, 1 and the 300 bytes survive rm notes.txt. soft.txt has its own inode 2011 holding only the text notes.txt, so it dangles once that name is gone.',
          'Three panels for the three steps. Names notes.txt and hard.txt point to inode 1042 with link counts 2, 2 and 1; soft.txt points to its own inode 2011 that stores the text notes.txt, marked dangling in the last panel.')


# ---- 2.4 chmod 644 -> 750 ----
def f4():
    o = [T(20, 28, 'notes.txt: from rw-r--r-- (644) to rwxr-x--- (750)', 15, 'start', bold=True)]
    before = list('rw-r--r--'); after = list('rwxr-x---')
    vals = [4, 2, 1] * 3
    x0, cw = 150, 52
    groups = [('owner', AC), ('group', LV), ('other', NX)]
    for g, (name, c) in enumerate(groups):
        o.append(R(x0 + g * 3 * cw + 2, 48, 3 * cw - 4, 26, FIGBG, c, 4, 1.5))
        o.append(T(x0 + g * 3 * cw + 1.5 * cw, 66, name, 13, fill=c, bold=True))
    o.append(T(140, 108, 'before', 14, 'end', bold=True))
    o.append(T(140, 168, 'after', 14, 'end', bold=True))
    o.append(T(140, 138, 'bit value', 13, 'end', MUT))
    for i in range(9):
        x = x0 + i * cw
        ch = before[i] != after[i]
        o.append(R(x + 3, 86, cw - 6, 34, PANEL, L2, 4, 1.2))
        o.append(TM(x + cw / 2, 109, before[i], 16, bold=True))
        o.append(T(x + cw / 2, 140, str(vals[i]), 13, fill=MUT))
        o.append(R(x + 3, 148, cw - 6, 34, LVS if ch else PANEL, LV if ch else L2, 4, 2 if ch else 1.2))
        o.append(TM(x + cw / 2, 171, after[i], 16, bold=True))
        if ch:
            o.append(T(x + cw / 2, 202, '+x' if after[i] == 'x' else '−r', 14, fill=LV, bold=True))
    o.append(T(140, 238, 'octal', 13, 'end', MUT))
    for g, (b, a, c) in enumerate([('4+2 = 6', '4+2+1 = 7', AC), ('4 = 4', '4+1 = 5', LV), ('4 = 4', '0', NX)]):
        cx = x0 + g * 3 * cw + 1.5 * cw
        o.append(T(cx, 238, f'{b}  →  {a}', 13, fill=c, bold=True))
    o.append(TM(360, 280, 'chmod 750 notes.txt    =    chmod u+x,g+x,o-r notes.txt', 14, bold=True))
    o.append(T(360, 310, 'New files start from 666, so umask 022 gives 644; to get 640 the umask must be 026.', 13, fill=MUT))
    return 326, ''.join(o)
FIG[4] = (f4, 'Each triad adds 4 for r, 2 for w and 1 for x: owner 6 becomes 7, group 4 becomes 5 and other 4 becomes 0, so chmod 750 and chmod u+x,g+x,o-r do the same job.',
          'Nine permission cells before and after, grouped as owner, group and other, with bit values 4, 2, 1 under each; the three changed cells are marked +x, +x and −r, and the octal digits go 6 to 7, 4 to 5 and 4 to 0.')


# ---- 2.5 who may read report.txt (mode 640) ----
def f5():
    o = [T(20, 28, 'report.txt: owner ravi (1001), group students, mode 640', 15, 'start', bold=True)]
    qs = [('effective user ID 0?', 'root: allowed', None), ('user ID = 1001 (ravi)?', 'owner bits rw-', None),
          ('in group students?', 'group bits r--', ('priya (1002) stops here:', 'read yes, write no', LV)),
          (None, 'other bits ---', ('arjun (1003) ends here:', 'read no, write no', NX))]
    y = 52
    for i, (q, res, who) in enumerate(qs):
        if q:
            o.append(R(30, y, 230, 42, PANEL, AC, 21, 2))
            o.append(T(145, y + 26, q, 14, bold=True))
            o.append(L(260, y + 21, 330, y + 21, AC, 2, arrow='n')); o.append(T(295, y + 15, 'yes', 13, fill=AC))
            o.append(R(334, y + 2, 150, 38, ACS, AC, 6)); o.append(T(409, y + 26, res, 14))
            o.append(L(145, y + 42, 145, y + 66, L2, 2, arrow='m')); o.append(T(155, y + 60, 'no', 13, 'start', MUT))
        else:
            o.append(R(30, y + 2, 230, 38, PANEL, L2, 6)); o.append(T(145, y + 26, 'everyone else', 14))
            o.append(L(260, y + 21, 330, y + 21, L2, 2, arrow='m'))
            o.append(R(334, y + 2, 150, 38, NXS, NX, 6)); o.append(T(409, y + 26, res, 14))
        if who:
            o.append(L(486, y + 21, 504, y + 21, who[2], 2))
            o.append(T(510, y + 16, who[0], 13, 'start', who[2], True))
            o.append(T(510, y + 34, who[1], 13, 'start', who[2]))
        y += 70
    o.append(T(360, 356, 'The check stops at the first yes. To let arjun read: setfacl -m u:arjun:r report.txt', 13, fill=MUT))
    return 372, ''.join(o)
FIG[5] = (f5, 'The kernel asks the questions top to bottom and stops at the first yes: priya is in students, so the group bits r-- let her read; arjun matches nothing, so the other bits --- deny him everything.',
          'A chain of three questions, effective user ID 0, user ID 1001 and member of students, each with a yes arrow to root allowed, owner rw- and group r--, ending in other ---. Priya enters at the group question and gets read only; Arjun falls to other and gets nothing.')


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d


def text_fixes(k):
    return []


def chapter_fix(k, ch):
    return unix_text.clean(ch)


def drop_sources():
    return ['.edu/', '.ac.in/', '.ac.uk/']
