# bm-instr-u4: free-model run

- Book: `books/bme/bm-instr/bm-instr-u4.html`
- Status: ok
- Model calls so far: 22 (79,936 tokens in, 190,128 out), 5.8 minutes

## Checker

```
bm-instr-u4.html: 7 chapters, 12802 words, 8 figures, 144 KB
OK
```

## For the reviewer

- chapter 2: the figure cannot be drawn: tree is too wide (6 leaves); use fewer leaves or shorter labels

## Reviewer notes (after any revision)

- ch 1 [low] Section 1, paragraph 2: The pronoun 'It' in 'It measures H⁺' can be read as referring to the ion-selective electrode, but an ion-selective electrode measures the ion its membrane is selective for, not necessarily H⁺.
- ch 1 [low] Section 1, paragraph 1: The claim that the transducer output is 'proportional to analyte concentration' is not true for potentiometric sensors, where voltage varies with the logarithm of ion activity; the chapter itself uses mV per decade in the exam traps.
- ch 1 [low] Section 3 and Exam traps: Sensitivity is defined as signal per unit concentration, but the exam traps give mV per decade for potentiometric sensors; the general definition and the stated units do not match.
- ch 2 [low] Figure, enzyme branch, node 'Km sets range': The note under 'Enzyme — glucose oxidase' reads '5.0 mmol/L'. That is the made-up Km of the worked example, not a literature value; real glucose oxidase has Km for glucose in the region of 20–40 mmol/L, which is above the blood glucose range. A student may memorise 5.0 mmol/L as the enzyme's true Km.
- ch 2 [low] Section 1, first line: 'An enzyme is a protein catalyst' is too narrow: some enzymes are RNA (ribozymes).
- ch 2 [low] Section 1, last paragraph: The paragraph implies an enzyme electrode oxidises the reaction product to pull an unfavourable equilibrium forward. On a glucose electrode the species oxidised at the electrode is hydrogen peroxide, and the reason is to generate a current signal; the glucose oxidase reaction itself is effectively irreversible, so no equilibrium needs pulling.
- ch 2 [low] Section 2, third paragraph, last sentence: 'Cells and chemoreception serve as recognition layers in whole-cell sensors' is unclear — chemoreception is a biological process, not a layer that can be fixed on a transducer.
- ch 3 [high] Section 2 (mediators paragraph): The text says running the electrode at +0.2 to +0.4 V is 'below the oxidation potentials of ascorbic acid and uric acid'. Ascorbic acid on a carbon electrode oxidises at roughly +0.2 to +0.4 V vs Ag/AgCl (and uric acid near +0.3 to +0.4 V), so +0.3 V is not below them. The claim overstates what a mediator does, and it contradicts the same sentence's own 'less false current'.
- ch 3 [low] Worked example 1, step 7: The reason given is wrong as stated: 1.93 V is about two-thirds of a 3 V rail, not 'too close' to it, and a normal op-amp swings well above 1.93 V on a 3 V supply. The real reason for a lower Rf is headroom for the largest expected signal.
- ch 3 [low] Section 3 (transimpedance amplifier): 'A microamp becomes a readable volt with Rf in the 100 kΩ to 1 MΩ range' is loose: 1 µA through 100 kΩ gives 0.1 V, not about a volt, and the inverting sign is not mentioned.
- ch 3 [low] Section 1 (Nernst formula note): The note calls a 'the activity of the ion' without saying activity is a dimensionless ratio, which can confuse students about units inside the log.
- ch 4 [high] figure spec, stack item 5: The note 'with reference electrode' is attached to the p-silicon substrate. The text and the figure caption both put the reference electrode in the sample electrolyte above the gate. A student reading the stack will think the Ag/AgCl electrode sits inside the silicon.
- ch 4 [low] figure spec, stack item 3: The layer is labelled 'Gate oxide (Ta₂O₅)'. Section 1 correctly describes the stack as a thin SiO₂ gate oxide plus a deposited Si₃N₄ or Ta₂O₅ sensing layer. Ta₂O₅ is not the gate oxide; it is the top sensing dielectric that carries the SiOH/TaOH sites.
- ch 4 [low] worked example 1, step 1: ΔpH is written as 7.4 − 7.1 = 0.3, i.e. initial minus final. By convention Δ means final minus initial, so ΔpH should be −0.3 here; the sign of ΔV_G then contradicts step 2 unless the reader guesses the convention.
- ch 4 [low] section 4, practical limits: 'The gate window is the only exposed silicon area' is wrong. Silicon is never exposed; the window opens onto the gate insulator (oxide or nitride), which contacts the sample.
- ch 4 [low] section 1, charge-to-current path: 'That potential is in series with the gate capacitance' is loose. The surface potential adds in series with the applied gate voltage; the double-layer capacitance at the electrolyte interface sits in series with the gate capacitance and forms a voltage divider with it.
- ch 4 [low] section 4, fabrication steps: The step list grows SiO₂ and then jumps to lithography, but the sensing nitride or Ta₂O₅ layer named in section 1 is never deposited. A student following the steps cannot build the stack the chapter describes.
- ch 4 [low] worked example 1, step 5: The estimate 'one electronic charge gives a sub-millivolt surface-potential change' is quoted without its dependence on gate capacitance, and the exponent is printed as '10−19', which reads as a subtraction.
- ch 5 [high] Worked example 1, part (d) and its answer: Part (d) is self-contradictory and its answer is arithmetically wrong. A meter that expects mmol/L accepts 11.8 mmol/L correctly, so 'entering 11.8 as 11.8 mg/dL into a mmol/L meter' describes no error at all. The claim that 'the dose would be wrong by about 18 times' is also false: the correction dose depends on (glucose − target), not on glucose alone, so a unit mix-up does not scale the dose by 18. Entering 11.8 as mg/dL against a 120 mg/dL target gives (11.8 − 120) ÷ 50, a negative number, i.e. no correction at all when 1.84 units are needed. A student cannot reproduce the stated conclusion.
- ch 5 [low] Section 1, paragraph 3: Sentence reads 'Early strips let oxygen accept the electrons and measured hydrogen peroxide or oxygen use', which is grammatically broken and unclear to a second-language reader.
- ch 5 [low] Section 2, paragraph 3: The reason given for the plasma–whole-blood difference, 'red cells displace plasma water and hold little glucose', can mislead: glucose does enter red cells, and the main reason whole-blood glucose is lower is the smaller water fraction per unit volume of red cells.
- ch 5 [low] Quiz Q8: The question asks for two diagnostic cut-offs but the answer lists three, so a student cannot tell which two are expected.
- ch 6 [low] Section 1, last sentence: The sentence says a block of ten thymines 'spaces chemically instead', which reads as if the T10 block replaces the MCH backfill. In standard practice the T10 is a linker placed between the thiol anchor and the probe sequence; it holds the probe away from the gold, but MCH backfilling is still done to block bare metal.
- ch 6 [low] Section 3, labelled routes bullet: 'A ferrocene-tagged target carries its own electroactive group only when it hybridises' is inaccurate: the ferrocene is covalently attached to the target whether or not it binds. Only its access to the electrode depends on hybridisation.
- ch 6 [low] Worked example 1, step 6 (and Section 2 wash rule): Step 6 says the mismatched duplex 'sits at its melting point and is removed', but the chapter defines Tm as the point where only half the duplex has separated. At a 55 °C wash, with mismatch Tm 55 °C, about half the mismatch is still paired at equilibrium. A student can read this as full melting at Tm.
- ch 6 [low] Quiz Q6: 'a small current with the one-mismatch probe' swaps the terms: the probe is the fixed strand on the electrode, the mismatched species is the target. This contradicts the exam trap that warns against swapping probe and target.
- ch 6 [low] Figure: The figure states 'hybridise at 55 °C' as a general step. That number comes from the worked example's 60 °C Tm probe; hybridisation temperature depends on the probe's Tm and buffer, so a fixed 55 °C reads as a rule.
- ch 6 [low] Worked example 1, step 7: Step 7 claims the 50% G+C content is 'why the probe is neither too sticky nor too weak for a 55 °C assay'. This is loose: the 55 °C choice follows from the Tm value; the G+C content only sets that Tm.
- ch 7 [low] Section 1, formula block: The Förster equation and the symbol R0 appear before FRET is ever introduced, and the abbreviation FRET is never spelt out. A student meets 'E', 'donor energy transferred' and 'Förster radius' with no statement of what the technique is. The transition into the next paragraph ('As a FRET donor...') is also abrupt.
- ch 7 [low] Section 1, formula symbol list: R0 is said to be 'usually 2–6 nm for such pairs'. For a quantum-dot donor with a dye acceptor, R0 is typically larger, about 4–7 nm, because the dot has a high extinction coefficient and a large size; 2–6 nm is the usual range for dye–dye pairs.
- ch 7 [low] Worked example 1 (steps 1–3) and Quiz Q4: The sixth-power exponents are typed as plain digits: '(r / R0)6', '0.806', '1.606', and in Q4 '0.56 = 1/64'. These read as multiplication by 6 or as the decimal 0.56, not as a power.
- ch 7 [low] Lead paragraph: 'This makes nanomaterial biosensors sensitive without complex optics' is too broad. Only the gold-nanoparticle colour and lateral-flow readout are optics-free; quantum-dot assays still need an excitation source and a fluorescence detector.
- ch 7 [low] Section 1 and Quiz Q1: The 2–10 nm figure is quoted for the quantum dot, but the example given is a CdSe core with a ZnS shell. The core is 2–10 nm; the capped dot is larger by roughly 1–2 nm of shell, so 'a CdSe core 2–10 nm across' and 'a dot 2–10 nm across' are not the same object.
