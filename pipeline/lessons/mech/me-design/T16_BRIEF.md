> **Superseded 21 Nov 2026.** Department lessons now use the split blueprint t16 (owner-approved). Follow
> `pipeline/lessons/DEPT_THUMBNAILS.md` and the skill ufe-t16-thumbnails, not this brief. Kept for history only.

# t16 thumbnails (phone style, Stage look) for the 22 Machine Design lessons

One thread, Opus high. Follow the ufe-t16-thumbnails skill; the style is phone (STYLE_OF in t16.py lists only CSE ids,
so pass the style explicitly) in the approved Stage look.

Inputs:
- the phone style is drawn by `t16.py` itself (r_phone): per lesson you only write the `t16` block in thumbs.json
  ("title" up to 14 characters, 3 to 6 "rows" of up to 14 characters each, "on" = the lit row), taken from that lesson's
  own parts, worked examples or key terms. Look at a finished phone sheet from the CSE subjects if one is in
  `/mnt/project-files/06_Deliver/t16/` (read only), and apply the approved Stage look as the recipe says.
- the Stage recipe `/mnt/project-files/06_Deliver/t16/stage_bg_recipe.md` and the logo `/mnt/project-files/06_Deliver/t16/logo_tight.png`.
- `t16.py` from the data pack (https://claude.ai/artifact/9j8tUxjFNfcEit4ZGerNpN, path thumbs/t16.py).
- branch `deliver/me-design` of SwathishThiyagu/ufe-books: `me-design/thumbs.json` (subject, topic, hook per lesson;
  the hooks are final) and `me-design/thumbnail/` (the other three thumbnails, for reference). That branch is made by the finishing thread: if it is not there yet, wait for it (check every 10 minutes) before step "Render".
- the lessons on branches `lesson/me-design-uN-Lk` and the books `books/mech/me-design/` on main, for the figures and numbers.

Fill the t16 block for all 22 lessons (style "phone"), render with t16.py, and fix every FIX line. Look at t16_sheet.jpg
and at three thumbnails at full size: no unit or lesson numbers, no college names, rows readable at phone size.

Deliver: commit `me-design/t16/` (the 22 `<lesson>_t16.jpg`, `t16_sheet.jpg`) and the updated
`me-design/thumbs.json` to the branch `deliver/me-design` and push. Do not write to /mnt/project-files or the
person's computer, and do not message the person. Hand back in under 10 lines by messaging the thread
"Build 8 new exam subjects" (thread id cmsg_01VwvcZRx1mMD7zJQeF8gbhCHJ7d555QwKT2VRz537cmu9): the commit, what each
drawing shows in a few words, and anything that did not fit.
