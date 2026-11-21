# ec-optical-u1: free-model run

- Book: `books/ece/ec-optical/ec-optical-u1.html`
- Status: ok
- Model calls so far: 29 (101,241 tokens in, 217,169 out), 5.1 minutes

## Checker

```
ec-optical-u1.html: 9 chapters, 15204 words, 10 figures, 160 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 2, Small size and weight bullet: A standard single-mode fiber has a 125 µm glass cladding (250 µm with coating). A human hair is roughly 50–100 µm, so the whole fiber is not thinner than a hair; only the core (about 8–10 µm single-mode, 50–62.5 µm multimode) is.
- ch 1 [low] Section 1 (wavelength windows) and Section 3: 1300 nm is described as the window 'for metro links'. In standard textbooks 1310 nm is the zero-dispersion window of standard single-mode fiber and is used for short and medium reach generally; calling it the metro window is a narrow and slightly misleading label.
- ch 1 [low] Section 2, Wide bandwidth bullet: 'Light has a very high frequency, so the fiber channel can be modulated at very high rates' is a non-sequitur as written. The usable modulation rate is set by the source, the detector and the drive electronics, not directly by the ~193 THz optical carrier.
- ch 1 [low] Section 1, last sentence ('see 1.2'): The cross-reference to total internal reflection is plain text, not a link, so a student reading on a phone cannot jump to it.
- ch 1 [low] Section 2, list of advantages: One standard advantage is missing: a fiber link has no sparks or hot metal joints, so it is safe in flammable areas such as fuel depots and chemical plants. The list also repeats the three wavelength windows already given in Section 1, which lengthens the chapter without adding anything.
- ch 2 [low] Section 2, last paragraph: The text states 'Numerical aperture is NA = sin θa', but that is only true when the outside medium is air (n0 = 1). The general definition carries n0, and later parts of the chapter (Q7, exam traps) use the general form, so the definition line is inconsistent.
- ch 2 [low] Section 3, first paragraph: 'A wider cone ... usually means a larger core and more modes' is loose. A larger NA by itself raises the mode count (V depends on NA and core radius); it does not imply a larger core.
- ch 3 [high] Section 2, third bullet: 'For a skew ray, the core–cladding incidence angle changes with rotation' is wrong. In a straight step-index fiber the ray travels in straight segments, so every reflection at the core–cladding boundary happens at the same angle of incidence; that angle is constant, not varying with rotation. What actually differs is that this constant angle is larger than for a meridional ray with the same axial slope, so total internal reflection is easier. The sentence also contradicts the Q5 answer, which says the skew ray strikes the boundary 'at a different incidence angle'.
- ch 3 [low] Quiz Q2 answer: 'NA is a ratio of refractive indices' is inaccurate: NA = √(n₁² − n₂²) is a square root of a difference of squares of indices, not a ratio. The conclusion (dimensionless) is right, but the reason given is wrong.
- ch 3 [low] Quiz Q5 answer: The answer says the incidence angle is 'different' but never says in which direction, so it does not explain why the two rays can differ in status.
- ch 4 [high] Section 3, last paragraph: It says the fibre V formula 'swaps d for 2a'. That is wrong and contradicts the chapter's own exam trap. A step-index fibre uses the core radius a: V = (2πa/λ)√(n1²−n2²). Putting 2a in place of d doubles V and roughly quadruples the mode count.
- ch 4 [low] Section 3, second paragraph: 'For a small index step, √(n1² − n2²) ≈ NA' suggests an approximation. For a step-index guide the numerical aperture is exactly √(n1² − n2²); the small-index-step approximation belongs to the other form, NA ≈ n1√(2Δ).
- ch 4 [low] Section 2, second paragraph: The cladding field is written as e^(−γ|x|), but the core runs from −d/2 to +d/2, so this expression does not join smoothly to the core field at x = ±d/2: its value there is e^(−γd/2), not 1.
- ch 4 [low] Exam traps, trap 3: The sentence 'Doubling it for TE and TM and doubling again for two polarizations overcounts' is confusing, because TE and TM are the two polarizations of a planar guide; there is no third doubling.
- ch 4 [low] Quiz Q7 and its answer: The question is ambiguous. If the fibre really has core radius 5 µm, then V = 5.90 is correct for that fibre, because the fibre V formula has the same form as the slab formula with d replaced by a. The answer still calls the V value wrong, which a student can dispute. Only the mode count is certainly wrong.
- ch 4 [low] Worked example 1, answer line: The answer says 'the guide supports 2 guided modes' without saying per polarization, while the trap section warns that TE and TM each carry this count. A student can read the two statements as contradicting each other.
- ch 5 [high] Worked example 1, steps 2 and 4: Superscripts are lost, so the shown arithmetic contradicts the answer. Step 2 reads 'NA = √(n12 − n22) = √(1.482 − 1.462) = √(2.1904 − 2.1316)', which a student reads as 1.482 − 1.462 = 0.02, not 0.0588. Step 4 reads '(29.3)2/2'.
- ch 5 [high] Section 1 (Δ exact form) and Section 3 (mode count formulas): Superscripts are lost, so the definitions are printed wrongly: 'Δ = (n12 − n22)/(2n12)' reads as n-twelve, and 'M ≈ V2/2' / 'M ≈ V2/4' read as V times 2. The quiz and exam traps use the correct ², so the chapter is internally inconsistent.
- ch 5 [low] Figure: The plotted graded-index points do not match the stated parabolic profile for n1 = 1.48, n2 = 1.46, a = 25 µm, α = 2. The formula gives n ≈ 1.477 at r = 10 µm and n ≈ 1.467 at r = 20 µm; the figure shows 1.472 and 1.464.
- ch 5 [low] Section 3: 'It counts how many half-wavelengths fit across the core at the given acceptance angle' is loose; V is a normalised frequency, not an exact half-wavelength count across the core.
- ch 5 [low] Section 1: The graded-index formula n(r) = n₁[1 − 2Δ(r/a)^α]^{1/2} gives exactly n(a) = n₂ only when Δ is the exact form. The chapter says it uses the approximate Δ unless stated, which leaves the profile slightly above n₂ at r = a.
- ch 6 [low] Section 2, cutoff wavelength paragraph: The inequality is broken: "Below cutoff, λ c, V is larger" drops the comparison sign, so the sentence has no meaning and students may misread which side of cutoff gives multimode operation.
- ch 6 [low] Section 2, last sentence on design: "λc near 1.1–1.3 µm" puts the cutoff very close to the 1.31 µm window. Practical single-mode fiber keeps cutoff comfortably below 1.31 µm so the window works with margin.
- ch 6 [low] Section 3, mode field diameter: MFD "typically 9–10 µm at 1.55 µm" is the value usually quoted for 1.31 µm; standard single-mode fiber has a slightly larger MFD at 1.55 µm.
- ch 7 [low] Section 3, 'Reading the numbers in a link': The extra delay over 10 km is stated as 'roughly 0.5 µs', which is the delay for a 1 percent index difference. The numbers quoted (n_eff = 1.46, N_g = 1.48) give a difference of about 1.4 percent, so the correct extra delay is L(N_g − n_eff)/c = 10,000 × 0.02 / (3.00 × 10^8) ≈ 0.67 µs (48.7 µs at vp versus 49.3 µs at vg), not 0.5 µs.
- ch 8 [high] Section 2, sentence 'Approximate single-mode behaviour when V Chapter 1.6.': The sentence is broken: the condition after 'V' is missing, so the student is never told the cutoff value the whole section depends on.
- ch 8 [high] Section 2, worked example step 6, exam traps item 2, quiz Q3: The cutoff used is V < 2.405, which is the single-mode limit of a step-index fibre (first zero of J0). For a slab/2D guide with the V defined here, the single-mode limit is V < π/2 ≈ 1.571 for a symmetric guide (and between π/2 and π for an asymmetric one). Using 2.405 lets a guide with, say, V = 2.0 be called single-mode when the slab is already multimode.
- ch 8 [low] Section 1 and exam trap 1: The strict split 'strip = raised, channel = buried' is convention, not standard. Many textbooks use 'channel waveguide' as the general name for any 3D guide (including ridge/strip guides), so a student reading another book will think one of them is wrong.
- ch 8 [low] Worked example 1: The example asks for NA, but the chapter body never defines NA or gives NA = √(n1² − n2²). A student meets the symbol for the first time inside a solved problem.
- ch 9 [low] Section 3: The text says the period is 'often around 500 nm for n_eff near 1.5' at 1550 nm, but 1550/(2×1.5) = 516.7 nm. The rounded 500 nm is the value that gives 1500 nm (the worked example), so a student may read a contradiction between Section 3 and Quiz Q7.
- ch 9 [low] Quiz Q6: The omnidirectional reflector is described only as reflecting 'over a wide range of incidence angles'. The standard definition is all incidence angles and both polarizations, which is what 'omnidirectional' means and why high index contrast is needed.
