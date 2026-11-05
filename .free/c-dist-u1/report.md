# c-dist-u1: free-model run

- Book: `books/cse/c-dist/c-dist-u1.html`
- Status: ok
- Model calls so far: 28 (107,109 tokens in, 219,179 out), 7.2 minutes

## Checker

```
c-dist-u1.html: 8 chapters, 14412 words, 9 figures, 151 KB
OK
```

## For the reviewer

- chapter 2: the figure cannot be drawn: note "not Flynn" runs off the right edge; shorten it
- chapter 2: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [high] Section 2, instruction level: The pipeline example is factually wrong for a standard pipeline. In a classic 5-stage pipeline, when instruction 1 is writing its result (WB), the instruction in the decode (ID) stage is three stages behind it, not instruction 2. As written, a student pictures two adjacent instructions in WB and ID at the same instant, which no pipeline does.
- ch 1 [low] Section 1, power formula note: 'Halving V cuts P four times' is ambiguous English; a student may read it as cutting power by 4 W or as four separate cuts.
- ch 1 [low] Section 2, bit level: Carry look-ahead is a fair example of bit-level parallelism, but a carry-save adder is a way of deferring carries (used in multipliers), not an example of a wider word doing more work per operation. Listing it here blurs the definition.
- ch 2 [low] Section 2, paragraph starting 'Shared-memory SIMD algorithms': 'Shared-memory SIMD algorithms' mixes two separate ideas. SIMD is about one instruction stream over many data items, not about shared memory, so a student may think SIMD requires shared memory or is a memory model.
- ch 2 [low] Figure (classification tree): The lead and the table say there are four Flynn classes, but the tree shows only SISD, SIMD and MIMD as children; MISD appears only as a small note on the root. A student revising from the figure alone can miss MISD.
- ch 2 [low] Section 1 and Section 3, chapter cross-references: Chapter 1.3 and Chapter 1.8 are named in plain text instead of being links, so the reader cannot jump to them from the phone.
- ch 3 [low] Section 2, send/receive paragraph: The asynchronous send is described but the buffer-reuse hazard is not stated, so a student may reuse or overwrite the send buffer while the transfer is still in progress and get corrupted data.
- ch 3 [low] Section 2 vs Beyond: Section 2 says flatly that a node cannot load or store an address in another node's RAM, but the Beyond paragraph introduces RDMA, which does let one node read or write another node's memory without the remote processor's involvement. The two statements look contradictory as written.
- ch 3 [low] Section 1, SIMD sentence: 'The tree and mesh machines are network forms' is loose: trees and meshes are interconnection-network topologies, not classes of machine, so the phrase can confuse a reader about what is being classified.
- ch 3 [low] Figure spec: In a top-down chart the network block sits above the node block, and the edge runs from the nodes upward to the network, so the picture mixes the two halves instead of showing messages passing between nodes.
- ch 4 [low] Section 1, 'no contention cost': A student can read 'no contention cost' as 'contention does not exist in PRAM', which then contradicts Section 2, where concurrent access to the same cell is exactly what EREW, CREW and CRCW restrict.
- ch 4 [low] Section 1 formula and Worked example 1, step 3: The chapter equates cost with work, then charges all P processors for every round. In the tree combine only 4, then 2, then 1 processors are active, so the real work is 7 combines, while 'cost' by the definition C = T × P is 24. The two numbers measure different things and a student will confuse them.
- ch 4 [low] Section 3, first paragraph: 'EREW must serialise a CRCW write conflict' suggests one-writer-at-a-time, which would take P rounds, and then the same paragraph says the tree does it in ⌈log₂ P⌉ rounds. The word and the number disagree.
- ch 4 [low] Quiz Q4, answer: 'Cost 1000 also means the parallel work equals 1000 sequential steps in the model, which bounds useful speedup' mixes processor-time with sequential steps and is only true if every processor is busy in all 10 steps. The correct bound needs the sequential run time T₁.
- ch 4 [low] Quiz Q6: The question states the answer inside itself ('while EREW simulation costs O(log P)') and 'EREW simulation' is ambiguous about which direction is simulated.
- ch 5 [high] worked example 1, step 1 (and the answer line): A 2 × 4 mesh has no node of degree 4. With only two rows, every node has exactly one vertical neighbour, so the largest degree is 3 (two horizontal links for an inner column, plus the vertical link). The reasoning 'an inside node touches 2 horizontal and 2 vertical links' is impossible in a mesh with two rows; degree 4 needs at least three rows and three columns.
- ch 5 [high] section 4, 'Mesh into hypercube', and quiz Q7: Writing i and j side by side in plain binary does not give dilation 1. Consecutive coordinates often differ in several bits, for example j going 1 → 2 (01 → 10, two bits) or i going 3 → 4 (011 → 100, three bits). One mesh link then becomes a hypercube path of up to ⌈log₂ k⌉ hops, so the stated dilation is wrong and the claim that the mesh runs at full speed fails.
- ch 5 [high] section 3, butterfly paragraph: The butterfly has no links inside a stage. The four links of a switch are two to the previous stage and two to the next stage (the straight link and the link that flips bit i). 'Inside a stage a node links to its immediate neighbours (rank links)... two inside its stage and two across' is a different network and contradicts the standard multistage butterfly definition.
- ch 5 [high] section 4, 'Tree into hypercube': Two errors. First, a complete binary tree of height n has 2ⁿ⁺¹ − 1 nodes, about twice the 2ⁿ nodes of the n-cube, so it cannot sit in the cube at one node per node. Second, 'congestion 1' is not the standard result: the complete binary tree does not even embed with dilation 1, because the 7-node tree has 5 nodes on one side of its bipartition while the 3-cube has only 4 on each side.
- ch 5 [low] section 4, list of other topologies (pyramid bullet): Degree 7 matches no usual definition of the pyramid: a node with four children and one parent has degree 5, and degree 9 if every level also has the four in-plane neighbours. The diameter is also overstated: a pyramid with 21 nodes has diameter 4, close to log₂ N, not 2 log₂ N.
- ch 6 [high] Section 1 (cost and work paragraph): The chapter says cost and work "carry different units, so do not compare them directly", but the efficiency formula given three lines earlier is exactly the comparison of the two: E = T₁ ÷ (p × Tₚ) = work ÷ cost. A student reading both statements will be confused about whether work and cost may be divided.
- ch 6 [low] Section 2 (step from the time bound to Amdahl's law): "Divide T₁ by both sides" is ambiguous; it reads as dividing the number T₁ by two sides rather than dividing T₁ by each side of the inequality.
- ch 6 [low] Section 2 (Gustafson's law): The same symbol f is used twice with different meanings: the serial fraction of the one-processor time in Amdahl's law, and the serial fraction of the parallel run in Gustafson's law. Students will carry f = 0.1 from Amdahl straight into S′ = f + p(1 − f) and get a wrong answer.
- ch 6 [low] Beyond box: The roofline model does not plot achieved speedup. It plots attained floating-point performance (FLOP/s) against arithmetic intensity (FLOP per byte), bounded by peak floating-point rate and by memory bandwidth.
- ch 7 [low] Section 2 and Exam traps (fourth trap): The sentence on waiting is muddled: 'that wait appears as idle time even when the processor has no ready task' (and the trap repeats 'is idle even if its processor has no work'). A processor with no ready task is idle anyway, so the sentence says nothing and clashes with the chapter's own definition idle = P × T − W, where waiting inside a task's cost would not show up as idle at all.
- ch 7 [low] Section 2 formula block and Worked example 1: The makespan symbol T collides with the task labels T1…T8 used throughout the chapter, so 'T = max(load₁, …, load_P)' next to 'T1–T3' reads badly.
- ch 7 [low] Quiz Q2: The question says 'equal total work per processor' with no mention of dependencies. Under the chapter's formula, equal loads with no waiting give makespan = W/P and idle = 0, so the premise as written looks false until the answer adds dependencies.
- ch 8 [low] Lead and Section 1; Quiz Q2: Calling data-parallel training 'SIMD at a larger scale' is loose. Flynn's SIMD means one instruction stream in lockstep over many data lanes, which is what a GPU lane or vector unit does. Separate replicas on separate devices each run their own instruction stream with their own control flow, so the standard label for distributed data parallelism is SPMD (single program, multiple data). A student can carry the wrong definition into a Flynn-taxonomy question.
- ch 8 [low] Section 1 formula and Q3: B_dev = B ÷ P silently assumes the global batch divides evenly by the number of devices. With B = 100 and P = 8 a student gets a fractional 12.5 examples per device and no guidance.
