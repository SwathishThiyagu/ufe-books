# e-mech-u2: free-model run

- Book: `books/common/e-mech/e-mech-u2.html`
- Status: ok
- Model calls so far: 27 (92,907 tokens in, 213,389 out), 5.1 minutes

## Checker

```
e-mech-u2.html: 9 chapters, 17131 words, 10 figures, 160 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 2, Use 2: The sentence 'Two forces on the same rigid body can be replaced by their vector sum at any point on the common line of action after sliding' is wrong in general. Two forces usually do not share a line of action; what they share is an intersection point. Adding them 'at any point on a common line' only works for collinear forces, and for non-collinear forces the resultant must act at the intersection of the two lines of action, otherwise the moment is not preserved. A student will try to add non-collinear forces at a convenient point on one of the lines and get the wrong resultant position.
- ch 1 [low] Section 3, step 4: 'Keep the perpendicular distance to any moment centre the same' is listed as an action step, but the student does not do anything to keep it the same. It follows automatically from sliding along the line, and listing it as a step suggests the distance must be adjusted by hand.
- ch 1 [low] Section 1, definition of line of action: 'The straight line through the force vector' is loose. The force vector is drawn as an arrow from the point of application, so a student may think the line is only as long as the arrow, or that it passes through the middle of the arrow rather than through the point of application.
- ch 2 [low] Worked example 1, step 8 and answer line (repeated in quiz Q6): "Clockwise when you look along +x" is ambiguous. If a student reads it as standing at the origin and looking in the +x direction, then +y is up and +z is to the right, so the negative moment would appear anticlockwise, the opposite of what is written. The stated sense is right only for a viewer on the positive x side looking back at the origin.
- ch 2 [low] Section 1, second paragraph: "A force at the same distance but more perpendicular gives a larger moment" is unclear about which distance. If the distance means the perpendicular distance d, then M = F d is unchanged and the sentence contradicts the formula.
- ch 3 [high] Section 2, proof: The proof says the vertical component has a lever arm 'about the x-axis direction of turning'. In a planar problem the moment about O is about an axis perpendicular to the plane (the z-axis), not the x-axis. This can mislead students about which axis the moment is taken about.
- ch 3 [high] Worked example 1, step 6: The line of action is described as passing 'above and to the left' of O. For the given data the line crosses x = 0 at y = 1 − 3 tan 30° ≈ −0.73 m, so it passes below O; the closest point on the line is down and to the right of O. The sign is still anticlockwise, but the stated geometry is wrong.
- ch 3 [low] Section 1, formula: The formula writes M_O = F₁d₁ + F₂d₂ + … with d_i defined as perpendicular distances. Perpendicular distances are normally positive, so the formula as written can look like it always adds magnitudes, while the next sentence requires a clockwise term to be negative.
- ch 3 [low] Worked example 2, step 5 and answer: Step 5 gives 107 N·m 'to three figures', but the answer gives 106.8 N·m. The values are consistent only at different rounding precision, which can confuse a student checking the working.
- ch 4 [high] Section 1: The three-dimensional rule given is wrong/ambiguous: "curl the fingers from the first force toward the second, and the thumb gives the couple vector." The two forces of a couple are antiparallel, so there is no unique way to curl from one to the other, and a student following this can get the opposite sense.
- ch 4 [high] Worked example 1, step 6: "the same 72 N·m clockwise couple is the moment about any other point of the plate; only the force at that other point would change" is wrong and contradicts Q6. If the translation is made to another point O', the force vector is unchanged, but the couple becomes r' × F, which is not 72 N·m. Only a couple by itself has the same moment about every point; a force-couple system does not.
- ch 4 [low] Section 2: "The position terms cancel in pairs, and the sum is still F d" skips the actual step. The two position terms do not cancel to zero; they combine into one term.
- ch 4 [low] Beyond: "a force and a couple at a point are packaged as a wrench" is loose. A general force plus couple reduces to a wrench only after a suitable choice of point; a wrench is a force together with a couple parallel to that force.
- ch 5 [low] Section 3, formula for θ: θ = tan⁻¹(R_y / R_x) gives the correct angle from the +x axis only when R_x > 0. With R_x < 0 the inverse tangent returns a first-quadrant angle, so the stated direction is wrong for forces pointing into the second or third quadrant.
- ch 5 [low] Section 2, third bullet: The bullet says a wrench appears when R is parallel to M_O. That is only the special case. After the perpendicular part of M_O is cancelled, any system with R ≠ 0 and R·M_O ≠ 0 is a wrench, with the leftover couple being the component of M_O along R, which need not equal M_O itself.
- ch 5 [low] Section 1, formula line: The chain 'M_O = Σ M_O = Σ (r × F)' defines the total moment using the same symbol for the total and for each individual term, so a student cannot tell what is being summed.
- ch 6 [low] Section 1, table row 'Short link or cable': The table treats a link and a cable the same. A cable or rope can only pull; a student may draw a cable reaction pushing on the body.
- ch 6 [low] Section 1, table row 'Slider or guide': 'One force normal to the guide' is true only for a smooth collar free to rotate on the rod. A square slider held in a guide also prevents rotation.
- ch 6 [low] Section 3, determinacy count: The count of three unknown reactions is treated as sufficient for stability. Three reactions that are all parallel, or all concurrent, still leave the body free to move.
- ch 6 [low] Section 2, last line: 'one arrow for a roller, two for a pin, three for a fixed support' compares arrows with components. A fixed support has two force arrows plus a moment, not three force arrows.
- ch 6 [low] Section 2, bullet list and the paragraph after it: The negative-answer rule is stated in the bullet list and then stated twice more in the following paragraph, which makes the page slower to read than it needs to be.
- ch 7 [low] Quiz Q7: The conclusion is right but the reason is garbled and misleading. The equations do not 'differ only by a force term common to them'. For points A, B, C on one line, ΣMB = ΣMA + (distance AB) × (component of ΣF perpendicular to that line). So any two of the moment equations force that transverse force sum to zero, and the third equation then adds nothing.
- ch 7 [low] Section 2 (other valid sets): The chapter allows replacing one force equation by a moment equation about a second point, but never states the condition for this set to be independent. Without it, a student can pick a forbidden combination and lose an equation.
- ch 7 [low] Figure 'Equilibrium recipe': The node 'Check unknowns ≤ 3, else indeterminate' is placed after 'Solve reactions', which suggests the count is checked after solving. The count must be made on the free body diagram, before any equation is written.
- ch 8 [high] Beyond: The statement says the three-force concurrency test checks whether a linkage can be in static equilibrium under three applied forces. The rule applies to a single rigid body, not to a linkage made of several bodies. A linkage needs each link analysed separately.
- ch 8 [low] Quiz Q6: The question says two known lines meet at P, so they are not parallel. The answer adds 'or be parallel to the other two if they are parallel', which is irrelevant here and can confuse the reader.
- ch 9 [high] Section 2: The principle and the method: The sentence says that if δU is not zero for some allowed displacement, 'the system can move that way.' For negative δU the active forces oppose the assumed displacement; the system tends to move opposite to it, and the reverse displacement gives positive work.
- ch 9 [high] Quiz Q7: The answer says the system 'can move that way' when δU is negative. Negative δU means the active forces do negative work for that displacement, so they tend to move the system opposite to it; the reverse displacement gives positive work, so the system is not in equilibrium.
