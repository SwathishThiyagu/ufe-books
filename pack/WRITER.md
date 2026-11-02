# One unit book (University free n easy)

You are writing one book of the University free n easy series: one unit of one subject, for students at any Indian university. The series follows the universal syllabus built from 10 universities' curricula (Anna Univ, SRM, IIT Madras, IIT Delhi, IIT Bombay, NIT Trichy, NIT Surathkal, NIT Calicut, Manipal MIT, Christ). Students reach a chapter from the v6 student site by its anchor, so the chapter list, order, ids and titles are fixed by the packet. Everything else is yours to write well.

**No college names anywhere in the book** (the channel's rule, 2 Nov 2026). The packet names the universities so you can set the depth and the exam wording, but the book never names one of them: not in the header, the about section, a chapter, the question bank or the sources. Write "some syllabi call this …" or "only a few universities teach this". Scientific history and publishers are not syllabus colleges (the Ramachandran plot was worked out at the University of Madras; Oxford University Press). The checker refuses a book that names one of the ten.

## Inputs you are given

- The **packet** (`packet.json`, made by `make_packet.py`): `subject` (name, aka, group, departments, taught_at, course_names per university, course_used), `unit` (n, name, `subtopics` in order, each with `t` text, `id` anchor, `unis` that cover it, `match` phrases, `tags`), `where` (per university: its course, which unit number this is there, that unit's title and the topics it lists), `other_units` (the subject's other units and their subtopics, for cross-references), `universities`, `order`, `out` (the book's path in the channel folder).
- `book_shell.html`: the page shell. Copy it; fill the `__PLACEHOLDERS__` and `<main>`; keep everything else.
- `check_book.py`: the checker. The book is finished only when `python3 check_book.py <book> <packet> --render` prints `OK`.
- The output path. If any input is missing, ask the orchestrator; do not improvise the data.

## Who reads it

A student in the semester that teaches this unit, at any of the 10 universities, often reading on a phone the week before an exam. Many read English as a second language. They want to understand the idea, see it worked out once, know what the examiner asks, and move on. So: plain sentences, short paragraphs, every symbol defined where it first appears, every formula followed by what each term means, numbers with units, one idea per paragraph. Indian context where it helps an example (rupees, UPI, IRCTC, cricket, a Chennai power cut). No filler ("In this chapter we will…"), no hedging, no jokes required, warmth allowed.

## Read the packet before planning

1. The subtopics in order: these are your chapters, exactly as given.
2. `where[].topics`: what each college lists for this unit. These lists set the depth and the exam wording. Where a college uses another name for the same thing, give that name in the chapter without naming the college ("some syllabi call this 'ADT operations'"). Where a college's list goes deeper than the universal subtopic, cover that depth in the chapter that owns it.
3. `tags`: `advanced` = only one or two universities teach it: write it shorter (650–900 words) and say that only a few universities teach it (never which). `added` = standard topic no syllabus lists: write it as a normal chapter and say in one line that it completes the subject.
4. `other_units`: cross-reference them ("see Unit 4, Binary search trees"); never re-teach their content.

Then plan each chapter in a few lines: the one idea, the figure, the worked example, the trap, what goes beyond.

## The file: fill the shell

Placeholders:

- `__TITLE__`: `<Subject> · Unit <N>: <Unit name> · University free n easy`
- `__CRUMB__`: `<Department label> · <Subject> · Unit <N> of <total units>`
- `__EYEBROW__`: `Universal syllabus · <Subject> · taught at <k> of 10 universities`
- `__SUBJECT__`, `__UNIT_NO__`, `__UNIT_NAME__`
- `__LEAD__`: two or three sentences: what the unit is about and what the student can do after it.
- `__CHIPS__`: `<span class="chip tier">Taught at k of 10</span>`, `<span class="chip">Usually Sem s</span>`, `<span class="chip">n chapters</span>` (no "Main course at" chip: it names colleges).
- `__FOOT__`: `Built for the University free n easy YouTube channel from the universal syllabus of <Subject> (Oct 2026). Written with top universities' syllabi and standard textbooks; check a formula against your prescribed book before an exam, and report mistakes on the channel.`
- `__MAIN__`: the sections below, in this order.

### `<section id="about">` — About this unit

- `<h2>About this unit</h2>`, one short paragraph on what the unit covers and how the chapters build on each other.
- No table of universities, no coverage squares and no colour legend (they name colleges).
- **Chapters**: an ordered list, each chapter name linked to its anchor, with `<span class="tag">advanced</span>` / `added` where tagged.
- **How to use this book**: three bullets (read the idea, do the worked example yourself, answer the questions before opening them).

### One `<section class="ch" id="<packet id>" data-n="<k>">` per subtopic, in packet order

1. `<h2><span class="num"><N>.<k></span> <subtopic text exactly as in the packet></h2>`
2. `<p class="lead">`: the idea in one paragraph: what it is, why it exists, where it is used.
3. Optional `<div class="prereq">`: "You need: …" with links to earlier chapters or units.
4. The explanation: two to four `<h3>` subsections. Define terms, then the mechanism, derivation or algorithm step by step (`<ol class="steps">` for procedures). Formulas in text with Unicode (x², √, Σ, ≤, →) or in `<pre>` for longer derivations; no MathJax or any external script. Code in `<pre><code>` with the language named in the text, and its output shown.
5. At least one `<figure class="fig">` with an inline `<svg>` you draw (rules below) and `<figcaption><b>Figure <N>.<k>.1</b> what the figure shows and what to notice</figcaption>`.
6. `<div class="example"><h4>Worked example</h4>`: a full exam-style question, then the solution step by step with intermediate values and units; for programming subjects, code plus a dry-run table and the expected output. Add a second example when the subtopic is calculation-heavy.
7. `<div class="traps"><h4>Exam traps</h4><ul>`: three to five bullets: confusions, sign and unit slips, look-alike terms, and the examiner's favourite question.
8. `<div class="quiz"><h4>Check yourself</h4>`: five to eight `<details class="q" data-level="remember|understand|apply|analyze"><summary><span class="lvl">Apply</span> the question <span class="marks">4 marks</span></summary><p>the model answer</p></details>`, at least one of each level. Answers short; for apply, the key steps and the final value.
9. `<div class="beyond"><h4>Beyond the syllabus</h4>`: three to six sentences on where this topic goes in industry, research or newer curricula (ACM/IEEE CS2023, current tools and standards), and what to search next. Say it is not for the exam.

Length: 900–1600 words per chapter (650–900 when tagged advanced). The checker refuses under 650 and over 1900. Say it once, well; a second pass of the same idea is what pushes a chapter over.

### Unit-level sections

- `<section id="summary">`: `<h2>Unit summary</h2>`; a `<div class="keybox">` with a table of key terms and formulas (Term | Meaning or formula | Chapter); a unit-map `<figure class="fig">` (SVG) showing how the chapters connect; six to ten numbered takeaway lines.
- `<section id="question-bank">`: `<h2>Exam question bank</h2>`; 10–16 long-answer questions (8–16 marks) as `<details data-level="…">` grouped under `<h3>` Remember and understand / Apply / Analyze and evaluate, each with an answer outline (the points an examiner looks for); at least two questions that span chapters. Where `where[].topics` shows the syllabi stress something, say so in a `<p class="note">` without naming any college ("most syllabi ask for the structure and function of each polysaccharide").
- `<section id="glossary">`: `<h2>Glossary</h2>`, `<dl class="gloss">` of 15–30 terms.
- `<section id="sources">`: `<h2>Sources and further reading</h2>`: the standard textbooks of the subject (title, author, edition only when sure; chapter pointers only when sure; never page numbers you have not seen), two to six open web resources you actually opened, with links, then one line: "Syllabus: the University free n easy universal syllabus, built from top universities' syllabi." Mark anything taken from memory "(from memory; check)".

## Figures

- Draw original diagrams in inline SVG: structures (arrays, lists, trees, graphs), flowcharts, block diagrams, free-body and circuit sketches, plots with axes and ticks (plot computed points only), timelines, pathways. One per chapter; a second only where one picture cannot show the mechanism (a before-and-after, a double rotation). A figure costs as much as 300 words, so make the one figure count.
- `<svg viewBox="0 0 720 H" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="…">`. Height to fit; nothing outside the viewBox. Text ≥ 13px in that scale, never overlapping, at least 8px from the edge. Colours through CSS variables so dark mode works: `style="fill:var(--panel);stroke:var(--accent);stroke-width:2"` for boxes, `fill="currentColor"` for text, `var(--line2)` for guides, `var(--accent)` / `var(--live)` / `var(--next)` to pick things out. Arrowheads via `<defs><marker>` with a unique id per figure (ids must be unique in the page). Keep a figure under about 60 elements; split rather than crowd.
- After the render check, read its figure warnings: text spilling outside the box means a longer label than the room; shorten the label or widen the spacing.

## Facts

- Write from what you know well. For named results, constants, complexity bounds, dates, standard values and anything numeric, verify with WebSearch or WebFetch when not sure, or leave the number out. At most five lookups per book, each for a specific number or claim; every page fetched costs more than a chapter. Never invent citations, page numbers, ISBNs or figure numbers.
- Original explanations only; no textbook passages, no lyrics, no long quotes.
- No notes to self, no "[verify]" left in the file, no empty sections.

## Working without losing work

Write the file in parts: the filled shell with the about section first, then each chapter appended before `  </main>` with Edit (one chapter per edit), then the unit sections. Run the checker once halfway (it will complain about missing chapters; read only the other complaints) and at the end with `--render`. Fix everything it lists.

## Hand back

When the checker prints OK, reply with: the book path; chapters, words and figures (from the checker line); anything you could not verify; and any place where the universal syllabus or the packet's college lists look wrong (a subtopic in the wrong unit, a college list that belongs to another subject), so the data can be fixed. Keep it under 15 lines.
