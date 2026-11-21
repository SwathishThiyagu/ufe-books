# ce-survey-u4: free-model run

- Book: `books/civil/ce-survey/ce-survey-u4.html`
- Status: ok
- Model calls so far: 28 (106,514 tokens in, 284,095 out), 8.1 minutes

## Checker

```
ce-survey-u4.html: 8 chapters, 14944 words, 9 figures, 151 KB
OK
```

## For the reviewer

- chapter 3: the figure cannot be drawn: tree label "Different axis level" is too long; shorten it
- chapter 3: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [high] Section 1, last paragraph, and Exam trap 3: The chapter says 'Swinging the upper part through 180° about the vertical axis is a different action: it changes face', and Exam trap 3 repeats that changing face is just swinging the upper part. This contradicts the standard definition. Changing face is the two-step operation: transit the telescope about the horizontal axis, then swing the upper plate 180° so the same target is sighted again with the vertical circle on the other side. A swing on its own only sends the telescope to a different direction; it does not put the observer on the other face of the same target.
- ch 1 [low] Section 4 table, Diaphragm test row: The 'what it checks' entry is 'Vertical hair lies in the plane of the line of collimation'. The vertical hair always lies in that plane by definition, so the entry does not say what the test is for. The adjustment is to make the vertical hair truly vertical, that is, perpendicular to the horizontal axis, so that raising or lowering the telescope makes a fixed point stay on the hair.
- ch 1 [low] Section 2 table, Telescope row: 'The screw slides the objective to focus' is only true of external-focusing telescopes. Most instruments a student will meet are internal-focusing, where the objective is fixed and the screw moves a small focusing lens inside the tube.
- ch 1 [low] Section 3, third bullet: Two foot screws are turned 'towards each other'. The direction depends on where the bubble is: the thumbs go towards each other or away from each other, whichever walks the bubble to the centre. A student with the bubble at the far end of the tube will turn the wrong way by following the text literally.
- ch 1 [low] Section 1, third paragraph: 'Adjustment is nothing but restoring three right angles' sets up only three conditions, but Section 4 lists six adjustments. Two of the extra three are not right-angle conditions: the altitude (telescope) level must be parallel to the line of collimation, and the vertical-circle index must read zero on a horizontal sight.
- ch 2 [high] Exam traps, first trap ('Face right read at face value'): The trap names a face-right mistake but the cure given ('reduce B by 180° and leave A alone') is the rule for the two verniers inside one face. It does not fix a face-right reading. A student who follows it will average the faces wrongly, because on face right the reading of the same direction is about 180° away from its face-left value.
- ch 2 [high] Section 3, list of errors, 'Vertical axis not truly vertical': It says to 'level carefully and use both faces', implying both faces remove this error. They do not. The reading for a given target direction depends only on the circle's orientation and the sight direction; both are the same on face left and face right, so the error is the same on both faces and does not cancel. Standard texts list this as an error not eliminated by double sighting.
- ch 2 [high] Section 2 (direction method, correction formula) and Quiz Q6: The correction is described as a flat amount per direction ('correction per direction = −e/m', 'subtract 6″ from each observed direction'). Applied flat, the horizon still does not close: the closing sight of the reference is still short by m·(e/m) − e/m. The correction must be cumulative over the angles, as in the standard reduction.
- ch 2 [low] Section 1, step 'Read both verniers': 'Take minutes and seconds from the vernier whose zero lies inside the main-scale interval' is unclear: every vernier zero lies between two main-scale marks, and the two verniers A and B are read separately.
- ch 2 [low] Section 3, 'Check the letters H and Z on the circle': The vertical circle is enclosed inside the instrument and is seen only through the reading microscope, so a student cannot look for letters on it. The practical test is a sight on a nearly horizontal object.
- ch 2 [low] Section 3, list of errors, 'Eccentricity of centres': 'The line of sight misses the instrument centre' does not define eccentricity of centres; it reads like a collimation fault and would confuse the two.
- ch 2 [low] Section 1 and Worked example 1, step 5: For a horizontal angle, half the face difference is not the collimation error of the instrument. It is the error collimation (and any tilt of the horizontal axis) produces in that particular angle, and it falls to zero when both targets are at the same altitude.
- ch 3 [low] Section 1: The definition of ht is circular: 'ht is the target height above the point sighted (m)'. The target is itself the point sighted, so the definition implies ht is always 0 and never explains why the formula subtracts it.
- ch 3 [low] Section 2: H, D_P and D_Q are used without definition. 'Then find H and add instrument height' also does not say which station's instrument height to add.
- ch 3 [low] Section 2, worked example 1 and Quiz Q4: 'Q farther' / 'Q farther away' does not say farther than what. If Q is merely farther from P than some other point but the object lies between P and Q, the single-plane formula fails.
- ch 3 [low] Lead: 'Only a few universities teach this chapter' is a coverage claim about syllabi that is likely wrong and could make students skip a standard surveying topic.
- ch 4 [low] Section 1 and Exam traps (additive constant C): The additive constant is described twice as 'usually between 0 and 0.3 m'. For ordinary external-focusing tacheometers C = f + d is typically around 0.3 m (roughly 0.3 to 0.45 m), and it is near zero only on internal-focusing instruments fitted with an anallatic lens. As written, a student may think any value under 0.3 m is normal for every instrument.
- ch 4 [low] Figure caption ('One sighting, two answers'): The caption states that the intercept and vertical angle give D = 122.46 m, V = 17.65 m 'so the staff station RL is 118.300 m', but the instrument-axis RL (102.500 m) and the mid-hair reading (1.850 m) needed for that RL are not shown. A reader cannot see where 118.300 m comes from.
- ch 4 [low] Section 3 (subtense bar): The chapter gives D = s / (2 tan(θ/2)) but never states that the bar must be set perpendicular to the line of sight, which is the condition that makes that triangle valid. A student could assume the bar may be held at any orientation.
- ch 4 [low] Section 3, last line ('See Unit 5 for that hardware'): The cross-reference to the total station unit is plain text, so the reader cannot jump to it on a phone, unlike other chapter references in the book.
- ch 5 [low] Worked example 1, steps 5–6 and answer: The arithmetic rounds wrongly. 500.000 × 0.84526 / 0.86603 = 488.007 m, so AC rounds to 488.01 m, not 488.02 m; the sum in step 6 and the answer line carry the same slip (511.18 + 488.01 = 999.19 m).
- ch 5 [low] Worked example 1, step 6: Adding BC and AC has no surveying meaning and is not a check of anything; a student may think the sum of two computed sides is a validation step.
- ch 5 [low] Section 2, field work paragraph: The sentence on refraction ends with 'observe on both faces', which corrects instrumental errors (collimation, vertical index) but does not correct refraction. A student may believe both-face observation removes refraction.
- ch 5 [low] Section 1, opening paragraph: 'All angles are observed, typically to about 20″' is a lower-order figure. First- and second-order triangulation angles are observed to a few seconds (about 1″–5″); 20″ applies only to tertiary work.
- ch 6 [low] Section 1, final paragraph: The claim that first-order work is 'an order of magnitude tighter' than 1 in 5000 suggests about 1 in 50 000, which is tighter than the usual first-order figure of about 1 in 25 000 (roughly five times tighter than a minor traverse).
- ch 6 [low] Figure (tree) versus Section 2: Section 2 lists four horizontal methods, but the tree under 'Horizontal' shows only triangulation, traverse and GNSS, so a student may think trilateration is not a horizontal control method.
- ch 6 [low] Section 3, first paragraph: The symbols ΣBS and ΣFS are used in the closing-error formula before they are defined; they are only explained later in Worked example step 1.
- ch 6 [low] Quiz Q3: 'Acceptable only at the limit' is ambiguous; a student may read it as 'not acceptable' because the value is exactly at the limit rather than inside it.
- ch 7 [high] Section 2, after the two-unknown normal equations: The formula σ₀ = √(Σw v²/(n−1)) is only correct for a single unknown. After a two-unknown adjustment the denominator must be n−2, and in general n−u, where u is the number of unknowns. A student may wrongly use n−1 for a two-unknown problem.
- ch 7 [low] Section 1, propagation of variances: The phrase 'relative variances add in outline' is vague. Students may not know what 'in outline' means or whether the rule is exact.
- ch 8 [high] Section 4: The relation sign has been lost: 'A summit falls (g₂  g₁)' reads as nonsense and the definition of a summit curve is unreadable. The missing character is '<'.
- ch 8 [low] Sections 1, 3 and 4 (formulas): The same symbol L is used for three different lengths in one chapter: curve length of the circular arc (Section 1), transition length (Section 3, and L = V³/(CR)), and vertical curve length (Section 4, inside c = N x²/(2L)). A student flipping between sections can substitute the wrong length.
- ch 8 [low] Section 3: 'Centrifugal force V²/R' is dimensionally an acceleration, not a force. The symbol list also never says what V²/R is.
- ch 8 [low] Section 3: e = V²/(gR) gives the equilibrium superelevation as a ratio (rise over run, that is tan θ), not a height in metres. Unstated, students will read e as a length.
- ch 8 [low] Quiz Q3: 250 tan 25° = 116.577 m, which rounds to 116.58 m, not 116.57 m.
- ch 8 [low] Figure: The series labelled 'circular, R = 150 m' plots the parabolic approximation x²/(2R), not the true circular offset R − √(R² − x²). At x = 50 m, x/R = 1/3 is not small: the true offset is 8.58 m but the plotted value is 8.33 m, a 0.25 m gap.
