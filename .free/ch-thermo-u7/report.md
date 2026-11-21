# ch-thermo-u7: free-model run

- Book: `work/wt-u7/books/chem/ch-thermo/ch-thermo-u7.html`
- Status: ok
- Model calls so far: 26 (102,285 tokens in, 234,861 out), 7.7 minutes

## Checker

```
ch-thermo-u7.html: 8 chapters, 21256 words, 9 figures, 230 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 1, sentence after the ΣνᵢAᵢ = 0 formula: The sentence 'If species i is consumed, νᵢ  0, so its moles rise' has lost its inequality signs and its logic is broken: a consumed species has negative νᵢ and its moles must fall, not rise. As printed, a student reads a contradiction of the sign convention just defined.
- ch 1 [low] Section 3, conversion formula: The formula Xᵢ = −νᵢξ/nᵢ₀ is written in the section on several independent reactions, but it holds only for a single reaction. With r reactions the change in moles of i is Σⱼνᵢⱼξⱼ, so a student applying this formula to the two-reaction case will get the wrong conversion.
- ch 1 [low] Section 2, paragraph on the range of ξ: Only forward reaction is described (ξ starts at 0 and grows). A reaction written in one direction can run backwards, in which case ξ is negative and products are consumed; the stated bounds do not say this.
- ch 2 [high] Section 3, Duhem's theorem paragraph: It says that fixing T and P fixes the composition 'though not the total amount of each phase'. This contradicts Duhem's theorem, which states that for a closed system made from specified initial amounts, fixing two independent intensive variables fixes the complete equilibrium state, including the amounts of each phase. The sentence also contradicts the sentence just before it.
- ch 2 [low] Section 2, third paragraph: 'If ΔGr r > 0, the reverse reaction proceeds' contains a typo ('ΔGr r'). The paragraph also gives only the positive and zero cases and never states the negative case, so the list of directions reads as incomplete.
- ch 2 [low] Section 1 and Section 3 formula boxes: The symbol P means pressure (bar) in Section 1 and number of phases in Section 3. A student reading the phase-rule box after the earlier boxes can take P for pressure.
- ch 2 [low] Section 1, definition of chemical potential: 'The chemical potential is the Gibbs energy per mole of that species at the actual mixture composition' is loose. In a mixture the chemical potential is the partial molar Gibbs energy, not simply G/n for the pure species.
- ch 2 [low] Section 2, second paragraph: The text says a zero first derivative could be a maximum, but for a closed system at fixed T and P the plain minimum is the stable state; the wording 'could also be a maximum' with only the second-derivative test is fine, but a stationary point that is neither a maximum nor a minimum (an inflection) is not mentioned, so 'a zero first derivative alone could also be a maximum' reads as the only alternative.
- ch 3 [low] Lead: The sentence 'The standard Gibbs energy change removes the composition part and leaves a number fixed by temperature, the equilibrium constant K' can be read as saying ΔG° is the same thing as K, which is not true; ΔG° is a Gibbs energy in J mol⁻¹ and K is a dimensionless number obtained from it.
- ch 3 [low] Section 2, gas activity sentence: 'fᵢ° is standard fugacity (equal to P° for ideal gas)' suggests the standard fugacity equals P° only for an ideal gas. With the ideal-gas standard state, fᵢ° = P° = 1 bar for every gas, real or ideal; the real gas enters through φᵢ.
- ch 3 [low] Section 3, concentration form (formula line): The exponent is not marked as a superscript: 'K = (RT/P°)Σν Kc' and 'Kc = Π cᵢνᵢ' read as if Σν and νᵢ multiply the brackets instead of being powers. Earlier formulas in the same section use superscripts, so the reader sees inconsistent notation.
- ch 3 [low] Quiz Q2 answer: The answer says 'Each gas activity is pᵢ/P°', which holds only for ideal gases; the chapter itself defines aᵢ = fᵢ/fᵢ° for gases in general, and the question does not restrict to ideal gases.
- ch 4 [low] Section 1: The sentence 'Differentiating with respect to T at constant pressure removes the direct part and leaves the standard enthalpy' is too vague; a student cannot see how the derivative of ln K gives ΔH°.
- ch 4 [low] Section 1: 'The derivative is local: it gives the slope of ln K at one temperature' does not say slope against which variable, so it can be confused with the slope of the ln K versus 1/T plot.
- ch 4 [low] Quiz Q1: The answer defines the symbols but does not give the units of ΔH° or the value and units of R, so a student cannot use the equation numerically.
- ch 4 [low] Quiz Q6: The answer says a straight line in ln K versus 1/T follows from constant ΔH° alone, but the intercept also requires ΔS° to be constant, i.e. ΔCp° ≈ 0.
- ch 5 [low] Section 3, third paragraph ('The γi depend on xi, so K is nonlinear in ξ'): K is a constant fixed by temperature and standard-state Gibbs energies, as the lead and Section 1 state. It cannot be nonlinear in ξ. What is nonlinear is the equilibrium relation (the equation that must be solved for ξ) once γi depend on composition. A student can read this as saying K itself changes with extent of reaction.
- ch 5 [low] Section 2 ('Solve, then back-substitute to check Q = K') and the figure caption: The reaction quotient Q is used in Section 2, Section 3 and the figure without being defined anywhere in the chapter, although every other symbol is defined.
- ch 5 [low] Section 2, second paragraph ('for A ⇌ 2B, nT = 1 + ξ, not 1'): The value nT = 1 + ξ holds only for a feed of 1 mol pure A. Stated before the feed basis is given, it looks like a general result for A ⇌ 2B.
- ch 6 [high] Worked example 1, answer line: The answer line is garbled and states the wrong direction. It reads "Q(0.10) = 0.0404  K so backward", which a student can read as: at ξ = 0.10 the reaction goes backward. Steps 5 and 6 correctly say forward at ξ = 0.10 and backward at ξ = 0.30, so the summary contradicts the worked steps and drops the second comparison.
- ch 6 [low] Exam traps, third trap: "Calling Q at equilibrium Q" is confusing, and the explanation "Q is the current-composition quotient before equilibrium" is not strictly right: Q can be written for any composition, including the equilibrium one, where it happens to equal K.
- ch 6 [low] Section 3, yield note: The symbol νD appears without definition in "divide by νDnL0", though earlier the generic νi was defined.
- ch 7 [low] Section 1, sentence after the K_y rearrangement: "the mixture moves toward reactants to restore K_y to the value set by K" is misleading. At the new pressure the required K_y is a new, lower value; it is not restored to the old one. A student can read this as saying K_y returns to its earlier value.
- ch 7 [low] Section 2, last sentence: "the effect is different" is vague and suggests the inert still does something to the equilibrium at fixed T and V. In the ideal-gas model it does nothing: the reacting partial pressures are unchanged and the composition does not shift (as Quiz Q6 correctly says). The two statements look contradictory.
- ch 8 [high] Section 3, the paragraph applying the reacting phase rule to steam reforming: The species in the two steam-reforming reactions are CH₄, H₂O, CO, CO₂ and H₂ — five species, not six. With N = 6 the numbers give F = 6 − 1 + 2 − 2 = 5, but the true count is N = 5, so F = 4. The sentence that follows ('fixing T, P and the feed element ratios fixes the composition') only works with F = 4, since T and P plus two element ratios (C:H:O has two independent ratios) is four variables. The section also contradicts Quiz Q6, which correctly gives N = 5 and F = 4.
- ch 8 [high] Quiz Q6, answer: The sentence 'Species present: CH₄, H₂O, CO, CO₂, H₂, so N = 5 plus the four elements — the species set gives N = 5' contradicts itself and states a wrong element count. There are three elements here (C, H, O), not four, and elements are never added to N — N counts chemical species only.
- ch 8 [low] Quiz Q4, answer: The answer writes x_A = x_B = (1 − x) and x_C = x_D = x, but x_i are mole fractions while x is the extent in mol. With 1 mol each of A and B fed, the total stays at 2 mol, so the mole fractions are (1 − x)/2 and x/2, not (1 − x) and x. The final K expression is right only because the factor 2 cancels.
- ch 8 [low] Section 3, sentence on counting independent reactions: 'The count r is what remains after species are eliminated with atom balances' is too vague for a student applying it to a new feed; it does not say how the elimination is done.
- ch 8 [low] Section 1, opening of the second paragraph: 'At 100–300 bar, as in ammonia or methanol synthesis' is loose for methanol: modern low-pressure methanol synthesis runs near 50–100 bar, not 100–300 bar.
