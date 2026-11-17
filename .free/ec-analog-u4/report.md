# ec-analog-u4: free-model run

- Book: `books/ece/ec-analog/ec-analog-u4.html`
- Status: ok
- Model calls so far: 31 (128,790 tokens in, 258,349 out), 8.7 minutes

## Checker

```
ec-analog-u4.html: 7 chapters, 13762 words, 8 figures, 146 KB
OK
```

## For the reviewer

- chapter 4: the figure cannot be drawn: too many columns for a left-to-right diagram; use direction "down"
- chapter 2: the figure cannot be drawn: note "shunt-series" runs off the right edge; shorten it
- chapter 2: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [low] Section 2 and Worked example 1, step 5: The relation ΔA_f/A_f = (ΔA/A)/D is a first-order (differential) result, exact only for small changes. The chapter applies it to a 10 % change and quotes 0.91 %, but the exact closed-loop change is 0.83 % (A: 1000 → 1100 V/V makes A_f: 90.91 → 91.67 V/V). The ±20 % → ±1.8 % line is likewise the linear estimate; exact values run about +1.5 % to −2.2 %. A student who checks with a calculator will think the chapter is wrong.
- ch 1 [low] Section 2, first paragraph: 'D spends the lost gain on stability' uses 'stability' in the sense of steadiness of gain, but the chapter later uses 'stability' for freedom from oscillation ('stability is 4.3'). A student can read the two sentences as the same thing.
- ch 1 [low] Lead paragraph: 'the same idea sets the gain by resistor ratio β rather than by the active device' is loose: the gain is set by 1/β, and β itself is a resistor ratio. As written, a student may think A_f = β or that β is the gain.
- ch 1 [low] Section 3, first paragraph and formula line: The text says BW_f ≈ BW × (1 + Aβ) while the formula line right below says BW_f = BW (1 + Aβ). The same quantity is written once as approximate and once as exact, which reads as a contradiction.
- ch 1 [low] Quiz Q6, answer: 'it corrects slow variations and distortion by factor D' — 'slow' is misleading; feedback corrects gain variations and distortion over the whole closed-loop bandwidth, not only slow ones.
- ch 1 [low] Section 3 and Exam traps: Cross-references 'Unit 3', '4.2', '4.3', '4.4' are plain text, not links, so a student reading on a phone cannot jump to them.
- ch 2 [high] Lead and Section 1 (final paragraph), echoed in Section 3 opening line: The chapter says 'Each topology fixes exactly one resistance: mixing decides the input resistance, sampling decides the output resistance' and 'Only the resistance chosen by the topology moves.' That contradicts the chapter's own table and Section 3 formulas, where every topology moves both R_in and R_out by D (voltage-shunt lowers both, current-series raises both). Read literally, a student would conclude voltage-series changes R_in but leaves R_out unchanged, which is false.
- ch 2 [high] Quiz Q7: The last sentence, 'the two mixed cases move only one resistance each', is wrong. Voltage-shunt (mixed units) lowers both R_in and R_out; current-series raises both. No topology moves only one resistance, so the answer contradicts the chapter's table and its own preceding sentence.
- ch 2 [high] Quiz Q6 answer: The reason given for rejecting current-series feedback for a 50 Ω load is physically wrong: 'most of the output current is lost inside the amplifier'. A high R_out makes the stage behave as a current source, so a 50 Ω load still receives nearly the full output current; what actually limits it is the voltage swing needed (I × 50 Ω) and the loss of voltage stiffness, not current lost internally.
- ch 2 [low] Beyond: 'a differential pair with a current-mirror load is a current-series stage' is loose: a stage alone is not a feedback topology; the topology depends on the feedback network placed around it.
- ch 3 [high] Section 1, paragraph beginning "At β = 0 the closed-loop poles...": It says that in a two-pole amplifier the closed-loop poles cross into the right half plane for too much β. A loop with only two poles can never become unstable: under negative feedback the two poles meet on the real axis, break away and stay in the left half plane for every value of β. This also contradicts Section 3 of the same chapter, which says a two-pole loop is always made safe by phase margin, and it contradicts worked example 1, where the gain margin is infinite.
- ch 3 [high] Quiz Q4: The answer treats the 1 kHz pole as giving a full −90° at 5 kHz. The pole is only a factor of 5 below the crossover, so it gives −arctan(5) = −78.7°, not −90°. The stated phase −116.6° and PM 63.4° are therefore both wrong. The chapter's own exam trap warns against exactly this −90° shortcut.
- ch 3 [low] Section 1, last sentence: "Deliberate positive feedback that makes T = 1" can be read as a statement about magnitude only, which would be wrong; an oscillator needs unity magnitude and zero phase around the loop.
- ch 4 [low] Quiz Q3 (and Worked example 1, answer line): Q3 answers that with |Aβ| = 1 exactly the circuit 'oscillates at 2 kHz'. Section 3 of the same chapter states that a circuit with |Aβ| exactly 1 and no start-up mechanism simply sits silent, so the two statements read as a contradiction to a student.
- ch 4 [low] Section 4 (RC row paragraph): 'tune easily with a ganged capacitor or a potentiometer' is imprecise: a Wien-bridge RC oscillator needs two ganged elements (a two-gang variable capacitor or a dual potentiometer), because R and C (or two R's and two C's) must change together to move f₀ without upsetting the balance.
- ch 4 [low] Quiz Q5 answer: The sentence 'the resonant network passes the fundamental but the amplifier is driven hard' is unclear and mixes two ideas; the reader cannot tell what is being contrasted with the thermistor case.
- ch 5 [low] Section 3, thermistor sentence: 'A thermistor works the same way' is too loose. The lamp stabilises because its resistance RISES with temperature (positive coefficient). A common NTC thermistor placed where the lamp is would have resistance FALL with temperature, so the gain would rise as the output rises and the amplitude would run away.
- ch 5 [low] Worked example 1, step 3: 6.5 kΩ is called a standard value, but it is not an E12 or E24 value (those are 6.2 kΩ and 6.8 kΩ). Only the E96 series contains 6.49 kΩ, which rounds to 6.5 kΩ.
- ch 5 [low] Quiz Q7: The question asks for two reasons the Wien bridge is easier to TUNE, but the second reason given (gain of 3 instead of 29) is about amplifier design, not tuning, so it does not answer the question asked.
- ch 5 [low] Section 2, β formula: The displayed formula gives the magnitude of β only, but the next sentence talks about 'the phase of β'. A student may think the formula also carries the phase information.
- ch 6 [high] worked example 1, 'dry run' and 'output' lines: The dry run table is empty and its columns 'i', 'a[i]', 'sum' are array-indexing terms that mean nothing in an LC-oscillator example. The 'output' is an unlabelled list of six numbers (110.0, 1.073, 0.0909, 11.0, 1.125, 4.9). A student has no way to know these are L_eq in µH, f₀ in MHz, β, minimum gain, wrong frequency in MHz and percentage error.
- ch 6 [low] quiz Q5: 1/1000 + 1/1000 + 1/10 = 0.102 pF⁻¹, not 0.101 pF⁻¹, so C_eq = 9.8 pF rather than 9.9 pF. The final 5.03 MHz is unaffected.
- ch 6 [low] section 4, Clapp tuning range: The reason given is unclear and slightly backwards: because C_eq ≈ C3, a change in C3 moves f₀ almost one-for-one. The narrower range of Clapp comes from keeping C3 small compared with C1 and C2, which limits how far C3 can be tuned before the approximation C_eq ≈ C3 fails and the feedback fraction changes.
- ch 6 [low] figure (tank impedance plot): The sampled points skip x = f/f₀ = 1. The Q = 10 curve peaks at 0.992 but the Q = 50 curve peaks at only 0.849, so the sharper curve looks lower than the flatter one. That contradicts the text, which says the peak value is |Z|/R = 1 for every Q.
- ch 6 [low] section 2, last paragraph: 'A few hundred kilohertz to a few megahertz' understates the usual Hartley range; standard texts give roughly tens of kilohertz up to tens of megahertz, the upper limit set by the coil and stray capacitances.
- ch 7 [high] Lead: The lead says the crystal's quality factor is 'often 10⁴ to 10⁶ times better than a coil-and-capacitor tank'. 10⁴ to 10⁶ is the absolute value of Q for a quartz crystal, not the ratio to an LC tank. An LC tank has Q of roughly 10² to 10³, so the crystal is only about 10² to 10⁴ times better. As written, a student would think crystal Q can be 10⁶ × 10³ = 10⁹.
- ch 7 [low] Section 2: 'C is in femt Farads and C₀ in picofarads' — wrong spelling and split word; the unit is written femtofarads.
- ch 7 [low] Quiz Q3 answer: Same spelling slip: 'a few femt Farads'.
- ch 7 [low] Section 2: 'The crystal impedance is small and resistive, equal to R' is only an approximation: at f_s the crystal is R in parallel with C₀, so the impedance is slightly below R and slightly capacitive in phase.
