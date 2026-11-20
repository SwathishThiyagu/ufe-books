# ec-signals-u2: free-model run

- Book: `work/claude_figs/ec-signals-u2/tree/books/ece/ec-signals/ec-signals-u2.html`
- Status: ok
- Model calls so far: 22 (75,905 tokens in, 199,277 out), 4.7 minutes

## Checker

```
ec-signals-u2.html: 7 chapters, 17983 words, 9 figures, 225 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 3: The text says every input can be treated as a 'sum of shifted impulses' in continuous time. In continuous time the representation is an integral of shifted impulses, not a sum.
- ch 1 [low] Section 3: The convolution integral y(t)=∫x(τ)h(t−τ)dτ has no limits, and τ is reused without saying it is now a dummy integration variable; Section 1 defined τ as the delay.
- ch 1 [low] Exam traps, first bullet: The phrase 'y(t)=x(2t) has no t in the multiplier' is misleading: the argument 2t does contain t. The intended point is that there is no standalone t term outside the input.
- ch 1 [low] Section 1: The name 'zero-input test' can be confused with the zero-input response, which is the response due to initial conditions and is a different idea.
- ch 2 [low] Section 1, Section 2, Section 3, worked example, quiz Q4 and Q7: Exponents are written inline with no superscript markup, so expressions such as '1000 e−1000tu(t)' and 'e−t/τ' can be read as 'e minus 1000t' or 'e minus t over tau' rather than e raised to a power. The same happens with '1×103 Ω' and '10−6 F' in the worked example.
- ch 2 [low] Exam traps, fourth bullet: The trap mixes two different derivatives. The derivative of e<sup>−t/τ</sup> alone is −(1/τ)e<sup>−t/τ</sup> (negative), while the derivative of s(t)=1−e<sup>−t/τ</sup> is +(1/τ)e<sup>−t/τ</sup>. As written, a student cannot tell whether the mistake is the missing 1/τ factor or the sign.
- ch 2 [low] Section 2, sentence after the first formula: 'The lower limit −∞ keeps any response before t=0' is unclear. The real purpose of −∞ is to include h(λ) for λ<0, which matters only for noncausal systems; for a causal system those terms are zero anyway.
- ch 3 [high] Section 1, causal-system paragraph: The sentence is corrupted: "h(t)=0 for tt; the upper limit becomes t. If x(t)=0 for tChapter 2.4." A student cannot read what the limits become, and a stray cross-reference is glued onto the sentence.
- ch 3 [high] Worked example 1, step 3: The formula is corrupted: "Case 0≤t0t e−(t−τ)dτ". The case condition 0≤t<2 s and the lower limit 0 are missing, so the step cannot be followed.
- ch 3 [high] Worked example 1, answer line: The final piecewise formula is corrupted: "y(t)=0 for t−t for 0≤t2−t−e−t for t≥2 s". The three pieces and their conditions are unreadable.
- ch 3 [high] Quiz Q2, answer: The answer is corrupted: "h(t)=0 for tt". The key condition (t<0) is lost, so the reason the upper limit becomes t is not stated.
- ch 3 [high] Quiz Q5, answer: The corrected integral is corrupted: "With causal h and x=0 for t0tx(τ)h(t−τ)dτ." The replacement formula and its limits are not readable.
- ch 3 [low] Section 2, opening line and bullets: "Graphical convolution is a four-step habit" is followed by five bullets (sketch x, sketch and flip h, shift, multiply, integrate). The count does not match the list.
- ch 4 [high] Section 1, paragraph after the four laws: The blanket claim 'except there is no inverse. You cannot divide by a signal to undo convolution' is false as stated. Many signals do have a convolutional inverse (the inverse system, h * h_inv = δ), which is exactly what deconvolution and inverse filters use; only some signals lack one. A student reads this and concludes convolution can never be undone.
- ch 4 [low] Section 1, first line: The convolution integral is written y(t)=∫ x(τ)h(t−τ)dτ with no limits, so the reader cannot tell it is taken over the whole real line, which matters for the proof hints that follow.
- ch 4 [low] Section 1, last paragraph: 'δ(t) has unit area and zero width' describes the impulse as if it were a pulse of vanishing width; δ is defined by its sifting property (unit area), not by a width.
- ch 5 [high] Section 3: The sentence 'Causal does not imply stable: u(t) is zero for tconvolution.' is garbled and unreadable, so the counterexample is lost.
- ch 6 [high] Section 2, paragraph after y=yn+yf: The text says the constants in yn come from initial conditions 'not from x', but the step response immediately gives A=-X for y(0)=0. In the natural/forced split, the homogeneous constants are chosen so yn+yf satisfies the initial conditions, so they can depend on the input through yf(0).
- ch 6 [low] Section 3, sentence after yf=(F0/B)t: The total response is described as 'a ramp plus a decaying exponential', but the homogeneous solution also has a constant term C1. Omitting it can make students drop the constant when fitting initial position.
- ch 6 [low] Exam traps, last bullet: The sentence 'For t0 particular solution there.' is incomplete and unclear.
- ch 7 [high] Section 2 and worked example 1 (the general recipe): The recipe (set x₁=y, x₂=y′, …, substitute) and the line xₙ′ = −a₀x₁−…−aₙ₋₁xₙ + b u are correct only when the right side of the LCCDE has no derivatives of u. For a normal LCCDE such as y″+3y′+2y = u′+u, substituting x₁=y and x₂=y′ leaves x₂′ = −2x₁−3x₂+u′, which is not x′ = Ax + Bu. The chapter presents this as the form for 'an LCCDE' in general and never states the restriction.
- ch 7 [low] Worked example 1 (code block and dry run): The code block contains only the placeholder word 'pass' and the dry-run table is empty ({'head': [], 'rows': []}). A student sees a program fragment that does nothing and a table with no content, with no explanation of what is being checked.
- ch 7 [low] Lead: 'most stop at the differential equation of Chapter 2.6' is an unverifiable claim about what other syllabi cover, and state-variable ideas do appear in several standard signals textbooks. The chapter should not guess at how many courses teach it.
