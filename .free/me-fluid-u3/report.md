# me-fluid-u3: free-model run

- Book: `books/mech/me-fluid/me-fluid-u3.html`
- Status: problems
- Model calls so far: 31 (134,556 tokens in, 256,512 out), 8.3 minutes

## Checker

```
me-fluid-u3.html: 8 chapters, 16275 words, 9 figures, 165 KB
PROBLEMS:
 - text contains "as an AI"
```

## For the reviewer

- chapter 5: the figure cannot be drawn: note "Francis formula" runs off the right edge; shorten it
- chapter 5: the figure could not be drawn; a plain box diagram stands in for it
- checker: text contains "as an AI"

## Reviewer notes (after any revision)

- ch 1 [low] Section 1, examples of control volumes: 'the gap between two turbine blades' is given as an example of a fixed region in space. In a running turbine that passage rotates with the rotor, so it is a moving control volume, not a fixed one. A student will later meet the moving-volume rule and think it contradicts this sentence.
- ch 1 [low] Worked example 1, steps 4 and 5; quiz Q5: ρQ(V₂ − V₁) is labelled 'Momentum flux out'. It is the net outward momentum flux, not the outflow. The result −20 N means more downstream momentum enters than leaves (net inflow of 20 N of downstream momentum), i.e. the fluid loses momentum. Step 5's sentence '20 N of momentum per second leaves in the negative direction' suggests momentum is being pushed upstream out of the region, which is not what the numbers say. The same loose wording appears in Q5 ('30 N of momentum per second leaving upstream').
- ch 1 [low] Section 3, moving control volume sentence; quiz Q7: The storage term is kept as ∂/∂t ∫ρb dV when the control volume moves. For a moving or deforming region the derivative of the volume integral over that moving region is a d/dt, not the local ∂/∂t of the fixed-volume case. Q7's justification ('unchanged in form because it is evaluated at the same instant in a fixed frame') is vague and does not say this.
- ch 1 [low] Section 3, last paragraph: 'Shrinking the control volume to a thin streamtube gives Euler's equation.' Euler's equation holds for inviscid flow only; the general result of shrinking the volume is the differential momentum equation, of which Euler's equation is the frictionless case.
- ch 1 [low] Figure: The note on the last block reads 'system rate = b + c', using the node ids b and c. In this chapter b is the symbol for the property per unit mass, so the note reads as 'system rate = property per kg + c'.
- ch 2 [low] Section 2 (normal balance across a curved streamline): The normal equation dp/dn = ρV²/r is presented as general, but it neglects the component of weight in the n direction; a student applying it to a curve in a vertical plane gets the wrong gradient.
- ch 2 [low] Section 2, after dp/ds = −ρV dV/ds: "Where velocity rises, pressure falls" is only guaranteed on a horizontal streamline (dz = 0). On a sloping streamline the g dz term can outweigh the acceleration term, so pressure can rise while speed rises.
- ch 2 [low] Section 1, derivation (acceleration step): Writing dV/dt = (dV/ds)(ds/dt) = V dV/ds silently drops the local acceleration ∂V/∂t; the step is only valid because the flow is steady, and that is not said at this point.
- ch 2 [low] Section 2, assumptions list: "The two points lie on the same streamline" is listed as an assumption for the differential equation, which is valid at a point. A student may think Euler's equation needs two points, and miss that the condition matters only when integrating to compare two points.
- ch 3 [high] Section 3, Torricelli's law paragraph: It says a real jet is slower 'because of friction and contraction'. Contraction reduces the jet area and hence the discharge; it does not reduce the jet speed. Only friction (and the resulting velocity profile) makes the actual velocity smaller than √(2gh), which is why the coefficient of velocity Cv is less than 1. The coefficient of contraction Cc is a separate correction for the area.
- ch 3 [low] Section 1, description of the figure: It says the velocity head at the wide end is 0 m and the pressure head is 5 m. A zero velocity head means V = 0, so no flow is passing; a student may think a pipe section can carry flow with no velocity.
- ch 3 [low] Section 2, sentence before the list of assumptions: 'The assumptions are exact' is the wrong word: assumptions are conditions that are satisfied or not, not quantities that are exact. A student may read it as 'the equation is exact even with friction'.
- ch 4 [low] Figure, node d: The flowchart note under 'Continuity' says 'removes V₂', but Section 1 states the step as replacing V₁ by (A₂/A₁)V₂ and then solving for V₂. A student reading both will be unsure which velocity continuity eliminates.
- ch 4 [low] Section 1, after the Bernoulli formula: The sentence 'The elevation terms cancel for a horizontal pipe' can make students think the Q formula is valid only for horizontal venturimeters. The same formula holds for vertical or inclined pipes, because h read from the U-tube is already the difference of piezometric heads.
- ch 4 [low] Exam traps, first bullet: 'The throat area gives only the velocity, not the discharge' is ambiguous. It reads as if Q = A₂V₂ is wrong, when the point is that V₂ must be found from the full area term before multiplying by A₂.
- ch 5 [high] Exam traps, fourth trap ("Mixing Cc and Cd"): The trap says that writing Cd = Cc / Cv "gives a value above 1, which is impossible". With Cc ≈ 0.62 and Cv ≈ 0.98, Cc / Cv = 0.63, which is below 1, so the stated consequence is false. The ratio that actually exceeds 1 is Cv / Cc = 0.98 / 0.62 ≈ 1.58.
- ch 5 [low] Section 1, large orifice formula: The powers are written as plain text: "Q = (2/3) Cd b √(2g) (H23/2 − H13/2)". A student reads H23/2 as H times 23/2, or as 0.403 divided by 2. The rest of the chapter uses <sub> and <sup>, so this formula looks like a different (wrong) expression.
- ch 5 [low] Section 3, Francis formula sentence: Two small faults. The power is again unmarked ("Q = 1.84 L H3/2"), and "with the approach head corrected inside the bracket" is too vague to act on; the earlier rule "replace H by H + ha" is only an approximation, while Francis uses a difference of two powers.
- ch 5 [low] Worked example 1, steps 1 and 2; Quiz Q5 answer: Missing superscripts make correct working read as wrong arithmetic: "4.429 m0.5/s", "H3/2 = 0.403/2 = ...", "0.2530 m3/2", and in Q5 "H5/2 = 0.252.5 = 0.03125 m2.5". As printed, 0.403/2 is a division and 0.252.5 is a decimal number.
- ch 5 [low] Worked example 1, part (b) statement: "The weir is shortened so that one end contracts" suggests the crest length itself changes, yet step 5 keeps L = 3 m. A student may shorten L and then also subtract the end-contraction term, applying the correction twice.
- ch 6 [high] Quiz Q3: The premise 'pressure forces cancel' is wrong. In a 90° bend the two cut-surface forces p₁A₁ and p₂A₂ are equal in magnitude but perpendicular to each other, so they add as vectors, not cancel. The stated answer (40 N per component, 56.6 N, 45°) is only the momentum-flux part, so the question as worded does not lead to its own answer.
- ch 6 [high] Section 2, last sentence: The pitot-tube sentence is technically wrong. The force from stagnation pressure acting over the probe face is about ½ρV²A, while the rate of momentum destroyed by bringing a stream of area A to rest is ρAV²; the two differ by a factor of two, so 'the stagnation pressure force on the probe equals the rate of momentum destroyed' is not a valid statement.
- ch 6 [high] Quiz Q7: The answer does not give the extra term asked for. For a control volume translating with acceleration a_cv, the equation needs velocities relative to the CV plus a term m_cv·a_cv (mass of fluid in the CV times its acceleration), which acts like an extra force. The answer mentions only the unsteady local term and 'relative velocities', so a student would miss the acceleration term entirely.
- ch 7 [low] Section 1, sentence after the vector equation: The sentence says the terms 'local acceleration ∂V/∂t, convective acceleration V·∇V, pressure force −∇p, gravity force ρg, and viscous force μ∇²V' are 'all per unit volume'. The two acceleration terms are accelerations (m/s²), not force per unit volume; only ρ times them is force per unit volume. A student can end up quoting ∂V/∂t with units of N/m³.
- ch 7 [low] Figure: The vertical axis is labelled u/u_max, but the Couette line rises from 0 to 1 in units of the plate speed U, while the parabola peaks at 1 in units of the Poiseuille maximum. The two series use different reference speeds, so the figure suggests the Couette surface speed equals the Poiseuille peak speed, which is true only in a special case.
- ch 7 [low] Worked example step 5 and quiz Q5 answer: The discharge per metre width is written as '2.5 × 10⁻⁴ m²/s per metre width'. The quantity q = mean × h already is the discharge per metre of width, with unit m²/s (equivalently m³/s per metre of width). Adding 'per metre width' to m²/s gives the wrong dimension, m/s.
- ch 8 [high] Section 2 and Worked example 1, step 5: The isentropic area–Mach relation for A/A* is never given in the body text; it appears only inside the figure's code expression. Step 5 then uses it, and quiz Q4 reasons with it, so a student cannot follow or reproduce the step. The symbol A* is also never defined.
- ch 8 [high] Worked example 1, step 5: The formula mixes a general γ in the factor 2/(γ + 1) with air-only numbers 0.2 and exponent 3: A/A* = (1/M)[(2/(γ + 1))(1 + 0.2M²)]³ is wrong for any gas other than γ = 1.4. Exponent 3 equals (γ+1)/(2(γ−1)) only at γ = 1.4.
- ch 8 [low] Section 1: 'Bring a moving gas to rest adiabatically and its temperature and pressure rise' is loose for pressure. T₀ needs only adiabatic deceleration, but p₀ is the pressure reached when the gas is brought to rest isentropically (adiabatically and reversibly). Read as written, it contradicts the later correct statement that p₀ falls across a shock.
- ch 8 [low] Section 3, first paragraph: 'Use the compressible relations when ... the gas is a vapour near saturation' invites a student to apply c = √(γRT) and p₀/p = (1 + 0.2M²)^{3.5} to wet steam, where the perfect-gas laws do not hold.
- ch 8 [low] Quiz Q6, answer: The numbers give a temperature rise of 0.8% but a pressure ratio of 1.028, an almost 3% change; saying 'the changes are about 1%' understates the pressure change and could make a student think 3% is negligible.
- ch 8 [low] Exam traps, fifth bullet: 'Stagnation pressure falls in both; only T₀ stays constant in an adiabatic shock' can be read as saying T₀ stays constant only in a shock. In adiabatic flow with friction (Fanno flow) T₀ is also constant while p₀ falls.
