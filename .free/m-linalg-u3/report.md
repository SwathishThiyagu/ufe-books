# m-linalg-u3: free-model run

- Book: `books/common/m-linalg/m-linalg-u3.html`
- Status: ok
- Model calls so far: 17 (57,826 tokens in, 122,841 out), 3.4 minutes

## Checker

```
m-linalg-u3.html: 6 chapters, 11111 words, 7 figures, 109 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 1, last bullet ("T is linear exactly when it sends every line..."): The "exactly when" claim is false. A linear map does not keep the spacing of points on a line: T(v) = 2v doubles every distance, and it is linear. Also, "sends every line through the origin to a line through the origin" alone is not enough: T(x, y) = (x³, y³) sends each line through the origin to a line through the origin but is not linear. A student will read this as a usable test and mark wrong answers right.
- ch 1 [low] Section 3, paragraph after the composition formula: The justification labels do not match the steps shown. The first equality T(S(u + v)) = T(S(u) + S(v)) uses additivity of S, not just the definition, and the second equality T(S(u) + S(v)) = T(S(u)) + T(S(v)) uses additivity of T, not "linearity of S inside T". As written, a student cannot follow which map is doing the work.
- ch 1 [low] Section 2, paragraph after the table ("Scaling by c stretches every length by |c| and fixes directions"): "Fixes directions" is wrong for c < 0, where every direction is reversed, and "stretches" is wrong for |c| < 1, where lengths shrink. The same sentence then says the zero map (the case c = 0) crushes everything to 0, which contradicts "fixes directions".
- ch 2 [low] Figure: The diagram sends ker T to '0 in W' and sends 'other inputs' to 'range T'. Read as drawn, it says the range is built only from the non-kernel inputs and that 0 is outside the range. In fact T(ker T) = {0} is inside im T, so im T contains 0 and is the span of all images, kernel images included.
- ch 2 [low] Exam traps, last bullet: 'Drop it if a free-variable solution produces it' describes a case that cannot happen. In the free-variable method each free parameter equals 1 in its own coordinate of its coefficient vector, so that vector is never the zero vector. A student may waste time looking for a zero vector that is not there.
- ch 2 [low] Quiz Q1: The answer writes T(v) = 0 without saying which zero. Here V and W are different spaces, so the zero on the right is the zero vector of W, not of V. The formula in Section 1 defines this; the quiz answer should repeat it.
- ch 3 [high] Exam traps, fourth bullet: The trap says "Do not use m + nullity = rank unless the matrix is square". The relation m + nullity A = rank A is never true, square or not. For a square n × n matrix the correct statement is n = rank A + nullity A, i.e. m = rank A + nullity A, not m + nullity A = rank A. A student can read the qualifier as licensing the wrong formula for square matrices.
- ch 3 [low] Section 2, third bullet (independence step): The step Σ c_j T(u_j) = 0 → Σ c_j u_j = Σ a_i v_i → all c_j = 0 skips the move that makes independence usable. The reader must see that Σ c_j u_j − Σ a_i v_i = 0 is a combination of the basis {v₁, …, v_k, u₁, …, u_{n−k}}.
- ch 4 [low] Exam traps, first bullet: The bullet says that swapping b1 and b2 'swaps the columns of P and permutes the rows of [T]B'. Only half is true: with B' = (b2, b1), we get [T]B' = S⁻¹[T]B S (S the swap matrix), which permutes the rows and the columns of [T]B together. Telling a student only about rows invites the slip of changing the row order while leaving the columns alone.
- ch 5 [low] Lead: The sentence 'Only a few universities teach this chapter' is inaccurate: invertible maps and isomorphisms are core material in almost every first linear algebra syllabus, so a student may skip it thinking it is optional.
- ch 5 [low] Exam traps, first bullet: The trap does not say which way the dimensions differ. With dim V > dim W a map can never be one-to-one, so a student may wrongly read the bullet as saying one-to-one is possible whenever dim V ≠ dim W.
- ch 5 [low] Exam traps, second bullet: 'It may still map some nonzero vector to zero' is too weak. When det A = 0, a nonzero vector is always sent to zero, and that non-trivial kernel is exactly why the map fails to be invertible.
- ch 6 [low] Worked example 1, output: The output block prints −5 and then four bare numbers (1.0, 0.0, 0.0, 1.0) with no label. A student on a phone cannot tell that the four numbers are the check matrix of fᵢ(bⱼ) = δᵢⱼ, not a second answer.
