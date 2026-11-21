# ae-avionics-u6: free-model run

- Book: `books/aero/ae-avionics/ae-avionics-u6.html`
- Status: ok
- Model calls so far: 27 (99,640 tokens in, 209,769 out), 5.7 minutes

## Checker

```
ae-avionics-u6.html: 8 chapters, 14010 words, 9 figures, 151 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 1 and Exam traps, bullet 1: The text says the autopilot and flight director 'fly the command'. The flight director does not move the controls; it only shows steering cues on the attitude display. A student may write in an exam that the flight director is an actuator.
- ch 1 [low] Quiz Q4: The arithmetic is rounded inconsistently. Time is written as 1.333 h, but 2000 x 1.333 = 2666 kg, not 2666.7 kg. The value 2666.7 kg comes from 1.3333 h.
- ch 2 [low] Section 1, the guidance loop: The text says five blocks sit in the loop, but the bullets list only four: seeker, guidance law, autopilot, fin servos. The airframe (the fifth block) is hidden inside the fin-servo bullet, and the fifth bullet just repeats the seeker to close the loop. A student counting blocks will not find five.
- ch 2 [low] Section 2, command guidance (beam riding): Beam riding is put under command guidance, whose stated test is that the guidance computer stays on the ground, launcher or aircraft. In beam riding the missile carries a receiver that senses its own offset from the beam and computes its own steering, so the stated test does not fit without explanation.
- ch 2 [low] Section 2, homing guidance (passive): 'listens for heat, reflected light or the target's own radar' invites confusion: light reflected from a target that is lit by a designator is semi-active laser homing, not passive homing.
- ch 2 [low] Section 3, classical and modern: The list of classical laws names 'LOS' as well as CLOS, but LOS guidance is never defined in the chapter, and the navigation family lists only pursuit, CLOS and PN. A student cannot tell how LOS guidance differs from CLOS.
- ch 2 [low] Section 2, SACLOS: SACLOS is expanded only as 'semi-automatic', which is not the full name of the abbreviation.
- ch 2 [low] Quiz Q6: The question hands the student the answer by stating 'command guidance with a CLOS rule' and then asks the student to classify it on both axes.
- ch 3 [high] Section 2, Passive bullet: The list of energy a passive missile listens to includes 'a radio command'. A command from the launcher is not radiation emitted by the target, so it does not fit the definition of passive homing given in the same paragraph and in the exam trap.
- ch 3 [high] Section 3 table, Command row, Range column: The table says command guidance has 'Long for radio or wire' range, but Section 1 says the wire link 'limits range', and the Quiz Q5 answer repeats that the cable length limits range. The two statements contradict each other.
- ch 3 [low] Section 2, first paragraph: 'The seeker measures the target's direction, and the missile's own computer steers to reduce that angle' is loose. A homing missile does not drive the line-of-sight angle to zero; it drives the line-of-sight rate to zero (proportional navigation).
- ch 4 [high] Section 3 (CLOS and beam riding): The sentence 'Errors are small near the launcher and grow in angle with range' is backwards. For a fixed sideways miss distance the angle it subtends at the launcher gets smaller as range grows, not bigger. What actually grows with range is the linear miss produced by a given angular (tracking) error, and the lateral acceleration the missile needs to stay on the swinging line. As written, a student will conclude that the angular error itself increases with range, which contradicts the same chapter's Exam trap 4 and Q5.
- ch 4 [low] Exam traps, trap 4: 'CLOS error grows with range even for a perfect missile, because a fixed miss distance subtends a smaller and smaller angle' gives a cause that does not lead to the stated effect. A shrinking angle by itself makes nothing worse; the growth comes from the tracker's finite angular resolution, which the sentence never mentions. With a truly perfect missile and perfect tracking the error would be zero.
- ch 4 [low] Section 2 (pure and deviated pursuit): 'From the front or the side the path is nearly straight' is only true for the head-on case. Against a crossing (side) target the missile turns noticeably, because it must keep swinging its heading onto a LOS that is being dragged sideways. Only a head-on, near-zero-β geometry is close to straight.
- ch 4 [low] Quiz Q6 answer: 'the LOS rate stays high' in a tail chase is wrong as stated. In a tail chase the closing speed is low, so the range R stays large and the LOS rate (which varies as Vt sinβ / R) is small for most of the flight. What is large is the total heading change the missile has to hold for a long time, plus the terminal lateral demand as R shrinks.
- ch 4 [low] Figure (engagement geometry): The node positions do not match the stated speeds. With M at (0,1), T at (2,1) and C at (4,3), the missile path |MC| = 4.47 units and the target path |TC| = 2.83 units, a ratio of 1.58, but 600 m/s against 300 m/s demands 2.0. The sine rule fails too: missile heading is 26.6° off the LOS against the 20.8° a collision course needs for those speeds. A student who checks the drawing against the worked example finds a contradiction.
- ch 5 [low] Lead, first paragraph: The lead says PN needs angle measurements 'not target range or target speed', but Section 2 requires the closing velocity Vc as a gain in a = N Vc λ̇. A student can read the lead as 'Vc is never needed'.
- ch 5 [low] Section 3, table, IPN row: The IPN row puts 'exact geometry' under Command and 'exact' under 'Perpendicular to', which are not a command and not a direction. The other rows give a formula and a direction, so the row reads as if it were unfinished.
- ch 5 [low] Exam traps, fourth bullet (sign of LOS rate): 'A sign error doubles the miss instead of removing it' states a specific factor that is not generally true; a reversed sign simply turns the missile away from the collision course and the miss grows without any fixed factor of two.
- ch 5 [low] Section 2, definition of N: N is called 'the effective navigation ratio'. Most textbooks reserve 'navigation ratio' for the constant N in the law and 'effective navigation ratio' for the value after kinematic effects; using the long name here without the short one can confuse the reader when the usual 3 to 5 range is quoted.
- ch 6 [low] Lead: The lead promises three ways to steer, but the third item (skid-to-turn versus bank-to-turn) is a turn convention, not a steering effector. A student may expect three hardware types in Section 2 and get only two plus a body-orientation choice.
- ch 6 [low] Section 2, bank-to-turn: 'BTT gives more lift per degree of angle of attack' is misleading. For the same angle of attack the body lift is essentially the same; the real BTT gain is that it can fly at a higher usable angle of attack (all lift in one plane, small skid angle), so it produces more lift before the limit and better lift-to-drag.
- ch 6 [low] Quiz Q3: 'Why are fins useless during boost?' is too broad. Boost lasts seconds and speed, hence q, rises quickly; the trap section itself says 'at launch'. The answer repeats the over-general claim.
- ch 6 [low] Section 3, gyro sentence: 'Gyros (rate, free, dynamically tuned) sense the resulting motion' sits inside the fin-actuator discussion, so 'the resulting motion' reads as the fin's motion. Gyros sense the missile body's angular rate or attitude and feed the autopilot, not the fin loop.
- ch 6 [low] Lead: 'Every homing missile is built around this chain' contradicts Section 2 and the Beyond box, which describe exo-atmospheric interceptors steered by reaction jets where fins do nothing.
- ch 7 [high] Section 3 (formula block and bullet steps), Worked example 1 (steps 4–5 and answer), Exam trap 2, Quiz Q3: The lift relation is wrong. After the roll, the lift plane contains the commanded acceleration vector, so the wing must produce the full command magnitude a_total, not a_total cos φ. The quantity a_total cos φ is only the in-plane component of the command before rolling (equal to √(a_total² − a_side²)); it is not the lift. As written the example is physically impossible: the missile is said to accelerate at 8 g while the wing gives only 6.93 g, and nothing supplies the remaining 4 g sideways component. The same slip makes Exam trap 2 and Quiz Q3 answers wrong.
- ch 7 [high] Section 1, sentence on gyros: A dynamically tuned gyro does have a spinning rotor (spun by a small motor); only the ring laser gyro and the fibre optic gyro have no spinning mass. The sentence wrongly groups all three as mass-free.
- ch 7 [low] Worked example 1, step 1: Accelerations are quoted in g but g is never defined, while the rest of the chapter uses m/s².
- ch 8 [low] Section 1 formula and Worked example 1: The formula defines P_load as 'the payload plus bus load', but the worked example says only 'a 500 W payload' and then uses 500 W as P_load. A student copying the method may forget to add the housekeeping/bus load, which the same chapter warns about in the exam traps.
- ch 8 [low] Exam traps, third bullet: 'a Celsius value can give a negative or wildly wrong area' is wrong on the negative part: T is raised to the fourth power, so T⁴ is never negative and the computed area is always positive, just badly wrong. The claim teaches a false symptom.
- ch 8 [low] Quiz Q5: The answer says the wheel 'reaches its limit and can give no more torque'. Saturation is a speed limit, not a torque limit: the wheel cannot store more momentum once it hits maximum speed, and torque authority is largely unaffected until that point.
- ch 8 [low] Exam traps, second bullet: 'which triples the capacity' overstates the number: 96 ÷ 35 ≈ 2.74, so the capacity grows to about 2.7 times, not three times.
- ch 8 [low] Section 1, shunt regulator sentence: 'dumps surplus array current into a resistor or a switch when the battery is full' is unclear: a switch is not a place to dump current. The second alternative is shorting (shunting) the array itself.
