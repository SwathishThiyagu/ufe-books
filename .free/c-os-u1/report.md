# c-os-u1: free-model run

- Book: `books/cse/c-os/c-os-u1.html`
- Status: error
- Model calls so far: 27 (98,632 tokens in, 258,147 out), 61.8 minutes

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 3: The text contains a redundant word in the sentence: 'are covered in detail in see Unit 4.'
- ch 2 [low] Section 2: The text states the CPU 'pushes the current Program Counter (PC)' onto the stack. Technically, it pushes the return address (the address of the next instruction), not the one currently being finished.
- ch 2 [low] Section 2: The text says the CPU 'disables lower-priority interrupts'. In many common architectures like x86, the CPU simply disables all maskable interrupts via a single flag; the priority logic is handled by the external Interrupt Controller.
- ch 2 [low] Section 3: The chapter lacks the requested Indian context/analogy to help ESL students understand the abstract concept of polling vs interrupts.
- ch 2 [low] Quiz Q5: The answer uses 1,048,576 for 1 MB. While mathematically correct (2²⁰), many Indian B.Tech exams and textbooks simplify 1 MB to 1,000,000 bytes for easier calculation in examples.
- ch 3 [high] Figure: Inconsistent process workload between the Sequential and Multiprogrammed lanes in the Gantt chart spec. The Sequential lane defines P1 with only one 10 ms CPU burst (0–10 ms) followed by I/O (10–25 ms), but the Multiprogrammed lane adds an extra 5 ms CPU burst for P1 from 25 to 30 ms that does not exist in the sequential execution.
- ch 3 [high] Quiz Q5: The question prompt states 'A system executes 3 jobs sequentially', but only provides parameters for 2 jobs (Job A and Job B). The calculated answer (70 ms total time, 25 ms CPU time) also accounts for only 2 jobs.
- ch 4 [high] Worked example 2: The scientific notation for frequency (10⁹) is written as '109' in steps 1 and 4, which is a significant mathematical error. A student would read this as 109 (one hundred and nine) instead of 1,000,000,000.
- ch 4 [high] Section 2: Privileged Instructions: The text states that attempting a privileged instruction generates a trap with an error message like 'Segmentation Fault'. This is technically incorrect. A 'Segmentation Fault' (SIGSEGV) is specifically for memory access violations. Attempting a privileged instruction (like CLI or I/O) triggers an 'Illegal Instruction' (SIGILL) or 'General Protection Fault'.
- ch 4 [low] Section 3: Timers and Preemption: The text mentions a '1 MHz' clock tick as an example, but the worked example uses '2.5 GHz'. While not factually wrong, using widely different orders of magnitude for the same concept in the same section can confuse students.
- ch 5 [high] Section 2, Resource Allocation: The sentence 'covered in see Unit 2' is grammatically incorrect and contains a redundant word.
- ch 5 [high] Figure spec: The layering order is technically incorrect. System calls are the interface that sits above the system services/kernel, not below them. The description implies system programs call services which then call system calls.
- ch 5 [high] Quiz Q3: The answer identifies 'Error Detection' as a primary service involved in blocking unauthorized file access. While it reports the error, the primary service that handles the request and enforces the rule is 'File-system manipulation'.
- ch 5 [low] Section 2, formula: The formula uses 'u<sub>i</sub>' but the definition uses 'ui'. Symbols should be consistent.
- ch 5 [low] Section 1, Error Detection: 'Index out of bounds' is a high-level programming error usually caught by a runtime (like JVM) rather than the OS directly.
