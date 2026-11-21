# Writer brief: Mass Transfer Operations lessons ch-mass-uN (replace N; the first lesson is L1 alone)

Exam course: CH3551 Mass Transfer II (exam date not found). Build EVERY lesson of your unit uN (L1, L2, ... as listed in uN/videos.ch-mass-uN.json), one after
another, with the ufe-unit-lessons skill, fast path, section 3 steps 2 and 3 only. Opus, high effort. (The first-lesson
thread builds only ch-mass-u1-L1.)

Inputs, all in the repo SwathishThiyagu/ufe-books on main (clone it with push access):
- `pipeline/lessons/engine/`: engine v4.6 (lesson_build.py, lesson_template.html, lesson_sheet.py, lesson_kinds.md, cuecheck.py, bumper/)
- `pipeline/lessons/chem/ch-mass/uN/`: WRITE.md, pronunciation.json, and per lesson `ch-mass-uN-Lk.js` and `.pron.json`
- `books/chem/ch-mass/ch-mass-uN.html`: the corrected library book the lessons were generated from
- `pipeline/lessons/ece/ec-signals/QUEUE.md`: the review note from the first approved lesson of the earlier subjects

1. Copy the engine, uN/WRITE.md, uN/pronunciation.json and the lesson files to your scratchpad and work there.
   Set up Kokoro (kokoro-tts skill step 1) and the fonts (ufe-unit-lessons section 2.3). Python playwright must match the
   preinstalled Chromium: `pip install playwright==1.63.0` if it says the browser is missing.
2. Read only WRITE.md and the lesson file (lesson_kinds.md for a kind's fields). Replace every TODO, including every
   vis / wv / rv picture. Say only what the book says; no college or university names; no unit or lesson numbers on
   screen or in the voice; check every number in python. pronunciation.json holds biotech words, so add this subject's
   terms (NTU, HTU, McCabe-Thiele, Ponchon-Savarit, VLE, Raoult, Henry, Fenske, Underwood, Gilliland, Langmuir, Freundlich, Shanks, kmol, mol fraction, L/G ...) to PR or to the lesson's .pron.json. Draw this subject's pictures: x-y equilibrium diagrams with operating lines and stepped stages, packed and tray columns with streams labelled, triangular extraction diagrams, leaching stage diagrams, isotherms and breakthrough curves, membrane modules. Plot computed points only.
3. Tips from earlier writers:
   - lesson constants named PH or LN clash with engine globals: prefix your own names;
   - the generator's figure halves can cut through boxes: re-cut views and drop items outside each view;
   - the figs note may be cut mid-word: rewrite it from the book;
   - --check lists only 12 unknown words per run;
   - aim for 800 to 880 words from the first draft; each worked example costs two calc scenes;
   - the final stage of a calc row replaces the row, so the final must restate the key value;
   - bookfig steps often come out all as one step: renumber them so the figure builds one panel at a time;
   - the next-lesson card may show the unit title: use the next lesson's first chapter title.
4. Build and check as the ufe-unit-lessons skill says (section 8): --check, voice build, lesson_sheet.py --frames --play,
   as often as you need; rebuild with --reuse when only the drawing changed. Look at sheet.png once, the bookfig, calc,
   picture and answer pages and the four logo frames.
5. Name each page ch-mass-uN-Lk_<slug>.html (slug from META title, lowercase, hyphens).
6. Deliver to git, never to /mnt/project-files (it is nearly full): per lesson an orphan branch `lesson/ch-mass-uN-Lk`
   holding only `ch-mass-uN-Lk/` with the html, .mp3, .words.json, final .js and .pron.json, and sheet.png renamed
   ch-mass-uN-Lk-sheet.png, and push it (`git worktree add --orphan -b lesson/ch-mass-uN-Lk ../wt-ch-mass-uN-Lk`, copy the folder in,
   commit, push; `git rm -rf` is blocked as destructive).
7. Hand back in under 15 lines per lesson by messaging the thread "Prepare four new departments for Nov/Dec exams"
   (thread id cmsg_01VwvcZRx1mMD7zJQeF8gbhCSEDpjn61f27m6aCSWHGR7t): the branch, runtime, scenes, words, what each picture shows, anything wrong in the book, what
   slowed you down. Do not write to the person's computer, do not touch other lessons' files, do not message the person.
8. Cue rule: on trap2, traps, notebook, recap and pa pages, every cue goes on the first two or three words of the
   sentence that introduces that item. Check with `python3 $E/cuecheck.py L.js` (must print 0 late cues; calc step cues
   inside a pa are exempt). Look at every trap2 / traps frame: the cards must appear as the voice says them.
9. Exam practice questions (pq pages): the voice asks the question and stops. Never add "Pause, and answer out loud";
   the page shows "Pause, answer, then listen." while the thinking clock runs.
10. Split figures (bookfig "(top)"/"(bottom)" halves) share defs ids: rename the marker/gradient ids in the second half
    (add a "b" suffix) and check the arrowheads on the sheet.
11. No thumbnails in this thread (the t16 step is a separate thread per subject).
