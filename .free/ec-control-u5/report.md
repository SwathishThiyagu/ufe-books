# ec-control-u5: free-model run

- Book: `books/eie/ec-control/ec-control-u5.html`
- Status: ok
- Model calls so far: 22 (73,881 tokens in, 258,294 out), 9.3 minutes

## Checker

```
ec-control-u5.html: 8 chapters, 13725 words, 9 figures, 148 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 1, second paragraph: The sentence is broken: "u = Umax when e > 0 and u = Umin when e max the upper level (heater on)". The condition for the low output (e < 0) is missing and the words run into the definition of Umax, so the ideal law cannot be read.
- ch 1 [low] Section 1, third paragraph, and Section 2, first paragraph: "h is in output units, e.g. °C" and "a ... b ... in output units per minute" use "output" for the controlled variable. In this chapter u is the controller output (power, volts) and y is the temperature, so a student may read h and the rates in the wrong units.
- ch 1 [low] Section 3, first paragraph: "The slope at e = 0 is infinite and the output saturates" describes a relay as if it were a saturating proportional element. A relay has no slope at e = 0; it jumps between two fixed levels.
- ch 2 [low] Exam traps, fifth bullet: The clause 'too large Kp lowers damping and causes oscillation' sits right after a first-order-loop statement. A first-order plant under P control gives a first-order closed loop, which cannot oscillate. A student may think a first-order loop can be made to oscillate by raising Kp.
- ch 2 [low] Section 1 (D bullet) and Section 2 (second-order plant): The D branch is said to add 'speed'. In the chapter's own second-order analysis, PD leaves ωn,eff = ωn√Kp unchanged and only raises ζeff. Damping rises; the natural frequency does not.
- ch 2 [low] Section 1, time-domain formula: The integral is written as '∫0te(τ)dτ' with the limits run together, and the control signal u(t) is used without ever being defined.
- ch 2 [low] Worked example 1, step 5 and Quiz Q4 answer: The limits in the velocity-error-constant limit are run together: 'Kv=lims→0sL(s)'. On a phone this reads as a product, not a limit.
- ch 2 [low] Section 2, PD sentence: 'PD adds damping' is stated without noting that it also shifts the closed-loop zero and so slows the very first part of the response when Kd is large; the sentence also does not say the added zero is at s = −Kp/Kd.
- ch 3 [low] Section 1, bullet list: "If the output decays, raise Kp. If it grows, lower Kp." A student can read "grows" as the output value rising to a new steady level, which happens with almost any P gain, rather than the oscillation amplitude growing. The action-word pair is also easy to mix up.
- ch 3 [low] Exam traps, fourth bullet: Ti and Td belong to the standard (ideal) form Kp(1 + 1/(Ti s) + Td s) as well as to the series (interacting) form; calling Kp, Ti, Td the "series-form settings" is not the usual naming and can confuse a student meeting the three forms for the first time.
- ch 4 [low] Section 1, first paragraph: Writing 'a zero at −z rad/s, a pole at −p rad/s' mixes a point on the s-plane with a frequency. A student may read it as a zero at a negative frequency instead of at s = −z.
- ch 4 [low] Section 2, Bode design steps: The step says to read the uncompensated gain crossover but never uses it. The formula φm = PMreq − PMold + δ quietly assumes the plant phase at the new crossover is close to the plant phase at the old crossover, with δ absorbing the difference. A student may think the formula is exact.
- ch 4 [low] Section 3 / worked example, after step 8: 'The closed-loop characteristic equation is s²+4s+16=0' drops the cancelled factor. Before cancellation the loop characteristic polynomial is (s+2)(s²+4s+16), so the pole at −2 remains a closed-loop mode unless the zero-pole cancellation is exact.
- ch 5 [low] Section 2, steps 4 and 6: The procedure never links β to the plant gain at the chosen ωc′. Step 6 then checks PM = 180° + ∠G(jωc′) + ∠C(jωc′) as if ωc′ were the gain crossover. Unless β is chosen so the lag attenuation cancels the plant gain there, |KG(jωc′)C(jωc′)| is not 1 and the number computed is not the phase margin.
- ch 5 [low] Section 2, step 6, last sentence: 'Increase β' works only with the Kc = 1/β option, where the extra attenuation lowers crossover. With the Kc = 1 option listed just above, raising β raises the low-frequency gain (and Kv) while the high-frequency loop gain stays the same, so crossover stays put or moves right and PM falls slightly. The advice is stated without that condition.
- ch 6 [high] Section 1, bullet 'Lead bracket': The line is corrupted and unreadable: 'DC gain z1/p1 1p1).' A student cannot tell whether the lead bracket DC gain is above or below 1, and the missing inequality is the whole point of the lead/lag distinction.
- ch 6 [low] Section 2, bullets 1 and 3: Two different bullets make two different parameters responsible for the same steady-state-error gain: β is found from the error specification and the lag pole is set to ωz2/β (so the lag alone gives a low-frequency boost of β), yet the next bullet says to raise Kc so the low-frequency gain meets the error constant. A student who does both gets a low-frequency gain β times too large.
- ch 6 [low] Section 1, formula glossary: 's = jω is the Laplace variable in rad/s' is loose: s is the complex Laplace variable, and only on the frequency-response plot is it restricted to s = jω.
- ch 6 [low] Section 1 formula vs the figure: The formula writes the lead bracket first, while the figure and its caption put the lag section first. Multiplication is commutative, so nothing is wrong mathematically, but the mismatch can make a student think the two orderings mean different compensators.
- ch 7 [low] Figure (block diagram), node 'spec': The specification node carries the achieved results — 'PM 51.8°, ωgc 3.14' — so the box that is supposed to feed the design already contains the answer, and the same PM 51.8° appears again in the Verify node. A student can read this as 'the spec is whatever the design produced'. The ωgc value also has no unit.
- ch 7 [low] Quiz Q1, answer: The magnitude part of the answer reads 'with magnitude 1 for the chosen K', which does not say what equals 1. For 1 + K G(s)H(s) = 0 the condition is K|G(s0)H(s0)| = 1, not |G(s0)H(s0)| = 1.
- ch 7 [low] Section 3, first paragraph: 'Decide the new gain crossover from the required PM plus a safety margin of about 5°' is too compressed. It does not say that the margin is added to the required PM to get the phase lead the compensator must supply, and that the new crossover is the frequency where the uncompensated phase has fallen to −180° + required PM + margin.
- ch 8 [high] Exam traps, second bullet (derivative term): The claim 'The gain changes by 1/T²' is wrong. Using Kd instead of Kd/T makes the derivative term smaller by a factor T, so the derivative gain differs by a factor 1/T, not 1/T² (with T = 0.1 s the derivative term is ten times too small, not a hundred). The bullet heading also names the wrong fault: the mistake is forgetting to divide by T, not dividing by T.
- ch 8 [low] Section 3, first sentence: 'Two standard conversions from s to the delay z−1' is loose wording: s is not converted to z⁻¹, it is replaced by an expression in z⁻¹ that stands for a one-sample delay.
