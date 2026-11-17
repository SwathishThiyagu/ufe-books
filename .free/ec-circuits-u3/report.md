# ec-circuits-u3: free-model run

- Book: `books/ece/ec-circuits/ec-circuits-u3.html`
- Status: ok
- Model calls so far: 25 (108,434 tokens in, 227,890 out), 5.4 minutes

## Checker

```
ec-circuits-u3.html: 8 chapters, 14834 words, 9 figures, 161 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 1, formula and text: The text says φ is 'in radians or degrees', but inside the expression ωt + φ the term ωt is in radians, so φ must be converted to radians before adding. A student may plug in 30 (degrees) directly and get a wrong instantaneous value.
- ch 1 [low] Section 2, definition of average value: 'Area under the curve divided by the interval length' does not say the area is signed. Taken literally, a student computes the unsigned area of a full sine and gets 0.637Vm instead of 0.
- ch 1 [low] Section 3, power formula: The symbol φ is reused in P = Vrms Irms cos φ, but here it means the phase difference between voltage and current, not the phase of v(t) defined in Section 1. This is not stated.
- ch 2 [high] Section 3: Phasor diagrams and lead/lag: The lead/lag sentence reads 'If φv − φi v − φi = +90°', which is garbled and leaves out the element being described. A student cannot tell whether this refers to an inductor or capacitor.
- ch 3 [low] Exam traps, third bullet (forgetting the quadrant): The trap says tan⁻¹ "loses the sign". It does not: arctan keeps the sign of X/R, and the chapter's own formula θ = tan⁻¹(X/R) correctly gave −72.6° in Worked example 1. What arctan really cannot do is tell a + jb from −a − jb, i.e. fix the quadrant when R is negative or when the ratio was formed from two complex numbers. As written, a student is told to distrust the formula the chapter just used.
- ch 4 [high] Section 2, paragraph 'The sign of θ tells you the story': The sentence breaks off: 'If X series resonance belongs to Unit 4.' The whole capacitive half of the sign rule is lost (X < 0 → capacitive, current leads) and the sentence is unreadable as printed. A student reading this never learns the rule that the worked example, Q4 and Q7 all depend on.
- ch 4 [low] Exam traps, last bullet: 'Check the sign: X  0 means inductive, current lags.' The comparison sign is missing, so the one-line reminder is broken.
- ch 4 [low] Section 1, fourth bullet and the figure caption: The general conversion rule is written with a cosine, i(t) = √2|I| cos(ωt + ψ), but the source in the worked example is a sine and the answer is written as a sine. A student who applies the stated rule to the example gets a waveform 90° away from the printed answer.
- ch 4 [low] Worked example 1, step 11: The squaring is slightly off: 212.5² = 45156, not 45176. The final 230.0 V is still right, so only the intermediate number is wrong.
- ch 4 [low] Section 3, Laplace check paragraph: The final value theorem does not guarantee this: it needs all poles of sF(s) in the left half plane, and a sinusoid's poles sit on the jω axis, so the limit has no final value in the theorem's sense. The conclusion is right, but the stated reason is not.
- ch 5 [high] Section 1, last sentence: It says the whole double-frequency component is the exchange with stored energy. That is false: p(t)=P(1−cos2ωt)−Q sin2ωt. The cos2ωt part is pulsation of real power and exists even in a pure resistor, where no energy is stored. A student will misunderstand why p(t) goes negative.
- ch 5 [low] Section 2, first paragraph: It calls reactive power 'the energy traded'. Q is power (rate of energy exchange), not energy; the unit is VAR, not joule. This can make students confuse reactive power with reactive energy.
- ch 5 [low] Section 2, apparent powers paragraph: The exception 'unless their power factors are equal' is incomplete. Two 100 VA loads at 0.8 lagging and 0.8 leading have equal power-factor magnitude but total |S|=160 VA, not 200 VA, because their Q values cancel.
- ch 6 [high] quiz Q4 answer: The last sentence says the load currents' phasor sum is 'no longer forced through the neutral', which reads as if the sum is now non-zero. With the neutral open there is no return path, so by KCL at the load star point the three load currents must sum to exactly zero; that is precisely why the star point shifts.
- ch 6 [low] Figure, node 'Load balanced?' note: The note 'equal Z, 120° apart' puts the 120° spacing on the impedances. Impedances have no phase spacing; it is the three phase currents (or voltages) that are 120° apart.
- ch 7 [low] Lead: "The difference gives the reactive power" is loose: the difference of the readings must be multiplied by √3 before it equals Q, so a student may write Q = W1 − W2.
- ch 7 [low] Section 3, reading the meters: "Below 0.5 pf, W2 is negative" is true only for a lagging load. For a leading load with pf below 0.5 it is W1, not W2, that turns negative, so the next sentence about lagging or leading can mislead.
- ch 7 [low] Figure caption: "Their sum stays positive" is not exact: the sum falls to zero at φ = 90° (it is shown as 0 on the plot at 90°), and it is positive only for φ below 90°.
- ch 7 [low] Section 1, the connection: "In this connection each meter sees a line-to-line voltage VL and a line current IL" is only exact for a balanced load; this section also claims the sum holds for an unbalanced load, where the two line-to-line voltages seen by the meters are not equal.
- ch 8 [low] Section 1, coefficient formulas: The formulas give a_n and b_n but never give the formula for a_0, although a_0/2 is the DC value used everywhere afterwards (including Q1 and Q3). A student cannot compute the DC term from the chapter alone.
- ch 8 [low] Figure, series labels: The middle curve is labelled '3 terms' and the last '7 terms', but the plotted expressions contain only two terms (1st and 3rd harmonic) and four terms (1st, 3rd, 5th, 7th). The labels contradict both the expressions and the caption ('one term, then adding the 3rd harmonic, then up to the 7th'), so a reader cannot tell what is being counted.
- ch 8 [low] Quiz Q6: The conclusion (an extremum at t = 0) is right, but the stated reason is not sufficient. Each cosine peaking at t = 0 does not by itself force the sum to peak there; a sum with mixed-sign coefficients can still be a minimum or a flat turning point. The correct reason is that all sine terms vanish at t = 0, so the slope is zero.
