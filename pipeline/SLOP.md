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
