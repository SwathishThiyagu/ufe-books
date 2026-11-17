# me-som-u1: free-model run

- Book: `books/mech/me-som/me-som-u1.html`
- Status: ok
- Model calls so far: 33 (122,799 tokens in, 265,583 out), 5.7 minutes

## Checker

```
me-som-u1.html: 9 chapters, 15638 words, 10 figures, 161 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 3, the paragraph 'Judge the size': The sentence 'Aluminium alloys are weaker; the same 159 MPa would be close to failure' is wrong as a general statement. Many wrought structural aluminium alloys (for example the 2xxx, 6xxx and 7xxx families) have yield strengths of 200 MPa or more, comparable to or above mild steel, so 159 MPa is not near failure in them. Only some cast and pure grades are that weak. A student can carry away the false rule 'aluminium fails around 160 MPa'.
- ch 1 [low] Section 2, the paragraph beginning 'V/A_s gives an average': 'Zero at its edges and peaks in the middle' is loose for a solid circular section. The shear stress is zero at the top and bottom points of the section (the ends of the diameter perpendicular to the load), not at every edge; the peak is at the centre and is 4/3 of the average, not just 'higher'.
- ch 1 [low] Section 3, exam trap 5: '159.2 kN/anything is wrong on the unit alone' reads awkwardly and the logic is inverted: a force divided by an area is a stress, so the error is writing a force where a stress is asked, not the division itself.
- ch 2 [high] Exam traps, item 4: The trap states the opposite of the truth: it says the 0.2% offset does not start at 0.2 on a percentage axis. On a percentage-strain axis, 0.2% strain is exactly the number 0.2, so the offset line must be started at 0.2 there, and at 0.002 only on a strain axis. As written, a student is taught to start at the wrong point on a percentage axis.
- ch 2 [high] Figure (MS series): The mild-steel curve runs from [18, 400] straight down to [24, 0], so the plotted breaking stress is 0 MPa. The text says the breaking stress is only slightly lower than the UTS, and no material fractures at zero engineering stress. A student reading the figure will conclude that the breaking stress is zero.
- ch 2 [high] Figure (MS series) and Section 2: The initial straight part goes from [0, 0] to [0.2%, 229 MPa]. Its slope is 229/0.002 = 114 500 MPa ≈ 115 GPa, about half the 200 GPa that steel actually has, and the text tells the student that this slope is Young's modulus. Anyone reading E off the figure gets a wrong number.
- ch 2 [low] Figure (CI series) against Section 3: The text says brittle cast iron shows under 1% elongation, but the CI curve breaks at 1.2% strain. The two statements disagree.
- ch 2 [low] Section 2, yield bullet: The lower yield point is the minimum stress at the bottom of the drop, not the flat part. The flat part is the yield plateau (Lüders band spreading along the gauge length).
- ch 3 [low] Section 1 (Hooke's law for tension and shear): The text says the law holds up to the elastic limit. Strictly, proportionality ends at the proportional limit, which lies at or below the elastic limit; between the proportional limit and the elastic limit the curve bends but unloading is still elastic. The same loose statement is repeated in the lead and in quiz Q1.
- ch 3 [low] Section 3, bullet on cost of failure: "IRCTC bridge" is a wrong name. IRCTC is the railway catering and tourism corporation; it does not build bridges, so the example misleads a reader.
- ch 3 [low] Section 3, bullet on loads being larger than estimated: "A Chennai power cut that starts a pump against a closed valve" is physically confused. A power cut stops a pump; the surge comes when supply returns and the pump restarts against a closed valve.
- ch 3 [low] Exam traps, fourth bullet: "Do not replace σ by P/(nA) and call it safe" does not say what P/(nA) is being compared with. Comparing P/(nA) with the working stress is conservative; the real error is comparing it with the failure stress (equivalently, P/n with σf A). A student can misread the trap.
- ch 4 [high] Exam traps, third bullet: The unit comparison is wrong: 200 GPa is 200 000 MPa, not 80 000 MPa. As written the sentence pairs two different stiffnesses while claiming they are the same.
- ch 4 [low] Exam traps, second bullet: The claim that the wrong-sign form E/[3(1 + 2ν)] 'can even give a negative K for larger ν' is false: 1 + 2ν stays positive, so that form never gives a negative K. Negative K only appears in the correct form when ν > 0.5.
- ch 4 [low] Section 3, first relation: 'All three moduli in the same unit' is loose: E = 2G(1 + ν) contains two moduli (E and G) and one dimensionless ratio.
- ch 4 [low] Section 1, bullet on the range of ν: Saying 0 ≤ ν ≤ 0.5 with 'a value outside this range means an error' clashes with the 'Beyond' paragraph, which describes auxetic materials with negative ν.
- ch 4 [low] Section 1, bullet on cork: The cork example is attached to the wrong effect. Cork grips the neck because it is squeezed radially and springs back, not because ν is near zero. The point of ν ≈ 0 is that cork does not bulge sideways when compressed along its length, so it can be driven in without jamming.
- ch 5 [high] Beyond: The sign of the effect is reversed. A negative Poisson's ratio means the material widens sideways when stretched, not that it shrinks sideways. Shrinking sideways is what an ordinary positive-ν material does.
- ch 5 [high] Section 3: The reason given for using oil instead of water in hydraulic presses is wrong. Oil is chosen for lubrication, corrosion protection and viscosity, not because water is too compressible; the bulk moduli of oil and water are of the same order (about 1.5 to 2.2 GPa), so compressibility does not decide the choice.
- ch 5 [low] Exam traps, third item: The second half is not a trap. For a nearly incompressible material, K = E/[3(1 − 2ν)] genuinely becomes very large; that is the correct answer, not a mistake.
- ch 5 [low] Quiz Q8: The answer justifies the result with ε_v = (σ/E)(1 − 2ν) = 0 "even for large axial strain", but Section 1 states that the linear sum of strains fails once a rubber part doubles in length. The conclusion is right; the justification contradicts the earlier warning.
- ch 6 [low] Worked example 1, steps 3 and 5: The division is written without brackets: "δ1 = 16 000 / 60 × 10⁶" and "δ2 = 24 000 / 40 × 10⁶". Read left to right (standard precedence) these give 2.67 × 10⁸ and 6.0 × 10⁸, not the stated 0.0002667 m and 0.0006000 m. A student copying the step exactly will land on a wrong number and not know why.
- ch 7 [high] Section 2, method steps (remove one support and compute the free displacement): The step says to compute the displacement at the cut from δ=FL/(AE). In the worked example the load P is at C, not at the cut B. After removing support B, segment CB carries no internal force, so the free displacement at B is only the elongation of AC: δ_P = P a/(AE) = 30,000×0.5/(6×10⁷) = 2.5×10⁻⁴ m. Using the full length L=1.5 m gives δ_P = 7.5×10⁻⁴ m and then R_B = 30 kN, R_A = 0, which is wrong. The method must tell students to sum the elongations of the segments between the fixed end and the cut.
- ch 7 [low] Section 2, method steps (compatibility equation): The text says δ_R is the displacement caused by the redundant reaction 'opposite in sense' to δ_P, then writes δ_P + δ_R = 0. If δ_R is read as a positive magnitude, the equation should be δ_P − δ_R = 0. A student can add magnitudes and get a sign error.
- ch 7 [low] Quiz Q7: The answer says subtracting 'sets equal magnitudes with the same sign', but subtracting a negative δ_CB adds its magnitude. The question is also ambiguous: if δ_CB is taken as a positive compression magnitude, δ_AC − δ_CB = 0 is the correct compatibility equation. The stated error follows only when δ_CB is a signed elongation (negative in compression).
- ch 7 [low] Section 3 and Quiz Q4: The parallel-rod argument assumes both rods have the same elongation. That holds only if the rigid block stays horizontal, for example because it is guided or the load is applied symmetrically. A freely hanging rigid block can tilt, and then the rod elongations are not equal.
- ch 7 [low] Section 2, method steps: 'Redundant reaction' is used without definition. A student may not know it means the extra unknown reaction removed to make the structure determinate.
- ch 8 [high] Quiz Q5: The stated compatibility condition is wrong for the situation described. A composite bar held between two rigid supports has zero total length change, so each material's total strain is zero. Writing α_sΔT+σ_s/E_s = α_bΔT+σ_b/E_b only says the two total strains are equal; it allows the assembly to change length, which rigid supports forbid. The equilibrium equation σ_sA_s+σ_bA_b=0 also fails here: the rigid supports supply a reaction, so the sum of internal forces need not be zero.
- ch 8 [low] Section 3: The composite-bar procedure gives only the free-at-one-end case. With both ends on rigid supports, 'equal total strains' is not the condition; zero total strain is. A student may apply Σσ_iA_i=P_ext with P_ext=0 to a rigidly held composite bar and get the wrong answer.
- ch 9 [low] Section 1: The definition 'Strain energy U is the elastic energy stored in a member when it deforms' has no elastic-limit restriction, yet every formula in the section (u = σ²/2E, U = P²L/2AE) is valid only while the material obeys Hooke's law. A student can carry these formulas past yield, which the traps later warn against but the definition does not.
- ch 9 [low] Section 1: 'Some syllabi call strain energy resilience' is loose. Textbooks define resilience as the strain energy stored up to the elastic limit, and proof resilience as the maximum such value at the limit; saying strain energy = resilience blurs the distinction made in the very next sentence.
- ch 9 [low] Section 2: The step 'P_max = 2W' silently assumes the weight is set on the member from rest, with zero initial velocity, at the undeformed position. A student who applies the same 2W/A result to a load arriving with any velocity gets an unsafe stress.
- ch 9 [low] worked example 1, step 2: The label 'Static stress' is not defined in the example; a reader may read it as the stress at the final static equilibrium of the suddenly applied weight rather than the stress for the same weight applied gradually.
