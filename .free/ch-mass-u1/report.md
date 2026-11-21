# ch-mass-u1: free-model run

- Book: `books/chem/ch-mass/ch-mass-u1.html`
- Status: ok
- Model calls so far: 33 (140,468 tokens in, 317,495 out), 8.9 minutes

## Checker

```
ch-mass-u1.html: 9 chapters, 16721 words, 10 figures, 176 KB
OK
```

## For the reviewer

- chapter 1: the figure cannot be drawn: tree label "Mass transfer operations" is too long; shorten it
- chapter 6: the figure cannot be drawn: note "liquid, viscosity" runs off the right edge; shorten it
- chapter 1: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [high] Lead: The sentence 'Every separation operation in a plant is a named way of arranging that push' is false. Many plant separations are mechanical, not mass transfer: filtration, screening, centrifugation, settling of grit in a Chennai water works. A student can carry this line into an exam and call filtration a mass transfer operation.
- ch 1 [low] Section 2, drying note: The placement and the reason given are muddled. Drying a wet solid with hot air is normally put under phase creation, because heat turns the water into a vapour phase. The clause 'the solid sits still while the air leaves with the water' does not describe a solid agent, which is a solid that takes up solute (adsorption, ion exchange).
- ch 1 [low] Section 3, relation ρA = cA MA: Units are missing on a formula that ties two unit systems together, so a student cannot check the factor of 1000 that appears in the worked example.
- ch 1 [low] Exam traps, first trap: 'a flux computed with the wrong one is off by a factor of the molar mass' is loose. Mole fraction and mass fraction are both dimensionless and differ by the ratio of molar masses (times the mean molar mass), and neither can be used as a concentration in a flux formula at all.
- ch 2 [low] Section 3 and Quiz Q5: The text says eddy diffusivity falls to zero at a wall 'where the eddy size falls to zero' (Q5: 'eddy size and D_E fall to zero'). Eddies do not shrink to zero size at a wall; what vanishes is the turbulent velocity fluctuation, which damps the mixing. The sentence can make a student think the turbulent structures become infinitely small rather than being suppressed.
- ch 2 [low] Quiz Q2 answer: 'their sum is the bulk flow' is imprecise. N_A + N_B is the net (total) molar flux of the mixture, not the bulk-flow term; the bulk-flow contribution to A's flux is y_A(N_A + N_B). As written a student may think N_A + N_B and y_A(N_A + N_B) are the same quantity.
- ch 2 [low] Exam trap 4: The trap warns against 'c_A times a guessed flow', but the bulk term is exactly c_A u: y_A(N_A + N_B) = y_A c u = c_A u. The wording hides this identity and can leave a student unsure whether the bulk term is c_A u or not.
- ch 2 [low] Section 1 table: The Definition column for molar concentration just repeats the symbol c_i, so the row teaches nothing and breaks the pattern of the other rows.
- ch 3 [high] Section 1 (First law) and Quiz Q1: J_A = −D_AB dc_A/dz is presented as the general first law for molar diffusion flux relative to the molar average velocity. That form is valid only when the total molar concentration c is constant. In general the molar form is J_A = −c D_AB dy_A/dz. The text also says to use the molar-fraction form when c is nearly constant, which reverses the real limitation.
- ch 3 [low] Section 1, sentence introducing cA = c yA: cA = c yA is the definition of mole fraction for any mixture, not only an ideal mixture. The wording can make students think nonideal mixtures do not obey it.
- ch 4 [low] Section 1: The reason given for treating distillation as equimolar counter-diffusion is imprecise. That assumption rests on the two components having nearly equal molar latent heats of vaporisation (equimolar overflow), not on their boiling points being close. A student may write 'close boiling points' as the justification in an exam.
- ch 4 [low] Beyond: The stated reason for needing Maxwell-Stefan is wrong for a binary mixture. A concentrated binary mixture still needs only one pair diffusivity; the Maxwell-Stefan set becomes necessary when there are three or more components, and when strong thermodynamic non-ideality must be included.
- ch 5 [low] Lead: "liquid falls down a tube" is listed as an example of a path that widens or narrows. A falling liquid level does not change the cross-section: what changes is the length of the gas column, which is a pseudo-steady length problem, not a variable-area problem. A student may look for a varying A(z) in the Stefan tube and not find one.
- ch 5 [low] Section 2, equimolar sphere formula: "If both sides are equimolar and the two spheres have radii R₁ and R₂" is unclear. The formula is for diffusion across the shell between two concentric spherical surfaces, not between two separate spheres, and "both sides are equimolar" does not say what is equimolar.
- ch 5 [low] Section 3, Exam traps (last), Quiz Q7: The stated reason for failure is wrong: "when the gas dissolves appreciably in the liquid, because then the gas holdup is not small". Whether gas dissolves in the liquid has nothing to do with the holdup of solute in the gas phase, so the logic does not connect.
- ch 6 [high] Section 4 (prediction in liquids), last paragraph: The order-of-magnitude check mixes units and contradicts the sentence just before it. The text says both correlations return cm²/s when μ is in cP and V_A in cm³/mol, so a correct liquid answer from the correlation is about 10⁻⁵ cm²/s (that is 10⁻⁹ m²/s). The chapter then tells the student to check that the answer is 'near 10⁻⁹ m²/s' and that 'a value near 10⁻⁵ means you used a gas correlation by mistake'. A student who gets the correct 10⁻⁵ cm²/s from the correlation will read it as an error, and a genuine gas-correlation slip (about 10⁻¹ cm²/s, i.e. 10⁻⁵ m²/s) is not what the sentence describes.
- ch 6 [low] Section 3, 'Read the dependence, not just the formula': The exponent is printed as plain 'T1.75' here, while the displayed formula uses T<sup>1.75</sup>. On a phone a reader can read 'T1.75' as T times 1.75.
- ch 6 [low] Section 3, formula term list: 'the exponents 1/3 and 0.5 are applied before the square' is ambiguous and half wrong: the 0.5 exponent acts on the mass term (1/M_A + 1/M_B) and has nothing to do with the square, which acts on the sum of the cube roots.
- ch 6 [low] Section 2, closed-cell sentence: 'A closed cell with a sensor or optical window works the same way for a single liquid or a gas, without flow' does not say which relation the student would fit, so the phrase 'the same way' is left hanging.
- ch 7 [low] Lead and Exam traps (first trap): The stated solid-diffusivity range 10⁻¹⁰ to 10⁻²⁰ m²/s contradicts the chapter's own worked value of 4.41×10⁻¹⁰ m²/s at 673 K (which lies above the upper bound), and it also sits badly with the Beyond note that interstitial hydrogen moves readily near room temperature (D for H in steel is of order 10⁻⁹ m²/s). A student who memorises the range will mark the worked answer as wrong.
- ch 7 [low] Section 3, polymer films bullet: 'low D keeps food fresh' implies only D controls permeation, although the paragraph just above defines permeability as the product D·S. A low-D film with high solubility can still let a gas through fast.
- ch 7 [low] Quiz Q6: The sentence 'A packaging film and a hydrogen pipeline both use polymers or steel' reads as if both use both materials, which is confusing for a second-language reader.
- ch 7 [low] Section 1, grain-boundary bullet: 'move faster than through the grain' is loose; the comparison is with movement through the grain interior (the lattice).
- ch 8 [high] Quiz Q3: The answer says adding y_j/D_ij is adding resistances in parallel. In Wilke's formula the friction contributions add, so the resistances 1/D_ij add in series, weighted by mole fraction. A parallel-resistance analogy would give the reciprocal-sum form, not the reciprocal-weighted sum used here. This can mislead students about the physical model.
- ch 9 [low] Figure (plot spec): The plotted first-term curve runs from Fo = 0, where 1.2732·exp(0) = 1.2732, so the figure shows a centre concentration ratio of about 1.27 at Fo = 0. C/C₀ cannot exceed 1, and the text itself says the first-term formula is invalid below Fo = 0.2. A student can read the figure as saying the centre concentration rises above its starting value.
- ch 9 [low] Section 2 and Exam traps: 'Below Fo = 0.2 ... the formula is badly wrong' overstates the error just below the limit. At Fo = 0.2 the first term is within about 1% of the full series; the error is around 5% at Fo = 0.1 and only becomes large (over about 10%) near Fo = 0.05 and below. The blanket phrase can make students distrust the formula in a range where it is still acceptable.
- ch 9 [low] Section 2: 'For the middle range, use charts' is vague: middle between which two ranges is not stated, so the reader has no clear rule for when to switch from the erfc solution to the chart to the first term.
