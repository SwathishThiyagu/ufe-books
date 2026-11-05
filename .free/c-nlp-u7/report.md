# c-nlp-u7: free-model run

- Book: `books/cse/c-nlp/c-nlp-u7.html`
- Status: ok
- Model calls so far: 27 (104,638 tokens in, 215,482 out), 5.7 minutes

## Checker

```
c-nlp-u7.html: 8 chapters, 14418 words, 9 figures, 155 KB
OK
```

## For the reviewer

- chapter 2: the figure cannot be drawn: tree is too wide (6 leaves); use fewer leaves or shorter labels

## Reviewer notes (after any revision)

- ch 1 [high] Quiz Q6: The question says the student's statement 'F0 = 16000 Hz' contains two separate mistakes, but the statement holds only one: 16000 Hz is the sampling rate, not F0 (a male F0 is about 100–150 Hz). The answer key's second point, that F0 is not the frame rate, does not follow: nothing in the student's claim confuses F0 with frame rate, and the frame rate here is 100 frames/s, not 16000. A student marking their own answer would look for a second mistake that is not there.
- ch 1 [high] Section 1: The text places unvoiced noise at the vocal folds: 'the folds stay apart and air rushes through a narrow gap, making noise', then gives the hiss in /s/ and /f/ as examples. For /s/ and /f/ the folds are apart but the turbulence is made at a constriction in the mouth (tongue near the alveolar ridge for /s/, lower lip against the upper teeth for /f/), not between the folds. A student will conclude that all unvoiced excitation is generated at the glottis, which is wrong for fricatives.
- ch 1 [low] Section 1: 'It leaves through the lips' contradicts the nasal branch mentioned in the same paragraph; for nasal sounds the air leaves through the nose.
- ch 2 [high] Quiz Q7 answer: The answer says English 'pin' and 'spin' differ in the following vowel. They do not: both have the same vowel /ɪ/ ([pʰɪn] and [spɪn]). The claim is false and a student would carry away a wrong test for phonemicity.
- ch 2 [low] Section 1, place list (retroflex): Retroflex is described as curling the tongue tip back 'to the hard palate', which is the same place given for palatal in the next-but-one line. Students will not see how ट and ட differ from /j/.
- ch 2 [low] Section 1, place list (palato-alveolar): 'Tongue blade near the hard palate' is too vague and overlaps with the palatal description, so /ʃ/ and /j/ look like the same place.
- ch 2 [low] Section 4, syllable example 'speaks': The nucleus is written /i/, but the vowel of 'speaks' is long, /iː/. The short /i/ is a different (though near) vowel and the symbol is wrong.
- ch 3 [low] Section 3: The zero-crossing-rate formula uses sgn(x[n]) without ever defining it, so a student meeting it first here has to guess that sgn is the sign function (+1, 0 or −1). The sum limits are also left out, and it is not said that the average is over the N−1 neighbouring sample pairs inside the frame.
- ch 3 [low] Section 2: The text says the stack of magnitudes |Xm[k]| 'is the short-time Fourier transform'. The STFT itself is complex-valued (it keeps phase); the magnitude, usually squared, is the spectrogram. The wording blurs a distinction examiners test.
- ch 3 [low] Section 3 (autocorrelation paragraph): R(τ) is maximised at τ = 0 and falls off as τ grows simply because fewer samples overlap and the window tapers the frame ends. Taking the plain argmax over the whole allowed range can therefore return a multiple of the true pitch period (2T, 3T), and the 'largest value' rule is biased towards short lags.
- ch 4 [high] Section 3 (mel scale): The sentence 'Below 1000 Hz the curve is nearly straight: a 100 Hz step is about a 100 mel step' contradicts the chapter's own formula, figure data and worked example. The formula gives 100 Hz = 150 mel, 200 Hz = 283 mel, 300 Hz = 402 mel, and near 1 kHz the step falls to about 68 mel per 100 Hz. A student who takes 'about 100 mel per 100 Hz' will answer 300 Hz = 300 mel instead of 402 mel.
- ch 4 [low] Section 2 and Quiz Q7: The Bark value is called a 'band index' in Q7 and 300 Hz is said to 'fall in band 3'. With z ≈ f/100, 300 Hz gives z = 3.0, which is the boundary between the third and fourth critical band, not a clean position inside band 3. Also, Bark is a continuous scale (critical band rate) just like mel, not a count of whole bands, so the Q7 contrast 'Bark counts bands while mel measures perceived pitch' misleads.
- ch 4 [low] Section 3 (mel scale): 'Each doubling of frequency adds only a few hundred mel' understates the figure. With mel = 2595 × log₁₀(1 + f/700), an octave well above 700 Hz adds 2595 × log₁₀2 ≈ 781 mel (1000→2000 Hz adds 521 mel, 4000→8000 Hz adds 694 mel).
- ch 5 [low] Section 1, first paragraph: The sentence repeats itself: 'The most common set is the mel-frequency cepstral coefficient (MFCC); some syllabi call it the mel-frequency cepstral coefficient.' The second clause says exactly the same thing as the first, so the student gets no new information and may think a distinction is being made.
- ch 5 [low] Section 3 table, GSM full rate row: GSM full rate is labelled 'hybrid CELP'. GSM full rate (13 kbps) actually uses RPE-LTP, regular-pulse excitation with long-term prediction. It is a hybrid analysis-by-synthesis coder like CELP, but it has no excitation codebook, so calling it CELP contradicts the standard description.
- ch 5 [low] Section 2, formula box: The section introduces deltas and delta-deltas but the only formula shown is the cepstral-mean-normalisation one. The reader is told a delta is the slope of a coefficient over nearby frames but is never given the standard regression expression, so the 39-dimensional count cannot be reproduced from the text.
- ch 6 [low] section 2, phoneme model description: The left-to-right model is written as 'state 3 to 3 only', which leaves the model with no way out of state 3. Read literally, a phoneme (and so a word) could never end or pass to the next phoneme, contradicting the next sentence that a word is a chain of phoneme models.
- ch 6 [low] section 2, forward recursion: The recursion is given but never started: π is defined and then never used, so a student cannot compute α at t = 1 and may think the formula alone is complete.
- ch 6 [low] section 3 and quiz Q6: 'Decision trees tie the many triphones that behave alike' and 'tying groups triphones that share similar behaviour' suggest whole triphones are merged. In standard practice the tying is done per state position: the first, second or third HMM state of many triphones is pooled, not the triphones as whole units.
- ch 6 [low] section 3, WER paragraph: 'Accuracy is not reported.' reads as a statement about what happens in the field rather than an instruction to the student, and sits oddly beside the WER definition.
- ch 7 [high] Section 3, unit-selection cost formula: The text says 'the divisor 100 normalises each penalty so it is dimensionless'. Dividing a quantity in hertz by 100 does not remove its units; the F0 term is still measured in units of 100 Hz and the duration term in units of 100 ms. A student would wrongly believe cost is a pure number with no units and would be confused about why 100 was chosen.
- ch 7 [low] Section 1: 'Grapheme-to-phoneme conversion, G2P, is the name for this step' comes after the sentence defining a phoneme, so 'this step' no longer clearly points to the conversion step.
- ch 8 [low] Section 2, framing and summarisation step: 'Voiced frames' is used but never defined, and summarising every feature over voiced frames only is inconsistent: energy and MFCCs are normally summarised over all frames, and pause length (a cue listed in Section 1) cannot be measured if silent frames are thrown away.
- ch 8 [low] Section 2 formula block and Quiz Q4: K is defined as 'the number of emotion classes', which suggests 7 for this task, but Q4 averages over K = 2 because the test set contains only sad and neutral. A student following the definition literally would divide by 7.
- ch 8 [low] Exam traps and Beyond: Arousal and valence are used ('Arousal is easier than valence', 'dimensional labels (arousal and valence)') without ever being defined, so a first-time reader cannot follow the point.
- ch 8 [low] Section 2, first bullet: '10 ms hop' is not explained; hop is a term a student may not know.
- ch 8 [low] Section 1, energy bullet: 'Energy (frame loudness)' gives no unit or scale, unlike F0 (Hz) and speaking rate (syllables per second).
