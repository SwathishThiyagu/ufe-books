# Fact review: Engineering Thermodynamics lessons (24), ufe-subject-pipeline step 3a

One thread, Opus high. You did not write these lessons: review them as a stranger would.

Inputs (repo SwathishThiyagu/ufe-books, clone with push access):
- the 24 lessons, each on its orphan branch `lesson/<id>` (folder `<id>/` with html, mp3, words.json, final .js, .pron.json, sheet png):
  me-thermo-u1-L1 to u1-L3, u2-L1 to u2-L4, u3-L1 to u3-L5, u4-L1 to u4-L3, u5-L1 to u5-L5, u6-L1 to u6-L4
- the library books `books/mech/me-thermo/me-thermo-u1..u6.html` on main (the lessons may say only what these say)
- the engine `pipeline/lessons/engine/` (v4.6), `pipeline/SLOP.md` (the audit rules, section C is yours)

For every lesson, read the final .js and look at its sheet once:
1. Recompute in python every worked example (every calc stage), every model answer, both exam traps (the "Don't write"
   must be false under every common convention, and the stated wrong result must be what the mistake really gives),
   every number drawn in a picture, the recap numbers. Check the sign convention (W done by the system positive, Q into
   the system positive, as the book uses) is the same on every board, picture and answer, and that steam-table values
   match the book's table rows exactly.
2. Every exam question (pq) shows all the givens its answer uses (R, cp, cv, γ, table values); the answer uses only those
   and what the lesson showed.
3. Every claim is in the book or follows from it; no overstated facts (keep the book's conditions: reversible, ideal gas,
   steady flow, "for every", "sufficient").
4. Pictures agree with the narration and their own numbers. No college names, city names, brands, unit, chapter or lesson numbers.
Known already from the writers (verify, then fix the book; the lessons already show the right value unless noted):
- u1: Fig 1.3.1 box "path 1→4→3" shows W = −10 + 0 = −10 kJ, the wrong sign (it should be +10 kJ).
- u2: the Apply question (0.5 kg air, 40 K rise at constant p) does not give R; a lead says "Only a few universities teach
  this as a separate topic"; two worked-example lines rely on givens that appear only in the hint.
- u3: Fig 3.2.1 "net: one reservoir" label overlaps the 200 kJ arrow; Fig 3.6.1 shows raw "< 0" text (escape it);
  Fig 3.7.1 the shaded area stops at the 250 K floor, not 0 K, so it looks smaller than its 301.5 label; 3.8
  −0.9008 + 0.9889 = 0.0881, not 0.0882; Fig 3.8.1 hot and cold colours are swapped (hot should be orange, cold blue);
  Q3 (insulated device, 300 K, 100 to 200 kPa) does not give R = 0.287; "Only a few universities ask for this form";
  two leads name Chennai (an air conditioner, a backup generator).
- u4: Fig 4.2.1 heading nearly touches the bracket label.
- u5: Fig 5.2.1 path (b) arrow runs past the boiling curve to x = 470 (stop it at 330); Fig 5.5.1 "250 °C" label sits on
  the 1 bar line; 5.7 worked example 2 "1.5 per cent low" is 1.44 %; two lines name Chennai (a room, a split air-conditioner coil).
- u6: Q2 does not give γ = 1.4; Q3 does not give rp, T1, cp or γ; the absorption chapter names the Electrolux brand
  (call it the three-fluid or diffusion-absorption refrigerator) and a worked example names "a hotel in Chennai" (say
  "a hotel"); the Q3 answer says the vapour is "less dense", which bears on capacity, not COP per kg: reword or drop it.
Every "few universities" sentence and every city name in the books is something students see: reword each and check
no lesson narrates or draws one.
Lessons, must check: me-thermo-u6-L4's next card already reads "Revise from the start: Microscopic and macroscopic
approaches" (keep it). me-thermo-u3-L5 and me-thermo-u5-L4 next cards put the topic in the second slot
(["UP NEXT", "Available and unavailable energy", "How much of the heat can become work"] and ["NEXT TIME", "Gas mixtures",
"Dalton's and Amagat's laws"]): make them ["…", "Next topic" or "Next lesson", "<the next lesson's title>", "book"] like
the others. me-thermo-u2-L1 had no glyphs for subscript v and p (check they render on the sheet); me-thermo-u5-L2's
chapter-2 title overflowed its part slide (check it fits); me-thermo-u6-L1 is 888 words (limit 880; trim only if you
rebuild it anyway). Several writers found the figs and sources notes garbled and rewrote them: confirm each picture's
source note names the right book figure.

Fix every must-fix item in the lesson .js, rebuild with `lesson_build.py --revoice` (only changed lines are voiced; set
up Kokoro and the fonts as the ufe-unit-lessons skill says), rerun --check, `cuecheck.py` and `lesson_sheet.py --frames
--play`, and push a new commit to the same `lesson/<id>` branch (keep the folder layout and names). Where the book is
wrong too, fix the book on main and rerun `python3 pack/check_book.py <book> packets/<unit>.json --render`.
Log the findings in `pipeline/SLOP.md` under "Engineering Thermodynamics fact review (Nov 2026)", in the style of the rows there.

Hand back in under 20 lines by messaging the thread "Build 8 new exam subjects" (thread id
cmsg_01VwvcZRx1mMD7zJQeF8gbhCHJ7d555QwKT2VRz537cmu9): per lesson, the findings and fixed / not fixed, the new commits,
any book fixes. Do not write to /mnt/project-files or the person's computer, and do not message the person.
