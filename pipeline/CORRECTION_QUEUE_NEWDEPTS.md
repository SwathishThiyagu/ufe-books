# Correction queue: four new departments (DeepSeek drafts of 21 Nov 2026)

Opus at high effort. Each thread takes the units listed, one at a time in that order, and hands back to the thread
"Prepare four new departments for Nov/Dec exams", one block per unit. Exams: ce-rcc 24 Nov, ae-avionics 25 Nov,
ae-struct 26 Nov, ce-survey and ei-sensor 27 Nov, ch-mass and bm-instr (dates not found), ch-thermo (20 Nov, past).

## Brief (same for every thread)

Correct the DeepSeek drafts of your units (University free n easy; the exam course and the new subtopics are in
`pipeline/EXAM_ND2026_NEWDEPTS.md` on main). Repo SwathishThiyagu/ufe-books with push access; draft branch per unit below.
Follow `pipeline/CORRECTION_BRIEF.md` on main exactly for each unit, reading EXAM_ND2026_NEWDEPTS.md wherever it says
EXAM_ND2026.md: trace every worked example and run every calculation, fix wrong facts, write chapters for any packet
subtopics the draft lacks, cover the exam course topics in the packet's `where`, redraw every figure with real labels via
`pipeline/claude_figs`, apply the notes cleanups and `pipeline/SLOP.md`, write a full step-by-step model answer for every
long question, pass `check_book.py --render`, then merge into the library on main, set queue.json status "ok" and commit
"<unit> book" (pull main first; other threads commit there too). ei-sensor is taught here as the Biomedical course
Sensors and Measurements (BM25C05): give biomedical applications where the exam course asks for them. Never name a
college or university, never count them. Do not commit work/. Keep large outputs out of /mnt/project-files (nearly full).
Reply with the hand-back in the brief, one block per unit.

## Threads

| Thread | Units (draft branch) | Extra |
|---|---|---|
| Correct Aero structures books 4-6 | ae-struct-u4 (free/), ae-struct-u5 (ds/), ae-struct-u6 (ds/) | AE3501 core |
| Correct Aero structures books 1-3 | ae-struct-u1, u2, u3 (ds/) | u1 adds fuselage and tail stress analysis |
| Correct Civil surveying books 3-4 | ce-survey-u3 (free/), ce-survey-u4 (ds/) | u3: chapter 2 is missing from the draft; write it in full from the packet |
| Correct Civil surveying books 1, 2, 5 | ce-survey-u1, u2, u5 (ds/) | |
| Correct Civil surveying books 6-7 | ce-survey-u6, u7 (ds/) | not in CE25C03; last |
| Correct Biomedical sensors books 1-3 | ei-sensor-u1 (free/), ei-sensor-u2 (ds/), ei-sensor-u3 (ds/) | u3 chapter 3 (induction potentiometer, synchros, microsyn) has no worked example |
| Correct Biomedical sensors books 4-6 | ei-sensor-u4 (ds/), u5 (ds/), u6 (free/) | |
| Correct Chemical mass transfer books 3-4 | ch-mass-u3, u4 (ds/) | CH3551 core |
| Correct Chemical mass transfer books 5-6 | ch-mass-u5 (free/), ch-mass-u6 (ds/) | CH3551 core |
| Correct Chemical mass transfer books 1, 2, 7 | ch-mass-u1, u2, u7 (ds/) | Mass Transfer I; last |
| Correct Diagnostic equipment books 1, 5, 6 | bm-instr-u1, u5, u6 | BM3591 core; branches when drafted |
| Correct Diagnostic equipment books 2-4 | bm-instr-u2, u3, u4 | |
| Correct Chemical thermodynamics books 1-2 | ch-thermo-u1 (ds/), ch-thermo-u2 (free/) | u2 draft status "error" (a figure fell back to a box diagram) |
| Correct Chemical thermodynamics books 3-4 | ch-thermo-u3, ch-thermo-u4 (ds/) | |
| Correct Chemical thermodynamics books 5-7 | ch-thermo-u5, u6 (ds/), u7 | Thermodynamics II; last |

Done before this file: ce-rcc-u1..u6 and ae-avionics-u1..u5 had one thread each; ae-avionics-u6 is written in the main chat.
