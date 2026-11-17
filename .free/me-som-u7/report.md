# me-som-u7: free-model run

- Book: `books/mech/me-som/me-som-u7.html`
- Status: ok
- Model calls so far: 33 (141,750 tokens in, 304,632 out), 7.1 minutes

## Checker

```
me-som-u7.html: 8 chapters, 13982 words, 9 figures, 159 KB
OK
```

## For the reviewer

- chapter 1: the figure cannot be drawn: tree label "Compression member" is too long; shorten it

## Reviewer notes (after any revision)

- ch 1 [low] Section 3: The ruler analogy is physically backwards as worded. A flat ruler does not bend easily about its thin edge; the thin edge (the short side of the rectangle) is the stiff direction. The easy bend is about an axis lying in the broad face, parallel to the width, giving the small I = b t³/12.
- ch 1 [low] Section 3: "Built-up sections need checking about both axes, and the smaller r governs" is loose. The governing quantity is the larger slenderness ratio Le/r, and Le can differ about the two axes because the end conditions about each axis may differ, so the smaller r alone does not always govern.
- ch 1 [low] Worked example 1: The chapter defines a vertical compression member as a column, then calls the same member a "vertical strut" in the example. A student may read this as contradicting the definition given 6 paragraphs earlier.
- ch 2 [low] Section 2, buckled shapes paragraph: "One fixed and one free gives a quarter-wave of length 2L" invites the reading that the quarter-wave itself is 2L long, which would make the effective length larger than 2L. The other three sentences in that paragraph give the effective length (Le), so this one breaks the pattern. The actual column of height L is a quarter of a sine wave; the equivalent half-sine spans 2L.
- ch 2 [low] Section 2, first paragraph after the formula: "the distance between points of zero bending moment changes" is true for pinned-pinned, fixed-fixed and fixed-pinned, but not for fixed-free: the fixed end carries the maximum bending moment, not zero. A student may look for a zero-moment point at the fixed end and get lost.
- ch 2 [low] Section 1, first two paragraphs: The text writes M = Py and then says "the moment acts to bend the column back toward the straight line". M = Py is the applied moment, which increases the bow; only the internal elastic moment EI d²y/dx² is restoring. Students often misread which moment carries the minus sign.
- ch 3 [high] Section 3, last sentence: The sentence is broken and unreadable: 'A column with λ 7.4.' The comparison sign and the whole second half are missing, so the student never learns what happens for λ below 89, which is the main point of the section.
- ch 3 [low] Section 3, second paragraph: Euler is valid up to the proportional limit, not the yield stress. Saying the proportional limit is 'taken as the yield stress' quietly shifts the limit upward; for mild steel the proportional limit sits below yield, so the cut-off slenderness is nearer 80-85 than 89 in real design.
- ch 4 [high] Section 2, large-λ limit bullet, repeated in Quiz Q2 answer: The algebra drops the area A. Writing P → σcA/(aλ²) = (σc/a)/λ² makes P equal to a stress, so the two sides of the equals sign have different units (N versus N/m²). Euler's load is P = π²E(A/λ²), not π²E/λ².
- ch 4 [low] Section 2, definition of σc: Calling σc the 'crushing (compressive yield) stress' is only right for ductile steel. For cast iron and timber the tabulated σc is the ultimate crushing strength, and those materials show no yield point.
- ch 4 [low] Lead paragraph: 'Stays safe at every slenderness ratio' suggests P is an allowable load. P is a crippling (failure) load; the factor of safety comes later in Section 3.
- ch 4 [low] Worked example 1, step 8 and answer line: 'Euler is 2.9 times the Rankine value ... about 2.9 times too high' mixes two readings: 2.9 times the correct load, or 2.9 times too large (which would mean 3.9 times). Rounding also jumps between 13.25 × 10⁶ N and 13 247 kN.
- ch 5 [high] figure caption (and flowchart edges c → d and c → e): The caption says 'the same cut shows why longitudinal stress is half the hoop stress'. The diametral cut (cut along a diameter) balances pressure p d L against two wall strips and gives hoop stress only. Longitudinal stress needs a different cut, taken across the axis through the end cap. The flowchart also draws both stresses out of the same 'Balance forces' box, so a student is taught a wrong derivation step.
- ch 5 [low] exam traps, first bullet: 'p d/(2t) uses diameter; p r/t gives the same number, so the slip hides' is muddled. Using p r/t correctly gives the same answer, but dropping the radius value into the d slot halves the result; the sentence does not say which mistake it means.
- ch 6 [high] Section 2, first paragraph: It says the direct stress σ is the same in all three directions. For a thin spherical shell the membrane stress is equal in the two directions in the surface, while the radial stress is negligible and taken as zero. The text's own Hooke's law result ε=(σ/E)(1−ν) is for biaxial surface stress; if all three stresses were equal it would be ε=(σ/E)(1−2ν).
- ch 6 [high] Beyond: The formula dV/V=(2σ/E)(1−2ν) is the volumetric strain (dilatation) of the wall material under biaxial plane stress, not the change in the internal gas volume. Since V is defined as πd³/6, the internal volume, this contradicts the standard thin-shell result and the worked example. Plane stress with zero radial stress is also already the standard assumption, not a stricter one.
- ch 6 [low] Section 2, formula definition for V: d was defined in mm in Section 1, but V=πd³/6 is labelled in m³. The unit of V follows the unit of d; the worked example uses d in metres. This unit inconsistency can cause conversion mistakes.
- ch 6 [low] Worked example step 3 and step 7; Quiz Q5 and Q6: Expressions such as 75×10⁶/2×10¹¹ are ambiguous and, read strictly left to right, wrong; the denominator is meant to be (2×10¹¹). The numerical answers are correct, but the notation can mislead.
- ch 6 [low] Section 3, first sentence: 'A dished end is part of a sphere' is too broad. Ellipsoidal and torispherical heads, mentioned later, are not spherical over the whole profile. The membrane formula pd/(4t) applies to the spherical crown or a hemispherical head.
- ch 7 [high] Section 1, exam traps (bullet 3), Quiz Q7: Section 1 defines the thin-cylinder formula as σθ = p d/(2t) with d as the mean diameter. With mean diameter the worked example gives d = 150 mm, so the thin formula returns 60 × 150/(2 × 50) = 90 MPa, not the 60 MPa quoted in the exam traps and in the Q7 answer. A student who follows the chapter's own definition gets a different number from the one the book states.
- ch 7 [low] Lead: The lead says the bore 'is always the first point to yield'. That holds for internal pressure only; under external pressure, or with shrink fits, the inner surface is not necessarily the most highly stressed point.
- ch 7 [low] Worked example 1, step 3: The step writes A = B/0.01 = 100B without saying where 0.01 comes from; a student reading on a phone may lose the thread between ro² = 0.01 and the number.
- ch 8 [high] Section 1, first bullet under the shrink fit: The direction of the outer tube's movement is reversed. When the outer tube is shrunk on, its bore opens out (its radius grows) to sit on the inner tube; it does not close in. Only the inner tube's outside is squeezed down. As written, a student would think both tubes shrink, which contradicts the physics of the fit and the sign of the residual stresses given just below.
- ch 8 [low] Section 2, the 'where' note after the superposition formula: 'the two hoop stresses simply add because they act on the same element in the same direction' reads as if the stresses can never cancel. They add algebraically, and a negative residual value is what reduces the tensile pressure value.
- ch 8 [low] Section 2, formula definitions: 'σθ is the hoop stress at radius r in metres, in N/m² (Pa)' attaches the metres to the stress instead of to r, which is confusing.
