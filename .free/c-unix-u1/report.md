# c-unix-u1: free-model run

- Book: `work/claude_figs/c-unix-u1/tree/books/cse/c-unix/c-unix-u1.html`
- Status: ok
- Model calls so far: 29 (101,024 tokens in, 159,540 out), 5.7 minutes

## Checker

```
c-unix-u1.html: 6 chapters, 11387 words, 7 figures, 144 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Figure (gantt spec): Each milestone is drawn as a three-year bar (Unix 1969–1972, C 1973–1976, v1.0 1994–1997) even though every one of them is a single-year event. The bar end years appear nowhere in the text, so a student can read the picture as 'Unix work lasted 1969 to 1972' or 'Linux work lasted 1991 to 1994'.
- ch 1 [low] Section 2: The paragraph implies Torvalds released the kernel under the GPL from the start. The first public releases (1991) carried a more restrictive licence; the GPL was adopted a few months later, in 1992, before version 0.12.
- ch 1 [low] Section 2: 'This is one form of open source' treats the GPL as simply an open-source licence. The GPL comes from the free-software movement and gives users freedoms; 'open source' is a later, separate term with a different emphasis. Blurring them can confuse a student who later meets both terms.
- ch 1 [low] Lead: 'Linux is a free Unix-like kernel' leaves 'free' undefined at first use. A student may read it as 'no cost' rather than 'freedom to run, study, change and share', which is the sense meant and the sense the GPL section later explains.
- ch 2 [high] figure: The caption says "the kernel schedules hardware". The scheduler schedules processes (tasks), not hardware; the kernel drives or controls hardware through drivers. As written, a student can form the wrong idea of what the scheduler does, and it contradicts Section 2, which correctly says the scheduler gives turns to processes.
- ch 2 [low] section 2: "or a higher-priority event arrives" is vague. Preemption happens when a higher-priority task becomes runnable or when the running task blocks or its time slice ends. "Event" hides the key point, which is a task becoming ready.
- ch 2 [low] lead: The lead lists "Android phones" as an example of a machine that "must serve many users". A phone normally has a single user account; multi-user login is the shared-server and cloud case, not the everyday phone case. The example slightly muddles the feature being introduced.
- ch 3 [high] Exam traps, third bullet: It says "ls is a utility, cd is a built-in, read is a system call". In bash, read is itself a built-in command (read name reads a line into a variable), so a student reading this trap concludes that typing read runs a system call. The trap then teaches the opposite of what it intends.
- ch 3 [low] Section 2, "A command can be one of four things": The list has built-ins, external commands, aliases and functions, but omits shell reserved words and keywords (if, for, while, {, [[). These are also commands as far as the shell's parser is concerned, and bash resolves a command line in five kinds, not four.
- ch 3 [low] Worked example 1, step 3: argv is called "the argument list" without saying that by convention argv[0] is the program name, so the traced call execve('/bin/ls', argv, envp) looks like it passes only the word ls. A student may think argv holds just the typed words.
- ch 4 [low] Section 1, second paragraph: The sentence says a compiler or interpreter turns source into machine instructions 'often called binaries'. An interpreter does not produce machine instructions or a binary file; it executes the source statements directly. A student can take away the wrong model.
- ch 4 [low] Section 2, cost sentence: The sentence attributes the no-per-user cost to the licence, but an open-source licence never charges a fee; any per-seat charge comes from a vendor's support or subscription plan. As written it sounds as if some open-source licences do charge per seat.
- ch 4 [low] Worked example 1 and Quiz Q4: The comparison sets the open-source total (licence plus support) against the proprietary licence alone, so the saving looks larger than it would be in a fair comparison. The section itself warns to compare like with like, and a student may copy this method in the exam.
- ch 4 [low] Section 2, last sentence: 'Linux runs ... Android phones' can read as if Android were a Linux distribution like the ones in this course. Android uses the Linux kernel but is not a normal Linux system.
- ch 4 [low] Section 2, long-term benefit: 'Long-term use improves because the source survives' is vague — what improves is continuity and the ability to keep maintaining the software, not the software by itself.
- ch 5 [low] Section 1, sentence 'Only the kernel is common to every distro': This contradicts the list given just above it, which presents the shell, core utilities and package manager as parts of every distribution. A student can read the two statements as opposites, and in practice almost every distro also carries a shell and some core utilities (not always Bash).
- ch 5 [low] Exam traps, first bullet: 'Ubuntu and Fedora run the same Linux kernel' can be read as saying the kernel binary is identical. The two distros usually ship different kernel versions with different patches.
- ch 5 [low] Quiz Q4: The question does not separate dual boot from a virtual machine: dual boot also keeps all Windows files (it only shrinks a partition). A student can defend either answer, so the question has no single correct option as worded.
- ch 6 [high] Quiz Q3: The answer says ls -l prints three lines, one for .hidden, a.txt and b.txt. But ls -l without -a never shows names beginning with a dot, so .hidden is not listed. The answer contradicts the chapter's own rule in Section 2 and would teach a wrong result.
- ch 6 [low] Worked example 1, step 6: It says ls prints the names 'one per line'. On a terminal ls prints names in columns; one name per line happens only when the output is piped or redirected.
- ch 6 [low] Exam traps, last bullet: 'quote patterns such as "*.txt" when you want find or the shell to treat them literally' is muddled. Quoting stops the shell from expanding the pattern; it does not make find treat the pattern literally — find still does its own matching with it.
- ch 6 [low] Figure and its caption: The tree shows a /home/ravi/work directory with the caption 'The separate work directory was never entered', but nothing in the worked example creates or mentions a work directory. A student may think mkdir or cp produced it.
