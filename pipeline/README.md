# Free book writer

Writes University free n easy unit books with the free Gemini API, in small checked steps, on GitHub Actions.
The model only ever returns JSON; code turns it into the book.

| Step | Who |
|---|---|
| Plan the unit: idea, figure, example, trap per chapter | model (1 call) |
| Write each chapter as JSON | model (1 call per chapter, retried with the problems if a check fails) |
| Draw the figure from a small spec (blocks, tree, graph, array, plot, gantt, stack, sets, sequence) | `figures.py` |
| Recompute worked-example numbers; compile and run C, C++, Java and Python programs | `verify.py` |
| Review each chapter; revise once if the review finds serious errors | a second model (1-2 calls) |
| Summary, question bank, glossary, sources; open every link | model (1 call) + `verify.py` |
| Fill the shell and run `pack/check_book.py --render`; send short chapters or spilled figures back | `render.py`, `run_unit.py` |

A unit of 9 chapters takes about 20-30 calls. Progress is saved in `.free/<unit>/` after every step, so a run that hits the
daily free quota (exit code 75) continues where it stopped. Every run leaves `.free/<unit>/report.md`: the checker result,
the calls used, and the points a person should look at before the book is merged.

Run: Actions tab > Free book writer > Run workflow (unit ids), or add lines to `requests.txt` and push.
Each unit goes to its own branch `free/<unit>-book`; nothing is written to `main`.
Test offline: `python3 pipeline/run_unit.py c-os-u1 --mock --offline --out work/test.html --state work/state`.
