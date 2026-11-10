# c-graphics-u3: free-model run

- Book: `work/claude_figs/c-graphics-u3/tree/books/cse/c-graphics/c-graphics-u3.html`
- Status: ok
- Model calls so far: 38 (153,456 tokens in, 285,428 out), 7.3 minutes

## Checker

```
c-graphics-u3.html: 8 chapters, 12679 words, 9 figures, 183 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 2 (and the heading 'clockwise ordering', plus the last exam trap): It says to list a face's vertices clockwise as seen from outside the solid and that then the cross product of the first two edge vectors points outward. In a right-handed x, y, z system (the one this chapter uses) that is backwards: clockwise-from-outside gives an inward normal. Counterclockwise-from-outside with the right-hand rule is what gives the outward normal, and that is also the convention the worked example itself follows — the base of the pyramid P1=(E4,E3,E2,E1) traverses V1→V4→V3→V2 and the side P2=(E1,E6,E5) traverses V1→V2→V5, both counterclockwise from outside. So the rule as written contradicts both the standard textbooks and the example, and the exam trap that warns about 'anticlockwise for one face and clockwise for another' teaches the wrong default.
- ch 1 [high] Worked example 1, step 6 and answer: 'The table stores 5 vertices once, so 16 − 5 = 11 references are saved' mixes two different things. The saving is in stored coordinates, not in references: in the three-table scheme the edge table alone holds 2 vertex indices per edge (8 × 2 = 16 vertex references) and the polygon table holds 16 edge references (4 + 4×3). Total index entries go up, not down, so saying 11 references are saved is wrong and a student will repeat it as a memory claim.
- ch 2 [high] Section 2, back-face test sentence: 'a face turned away from the camera gives the opposite sign at the eye' is elliptical. It never says that the plane expression must be evaluated at the eye point, and 'opposite sign' does not say opposite to what. A student can easily invert the test and cull the front faces instead of the back faces.
- ch 2 [low] Section 2, paragraph on unit normal: The plane constant is the capital D, and the signed distance is introduced as lowercase d. Two symbols that differ only in case, in the same paragraph, invite copying errors in the exam.
- ch 2 [low] Exam traps, second bullet: 'Quoting an unnormalised normal as though its length were a distance' is confusing: the length of the normal is never the distance. The real mistake is treating the raw value Ax + By + Cz + D, which is |n| times the distance, as a distance in model units.
- ch 2 [low] Section 2, last sentence: 'Only a few universities teach the coefficient formulas; most courses use the plane only for the back-face test' is unclear and contradicts the chapter itself, which does derive A, B, C, D and uses them for more than back-face removal. 'Coefficient formulas' is undefined.
- ch 2 [low] Lead: The lead promises that the equation gives 'the distance from the origin', but the text only gives the signed distance of a general point P. The distance from the origin, |D|/|n|, is never shown.
- ch 2 [low] Quiz Q5: The answer 'outside the solid' is only guaranteed for a convex solid. For a concave solid, a point on the outward side of one face plane can still sit inside another part of the same solid.
- ch 3 [high] Section 1 final bullet; Exam traps bullet 2; Quiz Q3 answer: The text says every quadric equation describes an unbounded surface and must be clipped. This is false: the sphere and ellipsoid listed in the same table are bounded. The Q3 answer repeats the same false general statement.
- ch 3 [high] Quiz Q6 answer: The answer is garbled and gets the 4-unit case wrong. It shows '0.037  0.5' with no comparison and then says one merged surface. At 4 units apart the midpoint field is 0.037, which is below 0.5, so the blobs are separate. The merged case belongs to 1 unit apart.
- ch 3 [high] Section 1 table, Sphere row: The sphere equation defines a surface, not a closed ball. A closed ball is the solid region (x−x₀)² + (y−y₀)² + (z−z₀)² ≤ r². Calling the sphere a closed ball contradicts standard terminology.
- ch 4 [high] Exam traps, first trap: The parenthetical "(and repeats at a repeated point)" is wrong for inner control points. Repeating an inner control point P1 = P2 does not make the curve pass through that point; at t = 0.5, for example, the curve point is (1/8)P0 + (3/4)P1 + (1/8)P3, which is generally not P1. A student will take away the false rule that repeating a control point puts the curve on it.
- ch 4 [low] Section 2, bullet list: The symbol Pi(1) for the interpolated point of the first de Casteljau level is ambiguous: it reads like point Pi with an argument, not a superscript level index. Students may confuse it with the parameter t or with a power.
- ch 5 [high] Section 2, degree-0 basis definition: The span is printed as 'ui ≤ t i+1', which is not a valid inequality — the right-hand knot and the '<' sign are missing. A student cannot tell what the degree-0 basis is nonzero on.
- ch 5 [low] Section 3, surface formula: The symbol m is reused: in Sections 1 and 2 it is the highest knot index (U has m+1 entries), but in the surface sum it is the highest control-net index in the v direction. The same letter means two different things.
- ch 5 [low] Sections 1 and 2: 'Knot span' is used (uniform knots, support of Ni,p) without ever being defined for the reader.
- ch 6 [low] Figure (Z-buffer inner loop): Both dashed return edges go from 'Write colour'/'Keep old pixel' back to 'Next polygon'. After one pixel is tested, the loop must continue with the next pixel of the same polygon; as drawn, a student would read that one test finishes a whole polygon and all its other pixels are dropped.
- ch 6 [low] Section 2, display step: The drawing rule is stated only for an eye in front of the root plane; a student may not see that the same 'find the eye's side, draw far subtree, root, near subtree' rule is applied at every node, not just at the root.
- ch 7 [low] Section 3, flat shading: "It is cheap and correct for a true flat face" is too strong. Flat shading uses one normal and one light vector for the whole face; with a nearby point light, and with a perspective viewer, both L and V change from point to point, so even a planar face is not uniformly lit.
- ch 7 [low] Exam traps, third bullet: The trap "Thinking n changes brightness" can mislead. Raising n lowers (R·V)ⁿ for every R·V < 1, so the specular term away from the mirror direction does get dimmer as n grows. Only the peak value at R·V = 1 is set by ks alone.
- ch 7 [low] Section 2, first sentence after the formula legend: "Use max(0, N·L) and max(0, R·V)" repeats the same instruction already given at the end of the legend line, so the reader meets the clamp rule twice in a row.
- ch 7 [low] Beyond: "Physically based rendering replaces the three coefficients with material roughness and metalness" leaves out the base colour. PBR materials normally carry base colour (albedo) as well, which is what replaces kd in practice.
- ch 8 [low] Section 2, glass paragraph: Snell's law is given as if a refracted ray always exists. When light travels from a denser to a rarer medium and the angle is large (n₁ sin θ₁ > n₂), sin θ₂ comes out greater than 1 and there is no refracted ray; the ray must be reflected instead (total internal reflection). A student will otherwise compute an impossible angle for glass.
- ch 8 [low] Section 2, reflection paragraph and I formula: Only the reflected ray is told to recurse with depth minus one. The refracted ray is also a child ray (I_refract appears in the formula), but the text never says it must be traced recursively with the depth reduced.
- ch 8 [low] Quiz Q6: The rough total is given as P×O×D. If D is the depth limit (number of bounces allowed), each pixel needs the primary ray plus up to D child rays, so the count is about P×O×(D+1); P×O×D undercounts by the primary level.
- ch 8 [low] Figure (spec): The edges chain hit → shadow → reflected → refracted, which reads as if the shadow ray produces the reflected ray and the reflected ray produces the refracted ray. They are independent branches from the same hit point. Also the note 'blocked means dark' overstates the effect: a blocked light adds no direct colour, but ambient light still reaches the point.
- ch 8 [low] Section 2, I formula: The coefficients k_r and k_t are only said to lie between 0 and 1. Nothing stops a student using k_r = k_t = 1, which creates energy at every bounce.
