"""Claude's hand-drawn figures for c-os-u1 (Operating Systems, unit 1), one per chapter, from each chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


# ---- 1.1 four apps, 8 GB RAM, 8 cores ----
def f1():
    s, x0 = 60, 60
    gx = lambda gb: x0 + gb * s
    o = [T(x0, 28, 'What the apps ask for: 4 × 2.5 GB = 10 GB', 15, 'start', bold=True), L(gx(8), 36, gx(8), 206, INK, 2, '5 4')]
    for i in range(4):
        fits = i < 3
        o.append(boxt(gx(i * 2.5) + 2, 42, 146, 44, [f'App {i + 1} · 2.5 GB'], ACS if fits else LVS, AC if fits else LV, 14,
                      dash=None if fits else '6 4'))
    o.append(brace(gx(8), gx(10), 98))
    o.append(T(gx(9), 122, 'short by 2.0 GB', 14, bold=True, fill=LV))
    o.append(T(x0, 140, 'What the phone has: RAM = 8 GB', 15, 'start', bold=True))
    o.append(Tb(gx(8) + 6, 140, '8 GB', 13, 'start', MUT))
    o.append(R(x0, 150, 8 * s, 52, PANEL, INK, 8))
    for i in range(3):
        o.append(boxt(gx(i * 2.5) + 4, 154, 142, 44, [f'App {i + 1}'], ACS, AC, 14))
    o.append(R(gx(7.5) + 3, 154, 24, 44, PANEL, L2, 4, 1.5, '3 3'))
    o.append(T(gx(7.75), 222, '0.5 GB free', 13, fill=MUT))
    o.append(T(gx(3.75), 222, '3 apps fit: 3 × 2.5 = 7.5 GB', 13, fill=MUT))
    o.append(T(x0, 262, 'CPU: 8 cores, so all 4 apps can run at the same time', 15, 'start', bold=True))
    for i in range(8):
        on = i < 4
        o.append(boxt(x0 + i * 56, 276, 48, 40, [f'A{i + 1}' if on else 'idle'], NXS if on else PANEL, NX if on else L2, 13))
    o.append(T(x0 + 8 * 56 + 8, 301, 'cores are not the problem', 14, 'start', MUT))
    o.append(T(x0, 352, 'RAM is the limit. The OS keeps 3 apps in RAM, and for app 4 it swaps', 14, 'start'))
    o.append(T(x0, 374, 'data out to storage, refuses the request, or reclaims cached memory.', 14, 'start'))
    return 390, ''.join(o)
FIG[1] = (f1, 'Four apps ask for 10 GB but the phone has 8 GB of RAM, so only 3 apps (7.5 GB) fit and app 4 is 2.0 GB short. The 8 cores could run all four; memory is what runs out, and the OS decides what to do about it.',
          'Four 2.5 GB app blocks laid against an 8 GB RAM bar: three fit, the fourth crosses the 8 GB line by 2 GB; below, 8 CPU cores with only 4 in use.')


# ---- 1.2 DMA + interrupt timeline ----
def f2():
    x0, s = 130, 5.6
    tx = lambda ms: x0 + ms * s
    o = [T(120, 120, 'CPU', 15, 'end', bold=True), T(120, 230, 'Disk', 15, 'end', bold=True)]
    o.append(boxt(tx(0), 96, 40 * s, 40, ['application 40 ms'], ACS, AC, 14))
    o.append(R(tx(40), 96, 5 * s, 40, LVS, LV, 4))
    o.append(boxt(tx(45), 96, 10 * s, 40, ['ISR'], LVS, LV, 13, rx=4))
    o.append(boxt(tx(55), 96, 45 * s, 40, ['application 45 ms'], ACS, AC, 14))
    o.append(L(tx(42.5), 66, tx(42.5), 94, LV, 1.5))
    o.append(T(tx(42.5) + 4, 60, 'interrupt entry 5 ms', 13, 'end', LV))
    o.append(L(tx(50), 84, tx(50), 94, LV, 1.5))
    o.append(T(tx(50) - 4, 80, 'disk ISR 10 ms', 13, 'start', LV))
    o.append(boxt(tx(0), 206, 40 * s, 40, ['DMA copies the block 40 ms'], NXS, NX, 14))
    o.append(boxt(tx(40), 206, 60 * s, 40, ['idle'], PANEL, L2, 13, dash='6 4'))
    o.append(L(tx(40), 204, tx(40), 142, LV, 2.5, arrow='l'))
    o.append(Tb(tx(40) + 8, 186, 'interrupt at 40 ms', 13, 'start', LV, True))
    o.append(L(tx(55), 140, tx(55), 160, AC, 1.5))
    o.append(Tb(tx(55) + 6, 162, 'resumes at 55 ms', 13, 'start', AC, True))
    o.append(xaxis(x0, tx(100), 272, list(range(0, 101, 10)), tx, 'time (ms)'))
    o.append(T(40, 350, 'Application time: 40 + 45 = 85 ms.  Interrupt handling: 5 + 10 = 15 ms.', 14, 'start'))
    o.append(T(40, 372, 'Check: 85 + 15 = 100 ms. The CPU did useful work while the disk copied.', 14, 'start'))
    return 390, ''.join(o)
FIG[2] = (f2, 'The disk copies the block by DMA for 40 ms while the CPU keeps running the application; one interrupt at 40 ms costs the CPU 5 + 10 = 15 ms, and the application resumes at 55 ms for 85 ms of work in 100 ms.',
          'Two timelines from 0 to 100 ms: the CPU runs the application, briefly handles an interrupt from 40 to 55 ms, then runs again; the disk does DMA from 0 to 40 ms and then sits idle.')


# ---- 1.3 eras of operating systems ----
def f3():
    x0, s = 70, 8
    tx = lambda yr: x0 + (yr - 1950) * s
    lanes = [('Batch', 1950, 1965, PANEL, L2), ('Time-sharing', 1965, 1985, ACS, AC), ('PC', 1980, 2000, PANEL, L2), ('Mobile', 2000, 2025, PANEL, L2)]
    o = [R(tx(1980), 100, 5 * s, 102, LVS, LV, 3, 1.5, '4 3')]
    o.append(T(tx(1982.5), 46, 'overlap: 1985 − 1980 = 5 years', 14, bold=True, fill=LV))
    o.append(L(tx(1982.5), 52, tx(1982.5), 98, LV, 1.5, arrow='l'))
    for i, (n, a, b, f, st) in enumerate(lanes):
        y = 62 + i * 46
        o.append(boxt(tx(a), y, (b - a) * s, 34, [n], f, st, 14, bold_first=(n == 'Time-sharing')))
    o.append(T(tx(1985) + 10, 135, '← first type where a user could', 13, 'start', AC))
    o.append(T(tx(1985) + 24, 151, 'talk to a running job', 13, 'start', AC))
    o.append(xaxis(x0, tx(2025), 256, [1950, 1965, 1980, 1985, 2000, 2025], tx))
    o.append(brace(tx(1950), tx(2025), 300, INK, up=True))
    o.append(Tb(tx(1987.5), 305, 'full span: 2025 − 1950 = 75 years', 14, bold=True))
    return 324, ''.join(o)
FIG[3] = (f3, 'The four eras on one time line: time-sharing (1965–1985) and PC systems (1980–2000) overlap for 5 years, and batch to mobile spans 75 years. Time-sharing was the first to let a user interact with a running job.',
          'Four horizontal bars for batch, time-sharing, PC and mobile systems from 1950 to 2025, with the 1980 to 1985 overlap of time-sharing and PC shaded.')


# ---- 1.4 mode bit over time ----
def f4():
    x0, s = 196, 40
    tx = lambda ms: x0 + ms * s
    yu, yk = 100, 200
    o = [R(tx(5), yu, 2 * s, yk - yu, LVS, 'none', 0, 0), R(tx(10), yu, 2 * s, yk - yu, LVS, 'none', 0, 0)]
    o += [L(x0, yu, tx(12), yu, LN, 1, '3 4'), L(x0, yk, tx(12), yk, LN, 1, '3 4')]
    o += [T(170, yu - 4, 'user mode', 14, 'end', bold=True), T(170, yu + 14, 'bit = 1', 13, 'end', MUT),
          T(170, yk - 4, 'kernel mode', 14, 'end', bold=True), T(170, yk + 14, 'bit = 0', 13, 'end', MUT)]
    o.append(P([(tx(0), yu), (tx(5), yu), (tx(5), yk), (tx(7), yk), (tx(7), yu), (tx(10), yu), (tx(10), yk), (tx(12), yk)], AC, 3))
    for t, lab, yy in ((5, 'read() traps', 40), (7, 'kernel returns', 62), (10, 'timer fires', 40)):
        o.append(L(tx(t), yy + 6, tx(t), 240, L2, 1.2, '4 4'))
        o.append(Tb(tx(t), yy, lab, 13, fill=LV if t != 7 else AC, bold=True))
    o.append(T(tx(6), yk + 32, 'kernel runs read()', 13, fill=LV))
    o.append(T(tx(6), yk + 48, '2 ms', 13, fill=LV))
    o.append(T(tx(11), yk + 32, 'timer handler', 13, fill=LV))
    for t, b in ((0, 1), (5, 0), (7, 1), (10, 0)):
        y = yu if b else yk
        o.append(f'<circle cx="{tx(t):.1f}" cy="{y}" r="13" style="fill:var(--panel);stroke:var(--accent);stroke-width:2.5"/>')
        o.append(T(tx(t), y + 5, str(b), 14, bold=True))
    o.append(xaxis(x0, tx(12), 270, [0, 2, 4, 5, 7, 10, 12], tx, 'time (ms)'))
    o.append(T(60, 346, 'Mode bit:', 15, 'start', bold=True))
    for i, (t, b) in enumerate(((0, 1), (5, 0), (7, 1), (10, 0))):
        o.append(T(170 + i * 130, 346, f't = {t} ms → {b}', 15, 'start', bold=True, fill=AC if b else LV))
    return 364, ''.join(o)
FIG[4] = (f4, 'The mode bit is 1 while the process runs its own code and drops to 0 whenever the CPU enters the kernel: at the read() trap (5 ms) and at the timer interrupt (10 ms). The kernel returns to user mode at 7 ms.',
          'A step line between user mode (bit 1) and kernel mode (bit 0) from 0 to 12 ms, dropping at 5 ms, rising at 7 ms and dropping again at 10 ms.')


# ---- 1.5 UPI payment service times ----
def f5():
    rows = [('UI event · user interface', 20, False), ('Fingerprint · I/O', 30, True), ('Network · communication', 40, True),
            ('Payment log · file system', 10, True), ('3 checks · protection', 3, False), ('Record · accounting', 2, False)]
    xb, s = 262, 9
    o = [R(262, 22, 18, 14, ACS, AC, 3), T(286, 34, 'I/O step', 13, 'start'), R(372, 22, 18, 14, PANEL, L2, 3), T(396, 34, 'other step', 13, 'start')]
    for i, (n, ms, io) in enumerate(rows):
        y = 56 + i * 40
        o.append(T(250, y + 18, n, 14, 'end'))
        o.append(R(xb, y, ms * s, 26, ACS if io else PANEL, AC if io else L2, 4))
        o.append(T(xb + ms * s + 8, y + 18, f'{ms} ms' if ms != 3 else '3 × 1 = 3 ms', 14, 'start', bold=io))
    o.append(T(360, 320, 'Total = 20 + 30 + 40 + 10 + 3 + 2 = 105 ms', 14, bold=True))
    s2, x0 = 600 / 105, 60
    o.append(boxt(x0, 334, 80 * s2, 36, ['I/O = 30 + 40 + 10 = 80 ms'], ACS, AC, 14))
    o.append(boxt(x0 + 80 * s2, 334, 25 * s2, 36, ['other 25 ms'], PANEL, L2, 13))
    o.append(T(360, 398, 'I/O share = 80 ÷ 105 × 100 ≈ 76.19%', 15, bold=True, fill=AC))
    return 414, ''.join(o)
FIG[5] = (f5, 'The six OS services behind the ₹500 UPI payment and the time each takes. The three I/O steps add to 80 ms of the 105 ms total, about 76.19%.',
          'Horizontal bars for six service steps of a UPI payment, with the fingerprint, network and log bars marked as I/O, and a total bar split into 80 ms of I/O and 25 ms of other work.')


# ---- 1.6 read(fd, buf, 10) system call path ----
def f6():
    xp, xl, xk = 110, 340, 590
    o = [R(470, 74, 240, 346, LVS, 'none', 10, 0)]
    o.append(T(250, 92, 'user mode', 13, fill=MUT, bold=True)); o.append(T(590, 92, 'kernel mode', 13, fill=LV, bold=True))
    for x, n in ((xp, 'Your program'), (xl, 'C library read()'), (xk, 'Kernel')):
        o.append(boxt(x - 85, 18, 170, 40, [n], PANEL, AC if x != xk else LV, 14, bold_first=True))
        o.append(L(x, 58, x, 410, L2, 1.5, '4 4'))
    o.append(L(xp, 124, xl - 4, 124, AC, 2, arrow='n')); o.append(Tb((xp + xl) / 2, 116, 'read(fd, buf, 10)', 14))
    o.append(boxt(xl - 80, 140, 160, 86, ['rax = 0 (read)', 'rdi = fd', 'rsi = buf', 'rdx = 10'], ACS, AC, 13))
    o.append(L(xl, 256, xk - 4, 256, LV, 2.5, arrow='l')); o.append(Tb(530, 248, 'syscall trap', 14, bold=True, fill=LV))
    o.append(boxt(xk - 100, 270, 200, 56, ['only 6 bytes left,', 'so it copies 6 into buf'], PANEL, LV, 13))
    o.append(L(xk, 352, xl + 4, 352, AC, 2, arrow='n')); o.append(Tb(470, 344, 'returns 6', 14, bold=True))
    o.append(L(xl, 388, xp + 4, 388, AC, 2, arrow='n')); o.append(Tb((xp + xl) / 2, 380, 'returns 6', 14, bold=True))
    y = 440
    o.append(T(30, y + 21, 'file:', 14, 'start', MUT))
    for i in range(6):
        o.append(boxt(70 + i * 40, y, 36, 32, [str(i + 1)], ACS, AC, 13, rx=4))
    o.append(boxt(310, y, 52, 32, ['EOF'], PANEL, L2, 13, rx=4))
    o.append(T(378, y + 12, 'asked for 10, got 6: 4 not read', 13, 'start'))
    o.append(T(378, y + 30, 'the next read() returns 0 (end of file)', 13, 'start'))
    return 486, ''.join(o)
FIG[6] = (f6, 'The path of read(fd, buf, 10): the library loads the call number 0 and the three arguments into registers and traps; the kernel finds only 6 bytes before end of file, copies them, and 6 comes back to the program. The next read returns 0.',
          'A sequence from the program to the C library to the kernel and back, with the registers rax, rdi, rsi and rdx, and a strip of 6 file bytes followed by end of file.')


# ---- 1.7 microkernel vs monolithic ----
def f7():
    o = [T(185, 28, 'Microkernel', 15, bold=True), T(535, 28, 'Monolithic kernel', 15, bold=True)]
    for x in (20, 370):
        o.append(R(x, 40, 330, 156, PANEL, LN, 10, 1))
        o.append(R(x, 204, 330, 96, LVS, 'none', 10, 0))
        o.append(T(x + 10, 58, 'user mode', 13, 'start', MUT, True))
        o.append(T(x + 10, 222, 'kernel mode', 13, 'start', LV, True))
    for j, (a, b) in enumerate(((40, 70), (190, 70), (40, 132), (190, 132))):
        crash = j == 0
        o.append(boxt(a, b, 140, 52, ['file server' if crash else 'server', '150,000 lines'], LVS if crash else ACS, LV if crash else AC, 13,
                      bold_first=True, dash='6 4' if crash else None))
    o.append(boxt(130, 232, 150, 52, ['kernel', '20,000 lines'], ACS, AC, 13, bold_first=True))
    o.append(P([(130, 258), (34, 258), (34, 102), (38, 102)], NX, 2, '5 4'))
    o.append(f'<line x1="34" y1="103" x2="38" y2="103" style="stroke:var(--next);stroke-width:2" marker-end="url(#ar-UID-x)"/>')
    o.append(Tb(84, 196, 'restarts it', 13, fill=NX, bold=True))
    o.append(T(535, 120, 'only the apps live up here', 13, fill=MUT))
    o.append(R(384, 232, 302, 60, ACS, AC, 8))
    o.append(T(470, 256, 'one kernel', 13, bold=True))
    o.append(T(470, 274, '5,000,000 lines', 13))
    o.append(boxt(560, 240, 116, 44, ['file service', 'crashes'], LVS, LV, 13, dash='6 4'))
    o.append(T(185, 322, 'in kernel mode: 20,000 ÷ 620,000 = 3.23%', 13))
    o.append(T(185, 340, 'crash: kill and restart one server', 13, fill=NX, bold=True))
    o.append(T(535, 322, 'in kernel mode: all 5,000,000 = 100%', 13))
    o.append(T(535, 340, 'crash: a bad pointer can stop the machine', 13, fill=LV, bold=True))
    s = 520 / 5_000_000
    o.append(T(30, 380, 'Total code', 14, 'start', bold=True))
    o.append(T(180, 406, 'microkernel 620,000', 13, 'end')); o.append(R(190, 394, 620_000 * s, 18, ACS, AC, 3))
    o.append(T(180, 432, 'monolithic 5,000,000', 13, 'end')); o.append(R(190, 420, 5_000_000 * s, 18, ACS, AC, 3))
    o.append(Tb(268, 406, '5,000,000 ÷ 620,000 ≈ 8.06 times larger', 13, 'start', bold=True))
    return 450, ''.join(o)
FIG[7] = (f7, 'In the microkernel system only the 20,000-line kernel runs in kernel mode (3.23% of the code), so a crashed file server is just restarted. The monolithic kernel puts all 5,000,000 lines in kernel mode, where one fault can stop the machine.',
          'Two panels split into user mode and kernel mode: on the left four 150,000-line servers above a small 20,000-line kernel, with the crashed file server restarted; on the right one large 5,000,000-line kernel holding the crashed file service.')


# ---- 1.8 boot timeline ----
def f8():
    x0, s = 60, 60
    tx = lambda t: x0 + t * s
    segs = [('firmware POST', 0, 2, PANEL, L2), ('bootloader', 2, 5, ACS, AC), ('kernel load', 5, 9, ACS, AC), ('init', 9, 10, PANEL, L2)]
    o = [T(tx(0), 50, 'power on', 13, 'start', MUT, True), L(tx(0), 56, tx(0), 76, L2, 1.5, arrow='m')]
    o.append(T(tx(10) + 6, 50, 'login prompt', 13, 'end', NX, True)); o.append(L(tx(10), 56, tx(10), 76, NX, 2, arrow='x'))
    for n, a, b, f, st in segs:
        o.append(boxt(tx(a), 80, (b - a) * s, 56, [n, f'{b - a} s'], f, st, 14 if b - a > 1 else 13, bold_first=True))
    o.append(xaxis(x0, tx(10), 160, [0, 2, 5, 9, 10], tx, 'seconds after power on'))
    o.append(brace(tx(2), tx(9), 148, AC, up=True))
    o.append(T(360, 238, 'Running total: 2 + 3 = 5 s, then 5 + 4 = 9 s, then 9 + 1 = 10 s', 14))
    o.append(T(360, 262, 'Bootloader and kernel load take 7 of the 10 seconds.', 14, bold=True, fill=AC))
    return 280, ''.join(o)
FIG[8] = (f8, 'The four boot stages in order on one 10 s time line; the running total reaches 10 s at the login prompt. The bootloader and kernel load take 7 of the 10 seconds.',
          'A bar from power on to the login prompt split into firmware 2 s, bootloader 3 s, kernel load 4 s and init 1 s, with marks at 2, 5, 9 and 10 seconds.')


# ---- 1.9 VMs on one host: CPU vs memory ----
def f9():
    o = [T(30, 34, 'CPU: 8 cores, 8 VMs × 2 vCPUs', 15, 'start', bold=True), T(390, 34, 'Memory: 32 GB, 8 VMs × 4 GB', 15, 'start', bold=True)]
    for i in range(8):
        x, y = 30 + (i % 4) * 80, 52 + (i // 4) * 80
        o.append(R(x, y, 72, 70, PANEL, L2, 8))
        o.append(T(x + 36, y + 18, f'core {i + 1}', 13, fill=MUT))
        o.append(R(x + 8, y + 30, 26, 30, LVS, LV, 4)); o.append(R(x + 38, y + 30, 26, 30, LVS, LV, 4))
    o.append(R(390, 52, 300, 150, PANEL, INK, 8))
    for i in range(8):
        x, y = 396 + (i % 4) * 73, 58 + (i // 4) * 70
        o.append(boxt(x, y, 69, 66, [f'VM {i + 1}', '4 GB'], NXS, NX, 13, bold_first=True))
    o.append(T(30, 226, 'each small box is one vCPU: 2 share each core', 13, 'start', MUT))
    o.append(T(390, 226, 'no free space left in the 32 GB', 13, 'start', MUT))
    o.append(T(185, 262, '16 vCPUs ÷ 8 cores = 2.0', 15, bold=True))
    o.append(T(185, 286, 'above 1: oversubscribed', 15, bold=True, fill=LV))
    o.append(T(185, 308, 'the hypervisor time-slices them', 13, fill=MUT))
    o.append(T(540, 262, '32 GB ÷ 32 GB = 1.0', 15, bold=True))
    o.append(T(540, 286, 'exactly full, not over', 15, bold=True, fill=NX))
    o.append(T(540, 308, 'any overhead would force swapping', 13, fill=MUT))
    return 324, ''.join(o)
FIG[9] = (f9, 'The same 8 VMs seen two ways: 16 vCPUs must share 8 cores, a ratio of 2.0, so the CPU is oversubscribed; 8 × 4 GB fills the 32 GB of RAM exactly, a ratio of 1.0, so memory is full but not oversubscribed.',
          'Left, eight CPU cores each holding two vCPU chips. Right, a 32 GB memory box filled exactly by eight 4 GB virtual machines.')


spec = make_spec(FIG)
