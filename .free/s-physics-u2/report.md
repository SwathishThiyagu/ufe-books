# s-physics-u2: free-model run

- Book: `books/common/s-physics/s-physics-u2.html`
- Status: ok
- Model calls so far: 24 (101,358 tokens in, 177,372 out), 4.2 minutes

## Checker

```
s-physics-u2.html: 8 chapters, 13567 words, 9 figures, 151 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Worked example 1 and Section 3: The example uses a mass hanging vertically on a spring, but the chapter never says that gravity only shifts the equilibrium position down by mg/k and does not change ω or T. A student may think the weight must be added to the restoring force and that ω = √(k/m) does not apply to a hanging spring.
- ch 1 [low] Exam traps, first bullet: The sentence 'Substituting ω for f puts a factor 2π into T, f and vmax' is muddled. vmax = Aω does not contain f at all; using f in place of ω makes vmax 2π times too small, and using ω in place of f makes f and T wrong by 2π.
- ch 2 [low] Section 2, final sentence: The wording 'use this balance' is vague. 'Balance' already means a weighing balance; here it means the balance of torque and inertia, which a first-time reader may miss.
- ch 2 [low] Lead, Section 2 and Beyond: The MEMS example changes three times: 'MEMS sensors' in the lead, 'MEMS gyroscopes' in Section 2, 'MEMS mirrors' in Beyond. A student revising from these notes sees three different devices for one idea.
- ch 2 [low] Beyond: It says the same C = πηr⁴/(2l) idea appears in the torsion bar suspension of vehicles. A vehicle torsion bar is a solid bar, usually not of circular cross-section, clamped at both ends, so the round-wire formula does not apply to it directly.
- ch 2 [low] Quiz Q2 answer: The answer is qualitative and stops short of the reason the motion is sinusoidal: a linear restoring torque with a constant I gives a linear differential equation.
- ch 3 [high] Section 1, damping cases sentence: The sentence reads "For ζ  1 (overdamping) it returns more slowly, also without oscillation." The comparison sign is missing, and the cases the reader needs are absent: the underdamped case (ζ < 1, oscillatory decay, which is the case the chapter's formula and worked example use) and critical damping (ζ = 1, fastest return without oscillation). The later claim that a shock absorber is "designed near critical" has nothing to refer back to.
- ch 3 [low] Section 1, formula box for x(t): A is described as "initial amplitude in m", but at t = 0 the displacement is x(0) = A cos φ, so A is not the initial displacement unless φ = 0.
- ch 3 [low] Figure, series label: The second curve is labelled "heavy damping", but its coefficient 0.6 equals 2ζ, so ζ = 0.3 — moderate damping. The curve still shows a clear peak of about 1.75, which misrepresents what heavy damping does.
- ch 4 [high] Exam traps, first trap: The trap says that putting the total mass 0.030 kg in place of μ gives a speed too large by a factor √L. It gives a smaller speed. With T = 120 N and m = 0.030 kg, √(T/m) = √4000 = 63.25 m/s, while the correct √(T/μ) = 77.46 m/s. Since √(T/m) = √(T/μ)/√L, the wrong speed is too small by √L, not too large.
- ch 4 [low] Section 2 and Section 1: The letter T is used for two different quantities: tension (N) in Section 1 and the period of the wave (s) in the sentence 'every period T = 1/f'. A student can read the period sentence as a statement about tension.
- ch 4 [low] Section 3, last paragraph: 'Sound in a pipe follows the same rule with pressure in place of displacement' invites the wrong picture. At a closed end the displacement has a node and reflects with a phase change of π, but the pressure has an antinode there and reflects with no phase change, so the boundary behaviour is not simply copied over.
- ch 5 [low] Section 1, energy per unit length: The text says 'the energy in that element is ½ μ ω² A² dx' and 'the energy per unit length is u = ½ μ ω² A²', as if this held at every instant. For a travelling wave it does not: the kinetic and potential energy of a string element peak together, and the instantaneous energy per unit length is μω²A²cos²(kx − ωt). Only the average over a wavelength (or a cycle) equals ½ μ ω² A². A student who later meets the cos² form will think the chapter contradicted itself.
- ch 5 [low] Section 2, antinode sentence: 'these are antinodes, swinging through 2A' is ambiguous: 'swinging through' usually means the full peak-to-peak travel, which here is 4A, not 2A. Earlier in the same paragraph the amplitude is correctly given as 2A.
- ch 6 [low] Figure: The x-axis runs linearly from 1 to 10¹² while the plotted quantity is 10 log₁₀(I/I₀). On a linear axis almost the whole curve is squashed against the y-axis, so the reader cannot see that each tenfold rise adds 10 dB, which is exactly the point the figure caption makes.
- ch 6 [low] Figure: The sample points jump straight from x = 1 to x ≈ 1.25×10¹⁰. Joined as a polyline on the linear axis, the first segment is a straight chord from 0 dB to about 101 dB, so the drawn curve is not the logarithm over that whole first stretch.
- ch 6 [low] Section 3: 'measured in m² sabins' uses two unit names for the same thing; the sabin is already defined as equivalent to 1 m² of perfect absorption, so a student may think absorption has a unit different from area.
- ch 6 [low] Exam traps, last item: The trap warns against I₀ = 10⁻⁶ W/m², a value students rarely meet. The confusion that actually happens is between 10⁻¹² W/m² and the older 10⁻¹⁶ W/cm² form.
- ch 7 [low] Section 1 (construction) and Section 2 (thickness resonance): Section 1 says the slab is 'clamped between two metal plates that hold it', but Section 2 says 'its faces are free'. Clamping a face holds it still, which contradicts the free-face antinode picture on which f = v/(2t) rests, so a student can reasonably ask why the faces are nodes in one sentence and antinodes in the next.
- ch 7 [low] Quiz Q7 answer: The answer says both quartz and PZT need 'roughly 0.3 mm' at 10 MHz, but Q4 in the same quiz uses v = 4.0 × 10³ m/s for PZT. With that value t = v/(2f) = 4000 ÷ (2 × 10⁷) = 0.20 mm, which is not 'roughly 0.3 mm'. The two questions give the student different PZT speeds.
- ch 8 [low] Section 2, opening paragraph: The claim that narrow beams and sharp reflection are 'why every application below works' is wrong for cleaning and for welding/drilling: those use cavitation collapse and mechanical vibration with abrasive slurry, not echoes. A student may repeat this wrong cause in an exam.
- ch 8 [low] Section 1, grating formula: The formula d sin θ = nλ and the inversion v = f d sin θ / n hold only when the sound strikes the grating at normal incidence. The chapter never says this outside the worked example, so a student may apply it to an oblique beam.
- ch 8 [low] Exam traps, first trap: The wording 'divide 1.5 mm by 5.0 mm, never by 5.0' is confusing: it does not say that a bare 5.0 is 5.0 m while 5.0 mm is 5.0 × 10⁻³ m, so the reader may not see what is actually wrong with the second division.
- ch 8 [low] Quiz Q3: The question asks how many diffracted beams appear, but the answer counts the zero order, which is the undiffracted transmitted beam. The count and the wording do not match.
