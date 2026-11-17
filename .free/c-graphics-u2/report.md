# c-graphics-u2: free-model run

- Book: `work/claude_figs/c-graphics-u2/tree/books/cse/c-graphics/c-graphics-u2.html`
- Status: ok
- Model calls so far: 40 (159,384 tokens in, 307,349 out), 8.6 minutes

## Checker

```
c-graphics-u2.html: 8 chapters, 15110 words, 9 figures, 190 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 1, rotation paragraph: "sin and cos must use the same unit, degrees or radians" states a triviality (sin and cos of one angle always share a unit) and hides the real rule a student needs: θ, the trig function's argument, must be in one consistent unit, and the calculator must be in that mode.
- ch 1 [low] Section 1, rotation paragraph: "θ is the rotation angle from the positive x-axis" can be misread as the angle at which the point already sits, not the angle it is turned through.
- ch 1 [low] Section 2: Scaling about a fixed point gets a formula, but rotation about a pivot point appears only as an exam trap with no formula in the body, so the worked example and the trap do not connect.
- ch 2 [low] Section 2: The section says W = 0 marks a direction 'such as an edge vector or a surface normal', then claims scaling multiplies such a direction by sx and sy 'because a stretched object has stretched edges'. That reasoning holds for edge vectors, but a surface normal under non-uniform scaling does not transform by the same scale matrix; it needs the inverse transpose (and then renormalising). A student who scales normals with sx, sy gets wrongly slanted shading.
- ch 2 [low] Beyond: 'OpenGL's glm::translate' is inaccurate: glm (OpenGL Mathematics) is a separate header-only C++ maths library commonly used with OpenGL; it is not part of OpenGL.
- ch 3 [high] Exam traps, item 1: The trap flags a correct expression. With column vectors, M = R · T means T (the translation) is applied first, so writing R · T when the translation happens first is exactly right, not a mistake. A student following this trap will build the wrong matrix.
- ch 3 [low] Section 2 (heading and example): The heading announces rotation and translation, but the worked matrices show rotation R(90°) combined with scaling S. Translation appears only in the closing sentence, so the heading does not match the example the student actually checks.
- ch 3 [low] Section 4: The count switches from 'matrix-vector products' to 'multiplies'. One matrix-vector product is nine multiplications, so '10,000 multiplies instead of 30,000' misstates the unit of the comparison.
- ch 3 [low] Section 3 figure: The blocks run left to right as T(−px, −py) → R(θ) → T(px, py) → M, that is, in application order. The chapter's rule says the product is written with the last-applied matrix on the left, so a student can read the picture as M = T(−px, −py) · R(θ) · T(px, py), which is the wrong matrix.
- ch 4 [high] Section 3, scaling about a fixed point: The matrix product M = T(−F) S(sx, sy, sz) T(F) is reversed for column vectors. With the chapter's convention that the rightmost matrix acts first, this product applies T(F) first, so it scales about −F, not F.
- ch 4 [high] Quiz Q6: The answer states M = T(−F) S(2) T(F), which is the same reversed product and would not give the shown image when applied to a column vector. The step-by-step computation P − F, scale, add F is correct, but the matrix product contradicts it.
- ch 4 [low] Lead: 'Multiply matrices in the order the transforms are applied' can be read as left-to-right, but for column vectors the product is written in reverse order of application: S then R then T becomes T R S.
- ch 5 [low] Section 1 and the figure spec: The pipeline shown runs World → Window → Norm → Viewport → Device and never mentions clipping, although clipping is one of the standard stages of the 2D viewing pipeline (it normally happens in normalized or window coordinates, before the viewport map). A student reading only the figure will think the pipeline has no clipping stage.
- ch 5 [low] Section 1, Normalized coordinates bullet, against the Beyond paragraph: Section 1 says normalized coordinates run from 0 to 1, while the Beyond paragraph says GPUs take normalized device coordinates in the range −1 to 1. Both conventions exist, but as written the two statements look contradictory to a student.
- ch 5 [low] Quiz Q7: The answer says the last column holds the shift and gives (100, 60, 1) for a viewport starting at (100, 60). That value is only correct because the window starts at the origin; a student will generalise the last column to (xvmin, yvmin, 1), which is wrong when xwmin or ywmin is not zero.
- ch 5 [low] Exam traps, fourth bullet (Dropping xvmin): The sentence 'so a viewport placed in the corner of the screen puts the picture in the wrong place' does not support the trap: if the viewport start is (0, 0), dropping xvmin changes nothing. The intended case is a viewport that does not start at the origin.
- ch 5 [low] Quiz Q5 answer: The world point (5, 5) is the window's top-right corner and maps to (400, 400), the outer boundary of a viewport declared as (0, 0) to (400, 400). If that viewport is 400 pixels wide, its inside pixels are numbered 0 to 399, so (400, 400) lies just past the last pixel; a student may be unsure whether the corner pixel is drawn.
- ch 6 [high] Quiz Q5 answer: Code 0010 is the right-hand bit (value 2, x > xmax), not the below bit. The answer says the second end point is cut against y = ymin, which is bit 2 (value 4, code 0100). With codes 0001 and 0010 both ends lie beyond vertical boundaries, so the y-clipping story in the answer is wrong.
- ch 6 [high] Section 2, region-code list: The bit list is garbled: 'Bit 2, value 4: y  xmax, right.' The comparison signs and the whole definition of bit 1 (value 2, right) are missing, and bit 2 is described as if it were the right bit. A student cannot recover the correct four-bit assignment from this line.
- ch 6 [low] Worked example 1 step 9, Exam traps bullet 3, Quiz Q1 answer: The same missing comparison signs appear in three more places: 'The p  0 rows give u2 = ...', 'p  0 tightens u2 with min', and 'Below y  xmax: 2' in the Q1 answer. The values are right but the printed text is unreadable.
- ch 6 [low] Section 1, three outcomes: Saying a crossing segment 'becomes a shorter segment whose new end points sit on the boundary' suggests both new end points move. Often only one end moves; the other is an original point already inside the window.
- ch 6 [low] Beyond: Cyrus–Beck is not simply 'the three-dimensional version'. It is the general parametric clipping algorithm for any convex clip region, in 2D or 3D; Liang–Barsky is its axis-aligned rectangle case.
- ch 7 [low] Section 2, intersection formulas: The symbol t appears in both crossing formulas without ever being defined, so a student cannot tell what it measures.
- ch 7 [low] Section 3, extra edges from concave polygons: "Those edges have zero width" is not a correct description. The extra edges are ordinary line segments lying along the window boundary; what matters is that they enclose no area, so the filled region is unchanged.
- ch 7 [low] Exam traps, fourth trap: The trap says polygons that split into several separate outlines "need Weiler–Atherton", but Section 3 has just said a concave polygon that splits into separate visible pieces is handled by Sutherland–Hodgman with boundary connecting edges. The two statements contradict each other and the trap overstates the limitation.
- ch 8 [high] Section 1, camera parameters and the view matrix: The right vector is built with the cross product in the wrong order. With f = normalize(L − E) and r = normalize(U × f), a point that is physically to the camera's right gets a negative x_v, so every image is mirrored left-to-right. Example: eye at the origin, L = (0, 0, −1) (looking down −z), U = (0, 1, 0) gives r = U × f = (−1, 0, 0), which points left. The up vector also has to change with it: with the corrected r, u = f × r gives the down direction.
- ch 8 [low] Section 2, after the perspective formula: 'Points with z ≤ 0 are behind or level with the eye and have no finite image' is only true for z = 0. For z < 0 the formula still returns a finite number: with d = 3 and z = −6, x·d/z is finite, but it is a meaningless point on the plane because the ray runs away from the projection plane. A student who substitutes z = −6 gets a finite answer and thinks the rule is wrong.
- ch 8 [low] Section 3, first paragraph: 'One-point perspective has one principal axis oblique to the picture plane' — in the one-point case that axis is perpendicular to the picture plane, not oblique, and the word 'oblique' collides with oblique parallel projection, which is discussed in the same chapter.
- ch 8 [low] Section 1, building the viewing coordinate system: The chapter never says that U must not be parallel to f. If U is parallel to f the cross product is zero, normalisation fails, and the whole view matrix is undefined — a failure students hit when the look direction is straight up or straight down.
