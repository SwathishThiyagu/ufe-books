# ee-pe-u5: free-model run

- Book: `work/ee-pe-u5/tree/books/eee/ee-pe/ee-pe-u5.html`
- Status: ok
- Model calls so far: 20 (73,829 tokens in, 242,165 out), 8.9 minutes

## Checker

```
ee-pe-u5.html: 6 chapters, 20291 words, 9 figures, 253 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 3, RL load paragraph: The reason given for gate-pulse failure at α < φ is wrong. The current expression does not 'begin negative': at θ = α it is exactly zero and its slope there is (Vm/Z)·sin α/sin φ, which is positive for 0 < α < π. The real cause is that when α < φ the current of the conducting SCR does not reach zero before the next SCR is gated (β > α + π), so at the moment the narrow pulse arrives the incoming SCR is not forward biased and the pulse is wasted; the output then goes discontinuous and asymmetric.
- ch 1 [high] Quiz Q6: The answer repeats the same wrong physics: 'the current expression would start negative'. At θ = α the current is zero and rises; it does not start negative.
- ch 1 [low] Section 2, phase control power factor sentence: 'near α = 180° it is very small even though the load still needs current' invites a wrong picture: with a resistive load the current is also small there. The point being made is that the supply voltage stays at full Vs while the load gets almost nothing, so the circuit uses the supply badly.
- ch 1 [low] Section 3 formulas and Worked example step 4: Squares and inverse tangent appear without superscript markup: 'Z = √(R2 + (ωL)2)', 'φ = tan−1(ωL/R)', 'P = Vrms2/R = (2302 × 0.5)/20'. Read literally these are wrong symbols (R2, 2302, tan−1 as reciprocal of tan).
- ch 2 [low] Figure (TRIAC triggering quadrants spec table): The rendered table gives Q2 as 'med' and Q4 as 'low', but the text and the table in Section 2 say Q2 is 'low' and Q4 is the 'lowest' of all. A student reading only the figure gets a different picture of the gate-current requirement.
- ch 2 [low] Worked example 1, step 6 (and Quiz Q5): 'half of the 100 W rating, so the lamp runs at half brightness' is loose. The calculation holds only because the 529 Ω is the hot, rated resistance held constant; a real filament is cooler at reduced power, so its resistance is lower and the actual power is somewhat more than 49.98 W. Also, visible light falls by more than half when the power is halved.
- ch 2 [low] Exam traps, last bullet: 'the controlled-rectifier formula V_rms = V_s cos α' names a formula that is not a standard controlled-rectifier result, so the trap teaches a wrong fact about rectifiers while making a correct point about the dimmer.
- ch 2 [low] Worked example 1, step 4, and Quiz Q5 formula: 'sin2α/2' can be read as sin(2α)/2 or as sin(2α/2); on a phone screen the ambiguity slows the reader down.
- ch 3 [high] Section 2, last paragraph (delta landmarks): The chapter says the 60° and 150° landmarks appear in the delta branch quantities. With one thyristor pair in series with each delta branch, each branch is just a single-phase controller fed by the line-to-line voltage. Its conduction is continuous only up to α = 90°, and its RMS branch voltage reaches zero at α = 180°, not 150°.
- ch 3 [high] Section 3, Uses paragraph: It says a soft starter "raises the firing angle slowly so the motor voltage rises". Raising α lowers the output voltage, so this reverses the action of a soft starter.
- ch 3 [high] Quiz Q6 answer: The answer says the currents contain "triplen components that cannot return in the neutral". In a three-wire star the three load currents sum to zero at every instant, so the zero-sequence (triplen) current component is identically zero and cannot appear in the currents at all. This also contradicts Section 3, which says triplens need a neutral or delta path.
- ch 3 [low] Section 2, formula lead-in: The sentence "The supply phase voltage is:" introduces a formula for the output (load) phase voltage V_o,ph, not for the supply voltage.
- ch 3 [low] Lead paragraph: "Changing the firing angle of one phase therefore changes the voltages of the other two" is true only for the three-wire star. In a delta with an ideal source the branch voltages are the supply line voltages and do not shift when another branch's firing angle changes.
- ch 3 [low] Exam traps, third trap: "The zero point is α = 150° because no return path remains for a conducting pair" is vague and can be read as saying the return path disappears only at 150°, when in fact there is never a neutral in this circuit.
- ch 3 [low] Section 3, first paragraph: "Phase control produces odd harmonics: 5th, 7th, 11th and so on" mixes the single-phase picture (all odd orders) with the balanced three-phase picture, and leaves a student wondering where the 3rd went before triplens are discussed.
- ch 4 [low] Lead: It says the load is fed in every switching period 'so the supply current stays close to a sine'. The unfiltered supply current is a pulse train (load current gated on and off), not a sine. Only the input filter makes it sinusoidal; a student can read this as saying no filter is needed for a good current shape.
- ch 4 [low] Section 1 vs Section 3: Section 1 gives the switching frequency range as 5 kHz to 50 kHz, while Section 3 says '5 kHz to 20 kHz covers most line-frequency designs'. Two different upper limits for the same quantity confuse the reader.
- ch 4 [low] Section 3: 'It also pushes ripple above the audible range' is true only above about 20 kHz. The range the chapter itself calls typical (5 kHz to 20 kHz) is inside the audible band, where the switching ripple can be heard as a whine.
- ch 4 [low] Section 3, three-phase paragraph: The reason does not support the conclusion. That the freewheeling current of a three-wire load must return through the other phases means the switching states must be coordinated so a freewheeling path always exists; it does not mean the patterns must be interleaved. Interleaving is an optional choice used to cancel ripple.
- ch 4 [low] Exam traps, first trap: The symbol V_o appears only here; everywhere else the supply-frequency component is called V_1. An undefined symbol in a trap is exactly what a student memorises wrongly.
- ch 4 [low] Quiz Q5 answer: 'The displacement factor falls to about cos α' is the result for a strongly inductive load, where the current is nearly a square wave lagging by α. For a resistive load the fundamental current lags by much less than α (roughly α/2), and the power factor falls mainly because the RMS voltage falls.
- ch 5 [high] Worked example 1 (and quiz Q5, which reuses its numbers): A fundamental output of 200 V RMS cannot come from a 230 V RMS single-phase supply. The group formula in the chapter gives a peak average of 2V_m/π = 2 × 325.3/π = 207 V, so the largest possible fundamental is 207/√2 = 146 V RMS (0.637 × V_s). With V_om = 200√2 = 282.8 V, the chapter's own ratio k = πV_om/(2V_m) = 1.37, which breaks the k ≤ 1 condition stated two sections earlier.
- ch 5 [low] Section 1, group average voltage formula: V_d = (2V_m/π) cos α is the single-phase full-bridge result, but the text calls each group 'a normal phase-controlled converter' without saying single-phase. Most large cycloconverters use three-phase groups, where the formula is different, so a student may apply the wrong one.
- ch 5 [low] Section 1 and the figure: The 50 Hz → 25 Hz example has an output half cycle of 20 ms, exactly one supply cycle. There is almost no room to modulate α within a half cycle, and 25 Hz is above the f_s/3 quality limit the chapter sets later. The illustration therefore shows a case the text itself calls poor quality, without saying so.
- ch 5 [low] Exam traps, second bullet: 'Do not claim any output frequency' is unclear; it can be read as 'do not state the output frequency at all', which is the opposite of the intended warning.
- ch 6 [high] Section 1, first paragraph (switch notation): The notation contradicts the figure. The text defines "switch Sij connects input i to output j", but the figure labels the nine devices S1 to S9 row by row: S1, S2, S3 are the three switches feeding output A. A student applying the Sij rule would read S2 as "input 2 to output 2", not "input b to output A", so the worked state (S2, S6, S7) cannot be decoded from the stated definition.
- ch 6 [low] Section 1, second paragraph (shared inputs): "Two outputs may share an input in some states, but many schemes avoid it to keep input currents balanced" misleads. States in which outputs share an input cannot be avoided in practice; the zero states connect all three outputs to one input and are used in every space-vector scheme. It is the choice of states, not avoidance, that shapes the input current.
- ch 6 [low] Section 2, the 0.866 limit paragraph: "The input voltage triangle" is not defined anywhere and is not a triangle in this context. A student cannot see where the √3/2 comes from.
