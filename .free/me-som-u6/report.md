# me-som-u6: free-model run

- Book: `books/mech/me-som/me-som-u6.html`
- Status: ok
- Model calls so far: 23 (84,398 tokens in, 219,416 out), 7.1 minutes

## Checker

```
me-som-u6.html: 7 chapters, 13342 words, 8 figures, 134 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 1, list of four assumptions: The fourth item, 'shear stress is proportional to the distance from the centre', is not an independent assumption; the same section derives it from 'plane sections remain plane' plus Hooke's law. A student meets it twice and cannot tell which statement is the starting point.
- ch 1 [low] Section 1, third paragraph (γ = rθ/L): The step from 'the radius is rotated by θ' to γ = rθ/L is skipped, and 'rotated by angle θ relative to the far end' is vague about which end moves relative to which.
- ch 1 [low] Figure (shear stress against radius): Each shaft is normalised by its own τmax, so both curves lie on the same line τ/τmax = r/R and the figure cannot show that, at the same torque, the hollow shaft's surface stress is 6.7% higher. The drawn hollow line adds nothing except a starting point.
- ch 1 [low] Section 3, first paragraph: 'A hollow shaft has a smaller J, so its maximum stress is slightly higher' is true only for the stated comparison (same outer diameter, same torque). Students often meet the opposite comparison, equal mass or equal area, where the hollow shaft is stronger, and may generalise the sentence wrongly.
- ch 2 [high] Section 2, exam trap 4 and quiz Q2: The chapter explains the stiffness check with q = θ/L = T/(G J), which does not contain L. So with this criterion the length of the shaft has no effect: a long shaft is neither more nor less likely to fail the stiffness check than a short shaft of the same T, G and J. The statements 'A long shaft can pass strength but fail stiffness because θ grows with L', the trap 'A long shaft can fail on θ/L although τmax ≤ τallow', and the Q2 answer 'Twist θ grows with L, so θ/L can exceed qallow' are therefore all wrong as written. In fact θ/L is independent of L, exactly like τmax = T r/J. What actually makes a shaft fail the twist limit is a small J (thin or small-diameter section), not a large L.
- ch 2 [low] Section 3: The sentence 'Some syllabi call U the torsional strain energy' adds nothing, because the formula was already introduced in this chapter as the torsional strain energy U. It reads like an unverified claim about other syllabi.
- ch 3 [high] Section 3, last paragraph: The line 'When two shafts are joined in series or parallel, the torque splits or adds' is wrong for the series case. Shafts in series carry the same torque through each of them; only the angles of twist add. Torque adds only for shafts in parallel.
- ch 3 [low] Quiz Q4: The cube root is truncated. d³ = 2.43 × 10⁻⁵ m³ gives d = 0.02897 m, which rounds to 29.0 mm, not 28.9 mm.
- ch 4 [high] Exam traps, trap 3: The claim 'Mixing 50 mm with 80 GPa gives an answer off by 10⁹' is numerically wrong. Using d in mm (J too big by 10¹²) and G in GPa (too small by 10⁹) gives a net error of only 10³, i.e. the twist comes out 1000 times too small: 800/(80 × 6.136 × 10⁵) = 1.63 × 10⁻⁵ rad instead of 0.0163 rad. The two unit slips partly cancel, so the stated factor of 10⁹ misleads a student who checks it.
- ch 4 [low] Figure caption: The caption says 'The upper branch is series ... The lower branch is parallel', but the spec is {'direction': 'down'}, so series and parallel appear as two side-by-side branches, not upper and lower. A student looking at the picture will not find an upper or lower branch.
- ch 4 [low] Section 3: 'such as a stepped axle' is given as an example of a tapered shaft. A stepped axle has abrupt changes of diameter and is analysed as shafts in series, not as a taper with a continuous d(x).
- ch 4 [low] Beyond: 'but G is not isotropic' is loosely worded: isotropy is a property of the material, not of G. In a carbon-fibre tube the shear modulus differs along the fibres and across them.
- ch 5 [low] Section 1, paragraph on maximum stress location: The sentence 'Both stresses are maximum at the outer surface and zero at the centre for torsion' reads as if 'zero at the centre' applies to both stresses, and puts the qualifier in the wrong place. A student can take away that bending stress vanishes at the centre in every direction rather than only on the neutral axis.
- ch 5 [low] Section 1, second sentence: 'At a section where both are largest' suggests M and T always peak at the same cross-section. In real shafts the maximum bending moment and the maximum torque usually occur at different sections, and the check must be made where the combination is worst.
- ch 5 [low] Section 3, figure and worked example: The flowchart is drawn as a design path ending in 'd = 60 mm' from d³ = 16Te/(πτallow), but the worked example below it treats 60 mm as a given and instead works forward to the stresses. Same numbers, but the two directions are mixed without a word of explanation, and the flowchart shows only the shear check, not the normal-stress check with Me.
- ch 6 [high] Section 1: With L = πDn as the total wire length, θ = T L/(GJ) is the total twist of all active coils, not 'the twist of one coil'. The next line δ = Rθ uses total twist, so the wording makes the derivation inconsistent.
- ch 6 [high] Section 2: The sentence 'The component in the coil plane twists ... normal to the coil plane bends' is reversed relative to the formulas. At α=0 the axial load is normal to the coil plane and causes torsion, not bending; the component along the wire axis causes the bending M=WR sinα.
- ch 6 [high] Exam traps: Counting total coils instead of active coils makes n larger, so it overestimates δ and makes the spring seem softer (lower k), not stiffer. This also contradicts Quiz Q6.
- ch 7 [high] Section 2 (deflection formula), worked example 1, and quiz Q5: The deflection formula δ = WL³/(4nEbt³) is the value for a spring whose leaves are all of full length. The chapter's own lead and Section 1 describe the standard semi-elliptic spring with shorter graduated leaves, for which the textbook result is δ = 3WL³/(8nEbt³) (1.5 times larger; equivalently an effective leaf count of 2n/3). The step 'I = nbt³/12' is used as if the section were constant from clamp to eye, which is false once the leaves are graduated, so the example deflection 30.5 mm is about one third too small (correct value 45.8 mm) and Q5's 61.0 mm is wrong too.
- ch 7 [low] Section 2, assumption sentence: 'The formula assumes equal leaves' is vague; a student cannot tell whether it means equal length, equal thickness or equal load sharing, and it hides the point that graduation changes the deflection by 50 per cent.
- ch 7 [low] Lead: 'spreads bending stress' is loose; a spring does not spread stress, it distributes the bending moment over more material and so lowers the stress.
