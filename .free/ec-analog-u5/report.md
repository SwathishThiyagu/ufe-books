# ec-analog-u5: free-model run

- Book: `books/ece/ec-analog/ec-analog-u5.html`
- Status: ok
- Model calls so far: 30 (123,507 tokens in, 294,646 out), 7.4 minutes

## Checker

```
ec-analog-u5.html: 8 chapters, 15971 words, 9 figures, 166 KB
OK
```

## For the reviewer

- chapter 1: the reviewer found 1 serious problem(s) and the revision did not pass the checks; read the review in the state folder

## Reviewer notes (after any revision)

- ch 1 [high] Quiz Q6: The question says the tail current source stays ideal, so the common-mode gain is exactly zero and the joined node rises by exactly 1 V. The model answer instead says the output moves by 'roughly RC/(2REE) times 1 V, which is a few millivolts' — but an ideal source has REE = ∞, giving zero. The answer contradicts its own question and a student will memorise a nonzero output for an ideal tail.
- ch 1 [low] Section 4 (and the lead): 'Every op-amp and comparator input stage is a differential pair' is too absolute. It is true of voltage-feedback op-amps, but a current-feedback op-amp uses a different input structure (a buffer plus a mirror), and some input stages add rail-to-rail complementary pairs.
- ch 1 [low] Exam traps, last bullet: For a MOSFET pair the square-law region ends at vid = √2·VOV (about 1.4 VOV), not 'a few times VOV'; the transconductance already drops noticeably near vid ≈ 0.6 VOV. Only the BJT figure ('a few times VT', full steering near 4VT ≈ 100 mV) is right.
- ch 1 [low] Section 3, third paragraph: 'Each half can be analysed as a plain CE or CS stage of gain gm RC' can be misread: a student may multiply gm RC by the full vid and get twice the correct single-ended answer.
- ch 2 [high] Section 2, superposition formula and formula box: The text defines Ad = vod/vid and Acm = voc/vicm (differential output and common-mode output), then writes vod = Ad vid + Acm vicm. This is wrong: common-mode input does not add to the differential output. For a single-ended output, vo = Ad vid + Acm vicm with Ad and Acm defined for that single output. For a differential output, the common-mode term is a different gain (A_cm-dm), zero for perfect symmetry. The formula box then uses single-ended Ad and Acm without saying so, conflicting with the earlier definitions.
- ch 2 [high] Worked example 1, step 7: Adds the differential output vod and the common-mode output voc as if they were parts of one output. They are not: vod is the difference between the two collector voltages, voc is their average. If the output is single-ended, the worst-case magnitude is |Ad vid| + |Acm vicm| = 4.020 V, but then the quantities are not vod and voc. If the output is differential, the common-mode output does not add to the differential output.
- ch 2 [high] Section 3, mismatch paragraph: The statement '|Acm/Ad| ≈ δ, so CMRR falls to about 1/δ' for a differential output with collector-resistor mismatch is wrong. The correct result is CMRR ≈ (REE/re)/δ (or gm REE/δ). The factor 1/(gm REE) is missing.
- ch 2 [high] Quiz Q6: The answer 40 dB is wrong because it assumes CMRR = 1/δ. The correct CMRR for a differential output with collector-resistor mismatch is (REE/re)/δ, which depends on REE and re. The question lacks these values.
- ch 2 [low] Section 3, first sentence: 'CMRR, also called the common-mode rejection ratio in some syllabi' is redundant because CMRR already stands for common-mode rejection ratio.
- ch 2 [low] Section 2, first sentence: 'Let vo1 and vo2 be the two collector voltages' is introduced before the BJT pair is mentioned, which may confuse readers about the general definition.
- ch 3 [low] Section 1, after the first paragraph: The sentence "Some syllabi call these current mirror circuits; the name is the same." says nothing and can confuse a student who expects a second name for the circuit.
- ch 3 [low] Section 2, second paragraph: It says the Wilson and the cascode mirror both raise ro "by stacking transistors and using local feedback". The cascode does not use feedback; it uses a common-base (BJT) or common-gate (MOSFET) device to hold the output device voltage nearly fixed.
- ch 3 [low] Section 2, third paragraph: "Its output resistance is lower than a cascode's" is not a safe general statement. The Widlar output resistance is ro(1 + gm R2), which grows with R2 and can approach or exceed a cascode's value.
- ch 4 [low] Section 3, first paragraph: "the parallel combination is close to half of the smaller one" is only true when ron and rop are comparable. The chapter's own worked example (100 kΩ and 50 kΩ in parallel = 33.33 kΩ) gives two-thirds of the smaller value, not half, so a student applying the sentence numerically gets the wrong estimate.
- ch 4 [low] Section 3, first sentence of the price paragraph: "The price is two extra devices" contradicts the table just above, which shows 2 resistors for the resistor load and 2 PMOS for the mirror load. The device count is the same; what you pay is matching between the two PMOS devices and a high-impedance node.
- ch 4 [low] Lead paragraph: "Every CMOS op-amp input stage is built this way" is an overstatement: many input stages use a cascoded or folded active load rather than the plain five-transistor mirror, though the active-load idea is the same.
- ch 5 [low] Section 1: The phrase "Its bias current sets input resistance and input bias current" uses "bias current" twice with different meanings, which can confuse students. The first is the tail bias current; the second is the input bias current (base current).
- ch 5 [low] Section 1: The text says "The tail source output resistance and the mirror matching set common-mode rejection ratio, CMRR" but omits the matching of Q1 and Q2, which also affects CMRR. The quiz Q6 correctly includes differential-pair matching, so the main text is incomplete.
- ch 6 [high] Lead: The lead says mismatched input transistors create the bias currents IB+ and IB−. Bias currents are just the DC currents the input devices draw; a perfectly matched pair still draws them. Mismatch is what creates VOS and the offset current IOS, as the chapter's own figure correctly says, so the lead contradicts the body and would push a student to write a wrong exam answer.
- ch 6 [low] Section 2, slew-rate paragraph: "Gm reduction by source degeneration lowers gm while keeping a larger I5" is backwards and unclear. The point of degeneration is to keep the same gm (so loop stability and bandwidth stay put) while running a larger I5.
- ch 6 [low] Section 3, PSRR formula box and text: The dB relation is given but not the unit rule inside the log, and students often plug a µV/V number straight into the logarithm and get -120 dB instead of +80 dB. The chapter also does not say that data sheets quote PSRR separately for the positive and negative rail.
- ch 6 [low] Figure, slew-rate node: The note on the slew-rate block reads 'I/Cc', but the current that charges Cc is the tail current I5, not a generic I. This invites the wrong formula on the exam.
- ch 6 [low] Figure caption: "All three add to output error or restrict output swing" is wrong for slew rate. Slew rate limits how fast the output can move (large-signal speed and settling), not how far it can swing. Swing and common-mode range are separate limits.
- ch 6 [low] Worked example 1 (steps 1 and 2), Section 2, exam trap 1: Powers of ten appear without superscripts: "0.5 × 106 V/s", "4 × 10−6 s", "3.979 × 104 Hz", "wrong by 106". Read literally, 106 V/s is a million times off, which is exactly the mistake the chapter is warning against.
- ch 7 [low] Section 2, phase-margin sentence: The number 2.2 does not give 60° in a two-pole loop. With PM = 90° − arctan(f_u/f_p2), f_p2 = 2.2 f_u gives arctan(1/2.2) ≈ 24.4°, so PM ≈ 65.6°. The exact two-pole value for 60° is f_p2 ≈ 1.73 f_u. A student who checks the chapter's own arctan formula will think they made a mistake.
- ch 7 [low] Section 1, Miller formula: A2 is called "the voltage gain of the second stage", but the same paragraph says the second stage inverts. With A2 taken as a negative number, Cc(1+A2) is wrong, and the formula only works if A2 means the gain magnitude. The quiz Q2 answer uses A2 the same loose way.
- ch 7 [low] Section 1, first paragraph: The reference to chapter 5.4 is plain text, not a chapter link, so a phone reader cannot jump to the differential pair being reused.
- ch 8 [high] Worked example 1, step 7: It calls ±50 µA the current limit. Iout is the difference of the two drain currents, so its limit is the whole tail current, ±IBIAS = ±100 µA. This also contradicts step 8 and Section 3, which correctly say the current flattens at ±IBIAS.
- ch 8 [high] Section 3, worked example step 8 and the example answer: The chapter says the pair 'stays close to linear for |vid| up to about VOV' and gives the linear range as ±0.2 V. At |vid| = VOV the slope Gm has already fallen to about 0.58 of its small-signal value, a drop of roughly 40 percent, and the transfer curve is about 13 percent compressed. A student would treat ±VOV as a clean linear range and get large distortion.
- ch 8 [low] Section 2, third paragraph: 'the difference of the two drain currents is the output current, and it equals the expression below' points at a formula for Gm, not for a current. A quick reader would take Gm = IBIAS/VOV to be an expression for Iout.
- ch 8 [low] Worked example 1, step 2: Unit slip: k′(W/L) is in A/V², so the denominator is 2500 µA/V², not 2500 µA/V.
- ch 8 [low] Section 3, Gm-C filters bullet: 'each resistor of an RC filter is replaced by an OTA and a capacitor' suggests the capacitor is new. In a Gm-C filter the resistor is replaced by an OTA and the existing capacitor stays; the cut-off is Gm/C.
- ch 8 [low] Section 2, second paragraph: 'the DC operating point stays roughly the same' is misleading. Changing IBIAS changes each drain current ID = IBIAS/2 and the overdrive VOV = √(IBIAS/(k′W/L)) by the square root of the bias ratio.
- ch 8 [low] Quiz Q7, answer: 'An integrated resistor carries a large process tolerance' is awkward and unclear English for readers using English as a second language.
