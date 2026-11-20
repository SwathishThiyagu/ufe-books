# me-design-u5: free-model run

- Book: `books/mech/me-design/me-design-u5.html`
- Status: ok
- Model calls so far: 23 (88,286 tokens in, 188,289 out), 5.2 minutes

## Checker

```
me-design-u5.html: 7 chapters, 14892 words, 8 figures, 147 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Lead: The lead says oil, grease, graphite powder and synthetic fluid 'all do the same four jobs', including 'carry heat away' and 'seal out dirt'. Section 2 then states that grease 'cannot carry heat away', and a dry graphite film carries no heat and seals nothing. A student reading only the lead gets a wrong generalisation.
- ch 1 [low] Section 3, paragraph on why two viscosities exist: 'The flow of oil into the gap, and its inertia, depend on μ/ρ' is loose. Inertia itself grows with density ρ; what depends on μ/ρ (that is, on 1/ν) is gravity-driven flow rate and the ratio of inertia force to viscous force. As written, a student may think a denser oil has less inertia.
- ch 2 [low] Section 3 table, row 'Friction coefficient', and Section 4 hydrodynamic bullet: The same regime gets two different ranges: the table gives 0.002 to 0.02 for a full film, while Section 4 gives 0.001 to 0.01 for hydrodynamic lubrication. A student revising from both places will not know which range to quote.
- ch 2 [low] Section 2, cylindrical roller bearing bullet: 'takes no axial load unless flanges are added' suggests flanges are an optional add-on. In a real bearing the flanges are part of the rings; it is specifically the flanged types, with ribs on both rings, that take a little axial load, and only in one direction.
- ch 2 [low] Quiz Q1: The question asks for lining materials, but cast iron is normally used as a solid bush, not as a thin lining bonded or cast into a steel shell like babbitt and bronze. The three items are not all of the same kind.
- ch 2 [low] Section 4, cross-reference to Chapter 5.3: The other chapter is named in plain text, so on a phone the reader cannot jump to it, unlike every other cross-reference in the book.
- ch 3 [low] Quiz Q4 answer: "The journal centre moves closer to the bearing" is ambiguous. The journal centre moves away from the bearing centre (the geometric centre of the sleeve) and toward the bearing surface; a student can read it the wrong way round.
- ch 3 [low] Section 3, clearance effects: "A larger c raises oil flow and hmin" states h_min as always rising with clearance. In practice h_min improves with clearance only up to an optimum; past that, the extra flow cannot remove the heat, viscosity drops and h_min falls again. The sentence as written is a half-truth.
- ch 4 [high] Exam traps, second bullet (πDL): The trap says the projected area is 'the rectangle you see looking along the shaft'. Looking along the shaft axis you see the circular cross-section of the journal, not a rectangle. The L × D rectangle is seen in side view, looking perpendicular to the axis. A student would memorise the wrong picture of why πDL is wrong.
- ch 4 [low] Section 2, naming paragraph: 'Some syllabi call S the bearing characteristic number' is misleading. The bearing characteristic number (also called the bearing modulus) is normally defined as μn/p alone, without the (r/c)² factor; S with the square is the Sommerfeld number. The sentence invites students to drop the square.
- ch 4 [low] Section 2, typical values: 'r/c between 500 and 1500' — the usual quoted band for machined bearings is r/c ≈ 500 to 1000 (c/r ≈ 0.001 to 0.002); 1500 is at the very loose end and is not typical.
- ch 4 [low] Section 3 and quiz Q5: Eccentricity and eccentricity ratio are used from Section 3 onward without a definition, but the symbol and its link to film thickness are needed to follow 'the journal rides higher'.
- ch 4 [low] Section 2, second formula: 'every length cancels inside the group' is not accurate: L, D and the r/c lengths do not cancel among themselves; they pair with W (through p = W/LD) to make the whole expression dimensionless.
- ch 5 [high] Quiz Q5: The pair S = 0.15, ε = 0.74 is impossible. Eccentricity falls as the Sommerfeld number rises, and Example 1 already reads ε = 0.62 at the lower S = 0.031 for the same L/D = 1. A student using this quiz answer will learn the trend backwards and will get impossible chart readings.
- ch 5 [low] Section 1, second paragraph and table: The text says 'read up to six outputs' but the table lists only five (eccentricity ratio, film thickness ratio, friction variable, flow variable, temperature rise). The chart set also carries an attitude angle and a side-leakage ratio, which are missing from the count and from the table.
- ch 5 [low] Section 1 lead and Section 2, second bullet: The Sommerfeld number S is used throughout but never defined here; a student revising from this unit alone does not know what to compute or what P means.
- ch 5 [low] Section 2, flow bullet: It says 'read the flow variable to get the oil flow Q' but gives no way to turn the number into Q, so the student cannot size the pump.
- ch 5 [low] Section 1, table row 'Flow variable': The row claims the flow variable gives both 'oil needed and side leakage', but Q/(r c n L) gives only the total flow. Side leakage comes from a separate chart that gives the ratio Q_s/Q.
- ch 5 [low] Figure and its caption: The caption calls it a 'design loop', but the figure is a straight chain with no return path, and the arrow from h_min to friction suggests friction is found from h_min. Friction is read from the charts at the same S and L/D, independently of h_min.
- ch 6 [low] Section 3, variable load and speed formula: The formula is printed without exponents or markup: 'Pe = [ (P1p n1 t1 + P2p n2 t2 + …) / (n1 t1 + n2 t2 + …) ]1/p'. A student reads P1p as a product, and neither Pe nor Pi is defined, nor are their units.
- ch 6 [low] Section 1, definition of C0: C0 is defined using '0.0001 times the ball diameter', but this section covers roller bearings too, where the reference is the roller diameter, not a ball diameter.
- ch 7 [high] Quiz Q3 answer: The explanation of the error is inverted. Putting hours (10 000) in place of L10 (720) makes L10^(1/3) bigger, not smaller: 10 000^(1/3) ≈ 21.5 against 8.96. So the computed C_req comes out far too large, and the bearing is over-sized, not under-sized as the answer claims.
- ch 7 [low] Worked example 1, step 1: The value of e is never given, so the student cannot check the claim that F_a/F_r = 0.4 is above e. The statement in the question ('the catalogue gives X = 0.56 and Y = 1.5, since F_a/F_r is greater than e') also assumes the result before the ratio is tested.
- ch 7 [low] Worked example 1, question and step 8: The question says the bearing 'may see shock', but step 8 uses s0 = 2 'for ordinary running'. Section 3 of the same chapter says to use 3 or more where shock is expected, so question and solution contradict the text.
- ch 7 [low] Figure caption: The caption says 'the highlighted box is the required rating', but the accent (highlight) is set on the equivalent load P node; C_req carries the 'live' style. A reader looking for the highlighted box is pointed at the wrong one.
