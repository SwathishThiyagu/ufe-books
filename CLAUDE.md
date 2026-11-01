# University free n easy · CSE unit books

This repo writes the CSE unit books of the University free n easy series. Each book is one HTML file per unit of the universal syllabus.

- `pack/WRITER.md` is the writing standard: read it in full before writing any book and follow it exactly.
- `pack/book_shell.html` is the page every book is built from; `pack/check_book.py` is the checker.
- `packets/<unit>.json` is each unit's packet. `queue.json` lists the units to write, in order, with their output paths.
- Known shell issues every book hits: (1) the shell's CSS comment contains the text `__PLACEHOLDERS__` and the word "placeholder", which the checker rejects — reword that one comment line to "Fill the marked fields and the <main> only"; (2) `.quiz summary` is display:flex, so wrap every quiz question text in a `<span>` or code/sub/sup inside it overflows at phone width; (3) write C macro names like __FILE__ with `&#95;` so they do not hit the placeholder check.

## How to run

1. Setup once: `pip install playwright && python -m playwright install chromium` (the checker's `--render` needs it). If Chromium cannot be installed, run the checker without `--render` and say so in the commit message.
2. Take the units in `queue.json` order. For each unit, spawn one subagent (several at once when the harness allows) with this brief:
   "Write one University free n easy unit book. Read pack/WRITER.md in full and follow it exactly. Packet: packets/<unit>.json. Shell: pack/book_shell.html. Output: <out from queue.json> (create the folder). Every book becomes the notes PDF students download and the source of voiced video lessons, so draw each figure clearly with real labels and give every worked example concrete numbers worked to the answer. [If first_of_subject: also audit the packet data and report errors.] Keep scratch files in work/<unit>/. Touch nothing else. Finish only when `python pack/check_book.py <out> packets/<unit>.json --render` prints OK, then reply with the hand-back described at the end of the standard."
3. On each hand-back: run the checker yourself; if OK set the unit's status to "ok" in queue.json, append the writer's syllabus-data notes to `notes.md`, and commit the book with queue.json and notes.md (`git add books queue.json notes.md && git commit -m "<unit> book" && git push`). Not OK: send the problems back to that subagent; after two failed repairs, start a fresh one.
4. Never delete or rewrite a committed book. Do not commit the work/ folder.
