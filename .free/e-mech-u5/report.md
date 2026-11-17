# e-mech-u5: free-model run

- Book: `books/common/e-mech/e-mech-u5.html`
- Status: ok
- Model calls so far: 23 (82,967 tokens in, 186,799 out), 4.6 minutes

## Checker

```
e-mech-u5.html: 8 chapters, 14258 words, 9 figures, 144 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Quiz Q1: The question asks the student to write v and a "in terms of s", but the expected answer gives derivatives with respect to t (ds/dt, d²s/dt²) plus v dv/ds. A student cannot tell whether position s or the variable s is meant, and may try to express everything as a function of s alone.
- ch 1 [low] Section 3, cases 1 and 3: The symbol s₀ appears in the integrated formulas (s = s₀ + ∫₀ᵗ v(τ)dτ and the limits of ∫ₛ₀ˢ f(s) ds) without ever being defined, though every other symbol in the chapter is defined.
- ch 1 [low] Section 3, case 3: The integral ∫ₛ₀ˢ f(s) ds uses s both as the upper limit and as the integration variable, which is loose notation a student may copy into an exam.
- ch 1 [low] Quiz Q5: The answer leaves out two things a marker would want: the unit of k (s⁻¹, so that kt is dimensionless) and the fact that the solution assumes v is never zero. It also should note why real drag problems use a = −kv rather than +kv.
- ch 2 [high] Figure (aria text and edges from 'v'): The figure description says the velocity splits into a tangential part and a normal part, and draws edges from 'Velocity v' to a_t and a_n. Velocity never splits: it has no normal component (as Quiz Q2 correctly states). It is the acceleration that splits into a_t and a_n.
- ch 2 [low] Section 1: The direction formula tan⁻¹(a_n/a_t) is undefined when a_t = 0 (constant-speed motion), the very case used in Q3 and Q5, so a student may be stuck.
- ch 2 [low] Section 2 table: 'r̈ | radial speed change' is imprecise. r̈ is the rate of change of the radial velocity ṙ, not a change of speed; the body text wording 'radial speeding up' has the same looseness.
- ch 2 [low] Section 2, last sentence: The remark 'ax = ẍ and ay = ÿ; these are just Cartesian components' belongs to the rectangular-components topic and is dropped in without use; it distracts from the radial-transverse derivation.
- ch 3 [low] Lead: The definition 'a particle thrown into the air' does not cover a body projected horizontally from a height, which Section 3 itself treats as a projectile. A student may think horizontal projection is not projectile motion.
- ch 3 [low] Section 1: Mass m appears in 'the only force is weight mg downward' but m is never defined, though every other symbol is.
- ch 3 [low] Section 3: 'Set y = 0 and solve' is incomplete; solve for what is not stated.
- ch 3 [low] Figure: The plotted curve runs past the landing point down to y = −0.40 m at x = 36 m, while the y-axis minimum is 0 m, so part of the drawn path is physically meaningless ground-level clipping beyond the range of 35.3 m.
- ch 4 [low] Section 1, first paragraph: The letter A is used for two different things. The first sentence makes A a frame ('Let frame B move relative to frame A'), but the next sentences make A the moving particle ('the velocity of particle A as seen from B', 'v_A is the velocity of A measured in the ground frame'). A student can lose track of what A and B stand for.
- ch 4 [low] Section 1, paragraph 3: The line 'The same rule holds for acceleration when B has constant acceleration: a_A = a_B + a_A/B' adds a condition that is not needed, and the symbol a_A/B is never defined. For any translating frame, whether the acceleration is constant or not, a_A/B = a_A − a_B. Only rotation of the frame spoils the rule, not changing acceleration.
- ch 4 [low] Exam traps, third bullet: The sentence 'Then the length is not constant, dL/dt is not zero' is wrong as written. The string is inextensible, so its total length is constant and dL/dt = 0 always. What goes wrong with a moving datum is that the sum of segments you wrote is not the total string length, so setting its derivative to zero gives a false relation.
- ch 5 [high] Exam traps, bullet 1: The consequence is stated backwards. If a student draws the inertia force and still writes ΣF = m a with all drawn arrows, the equation becomes (real net force) − m a = m a, so m a is counted twice and the reported acceleration comes out half the correct value, not double. With the worked-example numbers: 173.2 − 97.6 − 50a = 50a gives a = 0.756 m/s², which is half of 1.51 m/s².
- ch 5 [low] Worked example 1, step 7: Rounding slip. 50 × 1.51 = 75.5 N, not 75.6 N. The balance 173.2 = 97.6 + 75.6 only closes if a is carried as 1.512 m/s².
- ch 5 [low] Section 2, normal-tangential paragraph: The acceleration components are written as the English words at and an ("at changes the speed and an changes the direction"), which a student will read as the preposition and the article. The rest of the chapter uses <sub> tags.
- ch 5 [low] Section 2, cylindrical axes sentence: "taking ar and aθ from 5.2" is a bare section number: the symbols are not formatted and there is no link, so on a phone the reader cannot jump to the derivation of a<sub>r</sub> and a<sub>θ</sub>.
- ch 5 [low] Section 3, bullet on moments: The section talks of brackets carrying an accelerating motor and of taking moments, which invites rigid-body use, but only the inertia force is mentioned. A body that also spins needs an inertia couple, so a student may apply the rule to a rotating bracket and drop that term. The chapter is written for particles, so the gap is easy to close.
- ch 6 [high] Lead: The lead says that when a force 'depends only on position' its work can be stored as potential energy. Position dependence alone does not make a force conservative in three dimensions; the work must also be path-independent.
- ch 6 [low] Section 3: The sentence 'the force field itself is the conservative force field' is tautological and confusing.
- ch 6 [low] Quiz Q1: The question asks to define each symbol, but the answer defines only U₁₋₂ and T; m and v are not defined.
- ch 6 [low] Figure: 'falls 2.5 m down a smooth incline' can be read as 2.5 m along the incline, but 2.5 m is the vertical height and the incline length is 5 m.
- ch 6 [low] Worked example 1: The example does not state the standard assumption that the block passes from the incline onto the floor without losing speed at the junction.
- ch 7 [low] Section 1, first bullet paragraph: Saying impulse is 'a vector in N·s, pointing along the force' is loose when the force changes direction during contact; the impulse points along the vector integral ∫F dt, not along any one instantaneous force direction.
- ch 7 [low] Section 2, derivation line: The step F = ma = m dv/dt is integrated as if m is constant, but the chapter later mentions variable-mass rocket motion in 'Beyond'; the constant-mass condition should be stated so students do not apply the integrated form to a rocket.
- ch 7 [low] Section 2, last line: The reference to the next chapter 5.8 is written as plain text instead of the book's chapter link tag, so readers on a phone cannot jump to it.
- ch 8 [low] Section 1: The sentence 'It is the only direction in which the collision changes velocity' is stated as a general fact, but it holds only for smooth contact. A rough contact also changes the tangential velocity, and the chapter itself later qualifies the tangential part with 'when the contact is smooth'. A student reading Section 1 first may take the unqualified claim as universal.
- ch 8 [low] Worked example 1, step 2: The symbols u_A and u_B appear for the first time in step 2 ('e(u_A − u_B)') and are never defined; the problem statement gives only the numbers 6 m/s and 3 m/s.
- ch 8 [low] Figure caption and quiz Q6: The figure note 'the final speeds are 4.5 m/s and 6.0 m/s' does not say which body gets which value, so the faster final speed could be attached to the wrong mass. Similarly the Q6 answer uses u₁ and u₂ without defining them as the velocities before impact.
