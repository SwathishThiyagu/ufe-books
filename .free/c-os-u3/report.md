# c-os-u3: free-model run

- Book: `books/cse/c-os/c-os-u3.html`
- Status: ok
- Model calls so far: 44 (151,637 tokens in, 157,815 out), 7.6 minutes

## Checker

```
c-os-u3.html: 8 chapters, 11819 words, 9 figures, 142 KB
OK
```

## For the reviewer

- chapter 3: a c program's shown output was replaced by its real output; check the text around it
- chapter 4: a c program's shown output was replaced by its real output; check the text around it
- chapter 6: a c program's shown output was replaced by its real output; check the text around it
- chapter 1: a c program's shown output was replaced by its real output; check the text around it
- chapter 1: give 6 to 8 quiz questions
- chapter 8: give 6 to 8 quiz questions
- chapter 7: a python program's shown output was replaced by its real output; check the text around it
- chapter 7: the figure cannot be drawn: tree label "Check request ≤ need?" is too long; shorten it

## Reviewer notes (after any revision)

- ch 1 [high] Section 3 (naive flag solution), code output description: The explanation says the program often prints "final x = 1" because both threads read the flag as 0 before either writes 1. If both threads read the flag as 0 they will both enter the critical section and increment, producing final x = 2, not 1. The value 1 occurs when the second thread sees the flag as 1 and skips the increment.
- ch 1 [low] Worked example 1, step 2 description: The sentence "The only way to change the final value is the order of the two read actions" is misleading because the order of writes (and the interleaving of read‑modify‑write steps) also influences the final result.
- ch 2 [high] Section 1, bullet list: The bullet "Only one of flag[0] or flag[1] can be true while the other is waiting" is false. Both flags can be true at the same time; the turn variable decides which process proceeds.
- ch 2 [high] Section 1, formula: The formula uses the assignment operator "turn = j" instead of the equality operator.
- ch 2 [high] Worked example 1, code snippet: The code calls thread0() and then thread1() sequentially, so T1 never arrives while T0 is still in the while loop. This contradicts the narrative of the example.
- ch 2 [low] Section 2, mutual exclusion explanation: The text uses "turn = j" instead of the equality comparison "turn == j", which can confuse readers.
- ch 2 [low] Quiz Q5 answer: The answer states that a CAS lock can be blocked by the OS, which is not a property of the CAS primitive itself.
- ch 2 [low] Quiz Q8 answer: The starvation scenario described focuses on priority inversion rather than the lack of fairness inherent in a pure test‑and‑set spinlock.
- ch 2 [low] Section 3, test‑and‑set description: The phrase "reads a bit and sets it to 1" oversimplifies the operation.
- ch 3 [high] Section 2: Binary semaphore as a lock: The description of the V (signal) operation is contradictory. First it says "if S = 0, set S ← 1 and wake one blocked process". Later it says "V increments the value if it is 0; otherwise it does nothing". In a binary semaphore, when a blocked process exists, V should wake one waiting process and leave the semaphore value at 0, not set it to 1.
- ch 3 [high] Exam traps: The trap states that using V on a locked binary semaphore without a waiting process can cause the value to become 2, which is illegal. In reality, V on a locked binary semaphore (value 0) with no waiting process sets the value to 1, never to 2.
- ch 3 [low] Quiz Q4: The provided C fragment omits the required header file and declares the lock as a plain int, which is not safe for the atomic built‑ins used.
- ch 3 [low] Section 1: Mutex lock basics: The text does not mention that the process that acquires a mutex must be the one that releases it. This ownership rule is essential for correct mutex usage.
- ch 3 [low] Section 2: Binary semaphore as a lock: The explanation omits the fact that a binary semaphore does not enforce ownership, unlike a mutex. A process can perform V without having performed a prior P, which can lead to logical errors.
- ch 4 [high] Quiz Q5: The question uses broadcast(notEmpty) in the get() procedure, but get() should signal notFull. The answer also says producers wait on notEmpty, which is wrong; producers wait on notFull.
- ch 4 [low] Quiz Q1: The answer lists four components (shared data, procedures, condition variables, implicit lock) while the question asks for three components.
- ch 4 [low] Section 2, bullet list for wait operation: The first bullet "Acquire monitor lock" is unrelated to the wait operation and may confuse students.
- ch 4 [low] Bounded‑buffer example, shown output placeholder: The placeholder "[shown output]" does not display the actual output of the program.
- ch 5 [high] Section 1 (System model for deadlock analysis): The formula Σi Aij + Σi Qij = Ej is incorrect. The request matrix Q contains the remaining need, not the total demand, so allocated plus still‑needed does not necessarily equal the total instances.
- ch 5 [low] Worked example 1, step numbering: Step 9 is labeled "Step 5" causing a numbering mismatch.
- ch 5 [low] Section 2 (Four necessary conditions for a deadlock): The description of the circular‑wait condition mentions only processes, omitting the resources they wait for, which may confuse students.
- ch 5 [low] Section 2, terminology: The text says the four conditions are called the “Deadlock System Model”, which is not the standard term.
- ch 5 [low] Section 2, checklist after bullet list: The list of actions (identify allocation, identify request, check conditions, etc.) is not introduced and looks like a continuation of the bullet list, which may be unclear.
- ch 6 [high] Lead paragraph: The sentence "By breaking the condition, the system cannot enter a circular wait." is inaccurate because breaking any one of the four necessary conditions prevents deadlock, but it does not necessarily prevent a circular wait from forming if a different condition remains satisfied.
- ch 6 [low] Exam traps, bullet 1: The wording is confusing: it says eliminating mutual exclusion alone guarantees deadlock‑free execution, then adds that other conditions may still form a cycle, which seems contradictory.
- ch 6 [low] Section 3, preemption description: Memory pages are described as consumable resources, which is inaccurate; pages are sharable and can be swapped, not consumed like CPU time.
- ch 7 [high] Section 3 (Worked example): The allocation matrix (P0:0,1; P1:2,0; P2:3,0) uses 5 units of resource A while only 3 units exist, giving a negative Available vector (‑2,1). This makes the example inconsistent and unrealistic.
- ch 7 [high] Quiz Q3: The answer states that the safety test fails and the request must be denied, but the correct safety test succeeds, so the request should be granted.
- ch 7 [low] Section 2 (Banker's safety algorithm): The step description says "Check request ≤ Need; if not, raise error." This wording suggests an error rather than a normal denial.
- ch 7 [low] Python code comment: Comment reads "# prints True if safe" which may be misread as the code always prints True.
- ch 7 [low] Exam traps bullet "Treating a safe state as automatically deadlock‑free without verifying that all processes can actually finish.": The statement is redundant because the definition of a safe state already guarantees a sequence for all processes to finish.
- ch 8 [high] Worked example 1, step 9 (Recovery): The recovery step says aborting process P4 releases its request (1,1,1) and makes Available = (1,1,1). Aborting a process releases only the resources it currently holds, not the resources it is requesting. P4 holds no printers, so terminating it does not free any printer and the deadlock remains.
- ch 8 [low] Section 2 (Detection for multiple‑instance resources): The description introduces the Work vector but does not define the Finish vector, which is used in the algorithm steps.
