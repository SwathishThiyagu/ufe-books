# e-mech-u1: free-model run

- Book: `books/common/e-mech/e-mech-u1.html`
- Status: ok
- Model calls so far: 29 (114,352 tokens in, 217,872 out), 6.0 minutes

## Checker

```
e-mech-u1.html: 7 chapters, 13858 words, 8 figures, 138 KB
OK
```

## For the reviewer

- chapter 2: the figure cannot be drawn: note "vector, AB sin θ" runs off the right edge; shorten it
- chapter 2: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [high] Worked example 1, step 2: The divisor carries the wrong unit. Writing 245.25 N ÷ 9.81 m/s² gives 25 kg, not 25 kgf, because N ÷ (m/s²) = kg. The conversion factor must be 9.81 N/kgf; as printed, the units do not cancel to kgf and a student learns that g has units of N/kgf.
- ch 1 [low] Section 3: 'Every correct equation is homogeneous' is stated too strongly. Empirical formulas fitted to data (for example pipe-friction or heat-transfer correlations) carry dimensional constants and are deliberately not homogeneous; students meet them later and the absolute claim confuses them.
- ch 1 [low] Quiz Q4: The kinematics example says 'a projectile's path under fixed g'. Mentioning g brings in the cause of the motion, which the definition just said kinematics ignores, so the example sits awkwardly against its own definition.
- ch 2 [low] Section 3, dot product: The chapter gives only A·B = AB cos θ, but the worked example and quiz Q3/Q6 all compute the dot product from components. The component rule is used but never stated, so a student revising from the formulas alone cannot reproduce those steps.
- ch 2 [low] Section 2, scalar multiplication: "Multiplying by a scalar c changes the size to |c|B" mixes the vector name B with its magnitude B, which was written A for the vector and A for the magnitude in Section 1. The zero case is also not mentioned.
- ch 2 [low] Section 1, notation: The magnitude is called "a positive scalar". The magnitude of the zero vector is 0, so it is not always positive.
- ch 2 [low] Worked example, steps 2 and 4: "tan−1(7/7)" as printed can be read as tan minus 1 rather than the inverse tangent.
- ch 3 [low] Section 2, oblique resolution (the sentence "The angle opposite F is the angle between the two chosen lines"): The two statements about P and Q are correct, but the third is geometrically wrong. In the force triangle OAC (OA = P along line a, AC = Q parallel to line b, OC = F), the interior angle opposite F is the angle at A between AO (opposite to line a) and AC (along line b), which is 180° − α, not α. A student who draws the triangle will measure 105° for the 0°/75° case and think the text is wrong. The numbers still come out right only because sin(180° − α) = sin α.
- ch 4 [high] Exam traps, bullet 1: The stated cure for a negative Rx contradicts the quadrant table in Section 2. The rule 'use |Ry/Rx| and add 180 deg when Rx < 0' gives the wrong direction in the second quadrant: for Rx = -30 N, Ry = +40 N it produces 180 deg + 53.1 deg = 233.1 deg, but the true direction is 180 deg - 53.1 deg = 126.9 deg (third quadrant is the only case where 180 deg + alpha applies).
- ch 4 [low] Worked example 1, step 8: Step 8 says the polygon 'confirms both totals', but the figure was drawn from those same two totals, so it cannot independently confirm them, and Section 3 itself warns that a sketch is not proof.
- ch 4 [low] Section 2, formula for alpha: alpha = tan^-1(|Ry|/|Rx|) breaks down when Rx = 0 (division by zero), and the chapter never says what to do in that case, which happens often (forces acting vertically).
- ch 5 [high] Worked example 1, step 7 (check): The check states that T² + N² should not equal W² because the reactions and the weight are 'not at right angles to each other in that way'. This is false. T acts along the plane and N is perpendicular to the plane, so T and N are at right angles. Together they balance the weight: T + N + W = 0, so |T + N| = W, and because T ⊥ N, T² + N² = W² exactly. The numbers given (2406 + 7218 = 9624 = 98.1²) actually confirm it, so the sentence contradicts its own arithmetic and teaches the wrong geometry.
- ch 5 [high] Section 3, third bullet: The bullet heading reads 'The reaction that a support would give if it were still attached' as something that never appears on the diagram, then says 'only its reaction remains'. That is self-contradictory and flatly contradicts step 4 of Section 2, where the reaction must be drawn. A student can read this as 'do not draw the reaction', which is the exact mistake the chapter is trying to prevent. What must not appear is the support itself, not its reaction.
- ch 5 [low] Worked example 2, steps 1 and 2: Step 1 correctly says the body is the knot and 'the lamp's rope becomes a downward force', but step 2 then calls that force 'weight of the lamp W = 4 × 9.81 = 39.24 N down'. The lamp's weight acts on the lamp, not on the knot; what acts on the knot is the tension in the short rope, which equals 39.24 N here only because the lamp hangs in equilibrium.
- ch 5 [low] Figure spec, aria label: The aria text calls it 'A five-step flowchart', but the figure has six boxes and six steps, matching the six steps of Section 2. The rest of the aria sentence lists six items, so the count contradicts the drawing.
- ch 5 [low] Quiz Q6, answer: The answer says the correct diagram has 'three arrows', then adds the string tension only 'if a string is present'. For the smooth plane described in the question there are just two arrows (W and N), so the count and the condition do not match.
- ch 6 [low] Section 1, bullet list of procedure (the sentence after the two scalar-equation formula): 'Three unknown magnitudes cannot be found from statics alone; the problem needs stiffness or a support reaction elsewhere' is misleading. On a single particle, adding a support reaction elsewhere does not supply extra information — it only adds a fourth force and a fourth unknown. A student may think the fix is to invent a reaction.
- ch 6 [low] Section 2, proof: 'Replacing each triangle angle by the sine of the angle between the other two forces' is written loosely: an angle is not replaced by a sine. A careful reader may lose the thread of the proof at the last step.
- ch 6 [low] Section 3, paragraph on measuring angles: 'Measure each angle between the two force lines themselves, take the smaller angle at the knot, and check that the three angles add to 360°' mixes up lines and rays. Angles between undirected lines never exceed 90° and cannot add to 360°; only angles between the force directions (rays leaving the knot) add to 360°.
- ch 6 [low] Exam traps, last bullet: 'Typing sin 120 as a negative number' is confused. In degree mode sin 120° is +0.866, so no calculator gives a negative value here. The real trap is believing that the sine of an obtuse angle is negative.
- ch 7 [high] Section 3, sentence on cables: It says a cable 'pulls the particle away from the support'. A cable tension on the particle acts along the cable from the particle toward its support, so the cable pulls the particle toward the support, not away from it. This contradicts quiz Q5, which states the correct direction.
- ch 7 [low] Section 3, sentence on struts: 'A strut can push or pull' is loose; in most textbooks a strut is a compression member and a tie is a tension member, so calling a strut a member that may pull can confuse the sign convention.
- ch 7 [low] Beyond: 'when the load is small compared with the slings' has no clear meaning; the real condition for treating a spreader bar as a particle is that its size (and its own weight) can be neglected.
