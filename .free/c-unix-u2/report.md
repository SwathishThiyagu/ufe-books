# c-unix-u2: free-model run

- Book: `work/claude_figs/c-unix-u2/tree/books/cse/c-unix/c-unix-u2.html`
- Status: ok
- Model calls so far: 23 (87,860 tokens in, 166,391 out), 8.0 minutes

## Checker

```
c-unix-u2.html: 5 chapters, 10756 words, 6 figures, 126 KB
OK
```

## For the reviewer

- chapter 1: the figure cannot be drawn: note "commands" runs off the right edge; shorten it
- chapter 1: worked example 1: the worked example states [5.0] but recomputing it gives [2148.0, 1.0, 2.0, 1.0, 1.0, 9.0, 4.0, 1.0]; fix the steps and the answer so they match the correct values

## Reviewer notes (after any revision)

- ch 1 [high] worked example 1, step 10 and final answer: The path /home/ravi/lab/notes.txt has four name components (home, ravi, lab, notes.txt), not five. The step and the answer both say five, so the count a student copies is wrong.
- ch 1 [high] quiz Q6: The target string /etc/app.conf is 13 bytes ('/' plus 'etc' plus '/' plus 'app.conf' = 1+3+1+8 = 13), not 12. The size field 12 in the listing and the answer '12 is the length in bytes of the target string' are both wrong.
- ch 1 [high] worked example 1, part (d), step 9 step 10 and answer: The listing shown is of /home/ravi and contains notes.txt there. The link latest lives in lab and its relative target notes.txt resolves to /home/ravi/lab/notes.txt, which the listing never shows. So the answer cannot state that the final file 'is a regular file'; as drawn the link dangles.
- ch 1 [low] section 2, last paragraph: PATH_MAX is 4096 including the terminating null byte, so the longest usable path name is 4095 bytes, not 4096. The cap also applies to a path name passed to a system call, not to how deep the tree may be.
- ch 1 [low] section 1, bullet list of top-level directories: The list is presented as the fixed top level but leaves out directories students will meet at once, such as /sbin, /mnt, /opt and /srv (and /media, which the paragraph above already uses).
- ch 1 [low] section 3, step 3 of the worked example (link count of lab): The reasoning runs backwards: the listing does not show the contents of lab, so 'lab has no subdirectories' is not known from the listing. The link count is the evidence, not the conclusion.
- ch 1 [low] Beyond: systemctl is given as a tool that reads /proc and /sys directly. It mainly talks to systemd (PID 1) over D-Bus, so it is a poor example here and can mislead a student.
- ch 2 [high] Section 3, paragraph starting 'less does not load the whole file': The sentence 'most Linux systems use less even when you type more' is backwards for mainstream distributions. On Debian, Ubuntu, Fedora and similar systems, 'more' is a separate, simpler program (from util-linux), not a link to less. A student who checks this on their college machine will find a plain 'more' and be confused.
- ch 2 [low] Section 1, sentence '-a includes hidden names, and also . and ...': The text reads as three dots. A student cannot tell whether you mean the entries '.' and '..' or something else.
- ch 2 [low] Worked example 1, step 1 and answer: Counting one extra 'total' line is correct for GNU ls, but some ls versions (for example BusyBox ls on embedded boards) print no total line. Stating 7 unconditionally can look wrong to a student who tries it on such a machine.
- ch 2 [low] Lead and Worked example 1(e): The lead says '5 MB log' while the example file is 5,242,880 bytes, which is 5 MiB. Mixing MB and MiB in the same chapter weakens the point about -h using powers of 1024.
- ch 3 [low] Worked example 1, solution steps 1–4: The solution's step numbers are offset by one from the question's steps: 'step 1' describes the state before step 1, 'step 3' describes what step 2 (ln -s) did, and 'step 4' describes step 3 (rm). A student matching steps between question and answer can easily miscount the link count.
- ch 3 [low] Section 3, description of find tests: '-perm 644 matches permission bits' is loose. Plain -perm 644 matches only files whose mode is exactly 644. Files with extra bits such as 1644 or 664 are not matched; for 'at least these bits' find needs -perm -644.
- ch 3 [low] Section 3, description of -size +1M: '-size +1M is larger than 1 MB' hides the unit and the rounding rule. In find, M means 1 MiB = 1,048,576 bytes, not 1 MB = 1,000,000 bytes, and find rounds each file size up to whole MiB before comparing, so a file of exactly 1 MiB is not matched by +1M.
- ch 3 [low] Section 2, cp -r line: 'cp -r dir1 dir2 copies a directory tree' is true but hides the case that trips students in exams: the result depends on whether dir2 already exists.
- ch 3 [low] Section 2, first cp sentence: 'cp notes.txt backup.txt reads the source inode and writes a new inode' is imprecise: cp reads the file's data through the source inode and creates a new file with its own inode. Saying it 'reads the inode' suggests it copies metadata from the inode, which plain cp does not do.
- ch 4 [high] Figure caption: The caption says the numbers under the three triads add to 7, 5 and 0. The other triad is r--, which is 4+0+0 = 4, not 0. The array itself shows 4, 0, 0 and the aria text says 754, so the caption contradicts the figure it describes.
- ch 4 [high] Exam traps, trap 3: "A directory with 644 is broken for everyone but the owner" is wrong. In 644 the owner digit is 6 (rw-), so the owner has no x either and cannot enter the directory or create files in it. Only listing names works for the owner. The sentence as written teaches the opposite.
- ch 4 [low] Section 4, Sticky bit: It says the last slot shows t, but does not mention the upper-case T that appears when the sticky bit is set and x is off on that slot, even though the matching case S is explained for SUID.
- ch 5 [high] figure 'Which bits decide': The flowchart disagrees with the text in Section 3. The 'yes' branch of 'effective uid is 0?' leads to 'owner bits apply', but root is not decided by the owner triplet; root skips the triplet check for read and write. The chart also has no node for 'effective uid equals the file's uid?', so a reader who owns a file but is not in the file's group is routed from 'in the file's group?' straight to 'other bits apply', which is wrong. Step 2 of the list in Section 3 is missing from the diagram.
- ch 5 [low] worked example 1, parts (c) and step 5: The example gives chgrp arjun /home/ravi/project/report.txt without saying who runs it. The file's owner is ravi, and Section 2 correctly states that an owner may change the group only to a group the owner belongs to. Ravi is not in arjun, so ravi would get 'Operation not permitted'. Only root can make this change.
- ch 5 [low] Section 1, users are numbers: 'No other account has uid 0' is stated as a kernel fact. It is only an administrative convention: a second account created with uid 0 is also the superuser, because the kernel checks the number, not the name.
- ch 5 [low] worked example 1, step 7 and the ACL paragraph in Section 3: Adding an ACL entry also sets the ACL mask, which overrides the group permission bits shown in ls -l. Here the mask comes out as r--, so the students do keep read, but the general sentence 'the owner and group stay unchanged, so students keep their access' hides this and will trip students on a file where the mask is smaller than the group bits.
