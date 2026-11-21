# Writer brief: Optical Fiber Communication lesson ec-optical-uN-Lk (replace N and k)

Fill and build ONE lesson with the ufe-unit-lessons skill, fast path, section 3 steps 2 and 3 only. Opus, high effort.

Inputs, all in the repo SwathishThiyagu/ufe-books on main (clone it with push access):
- `pipeline/lessons/engine/` (lesson_build.py, lesson_template.html, lesson_sheet.py, lesson_kinds.md, cuecheck.py, bumper/): engine v4.6
- `pipeline/lessons/ece/ec-optical/uN/`: WRITE.md, pronunciation.json, your lesson `ec-optical-uN-Lk.js` and `.pron.json`
- `books/ece/ec-optical/ec-optical-uN.html`: the library book the lesson was generated from (corrected 21 Nov 2026)
- `pipeline/lessons/ece/ec-signals/QUEUE.md`: the review note from the first approved lesson

1. Copy the engine, uN/WRITE.md, uN/pronunciation.json and your two lesson files to your scratchpad and work there.
   Set up Kokoro (kokoro-tts skill step 1) and the fonts (ufe-unit-lessons section 2.3). Python playwright must match the
   preinstalled Chromium: `pip install playwright==1.63.0` if it says the browser is missing.
2. Read only WRITE.md and your lesson file (lesson_kinds.md for a kind's fields). Replace every TODO, including every
   vis / wv / rv picture. Say only what the book says; no college or university names; check every number in python.
   This is an engineering subject: pronunciation.json holds biotech words, so add optical terms (NA, WDM, DWDM, CWDM, EDFA, SOA, LED, APD, PIN, OTDR, SONET, SDH, STM, ATM, FBG, SBS, SRS, SPM, PMD, MFD, LP, TE, TM, InGaAs, InGaAsP, AlGaAs, GaAs, erbium, Rayleigh, Mie, Brillouin, Raman, Fresnel, Bragg, Mach-Zehnder, dB/km, dBm...) to PR or to your own .pron.json. Draw optical pictures: fiber cross-sections with core, cladding and the index profile, ray paths with the acceptance cone and angles marked, mode field shapes, attenuation and dispersion curves against wavelength with the windows marked, pulse broadening along a fiber, LED and laser structures and their P-I curves, photodiode layers and the band diagram, receiver blocks, link budget bars, WDM spectra and network rings.
   Plot computed points only.
3. Tips from earlier writers:
   - lesson constants named PH or LN clash with engine globals: prefix your own names;
   - the generator's figure halves can cut through boxes: re-cut views and drop items outside each view;
   - the figs note may be cut mid-word: rewrite it from the book;
   - --check lists only 12 unknown words per run;
   - aim for 800 to 880 words from the first draft.
   - each worked example costs two calc scenes: with four examples, plan for that or the first draft runs past 1000 words;
   - the final stage of a calc row replaces the row, so the final must restate the key value;
   - bookfig steps often come out all as one step: renumber them so the figure builds one panel at a time;
   - the next-lesson card may show the unit title: use the next lesson's first chapter title.
   - (from this subject's first lessons) SVG baseline-shift="sub" sits far too low: use dy/baseline-shift -0.2em at 72 % size;
   - pa `al` lines wrap on spaces and can break a tspan: keep formulas in an `al` line as plain text (exp(−j2πft₀));
   - the sheet captures each scene at 92 %: cue answer stamps and captions early, never on the last words;
   - when a unit has more worked examples than 880 words allow, keep one per chapter and fix agenda.ribbon2 to match;
   - a fact check on every stamp's unit is worth it (one writer stamped 4 mV²·s for 4×10⁻³ V²·s).
4. Build and check as the ufe-unit-lessons skill says (section 8): --check, voice build, lesson_sheet.py --frames --play,
   as often as you need; rebuild with --reuse when only the drawing changed. Look at sheet.png once, the bookfig, calc,
   picture and answer pages and the four logo frames.
5. Name the page ec-optical-uN-Lk_<slug>.html (slug from META title, lowercase, hyphens).
6. Deliver to git, never to /mnt/project-files (it is nearly full): make an orphan branch `lesson/ec-optical-uN-Lk`
   holding only `ec-optical-uN-Lk/` with the html, .mp3, .words.json, final .js and .pron.json, and sheet.png renamed
   ec-optical-uN-Lk-sheet.png, and push it (`git worktree add --orphan -b lesson/ec-optical-uN-Lk ../wt-ec-optical-uN-Lk`, copy the folder in, commit, push; `git rm -rf` is blocked as destructive).
7. Hand back in under 15 lines by messaging the thread "Build three ECE communication subjects" (thread id
   cmsg_01VwvcZRx1mMD7zJQeF8gbhCCumGwwGnSucYHrGS8SFv6V): the branch, runtime, scenes, words, what each picture shows,
   anything wrong in the book, what slowed you down. Do not write to the person's computer, do not touch other lessons'
   files, and do not message the person.
8. Cue rule: on trap2, traps, notebook, recap and pa pages, every cue goes on the first two or three words of the
   sentence that introduces that item, never at the end of a long sentence. Check it with `python3 $E/cuecheck.py L.js`
   (must print 0 late cues; calc step cues inside a pa are exempt). Render the trap pages at 0.4 and at the end and look
   at every trap2 / traps frame: the cards must appear as the voice says them, not after.
9. Exam practice questions (pq pages): the voice asks the question and stops. Never add "Pause, and answer out loud";
   the page itself shows "Pause, answer, then listen." while the thinking clock runs.
10. Split figures (bookfig "(top)"/"(bottom)" halves) share defs ids, so arrow markers in the second half vanish: rename
    the marker/gradient ids in the second half (add a "b" suffix) and check the arrowheads on the sheet.
