# ec-signals-u3: free-model run

- Book: `books/ece/ec-signals/ec-signals-u3.html`
- Status: ok
- Model calls so far: 24 (95,897 tokens in, 187,022 out), 4.7 minutes

## Checker

```
ec-signals-u3.html: 8 chapters, 12841 words, 9 figures, 155 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 3, after the properties table: The sentence says a time shift changes only phase 'exactly how a linear filter acts on a periodic input'. A general linear filter multiplies cₙ by H(jnω₀), so it can change both magnitude and phase; a time shift is only the all-pass special case H(jnω₀)=e^{-jnω₀t₀}.
- ch 1 [high] Worked example step 6: Even symmetry about t=0 does not by itself make even harmonics zero. It makes cₙ real and even (and bₙ=0). Here c₂, c₄, … vanish because the pulse is centered and high for exactly half the period, so sin(nπ/2)=0 for even n.
- ch 1 [high] Exam traps, first bullet: The scaling statement is wrong for the second mistake. Dropping 1/T₀ scales cₙ by T₀; using 2/T₀ instead of 1/T₀ scales cₙ by 2, not by T₀.
- ch 1 [high] Section 3, integration row of the properties table: The integration property cₙ/(jnω₀) for n≠0 requires x(t) to have zero average (c₀=0). If c₀≠0, ∫x(t)dt contains a ramp and is not periodic, so it has no Fourier series of this form. The text only mentions failure at n=0.
- ch 1 [low] Section 1, orthogonality formula: The cosine product formula leaves out n=m=0. For n=m=0 the integral is T₀, not T₀/2. The DC term must be handled separately.
- ch 2 [low] Section 1 prose, Section 2 table, Worked example 1 (steps 1–5), quiz answers Q3 and Q7: Exponents and integral limits are written flat, without superscript or subscript tags: "Σ c_n ejnω₀t", "e−2te−jωtdt", "∫0∞", "e−atu(t)", "e−j3ω". A student can read "e−2te−jωt" as "e minus 2t times e minus jωt" instead of e^(−2t)·e^(−jωt), and "e−atu(t)" is ambiguous.
- ch 2 [low] Quiz Q4 answer: "At ω=0, Sa(0)=1" is not strictly true: Sa(y)=sin y/y is undefined at y=0. Only its limit is 1.
- ch 2 [low] Section 3: "a short UPI confirmation burst needs more bandwidth than a steady carrier" compares a real pulse with a pure sinusoid. A steady carrier has exactly zero bandwidth, so the sentence invites the wrong picture that a carrier occupies some band.
- ch 2 [low] Section 1, inverse-transform formula note: The note says the 1/2π "converts an ω integral to an f integral". The factor is not a converter; it makes the ω-form inverse consistent with the forward transform, and in the f-form it is cancelled by dω=2πdf.
- ch 3 [low] Section 1, property table, and Sections 2–3 (all exponent expressions): Every exponential is written as plain running text, for example 'e−jωt₀X(ω)', 'ejω₀tx(t)', 'e−jω(u+τ)=e−jωue−jωτ'. On a phone this reads as e times jωt₀ times X(ω), not as e raised to a power. The transform definition in the same section does use <sup>, so the chapter is inconsistent with itself.
- ch 3 [low] Section 1, sentence before the table: 'Here a and b are constants, t₀ is a time shift in seconds, a is nonzero' states a twice, and the reader cannot tell whether the nonzero condition refers to the scaling constant a in x(at) or to something else.
- ch 3 [low] Worked example 1, step 7 and answer: X(0) is written as 0.019230769230769232 V·s, a machine-precision float. It suggests a precision the data does not have and is hard to read on a phone.
- ch 4 [low] Section 3, bandwidth sentence: The integral condition is garbled: it reads '0−BBESD(ω)dω = η(2πE)', which a student cannot parse as a definite integral from −B to B. The relation itself is correct, but the broken notation hides the limits and the meaning of the factor 2πE.
- ch 4 [low] Figure: The caption and aria text say the scaled two-sided area is the energy 1/6 J, but the plotted ω axis runs only from 0 to 10 rad/s. The area under the visible one-sided curve is half of that, 1/12 J, so the figure and its caption disagree, and this is exactly the one-sided/two-sided confusion warned about in exam trap 3.
- ch 4 [low] Worked example 1, step 1: The text is corrupted: 'for t0∞ e^{−6t}dt' loses the case t < 0 and the lower limit of the integral, so the step cannot be read as written.
- ch 5 [low] Section 3 and Exam traps (last bullet): The chapter states flatly that a low-pass has |H(0)|=1 and a high-pass has |H(0)|=0. The high-pass statement is fine (a high-pass must block DC), but |H(0)|=1 is only true for a low-pass whose passband gain has been normalised to 1. A general low-pass can have any DC gain, e.g. H(ω)=5/(1+jωRC) is still a low-pass with |H(0)|=5. A student may mark a correct filter wrong because its DC gain is not 1.
- ch 5 [low] Section 3, distortionless transmission sentence: Saying ∠H(ω) 'must be linear in ω' is incomplete. A straight line with a non-zero intercept (a constant phase offset added to every frequency) still distorts a real waveform. The correct condition is a straight line through the origin, ∠H(ω)=−ωt_d, where t_d is the delay in seconds.
- ch 5 [low] Section 1, sinusoidal steady-state formula: The input-output cosine rule is presented without saying that it gives the steady-state output only when the system is stable, i.e. when H(ω) exists. For an unstable system the transient never dies out and no steady-state sinusoid appears.
- ch 6 [high] Section 2, paragraph on consequences of the sinc: The sentence "h(t) is nonzero for t  0, so the filter is noncausal" has lost its inequality sign, so the key argument for noncausality cannot be read.
- ch 6 [high] Section 2, last sentence: It says ideal high-pass, band-pass and band-stop responses are "brick walls plus a δ(t) term". This is wrong for the ideal band-pass filter: its impulse response is (K/πt)(sin ω₂t − sin ω₁t), a difference of two sinc-type terms with no impulse at t = 0. The δ(t) term appears only where the response is 1 minus a low-pass (high-pass, band-stop).
- ch 6 [low] Worked example 1, output line: The four numbers 2.0, −1.0, 0.001, 1.0806 are shown without labels, and their order (magnitude, phase, delay, y(0)) does not follow the order of the steps. A reader cannot tell which number answers which part.
- ch 6 [low] Quiz Q6 answer: "Nonzero for every t < t_d" is too strong: the shifted sinc is zero at t = t_d − kπ/ω_c, so it is not nonzero at every point left of t_d. The conclusion is right, the wording is not.
- ch 6 [low] Section 3, Paley–Wiener statement: The rigorous Paley–Wiener condition for a causal, finite-energy impulse response is that the integral of |ln|H(ω)|| divided by (1 + ω²) is finite. The chapter states the unweighted integral, which is a stronger condition than the theorem. The zero-band divergence argument still works, but the statement as written is not the standard one.
- ch 7 [high] Worked example 1, step 1: The sentence defining x(t) is corrupted: "x(t)=0 for t−2t for t≥0" is unreadable, so the student cannot see the signal being transformed.
- ch 7 [high] Worked example 1, step 4: The text "For τx(−τ)=Rx(τ) for real x" is broken and loses the whole argument for negative lag; as printed it tells the student nothing about how Rx is found for τ<0.
- ch 7 [low] Section 2, power-signal paragraph: Saying flatly that the time-average autocorrelation of a power signal has a Fourier transform hides that this is a generalized transform: for a periodic signal Rx(τ) is periodic and Sx(ω) is a train of impulses, not an ordinary function.
- ch 8 [high] Section 1, definition and frequency response: The sentence is broken and runs two statements together: “The term sgn(ω) is the signum function: +1 for ω>0, 0 at ω=0, and −1 for ωH(ω)|=1 for every ω≠0.” The rest of the signum definition and the magnitude statement have been lost, so the student reads meaningless text (“−1 for ωH(ω)|=1”) and never sees the magnitude response stated properly.
- ch 8 [low] Section 1, Section 2, worked example steps 3–4, exam traps, Q1 and Q4 (notation): The frequency response is printed as “HH(ω)” everywhere (and “|HH|”, “|HH(ω)|=1”). The subscript of H has been flattened, so it reads like the product of two functions called H, which is confusing next to the input spectrum X(ω).
