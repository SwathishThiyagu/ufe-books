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


## c-coa-u6

- Christ: its `where` row is Unit 1 "Combinational Circuits" (K-maps, adders, PAL/PLA), matched only on "ROM", yet Christ is marked as teaching 6.1, 6.2, 6.5, 6.7 and 6.8.
- SRM: the course is an operating-systems one (21CSC211J, Unit 5 "Memory Management"); its last topic is a run-on string of lab experiments pasted from the lab list.
- NITC: the row is an ECE 8086 course (EC2003E, Unit 1); only memory read/write cycles and memory-mapped vs peripheral I/O relate to this unit.
- Whole course listed as one unit: IITD, IITB, NITK and Manipal. NITK's title "Example RISC ISA" does not match its list. IITB's items have week numbers merged in ("SMTs 10 Memory hierarchy including virtual memory 11 More on Caches").
- Likely missing coverage dots: IITB lists "Storage and I/O" but is not marked for 6.6 or 6.7; Manipal lists "Magnetic hard disk" but is not marked for 6.6.
- Standard values written from memory (no web): typical access times in Fig 6.1.1, EEPROM endurance 10⁵–10⁶ cycles, 64 ms DRAM refresh, ~600 MB/s SATA limit.


## c-oop-u3

- SRM: its unit-3 list is mostly Unit 2 and Unit 4 material (constructors, static members, overloading, operator overloading); only the last three items are inheritance, and its abstract-class item belongs to Unit 4.
- NITK: the row is its Unit 1 "Fundamentals of OOP", a whole-course list (exceptions, generics, STL, Factory patterns), with comma-split fragments like "and message passing".
- Manipal: the row is Unit 1 (Java basics, ending at "Inheritance basics"), yet Manipal is credited with virtual bases, interfaces and packages; the Manipal unit that covers packages and interfaces looks missing.
- Anna Univ: the row lists no overriding, interfaces, packages or aggregation, but chapters 3.5 and 3.7–3.9 credit Anna; its title "Inheritance and Compile Time Polymorphism" also covers Unit 4 overloading. Check which Anna course the credit comes from.
- NITC: the course used is EC2021E, which looks like an ECE course code; check it is the right course.
- Christ: `course_names` has a stray prefix, "1 Object Oriented Programming Using C++".
- From memory (web blocked): JEP 513 final in JDK 25; `typing.override` added in Python 3.12. All code examples were compiled and run (g++ 13.3, OpenJDK 21, Python 3.13).


## c-oop-u5

- NITC: course used is "Object Oriented Programming (EC2021E)"; the EC code suggests an electronics course — check it is the right one for CSE.
- Christ: course used is the Python course, yet it is credited for "STL containers" and "Generics in Java", which that unit does not list; `course_names` has a stray prefix "1 Object Oriented Programming Using C++"; its "Decorators and metaclasses" has no subtopic anywhere in the syllabus.
- Anna Univ: credited for "Generics in Java", but its C++ unit does not list generics.
- Anna Univ and NITC: both list "String" (no subtopic covers it), "IO streams" (belongs to Unit 6) and "hashes" (covered as `unordered_map` in 5.4).
- SRM: Unit 4 mixes in inline, friend and virtual functions (Units 2 and 4) and its unit title is empty. Manipal: unit includes multithreading and JavaFX (Unit 6). NITK: its "unit" is the whole course description cut into fragments, including Factory and Abstract Factory (Unit 6).
- From memory (web blocked): Java 5/7 feature dates, Python 3.11/3.12 features, C++23 items (`flat_map`, `std::generator`), Project Valhalla, textbook editions. All programs compiled and run (g++ 13.3, Java 21, Python 3.13).


## c-oop-u6

- NITC: its row is Unit 6 "Templates" (templates, STL, iterators, hashes), which belongs to Unit 5; only "iostreams and other types" maps to 6.1.
- Christ: its row is Python "Advanced OOP Concepts" (packages, exceptions, iterators, decorators, metaclasses), which belongs to Units 3 and 5; only "design patterns" maps to 6.7. Christ is credited with multithreading, events and JavaFX, which its Python course does not list — probably from its "Java Programming" course.
- Manipal: its row lists exceptions and generics (Unit 5) beside threads and JavaFX; Manipal is credited with 6.2 and 6.3 (file streams, binary files) though its row lists no file topics.
- SRM and NITK have no `where` rows but are credited with subtopics (SRM 6.2–6.5, NITK 6.4).
- The JavaFX listing in 6.6 was not compiled (JavaFX not installed); all other C++/Java programs were compiled and run (GCC 13, OpenJDK 21).

