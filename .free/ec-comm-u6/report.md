# ec-comm-u6: free-model run

- Book: `books/ece/ec-comm/ec-comm-u6.html`
- Status: ok
- Model calls so far: 25 (96,265 tokens in, 290,556 out), 7.5 minutes

## Checker

```
ec-comm-u6.html: 9 chapters, 16023 words, 10 figures, 171 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Worked example 1, step 6 and answer: The step says the tones are orthogonal because 10 kHz is greater than the 5 kHz minimum. A spacing larger than Rb/2 is not automatically orthogonal; coherent orthogonality needs spacing = nRb/2 for a positive integer n. Here 10 kHz = 2 x 5 kHz, so it is orthogonal, but the reason given is wrong and a student could apply it to a non-orthogonal spacing such as 7.5 kHz.
- ch 1 [high] Exam traps, third bullet: It says coherent tones need at least Rb/2 spacing and noncoherent tones need Rb. This is the same false test: any spacing above the minimum is not necessarily orthogonal. The exact conditions are spacing = nRb/2 for coherent and spacing = nRb for noncoherent, with positive integer n.
- ch 1 [low] Lead and Section 1 opening: The lead and section opening equate ASK with OOK. OOK is only the special case of binary ASK where the 0 bit has zero amplitude; binary ASK can use two nonzero amplitudes.
- ch 2 [low] Section 2, correlator formula: The text says y, the test statistic, is 'in volts'. It cannot be: r(t) is in volts and the reference waveform √(2/Tb)cos(2πfct) has units of 1/√s, so the integral carries units of V·√s (equivalently √joules with a 1 Ω reference). A student who checks dimensions will be confused, and the same symbol y is later compared against zero as if it were a voltage.
- ch 2 [low] Section 3, bandwidth sentence: With rectangular (NRZ) pulses the power spectral density of BPSK is sinc-squared shaped, not sinc shaped; the sinc shape describes the amplitude spectrum. Saying 'sinc-shaped band' can leave a student with the wrong picture of the PSD.
- ch 2 [low] Section 2, after the correlator formula: The noise term n is introduced but its statistics are never given, although every later result (the Q(·) expression) depends on them. A student cannot see where N0/2 enters the argument.
- ch 3 [low] Section 1, non-coherent OOK paragraph: The text says the BFSK error form applies 'with Eb the energy of the on burst'. The standard result is quoted with Eb as the average received energy per bit; the on burst carries twice that. With Eb taken as the on-burst energy the exponent must be Eb/(4N0), so the stated form overstates the OOK performance by 3 dB in energy.
- ch 3 [low] Section 2, first sentence: The sentence 'Some syllabi call DPSK differential phase shift keying' repeats the expansion already given in the previous sentence and adds no information; a student may look for a second meaning that does not exist.
- ch 3 [low] Section 2, DPSK error formula: Pb = ½ exp(−Eb/N0) is labelled 'a high-SNR approximation'. For binary DPSK in AWGN with an ideal one-bit delay this is the exact closed-form result, not an approximation.
- ch 3 [low] Section 3, opening line: The sentence announces 'The three non-coherent options', but the list has four bullets: the fourth is coherent BPSK, which is not a non-coherent option.
- ch 4 [high] Figure: The constellation labels contradict the bipolar mapping used earlier. Node A says I=+1,Q=+1 but is labelled 00; since bit 1 is +1 and bit 0 is −1, that point must be 11. Node C says I=−1,Q=−1 but is labelled 11; it must be 00.
- ch 4 [high] Section 3: The statement 'Doubling M halves the bandwidth per bit' is wrong. Doubling M adds one bit per symbol, so bandwidth per bit changes from 2/k to 2/(k+1); the ratio is k/(k+1), not 1/2.
- ch 4 [high] Section 2: A recovered-carrier phase error does not add a fixed offset to both decisions. It rotates the received constellation relative to the decision axes, so each decision contains a fraction of the other bit plus noise.
- ch 4 [low] Section 3: 'Only M=2^k with k=2,3,4,... is useful' excludes BPSK, which is M=2 (k=1) and is a useful PSK system.
- ch 4 [low] Section 1: The bullet 'bit 1 is +1 V and bit 0 is −1 V' gives I and Q units of volts, but the formula has A in volts multiplying dimensionless I and Q, so A·I would have units V².
- ch 5 [high] Section 2, bandwidth sentences: The chapter says 'With rectangular pulses, the baseband bandwidth is R_s / 2' and then 'the passband null-to-null bandwidth is B = 2R_s'. These two statements do not match each other. Rectangular (NRZ) pulses have a sinc² spectrum whose first baseband null is at R_s, so the baseband null-to-null bandwidth is R_s; the passband null-to-null value is then 2R_s. The value R_s / 2 is the Nyquist minimum baseband bandwidth, which needs ideal sinc pulses, not rectangular pulses.
- ch 5 [high] Exam traps, trap 5: The trap says that if a student uses the baseband value R_s / 2 as the passband null-to-null bandwidth, the efficiency comes out as k instead of k / 2. The arithmetic is wrong: R_b /(R_s / 2) = kR_s /(R_s / 2) = 2k, not k. For 16-QAM the wrong answer is 8 bps/Hz, not 4 bps/Hz.
- ch 5 [low] Section 2, modulator steps (step 5): The step says 'Subtract the Q product from the I product and transmit the sum'. Subtracting and then transmitting 'the sum' contradicts the signal formula s(t) = I cos − Q sin given just above, and a student may copy the wrong sign.
- ch 5 [low] Section 2, first paragraph: The sentence 'Some syllabi call QAM quadrature amplitude modulation' repeats the expansion already given in the previous sentence, so it adds nothing and reads like filler.
- ch 6 [low] Lead: "two frequencies that are only half a bit rate apart" is loose wording; a phone reader may read it as half of Rb or as half a hertz.
- ch 6 [low] Section 2, coherent detection: "samples at the bit instants" hides that in the I/Q form each rail holds its symbol for 2Tb, so each rail is sampled every 2Tb, with the two rails offset by Tb.
- ch 6 [low] Section 3: "The filter does not increase the data rate by itself" is a negative remark that does not tell the student anything positive and can be misread as a claim about throughput.
- ch 6 [low] Exam trap 1: The trap warns against h = 1 but does not say what h = 1 actually gives, so the student cannot check the mistake.
- ch 6 [low] Section 3: The Gaussian filter's impulse response width is mentioned as "longer" but no link is made to how far a bit spreads; a reader cannot judge the size of the effect.
- ch 7 [high] Exam traps, third bullet: The claim "16-QAM at the same E_s as QPSK has 6 dB less energy per bit, since E_s = 4E_b" is wrong. At the same E_s, QPSK gives E_b = E_s/2 and 16-QAM gives E_b = E_s/4, so 16-QAM has only half the energy per bit, i.e. 3 dB less than QPSK, not 6 dB. The 6 dB figure is the comparison against BPSK (E_s = E_b), not QPSK.
- ch 7 [low] Figure and its caption: The caption says the nearest-neighbour spacing shrinks as more points are packed into the same energy, but all three constellations are drawn on the same scale, so the spacing is 2 in every case (BPSK ±1, QPSK (±1, ±1), 16-QAM levels ±1, ±3). The average energies actually plotted are 1, 2 and 10, so the picture does not show what the caption claims.
- ch 7 [low] Section 4, power bill sentence: "About 4 dB at each step" is accurate for QPSK to 16-QAM (4/1.6 = 2.5, i.e. 4 dB) but the second step is 1.6/0.57 = 2.8, which is 4.5 dB.
- ch 8 [low] Exam traps, second bullet: The sentence "Processing gains add in dB. Do not add linear ratios and then convert unless you are multiplying them" contradicts itself. Cascaded linear gains multiply, they never add, so the "unless" clause is meaningless and a student may add linear gains.
- ch 8 [low] Section 2, jamming margin definition: Calling the jamming margin "the extra jammer power the link can tolerate" is vague. It does not say extra relative to what, or that the link must still meet the required E_b/N_0, so a student may give the answer in watts.
- ch 8 [low] Section 3: Processing gain is defined only through the chip-rate formula G_p = R_c/R_b, which is a DSSS formula. The FHSS part never states its processing gain, so a student may wrongly apply the chip-rate formula to a frequency-hopping system.
- ch 9 [low] Section 1, formula block: The 'where' list defines N (number of subcarriers) but N does not appear in the formula Δf = 1/T_u, so the definition hangs unused and a student may wonder where N belongs.
- ch 9 [low] Section 1, first paragraph: 'A high-rate single carrier over a multipath channel has a symbol time shorter than the delay spread' reads like a fixed law. It is a condition that holds only once the rate is high enough for the given channel.
- ch 9 [low] Section 2, after the Y[k] formula: 'After the cyclic prefix is removed, the channel acts as a circular convolution' can be read as if the physical channel were circular. The channel is linear; it is the received useful block that equals a circular convolution of x[n] with the channel impulse response, and only because the CP is long enough.
- ch 9 [low] Section 3, Doppler sentence: f_d = v f_c / c is the maximum Doppler shift, not the Doppler spread. Calling it the Doppler spread is loose and can confuse the definition of coherence time.
- ch 9 [low] Section 3 and Exam traps (CP rule): 'The rule is T_cp > τ_max' and 'The CP must be longer than τ_max' are slightly too strict. A CP exactly equal to the delay spread already keeps all echoes inside the prefix, so a student could wrongly mark T_cp = τ_max as a failure.
