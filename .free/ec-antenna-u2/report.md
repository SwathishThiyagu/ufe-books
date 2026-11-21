# ec-antenna-u2: free-model run

- Book: `books/ece/ec-antenna/ec-antenna-u2.html`
- Status: ok
- Model calls so far: 32 (140,419 tokens in, 281,533 out), 7.3 minutes

## Checker

```
ec-antenna-u2.html: 8 chapters, 14812 words, 9 figures, 155 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Quiz Q5: With l = 2 cm at f = 3 GHz, λ = 0.1 m so l = 0.2λ. That is not 'much shorter than a wavelength', so the element is not a Hertzian dipole and the far-field formula used gives a wrong value. For a uniform-current element of this length the broadside pattern factor sin(βl/2)/(βl/2) is 0.935, so the true field is about 1.41 V/m, not 1.51 V/m; and R_r would not be 80π²(l/λ)² = 31.6 Ω either.
- ch 1 [low] Worked example 1, step 3: The label says 'For a short dipole', but 80π²(l/λ)² is the radiation resistance of an infinitesimal (Hertzian) dipole carrying a uniform current. A short dipole with the usual triangular current has R_r = 20π²(l/λ)², four times smaller. A student may carry the wrong formula to the other case.
- ch 1 [low] Section 1, second sentence of the first paragraph: The sentence 'Switch the current off and the field collapses back; no field escapes to infinity' is misleading. Switching a current off means decelerating charge, and a sudden switch-off launches a travelling transient; that is exactly how a spark-gap transmitter radiates. Only a current that is steady or changing slowly enough leaves no radiated field.
- ch 2 [low] Lead: The phrase 'gain adds the antenna's losses' is misleading: gain is reduced by losses, not increased by them.
- ch 2 [low] Section 1: The main lobe is described as a direction, but it is a lobe region; side lobes are also all lobes other than the main lobe, not only those near it.
- ch 2 [low] Section 3: The estimate D ≈ 41253/(θE θH) uses θE and θH without defining them as the half-power beamwidths in the E-plane and H-plane.
- ch 3 [high] Section 1, the short-dipole formula, and Worked example 1 steps 2 and 4: The chapter says a short dipole's current falls to zero at the tips, then quotes Rr = 80π²(l/λ)². That value assumes a uniform (constant) current along the dipole. For a real short dipole with the triangular current distribution the chapter itself describes, referred to the current maximum, the value is Rr = 20π²(l/λ)² — one quarter of what is quoted. The table entries (8 Ω at λ/10, 0.32 Ω at λ/50) and the worked example results all rest on the unstated uniform-current assumption, so a student cannot tell which convention applies.
- ch 3 [low] Lead paragraph: The lead says "An antenna has three numbers that decide how well it works", but the chapter treats four quantities: radiation resistance, efficiency, effective aperture and polarization.
- ch 3 [low] Section 3, the half-wave dipole at 300 MHz: "The metal itself is a few centimetres across" invites the wrong picture: a half-wave dipole at 300 MHz is about 0.5 m long, tip to tip. Only its wire thickness is a few millimetres.
- ch 3 [low] Exam traps, third bullet (peak versus rms current): "This gives a factor-of-two error in both Rr and efficiency" is not right for efficiency. A factor of two in Rr gives an efficiency error that depends on RL — with true Rr = 2 Ω and RL = 1 Ω, the wrong Rr = 1 Ω gives η = 0.5 instead of 0.667, not a factor of two.
- ch 3 [low] Section 2, "at l = λ/50 the same 0.5 Ω takes almost everything": "Almost everything" overstates it on the chapter's own numbers: 0.32 Ω against 0.5 Ω gives ηrad ≈ 0.39, so about 61 per cent is lost, not almost all.
- ch 3 [low] Figure caption: "Radiation resistance grows as the square of electrical length" is only true in the very-short-dipole region; the λ/2 dipole at 73 Ω in the same table does not lie on that square-law curve, so the caption contradicts its own data.
- ch 4 [low] Section 1, paragraph after the reactive near-field formula: "energy sloshes back and forth ... and none of it escapes" and the lead's "fields that never leave" read as if no radiation leaves the antenna in the reactive near field. The 1/r radiating term is present there too, just dominated by the stored 1/r² and 1/r³ terms; a short dipole does radiate, only weakly.
- ch 4 [low] Section 1, paragraph after the reactive near-field formula: "E/H ... can be several hundred ohms for a short dipole" understates the value and clashes with the exam trap, which says it can be "far above 377 Ω". Very close to a short dipole |E/H| is thousands of ohms, not a few hundred.
- ch 4 [low] Figure caption and Section 1 table row for the far field: The figure says "The far field begins at r = 2D²/λ" with no small-antenna caveat, while Section 3 states the start is max(2D²/λ, 1.6λ) and also needs r ≫ D, r ≫ λ. A student revising from the figure alone gets an incomplete rule.
- ch 5 [high] Quiz Q7 (and its answer): The premise and the physics are wrong. A lossy ground plane adds loss resistance, so the measured feed resistance goes up, not down. A small plane gives an imperfect image, which makes the structure behave more like the full dipole, again pushing the resistance up toward 73 Ω. The answer's line 'Both change the current distribution and lower the measured resistance' is the opposite of what both stated causes do.
- ch 5 [low] Section 4, folded dipole paragraph: 'The feed current runs up one wire and back along the other, so both wires carry the same current I_in, in phase' reads as a contradiction: running up one wire and back along the other sounds like opposite directions, yet the sentence then says in phase. A student may conclude the two fields should cancel.
- ch 5 [low] Section 2, last sentence: 'Carry 73 Ω, 1.64 and 78° into any link budget' is misdirected: a link budget uses the gain (2.15 dBi) and, for coverage, the beamwidth. The 73 Ω is a matching quantity and does not appear in a link budget.
- ch 6 [high] Exam traps, third bullet: The sign is wrong. Substituting the diameter d = 2a into A = πa² gives A = πd² = 4πa², which is four times the true area, so R_r comes out sixteen times too large, not too small. As written, a student who makes this slip is told the opposite of what actually happens.
- ch 6 [low] Section 3, ferrite rod paragraph: "Raises radiation resistance by μ_eff² and raises the received voltage in the same way" reads as if the voltage also rises by μ_eff². R_r goes as A², so it rises by μ_eff²; the open-circuit received voltage goes as the effective area, so it rises only by μ_eff. The two factors are different.
- ch 6 [low] Section 3, first paragraph: "Even a λ/10 loop would be tens of metres across" overstates the size. At 1.6 MHz, λ/10 is 19 m of circumference, about 6 m across; only at the bottom of the band does the diameter reach roughly 18 m.
- ch 6 [low] Section 2, circumference formula: A = C²/(4π) holds only for a circle, so the C-only formula is for a single-turn circular loop. The text says just "for a single turn", which invites its use for square or rectangular loops.
- ch 7 [high] Section 2, effective length: The chapter states 'For a short dipole of physical length l much less than λ, leff = l'. For the standard short dipole (l << λ, triangular current falling linearly to zero at the ends) the effective length is l/2, not l. Using l gives a factor-of-two error in the induced voltage. leff = l is true only for the ideal Hertzian dipole with uniform current along its length.
- ch 7 [low] Section 3 (reciprocity two-way test) and the figure: The claim that driving A with current I and then B with the same current gives 'received power P₁ again' holds only if the two antennas are identical (equal radiation resistance) and the same load is used both times. With two different antennas the received powers differ by the ratio of the radiation resistances, even though Z12 = Z21. Similarly, 'the field at distance r is the same in both directions' is only true when the two antennas are the same.
- ch 8 [low] Section 1, first paragraph: The text says 'Put an isotropic source at the transmitter', but the very next sentence writes S = P_t G_t/(4πd²), which is the density for a directive antenna. A student may wonder where G_t came from if the source is isotropic.
- ch 8 [low] Section 3, last bullet, and figure caption: The bullet says doubling frequency adds 6.02 dB 'as the figure shows', but the figure compares 2.4 GHz with 5 GHz. The ratio is 5/2.4 = 2.08, so the gap is 20 log₁₀(2.08) = 6.4 dB, not 6.02 dB. The aria text also says 'about 6 dB', disagreeing with the caption's 6.4 dB.
- ch 8 [low] Lead: Saying a radar 'is checked this way' is loose: Friis is a one-way link equation, while radar uses the two-way radar range equation (Friis applied out and back with target RCS). A student may think Friis alone sizes a radar.
