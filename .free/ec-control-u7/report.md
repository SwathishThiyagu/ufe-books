# ec-control-u7: free-model run

- Book: `books/eie/ec-control/ec-control-u7.html`
- Status: ok
- Model calls so far: 19 (64,818 tokens in, 185,486 out), 5.7 minutes

## Checker

```
ec-control-u7.html: 6 chapters, 11761 words, 7 figures, 127 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Lead and Section 1 static-nonlinearity definition: The lead says every case, including backlash, is a static nonlinearity y=f(x) whose output depends only on the present input. Backlash has memory: its output depends on direction and history, and the input-output relation is multi-valued. Section 3 says this explicitly, so the lead contradicts the chapter.
- ch 1 [low] Section 3 formula box: The equations y=x−b (increasing) and y=x+b (decreasing) are branch equations only after the gap is taken up. Used immediately at a reversal they give a jump of 2b, while the prose correctly says the output holds until the input moves through 2b.
- ch 1 [low] Worked example 1 step 3 and Quiz Q4: The unit notation '3−0.1 mA' is dimensionally ambiguous: the 3 is also an input in mA.
- ch 2 [high] Section 1, 'Two assumptions make the method work': The chapter states as a required assumption that n(x) is odd AND memoryless (output depends only on the present input). But Section 2 and the exam traps then treat backlash, whose output depends on the direction of past motion, and whose describing function is complex. A student will think backlash cannot be analysed by this method, contradicting the rest of the chapter.
- ch 2 [low] Section 3, bullet 'Check the crossing direction': 'A small change in A must move the operating point toward the stable side' is circular and does not tell the student how to do the check. The stable side is exactly what the check is supposed to decide.
- ch 2 [low] Lead and Quiz Q1 answer: The lead defines N(A) as 'the amplitude of the fundamental output divided by A', a real number, while Section 1 defines it as the complex ratio of phasors Y1/A. The quiz answer repeats the real-word 'amplitude' and then adds that it may be complex. The two statements sit uneasily together.
- ch 2 [low] Section 3, last paragraph: The pointer 'See 7.4 Limit cycles' is plain text, so the student cannot jump to it on a phone, unlike other chapter cross-references in the series.
- ch 3 [low] Section 1, last sentence of the paragraph on equilibria: The description of a limit cycle as any closed path that traps nearby paths is too loose: in a linear centre the neighbouring closed orbits also surround and are trapped near each other, yet they are not limit cycles. The standard definition needs isolation.
- ch 3 [low] Section 2, nullcline paragraph: 'The x₂ = 0 line is the horizontal-axis nullcline' reads as if x₂ = 0 were the horizontal axis itself rather than the x₁-axis (the horizontal axis is the line x₂ = 0, but calling the nullcline 'horizontal-axis' is confusing when the arrows on it are vertical).
- ch 3 [low] Section 3, after the characteristic equation: 'Here j is the imaginary unit, j² = −1' is dropped in immediately after λ² − (∂f/∂x₂)λ − (∂f/∂x₁) = 0, an equation in which no j appears; a student may think j belongs to that formula.
- ch 3 [low] Section 3, eigenvalue class list: The list omits the repeated-real-root case (λ₁ = λ₂), which is still a node (stable or unstable, sometimes a star or degenerate node). A student meeting equal eigenvalues will not find a class for them.
- ch 3 [low] Section 1 or Section 2: The chapter never states the basic drawing rule that two trajectories cannot cross (they can only meet at an equilibrium point, where the vector is zero). Students sketching by hand join curves that should never touch.
- ch 4 [low] Section 1: "A nearby state inside the curve and a nearby state outside may spiral towards it" uses "may", which makes attraction sound optional. For a stable limit cycle every nearby state, inside or outside, approaches the curve; a student can read the sentence as describing a semi-stable cycle.
- ch 4 [low] Section 2 (Poincaré–Bendixson): The hypothesis says only that R is bounded and that a trajectory enters R and never leaves. The theorem also needs R to be closed (compact) and positively invariant — the trajectory, once inside, must be unable to cross the boundary — and the trajectory must be defined for all t ≥ 0.
- ch 4 [low] Section 3 figure paragraph and figure caption: The text says the intersection means the relay loop "has a limit cycle" and the caption says the loop "has a limit cycle", but the chapter itself states that an intersection is only a candidate and that a separate stability check is needed; the worked example never performs that check. The two statements pull in opposite directions.
- ch 4 [low] Exam traps, bullet 3: "Its frequency is not the frequency of any input sine" is stronger than the facts. In a forced system an oscillation frequency can coincide with the input frequency (entrainment). The point is that the limit-cycle frequency is set by the loop itself, not copied from the input.
- ch 4 [low] Beyond: The circle criterion is grouped with methods that give "more accurate tests" of a predicted limit cycle. The circle criterion is a sufficient condition for absolute stability — it certifies that no limit cycle exists in a sector-bounded system — so it answers a different question from describing-function amplitude prediction.
- ch 5 [high] Section 3 (Krasovskii method) and Quiz Q6: The Krasovskii theorem is stated too strongly. Negative definiteness of Jᵀ + J everywhere gives asymptotic stability of the origin; the step to global asymptotic stability also needs the candidate V(x) = f(x)ᵀf(x) to be radially unbounded (and the origin to be the only equilibrium). Without that hypothesis the global claim is not justified.
- ch 5 [low] Exam traps, first bullet: "the answer is no unless an extra argument ... is supplied" reads as if the system were declared not asymptotically stable. It only means this V cannot prove it; the system may well be asymptotically stable.
- ch 5 [low] Figure (blocks spec): Both outgoing edges of the node labelled "V̇<0?" are labelled "yes" and "≤0". "≤0" is not a branch of that question, so a student may read it as a second yes.
- ch 6 [low] Section 2 (stability guarantee) and Quiz Q3: The stated condition for the stability guarantee is incomplete. With Q ≥ 0 only (the chapter itself allows zero diagonal entries in Q) and (A, B) controllable, the Riccati equation can have a positive semidefinite solution whose closed loop A − BK still has an unstable pole. Example: A = diag(1, −1), B = [1; 1], Q = diag(0, 1), R = 1 is controllable, P = diag(0, 0.414) solves the ARE, yet A − BK has a pole at +1 because the unstable state carries zero weight in Q.
- ch 6 [low] Section 3, sentence 'R must be strictly positive, never zero, because free control makes the cost unbounded': The cost cannot become unbounded: the integrand xᵀQx + uᵀRu is non-negative. What fails with R = 0 is the problem itself — it becomes singular and the optimal input may be unbounded (impulsive), so no finite gain exists.
- ch 6 [low] Quiz Q6 answer: The answer explains the choice of the positive semidefinite solution only through 'feedback sign'. The sign of K is decided by P itself; the real reason is that P defines the optimal cost-to-go J* = xᵀPx, which is a squared quantity and so cannot be negative. The other roots are not valid value functions and give a saddle or unstable closed loop.
