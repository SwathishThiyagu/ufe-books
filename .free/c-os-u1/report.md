# c-os-u1: free-model run

- Book: `work/claude_figs/c-os-u1/tree/books/cse/c-os/c-os-u1.html`
- Status: ok
- Model calls so far: 57 (209,374 tokens in, 308,858 out), 8.6 minutes

## Checker

```
c-os-u1.html: 9 chapters, 16808 words, 10 figures, 194 KB
OK
```

## For the reviewer

- chapter 7: the figure cannot be drawn: note "mix" runs off the right edge; shorten it
- chapter 5: the figure cannot be drawn: tree is too wide (5 leaves); use fewer leaves or shorter labels
- chapter 9: the figure cannot be drawn: tree is too wide (6 leaves); use fewer leaves or shorter labels
- chapter 7: the figure could not be drawn; a plain box diagram stands in for it
- chapter 9: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [low] Section 2, opening paragraph: The paragraph says the OS manages four broad resources, but then defines five abstractions (process, thread, address space, file, pipe) without ever naming the four resources. A student cannot tell what the four resources are until the table.
- ch 1 [low] Section 3, figure reference: The text says 'The figure after Section 1 shows this path', but the figure is placed after Section 3. The reader looks in the wrong place.
- ch 1 [low] Figure: Section 3 lists the layers as applications, libraries, system call interface, kernel, hardware, but the figure drops the libraries layer, so the figure and the text do not match.
- ch 1 [low] Quiz Q1: 'The kernel is the core privileged part that always runs' can be read as 'kernel code executes at all times', which is false: kernel code runs only on system calls, interrupts and faults.
- ch 2 [low] Section 3 (vector table paragraph): The sentence 'Some syllabi call this the interrupt descriptor table' comes right after the ARM table, so 'this' is ambiguous, and it wrongly suggests the IDT is a syllabus naming choice. The IDT is Intel x86's own name for its vector table, already introduced two sentences earlier; the paragraph repeats it and can confuse a student about which name belongs to which architecture.
- ch 2 [low] Quiz Q1 answer: 'a signal that makes the CPU stop its current instruction stream' suggests the CPU halts in the middle of an instruction. Hardware interrupts are only taken at instruction boundaries, and the chapter itself says this in Section 3 (and in exam trap 5).
- ch 2 [low] Section 2 (polling paragraph): The status-bit polarity is stated as fixed ('bit 0 = not ready, bit 1 = ready'), but which value means ready depends on the device controller. A student may memorise 1 = ready as a general rule.
- ch 3 [low] Section 3, real-time paragraph: The gloss on interrupt latency ('the longest time before the OS answers a device') blurs two different things: the delay from the interrupt arriving to the OS starting the handler, and the full device response time. A student may take the second meaning.
- ch 3 [low] Figure caption: The caption says the bars show when each type 'dominated', but the bars overlap (time-sharing runs to 1985 while the PC bar starts at 1980), so 'dominated' contradicts what the reader sees.
- ch 3 [low] Section 2, time-sharing paragraph: The short turn given to each user is called a time slice but the synonym used by many textbooks, quantum, is never given, so a student meeting 'time quantum' in a question paper may not connect it.
- ch 4 [high] Exam traps, bullet 4 (read() / trap instruction): It says the trap instruction inside read() is privileged. A trap (system call) instruction is deliberately executable in user mode — that is the whole point of the controlled door. A privileged instruction is one the CPU refuses in user mode; if the trap instruction were privileged, no user program could ever make a system call. This contradicts Section 2 of the same chapter.
- ch 4 [low] Section 1 privileged-instruction list, and Quiz Q5 answer: Listing 'enter kernel mode' as an example of an instruction the CPU blocks in user mode clashes with Section 2, where entering kernel mode is exactly what a user program does through a trap. A student may conclude that a system call is forbidden in user mode.
- ch 5 [high] Section 3, paragraph 1: The order of steps in a system call is wrong. The text says the kernel 'checks arguments, switches to kernel mode and runs file-system code'. The mode switch happens at the trap instruction, before any kernel code runs; the kernel cannot check arguments while still in user mode. A student who copies this order loses marks.
- ch 5 [low] Worked example 1, part (c) and step 3: Part (c) defines I/O as 'the network hardware transfer', but the data gives one 40 ms figure for 'network request and reply' and step 3 labels all 40 ms as I/O. The communication-service work and the hardware transfer are not separated, so the stated definition and the arithmetic do not match.
- ch 5 [low] Quiz Q7: The answer names file-system manipulation and protection, but the app that writes directly to a physical flash address also bypasses the I/O operations service, since it does the device write itself instead of asking the OS.
- ch 5 [low] Section 1, last paragraph: 'Some syllabi call this list OS services' is misleading. Standard textbooks title both lists together as operating-system services; the first six are the user-facing ones, and allocation, accounting, protection and security are also OS services. A student may conclude the system services are not OS services.
- ch 5 [low] Figure: The system side of the tree shows only 'Protection', but Section 2 and the quiz treat protection and security as one system service. The picture drops half of it.
- ch 6 [low] Section 2 (Number, arguments and return value): The paragraph moves from the register that carries the kernel's return value straight to '-1 means an error'. On Linux x86-64 the kernel puts a negative error code in rax (for example -9 for EBADF); it is the C wrapper that converts that to -1 and copies the code into errno. As written, a student can think the kernel itself writes -1.
- ch 6 [low] Exam traps, first bullet on read and Quiz Q6: The chapter states flatly that a read return of 0 means end of file. For a regular file that is right, but 0 only means no bytes were transferred: a read with count 0, or a pipe or socket whose writer has closed, also returns 0 without being end of file. The quiz answer gives EOF as the only meaning.
- ch 6 [low] Quiz Q3: The answer calls the trap 'the single controlled entry point' into the kernel. Interrupts and exceptions also switch the CPU to kernel mode; the trap is the controlled entry for a system call request, not the only entry.
- ch 6 [low] Section 3, Device management bullet: The standard list of device-management services also includes logically attaching and detaching devices. The bullet leaves this out, so a student listing the services for an exam answer will lose a point.
- ch 7 [high] Section 2, microkernel step list, and Quiz Q5: The step list describes a full request–reply: client makes a system call (user→kernel), kernel passes the message and the scheduler switches to the file server (kernel→user), the server replies through the kernel (user→kernel), and the kernel copies the reply back to the client (kernel→user). That is four mode switches, and two message copies (request and reply). The text then says 'each request therefore costs two mode switches and at least one message copy', which contradicts its own steps and undercounts. Q5 inherits the error: it charges only two mode switches, giving 9 µs and a 45× ratio.
- ch 7 [low] Section 1 and Quiz Q1: Section 1 describes the simple structure as a sixth design and credits it with a 'tiny kernel', while the table, the figure and Q1's answer count only five structures (monolithic, layered, microkernel, modular, hybrid). A student can either name six structures in Q1 or believe the defining benefit of the simple structure is small size, when its real property is the absence of a kernel/user boundary. In systems such as early personal-computer operating systems the privileged core was not especially small; it simply had no enforced separation from applications.
- ch 8 [low] Worked example 1, step 2: The running total is labelled "5 s after firmware", which reads as if 5 s pass after firmware finishes. The 5 s is the cumulative time at the end of the bootloader (firmware plus bootloader), so the wording can mislead a reader.
- ch 9 [high] Section 1, hash table paragraph: "Page caches and routing tables use hash tables" is wrong for the Linux kernel that the rest of the paragraph assumes. Linux keeps page-cache pages in a radix tree (now the XArray), not a hash table, and routing entries in a trie (LC-trie / FIB trie), not a hash table. A student who repeats this in an exam or viva is repeating an inaccurate claim.
- ch 9 [low] Section 1, tree paragraph: "A tree stores parent-child order" is vague; a reader may not see what is actually stored.
- ch 9 [low] Section 2 and Exam traps: The sentence "a VM runs its own guest kernel; a container shares the host kernel" appears three times (Section 2 body, last line of Section 2, and trap 3) in a short chapter.
