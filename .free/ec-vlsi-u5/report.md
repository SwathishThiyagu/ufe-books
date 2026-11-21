# ec-vlsi-u5: free-model run

- Book: `books/ece/ec-vlsi/ec-vlsi-u5.html`
- Status: ok
- Model calls so far: 21 (70,935 tokens in, 153,205 out), 4.8 minutes

## Checker

```
ec-vlsi-u5.html: 7 chapters, 12397 words, 8 figures, 143 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 3, test handoff: The cost formula 'tester time per pattern × number of patterns × tester rate' does not say what unit 'tester rate' has, so a student can read it as patterns per hour and get a time instead of a cost in rupees.
- ch 1 [low] Section 1 versus Exam traps: Section 1 says verification 'runs beside RTL and continues to signoff', but the first exam trap says it 'runs beside every stage'. The two statements disagree, and the figure shows verification hanging off RTL only.
- ch 1 [low] Section 1, tapeout bullet: 'Tapeout: release masks, fabricate, package, test on the tester' merges four separate steps into the word tapeout. Tapeout is only the handoff of the final layout database for mask making; fabrication, packaging and test come after it.
- ch 2 [high] Section 3, Operators paragraph (shift operators): The shift sentence reads "Shift: >; >>> is arithmetic right shift for signed values." The left-shift and logical-right-shift operators are missing from the text, so only ">>>" is defined even though the figure and worked example use "a << 1". A student cannot learn <<, >>, >>> from this line.
- ch 2 [high] Section 3, Operators paragraph (relational and equality): The sentence reads "Relational  >= and equality == != return 1-bit", with a blank where the operators should be. The relational operators <, <= and > are never defined, yet > is used in the figure and worked example, so the operator set the exam tests is incomplete.
- ch 2 [low] Section 3, Operators paragraph (reduction): "Reduction: & | ^ ~& ~| ~^ before one vector return one bit" uses "before" where it means "applied to"; the wording is unclear on the phone.
- ch 3 [high] Section 3, Exam traps, Quiz Q4: The nonblocking assignment operator <= has been lost, so the text reads 'Use nonblocking  in sequential always blocks', 'Mixing = and  in one clocked always block. Use  for every state register update', and 'Why is nonblocking  used in a clocked always block?'. The student sees a blank where the most important operator of the section should be, and the contrast with blocking = is destroyed.
- ch 3 [low] Section 4, table, Behavioural row: The typical statement shown is 'always @(*) if (sel) y = b;' with no else. Copied as written, this holds y when sel=0 and infers a latch, which contradicts the latch warning two paragraphs above.
- ch 3 [low] Section 4, last paragraph: 'Gate level uses four instances of a 1-bit mux or gates' is loose: Verilog has no 1-bit mux primitive, so a mux can only be an instance of a user module (structural) or be built from gate primitives.
- ch 4 [high] Section 1, clock generation: always #5 clk = ~clk; does not give a 10 ns period on its own. A reg starts as x, and ~x is still x, so the clock line stays x forever and every clocked block in the bench stalls. The delay unit also depends on the timescale directive, not on ns by default.
- ch 4 [high] Section 3, timing checks: "For clocked logic, sample after the setup time has passed" is wrong: setup time is a constraint on the input before the active clock edge, not a delay after it. Sampling is timed from the edge, after the flip-flop's clock-to-Q delay.
- ch 4 [low] Worked example 1, step 6: It says "The checker drives each vector, waits #10 ... then compares", which mixes the stimulus role and the checker role and can confuse students writing the two blocks.
- ch 5 [high] Figure (4-input LUT truth table): Entry at index 3 is shown as 0. Index 3 is address 0011, so A=0, B=0, C=1, D=1, giving C·D = 1 and f = 0 OR 1 = 1. The table contradicts the function f = A·B + C·D that it claims to store.
- ch 5 [low] Exam traps, third bullet: The sentence 'Do not multiply product terms by outputs in a PAL' is unclear and does not say what the student should actually do; the second half then talks about PLA sharing instead of the PAL point.
- ch 5 [low] Quiz Q7: The question asks for blocks 'inside an FPGA logic fabric', but one of the four named blocks, the IOB, is the input/output block at the chip edge, not part of the logic fabric.
- ch 5 [low] Section 3, last sentence: Chapter 5.6 and 5.7 are named in plain text without the cross-reference links used elsewhere in the book, so a student reading on a phone cannot jump to them.
- ch 6 [low] Section 3 and Quiz Q7: Global routing is said to assign nets to "regions or tracks", but the exam trap correctly says global assigns regions while detailed routing picks exact tracks. The word "tracks" in the definition contradicts the trap and can confuse a student about where track assignment happens.
- ch 6 [low] Section 3, via definition: Saying each via "adds resistance and capacitance" overstates the capacitance. A via is mainly a resistance and a reliability risk; its capacitance is small next to the wire it joins.
- ch 6 [low] Lead: "Every CMOS chip uses this backend flow" is too strong. Hand-drawn analog, RF and small full-custom chips skip standard-cell floorplanning and placement, even though they still end in GDSII and signoff.
- ch 7 [low] Figure caption: The caption says "only the CPU is shown as synthesizable RTL". Students can read this as saying the UART soft IP is not synthesizable RTL, which contradicts Section 1, where soft IP is defined as synthesizable RTL. The diagram simply does not print the RTL note under the UART box.
- ch 7 [low] Section 2, address paragraph: "Every core needs an address in the memory map" is too strong. Blocks such as a PLL, a SerDes lane or a purely streaming datapath may have no memory-mapped registers, and a hard memory macro is addressed as memory, not as a core register space.

## Claude correction pass (21 Nov 2026)

Checker: `ec-vlsi-u5.html: 8 chapters, 23473 words, 10 figures, 243 KB` then `OK` (with --render).

- New ch 5.2 Introduction to ASICs (exam subtopic): ASIC types table, full-custom, standard cells, gate arrays (channelled, sea of gates, structured), NRE and break-even with a four-option cost example; later chapters moved to 5.3 to 5.8.
- 5.1 rewritten for the EC3552 topics: tapeout is only the handoff, wafer-to-chip flow, SoC verification and test issues, scan, boundary scan, test coding; second example on scan test time and cost.
- 5.3 second example (concatenation, sign extension, shifts, reductions, x, widths); 5.4 gate-level and switch-level code; 5.5 full self-checking bench with real output and a faulty-DUT run; 5.6 ROM/PAL/PLA example, Actel and Xilinx blocks, switching technologies; 5.7 HPWL swap example, global routing and via wording; 5.8 memory-map example, IEEE 1500 core test, soft-core names. All Verilog compiled and run with Icarus Verilog 12.
- Every figure redrawn by hand from its chapter's example; 13 full model answers; cross-unit references named by topic.
