# me-som-u4: free-model run

- Book: `books/mech/me-som/me-som-u4.html`
- Status: ok
- Model calls so far: 28 (107,570 tokens in, 250,615 out), 6.8 minutes

## Checker

```
me-som-u4.html: 7 chapters, 14074 words, 8 figures, 137 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Quiz Q6 answer: The answer says the second moment is 'Σ A y²'. That is only true when the A are infinitesimal elements. For a composite made of finite rectangles it gives the wrong number, because each rectangle's own I_c is missing. The chapter itself warns about this in the exam traps (do not add only A d²), so the two parts contradict each other.
- ch 1 [low] Exam traps, bullet 1: Saying the centroid 'changes value and sign' when measured from the top instead of the bottom is misleading. The centroid keeps the same position on the section; only the numerical coordinate changes (for example 70 mm from the bottom is 30 mm from the top). A sign appears only if you reverse the positive direction of the axis.
- ch 1 [low] Section 1 (holes): The chapter says a hole is a negative area and that its area and first moment are subtracted. It never says the same rule applies to the second moment, so a student may subtract only A d² for a hole and forget the hole's own I_c.
- ch 2 [low] Section 1: The sentence 'The top fibres shorten, the bottom fibres lengthen' is stated without a sign condition. It is true only for a sagging (positive) moment; for a hogging moment the top fibres lengthen and the bottom fibres shorten. A student may carry the sentence over to overhanging or cantilever regions.
- ch 2 [low] Section 2: The first step says 'Bend a short length of beam to radius R' before R is defined. Students may take R as the radius to the extreme fibre rather than to the neutral layer, which changes the (R + y) length step.
- ch 2 [low] Section 3: 'Shear stress follows a parabolic distribution' is stated for all sections. The parabola is the result for a rectangular section; for an I-section the web shear is nearly uniform, and the shape depends on the section.
- ch 2 [low] Quiz Q3: 'A 40 mm × 80 mm rectangle' does not say which dimension is the depth. The answer silently takes depth = 80 mm and width = 40 mm, so a student who reads it the other way gets a different y and I.
- ch 3 [low] Exam traps, second trap: The phrase 'the depth the beam actually bends over' is unclear. A student may not see which of the two dimensions b and d must be squared, which is the whole point of the trap.
- ch 3 [low] Section 2, table: The rectangle row writes 'Rectangle b × d' without saying that d is the dimension in the plane of bending and b the dimension parallel to the neutral axis. In the table the symbol d is also used for the diameter of the circle in the next two rows, so a reader skimming can carry the wrong meaning across.
- ch 4 [high] Worked example 1, step 8 and answer; Quiz Q5; Exam trap 5: The question asks for the maximum steel stress, but step 8 takes y = 105 mm, the mid-thickness of the plate. That is the stress at the plate centroid, not the maximum. Steel runs from y = 100 mm to y = 110 mm, so the largest steel stress is at the outer face, y = 110 mm. The answer 124 MPa is therefore not the maximum, and trap 5 pushes students towards the same half-right value. Q5 repeats the pattern: y = 84 mm is the plate centre, but the plate extends to y = 88 mm.
- ch 4 [high] Section 1, last paragraph: "without them the steel and timber slide and the stresses are lower than calculated" is wrong for timber. With slip the steel does less work and the timber does more, so the steel stress falls but the timber stress rises, often sharply. This contradicts the chapter's own Quiz Q6 answer.
- ch 4 [low] Lead, and Figure: The definition given (steel plates on top and bottom) is not the arrangement most Indian textbooks draw. The usual picture is a steel plate on each side face of the timber joist, or a single steel plate sandwiched between two timber joists, bolted through. A student meeting the standard exam figure may not connect it to this chapter.
- ch 4 [low] Worked example 1, steps 7 and 8; Quiz Q5 answer: Expressions such as "30 × 10⁶ × 100 / 5.08 × 10⁸" are ambiguous: read left to right they give the wrong value. The same happens in Q5 with "20 × 20 × 10⁶ × 84 / 2.08 × 10⁸".
- ch 5 [high] Section 3, weld pitch sentence: The instruction 'divide by weld strength per mm to get pitch' is technically wrong. Shear flow q is in N/mm. Dividing q by a weld strength in N/mm gives a dimensionless number, not a pitch in mm. The pitch also depends on how much weld length is laid in each pitch.
- ch 5 [low] Section 2, hollow circle/box paragraph: The sentence 'The peak is not always at the geometric centre if the width changes' is placed right after hollow circle and box, where the peak is at the centre; it can mislead students into thinking the hollow-circle peak is elsewhere. Also, for a box section at a web level, b is the total width of the two webs, not one wall thickness.
- ch 6 [high] Section 1: The sentence 'its centroid sits inside the web' is wrong. For a thin-walled channel the centroid lies between the web and the flange tips, on the flange side (about 25 mm from the web centreline for the b = 100 mm, h = 200 mm channel). Saying it sits in the web makes the centroid-to-shear-centre distance look like 37.5 mm when it is about 62.5 mm, and it puts the centroid in the wrong place for the whole chapter.
- ch 6 [high] Exam trap 1: Repeats the same error: 'The centroid lies inside the web'. A student who memorises this will draw the centroid on the web centreline and measure the load eccentricity from the wrong point.
- ch 6 [low] Quiz Q7 (the same wording appears in worked example step 6): The answer says 'the shear flow ... is proportional to t'. It is not: q = VQ/I has Q proportional to t and I proportional to t, so q itself is independent of t. Only the first moment of area Q and the second moment of area I are proportional to t. As written, a student would learn the wrong reason for t cancelling.
- ch 7 [high] Section 3 (beams of uniform strength): The shapes given are wrong for the loading stated. With width held constant, Z = bd²/6 ∝ d², so depth must vary as √M. For a cantilever with an end point load M ∝ x, giving d ∝ √x — a parabola in side view, not a triangle. The triangular side view (d ∝ x) belongs to a cantilever under a UDL, where M ∝ x². The simply supported UDL case is only parabolic if the depth is held constant and the width follows M.
- ch 7 [high] Section 2, last paragraph: "No amount of extra depth will rescue it — you need area" is false. Adding depth increases the area A = bd in proportion, so it lowers τ_max = 1.5V/A exactly as widening does. A student will remember that depth is useless against shear, which is wrong.
- ch 7 [low] Quiz Q6 answer: "Deepening alone barely helps because τ depends on area, not on d²" repeats the misconception of Section 2. It does help, linearly, because it adds area.
- ch 7 [low] Quiz Q7 answer: "Every fibre is at the allowable stress" is not true. Only the extreme fibre of each cross-section reaches σ_allow; the stress falls to zero at the neutral axis.
