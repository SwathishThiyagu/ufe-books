# s-chem-u2: free-model run

- Book: `books/common/s-chem/s-chem-u2.html`
- Status: ok
- Model calls so far: 22 (80,356 tokens in, 203,431 out), 4.5 minutes

## Checker

```
s-chem-u2.html: 9 chapters, 14330 words, 10 figures, 168 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 2, paragraph beginning 'Intensity is different from photon energy': 'Intensity counts photons per second per unit area' is the definition of photon flux, not intensity. Standard textbooks define intensity as power (energy per second) per unit area, in W m⁻². A student can lose a mark writing the chapter's version in an exam.
- ch 1 [low] Section 2, selection rules paragraph: The harmonic-oscillator rule is written Δv = ±1, but the letter v here is the vibrational quantum number while ν (nu) has just been used for frequency throughout the chapter. On a phone screen the two look alike and students mix them up.
- ch 1 [low] Section 3, first paragraph: 'An absorption spectrum is a plot of radiation missing after passing through a sample' is vague; it suggests plotting an absolute amount of lost radiation rather than the fraction absorbed against frequency or wavelength.
- ch 2 [low] Section 1: The constant k in dI/I = −k dl is never defined, and the step from I = I₀e^(−kl) to I = I₀ × 10^(−εcl) skips the conversion between the natural-exponential constant and the base-10 absorptivity.
- ch 2 [low] Lead vs Section 1: The lead says ε is fixed by 'the substance, wavelength and solvent', but Section 1 correctly adds temperature. A student may think temperature does not matter.
- ch 2 [low] Section 3: 'If A is too high, dilute and multiply c back' does not say what to multiply by.
- ch 2 [low] Section 3, first paragraph: 'Work below about 0.01 M' reads as a universal limit; the usable concentration range depends on the substance's ε and on the instrument.
- ch 2 [low] Section 2: c_unknown = A_unknown/slope is right only if the axis units are used; the figure plots c in units of 10⁻⁵ M, so the slope 0.12 gives c in 10⁻⁵ M, which a student may misread as mol L⁻¹.
- ch 3 [high] Section 3, paragraph beginning 'A UV-visible spectrum...': 'A weak band is not a weak concentration; it is a less allowed transition' is wrong as written. Absorbance A = εcl, so a weak band can be caused by low concentration or a short path length. The transition probability is measured by ε, not by the raw band height.
- ch 3 [low] Lead: 'the height tells you how likely the jump is' — the height (absorbance) also depends on concentration and path length. It is not a direct measure of transition probability.
- ch 3 [low] Section 3, paragraph 'Allowed means...': 'π→π* is allowed and strong' is an overgeneralization. Some π→π* transitions are symmetry-forbidden and weak, for example benzene's band near 254 nm with ε about 200.
- ch 3 [low] Section 1, last paragraph: 'absorbs 400-500 nm removes blue-green light' is imprecise. 400-435 nm is violet, not blue-green; the complementary colour of the whole band ranges from yellow-green to red.
- ch 3 [low] Section 2, auxochrome paragraph: 'does not absorb by itself in the useful UV range' is not strictly true: -OH, -NH₂ and -Cl have n→σ* absorptions below about 250 nm, which lie in the UV range.
- ch 4 [low] Section 2, first paragraph: The claim that bending bands are 'usually ... weaker' is not reliable. Several bending modes give strong bands, for example the out-of-plane aromatic C–H bends near 700–900 cm⁻¹, which are used to identify substitution patterns.
- ch 4 [low] Section 2, overall (title is 'modes of vibration'): The chapter never counts the vibrational modes of a molecule. Students meet questions such as 'how many vibrational modes does CO₂ or H₂O have?' and the counting rule is not given.
- ch 4 [low] Figure (HCl spectrum): HCl gas also shows rotational fine structure (P and R branches) around the fundamental, so a single sharp dip is a low-resolution sketch, not the real gas-phase spectrum.
- ch 5 [low] Section 2, selection rule sentence: The chapter says a molecule absorbs a microwave photon 'only when ΔJ = ±1'. This states the quantum-number rule but never states the other necessary condition: the molecule must have a permanent electric dipole moment. A student can wrongly conclude that N₂ or O₂, which have no dipole moment, give a microwave rotational spectrum.
- ch 5 [low] Section 1, rigid rotor description: 'The bond does not bend or stretch' is loose. A diatomic molecule has no bending motion at all; the only vibration it can have is stretching. Saying the bond does not bend can confuse students who later meet bending modes in polyatomics.
- ch 5 [low] Figure caption: 'The gap between neighbouring levels grows with J, so successive absorption lines sit 2B apart' joins two facts with 'so', but the growing gap does not cause the equal spacing. A student may think the spacing grows too.
- ch 6 [low] Section 4, instrument paragraph: The wording 'the solvent gives its own weak signal, not the analyte' suggests the deuterated solvent itself appears in the ¹H spectrum. A student may think CDCl₃ or D₂O gives a proton peak. The weak peak actually comes from a little residual protonated solvent (for example CHCl₃ left in CDCl₃, seen near 7.26 ppm); the deuterium itself resonates far away and is used for the lock, not seen in the ¹H window.
- ch 6 [low] Worked example 1, Section 3 formula box and Figure: The numbers are arithmetically correct, but J = 40 Hz for a proton–proton coupling is far larger than real ¹H–¹H couplings, which are typically 0–20 Hz (often 6–8 Hz for a three-bond coupling). Students may carry away a wrong feel for typical J values, and a 0.1 ppm doublet looks unrealistically wide.
- ch 6 [low] Quiz Q4: The answer writes δ = 800/200 = 4.0 ppm, mixing Hz and MHz without showing the 10⁶ factor. A student copying this cannot see why the units work out to ppm.
- ch 6 [low] Section 3, n + 1 rule: The rule is stated without its condition. It fails when the coupled protons are close in shift (J comparable to Δν) or magnetically non-equivalent, giving second-order patterns such as multiplets with more than n + 1 lines.
- ch 6 [low] Figure: The plot runs from 0 to 10 ppm left to right, while printed NMR spectra follow the convention that δ increases towards the left (downfield on the left, TMS at the right). A student comparing the figure with a real spectrum may be confused.
- ch 7 [high] Section 1: The text says to add nuclear repulsion to get the electronic energy U(R). Adding nuclear repulsion to the electronic energy gives the total (adiabatic) potential energy for nuclear motion, not the electronic energy.
- ch 7 [low] Section 3 and Quiz Q4: The statement that the transition probability is proportional only to the square of the vibrational overlap omits the electronic transition dipole moment. It holds for an allowed electronic transition when that moment is nearly constant over the relevant R.
- ch 7 [low] Section 1: The product is called the full molecular wavefunction, but χ_nuc is defined only as the vibrational part. The rotational nuclear part is omitted.
- ch 7 [low] Figure: The caption says absorption is a vertical jump, but the plot specification contains only the two potential-energy curves and no vertical transition line or arrow. The axes also have no units.
- ch 8 [low] Section 1, primary act: The photon energy hν is used but h and ν are never defined, so a student cannot tell what the symbols mean.
- ch 8 [low] Section 1, Iₐ = I₀ − Iₜ: The relation is said to need only negligible reflection, but scattering by the sample or cell also removes light that the sample did not absorb, so Iₐ would be overestimated.
- ch 8 [low] Section 2 formula and Section 3 formula / worked example: The amount of substance is written N in Section 2 and in Section 3's formula but n in the worked example and steps; N (a count) and n (moles) are different symbols and the switch can confuse students.
- ch 8 [low] Section 3, 'Same cell, same wavelength, same path length': The sentence implies that cell, wavelength and path length alone make the absorbed fraction comparable. The absorbed fraction actually depends on the absorbance, A = εcl, so a dilute actinometer and a concentrated sample in the same cell absorb very different fractions.
- ch 8 [low] Figure, absorption node note: The note reads 'I absorbed', which does not match the symbol Iₐ used everywhere else in the text.
- ch 9 [low] Section 1, singlet/triplet sentence: 'Exchange repulsion is smaller' is not the standard wording and can confuse. The triplet is lower because the exchange interaction keeps the two unpaired electrons apart, so their electrostatic repulsion is smaller than in the singlet, where the electrons come closer together.
- ch 9 [low] Section 3, first line: 'Emission always has lower energy than absorption' is too strong. The emission maximum is at lower energy, but the emission and absorption bands overlap near the 0–0 transition, so part of the emission lies at higher energy than the absorption maximum.
- ch 9 [low] Worked example 1: The step numbers are doubled: 'step 1: 1. Convert ...', 'step 2: 2. Convert ...'. Reads like a formatting slip.
- ch 9 [low] Quiz Q4: The question asks for the dominant route, but the answer names two. The largest single rate constant is k_ISC = 5.0×10⁸ s⁻¹ (half the total); internal conversion is second at 4.0×10⁸ s⁻¹.
