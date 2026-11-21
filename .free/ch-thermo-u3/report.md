# ch-thermo-u3: free-model run

- Book: `books/chem/ch-thermo/ch-thermo-u3.html`
- Status: ok
- Model calls so far: 33 (124,940 tokens in, 236,126 out), 5.0 minutes

## Checker

```
ch-thermo-u3.html: 10 chapters, 18067 words, 11 figures, 188 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 2: The sentence “Therefore W H and η < 1” is missing the inequality and subscript. As written it is meaningless and does not show that QC > 0 forces W < QH and hence η < 1.
- ch 1 [high] Quiz Q7: The answer is garbled: “so W H and η C/Win” has missing inequality signs and symbols, so it does not correctly explain why η < 1 while COP can exceed 1.
- ch 2 [high] Section 1, last sentence of the heat-engine paragraph: The sentence ends with the broken text 'so W H', which states nothing. A student cannot tell whether the intended relation is W < QH, W > QH or something else, so the key consequence of the second law is lost.
- ch 2 [high] Section 2, sentence after the efficiency derivation: The sentence reads 'so η 3.8', which is not a relation and contains a stray number. The meaning (efficiency is always below 1) is missing, and '3.8' could be misread as a value of efficiency.
- ch 2 [low] Section 2 and Section 3 formulas: Heat symbols are written two ways: QH in running text and Q<sub>H</sub> inside the formulas. Mixed subscripting looks like different quantities (QH versus QH with a subscript).
- ch 3 [low] Section 1 (four Carnot steps): The equality (V₂/V₁) = (V₃/V₄) is simply asserted. A student cannot see where it comes from, and it is the one step that makes Q_H/Q_C = T_H/T_C work.
- ch 3 [low] Section 2 (thermodynamic temperature scale): The text says the kelvin is fixed by one reference point, the triple point of water at 273.16 K. Since the 2019 SI redefinition the kelvin is fixed by the Boltzmann constant, and the triple point of water is a measured value (273.16 K, no longer exact by definition). A student may repeat an outdated statement in an exam.
- ch 3 [low] Section 1, opening line: The cycle is introduced with 'one mole of ideal gas', but every formula then uses n, and the text later says the ratio does not depend on n. The switch is small but can confuse.
- ch 4 [high] Quiz Q7: The reasoning step is wrong. For an isolated system Q = 0, so the cyclic integral ∮δQ/T is just 0, and 0 ≤ 0 tells you nothing; the inequality does not 'become' ΔS_isolated ≥ 0 through the cyclic integral. The answer also leaves the reader thinking ∮δQ/T is the same object as ΔS, which is exactly the confusion the chapter warns against in the exam traps.
- ch 4 [low] Section 2, second ideal-gas formula: 'The minus sign appears because pressure and volume move in opposite directions' is vague and does not explain the sign; a student can read it as 'two negatives make a plus' and then get the compression case wrong.
- ch 4 [low] Section 3: The process (non-cyclic) form of the Clausius inequality, ΔS_system ≥ ∫₁² δQ/T with T the boundary temperature, is never written down explicitly; only the cyclic form ∮δQ/T ≤ 0 and the constant-T₀ version ΔS_system − Q/T₀ ≥ 0 appear, and some syllabi examine the integral form directly.
- ch 5 [high] Section 2, heat exchanger paragraph: The sign given for heat leaked to the room is wrong. The steady balance gives S_gen = (entropy out with streams) − (entropy in with streams) − Σ Q_j/T_j. A room loss has Q_room negative, so the term actually added to S_gen is −Q_room/T_room, a positive number. Telling students to 'add Q_room/T_room with Q_room negative if it leaves' makes them subtract entropy and under-count S_gen, which can even hide a second-law violation.
- ch 5 [low] Section 1, definition of T_j: The formula Σ Q_j/T_j assumes each boundary j is at one uniform absolute temperature. Real boundaries (a boiler wall, a duct surface) often vary in temperature, and dividing total Q by one T gives the wrong entropy flow.
- ch 5 [low] Worked example 1: The state is named precisely (2 MPa, 400 °C) but the entropy quoted, 7.0 kJ/(kg·K), is not the steam-table value for that state (about 7.13 kJ/(kg·K)). A student who checks tables will think the data are wrong.
- ch 5 [low] Beyond: Pinch analysis for heat-exchanger networks is mainly an energy-targeting method (composite curves, minimum utility). Saying it 'uses the same flow-entropy bookkeeping' overstates the link; only exergy-based variants bring entropy in.
- ch 6 [low] Section 2 (integral and the C_p = aT³ step): The definite integral ∫₀ᵀ (C_p/T) dT uses T both as the upper limit and as the integration variable, so the symbol clashes inside the same expression; students copying it cannot tell which T is which.
- ch 6 [low] Section 2 (low-temperature law): The T³ law is strictly the Debye result for C_v, not C_p. The text writes C_p = aT³ without saying why C_p may be used in its place.
- ch 6 [low] Section 2 (metals): Saying only that 'metals add an electronic term' leaves the student unable to write the entropy of a metal; the extra term in C_p is γT, so it changes the integrated result, not just the heat capacity.
- ch 6 [low] Section 3 (residual entropy of CO): 'roughly R ln 2 per mole' is left symbolic although R was never given a value in the chapter, so the student cannot check the size of the residual entropy.
- ch 6 [low] Figure caption and spec: The y-axis label reads 'S (J/mol K)', which does not match the unit form J mol⁻¹ K⁻¹ used everywhere else in the chapter.
- ch 7 [high] Lead: The lead says the best work a steady-flow process can give is W_ideal = ΔH − T₀ΔS. Section 1 uses the work-input-positive convention, so for a work-producing unit ΔH − T₀ΔS is negative. The work the unit can give is −W_ideal, not W_ideal. A student reading only the lead gets the sign backwards.
- ch 7 [low] Section 1: "A process that exchanges heat only with this reservoir has no finite temperature difference, so it can be reversible" is loose. Exchanging heat with the environment does not by itself remove the temperature difference; the boundary must also be at T₀. As written it suggests any process that dumps heat to ambient is reversible.
- ch 7 [low] Section 2: "S_gen includes the system and its surroundings" does not tell the student that entropy generation is the sum of the two entropy changes. The worked example uses the sum, but the definition is never written.
- ch 7 [low] Quiz Q5: Q5's answer uses W_lost = W_ideal − W_actual with output magnitudes, which is the opposite arrangement to the input-positive rule W_lost = W_actual − W_ideal given in Section 2 and the exam traps. A student may take the two as contradictory.
- ch 8 [high] Quiz Q4 answer: The reasoning is thermodynamically wrong. It says that at a lower rejection temperature 'less entropy is carried away per unit of heat'. Entropy carried away per unit heat is Q/T, so a lower T means MORE entropy per unit heat, not less. The heat rejected also is not 'the same' — it falls. A student who memorises this sentence will get the second law backwards in the exam.
- ch 8 [low] Section 1, energy balance paragraph: The steady-flow balance q − w = Δh is written, then pump work is given as w_p = h₂ − h₁. For the pump (q = 0) this balance gives w = −(h₂ − h₁), so w_p as written is the work input magnitude, not w of the sign convention. A careful student may think the two statements contradict each other.
- ch 9 [high] Exam traps, first trap: The numbers in the Celsius trap are wrong twice over. Putting 250 °C and 300 °C straight into T_C/(T_H − T_C) gives 250/50 = 5, not 5.26, and the correct Carnot COP for those two Celsius temperatures is 523/50 ≈ 10.5, not 5. So the trap as written teaches a false arithmetic and a false reference answer.
- ch 9 [high] Quiz Q5 answer: The last sentence contradicts itself. If the vapour leaving the evaporator is superheated, the tail of the evaporator holds superheated vapour, not boiling liquid, so the whole surface cannot stay wet with boiling liquid (that is the flooded-evaporator case, which gives saturated, not superheated, vapour). A student will take away the opposite of the truth.
- ch 9 [low] Lead: "The same machine, run the other way round, is a heat pump" suggests reversing the machine. A heat pump is the same cycle with the same direction of flow; what changes is the useful output (Q_out instead of Q_in). Students may confuse this with a heat engine run in reverse.
- ch 10 [low] Section 1, two-box example: The example calls 'one particle on each side' a macrostate, but the chapter has just defined a macrostate as what is measured on the bench, i.e. U, V, N (and P, T). Under that definition all four arrangements belong to the same macrostate, so calling the one-on-each-side case a macrostate with Ω = 2 contradicts the definition and can confuse a student about what Ω is counting.
- ch 10 [low] Section 1, two-box example: The phrase 'the macrostate "any arrangement" has Ω = 4' is not a meaningful macrostate label; a macrostate is a set of macroscopic values, not a statement that anything goes.
- ch 10 [low] Exam traps, third bullet: The wording muddles two different formulas. 'Using R instead of kB gives molar entropy' is only correct when Ω is the number of microstates of one mole; as written a student may conclude S = R ln Ω and S = kB ln Ω are interchangeable for any Ω.
