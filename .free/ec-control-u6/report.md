# ec-control-u6: free-model run

- Book: `books/eie/ec-control/ec-control-u6.html`
- Status: ok
- Model calls so far: 16 (57,876 tokens in, 126,376 out), 4.7 minutes

## Checker

```
ec-control-u6.html: 5 chapters, 9942 words, 6 figures, 109 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 4, biomedical models: It says 'lung volume V and flow V̇ as the states'. Flow is the derivative of volume, so V and V̇ are not two independent numbers; a model cannot carry both as separate states. A student will conclude that a single-compartment lung has order 2, which is wrong.
- ch 1 [low] Section 2, after the matrix table: 'The eigenvalues of A are the poles of the system' is stated unconditionally. It holds only when the model is minimal; with a hidden mode (a pole–zero cancellation between A and C or B) an eigenvalue of A is not a pole of the transfer function.
- ch 1 [low] Section 2, integrator picture: Tense slip: 'the loop through A alone decided how the state drifts'. The sentence describes a general fact, not a past event, and it reads oddly right before 'which is exactly the free response'.
- ch 1 [low] Section 4, first paragraph: The discrete-time update x[k+1] = Φx[k] + Γu[k] uses Φ and Γ without defining them, and the letters appear nowhere else in the chapter.
- ch 1 [low] Section 4, biomedical models: Lung compliance is called C in the same paragraph that uses C for the output matrix of the state model. The same symbol for two different things confuses a reader meeting both on one screen.
- ch 1 [low] Exam trap 5, and the counting check in Section 3: Both equate a state variable with an energy storage element ('A 3×3 A matrix means ... three energy storage elements'). State variables are any independent set of numbers, and after a transformation x̄ = Tx they are usually mixes of physical quantities with no single storage element behind each one.
- ch 2 [low] Section 1, phase-variable sentence: "x₁ is the output of the first integrator in a chain" clashes with the matrices, where ẋ₁ = x₂. Counting from the input u, the first integrator produces xₙ, not x₁, so a student can build the wrong block diagram.
- ch 2 [low] Section 3, poles statement: "Its roots are the eigenvalues of A, so they are the poles of G(s)" is not always true. If a mode is uncontrollable or unobservable, a root of det(sI−A) cancels with a zero of the numerator and is not a pole of G(s).
- ch 3 [low] Worked example 1, step 4: The partial-fraction lines are written with an ellipsis denominator, e.g. (s+3)/… , so a student cannot see which denominator is meant and may copy it into an exam answer.
- ch 3 [low] Worked example 1, dry run: The dry run table is present but completely empty (no head, no rows), which will render as a blank table under a fully worked example that already has numbers.
- ch 4 [high] Section 2 (observability rank test): The sentence after "The test is rank(Qo) = n" is broken: "If rank(Qo) o is square n×n and det(Qo) ≠ 0 proves observability." The condition for failure (rank < n means not observable) is lost and the p = 1 determinant shortcut is left grammatically attached to an orphan "o". A student cannot read what the failure condition is.
- ch 4 [low] Lead, Section 1, exam traps and quiz Q2: "An−1B" and "CAn−1" are typed as plain text, so they read as A times n minus 1 times B rather than A to the power n−1 times B. The formula blocks use superscripts, so the notation is inconsistent inside the same chapter.
- ch 4 [low] Exam traps, first bullet: "One block proves nothing" is too strong. If B alone already has rank n (n independent inputs), the single block B does prove controllability.
- ch 4 [low] Section 1, last sentence: It says "The figure after this section shows ...", but the figure is placed after Section 3, two sections later, so a reader looking just below Section 1 finds no figure.
- ch 5 [low] Section 2 (step 2) and Ackermann formula in Section 3: Powers are typed as plain letters: 'sn + an−1sn−1' and 'An−1B' read as s times n and A times (n−1) times B, not as powers. A student copying the polynomial can lose the degree.
- ch 5 [low] Quiz Q6 answer: 'the leading row selects the last row of the inverse' is wrong wording: [0 0 … 0 1] is the last (bottom) standard row, not the leading one. It also does not say the row has n entries.
- ch 5 [low] Section 1 and Beyond: The chapter never mentions that u = r − Kx changes the reference-to-output gain. With a step reference the states settle at a nonzero value fixed by −(A − BK)⁻¹Br, so the output no longer tracks r with unity gain.
- ch 5 [low] Exam trap on the sign of K: The phrase 'every gain changes sign' is loose; the reader can think each individual ki flips sign independently rather than the whole row being negated.
