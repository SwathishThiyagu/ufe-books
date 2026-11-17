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

## Computer Fundamentals and Programming (17 Nov)

Audited 17 Nov 2026: all 16 c-fund lessons, every scene, narration and frame (sheets at 0.92; the three suspect frames
re-rendered at 0.995 were typing animations and render whole). Checker: 0 page errors, 0 cue failures, 0 text outside the
safe area on every sheet. Every worked example and model answer recomputed (Moore's law, laptop ad, bus bottleneck, address
lines, disk read, base conversions, binary + − × ÷, complements, IEEE 754 encode/decode, chop/round error, BCD, Gray, UTF-8
bytes, Full HD size, truth tables, minterms, De Morgan, NAND-only circuits, ripple-carry adder, digit sums, bill ladder,
row/column-major addresses, struct/union sizes, endianness, SQUARE macro); all correct. The C on screen was compiled and run
with gcc 13 (main.c + total.c and nm, the predict-the-output programs, 17 % 5 * 2 + 3 < 10 && 4, switch fall-through,
reverse 1234, pointer arithmetic, sizeof of every struct and union shown): outputs match. All 32 exam traps checked: every
"Write" is right and every "Don't write" is wrong, except the two lines below. No site/finder line, college name, TODO or
placeholder, and no repeated sentence beyond the template lines. Scene = 0-based SC index (the Lnn.png number).

lesson | scene | what's wrong | severity
--- | --- | --- | ---
c-fund-u5-L2 | bookfig (3) | Figure 5.3.1 shows `char s[10] = "HELLO";` with cells 6 to 9 as "?" and the narration says they "hold leftover junk"; a string initializer zero-fills the rest of the array, so they are all '\0' (same "?" cells on names[3][8]) | wrong fact: must fix
c-fund-u5-L3 | trap2 (7) | "Forget the ampersand or the star, and you get ten twenty": swap_r(a, b) without & passes ints as pointers, which gcc 13 warns about, gcc 14 refuses to compile, and which segfaults when run (checked). Only the missing star prints 10 20 | wrong fact: must fix
c-fund-u4-L2 | pa (15) vs pa (19) | A1 says double keeps rounding error small "as in money totals"; A3 in the same lesson says never use float or double for money | misleading: should fix
c-fund-u3-L1 | notebook (10) | Worked example 1 never shows or says the expression being simplified (the book's F = A·B + A·(B + C) + B·(B + C)); the board starts at "Distribute: …", so the step and the "3 AND + 3 OR" gate count can't be followed | misleading: should fix
c-fund-u4-L1 | trap2 (12) | "A missing header gives an implicit declaration warning instead": since GCC 14, implicit function declaration is an error by default in C99 and later; true only for older compilers | misleading: should fix
c-fund-u6-L1 | bookfig (4) | Figure 6.1.1 puts pointer parameters x and y at addresses 3000 and 3004 (4-byte pointers); the same lesson's answer 1 (pa 14) says a pointer is 8 bytes | misleading: should fix
c-fund-u6-L1 | notebook (3) | the picture puts int a and the int array both at address 1000, and item 4 and the picture use an undeclared q while the narration talks about p | cosmetic: later
c-fund-u1-L1, u1-L3, u2-L1, u2-L2, u4-L2, u4-L3, u5-L1, u5-L3 (8) | agenda (1) | "Chapters x to y of your book" on the title page (book2lesson.py:324 writes it) | cosmetic: later
c-fund-u3-L1, u3-L2 (2) | agenda (1) | "Chapters 3.x to 3.y of your notes": "free" missing | cosmetic: later
c-fund 14 of 16 (all but u2-L3, u4-L1) | figs (last but one) | on-screen note "Sources the book draws on: …" (book2lesson.py:389) | cosmetic: later
c-fund-u1-L1, u1-L3, u2-L1, u3-L2, u4-L3, u5-L1, u6-L1, u6-L2 (8) | pq (all three) | spoken Bloom levels, 24 lines: "An understand question", "Question two, apply", "Question three, at the analyze level" | cosmetic: later
c-fund-u1-L3, u2-L3, u3-L2, u4-L3, u5-L3 (5) | outro (last) | "Next time, Unit two: …" spoken, and "NEXT UNIT / Unit 2" shown (book2lesson.py:501) | cosmetic: later
c-fund-u3-L1 | trap2 (6) | "Carries belong to binary addition, back in Unit two" spoken; picture label "Binary addition (Unit 2)" | cosmetic: later
c-fund all 16 | every scene | engine header "COMPUTER FUNDAMENTALS AND PROGRAMMING · UNIT n · LESSON m OF k" shows the unit number on every frame (lesson_template.html); decide whether the unit-number rule covers it | cosmetic: later
c-fund-u2-L2 | bookfig (10), recap (14) | caret maths on screen: "2^(129 − 127)" in Figure 2.4.1 and "1.f × 2^(e − 127)" on the recap card | cosmetic: later
c-fund-u4-L3 | recap (19) | stock recap icons: smiley faces labelled "a+b" and "if" for Operators and Decisions, a refresh arrow for Loops; nothing drawn from the lesson (expression tree, ladder, loop shapes) | cosmetic: later
c-fund-u1-L2 | hookArt (0) | filler: "Imagine rewiring your phone to open the calculator" | cosmetic: later
c-fund-u4-L3 | pq (24), pa (25) | asks for "two one-token fixes", but the answer's fixes are a reorder and a (float) cast, neither one token | cosmetic: later
c-fund-u1-L3 | bookfig (16), cfCode (19) | "seven-line C file" / "7-line C source", but the main.c shown is 8 lines; the nm listing "U total · U printf · T main" is not the order nm prints (T main, U printf, U total) | cosmetic: later
c-fund-u4-L2 | bookfig (3) | "±1.8 × 10³⁰⁸" renders with the last digit dropped low, reading as 10³⁰₈ (fallback glyph) | cosmetic: later
c-fund-u1-L2 | bookfig (4) | the lower crop of Figure 1.3.1 slices the control-unit, register and ALU boxes at the top edge | cosmetic: later
c-fund-u6-L2 | pq (16), pa (17) | names the union's char array "tag" ("the six-byte tag") right after Q1 used "tag field" for the type tag | cosmetic: later

Counts: 2 must fix, 4 should fix, 16 cosmetic (22 lines). Patterns shared with AI, Data Structures and Linux: "your book" /
"the book" wording (generator), unit numbers in outros (generator), spoken Bloom levels, caret maths, stock recap icons.
New here: C behaviour stated for one compiler era (implicit declaration as a warning; a missing & that "still prints"),
an initializer rule got wrong in a figure, two answers in one lesson that contradict each other, and a worked example whose
starting expression never appears on screen. Not slop (checked): "really" (u3-L1 pq 18) and "magic 18" (u4-L2, the term
"magic number") are plain usage. YouTube: pipeline.json has live: false for all six units and upload_sheet.json holds no
video links, so none of these 16 lessons is published.

## Quantum Computing (17 Nov)

Audited 17 Nov 2026: all 20 c-quantum lessons (6 units), every scene, narration and frame (sheets at 0.92, re-rendered at
0.995; the half-written highlight lines at 0.92 render whole at 0.995). Checker: 0 page errors, 0 cue failures, 0 text
outside the safe area on any lesson. Scene numbers below are the 0-based SC index (the Lnn.png number).
Facts: every worked example and model answer recomputed (memory for n qubits, eigenvalues, tensor amplitudes, e^(iA),
Born-rule and ± basis probabilities, partial trace of |Φ+⟩, Bloch angles, CHSH E and 0.8536, Robertson bound, H Z H,
three-CNOT swap, H S H, T⁴, teleportation and superdense branches, Qiskit counts and bit order, kickback signs,
Deutsch-Jozsa, Bernstein-Vazirani for s = 101 and 1011, Simon equations, QFT|01⟩, order finding for 15 and 21, Grover
P(k) for N = 16, counting for N = 100 and 64, one-time pad, BB84 sifting, entropies 0.469 and 0.8113, bit-flip χ, Hamming
(7,4) codeword, bit-flip syndromes, 3p² failure rate, VQE energy, kernel eigenvalues, Ising form of the portfolio, AES and
RSA bits). All 46 exam traps checked: every "Don't write" is wrong and every "Write" is right. One stated method is wrong.
Clean (scripted): no filler words (hits were "take a dive" in a joke, "unlocks" a lock, "landscape" the optimisation term),
no site or finder line, no college names, no TODO or placeholder, no repeated sentences beyond template lines.
YouTube: pipeline.json has live: false for all six units and videos.json has no video link, so none is published.

lesson | scene | what's wrong | severity
--- | --- | --- | ---
c-quantum-u3-L1 | pa (21) | "Multiply by H on the left: one half times zero, two, two, zero, which is X"; board hint "multiply HZ first, then H on the left". H·(HZ) = Z; H Z H = (HZ)·H needs H on the right. The matrix shown is right, the method said is wrong | wrong fact: must fix
c-quantum-u3-L3 | pa (17) vs bookfig (9) | answer for m1m2 = 11 says "XZ: apply Z first, then X", but the lesson's own circuit applies X (from m2) and then Z (from m1); both work up to a global sign, but the answer contradicts the picture | misleading: should fix
c-quantum-u1-L2 | bookfig (11) | box "H\|0⟩ = \|+⟩, first row: 0.7071, 0.7071": H\|0⟩ is the first column (same numbers only because H is symmetric); u2-L2 pa (19) says "second column" correctly | misleading: should fix
c-quantum-u4-L2, u4-L3, u5-L2 (3) | bookfig (4); calc (10); bookfig (3, 8, 13), calc (5, 10, 16) | spoken "the book's picture / example / figure / channel / repetition code", 8 lines (must be "your free notes") | should fix
c-quantum-u1-L3, u2-L1, u2-L4, u3-L3, u4-L1, u4-L3, u6-L1 (7) | pq (all three) | spoken Bloom levels, 21 lines: "at the understand level", "An understand question", "Question two, apply", "Question three, analyze" | should fix
c-quantum-u1-L3, u2-L4, u3-L4, u4-L4, u5-L3 (5) | outro (last) | "Next time, Unit two/three/…" spoken, and "NEXT UNIT / Unit N" shown (book2lesson.py:501) | should fix
c-quantum-u6-L1 | pa (22) | on screen "QPE (Unit 4) reads an eigenvalue of H into ancillas" | should fix
c-quantum-u6-L2 | outro (25) | "THAT'S A WRAP / All six units" card (unit count shown) | cosmetic: later
c-quantum all 20 | figs (last but one) | on-screen red note "Sources the book draws on: …" (book2lesson.py:389) | cosmetic: later
c-quantum-u1-L1, u1-L3, u2-L1, u2-L2, u3-L2, u4-L1, u4-L2, u4-L3, u4-L4 (9) | notebook, calc, trap2, recap, pq/pa, bookfig text | caret maths on screen, about 100 strings: "e^(iθ)", "e^(−iHt/ħ)", "a^(r/2)", "2^(n/2)", "N^(1/3)", "(−1)^(s·x)", "e^(2πijk/N)" (u1-L3 alone has it in 8 scenes) | cosmetic: later
c-quantum-u2-L1, u2-L3, u2-L4, u3-L1, u4-L1, u4-L2, u4-L3, u5-L2, u5-L3 (9) | notebook, bookfig, calc, pa | underscore subscripts on screen: "ρ_A", "tr_B", "P_m", "H_A ⊗ H_B", "S_z", "F_z", "U_f", "U_w", "U_CNOT", "d_min" (u2-L3 in 12 scenes); same problem as caret maths, for subscripts | cosmetic: later
c-quantum-u5-L3 | recap (14) | stock recap icons: orange shield (Error correction), six scattered dots (Fault tolerance, the "chain" icon), red down arrow (The threshold); nothing from the lesson (three-qubit code, transversal CNOT, threshold curve) | cosmetic: later
c-quantum-u6-L2 | recap (17) | stock-looking recap icons: refresh arrow with a tick (Industry), padlock (Security), a bare "U" gate (Quantum AI); small and faint | cosmetic: later
c-quantum-u1-L3, u3-L2, u4-L2 (3) | recap | tiny recap pictures: icons about a tenth of the card in faint circles (u4-L2's QFT card is a generic four-way arrow) | cosmetic: later
c-quantum-u1-L3, u4-L2 (2) | recap | header pill wider than its card: "OPERATOR FUNCTIONS" and "BERNSTEIN-VAZIRANI" run into the next card (still there at 0.995) | cosmetic: later
c-quantum-u2-L4 | bookfig (9) | the view crops off the z magnet, so a stray "½ down" arrow points at a "blocked" box; the rest of the frame is three lines of text | cosmetic: later
c-quantum-u2-L2 | bookfig (4) | three pairs of probability bars with no headings (the \|0⟩, H\|0⟩, ZH\|0⟩ labels are outside the view) | cosmetic: later
c-quantum-u4-L3 | calc (10) | "Your turn, with the book's next one" on a worked example the board solves at once, with no pause | cosmetic: later
c-quantum-u5-L2 | pa (20) | "So the capacity needs a limit": vague; meant "capacity is a limit over many uses" (the screen says so) | cosmetic: later
c-quantum-u1-L1 | notebook (6) | the "mid-90s" pill touches the "Error correction" label in the timeline picture | cosmetic: later

Counts: 1 must fix, 6 should fix, 13 cosmetic (20 lines). Patterns shared with other subjects: "the book" wording (generator
note on all 20 figs pages plus 8 spoken lines), unit numbers in outros (generator), spoken Bloom levels, caret maths, stock
or tiny recap pictures. New here: underscore subscripts typed on screen (9 lessons, the subscript twin of caret maths);
recap header pills wider than the card (engine, long upper-case labels); a matrix-order method stated backwards while the
numbers are right; an answer whose gate order contradicts the lesson's own circuit.

## Mobile Application Development (17 Nov)

Audited 17 Nov 2026: all 17 c-mobile lessons, every scene, narration and frame (sheets at 0.92; every line that looked cut off
re-rendered at 0.995, where all render whole, so they were typing animations). Checker: 0 page errors, 0 cue failures, 0 text
outside the safe area on every sheet. About 70 worked numbers and model answers recomputed (transmission and delay times,
generation download times, GSM slots and frame rate, N/D/Q/SIR, handover loss, tunnel overhead, 802.11 efficiency, RREQ counts,
weights and dp/px, fitCenter/centerCrop, header-row positions, byte counts, cursor order, 1.5 MB in bytes, SMS parts and cost,
camera centre and spans, location filter rates, PIN lockout times, versionCode/versionName, card fees, Swift fares, stack-view
widths, constraint conflicts): no arithmetic error. All 40 exam traps checked: every "Don't write" is wrong and every "Write"
is right, except where listed. Scene = 0-based SC index (the Lnn.png number). No site/finder line, college name, TODO,
placeholder or filler word found; the only repeated non-template sentences are the spoken Bloom lines below.

lesson | scene | what's wrong | severity
--- | --- | --- | ---
c-mobile-u3-L1 | pa (17) | model answer: "Return false, and the event falls through, so the command looks dead". The handler code has already run; false only lets the click go on to fragments or the item's intent, so nothing "looks dead" | wrong fact: must fix
c-mobile-u6-L3 | bookfig (3), notebook (5) | fare written as "8 km × ₹11.50 = ₹92.00" (no booking fee, outstation rate), while scene 8/11 of the same lesson and u6-L1/L2 price 8 km as 20 + 8 × 9.0 = ₹92; same answer from two contradicting fare rules | misleading: should fix
c-mobile-u6-L1 | bookfig (10), calc (13) | fareLabel shows "fare = 20 + km * rate" with no parameter type; the same lesson just taught that km = 8 is an Int and km * rate stops the build. The book has fareLabel(km: Double); the lesson never shows it | misleading: should fix
c-mobile-u5-L2 | bookfig (15) | caption "A lockout delay matters more than PIN length"; by the lesson's own numbers two more digits (100× = 100,000 s) beat the lockout (61×) | misleading: should fix
c-mobile-u5-L2 | pa (23) | cause given as "the network provider with no GPS view of the sky": the network provider never uses the sky; the cause is that only the network (cell/Wi-Fi) provider is giving fixes | misleading: should fix
c-mobile-u2-L1 | trap2 (15) | "compileSdk is build time only, never in the manifest": aapt2 has written android:compileSdkVersion into the merged manifest since build tools 28. The point (it does not set run-time behaviour) is right; "never in the manifest" is not | misleading: should fix
c-mobile-u2-L1 | pa (18) | "a retail phone has no Linux package manager or shell tools": every Android phone ships /system/bin/sh and toybox; only the package manager part is right | misleading: should fix
c-mobile-u2-L3 | bookfig (4), notebook (5), trap2 (6) | "Check resolveActivity first, start only when not null" is taught as the safe rule; with targetSdk 30+ (the earlier lesson uses 34) package visibility makes resolveActivity return null unless `<queries>` is declared, so Share silently does nothing. Say: declare `<queries>`, or catch ActivityNotFoundException | misleading: should fix
c-mobile-u2-L3 | notebook (5) | code panel would not compile: "Intent.ACTION_DIAL" and "Uri.parse(...)" with no new Intent, setType/putExtra with no receiver, share never declared, resolveActivity(...) != null with no if | should fix
c-mobile-u2-L2 | calc (13, 14), bookfig (11, 12) | question says "launch, Home, recents, Back, then rotate" as one sequence; after Back the activity is destroyed, so there is nothing to rotate (needs a relaunch, 3 more lines). Present the five as separate actions | misleading: should fix
c-mobile-u4-L2 | bookfig (10) | Figure 4.5.1: the ✓ line (what the viewer may do) is orange and the ✗ line (cannot list, cannot write) is green, so the picture reads the forbidden actions as allowed (already noted in done.log, not fixed) | misleading: should fix
c-mobile-u3-L1 | hookArt (0) | hook repeats u2-L2's hook almost word for word ("tap a counter to seven, turn the phone, it reads zero; where did the seven go?") | should fix
c-mobile-u1-L3, u2-L3, u3-L2, u4-L2, u5-L3 | outro (27, 23, 26, 28, 23) | "Next time, Unit two/three/four/five/six" spoken; "NEXT UNIT, Unit N" card (book2lesson.py writes this card itself) | should fix
c-mobile-u1-L1, u1-L2, u1-L3, u2-L1, u2-L3, u3-L1, u3-L2, u4-L2, u5-L1, u5-L2, u5-L3, u6-L4 | pq (u1-L1 18/20/22; u1-L2 15/17/19; u1-L3 20/22/24; u2-L1 17/19/21; u2-L3 16/18/20; u3-L1 16/18/20; u3-L2 19/21/23; u4-L2 21/23/25; u5-L1 14/16/18; u5-L2 18/20/22; u5-L3 16/18/20; u6-L4 14/16/18) | spoken Bloom levels: "An understand question", "Question two, apply", "at the apply level", "Question three, analyze" (36 lines). u2-L2, u4-L1, u6-L1, u6-L2, u6-L3 say only "Question one/two/three" | should fix
c-mobile-u1-L1, u1-L2, u1-L3, u2-L2, u4-L2, u5-L1, u5-L2, u6-L1, u6-L2, u6-L3, u6-L4 | figs (second to last) | "Sources the book draws on: …" shown; the other 6 lessons say "Sources the notes draw on" | cosmetic
c-mobile-u5-L2 | calc (12, 13) | formula board "N = 10^d" typed with a caret | cosmetic
all 17 (engine) | every scene | header strip shows "MOBILE APPLICATION DEVELOPMENT · UNIT n · LESSON k OF K" on every frame (META.kick from book2lesson.py); u6-L4 outro also shows "All six units" | cosmetic
all 17 (engine) | pq, pa | question cards print the Bloom level on screen ("QUESTION 1 · UNDERSTAND", "· APPLY", "· ANALYZE") from lv, even where the narration avoids it | cosmetic
all 17 | META | META.subject is "biotech" (book2lesson.py default --subject biotech); not shown today, wrong if the engine ever uses it | cosmetic
c-mobile-u2-L1 | bookfig (6) | second half of a split figure: the three columns have no platform names (Android, iOS, Windows Phone sit on the previous scene) | cosmetic
c-mobile-u2-L2 | bookfig (12) | second half of Figure 2.4.1: five line counts under empty space and two orphan boxes (onStart, onResume) cut from the rotate column | cosmetic
c-mobile-u4-L2 | bookfig (4, 10) | split-figure halves start with an orphan arrow from nothing; scene 4 is a small table in a mostly empty box | cosmetic
c-mobile-u6-L2 | notebook (13), trap2 (14) | the index-out-of-range trap repeats u6-L1's trap (0...count reads one past the end) one lesson later | cosmetic
c-mobile-u1-L1 | calc (5, 10) | two conventions in one lesson: "1 KB = 1024 bytes" in example 1, "1 MB = 10⁶ bytes" in example 2 (each hinted, but not explained) | cosmetic
c-mobile-u2-L1 | notebook (10) | "a stack of six layers" but the narration lists five (native libraries and ART share one) | cosmetic
c-mobile-u4-L1 | figs (25) | sources line cut: "Sources the notes draw on: Bill Phillips (SQLite databases and content providers)", no book title | cosmetic
c-mobile-u6-L1 | outro (23) | next card reads "Swift structures · Building" (chapter titles cut mid-name) | cosmetic
c-mobile-u5-L2 | recap (17) | "Key numbers" card uses a generic clock and padlock for two unrelated numbers (3 updates a minute; PIN 1,000 s → 61,000 s) | cosmetic

Recap pictures otherwise come from each lesson's own content (towers, hexes, tunnels, stacks, tables, fare boxes); no shield,
refresh arrow or up-arrow stock icon. No picture contradicts its narration except Figure 4.5.1's colours above (the colour
cues spoken in u1-L3, u2-L2, u5-L1 and u6-L4 match their figures). YouTube: pipeline.json has live: false for all six units
and videos.json has an empty video link for all 17 lessons, so none is published.

## AR/VR (17 Nov)

Audited 17 Nov 2026: all 21 c-xr lessons (6 units, built 17 Nov), every scene, narration and frame. SC arrays dumped with
Playwright; sheets at 0.92, every overlap re-rendered at 0.995. Checker: 0 page errors, 0 cue failures, 0 text outside the
safe area on any lesson. Scene numbers below are the 0-based SC index (the Lnn.png number).
Facts: every worked example and model answer recomputed (frame budgets, latency sums, samples per frame, ultrasonic d = vt,
mocap counts, tilt from gravity, gyro drift, lighthouse angle, lens 1/f = 1/v − 1/u, pixel arcmin, shutter rates, stereo
disparity, ITD and samples, spring and saturation, pin counts, b > kT/2, mesh bytes, Rz(90°) placement, sphere penalty
force, record counts, projection, culling chain, quaternion rotation and m00, ray–sphere t and d, Go-Go, route length,
weighted success, scene-graph positions, draw calls, impulse, A/B rates, overlay slip, marker depth, precision/recall,
normalised gain, round-trip distance); all arithmetic is right. The PushCube C# script compiles as shown (legacy Input).
Recap icons: the stopwatch (u1-L2, u4-L4, u5-L4) and refresh arrow (u1-L2) each sit on a timing or loop card, so not flagged.
YouTube: pipeline.json has live: false for all six units and upload_sheet.json has no video link, so none is published.

lesson | scene | what's wrong | severity
--- | --- | --- | ---
c-xr-u2-L2 | bookfig (10, 11), calc (13), recap (15) | hysteresis "enter 145°, leave 135° → one fist, one event", but the held fist reads 137–143° (the figure draws it never reaching the 145° line), so it never fires: zero events, not one. The band must sit around a reading that crosses it (e.g. enter 140°, leave 130° for a fist held at 140 ± 3°). Same error in the unit book's Figure 2.4.1 | wrong fact: must fix
c-xr-u5-L1 | trap2 (8) | "Don't write: ray selection picks the object nearest along the ray (small t)" marks a true statement wrong: ray casting does take the first hit along the ray (u2-L2 trap (7) and u5-L1 notebook (5) say so; the book says "selects the first object it hits"). The wrong-side picture also shows an off-ray sphere labelled "nearest along the ray". Trap is writer-made, not in the book | wrong fact: must fix
c-xr-u2-L2 | bookfig (4), calc (5, 6), pa (19) | linear "virtual = D + k(d − D)" taught as Go-Go; the book says this is a simplified linear form and the original Go-Go gain grows with d (quadratic); the lesson drops that caveat | misleading: should fix
c-xr-u4-L3 | calc (12) | "54 million triangles a second" drops "per eye" (book and figure 4.6.1 say per eye); both eyes need 108 million, and the hook says the city is drawn twice | misleading: should fix
c-xr-u6-L1 | bookfig (12), calc (13, 14) | "video view is 3.4 times worse" drops the book's "until the camera frame is delayed to match the render" (video can delay the real view to match); and "the difference is the camera capture" while 68 − 20 = 48 ms, not 33 | misleading: should fix
c-xr-u3-L4 | bookfig (4) | "the rule: pin pitch ≈ the two-point threshold" but the narration gives the palm threshold as 10 mm and the palm array uses a 5 mm pitch (book has the same) | misleading: should fix
c-xr-u2-L3 | bookfig (13), calc (15) | lighthouse timing (four 4.17 ms sweeps per 16.67 ms frame, a 120° fan, 28,777°/s) is the book's toy model, stated as how lighthouse works; real v1 rotors turn at 60 rev/s (21,600°/s). Say "a simplified model" | misleading: should fix
c-xr-u1-L2, u2-L1, u2-L2, u3-L1, u3-L3, u4-L1, u4-L2, u4-L3, u4-L4, u5-L1, u5-L2, u5-L3, u5-L4, u6-L2, u6-L3 (15) | pq (all three) | spoken Bloom levels, 45 lines: "Exam practice! An understand question.", "Question two, apply.", "Question three, analyze." (u4-L3: "Question one, understand.") | should fix
c-xr-u1-L3, u2-L3, u3-L4, u4-L4, u5-L4 (5) | outro (21, 25, 22, 23, 24) | "Next time, Unit two/three/four/five/six: …" spoken, and "NEXT UNIT / Unit N" shown (book2lesson.py:501) | should fix
c-xr-u4-L3, u5-L3, u5-L4, u6-L3 (4) | bookfig (3, 8); codeBoard (14, 15); bookfig (5, 7, 14); bookfig (4, 10) | "the book's figure / chart / script / safe first session", 9 spoken lines; u5-L3 also shows "The book's script: PushCube" as the title of two scenes | should fix
c-xr-u2-L2 | calc (12, 13) | caret maths on the formula board: "resolution = range ÷ 2^bits" (the hint on the same board writes 2⁸ correctly) | should fix
c-xr all 21 | figs (last but one) | on-screen red note "Sources the book draws on: …" (book2lesson.py:389) | cosmetic: later
c-xr-u6-L3 | outro (21) | "THAT'S A WRAP / All six units" card (unit count shown) | cosmetic: later
c-xr all 21 | META | META.subject is "biotech" on CSE lessons (book2lesson.py:485 defaults --subject to biotech); not drawn, but anything reading META gets the wrong subject | cosmetic: later
c-xr-u3-L1 | hookArt (0) | filler "A walk-in CAVE looks amazing" | cosmetic: later
c-xr-u1-L3 | calc (11) | narration says "metres" (WRITE.md: US spelling in say) | cosmetic: later
c-xr-u1-L1 | bookfig (9) | "Here are four landmarks on one time line" names three; the fourth dot (1968) has no label until the next scene | cosmetic: later
c-xr-u1-L1 | trap2 (12) | "CAVE, 1992: about two decades later" for a 24-year gap (the lesson's own worked example) | cosmetic: later
c-xr-u5-L3 | codeBoard (15) | "OnTriggerEnter checks the Wall tag and calls haptics" while the body is only a comment | cosmetic: later
c-xr-u4-L3, u4-L4, u5-L3, u5-L4, u6-L1, u6-L2 (6) | bookfig (8, 9); (4); (11); (5, 7); (5, 12); (15) | small figure in a mostly empty panel: one thin strip or a few text lines in the top third of the stage | cosmetic: later
c-xr-u3-L1, u4-L4, u5-L3, u4-L2 (4) | bookfig (11); (4); (11); (5) | overlaps still there at 0.995: sight lines run through the "L img / R img" labels; the 11.1 ms budget line cuts "show"; "AddForce 1.6 N·s, Impulse" fills its box edge to edge; the two spheres are cut off at the bottom by the zoom | cosmetic: later
c-xr-u1-L1, u1-L2, u6-L3 (3) | recap (14, 13, 13) | small recap pictures: icons about a fifth of the card (u1-L1's "Three waves" is four dots on a line) | cosmetic: later

Counts: 2 must fix, 9 should fix, 11 cosmetic (22 lines). Patterns shared with other subjects: spoken Bloom levels (15 of 21
lessons, the most of any pattern here), "the book" wording (generator note on all 21 notes pages plus 9 spoken lines),
unit numbers in outros (generator), caret maths, small figures and recap pictures. New here: META.subject defaults to
biotech for every non-biotech subject; a writer-made exam trap that marks a true statement wrong; lessons that drop the
book's own caveat ("simplified linear form", "per eye", "until the camera frame is delayed") and so overstate the fact.

## Parallel and Distributed Computing (17 Nov)

Audited 17 Nov 2026: all 21 c-dist lessons, every scene, narration and frame (sheets at 0.92 and re-rendered at 0.995; every
line cut off at 0.92 was a typing animation and renders whole at 0.995). Checker: 0 page errors, 0 cue failures, 0 text
outside the safe area on every sheet. About 90 worked numbers and model answers recomputed (Amdahl, PRAM rounds and cost,
mesh/tree/cube degree-diameter-bisection, block loads and imbalance, transpose pairs, 2×2 products, doubling scan, p-ary
search, median-of-medians, bitonic depth, Gaussian elimination, Borůvka, OpenMP block sums, Scatter/Reduce, CUDA indices,
copy timelines, NDRange ids, message cost, RPC slowdown, NTP θ/δ, Lamport and vector stamps, 12 concurrent pairs, snapshot
totals, causal delivery, Ricart–Agrawala and Suzuki–Kasami counts, OM(1), the domino rollback, quorums, semi-join bytes,
2PC counts, IaaS/PaaS bills, pre-copy rounds, elastic sizing, grid schedules, edge-cache latency). Both code samples build:
the OpenMP sum compiles with gcc -fopenmp and prints S = 500000500000; the MPI sum passes a syntax check against MPI
prototypes. All 44 exam traps checked. Scene = 0-based SC index (the Lnn.png number). No site/finder line, college name,
TODO, placeholder, caret maths or repeated non-template sentence found ("site" hits are distributed-system sites).
YouTube: pipeline.json has live: false for all six units and upload_sheet.json holds no video links, so none is published.

lesson | scene | what's wrong | severity
--- | --- | --- | ---
c-dist-u5-L3 | pa (16) | "At-most-once sends the request once and never retries, so it may lose it": that is maybe semantics. At-most-once retries with duplicate filtering, exactly what the same lesson shows in scenes 3 to 6 | wrong fact: must fix
c-dist-u2-L2 | pa (20) | two-level scan with n = 10⁶, p = 1000 "takes about 1000 + 10 ≈ 1010 steps": every block is passed twice (local scan, then add the offset), so ≈ 2n/p + log p ≈ 2010. The order O(n/p + log p) is right | wrong fact: must fix
c-dist-u3-L3 | bookfig (3, 4), calc (6) | shared-memory sum step 1: thread 0 does s[0] = s[0] + s[1] while thread 1 writes s[1] = s[2] + s[3], same step, no barrier: a read-write race on s[1] in the lesson about barriers. Use s[0] += s[2], s[1] += s[3], barrier, s[0] += s[1] | wrong fact: must fix
c-dist-u4-L1 | trap2 (10) | "Write: 8 × 5000 × 2 ms = 80 s, not 10 s" assumes every message is serialised; eight machines each sending 5000 messages in parallel add about 10 s of wall time, so the "Don't write" can be right. The serial-messages assumption is never stated | misleading: should fix
c-dist-u5-L2 | notebook (3), trap2 (8) | "Crash faults: N ≥ 2f + 1, and f + 1 rounds" mixes two models: the synchronous f + 1-round algorithm tolerates any f < N; 2f + 1 is the asynchronous/partially synchronous (Paxos, Raft) majority bound. The trap's "Write" repeats it | misleading: should fix
c-dist-u5-L1 | notebook (15, 16), trap2 (17) | Chandy–Misra–Haas probe written as (waiting, waited-on, initiator); textbooks write probe(initiator, sender, receiver) and detect deadlock on probe(i, j, i). In the textbook notation the lesson's first probe(P1, P2, P1) already reads as "deadlock" | misleading: should fix
c-dist-u1-L4 | calc (13, 14) | "Data parallel ≈ 28 × faster" compares 32 images per 80 ms against a micro-batch of 1 image per 40 ms; the on-screen question never gives the micro-batch size, and with 32-image micro-batches model parallel gives 0.8 images/ms, faster than 0.711 | misleading: should fix
c-dist-u1-L4 | pq/pa (17, 18) | "Why does data parallelism match Flynn's SIMD model?": multi-GPU data parallelism is SPMD/MIMD (each GPU runs its own instruction stream). Contradicts the u1-L1 trap "multicore is MIMD, not SIMD" | misleading: should fix
c-dist-u3-L2 | bookfig (3), calc (5, 6) vs bookfig (9), calc (11, 12) | same add<<<2, 4>>> launch: C[5] = 11 + 3 = 14 in Figure 3.3.1 and example 1, but C[5] = 13 + 3 = 16 in Figure 3.4.1 and example 2 (there A[4] = 11) | misleading: should fix
c-dist-u2-L2 | notebook (11), trap2 (13) | selection "with p = n: time Θ(log n)": the median-of-medians rounds shown each need a prefix-sum compaction (Θ(log n)) over Θ(log n) rounds, so Θ(log² n); Θ(log n) needs a different algorithm | misleading: should fix
c-dist-u2-L2 | bookfig (9), notebook (11) | "p = 4 processors" but only 3 probes, and ⌈logₚ(n + 1)⌉ steps; the usual result uses all p probes: ⌈log₍ₚ₊₁₎(n + 1)⌉. Same answer (2) here, different formula in an exam | misleading: should fix
c-dist-u6-L2 | notebook (5), pq/pa (20, 21) | "3PC: a partition still blocks it" and "neither group can decide alone": 3PC's failure under a partition is that the two sides can decide differently (unsafe), not that it blocks | misleading: should fix
c-dist-u1-L3 | notebook (10) | picture label "idle time: E ≈ 0.588": the value is efficiency, not idle time | misleading: should fix
c-dist-u2-L1 | pa (15) | "swapping the diagonal can cause a double write, or a race": one processor owns each diagonal cell, so there is no race; it is only wasted work | misleading: should fix
c-dist-u1-L1, u4-L1, u4-L4 | agenda (1) | "Chapters x to y of your book" (generator default, book2lesson.py:324) | should fix
c-dist-u2-L1 (5, 12), u3-L3 (3, 9, 14), u5-L2 (11) | calc, trap2, bookfig | spoken "the book's example", "the book's model", "Your book's figure", "Your book's timeline", "the book's run" | should fix
c-dist-u1-L4 (24), u2-L3 (25), u3-L3 (26), u4-L4 (22), u5-L3 (22) | outro | "Next time, Unit two/three/…" spoken; "NEXT UNIT, Unit N" card (generator, book2lesson.py:501) | should fix
c-dist-u2-L1 (21), u6-L4 (24) | outro | "two building blocks of this unit" spoken; "All six units" on the wrap card | cosmetic
c-dist-u1-L1, u3-L1, u4-L3 | pq (17/16, 19/18, 21/20) | "An understand question", "Question two, at the apply level", "at the analyze level" spoken | should fix
c-dist-u4-L1, u4-L2, u4-L4 | pq (19/20/15, 21/22/17, 23/24/19) | "An understand question", "Question two, apply.", "Question three, analyze." spoken (a second phrasing the old pattern misses) | should fix
all 21 | figs | "Sources the book draws on: …" on screen (generator, book2lesson.py:389) | cosmetic
all 21 | every page, pq | engine shows "UNIT n · LESSON n OF n" in the header and "QUESTION 1 · UNDERSTAND/APPLY/ANALYZE" on question cards: shown unit numbers and Bloom words, outside the narration rule | cosmetic (decide)
c-dist-u1-L3 | recap (14) | stock icons: stopwatch (Performance), red X (Amdahl's ceiling); tiny cube for Networks | cosmetic
c-dist-u4-L1 (18), u4-L4 (14) | recap | stopwatch for "Key numbers" | cosmetic
c-dist-u4-L2 | recap (19) | stopwatch for "Models" | cosmetic
c-dist-u4-L3 | recap (15) | green tick for "The test" | cosmetic
c-dist-u1-L4 (10), u2-L2 (10), u4-L1 (4), u4-L2 (9) | bookfig | figure halves drawn as a thin strip or a bare time axis, two thirds of the stage empty | cosmetic
c-dist-u6-L2 | bookfig (4) | "figure" is a text paragraph with no picture; narration says "Below the timelines" but no timeline is on screen | cosmetic
c-dist-u6-L2 (3), u4-L4 (3), u5-L2 (11) | bookfig | overlaps: the three prepare and abort arrows run into one bundle; cut S1 runs along the message arrow through "₹30 in transit"; label C2,1 touches m4's arrowhead | cosmetic
c-dist-u1-L2 | bookfig (12) | priority CRCW "highest index P7 wins"; the common convention is lowest index, so say it is a chosen priority | cosmetic
c-dist-u4-L4 | pq/pa (17 to 20) | Q2 and Q3 repeat the worked example's numbers (₹100 each, ₹30, S1/S2); practice tests nothing new | cosmetic
c-dist-u5-L3 (13), u6-L3 (13) | trap2 | the same R + W > N trap in two lessons | cosmetic
c-dist-u6-L2 | hookArt (0) | filler "Now imagine" | cosmetic

New here: a model answer that contradicts its own lesson (u5-L3 at-most-once; u1-L4 SIMD against u1-L1's trap; u3-L2's two
values of C[5]), comparisons whose result depends on an assumption never put on screen (u1-L4 micro-batch, u4-L1 serial
messages), and a second spoken Bloom form ("Question two, apply.") that a check for "at the … level" alone misses.
Generator defaults (book2lesson.py:324 "of your book", :389 "Sources the book draws on", :501 "NEXT UNIT / Unit N") are
the source of three of the text patterns.

## Blockchain (17 Nov)

Audited 17 Nov 2026: all 20 c-block lessons (482 scenes), every scene, narration and frame (sheets at 0.92 and re-rendered
at 0.995; the cut-off lines at 0.92 were typing animations and render whole at 0.995). Checker: 0 page errors, 0 cue
failures, 0 text outside the safe area on every sheet. None is on YouTube yet (pipeline.json: all draft, live false).
About 70 worked numbers and model answers recomputed (2¹²⁷ key search, SHA-256 padding to 1024 bits, 2⁶³ hashes in years,
ECC doubling of P = (5, 1) on y² = x³ + 2x + 2 over F17 and all 18 plotted points, toy ECDSA with n = 11, Base58Check
25 bytes, flooding hops, fee rates, BFT quorums for n = 7, 10, 13, Tendermint rounds, 16⁴ nonce tries, retarget × 1.1667,
PoS share 28.93%, fork 355.76 → 356, change and fee in satoshi, P2PKH stack, halving reward in BTC and rupees, UTXO
selection, 6.67 tx/s, gas and wei to ETH, GHOST weights, insurance payouts with deductible and cap, supply-chain
percentages, fridge sensor hashes, 83.33 tx/s and 3.6 GB/day): no arithmetic error. All exam traps checked; the one
whose "Don't write" is not wrong is listed below. Agendas all say "free notes". Scene = 0-based SC index (the Lnn.png
number). No site/finder line, college name, TODO, placeholder or caret maths found.

lesson | scene | what's wrong | severity
--- | --- | --- | ---
c-block-u4-L2 | notebook (3), trap2 (5), recap (16), outro (24) | "scriptSig and scriptPubKey are joined and run once"; Bitcoin has run scriptSig, then scriptPubKey on the copied stack, separately since 2010, so the trap marks the real behaviour as the wrong answer | wrong fact: must fix
c-block-u5-L4 | calc (7) | says a transaction's "return value and events" are in the receipt once mined; a receipt holds status, gas used and logs, the return value is not stored (only a call or an event gives it back) | wrong fact: must fix
c-block-u5-L3 | notebook (3) | SimpleBank code does `emit Paid(msg.sender, msg.value);` with no `event Paid(...)` declared: does not compile | wrong fact: must fix
c-block-u1-L1 | trap2 (6), pa (17) | "3 January 2009: the network" / "ran live from 3 Jan"; 3 Jan is the genesis block's timestamp, the software and block 1 came on 9 Jan 2009 | misleading: should fix
c-block-u3-L2 | bookfig (5), calc (8) | "a 40% miner cannot outrun the honest chain" said and drawn as absolute; a 40% miner wins short races often ((q/p)^z = 0.67 for one block behind); only the calc step says "for long" | misleading: should fix
c-block-u4-L2 | trap2 (15) | narration "a 51% miner can reverse or censor its own transactions": it reverses its own but censors anyone's | misleading: should fix
c-block-u2-L3 | notebook (11), recap (14) | private key is d and k is the nonce in Part 1, then "P = k × G" in Part 2; the recap shows "P = k × G" beside "Fresh k every time", so the key and the nonce look the same | misleading: should fix
c-block-u5-L2 | notebook (10), pq/pa (18, 19) | teaches "a call only reads", then the question's CALL opcode changes storage (eth_call vs CALL message call never told apart) | misleading: should fix
c-block-u5-L3 | calc (11, 12) | "the fee goes to the miner"; u5-L1 teaches base fee burned and tip to the block producer, and there are no miners since the Merge | misleading: should fix
c-block-u5-L3 | bookfig (10) | private network steps "geth init … unlock A … mine block 1"; current Geth has no PoW mining or account unlock, a private net needs --dev or a consensus client | misleading: should fix
c-block-u5-L4 | notebook (11), pq/pa (15, 16) | uncle (ommer) blocks taught in the present tense (none since the Merge, Sept 2022); "uncle rewards also discourage selfish mining", but they make selfish mining more profitable | misleading: should fix
c-block-u6-L1 | trap2 (15) | "Don't subtract the deductible before the cap. That gives 1,70,000": subtracting before the cap gives the same 1,75,000 here (only subtracting twice gives 1,70,000), and deductible first, then limit, is common practice | misleading: should fix
c-block-u4-L4 | notebook (4) | "Co-spending: one signer held both keys" stated as certain; the next scene teaches CoinJoin, which breaks exactly that heuristic | misleading: should fix
c-block-u1-L3 | notebook (4) | "Merkle root: one hash for every transaction" reads as one hash per transaction (meant: one hash covering all) | misleading: should fix
c-block-u4-L2 | recap (16) | Scripts picture shows a stack of TRUE over pubkey over sig; after OP_CHECKSIG only TRUE is left: picture contradicts the narration | misleading: should fix
c-block-u5-L2 | recap (13) | EVM picture shows the stack 5 / 3 / 2 after ADD, which leaves only [5]: picture contradicts the narration | misleading: should fix
c-block-u2-L2, u2-L3, u3-L2, u6-L3 | bookfig (u2-L2 5, 11; u2-L3 3; u3-L2 4, 12), calc (u6-L3 15) | spoken "In the book's figure", "the book's toy example"; hint "decimal units, as in the book" (must be "your free notes") | should fix
c-block-u1-L3, u2-L3, u3-L3, u4-L4, u5-L4 | outro (24, 22, 25, 23, 22) | "Next time, Unit two/three/four/five/six" spoken; "NEXT UNIT, Unit N" card | should fix
c-block-u1-L1, u1-L2, u2-L2, u3-L2, u5-L2, u6-L3 | pq (u1-L1 14/16/18; u1-L2 18/20/22; u2-L2 16/18/20; u3-L2 19/21/23; u5-L2 14/16/18; u6-L3 18/20/22) | spoken Bloom levels: "An understand question", "at the apply level", "at the analyze level", "Question two, apply", "Question three, analyze" (18 lines) | should fix
all 20 | figs (second to last) | "Sources the book draws on: …" shown | cosmetic
all 20 (engine) | every scene header | "UNIT n · LESSON x OF y" on every page (same open question as Linux) | cosmetic
all 20 (engine) | pq, pa | on-screen "QUESTION n · UNDERSTAND / APPLY / ANALYZE" label (same open question as Linux) | cosmetic
c-block-u6-L3 | outro (25) | "All six units" card: unit count on screen | cosmetic
c-block-u1-L1 | recap (13) | stock shield for "Faults" | cosmetic
c-block-u3-L2 | recap (18) | generic document block for "PoW"; calendar for "Difficulty", though the retune is every 2016 blocks, not by date | cosmetic
c-block-u6-L3 | recap (17) | stock network graph for "Platforms" | cosmetic
c-block-u5-L4 | recap (14) | label "GHOST and side chains" runs past its card | cosmetic
c-block-u2-L2 | notebook (10) | repeats the six-item list of the scene before it word for word | cosmetic
c-block-u2-L2 | bookfig (11) | curve points faint grey; label backgrounds sit off their labels | cosmetic
c-block-u2-L2 | trap2 (14) | calculator shows 38.5 while the narration says 38 | cosmetic
c-block-u2-L1 | bookfig (13) | genesis block shows "prev: none"; elsewhere it is "32 zero bytes" | cosmetic
c-block-u3-L1 | calc (6), pa (18) | hops counted 1/2/3 in the worked example but round 0/1 in the Q2 answer | cosmetic
c-block-u4-L1 | notebook (3, 6), calc (9, 11) | 1 BTC written 10,00,00,000 sat (Indian grouping) in two scenes and 100,000,000 sat in two others | cosmetic
c-block-u1-L1, u4-L1 | hookArt (0) | same hook in both (photo sent to two friends as the double-spend story) | cosmetic
c-block-u2-L1, u2-L2 | notebook (5), (9) | "don't wait up" line repeated | cosmetic
c-block-u2-L3, u4-L1 | notebook (11), (3) | "there is no forgot password button" repeated | cosmetic
c-block-u5-L2 | hookArt (0) | opens on "Imagine …" | cosmetic
c-block-u5-L3 | pq (17) | "Give Alice balance, Bob balance": reads as a machine-made sentence | cosmetic
c-block-u2-L3 | bookfig (3) | split crop leaves the figure's boxes open at the bottom | cosmetic

Not slop (checked): "unlock(s)" (Bitcoin locking and unlocking scripts), "robust", "Site 1 / Site 2" (bank branches in a
story), "bloom" (the receipt's bloom filter). Same patterns as the other subjects (book wording, unit numbers in outros,
spoken Bloom, stock recap icons, generator lines on every lesson). New here: dated facts stated as current (pre-Merge
miners, uncles and PoW geth private nets in Ethereum; the pre-2010 joined-script model in Bitcoin), recap pictures that
show a state the lesson says can't exist (stacks), a code snippet missing a declaration, one symbol (k) reused for two
things, and a trap whose wrong answer isn't what the stated mistake produces.

## Computer Graphics (17 Nov)

Audited 17 Nov 2026: all 23 c-graphics lessons (06_Deliver/cse/c-graphics), every scene, narration and frame (sheets at
0.92; the frames that looked cut off, u2-L4 L05, u4-L1 L11 and u6-L2 L11, re-rendered at 0.995: the first two were typing
animations and render whole). Checker: 0 page errors, 0 cue failures, 0 text outside the safe area on every sheet. Every
worked example and model answer recomputed (frame-buffer and data rates, dpi/ppi, Bresenham and midpoint-circle traces,
scan-line spans, RGB→CMY→HSV, every 2D/3D matrix product, window-to-viewport, Cohen–Sutherland codes and Liang–Barsky u1/u2,
Sutherland–Hodgman lists, perspective divide, cross-product plane, sphere expansion, blob field, Bezier/de Casteljau, knot
counts, Phong sum, ray–sphere roots, raw media sizes, Huffman 224 bits, MP4/DVD sizes, motion-vector bits, skew, squash
volume, tweens, morph, composite alpha, motion blur, link capacity, L1/precision/recall, jitter, segments, U and the RM
bound, camera storage, LSB/PSNR). All 47 exam traps checked. Scene = 0-based SC index (the Lnn.png number).
No filler word, site/finder line, college name, TODO, placeholder, "your book" or repeated non-template sentence found.

lesson | scene | what's wrong | severity
--- | --- | --- | ---
c-graphics-u6-L4 | bookfig (3), calc (5), trap2 (6) | says "so RM fails" and "only EDF guarantees every deadline" for 4/10, 10/40, 5/20 (U = 0.90 > 0.7798). The periods 10, 20, 40 are harmonic, so RM schedules them up to U = 1 (response times 4, 9, 36 ms, all in time); above the Liu–Layland bound the test is only inconclusive. The trap's "Don't write: U ≤ 1, so RM meets every deadline" is true for this very task set | wrong fact: must fix
c-graphics-u6-L3 | notebook (8), calc (9), recap (18) | a leaky bucket that "drains at one fixed rate" is given a burst: "largest release over 0.5 s = r × T + b = 1,008,000 bits, 2.016 Mbit/s, just above r". A fixed-rate leaky bucket releases at most r × T (1,000,000 bits); r × T + b is the token-bucket bound. Contradicts the lesson's own Q3 answer (24: a leaky bucket allows no burst) | wrong fact: must fix
c-graphics-u1-L2 | bookfig (15), calc (17) | "The vertex shader scales each corner by two hundred, so the triangle lands at (0,0), (200,0), (0,200)": the shader outputs clip coordinates (−1 to 1); the move to window pixels is the fixed viewport transform after it | misleading: should fix
c-graphics-u2-L1 | trap2 (13) | marks [1 0 0; 0 1 0; tx ty 1] as wrong ("W′ is no longer one, the point is distorted"). That is the right matrix in the row-vector convention (P′ = P·T) that many syllabus books use; say "with column vectors, P′ = T·P" | misleading: should fix
c-graphics-u3-L3 | bookfig (15) | Figure 3.8.1: the eye ray meets the sphere head-on along its normal (d = (0,0,−1) at (0,0,−4)), yet the reflected ray is drawn leaving up-left and the refracted ray bending up-right; at normal incidence both go straight (back to the eye, and straight through) | misleading: should fix
c-graphics-u5-L1 | pq (20), pa (21) | Q3 gives no data ("an equal-step line and a slow-in curve"), but the answer quotes y = x²/12 and "0.25 units from frame 1 to 2" from a graph the question never shows; also calls a slow start "slow-in" (the principle "slow in" means slowing into a pose; the lesson itself calls a slow start ease-in) | misleading: should fix
c-graphics-u5-L3 | calc (11, 12) | hint "dpi is pixels per inch" contradicts u1-L1 Q1 (dpi = printer dots, ppi = image pixels); should say ppi | misleading: should fix
c-graphics-u5-L3 | bookfig (10) | figure text "4 × 300 = 1200 × 1200 px" and "4 × 150 = 600 × 600 px": false equalities on screen | misleading: should fix
c-graphics-u5-L4 | bookfig (3) | Figure 5.7.1 colours contradict the numbers: "blue fill (0, 0, 255)" drawn pale lavender, "background (200, 100, 50)" (orange-brown) drawn pale green; no swatch of the result (160, 80, 91) | misleading: should fix
c-graphics-u6-L2 | bookfig (11) | narration "Unit six leads down to Notes", but Notes is not drawn: the arrow from Unit6 ends in empty space (Notes only appears on the next scene); still missing at 0.995 | misleading: should fix
c-graphics-u6-L3 | trap2 (10) | "Don't write: Jitter = d max − d min": peak-to-peak delay variation is a standard jitter measure; the lesson's mean |d − d̄| is one definition. Say "here jitter means …; d max − d min is the spread" | misleading: should fix
c-graphics-u1-L1, u1-L2, u2-L2, u2-L3, u4-L1, u4-L2, u4-L3, u4-L4, u6-L2, u6-L3, u6-L4 | pq (each lesson's three questions, e.g. u1-L1 17/19/21) | spoken Bloom levels: "An understand question", "Question two, apply", "at the apply level", "an analyze question" (33 lines in 11 lessons) | should fix
c-graphics-u1-L4, u2-L4, u3-L3, u4-L4, u5-L4 | outro (23, 20, 27, 25, 25) | "Next time, Unit two/three/four/five/six" spoken; "NEXT UNIT, Unit N" card (book2lesson.py writes both) | should fix
c-graphics-u4-L1, u5-L2 | outro (26, 22) | next-lesson card cut at a comma: "Multimedia hardware and software · Image" (chapter "Image, graphics and animation file formats"), "Authoring metaphors and tools · Painting" (book2lesson.py splits titles on [:;,]) | cosmetic
c-graphics-u1-L1, u3-L1, u4-L3, u6-L4 | pq/pa (19, 20), notebook/calc (14, 16), pq/pa (20, 21), bookfig/calc (3, 5) | caret maths on screen: "1 MB = 10^6 bytes" (u1-L1, u4-L3), "e^(−d²)", "e^(−4)", "Σ e^(−|p − cᵢ|²)" (u3-L1), "3(2^(1/3) − 1)", "n(2^(1/n) − 1)" (u6-L4) | cosmetic
c-graphics-u1-L1, u1-L2, u1-L4, u3-L1, u3-L2, u4-L1, u4-L2, u4-L3, u5-L2, u5-L3, u6-L3, u6-L4 | figs (second to last) | "Sources the book draws on: …" shown (the other 11 say "the notes") | cosmetic
c-graphics-u4-L4 | recap (17) | stock pictures: plain film strip for Compression (no vector or residual), pale grey CD for MPEG family, clock for Sync | cosmetic
c-graphics-u6-L4 | recap (17) | stock clock for "OS support", stock padlock for "Security" (the lesson has a CPU-share bar and LSB bits to draw) | cosmetic
c-graphics-u6-L3 | recap (18) | "Four numbers" picture is two blank rectangles, a small clock and an X | cosmetic
c-graphics-u6-L2 | recap (15) | tiny, faint pictures: two pale boxes for "Hypermedia links", three pale dots for "Two rules" | cosmetic
c-graphics-u6-L1 | recap (17) | "Key numbers" picture is a small pale bar labelled "÷ (1 + o)" while the card says "rate × (1 + o)" | cosmetic
c-graphics-u1-L3 | bookfig (9), calc (11, 12) | "seven pixels in the octant" counts (6, 5), which lies past y = x (the mirror of (5, 6)); the first octant is (0,8) to (5,6), six pixels | cosmetic
c-graphics-u4-L2, u6-L3 | bookfig (4, 4) | figure split over two scenes leaves orphans: "× 7,200 s = 1.3824 GB" with its audio label on the other half (u4-L2); dashed lines leading to a play row drawn only three scenes later (u6-L3) | cosmetic
c-graphics-u2-L4 | notebook (9) | "View matrix: eye at the origin, looking along +z" with no word that OpenGL looks along −z | cosmetic
c-graphics-u2-L2, u3-L1, u5-L2, u5-L4 | bookfig (9), bookfig (13), bookfig (9), hookArt (0) | same joke twice: "elevator" (u2-L2, u3-L1), "before lunch" (u5-L2, u5-L4) | cosmetic
all 23 (engine) | every scene header | "UNIT n · LESSON x OF y" shown on every page (decide whether the unit-number rule covers the header) | cosmetic
all 23 (engine) | pq, pa | on-screen label "QUESTION n · UNDERSTAND / APPLY / ANALYZE" (decide whether the Bloom rule covers labels) | cosmetic

Not slop (checked): "site" and "Unit6" in u6-L2 are the hypermedia example's own page names; "robust" in u6-L4 is the
watermarking term; "elevator" is a joke, not filler. YouTube: pipeline.json has live: false for all six units and every
publish field in upload_sheet.json is empty, so none of the 23 is on YouTube. Same patterns as the other subjects (book
wording, unit numbers in outros, spoken Bloom, caret maths, stock and faint recap pictures). New here: a scheduling claim
that ignores harmonic periods, a leaky bucket given the token bucket's formula, figures whose drawn geometry or colours
contradict their own numbers, next-lesson titles cut at a comma by the generator, and convention-dependent traps (row vs
column vectors, jitter definition) stated as absolute.

## Object Oriented Programming (17 Nov)

Audited 17 Nov 2026: all 23 c-oop lessons (6 units, 544 scenes, built 17 Nov; the delivered copies in
06_Deliver/cse/c-oop are byte-identical to the audited ones). Each lesson's SC array was dumped with Playwright and every
scene's narration and screen text was read. Sheets were rendered at 0.92, and at 0.995 for every frame that looked cut. All
lines that looked cut at 0.92 were typing animations and render whole at 0.995. Checker: 0 page errors, 0 cue failures and
0 text outside the safe area on every sheet. Every worked example, model answer and trap was recomputed, and the C++ outputs
were re-run with g++ (setw/setfill/setprecision, the overflow and modulo lines, the fstream trace, what() overrides).
None is on YouTube yet (pipeline.json: every unit "live": false).

c-oop-u6-L1 | bookfig (10) | narration says ios::in|ios::ate lets you "seek back and write anywhere", but in|ate opens read-only and every write fails (g++: put() after seekp sets failbit). Writing needs in|out|ate | must fix
c-oop-u6-L3 | bookfig (14) | "The hollow diamond means any number of them": the hollow diamond means aggregation, and the 0..* multiplicity means "any number" | must fix
c-oop-u2-L4, u3-L4, u5-L1, u6-L3 | agenda (1) | star "Chapters x to y of your book" | should fix
c-oop-u4-L2 | agenda (1) | star "Chapters 4.3 to 4.4 of your notes" (missing "free") | should fix
c-oop-u5-L3 | bookfig (3, 10) | spoken "Your book's figure." | should fix
c-oop-u1-L4, u2-L4, u3-L4, u4-L4, u5-L4 | outro (23, 22, 26, 20, 26) | "Next time, Unit two/three/four/five/six" spoken; "NEXT UNIT, Unit N" card | should fix
c-oop-u2-L1 | bookfig (8) | "class Topper : public Student (derived, Unit 3)" on screen | should fix
c-oop-u3-L3 | notebook (5), pa (20) | "(Unit 4)" on screen twice | should fix
c-oop-u4-L1 | bookfig (3) | "Templates · Unit 5", "Overriding (Java) · Unit 3" in the figure | should fix
c-oop-u2-L1, u2-L2, u3-L1, u3-L3, u4-L2, u6-L3 | pq (u2-L1 13/15/17; u2-L2 15/17/19; u3-L1 17/19/21; u3-L3 15/17/19; u4-L2 14/16/18; u6-L3 19/21/23) | spoken Bloom levels: "at the understand/apply/analyze level", "An understand question", "Question two, apply", "Question three, analyze" (18 lines) | should fix
c-oop-u2-L2 | trap2 (7) | narration opens "Don't write that c equals b calls the copy constructor", then says "Box c equals b … the copy constructor runs": reads as a contradiction until the last sentence | should fix
all 23 | figs (second to last) | "Sources the book draws on: …" shown | cosmetic
all 23 (engine) | every scene header | "UNIT n · LESSON x OF y" on every page (same open question as Linux) | cosmetic
all 23 (engine) | pq, pa | on-screen "QUESTION n · UNDERSTAND / APPLY / ANALYZE" label (same open question as Linux) | cosmetic
c-oop-u1-L3 | figs (22) | note "(control structures and pointers in the same order as this unit.)": unit wording and a stray full stop | cosmetic
c-oop-u5-L1 | figs (21) | note calls Balagurusamy "the usual Indian text": regional claim | cosmetic
c-oop-u3-L4 | recap (18) | "Has-a" picture draws a plain line and a filled diamond, but the card text is "Hollow ◇ … Filled ◆": no hollow diamond drawn | cosmetic
c-oop-u4-L3 | bookfig (4) | the "p->area(): follow p …" callout runs past the bottom of its panel (still cut at 0.995) | cosmetic
c-oop-u1-L2 | pq, pa (20, 21) | "IRCTC booking" on screen: a real organisation's name (the voice says "train booking") | cosmetic
c-oop-u6-L1 | hookArt (0) | ends "Let's take control." | cosmetic

Not slop (checked): "super" (the Java keyword, 60 hits), "just" and "really" in ordinary use, "bits"; Chennai, Delhi, Pune
and Agra (city names in worked examples, not colleges); "null" and "undefined behaviour" (C++ terms); the one caret
(u1-L2 scene 13 "^ 11" is the XOR operator, and the result is right). None of the listed filler words appear (delve,
journey, unlock, crucial, essentially, imagine, amazing). No site or finder line, no TODO or placeholder, no college names.
No sentence repeats across lessons beyond the template lines ("See you there", the agenda count line, "Your free notes
are linked …"). Facts: every number, output, truth claim and trap checks out apart from the two must-fix lines above.
No stock recap icons (shield, refresh arrow, stopwatch, up arrow) and no tiny or faint pictures. Patterns shared with the
other subjects: book wording, unit numbers in outros and cross-references, spoken Bloom levels, and the generator's
"Sources the book draws on" line. New here: unit numbers inside figures and on-screen cross-references ("(Unit 4)"),
and a narration sentence that names the wrong UML symbol for a multiplicity.

## Digital Logic Design (17 Nov)

Audited 17 Nov 2026: all 22 c-digital lessons (518 scenes), every scene, narration and frame (sheets at 0.92 and re-rendered
at 0.995; the cut-off lines at 0.92 in u2-L1 sc4 and u2-L4 sc9 were typing animations and render whole at 0.995). Checker:
0 page errors, 0 cue failures, 0 text outside the safe area on every sheet. None is on YouTube yet (videos.c-digital-uN.json:
every "video" field empty). Every number, base conversion, complement, IEEE 754 encoding, truth table, K-map, QM chart, adder,
CLA, BCD adder, comparator, MUX table, FSM table, counter sequence, flip-flop conversion, memory sizing, LUT, CMOS power,
fan-out, noise margin, DAC/ADC and SAR value was recomputed (mostly in Python); the Verilog was traced by hand (no simulator
installed). Two wrong facts survived.

c-digital-u2-L3 | notebook (6) | SOP B′D′ + B′C′ + A′C′D called "8 literals"; it has 7 (2 + 2 + 3); the POS map caption repeats "6 literals, against 8" (from book 2.5) | wrong fact: must fix
c-digital-u3-L2 | trap2 (11) | dropping K "makes 9 + 9 read digit two with a carry: twelve" and the display shows 12; without K, C = 0 and the second adder's carry-out is unused, so it reads 02 with no carry | wrong fact: must fix
c-digital-u2-L1 | notebook (11) | "the complement of G": G = A(B′C + BC′) is never shown before G′ = A′ + BC + B′C′ | misleading: should fix
c-digital-u2-L2 | notebook (5) | prime-detector braces span rows 4–6 for AC′ and 5–7 for AC, so each covers a row its term doesn't (AC′ is rows 4, 6; AC is rows 5, 7): picture contradicts the narration | misleading: should fix
c-digital-u4-L1 | notebook (5) | text says "Z = Q" but the table's Z column copies Q⁺ (1, 0, 0, 1), not the present-state Q column (0, 1, 0, 0) | misleading: should fix
c-digital-u4-L3 | calc (6) | "On a warm day, dt is seven": heat raises gate delay, it doesn't lower it (same wording in book 4.5) | misleading: should fix
c-digital-u5-L4 | pq/pa (15, 16) | Q2 says the table "has rows 00 and 11 only", then lists rows 01 and 10 | misleading: should fix
c-digital-u6-L2 | calc (13, 14) | question board lists only the currents; the 11 ns gate delay, 15 ns clock-to-Q and 20 ns setup used later appear from nowhere (the book gives them) | misleading: should fix
c-digital-u6-L3 | bookfig (9) | R-2R figure has no bit switches, no op-amp + input and no Rf, while the narration says each bit switch ties its leg to the reference and the figure shows V_out = −I·R_f (book fig 6.7.1 also lacks Rf) | misleading: should fix
c-digital-u2-L1, u2-L2, u3-L3, u4-L1, u4-L2, u5-L1, u5-L3, u6-L2 | agenda (1); bookfig (u3-L3 3, u5-L3 3) | "Chapters x to y of your book" on the agenda; spoken "the figure from your book", "Your book's Mealy detector" (must be "your free notes") | misleading: should fix
c-digital-u1-L1, u1-L2, u3-L1 | pq (u1-L1 15/17/19; u1-L2 17/19/21; u3-L1 15/17/19) | spoken Bloom levels: "An understand / apply / analyze question", "Question two, at the apply level", "Question three, analyze" (9 lines) | should fix
c-digital-u1-L3, u2-L4, u3-L4, u4-L4, u5-L4 | outro (22, 22, 25, 28, 20) | "Next time, Unit two/three/four/five/six" spoken; "NEXT UNIT, Unit N" card (book2lesson.py line 548) | should fix
c-digital-u4-L2 | part (8) | "this unit" in the narration | should fix
all 22 | figs (second to last) | "Sources the book draws on: …" shown (book2lesson.py lines 433/436); u2-L2 (20) and u2-L3 (23) notes also say "this unit" | cosmetic
all 22 (generator) | every scene header | "UNIT n · LESSON k OF K" kicker on every page (book2lesson.py line 358) | cosmetic
all 22 (engine) | pq, pa | on-screen "QUESTION n · UNDERSTAND / APPLY / ANALYZE" label | cosmetic
c-digital-u1-L2, u5-L1 | calc (12, 13), notebook (3) | caret maths on screen: "2^(e − 127)", "2^(m+n)" | cosmetic
c-digital-u1-L3, u3-L1, u3-L4, u4-L4, u5-L1, u5-L2, u6-L2, u6-L3 | u1-L3 10; u3-L1 8; u3-L4 3; u4-L4 5, 6, 7, 17, 18; u5-L1 5; u5-L2 4, 5, 6, 11, 13; u6-L2 3, 4, 11, 12; u6-L3 9, 10 | underscore subscripts on screen (t_cq, f_max, V_out, D_A, C_in, d_min, NM_H …) instead of real subscripts | cosmetic
c-digital-u5-L2 | recap (13) | stock icons: network graph for "Design", refresh arrows for "Reduction", stopwatch for "Timing" | cosmetic
c-digital-u2-L3 | recap (16) | plain green check mark for "The cover" | cosmetic
c-digital-u1-L2 | recap (16) | tiny 4-bit boxes and a faint float bar; "SUBTRACT BY ADDING" tab runs past its card into the IEEE tab (confirmed at 0.995) | cosmetic
c-digital-u2-L2 | recap (13) | truth-table picture too small to read | cosmetic
c-digital-u6-L1 | recap (17) | bare decoder lines and small AND/OR boxes: faint, says little | cosmetic
c-digital-u3-L2 | bookfig (8) | Z wire runs through the "adds 0 C C 0" label (confirmed at 0.995) | cosmetic
c-digital-u4-L3 | hookArt (0) | opens on "Imagine …" | cosmetic
c-digital-u3-L3 | outro (22) | narration promises "decoders, encoders and priority encoders"; the next card says "Decoders · Code converters and seven-segment" | cosmetic
c-digital-u5-L3 | outro (22) | narration promises "flow tables, races, cycles and race-free assignment"; the next card says "Flow tables · Hazards" | cosmetic

Not slop (checked): no college names, TODO, placeholder or site/finder lines; "undefined" (u6-L2) is the TTL undefined
band; "essential" is essential prime implicants and essential hazards; no repeated sentences beyond the template lines;
"<" and "<=" in u3-L3 Q3 and the u6-L3 Verilog are real operators. Same patterns as the other subjects (book wording,
unit numbers in outros, spoken Bloom, generator lines on every lesson, stock recap icons). New here: errors carried
straight from the unit book (literal count, warm-day delay, R-2R figure without Rf), so the book needs the same fix as
the lesson; pictures that disagree with their own table (braces over the wrong rows, Z copied from the wrong column);
calc boards that hide givens used later; trap answers that don't follow from the stated mistake; outro promises that
don't match the next lesson's card; ASCII maths (^, _) on screen.
