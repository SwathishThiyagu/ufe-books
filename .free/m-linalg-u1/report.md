# m-linalg-u1: free-model run

- Book: `books/common/m-linalg/m-linalg-u1.html`
- Status: ok
- Model calls so far: 18 (63,078 tokens in, 152,540 out), 5.3 minutes

## Checker

```
m-linalg-u1.html: 5 chapters, 9994 words, 6 figures, 103 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Quiz Q7: The question and answer are wrong. Each system as given has a single equation in two unknowns, x + y = 3 and x + y = 5, and a single equation like that always has infinitely many solutions, so both are already consistent. The stated answer is also wrong in its second case: it says adding x + y = 5 to the system x + y = 5 makes it inconsistent because the line is 'parallel to x + y = 3', but x + y = 5 added to x + y = 5 is the same line twice, giving infinitely many solutions, still consistent. No inconsistency appears anywhere in the answer.
- ch 1 [low] Worked example 1, output line: The output block shows bare numbers 6, 5, 1 with no label. A reader cannot tell whether these are the b entries, the left-hand sides, or the solution values.
- ch 1 [low] Section 3: 'each equation ax + by = c is a straight line' silently assumes a and b are not both zero; if a = b = 0 the equation is 0 = c and has no line.
- ch 1 [low] Section 3, last paragraph: 'as rank and consistency shows' reads awkwardly and points to another chapter without a link, so the student cannot jump there.
- ch 2 [low] Section 2: 'fully reduced normal form' is not a standard textbook name for RREF; a student may meet it nowhere else and think it is a separate object.
- ch 2 [low] Section 2: 'Entries above a pivot and to its right may be anything at all' reads as if only entries that are both above a pivot and to its right are free. A student can misread this as a restriction on the pivot row or pivot column.
- ch 2 [low] Section 3, formula box: The pivot row is written R_j in Section 1 and in the 'Clear below' bullet, but R_p inside the formula. Three symbols for two roles confuse a reader who is checking the multiplier against the earlier rule.
- ch 2 [low] Section 3, after the formula: 'Scaling a pivot row to 1 first keeps the arithmetic in small numbers' is misleading. Dividing a row by its pivot usually creates fractions (pivot 2 in [2, 1, 3] gives [1, 0.5, 1.5]), so the numbers are not necessarily smaller.
- ch 2 [low] Exam traps, fourth trap: The trap does not say which row '2R₁ − R₂' is applied to. Read as a replacement of row 2 it is legal and only flips a sign; the error only exists when it is applied to row 1. A student can miss the point.
- ch 2 [low] Beyond: 'partial pivoting picks the largest available entry' — the sign is irrelevant; picking a large negative entry would defeat the purpose.
- ch 3 [low] Section 2, bullet on reading the answer (and lead): It says the matrix reaches RREF and 'x_k = b′_k is read straight from the last column'. That holds only when every column has a pivot. If a column is skipped, its entry stays non-zero in the pivot rows, so the pivot unknowns come out as x_k = b′_k minus terms in the free variables — the chapter's own worked example gives x = 3/2 − t/2, not x = 3/2.
- ch 3 [low] Section 3, first formula box: 'If r = n there is one solution' is missing the consistency condition. An overdetermined inconsistent system, for example rows [1 0 | 0], [0 1 | 0], [0 0 | 1], has r = n = 2 and no solution at all.
- ch 3 [low] Section 3, partial pivoting paragraph, and quiz Q8: It claims that with partial pivoting 'entries do not blow up and rounding error stays small'. The |m| ≤ 1 bound is correct, but entry growth is not ruled out: partial pivoting still allows a growth factor as large as 2^(n−1) for specially built matrices. The chapter's own 'Beyond' section mentions the growth factor, so the two parts disagree in tone.
- ch 3 [low] Quiz Q2: The question asks for 'the two properties' of RREF, but the answer lists four conditions and still leaves one out: the leading 1 of each row must lie to the right of the leading 1 of the row above (the staircase condition). The question and answer do not match.
- ch 4 [low] Section 2, the boxed test and the sentence below it: The two consistent cases are written as 'r = r′ = r < n' and 'r = r′ = r < n'. The chain 'r = r′ = r' is a tautology (r always equals r), so a student reads a condition that says nothing and may not see that the real condition is 'the common rank is less than n'. The notation also repeats the symbol r in two roles: the common value and the name of rank A.
- ch 4 [low] Section 1, minor-based definition: 'An r×r minor on pivot rows and pivot columns is nonzero' is loose: pivot rows are rows of the echelon form, not necessarily rows of A, so a student may think the nonzero minor is read straight off A without eliminating first.
- ch 5 [low] Section 1, definition of the multiplier: Writing ℓik = aik/akk uses the original entries of A, but the multipliers are computed from the entries that survive after the first k−1 elimination steps. A student who plugs original A entries into this formula will get wrong multipliers (for example in the worked example, entry (3,2) after step 1 is 3, not 7).
- ch 5 [low] Section 2, loop bullets: The two bullets 'For i = k+1 to n, set ℓik ...' and 'For j = k to n, replace U[i][j] ...' sit at the same level, so they read as two separate loops. Taken that way, all multipliers are computed from untouched rows before any row is updated, which gives wrong factors.
- ch 5 [low] Section 2, closing line of the algorithm: 'After the last column, A = LU' is unclear. The k-loop stops at column n−1, so there is no 'last column' being processed, and it does not say what the arrays hold at the end.
- ch 5 [low] Section 1, Crout form sentence: 'Crout form puts the pivots in L instead' is incomplete: in Crout form L is a general lower triangular matrix and U is unit upper triangular with 1s on its diagonal. Without that, a student cannot tell what Crout actually looks like.
