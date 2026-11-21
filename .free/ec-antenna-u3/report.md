# ec-antenna-u3: free-model run

- Book: `books/ece/ec-antenna/ec-antenna-u3.html`
- Status: ok
- Model calls so far: 28 (102,970 tokens in, 263,059 out), 6.9 minutes

## Checker

```
ec-antenna-u3.html: 9 chapters, 15947 words, 10 figures, 164 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 1, two-source model: The path-difference sentence has the wrong sign for the phase shift that follows it. If element 2 is the one farther along +z (the usual setup, element 1 at the origin), then in a direction θ measured from the +z array axis the far-field point is closer to element 2, so element 2's wave travels d cosθ less, not more, than element 1's. Its phase therefore advances by +βd cosθ, which is what gives ψ = βd cosθ + α. As written, 'element 2 travels d cosθ farther' would give a lag βd cosθ, i.e. ψ = α − βd cosθ, contradicting the formula on the next line.
- ch 1 [low] Section 1, formula explanation: 'The power pattern is |AF|² = 4 cos²(ψ/2), normalized to 1' is unclear: 4 cos²(ψ/2) peaks at 4, so it is not normalized to 1.
- ch 1 [low] Section 2, naming: 'Array factorization' is not the usual alternative name; students may think it is a distinct standard term.
- ch 1 [low] Section 2, dipole example: 'Two half-wave dipoles with parallel axes, spaced along z' does not say whether the dipole axes are along z (collinear) or perpendicular to z (side-by-side). The next sentence, about the dipole null, only makes sense if the dipole axis is not the array axis.
- ch 1 [low] Quiz Q6: The answer stops at θ = 180° without noting that at α = π the pattern has two equal maxima, at θ = 0° and θ = 180° (AF = 2 at both endfires).
- ch 2 [high] Section 4: The statement 'Spacing of one wavelength or more creates grating lobes' is only true for broadside arrays. For end-fire arrays, grating lobes appear when d ≥ λ/2. A student may wrongly believe d = λ/2 is safe for end-fire.
- ch 2 [high] Exam traps, bullet 4: The trap says 'Spacing d ≥ λ creates grating lobes; d = λ/2 is the safe design value in most exam questions.' This is misleading for end-fire arrays, where d = λ/2 already produces a grating lobe at the back.
- ch 2 [high] Quiz Q6: The question 'Why is d ≥ λ avoided in a uniform linear array?' and its answer are incomplete. For end-fire arrays, d ≥ λ/2 already creates grating lobes, so the answer is wrong if applied generally.
- ch 2 [high] Section 3, end-fire example: The end-fire example with d = λ/2 and N = 4 omits that a full grating lobe exists at θ = 180° (ψ = −2π). A student may think d = λ/2 is safe for end-fire, which is false.
- ch 2 [low] Section 1, formula: The formula AF = sin(Nψ/2) / [N sin(ψ/2)] can be negative, but the figure plots positive values. The normalized array factor is conventionally the magnitude.
- ch 3 [high] Section 1, binomial array factor, and Quiz Q2 answer: The exponent is lost in the binomial array factor. Written as |cos(ψ/2)|N−1 it reads as |cos(ψ/2)| multiplied by (N−1), which is a different function and is not the binomial pattern.
- ch 3 [high] Exam traps, fourth trap (sidelobe dB and R): The formula "R = 10−SLLdB/20" has lost its exponent and reads as 10 minus SLLdB/20. A student following it literally gets R = 11 for a −20 dB sidelobe instead of R = 10.
- ch 3 [low] Quiz Q6 answer: The answer stays qualitative and never puts a number on the squint, so the student cannot check the calculation.
- ch 4 [low] Section 2: "The reflector is longer than resonance, so its current lags" never says what the current lags behind, and "longer than resonance" is loose (resonance is a frequency, not a length). A student can easily read it as "lags the driven element's current", which reverses the array-phase argument used two lines later. The same wording problem repeats for the directors ("their currents lead").
- ch 4 [low] Quiz Q8: The answer says the active-region dipoles are "about λ/4 apart". In the active region L ≈ λ/2, so the spacing is d = 2σL = σλ, which for the stated σ range (0.06 to 0.2) is about 0.06λ to 0.2λ — typically 0.15λ, well below λ/4. A student who plugs in 0.25λ gets 180° − 90° = 90° of phase, i.e. quadrature, and cannot see why the back lobe cancels.
- ch 4 [low] Section 1 (director list): Director spacing is given as "about 0.2λ to 0.4λ apart". Typical designs use roughly 0.15λ to 0.35λ; 0.4λ is at the edge and in long arrays raises sidelobes and back radiation instead of adding gain.
- ch 5 [low] Section 2, horn gain sentence: The text says 'Gain follows D = 4πAe/λ²'. The right-hand side is directivity, not gain. Gain equals directivity only when radiation efficiency is 100 %, and the chapter itself warns that aperture efficiency is not radiation efficiency, so a student can carry away the wrong formula.
- ch 5 [low] Section 3, field form of Babinet's principle: 'For the two cases, the fields add to the field with no screen at all' is the standard statement, but written without a caveat it reads as plain scalar addition of two fields of the same polarization. For electromagnetic screens the slot field has E and H interchanged relative to the dipole field, so the sum that equals the unscreened field is a vector sum with that rotated polarization.
- ch 5 [low] Quiz Q3, answer: 'D = 10 log1041.89 = 16.22 dBi' is ambiguous on a phone screen; the 10, the log and its argument run together and a student may read it as log of 1041.89.
- ch 5 [low] Section 2, cross-references: The prose says '(see Chapter 3.6)' and '(see Chapter 3.8)' as plain text, while the book's house style is to point to another chapter with a link.
- ch 6 [high] Section 3, sentence after the gain formulas: It says the factor (πD/λ)² is 'roughly the number of square wavelengths filling the dish mouth'. That is wrong by a factor of 4π ≈ 12.6. The physical mouth area is πD²/4, so the number of square wavelengths it holds is (πD²/4)/λ² = 0.785 (D/λ)², while (πD/λ)² = 9.87 (D/λ)². For the 3 m dish at 4 GHz the mouth holds about 1257 square wavelengths but (πD/λ)² = 15,791. A student who trusts this sentence will mis-size the aperture.
- ch 6 [low] Exam traps, first bullet: 'not at the centre of the dish surface' is confusing: the centre of the dish surface is the vertex, which is where the focus is measured from. As written it contradicts the first half of the sentence.
- ch 7 [low] Section 3 and quiz Q7: The text says a probe feed 'works well on thick substrates' and Q7 calls it 'better for a thick substrate', but neither mentions the drawback: on a 3 mm substrate the probe is a long vertical wire whose series inductance is significant. That inductance detunes the patch and narrows the match, which is why thick-substrate probe designs use an L-probe or a compensating capacitance.
- ch 7 [low] Section 1: It says the voltage is maximum at the two edges separated by L, but it does not say the two maxima have opposite polarity. A student can then wonder how two out-of-phase voltages radiate as a broadside pair. The point is that the equivalent radiating slots are in phase even though the edge voltages are opposite in sign.
- ch 8 [low] Lead and Section 2: The lead says the test antenna receives and its received power is compared with a standard gain horn, but Section 2 uses a different arrangement: the standard horn transmits first and then the test antenna transmits, with a separate fixed receive antenna. A student may think the two paragraphs describe different experiments.
- ch 8 [low] Section 1, far-field criterion: Only the largest dimension of the test antenna is mentioned. When the range antenna is large (a big reflector or horn), its own 2D²/λ also has to be satisfied, and R is the distance between the two antennas' phase centres.
- ch 8 [low] Section 1, cable loss sentence: "A long cable lowers received power" ignores the transmit side: in the transmit role a long cable lowers the power radiated by the antenna, which also shifts the reading.
- ch 8 [low] Section 3, crossed-dipole paragraph: The paragraph says equal amplitudes with a 90° phase difference give circular polarization but does not say that the sign of the 90° decides the sense (LHCP or RHCP). Students often miss this in the lab.
- ch 8 [low] Figure: The caption says "Notice the separation R between the two antennas", but the diagram labels no R, so the reader has nothing to notice.
- ch 8 [low] Beyond: Grammar: "Millimetre-wave and 5G testing often uses" does not agree with the plural subject, and "because there is no RF connector" is stated too loosely.
- ch 9 [high] Section 3 (radio horizon), also Q7: The chapter says refraction makes the radio horizon longer than the geometric horizon, then gives d ≈ 3.57√h. But 3.57√h is the geometric horizon for the true earth radius (√(2Rh) with R = 6371 km). A ray refracted over a 4/3 earth radius has the constant √(4/3) × 3.57 = 4.12. So the number contradicts the reason just given, and the 25 m example (17.9 km) and Q7 answer (17.85 km) are geometric, not radio, horizon values.
- ch 9 [low] Section 2 (skip distance): 'a ground wave may still cover the near field' misuses 'near field', which in antenna theory means the reactive/near field region close to the antenna, not the short-distance coverage before the skip zone. Also, the skip zone starts at the end of ground-wave range, which the text does not say (Q6 does).
