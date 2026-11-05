# c-cloud-u3: free-model run

- Book: `books/cse/c-cloud/c-cloud-u3.html`
- Status: ok
- Model calls so far: 30 (103,752 tokens in, 191,031 out), 5.1 minutes

## Checker

```
c-cloud-u3.html: 9 chapters, 16827 words, 10 figures, 169 KB
OK
```

## For the reviewer

- chapter 2: the figure cannot be drawn: note "modified guest" runs off the right edge; shorten it
- chapter 2: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [high] Quiz Q5 answer: The failure condition is wrong. With 24 vCPU configured on 8 physical cores, contention does not start when combined demand approaches 24 cores; the host only has 8 cores of real capacity, so queues build once the VMs' combined busy vCPU demand approaches 8 cores. Saying it fails only near 24 cores would make overcommit look far safer than it is.
- ch 1 [low] Worked example 1, step 3: Cores and vCPU are mixed in one subtraction (16 cores - 10 vCPU), which reads as if the two units were interchangeable, the very confusion the exam traps warn against.
- ch 1 [low] Lead and Section 1: The text states flatly that the hypervisor sits on the hardware and owns the real hardware. That is true only for bare-metal (Type 1) hypervisors; a hosted (Type 2) hypervisor runs as a program on top of an ordinary host OS.
- ch 1 [low] Section 3, Pros, Consolidation bullet: Ten old servers each at 10% CPU add up to about one full server of CPU demand. If the new host is the size of one old server, the example leaves no headroom and contradicts the claim of a comfortable consolidation. It works only if the receiving host is larger than any single old server.
- ch 1 [low] Section 2, Encapsulation: The sentence 'Everything about the VM travels in those files' clashes with the live-migration answer in Q3, where the running memory state is copied over the network, not carried in the VM's files.
- ch 2 [high] Section 3, 'Reading a system by its level': The decision procedure gives a wrong answer for the two lower levels. Its second question is 'Ask whether processes share the host kernel. If yes, the level is OS-level.' Every ordinary process on Linux shares the host kernel, so a plain JVM (application-level) and a WINE program (library-level) both match this test and get labelled OS-level, contradicting Section 2 and quiz Q2/Q3. The 'first match' rule therefore only works for hardware-level.
- ch 2 [low] Figure (tree spec): The root node is at _x = 326, but its children span x = 88 to x = 632, whose centre is 360. The root box will sit visibly left of the tree's centre and the Hardware node at x = 564 leaves an uneven gap after OS-level at x = 360.
- ch 3 [low] Section 2, first paragraph: Saying Dom0 'runs a driver VM that talks to real devices' suggests the driver domain is a separate VM launched by Dom0. In Xen the driver domain is normally Dom0 itself; the wording will confuse students about what the control domain is.
- ch 4 [low] Worked example 1, problem statement: The stated workload rate is impossible with the stated costs. 1,000,000 operations per second at 2 μs each needs 2 seconds of hypervisor time in every second of real time, so a student who multiplies will get an answer above 100% CPU. The rate is also never used, since the example then asks about 1,000 operations.
- ch 4 [low] Section 1, definition of sensitive instruction: The definition covers only one half of the standard meaning. A sensitive instruction is one that either depends on machine state or changes machine state/configuration. As written, instructions whose effect alters the machine (halting the CPU, writing the page-table base register) fit only loosely, even though the chapter's own examples are of that kind.
- ch 4 [low] Section 3, table row 'Runs any OS image': 'Yes' is too broad: full virtualization runs any unmodified image built for the same CPU architecture, not literally any OS image (x86 will not boot an ARM kernel).
- ch 5 [high] Worked example 1, step 5: The decimal value given for the guest physical address is wrong. 0x142F0 = 1×65536 + 4×4096 + 2×256 + 15×16 = 65536 + 16384 + 512 + 240 = 82672, not 82704. The other two decimals (21232 for 0x52F0 and 328432 for 0x502F0) are correct, so a student checking the arithmetic will be confused about which figure is wrong.
- ch 5 [low] Section 2, EPT/NPT paragraph: VPID is an identifier for a virtual processor (a vCPU), not for a VM, so calling it a 'VM identifier' is loose. Also 'a miss costs two walks' hides that each walk is itself multi-level: with 4-level tables the hardware does up to 4 guest steps and up to 4 EPT steps per miss.
- ch 6 [low] Section 2, VLAN paragraph: "VLAN adds a 12-bit tag" is loose: the 802.1Q tag is 4 bytes, and only the VLAN ID inside it is 12 bits. A student may write 'the tag is 12 bits' in an exam.
- ch 6 [low] Section 1, RAID paragraph: "A hot spare lowers usable capacity" is true but does not say by how much, so it cannot be used in the (n − 1) × d formula that follows.
- ch 6 [low] Section 3, live migration sentence: "the VM's disk and MAC address move with it" can mislead: with a shared storage pool the disk file does not move at all; only the VM's memory state, MAC and port attachment move.
- ch 7 [high] Worked example 1, steps 4–7 (and quiz Q6): The example counts a 500 MB application layer for each of the 10 copies, but the same section says image layers are read-only and shared and that ten containers from one image share layers instead of copying them. Ten copies of the same application would share the 500 MB app layer too, giving 0.1 + 0.5 = 0.6 GB, not 5.1 GB. As written, a student learns that only the base is shared and that app layers are always copied per container, which is wrong.
- ch 7 [low] Section 1 and the figure: Section 1 defines the hypervisor as the layer that owns the physical CPU, memory and devices (a Type 1 hypervisor). The figure puts the hypervisor above a host OS, which is a Type 2 layout where the hypervisor reaches hardware through the host OS and does not own the devices directly.
- ch 7 [low] Section 3 table: The first column heading is 'Question', but the rows are attributes (Guest OS, Start, Image, Isolation, Best for), not questions. The Guest OS row also does not answer its own question for containers: 'shared host kernel' is the reason, not the value.
- ch 7 [low] Section 1 formula: The formula VM image = guest OS + app + data puts stored application data inside the image. In practice application data sits on separate volumes or disks and is not part of the image, and the worked example never counts any data.
- ch 7 [low] Section 2 (copy-on-write) and quiz Q7 answer: 'Only the changed blocks' is imprecise. With overlay filesystems, the common Docker storage driver, a modified file is copied whole on first write (file granularity); only block-level drivers copy individual blocks.
- ch 8 [low] Section 2, isolation paragraph: vCPU is used earlier in Section 2 and throughout the example and quiz, but never defined; a first-time reader may not know it is a share of a physical core.
- ch 8 [low] Section 2, build-a-VDC paragraph: LUN, NFS export, VLAN and overlay network are used as if already known; LUN in particular is jargon for block storage volumes.
- ch 8 [low] Exam traps, fifth trap: 'compares the request against committed capacity minus reservations' is ambiguous and can be misread as subtracting reservations from the request.
- ch 9 [low] Section 1, Device path in Xen: The device path is stated as a general rule for all Xen guests, but the shared-ring path applies only to a PV guest, or to an HVM guest that has PV drivers installed. A pure HVM guest without PV drivers reaches devices through QEMU emulation in Dom0 and does not use the ring path. The earlier paragraph says this, but the device-path paragraph contradicts it by omission.
- ch 9 [low] Section 2 / Figure caption: The caption says 'ESXi keeps management inside the VMkernel', but Section 2 says ESXi has no general-purpose service console and that management comes from outside (vSphere Client, vCenter, API). A student cannot tell which is meant.
- ch 9 [low] Quiz Q6 answer: The answer pairs the Dom0 backend driver with the parent VSP but does not name the Xen frontend driver, so the child-side analogy (VSC) is missing and the comparison is one-sided.
