# s-physics-u5: free-model run

- Book: `books/common/s-physics/s-physics-u5.html`
- Status: ok
- Model calls so far: 28 (90,693 tokens in, 198,158 out), 4.7 minutes

## Checker

```
s-physics-u5.html: 9 chapters, 13497 words, 10 figures, 162 KB
OK
```

## For the reviewer

- chapter 6: the figure cannot be drawn: note "barcode, CD" runs off the right edge; shorten it
- chapter 6: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [low] Section 1, absorption bullet: The absorption rate is said to be proportional to 'the light energy density', but Section 2 uses u(ν), the energy density per unit frequency at the transition frequency ν, in the rate B12N1u(ν). A student may take 'energy density' as the total (per unit volume) energy density and be confused why the units of B look strange.
- ch 1 [low] Section 2: The unit of A21 is given (s⁻¹) but the units of B12 and B21 are never given, although the rate equation and the A/B relation both need them. A student also cannot check why B2₁u(ν) comes out in s⁻¹.
- ch 1 [low] Section 3: The chain 'One photon can create two, two can create four, and so on. That is amplification by stimulated emission' is stated without the condition that makes it true. With more atoms in E1 than E2 the same photons are absorbed and the light is attenuated, not amplified; population inversion is only mentioned later.
- ch 1 [low] Figure: The figure shows absorption lifting the atom from E1 to E2, but neither emission path shows the atom coming back down to E1. The node 'Spontaneous' also reads as a photon rather than a process, so the picture does not make clear that one photon leaves in a random direction and the atom returns to E1.
- ch 2 [high] Exam traps, first bullet: The bullet mixes two different thresholds. High cavity loss or fast non-radiative decay does not stop population inversion from building up in the medium; high cavity loss only prevents the round-trip gain condition R₁R₂exp[2(g−α)L] ≥ 1 from being met, so lasing (oscillation) never starts. A student will wrongly conclude that cavity loss controls population inversion.
- ch 2 [low] Section 1, paragraph 3: It says absorption and stimulated emission are proportional to N₁ and N₂ 'with the same Einstein B coefficient'. The two B coefficients are equal only when the degeneracies are equal; in general g₁B₁₂ = g₂B₂₁. The statement sits uneasily with the degeneracy condition given two sentences later.
- ch 2 [low] Section 4, closing sentence: 'These four properties are independent' is wrong for brightness and contradicts quiz Q8: brightness depends directly on divergence (solid angle) and beam area, so poor directionality means low brightness.
- ch 3 [low] Section 2, fourth bullet: "and helium returns to ground at the tube walls" is placed where the reader expects the step that empties the neon lower level. What keeps the inversion going is that the neon 1s level (the state left after 2p decays) is emptied at the walls; helium metastables are also quenched there, but that is a separate point. As written a student may think helium's wall loss is what clears the lower laser level.
- ch 3 [low] Section 2, opening paragraph: "Helium does the absorbing" is loose: helium does not absorb light in this laser. It takes energy from electron collisions in the discharge. The next bullet says this, but the opening sentence can mislead.
- ch 3 [low] Exam traps, point 1: "it never runs continuously" is too absolute. Ruby is a pulsed laser in every practical and textbook use, but it has been made to lase continuously under special conditions. The safe exam statement is about how it is normally operated.
- ch 4 [low] Section 1, CO2 paragraph: The sentence says 10.6 μm is absorbed by many non-metals, then lists steel, which is a metal, in the same 'so it cuts ...' clause. A student may read it as claiming steel absorbs 10.6 μm strongly, which is not the reason CO2 lasers cut steel (they cut it with a reactive gas assist).
- ch 4 [low] Section 1, Nd:YAG paragraph, last sentence: 'The gas tube can be long' appears at the end of the Nd:YAG paragraph but talks about the CO2 gas tube. As placed, it reads as if it describes YAG.
- ch 5 [high] Section 3, last paragraph: The claim about divergence is inverted. A semiconductor laser's emitting facet is only a few micrometres across, and a small aperture gives large diffraction spread, so the beam diverges by roughly 10°–30° and is elliptical. The cavity acts on the longitudinal modes (narrow spectrum), not on the beam spread.
- ch 5 [low] Section 2, paragraph on population inversion: 'More electrons sit in conduction-band states than in valence-band states at the same energy' is loose: conduction-band and valence-band states are separated by the band gap and do not lie at the same energy, so a student can misread the condition.
- ch 5 [low] Section 3, paragraph 'A GaAs laser at 873 nm is used...': 873 nm is the wavelength computed from the GaAs band gap; the named consumer products do not work at that wavelength. CD players use about 780 nm, barcode scanners usually 650–680 nm, so the sentence misleads on numbers.
- ch 6 [low] Lead and Section 1: The lead says a laser is chosen by 'four numbers', but coherence is not a number. A student may look for a single coherence value, while it is coherence length or coherence time that is quantified.
- ch 6 [low] Section 1: The definition 'Coherence is how fixed the phase relation is across the beam' covers only spatial coherence. Interferometry and holography in this chapter depend on temporal coherence, that is, a narrow linewidth keeping a fixed phase relation over a path difference.
- ch 6 [low] Section 1: 'Wavelength is the colour or infrared line' is loose. Wavelength also covers ultraviolet lines such as the 193 nm excimer, so the sentence narrows the idea wrongly.
- ch 6 [low] Figure caption: The claim that communication and measurement share a branch 'because both depend on coherence' overstates the case. A directly modulated fibre link works with a narrow-line, bright source; coherence is essential for measurement (interference), not the main reason for a fibre source.
- ch 7 [high] Exam traps, bullet 1: The trap says that swapping the indices gives 'an angle above 90°' when n1 > n2. This is not what happens. For n1 > n2 the ratio n1/n2 is greater than 1, and the sine of an angle can never exceed 1, so sin⁻¹(n1/n2) is undefined. There is no angle above 90° at all. A student will take away a wrong idea about the inverse sine.
- ch 7 [low] Section 2, derivation of NA in the running text: The superscripts are lost in the inline working: 'n1√(1 − (n2/n1)2)' and '√(n12 − n22)' read as n twelve and n twenty-two on a phone screen. Every other formula in the chapter uses <sup>.
- ch 8 [low] Section 2, last paragraph: The sentence 'V < 2.405 is still the single-mode test' is stated without qualification for graded-index profiles. The 2.405 cutoff is the LP11 cutoff of a step-index profile; for a power-law graded core the cutoff is higher, V_c ≈ 2.405√(1 + 2/g), which is about 3.4 for a parabolic profile (g = 2). A student could apply 2.405 to a graded-index fibre and wrongly call a fibre single-mode.
- ch 8 [low] Section 2, first line: 'Core size sets the mode count' is incomplete. The mode count is set by V, which depends on core radius, numerical aperture and wavelength together; changing λ changes M at fixed core size.
- ch 8 [low] Section 2, end of first paragraph: The cross-reference 'Attenuation and link design are in 5.9' is plain text; the reader cannot jump to that chapter on a phone.
- ch 9 [low] Section 1 and Quiz Q1: The chapter uses 'attenuation' for two different quantities. Section 1 says 'The loss is called attenuation' (a total loss in dB), but the formula and Q1 define attenuation as loss per unit length in dB/km. A student can lose marks by mixing total loss with attenuation coefficient.
- ch 9 [low] Section 1, first paragraph: It says a pulse loses power 'for two reasons' but then names three: absorption, scattering and bending.
- ch 9 [low] Quiz Q6: 'A laser launches narrow, coherent light that couples well into a small single-mode core' gives the wrong reason for good coupling. Coherence does not set coupling; the laser's narrow beam divergence and small emitting area do. Coherence and narrow spectral width matter for low chromatic dispersion.
