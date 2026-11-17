# Claude figures for the figure-heavy books

DeepSeek Flash redraws the figures of every waiting CSE book (workflows `figures-flash*.yml`). For the subjects where
pictures carry the teaching, Claude redraws them by hand on top of that, one book at a time, in a fresh chat (a long chat
costs about twice as much per step). Text and examples are not touched.

## The books (31), each on its branch

| Subject | Units | Branch |
|---|---|---|
| Operating Systems | c-os-u1 … c-os-u6 | `ds/<unit>-book` |
| Computer Networks | c-cn-u1 … c-cn-u6 | `ds/<unit>-book` |
| Theory of Computation | c-toc-u1, c-toc-u2 | `ds/<unit>-book` |
| Compiler Design | c-compiler-u1 … c-compiler-u6 | `free/<unit>-book` |
| Deep Learning | c-dl-u1, c-dl-u3 … c-dl-u6 (c-dl-u2 done) | `free/<unit>-book` |
| Computer Graphics | c-graphics-u1 … c-graphics-u6 | `free/<unit>-book` |

Wait until the Flash redraw lane has finished that book (its branch has a commit after 7 Nov 2026 06:40 UTC) so the two do
not race.

## Order (updated 10 Nov 2026)

Lessons are being made now from the library copies of Compiler Design and Deep Learning, so do these next, in this
order, then continue with the rest of the table: c-compiler-u1 … u6, c-dl-u1, c-dl-u3 … u6, then c-cn, c-toc, c-graphics.
For any book that is already in the library (main has `books/cse/<sid>/<unit>.html`; true for all c-compiler and c-dl
units), push with `--push --library` so the library copy on main gets the new figures too.

## Next (17 Nov 2026): the last 8 CSE subjects, then the new core books

These are not in the library yet; `apply.py <unit> <branch> --push --library` now adds them (makes the folder, sets queue.json "ok").
One fresh chat per subject; in each book also remove college or university names, counts of universities and
university-hosted sources (`drop_sources()`), and fix any wrong example or answer you see (`chapter_fix` or `text_fixes`).

| Subject | Units | Branch | Note |
|---|---|---|---|
| Computer Graphics | c-graphics-u1 … u6 | `free/<unit>-book` | drawing modules exist but were never applied: add `text_fixes`, then apply |
| NLP | c-nlp-u1 … u7 | `free/<unit>-book` | |
| Parallel and Distributed Computing | c-dist-u1 … u6 | `free/<unit>-book` | |
| Mobile Application Development | c-mobile-u1 … u6 | `free/<unit>-book` | |
| AR/VR | c-xr-u1 … u6 | `free/<unit>-book` | |
| Quantum Computing | c-quantum-u1 … u6 | `free/<unit>-book` | |
| Linux and Shell | c-unix-u1 … u5 | `free/<unit>-book` | 5 units |
| Blockchain | c-block-u1 … u6 | `free/<unit>-book` | |

Then the 20 core subjects DeepSeek started on 17 Nov (branches `free/` lane 1, `ds/` lanes 2 to 5; see
`pipeline/requests-deepseek*.txt`), the same way, once each book's branch has its "free-model book" commit.

## Text that describes a figure (added 10 Nov 2026)

A new drawing must never sit next to text that describes the old one. For every chapter you redraw, read the chapter text
for sentences about its figure ("Figure 3.1.1 draws this clock", "the figure shows ...") and rewrite them to match the new
drawing, changing nothing else. Put them in the same drawing module as `text_fixes(k)` returning `[(old sentence, new
sentence), ...]`; `apply.py` applies them with the figure and stops if a sentence is not found exactly once.

## Per book

1. `git fetch origin <branch>` and read each chapter's worked example and current figure from `.free/<unit>/ch<k>.json`
   (`git show origin/<branch>:.free/<unit>/ch<k>.json`).
2. Write `pipeline/claude_figs/<unit with _>.py` defining `spec(k)` like `c_dl_u2.py` (the model): one SVG per chapter,
   viewBox width 720, drawn from that chapter's worked example with its own numbers; labels 13 px or larger; colours only
   the shell variables (`--ink --muted --accent --live --next --line --line2 --panel --fig` and the `-soft` tints);
   arrowheads `url(#ar-UID-n|m|l|x)`; captions 1 to 2 sentences without style names. Readers are students who find
   textbooks hard: one idea per figure, few labels, plain words.
3. `python pipeline/claude_figs/apply.py <unit> <branch>`: rebuilds the book with no model and runs the checker; look at
   every `work/claude_figs/<unit>/fig-<k>.png` once, fix overlaps, run again.
4. When clean: `python pipeline/claude_figs/apply.py <unit> <branch> --push` (commits the state and the book to the branch).
5. Update the table in `pipeline/STATUS.md` (one line per finished book).

Budget: about 0.1 to 0.2 % of the weekly Claude limit per book in a fresh chat; keep one chat per 4 to 6 books.
