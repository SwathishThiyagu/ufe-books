# me-fluid-u5: free-model run

- Book: `books/mech/me-fluid/me-fluid-u5.html`
- Status: ok
- Model calls so far: 39 (160,268 tokens in, 334,833 out), 7.6 minutes

## Checker

```
me-fluid-u5.html: 8 chapters, 15060 words, 9 figures, 154 KB
OK
```

## For the reviewer

- chapter 5: the figure cannot be drawn: tree label "Fundamental dimensions" is too long; shorten it
- chapter 8: the figure cannot be drawn: note "compressible" runs off the right edge; shorten it
- chapter 8: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [high] Section 2 and figure: The text says δ 'jumps' at transition to roughly 0.38x/Re_x^{1/5}, and the figure plots that turbulent correlation from x = 0. That correlation is for a layer turbulent from the leading edge (or needs a virtual origin); in a real flat plate δ is continuous through transition and is not 0.38x/Re_x^{1/5} at x_c.
- ch 1 [low] Exam traps: The statement 'changes the answer by a factor of ρ' is ambiguous: substituting μ for ν changes Re_x by a factor ρ, but changes δ by a factor √ρ.
- ch 1 [low] Quiz Q6: The answer uses the laminar scaling δ ∝ √(νx/U), but the question does not state that both layers remain laminar; at 4U the layer may already be turbulent at the same x.
- ch 2 [high] Section 1 (shape factor paragraph): The sentence 'A full, slow profile has a large mass deficit compared with its momentum deficit, so H is high' contradicts the next sentence and the standard textbooks. In boundary-layer language a 'full' profile (velocity rising quickly near the wall) is the one with LOW H; H is high only when the profile is thin/less full near the wall (laminar). As written, a student reads that full means high H, then two lines later reads that fuller means lower H.
- ch 2 [low] Exam traps, second trap: 'Using the displacement integrand gives a wrong value, often about twice too large' is only safe for the linear profile (0.5δ against 0.25δ, exactly twice). For the 1/7 power law the displacement integrand gives 0.125δ, which is SMALLER than the true δE = 0.175δ, so the 'twice too large' claim is misleading.
- ch 3 [high] Lead, sentence 4: "a very thin laminar sublayer ... carries almost all the velocity drop from zero to the free stream" is wrong. With the chapter's own numbers (u* = 0.67 m/s, U = 15 m/s), the velocity at the top of the viscous sublayer (y+ ≈ 5) is u ≈ 5u* ≈ 3.4 m/s, about 22 % of U; even at y+ ≈ 12 it is about 8 m/s, roughly half of U. Most of the velocity rise to U happens in the outer turbulent part, not in the sublayer.
- ch 3 [high] Section 2, definition of the sublayer vs the formula δs ≈ 11.6ν/u*: The chapter defines the viscous sublayer as y+ below about 5, but the formula δs ≈ 11.6ν/u* gives the height where y+ = 11.6 — the top of the buffer layer, not y+ = 5. A student who checks y+ = δs u*/ν gets 11.6 and concludes the two statements contradict each other. With y+ = 5 the sublayer here would be 0.11 mm, not 0.26 mm.
- ch 3 [low] Section 1, paragraph 5: The values 7.1 mm and 41 mm come from x = 2 m and ν = 1.5×10⁻⁵ m²/s, but neither x nor ν is given here, so the numbers cannot be reproduced from the formulas shown.
- ch 3 [low] Worked example steps 3, 5, 7; quiz Q1, Q3, Q5: Exponents lost their markup and will render as plain digits: "Rex1/5", "0.072/ReL1/5", "2−0.2 = 0.871", "(2.0×10⁶)1/5". On a phone this reads as Rex times 1/5 and is easy to misread.
- ch 3 [low] Quiz Q7 answer: "roughly 5 + < 30" is garbled and does not say what range it is. The answer also mentions "the log law", which the chapter never introduces (it only says "universal velocity profile").
- ch 3 [low] Worked example step 5 and Section 2 formula u* = U√(Cf/2): Cf = 0.072/Re<sup>1/5</sup> is the mean skin friction coefficient for the whole plate, while u* = U√(Cf/2) needs the local Cf at the station where the sublayer is being found. Using the mean value at the trailing edge overstates the local wall shear (local c<sub>f</sub> ≈ 0.0576/Re<sub>x</sub><sup>1/5</sup> = 0.00316, giving u* ≈ 0.60 m/s and δs ≈ 0.29 mm).
- ch 4 [high] Section 1, first paragraph: The sentence is broken: "the flow speeds up and pressure falls: dp/dx  0, an adverse pressure gradient." The inequality sign is missing, and the words left over say the opposite of the correct physics — falling pressure along the front is a favourable gradient, not an adverse one. A student cannot tell which sign belongs to which region.
- ch 4 [low] Worked example 1, step 3, and quiz Q4: The exponent is typed inline, not raised: "0.072 / (1.33×10⁶)1/5" and "0.072/(1.2×10⁶)1/5". Read literally this means multiplying by 1/5, which gives a wildly wrong Cf. The numbers quoted afterwards (16.8 and 16.44) are correct, so only the notation is wrong.
- ch 4 [low] Worked example 1, step 5 and answer: The claim that a real plate "gives between the two, near 1.03 N" overstates the turbulent figure. For this plate transition is at x = 5×10⁵ ν/U ≈ 0.75 m, so about 1.25 m of the 2 m is turbulent. A mixed boundary-layer estimate, Cf = 0.074/ReL<sup>1/5</sup> − 1742/ReL = 0.00441 − 0.00131 = 0.00310, gives D ≈ 0.00310 × 60 × 4.0 ≈ 0.74 N — roughly a quarter below 1.03 N, not "near" it.
- ch 4 [low] Beyond box, last sentences: The Tacoma Narrows collapse is attributed to vortex shedding. Standard accounts put that failure down to aeroelastic torsional flutter, with shedding at most a trigger for the early motion. A student carries away a wrong cause.
- ch 5 [low] Figure (tree): The tree attaches force as a child of M alone, velocity under L alone and acceleration under T alone. Force needs M, L and T together, and velocity and acceleration each need both L and T, so the picture suggests a derived quantity comes from one base dimension, which contradicts the caption and the rest of the chapter.
- ch 5 [low] Section 3, third use (convert between unit systems): The stated method is 'replace each unit by its dimension and cancel; the numerical factor follows from the unit sizes', but the example then just quotes the remembered fact 1 poise = 0.1 Pa·s. A student cannot see the method working, and dimensions alone cancel to 1 and give no numerical factor.
- ch 5 [low] Section 1, last sentence: The sentence 'a bare 9.81 can be m/s² or N/kg' does not show a real ambiguity, because m/s² and N/kg are the same dimension and the same size. The exam trap later in the chapter says exactly this.
- ch 6 [high] Worked example 1, step 7 and answer: The conversion from φ to the standard drag coefficient is wrong by a factor. With A = πD²/4, the denominator ½ρV²A equals ρV²πD²/8, so C_D = F/(½ρV²A) = 8φ/π, not (π/2)φ. The stated (π/2)φ ≈ 1.57φ understates it; the correct factor is 8/π ≈ 2.55.
- ch 6 [high] Section 1, method bullets (fourth bullet): "a dimensionless constant forces every exponent to sum to zero" is wrong and will mislead. Nothing sums to zero: the constant C simply contributes no M, L or T, so it drops out of the exponent equations. What you actually do is equate the M, L and T exponents of the two sides.
- ch 6 [low] Lead: "Two variables that are physically linked can be tested for a link using dimensions alone" is loose: dimensional analysis cannot discover or test whether a link exists. The variable list is a physical judgement supplied by the engineer; dimensions only fix the form of the relation.
- ch 6 [low] Section 3, first paragraph: F/(ρV²D²) is called "a drag coefficient", but step 7 of the worked example shows the usual drag coefficient is F/(½ρV²A), which differs by the factor 8/π. A student may take the two as the same quantity.
- ch 7 [high] worked example 1, step 5: The unit check for Weber number is wrong. ρV²D gives kg/m³ × m²/s² × m = kg/s² = N/m, not kg/(m·s²) = Pa. Pa is the unit of ρV² alone (before multiplying by D). As written, a student checking units would find the ratio is not dimensionless.
- ch 7 [high] Exam traps, third trap: The factor is inverted. If a book uses Eu = Δp/(ρV²), then Eu = Δp/(2 × ½ρV²), so its value is half the value obtained with the definition used in this chapter, not twice it.
- ch 7 [high] Section 2, Froude number paragraph: The inequality sign is missing: 'Fr  1 is supercritical' has no comparison, so the student cannot tell whether the limit is above or below 1.
- ch 7 [low] Quiz Q8: The subscripts m and p are never defined, and 'force a fixed length scale and fluid' is vague — the actual result is that, with the same fluid, both groups can be matched only at full scale (length ratio 1).
- ch 7 [low] Table 5.7.1 and lead: Froude and Mach are the square roots of force ratios (Fr² = inertia ÷ gravity, Ma² = inertia ÷ elastic force), not direct force ratios, while the table lists all five as simple ratios of two forces.
- ch 8 [high] Exam traps, fourth bullet (distorted model): The formula Q_r = L_hr × L_vr^(3/2) is right, but the reason given — 'because the plan area uses the horizontal scale' — is wrong. Discharge is (flow cross-section area) × velocity. The cross-section is width × depth: width scales with the horizontal ratio L_hr, depth scales with the vertical ratio L_vr, and velocity with √L_vr. Plan area would be L_hr², which gives a different (wrong) answer and leaves the student unable to derive the formula.
- ch 8 [high] Quiz Q5 answer: Same error: 'The discharge ratio uses the plan area, which comes from the horizontal scale, so Q_r = L_hr × L_vr^(3/2)'. Plan area comes from the horizontal scale twice (L_hr²); the factor L_vr enters through the depth of the flow section. A student copying this reasoning into an exam answer gives a wrong justification.
- ch 8 [low] Section 2 formulas and worked example, symbol use: F_r is defined as the force ratio while Fr is the Froude number, and the table writes 'Froude (Fr)'. Two symbols that differ only by a subscript carry different meanings, which is easy to misread on a phone screen and easy to mix up when writing by hand.
- ch 8 [low] Section 3, first sentence of the paragraph on distortion: 'River and harbour models are always distorted' is too absolute; undistorted river models are built for local, small-reach studies where the depth stays workable.
