# ch-thermo-u1: free-model run

- Book: `work/ch-thermo-u1/tree/books/chem/ch-thermo/ch-thermo-u1.html`
- Status: ok
- Model calls so far: 23 (85,115 tokens in, 188,150 out), 5.5 minutes

## Checker

```
ch-thermo-u1.html: 8 chapters, 24704 words, 10 figures, 222 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Exam traps, trap 2: The trap states flatly that joining vessels at 300 K and 400 K 'does not give 350 K'. That contradicts the Q6 answer, which correctly says 350 K is exactly what you get when the two masses of the same gas are equal and heat capacities are constant. A student meets two opposite statements in the same chapter.
- ch 1 [low] Worked example 1, steps 3-5 and dry run: The data are given to two significant figures (2.0 kg, 1.2 m³), but the answers are quoted as 1.667 kg/m³ and 0.6 m³/kg. The digits do not match the precision of the inputs, and 0.6 should be written 0.60.
- ch 1 [low] Chapter title and Section 3: The title promises 'variables', but the chapter never says that a property is also called a state variable. The word appears once ('classify the simple variables') without a definition, so a student may think variables and properties are different things.
- ch 2 [low] Section 1, exact differential formula: 'the test is done at constant other variable' is vague: a student may not see which variable is held fixed, and the phrase adds nothing because a partial derivative is already defined at constant other variable.
- ch 2 [low] worked example 1 and figure: The work is taken as the area under each P–V path without saying the paths are quasi-static. Area under the curve equals work only when the gas pressure is defined at every step and equals the plotted pressure. Exam trap 4 correctly warns that ∫P dV fails for an irreversible sudden expansion, so the example as written can look inconsistent with the trap.
- ch 2 [low] quiz Q4 (and the chapter body): The first-law sign convention is never stated in the text, yet the Q4 answer uses ΔU = Q − W with W taken as work done by the system. A student using the opposite convention (work done on the system) gets Q_B − Q_A = −3 J.
- ch 2 [low] lead: 'the first law ties the difference to the path' is ambiguous. The first law makes Q − W = ΔU the same for all paths, so the difference between Q and W does not depend on the path; only Q and W separately do.
- ch 2 [low] cross-references ('see 1.3', 'Unit 3', 'Unit 4'): Cross-chapter references are plain text, against the house style that links to other chapters use the anchor tag.
- ch 3 [low] Section 1 and Section 2 (symbols): The letter V carries three different meanings: speed in E = U + ½mV², volume in W = ∫P dV and P(V₂ − V₁), and voltage in the electrical power VI. A second-language reader on a phone can easily carry the wrong meaning across.
- ch 3 [low] Section 2, boundary work: W = ∫P dV is written as if it always holds. It holds only for a slow (quasi-equilibrium) expansion, where the gas pressure equals the external pressure. For a fast expansion the work is ∫P_ext dV.
- ch 3 [low] Section 2, units example: A pump does not deliver shaft work; it consumes it. The motor supplies the shaft work to the pump shaft.
- ch 3 [low] Section 3, Q = mCΔT and the rate formulas: The symbol C is used for specific heat, but the usual convention is lowercase c for specific heat in J/(kg·K) and uppercase C for heat capacity in J/K. The chapter's own pattern (E total, e = E/m specific) is broken here. Also ΔT in the conduction formula is not defined in sign.
- ch 3 [low] Quiz Q3 answer: 'Rigid means no boundary work and no ΔKE or ΔPE' is not right: rigidity only rules out boundary work. ΔKE and ΔPE are zero because the tank itself does not move or change height.
- ch 3 [low] Quiz Q4 answer: The question asks for a closed-system situation, but 'water flowing down a pipe between two levels' is a flow process through an open system, so it does not fit the closed-system first law ΔE = Q − W that the answer quotes.
- ch 3 [low] Quiz Q1: 'Kinetic energy is stored' can confuse a reader, because the kinetic energy of molecules is already part of internal energy U.
- ch 4 [low] Section 3, reading a thermometer: "Tap the bulb" is bad practice: tapping a glass thermometer can break the mercury/alcohol column or give a false reading, and it is not what settling at equilibrium requires.
- ch 4 [low] Section 1, bullet list: An adiabatic wall alone does not define an isolated system; an isolated system also exchanges no work and no mass with the surroundings. A wall that only blocks heat gives a thermally insulated system.
- ch 5 [high] Quiz Q6 (and its answer): The premise cannot happen as described, so the quiz answer is wrong. If a student writes ΔU = Q + W with W = +mgh (work done on the system), the result is ΔU = 0 + mgh = +mgh, which is exactly the correct answer, not twice it. Nothing in that route counts mgh twice, so the stated 'twice the correct value' and the explanation 'the sign is counted twice' are both unfounded. A student who reads this learns a wrong lesson about what the sign convention does.
- ch 5 [low] Section 2, formula ΔT = m g h / (m_w c): As printed the formula is dimensionally inconsistent: mgh comes out in joules while c is in kJ/(kg·K), so the numerical result is 1000 times too large unless the reader remembers the sentence below it. Students copy formulas off the page and skip the note.
- ch 6 [low] Lead paragraph: The lead says 'energy in equals energy out plus shaft work', which leaves out heat crossing the boundary and hides the case where shaft work enters (a compressor). A student can read it as Q = W_s, the very mistake the chapter later warns against.
- ch 6 [low] Section 2: 'The two push works combine with u into enthalpy' suggests the inlet and outlet Pv are netted first and then added to u. In fact each stream forms its own enthalpy from its own pressure and specific volume.
- ch 6 [low] Section 3: 'Q − W_s equals the net energy carried by the flow' is vague. The right side is the energy carried out by the flow minus the energy carried in.
- ch 6 [low] Quiz Q5: P1v1 = 1000 kJ/kg is not a realistic flow-work value for steam; for steam it is typically a few tens to a few hundred kJ/kg even at high pressure. The arithmetic of the answer is correct, but the numbers mislead a student about the size of Pv.
- ch 7 [low] Section 3: The sentence says Joule's experiment showed that 'a gas' expanding into vacuum shows no temperature change. For a real gas there is a small temperature change; the exact zero result holds only for an ideal gas, and the text's own next sentence then switches to the ideal-gas conclusion, so the first sentence overstates the result.
- ch 7 [low] Section 3, table: The diatomic value is printed as Cp = 3.5R = 29.11, but 3.5 × 8.314 = 29.099 J/(mol·K), which rounds to 29.10, not 29.11.
- ch 7 [low] Section 3, table header: The Cv and Cp columns show bare numbers (12.47, 20.79, 29.10, 1.67) with no unit, so a student cannot tell J/(mol·K) from J/(kg·K).
- ch 7 [low] Section 1: The same symbol u is defined twice: u = U/n in J/mol (molar) and u = U/m in J/kg (specific). Section 2 then uses u in J/(mol·K) for Cv, so the reader cannot tell which u is meant.
- ch 7 [low] Quiz Q6: 'A few J/(mol·K)' overstates the gap for liquid water: cp − cv for water near room temperature is under 1 J/(mol·K) (cp ≈ 75.3 J/(mol·K)).
- ch 7 [low] Section 1 and Section 2 cross-references: Cross-references appear as plain text, '(1.2)', '(1.1)', '(1.6)', '(1.5)', 'chapter 1.8', rather than as chapter links, so the phone reader cannot tap through.
- ch 8 [high] Section 1, third summary bullet: The sign is wrong under the chapter's own convention. The main equation is h₁ + v₁²/2 + gz₁ + q = h₂ + v₂²/2 + gz₂ + w_s, where w_s is defined as shaft work done <i>by</i> the fluid. Setting q = 0 and dropping kinetic and potential terms gives h₁ = h₂ + w_s, so w_s = h₁ − h₂. The book prints w_s = h₂ − h₁, which is the sign of the work done <i>on</i> the fluid and contradicts the definition just above it.
- ch 8 [high] Section 3, first paragraph after the P formula: "For compression h₂ is larger than h₁, so w_s is positive: work is done on the fluid." With w_s defined as work done by the fluid, h₂ > h₁ makes w_s negative, not positive. A student who follows this sentence will write the wrong sign in the energy equation, and it directly contradicts the Section 1 bullet that says w_s = h₂ − h₁.
- ch 8 [high] Section 3 formula and quiz Q3: The units do not match the working. Section 3 says h₁ and h₂ are in J/kg and P comes out in W, to be divided by 1000 for kW. Quiz Q3 then puts kJ/kg values (350 − 290 = 60) straight into P = ṁ(h₂ − h₁) and calls 0.5 × 60 = 30 kW, with no conversion. Taken with J/kg as stated, the same numbers give 30 W. In a chapter whose lead warns about exactly this unit slip, the two procedures must agree.
- ch 8 [high] Exam trap 3: "For compression h₂ > h₁, so the work term is positive work done on the fluid" repeats the sign muddle of Section 3 while the trap is about the sign. Written as it stands, the trap teaches the wrong rule.
- ch 8 [low] Quiz Q5 answer: The conclusion (lower exit velocity) is right, but the reason is self-contradictory: "less energy is available for kinetic energy at the same exit enthalpy" followed by "The exit enthalpy is also slightly lower". The exit enthalpy is not the same in the two cases, and the phrase will confuse a student trying to set up the comparison.
- ch 8 [low] Section 2, first sentence: "A nozzle is a duct whose cross-section narrows, so the fluid speeds up" is only the subsonic picture. Section 4 and quiz Q6 both deal with gas velocities of 400 m/s and the throat, where the accelerating part of the nozzle widens. A student can read the two sections as contradicting each other.
- ch 8 [low] Section 4, third paragraph: "Compressible flow becomes hard when velocity approaches the speed of sound; the flow behaviour there needs the second law" is too vague to teach anything. Choking follows from mass, energy and the sonic condition; the second law is what rules out processes and fixes the isentropic limit.
