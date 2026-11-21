# Fact review: Circuit Theory lessons (22), ufe-subject-pipeline step 3a

One thread, Opus high. You did not write these lessons: review them as a stranger would.

Inputs (repo SwathishThiyagu/ufe-books, clone with push access):
- the 22 lessons, each on its orphan branch `lesson/<id>` (folder `<id>/` with html, mp3, words.json, final .js, .pron.json, sheet png):
  ec-circuits-u1-L1 to u1-L4, u2-L1 to u2-L4, u3-L1 to u3-L4, u4-L1 to u4-L3, u5-L1 to u5-L3, u6-L1 to u6-L4
- the library books `books/ece/ec-circuits/ec-circuits-u1..u6.html` on main (the lessons may say only what these say)
- the engine `pipeline/lessons/engine/` (v4.6), `pipeline/SLOP.md` (the audit rules, section C is yours)

For every lesson, read the final .js and look at its sheet once:
1. Recompute in python every worked example (every calc stage), every model answer, both exam traps (the "Don't write"
   must be false under every common convention, and the stated wrong result must be what the mistake really gives),
   every number drawn in a picture, the recap numbers. Check the passive sign convention, current directions (I2 into
   port 2 for z, y, h; −I2 for ABCD) and RMS versus peak are the same on every board, picture and answer.
2. Every exam question (pq) shows all the givens its answer uses; the answer uses only those and what the lesson showed.
3. Every claim is in the book or follows from it; no overstated facts (keep the book's conditions: linear, bilateral,
   balanced, ideal, "for every", "sufficient").
4. Pictures agree with the narration and their own numbers; every phasor angle and curve is drawn to its own numbers.
   No college names, city names, unit, chapter or lesson numbers.
Known already from the writers (verify, then fix the book; the lessons already show the right value unless noted):
- u2: Fig 2.4.1 labels its network "worked example 1" (check the book's own example numbering matches the figure).
- u3: the unit intro says 3.8 is "taught at only a few universities", and the 3.8 lead says "Only a few universities
  teach this chapter; the rest stop at single-frequency AC"; the book's SVG subscripts (VL, XC) in Figs 3.3.1 and 3.4.1
  sit low and crowd the next character.
- u4: Fig 4.1.1 the "equal and opposite" label overlaps VR = 10 V.
- u5: the 5.1 lead names Chennai (a router held up "through a Chennai power cut": say "a power cut"); a lead says
  "Only a few universities teach this chapter"; Fig 5.7.1 the label "vC(0⁻) = 4 V" spills past the left panel border.
- u6: Fig 6.8.1 the full title runs past the figure's safe area.
- All units: the generator cut many figure halves through their circuits and plots; the writers re-cut them. Confirm
  each bookfig scene shows a whole circuit or plot, with its own labels and no stray items from the other half.
Every "few universities" sentence and every city name in the books is something students see: reword each and check
no lesson narrates or draws one.
Lessons, must check: ec-circuits-u5-L1 is 891 words, ec-circuits-u5-L2 895, ec-circuits-u3-L4 and u3-L2 881 (limit
880; trim only if you rebuild them anyway). Several lessons dropped some of the book's worked examples to fit the word
budget (u4-L1 kept 4 of 5, u4-L3 3 of 6, u5-L1 3 of 5, u6-L1 dropped the π network): check each ribbon's "N worked
examples" matches the calc scenes, and that no recap or answer relies on a dropped example. ec-circuits-u6-L1's next card
uses "Hybrid parameters" as its headline where every other lesson says "Next lesson" (make it ["NEXT TIME", "Next lesson",
"Hybrid (h) and inverse hybrid (g) parameters", "book"]). ec-circuits-u6-L4's next card already reads "Revise from the
start: Circuit elements R, L, C and their V-I relations" (keep it). Several writers found the figs and sources notes cut
mid-word and rewrote them: confirm each picture's source note names the right book figure and the sources are whole.

Fix every must-fix item in the lesson .js, rebuild with `lesson_build.py --revoice` (only changed lines are voiced; set
up Kokoro and the fonts as the ufe-unit-lessons skill says), rerun --check, `cuecheck.py` and `lesson_sheet.py --frames
--play`, and push a new commit to the same `lesson/<id>` branch (keep the folder layout and names). Where the book is
wrong too, fix the book on main and rerun `python3 pack/check_book.py <book> packets/<unit>.json --render`.
Log the findings in `pipeline/SLOP.md` under "Circuit Theory fact review (Nov 2026)", in the style of the rows there.

Hand back in under 20 lines by messaging the thread "Build 8 new exam subjects" (thread id
cmsg_01VwvcZRx1mMD7zJQeF8gbhCHJ7d555QwKT2VRz537cmu9): per lesson, the findings and fixed / not fixed, the new commits,
any book fixes. Do not write to /mnt/project-files or the person's computer, and do not message the person.
