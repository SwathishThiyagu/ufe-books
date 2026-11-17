# m-linalg-u2: free-model run

- Book: `books/common/m-linalg/m-linalg-u2.html`
- Status: ok
- Model calls so far: 19 (66,530 tokens in, 138,072 out), 3.3 minutes

## Checker

```
m-linalg-u2.html: 7 chapters, 13611 words, 8 figures, 127 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 4, Pn(t) example: The sentence 'Degree exactly n fails: tⁿ + (−tⁿ) = 0 has degree 0' is wrong. The sum is the zero polynomial, and the zero polynomial has no degree (some books assign it −∞, none assign it 0). A student will carry away the false fact that 0 has degree 0.
- ch 1 [low] Section 3, property 2 proof: The step jumps straight from a·(0 + 0) = a·0 + a·0 to a·0 = 0. The missing link is that 0 + 0 = 0, so the left side equals a·0; you then subtract a·0 from both sides.
- ch 1 [low] Section 3, property 4 proof: The chain 'so (a⁻¹a)·v = v = 0' skips the reason the right-hand side a⁻¹·0 is 0; it silently uses property 2, which was proved just above.
- ch 2 [high] Exam traps, third trap: The trap says: 'Direct means U ∩ W = {0}, not just dim(U + W) = dim U + dim W.' This is false. For finite-dimensional subspaces the dimension equality is exactly equivalent to directness, because dim(U ∩ W) = dim U + dim W − dim(U + W) = 0 forces U ∩ W = {0}. As written, a student is taught that a correct sufficient test is insufficient.
- ch 2 [low] Section 3, last sentence: 'If the intersection has positive dimension, the sum is not direct even when dimensions add up' contradicts itself: if U ∩ W has positive dimension then dim(U + W) is strictly less than dim U + dim W, so the dimensions never 'add up' in that case. A student will not know what 'dimensions add up' means here.
- ch 2 [low] Section 2, 'Why the two conditions agree': The symbols u and w appear in 'u + w = (u + v) + (w − v)' without saying what they are, and the two decompositions are only distinct because v ≠ 0. A reader may not see why this produces two different splits of the same vector.
- ch 3 [low] Section 3, Spanning sets: 'Some syllabi write generating set, linear hull, or closed linear span for the same object.' A generating set is the set S itself, not the span; and 'closed linear span' normally means the closure of the span (used in infinite-dimensional settings), which is a different object.
- ch 3 [low] Section 2, subspace-test bullets: The second bullet writes 'If u = Σaᵢvᵢ and w = Σbⱼwⱼ are in span(S)' — the letter w names both the sum vector and the vectors being combined, so a student cannot tell which is which.
- ch 3 [low] Section 3, Pictures: 'A single vector, or the zero vector alone, gives only that line or only the origin' pairs the two cases wrongly: it suggests a single vector gives a line and the zero vector gives the origin, but 'that line' has no clear antecedent and the sentence reads as if the zero vector were a separate kind of single vector.
- ch 4 [low] Worked example 1, output block: The output block shows the bare numbers 2, 2, 2, -1, 0 with no labels, so a student cannot tell which numbers are the two ranks and which are the coefficients of the relation. The order is also ambiguous.
- ch 4 [low] Section 1 and Exam traps, last trap: Section 1 defines independence for a set S = {v₁, …, vₖ}, but the trap says a set listing the same vector twice is dependent. Under set notation {v, v} is the one-element set {v}, which can be independent, so the two statements clash.
- ch 5 [high] Exam traps, bullet 1: The trap says the set {(1, 1), (1, 0)} is a basis of R² and is 'neither' orthogonal nor containing e₁, e₂. The set does contain e₁ = (1, 0), so the example contradicts its own claim.
- ch 5 [low] Section 1 and Section 2: Section 1 defines a basis as a set B, but coordinates are then written as an ordered list, and Section 2 says a basis is an ordered list when coordinates are written. A student may think the two statements conflict.
- ch 5 [low] Section 3, first two working rules: The rules 'a spanning set of exactly n vectors is a basis' and 'an independent set of exactly n vectors is a basis' do not state that the vectors must lie in V and that V has dimension n.
- ch 6 [low] Section 3: The sentence 'The system has one solution when nullity is 0, and infinitely many when nullity is positive' is written without repeating the consistency condition. Read on its own it is false: a system with nullity 0 can still be inconsistent (no solution), and a consistent system with positive nullity has infinitely many solutions only because it is consistent.
- ch 6 [low] Beyond: The chapter describes three subspaces (row, column, null), but the text calls them 'the four fundamental subspaces'. The fourth one is not mentioned, so a student counting three will be confused.
- ch 7 [low] Section 2, replacement proof: "u₁ is a non-zero combination of B" is ambiguous: a combination is not called non-zero, and a student may read it as u₁ ≠ 0 rather than as "a combination in which at least one coefficient of a vᵢ is non-zero".
- ch 7 [low] Exam traps, first bullet: The phrase "the sum is independent only because ..." uses "independent" in the everyday sense (independent of the representative) while the chapter elsewhere uses "independent" for linear independence. A student can misread the trap.
- ch 7 [low] Section 2, extension theorem: "Add vectors until maximal" is vague and does not tell the student where the added vectors come from, so the reason the process must stop and must end in a basis is missing.
