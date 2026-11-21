# ch-thermo-u4: free-model run

- Book: `books/chem/ch-thermo/ch-thermo-u4.html`
- Status: ok
- Model calls so far: 24 (86,457 tokens in, 193,425 out), 5.2 minutes

## Checker

```
ch-thermo-u4.html: 8 chapters, 12723 words, 9 figures, 140 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Lead and Section 1: The lead says the subtraction of TS leaves "the part that can become work". For G at constant pressure the usable part is only the non-PV (useful) work; total work including PΔV belongs to A. A student can read the lead and think −ΔG is the total work.
- ch 1 [low] Section 3, last paragraph, and Exam trap 5: ΔA = ΔU − TΔS and ΔG = ΔH − TΔS are written without saying they hold only when the temperature is constant. At constant T they are correct; in general the relation is ΔA = ΔU − Δ(TS).
- ch 1 [low] Section 1: The chapter never states plainly that A and G are state functions and extensive, so they add up over phases and scale with the amount of material. Students meeting ΔG of reaction mixtures later need this.
- ch 1 [low] Quiz Q1 answer: "Both have units of J, or J/mol per mole" is garbled wording; "J/mol per mole" means nothing.
- ch 1 [low] Section 2 (Gibbs-Helmholtz formula block) and Beyond: The Gibbs-Helmholtz equation is dropped in with no derivation or use, then the Beyond box tells the student to "search next for Gibbs-Helmholtz equation" as if it were new. Quiz Q8 tests it, so the treatment is thin for a 3-mark question.
- ch 2 [low] Section 3: The entropy equations are written for one mole, but the units given for the heat capacities do not match: CV is called J/K and CP is called J/K, while R is J mol⁻¹ K⁻¹ and the equation dS = CV dT/T + R dV/V only works when S, CV and V are all per mole. The same mix-up carries into the worked example, where V is in m³ mol⁻¹.
- ch 2 [low] Quiz Q6: The answer ties the sign of S to the phase being 'stable'. Entropy is positive for any condensed or gaseous phase at ordinary temperature (third law reference), so stability is not the reason; a student may wrongly conclude an unstable phase has negative entropy or a positive slope.
- ch 3 [high] Quiz Q6 (question text and answer): The text is broken and unreadable. The question reads 'A real gas has T(∂V/∂T)P JT, and does expansion warm or cool the gas?' with the comparison symbol and the value of μJT missing, so the student cannot tell what is given. The answer is also broken: 'so μJT JT dP > 0' has lost the inequality and the dT step.
- ch 3 [low] Section 1, closing sentences after the four relations: The claim 'The left side contains entropy in the denominator or numerator. The right side contains only P, V, T and their slopes' is wrong for two of the four relations: in the dU relation (∂T/∂V)S = −(∂P/∂S)V and the dH relation (∂T/∂P)S = (∂V/∂S)P, entropy sits in the denominator on the right side, and on the left side entropy only appears as the held-constant subscript.
- ch 3 [low] Section 3, first paragraph: 'Dropping the subscript changes the number and the units' is misleading. Changing the held-constant variable changes the value, but the units usually stay the same: (∂V/∂T)P and (∂V/∂T)S are both in m³/K.
- ch 3 [low] Exam traps, second bullet: The example '(∂V/∂T)V' is a poor illustration: at constant V there is no volume change, so that derivative is simply zero, which does not show the point being made.
- ch 4 [high] Section 1, definition at fixed T and P: The sentence 'A real gas approaches ideal behaviour as P → 0, so M^R → 0 at low pressure' is false for M = V. V^R = (Z − 1)RT/P tends to the finite second virial coefficient B as P → 0, not to zero; V and V^ig both diverge and their difference remains finite.
- ch 4 [high] Section 2, residual Gibbs energy and fugacity: The statement 'At P → 0, Z → 1, so the integrand approaches zero' is wrong. The integrand in ∫₀^P (Z − 1)dP/P is (Z − 1)/P. With Z = 1 + B′P + …, it tends to the finite value B′, not zero. The integral is finite because the integrand has a finite limit.
- ch 4 [high] Section 2 after the integral; Exam traps third bullet: The comparison sign is missing in 'If φ  1, G^R is positive' and in 'φ  1 gives positive G^R'. As written the sentence is incomplete and can teach the wrong sign.
- ch 4 [high] Quiz Q4 answer: The answer says that subtracting only volumes 'would not vanish for an ideal gas'. That is false: V − V^ig is exactly zero for an ideal gas. The real reason V − V^ig alone is not used is that it is not the correct integrand for H^R; it ignores the T(∂V/∂T)_P term coming from dS at constant T.
- ch 5 [high] Exam traps, first bullet: The trap says that using hg instead of hfg at 10 bar and x = 0.90 gives a value 'about 201 kJ/kg too high'. The 201 kJ/kg figure belongs to a different mistake: taking h = hg (the saturated-vapour value) as the mixture enthalpy, error 2778.1 − 2576.6 = 201.5. If a student really substitutes hg into the mixture formula, h = hf + x·hg = 762.8 + 0.90 × 2778.1 = 3263.1 kJ/kg, which is 3263.1 − 2576.6 = 686.5 kJ/kg too high, not 201. The headline and the number describe two different errors, so a student cannot tell which mistake is being warned against.
- ch 5 [low] Section 2, interpolation formula: The symbol x is already defined in Section 1 as quality, a mass fraction between 0 and 1. The interpolation formula reuses x for the known independent variable (T, P or h), so 'x' carries two meanings on the same page and a student may read quality into the interpolation arithmetic.
- ch 5 [low] Quiz Q2 answer: 'Using hg would count the liquid part twice' is loose. Using hg in h = hf + x·hg adds exactly x·hf extra, not the whole liquid enthalpy again; the phrase could be read as saying hf itself is doubled.
- ch 6 [high] Section 1, the sentence beginning 'For ice melting ΔV': The sentence is broken: 'For ice melting ΔV Chapter 4.3).' Words, the sign of ΔV, the conclusion about the slope, and the opening parenthesis of the chapter link are all missing. A student cannot read what the chapter concludes for melting, and the broken line looks like a printing fault.
- ch 6 [low] Figure: The declared y range is 10 to 13, but the plotted line reaches ln(P/Pa) = 9.966 at 1/T = 0.003, so the end of the line falls outside the box and is clipped.
- ch 6 [low] Exam traps, first bullet: 'Gives a wrong sign or size' is loose. Using Celsius in this temperature range keeps the sign of (1/T2 − 1/T1) and of ln(P2/P1) the same; the real damage is a badly wrong magnitude. A sign flip needs negative Celsius values, which is a special case.
- ch 7 [low] Section 1: "So Cp is always larger than Cv" is too strong and contradicts Q4 of this chapter. When α = 0 the two are equal — water at about 4 °C is the standard example — so the difference is never negative but can be zero.
- ch 7 [low] Lead: "Cp − Cv is the extra heat a substance needs" misses the per-kelvin part; the difference of two heat capacities is extra heat per unit temperature rise, not extra heat.
- ch 7 [low] Lead: The lead says the same PVT derivatives (α and κ_T) give how Cp and Cv change with pressure and volume. Those slopes come from second derivatives of v or P, not from α and κ_T themselves, so the sentence misleads a student into expecting α and κ_T to be enough.
- ch 7 [low] Figure: Both inputs from the α, κ_T node are labelled "divide", but in Tvα²/κ_T the coefficient α is squared and multiplied; only κ_T is divided.
- ch 7 [low] Section 2: The Gibbs-Helmholtz sentence appears with no link to Cp or Cv and is not used again; a student cannot see why it is here.
- ch 8 [high] figure (node 'jac'): The figure rewrites the target (∂S/∂V) at constant T as the Jacobian ratio J(S,V)/J(T,V). That ratio is not the target: with the held-constant variable T, the correct ratio is J(S,T)/J(V,T). As printed, a student would copy the wrong ratio into the worked example and get −(∂S/∂T)V instead of (∂P/∂T)V, and the stated result of the figure would not follow.
- ch 8 [low] exam traps, second trap (sign of a swap): 'Reversing the order and keeping the sign flips the answer' is ambiguous: reversing the order is exactly what flips the sign, so 'keeping the sign' after a reversal is the mistake that makes the answer wrong. A student can read it either way.
- ch 8 [low] section 1, first sentence: 'the determinant of their first derivatives' is loose; the Jacobian is the determinant of the 2×2 matrix of first partial derivatives, which is what the formula that follows actually shows.
