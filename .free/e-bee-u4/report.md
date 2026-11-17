# e-bee-u4: free-model run

- Book: `books/common/e-bee/e-bee-u4.html`
- Status: ok
- Model calls so far: 21 (79,689 tokens in, 154,672 out), 4.4 minutes

## Checker

```
e-bee-u4.html: 7 chapters, 14978 words, 8 figures, 149 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 2, junction at rest: The depletion width is given as 'a few micrometres'. For ordinary diffused junctions it is usually well under a micrometre; a few micrometres applies only to lightly doped or power devices, so a student may over-estimate it.
- ch 1 [low] Section 3, reverse bias: Saying the constant-voltage breakdown 'is the Zener effect' is too broad. In ordinary PN diodes with breakdown above about 5-6 V the mechanism is avalanche breakdown; the Zener effect dominates only in heavily doped junctions that break down below roughly 5-6 V.
- ch 1 [low] Exam traps, first trap: The error from ignoring the 0.7 V drop is not 15%. With 5 V and 220 Ω, the ideal value is 22.73 mA against 19.55 mA, an error of about 16% measured against the correct current (about 14% measured against the ideal value).
- ch 1 [low] Figure, silicon diode characteristic: The plotted points stop at 0.675 V (about 72.9 mA) while the x-axis runs to 1 V, so the forward curve ends in mid-plot. The expression 0.0001*exp(x/0.05) at x = 1 V gives about 4.85×10⁴ mA, far above the stated y maximum of 100 mA, so the curve is not drawn to the axis limits.
- ch 1 [low] Lead and Section 3: The lead says the diode conducts almost nothing below 'about 0.7 V', while Section 3 puts the knee at 0.6 V for silicon. A student may not see which number to quote for the knee.
- ch 1 [low] Section 3, cross-reference: The pointer to the Zener diode and voltage-regulator chapter is plain text, so it is not a working cross-chapter link like the others in the book.
- ch 2 [high] Lead and Section 3, first paragraph: The chapter says the Zener is used 'as the reference in three-terminal regulator chips such as the 7805 and LM317' and that a three-terminal regulator 'hides the Zener reference ... inside one package'. The 78xx family and the LM317 use a bandgap reference (the LM317's 1.25 V is a bandgap voltage), not a Zener. The chapter's own 'Beyond' note says bandgap references make the 1.25 V reference, so it contradicts itself.
- ch 2 [low] Section 2, last bullet and formula Pz = Vz × Iz(max): Iz(max) was defined earlier as the device rating (largest current the package can take), but here it is used for the actual worst-case operating current found in the design. A student may read Pz = Vz × Iz(max) as using the rating and get an inflated power.
- ch 3 [low] Quiz Q6: The answer states flatly that the transistor moves into saturation when β rises from 100 to 300. That depends on VCC and RC, which the question never gives. With a small supply (say VCC = 6 V and the stated VCE = 5 V), tripling IC would only pull VCE down to about 3 V, still in the active region.
- ch 3 [low] Worked example 1, step 5 and Quiz Q4: Both use IC(sat) ≈ VCC/RC (5.45 mA and 10 mA), but the load-line section defines IC(sat) = (VCC − 0.2)/RC. The two numbers differ slightly (5.45 mA against 5.36 mA), which can confuse a student checking the steps.
- ch 3 [low] Quiz Q1: The question asks for the doping and the thickness of all three regions, but the answer gives thickness only for the base ("thin") and only "larger" for the collector; emitter thickness is not addressed at all, so a student cannot see what a full-mark answer looks like.
- ch 3 [low] Section 3, CE input characteristic: "IB is almost zero below about 0.6 V and rises steeply after 0.7 V" leaves a 0.1 V gap in which the reader cannot tell whether the current is zero or rising. IB actually starts to be visible near 0.5–0.6 V and grows exponentially from there.
- ch 4 [low] Lead: "a negative or positive gate voltage changes the width of a conducting channel" mixes the two families. A student may think an n-channel JFET can be biased with a positive gate voltage, which forward biases its gate junction.
- ch 4 [low] Section 2 (formula note): VGS(off) is equated with the pinch-off voltage VP without a sign convention. Many textbooks quote VP as a positive magnitude, VP = |VGS(off)|, so a student meeting VP = 4 V elsewhere will redo the square law with the wrong sign.
- ch 4 [low] Section 3 (MOSFET saturation): The saturation formula is given without the condition for reaching saturation (VDS ≥ VGS − VT, the overdrive voltage). Quiz Q5 also assumes saturation without stating it, so the student cannot check the assumption.
- ch 5 [low] Worked example 1, step 5: The sentence mixes magnitude and sign: it says the voltage across Rf is 5 V and then that this 'agrees with Vout − 0 V = −5 V'. A student can read this as a contradiction, and the current direction is never stated.
- ch 5 [low] Section 2, saturation paragraph, and Exam trap 4: The headroom is stated as a fixed 'about 1 V below each rail'. On a real 741 the output swing depends on supply and load, and is typically 1–2 V below each rail, so ±11 V from ±12 V supplies is optimistic.
- ch 5 [low] Section 3, inverting and non-inverting amplifiers: The input resistance seen by the source is not given for either configuration, yet it is a standard exam point and follows directly from the two rules already stated.
- ch 5 [low] Lead: 'Op-amps sit inside sensor boards, audio mixers, filters and comparators' is loose: a comparator is a separate part, not a circuit that contains an op-amp, though an op-amp is often wired as one.
- ch 6 [high] Section 3 (Integrator and differentiator): The phase/sign statement is wrong. For an inverting integrator with Vin = A sin(ωt), Vout = −(1/(R1C))∫A sin(ωt)dt = +(A/(ωR1C))cos(ωt). The output is a cosine with a plus sign (it leads the input by 90°), not 'a cosine with a minus sign'.
- ch 6 [low] Section 3, integrator formula: The formula gives only the change in output and silently assumes the output starts at 0 V at t = 0. A student may apply it to a circuit whose capacitor already holds charge and get the wrong absolute level.
- ch 6 [low] Section 1, non-inverting adder sentence: 'scaled by the number of inputs' is ambiguous and can be read as Vout = (1 + Rf/R1)(V1 + V2 + …), which is the sum, not what the circuit does.
- ch 7 [high] Worked example 1, step 1: The step calls R1 + 2R2 'the charging path resistance'. The capacitor never charges through R1 + 2R2; it charges through R1 + R2 and discharges through R2. R1 + 2R2 is only the effective resistance that appears in the period formula. A student who memorises this label will use the wrong path resistance in the duty-cycle or high-time calculation.
- ch 7 [high] Quiz Q5, answer: The second cause and its fix are wrong. A small series resistor makes the LED brighter but does not change the duty cycle or stop it flashing, so 'raise the series resistor' cannot cure a steady glow. The answer also leaves out the most common real fault: an open or missing timing capacitor, which stops the capacitor ever reaching ⅔ VCC and holds the output permanently high.
- ch 7 [low] Section 1, first paragraph: The chapter states flatly that the name comes from three 5 kΩ resistors. That is the popular classroom story, not a documented fact; '555' was a product number chosen by the maker.
- ch 7 [low] Quiz Q4, answer: The frequency line 'f = 1.44/(24.7 × 10³ × 0.1 × 10⁻⁶) = 1.44/2.47 × 10⁻³ = 583 Hz' is ambiguous: read left to right it gives 1.44 ÷ 2.47 × 10⁻³, a very different number.
