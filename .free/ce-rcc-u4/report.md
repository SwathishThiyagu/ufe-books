# ce-rcc-u4: free-model run

- Book: `books/civil/ce-rcc/ce-rcc-u4.html`
- Status: ok
- Model calls so far: 35 (135,380 tokens in, 333,945 out), 12.4 minutes

## Checker

```
ce-rcc-u4.html: 6 chapters, 11011 words, 7 figures, 116 KB
OK
```

## For the reviewer

- chapter 2: the figure cannot be drawn: tree is too wide (9 leaves); use fewer leaves or shorter labels
- chapter 2: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [high] Section 1, last line: The sentence breaks off: 'If ly/lx 4.2.' It has no verb, no inequality sign and no chapter link, so a student cannot tell what condition or chapter is meant.
- ch 1 [high] Section 3, crack control: The cover values are wrong for moderate exposure. IS 456 Table 16 gives nominal cover 20 mm for mild exposure and 30 mm for moderate exposure. The 5 mm relaxation to 15 mm is allowed only for mild exposure when the main bar is 12 mm or smaller; it is not allowed for moderate exposure, so '20 mm for moderate' under-specifies cover by 10 mm.
- ch 1 [low] Worked example 1, step 3: The effective span is fixed at 3.0 m, but the rule given in Section 2 (clear span plus effective depth, or c/c of supports, whichever is less) gives 3.0 + 0.095 = 3.095 m, and c/c of supports is 3.23 m. Using 3.0 m is safe but contradicts the stated rule and may confuse a student writing the exam.
- ch 1 [low] Section 3, shear check: The check τv ≤ τc is conservative but omits the IS 456 provision that for solid slabs less than 300 mm thick the design shear strength is k·τc, where k depends on overall depth (1.30 for 150 mm or less, falling to 1.00 at 300 mm). Students who meet this in another text will think the chapter is incomplete.
- ch 2 [high] Section 2, the paragraph beginning 'Read the row by edge condition', and the figure tree: The list of the nine edge conditions is not the nine cases of IS 456 Table 26. Two entries are the same case under two names: 'one short edge continuous' is the same panel as 'three edges discontinuous with one short edge continuous', and 'one long edge continuous' is the same panel as 'three edges discontinuous with one long edge continuous'. Because of this double counting, the genuinely distinct cases 'one short edge discontinuous' and 'one long edge discontinuous' are missing. The figure repeats the same duplicated nine nodes.
- ch 2 [low] Section 2, Table 26 extract: The rows are out of order: 1.20, then 1.30, then the interpolated 1.25. A student reads the table top to bottom and expects increasing ly/lx, so the last row looks like a misprint. The table also does not name the edge case in its own header; the case is only stated in the sentence below it.
- ch 2 [low] Section 3, torsion steel paragraph, and worked example step 9: Only the full torsion steel for a corner where both edges are discontinuous is given. IS 456 also requires torsion reinforcement of half that amount at a corner bounded by edges over only one of which the slab is continuous. The worked example panel has two such corners, and the chapter never mentions them.
- ch 2 [low] Section 3 checks line and worked example step 10: 'Vu = w lx/2 at the long edge' is used without saying it is conservative. The short-direction strip actually carries only wx ≈ 0.71w of the load (Section 1), so the real shear per metre at the long edge is about wx lx/2 = 18.1 kN/m, not 25.5 kN/m. A student may take w lx/2 as the true shear.
- ch 3 [high] Section 1, shear bullet, and worked example 1, step 9: The text says the shear check is made at a distance d from the face, but gives V = wu l, which is the shear at the face itself. Step 9 then computes V = 11.625 × 1.5 = 17.44 kN/m, the face value, while claiming it is the section at d. The two statements contradict each other and the number belongs to the wrong section.
- ch 3 [low] Section 1, bullet on the span: The instruction 'take l from the face of the support to the free edge, never to the centre of the beam' is right about where the moment is critical, but it omits the code definition of the effective span of a cantilever, which adds half the effective depth to the clear projection. A student reading only this bullet will not know that provision exists.
- ch 3 [low] Section 2, list of conditions for using the coefficients: 'The members must not be carrying a load that the coefficients do not cover' is too vague to act on. A student cannot tell which loads the coefficients exclude.
- ch 4 [high] Worked example 1, step 7: The value quoted as k τc is wrong. For pt ≈ 0.40% and M25, IS 456 Table 19 gives τc ≈ 0.44 N/mm², and that is the value shown. The factor k for a solid slab of overall depth 150 mm is 1.30, so the permissible stress is k τc ≈ 1.30 × 0.44 = 0.57 N/mm². The example labels τc itself as k τc and quietly drops the k factor.
- ch 4 [low] Exam traps, second bullet (and quiz Q5): The sloping length of the 3.3 m flight is given as 3.6 m, which does not follow from the slope factor used everywhere else: 3.3 × 1.118 = 3.69 m. A student who multiplies will get a different number from the one in the text.
- ch 5 [low] Lead: "This saves headroom" is ambiguous and reads backwards: a beamless soffit does not save headroom, it adds clear height under the slab (or reduces floor-to-floor height). The body of Section 1 says the opposite idea correctly, so the lead contradicts it.
- ch 5 [low] Section 2, moment split: The 65 percent negative / 35 percent positive split is stated for any panel. These are the interior-panel proportions; end panels have different proportions, so a student may apply 65/35 to an end panel.
- ch 5 [low] Section 2, opening: The direct design method is presented as valid for any "regular panel of equal spans". The method has conditions: at least three continuous spans in each direction, longer span to shorter span ratio not more than 2, adjacent span lengths not differing too much, and the clear span lₙ not less than about 0.65 of the centre-to-centre span. Without these, a student will use the method on layouts where it is not allowed.
- ch 5 [low] Section 1, punching shear perimeter: The critical perimeter is said to lie at half the effective depth from the column face. That is right for a slab without a drop or capital; when a drop or capital is provided, the perimeter is measured from its edge, not from the column face. Since the same section recommends capitals and drops, the statement is incomplete.
- ch 5 [low] Quiz Q4: The answer gives an unrelated reason: carrying shear near the column is not why the code sends 75 percent of the negative moment to the column strip. The correct reason is the greater stiffness of the band along the column line, which attracts the hogging moment (and this band must deliver that moment to the column).
- ch 6 [high] Section 3 (upper bound and admissible patterns): The chapter says a wrong pattern 'overestimates strength, so it is safe but possibly uneconomical'. This reverses the meaning of an upper bound. Any admissible pattern gives a load at or above the true collapse load, so a pattern that is not the lowest overestimates the slab's strength and the design is unsafe (unconservative), not safe.
- ch 6 [high] Exam traps, trap 1: Wrong arithmetic. Using θ = 2δ/L instead of θ = 2√2 δ/L reduces the internal work by a factor of 1/√2 ≈ 0.707, not by half; so wu comes out as 0.707 wu, not wu/2.
- ch 6 [high] Quiz Q5: The question and answer are inconsistent with the mechanics. With θ = 2δ/L the student gets 1/√2 ≈ 0.71 times the correct wu (0.707 × 25.86 = 18.3 kN/m²), not half (12.9 kN/m²).
- ch 6 [low] Section 3 (free edge sentence): 'For a slab with a free edge, include a line parallel to that edge' reads as a general rule and is misleading. A line along the free edge carries no moment and is not a yield line; a yield line parallel to the free edge is the normal mechanism only in a cantilever slab. In a slab supported on three edges with a free fourth edge, the yield lines run from the free edge to the supported edges.
- ch 6 [low] Worked example 1, step 3: xu,max is used without being defined, and the ratio 0.48 is not identified as the Fe415 value.
