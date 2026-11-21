# Lesson slop found in the AI lessons (17 Nov 2026), to fix later with rules and fix threads

## Proposed rules (synthesis of the 17 and 18 Nov audits)

Status: Swathish approved this list on 17 Nov with changes: fix the 17 Nov must-fix facts first (done, see the fix log in
the thread); make recap built-in icons, mixed number grouping and filler "imagine" warnings, and keep hard failures for
book wording, unit numbers, Bloom words, carets/underscores and site/finder lines; D approved (no unit or lesson number in
the kicker, no Bloom word on the question card); add a fact-review step to the subject pipeline. The 18 Nov findings are
counted below but their fixes are not approved yet.

Scope: 16 CSE subjects, 337 lessons. 17 Nov: OOP 23, Digital Logic 22, Computer Fundamentals 16, Quantum 20, Parallel and
Distributed 21, Mobile 17, AR/VR 21, NLP 27, Linux 16, Blockchain 20, Computer Graphics 23 (226). 18 Nov: Theory of
Computation 21, Machine Learning 19, Software Engineering 23, Web Technologies 23, and a second full pass of Data Structures 25
(111; DS counts merge its 17 and 18 Nov rows). AI (22, first audit) is still given in brackets only. Counts are the lessons
named in each subject's rows below (recounted from the sections, not re-audited); "17 Nov n, 18 Nov m" splits each total.
Must-fix wrong facts: 31 (17 Nov 21, fixed; 18 Nov 10: Web 4, TOC 3, DS 1, ML 1, SE 1, not yet approved), at least one in
every subject. Code refs are to pipeline/lessons/engine/ as it is in this repo (book2lesson.py, lesson_build.py,
lesson_template.html) and pipeline/lessons/sample/WRITE.md.

Note on WRITE.md: it already says "your free notes", never "unit book" (WRITE.md:12), and US spellings in say (:39). Both
were broken anyway, so every text rule below is a checker rule; WRITE.md gets a line only so writers know why a build fails.

How the checker text rules should run: on every `say`, and on the rendered SVG text of each scene's last frame (the
checker already renders every scene), not only on SC strings. NLP found on-screen text drawn by a lesson's own art code
("the book's order", u7-L3) that an SC-only scan misses. Exempt code scenes (codeBoard, cfCode, code spans) from the maths
and filler rules, and give each lesson an allow list (META.allow) for content words: "booking site", "Site 1", "ticket
site", "the developer's site", "book a ticket", "unlock" in Bitcoin scripts and spinlocks, "book → back" in NLP edit
distance, "university" as a stemming example.

### A. Text the checker can fail automatically

pattern | subjects | lessons hit | rule that prevents it | where
--- | --- | --- | --- | ---
"Sources the book draws on: …" on the notes page | 16 of 16 | 317 of 337 (17 Nov 206 of 226; 18 Nov all 111) | generator writes "Sources your free notes draw on: …" (book2lesson.py:389); checker fails on `\b(your\|the\|unit) book('s)?\b` | generator + checker
"book" wording elsewhere: agenda star "Chapters x to y of your book" or "of your notes" without "free"; spoken "the book's figure / example / model" | 14 (all but Mobile, Graphics) | 107 (17 Nov 55: Linux 10, CFP 10, Digital 8, PDC 6, OOP 6, AR/VR 4, Blockchain 4, NLP 4, Quantum 3; 18 Nov 52: SE 17, Web 13, DS 12, TOC 9, ML 1) [AI 6] | generator writes "of your free notes" (book2lesson.py:324); checker fails on the book regex above and on "your notes" not preceded by "free" | generator + checker
Spoken Bloom levels in exam practice: "An understand question", "at the apply level", and the second form "Question two, apply." | 15 (all but ML) | 110 lessons, 330 lines (17 Nov 83 / 249: AR/VR 15, Mobile 12, Graphics 11, CFP 8, Quantum 7, Linux 6, PDC 6, Blockchain 6, OOP 6, Digital 3, NLP 3; 18 Nov 27 / 81: SE 10, Web 9, DS 6, TOC 2) [AI 4] | checker fails a pq/pa `say` matching `\ban? (remember\|understand\|apply\|analy[sz]e\|evaluate\|create) question\b`, `\bat the \w+ level\b` or `\bquestion (one\|two\|three)[,.]? (an? \|at the )?(remember\|understand\|apply\|analy[sz]e)\b`; WRITE.md: say only "Question one / two / three" | checker
Unit numbers in the outro: "Next time, Unit two: …" and the "NEXT UNIT / Unit N" card | 16 of 16 | 80 (5 in each subject; Linux 4, NLP 6) | generator puts the next unit's topic on the card and in the line, never "Unit N" (book2lesson.py:501 and the say template at :392/:505); checker fails on `\bunit (one\|two\|…\|ten\|\d+)\b` in say and on screen | generator + checker
Other unit references: "(Unit 4)" cross-references in figures and answers, "this unit", "All six units" or "COURSE COMPLETE · Units 1 to 6" on the last card; section numbers "(3.6)" on screen | 14 (not Linux, Graphics) | 24 (17 Nov 17: OOP 4, Digital 3, Quantum 2, PDC 2, NLP 2, CFP 1, Mobile 1, AR/VR 1, Blockchain 1; 18 Nov 7: DS 2, TOC 2, ML 1, SE 1, Web 1) [AI] | same checker regex plus `\bthis unit\b`, `\bnext unit\b`, `\ball \w+ units\b`, `\bunits \d+ to \d+\b`; warn on a bare `\(\d\.\d{1,2}\)` outside maths; WRITE.md: name the topic ("in the lesson on phase estimation") | checker
Site or finder line: "Find this unit in your own syllabus on the University free n easy site" (no such site yet) | 4 (DS, Web, TOC; AI) | 3 (DS u6-L5, Web u6-L4, TOC u6-L4) [AI 2] | generator writes no site line in the last outro; checker fails on `\b(find (this\|your)\b.*syllabus\|on (the\|our) (university free n easy )?site)\b` until META.site is set | generator + checker
ASCII maths on screen: caret (`2^(e − 127)`, `e^(iθ)`) and underscore subscripts (`ρ_A`, `t_cq`, `S_W`, `q_accept`) | 11 (Quantum, Digital, Graphics, CFP, Mobile, AR/VR, NLP, ML, TOC, SE, DS) | 48 (17 Nov 31: caret 19 in 7 subjects, underscore 17 in Quantum and Digital; 18 Nov 17: ML 9, TOC 6, SE 1, DS 1) [AI 2] | checker fails on-screen text matching `[\w)]\^[\w(−-]` or `[A-Za-zα-ω]_[A-Za-z0-9{]` outside code (keeps OOP's XOR `^` and C names); WRITE.md: Unicode ² ⁻¹ ₐ or a sup/sub tspan | checker (an engine sup/sub helper would make the fix easy)
Filler: "Imagine …", "amazing", "Let's take control", "a whole journey" | 7 (CFP, AR/VR, PDC, Blockchain, OOP, Digital, SE) | 7 (18 Nov: SE 1) | checker word list on say and screen text: delve, journey, unlock, crucial, essentially, amazing, dive into, let's take control fail; "imagine" warns (approved change); allow list for real terms | checker
Repeats across one subject's lessons: the same hook story, joke, trap or exam question twice (near word for word, so the exact-sentence scan missed them) | 8 (Mobile, PDC, Blockchain, Graphics, ML, SE, Web, DS) | 35 (17 Nov 15: Blockchain 5, Mobile 4, Graphics 4, PDC 2; 18 Nov 20: ML 9 (three spam hooks, four shop hooks, one joke twice), SE 5, Web 4, DS 2) | new subject-level check, `lesson_build.py --check-set <html folder>`: fail when two hooks share 60% or more of their content words, two trap2 scenes share a Write line, two pq lines match, or a joke repeats | checker
Two number conventions in one lesson (1 KB = 1024 and 1 MB = 10⁶; 10,00,00,000 sat and 100,000,000 sat; dpi called pixels per inch) | 3 (Mobile, Blockchain, Graphics) | 3 (none on 18 Nov) | checker warns (approved change) on a lesson that shows both Indian (`\d{1,2},\d{2},\d{3}`) and Western grouping; WRITE.md: state the KB/MB convention once on screen | checker
META.subject is "biotech" on CSE lessons | 7 flagged (Mobile, AR/VR, DS, Web, ML, TOC, SE) | 149 flagged (17 Nov 38, 18 Nov 111); every lesson built without --subject has it | generator: --subject required, no default (book2lesson.py:485); checker fails when META.subject doesn't match the lesson's department | generator + checker
Next-lesson card cut at the first comma ("Multimedia hardware and software · Image"), so the card no longer matches what the outro promises | 6 (Mobile, Graphics, Digital, SE, Web, DS) | 12 (17 Nov 5: Graphics 2, Digital 2, Mobile 1; 18 Nov 7: SE 4, Web 2, DS 1) | generator splits titles on ":" only, not "[:;,]" (book2lesson.py:498, also :276), and lists every chapter of the next lesson; checker fails when the card's title is not a whole chapter title from the book | generator + checker

### B. Pictures and layout (checker measures, engine prevents)

pattern | subjects | lessons hit | rule that prevents it | where
--- | --- | --- | --- | ---
Stock or generic recap icons that don't match their card (shield, refresh arrow, stopwatch, up arrow, clock, padlock, tick, network graph, document, gauge, gear) | 11 (not AR/VR, OOP, Web, ML, TOC) | 35 (17 Nov 25: Linux 5, PDC 5, Blockchain 3, Graphics 3, NLP 3, Quantum 2, Digital 2, CFP 1, Mobile 1; 18 Nov 10: SE 7, DS 3) [AI 2] | the generator's recap template asks for `'TODO icon'` (book2lesson.py:369), and the engine draws a name from its biotech icon set (lesson_template.html:588, icon() at :596). Generator asks for a lesson-drawn picture instead; checker warns (approved change) on a recap panel that uses a built-in ICON name unless META.allow lists it (AR/VR's stopwatch on a timing card was fine) | generator + checker
Tiny or faint pictures: recap pictures a tenth to a fifth of the card; bookfig halves that are a thin strip on an empty stage; split figures with orphan arrows or missing labels | 12 (17 Nov 9; ML, SE, TOC) | 55 (17 Nov 32: tiny recap 12, small or split bookfig 20; 18 Nov 23: ML 14, SE 8, TOC 1) [AI 2] | checker measures the ink box of each recap picture (fail under 35% of the picture area) and of each bookfig scene (fail under half the stage, or any shape cut by the view); generator splits a figure only between steps whose halves each keep their labels | checker + generator
Text that overflows its card or overlaps a line, still there at 0.995 (recap header pills wider than the card, labels past their card, lines through labels, values on ticks) | 8 (Quantum, AR/VR, PDC, Blockchain, OOP, Digital, ML, SE) | 22 (17 Nov 14; 18 Nov 8: ML 4, SE 4) | checker, at the last frame of every scene at 0.995: each text box inside its panel, no two text boxes intersect, warn when a stroke crosses text; engine fits the recap capbox font to the card width (fit() already does this for card lines) | checker + engine
Picture contradicts the narration or its own numbers (stack after ADD shows three items, braces over the wrong rows, colours that don't match the RGB values, a numbered cycle in the wrong order, a complete DFA with a missing edge, unnamed DFD flows the narration calls named) | 13 (not Quantum, AR/VR, DS) | 25 (17 Nov 17; 18 Nov 8: ML 2, TOC 2, SE 2, Web 2) | not checkable by script. WRITE.md: draw the end state the line states, in the colours the numbers give; the fact review (step 4) looks at every sheet | WRITE.md + fact review

### C. Facts (writer brief and a fact review; a script can't catch these)

pattern | subjects | lessons hit | rule that prevents it | where
--- | --- | --- | --- | ---
Lesson contradicts itself or hides its givens: an answer uses data the question never shows, the exam switches to a different corpus, grammar or machine from the worked example, two scenes or two lessons give different values or rules | 14 (not AR/VR, OOP) | 39 (17 Nov 23; 18 Nov 16: ML 5, SE 4, DS 3, TOC 2, Web 2) | WRITE.md: every pq shows all its givens; a pa uses only those and what the lesson showed; a question that reuses or changes the worked example's data says so | WRITE.md + fact review
Exam traps whose "Don't write" isn't wrong, whose stated wrong result isn't what the mistake produces, or that state one convention as the only one (row vs column vectors, jitter, deductible order, ½λw², UML sequence numbers) | 11 (17 Nov 8; Web, ML, SE) | 23 (17 Nov 15; 18 Nov 8: Web 3, ML 3, SE 2) | WRITE.md: recompute the wrong answer from the stated mistake; the Don't write must be false under every common convention, or the card names the convention. Generator marks book traps `src:'book'` so the checker can list writer-made traps for review | WRITE.md + generator + fact review
Dated, simplified or overstated facts stated as current: pre-Merge miners, GCC before 14, Linux 0.01 "under the GPL", React.createElement, *ngIf, the HTML outline, "sufficient" said as "when", a dropped "for every p", hierarchy without its conditions | 9 (Linux, CFP, Mobile, AR/VR, Blockchain, Web, TOC, SE, DS) | 19 (17 Nov 12; 18 Nov 7: Web 3, TOC 2, SE 1, DS 1) | WRITE.md: software, protocol and kernel behaviour names its version or era on screen ("since GCC 14", "since React 17", "before the Merge, 2022"); keep the book's own caveats ("simplified", "for every p") | WRITE.md + fact review
Errors inherited from the unit book | 5 (AR/VR, Digital, TOC, ML, DS) | 11 (17 Nov 6, fixed in the books; 18 Nov 5: TOC 3, ML 1, DS 1) | a fix thread that changes a fact or a bookfig also fixes the unit book and reruns pack/check_book.py; WRITE.md: a book error the writer spots goes in the hand-back, not into the narration | WRITE.md + the fix threads
Code on screen that wouldn't compile or run as shown, or whose shown output is not what it prints | 4 (CFP, Mobile, Blockchain, Web) | 6 (17 Nov 4; 18 Nov Web 2) | checker compiles every code board that names its language (gcc/g++ -fsyntax-only, javac, solc, others when installed; prints "skipped" if not) and fails on an error; a fragment is marked `frag:true`; WRITE.md: code panels are complete or marked as a fragment | checker

### D. Engine labels (approved 17 Nov)

The header kicker "UNIT n · LESSON k OF K" (written by book2lesson.py:316 as META.kick) and the question-card label
"QUESTION n · UNDERSTAND / APPLY / ANALYZE" (lesson_template.html:916 to 927) are on all 337 lessons; 11 subjects flagged
the header and 10 flagged the label. Approved: the kicker shows the subject and topic, with no unit or lesson number, and the
card shows "QUESTION n" only. The unit and Bloom regexes above also run on the kicker and the card labels.

### Seen in one subject only (no rule proposed)

"metres" in say (AR/VR, WRITE.md:39 already covers it); a real organisation's name on screen, "IRCTC" (OOP, and DS's
"IRCTCTRAINS", so this is now two subjects: add "IRCTC" to the checker word list); "the usual Indian text" (OOP); "Your
turn" with no pause before the answer (Quantum); a writer's "(from memory; check)" note on screen (Web); "Colours" on
cards under a "colors" title (Web); a sources line copied from another lesson (Web 2, TOC 1).

### On YouTube

AI and DBMS are on YouTube; neither is rebuilt. None of the 337 audited lessons is: every audited subject's pipeline.json has
live: false for every unit (Web has no pipeline.json), and the video link fields (upload_sheet.json or videos*.json) are
empty. So every fix can be made in place before upload, with no re-upload.

### Order (approved)

1. Fix the 17 Nov must-fix facts, in the lessons and the unit books (done).
2. Checker text rules (A), run on say and rendered text, since they fail the build by themselves.
3. Generator lines 316, 324, 369, 389, 485, 498, 501, with a rebuild of the generator's sample to confirm the checker passes.
4. Checker layout rules (B) and the engine capbox fit.
5. WRITE.md lines for C, and the trap and code rules; the fact-review step in the subject pipeline.

## Step 6: text rules on the earlier subjects (17 Nov, script only, report only)

The approved text rules (`lesson_build.py --check`, engine commit 5038bd3) run by script on every lesson source of the
subjects built before the 17 Nov audits: 13 CSE subjects and 3 Biotech subjects, 342 lessons (Microbiology's sources were
taken out of its built pages with lesson_extract.py). Each cell counts lessons with at least one hit. AI and DBMS are on
YouTube: reported only, never rebuilt. Nothing was changed.

subject | lessons | pass | sources line | other "book" | unit (outro) | unit (other) | Bloom said | site line | ^ or _ maths | warn: built-in icons | warn: mixed grouping | warn: filler
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
Artificial Intelligence (on YouTube) | 22 | 0 | 22 | 8 | 5 | 5 | 5 | 2 | 4 | 2 | 0 | 1
Algorithms | 25 | 1 | 21 | 13 | 6 | 2 | 6 | 0 | 4 | 2 | 0 | 0
Cloud Computing | 23 | 1 | 20 | 18 | 5 | 1 | 13 | 1 | 6 | 3 | 1 | 0
Computer Networks | 22 | 1 | 15 | 11 | 5 | 1 | 10 | 0 | 10 | 3 | 0 | 0
Computer Organization | 22 | 0 | 22 | 12 | 5 | 1 | 2 | 0 | 6 | 4 | 0 | 0
Compiler Design | 19 | 0 | 18 | 7 | 5 | 3 | 5 | 0 | 1 | 2 | 0 | 1
Computer Vision | 24 | 0 | 24 | 5 | 6 | 2 | 23 | 0 | 11 | 1 | 0 | 0
Data Science | 21 | 2 | 14 | 9 | 5 | 2 | 8 | 0 | 6 | 0 | 1 | 0
DBMS (on YouTube) | 23 | 0 | 23 | 15 | 5 | 2 | 17 | 0 | 1 | 3 | 0 | 2
Deep Learning | 21 | 0 | 21 | 18 | 5 | 1 | 13 | 0 | 13 | 1 | 0 | 3
IoT | 19 | 0 | 17 | 12 | 5 | 1 | 13 | 0 | 12 | 0 | 1 | 0
Operating Systems | 23 | 0 | 21 | 12 | 5 | 1 | 10 | 2 | 5 | 5 | 0 | 1
Security | 22 | 0 | 22 | 17 | 5 | 1 | 16 | 1 | 7 | 2 | 1 | 1
Biochemistry | 22 | 0 | 22 | 22 | 5 | 22 | 13 | 6 | 3 | 20 | 0 | 1
Cell Biology | 15 | 0 | 8 | 15 | 4 | 15 | 8 | 5 | 2 | 12 | 0 | 0
Microbiology | 19 | 0 | 12 | 19 | 5 | 19 | 11 | 6 | 5 | 12 | 0 | 0
**All** | **342** | **5** | **302** | **213** | **81** | **79** | **173** | **23** | **96** | **72** | **4** | **10**

Read with it:
- 5 of 342 lessons pass every failing rule. The sources line ("Sources the book draws on") alone is in 302; a fix in
  the generator and a scripted edit of each lesson's `figs` note clears it with no voice change.
- Other "book" wording (213 lessons) is mostly the agenda star "Chapters x to y of your book" (screen only), plus spoken
  lines such as "Your book's figure" and AI's "this book picks the rational agent".
- Unit numbers: 81 lessons have "Next time, Unit N" and the NEXT UNIT card in the outro. In Biotech every lesson also
  shows a "Biochemistry · Unit 4"-style label on its notes page (the "unit (other)" column).
- Bloom levels are spoken in 173 lessons ("An understand question", "Question three, analyze."). The engine's question
  card label and the "UNIT n · LESSON k OF K" kicker are on every built page as well; the new engine removes both on any
  rebuild, so they are not counted above.
- Site or finder lines: 23 lessons (AI 2, OS 2, Cloud 1, Security 1, Biotech 17).
- Caret or underscore maths on screen: 96 lessons (worst in Deep Learning 13, Computer Vision 11, IoT 12, Networks 10).
- Warnings: built-in recap icons in 72 lessons (44 of them Biotech, whose recaps were built on the stock set), mixed
  number grouping in 4, filler words in 10.
- Seen while making the notes PDFs: the PDFs carry the book's prerequisite boxes ("You need Unit 1, for where input sits
  among the components of a VR system"), so the notes still name unit numbers. make_site.py should drop or reword them.

Most of these hits are mechanical (sources line, agenda star, outro card and line, Bloom openers): the same script that
cleared the 25 rebuilt lessons (rules_fix: no new words beyond "Question one", "Next time:" and "from your free notes")
clears them, and `--revoice` voices only the changed lines (in the rebuild, 0 to 7 lines a lesson).

Rebuild of the 25 lessons not on YouTube (17 Nov): built with `--revoice`, then once more with `--reuse` for the final
header fit. All 25 pass `--check`; every sheet has 0 page errors, 0 cue failures, nothing outside the safe area, and the
play-through check passes. Re-voiced lines per lesson: 0 to 7 (68 in all). Layout warnings left are older design, not
rebuild damage: small recap pictures, book figures under half the stage, and text-over-text hits on hidden layers
(c-oop-u6-L1 scenes 13 and 17).

## Artificial Intelligence (17 Nov, first audit)

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

## Data Structures (18 Nov)

Second pass over the same 25 lessons (B.Tech/CSE/Data Structures/html, staged from the PC). It builds on the 17 Nov section
above: rows already listed there are not repeated, and lines added to a pattern the 17 Nov rows only partly covered say so.
Method: dumped every scene's say and the rendered text of its last frame at 0.995 (581 scenes), script-checked them for
book wording, site lines, unit numbers, Bloom words, caret or underscore maths, filler and repeats, ran lesson_sheet.py on
all 25 at 0.92 and 0.995 and looked at every sheet. Checker: 0 page errors, 0 cue failures, 0 text outside the safe area on
every lesson. Recomputed every trace and number again, by hand and in Python: addresses, step counts, Euclid, Θ constants,
recurrences (Hanoi, fib(40) calls, T(1024) = 11), sparse and fast transpose, array-list moves, Josephus (survivor 4),
polynomial add and R(2) = 68, first and best fit, every stack, queue, circular-queue and deque trace, infix to postfix and
prefix, postfix 52 and 9, tree counts, inorder traces, BST deletes, AVL RL (preorder 30 20 10 25 40 50), heap build,
deleteMin and insert 8, red-black inserts, B-tree order 3 and the 2-3 tree, CLRS t = 51 (4 reads), degrees, matrix vs list
memory (4 MB vs 168 KB), BFS/DFS, Kahn and DFS topological orders, components and cycles, Kruskal and Prim (21), Dijkstra
and Floyd-Warshall rounds, Bellman-Ford, binary search, the three simple sorts, merge sort (17 comparisons, 24 copies),
Lomuto, heap sort, Shell 11 vs 21 shifts, radix passes, log₂ n! (7 and 22), external sort k = 9, every hash and probe
(Knuth's 1.75, 2.5, 50.5, 10, 1.39), mod 13, 17011 prime, KMP lps [0,0,1,2,3,0] and [0,1,0,1,2,2,3] with 9 comparisons vs
13 naive, Boyer-Moore NEEDLE (shifts 5, 6, 4, found at 15, 10 comparisons, 16 of 24 never read), the trie (8 nodes + root).
The 17 Nov "facts: clean" no longer holds: the stack dry run below is wrong, and three statements are misleading.
Sheets: no overflow, overlap or faint picture; one more recap uses engine stock icons (u5-L4). Not on YouTube:
pipeline.json has live: false for all six units and the upload sheet has no video links.

lesson | scene | what's wrong | severity
--- | --- | --- | ---
c-ds-u3-L1 | notebook (11) | stack dry run, MAX = 4: after push 5, 8, 2, 9 and the overflowing push 4, it says and shows "pop, pop, peek, pop, pop print 9, 2, 8, 8, 5" and "The last pop finds top at minus one: underflow". Those five calls (four pops) empty the stack exactly, so nothing underflows. The book's question has a fifth pop (pop, pop, peek, pop, pop, pop); the lesson dropped it | wrong fact: must fix
c-ds-u6-L1 | bookfig (8), figs (19) | spoken and captioned "Only insertion sort does less work when the data is nearly sorted", against the same lesson's notebook (9) and trap2 (11): bubble sort with the swapped flag is O(n) on sorted input. The caption is the book's Figure 6.2.1, so the unit book needs the same fix | misleading: should fix
c-ds-u2-L3 | recap (14) | card "Keep tail: both ends O(1)": deleting the last node still walks to the node before tail, O(n), as the lesson's own notebook (11) says; only insert at both ends and delete at the front are O(1) | misleading: should fix
c-ds-u5-L3 | pa (16) | "When is the MST unique?" answered "When all the edge weights are distinct": that is sufficient, not necessary (a graph with tied weights can still have one MST). Say "It is unique if all weights are distinct" | misleading: should fix
c-ds-u4-L4, u4-L5, u5-L3 | calc (11), calc (6), bookfig (3) | spoken "Now the book's example", "Now the book's number", "Here is the book's figure" (adds 3 lessons to the 17 Nov book rows) | should fix
c-ds-u1-L3, u2-L4, u5-L2 | pq (18/20/22, 16/18/20, 15/17/19) | spoken Bloom levels: "An understand question", "An apply question", "An analyze question" | should fix
c-ds-u5-L1 | pq (15, 17, 19) | spoken Bloom levels: "An understand question", "Question two, apply level", "Question three, analyze level" | should fix
c-ds-u2-L3, u4-L2 | pq (15 / 13) | "An understand question" spoken; the 17 Nov row listed only their Question two and three lines | should fix
c-ds-u6-L5 | outro (24) | "That completes all six units" spoken and an "All six units" card title (unit reference; the 17 Nov row covers only the site and unit-book lines on this card) | should fix
c-ds-u3-L2, u4-L2 | hookArt (0) | same calculator hook twice, same picture: "2 + 3 × 4 gives 14, not 20" and "(2 + 3) × 4 = 20" | should fix
all 25 lessons | figs (19 to 26) | "Sources the book draws on: …" on screen | cosmetic
all 25 lessons | META | META.subject is "biotech" | cosmetic
c-ds-u2-L3, u4-L2 | agenda (1) | "Chapters x to y of your notes" without "free" | cosmetic
c-ds-u4-L5 | bookfig (12) | spoken "Your notes draw the same story" without "free" | cosmetic
c-ds-u5-L4 | recap (14) | engine stock icons: 'map' network on "Single-Source Shortest" and 'stop' red ✗ on "Negative Edges" | cosmetic
c-ds-u1-L1 | hookArt (0) | "To find the fortieth mark … forty pointer hops" with "Linked list: 40 pointer hops" on screen: the fortieth mark is index 39, so 39 hops; the lesson's own calc (6) uses roll 41 → index 40 → 40 links | cosmetic
c-ds-u1-L1 | outro (22) | next-lesson card "Static and dynamic memory allocation · Algorithms" leaves out the third chapter, time and space complexity, that Lesson 2 covers | cosmetic
c-ds-u1-L4, u2-L1, u2-L2 (hooks); u2-L4 hook, u3-L3 bookfig (4) (jokes) | hookArt (0), bookfig (4) | three hooks set in a cinema row (your row number; row six, seat twelve; a late friend wants the middle seat) and two cinema jokes ("booking a whole cinema for two friends", "a cinema turning you away from empty seats"): different stories, same setting | cosmetic
c-ds-u3-L2, u4-L2 | trap2 (13 / 11) | the same trap twice, "the first pop is the right operand / right child", also in both recaps and outros (the second is the tree form of the first, so it can stay if the lesson says so) | cosmetic
c-ds-u6-L5 | pa (18) | example text "IRCTCTRAINS" uses a real organisation's name (as OOP's IRCTC) | cosmetic

Count: 1 must fix, 9 should fix (3 misleading), 10 cosmetic (20 lines). With the 17 Nov rows, Data Structures has 1 must
fix, 15 should fix and 13 cosmetic. For the synthesis brackets: book wording DS 9 → 12 lessons (plus 25 sources lines),
spoken Bloom DS 2 → 6 lessons, unit references DS 1 → 2, stock recap icons DS 2 → 3, repeats DS 0 → 2 (calculator hook,
first-pop trap), META.subject DS 25. Patterns: one dropped step in a trace (the narration kept the book's ending), one
book caption that contradicts its own chapter, recap and model-answer wording that turns "only for insert" or
"sufficient" into "always".

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

## NLP (17 Nov)

Audited 17 Nov 2026: all 27 c-nlp lessons (B.Tech/CSE/Natural Language Processing/html), every scene, narration and frame
(sheets at 0.92; u6-L1 re-rendered at 0.995 where two number-line labels sat close: they render apart). Checker: 0 page
errors, 0 cue failures, 0 text outside the safe area on every sheet. Recomputed every worked example and model answer
(edit-distance tables cat→cart and book→back, DFA traces, token/type counts, Porter step 1a, FST counts, bigram MLE,
add-one, interpolation, perplexity, Brill net gain, Viterbi trellis, MEMM softmax, CRF Z, NER and relation P/R/F1,
leftmost derivations, CNF rule counts, CYK cells and split checks, PCFG tree products, UAS/LAS, chunk P/R/F1,
shift-reduce action counts, lexicalised ratio, model checks for ∀∃/∃∀, lambda order, path and Wu-Palmer similarity,
Lesk overlaps, MFS baseline, coreference link P/R/F1, TF-IDF matrix, Naive Bayes, spam metrics, lexicon score, cosines,
vector analogy, k-means, CNN filter, scalar RNN, attention with and without mask, scaled dot-product, temperature and
top-k, BLEU-2, EM/F1, TF-IDF ranking, AP, sample/byte/frame counts, mel values, MFCC rates, WER, unit-selection cost,
accuracy/UAR, F0 declination). All 54 exam traps checked. Scene = 0-based SC index (the Lnn.png number).
No filler word, college name, TODO, placeholder or repeated non-template sentence found. "site" hits are content
(the e-mail rao@site.in, "site layout" of crawled pages); "university" is a stemming example. None of these lessons is
on YouTube (pipeline.json: every lesson "draft", live false; videos.json: 0 of 27 video links).
Checker blind spot: on-screen text drawn by each lesson's own art functions (e.g. NLt(..., 'the book’s order') in u7-L3)
is not in SC, so an SC-only check misses it; scan the art code's string literals too.

lesson | scene | what's wrong | severity
--- | --- | --- | ---
c-nlp-u3-L3 | calc (13) | UAS/LAS board: "IF ate → quickly (dobj): right head, wrong label → UAS 0.8333 · LAS 4 ÷ 6 = 0.6667". With quickly on ate every head is right, so UAS = 6/6 = 1.0 and LAS = 5/6 = 0.8333 (the narration's "change only a label, and just the labeled score falls" is right; the board is not) | wrong fact: must fix
c-nlp-u3-L1 | pq/pa (19, 20), also (17, 18) | Q3 model answer "No PP rule, no P → in" for "G above", but the lesson shows PP → P NP twice (notebook 4 "Recursion: NP → NP PP and PP → P NP", calc 12 grammar). "G above" is never shown: the last grammar on screen (calc 12) has no "saw" and puts a PP in every S, so Q2's "the girl saw the boy" is not derivable from it either | wrong fact: must fix
c-nlp-u6-L4 | bookfig (3), calc (5, 6) | Figure 6.7.1 and worked example: predicted "the cat" vs gold "cat" given EM = 0, F1 = 0.667. The standard SQuAD scorer strips articles before comparing, so this pair scores EM 1, F1 1. Say "no normalisation" or use an example without an article | misleading: should fix
c-nlp-u2-L1 | bookfig (8), calc (11, 12), trap2 (13) | Part 2 counts (N = 10, V = 6, c(the) = 4; bar chart the/cat/sat/on/mat/dog) do not match Part 1's corpus "the cat sat on the mat the cat sat" (the × 3, 9 words), which Q3 (20) uses again with c(the) = 3; reads as the same corpus | misleading: should fix
c-nlp-u4-L2 | bookfig (3) | Figure 4.3.1 (top): narration "four edges down, you reach carnivore", but the picture shows only "entity", a depth axis that stops at 3 and a "4 edges" label beside depth 2; no carnivore, no node at depth 4 | misleading: should fix
c-nlp-u4-L3 | pa (16) | co-training views given as "the words left of the target and the words right of it"; the usual two views for WSD co-training are local collocations and wider topical context | misleading: should fix
c-nlp-u2-L4 | bookfig (3) | spoken "Here is the book's figure" (must be "your free notes") | should fix
c-nlp-u4-L1 | bookfig (3), notebook (6) | spoken "The book draws two models", "Work it with the book's model" | should fix
c-nlp-u7-L4 | bookfig (4, 10) | spoken "Here is the book's picture of unit selection", "This is the book's confusion matrix" | should fix
c-nlp-u7-L3 | trap2 (7) | on-screen label "the book’s order" under the Write card (lesson art code, not in SC) | should fix
c-nlp-u1-L4 | outro (23) | "Next time, Unit two: n-gram models…" spoken; "NEXT UNIT · Unit 2" card | should fix
c-nlp-u2-L4 | outro (22) | "Next time, Unit three…" spoken; "NEXT UNIT · Unit 3" card | should fix
c-nlp-u3-L4 | outro (23) | "Next time, Unit four…" spoken; "NEXT UNIT · Unit 4" card | should fix
c-nlp-u4-L4 | outro (23) | "Next time, Unit five…" spoken; "NEXT UNIT · Unit 5" card | should fix
c-nlp-u5-L3 | outro (23) | "Next time, Unit six…" spoken; "NEXT UNIT · Unit 6" card | should fix
c-nlp-u6-L4 | outro (23) | "Next time, Unit seven…" spoken; "NEXT UNIT · Unit 7" card | should fix
c-nlp-u3-L4 | notebook (4) | cross-reference by unit number: spoken "so Unit two's taggers work unchanged"; on screen "HMM · MEMM · CRF, as in Unit 2" | should fix
c-nlp-u2-L2 | pq (16, 18, 20) | spoken Bloom levels: "Question one, understand", "Question two, apply", "Question three, analyze" | should fix
c-nlp-u2-L4 | pq (15, 17, 19) | spoken Bloom levels: "Question one, at the understand level", "Question two, apply", "Question three, analyze" | should fix
c-nlp-u3-L1 | pq (15, 17, 19) | spoken Bloom levels: "An understand question", "Question two, apply", "Question three, analyze" | should fix
26 lessons (all but u4-L1) | figs (20–26, the "For your notes" scene) | "Sources the book draws on: …" in red on screen; u4-L1 already says "Sources the notes draw on" | cosmetic
c-nlp-u2-L2 | bookfig (3), calc (5, 6, 7), trap2 (8), recap (15), pa (17, 19), figs (22) | caret maths on screen: "PP(W) = P(W)^(−1/m)", "0.1^(−1/3)", "e^0.7675", "0.01^(1/3)", "PP = 2^H" (18 places) | cosmetic
c-nlp-u1-L4 | recap (15) | stock shield on the "Two traps" card (a match adds 0; dedupe before the split) | cosmetic
c-nlp-u6-L4 | recap (15) | all three cards are generic icons (a document, list blocks, a bar chart), not the lesson's own figures (EM/F1 pair, index, AP list) | cosmetic
c-nlp-u4-L2 | recap (15) | "WordNet" card is a generic document/list icon, not a synset | cosmetic
c-nlp-u7-L4 | outro (22) | end card "THAT'S A WRAP · All seven units" counts units | cosmetic

Count: 2 must fix, 18 should fix, 6 cosmetic (26 lines). Patterns: "book" wording (26 sources lines + 4 lessons with
spoken or drawn "the book's …"), unit numbers in outros and one cross-reference (7 lessons), spoken Bloom levels
(9 lines in 3 lessons), caret maths (1 lesson, 18 places), generic recap icons (3 lessons), and two lessons whose exam
or worked example silently switches to a different grammar or corpus (u3-L1, u2-L1).

## Web Technologies and Full Stack Development (18 Nov)

Audited 18 Nov 2026: all 23 c-web lessons (04_Lessons/cse/c-web/_work/uN/out; this subject has no B.Tech/CSE folder yet),
every scene, narration and the rendered last frame of each scene (dumped at 0.995), plus lesson_sheet.py sheets at 0.92 for
all 23 (the 3 lines that looked cut on a sheet render whole at 0.995: u1-L2 (5), u6-L4 (4), u4-L3 (12)). Checker: 0 page
errors, 0 cue failures, 0 text outside the safe area on every sheet. Recomputed every worked example, model answer and trap
(DNS chain and TTL, request-rate and server counts, status-code classes, box model and border-box, hex/rgb/HSL of #FF6347,
flex grow shares with gaps, Bootstrap 80 px columns, auto-fit grid 4 × 210 px, specificity, element counts, colspan totals,
GET URLs, JS outputs ('5' == 5, x += '5', sort [1,10,9], splice/slice, var/let loops, f(5)/f(5,3), event-loop orders),
readyState/status, PHP 885 bill, "Pay: " . 885 vs + (TypeError in PHP 8), 0 == "" in PHP 8, fact(5), regex with and
without anchors, cookie 1800 s, servlet init/service/destroy counts, 405 from default doGet, JSX call counts, setCount
batching, login-form length 16, router matches, TS2322/TS2345, Angular totals, PWA cache 132 KB, Redux counts, debounce
700 ms, caret/tilde ranges, 64 KB chunks 16,384 and 8,192, mysql2 insertId/affectedRows/changedRows, Mongo
matched/modified, JWT lateness 600 s and 100 s, CI 110 s vs 1200 s). Ran the disputed snippets: jQuery 3.7.1 in Chromium
($('li').text() on Pen/Book/Bag gives "PenBookBag"; .html() gives "Pen"), the nested-p parse in Chromium (body becomes
`<p>one</p><p>two</p><p></p>`), and fs.readFile on a 2 GiB file in Node 22 (ERR_FS_FILE_TOO_LARGE). Scene = 0-based SC index
(the Lnn.png number). Sheets: no stock recap icons, no tiny or faint pictures, no overflow or overlap; every hook and recap
picture is the lesson's own. No filler word, college name, TODO, placeholder or caret maths outside code found.
No pipeline.json or videos.json exists for c-web, so none of these lessons is on YouTube.

lesson | scene | what's wrong | severity
--- | --- | --- | ---
c-web-u3-L4 | notebook (9) item 3, trap2 (12) | ".text() reads the first; .text('x') sets them all" and the trap "Write: .text() returns the first element's text only; use .each() to collect every text". Backwards: the jQuery .text() getter returns the combined text of every matched element ("PenBookBag", run in Chromium with jQuery 3.7.1); the struck-out "Don't write" line is the true one. .html(), .val() and .attr() are the getters that read only the first | wrong fact: must fix
c-web-u3-L2 | pa (23) | event-delegation model answer: "row = event.target.closest('tr'); if not null, delete that row" deletes a row on any click anywhere in the row, not only on its delete button. The check must be on the button (e.target.closest('button.delete')), then remove that button's tr | wrong fact: must fix
c-web-u5-L3 | hookArt (0), bookfig (3), calc (7), figs (22) | `Total: {{ price * qty \| currency }}` shown as "₹7,497.00". With no currency code the pipe uses DEFAULT_CURRENCY_CODE, which is USD, so it prints "$7,497.00"; needs `currency:'INR'` like the price line. The template also says price while the class field is product.price | wrong fact: must fix
c-web-u6-L3 | trap2 (12) | trap "Write: a plain object replaces the document; updateOne(filter, {marks: 88}) leaves only _id and marks". In the Node driver and mongosh, updateOne without update operators throws "Update document requires atomic operators"; replacing a document is replaceOne (only the old update() replaced) | wrong fact: must fix
c-web-u5-L4 | trap2 (8) | the rule (return a new object) is right but the picture's case is wrong: a mutating reducer doing count++ and a badge reading useSelector(s => s.count) does re-render, because the number changed. The stale case is a selector that returns the mutated object or array (s.items) | misleading: should fix
c-web-u6-L1 | bookfig (11), figs (20) | caption "The tilde locks the minor number: only 1.2.9 is allowed" and "Allowed: 2 for ^4.18.2 … and 1 for ~1.2.3 (1.2.9)": the filled 1.2.3 end (and every 1.2.x) is allowed too. The caret count includes its own lower bound 4.18.2, the tilde count leaves it out | misleading: should fix
c-web-u6-L2 | pa (24) | "4 × readFile of a 2 GB file = 4 × 2048 MB = 8 GB, out of memory": fs.readFile refuses any file over 2 GiB with ERR_FS_FILE_TOO_LARGE (checked on Node 22), so each call fails and no 8 GB is ever held. Use a 1.5 GB file or say "would try to hold" | misleading: should fix
c-web-u4-L4 | notebook (17) | Student entity shown with package-private fields, no getters or setters and a package-private constructor; Jackson finds no properties, so the 200 {"id":1,…} and 201 replies on screen cannot come from this code, and JPA wants a public or protected no-arg constructor. Add getters/setters (or a record DTO) or label it a fragment | misleading: should fix
c-web-u2-L1 | bookfig (3) | spoken "Under head: title, meta and link, dashed because they're void": title is not void (the picture is right, only meta and link are dashed) | misleading: should fix
c-web-u2-L1 | pa (25) | nested-p model answer: "the tree has two sibling paragraphs". The stray </p> makes a third, empty p (Chromium: `<p>One</p><p>Two</p><p></p>`); the picture shows two | misleading: should fix
c-web-u2-L2 | pa (18) | "the heading … gives it a place in the outline": the HTML outline algorithm was never implemented by browsers or screen readers and was removed from the spec in 2022 | misleading: should fix
c-web-u5-L1 | bookfig (3, 4), recap (16), pa (18), figs (23) | "Babel turns each JSX tag into a React.createElement call" stated as how it works now; since React 17 the default automatic runtime emits jsx()/jsxs() from react/jsx-runtime. Say "classic runtime" (Q2's createElement exercise can stay) | misleading: should fix
c-web-u5-L3 | notebook (5), pq/pa (18, 19) | *ngIf, *ngFor and trackBy taught as current Angular. Angular 17 added @if/@for (track required) and v20 (2025) deprecated *ngIf/*ngFor; name the version or teach both | misleading: should fix
c-web-u6-L4 | outro (24) | site/finder line on the end card "Find this unit in your own syllabus" with the spoken "on the University free and easy site", plus "end of unit six" and a "COURSE COMPLETE · Units 1 to 6" card | should fix
c-web-u3-L2 | figs (24) | writer's note on screen: "Sources the book draws on: … Jon Duckett, JavaScript and jQuery (both from memory; check)." | should fix
c-web-u1-L3 | calc (6), bookfig (12) | spoken "Now the book's worked example" (twice) | should fix
c-web-u2-L4 | bookfig (5, 12) | spoken "Your book's figure" | should fix
c-web-u4-L2 | bookfig (4, 11) | spoken "fact of four from your book", "Now your book's figure" | should fix
c-web-u5-L4 | bookfig (4, 12) | spoken "Your book's figure" | should fix
c-web-u2-L2, u3-L1, u3-L2, u3-L3, u6-L2, u6-L3 | agenda (1) | "Chapters x to y of your book" on the agenda card (the other 17 say "of your free notes") | should fix
c-web-u1-L3 | outro (22) | "Next time, Unit two…" spoken; "NEXT UNIT · Unit 2" card | should fix
c-web-u2-L4 | outro (24) | "Next time, Unit three…" spoken; "NEXT UNIT · Unit 3" card | should fix
c-web-u3-L4 | outro (21) | "Next time, Unit four…" spoken; "NEXT UNIT · Unit 4" card | should fix
c-web-u4-L4 | outro (27) | "Next time, Unit five…" spoken; "NEXT UNIT · Unit 5" card | should fix
c-web-u5-L4 | outro (25) | "Next time, Unit six…" spoken; "NEXT UNIT · Unit 6" card | should fix
c-web-u1-L1, u1-L3, u3-L1, u4-L2 | pq (15/17/19; u3-L1 18/20/22; u4-L2 17/19/21) | spoken Bloom levels: "An understand question", "Question two, an apply question", "Question three, an analyze question" | should fix
c-web-u2-L1, u6-L2, u6-L3 | pq (u2-L1 20/22/24; u6-L2 19/21/23; u6-L3 14/16/18) | spoken Bloom levels: "Question one, understand.", "Question two, apply.", "Question three, analyze." | should fix
c-web-u3-L2, u3-L3 | pq (u3-L2 18/20/22; u3-L3 17/19/21) | spoken Bloom levels: "at the apply level", "Question one, at the understand level" | should fix
all 23 lessons | figs (the "For your notes" scene) | "Sources the book draws on: …" on screen | cosmetic
all 23 lessons | META, kicker, pq cards (engine) | META.subject is "biotech"; kicker "UNIT n · LESSON k OF K" and "QUESTION n · UNDERSTAND/APPLY/ANALYZE" labels on every question card | cosmetic
c-web-u1-L1 | outro (22) | next-lesson card "Web browsers · HTTP and HTTPS" cut from "Web browsers, web servers and application servers" | cosmetic
c-web-u1-L2 | outro (25) | next-lesson card "Front end · Developer tools" while the narration says "front end, back end and full stack roles, and the MERN stack" | cosmetic
c-web-u1-L3 | bookfig (12) | caption "Only bytes that crossed count: 34 KB, not 46": 46 is never derived (app.css's size is not shown) | cosmetic
c-web-u2-L1, u2-L3, u6-L1 | bookfig (u2-L1 10, 16; u2-L3 3; u6-L1 3, 10); u1-L3 bookfig (3) | spoken "your notes'" / "from your notes" without "free" | cosmetic
c-web-u2-L3 | agenda (1), part, recap | title "Box model, colors and fonts" but "Colours and fonts", "Colour" on the part and recap cards | cosmetic
c-web-u3-L3, u6-L1 | pq/pa (u3-L3 19, 20; u6-L1 16, 17) | the same question twice: "console.log(1); setTimeout(…2, 0); Promise.resolve().then(…3); console.log(4)", same answer 1, 4, 3, 2; the A/D/C/B worked example is also in both | cosmetic
c-web-u1-L3, u3-L2 | hookArt (0) | same hook twice: "You tap Add to cart", cart badge 2 → 3 | cosmetic
c-web-u4-L2 | bookfig (12), trap2 (15) | "^ and $ make the whole string count": in PCRE $ also matches before a final \n (use \z or the D modifier) | cosmetic
c-web-u4-L3 | calc (13, 14) | Set-Cookie line "PHPSESSID=abc123; Max-Age=1800; HttpOnly" drops the SameSite=Lax that the flags step sets | cosmetic
c-web-u5-L1 | trap2 (6) | `<div class>` / `<label for>` imply failure; React 16+ renders them with a dev warning | cosmetic
c-web-u5-L3 | notebook (12) | "hydrateRoot adds the handlers" in an Angular lesson (React API, unnamed); "a PWA needs a service worker" to install is dated (Chrome dropped that in 2023) | cosmetic
c-web-u6-L2 | notebook (16) | "Safe (changes nothing): GET only" vs u1-L2 "GET, HEAD, OPTIONS" (only GET is among the five methods shown) | cosmetic
c-web-u6-L3 | notebook (4) | "createPool: 10 ready connections": mysql2 opens them lazily up to connectionLimit 10 | cosmetic
c-web-u6-L3, u6-L4 | figs | sources "Casciaro (streams and modules); Brown (REST APIs and deployment)" copied from u6-L2; they do not match a MySQL/MongoDB or a security/Docker lesson | cosmetic

Count: 4 must fix, 24 should fix, 16 cosmetic (44 lines). Patterns: four wrong technical facts (jQuery .text(), event
delegation, Angular currency pipe, Mongo updateOne), version-dependent behaviour stated as current (JSX runtime,
*ngIf/*ngFor, the HTML outline, PWA install), "book" wording (6 agendas, 4 lessons spoken, 23 sources lines), unit numbers
in 6 outros plus one site/finder line, spoken Bloom levels in 9 lessons, and one writer's "from memory; check" note on screen.

## Machine Learning (18 Nov)

Audited 17–18 Nov 2026: all 19 c-ml lessons (04_Lessons/cse/c-ml/_work/u1–u6/out, byte-identical to the PC copy
B.Tech/CSE/Machine Learning/html), every scene, narration and last frame (SC dump plus rendered text at 0.995; sheets
at 0.92 and again at 0.995). Checker: 0 page errors, 0 cue failures, 0 text outside the safe area on every sheet.
Recomputed every worked example and model answer: accuracy and train/test gaps, the 90%/recall-0 loan model, Find-S
and candidate elimination (S, G, version space), least squares (Sxy, Sxx, b0, b1, SSE, MSE), every gradient-descent
step and J value, sigmoid values and the decision boundary, logistic gradients, ridge/lasso values, confusion-matrix
precision/recall/F1/specificity, CV mean, entropy and information gain, ID3 split, Naive Bayes scores and posterior,
Laplace smoothing, Bayes optimal classifier, Bayes-net joint and P(S), kNN distances and weights, SVM w, b and margin,
AdaBoost ε, α and reweighting, LWR normal equations, k-means distances, centroids and SSE, single linkage, EM
responsibilities and means, PCA covariance, eigenvalues and projections, LDA S_W, S_B, w and projections, silhouettes,
fuzzy c-means memberships and centres, perceptron runs and MP units, 2–3–1 and 3–4–2 parameter counts, XOR outputs,
softmax and cross-entropy, sigmoid backprop (δ and the updated weight), momentum steps, L2 decay, vanishing-gradient
products, convolution and max-pool maps, CNN parameter counts, RNN states and gradient factors, discounted returns,
TD error, Q-learning and SARSA updates, rule precision and FOIL gain. All exam traps checked; the script found no
near-duplicate traps. Scene = 0-based SC index (the Lnn.png number).
No spoken Bloom words (every pq says "Question one/two/three"), no site/finder line, no filler, no TODO; next-lesson
cards are whole titles. None of these lessons is on YouTube (live false, not uploaded).
META.subject is "biotech" on all 19 lessons (should be the ML subject id).

lesson | scene | what's wrong | severity
--- | --- | --- | ---
c-ml-u1-L2 | notebook (4) | art (u1/out/c-ml-u1-L2.js, writer-made) shows the MAP rule as "h* = arg max P(h) over H", which picks by the prior alone; MAP is argmax_h P(D\|h) P(h) (the notes: argmax [log P(D\|h) + log P(h)]) | wrong fact: must fix
c-ml-u1-L2 | notebook (4) | design-cycle snake numbered 1 T,P,E · 2 collect · 3 prepare · 4 features · 5 deploy · 6 test once · 7 algorithm · 8 space H: row 2 is numbered backwards, so deploy comes before H, algorithm and test, against the narration and card ("data, features, H, algorithm, test, deploy") | misleading: should fix
c-ml-u1-L3 | pa (17) | Find-S "why ignore negatives": "No step rejects a negative, so its final hypothesis may cover one", and the picture shows a covered negative. The reason is the opposite: if the target is in H and the data has no noise, the most specific consistent h can never cover a negative, so negatives need no update | misleading: should fix
c-ml-u2-L2 | trap2 (7) | "Don't write: the answer is p = 0.73", but worked example (a) asks for p at x = 3, and 0.731 is exactly that answer; the trap only holds when the question asks for the class | misleading: should fix
c-ml-u3-L3 | trap2 (13) | "salary differences are about a million times bigger": the squared terms differ by about 3×10⁶ (8.1×10⁹ vs 2.7×10³); the differences themselves differ by about 1,700× | misleading: should fix
c-ml-u5-L2 | calc (6, 7) | worked example counts a 2–3–1 network (13 parameters), then runs XOR with only two hidden units h₁, h₂; the third hidden unit is never defined (same mismatch in the c-ml-u5 notes, 5.3 worked example) | misleading: should fix
c-ml-u5-L3 | trap2 (8) | "Don't write the L2 gradient as λw", but u2-L3 (notebook 9, calc 10) uses ridge ½λw², whose gradient is λw; the trap should name its λw² convention instead of calling λw wrong | misleading: should fix
c-ml-u5-L4 | calc (13), recap (15) | "Ten steps: 0.1201⁵ ≈ 0.000025" repeats the two-step factor five times; this RNN's real ten-step product (x = 1 each step) is ≈ 3.0×10⁻⁶ (the notes hedge with "ten similar steps"; the lesson does not) | misleading: should fix
c-ml-u6-L2 | bookfig (8), notebook (10) | FOIL gain "3 × [log₂(3/3) − log₂(4/8)] = 3": the binding counts (4 of 8 before, 3 of 3 after) are given on the board but never derived, and they do not follow from the family tree shown | misleading: should fix
c-ml-u6-L1 | bookfig (10) | spoken "the book's Python code" (must be "your free notes") | should fix
c-ml-u1-L3 | outro (23) | "Next time, Unit two…" spoken; "NEXT UNIT · Unit 2" card | should fix
c-ml-u2-L3 | outro (25) | "Next time, unit three…" spoken; "NEXT UNIT · Unit 3" card | should fix
c-ml-u3-L4 | outro (24) | "Next time, Unit four…" spoken; "NEXT UNIT · Unit 4" card | should fix
c-ml-u4-L3 | outro (29) | "Next time, Unit five…" spoken; "NEXT UNIT · Unit 5" card | should fix
c-ml-u5-L4 | outro (23) | "Next time, unit six…" spoken; "NEXT UNIT · Unit 6" card | should fix
c-ml-u6-L2 | outro (25) | "revise all six units" spoken; end card "All six units, with your free notes" | should fix
c-ml-u1-L1, u2-L2, u3-L3 | hookArt (0) | three spam-email hooks | should fix
c-ml-u4-L1, u4-L2, u4-L3 (and u2-L1) | hookArt (0) | shop-customer hook in three lessons in a row (u2-L1 is a shop too) | should fix
c-ml-u1-L2, u2-L3 | hookArt (0) | same joke twice: model looks great, the team celebrates ("orders cake" / "high-fives"), then it fails | should fix
all 19 lessons | META | META.subject = "biotech" | should fix
all 19 lessons | figs ("For your notes" scene) | "Sources the book draws on: …" on screen | cosmetic
c-ml-u2-L2 | notebook (4), calc (5, 6), pa (17) | caret maths: "e^(−z)", "e^(−1)", "e^(3)", "e^(−3)" | cosmetic
c-ml-u3-L4 | bookfig (4), calc (6, 7), trap2 (8) | caret maths: "e^α", "e^−α", "e^0.5493" | cosmetic
c-ml-u5-L2 | calc (12) | caret maths: "e^zᵢ" | cosmetic
c-ml-u4-L3 | 3, 6, 7, 8, 10, 16, 17, 18, 21, 24, 25, 27 | underscore subscripts outside code: S_W, S_B, μ_c, N_c, u_ij, d_ij, S_i, M_ij, μ_1 | cosmetic
c-ml-u1-L3, u3-L3, u3-L4, u4-L2 | notebook (12); calc (5, 6, 11, 12); calc (13, 14); notebook (10) | underscore subscripts: n_train, n_test; Σ_S, Σ_F, x_Q, x_i, w_i; S_x, S_xx, S_y, S_xy; W_k | cosmetic
c-ml-u5-L2, u5-L3, u5-L4 | notebook (5, 16); notebook (11); notebook (4), calc (6, 19) | code-style names in prose: a_prev, fan_in, C_in (u6-L2 route_clear is a predicate name and can stay) | cosmetic
c-ml-u1-L2, u2-L2, u2-L3, u3-L4, u4-L2, u5-L1, u5-L2, u5-L3, u5-L4, u6-L2 | recap | tiny pictures: a small icon in a circle, about 1/5 of the card | cosmetic
c-ml-u4-L3, u3-L1 | recap | Fuzzy card is a thin bar; MAP/MLE card is generic bars | cosmetic
c-ml-u3-L1, u3-L4, u6-L1, u1-L2 | bookfig (3); bookfig (3); bookfig (10); bookfig (3) | mostly empty stage: two orphan arrows on an empty card; a small table; a small figure; sparse | cosmetic
c-ml-u4-L1 | notebook (9) | sparse picture | cosmetic
c-ml-u4-L3 | bookfig (4) | caption "w joins the two class means", but the drawn w starts at the origin and passes through neither mean; the "(1, 2)" label covers the y-axis tick "2" | cosmetic
c-ml-u4-L3 | bookfig (11) | "A 0.868" label sits on the axis "0" | cosmetic
c-ml-u4-L1 | bookfig (5) | the 1,000 and 5,000 tick labels sit under the centroid markers | cosmetic
c-ml-u5-L2 | bookfig (10) | the 0.245 value overlaps its probability bar | cosmetic
c-ml-u3-L3 | bookfig (9) | the k circle crosses the "2" tick labels | cosmetic
c-ml-u2-L1 | calc (5) | b₁ = 2 is only spoken, not on the board | cosmetic
c-ml-u5-L3 | pa (19) | Q2 asks for the velocity and the weight after two steps; the board shows only w (v₂ = 0.95 is implicit) | cosmetic

Count: 1 must fix, 19 should fix, 18 cosmetic (38 lines). Patterns: one wrong formula in writer-made art (u1-L2 MAP),
traps and model answers that call a valid convention or the correct answer wrong (u2-L2, u5-L3, u1-L3), worked examples
whose givens are missing or inconsistent (u5-L2 hidden unit, u6-L2 bindings, u5-L4 ten steps), unit numbers in all
6 last-lesson outros, META.subject "biotech" everywhere, repeated spam/shop/celebration hooks (8 lessons), caret and
underscore maths (12 lessons), tiny recap pictures (10 lessons).

## Theory of Computation (18 Nov)

Audited 18 Nov 2026: all 21 c-toc lessons (B.Tech/CSE/Theory of Computation/html: u1 L1–L4, u2 L1–L4, u3 L1–L4, u4 L1–L2,
u5 L1–L3, u6 L1–L4), every scene, narration and the rendered last frame of each scene (dumped at 0.995), plus
lesson_sheet.py sheets at 0.92 for all 21 (u4-L2 re-rendered at 0.995). Checker: 0 page errors, 0 cue failures, 0 text
outside the safe area on every sheet. Recomputed every worked example, model answer and trap in code: every DFA, NFA, ε-NFA,
PDA and TM trace; every regex on its strings (0+1(01)*, 0*(10*10*)*, (0*1)*0*1 = (0+1)*1, the mobile-number regex); ECLOSE
sets, the subset construction and the minimisation passes; Arden's rule; Thompson counts (10 states, 9 ε-moves); the
product DFA and |Q_A| × |Q_B|; every pumping-lemma split; derivations, ambiguity, simplification (8 productions), CNF
(5 rules) and CYK (V[1,3] = {S}); closure constructions; PDA and DPDA runs; leftmost/rightmost parse orders; TM IDs, the
unary adder, two-tape 2n+3 and the storage machine; dovetailing step counts; PCP instances (1,2,3 = aabbab; Q2 = aba);
the diagonal tables, Rice/FIN, Hamiltonian-cycle and SPACE ⊆ TIME arguments. Each wrong fact below was also checked against
the unit book (c-toc-uN.html): the u4-L2 PDA, the u6-L1 step counts and the u1-L1 figure machine are wrong in the book too.
Scene = 0-based SC index (the Lnn.png number). Sheets: no stock recap icons (every recap picture is the lesson's own), no
tiny or faint pictures, no overflow or overlap; no filler word, no repeated hook, joke or trap, no cut next-lesson card.
pipeline.json has live: false for every unit, so none of these lessons is on YouTube.

lesson | scene | what's wrong | severity
--- | --- | --- | ---
c-toc-u4-L2 | bookfig (11, 12), notebook (13) | one-state CFG→PDA for S → aSb \| ε has both δ(q, ε, Z₀) = {(q, SZ₀)} and δ(q, ε, Z₀) = {(q, ε)} on the same state, so after a full match it can push S again and accepts (aⁿbⁿ)*: abab and abaabb are accepted (run in code). The book says the final pop is "safe because S → ε"; it is not. Start with S as the initial stack symbol, or use separate start and end states. The scene also flips stack conventions (stack top-left in one table, "bottom → top" in the next) | wrong fact: must fix
c-toc-u6-L1 | bookfig (3, 4), calc (6, 7), pa (18), figs (21) | dovetailing counts: round k runs "k steps of M, then k of M′", so D stops the moment M accepts at step 6 of round 6: 30 + 6 = 36 steps, not 42 (Q2: 12 + 4 = 16, not 20). The hint "M′ never accepts, so D never waits for it" contradicts 42. Same numbers in the book. Either say D checks only at the end of a round, or use 36 and 16 | wrong fact: must fix
c-toc-u5-L3 | bookfig (3, 4), notebook (6), pa (23) | machine "accepts strings ending in 1" with q1 as its accept state, but its run passes through q1 at move 1. Under u5-L1's definition (entering q_accept accepts and halts) it accepts 10 and 100; it also breaks the lesson's own trap (18) "never make q01 accepting: halts early". The book uses a private convention (accept on halting in q1; a final state may have outgoing moves) the lesson never states | wrong fact: must fix
c-toc-u3-L3 | bookfig (12), calc (13, 14) | pumping-lemma proof "Assume CF, with p equal to five": the book's caveat "let p be its pumping length … the same argument works for every p" is dropped, so students learn to choose p themselves (the adversary picks p) | misleading: should fix
c-toc-u1-L1 | bookfig (14), notebook (15, 16) | Figure 1.3.1 uses a machine where C loops on 0 and 1 (the "contains 01" DFA), straight after trap (12) says that machine is wrong for "ends in 01"; the lesson never says the language changed. Inherited from the book, which reuses the names A, B, C | misleading: should fix
c-toc-u2-L4 | bookfig (8) | Figure 2.9.1 counts "11 live states plus dead state d = 12" (a complete DFA) but draws no q10 → d edge on 0–9, so an 11-digit number has nowhere to go; only q0 → d on 0–5 is drawn | misleading: should fix
c-toc-u3-L4 | notebook (17) | Type 3 example S → aS \| B, B → bB \| ε breaks the strict right-linear shape A → aB \| a given in (15) and Figure 3.9.1 (unit rule S → B and an ε-rule) | misleading: should fix
c-toc-u6-L4 | notebook (3) | "More time or space decides strictly more languages" is false as stated: linear speedup gives TIME(n²) = TIME(2n²); the hierarchy theorems need constructible bounds and a log-factor (time) or strictly larger (space) gap | misleading: should fix
c-toc-u1-L2 | notebook (9) | side picture shows ECLOSE(q0) = {q0, q1, q2}, ECLOSE(q2) = {q2}, while figure (8) and worked example (10) use ECLOSE(q0) = {q0, q1}, ECLOSE(q2) = {q2, q3}: same names, different machine | misleading: should fix
c-toc-u2-L2 | bookfig (9) | "subset construction gives the two-state parity DFA" from a Thompson ε-NFA: it gives more states; minimisation is needed for two | misleading: should fix
c-toc-u6-L4 | outro (21) | "Find this unit in your own syllabus on our site." spoken | should fix
c-toc-u1-L2, u1-L3, u3-L2 | agenda (1) | "Chapters x to y of your book" on the agenda card (the other 18 say "of your free notes") | should fix
c-toc-u1-L2, u1-L3, u2-L2, u3-L4, u5-L1, u5-L2, u6-L1, u6-L2 | u1-L2 (3); u1-L3 (3, 8); u2-L2 (3, 5, 9); u3-L4 (11); u5-L1 (5, 10, also in the cue text); u5-L2 (3); u6-L1 (3, 10); u6-L2 (3, 6) | spoken "the book's figure…" / "from your book" | should fix
c-toc-u1-L4 | outro (23) | "Next time, Unit two…" spoken; "NEXT UNIT · Unit 2" card | should fix
c-toc-u2-L4 | outro (22) | "Next time, Unit three…" spoken; "NEXT UNIT · Unit 3" card | should fix
c-toc-u3-L4 | outro (27) | "Next time, Unit four…" spoken; "NEXT UNIT · Unit 4" card | should fix
c-toc-u4-L2 | outro (29) | "Next time, Unit five…" spoken; "NEXT UNIT · Unit 5" card | should fix
c-toc-u5-L3 | outro (27) | "Next time, Unit six…" spoken; "NEXT UNIT · Unit 6" card | should fix
c-toc-u3-L4 | notebook (17); bookfig (4, 13) | "not recursive (Unit 6)" on screen; section cross-references "(3.6)", "(3.5)" on screen | should fix
c-toc-u1-L3 | pq (14, 16, 18) | spoken Bloom levels: "An understand question", "Question two, apply", "Question three, analyze" | should fix
c-toc-u3-L1 | pq (17, 19, 21) | spoken Bloom levels: "An understand question", "at the apply level", "at the analyze level" | should fix
c-toc-u4-L2 | bookfig (16, 17) | Figure 4.5.1 (parse tree of id + id * id) is split across two moving pages: the first shows the top three levels without F and id, the second only the bottom subtrees, so no frame shows the whole tree with all 8 ↓ and 8 ↑ numbers | cosmetic
c-toc-u6-L4 | outro (21) | card "Unit 6 complete · all six units done" | cosmetic
c-toc-u3-L2 | figs (22) | sources line cites normal forms, PDAs and the pumping lemma; does not match a lesson on ambiguity and simplification | cosmetic
c-toc-u2-L3, u5-L2, u6-L1, u6-L2, u6-L3 | u2-L3 (10–12); u5-L2 (10–12); u6-L1 (5, 8, 10–13, 19–21); u6-L2 (5, 10, 12, 16); u6-L3 (9, 11, 12, 20) | underscore maths outside code on screen: \|Q_P\| = \|Q_A\| × \|Q_B\|, q_accept, L_u, A_TM, E_TM, EQ_TM, M_w, S_P, χ_L (use subscripts) | cosmetic
c-toc-u6-L4 | notebook (18), pa (19) | caret maths 2^(O(s)) on screen | cosmetic
c-toc-u3-L4 | notebook (13, 15) | audio only: the lexicon reads terminal "a" as "A", so "A goes to a B" is heard as A → AB | cosmetic
all 21 lessons | figs (the "For your notes" scene) | "Sources the book draws on: …" on screen | cosmetic
all 21 lessons | META, kicker, pq cards (engine) | META.subject is "biotech"; kicker "UNIT n · LESSON k OF K" and "QUESTION n · UNDERSTAND/APPLY/ANALYZE" labels on every question card | cosmetic

Count: 3 must fix, 18 should fix, 8 cosmetic (29 lines). Patterns: three wrong facts, two of them in the unit book too
(a one-state PDA that loops back to S, dovetailing counts that ignore early stopping) and one from a private TM acceptance
convention; a dropped "for every p" in a pumping proof; figures that quietly switch machines (u1-L1, u1-L2) or leave a
complete DFA incomplete (u2-L4); "book" wording (3 agendas, 8 lessons spoken, 21 sources lines), unit numbers in 5 outros
plus one site line, spoken Bloom levels in 2 lessons, and _ / ^ maths in 6 lessons.

## Software Engineering (18 Nov)

Audited 18 Nov 2026: all 23 lessons in B.Tech/CSE/Software Engineering/html (u1 L1–L3, u2–u6 L1–L4), every scene's
narration and the rendered last frame of each scene (dumped at 0.995), plus lesson_sheet.py sheets at 0.92 for all 23, with
re-renders at 0.995 for every sheet that looked cut (the four recap pills below stay cut at 0.995; the u6-L3 and u5-L2
values that looked blank render at 0.995). Checker: 0 page errors, 0 cue failures, 0 text outside the safe area on every
sheet. Recomputed every worked example, model answer and trap: basic COCOMO (10 KLOC organic E = 26.93 pm, D = 8.74 months,
3.08 staff; 5 KLOC E = 13.0, D = 6.63), CPM (14 days, slack C and E 4) and PERT (5), cyclomatic complexity (V(G) 3 and 5,
basis paths and their inputs), boundary values, loop tests, GST ₹180, availability (99.9 % = 8.76 h, 99.95 % = 4.38 h, 99.01 %,
90.9 %), MTBF 625 and 500 h, DRE, leakage and defect density, break-even 15 runs, test-plan cycles 15.8/23.8/17.9 days,
release report rates, pipeline 41/26/22 min, merge to 26 lines, incremental build 9.23×, Ansible 36/0 changes, risk
exposures, inspection rate 200 lines/h and 83.33 %, re-engineering payback 0.9375 years, QFD 60/44, DFD 12/19, feasibility
(₹3,60,000, ₹1,52,000, ₹2,08,000, 2.88 years), workshop 1080 and 77.78 %, communication paths 10/28/15/45, velocity
4 sprints, semantic versions, and UML notation (composition's filled diamond at Account, multiplicities, aggregation vs
composition): all correct except the lines below. Not slop: "book" as a verb ("book a ticket") or library books in
examples, "ticket site", "the developer's site" / "the user's site" (alpha and beta testing), "a standards book"
(Pressman's myth). No site/finder line and no college names. None of the 23 is on YouTube (pipeline.json live: false,
upload_sheet publish fields empty).

lesson | scene | what's wrong | severity
--- | --- | --- | ---
c-se-u5-L2 | notebook (11), calc (14), bookfig (15) | execution progress "executed 1140 of 1200 = 95%" counts the 60 blocked cases (900 passed + 180 failed + 60 blocked = 1140) as executed, while the same notebook says a blocked case "could not run"; executed is 1080, progress 90% (or change the counts) | wrong fact: must fix
c-se-u4-L4 | hookArt (0); bookfig (4), calc (6, 7) | hook says 10,000 users on the ticket site makes each page take 8 s; the lesson's own graph gives 2.8 s at 10,000 users (the 3 s target holds to about 10,714) | misleading: should fix
c-se-u2-L2 | pa (16) | "verification works on the code [the built system]; validation works on the document" reverses u4-L1 (11, 12, outro): verification is static review of documents and code, validation runs the product | misleading: should fix
c-se-u3-L4 | trap2 (10), pa (23) | numbering the messages on a sequence diagram is called a non-standard, mark-losing error; UML allows sequence numbers there (optional, redundant with the time axis). Only the "time axis on a collaboration diagram" half is wrong | misleading: should fix
c-se-u3-L2 | notebook (14) | "a class adapter needs multiple inheritance, so it is not possible in Java": Java does it when Target is an interface (class Adapter extends Adaptee implements Target) | misleading: should fix
c-se-u6-L3 | pa (23) | answer and board use "a ten person-week impact" ("1.2, I = 10 pw") for a risk the question gives only as exposure 1.2; P would be 0.12, never shown, and no risk in the lesson has P 0.12 | misleading: should fix
c-se-u5-L4 | calc (13), bookfig (14) | host 9 is down (unreachable) but the recap reads "11 ok, 1 failed"; Ansible's PLAY RECAP counts it as unreachable=1, failed=0 | misleading: should fix
c-se-u4-L2 | bookfig (15, 16), calc (18) | the Invoice stub returns ₹1,180 (₹1,000 plus the 18% GST just computed) and GST is charged on it again (₹212.40, total ₹1,392.40) while the narration says "the total comes out right": reads as double taxation | misleading: should fix
c-se-u2-L4 | bookfig (3) | narration "the arrows are named data flows, each carrying a noun" over a level-1 DFD whose arrows carry no names (only "confirmation"); the lesson's own trap says unnamed flows lose marks | misleading: should fix
c-se-u1-L1, u3-L1, u3-L2, u3-L3, u4-L3, u6-L3, u6-L4 | agenda (1) | "Chapters x to y of your book" on the agenda card | should fix
c-se-u2-L4, u3-L1, u4-L3, u6-L1, u6-L4 | bookfig (u2-L4 3, 10; u3-L1 3, 10; u4-L3 3; u6-L1 3, 9; u6-L4 9) | spoken "the book's …": "Here is the book's level one diagram", "In the book's hostel mess", "Here's the book's ticket site", "In the book's figure", "the book's system test", "the book's hostel mess app", "The book's figure", "The book's payroll system" (8 lines) | should fix
c-se-u1-L3, u2-L4, u3-L4, u4-L4, u5-L4 | outro (28, 22, 25, 24, 24) | "Next time, Unit two/three/four/five/six…" spoken; "NEXT UNIT · Unit N" card | should fix
c-se-u1-L1, u1-L2, u2-L2, u3-L3, u4-L1, u4-L4, u5-L2, u5-L4, u6-L2, u6-L3 | pq (three per lesson: u1-L1 18/20/22, u1-L2 16/18/20, u2-L2 15/17/19, u3-L3 18/20/22, u4-L1 20/22/24, u4-L4 17/19/21, u5-L2 19/21/23, u5-L4 17/19/21, u6-L2 19/21/23, u6-L3 18/20/22) | spoken Bloom levels: "An understand question", "Question two, apply" / "at the apply level", "Question three, analyze" (30 lines) | should fix
all 23 lessons | META | META.subject is "biotech" | should fix
all 23 lessons | figs | "Sources the book draws on: …" on screen | cosmetic: later
all 23 lessons | kicker, pq cards (engine) | kicker "UNIT n · LESSON k OF K" and "QUESTION n · UNDERSTAND/APPLY/ANALYZE" labels (open question D) | cosmetic: later
c-se-u1-L2, u4-L4, u5-L2, u5-L4, u6-L2 | agenda (1); bookfig (u1-L2 7, u2-L1 13, u3-L3 12, u5-L1 5, 10, u5-L2 7, 15, u5-L3 4, u5-L4 4, 7, 14, u6-L2 7) | "of your notes" / spoken "Your notes draw it…" without "free" | cosmetic: later
c-se-u6-L4 | outro (26) | "COURSE COMPLETE · Units 1 to 6" card | cosmetic: later
c-se-u1-L2, u3-L3, u4-L2, u4-L3 | outro (23, 25, 28, 23) | next-lesson card cut at a comma: "Waterfall, incremental, spiral · Agile"; "UML interaction diagrams · UML state chart" (3.8 also has activity, component, deployment); "System testing · Regression testing" vs narration "system testing, acceptance testing and debugging"; "Performance · Testing object-oriented" | cosmetic: later
c-se-u5-L2 | calc (13, 14), trap2 (17), pa (22) | underscore subscripts "D_pre", "D_post" on screen outside code (no caret maths in this subject) | cosmetic: later
c-se-u1-L2 | hookArt (0) | filler "a whole journey" | cosmetic: later
c-se-u3-L1, u4-L4; u5-L4, u6-L4 | hookArt (0) | repeated hooks: two "crowd on the ticket site" openers; two "the Friday release breaks production" openers; u2-L1 and u4-L4 share the "Long enough to …" joke shape | cosmetic: later
c-se-u3-L1, u5-L4, u5-L2, u2-L2, u6-L3, u4-L1, u6-L1 | recap (16, 16, 18, 14, 17, 19, 14) | stock or generic recap icons: stopwatch for "99.9 % up allows 8.76 h"; refresh arrow (Declare the state) and stopwatch (The numbers); clock (Break-even) and gauge (Metrics); refresh arrow with tick (Change control); shield and lightning (Risk management); gear and magnifier (QA vs QC); generic list and bar chart (Management spectrum, Metrics) | cosmetic: later
c-se-u4-L4, u3-L4, u5-L3 | recap (16, 17, 17) | tiny or faint recap pictures: Platforms tree (u4-L4), Interaction and Physical (u3-L4), Delivery pipeline boxes (u5-L3) | cosmetic: later
c-se-u5-L4, u6-L1, u2-L1, u5-L3 | recap (16, 14, 16, 17) | header pill overflows its card at 0.995: "DECLARE THE STATE" crosses into the next card, "Management Spectrum" runs past its card, "What, how well" clipped at the pill edge, "Continuous integration" touches the card edge | cosmetic: later
c-se-u6-L1 | recap (14) | "EV 15%" for effort variance; EV normally means earned value | cosmetic: later
c-se-u1-L3, u2-L1, u3-L3, u3-L2, u1-L2 | bookfig (u1-L3 15, 16; u2-L1 5; u3-L3 4; u3-L2 15; u1-L2 7) | split or thin figures: failure-cause boxes cut at the bottom edge (u1-L3 15) and orphaned on a mostly empty stage (16); one box on an empty stage (u2-L1 5); thin strip with cut card tops (u3-L3 4); facade arrow points to nothing (u3-L2 15); deploy box "10" squeezed with its label outside (u1-L2 7) | cosmetic: later
c-se-u3-L3 | pa (23) | eight same-looking buttons called a consistency break; it is a missing visual hierarchy (the buttons are consistent) | cosmetic: later
c-se-u4-L1 | trap2 (9) | "wrong interest at run time" while the example is a withdrawal check (amt < bal) | cosmetic: later
c-se-u6-L2 | bookfig (8) | "26.9 × ₹80,000 = ₹21,54,240": 26.9 × 80,000 = 21,52,000; 21,54,240 uses the unrounded 26.928 | cosmetic: later
c-se-u5-L4 | pa (20) | board label "Link and package = 160 s" is the total (3 × 45 s… = 160 s), not link and package | cosmetic: later
c-se-u4-L1 | pa (25) | chapter reference "new inputs (4.4)" on screen | cosmetic: later
c-se-u3-L1 | bookfig (3) | "up: 99.9 % of 365 × 24 = 8760 h" reads as if uptime were 8760 h | cosmetic: later

Count: 1 must fix, 13 should fix (8 misleading facts, 5 template lines), 21 cosmetic (35 lines). Patterns: one wrong number
(blocked cases counted as executed), contradictions inside a lesson or between lessons (u4-L4 hook vs its graph, u2-L2 vs
u4-L1 on verification and validation, u2-L4 narration vs its own DFD), dated or overstated rules (sequence numbers, Java
class adapter), "book" wording (7 agendas, 8 spoken lines in 5 lessons, 23 sources lines), unit numbers in 5 outros, spoken
Bloom levels in 10 lessons (30 lines), and recap pills too long for their cards.

## Signals and Systems fact review (Nov 2026)

Audited 21 Nov 2026: all 18 lessons on the branches lesson/ec-signals-u1-L1 … u6-L3 (u1 L1–L4, u2–u6 L1–L3), every
scene's narration and on-screen text against the library books books/ece/ec-signals/ec-signals-u1..u6.html on main, and
each lesson's lesson_sheet.py sheet once. Recomputed in python every worked example, model answer, trap, picture number and
recap number: Fourier series (c₁₂ = 4/π, 81 % power share, truncation error 1.190), RC step (y(1) = 0.632, y(2) = 0.865,
10–90 % in 2.2τ), |X(2)| = 0.354, 1/52, bandwidth B = 18.94 rad/s, Butterworth orders N = 12 and N = 3 with 34.1 dB,
sinc(0.425) = 0.728, SQNR 19.82 dB, 1 + 3.706⁶ = 2591, DFTs [3, 1.71 − j1.71, …] and [10, −2+2j, −2, −2−2j], circular
[5, 3, 5, 7] against linear [1, 3, 5, 7, 4] convolution, partial fractions A = −1/3, B = 4/3, plus the convolutions,
Euler steps, Laplace and z ROCs and sampling rates: all correct. Every pq shows its givens; no college, unit, chapter or
lesson numbers. No book errors beyond the two already fixed on main (u1 Q3 model answer 9c725a3, u5 2591), so no book
fixes. Fixed lessons rebuilt with --revoice (u3-L3, u5-L1, u6-L1) or --reuse (u5-L3); each --check OK, cuecheck 0 late
cues, sheet 0 page errors, 0 cue failures, 0 text outside the safe area, play-through OK.

lesson | scene | what's wrong | severity
--- | --- | --- | ---
ec-signals-u1-L1 | pa (Q3) | "3 cos(0.25πn) has no continuous parent": false (it samples 3 cos(0.25πt) at t = n); fixed before this review, lesson 59b639a, book 9c725a3 | wrong fact: fixed
ec-signals-u3-L3 | notebook (5) | "Paley–Wiener forbids a band of exact zeros" drops "causal", right after the ideal (noncausal) filter that has one; now "no causal filter can have a band of exact zeros" | misleading: fixed 4a64e41
ec-signals-u6-L1 | notebook (12) | "It exists when Σ\|x[n]\| is finite" states the sufficient condition as if it were the rule; the book says sufficient, not necessary; now "enough, though not required" | should fix: fixed 8c93284
ec-signals-u5-L1 | hookArt (0) | "The phone keeps 8000 numbers a second": dated (HD voice samples at 16 kHz); now "A classic phone line" | should fix: fixed d6fb762
ec-signals-u5-L3 | notebook (5), panel 4 | "Σ\|h[n]\| = 2 ✓" unlabeled, right after a panel with h = [1, 2] (sum 3); panel now labeled h[n] = (0.5)ⁿu[n] (drawing only, voice kept) | cosmetic: fixed e3761b6
ec-signals-u1-L3 | calc (6, 7) | hint "u(t) = 1 for t > 0" while the book takes u(0) = 1 | cosmetic: later
ec-signals-u2-L3 | notebook (4) | "a step rises 10–90 % in 2.2τ" said generally; true for a first-order (RC) system, which is the page's example | cosmetic: later
ec-signals-u3-L3 | bookfig (5) | figure fills 43 % of the stage (the sheet's own warning) | cosmetic: later

Count: 0 must fix found (1 wrong fact already fixed before the review), 1 misleading fact and 2 should-fix lines fixed, 1
cosmetic fixed, 3 cosmetic left. Clean: u1-L2, u1-L4, u2-L1, u2-L2, u3-L1, u3-L2, u4-L1, u4-L2, u4-L3, u5-L2, u6-L2, u6-L3.
Patterns: a condition dropped from a theorem (causal) or a sufficient condition stated as "when", and one dated
everyday fact in a hook.
