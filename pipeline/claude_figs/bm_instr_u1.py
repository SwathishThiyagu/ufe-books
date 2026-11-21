"""Claude's hand-drawn figures for bm-instr-u1 (bioelectric signals, electrodes and recorders), one per chapter.
Every number comes from that chapter's worked example. Colours are the shell's CSS variables."""
import os, sys, math, random
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
AFTER = {1: 3, 2: 2, 3: 3, 4: 4, 5: 2, 6: 2, 7: 2, 8: 2, 9: 3, 10: 1, 11: 2}


def sb(base, s, size=11):
    return f'{base}<tspan baseline-shift="sub" font-size="{size}">{s}</tspan>'


def res_h(x1, x2, y, c=INK, n=6, amp=7):
    xm1, xm2 = x1 + (x2 - x1) * 0.25, x2 - (x2 - x1) * 0.25
    pts = [(x1, y), (xm1, y)]
    for i in range(n):
        pts.append((xm1 + (xm2 - xm1) * (i + 0.5) / n, y + (amp if i % 2 == 0 else -amp)))
    pts += [(xm2, y), (x2, y)]
    return P(pts, c, 1.8)


def res_v(x, ytop, ybot, c=INK, n=6, amp=7):
    ym1, ym2 = ytop + (ybot - ytop) * 0.25, ybot - (ybot - ytop) * 0.25
    pts = [(x, ytop), (x, ym1)]
    for i in range(n):
        pts.append((x + (amp if i % 2 == 0 else -amp), ym1 + (ym2 - ym1) * (i + 0.5) / n))
    pts += [(x, ym2), (x, ybot)]
    return P(pts, c, 1.8)


def cap_v(x, ytop, ybot, c=INK, w=22):
    ym = (ytop + ybot) / 2
    return (L(x, ytop, x, ym - 5, c, 1.8) + L(x, ym + 5, x, ybot, c, 1.8)
            + L(x - w / 2, ym - 5, x + w / 2, ym - 5, c, 3) + L(x - w / 2, ym + 5, x + w / 2, ym + 5, c, 3))


def batt_h(x1, x2, y, c=INK):
    """cell between x1 and x2 on a horizontal wire: long plate (+) then short plate"""
    xm = (x1 + x2) / 2
    return (L(x1, y, xm - 4, y, c, 1.8) + L(xm + 4, y, x2, y, c, 1.8)
            + L(xm - 4, y - 14, xm - 4, y + 14, c, 2.5) + L(xm + 4, y - 7, xm + 4, y + 7, c, 4))


def gnd(x, y, c=INK):
    return L(x - 12, y, x + 12, y, c, 2) + L(x - 7, y + 5, x + 7, y + 5, c, 2) + L(x - 3, y + 10, x + 3, y + 10, c, 2)


def dot(x, y, c=INK):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" style="fill:{c}"/>'


def chain(x0, y, items, w, h=56, gap=22, fills=None, size=13):
    """a row of boxes joined by arrows; items are lists of lines"""
    o = []
    for i, lines in enumerate(items):
        x = x0 + i * (w + gap)
        f = fills[i] if fills else PANEL
        o.append(boxt(x, y, w, h, lines, f, AC, size, bold_first=True))
        if i:
            o.append(L(x - gap, y + h / 2, x - 2, y + h / 2, AC, 2, arrow='n'))
    return ''.join(o)


# ---- 1.1 the action potential of the worked example ----
def f1():
    x0, x1, y0, y1 = 80, 520, 40, 330
    fx = lambda t: x0 + t / 5 * (x1 - x0)
    fy = lambda v: y1 - (v + 90) / 130 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [0, 1, 2, 3, 4, 5], [-80, -55, -30, 0, 30], fx, fy, 'time (ms)', 'V (mV)', str, neg)]
    o.append(L(fx(0), fy(-70), fx(5), fy(-70), L2, 1.5, '6 4')); o.append(Tb(fx(4.4), fy(-70) - 6, 'rest −70', 13, fill=MUT))
    o.append(L(fx(0), fy(-55), fx(5), fy(-55), NX, 1.5, '6 4')); o.append(Tb(fx(4.25), fy(-55) - 6, 'threshold −55', 13, fill=NX))
    # piecewise smooth trace
    def v(t):
        if t < 0.6: return -70
        if t < 1.0: return -70 + 15 * ((t - 0.6) / 0.4) ** 2
        if t < 1.4: return -55 + 85 * math.sin((t - 1.0) / 0.4 * math.pi / 2)
        if t < 2.2: return 30 - 100 * (1 - math.cos((t - 1.4) / 0.8 * math.pi)) / 2
        if t < 2.7: return -70 - 10 * math.sin((t - 2.2) / 0.5 * math.pi / 2)
        if t < 4.4: return -80 + 10 * (1 - math.cos((t - 2.7) / 1.7 * math.pi)) / 2
        return -70
    pts = [(fx(i / 200 * 5), fy(v(i / 200 * 5))) for i in range(201)]
    o.append(P(pts, AC, 3))
    o.append(T(fx(0.62), fy(-73) + 22, 'stimulus', 13, 'start', MUT))
    o.append(L(fx(0.6), fy(-74) + 4, fx(0.6), fy(-66), MUT, 1.5, arrow='m'))
    o.append(Tb(fx(1.4), fy(30) - 10, 'peak +30', 13, fill=AC, bold=True))
    o.append(T(fx(0.95), fy(0), 'Na⁺ in', 13, 'end', AC))
    o.append(T(fx(1.95), fy(0), 'K⁺ out', 13, 'start', AC))
    o.append(T(fx(2.75), fy(-80) + 22, 'undershoot −80', 13, 'middle', MUT))
    # brackets on the right
    bx = fx(5) + 30
    o.append(L(bx, fy(-70), bx, fy(30), INK, 1.6)); o.append(L(bx - 6, fy(-70), bx + 6, fy(-70), INK, 1.6)); o.append(L(bx - 6, fy(30), bx + 6, fy(30), INK, 1.6))
    o.append(T(bx + 12, fy(-20), 'spike amplitude', 13, 'start')); o.append(T(bx + 12, fy(-20) + 18, '30 − (−70) = 100 mV', 14, 'start', bold=True))
    bx2 = fx(5) + 60
    o.append(L(bx2, fy(-70), bx2, fy(-55), NX, 1.6)); o.append(L(bx2 - 5, fy(-70), bx2 + 5, fy(-70), NX, 1.6)); o.append(L(bx2 - 5, fy(-55), bx2 + 5, fy(-55), NX, 1.6))
    o.append(T(bx2 + 10, fy(-62.5) + 5, '15 mV to threshold', 13, 'start', NX, bold=True))
    # duration
    o.append(brace(fx(1.0), fx(2.2), fy(30) - 34, INK, up=False))
    o.append(T(fx(1.6), fy(30) - 42, 'about 1.2 ms', 13))
    return 380, ''.join(o)
FIG[1] = (f1, 'The worked example\'s neuron: from rest at −70 mV a stimulus lifts the membrane 15 mV to the −55 mV threshold, Na⁺ inflow drives it to +30 mV, and K⁺ outflow brings it back through a small undershoot. The spike amplitude is 100 mV and the spike lasts about 1.2 ms.',
          'Plot of membrane voltage against time over 5 milliseconds: rest at minus 70 millivolts, threshold at minus 55, a spike to plus 30 and an undershoot to minus 80, with brackets showing 15 millivolts to threshold and a 100 millivolt spike amplitude.')


# ---- 1.2 electrode equivalent circuit and the divider of the worked example ----
def f2():
    o = [T(20, 26, 'One electrode as a circuit', 15, 'start', bold=True)]
    y = 92
    o.append(R(20, 52, 120, 80, ACS, AC, 8)); o.append(T(80, 86, 'tissue and', 13)); o.append(T(80, 103, 'gel (ions)', 13))
    o.append(L(140, y, 170, y, INK, 1.8))
    o.append(batt_h(170, 220, y)); o.append(T(195, y - 22, sb('E', 'hc'), 14, bold=True)); o.append(T(195, y + 34, 'half-cell', 13, fill=MUT))
    # parallel Rd Cd
    o.append(L(220, y, 250, y, INK, 1.8)); o.append(L(250, y - 26, 250, y + 26, INK, 1.8)); o.append(L(350, y - 26, 350, y + 26, INK, 1.8))
    o.append(res_h(250, 350, y - 26)); o.append(T(300, y - 40, sb('R', 'd'), 14, bold=True))
    o.append(L(250, y + 26, 293, y + 26, INK, 1.8) + L(307, y + 26, 350, y + 26, INK, 1.8) + L(293, y + 14, 293, y + 38, INK, 3) + L(307, y + 14, 307, y + 38, INK, 3))
    o.append(T(300, y + 56, sb('C', 'd') + ' double layer', 13, fill=MUT))
    o.append(L(350, y, 380, y, INK, 1.8)); o.append(res_h(380, 460, y)); o.append(T(420, y - 16, sb('R', 's'), 14, bold=True)); o.append(T(420, y + 34, 'gel and skin', 13, fill=MUT))
    o.append(L(460, y, 500, y, INK, 1.8)); o.append(R(500, 66, 200, 52, PANEL, AC, 8)); o.append(T(600, 90, 'wire to amplifier', 13)); o.append(T(600, 108, '(electrons)', 13, fill=MUT))
    o.append(T(20, 182, 'Worked example: 10 MΩ glass microelectrode into a 1 GΩ amplifier', 15, 'start', bold=True))
    # divider
    top, bot = 214, 340
    o.append(f'<circle cx="80" cy="{(top + bot) / 2:.1f}" r="22" style="fill:var(--panel);stroke:var(--accent);stroke-width:2"/>')
    o.append(T(80, (top + bot) / 2 + 5, sb('V', 'bio'), 14, bold=True))
    o.append(L(80, top, 80, (top + bot) / 2 - 22, INK, 1.8) + L(80, (top + bot) / 2 + 22, 80, bot, INK, 1.8))
    o.append(L(80, top, 150, top, INK, 1.8)); o.append(res_h(150, 290, top, NX)); o.append(T(220, top - 16, sb('Z', 'e') + ' = 10 MΩ', 14, fill=NX, bold=True))
    o.append(L(290, top, 380, top, INK, 1.8)); o.append(dot(380, top))
    o.append(res_v(380, top, bot, LV)); o.append(T(396, (top + bot) / 2 + 5, sb('Z', 'in') + ' = 1 GΩ', 14, 'start', LV, bold=True))
    o.append(L(80, bot, 380, bot, INK, 1.8)); o.append(gnd(230, bot + 1))
    o.append(L(380, top, 470, top, INK, 1.8)); o.append(T(480, top + 5, sb('V', 'in') + ' at the amplifier', 14, 'start'))
    o.append(boxt(470, 248, 230, 92, ['V<tspan baseline-shift="sub" font-size="11">in</tspan> / V<tspan baseline-shift="sub" font-size="11">bio</tspan> = 1 / (1 + 0.01)', '= 0.9901 arrives', '0.99 % lost in the tip'], LVS, LV, 14))
    return 372, ''.join(o)
FIG[2] = (f2, 'Top: one electrode is a half-cell voltage E<sub>hc</sub>, the double layer R<sub>d</sub> ∥ C<sub>d</sub> and the gel-and-skin resistance R<sub>s</sub>. Bottom: the worked example\'s 10 MΩ tip and 1 GΩ input form a divider, so 0.9901 of the bio-potential arrives and 0.99 % is lost.',
          'Equivalent circuit of one electrode, a half-cell source in series with a resistor-capacitor pair and a series resistance; below, a 10 megohm electrode impedance and a 1 gigaohm amplifier input forming a voltage divider that passes 0.9901 of the signal.')


# ---- 1.3 quarter bridge of the worked example ----
def f3():
    o = [T(20, 26, 'Quarter bridge: one active 350 Ω gauge, GF = 2.0, 5 V excitation', 15, 'start', bold=True)]
    cx, cy, r = 220, 210, 120
    top, bot, lft, rgt = (cx, cy - r), (cx, cy + r), (cx - r, cy), (cx + r, cy)
    def arm(a, b, lab, col, lx, ly, anchor):
        mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        return (L(a[0], a[1], b[0], b[1], col, 2.2) + f'<rect x="{mx - 16:.1f}" y="{my - 16:.1f}" width="32" height="32" rx="3" style="fill:var(--panel);stroke:{col};stroke-width:2" transform="rotate({math.degrees(math.atan2(b[1] - a[1], b[0] - a[0])):.1f} {mx:.1f} {my:.1f})"/>'
                + T(lx, ly, lab, 14, anchor, col, bold=True))
    o.append(arm(top, rgt, 'R + ΔR = 350.7 Ω', LV, cx + 78, cy - 78, 'start'))
    o.append(arm(top, lft, '350 Ω', INK, cx - 78, cy - 70, 'end'))
    o.append(arm(lft, bot, '350 Ω', INK, cx - 78, cy + 82, 'end'))
    o.append(arm(rgt, bot, '350 Ω', INK, cx + 78, cy + 82, 'start'))
    for p in (top, bot, lft, rgt): o.append(dot(*p))
    o.append(L(cx, cy - r, cx, cy - r - 24, INK, 1.8)); o.append(T(cx, cy - r - 30, '+5 V', 14, bold=True))
    o.append(L(cx, cy + r, cx, cy + r + 14, INK, 1.8)); o.append(gnd(cx, cy + r + 14))
    o.append(L(lft[0], cy, lft[0] - 40, cy, INK, 1.8)); o.append(L(rgt[0], cy, rgt[0] + 40, cy, INK, 1.8))
    o.append(T(lft[0] - 46, cy + 5, 'a', 14, 'end', bold=True)); o.append(T(rgt[0] + 46, cy + 5, 'b', 14, 'start', bold=True))
    o.append(Tb(cx, cy + 5, sb('V', 'ab') + ' = 2.5 mV', 15, fill=AC, bold=True))
    # beam
    bx = 470
    o.append(R(bx, 120, 26, 150, 'var(--line)', L2, 2, 1.5)); o.append(T(bx + 13, 290, 'wall', 13, fill=MUT))
    o.append(R(bx + 26, 170, 190, 22, ACS, AC, 3)); o.append(R(bx + 70, 162, 46, 8, LVS, LV, 2)); o.append(T(bx + 93, 152, 'gauge in tension', 13, fill=LV))
    o.append(L(bx + 206, 120, bx + 206, 166, NX, 3, arrow='x')); o.append(T(bx + 200, 112, 'force', 13, 'end', NX, bold=True))
    o.append(T(bx + 120, 230, 'ε = 1000 µε = 1 × 10⁻³', 14, bold=True))
    o.append(T(bx + 120, 252, 'ΔR = R GF ε = 350 × 2.0 × 10⁻³', 13))
    o.append(T(bx + 120, 270, '= 0.70 Ω', 13, bold=True))
    o.append(R(440, 296, 260, 70, LVS, LV)); o.append(T(570, 322, 'ΔV = V<tspan baseline-shift="sub" font-size="11">ex</tspan> × GF × ε / 4', 14)); o.append(T(570, 352, '= 5 × 2.0 × 10⁻³ / 4 = 2.5 mV', 14, bold=True))
    return 384, ''.join(o)
FIG[3] = (f3, 'The worked example\'s quarter bridge: 1000 µε raises the active gauge from 350 Ω to 350.7 Ω, and the 5 V bridge gives V<sub>ab</sub> = 5 × 2.0 × 10⁻³ / 4 = 2.5 mV (2.497 mV exactly) to the amplifier.',
          'A Wheatstone bridge with three fixed 350 ohm arms and one active strain gauge of 350.7 ohms, excited by 5 volts, giving 2.5 millivolts between its middle nodes; beside it a cantilever beam with the gauge bonded on top under a force.')


# ---- 1.4 the bio-amplifier and DAS chain with the worked example's signal ----
def f4():
    o = [T(20, 26, 'Gain 1000, CMRR 80 dB: 1 mV signal on 50 mV common-mode', 15, 'start', bold=True)]
    row1 = [['Electrodes', '1 mV + 50 mV'], ['INA', 'gain 10'], ['High-pass', '0.05 Hz'], ['Gain ×100', 'total 1000'], ['Low-pass', '150 Hz']]
    o.append(chain(14, 56, row1, 120, 60, 24, [PANEL, ACS, PANEL, ACS, PANEL]))
    o.append(P([(14 + 4 * 144 + 60, 116), (14 + 4 * 144 + 60, 150), (674, 150)], AC, 2))
    row2 = [['Notch', '50 Hz'], ['Sample', 'and hold'], ['ADC', '12 bit, 3.3 V'], ['MCU', 'store, display']]
    xs = [524, 380, 236, 92]
    for i, (lines, x) in enumerate(zip(row2, xs)):
        o.append(boxt(x, 164, 120, 60, lines, PANEL if i != 2 else ACS, AC, 13, bold_first=True))
    o.append(L(674, 150, 674, 194, AC, 2)); o.append(L(674, 194, 646, 194, AC, 2, arrow='n'))
    o.append(L(524, 194, 502, 194, AC, 2, arrow='n')); o.append(L(380, 194, 358, 194, AC, 2, arrow='n')); o.append(L(236, 194, 214, 194, AC, 2, arrow='n'))
    o.append(T(360, 250, 'analog filters come before the sampler, so nothing above fs/2 can alias', 13, fill=MUT))
    o.append(boxt(20, 270, 330, 104, ['signal out = 1000 × 1 mV = 1 V', 'A<tspan baseline-shift="sub" font-size="11">cm</tspan> = 1000 / 10⁴ = 0.1', 'interference = 0.1 × 50 mV = 5 mV', '= 0.5 % of the signal'], LVS, LV, 14))
    o.append(boxt(370, 270, 330, 104, ['ADC step = 3.3 V / 4096 = 0.806 mV', 'at the electrodes: 0.806 mV / 1000', '= 0.806 µV per count'], PANEL, AC, 14))
    return 388, ''.join(o)
FIG[4] = (f4, 'The chain from electrodes to stored number, with modest first-stage gain, the offset-removing high-pass, more gain, the anti-alias low-pass and the notch all before the sampler. With the worked example\'s numbers the 1 mV ECG leaves as 1 V and the 50 mV common-mode leaves as only 5 mV (0.5 %).',
          'Block chain of electrodes, instrumentation amplifier, high-pass filter, second gain stage, low-pass filter, notch, sample and hold, 12-bit ADC and microcontroller, with boxes giving the 1 volt signal output, 5 millivolt interference and 0.806 microvolt input step.')


# ---- 1.5 ECG strip of the worked example ----
def f5():
    s = 12  # px per mm
    gx, gy, wmm, hmm = 30, 50, 54, 22
    o = [T(20, 26, '25 mm/s, 10 mm/mV: RR = 18 mm, QRS = 2 mm', 15, 'start', bold=True)]
    for i in range(wmm + 1):
        o.append(L(gx + i * s, gy, gx + i * s, gy + hmm * s, 'var(--line)' if i % 5 else L2, 1 if i % 5 else 1.4))
    for j in range(hmm + 1):
        o.append(L(gx, gy + j * s, gx + wmm * s, gy + j * s, 'var(--line)' if j % 5 else L2, 1 if j % 5 else 1.4))
    base = gy + 16 * s
    # calibration bar: 1 mV = 10 mm high, 5 mm wide
    o.append(P([(gx + 1 * s, base), (gx + 1 * s, base - 10 * s), (gx + 5 * s, base - 10 * s), (gx + 5 * s, base)], LV, 2.5))
    o.append(Tb(gx + 3 * s, base - 10 * s - 8, '1 mV = 10 mm', 13, fill=LV, bold=True))
    def beat(x0):
        """x0 = R peak position in mm"""
        pts = []
        def add(mm, mv): pts.append((gx + mm * s, base - mv * 10 * s))
        for i in range(0, 13):  # P wave, 2.5 mm wide, 0.15 mV, ends 2 mm before Q
            t = i / 12; add(x0 - 6.5 + 2.5 * t, 0.15 * math.sin(math.pi * t))
        add(x0 - 1.0, 0); add(x0 - 0.6, -0.1); add(x0, 1.0); add(x0 + 0.6, -0.2); add(x0 + 1.0, 0)
        for i in range(0, 17):
            t = i / 16; add(x0 + 3.0 + 4.0 * t, 0.3 * math.sin(math.pi * t))
        return [(gx + (x0 - 9) * s, base)] + pts + [(gx + (x0 + 9) * s, base)]
    r1, r2 = 18, 36
    o.append(P([(gx + 6 * s, base)] + beat(r1) + beat(r2) + [(gx + wmm * s, base)], AC, 2.5))
    o.append(T(gx + (r1 - 5.25) * s, base - 3.0 * s, 'P', 14, bold=True))
    o.append(T(gx + r1 * s + 14, base - 9.6 * s, 'R', 14, 'start', bold=True))
    o.append(T(gx + (r1 + 5) * s, base - 4.6 * s, 'T', 14, bold=True))
    # RR bracket
    yb = gy + 2 * s
    o.append(L(gx + r1 * s, yb, gx + r2 * s, yb, INK, 1.8)); o.append(L(gx + r1 * s, yb - 7, gx + r1 * s, yb + 7, INK, 1.8)); o.append(L(gx + r2 * s, yb - 7, gx + r2 * s, yb + 7, INK, 1.8))
    o.append(Tb(gx + (r1 + r2) / 2 * s, yb + 5, 'RR = 18 mm', 14, bold=True))
    # QRS width bracket under
    yq = base + 2.5 * s
    o.append(brace(gx + (r2 - 1) * s, gx + (r2 + 1) * s, yq, NX, up=True))
    o.append(Tb(gx + r2 * s, yq + 22, 'QRS 2 mm', 13, fill=NX, bold=True))
    o.append(T(gx, gy + hmm * s + 26, 'small square 1 mm = 0.04 s and 0.1 mV; large square 5 mm = 0.2 s', 13, 'start', MUT))
    o.append(boxt(gx, gy + hmm * s + 40, 320, 56, ['RR = 18 / 25 = 0.72 s', 'HR = 60 / 0.72 = 83.3 bpm'], LVS, LV, 14))
    o.append(boxt(gx + 340, gy + hmm * s + 40, 308, 56, ['QRS = 2.0 / 25 = 0.08 s', '= 80 ms (normal)'], NXS, NX, 14))
    return gy + hmm * s + 108, ''.join(o)
FIG[5] = (f5, 'The worked example\'s strip on standard paper: two beats 18 mm apart at 25 mm/s give RR = 0.72 s and 83.3 bpm, and the 2 mm QRS is 0.08 s. The 1 mV calibration bar must stand exactly 10 mm tall before any height is read.',
          'ECG paper grid with a 10 millimetre calibration bar and two heartbeats whose R peaks are 18 millimetres apart, the QRS complex 2 millimetres wide, with boxes converting to 0.72 seconds, 83.3 beats per minute and 0.08 seconds.')


# ---- 1.6 EEG and EMG bands on a frequency axis, with their gains ----
def f6():
    x0, x1 = 60, 680
    fx = lambda f: x0 + (math.log10(f) + 1) / 4 * (x1 - x0)  # 0.1 Hz .. 1000 Hz
    o = [T(20, 26, 'Two chains, two bands (log frequency axis)', 15, 'start', bold=True)]
    ya = 190
    o.append(xaxis(x0, x1, ya, [0.1, 1, 10, 100, 1000], fx, 'frequency (Hz)', lambda v: f'{v:g}'))
    o.append(R(fx(0.5), 70, fx(70) - fx(0.5), 34, ACS, AC, 6)); o.append(T((fx(0.5) + fx(70)) / 2, 92, 'EEG 0.5–70 Hz', 14, fill=AC, bold=True))
    o.append(R(fx(8), 112, fx(13) - fx(8), 22, LVS, LV, 4)); o.append(T(fx(8) - 6, 128, 'alpha 8–13 Hz', 13, 'end', LV))
    o.append(R(fx(20), 142, fx(500) - fx(20), 34, NXS, NX, 6)); o.append(T(fx(170), 164, 'EMG 20–500 Hz', 14, fill=NX, bold=True))
    o.append(L(fx(50), 54, fx(50), ya, INK, 1.8, '5 4')); o.append(T(fx(50), 48, '50 Hz notch', 13, bold=True))
    o.append(L(fx(125), 60, fx(125), 104, AC, 1.5, '3 3')); o.append(T(fx(125) + 4, 66, 'EEG Nyquist 125 Hz', 13, 'start', AC))
    y = 250
    o.append(boxt(20, y, 330, 104, ['EEG: 50 µV × 10⁴ = 0.5 V', 'fs = 250 Hz, Nyquist = 125 Hz', 'above the 70 Hz band: no alias', '(analog low-pass still first)'], ACS, AC, 14))
    o.append(boxt(370, y, 330, 104, ['EMG: 2 mV × 500 = 1 V', 'fs = 2000 Hz, Nyquist = 1000 Hz', 'EEG gain on EMG: 2 mV × 10⁴', '= 20 V, the amplifier clips'], NXS, NX, 14))
    return 366, ''.join(o)
FIG[6] = (f6, 'EEG and EMG occupy different bands and sizes, so each gets its own gain and filters. With the worked example\'s numbers the 50 µV EEG leaves at 0.5 V and its 250 Hz sampling gives a 125 Hz Nyquist frequency, above the 70 Hz band; a 2 mV EMG needs only gain 500.',
          'Log frequency axis from 0.1 to 1000 hertz with the EEG band 0.5 to 70 hertz, the alpha band 8 to 13 hertz, the EMG band 20 to 500 hertz and a 50 hertz notch marked; boxes below give the EEG output of 0.5 volts and the EMG output of 1 volt.')


# ---- 1.7 nerve conduction: two stimulation sites and two responses ----
def f7():
    o = [T(20, 26, 'Motor NCV: stimulate at two sites, record over the muscle', 15, 'start', bold=True)]
    # limb
    o.append(P([(40, 92), (560, 92), (610, 78), (680, 80)], L2, 26))
    o.append(P([(40, 92), (560, 92), (610, 78), (680, 80)], 'var(--fig)', 20))
    o.append(T(60, 70, 'elbow', 13, 'start', MUT)); o.append(T(520, 70, 'wrist', 13, 'start', MUT)); o.append(T(640, 116, 'hand muscle', 13, fill=MUT))
    o.append(L(40, 92, 600, 92, NX, 2, '6 4')); o.append(T(300, 86, 'nerve', 13, fill=NX))
    for x, lab in ((140, 'S2 proximal'), (480, 'S1 distal')):
        o.append(C(x, 92, 8, LV)); o.append(T(x, 128, lab, 13, fill=LV, bold=True))
    o.append(R(632, 70, 30, 18, ACS, AC, 3)); o.append(T(647, 60, 'record', 13, fill=AC, bold=True))
    o.append(L(140, 146, 480, 146, INK, 1.8)); o.append(L(140, 139, 140, 153, INK, 1.8)); o.append(L(480, 139, 480, 153, INK, 1.8))
    o.append(Tb(310, 151, 'd = 200 mm between the two cathodes', 14, bold=True))
    # traces
    x0, x1 = 80, 600
    fx = lambda ms: x0 + ms / 12 * (x1 - x0)
    def cmap(t0, yb, col):
        pts = []
        for i in range(241):
            t = i / 240 * 12
            u = t - t0
            v = 0 if u < 0 else (-math.sin(math.pi * u / 3) if u < 3 else (0.45 * math.sin(math.pi * (u - 3) / 3) if u < 6 else 0))
            pts.append((fx(t), yb + v * 34))
        return P(pts, col, 2.5)
    ya, yb = 220, 300
    o.append(T(20, ya - 40, 'distal', 13, 'start', LV, bold=True)); o.append(cmap(2, ya, LV))
    o.append(T(20, yb - 40, 'proximal', 13, 'start', NX, bold=True)); o.append(cmap(6, yb, NX))
    o.append(L(fx(0), ya - 52, fx(0), yb + 30, INK, 1.5, '4 3')); o.append(T(fx(0), yb + 46, 'stimulus 0', 13))
    o.append(L(fx(2), ya - 48, fx(2), ya + 6, LV, 1.5)); o.append(T(fx(2) + 4, ya - 50, '2 ms', 13, 'start', LV, bold=True))
    o.append(L(fx(6), yb - 48, fx(6), yb + 6, NX, 1.5)); o.append(T(fx(6) + 4, yb - 50, '6 ms', 13, 'start', NX, bold=True))
    o.append(xaxis(x0, x1, yb + 60, [0, 2, 4, 6, 8, 10, 12], fx, 'time after the stimulus (ms)'))
    o.append(boxt(610, 196, 100, 122, ['Δt = 6 − 2', '= 4 ms', 'v = 200 / 4', '= 50 m/s'], LVS, LV, 14))
    return yb + 116, ''.join(o)
FIG[7] = (f7, 'The worked example: the distal response starts 2 ms after the stimulus and the proximal one 6 ms after it. Only the 4 ms difference belongs to the 200 mm segment between the two sites, so v = 200 mm / 4 ms = 50 m/s.',
          'A forearm with stimulation sites at the elbow and the wrist 200 millimetres apart and a recording electrode on the hand muscle; below, two muscle responses starting at 2 and 6 milliseconds, giving a 4 millisecond difference and 50 metres per second.')


# ---- 1.8 heart-rate monitor and Holter paths ----
def f8():
    o = [T(20, 26, 'One ECG, two uses', 15, 'start', bold=True)]
    o.append(boxt(14, 104, 108, 70, ['ECG', 'amplifier'], ACS, AC, 13, bold_first=True))
    o.append(P([(122, 139), (140, 139), (140, 79), (156, 79)], AC, 2)); o.append(L(150, 79, 156, 79, AC, 2, arrow='n'))
    o.append(P([(140, 139), (140, 219), (156, 219)], AC, 2)); o.append(L(150, 219, 156, 219, AC, 2, arrow='n'))
    top = [['Band-pass', '5–15 Hz'], ['QRS detect', '200 ms lock'], ['RR timer', 'RR = 0.80 s'], ['HR = 60/RR', '75 bpm']]
    o.append(chain(158, 52, top, 118, 56, 16, [PANEL, PANEL, PANEL, LVS]))
    o.append(T(430, 136, 'alarm if the rate leaves the set limits', 13, fill=MUT))
    bot = [['ADC', '3 ch × 250 S/s'], ['Flash memory', '97.2 MB/day'], ['Replay', 'scan all beats'], ['Average', '75 bpm']]
    o.append(chain(158, 192, bot, 118, 56, 16, [PANEL, ACS, PANEL, LVS]))
    o.append(boxt(158, 272, 268, 76, ['3 × 250 × 86,400 × 1.5 bytes', '= 97.2 MB per 24 h'], ACS, AC, 14))
    o.append(boxt(442, 272, 264, 76, ['108,000 beats ÷ 1440 min', '= 75 bpm average'], LVS, LV, 14))
    return 362, ''.join(o)
FIG[8] = (f8, 'The bedside monitor detects each QRS, times RR and shows 60/RR, so RR = 0.80 s reads 75 bpm. The Holter stores every sample instead: three channels at 250 samples/s need 97.2 MB a day, and the replay of 108,000 beats over 1440 minutes gives the same 75 bpm average.',
          'Block diagram in which one ECG amplifier feeds a heart-rate path of band-pass filter, QRS detector, RR timer and rate display, and a Holter path of ADC, flash memory, replay and average, with the worked numbers 97.2 megabytes per day and 75 beats per minute.')


# ---- 1.9 averaging raises the SNR by root N ----
def f9():
    random.seed(7)
    x0, x1 = 170, 600
    fx = lambda ms: x0 + ms / 300 * (x1 - x0)
    def ep(t):  # VEP-like: N75, P100, N145 (µV)
        return (-0.6 * math.exp(-((t - 75) / 10) ** 2) + 1.0 * math.exp(-((t - 100) / 11) ** 2) - 0.7 * math.exp(-((t - 145) / 16) ** 2))
    comps = [(random.uniform(4, 30), random.uniform(0, 6.28)) for _ in range(12)]
    def noise(t):
        return sum(math.sin(2 * math.pi * f * t / 1000 + ph) for f, ph in comps)
    rms = math.sqrt(sum(noise(i) ** 2 for i in range(0, 300)) / 300)
    o = [T(20, 26, 'VEP of 1 µV in 2 µV of EEG noise (single-trial SNR 0.5)', 15, 'start', bold=True)]
    rows = [(1, 'one trial', 'SNR 0.5'), (16, '16 trials', 'SNR 0.5 × 4 = 2'), (400, '400 trials', 'SNR 0.5 × 20 = 10')]
    for i, (n, lab, snr) in enumerate(rows):
        yb = 100 + i * 100
        scale = 2.0 / math.sqrt(n) / rms
        random.seed(11 + i)
        sh = random.uniform(0, 300)
        pts = [(fx(t), yb - max(-5.0, min(5.0, ep(t) + scale * noise(t + sh))) * 8) for t in range(0, 301, 2)]
        o.append(L(x0, yb, x1, yb, 'var(--line)', 1))
        o.append(P(pts, AC if n < 400 else LV, 2))
        o.append(T(20, yb - 6, lab, 14, 'start', bold=True)); o.append(T(20, yb + 13, snr, 13, 'start', MUT))
    o.append(L(fx(100), 50, fx(100), 336, NX, 1.5, '5 4')); o.append(T(fx(100) + 6, 360, 'P100 at 100 ms', 13, 'start', NX, bold=True))
    o.append(L(fx(0), 40, fx(0), 336, INK, 1.5)); o.append(T(fx(0), 360, 'stimulus', 13))
    o.append(xaxis(x0, x1, 380, [0, 100, 200, 300], fx, 'time after the stimulus (ms)'))
    o.append(boxt(612, 150, 100, 110, ['SNR', '= 0.5 √N', 'N = 400', 'for SNR 10'], LVS, LV, 14))
    return 432, ''.join(o)
FIG[9] = (f9, 'The same 1 µV response is locked to the stimulus in every trial while the 2 µV background is not, so the average keeps the response and the noise shrinks by √N. Sixteen trials give SNR 2; the worked example\'s 400 trials give SNR 10 and a clear P100.',
          'Three traces of a visual evoked potential after one, 16 and 400 averaged trials, the first buried in noise and the last showing a clear positive peak at 100 milliseconds, with signal-to-noise ratios of 0.5, 2 and 10.')


# ---- 1.10 the EMG biofeedback loop of the worked example ----
def f10():
    o = [T(20, 26, 'EMG relaxation loop: 20 µV RMS test input, gain 1000', 15, 'start', bold=True)]
    items = [['Electrodes', '20 µV RMS'], ['Amplifier', '× 1000'], ['Band-pass', '20–500 Hz'], ['Rectifier', '|v|'], ['Smoother', '0.90 × RMS']]
    o.append(chain(14, 52, items, 120, 60, 22, [PANEL, ACS, PANEL, PANEL, PANEL]))
    o.append(T(14 + 1 * 142 + 60, 132, '20 mV RMS', 13, fill=AC, bold=True))
    o.append(T(14 + 4 * 142 + 60, 132, '18.0 mV', 13, fill=AC, bold=True))
    o.append(P([(14 + 4 * 142 + 60, 140), (14 + 4 * 142 + 60, 176), (520, 176)], AC, 2))
    o.append(L(530, 176, 506, 176, AC, 2, arrow='n'))
    o.append(boxt(330, 156, 176, 72, ['Comparator', 'on ≥ 15 mV, off < 12 mV'], LVS, LV, 13, bold_first=True))
    o.append(L(330, 192, 252, 192, AC, 2, arrow='n'))
    o.append(boxt(140, 162, 112, 60, ['Tone', 'ON (C = 1)'], NXS, NX, 13, bold_first=True))
    o.append(boxt(14, 162, 100, 60, ['Patient', 'hears it'], PANEL, INK, 13, bold_first=True))
    o.append(L(140, 192, 116, 192, NX, 2, arrow='x'))
    o.append(P([(64, 162), (64, 118)], NX, 2, '6 4')); o.append(L(64, 124, 64, 116, NX, 2, arrow='x'))
    o.append(T(72, 146, 'relaxes', 13, 'start', NX))
    # hysteresis strip
    x0, x1, y0, y1 = 90, 700, 274, 374
    fx = lambda t: x0 + t / 10 * (x1 - x0)
    fy = lambda v: y1 - v / 20 * (y1 - y0)
    o.append(L(x0, y1, x1, y1, L2, 1.5)); o.append(L(x0, y0, x0, y1, L2, 1.5))
    o.append(T(x0 - 8, fy(15) + 4, '15', 13, 'end', LV)); o.append(T(x0 - 8, fy(12) + 4, '12', 13, 'end', LV)); o.append(T(x0 - 8, fy(18) + 4, '18', 13, 'end', MUT))
    o.append(L(x0, fy(15), x1, fy(15), LV, 1.5, '6 4')); o.append(L(x0, fy(12), x1, fy(12), LV, 1.5, '6 4'))
    env = lambda t: 18.0 if t < 4 else (18.0 - 7.2 * (t - 4) / 3 if t < 7 else 10.8)
    o.append(P([(fx(i / 20), fy(env(i / 20))) for i in range(201)], AC, 2.5))
    o.append(T(fx(1.6), fy(18) - 8, 'envelope 18.0 mV: tone on', 13, fill=AC))
    o.append(T(fx(8.4), fy(10.8) + 20, '10.8 mV: tone off', 13, fill=AC))
    o.append(T(x0 + 4, y0 - 22, 'envelope (mV) as the patient relaxes', 13, 'start', MUT))
    return 398, ''.join(o)
FIG[10] = (f10, 'The worked example\'s loop: 20 µV RMS becomes 20 mV RMS, the rectifier and smoother give an 18.0 mV envelope, and the comparator with hysteresis (on at 15 mV, off below 12 mV) sounds the tone. When the patient relaxes to 12 µV the envelope falls to 10.8 mV and the tone stops.',
          'Biofeedback loop of electrodes, amplifier, band-pass filter, rectifier, smoother, comparator and tone, closed by the patient; below, the envelope falling from 18 to 10.8 millivolts across the 15 and 12 millivolt hysteresis thresholds.')


# ---- 1.11 the gait cycle and the step and stride of the worked example ----
def f11():
    o = [T(20, 26, 'One gait cycle of the right foot: 1000 ms', 15, 'start', bold=True)]
    x0, x1 = 60, 660
    fx = lambda ms: x0 + ms / 1000 * (x1 - x0)
    o.append(R(fx(0), 50, fx(600) - fx(0), 44, ACS, AC, 6)); o.append(T(fx(300), 78, 'stance 0–600 ms (60 %)', 14, fill=AC, bold=True))
    o.append(R(fx(600), 50, fx(1000) - fx(600), 44, NXS, NX, 6)); o.append(T(fx(800), 78, 'swing 600–1000 ms (40 %)', 14, fill=NX, bold=True))
    o.append(xaxis(x0, x1, 104, [0, 200, 400, 600, 800, 1000], fx, None))
    o.append(T(fx(0), 142, 'heel strike', 13, fill=MUT)); o.append(T(fx(600), 142, 'toe-off', 13, fill=MUT)); o.append(T(fx(1000), 142, 'heel strike', 13, 'end', MUT))
    # footprints
    sc = 300  # px per metre
    fx2 = lambda m: 70 + m * sc
    def foot(xm, y, col, lab):
        return (f'<ellipse cx="{fx2(xm) + 22:.1f}" cy="{y:.1f}" rx="26" ry="11" style="fill:{col};stroke:var(--ink);stroke-width:1.2"/>' + T(fx2(xm) + 22, y + 32, lab, 13, fill=MUT))
    yR, yL = 196, 252
    o.append(foot(0, yR, ACS, 'R')); o.append(foot(0.7, yL, NXS, 'L')); o.append(foot(1.4, yR, ACS, 'R'))
    o.append(L(fx2(0), 290, fx2(0.7), 290, NX, 1.8)); o.append(L(fx2(0), 283, fx2(0), 297, NX, 1.8)); o.append(L(fx2(0.7), 283, fx2(0.7), 297, NX, 1.8))
    o.append(Tb(fx2(0.35), 295, 'step 0.7 m', 13, fill=NX, bold=True))
    o.append(L(fx2(0), 172, fx2(1.4), 172, AC, 1.8)); o.append(L(fx2(0), 165, fx2(0), 179, AC, 1.8)); o.append(L(fx2(1.4), 165, fx2(1.4), 179, AC, 1.8))
    o.append(Tb(fx2(0.7), 177, 'stride 1.4 m = 2 steps', 13, fill=AC, bold=True))
    o.append(boxt(560, 176, 150, 120, ['cadence', '120 / 60 = 2.0 steps/s', 'speed', '0.7 × 2.0 = 1.4 m/s'], LVS, LV, 13))
    return 316, ''.join(o)
FIG[11] = (f11, 'The worked example\'s walker: a 1.0 s cycle with stance 0.60 s and swing 0.40 s, a 0.7 m step and a 1.4 m stride. At 2.0 steps/s the speed is 0.7 × 2.0 = 1.4 m/s.',
          'A time bar of one 1000 millisecond gait cycle split into stance from 0 to 600 milliseconds and swing from 600 to 1000, above footprints showing a 0.7 metre step and a 1.4 metre stride, with cadence 2.0 steps per second and speed 1.4 metres per second.')


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    return {'caption': cap, 'after_section': AFTER[k], 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
