# Circuit Theory: notes PDFs, thumbnail (t16 only, split blueprint) and upload sheet

One thread, Opus high. Follow the ufe-subject-pipeline skill from "notes PDFs" on; the lessons and fact review are done.
The model to copy is Signals and Systems: branch `deliver/ec-signals` (folder `ec-signals/`) holds exactly what you
must produce here, and `work/` is never committed.

Inputs (repo SwathishThiyagu/ufe-books):
- the 22 lessons, each on its branch `lesson/ec-circuits-uN-Lk` (folder `ec-circuits-uN-Lk/`); take the html, words.json and sheet
  from the branch tip (the fact review may have pushed new commits: always take the tip).
- `pipeline/lessons/eee/ec-circuits/uN/videos.ec-circuits-uN.json` (from book2lesson) for the lesson list; set each title from the
  lesson's META title and each file name from the branch; add 2-3 hashtags per lesson (CamelCase, from the lesson's topics).
- the books `books/ece/ec-circuits/ec-circuits-u1..u6.html` on main (fixed by the fact review).
- the data pack artifact https://claude.ai/artifact/9j8tUxjFNfcEit4ZGerNpN (site/make_site.py, subject/make_subject.py,
  thumbs/make_thumbs.py, logos, universal.json, worklist.json). Read it with the Artifact tool, action read, path ....

Steps:
1. Fonts first (sparse clone of google/fonts ofl/rubik, nunitosans, notosansmath, ibmplexsans, ibmplexmono,
   bricolagegrotesque into ~/.fonts, fc-cache), and `pip install playwright==1.63.0`.
2. Notes PDFs, one per lesson, with chapter numbers taken out (rule of 21 Nov: no "3.1"-style numbers in student PDFs):
   `DENUMBER_DUMP=cut python3 pipeline/lessons/engine/notes_denumber.py <pack>/site/make_site.py <pack>/universal.json
   <pack>/worklist.json videos.json books site --pdf-only`. Use notes_denumber.py from main as it is now (it rewrites "this unit" wording). Open three PDFs and check: no chapter or unit numbers, figures
   numbered from 1, chapter titles in quotes where a number was, no college names.
3. Descriptions (site/descriptions/*.txt from the same run): check each has the notes link and no unit or lesson number.
4. Thumbnails: t16 only, in the split blueprint look (owner-approved 21 Nov 2026; see
   `pipeline/lessons/DEPT_THUMBNAILS.md` and the skill ufe-t16-thumbnails). `make_thumbs.py scan` the 22 html and write
   one hook per lesson (at most 40 characters, a question the lesson answers) into thumbs.json. Subject kicker "CIRCUIT THEORY" only.
   Do not run `make_thumbs.py build`: no t11, t14 or t15. Then write `work/t16/ec-circuits/specs.py` from each lesson's book worked
   example and run `t16_split.py build` until it prints OK; look at t16_sheet.jpg and three thumbnails at full size.
5. Upload sheet: `make_subject.py ec-circuits --lessons --notes --thumbs work/t16/ec-circuits/out --thumb t16 --out --universal --videos` must print OK
   (apply the t16-only patch in DEPT_THUMBNAILS.md first).
6. Deliver: commit `ec-circuits/` (pdf/, thumbnail/thumbs.json, t16/ with the _t16.jpg files, t16_sheet.jpg and specs.py, descriptions/, upload_sheet.html,
   upload_sheet.json, videos.json) to a new orphan branch `deliver/ec-circuits`
   (only the `ec-circuits/` folder in it, nothing from main) and push.
7. Two make_subject.py bugs (found on VLSI, fix them in your local copy): its college check reads plain "bits" as BITS
   (match only "BITS" in capitals or "BITS Pilani"), and key moments carry raw SVG <tspan> markup from trap lines: strip the
   tags (write a superscript as ^(...) and a subscript as _x) and unescape &amp;amp;. Check the sheet for "tspan" and "&amp;amp;".
   A third, found on Machine Design: key moments titled "Worked example: 2" should read "Worked example 2".

Do not write to /mnt/project-files or the person's computer, and do not message the person. Hand back in under 10 lines by
messaging the thread "Build 8 new exam subjects" (thread id cmsg_01VwvcZRx1mMD7zJQeF8gbhCHJ7d555QwKT2VRz537cmu9): the
commit, the checks, anything that did not fit.
