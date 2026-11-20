import json
from u import *
old = json.load(open('ch6.json'))
A5 = '<a href="#discrete-time-lti-systems-and-convolution-sum">discrete-time LTI systems and convolution sum</a>'
ch = {
'lead': "A difference equation is the discrete-time twin of a differential equation. It ties the present output sample to a few past outputs and to present and past inputs, through fixed coefficients. Give it its starting values and a loop computes every later sample, which is what a digital filter does inside a phone or an ECG monitor. The roots of its characteristic equation decide whether the output settles or blows up.",
'prereq': "You need: the convolution sum and impulse response from " + A5 + ", and the unit step, unit impulse and time shifting (see Standard signals: impulse, step, ramp, exponential).",
'sections': [
 sec("The equation, its order and its two kinds",
  p("A <b>linear constant-coefficient difference equation</b> (LCCDE) of order N is"),
  F("Σ_{k=0}^{N} a_k y[n − k] = Σ_{m=0}^{M} b_m x[n − m]", "Here y[n] is the output, x[n] the input, a_k and b_m are constants with a_0 = 1, N is the order (the largest output delay) and M the largest input delay."),
  p("Moving the past outputs to the right gives the <b>recursive form</b> y[n] = −a_1y[n − 1] − … − a_Ny[n − N] + b_0x[n] + … + b_Mx[n − M], which computes each sample from numbers already known. The coefficients must be plain numbers: a term such as n·y[n − 1] breaks time invariance and y[n]·y[n − 1] breaks linearity."),
  p("If some a_k (k ≥ 1) is nonzero, the output feeds back and the system is <b>recursive</b>; its impulse response normally lasts forever, so it is an <b>IIR</b> (infinite impulse response) system. (A pole cancelled by a zero is the rare exception.) If every a_k = 0 for k ≥ 1, then y[n] = Σ b_m x[n − m], the convolution sum with h[n] = b_n for 0 ≤ n ≤ M: a <b>non-recursive</b> or <b>FIR</b> system."),
  p("To start the recursion you need N past outputs y[−1], …, y[−N], the <b>initial conditions</b>. <b>Initial rest</b> means y[n] = 0 for n < 0. Under initial rest an LCCDE describes a causal LTI system.")),
 sec("Block diagram: adders, delays and multipliers",
  p("Three blocks build every LCCDE: an adder (Σ), a multiplier by a constant, and a unit delay, drawn as z⁻¹ (the symbol comes from Z-transform analysis; here it only means one sample of memory: input y[n], output y[n − 1]). <b>Direct form I</b> draws the input side and the output side separately and uses M + N delays. <b>Direct form II</b> shares one chain of delays between both sides and uses only max(N, M) delays, the least possible; both use N + M + 1 multipliers."),
  p("The figure draws worked example 2, y[n] = x[n] + 0.75y[n − 1] − 0.125y[n − 2]. The output passes through two delays; the taps are multiplied by −a_1 = 0.75 and −a_2 = −0.125 and fed back to the adder.")),
 sec("Closed form: natural plus forced response",
  p("<b>Natural response.</b> With the input set to zero, try y[n] = λⁿ. Dividing out λ^{n−N} gives the <b>characteristic equation</b>:"),
  F("λ^N + a_1λ^{N−1} + … + a_N = 0", "Its N roots λ_i (counting repeats) are the natural modes; without pole–zero cancellation they are the poles of the system."),
  p("Each distinct root gives a term C_iλ_i^n. A root repeated r times gives (C_0 + C_1n + … + C_{r−1}n^{r−1})λⁿ."),
  p("<b>Forced response.</b> Guess a form like the input: a constant for a constant input, A·2ⁿ for 2ⁿ, A cos ωn + B sin ωn for a sinusoid. If the guess is itself a natural mode (a constant input with λ = 1 a root, or 2ⁿ with λ = 2 a root), multiply the guess by n. Substitute and solve for the constants."),
  p("<b>Total response</b>: y[n] = y_{nat}[n] + y_{forced}[n] for n ≥ 0. Fix the N constants C_i from N known values, either y[−1], …, y[−N] or y[0], …, y[N − 1] found by iterating first.")),
 sec("Stability from the root positions",
  F("|λ_i| < 1 for every root ⟺ stable", "This is for a causal system; λ_i are the characteristic roots (poles) and |·| is the magnitude of a complex number."),
  table(['Root position', 'Mode λⁿ', 'Verdict'],
        [['|λ| < 1, inside', 'decays to 0', 'stable'],
         ['|λ| = 1, simple root', 'constant amplitude, may oscillate', 'marginally stable; not BIBO stable'],
         ['|λ| = 1, repeated root', 'grows like n', 'unstable'],
         ['|λ| > 1, outside', 'grows like |λ|ⁿ', 'unstable']]),
  p("A marginally stable system's own modes stay bounded, but an input at the mode's frequency makes the output grow: u[n] into y[n] = y[n − 1] + x[n] gives n + 1. A negative root such as −0.9 gives an alternating, slowly decaying mode.")),
],
'examples': [
 ex("A causal system is described by y[n] − 0.5y[n − 1] = x[n], with x[n] = u[n] and initial rest. (a) Iterate for n = 0 to 3. (b) Find the closed form. (c) Is the system stable?",
  ["Recursive form: y[n] = x[n] + 0.5y[n − 1]; here a_1 = −0.5, so the feedback multiplier is −a_1 = 0.5.",
   "Iteration: y[0] = 1 + 0.5(0) = 1; y[1] = 1 + 0.5(1) = 1.5; y[2] = 1 + 0.5(1.5) = 1.75; y[3] = 1 + 0.5(1.75) = 1.875.",
   "Characteristic equation λ − 0.5 = 0, root λ = 0.5; natural response C(0.5)ⁿ.",
   "Forced response: try a constant A (λ = 1 is not a root). A − 0.5A = 1 gives A = 2.",
   "Total y[n] = 2 + C(0.5)ⁿ. From y[0] = 1: 2 + C = 1, so C = −1, and y[n] = 2 − (0.5)ⁿ for n ≥ 0.",
   "Check: n = 3 gives 2 − 0.125 = 1.875, matching the iteration, and the same result as the convolution of u[n] with (0.5)ⁿu[n] in the previous chapter.",
   "The root 0.5 is inside the unit circle, so the system is stable and y[n] settles at 2."],
  "y[0..3] = 1, 1.5, 1.75, 1.875; y[n] = (2 − (0.5)ⁿ)u[n]; stable, final value 2.",
  dry=(['n', 'x[n]', 'y[n − 1]', 'y[n] = x[n] + 0.5y[n − 1]'], [['0', '1', '0', '1'], ['1', '1', '1', '1.5'], ['2', '1', '1.5', '1.75'], ['3', '1', '1.75', '1.875']])),
 ex("Find the impulse response of the causal system y[n] − 0.75y[n − 1] + 0.125y[n − 2] = x[n] in closed form, and check h[2] and h[3] by iteration.",
  ["Characteristic equation: λ² − 0.75λ + 0.125 = 0. λ = [0.75 ± √(0.5625 − 0.5)]/2 = (0.75 ± 0.25)/2, so λ_1 = 0.5 and λ_2 = 0.25.",
   "For n ≥ 1 the input δ[n] is zero, so h[n] = C_1(0.5)ⁿ + C_2(0.25)ⁿ, a form that also holds at n = 0.",
   "Starting values from the recursion with h[−1] = h[−2] = 0: h[0] = 1, h[1] = 0.75 × 1 = 0.75.",
   "n = 0: C_1 + C_2 = 1. n = 1: 0.5C_1 + 0.25C_2 = 0.75. Substituting C_2 = 1 − C_1: 0.25C_1 + 0.25 = 0.75, so C_1 = 2 and C_2 = −1.",
   "h[n] = [2(0.5)ⁿ − (0.25)ⁿ]u[n].",
   "Check by iteration: h[2] = 0.75(0.75) − 0.125(1) = 0.4375, and the formula gives 2(0.25) − 0.0625 = 0.4375. h[3] = 0.75(0.4375) − 0.125(0.75) = 0.234375; formula 2(0.125) − 0.015625 = 0.234375.",
   "Both roots are inside the unit circle, so the system is stable; Σh[n] = 2/(1 − 0.5) − 1/(1 − 0.25) = 4 − 1.333 = 2.667 = 1/(1 − 0.75 + 0.125), the DC gain."],
  "h[n] = [2(0.5)ⁿ − (0.25)ⁿ]u[n] = 1, 0.75, 0.4375, 0.234375, …; poles 0.5 and 0.25, stable.")],
'traps': [
 "Sign slip: y[n] + a_1y[n − 1] = x[n] becomes y[n] = −a_1y[n − 1] + x[n]. The feedback multiplier is −a_1.",
 "For y[n] − 0.5y[n − 1] = x[n] the characteristic equation is λ − 0.5 = 0. Writing 1 − 0.5λ = 0 gives the false root λ = 2 and a false 'unstable'.",
 "Guessing a constant forced response when λ = 1 is a root: the guess vanishes. Multiply it by n.",
 "Order versus input length: N counts output delays and M counts input delays; a second-order equation can have any number of b coefficients.",
 "Calling a simple root on the unit circle stable. It is only marginally stable, and an input at that frequency gives an output that grows without bound."],
'quiz': [
 Q('remember', 2, "Define the order of a difference equation.", "The order N is the largest delay of the output, y[n − N], in the equation. It is also the number of initial conditions needed."),
 Q('understand', 3, "Why is a non-recursive difference equation called FIR?", "With every a_k = 0 for k ≥ 1 nothing feeds back, so y[n] is a finite weighted sum of x[n], …, x[n − M], and h[n] = b_n lasts only M + 1 samples."),
 Q('apply', 4, "For y[n] = 0.5y[n − 1] + x[n] with x[n] = δ[n] and initial rest, find y[0], y[1], y[2] and the impulse response.", "y[0] = 1, y[1] = 0.5, y[2] = 0.25, so h[n] = (0.5)ⁿu[n], which decays: the system is stable."),
 Q('apply', 4, "A causal second-order system has roots λ = 0.8 and λ = −1.2. Is it stable?", "No. |−1.2| = 1.2 > 1, so the mode (−1.2)ⁿ grows with alternating sign. One root outside the unit circle is enough."),
 Q('analyze', 5, "A causal system has simple roots λ = +j and λ = −j. Describe its natural response and its stability.", "Both have magnitude 1, so the natural response is a pure oscillation of fixed amplitude at ω = π/2 (period 4 samples). It is marginally stable but not BIBO stable: an input at ω = π/2 makes the output grow."),
 Q('analyze', 4, "How many delays do direct form I and direct form II need for y[n] = 0.75y[n − 1] − 0.125y[n − 2] + x[n] + x[n − 1]?", "N = 2, M = 1. Direct form I needs M + N = 3 delays; direct form II needs max(2, 1) = 2. Both need N + M + 1 = 4 multipliers (b_0 = 1 can be a plain wire).")],
'beyond': "Real-time audio equalisers, pacemaker filters and echo cancellers run difference equations like these in fixed-point arithmetic, usually as cascades of second-order sections (biquads). Rounding the coefficients moves the poles, so designers check the pole radius after rounding. Search next: biquad, direct form II transposed, coefficient quantization."
}
ch = save(6, ch, old)
import sys; sys.path.insert(0, '../../pipeline'); import render as R; print(R.word_count(ch))
