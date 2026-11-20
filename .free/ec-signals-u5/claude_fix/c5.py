import json
from u import *
old = json.load(open('ch5.json'))
A6 = '<a href="#linear-constant-coefficient-difference-equations">linear constant-coefficient difference equations</a>'
ch = {
'lead': "A discrete-time system turns one sequence into another. If it is linear and time-invariant (LTI), a single sequence describes it completely: its <b>impulse response</b> h[n]. The output for any input x[n] is then the <b>convolution sum</b> of x[n] and h[n], the discrete twin of the convolution integral. Phone audio filters, ECG smoothing and moving averages on sensor data all run this sum sample by sample.",
'prereq': "You need: the samples x[n] = x(nT_s) from <a href=\"#sampling-theorem-and-reconstruction-of-signals\">sampling theorem and reconstruction</a>; δ[n], u[n] and the system properties (see System properties: linearity, time invariance, causality, stability); and the convolution integral it mirrors (see Convolution integral and its evaluation).",
'sections': [
 sec("Sequences, impulse and step",
  p("A <b>discrete-time signal</b> is a sequence x[n], defined only at integer n. A sequence is periodic if x[n + N] = x[n] for every n; the smallest such positive integer N is its period. A <b>discrete-time system</b> maps an input sequence x[n] to an output y[n]; it is LTI when it obeys superposition and a delayed input gives an equally delayed output."),
  p("The <b>unit impulse</b> is δ[n] = 1 at n = 0 and 0 elsewhere. The <b>unit step</b> is u[n] = 1 for n ≥ 0 and 0 for n < 0. They are related by δ[n] = u[n] − u[n − 1]. Any sequence is a sum of shifted, scaled impulses, the sum running over all integers k:"),
  F("x[n] = Σ_{k=−∞}^{∞} x[k] δ[n − k]", "Here x[k] is the value of the input at index k, and δ[n − k] is an impulse placed at n = k."),
  p("The <b>impulse response</b> h[n] is the output when the input is δ[n] and the system starts at rest. By time invariance, δ[n − k] gives h[n − k]; by linearity, x[k]δ[n − k] gives x[k]h[n − k]; adding over k gives the output.")),
 sec("The convolution sum and how to evaluate it",
  F("y[n] = Σ_{k=−∞}^{∞} x[k] h[n − k]", "Here y[n] is the output at index n, x[k] the input at index k, h[n − k] the impulse response flipped and shifted by n, and k the summation index. Swapping the roles gives the same result: y[n] = Σ h[k] x[n − k]."),
  p("For finite sequences only the overlapping terms are nonzero. If x[n] has N₁ samples and h[n] has N₂ samples, y[n] has N₁ + N₂ − 1 samples, starting at the sum of the two start indices."),
  steps("Flip and slide: draw x[k]; draw h[−k], the impulse response flipped about k = 0.",
        "Shift the flipped sequence right by n to get h[n − k]. Multiply the overlapping samples and add: that sum is y[n].",
        "Increase n by one and repeat until the sequences no longer overlap.",
        "Table check: write x along the top and h down the side, fill each cell with the product, and add along the anti-diagonals; the sums are y[0], y[1], …."),
  p("For an infinite h[n] such as aⁿu[n], the same sum is a geometric series; a finite series from 0 to n has the closed form (1 − a^{n+1})/(1 − a).")),
 sec("Properties, causality, stability and frequency response",
  bullets("Commutative: x[n] * h[n] = h[n] * x[n].",
          "Associative: (x * h₁) * h₂ = x * (h₁ * h₂), so two systems in cascade act like one with h₁ * h₂.",
          "Distributive: x * (h₁ + h₂) = x * h₁ + x * h₂, so two systems in parallel add their impulse responses.",
          "Identity: x[n] * δ[n] = x[n], and x[n] * δ[n − m] = x[n − m], a delay of m samples."),
  p("An LTI system is <b>causal</b> exactly when h[n] = 0 for n < 0: the output then uses only present and past inputs. It is <b>BIBO stable</b> exactly when Σ|h[n]| over all n is finite; every bounded input then gives a bounded output. The <b>step response</b> is the running sum s[n] = Σ_{k=−∞}^{n} h[k]."),
  F("H(e^{jω}) = Σ_{n=−∞}^{∞} h[n] e^{−jωn}", "Here H(e^{jω}) is the frequency response, ω the frequency in radians per sample and j = √−1. The sum converges when Σ|h[n]| is finite, so every stable system has one. For the input e^{jωn}, the output is H(e^{jω}) e^{jωn}: the magnitude of H is the gain and its angle the phase shift at ω. It is studied fully under the discrete-time Fourier transform.")),
],
'examples': [
 ex("For x[n] = [2, 1, 3] at n = 0, 1, 2 and h[n] = [1, 2] at n = 0, 1, use y[n] = Σ x[k]h[n − k] to find y[n]. Then test h[n] = (0.5)ⁿu[n] for causality and BIBO stability.",
  ["Nonzero samples: x[0] = 2, x[1] = 1, x[2] = 3; h[0] = 1, h[1] = 2. Output length N₁ + N₂ − 1 = 3 + 2 − 1 = 4, from n = 0 to 3.",
   "y[0] = x[0]h[0] = 2·1 = 2.",
   "y[1] = x[0]h[1] + x[1]h[0] = 2·2 + 1·1 = 4 + 1 = 5.",
   "y[2] = x[1]h[1] + x[2]h[0] = 1·2 + 3·1 = 2 + 3 = 5.",
   "y[3] = x[2]h[1] = 3·2 = 6.",
   "Check: the sum of y equals (sum of x)(sum of h): 2 + 5 + 5 + 6 = 18 = (2 + 1 + 3)(1 + 2) = 6 × 3.",
   "h[n] = (0.5)ⁿu[n] is zero for n < 0, so the system is causal. Σ|h[n]| = 1 + 0.5 + 0.25 + … = 1/(1 − 0.5) = 2, finite, so it is BIBO stable."],
  "y[n] = [2, 5, 5, 6] for n = 0 to 3; the system h[n] = (0.5)ⁿu[n] is causal and BIBO stable (Σ|h[n]| = 2).",
  dry=(['n', 'terms x[k]h[n − k]', 'y[n]'], [['0', '2·1', '2'], ['1', '2·2 + 1·1', '5'], ['2', '1·2 + 3·1', '5'], ['3', '3·2', '6']])),
 ex("Find the step response of the system h[n] = (0.5)ⁿu[n]: y[n] = u[n] * h[n]. Give y[0] to y[3] and the final value.",
  ["For n < 0 the flipped step u[n − k] does not overlap h[k], so y[n] = 0.",
   "For n ≥ 0: y[n] = Σ_{k=0}^{n} (0.5)^k u[n − k] = Σ_{k=0}^{n} (0.5)^k, because u[n − k] = 1 for k ≤ n.",
   "Finite geometric series: y[n] = (1 − 0.5^{n+1})/(1 − 0.5) = 2(1 − 0.5^{n+1}) = 2 − (0.5)ⁿ.",
   "y[0] = 2 − 1 = 1; y[1] = 2 − 0.5 = 1.5; y[2] = 2 − 0.25 = 1.75; y[3] = 2 − 0.125 = 1.875.",
   "As n grows, (0.5)ⁿ → 0, so y[n] → 2, which equals Σ h[n], the DC gain."],
  "y[n] = (2 − (0.5)ⁿ)u[n]: 1, 1.5, 1.75, 1.875, … settling at 2. The next chapter gets the same answer from a difference equation.")],
'traps': [
 "Not flipping h: sliding h[k] instead of h[n − k] gives the correlation, not the convolution.",
 "Losing the first or last output sample. A finite result has N₁ + N₂ − 1 samples; check also that the sum of y equals the product of the sums of x and h.",
 "Mixing up n and k: n is the output index you want; k is the dummy index you sum over.",
 "Testing stability from the first few terms of h[n]. The whole sum Σ|h[n]| must be finite: u[n] has bounded terms but an infinite sum.",
 "Confusing h[n] (a sequence in n) with H(e^{jω}) (a function of ω)."],
'quiz': [
 Q('remember', 2, "Define the impulse response of a discrete-time LTI system.", "The output h[n] when the input is δ[n] and the system is initially at rest."),
 Q('understand', 3, "Why does h[n] describe an LTI system completely?", "Any input is a sum of shifted, scaled impulses x[k]δ[n − k]. Time invariance turns each into x[k]h[n − k], and linearity adds them, so the output depends only on x and h."),
 Q('apply', 4, "x[n] = [1, 2] and h[n] = [1, 1, 1], both starting at n = 0. Find y[n].", "y[0] = 1·1 = 1; y[1] = 1·1 + 2·1 = 3; y[2] = 1·1 + 2·1 = 3; y[3] = 2·1 = 2. So y[n] = [1, 3, 3, 2]; check 9 = 3 × 3."),
 Q('analyze', 4, "Is the system h[n] = (0.9)ⁿu[n] BIBO stable? Justify.", "Yes. Σ|h[n]| = Σ (0.9)ⁿ = 1/(1 − 0.9) = 10, which is finite."),
 Q('apply', 3, "x[n] = δ[n − 2] passes through h[n] = [1, −1, 2] starting at n = 0. Find y[n].", "Convolving with δ[n − 2] delays by 2: y[n] = h[n − 2] = [0, 0, 1, −1, 2] for n = 0 to 4."),
 Q('understand', 2, "What condition on h[n] makes a discrete-time LTI system causal?", "h[n] = 0 for every n < 0."),
 Q('analyze', 5, "For h[n] = u[n] (an accumulator), state whether the system is causal and BIBO stable.", "Causal, because h[n] = 0 for n < 0. Not stable: Σ|h[n]| = 1 + 1 + 1 + … diverges, and the bounded input u[n] gives y[n] = n + 1, which grows without limit."),
 Q('apply', 3, "Write H(e^{jω}) for h[n] = [1, 2] at n = 0, 1, and find the gain at ω = 0 and ω = π.", "H(e^{jω}) = 1 + 2e^{−jω}. At ω = 0: 1 + 2 = 3. At ω = π: 1 − 2 = −1, a gain of magnitude 1.")],
'beyond': "In industry the convolution sum runs as FIR filtering in audio, radio, ECG cleanup and image blurring. Long filters are computed with the FFT, block by block, by the overlap-add or overlap-save method. Search next: FIR filter, circular convolution, overlap-add."
}
ch = save(5, ch, old)
import sys; sys.path.insert(0, '../../pipeline'); import render as R; print(R.word_count(ch))
