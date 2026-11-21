# Fact review: Automotive Electrical and Electronics lessons (25), ufe-subject-pipeline step 3a

One thread, Opus high. You did not write these lessons: review them as a stranger would.

Inputs (repo SwathishThiyagu/ufe-books, clone with push access):
- the 25 lessons, each on its orphan branch `lesson/<id>` (folder `<id>/` with html, mp3, words.json, final .js, .pron.json, sheet png):
  au-elec-u1-L1 to u1-L4, u2-L1 to u2-L4, u3-L1 to u3-L6, u4-L1 to u4-L3, u5-L1 to u5-L3, u6-L1 to u6-L5
- the library books `books/auto/au-elec/au-elec-u1..u6.html` on main (the lessons may say only what these say)
- the engine `pipeline/lessons/engine/` (v4.6), `pipeline/SLOP.md` (the audit rules, section C is yours)

For every lesson, read the final .js and look at its sheet once:
1. Recompute in python every worked example (every calc stage), every model answer, both exam traps (the "Don't write"
   must be false under every common convention, and the stated wrong result must be what the mistake really gives),
   every number drawn in a picture, the recap numbers.
2. Every exam question (pq) shows all the givens its answer uses; the answer uses only those and what the lesson showed.
3. Every claim is in the book or follows from it; no overstated facts (keep the book's conditions, "for every", "sufficient").
   Standards and protocols (CAN, CAN FD, LIN, FlexRay, MOST, OBD-II, ISO 26262, MISRA, DSRC/802.11p, Bharat Stage, Euro)
   must carry the book's numbers exactly: bit rates, payload sizes, voltage levels, ASIL letters, band and channel widths.
4. Pictures agree with the narration and their own numbers. No college names, city names, unit, chapter or lesson numbers.
Known already from the writers (verify, then fix the book; the lessons already show the right value unless noted):
- u1: worked example 14,100 V comes from the rounded 0.141 A (exact 14,118 V); Fig 1.6.1 the dashed sense wire ends
  below the battery's negative plate (it should reach the + lead); 1.11 "Only a few universities teach the EV traction part".
- u2: worked example 2 "51.2 mJ" uses the unrounded 3.578 A (3.58 A gives 51.3 mJ: print 3.578 or 51.3); the leads of
  2.5 to 2.7 and two more chapters say "Only a few universities teach this topic / this grouping / as a separate topic".
- u3: 3.6 worked example 4 round(0.545 × 1023 / 5) = 111 is off by one as written (0.545 V gives 111.5; the exact
  0.5449 V gives 111.49): make the printed input and count agree; Fig 3.4.1 pulse train runs past the viewBox (x 733 > 720);
  the unit intro and 3.12 say "only a few universities teach"; the 3.12 Analyze question names Chennai (say "slow city traffic").
- u4: 4.3 BSFC 11.5 × 1000 / 47.12 printed as 244.04 (it is 244.06; 244.04 needs 47.124); a lead says "Only a few
  universities teach it in depth".
- u5: Fig 5.4.1 "ABS band" overlaps the λ label; Fig 5.6.1 the −800 tick overlaps the case 1 label; 5.6 and the ADAS
  and tuning chapters say "only a few universities"; 5.9 worked example 2 "peak force falls to about 3550 N" is the force
  at t = 3 s (the true peak is about 3573 N at 3.75 s).
- u6: the unit intro and the 6.9 and 6.10 leads (and one more, "this stack") say "Only a few universities teach this in depth".
Every "few universities" sentence in the books (14 across u1 to u6) is a college-type reference students see: reword each
as a plain scope note ("This goes beyond most exam syllabi" or simply drop it) and check no lesson narrates one.
Lessons, must check: au-elec-u6-L4's next card is split wrongly at a comma (["VANET architecture", "applications and
routing · DSRC, ..."]): it should read ["NEXT TIME", "Next lesson", "VANET architecture, applications and routing · DSRC,
IEEE 802.11p and WAVE", "book"]. au-elec-u6-L5's next card already reads "Revise from the start: Evolution of
electronics in automobiles" (keep it). au-elec-u3-L6 ADC / SOC / SOH need pron entries (the check does not flag them);
au-elec-u6-L2 part-2 points were cut mid-phrase; au-elec-u1-L1 worked example 1 began as a notebook stub (made calc):
recheck its numbers. Several writers found the figs source notes garbled and rewrote them: confirm each picture's
source note now names the right book figure.

Fix every must-fix item in the lesson .js, rebuild with `lesson_build.py --revoice` (only changed lines are voiced; set
up Kokoro and the fonts as the ufe-unit-lessons skill says), rerun --check, `cuecheck.py` and `lesson_sheet.py --frames
--play`, and push a new commit to the same `lesson/<id>` branch (keep the folder layout and names). Where the book is
wrong too, fix the book on main and rerun `python3 pack/check_book.py <book> packets/<unit>.json --render`.
Log the findings in `pipeline/SLOP.md` under "Automotive Electrical and Electronics fact review (Nov 2026)", in the style of the rows there.

Hand back in under 20 lines by messaging the thread "Build 8 new exam subjects" (thread id
cmsg_01VwvcZRx1mMD7zJQeF8gbhCHJ7d555QwKT2VRz537cmu9): per lesson, the findings and fixed / not fixed, the new commits,
any book fixes. Do not write to /mnt/project-files or the person's computer, and do not message the person.
