# ae-struct-u4: free-model run

- Book: `books/aero/ae-struct/ae-struct-u4.html`
- Status: ok
- Model calls so far: 28 (120,347 tokens in, 300,242 out), 9.6 minutes

## Checker

```
ae-struct-u4.html: 6 chapters, 12004 words, 7 figures, 126 KB
OK
```

## For the reviewer

- chapter 2: the figure cannot be drawn: note "sum of two terms" runs off the right edge; shorten it
- chapter 2: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [high] Section 2, asymmetric section paragraph: The rule 'use the tension-side value to check yielding' is wrong as a general rule. Yielding is set by the largest distance from the neutral axis, whichever face that is; in many sections (an inverted T, an I-beam with a big bottom flange) the compression face is farther, so compression governs yielding. The same sentence also says such a section 'has two values of y_max', which contradicts the earlier definition of y_max as the distance to the farther face.
- ch 1 [low] Section 1, assumptions and derivation list: The five assumptions and the five derivation steps run on as one continuous bullet list, so 'Eliminate R between steps 2 and 4' is ambiguous: a reader counting from the top of the list lands on the wrong bullets.
- ch 1 [low] Section 3, second paragraph: 'This is the one Poisson effect that a bending member cannot avoid' reads as if the anticlastic curl itself cannot be avoided, which the next paragraph contradicts.
- ch 1 [low] Section 3, last paragraph: 'Simple bending theory is accurate for stiffened wing boxes and crude for a plain strip' overstates the case. The free anticlastic curl barely alters the direct stress, so σ = M y / I stays close for the plain strip too; what differs is the deformation and the transverse stress.
- ch 1 [low] Section 1 and Section 2 cross-references: Forward references appear as plain text: '(see 4.4)', 'as chapter 4.2 shows', '(see Unit 6, Plates, Buckling and Composite Structures)'. On a phone the reader cannot jump to them.
- ch 2 [high] Section 2, sentence after the neutral-axis formula ("When I_xy ≠ 0, this line is not perpendicular to the moment vector"): Wrong geometric statement, and it contradicts the lead of the chapter. In symmetric bending about a principal axis the neutral axis lies along the moment vector (M_x only, I_xy = 0 gives α = 0, i.e. the neutral axis is the x-axis, the same line as the moment vector). So the neutral axis is never perpendicular to the moment vector; what is true is that it is no longer perpendicular to the plane of the applied moment (it no longer lies along the moment vector). A student will memorise "perpendicular becomes non-perpendicular" and get the geometry backwards.
- ch 2 [high] Quiz Q6 (question and answer): Both the question ("why is the neutral axis not perpendicular to the moment vector") and the answer ("the two directions coincide only when I_xy = 0") are false. With I_xy = 0 and both M_x and M_y acting, tan α = −(M_y I_xx)/(M_x I_yy) while the moment vector has tan β = M_y/M_x, so the two directions do not coincide unless the moment acts about one principal axis only. Conversely, for special combinations of M_x and M_y they do coincide even when I_xy ≠ 0. The stated rule is wrong in both directions.
- ch 2 [low] Quiz Q7, answer: The sign statement is reversed under the chapter's own formula tan 2θ_p = −2I_xy/(I_xx − I_yy). With I_xx = I_yy and I_xy > 0, 2θ_p → −90°, so θ_p = −45°, and it is this −45° that gives I_u = I + I_xy = I_max. Saying "the sign follows the sign of I_xy" pairs I_max with the wrong angle.
- ch 2 [low] Section 3, principal-axes formulas: The two moment-resolution formulas and the two-term stress formula depend on which way the axes are rotated, but the coordinate rotation is never written down. A reader cannot tell whether u = x cos θ_p + y sin θ_p or the mirror version, and so cannot reproduce the signs of M_u, M_v and of the stress terms.
- ch 2 [low] Figure notes ("Ixy = 0.8e-6", "tan alpha = 0.667"): Quantities in the figure notes carry no units and use computer notation, while the text uses m⁴ and powers of ten.
- ch 2 [low] Section 2, sentence "Some syllabi call this the k method; others call it the neutral axis method": Neither name is a recognised textbook name for this formula; the claim about syllabi is unsupported and may confuse a student looking the topic up elsewhere.
- ch 3 [high] Section 2, paragraph after the tan β formula: The sentence is broken: "When the v-plane is the more flexible one, I_v  θ, so the tip swings away from the load line towards v." A number, the comparison and the inequality have dropped out, so a student cannot tell what condition makes β exceed θ.
- ch 3 [low] Worked example 1, step 4 and step 5 (same pattern in quiz Q3 answer): The arithmetic is written as "6400 / 8.40 × 10⁵ = 7.62 × 10⁻³ m". Read left to right as printed this gives 7.62 × 10⁵, not 7.62 × 10⁻³. The denominator is not bracketed, so a student copying the line gets a nonsensical answer.
- ch 3 [low] Section 1, definitions of I_u and I_v: The labels follow the plane, not the axis: I_u here means the second moment that governs bending in the u–z plane, which is the moment about the v axis (∫u² dA). Most textbooks, and the stress formula of Chapter 4.2, write I_u for the second moment about the u axis (∫v² dA). A student carrying this page into 4.2 will pair the symbols wrongly.
- ch 3 [low] Section 3, first sentence: "Other supports change only the constant in front" is imprecise: the deflected shape changes too (z²(3L − z)/(2L³) for a cantilever tip load, z(3L² − 4z²)/(48L³) for a central point load on a simple span). What stays true is that the two planes still share one shape, so the components still combine as vectors.
- ch 4 [high] Section 2, second-moment formulas: The I_xx, I_yy and I_xy sums omit the parallel-axis terms of the wall areas. As written, a wall offset from the centroid contributes only its own centroidal second moment. The worked example correctly adds A y² for the horizontal walls and A x² for the vertical walls, so the formula and the example disagree.
- ch 4 [low] Quiz Q6: The clause 'shear lag reduces stress in some booms, so the real load capacity is lower' is misleading. Shear lag lowers stress away from webs but raises it near webs; capacity falls because the peak stress is higher, not because some booms carry less.
- ch 5 [high] Section 1: The statement "If not, I_xy≠0 and the axes are not principal" is wrong as a general rule. A layout that is not symmetric about both centroidal axes can still give I_xy = 0: symmetry about even one centroidal axis is enough, because every boom at (x, y) has a partner at (−x, y) or (x, −y), so ΣA x y cancels. In that case the centroidal axes are still principal axes.
- ch 5 [low] Section 2: The positive sense of M_x and M_y is never defined, so a student cannot tell which way the neutral axis tilts or how to sign the moments taken from Unit 1. The worked example uses a convention (positive M_x gives tension at positive y, positive M_y gives tension at positive x) without saying so.
- ch 5 [low] Exam trap 1: "the skin's direct area moves the axis and tilts every stress" is unclear — stress is not tilted.
- ch 5 [low] Quiz Q5: The answer names the coupling terms but does not say what coupling means, so a student can reproduce the symbols without understanding them.
- ch 6 [high] Section 2: The stress is called self-equilibrating because 'resultant force is zero', but with curvature prevented the distribution σ(y) = −Eαk·y has zero force and a non-zero moment resultant (M = Eαk·I). It is therefore not self-equilibrating: a restraining moment must be supplied by the supports. A student will wrongly conclude that no moment is needed to hold the spar straight.
- ch 6 [low] Quiz Q3: The question says only 'curvature is prevented'. The quoted answer, EαΔT/2, is valid only if axial extension is also free; with the ends axially fixed the stress would be EαΔT at the faces. The answer also gives only a magnitude and does not say which face is in compression.
- ch 6 [low] Figure: The temperature (K) and stress (MPa) curves share one y-axis labelled 'value (K or MPa)'. Two different quantities in different units on one scale are easy to misread, for example taking the stress at mid-depth as 20 MPa instead of zero.
- ch 6 [low] Section 1: 'The beam bows toward the hotter face' can be read as the ends curling toward the hot side, which is the opposite of what happens. Also, ΔTmean is defined as the mid-depth rise, but the step ε0 = αΔTmean in Section 2 requires the area-average rise; the two coincide only for a section symmetric about mid-depth.

## Correction pass (21 Nov 2026)

Every chapter rewritten from the draft on one sign convention (y up, M_x positive when it puts positive y in tension) and every worked example, quiz answer and model answer computed in Python. All reviewer notes above are resolved; the restrained anticlastic stress is now +νσ (the draft had −νσ). AE3501 coverage: the k method, neutral axis method and principal axis method are each taught and worked on one Z-section (all give 171.4 MPa), and deflection under unsymmetrical bending is worked by the curvature equations and by principal axes. New examples: T-section with two section moduli, Z-section by three methods, Z cantilever deflection (21.16 mm sideways, 14.11 mm down) and a Python deflection-shape program, angle and Z section-property tables, an unequal-boom wing box under lift and drag, a heated boom in a free four-boom beam. Six figures hand-drawn from the worked examples (pipeline/claude_figs/ae_struct_u4.py), 13 full model answers. University-hosted links dropped (DoITPoMS, MIT OCW, NPTEL). check_book.py --render: OK.
