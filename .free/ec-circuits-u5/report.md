# ec-circuits-u5: free-model run

- Book: `books/ece/ec-circuits/ec-circuits-u5.html`
- Status: ok
- Model calls so far: 30 (133,934 tokens in, 247,228 out), 4.7 minutes

## Checker

```
ec-circuits-u5.html: 9 chapters, 17017 words, 10 figures, 180 KB
OK
```

## For the reviewer

- chapter 5: the figure cannot be drawn: note "unstable, grows" runs off the right edge; shorten it

## Reviewer notes (after any revision)

- ch 1 [high] Exam traps, bullet 1: This trap contradicts Section 2 and Worked Example 1. It says treating the inductor as an open circuit or the capacitor as a short at t = 0⁺ is wrong, and that the short/open rule belongs only to t → ∞ and DC steady state. But Section 2 and Step 3 of the worked example both use exactly that: with nothing stored, the 0 A inductor source is an open branch and the 0 V capacitor source is a short (20/4 = 5 A in Q6 depends on it). As written, a student who follows the trap will refuse to short the capacitor at 0⁺ and get the worked example and Q6 wrong.
- ch 2 [low] Section 2, R comparison paragraph: The line 'More resistance removes more energy per ampere' is loose. For a fixed I₀ the stored energy ½LI₀² is the same whatever R is; R only changes how fast that energy leaves.
- ch 2 [low] Exam traps, second trap: 'That is the charging curve' is imprecise. On a charging curve the value at t = τ is 63.2 % of the final value, not of the starting value.
- ch 2 [low] Figure: The tangent series is defined as 1 − x and is tabulated all the way to −4, while the plot's y minimum is 0. The line will be clipped or will stretch the y-axis far below zero, and the tangent only matters between t = 0 and t = τ.
- ch 2 [low] Figure caption: 'one unit on the x-axis is 5 ms' is unclear because the x-axis is labelled t/τ, not t.
- ch 2 [low] Lead: A fan slowing down is mostly mechanical inertia, not an electrical time constant. A student may connect the two wrongly.
- ch 3 [low] Section 1 and Section 2 prose, and Section 3 pulse paragraph: The exponential is typed as plain text in several places ("A e−t/τ", "vC = Vs(1 − e−t/τ)", "i = (Vs/R)e−t/τ"), so a student reads "e minus t over tau" instead of e raised to −t/τ. Formulas elsewhere in the chapter use the superscript tag, so the notation is inconsistent.
- ch 3 [low] Section 3, pulse paragraph: "the output looks like a distorted copy of the pulse" does not say which quantity is the output. When Tp is much smaller than τ the capacitor voltage barely moves; it is the resistor voltage that copies the pulse shape, and the capacitor voltage is a small, rounded version of it.
- ch 3 [low] Beyond: "SPICE transient analysis solves exactly this exponential update" is not accurate. SPICE steps time with numerical integration rules (backward Euler, trapezoidal, Gear) using a companion model; the exponential comes out as an approximation whose accuracy depends on the time step.
- ch 3 [low] Lead: "every voltage and current settles along the same exponential curve" can be read as saying all variables share one waveform. They share only the time constant τ; each has its own starting value, final value and sign, so some rise and some fall.
- ch 4 [high] Section 1, the sentence after the three bullets: "α = 12 s⁻¹ and ω₀ = 10 rad/s is overdamped because 144 > 100, even though α is larger than ω₀." The words "even though" say α > ω₀ is surprising or against the answer. It is the opposite: α > ω₀ is exactly the overdamped condition given in the bullets two lines above. A student will think α > ω₀ is not a valid test.
- ch 4 [high] Exam traps, second trap: "Comparing α with ω₀ directly; compare α² with ω₀²." Comparing α with ω₀ directly is correct and is the standard test; it is what Section 1 uses in its own bullets (α > ω₀ overdamped, α = ω₀ critical, α < ω₀ underdamped). Calling this a trap contradicts the chapter and will make students reject a valid method.
- ch 4 [low] Figure: The legend and aria text label the curves with ζ (ζ = 0.2, 1, 2), but ζ is defined nowhere in the text; only α and ω₀ are defined, and ζ first appears unexplained in the Beyond paragraph.
- ch 5 [low] Section 2 (after the ω_d formula): The sentence 'They differ only when ζ is large' is misleading. ω_d and ω_n differ for every ζ > 0, just by a small amount when ζ is small (in the worked example ζ = 0.1 gives only a 0.5 % difference). A student may read it as ω_d = ω_n at moderate damping.
- ch 5 [low] Section 2 (real part of the pole): 'The real part −ζω_n is the decay rate in s⁻¹' blurs two quantities: the decay rate constant is σ = ζω_n, and −ζω_n is the real part of the pole (a negative number). Written as it stands, a student may think the decay rate is negative or be unsure of the sign.
- ch 5 [low] Quiz Q3 answer: 'Damping removes energy every cycle, so the circuit completes its swings more slowly' gives the wrong cause. Losing energy per cycle does not by itself change the oscillation frequency; the damping force (proportional to velocity) opposes motion and reduces the net restoring effect, which lengthens the period.
- ch 6 [high] Section 3, paragraph 'Switching at a bad instant can double the first peak': The sentence 'A 2 A steady current with a 2 A offset starts near 4 A or near 0 A, depending on φ' contradicts the chapter's own rule. K = i(0⁺) − i_ss(0), so when the circuit is switched on with zero initial current (the normal case, and the case of the worked example and the figure), the total always starts at 0 A whatever φ is. It cannot start at 4 A. A student will read this as 'the current jumps to 4 A at t = 0', which conflicts with inductor-current continuity that the chapter stresses twice.
- ch 6 [low] Section 1, paragraph 'Series RC works the same way' and exam trap 4: The text says 'K still comes from the total current at t = 0⁺' without saying how i(0⁺) is found in an RC circuit. The capacitor voltage cannot jump, but the current can, so a student may wrongly assume the current is continuous at t = 0⁺ the way an inductor current is. The chapter never states the rule it uses in Quiz Q5.
- ch 7 [high] Quiz Q1 (answer): The answer says the 0⁻ limit 'keeps any jump at the switching instant outside the integral', which is the exact opposite of what Section 1 states and of the truth: the lower limit 0⁻ is taken so that the jump at t = 0 falls inside the integration range, which is why the initial-condition term −f(0⁻) appears in the derivative rule. A student reading both would be confused about the whole reason for 0⁻.
- ch 7 [low] Section 3, repeated poles: The inversion of a repeated pole is given as t^(r−1) e^(pt) with no factorial. For r ≥ 3 a factor 1/(r−1)! is missing, so the stated general rule is off by a scale factor (only r = 2 happens to be right).
- ch 7 [low] Section 3, partial fractions and the pair table: The method reads every term off the six-entry pair table, but that table has no entry for the repeated-pole shape the text itself introduces (t e^(−at)), and nothing says F(s) must be strictly proper before the K_i formula is used.
- ch 8 [low] Section 2: The text says the poles do not depend on where the input is applied, then says only 'the zeros do depend on where the output is taken'. A student can read this as: zeros depend only on the output port. In fact the zeros depend on both the input port and the output port.
- ch 8 [low] Worked example 1, step 1 and answer: Writing H(s) = 100/(s² + R s + 100) 'where R is the resistance value in ohms' hides the units. The coefficient of s is R/L, not R: it equals the number R only because L = 1 H, and its unit is s⁻¹. A student may try to add ohms to seconds.
- ch 8 [low] Section 3: 'A pole at s = 0 is a constant offset' is vague and can mislead. A pole at the origin puts a constant, non-decaying term A e^(0·t) = A in the impulse response; the step response of such a circuit then ramps without bound.
- ch 8 [low] Section 3: 'A zero near a pole can cancel its visible effect' is too strong. Only an exact zero at the pole removes that term. A zero that is merely near the pole leaves a small residue, and the slow pole still sets the long tail of the response.
- ch 8 [low] Figure: The x-axis is labelled ω/ω₀ while the text and worked example use ω_n, so two symbols stand for the same normalising frequency. The legend also names resistance values (R = 2 Ω, R = 10 Ω) for a curve that is plotted as a generic normalised second-order function.
- ch 9 [low] Section 1, 'What the state vector holds': The sentence 'A circuit with n storage elements has n states' is stated as a rule. It fails for degenerate circuits: two capacitors in parallel, a loop of capacitors only, or a cutset of inductors only. In those cases some states are dependent and the order of the circuit is less than the number of storage elements.
- ch 9 [low] Section 1, definition of D: The text reads 'D is p × m; D is the direct feedthrough through resistors.' The second 'D is' repeats the first and 'through resistors' is vague; a student may not see when D is nonzero.
- ch 9 [low] Exam trap 4: 'A resistor or inductor voltage usually has a direct path from the source, so D ≠ 0' overgeneralises. In a series RLC the resistor voltage is vR = R iL, which is R times a state, so D = 0 there. A student applying the trap to that case gets a wrong D.
- ch 9 [low] Figure in Section 3: The block diagram shows only the Cx path to the output. The full output equation is y = Cx + Du, so the feedthrough path Du from u to y is missing and the figure does not match the equation it illustrates.
- ch 9 [low] Quiz Q6: The answer is written 'e−0.5t times a sine at 3 rad/s'. Without an exponent marker this reads as e minus 0.5t and the damping is unclear.
