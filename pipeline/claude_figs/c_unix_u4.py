"""Claude's hand-drawn figures for c-unix-u4 (Linux and Shell Programming, unit 4: processes and system administration),
one per chapter, from each chapter's worked example. chapter_fix also corrects 4.7: the old archive was named
www-20261030, which is 7 days before 20261106, not the 8 days the example and its demo use; it becomes www-20261029."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *
import unix_text

FIG = {}
AFTER = {}


def arrow_for(c):
    return {LV: 'l', NX: 'x', L2: 'm'}.get(c, 'n')


# ---- 4.1 PID 4242 from start to gone ----
def f1():
    o = [T(20, 28, 'sleep 300 &  →  [1] 4242', 15, 'start', bold=True)]
    o.append(R(20, 48, 200, 60, PANEL, AC, 8)); o.append(T(120, 72, 'shell', 14, bold=True)); o.append(T(120, 94, 'PID 4100', 14, fill=AC, bold=True))
    o.append(L(120, 108, 120, 140, AC, 2, arrow='n')); o.append(T(130, 130, 'parent of', 13, 'start', MUT))
    o.append(R(20, 144, 200, 84, ACS, AC, 8)); o.append(T(120, 168, 'sleep 300', 14, bold=True))
    o.append(T(120, 190, 'PID 4242   PPID 4100', 13)); o.append(T(120, 212, 'STAT S (waiting on a timer)', 13, fill=AC))
    # timeline
    x0, y = 260, 186
    o.append(L(x0, y, 700, y, L2, 2, arrow='m'))
    pts = [(300, 'running', 'STAT S', AC), (440, 'kill -TERM 4242', 'signal 15', LV), (560, 'exits', 'STAT Z, briefly', MUT), (660, 'reaped', 'no row', MUT)]
    for x, a, b, c in pts:
        o.append(C(x, y, 7, c))
        o.append(T(x, y - 34, a, 13, fill=c if c != MUT else INK, bold=True))
        o.append(T(x, y - 16, b, 13, fill=MUT))
    o.append(L(222, 186, 292, 186, AC, 2))
    o.append(R(370, 230, 330, 64, FIGBG, NX, 8, 1.5, '6 4'))
    o.append(T(535, 254, 'only if still alive after 5 s:', 13, fill=NX))
    o.append(TM(535, 278, 'kill -KILL 4242  (signal 9)', 13, fill=NX, bold=True))
    o.append(L(440, 196, 440, 228, NX, 1.6, '4 3', arrow='x'))
    o.append(T(360, 322, 'Try SIGTERM first so the program can clean up; SIGKILL cannot be caught.', 14, fill=MUT))
    return 338, ''.join(o)
FIG[1] = (f1, 'The shell (PID 4100) starts sleep 300 as PID 4242 in state S. SIGTERM ends it; it may show STAT Z for a moment until the shell collects it, then ps shows no row. SIGKILL is only the fallback after 5 s.',
          'A shell box with PID 4100 above a sleep box with PID 4242, PPID 4100 and STAT S, and a time line: running, kill -TERM 4242, exits with a brief Z state, reaped with no row; a dashed box gives kill -KILL 4242 as the fallback.')


# ---- 4.2 which file passwd -l changes ----
def f2():
    o = [T(20, 28, 'passwd -l ravi changes one file; id ravi reads the other two', 15, 'start', bold=True)]
    files = [('/etc/passwd', 'ravi:x:1500:2000::/home/ravi:/bin/bash', AC, PANEL),
             ('/etc/group', 'students:x:2000:   project:x:2001:ravi', AC, PANEL),
             ('/etc/shadow', 'ravi:!$6$...hash...:...', NX, NXS)]
    for i, (n, line, c, f) in enumerate(files):
        y = 52 + i * 82
        o.append(R(250, y, 450, 62, f, c, 8, 2))
        o.append(TM(264, y + 24, n, 14, 'start', c, True))
        o.append(TM(264, y + 48, line, 13, 'start'))
    o.append(R(20, 66, 150, 120, LVS, LV, 8)); o.append(TM(95, 96, 'id ravi', 14, bold=True))
    o.append(T(95, 122, 'reads passwd', 13)); o.append(T(95, 142, 'and group', 13))
    o.append(T(95, 168, 'same output', 13, fill=LV, bold=True))
    o.append(L(172, 100, 246, 84, LV, 2, arrow='l')); o.append(L(172, 140, 246, 160, LV, 2, arrow='l'))
    o.append(R(20, 224, 150, 60, NXS, NX, 8)); o.append(TM(95, 250, 'passwd -l ravi', 13, bold=True))
    o.append(T(95, 272, 'adds ! to the hash', 13, fill=NX))
    o.append(L(172, 254, 246, 254, NX, 2, arrow='x'))
    o.append(R(20, 304, 680, 44, FIGBG, L2, 6, 1.2))
    o.append(TM(360, 331, 'uid=1500(ravi) gid=2000(students) groups=2000(students),2001(project)', 13))
    o.append(T(360, 368, 'before and after locking: the lock stops password logins, not the identity', 13, fill=MUT))
    return 384, ''.join(o)
FIG[2] = (f2, 'passwd -l ravi puts ! in front of the hash in /etc/shadow only. id ravi reads /etc/passwd and /etc/group, so it prints the same line before and after the lock.',
          'Three file boxes, /etc/passwd, /etc/group and /etc/shadow. id ravi has arrows to the first two; passwd -l ravi has an arrow to /etc/shadow. Below, the id output line that stays the same.')


# ---- 4.3 45 waiting packages, 12 upgraded ----
def f3():
    o = [T(20, 28, 'apt update, then apt upgrade -y: 45 packages were waiting', 15, 'start', bold=True)]
    x0, y0, s = 40, 56, 30
    for i in range(45):
        r, c = divmod(i, 15)
        up = i < 12
        o.append(R(x0 + c * s, y0 + r * s, s - 6, s - 6, LVS if up else PANEL, LV if up else L2, 3, 1.6 if up else 1.2))
    o.append(R(x0 + 15 * s + 16, y0, s - 6, s - 6, ACS, AC, 3, 2))
    o.append(T(x0 + 15 * s + 50, y0 + 17, 'new kernel', 13, 'start', AC, True))
    o.append(T(x0 + 15 * s + 50, y0 + 35, '(not one of the 45)', 13, 'start', MUT))
    y = y0 + 3 * s + 22
    o.append(R(40, y - 12, 16, 16, LVS, LV, 3)); o.append(T(64, y + 1, '12 upgraded', 14, 'start', LV, True))
    o.append(R(200, y - 12, 16, 16, PANEL, L2, 3)); o.append(T(224, y + 1, '45 − 12 = 33 still not upgraded', 14, 'start', bold=True))
    o.append(T(40, y + 28, 'changes made by the upgrade: 12 + 1 new kernel = 13', 14, 'start', AC, True))
    o.append(T(40, y + 52, 'apt update only refreshed the package lists; it changed none of the 45.', 13, 'start', MUT))
    y2 = y + 78
    o.append(R(40, y2, 300, 58, PANEL, AC, 8)); o.append(TM(190, y2 + 24, 'apt remove nginx', 14, bold=True))
    o.append(T(190, y2 + 46, 'program gone, /etc/nginx kept', 13))
    o.append(R(380, y2, 300, 58, NXS, NX, 8)); o.append(TM(530, y2 + 24, 'apt purge nginx', 14, bold=True))
    o.append(T(530, y2 + 46, 'program and /etc/nginx gone', 13, fill=NX))
    return y2 + 72, ''.join(o)
FIG[3] = (f3, 'Of the 45 waiting packages, 12 were upgraded and 33 were not; the run also added 1 new kernel, so it made 13 changes. apt remove keeps /etc/nginx, apt purge deletes it.',
          'A grid of 45 squares with 12 shaded as upgraded and 33 plain, one extra square for the new kernel, and two boxes below contrasting apt remove nginx, which keeps /etc/nginx, with apt purge nginx, which deletes it.')


# ---- 4.4 four is-active readings ----
def f4():
    o = [T(20, 28, 'systemctl is-active nginx after each stage', 15, 'start', bold=True)]
    st = [('before', None, 'inactive', 'no process'), ('systemctl start', 'start', 'active', 'Main PID 812'),
          ('systemctl restart', 'restart', 'active', 'Main PID 947'), ('systemctl stop', 'stop', 'inactive', 'no process')]
    w = 160
    for i, (a, cmd, r, pid) in enumerate(st):
        x = 20 + i * 173
        act = r == 'active'
        c = LV if act else L2
        o.append(T(x + w / 2, 66, f'stage {i + 1}', 13, fill=MUT))
        o.append(TM(x + w / 2, 88, a, 13, bold=True))
        o.append(R(x, 102, w, 92, LVS if act else PANEL, c, 8, 2))
        o.append(TM(x + w / 2, 140, r, 16, fill=LV if act else MUT, bold=True))
        o.append(T(x + w / 2, 170, pid, 13))
        if i < 3: o.append(L(x + w + 2, 148, x + 171, 148, L2, 2, arrow='m'))
    o.append(T(20 + 2 * 173 + w / 2, 214, 'new process: 812 → 947', 13, fill=NX, bold=True))
    o.append(T(360, 250, 'readings: inactive, active, active, inactive  →  2 active, 2 inactive', 14, bold=True))
    return 266, ''.join(o)
FIG[4] = (f4, 'The four readings are inactive, active, active and inactive: 2 active and 2 inactive. Start gives Main PID 812; restart replaces it with a new process, PID 947.',
          'Four stage boxes left to right: before, inactive; after start, active with Main PID 812; after restart, active with Main PID 947; after stop, inactive.')


# ---- 4.5 two networks and a gateway ----
def f5():
    o = [T(20, 28, 'Laptop 192.168.1.10/24 pings across to 10.0.0.0/24', 15, 'start', bold=True)]
    o.append(R(20, 50, 300, 200, FIGBG, AC, 10, 1.5, '6 4'))
    o.append(T(36, 72, 'network 192.168.1.0/24', 13, 'start', AC, True))
    o.append(T(36, 92, '32 − 24 = 8 host bits: 2⁸ − 2 = 254 hosts', 13, 'start', MUT))
    o.append(boxt(40, 112, 150, 56, ['laptop', '192.168.1.10'], ACS, AC, 13, True))
    o.append(boxt(170, 184, 140, 56, ['gateway', '192.168.1.1'], LVS, LV, 13, True))
    o.append(L(140, 168, 196, 182, AC, 2, arrow='n'))
    o.append(R(400, 50, 300, 200, FIGBG, NX, 10, 1.5, '6 4'))
    o.append(T(416, 72, 'network 10.0.0.0/24', 13, 'start', NX, True))
    o.append(boxt(430, 100, 180, 56, ['file server', '10.0.0.5'], NXS, NX, 13, True))
    o.append(R(430, 176, 180, 56, PANEL, L2, 8, 1.5, '5 4'))
    o.append(T(520, 200, '10.0.0.99', 13, bold=True)); o.append(T(520, 220, 'no such host', 13, fill=MUT))
    o.append(L(312, 204, 426, 134, LV, 2.5, arrow='l'))
    o.append(L(312, 220, 424, 206, L2, 2, '6 4', arrow='m'))
    o.append(T(20, 278, 'ping 10.0.0.5: 4 sent, 4 back, 0% loss. ping 10.0.0.99: Destination Host Unreachable.', 13, 'start', LV, True))
    o.append(T(20, 300, 'Different /24 networks, so the laptop sends to its default gateway 192.168.1.1.', 13, 'start'))
    o.append(TM(20, 326, 'sudo mount -t nfs 10.0.0.5:/data /mnt/data', 13, 'start', bold=True))
    o.append(TM(20, 350, 'scp student@10.0.0.5:/data/report.pdf .', 13, 'start', bold=True))
    return 366, ''.join(o)
FIG[5] = (f5, 'The laptop and the file server sit on different /24 networks, so the ping goes through gateway 192.168.1.1 and gets 4 of 4 replies. The failure for 10.0.0.99 says nothing about 10.0.0.5.',
          'Two dashed network regions. On 192.168.1.0/24 the laptop sends to gateway 192.168.1.1, which forwards to the file server 10.0.0.5 on 10.0.0.0/24 with 0 percent loss; a dashed arrow to 10.0.0.99 is unreachable.')


# ---- 4.6 container on the host kernel, guest with its own ----
def f6():
    o = [T(20, 28, 'One host, two ways to run a web server', 15, 'start', bold=True)]
    o.append(R(20, 296, 680, 40, PANEL, L2, 6)); o.append(T(360, 321, 'hardware (VT-x on)', 14, bold=True))
    o.append(R(20, 246, 680, 42, ACS, AC, 6)); o.append(T(360, 272, 'host Linux kernel', 14, bold=True))
    # container
    o.append(R(40, 60, 300, 176, FIGBG, LV, 8, 1.5, '6 4'))
    o.append(T(190, 82, 'Docker container "web"', 14, fill=LV, bold=True))
    o.append(boxt(70, 96, 240, 50, ['nginx process tree', 'image web:v1'], LVS, LV, 13))
    o.append(T(190, 172, 'host port 8080 → port 80', 13))
    o.append(T(190, 196, 'no kernel of its own', 13, fill=LV, bold=True))
    o.append(L(190, 206, 190, 244, LV, 2.5, arrow='l'))
    # vm
    o.append(R(380, 60, 300, 176, FIGBG, NX, 8, 1.5, '6 4'))
    o.append(T(530, 82, 'KVM guest "webvm"', 14, fill=NX, bold=True))
    o.append(boxt(410, 96, 240, 40, ['web server'], PANEL, NX, 13))
    o.append(boxt(410, 142, 240, 40, ['guest kernel (its own)'], NXS, NX, 13))
    o.append(T(530, 204, '2 vCPUs · 2048 MB RAM · 10 GB disk', 13))
    o.append(L(530, 214, 530, 244, NX, 2, arrow='x'))
    return 346, ''.join(o)
FIG[6] = (f6, 'The container web is a process tree on the host kernel, reached at host port 8080 forwarded to port 80. The guest webvm boots its own kernel on 2 vCPUs with 2048 MB of RAM and a 10 GB disk.',
          'A hardware layer and a host kernel layer. On the left a container box with the nginx process tree and port 8080 to 80, arrow straight into the host kernel. On the right a KVM guest box with its own guest kernel, 2 vCPUs, 2048 MB and 10 GB.')


# ---- 4.7 the 7-day cut-off ----
def f7():
    o = [T(20, 28, 'cron runs backup.py at 02:00 on 6 Nov 2026', 15, 'start', bold=True)]
    x0, x1 = 60, 680
    fx = lambda d: x0 + (d + 9) / 9.5 * (x1 - x0)  # d = days before now (negative)
    y = 150
    o.append(L(x0, y, x1, y, L2, 2))
    for d in range(-9, 1):
        o.append(L(fx(d), y, fx(d), y + 6, L2, 1.5))
        o.append(T(fx(d), y + 24, '6 Nov' if d == 0 else f'{6 + d} Nov' if 6 + d > 0 else f'{31 + 6 + d} Oct', 13, fill=MUT))
    o.append(R(fx(-7), 54, fx(0) - fx(-7), 90, LVS, LV, 4, 1))
    o.append(T((fx(-7) + fx(0)) / 2, 74, 'kept: 7 days or newer', 13, fill=LV, bold=True))
    o.append(L(fx(-7), 46, fx(-7), y, NX, 2.5, '6 4'))
    o.append(T(fx(-7) - 6, 60, 'cut-off', 13, 'end', NX, True)); o.append(T(fx(-7) - 6, 78, '7 × 86,400 s', 13, 'end', NX))
    o.append(C(fx(0), y, 8, LV)); o.append(TM(fx(0) - 8, 116, 'www-20261106', 13, 'end', LV, True))
    o.append(T(fx(0) - 8, 134, 'new archive, tar rc 0', 13, 'end'))
    o.append(C(fx(-8), y, 8, NX)); o.append(L(fx(-8) - 9, y - 9, fx(-8) + 9, y + 9, NX, 2.5)); o.append(L(fx(-8) - 9, y + 9, fx(-8) + 9, y - 9, NX, 2.5))
    o.append(TM(fx(-8), 206, 'www-20261029', 13, 'middle', NX, True))
    o.append(T(fx(-8), 226, '8 days old: deleted', 13, fill=NX))
    o.append(R(20, 252, 680, 44, FIGBG, L2, 6, 1.2))
    o.append(TM(360, 279, '0 2 * * *  /usr/bin/python3 /usr/local/bin/backup.py', 14, bold=True))
    o.append(T(360, 318, 'tar returns 0, so the script deletes the old archive, logs done and exits 0; a failed tar would exit 1.', 13, fill=MUT))
    return 334, ''.join(o)
FIG[7] = (f7, 'Run at 02:00 on 6 Nov, the script makes www-20261106.tar.gz and deletes any archive more than 7 days old: www-20261029.tar.gz is 8 days old, so it goes.',
          'A day line from 28 Oct to 6 Nov with a dashed cut-off 7 days back; the new archive of 6 Nov sits in the kept zone and the archive of 29 Oct, 8 days old, is crossed out. Below, the crontab line.')


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
    if k == 7:
        ch = json.loads(json.dumps(ch, ensure_ascii=False).replace('20261030', '20261029'))
    return ch


def drop_sources():
    return ['.edu/', '.ac.in/', '.ac.uk/']
