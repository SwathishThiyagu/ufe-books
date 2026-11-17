# ec-signals-u5: free-model run

- Book: `books/ece/ec-signals/ec-signals-u5.html`
- Status: ok
- Model calls so far: 18 (73,759 tokens in, 184,568 out), 4.6 minutes

## Checker

```
ec-signals-u5.html: 6 chapters, 10724 words, 7 figures, 124 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Quiz Q1: The question asks for a definition of Nyquist rate and Nyquist frequency, but the answer only substitutes numbers from one example. A student who memorises this answer cannot define the two terms; the numbers happen to be right, but the definition asked for is missing.
- ch 1 [low] Section 1: The text says samples are taken at n = 0, 1, 2, ..., but the impulse-train and interpolation sums in Sections 2 and 3 run over all integers, including negative n. The two statements disagree.
- ch 1 [low] Section 1 and exam trap 1: 'fs/2 is the Nyquist frequency, the highest frequency a sampler at fs can represent' contradicts the chapter's own correct statement that a sinusoid exactly at fs/2 (i.e. at f_max when fs = 2 f_max) loses its amplitude and phase. Likewise the trap wording 'they are not the same number' ignores the case fs = 2 f_max, where the two numbers are equal.
- ch 2 [high] Exam traps, guard band vs transition width bullet: This contradicts Section 3. Section 3 defines the transition width as Δf = f_s/2 − f_max, which is exactly the guard band. The bullet says they are equal only when f_c = f_s/2.
- ch 2 [high] Section 3, cutoff choice sentence: The statement that setting f_c = 2 f_max is wrong is too strong. It is wrong only when 2 f_max > f_s/2. If 2 f_max ≤ f_s/2, it is a legal cutoff below the Nyquist frequency, though it may pass more out-of-band noise.
- ch 2 [low] Section 1, spectral copies overlap: The sentence about the copy centred at f_s reaching down to f_s − f_max is only true for f_s/2 < f_max < f_s. For f_max > f_s, such as 1300 Hz at f_s = 1000 Hz, f_s − f_max is negative and is not inside the positive baseband; the alias comes from a different copy.
- ch 2 [low] Exam traps, alias amplitude bullet: The statement that the alias keeps the amplitude is true for an isolated cosine but not for a general signal. Multiple components can fold onto the same frequency and add or cancel, changing the amplitude.
- ch 3 [high] Section 2, aperture effect explanation: The text says multiplication in time by the hold rectangle becomes convolution in frequency, then gives H(f)=τ sinc(fτ). The zero-order hold is convolution in time with the rectangle, so the spectrum is multiplied by the rectangle's Fourier transform, a sinc. The stated operation is the wrong one and will confuse students.
- ch 3 [high] Quiz Q4 answer: As written the answer has lost inequality signs and the m=5 lower-edge check: '8 kHz  7 kHz' is not a valid test, so the quiz answer does not actually show why no integer m fits.
- ch 3 [low] Worked example 1, step 8: A filter passing 0-1 kHz is a low-pass filter, not normally called band-pass. Saying 'band-pass filter centred on the 0-1 kHz image' can confuse.
- ch 3 [low] Figure: The text defines normalized aperture magnitude as |sinc(fτ)|, but the plotted expression is the signed sinc. It goes negative after 4 kHz while y min is 0, so the negative part is clipped and the figure does not show the stated magnitude.
- ch 4 [low] Lead: The lead says quantization error is 'the difference between the true sample and the rounded value', i.e. true minus rounded, while Section 2 defines e_q = Q(x) − x, rounded minus true. A student can carry the wrong sign into an exam answer.
- ch 4 [low] Section 1: The formula Δ = (x_max − x_min)/L silently assumes the mid-rise convention, where L steps of width Δ exactly tile the range. For the mid-tread case mentioned in the same section (a level at zero, and levels at both x_min and x_max as well), the spacing would be (x_max − x_min)/(L − 1), so the single formula contradicts the second quantizer type.
- ch 4 [low] Worked example 1, step 4: 'the distances are 0.9 V to 2.5 V and 0.1 V to 3.5 V' reads like a range from 0.9 V to 2.5 V instead of a distance between two values.
- ch 4 [low] Section 2 (companding sentence): 'giving small signals finer relative resolution' mixes two ideas. Log companding gives small signals finer steps in volts (more levels at low amplitude), so their SQNR comes close to that of large signals; the relative step Δ/x is roughly constant over a wide range, not 'finer' at small amplitudes.
- ch 4 [low] Figure spec: The plotted expression floor(x) + 0.5 evaluated at x = 8 V gives 8.5 V, which lies outside the stated 0 V to 8 V output axis. If the plotting engine samples the whole domain, a point above the axis appears.
- ch 5 [low] Section 1 and Section 3 (summation signs): Several summation signs have no limits, so students cannot tell whether the sum runs over all n or only a range: "x[n] = Σk x[k] δ[n − k]" in Section 1 and "s[n] = Σk=−∞n h[k]" in Section 3. In the second one the upper limit n is not raised, so it reads like multiplication.
- ch 5 [low] Worked example 1 (steps 7–8) and quiz Q4, Q8: Exponents are not marked, so (0.5)nu[n], (0.9)n, ejωn, H(ejω) and e−jω can be read as plain multiplication by n. In step 7 this makes h[n] look like 0.5·n·u[n], which diverges, contradicting the stability answer in step 8.
- ch 5 [low] Quiz Q3, answer: The answer lists only the sums y[1] = 1 + 2 = 3 and y[2] = 1 + 2 = 3. The two terms are not identified, so a student cannot see which product comes from which index and cannot check the working.
- ch 5 [low] Section 3, frequency response formula: The chapter defines H(ejω) without saying when this sum converges. Students may plug in h[n] = u[n] and conclude the frequency response exists, though that system is not BIBO stable.
- ch 6 [low] Section 1, paragraph on recursion and IIR: The text says that if at least one a_k is nonzero the impulse response lasts forever, so the system is IIR. A recursive equation can still have a finite impulse response when a pole cancels a zero (for example y[n] = x[n] − 0.5x[n−1] + 0.5y[n−1] has h[n] = δ[n]). The absolute statement will be marked wrong by a strict examiner.
- ch 6 [low] Section 2, block diagram paragraph: The sentence mixes two realisations. It claims N delays, one adder and up to N + M + 1 multipliers. The count N + M + 1 multipliers with a single adder belongs to direct form II, which needs max(N, M) delays, not N. Direct form I needs N + M delays and two adders. Section 1 also says the number of unit delays in the hardware equals N, which fails when M > N.
- ch 6 [low] Section 3, forced response: The rule 'a constant input gives a constant guess A' fails when the input has the same form as a natural mode, for example a constant input when λ = 1 is a root, or an input 2ⁿ when λ = 2 is a root. Substituting the guess then gives 0 = 1 and the student is stuck.
- ch 6 [low] Section 3, natural and repeated-root sentences: The prose drops the subscripts and superscripts, so terms read as 'Ciλin', 'Cr−1nr−1' and 'multiplying by λN'. A student can read these as products of separate letters instead of C_i times λ_i to the power n.
- ch 6 [low] Section 1, opening of the standard form: The sentence says that writing every output on the left and every input on the right gives the standard form, but the formula displayed already has y[n] alone on the left with the feedback terms moved to the right. The words describe one arrangement and the formula shows another.
