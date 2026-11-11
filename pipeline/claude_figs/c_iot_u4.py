"""Claude's hand-drawn figures for c-iot-u4 (Internet of Things, unit 4: prototyping with Arduino and Raspberry Pi),
one per chapter, each drawn from that chapter's worked example with its own numbers."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

FIG = {}
AFTER = {}


def resistor(x, y, w=70, c=AC):
    """horizontal zigzag resistor from x to x+w at height y"""
    n = 6; pts = [(x, y), (x + 8, y)]
    for i in range(n):
        pts.append((x + 8 + (i + 0.5) * (w - 16) / n, y + (-9 if i % 2 == 0 else 9)))
    pts += [(x + w - 8, y), (x + w, y)]
    return P(pts, c, 2.2)


def led(x, y, c=NX, s=16):
    """LED pointing right, anode at x, cathode at x+2s"""
    return (f'<path d="M{x},{y - s} L{x + 1.6 * s},{y} L{x},{y + s} Z" style="fill:var(--next-soft);stroke:{c};stroke-width:2"/>'
            + L(x + 1.6 * s, y - s, x + 1.6 * s, y + s, c, 2.5)
            + L(x + 0.6 * s, y - s - 4, x + 1.2 * s, y - s - 14, c, 1.5, arrow='x') + L(x + 1.1 * s, y - s - 2, x + 1.7 * s, y - s - 12, c, 1.5, arrow='x'))


def ground(x, y, c=INK):
    return L(x - 14, y, x + 14, y, c, 2) + L(x - 9, y + 5, x + 9, y + 5, c, 2) + L(x - 4, y + 10, x + 4, y + 10, c, 2)


# ---- 4.1 LED on Arduino pin 9 ----
def f1():
    o = []
    y = 70
    o.append(boxt(20, y - 26, 120, 52, ['Uno pin 9', 'HIGH = 5 V'], ACS, AC, 13, True))
    o.append(L(140, y, 220, y, INK, 2))
    o.append(resistor(220, y))
    o.append(T(255, y - 18, '1 kΩ', 13, bold=True))
    o.append(L(290, y, 380, y, INK, 2))
    o.append(led(380, y))
    o.append(T(395, y + 34, 'LED', 13, bold=True))
    o.append(L(406, y, 500, y, INK, 2)); o.append(L(500, y, 500, y + 30, INK, 2)); o.append(ground(500, y + 30))
    o.append(T(520, y + 40, 'GND 0 V', 13, 'start', MUT))
    o.append(L(170, y + 6, 196, y + 6, NX, 2, arrow='x')); o.append(T(183, y + 24, 'I', 14, fill=NX, bold=True))
    o.append(brace(220, 290, y + 34, AC)); o.append(T(255, y + 58, 'V_R = 5 − 2 = 3 V', 13, fill=AC, bold=True))
    o.append(brace(372, 410, y + 54, NX)); o.append(T(391, y + 78, 'V_f = 2 V', 13, fill=NX, bold=True))
    o.append(T(20, 186, 'I = 3 V ÷ 1,000 Ω = 3 mA (well under the 20 mA pin limit)', 14, 'start'))
    o.append(T(20, 208, 'P = I² × R = 0.003² × 1,000 = 0.009 W = 9 mW in the resistor', 14, 'start'))
    # blink waveform
    o.append(T(20, 250, 'digitalWrite HIGH, delay(500), LOW, delay(500): one cycle = 1,000 ms → 1 Hz', 14, 'start', bold=True))
    x0, x1, yh, yl = 70, 670, 274, 324
    fx = lambda t: x0 + t / 2000 * (x1 - x0)
    pts = []
    for c in range(2):
        t0 = c * 1000
        pts += [(fx(t0), yl), (fx(t0), yh), (fx(t0 + 500), yh), (fx(t0 + 500), yl), (fx(t0 + 1000), yl)]
    o.append(P(pts, AC, 2.5))
    o.append(T(x0 - 8, yh + 5, '5 V', 13, 'end', MUT)); o.append(T(x0 - 8, yl + 5, '0 V', 13, 'end', MUT))
    o.append(xaxis(x0, x1, yl + 6, [0, 500, 1000, 1500, 2000], fx, None, lambda v: f'{v} ms'))
    o.append(T(fx(250), yh + 20, 'LED on', 13, fill=AC)); o.append(T(fx(750), yl - 8, 'off', 13, fill=MUT))
    return 368, ''.join(o)
FIG[1] = (f1, 'With pin 9 HIGH at 5 V, the LED holds 2 V and the 1 kΩ resistor takes the other 3 V, so 3 mA flows and the resistor wastes 9 mW; 500 ms on and 500 ms off make one 1,000 ms cycle, a 1 Hz blink.',
          'A circuit from Arduino pin 9 at 5 volts through a 1 kilo-ohm resistor and an LED to ground, with 3 volts across the resistor and 2 volts across the LED; below, a square wave high for 500 ms and low for 500 ms, twice.')


# ---- 4.2 button with a pull-down, and the sketch's loop ----
def f2():
    o = [T(20, 24, 'Pressed', 15, 'start', bold=True)]
    x = 90
    o.append(T(x, 52, '5 V', 14, bold=True)); o.append(L(x, 58, x, 80, INK, 2))
    # push button
    o.append(L(x, 80, x - 18, 112, INK, 2)); o.append(C(x, 80, 3, INK)); o.append(C(x, 116, 3, INK))
    o.append(L(x, 116, x, 136, INK, 2)); o.append(T(x - 26, 104, 'button', 13, 'end', MUT))
    o.append(L(x - 18, 112, x, 116, AC, 2.5))
    o.append(C(x, 140, 5, AC)); o.append(L(x, 140, 200, 140, INK, 2))
    o.append(boxt(200, 120, 90, 40, ['pin 2'], ACS, AC, 13, True)); o.append(T(304, 145, 'reads HIGH', 13, 'start', AC, True))
    # pull-down
    o.append(L(x, 140, x, 160, INK, 2))
    vr = [(x, 160), (x, 166)] + [(x + (-9 if i % 2 == 0 else 9), 166 + (i + 0.5) * 8) for i in range(6)] + [(x, 214), (x, 220)]
    o.append(P(vr, AC, 2.2)); o.append(T(x + 18, 196, '10 kΩ pull-down', 13, 'start', bold=True))
    o.append(L(x, 220, x, 236, INK, 2)); o.append(ground(x, 236))
    o.append(L(x - 30, 150, x - 30, 214, NX, 2, arrow='x'))
    o.append(T(x - 38, 186, 'I', 14, 'end', NX, True))
    o.append(T(20, 280, 'I = 5 V ÷ 10,000 Ω = 0.5 mA', 14, 'start', NX, True))
    o.append(T(20, 302, 'Released: no 5 V path, the resistor holds pin 2 at 0 V, I = 0', 13, 'start', MUT))
    # sketch flow
    fx0 = 430
    o.append(boxt(fx0, 14, 270, 50, ['setup(), once', 'pinMode(2, INPUT); pinMode(13, OUTPUT)'], PANEL, AC, 13, True))
    o.append(L(fx0 + 135, 66, fx0 + 135, 88, AC, 2, arrow='n'))
    o.append(boxt(fx0 + 35, 92, 200, 46, ['loop(): digitalRead(2)', 'HIGH?'], ACS, AC, 13, True))
    o.append(L(fx0 + 85, 140, fx0 + 50, 176, AC, 2, arrow='n')); o.append(T(fx0 + 54, 160, 'yes', 13, 'end', AC, True))
    o.append(L(fx0 + 185, 140, fx0 + 220, 176, L2, 2, arrow='m')); o.append(T(fx0 + 214, 160, 'no', 13, 'start', MUT, True))
    o.append(boxt(fx0, 180, 120, 50, ['pin 13 HIGH', 'LED on'], NXS, NX, 13, True))
    o.append(boxt(fx0 + 150, 180, 120, 50, ['pin 13 LOW', 'LED off'], PANEL, L2, 13, True))
    o.append(P([(fx0 + 60, 232), (fx0 + 60, 252), (fx0 + 290, 252), (fx0 + 290, 115), (fx0 + 238, 115)], L2, 1.8))
    o.append(L(fx0 + 250, 115, fx0 + 240, 115, L2, 1.8, arrow='m'))
    o.append(L(fx0 + 210, 232, fx0 + 210, 252, L2, 1.8))
    o.append(T(fx0 + 135, 274, 'repeat forever', 13, fill=MUT))
    return 318, ''.join(o)
FIG[2] = (f2, 'Pressing the button joins pin 2 to 5 V, so it reads HIGH while 0.5 mA flows through the 10 kΩ pull-down; released, the resistor holds pin 2 at 0 V. The loop reads pin 2 and copies it to the LED on pin 13.',
          'Left, a circuit: 5 volts through a push button to pin 2, with a 10 kilo-ohm resistor from pin 2 to ground carrying 0.5 mA. Right, a flow: setup once, then loop reads pin 2; if HIGH the LED on pin 13 is on, otherwise off, and the loop repeats.')


# ---- 4.3 LED resistor for a 3.3 V Raspberry Pi pin ----
def f3():
    o = []
    y = 60
    o.append(boxt(20, y - 26, 130, 52, ['Pi GPIO high', '3.3 V'], ACS, AC, 13, True))
    o.append(L(150, y, 230, y, INK, 2)); o.append(resistor(230, y)); o.append(T(265, y - 18, 'R = ?', 13, bold=True))
    o.append(L(300, y, 390, y, INK, 2)); o.append(led(390, y))
    o.append(L(416, y, 500, y, INK, 2)); o.append(L(500, y, 500, y + 26, INK, 2)); o.append(ground(500, y + 26))
    o.append(brace(230, 300, y + 34, AC)); o.append(T(265, y + 58, '3.3 − 2.0 = 1.3 V', 13, fill=AC, bold=True))
    o.append(brace(382, 420, y + 34, NX)); o.append(T(401, y + 58, '2.0 V', 13, fill=NX, bold=True))
    o.append(T(530, y + 4, 'target 5 mA', 13, 'start', MUT))
    o.append(T(20, 168, 'Exact: R = 1.3 V ÷ 0.005 A = 260 Ω, which is not a value you can buy.', 14, 'start'))
    # standard values on a number line
    x0, x1, yl = 60, 660, 236
    fx = lambda r: x0 + (r - 200) / 200 * (x1 - x0)
    o.append(L(x0, yl, x1, yl, L2, 1.5))
    for r in (220, 270, 330, 390):
        o.append(C(fx(r), yl, 8, AC if r != 270 else NX))
        o.append(T(fx(r), yl + 28, f'{r} Ω', 13, fill=NX if r == 270 else MUT, bold=r == 270))
    o.append(L(fx(260), yl - 30, fx(260), yl - 4, LV, 2, arrow='l'))
    o.append(T(fx(260), yl - 36, '260 Ω exact', 13, fill=LV, bold=True))
    o.append(T(x1, yl - 18, 'standard (E12) values', 13, 'end', MUT))
    o.append(T(20, 304, 'Use 270 Ω, the nearest standard value: I = 1.3 V ÷ 270 Ω = 4.81 mA (just under 5 mA).', 14, 'start', NX, True))
    return 320, ''.join(o)
FIG[3] = (f3, 'A 3.3 V GPIO pin and a 2.0 V red LED leave 1.3 V for the resistor, so 5 mA needs 260 Ω; that is not a standard value, so 270 Ω is used and the current becomes 4.81 mA.',
          'A circuit from a 3.3 volt Pi pin through a resistor and LED to ground with 1.3 volts and 2.0 volts marked; below, a line of standard resistor values 220, 270, 330, 390 ohms with 260 marked between 220 and 270 and 270 chosen.')


# ---- 4.4 one LM35 reading over SPI ----
def f4():
    xs = {'LM35': 100, 'MCP3008 (ch 0)': 340, 'Pi, Python script': 590}
    o = []
    for n, x in xs.items():
        o.append(boxt(x - 85, 14, 170, 38, [n], LVS if n == 'LM35' else ACS, LV if n == 'LM35' else AC, 14, True))
        o.append(L(x, 54, x, 214, L2, 1.5, '5 5'))
    def msg(a, b, y, lab, dash=None, c=AC, ar='n'):
        xa, xb = xs[a], xs[b]; d = 1 if xb > xa else -1
        return L(xa + d * 3, y, xb - d * 6, y, c, 2.2, dash, ar) + Tb((xa + xb) / 2, y - 9, lab, 13)
    o.append(msg('LM35', 'MCP3008 (ch 0)', 84, '20 °C × 10 mV/°C = 0.200 V', c=LV, ar='l'))
    o.append(msg('Pi, Python script', 'MCP3008 (ch 0)', 124, 'SPI: read channel 0'))
    o.append(msg('MCP3008 (ch 0)', 'Pi, Python script', 164, 'raw_value = 62', '6 4'))
    o.append(boxt(440, 226, 270, 52, ['V_in = 62 ÷ 1023 × 3.3', '= 0.200 V'], PANEL, AC, 14, True))
    o.append(L(590, 280, 590, 300, AC, 2, arrow='n'))
    o.append(boxt(440, 304, 270, 52, ['T = 0.200 V ÷ 0.010 V/°C', '= 20.0 °C'], NXS, NX, 14, True))
    o.append(T(20, 250, '10-bit ADC: codes 0 … 1023,', 13, 'start', MUT))
    o.append(T(20, 270, 'so full scale is 1023 = 2¹⁰ − 1.', 13, 'start', MUT))
    o.append(T(20, 304, 'The Pi has no analog input:', 13, 'start', MUT))
    o.append(T(20, 324, 'the MCP3008 does the conversion.', 13, 'start', MUT))
    return 370, ''.join(o)
FIG[4] = (f4, 'The LM35 puts 0.200 V on channel 0 at 20 °C, the script asks the MCP3008 for that channel over SPI and gets code 62, then converts 62 ÷ 1023 × 3.3 V back to 0.200 V and 0.200 ÷ 0.010 to 20.0 °C.',
          'A sequence diagram with LM35, MCP3008 and the Pi script: 0.200 volts goes to channel 0, the Pi requests channel 0 over SPI, code 62 comes back; two boxes convert it to 0.200 volts and 20.0 degrees.')


# ---- 4.5 HC-SR04 echo to distance ----
def f5():
    o = []
    x0, x1 = 100, 640
    fx = lambda cm: x0 + cm / 25 * (x1 - x0)
    o.append(boxt(20, 40, 76, 70, ['HC-SR04'], ACS, AC, 13, True))
    obj = fx(9.947)
    o.append(R(obj, 30, 18, 90, 'var(--line)', L2, 2, 1.5)); o.append(T(obj + 9, 140, 'object', 13, fill=MUT))
    o.append(L(x0, 62, obj - 4, 62, AC, 2.2, arrow='n')); o.append(T((x0 + obj) / 2, 54, 'out', 13, fill=AC))
    o.append(L(obj - 2, 90, x0 + 4, 90, AC, 2.2, '6 4', 'n')); o.append(T((x0 + obj) / 2, 108, 'back', 13, fill=AC))
    o.append(L(fx(20), 24, fx(20), 140, NX, 2, '6 4')); o.append(T(fx(20) + 6, 36, '20 cm alarm line', 13, 'start', NX, True))
    o.append(xaxis(x0, x1, 156, [0, 5, 10, 15, 20, 25], fx, 'distance from the sensor (cm)'))
    # echo pulse
    o.append(T(20, 236, 'Echo pin HIGH for the round trip:', 14, 'start', bold=True))
    o.append(P([(40, 290), (110, 290), (110, 256), (430, 256), (430, 290), (560, 290)], AC, 2.5))
    o.append(T(270, 280, '580 µs = 5.80 × 10⁻⁴ s', 14, bold=True))
    o.append(T(20, 326, 'round trip = 343 m/s × 5.80 × 10⁻⁴ s = 0.19894 m', 14, 'start'))
    o.append(T(20, 350, 'one way = 0.19894 ÷ 2 = 0.09947 m ≈ 9.95 cm', 14, 'start', AC, True))
    o.append(T(20, 374, '9.95 cm < 20 cm → the buzzer sounds', 14, 'start', NX, True))
    return 390, ''.join(o)
FIG[5] = (f5, 'The echo pin stays HIGH for 580 µs while the sound goes out and back, a round trip of 343 × 0.000580 = 0.19894 m; half of it puts the object 9.95 cm away, inside the 20 cm alarm line, so the buzzer sounds.',
          'An ultrasonic sensor sends a pulse to an object at 9.95 centimetres and it returns, on a distance scale to 25 centimetres with a dashed alarm line at 20; below, the echo pulse 580 microseconds wide and the distance working.')


# ---- 4.6 NodeMCU wake and deep sleep ----
def f6():
    o = [T(20, 24, 'Current over two 60 s cycles (drawn to scale)', 14, 'start', MUT)]
    x0, x1, y0, y1 = 70, 680, 72, 240
    fx = lambda t: x0 + t / 120 * (x1 - x0)
    fy = lambda i: y1 - i / 80 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 20, 40, 60, 80, 100, 120], [0, 20, 40, 60, 80], fx, fy, 'time (s)', 'current (mA)'))
    for c in (0, 60):
        o.append(R(fx(c), fy(80), fx(2) - fx(0), fy(0) - fy(80), ACS, AC, 1, 2))
    o.append(L(fx(0), fy(2.686), fx(120), fy(2.686), NX, 2.5, '8 5'))
    o.append(Tb(fx(30), fy(2.686) - 12, 'average 2.686 mA', 14, 'middle', NX, True))
    o.append(Tb(fx(2) + 8, fy(70), 'awake 2 s at 80 mA', 13, 'start', AC, True))
    o.append(Tb(fx(70), fy(18), 'asleep 58 s at 20 µA = 0.020 mA (too small to see)', 13, 'start', MUT))
    o.append(T(20, 310, 'Charge per cycle: awake 80 × 2 = 160 mA·s, asleep 0.020 × 58 = 1.16 mA·s', 14, 'start'))
    o.append(T(20, 334, 'I_avg = (160 + 1.16) ÷ 60 = 161.16 ÷ 60 = 2.686 mA, about one thirtieth of 80 mA', 14, 'start', NX, True))
    o.append(T(20, 358, 'Here the 2 s awake burst sets the average: shorten it to save the battery.', 13, 'start', MUT))
    return 372, ''.join(o)
FIG[6] = (f6, 'Each 60 s cycle has 2 s awake at 80 mA (160 mA·s) and 58 s asleep at 0.020 mA (1.16 mA·s), so the average is 161.16 ÷ 60 = 2.686 mA, about one thirtieth of the awake current.',
          'A to-scale current plot over 120 seconds: two narrow 80 mA blocks of 2 seconds each, a sleep floor too small to see, and a dashed average line at 2.686 mA.')


# ---- 4.7 water tank level and pump rule ----
def f7():
    o = []
    tx, tw, ty, th = 80, 200, 50, 300
    fy = lambda h: ty + th - h / 100 * th
    o.append(R(tx, fy(30), tw, fy(0) - fy(30), ACS, 'none', 0, 0))
    o.append(P([(tx, ty), (tx, ty + th), (tx + tw, ty + th), (tx + tw, ty)], INK, 2.5))
    o.append(L(tx, fy(30), tx + tw, fy(30), AC, 2.5))
    o.append(boxt(tx + 60, ty - 30, 80, 26, ['sensor'], LVS, LV, 13, True))
    o.append(L(tx + 100, ty - 2, tx + 100, fy(30) - 4, LV, 2, '6 4', 'l'))
    o.append(Tb(tx + 108, fy(65), 'd = 70 cm', 14, 'start', LV, True))
    o.append(Tb(tx + tw / 2, fy(15), 'h = 100 − 70 = 30 cm', 14, 'middle', AC, True))
    for h, lab, c in ((90, 'stop at h ≥ 90 cm', L2), (30, 'start at h ≤ 30 cm', NX)):
        o.append(L(tx + tw, fy(h), tx + tw + 40, fy(h), c, 2, '5 4'))
        o.append(T(tx + tw + 46, fy(h) + 5, lab, 13, 'start', c if c == NX else MUT, True))
    o.append(T(tx - 8, ty + 5, '100', 13, 'end', MUT)); o.append(T(tx - 8, ty + th + 5, '0 cm', 13, 'end', MUT))
    o.append(T(tx + tw / 2, ty + th + 24, 'base area 1 m² = 10,000 cm²', 13, fill=MUT))
    x = 470
    o.append(T(x, 120, 'Volume = 30 cm × 10,000 cm²', 14, 'start'))
    o.append(T(x, 142, '= 300,000 cm³ ÷ 1,000 = 300 L', 14, 'start', AC, True))
    o.append(T(x, 186, 'Rule: start when h ≤ 30 cm', 14, 'start'))
    o.append(T(x, 208, '30 ≤ 30 is true →', 14, 'start'))
    o.append(boxt(x, 220, 150, 44, ['pump ON'], NXS, NX, 15, True))
    o.append(T(x, 290, 'With h < 30 instead, 30 < 30', 13, 'start', MUT))
    o.append(T(x, 308, 'is false and the pump stays off.', 13, 'start', MUT))
    return 384, ''.join(o)
FIG[7] = (f7, 'The sensor at the top of the 100 cm tank reads d = 70 cm, so the water stands h = 30 cm deep, 300 L over a 1 m² base; the start rule h ≤ 30 cm is true at exactly 30 cm, so the pump starts.',
          'A tank 100 centimetres tall with a sensor at the top measuring 70 centimetres down to water 30 centimetres deep; dashed marks at 30 for start and 90 for stop; text gives 300 litres and pump on.')


TEXT = {}


def spec(k):
    fn, cap, aria = FIG[k]
    h, body = fn()
    d = {'caption': cap, 'spec': {'type': 'svg', 'h': h, 'body': body, 'aria': aria}}
    if k in AFTER: d['after_section'] = AFTER[k]
    return d


def text_fixes(k):
    return TEXT.get(k, [])
