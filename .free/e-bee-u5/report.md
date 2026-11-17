# e-bee-u5: free-model run

- Book: `books/common/e-bee/e-bee-u5.html`
- Status: ok
- Model calls so far: 26 (97,310 tokens in, 203,366 out), 5.4 minutes

## Checker

```
e-bee-u5.html: 7 chapters, 13036 words, 8 figures, 143 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 1 (unsigned range), Section 2 (signed range), Q7 (modulo): The exponent is missing its superscript, so the ranges read literally as '0 to 2n−1' and '−2n−1 to 2n−1−1', which is not the standard range and gives a wrong formula if read as printed. Elsewhere the chapter does use <sup>, so the notation is inconsistent.
- ch 1 [low] Figure (BCD addition of 8 + 7): The 'live' mark on the '7 in BCD' row is at cell index 4, which holds 0 in 0000 0111. The intended highlighted bit (the first 1 of the low nibble) is at index 5.
- ch 2 [high] Exam traps, third bullet: The claim 'An XOR-only circuit cannot make AND without a fixed 0 or 1' is false. Adding constant 0 or 1 does not help: any circuit built only from XOR gates and constants computes an affine function of the inputs (F = c ⊕ a₁A ⊕ a₂B ⊕ ...), while AND is not affine. A student reads this and concludes that XOR plus a constant can build AND.
- ch 2 [high] Quiz Q6 answer: The answer says AND and OR 'cannot produce NOT from a single input without a fixed 1 or 0', implying that a fixed 1 or 0 would let them invert. It does not: AND(1,A) = A, AND(0,A) = 0, OR(0,A) = A, OR(1,A) = 1. The stated reason is wrong even though the conclusion (not universal) is right.
- ch 2 [low] Section 3, NOR paragraph: Gate counts are given for the three NAND constructions but not for the two NOR constructions, so the student cannot compare cost.
- ch 2 [low] Section 1, first paragraph: '0 for low voltage, 1 for high voltage' is stated as if it were the only convention; it is the positive-logic convention.
- ch 3 [high] Quiz Q5: The pair m5, m7 does not give BC. m5 = 101 and m7 = 111, so A = 1 and C = 1 in both, while B is 0 in m5 and 1 in m7 and therefore drops out. The term for that pair is AC, so the stated answer F = C' + BC is wrong and does not even cover m5 (B = 0 there). The answer also misses the better use of the don't-cares.
- ch 3 [low] Section 1, formula line: "i runs over 0 to 2n−1" reads as 2n minus 1, not 2 to the power n minus 1. A student can copy the wrong limit.
- ch 3 [low] Section 2, group sizes: The list of legal group sizes stops at 8, but a 4-variable map (16 cells) also allows one group of 16, which gives the constant 1.
- ch 4 [low] Section 3 (BCD adder), correction formula: Cout appears in Ccorr = Cout + S3S2 + S3S1 without being defined in this section. Earlier the same symbol meant the full adder's output carry (Section 2), so a student can mix up the full adder carry with the carry out of the 4-bit binary adder.
- ch 4 [low] Worked example 1, step 7: The line 'so Ccorr = S3S1 = 1' silently drops the other two terms and can read as if the correction condition were only S3 AND S1.
- ch 4 [low] Quiz Q4, answer: The final answer says 'carry 1 and low digit 0101, decimal 15'. It never shows the two BCD digits, so a student may take 0101 alone as the result (which would be 5).
- ch 4 [low] Section 3, first paragraph: 'the raw sum can land in 10 to 19' uses numbers without a stated base or a note on where 19 comes from.
- ch 5 [high] Section 2, end of the paragraph (after the 8:1 sentence): The sentence 'The delay is two MUX delays, not three, because the final MUX combines two parallel branches' comes right after the 8:1 MUX sentence, so a student reads it as the delay of the 8:1 tree. An 8:1 MUX built from seven 2:1 MUXes in three stages has three MUX delays, one per stage. The two-delay fact is true only for the 4:1 tree built above.
- ch 5 [high] Section 1, enable paragraph (and it affects exam traps item 3 and Q8): The chapter says EN' = 1 forces Y = 0, then says the enable lets several MUX outputs share one bus with only the enabled MUX driving it. Both cannot be true: an output forced to 0 cannot sit on a shared bus with an active output, because the two outputs would fight. Bus sharing needs a high-impedance (tri-state) disable.
- ch 5 [low] Section 4, decoder paragraph: 'One-hot lines' is used without definition, which an ESL reader may not know.
- ch 5 [low] Figure aria text: The figure is described as a 'three-level tree'. The mux stages are two, and the chapter itself stresses two MUX delays, so 'three-level' can be misread as three stages of multiplexers.
- ch 6 [low] Lead and Exam trap 1: The lead says the flip-flop cell is 'also called a latch', but exam trap 1 says 'Do not treat the names as synonyms'. A student reading both will be confused about whether latch and flip-flop are the same thing.
- ch 6 [low] Section 1: The plain SR latch has no clock or enable input, so calling it 'this level-triggered cell' is inaccurate; level triggering only applies once a clock or enable gate is added (Section 2). It also sits oddly next to the sentence 'A clock is not needed for this basic latch.'
- ch 7 [high] Worked example 1, steps 1 and 8 (and Section 2 block list): The example picks an 8051-family chip and then assumes an on-chip ADC: 'the ADC, timer, GPIO, program memory and RAM are all on the one chip' and 'a microprocessor would need separate ROM, RAM, timer and ADC chips'. The classic 8051 has no built-in ADC; it needs an external ADC0808/0809 (or a special variant) plus its wiring. A student would write in the exam that the 8051 has an internal ADC and lose marks.
- ch 7 [low] Section 1, word length paragraph, and Exam trap 3: 'It is the width of the data bus' and 'the data bus width is the word length' are stated as if always true. Usually true, but not always: the 8088 has a 16-bit word with an 8-bit external data bus, and the 8086 has a 16-bit word with a 16-bit data bus. Presented as a rule, it can mislead.
- ch 7 [low] Figure ('Inside a microcontroller chip'): The figure shows Flash and RAM both hanging from one system bus, which contradicts the Harvard description given just above it: an 8051-type Harvard MCU has separate program and data buses.
- ch 7 [low] Quiz Q3 answer: 'It has no program memory, no RAM, no timer, no ADC and no I/O pins' — a microprocessor does have pins (address, data, control, and often serial lines); what it lacks is general-purpose parallel I/O ports, which come from chips such as the 8255.
