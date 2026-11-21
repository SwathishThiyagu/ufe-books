# me-design-u4: free-model run

- Book: `books/mech/me-design/me-design-u4.html`
- Status: ok
- Model calls so far: 30 (124,674 tokens in, 291,654 out), 7.4 minutes

## Checker

```
me-design-u4.html: 10 chapters, 26894 words, 11 figures, 247 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 4: The formula gives only the moment-induced bolt force. An eccentric tensile load F also produces a direct tensile share F/n in every bolt. The section tells students to add only the moment term to preload, so the total external bolt tension is understated and the force balance is incomplete.
- ch 1 [low] Worked example 1, step 5: The example says the two bolts at (50, 100) and (50, −100) give the largest secondary shear. All four corner bolts have r = 111.8 mm, so all four have the same secondary shear magnitude. Singling out two can mislead students.
- ch 1 [low] Section 2 and Section 4: The symbol F_i is used for preload in Section 2 and again for bolt tensile force in Section 4. The same symbol for two different quantities is confusing when adding them.
- ch 2 [high] Section 3, third paragraph: It says 'For a fillet weld both parts are shear on the throat, so combine them as vectors.' This contradicts the sentence just before it ('Add the direct stress P/A_w algebraically') and it is wrong. For an out-of-plane load, the direct stress and the bending stress are both produced by forces perpendicular to the weld plane, so at any point they act in the same direction on the throat and must be added algebraically. Only the in-plane case (direct shear plus torsional shear) needs a vector sum.
- ch 2 [high] Worked example 1, step 6 and answer: It calls the top of 'either' weld critical. Only the two ends of the weld on the same side as the load line give 46.6 MPa. The other weld, at x = −50, has the torsional shear partly opposing the direct shear: its ends give (−26.5, −14.7) and (26.5, −14.7), that is 30.3 MPa, not 46.6 MPa. A student told 'either weld' would check the wrong corner.
- ch 2 [high] Exam traps, first trap: Wrong percentage. Using h instead of 0.707h multiplies the area by 1/0.707 = 1.414, so the calculated stress is 1/1.414 = 0.707 of the true value: it is understated by about 29%, not 41%. (The true stress is about 41% higher than the wrong value, which is where the number seems to come from.)
- ch 2 [high] Section 2, step list, second bullet: Wrong unit. A_line = ΣL is a length, so it is in mm, not mm². Only after multiplying by the throat thickness does the area A_w = t·A_line come out in mm².
- ch 2 [low] Section 2, explanation of J_line: 'd is the distance from each line's own centroid to the group centroid' is imprecise: d must be measured perpendicular to the weld line, otherwise the parallel-axis term is wrong for groups of unequal or offset welds.
- ch 2 [low] Quiz Q6, answer: The reason given is wrong for the case it names. For two well-separated parallel welds the L·d² term dominates and J_line grows only in proportion to L, so torsional shear falls at about the same rate as direct shear. The L³ growth holds for a single long weld (where r also grows with L, giving about 1/L²).
- ch 2 [low] Worked example 1 and Quiz Q5: Both give 'each 100 mm long' (and '80 mm long') and then use the full length as L, although the chapter defines L as the effective length = actual length − 2h. The reader cannot tell whether 2h has already been subtracted.
- ch 3 [high] Figure (blocks diagram, node 'e'): The flow chart is titled 'Knuckle joint sizing', but it includes a block 'Cotter — shear check' between 'Eye and fork' and 'Joint sized'. A knuckle joint has no cotter; its parts are eye, fork, pin and pin retainer. A student reading the chart will think a cotter is part of the knuckle joint.
- ch 3 [low] Section 2, pin bending sentence: The moment is never written, so the student cannot compute it. The sentence only says 'P at the centre and P/2 at each tine; then σb = M/Z'. The lever arm (half eye thickness plus half tine thickness) is missing.
- ch 3 [low] Section 2, bearing and bending formulas: The symbol σb is used twice with two different meanings: for bearing stress (σb = P/(dpte)) and for pin bending stress (σb = M/Z). In one section the same symbol names two different stresses.
- ch 3 [low] Section 3, 'Socket tearing' bullet: A<sub>net</sub> is described only in words ('the socket wall area left on both sides of the cotter slot'), so a student cannot put numbers into the check that the exam asks for.
- ch 4 [high] Section 2 (Torque, efficiency and self-locking), after the lowering-torque formula: The sentence 'If Tl ≤ 0, the load will not run the screw down by itself' contradicts the chapter's own formula and its own self-locking condition. With Tl = (W dm/2)(μ − tan α)/(1 + μ tan α), Tl ≤ 0 happens when μ ≤ tan α, and that is exactly the overhauling case where the load does run the screw down. The correct self-locking case is Tl > 0 (μ > tan α). As printed, a student who follows the sentence will invert the self-locking test.
- ch 4 [high] Exam traps, fourth trap (collar friction): The trap says a collar 'adds Tc = μc W rc; the screw may no longer self-lock'. This is backwards. Collar friction opposes the load running down, so a collar can only make a screw more firmly self-locking, never less. A screw that overhauls without a collar may be held once a collar is fitted.
- ch 4 [low] Quiz Q6, answer: 'Increase friction (different materials or lubrication)' reads as if lubrication increases friction, which is the opposite of the usual effect and will confuse a student.
- ch 4 [low] Figure caption: The caption says efficiency 'rises with lead angle'. That is true only over the plotted 0–20° range. For μ = 0.15 the efficiency peaks near α ≈ 41° (tan α = √(1 + μ²) − μ) and falls after that, so the sentence is misleading if read as a general rule.
- ch 5 [high] Quiz Q7: The answer says the stress falls when D is increased at fixed W and d. The uncorrected stress 8WD/(πd³) grows in direct proportion to D, and the small fall in Kw does not cancel it. For example, D = 50 mm gives about 347 MPa, while D = 60 mm gives about 405 MPa. A student who reads this answer will learn the opposite of the truth.
- ch 5 [low] Section 2, free length formula: The word 'clearance' appears in Lf = Ls + δmax + clearance but is never defined, so a student cannot use the formula.
- ch 5 [low] Section 3 (and the fatigue sentence): The chapter refers to chapter 4.6 by plain text twice ('see 4.6', 'their load sharing is in 4.6') instead of an inline link, so a reader on a phone cannot jump to it.
- ch 6 [low] Lead: The last sentence, 'This chapter shows how the load divides...', is a table-of-contents sentence, not teaching content; the instructions ask for no such filler.
- ch 6 [low] Section 2, first paragraph: 'At solid height the coils touch, deflection stops and the rate jumps' reads as if the rate of the set rises. Section 1 says the set rate falls to k1 when the inner spring goes solid, so a student can see a contradiction.
- ch 6 [low] Section 2, clearance bullet: The 1 mm gap is not specified as radial or diametral, and it is stated at free length only. Under load the outer spring grows in diameter and the inner shrinks, so the gap closes.
- ch 6 [low] Section 2, bullet 'Deflection at full load': δ_max = W_max/(k1 + k2) holds only while neither spring has gone solid; the bullet is stated as a general rule before the check that follows it.
- ch 6 [low] Section 3, first bullets and quiz Q6: The fractions 0.22 S_ut and 0.35 S_ut are given without their life basis; they are values for steel spring wire at about 10^6 cycles and do not hold for other lives or materials.
- ch 6 [low] Exam traps, fourth trap: The phrase 'roughly 0.22–0.35 and 0.67 of S_ut' sits next to the mention of S_sy, so a student may take S_sy as 0.67 S_ut. S_sy is about 0.45 S_ut.
- ch 7 [high] Section 2 (justification of the deflection formula): The sentence 'The deflection formula treats the stack as one beam with second moment n b t³/12' contradicts the formula it is supposed to explain. A cantilever of constant I = nbt³/12 carrying W at the eye deflects 4WL³/(Enbt³), not 6WL³/(Enbt³). The factor 6 comes from a beam of uniform strength, where the number of leaves (and hence I) grows in proportion to the bending moment from the eye to the centre. A student who checks the factor with I = nbt³/12 will find a factor 4 and lose confidence in the formula.
- ch 7 [high] Section 1, sentence 'They are placed symmetrically on both sides of the master leaf': Graduated leaves are not stacked on both sides of the master leaf. The master leaf is the top (or bottom) leaf of the stack, and all graduated leaves lie on one side of it. What is symmetric is the arrangement along the length about the centre bolt, with equal lengths on each side. The sentence also contradicts the lead ('sit above or below it') and the figure, which shows all graduated leaves below the master leaf.
- ch 7 [low] Section 3, nipping paragraph: 'The residual stress opposes working stress, so the master leaf sees a smaller stress range' is loose. Residual stress does not change the stress range for a given load cycle; it shifts the mean stress. What nipping reduces is the peak (maximum) stress in the master leaf under load.
- ch 7 [low] Figure spec, 'Leaf 1' note: The note reads 'master, b = 75' with no unit, while every other number in the chapter carries one.
- ch 8 [low] Section 2 (arm stresses): The simplified model F = T/(nr) assumes every arm shares the torque equally. With a cast rim that flexes, the arms near the loaded side take most of the torque, so many textbooks design integral arms for the whole torque shared by only half the arms, giving M = 2T/n. A student using F = T/(nr) alone may under-design the arms.
- ch 8 [low] Section 2, formula legend: The text tells the student to 'check σt = Fc/A', but σt is never defined and A appears in the legend attached to a formula block that does not contain σt.

## Correction pass (21 Nov 2026)

- Every chapter rewritten and every example, quiz and bank answer traced by script; new chapters on riveted and bonded joints and on rubber springs (packet order 1 to 10); every figure redrawn by hand from the chapter's worked example; 14 full model answers. The draft figures are kept as figclaude_old1 to 8.
