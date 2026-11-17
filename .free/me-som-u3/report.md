# me-som-u3: free-model run

- Book: `books/mech/me-som/me-som-u3.html`
- Status: ok
- Model calls so far: 23 (92,853 tokens in, 174,700 out), 7.0 minutes

## Checker

```
me-som-u3.html: 5 chapters, 11223 words, 6 figures, 113 KB
OK
```

## For the reviewer

- chapter 1: the figure cannot be drawn: tree is too wide (7 leaves); use fewer leaves or shorter labels
- chapter 1: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [high] Section 3 (self weight formula) and Quiz Q4 answer: The chapter defines w as a UDL intensity in kN/m everywhere, but the self-weight rule w = ρ A g with ρ in kg/m³, A in m² and g in m/s² gives N/m, not kN/m. A student using ρ = 2500 kg/m³ and A = 0.1 m² would write w = 2452.5 kN/m instead of 2.45 kN/m.
- ch 1 [low] Section 4, quick count paragraph: "Note that a fixed end on its own already uses up all three equations" is misleading. A fixed support does not consume equations; it supplies three unknowns, which is exactly the number a cantilever has.
- ch 1 [low] Section 3, applied couple: "an eccentric load replaced by a force plus a moment" is given as an example of a pure couple, but that replacement produces a force and a couple together, not a pure moment.
- ch 2 [low] Worked example 1, dry run block: The printed output does not match the table above it. The table rows are W = 30 kN, R_B = 21.67 kN, R_A = 28.33 kN, but the output shows 21.67, 28.33, 170.0: the 30 is missing and the 170.0 appears from nowhere.
- ch 2 [low] Section 1, first paragraph after the lead: The sentence 'The equations ΣF = 0 and ΣM = 0 hold only for a body with every contact removed' is misleading. Equilibrium holds for the real beam too; what the free body diagram does is make every contact force an explicit external arrow with a known line of action.
- ch 2 [low] Worked example 1, step 6: '28.33 × 6 = 170 kN·m' is written as an exact equality, but 28.33 is rounded; the product is 169.98. A student copying the rounded number will not get 170.
- ch 3 [low] Exam traps, item 4: The wording 'a point load at the free end is not included in the shear just left of the free end' reads as if V just left of B is not 10 kN. In the worked example V at B is exactly the 10 kN end load; the load simply does not sit on the kept left piece when the cut is taken at x = 4.
- ch 3 [low] Quiz Q7: The answer gives V = wx as a 'magnitude' only, but the chapter uses one sign convention throughout and V is genuinely positive here (upward on the left face of the kept right part). Calling it a magnitude contradicts the question, which asks how the expressions change, and hides the fact that V = −dM/dx when x is measured from the free end.
- ch 3 [low] Quiz Q1: The answer uses w(L − x)²/2 without saying where x is measured from; a student measuring x from the free end gets a different expression and may think the answer is wrong.
- ch 4 [high] Section 1: "the free end carries zero moment but not zero shear" is wrong in general. At a free end with no concentrated load or applied moment there, the shear force is also zero (in the worked example V falls from +20 kN at B to 0 at C). Stating that the free end carries shear teaches a false rule.
- ch 4 [high] Section 2, curve-crossing paragraph: "The shear force crosses zero twice in general ... The other crossing lies on the overhang" is wrong. On an overhang the shear does not normally pass through zero; it runs from a finite value at the support down (or up) to zero at the free end. In the chapter's own worked example V on the overhang is 60 − 10x, i.e. +20 kN at B falling to 0 at C, with no crossing. Only one genuine interior zero crossing exists (x = 1.5 m).
- ch 4 [high] Section 2, SFD drawing bullet: The instruction says "walking left to right" but then gives a right-to-left sequence: start at 0 at the free end, drop by the overhang load, jump by RB, jump by RA. Walking left to right on this beam you meet A first, so the jumps come out in the wrong order and the diagram would not close at zero, contradicting the trap that says it must.
- ch 4 [high] Quiz Q7: The answer "Twice in general ... Each zero crossing adds another contraflexure" is wrong and contradicts the exam trap "Calling the zero-shear point the contraflexure point". A zero in shear marks a maximum or minimum of bending moment, never a contraflexure. Also, for a beam overhanging equally on both sides with a UDL over the whole length, the shear crosses zero only once (at mid-span), not twice.
- ch 4 [low] Section 2, last paragraph: M(x) = RAx − wx²/2 is written as if it holds for the whole beam. It holds only between A and B (0 ≤ x ≤ L); past B the section equation must also include RB(x − L).
- ch 4 [low] Worked example 1, step 9: The roots x = 0 and x = 3 m are both listed, but x = 0 is the pinned end A, where the moment is zero because it is an end, not because the curvature reverses. Only x = 3 m is a point of contraflexure. A student may quote both as contraflexures.
- ch 4 [low] Section 3, sign paragraph: "Loads on the left overhang sit at negative x and give a positive moment about A" is only true under one moment sign convention, which the chapter never states. A student using the opposite convention will get a sign clash and think the text is wrong.
- ch 4 [low] Exam traps, last trap: "The SFD must close at zero at both free ends" assumes two overhangs. A beam with one overhang has a single free end; at A the diagram jumps from 0 by RA, it does not close at zero.
- ch 4 [low] Beyond: "the contraflexure point as the place where lap lengths must not be placed" clashes with the common textbook advice that lap splices are placed where the bending moment is low, which is exactly near contraflexure. Codes restrict lap positions for their own reasons, so the flat statement can mislead.
- ch 5 [low] Section 1, moment equilibrium: The step from 'the bending moments on the two faces differ by dM' to 'dM = V dx' hides the signs. A student cannot see why the right-face shear moment and dM oppose each other, and why the left-face shear contributes nothing.
- ch 5 [low] Section 1 and lead: The three relations are written as if they hold everywhere, but they hold only between concentrated loads and couples, where w is a continuous function. At a point load or couple the derivatives do not exist and jumps apply.
- ch 5 [low] Section 2: 'the SFD is horizontal where w = 0' is only true where w is zero over a finite length. At an isolated point where w = 0 (for example right under a point load) the shear diagram is not horizontal.
- ch 5 [low] Quiz Q3: The answer gives V = 5 kN without stating the section or the sign convention, so a student measuring x from the free end and using V = dM/dx gets −5 kN and thinks the answer is wrong. The sign of M = −10 kN·m is also left only as the word 'hogging'.
- ch 5 [low] Quiz Q6: 'The BM slope is unchanged by the couple except through the jump' is confusing. The slope dM/dx equals V, which is continuous at the section, so the slope is the same immediately left and right of the couple; only M itself jumps.
- ch 5 [low] Quiz Q7: The answer says 'it may be an inflection or flat, and end or support values must be compared'. That weakens the logic: if V = 0 at a point without changing sign, M has a horizontal point of inflection there and is not a local extremum at all, so no comparison is needed to reject it as a maximum.
- ch 5 [low] Figure spec: The plotted point lists carry unrounded floating-point values such as 3.9000000000000004, 17.988749999999996 and -11.399999999999999, which will show as ugly readouts if the plot labels points.
