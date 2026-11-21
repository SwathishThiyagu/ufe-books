> **Superseded 21 Nov 2026.** Department lessons now use the split blueprint t16 (owner-approved). Follow
> `pipeline/lessons/DEPT_THUMBNAILS.md` and the skill ufe-t16-thumbnails, not this brief. Kept for history only.

# t16 thumbnails (cubes style, Stage look) for the 24 VLSI Design lessons

One thread, Opus high. Follow the ufe-t16-thumbnails skill; the style is cubes (STYLE_OF in t16.py lists only CSE ids,
so pass the style explicitly) in the approved Stage look.

Inputs:
- the cubes code the CSE threads built, in the shared folder `/mnt/project-files/06_Deliver/t16/cubes/src/`
  (`run.py`, `h.py`, `draw.py`, `kit.py`, `blocks.py`, and `specs_d.py` (Digital logic) as the closest model: one small
  drawing per lesson from that lesson's own book figure and numbers, plus a chip). Read only; copy it to your scratchpad.
  Look at the finished samples in `/mnt/project-files/06_Deliver/t16/cubes/samples_stage/` and `c-digital_t16_sheet.jpg`.
- the Stage recipe `/mnt/project-files/06_Deliver/t16/stage_bg_recipe.md` and the logo `/mnt/project-files/06_Deliver/t16/logo_tight.png`.
- `t16.py` from the data pack (https://claude.ai/artifact/9j8tUxjFNfcEit4ZGerNpN, path thumbs/t16.py).
- branch `deliver/ec-vlsi` of SwathishThiyagu/ufe-books: `ec-vlsi/thumbs.json` (subject, topic, hook per lesson;
  the hooks are final) and `ec-vlsi/thumbnail/` (the other three thumbnails, for reference). That branch is being made
  now by the finishing thread: if it is not there yet, wait for it (check every 10 minutes) before step "Render".
- the lessons on branches `lesson/ec-vlsi-uN-Lk` and the books `books/ece/ec-vlsi/` on main, for the figures and numbers.

Write `specs_vlsi.py` (S['ec-vlsi-uN-Lk'] = fn, as specs_d.py does) for all 24 lessons: transistor cross-sections,
I-V and transfer curves, gate and transistor schematics, stick diagrams, adders, memory cells, scan chains, every value computed in python from
the lesson. Render with run.py and t16.py (style cubes, your specs module). It must report no FIX lines. Look at t16_sheet.jpg
and at three thumbnails at full size.

Deliver: commit `ec-vlsi/t16/` (the 24 `<lesson>_t16.jpg`, `t16_sheet.jpg`, `specs_vlsi.py`) and the updated
`ec-vlsi/thumbs.json` to the branch `deliver/ec-vlsi` and push. Do not write to /mnt/project-files or the
person's computer, and do not message the person. Hand back in under 10 lines by messaging the thread
"Build 8 new exam subjects" (thread id cmsg_01VwvcZRx1mMD7zJQeF8gbhCHJ7d555QwKT2VRz537cmu9): the commit, what each
drawing shows in a few words, and anything that did not fit.
