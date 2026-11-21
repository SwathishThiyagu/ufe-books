# ch-mass-u2: free-model run

- Book: `books/chem/ch-mass/ch-mass-u2.html`
- Status: ok
- Model calls so far: 34 (150,894 tokens in, 322,379 out), 7.9 minutes

## Checker

```
ch-mass-u2.html: 9 chapters, 15530 words, 10 figures, 171 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Quiz Q4: Wrong magnitude and unit by a factor of 1000. kG = kc/RT with kc = 0.02 m/s and RT = 0.0246 m³·atm/mol gives (m/s)/(m³·atm/mol) = mol/(m²·s·atm), so kG = 0.81 mol/(m²·s·atm), not 0.81 kmol/(m²·s·atm). The stated unit reasoning is also garbled: "mol/m³ divided by m³·atm/mol is mol/(m³·atm)" is not a valid unit operation, and no kmol appears anywhere in the data.
- ch 1 [low] Section 1, sentence after the formula ("It is the volume of fluid cleared..."): The two 'per' clauses read as m/s per (mol/m³), which is not the unit of kc and can confuse a student. kc already is the flux divided by the concentration difference; it equals a volume per unit area per second only when the concentration difference is unity.
- ch 1 [low] Section 3, the four-item list (By position / By phase / By combination / By driving force): The list starts with no lead-in sentence, so it hangs unexplained, and the 'By phase' and 'By driving force' lines partly repeat each other (kc and kL both sit on concentration).
- ch 2 [low] Section 3 and Quiz Q4: Section 3 sets a rule that a film controls only when its share is above about 80%. Quiz Q4 then says the liquid film 'now controls' when its share is 65.2%, which contradicts the rule the student was just given.
- ch 2 [low] Figure: The figure gives bulk compositions y = 0.10 and x = 0.02, but the worked example never states any bulk compositions, so the student cannot tell where these numbers come from or check them.
- ch 2 [low] Beyond: HTU is used without being defined anywhere in the chapter.
- ch 3 [high] exam traps, trap 3 (also relates to section 2, turbulent flat-plate correlation): The trap claims Sh = 0.037 Re^0.8 Sc^(1/3) 'already averages a plate that starts laminar at the leading edge'. Standard texts treat this fit as turbulent flow from the leading edge; the mixed laminar-then-turbulent plate is described by Sh = (0.037 Re^0.8 − 871) Sc^(1/3). At the lower end of the stated range (Re = 5×10⁵) the two differ by about a factor of three, so a student who follows the trap will report a badly wrong Sh and k_c.
- ch 3 [low] figure: The laminar curve is drawn to Re = 10⁶ although the text says it holds below about 5×10⁵, and the turbulent curve is drawn from Re = 10⁴ although the text says it holds from about 5×10⁵ to 10⁷. The plot therefore shows exactly the extrapolation the section warns against, and a student may read off values outside the fitted bands.
- ch 3 [low] section 3, sentence on Sc values: 'Gas diffusivities give Sc near 0.6 to 1' is too narrow. Gases span roughly 0.2 (hydrogen or helium in air) to about 3; 0.6 to 1 covers only common pairs such as water vapour in air.
- ch 3 [low] section 2, sentence after the sphere formula: 'All three are empirical fits to the same boundary-layer problem' is not accurate. The two flat-plate fits come from boundary-layer theory on a plate; the sphere fit (Ranz–Marshall type) is an empirical correlation for a completely different geometry, which is why it has the additive term 2.
- ch 3 [low] section 1, first sentence: 'Convection adds to diffusion, so the flux is written N_A = k_c Δc' suggests the flux is a sum of two separate contributions. N_A = k_c Δc is a definition of the coefficient, and mixing raises k_c by steepening the near-wall concentration gradient; the 'so' will confuse a reader meeting this for the first time.
- ch 4 [low] Lead, sentence 'The three pictures give different dependence on diffusivity D (m²/s)': The lead says the three theories give different dependence on D, but penetration and surface renewal both give k_c ∝ √D. Only two distinct dependences exist.
- ch 4 [low] Figure, notes for Surface renewal and Penetration: The notes give k values without units, while the Film note includes 'm/s'. This is inconsistent and may confuse students about units.
- ch 4 [low] Beyond, last sentence: The cross-reference 'Chapter 2.9' is plain text, not an anchor link. The formatting rules require cross-references to other chapters to be links.
- ch 5 [high] Section 2, steps for estimating kc from pressure drop: The steps use the same symbol L, defined as the pipe length over which Δp is measured, as the characteristic length in Re = ρuL/μ, in Sh, and in kc = Sh DAB/L. For pipe flow Re and Sh must be based on the pipe diameter D, not the length. Using L = pipe length gives an absurdly large Re and a wrong kc.
- ch 5 [low] Section 3, last paragraph: The sentence warns that strong blowing or suction breaks jD = f/2, then points to 'Chapter 2.9 for reaction-enhanced transfer'. The pointer does not match the point being made, so a student looks for the wrong topic.
- ch 5 [low] Section 2 and quiz Q3, Q5; worked example steps 2–3: Exponents appear as plain digits: 'Pr1/3', 'Sc1/3', '0.61/3', which read like multiplication by 1/3 or 1/3 itself.
- ch 5 [low] Section 3, first paragraph: A gas with Sc about 0.6 is given as an example of Sc 'far from 1'. 0.6 is typical for gases and is close to 1, so it is a poor example of the case where the Reynolds analogy fails badly.
- ch 5 [low] Lead: The lead offers 'estimate evaporation from a duct using its fan power' as a use case, but fan power comes from the whole system pressure drop, which includes form drag; Section 3 itself says form drag makes the predicted kc too high. The example works against the chapter's own warning.
- ch 6 [low] Section 1 and Section 2 formula notes: The coefficient units are written as kmol/(m²·s·Δy) and kmol/(m²·s·Δx). Δy and Δx are not units; the film coefficient is simply kmol/(m²·s) per unit mole-fraction difference, and mole fractions are dimensionless. A careful student can be confused about whether Δy is a unit or a quantity.
- ch 6 [low] Section 3, second paragraph: The coefficients are quoted as 'ky = 0.05 and kx = 0.08' with no units, while the worked example gives units. The reader cannot tell the basis of these numbers from this paragraph alone.
- ch 6 [low] Exam traps, fourth bullet: 'The interface lies between the bulk point and the equilibrium line' is misleading. In the figure the interface point is on the equilibrium line, and the line from the bulk point to the interface meets the equilibrium line exactly at the interface. A student may look for an interface point off the equilibrium line, between the two.
- ch 7 [low] Section 1 (overall efficiency paragraph): The line "Eo is usually less than EM because it also includes entrainment, weeping and flow maldistribution" is too strong and is not what the standard texts say. Eo and EM measure different things, so Eo can be above or below EM; in distillation Eo often exceeds EM because the equilibrium curve and operating line are not parallel, while entrainment and weeping push it down. The claim also contradicts quiz Q5 in the same chapter, where Eo = 0.70 is greater than EM = 0.50.
- ch 7 [low] Quiz Q5 answer: The answer lists entrainment, weeping and maldistribution, which all lower efficiency, so it does not actually explain how the column value (0.70) can be higher than the tray value (0.50).
- ch 7 [low] Quiz Q7 answer: "24" is a lost superscript; read literally, 24 − 2 = 22 and 24 − 1 = 23, but the next step jumps to 16. A student will stumble here.
- ch 7 [low] Quiz Q6 answer: "How much liquid flow is available relative to the minimum set by equilibrium" is vague and does not say what the factor actually compares.
- ch 8 [high] Section 2, NTU integral: The sign statement is reversed. Since y* > y in absorption, the integrand 1/(y* − y) is positive, and dy is positive only when you move from the lower yout up to the higher yin. Integrating from the higher yin down to the lower yout makes dy negative and gives a negative NTU, which contradicts the exam trap that says reversing the limits changes the sign.
- ch 8 [low] Section 1, tray spacing sentence: 0.3 m to 0.6 m is a narrow range that reads like the whole practical range. Standard design allows spacing from about 0.15 m in small columns up to 0.9 m in large ones, with 0.45–0.6 m the usual choice.
- ch 8 [low] Figure: The diagram is titled 'Stage or packed height', but the tray branch stops at the HETP block and never shows a tray-section height, so only the packed route reaches a Z. A student may read it as saying HETP is itself the tray height.
- ch 9 [high] Exam traps, second bullet (Unit slips): The factor is wrong. 1 cm²/s = 10⁻⁴ m²/s, and Ha takes the square root of D_A, so entering D_A in cm²/s instead of m²/s makes Ha 100 times too big (or 100 times too small if k_L is entered in cm/s), not 10 times.
- ch 9 [low] Section 3, CO₂/MEA paragraph: The tower height falls by the factor E only when the liquid film controls the overall rate. If the gas film carries most of the resistance, the same E in the liquid hardly changes the overall coefficient or the HTU, and a student will expect a ten-fold shorter tower in every case.
- ch 9 [low] Figure: The 'slow reaction' curve 1 − 1.5x + 0.5x² has slope −1.5 at x = 0, so it draws an enhancement factor of 1.5. The table and caption call this case slow with E ≈ 1, so the picture contradicts the text.
- ch 9 [low] Section 2, table: The table jumps from fast pseudo-first-order to instantaneous without saying when the pseudo-first-order result stops being valid. E ≈ Ha holds only while Ha is well below E∞; near Ha ≈ E∞ the reaction plane forms and E levels off at E∞ even though k is large.
