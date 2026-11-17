# ec-embedded-u2: free-model run

- Book: `books/ece/ec-embedded/ec-embedded-u2.html`
- Status: ok
- Model calls so far: 30 (115,690 tokens in, 303,813 out), 6.6 minutes

## Checker

```
ec-embedded-u2.html: 7 chapters, 13004 words, 8 figures, 147 KB
OK
```

## For the reviewer

- chapter 4: the figure cannot be drawn: tree is too wide (6 leaves); use fewer leaves or shorter labels

## Reviewer notes (after any revision)

- ch 1 [high] Section 1, first paragraph: The paragraph says the classic 8051 and near-clones such as AT89S52 have 4 KB program memory, 128 bytes RAM, two timers and five interrupt sources. AT89S52 is an 8052-type part with 8 KB flash, 256 bytes RAM, three timers and six interrupt sources. The later paragraph even says 8052-type parts have 256 bytes and a third timer, so the text contradicts itself.
- ch 1 [high] Section 3, first paragraph: MOV A,P1 reads the pin state, not the port latch. Only read-modify-write instructions read the latch. Students will get the opposite rule for port input.
- ch 1 [high] Quiz Q4: PSW = 18H is binary 0001 1000, so RS1 = 1 and RS0 = 1. That selects bank 3, not bank 2. The stated base 10H and R5 address 15H are also wrong.
- ch 1 [low] Section 1 and Quiz Q3: The 8051 has separate program and data address spaces, but it is not pipelined and its external bus is shared/multiplexed. Instruction fetch and data read do not overlap in the classic core. Saying one bus and another and can therefore overlap overstates the architecture.
- ch 1 [low] Section 4, PSW bit list: PSW.1 is commonly the user flag F1, not reserved. Some variants leave it reserved, but standard 8051 tables name F1.
- ch 1 [low] Quiz Q7: The byte at 08H can also be read with indirect addressing by loading a pointer with 08H. Direct addressing is not the only way.
- ch 1 [low] Section 4, writing PSW: P is the parity flag and is updated by hardware. Writing 08H does not force P to 0 when ACC has odd parity, so clears every flag is not exact.
- ch 2 [high] Worked example 1, step 3: The example writes 21H into STATUS and then reads TO = 0 and PD = 0 from the written bits. TO (bit 4) and PD (bit 3) of STATUS are read-only on the PIC16F877A; a write to STATUS does not change them. After power-up both are 1, so writing 21H leaves the register at 0011 0001 (TO = 1, PD = 1), not 0010 0001.
- ch 2 [low] Figure caption and node labels: "STATUS 21H" and the node label "STATUS = 21H" read as if 21H were the address of the STATUS register. Section 2 correctly gives the address as 03H; 21H is only a value written into it in the worked example.
- ch 2 [low] Lead: "one 8-bit address field cannot reach all of it" clashes with Section 2, which says the direct address inside an instruction is 7 bits. A student meets 8-bit in the lead and 7-bit two paragraphs later and reads it as a contradiction.
- ch 2 [low] Exam traps, fourth bullet: "The 8-level stack holds return addresses for CALL only" is wrong on one point: an interrupt also pushes the return address onto the same 8-level stack when it is taken. A student may conclude interrupts do not touch the stack, which contradicts the 0004H vector explained in Section 2.
- ch 2 [low] Section 1, first paragraph: "the ALU ... takes one operand from the working register W and the other from a file register in data memory" leaves out the literal instructions (MOVLW, ADDLW, ANDLW, IORLW, XORLW, SUBLW, RETLW), where the second operand comes from the instruction word itself, not from data memory.
- ch 3 [low] Section 1: The ARM7TDMI name is unpacked as 'ARM7 core, Thumb, debug support and a multiplier'. The letters are T, D, M, I — the I (EmbeddedICE) is dropped and D and I are merged into one vague phrase.
- ch 3 [low] Section 1 (CPSR flags): 'C means carry or borrow' is loose. In ARM the C flag is the carry out of the ALU; after a subtraction C = 1 means no borrow, so a student may read C = 1 as 'a borrow happened'.
- ch 3 [low] Section 2 (System mode): 'An operating system uses it to run privileged code without a mode switch' is misleading — entering System mode is itself a mode switch. The point being made is that no register bank changes.
- ch 3 [low] Exam traps, fourth bullet: The wording is inverted and confusing: R13, R14 and R15 are exactly the hardware names; it is SP, LR and PC that are software conventions. A student can read this as saying R13–R15 are not defined by the architecture.
- ch 4 [high] Section 2, the sentence that defines the four flags after an S-form: It says 'C is the carry out of an addition or the borrow out of a subtraction'. This inverts the subtraction case. On ARM, C for a subtraction is the NOT of the borrow: C = 1 when no borrow is needed, C = 0 when a borrow occurs. As written, a student will get CS/CC, HI/LS and the unsigned-compare questions wrong, and the same wrong idea is repeated nowhere else but is not corrected later.
- ch 4 [low] Section 2, the sentence defining V: The rule given ('both inputs have the same sign and the result has the other sign') is the overflow rule for addition only. For a subtraction, V = 1 when the two inputs have different signs and the result sign differs from the sign of the first operand.
- ch 4 [low] Section 1, list of condition codes: HI, LS, GE, LT, GT and LE are named without their flag meanings, so a student cannot use them. They also depend on the C flag that Section 2 defines wrongly.
- ch 4 [low] Section 3, Exam trap 3 and Quiz Q7: 'The final value depends on the transfer order' is not the standard rule. In the ARM architecture, LDM with writeback and the base in the list makes the base value UNPREDICTABLE, and STM with writeback and the base in the list makes the stored value of the base UNKNOWN. It is not a defined order-dependent result.
- ch 4 [low] Section 3, the BX sentence: 'on older cores' suggests newer cores do not use bit 0 for state. Bit 0 of the BX target selects ARM or Thumb state on every core that supports ARM and Thumb states; on Thumb-only cores such as Cortex-M the bit must be 1 and an attempt to switch to ARM state faults.
- ch 4 [low] Beyond note: 'Cortex-M microcontrollers run Thumb-2 only' is not true for the whole family. Cortex-M0 and M0+ implement ARMv6-M, which is basically Thumb-1 plus a few 32-bit instructions, not full Thumb-2.
- ch 5 [high] Section 1, first paragraph after the five operand kinds: The text says 'Five operand kinds repeat across families' but then lists six kinds: immediate, register, direct, indirect, indexed and relative. The count is wrong.
- ch 5 [high] Section 3, PIC modes paragraph: PIC16F877A does not have a general PC-relative branch/call offset mode. GOTO and CALL use absolute 11-bit addresses with PCLATH page bits; conditional branches are skip instructions, not signed PC offsets.
- ch 5 [high] Section 3, PIC indirect addressing sentence: For PIC16F877A, indirect addressing uses the 8-bit FSR together with the IRP bit (STATUS<7>) to form the 9-bit data-memory address. Saying the access goes to the address in FSR omits IRP and is wrong for banks 2 and 3.
- ch 5 [low] Figure and worked example 1: The figure labels code memory as 0000H-0FFFH but then shows code byte 1000H = 7BH. 1000H is outside the basic on-chip 4 KB code memory; it can only be external code, which the figure does not mark.
- ch 5 [low] Section 1, terminology sentence: 'Pointer addressing' normally means indirect addressing, not indexed addressing. The sentence can make students confuse indexed (base+index) with indirect (pointer).
- ch 6 [high] Section 1, the # paragraph: It says that without # , '250 means the byte stored at internal RAM address 250'. On the 8051, direct addresses 80H–FFH are the special function register block, not the 128-byte internal RAM (00H–7FH). The number 250 is 0FAH, which is in SFR space and is not a defined SFR on the classic 8051, so the example points at a location that does not hold a normal RAM byte. A student learns the memory map wrongly.
- ch 6 [high] Section 3, the line below the delay formula: The arithmetic is printed as t_cyc = 12 ÷ (12 × 106) = 1 μs. As written, 12 × 106 = 1272, which gives 0.0094 s, not 1 μs. The intended number is 12 × 106 (ten to the power six), i.e. 12 MHz in Hz.
- ch 6 [low] Section 2, first paragraph after the 8051/PIC/ARM list: 'A loop is a counter, a body and a test. The 8051 does all three in one instruction: DJNZ R2,loop.' DJNZ does not contain the body. It combines the counter update, the test and the branch; the body is whatever instructions sit between the label and the DJNZ. As written, a student may think the work to be repeated is inside DJNZ.
- ch 6 [low] Section 3, register-versus-stack paragraph: 'Registers are quicker, the stack survives an interrupt that reuses the same registers.' The contrast is missing its joining word, so the sentence reads as two unrelated statements and the point (registers are faster, but volatile across an interrupt) is lost.
- ch 6 [low] Section 1, opening sentence: 'Every assembler, for every CPU, uses the same line layout' is too absolute. Field order, label placement and the comment character differ between assemblers (semicolon on 8051 tools, other characters elsewhere); the four-field idea is what is common.
- ch 6 [low] Lead paragraph: It says a C compiler cannot 'touch a named special function register byte'. C compilers for these chips do reach SFRs, for example Keil's sfr declarations or a volatile pointer at a fixed address. The real limitation is guaranteed cycle timing, not access to the register.
- ch 7 [high] worked example 1, steps 1 and 4: The powers of two are written without superscripts, so the text reads 'full-scale code = 210 - 1 = 1023' and 'Resolution = Vref ÷ 210 = 5 V ÷ 1024'. As printed, '210 - 1 = 1023' is arithmetically false and '5 V ÷ 210' equals 0.0238 V, not 0.00488 V. A student copying this line gets the wrong resolution.
- ch 7 [low] section 2, pseudo code: The '[shown output]' block is empty, but the text promises that the sketch 'prints the code'. The reader has no idea what appears on the serial monitor.
- ch 7 [low] section 3, last paragraph: 'see Unit 5' points to another unit with no link, so a student reading on a phone cannot jump to it, and the reference is not a proper chapter link.
