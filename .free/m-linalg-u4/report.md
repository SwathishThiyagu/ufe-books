# m-linalg-u4: free-model run

- Book: `books/common/m-linalg/m-linalg-u4.html`
- Status: ok
- Model calls so far: 26 (92,952 tokens in, 205,803 out), 5.6 minutes

## Checker

```
m-linalg-u4.html: 7 chapters, 12817 words, 8 figures, 137 KB
OK
```

## For the reviewer

- chapter 2: the figure cannot be drawn: note "poly" runs off the right edge; shorten it

## Reviewer notes (after any revision)

- ch 1 [low] Section 2, the two shortcuts: The trace of A is used in the 2×2 formula λ² − (trace A)λ + det A but has not been defined anywhere earlier in the chapter. A reader who has not met the word will not know it means the sum of the diagonal entries.
- ch 1 [low] Section 2, triangular shortcut: The product is written (a₁₁ − λ)(a₂₂ − λ)⋯(ann − λ). The last factor is missing its subscript; 'ann' reads as a word, not as a_nn.
- ch 1 [low] Beyond: Plain inverse iteration does not target 'the smallest' eigenvalue by itself; it converges to the eigenvalue nearest the chosen shift, and only the shift 0 gives the smallest in magnitude.
- ch 2 [low] Section 1, opening of the bullet list (and exam trap 3): The sentence "Transformed matrices keep the same eigenvectors" is true in one direction only. Every eigenvector of A is an eigenvector of A⁻¹, A^k and p(A), but A^k and p(A) can have extra eigenvectors that A does not have. Example: A = [[0,1],[0,0]] has only one eigenvector line, while A² = 0 has every vector as an eigenvector. Trap 3 ("the eigenvectors stay the same") repeats the same overstatement.
- ch 2 [low] Lead: "Multiplicities then tell you how many independent eigenvectors are available" suggests the algebraic multiplicity gives the count. It does not: a(λ) only gives an upper bound, and the actual number g(λ) must be computed from null(A−λI).
- ch 2 [low] Section 3, proof that distinct eigenvalues give independent eigenvectors: After applying A−λmI the shorter relation is c1(λ1−λm)v1+…+c(m−1)(λ(m−1)−λm)v(m−1)=0. The text does not say why this is a real contradiction: it is nontrivial because c_i ≠ 0 and λ_i ≠ λ_m, so every coefficient is nonzero.
- ch 2 [low] Section 3, last sentence of the formula paragraph: "Equality g(λ)=a(λ) for every eigenvalue is exactly the condition for diagonalizability" is incomplete for real matrices. A real rotation such as [[0,−1],[1,0]] has eigenvalues i, −i with g=a=1, yet it is not diagonalizable over the reals because it has no real eigenvectors.
- ch 3 [high] Exam traps, fifth bullet (3×3 verification sign): The bullet says that expanding det(A − λI) and dropping the (−1)³ sign 'gives a polynomial that does not kill A'. This is false. det(A − λI) = (−1)ⁿp(λ) is a scalar multiple of p, so it also satisfies q(A) = 0; and dropping the sign on a 3×3 gives back exactly p(λ), which certainly kills A. A student who reads this will believe a correct annihilator is wrong.
- ch 3 [low] Section 3, bullet 'deg m ≤ n, and m = p exactly when no eigenvalue can be dropped': The phrase 'no eigenvalue can be dropped' contradicts the bullet above it, which says m and p have the same roots (so no root is ever dropped). What can shrink is the multiplicity, not the root.
- ch 3 [low] Section 3, heading 'Where m is smaller than p' and its third bullet: The heading promises examples where m is smaller than p, but the third bullet (A = [[2,1],[0,2]]) is an example where m = p. The mismatch is confusing on a first read.
- ch 4 [low] Section 1: The justification 'but only the first is diagonal' does not by itself prove the two matrices are not similar. Being diagonal is not what similarity keeps; diagonalizability is. As written, a student may conclude that similarity preserves the property of being a diagonal matrix, which is false.
- ch 4 [low] Section 2, multiplicity condition paragraph: The phrase 'some syllabi call the distinct-eigenvalue case regular eigenvalues' is vague and uses a name that is not standard. Students will not know what to write in an exam.
- ch 5 [high] worked example 1, step 8: Step 8 says 'Check QᵀQ = I gives QᵀAQ = diag(1, 3)'. Orthogonality of Q does not imply QᵀAQ = D. QᵀQ = I only proves the columns are orthonormal; QᵀAQ = D holds only because those columns are eigenvectors placed in the same order as the eigenvalues in D. A student will read this as an implication and repeat the mistake.
- ch 5 [low] section 1, third paragraph: 'A general matrix may lack eigenvectors' is imprecise. Over the complex numbers every square matrix has at least one eigenvector; what a general real matrix may lack is a full set of real eigenvectors (a rotation matrix has none), and it may need complex eigenvalues.
- ch 6 [high] Section 2, orthogonal reduction: The letter Q is used for two different things in the same line: the orthogonal matrix and the quadratic form Q(x). 'Put x = Qy. Then Q(x) = xᵀAx = yᵀQᵀAQy' reads as if the matrix Q equals the form Q(x), which will confuse students.
- ch 6 [high] Worked example 1, step 5 and step 6: Step 5 calls the orthogonal matrix Q, and step 6 then writes 'Q = 2x² + 2xy + 2y² = 3u² + v²', using Q for the quadratic form again. The same symbol means a matrix in one step and a scalar expression in the next.
- ch 6 [low] Section 3, general second-degree equation: 'If one eigenvalue is zero, the equation has a linear term in that direction, and translation cannot remove it' is not always true. With λ₂ = 0 the term 2f′y₂ may be absent (f′ = 0); then the equation gives a pair of parallel lines, a single line, or nothing, and no linear term exists to remove.
- ch 7 [high] Section 2, conic paragraph (the discriminant sentence): The sentence is corrupted: "h2 − ab 2 − ab = 0 is semidefinite" repeats itself and reads as nonsense, so the student cannot tell what the condition is.
- ch 7 [low] Section 2, conic paragraph: Only two of the three discriminant cases are given. The definite case h² − ab < 0 is never stated, though the ellipse discussion just before it depends on that case.
- ch 7 [low] Section 2, conic paragraph: "The signs of its eigenvalues are p and q" is wrong: p and q are counts of positive and negative eigenvalues, not the signs themselves. A student may read p as a sign.
- ch 7 [low] Section 2, conic paragraph (definite case): "gives an ellipse, or an imaginary ellipse or a single point when no real points satisfy the equation" attaches the no-real-points condition to the single point too, but a single point does have a real solution.
- ch 7 [low] Figure, node h: The node labelled "indefinite" carries the note "conic: ellipse". That pairs two different things: the 3-variable form is indefinite, while the ellipse comes from the separate 2-variable quadratic part x² + 4y².
- ch 7 [low] Lead and Section 1: The lead calls index = p the "common convention". Many textbooks define the index (index of inertia) as the number of negative squares, so calling p the common choice is misleading even though the chapter later warns about conventions.
