# Fact review: Analog and Digital Communication lessons (units 1 to 4), ufe-subject-pipeline step 3a

One thread, Opus high. You did not write these lessons: review them as a stranger would.

Inputs (repo SwathishThiyagu/ufe-books, clone with push access):
- the 15 lessons, each on its orphan branch `lesson/<id>` (folder `<id>/` with html, mp3, words.json, final .js, .pron.json, sheet png):
  ec-comm-u1-L1, ec-comm-u1-L2, ec-comm-u1-L3, ec-comm-u2-L1, ec-comm-u2-L2, ec-comm-u2-L3, ec-comm-u2-L4, ec-comm-u3-L1, ec-comm-u3-L2, ec-comm-u3-L3, ec-comm-u3-L4, ec-comm-u4-L1, ec-comm-u4-L2, ec-comm-u4-L3, ec-comm-u4-L4
- the library books `books/ece/ec-comm/ec-comm-u1.html`, `books/ece/ec-comm/ec-comm-u2.html`, `books/ece/ec-comm/ec-comm-u3.html`, `books/ece/ec-comm/ec-comm-u4.html` on main (the lessons may say only what these say)
- the engine `pipeline/lessons/engine/` (v4.6), `pipeline/SLOP.md` (the audit rules, section C is yours)

For every lesson, read the final .js and look at its sheet once:
1. Recompute in python every worked example (every calc stage), every model answer, both exam traps (the "Don't write"
   must be false under every common convention, and the stated wrong result must be what the mistake really gives),
   every number drawn in a picture, the recap numbers.
2. Every exam question (pq) shows all the givens its answer uses; the answer uses only those and what the lesson showed.
3. Every claim is in the book or follows from it; no overstated facts (keep the book's conditions, "for every", "sufficient").
4. Pictures agree with the narration and their own numbers. No college names, no unit, chapter or lesson numbers.
Known already from the writers (check each, then fix it in the book on main; the lessons did not use the wrong values):
- ec-comm-u4 4.8 Worked example 2 (from the u4-L4 writer): AMI total power is V²/4, not V²/2 (half the bits are 1s, half-width pulses); AMI share below its first null is 79.6 %, not 85.6 %; polar RZ 90.3 % not 90.4 %; Manchester 85.6 % not 85.7 % (verify numerically, then fix the book).
- ec-comm-u1 Figure 1.3.1: superscript −j2πfct lacks the subscript on c (cosmetic).
- ec-comm-u4 4.3 WE2 and its figure label: mu-law y(0.01) = 0.2285 -> 0.228, not 0.229.
- ec-comm-u1 1.6 WE2: sqrt(32.0 + 80.0) printed as 10.59; show 32.02 + 80.05 so the rounding matches (nit).
- ec-comm-u3 Fig 3.6.1: the beta = 5 threshold label box sits over the beta = 2 line (cosmetic).
- ec-comm-u3 Fig 3.2.1: labels n = +4 but not n = -4; subscripts use baseline-shift=sub (too low) (cosmetic).
Many writers re-cut book figures and wrote their own pictures: check each bookfig against the book and every picture's numbers.

Fix every must-fix item in the lesson .js, rebuild with `lesson_build.py --revoice` (only changed lines are voiced; set
up Kokoro and the fonts as the ufe-unit-lessons skill says; `pip install playwright==1.63.0` if Chromium is missing),
rerun --check, `cuecheck.py` and `lesson_sheet.py --frames --play`, and push a new commit to the same `lesson/<id>` branch
(keep the folder layout and names). Where the book is wrong, fix the book on main (a targeted fix, never a rewrite) and
rerun `python3 pack/check_book.py <book> packets/<unit>.json --render`.
Log the findings in `pipeline/SLOP.md` under "Analog and Digital Communication fact review (Nov 2026)", in the style of the rows there.

Hand back in under 20 lines by messaging the thread "Build three ECE communication subjects" (thread id
cmsg_01VwvcZRx1mMD7zJQeF8gbhCCumGwwGnSucYHrGS8SFv6V): per lesson, the findings and fixed / not fixed, the new commits,
any book fixes. Do not write to /mnt/project-files or the person's computer, and do not message the person.
