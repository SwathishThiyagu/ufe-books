# me-design-u7: free-model run

- Book: `books/mech/me-design/me-design-u7.html`
- Status: ok
- Model calls so far: 31 (115,769 tokens in, 292,166 out), 8.9 minutes

## Checker

```
me-design-u7.html: 9 chapters, 16634 words, 10 figures, 167 KB
OK
```

## For the reviewer

- chapter 5: the figure cannot be drawn: note "√((d1/2)²+(d2/2)²)" runs off the right edge; shorten it

## Reviewer notes (after any revision)

- ch 1 [low] Section 2, inch units sentence: The text says 'Some syllabi call m the metric module and P the English module'. P is the diametral pitch, in teeth per inch. The English (inch) module is the reciprocal, 1/P = d/z with d in inches, and its unit is inches. Calling P the English module contradicts the standard definitions.
- ch 1 [low] Section 2, pressure angle definition: 'The angle between the common normal at the pitch point and the common tangent' leaves the tangent undefined; a student can read it as the tangent to the tooth profile or to the line of centres.
- ch 1 [low] Section 2, nomenclature: The addendum circle and dedendum circle are never defined, but Exam trap 1 uses 'the addendum circle' and students need it for any drawing question. Tooth thickness and space width are also left out of a section titled nomenclature.
- ch 1 [low] Quiz Q8, answer: 'The cutter removes material from the pinion root to avoid interference' reads as if undercutting is a cure. Undercutting is the damage that interference causes during generation; it is not done on purpose.
- ch 2 [low] Section 1, pinion rule paragraph: The sentence 'a 20-tooth pinion driving a 60-tooth gear makes three times the cycles, because it meets every gear tooth once per revolution' gives the wrong reason. Meshing once per revolution is common to both wheels; the 3× comes from the speed ratio, since the pinion turns three times for each turn of the gear.
- ch 2 [low] Section 3, grey cast iron paragraph: The figure 200 MPa is the tensile strength of grade FG 200, not its bending (flexural) strength, which is higher. Written as bending strength it can mislead a student comparing it with tooth bending stress.
- ch 2 [low] Section 2, nitriding bullet: A case hardness of 500–600 HV is at the bottom of the nitrided range. Typical gas-nitrided cases reach about 600–750 HV on Cr-Mo steels and above 900 HV on nitriding steels, which is why nitriding is chosen for wear resistance.
- ch 2 [low] Worked example 1, step 6: The 30–50 BHN rule applies to through-hardened pairs. Comparing a case-carburised pinion quoted in HRC with a gear quoted '30–50 BHN softer' mixes two hardness scales and suggests a through-hardness no alloy gear can reach (58 HRC is roughly 650 BHN).
- ch 2 [low] Quiz Q6: 'Reduce the ratio' is offered as a fix for pitting, but a lower ratio only reduces the cycle difference; the lives are still unequal at equal hardness and nothing about the load capacity improves.
- ch 3 [high] Section 1, first paragraph: "The tangential force Ft acts near the pitch point" is wrong and contradicts the lead and the quiz answer. Lewis puts the whole load at the tooth tip (one tooth carrying everything), because that gives the largest bending moment at the root. The pitch point is not the worst case.
- ch 3 [high] Section 1, second paragraph ('An equivalent form is σb b πm Y, with Y = πy'), repeated in Exam trap 4: The relation between the two forms of the Lewis equation is inverted. From σb b m y = σb b π m Y it follows that Y = y/π, not πy. As written, σb b π m (πy) = π² σb b m y, about 9.9 times too large. With y = 0.32, the π-form factor must be about 0.10, not 1.0.
- ch 3 [high] Section 2 last paragraph, Section 3 design order, Exam trap 5: The bending check compares the static force Ft with the beam strength, while the wear check uses the dynamic load Fd. Section 2 itself says "the dynamic load is what the tooth actually feels", so leaving it out of bending is inconsistent and understates the bending load. Standard treatments compare the dynamic (effective) load with both limits.
- ch 3 [low] Section 1, third paragraph: "a small tooth has a stubbier, more highly stressed root" is misleading. A stubby tooth is stronger. With fewer teeth the involute flank is more sharply curved and the root is relatively thin, and below about 17 teeth a 20° full-depth tooth is undercut.
- ch 3 [low] Section 2, velocity factor paragraph: Most Indian textbooks use a velocity factor Cv less than 1 and divide: effective load = Ft/Cv. The factor greater than 1 that multiplies is the AGMA/Shigley dynamic factor Kv. A student will use the wrong symbol direction. The sentence "Do not apply Cv and Fd without knowing which method your syllabus uses" is also unclear.
- ch 3 [low] Exam trap 2: "Forgetting v, or forgetting the velocity factor Cv, gives a force that is too low" does not say what error is meant; leaving v out of Ft = P/v does not by itself give a force that is too low.
- ch 4 [high] Section 2 (modified Lewis equation): The equation is written σ = Ft / (Cv b mn y) with y called the Lewis form factor read for zv. With the standard Indian textbook tooth form factor y (values around 0.1, e.g. y = 0.154 − 0.912/zv ≈ 0.11 for zv = 22), the π factor is missing. As printed, the calculated bending stress comes out about 3.14 times too small, so a tooth that is actually overstressed passes as safe — an unsafe design.
- ch 4 [low] Section 2, first sentence of the virtual teeth part: 'The normal section of a helical tooth is an ellipse' is loose: it is the intersection of the normal plane with the pitch cylinder that is an ellipse, not the tooth section itself. A student may picture the tooth cross-section as an ellipse.
- ch 4 [low] Quiz Q6 answer: 'each bearing must take its gear's thrust' suggests both bearings of a shaft carry thrust. In normal practice one bearing is located to take the thrust and the other is free to float axially.
- ch 5 [high] Section 2 (torque formula): The torque formula is printed as T = 60×106 P/(2πN). As shown, 106 is a plain number, so the result is wrong by a factor of about one million. The power of ten has lost its superscript (compare the correctly written 60×10⁶ elsewhere in the same sentence pattern). A student who copies this gets nonsense units for T.
- ch 5 [low] Worked example 1, step 4: The step says the face width is 'close to the R/3 limit', but b = 30 mm is slightly more than R/3 = 89.44/3 = 29.81 mm, so the example breaks the rule stated one section earlier (b ≤ R/3).
- ch 5 [low] Quiz Q6 (answer): 'a component Wt tan φ in the plane of the tooth' is vague; there are many planes containing the tooth, and a student may place the component wrongly and then swap the sine and cosine terms.
- ch 6 [high] Section 1 (geometry): The effect of q on worm thickness and lead angle is reversed. Since d1 = q m, a small q gives a thin (slender) worm and a large tan λ = zw/q, and a large q gives a thick worm and a small λ. The chapter says the opposite.
- ch 6 [low] Exam traps, fifth bullet: The comparison sign is missing: 'Self-locking is λ  φ' leaves the reader without the actual condition and could be misread as λ > φ.
- ch 7 [high] Section 2, first paragraph: "Fixing two members drives the third" is wrong. The sun–planet–ring train has two degrees of freedom. If you fix two members the train locks solid and the third member cannot move (this is exactly the clutch lock-up used for direct drive).
- ch 7 [low] Section 2 and its table: Notation switches between lowercase z_s, z_p, z_r in the text and capital z_S, z_R in the formula block, so the reader has to guess they are the same symbols.
- ch 7 [low] Section 2, table and figure: The numbers 24, 18 and 60 quietly rely on the geometry relation between the three gears, but the relation is never given, so a student cannot check whether any three tooth numbers are possible.
- ch 8 [high] Worked example 1, step 4: The step is written as "Peq = 665.61/3 = 8.73 kW". Read literally, 665.61 divided by 3 is 221.87, not 8.73. The cube-root sign has been lost, so the shown arithmetic does not match the answer and a student copying the line will get a wrong number.
- ch 8 [low] Quiz Q3: Same lost cube-root notation: "Peq = 2881/3 = 6.60 kW" reads as 2881 ÷ 3 = 960.3. The answer 6.60 kW is correct but the line as printed is not.
- ch 8 [low] Section 1 and Section 2 (prose): Powers of ten and squares/cubes lose their superscripts in the running text: "5.76×108 cycles", and in Section 2 "Peq = (Σ pi Pi3)1/3". As printed the first reads as about 622 cycles and the second as Pi times 3, which is not the formula.
- ch 8 [low] Figure (Gearbox design flow), node 'Gear size': The note under 'Gear size' is '6×10⁸ cycles', which is a life in cycles, not a size. It repeats the life already fixed in the load-spectrum step and can confuse a student into thinking the size is quoted in cycles.
- ch 9 [low] Section 2 (ray diagram and structure formula), ray description: 'Parallel rays mean equal ratio steps' is misleading. Rays inside one group are not parallel: they fan out, and the equal step ratio appears as equal vertical spacing between neighbouring rays. Two parallel rays mean the same transmission ratio appearing twice, not 'equal ratio steps'.
- ch 9 [low] Section 2, sentence on vertical rise: 'The vertical rise of a ray equals log φ for that step' is not right. A ray spans one gear pair, so its rise is log of that pair's ratio, which is a whole number of log φ intervals (the characteristic times log φ), not log φ itself.
