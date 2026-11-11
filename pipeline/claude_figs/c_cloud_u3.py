"""Claude's hand-drawn figures for c-cloud-u3 (Cloud Computing, unit 3: virtualization), one per chapter, from each
chapter's worked example, plus the sentences in the chapter text that describe a figure (text_fixes)."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


def hbar(x, y, w, h, fill, c, label=None, size=13, fc=INK, bold=False):
    o = R(x, y, w, h, fill, c, 4, 2)
    if label: o += T(x + w / 2, y + h / 2 + size * 0.36, label, size, fill=fc, bold=bold)
    return o


def cells(x, y, n, cw, ch, fills, gap=4):
    """a row of n cells; fills[i] = (fill, stroke)"""
    return ''.join(R(x + i * (cw + gap), y, cw, ch, fills[i][0], fills[i][1], 4, 1.6) for i in range(n))


# ---- 3.1 five VMs on one host: limits, not reservations ----
def f1():
    o = [T(40, 26, 'Host: 16 cores, 64 GB RAM, running 5 VMs of 2 vCPU and 8 GB', 15, 'start', bold=True)]
    cw = 30
    o.append(T(40, 66, 'vCPU limits', 14, 'start', bold=True))
    fl = [(ACS, AC)] * 10 + [('var(--fig)', L2)] * 6
    o.append(cells(170, 46, 16, cw, 30, fl))
    for v in range(5):
        x = 170 + v * 2 * (cw + 4)
        o.append(T(x + cw + 2, 96, f'VM{v + 1}', 13, fill=MUT))
    o.append(T(170 + 10 * (cw + 4) + 3 * (cw + 4) - 2, 96, '6 free', 13, fill=MUT))
    o.append(T(40, 146, 'average work', 14, 'start', bold=True))
    fl2 = [(NXS, NX)] * 2 + [('var(--fig)', L2)] * 14
    o.append(cells(170, 126, 16, cw, 30, fl2))
    o.append(T(170, 178, '5 VMs × 20% of 2 vCPU = 2.0 cores busy, 2 ÷ 16 = 12.5% of the host', 13, 'start', bold=True))
    # RAM
    s = 500 / 64
    o.append(T(40, 236, 'RAM', 14, 'start', bold=True))
    for v in range(5):
        o.append(hbar(170 + v * 8 * s, 214, 8 * s, 34, ACS, AC, '8 GB', 13))
    o.append(hbar(170 + 40 * s, 214, 24 * s, 34, 'var(--fig)', L2, '24 GB free', 13))
    o.append(T(40, 290, 'Allocated: 10 vCPU and 40 GB. A vCPU count is a limit the hypervisor enforces, not a core', 14, 'start'))
    o.append(T(40, 310, 'locked away: the VMs leave most of the 16 cores idle.', 14, 'start'))
    return 326, ''.join(o)
FIG[1] = (f1, 'Five VMs take 10 vCPU and 40 GB as limits, leaving 6 vCPU and 24 GB unallocated; at 20% use they keep only about 2 of the 16 cores busy, 12.5% of the host.',
          'A row of 16 core cells with 10 marked as VM limits and 6 free, a second row with only 2 cells busy, and a RAM bar of five 8 GB blocks and 24 GB free.')


# ---- 3.2 four workloads, four implementation levels ----
def f2():
    o = []
    levels = [('application level', 'J: a Java program on the JVM', 'the JVM is a process that runs bytecode'),
              ('library level', 'W: a Windows program under WINE', 'Windows calls translated to Linux calls'),
              ('OS level', 'D: Docker containers', 'one shared Linux kernel, no guest OS'),
              ('hardware level', 'X: Xen, unmodified guest OS', 'guest boots on virtual hardware (full virtualization)')]
    y = 20
    fills = [ACS, LVS, NXS, ACS]
    strokes = [AC, LV, NX, AC]
    for (lv, wl, why), f, c in zip(levels, fills, strokes):
        o.append(R(40, y, 170, 60, f, c, 8))
        o.append(T(125, y + 36, lv, 14, bold=True))
        o.append(L(212, y + 30, 246, y + 30, c, 2, arrow='n'))
        o.append(R(250, y, 430, 60, PANEL, L2, 8, 1.5))
        o.append(T(266, y + 25, wl, 14, 'start', bold=True))
        o.append(T(266, y + 45, why, 13, 'start', MUT))
        y += 70
    o.append(R(40, y, 640, 34, 'var(--fig)', L2, 8, 1.5, '6 4'))
    o.append(T(360, y + 22, 'physical hardware', 14, fill=MUT, bold=True))
    o.append(T(40, y + 64, 'Ask where the virtual layer sits: under a guest OS, beside the kernel, under the library calls or under one program.', 13, 'start'))
    return y + 80, ''.join(o)
FIG[2] = (f2, 'Each workload sorted by where its virtual layer sits: the JVM at application level, WINE at library level, Docker at OS level, and Xen with an unmodified guest at hardware level with full virtualization.',
          'Four level boxes stacked above physical hardware, application, library, OS and hardware level, each pointing to the workload that uses it: JVM, WINE, Docker and Xen.')


# ---- 3.3 Type 1 and Type 2, with the 16 GB laptop ----
def f3():
    o = [T(150, 24, 'Type 1 (bare-metal)', 15, bold=True), T(510, 24, 'Type 2 (hosted): the 16 GB laptop', 15, bold=True)]
    # type 1
    o.append(R(40, 50, 100, 60, ACS, AC, 8)); o.append(T(90, 85, 'VM', 14, bold=True))
    o.append(R(160, 50, 100, 60, ACS, AC, 8)); o.append(T(210, 85, 'VM', 14, bold=True))
    o.append(boxt(40, 122, 220, 46, ['hypervisor (Xen, ESXi)'], LVS, LV, 14))
    o.append(boxt(40, 180, 220, 46, ['hardware'], PANEL, L2, 14))
    o.append(T(150, 254, 'no host OS in between', 13, fill=MUT))
    # type 2 with numbers, to scale
    x0, w = 360, 300
    s = 300 / 16
    y = 50
    o.append(R(x0, y, w, 60, 'none', LV, 8, 2, '6 4'))
    o.append(T(x0 + 150, y + 26, 'VM asks for 12 GB', 14, bold=True))
    o.append(T(x0 + 150, y + 46, 'only 11 GB free: 1 GB short', 14, fill=LV, bold=True))
    o.append(boxt(x0, 122, w, 46, ['Type 2 hypervisor: 1 GB'], LVS, LV, 14))
    o.append(boxt(x0, 180, w, 46, ['host OS: 4 GB'], NXS, NX, 14))
    o.append(boxt(x0, 238, w, 46, ['laptop hardware: 16 GB RAM'], PANEL, L2, 14))
    o.append(T(x0 + w + 10, 151, '16 − 4', 13, 'start', MUT)); o.append(T(x0 + w + 10, 169, '− 1 = 11', 13, 'start', MUT))
    o.append(T(40, 314, 'Type 2 pays twice before the VM starts: the host OS and the hypervisor both take RAM first.', 14, 'start', bold=True))
    o.append(T(40, 336, 'The 12 GB VM fits only with overcommit or ballooning.', 14, 'start'))
    return 352, ''.join(o)
FIG[3] = (f3, 'Left, a Type 1 hypervisor sits straight on the hardware. Right, on the laptop a Type 2 hypervisor sits on a host OS: 16 − 4 − 1 leaves 11 GB, so a 12 GB VM is 1 GB short.',
          'Two stacks: Type 1 with VMs on a hypervisor on hardware, and Type 2 with a VM on a hypervisor on a host OS on 16 GB laptop hardware, where the VM asking for 12 GB is 1 GB short.')


# ---- 3.4 full versus para-virtualization, 1,000 privileged operations ----
def f4():
    X0, X1 = 170, 650
    fx = lambda us: X0 + us / 2000 * (X1 - X0)
    o = [T(40, 26, 'Time for 1,000 privileged operations', 15, 'start', bold=True)]
    o.append(T(X0 - 12, 70, 'full', 14, 'end', bold=True))
    o.append(hbar(fx(0), 50, fx(2000) - fx(0), 34, LVS, LV, '1,000 traps × 2 μs = 2,000 μs', 13))
    o.append(T(X0 - 12, 128, 'para', 14, 'end', bold=True))
    o.append(hbar(fx(0), 108, fx(800) - fx(0), 34, NXS, NX, '800 hypercalls × 1 μs', 13))
    o.append(hbar(fx(800), 108, fx(1200) - fx(800), 34, LVS, LV, '200 × 2 μs', 13))
    o.append(T(fx(1200) + 8, 130, '1,200 μs', 14, 'start', bold=True))
    o.append(L(fx(1200), 152, fx(1200), 172, INK, 1.2)); o.append(L(fx(2000), 92, fx(2000), 172, INK, 1.2, '4 4'))
    o.append(L(fx(1200), 168, fx(2000), 168, INK, 2)); o.append(L(fx(1200), 162, fx(1200), 174, INK, 2)); o.append(L(fx(2000), 162, fx(2000), 174, INK, 2))
    o.append(T((fx(1200) + fx(2000)) / 2, 192, 'saved 800 μs = 40%', 14, bold=True))
    o.append(xaxis(X0, X1, 216, [0, 500, 1000, 1500, 2000], fx, 'microseconds', lambda v: f'{v:,}'))
    o.append(T(40, 282, 'The guest that cooperates (a changed kernel) swaps 80% of its traps for cheaper hypercalls.', 14, 'start'))
    return 300, ''.join(o)
FIG[4] = (f4, 'Full virtualization traps all 1,000 operations at 2 μs, 2,000 μs in all; para-virtualization turns 800 into 1 μs hypercalls and traps only 200, 1,200 μs, a saving of 800 μs or 40%.',
          'Two timing bars: a full-virtualization bar of 2,000 microseconds and a para-virtualization bar of 800 microseconds of hypercalls plus 400 of traps, with the 800 microsecond saving marked.')


# ---- 3.5 two-level address translation ----
def f5():
    o = []
    def addr(x, y, title, page, off, hexv, c, f):
        r = [T(x + 100, y - 10, title, 14, bold=True)]
        r.append(R(x, y, 120, 40, f, c, 6)); r.append(TM(x + 60, y + 26, page, 14, bold=True))
        r.append(R(x + 124, y, 76, 40, 'var(--fig)', L2, 6, 1.5)); r.append(TM(x + 162, y + 26, off, 14))
        r.append(TM(x + 100, y + 64, hexv, 15, bold=True))
        return ''.join(r)
    o.append(addr(20, 50, 'guest virtual', 'page 5', '0x2F0', '0x52F0', AC, ACS))
    o.append(addr(260, 50, 'guest physical', 'page 20', '0x2F0', '0x142F0', LV, LVS))
    o.append(addr(500, 50, 'machine', 'page 80', '0x2F0', '0x502F0', NX, NXS))
    o.append(L(142, 96, 258, 96, AC, 2, arrow='n')); o.append(L(382, 96, 498, 96, AC, 2, arrow='n'))
    o.append(boxt(150, 150, 150, 48, ['guest page table', '5 → 20'], PANEL, AC, 13))
    o.append(boxt(390, 150, 150, 48, ['hypervisor table', '20 → 80'], PANEL, AC, 13))
    o.append(L(225, 148, 200, 102, L2, 1.5, '4 4')); o.append(L(465, 148, 440, 102, L2, 1.5, '4 4'))
    o.append(T(40, 236, 'Only the page number is translated, twice; the offset 0x2F0 (low 12 bits of a 4 KB page) rides through.', 14, 'start'))
    o.append(T(40, 258, 'machine address = 80 × 0x1000 + 0x2F0 = 0x502F0 = 328432', 14, 'start', bold=True))
    return 276, ''.join(o)
FIG[5] = (f5, 'Guest virtual page 5 becomes guest physical page 20 through the guest’s own table, then machine page 80 through the hypervisor’s table; the offset 0x2F0 never changes, so the machine address is 0x502F0.',
          'Three addresses side by side, each split into page number and offset: page 5, page 20 and page 80, all with offset 0x2F0, linked by the guest page table and the hypervisor table.')


# ---- 3.6 the storage chain and the network chain ----
def f6():
    o = [T(40, 24, 'Storage: what the VM writes to, and what is really behind it', 14, 'start', bold=True)]
    y = 40
    o.append(boxt(40, y, 120, 54, ['VM', 'virtual disk'], ACS, AC, 13))
    o.append(L(162, y + 27, 194, y + 27, AC, 2, arrow='n'))
    o.append(boxt(198, y, 180, 54, ['12 thin volumes', '× 1.5 TB = 18 TB promised'], LVS, LV, 13))
    o.append(L(380, y + 27, 412, y + 27, AC, 2, arrow='n'))
    o.append(boxt(416, y, 264, 54, ['pool: 6 × 2 TB disks, RAID 5', 'usable (6 − 1) × 2 = 10 TB'], PANEL, L2, 13))
    s = 640 / 18
    yb = 116
    o.append(hbar(40, yb, 7.2 * s, 26, NXS, NX, 'real data 0.4 × 18 = 7.2 TB', 13))
    o.append(hbar(40 + 7.2 * s, yb, 2.8 * s, 26, 'var(--fig)', L2, '2.8 TB spare', 13))
    o.append(R(40 + 10 * s, yb, 8 * s, 26, 'none', LV, 4, 1.5, '5 4'))
    o.append(T(40 + 14 * s, yb + 18, 'promised, not there', 13, fill=LV, bold=True))
    o.append(T(40 + 10 * s, yb + 46, '10 TB', 13, fill=MUT)); o.append(T(680, yb + 46, '18 TB', 13, 'end', MUT))
    o.append(T(40, yb + 46, 'overprovision 18 ÷ 10 = 1.8', 13, 'start', bold=True))
    y = 214
    o.append(T(40, y, 'Network: twenty vNICs share one uplink', 14, 'start', bold=True))
    y += 16
    o.append(boxt(40, y, 120, 54, ['VM', 'vNIC'], ACS, AC, 13))
    o.append(L(162, y + 27, 194, y + 27, AC, 2, arrow='n'))
    o.append(boxt(198, y, 180, 54, ['20 vNICs', '× 1 Gb/s cap = 20 Gb/s'], LVS, LV, 13))
    o.append(L(380, y + 27, 412, y + 27, AC, 2, arrow='n'))
    o.append(boxt(416, y, 120, 54, ['vSwitch', 'VLAN / VXLAN'], PANEL, L2, 13))
    o.append(L(538, y + 27, 560, y + 27, AC, 2, arrow='n'))
    o.append(boxt(564, y, 116, 54, ['uplink NIC', '10 Gb/s'], PANEL, L2, 13))
    o.append(T(40, y + 84, 'contention 20 ÷ 10 = 2:1 if every VM sends at its cap at once', 13, 'start', bold=True))
    return y + 100, ''.join(o)
FIG[6] = (f6, 'Storage: 12 thin volumes promise 18 TB on a 10 TB RAID 5 pool (ratio 1.8), which works while real data is 7.2 TB. Network: 20 vNICs capped at 1 Gb/s share one 10 Gb/s uplink, 2:1 contention.',
          'Two chains: VM, virtual disk, thin volumes and a RAID 5 pool with a bar of real data against promised space; and VM, vNIC, vSwitch and a 10 Gb/s uplink.')


# ---- 3.7 ten copies: VM images against container layers ----
def f7():
    o = [T(40, 24, 'Image storage for 10 copies', 15, 'start', bold=True)]
    o.append(T(40, 56, '10 VMs', 14, 'start', bold=True))
    bw = 58
    for i in range(10):
        x = 40 + i * (bw + 6)
        o.append(R(x, 66, bw, 96, NXS, NX, 4, 1.5)); o.append(T(x + bw / 2, 118, '2 GB', 13))
        o.append(R(x, 66 + 96, bw, 24, ACS, AC, 4, 1.5)); o.append(T(x + bw / 2, 66 + 96 + 17, '0.5', 13))
    o.append(T(40 + 10 * (bw + 6) - 6, 212, '10 × (2 + 0.5) = 25 GB', 14, 'end', bold=True))
    o.append(T(40, 250, '10 containers', 14, 'start', bold=True))
    for i in range(10):
        x = 40 + i * (bw + 6)
        o.append(R(x, 260, bw, 24, ACS, AC, 4, 1.5)); o.append(T(x + bw / 2, 277, '0.5', 13))
    o.append(R(40, 288, 10 * (bw + 6) - 6, 10, LVS, LV, 3, 1.5))
    o.append(T(40, 318, 'one shared 0.1 GB base image', 13, 'start', LV, True))
    o.append(T(40 + 10 * (bw + 6) - 6, 318, '0.1 + 10 × 0.5 = 5.1 GB', 14, 'end', bold=True))
    o += [R(40, 342, 18, 14, NXS, NX, 3), T(66, 354, 'guest OS, one per VM', 13, 'start'),
          R(240, 342, 18, 14, ACS, AC, 3), T(266, 354, 'application layer', 13, 'start'),
          R(420, 342, 18, 14, LVS, LV, 3), T(446, 354, 'shared base', 13, 'start')]
    o.append(T(40, 384, 'Saving 25 − 5.1 = 19.9 GB, that is 79.6%: the guest OS copies are what the containers drop.', 14, 'start', bold=True))
    return 400, ''.join(o)
FIG[7] = (f7, 'Each VM stores its own 2 GB guest OS beside a 0.5 GB application, 25 GB for ten; the ten containers share one 0.1 GB base and add 0.5 GB each, 5.1 GB, a saving of 19.9 GB or 79.6%.',
          'Ten tall VM columns each with a 2 GB guest OS block and a 0.5 GB application block, above ten small container blocks of 0.5 GB sitting on one thin shared base image.')


# ---- 3.8 admission control for a virtual data centre ----
def f8():
    o = [T(40, 24, 'Tenant request against the whole building (50 hosts)', 15, 'start', bold=True)]
    s = 500 / 1200
    o.append(T(40, 68, 'CPU', 14, 'start', bold=True))
    o.append(hbar(140, 48, 1200 * s, 32, 'var(--fig)', L2))
    o.append(hbar(140, 48, 320 * s, 32, ACS, AC, '320 vCPU', 13, bold=True))
    o.append(T(140 + 500 + 8, 69, '1,200 cores', 13, 'start', MUT))
    o.append(T(140, 100, '20 × 16 = 320 of 50 × 24 = 1,200: 26.7%', 13, 'start'))
    s2 = 500 / 12800
    o.append(T(40, 148, 'RAM', 14, 'start', bold=True))
    o.append(hbar(140, 128, 12800 * s2, 32, 'var(--fig)', L2))
    o.append(hbar(140, 128, 1280 * s2, 32, NXS, NX)); o.append(T(140 + 1280 * s2 + 8, 149, '1,280 GB', 13, 'start', bold=True))
    o.append(T(140 + 500 + 8, 149, '12,800 GB', 13, 'start', MUT))
    o.append(T(140, 180, '20 × 64 = 1,280 of 50 × 256 = 12,800: 10.0%', 13, 'start'))
    o.append(R(140, 204, 300, 34, NXS, NX, 8))
    o.append(T(290, 226, 'admitted: both well under 100%', 14, bold=True))
    o.append(T(40, 270, 'Oversubscription R = 320 ÷ 1,200 = 0.27, below 1. The check is against the pool, not one host.', 14, 'start'))
    return 288, ''.join(o)
FIG[8] = (f8, 'The tenant’s 320 vCPU and 1,280 GB are weighed against the whole building’s 1,200 cores and 12,800 GB: 26.7% and 10.0%, so the virtual data centre is admitted with oversubscription 0.27.',
          'Two bars, CPU and RAM, each showing the requested share inside the data centre total: 320 of 1,200 cores and 1,280 of 12,800 GB, with an admitted verdict.')


# ---- 3.9 a Xen host: Dom0 counts too ----
def f9():
    o = [T(40, 24, 'Xen host: 32 cores, 128 GB RAM', 15, 'start', bold=True)]
    cw = 16
    fl = [(LVS, LV)] * 2 + [(ACS, AC)] * 24 + [('var(--fig)', L2)] * 6
    o.append(T(40, 66, 'cores', 14, 'start', bold=True))
    o.append(cells(110, 48, 32, cw, 28, fl, 2.5))
    o.append(T(110 + 18, 96, 'Dom0 2', 13, fill=LV, bold=True))
    for g in range(6):
        x = 110 + (2 + g * 4) * (cw + 2.5)
        o.append(L(x + 1, 82, x + 4 * (cw + 2.5) - 3, 82, AC, 2))
    o.append(T(110 + 14 * (cw + 2.5), 100, '6 DomU × 4 = 24', 13, fill=AC, bold=True))
    o.append(T(110 + 29 * (cw + 2.5), 100, '6 free', 13, bold=True))
    s = 560 / 128
    o.append(T(40, 152, 'RAM', 14, 'start', bold=True))
    o.append(hbar(110, 132, 4 * s, 32, LVS, LV))
    for g in range(6):
        o.append(hbar(110 + (4 + g * 8) * s, 132, 8 * s, 32, ACS, AC, '8', 13))
    o.append(hbar(110 + 52 * s, 132, 76 * s, 32, 'var(--fig)', L2, '76 GB free', 13))
    o.append(T(110, 184, 'Dom0 4 GB', 13, 'start', LV, True))
    o.append(T(40, 222, 'Allocated: 2 + 24 = 26 vCPU and 4 + 48 = 52 GB; free: 6 cores and 76 GB.', 14, 'start', bold=True))
    o.append(T(40, 244, 'Dom0 is the control domain, but its vCPU and RAM come out of the same host.', 14, 'start'))
    return 262, ''.join(o)
FIG[9] = (f9, 'Dom0 takes 2 cores and 4 GB, the six DomU guests 24 cores and 48 GB; the host has 26 vCPU and 52 GB allocated and 6 cores and 76 GB free.',
          'A row of 32 core cells, 2 for Dom0, 24 for six DomU guests and 6 free, above a RAM bar with Dom0’s 4 GB, six 8 GB blocks and 76 GB free.')


spec = make_spec(FIG)


def text_fixes(k):
    return {
        7: [('A Type 1 hypervisor sits directly on hardware; a Type 2 hypervisor runs as a program on a host OS, as in the figure.',
             'A Type 1 hypervisor sits directly on hardware; a Type 2 hypervisor runs as a program on a host OS (Figure 3.3.1 draws both).')],
    }.get(k, [])
