# m-de-u4: free-model run

- Book: `books/common/m-de/m-de-u4.html`
- Status: ok
- Model calls so far: 17 (55,344 tokens in, 150,899 out), 4.2 minutes

## Checker

```
m-de-u4.html: 6 chapters, 10520 words, 7 figures, 115 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Quiz Q6: The answer stops at p = q. That relation is true for the family, but it was obtained without using the original relation, so z has dropped out and the PDE is weaker than the proper one: the general solution of p = q is z = φ(x+y), which contains the family only as a small subfamily. It also contradicts the chapter's own rule in Section 2 (one constant → use one derivative equation plus the original relation) and the rule that the formed PDE contains z.
- ch 1 [low] Section 2: The rule is stated too loosely in two places: 'The two new equations contain a and b' is not always true (for z = a(x+y) + b the x-derivative gives only a), and 'If only one constant remains, one derivative equation plus the original relation is usually enough' leaves the reader unsure when that fails. A student may think a constant that never appears in p or q can be removed at first order.
- ch 1 [low] Section 1: 'A first-order PDE contains x, y, z, p and q' reads as if all five must appear. Many first-order PDEs lack one or more of them (for example q = 0, or the answer p = q in Q6, which has no z).
- ch 2 [high] Exam traps, first trap: The reason given is inverted. Setting q=a in f(z,p,q)=0 does not remove the z dependence: the equation still contains z, as f(z,p,a)=0. The real reason the type-2 substitution is needed is that q=a alone leaves an equation mixing z, p and the parameter a, which is not an ODE in one variable; the substitution u=x+ay makes z depend on u alone so the PDE becomes an ODE.
- ch 2 [low] Section 1, definition of nonlinear: "p or q appears in a power, product, or function" is ambiguous. A student can read "product" as p multiplied by x, and then classify xp+q=z as nonlinear, although that equation is linear (later in the chapter Pp+Qq=R is called linear).
- ch 2 [low] Section 2, type 2 paragraph: "Moving frame" is not a standard name for the change u=x+ay in this topic, and it may suggest a coordinate transformation of the whole surface rather than the assumption that z depends on the single variable u.
- ch 3 [low] Lead: The lead says 'z is the unknown surface'. z is the unknown function of x and y; only its graph is a surface. Section 1 gives the correct wording, so the lead contradicts it slightly.
- ch 3 [low] Lead: 'The method turns the PDE into two ordinary first integrals along characteristic curves' is garbled. The method turns the PDE into a system of ordinary differential equations; solving that system gives the two first integrals.
- ch 3 [low] Section 3: 'Any characteristic curve that touches an integral surface lies wholly on that surface' — 'touches' can be read as 'is tangent to', which is not the condition being stated.
- ch 3 [low] Figure, node d: The note 'd(x²+y²+z²)=0' drops the factor. With multipliers x, y, z the sum condition gives x dx + y dy + z dz = 0, which is ½d(x²+y²+z²) = 0.
- ch 3 [low] Quiz Q7: The independence check and the determinant are correct, but u = x − y and v = x + y can never both be first integrals of a non-degenerate Lagrange equation: P u_x + Q u_y + R u_z = 0 forces P = Q, and the same for v forces P = −Q, so P = Q = 0. The pair is artificial and may confuse a student who tries to write down the PDE.
- ch 4 [low] Lead and Section 1: The second relation is described as one 'between p and q'. In general the Charpit integral f = a also contains x, y and z, so a student may expect a purely algebraic relation in p and q only.
- ch 4 [low] Section 1, last paragraph: Clairaut-type z = p x + q y + f(p, q) is listed as a case where the standard substitutions of 4.2 fail, but Clairaut's form is itself a standard case usually solved by differentiating with respect to x and y. The student may be unsure which route is expected.
- ch 4 [low] Section 2, note on minus signs: 'They come from the characteristic equations and flip signs when F_z is nonzero' is vague. The sign of each term is fixed by the denominator F_x + p F_z; there is no separate rule about F_z flipping anything.
- ch 4 [low] Quiz Q3: The answer writes b = √(1 − a²) without stating that a must satisfy a² ≤ 1, and it silently drops the negative root q = −√(1 − a²).
- ch 5 [low] Section 1: The strip is described as 'a narrow ribbon of surface'. At this stage no surface is known yet; the strip is data (a curve plus a tangent plane at each of its points), and calling it a piece of surface can mislead a student into thinking the surface is already available.
- ch 5 [low] Section 1: 'Here z is the unknown surface' is loose: z is the unknown function z(x,y); it is the graph of z that is the surface.
- ch 5 [low] Section 2 (also quiz Q4): The non-characteristic test is written only as x₀′F_q − y₀′F_p ≠ 0. The reader is not told where it must hold; a single nonzero value at one point does not give a surface near the whole curve.
- ch 5 [low] Section 2: 'Two equations in two unknowns usually give one or two branches' is vague and slightly wrong: F=0 together with the strip condition can give one solution, two solutions, more, or none, depending on F.
- ch 5 [low] Worked example 1: Each step carries a doubled label ('step 1: 1. Write ...', 'step 2: 2. Strip condition ...'). This is a formatting slip that reads badly on a phone.
- ch 6 [high] Quiz Q5: The premise says flatly that an integrable Pfaffian is not exact. Many integrable Pfaffians are exact (worked example 1 and Q3/Q7 are). This contradicts Section 2's own statement that exact implies integrable, and it teaches a false rule.
- ch 6 [low] Section 1, first line of the test: A leftover placeholder token '[formula]' sits right before the integrability condition, so the reader sees 'is: [formula] P(∂R/∂y − …)=0'.
- ch 6 [low] Figure: The flowchart moves straight from 'Integrability test' to 'Exact?' with no failure branch, so it suggests every Pfaffian passes the test and gets a surface. The Lead and Section 1 both say a nonzero result means no surface.
- ch 6 [low] Exam traps, fifth trap: 'A zero test gives local surfaces; a global surface may fail where P, Q, R are not smooth' is muddled: the test does not give surfaces, it only guarantees a local integrating factor.
- ch 6 [low] Section 2, geometry paragraph: The reference to the auxiliary system of 4.3 is plain text, so on a phone the student cannot jump to that chapter.
- ch 6 [low] Section 1, last paragraph: 'It lets a non-exact equation be integrable' is confusing: a test cannot make an equation integrable.
