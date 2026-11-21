# Fact review: Analog and Digital Communication lessons (units 5 to 7), ufe-subject-pipeline step 3a

One thread, Opus high. You did not write these lessons: review them as a stranger would.

Inputs (repo SwathishThiyagu/ufe-books, clone with push access):
- the 9 lessons, each on its orphan branch `lesson/<id>` (folder `<id>/` with html, mp3, words.json, final .js, .pron.json, sheet png):
  ec-comm-u5-L1, ec-comm-u5-L2, ec-comm-u5-L3, ec-comm-u6-L1, ec-comm-u6-L2, ec-comm-u6-L3, ec-comm-u7-L1, ec-comm-u7-L2, ec-comm-u7-L3
- the library books `books/ece/ec-comm/ec-comm-u5.html`, `books/ece/ec-comm/ec-comm-u6.html`, `books/ece/ec-comm/ec-comm-u7.html` on main (the lessons may say only what these say)
- the engine `pipeline/lessons/engine/` (v4.6), `pipeline/SLOP.md` (the audit rules, section C is yours)

For every lesson, read the final .js and look at its sheet once:
1. Recompute in python every worked example (every calc stage), every model answer, both exam traps (the "Don't write"
   must be false under every common convention, and the stated wrong result must be what the mistake really gives),
   every number drawn in a picture, the recap numbers.
2. Every exam question (pq) shows all the givens its answer uses; the answer uses only those and what the lesson showed.
3. Every claim is in the book or follows from it; no overstated facts (keep the book's conditions, "for every", "sufficient").
4. Pictures agree with the narration and their own numbers. No college names, no unit, chapter or lesson numbers.
Known already from the writers (check each, then fix it in the book on main; the lessons did not use the wrong values):
- ec-comm-u7 7.3 Check yourself "Why must I lie between 0 and min": "I >= 0 because it is an average of non-negative information terms" is wrong (the pointwise terms can be negative); give the right reason (conditioning cannot raise average uncertainty, or Jensen / Gibbs).
- ec-comm-u5 5.6 worked example: the extracted text reads "1010/10" for 10^(10/10); check that the rendered book shows the superscript (a raw or lost sup tag), and fix it if not.
- ec-comm-u5 Fig 5.2.1: the label "opening 2 (noise margin)" crosses the eye frame: move it (cosmetic).
- u5-L1, u6-L1, u6-L2 writers fixed a garbled generator sources line ("Simon Haykin (spread spectrum and multicarrier modulation.)"); check the others.
- Every lesson: the sources note on the notes/description has been garbled by the generator in other subjects (cut titles, wrong book credited); check it against the book's sources list.
Many writers re-cut book figures and wrote their own pictures: check each bookfig against the book and every picture's numbers.

Fix every must-fix item in the lesson .js, rebuild with `lesson_build.py --revoice` (only changed lines are voiced; set
up Kokoro and the fonts as the ufe-unit-lessons skill says; `pip install playwright==1.63.0` if Chromium is missing),
rerun --check, `cuecheck.py` and `lesson_sheet.py --frames --play`, and push a new commit to the same `lesson/<id>` branch
(keep the folder layout and names). Where the book is wrong, fix the book on main (a targeted fix, never a rewrite) and
rerun `python3 pack/check_book.py <book> packets/<unit>.json --render`.
Log the findings in `pipeline/SLOP.md` under "Analog and Digital Communication fact review B (Nov 2026)", in the style of the rows there.

Git: fetch single branches (`git fetch --depth 1 origin lesson/<id>`); a full fetch stalls on the lesson branches. The Optical and Antennas reviews run at the same time and also write SLOP.md and main: push book and SLOP commits straight to main; if the push is rejected, fetch main, merge (keep both SLOP sections), rerun the checker on your books and push again. Never force-push.

Hand back in under 20 lines by messaging the thread "Build three ECE communication subjects" (thread id
cmsg_01VwvcZRx1mMD7zJQeF8gbhCCumGwwGnSucYHrGS8SFv6V): per lesson, the findings and fixed / not fixed, the new commits,
any book fixes. Do not write to /mnt/project-files or the person's computer, and do not message the person.
