# ec-mp-u6: free-model run

- Book: `books/ece/ec-mp/ec-mp-u6.html`
- Status: ok
- Model calls so far: 36 (126,481 tokens in, 254,432 out), 7.8 minutes

## Checker

```
ec-mp-u6.html: 8 chapters, 13355 words, 9 figures, 147 KB
OK
```

## For the reviewer

- chapter 7: the figure cannot be drawn: tree is too wide (6 leaves); use fewer leaves or shorter labels
- chapter 1: the figure cannot be drawn: note "microcontroller" runs off the right edge; shorten it
- chapter 7: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [high] Worked example 2, step 4: The step says 'the last 98 retire one per clock', but after the first instruction fills 3 stages there are 99 instructions left (instructions 2 to 100), so the count is 3 + 99 = 102. The stated 98 contradicts the 102 clocks in step 2 and the final answer.
- ch 1 [high] Section 2, pipeline stage list (LDR/STR bullet): It says the memory access for LDR/STR 'takes extra clocks'. In the classic 3-stage ARM pipeline the address is computed and the data transfer completed inside the execute stage, so a load or store takes one clock when memory has zero wait states. Only slow memory (wait states) stretches that cycle.
- ch 1 [low] Quiz Q6, answer: The last sentence ('It also keeps instruction encoding short enough for condition codes') does not follow: the load-store rule has nothing to do with making room for the condition-code field, so a student will look for a link that is not there.
- ch 1 [low] Section 2, data-flow description: It says data-processing instructions 'take one or two registers'. A typical ARM data-processing instruction reads two source registers (three in some forms) and writes one destination register, so the count is misleading.
- ch 1 [low] Section 4 and the first exam trap: Saying flatly that 'ARM cores are bi-endian' and that 'the core is bi-endian' overstates it: some small Cortex-M cores are little-endian only, and the big-endian option exists on other cores only when the memory system is configured for it (BE8).
- ch 2 [low] Section 3, paragraph on flag updates: The sentence lists CMP and TST among instructions that update flags "only if they have the S suffix". CMP, CMN, TST and TEQ have no separate non-flag form: they always update the flags, and the S bit is implied in their encoding. A student may look for a "CMPS" instruction that does not exist.
- ch 2 [low] Section 1, calling convention sentence: "R0-R3 pass the first four arguments and return values" can be read as four return values. Also R0-R3 are scratch, so a callee may destroy them.
- ch 2 [low] Section 1, calling convention sentence: "R4-R11 hold local variables" is not exact under the standard ARM calling convention: R9 is a platform register that a given platform may reserve, and R12 is the scratch register (IP) that linker veneers may destroy.
- ch 2 [low] Figure caption/notes: The note on PC says "next instruction", but Section 2 states that a read of R15 gives the current instruction's address plus 8 in ARM state. "Next instruction" suggests current + 4 and contradicts the rule just taught.
- ch 2 [low] Quiz Q2 answer: "Thumb uses 2-byte instructions and an offset of 4" is only true of classic 16-bit Thumb. Thumb-2 also has 32-bit instructions, yet a read of R15 still returns current + 4, so the reasoning by instruction size misleads.
- ch 2 [low] Lead: The lead says every ARM program uses the sixteen registers and "the CPSR", and names a Cortex-M motor controller. Cortex-M cores expose xPSR plus PRIMASK, FAULTMASK and BASEPRI, with no ARM/Thumb state bit and no User/FIQ/IRQ/Supervisor mode encoding of the classic kind.
- ch 3 [high] Section 1, paragraph starting 'Each privileged mode has its own R13 (SP)...': It says every privileged mode has its own SPSR. That is false for System mode. System is privileged but shares the User register bank (R13_usr, R14_usr) and has no SPSR of its own, so the rule as written contradicts standard ARM documentation and also contradicts the chapter's own next sentence about System mode.
- ch 3 [low] Section 2 and Exam traps, return rules: The return rules list IRQ/FIQ (#4), data abort (#8) and SWI (MOVS PC, LR), but never give prefetch abort. A student can read the trap 'IRQ and FIQ return subtract 4 bytes' and conclude that only those two exceptions use #4, so the prefetch abort case is left untested and unclear.
- ch 4 [high] Section 1, first paragraph: The barrel shifter is put on the result path: 'read one or two registers, pass the result through the barrel shifter, and write a register'. In ARM the shifter sits on the Operand2 input of the ALU only, before the operation; the ALU result goes straight to Rd.
- ch 4 [low] Section 1, first paragraph: The sentence says data processing instructions 'write a register', but CMP (and TST, TEQ) are in this class and write only the flags, not a register. The same paragraph later says CMP writes only flags, so a student meets a contradiction.
- ch 4 [low] Section 3, condition field paragraph: 'Every 32-bit ARM instruction has a 4-bit condition field' contradicts the lead ('Almost every instruction') and is not true from ARMv5T onward, where the encoding cond = 1111 is used for the unconditional instruction space (BLX, PLD, and later others).
- ch 4 [low] Section 3, branch offsets paragraph: 'The assembler calculates the distance from the branch instruction to the label' hides the pipeline detail that matters in exams: the offset is added to the PC, and in ARM state PC reads as the address of the branch plus 8.
- ch 4 [low] Section 2, byte forms sentence: Only byte forms LDRB and STRB are named. Halfword access (LDRH, STRH, LDRSB, LDRSH) is standard and often asked, and a student may think memory access is only word or byte.
- ch 5 [high] Section 1, last part of the paragraph on the T bit: It says 'In Thumb state the PC still points to the current instruction'. On the ARM7TDMI, reading the PC does not give the address of the current instruction. Due to the 3-stage pipeline, the PC reads as current instruction address + 4 in Thumb state and + 8 in ARM state. A student who writes 'PC = current instruction' in an exam answer loses marks, and the wrong idea breaks the explanation of PC-relative loads and branch offsets.
- ch 5 [low] Section 1 and Section 3: CPSR, PC and LR appear without being spelled out on first use. A reader whose English is weak has to guess what the abbreviations stand for.
- ch 5 [low] Quiz Q6: Two small points. First, 2000 bytes is 2 kB in decimal but about 1.95 KiB if 1 KB is taken as 1024 bytes, so the unit should be stated. Second, the question assumes ARM and Thumb need the same number of instructions, which contradicts Section 2 (a Thumb routine often needs more instructions). The arithmetic itself is right.
- ch 6 [high] Section 3, paragraph on calling C from assembly: The paragraph says 'Save LR and any live R4-R11 before that call, because C may change R0-R3 and LR.' Saving R4-R11 is not needed for a C call: under AAPCS the C function preserves R4-R11. The sentence therefore contradicts the very next paragraph ('C functions preserve R4-R11, so assembly can keep a loop counter in R5 across a C call') and teaches students the wrong rule.
- ch 6 [low] Section 2, after the code listing: 'LR is saved because the subroutine uses the stack' gives the wrong reason. SUM never calls another function, so LR is not clobbered; LR is pushed so that POP {R4, PC} can load the return address into PC (and so the frame is 8 bytes).
- ch 6 [low] Figure and worked example 1, steps 3-4: The figure and the worked example say R1 is added and decremented ('R0=R0+R1', 'decrement R1', 'Use SUBS and BNE to repeat while R1 is not zero'), but the code first copies N into R4 and decrements R4, leaving R1 unchanged. A student tracing the figure against the code sees two different loops. The figure also omits the N ≤ 0 test that the code does with CMP/BLE.
- ch 6 [low] Section 2 and worked example 1, code listing / shown output: The listing is preceded by a bare '[text code]' marker and followed by '[shown output]' with nothing shown, so the reader never sees the result of the example printed.
- ch 6 [low] Quiz Q7: The answer 'Save R5 and LR; restore them after the call' suggests R5 is saved because of the C call, which is not the case (C preserves R4-R11). It repeats the confusion created in Section 3.
- ch 7 [high] Section 2, table row Cortex-M0/M0+, Exam trap 5: The text says M0 and M0+ run a plain 16-bit Thumb set and 'do not execute Thumb-2's 32-bit instructions'. ARMv6-M, the architecture of both cores, is a subset of Thumb-2 that contains mostly 16-bit instructions plus a small number of 32-bit encodings (BL, MSR, MRS, DMB, DSB, ISB). So the absolute claim is wrong, and a student who repeats it loses marks.
- ch 7 [low] Lead: 'Both share the ARM programmer's model, so one C compiler serves either' can be read as saying the same compiled program runs on both. It does not; the compiler must be given a different target (for example -mcpu=arm7tdmi against -mcpu=cortex-m3).
- ch 7 [low] Section 1, paragraph 2: 'arithmetic works on registers R0 to R15' lists all sixteen registers without saying that R13, R14 and R15 are the stack pointer, link register and program counter. A beginner may treat R15 as an ordinary operand register in every instruction.
- ch 7 [low] Quiz Q4 answer: 'so the control loop timing can be calculated instead of measured' is vague about what fixed latency buys. The examiner looks for determinism, that is, the worst-case response time is known in advance.
- ch 8 [high] Section 2, DVFS paragraph: 'Lower f at the same V saves little energy per operation' is wrong. Dynamic energy per operation is E_op = α × C × V², which does not contain f at all. Lowering f at constant V reduces power (P = αCV²f) but saves no switching energy per operation, and can raise total energy because the block runs longer and leaks for longer.
- ch 8 [low] Quiz Q1 answer: 'Stop its clock until the interrupt arrives' is stated as a guarantee. WFI is only a hint: the architecture says execution suspends until an interrupt is taken, and the chip decides what low-power state (if any) is entered. If an interrupt is already pending, WFI completes immediately.
- ch 8 [low] Worked example 1, step 4 and answer: The charge is left in mA·ms only. Students cannot judge whether 200.45 mA·ms is a sane number, and the unit looks unusual on an answer sheet.
- ch 8 [low] Quiz Q4 answer: 'Reduces both switching energy and frequency' is muddled: cutting frequency does not itself save energy. The saving comes from V², and the frequency cut is what keeps the circuit stable at the lower V.
