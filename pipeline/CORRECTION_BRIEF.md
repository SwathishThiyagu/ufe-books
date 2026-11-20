# Correction pass for one DeepSeek draft (Nov/Dec 2026 exam subjects)

One thread per unit, Opus at high effort. The thread's message names the unit (for example `ec-signals-u3`) and its draft branch (`free/<unit>-book` or `ds/<unit>-book`).

## Setup

1. Clone `SwathishThiyagu/ufe-books`. Read `CLAUDE.md`, `pack/WRITER.md` (the standard), `pipeline/SLOP.md` (the AI-slop rules: use them as the checklist), `pipeline/claude_figs/README.md` (the figure workflow) and `pipeline/EXAM_ND2026.md` (the exam course and what was added to the packets).
2. Use the packet on **main** (`packets/<unit>.json`): it now lists the exam course's official topics under `where` and may have new subtopics the draft lacks.
3. Read the draft: `git fetch origin <branch>`, the book at `books/<dept>/<sid>/<unit>.html` on that branch, the chapter states `.free/<unit>/ch<k>.json` and `.free/<unit>/report.md` (note every "serious" flag).
4. Scratch files go in `work/<unit>/` (never committed).

## What to fix (all of it, chapter by chapter)

1. **Every worked example and every calculation:** trace it by hand or run it (Python for numbers, a compile for code). Fix any wrong step, value, unit or final answer, and any text that refers to it. A trace that does not do what the text says is a wrong example (the Data Structures miss).
2. **Wrong facts:** fix them. Leave out a number you cannot verify; never invent sources, page numbers or links.
3. **New subtopics:** write a full chapter for each packet subtopic the draft does not have, to the standard in `pack/WRITER.md`, in packet order (chapter numbers follow the packet).
4. **Exam course coverage:** check each chapter against the exam course topics in `where` and cover anything listed that the chapter misses (the depth notes in `pipeline/EXAM_ND2026.md` say where).
5. **Figures:** redraw every figure by hand with real labels, drawn from that chapter's own worked example and numbers (`pipeline/claude_figs`, model `c_dl_u2.py`, `apply.py`). Rewrite any sentence that describes the old figure. Look at every rendered figure once.
6. **Notes cleanups:** no unit or chapter numbers that point to other units (name the topic instead: "see Laplace transform analysis"); no "(from memory; check)" anywhere; the web-resources heading is "Further reading online" with no note about the book script; no college or university names, no counts of universities, no university-hosted sources.
7. **Long questions:** every long-answer question in the question bank gets "Points to cover" (the old outline) and a full "Model answer": numbered steps; a full trace or working table where the question is a calculation or a trace; a figure or code where asked; a closing check with numbers; 360 to 990 words by marks. Every number in an answer is computed, not guessed. Answers use the book's own notation and conventions. Answer tables must scroll sideways on a phone. `pipeline/render.py` supports this: give a question-bank item in the unit state an `"answer"` list of steps (a string, or a dict with `text` plus optional `table` {head, rows}, `pre`, `svg` {h, body, aria}); the book then shows "Points to cover." and a numbered "Model answer.". Reuse it; do not each edit render.py.
8. **Slop:** apply every rule in `pipeline/SLOP.md`.

## Finish

1. `python pack/check_book.py <book> packets/<unit>.json --render` prints OK.
2. Commit the corrected state and book to the draft branch (`apply.py ... --push`, or a plain commit on the branch).
3. Merge into the library on main: `git checkout origin/<branch> -- books/<dept>/<sid>/<unit>.html`, set the unit's status to "ok" in `queue.json`, append any syllabus-data notes to `notes.md`, commit "<unit> book" and push to main. Never rewrite a book already committed to main.
4. Add one line to the table in `pipeline/STATUS.md`.
5. Reply with: the book path, the checker's summary line, the examples you changed and why (one line each), the chapters you added, anything you could not verify, and any packet problem.
