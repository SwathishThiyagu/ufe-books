# me-fluid-u7: free-model run

- Book: `books/mech/me-fluid/me-fluid-u7.html`
- Status: problems
- Model calls so far: 28 (101,339 tokens in, 224,922 out), 5.9 minutes

## Checker

```
me-fluid-u7.html: 8 chapters, 13971 words, 9 figures, 152 KB
PROBLEMS:
 - text contains "as an AI"
```

## For the reviewer

- chapter 1: the figure cannot be drawn: tree is too wide (7 leaves); use fewer leaves or shorter labels
- chapter 1: the figure could not be drawn; a plain box diagram stands in for it
- checker: text contains "as an AI"

## Reviewer notes (after any revision)

- ch 1 [low] Lead and Section 1: The opening line says every rotodynamic pump works because 'a spinning impeller flings the liquid outward'. Axial-flow and mixed-flow pumps are rotodynamic but do not throw liquid outward; in an axial pump the liquid is pushed along the shaft. A student can read the lead as saying axial pumps are not rotodynamic, which contradicts the family tree in Section 2.
- ch 1 [low] Section 2, centrifugal bullet: 'Medium to high head with large flow' overstates a plain centrifugal pump. A single-stage centrifugal pump gives large flow at low to medium head; high head needs multistage impellers or higher speed. The chapter itself says later that one impeller cannot lift water from deep down a borewell, which contradicts 'high head' here.
- ch 1 [low] Worked example 1, step 4: The test uses a size rule — 'millilitres to a few tens of millilitres per revolution' — that no textbook gives and that is not defined anywhere in the chapter. Large plunger and gear pumps with a trapped volume of 0.8 L per revolution do exist. The conclusion is right, but the reason given is a made-up threshold and a careful student can argue with it.
- ch 1 [low] Quiz Q5: The answer calls 0.103 L per revolution 'large for a small displacement pump' and concludes 'more likely rotodynamic'. A gear pump of about 100 mL per revolution running at 2900 rpm is a real machine and would give exactly this duty, so the volume alone does not settle the family. The reasoning is also loose next to Worked example 1, where 0.83 L per revolution is called absurd.
- ch 2 [low] Section 2, paragraph 'Inside the impeller, shaft power becomes kinetic energy': The sentence says shaft power becomes only kinetic energy. The impeller also raises the static pressure of the water, so a student can wrongly conclude that all pressure rise happens in the casing and none in the impeller.
- ch 2 [low] Section 2, formula p_eye = p_atm − ρ g (H_s + h_fs): The formula leaves out the velocity head needed to give the water its speed at the eye (and any loss in the eye itself). Quiz Q6 then counts 'the velocity head at the eye' as part of the margin, so the two parts disagree.
- ch 2 [low] Section 1, list of parts: The delivery valve and the priming plug are used in Section 2 ('start with the delivery valve closed', 'open the delivery valve slowly', 'fill through the priming plug') but are never named or described in the parts list.
- ch 2 [low] Worked example 1, part (c): 'The impeller develops the same 3 m of head in air' has no antecedent. The only 3 m earlier in the problem is the suction lift, not a head, so the reader cannot tell where this 3 m comes from.
- ch 2 [low] Worked example 1, output block: The third output 3.6 is printed without its unit, while the answer text gives 3.6 mm; the reader has to guess whether it is metres or millimetres.
- ch 3 [high] Section 2, sentence after the flange formula: The sentence "Hydraulic losses make Hm e." is truncated and meaningless. The key inequality Hm < He — the whole point of the section — is lost.
- ch 3 [high] Quiz Q2: The answer says leakage and mechanical losses consume part of the impeller work and so lower Hm. Mechanical losses occur outside the fluid (bearings, gland, shaft) and do not reduce the head imparted per unit weight; leakage lowers the delivered discharge (a volumetric effect), not the head per unit weight. Only hydraulic losses inside impeller and casing (friction, shock, eddy formation) make Hm smaller than He.
- ch 3 [low] Section 2, manometric efficiency formula note: Calling manometric efficiency simply "(hydraulic) efficiency" is loose. Many books reserve hydraulic efficiency for the impeller alone, i.e. the ratio of actual head to the ideal Euler head after allowing for slip, which is a different number.
- ch 4 [low] Section 1, first paragraph of the derivation: The sentence 'The pressure head the pump must produce is the manometric head Hm' calls Hm a pressure head. The manometric head is a total head in metres; it contains the pressure rise, the velocity head difference and the elevation difference. Calling it a pressure head can make a student read Hm as p/(ρg) only.
- ch 4 [low] Section 1, opening sentence: 'At standstill the impeller cannot push water into a delivery pipe that already needs a pressure head' mixes up standstill with low speed. At standstill the impeller gives no head at all; the argument is about speeds below Nmin, where the head exists but is smaller than Hm.
- ch 4 [low] Section 1, formula note on eta_man: The note does not say which operating point eta_man belongs to. At shut-off the useful hydraulic power is zero, so the efficiency there is zero, and a student may wonder why a non-zero eta_man is put into the formula.
- ch 4 [low] Quiz Q6 answer: The closing claim 'flow increases by less than double' is only true when pipe friction dominates the system curve. If the system is mostly static head (a deep borewell lift, for example), doubling the head can more than double the flow, so a student can carry away a wrong general rule.
- ch 5 [high] Section 3 (NPSH required and safe running): The sentence 'NPSHR rises with flow and speed, so a pump that is safe at design flow may cavitate when throttled or run faster' contradicts itself and the rest of the chapter. Throttling the discharge reduces flow, so NPSHR falls; the chapter's own Q8 correctly says cavitation risk grows at higher flow. As written, a student will think closing the delivery valve causes cavitation.
- ch 5 [low] Section 3, Thoma cavitation factor: The standard textbook definition is that the Thoma cavitation factor σ is NPSHA/H, and its critical value σ_c (at which cavitation begins) is NPSHR/H. Presenting only σ = NPSHR/H labels the critical value with the plain name.
- ch 5 [low] Section 2, explanation of terms: 'The second is the head spent in boiling the liquid' is misleading. p_v/(ρg) is the head equivalent of the vapour pressure, that is, the absolute pressure at which the liquid boils at that temperature; nothing is 'spent' in boiling.
- ch 5 [low] Section 3, definition of NPSH required: Saying NPSHR is the NPSHA at which the maker 'guarantees cavitation-free operation' is too strong. By standard test practice it is the NPSH at which the pump head has dropped by a fixed small amount (commonly 3%) from the cavitation-free value, so it already contains an acceptance margin, not a zero-cavitation guarantee.
- ch 6 [high] Quiz Q4 answer: The head term is written as plain text '243/4' instead of 24 to the power 3/4. Read literally, 243/4 = 60.75, which does not match the 10.84 shown next, so the working looks self-contradictory and a student may copy the wrong exponent.
- ch 7 [high] Section 4 (work and power formulas): The sign is wrong. If hs is a suction lift and hd is the delivery height, the cylinder pressure during suction is (patm − ρg hs) and during delivery it is (patm + ρg hd). So the pressure difference across the stroke, and hence the work per stroke, is ρg(hd + hs)AL, not ρg(hd − hs)AL. As written, a pump lifting water 4 m and delivering 20 m would show a total head of 16 m instead of 24 m.
- ch 7 [high] Exam traps, last bullet: Wrong number. Slip fraction = 1 − C<sub>d</sub>, so C<sub>d</sub> = 0.92 means a slip fraction of 0.08, that is 8 % slip, not 12 %. The trap text states the opposite of the chapter's own quiz Q5, which correctly gets 8 %.
- ch 7 [low] Section 4 (real indicator diagram): 'Both lines are wavy, flattest at mid-stroke where piston speed is highest' gives the wrong reason. The lines come closest to the ideal levels at mid-stroke because the acceleration of the water column is zero there, not because the piston is fastest. At mid-stroke the piston is fastest, so friction, not acceleration, is at its largest at that instant.
- ch 7 [low] Quiz Q7 answer: The ratio of ideal power to actual (indicated) power is not the pump's overall efficiency. Overall efficiency is the water power actually delivered divided by the shaft power input, and it also carries the bearing, gland and seal losses that never appear on the indicator diagram.
- ch 7 [low] Quiz Q7 answer: The extra area is said to be spent 'on accelerating the water column'. Work done against acceleration is stored in the moving water and given back during the deceleration half of the same stroke, so over a full stroke it adds nothing to the enclosed area.
- ch 8 [low] Quiz Q7: The arithmetic is slightly off: 3/(2π²) = 0.15198, which rounds to 0.152 (15.2%), not 0.151 (15.1%). The corresponding saving is 84.8%, the same value quoted in Section 3 and the worked example, not 84.9%. A student comparing Q7 with the worked example will see two different savings for the same physics.
- ch 8 [low] Exam traps, third trap: "Do not apply the π² formula ... to the suction pipe" is misleading. If a large air vessel is fitted on the suction pipe, the suction-pipe friction head also becomes steady at h_s,max/π² by exactly the same argument; what the π² result does not cover is acceleration head, which is the suction vessel's main job.
- ch 8 [low] Section 1, final paragraph: "The mean of sin² θ is 1/2, but work uses the integral of sin³ θ ... That is the source of the 2/3 factor" can make a student think 2/3 is the average value of sin³ θ. The average of sin³ θ over the stroke is 4/(3π) ≈ 0.424, not 2/3.
