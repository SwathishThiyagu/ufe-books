# ec-mp-u3: free-model run

- Book: `books/ece/ec-mp/ec-mp-u3.html`
- Status: ok
- Model calls so far: 32 (114,732 tokens in, 245,267 out), 5.5 minutes

## Checker

```
ec-mp-u3.html: 8 chapters, 14860 words, 9 figures, 147 KB
OK
```

## For the reviewer

- chapter 2: the figure cannot be drawn: tree is too wide (7 leaves); use fewer leaves or shorter labels

## Reviewer notes (after any revision)

- ch 1 [high] Figure: The figure says only the branch group can change the program counter, but Section 3 lists JB and JNB inside the bit manipulation group, and those two are conditional jumps that load the program counter. The figure and the text contradict each other, and a student will copy the wrong rule.
- ch 1 [low] Lead: 'the same job takes one byte on the 8085, six on the 8086' reads as if a comparable operation is six bytes on the 8086. Six bytes is the maximum instruction length, not a typical job; a register move is two bytes on the 8086.
- ch 1 [low] Section 2: 'The 8085, 8086 and 8051 are two-address machines' clashes with Exam trap 4, which shows 8085 ADD B as a one-address instruction with an implicit accumulator. Many textbooks call the 8085 a one-address machine for exactly this reason, so the flat statement confuses the classification the chapter is teaching.
- ch 1 [low] Section 3, data transfer: 'They move bits and change nothing else' is wrong for PUSH and POP, which change the stack pointer (and write or read memory).
- ch 1 [low] Section 1, formula: L = B_op + B_M + B_d + B_i has no term for 8086 prefix bytes (LOCK, REP, segment override), so a student applying it to a prefixed instruction gets too small a length.
- ch 1 [low] Section 1, PIC bullet: 'almost every instruction is one word' implies exceptions exist in the PIC12 and PIC16 families, but every instruction in these cores is a single word.
- ch 2 [high] Section 2, Relative mode: The claim that '8085 conditional jumps use an 8-bit offset relative to the program counter' is false. The 8085 has no program-counter-relative branching at all: JMP and every conditional jump (JZ, JC, JNC, etc.) carry a full 16-bit absolute address in the instruction. The 8-bit signed PC offset belongs to the 8051 (SJMP, JZ rel, DJNZ rel), so a student could carry the wrong fact into the exam and also mis-answer a question on why 8085 code is not position independent.
- ch 2 [high] Section 2, Stack mode: '8086 PUSH AX stores AX at [SP] and then subtracts 2 from SP' gives the wrong order and the wrong final location. On the 8086, SP is decremented first and AX is then written at the new SP. As written, a student would conclude the pushed word sits at the old top-of-stack address, which is exactly one word too high. It also contradicts the 8085 sentence just before it.
- ch 2 [low] Beyond box: The sentence says RISC-V and ARM 'add scaled index modes for arrays of 2, 4 or 8 bytes'. ARM does have scaled register offsets (a shift applied to the index register), but base RISC-V has no scaled index mode: the index must be converted to a byte offset with a shift instruction before the load or store. Only x86-64 scales the index inside the instruction, through the SIB scale factor.
- ch 3 [high] Quiz Q6: The answer says HL and DE can be swapped with three MOV instructions taking three bytes. Two 8-bit registers cannot be swapped with three moves: each byte needs a temporary, and A can hold only one byte at a time. The real sequence is six MOVs (MOV A,H / MOV H,D / MOV D,A / MOV A,L / MOV L,E / MOV E,A), that is six bytes and six instructions. A student who writes 'three MOVs' loses marks.
- ch 3 [high] Quiz Q6: The second reason given is not a difference: MOV also leaves all five flags unchanged on the 8085, so 'XCHG leaves the flags unchanged' cannot be a reason to prefer XCHG over MOVs.
- ch 3 [low] Quiz Q5: 'A memory-to-memory copy would also need two bus cycles' is loose. A single instruction reading and writing memory needs two separate memory accesses (a read machine cycle and a write machine cycle), each several T-states long.
- ch 3 [low] Section 2 and Exam trap 3: 'HL is not allowed because [HL] already has the name M' and 'HL has no 16-bit form here' are misleading. HL is a 16-bit register pair; the actual reason is that no LDAX H / STAX H opcode exists, because MOV A,M and MOV M,A already do that job.
- ch 4 [high] Section 2 and exam trap 3: DAS is presented next to the 8085 rotate and CMA instructions, so a student concludes the 8085 has DAS. The 8085 has only DAA; DAS is an 8086 instruction. Trap 3 ('DAA ... and DAS only after BCD subtraction ... On the 8051, DA A is used only after addition') repeats the implication that DAS belongs to this 8085 family.
- ch 4 [high] Section 2, bit-manipulation sentence: 'The 8086 has bit test and modify forms' is wrong. BT, BTS, BTR and BTC arrived with the 80386 and later. The 8086 has only TEST (an AND that sets flags and discards the result).
- ch 4 [low] Lead: 'Each instruction takes operands, computes a result, writes it back, and updates flags' overgeneralises. CMP and CPI compute but do not write back. INR and DCR never touch C, INX and DCX touch no flags. A student may expect every instruction to behave like ADD.
- ch 4 [low] Section 1, flags paragraph: AC is defined only as 'carry from bit 3 to bit 4'. In subtraction AC means a borrow from bit 4, which the chapter never says, though it uses SUB in quiz Q7.
- ch 4 [low] Section 2, first line of the rotate group: 'Rotates move bits through carry' is true for RAL and RAR only. RLC and RRC rotate the accumulator circularly and merely copy the shifted-out bit into C; the old C does not enter.
- ch 4 [low] Quiz Q4 answer: The correction condition is misstated. DAA adds 60H when the high nibble is greater than 9 or CY was set, not when AC was set. As written, '06H or 60H when a nibble exceeded 9 or AC was set' wrongly ties 60H to AC.
- ch 4 [low] Exam trap 5: 'DIV and IDIV ... do not set flags like ADD' can be read as 'flags are left unchanged'. On the 8086 the flags after DIV/IDIV are undefined, not preserved.
- ch 5 [high] Section 3, last paragraph ("The 8086 SHORT jump is relative; NEAR and FAR jumps are absolute..."): Says 8086 NEAR jumps are absolute. A same-segment NEAR JMP assembles to a 16-bit displacement counted from the address of the next instruction; it is relative, not absolute. Only the FAR JMP carries a full CS:IP absolute address (and indirect near jumps take the target from a register or memory). A student will wrongly think a NEAR jump stores a full offset.
- ch 5 [low] Section 1, conditional jump paragraph: JP means "jump if positive (S = 0)" on the 8085 but "jump if parity even (P = 1)" on the 8086. The chapter lists both meanings without warning that the same mnemonic flips meaning, and a student revising quickly can carry the 8085 meaning over to the 8086.
- ch 5 [low] Section 3, AJMP sentence: "keeps the upper 5 bits of PC" is ambiguous: those 5 bits come from the address of the instruction after the 2-byte AJMP, not from the AJMP's own address. An AJMP placed across a 2 KB boundary will not reach the page a student expects.
- ch 6 [high] Section 2 (CALL and RET), sentence on conditional forms: RC and RNC are not conditional CALL instructions on the 8085; they are conditional RET instructions (return if carry, return if no carry). Listing them beside CC and CNC as conditional calls is wrong, and the following sentence ('a call that fails its test pushes nothing') then wrongly describes them.
- ch 6 [high] Section 4 (Stack limits and overflow), the LXI SP / MOV SP sentence: The sentence says SP is pointed at the top of the reserved area and that 'each call and each push then eats into that area from the top downwards'. That is true for the 8085 but false for the 8051, where PUSH increments SP first, so the 8051 stack grows upward from the starting value (SP = 50H fills 51H, 52H, ...). The sentence contradicts the table in Section 1.
- ch 6 [low] Section 2 (CALL and RET), nested calls paragraph: For 'A calls B and B calls C' the stack holds two return addresses, not three. Three is correct only if A itself was called by something else.
- ch 6 [low] Worked example 1, steps 3 to 5: Section 2 says the push happens first and PC is loaded with the target afterwards, but the worked example loads PC with 2100H in step 3 and only pushes in steps 4 and 5. The final state is right, but the order contradicts the text a student has just read.
- ch 6 [low] Quiz Q3: 'CALL 2500H, stored at 2500H' uses the same address as both the target and the location of the CALL instruction, which is confusing; the answer silently assumes the CALL occupies 2500H to 2502H.
- ch 6 [low] Quiz Q2, answer: 'Nothing in the hardware forces the direction; the PUSH microcode sets it' reads as self-contradictory, because the microcode is hardware.
- ch 7 [high] Quiz Q4: The answer says that without reloading, the inner counter would execute zero times and add almost no inner delay. This contradicts the chapter's own DCR/JNZ count-down loop (and the 8051 DJNZ loop): at the start of the next outer pass the inner counter is 00H, and DCR 00H gives FFH, so the inner loop wraps and runs 256 times, not zero. The delay is wrong, not almost zero.
- ch 8 [high] Quiz Q7: The premise contradicts itself. Changing ORG in the source 'without reassembling' changes nothing — the object file stays exactly as before, the code still sits at 2000H and JMP 2500H still works. The answer then explains what happens after a reassembly, so the question and answer describe two different situations. A student cannot tell which case is being asked.
- ch 8 [low] Figure: The node label 'Object .hex' joins two different file types into one name, while Section 2 explains that an object file and a hex file are not the same thing.
- ch 8 [low] Section 2: 'It has no labels, so a simulator shows addresses only' is too absolute. Most assemblers also emit a symbol or listing file that a simulator or debugger can load to show label names next to addresses.
- ch 8 [low] Section 2, last paragraph: 'copied to the board by a programmer' can be read as a person rather than the device that burns the chip.
- ch 8 [low] Quiz Q5: JNZ at 2003H is 3 bytes, so it occupies 2003H-2005H; a target of 2005H is the last byte of the instruction itself. The bytes asked for are correct, but the example makes a student picture a jump into the middle of an instruction.
