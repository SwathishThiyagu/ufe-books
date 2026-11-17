# me-fluid-u4: free-model run

- Book: `books/mech/me-fluid/me-fluid-u4.html`
- Status: ok
- Model calls so far: 30 (125,349 tokens in, 233,634 out), 7.4 minutes

## Checker

```
me-fluid-u4.html: 8 chapters, 14777 words, 9 figures, 155 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Lead: 'Re tells you which regime to expect before you open the valve' is misleading: Re needs the mean velocity V, and V is set by the valve opening (or by the design discharge). Before the valve is set you do not have V.
- ch 1 [low] Section 1: The apparatus list leaves out the bell-mouth (trumpet-shaped) entrance and the stilling arrangements (honeycomb/screens, settling time) that keep inlet disturbances low. Without them the dye line breaks up early and the lower critical Re falls well below 2000, which is exactly why the chapter later says the switch is not sharp.
- ch 1 [low] Section 3: 'The velocity profile is a paraboloid' can confuse a student into thinking of a 3-D surface; the exam point is the parabolic variation of u with radius, u = u_max(1 − r²/R²).
- ch 2 [high] Exam traps, first bullet: The direction of the error is stated backwards. Putting D in place of R in u(r) = Δp(R² − r²)/(4μL) gives a centreline value ΔpD²/(4μL) = 4ΔpR²/(4μL), which is four times the true umax, not four times too small. A student who trusts this line will mis-remember which way the mistake goes.
- ch 3 [high] Quiz Q6, answer: The last sentence says that using f = 0.02 at low flow overestimates hf. In laminar flow the true factor is f = 64/Re, which is larger than 0.02 whenever Re < 2000 (for example f = 0.032 at Re = 2000, and bigger at lower Re). Holding f at 0.02 therefore gives a head loss smaller than the real one, so the estimate is low, not high.
- ch 3 [low] Section 3, first paragraph: The unit of the Chezy coefficient is written as 'm1/2/s', which a student can read as 'metres per 2 seconds' or 'm1 divided by 2 divided by s'. The half power is missing.
- ch 3 [low] Section 2, explicit approximation: The exponent is typed with a caret ('Re^0.9') while the rest of the chapter uses Unicode superscripts; on a phone the caret term can be misread as part of the denominator.
- ch 3 [low] Section 2, after the Colebrook-White equation: 'Solve it by iteration, or read 4.4' does not say what 4.4 is and has no chapter link, so a student revising on a phone cannot jump there.
- ch 4 [high] Worked example 1, problem statement and step 1: The stated Reynolds number does not match the stated velocity and diameter for water. Re = VD/ν = 1.5 × 0.2 / 1×10⁻⁶ = 3×10⁵, not 1×10⁵, and the book itself uses ν = 1×10⁻⁶ m²/s for water in quiz Q6. A student who checks Re with the formula from Section 3 gets a different number, and a different friction factor (about 0.024 instead of 0.025).
- ch 4 [high] Worked example 1, step 3: The Haaland check value is wrong. With the chapter's own Haaland form, ε/D = 0.002 and Re = 1×10⁵ give (0.002/3.7)^1.11 = 2.37×10⁻⁴, 6.9/10⁵ = 6.9×10⁻⁵, sum = 3.06×10⁻⁴, log₁₀ = −3.514, 1/√f = 6.325, f = 0.0250. The value 0.0246 is not produced by Haaland, nor by Colebrook-White (which gives 0.0251) at these conditions.
- ch 4 [low] Section 3, reading steps: The step says 'Confirm the read value with the Haaland approximation', but the first formula shown after it is the implicit Colebrook-White equation, with the Haaland equation only after that. The order contradicts the instruction and a student may think the first formula is the Haaland one.
- ch 4 [low] Figure caption: The caption says both curves flatten at high Re. Only the ε/D = 0.002 curve flattens (0.02348 at Re = 10⁷, still falling slowly). The smooth-pipe curve keeps falling over the whole range, from 0.0661 at Re = 10³ to 0.00813 at Re = 10⁷, because it has no roughness to reach a constant f.
- ch 4 [low] Figure: The plotted range starts at log₁₀ Re = 3, but the Haaland correlation drawn is a turbulent-flow fit and is not valid below Re ≈ 4000. The left part of the plot therefore shows a turbulent curve in the laminar and critical zones, where the text says the chart is a single straight line f = 64/Re.
- ch 5 [high] Quiz Q4: The arithmetic is right but the ratio is mislabelled. 0.204 m against a major loss of 1.019 m is about 20% of the major loss; 17% is the share of the total loss (0.204/1.223). A student copying '17% of major' learns a wrong ratio.
- ch 5 [low] Section 3: The 5–10% figure for L/D above about 1000 is not generally true and contradicts the chapter's own numbers. Minor/major = ΣK/(fL/D). With ΣK = 5.8 and f = 0.03 (the worked example), L/D = 1000 gives about 19%, not 5–10%.
- ch 5 [low] Exam traps, fourth bullet: 'Convert D to metres before dividing by 0.05 m' is confusing: 0.05 m is this example's diameter, not a general step, and L/D and KD/f are two different divisions.
- ch 6 [low] Section 2, first sentence: "Both lines fall in the direction of flow when there is no pump" is stated as an absolute rule, but the very next paragraph says the HGL can rise in a diffuser. A student reading the first line will mark the second statement as wrong.
- ch 6 [low] Exam traps, first trap: "It must be at least one velocity head above the HGL" is loose. The gap is exactly V²/(2g) at a section, not a minimum.
- ch 6 [low] Lead: "Every friction length" is unclear; a student may read it as a special term.
- ch 7 [low] Section 3, third paragraph: The minor-loss formula hm = K(V²/2g) uses K without defining it, and the equivalent length Le = KD/f does not say that D and f must be those of the pipe the loss is being charged to. A reader meeting K for the first time cannot tell whether it is dimensionless or what it multiplies.
- ch 7 [low] Section 2, first paragraph: 'Both see the same pressure difference, so the head loss from A to B is the same' skips a step: the head loss is equal because the pressure difference and the elevation difference between the same two nodes are equal for both branches. As written, a student may think equal pressure difference alone gives equal head loss, which is false when the two ends are at different levels.
- ch 7 [low] Section 2, last sentence: HGL and TEL are used without being expanded anywhere in the chapter. Readers who meet these abbreviations for the first time will not know what lines are being referred to.
- ch 7 [low] Worked example 1, step 5: The unit of the sum is written 'm-1/2', which reads as 'metres minus one half' rather than an inverse square root. Since 1/√L has units of m⁻¹/², the line is easy to misread and the unit check at the end of the chapter is weakened.
- ch 8 [high] Exam traps, bullet 1, and Quiz Q7: The slow-closure surge is given as Δp ≈ ρLV/Tc. For gradual closure (Tc > 2L/a) with a roughly linear velocity change, the standard textbook result is Δp ≈ 2ρLV/Tc (equivalent to ΔH = 2LV/(gTc)); it matches the Joukowsky rise ρaV exactly at Tc = 2L/a and then falls off as 1/Tc. The value ρLV/Tc is the rigid-column estimate and is only half the standard result, so the Q7 answer 0.83 MPa (said to be 'about one third' of 2.47 MPa) is wrong by a factor of two.
- ch 8 [low] Section 3, sentence after the crest-pressure formula: 'Every term on the right is subtracted' is not true: the atmospheric term patm/ρg is added, not subtracted. A student may misread the formula.
- ch 8 [low] Quiz Q6: Q6 repeats Worked Example 2 with the same numbers (6.0 m crest, 1.5 m/s, 0.8 m loss, 33.5 kPa), so it adds no new practice.
- ch 8 [low] Section 2, Joukowsky equation: Only the pressure form Δp = ρaV is given. Most exams ask for the surge head as well, and the worked example converts to head afterwards without stating the shortcut.
