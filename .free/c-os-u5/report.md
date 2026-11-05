# c-os-u5: free-model run

- Book: `books/cse/c-os/c-os-u5.html`
- Status: ok
- Model calls so far: 33 (105,691 tokens in, 104,578 out), 4.3 minutes

## Checker

```
c-os-u5.html: 9 chapters, 12306 words, 10 figures, 151 KB
OK
```

## For the reviewer

- chapter 7: a c program's shown output was replaced by its real output; check the text around it
- chapter 9: a c program's shown output was replaced by its real output; check the text around it
- chapter 5: a c program's shown output was replaced by its real output; check the text around it
- chapter 2: a c program's shown output was replaced by its real output; check the text around it
- chapter 8: a c program's shown output was replaced by its real output; check the text around it

## Reviewer notes (after any revision)

- ch 1 [low] Section 1, bullet list: The description "Name – unique identifier within a directory" may be misread as implying global uniqueness.
- ch 1 [low] Section 2, formula: The formula does not state the unit of blockSize, which could confuse readers.
- ch 1 [low] Quiz Q3: The answer gives the offset in KB only, while the formula expects bytes.
- ch 1 [low] Quiz Q6: The term "OS File Manager" is informal and not the standard component name.
- ch 1 [low] Section 2, bullet list: The bullet "Open the file with a system call (e.g., open())" is not an access method but a prerequisite step.
- ch 2 [high] Quiz Q5: The explanation says a balanced tree (e.g., B‑tree) halves the search space at each step, which is true for binary trees but not for B‑trees that use a higher branching factor.
- ch 2 [low] Section 1 bullet list: The statement "average search O(log N) if directories are balanced" may mislead students because most modern file systems use hash tables or B‑trees that give O(1) average lookup, not O(log N).
- ch 2 [low] Lead paragraph: Uses the phrase "pointer to the file's inode" which is not precise; the directory stores the inode number, not a direct memory pointer.
- ch 2 [low] Section 3 (Path definition): Defines a path only as a sequence of directory names, omitting that the last component can be a file name.
- ch 2 [low] Quiz Q3: The answer "/home/var" assumes a directory "var" exists under "/home", which is uncommon and may confuse students.
- ch 3 [low] Section 2, bash code example: The mount command order is unconventional; options are placed after the device path.
- ch 3 [low] Quiz Q5, answer point 2: It claims that mounting read‑only makes the OS report the underlying device’s used space, which is incorrect.
- ch 3 [low] Quiz Q5, answer point 1: It suggests that files already present in the mount‑point directory can cause 0 B free space after a successful mount, which is misleading.
- ch 3 [low] Section 1, bullet about bind mounts: Describes bind mounts as “multiple mount points can refer to the same source”, which may imply the same device; bind mounts actually attach an existing directory subtree, not necessarily the same source device.
- ch 4 [high] Section 1, bullet list: The statement "Superblock: immutable after creation" is incorrect. Many fields in the superblock (e.g., free block count, timestamps) are updated during normal operation.
- ch 4 [high] Quiz Q5 (apply, 6 marks): The answer describes FAT using "inode" terminology, but FAT does not have inodes; it uses directory entries that contain starting cluster numbers.
- ch 4 [low] Quiz Q2 (understand): The answer claims a bitmap allows O(1) allocation "by scanning bits", which is misleading because scanning the bitmap can be O(n) in the worst case.
- ch 4 [low] Section 3, bullet list: The bullet "VFS provides portability across different storage media" is vague; VFS provides portability across different file‑system types, not media.
- ch 4 [low] Worked example 1, dry‑run representation: The JSON‑like "dry run" table is confusing for readers and adds no educational value.
- ch 5 [high] Section 1 (Contiguous allocation): The formula labeled "Fragmentation = Block size – (File size mod Block size)" computes internal fragmentation, but the text describes external fragmentation.
- ch 5 [high] Section 2 (Linked allocation) – step description: The step says "write the address of the previous block into its pointer field", which reverses the direction of the link.
- ch 5 [high] Section 2 (Linked allocation) – pointer direction example: The Python example prints "Block 30 points to 31" etc., which matches forward linking, but the textual description contradicts it.
- ch 5 [low] Quiz Q5 (time to read 4th block): The answer ignores the time to actually read the data block after the index lookup, giving only 1 ms for indexed allocation.
- ch 5 [low] Worked example code for indexed allocation: The array `indexed[]` contains the index block (40) together with data blocks, which may confuse readers who expect only data block numbers.
- ch 6 [high] Quiz Q6: The answer assumes a 32‑bit integer can address 2³² blocks, but a 32‑bit bitmap has only 32 bits, so it can represent at most 32 blocks.
- ch 6 [high] Beyond section: It repeats the same incorrect claim that a 32‑bit integer can address 4,294,967,296 blocks.
- ch 7 [high] Lead paragraph: The opening sentence says "I/O hardware uses three mechanisms to move data between a device and memory: polling, interrupts and DMA." Polling and interrupts do not move data; they only detect or signal data readiness.
- ch 7 [low] Figure specification: The figure is described as a sequence for polling, interrupt and DMA, but the listed messages only cover polling status and DMA transfer. No interrupt‑related messages are included, and the actor list includes DMA even for polling and interrupt cases.
- ch 7 [low] Section 2 (Interrupt‑driven I/O) bullet point: The statement "Latency is usually a few microseconds on modern CPUs" is overly optimistic; typical interrupt latency is often tens of microseconds depending on the OS and hardware.
- ch 7 [low] Section 1 (Polling I/O) formula description: t_busy is defined only as "time spent reading the status register", which ignores the loop overhead and other CPU work performed during polling.
- ch 7 [low] Section 1 bullet list: The bullet "CPU waste: the loop runs at the speed of the processor" may be unclear to students.
- ch 8 [high] Section 1: The I/O software stack order is contradictory. Earlier it says the request passes through a buffer cache before the driver, but the listed stack order is Application → OS API → Driver → Buffer Cache → Device.
- ch 8 [high] Quiz Q1: The answer lists the layers in the wrong order (Application → OS API → Driver → Buffer Cache → Device).
- ch 8 [low] Section 2: It states that a small kernel buffer is allocated for each open file. In modern OS kernels the buffering is done via the page cache, not a per‑open‑file kernel buffer.
- ch 8 [low] Section 2, formula B = Bsize × Nreads: The formula assumes every read transfers a full buffer, which is false when the file size is not an exact multiple of the buffer size.
- ch 8 [low] Quiz Q4: The answer assumes a 4 KB block size without stating it, which may confuse students.
- ch 9 [high] Section 3, Worked example 1 (SCAN part): The SCAN algorithm is described as stopping at the last request (90) and then reversing, which is actually the LOOK algorithm. SCAN should continue to the outermost cylinder of the disk before reversing.
- ch 9 [low] Section 1, bullet "Sectors per track": The sentence says sectors per track defines rotational latency; more sectors mean less wait for a given sector. Rotational latency is the time for half a rotation on average and does not depend on the number of sectors.
- ch 9 [low] Section 2, formula for Transfer time: The formula "Transfer time equals (Sector size ÷ Data rate)" does not mention that the result is in seconds (or milliseconds) after unit conversion.
