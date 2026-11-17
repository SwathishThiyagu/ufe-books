# e-bee-u6: free-model run

- Book: `books/common/e-bee/e-bee-u6.html`
- Status: ok
- Model calls so far: 29 (103,148 tokens in, 247,518 out), 6.9 minutes

## Checker

```
e-bee-u6.html: 8 chapters, 16424 words, 9 figures, 165 KB
OK
```

## For the reviewer

- chapter 4: the figure cannot be drawn: tree is too wide (6 leaves); use fewer leaves or shorter labels

## Reviewer notes (after any revision)

- ch 2 [low] Section 1, paragraph 3: The text jumps straight to 'torque proportional to V × I × cos φ'. It never says why the cosine appears, so a student cannot see where the cos φ comes from and may think any two coils give a power-reading meter.
- ch 2 [low] Section 1, paragraph 4: N was defined as the number of disc revolutions, but the next sentence calls it 'the number of turns N'. Turns usually means coil turns in this chapter, so the word collides with the coil description.
- ch 2 [low] Section 2, megger test sequence: Only live-to-earth and live-to-neutral tests are listed. The standard insulation test of an installation also includes neutral to earth, and leaving it out makes the procedure look complete when it is not.
- ch 2 [low] Section 3, last paragraph: 'Keep the sample rate at least twice the highest signal frequency you want to see' gives the bare Nyquist limit. At exactly twice, a sine can be located but its shape is not faithfully displayed, and real waveforms contain harmonics well above the fundamental.
- ch 2 [low] Section 3, last paragraph (isolation transformer advice): 'Use a differential probe or an isolation transformer' does not say which device is isolated. A student may isolate the oscilloscope itself, which floats the earthed chassis and the probe ground clip and creates a shock hazard instead of removing one.
- ch 3 [low] Section 2, paragraph beginning 'Hall sensors measure magnetic field': It says a toothed wheel passing the sensor gives one pulse per tooth. A plain steel toothed wheel does not change the field at a bare Hall element; a Hall gear-tooth sensor needs a small back-bias magnet behind the element (or magnets on the wheel) so the teeth modulate the flux.
- ch 3 [low] Worked example 1, step 1: "10 × 10-3" loses the superscript, so a student can read it as 10 × 10 − 3 and get a wrong value before starting.
- ch 3 [low] Figure (aria text and edges): The aria text says the comparator gives a '4 V switch output', but 4 V is the amplifier output that feeds the comparator. The comparator output is a HIGH/LOW level near the supply rail, not 4 V.
- ch 3 [low] Quiz Q3, answer: 'Because the charge separation is small' gives the effect, not the cause, and can mislead a student into thinking a thicker element gives a bigger Hall voltage (it gives a smaller one).
- ch 3 [low] Section 2 (end) and Section 3 (end), unit cross-references: 'see Unit 3, special machines' and 'as in Unit 4' are plain-text pointers with no link, and the second does not say which topic it means, so a student revising on a phone cannot jump to it.
- ch 4 [high] Lead, first sentence: The lead says electric power is always made by turning the source into mechanical rotation and then into alternating voltage. Solar PV does the opposite: light becomes DC directly, with no turbine, no shaft and no rotation. A student reading the lead then Section 2 meets two contradictory chains.
- ch 4 [high] Section 3 text and comparison table: The text says 'Coal has cheap fuel but high emissions', but the table row 'Fuel cost | Coal | High' says the opposite. The same chapter gives two answers about coal fuel cost, and a student cannot tell which to write in the exam.
- ch 4 [low] Section 3, comparison table, Nuclear fuel cost: Nuclear fuel cost is marked 'Medium'. In standard treatment nuclear fuel is a small share of the cost of nuclear electricity; the high cost is capital and decommissioning. Nuclear fuel cost is lower than coal's, not between coal and zero.
- ch 4 [low] Section 3, comparison table, Emissions row: 'Waste' is not an emission. Putting it in the Emissions column mixes two different side effects, and a student may write 'nuclear emits waste' as an answer about emissions.
- ch 5 [high] Section 4, Reading a single-line diagram: The rule 'It must fall, never rise' contradicts the rest of the chapter. An SLD read from source (generator at 11–25 kV) to load must show the voltage RISING at the step-up transformer before it falls at the step-down substations and the distribution transformer. As written, a student would mark the correct step-up transformer as an error.
- ch 5 [low] Figure, specs: The figure chain is not consistent with the text chain. The step-down substation is noted '66/33 kV', which skips the first 400/220 kV stage, and the next node is already the 11 kV feeder, skipping 33/11 kV. The step-up note '220 kV' also differs from the text, which gives 400/220/132 kV.
- ch 5 [low] Section 2, Transmission line bullet: The list of standard Indian transmission levels leaves out 765 kV, the highest AC level in use, and presents 66 kV as a transmission level, although it is normally classed as subtransmission and is used only in some regions.
- ch 5 [low] Section 4, symbols list: The isolator is described only as 'a diagonal line that opens'. A student misses the key operating point that an isolator must not be opened on load.
- ch 5 [low] Section 3, transformer bullet: 'The delta blocks triplen harmonics' can be read as the delta removing harmonics from the whole transformer. The delta winding actually gives the triplen (third-harmonic) currents a closed path to circulate, so they do not appear in the line voltages.
- ch 6 [low] Section 1, bill formula: Fuel surcharge is defined as a ₹ per kWh rate, but in the formula it is added as a lump rupee amount. Adding a ₹/kWh quantity to a ₹ total is dimensionally wrong; the PF penalty term has the same problem.
- ch 6 [low] Section 1, bullet on fixed charge: "Fixed charge is ₹ per month for the connection" is too flat. In most Indian tariff orders the fixed (demand) charge is ₹ per kW per month on the sanctioned load, so a bigger connection pays more even at zero units.
- ch 6 [low] Section 3, panel count formula: Panel count = array kW ÷ panel kW can give a fraction, and panels come only in whole numbers. A student may write 7.5 panels as an answer.
- ch 6 [low] Worked example 1, given data: "Average generation is 4 kWh per kW per day" already includes heat and wiring losses, but the chapter's formula is Daily kWh = array kW × PSH × PR. A student may read 4 as PSH and multiply by PR = 0.80 again, getting 9.6 kWh per day instead of 12.
- ch 7 [low] Section 1 (design bullets) and Section 2 (formula box): Two different sizing rules are given for the same MCB. Section 1 says I_b ≤ I_n ≤ I_z. Section 2 says I_n ≥ 1.25 × I. A student does not know whether the 25 % margin is already inside I_b (which includes the diversity factor D) or is a separate step, and applying 1.25 to I_b gives a different answer from applying it to the plain load current.
- ch 7 [low] Figure caption (distribution board): 'The RCCB is the only device that reacts to current leaking to earth' is too strong. When the earth path is healthy and the fault current is large, the MCB also trips on that earth-fault current, as the Q6 answer itself implies ('no fault current flows, so the MCB or RCCB may not trip').
- ch 7 [low] Section 3, RCCB paragraph: Calling an ELCB simply 'the older name' for an RCCB is imprecise. The current-operated ELCB is essentially an RCCB, but the older voltage-operated ELCB is a different device that senses the voltage of the metal body to earth and needs its own earth electrode.
- ch 7 [low] Exam traps, second trap: 'An open earth makes the metal body live' is incomplete. A broken earth by itself does not energise the body; the body becomes live only when a fault or leakage puts live voltage on it and there is no earth path to carry the current away.
- ch 7 [low] Quiz Q5: The question adds lamps, fans, a geyser and an air conditioner and asks for one MCB. In a real board these are separate sub-circuits (5 A light circuit, 16 A power circuits), and one 16 A MCB cannot feed all of them. The answer also skips the 1.25 margin step that Q4 and Section 2 use, so the method shown differs from the rest of the chapter. The numerical result (16 A) stays correct either way.
- ch 7 [low] Section 2, first paragraph: 'Can be miswired' is vague. The real danger with a rewirable fuse is that it is rewired with a thicker wire than its rating, so it no longer protects the cable.
- ch 8 [high] Quiz Q4: 23 A is only 1.15 times the 20 A MCB rating. An MCB will not trip on this current in a reasonable time; it may carry 1.13 times its rating indefinitely. The answer 'yes, the MCB trips' is wrong for fault protection.
- ch 8 [low] Section 2: The text says the backfill 'such as bentonite or graphite' holds moisture. Graphite is a conductive material and does not hold moisture; bentonite does.
- ch 8 [low] Section 4: A three-terminal earth tester uses two probes: a current probe and a potential probe. The text mentions only 'a probe', which is incomplete.
- ch 8 [low] Section 4: A clamp-on earth tester measures earth resistance, not current. The text says it 'measures the current in the earth path'.
- ch 8 [low] Quiz Q6: The 2.3 A is the earth fault current, not the current through a person. The danger is the high touch voltage on the metal body, which can drive a lethal current through a person.
- ch 8 [low] Figure: The note '5 Ω total' is placed on the earth wire node, but the 5 Ω is the total of the earth wire and electrode. This can confuse students into thinking the earth wire alone is 5 Ω.
