# t16 thumbnails (emboss style, Stage look) for the 25 Automotive Electrical and Electronics lessons

One thread, Opus high. Follow the ufe-t16-thumbnails skill; the style is emboss (STYLE_OF in t16.py lists only CSE ids,
so pass the style explicitly) in the approved Stage look. This is the first emboss sheet for a non-CSE subject: the
person sees it before it is saved, so make it right on the first pass.

Inputs:
- the approved emboss Stage look: `/mnt/project-files/06_Deliver/t16/emboss_stage/<id>/` for six CSE subjects (read only),
  with three samples in `/mnt/project-files/06_Deliver/t16/emboss/samples_stage/`. Their thumbs.json `e2` blocks show the
  drawing those used (nodes with a value and a small sub label, lit/ok/dim states, labelled links, texts, a caption with
  one bold phrase, extra svg). `t16.py`'s own r_emboss draws the simpler {nodes, edges, tape, head} block; if it has no
  `e2` path, extend r_emboss in your scratchpad copy so it draws `e2` blocks to match those samples, and say so.
- the Stage recipe `/mnt/project-files/06_Deliver/t16/stage_bg_recipe.md` and the logo `/mnt/project-files/06_Deliver/t16/logo_tight.png`.
- `t16.py` from the data pack (https://claude.ai/artifact/9j8tUxjFNfcEit4ZGerNpN, path thumbs/t16.py).
- branch `deliver/au-elec` of SwathishThiyagu/ufe-books: `au-elec/thumbs.json` (subject, topic, hook per lesson;
  the hooks are final) and `au-elec/thumbnail/` (the other three thumbnails, for reference). That branch is made by the
  finishing thread: if it is not there yet, wait for it (check every 10 minutes) before step "Render".
- the lessons on branches `lesson/au-elec-uN-Lk` and the books `books/auto/au-elec/` on main, for the figures and numbers.

Per lesson, 2 to 4 raised circles joined by arrows, taken from that lesson's own content and numbers: a signal chain
(sensor, ECU, actuator), battery, alternator and regulator, coil primary to secondary with the kV, CAN nodes on a bus with
the bit rate, ABS wheel-speed to modulator, ignition timing steps; the tape is the sequence or the values, `head` the
step the hook is about. Every value computed in python from the lesson. Render with t16.py; it must report no FIX lines.
Look at t16_sheet.jpg and at three thumbnails at full size: no unit or lesson numbers, no college or city names,
labels readable at phone size.

Deliver: commit `au-elec/t16/` (the 25 `<lesson>_t16.jpg`, `t16_sheet.jpg`, and your renderer changes if any) and the
updated `au-elec/thumbs.json` to the branch `deliver/au-elec` and push. Do not write to /mnt/project-files or the
person's computer, and do not message the person. Hand back in under 10 lines by messaging the thread
"Build 8 new exam subjects" (thread id cmsg_01VwvcZRx1mMD7zJQeF8gbhCHJ7d555QwKT2VRz537cmu9): the commit, what each
drawing shows in a few words, and anything that did not fit.
