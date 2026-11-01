# University free n easy: unit-book data pack

The data the `ufe-unit-books` (orchestrator) and `ufe-unit-book-writer` (one book) skills read. Built 31 Oct 2026 from the
universal syllabus (v5) and the 10 universities' curriculum documents (Anna Univ, SRM, IIT Madras, IIT Delhi, IIT Bombay,
NIT Trichy, NIT Surathkal, NIT Calicut, Manipal MIT, Christ).

| File | What it is |
|---|---|
| `universal.json` | Every subject (217), its units (1,313) and subtopics (9,706). Per subject: `id`, `name`, `aka`, `group`, `departments` (where it is listed), `dept` (its home department = book folder), `scope` (`btech` or `other`), `usual_sem`, `taught_at`, `main_course_at`, `syllabi_compared`, `course_names` (what each university calls it), `course_used` (the course used for the unit mapping). Per unit: `n`, `name`, `subtopics` (`t` text, `id` anchor slug, `unis` that cover it, `match` phrases, `tags`: `advanced` = few universities teach it, `added` = none list it), `where` (per university: its course, which unit number there, that unit's title and listed topics). |
| `worklist.json` | One entry per unit book in writing order: common subjects first, then departments in catalogue order; inside a department by usual semester. `out` is the book's path under the channel folder. |
| `make_packet.py` | `python3 make_packet.py universal.json <subject id> <unit no> packet.json` writes the packet a writer thread reads. `--list btech` prints the work list. |
| `book_shell.html` | The page every book is built from: styles, header, contents list, progress ticks. Writers fill the `__PLACEHOLDERS__` and `<main>` and keep the rest. |
| `check_book.py` | `python3 check_book.py book.html packet.json --render` checks a finished book: one chapter per subtopic in order with the packet's ids and titles, figures, worked example, exam traps, levelled questions, beyond-the-syllabus box, unit sections, self-contained, fits a phone. Exit 0 = OK. |

Slug rule for anchors (same as the v6 student site): lowercase, `&` → `and`, every other run of non-alphanumerics → `-`,
trim `-`, at most 64 characters. A chapter's `id` is the packet's `subtopics[].id`; v6 links `u:<subject id>:<slug>`.

Book path: `03_Books/<dept>/<subject id>/<subject id>-u<N>.html` under `University_Free_n_Easy`.
