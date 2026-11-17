# Fill these lesson files (fast path of the ufe-unit-lessons skill)

The files here were generated from the library unit book by `book2lesson.py`. Everything that comes from the book is
already on screen (part slides, the book's figures, worked-example text, traps, exam questions with the book's model
answers, notes page, next card). Your job is the writing: replace every `TODO`. Do not read the whole skill or the
reference lessons unless something below is unclear; `lesson_kinds.md` has the field list of every kind.

## What to write

- `say`: one narration line per scene, warm, second person, short sentences, 20 to 40 words (pq lines shorter).
  The whole lesson 800 to 880 words (5 to 7 minutes; the check prints the count). Say only what the book says.
- The student's notes are this lesson's free notes PDF, linked in the description: say "your free notes" (hook
  `star`, notes page), never "unit book", the finder or the site. Only lesson PDFs are offered (no unit books).
- `cues`: for every key the scene uses, the first two to four words of the phrase in `say` where that thing should
  appear. The phrase must occur exactly in the line.
- Short on-screen text: titles, notebook items (under 60 characters each), trap lines, recap lines, the shortened `al`
  answer lines (keep the book's facts, cut the words), META.title/big/star/parts/chips, the hook.
- `bookfig`: narrate the figure in the order it builds (left to right, `steps` pieces, cues `s1..s4`) and give `cap`
  one takeaway line. Delete a figure scene only if it duplicates another.
- `calc`: `q` two short lines, `f` the formula(s) on the board, `hint`, then each step's `stage` as the row the
  narrator reaches (use `['τ = 1 / 0.05','τ = 20 s']` for a row that transforms). Work every number in python first.
- Two or three light jokes (not more) in hook, notebook or bookfig lines (never in definitions, traps, questions or answers).
- `agenda.ribbon2` is already counted from the book (parts, worked examples); keep it unless you cut a worked example.
- `pa.vis` (optional answer picture): drawn in a box about 620 × 510 with origin top left; it may use its own cue keys
  (add them to `cues`); keep everything inside the box.
- `calc` draws only the rows up to the last `live` index; a long example is two calc scenes (`live:[0,1,2]`, `live:[3,4]`).
- `bookfig`: each figure item is `[x, svg, step]`; the generator groups pieces into steps (background first, then up to
  three left-to-right groups, labels with their shape). If the order reads wrong, change the step numbers (1-4), not
  the drawing. Cue each step `s1..s4` to the words that name it, and cue `cap` early enough to be read (not the last word).
- The contact sheet shows each scene at 92% of its time; a caption or stamp cued at the very end will not be on it.

## Kokoro safety (the build checks these)

- No digits or symbols in `say`: write numbers and units as words ("seven point five micrometres").
- Technical names, acronyms and Greek letters go in `PR` (misaki phonemes) and are spoken as `${P('ATP')}`; copy
  existing entries from `pronunciation.json` beside the engine. Other words the dictionary lacks go in YOUR lesson's
  `<lesson>.pron.json` beside it (never edit another lesson's file; the build reads the engine's, the folder's and yours).
  A bare letter A is written `[A](/ˈA/)`.
- US spellings in `say` (the on-screen text may keep the book's spelling).
- No college or university names anywhere, and no real organisation's brand in examples.

## Text the check fails (SLOP.md rules; they run on every `say`, on the text each scene draws, and on META)

- "book" in any form ("your book", "the book's figure", "unit book"): say "your free notes"; "of your notes" without "free".
- Unit numbers or unit references ("Unit two", "this unit", "all six units", "(Unit 4)"): the syllabus is universal, so
  name the topic instead ("in the lesson on phase estimation", "next time: process scheduling").
- Bloom levels, spoken or shown ("An apply question", "at the analyze level", "Question two, apply."): say only
  "Question one / two / three".
- Caret or underscore maths on screen (`2^(n−1)`, `x_i`, `S_W`): use ² ⁻¹ ₐ or a sub/sup tspan
  (`V<tspan baseline-shift="sub" font-size="70%">in</tspan>`). Code in a monospace font is exempt.
- A site or finder line ("find this unit in your syllabus on the site"): there is no site yet.
- A real content phrase that trips a rule ("booking site", "OP_DUP", "the library issues the book") goes in
  `META.allow:['booking site']`. Warnings (printed, not failing): built-in recap icons, Indian and Western number
  grouping in one lesson, filler words (imagine, journey, crucial, amazing, delve, unlock).

## Facts (a fact review recomputes these before the subject is approved)

- Every `pq` shows all its givens on screen; its `pa` uses only those and what the lesson showed. A question that
  reuses or changes the worked example's data says so.
- A trap's "Don't write" must be wrong under every common convention, and its stated wrong result must be what that
  mistake really produces (recompute it). If the rule depends on a convention, the card names it.
- Software, protocol and kernel behaviour names its version or era on screen ("since GCC 14", "since React 17",
  "before the Merge, 2022"); keep the book's caveats ("simplified", "for every p", "sufficient, not necessary").
- Draw the end state the line states, in the colours the numbers give; a picture never contradicts its narration.
- Code on screen is complete and runs as shown, or is marked `frag:true`; output shown is what it prints.
- If you find an error in the book, write it in your hand-back; do not narrate around it.
- Recap pictures are the lesson's own (draw them in `EXTRA` as `ICON.name`), filling most of their card.

## Pictures on every list page (required)

Every `notebook` page gets `vis:(c,u,box)=>svg`: a picture of its points in the mint panel on the left (640 × 690; the list sits on the right),
each part landing on its item's cue (`g('pop', tk(c,'i1'), …)`), building one diagram as the narrator goes. Every `trap2`
gets `wv` and `rv` (640 × 330 inside each card): the wrong idea drawn (the engine strikes it through) and the right idea
drawn. Draw what the line says, exactly as the book says it: molecules, membranes, arrows, before/after, a tiny graph.
A `traps` list gets the same left panel, one small picture per trap on its cue. Trap pages are in the dull crimson `TRED`:
number any rows in a trap picture with `TRED` badges at `fill-opacity="${TOP}"` (80 %), not `RED`. Never shorten an on-screen line to fit: long lines wrap.

## Where to spend more effort (IMPROVISE)

Only the scenes marked IMPROVISE in the file: the hook, a `vis` answer picture when the answer is a mechanism or a
comparison, a figure whose text would be too small (zoom with `view:[x,y,w,h]` or split it), and a process the book
draws statically but that only makes sense moving (a cycle, a cascade): then a bespoke kind in `EXTRA` is worth it.
Everything else is filling, not designing.

## Build and check (in this order, stop at the first failure and fix it)

```bash
E=<engine dir>   # lesson_template.html, lesson_build.py, lesson_sheet.py, bumper/
python3 $E/lesson_build.py L.js out.html --check        # every TODO left fails; fix until clean
python3 $E/lesson_build.py L.js out.html                # voice + HTML
python3 $E/lesson_sheet.py out.html sheet/ --frames --play
```

The sheet must end clean: 0 page errors, 0 cue failures, 0 text outside the safe area, play-through OK. Then look
only at: `sheet/sheet.png` (once, whole lesson), every frame the report lists, the `bookfig` and `calc` frames, and
the four logo frames `B_*`, and every layout warning it prints (text over text, text past its card, small recap
pictures, book figures under half the stage or cut). Fix what is wrong and rebuild with `--reuse` (keeps the voice) when
only the drawing changed, or `--revoice` (voices only the changed lines) when some narration changed.
