# ec-optical-u5: free-model run

- Book: `books/ece/ec-optical/ec-optical-u5.html`
- Status: ok
- Model calls so far: 16 (58,667 tokens in, 131,724 out), 5.5 minutes

## Checker

```
ec-optical-u5.html: 5 chapters, 10283 words, 6 figures, 112 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 3, definition of modulation index m: The phrase 'peak swing of the optical power divided by its mean value' can be read as the full peak-to-peak swing, which would make m twice as large as intended. The rest of the chapter (signal current mI/√2, signal power (mI)²/2) assumes m is the peak deviation from the mean, so a student who reads 'peak swing' as peak-to-peak will get the wrong formula.
- ch 1 [low] Worked example 1, step 6: 'CNR = 6.125 ÷ 2.5 × 10⁻⁵' reads left to right as 6.125 ÷ 2.5 × 10⁻⁵ = 2.45 × 10⁻⁵ under normal precedence, which contradicts the stated answer 2.45 × 10⁵. The10⁻⁵ belongs in the denominator.
- ch 2 [low] quiz, Q4: The arithmetic is right, but the answer stops at 'the budget closes' and never applies the chapter's own overload rule. With P_T = −3 dBm and only 3.5 dB of physical loss, the received power is −6.5 dBm. For an 850 nm short link that is close to, or beyond, the overload point of many receivers, so a student may accept a design that fails from too much power.
- ch 2 [low] Lead: 'The link power budget is a single addition' reads as if there is one term. The budget is a sum of several terms (fiber, connectors, splices, margin, penalty), and a student skimming the lead may take away the wrong picture.
- ch 3 [low] Section 1 formula box, worked example step 1, exam trap 4: Powers of ten are printed as plain digits: "1/(1 × 109) s", "Tb = 1/B is the bit period in ps" and "multiply by 1012 for ps". As printed, 1 × 109 reads as one hundred nine, so the shown equalities look wrong to a student.
- ch 3 [low] quiz Q2 answer: "their standard deviations add as squares" is wrong wording: it is the squares of the standard deviations (the variances) that add; the standard deviations themselves add in quadrature.
- ch 3 [low] Section 1, second paragraph: The symbol Tr is defined as the 10–90% rise time and then never used; the budget formula uses Ttx, Tfiber and Trx instead, which can make a student hunt for a missing term.
- ch 4 [high] Worked example 1, step 7: It calls 0.6991 dB/km 'a fair value for good single-mode fiber at 1550 nm'. Standard single-mode fiber at 1550 nm loses about 0.19–0.22 dB/km. 0.70 dB/km is three times too high for good fiber at that window, so the sentence teaches a wrong benchmark.
- ch 4 [high] Worked example 2 (and quiz Q5), opening line: It says 'The same fiber on an OTDR: group delay reads 500.0 ps at 1548 nm…'. An OTDR measures backscatter loss against distance; it does not measure group delay against wavelength, so it cannot give dispersion. The instrument named belongs to another method.
- ch 4 [high] Worked example 2, step 1–2 (and quiz Q5): 500.0 ps is presented as the group delay through 10 km of fiber. The true delay is about L·n_g/c ≈ 10⁴ m × 1.47 ÷ (3 × 10⁸ m/s) ≈ 49 μs, a hundred thousand times larger. Only a delay difference can be a few hundred picoseconds.
- ch 4 [low] Worked example 2 answer, and quiz Q5: D = 0.17 ps/(nm·km) at 1550 nm is the value for dispersion-shifted fiber, not the standard single-mode fiber implied by Worked example 1, which would give about 17 ps/(nm·km). Calling it 'the same fiber' confuses two different fiber types.
- ch 4 [low] Section 2, first reading of the trace: 'The slope of the straight part is α in dB/km' hides the round trip. Rayleigh backscatter travels out and back, so the raw trace falls at 2α per km; only after the instrument halves it does the slope equal the one-way α. A student may then treat a raw dB difference between markers as one-way loss (as in quiz Q4).
- ch 4 [low] Exam traps, unit-mixing bullet: 'A value like 17 ps/nm for a whole spool is not the coefficient' is muddled: for a 1 km spool the total 17 ps/nm and the coefficient 17 ps/(nm·km) have the same number, so the example does not show the confusion it means to show.
- ch 5 [high] Section 1, the sentence starting 'A short wavelength has a wider mode field': The physics is backwards. The mode field widens as wavelength increases; at short wavelengths the mode is tighter and better confined (bend loss of the fundamental grows with wavelength). The looped trace drops at short wavelengths because below cutoff a weakly confined higher-order mode (LP11) is still guided and the bend strips it, not because short wavelengths are weakly confined.
- ch 5 [low] Section 1, 'Launch the same broad-spectrum source into two samples': Two separate samples of fiber are not comparable; the straight and looped traces must come from the same fiber, otherwise the difference reflects fiber-to-fiber variation.
- ch 5 [low] Section 1, cutoff criterion: The text tells the student to report the loop diameter but never gives the standard value, so the student cannot tell whether a reported diameter is normal.
- ch 5 [low] Quiz Q2, answer: 'Above cutoff the core guides the fundamental mode' suggests the fundamental is not guided below cutoff, which is wrong; it is guided on both sides of cutoff.
- ch 5 [low] Section 1, 'The index profile gives the same value': The far-field 5% value and the profile value agree only approximately; the far-field NA usually comes out a little larger because of launch and mode-excitation effects. 'The same value' reads as exact equality.
