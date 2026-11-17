# e-bee-u3: free-model run

- Book: `books/common/e-bee/e-bee-u3.html`
- Status: ok
- Model calls so far: 33 (128,991 tokens in, 237,172 out), 6.1 minutes

## Checker

```
e-bee-u3.html: 8 chapters, 15096 words, 9 figures, 156 KB
OK
```

## For the reviewer

- chapter 8: the figure cannot be drawn: tree is too wide (6 leaves); use fewer leaves or shorter labels

## Reviewer notes (after any revision)

- ch 1 [high] Exam traps, fourth bullet: The trap says that adding MMFs directly in a series circuit is a mistake. This contradicts Section 3, which correctly states that the total MMF is the sum of the part MMFs, F = ΦS_iron + ΦS_gap. A student will wrongly conclude that MMFs never add in series.
- ch 1 [low] Lead: A transformer core is normally a closed iron path with no intentional air gap. Naming a transformer as a device where a small air gap controls flux is misleading, even as a passing example.
- ch 1 [low] Figure: The reluctance node notes '4.97 × 10⁵' and '1.99 × 10⁶' give numbers without units, which breaks the rule that numbers carry units and may confuse the reader.
- ch 2 [high] section 1, sinusoid paragraph, and figure caption: The paragraph gives e = −N·Φₘ·ω·cos ωt and then says 'The EMF leads the flux by 90°'. A negative cosine lags the sine it came from: with Φ = Φₘ sin ωt, e = NΦₘω·sin(ωt − 90°), so the induced EMF lags the flux by 90°, not leads. The figure also plots e = +cos (dropping the minus sign of Faraday's law), so formula, sentence and plot contradict each other. A student will lose marks on the standard exam statement that the induced EMF lags the flux by 90°.
- ch 2 [low] section 1, second paragraph: 'In a sinusoid the resistance shows up as a time shift' names the wrong quantity. Resistance in a coil causes no phase shift here; it is Lenz's-law opposition (the minus sign) that shifts the EMF by 90° from the flux. A student may think R is what shifts the phase.
- ch 3 [low] Section 2, the [formula] note after E = 4.44 f N Φm: The gloss "4.44 = 4 × 1.11, the form factor of a sine wave times the half-cycle average 4fΦm" is garbled. Read literally it says the form factor multiplies the average to give something called a 'half-cycle average', which is not what is meant. A student may not see which factor is the form factor and which is the average EMF per turn.
- ch 3 [low] Exam traps, third bullet (inverting the current ratio): The text says "current ratio is N₂/N₁" without saying which current is on top. Earlier the chapter fixes I₂/I₁ = N₁/N₂, so a student who reads this bullet as I₂/I₁ = N₂/N₁ gets a rule that contradicts the formula block above it.
- ch 3 [low] Quiz Q6: The answer opens with "The flux stays constant, so dΦ/dt is zero", which is only true after the transient. At the instant of switching on, the current and the core flux rise from zero, so an EMF is induced for a short time and the current is partly limited during that rise. Stating that flux is constant from the start will confuse a student who knows Faraday's law.
- ch 3 [low] Quiz Q4: Q4 repeats Worked example 2 word for word (same 200 turns, same 230 V, same 50 Hz, same answer 5.18 mWb). It tests nothing new and uses up 4 marks.
- ch 4 [low] Section 1 (construction) and Quiz Q1 answer: The chapter says the commutator reverses each coil's connections 'twice per revolution'. That is true only for a simple 2-pole machine. In a P-pole machine the coil EMF completes P/2 cycles per revolution, so the commutator reverses the coil P times per revolution. Since the worked example uses a 4-pole machine, a student will apply 'twice' to a 4-pole case and be wrong.
- ch 4 [low] Section 3 (motor action): The force formula F = BIl is written without defining its symbols, though the chapter defines symbols everywhere else.
- ch 4 [low] Quiz Q6 answer: 'the voltage per path is lower' is unclear. The parallel paths all have the same EMF; the point is that with A = P paths the EMF of each path (which becomes the terminal voltage) is lower than a wave winding with the same conductors, while the total current splits into P paths.
- ch 5 [high] Section 3 (torque-slip curve), against the table: The chapter contradicts itself on starting torque. Its own formula with s_m = 0.20 gives T/T_max = 0.38 at standstill (the table says so), and the table puts full load at 0.47 T_max. So the curve implies a starting torque of about 0.38 × 2.1 ≈ 0.8 times full-load torque — less than full load, which could not start a loaded machine. Two paragraphs later the text says a standard cage motor has 'a starting torque of roughly 1.5 to 2 times full-load torque'. A student who checks the table will find the text wrong, and vice versa.
- ch 5 [low] Section 1, formula N_s = 120 f / P: P is described as 'the number of poles per phase winding'. That is non-standard wording. A reader can easily multiply by 3 and get 500 rpm for a 4-pole motor.
- ch 5 [low] Section 3, formula T = 2 T_max / (s/s_m + s_m/s): Presented as exact, but it is the approximate form that ignores stator resistance and stator leakage reactance. Students who compare it with measured motor data will find the standstill end of the curve much too low.
- ch 5 [low] Section 1, bullet 2: '(Chapter 3.2)' is written as plain text, so the cross-reference does not link.
- ch 6 [low] Section 2, centrifugal switch sentence: The switch is said to cut out at 'about 75% of full speed'. Textbooks state this as a percentage of synchronous speed; on a motor with a few percent slip the two numbers differ and students repeat the wrong reference point.
- ch 6 [low] Quiz Q4, answer: The reasoning is loose: 'much larger relative speed' is offered as the cause of 'much less torque', but a larger relative speed by itself would mean more rotor EMF, not less torque. A student can read this as a contradiction.
- ch 6 [low] Figure (Capacitor-start motor block diagram): The figure sits after Section 3, but it illustrates the capacitor-start method of Section 2 and repeats the 85° split of Worked example 1. The reader meets it one section late, after the universal-motor material.
- ch 7 [high] Section 3, paragraph on overexcited motor and field control: The sentence 'This control is why field current is adjusted in steps, not continuously in simple sets' is technically wrong. Synchronous-motor field current is normally varied continuously by a field rheostat or an exciter/AVR; power-factor control is not inherently stepwise.
- ch 7 [low] Section 2 formula V_L = √3 E_ph, Worked example 1 step 6, Quiz Q4: The chapter calls √3 times the generated phase EMF the 'line voltage' without saying no-load. Under load the terminal line voltage is not √3 E_ph because armature reaction and synchronous impedance drop the terminal voltage; the calculation is valid only for open-circuit/no-load EMF.
- ch 8 [high] Section 3 (BLDC motor: brushes replaced by electronics): The text says 'speed is set by the switching frequency'. In a BLDC motor the commutation frequency follows the rotor; you cannot set the speed by choosing a switching frequency the way a V/f induction-motor drive does. Speed comes from the DC bus voltage and the load.
- ch 8 [low] Section 1, open-loop paragraph: Pull-out torque is used as if the reader already knows it, but the chapter never defines it. A student cannot tell how it differs from holding torque.
- ch 8 [low] Section 2, second paragraph: 'if θact is too large, it reverses' is ambiguous: 'it' could be read as the motor reversing direction, whereas only the torque is reversed.
- ch 8 [low] Section 1, last bullet, and Section 2, third paragraph: 'Units 4 and 5' and 'Chapter 3.4' are plain text, so they are not clickable cross-links like the rest of the book's chapter references.
