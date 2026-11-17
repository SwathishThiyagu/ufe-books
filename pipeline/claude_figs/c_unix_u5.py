"""Claude's hand-drawn figures for c-unix-u5 (Linux and Shell Programming, unit 5: Linux kernel internals), one per
chapter, from each chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *
import unix_text

FIG = {}
AFTER = {}


# ---- 5.1 PID hash and the zombie ----
def f1():
    o = [T(20, 28, 'Find PID 1201 in a hash table of 512 buckets', 15, 'start', bold=True)]
    o.append(T(20, 56, '1201 mod 512:  512 × 2 = 1024,  1201 − 1024 = 177', 14, 'start', AC, True))
    rows = [('0', False), ('1', False), ('⋮', None), ('176', False), ('177', True), ('178', False), ('⋮', None), ('511', False)]
    y = 74
    for lab, hit in rows:
        if hit is None:
            o.append(T(70, y + 18, '⋮', 15, fill=MUT)); y += 26; continue
        o.append(R(40, y, 60, 26, ACS if hit else PANEL, AC if hit else L2, 3, 2 if hit else 1.2))
        o.append(T(70, y + 18, lab, 13, bold=hit))
        if hit: yh = y + 13
        y += 30
    o.append(L(102, yh, 168, yh, AC, 2.5, arrow='n'))
    # task before / after
    def task(x, title, st, rows_, c, cs):
        out = [R(x, 88, 240, 200, cs, c, 8, 2), T(x + 120, 112, title, 14, fill=c, bold=True)]
        out.append(TM(x + 16, 140, st, 13, 'start', c, True))
        for i, (a, b, keep) in enumerate(rows_):
            yy = 166 + i * 24
            out.append(TM(x + 16, yy, a, 13, 'start', INK if keep else MUT))
            out.append(T(x + 226, yy, b, 13, 'end', LV if keep else MUT))
            if not keep: out.append(L(x + 14, yy - 4, x + 20 + len(a) * 8, yy - 4, NX, 1.8))
        return ''.join(out)
    o.append(task(172, 'task_struct, running', 'TASK_RUNNING', [('pid 1201', 'set', True), ('mm', 'address space', True), ('files', 'open files', True), ('exit code', '–', True), ('signal state', 'set', True)], AC, ACS))
    o.append(L(414, 196, 454, 196, NX, 2.5, arrow='x')); o.append(T(436, 184, 'exit()', 13, fill=NX, bold=True))
    o.append(task(460, 'after exit, no wait() yet', 'TASK_ZOMBIE', [('pid 1201', 'kept', True), ('mm', 'freed', False), ('files', 'closed', False), ('exit code', 'kept', True), ('signal state', 'kept', True)], NX, NXS))
    o.append(T(580, 310, 'wait() by the parent', 13, fill=NX, bold=True))
    o.append(T(580, 328, 'releases the rest', 13, fill=NX))
    return 344, ''.join(o)
FIG[1] = (f1, 'PID 1201 hashes to bucket 177 because 1201 − 2 × 512 = 177. After exit() with no wait(), the task becomes a zombie: its memory and open files are freed, but the task_struct keeps the PID and exit code.',
          'A column of hash buckets 0 to 511 with bucket 177 highlighted and an arrow to a running task_struct; an exit arrow leads to the zombie version, where mm and files are struck out and pid, exit code and signal state are kept.')


# ---- 5.2 jiffies at HZ = 250 ----
def f2():
    o = [T(20, 28, 'HZ = 250: one timer tick every 4 ms', 15, 'start', bold=True)]
    x0, x1 = 60, 660
    fx = lambda ms: x0 + ms / 24 * (x1 - x0)
    y = 120
    o.append(L(x0, y, x1 + 20, y, L2, 2, arrow='m'))
    for ms in range(0, 25, 2):
        o.append(L(fx(ms), y, fx(ms), y + 5, L2, 1.2))
        if ms % 4 == 0: o.append(T(fx(ms), y + 24, f'{ms} ms', 13, fill=MUT))
    for i, ms in enumerate(range(4, 24, 4)):
        o.append(L(fx(ms), y - 34, fx(ms), y, LV, 3))
        o.append(T(fx(ms), y - 42, f'tick {i + 1}', 13, fill=LV, bold=True))
    o.append(brace(fx(0), fx(20), y + 40, AC))
    o.append(T(fx(10), y + 66, '20 ms = 0.020 s × 250 = 5 jiffies', 14, fill=AC, bold=True))
    o.append(T(fx(22), y - 60, '1 s = 250 jiffies', 13, fill=MUT))
    o.append(R(20, 222, 680, 96, PANEL, NX, 8))
    o.append(T(36, 246, 'A 32-bit jiffies counter wraps after 2³² = 4,294,967,296 ticks', 14, 'start', bold=True))
    o.append(T(36, 270, '4,294,967,296 ÷ 250 = 17,179,869.184 s', 14, 'start'))
    o.append(T(36, 296, '17,179,869.184 ÷ 86,400 ≈ 198.84 days', 14, 'start', NX, True))
    return 334, ''.join(o)
FIG[2] = (f2, 'At HZ = 250 the timer ticks every 4 ms, so 20 ms holds 5 jiffies and 1 s holds 250. A 32-bit counter of ticks wraps after 2³² ÷ 250 s, about 198.84 days.',
          'A millisecond ruler from 0 to 24 ms with a tick mark every 4 ms, a bracket over the first 20 ms reading 5 jiffies, and a box working out that a 32-bit counter wraps after about 198.84 days.')


# ---- 5.3 address translation ----
def f3():
    o = [T(20, 28, 'Virtual address 0x00403ABC, 4 KB pages, 32-bit x86', 15, 'start', bold=True)]
    segs = [('0000000001', 'bits 31–22', 'directory 1', 10, AC, ACS), ('0000000011', 'bits 21–12', 'table 3', 10, LV, LVS), ('101010111100', 'bits 11–0', 'offset 0xABC = 2748', 12, NX, NXS)]
    x = 40
    cw = 640 / 32
    xs = []
    for bits, rng, lab, n, c, cs in segs:
        w = n * cw
        o.append(R(x, 50, w, 34, cs, c, 4, 2))
        o.append(TM(x + w / 2, 72, bits, 13, bold=True))
        o.append(T(x + w / 2, 102, rng, 13, fill=MUT))
        o.append(T(x + w / 2, 122, lab, 14, fill=c, bold=True))
        xs.append(x + w / 2)
        x += w
    # page directory
    def table(tx, title, hi, val, c, cs):
        out = [T(tx + 60, 158, title, 13, bold=True)]
        for i in range(5):
            yy = 168 + i * 26
            h = i == hi
            out.append(R(tx, yy, 120, 24, cs if h else PANEL, c if h else L2, 2, 2 if h else 1))
            out.append(T(tx + 8, yy + 17, str(i), 13, 'start', MUT))
            if h: out.append(TM(tx + 66, yy + 17, val, 13, fill=c, bold=True))
        return ''.join(out)
    o.append(table(60, 'page directory', 1, '→ table', AC, ACS))
    o.append(L(xs[0], 128, 186, 200, AC, 2, arrow='n'))
    o.append(table(260, 'page table', 3, '0x00012007', LV, LVS))
    o.append(L(xs[1] + 16, 128, 386, 252, LV, 2, arrow='l'))
    o.append(L(182, 207, 256, 207, AC, 2, '5 4', arrow='n'))
    o.append(L(382, 259, 396, 259, LV, 2, arrow='l'))
    o.append(R(400, 214, 150, 94, LVS, LV, 6))
    o.append(T(475, 236, '>> 12 → frame 18', 13, bold=True))
    o.append(T(475, 256, 'flags 0x007 = 111:', 13, fill=MUT))
    o.append(T(475, 276, 'present, writable,', 13, fill=MUT))
    o.append(T(475, 296, 'user', 13, fill=MUT))
    o.append(L(xs[2], 128, xs[2], 314, NX, 2, '6 4', arrow='x'))
    o.append(T(xs[2] + 8, 168, 'offset passes', 13, 'start', NX)); o.append(T(xs[2] + 8, 186, 'straight through', 13, 'start', NX))
    o.append(R(40, 318, 660, 44, NXS, NX, 6))
    o.append(T(370, 345, 'physical = 18 × 4096 + 2748 = 73728 + 2748 = 76476 = 0x12ABC', 14, bold=True))
    return 376, ''.join(o)
FIG[3] = (f3, 'The 32 bits split 10 | 10 | 12 into directory index 1, table index 3 and offset 2748. Entry 3 holds 0x00012007, so the frame is 18, and the physical address is 18 × 4096 + 2748 = 0x12ABC.',
          'The virtual address drawn as a 32-bit strip cut into 10, 10 and 12 bits. The first part picks entry 1 of the page directory, the second picks entry 3 of the page table holding 0x00012007, giving frame 18; the offset drops straight down to the sum 76476.')


# ---- 5.4 the lost update ----
def f4():
    o = [T(20, 28, 'count = 5, and two CPUs each run count++ once', 15, 'start', bold=True)]
    x0, x1 = 130, 690
    fx = lambda s: x0 + s / 13 * (x1 - x0)
    o.append(T(20, 52, 'no lock', 14, 'start', NX, True))
    lanes = [('CPU 0', [(0, 3, 'read 5'), (3, 7, 'add 1 → 6'), (7, 10, 'write 6')], AC, ACS, 70),
             ('CPU 1', [(2, 5, 'read 5'), (5, 9, 'add 1 → 6'), (9, 12, 'write 6')], LV, LVS, 112)]
    for name, bars, c, cs, y in lanes:
        o.append(T(120, y + 21, name, 14, 'end', bold=True))
        for a, b, s in bars:
            o.append(R(fx(a), y, fx(b) - fx(a) - 2, 30, cs, c, 4, 1.6))
            o.append(T((fx(a) + fx(b)) / 2, y + 20, s, 13))
    o.append(T(120, 175, 'count', 14, 'end', bold=True))
    for a, b, v, hi in [(0, 7, '5', False), (7, 9, '6', False), (9, 13, '6', True)]:
        o.append(R(fx(a), 156, fx(b) - fx(a) - 2, 28, NXS if hi else PANEL, NX if hi else L2, 4, 2 if hi else 1.2))
        o.append(T((fx(a) + fx(b)) / 2, 175, v, 14, fill=NX if hi else INK, bold=hi))
    o.append(T(fx(13), 204, 'ends at 6, not 7: one update lost', 13, 'end', NX, True))
    o.append(L(20, 220, 700, 220, LN, 1))
    o.append(T(20, 246, 'with spin_lock(&l) around count++', 14, 'start', AC, True))
    o.append(T(120, 287, 'CPU 0', 14, 'end', bold=True)); o.append(T(120, 329, 'CPU 1', 14, 'end', bold=True))
    o.append(R(fx(0), 266, fx(5) - fx(0) - 2, 30, ACS, AC, 4, 1.6)); o.append(T((fx(0) + fx(5)) / 2, 286, 'lock · 5 → 6 · unlock', 13))
    o.append(R(fx(0), 308, fx(5) - fx(0) - 2, 30, FIGBG, L2, 4, 1.2, '5 4')); o.append(T((fx(0) + fx(5)) / 2, 328, 'spins, waiting', 13, fill=MUT))
    o.append(R(fx(5), 308, fx(10) - fx(5) - 2, 30, LVS, LV, 4, 1.6)); o.append(T((fx(5) + fx(10)) / 2, 328, 'lock · 6 → 7 · unlock', 13))
    o.append(T(fx(13), 364, 'ends at 7', 14, 'end', LV, True))
    return 380, ''.join(o)
FIG[4] = (f4, 'Without a lock both CPUs read 5 before either writes, so both write 6 and one increment is lost. With the spinlock CPU 1 waits, reads 6 and writes 7.',
          'Top: two CPU lanes each doing read 5, add, write 6 with overlapping times, and the shared count going 5, 6, 6. Bottom: with a spinlock, CPU 0 goes 5 to 6 while CPU 1 spins, then CPU 1 goes 6 to 7.')


# ---- 5.5 the pipe buffer ----
def f5():
    o = [T(20, 28, 'Pipe of 65536 bytes, write end O_NONBLOCK', 15, 'start', bold=True)]
    x0, W = 210, 470
    fx = lambda b: x0 + b / 65536 * W
    steps = [('write(70000)', 'returns 65536', 0, 65536, '4464 B wait in the writer', AC),
             ('read(8192)', 'returns 8192', 8192, 65536, '57344 B left, 8192 free', LV),
             ('write(4464)', 'returns 4464', 8192, 65536 + 4464, 'pipe holds 61808 B', NX)]
    y = 54
    for cmd, ret, a, b, note, c in steps:
        o.append(TM(200, y + 18, cmd, 14, 'end', bold=True))
        o.append(T(200, y + 38, ret, 13, 'end', c, True))
        o.append(R(x0, y, W, 44, FIGBG, L2, 4, 1.5))
        if a > 0 and b > 65536:
            o.append(R(fx(0), y, fx(65536 - 8192 + 4464) - x0, 44, ACS, AC, 4, 1.2))
            o.append(R(fx(57344), y, fx(61808) - fx(57344), 44, NXS, NX, 0, 2))
        else:
            o.append(R(fx(0), y, fx(b - a) - x0, 44, ACS, AC, 4, 1.2))
        o.append(T(x0 + W / 2, y + 64, note, 13, fill=c, bold=True))
        y += 92
    o.append(T(x0, y - 4, '0', 13, fill=MUT)); o.append(T(x0 + W, y - 4, '65536', 13, 'end', MUT))
    o.append(T(360, y + 20, 'A non-blocking write copies what fits and returns that count instead of waiting.', 13, fill=MUT))
    return y + 36, ''.join(o)
FIG[5] = (f5, 'The first write fills the 65536-byte pipe and returns 65536, leaving 4464 bytes with the writer. The read takes 8192, and the second write of 4464 fits, so the pipe ends holding 61808 bytes.',
          'Three bars for the pipe, 65536 bytes wide: full after the first write, 57344 bytes after the read, and 61808 bytes after the second write, with the new 4464 bytes shown at the end.')


# ---- 5.6 where offset 300000 lives ----
def f6():
    o = [T(20, 28, 'ext2, 1 KB blocks: which block holds byte 300000?', 15, 'start', bold=True)]
    segs = [('12 direct', '0 – 12287', 110, PANEL, L2), ('single indirect: 256 blocks', '12288 – 274431', 250, ACS, AC),
            ('double indirect', 'from 274432', 280, LVS, LV)]
    x = 40
    for name, rng, w, f, c in segs:
        o.append(R(x, 56, w, 48, f, c, 4, 2))
        o.append(T(x + w / 2, 76, name, 13, bold=True)); o.append(T(x + w / 2, 96, rng, 13, fill=MUT))
        x += w
    o.append(T(690, 84, '…', 15, fill=MUT))
    xd = 400
    o.append(T(40, 162, '300000 − 274432 = 25568 bytes into the double area', 14, 'start'))
    o.append(T(40, 186, '25568 ÷ 1024 = 24.97, so data block 24 (top entry 0, second entry 24)', 14, 'start'))
    o.append(boxt(400, 210, 130, 44, ['top entry 0'], PANEL, LV, 13))
    o.append(L(465, 254, 465, 274, LV, 2, arrow='l'))
    o.append(boxt(400, 278, 130, 44, ['second entry 24'], PANEL, LV, 13))
    o.append(L(530, 300, 556, 300, LV, 2, arrow='l'))
    o.append(R(560, 272, 140, 56, NXS, NX, 6)); o.append(T(630, 294, 'data block 24', 13, bold=True)); o.append(T(630, 314, '299008 – 300031', 13, fill=NX, bold=True))
    o.append(R(40, 214, 330, 108, PANEL, AC, 8))
    o.append(T(56, 238, 'largest file', 14, 'start', AC, True))
    o.append(T(56, 262, '12 + 256 + 256² + 256³', 13, 'start'))
    o.append(T(56, 284, '= 16,843,020 blocks of 1 KB', 13, 'start'))
    o.append(T(56, 306, '≈ 16.06 GiB', 13, 'start', AC, True))
    return 340, ''.join(o)
FIG[6] = (f6, 'Direct blocks cover bytes 0 to 12287 and single indirect up to 274431, so byte 300000 is 25568 bytes into the double-indirect area: top entry 0, second entry 24, data block 24 covering 299008 to 300031.',
          'A strip of byte ranges: 12 direct blocks, single indirect and double indirect. Below, the arithmetic for offset 300000 and a chain from top entry 0 to second entry 24 to data block 24, plus a box with the largest file size of about 16.06 GiB.')


# ---- 5.7 read() down to my_read ----
def f7():
    o = [T(20, 28, 'read(fd, buf, 100) on /dev/mydrv  (c 240 3)', 15, 'start', bold=True)]
    names = [('your program', 90), ('VFS', 280), ('my_read', 460), ('buf (user)', 630)]
    for n, x in names:
        o.append(R(x - 70, 46, 140, 34, ACS if n == 'my_read' else PANEL, AC, 6, 2))
        o.append(TM(x, 68, n, 13, bold=True))
        o.append(L(x, 80, x, 300, L2, 1.4, '5 4'))
    msgs = [(90, 280, 112, 'read(fd, buf, 100)', AC, 'n'), (280, 460, 152, 'major 240 → mydrv', AC, 'n'),
            (460, 630, 192, 'copy_to_user, 100 B', LV, 'l'), (630, 460, 226, '0 B left over', L2, 'm'),
            (460, 280, 260, 'returns 100', LV, 'l'), (280, 90, 290, 'read() = 100', LV, 'l')]
    for a, b, y, s, c, ar in msgs:
        o.append(L(a, y, b + (-6 if b > a else 6), y, c, 2, '6 4' if c == L2 else None, arrow=ar))
        o.append(Tb((a + b) / 2, y - 8, s, 13, fill=c if c != L2 else MUT, bold=c != L2))
    o.append(R(20, 318, 680, 46, PANEL, L2, 6, 1.2))
    o.append(T(360, 346, 'dev_t = (240 << 8) | 3 = 61440 + 3 = 61443', 14, bold=True))
    return 378, ''.join(o)
FIG[7] = (f7, 'VFS reads major 240 from the device node and calls the driver\'s my_read, which copies all 100 bytes into the user buffer with 0 left over, so both my_read and read() return 100.',
          'A sequence of messages between four columns, your program, VFS, my_read and the user buffer: read for 100 bytes goes down, copy_to_user moves 100 bytes, and 100 comes back up. Below, dev_t worked out as 61443.')


# ---- 5.8 CPU shares with and without pinning ----
def f8():
    o = [T(20, 28, '8 equal CPU-bound tasks on 4 CPUs', 15, 'start', bold=True)]
    cw, x0 = 140, 110
    def panel(y, title, groups):
        out = [T(20, y, title, 14, 'start', bold=True)]
        for g in groups:
            cpus, ntask, share, c, cs = g
            gx = x0 + cpus[0] * (cw + 10)
            gw = len(cpus) * cw + (len(cpus) - 1) * 10
            out.append(R(gx, y + 12, gw, 92, FIGBG, c, 6, 1.5))
            out.append(T(gx + gw / 2, y + 32, ' + '.join(f'CPU {k}' for k in cpus) if len(cpus) < 3 else f'CPUs {cpus[0]}–{cpus[-1]}', 13, fill=c, bold=True))
            tw_ = (gw - 20 - (ntask - 1) * 6) / ntask
            for i in range(ntask):
                out.append(R(gx + 10 + i * (tw_ + 6), y + 44, tw_, 30, cs, c, 4, 1.4))
            out.append(T(gx + gw / 2, y + 96, f'{len(cpus)} ÷ {ntask} = {share} CPU each', 13, fill=c, bold=True))
        return ''.join(out)
    o.append(panel(60, 'no affinity', [([0], 2, '0.5', AC, ACS), ([1], 2, '0.5', AC, ACS), ([2], 2, '0.5', AC, ACS), ([3], 2, '0.5', AC, ACS)]))
    o.append(panel(200, 'four pinned to CPU 0', [([0], 4, '0.25', NX, NXS), ([1, 2, 3], 4, '0.75', LV, LVS)]))
    o.append(T(20, 344, 'The rule is capacity ÷ tasks sharing it: 4 ÷ 8 = 0.5, 1 ÷ 4 = 0.25 and 3 ÷ 4 = 0.75.', 13, 'start', MUT))
    return 360, ''.join(o)
FIG[8] = (f8, 'With no affinity each task gets 4 ÷ 8 = 0.5 CPU. Pinning four tasks to CPU 0 leaves them 1 ÷ 4 = 0.25 CPU each, while the other four share CPUs 1 to 3 at 0.75 CPU each.',
          'Two rows of CPU boxes: first, four CPUs each running two tasks at 0.5 CPU; second, CPU 0 crowded with four pinned tasks at 0.25 CPU each and CPUs 1 to 3 shared by four tasks at 0.75 CPU each.')


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
