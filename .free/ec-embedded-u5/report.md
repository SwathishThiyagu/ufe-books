# ec-embedded-u5: free-model run

- Book: `books/ece/ec-embedded/ec-embedded-u5.html`
- Status: ok
- Model calls so far: 29 (109,799 tokens in, 231,739 out), 5.6 minutes

## Checker

```
ec-embedded-u5.html: 9 chapters, 18643 words, 10 figures, 181 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] quiz Q7, together with the Section 2 sentence "ARM Cortex-M, from Unit 2, gives the CPU two privilege levels": Cortex-M0 and Cortex-M0+ implement ARMv6-M. In ARMv6-M the CONTROL register has bit 1 (SPSEL) but no bit 0 (nPRIV), so thread mode is always privileged and no unprivileged state exists. Unprivileged thread mode comes with ARMv7-M and ARMv8-M cores (Cortex-M3, M4, M7, M23, M33). A Cortex-M0+ therefore cannot run a user/kernel split at all, and the "yes" answer to Q7 has no valid basis.
- ch 1 [low] Section 1, last paragraph ("Firmware and OS run privileged in kernel space; the application runs unprivileged in user space"): Written as a universal fact. The split is a build option, and most small RTOS builds, including the default FreeRTOS Cortex-M demos, run every task privileged inside the kernel image.
- ch 1 [low] lead paragraph: "You meet this design in every RTOS" is too strong, and "FreeRTOS calls it kernel and user modes" is not FreeRTOS terminology: FreeRTOS speaks of the kernel and of tasks, and only its ARMv7-M MPU port offers unprivileged tasks.
- ch 1 [low] Section 2 ("cannot change the stack pointer") and quiz Q7 answer: Unprivileged code changes its own stack pointer constantly: ordinary pushes, pops and locals all move the PSP. What it cannot do is switch CONTROL.SPSEL to the MSP, or read and write MSP/PSP with MSR and MRS.
- ch 1 [low] quiz Q5 answer: "Each call costs one change down and one up" reverses the directions used in Worked example 1, where entering the kernel is counted as a change up and the exception return as a change down. A student copying the answer writes the wrong direction.
- ch 2 [low] Section 4, utilisation formula: The text says only that U > 1 means deadlines cannot all be met. A student can read this backwards and assume U ≤ 1 guarantees schedulability, which is false for fixed-priority scheduling.
- ch 2 [low] Section 2, TCB bullet list: 'Owner or ID: which task or process this TCB belongs to' is ambiguous — a TCB does not belong to another task; the field holds the task's own identifier and, where relevant, its owning process.
- ch 2 [low] Lead: 'a fixed priority each' is presented as a property of all RTOS tasks. Many RTOSs support priority changes at run time, so the sentence overstates.
- ch 3 [high] Figure caption and worked example 1, answer line: Both say "Both tasks finish at 16 ms". Task A finishes at 13 ms (step 5) and only task B finishes at 16 ms. The schedule ends at 16 ms, but the two tasks do not finish together, so the statement contradicts the steps above it and would mislead a student writing the answer in an exam.
- ch 3 [low] Section 2, second bullet of the step list: "The kernel pushes the PC and status register on the current task's stack" is not true on most microcontrollers (for example ARM Cortex-M), where the hardware pushes the PC and status register on interrupt entry; elsewhere in Section 3 the chapter itself says "the hardware saves the minimum". A student may be marked down for saying software saves them.
- ch 3 [low] Quiz Q5, answer: "The register save is the same tens of cycles in both" is too strong. An application processor usually saves extra state (floating-point, SIMD/vector registers, sometimes more status words), so its register-save term is larger than a small microcontroller's, not equal.
- ch 4 [high] Section 1 (definition of response time), Section 2 (response-time test), and Exam traps bullet 4: The chapter defines response time as 'from arrival to first run', but the response-time test then uses Rᵢ as the time from release to completion. In the example T3 first runs at 3 ms but R₃ = 8 ms, which is its completion time. The trap bullet repeats the first-run definition, so the student is told two different things about the same symbol.
- ch 4 [low] Figure caption: The caption says 'T1 preempts T2 and T3, T2 preempts T3'. In the drawn schedule T2 never preempts T3, and T1 never preempts T2; the only real preemption is T1 interrupting T3 at 4 ms.
- ch 4 [low] Section 2, response-time test paragraph, and Quiz Q5: The text jumps straight to '8 ms at R₃ = 8', which is circular, and Q5 only states that 8 ms is the smallest solution. A student cannot see how the fixed point was reached.
- ch 5 [high] Section 2 formula: The response-time formula R = L_int + L_sch + T_sw + T_eff omits the ISR's own execution time. L_int stops at the first ISR instruction and L_sch starts after the ISR, so the code between them is missing. The 14 µs example is therefore not a complete event-to-output response.
- ch 5 [high] Section 1 formula: slack = deadline − WCET conflicts with Section 2 and the worked example, which use slack = deadline − R. WCET is the task's code execution time, not the full event-to-output response time. A student following the Section 1 formula gets 20 − 4 = 16 µs instead of 6 µs.
- ch 5 [high] Worked example 1, step 7: After the scheduler is cut to 3 µs, the remaining stages are ISR 3, scheduler 3, switch 2, time-to-effect 4. The largest is T_eff = 4 µs, but step 7 says to attack ISR entry next and then the switch, ignoring the 4 µs stage.
- ch 5 [high] Section 1, jitter paragraph: The sentence '1 µs average and a 50 ms worst case ... cannot be called real-time' is false without a deadline. A bounded 50 ms worst case can be hard real-time for a 100 ms deadline. Real-time means meeting the deadline, not having low jitter.
- ch 5 [high] Section 3, priority inheritance: Priority inheritance does not stop a low-priority lock holder from blocking a high-priority task. It bounds that blocking by raising the holder's priority while it holds the lock.
- ch 5 [low] Section 3 table, worst-case latency row: 'Unbounded (ms to tens of ms)' is self-contradictory: unbounded means no upper limit, but a ms-to-tens-of-ms range gives one.
- ch 5 [low] Figure aria: The aria says the chain ends at the motor task's first instruction, but the final 4 µs is labelled 'Motor task runs' and is the time to effect after that first instruction.
- ch 5 [low] Quiz Q6: The question asks 'by how much must each stage shrink', but the answer shrinks only the scheduler. 'Each stage' suggests a per-stage reduction that is not given.
- ch 6 [low] Section 1, interrupt-disable protection: The sequence 'mask interrupts, run the few instructions, unmask' does not say to save the previous interrupt-mask state. If the code is already inside another critical section, the unconditional unmask enables interrupts too early and nesting breaks.
- ch 6 [low] Section 1, the two protections: The chapter never says that a mutex or lock cannot protect data that an ISR also touches. A student may take a mutex around a variable that an ISR writes, and the ISR cannot take the mutex, so the protection silently fails.
- ch 6 [low] Lead: The lead says inter-task communication gives 'three tools', but Section 3 also covers mailboxes, event flags and pipes, so the count does not match the chapter.
- ch 6 [low] Exam traps, trap 4: Calling a mutex that is never released 'deadlock' contradicts the chapter's own definition two paragraphs earlier, which says deadlock is a cycle of tasks each waiting for a resource held by the next. Here there is one holder and one waiter, no cycle.
- ch 6 [low] Section 2, sentence 'only a task may take one, because an ISR cannot block': Some kernels do allow a non-blocking take (zero timeout) from an ISR. The absolute rule can confuse a student who later meets such an API.
- ch 7 [high] Quiz Q1: The question asks for six entry points but the answer lists seven: init, open, close, read, write, ioctl and the ISR. A student who lists exactly six and leaves out one item loses marks against an answer key that itself breaks the count.
- ch 7 [low] Section 2 formula and Worked example 1, step 3: The symbol f is defined twice with different meanings: in the Section 2 formula f is the fraction of CPU time used by transfers, while in the worked example f is the 1 MHz SPI clock (the fraction later appears as f_cpu). Students copying the formula may mix the two up.
- ch 7 [low] Section 1, last paragraph: 'On-board bus drivers for I2C, SPI and CAN move register addresses and frames' is unclear: I2C and SPI carry addresses and data bytes, CAN carries frames, and a bus driver moves data, not addresses.
- ch 8 [low] Section 2: The sentence 'Every request is rounded up to B bytes' is imprecise. A request larger than one block (say 200 bytes with B = 128) is rounded up to a whole number of blocks, not to B bytes. The worked example only uses requests ≤ B, so the wording is never corrected.
- ch 8 [low] Section 1: '.bss (zero-initialised globals)' leaves out static variables. The line above correctly says .data holds 'initialised globals and static variables', but a zero-initialised static variable (for example a static buffer) also lives in .bss, and a student may write otherwise in an exam.
- ch 8 [low] Figure: The figure stacks flash, .data/.bss, heap, free RAM and stack on one continuous ramp labelled 'low address' to 'high address'. On most microcontrollers flash and RAM sit in separate address ranges with a gap between them, so a student can wrongly conclude that .data follows code contiguously in one address space.
- ch 9 [low] Lead: The lead calls the bootloader 'the first code that runs after reset'. Section 2 of this same chapter correctly says the processor starts in on-chip ROM code, which runs before any bootloader, so the two statements contradict each other and a student may write the wrong first stage in an exam.
- ch 9 [low] Section 1 (kernel images): 'A zImage is a compressed kernel that decompresses itself in place' is misleading. The self-extracting stub copies the kernel to the address it was linked for; it does not decompress the kernel on top of the compressed image.
- ch 9 [low] Section 2 and the figure: The stage timings put init in two places. The text says 'kernel decompression and init 1.4 s', while the figure labels the 2.5 s stage 'Rootfs and init'. init is the first user-space process and can only start after the root file system is mounted, so it cannot also belong to the kernel stage.
- ch 9 [low] Quiz Q1: The question asks for 'the five stages of the boot chain', but the model answer lists the five stages and then adds the application, which is a sixth box in the figure. A student counting six items against a five-mark question freezes.
