# Fact review: Antennas, RF and Microwave Engineering lessons (units 4 and 1), ufe-subject-pipeline step 3a

One thread, Opus high. You did not write these lessons: review them as a stranger would.

Inputs (repo SwathishThiyagu/ufe-books, clone with push access):
- the 7 lessons, each on its orphan branch `lesson/<id>` (folder `<id>/` with html, mp3, words.json, final .js, .pron.json, sheet png):
  ec-antenna-u4-L1, ec-antenna-u4-L2, ec-antenna-u4-L3, ec-antenna-u1-L1, ec-antenna-u1-L2, ec-antenna-u1-L3, ec-antenna-u1-L4
- the library books `books/ece/ec-antenna/ec-antenna-u4.html`, `books/ece/ec-antenna/ec-antenna-u1.html` on main (the lessons may say only what these say)
- the engine `pipeline/lessons/engine/` (v4.6), `pipeline/SLOP.md` (the audit rules, section C is yours)

For every lesson, read the final .js and look at its sheet once:
1. Recompute in python every worked example (every calc stage), every model answer, both exam traps (the "Don't write"
   must be false under every common convention, and the stated wrong result must be what the mistake really gives),
   every number drawn in a picture, the recap numbers.
2. Every exam question (pq) shows all the givens its answer uses; the answer uses only those and what the lesson showed.
3. Every claim is in the book or follows from it; no overstated facts (keep the book's conditions, "for every", "sufficient").
4. Pictures agree with the narration and their own numbers. No college names, no unit, chapter or lesson numbers.
Known already from the writers (check each, then fix it in the book on main; the lessons did not use the wrong values):
- ec-antenna-u1: label backgrounds behind 'VSWR <= 1.5...' and 'matched again at 3f0' are narrower than the text (cosmetic).
- ec-antenna-u4 4.8 WE1: tan 54.27 deg = 1.390, not 1.392 (zL 0.896 - j0.892 already matches 1.390).
- ec-antenna-u1 microstrip W/h = 2 answer: 0.667 ln 3.444 rounded to 0.824 (exact 0.825), so 7.709 should be 7.711; Z0 48.9 ohm unchanged (nit).
- ec-antenna-u1 1.1 trap 'total L of a 20 m cable is wrong by sqrt(20)' holds only if C stays per metre (total L with total C gives the right Z0): reword.
Many writers re-cut book figures and wrote their own pictures: check each bookfig against the book and every picture's numbers.

Fix every must-fix item in the lesson .js, rebuild with `lesson_build.py --revoice` (only changed lines are voiced; set
up Kokoro and the fonts as the ufe-unit-lessons skill says; `pip install playwright==1.63.0` if Chromium is missing),
rerun --check, `cuecheck.py` and `lesson_sheet.py --frames --play`, and push a new commit to the same `lesson/<id>` branch
(keep the folder layout and names). Where the book is wrong, fix the book on main (a targeted fix, never a rewrite) and
rerun `python3 pack/check_book.py <book> packets/<unit>.json --render`.
Log the findings in `pipeline/SLOP.md` under "Antennas, RF and Microwave Engineering fact review (Nov 2026)", in the style of the rows there.

Hand back in under 20 lines by messaging the thread "Build three ECE communication subjects" (thread id
cmsg_01VwvcZRx1mMD7zJQeF8gbhCCumGwwGnSucYHrGS8SFv6V): per lesson, the findings and fixed / not fixed, the new commits,
any book fixes. Do not write to /mnt/project-files or the person's computer, and do not message the person.
