# ec-comm-u4: free-model run

- Book: `work/ec-comm-u4/tree/books/ece/ec-comm/ec-comm-u4.html`
- Status: ok
- Model calls so far: 22 (80,434 tokens in, 171,524 out), 5.9 minutes

## Checker

```
ec-comm-u4.html: 8 chapters, 20706 words, 11 figures, 300 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 1, theorem and sample rate: It says an ideal lowpass filter from 0 to fm recovers M(f) exactly, but the sampled spectrum carries a factor fs, so a filter with unit gain would give fs·M(f), not M(f). The cutoff also need not be exactly fm; any cutoff between fm and fs − fm works.
- ch 1 [low] Section 3, reconstruction and aperture effect (and Quiz Q6): The hold is fixed at Ts and the response given as Ts sinc(fTs), but Q6 says a shorter hold reduces the aperture effect. In flat-top PAM the hold lasts a pulse width τ ≤ Ts and the response is τ sinc(fτ); the chapter does not define τ, so the two statements look contradictory to a student.
- ch 1 [low] Section 3, reconstruction and aperture effect: "PAM circuits use both names" is unclear — it does not say which two things are named.
- ch 1 [low] Quiz Q7: The comparison "Nyquist rate = 3600 > 3000" has no units, so the rate and the sampling rate are compared as bare numbers.
- ch 1 [low] Beyond: It sends the reader to search for bandpass sampling, which Section 3 has already introduced, so the pointer reads as if the topic were new.
- ch 2 [high] Section 2, PPM paragraph: "The leading edge may be fixed and the trailing edge shifted, or the reverse" describes PWM, not PPM. In PPM the width stays fixed and the whole narrow pulse slides in time.
- ch 2 [high] Section 2, PPM generation, and Quiz Q5: An edge detector giving "one short pulse per PWM edge" produces two pulses per PWM period, so the pulse rate doubles and the modulation is not the standard PPM. PPM has one pulse per sampling period.
- ch 2 [low] Lead paragraph: "This keeps the pulse timing fixed" contradicts PPM, where the pulse position is the message.
- ch 2 [low] Section 1, PAM spectrum formula: The formula P_PAM(f) = (1/Ts) Σ M(f − n fs)·P(f) with P(f) = Aτ sinc(fτ) is the flat-top (sample-and-hold) PAM result. It is stated as the general PAM spectrum even though natural PAM was just defined.
- ch 2 [low] Worked example 1 and Quiz Q3/Q7: Powers of ten appear as plain digits: "8×103 Hz", "125×10−6 s", "10×103". Read literally these are wrong values (8×103 = 824), which confuses a phone reader.
- ch 2 [low] Section 2, last sentence: "Some syllabi call PPM pulse-position modulation and PWM pulse-duration modulation" repeats names already defined one paragraph earlier (PDM was introduced as the same thing as PWM).
- ch 3 [low] Lead: The lead says uniform steps 'waste resolution on quiet passages and clip loud peaks'. This attributes clipping to uniform spacing itself, hinting that non-uniform quantization or companding avoids clipping. Section 3 and exam trap 3 say the opposite: any quantizer clips once the input passes ±V.
- ch 3 [low] Figure caption: The caption calls the straight line y = x 'the uniform quantizer'. A uniform quantizer's transfer characteristic is a staircase of L steps, not a straight line; the line only shows the no-companding (identity) reference.
- ch 5 [high] Section 1 ('Predict, subtract, encode'): The letter n is used twice with two different meanings. It is the time index in x[n], e[n], x̂[n], and it is also the number of bits per sample in 'an n-bit code word' and in the bit rate 'fs·n'. A student will read fs·n as 'sampling frequency times the time index'. The sampling frequency fs is also never defined.
- ch 5 [high] Figure: The adder output is labelled x̂[n], but the adder output is the reconstructed sample x̃[n]. The predictor note 'x̂[n−1]' is also wrong: the predictor input is the reconstructed sample x̃[n−1] and its output is the prediction x̂[n]. This contradicts the x̂/x̃ notation used everywhere in the text.
- ch 5 [low] Figure: The diagram shows one predictor fed from the receiver-side adder, with dashed edges crossing back to the transmitter subtractor. The text says the transmitter needs its own local decoder and predictor, but the figure does not show it, so the reader may think the prediction physically travels back over the channel.
- ch 5 [low] Section 2, last paragraph: 'The dashed feedback path in the figure is the reason DPCM stays stable' points at the wrong edges: the dashed edges carry the prediction, while the reconstructed sample travels on the solid edge from the adder to the predictor.
- ch 6 [low] Section 1, describing the staircase update: Saying x̂(t) 'moves one step of Δ volts toward the input' suggests the staircase always closes the gap exactly. If the input is above x̂ by less than Δ, a 1 makes the staircase overshoot the input and the next bit steps it back down. That overshoot-and-return is exactly the granular noise discussed later, so the sentence can mislead a student about how the estimate settles.
- ch 7 [high] Section 3, paragraph on timing error: The sentence says that if the receiver samples late it may read the tail of the previous slot or the start of the next slot. This contradicts the quiz Q4 answer and is technically wrong: a late sample drifts forward into the start of the next slot, while reading the tail of the previous slot happens when the sample is early.
- ch 7 [low] Section 3, paragraph on sync loss: 'Frame slip' is used for a one-slot misalignment that swaps channel 1 into channel 2. In standard telephony a frame slip means a whole frame is lost or repeated because the receiver clock drifts from the incoming clock.
- ch 7 [low] Section 3, first paragraph: 'A sync bit in every frame is enough for four channels' is an unsupported claim; the risk of false locking depends on the data pattern and sync pattern, not on the number of channels being four.
- ch 7 [low] Section 2, last paragraph: 'Some syllabi write TDM(A) for that access method' reads as if the abbreviation is TDM(A); the intended term is TDMA.
- ch 7 [low] Exam traps, last bullet: '125×10-6 s' has no superscript, so a student can read it as 125 times minus six seconds.
- ch 8 [high] Section 3, clock recovery and choice: The sentence 'That is why Manchester is used where the clock must survive AC coupling and polarity inversion' implies plain Manchester is tolerant of polarity inversion. It is not: swapping the two wires inverts every bit under plain Manchester. Only differential Manchester (and NRZ-I) carry data in transitions and so survive a swapped pair. A student can carry this into an exam and write that Manchester is immune to polarity reversal.
- ch 8 [low] Section 2, spectra and first nulls, PSD formula: The formula is written 'pNRZ(f) = V2 Tb sinc2(f Tb)'. The superscripts are missing, so 'V2' reads as V times 2 and 'sinc2' as sinc times 2. Everywhere else in the chapter the ² symbol is used correctly.
- ch 8 [low] Worked example 1, step 6 and answer: Step 6 says Manchester is DC-free and self-clocking as if it were the only such code. Polar RZ is also DC-free when bits are equally likely (its PSD is a sinc² with no line at DC) and it puts a transition in every bit period, as Section 3 itself says. The question does not state bit statistics, so a careful student can answer 'polar RZ' and be marked wrong.
- ch 8 [low] Section 3, last paragraph: 'NRZ is best for bandwidth but needs scrambling or framing to avoid long runs. RZ sits between them.' The phrase 'sits between them' is unclear and, on bandwidth, wrong: RZ needs about twice the bandwidth of NRZ, the same order as Manchester. Its only middle position is in clock content, not width.
- ch 8 [low] Figure table, RZ row: The RZ cells are written '+0' and '−0'. The symbol 0 here means the zero-volt level, not the bit 0, and the table gives no key, so a reader can mistake '−0' for a minus sign followed by the bit value zero.

## Correction pass (Claude, 21 Nov 2026)

- Every reviewer note fixed ([high] first); every chapter rewritten from the draft, every example, trap, quiz and bank answer recomputed by script.
- Second worked examples added in every chapter; eight figures hand-drawn from the chapter examples (pipeline/claude_figs/ec_comm_u4.py).
- 14 full model answers; cross-unit references named by topic; MIT links dropped.
