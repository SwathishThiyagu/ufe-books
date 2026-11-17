# e-bee-u2: free-model run

- Book: `books/common/e-bee/e-bee-u2.html`
- Status: ok
- Model calls so far: 24 (94,883 tokens in, 186,226 out), 5.3 minutes

## Checker

```
e-bee-u2.html: 7 chapters, 13262 words, 8 figures, 140 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 1: The text says 'The flux linking the coil is B A cos ωt' and then 'Flux linkage changes as cos ωt', but the emf formula uses N turns. A student can lose track of where N comes from: BA cos ωt is the flux through one turn, while the flux linkage of the whole coil is N times that.
- ch 1 [low] Section 2, half-cycle average bullet: 'Half-cycle average: use in rectifier calculations' is vague and can mislead. A half-wave rectified sine has full-cycle output average Vm/π ≈ 0.318Vm, not 0.637Vm; 0.637Vm is the half-cycle average of the original sine (and the full-cycle average only of a full-wave rectified sine).
- ch 2 [high] Section 3, the capacitor sentence: The conclusion is wrong for an AC-rated capacitor. An AC voltage rating is an RMS rating, so a 250 V AC capacitor is fine on a 230 V RMS supply; the peak of 325 V is already covered by the rating (its own peak rating would be about 354 V). Only a DC-rated capacitor would be stressed by the 325 V peak.
- ch 2 [low] Section 3, last sentence: "High crest factor warns of pulses that heat equipment more than a sine of the same RMS" reads as if heating depends on the shape. In a plain resistor, the same RMS gives the same heating. The extra heating comes from losses that depend on peak current (winding eddy and skin effects, diodes, capacitors) in real equipment.
- ch 3 [high] Section 1: The sentence "if φ 1 lags" is garbled and reads as nonsense. The sign rule for lagging is never stated, so a student cannot tell what a negative φ means.
- ch 3 [low] Section 2: The exponential form is written as "r ejθ" with no superscript, so it can be misread as r × e × j × θ rather than r·e^(jθ).
- ch 3 [low] Lead: The lead calls the phasor "a rotating arrow", but Section 1 later says the rotation is frozen and the frozen arrow is the phasor. The two statements pull in opposite directions.
- ch 4 [high] Section 3, table (second data row): The condition for the capacitive row has lost its comparison sign and reads "XL C", which is not a condition at all. A student cannot tell that this row means the case where the capacitive reactance wins.
- ch 4 [low] Worked example 1, dry run and output: The dry-run table numbers the six rows 1–6, but in the worked example those same quantities are steps 2–7. The output block also prints nine bare numbers with no labels or units and no row for the three element voltages in the table, so the reader has to guess which number is which.
- ch 5 [high] Section 2, last sentence: The sentence says that mixing peak voltage with RMS current needs "the correct 1/2 or 2 factor". That factor is wrong: Vm × Irms = √2 × Vrms × Irms, so the correction factor is 1/√2 (about 0.707), not 1/2 or 2. A student who follows this will get a power that is 41% too large.
- ch 5 [low] Section 2 table: The column is headed simply φ, but it lists +90° for a pure inductor while the current phasor angle for that load is −90°. A student can read φ here as the current's angle and then get the sign of Q backwards.
- ch 6 [low] Section 2 and the figure: The text calls A, B and C the three windings ("Join one end of each winding A, B and C to a common point N. Leave the other ends as the three line terminals"), but the star drawing uses A, B and C as the outer nodes joined to N, so it looks like A, B, C are the line terminals and there are no line terminals shown at all. A student comparing text and figure cannot tell where the three lines leave the star.
- ch 6 [low] Beyond: "Delta windings block zero-sequence current from the line side" is loosely worded. A delta winding does not block zero-sequence current; it gives zero-sequence current a closed path inside the triangle, so such current circulates in the delta and does not appear in the line conductors.
- ch 7 [high] Exam traps, second bullet: The bullet says 'Do not use the angle between a line voltage and a line current.' In a balanced circuit this angle is exactly φ, the same load angle. In star, line current equals phase current and line voltage is the corresponding phase voltage shifted by 30°, so the angle between them is unchanged. In delta, line voltage equals phase voltage and line current is the phase current shifted by 30°, again unchanged. The warning is therefore false for every balanced case this chapter covers and can make a student distrust correct working.
- ch 7 [low] Section 1: The chapter derives the √3 magnitude but never states the phase shift between line and phase voltage. Students are commonly asked for this, and it is also the reason the line-current derivation in delta works.
