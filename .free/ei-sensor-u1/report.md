# ei-sensor-u1: free-model run

- Book: `work/ei-sensor-u1/tree/books/eie/ei-sensor/ei-sensor-u1.html`
- Status: ok
- Model calls so far: 26 (110,889 tokens in, 186,139 out), 6.1 minutes

## Checker

```
ei-sensor-u1.html: 6 chapters, 19929 words, 8 figures, 217 KB
OK
```

## For the reviewer

- chapter 1: the figure cannot be drawn: tree is too wide (6 leaves); use fewer leaves or shorter labels
- chapter 1: worked example 2: the worked example states [1.0000000000021104e-05] but recomputing it gives [0.02498750624687656, 1.249375312344092e-05]; fix the steps and the answer so they match the correct values
- chapter 1: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [high] Section 2, second paragraph: 'A passive sensor ... converts nothing' is wrong and contradicts Section 1 ('Every sensor is a transducer'). A passive sensor does convert the measurand — into a change of resistance, inductance or capacitance. What it does not do is generate a signal of its own. A student can quote this line and lose marks.
- ch 1 [low] Exam traps, third trap: 'It draws no power to sense' is false: a passive sensor draws power from the excitation supply while it is sensing, and that is exactly why self-heating is a design issue (as the chapter itself says in Section 2 and Worked example 1). The trap's own wording repeats the mistake it warns against.
- ch 1 [low] Section 1, third paragraph: 'For a purpose other than measurement' is an added restriction that standard definitions do not carry. Inverse transducers are common inside measurement systems — the pen motor of a chart recorder, the deflection coil of a CRO — so the qualifier can mislead.
- ch 1 [low] Lead: 'emf' is used from the first sentence and never expanded. Many readers will not know it means electromotive force, that is, a source voltage.
- ch 1 [low] Section 2, active list and Worked example 1(b): '12 mV per g' uses g without definition. In a sensor chapter a reader can take g for gram; it here means the acceleration due to gravity, 9.81 m/s².
- ch 1 [low] Section 3, first paragraph: 'Digital output travels over long cable without losing accuracy' is too absolute. A digital signal resists noise far better than an analog one, but long cables, ground loops and ringing can still corrupt pulses or code words.
- ch 1 [low] Beyond box: 'MEMS' is not expanded anywhere, and the box is meant for reading without other references.
- ch 2 [high] Section 1, first sentence: The text says every sensing path has four stages, then lists five: stimulus → sensing element → physical law → parameter change → electrical output. The figure also has five nodes. A student counting stages will think one is missing.
- ch 2 [low] Section 3, Faraday's law: e = −dΦ/dt is the single-turn form. The preceding sentence describes a coil with N turns, so a student applying it to that coil will drop the factor N.
- ch 2 [low] Lead paragraph: "A temperature difference across two metals makes a small emf" is loose. The emf comes from two junctions of two dissimilar metals held at different temperatures, not from a difference "across" the metals. Section 2 states it correctly, so the lead contradicts it in form.
- ch 2 [low] Exam traps, second trap: "A 10 % gap change gives about 11 % capacitance change" is only true for a 10 % reduction in gap. A 10 % increase gives about 9.1 %. Without the direction the trap teaches the wrong number.
- ch 2 [low] Section 1, electrical quantities: The symbol C is used for the coulomb (unit of charge) and then immediately for capacitance and for the change in capacitance (ΔC). Readers with English as a second language can trip over this in the same paragraph.
- ch 3 [high] Section 1, conversion paragraph: The V/psi to V/kPa conversion is done in the wrong direction. Multiplying 0.137 V/psi by 6.89476 kPa/psi gives 0.945 V·kPa/psi², which is not a sensitivity at all. Since 1 psi is bigger than 1 kPa, a sensitivity in V/psi must become a smaller number in V/kPa, not a larger one. The stated 0.945 V/kPa also contradicts the worked example's 19.9 mV/kPa for the same sensor and contradicts Quiz Q3.
- ch 3 [low] Section 1, dimensional-check sentence: Saying 'a pressure sensor giving 19.9 mV/kPa has a unit of V/Pa' is dimensionally true but numerically misleading: 19.9 mV/kPa equals 1.99×10⁻⁵ V/Pa, so a student may read the two as the same number.
- ch 3 [low] Worked example step 10 and Exam traps, %FS denominator: The chapter defines full scale as the span, the algebraic difference between the range limits, and says it is the %FS denominator. For this sensor the output span is 4.00 − 0.02 = 3.98 V, but step 10 and the trap use 4.00 V, which is the output at the upper limit, not the span. The two rules disagree and the numbers differ slightly (0.75 % versus 0.754 %).
- ch 3 [low] Figure spec, 'SI base units' note: The note lists only m, kg, s, A, K, while the text names seven base units. A student comparing figure and text will think mol and cd were dropped.
- ch 4 [high] Section 1, Range and span paragraph: It says a sensor can have a zero offset, so range and span are not the same. Zero offset is an output offset at zero input, not a non-zero lower input limit. The sentence confuses input range with output offset.
- ch 4 [low] Section 2, hysteresis definition: Hysteresis is defined as 'the difference' between up-scale and down-scale readings. The specification should be the maximum difference over the range; the quiz later uses 'maximum difference'.
- ch 5 [high] Section 3, second paragraph ("For a step of size A and ζ  1 it is overdamped..."): The sentence is broken: the text for ζ < 1 and ζ = 1 is missing, so the reader never learns that the response overshoots when ζ < 1 and that ζ = 1 is critically damped. Worse, the standard step-response results used later — overshoot Mp = exp(−πζ/√(1−ζ²)) and peak time tp = π/ωd — are never stated, yet the worked example (steps 7 and 8) and quiz Q5 compute them from nothing.
- ch 5 [high] Section 1, zero order (potentiometer sentence): "A heavy load adds lag and makes it first order" is not correct. Finite load resistance on a potentiometer causes a loading error — the output becomes a nonlinear function of wiper position — but a purely resistive load stores no energy, so it creates no time constant and no lag. The potentiometer's actual dynamic lag comes from the mass and compliance of the wiper, which makes it second order at high speed, not first order.
- ch 5 [low] Section 3, last two lines: ωd appears in "the impulse response is a decaying sine at ωd" without being defined in the section, and the decay rate is not given. Students meet ωd for the first time in the worked example.
- ch 5 [low] Section 2 (thermocouple model) versus Section 2 step response and Section 3: The symbol A is used twice: for the surface area of the thermocouple bead in τ = mc/(hA), and for the step size in y(t) = K A (1 − e^(−t/τ)). The same letter meaning two things in one section confuses a first-time reader.
- ch 6 [high] Worked example 1, steps 5–6 and answer: Section 3 tells the student to combine the resolution uncertainty in quadrature with the scatter, but the example stops at the scatter and quotes the 95 % interval as ±11.5 mV only. The resolution term (2.887 mV) is not negligible, and the stated final uncertainty is therefore too small and contradicts the chapter's own rule.
- ch 6 [high] Quiz Q5 answer: The scatter term is computed as 0.002/√4 = 0.0005 V. With n = 16 the divisor must be √16 = 4; as written the step divides by 2 and the shown arithmetic (0.002/2 = 0.001) does not even give the stated 0.0005 V.
- ch 6 [low] Section 3, power-law rule: The formula is printed as “y = an”, which reads as a multiplied by n, not as a power. A student may apply the rule to the wrong expression.
- ch 6 [low] Worked example 1, step 5: Using k = 2 with only n = 10 readings gives about 93 % coverage, not 95 %, because the mean of 10 readings follows a t-distribution with 9 degrees of freedom. The stated 95 % interval is slightly optimistic.
- ch 6 [low] Quiz Q4 answer: The answer quotes y = 100.0 and u_y = 5.385 with no units, so the student cannot see that u_y carries the same unit as y.
