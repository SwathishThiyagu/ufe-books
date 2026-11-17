# ec-analog-u6: free-model run

- Book: `books/ece/ec-analog/ec-analog-u6.html`
- Status: ok
- Model calls so far: 35 (154,931 tokens in, 355,562 out), 10.7 minutes

## Checker

```
ec-analog-u6.html: 9 chapters, 17991 words, 10 figures, 182 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Lead, first paragraph: "a few microvolts between the inputs is enough to slam the output against a supply rail" understates the real number by roughly twenty times. With AOL = 10⁵ and ±12 V supplies the input must reach about 110 µV (55 µV of overdrive) before the output clamps, and the chapter's own worked example uses exactly this figure.
- ch 1 [low] Section 1, ideal properties list: The acronym "IOA (ideal op-amp) model)" is not a standard textbook name; presenting it as something "some syllabi call" the circuit is an invented term and may confuse a student who searches for it.
- ch 1 [low] Section 2, paragraph after the strip-width formula: "A differential input of one millivolt is twenty times too big" is arithmetically off: 1 mV = 1000 µV against a linear limit of 55 µV gives about 18 times, not 20. Against the full 110 µV strip it is about 9 times, so the comparison base is also ambiguous.
- ch 1 [low] Section 1, second formula line: The open-loop gain appears as plain text "AOL" in the formula line while everywhere else it is written A<sub>OL</sub> (and once as "A_OL" in the figure). Inconsistent notation for the same symbol.
- ch 2 [low] Lead: The lead says the voltage follower is the non-inverting case with R1 open only. The standard voltage follower also needs Rf = 0 (direct feedback); otherwise the usual circuit is not fully specified.
- ch 2 [low] Section 3: The numerical statement 'A gain of 10 with A_OL = 10^5 has about 0.011% error' is only true for an inverting gain of magnitude 10. For a non-inverting gain of 10, the error is about 0.010%. The sentence follows 'for both connections', so it is ambiguous and partly wrong.
- ch 2 [low] Figure: The figure edges and text imply current through Rf flows from the output to the virtual ground. For positive v_in and negative v_out, conventional current through Rf flows from the virtual ground to the output.
- ch 2 [low] Worked example 1, step 6: Calling 1 + Rf/R1 = 11 the 'loop factor' is nonstandard and can be confused with loop gain. The actual loop gain is A_OL R1/(R1 + Rf).
- ch 2 [low] Section 3: The sentence 'Finite open-loop gain A_OL makes the closed-loop gain slightly smaller than ideal' is technically wrong for the signed inverting gain: −9.9989 is larger than −10. It is correct only for gain magnitude.
- ch 3 [high] Section 3 (last sentence) and exam trap 5: The noise gain is quoted as 1 + R_f/R₁ and trap 5 applies it to 'the summer'. That value is the noise gain of the four-resistor subtractor (or of a single-input inverting amplifier). In an n-input inverting summer the offset voltage sees all input resistors in parallel to ground, so its gain is 1 + R_f/(R₁∥R₂∥…∥Rₙ), which is much larger. Example: with R_f = 10 kΩ and three 10 kΩ inputs the offset gain is 1 + 10k/3.33k = 4, not 2. A student will under-estimate the output offset of the summer.
- ch 4 [high] Section 1, third bullet ("the two inputs do not look alike"): This describes the four-resistor difference amplifier wrongly, and contradicts the first bullet of the same section and the answer to Q4. In the difference amplifier both sources are loaded by a resistor R₁ (one goes to the virtual node at the inverting input, the other to the non-inverting input which also has R₁ to ground), so neither input is "a high-resistance op-amp input". The description given belongs to the two-op-amp instrumentation amplifier (Section 3), not to a plain difference amplifier.
- ch 4 [low] Section 1, closing paragraph: The text says the bridge, thermocouple or skin electrode "asks for four things" but only three items are listed (high input resistance, gain set by one resistor, CMRR above 100 dB).
- ch 4 [low] Section 3, CMRR bullet: "the first stage's very high value" is inaccurate. The input stage has common-mode gain exactly 1 and differential gain 1 + 2R/R_G, so its own CMRR is only 1 + 2R/R_G (60 dB at a gain of 1000, 0 dB when R_G is open). What makes the first stage harmless is that its common-mode gain is 1, not a very high CMRR.
- ch 4 [low] Section 4, Practical bullet (driven shield): "take the shield from the R_G node" is ambiguous and, read literally, wrong: R_G has two ends, one sitting at v₁ and the other at v₂, so a shield connected there would be driven by the signal itself and its capacitance would be charged by the signal. A driven shield must follow the common-mode voltage.
- ch 4 [low] Quiz Q5, answer: The question says only that the four second-stage resistors are equal; it never gives a value. The answer inserts 10 kΩ ("10 kΩ/10 kΩ = 1"), which is a number the student cannot know from the question.
- ch 4 [low] Figure spec: The label "1 + 2R/R_G" is placed on the buffer→R_G edge, which suggests the signal (and the gain) passes through R_G into the next block, and R_G has no onward edge. Students may read the gain as coming out of R_G instead of out of the two buffers.
- ch 4 [low] Lead: "Strain-gauge weighings" is not idiomatic English and is vague for a second-language reader.
- ch 5 [low] Section 1, frequency-response sentence: The text says the gain falls at 20 dB per decade 'above the corner f = 1/(2πR₁C)'. For an ideal integrator the magnitude falls at 20 dB per decade at every frequency; the corner is only the point where the gain passes through 1 (0 dB). As written, a student may think the gain is flat below the corner, which is true of the practical circuit in Section 2, not the ideal one.
- ch 5 [low] Section 3, sine-input sentence: 'A sine input gives a cosine output, shifted by 90°' drops the minus sign from vout = −RC dvin/dt. The true output for vin = V sin(ωt) is −RCω cos(ωt), an inverted cosine, i.e. the output lags the input by 90°. A student reading only this sentence will sketch a plain +cosine.
- ch 5 [low] Figure (plot spec data): The sample points for both series are spaced 1250 Hz apart on a linear grid, so the first plotted point is at about 1.25 kHz. On a 1 Hz to 100 kHz log axis the integrator line and the differentiator line are drawn only in the right-hand part of the plot; the whole 1 Hz to 1.25 kHz region has no curve, so the figure does not show the low-frequency behaviour it describes.
- ch 6 [low] Section 2 (Howland current pump): The four bridge resistors R1 to R4 are named but never placed: no figure or sentence says which resistor joins which node, so 'R1/R2 = R3/R4' cannot be checked or used by a student. Also, 'the load current is again v_in/R' is only true when the input divider is unity (R1 = R2, and then R3 = R4); with a general matched bridge the transconductance is scaled by R2/R1.
- ch 6 [low] Worked example 1, Quiz Q3 and Q7: These use V_sat equal to the supply rail (12 V on ±12 V, 15 V on ±15 V), but Section 2 states V_sat is the rail minus 1 V to 2 V. A student sees the rule and then sees it broken in every numerical case.
- ch 6 [low] Section 3 (transimpedance amplifier), photodiode sentence: 'Its own capacitance never charges because its terminal stays at 0 V' is loose. Both photodiode terminals are held at fixed voltages, so the point is that the voltage across the diode, and hence the charge on its capacitance, never changes with the signal.
- ch 6 [low] Section 1 and Quiz Q3: The compliance limit R_L(max) = (V_sat - v_in)/I_L is derived only for the Howland pump in Section 2, yet Q3 asks for R_L(max) of the floating-load converter. The floating-load section never says the same limit applies, or why.
- ch 7 [low] Section 2 (BJT log amplifier): It says the emitter drives the output but never says where the base goes. Without that, a student cannot draw the transdiode connection, and cannot see why V_BE = −v_out.
- ch 7 [low] Section 3 (antilog amplifier): The polarity rule is given only for the log amplifier. In the antilog stage a negative v_in reverse-biases the diode, the feedback path opens and the output sits at a rail, so the 'few hundred millivolts' range is one-sided.
- ch 7 [low] Exam traps, third trap: 'Applying a negative or zero input: the diode cuts off' is loose for the zero case. At v_in = 0 the diode is not reverse-biased, it simply carries no current, so ln(0) is undefined and the output drives to the positive rail.
- ch 8 [high] Section 1, formula: The formula v_D,eff = v_D / A_OL is only correct for a unity-gain non-inverting loop (feedback factor β = 1). In the inverting precision rectifier discussed next, the loop gain is A_OL β with β = R₁/(R₁+R_f). For R₁ = R_f, β = 0.5, so the output error is 2v_D/A_OL = 14 µV, not 7 µV. The chapter presents the formula as general.
- ch 8 [low] Section 3, peak detector description: The sentence 'The op-amp input receives v_in' is vague; a student may not know which input.
- ch 9 [high] Section 1, second sentence of the comparator definition: The sentence is broken: "and −Vsat when v+ −." The condition for the low output is missing, so the basic definition of a comparator is unreadable.
- ch 9 [high] Section 2, paragraph describing the inverting Schmitt trigger thresholds: "The output stays high while vin sat" is garbled; the upper limit is missing, so the switching condition is not stated.
- ch 9 [high] Section 3, output condition of the window detector: "The final output is high only while VL in U" is garbled. Taken literally it is meaningless, and the comparator polarities that make the AND gate work are never stated.
- ch 9 [low] Worked example 1, step 5: Saying "at 3 V or 5 V the strict inequality makes it low" is not physically true: at exactly the threshold the comparator output is indeterminate, and the AND output is undefined, not guaranteed low. The strict inequality is a convention, not a mechanism.
- ch 9 [low] Section 1: V_sat is used in section 1 ("V_sat or −V_sat") before it is defined; the definition only appears in the formula block in section 2.
