# c-dist-u6: free-model run

- Book: `work/claude_figs/c-dist-u6/tree/books/cse/c-dist/c-dist-u6.html`
- Status: ok
- Model calls so far: 25 (92,844 tokens in, 215,445 out), 14.8 minutes

## Checker

```
c-dist-u6.html: 8 chapters, 14584 words, 9 figures, 161 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Worked example 1, step 2 and answer: Step 2 says the mount-point handle is used 'if absent' as one RPC to S. That hedged case would make the first open cost 2 round trips to S, but the answer states 1. A student cannot tell which case the count assumes.
- ch 1 [low] Section 1, definitions of name and identifier: Only half of the standard definition of an identifier is given. The usual definition has two conditions: at most one entity per identifier, and at most one identifier per entity.
- ch 1 [low] Section 2, NFS v3 sentence: Saying the NFS v3 server keeps no per-client open or lock state is too strong for locking: file locking in NFS v3 is handled by a separate lock manager protocol that does keep per-client state. Only the core NFS protocol is stateless.
- ch 2 [low] Section 2: The text says the cost is 'a sum of three parts', but the formula C = c_cpu × cpu_ops + c_io × pages + c_msg × messages + c_byte × bytes has four weighted terms. A student counting the constants will think the formula is wrong.
- ch 2 [low] Section 2: 'Disk and CPU costs are fixed by local hardware, so they are paid once per site' reads as if CPU and disk are paid a single time no matter how many operations run. They are paid per operation; the real point is that they are not repeated on every network hop.
- ch 2 [low] Section 4, adaptive plans: The text says that when the first result arrives 'much smaller than estimated, the next join switches to a semi-join'. The quiz answer Q6 gives a different and more usual response (nested-loop or broadcast). A small intermediate result is normally broadcast or used as the build side, not turned into a semi-join. The two places contradict each other.
- ch 2 [low] Section 3, Bloom join bullet: 'a few false positives slip through and are joined again after the transfer' is unclear: the false positives are tuples of R that travel to B and are then dropped by the final join, they are not joined a second time.
- ch 2 [low] Lead: 'Every distributed database, and every warehouse built on MapReduce or Spark, works this way' overstates the case. Many warehouse engines run without fragment-level cost-based planning, and not every plan is chosen by a byte-cost search.
- ch 2 [low] Section 4, last paragraph: The chapter points to '6.6' as plain text while the book format expects a cross-reference link, so the note cannot be tapped on a phone.
- ch 3 [high] Section 1: It says a parent in a nested transaction may commit only if all children commit. In standard nested transactions, a child can abort without forcing the parent to abort; the parent must wait for all children to finish, but it can still commit after handling a child abort, with that child's effects rolled back.
- ch 3 [high] Section 1: It conflates a private workspace with an undo log: 'It writes new values there, not to the database.' With undo logging, the participant writes new values to the database and stores old values in the undo log; the changes are kept hidden by locks, not by being absent from the database.
- ch 3 [high] Section 2 and Worked example 1 step 3: It states the log write must happen before any decision message and forces ABORT before sending abort. In 2PC only a COMMIT decision must be forced before the commit message; an abort need not be logged first, because presumed abort makes a missing commit record mean abort.
- ch 3 [high] Section 2 and Quiz Q5: Presumed abort is described as 'if a site finds no commit record, it treats the transaction as aborted.' A participant that voted yes and has a prepare record must not abort just because it has no local commit record; it must wait or query. Presumed abort is a coordinator/recovery rule, not a rule for any prepared participant.
- ch 3 [low] Lead: 3PC is said to add pre-commit 'to reduce waiting'. Its purpose is to avoid blocking or indefinite waiting under some failures, not to reduce waiting generally; it adds a phase and more messages, so latency can increase.
- ch 3 [low] Section 3: Strict 2PL is defined as holding locks until commit. Strict 2PL holds locks until commit or abort.
- ch 4 [low] Section 3, deployment models (hybrid): The definition 'two or more models are joined so data and applications can move between them' is loose enough that a student can label two public clouds from different providers as hybrid. Textbooks keep hybrid as a private or community cloud bound to a public cloud, and usually give the several-public-clouds case its own name, multi-cloud.
- ch 4 [low] Figure description (the sentence above the figure spec): 'The lower layer leaves the operating system and runtime to you' is ambiguous in a three-layer stack; a reader cannot tell whether 'lower layer' means PaaS or IaaS.
- ch 5 [low] Section 1: The opening sentence says the hypervisor 'owns the real hardware'. That holds for type 1, but a type 2 hypervisor runs as a process on the host OS and reaches the hardware only through the host OS, so a student may take away a definition that the chapter itself later contradicts.
- ch 5 [low] Section 2: The Intel and AMD terms are mixed. VT-x uses root and non-root operation; AMD-V uses host and guest mode. The sentence names both vendors but gives only the Intel names.
- ch 5 [low] Section 3 and Worked example 1: The rule is stated as stopping when the dirty set is 'at or below a threshold', but the example says 'below 64 MB' and ends at 41.94 MB. A student cannot tell whether a dirty set exactly equal to 64 MB ends the pre-copy phase.
- ch 5 [low] Worked example 1: The 67.99 s total is the sum of the six transfer times only. The text defines downtime as 'the last copy plus setup', but no per-round setup time, no final resume time and no transfer of VM state at the target is counted, so the label 'total time' is broader than what was computed.
- ch 5 [low] Beyond: Kata Containers is a container runtime that uses lightweight VMs, not a VM monitor like Firecracker. Grouping both as 'lightweight VM monitors' is imprecise.
- ch 5 [low] Beyond: 'Kubernetes moved live migration into scheduler and operator discussions' is vague and can read as if the core Kubernetes scheduler itself live-migrates VMs.
- ch 6 [low] Figure caption (Section 3): The caption says the 20% serial curve "flattens at 400 req/s" at 16 servers, but section 1 states the ceiling for s=0.2 is 1/s = 5×, i.e. 500 req/s. The curve only reaches 400 at 16 servers and is still rising towards 500, so the caption can make a student think 400 is the asymptote.
- ch 7 [low] Section 1, table row Ownership: The grid cell says "Many owners, one VO". This contradicts the lead, where a VO is tied to one project. A single grid usually serves several VOs at the same time, so "one VO" reads as if a grid can have only one.
- ch 7 [low] Section 1, first paragraph and Quiz Q1: The VO is defined only as the set of users allowed to share. Standard definitions include the resource providers and the sharing rules, not just users. A student may answer Q1 with users alone and lose marks.
- ch 7 [low] Section 2, collective layer: "Brokers, allocation and directories" puts plain allocation in the collective layer. Allocating one site's own resource is a resource-layer job; the collective layer does co-allocation and brokering across several sites. As written, the two layers overlap and the student cannot tell them apart.
- ch 7 [low] Worked example 1: The schedule silently assumes that all three sites are free from the same instant and that the job can run on all 160 CPUs at once. Real grids queue jobs at each site, so the 6.67-hour answer is only valid under these assumptions, which are never stated.
- ch 8 [low] Section 1 and Exam traps: Only GET and PUT are named as idempotent, while DELETE is defined in the same paragraph and is also idempotent. A student can conclude that DELETE is not idempotent and lose marks on a method-semantics question.
- ch 8 [low] Worked example 1, steps 4-6: On a miss the 300 KB body crosses two links, origin to edge and edge to browser, but the transfer time of 150 ms is counted only once. The arithmetic is right only if the edge streams the body to the client while receiving it.
- ch 8 [low] Section 2, sentence 'The hit ratio decides cost': Overstated. Cost is decided by bytes served from the origin, which the request hit ratio does not fix; the chapter's own trap says a small hot object raises the request hit ratio without saving much bandwidth.
