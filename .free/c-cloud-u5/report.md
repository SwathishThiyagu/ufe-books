# c-cloud-u5: free-model run

- Book: `books/cse/c-cloud/c-cloud-u5.html`
- Status: ok
- Model calls so far: 33 (116,785 tokens in, 253,625 out), 5.0 minutes

## Checker

```
c-cloud-u5.html: 9 chapters, 16335 words, 10 figures, 179 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Lead paragraph (also the figure aria text): The lead names only three models (threads, message passing, data parallel) and says 'The same three models', but Section 2 is titled 'Four families of parallel models' and adds master-worker. A student cannot tell whether the count is three or four.
- ch 1 [low] Section 3, sentence on coordination as the second ceiling: It says thread creation, locks and the final merge 'all sit outside the parallel part'. Locks do not sit outside: a lock is taken and released inside the parallel phase and serialises part of it, which is exactly why lock contention lowers speedup.
- ch 1 [low] Worked example 1, code block: The code claims to show the split of 8,000,000 numbers, but each thread computes part[i] = (lo + hi) * chunk // 2, a closed-form sum, so it never adds 2,000,000 numbers. The stated 40 ms per thread comes from adding numbers, so the code's cost does not match the cost model, and the input is silently assumed to be the integers 1 to 8,000,000.
- ch 2 [high] Quiz Q5: The answer contradicts the chapter's own arithmetic. With 24 workers each task takes 4 + 0.5 = 4.5 min per worker, so 600 tasks means 25 tasks per worker = 112.5 min, which is roughly half of 225 min. The workers would draw tasks at only 24 ÷ 4.5 ≈ 5.3 tasks/min, far below the master's 40 tasks/min. Dispatching all 600 tasks takes just 15 min, so the master is not a bottleneck and the makespan really would halve. The stated answer is false for the numbers given.
- ch 2 [high] Exam traps, third bullet: 'Adding workers can hurt: when o is large compared with t, the pool spends its time shuffling tasks, and throughput per worker saturates at 1 ÷ (t + o)' is wrong as written. Overhead o is paid by each worker on its own task, so per-worker throughput is always 1 ÷ (t + o) and total throughput W ÷ (t + o) grows with W; the formula T = N × (t + o) ÷ W never gets worse with more workers. A student will conclude that overhead causes harm from extra workers, which the model does not show.
- ch 2 [low] Section 2, last sentence: 'The queue is kept short so that one slow task does not leave the other workers idle' is unclear. A short master queue does not by itself protect against a slow task; what helps is keeping each task small and not handing a worker a long batch of tasks in advance.
- ch 2 [low] Section 1, makespan formula: T = N × (t + o) ÷ W silently assumes N divides evenly by W. With 601 tasks on 12 workers the last worker gets one extra task and the real makespan is one task longer.
- ch 3 [high] Worked example 1, dry-run table: The 'Shuffle group' column is wrong for the rows before the last one. Row for line 1 shows 'cat [2,1], dog [1]', but at that point only line 1 has been combined, so cat should hold a single value 2; the 1 from line 3 does not exist yet. The row for line 3 shows 'cat [2,1]' and drops dog, so the column is inconsistent and a student will think shuffle happens line by line.
- ch 3 [low] Section 1, last line: 'Only reduce output is final' is too absolute. A job with zero reducers writes the map output straight out as the job's final output, which is common for map-only jobs.
- ch 3 [low] Section 3, last paragraph: 'see Chapter 5.4' is written as plain text, so it is not a working cross-reference inside the book.
- ch 4 [high] Section 1, first paragraph: "Every operation creates a new RDD" is false. Transformations create new RDDs, but actions such as collect() and count() return values or write output; they do not create RDDs. A student may think actions also produce RDDs.
- ch 4 [high] Section 2, MapReduce paragraph: MapReduce does not write intermediate data to disk "between jobs" as the key comparison. It writes map output (intermediate data) to local disk before the reduce phase within a job.
- ch 4 [low] Section 1, persistence paragraph; Exam traps, third bullet: The claim that cache() and persist() use executor memory, and that data that does not fit is evicted and recomputed, is only true for memory-only storage. persist() can use disk; MEMORY_AND_DISK spills to disk, and DISK_ONLY does not use memory.
- ch 4 [low] Worked example 1, dry run, collect row: The dry-run collect output is missing the closing square bracket: '[(a,2), (b,2), (c,1)'.
- ch 5 [low] Section 1, launch steps: The SSH line is truncated: 'ssh -i key.pem ec2-user@' has no host after the @, so a student who copies it gets an error, and the login name differs by AMI (ec2-user for Amazon Linux, ubuntu for Ubuntu images).
- ch 5 [low] Section 2 vs Exam traps: Section 2 says of an EBS volume 'The volume outlives the instance', but the Exam traps correctly say a terminated instance deletes its root volume by default. Read together the two statements contradict each other.
- ch 5 [low] Figure and worked example 1: The figure has no load balancer, yet the caption, Section 3 and step 3 of the worked example all place an Application Load Balancer in the public subnet in front of the web instances. The reader cannot match the diagram to the design.
- ch 5 [low] Section 2 and Exam traps, 'no seek': 'There is no seek' is imprecise. S3 does serve byte-range GET requests (partial reads) over HTTPS; what it does not support is in-place or partial writes to an existing object.
- ch 5 [low] Lead: The unsupported claim that 'Most Indian startups, banks and government portals run at least part of their stack this way' invites an examiner question and cannot be backed by the chapter.
- ch 6 [low] Section 1, the formula and its term list: The term list defines 60 as the CPU-seconds per minute one instance supplies at 100% utilization, with no vCPU assumption stated. This is true only for a one-vCPU instance. Earlier in the same chapter an e2-small machine is described as having 2 vCPUs, so a student may plug 60 into a two-vCPU case and get half the correct instance count.
- ch 6 [low] Section 1, Standard bullet, and Exam traps, first bullet: The chapter says standard App Engine 'cannot write to local disk' and repeats 'no local disk writes' in the traps. Standard instances do have a small writable /tmp area; what they lack is persistent local storage. As written, a student will say the filesystem is entirely read-only, which is the wrong mechanism.
- ch 6 [low] Quiz Q2: The question asks for 'the five fields every VPC firewall rule carries', but every rule also carries a priority (default 1000), which decides which rule wins when two rules match the same traffic. The listed five are the matching fields only, so the answer understates the rule's full set of fields.
- ch 7 [high] Lead: It says a virtual network connects "the virtual machines, databases and storage inside it". A storage account (Blob) does not sit inside a VNet; it is reached through a public endpoint, or through a private endpoint/service endpoint when you deliberately configure one. A student will draw blob storage as a VNet resource.
- ch 7 [high] Worked example 1, step 1: The count of 8 is wrong. It counts the resource group itself, which is not a resource inside the group, and it leaves out the NSG described in the same sentence and the storage account that holds the blob container. A student copying this will miss those resources in the exam.
- ch 7 [low] Section 3, Azure Storage: "Three shapes" and "Tiers are hot, cool and archive" are incomplete. A storage account also offers Queue and Table services, and Azure has a cold access tier between cool and archive.
- ch 7 [low] Quiz Q5: The answer says a compromised web VM "still has limited reach", which is unclear: a compromised web VM can of course still open 1433 to the database.
- ch 7 [low] Worked example 1, step 6: Step 6 is not a computation; it just restates the given 100 GB. It pads the six-step method without adding anything.
- ch 8 [low] Section 1, formulas: The VMs formula gives base capacity with no CPU-overcommit term, yet the worked example and quiz then use a 2:1 overcommit ratio. A student may not see how to plug the ratio into the formula given in the text.
- ch 8 [low] Lead and Section 3: The lead names only Eucalyptus, OpenStack and OpenNebula, and the chapter title lists the same three, but Section 3 and the comparison table add Apache CloudStack with no warning. The reader meets a fourth platform suddenly.
- ch 8 [low] Section 2 and lead: Eucalyptus is presented as a live choice alongside OpenStack and OpenNebula, but its open-source releases stopped after the company was acquired and it is rarely deployed in new projects today. The lead's claim that campuses and companies 'use these platforms' overstates its present use.
- ch 9 [high] Section 2, output table: The table mislabels one column and drops two that CloudSim actually prints. In the standard output of the shipped examples the header is: Cloudlet ID, STATUS, DataCenter ID, VM ID, Time, Start Time, Finish Time. The 'Time' column is the cloudlet's actual CPU time (finish time minus start time), not its finish time, so a student reading the table will take a duration for an absolute time. The table also has no 'Finish Time' column, which contradicts the sentence just above it saying 'the two you need are start and finish'.
- ch 9 [low] Section 2, run commands: The demo command puts only the core jar on the classpath (java -cp cloudsim.jar:. org.cloudbus.cloudsim.examples.CloudSimExample1). The example classes are not inside the core CloudSim jar in the released download, so the command fails with a 'class not found' error unless the example code is also on the classpath.
