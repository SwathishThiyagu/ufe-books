# me-ic-u5: free-model run

- Book: `work/me-ic-u5/tree/books/mech/me-ic/me-ic-u5.html`
- Status: ok
- Model calls so far: 33 (127,469 tokens in, 271,784 out), 6.3 minutes

## Checker

```
me-ic-u5.html: 8 chapters, 22936 words, 10 figures, 223 KB
OK
```

## For the reviewer

- chapter 7: the figure cannot be drawn: tree label "Improve performance" is too long; shorten it
- chapter 7: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [high] Quiz Q7: The torque conclusion is wrong and contradicts the book's own formula T = bmep × V_d / (2π n_R). With n_R = 2 in the denominator, the four-stroke gives HALF the torque of the two-stroke, not twice. As written the answer also contradicts itself: if the four-stroke had twice the torque at the same speed it would also make twice the power, not half.
- ch 1 [low] Section 3, equivalence ratio sentence: A comparison sign has dropped out: the sentence reads 'so φ  1 is rich', leaving the student unable to tell whether rich means φ > 1 or φ < 1.
- ch 1 [low] Quiz Q3: The answer says bmep 'stays nearly constant over the useful speed range', but bmep is proportional to torque at fixed swept volume, so it rises to a peak and falls exactly as the torque curve does (Section 4 of this chapter says so). The real reason bmep is fairer is that it normalises by swept volume, not that it is flat with speed.
- ch 2 [high] Quiz Q6: The question says the motoring test on a cold engine gives a higher friction power, but the second reason in the answer (no combustion gas pressure behind the rings) works in the opposite direction: less gas pressure behind the rings means less ring force on the bore and therefore lower friction, not higher. A student reading this cannot tell which effect is being claimed.
- ch 2 [low] Exam traps, third bullet: "That doubles IP and drops mechanical efficiency to about 50 %" is loose. Doubling IP halves the efficiency; the answer is only near 50 % by accident, and for the 85.5 % example it falls to about 43 %.
- ch 2 [low] Lead: The lead says friction power is found "by the Morse test, the motoring test, or Willan's line", but Section 3 and the exam traps say the Morse test gives indicated power, with friction power following by subtraction. The two statements contradict each other.
- ch 2 [low] Figure and its caption: The caption says "only the left-hand path starts from a measured quantity", but the Morse test also starts from measured brake powers (the cut readings are brake powers read on the dynamometer). The title says "Three routes" while the diagram shows only two, with no node for the motoring test or Willan's line.
- ch 3 [low] Exam traps, third bullet: The phrase 'so the engine never drinks during filling' is literally false and confusing: while the burette refills the engine does drink, from the main tank. A student can read it as 'the engine is stopped during filling'.
- ch 3 [low] Worked example 1, step 6: The label '0.00236 kg per cycle-set' is loose. ρ_a × V_s is the mass of air swept by all cylinders in one revolution, not per cycle or per 'cycle-set'.
- ch 3 [low] Section 1, gas fuels bullet: The formula ρ = p/(R T) is given without saying which R. The chapter defined R = 287 J/(kg·K) for air earlier, so a student may wrongly use 287 for CNG or hydrogen.
- ch 3 [low] Exam traps, first bullet: 'a volume ratio near 31 is meaningless' is puzzling: 31 is the mass-based AFR of this example, and the reason a volume ratio is wrong does not depend on that number.
- ch 4 [high] Section 1 bullet on DC generator vs Quiz Q6: The Section 1 bullet says a DC generator dynamometer 'can also motor the engine', but Q6 asks for a difference between a motoring and a generator dynamometer and the answer says a generator dynamometer 'only absorbs power from the engine'. The tree also puts DC generator only under Absorption. A student reads one page and finds two opposite statements.
- ch 4 [low] Quiz Q5: A rope brake has no torque arm. Its torque is (W − S) × R, where R is the effective radius of the flywheel plus rope. Calling it 'the arm is 0.5 m' mixes the rope brake with the torque-arm brake of Section 1.
- ch 4 [low] Exam traps, third trap: The trap is headed 'Putting rev/min straight into 2πNT/60', but the formula already contains the /60. The sentence then says N must be in rev/min, which reads as if the trap is about the opposite mistake. The real mistake is dropping the 60.
- ch 4 [low] Section 1 (eddy-current bullet) vs Section 2: The eddy-current brake is described as having 'fast control', while Section 2 says an absorption dynamometer sets load 'by hand or by a slow controller'. The two statements pull against each other.
- ch 4 [low] Worked example 1, step 2: The line '2π × 1500 × 60 / 60' shows two 60s with different meanings (one is T = 60 N·m, the other is the minutes-to-seconds factor) with no label, which invites the wrong cancellation.
- ch 5 [low] Worked example 1 and Quiz Q4: The exhaust mass flows given are large for the stated fuel flows. 3.0 kg/h of fuel with m_g = 0.045 kg/s (162 kg/h) implies an air-fuel ratio near 53:1, and Q4 gives about 44:1. A student who has just learnt m_g = m_a + m_f may try to check the numbers and get stuck on an air-fuel ratio that is far leaner than a small diesel at full load.
- ch 5 [low] Section 2, bullet on exhaust gas flow: The mass balance is written as m_g = m_a + m_f with no units, while section 1 defines m_f in kg/h and section 2 uses m_g in kg/s. That is exactly the unit mixing the exam traps warn against.
- ch 5 [low] Quiz Q4 answer: The subtraction is shown as 47.78 − 12 − 5.57 − 19.95 = 10.25 kW, but those figures give 10.26 kW (exact value 10.256 kW). The percentage is unaffected.
- ch 5 [low] Section 1, definition of P_u: P_u is said to include 'heat to the lubricating oil', but if the lube oil is cooled by the jacket water, that heat already appears inside P_c and would be counted twice.
- ch 5 [low] Beyond: 'Research engines now add a fifth stream, unburnt fuel and CO in the exhaust' clashes with section 1, where unburnt fuel is already folded into P_u as part of the remainder.
- ch 6 [high] Figure (brake thermal efficiency vs speed): The 10° retarded curve lies above the MBT curve at low speed: at 1000 rpm retarded gives 24.04 % while 'MBT timing' gives only 21.04 %. The curves cross near 1350 rpm. MBT timing is defined in Section 2 as the timing that gives the highest brake torque (and hence best efficiency) at a given speed and mixture, so a retarded curve can never be above it anywhere. A student reading the graph will learn the opposite of the definition.
- ch 6 [low] Section 3, coolant and oil temperature: 'Cold coolant and cold oil raise friction and poor fuel vaporisation' is grammatically broken and a student may read 'raise ... poor fuel vaporisation' as raising a quantity rather than worsening it.
- ch 6 [low] Section 1: 'Brake thermal efficiency is the inverse idea' is vague; it does not say what is inversely related to what.
- ch 6 [low] Section 2, lean mixture and best efficiency: The reason given for the lean best-efficiency point, 'because there is less fuel for the same work', is circular and does not match the standard explanation.
- ch 6 [low] Lead paragraph: 'Engine ratings exist so that these effects are separated from weather and test-cell conditions' is unclear — ratings do not remove the effects, they state the reference conditions.
- ch 7 [low] Section 3, trade-off paragraph: "advanced injection raises NOx" can be misread as "improved injection". The meaning is advancing the injection timing, which is the opposite of retarding it to cut NOx.
- ch 7 [low] Section 3, trade-off paragraph: "less friction can raise wear" is too compressed. A student may not see why less friction would ever be harmful.
- ch 7 [low] Section 2, Otto formula: The formula is placed right after Miller/Atkinson, so a student may apply it directly to those cycles. Miller/Atkinson efficiency depends on the effective compression ratio, not the geometric one, and the heat-release is not constant volume.
- ch 7 [low] Section 3, last line: The cross-reference to 5.8 is plain text, so it is not a clickable chapter link like the other cross-references in the book.
- ch 7 [low] Worked example 1, steps 4 and 5; Quiz Q7: Thousands are separated by a space ("26 880 g/h", "22 500 g/h"). Most Indian textbooks use a comma, sometimes the Indian grouping.
- ch 8 [high] Section 3 (bulletin 'TDC reference and pegging', last line) and Exam traps (trap 1): It says a wrong peg leaves 'every imep ... wrong by a constant' and that 'a missing peg moves both peak pressure and imep'. A constant pressure offset cancels in the closed-cycle integral ∮p dV, because the cycle starts and ends at the same volume, so imep is almost unaffected by a pegging error. What a wrong peg really corrupts is the absolute level: peak pressure, the pressure trace in bar, polytropic index and the heat-release rate curve. Only the angle error (TDC offset), not the pressure offset, distorts imep, and only slightly.
- ch 8 [low] Section 3, pegging bullet: Written as 'pVn = constant'; the exponent is not a superscript. Quiz Q2 writes 'pV^n', so the notation is inconsistent, and a student may read pVn as p × V × n.
- ch 8 [low] Section 3, first paragraph: 'Cylinder pressure swings from about 1 bar to 80 bar' is only true for spark-ignition engines. A turbocharged diesel peaks near 150–180 bar, which this chapter also covers (imep, pegging and heat release are shown for diesels too).
- ch 8 [low] Section 2, MIDC bullet: 'It is the cycle behind the BS VI limits' is too broad. BS VI type approval for cars and light-duty vehicles uses MIDC, but BS VI for two-wheelers uses the WMTC.
