# m-calculus-u6: free-model run

- Book: `books/common/m-calculus/m-calculus-u6.html`
- Status: ok
- Model calls so far: 23 (85,411 tokens in, 192,818 out), 4.2 minutes

## Checker

```
m-calculus-u6.html: 9 chapters, 15933 words, 10 figures, 155 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 1: The statement that ∇φ at a point is normal to the level surface, and the formula n̂ = ∇f/|∇f|, silently assume ∇φ is not zero. At a critical point, for example φ = x² + y² + z² at the origin, the gradient vanishes and no normal exists.
- ch 1 [low] Section 1: The example 'for φ = x² + y² + z², the level surfaces are spheres centred at the origin' fails for c = 0, where x² + y² + z² = 0 is the single point (0, 0, 0), not a sphere.
- ch 1 [low] Section 1 and Quiz Q5: A surface has two unit normals, ∇f/|∇f| and its negative. The chapter gives only the plus sign, so a student may think there is a single correct normal.
- ch 1 [low] Figure: The edge from b (gradient ∇φ) to c (unit vector û) suggests the unit direction is obtained from the gradient. In fact û comes from the given direction a, divided by |a|; the gradient and û are independent inputs that meet only in the dot product.
- ch 1 [low] Beyond: 'weather models move air along pressure gradients' is misleading: air is pushed from high to low pressure, that is along −∇p, not along +∇p.
- ch 2 [high] Section 2 (curl and the paddle wheel), sentence about the j component: The text says the j component is ∂F₁/∂z − ∂F₃/∂x "with the x-derivative of F₁ first". ∂F₁/∂z is F₁ differentiated with respect to z, not x. A student who follows this sentence will differentiate F₁ with respect to the wrong variable.
- ch 2 [low] Section 3 (product rules and the three identities): The text says "Two identities are exam favourites" and then lists three bullets, one of which (div(∇φ) = ∇²φ) is a definition of the Laplacian rather than a prove-that identity. The count does not match what follows.
- ch 2 [low] Exam traps, third bullet: The cross-reference "(see 6.3)" is plain text, so on a phone the reader cannot jump to that chapter.
- ch 2 [low] Lead: "The del operator ∇ answers both, along with the gradient of the previous chapter" is muddled: it is unclear whether the gradient answers the two questions or is just the third use of ∇.
- ch 2 [low] Figure spec: Each child of the tree repeats the same words in the edge label and the note (edge "scalar in", note "scalar in, vector out"), so the figure prints the phrase twice.
- ch 3 [low] Section 1, irrotational bullet: "Water moving steadily along a straight pipe is irrotational" is only true for uniform flow. Real flow in a pipe slows to zero at the wall, so the velocity profile is curved and curl v ≠ 0; a student can carry the wrong picture into fluid mechanics.
- ch 3 [low] Figure and its caption: The chart is one straight chain: div test → curl test → set F = ∇φ. Read as a flow, it says a field must pass the div test before a potential is built. Worked example 1 itself finds φ for a field with div F = 6, so the chart contradicts the example and can mislead a student into stopping at a non-zero divergence.
- ch 4 [low] Section 2: The sentence 'A fan blade, a wing section and a wire loop all have a natural circulation' treats circulation as a property of a solid object. Circulation is a line integral of a vector field around a closed curve, not something an object possesses by itself.
- ch 4 [low] Figure: The caption says 'up through C and down through D', but the graph places D at the same height as A, and the route A to D to B goes horizontally then up, not down.
- ch 5 [low] Section 1, the plane example: The sentence gives f_x = −1 and f_y = −1 but never finishes the calculation, so the student is left without the dS value the step was meant to show.
- ch 5 [low] Section 2, first paragraph: 'The value counts field crossing S per unit area' describes the integrand, not the integral. The integral ∬ F·n dS is the total crossing; F·n is the crossing per unit area. A student can read this as saying the whole answer is per unit area.
- ch 5 [low] Figure: The caption says S is the plane x + y + z = 1 inside the solid tetrahedron V. That plane is the slanted boundary face of V, not a sheet lying inside it. The nested-drawing wording ('a curve lies inside a surface, which lies inside a solid') repeats the same wrong picture.
- ch 5 [low] Figure: The values 0.5 for ∬ F·n dS and ∭ 3 dV only make sense for F = (x, y, z), and the figure never states the field. A reader sees two numbers with no source.
- ch 5 [low] Figure: The innermost set is a curve C with ∫ F·dr, which is line-integral material not used anywhere in 6.5 and has no stated value. It invites questions the section does not answer.
- ch 6 [low] Lead: The lead says Green's theorem "shows when a line integral depends only on endpoints", but the chapter never states the condition. A student can easily conclude that ∂N/∂x = ∂M/∂y everywhere is enough, which is false on a region with a hole (the field (−y, x)/(x²+y²) has zero curl yet its integral round a circle is 2π).
- ch 6 [low] Section 1: "M and N have continuous first partial derivatives on R and on C" is not the standard condition: a partial derivative on a curve C alone is not a well-defined requirement, and the standard hypothesis is that the partials are continuous on an open region containing R.
- ch 6 [low] Quiz Q1: The model answer omits the conditions on the curve C (piecewise smooth, closed, anticlockwise), which are part of the statement being asked for in a recall question.
- ch 6 [low] Section 3 heading: The heading promises "Corners", but corners are handled in Section 1; Section 3 only deals with holes and orientation/sign.
- ch 7 [low] Worked example 1, step 8: The limits of the integral are written flat as "∫02π 4 dt", so on a phone it reads like the number 02π or like a product; the subscript and superscript tags used elsewhere in the chapter are missing here.
- ch 7 [low] Exam traps, fourth bullet (closed surface): The sentence says "the closed-surface result is Gauss' theorem, not Stokes'", which blurs two different integrands and can leave a student unsure what Stokes' theorem actually gives on a closed surface. With no boundary curve the line integral is zero, so the flux of the curl through a closed surface is zero; Gauss' theorem is a separate statement about the flux of F itself.
- ch 7 [low] Exam traps, third bullet (component of F then curl): "The order matters because n may vary over S" does not explain the mistake. The real reason is that a single component of F is a scalar, and ∇×F needs all three components of F at each point before any dot product with n is taken.
- ch 8 [low] Section 3, tank sentence: The sentence 'the flux of water across the walls plus the rate of change of stored water balance' is grammatically incomplete and misleading: a rigid tank's walls carry no flux, and it is the inflow and outflow through the pipes that balance the change of stored water.
- ch 8 [low] Exam traps, third bullet: 'the two faces with zero flux' is stated as if a cube always has exactly two such faces. The number depends on the field; in Worked example 1 three faces give zero flux.
- ch 8 [low] Section 3, last line: 'See 6.3.' is a bare chapter reference with no link, so on a phone the reader cannot jump to it; other chapter links in the series are given as links.
- ch 9 [low] Lead: 'Torsion measures how fast the curve leaves its own plane' is loose: a space curve has no single 'own plane'. Torsion is the rate at which the osculating plane (the plane of T and N) turns about the tangent, per unit arc length. A student may read this as distance from a fixed plane.
- ch 9 [low] Section 1: The claim 'Its derivative dT/ds is perpendicular to T' is stated with no reason. Students memorise it but cannot reproduce the one-line proof.
- ch 9 [low] Section 1: N = (dT/ds)/|dT/ds| is undefined where dT/ds = 0 (κ = 0, e.g. a straight line or at an inflection). The chapter defines N without saying this, so students think N always exists.
- ch 9 [low] Section 2: In the torsion formula note, 'the dot is the scalar triple product' mislabels the operation. The dot is the dot product; the whole combination (r′ × r″) · r‴ is the scalar triple product.
- ch 9 [low] Exam traps, bullet 3: 'Swapping the order in (r′ × r″) · r‴ flips the sign of τ' is ambiguous. A cyclic swap r′ → r″ → r‴ leaves the triple product unchanged; only an odd swap (one interchange, e.g. r″ × r′) flips the sign.
- ch 9 [low] Quiz Q5: The answer gives |r′| = 5 without units, although Q2 has just asked about units and the coordinates are in metres.
- ch 9 [low] Section 2: The chapter never says τ can be negative or what the sign means, although the formula itself produces signs. Students then assume torsion is always a positive number like curvature.
