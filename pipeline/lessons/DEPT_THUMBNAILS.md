# Department lessons: t16 only, in the split blueprint look (owner-approved 21 Nov 2026)

Every lesson of a non-CSE department (EEE, ECE, Mech, Auto and every new department) gets **one** thumbnail,
`<lesson>_t16.jpg`, in the split blueprint look. Do not make t11, t14 or t15 for these lessons any more; leave any
that already exist untouched (on the computer and on the deliver branches). CSE keeps its seven t16 category styles
and its t11/t14/t15. Biotech, AI and DBMS are out of scope. Civil, Chemical, Aero and Biomedical are prototypes only:
do not use them until the owner approves their palette and line art.

The full rules are in the skill `ufe-t16-thumbnails`, section "Department lessons: the split blueprint look".
The older glass/emboss/cubes `T16_BRIEF.md` files in the department folders are superseded.

## Tool

Data pack https://claude.ai/artifact/9j8tUxjFNfcEit4ZGerNpN, version 49 or later, folder `thumbs/t16_split/`:
`t16_split.py.txt`, `t16_base.py.txt`, `bp_sheet.py.txt`, `examples.py.txt` (save them without `.txt`),
`logo_tight.png`, `art/<dept>.svg`, `samples/<dept>.html` (the approved look per department: open it and match it).

| Dept | Subjects so far |
|---|---|
| ece | ec-signals, ec-vlsi, ec-comm, ec-antenna, ec-optical |
| eee | ec-circuits, ee-pe |
| mech | me-thermo, me-design |
| auto | au-elec, me-ic |

## In a subject's finishing run

1. `make_thumbs.py scan` the lesson html and write one hook per lesson into `thumbs.json` (at most 40 characters, a
   question the lesson answers), with the subject kicker. Do **not** run `make_thumbs.py build`: no t11/t14/t15.
2. Write `work/t16/<sid>/specs.py`: one spec per lesson, built from that lesson's own book worked example
   (`books/<dept>/<sid>/<sid>-u<N>.html` on main, the chapters the lesson covers), every number computed in Python and
   matching the book's answer. Keep subject, topic and hook from `thumbs.json`. Title on 2 to 3 lines, takeaway two
   lines with one gold and one cyan word, card title 30 characters at most, 4 to 5 chips, 2-line summary, a board with
   only the example's objects. No unit or lesson numbers (tag `Book example`), no college names, no two lessons with
   the same picture.
3. `python3 t16_split.py build work/t16/<sid>/specs.py work/t16/<sid>/out` until it prints OK; look at
   `t16_sheet.jpg` and three thumbnails at full size and fix anything crowded, clipped or untrue.
4. Upload sheet: run `make_subject.py ... --thumb t16 --thumbs work/t16/<sid>/out` with the t16-only patch below.
5. Deliver to `deliver/<sid>`: `<sid>/thumbnail/thumbs.json` and, under `<sid>/t16/`, the `<lesson>_t16.jpg` files,
   `t16_sheet.jpg` and `specs.py`. On the computer they go to `B.Tech\<Dept>\<Subject>\thumbnail\` (an old
   `<lesson>_t16.jpg` is first moved to `thumbnail\_to_delete\`).

## make_subject.py: t16-only patch (fix in your local copy)

`make_subject.py` still expects t11/t14/t15 and reports "no thumbnail t11" for every lesson. With `--thumb t16`:
- in the row builder, set `thumbs_other` to `[]` when the style is `t16` (the sheet must not list t11/t14/t15 files);
- in the copy loop (`for st in ('t11', 't14', 't15')`), check and copy only `('t16',)` when the style is `t16`.
It must then print OK with one `_t16.jpg` per lesson.
