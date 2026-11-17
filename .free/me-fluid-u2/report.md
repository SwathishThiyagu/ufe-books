# me-fluid-u2: free-model run

- Book: `books/mech/me-fluid/me-fluid-u2.html`
- Status: ok
- Model calls so far: 34 (138,331 tokens in, 289,643 out), 9.0 minutes

## Checker

```
me-fluid-u2.html: 9 chapters, 16114 words, 10 figures, 164 KB
OK
```

## For the reviewer

- chapter 2: the figure cannot be drawn: note "how many coordinates?" runs off the right edge; shorten it

## Reviewer notes (after any revision)

- ch 1 [low] Worked example 1, step 4: The Eulerian field is built from one particle's path only. One path gives u and v along that path, not u and v at every point in space. Saying 'u = 2 m/s everywhere' and 'v = 3(x − 1) m/s' is an extra assumption, and a student may wrongly conclude that a single Lagrangian trajectory always yields the full field.
- ch 1 [low] Section 3, last but one paragraph: 'the two-part acceleration is in velocity and acceleration of fluid particles' is a dangling cross-reference to another chapter. A student reading only this unit does not learn that the two parts are the local term ∂V/∂t and the convective term (V·∇)V.
- ch 1 [low] Exam traps, second point: 'The mass inside a control volume is not fixed' is true in general but reads as if the mass inside a fixed control volume always changes. In steady flow through a fixed control volume the mass inside is constant, even though mass keeps crossing the surface.
- ch 2 [high] Beyond: The claim that a fixed-point velocity record shows "flat (steady) or fluctuating (turbulent)" undoes the chapter's own correct distinction in Section 3 that laminar/steady and turbulent/unsteady are separate questions. A turbulent flow that is steady in the mean gives a fluctuating record with a constant mean, so 'fluctuating' alone does not mean turbulent, and a fluctuating record with a drifting mean means unsteady, not turbulent.
- ch 2 [low] Quiz Q7: The question asks for all four labels, but the answer for the surge gives only unsteady, non-uniform and three-dimensional, plus 'rapidly varied', which is not one of the four labels. The order label (laminar or turbulent) is missing for the surge itself, so a 5-mark answer would lose marks.
- ch 2 [low] Section 4, last paragraph: 'Open channels add one more label, rapidly varied unsteady flow' treats a compound of two independent axes as a single label. Rapidly varied flow is normally a sub-class of non-uniform flow and can be steady (a hydraulic jump on a steady flow); only a surge or bore is both rapidly varied and unsteady.
- ch 3 [low] Section 1, definition of the Eulerian field: The phrase 'components u, v and w, in m/s, along the axes x, y and z, in metres' is garbled: it makes the axes themselves seem to be measured in metres, and the student cannot tell which symbol carries which unit.
- ch 3 [low] Section 2, after the streamline equation: 'Solving this first-order differential equation gives a family of curves with one constant' is true only for the two-dimensional form. In three dimensions dx/u = dy/v = dz/w gives two independent first-order equations, so a streamline is fixed by two constants (the intersection of two surfaces).
- ch 3 [low] Section 2, stream tube paragraph: The statement that the discharge through every section of a stream tube is the same is true for steady incompressible flow; in unsteady flow the volume between sections changes, and in compressible flow it is the mass flow ρAV that stays constant, not the volume discharge.
- ch 3 [low] Section 3, incense-stick example: The example says the smoke rises 'in still room air', but Quiz Q7 explains the same smoke by saying the room air has draughts and is unsteady. A student meets two different settings for the same example, and in truly still air the rising smoke is a buoyant plume rather than a line of the room-air velocity field.
- ch 3 [low] Section 2, first sentence of the streamline discussion: 'A streamline freezes time and shows the whole field at that instant' overstates what one curve does: a single streamline shows the velocity direction only at the points lying on it, not the whole field.
- ch 3 [low] Beyond: 'the streakline from a chimney is what a monitoring station actually samples' is loosely worded: a station measures concentration at one fixed point as the plume passes, not the streakline itself.
- ch 4 [low] Lead paragraph: The lead says a particle can 'speed up' for two reasons, but acceleration also changes when the direction of the velocity changes. A student may read the chapter as being only about speed.
- ch 4 [low] Section 2, formula box for streamline coordinates: The box gives a_s = V dV/ds without saying it holds only in steady flow. In unsteady flow the tangential acceleration also contains the local term ∂V/∂t. The sentence above the box states the steady-flow condition, but the box itself does not.
- ch 4 [low] Section 1 definition list: 't is seconds' is missing a word and reads awkwardly next to the other definitions.
- ch 4 [low] Beyond: Saying blood flow 'uses the V²/R term to estimate wall stress' is loose. The V²/R term gives the transverse pressure difference across a curved vessel and drives curvature-induced secondary flow; wall stress itself is estimated from the velocity gradient near the wall.
- ch 5 [low] Section 3, branching junction paragraph: The sentence 'At a branching junction in steady flow, the volume flows into the junction add up to the volume flows out' is written as if it holds for any steady flow. Volume balance needs constant density as well; a gas junction must be balanced on mass. The exam-trap list corrects this later, but a student reading only this paragraph can be misled.
- ch 5 [low] Section 3, gas paragraph: 'Gases keep the density' is ambiguous. It can be read as 'the density of a gas stays constant', which is the opposite of the point being made, and it clashes with the very next sentence about air at 5 bar being denser than at 1 bar.
- ch 6 [low] Section 1, definition of ω_z (and Exam trap 3): "positive counterclockwise when viewed along +z" is ambiguous. "Along +z" can be read as looking in the +z direction (from the origin outward), which is exactly the view that makes clockwise appear positive and reverses the sign convention the chapter relies on.
- ch 6 [low] Section 3, formula ζ_z = (1/r) ∂(r v_θ)/∂r: This is only the tangential part of the polar vorticity. It is correct for a purely swirling field with v_r = 0, but the text never says so, so a student applying it to a flow that also has a radial component (source plus vortex) will drop a term and get the wrong answer.
- ch 6 [low] Section 3, pipe-flow illustration: A pipe profile varies with radius r, not with a Cartesian y. Writing ∂u/∂y mixes the two systems and sits oddly next to the polar formula just above, which can confuse a student reading them together.
- ch 6 [low] Lead (opening paragraph): "...yet only one has vorticity" is too absolute. Both real flows carry vorticity somewhere; the drain flow merely comes close to an irrotational free vortex except near its rotating core. Read next to the careful statement in Section 3, the lead looks like a contradiction.
- ch 7 [low] Lead and Section 2: The text says the velocity potential gives the velocity 'as the gradient of a scalar', but the convention actually used two lines later is u = −∂φ/∂x, v = −∂φ/∂y. A student can read 'gradient' literally and lose the minus sign, which the chapter itself warns about in the exam traps.
- ch 7 [low] Quiz Q6: The unit in the answer is wrong. Discharge per unit depth already means per metre of depth, so its unit is m²/s. Writing '0.6 m²/s per metre depth' counts the depth twice and would read as m/s.
- ch 8 [high] Section 2 (q formula), Section 3, Worked example 1 answer: The unit of q is written as "m²/s per m depth". q is already the discharge per unit depth, so its unit is m²/s (that is, m³/s for each metre of depth). "m²/s per m" divides by a metre twice and comes out as m/s, which is a velocity, not a discharge.
- ch 8 [low] Section 2, drawing steps 2 and 3: The steps tell the student to choose Δψ and Δφ separately, then adjust until the cells are squares. In any cell Δψ = v Δn and Δφ = v Δs, so Δn/Δs = Δψ/Δφ at every point. If the two increments are not equal, every cell stays a rectangle and no amount of adjusting can make squares. Section 1 says the two increments across a cell are equal, so the procedure contradicts it.
- ch 8 [low] Lead and Section 3 (uses): A sudden contraction in a pipe is an axisymmetric flow, not a planar two-dimensional one. The planar flow net and q = N_f Δψ do not carry over directly, because the axisymmetric (Stokes) stream function carries an extra radius factor.
- ch 8 [low] Beyond: "Commercial CFD codes solve Laplace's equation" overstates it. General-purpose CFD codes solve the Navier–Stokes equations; solving Laplace's equation for φ is what potential-flow codes do.
- ch 9 [high] Section 3 (Rankine vortex): The text says velocities agree at rc but surface slopes do not. With K = ω rc², the free-surface slope dz/dr = vθ²/(gr) is also continuous at rc; only the curvature changes. A student will expect a kink that is not there.
- ch 9 [high] Section 2 and Quiz Q4 answer: The text says a forced vortex needs torque to overcome friction between neighbouring rings, and Q4 says neighbouring rings slide over each other with vorticity 2ω. In steady rigid-body rotation vθ = ωr, adjacent rings have the same angular speed; the strain rate is zero, so there is no inter-ring shear/friction. Vorticity 2ω is element spin, not sliding between rings.
- ch 9 [low] Quiz Q8 answer: The answer compares the surface dip/rise and explains why the free vortex has the larger dip, but it does not answer the part about energy stored.
