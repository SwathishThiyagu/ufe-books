# The lesson file: scene kinds and fields

A lesson is one JavaScript file: a pronunciation map, `META`, and `SC`, the list of scenes. The engine in `lesson_template.html` draws every scene from its fields on a 1600 × 900 page; `lesson_build.py` voices the narration (Kokoro), times every cue to its spoken word, and writes the self-contained HTML: a video page that plays straight through, nothing stops it and nothing pops up (it goes to YouTube). Copy the shape of `ref_ampk6.js` (a finished lesson of the same engine).

## Top of the file

```js
const PR={GPCR:'ʤˌipˌisˌiˈɑɹ', JAK:'ʤˈæk', STAT:'stˈæt', PI3K:'pˌi ˌI θɹˌi kˈA', cAMP:'sˈIklɪk ˌAˌɛmpˈi'};   // misaki phonemes
const P=k=>`[${k}](/${PR[k]}/)`;                                   // P('GPCR') -> [GPCR](/…/) inside narration
const META={n:1, subject:'biotech', title:'How cells talk', badge:'Lesson 1', kick:'CELL BIOLOGY · UNIT 5 · LESSON 1 OF 3',
  series:'University free n easy', big:'TALK', star:'Starring: the receptor!',
  parts:['Who is talking','Receptors','G-protein coupled receptors'],
  chips:[['WHO IS','TALKING'],['THE','RECEPTORS'],['G-PROTEIN','RECEPTORS']]};  // one [two lines] per part, upper case, short
const RC=META.parts.length+1, QZ=RC+1, LS=RC+2, OUT=RC+3;         // section ids: 0 intro, 1..n parts, recap, exam practice, surprise, outro
const SC=[ …scenes… ];
// optional: function LESSON_MASCOT(x,y,s,o){ return …svg… }  — replaces the AMPK mascot on the agenda and exam pages
// optional: function EXTRA(R,ICON){ R.myScene=(sc,c,u)=>{…}; ICON.myIcon=(x,y)=>'…'; }  — bespoke scene kinds and icons
```

Every scene has: `s` (section id), `k` (kind), `term` (short name for the scene menu), `say` (one narration line), `cues` (`{key:'first words of the phrase'}`: the time each key fires is when the narrator reaches those words; `c.end` is the scene's end), `pause` (seconds of silence after the line; `4.5` on a question, `.6` to `1.2` to let a punchline sit), optional `joke:'note'` and `line` (index of another scene's narration to reuse). Cue keys are what the kind below expects; a missing cue fires at 0.2–0.3 s.

## The page kinds

| Kind | Fields | Cues |
|---|---|---|
| `hookArt` | `art:[[icon,cueKey,x,y,scale]]` inside the mint disc at the right (centre about 1110,440); `caps:[[text,cueKey,hot]]` **three** caption lines on the left (hot=1 is magenta); `bang:[text,cueKey]` the question as the headline | the keys you name |
| `agenda` | `big`, `ribbon` (the lesson title), `star`; draws the parts from META | `t` title, `r` ribbon, `p1`…`p3` parts, `q` the exam-practice stamp |
| `part` | `n` (part number); `pts:[three short lines]` what the part covers; draws META.chips[n-1] as the title on a deep page in the part's colour, with the giant numeral and the strip of all parts | `p` the number, `o` the title |
| `flow` | `title`; `lead:[text,cueKey]`; `nodes:[{t,sub,i:icon,k:cueKey,c:colour,x:cueKey}]` (2–5 cards in a row, `x` adds a cross on that card); `links:['+'|'-']` between nodes (`-` is a blocking bar); `out:{t,k,c}` a stamp under the row; `notes:[[text,cueKey,colour]]`; `cite` + `citeK` a "First shown: …" card | node keys |
| `cards` | `title`; `lead`; `cards:[{h:header,c:colour,i:icon,l:[lines],k:cueKey,big,bfs,em,fs}]` (2–4); `pill:[text,cueKey,colour,x,y]` | card keys |
| `trap2` | `title`; `wrong:[lines]`, `right:[lines]`; `wl`, `rl` headers; `wi`, `ri` icons; **`wv`, `rv`: `(c,u,box)=>svg` a picture inside each card under its lines (box 640 × 330)**; the wrong side is struck through and stamped in the dull crimson `TRED`, the right side underlined and stamped | `x` warning stamp, `w` wrong side, `r` right side |
| `traps` | `title`; `items:[[headline,explanation,cueKey]]` (up to 5); `live`; **`vis:(c,u,box)=>svg` a picture of the traps in a mint panel on the LEFT (640 × 690), the cards on the right**; an explanation too long for one line wraps to two (v4.5), so never shorten one to fit; trap pages use the dull crimson `TRED` (#A0393A) and card tint `TPINK`, and any number badge inside a trap picture uses `TRED` with `fill-opacity="${TOP}"`; trap numbers and underlines are at 80 % opacity (`TOP`) | item keys |
| `notebook` | `title`; `items:[[text,cueKey,icon?]]` lined page (numbers pop, lines write in, the spoken line is highlighted, a tick when done); `live`; `lh`; `start`; **`vis:(c,u,box)=>svg` a picture of the points in a mint panel on the LEFT, the list on the right (box 640 × 690), each part landing on its item's cue — every notebook page should have one**; a line too long for one line wraps to two and every line on the page shares one size (v4.5), so never shorten an item to fit | item keys |
| `calc` | a calculation that transforms in place beside a **formula board**: `title`; `q:[question lines]`; `f:[formula lines]`; `hint`; `fk` the board's cue; `steps:[[label, stage \| [stages], cue \| [cues]]]` (each stage rewrites the same row when its cue is spoken, so `'τ = 1 / 0.05'` becomes `'τ = 20 s'` instead of piling up); `live:[step indices animated in this scene]` (earlier steps stand finished); `ans:[text,cue]` a stamp; `fs`, `rh` | step cues, `fk` |
| `check` | quick check: `ql:[question lines]`, `ics:[icons]`; `pause:3.4` | `k` mascot, `w` bubble |
| `answer` | `al:[answer lines]`, `word` (yellow stamp), `ics` | `b` stamp, `a` bubble |
| `quizQ` / `quizA` | `n`, `q`, `opts:[A,B]`, `ans` (0/1), `why` (one-line reason, answer page) | question: `a` cards; answer: `k` correct, `e` reason |
| `recap` | `panels:[[header,colour,icon,[lines],cueKey]]` (3); `live:[indices animated in this scene]` | panel keys |
| `pq` | exam question, in the open (no card, no button): `lv:'R'|'U'|'A'|'N'|'B'` (Remember, Understand, Apply, Analyze, Beyond), `n`, `q`; `pause:3.4` is the thinking time, marked by the maths lessons' thinking clock (a navy disc with a question mark whose ring drains over the last three seconds); `hint` a formula line shown in yellow during the pause; `qfs` | `k` level line, `q` question |
| `pa` | model answer: `lv`, `q`, `al:[[line,cueKey]]` (2–5 lines), or `big` (one short answer), or `calc:{f,hint,fk,steps,live,fs,rh}` when the answer is a calculation (drawn as the `calc` kind inside the answer card); `vis:(c,u,box)=>svg` an **animated picture of the answer** drawn on the left in a mint box of `box.w` × `box.h` (620 × about 480, origin top left; use the helpers and `g(anim,tk(c,key),…)` so its parts land on the same cues as the lines), the `al` lines then sit on the right; `fs` | line keys, `b` big, step cues |
| `bookfig` | **the unit book's own figure**, built up piece by piece left to right (no redrawing): `fig:{vb,defs,items}` as written by `book2lesson.py`; `title`; `steps` (default 4); `cap` one takeaway line; `view:[x,y,w,h]` zooms into part of the figure (use it when the book's smallest text would land under about 22 px); `static:true` shows it whole at once. Colours come from `BOOKVARS` (the book's palette, written at the top of a generated lesson) so the figure looks exactly like the student's notes | `s1`…`sN` the pieces, `cap` |
| `figs` | for your notes: the unit book **is** the student's notes. `title`; `lhead` (default "Your notes: the free unit book") with `tags:[[line, detail]]` naming the unit book, the chapters this lesson covers, and its question bank; `rhead` (default "Redraw these from the book") with `figs:[[figure, what it shows]]` the book figures to copy out; `note` for the textbooks the book draws from (sources, not reading lists); no college names | `t` tags, `f` figures |
| `outro` | `words:[[word,colour,cueKey]]` three memory stamps; `next:[label,title,sub,icon]`; `end` | `f` "So remember", `n` next card, `s` end line |

Colours by name: `BLU RED GRN ORG MAG PUR CYN ACC ACD SLT INK`. Icons: `ampk ampkOn ampkSleep ampkAlarm glucose glucoses drop drops mito mitoSplit mitoMany nucleus dna gene ribosome chain pill flask liver muscle heart clock histone recycle cholesterol glycogen membrane battLow battFull ca o2 poison starve run hormone yeast plant human tumor map lysosome shield up down stop ok timer calendar map2`, plus `blob:COLOUR:name` (a round labelled character) and `nuc:N` (a nucleotide with N phosphates). New icons go in `EXTRA`.

## On every page

The engine draws a **wayfinder** on every scene: the lesson's address from `META.kick` top left in spaced capitals ("CELL BIOLOGY · UNIT 5 · LESSON 1 OF 3") and the section rail top right (PART 1 · PART 2 · PART 3 · RECAP · PRACTICE), the current section filled in its colour, finished ones ticked. Keep the top 90 px of a bespoke scene clear of it, and keep every element 20 px inside the 1600 × 900 page: `lesson_sheet.py` lists any text outside that safe area. A scene can opt out with `wf:false` (never for a teaching page). The build adds the channel bumper before and after the lesson (`--no-bumper` to skip); nothing else of the channel appears on the teaching pages.

## Bespoke scenes

A raw `<path>` in a bespoke drawing needs `fill="none"` (the `arrow`/`parrow` helpers set it); `capbox` sizes itself from an estimate of the text width, so give a long caption `pad` or `w` when it must not spill.

A figure from the book that no kind can show (a receptor in a membrane, a cascade with branches) is a bespoke kind written in `EXTRA(R,ICON)` with the engine's helpers: `pageBG(u,COLOUR)`, `title(text)`, `panel(x,y,w,h,{fill})`, `capbox(x,y,text|[lines],{fs,bg,fg,a})`, `bang(x,y,text,{fs,fill})`, `lt(x,y,text,{fs,fill,a})`, `sfx(x,y,text,{fs,bg,fill,r})` (a stamp), `arrow(x1,y1,x2,y2,{col,w,hl,block})`, `parrow(points,{col})`, `nbox(x,y,w,h,text,sub,colour)`, `blob(x,y,scale,colour,name,{mood})`, `face(...)`, `icon(name,x,y)`, and the timing wrappers `g(anim,time,svg)` with anims `pop slam rise fade slideR slideL grow growX wig type`, `swap(t0,t1,svg)`, `showAt(t,svg)`, `hideAt(t,svg)`. Keep text inside 1600 × 900, at 24 px or larger; `fit(text,fs,maxWidth)` returns the largest size at or under `fs` whose estimated width fits (the engine's own slots already use it).

## Rules that the build checks

- `META` has `title`, `parts`, `chips`, `badge`, `kick`; one `chips` pair per part.
- An `agenda`, a `recap` and an `outro` exist; every `pq` is followed by its `pa`.
- Every scene has a `say`; no digits or symbols in the spoken text (numbers as words; `[GLUT4](/…/)` marks are fine); under 60 words a line; the whole lesson about 800 to 880 words (Kokoro af_heart at 1.0 speaks about 2.3 words a second, so that is 5 to 7 minutes with the pauses; the check prints the estimate); every cue phrase occurs in its line; no bare letter A (`[A](/ˈA/)` for the letter, `[a](/ɐ/)` for an article the check misreads: marked words are skipped); every word is in the dictionary or has inline phonemes or a `pronunciation.json` entry beside the lesson.
- Every scene renders without an error and without "undefined" or NaN in its drawing.
- `python3 lesson_sheet.py built.html outdir --frames --play` (after a build): no page errors, no cue failures, no text outside the safe area, calc frames written, play-through OK; look at `outdir/sheet.png` and the `calc_*` frames.
- No college or university names anywhere in a lesson (narration, captions, notes).

## Fast path: generate the lesson from the book

`python3 book2lesson.py <library book.html> <outdir> [--split 2.1-2.2,2.3-2.5] [--next-unit "title"]` splits the unit into lessons,
writes each lesson file with every on-screen field the book supplies already filled (part slides, `bookfig` figures,
worked-example text, traps, the book's exam questions and model answers, notes page, next card) and `TODO` where a writer
is needed, plus `WRITE.md` (the short rules for the writer) and `videos.<unit>.json` for `site/make_site.py`.
`lesson_build.py --check` fails while any `TODO` is left. Scenes marked IMPROVISE (hook, `vis` answer pictures, figures
too small to read, processes that need motion) are where a writer spends real effort; the rest is filling.
