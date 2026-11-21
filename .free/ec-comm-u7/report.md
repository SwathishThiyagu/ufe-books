# ec-comm-u7: free-model run

- Book: `work/ec-comm-u7/tree/books/ece/ec-comm/ec-comm-u7.html`
- Status: ok
- Model calls so far: 38 (157,720 tokens in, 331,328 out), 8.7 minutes

## Checker

```
ec-comm-u7.html: 9 chapters, 24295 words, 10 figures, 249 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Section 1, first paragraph: The probability range is printed as "0 i ≤ 1", which is garbled: the variable and the lower-bound inequality sign are missing, so the definition of pi is incomplete and a student cannot tell whether p = 0 is allowed.
- ch 1 [low] Section 2, second paragraph: "A source with many likely symbols has high entropy" is loose — many likely symbols is not the point; what matters is that the probabilities are close to equal.
- ch 1 [low] Whole chapter (prose vs formulas): Base-2 logarithms are written "log2" in running text (e.g. "Hmax = log2 M", "log2 8 = 3") but as log<sub>2</sub> inside the displayed formulas, so the notation is inconsistent.
- ch 2 [high] Section 1, Kraft inequality formula: The Kraft inequality is printed as Σ 2−lᵢ ≤ 1. As written this means the sum of (2 minus lᵢ), which is not the Kraft inequality. The −lᵢ must be an exponent of 2.
- ch 2 [low] Section 1, formula box H(X) ≤ L̄ < H(X) + 1: The upper bound is attributed to the average length of 'a prefix code', which reads as if every prefix code satisfies L̄ < H(X) + 1. A badly built prefix code can exceed H(X) + 1; the bound holds for an optimal (Huffman) code or, in general, for a code built by the Shannon-Fano procedure.
- ch 2 [low] Worked example 1, part (b) and step 5: The question says 'choosing the tie so that D and E merge first', but D and E at 0.1 each are strictly the two smallest probabilities — there is no tie at that step. The actual tie comes at the next step, where B, C and DE all have probability 0.2.
- ch 3 [high] exam traps, third trap: The explanation of the wrong-sign trap is itself wrong. Writing I = H(X) + H(Y) + H(X,Y) does not give back H(X,Y); it gives H(X)+H(Y)+H(X,Y), which is not an entropy of anything useful. A student reading this will believe the plus sign reproduces the joint entropy.
- ch 3 [low] section 3, binary erasure channel sentence: It says the channel 'either passes a bit or outputs an erasure with probability e' but never states the probability of passing, so the erasure probability is attached to the wrong alternative in the reader's mind.
- ch 3 [low] section 1, joint and conditional entropy formulas: The formulas contain log₂ P for terms where P can be zero (for example a channel matrix with zero entries), and the convention that is used in that case is not stated.
- ch 4 [low] Lead: "It is the best error-free data rate the channel can support" is too strong. Capacity is the highest rate at which the error probability can be made arbitrarily small (in the limit of long blocks). A student may read "error-free" as "a simple link can reach C with zero errors", which later material on the coding theorem contradicts.
- ch 4 [low] Section 1: The maximisation max over p(x) of I(X;Y) is stated without the average input power constraint. For a continuous channel with no power limit the mutual information can be made as large as we like, so the step to C = B log₂(1 + S/N) is unexplained and a student cannot see where S enters the maximisation.
- ch 4 [low] Figure: "at low SNR the absolute changes are smaller" is vague. Smaller than what, and in which units? A student may read it as "capacity barely changes at low SNR", which the plot (0.14 to 1 bit/s/Hz between −10 dB and 0 dB) can appear to contradict depending on how it is read.
- ch 5 [high] Section 1, random-coding paragraph: The number of randomly chosen codewords is printed as "2nR", which reads as 2 × n × R. The random-coding proof uses 2^(nR) codewords, i.e. 2 raised to the power nR, to get rate R = (log₂ M)/n with M = 2^(nR). A student reading 2nR would get a completely wrong rate.
- ch 5 [high] Quiz Q1 answer: The answer is corrupted: "every rate R e → 0 as n → ∞" has lost the condition R < C and the symbol P<sub>e</sub>, so the statement is meaningless and, as printed, wrong.
- ch 5 [low] Section 2, coding gain formula and the 10 dB / 7 dB example: The formula needs the linear (power-ratio) values of Eb/N0, but the example quotes 10 dB and 7 dB. A student who substitutes 10 and 7 directly into the formula gets 10 log₁₀(10/7) = 1.55 dB, not the 3 dB stated.
- ch 6 [high] Section 3 and Quiz Q6: The exponents are lost, so the displayed arithmetic is false. Section 3 reads "The Hamming bound for t = 1 is 2n−k ≥ 1 + n. For (7,4): 23 = 8 and 1 + 7 = 8", and Q6 reads "23 ≥ 1 + 7". "23 = 8" is not true, and "2n−k" can be misread as 2n − k.
- ch 6 [high] Section 2, hardware paragraph: "each output bit is the modulo-2 sum of the G columns marked by m" is wrong twice: the encoder XORs the <i>rows</i> of G picked by the 1 bits of m, and that XOR gives the whole codeword, not one output bit. Bit j of c is the sum of the entries in column j of the selected rows. A student who follows the text will build the wrong wiring.
- ch 7 [high] Section 1, second paragraph (bit numbering): The text says the leftmost bit of a 7-bit word is c₇, but a 7-bit word has coefficients c₀ to c₆. This also contradicts the formula given two lines later (c_{n−1} is the leftmost, i.e. c₆) and the worked example, where the message 1101 is called x³ + x² + 1 with the leftmost bit as the x³ coefficient.
- ch 7 [low] Section 2, first paragraph: "Keeps the message in the first k positions" is ambiguous, because the chapter has just numbered positions from the right (c₀, c₁, …). A student can read "first k" as c₀…c_{k−1}, which is exactly the parity-on-the-left mistake listed in the exam traps.
- ch 8 [high] Section 2, Section 3, Exam traps, Quiz Q4: Exponent notation is missing throughout: '22 = 4', '2K−1 states', '2K states', '2K−1 compare-select', and '2K−1 = 26 = 64' read as 22, 2K minus 1, etc. This gives the wrong state count and the wrong number of compare-select operations.
- ch 9 [high] Lead: The lead says all three codes 'sit within a fraction of a decibel of the Shannon limit'. BCH codes are a few dB from capacity, as the chapter's own table in Section 4 states, so the lead contradicts the table and overstates BCH.
- ch 9 [high] Section 1, second paragraph: The superscripts are lost, so the text reads 'GF(2m), a field with 2m elements' and 'α, α², …, α2t'. A field with 2m elements is not what the construction gives; the field has 2^m elements, and the roots run to α^(2t). A student would misread both.
- ch 9 [low] Section 1, third paragraph: 'Two standard codes exist here' is not true: with m = 4 the length-15 BCH family also contains the t = 1 code (15,11), which is the Hamming code, and the (15,1) code.

## Claude correction pass (21 Nov 2026)

- Every worked example, quiz answer and bank answer recomputed in Python (entropy, Huffman and Shannon-Fano lengths and efficiencies, BSC mutual information and capacity, Shannon-Hartley, repetition error rates, Hamming (7,4) encode and syndromes, cyclic division and shift register, convolutional encoding and full Viterbi trellises, union bound).
- All reviewer notes checked; the exponent, garbled-inequality and wrong-hardware notes were already fixed in the revision; the remaining ones (capacity "error-free", missing power constraint, BEC derivation pointer, lead claims, wrong-sign trap) fixed here.
- Formulas longer than one line showed raw sub/sup tags in the draft book; rewritten in Unicode.
- New worked examples: Nyquist-sampled 4-level source (1.811 bits, 14.5 kbit/s); Shannon-Fano vs Huffman (2.31 vs 2.30 bits/symbol); BSC with unequal input (0.456 bit); bandwidth vs power (4.00, 6.17, 4.95, 21.6 Mbit/s). Cyclic example now decodes a concrete received word; Viterbi example has the full trellis table.
- All 9 figures redrawn by hand from each chapter's own example; 13 bank questions have model answers.
