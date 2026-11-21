# ae-struct-u2: free-model run

- Book: `work/ae-struct-u2/tree/books/aero/ae-struct/ae-struct-u2.html`
- Status: ok
- Model calls so far: 31 (120,325 tokens in, 277,778 out), 6.8 minutes

## Checker

```
ae-struct-u2.html: 8 chapters, 19870 words, 10 figures, 217 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 1: The sentence 'A load dropped on suddenly does twice this work' is wrong. A suddenly applied constant load of the same final magnitude produces twice the deflection and twice the stress, but the work done by the load and the maximum strain energy stored are four times the gradually applied values (work = P × 2Δ = 4 × ½PΔ). 'Dropped on' also suggests impact, which is a different case again.
- ch 1 [low] Section 3, resilience paragraph: 'Resilience is the same quantity per unit volume' contradicts the next two sentences, which treat resilience/proof resilience as a total energy in joules and give the per-volume value separately as the modulus of resilience. A student will not know which term means what.
- ch 1 [low] Section 3, simply supported beam derivation: The cantilever step says x is measured from the free end, but the simply supported step writes M = Px/2 without saying where x starts, so the reader cannot reproduce the integration limits.
- ch 1 [low] Worked example, step 6: The sense check compares 16 with 20 and says 'both energies scale as P²', but the ratio of the two energies is fixed by the two members' stiffnesses, not by the load ratio. The sentence does not check anything and can mislead a student into thinking 16 ≈ 20 confirms the answer.
- ch 1 [low] Quiz Q6: 'Twice the depth' gives I ∝ depth³ only if the breadth is unchanged; the answer assumes a rectangular section of the same width without saying so.
- ch 2 [high] Quiz Q6: The stated answer contradicts the chapter's own linear-elastic single-load result. For one applied load, U = ½PΔ, so if two members carry the same P and store the same U, then Δ = 2U/P is also the same. The reasoning 'equal energy at one load does not fix the slope' is false when U ∝ P²: one point on the curve fixes the constant, hence the slope.
- ch 2 [low] Section 2 and exam trap 2 (reactions): Calling differentiation with respect to a support reaction simply an error is misleading. ∂U/∂R gives the displacement of that support in the direction of R, which is zero on a rigid support — this zero is exactly the compatibility equation used to find a redundant reaction (least-work / Menabrea theorem). The sentence 'A reaction is not a load' is also loose: a reaction is a force applied to the structure by its support, and the theorem applies to it.
- ch 2 [low] Lead: The claim 'Only a few universities teach this topic' is doubtful: Castigliano's theorem is a standard part of energy-method syllabi in structural analysis and aircraft structures in India. A student reading it may skip a topic that is likely to be examined.
- ch 2 [low] Worked example 1 and 2, output lines: The output lines show bare numbers (0.8333 / 1.6667 and 25.0 / 1.0) with no units, and the second number in each pair is in millimetres while the derivative ∂U/∂P was computed in metres. A student can read 1.6667 as metres.
- ch 3 [high] Section 2, calculation table header: The last column is labelled nNL/A (N·m). With n dimensionless (a ratio from a 1 kN unit load), N in newtons, L in metres and A in m², the product nNL/A has units N·m/m² = N/m, not N·m. Dividing by E (N/m²) must then give metres, which only works with N/m.
- ch 3 [low] Lead: "Virtual work finds a deflection without integrating along the structure" overstates the case: for a truss the sum over members replaces the integral, but for a beam or frame the same principle becomes ∫mM/(EI) dx, an integral along the member. A student may think no integration is ever needed.
- ch 3 [low] Quiz Q4 answer: "The member's contribution is in the direction of the unit load" is loose: a single member's term is a scalar added into the sum, and it is the total Δ that has a direction. Also the answer skips the intermediate step that a compression–compression pair means both N and n carry the same sign.
- ch 4 [low] Section 1: The chapter treats the count D = m + r − 2j as decisive: 'D = 0 means determinate: equilibrium gives every force.' The count is only a necessary condition. An improperly arranged truss can give D = 0 and still be a mechanism, for example when two members cross without a joint at the crossing, so the crossing is counted as a joint but is not one. Standard texts state the count together with a check that the members are properly arranged.
- ch 4 [low] Lead / Section 2: The idealisation behind the method is never stated. A plane truss analysis assumes frictionless pins, straight members carrying axial force only, loads applied only at joints, and self-weight neglected. A student who does not know these conditions may apply the method to a member loaded between joints.
- ch 4 [low] Worked example 1, step 3: The angle θ appears without a definition. sin θ = cos θ = 0.7071 is written without saying which angle θ is.
- ch 4 [low] Worked example 1, steps 4 and 5: The equilibrium equations carry no units: '5 + AC × 0.7071 = 0' and 'AB + (−7.07 × 0.7071) = 0'. The 5 is a force in kN and AC, AB are in kN.
- ch 5 [high] Quiz Q6: The stated error does not produce the stated wrong answer. If the 1/2 in M(x) = w(L−x)²/2 is dropped, M doubles, so the integral gives wL⁴/(4EI), which is twice wL⁴/(8EI), not wL⁴/(2EI). A student who got wL⁴/(2EI) (four times too big) made a different mistake, so the answer as written misleads.
- ch 5 [low] Section 2, segment table: The table lists M(x) = 2(3−x)² kN·m and m(x) = (3−x) m with no signs, while the worked example uses the hogging-negative values −2(3−x)² and −(3−x) under a stated sagging-positive convention. The same chapter shows the same moment with two opposite signs, which is exactly the sign slip the traps warn about. The table also uses w = 4 kN/m without saying so.
- ch 5 [low] Section 3, closing paragraph: The moment expression M = wx²/2 assumes x is measured from the free end, but Section 1 and the worked example measured x from the fixed end, where M = w(L−x)²/2. A student can plug the fixed-end x into wx²/2 and get a wrong diagram.
- ch 5 [low] Figure caption: 'The unit-load moment falls as a straight line from 3 m' reads as a length, not a moment. The quantity is 3 kN·m per kN of unit load, which is numerically 3 m only because the unit load is 1 kN.
- ch 6 [high] Section 2 (fixed-fixed beam under UDL): The claim that the bending moment crosses zero at L/4 from each end is numerically wrong. Solving wL²/12 − wLx/2 + wx²/2 = 0 gives x = L(1 − 1/√3)/2 ≈ 0.211L from each end, not 0.25L.
- ch 6 [high] Quiz Q5 (against Section 2): Section 2 solves the fixed-fixed beam with only two redundants (the two end moments), which is the standard treatment for transverse loading once the two horizontal reactions are taken as zero. Q5 then says the beam has three redundants and counts six reactions against three equations, so the student cannot reconcile the two statements.
- ch 7 [low] Section 1, main formula: The three-moment equation is stated without its assumptions. It is valid for constant EI and no support settlement; with varying EI or settlement the coefficients and right side change, so a student could apply it outside its range.
- ch 8 [high] Section 1, sign convention: The sentence 'A hogging moment at one end and a sagging moment at the other have opposite signs' is false under the stated clockwise-positive member-end convention. Hogging at the left end is negative and sagging at the right end is also negative — same sign. Hogging at both ends, or sagging at both ends, are the cases with opposite signs.
- ch 8 [high] Section 1, start of the method: 'Imagine every joint is clamped' contradicts the worked example, where A and C are pinned and the FEMs are wL²/8, not the fixed-fixed wL²/12. The method locks only joints that can rotate; simple supports remain pins.
- ch 8 [low] Section 2, stiffness definition: The definition says 'far end held' for both cases, but the pinned far end is not held against rotation. It is held only in position.
- ch 8 [low] Worked example step 1 and figure table: Stiffness is written as 0.5EI and 0.75EI, but k = 3EI/L with L in metres gives 0.5EI/m and 0.75EI/m. The per-metre unit is dropped. The figure row 'k/EI = 3/L' also omits the unit m⁻¹.
- ch 8 [low] Beyond section: The final sentence 'Search for Hardy Cross moment distribution' is a search instruction, not study content, and the chapter should not include it.
