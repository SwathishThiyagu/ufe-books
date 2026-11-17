"""Claude's hand-drawn figures for c-unix-u3 (Linux and Shell Programming, unit 3: shell scripting and text processing),
one per chapter, from each chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *
import unix_text

FIG = {}
AFTER = {}


def term(x, y, w, lines, title=None, h=None, size=13, colors=None):
    lh = size + 8
    h = h or (len(lines) * lh + 18 + (22 if title else 0))
    o = R(x, y, w, h, FIGBG, L2, 6, 1.5)
    yy = y + 22
    if title:
        o += T(x + 10, yy, title, 13, 'start', MUT, True); yy += 22
    for i, s in enumerate(lines):
        o += TM(x + 12, yy + i * lh, s, size, 'start', (colors[i] if colors else INK))
    return o


# ---- 3.1 three ways to run greet.sh ----
def f1():
    o = [T(20, 28, 'greet.sh: #!/bin/sh then echo "Hi $USER", with USER=asha', 15, 'start', bold=True)]
    rows = [('./greet.sh', 'mode 644: no x bit', 'kernel refuses', 'Permission denied', NX, NXS),
            ('chmod 755, then ./greet.sh', 'mode 755: x bit set', 'kernel reads #!/bin/sh, starts sh', 'Hi asha', LV, LVS),
            ('bash greet.sh  (or sh greet.sh)', 'you name the shell', '#! line is only a comment', 'Hi asha', AC, ACS)]
    y = 50
    for cmd, a, b, out, c, cs in rows:
        o.append(R(20, y, 680, 82, cs, c, 8, 1.5))
        o.append(TM(34, y + 26, cmd, 14, 'start', bold=True))
        o.append(T(34, y + 50, a, 13, 'start', MUT))
        o.append(T(34, y + 70, b, 13, 'start', MUT))
        o.append(L(440, y + 41, 500, y + 41, c, 2, arrow={'var(--next)': 'x', 'var(--live)': 'l'}.get(c, 'n')))
        o.append(R(506, y + 22, 180, 38, FIGBG, c, 6, 2))
        o.append(TM(596, y + 47, out, 14, fill=c, bold=True))
        y += 96
    o.append(T(360, y + 10, 'The shebang matters only when the file itself is executed.', 14, fill=MUT))
    return y + 24, ''.join(o)
FIG[1] = (f1, 'With mode 644 the kernel refuses ./greet.sh; after chmod 755 it reads #!/bin/sh and prints Hi asha. Naming bash or sh yourself also prints Hi asha, because the named shell just reads the file.',
          'Three rows: ./greet.sh at mode 644 gives Permission denied; after chmod 755 the kernel starts sh and prints Hi asha; bash greet.sh or sh greet.sh prints Hi asha with the shebang treated as a comment.')


# ---- 3.2 quoting decides what expands ----
def f2():
    o = [T(20, 28, 'NAME=Asha   COUNT=7: what does each echo print?', 15, 'start', bold=True)]
    rows = [('echo "$NAME has $COUNT"', 'Asha has 7', 'double quotes: variables expand', AC),
            ("echo '$NAME has $COUNT'", '$NAME has $COUNT', 'single quotes: nothing expands', NX),
            ('echo $((COUNT+3))', '10', 'arithmetic: 7 + 3', LV),
            ('echo ${#NAME}', '4', 'length of Asha', LV)]
    o.append(T(40, 60, 'line in the script', 13, 'start', MUT)); o.append(T(470, 60, 'printed', 13, 'start', MUT))
    y = 72
    for cmd, out, why, c in rows:
        o.append(R(20, y, 680, 58, PANEL, L2, 6, 1.2))
        o.append(TM(36, y + 25, cmd, 14, 'start', bold=True))
        o.append(T(36, y + 46, why, 13, 'start', c))
        o.append(L(372, y + 29, 452, y + 29, c, 2, arrow={'var(--next)': 'x', 'var(--live)': 'l'}.get(c, 'n')))
        o.append(R(460, y + 10, 226, 38, FIGBG, c, 6, 2))
        o.append(TM(573, y + 35, out, 15, fill=c, bold=True))
        y += 68
    return y + 6, ''.join(o)
FIG[2] = (f2, 'Double quotes expand $NAME and $COUNT, single quotes print them as typed, $((COUNT+3)) computes 10 and ${#NAME} counts the 4 letters of Asha.',
          'Four rows, each an echo line with an arrow to what it prints: Asha has 7, then the literal $NAME has $COUNT, then 10, then 4.')


# ---- 3.3 dry run of the loop ----
def f3():
    o = [T(20, 28, 'for n in 4 7 10 13: print n if (( n % 2 == 1 && n > 5 ))', 15, 'start', bold=True)]
    heads = ['n', 'n % 2', 'odd?', 'n > 5?', 'both?', 'printed']
    xs = [40, 150, 260, 370, 480, 590]
    w = 100
    for x, h in zip(xs, heads):
        o.append(R(x, 50, w, 32, ACS, AC, 4, 1.5)); o.append(T(x + w / 2, 71, h, 14, bold=True))
    data = [(4, 0, 'no', 'no', 'no', '–'), (7, 1, 'yes', 'yes', 'yes', '7'), (10, 0, 'no', 'yes', 'no', '–'), (13, 1, 'yes', 'yes', 'yes', '13')]
    y = 90
    for row in data:
        hit = row[4] == 'yes'
        for j, (x, v) in enumerate(zip(xs, row)):
            fill = LVS if (hit and j >= 4) else PANEL
            st = LV if (hit and j >= 4) else L2
            o.append(R(x, y, w, 36, fill, st, 4, 2 if hit and j >= 4 else 1.2))
            col = NX if v == 'no' else (LV if hit and j == 5 else INK)
            o.append(T(x + w / 2, y + 24, str(v), 15, fill=col, bold=(j in (0, 5))))
        y += 42
    o.append(T(360, y + 16, 'Output: 7, then 13 on the next line', 14, fill=LV, bold=True))
    return y + 30, ''.join(o)
FIG[3] = (f3, 'The loop tests each n in turn: 4 and 10 are even, so nothing prints; 7 and 13 are odd and greater than 5, so the script prints 7 and then 13.',
          'A table with rows for n = 4, 7, 10 and 13 and columns n mod 2, odd, greater than 5, both and printed; only the rows for 7 and 13 print.')


# ---- 3.4 stdout carries data, return carries status ----
def f4():
    o = [T(20, 28, 'f 4 6; s=$?; echo $s   with   f() { echo $(( $1 + $2 )); return 3; }', 14, 'start', bold=True)]
    o.append(R(200, 56, 320, 120, ACS, AC, 8))
    o.append(T(360, 80, 'inside f:  $1 = 4,  $2 = 6', 14, bold=True))
    o.append(TM(360, 110, 'echo $((4 + 6))', 14))
    o.append(TM(360, 150, 'return 3', 14))
    # stdout path
    o.append(L(200, 106, 120, 106, LV, 2.5, arrow='l'))
    o.append(T(160, 98, 'stdout', 13, fill=LV, bold=True))
    o.append(term(20, 210, 200, ['10', '3'], 'terminal'))
    o.append(L(70, 112, 70, 206, LV, 2.5, arrow='l'))
    o.append(R(40, 92, 70, 28, LVS, LV, 4)); o.append(TM(75, 111, '10', 14, fill=LV, bold=True))
    # status path
    o.append(L(520, 146, 590, 146, NX, 2.5, arrow='x'))
    o.append(T(555, 138, '$?', 14, fill=NX, bold=True))
    o.append(R(594, 128, 106, 36, NXS, NX, 6)); o.append(TM(647, 151, '$? = 3', 14, fill=NX, bold=True))
    o.append(L(647, 164, 647, 206, NX, 2, arrow='x'))
    o.append(R(574, 210, 126, 36, PANEL, NX, 6)); o.append(TM(637, 233, 's=$? → 3', 14, bold=True))
    o.append(L(574, 228, 224, 268, NX, 2, '6 4', arrow='x'))
    o.append(T(400, 264, 'echo $s', 13, fill=NX))
    o.append(T(360, 310, 'The sum travels as text on stdout; return can only give a status from 0 to 255.', 14, fill=MUT))
    return 326, ''.join(o)
FIG[4] = (f4, 'Inside f, $1 = 4 and $2 = 6, so echo writes 10 to stdout; return 3 only sets $? to 3, which s stores and echo prints, so the terminal shows 10 and then 3.',
          'A function box with two exits: a stdout arrow carrying 10 straight to the terminal, and a status arrow carrying 3 into $?, then into s, which echo prints on the terminal after 10.')


# ---- 3.5 redirection of the three descriptors ----
def f5():
    o = [T(20, 28, './count.sh < data.txt > out.txt 2> err.txt', 15, 'start', bold=True)]
    o.append(term(20, 60, 170, ['1 2', '3 4', '5 6'], 'data.txt'))
    o.append(R(270, 80, 190, 120, ACS, AC, 8))
    o.append(T(365, 104, 'count.sh', 15, bold=True))
    o.append(TM(365, 132, 'read a b', 13)); o.append(TM(365, 154, 'echo $((a + b))', 13))
    o.append(T(365, 184, 'loop ends at end of file', 13, fill=MUT))
    o.append(L(192, 120, 266, 120, AC, 2.5, arrow='n')); o.append(T(229, 112, 'fd 0', 13, fill=AC, bold=True))
    o.append(term(540, 56, 160, ['3', '7', '11'], 'out.txt'))
    o.append(T(620, 178, '7 bytes (with newlines)', 13, fill=LV))
    o.append(L(460, 110, 536, 100, LV, 2.5, arrow='l')); o.append(T(498, 96, 'fd 1', 13, fill=LV, bold=True))
    o.append(R(540, 206, 160, 52, FIGBG, L2, 6, 1.5)); o.append(T(550, 228, 'err.txt', 13, 'start', MUT, True))
    o.append(T(550, 248, 'empty, 0 bytes', 13, 'start', MUT))
    o.append(L(460, 180, 536, 226, L2, 2, '6 4', arrow='m')); o.append(T(486, 222, 'fd 2', 13, fill=MUT, bold=True))
    o.append(T(30, 230, 'passes: 1+2 = 3,  3+4 = 7,  5+6 = 11', 14, 'start'))
    o.append(T(30, 254, 'exit status 0', 14, 'start', LV, True))
    o.append(T(360, 290, 'The shell opens all three files before count.sh starts; the script never names a file.', 13, fill=MUT))
    return 306, ''.join(o)
FIG[5] = (f5, 'The shell points fd 0 at data.txt, fd 1 at out.txt and fd 2 at err.txt before count.sh runs. The three passes write 3, 7 and 11 to out.txt (7 bytes), err.txt stays empty and the exit status is 0.',
          'data.txt with lines 1 2, 3 4 and 5 6 feeds fd 0 into count.sh; fd 1 goes to out.txt holding 3, 7 and 11; a dashed fd 2 goes to an empty err.txt.')


# ---- 3.6 the pipeline, stage by stage ----
def stages(title, cols, foot, h=300):
    o = [T(20, 28, title, 14, 'start', bold=True)]
    n = len(cols)
    w = (680 - (n - 1) * 26) / n
    for i, (head, lines, keep) in enumerate(cols):
        x = 20 + i * (w + 26)
        o.append(R(x, 50, w, 30, ACS if i else PANEL, AC if i else L2, 4, 1.5))
        o.append(TM(x + w / 2, 70, head, 13, bold=True))
        for j, s in enumerate(lines):
            y = 90 + j * 34
            k = keep[j] if keep else True
            o.append(R(x, y, w, 28, LVS if (i == n - 1) else PANEL, LV if i == n - 1 else L2, 4, 1.2))
            o.append(TM(x + w / 2, y + 19, s, 13, fill=INK if k else MUT))
            if not k: o.append(L(x + 8, y + 14, x + w - 8, y + 14, NX, 1.8))
        if i < n - 1:
            o.append(L(x + w + 3, 65, x + w + 22, 65, AC, 2, arrow='n'))
    o.append(T(360, h - 16, foot, 14, fill=LV, bold=True))
    return h, ''.join(o)


def f6():
    return stages('cut -d, -f1,3 sales.csv | grep \'^Delhi\' | sort -t, -k2 -n | head -2', [
        ('cut -f1,3', ['Delhi,120', 'Mumbai,80', 'Delhi,300', 'Chennai,50', 'Delhi,150'], [1, 0, 1, 0, 1]),
        ("grep '^Delhi'", ['Delhi,120', 'Delhi,300', 'Delhi,150'], None),
        ('sort -t, -k2 -n', ['Delhi,120', 'Delhi,150', 'Delhi,300'], [1, 1, 0]),
        ('head -2', ['Delhi,120', 'Delhi,150'], None)], 'Two rows reach the screen: 120 and 150 rupees', 290)
FIG[6] = (f6, 'Each column is the stream after one command: grep drops the Mumbai and Chennai lines, sort puts 120, 150, 300 in order, and head -2 keeps Delhi,120 and Delhi,150.',
          'Four columns of lines, one per command in the pipeline; struck-out lines are the ones the next command drops, and the last column holds Delhi,120 and Delhi,150.')


# ---- 3.7 grep, sed, awk ----
def f7():
    h, body = stages("grep -v '^R' | sed 's/ /,/' | awk -F, '$2 >= 60 {sum += $2; n++} END {print n, sum}'", [
        ('marks.txt', ['Asha 78', 'Ravi 45', 'Meena 91', 'Arjun 60'], [1, 0, 1, 1]),
        ("grep -v '^R'", ['Asha 78', 'Meena 91', 'Arjun 60'], None),
        ("sed 's/ /,/'", ['Asha,78', 'Meena,91', 'Arjun,60'], None),
        ('awk: n, sum', ['n=1  sum=78', 'n=2  sum=169', 'n=3  sum=229'], None)], 'END prints: 3 229', 280)
    return h, body
FIG[7] = (f7, 'grep -v drops the Ravi line, sed turns the first space into a comma, and awk adds each mark of 60 or more: 78, then 169, then 229. END prints the count and total, 3 229.',
          'Four columns: marks.txt with the Ravi line struck out, the three lines after grep, the same lines with commas after sed, and awk running totals n = 1, 2, 3 and sum = 78, 169, 229.')


# ---- 3.8 set -e stops at the first failure ----
def f8():
    o = [T(20, 28, './backup.sh a.txt missing.txt c.txt', 15, 'start', bold=True)]
    cmds = [('cp a.txt', 'status 0'), ('cp missing.txt', 'status 1'), ('cp c.txt', 'status 0'), ('echo done', 'status 0')]
    for lane, (name, y, stop) in enumerate([('with set -e', 60, True), ('without set -e', 190, False)]):
        o.append(T(20, y + 18, name, 14, 'start', bold=True))
        x = 20
        for i, (c, st) in enumerate(cmds):
            bx = 20 + i * 140
            ran = not (stop and i >= 2)
            fail = i == 1
            fill = NXS if fail else (PANEL if ran else FIGBG)
            stc = NX if fail else (AC if ran else L2)
            o.append(R(bx, y + 32, 124, 52, fill, stc, 6, 2 if ran else 1.2, None if ran else '5 4'))
            o.append(TM(bx + 62, y + 54, c, 13, fill=INK if ran else MUT, bold=ran))
            o.append(T(bx + 62, y + 74, st if ran else 'not run', 13, fill=(NX if fail else (MUT))))
            if i < 3:
                o.append(L(bx + 126, y + 58, bx + 138, y + 58, AC if (ran and not (stop and i == 1)) else L2, 2))
        ex = '1' if stop else '0'
        c = NX if stop else LV
        o.append(R(580, y + 32, 120, 52, NXS if stop else LVS, c, 6, 2))
        o.append(T(640, y + 54, f'exit {ex}', 15, fill=c, bold=True))
        o.append(T(640, y + 74, '1 file copied' if stop else '2 copied, done', 13, fill=c))
        if stop:
            o.append(arc(184, y + 30, 600, y + 30, 0.08, NX, 2, 'x'))
            o.append(Tb(390, y + 18, 'set -e: stop at once', 13, fill=NX, bold=True))
    o.append(T(360, 312, 'Without set -e the last command, echo, gives 0 and hides the failed copy.', 14, fill=MUT))
    return 328, ''.join(o)
FIG[8] = (f8, 'The second cp fails with status 1. With set -e the script exits 1 straight away after one copy; without it the script copies c.txt, prints done and exits 0, hiding the failure.',
          'Two lanes of four commands. In the set -e lane, cp missing.txt fails with status 1 and an arrow jumps to exit 1, leaving the last two commands not run. In the other lane all four run and the script exits 0.')


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d


def text_fixes(k):
    return []


def chapter_fix(k, ch):
    ch = unix_text.clean(ch)
    if k == 5:
        # 3.5 analyze question: /etc/passwd is world-readable, so grep on it never prints "Permission denied";
        # /etc/shadow, run by an ordinary user, does
        for q in ch.get('quiz', []):
            if 'grep root /etc/passwd' in q['q']:
                q['q'] = 'Run by an ordinary user, why does ' + q['q'][len('Why does '):].replace('grep root /etc/passwd', 'grep root /etc/shadow')
    return ch


def drop_sources():
    return ['.edu/', '.ac.in/', '.ac.uk/']
