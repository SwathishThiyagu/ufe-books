# e-mech-u4: free-model run

- Book: `books/common/e-mech/e-mech-u4.html`
- Status: ok
- Model calls so far: 27 (108,161 tokens in, 236,146 out), 7.2 minutes

## Checker

```
e-mech-u4.html: 8 chapters, 16143 words, 9 figures, 153 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 2 (four standard results for lines) and its table: The triangle is listed as one of the 'four standard results for lines' with centroid at h/3 from the base. That is the centroid of a triangular area, not of a line (the perimeter of a triangle has a different centroid, not a simple h/3 rule). The paragraph immediately after the table says 'These are centroids of lines, not of areas', which directly contradicts the triangle entry.
- ch 1 [high] Section 1, centre of gravity and centre of mass: 'If the body has uniform density, G is also the centre of mass' gives the wrong condition. The centre of gravity coincides with the centre of mass whenever the gravitational field is uniform (g the same at every point of the body), whatever the density distribution. Uniform density alone does not make them coincide, and a body of non-uniform density still has G at its centre of mass in a uniform field.
- ch 1 [low] Lead: 'find where a composite beam section carries its area' is vague; a student will not see what is being located.
- ch 1 [low] Section 3 and Worked example 1: The same L-shaped wire problem is stated and solved twice, once as a bullet list in Section 3 and again as Worked example 1 with the same numbers. On a phone this is wasted space and invites the reader to think they are two different problems.
- ch 1 [low] Section 1, first paragraph: Small element weights are written dW while being summed with Σ ('the total weight W is the sum of those small weights dW'). The d-notation suggests an integral, but the chapter says integration comes in 4.2.
- ch 2 [high] Worked example 1, step 1 and answer: The axes are set with x measured from the vertical centre line, so the centroid's x-coordinate on those axes is x̄ = 0, not 50 mm. The answer then says '50 mm from the vertical centre line, i.e. on the centre line', which contradicts itself: 50 mm from a line is not on it. A student cannot tell which reference the 50 mm belongs to.
- ch 2 [low] Figure caption/table title: The table title gives units for the area column (mm²) and the last column (10³ mm³) but not for the middle column, which holds ȳ in mm. A reader has to guess the units of the 40, 90 and 67.8 entries.
- ch 3 [low] Section 3, last bullet: The conversion factors are incomplete and misleading. A length mismatch (cm against mm) changes x̄ by 10, an area mismatch (cm² against mm²) by 100, and a volume mismatch (cm³ against mm³) by 1000. Saying 'a factor of 10 or 1000' skips the factor 100, which is exactly the one a student meets when S is recorded in cm² and L in mm.
- ch 3 [low] Figure caption: 'both the outer surface area and the enclosed volume' suggests only the outward-facing half of the torus surface is being found. The theorem gives the whole surface of the ring, inner and outer together.
- ch 4 [high] Worked example 1, step 2: The intermediate product is given the unit mm⁵. b h³ is a length times a length cubed, so it is length to the fourth power; the unit carried through the line must be mm⁴, matching the final answer.
- ch 4 [high] Quiz Q6: The question says the two beams have equal area, but 100 mm × 200 mm = 20,000 mm² while 150 mm × 150 mm = 22,500 mm². The premise is false, and the marked answer repeats it implicitly by crediting the result to shape alone at equal area.
- ch 4 [low] Section 3, circle sentence: "A diameter is a diameter, so no axis needs naming" is unclear; a student may read it as saying the axis direction does not matter for non-circular shapes too.
- ch 4 [low] Lead: "depends not on how much material it has but on how far that material sits from the neutral axis" reads as if area is irrelevant, which contradicts the section on scaling where both b and h enter.
- ch 5 [high] Section 2, last paragraph (why the theorem fails for thick plates and shafts): The direction of the thickness contribution is reversed. Writing Ix = ∫(y²+z²)dV, Iy = ∫(x²+z²)dV and Iz = ∫(x²+y²)dV, the out-of-plane material adds 2∫z²dV to Ix + Iy and adds nothing to Iz. So the sum fails because Ix + Iy is bigger than Iz, not because the material adds to Iz. The chapter says the opposite.
- ch 5 [high] Quiz Q5: The answer gives the same reversed reason (length material contributing to the polar moment but not to the in-plane moments). For a body of length along z, the polar moment about the length axis is ∫(x²+y²)dV and carries no z² term, while Ix and Iy each carry a z² term. The stated reason is wrong even though 'larger' / 'theorem fails' is the right conclusion.
- ch 5 [low] Quiz Q4: The rectangle is given only as '40 mm by 60 mm' with no statement of which side lies along x, yet the answer assigns Ix = 40 × 60³/12. A student cannot tell which axis is x.
- ch 6 [low] Section 2, solid-circle integration: The chain jumps from the integral to 2π[r⁴/4] and then to πd⁴/32 without showing the limits being put in, so the middle expression is not a number and a student cannot see where d/2 enters.
- ch 6 [low] Section 1, perpendicular axis theorem sentence: Calling the perpendicular axis theorem "read as a definition" is confusing: J = Ix + Iy follows from r² = x² + y², it is not a separate definition of J.
- ch 6 [low] Lead: The lead says the radius of gyration is "the size of a thin ring that would behave the same way", but the axial radius of gyration k corresponds to concentrating the area on a line at distance k; only the polar radius kₚ corresponds to a ring.
- ch 6 [low] Quiz Q7 answer: The last sentence ("its material is used less efficiently than a hollow shaft of the same area") was not asked for, and "same area" is ambiguous — same area as what?
- ch 7 [high] Quiz Q6 (and the last sentences of Section 2): The answer says plotting Ixy downward 'makes the angle 2θp come out with the same sense as the physical rotation'. With the chapter's own conventions (θ counterclockwise, Ix′y′ = ((Ix−Iy)/2) sin 2θ + Ixy cos 2θ), the plotted point (Ix′, Ix′y′) turns counterclockwise by 2θ as θ increases. Plotting Ixy downward flips the ordinate, so the point then turns clockwise, i.e. opposite to the physical rotation. In the worked example the x-axis point sits 50.2° above the horizontal on a downward plot, and I₁ lies 50.2° clockwise from it, while the true principal axis is 25.1° counterclockwise from x. A student following Q6 will draw the principal axis on the wrong side.
- ch 7 [low] Quiz Q7: With Ix = Iy and Ixy = +4 × 10⁶ mm⁴, the formula gives tan 2θp = −2Ixy/(Ix − Iy) = −∞, so 2θp = −90° and θp = −45° for the larger moment. The answer states 2θp = 90°, θp = 45°, which is the axis of I₂ = 6 × 10⁶ mm⁴, so the larger-moment direction is reported with the wrong sign and is not identified.
- ch 7 [low] Section 1, composite-area sentence: 'For a composite area, add Aᵢ x̄ᵢ ȳᵢ for all parts' drops each part's own centroidal product Īxy,i. That term is zero for rectangles but not for triangles, so a student adding a triangle to a composite will get Ixy wrong.
- ch 7 [low] Exam traps, second bullet: 'Using a product of inertia about non-centroidal axes in the principal-moment formula without first shifting it to the centroid' suggests the principal-moment formulas need centroidal axes. They do not: they hold for any perpendicular pair x, y through the same point and give the principal moments about that point. The real error is mixing Ix, Iy about one pair with Ixy about a different pair.
- ch 7 [low] Exam traps, third bullet: 'The two roots are 90° apart, not 180°' can be misread as being about the roots of 2θp, which are in fact 180° apart.
- ch 8 [high] Exam traps, fifth bullet: The trap says the mass comes out a billion times too small when volume is in mm³ with density in kg/m³. Numeric mm³ is 10⁹ times the m³ value, so using it directly with kg/m³ gives a mass 10⁹ times too large, not too small.
- ch 8 [low] Section 1 (radius of gyration) and Quiz Q6: The text says k is not the outer radius unconditionally. For a thin ring, k = r, so the radius of gyration equals the ring radius/outer radius. Q6 repeats 'not the actual outer radius', which is false for a thin ring.
- ch 8 [low] Section 3, composite bodies paragraph: The ring-versus-disc energy comparison says a ring stores more energy for the same mass and speed, but omits 'same radius'. With same mass and same angular speed but different radii, a solid disc can store more energy.
