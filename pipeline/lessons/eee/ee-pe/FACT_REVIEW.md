# Fact review: Power Electronics lessons (21), ufe-subject-pipeline step 3a

One thread, Opus high. You did not write these lessons: review them as a stranger would.

Inputs (repo SwathishThiyagu/ufe-books, clone with push access):
- the 21 lessons, each on its orphan branch `lesson/<id>` (folder `<id>/` with html, mp3, words.json, final .js, .pron.json, sheet png):
  ee-pe-u1-L1 to u1-L3, u2-L1 to u2-L5, u3-L1 to u3-L4, u4-L1 to u4-L3, u5-L1 to u5-L3, u6-L1 to u6-L3
- the library books `books/eee/ee-pe/ee-pe-u1..u6.html` on main (the lessons may say only what these say)
- the engine `pipeline/lessons/engine/` (v4.6), `pipeline/SLOP.md` (the audit rules, section C is yours)

For every lesson, read the final .js and look at its sheet once:
1. Recompute in python every worked example (every calc stage), every model answer, both exam traps (the "Don't write"
   must be false under every common convention, and the stated wrong result must be what the mistake really gives),
   every number drawn in a picture, the recap numbers. Check RMS versus peak, phase versus line voltage, and where α is
   measured from (the natural commutation point) are the same on every board, picture and answer; re-solve every
   extinction angle β numerically.
2. Every exam question (pq) shows all the givens its answer uses; the answer uses only those and what the lesson showed.
3. Every claim is in the book or follows from it; no overstated facts (keep the book's conditions: continuous conduction,
   ideal switches, ripple-free load current, "for every", "sufficient").
4. Pictures agree with the narration and their own numbers; every waveform is drawn from computed points to its own
   numbers. No college names, city names, publisher names, unit, chapter or lesson numbers.
Known already from the writers (verify, then fix the book; the lessons already show the right value unless noted):
- u1: Fig 1.4.1 the "tq = 30 µs" label sits on the "20" axis tick; Fig 1.7.1 the label "P = ½C<sub>sV</sub>²f<sub>s</sub>"
  puts V inside the subscript (should be ½CsV²fs).
- u2: 2.1 worked example 1 "√(1.111² − 1) = √0.2337" mixes the rounded FF with the unrounded square (1.111² − 1 = 0.2343,
  √ = 0.484; RF = 0.483 comes from the unrounded FF: print FF = 1.1107 or RF = 0.484); Fig 2.8.1 the labels "inverter:
  power to AC" and "rectifier: power to DC" sit in each other's half (swap them).
- u3: 3.4 body says practical boosts keep D below about 0.85, its check-yourself answer says about 0.9 (make them agree);
  3.6 "only a few universities teach it" (active clamp); 3.7 says Ptotal "has a minimum at a best frequency", but a flat
  conduction term plus a switching term rising with fs has no minimum: add the magnetics term that falls with fs, as the
  Understand answer does; 3.7 "Only a few universities derive the full gain curves".
- u4: a lead says "Only a few universities teach it as a separate topic"; 4.6 worked example 2 the n = 3 and n = 5 sums are
  −0.0007 and −0.0009, not positive (the ≈ 0 conclusion holds); the trap "N angles remove N − 1 harmonics" sits beside an
  example where 2 angles remove 2 because the fundamental is left free: say "fix the fundamental, and N angles remove
  N − 1"; Figs 4.5.1 and 4.6.1 subscript lines overlap in their info boxes.
- u5: 5.1 worked example 2 "P = 14.60² × 10 = 2133 W" (14.60² × 10 = 2131.6; 2134 unrounded) and "sin 448.3°" should be
  448.4° (2β); Fig 5.3.1 legend and point labels run past the shaded band rectangles.
- u6: the induction figure labels the hot layer "δ = 12.5 mm" at 2 kHz, the worked example gives 12.3 mm (12.5 mm needs
  1945 Hz); 6.3 "Only a few universities teach its design as a full topic"; 6.7 "Only a few universities teach process
  control inside a power electronics course"; the 25 % example gives α = 1.986 rad, which rounds to 1.987 rad (113.8° is
  right); the sources name "Oxford University Press" (keep the author and title, drop the publisher).
- All units: the generator cut the figs-note source titles at commas ("Ned Mohan (and Design)") and many figure halves
  through their circuits; the writers rewrote and re-cut them. Confirm each lesson's sources are whole and each bookfig
  scene shows a whole circuit or plot.
Every "few universities" sentence and every city name in the books is something students see: reword each and check
no lesson narrates or draws one.
Lessons, must check: ee-pe-u4-L1 is 898 words (limit 880; trim only if you rebuild it anyway). Most lessons dropped some
of the book's worked examples to fit the word budget (u1-L1, u1-L2 and u4-L1 kept 3 of 6, u4-L2 kept 3 of 6, u6-L1 kept 4
of 5, u1-L3 merged one into its figure): check each ribbon's "N worked examples" matches the calc scenes, and that no
recap or answer relies on a dropped example. ee-pe-u5-L3 Q2 had its givens (230 V, 10 Ω) added: check. ee-pe-u6-L3's
next card already reads "Revise from the start: Power diodes: static and switching characteristics" (keep it).

Fix every must-fix item in the lesson .js, rebuild with `lesson_build.py --revoice` (only changed lines are voiced; set
up Kokoro and the fonts as the ufe-unit-lessons skill says), rerun --check, `cuecheck.py` and `lesson_sheet.py --frames
--play`, and push a new commit to the same `lesson/<id>` branch (keep the folder layout and names). Where the book is
wrong too, fix the book on main and rerun `python3 pack/check_book.py <book> packets/<unit>.json --render`
(the --render step needs Python playwright 1.63.0; older versions skip it and still print OK).
Log the findings in `pipeline/SLOP.md` under "Power Electronics fact review (Nov 2026)", in the style of the rows there.

Hand back in under 20 lines by messaging the thread "Build 8 new exam subjects" (thread id
cmsg_01VwvcZRx1mMD7zJQeF8gbhCHJ7d555QwKT2VRz537cmu9): per lesson, the findings and fixed / not fixed, the new commits,
any book fixes. Do not write to /mnt/project-files or the person's computer, and do not message the person.
