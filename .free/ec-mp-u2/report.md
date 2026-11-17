# ec-mp-u2: free-model run

- Book: `books/ece/ec-mp/ec-mp-u2.html`
- Status: ok
- Model calls so far: 18 (65,207 tokens in, 159,931 out), 4.4 minutes

## Checker

```
ec-mp-u2.html: 6 chapters, 11820 words, 7 figures, 133 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 3 pin list (and repeated in Quiz Q7): The pin-number-to-signal order is reversed. Pin 12 is AD0 and pin 19 is AD7; pin 21 is A8 and pin 28 is A15. Writing 'Pins 12-19: AD7-AD0' and 'Pins 21-28: A15-A8' reads as if pin 12 = AD7 and pin 21 = A15, which would make a student wire the bus backwards.
- ch 1 [low] Figure spec: The diagram shows a separate 'Data buffer' with note 'D7-D0', but the 8085 has no separate D7-D0 pins: the low address and data share AD7-AD0. The figure contradicts Section 1 ('address/data buffer carries the low address byte AD7-AD0, then data') and can make a student think there is a dedicated data bus.
- ch 1 [low] Section 2 flags; Exam traps: AC is defined only as the carry from bit 3 to bit 4. In subtraction the same flag is set by a borrow. Students who only see the addition wording get confused by SUB and by DAA after subtraction.
- ch 2 [high] Section 3, the byte-count rule: The rule states flatly that a three-byte instruction takes 4 + 3 + 3 = 10 T. That holds for JMP/LXI but not for the common three-byte instructions that also touch memory or the stack. LDA 2050H and STA 2050H need a fourth machine cycle (memory read or memory write), so they take 13 T, and CALL 2000H pushes the return address, so it takes 18 T. The chapter lists only two corrections, so a student will answer 10 T for LDA and lose marks.
- ch 2 [low] Section 2, opening paragraph: The sentence says all five machine cycles begin with the high address byte on A15-A8 and the low address byte on AD7-AD0. In the two I/O cycles A15-A8 does not carry a high address byte: the same 8-bit port address is placed on both A15-A8 and AD7-AD0, as the I/O bullets later say. A student meets two different statements about the same wires.
- ch 3 [high] Lead (opening paragraph): It says every later x86 chip still carries 'this 20-bit address scheme'. Later x86 chips do not use a 20-bit physical address: the 80286 uses 24 bits, the 80386 and later use 32 bits, and x86-64 uses 64 bits. A student will write in the exam that a modern PC has a 1 MB address space.
- ch 3 [low] Section 4, opening line: It says 'Learn the pins in six groups', but only five bullets follow: address and data, control and status, interrupts, DMA, clock and power.
- ch 3 [low] Section 4: RESET and TEST are missing from the signal description, though a signal-description question almost always asks about RESET (it forces CS = FFFFH, IP = 0000H, so the first fetch is from FFFF0H).
- ch 3 [low] Section 2, FLAGS description: CF is defined as 'carry out of bit 15'. That is right for 16-bit operations but wrong for 8-bit operations, where the carry out of bit 7 is the one recorded.
- ch 3 [low] Quiz Q5: The answer says the BIU 'loads CS and IP from the jump target'. For a near (intra-segment) JMP only IP is loaded; CS changes only for a far jump.
- ch 3 [low] Exam traps, first bullet: The arithmetic in the 'decimal 10' trap is muddled: 1234H = 4660 decimal, so 1234H × 10 decimal is 46600 = B608H, not 3034H. The 3034H figure comes from reading the hex digits as decimal digits, which is a third mistake mixed into the same bullet.
- ch 4 [low] Section 2, data bus paragraph: The sentence says the 8086 drives 'RD or WR to set the direction of the transfer'. Direction is set by DT/R, as the previous sentence itself says. RD and WR only tell memory or I/O whether the cycle is a read or a write, so a student can end up with two conflicting rules for DT/R.
- ch 4 [low] Section 1 and Section 4 table, typical use: The text says maximum mode 'exists for systems with a coprocessor, a DMA controller, or more than one bus master'. A single DMA controller can take the bus in minimum mode too, using HOLD and HLDA, so the rule as written is not a clean test between modes.
- ch 4 [low] Figure (edge cpu to clk): The arrow labelled 'timing' points from the 8086 to the 8284, which suggests the CPU feeds the clock generator. The 8284 supplies CLK, READY and RESET to the CPU.
- ch 4 [low] Figure (latch note and control bus note): The latch node is labelled 'A19-A16' and the edge from it to memory is labelled 'A19-A16', as if only the upper four address bits are latched; in fact two 8282 chips latch A0-A15 as well. The control bus node is labelled 'RD WR M/IO', which are minimum-mode names only.
- ch 4 [low] Section 2, first paragraph on the 8284: The text says the 8284 'divides the crystal frequency' but never gives the factor, which exam answers usually expect.
- ch 5 [high] Section 2, first paragraph ("A simple decoder is an AND gate..." ): The gate described contradicts its stated output. An AND gate whose inputs are address lines (some inverted) goes HIGH exactly when the address pattern matches. That is an active-HIGH select, not active-low CS. Driving an active-low CS needs a NAND gate, or an AND gate followed by an inverter.
- ch 5 [low] Section 2, third bullet (8086): "A19-A0 and BHE/A0 select banks" is compressed and a student can read it as if the whole address bus selects banks. It is BHE and A0 that choose the byte bank.
- ch 5 [low] Section 3, fourth bullet: "the memory-read control, RD when IO/M is low" is not a signal; RD alone is low for I/O reads too, so a student may wire RD straight to OE.
- ch 5 [low] Quiz Q4: The setup is muddled. Partial decoding normally shows one chip at many ranges (mirroring); here two chips are both placed in the identical range, which is a wiring clash rather than a partial-decoding example.
- ch 6 [high] Figure (REP MOVSB loop) and its aria text: The figure shows MOVSB as 'Copy [SI] to AL' then 'AL to [DI]'. MOVSB is a memory-to-memory byte move; it does not pass the byte through AL, and showing AL here teaches the wrong internal model (LODS/STOS are the instructions that use AL/AX). The figure also routes DF = 1 straight to 'Decrement SI and DI', skipping the copy and store, which would mean nothing is copied when DF = 1. All three nodes and the aria description repeat this wrong path.
- ch 6 [low] Quiz Q4: The answer says only that [SP] holds 'the address of the next instruction'. The question gives CS:IP = 1000H:0200H and asks what is on the stack, so the student should produce the actual return offset. A near CALL is a 3-byte instruction, so the return IP is 0203H, not 0200H.
- ch 6 [low] Section 1: CMPS is described as comparing '[SI] with [DI]' and SCAS as comparing AL or AX with '[DI]'. This hides which segment each operand uses: CMPS compares [DS:SI] with [ES:DI], and SCAS always compares AL/AX with [ES:DI]. DI can never be paired with DS, which is exactly the trap the chapter itself warns about later.
- ch 6 [low] Lead: 'some syllabi call this advanced instructions' is ungrammatical and unclear — a student cannot tell what is being named.
