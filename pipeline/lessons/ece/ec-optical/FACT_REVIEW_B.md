# Fact review: Optical Fiber Communication lessons (units 4 to 6), ufe-subject-pipeline step 3a

One thread, Opus high. You did not write these lessons: review them as a stranger would.

Inputs (repo SwathishThiyagu/ufe-books, clone with push access):
- the 9 lessons, each on its orphan branch `lesson/<id>` (folder `<id>/` with html, mp3, words.json, final .js, .pron.json, sheet png):
  ec-optical-u4-L1, ec-optical-u4-L2, ec-optical-u4-L3, ec-optical-u5-L1, ec-optical-u5-L2, ec-optical-u6-L1, ec-optical-u6-L2, ec-optical-u6-L3, ec-optical-u6-L4
- the library books `books/ece/ec-optical/ec-optical-u4.html`, `books/ece/ec-optical/ec-optical-u5.html`, `books/ece/ec-optical/ec-optical-u6.html` on main (the lessons may say only what these say)
- the engine `pipeline/lessons/engine/` (v4.6), `pipeline/SLOP.md` (the audit rules, section C is yours)

For every lesson, read the final .js and look at its sheet once:
1. Recompute in python every worked example (every calc stage), every model answer, both exam traps (the "Don't write"
   must be false under every common convention, and the stated wrong result must be what the mistake really gives),
   every number drawn in a picture, the recap numbers.
2. Every exam question (pq) shows all the givens its answer uses; the answer uses only those and what the lesson showed.
3. Every claim is in the book or follows from it; no overstated facts (keep the book's conditions, "for every", "sufficient").
4. Pictures agree with the narration and their own numbers. No college names, no unit, chapter or lesson numbers.
Known already from the writers (check each, then fix it in the book on main; the lessons did not use the wrong values):
- ec-optical-u5 5.1(b): '96 % of it thermal' should be 95 % (2.65/2.77 = 0.954).
- ec-optical-u5 5.4 WE2: 357 MHz·km comes from the unrounded 178.3 (178 × 2 = 356): print 178.3 or 356 so the rounding matches (nit).
- ec-optical u4 (and u5, u6 if present): 'Only a few universities teach ...' sentences: reword without universities ('Some syllabi cover this ...'), in the books and any lesson.
- ec-optical-u6-L4 and L3 writers rewrote truncated generator figure titles ('switchin'): check every figure title and caption on screen is whole.
- Every lesson: the sources note on the notes/description has been garbled by the generator in other subjects (cut titles, wrong book credited); check it against the book's sources list.
Many writers re-cut book figures and wrote their own pictures: check each bookfig against the book and every picture's numbers.

Fix every must-fix item in the lesson .js, rebuild with `lesson_build.py --revoice` (only changed lines are voiced; set
up Kokoro and the fonts as the ufe-unit-lessons skill says; `pip install playwright==1.63.0` if Chromium is missing),
rerun --check, `cuecheck.py` and `lesson_sheet.py --frames --play`, and push a new commit to the same `lesson/<id>` branch
(keep the folder layout and names). Where the book is wrong, fix the book on main (a targeted fix, never a rewrite) and
rerun `python3 pack/check_book.py <book> packets/<unit>.json --render`.
Log the findings in `pipeline/SLOP.md` under "Optical Fiber Communication fact review B (Nov 2026)", in the style of the rows there.

Git: fetch single branches (`git fetch --depth 1 origin lesson/<id>`); a full fetch stalls on the lesson branches. Review A (units 1 to 3) runs at the same time and also writes SLOP.md and main: push book and SLOP commits straight to main; if the push is rejected, fetch main, merge (keep both SLOP sections), rerun the checker on your books and push again. Never force-push.

Hand back in under 20 lines by messaging the thread "Build three ECE communication subjects" (thread id
cmsg_01VwvcZRx1mMD7zJQeF8gbhCCumGwwGnSucYHrGS8SFv6V): per lesson, the findings and fixed / not fixed, the new commits,
any book fixes. Do not write to /mnt/project-files or the person's computer, and do not message the person.
