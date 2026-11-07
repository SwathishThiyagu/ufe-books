"""Claude's hand-drawn figures for c-os-u5 (Operating Systems, unit 5: file systems, I/O and disks), one per chapter,
from each chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def badge(x, y, n, c=AC):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="11" style="fill:{c}"/>' + T(x, y + 4.5, str(n), 13, fill='var(--fig)', bold=True)


# ---- 5.1 direct access to record 250 ----
def f1():
    o = [T(30, 30, '1000 records of 200 bytes, numbered from 1', 15, 'start', bold=True)]
    cells = [('1', 0), ('2', 0), ('3', 0), ('…', 2), ('249', 0), ('250', 1), ('251', 0), ('…', 2), ('1000', 0)]
    x = 40
    pos = {}
    for lab, kind in cells:
        w = 40 if kind == 2 else 64
        if kind == 2:
            o.append(T(x + w / 2, 72, '…', 16, fill=MUT))
        else:
            o.append(boxt(x, 50, w - 4, 36, [lab], ACS if kind else PANEL, AC if kind else L2, 14, bold_first=bool(kind), rx=4))
        pos[lab] = x + (w - 4) / 2
        x += w
    o.append(f'<path d="M{pos["1"]:.1f},92 C{pos["1"]:.1f},150 {pos["250"]:.1f},150 {pos["250"]:.1f},92" style="fill:none;stroke:var(--accent);stroke-width:2.5" marker-end="url(#ar-UID-n)"/>')
    o.append(Tb((pos['1'] + pos['250']) / 2, 140, 'direct: jump to (250 − 1) × 200 = 49,800 bytes, 1 read', 13, fill=AC, bold=True))
    o.append(T(x - 4, 116, 'sequential: 250 reads,', 13, 'end', LV, True))
    o.append(T(x - 4, 132, 'one record after another', 13, 'end', LV))
    o.append(T(30, 196, 'Disk blocks of 4096 bytes, counted from 0', 15, 'start', bold=True))
    blocks = [(11, 45056), (12, 49152), (13, 53248)]
    for i, (b, start) in enumerate(blocks):
        bx = 60 + i * 200
        o.append(boxt(bx, 212, 196, 46, [f'block {b}'], ACS if b == 12 else PANEL, AC if b == 12 else L2, 14, bold_first=b == 12, rx=3))
        o.append(T(bx, 276, f'{start:,}', 13, fill=MUT))
    o.append(T(660, 276, '57,344', 13, fill=MUT))
    px = 260 + (49800 - 49152) / 4096 * 196
    o.append(L(px, 300, px, 262, LV, 2.5, arrow='l'))
    o.append(T(px, 316, 'byte 49,800', 13, fill=LV, bold=True))
    o.append(T(360, 350, 'floor(49,800 ÷ 4096) = floor(12.158) = 12, so the record starts in block 12.', 14))
    return 366, ''.join(o)
FIG[1] = (f1, 'Direct access computes where record 250 starts, (250 − 1) × 200 = 49,800 bytes, and reads it at once, while sequential access passes 250 records. Byte 49,800 lies in disk block 12.',
          'A strip of fixed-size records with an arrow jumping from record 1 to record 250, above a strip of disk blocks 11 to 13 with byte 49,800 marked inside block 12.')


# ---- 5.2 path resolution ----
def f2():
    o = [T(30, 30, 'Resolving /home/ravi/notes.txt (1 ms per directory read)', 15, 'start', bold=True)]
    steps = [('/ (root)', 'home', 'cached', '0 ms', 0, NX), ('home', 'ravi', 'read', '1 ms', 1, AC), ('ravi', 'notes.txt', 'read', '1 ms', 2, AC)]
    for i, (name, entry, how, cost, cum, c) in enumerate(steps):
        x = 20 + i * 176
        o.append(R(x, 52, 150, 116, PANEL, c, 8))
        o.append(T(x + 75, 76, name, 15, bold=True))
        o.append(T(x + 75, 96, 'directory', 13, fill=MUT))
        o.append(boxt(x + 12, 108, 126, 34, [f'entry: {entry}'], ACS if c == AC else NXS, c, 13, rx=4))
        o.append(T(x + 75, 160, f'{how}: {cost}', 13, fill=c, bold=True))
        o.append(L(x + 150, 125, x + 174, 125, AC, 2, arrow='n'))
        o.append(T(x + 75, 196, f'total so far: {cum} ms', 14, bold=(i == 2)))
    o.append(boxt(548, 88, 150, 74, ['inode 2048', 'notes.txt'], NXS, NX, 15, bold_first=True))
    o.append(L(20, 216, 700, 216, LN, 1))
    o.append(T(360, 250, 'Root cached: 0 + 1 + 1 = 2 ms', 15, bold=True, fill=AC))
    o.append(T(360, 276, 'Root not cached: one more read, 2 + 1 = 3 ms', 15))
    return 294, ''.join(o)
FIG[2] = (f2, 'Each directory on the path names the next one: the root (cached) gives home, home gives ravi, and ravi gives inode 2048 for notes.txt. Two 1 ms reads make 2 ms, or 3 ms if the root must be read too.',
          'Three directory boxes, root, home and ravi, each holding the entry for the next name, ending at inode 2048, with the running time 0, 1 and 2 ms.')


# ---- 5.3 mounting hides the old directory ----
def f3():
    o = []
    def chain(x0, title, usb_note, leaf, leaf_c, leaf_f):
        o.append(T(x0 + 150, 30, title, 15, bold=True))
        names = ['/', 'mnt', 'usb', 'note.txt']
        for i, n in enumerate(names):
            y = 50 + i * 62
            mounted = usb_note and n in ('usb', 'note.txt')
            o.append(boxt(x0 + 20, y, 120, 40, [n], NXS if mounted else PANEL, NX if mounted else L2, 14, bold_first=True))
            if i: o.append(L(x0 + 80, y - 22, x0 + 80, y - 2, L2, 2, arrow='m'))
        o.append(L(x0 + 140, 50 + 3 * 62 + 20, x0 + 168, 50 + 3 * 62 + 20, leaf_c, 2.5, arrow='x' if leaf_c == NX else 'n'))
        o.append(boxt(x0 + 172, 50 + 3 * 62, 130, 40, [leaf], leaf_f, leaf_c, 14, bold_first=True))
    chain(20, 'Before the mount', False, 'local inode 101', AC, ACS)
    chain(380, 'After mounting /dev/sdb1 on /mnt/usb', True, 'USB inode 77', NX, NXS)
    o.append(T(560, 180, '/dev/sdb1', 13, 'start', NX, True)); o.append(T(560, 196, 'file system starts here', 13, 'start', NX))
    o.append(L(556, 186, 524, 186, NX, 1.5, arrow='x'))
    o.append(boxt(400, 306, 300, 56, ['old local note.txt (inode 101): hidden,', 'but a process that opened it earlier still reads it'], PANEL, L2, 13, dash='6 4'))
    o.append(L(360, 30, 360, 360, LN, 1))
    return 372, ''.join(o)
FIG[3] = (f3, 'The same path /mnt/usb/note.txt resolves to local inode 101 before the mount and to USB inode 77 after it. The old local file is hidden from new lookups, but a process that already opened it keeps reading inode 101.',
          'Two path chains from root to mnt, usb and note.txt: before mounting it ends at local inode 101, after mounting the USB part ends at inode 77 and the old file is shown hidden.')


# ---- 5.4 open and two reads move the offset ----
def f4():
    o = []
    flow = [(20, 230, ['open("/home/ravi/notes.txt")']), (280, 90, ['VFS']), (400, 300, ['ext4: inode 2048, size 4000 B'])]
    for x, w, lab in flow:
        o.append(boxt(x, 20, w, 40, lab, ACS if x == 400 else PANEL, AC, 13, bold_first=x == 400))
    o.append(L(250, 40, 276, 40, AC, 2, arrow='n')); o.append(L(370, 40, 396, 40, AC, 2, arrow='n'))
    s = 600 / 4000
    o.append(T(60, 104, 'the whole file, 4000 bytes', 13, 'start', MUT))
    o.append(R(60, 112, 600, 36, PANEL, L2, 4, 1.5))
    o.append(R(60, 112, 150 * s, 36, LVS, LV, 2, 1.5))
    o.append(T(60 + 150 * s + (600 - 150 * s) / 2, 135, 'left after the reads: 4000 − 150 = 3850 bytes', 14))
    o.append(P([(60, 150), (60, 214)], L2, 1.5, '4 4')); o.append(P([(60 + 150 * s, 150), (510, 214)], L2, 1.5, '4 4'))
    z = 3.0
    o.append(T(60, 206, 'zoom: the first 200 bytes', 13, 'start', MUT))
    o.append(boxt(60, 216, 100 * z, 44, ['read 1: 100 bytes'], ACS, AC, 14, rx=3))
    o.append(boxt(60 + 100 * z, 216, 50 * z, 44, ['read 2: 50'], NXS, NX, 14, rx=3))
    o.append(R(60 + 150 * z, 216, 50 * z, 44, PANEL, L2, 3, 1.5, '4 4'))
    for b, lab, c in ((0, 'offset 0', MUT), (100, 'after read 1: 100', AC), (150, 'after read 2: 150', NX)):
        X = 60 + b * z
        o.append(L(X, 262, X, 286, c, 2))
        o.append(T(X + (4 if b == 0 else 0), 302, lab, 13, 'start' if b == 0 else 'middle', c, b != 0))
    o.append(T(360, 340, 'Each read starts at the saved offset and moves it forward: 0 → 100 → 150.', 14))
    return 356, ''.join(o)
FIG[4] = (f4, 'open() reaches ext4 inode 2048 through the VFS and sets the offset to 0. The first read takes bytes 0–100 and the second 100–150, so the offset is 150 and 3850 of the 4000 bytes are left.',
          'A flow from open through the VFS to inode 2048, a bar for the 4000-byte file with the first 150 bytes marked, and a zoom showing read 1 of 100 bytes and read 2 of 50 bytes.')


# ---- 5.5 disk reads to reach logical block 2 ----
def f5():
    o = [T(30, 30, 'Disk reads to fetch logical block 2 (the third block) of file F', 15, 'start', bold=True)]
    def row(y, name, total, items):
        o.append(T(30, y + 26, name, 15, 'start', bold=True)); o.append(T(30, y + 46, f'{total} read' + ('s' if total > 1 else ''), 14, 'start', LV, True))
        for kind, x, w, lab, n in items:
            if kind == 'box':
                hot = n is not None
                o.append(boxt(x, y + 8, w, 40, [lab], ACS if hot else PANEL, AC if hot else L2, 14, bold_first=hot, rx=4))
                if hot: o.append(badge(x + w - 4, y + 6, n, LV))
            elif kind == 'arrow':
                o.append(L(x, y + 28, x + w, y + 28, AC, 2, arrow='n'))
            elif kind == 'note':
                o.append(T(x, y + 74, lab, 13, 'start', MUT))
    row(50, 'Contiguous', 1, [('box', 160, 60, '12', None), ('box', 224, 60, '13', None), ('box', 288, 60, '14', 1), ('box', 352, 60, '15', None),
                              ('note', 160, 0, 'start 12 + 2 = block 14: computed, then read once', None)])
    row(150, 'Linked', 3, [('box', 160, 60, '12', 1), ('arrow', 222, 30, '', None), ('box', 256, 60, '7', 2), ('arrow', 318, 30, '', None),
                           ('box', 352, 60, '20', 3), ('arrow', 414, 30, '', None), ('box', 448, 60, '5', None),
                           ('note', 160, 0, 'each block holds the next pointer, so 12 and 7 must be read first', None)])
    row(250, 'Indexed', 2, [('box', 160, 150, 'index block 30', 1), ('arrow', 312, 30, '', None), ('box', 346, 60, '20', 2),
                            ('note', 160, 0, 'entry 2 of the index is 20, so one more read gets the data', None)])
    o.append(R(560, 252, 150, 56, PANEL, LN, 6, 1)); o.append(T(635, 274, 'index entries', 13, fill=MUT)); o.append(T(635, 294, '12, 7, 20, 5', 14, bold=True))
    return 350, ''.join(o)
FIG[5] = (f5, 'Fetching logical block 2 of F: contiguous allocation computes block 14 and reads it once, linked allocation must follow 12 → 7 → 20 (3 reads), and indexed allocation reads index block 30 and then block 20 (2 reads).',
          'Three rows of disk blocks for contiguous, linked and indexed allocation, with numbered badges marking each disk read needed to reach logical block 2.')


# ---- 5.6 free-space bitmap ----
def f6():
    used = {0, 1, 2, 5, 9, 10, 15}
    x0, cw = 40, 40
    o = [T(30, 30, 'Bitmap for 16 blocks: 1 = free, 0 = used', 15, 'start', bold=True), T(30, 66, 'block', 13, 'start', MUT)]
    for b in range(16):
        x = x0 + b * cw
        free = b not in used
        o.append(T(x + cw / 2, 84, str(b), 13, fill=MUT))
        o.append(boxt(x + 2, 94, cw - 4, 46, ['1' if free else '0'], NXS if free else PANEL, NX if free else L2, 17, bold_first=free, rx=4))
    o.append(L(x0 + 3 * cw + cw / 2, 196, x0 + 3 * cw + cw / 2, 146, LV, 2.5, arrow='l'))
    o.append(T(x0 + 3 * cw + cw / 2 - 30, 214, 'first free: block 3', 14, 'start', LV, True))
    o.append(P([(x0 + 2, 150), (x0 + 2, 160), (x0 + 3 * cw - 2, 160), (x0 + 3 * cw - 2, 150)], MUT, 1.5))
    o.append(T(x0 + 1.5 * cw, 178, 'scan: 0, 0, 0', 13, fill=MUT))
    o.append(T(30, 258, 'Read left to right: 0001101110011110', 15, 'start', bold=True))
    o.append(T(30, 284, 'Used blocks 0, 1, 2, 5, 9, 10, 15 → free = 16 − 7 = 9 blocks', 14, 'start'))
    return 300, ''.join(o)
FIG[6] = (f6, 'One bit per block: the seven used blocks are 0 and the nine free blocks are 1. A first-fit scan passes the 0s in blocks 0, 1 and 2 and stops at block 3.',
          'Sixteen bit cells for blocks 0 to 15, with free blocks marked 1 and used blocks 0, and an arrow at block 3 as the first free block.')


# ---- 5.7 polling vs interrupt during one DMA-free transfer ----
def f7():
    x0, s = 150, 520 / 41
    tx = lambda us: x0 + us * s
    o = [T(138, 66, 'device', 14, 'end', bold=True), T(138, 82, 'transfer', 13, 'end', MUT),
         T(138, 146, 'polling', 14, 'end', bold=True), T(138, 162, 'every 1 µs', 13, 'end', MUT),
         T(138, 226, 'interrupt', 14, 'end', bold=True), T(138, 242, 'one signal', 13, 'end', MUT)]
    o.append(boxt(tx(0), 52, 40.96 * s, 40, ['4096 B ÷ 100 MB/s = 40.96 µs'], ACS, AC, 14))
    for t in range(41):
        o.append(L(tx(t), 132, tx(t), 172, LV, 2))
    o.append(Tb(tx(20.5), 190, '41 status reads at 0, 1, 2, …, 40 µs', 13, fill=LV, bold=True))
    o.append(L(tx(0), 232, tx(40.96), 232, L2, 1.5, '4 4'))
    o.append(L(tx(40.96), 252, tx(40.96), 210, NX, 3, arrow='x'))
    o.append(T(tx(40.96) - 8, 252, 'done at 40.96 µs', 13, 'end', NX, True))
    o.append(T(tx(20), 226, 'CPU free for other work', 13, fill=MUT))
    o.append(xaxis(x0, tx(41), 272, [0, 10, 20, 30, 40], tx, 'time (µs)'))
    o.append(T(360, 346, 'Polls = ⌊40.96 ÷ 1⌋ + 1 = 41; the interrupt costs the CPU one entry instead.', 14))
    return 362, ''.join(o)
FIG[7] = (f7, 'Moving 4 KB at 100 MB/s takes 40.96 µs. A CPU polling once per µs checks the status 41 times in that window, while with an interrupt it is told once, when the transfer ends.',
          'Three lanes over 41 microseconds: the device transfer bar, 41 polling ticks, and a single interrupt arrow at 40.96 microseconds.')


# ---- 5.8 cache hit ratio vs average read time ----
def f8():
    x0, x1, y0, y1 = 80, 680, 60, 300
    fx = lambda h: x0 + h * (x1 - x0)
    fy = lambda t: y1 - t / 10 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [0, 0.2, 0.4, 0.6, 0.8, 1.0], [0, 2, 4, 6, 8, 10], fx, fy, 'cache hit ratio h', 'average read time (ms)', lambda v: f'{v:g}')]
    o.append(P([(fx(0), fy(10)), (fx(1), fy(0.1))], AC, 3))
    o.append(L(fx(0.8), fy(2.08), fx(0.8), y1, INK, 1.5, '4 4')); o.append(L(x0, fy(2.08), fx(0.8), fy(2.08), INK, 1.5, '4 4'))
    o.append(C(fx(0.8), fy(2.08), 6, AC))
    o.append(T(fx(0.6), fy(7.2), 'h = 0.8:', 14, 'start', AC, True))
    o.append(T(fx(0.6), fy(6.4), '0.8 × 0.1 + 0.2 × 10', 14, 'start'))
    o.append(T(fx(0.6), fy(5.6), '= 0.08 + 2.0 = 2.08 ms', 14, 'start', AC, True))
    o.append(L(fx(0.79), fy(5.1), fx(0.8), fy(2.08) - 9, AC, 1.5))
    o.append(T(fx(0.22), fy(9.2), 'h = 0: every read goes to disk, 10 ms', 13, 'start', MUT))
    o.append(T(fx(1) - 4, fy(2.6), 'h = 1: 0.1 ms', 13, 'end', MUT))
    o.append(T(380, 382, '1000 reads × 2.08 ms = 2080 ms. The misses (2.0 ms) dominate the average.', 14))
    return 396, ''.join(o)
FIG[8] = (f8, 'The average read time falls in a straight line as more reads hit the 0.1 ms cache instead of the 10 ms disk. At h = 0.8 it is 2.08 ms, so 1000 reads take 2080 ms.',
          'A falling line of average read time from 10 ms at hit ratio 0 to 0.1 ms at hit ratio 1, with the point h = 0.8, 2.08 ms marked.')


# ---- 5.9 disk scheduling head paths ----
def f9():
    x0, x1 = 186, 690
    cx = lambda c: x0 + c / 199 * (x1 - x0)
    o = [L(x0, 40, x1, 40, L2, 1.5)]
    for c in (0, 50, 100, 150, 199):
        o += [L(cx(c), 36, cx(c), 44, L2, 1.5), T(cx(c), 30, str(c), 13, fill=MUT)]
    o.append(T(x0 - 12, 30, 'cylinder', 13, 'end', MUT))
    algos = [('FCFS', 300, [50, 55, 90, 30, 120, 10], LV), ('SSTF', 160, [50, 55, 30, 10, 90, 120], AC), ('SCAN to 0', 170, [50, 30, 10, 0, 55, 90, 120], NX)]
    y = 62
    for name, tot, path, c in algos:
        pts = [(cx(v), y + i * 16) for i, v in enumerate(path)]
        o.append(T(x0 - 14, y + 30, name, 15, 'end', bold=True)); o.append(T(x0 - 14, y + 50, f'{tot} cylinders', 13, 'end', c, True))
        o.append(P(pts, c, 2.5))
        for i, (v, (px, py)) in enumerate(zip(path, pts)):
            o.append(C(px, py, 4.5, INK if i == 0 else c))
            nb = [path[j] for j in (i - 1, i + 1) if 0 <= j < len(path)]
            lab, col = ('start 50' if i == 0 else str(v)), (INK if i == 0 else c)
            if all(q <= v for q in nb): o.append(T(px + 9, py + 5, lab, 13, 'start', col))
            elif all(q >= v for q in nb) and v >= 15: o.append(T(px - 9, py + 5, lab, 13, 'end', col))
            elif all(q >= v for q in nb): o.append(T(px, py + 19, lab, 13, fill=col))
            elif path[i - 1] < v: o.append(T(px - 8, py + 15, lab, 13, 'end', col))
            else: o.append(T(px + 8, py + 15, lab, 13, 'start', col))
        y += len(path) * 16 + 30
    o.append(T(360, y + 6, 'SSTF moves least (160); SCAN moves 170 but no request waits more than one sweep.', 14, bold=True))
    return y + 22, ''.join(o)
FIG[9] = (f9, 'The head starts at cylinder 50 with requests 55, 90, 30, 120 and 10. FCFS zigzags 300 cylinders, SSTF always takes the nearest for 160, and SCAN sweeps down to 0 and back for 170.',
          'Three head paths drawn over a cylinder axis from 0 to 199: FCFS zigzags widely, SSTF goes 55, 30, 10 then 90, 120, and SCAN goes down to 0 then up to 120.')


spec = make_spec(FIG)
