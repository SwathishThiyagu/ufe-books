# ch-thermo-u6: free-model run

- Book: `work/wt-u6/books/chem/ch-thermo/ch-thermo-u6.html`
- Status: ok
- Model calls so far: 20 (90,103 tokens in, 207,067 out), 6.4 minutes

## Checker

```
ch-thermo-u6.html: 7 chapters, 23066 words, 8 figures, 238 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Lead: The lead says fugacity is used 'because μ has no absolute zero'. Chemical potential does have a zero on a chosen scale; what makes it awkward is the arbitrary standard-state (reference) term. A student may take the sentence literally.
- ch 1 [low] Lead: The lead states without qualification that the two phases share the same pressure. The curved-interface exception (P^α ≠ P^β) appears only later in Section 1 and in Q6, so the lead contradicts the rest for a careful reader.
- ch 1 [low] Section 2: The first derivative ln(x₁/x₂) + A(1 − 2x₁) is only correct if x₂ is treated as dependent on x₁. The text never says x₂ = 1 − x₁ before differentiating, so a student may differentiate as if x₁ and x₂ were independent.
- ch 1 [low] Section 2: 'Some syllabi call the first equality the criterion of equilibrium' is ambiguous: the 'first equality' listed earlier is T^α = T^β. A student can read it as the thermal equality.
- ch 1 [low] Section 2: The text switches from (∂²G/∂x₁²)_{T,P} to 'this expression' 1/x₁ + 1/x₂ − 2A, which is d²(g^M/RT)/dx₁². The two differ by the factor RT, so the words 'equivalently this expression > 0' mix a J/mol quantity with a dimensionless one.
- ch 1 [low] Section 2: 'The binodal is the common-tangent line' is loose: the common tangent is a construction; the binodal is the curve (locus) of the compositions of the two coexisting phases.
- ch 1 [low] Exam traps (fugacity vs fugacity coefficient): 'They differ by pressure and composition' does not say how. A student cannot tell that f_i = φ_i p_i = φ_i y_i P.
- ch 2 [high] Section 2 (reduced rule) and Exam traps, bullet 2: The letter P is used for two different things in the same breath. The formula box defines P as the number of phases, but the sentence just before it says 'Freezing P removes one variable' (P = pressure), and the trap says 'Once P is set, use F = C − P + 1', where the first P is pressure and the second P is phases. A student will read the formula as C − (pressure) + 1.
- ch 2 [low] Section 2, example of fixed-pressure equipment: 'A cylinder at its own pressure' is not a case of an externally fixed pressure. In a gas cylinder the pressure is a variable set by temperature and fill; in an LPG cylinder with liquid and vapour it is the vapour pressure, which is the phase rule at work, not the reduced rule.
- ch 2 [low] Lead: Duhem's theorem is stated as 'pick any two independent variables'. Only intensive variables count; fixing an extensive variable such as a phase amount is not the theorem.
- ch 2 [low] Section 3, binary VLE paragraph: 'P and y₁ drop out of the two equilibrium equations' reads as if they cancel. The meaning is that they are determined by the two equations; 'drop out' is ambiguous for readers with English as a second language.
- ch 2 [low] Section 3, 'Why, in one line': 'so unknowns and equations rise together' is misleading: the unknowns rise by P − 1 and the equations by C − 1, which are not equal when P ≠ C. What makes the result 2 is that the difference cancels the −P + C already in the phase rule.
- ch 2 [low] Worked example 1, step 4: 'one mole fraction (the other follows from the sum)' is confusing for a three-species gas. Knowing one species mole fraction does not give the other two from the sum alone; reaction equilibrium is also needed.
- ch 2 [low] Section 3, last sentence: The causal link is loose. Fixing T and x₁ is a Duhem statement about a closed system of fixed overall composition; a P-x-y diagram being two curves follows from the phase rule giving F = 1 once T is fixed, with no overall composition involved.
- ch 3 [low] Section 2: The sentence 'For the ideal liquid mixture used here, fiV=yiP and fiL=xiPisat' attributes both equalities to liquid ideality. The first one, fiV=yiP, is true only if the vapour is treated as an ideal gas (vapour fugacity coefficient = 1); the second, fiL=xiPisat, is true only if the liquid is an ideal solution and the Poynting correction is neglected. A student will carry away the wrong reason for each equation.
- ch 3 [low] Section 3: The lever rule uses nL and nV without defining them; every other symbol in the chapter is defined at first use.
- ch 3 [low] Quiz Q7: The answer says the lever rule 'gives no separation in composition'. At an azeotrope z1 = x1 = y1, so both (y1−z1) and (z1−x1) are zero and the lever rule gives 0/0, which is undetermined, not simply zero. The phase amounts are then fixed by the overall material balance plus the equilibrium relation, not by a tie line.
- ch 3 [low] Section 1 (Antoine equation): The formula is written with ln, but the constants printed in most handbooks and data tables are for log10 P. A student who takes a tabulated log10 set of A, B, C and substitutes it into this ln formula gets a badly wrong Psat. The unit-set warning is given; the log-base warning is not.
- ch 4 [high] Section 1 (Antoine sentence) and Exam trap 3: The chapter says to take T in kelvin in ln P_i^sat = A − B/(T + C), and the trap tells students to 'convert to kPa and K before adding terms'. Many standard Antoine tables are fitted with T in °C and P in mmHg; feeding kelvin into those constants gives a completely wrong vapour pressure. The phrase 'in whatever unit the constant A was fitted for' is also loose, because A is not in general a pressure-unit-bearing constant.
- ch 4 [low] Section 2, dew-point paragraph: The recipe says y and P are known and only x is unknown, so a student will iterate on x alone at fixed T. At fixed T and P the sum Σ y_i/(γ_i P_i^sat) does not equal 1 in general, so the loop as written cannot settle. The dew temperature, which is the real unknown here, is never mentioned, and the intermediate x_i are not normalised to sum to 1.
- ch 5 [high] Figure caption and figure aria text (also repeated idea in Section 2): The caption says the real curve 'crosses the Raoult line'. It does not. With A = 0.405 > 0 the plotted curve p₁ = x₁ exp[A(1 − x₁)²] P₁sat is larger than x₁ P₁sat for every x₁ between 0 and 1 (33.2 kPa against 30 kPa at x₁ = 0.5), so it stays above the Raoult line and only meets it at x₁ = 0 and x₁ = 1. A student looking at the figure will be confused about which curve is which and about the sign of the deviation.
- ch 5 [low] Quiz Q2 answer: The phrase 'but with the molecular environment and activity coefficient it would have at infinite dilution' suggests the standard state carries the value γi∞. That contradicts the Henry convention, where the standard state has activity coefficient 1 by definition and γi∞ = Hi/Pisat, which here would be 90/60 = 1.5, not 1. The rest of the answer is right; the middle clause muddles it.
- ch 6 [low] Section 3, flash loop (Rachford-Rice step): The loop says to solve Rachford-Rice for β between 0 and 1, but no β in (0,1) exists when every Ki is above 1 or every Ki is below 1 (single-phase feed). As written, a student can set up a two-phase flash at 40 bar for a mixture whose K values are all below 1, as in Worked example 1, and get a spurious or non-converging β.
- ch 6 [low] Section 2 and Section 3 (loop and exam traps): The phi-phi loop can converge to the trivial solution, where the EOS returns the same root for both phases, giving Ki = 1 for every component and x = y. This is a false convergence, and the chapter never tells the student to test for it.
- ch 6 [low] Section 3, bubble point and dew point sentences: The bubble point needs a vapour composition to evaluate φiV, and the dew point needs a liquid composition to evaluate φiL, but the text only says solve ΣxiKi = 1 or Σyi/Ki = 1. A student will not know what composition goes into the EOS inside the bubble/dew loop.
- ch 6 [low] Lead paragraph: Natural gas drying is usually glycol absorption, not a separation whose design rests on the phi-phi flash described here; listing it next to gas separation and absorption is loose.
- ch 7 [low] Section 3 and Quiz Q7: The sentence 'The only free intensive variable is one' is garbled and a student may not follow what F = 1 means here.
- ch 7 [low] Section 2: 'The tie lines shrink to a point called the plait point' can be read as if the plait point were a separate location where tie lines meet; strictly, tie lines shorten to zero length at the plait point, which is a point on the binodal where the two liquid phases become identical.
- ch 7 [low] Section 2 (KD definition): KD is defined here as a mole-fraction ratio, but in extraction practice KD is usually a concentration or mass-fraction ratio. Students may mix the two bases without being told.
- ch 7 [low] Section 1: The equation's validity range and the standard state of γ₁ are not stated: it applies for T below Tm, and γ₁ is relative to pure (supercooled) liquid 1 at the same T and P.
