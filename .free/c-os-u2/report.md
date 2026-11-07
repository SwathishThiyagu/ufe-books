# c-os-u2: free-model run

- Book: `books/cse/c-os/c-os-u2.html`
- Status: ok
- Model calls so far: 38 (153,291 tokens in, 248,047 out), 6.2 minutes

## Checker

```
c-os-u2.html: 9 chapters, 17271 words, 10 figures, 183 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Beyond: The claim that 'reading it is how tracing tools such as strace and perf follow a process' is technically wrong. strace works through the ptrace system call and stops/inspects the tracee at each system call; perf uses performance counters and sampling. Neither follows a process by reading task_struct through /proc.
- ch 1 [low] Beyond: /proc/<pid>/stat does contain kstkesp and kstkeip fields for the kernel stack pointer and instruction pointer, but on current kernels these fields are reported as 0, so a student who looks will see zeros and think the chapter is false.
- ch 1 [low] Section 2: Contradiction inside the state list: New says the PCB already exists, but the new → ready edge says 'memory and PCB have been allocated' as if the PCB appears only at admission.
- ch 1 [low] Figure: 'Running has an exit back to Ready for the timer interrupt' uses the word 'exit', which in this chapter means the Terminated state and is also the label of the Running → Terminated edge. A student can misread it as Running leaving to Terminated.
- ch 1 [low] Quiz Q5: The answer says a Waiting → Running jump 'would put two processes on one core'. If a core is idle it would not, so the stated reason is overstated and the real reasons (no scheduling decision, inconsistent state meaning) get lost.
- ch 2 [low] Worked example 1, step 3: Step 3 says the 200 ns scheduler decision 'is part of dispatch latency'. That contradicts the definition given two paragraphs earlier in Section 2 (dispatch latency = time to stop one process and start another, i.e. the dispatcher's work). It is fine to count the scheduler time in the switch overhead, but calling it part of dispatch latency will make students write the wrong definition in the exam.
- ch 2 [low] Section 1 / Figure: Section 1 says the figure traces the full life cycle, including admission 'from the job queue into the ready queue', but the figure has no job queue node and no admitted edge. A student comparing text and figure will look for a path that is not drawn.
- ch 2 [low] Quiz Q7: The answer lumps two independent costs together. Register save/restore does scale with register count, but TLB size does not reliably make a switch dearer: a larger TLB can be invalidated by a single instruction or spared a flush entirely by address-space tags (ASIDs/PCIDs). Also, 'no cache of translations' on machine A cannot be read as 'cheaper', because without a TLB every access is slower. The qualifier 'tagged TLB entries' is attached to the register argument, where it does not belong.
- ch 3 [low] Lead: "Every running process in an operating system comes from another process" is not strictly true: the first process (init/systemd) is created by the kernel at boot, and kernel threads also start from the kernel, not from a fork by a user process. A student may think init was forked by something.
- ch 3 [low] Section 2 (exec forms): "whether the shell path is searched" is wrong terminology. The exec variants differ in whether they search the PATH environment variable for the file name; "shell path" can be misread as the path of the shell itself.
- ch 3 [low] Section 2 (exit): "exit() is the reverse of creation" is vague. It does not say that exit ends the calling process and that the parent sees only the low 8 bits of the status through WEXITSTATUS, so a student may expect the full integer to be readable.
- ch 4 [low] Figure (sequence spec) and its caption: The caption says the writer makes 65 writes, but the spec shows 'write 1000 B' followed by '65 more writes', which is 66 writes. The 66th write is the one that blocks, so the spec and caption disagree by one write.
- ch 4 [low] Section 3, unnamed pipe blocking rule: 'When it is empty the reader blocks' is incomplete. A read on an empty pipe returns end-of-file (0 bytes) if no process holds the write end open; it blocks only while some writer still has the pipe open. As written, a student may think the reader blocks forever after the writer closes.
- ch 5 [low] Figure caption and node notes (Section 3 figure): The caption says only the stack and registers sit inside each thread, but the chapter's own list (and the exam trap) also makes the program counter and thread id private to a thread. A student may copy the incomplete list in the exam.
- ch 5 [low] Section 3, last line: 'More threads than cores does not increase speed' is too absolute. Extra threads cannot raise the parallel speedup of CPU-bound work, but they do raise throughput when threads block on I/O (disk, network), which is the reason thread pools exist.
- ch 6 [high] Section 3, waiting-time formula and table: The formulas contradict each other on I/O. Turnaround is defined as 'waiting plus CPU time plus all I/O', but waiting time is then given as turnaround − burst, and the same line says 'I/O time is not waiting time'. If turnaround includes I/O, subtracting only the burst leaves I/O counted inside waiting time, which is wrong. A student who meets an example with I/O will compute an inflated waiting time.
- ch 6 [low] Section 2, second paragraph: The term 'dispatcher latency' is non-standard; the standard name is dispatch latency (the time the dispatcher takes to stop one process and start the next).
- ch 7 [high] Exam traps, second bullet (and the formula W = S − A in Section 1): The trap bullet states generally that W = start − arrival. That is only true when the process is never preempted. For a preempted process it gives the wrong answer: P1 in the round-robin example starts at 0 ms and arrives at 0 ms, which would give W = 0 ms, but step 9 correctly computes W = 6 ms. The chapter contradicts itself, and a student who memorises the trap bullet will lose marks on every preemptive question (RR, SRTF, preemptive priority).
- ch 7 [low] Section 4, the sentence on a tiny quantum: With q = 10 µs and a switch costing 10 µs, the overhead fraction is 10/(10+10) = 50%, so the CPU does not spend 'most of its time' switching; half of it is useful work.
- ch 7 [low] Section 4, last sentence: CFS is not descended from the multilevel feedback queue ladder. It keeps one run queue and orders tasks by virtual runtime; its ancestry is weighted fair queueing / stride scheduling. The MLFQ is the Windows-style design, not CFS.
- ch 8 [low] Section 3, utilization formula box: The box says U is 'from 0 to 1'. A task set's total utilization Σ tᵢ/pᵢ can easily exceed 1, and that is exactly the signal that the set cannot be scheduled. A student who computes U = 1.2 may think the calculation is wrong.
- ch 8 [low] Section 1, PCS definition: 'user threads compete only inside their own process for one available LWP' is misleading. Under PCS the threads of the process compete with each other for CPU time, and the thread library maps the winners onto the LWPs the process already holds. They do not compete 'for one LWP'.
- ch 8 [low] Section 1, SCS example: 'the two LWPs sit in the system ready queue' mixes two objects. The kernel schedules kernel threads; each LWP is attached to one kernel thread. As written, a student may think LWPs themselves are queued by the kernel.
- ch 8 [low] Section 3, RMS bound: The bound U ≤ n(2^(1/n) − 1) is stated without its conditions. It holds for independent periodic tasks, fixed worst-case execution time per job, preemption with no blocking, and each deadline equal to its period. Without these, the bound does not apply.
- ch 8 [low] Quiz Q4 answer: 'EDF can meet all deadlines if U ≤ 1' is stated without the condition. With deadlines shorter than periods, U ≤ 1 does not guarantee EDF schedulability.
- ch 8 [low] Section 2, load balancing: 'CPU utilization is better but harder to read' is vague and unsupported. Both measures are standard; the point is what each one captures, not that one is 'better'.
- ch 8 [low] Figure caption: 'Task T1 runs every 4 ms' can be read as execution time 4 ms, which clashes with the worked example where T1's execution time is 1 ms.
- ch 9 [low] Section 3 and Exam trap 4: The chapter says a waking task is placed exactly at the tree's minimum vruntime, i.e. at cfs_rq->min_vruntime. In the kernel the value is max(old vruntime, min_vruntime − threshold), and with GENTLE_FAIR_SLEEPERS on by default the threshold is half of sched_latency. So a sleeper does get a small bounded credit (half a latency window), not exactly the minimum. The conclusion 'sleeping earns no extra CPU' is still right, but the sentence is stated too absolutely.
- ch 9 [low] Exam trap 5: The last clause, 'a normal task placed in the first band outranks everything', is confusing. A normal task is never given a priority in 0–99, and if it were it would outrank other normal tasks but still sit with the real-time band, not above everything.
- ch 9 [low] Section 1, step 1 (also the figure): A waking task is not always inserted in the active array. In the O(1) scheduler, if the woken task's priority is not better than the currently running task's, it is queued in the expired array so it cannot preempt the running task; only a higher-priority wakeup goes to the active array.
- ch 9 [low] Lead and Section 1: '140 priority queues' is loose: the runqueue has two arrays of 140 lists each (280 lists in all), one array active and one expired, with a bitmap per array.
- ch 9 [low] Beyond: 'one step gives roughly 25% more CPU' is direction-blind. Moving one step toward higher weight (nice 0 to nice −1) multiplies weight by 1.25, giving 25% more CPU; moving one step the other way (nice 0 to nice 1) gives 1024/820, about 20% less.
