# Lesson slop found in the AI lessons (17 Nov 2026), to fix later with rules and fix threads

Checked all 22 c-ai lessons (every scene, narration and frame). Facts, numbers and layout were clean. Found:

1. Non-existent site: c-ai-u5-L4 and c-ai-u6-L4 outros say "Find this unit in your own syllabus on the University free n easy
   site"; u6-L4 also shows "Find your syllabus on the site". Rule: no site or finder line until the site is live.
2. "Chapters x to y of your book" on the title page (agenda `star`) in u3-L1, u3-L3, u5-L4, u6-L2, u6-L3, u6-L4.
   Rule: always "of your free notes"; never "book".
3. Stock recap icons with no meaning: u1-L4 (recycle for Search, shield for Toy problems), u3-L2 (shield for Alpha-Beta,
   timer, up arrow). Rule: recap pictures drawn from the lesson's own content (tree, board, table), no stock icons.
4. Tiny or faint recap pictures: u2-L2 (all three), u6-L4 (Clustering; MYCIN card is an empty dashed "engine" box).
5. Caret maths on screen: "O(b^(d/2))", "b^(m/2)" in u2-L2 (4 places) and u3-L2. Rule: real superscripts.
6. Spoken Bloom levels: "Question two, at the apply level" (9 lines in u1-L2, u2-L1, u3-L1, u4-L3). Rule: no Bloom words in narration.
7. Unit numbers spoken or shown ("Next time, Unit two", "use probability (Unit 5)"). Rule: name the topic, not the unit number.

Published videos stay as they are (no re-upload). The two "site" videos get a description line until the site is live.
Fixed already: the recycle icon's arrowhead (engine, data pack v44).

## Data Structures (audited 17 Nov 2026, 25 lessons, every scene, frame, worked example, model answer and trap)

Facts: clean. About 120 worked numbers and model answers recomputed (addresses, recurrences, Big-O constants, heaps,
AVL and red-black steps, B-tree splits, BFS/DFS, Kahn, Kruskal/Prim, Dijkstra, Floyd-Warshall rounds, sort passes,
Shell shifts, radix passes, hashing and probe counts, KMP lps and comparisons, Boyer-Moore shifts, trie nodes): no error.
All 52 exam traps checked: every "Don't write" is wrong and every "Write" is right. No checker errors on any sheet.

lesson | scene | what's wrong | severity
--- | --- | --- | ---
c-ds-u6-L5 | outro (24) | says and shows "Find this unit in your own syllabus on the University free n easy site" and "Every Data Structures unit book and lesson on the University free n easy site" (no such site; unit books not offered) | misleading: should fix
c-ds-u6-L5 | bookfig (5) | spoken "Your book's figure" | should fix
c-ds-u1-L4, u4-L3, u4-L5, u5-L1, u5-L2, u5-L4, u6-L1, u6-L5 | agenda (1) | "Chapters x to y of your book" (must be "of your free notes") | should fix
c-ds-u1-L4, u2-L4, u3-L3, u4-L5, u5-L4 | outro | "Next time, Unit two/three/…" spoken; "NEXT UNIT, Unit N" card | should fix
c-ds-u1-L1 | pa (20) | model answer says "balanced trees come in unit four" / "(hence AVL trees, Unit 4)" | should fix
c-ds-u2-L3, u4-L2 | pq (17, 19 / 15, 17) | "Question two, at the apply level", "at the analyze level" spoken | should fix
c-ds-u1-L3 | recap | stock icons: up arrow (Notations), stopwatch (Cases), green tick (Linear search) | cosmetic
c-ds-u4-L5 | recap | plain "4 KB" box and up arrow | cosmetic
c-ds-u6-L3 | notebook (4) | "Θ(n^1.5)" typed with a caret | cosmetic

Not slop (checked): "booking site" (u4-L5 hook) and "train site" (u5-L4 hook) are story words.
Same patterns as the AI lessons, so the rules proposed above (no site line, "free notes" never "book", topic not unit
number, no Bloom words, real superscripts, recap pictures from the lesson) would have caught all of them.

## Linux and Shell Programming (17 Nov)

Audited 17 Nov 2026: all 16 c-unix lessons, every scene, narration and frame (sheets at 0.92 and re-rendered at 0.995; the
cut-off lines at 0.92 were typing animations and render whole at 0.995). Checker: 0 page errors, 0 cue failures, 0 text
outside the safe area on every sheet. About 60 worked numbers and model answers recomputed (dates, install/clone minutes,
licence saving, syscall counts, ls -lah sizes, chmod/umask, link counts, count.sh, the cut|grep|sort|head and grep|sed|awk
pipelines, return 300 = 44, /24 hosts, ping loss, 120 MB in bytes, cron cut-off, PID hash buckets, jiffies wrap, 32-bit page
translation, pipe fill, ext2 limits and byte 300000, dev_t, CPU shares). All 30 exam traps checked; every command and
flag shown (chmod, umask, ln, find, setfacl, usermod -aG, passwd -l, apt, systemctl, ss, ip, mount -t nfs, scp, docker -p,
virt-install, subprocess.run, crontab, set -e/-u/-x, pipefail) is right. Scene = 0-based SC index (the Lnn.png number).
No site/finder line, college name, TODO, placeholder, caret maths or repeated non-template sentence found.

lesson | scene | what's wrong | severity
--- | --- | --- | ---
c-unix-u1-L1 | notebook (5) | says and shows "1991: Linus Torvalds announces a kernel, under the GPL"; Linux 0.01 (1991) had Torvalds' own no-commercial-use licence, GPLv2 came with 0.12 in 1992 | wrong fact: must fix
c-unix-u4-L1 | bookfig (14), calc (16) | "apt upgrade -y: 12 upgraded, 45 − 12 = 33 still waiting" with no reason given; apt upgrade installs every available upgrade except held-back or phased ones, so students learn that upgrade is partial | misleading: should fix
c-unix-u4-L1 | pa (22) | Q2 asks for PID, PPID and STAT after kill -9 5010; the answer never states them (5010, 5000, Z briefly, then no row) | misleading: should fix
c-unix-u2-L2 | calc (10) | (d) Priya is refused lab (drwxr-x---) as "other", but lab's group is never given and scenes 13 and 15 put Priya in students, ravi's group; with that group she would get r-x | misleading: should fix
c-unix-u5-L3 | pa (19) | Q2 answer (write returns 10536, "pipe full at 65536 B") treats the pipe as a byte-counted ring; Linux fills whole 4 KB page slots, so a real O_NONBLOCK write here returns 8192. State the byte-buffer assumption | misleading: should fix
c-unix-u5-L1 | notebook (4), calc (5), trap2 (6) | "bucket = PID mod B" and the trap's "right" answer (task list + PID hash) are the pre-4.15 model; the hash was hash_long, and PIDs now live in an IDR radix tree. Say "classic kernels" | misleading: should fix
c-unix-u5-L3 | notebook (3), recap (15) | "A socket is a pipe with an address": a pipe is one-way, a socket is a two-way endpoint with a domain and type | misleading: should fix
c-unix-u1-L2 | bookfig (5) | Figure 1.3.1 shows "ls calls open, read" to list a directory; read() on a directory fails (EISDIR), ls uses getdents64 | misleading: should fix
c-unix-u3-L4 | hookArt (0), calc (5) | hook asks "who scored sixty or more?", but the pipeline first drops every name starting with R (grep -v '^R'), which has nothing to do with the question; a Ravi with 65 would be missed | misleading: should fix
c-unix-u5-L1 | recap (14) | Signals card shows a big red X for "blocked = pending, not ignored": the picture says discarded | misleading: should fix
c-unix-u1-L1, u2-L1, u3-L1, u3-L3, u5-L2, u5-L3, u5-L4 | agenda (1) | "Chapters x to y of your book" (must be "of your free notes") | should fix
c-unix-u2-L1 | bookfig (3) | spoken "Here's the tree from your book." | should fix
c-unix-u3-L4 | bookfig (3) | spoken "Here is the pipeline from your book." | should fix
c-unix-u3-L3 | calc (5, 11) | spoken "Try the book's example", "Now the book's sales example" | should fix
c-unix-u1-L3, u2-L2, u3-L4, u4-L3 | outro (22, 25, 22, 22) | "Next time, Unit two/three/four/five" spoken; "NEXT UNIT, Unit N" card | should fix
c-unix-u1-L1, u3-L1, u4-L1, u5-L2, u5-L3, u5-L4 | pq (u1-L1 18/20/22; u3-L1, u5-L2, u5-L3 16/18/20; u4-L1 19/21/23; u5-L4 14/16/18) | spoken Bloom levels: "An understand question", "Question two, apply", "at the apply level", "at the analyze level" (18 lines) | should fix
all 16 | figs (second to last) | "Sources the book draws on: …" shown | cosmetic
c-unix-u1-L3, u4-L2 | agenda (1) | "of your notes" (house wording is "your free notes") | cosmetic
c-unix-u1-L1 | recap (17) | stock stopwatch for "90 processes ÷ 2 cores = 45 per core" | cosmetic
c-unix-u3-L4 | recap (14) | stock shield for "Safe scripts"; "Key numbers" card (0, 1, 126, 127, 128+n) shows the awk output "3 229" | cosmetic
c-unix-u4-L2 | recap (14) | stock clock for "Services", stock shield for "The path" | cosmetic
c-unix-u5-L2 | recap (15) | stock shield for "Kernel locks", generic network graph for "Paging", plain tick for "The rules" | cosmetic
c-unix-u5-L1 | recap (14) | "Kernel data" picture is loose coloured dots, no list, hash or tree | cosmetic
c-unix-u2-L1 | recap (13) | all three recap pictures tiny and faint (outline tree, small terminal, small "÷1024 5.0M" box) | cosmetic
c-unix-u3-L3 | recap (13) | "Order" picture is two tiny dots and an arrow; "Pipes" is a small bar | cosmetic
all 16 (engine) | every scene header | "UNIT n · LESSON x OF y" shown on every page: unit number on screen (decide whether the rule covers the header) | cosmetic
all 16 (engine) | pq, pa | on-screen label "QUESTION n · UNDERSTAND / APPLY / ANALYZE": Bloom level shown (decide whether the rule covers labels) | cosmetic

Not slop (checked): "just", "simply", "actually", "unlock(s)" hits are plain usage (spinlock unlock, "the shell is just a
program"). Same patterns as AI and Data Structures (book wording, unit numbers, spoken Bloom, stock recap icons, tiny recap
pictures); new here: facts that are dated or simplified kernel models stated as plain Linux fact (GPL date, PID hash, pipe
bytes), and answers that skip part of their own question.
