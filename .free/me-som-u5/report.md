# me-som-u5: free-model run

- Book: `books/mech/me-som/me-som-u5.html`
- Status: ok
- Model calls so far: 30 (108,720 tokens in, 248,687 out), 8.6 minutes

## Checker

```
me-som-u5.html: 8 chapters, 14440 words, 9 figures, 146 KB
OK
```

## For the reviewer

- chapter 8: the figure cannot be drawn: tree label "Indeterminate beam" is too long; shorten it

## Reviewer notes (after any revision)

- ch 1 [high] Section 3, cantilever paragraph: The claim that at the free end V = 0, so y‴ = 0, is false for the very cantilever described. With M(x) = −P(L − x), the shear is dM/dx = P at every section, including the free end x = L, so y‴ = P/EI there, not zero. Only M = 0 holds at that free end.
- ch 1 [low] Section 2, table, Free end row: The row 'Free end | M = 0 so y″ = 0; V = 0 so y‴ = 0' is stated without a condition and contradicts the cantilever with a tip point load discussed later in the chapter.
- ch 1 [low] Exam traps, second bullet: The sentence 'Calling curvature 1/R the radius of curvature' is muddled and a student may read it as saying curvature is not 1/R.
- ch 1 [low] Quiz Q7: A cantilever fixed at x = 0 with M(x) = −10x kN·m has zero moment at the fixed end, which no loaded cantilever can have (the fixed-end moment there must balance the loads). The data describe no real beam, which can distract a careful student.
- ch 2 [low] Figure: The caption gives span 6 m, load 4 kN/m and midspan deflection 11.25 mm, but the value 11.25 mm only follows if EI = 6000 kN·m², which the caption never states. The plotted expression on the figure uses EI = 6000, so a student cannot reproduce the curve from the caption alone.
- ch 2 [low] Section 3, table of standard cases: The row 'Simply supported, central P | Px/2; P(L − x)/2' does not say which expression belongs to which part of the span. A student can plug Px/2 past midspan and get a wrong moment, which is exactly the trap this chapter warns about.
- ch 2 [low] Section 2, support conditions table: The table is headed 'End | Conditions', but its third row ('Matching at a load point') is a continuity condition at an interior point, not an end condition. The heading misdescribes the row.
- ch 2 [low] Section 3, central point load paragraph: The text says 'Match y and y′ at midspan, or use symmetry y′ = 0 at midspan' without saying that these are alternatives for a two-region problem with four constants. A student may think one condition, y′ = 0 at midspan, replaces both matching equations in a two-region solution.
- ch 3 [low] Section 2, table row for applied moment: The table gives the term as +M₀⟨x − a⟩⁰ but never states the sense of the couple. The note says only that the signs suit 'sagging positive with downward loads', and a couple has no downward direction, so a student cannot tell whether +M₀ means clockwise or anticlockwise.
- ch 3 [low] Section 2, last bullet: 'Loads left of the origin never need a bracket' is confusing and reads like a rule about a region where no load can exist. The useful point is that a load placed at x = 0 needs no bracket, because ⟨x − 0⟩ⁿ is just xⁿ.
- ch 3 [low] Section 3, boundary-condition bullet: 'x = L gives C₁' is too short. Substituting x = L gives a linear equation in C₁ that also contains the known constant terms (and C₂ if it is not zero); C₁ is then solved for, not read off.
- ch 3 [low] Exam trap 3: The consequence is described wrongly. The reactions were already found from the true loading, so they still balance; what goes wrong is the moment expression, which then does not vanish at the far end and gives inconsistent slopes and deflections.
- ch 3 [low] Section 3 (missing condition): The chapter never states that EI must be constant along the whole span. One integration of a single M(x) assumes the same EI everywhere, and a student with a stepped shaft or a beam with a changed section will use the method wrongly.
- ch 4 [high] Quiz Q6: The question asks for the moment of the triangular M/EI area about the apex (zero-ordinate) end, but the answer takes the moment about the taller end and uses a lever arm of 2L/3. For a triangle of height h at one end, the centroid is L/3 from the taller end and 2L/3 from the apex end. So the moment about the taller end is ½Lh × L/3 = L²h/6, not ½Lh × 2L/3. The answer pairs the wrong end with the wrong lever arm and so gives twice the correct value.
- ch 4 [low] Section 2, second paragraph: "a turn dθ at a distance x from B lifts or drops B by x dθ relative to the tangent there" — "the tangent there" is ambiguous; it can be read as the tangent at B rather than the tangent at the slice.
- ch 4 [low] Section 1, sign rule: The bracket "(concave up in the usual plotting)" does not say what is plotted or which way, so the sign rule stays murky for a reader meeting curvature for the first time.
- ch 5 [low] Section 1, sign convention sentences: The stated pair 'sagging M positive, downward y positive' does not sit with the relation d²y/dx² = M/EI that the chapter compares against: with y measured downward and sagging M positive, the elastic-curve relation carries a minus sign. Saying only 'apply the M/EI load in the direction that keeps the signs consistent' leaves a student unable to decide which way to point q*, and a wrong load direction flips the sign of both θ and y.
- ch 5 [low] Section 2, last paragraph: 'The method is for determinate beams' is too strong and contradicts the sentence that follows it. Standard texts apply the conjugate beam to any beam once M is known; for an indeterminate beam the conjugate beam is simply loaded with the true M/EI diagram (for a fixed-fixed beam the conjugate beam is free at both ends and the M/EI load is self-equilibrating).
- ch 5 [low] Beyond: 'It also helps in beam-column problems where the M/EI load includes axial effects' is not a standard use. A beam-column obeys EI y'' = M − P y, so the M/EI load alone no longer gives the deflection; a plain conjugate beam loaded with M/EI does not solve it.
- ch 5 [low] Worked example step 5 and quiz Q5: The total conjugate load is written as a bare number: 'Total conjugate load = area = ½ × 6 × 0.0036 = 0.0108'. Every other quantity in the example carries a unit, and the reader cannot tell whether 0.0108 is a force or a rotation.
- ch 6 [high] Section 2, overhanging beam bullet: The bullet says to 'treat the span between supports and the overhang separately, then add the deflection at the chosen point'. Superposition splits loads, not the geometry of one continuous beam. The overhang is carried by the rotation of the support, which comes from the loading on the main span. Adding a separately computed main-span deflection to a separately computed cantilever deflection gives a wrong answer.
- ch 6 [high] Section 2, last sentence (and Exam traps): It states superposition is invalid if EI changes along the span. For a linear elastic beam the governing equation EI(x)·d²y/dx² = M(x) is still linear in the loads when EI varies with x, so superposition remains valid. What fails with a stepped or tapered beam is only the constant-EI standard formulas for the whole span, not the principle.
- ch 6 [high] Quiz Q7: The answer gives 'nonlinear EI variation along the span' as a situation where superposition is unsafe. This repeats the error above: a varying EI does not break superposition for a linear elastic beam, so the answer is wrong.
- ch 6 [low] Section 2 sign convention vs Worked example 1, step 4: Section 2 says downward deflections are negative and upward positive, but step 4 adds two downward deflections as 9 + 11.25 = +20.25 mm downward, which contradicts that convention and will confuse a student applying signs.
- ch 7 [high] Exam traps, second trap: The effect of the error is stated backwards. The correct energy is ∫M²/(2EI)dx. A student who writes M²/(EI) gets an energy twice as large, so ∂U/∂P and hence every deflection comes out doubled, not halved.
- ch 7 [low] Section 1, last paragraph: Squaring the moment diagram and integrating gives the strain energy, not the deflection. The sentence skips the differentiation step, which is the whole point of the chapter and of the exam trap.
- ch 7 [low] Section 3, last paragraph before the summary list: The symmetry of the flexibility matrix is a consequence of Maxwell/Betti, but it is not what 'makes' the unit-load equations solvable with one unknown; the single unknown comes from the single degree of indeterminacy of a propped cantilever.
- ch 7 [low] Beyond: 'a volume integral of stress times strain' omits the factor 1/2 in the strain-energy density.
- ch 8 [high] Section 3, first sentence: "A fixed beam has both ends rotation-free" is backwards. A fixed end has zero rotation; rotation-free ends describe a simply supported (or free) end. A student reading this will get the whole point of a fixed beam wrong.
- ch 8 [high] Section 3, three-moment equation formula block: The settlement term has the wrong sign for the convention the chapter declares (sagging moments positive, downward settlements positive). As written it predicts sagging over a support that settles, which is physically wrong. Check: two equal spans L, A and C level, B settling by δ downward, no loads. Correct working gives 2MB(2L) = −6EI(δ/L + δ/L), so MB = −3EIδ/L², hogging, which matches a slope-deflection solution. The printed +6EI form gives MB = +3EIδ/L², sagging.
- ch 8 [high] Quiz Q5: The answer concludes the moment is sagging and positive. With sagging positive and B settling downward between level supports, the moment at B is hogging (negative); the magnitude quoted is right, the sign and the word "sagging" are wrong.
- ch 8 [high] Section 2, settlement sentence: The compatibility equation is written with the deflection signs swapped. The load pushes B down by wL⁴/(8EI); the prop pushes it up by RBL³/(3EI). The net downward movement at B must equal the settlement δ, so the equation as printed (net upward = δ) is wrong and gives the wrong RB when B settles.
- ch 8 [low] Section 3, three-moment "where" list: A1 and A2 are only called "areas of the free bending-moment diagrams"; which span each belongs to is not stated, and the centroid directions (x1 from A, x2 from C) then look arbitrary.
