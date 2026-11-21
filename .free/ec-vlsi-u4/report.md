# ec-vlsi-u4: free-model run

- Book: `books/ece/ec-vlsi/ec-vlsi-u4.html`
- Status: ok
- Model calls so far: 23 (89,426 tokens in, 234,422 out), 7.4 minutes

## Checker

```
ec-vlsi-u4.html: 7 chapters, 14238 words, 8 figures, 150 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Quiz Q6: The question gives a = 1011 and b = 0110, but the answer quotes the generic worst case (c1 at 2, c2 at 4, c3 at 6, c4 at 8, sum at 9). For this particular input the carry is not born at column 0: g0 = 1·0 = 0, so c1 = 0. The carry is born at column 1 (g1 = 1·1 = 1) and then propagates through columns 2 and 3 (p2 = 1, p3 = 1). So c2 is ready about 2 gate delays in (g1 plus one OR), c3 at about 4, c4 at about 6, and the last sum bit at about 7 — not 8 and 9. A student who follows the stem gets the wrong numbers, and the same input pair appears in Worked example 1, which makes the confusion worse.
- ch 2 [high] Section 1, paragraph 4 (area): The mux count for a two-bit carry-select block is wrong. Two sum bits and the block carry out are each selected, so three 2:1 multiplexers are needed, not two. The same section says 'The carry out of the block is also selected', which contradicts 'two 2:1 multiplexers'.
- ch 2 [high] Section 1, paragraph 5 (square-root layout): 'area grows roughly with √n' is technically wrong. Every one of the n sum bits still needs at least one full adder, so area is proportional to n; two ripple adders per block make it roughly double a plain ripple adder. Only the delay falls as √n.
- ch 2 [low] Section 1 last paragraph and Section 2 third paragraph: The name 'square-root adder' is used for both carry select (the square-root layout) and carry skip (k = √n). A student may think the two names refer to the same architecture.
- ch 3 [low] Section 1 and Section 2 (gate count), and Quiz Q1: The chapter says a 4×4 array 'needs 12 full adders' and generalises to 'n(n−1) full adders'. The total number of adders, n(n−1), is right, but in the usual array the adders that receive only two bits plus no carry (the leftmost adder of each row) are half adders, not full adders. A student who draws the array and counts three-input adders will get fewer than 12 full adders and think the chapter is wrong.
- ch 3 [low] Section 2, first paragraph: 'The layout is rectangular and regular, so it maps cleanly to layout and to a cell library.' The word 'layout' is used twice with two different meanings, which reads badly for a second-language reader.
- ch 3 [low] Section 2, 'Each column adds the bits that land in it plus the carry from the column above.': 'the column above' suggests a carry comes straight down the same column, which contradicts the diagonal-carry idea the chapter keeps stressing. In the array, a carry arrives at column k+1 from row j−1, that is from the column on the left in the row above.
- ch 3 [low] Figure (4×4 Braun array spec): Every row shows the same four cells in the same positions, with no shift, and the cells are written MSB-first (1 1 0 1 for a = 1101) while show_index with index_from 0 labels the leftmost cell as column 0. A student can read the figure as saying row 1 has the same weight as row 0, and can also misread which cell is a0.
- ch 4 [low] Figure spec and caption: The level-4 box is labelled '2 rows' but its note says 'final adder'. The step from 3 rows to 2 rows is itself one carry save adder (3:2 counter). The final carry propagate adder comes after those 2 rows, so the figure contradicts the text ('four reduction levels', CPA is not a reduction level). The caption adds to the confusion by saying 'The last box is the final carry propagate adder' when the last box is labelled '2 rows'.
- ch 4 [low] Section 1, first paragraph: 'A carry save adder (CSA) takes three bits of the same weight' describes a full adder, not a CSA. A CSA takes three N-bit operands and produces a sum word and a carry word; one full adder handles one bit column. The next sentence ('A full adder is one column of a CSA') corrects this, but the opening definition is loose and a student may quote the wrong version in the exam.
- ch 5 [high] Section 3 (Comparator), magnitude-cell formulas: The first carry equation is mislabelled. The text says 'L means Aout = Gin + Ein·Ai·Bi′', but the correct equation is Gout = Gin + Ein·Ai·Bi′. Gout is never defined, and L is not defined as A<B.
- ch 5 [high] Section 3 (Comparator), final flags sentence: The final sentence says 'Lout=1 means Aout=1 means A=B', which is wrong. Lout=1 means A<B; Eout=1 means A=B.
- ch 5 [high] Figure: The figure says the same three inputs feed a 3-to-8 decoder, an 8-to-1 multiplexer and a 4-bit comparator. An 8:1 mux needs 8 data inputs plus 3 selects, and a 4-bit comparator needs two 4-bit words (8 bits), so the same three bits cannot feed all three.
- ch 5 [low] Section 3 (Comparator), equality delay: A linear AND chain for n bit-equality signals needs n−1 AND gates, not n, and the XNOR delay is omitted from the chain comparison. The delay is tXNOR + (n−1)·tAND, or n·tAND only as a loose upper bound.
- ch 5 [low] Section 2 (Multiplexer), mux-tree delay: The delay is written as log₂N mux levels for an N:1 mux. For N not a power of two this is not an integer; a mux tree uses ceil(log₂N) levels.
- ch 6 [high] Section 2, master-slave register: The clock assignment contradicts the behaviour described in the same paragraph and the EN convention defined in Section 1. Section 1 says a D latch is transparent when EN=1. If the master is driven by CLK and is transparent while CLK=0, that means its enable is CLKbar, not CLK. As written ('Drive the master with CLK and the slave with CLKbar'), the master would be transparent while CLK=1 and the slave while CLK=0, which gives a falling-edge register, not the rising-edge one the paragraph and the figure describe.
- ch 6 [low] Section 3, last sentence on clock skew: 'Add clock skew if the clock arrives at different times at launch and capture' does not say which sign, and a student who literally adds skew to the setup inequality gets the wrong answer. Positive skew (capture clock arrives later than the launch clock) relaxes setup but tightens hold.
- ch 6 [low] Section 1, last sentence of the gated D latch part: 'It is small, fast and common inside flip-flops and SRAM cells' attaches the gated D latch to SRAM. An SRAM cell is a pair of cross-coupled inverters with access transistors (a static latch), not a gated D latch, so a student may draw the wrong cell structure.
- ch 7 [high] Section 1, array organisation and the R = 2^r, C = 2^c formula: The word count and the address split contradict each other. The text says the array is 'R words of C bits each' and also that the address splits into r row bits and c column bits, with the column multiplexer passing only Cout of the C bitline pairs. If a c-bit column address exists, the array holds 2^r × 2^c = R·2^c words of C/2^c (= Cout) bits each, not R words of C bits. Also, C = 2^c and Cout < C cannot both hold if the words are C bits wide. A student cannot tell how many words the array really stores.
- ch 7 [low] Section 2, 6T SRAM, cell ratio sentence: 'Make the pull-down wider than the access transistor, typically above about 1.2 to 2' is vague — it is unclear whether the target is 1.2, 2, or a range. The cell ratio is a strength ratio, not a width, so 'wider' alone is loose.
- ch 7 [low] Section 2, 1T1C DRAM, bitline swing sentence: The numbers do not match. With CS in the tens of fF and CBL in the hundreds of fF, CS/(CS + CBL) is about 0.1, so with (Vcell − VDD/2) at most about VDD/2 the swing is tens of millivolts, not 'tens to hundreds of mV'.

## Correction pass (2026-11-21)

- Checker: `ec-vlsi-u4.html: 10 chapters, 30081 words, 11 figures, 281 KB` / OK (with --render).
- Every reviewer note above was fixed in the text. Worked examples and calculations were retraced and corrected.
- New chapters: pipelining and sequential circuits (7), timing and clocking strategies (8), memory architecture (10). Chapter 6 was rewritten. Memory cells moved to chapter 9 (old review7 is now review9).
- All figures were redrawn by hand (pipeline/claude_figs/ec_vlsi_u4.py).
- The question bank now has 16 long questions, each with points to cover and a full model answer.
- The university-hosted source was dropped from the sources list.
