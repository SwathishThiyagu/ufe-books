# ec-mp-u1: free-model run

- Book: `books/ece/ec-mp/ec-mp-u1.html`
- Status: ok
- Model calls so far: 26 (88,707 tokens in, 155,132 out), 5.5 minutes

## Checker

```
ec-mp-u1.html: 6 chapters, 12285 words, 7 figures, 130 KB
OK
```

## For the reviewer

- chapter 4: the figure cannot be drawn: tree is too wide (6 leaves); use fewer leaves or shorter labels
- chapter 1: the figure cannot be drawn: tree is too wide (6 leaves); use fewer leaves or shorter labels

## Reviewer notes (after any revision)

- ch 1 [low] Section 2, 8-bit bullet: The bullet pairs the 8080 and the 8085 and says they 'powered the first personal computers'. The first hobby/personal machines (Altair 8800, IMSAI) used the 8080; the 8085 arrived in 1976 and is not the chip of the first personal computers, so a student may learn the wrong chip-to-machine link.
- ch 1 [low] Section 2 table, 16-bit row: The table lists the 8086 (1978) with the job 'IBM PC', but the text itself correctly says the 8088, the 8086's 8-bit-bus twin, went into the first IBM PC. Table and text contradict each other.
- ch 1 [low] Section 2, 32-bit bullet and table row: 'The Intel 80386 in 1985, which brought protected memory' overstates it: protected mode first appeared on the 80286 in 1982. The 80386's contribution was 32-bit protected mode with paging and flat memory, which is what let real multitasking operating systems run.
- ch 1 [low] Beyond: 'a ₹-scale sensor node' is unclear; the reader cannot tell whether it means a cheap node or a node costing a few rupees.
- ch 2 [high] worked example 1, steps 3 and 4: The powers of two have lost their superscripts: the text reads "8192 bytes = 213 bytes" and "2048 bytes = 211 bytes". As printed these are wrong numbers (213 bytes and 211 bytes), and the following conclusion of 13 and 11 address lines looks unjustified.
- ch 2 [high] section 2, The three buses: "If the address bus has n lines, the CPU can select 2n distinct addresses" reads as 2 × n, which is wrong; the formula block two lines later correctly shows N = 2ⁿ, so the two statements contradict each other.
- ch 2 [low] worked example 1, question line: "the largest byte it can transfer in one bus cycle" is unclear: a byte has a fixed size, so there is no largest byte.
- ch 2 [low] section 2, The three buses: The chapter states that the address bus is unidirectional but never states the direction of the data bus, which is a standard exam point.
- ch 2 [low] section 3, end of section: Cross-references ("covered in Unit 2", "are in Chapter 1.5") are plain text, so a reader on a phone cannot jump to them and the chapter id is not shown.
- ch 3 [high] Section 2, Indirect addressing: "If the byte at 2000h contains 3050h" is impossible: one byte holds 8 bits, so it cannot contain the 16-bit value 3050h. A student copying this will think a pointer fits in one byte.
- ch 3 [low] Section 2, Direct addressing: The mnemonics in this section are 8051-style (MOV A, @R0; MOV R1, #25h), but 8051 direct addressing reaches only on-chip addresses 00h–FFh. MOV A, 2000h is not valid 8051 code, and the chapter later calls the 8051 a Harvard microcontroller, so students may take it as real 8051 syntax.
- ch 4 [low] Worked example 1, opening line and step 1: The example opens with 'A CISC CPU has 120 instructions', but 120 is the size of the instruction set and is never used. The steps then use IC = 10⁶, which is the dynamic instruction count of the program. A student can easily think the 120 and the 10⁶ are the same quantity, or wonder where 120 went.
- ch 4 [low] Worked example 1 step 6, and Quiz Q5 answer: The division is written as '1.68 × 10⁶ ÷ 4 × 10⁶' and '3.22 × 10⁶ ÷ 6 × 10⁶'. Read left to right this means divide by 4 and then multiply by 10⁶, which gives 4.2 × 10⁵, not 0.42. The intended grouping is hidden.
- ch 4 [low] Quiz Q2 answer (and the table row on instruction length): The answer says 'ARM is RISC: fixed 4-byte instructions' without the ARM-state qualifier used in Section 1, and the table says 'fixed, 4 bytes'. ARM also has 2-byte Thumb instructions, so the unqualified statement is not strictly true.
- ch 5 [low] Figure caption (Section 3): The word 'stack' is used for the hierarchy diagram, but the same word earlier means the call stack in RAM. A student can think the diagram shows the push/pop stack.
- ch 5 [low] Section 3, first paragraph: 'A common layout puts ROM at low addresses for reset code' is true for the 8085 (reset at 0000H) but not universal: the 8086 starts at FFFF0H, so ROM often sits at the top of the map instead.
- ch 5 [low] Exam traps, trap 2: 'A 2 KB chip is 0800H bytes' mixes a hex count with the word 'bytes' and reads as if 0800H were a size in bytes rather than the hex form of 2048.
- ch 5 [low] Worked example 1, step 6: Step 6 ('The RAM end 27FFH is 10239 in decimal') does not move the solution forward; it only invites confusion with step 7's count of 10240.
- ch 6 [high] Figure: The caption contradicts the timeline it describes. In the gantt, I1 is in MEM during cycles 3–4, the same cycles in which I4 is in IF; I1 reaches WB only in cycles 4–5, when I4 is already in ID. A student reading the caption against the picture sees a mismatch.
- ch 6 [low] Lead: 'Processors from the 8086 to ARM use pipelining' suggests the 8086 has a classic multi-stage pipeline. The 8086 only prefetches instructions into a 6-byte queue while the execution unit works — a limited two-stage overlap, not a k-stage pipeline.
- ch 6 [low] Lead: 'it is why a phone opens an app while still fetching data from memory' is vague and overstates the idea; opening an app depends on many things, and pipelining only overlaps instruction steps.
- ch 6 [low] Section 3: 'See Unit 6 for the ARM pipeline' is a bare text reference; house style uses a cross-chapter link so a phone reader can tap through.
