# University free n easy · CSE unit books (instructions for Codex)

This repo holds the CSE unit books of the University free n easy series: one HTML file per unit of the universal syllabus. Every book becomes the notes PDF students download and the source of voiced video lessons, so it must be complete, correct and clear on a phone.

## Your task

Each task names **one unit**, for example `c-oop-u3`. Write that one book and nothing else.

1. Read `pack/WRITER.md` in full before you start, and follow it exactly. It is the standard; where it and your habits differ, it wins.
2. Inputs:
   - the packet `packets/<unit>.json` (the chapters, their order, ids and titles are fixed by it);
   - the shell `pack/book_shell.html` (copy it; fill the marked fields and `<main>`; keep everything else);
   - the output path: the `out` field of the unit's entry in `queue.json` (for example `books/cse/c-oop/c-oop-u3.html`). Create the folder.
3. Draw every figure clearly with real labels, and give every worked example concrete numbers worked through to the answer. For programming chapters, show real code, a dry-run table and the exact output.
4. Known shell issues every book hits:
   1. the shell's CSS comment contains the text `__PLACEHOLDERS__` and the word "placeholder", which the checker rejects: reword that one comment line to "Fill the marked fields and the <main> only";
   2. `.quiz summary` is `display:flex`, so wrap every quiz question's text in a `<span>`, or code/sub/sup inside it overflows at phone width;
   3. write C macro names like `__FILE__` as `&#95;&#95;FILE&#95;&#95;` so they do not hit the placeholder check.
5. Check your book with
   `python pack/check_book.py <out> packets/<unit>.json --render`
   and fix everything it lists until it prints `OK`. If Chromium is not available, run it without `--render`, fix everything, and say so in the pull request. Never change the checker, the shell, the standard or the packet to make a check pass.
6. Facts: write what you know well. If you cannot look something up, leave an uncertain number out. Never invent citations, page numbers, ISBNs or links. In the sources section, list only standard textbooks you are sure of and open web resources you are sure exist, and leave out anything you are not sure of. Do not add notes such as "(from memory; check)" or "(link not opened; check)" anywhere in a book.
7. The channel's rules, which the checker also enforces: **no college or university names anywhere in the book**, and **no count of the universities that teach a topic** ("taught at 8 of 10" is not allowed). Write "some syllabi call this …" or "only a few universities teach this". The packet names the universities only so you can set the depth.

## What to change

- Add **only** the book file at its `out` path.
- Do **not** edit `queue.json`, `notes.md`, `pack/`, `packets/`, `CLAUDE.md`, `AGENTS.md` or any other book. The maintainer updates the queue and notes when your book is merged.
- Keep scratch files in `work/<unit>/` (ignored by git).

## Pull request

- If the environment cannot reach the GitHub API, do not wait for it: commit on a branch named `codex/<unit>-book`, push it, and put the hand-back in your final message instead. The maintainer merges branches directly.
- Title: `<unit> book` (for example `c-oop-u3 book`).
- Description: the hand-back from the end of `pack/WRITER.md`: the book path; chapters, words and figures (copy the checker's summary line); whether the check ran with `--render`; anything you could not verify; and any place where the universal syllabus or the packet's lists look wrong (a subtopic in the wrong unit, a list that belongs to another subject). Keep it under 15 lines.
- If the task says the unit is the **first of its subject**, also audit that packet's data (subtopic order, missing or duplicated topics, a unit that belongs to another subject) and report what you find in the description.

## Environment setup (for the maintainer)

Codex environment setup script, so the render check works (no admin rights in Codex, so no `--with-deps`):

```
pip install playwright && python -m playwright install chromium
```

Internet access for the environment: package managers plus the Playwright browser download domains (`cdn.playwright.dev` and the ones Codex proposes).
