# c-dist-u3: free-model run

- Book: `work/claude_figs/c-dist-u3/tree/books/cse/c-dist/c-dist-u3.html`
- Status: ok
- Model calls so far: 29 (110,121 tokens in, 213,807 out), 14.3 minutes

## Checker

```
c-dist-u3.html: 7 chapters, 13739 words, 8 figures, 178 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [high] Worked example 1, code and steps 1–8: The question asks for a program that uses 4 threads, but the code sets no thread count. There is no num_threads(4) clause on the pragma and no omp_set_num_threads(4) call, so the runtime uses its default team size, usually one thread per core. The four block sums in steps 2–8, the dry-run table and the final answer therefore do not follow from the code shown. Step 1 also says 'the compiler must split them across 4 threads', which is wrong: the compiler emits the parallel code, but the run-time library decides how many threads run.
- ch 1 [low] Section 2, reduction operators: The list of reduction operators is incomplete. It omits the valid C/C++ operators ^, &&, || and − (subtraction), so a student may think only +, *, min, max, &, | are allowed.
- ch 1 [low] Section 3, independence condition: The independence condition is stated in one direction only: 'no iteration reads what another writes'. The other direction matters too, where one iteration writes a location another iteration reads, and two iterations writing the same location must also be excluded. As written a student can pass a loop that is still order-dependent.
- ch 2 [high] Beyond: The MPI version history is wrong: one-sided communication was added in MPI-2, not MPI-3, and non-blocking collectives were added in MPI-3, not in 'newer versions'. The same error appears in the 'Search next' line.
- ch 2 [low] Section 3: The sentence 'All ranks must pass the same count, datatype, operation and root' implies every collective has an operation and root. MPI_Bcast has no operation; MPI_Scatter and MPI_Gather have no operation; root applies only to rooted collectives.
- ch 2 [low] Worked example 1, dry run: The rank 1 row shows 36 under 'Final total at rank 0'. A student may read this as rank 1 also holding the final total. After MPI_Reduce only rank 0's total is valid; rank 1's total is not set by the reduction.
- ch 3 [high] Section 2, host/device paragraph: The launch syntax has lost its angle brackets and the launch configuration: the text prints "the host calls it with launch syntax kernel>>(args)" and then "add>>(A,B,C)" with no block/thread numbers shown, though the next sentence refers to "the first number" and "the second". As printed, a student cannot see the correct call form and the example call is not valid CUDA.
- ch 3 [high] Section 2, guard sentence: The guard condition has lost its comparison and is unreadable: "A guard if (tid  protects a partly filled last block." The condition and closing parenthesis are missing, so the sentence that explains why a partly filled last block is safe makes no sense.
- ch 4 [high] Section 1, launch syntax and 2-block example: The CUDA launch is written as kernel>>(arguments), and the 2-block/4-thread launch is written as add>>(dA, dB, dC). The triple angle brackets and launch configuration are missing, so the syntax is wrong and the example cannot be compiled.
- ch 4 [high] Quiz Q6: The question compares two launches shown only as >> and >>. The launch configurations are missing, so the question is unreadable and the answer cannot be checked against the displayed code.
- ch 4 [low] Exam traps, swapped gridDim/blockDim trap: The trap says the index becomes wrong for every block after 0. With a swapped formula it is also wrong inside block 0 for every thread except thread 0.
- ch 5 [high] Beyond: It says distributed shared memory is exposed 'across blocks on different chips'. On NVIDIA hardware, distributed shared memory works only between blocks of the same thread block cluster, and a cluster is co-scheduled inside one GPU (one GPC). No mechanism lets a block read another chip's shared memory directly.
- ch 5 [low] Worked example 1: The listed code is ordinary host C (int s[4] in main), but the steps say 'Declare __shared__ int s[4]' and call __syncthreads(). A student may think the listing is CUDA code, and may think __shared__ can be declared inside a host function.
- ch 6 [low] Section 2, pinned memory paragraph: "The driver may copy through a hidden staging buffer, so cudaMemcpyAsync cannot safely overlap it" is vague and the word "safely" is misleading. The real rule is that a copy from pageable host memory is not truly asynchronous: the driver must stage it through a temporary pinned buffer (and may synchronise the stream first), so the call gives no overlap.
- ch 6 [low] Section 3, tiling paragraph: "each element is used blockDim times from shared memory" is imprecise: blockDim is a dim3 (three components), and the reuse count equals the tile width, which in the usual square-tile kernel is blockDim.x (or blockDim.y), not "blockDim".
- ch 6 [low] Quiz Q4: The 32 addresses 0, 2, 4, ..., 62 (in floats) cover bytes 0 to 251, a span of 252 bytes, not 256 bytes. The answer's efficiency figure is right, but the stated span is a wrong number a student may copy.
- ch 6 [low] Section 3, arithmetic intensity: The chapter extends the standard definition of B (bytes between global memory and the processor) to include host-device copies. That is a defensible measure of the whole pipeline, but it differs from the textbook roofline arithmetic intensity, which is introduced later in "Beyond"; a student may wonder why the same kernel has two different intensities.
- ch 7 [low] Section 1 and Exam traps, third trap: The rule is stated as a hard OpenCL rule: 'global size must be a multiple of local size' and 'local size must divide global size'. That is true for OpenCL 1.x, but OpenCL 2.0 and later allow non-uniform work-groups, where the last group may be smaller (if the device supports it). A student may quote the absolute rule and lose marks on a modern-OpenCL question.
- ch 7 [low] Worked example 1, dry run table: The table lists only two of the eight work-items (group 1, local ids 2 and 3). A student reading a 'dry run' expects every work-item, and it is not clear why group 0 and local ids 0 and 1 are missing.
