"""Claude's hand-drawn figures for c-cloud-u4 (Cloud Computing, unit 4: cloud storage, GFS and HDFS, BigTable and
NoSQL, provisioning, scheduling, fault tolerance, energy, pricing and federation), one per chapter, from each chapter's
worked example."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def hbar(x, y, w, h, fill, c, label=None, size=13, fc=INK, bold=False):
    o = R(x, y, w, h, fill, c, 4, 2)
    if label: o += T(x + w / 2, y + h / 2 + size * 0.36, label, size, fill=fc, bold=bold)
    return o


# ---- 4.1 three copies against RS(6,3) ----
def f1():
    s = 560 / 1800
    o = [T(40, 26, 'Raw disk for 600 GB of photos', 15, 'start', bold=True)]
    o.append(T(40, 62, 'replication r = 3', 14, 'start', bold=True))
    for i in range(3):
        o.append(hbar(40 + i * 600 * s, 72, 600 * s, 36, ACS, AC, f'copy {i + 1}: 600 GB', 13))
    o.append(T(40 + 1800 * s - 4, 128, '600 × 3 = 1,800 GB → ₹2,700 a month', 14, 'end', bold=True))
    o.append(T(40, 170, 'erasure coding RS(6,3)', 14, 'start', bold=True))
    for i in range(9):
        par = i >= 6
        o.append(hbar(40 + i * 100 * s, 180, 100 * s, 36, LVS if par else NXS, LV if par else NX, ('p' if par else 'd') + str(i - 5 if par else i + 1), 13))
    o.append(T(40 + 900 * s + 10, 204, '9 × 100 GB = 900 GB', 14, 'start', bold=True))
    o.append(T(40 + 900 * s + 10, 226, '→ ₹1,350 a month', 14, 'start', bold=True))
    o.append(T(40, 238, '6 data fragments d1–d6 of 100 GB', 13, 'start', NX))
    o.append(T(40, 256, '+ 3 parity fragments p1–p3', 13, 'start', LV))
    o.append(T(40, 296, 'Storage factor: 3 for replication, (6 + 3) ÷ 6 = 1.5 for RS(6,3). Any 6 of the 9 rebuild the data.', 14, 'start'))
    o.append(T(40, 320, 'Saving ₹2,700 − ₹1,350 = ₹1,350 a month at ₹1.5 per GB-month.', 14, 'start', bold=True))
    return 338, ''.join(o)
FIG[1] = (f1, 'Three full copies of 600 GB take 1,800 GB and ₹2,700 a month; RS(6,3) cuts the data into 6 fragments of 100 GB and adds 3 parity fragments, 900 GB and ₹1,350 a month.',
          'Two bars to scale: three 600 GB copies making 1,800 GB, and nine 100 GB fragments, six data and three parity, making 900 GB.')


# ---- 4.2 an HDFS write: metadata in the NameNode, bytes along the pipeline ----
def f2():
    o = [T(40, 24, 'A 1,024 MB file in HDFS (128 MB blocks, 3 replicas)', 15, 'start', bold=True)]
    for i in range(8):
        o.append(hbar(40 + i * 80, 38, 76, 30, ACS if i else NXS, AC if i else NX, f'b{i}', 13, bold=(i == 0)))
    o.append(T(40, 88, '1,024 ÷ 128 = 8 blocks; 8 × 3 = 24 replicas on DataNodes', 13, 'start', MUT))
    o.append(boxt(40, 108, 220, 64, ['NameNode: 9 entries', '/f + b0 … b7 and where they are'], PANEL, LV, 13))
    o.append(boxt(40, 220, 100, 44, ['client'], PANEL, AC, 14))
    o.append(L(90, 218, 120, 176, LV, 1.5, '4 4', arrow='l')); o.append(Tb(160, 202, 'where?', 13, 'middle', LV))
    xs = [230, 380, 530]
    for j, x in enumerate(xs):
        o.append(boxt(x, 220, 120, 44, [f'DataNode {j + 1}'], NXS, NX, 14))
    o.append(L(142, 236, 226, 236, AC, 2.5, arrow='n')); o.append(L(352, 236, 376, 236, AC, 2.5, arrow='n')); o.append(L(502, 236, 526, 236, AC, 2.5, arrow='n'))
    o.append(L(376, 252, 352, 252, NX, 1.6, '4 3', arrow='x')); o.append(L(526, 252, 502, 252, NX, 1.6, '4 3', arrow='x')); o.append(L(226, 252, 142, 252, NX, 1.6, '4 3', arrow='x'))
    o.append(T(410, 290, 'block b0’s 128 MB flows 1 → 2 → 3; the ack returns 3 → 2 → 1', 13, 'middle', MUT))
    o.append(T(40, 330, 'No block byte passes through the NameNode: it answers only with locations.', 14, 'start', bold=True))
    o.append(T(40, 354, 'GFS, 64 MB chunks: 1,024 ÷ 64 = 16 chunks, 48 replicas, 16 + 1 = 17 master entries.', 14, 'start'))
    return 372, ''.join(o)
FIG[2] = (f2, 'The file becomes 8 blocks of 128 MB; the NameNode holds just 9 entries (the file plus 8 blocks) and gives locations, while each block’s bytes flow client → DataNode 1 → 2 → 3. With 64 MB GFS chunks the counts are 16, 48 and 17.',
          'A file bar cut into eight blocks, a NameNode box with nine entries, and a write pipeline from client through three DataNodes with acknowledgements returning the other way.')


# ---- 4.3 a BigTable cell with versions ----
def f3():
    o = [T(40, 24, 'Row com.cnn.www', 15, 'start', bold=True)]
    # contents versions
    o.append(T(160, 54, 'contents:', 14, bold=True))
    vers = [('t6', 'newest', LVS, LV), ('t5', 'returned', NXS, NX), ('t3', 'oldest', PANEL, L2)]
    for i, (t, note, f, c) in enumerate(vers):
        y = 68 + i * 44
        o.append(R(80 + i * 8, y, 180, 36, f, c, 6))
        o.append(TM(110 + i * 8, y + 23, t, 14, bold=True))
        o.append(T(190 + i * 8, y + 23, 'page text', 13, fill=MUT))
        o.append(T(272 + i * 8, y + 23, note, 13, 'start', c if c != L2 else MUT, True))
    o.append(T(470, 54, 'anchor columns: 2', 14, bold=True))
    o.append(boxt(380, 68, 180, 36, ['anchor:cnnsi.com @ t3'], PANEL, AC, 13))
    o.append(boxt(380, 112, 180, 36, ['anchor:my.look.ca @ t6'], PANEL, AC, 13))
    # timeline
    X0, X1 = 80, 640
    fx = lambda t: X0 + (t - 2) / 5 * (X1 - X0)
    y = 236
    o.append(L(X0, y, X1, y, L2, 2))
    for t in (3, 5, 6):
        o.append(C(fx(t), y, 6, NX if t == 5 else (LV if t == 6 else L2))); o.append(T(fx(t), y + 24, f't{t}', 13, bold=True))
    o.append(L(fx(5.5), y - 26, fx(5.5), y + 8, INK, 2.5)); o.append(T(fx(5.5), y - 32, 'read at t5.5', 13, bold=True))
    o.append(R(X0, y - 10, fx(5.5) - X0, 20, NXS, 'none', 4, 0))
    o.append(L(X0, y, X1, y, L2, 2))
    for t in (3, 5, 6):
        o.append(C(fx(t), y, 6, NX if t == 5 else (LV if t == 6 else L2)))
    o.append(T(X0, y + 52, 'Candidates are the versions at or before t5.5 (t3, t5); the newest, t5, is returned.', 13, 'start'))
    o.append(T(X0, y + 72, 't6 is newer than the read time, so this read does not see it.', 13, 'start'))
    o.append(T(X0, y + 98, 'Reversed key: com.cnn.www sorts every cnn.com page together, so one range scan reads them.', 13, 'start'))
    return y + 114, ''.join(o)
FIG[3] = (f3, 'The row has 3 contents versions and 2 anchor columns. A read at t5.5 looks only at versions at or before t5.5 and returns the newest, t5; the t6 version is not visible to it.',
          'A stack of three timestamped versions of the contents cell, t6, t5 and t3, beside two anchor columns, above a timeline where a read at t5.5 picks t5.')


# ---- 4.4 two hosts: where the 12 idle vCPU go ----
def f4():
    o = [T(40, 24, '10 VMs of 2 vCPU on hosts of 16 vCPU (20% kept for the hypervisor)', 15, 'start', bold=True)]
    u = 34
    def host(y, nvm, title, gap_lab, gap):
        r = [T(40, y + 26, title, 14, 'start', bold=True)]
        x = 140
        for i in range(nvm):
            r.append(hbar(x, y, 2 * u, 40, ACS, AC, 'VM', 13)); x += 2 * u
        r.append(hbar(x, y, gap * u, 40, 'var(--fig)', L2, gap_lab, 13)); x += gap * u
        r.append(hbar(x, y, 3.2 * u, 40, LVS, LV, 'reserve 3.2', 13))
        return ''.join(r)
    o.append(host(50, 6, 'host 1', '0.8', 0.8))
    o.append(T(140 + 12 * u + 0.4 * u, 112, 'stranded', 13, fill=MUT, bold=True))
    o.append(host(130, 4, 'host 2', '4.8 unused', 4.8))
    o.append(T(40, 250, 'CPU limit ⌊12.8 ÷ 2⌋ = 6 VMs, RAM limit ⌊64 ÷ 8⌋ = 8 VMs: the smaller, 6, wins. 10 VMs need 2 hosts.', 13, 'start'))
    o.append(T(40, 274, 'Allocated 20 of 32 vCPU = 62.5%. Idle 12 = 6.4 reserve + 0.8 stranded + 4.8 unused.', 14, 'start', bold=True))
    o.append(xaxis(140, 140 + 16 * u, 180, [0, 4, 8, 12, 16], lambda v: 140 + v * u, 'vCPU on one host'))
    return 292, ''.join(o)
FIG[4] = (f4, 'CPU allows 6 VMs per host and RAM 8, so 6 wins and 10 VMs take 2 hosts. Of the 32 vCPU, 20 are allocated (62.5%); the 12 idle are 6.4 reserve, 0.8 stranded on host 1 and 4.8 unused on host 2.',
          'Two host bars of 16 vCPU: host 1 with six 2-vCPU VMs, 0.8 stranded and a 3.2 reserve; host 2 with four VMs, 4.8 unused and a 3.2 reserve.')


# ---- 4.5 FCFS against SJF ----
def f5():
    X0, X1 = 110, 540
    fx = lambda t: X0 + t / 5 * (X1 - X0)
    o = [T(40, 24, 'Three cloudlets on one 1,000 MIPS VM (all arrive at 0)', 15, 'start', bold=True)]
    jobs = {'P1': (3, LVS, LV), 'P2': (0.6, NXS, NX), 'P3': (1.2, ACS, AC)}
    def lane(y, title, order, waits):
        r = [T(X0 - 12, y + 24, title, 14, 'end', bold=True)]
        t = 0
        for j in order:
            d, f, c = jobs[j]
            r.append(hbar(fx(t), y, fx(d) - fx(0), 36, f, c, j if d < 1 else f'{j} {d:g} s', 13)); t += d
        r.append(T(fx(4.8) + 10, y + 16, 'waits ' + waits[0], 13, 'start'))
        r.append(T(fx(4.8) + 10, y + 34, 'avg ' + waits[1], 13, 'start', bold=True))
        return ''.join(r)
    o.append(lane(50, 'FCFS', ['P1', 'P2', 'P3'], ('0, 3, 3.6', '2.2 s')))
    o.append(lane(120, 'SJF', ['P2', 'P3', 'P1'], ('0, 0.6, 1.8', '0.8 s')))
    o.append(xaxis(X0, fx(5), 180, [0, 1, 2, 3, 4, 4.8], fx, 'seconds', lambda v: f'{v:g}'))
    o.append(L(fx(4.8), 44, fx(4.8), 176, INK, 1.5, '5 4'))
    o.append(T(40, 250, 'Run time = MI ÷ MIPS: 3,000 → 3 s, 600 → 0.6 s, 1,200 → 1.2 s. Same makespan 4.8 s either way;', 13, 'start'))
    o.append(T(40, 270, 'putting the short jobs first cuts the average wait from 2.2 s to 0.8 s.', 13, 'start', bold=True))
    return 288, ''.join(o)
FIG[5] = (f5, 'FCFS runs the 3 s job first, so the others wait 3 s and 3.6 s (average 2.2 s); SJF runs 0.6 s and 1.2 s first (average 0.8 s). Both end at 4.8 s.',
          'Two Gantt lanes: FCFS with P1 3 s, P2 0.6 s, P3 1.2 s, and SJF with P2, P3, then P1, both ending at 4.8 seconds.')


# ---- 4.6 RPO, RTO and the snapshot interval ----
def f6():
    X0, X1 = 80, 660
    fx = lambda m: X0 + m / 130 * (X1 - X0)
    o = [T(40, 24, 'A crash at minute 59: how much data is lost, how soon it is back', 15, 'start', bold=True)]
    def row(y, title, step, c):
        r = [T(40, y - 8, title, 13, 'start', bold=True), L(X0, y + 10, fx(130), y + 10, L2, 1.5)]
        for m in range(0, 130, step):
            r.append(L(fx(m), y, fx(m), y + 20, c, 3))
        return ''.join(r)
    o.append(row(60, 'hourly snapshot', 60, LV))
    o.append(R(fx(0), 64, fx(59) - fx(0), 12, LVS, LV, 3, 1.5))
    o.append(T(fx(57), 100, 'lost up to 60 min = 4 × the RPO', 13, 'end', LV, True))
    o.append(row(140, 'snapshot or log ship every 15 min', 15, NX))
    o.append(R(fx(45), 144, fx(59) - fx(45), 12, NXS, NX, 3, 1.5))
    o.append(T(fx(57), 180, '≤ 15 min lost: RPO met', 13, 'end', NX, True))
    o.append(L(fx(59), 36, fx(59), 200, INK, 2.5)); o.append(Tb(fx(59), 212, 'crash', 13, bold=True))
    o.append(L(fx(59), 230, fx(119), 230, AC, 2.5, arrow='n')); o.append(T(fx(89), 250, 'RTO: service back within 60 min', 13, fill=AC, bold=True))
    o.append(xaxis(X0, fx(130), 266, [0, 15, 30, 45, 60, 75, 90, 105, 120], fx, 'minutes'))
    o.append(T(40, 330, 'Downtime allowed in a 43,200-minute month: 99.9% → 43.2 min, 99.99% → 4.32 min.', 14, 'start', bold=True))
    return 346, ''.join(o)
FIG[6] = (f6, 'With hourly snapshots a crash just before the next one loses up to 60 minutes of data, four times the 15-minute RPO; snapshots every 15 minutes keep the loss under the RPO. The 1-hour RTO is a separate clock for getting service back.',
          'Two timelines of snapshot ticks, hourly and every 15 minutes, with a crash at minute 59 showing the data lost in each, and an arrow for the 60-minute recovery time.')


# ---- 4.7 the idle floor and consolidation ----
def f7():
    X0, X1, Y0, Y1 = 70, 360, 60, 300
    fx = lambda u: X0 + u * (X1 - X0)
    fy = lambda p: Y1 - p / 400 * (Y1 - Y0)
    o = [axes(X0, X1, Y0, Y1, [0, 0.25, 0.5, 0.75, 1], [0, 100, 200, 300, 400], fx, fy, 'utilisation u', 'power per server (W)', lambda v: f'{v:g}')]
    o.append(R(fx(0), fy(200), fx(1) - fx(0), fy(0) - fy(200), 'var(--line)', 'none', 0, 0))
    o.append(Tb(fx(0.5), fy(100), 'idle floor 200 W', 13, bold=True))
    o.append(P([(fx(0), fy(200)), (fx(1), fy(400))], AC, 3))
    o.append(C(fx(0.3), fy(260), 6, LV)); o.append(C(fx(0.75), fy(350), 6, NX))
    o.append(Tb(fx(0.3) - 6, fy(260) - 14, '0.3 → 260 W', 13, 'end', LV, True))
    o.append(Tb(fx(0.75) + 4, fy(350) + 26, '0.75 → 350 W', 13, 'start', NX, True))
    o.append(T(fx(0.5), 30, 'P = 200 + 200u', 14, bold=True))
    # bars
    bx = 420
    o.append(T(bx, 50, 'Monthly facility energy (PUE 1.5)', 14, 'start', bold=True))
    s = 260 / 28470
    o.append(T(bx, 82, '100 servers at 0.3: 26 kW', 13, 'start'))
    o.append(hbar(bx, 90, 28470 * s, 30, LVS, LV, '28,470 kWh', 13, bold=True))
    o.append(T(bx, 146, '40 servers at 0.75: 14 kW', 13, 'start'))
    o.append(hbar(bx, 154, 15330 * s, 30, NXS, NX, '15,330 kWh', 13, bold=True))
    o.append(T(bx, 214, '₹2,27,760 → ₹1,22,640', 14, 'start', bold=True))
    o.append(T(bx, 236, '46.15% less for the same work', 14, 'start', bold=True))
    o.append(T(bx, 268, 'Fewer, busier servers pay the', 13, 'start', MUT))
    o.append(T(bx, 286, '200 W floor fewer times.', 13, 'start', MUT))
    return 350, ''.join(o)
FIG[7] = (f7, 'Each server draws 200 W even idle, so at 30% load it takes 260 W. Moving the work from 100 servers at 0.3 to 40 at 0.75 cuts facility energy from 28,470 to 15,330 kWh a month, 46.15% less.',
          'A line of power against utilisation starting at a 200 watt floor with points at 0.3 and 0.75, beside two energy bars of 28,470 and 15,330 kilowatt-hours.')


# ---- 4.8 three pricing schemes, one month ----
def f8():
    s = 480 / 9410
    o = [T(40, 24, '2 VMs for 730 hours, 200 GB stored, 50 GB sent out', 15, 'start', bold=True)]
    rows = [('on-demand', '₹6/VM-h', 8760, '₹9,410'), ('reserved', '₹4/VM-h', 5840, '₹6,490'), ('spot', '₹2.1/VM-h', 3066, '₹3,716')]
    y = 50
    for name, rate, comp, tot in rows:
        o.append(T(40, y + 18, name, 14, 'start', bold=True)); o.append(T(40, y + 36, rate, 13, 'start', MUT))
        o.append(hbar(140, y, comp * s, 40, ACS, AC, f'compute ₹{comp:,}', 13))
        o.append(hbar(140 + comp * s, y, 400 * s, 40, NXS, NX))
        o.append(hbar(140 + (comp + 400) * s, y, 250 * s, 40, LVS, LV))
        o.append(T(140 + (comp + 650) * s + 8, y + 26, tot, 15, 'start', bold=True))
        y += 62
    o += [R(140, y + 4, 18, 14, NXS, NX, 3), T(166, y + 16, 'storage 200 × ₹2 = ₹400', 13, 'start'),
          R(390, y + 4, 18, 14, LVS, LV, 3), T(416, y + 16, 'egress 50 × ₹5 = ₹250', 13, 'start')]
    o.append(T(40, y + 50, 'Reserved saves ₹9,410 − ₹6,490 = ₹2,920 (31.03%). Spot is cheapest but the VMs can be reclaimed.', 14, 'start', bold=True))
    return y + 66, ''.join(o)
FIG[8] = (f8, 'Only the compute line changes between schemes: ₹8,760 on demand, ₹5,840 reserved and ₹3,066 spot, while storage (₹400) and egress (₹250) stay. Reserved saves ₹2,920 a month, 31.03%.',
          'Three stacked bars, on-demand, reserved and spot, each with a compute block of shrinking size and the same small storage and egress blocks, totalling ₹9,410, ₹6,490 and ₹3,716.')


# ---- 4.9 the broker checks delay before price ----
def f9():
    o = [T(40, 24, 'Cricket final: 300 VMs needed for 4 hours, 100 owned in cloud A', 15, 'start', bold=True)]
    o.append(boxt(40, 50, 170, 60, ['site in cloud A', 'rent 300 − 100 = 200'], PANEL, AC, 13))
    o.append(L(212, 80, 262, 80, AC, 2, arrow='n'))
    o.append(boxt(266, 50, 120, 60, ['broker'], ACS, AC, 15))
    o.append(L(388, 70, 446, 56, AC, 2, arrow='n')); o.append(L(388, 90, 446, 136, AC, 2, arrow='n'))
    o.append(R(450, 30, 230, 64, NXS, NX, 8))
    o.append(T(466, 54, 'cloud B: ₹5 per VM-hour', 14, 'start', bold=True)); o.append(T(466, 78, '200 × 5 × 4 = ₹4,000', 13, 'start'))
    o.append(R(450, 110, 230, 64, LVS, LV, 8))
    o.append(T(466, 134, 'cloud C: ₹4.5 per VM-hour', 14, 'start', bold=True)); o.append(T(466, 158, '200 × 4.5 × 4 = ₹3,600', 13, 'start'))
    # delay check
    X0, X1 = 140, 620
    fx = lambda ms: X0 + ms / 250 * (X1 - X0)
    y = 220
    o.append(T(40, y - 10, 'Added delay against the 150 ms budget', 14, 'start', bold=True))
    o.append(T(X0 - 10, y + 22, 'B', 14, 'end', bold=True)); o.append(hbar(fx(0), y + 6, 4, 26, NXS, NX)); o.append(T(fx(0) + 12, y + 24, '≈ 0 ms: passes', 13, 'start', NX, True))
    o.append(T(X0 - 10, y + 62, 'C', 14, 'end', bold=True)); o.append(hbar(fx(0), y + 46, fx(200) - fx(0), 26, LVS, LV)); o.append(T(fx(75), y + 64, 'adds 200 ms', 13))
    o.append(T(fx(200) + 8, y + 64, 'fails', 13, 'start', LV, True))
    o.append(L(fx(150), y - 2, fx(150), y + 80, INK, 2, '6 4')); o.append(Tb(fx(150), y + 96, '150 ms budget', 13, bold=True))
    o.append(T(40, y + 132, 'C is ₹400 (10%) cheaper but too slow, so the interactive load goes to B for ₹4,000;', 14, 'start', bold=True))
    o.append(T(40, y + 154, 'only delay-tolerant batch work could move to C.', 14, 'start'))
    return y + 170, ''.join(o)
FIG[9] = (f9, 'The site rents 200 VMs through the broker. Cloud C is ₹400 cheaper (₹3,600 against ₹4,000) but adds 200 ms, over the 150 ms budget, so the interactive load goes to cloud B.',
          'A site sends its request for 200 VMs to a broker, which compares cloud B at ₹4,000 and cloud C at ₹3,600; a delay bar shows C at 200 ms crossing the 150 ms budget.')


spec = make_spec(FIG)


def text_fixes(k):
    return []
