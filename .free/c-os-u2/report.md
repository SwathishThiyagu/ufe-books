# c-os-u2: free-model run

- Book: `books/cse/c-os/c-os-u2.html`
- Status: problems
- Model calls so far: 46 (155,307 tokens in, 160,273 out), 6.2 minutes

## Checker

```
c-os-u2.html: 9 chapters, 12736 words, 10 figures, 152 KB
PROBLEMS:
 - chapter "threads-multicore-programming-and-multithreading-models": needs a <div class="quiz"> with at least 5 <details data-level=...> questions
```

## For the reviewer

- chapter 6: a c program's shown output was replaced by its real output; check the text around it
- chapter 1: a c program's shown output was replaced by its real output; check the text around it
- chapter 5: a c program's shown output was replaced by its real output; check the text around it
- chapter 5: give 6 to 8 quiz questions
- chapter 5: a c program prints
Image 1 done
Image 2 done
Image 3 done
Image 4 done
All downloads complete
but the chapter shows
Image 1 done
Image 3 done
Image 4 done
Image 2 done
All downloads complete
Make the shown output and any explanation match what the program really prints
- chapter 3: a c program does not run (compile error: /usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/13/../../../x86_64-lin)
- chapter 3: the figure cannot be drawn: tree label "Parent (PID 1000)" is too long; shorten it
- chapter 3: worked example 1: the example's "check" code failed: File "/tmp/tmp5og92z3l/check.py", line 1
    pids = [1000, 2000, 2001, 2002]\nfor pid in pids:\n    print(pid)
                                    ^
SyntaxError: unexpected character after line continuation character
- chapter 3: a c program does not run: compile error: /usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/13/../../../x86_64-linux-gnu/Scrt1.o: in function `_start':
(.text+0x1b): undefined reference to `main'
collect2: error: ld returned 1 exit status
- chapter 4: a c program does not run (compile error: /usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/13/../../../x86_64-lin)
- chapter 4: a c program does not run: compile error: /usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/13/../../../x86_64-linux-gnu/Scrt1.o: in function `_start':
(.text+0x1b): undefined reference to `main'
collect2: error: ld returned 1 exit status
- chapter 8: a c program's shown output was replaced by its real output; check the text around it
- chapter 8: a python program's shown output was replaced by its real output; check the text around it
- chapter 8: the figure cannot be drawn: cannot evaluate "0 if x%5<1 else None": float() argument must be a string or a real number, not 'NoneType'
- chapter 9: a c program's shown output was replaced by its real output; check the text around it
- chapter 5: the reviewer found 1 serious problem(s) and the revision did not pass the checks; read the review in the state folder
- chapter 3: the reviewer found 4 serious problem(s) and the revision did not pass the checks; read the review in the state folder
- chapter 4: the reviewer found 2 serious problem(s) and the revision did not pass the checks; read the review in the state folder
- checker: chapter "threads-multicore-programming-and-multithreading-models": needs a <div class="quiz"> with at least 5 <details data-level=...> questions

## Reviewer notes (after any revision)

- ch 1 [high] Quiz Q2: The question asks why a process moves from the Ready state to the Waiting state, but a process can only enter Waiting (Blocked) from the Running state after issuing an I/O request.
- ch 1 [high] Worked example step 1: The description says “OS admits P → state New”, which is incorrect. Admission moves a process from New to Ready; the process is initially in the New state when created.
- ch 1 [low] Quiz Q4: The answer is vague and says the exact sequence depends on the I/O of P1, which does not give a clear expected answer for the exam.
- ch 1 [low] Section 2: Process Life‑Cycle States: The bullet list includes “Admission” and “Dispatch” as if they were process states, but they are scheduling actions.
- ch 2 [high] Section 3, bullet point about Dispatcher: The bullet says "Dispatcher = hardware‑software module that saves, selects, and restores." The dispatcher does not perform the selection; the scheduler selects the next process.
- ch 2 [high] Section 3, definition of dispatch latency: It states "Dispatch latency = total time spent inside the dispatcher," which is inaccurate. Dispatch latency includes the scheduler overhead as well, not only the dispatcher’s work.
- ch 2 [low] Section 1, description of moving a PCB: The sentence "This movement is fast because the OS only updates a pointer in the PCB" oversimplifies; moving a PCB between queues usually involves list‑node operations, not just a pointer inside the PCB.
- ch 2 [low] Exam traps: The term "dispatch time" is used without prior definition, which may confuse students.
- ch 3 [high] Section 1: The formula "PID_child = fork() ? 0 : new_PID" is incorrect. The ternary expression does not represent the actual return values of fork().
- ch 3 [high] Worked example 1: It assumes that PIDs are assigned consecutively (2000, 2001, 2002). In real systems PID allocation is not guaranteed to be sequential.
- ch 3 [high] Quiz Q7: The C snippet shows "#include \n#include \n#include \n" without actual header names, making the code invalid.
- ch 3 [high] Quiz Q7 answer: The answer repeats the same incomplete include placeholders, leaving the snippet unusable.
- ch 3 [low] Section 2 (C code example): The code uses exit(42) but does not include <stdlib.h>, where exit() is declared.
- ch 3 [low] Section 3 (state diagram description): The transition "running → terminated → zombie → reaped" is inaccurate; after exit the process becomes a zombie directly.
- ch 3 [low] Worked example 1, step 2: Wording "Second fork is executed by both existing processes" can be unclear for beginners.
- ch 4 [high] Section 3 (Pipe IPC): The statement that the typical default pipe buffer size is 4 KB is outdated; on modern Linux kernels the default pipe capacity is 64 KB.
- ch 4 [high] Quiz Q7: The suggested mitigation of using flock() on a FIFO is incorrect because flock does not work reliably on named pipes; atomic writes up to PIPE_BUF should be used instead.
- ch 4 [low] Section 1 (Shared‑memory IPC): The description mentions only System V keys for identifying a segment, omitting POSIX shared memory which uses a name.
- ch 4 [low] Formula in Section 1: Units for throughput are not specified; readers may be unclear whether the result is bytes per millisecond or another unit.
- ch 5 [high] Section 2: Threading models: The text says "Solaris 9 introduced this model" for the many‑to‑many threading model, but the many‑to‑many model was introduced earlier (Solaris 2.5 / SunOS 5.5). This is a factual inaccuracy.
- ch 5 [low] Section 3: Multicore programming and responsiveness: The instruction "Create a thread for each task using the one‑to‑one model" suggests that the programmer chooses the threading model, which is not true; the OS decides the mapping.
- ch 5 [low] Code example output (Section 3): The shown output lists a specific order of lines, which may give the impression that thread output order is deterministic, while in reality it can vary each run.
- ch 5 [low] Formula in Section 1: The summation Σ(Stack_i) does not specify the range of i, which could be unclear for beginners.
- ch 6 [low] Figure description: The caption says the Gantt chart shows two processes executed non‑preemptively, then preemptively, which contradicts the earlier statement that it is non‑preemptive only.
- ch 6 [low] Section 1, definition of Waiting time: Waiting time is defined as turnaround time minus the CPU burst time, which is only correct when a process has a single CPU burst and no I/O. The definition may mislead students.
- ch 6 [low] Quiz Q4: The answer "response time = 2 ms × N" is ambiguous about whether N includes the newly arrived process and does not explain the reasoning.
- ch 7 [high] Figure ready‑queue order: The SJF row shows order P2, P1, P3, but for the example bursts (P1 8 ms, P2 4 ms, P3 2 ms) the correct SJF order is P3, P2, P1.
- ch 7 [high] Quiz Q3: The answer gives the wrong execution order for non‑preemptive SJF and therefore wrong waiting times and average.
- ch 7 [high] Worked example step 10 (RR waiting time for P1): The expression shown "(4‑0) idle after first slice =6 ms" is mathematically incorrect; (4‑0) equals 4, not 6.
- ch 7 [low] Quiz Q2 answer: Uses phrase "shortest remaining CPU burst" which is inaccurate for non‑preemptive SJF.
- ch 7 [low] Quiz Q8 answer: States that the first process has a remaining burst of 5 ms at 5 ms, but it has already finished.
- ch 8 [high] Section 3 (Choosing the right algorithm) and Section 2 (Real‑time scheduling concepts): The text says “If U_total ≤ RM bound → RM feasible” and “compare U_total with the Liu‑Layland bound”. This wording implies the bound is a necessary and sufficient condition. In reality the Liu‑Layland bound is only a sufficient condition; a task set with U_total greater than the bound may still be schedulable under Rate‑Monotonic.
- ch 8 [low] Section 1 (Multiprocessor load balancing and CPU affinity): The phrase “strong affinity flag” is not defined and may confuse students.
- ch 9 [high] Section 2: Weight values for nice levels are incorrect. The text says nice = ‑5 gives weight ≈ 1280 and nice = 10 gives weight = 512, which do not match the Linux kernel's weight table.
- ch 9 [high] Quiz Q4: The answer computes vruntime increase using weight = 512 for nice = 10, which is wrong.
- ch 9 [high] Quiz Q8: Both weight values are wrong: nice = ‑10 is not ≈ 2048 and nice = 5 is not ≈ 800.
- ch 9 [high] Section 2: The statement "Load average is the sum of all task weights divided by the reference weight" is incorrect. Load average measures the average number of runnable tasks, not weighted sum.
- ch 9 [high] Section 2: The claim that the default time slice is 4 ms on a single CPU is inaccurate. CFS does not use a fixed slice; it uses a target latency (default ≈ 20 ms) and a minimum granularity (default ≈ 1 ms) to compute per‑task slices.
