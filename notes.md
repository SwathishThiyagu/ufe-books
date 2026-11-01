# Writers' notes on the syllabus data (CSE)

## c-coa-u2

- SRM: its unit 1 ("Introduction", 21CSC211J) lists only "SISC- RISC" (a typo for CISC) and memory models; nothing in it supports the SRM coverage marks on subtopics 2.1–2.4 and 2.6.
- NITT: its unit 2 list is mostly arithmetic (add/sub, multiplication, division, floating point, SSE/AVX), which belongs to Unit 3; only the first four items are ISA. Typo "Parallelissm".
- Whole-course lists: NITK unit 3, Manipal unit 2 and IITD unit 1 each list topics from Units 3–6 (ALU, datapath, control, memory, I/O).
- NITC: the course used, EC2003E, is an ECE 8086 course; its list includes pin diagram, clock and timing diagrams, which do not belong in this unit.
- Anna Univ: unit 5 ("Processing and Pipelining") also lists hardwired/microprogrammed control and pipelining, which are Units 4–5.
- Christ: marked for "Instruction formats and encoding", but its list has no such item; its list mixes Unit 1 and Unit 3 topics.
- Packet `out` (03_Books/…) differs from queue.json `out` (books/…); the book follows queue.json.
- Web lookups failed in the writer's session, so the Sources links were not opened (the page says so).


## c-coa-u1

- IITM is in `taught_at` and `main_course_at` but has no `where` row and is missing from `syllabi_compared`; Manipal is in `syllabi_compared` but has no `where` row.
- IITD (COL2016) and IITB (CS 230) `where` rows put each whole course under "unit 1" with an empty title. IITB's topics have week numbers fused into the text ("FSMs 4 FSM", "…7 Mid-sem Week 8 Superscalar…"); IITB's real unit 1 is logic gates and K-maps, and its von Neumann match comes from week 5.
- NITC `course_used` is "Computer Architecture and Processors (EC2003E)": an ECE 8086 course not in NITC's `course_names`; its "unit 1" list is the whole 40-item course.
- SRM `course_used` is 21CSC211J (Computer Architecture and Operating Systems), not SRM's own "Computer Organization and Architecture" course; "SISC- RISC" is probably a typo for CISC; SRM is marked for bus structures and operational concepts though its list names neither.
- `unis` vs college lists: NITT lists "Performance" but is missing from the performance subtopic's `unis`; NITK is marked for performance, von Neumann/Harvard and the power wall though its three-item list names none; NITT is marked for history and functional units on "Introduction" alone.
- Lists reaching into later units: NITT unit 1 includes Patterson–Hennessy ch. 2 topics (operations, operands, representing instructions, logical ops, decisions) = universal Units 2–3; Christ unit 4 includes memory addresses, signed add/subtract, fast adders, multiplication (Units 2–3).
- Fact to check: the book gives TIFRAC as commissioned in 1960; sources differ (1960 or 1962).

