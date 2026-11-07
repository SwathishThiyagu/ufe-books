"""Claude's hand-drawn figures for c-os-u2 (Operating Systems, unit 2: processes, threads, CPU scheduling), one per chapter,
from each chapter's worked example."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


# ---- 2.1 process states and the PCB ----
def f1():
    st = {'New': (20, 60, 100), 'Ready': (180, 60, 110), 'Running': (380, 60, 120), 'Terminated': (590, 60, 120), 'Waiting': (250, 230, 120)}
    o = []
    cx = lambda n: st[n][0] + st[n][2] / 2
    # muted moves
    o.append(L(120, 83, 176, 83, L2, 2, arrow='m')); o.append(T(148, 74, 'admit', 13, fill=MUT))
    o.append(L(500, 83, 586, 83, L2, 2, arrow='m')); o.append(T(543, 74, 'exit', 13, fill=MUT))
    o.append(f'<path d="M420,58 C400,14 270,14 250,56" style="fill:none;stroke:var(--line2);stroke-width:2" marker-end="url(#ar-UID-m)"/>')
    o.append(T(335, 26, 'timer: back to Ready', 13, fill=MUT))
    # highlighted path
    o.append(L(470, 108, 360, 226, LV, 3, arrow='l')); o.append(Tb(470, 170, '1  read() on slow SD card', 14, 'start', LV, True))
    o.append(L(270, 228, 230, 110, NX, 3, arrow='x')); o.append(Tb(236, 180, '2  card done', 14, 'end', NX, True))
    o.append(T(232, 198, '(interrupt)', 13, 'end', NX))
    o.append(L(290, 90, 376, 90, AC, 3, arrow='n')); o.append(T(335, 112, '3  dispatch', 13, fill=AC, bold=True))
    o.append(T(335, 128, 'when a core is free', 13, fill=AC))
    for n, (x, y, w) in st.items():
        hot = n in ('Running', 'Waiting', 'Ready')
        o.append(boxt(x, y, w, 46, [n], ACS if hot else PANEL, AC if hot else L2, 15, bold_first=hot))
    o.append(T(310, 300, 'Waiting never goes straight back to Running.', 13, fill=MUT))
    # PCB card
    o.append(R(450, 214, 250, 118, PANEL, INK, 8))
    o.append(T(575, 236, 'PCB of pid 1042', 14, bold=True))
    rows = [('state', 'Running → Waiting', LV), ('PC', 'saved: the next instruction', INK), ('SP', '0x7FF0 (saved)', INK), ('files', '3 open (unchanged)', MUT)]
    for i, (a, b, c) in enumerate(rows):
        o.append(T(462, 260 + i * 20, a, 13, 'start', MUT)); o.append(T(510, 260 + i * 20, b, 13, 'start', c, i == 0))
    return 340, ''.join(o)
FIG[1] = (f1, 'Process 1042 calls read() on a slow SD card: it moves Running → Waiting, the card\'s interrupt moves it to Ready, and only a later dispatch puts it back on a core. The PCB keeps the saved PC, SP and registers meanwhile.',
          'Five process states as boxes with the path Running to Waiting to Ready to Running numbered 1 to 3, and a card showing the PCB fields of process 1042.')


# ---- 2.2 cost of one context switch ----
def f2():
    x0, s = 60, 600 / 280
    tx = lambda ns: x0 + ns * s
    o = [T(x0, 36, 'One context switch = 40 + 200 + 40 = 280 ns', 15, 'start', bold=True)]
    o.append(boxt(tx(0), 52, 40 * s, 62, ['save', '8 × 5', '= 40 ns'], LVS, LV, 13, rx=4))
    o.append(boxt(tx(40), 52, 200 * s, 62, ['scheduler picks the next process', '200 ns'], ACS, AC, 14, rx=4))
    o.append(boxt(tx(240), 52, 40 * s, 62, ['restore', '8 × 5', '= 40 ns'], NXS, NX, 13, rx=4))
    o.append(T(tx(20), 136, 'old process', 13, fill=LV)); o.append(T(tx(260), 136, 'new process', 13, fill=NX))
    # zoom lines from the sliver on the slice bar
    o.append(P([(x0, 148), (x0, 246)], L2, 1.5, '4 4')); o.append(P([(tx(280), 148), (x0 + 3, 246)], L2, 1.5, '4 4'))
    o.append(Tb(440, 226, 'zoomed in: on the real scale the switch is a hairline', 13, fill=MUT))
    o.append(R(x0, 248, 600, 40, ACS, AC, 4))
    o.append(R(x0, 248, 3, 40, LV, LV, 0, 1))
    o.append(T(380, 273, 'one time slice: 5 ms = 5,000,000 ns', 14))
    o.append(T(380, 322, '280 ÷ 5,000,000 = 0.000056, which is 0.0056% of the slice', 15, bold=True, fill=AC))
    return 340, ''.join(o)
FIG[2] = (f2, 'One switch saves 8 registers (40 ns), runs the scheduler (200 ns) and restores 8 registers (40 ns): 280 ns in all. Against a 5 ms time slice that is only 0.0056%.',
          'A bar of 280 nanoseconds split into save 40, scheduler 200 and restore 40, zoomed out of a hairline on a 5 millisecond time-slice bar.')


# ---- 2.3 fork tree ----
def f3():
    xs, xe = [130, 230, 330], 430
    ry = lambda r: 66 + r * 34
    o = [T(60, 36, 'start', 13, fill=MUT)] + [T(x, 36, f'fork {i + 1}', 13, fill=MUT, bold=True) for i, x in enumerate(xs)]
    o += [L(x, 44, x, 320, LN, 1, '3 4') for x in xs]
    o.append(L(40, ry(0), xe, ry(0), INK, 2.5))
    lines = [(0, 4, 0), (0, 2, 1), (4, 6, 1), (0, 1, 2), (2, 3, 2), (4, 5, 2), (6, 7, 2)]
    for p, c, f in lines:
        x = xs[f]
        o.append(P([(x, ry(p)), (x + 24, ry(c)), (xe, ry(c))], AC, 2.5))
    for r in range(8):
        o.append(C(xe + 8, ry(r), 8, AC if r else INK))
    o.append(T(xe + 24, ry(0) + 5, 'original', 13, 'start', MUT))
    o.append(T(xe + 24, ry(4) + 5, 'first child', 13, 'start', MUT))
    o.append(T(240, 352, 'Each fork doubles: 1 → 2 → 4 → 8', 15, bold=True))
    o.append(T(240, 374, 'processes, so 7 are new children.', 15, bold=True))
    # second program
    o.append(R(500, 30, 210, 50, PANEL, LN, 8, 1))
    o.append(T(512, 51, 'pid = fork();', 13, 'start')); o.append(T(512, 70, 'if (pid == 0) fork();', 13, 'start'))
    o.append(boxt(520, 112, 64, 40, ['P'], PANEL, INK, 15, bold_first=True))
    o.append(boxt(620, 176, 76, 40, ['C1'], ACS, AC, 15, bold_first=True))
    o.append(boxt(620, 262, 76, 40, ['C2'], ACS, AC, 15, bold_first=True))
    o.append(L(584, 140, 618, 180, AC, 2, arrow='n'))
    o.append(L(658, 216, 658, 258, AC, 2, arrow='n'))
    o.append(T(552, 174, 'pid > 0:', 13, fill=MUT)); o.append(T(552, 190, 'skips the if', 13, fill=MUT))
    o.append(T(612, 240, 'pid == 0: forks', 13, 'end', MUT))
    o.append(T(610, 352, 'Total: P, C1, C2', 15, bold=True)); o.append(T(610, 374, '= 3 processes', 15, bold=True))
    return 390, ''.join(o)
FIG[3] = (f3, 'Left: three plain fork() calls double the processes each time, 1 → 2 → 4 → 8, so 7 are new. Right: with if (pid == 0) only the child forks again, giving 3 processes.',
          'Left, a branching diagram where one process line splits at each of three forks into eight lines. Right, a small tree from P to child C1 to grandchild C2.')


# ---- 2.4 pipe buffer fills and drains ----
def f4():
    o = []
    def pipe(y, title, used_x0, used_w, used_lab, read_w):
        o.append(T(30, y - 14, title, 15, 'start', bold=True))
        o.append(boxt(20, y, 92, 50, ['writer'], PANEL, AC, 14, bold_first=True))
        o.append(boxt(618, y, 92, 50, ['reader'], PANEL, AC, 14, bold_first=True))
        o.append(R(140, y - 4, 450, 58, PANEL, INK, 10))
        if read_w:
            o.append(boxt(530 - 0, y + 2, 56, 46, [''], NXS, NX, 13, rx=6, dash='5 4'))
        o.append(boxt(used_x0, y + 2, used_w, 46, used_lab, ACS, AC, 14, rx=6))
        o.append(boxt(146, y + 2, 34, 46, [''], NXS, NX, 13, rx=6, dash='5 4'))
        o.append(L(112, y + 25, 136, y + 25, AC, 2, arrow='n')); o.append(L(592, y + 25, 614, y + 25, AC, 2, arrow='n'))
    pipe(64, 'The buffer is nearly full', 184, 400, ['65 writes × 1,000 B = 65,000 B'], False)
    o.append(T(163, 140, '536 B free', 13, fill=NX, bold=True))
    o.append(boxt(20, 150, 150, 40, ['write 66: 1,000 B'], LVS, LV, 13, dash='6 4'))
    o.append(T(180, 175, '1,000 > 536, so the writer blocks and sleeps on the pipe', 14, 'start', LV, True))
    pipe(250, 'The reader takes 4,000 B', 184, 340, ['61,000 B still waiting'], True)
    o.append(T(163, 326, '536 B', 13, fill=NX, bold=True)); o.append(T(558, 326, '4,000 B', 13, fill=NX, bold=True))
    o.append(T(30, 360, 'Free = 536 + 4,000 = 4,536 B. 4,536 ≥ 1,000, so the kernel wakes the writer', 14, 'start'))
    o.append(T(30, 380, 'and write 66 goes in.', 14, 'start'))
    return 396, ''.join(o)
FIG[4] = (f4, 'The pipe holds 65,536 B: 65 writes of 1,000 B leave 536 B free, so write 66 blocks. When the reader takes 4,000 B, 4,536 B are free and the writer wakes. Boxes are not drawn to scale.',
          'Two pictures of a pipe between a writer and a reader: first almost full with a blocked 1,000-byte write outside, then with 4,000 bytes read out and 4,536 bytes free.')


# ---- 2.5 Amdahl: the serial part never shrinks ----
def f5():
    x0, s = 120, 4.4
    o = [R(x0, 22, 18, 14, LVS, LV, 3), T(x0 + 24, 34, 'serial 20% (cannot be split)', 13, 'start'),
         R(x0 + 230, 22, 18, 14, ACS, AC, 3), T(x0 + 254, 34, 'parallel 80% ÷ N', 13, 'start')]
    rows = [(1, '1 core'), (2, '2 cores'), (4, '4 cores'), (8, '8 cores'), (None, 'any N')]
    for i, (n, lab) in enumerate(rows):
        y = 58 + i * 50
        par = 80 / n if n else 0
        tot = 20 + par
        hot = n == 4
        o.append(T(x0 - 12, y + 23, lab, 14, 'end', bold=hot))
        o.append(R(x0, y, 20 * s, 34, LVS, LV, 4))
        if par:
            o.append(boxt(x0 + 20 * s, y, par * s, 34, [f'{par:g}'], ACS, AC, 13, rx=4))
        o.append(T(x0 + 10 * s, y + 22, '20', 13))
        sp = 100 / tot
        txt = f'time {tot:g} → speedup {round(sp, 2):g}' if n else 'time 20 → speedup 5, the limit'
        o.append(T(x0 + tot * s + 12, y + 22, txt, 14, 'start', AC if hot else INK, hot or not n))
    o.append(L(x0 + 20 * s, 50, x0 + 20 * s, 300, LV, 1.5, '4 4'))
    o.append(T(360, 334, '4 cores: 1 ÷ (0.20 + 0.80 ÷ 4) = 1 ÷ 0.40 = 2.5 times faster', 14, bold=True))
    o.append(T(360, 356, 'No number of cores beats 1 ÷ 0.20 = 5 times: the 20 never shrinks.', 14))
    return 372, ''.join(o)
FIG[5] = (f5, 'Run time out of 100 for the image filter as cores are added: the parallel 80 is divided by N but the serial 20 stays. With 4 cores the time is 40, a 2.5 times speedup, and no number of cores gets past 5 times.',
          'Five stacked bars for 1, 2, 4, 8 and unlimited cores, each with a fixed serial part of 20 and a parallel part of 80 divided by the number of cores.')


# ---- 2.6 FCFS vs preemptive SRTF ----
def f6():
    x0, s = 150, 44
    tx = lambda t: x0 + t * s
    o = []
    def chart(y, title, segs, avg):
        o.append(T(30, y - 44, title, 15, 'start', bold=True))
        for n, a, b in segs:
            o.append(boxt(tx(a), y, (b - a) * s, 38, [n], ACS if n == 'P1' else NXS, AC if n == 'P1' else NX, 14, bold_first=True, rx=4))
        o.append(xaxis(x0, tx(12), y + 44, sorted({t for _, a, b in segs for t in (a, b)} | {1}), tx))
        o.append(L(tx(1), y - 26, tx(1), y - 2, LV, 2, arrow='l'))
        o.append(T(tx(1) + 6, y - 18, 'P2 arrives (needs 4 ms)', 13, 'start', LV))
        o.append(T(30, y + 25, avg[0], 13, 'start', MUT)); o.append(T(30, y + 41, avg[1], 13, 'start', MUT))
        o.append(T(360, y + 92, avg[2], 14, bold=True))
    chart(84, '(a) FCFS, no preemption', [('P1', 0, 8), ('P2', 8, 12)], ('P2 waits', 'from 1 to 8', 'Average wait 3.5 ms · response 3.5 ms · turnaround 9.5 ms'))
    chart(280, '(b) SRTF, preemptive', [('P1', 0, 1), ('P2', 1, 5), ('P1', 5, 12)], ('P2 has 4 left,', 'P1 has 7 left', 'Average wait 2 ms · response 0 ms · turnaround 8 ms'))
    return 392, ''.join(o)
FIG[6] = (f6, 'The same two jobs scheduled two ways. Without preemption P2 waits from 1 ms to 8 ms; with SRTF the shorter P2 takes the CPU at 1 ms, so the average wait falls from 3.5 ms to 2 ms.',
          'Two Gantt charts from 0 to 12 ms: in the first P1 runs 0 to 8 and P2 8 to 12; in the second P1 runs 0 to 1, P2 1 to 5 and P1 5 to 12.')


# ---- 2.7 FCFS, SJF and RR on the same three jobs ----
def f7():
    x0, s = 150, 18
    tx = lambda t: x0 + t * s
    sty = {'P1': (ACS, AC), 'P2': (NXS, NX), 'P3': (LVS, LV)}
    charts = [('FCFS', 'average wait 17 ms', [('P1', 0, 24), ('P2', 24, 27), ('P3', 27, 30)]),
              ('SJF', 'average wait 3 ms', [('P2', 0, 3), ('P3', 3, 6), ('P1', 6, 30)]),
              ('RR, q = 4 ms', 'average wait 5.67 ms', [('P1', 0, 4), ('P2', 4, 7), ('P3', 7, 10)] + [('P1', t, t + 4) for t in range(10, 30, 4)])]
    o = []
    for i, (name, avg, segs) in enumerate(charts):
        y = 30 + i * 92
        o.append(T(138, y + 16, name, 15, 'end', bold=True)); o.append(T(138, y + 34, avg, 13, 'end', AC if i == 1 else MUT, i == 1))
        for n, a, b in segs:
            f, c = sty[n]
            o.append(boxt(tx(a), y, (b - a) * s, 38, [n], f, c, 13, rx=3))
        ticks = sorted({t for _, a, b in segs for t in (a, b)})
        o.append(xaxis(x0, tx(30), y + 42, ticks, tx))
    o.append(T(360, 316, 'Waits (P1, P2, P3): FCFS 0, 24, 27 · SJF 6, 0, 3 · RR 6, 4, 7 ms', 14))
    o.append(T(360, 338, 'Running the two short jobs first cuts the average wait the most.', 14, bold=True))
    return 354, ''.join(o)
FIG[7] = (f7, 'Jobs of 24, 3 and 3 ms, all arriving at 0, under three rules: FCFS makes the short jobs wait behind the long one (17 ms average), SJF runs them first (3 ms), and round robin with q = 4 ms sits between (17/3 ≈ 5.67 ms).',
          'Three Gantt charts from 0 to 30 ms for FCFS, shortest job first and round robin with a 4 ms quantum, each labelled with its average waiting time.')


# ---- 2.8 rate-monotonic schedule ----
def f8():
    x0, s = 90, 30
    tx = lambda t: x0 + t * s
    o = [T(360, 26, 'U = 1/4 + 2/5 = 0.65 ≤ 0.828, so the rate-monotonic test passes', 14, bold=True)]
    lanes = [('T1', 'p = 4, c = 1', 74, [(0, 1), (4, 5), (8, 9), (12, 13), (16, 17)], range(0, 20, 4), ACS, AC),
             ('T2', 'p = 5, c = 2', 164, [(1, 3), (5, 7), (10, 12), (15, 16), (17, 18)], range(0, 20, 5), NXS, NX)]
    for n, sub, y, jobs, rel, f, c in lanes:
        o.append(T(78, y + 16, n, 15, 'end', bold=True)); o.append(T(78, y + 32, sub, 13, 'end', MUT))
        o.append(R(x0, y, 20 * s, 38, PANEL, LN, 3, 1))
        for a, b in jobs:
            o.append(R(tx(a), y, (b - a) * s, 38, f, c, 3))
        for r in rel:
            o.append(L(tx(r), y - 22, tx(r), y - 3, MUT, 1.5, arrow='m'))
    o.append(T(tx(0) + 6, 60, 'release', 13, 'start', MUT))
    o.append(L(tx(16), 114, tx(16), 162, LV, 2, '4 3'))
    o.append(Tb(tx(16) - 6, 140, 'T1 preempts T2 at 16', 13, 'end', LV, True))
    o.append(T(tx(16.5), 230, 'resumes', 13, fill=NX))
    o.append(xaxis(x0, tx(20), 250, list(range(0, 21)), tx, 'time (ms)'))
    o.append(T(30, 328, 'T1 finishes at 1, 5, 9, 13, 17 (deadlines 4, 8, 12, 16, 20)', 14, 'start'))
    o.append(T(30, 350, 'T2 finishes at 3, 7, 12, 18 (deadlines 5, 10, 15, 20): no deadline missed', 14, 'start'))
    return 366, ''.join(o)
FIG[8] = (f8, 'T1 has the shorter period, so it always has priority. Over 20 ms every job of both tasks finishes before its deadline, including at 16 ms when T1 preempts T2.',
          'Two lanes from 0 to 20 ms: T1 runs for 1 ms after every 4 ms release, T2 runs 2 ms per 5 ms period and is interrupted by T1 at 16 ms.')


# ---- 2.9 CFS: real time vs virtual time ----
def f9():
    x0, s = 190, 25
    o = [T(30, 34, 'Real CPU time in one 24 ms window (slice = 24 × weight ÷ 1844)', 15, 'start', bold=True)]
    o.append(T(178, 75, 'A · nice 0', 14, 'end', bold=True)); o.append(T(178, 92, 'weight 1024', 13, 'end', MUT))
    o.append(boxt(x0, 56, 13.33 * s, 42, ['13.33 ms'], ACS, AC, 14))
    o.append(T(178, 129, 'B · nice 1', 14, 'end', bold=True)); o.append(T(178, 146, 'weight 820', 13, 'end', MUT))
    o.append(boxt(x0, 110, 10.67 * s, 42, ['10.67 ms'], NXS, NX, 14))
    o.append(T(x0 + 13.33 * s + 12, 82, 'A runs longer', 13, 'start', MUT))
    o.append(T(30, 200, 'Virtual time added (vruntime growth = slice × 1024 ÷ weight)', 15, 'start', bold=True))
    o.append(T(178, 240, 'A', 14, 'end', bold=True)); o.append(boxt(x0, 220, 13.33 * s, 42, ['13.33 × 1024 ÷ 1024'], ACS, AC, 14))
    o.append(T(178, 294, 'B', 14, 'end', bold=True)); o.append(boxt(x0, 274, 13.33 * s, 42, ['10.67 × 1024 ÷ 820'], NXS, NX, 14))
    o.append(L(x0 + 13.33 * s, 212, x0 + 13.33 * s, 324, INK, 1.5, '4 4'))
    o.append(T(x0 + 13.33 * s + 12, 262, 'both = 13.33 ms', 14, 'start', bold=True))
    o.append(T(x0 + 13.33 * s + 12, 280, 'level in the tree', 13, 'start', MUT))
    o.append(T(360, 352, 'B gets fewer real milliseconds but the same virtual progress, so neither starves.', 14))
    return 368, ''.join(o)
FIG[9] = (f9, 'In each 24 ms window CFS gives A (weight 1024) 13.33 ms and B (weight 820) 10.67 ms. Scaled by 1024 ÷ weight, both virtual runtimes grow by 13.33 ms, so the two stay level.',
          'Top, two bars of real CPU time, 13.33 ms for task A and 10.67 ms for task B. Bottom, two equal bars of virtual time, both 13.33 ms.')


spec = make_spec(FIG)
