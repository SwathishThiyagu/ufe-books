# m-calculus-u3: free-model run

- Book: `books/common/m-calculus/m-calculus-u3.html`
- Status: ok
- Model calls so far: 24 (91,059 tokens in, 183,303 out), 3.7 minutes

## Checker

```
m-calculus-u3.html: 8 chapters, 12341 words, 9 figures, 142 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 3, subsequences paragraph: The sentence 'The converse fails: (−1)ⁿ has subsequences constant at 1 and at −1, but the whole sequence diverges' is logically wrong and contradicts Quiz Q8. The converse of 'aₙ → L implies every subsequence → L' is 'every subsequence → L implies aₙ → L', and that converse is TRUE. What fails is the weaker statement that having some convergent subsequences forces the whole sequence to converge.
- ch 1 [high] Worked example 1, step 4: The inequalities have dropped out of the formula: 'We need 5/(n+2)  5/ε, so n > 5/ε − 2.' The step cannot be read and the logic of solving for n is lost.
- ch 1 [high] Quiz Q5, answer: The inequality is missing: '|1/n| = 1/n  1000'. The reasoning that gives n > 1000 has disappeared.
- ch 1 [high] Quiz Q6, answer: The inequality is missing: 'Need 1/(n+1)  50 → n > 49.' The step from the requirement to n > 49 is unreadable.
- ch 1 [low] Section 3, limsup/liminf formula: Defining limsup and liminf as the largest and smallest limits of convergent subsequences is only correct for bounded sequences; an unbounded sequence may have no convergent subsequence, and the limsup is then +∞ or −∞.
- ch 1 [low] Figure caption: 'after n passes 499' is imprecise: the term a₄₉₉ already lies inside the band, since 5/501 < 0.01.
- ch 2 [high] Section 4, Cauchy criterion: The statement is cut off in the middle of the inequality: "…for all m > n ≥ N, |a_{n+1} + a_{n+2} + … + a_m| 3.8." The required "< ε" is missing, and "3.8" appears with no meaning, so the criterion is left as an incomplete sentence a student cannot use.
- ch 2 [high] Quiz Q6, answer: The quiz answer repeats the broken inequality: "|a_{n+1} + … + a_m|  n ≥ N." The "< ε" and the quantifier "for all m > n ≥ N" are missing, so the model answer is not a correct statement of the criterion.
- ch 2 [low] Section 1, closing lines: "The terms aₙ alone do not decide it" is false as written: the sequence of terms fully determines the series. The intended point is narrower — the limit of aₙ alone does not decide convergence.
- ch 2 [low] Section 1, second paragraph: "Some syllabi say series of real numbers or partial sums for the same idea" confuses two different objects. A series is the infinite sum; the partial sums form a sequence, not the same idea.
- ch 2 [low] Section 4, harmonic series grouping: The block formula "from 1/(2^k + 1) to 1/2^{k+1}" is used without saying where k starts or noting the first two terms 1 and 1/2 are outside the blocks. A reader can miscount the terms.
- ch 3 [high] Section 1, limit comparison: The sentence is corrupted: "let L = lim (aₙ/bₙ) with 0 1), Σaₙ converges." The condition on L and one whole direction of the conclusion have dropped out, so the test cannot be read. As printed it also fails to say that no conclusion is possible when L = 0 or L = ∞.
- ch 3 [high] Section 3, ratio test rule: The rule reads "if L  1, it diverges". The case L < 1 (converges) has been lost, so the test as printed is incomplete and its inequality symbols are missing. A student copying this gets a wrong rule.
- ch 3 [high] Quiz Q3, answer: The answer is corrupted: "The ratio (aₙ/bₙ) → 1, and 0 1), the series converges." The limit comparison condition and the reason Σ1/n² converges are both missing, so the argument does not hang together.
- ch 3 [high] Beyond box, last lines: "The p-series is the real part of the Riemann zeta function" is false. For real s > 1, ζ(s) = Σ1/nˢ is exactly the p-series with p = s; it is not a real part of anything.
- ch 3 [low] Section 2, first step of the method list: "Check f(x) = aₓ is positive..." mixes the index x with the term aₙ. The integral test was stated with aₙ = f(n), so the check should be written on f(x) alone, with aₙ read off as f(n).
- ch 3 [low] Section 3, Cauchy condensation paragraph: Σ1/(n log n) is given as an example the condensation test "handles", without saying the outcome. Many students will read this as an example that converges, but this series diverges.
- ch 3 [low] Section 3, opening formula block: The placeholder text "[formula]" is left in front of the ratio limit, before "L = lim |aₙ₊₁/aₙ|".
- ch 4 [low] section 3, first paragraph: The paragraph says 'A failure of any condition means the test gives no conclusion, not that the series diverges', then two sentences later says that if bn does not tend to 0 the series diverges. The first sentence is false for the limit condition, and a student reading quickly will carry away the wrong rule.
- ch 4 [low] worked example 1, step 4, and exam traps entry 1: The chapter counts the Leibnitz hypotheses inconsistently. Section 3 says 'check the three conditions', but step 4 says 'the two conditions of the Leibnitz test hold' and the first trap says 'both conditions form the hypothesis'. Students copying this into an exam answer will mix up the count.
- ch 5 [high] Section 1, last paragraph of the definitions: The sentence "The absolutely convergent series Σ1/n² and Σ1/2n sit inside the convergent family" writes the geometric series as Σ1/2n, with no exponent on the 2. Read in the natural way, Σ1/(2n) is half the harmonic series and diverges, so the sentence then declares a divergent series absolutely convergent. The figure writes Σ1/2ⁿ correctly, but the body text does not.
- ch 5 [low] Worked example 1, steps 1 and 2: "1/(n+1)1/2" and "Σm=2∞ 1/m1/2" use 1/2 as an exponent but print it on the baseline, so they can be read as multiplying by one half. The same happens in Section 2 with "Σ1/np" for the p-series.
- ch 5 [low] Section 1, definitions: "Some syllabi say “convergence with absolute values” for absolute convergence" is not a recognised alternative name in standard texts; a student may take it as a term to reproduce in an exam.
- ch 5 [low] Section 1 formula box and definitions, Section 2 worked list: The formula is printed with subscripts (Σ|a<sub>n</sub>|) but the text beside it writes "an", "|an|", "aN", "Σn=1N |an|" on the baseline. On a phone these read as products, so the definitions of an and AN are hard to follow.
- ch 6 [high] Section 2, note under the formula R = lim |cₙ/cₙ₊₁|: The two extreme cases are swapped. Since R is that limit, a limit of 0 gives R = 0 (as the chapter's own example Σ n! xⁿ shows), and a limit of ∞ gives R = ∞. The chapter states the opposite, so a student following the note would get R = 0 and R = ∞ interchanged for every factorial-type series.
- ch 6 [high] Quiz Q2 answer: The answer repeats the swapped extreme cases: 'If the limit is 0 then R = ∞; if the limit is ∞ then R = 0.' This marks a wrong statement as correct and contradicts the worked example Σ n! xⁿ given in Section 2.
- ch 6 [high] Section 2 (ratio test sentence), Section 3 (first sentence), Worked example 1 step 3: The inequality signs have dropped out, leaving meaningless statements: 'L|x−a|  1' in Section 2, 'For |x−a|  R it diverges' in Section 3, and 'absolute convergence for |x|  1' in step 3. Section 2 then says 'Read the first condition as |x−a| < 1/L', but no first condition is visible. Step 3 also never states divergence for |x| > 1, so 'Hence R = 1' is left unsupported.
- ch 6 [low] Lead paragraph: 'Every scientific calculator uses this idea' is an overstatement; many calculators evaluate sin and log by other algorithms (for example CORDIC), and the series enter through polynomial approximations derived from them.
- ch 7 [low] Section 1, first step of the numbered list: The step 'Check aₙ > 0 and ratio limit 1' reads as if the ratio limit must equal 1 for Raabe's test to be legal. The only hypothesis of the test is aₙ > 0; ρ = 1 is just the situation in which the ratio test has already failed and Raabe's test becomes useful. A student may wrongly reject a valid Raabe computation when ρ ≠ 1.
- ch 7 [low] Section 2, closing paragraph: 'Use Raabe's reciprocal aₙ/aₙ₊₁' is loose wording. aₙ/aₙ₊₁ is the reciprocal of the ratio-test quantity aₙ₊₁/aₙ; calling it 'Raabe's reciprocal' can confuse a reader into thinking an extra inversion is needed.
- ch 7 [low] Both formula blocks and the statement of each test: The limits are written only as '→ L' with no statement that n → ∞ and no condition that the limit must exist. If Rₙ (or the log quotient) oscillates and has no limit, neither test gives any conclusion, and the chapter never says so.
- ch 8 [high] Section 2, Archimedean property paragraph: The sentence is broken: "For example, to force 2/N  200." The inequality sign and the middle of the sentence are missing, so the student sees no condition and no conclusion. The same characters ("<") were swallowed elsewhere in the chapter, so the text was cut.
- ch 8 [high] Section 2, Cauchy criterion for series: The criterion is cut off: "there is N such that |a_{N+1} + … + a_m|  N." The inequality and the quantifier over m are lost, so the statement cannot be read.
- ch 8 [high] Worked example 1, step 3: Step 3 reads "Need 2/N  200." The condition 2/N < 0.01 and the resulting requirement N > 200 are missing, so steps 3 and 4 do not connect.
- ch 8 [high] Quiz Q3, answer: The answer reads "Need 2/N  100. Take N = 101; 2/101 ≈ 0.0198." The inequality 2/N < 0.02 and the step N > 100 are missing, so the answer does not show why N = 101 is chosen.
- ch 8 [low] Quiz Q2, answer: The triangle-inequality step is compressed; it skips the middle term and the range of m, n.
- ch 8 [low] Figure description: "…with ε = 0.01 gaining a real limit, then completeness" is vague; a reader cannot tell what the solid path means.
