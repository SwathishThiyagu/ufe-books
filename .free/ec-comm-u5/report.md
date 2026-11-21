# ec-comm-u5: free-model run

- Book: `books/ece/ec-comm/ec-comm-u5.html`
- Status: ok
- Model calls so far: 23 (103,434 tokens in, 222,862 out), 7.2 minutes

## Checker

```
ec-comm-u5.html: 7 chapters, 14381 words, 8 figures, 150 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Quiz Q5: The stated reason is wrong. An ideal rectangular NRZ pulse of width T is 1 only for |t| < T/2 and is already 0 at t = ±T, ±2T, …, so it does satisfy p(nT) = 0 for n ≠ 0 at the sampling instants. It does not fail Nyquist's first criterion; it fails because its spectrum T·sinc(fT) has unbounded width, so no finite-bandwidth channel can pass it without spreading. The answer's claim that 'p(±T) is not zero and neighbours spill fully into each sample' contradicts the definition and will teach the wrong idea.
- ch 1 [low] Figure: The series names do not match the plotted data. The curve named a₋₁ p(t−T) peaks at t/T = 3 and the curve named a₀ p(t−2T) peaks at t/T = 4, but p(t−T) peaks at t/T = 1 and p(t−2T) peaks at t/T = 2. A student checking the labels against the axis will be confused.
- ch 1 [low] Quiz Q6: The expression 'each contributes p(0.05T) plus p((k−n)T + 0.05T) terms' mixes up two things: p(0.05T) is the wanted pulse sampled slightly off its peak, not a neighbour's contribution. The final line 'peak distortion rises from 0' is also loose: for the untruncated sinc the timing-error ISI sum Σ δ/(n+δ) diverges, so in theory peak distortion becomes unbounded; only truncation keeps it finite in practice.
- ch 2 [high] Section 1: The text says a DSL line on α = 0.25 pays 12.5 % extra bandwidth. Excess bandwidth is αR_s/2, which is 25 % of the Nyquist minimum R_s/2, not 12.5 %.
- ch 2 [high] Section 2: Two technical errors. (i) 'At every t = kT ... the denominator is not [zero]' is false: for α = 0.5 and k = ±1 the denominator 1 − (2αk)² is zero. (ii) 'At t = ±T/(2α) ... the limit there is π/4' is wrong for the pulse: the limit is (π/4) sinc(1/(2α)), not π/4.
- ch 2 [high] Section 3, eye-pattern bullets: The slope-at-zero-crossing bullet is backwards. A steep crossing makes the horizontal eye opening wider and increases tolerance to timing jitter; a gradual crossing narrows it.
- ch 2 [low] Figure caption: The caption says 'no single block is a raised cosine by itself', but the figure includes a block labelled 'Overall p(t) raised cosine'. This can confuse a reader.
- ch 3 [high] Section 3 (LMS), repeated in the figure and in the Exam traps: The error is defined as e(n) = d(n) − â(n), where â(n) is called the decided output symbol. But the same section says decision-directed mode uses the receiver's own decision as d(n). If d(n) = â(n), then e(n) = 0 and the weights never update. A student following the text literally gets no adaptation in decision-directed mode.
- ch 3 [low] Figure box (spec): The error box note says 'd(n) − â(n)', which carries the same contradiction as Section 3: in decision-directed mode d(n) is the decision â(n).
- ch 3 [low] Worked example 1, step 1: The index and time notations are mixed: y(n) = c0x(n) + c1x(n−T), while everywhere else the stored sample is written x(n−k) with an integer lag k.
- ch 3 [low] Section 1, first paragraph: The pointer to the Nyquist condition is written as plain text '5.1' with no cross-reference link, so on a phone the reader cannot jump to it.
- ch 4 [high] Exam traps, fifth trap: The trap says that when the axes change 'only the numbers attached to the signals stay the same'. The coordinates are exactly the numbers that do change: swap the order of s₁ and s₂ in the worked example and s₂ becomes (√2, 0) instead of (1, 1). A student will carry away the opposite of what Section 2 just proved.
- ch 4 [high] Quiz Q7: The answer calls identical or antipodal signals 'the worst case for a detector, since the two points are as far apart, or as close, as the geometry allows'. Identical signals (correlation +E) sit at distance 0 and cannot be told apart — that is the worst case. Antipodal signals (correlation −E) sit at the largest possible distance 2√E — that is the best case, not the worst. The two cases cannot be given one verdict.
- ch 4 [low] Worked example 1, step 1, step 4 and the answer line: The axes are written as plain numbers: 'φ₁ = s₁/‖s₁‖ is 1 V over the whole interval', and 'φ₂ … is +1 over the first half and −1 over the second'. An axis does not carry volts; in these units it carries 1/√ms, so its amplitude is 1/√ms, not 1 V. The chapter's own trap about dropping units is broken here.
- ch 4 [low] Section 3, matched filter paragraph: 'For a fixed received energy, ⟨r, s⟩ is largest when the reference s has exactly the incoming shape, and the largest value is ‖r‖‖s‖.' Fixing only the received energy does not bound ⟨r, s⟩ — the reference energy ‖s‖² must also be fixed, otherwise the quantity grows without limit. The inequality is not yet usable as written.
- ch 5 [low] Section 1, noise variance formula: The output noise variance is written as σ² = (N₀/2)∫₀ᵀ h²(τ)dτ. For a general filter the integral must run over every τ where h(τ) is nonzero; a filter impulse response longer than T would give more output noise than this formula predicts. The 0-to-T limits are valid only because the matched filter is confined to the pulse interval.
- ch 5 [low] Section 1, last paragraph: "The filter folds the pulse about T" is loose and can mislead. With h(t) = s(T − t) the reflection is about t = T/2; what the sentence describes is a time reversal followed by a delay of T.
- ch 5 [low] Worked example 1, step 1: The unit check "V²·s = W·s = J" is true only when the voltage is taken across a 1 Ω reference. Strictly V²·s = W·Ω·s, so the jump to joules is not dimensionally clean as written.
- ch 6 [low] Figure: The node notes on s₁ and s₂ are '0' and 'E'. That reads as the two points 0 and √E_s, which have unequal energy. The caption then says the minimum-distance rule decides s₂, but the chapter itself states (exam trap 4) that nearest-point equals ML only for equal energies. The figure as labelled contradicts the rule it is meant to illustrate.
- ch 6 [low] Section 1: "The terms ||r||² and 1/N₀ are common" is loose: ||r||² is a term inside the squared distance, while 1/N₀ is a common positive factor outside the exponent. A student can read this as 1/N₀ being a term of the expansion.
- ch 7 [high] Section 2 (modified duobinary and its cost), the noise-margin paragraph: The sentence 'For the same transmitted power, the adjacent levels are closer than in binary, so the error probability roughly doubles' draws the wrong conclusion from its own premise. Closer levels at the same average power raise the error probability by a large factor (exponentially at high SNR), not by roughly two. The 'factor of two' figure only belongs to a same-spacing comparison (three levels with two thresholds give about 4/3 the binary symbol-error count), which is a different situation. A student will carry away 'duobinary costs about 3 dB', which is wrong.
- ch 7 [low] Section 3 (M-ary PAM), the energy paragraph: 'If you keep the same gap d and double the bits per symbol, the energy rises by (M² − 1)/3 compared with binary' mixes two ideas. 'Double the bits per symbol' fixes M = 4, where the factor is 5, while the formula is general in M; also 'rises by' should be 'rises by a factor of', otherwise it reads as a difference, not a ratio.
- ch 7 [low] Section 1 (duobinary precoder): The recursive precoder pₖ = bₖ ⊕ pₖ₋₁ is stated without a starting value, so pₖ is undefined for the first bit and a student cannot run the coder by hand.
