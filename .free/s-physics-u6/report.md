# s-physics-u6: free-model run

- Book: `books/common/s-physics/s-physics-u6.html`
- Status: ok
- Model calls so far: 29 (122,113 tokens in, 248,157 out), 5.7 minutes

## Checker

```
s-physics-u6.html: 9 chapters, 16861 words, 10 figures, 176 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 2, closing paragraph: "The name marks the short-wavelength end of the spectrum; the divergence appears even earlier, in the far ultraviolet and X-rays." The word "earlier" is ambiguous (earlier in wavelength? earlier in time?) and reads as if the divergence happens somewhere other than at short λ. A student can take it to mean the Rayleigh-Jeans formula stops diverging beyond the ultraviolet.
- ch 1 [low] Section 3, first paragraph and Planck formula, plus quiz Q8 answer: The exponent is not marked up in running text: "hν ÷ (ehν/kT − 1)", "ehν/kT ≈ 1 + hν/kT" and "hν e−hν/kT" read as e times hν/kT, not e raised to the power hν/kT. On a phone this is the most misread line in the chapter. The displayed formula uses <sup> correctly; the prose and the quiz answer do not.
- ch 1 [low] Section 3, Planck's radiation law formula note: The symbol I was defined in Section 1 as power per unit area per unit wavelength (W·m⁻² per m), and the prefactor 2πhc²/λ⁵ is correct for that quantity. The note then calls I "spectral radiance per unit wavelength". Radiance is power per unit area per unit solid angle per unit wavelength, and for radiance the prefactor is 2hc²/λ⁵, without the π. A student who compares with a textbook that uses B_λ will find a factor π that is not explained.
- ch 2 [high] Section 2 (determination from the V0 against ν plot): V0 = (h/e)ν − φ/e, so the intercept on the V0 axis is negative: −φ/e. The chapter says the intercept is φ/e, contradicting its own earlier statement that the Kmax against ν line has y-intercept −φ. A student who writes 'intercept = φ/e' loses the sign mark.
- ch 2 [low] Exam traps, item 2: 'or Kmax is wrong by a factor of 1.60 × 10⁻¹⁹' misdescribes the mistake. If you subtract an eV number from a joule number you do not get a scaled Kmax; you get a meaningless value, because the work-function term alone is off by the factor 1.60 × 10⁻¹⁹.
- ch 3 [low] Lead: The phrase 'a particle with fixed energy and momentum' can mislead a student into thinking every photon has the same energy. A photon's energy and momentum depend on its frequency/wavelength.
- ch 3 [low] Lead: Spelling is inconsistent: 'wave length' appears once, while the rest of the chapter writes 'wavelength'.
- ch 3 [low] Section 1: 'the wave whose intensity gives the probability of finding the particle' is loose. The intensity gives the probability density (probability per unit volume), not the probability itself.
- ch 3 [low] Section 2: The step from p = √(2meV) to λ = h/√(2meV) is called 'Planck's relation'. Planck's relation is E = hν; the wavelength step is the de Broglie relation.
- ch 3 [low] Section 2: 'use relativistic momentum from Unit 1' is a vague pointer, and a student revising this chapter alone cannot look it up.
- ch 3 [low] Exam trap 2: The sentence 'energy eV is in joules when e = 1.60 × 10⁻¹⁹ C' is confusing: eV is the symbol for the electron-volt unit as well as charge times voltage.
- ch 3 [low] Quiz Q4: The reason given is compressed. Fringe spacing w = λD/d halves, but the deeper reason wave effects become hard to see is that λ becomes small compared with the slit separation and slit width, so the diffraction angles shrink.
- ch 4 [low] Section 3 and the velocity table: The text defines ω = E/ℏ with E called 'the total energy', then states that non-relativistically vp = E/p = v/2. That value only follows if E is the kinetic energy p²/2m; a total energy that includes the rest energy mc² gives vp ≈ c²/v even at low speed. A student cannot reconcile the two statements.
- ch 4 [low] Worked example 1, step 6: The 3% gap (48.55° calculated against 50° observed) is blamed on d being a rounded value. The accepted plane spacing for nickel (111) planes is 2.03 Å, and using a more precise value does not remove the gap, so the stated reason is wrong.
- ch 5 [low] Section 2, slit estimate: The chapter computes Δx Δp ≈ h and then calls it 'of the order of ℏ'. h is 2π times ℏ, about 6.3ℏ, so the product is consistent with the bound but is not numerically of order ℏ; a student may think the two constants are interchangeable.
- ch 5 [low] Section 3, natural linewidth: Using ΔE ≥ ℏ/(2τ) gives Δν ≈ 1/(4πτ) = 8 MHz for τ = 10 ns. Many textbooks define the natural linewidth as the full width at half maximum of the Lorentzian, Γ = ℏ/τ, i.e. Δν = 1/(2πτ) ≈ 16 MHz. A student comparing with another book sees a factor of 2.
- ch 5 [low] Figure, edge slit → diffraction spread: The edge label 'narrows' reads as if the diffraction spread is narrowed, which is the opposite of the figure's message (a narrow slit widens the spread).
- ch 6 [high] Quiz Q2: The answer gives a wrong reason. Interference comes from adding two amplitudes before squaring, and real amplitudes interfere perfectly well (that is how classical sound and water waves make fringes, and two real wavefunctions with opposite signs also cancel). Probabilities are always real and non-negative and never interfere; saying 'a purely real positive probability could not produce interference fringes' confuses probability with amplitude and teaches a false rule.
- ch 6 [low] Section 3, list of acceptable wavefunctions: The list (finite, single-valued, continuous, continuous first derivative) leaves out the square-integrability requirement, which is the one that actually makes normalisation possible. A student could think a bounded but non-normalisable function such as a constant is acceptable.
- ch 6 [low] Section 1: 'the average energy using the Schrödinger equation' is vague; the average energy comes from the Hamiltonian operator, not from the equation itself.
- ch 6 [low] Figure caption: The caption calls |ψ|² the 'lower' curve, but both curves reach the same peak value 1 at x = 0 in the plotted functions, so |ψ|² is not lower at the centre, only narrower and lower away from it.
- ch 6 [low] Section 3: The phase factor is written as e^{iφ}, which is LaTeX-style notation; this book uses plain Unicode for formulas.
- ch 7 [high] Figure (flow diagram 'From TDSE to steady state'): The arrow from 'Separate' to 'TI equation' is labelled 'time part'. The time part gives the phase factor φ(t) = e^(−iEt/ℏ); it is the space part that yields Ĥψ = Eψ. As drawn, the diagram teaches the reverse of what the text says.
- ch 7 [low] Section 3, free-particle formula and its symbol list: The text introduces ψ(x) = A e^(ikx) + B e^(−ikx) and then lists 'A and B are the amplitudes of the right-going and left-going waves', but the displayed boxed formula contains only the A term ψ(x, t) = A e^(i(kx − ωt)). A reader hunting for B in the formula finds nothing.
- ch 8 [low] Section 2, nodes paragraph: The sentence 'The probability density ... has n humps, so a highly excited particle is almost equally likely anywhere in the box' reads as if |ψn|² itself becomes flat for large n. It does not: |ψn|² still swings between 0 and 2/L at any n. Only the average over a small range of x becomes uniform, which is the classical limit.
- ch 8 [low] Section 2, zero-point energy paragraph: Taking Δx of order L with Δp ≥ ℏ/2L and then identifying the result with E1 = h²/(8mL²) does not match numerically. Putting Δp = ℏ/2L into Δp²/2m gives ℏ²/(8mL²) = h²/(32π²mL²), about 40 times smaller than h²/(8mL²), so a student who follows the numbers gets a different answer from the quoted E1.
- ch 9 [high] Worked example 1, step 7 (and Section 2, prefactor remark): Step 7 claims that because κa = 2.56 the dropped prefactor 'cannot change the answer much'. For these numbers the prefactor is not near one: 16E(V − E)/V² = 16 × 1.0 × 1.0 / 2.0² = 4. So the fuller formula gives T ≈ 4 × 5.98 × 10⁻³ ≈ 2.4 %, four times the quoted 0.60 %. κa = 2.56 is only moderately large, and E = V/2 is exactly the case where this prefactor is at its maximum.
- ch 9 [low] Exam traps, bullet 2: The size of the error is wrong for κ. Feeding eV numbers into the square root instead of joules makes κ too large by about a factor 2.5 × 10⁹ (10¹⁹ is the error in the squared quantity 2m(V − E), not in κ).
- ch 9 [low] Section 2, sentence giving the fuller formula: 'The exact thick-barrier answer' contradicts itself: the formula is the leading thick-barrier approximation, not an exact result. There is no exact point; the expression omits the next term in e^(−2κa).
- ch 9 [low] Worked example 1, step 3: √(2m(V − E)) is called 'the momentum the electron would need inside the barrier', which suggests the electron has kinetic energy V − E there. It does not; inside the barrier the momentum is imaginary and this quantity is its magnitude, ℏκ.
- ch 9 [low] Quiz Q3, question wording: The phrase 'An electron with E − V relations as in the worked example' is garbled and gives no energy values, so the question cannot be answered on its own.
- ch 9 [low] Exam traps, last bullet: 'Perfect transmission needs E ≫ V' is not strictly true. For E > V a single rectangular barrier also gives T = 1 at isolated energies where the width holds a whole number of half-wavelengths (transmission resonances).
