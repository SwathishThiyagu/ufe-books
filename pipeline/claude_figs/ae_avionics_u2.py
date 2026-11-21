"""Claude's hand-drawn figures for ae-avionics-u2 (Hydraulic, pneumatic and environmental systems), one per chapter, drawn
from each chapter's own worked example and numbers. Colours are the shell's CSS variables."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}


def sub(base, s, size=14):
    return f'{base}<tspan dy="4" font-size="{size - 3}">{s}</tspan><tspan dy="-4">&#8203;</tspan>'


def arrow_down(x, y1, y2, c=AC, w=2, a='n'):
    return L(x, y1, x, y2, c, w, arrow=a)


# ---- 2.1 hydraulic circuit with the worked examples' accumulator and actuator ----
def f1():
    o = []
    o.append(boxt(20, 40, 130, 60, ['Reservoir', 'low pressure'], PANEL, L2, 14, True))
    o.append(L(150, 70, 186, 70, AC, 2.5, arrow='n'))
    o.append(boxt(190, 40, 120, 60, ['Engine-driven', 'pump'], ACS, AC, 14, True))
    o.append(L(310, 70, 346, 70, AC, 2.5, arrow='n'))
    o.append(boxt(350, 45, 80, 50, ['Filter'], PANEL, AC, 14))
    o.append(L(430, 70, 655, 70, AC, 2.5))
    o.append(T(560, 60, 'pressure line, 3000 psi', 13, 'middle', AC))
    # accumulator hanging below the pressure line
    ax = 470
    o.append(L(ax, 70, ax, 106, AC, 2.5))
    o.append(R(ax - 34, 106, 68, 104, PANEL, AC, 28))
    o.append(L(ax - 34, 160, ax + 34, 160, NX, 3))
    o.append(T(ax, 140, 'N₂', 15, 'middle', NX, True))
    o.append(T(ax, 188, 'fluid', 13, 'middle', AC))
    o.append(T(ax - 46, 124, 'Accumulator 4.0 L', 14, 'end', INK, True))
    o.append(T(ax - 46, 146, 'precharge 1000 psi', 13, 'end', MUT))
    o.append(T(ax - 46, 166, 'at 3000 psi: 2.67 L fluid', 13, 'end', MUT))
    o.append(T(ax - 46, 186, 'usable to 1500 psi: 1.33 L', 13, 'end', NX, True))
    # selector valve
    o.append(L(655, 70, 655, 104, AC, 2.5, arrow='n'))
    o.append(boxt(600, 108, 110, 50, ['Selector', 'valve'], PANEL, AC, 14, True))
    # line from the selector to the cap end of the actuator
    cy = 290
    o.append(P([(655, 158), (655, 232), (300, 232), (300, cy - 40)], AC, 2.5))
    o.append(L(300, cy - 44, 300, cy - 38, AC, 2.5, arrow='n'))
    # actuator
    o.append(R(260, cy - 36, 360, 72, PANEL, L2, 6))
    o.append(R(470, cy - 34, 18, 68, ACS, AC, 3))
    o.append(R(488, cy - 10, 212, 20, L2, L2, 2))
    o.append(T(365, cy + 6, 'full piston area', 14, 'middle', AC, True))
    o.append(T(365, cy + 26, 'Ø 5 cm', 13, 'middle', AC))
    o.append(T(554, cy - 16, 'annulus', 13, 'middle', NX))
    o.append(T(662, cy - 18, 'rod Ø 2 cm', 13, 'middle', MUT))
    # rod-side port back to the reservoir
    o.append(P([(600, cy + 36), (600, 356), (85, 356), (85, 104)], L2, 2, '6 4'))
    o.append(L(85, 112, 85, 104, L2, 2, arrow='m'))
    o.append(T(95, 340, 'return to the reservoir (through the selector)', 13, 'start', MUT))
    o.append(T(380, 394, 'extend: F = p × A = 2.07 × 10⁷ × 1.963 × 10⁻³ = 40.6 kN', 14, 'middle', AC, True))
    o.append(T(380, 418, 'retract (annulus 1.649 × 10⁻³ m²): 34.1 kN', 14, 'middle', NX, True))
    return 432, ''.join(o)

FIG[1] = (f1, 'The worked examples on one circuit: a pump fills a 4.0 L accumulator to 3000 psi but only 1.33 L of its fluid is usable '
              'down to 1500 psi, and at 207 bar the 5 cm actuator pushes 40.6 kN out but only 34.1 kN back, because the rod takes area.',
          'Hydraulic circuit: reservoir, engine-driven pump and filter feed a 3000 psi pressure line. An accumulator of 4.0 litres hangs '
          'below the line with nitrogen above the fluid, precharge 1000 psi, 1.33 litres usable. A selector valve sends fluid to an '
          'actuator of 5 centimetre bore that extends with 40.6 kilonewtons and retracts with 34.1; fluid returns to the reservoir.')


# ---- 2.2 bleed air system and the emergency bottle ----
def f2():
    o = []
    o.append(R(20, 30, 150, 150, PANEL, L2, 10))
    o.append(T(95, 54, 'Engine', 14, 'middle', INK, True))
    o.append(boxt(34, 70, 122, 36, ['LP port'], ACS, AC, 13))
    o.append(boxt(34, 126, 122, 36, ['HP port'], NXS, NX, 13))
    o.append(T(95, 200, 'HP valve opens only', 13, 'middle', NX))
    o.append(T(95, 218, 'at low engine power', 13, 'middle', NX))
    o.append(L(156, 88, 200, 88, AC, 2.5))
    o.append(T(178, 80, 'check', 13, 'middle', MUT))
    o.append(P([(156, 144), (200, 144), (200, 92)], NX, 2.5))
    o.append(L(200, 88, 226, 88, AC, 2.5, arrow='n'))
    o.append(boxt(230, 62, 110, 52, ['Precooler', 'fan air'], PANEL, AC, 13, True))
    o.append(L(340, 88, 366, 88, AC, 2.5, arrow='n'))
    o.append(boxt(370, 62, 110, 52, ['PRV', 'few 100 kPa'], ACS, AC, 13, True))
    o.append(L(480, 88, 700, 88, AC, 3))
    o.append(T(590, 78, 'manifold', 14, 'middle', AC, True))
    # APU joining downstream
    o.append(boxt(500, 150, 110, 46, ['APU bleed', 'valve + check'], PANEL, L2, 13))
    o.append(L(555, 150, 555, 92, L2, 2.5, '6 4', arrow='m'))
    # users
    o.append(L(650, 88, 650, 128, AC, 2, arrow='n'))
    o.append(T(650, 146, 'packs, anti-ice,', 13, 'middle', INK))
    o.append(T(650, 164, 'engine start', 13, 'middle', INK))
    # emergency bottle panel
    y0 = 250
    o.append(R(20, y0, 680, 120, PANEL, L2, 10, 1.5))
    o.append(T(36, y0 + 26, 'Emergency gear bottle (Boyle’s law)', 14, 'start', INK, True))
    o.append(R(60, y0 + 42, 70, 62, NXS, NX, 18))
    o.append(T(95, y0 + 70, '2.5 L', 14, 'middle', NX, True))
    o.append(T(95, y0 + 90, '200 bar', 13, 'middle', NX))
    o.append(L(140, y0 + 73, 250, y0 + 73, NX, 2.5, arrow='x'))
    o.append(R(260, y0 + 42, 190, 62, PANEL, AC, 8))
    o.append(T(355, y0 + 68, 'bottle + lines + actuators', 13, 'middle', INK))
    o.append(T(355, y0 + 90, '12.0 L at 41.7 bar', 14, 'middle', AC, True))
    o.append(T(470, y0 + 64, '200 × 2.5 ÷ 12.0 = 41.7 bar', 14, 'start', INK))
    o.append(T(470, y0 + 88, 'need 30 bar: 11.7 bar spare', 14, 'start', LV, True))
    return 384, ''.join(o)

FIG[2] = (f2, 'Bleed air leaves the LP port (the HP port only at low power), is cooled in the precooler and regulated by the PRV; the APU '
              'joins the manifold downstream. Below, the worked example’s emergency bottle: 2.5 L at 200 bar spreads into 12.0 L at 41.7 bar.',
          'Top: engine LP and HP ports with a check valve, then the precooler cooled by fan air, the pressure regulating valve and the '
          'manifold feeding packs, anti-ice and engine start; APU bleed joins the manifold after the regulator. Bottom: an emergency '
          'nitrogen bottle of 2.5 litres at 200 bar discharging into 12 litres in all, reaching 41.7 bar, 11.7 bar above the 30 bar needed.')


# ---- 2.3 oleo strut, static and compressed ----
def f3():
    o = []

    def strut(x, gas_h, lab1, lab2, lab3, col, orifice_label):
        top = 40
        o.append(R(x, top, 90, 250, PANEL, L2, 8))
        o.append(R(x + 4, top + 4, 82, gas_h, NXS, NXS, 4, 0))
        o.append(T(x + 45, top + 4 + gas_h / 2 + 5, 'N₂', 15, 'middle', NX, True))
        o.append(R(x + 4, top + 4 + gas_h, 82, 120, ACS, ACS, 4, 0))
        o.append(T(x + 45, top + 4 + gas_h + 26, 'oil', 14, 'middle', AC, True))
        oy = top + 4 + gas_h + 50
        o.append(L(x + 4, oy, x + 38, oy, INK, 3)); o.append(L(x + 52, oy, x + 86, oy, INK, 3))
        if orifice_label: o.append(T(x + 100, oy + 5, 'orifice plate', 13, 'start', MUT))
        py = top + 4 + gas_h + 120
        o.append(R(x + 14, py, 62, 344 - py, PANEL, AC, 4))
        o.append(T(x + 45, py + 26, 'piston', 13, 'middle', AC))
        o.append(f'<circle cx="{x + 45}" cy="370" r="24" style="fill:var(--panel);stroke:var(--line2);stroke-width:3"/>')
        o.append(T(x + 110, 262, lab1, 14, 'start', col, True))
        o.append(T(x + 110, 286, lab2, 14, 'start', INK))
        o.append(T(x + 110, 310, lab3, 14, 'start', INK))

    strut(60, 110, 'Static, on the ramp', 'gas 4.0 L at 86.2 bar', 'F = 270.8 kN per leg', AC, True)
    strut(390, 44, 'Touchdown stroke', 'gas 1.6 L at 215.5 bar', 'F = 677 kN (2.5 × static)', NX, False)
    o.append(L(200, 84, 376, 84, NX, 2.5, arrow='x'))
    o.append(T(288, 72, 'strut closes', 13, 'middle', NX))
    o.append(T(40, 418, 'piston Ø 0.20 m, A = 0.0314 m²; the gas keeps pV constant: 4.0 × 86.2 = 1.6 × 215.5 = 345', 13, 'start', MUT))
    return 432, ''.join(o)

FIG[3] = (f3, 'The worked example’s main oleo: on the ramp its nitrogen is at 86.2 bar and carries 270.8 kN; squeezed from 4.0 L to 1.6 L at '
              'touchdown it reaches 215.5 bar and pushes with 677 kN, while oil forced through the orifice turns the bounce into heat.',
          'Two cut-away oleo struts side by side. Left, static: a tall nitrogen space above the oil, gas 4.0 litres at 86.2 bar, force 270.8 '
          'kilonewtons per leg. Right, compressed at touchdown: a short nitrogen space, gas 1.6 litres at 215.5 bar, force 677 kilonewtons. '
          'Each strut shows the oil, the orifice plate and the piston.')


# ---- 2.4 fuel path and oil loop ----
def f4():
    o = []
    xs = [20, 150, 280, 410, 540]
    labs = [['Tank', 'boost pump'], ['Fuel-oil', 'heat exch.'], ['LP filter', 'bypass'], ['HP pump', 'gearbox'], ['Metering', 'unit']]
    for i, (x, lab) in enumerate(zip(xs, labs)):
        o.append(boxt(x, 40, 110, 56, lab, ACS if i == 4 else PANEL, AC, 13, True))
        if i: o.append(L(xs[i - 1] + 110, 68, x - 4, 68, AC, 2.5, arrow='n'))
    o.append(L(650, 68, 690, 68, AC, 2.5))
    o.append(L(690, 68, 690, 132, AC, 2.5, arrow='n'))
    o.append(T(690, 152, 'nozzles', 13, 'middle', INK))
    o.append(T(540, 118, 'FADEC sets the flow', 13, 'start', AC))
    o.append(T(240, 152, '1200 kg/h ÷ 0.8 kg/L = 1500 L/h = 0.42 L/s', 14, 'start', AC, True))
    # oil loop below, sharing the heat exchanger
    o.append(boxt(150, 210, 110, 56, ['Oil tank'], PANEL, NX, 13, True))
    o.append(boxt(330, 210, 120, 56, ['Pressure', 'pump, filter'], PANEL, NX, 13))
    o.append(boxt(520, 210, 160, 56, ['Bearings', '80 → 140 °C'], NXS, NX, 13, True))
    o.append(L(260, 238, 326, 238, NX, 2.5, arrow='x'))
    o.append(L(450, 238, 516, 238, NX, 2.5, arrow='x'))
    o.append(P([(600, 266), (600, 320), (205, 320), (205, 270)], NX, 2.5))
    o.append(T(400, 342, 'scavenge pumps, chip detector, back via the cooler', 13, 'middle', NX))
    o.append(L(205, 96, 205, 206, L2, 2, '6 4'))
    o.append(T(214, 192, 'oil heat warms the fuel', 13, 'start', MUT))
    o.append(T(588, 300, 'ΔT = 60 ÷ (0.5 × 2.0) = 60 K', 14, 'end', NX, True))
    return 360, ''.join(o)

FIG[4] = (f4, 'Fuel runs from the tank through the fuel-oil heat exchanger, filter and HP pump to the metering unit; the worked example’s '
              '1200 kg/h is 0.42 L/s. The oil loop below picks up 60 kW at the bearings, 80 → 140 °C, and gives heat to the fuel.',
          'Top row: tank and boost pump, fuel-oil heat exchanger, low-pressure filter with bypass, high-pressure pump and metering unit, then '
          'the nozzles; 1200 kilograms per hour is 0.42 litres per second. Bottom: oil tank, pressure pump and filter, bearings where the oil '
          'rises from 80 to 140 degrees, and the scavenge return; a dashed link shows the oil heating the fuel in the heat exchanger.')


# ---- 2.5 N2 against time during the start ----
def f5():
    o = []
    x0, x1, y0, y1 = 70, 470, 40, 300
    fx = lambda t: x0 + t / 35 * (x1 - x0)
    fy = lambda n: y1 - n / 70 * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 10, 20, 30], [0, 20, 40, 60], fx, fy, 'time from cranking (s)', 'N2 (%)'))
    pts = [(fx(0), fy(0)), (fx(13.75), fy(22)), (fx(25.42), fy(50))]
    o.append(P(pts, AC, 3))
    o.append(P([(fx(25.42), fy(50)), (fx(29), fy(57)), (fx(34), fy(60))], AC, 2.5, '6 4'))
    for t, n, lab, col, dx, anchor in ((10, 16, 'ignition 16 % at 10.0 s', LV, 10, 'start'), (13.75, 22, 'fuel 22 % at 13.75 s', NX, -10, 'end'),
                                       (25.42, 50, 'cut-out 50 % at 25.4 s', AC, -12, 'end')):
        o.append(L(fx(t), fy(n), fx(t), y1, col, 1.5, '4 4'))
        o.append(C(fx(t), fy(n), 6, col))
        o.append(Tb(fx(t) + dx, fy(n) + (18 if anchor == 'start' else -10), lab, 13, anchor, col, True))
    o.append(T(fx(6.5) - 8, fy(10.4) - 12, '1.6 %/s', 13, 'end', MUT))
    o.append(T(fx(20.5), fy(30), '2.4 %/s', 13, 'start', MUT))
    o.append(T(fx(30), fy(63), 'to idle', 13, 'middle', MUT))
    # exciter panel
    o.append(R(500, 50, 200, 170, PANEL, L2, 8, 1.5))
    o.append(T(516, 76, 'Exciter spark', 14, 'start', INK, True))
    o.append(T(516, 102, 'C = 4.0 µF, V = 2.0 kV', 13, 'start', INK))
    o.append(T(516, 126, 'E = ½CV² = 8.0 J', 14, 'start', LV, True))
    o.append(T(516, 150, '1 spark/s → 8.0 W', 13, 'start', INK))
    o.append(T(516, 180, '20 J needs 3.16 kV', 13, 'start', MUT))
    o.append(T(516, 202, '(energy goes with V²)', 13, 'start', MUT))
    return 350, ''.join(o)

FIG[5] = (f5, 'The worked example’s start: N2 climbs at 1.6 %/s on the starter, the igniters spark from 10.0 s, fuel arrives at 13.75 s and '
              'light-off steepens the climb to 2.4 %/s until cut-out at 50 % (25.4 s). The panel works the exciter’s 8.0 J spark.',
          'Graph of N2 in percent against time in seconds. A line rises from zero to 22 percent at 13.75 seconds, then more steeply to 50 '
          'percent at 25.4 seconds, then dashed to idle near 60 percent. Markers: ignition at 16 percent and 10 seconds, fuel at 22 percent '
          'and 13.75 seconds, starter cut-out at 50 percent and 25.4 seconds. Side panel: a 4 microfarad capacitor at 2 kilovolts stores 8 joules.')


# ---- 2.6 cabin and outside pressure, and the cooling turbine ----
def f6():
    o = []
    # fuselage section
    cx, cy, r = 150, 190, 120
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" style="fill:var(--accent-soft);stroke:var(--accent);stroke-width:3"/>')
    o.append(T(cx, cy - 34, 'cabin at 8000 ft', 14, 'middle', AC, True))
    o.append(T(cx, cy - 10, '75.3 kPa', 16, 'middle', AC, True))
    o.append(T(cx, cy + 22, 'Δp = 51.5 kPa', 14, 'middle', NX, True))
    o.append(T(cx, cy + 44, '(7.47 psi)', 13, 'middle', NX))
    for a in (30, 90, 150, 210, 270, 330):
        t = math.radians(a)
        o.append(L(cx + (r - 28) * math.cos(t), cy + (r - 28) * math.sin(t), cx + (r + 22) * math.cos(t), cy + (r + 22) * math.sin(t), NX, 2, arrow='x'))
    o.append(T(cx, 36, 'outside at 35 000 ft: 23.8 kPa', 14, 'middle', MUT))
    o.append(T(cx, 352, 'door 1.2 m²: F = 51 500 × 1.2 = 61.8 kN', 14, 'middle', INK, True))
    # turbine panel
    x0 = 330
    o.append(R(x0, 60, 370, 250, PANEL, L2, 10, 1.5))
    o.append(T(x0 + 16, 86, 'Cooling turbine of the pack', 14, 'start', INK, True))
    o.append(f'<polygon points="{x0 + 140},120 {x0 + 230},100 {x0 + 230},230 {x0 + 140},210" style="fill:var(--live-soft);stroke:var(--live);stroke-width:2.5"/>')
    o.append(T(x0 + 185, 170, 'turbine', 14, 'middle', LV, True))
    o.append(L(x0 + 30, 165, x0 + 136, 165, AC, 2.5, arrow='n'))
    o.append(T(x0 + 20, 140, '300 kPa', 14, 'start', AC, True))
    o.append(T(x0 + 20, 196, '40 °C', 14, 'start', AC, True))
    o.append(L(x0 + 234, 165, x0 + 290, 165, LV, 2.5, arrow='l'))
    o.append(T(x0 + 296, 140, '80 kPa', 14, 'start', LV, True))
    o.append(T(x0 + 296, 196, '−38.8 °C', 14, 'start', LV, True))
    o.append(L(x0 + 185, 232, x0 + 185, 262, NX, 3, '6 4'))
    o.append(T(x0 + 185, 284, 'shaft work drives the compressor', 13, 'middle', NX))
    o.append(T(x0 + 185, 304, 'ideal −58.5 °C; real (η = 0.80) −38.8 °C', 13, 'middle', MUT))
    return 372, ''.join(o)

FIG[6] = (f6, 'The two worked examples: the cabin held at 75.3 kPa while the outside is at 23.8 kPa gives Δp = 51.5 kPa and 61.8 kN on a '
              '1.2 m² door; in the pack, air expanding from 300 kPa and 40 °C to 80 kPa leaves the turbine at −38.8 °C.',
          'Left: a fuselage cross-section at 75.3 kilopascals, cabin altitude 8000 feet, with arrows pushing outward; outside air at 35 000 '
          'feet is 23.8 kilopascals, so the differential is 51.5 kilopascals and a 1.2 square metre door carries 61.8 kilonewtons. Right: the '
          'pack cooling turbine, air in at 300 kilopascals and 40 degrees, out at 80 kilopascals and minus 38.8 degrees, its shaft driving the compressor.')


# ---- 2.7 vapour cycle loop with the worked example's heat flows ----
def f7():
    o = []
    l, r_, t, b = 140, 520, 70, 290
    # four components on a loop
    o.append(boxt(l - 70, t + 70, 140, 60, ['Evaporator', 'low pressure'], LVS, LV, 13, True))
    o.append(boxt(r_ - 70, t + 70, 140, 60, ['Condenser', 'high pressure'], NXS, NX, 13, True))
    o.append(boxt(260, t - 26, 140, 52, ['Compressor'], ACS, AC, 13, True))
    o.append(boxt(260, b - 26, 140, 52, ['Expansion', 'valve'], PANEL, AC, 13, True))
    o.append(P([(l, t + 70), (l, t), (200, t)], AC, 2.5)); o.append(L(198, t, 256, t, AC, 2.5, arrow='n'))
    o.append(L(400, t, r_, t, AC, 2.5)); o.append(L(r_, t, r_, t + 66, AC, 2.5, arrow='n'))
    o.append(P([(r_, t + 130), (r_, b), (460, b)], AC, 2.5)); o.append(L(462, b, 404, b, AC, 2.5, arrow='n'))
    o.append(L(260, b, l, b, AC, 2.5)); o.append(L(l, b, l, t + 134, AC, 2.5, arrow='n'))
    o.append(T(l + 8, t - 10, 'vapour', 13, 'start', MUT))
    o.append(T(r_ - 8, b + 22, 'liquid', 13, 'end', MUT))
    # heat flows
    o.append(L(20, t + 100, l - 74, t + 100, LV, 3, arrow='l'))
    o.append(T(20, t + 88, 'cabin', 13, 'start', LV))
    o.append(T(10, t + 150, 'Q evap = 12 kW', 14, 'start', LV, True))
    o.append(L(r_ + 72, t + 100, 700, t + 100, NX, 3, arrow='x'))
    o.append(T(700, t + 88, 'outside', 13, 'end', NX))
    o.append(T(710, t + 150, 'Q cond = 15 kW', 14, 'end', NX, True))
    o.append(L(330, 14, 330, t - 30, AC, 3, arrow='n'))
    o.append(T(340, 24, 'W = 3 kW', 14, 'start', AC, True))
    o.append(R(190, 318, 280, 52, PANEL, L2, 8, 1.5))
    o.append(T(330, 340, 'COP = 12 ÷ 3 = 4.0', 14, 'middle', INK, True))
    o.append(T(330, 360, '15 = 12 + 3 (first law)', 13, 'middle', MUT))
    return 384, ''.join(o)

FIG[7] = (f7, 'The worked example’s pack on the loop: 3 kW of compressor work moves 12 kW out of the cabin air at the evaporator, so the '
              'condenser must reject 15 kW to the outside air and the COP is 4.0.',
          'A closed loop of four parts: compressor at the top, condenser on the right, expansion valve at the bottom, evaporator on the left. '
          'Arrows show 12 kilowatts entering the evaporator from the cabin, 3 kilowatts of work into the compressor and 15 kilowatts leaving '
          'the condenser to the outside. A box states COP equals 12 over 3, which is 4.0.')


# ---- 2.8 passenger oxygen from a cylinder ----
def f8():
    o = []
    o.append(R(30, 60, 90, 200, NXS, NX, 40))
    o.append(T(75, 140, '50 L', 15, 'middle', NX, True))
    o.append(T(75, 164, '124 bar', 14, 'middle', NX, True))
    o.append(T(75, 290, 'cylinder', 13, 'middle', MUT))
    o.append(L(120, 110, 166, 110, AC, 2.5, arrow='n'))
    o.append(boxt(170, 84, 110, 52, ['Shut-off', 'valve'], PANEL, AC, 13))
    o.append(L(280, 110, 316, 110, AC, 2.5, arrow='n'))
    o.append(boxt(320, 84, 110, 52, ['Pressure', 'reducer'], PANEL, AC, 13))
    o.append(L(430, 110, 700, 110, AC, 2.5))
    o.append(T(560, 100, 'low-pressure manifold', 13, 'middle', AC))
    for i in range(6):
        x = 460 + i * 42
        o.append(L(x, 110, x, 150, AC, 1.8))
        o.append(f'<path d="M{x - 11},{150} h22 l-4,18 h-14 z" style="fill:var(--panel);stroke:var(--accent);stroke-width:2"/>')
    o.append(T(570, 192, '12 masks × 4 L/min = 48 L/min', 14, 'middle', AC, True))
    o.append(T(570, 212, '(continuous flow)', 13, 'middle', MUT))
    o.append(R(170, 240, 530, 92, PANEL, L2, 8, 1.5))
    o.append(T(186, 266, 'usable gas = 50 × (124 − 10) ÷ 1 = 5700 L at 1 bar', 14, 'start', INK, True))
    o.append(T(186, 290, 'duration = 5700 ÷ 48 = 118.75 min, about 1 h 59 min', 14, 'start', LV, True))
    o.append(T(186, 314, 'the last 10 bar stays in the cylinder as a reserve', 13, 'start', MUT))
    return 350, ''.join(o)

FIG[8] = (f8, 'The worked example’s passenger supply: a 50 L cylinder at 124 bar, used down to 10 bar, gives 5700 L at 1 bar; twelve '
              'continuous-flow masks at 4 L/min draw 48 L/min, so it lasts about 119 minutes.',
          'An oxygen cylinder of 50 litres at 124 bar feeds a shut-off valve and a pressure reducer, then a low-pressure manifold with six '
          'mask symbols standing for twelve masks at 4 litres per minute each, 48 litres per minute in all. A box works the usable gas, '
          '5700 litres, and the duration, 118.75 minutes.')


# ---- 2.9 dual loops, AND logic, squib and the cargo agent ----
def f9():
    o = []
    o.append(f'<ellipse cx="130" cy="120" rx="110" ry="70" style="fill:var(--panel);stroke:var(--line2);stroke-width:2"/>')
    o.append(T(130, 40, 'engine nacelle', 13, 'middle', MUT))
    o.append(f'<ellipse cx="130" cy="120" rx="86" ry="48" style="fill:none;stroke:var(--next);stroke-width:2.5"/>')
    o.append(f'<ellipse cx="130" cy="120" rx="64" ry="30" style="fill:none;stroke:var(--accent);stroke-width:2.5;stroke-dasharray:7 4"/>')
    o.append(T(130, 116, 'loop A (solid)', 13, 'middle', NX, True))
    o.append(T(130, 136, 'loop B (dashed)', 13, 'middle', AC, True))
    o.append(L(240, 120, 290, 120, AC, 2.5, arrow='n'))
    o.append(boxt(294, 88, 130, 64, ['Control unit', 'A AND B → FIRE'], ACS, AC, 13, True))
    o.append(L(424, 120, 466, 120, AC, 2.5, arrow='n'))
    o.append(boxt(470, 88, 110, 64, ['FIRE light', 'and bell'], LVS, LV, 13, True))
    o.append(L(580, 120, 610, 120, LV, 2.5, arrow='l'))
    o.append(boxt(614, 88, 96, 64, ['Pull,', 'then turn'], PANEL, LV, 13))
    o.append(T(359, 178, 'one loop failed: FAULT,', 13, 'middle', MUT))
    o.append(T(359, 196, 'the other works alone', 13, 'middle', MUT))
    o.append(L(662, 152, 662, 226, NX, 2.5, arrow='x'))
    o.append(boxt(590, 230, 120, 56, ['Squib fires,', 'bottle empties'], NXS, NX, 13, True))
    o.append(P([(590, 258), (250, 258), (250, 186)], NX, 2.5))
    o.append(L(250, 186, 250, 178, NX, 2.5, arrow='x'))
    o.append(T(420, 250, 'agent through pipes to the zone', 13, 'middle', NX))
    o.append(R(20, 300, 680, 70, PANEL, L2, 8, 1.5))
    o.append(T(36, 326, 'Cargo hold 40 m³ at 6 %: V = 0.06 × 40 ÷ 0.94 = 2.55 m³', 14, 'start', INK, True))
    o.append(T(36, 352, 'm = 2.55 × 6 kg/m³ = 15.3 kg (the simple form 0.06 × 40 gives only 14.4 kg)', 13, 'start', MUT))
    return 384, ''.join(o)

FIG[9] = (f9, 'Two loops in the nacelle must both sense a fire before the control unit lights FIRE; the crew pulls and turns the handle, a '
              'squib empties the bottle into the zone. Below, the worked example’s hold needs 2.55 m³ of agent vapour, 15.3 kg.',
          'An engine nacelle with two detector loops A and B feeding a control unit with AND logic, which lights the fire light and bell; '
          'the pilot pulls then turns the fire handle, a squib fires and the bottle sends agent back to the nacelle. A note says a failed loop '
          'gives a fault and the other works alone. Bottom box: a 40 cubic metre hold at 6 percent needs 2.55 cubic metres, 15.3 kilograms.')


# ---- 2.10 stall speeds, warning margin and the sensor chain ----
def f10():
    o = []
    xs = [20, 190, 380, 560]
    o.append(boxt(20, 30, 150, 56, ['AoA vane', 'rotary transducer'], PANEL, AC, 13, True))
    o.append(boxt(20, 100, 150, 46, ['Flap, slat, Mach'], PANEL, AC, 13))
    o.append(L(170, 58, 226, 84, AC, 2.5, arrow='n')); o.append(L(170, 122, 226, 100, AC, 2.5, arrow='n'))
    o.append(boxt(230, 60, 150, 60, ['Stall warning', 'computer'], ACS, AC, 13, True))
    o.append(L(380, 78, 446, 52, LV, 2.5, arrow='l')); o.append(L(380, 102, 446, 126, NX, 2.5, arrow='x'))
    o.append(boxt(450, 26, 250, 46, ['Stick shaker: warning'], LVS, LV, 13, True))
    o.append(boxt(450, 104, 250, 46, ['Stick pusher: protection (some types)'], NXS, NX, 13))
    # speed scale
    x0, x1, y = 60, 690, 270
    fx = lambda v: x0 + (v - 90) / 70 * (x1 - x0)
    o.append(xaxis(x0, x1, y, [90, 100, 110, 120, 130, 140, 150, 160], fx, 'airspeed (kt), 64 000 kg at sea level'))
    for v, lab, col, dy in ((106.2, 'stall, full flap 106.2', NX, -64), (111.5, 'earliest warning 111.5', LV, -30),
                            (145.1, 'stall, clean 145.1', AC, -64)):
        o.append(L(fx(v), y - 50 if dy == -64 else y - 18, fx(v), y, col, 3))
        o.append(Tb(fx(v), y + dy + 8, lab, 13, 'middle', col, True))
    o.append(T(380, 190, 'V = √(2W ÷ (ρ S C<tspan dy="4" font-size="10">Lmax</tspan><tspan dy="-4">))</tspan>: C<tspan dy="4" font-size="10">Lmax</tspan><tspan dy="-4"> 2.8 with flap, 1.5 clean</tspan>', 14, 'middle', INK))
    return 330, ''.join(o)

FIG[10] = (f10, 'The vane, flap and Mach inputs feed the stall computer, which shakes the stick first and pushes only on some types. The '
                'scale shows the worked example: the same aircraft stalls at 145.1 kt clean but 106.2 kt with full flap, so the warning '
                'limit must change with flap; with full flap it may not start below 111.5 kt.',
           'Top: an angle of attack vane and the flap, slat and Mach inputs feed a stall warning computer, which drives a stick shaker as the '
           'warning and, on some types, a stick pusher as protection. Bottom: an airspeed scale from 90 to 160 knots with marks at 106.2 '
           'knots, stall with full flap, 111.5 knots, the earliest warning, and 145.1 knots, stall clean.')


# ---- 2.11 iced leading edge and the stall speed rise ----
def f11():
    o = []
    # leading edge of an aerofoil
    o.append('<path d="M330,120 C230,120 150,140 120,170 C150,200 230,212 330,214" style="fill:var(--panel);stroke:var(--accent);stroke-width:2.5"/>')
    o.append('<path d="M126,156 L106,116 L162,134 Z M126,184 L106,224 L162,206 Z M126,156 C110,162 110,178 126,184 L120,170 Z" style="fill:var(--next-soft);stroke:var(--next);stroke-width:2;stroke-linejoin:round"/>')
    o.append(L(330, 122, 330, 212, L2, 1.5, '4 4'))
    o.append(T(70, 106, 'ice horns', 13, 'middle', NX, True))
    o.append(T(250, 172, 'wing', 14, 'middle', AC))
    o.append(L(20, 170, 84, 170, L2, 2, arrow='m'))
    o.append(T(20, 160, 'airflow', 13, 'start', MUT))
    o.append(T(200, 250, 'C', 14, 'middle', INK) .replace('>C<', '>C<tspan dy="4" font-size="10">Lmax</tspan><tspan dy="-4"> 1.6 → 1.25</tspan><'))
    o.append(T(200, 272, 'ice adds 100 kg to 20 000 kg', 13, 'middle', MUT))
    # bars of stall speed
    x0, y0 = 400, 60
    fx = lambda v: x0 + (v - 90) / 50 * 280
    o.append(T(x0, y0 - 16, 'stall speed (kt)', 14, 'start', INK, True))
    for i, (v, lab, col, fill) in enumerate(((111.4, 'clean 111.4', AC, ACS), (126.3, 'iced 126.3', NX, NXS))):
        y = y0 + i * 70
        o.append(R(x0, y, fx(v) - x0, 40, fill, col, 4))
        o.append(T(x0 + 10, y + 26, lab, 14, 'start', col, True))
    o.append(T(x0, y0 + 168, '+14.9 kt (+13.4 %)', 14, 'start', NX, True))
    o.append(T(x0, y0 + 192, 'weight alone: +0.25 %', 13, 'start', MUT))
    o.append(T(x0, y0 + 214, 'lost lift: ×1.131, +13.1 %', 13, 'start', MUT))
    return 300, ''.join(o)

FIG[11] = (f11, 'Ice horns on the leading edge spoil the flow: in the worked example C<sub>Lmax</sub> falls from 1.6 to 1.25 and the stall '
                'speed rises from 111.4 kt to 126.3 kt, almost all of it from the lost lift and very little from the 100 kg of ice.',
           'Left: the leading edge of a wing with ice horns growing above and below the nose in the airflow; maximum lift coefficient falls '
           'from 1.6 to 1.25 and the ice adds 100 kilograms. Right: two bars of stall speed, 111.4 knots clean and 126.3 knots iced, a rise of '
           '14.9 knots or 13.4 percent, of which the weight gives only 0.25 percent.')


spec = make_spec(FIG)
