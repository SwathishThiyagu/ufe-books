# t16 thumbnails (glass style, Stage look) for the 18 Signals and Systems lessons

One thread, Opus high. Follow the ufe-t16-thumbnails skill; the style is glass (STYLE_OF in t16.py lists only CSE ids,
so pass the style explicitly) in the approved Stage look.

Inputs:
- the glass code the AI/ML thread built, in the shared folder `/mnt/project-files/06_Deliver/t16/glass/code/`
  (`render.py`, `gfx.py`, `d_ml.py` as the model: one small hand-drawn SVG per lesson, from that lesson's own book
  figure and numbers, plus a chip). Read only; copy it to your scratchpad. Look at one finished sample,
  `/mnt/project-files/06_Deliver/t16/glass/c-ml/c-ml-u1-L1_t16.jpg`.
- the Stage recipe `/mnt/project-files/06_Deliver/t16/stage_bg_recipe.md` and the logo `/mnt/project-files/06_Deliver/t16/logo_tight.png`.
- `t16.py` from the data pack (https://claude.ai/artifact/9j8tUxjFNfcEit4ZGerNpN, path thumbs/t16.py).
- branch `deliver/ec-signals` of SwathishThiyagu/ufe-books: `ec-signals/thumbs.json` (subject, topic, hook per lesson;
  the hooks are final) and `ec-signals/thumbnail/` (the other three thumbnails, for reference).
- the lessons on branches `lesson/ec-signals-uN-Lk` and the books `books/ece/ec-signals/` on main, for the figures and numbers.

Write `d_signals.py` (D['ec-signals-uN-Lk'] = (fn, chip, book figure)) for all 18 lessons: waveforms on time axes
with ticks, spectra, pole-zero plots with the ROC, sampled stems, block diagrams, every value computed in python from
the lesson. Render with render.py (map 'ec-signals' to your module). It must report no FIX lines. Look at t16_sheet.jpg
and at three thumbnails at full size.

Deliver: commit `ec-signals/t16/` (the 18 `<lesson>_t16.jpg`, `t16_sheet.jpg`, `d_signals.py`) and the updated
`ec-signals/thumbs.json` to the branch `deliver/ec-signals` and push. Do not write to /mnt/project-files or the
person's computer, and do not message the person. Hand back in under 10 lines by messaging the thread
"Build 8 new exam subjects" (thread id cmsg_01VwvcZRx1mMD7zJQeF8gbhCHJ7d555QwKT2VRz537cmu9): the commit, what each
drawing shows in a few words, and anything that did not fit.
