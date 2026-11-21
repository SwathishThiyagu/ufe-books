# ei-sensor-u2: free-model run

- Book: `work/ei-sensor-u2/tree/books/eie/ei-sensor/ei-sensor-u2.html`
- Status: ok
- Model calls so far: 22 (98,575 tokens in, 214,184 out), 7.0 minutes

## Checker

```
ei-sensor-u2.html: 7 chapters, 22411 words, 9 figures, 227 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Quiz Q5 (and Section 2's ten-times rule): The advice 'use a load at least ten times the track resistance' does not actually meet the 1 % full-scale target set in the question. At RL = 10R the mid-stroke error is 1.22 % of full scale, not 1 %.
- ch 1 [low] Section 3, figure caption: The caption says 'the same potentiometer feeding a 10 kΩ load', but the track resistance is not given here. The reader cannot tell that R = 10 kΩ (and so r = 1) until worked example 1, which comes after the figure.
- ch 1 [low] Exam trap 1: 'use the loaded formula whenever the load is within about ten times the track' is ambiguous and reads two ways.
- ch 1 [low] Section 2 and Section 3 cross-references: The pointers 'See Unit 6 for buffer amplifiers', 'For bridge circuits, see Unit 6' and 'see Unit 4' are plain text, not links, so a student reading on a phone cannot jump to them.
- ch 2 [low] Section 1, microstrain definition: "1 µε = 10⁻⁶" is written as an equality without saying what the 10⁻⁶ refers to, right after saying strain has no unit. A student may read it as 1 µε = 10⁻⁶ of something unspecified, or as a unit conversion.
- ch 2 [low] Section 3, bridge paragraph: "Half bridges lie between these" gives no number, so the student cannot check a half-bridge answer.
- ch 2 [low] Section 3, quarter-bridge formula: The output V_s·GF·ε/4 is stated without its assumptions (the other three arms are fixed resistors equal to R, transverse sensitivity and lead resistance are negligible, output taken unloaded). A student may apply it to any bridge.
- ch 2 [low] Section 3, lead resistance: The paragraph says long leads unbalance a quarter bridge but does not mention the usual remedy, the three-wire connection that puts equal lead resistance in adjacent arms.
- ch 3 [low] Section 1, the sentence after the element list: 'Two gauges see tension and two see compression': This is true for a bending beam, but the chapter's worked example is a solid column in pure compression, where all four axially bonded gauges compress. In a real column cell two gauges are axial (compression) and two are transverse Poisson gauges (tension, magnitude about 0.3ε), so the four strains are not of equal magnitude and the output is not exactly V_s·GF·ε. A student can read this sentence, then the example, and be confused about which arrangement gives the factor of four.
- ch 3 [low] Lead paragraph: 'calibrated directly in newtons or kilograms' — the kilogram is a unit of mass, not force. A load cell senses force; a display showing kg is showing the equivalent mass at a stated value of g.
- ch 3 [low] Exam traps, last bullet: 'a four-gauge full bridge already includes temperature compensation' overstates it. The full bridge cancels the apparent strain (zero shift) caused by uniform temperature change, because all gauges move together. It does not cancel the span (sensitivity) drift caused by the change of elastic modulus with temperature, which real cells correct with a modulus-compensating resistor in the bridge circuit.
- ch 3 [low] Section 3, formula T = F · r: The relation holds only for a force tangential to the radius. A force along the axis or radial produces no torque about that axis, and the definition should say so.
- ch 4 [high] Figure caption: The caption says 'Normalised so both curves start near 1', but the plot does not do that. The Pt100 curve is divided by its R₀ at 0 °C, so it starts at 1.00; the NTC curve is divided by its R₀ at 25 °C, so at 0 °C it starts at about 2.93. A student reading the caption and then the graph sees a contradiction.
- ch 4 [low] Quiz Q4 answer: The answer says a PTC gives 'no usable, monotonic reading over a range of temperatures'. A PTC characteristic is in fact monotonic (it never decreases); what makes it useless as a thermometer is that it is almost flat below the transition and then extremely steep inside a narrow transition band.
- ch 4 [low] Section 1, Pt1000 sentence: 'The larger value gives a larger voltage for the same current, which helps when the cable is long' gives the wrong reason. The main benefit of Pt1000 on long cables is that a fixed lead resistance is a ten times smaller fraction of the element resistance, so the lead error in °C is ten times smaller.
- ch 4 [low] Section 3 versus Worked example 1, step 10: Section 3 says an NTC is 'about ten times' as sensitive as a Pt100, while the worked example concludes 'about eight times'. Both are defensible (local fractional sensitivity at 300 K versus average over 25–37 °C) but the mismatch is not explained and can look like an inconsistency.
- ch 5 [low] Section 2, constant-temperature paragraph: Saying the constant-temperature mode is 'less sensitive to ambient temperature' reads as if it is immune to T_a, yet the very next bullet says a cold wire is added to measure T_a for compensation, and Exam trap 3 says the wire responds to T_a. A student will see a contradiction.
- ch 5 [low] Exam traps, item 4: The trap is titled 'Using inconsistent units in King's law' but the unit quoted, V²/(m s⁻¹)^0.5, belongs to B in the calibration equation E² = A + B·u^0.5, not to a or b in King's law h = a + b·u^0.5 (those carry W/(m²·K) and W/(m²·K)·(m/s)^−0.5).
- ch 5 [low] Section 3 and worked example 1(c): 'About one decade per 30 % RH' is stated as a property of resistance hygrometers, but real films vary widely and many fall faster (roughly a decade per 15–25 % RH). All the numerical answers depend on this one figure.
- ch 5 [low] Section 1, first sentence: The heat balance I²R_w = hA(T_w − T_a) ignores heat lost by conduction along the wire to the prongs and by radiation, which is a real loss in short wires mounted on supports.
- ch 5 [low] Section 1, probe dimensions: 'A few millimetres long' overstates typical hot wires, which are usually about 1 mm to 2 mm of active length.
- ch 6 [low] Section 1, formula line and Exam traps, first trap: In the formula note the exponent on the unit is lost: 'A is a constant in Ω·luxγ' reads as lux times γ. In the trap line 'R = A·E−γ' the exponent is lost too, so a student reads E minus γ instead of E to the power minus γ.
- ch 6 [low] Figure caption: 'The curve is steep in dim light, so the LDR is most sensitive there' is true of the resistance slope dR/dE, but it clashes with Section 2 ('sensitivity is highest when RLDR is near Rf') and with the Q4 answer. A student can conclude the divider output is most sensitive in the dimmest light, which is wrong for a circuit with Rf = 10 kΩ.
- ch 6 [low] Section 1, bullet on CdS peak: 540 nm is green light; green-yellow lies around 570 nm, so the colour name is slightly off.
- ch 6 [low] Section 1 (first use of lux) and Section 3 (ABS): The unit lux is never defined, and the abbreviation ABS is used without expansion.
- ch 6 [low] Worked example 1, step 1 and quiz Q3, Q7: The constant 10⁶ is written without units, so the law looks dimensionally bare and a student cannot check that R comes out in ohms.
- ch 7 [high] Quiz Q5: The numbers contradict each other. With the cold junction at 25 °C (E = 1.28 mV) and the meter reading 8.50 mV, the emf referred to 0 °C is 9.78 mV, which on the J-type table is about 182 °C, not 175 °C. The average sensitivity over 175 °C would be 9.40/175 = 53.7 µV/°C, so 55.9 µV/°C is not 'consistent with 52' either. A student who checks the table will get a different answer.
- ch 7 [low] Quiz Q4 (and the copper-wire exam trap): The conclusion is right but the stated reason is wrong and clashes with Section 2. If copper is joined to chromel and alumel at one isothermal point, the two extra junctions cancel by the intermediate-metals law and no error appears — so 'they cancel only if both are at the same temperature; in a real installation they are not' is not the real mechanism, and 'at the instrument end' is the wrong place. The actual error comes from the reference junction moving to the remote junction box or probe head, whose temperature is not the temperature the instrument's cold-junction sensor measures.
- ch 7 [low] Section 3, table, row E: The Range column holds a remark ('most sensitive') instead of a range, so the table cannot be read column by column.
- ch 7 [low] Section 3, table, row B: 'above 1600' misstates the type B range. Type B is used from roughly 600 °C to 1700 °C, and its published tables run to about 1820 °C; its emf is very small at low temperature, which is why it is not used there.
- ch 7 [low] Beyond: 'The same Seebeck effect run backwards is a thermoelectric generator' is wrong. A generator uses the Seebeck effect directly; it is the Peltier cooler that runs the effect in reverse, and a generator is that cooler module driven in reverse.
