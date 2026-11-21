# VLSI Design: notes PDFs, thumbnails (t11/t14/t15) and upload sheet

One thread, Opus high. Follow the ufe-subject-pipeline skill from "notes PDFs" on; the lessons and fact review are done.
The model to copy is Signals and Systems: branch `deliver/ec-signals` (folder `ec-signals/`) holds exactly what you
must produce here, and `work/` is never committed.

Inputs (repo SwathishThiyagu/ufe-books):
- the 24 lessons, each on its branch `lesson/ec-vlsi-uN-Lk` (folder `ec-vlsi-uN-Lk/`); take the html, words.json and sheet
  from the branch tip (the fact review pushed new commits to u2-L1, u2-L2, u2-L3 and u6-L3).
- `pipeline/lessons/ece/ec-vlsi/uN/videos.ec-vlsi-uN.json` (from book2lesson) for the lesson list; set each title from the
  lesson's META title and each file name from the branch; add 2-3 hashtags per lesson (CamelCase, from the lesson's topics).
- the books `books/ece/ec-vlsi/ec-vlsi-u1..u6.html` on main (fixed by the fact review).
- the data pack artifact https://claude.ai/artifact/9j8tUxjFNfcEit4ZGerNpN (site/make_site.py, subject/make_subject.py,
  thumbs/make_thumbs.py, logos, universal.json, worklist.json). Read it with the Artifact tool, action read, path ....

Steps:
1. Fonts first (sparse clone of google/fonts ofl/rubik, nunitosans, notosansmath, ibmplexsans, ibmplexmono,
   bricolagegrotesque into ~/.fonts, fc-cache), and `pip install playwright==1.63.0`.
2. Notes PDFs, one per lesson, with chapter numbers taken out (rule of 21 Nov: no "3.1"-style numbers in student PDFs):
   `DENUMBER_DUMP=cut python3 pipeline/lessons/engine/notes_denumber.py <pack>/site/make_site.py <pack>/universal.json
   <pack>/worklist.json videos.json books site --pdf-only`. Open three PDFs and check: no chapter or unit numbers, figures
   numbered from 1, chapter titles in quotes where a number was, no college names.
3. Descriptions (site/descriptions/*.txt from the same run): check each has the notes link and no unit or lesson number.
4. Thumbnails: `make_thumbs.py scan` the 24 html, write one hook per lesson (at most 40 characters, a question the lesson
   answers) and the page picks, `build`. Subject kicker "VLSI DESIGN" only. Look at thumbs_sheet.jpg and three thumbnails
   at full size.
5. Upload sheet: `make_subject.py ec-vlsi --lessons --notes --thumbs --out --universal --videos` must print OK.
6. Deliver: commit `ec-vlsi/` (pdf/, thumbnail/ with thumbs.json and thumbs_sheet.jpg, descriptions/, upload_sheet.html,
   upload_sheet.json, videos.json) to a new branch `deliver/ec-vlsi` and push.

Do not write to /mnt/project-files or the person's computer, and do not message the person. Hand back in under 10 lines by
messaging the thread "Build 8 new exam subjects" (thread id cmsg_01VwvcZRx1mMD7zJQeF8gbhCHJ7d555QwKT2VRz537cmu9): the
commit, the checks, anything that did not fit.
