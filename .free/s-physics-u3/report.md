# s-physics-u3: free-model run

- Book: `books/common/s-physics/s-physics-u3.html`
- Status: ok
- Model calls so far: 31 (132,803 tokens in, 247,366 out), 5.7 minutes

## Checker

```
s-physics-u3.html: 9 chapters, 17511 words, 10 figures, 179 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 3 (curl): The sentence says 'The determinant form below gives a vector', but the formula shown is the expanded component expression, not a determinant. A student looking for a determinant will be confused.
- ch 1 [low] Quiz Q7 answer: 'E = −∇V in a charge-free region' suggests the relation E = −∇V needs the charge-free condition. In electrostatics E = −∇V holds quite generally; the charge-free condition is what makes ∇·E = 0.
- ch 1 [low] Section 2 and Section 3 cross-references: '(see Gauss's law)' and '(see electric potential)' are plain text, so a reader on a phone cannot jump to those chapters.
- ch 2 [low] Lead: "Every electric field is this law added up over all charges" is too broad: an electric field also arises from a changing magnetic field, which Coulomb's law does not cover. A student could carry the wrong generalisation out of the electrostatics unit.
- ch 2 [low] Section 1: "The constant 1/(4πε₀) equals 9×10⁹ N m² C⁻²" states an exact equality; the accepted value is 8.99×10⁹, rounded here to one significant figure.
- ch 2 [low] Section 2: The point-charge field is printed as "E = (1/(4πε₀)) Q / r² r̂", which can be misread as Q divided by (r²r̂).
- ch 2 [low] Section 2, field-line bullet: "The number of lines through unit area shows the field strength" is loose: the count must be per unit area drawn perpendicular to the lines, otherwise a tilted area gives a wrong idea of the field.
- ch 2 [low] Sections 2 and 3: The same remark about Gauss's law being quicker for symmetric distributions appears at the end of both sections; the repetition adds nothing.
- ch 3 [high] Section 3, first paragraph on the thin shell: The sentence reads 'For r  R it encloses Q' — the inequality sign is missing, so the condition is unreadable. Worse, the section never states the field inside the shell (E = 0 for r < R), even though the worked quiz Q4, exam trap 4 and exam trap 5 all use it. A student reading only the body would not know the inside result.
- ch 3 [high] Section 4, last paragraph: 'Air breaks down near 3 × 10⁶ V/m, which is why lightning rods and high-voltage busbars are rounded' is wrong. Lightning rods are deliberately pointed, so that the large σ and E at the tip produces corona and a conducting path for the strike. Only hardware that must avoid corona (busbars, corona rings, terminal ends) is rounded.
- ch 3 [low] Worked example 1, step 8: The unit of the quantity 2πε₀r is given as C²/N. Since r carries a metre, the unit is C²/(N·m). The final N/C comes out right only with the correct unit.
- ch 3 [low] Section 4, first paragraph: 'All excess charge therefore sits on the outer surface' is stated without the condition that the cavity is empty. If a charge is placed inside a hollow conductor, an equal and opposite charge is induced on the inner wall, and the next sentence about shielding can then confuse the reader.
- ch 4 [low] Section 3, boundary conditions: The sentence 'the normal derivative of V jumps by σ/ε₀' hides a sign. Taking the normal n to point from side 1 to side 2, the field jump is E₂ₙ − E₁ₙ = σ/ε₀, and because Eₙ = −∂V/∂n the potential derivative obeys ∂V/∂n|₁ − ∂V/∂n|₂ = σ/ε₀, i.e. ∂V/∂n|₂ − ∂V/∂n|₁ = −σ/ε₀. A student reading 'jumps by σ/ε₀' will very likely write the jump with the wrong sign.
- ch 5 [low] Section 1, polar and nonpolar molecules: The phrase 'its centre of positive charge on top of its centre of negative charge' can be read as the two centres being separated vertically, which would contradict the next clause that there is no dipole moment.
- ch 5 [low] Section 3, the two battery cases: The battery-connected case only says 'the battery supplies the extra charge'. It does not say where the battery's energy goes, so a student cannot reconcile the battery work V·ΔQ with the rise in stored energy U₀ → ε_rU₀.
- ch 6 [high] Exam traps, first trap (dl × r̂ order): The trap says 'dl × r̂ points from the element to the field point'. That is wrong: r̂ is the vector that points from the element to the field point. The cross product dl × r̂ is perpendicular to both dl and r̂, and only its direction (by the right-hand rule) is along dB. As written, a student will believe the cross product is the position vector.
- ch 6 [high] Section 3, field on the axis of a loop: The formula is printed as B = μ₀IR²/[2(R²+z²)3/2]. With no superscript, the '3/2' reads as multiplication by 3/2, which makes the expression dimensionally wrong (B would not come out in tesla).
- ch 6 [low] Worked example 1, step 3: The text says 'Cancel π and 2', but the fraction shown, (4×10⁻⁷ × 2)/(2 × 0.10), still contains the 2 in numerator and denominator. The arithmetic is right, but the instruction and the displayed line do not match.
- ch 7 [low] Quiz Q2: The question asks for the base equivalence of the henry, but the answer only gives derived equivalents (Wb/A and V·s/A). The base-SI form is never stated, so the answer does not cover that part of the question.
- ch 7 [low] Section 3, solenoid formula: L = μ₀n²Al holds for an air or vacuum core only. The same paragraph says L is set by 'the core material', but the formula never shows where the core enters, so a student with a ferrite-core choke cannot use it.
- ch 7 [low] Section 1, flux integral: 'dS a small area element with its outward normal' is ambiguous here. The loop is an open surface, which has no inside or outside. The normal direction must be tied to the sense in which the loop is walked, otherwise the minus sign in ∮E·dl = −dΦ/dt is unexplained.
- ch 7 [low] Section 3, LR circuit: The symbol ε is used for the induced emf in Sections 1 and 2 and then reused for the battery emf in ε = iR + L di/dt. A student can read the equation as saying the induced emf drives the current.
- ch 7 [low] Quiz Q7: I²R is power in watts, not heat, and the answer calls it heat. 'Two identical loops of the same area' also repeats itself, since identical loops already have equal area.
- ch 8 [high] Section 2, the displacement-current formula block: The chained equality I_d = ε₀ dΦ_E/dt = d/dt ∫ D·dS is true only in vacuum. In a dielectric, Φ_E = ∫E·dS does not give the displacement current; the correct general form uses D, and ε₀ dΦ_E/dt is a vacuum special case. The text just above the formula says this, but the formula contradicts it, so a student will carry the wrong relation into matter.
- ch 8 [low] Figure spec: The node labelled 'Gauss for E' carries the note ∇·D = ρ (label and equation use different fields), and the edges from the two Gauss-law nodes into 'Faraday' suggest the Gauss laws produce Faraday's law. Section 4 correctly says the wave equation comes from Faraday's law combined with the Ampere–Maxwell law only.
- ch 8 [low] Section 3 and Quiz Q5: The symbol σ is used twice with different meanings: σ_f is free surface charge density (C/m²) in the boundary conditions, and σ is conductivity (S/m) in J = σE. On a phone screen in a hurry, students mix them up.
- ch 9 [low] Section 4 (dipole antenna): An FM station at 100 MHz radiates λ = 3 m, so its tower is a few metres tall' is misleading: a real FM mast is tens of metres tall, and what is about λ/2 (roughly 1.5 m) is the radiating dipole element mounted on top of it. A student may read this as a claim about the physical mast.
- ch 9 [low] Quiz Q2 answer: The argument stops at ∂E_z/∂z = 0, which only says E_z does not vary with z. It does not by itself forbid a longitudinal field that is uniform in space but varies in time, so the step from 'no z-variation' to 'no z-component' is incomplete and a student could misread it.
- ch 9 [low] Lead paragraph: Saying the fields 'carry energy, momentum and pressure in a direction given by E × B' is sloppy: pressure is not carried along a direction, it is a force per unit area that the wave exerts on a surface. A student may take away the wrong picture.
- ch 9 [low] Exam trap 3: 'A phase difference appears only in a conducting medium or in a standing wave' is too strong. A phase difference between E and B also appears in total internal reflection (evanescent wave), in the near field of a dipole, and in anisotropic media.
