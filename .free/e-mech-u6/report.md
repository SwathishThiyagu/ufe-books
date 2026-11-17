# e-mech-u6: free-model run

- Book: `books/common/e-mech/e-mech-u6.html`
- Status: ok
- Model calls so far: 26 (95,817 tokens in, 209,931 out), 5.3 minutes

## Checker

```
e-mech-u6.html: 8 chapters, 15822 words, 9 figures, 153 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 3: The sentence says the rim stress in a flywheel 'grows with ω²r'. Hoop (rim) stress in a thin ring is σ = ρv² = ρω²r², so it scales with ω²r², not ω²r. The 'Beyond' note later in the same chapter states ρω²r² correctly, so the two statements contradict each other.
- ch 1 [low] Figure caption: 'The two simple motions a rigid body can have' reads as if a rigid body can only translate or only rotate about a fixed axis. A body can also have general plane motion, combining both; the caption overstates the list.
- ch 2 [low] quiz Q5: The closing sentence says the ladder's midpoint 'is the centre only in special positions'. For a ladder with a horizontal foot velocity and a vertical top velocity the instant centre is fixed by geometry: it sits at the corner point (foot x, top y), level with the top and directly above the foot. The midpoint of the ladder is at (foot x / 2, top y / 2), so it can never coincide with the instant centre. The claim invents 'special positions' that do not exist.
- ch 2 [low] figure caption: The caption says 'Notice the two equations in the last row', but the figure is laid out top to bottom, so there is no row of two equations; the velocity equation and the acceleration equation are two separate boxes, one below the other.
- ch 3 [low] Section 3, four-bar paragraph: The sentence 'Acceleration uses the normal accelerations of both cranks and the coupler' lists only normal terms for the coupler, so a student may think the coupler contributes no tangential term. The coupler contributes both α_AB × r and −ω²r.
- ch 3 [low] Exam traps, fourth bullet: The trap 'Using a velocity triangle when the directions are not perpendicular to AB and assuming a right angle that is not there' is worded so loosely that the student cannot tell which triangle is meant or which right angle is being wrongly assumed.
- ch 4 [high] Section 2, sentence before Worked example 1: It says the worked example uses a bar at a general slant, not touching walls. But the example has A at (0.9, 0) m and B at (0, 1.2) m with horizontal and vertical velocities. That is exactly the floor-wall (ladder) case: A lies on y = 0 and B on x = 0. The sentence contradicts the example and the figure.
- ch 4 [high] Section 3; Exam traps 1 and 2: The text overgeneralises: 'It does not have zero acceleration' and 'never write aP = ω² rP or aP = α rP about I' and 'treating I as fixed' are not true for fixed-axis rotation. In fixed-axis rotation, I is fixed on the axis, its acceleration is zero, and fixed-axis acceleration formulas about that axis are valid. The caution applies only to general plane motion with a moving instantaneous centre.
- ch 4 [low] Section 3: 'For general plane motion, I changes with time and is not the mass centre' is too absolute. The instantaneous centre can coincide with the mass centre at an instant, for example when the mass centre is instantaneously at rest.
- ch 5 [low] Section 2 (kinetic diagram bullets) and Quiz Q6: The chapter first says correctly that the kinetic diagram carries m aG and IG α and that the inertia terms carry a minus sign in D'Alembert form, but Q6 calls m aG and IG α 'inertia terms'. The figure edge label 'add inertia' on the KD step repeats the same slip. A student can end up drawing −m aG on the KD, which is the opposite of what Section 2 teaches.
- ch 5 [low] Exam traps, fifth bullet: 'Using ΣF = m aG for a point other than G' is garbled. ΣF = m aG is always true, whatever point you think about; the error being warned against is writing ΣF = m aP with the acceleration of a point P that is not the mass centre.
- ch 5 [low] Quiz Q8 answer: The answer makes ΣMG = 0 look conditional on there being no applied couple. In pure translation ΣMG = I<sub>G</sub> α = 0 always, because α = 0; an applied couple cannot be present in pure translation, since it would itself produce α.
- ch 6 [high] Exam traps, trap 1: The trap says it is wrong to use H = Iω when I is taken about a point that is 'not on the rotation axis or not G'. That contradicts Section 1, which correctly teaches H_O = I_O ω for a fixed axis through O, where O is on the axis but is usually not G. A student will read the trap and think the valid I_O formula is a mistake.
- ch 6 [low] Figure (block 'change'): The note gives a bare number 'H₂ − H₁ = −100' with no unit, while every other number in the chapter carries a unit.
- ch 7 [high] Section 2, paragraph on normal reaction and gravity: The sentence 'Normal reaction and gravity at the mass centre do no work when they stay perpendicular to the motion' is then used to explain why 'a rolling body on an incline goes faster as the drop grows'. On an incline gravity is not perpendicular to the motion: it does work m g h, and that work is exactly what speeds the body up. A student reads that gravity does no work and then sees the body gain speed, which contradicts the physics and the worked example that follows.
- ch 7 [low] Section 2, conservation formula line: The 'where' line is grammatically broken: 'where: holds when only conservative forces (gravity, springs) do work.' It does not say what the symbols are or what the condition attaches to.
- ch 7 [low] Exam traps, third bullet: 'using I about the contact point without adding m d² by the parallel axis theorem' is misleading. For a body rolling without slip, T = ½ I_C ω² with I_C = I_G + m r² taken about the instantaneous contact point is a correct and standard shortcut, not an error. As written, a student may think the contact-point route is always wrong.
- ch 8 [high] Figure (displacement of the worked example): The plotted curve is x = 0.05 sin(20t), which starts at x = 0 at t = 0. The worked example says the mass is pulled down 0.05 m and released from rest, so at t = 0 the displacement must be at its extreme value (+A if down is positive). Section 2 of the chapter itself states this rule (x = A cos ω_n t for release from rest), so the figure contradicts both the example and the text. A student matching the graph to the example will be confused about the phase.
- ch 8 [low] Section 3: "1 Hz = 1 cycle/s = 2π rad/s" mixes two different quantities. Hz measures cycles per second; rad/s measures angular frequency. The correct link is ω = 2πf, so f = 1 Hz corresponds to ω = 2π rad/s. As written it reads like a unit conversion and sits awkwardly next to the advice to keep ω_n and f separate.
- ch 8 [low] Exam traps, second trap: "8 N/cm is 800 N/m, so the frequency changes by a factor of 10 in ω_n" is loosely worded: it does not say which way, and 'the frequency changes' sounds as if k itself changed. The point is what happens to the student's answer when the conversion is skipped.
