# c-unix-u5: free-model run

- Book: `books/cse/c-unix/c-unix-u5.html`
- Status: ok
- Model calls so far: 36 (135,507 tokens in, 246,201 out), 6.4 minutes

## Checker

```
c-unix-u5.html: 8 chapters, 14918 words, 9 figures, 161 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Worked example 1, step 5: Step 5 says exit() 'releases signal and credential resources' while keeping task_struct until wait(). The credentials (cred) and the signal state (signal_struct, and the sighand handler table) are not freed at exit. They stay attached to the zombie and are freed only when the task structure itself is finally released, after the parent reaps it.
- ch 1 [low] Section 3, PID hash table bullet (and lead): The bullet says the three views hold 'the same task_struct objects' and that the hash chain stores tasks. In current kernels the PID hash table links struct pid entries (one per task, reached through the numeric PID in a namespace) and each struct pid then points to the task_struct. A student may come away thinking the buckets hold task_struct pointers directly.
- ch 1 [low] Section 2, ppid bullet: The wording can be read as if task_struct has a ppid field. It does not have one; the parent link is real_parent (and parent), and the ppid shown in /proc is derived from real_parent->pid.
- ch 2 [high] Section 2 (interrupts and bottom halves): "Tasklets are built on softirqs, one instance per CPU" reads as if one copy of a tasklet exists per CPU and they run in parallel. The standard rule is the opposite: a given tasklet never runs on two CPUs at the same time, so it needs no locking against itself.
- ch 2 [low] Section 1 (signals): "It reports an event and carries no data" is true only for the standard signals. A signal sent with sigqueue() carries a value and a siginfo_t, and real-time signals are queued with such data.
- ch 2 [low] Section 1 (signal delivery): "It takes pending & ~blocked, clears that bit" does not say what happens when several signals are pending; a student may assume order is arbitrary or arrival order.
- ch 2 [low] Figure (Interrupt path): The edge chain top half → softirq/tasklet → workqueue suggests a workqueue always follows a softirq. The prose correctly says "softirqs, tasklets or workqueues"; the figure shows them as consecutive stages.
- ch 3 [high] Section 3, copy-on-write paragraph: It says the fault handler 'copies the frame, and marks the PTEs writable again'. If both processes' PTEs were made writable at that moment, the next write would silently change a shared frame and copy-on-write would break. Only the writer's PTE gets the new frame with write permission.
- ch 3 [high] Section 3, zones and direct map: The direct map is described as covering 'all physical RAM'. This contradicts the HIGHMEM sentence just before it: on 32-bit systems high memory is by definition not permanently mapped, so it is absent from the direct map.
- ch 3 [low] Figure: The example is 32-bit x86 two-level paging (page directory + page table), but the boxes are labelled 'PGD → PMD 1' and 'PTE 0/PTE 3'. PMD is the four-level x86-64 name and does not exist as a separate level in this walk, so the figure contradicts Section 1's own naming.
- ch 3 [low] Exam traps, second bullet: Typo 'mallocc' in a bullet students will copy into notes.
- ch 3 [low] Section 1, physical address formula: 'PTE >> 12' gives the frame number only for a 32-bit PTE. A 64-bit PTE also carries high bits such as the no-execute bit at bit 63, so a plain shift produces a garbage frame number.
- ch 4 [low] Section 2, the paragraph explaining why the holder must not sleep: The sentence 'Sleeping means calling schedule(), which can switch to another task that wants the same lock; the holder is then not running, so nobody releases it' is loose. A sleeping holder usually does release the lock later; the real trouble is that every other CPU keeps spinning (wasting cycles) and, if the wake-up itself needs that lock, the system deadlocks. As written a student may think any sleep inside a spinlock is an instant permanent deadlock, or may miss the 'other CPUs waste cycles' reason.
- ch 4 [low] Section 3, definition of a mutex: 'the count is 0 or 1' is incomplete and slightly misleading: in Linux an unlocked mutex has count 1, a locked mutex has count 0, and the count goes negative when tasks are waiting. A student may also read '0 or 1' as 'up to two holders'.
- ch 4 [low] Section 3, sentence on completions: 'A completion is a one-shot signal' can mislead. A completion counts complete() calls and is reusable: if complete(&c) runs before wait_for_completion(&c), the wait returns immediately instead of blocking, and the same completion object can be used again.
- ch 5 [low] Lead: "Two processes cannot read each other's memory" is false as written. The same chapter later shows two ways they can: shared memory (Section 2) maps the same physical pages into both, and ptrace (Section 3) reads and writes another process's memory. The intended point is only that processes do not share an address space by default, so the sentence as written will confuse a student who has just read Sections 2 and 3.
- ch 5 [low] Section 2, first sentence: Calling a socket "a pipe with an address" / "the same idea but addressed" suggests a socket is still one-way like a pipe. A connected SOCK_STREAM socket (AF_UNIX or AF_INET) is bidirectional: both ends can read and write. The addressing is not the only difference.
- ch 5 [low] Exam traps, PTRACE_PEEKTEXT bullet: waitpid on a stopped tracee does not "reap" it. It reports the stop (WIFSTOPPED); the tracee is still alive and only becomes reapable when it later exits.
- ch 5 [low] Section 1, capacity formula: The arithmetic is right only because the page size is taken as 4096 bytes. The default is 16 pages, so on a kernel built with larger pages the same ring holds more than 65536 bytes. The buffer size is also changeable at run time with fcntl(F_SETPIPE_SZ), which the chapter never mentions and a student may assume is impossible.
- ch 6 [low] Section 2, ext2 layout paragraph: The text says every block group carries a copy of the superblock and group descriptors. On a default ext2 file system (sparse_super) only group 0, group 1 and groups whose number is a power of 3, 5 or 7 keep backups; the other groups start straight at the bitmaps.
- ch 6 [low] Figure caption and aria text of the ext2 block diagram: "the inode table pointing into data blocks" and "the inode table ... holds the block pointers" make the table itself the pointer holder. The inodes inside the table hold the 15 block pointers.
- ch 6 [low] Figure, ext2 block diagram: The vertical chain puts a boot block at the top of the per-group sequence, which suggests every block group begins with a boot block. The 1 KB boot block exists only once, at the start of the file system (block 0).
- ch 6 [low] Quiz Q4 answer: The arithmetic shown is (300000 − 274432) ÷ 1024 = 24.9, but 25568 ÷ 1024 = 24.97, and the block index comes from taking the floor, which the answer does not state.
- ch 6 [low] Worked example 1, step 3 and answer: 16,843,020 KB (about 16.06 GiB) is the capacity of the pointer scheme, but it is presented as the largest ext2 file. An ext2 inode stores the size in a 32-bit field, so a real ext2 file is capped at 4 GiB, well below the counted value. As written, a student will quote 16 GiB as the ext2 file-size limit.
- ch 7 [high] Section 2, final paragraph: "Calling printf or malloc from a driver crashes the machine" states the wrong consequence. Kernel modules are linked against the kernel's exported symbols, so a call to printf or malloc normally makes the module fail to load with an "Unknown symbol" error; the machine does not crash. A student may believe the danger is a runtime panic rather than an unresolved symbol at load time.
- ch 7 [low] Section 2, return-value paragraph: "Return count on success" overstates it. A driver returns the number of bytes actually transferred, which may be less than count (a short read), and it must also advance *f_pos. As written, a student may think the return value must always equal count.
- ch 7 [low] Section 3, gendisk paragraph: The field minors is described as "how many partitions". In struct gendisk, minors is the count of minor numbers reserved for the whole device, which includes the disk itself plus its partitions (for example 16 for a SCSI disk: 1 disk + 15 partitions).
- ch 7 [low] Section 4: The whole of Section 4 (module load/unload, MODULE_LICENSE, insmod/modprobe/rmmod/lsmod/modinfo) is general module material rather than character-versus-block driver material, and it likely duplicates a separate chapter on kernel modules. Only the last two paragraphs (process context versus interrupt context) belong to this chapter.
- ch 8 [low] Section 1, affinity paragraph: The sentence "taskset -c 0 make runs make only on CPU 0" is garbled: "make" appears twice and reads as if the command runs itself. A phone reader will stall on it.
- ch 8 [high] Quiz Q2 answer: The answer contradicts itself and the section. It first says "no other CPU touches that copy", then says "without this, another CPU could see or change it". A per-CPU copy is never touched by another CPU; the real danger of leaving preemption on is that the task can migrate between reading the CPU number and using the copy, so it operates on the wrong CPU's copy.
