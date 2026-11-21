# ee-pe-u6: free-model run

- Book: `work/ee-pe-u6/tree/books/eee/ee-pe/ee-pe-u6.html`
- Status: ok
- Model calls so far: 24 (87,194 tokens in, 206,277 out), 6.0 minutes

## Checker

```
ee-pe-u6.html: 7 chapters, 22035 words, 9 figures, 237 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] figure caption: The caption says the dashed static bypass is used "for maintenance or if the inverter trips". Section 1 and quiz Q6 correctly separate the two: a static bypass (thyristors) takes the load to mains on inverter overload or fault, while a maintenance bypass is a separate manual path that isolates the UPS for service. The caption contradicts the chapter's own definition.
- ch 1 [low] section 1: Transfer time is given only for the off-line type. A line-interactive UPS also transfers the load to its inverter on mains failure; not stating this leaves the reader thinking only the standby type switches.
- ch 1 [low] section 2: "Output THD is the RMS sum of harmonic voltages" is loose wording; a student may read it as adding the harmonic RMS values directly instead of the square root of the sum of squares.
- ch 1 [low] section 3: The linear-supply and SMPS description repeats material that belongs to the power-supplies unit, and the two cross-references ("see Unit 3", "see 6.6") are plain text rather than links, so a phone reader cannot jump to them.
- ch 2 [low] Worked example 1 and the figure: The example treats the whole 55.6 Ah as delivered in the CC phase (5.56 h at 10 A) and then adds a 2 h taper on top. But the taper also pushes charge in: roughly (10 + 2)/2 × 2 = 12 Ah here. So the battery would receive about 55.6 + 12 ≈ 68 Ah against the 55.6 Ah needed, and a real CC phase would end earlier. A sharp student will notice the double counting.
- ch 2 [low] Section 3, emergency lighting paragraph: 'Three-hour duration is common for escape lighting' is stated as if universal. Required autonomy is set by the local code and varies; some codes ask for about one hour, others three hours. A student may quote 3 h as a rule.
- ch 2 [low] Figure: Two small points. The voltage curve starts at 11.5 V, which is below the open-circuit voltage of a 12 V lead-acid block at 50% depth of discharge (about 12.1 V), and well below what it reads under a 10 A charge. Also the caption says the current tapers 'while voltage rises to 14.4 V and holds', which suggests the voltage is still rising during the taper, although the plot has it flat at 14.4 V from 5.6 h.
- ch 3 [low] Section 1, also Exam trap 1: The skin depths 'At 50 Hz, steel δ is centimetres; at 10 kHz it is a few millimetres' are true only for steel with μ_r ≈ 1 (above the Curie point or austenitic). For magnetic steel at room temperature (μ_r ≈ 100, ρ ≈ 2 × 10⁻⁷ Ω·m) the same formula gives δ ≈ 3 mm at 50 Hz and ≈ 0.23 mm at 10 kHz — exactly the value quiz Q3 computes. A student who does Q3 and then reads 'a few millimetres at 10 kHz' sees a contradiction.
- ch 3 [low] Quiz Q5 answer: 'Power drops unless the control raises frequency or DC link voltage' conflicts with Section 2, which says that above resonance moving f closer to resonance raises power, so raising f lowers it. Above the Curie point the coil inductance falls, so the tank's resonant frequency rises and the old operating frequency ends up below resonance; the remedy is to follow the new resonance, not simply to raise f.
- ch 3 [low] Section 2, last line of first paragraph: 'See resonant converters for the switching ideas' names another chapter but carries no link, so a reader on a phone cannot jump to it.
- ch 4 [high] Worked example 1, step 5 and answer: Part (c) asks for the reactive power at 50% of DC power, but step 5 uses the full 2000 MW. Q ≈ 0.5 × 2000 MW = 1000 MVAr is the draw at 100% power, not at 50%, so the step ignores the stated condition and the answer contradicts the question.
- ch 4 [low] Lead: "the line carries pure DC" overstates it. A real DC line carries a slightly rippled current; the smoothing reactor reduces the ripple but does not remove it.
- ch 4 [low] Section 3, formula for P_d: The definitions of V_d and I_d are written only for a bipolar link (pole-to-pole voltage, current in each pole). A student meeting a monopolar or back-to-back link will not know what to substitute.
- ch 5 [low] Section 3: STATCOM, TCSC, SSSC and UPFC are used without being spelled out, while SVC, FACTS, VSC, TCR, TSC and TSR are defined. A second-language reader meeting TCSC and SSSC in the bullet list has no expansion to hold on to.
- ch 5 [low] Section 3, STATCOM paragraph: 'If the converter voltage is higher than the bus voltage, leading current flows' does not say which current. The current the converter pushes into the line actually lags; it is the current drawn from the bus that leads, which is why the STATCOM looks like a capacitor.
- ch 5 [low] Section 3, UPFC bullet: 'the shunt converter supplies active power and vars' can be read as the shunt converter supplying vars to the series converter. The DC link carries active power only; vars are exchanged with the bus at each converter's own terminals.
- ch 5 [low] worked example 1, step 6 and answer: Q is computed from the fundamental current only. At α = 120° the TCR current is not sinusoidal, so 42.6 MVAr is the fundamental reactive power, not the total, and the answer does not say so. At α = 90° the current is sinusoidal, so step 8 is exact.
- ch 5 [low] Section 3, last paragraph: The pointer 'see HVDC transmission' is plain text, not a chapter link, unlike the cross-reference style used elsewhere in the book.
- ch 6 [high] Worked example 1, steps 1 and 3: Step 1 sizes the array from the AC load (4000 Wh) using only the 0.75 wiring/dust factor, so the array delivers 4000 Wh of DC per day. Step 3 then says the DC bus must supply 4444.4 Wh per day because the inverter is only 0.9 efficient. The two steps contradict each other and the array is undersized by 11%, so the stated answer cannot meet the load.
- ch 6 [high] Section 2, after the switching-frequency formula: It says the filter and the worst-case loss are designed at the low-frequency end. The lowest switching frequency (near the sine peak) sets the filter, but switching loss falls with frequency, so the worst-case switching loss is at the highest frequency, near v_g = 0, not at the low-frequency end.
- ch 6 [low] Worked example 1, step 5 and answer: The required capacity is 308.6 Ah, but the answer offers a 300 Ah block, which is smaller than the requirement and would deepen the discharge beyond 60%.
- ch 6 [low] Section 2, paragraph on direction of power: 'a reference that delivers power gives inversion, one that is in phase with the grid voltage but draws power gives rectification' is confusing: whether the current is in phase or anti-phase with the grid voltage depends on which direction is taken as positive, and the text does not say.
- ch 6 [low] Worked example 1, step 4: The stored-energy calculation ignores the battery's round-trip efficiency (~90% for lithium, quoted in Section 4), and the 60% DoD is deeper than the 50% the section gives for lead-acid, without saying which chemistry the example assumes.
- ch 7 [low] Section 2 and Quiz Q3: The claim that integral-cycle control gives 'almost no harmonics' / 'Current stays nearly sinusoidal' is overstated. Each burst is a sinusoidal segment, but the on/off modulation at the burst rate (2.5 Hz for a 0.4 s period) puts subharmonic/interharmonic currents on the line. A strict examiner would mark the unqualified statement down.
- ch 7 [low] Worked example 1, step 3: The step verifies the bracket value at α = 90° instead of showing it follows from the power fraction. A student reading the steps sees 162.63 V appear before the link between V_rms and α is made; the step reads as if α = 90° were assumed.
- ch 7 [low] Exam traps, third trap: '4 mA is zero, not 0 mA' reads as nonsense on first pass: 4 mA is not zero in milliamps, it is the zero of the measurement scale.
- ch 7 [low] Section 3: 'Four-quadrant operation lets a drive motor or brake in either direction' is ambiguous — 'motor' and 'brake' can be read as nouns, so the sentence parses wrongly for a second-language reader.
- ch 7 [low] Quiz Q6: The answer hedges 'quadrant II or IV' without fixing the sign convention, so a student cannot tell which single quadrant answers the question as asked. Also, for a DC drive the regenerated energy normally goes back to the supply through the converter, not only to a DC bus or chopper resistor.
- ch 7 [low] Figure: The edge from 'Thyristor power controller' to 'Heater 2 kW' is labelled α. The firing angle is set inside the controller; what reaches the heater is an RMS voltage, so the label can mislead a student into thinking α is a signal sent to the load.
