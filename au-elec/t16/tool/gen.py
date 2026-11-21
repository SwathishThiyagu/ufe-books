"""Write the t16 emboss (e2) block for every Automotive Electrical and Electronics lesson.
Every value is computed here from the lesson's own worked examples (lesson branches lesson/au-elec-uN-Lk, books/auto/au-elec).
Usage: python3 gen.py <thumbs.json in> <thumbs.json out>"""
import json, math, sys


def C(id, x, y, text, sub=None, r=66, size=None, **kw):
    n = dict(id=id, x=x, y=y, text=text, r=r, **kw)
    if sub: n['sub'] = sub
    if size: n['size'] = size
    return n


def R(id, x, y, w, h, text, size=24, **kw):
    return dict(id=id, x=x, y=y, w=w, h=h, text=text, size=size, **kw)


def K(a, b, label=None, **kw):
    return dict(a=a, b=b, label=label, **kw)


def T(x, y, text, size=22, color='#5B7CFA', **kw):
    return dict(x=x, y=y, text=text, size=size, color=color, **kw)


def tape(cells, head, y=470, cx=360, cw=64):
    w = sum(max(cw, 26 + 17 * len(str(c))) for c in cells) + 12 * (len(cells) - 1)
    return dict(x=round(cx - w / 2), y=y, cells=cells, head=head, cw=cw)


def f(v, d=1):
    s = f'{v:.{d}f}'
    return s


Y = 250          # main row
GREY = '#A9B4C6'
BLUE = '#5B7CFA'


# ---------------------------------------------------------------- unit 1
def u1L1():                      # hook: Why is the 12 V bus really 14 V?
    I = 120
    right, wrong = 14 * I, 12 * I
    return dict(nodes=[C('b', 110, Y, '12 V', 'nominal', r=70, size=34, dim=True),
                       C('r', 345, Y, '14 V', 'regulated', r=84, size=40, lit=True),
                       C('p', 590, Y, f'{right} W', f'at {I} A', r=82, size=32, ok=True)],
                links=[K('b', 'r', 'alternator'), K('r', 'p', f'× {I} A')],
                texts=[T(360, 430, f'not 12 V × {I} A = {wrong} W', 24, GREY)],
                tapes=[], caption=f'the bus runs at 14 V: <b>{right} W</b>, not {wrong}')


def u1L2():                      # hook: Which plate is lead dioxide?
    sg = 1.28
    cell = sg + 0.84
    return dict(nodes=[C('p', 115, 200, 'PbO<sub>2</sub>', 'positive', r=78, size=34, lit=True),
                       C('n', 605, 200, 'Pb', 'negative', r=78, size=36),
                       C('s', 360, 380, 'PbSO<sub>4</sub>', 'discharged', r=78, size=32, subsize=17, dim=True)],
                boxes=[dict(x=360, y=200, w=190, h=60, text=f'acid · SG {sg}', size=22, inset=True)],
                links=[K('p', 's', 'discharge', lx=-78, ly=34, size=22), K('n', 's', 'discharge', lx=78, ly=34, size=22)],
                texts=[],
                tapes=[tape([f'{cell:.2f} V', '× 6 cells', f'{6 * cell:.2f} V'], 2, y=500)],
                caption='positive is <b>lead dioxide</b>; negative is spongy lead')


def u1L3():                      # hook: Does revving raise the bus voltage?
    Imax = 144
    I = lambda n: Imax * (1 - 1000 / n)
    return dict(nodes=[C('e', 110, Y, '6000', 'rpm, revved', r=72, size=34),
                       C('f', 345, Y, 'field', 'regulator', r=76, size=32),
                       C('v', 590, Y, '14.2 V', 'unchanged', r=84, size=34, subsize=18, lit=True)],
                links=[K('e', 'f', 'sensed'), K('f', 'v', 'holds')],
                texts=[T(360, 430, f'only the output available rises: {I(2000):.0f} A → {I(6000):.0f} A', 23, BLUE)],
                tapes=[tape(['2000 rpm · 14.2 V', '6000 rpm · 14.2 V'], 1, y=480)],
                caption='revving raises the output, <b>not the voltage</b>')


def u1L4():                      # hook: Does the key carry 250 A?
    return dict(nodes=[C('k', 110, Y, '0.2 A', 'key → relay', r=70, size=32),
                       C('s', 345, Y, '40 A', 'solenoid', r=74, size=34),
                       C('m', 590, Y, '250 A', 'starter', r=90, size=40, lit=True)],
                links=[K('k', 's', 'term. 50'), K('s', 'm', 'main contacts', size=22)],
                texts=[T(360, 440, f'the motor current is {250 / 0.2:.0f} times the key current', 23, BLUE)],
                tapes=[], caption='the key only feeds the relay: <b>main contacts carry 250 A</b>')


# ---------------------------------------------------------------- unit 2
def u2L1():                      # hook: How does 12 V become a 25 kV spark?
    v_sec = 250 * 100
    E = 0.5 * 8e-3 * 6 ** 2 * 1000
    return dict(nodes=[C('b', 105, Y, '12 V', 'battery', r=68, size=34),
                       C('p', 340, Y, '250 V', 'primary', r=78, size=36),
                       C('s', 590, Y, f'{v_sec / 1000:.0f} kV', 'secondary', r=92, size=40, lit=True)],
                links=[K('b', 'p', 'points open'), K('p', 's', '× 100 turns')],
                texts=[T(360, 440, f'8 mH at 6 A stores {E:.0f} mJ, released when the field collapses', 21, BLUE)],
                tapes=[], caption=f'250 V × 100, not 12 V × 100: <b>{v_sec / 1000:.0f} kV</b>')


def u2L2():                      # hook: Why does a waste spark fire twice?
    rev = 60 / 4000 * 1000
    return dict(nodes=[C('c', 140, 250, '1 & 4', 'one coil', r=86, size=36, lit=True),
                       C('a', 560, 130, '1', 'compression', r=72, size=38, subsize=17, ok=True),
                       C('b', 560, 370, '4', 'exhaust', r=72, size=38, subsize=17, dim=True)],
                links=[K('c', 'a', 'useful', lit=True, lx=-34, ly=-24), K('c', 'b', 'waste', lx=-34, ly=30)],
                texts=[T(360, 500, f'coil 1 & 4 fires at 0° and 360°: every {rev:.0f} ms at 4000 rpm', 20, GREY)],
                tapes=[tape(['1', '3', '4', '2'], 0, y=525)],
                caption='one fire every revolution: <b>twice per cycle</b>, roles swapped')


def u2L3():                      # hook: Twice the distance: half the light?
    I = 20000
    e25, e50 = I / 25 ** 2, I / 50 ** 2
    return dict(nodes=[C('l', 110, Y, '20 000', 'candela', r=74, size=30),
                       C('a', 345, Y, f'{e25:.0f} lx', 'at 25 m', r=78, size=36),
                       C('b', 590, Y, f'{e50:.0f} lx', 'at 50 m', r=84, size=40, lit=True)],
                links=[K('l', 'a', '÷ 25²'), K('a', 'b', '÷ 50²')],
                texts=[T(360, 440, 'E = I ÷ d²', 30, BLUE)],
                tapes=[], caption=f'twice the distance: <b>a quarter</b>, {e25:.0f} → {e50:.0f} lx, not {e25 / 2:.0f}')


def u2L4():                      # hook: Can an immobilised engine crank?
    return dict(nodes=[C('k', 105, 300, 'key', 'turned', r=68, size=34),
                       C('s', 360, 160, 'cranks', 'starter', r=74, size=30, ok=True),
                       C('e', 360, 440, 'no enable', 'engine ECU', r=80, size=26, lit=True),
                       C('i', 610, 440, '0', 'fuel, spark', r=74, size=38, subsize=16, dim=True)],
                links=[K('k', 's', 'relay', lx=-30, ly=-14), K('k', 'e', 'wrong code', dim=True, lx=-44, ly=22, size=22),
                       K('e', 'i', 'blocked', dim=True)],
                texts=[], tapes=[],
                caption='it <b>cranks</b>, but injectors and coils never fire')


# ---------------------------------------------------------------- unit 3
def u3L1():                      # hook: How does an ECU read a sensor?
    v80 = 5 * 500 / 1500
    c80 = round(v80 * 1023 / 5)
    v25 = 5 * 2000 / 3000
    return dict(nodes=[C('s', 90, Y, '500 Ω', 'NTC, 80 °C', r=66, size=28),
                       C('v', 265, Y, f'{v80:.2f} V', 'divider', r=66, size=28),
                       C('n', 445, Y, f'{c80}', '10-bit', r=70, size=34, lit=True),
                       C('t', 625, Y, '80 °C', 'table', r=66, size=30, ok=True)],
                links=[K('s', 'v', '1 kΩ'), K('v', 'n', 'ADC'), K('n', 't', 'look up')],
                texts=[T(360, 430, f'at 25 °C: 2 kΩ, {v25:.2f} V, count {round(v25 * 1023 / 5)}', 23, BLUE)],
                tapes=[], caption=f'ohms to volts to a count: <b>{5 / 1023 * 1000:.2f} mV</b> a count')


def u3L2():                      # hook: How long is the 60-2 gap?
    T_ = 60 / 3000 / 60 * 1000
    return dict(nodes=[C('w', 110, Y, '60−2', 'crank wheel', r=74, size=32),
                       C('t', 345, Y, f'{T_:.3f}', 'ms a tooth', r=74, size=32),
                       C('g', 590, Y, '3T', f'{3 * T_:.0f} ms gap', r=88, size=44, lit=True)],
                links=[K('w', 't', '3000 rpm'), K('t', 'g', '2 missing')],
                texts=[], tapes=[tape(['T', 'T', 'T', '3T', 'T'], 3, y=440)],
                caption='two teeth missing, yet <b>the gap is 3 T</b>, not 2 T')


def u3L3():                      # hook: Does a VR sensor work at zero speed?
    v = 72 / 3.6; rps = v / 0.3 / (2 * math.pi); fz = rps * 48
    return dict(nodes=[C('w', 120, 260, '0 rpm', 'wheel stopped', r=76, size=30),
                       C('v', 560, 140, '0 V', 'VR coil', r=74, size=36, dim=True),
                       C('h', 560, 380, 'edge', 'Hall switch', r=78, size=34, lit=True)],
                links=[K('w', 'v', 'no motion', dim=True, lx=-30, ly=-24, size=22), K('w', 'h', 'still reads', lit=True, lx=-30, ly=30, size=22)],
                texts=[T(360, 530, f'VR grows with speed: {fz / 20:.1f} Hz at 3.6 km/h, {fz:.0f} Hz at 72', 20, GREY)],
                tapes=[], caption='at standstill: <b>VR is silent</b>, a Hall switch still reads')


def u3L4():                      # hook: Does 0.9 V mean rich or lean?
    lam = 15.4 / 14.7
    k = 8.314 * 1073.15 / (4 * 96485)
    return dict(nodes=[C('r', 120, 150, 'λ < 1', 'rich', r=70, size=32),
                       C('rv', 560, 150, '0.9 V', 'little O<sub>2</sub>', r=78, size=36, subsize=17, lit=True),
                       C('l', 120, 400, f'{lam:.3f}', 'λ, lean', r=70, size=30),
                       C('lv', 560, 400, f'{k * math.log(21) * 1000:.0f} mV', 'spare O<sub>2</sub>', r=78, size=32, subsize=17)],
                links=[K('r', 'rv', 'zirconia'), K('l', 'lv', 'zirconia')],
                texts=[],
                tapes=[], caption='about 0.9 V means <b>rich</b>; about 0.1 V means lean')


def u3L5():                      # hook: Does microstepping add torque?
    full = 1.8
    return dict(nodes=[C('f', 110, Y, f'{full}°', 'full step', r=70, size=34),
                       C('m', 345, Y, f'{full / 16:.4g}°', '1/16 step', r=76, size=30, ok=True),
                       C('t', 590, Y, 'same', 'max holding torque', r=88, size=36, subsize=15, lit=True)],
                links=[K('f', 'm', '÷ 16'), K('m', 't', 'smoother')],
                texts=[T(360, 440, f'{360 / full:.0f} full steps a turn → {360 / full * 16:.0f} microsteps', 23, BLUE)],
                tapes=[], caption='microstepping is <b>smoother, not stronger</b>')


def u3L6():                      # hook: Why does a running motor draw less?
    I = (12 - 10) / 0.2
    return dict(nodes=[C('s', 110, Y, '12 V', 'supply', r=70, size=34),
                       C('e', 345, Y, '10 V', 'back emf', r=76, size=36),
                       C('i', 590, Y, f'{I:.0f} A', 'running', r=88, size=42, lit=True)],
                links=[K('s', 'e', '500 rad/s'), K('e', 'i', '÷ 0.2 Ω')],
                texts=[], tapes=[tape([f'stall {12 / 0.2:.0f} A', f'run {I:.0f} A'], 1, y=440)],
                caption=f'the back emf subtracts: <b>(12 − 10) ÷ 0.2 = {I:.0f} A</b>')


# ---------------------------------------------------------------- unit 4
def u4L1():                      # hook: What does λ = 1 really mean?
    return dict(nodes=[C('a', 110, Y, '14.7 kg', 'air', r=74, size=30),
                       C('f', 345, Y, '1 kg', 'petrol', r=74, size=34),
                       C('l', 590, Y, 'λ = 1', 'stoichiometric', r=88, size=38, subsize=16, lit=True)],
                links=[K('a', 'f', 'with'), K('f', 'l', 'burns')],
                texts=[T(360, 425, 'λ = actual AFR ÷ 14.7, no unit', 23, BLUE)],
                tapes=[tape([f'{13.2 / 14.7:.2f} rich', '1.00', '1.02 lean'], 1, y=465)],
                caption='λ = 1 is <b>14.7 : 1</b> air to fuel, not 1 : 1')


def u4L2():                      # hook: Is an ECU map closed loop?
    ms = 4 + 2 * 0.6
    return dict(nodes=[C('m', 130, 160, f'{ms:.1f} ms', 'map lookup', r=74, size=30),
                       C('i', 590, 160, 'injector', 'pulse', r=74, size=26),
                       C('l', 590, 410, 'λ sensor', 'measures', r=74, size=26),
                       C('t', 130, 410, 'trim', 'closed loop', r=78, size=34, lit=True)],
                links=[K('m', 'i', 'open loop', dim=True), K('i', 'l', 'exhaust', lx=50, size=22),
                       K('l', 't', 'feedback', lit=True, ly=38), K('t', 'i', 'corrects', lit=True, lx=-6, ly=-14, size=22)],
                texts=[T(360, 556, f'2000 rpm, 46 kPa: 4 + 2 × 0.6 = {ms:.1f} ms', 21, GREY)],
                tapes=[], caption='the loop closes only when <b>a sensor measures</b> the result')


def u4L3():                      # hook: Why does dwell angle grow with speed?
    dwell = 3
    a3, a6 = 6 * 3000 / 1000 * dwell, 6 * 6000 / 1000 * dwell
    return dict(nodes=[C('t', 110, Y, f'{dwell} ms', 'dwell held', r=74, size=34, ok=True),
                       C('a', 345, Y, f'{a3:.0f}°', '3000 rpm', r=74, size=36),
                       C('b', 590, Y, f'{a6:.0f}°', '6000 rpm', r=88, size=42, lit=True)],
                links=[K('t', 'a', '18°/ms'), K('a', 'b', '36°/ms')],
                texts=[T(360, 430, f'spark 25° BTDC: charging starts at {25 + a3:.0f}°, then {25 + a6:.0f}°', 23, BLUE)],
                tapes=[], caption='the time is held, so <b>the angle grows</b>')


# ---------------------------------------------------------------- unit 5
def u5L1():                      # hook: How does ACC keep a 2 s gap?
    v, gap = 25, 60
    target = 2 * v
    return dict(nodes=[C('h', 110, Y, f'{v} m/s', 'host', r=72, size=30),
                       C('g', 345, Y, f'{gap} m', f'{gap / v:.1f} s now', r=76, size=34),
                       C('t', 590, Y, f'{target} m', '2 s target', r=88, size=40, lit=True)],
                links=[K('h', 'g', 'radar'), K('g', 't', f'−{gap - target} m')],
                texts=[T(360, 430, f'brake 1.25 m/s² for 4 s to settle on {target} m', 23, BLUE)],
                tapes=[tape([f'20 m/s · {2 * 20} m', f'25 m/s · {2 * 25} m'], 1, y=475)],
                caption=f'the gap is in seconds: <b>2 s = {target} m</b> at {v} m/s')


def u5L2():                      # hook: Understeer: which wheel gets braked?
    des, meas = 0.278, 0.2
    return dict(nodes=[C('d', 90, Y, f'{des}', 'desired yaw', r=66, size=28),
                       C('m', 265, Y, f'{meas:.3f}', 'gyro', r=66, size=28),
                       C('e', 445, Y, f'+{des - meas:.3f}', 'understeer', r=70, size=26),
                       C('w', 625, Y, 'rear inner', '2000 N', r=72, size=22, lit=True)],
                links=[K('d', 'm', ''), K('m', 'e', ''), K('e', 'w', 'brake')],
                texts=[T(360, 430, f'2000 N × 0.75 m = {2000 * 0.75:.0f} N·m into the turn', 23, BLUE),
                       T(360, 500, 'oversteer is the other way: front outer', 21, GREY)],
                tapes=[],
                caption='nose runs wide: brake <b>the rear inner</b> wheel')


def u5L3():                      # hook: Does an airbag replace the belt?
    v = 50 / 3.6; a = v * v / 1.2; t = v / a * 1000
    return dict(nodes=[C('i', 90, Y, '0 ms', 'impact', r=64, size=30),
                       C('s', 265, Y, '25 ms', 'inflating', r=66, size=30, subsize=16),
                       C('f', 445, Y, '50 ms', 'bag full', r=72, size=32, lit=True),
                       C('c', 625, Y, f'{t:.0f} ms', 'car stops', r=66, size=30, subsize=16)],
                links=[K('i', 's', ''), K('s', 'f', ''), K('f', 'c', '')],
                texts=[T(360, 430, f'50 km/h crash: {a / 9.81:.1f} g over {t:.0f} ms', 24, BLUE)],
                tapes=[tape(['belt: stops you', 'bag: spreads the load'], 0, y=475)],
                caption='SRS is supplemental: <b>the belt does the stopping</b>')


# ---------------------------------------------------------------- unit 6
def u6L1():                      # hook: How do 12 ECUs share one bus?
    n = 12; links = n * (n - 1) // 2
    load = (20 * 125 * 100 + 50000) / 500000
    return dict(nodes=[C('n', 130, 270, f'{n}', 'ECUs', r=78, size=42),
                       C('m', 560, 130, f'{links}', 'links if meshed', r=74, size=38, subsize=16, dim=True),
                       C('b', 560, 400, '1', 'shared pair', r=80, size=46, subsize=18, lit=True)],
                links=[K('n', 'm', f'{n}×{n - 1}÷2', dim=True, lx=-40, ly=-24, size=22), K('n', 'b', f'{n} transceivers', lit=True, lx=-50, ly=30, size=22)],
                texts=[T(360, 560, f'bus load 300 ÷ 500 kbit/s = {load * 100:.0f}%', 21, GREY)],
                tapes=[], caption=f'one twisted pair replaces <b>{links} links</b>')


def u6L2():                      # hook: Can a CAN FD frame carry 9 bytes?
    fd = {9: 12, 10: 16, 11: 20, 12: 24, 13: 32, 14: 48, 15: 64}
    return dict(nodes=[C('d9', 150, 160, '9', 'DLC', r=70, size=40),
                       C('b9', 540, 160, f'{fd[9]}', 'bytes', r=80, size=44, lit=True),
                       C('d15', 150, 370, '15', 'DLC', r=70, size=40),
                       C('b15', 540, 370, f'{fd[15]}', 'bytes', r=80, size=44)],
                links=[K('d9', 'b9', 'a code'), K('d15', 'b15', 'a code')],
                texts=[T(360, 500, 'DLC 8 to 15 → bytes', 21, GREY)],
                tapes=[tape(['8'] + [str(fd[d]) for d in range(9, 16)], 1, y=518)],
                caption='above 8 the DLC is a code: <b>9 means 12 bytes</b>')


def u6L3():                      # hook: Does clearing codes fix the fault?
    return dict(nodes=[C('r', 90, Y, '03', 'read codes', r=66, size=36, subsize=15),
                       C('c', 265, Y, 'P0301', 'misfire cyl 1', r=70, size=26, lit=True),
                       C('x', 445, Y, '04', 'lamp off', r=66, size=36, dim=True),
                       C('b', 625, Y, 'P0301', 'comes back', r=70, size=26)],
                links=[K('r', 'c', ''), K('c', 'x', ''), K('x', 'b', '')],
                texts=[T(360, 430, 'reply 43 02 03 01 01 33 → P0301, P0133', 23, BLUE)],
                tapes=[], caption='service 04 only <b>switches the lamp off</b>; the fault returns')


def u6L4():                      # hook: Does MISRA code meet ISO 26262?
    return dict(nodes=[C('m', 110, Y, 'MISRA', 'coding only', r=74, size=28, ok=True),
                       C('h', 345, Y, 'HARA', 'S3 E4 C3', r=74, size=30),
                       C('a', 590, Y, 'D', 'ASIL, safety goal', r=88, size=52, subsize=16, lit=True)],
                links=[K('m', 'h', '+'), K('h', 'a', '3 + 4 + 3')],
                texts=[T(360, 430, 'still needed: safety concept, metrics, verification', 22, BLUE)],
                tapes=[], caption='passing MISRA is only <b>coding evidence</b>')


def u6L5():                      # hook: Is WAVE just 802.11p?
    bits = 300 * 8
    t = bits / 6e6 * 1000
    return dict(nodes=[C('p', 110, 330, '11p', 'radio + MAC', r=72, size=36, subsize=15, dim=True),
                       C('c', 340, 330, '1609.4', 'channels', r=74, size=28, lit=True),
                       C('m', 340, 120, '1609.3', 'messages', r=70, size=28, lit=True),
                       C('s', 585, 225, '1609.2', 'security', r=74, size=28, lit=True)],
                links=[K('p', 'c', ''), K('c', 'm', '', lx=0), K('c', 's', '', arrow=False, dim=True), K('m', 's', '', arrow=False, dim=True)],
                texts=[T(360, 470, f'CCH 50 ms: {int(45 / t)} safety messages of {t:.1f} ms', 21, GREY)],
                tapes=[tape(['CCH 50 ms', 'SCH 50 ms'], 0, y=490)],
                caption='WAVE is <b>the 1609 family</b> on top of 802.11p')


ALL = {'au-elec-u1-L1': u1L1, 'au-elec-u1-L2': u1L2, 'au-elec-u1-L3': u1L3, 'au-elec-u1-L4': u1L4,
       'au-elec-u2-L1': u2L1, 'au-elec-u2-L2': u2L2, 'au-elec-u2-L3': u2L3, 'au-elec-u2-L4': u2L4,
       'au-elec-u3-L1': u3L1, 'au-elec-u3-L2': u3L2, 'au-elec-u3-L3': u3L3, 'au-elec-u3-L4': u3L4,
       'au-elec-u3-L5': u3L5, 'au-elec-u3-L6': u3L6, 'au-elec-u4-L1': u4L1, 'au-elec-u4-L2': u4L2,
       'au-elec-u4-L3': u4L3, 'au-elec-u5-L1': u5L1, 'au-elec-u5-L2': u5L2, 'au-elec-u5-L3': u5L3,
       'au-elec-u6-L1': u6L1, 'au-elec-u6-L2': u6L2, 'au-elec-u6-L3': u6L3, 'au-elec-u6-L4': u6L4,
       'au-elec-u6-L5': u6L5}

if __name__ == '__main__':
    src, dst = sys.argv[1], sys.argv[2]
    Dj = json.load(open(src, encoding='utf-8'))
    for k, L in Dj['lessons'].items():
        if k in ALL:
            e2 = ALL[k]()
            ys = {n['y'] for n in e2['nodes']}
            if ys == {Y}:                       # single row: sit it lower, nearer the middle of the picture
                for grp in ('nodes', 'texts', 'tapes', 'boxes'):
                    for it in e2.get(grp, []):
                        it['y'] += 25
            L['t16'] = {'style': 'emboss', 'e2': e2}
    json.dump(Dj, open(dst, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('t16 blocks:', sum(1 for k in Dj['lessons'] if k in ALL))
