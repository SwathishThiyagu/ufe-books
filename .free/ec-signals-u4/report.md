# ec-signals-u4: free-model run

- Book: `books/ece/ec-signals/ec-signals-u4.html`
- Status: ok
- Model calls so far: 19 (64,620 tokens in, 161,336 out), 5.1 minutes

## Checker

```
ec-signals-u4.html: 4 chapters, 7470 words, 5 figures, 93 KB
OK
```

## For the reviewer

- chapter 2: the figure cannot be drawn: tree is too wide (6 leaves); use fewer leaves or shorter labels

## Reviewer notes (after any revision)

- ch 1 [high] Section 2 and Section 3 table: The chapter says it uses the one-sided transform unless stated, but then computes transforms of left-sided and two-sided signals such as −e^(−at)u(−t) and e^(−2t)u(t)+e^(3t)u(−t). The one-sided integral from 0 to ∞ ignores the left-sided part, so those transforms are not 1/(s+a) or 1/(s+2)−1/(s−3); they require the bilateral transform. The switch is never stated.
- ch 1 [low] Section 2: The sentence is cut off: 'but the integral converges for Re(s)−2tu(t)...' The inequality and the start of the two-sided example are missing, so the text is unreadable.
- ch 1 [low] Section 1: The statement 'The Fourier transform is the special case σ=0, so X(jω)=X(s) at s=jω when the ROC includes the jω axis' is only true for the bilateral transform or for signals that are zero for t<0. With the one-sided transform, X(jω) is the Fourier transform of x(t)u(t), not of x(t) if x(t) is nonzero for t<0.
- ch 1 [low] Section 3: 'For a causal system, the ROC is outside the outermost pole' is vague and can be wrong if 'outermost' means largest magnitude. The correct rule is that the ROC lies to the right of the rightmost pole.
- ch 2 [high] Section 1, time-scaling formula: The property is stated for 'a is a nonzero real number', but the chapter defines the one-sided transform with a lower limit of 0−. For a<0 the formula fails. Example: x(t)=u(t), a=−1. Then u(−t)=0 for t>0, so L{u(−t)}=0, while (1/|a|)X(s/a)=−1/s. A student who uses a=−2 gets a wrong answer.
- ch 2 [low] Section 1, time-shift formula (also quiz Q1): The formula is written for a shift of t₀ but never says t₀ must be positive. With the one-sided integral, for t₀<0 the signal x(t−t₀)u(t−t₀) is already running at t=0, the part before t=0 is not integrated, and L{x(t−t₀)u(t−t₀)}=e^(−s t₀)X(s) is no longer true.
- ch 2 [low] Worked example 1, dry run table: The row 'multiplier a = 3' reuses the symbol a, which the chapter uses for the time-scaling constant. In the s-shift rule the multiplier is e^(s₀t) with s₀=−3, and the decay constant is 3, so the label is misleading.
- ch 3 [high] Section 3, first paragraph: The sentence giving the left-sided case is garbled: "and gives −e^(−at)u(−t) when Re(s)0." The inequality is broken, so the condition for the left-sided inverse is missing. A student cannot tell which ROC gives −e^(−at)u(−t).
- ch 3 [low] Section 1, cover-up formula note: The note "p_k is positive when the pole is at −p_k" is vague and reads like a condition on p_k rather than a definition of the pole location. Students may think p_k must be positive.
- ch 3 [low] Figure, node f: The last node is labelled x(t) but its note gives only the ROC ("ROC Re(s)>−1"), not the time function the flowchart is supposed to end with. The reader has to jump back to the text to see the result.
- ch 4 [high] Section 2 (cancellation example), echoed by Quiz Q4: The example does not show what the sentence claims. In H(s)=(s+1)/((s+1)(s−2)) the cancelled factor (s+1) is a stable pole at s=−1 paired with a zero at s=−1. Cancelling it gives 1/(s−2), which still shows the pole at s=2. So nothing is hidden, and the sentence 'hides an unstable pole at s=2' is wrong; it also contradicts the Q4 answer, which says the pole at s=2 survives cancellation.
- ch 4 [low] Section 2 and Exam traps (pole on the jω axis): 'A simple axis pole gives a sustained bounded oscillation' is true only for a simple pole pair at s=±jω with ω≠0. A simple pole at s=0 gives a constant, non-decaying impulse response, and a step input gives a growing ramp, not an oscillation. Quiz Q6 itself uses a pole at s=0, so the trap wording can mislead.
