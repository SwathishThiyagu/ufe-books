# ec-control-u1: free-model run

- Book: `books/eie/ec-control/ec-control-u1.html`
- Status: ok
- Model calls so far: 27 (93,556 tokens in, 224,440 out), 5.9 minutes

## Checker

```
ec-control-u1.html: 9 chapters, 16221 words, 10 figures, 162 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Quiz Q4: The question opens with "A tank holds 100 L", which reads as tank capacity. On that reading an answer of 160 L in part (a) overflows the tank and 130 L is above capacity, so the problem looks physically impossible.
- ch 1 [low] Section 3, physiological example: Fever is called "a disturbance", but the Exam traps say a disturbance enters at the plant while a shift of the target is a reference change. Fever resets the hypothalamic set point, so the two statements contradict each other and a student will not know how to classify it.
- ch 1 [low] Section 1, definition of controller: The controller is defined as deciding "from the reference and the error", but in Section 2 the open-loop controller has no error signal at all, so the definition does not fit half the chapter.
- ch 2 [low] Section 2, sensitivity formula box: 'Fractional change ratio' is not a standard name for S; no textbook uses it, so a student may think it is a second quantity or a different definition.
- ch 2 [low] Quiz Q7, answer (analyze): The condition '|GH| ≥ 1 at −180° phase' is stated as unstable. At |GH| = 1 exactly the closed-loop poles lie on the imaginary axis, so the system is marginally stable, not unstable.
- ch 2 [low] Section 3, disturbance bullet: 'Attenuated by about 1 + GH' can be read as a subtraction rather than a division by 1 + GH.
- ch 3 [low] Lead: The UPI example suggests a payment server's response to a request can be modelled by a transfer function. Such a server is a queueing, event-driven, nonlinear system, so a student may wrongly conclude that any input-output pair fits the LTI model.
- ch 3 [low] Section 2: 'zeros shape how inputs combine' is too vague. A student cannot tell what a zero actually does to the response.
- ch 4 [low] Figure caption: The caption says 'Notice the same three element types: inertia, spring and damper', but the Rotational branch of the tree shows only one node, 'Inertia J'. The figure does not show any rotational spring or damper, so the caption promises something the figure does not deliver.
- ch 4 [low] Section 3, standard-form paragraph: 's² + 2ζωns + ωn²' runs the symbol ωn straight into s, so a reader on a phone can read it as ωns or as 2ζωns as one quantity.
- ch 4 [low] Quiz Q1: The answer gives F = c v, but the chapter itself defines the damper force as −c x′, opposing motion. A student may take F = c v as the signed force in the equation of motion.
- ch 5 [low] quiz, Q5 answer: The closing phrase 'wrong by a factor of 4, which is √(k²)' is confusing: √(k²) is just k, so the extra square root adds nothing, and 'by a factor of 4' does not say whether the wrong value is 4 times too big or 4 times too small (it is 4 times too small). A student may think some square-root rule is at work here.
- ch 6 [low] Section 1, mechanical equation: The text says 'The load has inertia J (kg·m²) and viscous friction b', which suggests J is only the external load. The equation J dω/dt + bω = T then only holds if J and b are the total inertia and damping referred to the motor shaft, including the rotor itself. A student may use only the load inertia and get a wrong answer.
- ch 6 [low] Section 1 and exam traps, Kt–Kb equality: 'Kt and Kb are often equal numerically when losses are ignored' is a hedge that can confuse. In SI with N·m/A and V·s/rad the two constants are equal by energy conservation; the loss caveat belongs to efficiency, not to the constant relation.
- ch 6 [low] Figure spec: The block notes give fixed numbers (Kt = 0.5 N·m/A, Kb = 0.5 V·s/rad) in a diagram meant to be general, so a reader may take them as fixed motor data rather than the worked-example values.
- ch 7 [high] Section 1, linearised outflow: The text writes qout = h/R and then says linearisation of qout = Cd a √(2gh) gives this R. If h is the absolute level, the correct small-signal linearisation about h0 is qout = q0 + (h - h0)/R, or in deviation form Δqout = Δh/R. Using qout = h/R with absolute h gives the wrong operating outflow and can make students apply the linearised R as if it were valid for total level.
- ch 7 [high] Section 3, volumetric-flow note: The sentence says to absorb the reference density into Rp only. If q is volumetric, both the resistance and the capacitance change: Rp,vol = ρ Rp,mass and Cp,vol = Cp,mass/ρ = V/(ρ Rg T). Leaving Cp in kg/Pa makes the equation unit-inconsistent.
- ch 7 [high] Figure: The feedback block is labelled R = 5. In a block diagram the feedback path from h to the summing junction must compute qout = h/R, so its gain is 1/R = 0.2 m²/s, not R. A block gain of R would imply qout = R h and contradict the worked example and τ = 10 s.
- ch 7 [low] Exam traps, mixing gauge and absolute references: The phrase 'absolute T uses no Ta in the left side' is unclear; the energy balance always has Ta in the loss term (T − Ta)/Rt when absolute temperature is used.
- ch 7 [low] Section 3, Cp formula: Cp = V/(Rg T) assumes isothermal changes in the fixed volume. The chapter does not say this; for adiabatic small changes the capacitance is V/(γ Rg T).
- ch 8 [high] Exam traps, second bullet: The compensating factors for a moved take-off point are reversed. Moving a take-off point from before G to after G means it now taps GX, so the branch needs 1/G to recover X, not G. Moving it from after G to before G means it now taps X, so the branch needs G, not 1/G. As written, the trap contradicts Section 2 and the answer to Q4.
- ch 8 [low] Section 2, opening lines: "The crossed block is G" is vague: a student may not connect "crossed" with the block the point is moved across.
- ch 9 [low] Quiz Q8 answer: The answer says the extra ΣLiLj product makes the denominator polynomial 'gain a wrong constant term'. That is true only when both loop gains are pure numbers. In an s-domain graph the loop gains are functions of s, so the product L1L2 adds a term that changes several coefficients (and possibly the degree) of the denominator, not just its constant.
