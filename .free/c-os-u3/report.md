# c-os-u3: free-model run

- Book: `books/cse/c-os/c-os-u3.html`
- Status: ok
- Model calls so far: 40 (134,980 tokens in, 137,733 out), 5.6 minutes

## Checker

```
c-os-u3.html: 8 chapters, 11807 words, 9 figures, 139 KB
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
- chapter 7: the reviewer found 3 serious problem(s) and the revision did not pass the checks; read the review in the state folder

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
- ch 7 [high] Section 3, worked example: The allocation matrix uses more units than the total resources (A: 0+2+3 = 5 > 3, B: 1+0+0 = 1 ≤ 2). This makes Available negative and forces an artificial correction to (0,1), which is not a valid example.
- ch 7 [high] Section 3, pretend allocation step: After correcting the allocation, the pretend allocation still subtracts the request (1,0) from Available (0,1), producing a negative Available' = (‑1,1). The Banker's algorithm must first check that the request does not exceed the current Available; a negative Available' is impossible.
- ch 7 [high] Quiz Q3: The answer states that the request should be denied because the safety test fails. With the given data (Available = (2,1), Allocation = [[1,0],[0,1]], Max = [[2,1],[1,2]], request = (1,1)), the safety test actually succeeds, so the request must be granted.
- ch 7 [low] Section 2, Banker's safety algorithm: The algorithm description omits the required check that the request does not exceed the currently Available resources.
- ch 7 [low] Section 3, worked example narrative: The sentence "Since negative availability is impossible, the initial state is already unsafe; however, for the purpose of the algorithm we treat Available as (0,1) after correcting the input error" is confusing and hides the real mistake in the data.
- ch 8 [high] Worked example 1, step 9 (Recovery): The recovery step says aborting process P4 releases its request (1,1,1) and makes Available = (1,1,1). Aborting a process releases only the resources it currently holds, not the resources it is requesting. P4 holds no printers, so terminating it does not free any printer and the deadlock remains.
- ch 8 [low] Section 2 (Detection for multiple‑instance resources): The description introduces the Work vector but does not define the Finish vector, which is used in the algorithm steps.
