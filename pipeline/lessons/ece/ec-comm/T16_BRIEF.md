# t16 thumbnails (glass style, Stage look) for Analog and Digital Communication (24 lessons) and Optical Fiber Communication (21 lessons)

One thread, Opus high. Follow the ufe-t16-thumbnails skill; the style is glass for both subjects, in the approved Stage look.
Add the ids to STYLE_OF in your copy of t16.py ('ec-comm': 'glass', 'ec-optical': 'glass') and commit that patched t16.py with the thumbnails, so the style is set by STYLE_OF rather than passed by hand.
Do Analog and Digital Communication first, then Optical Fiber Communication.

Inputs:
- the glass code the AI/ML thread built, in the shared folder `/mnt/project-files/06_Deliver/t16/glass/code/`
  (`render.py`, `gfx.py`, `d_ml.py` as the model: one small hand-drawn SVG per lesson, from that lesson's own book
  figure and numbers, plus a chip). Read only; copy it to your scratchpad. Look at one finished sample,
  `/mnt/project-files/06_Deliver/t16/glass/c-ml/c-ml-u1-L1_t16.jpg`. Signals and Systems is the closest ECE model:
  branch `deliver/ec-signals`, folder `ec-signals/t16/` (`d_signals.py` and the 18 thumbnails).
- the Stage recipe `/mnt/project-files/06_Deliver/t16/stage_bg_recipe.md` and the logo `/mnt/project-files/06_Deliver/t16/logo_tight.png`.
- `t16.py` from the data pack (https://claude.ai/artifact/9j8tUxjFNfcEit4ZGerNpN, path thumbs/t16.py).
- branches `deliver/ec-comm` and `deliver/ec-optical` of SwathishThiyagu/ufe-books: `<sid>/thumbnail/thumbs.json` (subject,
  topic, hook per lesson; the hooks are final) and `<sid>/thumbnail/` (the other three thumbnails, for reference). Those
  branches are made by the finishing threads: if one is not there yet, wait for it (check every 10 minutes) before rendering it.
- the lessons on branches `lesson/<sid>-uN-Lk` and the books `books/ece/<sid>/` on main, for the figures and numbers.
  Fetch single branches with --depth 1 (a full fetch stalls on the lesson branches).

Write `d_comm.py` and `d_optical.py` (D['<sid>-uN-Lk'] = (fn, chip, book figure)) for every lesson. Analog and Digital
Communication: AM and FM waveforms on time axes with the envelope, spectra with sidebands and Carson bandwidth, sampled
stems and quantiser steps, line-code bit rows, eye diagrams, constellations, Huffman trees, trellis paths. Optical: a fiber
cross-section with the acceptance cone, ray paths, index profiles, attenuation against wavelength with the windows, pulse
spreading, LED and laser L-I curves, photodiode response, power-budget bars, WDM combs. Every value computed in python from
the lesson. Render with render.py (map each sid to its module). It must report no FIX lines. Look at each subject's
t16_sheet.jpg and at three thumbnails at full size: no unit or lesson numbers, no college or city names, labels readable at phone size.

Deliver: commit `<sid>/t16/` (the `<lesson>_t16.jpg` files, `t16_sheet.jpg`, the d_ module and the patched t16.py) and the
updated `<sid>/thumbnail/thumbs.json` to the branch `deliver/<sid>` and push, for each subject. The owner sees one sheet
per style before anything is saved to their computer, so hand back as soon as the first subject's sheet is pushed
(a short note), then again when both are done. Do not write to /mnt/project-files or the person's computer, and do not
message the person. Hand back in under 10 lines by messaging the thread "Build three ECE communication subjects" (thread id cmsg_01VwvcZRx1mMD7zJQeF8gbhCCumGwwGnSucYHrGS8SFv6V): the commit, what each drawing shows in a few
words, and anything that did not fit.
