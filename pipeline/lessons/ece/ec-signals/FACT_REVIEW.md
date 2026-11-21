# Fact review: Signals and Systems lessons (18), ufe-subject-pipeline step 3a

One thread, Opus high. You did not write these lessons: review them as a stranger would.

Inputs (repo SwathishThiyagu/ufe-books, clone with push access):
- the 18 lessons, each on its orphan branch `lesson/<id>` (folder `<id>/` with html, mp3, words.json, final .js, .pron.json, sheet png):
  ec-signals-u1-L1 u1-L2 u1-L3 u1-L4, u2-L1 u2-L2 u2-L3, u3-L1 u3-L2 u3-L3, u4-L1 u4-L2, u5-L1 u5-L2 u5-L3, u6-L1 u6-L2 u6-L3
- the library books `books/ece/ec-signals/ec-signals-u1..u6.html` on main (the lessons may say only what these say)
- the engine `pipeline/lessons/engine/` (v4.6), `pipeline/SLOP.md` (the audit rules, section C is yours)

For every lesson, read the final .js and look at its sheet once:
1. Recompute in python every worked example (every calc stage), every model answer, both exam traps (the "Don't write"
   must be false under every common convention, and the stated wrong result must be what the mistake really gives),
   every number drawn in a picture, the recap numbers.
2. Every exam question (pq) shows all the givens its answer uses; the answer uses only those and what the lesson showed.
3. Every claim is in the book or follows from it; no overstated facts (keep the book's conditions, "for every", "sufficient").
4. Pictures agree with the narration and their own numbers. No college names, no unit, chapter or lesson numbers.
Known already: the u1-L1 Q3 "no continuous parent" claim (fixed); u5 book 1 + 3.706^6 = 2591 (fixed on main).

Fix every must-fix item in the lesson .js, rebuild with `lesson_build.py --revoice` (only changed lines are voiced; set
up Kokoro and the fonts as the ufe-unit-lessons skill says), rerun --check, `cuecheck.py` and `lesson_sheet.py --frames
--play`, and push a new commit to the same `lesson/<id>` branch (keep the folder layout and names). Where the book is
wrong too, fix the book on main and rerun `python3 pack/check_book.py <book> packets/<unit>.json --render`.
Log the findings in `pipeline/SLOP.md` under "Signals and Systems fact review (Nov 2026)", in the style of the rows there.

Hand back in under 20 lines by messaging the thread "Build 8 new exam subjects" (thread id
cmsg_01VwvcZRx1mMD7zJQeF8gbhCHJ7d555QwKT2VRz537cmu9): per lesson, the findings and fixed / not fixed, the new commits,
any book fixes. Do not write to /mnt/project-files or the person's computer, and do not message the person.
