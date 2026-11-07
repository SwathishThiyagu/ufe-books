# c-cn-u2: free-model run

- Book: `books/cse/c-cn/c-cn-u2.html`
- Status: ok
- Model calls so far: 54 (240,672 tokens in, 378,536 out), 12.5 minutes

## Checker

```
c-cn-u2.html: 8 chapters, 13954 words, 9 figures, 173 KB
OK
```

## For the reviewer

- chapter 4: the figure cannot be drawn: tree is too wide (6 leaves); use fewer leaves or shorter labels
- chapter 4: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [low] Lead vs Section 1: The lead says three numbers describe a sine wave completely (amplitude, frequency, phase), but Section 1 says 'Four numbers describe a sine wave' and lists amplitude, period, frequency, phase. Period and frequency are not independent (T = 1/f), so a careful student sees a contradiction.
- ch 1 [low] Lead: 'every UPI payment that rides on one' suggests a UPI payment travels on a 64 kbit/s PCM voice channel. UPI runs over packet data, not over a voice channel, and data is not PCM-coded the way speech is.
- ch 1 [low] Exam traps, fifth bullet: The trap says 'Reading period = 0.2 s and writing frequency = 0.2 Hz', but nowhere is 0.2 s a period. In the worked example 0.2 s is the time for 50 cycles, and the error a student would actually make there is f = 1 ÷ 0.2 s = 5 Hz, not 0.2 Hz.
- ch 2 [low] Section 1 (after the dBm formula) and Worked example 1: The definition dB = 10 log₁₀(P₂/P₁) makes a loss negative, and the text says so (−3 dB halves power). But the link-sum sentence and the worked example quote loss as a positive number ('30 dB loss', 'Total loss = 15 dB') and divide by 10^(15/10). A student may not see whether to write −15 dB or +15 dB, and whether to divide or multiply.
- ch 2 [low] Section 2, SNR paragraph: 'Shannon capacity uses it directly' comes straight after SNRdB = 10 log₁₀(S/N), so 'it' can be read as the dB value. Shannon's formula needs the linear power ratio, and a student who substitutes dB gets a wrong capacity.
- ch 2 [low] Section 1, the 20 log₁₀ formula: The where-line does not state that the 20 log₁₀ form for voltage or current holds only when the resistance is the same at both points (so that P is proportional to V²). Across a mismatched interface the two forms disagree.
- ch 2 [low] Section 2, distortion paragraph: Distortion is described only as components arriving out of step (delay distortion). The other form, where different frequencies are attenuated by different amounts so the shape changes even with no delay spread, is not named; some syllabi call it attenuation distortion.
- ch 3 [high] worked example 1, step 6 and answer; quiz Q6: The rounding direction is wrong and contradicts Section 3, which says L = √(1+S/N) is the largest number of levels that still reaches the Shannon limit. L = √3163.3 ≈ 56.24 levels. Rounding up to 57 gives a Nyquist rate of 2 × 3000 × log₂57 ≈ 35.0 kbit/s, which is above the Shannon capacity of 34.9 kbit/s, so it is not reliable. The chapter also says elsewhere 'about 56 levels is the useful ceiling', so the example answers disagree with the text.
- ch 3 [low] section 1: The sentence 'Doubling L adds only one bit per sample when L doubles' repeats itself and reads awkwardly.
- ch 3 [low] quiz Q6: The question writes 'SNR = 35 dB'. SNR alone names a power ratio; 35 dB is the decibel form, so the symbol is ambiguous for a student.
- ch 4 [high] Section 3, satellite microwave: The chapter says the geostationary satellite delay is 'about a quarter of a second each way'. The quarter second is the one-way delay for the whole path ground → satellite → ground (about 36,000 km up plus 36,000 km down at 3 × 10⁸ m/s), so 'each way' doubles the true figure and a student will quote 0.5 s one way or 1 s round trip.
- ch 4 [low] Table, Radio and microwave row, Bandwidth column: The bandwidth is listed as 'kHz to GHz bands', but the chapter itself puts microwaves up to 300 GHz, so the table understates the top of the range and contradicts Section 3.
- ch 4 [low] Section 2, fibre joins: Only SC and ST connectors are named. LC is the connector on almost every modern patch panel and SFP module, so a student may not recognise it.
- ch 5 [low] Section 2, NRZ-I paragraph: The sentence "the first bit sets the starting level" is confusing and does not match the worked example, which needs a level before the first bit (+1 V) to produce any output at all. A student may think the first bit always determines the level in the same way.
- ch 5 [low] Section 2, RZ paragraph: "RZ returns to 0 V in the second half of every bit. It gives a transition for every 1" describes unipolar RZ only. In polar RZ a 0 is sent as −V then 0 V, so every bit, 1 or 0, has a mid-bit transition. As written, a student will over-generalise the rule to all RZ.
- ch 5 [low] Section 2, unipolar NRZ paragraph: "No transition during a run of 0s" is incomplete: a run of 1s also gives no transition in unipolar NRZ, since the level stays at +V.
- ch 5 [low] Figure: The NRZ-I trace starts at −1 without saying why. The reader cannot tell that this comes from a chosen level of +1 V before the first bit, so the figure and the worked example seem to disagree on the starting point.
- ch 6 [high] Section 4, PSK paragraph: "a 180° error is the farthest apart two points can be" is garbled: a student reads "180° error" as the error event itself, when the point being made is that the two BPSK symbols sit 180° apart, the largest possible separation.
- ch 6 [low] Section 1, third reason: Sharing one medium on different carriers is frequency-division multiplexing (FDM), not frequency reuse. Frequency reuse in standard usage means reusing the same band in different cells or beams.
- ch 6 [low] Section 4, ASK paragraph: "it survives where noise is low, as in short optical links" gives the wrong reason and understates optical links. Optical fibre uses on-off keying because the source is switched on and off (intensity modulation) and direct detection is cheap, not because only short links have low noise.
- ch 6 [low] Worked example 1: "A QAM-16 modem on the same link" clashes with the numbers: a link only 2 kHz wide cannot carry 2400 symbols per second (Nyquist needs at least 2400 Hz). The two parts of the example contradict each other.
- ch 6 [low] Quiz, Q1–Q7: The marks are printed twice for every question, once in the header, e.g. "Q1 (remember, 2 marks)", and again at the end, "(2 marks)".
- ch 6 [low] Figure spec, demodulator node: The note "carrier out" can be read as "the carrier comes out", the opposite of what the figure text says (the demodulator takes the carrier back out).
- ch 7 [high] Exam traps, last bullet: The direction of the wavelength–frequency relation is inverted. Since f = c/λ, a smaller wavelength gap Δλ gives a smaller frequency gap: Δf ≈ (c/λ²)·Δλ. Closer wavelengths therefore mean narrower bands in Hz, not wider ones. A student who memorises 'closer wavelengths = wider bands in Hz' will get the conversion backwards.
- ch 7 [low] Section 3, paragraph after the table: The sentence 'Statistical TDM divides time but not fairly, which is why it needs addresses' gives a wrong cause. Addresses are needed because slot position no longer identifies the user when slots are handed out on demand, not because the sharing is unfair.
- ch 7 [low] Section 1, analog telephone hierarchy sentence: The text says 12 channels of 4 kHz fill a 48 kHz group with no guard bands, while the formula above says bandwidth = ΣBi + (n − 1)·Bguard. A student can read this as a contradiction.
- ch 8 [high] Section 3 (frequency hopping), fast hopping sentence: It says the receiver must track the schedule "chip by chip". Chips belong to DSSS; an FHSS signal has hops, not chips. A student will carry the DSSS chip idea into FHSS and think FHSS also multiplies data by a chip code.
- ch 8 [low] Section 1, last two sentences: The sentence "Only a few universities teach this topic in depth" is repeated word for word from the lead, and the application list (GPS, Wi-Fi, Bluetooth, military) is also repeated from the lead. Two nearly identical sentences in a short chapter waste the reader's attention.
- ch 8 [low] Worked example 1, part (b) and step 4: The answer "about 11 times stronger" does not say what the interferer's power is measured over. The jamming margin only holds when the interferer's power falls inside the spread band the receiver despreads; a student may read it as 11 times the signal power at any single frequency.
- ch 8 [low] Quiz Q2: The answer is too thin for 3 marks and only gives half the reason. Coherent addition explains why the wanted signal survives, but not why it can sit below the noise floor: the despreader also narrows the noise bandwidth by the processing gain.
- ch 8 [low] Beyond: "5G and Wi-Fi combine spreading ideas with OFDM and adaptive coding" is loose. Modern Wi-Fi (OFDM modes) and 5G NR are not spread-spectrum air interfaces; only the older DSSS mode of Wi-Fi spreads.
