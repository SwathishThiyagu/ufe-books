# s-physics-u1: free-model run

- Book: `books/common/s-physics/s-physics-u1.html`
- Status: ok
- Model calls so far: 26 (99,254 tokens in, 200,583 out), 6.2 minutes

## Checker

```
s-physics-u1.html: 7 chapters, 11662 words, 8 figures, 127 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 4, work formula: The sentence says 'for a constant force along the motion, W = F d cos θ'. If the force is along the motion then θ = 0, so the cos θ factor has no role; the words and the formula contradict each other and students may memorise cos θ as belonging to a force along the motion.
- ch 1 [low] Section 1, definition of force: 'A force is a push or pull that changes a body's velocity' is not true of a single force: one force among several may change nothing (a book pressed on a table). Only the net force changes velocity.
- ch 1 [low] Lead paragraph: 'The same bookkeeping gives conservation of energy and of angular momentum' overstates the case. Momentum conservation follows from the action–reaction pairs, but energy conservation needs the internal forces to be conservative, and angular momentum conservation needs the external torque about the chosen point to vanish (central forces).
- ch 1 [low] Section 1, third law: The third law is stated as requiring the two forces to lie 'along the same line'. That holds for contact and gravitational forces, but not for every pair — the magnetic force between two moving charges is not in general along the line joining them.
- ch 1 [low] Section 1, impulse: 'A force acting for a short time delivers an impulse: ΣF Δt = Δp' uses the symbol ΣF as if the force were constant. In the bat example the force varies over the 0.010 s.
- ch 1 [low] Section 4, potential energy: 'F = −dU/dx' is the one-dimensional form only; students meeting a central force two lines later may apply it along the wrong axis.
- ch 2 [high] Figure and its caption (Section 2): The plotted mild-steel curve makes the straight-line elastic part run up to about 400 MPa and puts yield near 415–430 MPa, while standard values for mild steel are a proportional limit near 200 MPa and a yield point near 250 MPa. The strain axis also stops at 8×10⁻³, so fracture appears at about 0.7 % strain. That is brittle behaviour and contradicts the text, which says mild steel is ductile with a long plastic region. A student reading the numbers off the axes will get wrong values for yield stress and fracture strain.
- ch 2 [low] Figure, 'Hooke line' series: The Hooke line is drawn all the way to 600 MPa, far past the proportional limit, without a label saying it is only an extension of the elastic line.
- ch 2 [low] Section 1: The text says some books write σ for Poisson's ratio, but σ was defined two lines earlier as stress and is used again in the bulk-modulus formula. Students will read σ as stress everywhere.
- ch 2 [low] Exam traps, bullet 3: The trap says writing strain in m/m loses marks. m/m equals 1, so it is a harmless way to show strain is dimensionless; only N/m² is genuinely wrong for strain. As written, a student may think m/m is an error.
- ch 3 [high] Quiz Q4: The denominator in the substitution is wrong. 4bd³δ = 4 × 0.020 × 1.25×10⁻⁷ × 4.9×10⁻³ = 4.9×10⁻¹¹ m⁴, not 2.0×10⁻⁹ m⁴. With the printed 2.0×10⁻⁹ the division gives 4.9×10⁹ Pa, which contradicts the stated answer 2.0×10¹¹ Pa, so the working does not lead to the result.
- ch 3 [low] Section 3: A roof truss is not I-shaped; it is a triangulated frame. Listing trusses among shapes that "follow this shape" can mislead a student looking at a truss drawing.
- ch 3 [low] Quiz Q6: A girder normally spans two supports, but the answer justifies the smaller sag with the cantilever formula δ = WL³/(3YI). The constant is wrong for a simply supported girder, though the conclusion (larger I gives smaller sag) is right.
- ch 4 [high] Section 2: The sentence "If ρ t is negative and the sphere rises" is garbled and states no condition. Read literally it is meaningless, and the student cannot tell when the ball rises.
- ch 4 [low] Section 1 (and worked example): The viscosity of glycerine is quoted as ≈ 0.8 Pa·s with no temperature, while water is correctly tied to 20 °C. Glycerine's η changes steeply with temperature: about 1.4 Pa·s at 20 °C and about 0.8 Pa·s only near 27–30 °C, so a student may memorize 0.8 Pa·s as the 20 °C value.
- ch 4 [low] Figure: The plotted curve 6.9(1 − e^(−2t)) has a time constant of 0.5 s, so the ball takes about 2 s to reach terminal speed. For the 2 mm steel ball of the worked example the real time constant is a few milliseconds, so the figure's time axis is not physical.
- ch 5 [low] Figure spec, node 'formula' and aria text: The label 'T = mg/2πrf' and the aria string 'T = mg/2πrf' can be read as (mg/2π)·rf, which is a different formula; the text of Section 2 writes T = mg/(2πrf). A student copying the figure gets the wrong expression.
- ch 5 [low] Lead: 'The drop breaks when its weight almost equals the force around the tube rim' is loose. With the correction factor the breaking weight is 2πrT f, which is clearly less than 2πrT (f = 0.87 in the worked example), so 'almost equals' hides the reason f exists.
- ch 5 [low] Section 2, procedure list: The steps never say the drops must form slowly. The static balance mg = 2πrT f and the correction tables assume a quasi-static drop (roughly one drop per second); fast dripping gives wrong results.
- ch 6 [low] Worked example 1, opening line: The rail is said to be 'clamped at both ends at 25 °C', but part (a) then asks for the gap an expansion joint must allow. A clamped rail has no free end, so the two halves of the question contradict each other and a student may not see which case is which.
- ch 6 [low] Exam traps, third bullet: 'β ≈ 2α and γ ≈ 3α hold for an isotropic solid, not for a long rod where only length matters' is misleading. The relations do hold for the material of a rod; its cross-section also grows as 2αΔT. The sentence can leave a student thinking β ≠ 2α for rods.
- ch 6 [low] Quiz Q1: The question asks for the SI unit, but the answer gives 'per °C or per K'. Only per kelvin (K⁻¹) is the SI unit; per °C is a commonly used non-SI equivalent with the same number.
- ch 6 [low] Exam traps, second bullet: The bullet states that a per-°F coefficient is smaller than the per-°C one but never gives the factor, so a student cannot actually carry out the conversion it demands.
- ch 6 [low] Section 1 table and figure: The figure compares brass with iron (α = 12×10⁻⁶ /°C) but the table has no iron row; it lists steel at the same value. A reader checking the figure against the table finds no entry for iron.
- ch 7 [low] Worked example 1, step 6: The arithmetic uses the rounded lifetime: 2.94×10⁸ m/s × 11.1×10⁻⁶ s = 3.26×10³ m, not 3.25×10³ m. The printed 3250 m comes from the unrounded 11.066 μs, so the shown numbers and the shown answer do not quite match.
- ch 7 [low] Exam traps, 4th bullet: 'only c and the interval s² are shared' overstates the case; rest mass, proper time, proper length and electric charge are also frame-independent. A student may read this as saying nothing else is invariant.
- ch 7 [low] Section 1: The ball example gives 30 m/s for the ground observer but does not say the ball is thrown forward along the train's motion. Thrown sideways or backward, the ground speed is different.
