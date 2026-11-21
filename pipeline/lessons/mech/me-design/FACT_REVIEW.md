# Fact review: Machine Design lessons (22), ufe-subject-pipeline step 3a

One thread, Opus high. You did not write these lessons: review them as a stranger would.

Inputs (repo SwathishThiyagu/ufe-books, clone with push access):
- the 22 lessons, each on its orphan branch `lesson/<id>` (folder `<id>/` with html, mp3, words.json, final .js, .pron.json, sheet png):
  me-design-u1-L1 to u1-L3, u2-L1 u2-L2, u3-L1 to u3-L3, u4-L1 to u4-L5, u5-L1 to u5-L4, u6-L1 u6-L2, u7-L1 to u7-L3
- the library books `books/mech/me-design/me-design-u1..u7.html` on main (the lessons may say only what these say)
- the engine `pipeline/lessons/engine/` (v4.6), `pipeline/SLOP.md` (the audit rules, section C is yours)

For every lesson, read the final .js and look at its sheet once:
1. Recompute in python every worked example (every calc stage), every model answer, both exam traps (the "Don't write"
   must be false under every common convention, and the stated wrong result must be what the mistake really gives),
   every number drawn in a picture, the recap numbers.
2. Every exam question (pq) shows all the givens its answer uses; the answer uses only those and what the lesson showed.
3. Every claim is in the book or follows from it; no overstated facts (keep the book's conditions, "for every", "sufficient").
4. Pictures agree with the narration and their own numbers. No college names, no unit, chapter or lesson numbers.
Known already from the writers (verify, then fix the book; the lessons already show the right value):
- u3: 3.6 worked example 1 step 4 prints "456 070/t²" then "456 060": both are 456 670; the Apply answer's
  "3.17 × 64 = 203.2" (3.17 × 64 = 202.88; 203.2 comes from the exact 419/132).
- u4: Fig 4.6.1 label "gap left: 3.9 mm" is 3.7 mm (98 − 73.7 − 70).
- u5: Fig 5.7.1 subscript "req" sits on the next line.
- u7: Fig 7.3.1 colours the failing 6912 N wear bar in the pass green.
Lessons, check: me-design-u5-L2 Q1 model answer argues from magnitude (500² vs 10⁻⁷), not sensitivity; me-design-u1-L3 Q3
was rewritten to show its givens (the book names "the shaft of the direct-stress chapter"); me-design-u6-L2 is 881 words.
Most writers cut worked examples to fit 880 words: the ribbon must match the examples taught.

Fix every must-fix item in the lesson .js, rebuild with `lesson_build.py --revoice` (only changed lines are voiced; set
up Kokoro and the fonts as the ufe-unit-lessons skill says), rerun --check, `cuecheck.py` and `lesson_sheet.py --frames
--play`, and push a new commit to the same `lesson/<id>` branch (keep the folder layout and names). Where the book is
wrong too, fix the book on main and rerun `python3 pack/check_book.py <book> packets/<unit>.json --render`.
Log the findings in `pipeline/SLOP.md` under "Machine Design fact review (Nov 2026)", in the style of the rows there.

Hand back in under 20 lines by messaging the thread "Build 8 new exam subjects" (thread id
cmsg_01VwvcZRx1mMD7zJQeF8gbhCHJ7d555QwKT2VRz537cmu9): per lesson, the findings and fixed / not fixed, the new commits,
any book fixes. Do not write to /mnt/project-files or the person's computer, and do not message the person.
