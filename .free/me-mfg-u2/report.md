# me-mfg-u2: free-model run

- Book: `books/mech/me-mfg/me-mfg-u2.html`
- Status: ok
- Model calls so far: 24 (93,181 tokens in, 213,243 out), 6.2 minutes

## Checker

```
me-mfg-u2.html: 7 chapters, 12681 words, 8 figures, 140 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 2, plane-strain paragraph: The chapter says 'Rolling and drawing are nearly plane strain: the width cannot change'. This is true for rolling of wide strip and for strip drawing, but wire and bar drawing are axisymmetric: the diameter changes, σ2 = σ3, and yield is at σ1 − σ3 = σy, not 1.15σy. A student may wrongly apply the 1.15 factor to wire drawing.
- ch 1 [low] Section 2, plane-strain paragraph: 'Using σy instead of 1.15σy underestimates the load by 15%' is numerically loose: using σy gives 1/1.15 ≈ 0.87 of the correct load, an underestimate of about 13%, not 15%.
- ch 1 [low] Section 3, warm working paragraph: Warm working is placed between about 0.3 Tm and 0.4 Tm, but T_recryst is also about 0.4 Tm. By the chapter's own definition, deformation below T_recryst is cold working, so the warm-working range reads as a subset of cold working without explanation.
- ch 1 [low] Section 1 and figure: The power law σ = Kεⁿ gives σ = 0 at ε = 0, and the plotted cold curve starts at zero. Real metal has a yield strength at zero plastic strain, so the plot can mislead students into thinking flow stress vanishes at zero strain.
- ch 1 [low] Lead: 'Hot metal keeps softening by recrystallisation' can suggest the flow stress falls continuously. In hot working, recrystallisation removes strain hardening and keeps the flow stress roughly constant; it does not keep softening the metal.
- ch 2 [low] Figure ('One rolling pass'): The figure uses exactly the worked-example data (h₀ = 20 mm, h₁ = 15 mm, R = 300 mm, μ = 0.10) and shows a completed pass with a 5 mm draft and L = 38.7 mm. Worked example 1 proves with the same numbers that this pass is impossible (Δh = 5 mm > Δhmax = 3 mm). A student can read the figure as a pass that succeeds and then meet the example that says it fails.
- ch 2 [low] Section 1, definition of bite angle: 'The bite angle α is the angle between the entry point and the roll centre line' is vague. An angle is between two lines or planes, not between a point and a line; a student may not see which two lines to draw.
- ch 2 [low] Section 1 and formula box for L: The text calls L the 'horizontal length' of the arc, but the formula box calls it the 'contact length along the arc'. These are two different lengths (projected length R sin α against arc length Rα), even though both come to about √(RΔh) for shallow bites, so the wording contradicts itself.
- ch 3 [low] Worked example 1, step 3 and answer: The question asks for the 'average contact area', but the worked step computes the final (maximum) contact area, A₂ = 8,378 mm². A student will read 'average' as the mean of the starting and final areas and get a different number.
- ch 3 [low] Section 1, open-die operations list, fullering: 'A rounded tool spreads metal sideways' is incomplete. Fullering is a partial-penetration tool that reduces the cross-section locally and pushes metal away from that zone, both sideways and along the length.
- ch 3 [low] Lead paragraph, last sentence: 'defects to reject' reads oddly and could be misread as defects that the inspector should reject rather than defects that make the part scrap.
- ch 4 [low] Figure caption: The caption says 'only the indirect route removes sliding between billet and container wall'. Section 3 says hydrostatic extrusion has no container friction because a fluid film separates billet and container. A student reading only the caption will think hydrostatic extrusion still has direct wall friction like the direct route.
- ch 4 [low] Lead: Toothpaste tubes are listed with aluminium window sections, heat-sink fins and ladder rails as products that 'come out as one long continuous piece'. Tubes are not continuous lengths; they are single impact-extruded cups, as Section 3 itself explains.
- ch 4 [low] Quiz Q5 answer: 'volume conservation forces a long thin wall' is vague and does not say what sets thickness and what sets length, so a student may still think a longer punch stroke gives a thinner wall.
- ch 5 [high] Exam traps, second bullet: The safety check is printed as "Forgetting the safety check σd y." The inequality symbol has dropped out, so the condition is unreadable and a student cannot tell what is being compared with what.
- ch 5 [low] Section 1 (last lines) and Worked example 1: The text calls the 36% pass "heavy but safe" just after saying real mills take about 20% per pass because centre cracks grow, and the figure splits the same 5 mm to 4 mm reduction into two passes (4.5 mm then 4 mm) with an anneal in between. A student will not see why one pass is safe in the example but two passes are used in the figure.
- ch 5 [low] Section 3, third paragraph: A paragraph listing wire defects (centre burst, chevron cracking, die scratches, breakage) sits inside the tube-drawing section, which is confusing after the reader has been told the section is about tubes.
- ch 6 [low] Figure: The text says the friction estimate uses b ≈ 1.5, which with σ̄ = 350 MPa gives p = 525 ln R, but the plotted friction curve is 520 ln R (b ≈ 1.49). A student comparing text and figure sees two slightly different constants.
- ch 6 [low] Figure: 'about 1.49 times higher at every R' can be misread as 149 % higher; the ratio of the two curves is 1.49, so the pressure is 49 % higher.
- ch 6 [low] Section 2: F = σ̄wL and T = FL/2 are the simplest estimates. They leave out the friction-hill multiplier on roll pressure (typically about 1.1–1.2 in hot rolling) and the mill/transmission efficiency, so the computed force and power are lower bounds presented as exact.
- ch 6 [low] Section 2: P = 2Tω assumes both rolls are driven. If only one roll is driven the motor supplies Tω, not 2Tω. The chapter does not state this assumption, though the 'factor 2' trap depends on it.
- ch 6 [low] Section 2: 'Extrusion force is p times ram area' leaves the ram area unnamed. The ram area is the billet cross-section A₀, not the product area A_f used in R, and students mix the two.
- ch 7 [high] Lead paragraph: The example of a mixture that 'would separate in a melt' is wrong. Copper and tin dissolve completely in each other in the liquid state — cast bronze is an ordinary commercial alloy — so a copper–tin melt does not separate. A student learns a false metallurgical fact. The real P/M advantage is for combinations that are immiscible or that cannot be melted together, such as copper–graphite, copper–tungsten, silver–tungsten, or tungsten carbide with cobalt.
- ch 7 [high] Quiz Q5 answer: The oil movement is described backwards. Oil exudes out of the pores when the bush warms up (the oil expands and capillary action changes), and is drawn back into the pores when the bush cools down. Saying oil 'is drawn back' when the bearing warms contradicts the first sentence and gives the wrong mechanism, which is exactly the point being examined.
- ch 7 [low] Section 2, formula block and Section 3, first paragraph: The chapter states the sintering temperature as a fixed '0.7–0.8 Tm'. Many standard textbooks give 0.7–0.9 Tm, so the stated range is narrower than the usual one and reads as if 0.8 Tm were a hard ceiling.
