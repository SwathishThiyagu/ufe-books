# me-fluid-u1: free-model run

- Book: `books/mech/me-fluid/me-fluid-u1.html`
- Status: ok
- Model calls so far: 37 (144,856 tokens in, 272,836 out), 7.4 minutes

## Checker

```
me-fluid-u1.html: 9 chapters, 16230 words, 10 figures, 169 KB
OK
```

## For the reviewer

- chapter 2: the figure cannot be drawn: note "1/K in 1/Pa" runs off the right edge; shorten it
- chapter 2: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [high] Section 2: The shrinking-volume argument is stated backwards. The text says that as ΔV shrinks 'at first the value jumps about' and 'below some size, the value settles to a steady plateau'. In the standard picture the steady plateau lies at large ΔV, and fluctuations grow as ΔV is shrunk below the averaging volume, becoming violent at molecular scales. As written, a student will conclude that very small volumes give smooth, reliable averages.
- ch 1 [low] Lead: The lead says the continuum applies when the region of interest is 'much larger than the molecular spacing'. For a gas the controlling length is the mean free path, which is hundreds of times the molecular spacing. A student could take the wrong length scale from the lead, though Section 1 later puts it right.
- ch 1 [low] Section 3, table row 'Typical use': The stream function is listed as a use of the ideal-fluid model, but a stream function exists for any two-dimensional incompressible flow, real or ideal. Only potential flow (velocity potential) genuinely needs the inviscid, irrotational assumption.
- ch 2 [high] Section 1 (mass density, last paragraph): The density rise at the bottom of a 100 m dam is given as about 0.5 %, which is ten times too large. The pressure rise is only ρg h ≈ 1000 × 9.81 × 100 ≈ 9.8 × 10⁵ Pa, and Δρ/ρ = Δp/K = 9.8 × 10⁵ / 2.2 × 10⁹ ≈ 4.5 × 10⁻⁴, that is about 0.05 %. A student quoting 0.5 % would be off by a factor of ten.
- ch 2 [low] Section 3 (bulk modulus and compressibility, paragraph on water and mercury): "Air has K ≈ 10⁵ Pa, five orders of magnitude softer" overstates the gap. Water's K is 2.2 × 10⁹ Pa and air's is about 1 × 10⁵ Pa, a ratio of about 2.2 × 10⁴, which is four orders of magnitude, not five.
- ch 2 [low] Figure caption: The caption says "only specific weight carries units of force", but the same figure gives bulk modulus in Pa, and 1 Pa = 1 N/m², which also contains a force unit. The sentence contradicts the figure's own labels and can confuse a student about units.
- ch 2 [low] Section 2 (specific gravity paragraph): "Petrol has SG about 0.72, so one litre weighs about 0.72 kg" mixes mass and weight in the same section that insists weight is a force measured in newtons. A student may copy "weighs 0.72 kg" into an answer.
- ch 3 [low] Section 1 and Section 3, first use of the gap symbol: The gap is written as t ("Across the gap t the velocity changes from 0 to U", "du/dy = U/t") but t is never explicitly defined where it first appears, and it is missing from the list of terms under τ = μ du/dy. A student meeting the formula cannot tell what t is or its unit.
- ch 3 [low] Section 3 assumptions and exam trap 5: The chapter says du/dy = U/t needs a thin film and fails "if the gap is wide". For steady, fully developed laminar flow between parallel plates with no pressure gradient, the profile is exactly linear for any gap: Navier–Stokes reduces to d²u/dy² = 0 whatever t is. Gap width only matters through edge effects, entry length and possible instability, so the stated criterion is technically wrong.
- ch 3 [low] Section 2, explanation of kinematic viscosity: "Dividing by density removes the inertia of the fluid" is misleading. Dividing by density does not remove inertia; it turns viscosity into a momentum diffusivity (m²/s) and gives the viscosity-to-density ratio that appears in the Reynolds number.
- ch 4 [high] worked example, step 6: The comparison sign is missing: the text reads 'B is shear-thinning because n  1', which is unreadable and contradicts the definition in Section 2 (B has n = 0.6).
- ch 4 [high] exam traps, item 4: The comparison sign is missing again: 'n  1 is shear-thickening' does not state which way the inequality goes, so a student cannot tell it means n greater than 1.
- ch 4 [low] section 2 and section 3: The same food is placed in two different classes: ketchup (tomato sauce) is given as pseudoplastic in Section 2 and as a Bingham plastic in Section 3. A student may think one of the two statements must be wrong.
- ch 5 [high] Section 3, first paragraph (contact angle): The sentence reads 'If θ  90°, it does not wet the wall', with the comparison sign and the wetting half of the rule missing. A student cannot read the definition of wetting, and the mercury example (θ ≈ 140°) then hangs on an incomplete sentence.
- ch 5 [high] Worked example 1, step 4: The denominator ρgr is written with unit N/m³. The product (kg/m³)(m/s²)(m) = N/m², not N/m³. Only N/m² divided into the numerator 0.144 N/m gives metres, so the shown unit contradicts the division in step 5.
- ch 5 [low] Section 2, the numerical illustration: 'A 1 mm water droplet has Δp = 144 Pa' is ambiguous: the value 144 Pa comes from R = 1 mm, but most readers take 'a 1 mm droplet' to mean a diameter of 1 mm (R = 0.5 mm, Δp = 288 Pa). The 0.1 mm case has the same ambiguity.
- ch 5 [low] Figure note (cap node): The note '2.94 cm in 0.5 mm tube' does not say whether 0.5 mm is the radius or the diameter, and the formula uses the radius. A student reading it as diameter would get 5.88 cm.
- ch 6 [high] Section 3, sign care paragraph: The sentence "If a point is above the free surface, h is negative and gauge pressure can be negative" invites students to apply p = p0 + ρgh with the liquid density to the gas space above the water surface. In a sealed tank, or in an open tank, the air above the free surface is a different fluid at almost constant pressure p0; the liquid depth rule does not apply there. The rule holds only inside one continuous fluid of density ρ.
- ch 6 [low] Section 2, column derivation: "The fluid above pushes down with force p0A" is loose: the top face of the column is the free surface, and the downward force there comes from the atmosphere or the pressurised gas above, not from the same liquid.
- ch 6 [low] Section 3, effective gravity: "Replace g by g_eff in the depth rule" does not say how h is measured. In a tilted free surface, vertical depth below the free surface is not the h that appears in p0 + ρg_eff h; h must be measured along the direction of g_eff, perpendicular to the isobars.
- ch 6 [low] Quiz Q2 answer: The answer says only that a horizontal line has constant h. That is true only if the fluid is continuous and p0 is the same at every point of the line; the statement as written hides this assumption.
- ch 7 [low] Section 1, the sentence 'The liquid settles when the pressure difference is balanced by the weight of the liquid column': Slightly imprecise: the balance is against the weight of the extra (unbalanced) column, that is, the height difference between the two surfaces, not the whole column.
- ch 7 [low] Section 2, U-tube bullet, 'The U-tube can measure gas pressure and higher pressures because mercury is dense': Density is only part of the reason. A U-tube measures gas pressure because the gauge liquid is held separately in the tube and cannot escape into the pipe; density only keeps the tube short when the pressure is high.
- ch 7 [low] Quiz Q4, answer: The answer says 'the common water terms cancel' but never shows where the remaining −ρw g h comes from, so a student cannot see how the water term enters the final formula.
- ch 8 [high] Section 2, paragraph after the resultant formula: The sentence 'The pressure volume gives the line of action: its volume equals the force magnitude and its centroid lies on the line of action' is borrowed from the plane-surface pressure prism. On a curved surface the pressures act in different directions, so a scalar volume of pressure cannot equal the magnitude of the resultant. A student will carry a wrong rule into the curved-surface problems.
- ch 8 [low] Lead, third sentence: 'F = p_c A at the centre of pressure' fuses two separate facts and can be read as saying p_c is the pressure at the centre of pressure. Actually p_c is the pressure at the centroid; the force acts at the centre of pressure, which is lower.
- ch 9 [low] Section 2 (BM formula): The chapter says I is the second moment of the waterplane area 'about the axis of tilt' but does not say the axis must pass through the centroid of the waterplane. For a waterplane that is not symmetric fore-and-aft, a student will use the wrong axis.
- ch 9 [low] Section 2 (metacenter definition): Defining M as the point where the line through the new B cuts 'the body's original centreline' is loose. The correct reference line is the original vertical through the old B; only for a symmetric body does this coincide with the centreline.
- ch 9 [low] Section 3 and figure caption: The figure caption already uses the barge numbers GM = 2.6667 − 0.75 = 1.9167 m, but the barge is only introduced in Worked example 1 below the figure. At that point the numbers have no meaning.
- ch 9 [low] Section 3 last line: 'A GM in metres is read directly as a stability margin' is vague; GM is a length, not a margin in some other unit, and a very large GM is not always desirable.
- ch 9 [low] Quiz Q3 answer: 'The new buoyancy line lies on the same side as the tilt beyond G' can be misread. The real reason is that M lies below G, so the weight and the buoyancy force form a couple acting in the direction of the tilt.
- ch 9 [low] Chapter style: Both 'Center' and 'centre' are used (Center of buoyancy B, then centre of gravity G). Inconsistent spelling in a definition paragraph.
