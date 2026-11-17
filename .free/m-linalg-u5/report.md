# m-linalg-u5: free-model run

- Book: `books/common/m-linalg/m-linalg-u5.html`
- Status: ok
- Model calls so far: 24 (88,742 tokens in, 191,890 out), 4.3 minutes

## Checker

```
m-linalg-u5.html: 7 chapters, 11775 words, 8 figures, 124 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Figure (spec and aria): The flow and the aria say the inner product ⟨u, v⟩ gives the norm. The norm comes from the inner product of a vector with itself, ⟨u, u⟩, not from ⟨u, v⟩. The caption is right but the diagram story is not.
- ch 1 [low] Section 2, polynomial-space paragraph: 'Two functions are close everywhere on [0, 1] in the average sense' is contradictory. The integral norm measures average (mean-square) closeness over [0, 1]. It does not control closeness at each point: two functions can be close in this norm and still differ sharply on a short interval.
- ch 1 [low] Beyond: 'The same three axioms, with the integral inner product on functions, lead to Hilbert spaces' is incomplete. The inner product axioms alone give an inner product space (a pre-Hilbert space). A Hilbert space also requires completeness, that every Cauchy sequence converges in the space.
- ch 2 [high] Figure (nodes and caption): The chart shows the chain orth (u ⊥ v) → Pythagoras → parallelogram law, and the caption says 'orthogonality gives the Pythagorean relation and the parallelogram law'. The parallelogram law is not a consequence of orthogonality or of Pythagoras. The text itself derives it by adding the expansions of ‖u+v‖² and ‖u−v‖², which works for any two vectors with no condition on ⟨u,v⟩. A student reading the chart will believe the parallelogram law needs u ⊥ v.
- ch 2 [low] Section 2, angle sentence: cos θ = ⟨u,v⟩/(‖u‖‖v‖) divides by the lengths, so it is undefined if u = 0 or v = 0. The sentence says the angle 'exists' for all vectors.
- ch 2 [low] Section 2, first line: 'Add the expansion of ‖u + v‖²' — nothing is being added at this point; the expansion itself is what is written.
- ch 2 [low] Beyond: Chapter 5.3 is named in plain text; the book's convention is to point to another chapter with a link so the reader on a phone can jump there.
- ch 3 [high] Exam traps, Bessel/Parseval bullet: The statement 'Equality, Parseval's identity, holds only for a full orthonormal basis' is false. For a partial orthonormal set, equality in Bessel can hold for a particular vector u whenever u lies in the span of that set, for example u = 0. The correct restriction is that Parseval's identity holds for every u only when the orthonormal set is a full basis.
- ch 3 [low] Section 2, after Bessel's inequality: The text calls the partial orthonormal set 'the basis' even though it has just said the set is not necessarily a full basis. This is imprecise and can confuse students about what is being projected onto.
- ch 3 [low] Section 3, dimension proof sentence: 'Gram–Schmidt turns the added vectors into a basis of W⊥' is ambiguous. If Gram–Schmidt is applied only to the added vectors, they need not become orthogonal to W. The process must be applied to the whole extended basis, starting with the basis of W.
- ch 4 [high] Section 3 (Original-vector form): The un-normalized formula subtracts projections onto the original input vectors uᵢ: vₖ = uₖ − Σ (⟨uₖ, uᵢ⟩/⟨uᵢ, uᵢ⟩) uᵢ. This is only valid if the uᵢ are already mutually orthogonal, which they are not in general. The orthogonal vectors produced so far, v₁, …, vₖ₋₁, must be used inside the sum. Test with the chapter's own example: u₁ = (1,1,0), u₂ = (1,0,1), u₃ = (0,1,1) gives v₃ = (−1, 1/2, 1/2), which is not even perpendicular to u₁, instead of the correct (−2/3, 2/3, 2/3).
- ch 4 [high] Exam traps, trap 2: The trap says the original-vector coefficient is ⟨uₖ, uᵢ⟩/‖uᵢ‖². That is wrong for a general (non-orthogonal) basis and contradicts trap 1 in the same list, which correctly insists the coefficient pairs with a vector already made orthogonal to the others.
- ch 4 [low] Section 2, why the subtraction works: 'dividing by ‖vₖ‖ keeps that direction' is loose: it should say that scaling by a positive number preserves the zero inner products and gives length one.
- ch 5 [high] Section 1, Best approximation line: The inequality is broken: it reads "for every w in W with w ≠ p, ‖b−p‖  ‖b−p‖²", with the comparison sign missing and the right-hand side wrongly written as ‖b−p‖² instead of ‖b−w‖. As printed the sentence states no property and a student cannot tell what is being claimed.
- ch 5 [high] Quiz Q1: The question asks for the three matrix properties of an orthogonal projection matrix, but the given answer lists P = QQᵀ (a formula for one particular construction of P, not a property) together with only two properties. It does not match the three properties stated in Section 1 (P² = P, Pᵀ = P, and P projects onto col(Q)).
- ch 5 [low] Section 3, second paragraph: The last term of the sum is printed as "em²" instead of e with subscript m, so the expression looks like the product e times m squared.
- ch 5 [low] Figure: Node p is labelled "p = QQᵀb" while its note says "closest point in col(A)". QQᵀ projects onto col(Q), which equals col(A) only when Q is an orthonormal basis of col(A); the figure does not say this, so the two labels read as inconsistent.
- ch 5 [low] Lead: "A projection drops a vector straight down onto a subspace" suggests a vertical drop, which is only the picture for a horizontal subspace. In general the drop is perpendicular to the subspace, in any direction.
- ch 6 [high] Exam traps, 4th bullet (sign slip): It says that when qⱼ is multiplied by −1, column j of R also changes sign. That is wrong. Since A = QR = Σᵢ qᵢ · (row i of R), the qⱼ term is qⱼ times row j of R, so the sign flip must be applied to row j of R, not to column j. Negating column j of R would change column j of A and break A = QR.
- ch 6 [low] Section 1, sentence after qⱼ = vⱼ/‖vⱼ‖: 'The numbers you subtract are exactly the entries of R' can mislead a student into thinking every entry of R comes from a subtraction. The diagonal entry rⱼⱼ is not subtracted; it is the norm ‖vⱼ‖.
- ch 6 [low] Quiz Q2 answer: 'At step j only q₁,…,qⱼ₋₁ are used, so entries below row j are zero' is loose. The zeros are in column j, below the diagonal, and the reason needs the span statement.
- ch 7 [low] Section 2, computing the factors (last line of the bullet list): The sentence 'You may also compute A Aᵀ to get U directly; its nonzero eigenvalues are the same σᵢ². AᵀA is usually better for V because A has n columns' does not actually explain the choice. Whether AᵀA is the better one depends on whether n is smaller than m, not just on A having n columns; as written a student may think AᵀA is always preferable.
- ch 7 [low] Section 1, 'Why does this always work?': The proof stops after showing the uᵢ are orthonormal and then states 'Thus A = UΣVᵀ holds.' The step that the sum Σᵢ σᵢuᵢvᵢᵀ really rebuilds A is never shown, so the conclusion looks like it comes from orthonormality alone.
