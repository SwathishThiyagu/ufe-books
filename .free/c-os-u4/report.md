# c-os-u4: free-model run

- Book: `books/cse/c-os/c-os-u4.html`
- Status: ok
- Model calls so far: 41 (131,344 tokens in, 143,337 out), 6.1 minutes

## Checker

```
c-os-u4.html: 9 chapters, 11951 words, 10 figures, 148 KB
OK
```

## For the reviewer

- chapter 3: a c program's shown output was replaced by its real output; check the text around it
- chapter 5: a c program's shown output was replaced by its real output; check the text around it
- chapter 1: a c program's shown output was replaced by its real output; check the text around it
- chapter 2: a c program's shown output was replaced by its real output; check the text around it
- chapter 8: a c program's shown output was replaced by its real output; check the text around it
- chapter 9: a c program's shown output was replaced by its real output; check the text around it
- chapter 9: worked example 1: the worked example states [1.0] but recomputing it gives [3.0, 3.0]; fix the steps and the answer so they match the correct values
- chapter 9: the reviewer found 1 serious problem(s) and the revision did not pass the checks; read the review in the state folder

## Reviewer notes (after any revision)

- ch 1 [high] Quiz Q3 (apply, 4 marks): The computed page number and offset are incorrect. For an 8 KB page (size 0x2000) the logical address 0x1C23 is less than one page, so the page number should be 0 and the offset should be 0x1C23 (7203 decimal). The answer given (page number = 1, offset = 0xC23) is wrong.
- ch 1 [low] Section 3 (Logical, physical, and virtual addresses): The statement "If the logical address is larger than the limit, the OS raises an out‑of‑bounds fault" is imprecise. The fault occurs when the logical address is greater than or equal to the limit (size).
- ch 2 [high] Section 1: The text says each swapped‑out process is written to a contiguous region of the swap area. In most operating systems the swap image may be stored in non‑contiguous blocks; contiguity is not required.
- ch 2 [low] Section 1: The statement “Swap space size is usually a multiple of RAM (e.g., 2× RAM)” is outdated and can mislead students, as modern systems often use smaller or larger swap sizes depending on workload.
- ch 2 [high] Quiz Q3: The answer incorrectly assumes that four 10 MB processes can reside in 24 MB of RAM and that three resident processes exist before swapping. In reality only two 10 MB processes (20 MB) can fit; a third process already requires swapping.
- ch 3 [high] Section 1 (Fixed and dynamic partitions): The text says that in dynamic (variable‑size) partitions the leftover hole size becomes internal fragmentation. In reality, allocating exactly the process size means internal fragmentation is zero; the leftover hole contributes to external fragmentation.
- ch 3 [low] Section 2 (External fragmentation definition): Definition ties external fragmentation to a pending request, which can be confusing.
- ch 3 [low] Section 3 (Compaction description): Mentions updating the base address in a page table, which is not relevant for pure contiguous allocation.
- ch 4 [high] Section 3 table: EAT values are miscalculated. For h = 0.5 the correct EAT is 151.0 ns (0.5×101 ns + 0.5×201 ns). For h = 0.95 the correct EAT is 106.0 ns (0.95×101 ns + 0.05×201 ns). The entry for h = 0.8 is correct.
- ch 4 [high] Quiz Q5: EAT calculations use wrong numbers. With hit cost = 101 ns and miss cost = 201 ns, EAT for h = 0.7 is 131.0 ns, not 132.0 ns. For h = 0.85 it is 116.0 ns, not 112.6 ns. The stated reduction of 19.4 ns is therefore incorrect.
- ch 4 [low] Section 2 bullet list: The bullet for a miss says “read the page table from RAM, then update the TLB”. It omits that after the page‑table lookup the actual data access still occurs.
- ch 4 [low] Section 3 text: The phrase “Doubling the hit ratio from 0.5 to 1.0” is misleading because 1.0 is not double 0.5.
- ch 5 [high] Quiz Q4: Frames count is computed incorrectly. 2 GiB is 2³¹ bytes, not 2²³. The answer uses 2²³ / 2¹² = 2¹¹ = 2,097,152 frames, which is wrong. Correct frames = 2³¹ / 2¹² = 2¹⁹ = 524,288 frames. Consequently the table size should be 524,288 × 8 B = 4,194,304 bytes = 4 MiB, not 16 MiB.
- ch 5 [low] Section 1, entry size formula: The abbreviation PFN (Page Frame Number) appears without a prior definition.
- ch 6 [high] Worked example 1, step 3: The example checks "Offset ≤ Limit" while the definition of a valid offset requires Offset < Limit. Using ≤ would allow an offset equal to the limit, which points one byte past the segment.
- ch 6 [high] Section 2, C code example: The code treats the logical address as an absolute address and computes offset as "logical - base". In true segmentation the logical address is a (segment number, offset) pair; the offset is not obtained by subtracting the base.
- ch 6 [low] Lead paragraph: It says segmentation is used in "older UNIX variants", but classic UNIX used a flat memory model and did not rely on segmentation.
- ch 6 [low] Section 1, bullet list: The description of protection bits mentions only read, write, execute flags.
- ch 7 [high] Quiz Q4: The answer states that using a larger page size can reduce thrashing. This is not generally true; larger pages increase the amount of data transferred per fault and can worsen thrashing. Standard textbooks list increasing frames or reducing the working set as ways to reduce thrashing, not larger page size.
- ch 7 [low] Quiz Q4 answer explanation: The answer says "All three can be effective depending on context" which is vague and contradicts the correction above.
- ch 7 [low] Section 2 formula: The effective access time formula omits the memory access time for the case when a page fault occurs. The more precise formula is EAT = (1‑p)×ma + p×(pf_time + ma).
- ch 8 [high] answer section: The answer states FIFO incurs 10 faults, but the correct number of FIFO page faults for the given reference string with 3 frames is 9 (as shown by the C code output and by manual FIFO simulation).
- ch 8 [low] Section 2 (LRU and Optimal): The statement "LRU needs hardware support (e.g., reference bits)" is inaccurate; pure LRU requires full ordering of accesses, which is usually approximated with hardware reference bits in the Clock algorithm.
- ch 8 [low] Figure description: The description of the reference‑string simulation figure is vague and the JSON‑like spec is not explained, making it hard for students to understand what the marks mean.
- ch 9 [high] Section 2 (Global vs local replacement): The Python function select_victim uses the variable faulting_proc without defining it or passing it as a parameter, causing a NameError. The lambda for local replacement also relies on this undefined variable.
- ch 9 [low] Section 1 (Proportional frame allocation): The description calls F "the total number of free frames" which can be confusing because the formula uses the total number of frames available for allocation, not only currently free ones.
- ch 9 [low] Section 2 (Global vs local replacement): The placeholder "[shown output]" is left without any actual output, leaving the reader without a concrete example.
- ch 9 [low] Section 3 (Working‑set model and thrashing detection): The statement "If the sum of all working‑set sizes exceeds the total frames, the system thrashes" is presented as a definition, but it is actually a sufficient condition for thrashing, not a strict definition.
