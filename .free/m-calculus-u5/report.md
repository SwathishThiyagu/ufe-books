# m-calculus-u5: free-model run

- Book: `books/common/m-calculus/m-calculus-u5.html`
- Status: ok
- Model calls so far: 22 (72,224 tokens in, 180,082 out), 5.8 minutes

## Checker

```
m-calculus-u5.html: 5 chapters, 9162 words, 6 figures, 98 KB
OK
```

## For the reviewer

- chapter 4: a python program's shown output was replaced by its real output; check the text around it
- chapter 4: worked example 1: the worked example states [1.5] but recomputing it gives [1.0, 1.0]; fix the steps and the answer so they match the correct values
- chapter 5: the figure cannot be drawn: too many columns for a left-to-right diagram; use direction "down"

## Reviewer notes (after any revision)

- ch 1 [low] section 2 body text and quiz Q1, Q4: The integral limits are written inline as plain letters, e.g. "∫ab f(x,y) dx" and "∫cd (∫ab f(x,y) dx) dy". On a phone a student can read "∫ab" as the integral of the product a·b, and "∫cd" as ∫(cd). The tags <sub> and <sup> are available and the rest of the chapter already uses them (∫<sub>a</sub><sup>b</sup>).
- ch 1 [low] figure: The figure states a final value of 4 for "the double integral" over R = [0,2]×[0,1] but never says which function is being integrated. A number without an integrand is meaningless, and a student may think the integral of any function over that rectangle is 4.
- ch 1 [low] quiz Q4: "signed area of the slice of the surface z = f(x,y) along the line at that fixed y" calls the quantity a slice area. The slice of the surface is a curve; the integral is the area between that curve and the x-axis in the plane y = constant. As written, a student may think the inner integral gives the arc length or the area of the curve itself.
- ch 2 [low] Section 2 (four steps) and worked example, step 3: The chapter says the same region can be described as type I and type II, but never warns that some regions fail the new description and must be split into two integrals before the order can be changed. A student meeting such a sketch will force a single pair of limits and get a wrong answer.
- ch 2 [low] Worked example 1, step 4: The line 'I = ∫₀¹ [x e^(y²)] from x=0 to x=y dy' puts the dy inside the bracket, so it reads as if dy is part of the evaluated expression rather than the outer differential.
- ch 3 [low] Lead: The lead says integrals over round regions 'become ordinary one-variable integrals'; a double or triple integral becomes two or three nested one-variable integrals, not one, and a student may read it as a single integral.
- ch 3 [low] Section 1: 'Set the r-limits from the nearest and farthest points of the region' is only true for regions that are disks, sectors or rings about the origin, which is the stated scope, but the sentence reads as general. For a disk shifted off the origin, e.g. (x−1)²+y² ≤ 1, nearest and farthest points give 0 ≤ r ≤ 2, which is wrong because r then depends on θ.
- ch 3 [low] Section 3: 'When the integrand depends only on ρ, the θ and φ integrals separate and give 4π' is correct only because the sinφ of the Jacobian is inside the angular integral; as written, a student may think ∫dθ dφ alone equals 4π.
- ch 4 [high] Worked example 1, code block: The code prints 1 and 1.0, but the triple integral is 3/2. middle_exact(z)=1+z is the result after the y-integration; the outer z-integral needs ∫₀¹(1+z)dz, not middle_exact(1)-middle_exact(0). The unused middle helper also returns 1, not 1+z.
- ch 4 [high] Quiz Q5 answer: It says the constant z limits 0 to 1 ignore the parabolic floor. In the student's order dx dy dz, z is outermost, and z=0 to 1 is the correct overall range. The error is the constant x,y limits 0 to 1: at fixed z the cross-section is x²+y²≤z. The answer's alternative order is valid, but the diagnosis of the z limits is wrong.
- ch 4 [high] Exam traps, first bullet: The claim 'Only the outermost variable has constant limits' is false. In Quiz Q4, the middle y-limits 0 to 1 are constant in a non-box solid. Inner limits may be constant or may depend on outer variables.
- ch 4 [high] Worked example 1, step 1: It says 'order dz dy dx, integrating x innermost'. Under standard notation dz dy dx makes z innermost; the steps actually use x innermost, y middle, z outer, i.e. dx dy dz.
- ch 4 [low] Section 1, non-box paragraph: The phrase 'not a box, a slab, a cylinder or a pyramid, for example' is ambiguous: it can read as excluding all those shapes rather than giving examples of non-box solids.
- ch 5 [high] Quiz Q5: The disk x² + y² ≤ 2 has radius √2, not 2. The answer uses the limits 0 ≤ r ≤ 2 and so gets the wrong inner value (10 instead of 5) and the wrong volume 20π ≈ 62.832 cubic units.
- ch 5 [low] Section 3, first sentence: 'Circular bases are why polar coordinates exist' is an overstatement that can mislead: polar coordinates are a general change of variables, useful for many things beyond circular bases.
