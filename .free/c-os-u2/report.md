# c-os-u2: free-model run

- Book: `books/cse/c-os/c-os-u2.html`
- Status: problems
- Model calls so far: 61 (207,601 tokens in, 214,292 out), 9.5 minutes

## Checker

```
c-os-u2.html: 9 chapters, 12931 words, 10 figures, 156 KB
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
- chapter 3: a c program does not run (compile error: rror: missing terminating " character
   17 | ", WEXITSTATUS(stat)
- chapter 3: a c program does not run (compile error: ror: missing terminating " character
   26 | ", getpid(), pid1, p)
- chapter 4: a c program does not run (compile error:   14 |         printf("Child read: %s
      |                ^~~~)
- chapter 4: a c program does not run (compile error: : error: missing terminating " character
   10 |     printf("Tota)
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
- ch 3 [high] Section 1 formula: The ternary expression PID_child = fork() ? 0 : new_PID is wrong. In C, fork() returns 0 in the child (false), so the expression would evaluate to new_PID, not 0.
- ch 3 [high] Worked example 1 description: It claims that each subsequent fork creates a child that receives the next consecutive PID. PIDs are allocated from a pool and are not guaranteed to be consecutive.
- ch 3 [low] Section 2 C code example: The code uses exit(42) without including <stdlib.h>, which declares exit().
- ch 3 [low] Quiz Q7 code snippet: The snippet shows incomplete include directives ("#include \n#include \n#include \n"). It also omits <stdlib.h> for exit().
- ch 3 [low] Lead paragraph: It refers to spawn() as a system call on Windows. spawn() is a POSIX library function; Windows uses CreateProcess() as the system call.
- ch 4 [high] Section 3 (Pipe IPC): The statement "Pipe buffer size is kernel defined; typical default is 4 KB" is outdated. On modern Linux kernels the default pipe capacity is 64 KB (and can be larger on other systems).
- ch 4 [high] Quiz Q5: The answer assumes that a blocking write on a pipe can return after writing only part of the data (4 KB of a 6 KB request). In blocking mode the write call blocks until all data is written; partial writes occur only when the pipe is opened with O_NONBLOCK.
- ch 4 [low] Section 3 (Pipe IPC) bullet list: The bullet does not mention the atomic‑write guarantee for writes up to PIPE_BUF bytes, which is important for avoiding interleaving of data from multiple writers.
- ch 4 [low] Quiz Q7: The suggested mitigation uses "flock" on a FIFO, but advisory file locks are not defined for FIFO special files and may not work reliably.
- ch 4 [low] Section 2 (Message‑queue IPC) bullet list: The phrase "Message size is limited (often 8192 bytes)" may mislead students; the actual limit (MSGMAX) is implementation‑defined and can be larger.
- ch 5 [high] Quiz Q3: The answer states the minimum wall‑clock time is 300 ms, assuming each thread runs uninterrupted on a core. With perfect preemptive scheduling on a dual‑core CPU, the total CPU work is 3 × 150 ms = 450 ms, so the theoretical minimum wall‑clock time is 450 ms ÷ 2 = 225 ms. The given answer overestimates the minimum time.
- ch 5 [low] Section 2 (Threading models): The text says "Solaris 9 introduced this model" for many‑to‑many, but many‑to‑many was introduced earlier, in Solaris 2.5 (mid‑1990s).
- ch 5 [low] Section 3 (Multicore programming and responsiveness), bullet point 2: The bullet says "Create a thread for each task using the one‑to‑one model", which may mislead students to think they choose the threading model.
- ch 5 [low] Section 1 (Thread control block and per‑thread resources): The memory formula does not specify the unit of measurement.
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
