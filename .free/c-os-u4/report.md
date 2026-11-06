# c-os-u4: free-model run

- Book: `books/cse/c-os/c-os-u4.html`
- Status: ok
- Model calls so far: 27 (98,611 tokens in, 201,578 out), 5.2 minutes

## Checker

```
c-os-u4.html: 9 chapters, 15575 words, 10 figures, 173 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 2, base and limit registers: The limit register is said to hold the size 'in bytes or words' while the offset is what the CPU sends. If the limit is in bytes and the offset counts words, the comparison mixes units and the check gives wrong results. A student may not notice the mismatch.
- ch 1 [low] Section 2, last paragraph: 'In a multiprocessor or time-sharing machine, each process has its own base and limit' suggests the private base/limit pair is a feature of multiprocessors or time-sharing. Every process in any multiprocess system has its own pair; time-sharing only makes the reloading on context switch frequent.
- ch 1 [low] Section 1, last paragraph: 'The OS keeps the mapping private to each process, which is the base of protection' is loose wording; the mapping is not what is private, the registers and address space are, and 'base of protection' can be read as the base register.
- ch 2 [high] Section 3, bullet on Android and iOS: "Android and iOS normally do not swap at all" is wrong for Android. Android does swap, but into a compressed region of RAM (zram), which the chapter itself calls "compressed RAM swap" in the Beyond section. The next sentence ("Android compresses some pages in RAM") contradicts the first, and a student could write in an exam that Android never swaps.
- ch 2 [low] Section 1, last paragraph: "Swapping out a process that will be needed again within a few microseconds" uses a time scale that does not fit process scheduling; a student may read it literally as a hard cutoff.
- ch 2 [low] Figure, node 'in': The note "2.01 s for next process" silently assumes the incoming process is also 100 MB, the same size as the victim. The copy-in time depends on the incoming process's own size.
- ch 2 [low] Section 3, Unix-style bullet: "the rest of the time they reclaim pages and drop clean file pages" is muddled: reclaiming pages and dropping clean file pages are the same activity, and reclaiming may itself send pages to swap.
- ch 3 [low] Figure: The first-fit row shows 288 KB and the worst-fit row shows 388 KB, but these are not among the five starting holes named in the title (100, 500, 200, 300, 600 KB). They are leftovers created earlier in the same run, so a student reading the table before the worked example sees numbers that cannot be traced to the given holes.
- ch 4 [low] Section 2, fourth bullet (wired entries): The phrase 'code that must never fault' is misleading. A wired TLB entry guarantees the translation is never evicted, so that code never takes a TLB miss. It has nothing to do with page faults, and a student may read 'fault' as 'page fault'.
- ch 4 [low] Section 3, first sentence: The 'so' gives the wrong cause. The PTBR changes on every context switch because each process has its own page table, not because the page table lives in memory.
- ch 4 [low] Section 3, last sentence: The dirty bit is not 'checked' during translation. The valid and protection bits are checked; the dirty bit is set by the hardware on a write so that the OS knows the page must be written back.
- ch 4 [low] Quiz Q3 answer: The arithmetic jumps from 2 × 2048 straight to 4096, so a student cannot see how the remainder 904 is obtained.
- ch 5 [high] Section 1, formula box: The definition says 'n is the number of offset bits, with page size = 2n bytes'. As written this reads page size = 2 × n bytes, which is wrong (for n = 12 it would give 24 bytes instead of 4096 bytes). The superscript was lost in this one place, while the rest of the chapter correctly uses 2ⁿ.
- ch 5 [low] Figure (blocks spec): The flow puts p2 after the outer table and draws an edge from the outer table to p2, which suggests p2 is produced by the outer table. In reality p1, p2 and d are all slices of the same address; the outer table entry points to the inner table, and p2 indexes inside that inner table.
- ch 6 [high] Section 3 (paged segmentation paragraph): It says the segment-table entry holds "the base and length of that segment's page table". The entry holds the page table's base address, but the length field is still the segment's own limit (its length in bytes), which the hardware keeps checking offsets against. The page table's size is not stored in the entry; it follows from the segment limit divided by the page size. A student will wrongly think the limit becomes a page-count bound.
- ch 6 [low] Worked example 1, answer line: The last sentence, "The check prints 143 and then 1 for each of the three traps", refers to the output of a program that the chapter never shows. Read literally, a student may think the trapped accesses produce a physical address of 1, or look for missing code.
- ch 7 [high] Section 2: The page fault and its cost: When a victim frame is reused, the handler never invalidates the victim page's PTE. The old PTE still has valid 1 and points to the frame, which now holds a different page, so a later reference to the victim page can read the wrong page.
- ch 7 [low] Section 2: The page fault and its cost: The handler says the needed page is read from swap space and a dirty victim is written to swap space. File-backed pages, such as mmap pages or program text, come from and go to their file, not swap.
- ch 7 [low] Worked example 1, step 6: The expression 1 ÷ 2.500062502 × 10⁻⁶ is evaluated left to right as (1 ÷ 2.500062502) × 10⁻⁶, not as 1 ÷ (2.500062502 × 10⁻⁶), so the written expression does not equal 399,990.
- ch 7 [low] Section 3: Copy-on-write and vfork: It says all shared pages are marked read-only and that a write by either process causes a COW copy. A page that was already read-only, such as a code page, must not be copied on a write; writing it is a protection error.
- ch 8 [low] Figure description (after Section 3): It says 'OPT avoids loading pages that will not be used soon'. OPT cannot avoid loading: every referenced page that is not in a frame must still be brought in and counts as a fault. What OPT does is choose the victim whose next use is farthest away.
- ch 8 [low] Worked example 1, step 4, reference 3: At that fault, frames hold 1, 2, 5, and pages 1 and 2 are both never used again. The notes say 'evict 1; 1 never used again' without saying that evicting 2 would give the same 7 faults, so a student may think the choice is forced.
- ch 8 [low] Section 3, paragraph on exact LRU: 'doing that in software would double the cost of each access' is an unsupported number; a software stack search is far more than double.
- ch 8 [low] Lead: 'The choice is invisible until the next fault' is vague; readers may not see what is invisible.
- ch 8 [low] Lead: The second sentence lists the chapter's contents ('This chapter counts faults ... explains Belady's anomaly ...'), which is filler of the 'in this chapter we will' kind.
- ch 9 [low] Section 1, equal allocation sentence: The sentence says 'When m frames are free', but m is the total usable frame count, not the number of free frames. A student can read it as dividing only the currently unallocated frames among processes, which contradicts the formula that defines m as 'the number of usable frames'.
- ch 9 [low] Section 1, proportional allocation: The section never says that the computed share must still respect the minimum-frame floor from the first paragraph. With many small processes, floor(m × s_i ÷ S) can fall below the minimum, and the chapter gives no instruction for that case.
- ch 9 [low] Section 3, memory compression paragraph: 'Only a few universities teach it' is attached to memory compression, a real kernel technique, not a syllabus topic. It reads as a claim about how rare the technique is, which is not what is meant and is not verifiable here.
- ch 9 [low] Worked example 1, part (c) and step 7: Part (c) never says which process the reference string belongs to, and step 7 compares a working-set size 'in pages' with 100 'frames' without saying that one page occupies exactly one frame.
- ch 9 [low] Beyond section: 'Cloud hosts overcommit memory and rely on ballooning and hotplug to correct mistakes' implies ballooning fixes errors. Ballooning and hotplug are planned mechanisms for reclaiming memory from guests, not error recovery.
