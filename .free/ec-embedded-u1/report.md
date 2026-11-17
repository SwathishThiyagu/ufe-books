# ec-embedded-u1: free-model run

- Book: `books/ece/ec-embedded/ec-embedded-u1.html`
- Status: ok
- Model calls so far: 30 (114,798 tokens in, 200,295 out), 6.4 minutes

## Checker

```
ec-embedded-u1.html: 7 chapters, 13573 words, 8 figures, 142 KB
OK
```

## For the reviewer

- chapter 2: the figure cannot be drawn: tree is too wide (8 leaves); use fewer leaves or shorter labels
- chapter 2: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [high] Section 1: The Apollo guidance computer had about 36,000 words of fixed (core-rope) memory plus about 2,000 words of working memory. Saying it flew on 'only a few thousand words of memory' understates the figure by roughly a factor of ten and is a wrong number.
- ch 1 [low] Figure: The edge from 'Signal conditioning' to 'Processor + memory' is labelled 'digitised input', but the signal is still analog at that point; the text itself says the processor does the digitising with its ADC.
- ch 1 [low] Lead and Section 3: 'The two ends of every embedded system' and 'Every embedded system touches the physical world at two ends' overstate the case. Many systems (set-top box, router, UPI soundbox) take their input from a network or a keypad, not a sensor, and some (a data logger) drive no actuator.
- ch 1 [low] Section 4 table, Banking row: The IRCTC ATVM is a railway ticketing machine, so grouping it under 'Banking' sits oddly with the rest of the table, and the same device is called a 'ticket machine' in the worked example.
- ch 1 [low] Quiz Q6, answer: The answer says the Wi-Fi radio 'fights the coin-cell and low-power target', but an electricity meter is mains powered and is never run from a coin cell, so the point is confused.
- ch 2 [high] Section 1 table vs worked example step 4: The complexity table lists 'Router' as a Medium-class example (16/32-bit MCU, tens of KB, small RTOS), but worked example step 4 classifies the bank-branch 4G router as Large (32/64-bit SoC, embedded Linux). A student sees the same device class in two different ways.
- ch 2 [high] Quiz Q4 answer: The answer uses 'a small 8-bit airbag controller' as the small-but-hard counterexample. Worked example step 5 and the dry-run table classify the airbag controller as Medium complexity (dedicated MCU with a tight control task). The chapter contradicts itself, and the pair small/medium for the same device will confuse a student.
- ch 2 [low] Section 2, paragraph before the bullet list: The line 'A tiny 8-bit microwave controller can be hard real-time' is asserted without a deadline, and a microwave oven that is late does not fail — it just cooks for the wrong time, which is firm or soft under the chapter's own definitions. As written it teaches the wrong example of hardness.
- ch 2 [low] Lead: 'A washing-machine controller and an airbag controller can both be tiny' conflicts with worked example step 5, which calls the airbag controller medium complexity. 'Tiny' is being used for physical size in one place and computing class in the other.
- ch 2 [low] Section 2, first paragraph: 'An airbag that fires after 20 ms too late' is muddled wording; it reads as if the airbag fires and then is late.
- ch 2 [low] Quiz Q3 answer: The answer calls a missed 2 ms paper feed 'hard real-time' because it causes a jam. A jam is recoverable and damages nothing, so under the chapter's own definitions this is firm (result worthless, no failure), not hard. Students will copy 'any miss that spoils the job = hard'.
- ch 2 [low] Section 3 and figure; Quiz Q1 answer: Section 3 and Q1 name three form classes (standalone, networked, mobile), but the figure's Form branch has only Standalone and Networked leaves. The figure therefore does not match the text it illustrates.
- ch 3 [high] Section 3, power budget sentence: It says to check the resulting watts against the battery's energy. Watts measure power and joules or watt-hours measure energy, so the units do not match and the comparison is invalid.
- ch 4 [high] Quiz Q1: The question asks for 'the four software layers', but the answer lists hardware as the bottom item. Hardware is not a software layer. The chapter itself defines the stack as hardware, drivers/BSP, middleware and application software, so only three of the four items are software. A student will either write a wrong fourth software layer or be marked down for including hardware.
- ch 4 [low] Worked example 1, step 1: The parts list gives the real-time clock, LCD and UART as separate items, but step 1 silently moves the RTC and LCD driver inside the MCU ('The MCU contains ... real-time clock, UART and LCD driver'). The example then lists the RTC both as an MCU block and as external. This is an unstated assumption, not a calculation error.
- ch 4 [low] Section 2, first paragraph: The text says 'the device driver, or board support package (BSP)', which makes the two terms equal. Standard usage treats the BSP as wider than drivers: it also holds startup code, clock and memory initialisation and the linker/memory layout. The worked example uses 'BSP layer' only for drivers, which reinforces the narrow meaning.
- ch 4 [low] Worked example 1, answer line: Part (a) asks for hardware blocks and external parts, and part (c) depends on them, but the answer line leaves out the push button and the 10 kΩ pull-up resistor from the hardware list.
- ch 5 [low] Section 2, bullet on separate buses, and Quiz Q3 answer: The text credits plain Harvard organisation with delivering 'an instruction and its two operands' in one cycle, and the Q3 answer says 'the two data operand fetches travel on different buses'. Plain Harvard gives one program bus and one data bus, so only one data operand per cycle. Fetching two operands (coefficient and sample) in the same cycle needs a second data bus or dual-ported data memory, which DSPs add on top of Harvard. A student may write the loose version in an exam.
- ch 5 [low] Lead: 'An SoC puts a complete system, radio included, on one die' reads as a definition, so a student will think every SoC must contain a radio. Many SoCs (a display controller chip, a motor-control SoC) have no radio at all. Section 3 itself only says a phone SoC has one.
- ch 5 [low] Section 1, second paragraph: The text gives 'an ARM Cortex-A in a phone' as the modern microprocessor example, but section 3 says the phone processor is an SoC. The same chip is used as an example of two different families, which confuses the very distinction the chapter draws.
- ch 6 [high] Section 3, last paragraph: The arithmetic does not match the wording. A 100 MHz clock gives a 10 ns cycle, and 'waits four cycles on every flash access' means 4 × 10 ns = 40 ns per access, which is 25 million instructions per second, not 20 million. The stated 20 M figure only comes out if the access takes five cycles (one transfer plus four wait states).
- ch 6 [low] Section 2, von Neumann paragraph: The bootloader example is misleading. Bootloaders that copy new firmware into flash are common on Harvard microcontrollers too (they use a special program-memory write instruction), so this does not illustrate anything specific to a shared address space. A student may conclude bootloaders need von Neumann memory.
- ch 6 [low] Section 2, Harvard paragraph: 'every DSP uses Harvard' is too absolute; several DSPs use modified Harvard or a single external memory with separate on-chip buses. The 'almost every' hedge used for microcontrollers is safer here too.
- ch 6 [low] Section 3, 'Read a datasheet this way': 'If every instruction is a fixed four bytes, the core is RISC' reads as a definition, and it contradicts the Beyond box, which notes that ARM Thumb-2 and compressed RISC-V mix 16-bit and 32-bit encodings.
- ch 7 [low] Figure and its caption: The caption says flash/ROM is 'the only level that keeps code without power', but the same stack puts NAND flash and an SD card below it, and Section 1 correctly says those are non-volatile too. A student will read the caption as a contradiction.
- ch 7 [low] Figure, item order against the side labels 'faster, costlier per bit' (top) and 'slower, cheaper per bit' (bottom): Flash/ROM is placed above DRAM, which under these labels claims that NOR flash random reads are faster than DRAM reads. In practice a DRAM read is faster (tens of nanoseconds) than a NOR flash random access, typically 70–120 ns. The stack mixes a volatility/role axis with a pure speed axis without saying so.
- ch 7 [low] Section 2, wear example: '1000 writes/s would wear a 10⁴-cycle block in about 10 s' silently assumes one block erase per write. A real logger fills a sector with many 4-byte samples before erasing, so the erase rate, and therefore the wear time, is smaller by the number of samples per block.
