# ec-antenna-u6: free-model run

- Book: `books/ece/ec-antenna/ec-antenna-u6.html`
- Status: ok
- Model calls so far: 32 (131,449 tokens in, 255,463 out), 7.1 minutes

## Checker

```
ec-antenna-u6.html: 9 chapters, 16793 words, 10 figures, 181 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 3, third paragraph (trade-off): The claim 'Lower bands also see more ground and weather clutter in the beam' is backwards. Rain backscatter and ground/vegetation clutter reflectivity both rise with frequency, which is exactly why S band is preferred for weather radar and why low bands penetrate foliage instead of being blinded by it. The only real low-band clutter penalty is the wider beam (larger illuminated patch) and anomalous propagation, not stronger clutter echoes.
- ch 1 [low] Section 2, bullet 'Modulator': In the classic pulsed radar built around a magnetron or klystron, the modulator is the high-voltage pulse generator that switches the transmitter tube on for τ. Calling it a former of a 'low-power pulse envelope' fits only an amplifier chain and can mislead a student asked to describe the modulator's job.
- ch 1 [low] Figure spec, node order and edges: The nodes are laid out vertically as Synchronizer → Modulator → Transmitter → Duplexer → Antenna → Receiver → Signal processor → Display, so the drawn chain suggests the antenna feeds the receiver directly. The receiver is reached only through the duplexer on receive.
- ch 2 [low] Section 2, and quiz Q5: Smin = kT0FB gives the receiver noise floor, not the minimum detectable signal. Standard texts define the minimum detectable signal as the noise floor multiplied by the signal-to-noise ratio needed for detection, Smin = kT0BF(S/N)min. As written, a student would answer Q5 with the noise power and call it minimum detectable signal, and the Rmax it produces is optimistic by 10log10(S/N)min dB in the noise budget.
- ch 2 [low] Section 3, figure text, Q2, Q4, Q7: Exponents are typed without <sup> in several places, so they render as ordinary digits: '1001/4 = 3.16', 'σ1/4', 'λ1/2', '(1/4)1/2 = 1/2', '(1/16)1/4 = 1/2', and 'Rmax = [PtAe²σ/(4πλ²SminL)]1/4'. A student reading '1001/4 = 3.16' sees a false arithmetic statement.
- ch 2 [low] Section 2 and Section 3: Section 2 introduces integration of n pulses and the gain from it, then Section 3 sets Pr/L = Smin and solves, with no n anywhere in Rmax. The reader is left unsure whether Smin is a single-pulse threshold or an integrated one.
- ch 2 [low] Section 1: 'Chapter 6.3 explains it' is plain text, so it will not link to the cross-section chapter in the phone reader.
- ch 3 [high] Quiz Q4: The answer labels ka = 6.28 as the optical region, but the chapter itself defines the optical region as ka ≫ 1 and the resonance/Mie region as ka around 1 to roughly 10. A sphere with ka = 6.28 (a = 0.1 m, λ = 0.1 m) sits at the upper end of the Mie/resonance region, not in the optical region. A student will memorise the wrong region boundary.
- ch 3 [low] Exam traps, second bullet: 'The same aircraft nose may be in the Rayleigh region on a VHF radar' is inaccurate: an aircraft nose of about 1 m at VHF (λ of the order of 1–10 m) has ka near 1 to a few, which is the resonance region, not Rayleigh. Rayleigh needs the scatterer to be much smaller than a wavelength.
- ch 4 [high] Section 2, range gating paragraph: The gate is called a sampling window in time, but its width is then given as cτ/2, which is a length in metres. A student will copy a time width in metres, or a range width in seconds, into the exam. The time width of one gate is τ; the range width it corresponds to is cτ/2.
- ch 4 [low] Section 1, first paragraph: 'The listening window is Tr = 1 / PRF' is loose: a part of the period, τ, is spent transmitting, so the receiver actually listens for Tr − τ, not for the whole of Tr. As written, a student may state in the exam that reception lasts the full period.
- ch 5 [high] Lead (opening paragraph): The lead lists the police speed gun as an FMCW application, but Section 1 and the CW/FMCW table both say a police speed gun is CW (it reads fd only). A student reading the lead will believe the speed gun measures range by sweeping.
- ch 5 [high] Section 3, applications paragraph: It says 'A tank level gauge is FMCW or CW: it measures the surface distance.' A CW radar cannot measure distance, which is the whole point of Section 1 and the table (CW: measures range = no). The sentence contradicts the chapter.
- ch 5 [low] Section 3, multiple tones paragraph: 'The range is unambiguous only over a short interval, set by the tone spacing' states no relation, so the student cannot tell whether a larger or smaller tone spacing helps.
- ch 6 [low] Lead: The lead calls the Doppler nulls 'blind speeds': 'zeros at Doppler frequencies called blind speeds'. A zero is a blind Doppler frequency; the blind speed is the target radial speed that produces it. Students then mix up the units (Hz against m/s).
- ch 6 [low] Lead and Section 3: The lead puts rain in the clutter list and then says clutter 'has no Doppler shift'. Rain moves with the wind and does give a Doppler shift; Section 3 itself mentions weather Doppler radar measuring rain motion. The two statements contradict each other.
- ch 6 [low] Section 1 and Section 3: The sentence on coherent versus noncoherent MTI appears twice, almost word for word, in Section 1 and again in Section 3. The repeat adds nothing and wastes phone-screen space.
- ch 6 [low] Section 1: 'MTI stores the video of one pulse' is vague about how much is stored. The canceller needs the previous pulse held for exactly one pulse repetition interval, not one pulse.
- ch 7 [high] Section 2, conical scan, third bullet: It says the conical-scan modulation 'sits close to Doppler frequencies'. A conical-scan rate is a few tens of hertz, while target Doppler shifts are kilohertz and above, so the two are nowhere near each other. A student will wrongly conclude that Doppler filtering removes the scan modulation.
- ch 7 [low] Section 3, sum and difference formulas: The formulas Δaz = (A + B) − (C + D) and Δel = (A + C) − (B + D) only work for one particular numbering of the four horns, and that numbering is never stated. A student using the common clockwise labelling (A top-left, B top-right, C bottom-left, D bottom-right) will get both difference channels wrong.
- ch 7 [low] Quiz Q7 answer: The answer says only that 'changing the scan rate only helps partly' and jumps to monopulse. The standard practical countermeasure is missing: a randomized or swept scan rate, and conical-scan-on-receive-only (COSRO), where the transmitter beam is fixed and only the receive beam scans, so a repeater jammer that copies the transmitted signal carries no scan modulation.
- ch 7 [low] Quiz Q1 answer: 'Boresight is the antenna axis of maximum gain' is loose for the tracking antennas in this chapter. On a monopulse antenna the boresight axis is where the squinted beams cross and the difference channel nulls, and on a conical-scan antenna it is the rotation axis; neither is a single-beam gain peak.
- ch 7 [low] Section 3, comparator sentence: The cross-reference to the waveguide-tee and coupler chapter is written as plain text ('see Unit 4, ...'), so it is not clickable on the phone.
- ch 8 [low] Section 2, paragraph on threshold and Pfa: The chapter defines two detectors (envelope gives |y(T)|, square-law gives |y(T)|²) but then gives only the linear-envelope false-alarm formula Pfa = exp(−VT²/(2σ²)). A student who squares the output may apply this formula to a power value and get the wrong answer.
- ch 8 [low] Figure, node 'env': The node is labelled 'Envelope detector' but its note says 'square law', which contradicts the text where the envelope detector and the square-law detector are two different devices.
- ch 8 [low] Figure, edge from 'mf' to 'env': The edge label is 'peak SNR 2E/N0', which is a performance figure, not the signal travelling on that wire. Students may read it as a voltage or power carried between blocks.
- ch 8 [low] Section 2, coherent integration: 'For equal pulses the SNR rises about N times' hedges an exact result; with ideal phase coherence and equal amplitudes the rise is exactly N.
- ch 8 [low] Section 3, cell-averaging CFAR definition: 'the cell under test (CUT) is the cell being tested' is circular and defines nothing for a reader meeting the term first.
- ch 8 [low] Section 2, Swerling models sentence: 'only name how target cross section fluctuates' understates the topic and reads oddly; the models are probability distributions used to compute Pd.
- ch 9 [high] Quiz Q2: The answer says the cosecant-squared pattern 'reduces gain at low elevation'. This is backwards. The pattern keeps high gain near the horizon and reduces gain at high elevation angles (short ranges). As written, the student learns the opposite of how the pattern works.
- ch 9 [high] Exam traps, cosecant-squared trap: 'It trades gain at low elevation for a more uniform echo' contradicts the main text, which correctly says gain falls above the horizon. The gain given up is at high elevation angles, not low ones.
- ch 9 [low] Section 1: 'A common search radar moves the feed, not the dish, to scan the beam' overgeneralises. Most simple 2D search radars rotate the whole antenna; feed movement is used in some sets, for example nodding-feed height finding on top of a rotating dish.
- ch 9 [low] Section 2: Pulse rise time and flat top are said to set 'the smallest usable range'. The minimum range is set mainly by the pulse width τ and the duplexer recovery time; rise time mainly affects the pulse spectrum and spectral splatter.
- ch 9 [low] Figure, signal processor node: CFAR appears in the figure but is never expanded anywhere in the chapter, so a student meeting the acronym for the first time cannot read it.
