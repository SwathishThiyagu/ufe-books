# me-thermo-u1: free-model run

- Book: `books/mech/me-thermo/me-thermo-u1.html`
- Status: ok
- Model calls so far: 18 (60,196 tokens in, 124,034 out), 3.5 minutes

## Checker

```
me-thermo-u1.html: 7 chapters, 12946 words, 8 figures, 134 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Lead and Section 1: The definition of thermodynamics appears twice in almost the same words (lead: 'studies energy, matter and their changes'; Section 1: 'the study of energy, matter and the changes they undergo'). A student on a phone reads the opening twice and gains nothing the second time.
- ch 1 [low] Section 2: 'About 10¹⁹ molecules' per cubic centimetre is loose. At room conditions the count is nearer 2.5×10¹⁹ per cm³, so a student who meets the Loschmidt number later may think the notes were wrong by a factor of two or three.
- ch 1 [low] Exam trap 4: 'The two views do not give different thermodynamics' is vague. A student may not see whether this means different laws, different results or different properties.
- ch 1 [low] Quiz Q7: The phrase 'microscopic-type molecular quantity' is a new, undefined label. The chapter never defines 'microscopic-type', so the student cannot tell whether this is a formal classification or a description.
- ch 2 [low] Worked example 1, step 4 and answer: The example treats heat as the only energy transfer. The 0.50 kg of air that escapes also carries energy (internal energy plus flow energy) out of the tank. A student can read step 4 as 'in an open system energy crosses only as heat', which is wrong. The same gap appears in the Q4 and Q8 answers, where entering or leaving mass carries energy but only Q is mentioned.
- ch 2 [low] Worked example 1, step 1 vs step 5: Step 1 names the system as 'the air inside the tank', which reads like a fixed amount of matter (a control mass), yet step 5 correctly calls it an open system. The wording is loose where the chapter is teaching exactly this distinction.
- ch 2 [low] Section 3, table, Rigid row: The column asks 'Work may cross' and the cell answers 'No p dV'. The header and cell do not match, so the reader cannot tell whether the answer is yes or no.
- ch 2 [low] Quiz Q6, answer: Pushing a thermometer through the wall makes a hole, so mass can cross too; the system is then open, not 'at best closed'. The answer also implies the flask was isolated before the hole, though a metal wall already passes heat.
- ch 2 [low] Figure caption, Section 3: The caption says 'the three lower blocks classify it' but the diagram has six blocks below the top one (three classification blocks and three note blocks), so the description does not match the figure.
- ch 3 [low] Section 2, first paragraph, and Exam traps (last bullet): Section 2 says a single process whose start and end states are the same 'is cyclic, or a cycle', while the last exam trap tells the student that treating a process and a cycle as the same thing is an error. A student meets a direct internal clash.
- ch 3 [low] Section 3 and the figure: The text says 'For the cycle in the figure' and then gives p and V values, but the figure is a state graph with numbered nodes and arrows, not a p–V plot. A student may try to read areas or slopes off it.
- ch 4 [high] Section 1, mechanical equilibrium: The piston balance is stated as gas pressure = piston weight ÷ area. This omits the atmosphere pressing on the outside of the piston, so a student who uses this formula will get the wrong gas pressure for every usual cylinder problem.
- ch 4 [high] Section 3, formula block: The formula pV = C is placed immediately after the definition of a quasi-static process, which makes it look like a property that every quasi-static process obeys. It is not. pV = constant is one particular path (an isothermal path for an ideal gas, or simply the path assumed in the worked example). A general quasi-static path has no such relation.
- ch 4 [high] Section 3 versus Exam traps, item 3: Section 3 says a fast expansion is 'not at a state at all', while the trap says a fast process 'still passes through states, just not equilibrium states'. The two statements contradict each other and a student will not know which to write in the exam.
- ch 4 [low] Section 3, bullet list, first bullet: The symbol dp is used without definition, and 'remove the imbalance' is misleading: adding a grain of sand or lowering the outside pressure creates a small imbalance to drive the change, it does not remove one.
- ch 4 [low] Section 3, bullet list: The two examples move the system in opposite directions: adding sand to the piston compresses the gas, while lowering the outside pressure expands it. Placed side by side without comment, this reads as if both do the same thing.
- ch 4 [low] Section 3, closing paragraph: The chapter never says that a truly quasi-static process takes infinite time, so students may conclude that any 'slow enough' real process is exactly quasi-static instead of only an approximation to it.
- ch 5 [low] Lead: "Temperature is the property that two bodies share when no heat flows between them" is loose: two bodies separated by an adiabatic wall also have no heat flow between them, yet their temperatures can differ. A student can read this as saying any two bodies with no heat exchange are at the same temperature.
- ch 5 [low] Section 3, third bullet: "If θ_A = θ_B, the zeroth law says A and B are in thermal equilibrium" — at that moment A and B are separate and not in contact. The law guarantees that they would be in thermal equilibrium once connected; the sentence as written can confuse a student about what equilibrium means.
- ch 5 [low] Section 2, last paragraph: The forward reference "Unit 3, Thermodynamic temperature scale" is plain text, not a chapter link, so on a phone the reader cannot jump to it and may not know which chapter is meant.
- ch 6 [low] Section 1: The chapter writes 'Small amounts are written δQ and δW' but never says what δ means. A student can easily read δQ as 'a small change of a property Q' and later write ΔQ, which contradicts the point that Q and W are path functions.
- ch 6 [low] Section 4: The example 'heat it slowly at constant pressure, or heat it quickly and let the pressure change; the end states can match' is loose. A constant-pressure path fixes the final pressure, so the quick path must also return to that same pressure; as written a student may think the two final states differ in pressure.
- ch 6 [low] Section 3: 'A movable boundary lets displacement work cross' uses the term displacement work without defining it, so the label is not usable on its own.
- ch 7 [low] figure (plot spec): The caption and aria text describe a constant-pressure path that ends at 0.25 m³, but the plotted series runs from 0.10 m³ to 0.30 m³, so the drawn line is longer than the process the chapter is about. A student reading the area from the graph would get 200 × 0.20 = 40 kJ, not the stated 30 kJ.
- ch 7 [low] quiz Q8: The symbol V is used for the potential difference of the capacitor, but everywhere else in the chapter V is volume and φ is potential difference. A student can read 'charged from 0 to V' as a volume.
