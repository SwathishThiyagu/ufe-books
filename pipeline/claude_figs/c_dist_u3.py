"""Claude's hand-drawn figures for c-dist-u3 (Parallel and Distributed Computing, unit 3: OpenMP, MPI, CUDA and OpenCL),
one per chapter, from each chapter's worked example, plus the sentences that describe a figure (text_fixes)."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def cell(x, y, w, h, s, f=PANEL, st=L2, size=14, bold=True, mono=False):
    t = TM if mono else T
    return R(x, y, w, h, f, st, 5) + t(x + w / 2, y + h / 2 + size * 0.36, s, size, bold=bold)


# ---- 3.1 OpenMP fork, private partial sums, join ----
def f1():
    o = [boxt(20, 14, 200, 36, ['serial: S = 0'], PANEL, L2, 14)]
    o.append(T(234, 37, '#pragma omp parallel for reduction(+:S) num_threads(4)', 12, 'start', MUT))
    rng = ['1 … 250,000', '250,001 … 500,000', '500,001 … 750,000', '750,001 … 1,000,000']
    ps = ['31,250,125,000', '93,750,125,000', '156,250,125,000', '218,750,125,000']
    for t in range(4):
        x = 20 + t * 172
        o.append(L(120, 52, x + 80, 84, AC, 2, arrow='n'))
        o.append(R(x, 88, 160, 112, ACS, AC, 8))
        o.append(T(x + 80, 110, f'thread {t}', 14, bold=True))
        o.append(T(x + 80, 132, rng[t], 13))
        o.append(T(x + 80, 160, 'private S =', 13, fill=MUT))
        o.append(T(x + 80, 182, ps[t], 13, bold=True))
        o.append(L(x + 80, 202, 360, 236, LV, 2, arrow='l'))
    o.append(boxt(200, 240, 320, 40, ['join: S = 500,000,500,000'], LVS, LV, 15))
    o.append(T(20, 316, 'Without reduction, a shared total races:', 14, 'start', bold=True))
    o.append(T(20, 340, 'both threads load total = 100, each adds its i, both store: one addition is lost.', 14, 'start', NX))
    return 356, ''.join(o)
FIG[1] = (f1, 'At the parallel for the team forks into 4 threads; the static schedule gives each a block of 250,000 numbers and a private S. The join adds the four partial sums into 500,000,500,000.',
          'Serial code forks into four threads, each summing a quarter of 1 to one million into its own private sum, and the four sums join into S equal to 500,000,500,000.')


# ---- 3.2 MPI scatter and reduce ----
def f2():
    o = [T(20, 24, 'rank 0 (root) holds A', 14, 'start', bold=True)]
    for i, v in enumerate(range(1, 9)):
        o.append(cell(20 + i * 40, 34, 36, 32, str(v), ACS if i < 4 else LVS, AC if i < 4 else LV))
    o.append(T(360, 56, 'MPI_Scatter, count 4', 13, 'start', MUT))
    o.append(L(96, 70, 150, 116, AC, 2, arrow='n')); o.append(L(256, 70, 470, 116, LV, 2, arrow='l'))
    for r, (x, vals, s, f, st) in enumerate([(60, [1, 2, 3, 4], 10, ACS, AC), (400, [5, 6, 7, 8], 26, LVS, LV)]):
        o.append(R(x, 120, 260, 104, PANEL, st, 8))
        o.append(T(x + 130, 142, f'rank {r}', 14, bold=True))
        for i, v in enumerate(vals): o.append(cell(x + 32 + i * 50, 152, 44, 30, str(v), f, st))
        o.append(T(x + 130, 210, f'local sum = {" + ".join(map(str, vals))} = {s}', 13))
    o.append(L(190, 226, 340, 266, AC, 2, arrow='n')); o.append(L(530, 226, 380, 266, LV, 2, arrow='l'))
    o.append(T(470, 254, 'MPI_Reduce, MPI_SUM', 13, 'start', MUT))
    o.append(boxt(250, 270, 220, 40, ['rank 0: 10 + 26 = 36'], NXS, NX, 15))
    return 322, ''.join(o)
FIG[2] = (f2, 'Rank 0 scatters the eight values four each, keeping [1, 2, 3, 4] and sending [5, 6, 7, 8] to rank 1. Each rank sums its own part, 10 and 26, and MPI_Reduce adds them to 36 at rank 0.',
          'Array 1 to 8 on rank 0 split into two halves sent to rank 0 and rank 1, each computing a local sum, which are reduced to 36 at rank 0.')


# ---- 3.3 grid, block, thread: global index ----
def f3():
    o = [R(14, 14, 692, 196, PANEL, L2, 10), T(30, 38, 'grid: add&lt;&lt;&lt;2, 4&gt;&gt;&gt;  (gridDim.x = 2 blocks, blockDim.x = 4 threads)', 14, 'start', bold=True)]
    for b in range(2):
        x = 34 + b * 340
        o.append(R(x, 54, 312, 140, ACS, AC, 8))
        o.append(T(x + 156, 76, f'block {b}  (blockIdx.x = {b})', 14, bold=True))
        for t in range(4):
            tid = b * 4 + t
            hot = tid == 5
            o.append(R(x + 12 + t * 74, 92, 66, 88, NXS if hot else PANEL, NX if hot else AC, 6))
            o.append(T(x + 45 + t * 74, 116, f'thread {t}', 13))
            o.append(T(x + 45 + t * 74, 142, f'tid {tid}', 15, bold=True, fill=NX if hot else INK))
            o.append(T(x + 45 + t * 74, 166, f'{b}×4+{t}', 12, fill=MUT))
    o.append(T(30, 244, 'tid = blockIdx.x × blockDim.x + threadIdx.x', 15, 'start', bold=True))
    o.append(T(30, 270, 'threadIdx.x restarts at 0 in every block, so block 1, thread 1 is tid = 1 × 4 + 1 = 5', 14, 'start'))
    o.append(T(30, 294, 'tid 5 computes C[5] = A[5] + B[5] = 11 + 3 = 14', 14, 'start', NX, bold=True))
    return 310, ''.join(o)
FIG[3] = (f3, 'A launch of 2 blocks of 4 threads makes a grid of 8 threads. threadIdx.x restarts at 0 in each block, so thread 1 of block 1 has global index 1 × 4 + 1 = 5 and computes C[5] = 11 + 3 = 14.',
          'A grid box holding block 0 and block 1, each with four threads labelled with their global index 0 to 7; thread 1 of block 1, index 5, is highlighted.')


# ---- 3.4 one thread per element ----
def f4():
    A = [2, 3, 5, 7, 11, 13, 17, 19]; B = [1, 1, 2, 2, 3, 3, 4, 4]
    x0, w = 120, 72
    o = []
    o.append(R(x0 - 4, 14, 4 * w, 30, ACS, AC, 6)); o.append(T(x0 - 4 + 2 * w, 34, 'block 0', 13, bold=True))
    o.append(R(x0 - 4 + 4 * w, 14, 4 * w, 30, LVS, LV, 6)); o.append(T(x0 - 4 + 6 * w, 34, 'block 1', 13, bold=True))
    rows = [('thread t', [str(i % 4) for i in range(8)]), ('i = b×4 + t', [str(i) for i in range(8)]),
            ('A[i]', list(map(str, A))), ('B[i]', list(map(str, B))), ('C[i]', [str(a + b) for a, b in zip(A, B)])]
    for r, (lab, vals) in enumerate(rows):
        y = 56 + r * 42
        o.append(T(x0 - 12, y + 22, lab, 13, 'end', MUT if r < 2 else INK, bold=r >= 2))
        for i, v in enumerate(vals):
            hot = i == 5
            f = NXS if hot else (PANEL if r < 4 else ACS)
            o.append(cell(x0 + i * w, y, w - 6, 32, v, f, NX if hot else (L2 if r < 4 else AC), 14, bold=r >= 1))
        if r == 3: o.append(L(x0 - 6, y + 38, x0 + 8 * w - 6, y + 38, INK, 1.5))
    o.append(T(20, 290, 'Each column is one thread. Thread 1 of block 1: i = 1 × 4 + 1 = 5, C[5] = 13 + 3 = 16.', 14, 'start'))
    o.append(T(20, 314, 'Every i from 0 to 7 is used once: C = [3, 4, 7, 9, 14, 16, 21, 23].', 14, 'start', bold=True))
    return 330, ''.join(o)
FIG[4] = (f4, 'Each column is one thread of the 2 × 4 launch, and it adds one pair of elements. The marked column is thread 1 of block 1: i = 1 × 4 + 1 = 5, so it writes C[5] = 13 + 3 = 16.',
          'A table of eight thread columns grouped into two blocks, with rows for thread number, global index, A, B and the sum C; column 5 is highlighted.')


# ---- 3.5 shared-memory reduction in a block ----
def f5():
    o = []
    states = [('after load', [3, 1, 4, 2], ()), ('after step 1', [4, 6, 4, 2], (0, 1)), ('after step 2', [10, 6, 4, 2], (0,))]
    ys = [40, 150, 260]
    x0, w = 200, 70
    for k, (lab, vals, hot) in enumerate(states):
        y = ys[k]
        o.append(T(x0 - 14, y + 23, lab, 14, 'end', bold=True))
        o.append(T(x0 + 2 * w - 4, y - 10, '&#95;&#95;shared&#95;&#95; int s[4]', 12, fill=MUT) if k == 0 else '')
        for i, v in enumerate(vals):
            f = NXS if (k == 2 and i == 0) else (ACS if i in hot else PANEL)
            o.append(cell(x0 + i * w, y, w - 8, 34, str(v), f, NX if (k == 2 and i == 0) else (AC if i in hot else L2), 15))
    # step 1 arrows
    c = lambda i: x0 + i * w + (w - 8) / 2
    o.append(L(c(0), 76, c(0) - 4, 146, AC, 2, arrow='n')); o.append(L(c(1), 76, c(0) + 6, 146, AC, 2, arrow='n'))
    o.append(L(c(2), 76, c(1) + 4, 146, AC, 2, arrow='n')); o.append(L(c(3), 76, c(1) + 12, 146, AC, 2, arrow='n'))
    o.append(T(c(3) + 50, 116, 'thread 0: 3 + 1 = 4', 13, 'start')); o.append(T(c(3) + 50, 134, 'thread 1: 4 + 2 = 6', 13, 'start'))
    o.append(L(c(0), 186, c(0) - 4, 256, NX, 2, arrow='x')); o.append(L(c(1), 186, c(0) + 6, 256, NX, 2, arrow='x'))
    o.append(T(c(3) + 50, 232, 'thread 0: 4 + 6 = 10', 13, 'start'))
    for y in (92, 202):
        o.append(L(30, y, 480, y, LV, 2, '6 4')); o.append(T(30, y - 6, '&#95;&#95;syncthreads()', 12, 'start', LV))
    o.append(T(20, 322, 'Each barrier makes every write visible before any thread reads it. Final sum = 10.', 14, 'start'))
    return 336, ''.join(o)
FIG[5] = (f5, 'The block loads x into shared memory, waits at __syncthreads(), then threads 0 and 1 add pairs to get [4, 6, 4, 2]. After a second barrier thread 0 adds 4 + 6, leaving the sum 10 in s[0].',
          'The shared array s shown three times: 3 1 4 2 after loading, 4 6 4 2 after the first pair sums, and 10 in the first cell after the last step, with barriers between.')


# ---- 3.6 copies dominate: copy every time vs keep on device ----
def f6():
    fx = lambda t: 150 + t * 54
    o = [T(20, 24, 'N = 1,000,000 floats = 4 MB; one copy at 10 GB/s = 0.4 ms; kernel = 0.2 ms', 14, 'start', bold=True)]

    def seq(y, segs):
        r = []; t = 0
        for d, kind in segs:
            f, st = {'c': (LVS, LV), 'k': (ACS, AC)}[kind]
            r.append(R(fx(t), y, fx(t + d) - fx(t) - 0.6, 28, f, st, 2, 1.2)); t += d
        return ''.join(r), t
    o.append(T(140, 62, 'one iteration', 13, 'end'))
    s, t = seq(44, [(0.4, 'c'), (0.2, 'k'), (0.4, 'c')]); o.append(s)
    o.append(T(fx(0.2), 63, 'in', 12)); o.append(T(fx(0.8), 63, 'out', 12))
    o.append(T(fx(1.0) + 8, 64, '0.4 + 0.2 + 0.4 = 1.0 ms (kernel only 20 %)', 13, 'start'))
    o.append(T(140, 120, '10 iterations,', 13, 'end')); o.append(T(140, 136, 'copy every time', 13, 'end'))
    s, t = seq(104, [(0.4, 'c'), (0.2, 'k'), (0.4, 'c')] * 10); o.append(s)
    o.append(T(fx(10), 152, '10 × 1.0 = 10.0 ms', 14, 'end', bold=True))
    o.append(T(140, 196, '10 iterations,', 13, 'end')); o.append(T(140, 212, 'data stays on GPU', 13, 'end'))
    s, t = seq(182, [(0.4, 'c')] + [(0.2, 'k')] * 10 + [(0.4, 'c')]); o.append(s)
    o.append(T(fx(2.8) + 8, 202, '0.4 + 10 × 0.2 + 0.4 = 2.8 ms', 14, 'start', LV, bold=True))
    o.append(xaxis(fx(0), fx(10), 236, list(range(0, 11)), fx, 'time (ms)'))
    o += [R(150, 300, 22, 14, LVS, LV, 2, 1.2), T(178, 312, 'copy (host ↔ device)', 13, 'start'),
          R(360, 300, 22, 14, ACS, AC, 2, 1.2), T(388, 312, 'kernel', 13, 'start')]
    return 326, ''.join(o)
FIG[6] = (f6, 'One iteration spends 0.8 ms of its 1.0 ms copying, so copying in and out every time makes 10 iterations cost 10.0 ms. Keeping the array on the device pays the two 0.4 ms copies once and finishes in 2.8 ms.',
          'Three timelines of copies and kernels: one iteration of 1 millisecond, ten iterations copying each time ending at 10 milliseconds, and ten kernels between a single copy in and out ending at 2.8 milliseconds.')


# ---- 3.7 OpenCL NDRange ----
def f7():
    A = [1, 2, 3, 4, 5, 6, 7, 8]
    x0, w = 150, 68
    o = [T(20, 24, 'NDRange: global size 8, local size 4 → 8 ÷ 4 = 2 work-groups', 15, 'start', bold=True)]
    o.append(R(x0 - 4, 40, 4 * w, 28, ACS, AC, 6)); o.append(T(x0 - 4 + 2 * w, 59, 'work-group 0', 13, bold=True))
    o.append(R(x0 - 4 + 4 * w, 40, 4 * w, 28, LVS, LV, 6)); o.append(T(x0 - 4 + 6 * w, 59, 'work-group 1', 13, bold=True))
    rows = [('get_global_id(0)', [str(i) for i in range(8)]), ('get_local_id(0)', [str(i % 4) for i in range(8)]),
            ('A[i]', list(map(str, A))), ('B[i]', ['10'] * 8), ('C[i] = A + B', [str(a + 10) for a in A])]
    for r, (lab, vals) in enumerate(rows):
        y = 80 + r * 40
        o.append(T(x0 - 12, y + 21, lab, 13, 'end', INK if r != 1 else MUT, bold=r in (0, 4)))
        for i, v in enumerate(vals):
            hot = i == 6
            o.append(cell(x0 + i * w, y, w - 6, 30, v, NXS if hot else (ACS if r == 4 else PANEL), NX if hot else (AC if r == 4 else L2), 14, bold=r != 1))
    o.append(T(20, 300, 'Work-item 6 is in group 1 at local id 2: C[6] = 7 + 10 = 17. The last global id is 8 − 1 = 7.', 14, 'start'))
    o.append(T(20, 322, 'CUDA names the same things grid, block and thread.', 13, 'start', MUT))
    return 336, ''.join(o)
FIG[7] = (f7, 'Global size 8 with local size 4 gives 2 work-groups of 4. Each work-item has a global id 0 to 7 and a local id 0 to 3 inside its group; work-item 6 (group 1, local id 2) computes C[6] = 7 + 10 = 17.',
          'A table of eight work-item columns split into two work-groups, with rows for global id, local id, A, B and C; work-item 6 is highlighted with C equal to 17.')


TEXT = {
    3: [('A grid is all blocks from one kernel launch. The figure shows the three levels.',
         'A grid is all blocks from one kernel launch. The figure shows a grid of 2 blocks with 4 threads each.')],
}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}


def text_fixes(k):
    return TEXT.get(k, [])
