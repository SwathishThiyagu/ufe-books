"""Claude's hand-drawn figures for c-cn-u2 (Computer Networks, unit 2: signals, impairments, capacity, media, line
coding, modulation, multiplexing and spread spectrum), one per chapter, from each chapter's worked example."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}


# ---- 2.1 an analog sine and a digital bit stream ----
def f1():
    o = []
    # analog panel
    x0, x1, yc, A = 70, 620, 90, 46
    fx = lambda t: x0 + t / 8 * (x1 - x0)          # t in ms, 0..8
    o.append(T(20, 24, 'Analog: 50 cycles in 0.2 s', 14, 'start', AC, True))
    o.append(L(x0, yc, x1, yc, L2, 1.2))
    o.append(P([(fx(t / 50), yc - A * math.sin(2 * math.pi * (t / 50) / 4)) for t in range(401)], AC, 2.6))
    for t in (0, 4, 8):
        o.append(L(fx(t), yc + A + 6, fx(t), yc + A + 14, L2, 1.5)); o.append(T(fx(t), yc + A + 30, f'{t} ms', 13, fill=MUT))
    o.append(P([(fx(0), yc + A + 10), (fx(4), yc + A + 10)], AC, 1.6))
    o.append(T(fx(2), yc + A + 30, 'one period T = 1 ÷ 250 = 4 ms', 13, fill=AC, bold=True))
    o.append(T(x1 + 10, yc - 8, 'f = 250 Hz', 13, 'start', AC, True))
    o.append(T(x1 + 10, yc + 12, 'λ = 800 km', 13, 'start', AC, True))
    # digital panel
    y0 = 240
    bits = [1, 0, 1, 1, 0, 1, 0, 0]
    bw = (x1 - x0) / 8
    o.append(T(20, y0 - 32, 'Digital: 1000 bits in 0.25 ms', 14, 'start', NX, True))
    o.append(L(x0, y0 + 40, x1, y0 + 40, L2, 1.2))
    pts = []
    for i, b in enumerate(bits):
        yy = y0 + (0 if b else 40)
        pts += [(x0 + i * bw, yy), (x0 + (i + 1) * bw, yy)]
    o.append(P(pts, NX, 2.6))
    for i, b in enumerate(bits):
        o.append(T(x0 + i * bw + bw / 2, y0 - 6 if b else y0 + 30, str(b), 13, fill=NX, bold=True))
    o.append(brace(x0, x0 + bw, y0 + 52, NX))
    o.append(T(x0 + bw / 2 + 8, y0 + 76, 'one bit = 0.25 ms ÷ 1000 = 0.25 µs', 13, 'start', NX, True))
    o.append(T(x1 + 10, y0 + 24, '4 Mbit/s', 13, 'start', NX, True))
    o.append(T(20, y0 + 110, 'A sine takes every value and repeats; a digital wave jumps between two levels, one bit per interval.', 13, 'start', MUT))
    return y0 + 126, ''.join(o)
FIG[1] = (f1, 'The analog signal repeats every 4 ms, so f = 250 Hz and λ = 2 × 10⁸ ÷ 250 = 800 km in the cable. The digital signal holds each bit for 0.25 µs, so its bit rate is 1 ÷ 0.25 µs = 4 Mbit/s.',
          'Top, two cycles of a sine over 8 ms with one period of 4 ms marked; bottom, a two-level digital wave of eight bits with one bit interval of 0.25 µs marked.')


# ---- 2.2 signal falls 3 dB per km, noise stays flat ----
def f2():
    x0, x1, y0, y1 = 80, 480, 40, 290
    fx = lambda d: x0 + d / 5 * (x1 - x0)
    fy = lambda p: y1 - (p + 20) / 35 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [0, 1, 2, 3, 4, 5], [-20, -15, -10, -5, 0, 5, 10, 15], fx, fy,
              'distance along the cable (km)', 'power (dBm)', yfmt=neg)]
    o.append(L(fx(0), fy(10), fx(5), fy(-5), AC, 3))
    o.append(L(fx(0), fy(-17), fx(5), fy(-17), LV, 3, '7 4'))
    o.append(C(fx(0), fy(10), 6, AC)); o.append(C(fx(5), fy(-5), 6, AC)); o.append(C(fx(5), fy(-17), 6, LV))
    o.append(T(fx(0) + 12, fy(10) - 8, 'in: 10 mW = 10 dBm', 13, 'start', AC, True))
    o.append(T(fx(2.6), fy(3.5), '−3 dB every km', 13, 'start', AC, True))
    o.append(T(fx(0) + 12, fy(-17) - 10, 'noise 20 µW = −17 dBm', 13, 'start', LV, True))
    o.append(L(fx(5) + 14, fy(-5), fx(5) + 14, fy(-17), INK, 1.8))
    o.append(L(fx(5) + 9, fy(-5), fx(5) + 19, fy(-5), INK, 1.8)); o.append(L(fx(5) + 9, fy(-17), fx(5) + 19, fy(-17), INK, 1.8))
    o.append(T(fx(5) + 26, fy(-5) + 4, 'out: 0.316 mW = −5 dBm', 13, 'start', AC, True))
    o.append(T(fx(5) + 26, fy(-11) + 4, 'SNR = 12.0 dB', 14, 'start', INK, True))
    o.append(T(fx(5) + 26, fy(-11) + 22, '0.316 ÷ 0.020 = 15.8', 13, 'start', MUT))
    return 350, ''.join(o)
FIG[2] = (f2, 'Each kilometre costs 3 dB, so the 10 mW signal (10 dBm) falls in a straight line to 0.316 mW (−5 dBm) at 5 km, while the noise stays at 20 µW (−17 dBm). The 12.0 dB gap at the end is the SNR.',
          'A power-in-dBm plot over 5 km: a falling signal line from 10 dBm to −5 dBm and a flat dashed noise line at −17 dBm, with the 12 dB gap at 5 km marked.')


# ---- 2.3 Nyquist rate against the Shannon ceiling ----
def f3():
    x0, x1, y0, y1 = 80, 600, 40, 290
    fx = lambda L_: x0 + L_ / 64 * (x1 - x0)
    fy = lambda r: y1 - r / 40 * (y1 - y0)
    o = [axes(x0, x1, y0, y1, [2, 8, 16, 32, 48, 56, 64], [0, 10, 20, 30, 40], fx, fy,
              'number of signal levels L', 'bit rate (kbit/s)')]
    o.append(L(x0, fy(34.9), x1, fy(34.9), LV, 2.4, '7 4'))
    o.append(T(x0 + 8, fy(34.9) - 8, 'Shannon ceiling: 3000 × log₂(1 + 3162) = 34.9 kbit/s', 13, 'start', LV, True))
    o.append(P([(fx(l), fy(6 * math.log2(l))) for l in [2 + i * 0.62 for i in range(101)]], AC, 3))
    o.append(T(fx(24), fy(21), 'Nyquist: 2 × 3000 × log₂ L', 13, 'start', AC, True))
    o.append(C(fx(8), fy(18), 7, AC))
    o.append(T(fx(8) + 10, fy(18) + 22, 'L = 8: 6000 × 3 = 18.0 kbit/s', 13, 'start', AC, True))
    o.append(L(fx(56.2), fy(34.9), fx(56.2), y1, NX, 1.6, '4 3'))
    o.append(C(fx(56.2), fy(34.9), 7, NX))
    o.append(T(fx(56.2) - 10, fy(27), 'meets it at L = √3163 = 56.2', 13, 'end', NX, True))
    return 350, ''.join(o)
FIG[3] = (f3, 'For the 3 kHz voice channel more levels mean more bits, but the Nyquist curve meets the 34.9 kbit/s Shannon ceiling at about 56 levels. Eight levels give only 18.0 kbit/s, well below what the channel allows.',
          'A rising Nyquist curve 6 log₂ L kbit/s against level count L from 2 to 64, a dashed horizontal Shannon ceiling at 34.9 kbit/s, the point L = 8 at 18.0 and the crossing at L = 56.2.')


# ---- 2.4 acceptance angle outside, critical angle inside ----
def f4():
    o = []
    xf, xe, yc, hc, hd = 250, 700, 120, 40, 70
    o.append(R(xf, yc - hd, xe - xf, 2 * hd, PANEL, L2, 0, 1.4))
    o.append(R(xf, yc - hc, xe - xf, 2 * hc, ACS, AC, 0, 1.6))
    o.append(T(xe - 8, yc - hd + 20, 'cladding n₂ = 1.48', 13, 'end', MUT, True))
    o.append(T(xe - 8, yc + 30, 'core n₁ = 1.50', 13, 'end', AC, True))
    o.append(L(40, yc, xf, yc, L2, 1.2, '5 4'))
    # ray: outside at 14.13 deg, inside at 9.37 deg to the axis
    ta, ti = math.tan(math.radians(14.13)), math.tan(math.radians(9.37))
    xs = 60
    o.append(L(xs, yc + (xf - xs) * ta, xf, yc, LV, 2.6))
    xr = xf + hc / ti
    o.append(L(xf, yc, xr, yc - hc, LV, 2.6))
    o.append(L(xr, yc - hc, xe, yc - hc + (xe - xr) * ti, LV, 2.6, arrow='l'))
    # acceptance angle arc
    r = 90
    a0 = math.radians(180); a1 = math.radians(180 - 14.13)
    o.append(f'<path d="M{xf + r * math.cos(a0):.1f},{yc - r * math.sin(a0):.1f} A{r},{r} 0 0 0 {xf + r * math.cos(a1):.1f},{yc + r * math.sin(math.radians(14.13)):.1f}" style="fill:none;stroke:var(--next);stroke-width:2"/>')
    o.append(T(xf - 20, yc - 30, 'θa = 14.13°', 14, 'end', NX, True))
    o.append(T(xf - 20, yc - 12, 'outside, from the axis', 13, 'end', NX))
    # normal and critical angle at the reflection point
    o.append(L(xr, yc - hc - 30, xr, yc + hc, INK, 1.4, '4 3'))
    o.append(T(xr + 8, yc - hc - 36, 'normal', 13, 'start', MUT))
    o.append(T(xr - 10, yc + 18, 'θc = 80.63°', 14, 'end', LV, True))
    o.append(T(xr - 10, yc + 36, 'inside, from the normal', 13, 'end', LV))
    o.append(T(20, 238, 'sin θc = 1.48 ÷ 1.50 = 0.9867;   NA = √(1.50² − 1.48²) = √0.0596 = 0.2441;   θa = sin⁻¹ 0.2441', 13, 'start', INK, True))
    o.append(T(20, 260, 'A ray entering at 14.13° meets the core wall at exactly 80.63°, so it is just trapped.', 13, 'start', MUT))
    return 276, ''.join(o)
FIG[4] = (f4, 'Core 1.50 over cladding 1.48: the critical angle 80.63° is measured inside the core from the normal, and the acceptance angle 14.13° outside, from the fibre axis. A ray entering at 14.13° strikes the core wall at exactly 80.63°.',
          'A fibre drawn as a core band inside a cladding band, with a ray entering the face at 14.13° to the axis and reflecting off the core wall at 80.63° to the dashed normal.')


# ---- 2.5 one stream, four line codes ----
def f5():
    bits = [1, 0, 1, 1, 0, 0, 1]
    codes = [('NRZ-L', [+1, -1, +1, +1, -1, -1, +1], AC, None),
             ('NRZ-I', [-1, -1, +1, -1, -1, -1, +1], LV, None),
             ('Manchester', None, NX, [-1, 1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1]),
             ('AMI', [+1, 0, -1, +1, 0, 0, -1], AC, None)]
    x0, bw, A = 140, 64, 16
    o = []
    for i, b in enumerate(bits):
        x = x0 + i * bw
        o.append(T(x + bw / 2, 26, str(b), 16, fill=INK, bold=True))
    for i in range(8):
        o.append(L(x0 + i * bw, 34, x0 + i * bw, 34 + 4 * 74, LN, 1, '3 3'))
    for r, (name, lv, c, half) in enumerate(codes):
        yc = 72 + r * 74
        o.append(T(x0 - 14, yc + 5, name, 14, 'end', c, True))
        o.append(L(x0, yc, x0 + 7 * bw, yc, L2, 1))
        pts = []
        if half:
            for k, v in enumerate(half):
                pts += [(x0 + k * bw / 2, yc - v * A), (x0 + (k + 1) * bw / 2, yc - v * A)]
        else:
            for k, v in enumerate(lv):
                pts += [(x0 + k * bw, yc - v * A), (x0 + (k + 1) * bw, yc - v * A)]
        o.append(P(pts, c, 2.6))
        if name == 'NRZ-I':
            prev = +1
            for k, v in enumerate(lv):
                if v != prev:
                    o.append(C(x0 + k * bw, yc, 5, LV))
                prev = v
    o.append(T(x0 + 7 * bw + 10, 72 + 74 + 5, 'flips at each 1', 13, 'start', LV, True))
    o.append(T(x0 + 7 * bw + 10, 72 + 3 * 74 + 5, '1s alternate ±', 13, 'start', AC, True))
    o.append(T(x0 + 7 * bw + 10, 72 + 2 * 74 + 5, 'mid-bit edge', 13, 'start', NX, True))
    o.append(T(x0 + 7 * bw + 10, 72 + 5, '1 = +1, 0 = −1', 13, 'start', AC, True))
    return 34 + 4 * 74 + 14, ''.join(o)
FIG[5] = (f5, 'One 7-bit stream, 1 0 1 1 0 0 1, under four rules. NRZ-L copies each bit into the level, NRZ-I flips only at each 1 (the dots), Manchester changes in the middle of every bit, and AMI gives the 1s alternating signs and 0 V to the 0s.',
          'Four waveforms under the bits 1 0 1 1 0 0 1: NRZ-L, NRZ-I with dots at each flip, Manchester with a transition in every bit, and AMI with alternating positive and negative pulses for the ones.')


# ---- 2.6 AM: envelope and spectrum ----
def f6():
    o = []
    x0, x1, yc, s = 60, 420, 170, 6           # 1 V = 6 px
    fx = lambda t: x0 + t * (x1 - x0)           # t = fraction of one 1 kHz cycle
    env = lambda t: 10 * (1 + 0.6 * math.cos(2 * math.pi * t))
    o.append(T(20, 26, 'One cycle of the 1 kHz tone on the carrier (carrier drawn slowed down)', 14, 'start', bold=True))
    o.append(L(x0, yc, x1, yc, L2, 1.2))
    N = 24
    o.append(P([(fx(t / 1200), yc - env(t / 1200) * s * math.cos(2 * math.pi * N * t / 1200)) for t in range(1201)], AC, 1.4))
    o.append(P([(fx(t / 200), yc - env(t / 200) * s) for t in range(201)], LV, 2.4, '6 4'))
    o.append(P([(fx(t / 200), yc + env(t / 200) * s) for t in range(201)], LV, 2.4, '6 4'))
    o.append(T(x0 - 6, yc - 16 * s + 5, '16 V', 13, 'end', LV, True))
    o.append(T(fx(0.5), yc - 4 * s - 10, '4 V', 13, 'middle', LV, True))
    o.append(T(fx(0.5), yc + 16 * s + 22, 'μ = 6 ÷ 10 = 0.6: never reaches 0 V', 13, fill=LV, bold=True))
    # spectrum
    sx0, sx1, sy = 470, 700, 250
    fsx = lambda f: sx0 + (f - 98) / 4 * (sx1 - sx0)
    o.append(L(sx0, sy, sx1, sy, L2, 1.5))
    for f, a, c in ((99, 3, NX), (100, 10, AC), (101, 3, NX)):
        o.append(L(fsx(f), sy, fsx(f), sy - a * 14, c, 4))
        o.append(T(fsx(f), sy + 20, str(f), 13, fill=MUT))
    o.append(T((sx0 + sx1) / 2, sy + 40, 'frequency (kHz)', 13, fill=MUT))
    o.append(T(fsx(100), sy - 150, 'carrier', 13, fill=AC, bold=True))
    o.append(T(fsx(99), sy - 52, 'LSB', 13, fill=NX, bold=True)); o.append(T(fsx(101), sy - 52, 'USB', 13, fill=NX, bold=True))
    o.append(brace(fsx(99), fsx(101), sy + 56, NX))
    o.append(T(fsx(100), sy + 80, 'bandwidth 2 kHz', 13, fill=NX, bold=True))
    return sy + 96, ''.join(o)
FIG[6] = (f6, 'A 6 V, 1 kHz tone on a 10 V, 100 kHz carrier: the envelope swings between 16 V and 4 V because μ = 0.6, so it never touches zero. In frequency, the sidebands sit at 99 and 101 kHz, a bandwidth of 2 kHz.',
          'Left, an AM waveform whose dashed envelope swings between 16 V and 4 V over one tone cycle; right, a spectrum with the carrier at 100 kHz and sidebands at 99 and 101 kHz spanning 2 kHz.')


# ---- 2.7 one T-1 frame ----
def f7():
    o = [T(20, 26, 'One frame: one framing bit, then one 8-bit sample from each of the 24 channels', 14, 'start', bold=True)]
    x0, y, fw, sw = 30, 50, 22, 27
    o.append(R(x0, y, fw, 50, LVS, LV, 2, 1.8)); o.append(T(x0 + fw / 2, y + 31, 'F', 14, fill=LV, bold=True))
    for i in range(24):
        x = x0 + fw + i * sw
        o.append(R(x, y, sw, 50, ACS if i % 2 == 0 else PANEL, AC, 0, 1.2))
        o.append(T(x + sw / 2, y + 31, str(i + 1), 13, fill=AC, bold=True))
    xe = x0 + fw + 24 * sw
    o.append(brace(x0, xe, y + 62, INK))
    o.append(T((x0 + xe) / 2, y + 86, '1 + 24 × 8 = 193 bits, lasting 1 ÷ 8000 s = 125 µs', 14, fill=INK, bold=True))
    o.append(brace(x0 + fw, x0 + fw + sw, y - 8, AC, up=True))
    o.append(T(x0 + fw + sw + 8, y - 6, '8 bits of channel 1', 13, 'start', AC, True))
    # a row of frames
    yy = 190
    o.append(T(20, yy - 12, 'Frames repeat 8000 times a second', 14, 'start', bold=True))
    for k in range(5):
        x = 30 + k * 130
        o.append(R(x, yy, 124, 30, ACS, AC, 3, 1.4)); o.append(T(x + 62, yy + 20, f'frame {k + 1}', 13, fill=AC, bold=True))
    o.append(T(30 + 5 * 130 + 2, yy + 20, '…', 14, 'start'))
    o.append(T(20, yy + 66, 'line rate 193 × 8000 = 1,544,000 bit/s = 1.544 Mbit/s', 14, 'start', LV, True))
    o.append(T(20, yy + 90, 'each channel 8 × 8000 = 64 kbit/s;  24 × 64 + 8 framing = 1,544 kbit/s', 14, 'start', AC, True))
    return yy + 106, ''.join(o)
FIG[7] = (f7, 'A T-1 frame is one framing bit plus an 8-bit slot for each of the 24 channels, 193 bits sent every 125 µs. At 8000 frames a second that is 1.544 Mbit/s on the line and 64 kbit/s for each channel.',
          'A frame bar of a framing bit F followed by 24 numbered 8-bit slots, braced as 193 bits in 125 µs, above a row of repeating frames and the line rate 1.544 Mbit/s.')


# ---- 2.8 DSSS: spreading and despreading one bit ----
def f8():
    code = [1, -1, 1, 1, -1, 1, 1, 1, -1, -1, -1]
    o = [T(20, 26, 'Data bit 1 is sent as the 11 chips of the Barker code', 14, 'start', bold=True)]
    x0, cw = 190, 40
    rows = [('sent chips (bit × code)', code, AC, ACS), ('× receiver’s code', code, MUT, PANEL), ('= product', [1] * 11, NX, NXS)]
    for r, (name, vals, c, f) in enumerate(rows):
        y = 50 + r * 60
        o.append(T(x0 - 12, y + 26, name, 13, 'end', c, True))
        for i, v in enumerate(vals):
            o.append(R(x0 + i * cw, y, cw - 4, 40, f, c if c != MUT else L2, 4, 1.4))
            o.append(T(x0 + i * cw + (cw - 4) / 2, y + 26, '+1' if v > 0 else '−1', 14, fill=c if c != MUT else INK, bold=True))
    o.append(T(x0 + 11 * cw + 4, 50 + 2 * 60 + 26, 'sum = +11', 14, 'start', NX, True))
    o.append(T(20, 268, 'The sum +11 gives back the bit 1. Chips run 11 times faster than data:', 14, 'start'))
    o.append(T(20, 292, 'processing gain 10 log₁₀ 11 = 10.4 dB, so an in-band interferer must be about 11 times stronger.', 14, 'start', NX, True))
    return 310, ''.join(o)
FIG[8] = (f8, 'One data bit 1 goes out as the 11 Barker chips; multiplying by the same code at the receiver turns every chip into +1, and the eleven add to +11, giving back the bit. That factor of 11 is a processing gain of 10.4 dB.',
          'Three rows of eleven cells: the sent chips +1 −1 +1 +1 −1 +1 +1 +1 −1 −1 −1, the same receiver code, and their product, eleven +1s summing to +11.')


spec = make_spec(FIG)
