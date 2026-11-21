# Fact review: Internal Combustion Engines lessons (25), ufe-subject-pipeline step 3a

One thread, Opus high. You did not write these lessons: review them as a stranger would.

Inputs (repo SwathishThiyagu/ufe-books, clone with push access):
- the 25 lessons, each on its orphan branch `lesson/<id>` (folder `<id>/` with html, mp3, words.json, final .js, .pron.json, sheet png):
  me-ic-u1-L1 to u1-L4, u2-L1 to u2-L5, u3-L1 to u3-L4, u4-L1 to u4-L3, u5-L1 to u5-L4, u6-L1 to u6-L5
- the library books `books/mech/me-ic/me-ic-u1..u6.html` on main (the lessons may say only what these say)
- the engine `pipeline/lessons/engine/` (v4.6), `pipeline/SLOP.md` (the audit rules, section C is yours)

For every lesson, read the final .js and look at its sheet once:
1. Recompute in python every worked example (every calc stage), every model answer, both exam traps (the "Don't write"
   must be false under every common convention, and the stated wrong result must be what the mistake really gives),
   every number drawn in a picture, the recap numbers.
2. Every exam question (pq) shows all the givens its answer uses; the answer uses only those and what the lesson showed.
3. Every claim is in the book or follows from it; no overstated facts (keep the book's conditions, "for every", "sufficient").
4. Pictures agree with the narration and their own numbers. No college names, no unit, chapter or lesson numbers.
Known already from the writers (verify, then fix the book; the lessons already show the right value unless noted):
- u1: 1.7 trap "80.4 = 2.297" lost its superscript (8^0.4); Fig 1.3.1 crankcase wall unbroken at the inlet port.
- u2: Fig 2.2.1 and Fig 2.11.1 have stroke-dasharray:True (invalid); Fig 2.11.1 "72°: impossible advance" should read
  "58° advance (72° spark to peak)"; 2.7 multi-hole "3 to 10" vs Remember answer "3 to 8", pintle "IDI chambers" vs
  "older small DI and IDI"; 2.7 Apply question "Δp0.25" lost its superscript.
- u3: 3.3 worked example (b) "about 8 % more fuel" is about 9 % (44/40.4); 3.7 answer 29 % is 28.4 %, 45 % is 44.4 %;
  Fig 3.1.1 "III: afterburning" overlaps "C: 50.3 bar" and the motoring label runs off the right edge; Fig 3.4.1 knock
  arrow points at the pre-ignition curve and its label crosses the spark line.
- u4: 4.2 says "a few universities"; 4.2 cap paragraph ends mid-sentence; Fig 4.3.1 "motoring test ... indicated power
  30 kW" (IP comes from the firing test); 4.7 typo "interfere; Lightweight".
- u5: 5.3 sentence repeats "to 13.5 to 13.5 ..." (should end "near 12.5 to 13.5"); 5.5 "only a few universities";
  5.6 worked example 14.31 % vs 14.325 %; 5.7 worked example 2 9.5^0.4 = 2.4606 is 2.4609; Willans caption says
  worked example 2.
- u6: glossary three-way catalyst "λ = 16.3" should be λ = 1 (A/F 14.7); 6.3 step 5 rounding (0.1472/0.8528);
  6.4 example 2 "6 %" is 6.6 %; Fig 6.x "200 kW" on the EGR loop belongs to the SCR example; 6.6 example 2 and Fig 6.6.1
  note 503 MJ / 11.4 kg should be 504 MJ / 11.45 kg; 6.8 and 6.9 name brands (Honda CVCC, Texaco TCCS, Ford PROCO, a
  maker's SPCCI): reword as generic types; 6.8 heads two examples "Worked example 2"; Fig 6.10.1 mirror drawn "/"
  should be "\".
Lessons, must check: me-ic-u6-L5's next card names the next unit's lesson, but it is the last lesson of the subject:
use "Revise from the start: <first chapter title>" as ec-signals-u6-L3 does. me-ic-u5-L1 Q3 "weaker mixture at light
load" (true for CI, not throttled SI). me-ic-u4-L2 is 884 words (limit 880; trim only if you rebuild it anyway).

Fix every must-fix item in the lesson .js, rebuild with `lesson_build.py --revoice` (only changed lines are voiced; set
up Kokoro and the fonts as the ufe-unit-lessons skill says), rerun --check, `cuecheck.py` and `lesson_sheet.py --frames
--play`, and push a new commit to the same `lesson/<id>` branch (keep the folder layout and names). Where the book is
wrong too, fix the book on main and rerun `python3 pack/check_book.py <book> packets/<unit>.json --render`.
Log the findings in `pipeline/SLOP.md` under "Internal Combustion Engines fact review (Nov 2026)", in the style of the rows there.

Hand back in under 20 lines by messaging the thread "Build 8 new exam subjects" (thread id
cmsg_01VwvcZRx1mMD7zJQeF8gbhCHJ7d555QwKT2VRz537cmu9): per lesson, the findings and fixed / not fixed, the new commits,
any book fixes. Do not write to /mnt/project-files or the person's computer, and do not message the person.
