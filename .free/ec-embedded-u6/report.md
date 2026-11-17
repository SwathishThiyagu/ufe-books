# ec-embedded-u6: free-model run

- Book: `books/ece/ec-embedded/ec-embedded-u6.html`
- Status: ok
- Model calls so far: 27 (93,214 tokens in, 191,266 out), 4.0 minutes

## Checker

```
ec-embedded-u6.html: 9 chapters, 15765 words, 10 figures, 172 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Figure 'Port bit masking': The rows are written MSB-first, so the leftmost cell of 10100101 is bit 7. But the figure is drawn with show_index and index_from 0, so the columns are labelled 0 to 7 from the left. The label '4' therefore sits under a cell that is really bit 3, and the label '2' under a cell that is really bit 5. A student reading the index labels concludes bit 0 is the leftmost bit, which is exactly what the exam trap warns against.
- ch 1 [low] Section 2, first paragraph: The sentence 'For bit n, 1  has a single 1 at position n' has a missing shift expression, so the sentence as printed is false (the number 1 has its only 1 at position 0).
- ch 1 [low] Exam traps, second bullet, and Quiz Q6: Both write 'p |= 0x08 & 0x20', but everywhere else p is the pointer (volatile uint8_t *p) and the register is *p. As written, p |= ... increments the pointer, not the port.
- ch 1 [low] Section 2, third paragraph: 'Both do read-modify-write' is not accurate for 8051 sbit access. Writing an sbit such as LED = 1 compiles to a single-bit instruction (SETB/CLR) on the bit-addressable port latch; it is not a read-modify-write of the whole byte. Read-modify-write happens only when C writes the whole port, as in P1 |= 0x08.
- ch 1 [low] Lead: The lead says Embedded C 'adds fixed-width integer types'. The types uint8_t, int16_t and uint32_t are standard C (C99, <stdint.h>), not an embedded extension; what embedded code adds is their use for register layouts plus volatile, masks and ISR syntax.
- ch 2 [low] Section 1: The GCC name is explained as 'arm-none-eabi-gcc', where 'none' is said to mean 'no operating system'. In the standard machine-vendor-OS triplet, 'none' fills the vendor slot (no vendor), and the absence of an OS is shown by 'eabi' standing in for an OS name such as 'linux'. A student can carry the wrong field meaning into an exam answer.
- ch 2 [low] Section 2: The chapter says .text holds 'code and constants'. Read-only constants are normally placed in a separate .rodata section, which the linker script then puts in flash alongside .text. Calling .text the home of constants is loose and can mislead a student reading a real map file.
- ch 2 [low] Section 4: The cross-reference 'See Chapter 6.3 for that trade-off' is plain text, while other chapters are meant to be linked so a phone reader can jump to them.
- ch 3 [high] Section 3, first sentence of 'Real-time limits matter' (the same claim appears in Quiz Q4 answer): The text says 'Halting the CPU freezes timers'. Halting the core stops instruction execution, but on most MCUs the on-chip peripherals, timers and watchdog keep counting unless the debugger explicitly sets freeze bits. This is exactly why the chapter's own trap says a halt 'can trigger the watchdog'; the two statements contradict each other, and a student will repeat the wrong one.
- ch 3 [low] Section 2, first paragraph: 'it connects to the target socket or a debug header' mixes the two tools. An emulator pod normally plugs into the MCU socket or a dedicated emulation header; reaching the chip through the ordinary debug header is the in-circuit debugger's route, not the emulator's. The chapter has just drawn that distinction and then blurs it.
- ch 3 [low] Section 2, on-chip debug paragraph: 'Some syllabi call the on-chip block the debug access port' is loose. The debug access port (DAP) is one specific block inside ARM CoreSight that lets the probe reach memory and peripherals; the whole on-chip debug logic is not called the DAP.
- ch 4 [high] Section 3, integration paragraph: "Bottom-up integration starts at the leaf drivers and drives them with test programs" confuses the two standard integration aids. A driver is the test program, not a module; bottom-up integration starts at the lowest-level (leaf) modules and tests them using drivers, while stubs are used in top-down integration. As written, a student would write "leaf drivers" in the exam and lose marks.
- ch 4 [low] Section 3, first paragraph, and Exam trap 3: Verification is defined as checking that "each artifact match[es] the stage before it". That holds for a strict waterfall handover, but it contradicts the V-model rule given in Section 2, where a system test verifies against the specification written several stages earlier and an acceptance test verifies against the requirements. The definition is too narrow.
- ch 4 [low] Section 1, formula box: T_total = sum of the stage weeks is only true when the stages run one after another. On a real Gantt chart with overlap the sum double-counts the overlapping weeks, and the formula says nothing about this. It also leaves out maintenance without saying so, while the stage list above it has maintenance as a stage.
- ch 4 [low] Figure, architecture node: The figure note on architecture reads "design 3 weeks", but the worked example gives specification and architecture together as 3 weeks. A student adding the figure notes gets the right total by luck, but the note misstates which stages the 3 weeks cover.
- ch 5 [low] Worked example 1, steps 4 and 6: MIPS and Mops/s are used as units but never defined, and the abbreviation 'Mops/s' is not standard (usually MOPS). A second-language reader may not connect MIPS to millions of instructions per second.
- ch 5 [low] Section 1, first paragraph: 'The specification is executable: a model produces test data' narrows an executable specification to a test-data generator and can mislead. An executable specification is a simulatable model of the whole system that can be run to check behaviour and to produce expected outputs.
- ch 5 [low] Quiz Q2: The question asks for four stages, but the answer lists six items where 'hardware and software design' can be read as one stage or two, so a student cannot tell how many stages are being counted.
- ch 5 [low] Quiz Q6 answer: 'Keep auto-exposure control in software because it changes rarely' is misleading: auto-exposure is recomputed every frame. The real reason is that it runs at a low rate (once per frame, about 30 times a second) compared with the per-pixel filter, and needs tuning.
- ch 6 [low] Section 3, formula block and TTC definition: TTC = d ÷ (vhost − vtarget) is stated without its condition. If the car ahead is faster than the host, the denominator is zero or negative and the TTC value is meaningless, but a student can still plug numbers in and get an answer.
- ch 6 [low] Section 3, formula block (D = vhost × Tdesired): The desired-distance formula is the pure time-gap part only. Production adaptive cruise control keeps an extra standstill clearance, so a student may believe D = v × T is the whole rule at low speeds.
- ch 6 [low] Section 2, last paragraph: 'The ECU then trusts the sensor's status bits and plausibility checks' contradicts Section 4, which says a plausible but wrong reading is dangerous. A student may conclude the ECU accepts smart-sensor data without checking it.
- ch 6 [low] Figure (ADAS pipeline), nodes 'perc' and 'dec': The notes put the gap (1.6 s) and closing speed (5 m/s) under Perception and only the desired gap under Decision, but computing time gap and TTC is a decision-stage calculation, not perception. Perception should output the lead car with its range and relative speed.
- ch 6 [low] Section 2, paragraph 2: 'shortens the wire from the sensing point' is vague. The point of a smart sensor is that the analog wire between the sensing element and the ADC stays inside the sensor, and only a short digital bus run leaves it.
- ch 7 [low] worked example 1: The output count 224×224×64 assumes padding keeps the spatial size at 224×224, but the question does not say this. A student using a valid 3×3 filter with no padding gets 222×222×64 and a different answer.
- ch 7 [low] worked example 1, question line: 'At 100 GOPS (10⁹ operations/s)' can be misread as 100 GOPS = 10⁹ operations/s, which contradicts step 4.
- ch 7 [low] quiz Q3: The word 'taps' is used for both filter coefficients and the 16-input-channel factor. 'Each output uses 3×3×16 taps' hides that 3×3 is the spatial filter and 16 is the number of input channels.
- ch 7 [low] quiz Q5: The question asks for one difference, but the answer adds a second claim ('faster and uses less fabric area') that is not the stated difference and is only a general tendency.
- ch 8 [low] Section 1, last sentence: The abbreviation EDLC is used without being defined, and a reader on a phone cannot look it up mid-chapter.
- ch 8 [low] Section 2: "The boundary-scan register (BSR) has one cell for each device pin" is loose: supply and ground pins do not get cells, and special pins may differ.
- ch 8 [low] Quiz Q7: The question asks for two reasons but the answer lists three (fault model misses defects, coverage below 100 percent, thresholds passing marginal boards).
- ch 9 [high] Section 3, peripheral clock control (pin configuration sentence): The advice "Configure unused pins as outputs or with pull-ups disabled, because a floating input can draw current" contradicts its own reason. Disabling the pull-up on an unconnected input is exactly what leaves the pin floating, so the input buffer can sit at mid-rail and draw cross-bar current. A student will follow the sentence and create the current drain it warns about.
- ch 9 [low] Section 1, where the power goes: Short-circuit power is said to be "roughly proportional to V² f". The usual model is P_sc ≈ (β/12)(V − 2V_T)³ (t_r + t_f) f, so it grows roughly as V³ f, not V² f. Giving it the same V² f dependence as dynamic power makes the two look identical, which they are not.
- ch 9 [low] Section 1 and the figure spec: The model P = f³/1000 has hidden units. The number 1000 only works when f is inserted in MHz to get mW; a student who puts f in Hz gets an absurd result and cannot see where the constant came from.
