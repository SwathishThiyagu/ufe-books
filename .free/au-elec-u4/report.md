# au-elec-u4: free-model run

- Book: `work/au-elec-u4/tree/books/auto/au-elec/au-elec-u4.html`
- Status: ok
- Model calls so far: 24 (86,824 tokens in, 189,197 out), 5.7 minutes

## Checker

```
au-elec-u4.html: 6 chapters, 18930 words, 8 figures, 194 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Quiz Q6, answer: The answer says 'g/km is vehicle mass per km'. Read literally, g/km becomes the mass of the vehicle per kilometre, which is meaningless. The unit is the mass of pollutant emitted per kilometre driven.
- ch 1 [low] Lead, first sentence: The definition says an emission standard limits 'pollutant mass per kilometre', but particle number (PN) is a count per kilometre, not a mass. The definition is narrower than the standards it introduces.
- ch 1 [low] Section 2, electronic control sentence: 'The ECU holds λ = 1' reads as if it applies to every engine in the chapter, but the chapter has just discussed diesel particulate filters. A diesel engine runs lean (λ well above 1); it does not hold λ = 1.
- ch 1 [low] Section 2, cross-reference: 'See 4.5 and 4.6.' is a bare number reference: the reader is not told what those units cover, and on a phone the numbers are not tappable.
- ch 1 [low] Section 2, first paragraph: 'India copied it as Bharat Stage I to BS VI' suggests BS VI is an exact copy of Euro 6. BS VI is based on Euro 6 but has India-specific differences, such as real-driving emission testing introduced later than in Europe.
- ch 2 [high] Section 1, first paragraph and the formula where-list: The comparison sign is missing twice: "λ  1 is lean" reads as a broken sentence, so the definition of lean (λ > 1) is never actually stated, and the same gap appears again in "λ is dimensionless, with λ = 1 stoichiometric, λ  1 lean".
- ch 2 [low] Section 2, bullet list: The reaction equations are not balanced: "CO + O2 → CO2" and "HC + O2 → CO2 + H2O" break mass balance and a student may copy them into an answer book as written.
- ch 2 [low] Section 2 (EGR paragraph), Section 3 summary and Quiz Q5: "It costs some fuel economy" is stated as a rule. In standard texts EGR at part load has little effect on fuel economy, and often slightly improves it by cutting pumping losses and allowing more spark advance; only very high EGR rates hurt economy. The cost is a real simplification that contradicts the usual textbook statement.
- ch 2 [low] Section 3, first paragraph on CO2: "CO2 comes from the carbon in the fuel, not from incomplete combustion" can be misread as saying CO2 does not come from combustion at all.
- ch 3 [high] Section 1, last paragraph (BMEP): The text defines brake mean effective pressure as torque divided by swept volume. That ratio is only proportional to BMEP; the standard definition is brake work per cycle divided by swept volume, which for a four-stroke engine is 4πT/V_d. As written a student who computes T/V_d gets a number about 12.6 times too small and not in the correct relation to the textbook formula.
- ch 3 [low] Lead: "BSFC is the mass of fuel spent for each unit of power produced" is dimensionally loose: BSFC is mass of fuel per unit of energy (work) delivered, not per unit of power. A student may take the definition literally and think the unit is g/kW.
- ch 3 [low] Lead: "a badly matched engine can be thirsty at both" does not say at both what, so the sentence is unclear.
- ch 4 [high] Lead: The lead says the loop exists because a three-way catalyst needs λ held within one percent of 1, then says "Every modern petrol and diesel engine uses this loop". A diesel always runs lean (λ well above 1), has no stoichiometric three-way catalyst, and controls fuel quantity directly; it uses an ECU but not this λ = 1 feedback loop. A student will conclude diesels hold λ = 1.
- ch 4 [low] Section 1: λ is used throughout but never defined as a ratio; "λ = 1, the stoichiometric air-fuel ratio" reads as if λ is itself the air-fuel ratio. Students then cannot say what λ = 1.05 means.
- ch 4 [low] Section 1: The switching oxygen sensor is described only as switching "sharply from lean to rich". The actual voltage values (about 0.1 V lean, about 0.8 to 0.9 V rich for a zirconia sensor) are what the ECU compares against its threshold, and their absence leaves the description incomplete.
- ch 4 [low] Section 2: "keeps adaptive trims in electrically erasable memory that survives battery disconnection" is not true of all ECUs; many store learned trims in keep-alive RAM that is lost when the battery is disconnected, which is why the vehicle then relearns its mixture.
- ch 5 [high] Section 3, EVAP purge solenoid bullet: The direction of the correction is reversed. Petrol vapour drawn from the canister is extra fuel, so the charge goes rich and the ECU must reduce the injected fuel, not add more. Adding fuel to 'burn the extra fuel' makes no chemical sense.
- ch 5 [low] Section 2, terms below the air-flow formula: MAP is used but never expanded, and the same word 'map' later means the calibration look-up table in the figure. A reader on a phone may confuse the sensor with the table.
- ch 5 [low] Section 2, definition of η_v: Volumetric efficiency is given the range '(0 to 1)'. Well-tuned intake and exhaust systems push η_v slightly above 1 at some speeds, so a student will mark a correct value wrong.
- ch 5 [low] Section 3 and Quiz Q5 versus Section 2: Section 2 estimates air with speed density (MAP and temperature), but the fuel-trim paragraph and Q5 talk about a dirty 'air-flow sensor' and an 'air-flow meter'. Two different air-measurement systems appear without explanation.
- ch 5 [low] Lead paragraph: 'Electronic fuel control measures the air entering the engine' contradicts the speed-density method taught in Section 2, which estimates air from manifold pressure and speed rather than measuring it.
- ch 5 [low] Section 1, last line of the carburettor paragraph: '(see 4.1)' is a bare chapter number with no link, so the student cannot jump to it and the numbering may not match every syllabus.
- ch 6 [low] Section 1, dwell time and dwell angle: The reason given for shortening dwell at 6000 rpm does not hold. In a four-cylinder engine the gap between sparks at 6000 rpm is 5 ms, so 3.0 ms (108 crank degrees) would still fit. A careful student will see the explanation does not force 2.0 ms, and may wrongly conclude dwell angle can never exceed 180 degrees.
- ch 6 [low] Section 1, dwell time paragraph: 'It is fixed for a given coil and battery voltage' is contradicted later in the same section, where dwell is shortened at high speed. The student cannot tell whether dwell time is fixed or not.
- ch 6 [low] Worked example 1, step 4: 'The coil must close 54 degrees before the spark falls' is unclear; the spark does not 'fall', it occurs and then ends.
- ch 6 [low] Beyond, per-cylinder knock detection: 'Either with a separate sensor per bank or by measuring ion current' does not give per-cylinder detection: one sensor per bank only locates knock to a bank of cylinders.
- ch 6 [low] Section 3, correction table introduction: 'added as angles before the coil is charged' is ambiguous; the student may think the correction is applied to the charging instant rather than to the spark advance.
