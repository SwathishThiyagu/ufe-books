# Fact review: VLSI Design lessons (24), ufe-subject-pipeline step 3a

One thread, Opus high. You did not write these lessons: review them as a stranger would.

Inputs (repo SwathishThiyagu/ufe-books, clone with push access):
- the 18 lessons, each on its orphan branch `lesson/<id>` (folder `<id>/` with html, mp3, words.json, final .js, .pron.json, sheet png):
  ec-vlsi-u1-L1 u1-L2 u1-L3, u2-L1 u2-L2 u2-L3 u2-L4, u3-L1 to u3-L5, u4-L1 to u4-L5, u5-L1 to u5-L4, u6-L1 u6-L2 u6-L3
- the library books `books/ece/ec-vlsi/ec-vlsi-u1..u6.html` on main (the lessons may say only what these say)
- the engine `pipeline/lessons/engine/` (v4.6), `pipeline/SLOP.md` (the audit rules, section C is yours)

For every lesson, read the final .js and look at its sheet once:
1. Recompute in python every worked example (every calc stage), every model answer, both exam traps (the "Don't write"
   must be false under every common convention, and the stated wrong result must be what the mistake really gives),
   every number drawn in a picture, the recap numbers.
2. Every exam question (pq) shows all the givens its answer uses; the answer uses only those and what the lesson showed.
3. Every claim is in the book or follows from it; no overstated facts (keep the book's conditions, "for every", "sufficient").
4. Pictures agree with the narration and their own numbers. No college names, no unit, chapter or lesson numbers.
Known already from the writers (check and fix): book 2.4 worked example step 1 prints 2qεSi·NA = 3.31e-16, it is 3.33e-16
(lesson shows 3.33); book 3.4 "Here d is the path delay" should be D; book 1.6.1 figure labels "field VDD/L" and "10 V/µm"
overlap; books 1.8 and 2.4 say "only a few universities teach" (reword without universities); u2-L3 Q3 model answer's
area-and-yield point is not in the chapter text; u6-L3 Q2 asks about MATS+, which the lesson shows only in the hint;
u5-L3 and u4-L3 swapped a generated question for another from the book. Many writers re-cut book figures: check each
bookfig against the book.

Fix every must-fix item in the lesson .js, rebuild with `lesson_build.py --revoice` (only changed lines are voiced; set
up Kokoro and the fonts as the ufe-unit-lessons skill says), rerun --check, `cuecheck.py` and `lesson_sheet.py --frames
--play`, and push a new commit to the same `lesson/<id>` branch (keep the folder layout and names). Where the book is
wrong too, fix the book on main and rerun `python3 pack/check_book.py <book> packets/<unit>.json --render`.
Log the findings in `pipeline/SLOP.md` under "VLSI Design fact review (Nov 2026)", in the style of the rows there.

Hand back in under 20 lines by messaging the thread "Build 8 new exam subjects" (thread id
cmsg_01VwvcZRx1mMD7zJQeF8gbhCHJ7d555QwKT2VRz537cmu9): per lesson, the findings and fixed / not fixed, the new commits,
any book fixes. Do not write to /mnt/project-files or the person's computer, and do not message the person.
