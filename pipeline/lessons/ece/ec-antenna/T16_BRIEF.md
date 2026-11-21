# t16 thumbnails (emboss style, Stage look) for the 20 Antennas, RF and Microwave Engineering lessons

One thread, Opus high. Follow the ufe-t16-thumbnails skill; the style is emboss (STYLE_OF in t16.py lists only CSE ids,
so add 'ec-antenna': 'emboss' to STYLE_OF in your copy and commit that patched t16.py) in the approved Stage look.
Circuit Theory and Automotive Electrical were built in the same emboss look (branches deliver/ec-circuits and deliver/au-elec,
folders <sid>/t16/): reuse their renderer changes.

Inputs:
- the approved emboss Stage look: `/mnt/project-files/06_Deliver/t16/emboss_stage/<id>/` for six CSE subjects (read only),
  with three samples in `/mnt/project-files/06_Deliver/t16/emboss/samples_stage/`. Their thumbs.json `e2` blocks show the
  drawing those used (nodes with a value and a small sub label, lit/ok/dim states, labelled links, texts, a caption with
  one bold phrase, extra svg). `t16.py`'s own r_emboss draws the simpler {nodes, edges, tape, head} block; if it has no
  `e2` path, extend r_emboss in your scratchpad copy so it draws `e2` blocks to match those samples, and say so.
- the Stage recipe `/mnt/project-files/06_Deliver/t16/stage_bg_recipe.md` and the logo `/mnt/project-files/06_Deliver/t16/logo_tight.png`.
- `t16.py` from the data pack (https://claude.ai/artifact/9j8tUxjFNfcEit4ZGerNpN, path thumbs/t16.py).
- branch `deliver/ec-antenna` of SwathishThiyagu/ufe-books: `ec-antenna/thumbnail/thumbs.json` (subject, topic, hook per lesson;
  the hooks are final) and `ec-antenna/thumbnail/` (the other three thumbnails, for reference). That branch is made by the
  finishing thread: if it is not there yet, wait for it (check every 10 minutes) before step "Render".
- the lessons on branches `lesson/ec-antenna-uN-Lk` and the books `books/ece/ec-antenna/` on main, for the figures and numbers.

Per lesson, 2 to 4 raised circles joined by arrows, taken from that lesson's own content and numbers: a line
from source to load with Z0, ZL and the VSWR, Smith-chart steps (normalise, rotate, read), waveguide modes with their
cutoff, a microwave tee's ports with the S-parameter on each link, an antenna to array to beam chain, a receiver chain
(LNA, mixer, IF) with gain and noise figure, a radar pulse out and back with the range; the tape is
the sequence or the values, `head` the step the hook is about. Every value computed in python from the lesson. Render with t16.py; it must report no FIX lines.
Fetch single branches with --depth 1. Look at t16_sheet.jpg and at three thumbnails at full size: no unit or lesson numbers, no college or city names,
labels readable at phone size.

Deliver: commit `ec-antenna/t16/` (the 22 `<lesson>_t16.jpg`, `t16_sheet.jpg`, and your renderer changes if any) and the
updated `ec-antenna/thumbnail/thumbs.json` to the branch `deliver/ec-antenna` and push. The owner sees the sheet before anything is saved to their computer. Do not write to /mnt/project-files or the
person's computer, and do not message the person. Hand back in under 10 lines by messaging the thread
"Build three ECE communication subjects" (thread id cmsg_01VwvcZRx1mMD7zJQeF8gbhCCumGwwGnSucYHrGS8SFv6V): the commit, what each
drawing shows in a few words, and anything that did not fit.
