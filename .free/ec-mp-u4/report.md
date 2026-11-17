# ec-mp-u4: free-model run

- Book: `books/ece/ec-mp/ec-mp-u4.html`
- Status: ok
- Model calls so far: 30 (120,739 tokens in, 256,638 out), 7.1 minutes

## Checker

```
ec-mp-u4.html: 7 chapters, 14118 words, 8 figures, 139 KB
OK
```

## For the reviewer

- chapter 7: a c program does not run (compile error: /tmp/tmp5_bwuzcd/p.c:1:10: fatal error: xc.h: No such file or dir)
- chapter 7: the figure cannot be drawn: note "LPM0 to LPM4" runs off the right edge; shorten it
- chapter 7: a c program does not run: compile error: /tmp/tmprlhg2rvl/p.c:1:10: fatal error: xc.h: No such file or directory
    1 | #include <xc.h>
      |          ^~~~~~
compilation terminated.

## Reviewer notes (after any revision)

- ch 1 [high] Section 3, memory map; Exam trap 1; Quiz Q6: The chapter presents addresses 80-FF as 'the upper 128 bytes of RAM' of the 8051, but the lead and the figure say the 8051 has only 128 bytes of data RAM (00-7F). The upper 128 bytes at 80-FF exist only on the 8052/8032 family; on a plain 8051, 80-FF is SFR space only. As written, trap 1 ('to read RAM byte 0x80 use @R0') and Q6 describe an 8052 as if it were the 8051, so the chapter contradicts itself.
- ch 1 [low] Section 1 and Section 3 (code fetch and PSEN): Saying 'a code fetch drives PSEN' and 'Code: 0000-0FFF, fetched with PSEN' is misleading. PSEN is activated only when code is fetched from external program memory. With EA high, fetches from the internal 4 KB ROM do not drive PSEN at all, and the chapter itself explains EA low/high in the traps.
- ch 1 [low] Exam traps, third bullet: 'Move SP (say to 30)' mixes radix. Everywhere else the chapter writes 0x30, and bare 30 reads as decimal 30 = 1EH, which is inside register bank 3 — the opposite of what the advice intends. A student following it literally corrupts a bank.
- ch 1 [low] Section 2, last paragraph: 'Some syllabi call this list the pin diagram and the register list below the SFR map. Only a few universities teach it pin by pin.' is vague and reads like filler; 'the register list below the SFR map' does not match anything in the chapter.
- ch 2 [low] Lead: The lead says that writing 1 to a pin lets 'a weak internal pull-up' raise it, stated for all four ports. P0 has no internal pull-up at all, so a student who reads only the lead will write 1 to P0 and still see a floating pin.
- ch 2 [low] Section 2, read-modify-write paragraph: 'so an external load that drags the pin slowly cannot be misread as the value the software intended' is garbled. The point of reading the latch is that the pin voltage may be degraded by the load, so the hardware ignores the pin and uses the value the software last wrote.
- ch 2 [low] Section 2 table, header row: The header says 'Instruction (port is destination)', but the first two rows (MOV A,P1, MOV C,P1.0, MOV 30H,P1, ANL A,P1, ADD A,P1) have the port as the source, not the destination, and read the pin. The header contradicts its own rows.
- ch 2 [low] Section 2, rule sentence after the table, and Quiz Q5 answer: The separating rule is given as 'the port is the destination of a logical or bit instruction', but the table itself lists INC P1, DEC P1 and DJNZ P1,rel as latch reads, and they are neither logical nor bit instructions. A student can conclude DJNZ P1,rel reads the pin.
- ch 2 [low] Exam traps, P0 bullet: 'an LED or gate on P0 with no resistor never goes high' clashes with the LED wiring taught in Section 1 (anode to +5 V through a resistor, cathode to the pin). That sink wiring works on P0 without any pull-up; only a pin that must source current or drive a logic input needs the resistor.
- ch 3 [high] Exam traps, bullet 2 (11.0592 MHz): The direction of the error is reversed. If you wrongly take one count as 1 µs when the crystal is 11.0592 MHz, the real machine cycle is 1.0851 µs, so the computed count of N = delay/1 µs gives an actual delay of N × 1.0851 µs. The delay produced is about 8.5% too long, not too short; the count taken is 8.5% too many.
- ch 3 [high] Exam traps, bullet 3 (reload = 65,536 − N): The claim that loading the count itself makes the timer 'overflow almost immediately' and the delay 'come out near zero' is false in general. Loading N counts means the timer runs 65,536 − N counts. In this chapter's own 50 ms example, loading 50,000 gives 15,536 counts = 15.536 ms, not near zero; and for any N below 32,768 the delay becomes longer than intended, not shorter.
- ch 3 [low] Section 3, code block, [shown output]: The shown output for the program is left empty, so the reader sees no result to check the code against.
- ch 3 [low] Section 2, mode table, Mode 3 row: The row says only what Timer 0 does in mode 3. It does not say that Timer 1 in mode 3 simply stops and holds its count, which is the fact students most often ask about.
- ch 4 [high] Section 4, polling transmit pseudo code: The wait instruction JNB TI, TX jumps back to the label TX, which sits on MOV SBUF, A. Until TI sets, the loop re-executes MOV SBUF, A again and again, overwriting the transmit register with the same byte. The frame can be corrupted and the listing does not show the intended 'write once, then wait' behaviour. (The RX routine is fine, because there the label is on the JNB instruction itself.)
- ch 4 [high] Quiz Q6, answer explanation: The last sentence says 'The SMOD divide-by-2 halves the overflow rate seen by the UART, which corrects the factor.' This is the wrong direction: SMOD = 1 makes the UART divide by 16 instead of 32, so it doubles the baud rate. Halving the rate would give 1200 baud, not the 2400 bit/s the answer computes, and it contradicts Section 2 ('Setting SMOD = 1 doubles the baud rate').
- ch 4 [low] Section 1, SBUF paragraph: 'Hardware sets TI when the stop bit has left' is slightly off. In mode 1 the UART sets TI at the start of the stop bit, not after it has been shifted out completely.
- ch 4 [low] Quiz Q5, answer explanation: The closing reason 'because 12 MHz is not a whole multiple of the standard rates' is misleading: 12 MHz is an exact multiple of 2400 (5000 times). The rounding error comes from the fixed dividers, because 12,000,000 / (12 × 32 × 2400) is not a whole number.
- ch 4 [low] Section 4, after the assembly listing: An empty '[shown output]' block appears after the pseudo code with no output listed, which looks like a missing item a student may search for.
- ch 5 [low] Quiz Q6 answer: A 12-byte routine starting at 000BH ends at 0016H, so it overwrites four bytes, 0013H to 0016H, not just 0013H and 0014H. The conclusion is right but the address detail is wrong and would mislead a student counting bytes.
- ch 5 [low] Figure caption and spec: The caption explains only the accent and live marks on the Vector row; the spec also puts a 'next' mark on the Source row at index 1 (T0), which the caption never mentions, so the reader cannot tell what that highlight means.
- ch 5 [low] Section 2, priority: The section explains which source wins when two requests arrive together, but never states the pre-emption rule: a high-priority request interrupts a running low-priority ISR, while a same-priority request must wait. Interrupt programming depends on this.
- ch 6 [high] Section 3, Timer 0 interrupt program: The ISR only does ticks++ and never reloads TH0/TL0. In mode 1 (TMOD = 0x01, 16-bit, no auto-reload) the timer counts on from 0x0000 after overflow, so only the first interval is 1000 counts; every later interrupt comes after 65536 counts. The example therefore does not give regular timing, which is exactly what students will copy.
- ch 6 [low] Section 3, port program: Writing P1 = 0xFF to make P1.0 an input also turns every other pin of P1 into an input, wiping the outputs just set by P1 = 0x0F. A student reading only this line will corrupt the other pins.
- ch 6 [low] Exam traps, sbit/sfr bullet: "Mixing them causes address errors" is vague and misses the real restriction: sbit works only for SFRs whose byte address is bit-addressable (address ending in 0 or 8). TMOD (0x89) and SBUF (0x99) cannot have an sbit name.
- ch 6 [low] Section 3, memory models: "Small code and small data usually beat large models on an 8051 because code space and stack are limited." The data model does not consume program code space in that sense; the real cost of the large model is 16-bit pointers, extra pointer arithmetic and slow external-memory (MOVX) cycles.
- ch 7 [high] Section 4, final paragraph: "only the MSP430 offers named sleep modes with sub-microsecond wake-up" contradicts the chapter's own table, which lists 8051 Idle/Power-down and PIC18 Sleep as named modes. The wake-up figure is also overstated: waking from LPM3 (DCO off) takes a few microseconds on real parts; only LPM0 wake-up is immediate.
- ch 7 [low] Lead: "The PIC keeps an 8-bit data path and fetches 16-bit instruction words from flash, so it needs banked RAM" gives the wrong cause. Banking comes from the 8-bit address field inside each instruction, not from the 8-bit data path or the flash width. Section 2 states the correct reason, so the lead contradicts it.
- ch 7 [low] Section 1: "Every instruction is 16 bits wide" is too strong. On the PIC18, GOTO, CALL, MOVFF and LFSR occupy two 16-bit words. The word count 16,384 is still correct because flash is organised as 16-bit words, but a student will be surprised when GOTO eats two words.
- ch 7 [low] Section 2, C code: pattern[] and i are declared after the TRISB and PORTB statements. Older XC8 projects compile in C90 mode, where all declarations must come before the first statement, so this listing will not build there.
- ch 7 [low] Section 3: The constant generator R3 is said to produce "0, 1, 2, −1 or 4". The standard set is 0, 1, 2, 4, 8 and −1; 8 is missing, so the list is incomplete as written.
- ch 7 [low] Section 3, clock paragraph: "A digitally controlled oscillator (DCO) starts in under a microsecond" is not supported: data sheets quote the DCO wake-up time in the microsecond range (a few microseconds), and the chapter gives no part number.
- ch 7 [low] Section 4, first paragraph: "one instruction adds two bytes" is unclear; a student may read it as a 16-bit add handling two memory bytes at once.
- ch 7 [low] Quiz Q4: The answer 8 bits of opcode is only the arithmetic of this made-up question. The real MSP430 dual-operand format has a 4-bit opcode, two 4-bit register fields, and 4 remaining bits for the Ad, B/W and As addressing-mode fields, so a student may carry away the false idea that the MSP430 has an 8-bit opcode.
