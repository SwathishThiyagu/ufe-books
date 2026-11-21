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


## c-oop-u4

- Manipal: mapped unit is ICT 2122 Unit 3 (exceptions, threads, generics, JavaFX), which matches Units 5 and 6, not polymorphism.
- SRM: Unit 3 row has an empty title and mostly covers constructors, static members and inheritance (Units 2 and 3); only overloading, operator overloading and abstract classes belong here.
- NITK: Unit 1 lists the whole course, down to design patterns, with oddly split items ("and message passing").
- Duck-typing subtopic: its `unis` include Anna, SRM, NITK and NITC, which teach in C++; only Christ lists duck typing — the match was probably made on "dynamic method".
- "Base class pointers to derived class objects" is tagged advanced because only Anna lists it on its own, but every course needs it before virtual functions.
- Christ: `course_names` has a stray "1 " prefix ("1 Object Oriented Programming Using C++").
- Anna and NITC put the this pointer and virtual base classes in this unit; the book sends readers to Units 2 and 3 for those.
- All programs compiled and run (g++ 13.3 C++17, Python 3.13, OpenJDK 21); CS2023 mention in 4.1 is from memory.


## c-coa-u5

- SRM: the `where` row (21CSC211J unit 3, "Process Management") is operating-systems content (scheduling, IPC, synchronisation), matched only through "Multi threading Models" (software threads); SRM's coverage of 5.1, 5.3, 5.7 and 5.9 needs checking.
- IITB and IITD: both rows are the whole course flattened into "unit 1"; IITB's items are mangled weekly-schedule strings ("computer organization 6 Instruction pipelining 7 Mid-sem Week 8 Superscalar processors…").
- NITC: `course_used` is "Computer Architecture and Processors (EC2003E)", an ECE code not in NITC's `course_names`; NITC has no `where` row.
- Anna: credited with all nine subtopics, but its row (CS25C06 unit 6) lists only stages, the timing diagram and hazards.
- Mixed units: Manipal unit 2 and Christ unit 5 mix Unit 3, 4 and 6 content (Booth's algorithm, control unit, cache) with pipelining; NITT unit 3 includes building the datapath (Unit 4).
- From memory (web blocked): Core i7 920 ~14 stages and 130 W, Cortex-A8 ~2 W, Hamacher stage names, MIPS Cause codes 10 and 12, handler address 0x80000180. Cortex-A8 13-stage dual-issue in-order pipeline confirmed by web search.


## c-coa-u4

- Subtopic 4.2 ("Register transfers and executing a complete instruction") is tagged advanced and limited to Manipal and Christ, but it is core basic-processing-unit material that hardwired and microprogrammed control depend on; it should probably carry 4.1's universities and lose the tag.
- NITT is listed for hardwired (4.5) and microprogrammed (4.6) control, but its own list (datapath plus pipelining) names neither.
- IITD (Unit 1, no title, 13 topics), NITK (Unit 3, 27 topics) and Manipal (Unit 2, 21 topics) are whole-course lists, not unit lists; NITK's title "Example RISC ISA" does not match its topics.
- Anna Univ Unit 5 also lists universal Unit 2 (ISA, RISC vs CISC, addressing modes) and Unit 5 (pipelining) material.
- Merged strings: Christ "Restoring and Non Restoring algorithms-Fundamental concepts"; NITT "…Matrix Multiply Hardware Design language". Christ's unit title "Arithmetic & Logic Unit" covers only half its topics.
- NITC `course_used` "Computer Architecture and Processors (EC2003E)" is an EC course not in NITC's course names; SRM, IITM, IITB and NITC have no unit mapping.
- Checked by web search only: Wilkes 1951 microprogramming / EDSAC 2 in 1958; 68000 microcode plus nanocode; Intel 2018 microcode updates for Spectre v2.


## c-coa-u3

- SRM: the row is Unit 1 "Introduction" of a combined architecture and OS course and lists only "Number System" from this unit, yet SRM is tagged on six subtopics (add/subtract, multiplication, division, IEEE 754, ALU, number representation).
- NITC is tagged on all 9 subtopics but has no row for this unit; its course used, EC2003E, is an ECE course.
- Christ Unit 5 mixes Booth and division with Unit 4 and 5 material (hardwired and microprogrammed control, multiple-bus organization, pipelining, data hazards); Christ is tagged on add/subtract, carry lookahead, multiplication and ALU, but its list shows none of them.
- Anna Univ Unit 3 includes digital-logic topics (combinational circuits, multiplexers, decoders) and a cut-off item, "Sequential".
- IITD and IITB rows are each course's whole topic list (unit 1, no title); IITB strings still contain week numbers ("FSMs 4 FSM").
- NITT, NITK and Manipal Unit 2 mix instruction-set topics (universal Unit 2) with arithmetic.
- Worked examples and quiz answers verified by script (Booth, restoring/non-restoring traces, IEEE 754 hex, CLA gate delays); FP16/bfloat16 layouts and IEEE 754-2019 confirmed by web search.


## c-data-u1

- NITK: marked on 1.1, 1.2 and 1.5 but has no Unit 1 `where` row; its course MA255N lists only statistics, EDA, hypothesis tests and dimensionality reduction, so nothing supports these marks.
- NITC: its row is unit 2 "Database for Data Science"; only the first 6 items fit this unit. Keys, normal forms (1NF–3NF) and SQL table operations belong to no unit of this subject; the NoSQL and big-data models belong to Unit 6. Nothing supports its 1.5 mark. Course code EC2023E looks like an ECE course.
- 1.4 "Types of analytics": only Manipal's list names it. Anna, SRM and NITT marks are not supported by their unit-1 lists (Anna matches only through its unit titles "Descriptive Analytics"/"Predictive Analytics"); NITT's mark on 1.2 is also unsupported.
- Whole-course lists: Manipal unit 1 (sampling, hypothesis tests, ANOVA, PCA), IITB's 40-item list and IITD's 25-item list are reused as `where` rows for Units 2–5. IITD's list starts with "Introduction to data science", yet IITD has no Unit 1 row or mark.
- Christ: unit 1 (big data, data lakes and warehouses, ecosystem) overlaps Unit 6.1 and 6.7; its 1.1 mark is weak. Unit 6.1 also overlaps chapters 1.2 and 1.5 (the book cross-references rather than re-teaches).
- SRM: unit 1 is mostly NumPy and Pandas (Unit 2 content).
- Parsing: merged items ("Data Science Process Introduction to Numpy: Numpy", "Index Hierarchy Data Acquisition: …") and fragments ("and transforming data", "and unstructured data"); NITT unit title empty.
- IITM's "Algorithms for Data Science" (not in `syllabi_compared`) looks like a different course; IITD `course_names` include "Modern Data Analytics in Materials Science".


## c-data-u6

- Coverage marks without support: only NITC and Christ have `where` rows; Anna Univ, SRM, NITT, NITK and Manipal are marked on all 6–8 subtopics with no unit list behind the marks.
- NITC: its unit 2 ("Database for Data Science", EC2023E) supports only 6.1 (big data characteristics) and 6.5 (NoSQL models and architecture), yet NITC is marked on all eight subtopics (Hadoop, MapReduce, YARN/Hive/Pig, Spark, warehouses, security). Most of its list (relational databases, keys, 1NF–3NF, SQL, parsing XML in Python) has no home in any unit of this subject.
- Christ: its list (AI742E0 unit 2) has no Hive, Pig, HBase, warehouse/lake or security/privacy items, yet Christ is marked on 6.4, 6.5, 6.7 and 6.8; its "Big Data Integration and ETL Processes" belongs to Unit 2 (data integration and ETL).
- IITM is in `taught_at` and `main_course_at` but missing from `syllabi_compared`.
- From memory (web blocked): NameNode ~150 bytes per file/block, dead-DataNode timeout ~10 min, Laney's three Vs (2001), Hadoop defaults (128 MB blocks, replication 3, 3 s heartbeat). DPDP Act ₹250 crore penalty confirmed by web search.


## c-data-u4

- IITB: the EE 353 unit 1 list covers the whole course (charts, regression, SVM, neural networks); only "Hypothesis testing; t-test; chi-squared test; non-parametric tests" belong here. It lists "chi-squared test" but is not marked on 4.6 because the match phrase "chi square" misses "chi-squared". Nothing supports its marks on 4.2 and 4.3.
- NITT: unit 5 list is time series, anomaly detection and feature selection (Units 5 and 2); its only link here is "chi-square based filtering", the source of its 4.6 mark.
- Manipal: unit 1 list spans Units 1–3 and 5; only sampling distributions, hypothesis tests, ANOVA and confidence intervals belong here. No subtopic owns confidence intervals (covered in 4.2).
- Anna Univ: the `where` row shows only unit 4 (t-tests, F-tests, ANOVA); its marks on 4.1–4.3 must come from another unit — from memory, AD3491 Unit 3 "Inferential Statistics".
- NITK unit 5 lists no estimation topic, yet it is marked on 4.3. SRM and NITC have no `where` row but are marked on several chapters.
- SciPy was not available to the writer; the orchestrator later ran the three SciPy blocks (ttest_1samp, chi2_contingency, f_oneway) with SciPy 1.18.1 and the printed outputs match exactly. From memory: Gosset's 1908 "Student" paper; the 2016 ASA statement on p-values.


## c-data-u3

- IITD, IITB and Manipal: each "unit 1" lists the whole course (SQL/ER, SVMs, neural nets, ANOVA, PCA…), not this unit's topics.
- NITC unit 4: includes its practical-session list with numbering fused into names ("Normalizing a database to normal form 3", "Parsing XML in Python 5"), plus Unit 2 topics (indexing, slicing, reshaping) and Unit 1's "scraping online/website data".
- Anna Univ unit 2 also lists regression, least squares, standard error of estimate, multiple regression and regression toward the mean, which belong to Unit 5.
- NITT is marked on 3.2 and 3.4 but has no `where` row; Christ is in `taught_at` but has no `where` row and no subtopic marks.
- 3.1 is tagged "advanced" with Anna only, but Manipal's "data tabulation" and "distributions" cover the same topic, so coverage looks under-counted.
- Topics with no match phrase: IITB's QQ plots, error bars and bubble charts; NITC's KDE plots (covered in 3.3, 3.7, 3.8).
- The Matplotlib, Seaborn and Plotly code was not run (libraries not installed); the page says so. pandas outputs come from real runs.


## c-data-u2

- Anna Univ: the packet maps AD3491 Unit 1 (data science process); nothing in it backs Anna's marks on 2.1, 2.2, 2.4, 2.7, 2.8. From memory (check): AD3491 Unit 4 "Python libraries for data wrangling" (NumPy, pandas, missing data, hierarchical indexing, combining datasets, pivot tables) is this unit's true home.
- SRM: its unit-2 list has no NumPy or pandas basics, so its marks on 2.1 and 2.2 must come from another unit.
- Subtopic 2.6 is tagged advanced but is core pandas (and Anna's Unit 4 lists it, from memory); consider removing the tag.
- Whole-course lists: IITB EE 353 "unit 1" is the entire course; Manipal unit 1 mixes Units 1, 3, 4 and 5 (hypothesis tests, ANOVA, PCA).
- NITT unit 5 is mostly time-series forecasting and PCA (Unit 5); only anomaly detection and feature selection fit, so nothing supports NITT's marks on 2.3 and 2.5.
- NITK unit 3's plotting items (heatmaps, pair plots, Seaborn, Plotly) belong in Unit 3; Christ unit 2 is Hadoop, NoSQL and Spark (Unit 6), only its ETL item fits 2.9.
- IITD (marked on 2.1, 2.2, 2.8) and IITM (in taught_at) have no `where` row.
- From memory: the 3.5 modified z-score cut-off; one-line summary of the DPDP Act 2023. All code run (NumPy 2.5.3, pandas 3.0.5).


## c-ai-u5

- IITB and NITC have no `where` row yet are marked on 5.1, 5.2, 5.5 (IITB) and 5.1–5.4 (NITC). IITB's course_used "AI and Data Science (CL 205)" carries what looks like a Chemical Engineering code.
- SRM: its row is Unit 4 "Knowledge Representation" (logic); only "Uncertain Knowledge and reasoning Methods" belongs here, but SRM is marked on 5.1, 5.2, 5.4, 5.7.
- NITT: its unit 4 is machine learning (decision trees, SVM, perceptron, MLP) = universal Unit 6; only "Bayesian belief networks" fits, yet NITT is marked on 5.1, 5.2, 5.7.
- NITK: unit 3 "First order logic" is mostly Unit 4 material; marked on 5.8 (non-monotonic and temporal reasoning) but lists neither.
- Manipal: the course is a mechatronics one (MET 3104) with the whole course listed as unit 1; it supports only fuzzy logic (5.7), yet Manipal is marked on 5.1–5.4.
- Anna Univ: marked on 5.7 (fuzzy), but the CS3491 unit 2 list has no fuzzy item.
- IITM: course name "Artificial Intelligence DAXXXX" has a dummy code (book prints "Artificial Intelligence").
- From memory: dates for Reiter, McCarthy, Doyle, Allen, Dempster, Shafer, Zadeh; Rich & Knight contents. Web search confirmed AIMA 4e ch. 12–13 titles and the Sendai fuzzy subway (1987).


## c-dbms-u2

- 2.2 Keys is tagged `advanced` but is core: lists only anna and nitt, yet NITK and Manipal both list "Keys" (the match phrases miss the plain word "Keys").
- 2.5 Set operations / product / joins is tagged `advanced` but is core: lists only nitt, yet NITK ("Complete set of operators", "Additional operators") and Manipal ("Set Operations", "Join Expressions") teach it, as does every algebra course. Both chapters were still written at advanced length (≤900 words) as the standard requires.
- Anna's `where` row (Anna Unit 3) is mostly ER material (participation, weak entities, ER-to-relations, ISA/EER) belonging to Unit 1; only its title's keys belong here.
- SRM's row (its Unit 4) mixes four units: Codd rules and referential integrity fit, but it also lists normalization (Unit 4), indexing and B-trees (Unit 6), PL/SQL (Unit 3) and ACID (Unit 5).
- NITK `course_used` "Systems and Databases (MA300N)" looks like a maths-department course rather than its "Database Systems".
- IITM and Christ have no `where` row; Christ's course shown is "Data Management for Machine Learning".
- Division has no subtopic (implied by NITK's "Additional operators"); covered in 2.6 with the "for all" query.
- From memory: Codd 1970 paper, Codd's theorem (1972), Codd's rules (1985, Computerworld), QBE (Zloof, IBM), Ingres/QUEL.


## c-ai-u4

- Anna Univ: marked on 6 of 8 subtopics but has no `where` row; its `course_used` CS3491 (as recalled) has no logic unit — check which Anna course these marks come from.
- Manipal: marked on 5 subtopics but has no `where` row; its `course_used` "Computational Intelligence for Mechatronics (MET 3104)" is not in its `course_names`.
- IITM: `course_names` entry "Artificial Intelligence DAXXXX" has a dummy code.
- NITK (MA301N unit 3): its list names neither propositional logic, frames/nets/rules, logic programming, natural deduction nor forward chaining, yet it is marked for 4.2, 4.3, 4.7, 4.8; the list also includes Unit 5 topics (conditional independence, variable elimination, fuzzy sets).
- NITT unit 2: marked for 4.3, 4.5, 4.6 with no matching item; the list mixes Unit 3 (game playing, alpha-beta), Unit 1 (goal-based agents) and lab exercises; its items follow Russell–Norvig 1st ed.'s FOL chapter ("representation change" = situation calculus, covered in 4.4).
- SRM unit 4 ends with "Uncertain Knowledge and reasoning Methods" (Unit 5); SRM is marked for forward and backward chaining but lists neither.
- NITC: the whole 40-item course is listed as "unit 1".
- Christ: "Rules based deduction system" suggests Christ should also be marked for 4.6 (forward/backward chaining), but it is not.
- Prolog programs not run (no Prolog installed); SWI-Prolog output punctuation in 4.8 from memory. From memory: 3-SAT ratio ≈4.3, Cook 1971, Coq→Rocq rename. Web search confirmed AIMA 4e (US) ch. 7–10; Wumpus model count (3 of 128) checked by script.


## c-data-u5

- IITD (COL2010) and IITB (EE 353) rows are whole-course topic lists filed as "Unit 1" (crosswalk shows only the relevant part).
- Manipal's row (CES 2103 Unit 1, Introduction to Analytics) is mostly Unit 1–4 material (analytics types, cleaning, hypothesis tests, ANOVA); only "Dimensionality reduction; PCA" belongs here.
- Christ's row (AI742E0 Unit 3: Hive, Pig, Impala, big-data visualization tools) belongs to Unit 6; only "Introduction to Machine Learning on Big Data" fits Unit 5.
- College topics with no universal subtopic: NITT's anomaly detection (distance/density-based outliers, LOF) — covered briefly in 5.1 and 5.6; NITT's feature-selection items — belong to Unit 2; NITK's autoencoder — covered in 5.5 and 5.7; Anna's survival analysis — only in 5.9's Beyond box.
- From memory: Rosenblatt 1958, Minsky–Papert 1969, backpropagation 1986, ID3 1986, CART 1984, Pearson 1901, Hotelling 1933, Fisher 1936, ImageNet 2012, transformers 2017; claim that Anna's AD3491 unit follows Downey's Think Stats. All numbers computed in Python; NumPy/pandas snippets run.


## c-ai-u3

- IITB is marked for 3.1 but has no `where` row; its course_used "AI and Data Science (CL 205)" looks like a chemical-engineering code. Manipal is in `syllabi_compared` with no `where` row; its course_used MET 3104 is a mechatronics course.
- IITM's course name has the dummy code "DAXXXX".
- Marks not supported by lists: Anna marked for 3.3 and 3.6 but lists only "adversarial search; constraint satisfaction problems (CSP)"; NITT marked for 3.5 and 3.6 but its unit-2 list has no CSP item; NITC marked for 3.1 with no game-playing phrase.
- Likely missing marks: 3.2 Minimax — Anna, NITT, Christ (they list games and alpha-beta); 3.4 — Christ ("Bounded Look-ahead Strategy and use of Evaluation Functions") and NITC ("Stochastic Games"); 3.6 — NITC and Christ.
- Lists reaching other units: NITT's and NITK's unit-2 lists are half logic (Unit 4); SRM unit 3 adds agents and rationality (Unit 1); NITC's and Christ's rows are whole-course or multi-unit lists; NITK fuses "Expectimax search Knowledge and Reasoning".
- Game trees, alpha-beta prunes, FC/AC-3 traces, 4-queens counts and cryptarithm answers computed by script. From memory: R&N 4e names and chapters, Knuth–Moore 1975, Mackworth 1977, Appel–Haken 1976, checkers solved 2007, Libratus 2017.


## c-ai-u1

- IITB: CL 205 is a Chemical Engineering probability/statistics course, listed whole as "unit 1"; nothing in it supports IITB's marks on 1.1–1.3.
- Marks with no support in that college's own list: SRM 1.1–1.5; Anna 1.4, 1.5; NITT 1.2, 1.4, 1.7 (1.4 matched "Measure of performance … of search algorithms"); NITK 1.2, 1.7; NITC 1.5. Christ looks unmarked on 1.6 ("General Problem Solving; Characteristics of Problem").
- Lists running into other units: NITC lists its whole 40-item course; Anna, NITT, NITK and Christ include Unit 2–3 search, games and CSP; NITT has lab items pasted in ("Lab Component…", "etc"); SRM's items are run-on strings.
- IITM's course name "Artificial Intelligence DAXXXX" has a dummy code.
- IITM and IITD have no `where` rows; Manipal has none either yet is marked on 1.1, 1.2, 1.3, 1.5, 1.7; its `course_used` (MET 3104, mechatronics) is not in its `course_names`.
- "Toy problems" is tagged advanced only because its match phrases are narrow; these are standard textbook examples (Russell and Norvig class TSP as a real-world problem).
- From memory: R1/XCON 1980, Lisp-machine collapse 1987, Bhashini, AskDISHA, DigiYatra, IndiaAI Mission 2024, NIST AI RMF and ISO/IEC 42001 (2023), Rich & Knight's production-system table.


## c-dbms-u1

- Christ: course used is AI433 "Data Management for Machine Learning" (unit-2 list = ETL and data cleaning); nothing supports Christ's marks on 1.1–1.5 and 1.7. Mapping should use Christ's own "Database Management System" course.
- Anna Univ: the row is unit 3 of CS25C13 with a "title" that is a fragment of the topic list; the same row is reused for Unit 2. Anna is credited for 1.1–1.4 but no Anna row lists database concepts (earlier units missing). SRM same gap: row is unit 2 (ER only, empty title), yet credited for 1.1–1.4.
- IITM is in `taught_at` and `main_course_at` but has no `where` row, is not in `syllabi_compared` and has no marks. IITD is in `syllabi_compared` but has no Unit 1 row, though its whole-course list starts with "Data modeling; database design".
- Whole course listed as "unit 1": IITB (fragments like "and transaction processing"), NITC (25 items), Manipal (37 items). NITK's list also has relational algebra and aggregate functions (Units 2–3); NITK `course_used` "Systems and Databases (MA300N)" is not among its `course_names`.
- Missing marks: 1.6 missing NITT ("relationships; relationship types"), IITB and Manipal; 1.7, 1.8 ("Extended E-R Features") and 1.9 ("Reduction to Relational Schemas") missing Manipal.
- Overlap: 1.5's keys overlap Unit 2's "Keys: super, candidate, primary and foreign keys" (book covers entity-set keys, points to Unit 2).
- Checked by web search only: NPTEL 106105175, CODASYL DBTG report (1971), ISO GQL (2024). From memory: IMS for Apollo (late 1960s); Silberschatz 7e notation details.


## c-ai-u6

- IITM's course name "Artificial Intelligence DAXXXX" has an unfilled code. IITM, IITD and NITK have no `where` rows (NITK has a `course_used`, MA301N).
- Anna Univ's row is CS3491 Unit 5 (neural networks), with lab exercises and outcome text mixed in ("45 PERIODS PRACTICAL EXERCISES", "OUTCOMES"…); nothing in it supports Anna's marks on 6.4, 6.5, 6.7, 6.8.
- IITB's CL 205 row is a probability/statistics unit from a chemical-engineering course; only "Introduction to supervised learning" fits, so its marks on 6.1 and 6.5–6.7 are unsupported.
- NITC and Manipal rows each list the whole course as "Unit 1"; Manipal's course is mechatronics (MET 3104) and its marks on 6.1, 6.8, 6.9 (MYCIN, DART) are not in its list (nearest: "rule-based decision-making").
- Christ's row (Unit 4, Planning and Learning) has no expert-system, MYCIN or DART item, so its 6.8 and 6.9 marks are unsupported; it also lists genetic algorithms (a Unit 2 subtopic).
- SRM topic strings are run together ("Mean Ends analysis Learning", "…models Introduction to expert system").
- NITT's unit lists SVMs (no AI subtopic covers them) and Bayesian belief networks (Unit 5).
- Web search: DART (Stanford with IBM, ~1981). From memory: MYCIN ~450 rules and 0.2 CF threshold, EMYCIN → PUFF and SACON, CLIPS (NASA, 1985).


## c-ai-u2

- 2.7 Genetic algorithms: SRM, NITT and Christ are marked but their listed units have no GA item; NITC lists "Evolutionary Computation" but is not marked.
- 2.6 Local search: SRM is marked, but its unit lists no local search or hill climbing.
- IITB (marked 2.1, 2.6) and Manipal (marked 2.1, 2.5) have no `where` row; IITB's course used is CL 205 (a Chemical Engineering code); Manipal's "Computational Intelligence for Mechatronics (MET 3104)" is not in its course names.
- IITM's course name carries a stub code, "Artificial Intelligence DAXXXX".
- College lists: NITC's row is its whole 40-item course; NITT includes lab fragments ("Lab Component (Exercises similar to the following)", "etc"); NITK's "(RBFS SMA*" has an unbalanced parenthesis; Christ lists "Introduction" twice; Anna's unit also covers adversarial search and CSP (Unit 3).
- No subtopic of their own: memory-bounded search (IDA*, RBFS, SMA*; NITT, NITK, Christ) — covered in 2.5; local beam search (NITK) — in 2.6; NITC's "searching with nondeterministic actions" — short paragraph in 2.1.
- From memory: Dijkstra 1959, A* 1968, simulated annealing 1983, Korf 1985, NASA ST5 evolved antenna, NSGA-II from Kalyanmoy Deb's group (IIT Kanpur). 8-queens hill-climbing rates (~14%, ~94% with sideways moves) computed by script.


## c-dbms-u3

- Joins (3.5): only SRM is marked and the chapter is tagged advanced, but Anna Univ ("join and its types"), NITK ("JOIN operations") and Manipal ("Join Expressions") list joins too — a core topic. The book follows the tag but names all four.
- PL/SQL (3.9): Anna and SRM are marked, but neither list has PL/SQL, cursors, procedures or triggers; SRM is also marked for views but lists none. These marks probably come from units not in the packet. (3.9 runs 1,015 words, mostly code, above the 900-word advanced target.)
- SRM: its unit-3 list includes relational algebra (Unit 2) and functional dependencies (Unit 4).
- NITT: marked for set operations and nested subqueries, but its list only says "Querying in SQL". NITT and NITK both list embedded SQL, which no subtopic covers (short note in the 3.9 lead).
- Christ: marked for 3.1, 3.2, 3.6, 3.8 but has no `where` row; its course (AI433, "Data Management for Machine Learning") is not a DBMS course.
- IITM, IITD, IITB and NITC: no `where` rows and no coverage on any chapter, though IITB's CS 317 lists SQL.
- NITK's row is its Unit 2 "Normalization" from MA300N (mixes Unit 4 with SQL; MA300N is not among NITK's course names). Manipal's row is its whole course.
- Web search: MySQL ignored CHECK before 8.0.16. From memory: SQL*Plus exit commits, ADD_MONTHS end-of-month rule, MOD sign with negatives, quoted Oracle error messages, SQL Server allowing one NULL in a UNIQUE column.


## c-dbms-u4

- IITM: in `taught_at` and `main_course_at` but has no `where` row and is missing from `syllabi_compared`.
- SRM: its Unit 4 mixes in Codd rules and referential integrity (Unit 2), indexing, ISAM and B-trees (Unit 6), PL/SQL (Unit 3) and ACID (Unit 5); unit title empty. Credited for 4.2 and 4.6 but its list names no FDs or decomposition.
- Probably missing coverage dots: IITB lists "Relational database design and normalization" but is credited only for 4.1; NITC lists "Normal Forms" but is not credited for 4.4 or 4.5.
- Manipal: credited for 4.2, 4.6, 4.7, but its list has only "Features of Good Relational Design" and "Atomic Domains and Normalization" (credit probably from another course or unit).
- Christ: course used is an AI course (AI433) whose only matching item is "Schema design and data normalization", yet Christ is credited for 4.2, 4.4, 4.5.
- Anna Univ: the CS25C13 row names no minimal cover, MVD/4NF or JD/5NF, yet Anna is credited for 4.3, 4.7, 4.8.
- NITK: course used "Systems and Databases (MA300N)" has a maths code and is not in NITK's `course_names`; its Unit 2 also lists SQL topics (Unit 3).
- Whole course listed as "unit 1": IITD, IITB, NITC, Manipal.
- Web search: Armstrong 1974, BCNF 1974, Fagin's 4NF paper (1977). From memory: Fagin's 5NF paper (1979), Kent 1983.


## c-algo-u3

- Fractional knapsack: NITT ("Knapsack problem" in its greedy unit 2) and NITK ("Knapsack Problem" right after "Elements of Greedy Strategy") are probably missing from this subtopic's `unis`.
- Anna Univ: credited for MST, Dijkstra and optimal merge patterns, but its CS25C12 unit 3 list names none of them; "Knapsack 0" is a cut-off "0/1"; `course_names` has the fused "Algorithmsforvlsiphysicaldesignautomation".
- IITM: in `taught_at` and `main_course_at` but has no `where` row and is not in `syllabi_compared`.
- Whole-course lists: IITD and IITB as unit 1 with empty titles; NITK's unit 2 title "Recurrences, Analyzing recurrences" does not match a list running to FFT and NP-completeness; NITC's unit 1 is its whole course; Manipal's unit 3 title "Conquer, Decrease and Conquer" is cut off and its list spans Units 2 and 4–7.
- SRM: unit 3 includes "Tree traversals" (not greedy) and dynamic-programming topics (Unit 4), with items run together ("Prims algorithm Introduction to dynamic programming").
- Topics no subtopic owns: NITK's Bellman–Ford (covered briefly in 3.6); NITC's Horn formulas (in 3.1).
- Web search: Duan et al. O(m log^(2/3) n) shortest paths, STOC 2025 best paper. From memory: Huffman 1952, Dijkstra 1959, Borůvka 1926. C and Python programs compiled and run (gcc 13.3, Python 3.13).


## c-dbms-u5

- No `where` row, but credited: Manipal for 5.1 and 5.3–5.6; Christ for 5.1, 5.3, 5.4, 5.8, 5.9 (including ARIES) — Christ's course used, "Data Management for Machine Learning (AI433)", is an unlikely source for ARIES. IITM has no row either.
- Likely missing coverage dots: NITK lists "database recovery management" and NITC lists "Database recovery concepts and techniques", but neither is credited for 5.8 or 5.9; NITC lists "Optimistic Concurrency Control" (covered in 5.5) but is not credited there.
- Dots the lists do not support: NITT credited for 5.6 deadlocks but lists none; SRM credited for 5.1, 5.2, 5.5 but its list has no states, no ACID (in its Unit 4) and no timestamps; Anna credited for 5.7 granularity and 5.9 but its list has only "Isolation Levels" and a cut-off "Log-Based".
- SRM's row mixes in PL/SQL items (Unit 3) and database security, mandatory access control and multilevel security, which no subtopic in the universal syllabus covers; its item "Two-Phase Control Commit" confuses two-phase locking with two-phase commit (the book flags this in a trap).
- Whole-course lists: IITD, IITB and NITC rows are each a whole course filed under "unit 1".
- From memory: default isolation levels (PostgreSQL and Oracle READ COMMITTED, InnoDB REPEATABLE READ), PostgreSQL deadlock_timeout 1 s and error 40P01, MySQL error 1213 and InnoDB victim choice, paper years (Härder–Reuter 1983, Eswaran et al. 1976, Kung–Robinson 1981, ARIES 1992, Berenson 1995).


## c-algo-u1

- IITM is in `taught_at` and `main_course_at` but has no `where` row, no `course_used`, and is missing from `syllabi_compared`.
- `course_names` mixes in other courses: a garbled Anna name ("Algorithmsforvlsiphysicaldesignautomation"), IITB Game Theory, NITT/NITK Randomized Algorithms, NITK Approximation Algorithms, NITC Algorithmic Graph Theory; Christ appears twice (singular "Algorithm").
- Whole course as one unit: IITD, IITB and NITC rows are whole courses as "unit 1" with empty titles (NITC's follows Dasgupta–Papadimitriou–Vazirani's chapters); NITK's row is its unit 2, running from divide and conquer to NP; Manipal's list is cut off at "Divide and".
- Coverage dots the rows do not support: Anna on 1.1, 1.2, 1.4, 1.6, 1.8; SRM on 1.8 (no master theorem listed); NITK on 1.1 and 1.3–1.6 (its unit 1 row looks missing); NITC on 1.1 and 1.4–1.6; Manipal on 1.1 and 1.2 (probably its unit 1); Christ on 1.1.
- Topics belonging elsewhere: Anna "probabilistic analysis" and IITB/NITC "lower bounds" belong in Unit 7; NITT "Tournament method" belongs with Unit 2's "Finding maximum and minimum"; NITT "pre-processing of coefficients" has no subtopic (covered briefly with Horner's rule in 1.6).
- Typos: SRM "O, O, Ө, ω, Ω" (second O should be little o); SRM "Solution of recurrence relations" appears three times; SRM lists little-omega, which the 1.5 title omits (chapter covers it); Christ items split mid-phrase ("Polynomial Vs" / "Exponential Algorithms", "Average" / "Best and Worst case complexity").
- Course codes to check: Christ's `course_used` is a BCA course (BCA433) in a B.Tech-scope subject; NITK's MA251N looks like a maths-department code.
- Web search: CLRS 4e (2022) has Akra–Bazzi in Section 4.7; KeY Timsort bug 2015. From memory: Knuth's five properties, notation history, Bentley–Haken–Saxe 1980, 2008 Gödel Prize (smoothed analysis), 2011 hash-flooding, quicksort ≈1.39 n log₂ n. C programs compiled and run (gcc 13.3).


## c-algo-u2

- NITC is missing from two `unis` lists: its "Multiplication of two numbers" belongs in 2.6 (now Anna only) and "Maximum Sum Contiguous Subsequence" in 2.7 (now SRM only, listed under both D&C and DP).
- Topics no universal subtopic covers: SRM's "closest pair problem"; NITC's "Medians", "Order statistics" and "Selection in expected/worst-case linear time".
- Anna CS25C12 unit 2 lists only merge sort, long integer multiplication, Strassen, master method and job sequencing; its marks on 2.2, 2.4, 2.8, 2.9 and quick sort are unsupported. Job sequencing belongs in Unit 3 and the master method in Unit 1 (SRM also lists a master theorem proof).
- Other unbacked marks: NITT on 2.2 and 2.3 (list has only "Divide and Conquer method" and Strassen); NITK on 2.4 (no max-min item).
- IITD, IITB and NITC rows are whole-course lists under "unit 1" with empty titles; NITK unit 2 is also whole-course; Manipal unit 3 ("Conquer, Decrease and Conquer", title looks truncated) lists the rest of its course.
- Anna `course_names` has a run-together entry, "Algorithmsforvlsiphysicaldesignautomation".
- The three advanced chapters run 917–947 words (slightly above the 900 target). All programs run and traces checked by script. From memory: matrix-multiplication exponent just below 2.372, AlphaTensor 47 multiplications (4×4 mod 2), Karatsuba 1960, Harvey–van der Hoeven 2019.


## c-algo-u4

- Anna Univ: "Knapsack 0" is "Knapsack 0/1" cut at the slash; its unit lists no Floyd–Warshall or TSP, yet Anna is credited for 4.6 and 4.8; `course_names` includes the run-together "Algorithmsforvlsiphysicaldesignautomation".
- SRM: its unit lists no Floyd–Warshall or TSP but SRM is credited for both; first item is three topics run together; "Prims algorithm Introduction to dynamic programming" is two items fused.
- NITK: the row is the whole course (25 items); credited for 0/1 knapsack and Floyd–Warshall, but its "Knapsack Problem" sits under Greedy (likely fractional) and its graph items are Bellman–Ford and Dijkstra, not Floyd.
- Manipal: TSP and the second "Knapsack Problem" sit under Branch and Bound (Unit 5), yet Manipal is credited for 4.8; unit title "Conquer, Decrease and Conquer" is a fragment and the list spans most of the course.
- Christ: "optimal parameterization" should be "optimal parenthesization"; Christ is credited for 0/1 knapsack, which its list does not name.
- NITC: credited for TSP, but no TSP item appears in its list.
- Whole course as "unit 1": NITC (40 items), IITD, IITB.
- NITT: "longest common subsequence Multistage graphs" is two items fused.
- IITM has no `where` row.
- From memory: Roy 1959, Warshall 1962, Floyd 1962, Held–Karp/Bellman 1962, CLRS 3e ch. 15 and 25. All numbers computed by script; C programs compiled and run (gcc 13.3).


## c-algo-u5

- Anna Univ's Unit 5 ("Solvability and Tractability") mixes P, NP and NP-complete topics (this subject's Unit 7) with backtracking and branch and bound; it is effectively Units 5 and 7 combined.
- SRM's Unit 4 list includes graph searches (DFS/BFS, Unit 6) and Floyd–Warshall (Unit 4), and repeats "Travelling salesman problem using branch and bound example" three times.
- NITT's row (Unit 5, "NP Problems") is the NP-completeness unit and belongs to Unit 7; NITT is credited on the Hamiltonian-cycles chapter only because "Hamiltonian cycle" appears there as an NP-complete problem, not as backtracking.
- Manipal's Unit 3 list ("Conquer, Decrease and Conquer") covers the whole course, insertion sort to TSP; the title looks wrong.
- Christ's Unit 5 also lists random number generators and primality testing (Units 6 and 7).
- Web search: 27-queens count computed at TU Dresden (2016); Concorde's optimal pla85900 tour (2005–06). From memory: Knuth 1975, Kuhn 1955, Land and Doig 1960. N-Queens C program compiled and run; all bounds and counts checked by script against brute force.


## c-algo-u6

- Anna Univ: the row is Unit 4 (string matching and convex hull) and supports only 6.7–6.9; its convex hull (Unit 2) and multithreaded-algorithms items belong elsewhere. Nothing supports Anna's marks on 6.2–6.6 (possibly an Anna unit missing from the packet).
- SRM: the row is Unit 5 (randomized, approximation, NP-completeness = Unit 7 material); only Rabin–Karp fits. The BFS/DFS mark seems to come from the lab list pasted in as the last topic.
- NITK: course code MA251N looks like a maths course — check it is the right one. The row (Unit 2, "Recurrences") lists the whole course; only FFT and Rabin–Karp fit; nothing supports its marks on 6.1, 6.2, 6.3, 6.5, 6.6.
- NITC: whole course as Unit 1, in Dasgupta–Papadimitriou–Vazirani chapter order; supports 6.8 and 6.9; flows (6.5, 6.6) appear only indirectly via "Linear Programming and Reductions".
- Manipal: title "Conquer, Decrease and Conquer" is truncated; its string-matching item is Horspool's input enhancement, not naive or Rabin–Karp (short Horspool section added to 6.7); the list also carries Unit 3–5 topics.
- Christ: "Lower Bound Theory" belongs to Unit 7; "Essential" is a stray fragment; Christ is marked for 6.9 with no matching item.
- 6.6 (push-relabel and min-cost flow): no college list names either topic.
- 6.1 (advanced) runs 939 words, slightly above the 900 target. From memory: AKS (IIT Kanpur, 2002), Cooley–Tukey 1965 and Gauss ~1805, Lamé's bound, push-relabel bounds, the 2022 almost-linear max-flow result, ML-KEM using the NTT. All numbers and code outputs computed/run in Python.


## c-dbms-u6

- NITK is in `taught_at` and credited on 6 of these subtopics but has no `where` row; IITM has none either. NITK's `course_used` "Systems and Databases (MA300N)" looks like a maths-department course rather than its DBMS course.
- SRM's Unit 4 list mixes in Units 2–5 material (Codd's rules, normalization, PL/SQL, ACID); only "Indexing: Primary, Secondary, Multilevel; ISAM, B-Trees" belongs here.
- IITD, IITB, NITC and Manipal rows are whole-course topic lists labelled "unit 1".
- IITB's list covers key-value stores, distributed storage, replication and MapReduce, but IITB is missing from 6.8 and 6.9; IITD lists NoSQL but is missing from 6.9.
- Christ's row is AI433 Data Management for ML (nothing on indexing, hashing or distributed databases), yet Christ is credited for 6.3, 6.5, 6.8 — probably matched from another Christ course.
- Manipal's 6.1 (RAID) credit seems to come from "Data Storage and Querying" and "Storage" (recovery), not RAID; its "Measure of Query Cost" fits 6.7, but Manipal is not credited there.
- From memory (no lookups): RAID 1988, Bayer–McCreight 1972, Fagin 1979, Litwin 1980, Selinger 1979, CAP/Gilbert–Lynch 2002, MongoDB 4.0 transactions (2018), GQL (2024).


## c-ml-u6 (Codex, 5 Nov 2026)
- Packet `out` path is stale (old 03_Books/ path); queue.json holds the right one.
- Neighbouring syllabus lists mix clustering and instance-based learning, which belong to other ML units.


## ec-signals-u6 (Claude correction pass, 20 Nov 2026)
- Packet: no new subtopics for this unit; the exam course lists DFS, DTFT, z-transform and properties, and LTI analysis with z, all covered by chapters 6.1, 6.2, 6.4, 6.5 and 6.7.
- Packet `out` path is stale (old 03_Books/ path); queue.json holds the right one.
- The exam course also lists "Discrete-time signals and systems" and the sampling topics in the same unit; those live in the Sampling unit of this subject.


## ec-signals-u3 (Claude correction pass, 20 Nov 2026)
- Packet: no new subtopics for this unit. The exam course's unit 3 is "Fourier Transform & Laplace Transform": its Fourier topics (aperiodic transform, standard and periodic signals, properties, Hilbert transform and properties) are covered here, its Laplace topics in the Laplace transform unit.
- Frequency response, distortionless transmission and correlation are not in the exam course's list for this unit; they stay as chapters for the other syllabi.
- Packet `out` path is stale (old 03_Books/ path); queue.json holds the right one.

## ec-signals-u4 (Claude correction pass, 20 Nov 2026)
- Packet: no new subtopics for this unit; the exam course lists Laplace transforms, ROC, properties and the inverse transform (chapters 4.1 to 4.3). Its later unit "Continuous-Time LTI Systems" lists "Analysis of LTI System using Laplace and Fourier transforms", which chapter 4.4 covers (transfer function, poles and zeros, causality and stability, complete response, frequency response).
- The unit map (render.unit_map) cuts chapter titles at four words, so two boxes read "Properties of the Laplace" and "Inverse Laplace transform by"; a pipeline matter, not a packet one.

## ec-signals-u5 (Claude correction pass, 20 Nov 2026)
- Packet: no new subtopics for this unit. The exam course's practical sampling and aperture effect are covered in "Low-pass, band-pass and practical sampling" (natural vs flat-top sampling, the sinc droop with a worked example, inverse-sinc compensation). Its "Discrete Fourier series, DTFT, Z-transform and analysis of LTI systems using Z" belong to the subject's Z-transform and discrete Fourier analysis unit, so this book only points to them.
- "Quantization of sampled signals" is tagged advanced (one syllabus), but it is on the exam course's list; the chapter is kept full length.
- Packet `out` path is stale (old 03_Books/ path); queue.json holds the right one.

## ec-signals-u2 (Claude correction pass, 20 Nov 2026)
- Packet: no new subtopics for this unit. The exam course's unit "Continuous-Time LTI Systems" lists CT systems and their properties (covered in the classification unit), LTI systems, impulse response and convolution (chapters 2.1 to 2.3) and "Analysis of LTI System using Laplace and Fourier transforms" (Laplace transform analysis and Fourier units; chapter 2.6 now previews H(jω) and H(s) of the RC circuit and points there by topic).
- Packet `where` parsing: the Manipal entry's unit title is "Total Number of contact hours" and its topic list is the whole course; the IIT Delhi and NIT Surathkal entries also list whole courses under unit 1. These lists set no extra depth for this unit.
- Packet `out` path is stale (old 03_Books/ path); queue.json holds the right one.
- render.block puts a formula longer than 46 characters in a <pre> with its tags escaped, so a long formula with <sub>/<sup> prints raw tags; this book uses Unicode sub/superscripts in long formulas.


## ec-signals-u1 (Claude correction pass, 20 Nov 2026)
- The exam course's unit 1 topics list no system classification or system properties; chapters 1.5 and 1.6 stay for the other syllabi (that course likely teaches them with LTI systems).
- Its "Analogy between vectors and signals" was missing from the draft; chapter 1.7 now carries it (component c12 and the best approximation).
- Packet `out` path is stale (old 03_Books/ path); queue.json holds the right one.


## ec-circuits-u3 (Claude correction pass, 20 Nov 2026)
- Packet: no new subtopics for this unit. The exam course (EE25302) spreads this unit over its units "Phasors and AC steady state analysis" (chapters 3.1 to 3.4) and "Three phase circuits" (chapters 3.6 and 3.7); the three-phase chapter now has a 3-wire/4-wire unbalanced star example with a broken neutral, R-Y-B naming throughout, a phasor diagram, and an unbalanced delta long question with wattmeter readings.
- Packet `out` path is stale (old 03_Books/ path); queue.json holds the right one (books/ece/ec-circuits/). The coordinator's note said books/eee/; the book follows queue.json like the other library books.
- Packet `usual_sem` is 2 (the "Usually Sem 2" chip); the EE25302 exam course sits in semester 3.
- Packet `where` parsing: the Manipal, IIT Delhi and NIT Trichy entries list whole courses under one unit; they set no extra depth here. The Manipal unit title is "Total Number of contact hours".
- The draft's resonance long question belonged to the resonance unit; it was replaced by an unbalanced delta question.

## me-thermo-u1 (Claude correction pass, 20 Nov 2026; first of subject)
- Packet: no new subtopics for this unit. The exam course (ME25301) unit 1 also lists the continuum, the state postulate, state diagrams, the ideal gas equation of state and the thermodynamic temperature scale: covered in chapters 1.1, 1.3 and 1.5, with the full treatment left to "Ideal and real gases; equations of state" and "Thermodynamic temperature scale" by topic name.
- The packet's `where` also carries ME25301 unit 2 (energy, heat and work modes, moving boundary work, first law, steady and unsteady flow). Chapters 1.6 and 1.7 cover heat, work, the work modes and moving boundary work; the rest belongs to the First Law unit.
- Packet data: the SRM entry (UPY23203J Heat and Thermodynamics, unit 4) is a physics course and includes a lab item ("Carey Foster Bridge"), so it belongs to another subject; the IIT Delhi and NIT Surathkal entries list the whole course under unit 1. They set no extra depth here.
- Packet `out` path is stale (old 03_Books/ path); queue.json holds the right one.
- Web links could not be re-opened from this workspace (proxy refused); the three kept are the ones the draft run had opened, and the unverified Khan Academy link was dropped.

## me-thermo-u3 (Claude correction pass, 20 Nov 2026)
- Packet: new subtopic "Entropy generation and second-law analysis of control volumes" written as chapter 3.9 (closed-system and steady-flow entropy balance, lost work T₀S_gen, and the microscopic view S = k ln W the exam course lists); the third law moved to 3.10.
- The exam course (ME25301) unit 3 also lists the limitations of the first law and perpetual motion machines (now in 3.2, PMM1 against PMM2) and exergy analysis of closed and open systems, which belongs to "Available and unavailable energy" and "Exergy analysis and second law efficiency" and is named there by topic.
- Packet data: the SRM entry (UPY23203J Heat and Thermodynamics) is a physics course and lists thermodynamic potentials and the Joule-Kelvin coefficient under this unit; the IIT Delhi and NIT Surathkal entries list whole courses under one unit. They set no extra depth here.
- Several of the draft reviewer's "high" flags (ch 3.7 missing inequality, ch 3.9 missing exponents) were artefacts of its plain-text view stripping "<" and tags; the book itself was right there. The real errors were the long formulas printing raw <sub> tags, the 3.1 example's reversed device, the 3.5 gas-thermometer and 3.9 steam-table claims, and a C program in the 3.8 example.
- Web: MIT OCW (university-hosted) and an unopened Khan Academy link dropped.

## me-thermo-u2 (Claude correction pass, 20 Nov 2026)

- Packet: new subtopic "Unsteady flow processes: filling and emptying of vessels" written as chapter 2.7 (USUF mass and energy balances, filling an empty tank to γTᵢ, adiabatic discharge following the reversible adiabatic law); the draft's limitations chapter moved to 2.8.
- Exam course (ME25301) unit 2 topics covered: forms of energy and Q − W = ΔE (2.1), moving boundary work and free expansion (2.1), first law for closed systems and control volumes (2.1, 2.6), steady and unsteady flow (2.6, 2.7). Heat, work modes and reversible processes belong to other units and are named there by topic.
- Packet data: "Specific heats of gases" and "Perpetual motion machine of the first kind" are tagged advanced, though PMM-1 is in most first-law textbooks as a one-line corollary. The SRM entry (UPY23203J Heat and Thermodynamics) is a physics course, and the IIT Delhi and NIT Surathkal entries list whole courses under one unit.
- Draft errors fixed: the bank's isothermal-vs-adiabatic compression outline (a closed-system adiabatic needs less boundary work to the same pressure), the free-expansion question ("same whatever the gas" holds for U₂ = U₁, not T₂ = T₁), an unnamed refrigerant (now R-134a), q = Δh for every no-work device, PMM-1 lead, Unit/Chapter cross-references. MIT OCW link dropped.

## me-thermo-u6 (Claude correction pass, 20 Nov 2026)

- Exam course: ME25301 Engineering Thermodynamics has no cycles unit (pipeline/EXAM_ND2026.md), so this book serves the other syllabi; the packet's exam entry is ME25C11 Applied Thermodynamics unit 3 (Carnot, Otto, Diesel, Dual and Brayton cycles, air standard efficiency, MEP, comparison), all covered in chapters 6.1 to 6.4.
- Packet data: the NIT Trichy list for this unit also has psychrometric properties and the chart, which the universal syllabus puts in "Pure Substances and Gas Mixtures" (Psychrometry); the IIT Delhi and NIT Surathkal entries list whole courses under one unit.
- The DeepSeek draft had no chapter 1 and no unit sections; its chapter states were used only as material. Its flagged errors (Dual cut-off ratio, the comparison's "gas cools" reason and drafting leftover, pump-work factor, wet-exhaust check, open-heater pump, compressor-with-liquid sentence, absorption component count, two-temperature absorption COP) are all gone.
- Property values: steam from IAPWS (they match the common SI steam tables to the printed digits; interpolated superheat values may differ by about 1 kJ/kg), R-134a with the IIR reference (h = 200 kJ/kg for saturated liquid at 0 °C; tables with another reference shift every h by a constant).
## me-thermo-u4 (Claude correction pass, 20 Nov 2026)

- Packet: two new subtopics written as full chapters: 4.3 "Exact differentials, reciprocity and cyclic relations" (exactness test, δq inexact and ds exact with two traced paths, reciprocity and cyclic relations checked for air) and 4.7 "Expansivity, compressibility, Mayer relation and Joule-Thomson coefficient" (β, κT, κs, cp − cv = Tvβ²/κT with water at 25 °C, γ = κT/κs, μJT with a van der Waals nitrogen example and inversion temperature). The draft's 4.3 to 4.5 moved to 4.4 to 4.6; the draft's Maxwell chapter now carries the TdS equations and energy relations, and its throttling section moved to 4.7.
- Exam course (ME25301) coverage: exergy analysis of closed and open systems (4.2, closed-tank and turbine examples); reciprocity and cyclic relations, Helmholtz and Gibbs functions, Maxwell relations, Clapeyron and Clausius-Clapeyron, volume expansivity, isothermal and adiabatic compressibility, Mayer relation and Joule-Thomson coefficient all have chapters.
- Draft errors fixed: 4.1 example step (1000 × 0.6 written for 1000 × 0.4), dead state now includes rest, height and chemical equilibrium, the Gibbs chapter's claim that −ΔG bounds turbine shaft work, the "kJ/kg K" units trap for A and G, the garbled throttling sentence, van der Waals μJT units, dT/dp vs dp/dT for ice, and the 4.6 figure caption that showed a model value as data.
- Packet data: the SRM entry (UPY23203J Heat and Thermodynamics) is a physics course; it lists the Joule-Kelvin coefficient for van der Waals gases, which set the depth of 4.7. The `where` list also carries ME25C11 unit 2, which belongs mostly to the first- and second-law units.
- Web: MIT OCW (university-hosted) dropped; the three kept links are the ones the draft run had opened (the proxy refused new fetches here). Not independently verified: water β = 2.57 × 10⁻⁴ K⁻¹ and κT = 4.52 × 10⁻¹⁰ Pa⁻¹ at 25 °C (given as data in the example) and nitrogen's measured maximum inversion temperature "near 620 K".
## ec-circuits-u1 (Claude correction pass, 20 Nov 2026)

- Exam course (EE25302) topics for this unit covered: types of sources (ideal and practical, independent and dependent, V-I lines) in 1.2; series-parallel review including L and C in 1.5; star and delta transformation with an unbalanced bridge in 1.6. Mesh and nodal analysis with dependent sources and supermesh/supernode belong to the network-theorems unit; locus diagrams to the resonance unit.
- Packet data: the subject is listed under ECE (`books/ece/`, crumb "Electronics & Communication") although EE25302 is an EEE course; queue.json's out path was kept. "Network topology: graphs, tie-sets and cut-sets" is not in the EE25302 unit topics but is in the other syllabi, so it stays a full chapter. The NIT Calicut unit entry lists transient analysis, which belongs to the transient-analysis unit.
- Draft errors fixed: 1.4 worked example (series pairs denied, "each chord closes a mesh"), 1.5 first trap (its "wrong" formula was the right one), 1.6 power warning and balanced trap, 1.7 arrow sentence and simulator claim, 1.8 "smallest set" lead, missing connectedness condition and "bad data" claim; formula lines that would print raw sub/sup tags. MIT OCW, Khan Academy and ibiblio links dropped.



## ec-circuits-u4 (Claude correction pass, 20 Nov 2026)
- Packet: new exam subtopic "Locus diagrams of RL, RC and RLC circuits" (EE25302) written as a new chapter 4.5 (current circles for R or X varied, series RLC with frequency varied, parallel branches and the two resonant settings, two worked examples); the draft's mutual inductance, dot convention, transformer and magnetic circuit chapters moved to 4.6 to 4.9.
- Packet `out` path is stale (old 03_Books/ path); the book follows queue.json (books/ece/ec-circuits/) like ec-circuits-u3. The coordinator's note said books/eee/.
- Draft data error: the bank question with coils of 0.4 H and 0.9 H gave 1.5 H aiding and 0.9 H opposing, which no single M satisfies (aiding − opposing = 4M and the sum = 2(L₁ + L₂) = 2.6 H). Now 1.6 H and 1.0 H, so M = 0.15 H and k = 0.25.
- Draft errors fixed: the series-parallel resonance formula, R_D = r(1 + Q²) for the practical tank, the energy form of Q, f₁f₂ = f₀² and exact half-power points against f₀ ± BW/2, the effect-of-Q table, "magnetic pressure" for MMF, the k ≤ 1 proof. MIT OCW link dropped.

## ec-circuits-u5 (Claude correction pass, 20 Nov 2026)
- Packet: no new subtopics for this unit (still 9 chapters). The exam course (EE25302) unit "Solution of First and Second Order Networks" is covered in full: series and parallel RL, RC and RLC equations, initial and final conditions, forced and free response, time constants, steady and transient state, and Laplace transforms for circuits.
- Packet `out` path is stale (old 03_Books/ path); queue.json holds the right one (books/ece/ec-circuits/). The coordinator's note said books/eee/; the book follows queue.json like the other library books.
- The draft's MIT web sources were dropped (university-hosted); OpenStax and Khan Academy remain. No link could be opened from the sandbox, so no new links were added.

## ec-circuits-u6 (Claude correction pass, 20 Nov 2026)
- Packet: no new subtopics for this unit (still 8 chapters). The exam course (EE25302) two-port unit also lists resonance; this subject teaches resonance in its resonance and coupled-circuits book, so it was not repeated here. Network synthesis (Foster and Cauer) is in the packet but not in the EE25302 list; it was kept and corrected.
- The draft's MIT and NPTEL web sources were dropped (university-hosted); All About Circuits and Khan Academy remain. The sandbox proxy blocked every page, so no link was reopened and none was added.

## ec-circuits-u2 (Claude correction pass, 20 Nov 2026)
- The packet on main adds "Compensation theorem" as subtopic 7 (from the exam course); the draft had no chapter for it, so chapter 2.7 is new and AC applications moved to 2.8. Only a few syllabi list compensation; the chapter says so without naming any.
- The draft's state had review7.json for the AC chapter; it is now review8.json.
- Packet `out` path is stale (old 03_Books/ path); queue.json holds the right one (books/ece/ec-circuits/).
## me-thermo-u5 (Claude correction pass, 20 Nov 2026)
- The packet was built from ME25C11 Applied Thermodynamics; the exam course ME25301 unit 4 covers pure substances, property diagrams, the Gibbs phase rule, tables and charts, real gases, van der Waals, Z and the generalized chart, but not gas mixtures or psychrometry. Chapters 5.9 and 5.10 stay for the other syllabi.
- The Gibbs phase rule (new in the packet) is chapter 5.3; the draft's chapters 5.3–5.9 moved to 5.4–5.10.
- Draft errors fixed: v_g at 1 atm 1.673 m³/kg (not 1.694), the 0 °C / 0.5 kPa triple-point example, the steam calorimeter limits, and the psychrometry bank answer (30 °C DBT, 20 °C WBT gives w 0.0105, φ 40 %, dew point 14.8 °C).
- Packet `out` path is stale (old 03_Books/ path); queue.json holds the right one.

## me-ic-u4 (Claude correction pass, 21 Nov 2026)
- The exam course AU25301 holds this material in its unit 5 (cooling system types, coolant properties, crankcase ventilation, lubrication, supercharging and turbocharging) together with stratified charge, LHR, HCCI and RCCI engines, which the universal syllabus keeps in the emissions and advanced combustion unit.
- Crankcase ventilation (new in the packet) is chapter 4.5; the draft's chapters 4.5–4.8 moved to 4.6–4.9.
- "Thermosyphon, forced circulation and pressure cooling; coolants" is still tagged advanced (one university), but the exam course lists cooling system types and coolant properties, so the tag no longer fits; consider removing it.
- Draft errors fixed: thermosyphon densities (992.2 and 971.8 kg/m³, Δp 80 Pa), physically impossible blower outlet temperatures (340 K at ratio 1.6, 320 K at 1.5), turbo mechanical efficiency 0.65 (now 0.95), pressure-cap "3 °C per 10 kPa", roots blower description, SAE grade definition.
## me-ic-u5 (Claude correction pass, 21 Nov 2026)
- The exam course AU25301 has no engine-testing unit (its unit 5 is cooling, lubrication, crankcase ventilation, boosting and advanced engines, which sit in me-ic-u4 and u6), so no exam subtopic was added here; the book follows the packet and the older AU3303 testing unit.
- Draft errors fixed: heat-balance exhaust flows that implied air-fuel ratios of 44 to 66, a bank Morse test with negative friction power, a bank heat balance with a negative remainder, a 30 mm orifice giving 44 % volumetric efficiency, bmep key term with "n = 4", BP key term with N in rev/s, a timing figure where the retarded curve beat MBT, and the rope-brake dead-weight mix-up.
- Packet `out` path is stale (old 03_Books/ path); queue.json holds the right one.
## me-ic-u1 (Claude correction pass, 21 Nov 2026)
- The AU25301 unit 1 topics (classification, terminology, components and materials, SI and CI working and comparison, two- and four-stroke SI and CI engines, valve and port timing, fuel-air and actual cycles) all map onto the packet's eight subtopics; no subtopic was added. Two-stroke CI engines (blower and uniflow scavenging) and the SI/CI comparison table were added to the chapters that own them.
- The packet's `where` lists for some courses hold topics of other units: the SRM unit 1 list adds intake and exhaust system components (manifolds, air filter, mufflers, after-treatment), the NITT entry lists advanced combustion (LTC, HCCI, RCCI, GCI), and AU3303 unit 1 lists engine emissions. These belong to the fuel-supply and emissions units and were not taught here.
- Draft errors fixed: Lenoir's engine "lit by a flame" (it used an electric spark), history order (Clerk before Diesel), "fires twice per revolution", CI overlap "often larger", the 1-2-4-3 pairing claim, the Q7 diesel-in-petrol-engine reasoning (722 K is above diesel's self-ignition temperature; the real reason is ignition delay), Diesel-cycle plot below r = ρ, cp/cv label in the fuel-air figure, raw exponents and subscript tags printed as text, and a percentage-points example replaced by traced variable-cv and indicator-diagram examples.
- Packet `out` path is stale (old 03_Books/ path); queue.json holds the right one.

## me-ic-u6 (Claude correction pass, 21 Nov 2026)
- The packet on main adds "Stratified charge and low heat rejection (LHR) engines" as subtopic 8 (from AU25301, whose unit 5 lists stratified charge, LHR, HCCI and RCCI); the draft had no chapter for it, so chapter 6.8 is new and HCCI/RCCI and optical engines moved to 6.9 and 6.10. The draft's review8/review9 files are now review9/review10.
- Of the emissions chapters (6.1–6.5) and alternative fuels (6.6–6.7), AU25301 lists none; they stay for the other syllabi. AU25301's other unit-5 topics (cooling, coolants, crankcase ventilation, lubrication, supercharging) belong to me-ic-u4.
- Draft errors fixed: water-gas shift needs steam, Zeldovich vs extended Zeldovich, NO peak at φ 0.9 = AFR 16.3 (not 15), quench layer 0.1 mm (not 1 mm), spark retard lowers HC, the PM example that treated the filter sample as the engine's exhaust flow, the EGR formula (share of charge 14.7 %, not 17.3 %), the TWC window and its ±0.3 λ trap, g/km called "mass per unit work", the CO limit of 0.06 g/km, the missing BS-IV step, producer gas LHV and composition, DME shown as a liquid, methane-slip trap, the φ–T text and figure that contradicted each other, RCCI called production-ready, Bowditch, Nd:YAG 532 nm and LDA wording, a raw "dry run" object printed inside an example.
- Facts used without a web check (the sandbox could reach no web page): BS-VI car limits taken as the Euro 6 values; MIDC built on the NEDC trace (the drawn trace sums to 11.0 km); RDE with BS-VI stage 2 from April 2023; heavy-engine 0.46 g/kWh NOx and 0.01 g/kWh PM on the transient cycle; methane GWP100 about 28. The MIT OCW link was dropped; the four remaining links are the draft's.
- Packet `out` path is stale (old 03_Books/ path); queue.json holds the right one.

## me-ic-u3 (correction pass, 21 Nov 2026)

- The packet on main adds "Gasoline fuel properties and cycle-to-cycle variations" as subtopic 3 (from AU25301 unit 3, which lists basic fuel properties of gasoline and cycle-to-cycle variations); the draft had no chapter for it, so chapter 3.3 is new and the draft's chapters 3–8 moved to 3.4–3.9 (review files renumbered with them).
- AU25301 splits this unit into SI combustion (its unit 3) and CI combustion (its unit 4); both are covered here. "Influence of engine operating and design parameters on combustion" is covered by the flame-speed factors in 3.2 and the knock factors in 3.5; "fuel-air mixing" and "swirl ratio" in 3.6 and 3.8.
- "Diesel knock and its control" is tagged advanced in the packet, but AU25301 lists "knock in CI engines and methods of controlling diesel knock", so the chapter runs to about 1100 words rather than 650–900. The tag may be worth dropping.
- Draft errors fixed: motoring curve defined with "fuel but no ignition"; flame propagation ending at 42° aTDC while peak pressure was put at 10–15°; ρu of 10–15 kg/m³ "at the spark" (about 6 at the spark, 12–13 mid-burn); a turbulent flame speed table (10–30 m/s) that contradicted S_T ≈ S_L + u′ (now laminar, turbulent burning and flame-travel velocities are separate); φ = 0.85 called rich; knock said to occur only in petrol engines; injection retard said always to shorten the delay; glow plug grouped with intake heating; squish called a rotation; hemispherical chamber said to have the largest surface (it has the lowest S/V, now worked out: 2.06 against 2.33 cm⁻¹); formulas that printed raw <sub> tags.
- Facts used without a web check: BS-VI petrol density 720–775 kg/m³ and 10 ppm sulphur; regular petrol about 91 RON; COV_imep driveability limit about 10 %; IDI fuel economy 10–15 % worse than DI; first-mode knock frequency f ≈ 1.84 c/(πB). The MIT OCW link was dropped; the other links are the draft's.
- Packet `out` path is stale (old 03_Books/ path); queue.json holds the right one.

## me-ic-u2 (Claude correction pass, 21 Nov 2026)
- The packet on main adds "Gasoline direct injection (GDI)" (subtopic 6) and "Electronic ignition and laser ignition" (subtopic 10) from AU25301; both chapters are new, and the draft's chapters 6–9 moved to 2.7–2.9 and 2.11 (reviews moved with them). The draft's GDI section in the EFI chapter now lives in 2.6.
- AU25301 also lists air filters, the throttle and the simple carburettor; they are in 2.1 with a carburettor-sizing example. "Fuel injector" (the nozzle holder) is covered in the nozzle chapter.
- "Ignition timing and spark advance" is tagged advanced (one syllabus); AU25301 does not list it but the chapter was kept and corrected.
- The draft's MIT, NPTEL (university-hosted) and AFDC (off-topic) links were dropped; only SAE remains. The sandbox proxy blocks Wikipedia, so no link could be opened or added.
- The Hiroyasu–Arai penetration correlation and the GDI pressure range (50–200 bar, up to about 350 bar) are from memory of standard sources and could not be re-checked online.
- Packet `out` path is stale (old 03_Books/ path); queue.json holds the right one.

## au-elec-u4 (Claude correction pass, 21 Nov 2026)

- The exam course AU3502 does not teach this unit (its unit 4 is automotive electronics, sensors and actuators, which this subject's sensors-and-actuators unit covers); the packet's `where` lists it for the record only. No subtopics were added; the chapters follow the other syllabi (electronic engine control).
- BS IV and BS VI car limits (Euro 4 and Euro 6 values), the April 2017 and April 2020 dates, the 50 to 10 ppm sulphur step and the April 2023 second BS VI phase are from memory of standard sources and could not be re-checked online.
- The draft's NPTEL and MIT links were dropped; SAE, AFDC and DieselNet remain.
- Packet `out` path is stale (old 03_Books/ path); queue.json holds the right one.
## ec-vlsi-u1 (Claude correction pass, 21 Nov 2026)

- EC3552 unit 1 also lists "MOS logic families (NMOS and CMOS)" and "power consumption", which the universal syllabus places in the CMOS inverters unit (NMOS inverters; static and dynamic power). They are covered here briefly (switches, NMOS logic against CMOS in 1.1; dynamic, short-circuit and static power with the power-delay product in 1.6) and named by topic for the full treatment.
- "Static and dynamic conditions" is read as DC I-V behaviour (1.3) and device capacitances (1.5); SRM's temperature and geometry dependence are in 1.2, 1.4 and 1.7.
- The subject chip says "Usually Sem 4"; EC3552 is a semester 5 course (Regulation 2021). The packet's `usual_sem` may want a look.
- Packet `out` path is stale (old 03_Books/ path); queue.json holds the right one.
- The velocity-saturation chapter uses v = µE/(1 + E/Ec) with Ec = vsat/µ and the exact VDSsat that follows; textbooks differ (some define Ec = 2vsat/µ), and the chapter says so.
- The draft's NPTEL and MIT links were dropped; All About Circuits and three Wikipedia pages remain (opened by the draft run's link check; the sandbox could not reopen them).
## ee-pe-u6 (Claude correction pass, 21 Nov 2026)
- The exam course EE3591 has no applications unit, so no exam subtopic was added; the book follows the packet.
- SRM's unit lists liquid level control, light dimmers and electronic timers; the draft had no liquid level control, now a section of the process control chapter (on-off probes, level transmitter, VFD and pump affinity laws).
- Draft errors fixed: CC-CV charge time double-counted the taper charge (now 4.44 h CC + 1.85 h CV = 6.30 h), skin depths of steel at 50 Hz and 10 kHz (cold 3.2 / 0.23 mm, hot 78 / 5.5 mm), STATCOM current direction, UPFC shunt-converter role, anti-islanding time (about 2 s, not a few cycles), thyristor loss in the heater controller, crane quadrant, CC-CV and backup-time key terms, a bank outline that called the pump power law quadratic.
- Packet `out` path is stale (old 03_Books/ path); queue.json holds the right one.
## au-elec-u5 (Claude correction pass, 21 Nov 2026)
- The exam course AU3502 has no vehicle-motion-control unit (pipeline/EXAM_ND2026.md: u4 and u5 go beyond AU3502), so no exam subtopic was added; the book follows the packet.
- Manipal's `where` entry for this unit (Autotronics, unit 2 "Ignition systems") lists ignition, fuel injection, sensors and CAN topics that belong to au-elec-u2, u3, u4 and u6; only its last items (traction control, cruise control, automatic transmission, ABS) belong here. Its unit mapping looks wrong.
- Draft errors fixed: ACC "average deceleration" 0.42 m/s² that did not settle the gap (now 1.25 m/s² for 4 s), EPS assist of 8 N·m at parking (about a fifth of a real pinion load), ABS "hold" at λ = 0.10 on the band edge, ESP chapter number pointing to the ABS chapter, semi-active damper limit not given in the question, PI quiz answer that could not be computed (b missing).
- Packet `out` path is stale (old 03_Books/ path); queue.json holds the right one.
## me-design-u3 (Claude correction pass, 21 Nov 2026)
- The exam course ME3591 puts shafts, keys and couplings in one unit and connecting rods and crankshafts in its energy-storing and engine-components unit; the packet's new subtopic "Connecting rods and crankshafts" is written as chapter 6 here. Clutches and brakes are not in ME3591 (they belong to the transmission-design course); the chapter is kept for the universal syllabus.
- Draft errors fixed: ASME allowable 0.30S_yt / 0.18S_ut stated as applying "for a shaft with a keyway" (the keyway takes a further 25 % cut); whirl response and mm-trap direction (reviewer flags); clutch heat 11.8 kJ (5.9 kJ with the mean slip speed); outer-edge wear wording; the Rayleigh bank question gave deflections (0.25 mm and 0.10 mm) that no single shaft could have, now computed for a real shaft; hollow-shaft weight outline muddled equal-diameter and equal-torque cases; output and dry-run code boxes on mechanical examples.
- Packet `out` path is stale (old 03_Books/ path); queue.json holds the right one.

## me-design-u5 (Claude correction pass, 21 Nov 2026)
- New ch 5.8 Seals and gaskets from the exam course ME3591 ("Design of Seals and Gaskets"); packet order kept.
- Draft errors fixed: Raimondi and Boyd readings that contradict the L/D = 1 table (ε = 0.62 and (r/c)f = 1.9 at S = 0.031; ε = 0.45 at S = 0.15), a bank chart question with no load or length given, two friction ranges for the same full film, "cylindrical roller takes axial load if flanges are added", the static-load formula given for roller bearings, a projected-area trap that described the wrong view, inconsistent e and Y in the selection example, and old ISO 281 reliability factors.
- Packet: SRM's `where` topics include a lab line ("Experiments: screw jack Modeling Simulation and Analysis ...") that is not syllabus content; NITK's and Manipal's entries list their whole course (unit 1) rather than this unit. The packet `out` path is stale (03_Books/...); queue.json holds the right one.

## au-elec-u3 (Claude correction pass, 21 Nov 2026)
- The exam course AU3502 lists "Automotive Electronics: overview and demands ... Glossary for automotive microelectronics", "Fluid-mechanical actuators" and "Electrical machines ... Duty-type ratings" in this unit; the packet's three new subtopics carry them (new chapters 3.1, 3.10, 3.11). Its "Single-phase alternating-current machines" sits inside 3.11.
- NITT's list keeps LIDAR and the flex-fuel sensor in this unit although they are motion-control and fuel topics; they stay short in 3.8.
- Manipal's `where` entry is its ignition and engine-control unit (most topics belong to au-elec u2 and u4), not a sensors unit.
- The packet `out` path is stale (03_Books/...); queue.json holds the right one.

## me-design-u6 (Claude correction pass, 21 Nov 2026)
- Belts, chains and wire ropes are not in the exam course ME3591 (pipeline/EXAM_ND2026.md), so this book follows the other syllabi; no exam topics were added.
- SRM's `where` topics include lab lines ("Experiments: Mode thermal analysis of Composite material Frequency analysis", "Harmonic Analysis") that are not syllabus content; NITK's entry lists its whole course (unit 1) rather than this unit.
## au-elec-u2 (Claude correction pass, 21 Nov 2026)
- No new subtopics for this unit; the exam course AU3502 lists "Wiper and Washer systems" and "electric horns", now covered in 2.9 (washer system, horn construction and horn relay), and "Special purpose lamps", covered in 2.6.
- The packet tags 2.5 to 2.7 (lighting) "advanced" because only one syllabus lists them, but they are core exam topics of AU3502; the chapters run 1300 to 1450 words rather than the 650 to 900 advanced target.
- Manipal's `where` entry for this unit is its whole ignition and engine-control unit (fuel control, sensors, CAN, ABS), most of which belongs to au-elec u3 to u6; NITT's is its automobile-fundamentals unit (engine block, drivetrain), only partly ignition.
- The packet `out` path is stale (03_Books/...); queue.json holds the right one.

## me-design-u2 (Claude correction pass, 21 Nov 2026)
- No new subtopics for this unit. ME3591 lists "Design for finite and infinite life under variable loading": finite life (Sf from the S–N line), Miner's rule and a Soderberg sizing example are now in 2.3 and 2.4.
- Impact and shock loading (2.5) is tagged "advanced" and appears only in the R2025 course ME25C06, not in ME3591; it stays short.
- Many Indian syllabi and textbooks teach five or six theories of failure including maximum strain energy (Haigh); the packet's universal list did not name it, so it was added to 2.1.
## ec-vlsi-u5 (Claude correction pass, 21 Nov 2026)
- New subtopic 5.2 "Introduction to ASICs: full-custom, standard-cell and gate-array" written (the draft predates it); the draft's chapters moved to 5.3 to 5.8.
- EC3552's unit 5 also lists fault models, ATPG, DFT, scan and boundary scan, which the packet places in ec-vlsi-u6; 5.1 gives them at exam-introduction depth and points to that unit by topic. "Test coding" in the EC3552 list is read as turning patterns into a tester program (STIL); the syllabus does not define it.
- Programmable devices (ROM, PLA, FPGA) sit in EC3552 unit 4 but in this packet's 5.6; 5.6 now covers ROM, PAL and PLA logic implementation for that reason.
- The packet `out` path is stale (03_Books/...); queue.json holds the right one.

## me-design-u1 (Claude correction pass, 21 Nov 2026)
- The DeepSeek run stopped on chapter 2 (selection of materials) and left no book; the whole book was written by hand from the packet, using the draft chapters as material.
- ME3591 unit 1 also lists theories of failure, stress concentration, fluctuating stresses, endurance limit and finite/infinite life; the packet keeps them in "Failure Theories and Fatigue Design", so this book only points there by topic name (bank note says so).
- Crane hook and C-frame (ME3591) are worked in 1.9 Curved beams, with the trapezium and circle formulas for R_n; modes of failure and exposure to standards (IS 1570, IS 919, IS 2062, ISO 3, ISO 286) are in 1.4.
- Packet data: `where` for one university lists the whole course (all units) as unit 1; one university's `course_used` is Electrical Machine Design, and `course_names` mixes in Electrical Machine Design and Robot and Machine Elements Design (other subjects); the packet `out` path is stale (03_Books/...).

## ee-pe-u3 (Claude correction pass, 21 Nov 2026)
- EE3591 lists this material as its unit 1 "Switching Power Supplies", which also names MOSFET dynamic behaviour, driver and snubber circuits, and switching loss calculations with thermal design; the packet keeps those in "Power Semiconductor Devices", so this book points there by topic name and adds a junction-temperature check (3.2) and the switching-loss example (3.7). "Isolated topologies" is covered by flyback, forward and a new push-pull/half-bridge/full-bridge paragraph in 3.6.
- Packet data: one university's `where` lists its whole course (devices to UPS) as unit 1 with the title "Total Number of contact hours"; another's unit title is "Heat Sinks for Power Switching Devices" over a DC-DC topic list; one university's unit 4 mixes inverters and choppers; the packet `out` path is stale (03_Books/...).

## au-elec-u6 (Claude correction pass, 21 Nov 2026)
- AU3502 lists this material as its unit 5 "Vehicle Networking" (network topology, organization, OSI model, control mechanisms, embedded protocols, cross-system functions, requirements and classification of bus systems, coupling of networks, CAN, LIN, FlexRay, MOST); the new chapters 6.2 (topology, OSI, classification) and 6.5 (MOST, gateways) cover them, and 6.1 now covers cross-system functions, bus requirements and the board-level protocols (UART, SPI, I²C).
- Packet data: one university's `where` entry (unit title "Ignition systems") lists its whole course, from ignition and fuel injection through sensors, ABS and climate control, with only "In vehicle networks", "CAN standard" and "diagnostics" belonging to this unit; the packet `out` path is stale (03_Books/...).
- SAE defines bus classes A, B and C only; the book gives C+/D as a textbook extension for buses above 1 Mbit/s.

## ec-vlsi-u6 (Claude correction pass, 21 Nov 2026)
- The packet's nine subtopics already cover CEC362 and the testing half of EC3552 unit 5; no chapter was added. EC3552 topics not named in the packet (wafer-to-chip flow, test and verification issues of SoCs and embedded cores, test coding) are worked into 1 (flow, test versus verification) and 8 (SoC and core issues, test coding). Test benches and the ASIC flow stay in "ASIC Design and Testing".
- "Test coding" is not defined by the syllabus; it is read as turning patterns into a tester program (STIL, IEEE 1450), with don't-care fill and compression (8).
- The draft's March C− had the wrong element order (it missed 24 of 80 simulated cell faults); corrected to ⇕(w0); ⇑(r0,w1); ⇑(r1,w0); ⇓(r0,w1); ⇓(r1,w0); ⇕(r0).
- Packet data: the packet `out` path is stale (03_Books/...); queue.json holds the right one.

## ec-vlsi-u2 (Claude correction pass, 21 Nov 2026)
- No new subtopics for this unit. EC3552's unit 2 is "Combinational Logic Circuits": only "stick diagram" and "Layout diagrams" belong here (7; a NAND stick-to-layout example with a λ width estimate was added); its delay, Elmore, logic-style and power topics are in the packet's unit 3.
- EC3552's unit 5 lists "Introduction to wafer to chip fabrication process flow"; it is now a section of 2.3 (crystal growth to final test, with dies per wafer and good dies).
- One university's `where` list is the whole course placed under unit 1; another lists FinFET technologies here, which the packet keeps in unit 1; one list ends with electron-beam characterisation topics ("Analytical Beams", "Beam Specimen interactions") that are not CMOS fabrication and are not covered.
- The packet `out` path is stale (03_Books/...); queue.json holds the right one.

## au-elec-u1 (Claude correction pass, 21 Nov 2026)
- The packet now has 11 subtopics; the two new ones (power supply, wire sizing and circuit diagrams; electromagnetic compatibility and interference suppression) are chapters 1.2 and 1.3, and the draft's chapters 1.2–1.9 moved to 1.4–1.11.
- The subtopic "High-voltage circuits and power distribution" comes from one university's ignition list, where "High voltage circuit and distribution" means the ignition secondary and the distributor, not EV traction voltage. The chapter now covers ignition HV distribution (distributor, distributorless, coil-on-plug, suppression) alongside low-voltage power distribution; the EV traction part is kept short and marked advanced.
- AU3502's unit 1 also lists battery versions and substitutes, alternator circuitry and versions, regulator versions and starter development and design variations; each is now a section or paragraph in 1.5, 1.6, 1.7, 1.8 and 1.10.
- The packet `out` path is stale (03_Books/...); queue.json holds the right one.

## ec-vlsi-u3 (Claude correction pass, 21 Nov 2026)
- The packet now has 11 subtopics; the two new ones (interconnect parameters and electrical wire models; the Elmore delay model) are chapters 3.5 and 3.6, and the draft's chapters 3.5–3.9 moved to 3.7–3.11.
- EC3552's unit 2 "Combinational Logic Circuits" maps here except "stick diagram" and "Layout diagrams", which the packet keeps with fabrication and layout (unit 2 book). "Examples of combinational logic design" is covered by the compound-gate and multiplexer examples in 3.9 and 3.10; "Elmore's constant" by 3.6.
- EC3552's unit 4 lists "Interconnect Parameters: Capacitance, Resistance, and Inductance" and "Electrical Wire Models"; both are now 3.5. The rest of that unit (arithmetic, programmable devices, memory) belongs to other units.
- The packet's `where` list also carries the CEC362 VLSI testing course units, which do not belong to this unit and are not covered here.
- The packet `out` path is stale (03_Books/...); queue.json holds the right one.

## ee-pe-u4 (Claude correction pass, 21 Nov 2026)
- No new subtopics for this unit. EE3591 lists this material as its unit 2 "Inverters", which opens with "IGBT, static and dynamic behavior"; the packet keeps IGBTs in "Power BJT, MOSFET and IGBT", so this book points there by topic name. "Various harmonic elimination techniques" is an exam topic, though the packet tags "Harmonic elimination techniques" advanced; chapter 6 covers pulse-width, notching (selective elimination), transformer phase-shifting and stepped-wave methods.
- Packet data: one university's `where` entry (unit title "Total Number of contact hours") lists its whole course; another mixes inverters and choppers in one unit; the packet `out` path is stale (03_Books/...).
- Harmonic amplitudes in the SPWM chapter (bipolar m_f and m_f ± 2, unipolar 2m_f ± 1 at m_a = 0.8) and the selective-elimination and cascaded H-bridge switching angles were computed by script (FFT and Newton iteration), not copied from a table.

## ee-pe-u1 (Claude correction pass, 21 Nov 2026)
- No new subtopics for this unit (the packet on main differs from the draft only in other_units). EE3591 lists this material inside its unit 1 "Switching Power Supplies", which also names buck, boost, buck-boost, isolated and resonant converters; the book teaches those under DC-DC converters, not here. MOSFET dynamic behaviour (gate charge, Miller plateau), drivers and snubbers, and switching loss with heat-sink design are covered in the MOSFET, protection and thermal chapters.
- Packet data: another university's unit 1 list ends with DC-DC converter topics that belong with choppers; the textbook entries give no chapter or page numbers to check; the packet `out` path is stale (03_Books/...), queue.json holds the right one.
- Device values (critical fields, t_q ranges, gate limits, R_DS(on)) are typical figures marked "about"; bank questions on datasheet reading use illustrative values stated as such.
## ec-vlsi-u4 (Claude correction pass, 21 Nov 2026)
- The packet now has 10 subtopics; the three new ones (pipelining and sequential circuits; timing issues and clocking strategies; memory architecture and building blocks) are chapters 4.7, 4.8 and 4.10. The draft's memory chapter moved to 4.9, and 4.6 (latches and registers) was rewritten.
- EC3552 spreads this material over its unit 3 "Sequential Logic Circuits and Clocking Strategies" (static and dynamic latches and registers, timing issues, pipelines, clock strategies, memory architecture and building blocks) and unit 4 "Interconnect, Memory Architecture and Arithmetic Circuits" (adders, multipliers, memory cells). The exam topics from both are covered here: C²MOS and TSPC registers, Schmitt trigger, monostable and astable circuits, skew and jitter, self-timed and asynchronous design, and memory core and periphery.
- PLA, PAL and FPGA belong to the programmable-devices unit (u5) and are only named here.
- EC3552's unit 4 also lists interconnect parameters and wire models (covered in the u3 book) and "Logic implementation using programmable devices (ROM, PLA, FPGA)": ROM as logic is in 4.9, PLA and FPGA are in u5.
- Packet data: one `where` entry (ECPC23, unit 3) has an empty unit title; the packet `out` path is stale (03_Books/...); queue.json holds the right one.
- The MIT OCW source was dropped from the sources list (university-hosted).

## me-design-u7 (Claude correction pass, 21 Nov 2026)
- ME3591 (the exam course) has no gears unit, and the packet has no `where` entry for it, so this book follows the universal subtopics only; the bank note does not point to an exam unit.
- The whole book uses one convention (Lewis S_b = σ_b b m Y with Y = 0.484 − 2.87/z, C_v = 3/(3 + v) for spur and 5.6/(5.6 + √v) for helical, Buckingham F_d with C = 11 400 N/mm², wear S_w = b Q d_1 K with K = 0.16(BHN/100)², bevel (1 − b/R) and 0.75/cos γ_1 forms, worm η with α_n); the draft mixed conventions between chapters.
- Packet data: three `where` entries give the whole course (failure theories to gears) as unit 1 with an empty unit title, and one more has an empty title; the packet `out` path is stale (03_Books/...).

## ee-pe-u5 (Claude correction pass, 21 Nov 2026)
- The packet has the same six subtopics as the draft, so no chapter was added.
- Matrix converters are tagged for two courses whose `where` entries do not list them: EE3591 unit 5 ("Ac Phase Controllers") covers only TRIAC triggering, TRIAC phase controllers and SCR controller configurations, and the 21EIC402J entry is its converters unit, which is mostly rectifier topics from the controlled-rectifier unit plus the cycloconverter.
- Packet data: the EEPC19 `where` entry has an empty unit title; the ECE 4464 entry is the whole course listed as unit 1 with the title "Total Number of contact hours"; the packet `out` path is stale (03_Books/...); queue.json holds the right one.
- The two MIT OCW sources were dropped from the further-reading list (university-hosted).
## ee-pe-u2 (Claude correction pass, 21 Nov 2026)
- The packet now has 10 subtopics; the two new ones (voltage doubler and three-phase diode bridge rectifiers; inversion mode and the inverter angle limit) are chapters 2.3 and 2.8. The draft's chapters moved: 2.3 to 2.4, 2.4 to 2.5, 2.5 to 2.6, 2.6 to 2.7, 2.7 to 2.9, 2.8 to 2.10.
- EE3591 puts this material in its unit 4 "Controlled Rectifiers" (1, 2, 3 and 6-pulse converters, displacement factor, ripple and harmonic factor, power factor mitigation, performance parameters, source inductance, inverter angle limit, dual converter). That unit's list also starts with "SCR two transistor analogy based turn-ON, turn ON losses, thermal protection", which are device topics taught in the u1 book, not here. Power factor mitigation is covered with extinction angle, symmetrical angle, PWM and sequence control.
- Another university's list here includes cyclo-converters (AC-AC converters book) and one entry gives the whole course as unit 1 with "Total Number of contact hours" as its title.
- Packet data: the packet `out` path is stale (03_Books/...); queue.json holds the right one.
- The allaboutcircuits link and a duplicate power-factor-correction link were dropped from the sources list.

## me-design-u4 (Claude correction pass, 21 Nov 2026)
- The packet has 10 subtopics; the two new ones (riveted joints for structures and bonded joints; rubber springs) are chapters 4.4 and 4.9. The draft's chapters moved: 4.4 (power screws) to 4.5, 4.5 to 4.6, 4.6 to 4.7, 4.7 to 4.8, 4.8 (flywheels) to 4.10.
- ME3591 spreads this material over two units: threaded fasteners, welded joints, knuckle and cotter joints, riveted joints and bonded joints in one, and springs (helical, concentric, fatigue, leaf, rubber) and flywheels in the next. ME3591 does not list power screws; the chapter is kept for the other syllabi that do.
- ME3591's unit with flywheels also lists connecting rods and crankshafts; they are not in this packet and belong with the shafts book (u3) or a later engine-parts unit.
- The packet appears to be built from a newer regulation of the same course (ME25C06); one `where` entry's course_used names an unrelated course (an electrical machine design subject).
- One convention is used throughout: bolt groups by direct plus moment shear, tilting brackets by W = Pel/Σl² with the principal-stress combination, welds checked on the 0.707h throat with τ = √(σ<sub>b</sub>² + τ₁²), Wahl K on the alternating stress and K<sub>s</sub> on the mean stress (Shigley's K-on-both noted), nipped leaf springs with effective length 2L₁ − l, rimmed flywheels with 0.75σ<sub>t</sub> + 0.25σ<sub>b</sub>.
- Left out as unverifiable: a 94 MPa weld stress figure, a 15 to 18 MPa bearing-pressure table and fixed S<sub>se</sub> fractions of S<sub>ut</sub>. Kept but not checked against a source this session: the P<sub>i</sub> = 2840d preload rule, the 30 to 40 m/s cast-iron rim speed, the rubber G range and k ≈ 1 in E<sub>c</sub> = E(1 + 2kS²).
- MIT OCW, NPTEL and OpenStax links were dropped from the sources (university-hosted or not checked); Wikipedia could not be reached.

## ec-optical-u5 (Claude correction pass, 21 Nov 2026)

- Packet left unchanged (owner's rule for the communication subjects). Chapters 5.4 and 5.5 are tagged advanced but carry a whole exam unit on fiber measurements for one course (attenuation, time- and frequency-domain dispersion, cutoff, NA, diameter, reflectance and ORL, field tests), so they are written at about 1250 and 1450 words rather than the 650 to 900 the tag asks for.
- One course's unit lists "WDM and passive devices" with link design; that belongs with the WDM unit of this subject and is not covered here.
- Conventions used throughout: t<sub>chrom</sub> = |D|Lσ<sub>λ</sub> with the half-power spectral width, t<sub>mod</sub> = 440L<sup>q</sup>/B<sub>0</sub> ns, t<sub>rx</sub> = 350/B<sub>rx</sub> ns, 0.7T<sub>b</sub> (NRZ) and 0.35T<sub>b</sub> (RZ); dispersion limit from the rise-time budget (L ≈ 0.7/(B|D|σ<sub>λ</sub>) as the fiber-only bound).
- Kept but not checked against a source this session: the bend-reference cutoff details (2 m sample, 0.1 dB criterion), cable cutoff ≤ 1260 nm, the 5 % far-field level for NA, connector reflectance "−50 dB or lower" for a good connector.
- NPTEL dropped from the sources (university-hosted); the RP Photonics and FOA links were dropped because the draft's link check only reached a bot page.

## ec-optical-u1 (Claude correction pass, 21 Nov 2026)

- Packet left unchanged (owner's rule for the communication subjects); it has no `where` list for this unit, so every packet subtopic is covered in full and no chapter was added.
- Tags look off for exam use: "Numerical aperture and skew rays" is tagged advanced, but NA, Δ and the acceptance angle are core exam material in every course (only the skew-ray half is niche); "Photonic crystals and photonic band gap" is untagged although it is the most specialised chapter. The chapters follow the tags as given but carry the full NA and skew-ray calculations.
- Conventions used throughout: Δ exact = (n₁² − n₂²)/(2n₁²) with the approximation (n₁ − n₂)/n₁ shown beside it; slab V = (2πd/λ)NA with the full thickness d (cutoffs mπ, single-mode V < π), with a note that half-thickness books use mπ/2; fiber V uses the radius a; mode counts V²/2 (step) and V²/4 (parabolic); skew-ray acceptance n₀ sin θas cos γ = NA; λB = 2n̄a with the thickness-weighted mean index.
- Kept but not checked against a source this session: cabled cutoff ≤ 1260 nm for standard single-mode fiber, MFD about 9 µm at 1310 nm and 10 µm at 1550 nm, typical NA ranges per fiber type, the 220 nm × 500 nm silicon guide. The 98.4 % peak reflectance and the 1407–1726 nm stop band are computed (transfer matrix and the quarter-wave gap formula), not quoted.
- OpenStax dropped from the sources (consistent with the other correction passes); HyperPhysics was never in the rendered list. Question-bank Q11 (modal and material dispersion) belongs to the signal-degradation unit and was replaced by a cross-chapter single-mode design question.

## ec-optical-u2 (Claude correction pass, 21 Nov 2026)

- Packet left unchanged (owner's rule for the communication subjects); it has no `where` list for this unit, so every packet subtopic is covered in full and no chapter was added.
- The srm entry under `where` lists "Microwave Measurements" topics (VSWR, network analyzer), which belong to the microwave subject, not to fiber signal degradation; only its "Attenuation" item matches this unit.
- Conventions used throughout: bit-rate limit B ≤ 1/(2δT) for a full spread and B ≈ 0.2/σ for an RMS width; graded-index delay Ln₁Δ²/(8c) for the near-parabolic profile (with a note that some books give Ln₁Δ²/(2c)); RMS forms Ln₁Δ/(2√3c) and Ln₁Δ²/(20√3c); D > 0 when longer wavelengths arrive later; Rayleigh C = 0.8 dB·km⁻¹·µm⁴.
- Formula constants kept from standard texts but not opened this session: the germania UV-tail formula, the single-mode critical-radius formula (20λ/(n₁ − n₂)^3/2)(2.748 − 0.996λ/λc)^−3, and the empirical SBS/SRS thresholds 4.4 × 10⁻³ d²λ²αν and 5.9 × 10⁻² d²λα. The IR-tail formula 7.81 × 10¹¹ e^(−48.48/λ) was checked against lecture notes. Model curves (material zero 1270 nm, slope 0.0986; D(λ) = (S₀/4)(λ − λ₀⁴/λ³)) are illustrative.
- NPTEL and OpenStax dropped from the sources.
## ec-optical-u3 (Claude correction pass, 21 Nov 2026)

- Packet left unchanged (owner's rule for the communication subjects). Chapters 3.1, 3.3, 3.5 and 3.6 are tagged advanced but carry the queue's calculations (photon energy from bandgap, threshold gain and mode spacing, QW levels and bandgap formulas, radiance-based launching and Fresnel loss), so they run to about 1,050–1,450 words rather than the 650 to 900 the tag asks for.
- Conventions used throughout: Γg<sub>th</sub> = α<sub>i</sub> + (1/2L)ln[1/(R1R2)] with L in cm; Δν = c/(2n<sub>g</sub>L); P = η<sub>s</sub>(I − I<sub>th</sub>), η<sub>s</sub> = η<sub>d</sub>(hν/q); Lambertian launching P = π²r<sub>s</sub>²B<sub>0</sub>NA² (r<sub>s</sub> ≤ a) or π²a²B<sub>0</sub>NA² (r<sub>s</sub> > a); step-index joint losses with uniform launch (lateral (2/π)[arccos x − x√(1 − x²)], x = d/2a; gap [a/(a + s tan θ<sub>c</sub>)]²; tilt 1 − nθ/(πNA)); push-pull Vπ = λd/(2n³r<sub>33</sub>ΓL); LED electrical 3 dB bandwidth 1/(2πτ), optical √3 times larger.
- Kept but not checked against a source this session: Al<sub>x</sub>Ga<sub>1−x</sub>As E<sub>g</sub> = 1.424 + 1.266x + 0.266x² and InGaAsP E<sub>g</sub> = 1.35 − 0.72y + 0.12y² (standard textbook fits), the edge-emitter beam of about 120° × 30°, T<sub>c</sub> of 50–70 K for InGaAsP, LiNbO<sub>3</sub> n = 2.14 and r<sub>33</sub> = 30.8 pm/V, and the 90 ps/(nm·km) dispersion given in one model answer.
- The draft's web sources (RP Photonics, Wikipedia) were kept as they were; none is university-hosted.

## ec-comm-u2 (Claude correction pass, 21 Nov 2026)

- Packet left unchanged (owner's rule for the communication subjects); all eight subtopics covered in packet order. No packet problems found: the eight subtopics are the standard amplitude-modulation unit, and FM, noise and FM stereo correctly sit in the angle-modulation unit.
- Conventions used throughout: s(t) = A<sub>c</sub>[1 + m cos 2πf<sub>m</sub>t] cos 2πf<sub>c</sub>t; DSB-SC s(t) = A<sub>c</sub>m(t) cos 2πf<sub>c</sub>t with A<sub>c</sub> a multiplier gain (so the units close); coherent detector y = (A<sub>c</sub>/2)m(t) cos φ; Hilbert transform delays positive frequencies by 90° (cos → sin), USB = m cos − m̂ sin; image rejection α = √(1 + Q²ρ²), ρ = f<sub>si</sub>/f<sub>s</sub> − f<sub>s</sub>/f<sub>si</sub>; envelope-detector limit RC ≤ √(1 − m²)/(2πf<sub>m</sub>m) and m ≤ R<sub>ac</sub>/R<sub>dc</sub>; FDM B<sub>T</sub> = N·B<sub>ch</sub> + (N − 1)·B<sub>g</sub>, with the slot convention N(B<sub>ch</sub> + B<sub>g</sub>) also shown.
- Kept but not checked against a source this session: PAL-B video 5 MHz with a 0.75 MHz vestige in a 7 MHz channel; the CCITT basic group (carriers 64 to 108 kHz, LSB, 60 to 108 kHz) and supergroup (312 to 552 kHz); typical class C efficiency 70 % to 80 % and linear-stage 40 % to 60 %.
- Web sources kept from the draft (Wikipedia only); "Vestigial sideband" dropped because it redirects to the SSB page, "Envelope detector" added from the draft's checked list. None is university-hosted.
## ec-comm-u4 (Claude correction pass, 21 Nov 2026)

- The packet was not changed (owner's rule for these subjects). Two `where` lists cover more than this unit: one lists narrowband and wideband FM and spectral analysis (angle-modulation topics, the FM unit), and another lists matched-filter reception, error probability, ISI and the eye pattern (the baseband detection unit) and digital modulation (the passband unit). Only those lists' sampling, quantization, PCM, DPCM, ADPCM, DM and ADM topics are covered here.
- Line coding is listed by only two of the syllabi; it is kept as a full chapter because PCM and TDM need it.
- One convention throughout: f<sub>s</sub> ≥ 2f<sub>m</sub> with a guard band; flat-top hold τ sinc(fτ); SQNR = 4.77 + 6.02n − 20 log(V/σ) (6.02n + 1.76 for a full-scale sine); DM bit b[n] = 1 if x[n] ≥ x̃[n − 1]; Manchester 1 = low-to-high (IEEE 802.3); differential Manchester 0 = transition at the start.
- μ-law SQNR against level is from the fine-step formula (a quantizer simulation agrees within about 0.6 dB). Kept but not checked against a source this session: speech neighbour correlation 0.85 to 0.9 at 8 kHz.
- MIT OCW links dropped from the sources (university-hosted); Wikipedia could not be reached from this session, so only the two Wikibooks pages the writer run had opened are listed.
## ec-optical-u6 (Claude correction pass, 21 Nov 2026)

- Packet left unchanged (owner's rule for the communication subjects). Chapters 6.3, 6.4 and 6.8 are tagged advanced but carry the queue's calculations (EDFA gain, power conversion efficiency and OSNR; γ, L<sub>eff</sub>, SPM phase and soliton lengths; AAL5 cell counts), so they run to about 1,340–1,770 words rather than the 650 to 900 the tag asks for.
- The exam-course topic "Optical network transmission modes" has no subtopic of its own; it is covered as circuit against packet switching in 6.5.
- Conventions used throughout: Δλ = λ²Δf/c with c = 3 × 10⁸ m/s; coupler ports 1, 2 input side and 3, 4 output side, directivity 10 log₁₀(P<sub>in</sub>/P₂); PCE = (P<sub>s,out</sub> − P<sub>s,in</sub>)/P<sub>p</sub> ≤ λ<sub>p</sub>/λ<sub>s</sub>; OSNR ≈ 58 + P<sub>in</sub> − NF − 10 log₁₀ N in 0.1 nm; NLS in the β₂/γ form with N² = L<sub>D</sub>/L<sub>NL</sub>; bidirectional lightpaths counted once per pair with one wavelength on both fibers.
- Kept but not checked against a source this session: isolator isolation 30 to 60 dB and insertion loss 0.5 to 1 dB, SOA noise figure 6 to 9 dB, erbium level-2 lifetime about 10 ms, the 58 dB OSNR constant, and the qualitative switch-element table (switching times only; the draft's dB columns were dropped as unverified).
- Dropped the MIT OpenCourseWare link (university-hosted); RP Photonics and ITU-T kept.

## ec-optical-u4 (Claude correction pass, 21 Nov 2026)

- Packet left unchanged (owner's rule for the communication subjects). Chapters 4.1, 4.4 and 4.6 are tagged advanced but carry the queue's calculations, so they run longer than the 650 to 900 words the tag asks for.
- Only one syllabus lists photodetector noise and optical receivers for this unit, and none names BER; the others stop at PIN and APD detectors, and one teaches detectors in its sources unit. The packet keeps noise, receivers and BER here (two as advanced chapters), which fits the subject.
- Conventions used throughout: q = 1.602 × 10⁻¹⁹ C, h = 6.626 × 10⁻³⁴ J·s, c = 3 × 10⁸ m/s, k<sub>B</sub> = 1.38 × 10⁻²³ J/K (k is kept for the ionisation ratio); R = ηλ/1.24; surface reflectivity r, extinction ratio r<sub>ex</sub>; f<sub>tr</sub> ≈ 0.44/t<sub>tr</sub> (some textbooks use v<sub>sat</sub>/2w); F = kM + (1 − k)(2 − 1/M); APD sensitivity (Q/R)(qFBQ + σ<sub>T</sub>/M); BER = ½erfc(Q/√2), Q = 7.03 for 10⁻¹².
- Kept but not checked against a source this session: v<sub>sat</sub> of 6.5 × 10⁴ m/s for InGaAs holes, typical k values (Si 0.02–0.05, InP about 0.5, Ge near 1), F ≈ M<sup>x</sup> with x = 0.3 (Si) and 0.7 (InGaAs), and "APD receivers 5 to 10 dB better than PIN".

## ec-comm-u3 (Claude correction pass, 21 Nov 2026)

- Packet left unchanged (owner's rule for the communication subjects); no errors found in its subtopics or exam weights. All eight subtopics already had chapters, so none were added; each chapter now carries two worked examples carried to the answer.
- Conventions used throughout: β = Δf/f<sub>m</sub>; Carson B<sub>T</sub> = 2(Δf + f<sub>m</sub>); figure of merit = (S/N)<sub>o</sub> over the channel SNR with total received power in N<sub>0</sub>W (AM m²/(2 + m²), DSB-SC and SSB 1, FM 3β²/2 with tone modulation); FM threshold taken at a carrier-to-noise ratio of 10 dB in B<sub>T</sub>, with 13 dB mentioned as the other common figure; stereo separation from pilot phase error φ as 20 log₁₀[(1 + cos φ)/(1 − cos φ)] (the draft's 20 log cot φ was wrong).
- Kept but not checked against a source this session: the edition of Taub and Schilling (listed without one), and the click-noise expression for the FM threshold curve (not used; the threshold figure marks the fall below threshold as not to scale). The 50 µs de-emphasis is described as the value used outside the Americas, without naming countries.
- Dropped the MIT OpenCourseWare link (university-hosted); kept two Wikipedia pages, two All About Circuits pages and dspguide.com.
## ec-comm-u1 (Claude correction pass, 21 Nov 2026)

- The packet was not changed (owner's rule for these subjects). Several `where` lists for this unit belong mostly to other units: two of them list AM, FM and PCM topics (the modulation and digitisation units). Only their block-diagram, Fourier, random-process and noise topics are covered here.
- One convention throughout: R<sub>X</sub>(τ) = E[X(t + τ)X(t)]; two-sided PSD N₀/2; T₀ = 290 K; noise factor F linear and NF in dB; Friis in F and in T<sub>e</sub>, with T<sub>e</sub> referred to the stage input; complex envelope x̃ = x<sub>I</sub> + jx<sub>Q</sub> with x(t) = Re[x̃ e<sup>j2πf<sub>c</sub>t</sup>] and ỹ = ½ x̃ ∗ h̃.
- Bandwidth of a T-second pulse given in all three forms: null-to-null 2/T band-pass (1/T one-sided baseband) and full 3-dB width 0.886/T (0.443/T one-sided).
- MIT OCW links dropped from the sources (university-hosted). The web could not be reached from this session, so only pages the pipeline had already opened are listed (dspguide.com, the Communication Systems Wikibook and PySDR).
## ec-antenna-u4 (Claude correction pass, 21 Nov 2026)

- The packet was not changed. Its nine subtopics match the draft's nine chapters, and each is covered in full (there is no `where` list for this unit).
- Rat-race numbering used throughout: arcs 1–2 = λg/4, 2–3 = 3λg/4, 3–4 = λg/4, 4–1 = λg/4; port 1 is the sum port, port 3 the difference port, outputs 2 and 4. The draft's numbering made port 1 a difference port, and the reviewer's suggested numbering was also inconsistent with the stated arcs.
- Conventions: Sᵢⱼ = bᵢ/aⱼ with the other ports matched; coupler ports 1 input, 2 through, 3 coupled, 4 isolated, I = C + D; reflex modes N = n + ¾ (n = 0, 1, 2 …); Gunn transit-time mode n₀L > 10¹² cm⁻², LSA 2 × 10⁴ < n₀/f < 2 × 10⁵ s/cm³.
- Not checked against a source this session: the GaAs velocity–field curve in the Gunn figure is an empirical fit (threshold 3.2 kV/cm, peak near 2 × 10⁷ cm/s); typical ranges (magnetron 40 % to 70 %, IMPATT up to about 15 %, spiral-inductor Q about 10 to 20) are textbook-typical figures quoted without a citation. The draft's "±20 % bandwidth" for the Wilkinson was removed as unverified.
- Sources: three textbooks (Pozar 4th, Collin 2nd, Liao 3rd), Microwaves101 and five Wikipedia pages; no university-hosted pages.

## ec-antenna-u6 (Radar Systems) correction pass, 21 Nov 2026

- Packet left unchanged (owner's rule for the communication subjects); no `where` list, so every packet subtopic is covered in full; no chapter added.
- Conventions: R<sub>max</sub> uses S<sub>min</sub> = kT<sub>0</sub>BF·(S/N)<sub>min</sub> with a system loss L; Doppler positive for a closing target; FMCW f<sub>b</sub> = 2RΔf/(cT<sub>m</sub>) per sweep, with the triangular textbook form 4RΔf·f<sub>m</sub>/c shown beside it; matched-filter peak S/N 2E/N<sub>0</sub> (E/N<sub>0</sub> on the average-power basis); CA-CFAR formula stated for a square-law detector; monopulse horns A top-left, B bottom-left, C top-right, D bottom-right.
- Kept but not checked against a source this session: typical cross sections (insect 10⁻⁵ to ship 10⁴ m²), the IEEE band edges, the ~1.4/τ filter within 1 dB of matched, ~13 dB plain-chirp sidelobes, 60–70 dB TR-tube isolation. The sphere curve, CFAR multipliers and Albersheim estimate are computed, not quoted.
- Only one online source is left (radartutorial.eu); MIT OCW, NPTEL (university-hosted) and the Internet Archive home page were dropped, and the container could not open new pages to add others.

## ec-antenna-u3 (Antenna Arrays, Types and Propagation) correction pass, 21 Nov 2026

- Packet left unchanged (owner's rule for the communication subjects); no `where` list, so every packet subtopic is covered in full; no chapter added.
- Conventions: θ measured from the array axis throughout, ψ = βd cosθ + α with α the lead of the next element; scan angles from broadside are converted (θₛ = 90° − θ₀); Dolph-Chebyshev sidelobe level written as a positive dB number in R = 10^(SLL/20); dish HPBW ≈ 70λ/D (58λ/D stated for uniform illumination); radio horizon 4.12√h km (4/3 earth).
- Kept but not checked against a source this session: the optimum-horn beamwidth constants 56λ/B and 67λ/A (Kraus), typical Yagi/LPDA gains and dimension ranges, patch bandwidth ranges, and the 0.85 × MUF optimum working frequency rule. Every worked number (array patterns, Chebyshev currents, beamwidths and directivities, LPDA, horn, dish, patch, measurement and ionosphere values) was computed in Python.
- Sources: four textbooks (Balanis 4th, Kraus and Marhefka 3rd, Pozar 4th, Saunders and Aragón-Zavala 2nd), antenna-theory.com and five Wikipedia pages; no university-hosted pages.

## ec-comm-u5 (Claude correction pass, 21 Nov 2026)

- Packet left unchanged (owner's rule for the communication subjects); it has no `where` list for this unit, so every packet subtopic is covered in full and no chapter was added.
- "Correlative coding and M-ary PAM" carries the M-PAM symbol error derivation; "Optimum detection and probability of error" keeps binary, the union bound and decision regions and points to it, so the two chapters do not repeat each other.
- Draft error beyond the reviewer notes: it said the nearest-point rule is ML only for equal energies. Minimum distance is ML in AWGN for any energies; it is the bare largest-correlation rule that needs equal energies. Fixed in the text, a trap and a worked example (r = (1.4, 0.3) against points of energies 1, 2, 2).
- Conventions used throughout: overall pulse p(t), channel samples h<sub>m</sub>, equalizer taps c<sub>k</sub>, combined response v<sub>m</sub>; polar duobinary with levels −2, 0, +2 and the |c<sub>k</sub>| < 1 → 1 rule (unipolar mod-2 form mentioned once); M-PAM levels ±d … ±(M − 1)d, P<sub>e</sub> = 2(1 − 1/M)Q(√(6E<sub>s</sub>/((M² − 1)N₀))); duobinary P<sub>e</sub> = 1.5 Q((π/4)√(2E<sub>b</sub>/N₀)) derived for an equal transmit/receive split of the 1 + D response with symbol-by-symbol detection (2.1 dB).
- Kept but not checked against a source this session: "about 2 dB" soft-decision gain (Beyond the syllabus only), DVB-S2 roll-off menu, PAM4 in 400G Ethernet.
- MIT OpenCourseWare dropped from the sources (university-hosted).

## ec-comm-u6 (Claude correction pass, 21 Nov 2026)

- Packet left unchanged (owner's rule for the communication subjects); every packet subtopic is covered in full and no chapter was added. Spectral density comparison, m-sequences, FH processing gain, coherence bandwidth and time, Rayleigh fading and diversity were added inside the existing chapters.
- Packet note: one of the unit's `where` entries lists the topics of a whole first communication-systems course (unit 1 of that course) rather than passband modulation topics, so it gives no useful coverage signal for this unit.
- Conventions: P<sub>b</sub> against E<sub>b</sub>/N<sub>0</sub> throughout, with E<sub>s</sub> = E<sub>b</sub>log<sub>2</sub>M for M-ary schemes; Gray coding with P<sub>b</sub> ≈ P<sub>s</sub>/log<sub>2</sub>M; DPSK P<sub>b</sub> = ½e<sup>−E<sub>b</sub>/N<sub>0</sub></sup>, non-coherent BFSK ½e<sup>−E<sub>b</sub>/2N<sub>0</sub></sup>; MSK tone spacing 1/(2T<sub>b</sub>); DSSS processing gain T<sub>b</sub>/T<sub>c</sub> and jamming margin G<sub>p</sub> − (E<sub>b</sub>/N<sub>0</sub>)<sub>req</sub> − L; OFDM Δf = 1/T<sub>u</sub> with the guard interval added to the symbol time.
- Kept but not checked against a source this session: the rules of thumb B<sub>c</sub> ≈ 1/(5σ<sub>τ</sub>) and T<sub>c</sub> ≈ 0.423/f<sub>d</sub>; the 99 % bandwidths (about 20.6R<sub>b</sub>, 10.3R<sub>b</sub>, 1.18R<sub>b</sub>) were found by numerical integration, not quoted. The web links were kept from the draft's checked list because the container could not open pages.
- MIT OpenCourseWare dropped from the sources (university-hosted); pysdr.org and gnuradio.org kept.
## ec-antenna-u2 (Antenna Fundamentals and Radiation) correction pass, 21 Nov 2026

- Packet unchanged. Its eight subtopics fit the unit; "Receiving antenna, reciprocity and effective area" and "Radiation resistance, efficiency, effective aperture and polarization" share effective aperture, so 2.3 defines A<sub>e</sub> and 2.7 derives Dλ²/4π on the Hertzian dipole and adds effective length, without repeating each other.
- Conventions used throughout: η = 120π Ω for the medium and η<sub>rad</sub> for radiation efficiency (the draft's unit sections used e<sub>cd</sub>); R<sub>r</sub> = 80π²(l/λ)² only for uniform current, 20π²(l/λ)² for a centre-fed short dipole with triangular current, both referred to the feed; l<sub>eff</sub> = l, l/2 and λ/π for those two and the half-wave dipole; D in 2D²/λ is the largest physical dimension.
- Far-field rule for small antennas taken as max(2D²/λ, 1.6λ), justified in the text by βr = 10 (induction term a tenth of the radiation term); the book says it is a working rule, since texts differ.
- Kept but not checked against a source this session: 0.47λ to 0.48λ resonant dipole length, μ<sub>eff</sub> "tens to a few hundred" for rods, 0.5 to 0.7 dish aperture efficiency, the Wheeler cap method in one model answer.
- NPTEL dropped from the sources (institute-hosted); the other three web sources are the draft's checked links (no web access this session, so no new links were added).
## ec-antenna-u5 (RF Circuits and Transceivers) correction pass, 21 Nov 2026

- Packet left unchanged (owner's rule for the communication subjects); no `where` list, so every packet subtopic is covered in full; no chapter added.
- Conventions: spiral Q as ωL/R<sub>s</sub> with the self-resonance correction Q<sub>eff</sub> = Q(1 − f²/f<sub>SR</sub>²); Friis written in linear factors with sensitivity −174 + NF + 10 log B + SNR<sub>min</sub>; cascaded IIP3 summed in milliwatts with each stage referred to the input; SFDR = (2/3)(IIP3 − noise floor); EIRP = P<sub>PA</sub> − L<sub>feed</sub> + G<sub>ant</sub> (no loss term from the antenna port); ACLR as wanted over adjacent power, larger is better; Leeson stated with the 2FkT/P<sub>s</sub> prefactor, the FkT/(2P<sub>s</sub>) form of some books noted beside it.
- Draft error beyond the reviewer notes: a bank answer said a filter after the LNA costs only 0.05 dB; with the stated chain the noise figure rises from 2.46 to 2.75 dB (+0.29 dB).
- Kept but not checked against a source this session: typical ranges (on-chip spiral Q 5 to 20, handset duplexer loss 1 to 3 dB, uncalibrated image rejection 30 to 40 dB). Every worked number (Q and self-resonance, varactor tuning, Friis and sensitivity, two-tone IIP3, cascaded IIP3 and SFDR, image rejection, EIRP and duplexer desensitisation, LNA matching, Gilbert-cell gain, spurs, PA efficiency and load-line match, Leeson and PLL divider) was computed in Python.
- Sources kept as in the draft: Razavi, Pozar and Lee textbooks, microwaves101, rfwireless-world, allaboutcircuits and mtt.org; no university-hosted pages.
## ae-avionics-u3 (Aircraft Electrical Systems and Instruments) correction pass, 21 Nov 2026

- Packet unchanged; all 13 subtopics (8 universal plus the 5 added for AE25301) were already in the draft, so no chapter was added. AE25301 topics folded in: lithium-ion batteries and the 2013 B787 battery events (3.3), the APU as the third source (3.4), over- and under-voltage protection with the MIL-STD-704 normal bands (3.1), limiting resistors (3.10), single- and twin-engine bus systems (3.11), engine starting and primary/secondary indicators (3.13).
- Packet data to note: chapters 3.2 to 3.4 and 3.6 are tagged advanced (one syllabus), but batteries, inverters and the APU are in the AE25301 exam course, so they were written at full depth; the "advanced" tag on 3.3 and 3.2 now undersells them. Air data (3.7) and avionics packaging/EMI (3.6) are not in AE25301 unit 1.
- Convention: aircraft AC voltages are line-to-neutral (115 V, 235 V), so three-phase power is 3 × V<sub>ph</sub> × I, or √3 × 200 V × I; the draft's B787 example had used 115 V as a line voltage.
- Kept but not checked against a source this session (no web lookups): MIL-STD-704 bands 22 to 29 V and 108 to 118 V, A320 TR 200 A and emergency generator about 5 kVA, B787 APU starter-generators 225 kVA, AWG 6 and 4 resistances (1.30 and 0.815 mΩ/m), ARINC 404 ATR and ARINC 600 MCU sizes.
- Sources: MIT, NPTEL and OpenStax links dropped; Moir and Seabridge, and Wyatt and Tooley, added to the textbooks.

## ce-rcc-u1 (Design Philosophies and Material Behaviour) correction pass, 21 Nov 2026

- Packet unchanged; the 7 subtopics were all in the draft, so no chapter was added. CE3501 unit topics folded in: design of a singly reinforced beam by the working stress method (worked example and a 15-mark model answer), IS 456 Annex B permissible stresses, the advantages of the limit state method over the other two (comparison table and a WSM-against-LSM worked example). LSM analysis and design of singly reinforced beams is covered through the stress block chapter and two bank answers; doubly reinforced beams are left to limit state design of beams.
- Packet data to note: the stress block parameters chapter is tagged advanced (one syllabus), but CE3501 uses it for every LSM beam, so it is written at full depth (about 1700 words, with the 0.36/0.42 derivation).
- Facts corrected from the draft: IS 456 creep coefficients are 2.2, 1.6 and 1.1 for loading at 7 days, 28 days and one year (draft: 2.2 at 28 days, 1.6 at one year); HYSD steel reaches 0.87fy only at 0.87fy/Es + 0.002 (SP 16 Table A), not on a yield plateau; the stress block is not a uniform 0.36fck (it is the parabola-rectangle with peak 0.446fck; 0.36 and 0.42 are its area and centroid).
- Kept from memory of the code, not looked up this session: IS 456 Tables 21/22 permissible stresses, Table 8 assumed standard deviations, Table 18 load factors, Tables 5/16 minimum grade and nominal cover, 23.2 deflection limits, 35.3.2 crack widths, IS 1786 elongations 14.5 % and 12 %, and the 1978 revision as the edition that adopted the limit state method.
- Sources: MIT OpenCourseWare and NPTEL links dropped; IS 456:2000 and SP 16 added to the textbooks.

## ae-avionics-u1 (Flight Control Systems) correction pass, 21 Nov 2026

- Packet unchanged; the 8 subtopics were all in the draft, so no chapter was added. The exam course AE25301 lists none of this unit's topics (it was built from AS3302 Flight Systems); the AS3302 and other syllabus topics are covered: components of the conventional system, flexible push-pull cables, power-actuated systems (EHA), DFBW operation and advantages, auto-throttle operation and advantages (list added).
- Packet data to note (first unit of the subject): AS3302 lists "Communication and Navigation systems" and "Instrument landing systems" under flight controls; here they belong to radio navigation and landing aids. One syllabus lists FMS, LRU and IMA under flight controls; they sit in guidance (FMS) and avionics architecture (IMA, LRU). The auto-made unit map labels chapter 1.1 "Need for control systems;" with the semicolon (render.py cuts on ":" only).
- Facts corrected from the draft: servo tab is driven by the pilot while the surface floats (draft: linked to fixed structure, which is a geared tab); the anti-servo stabilator example is the Piper PA-28, not the Cessna 172 (conventional elevator); a gas-turbine FCU uses an acceleration schedule that caps fuel against surge (draft: "acceleration enrichment", a piston-engine term); C* is rate-like at low speed and g-like at high speed (draft: "limits load factor"); triplex voting is lost at about 3p² = 3 × 10⁻⁸, not only all-fail p³; RSS on fighters is used for agility; autoland is used for Category II/III approaches (draft: autoland "classified" by category).
- Examples rebuilt: 1.1 gearing, hinge moment and rod force now consistent (MA 3.44, not an unrelated 4); 1.2 rod checked for Euler buckling with guide spacing; 1.3 boost ratio uses linkage gearing and sizes the actuator; 1.5 majority-loss probabilities; 1.6 heading-select outer loop added; 1.7 root bending added; 1.8 fuel-cost example replaced by FADEC corrected fan speed against inlet temperature.
- Kept but not checked against a source this session: A320 mechanical backup to rudder and pitch trim, Kawasaki P-1 fly-by-light, KAP-type single-axis autopilot on many C172R using the turn coordinator.
- Sources: SKYbrary autopilot and FADEC links dropped (address not confirmed); SKYbrary flight controls and autothrottle/autothrust added; Pallett and Coyle, Automatic Flight Control, added to the textbooks.

## ae-avionics-u2 (Hydraulic, Pneumatic and Environmental Systems) correction pass, 21 Nov 2026

- Packet unchanged; all 11 subtopics (including the two added for AE25301) were in the draft, so no chapter was added. AE25301 unit topics folded in: electric starting circuit and exciter energy, landing gear control units and proximity sensors, trailing-edge flap drive with asymmetry and wing-tip brakes, light-aircraft and transport stall warning with the 5 kt / 5 % margin, baggage (cargo class C and E) fire protection, windscreen heat control and rain removal. AS3302 topics added: high-pressure pneumatic power system and emergency bottles, shock absorber classes, retraction mechanism, brake system, rocket separation mechanisms (short note with landing gear).
- Packet data to note: engine fuel/lubricating and starting/ignition are tagged advanced (one syllabus), but AE25301 examines starting and ignition, so that chapter is written at full depth (about 1600 words).
- Facts corrected from the draft: 8000 ft is 75.3 kPa (draft 75.6, so Δp 51.5 kPa and 61.8 kN); Fenwal is the single-wire resistance loop and the gas-pressure loop is the Lindberg/Systron-Donner type (draft had Fenwal as pneumatic); stall speed rises as √W (draft example and quiz used 1/√m); starter cut-out on one common narrow-body is about 50 % N2 (draft 25–40 %); passenger masks are continuous flow, airliners mostly use chemical generators; boots are now cycled from the first sign of ice (draft and reviewer used the old 6–13 mm rule); simple-cycle ACM has a fan, not "no compressor and nothing else"; outflow-valve-jammed quiz rewritten (jammed closed raises Δp to the safety valve).
- Kept but not checked against a source this session: A320 auto-start values (16 % ignition, 22 % fuel, 50 % cut-out), exciter spark energies up to about 20 J, chemical generator duration 12–22 min, hydraulic accumulator precharge 1000 psi.
- Sources: MIT OpenCourseWare link dropped; Collinson replaced by Tooley and Wyatt, Aircraft Electrical and Electronic Systems.

## ce-rcc-u3 (Shear, Torsion and Bond) correction pass, 21 Nov 2026

- Packet unchanged; all 7 subtopics were in the draft, so no chapter was added. CE3501 unit topics covered: bond and anchorage behaviour, code design requirements (detailing chapter), shear and torsion behaviour, and a full design for combined bending, shear and torsion (M_e1, M_e2 and the IS 456 torsion stirrup formula, which the draft lacked; it designed torsion stirrups for V_e with the plain shear formula).
- Packet data to note: "Combined bending, shear and torsion" and "Lap splices and curtailment" are tagged advanced (one syllabus each), but CE3501 examines combined design as a long question, so both chapters run to about 1650–1700 words (above the pipeline's soft 1000-word target for advanced chapters, within the checker's 1900).
- Facts corrected from the draft: deformed-bar bond stress (draft used the plain-bar 1.4 N/mm² for M25 in the laps chapter, giving L_d = 1030 mm for a 16 mm bar instead of 645 mm); lap of bars of two diameters is based on the smaller bar (IS 456 26.2.5.1; the draft's reviewer had reversed it); curtailed bars extend by the greater of d and 12φ, not L_d; minimum clear spacing is the greater of φ and aggregate + 5 mm (no 25 mm floor in IS 456), vertical gap between layers is the greatest of 15 mm, 2/3 aggregate and bar size; compatibility torsion is neglected only if torsional stiffness is neglected in analysis (no ACI-style threshold); L_0 is measured from the support centre and 1.3 M_1/V applies with a confining reaction; τ_c at p_t = 0.89 % for M25 is 0.61 N/mm² (draft 0.62, with no p_t given).
- Kept but not checked against a source this session: τ_c and τ_c,max table values, τ_bd values and Table 16 covers are from IS 456:2000 as remembered (cross-checked against each other); a/d failure ranges are textbook values; the Wikipedia links in "Further reading online" could not be opened from this container (blocked) and were added by title.
- Sources: NPTEL, MIT OpenCourseWare and ScienceDirect dropped; IS 456, SP 16 and SP 34 added as references.

## ae-avionics-u4 (correction pass, 21 Nov 2026)

- Packet unchanged; all 11 subtopics (including the two added for AE25301, transducers and avionics electronics) were in the draft, so no chapter was added. queue.json still says 9 subtopics for this unit; the packet has 11.
- AE25301 unit topics covered: evolution of civil and military aircraft electronics (4.1), diodes and transistors, op-amps and signal conditioning, ADC and DAC, microprocessors and microcontrollers (4.11), transducers for solenoids, pressure, temperature, strain, rotary position and acceleration (4.10). Other syllabi's items covered too: organisation framework and payload types (4.1), EADI, EHSI, EICAS and electronic systems monitor displays (4.4); ADS-B is left to the navigation unit.
- Facts corrected from the draft: a 1553B receive message has one status word, as a transmit message does (the draft and its reviewer both gave it an extra one); ARINC 429 needs one pair per transmitter, not per parameter; EICAS advisories are amber (indented), not cyan; HUD collimation removes refocusing between symbols and scene, not between panel and HUD; HUD angle relabelled; ADC formulas had lost their exponents (Q = Vref ÷ 2N); scan worst-case wait is scan time minus one dwell (2.0 s, not 2.4 s).
- Kept but not looked up this session (well known, from memory): DO-178B objective counts 66/65/57/28, AFDX end-system jitter 500 µs, 1553B response time 4 to 12 µs, 10 s speed trend, ARINC 429 BNR SSM codes. Type K sensitivity 41 µV/°C is stated as a classroom approximation.
- Sources: MIT OpenCourseWare link dropped (university-hosted); FAA, RTCA, NASA NTRS and EASA kept; Eismin's Aircraft Electricity and Electronics added for the electronics chapters.

## ce-rcc-u6 (correction pass, 21 Nov 2026)

- Packet unchanged; all 9 subtopics were in the draft, so no chapter was added. The unit is outside the CE3501 exam, so no exam topics were added. The packet's `where` list holds only one prestressed course; the advanced chapter (stressing systems in detail) is marked as taught in only a few syllabi.
- Facts corrected from the draft: a straight cable over two spans is not concordant (secondary reaction 3Pe/L, pressure line e/2 above the middle support); linear transformation keeps the pressure line, not the reactions; anchorage slip with friction uses the setting length l<sub>s</sub> = √(E<sub>s</sub>A<sub>p</sub>δ/p), loss 2pl_s at the anchor; spalling comes from the restrained face behind the plate, not from the spreading of the force; flanged ultimate sections treated as in RC T-beams; "effective prestress at ultimate" in partial prestressing replaced by strain compatibility; kN/N slips in the loss formulas fixed.
- Kept but not looked up this session (given as question data or left out): IS 1343:1980 relaxation table, friction coefficients μ and k, Table 11 rows, transmission lengths. M30 as the post-tensioned minimum is from the 1980 edition; M40 pre-tensioned is current.
- Sources: NPTEL and Britannica entries dropped; Krishna Raju, Lin & Burns, Dayaratnam and Rajagopalan kept as textbooks.

## ce-rcc-u4 (Design of Slabs and Staircases) correction pass, 21 Nov 2026

- Packet unchanged; all 6 subtopics were in the draft, so no chapter was added. CE3501 unit topics covered: cantilever, one-way, two-way and continuous slabs (Table 26 and 27 panels, Table 12 and 13 coefficients), types of staircases, design of a dog-legged staircase, and an introduction to flat slabs (direct design method and punching shear).
- Packet data to note: "Staircases" is tagged advanced, but CE3501 examines a full dog-legged design as a long question, so that chapter runs to about 1380 words (above the 650–900 target for advanced chapters, within the checker's 1900). "Yield line theory" is not in CE3501; it is kept short and says only a few universities teach it.
- Facts corrected from the draft: two-way M_y was computed with l_y² (IS 456 Annex D uses α_y w l_x² both ways), which overstated the long-span moments by about 56 %; the one-way example took the clear span as the effective span (cl. 22.2 gives the smaller of clear span + d and centre to centre); the 150 mm cantilever that the draft passed fails the span/d check (basic 7 × Fig. 4 factor); the stair flight span was assumed (3.3 m) instead of going + half landing or 1 m at each end (cl. 33.1), and the 150 mm waist it used fails deflection on the correct span; the flat slab example had no punching check (the draft's 180 mm plate fails it) and now has drops with two punching perimeters; the yield-line chapter now treats the method as an upper bound with a pattern search on a rectangle (minimum at b = 2.38 m against the closed form).
- Kept but not checked against a source this session: Fig. 4 modification factors come from the standard fitted equation (marked "about" in the text); Table 19, Table 26 and Table 27 values and the 2R + T comfort range of 550–700 mm are from IS 456 and textbooks as remembered and cross-checked against each other.
- Sources: IS 456:2000, SP 16:1980 and Park and Gamble's Reinforced Concrete Slabs added; the four Wikipedia links kept.

## ae-avionics-u6 (Claude writer, 21 Nov 2026)
- Unit rewritten as "Guidance, Flight Management and Spacecraft Systems": missile guidance laws (PN, pursuit/LOS/CLOS), missile airframe, fin servos and bank-to-turn left out on purpose; GNC taught at overview level with civil examples; approach and landing guidance added. 5 chapters, 9,702 words, 6 figures.
- Writer could not fully verify: CAT IIIA RVR (book says 175 m to 200 m by authority), autoland LAND-mode arm height (given as a range), Li-ion LEO depth of discharge 20-30 % and path efficiencies 0.6 / 0.8 (textbook values).
- Syllabus data: unit 6 mixes three courses (a Flight Systems course, an EE Control and Guidance course, a Flight Control Systems unit); that last list's FBW/FBL, LRU and IMA belong to units 1 and 4; "Gyroscope and its types" belongs with unit 5; one course_names entry "Underwater Navigation Systems" looks unrelated to this subject; the spacecraft subtopic's "attitude stabilisation" match is listed for one university only.

## ae-avionics-u5 (Radio, Inertial and Satellite Navigation) correction pass, 21 Nov 2026

- Packet unchanged; all 10 subtopics were in the draft, so no chapter was added. AE25301 examines only terrain awareness and ground proximity warning from this unit (TAWS chapter: modes, FLTA, premature descent alert, Class A/B); the rest of the unit goes beyond AE25301.
- Packet data to note: the `where` list for this unit includes AS3302 flight-control topics that belong with the flight-control unit, and the SRM instrument topics overlap the gyro instruments taught in units 3 and 4.
- Facts corrected from the draft: ILS glide path sense was reversed (90 Hz predominates above, 150 Hz below) and its full scale given as ±0.35° (it is about ±0.7°, DDM 0.175); CAT IIIA/IIIB minima; Galileo and BeiDou called regional; true anomaly said to be broadcast (it is the mean anomaly); the INS one-hour gyro-bias example used the open-loop t³ formula (3.70 km) where the Schuler loop gives 1.35 km; the radar example used 1030 MHz, the SSR interrogation frequency; GPWS Mode 2/3/4 descriptions and two quiz answers; an unrealistic gyro rotor inertia.
- Kept but not checked against a source this session: the GPS error budget in one model answer is illustrative (stated as such); the nutation example assumes a transverse inertia of half the spin inertia; ICAO category minima, marker distances and TAWS class contents as remembered.
- Sources: Kayton and Fried, Groves and Skolnik added as textbooks; web links unchanged.

## ce-rcc-u2 (Limit State Design of Beams) correction pass, 21 Nov 2026

- Packet unchanged; all 7 subtopics were in the draft, so no chapter was added. CE3501 unit topics covered here: analysis and design of flanged beams (flange in the slab and in the web, with y_f), design aids for flexure (SP 16 Tables 1–4 and Table F), serviceability (L/d with k_t, k_c, k_f, Annex F crack width). The same CE3501 unit also lists bond and anchorage, shear and torsion; those are in the shear, torsion and bond book (ce-rcc-u3). The prestressed concrete course listed under this unit's "where" (WSM, end blocks, losses) belongs with the prestressed unit (ce-rcc-u6), not here. WSM analysis asked by one course is in ce-rcc-u1; the cracked-section stresses in the transformed-sections chapter use the same m.
- Examples changed from the draft: singly reinforced design gave 3 bars of 22 mm (1140 mm²) for 1022 mm² required, which puts x_u = 198.9 mm above x_u,max = 192 mm, so the "designed" beam was over-reinforced (now 112.5 kN·m from loads, 3 of 20 mm, checked); doubly reinforced design called A_st2 (211.9 mm²) the compression steel A_sc (true 217.3 mm², f_sc = 352.1 from the design curve) and over-provided 4 of 25 mm; the design-aid example used 5 bars of 16 mm in a 250 mm web (clear gap 23.5 mm, below aggregate + 5 mm); the deflection example only compared two given deflections with span/250 and span/350, now a full L/d check with k_t and k_c and an Annex F crack width. Added worked analyses: strain-compatibility over-reinforced section, doubly reinforced analysis by trials, T-beam with the neutral axis in the web and y_f, cracked transformed section with I_eff.
- Kept but not checked against a source this session: k_t and k_c come from the standard fitted equations to IS 456 Figs 4 and 5 (marked as curve fits in the text); SP 16 table numbers used in the book (Tables 1–4 singly reinforced by concrete grade, Tables 45–56 doubly reinforced, Table F for f_sc) and the Table F values (Fe415 355/353/342/329, Fe500 424/412/395/370 N/mm² at d′/d 0.05–0.20) are as remembered and agree with the Fig. 23A curve, but the printed SP 16 was not re-opened this session.
- Sources: IS 456:2000 and SP 16 added; Pillai and Menon, Varghese, Subramanian, Wight and MacGregor as textbooks; web links reduced to the BIS and ACI sites.

## ce-rcc-u5 (Design of Columns and Footings) correction pass, 21 Nov 2026

- Packet unchanged; all 8 subtopics were in the draft, so no chapter was added. CE3501 topics covered here: types of columns, axially loaded rectangular, square and circular (helical) columns, uniaxial and biaxial bending with SP 16 and the load-contour check, slender columns with the additional moment, wall footing, axially and eccentrically loaded isolated pads, sloped footing and the two-column rectangular combined footing. Retaining walls and water tanks are in the packet but not in CE3501.
- Packet data to note: the `where` list carries two exam-course units whose footing topics overlap, so footings appear twice; the retaining wall and water tank subtopics have no CE3501 counterpart.
- Examples changed from the draft: slenderness example called a ratio of exactly 12 short (IS 456 needs both ratios below 12), now slender about y with e_min 22.2/20 mm and a second example on M_a with k = 0.31; axial column 300 × 400 broke e_min ≤ 0.05D, replaced by a 400 × 400 design (6 of 25 mm, 2075 kN) and a helical column (8 mm helix at 50 mm); biaxial check used assumed SP 16 capacities, replaced by strain-compatibility uniaxial (174 kN·m at 1200 kN) and biaxial (8 of 20 mm fails at 1.31, 8 of 25 mm passes at 0.87) designs; wall footing used stirrups in a footing (below minimum) and the face moment for a masonry wall, now B 1.2 m, D 250 mm, moment at the masonry section; square pad stopped at bending depth, now a full rectangular pad with one-way, punching, central band and an eccentric pad (400.3 kN·m at the face); combined footing completed with SFD/BMD, shear with the top steel counted in the hogging zone, punching and transverse strips; retaining wall example had no geometry, now a full stability check (sliding fails, shear key) and stem design; water tank used 150 N/mm² for hoop tension, now 130 N/mm² (IS 3370-2:2009) with a thickness and concrete-tension check.
- Kept but not checked against a source this session: IS 456 and IS 3370-2 values as remembered (clause numbers given in the text); SP 16 chart readings replaced by computed p/f_ck values; the transverse-strip width for combined footings (column width + 2d) is a common choice, not a code rule.
- Sources: IS 456, SP 16 and IS 3370-2 added; Pillai and Menon, Varghese, Krishna Raju as textbooks; NPTEL and MIT links dropped.

## ce-survey-u1 (Foundations: Surveying Principles and Distances) correction pass, 21 Nov 2026

- Packet unchanged; all 6 subtopics were in the draft, so no chapter was added. CE25C03's matching unit is "Levelling" (chain surveying, datum, benchmarks, levelling methods, booking and reduction, contouring): chain surveying and datum/benchmarks are covered here; levelling, booking and contouring belong to the universal levelling unit (ce-survey-u3).
- Packet data to note (first unit of the subject): the CE25C03 unit mapped to this book is mostly levelling, which the universal syllabus puts in u3; four `where` entries (iitd, iitb, nitk, nitc) list the whole course's topics under "unit 1", so they are not a per-unit list; the SRM entry is its modern-equipment unit (EDM, total station, GPS), which overlaps u5 more than this unit.
- Examples changed from the draft: the tape that reads 100.05 m on 100.00 m was called a tape that "under-measures" (it is short and over-reads); the datum example gave a 134 m orthometric height at Chennai's coordinates, now a survey pillar plus a separate UTM zone and central meridian calculation; code-style "dry run / output" blocks removed from the scale and tape examples; new second EDM example (coarse/fine phase, prism constant, vertical angle: 423.070 → 422.460 m); quiz answers fixed for the catchment map scale (1:50,000, not 1:250,000) and the check-line verdict.
- Facts fixed: reciprocal ranging does not "prolong" a line; the 1.5 cm offset rule replaced by the limiting length of offset; scale classes (1:25,000 and 1:50,000 are medium, topographic); sag formula is per span (times n spans); "Not for exam" beyond line.
- Kept but not checked against a source this session: the 250 km² plane-survey guide (textbook value); typical chain, rod and arrow dimensions; carrier-wave grouping of EDMs; the older Indian datum on the Everest ellipsoid with origin at Kalianpur, and the open series maps on WGS84.
- Sources: S. K. Duggal added; DGCA and ISRO links dropped (not about this unit).

## ce-survey-u6 (Remote Sensing and Image Interpretation) correction pass, 21 Nov 2026

- Not in the exam course CE25C03 (remote sensing is outside it); no exam topics added. Packet data looks right: the seven subtopics match the remote-sensing units of the syllabi; the only `where` entry is a remote-sensing unit of an engineering surveying course.
- Examples changed from the draft: the hazy-day reflectance example halved the radiance and so contradicted the chapter's own path-radiance paragraph (now T = 0.9, L<sub>p</sub> = 4.0: sensor 22.0, uncorrected 0.173, corrected 0.157); NDVI example now reads vegetation, soil and water from the figure (0.818, 0.100, −0.333) and shows the shaded crop unchanged; new second examples: Wien peaks (0.50, 9.66, 3.62 µm), orbital period at 705 km (98.9 min, 14.56 orbits, 2752 km spacing) and 35 786 km (86 164 s), 8-bit vs 12-bit quantisation (DN 128/128 vs 2049/2056), photo scale 1:20 000 with tower height 25.2 m from shadow, error matrix (OA 0.830, κ = 0.725).
- Facts fixed: band table (NIR 0.7–1.3, SWIR 1.3–3, mid IR 3–8, TIR 8–14 µm; no "3–15 µm window"), mid-IR window 3–5 µm, the 1.37 µm cirrus band, reflectance changes with the surface (season), irradiance with area, tilted-photo scale, small-angle GSD, 2ⁿ − 1 steps; unit numbers in prerequisites named by topic.
- Kept but not checked against a source this session: Landsat 8 at 705 km with a 185 km swath and 16-day repeat; the 6S/MODTRAN and Indian mission descriptions are qualitative.
## ei-sensor-u1 (Foundations: Sensor Characteristics and Errors) correction pass, 21 Nov 2026

- Taught as the Biomedical course Sensors and Measurements (BM25C05) unit 1. Packet data to note (first unit of the subject): the subject name in the packet is "Sensors and Transducers" (built from EI25C02), so the book's header says that, not the exam course name; the SRM entry is a Fraden-style "sensors, signals and systems" unit that also lists strain gauge, load cell and thermocouple characteristics (unit 2 material); the NITC entry is a MEMS course whose unit 1 belongs with the micro sensors unit.
- Examples changed: the loading example said 24.99 mV with a 0.01 mV loss (the loss is 0.0125 mV, 0.05 %), now with a second 10 kΩ case (23.81 mV, 4.76 %); the calibration example now has down-scale readings and hysteresis (0.04 V = 1.0 %FS) and uses the 3.98 V output span as the %FS denominator, the same convention as the static-characteristics chapter; a second dynamic example added (catheter-transducer, f<sub>n</sub> 25 Hz: ratio 2.08 at 20 Hz with ζ 0.2, 0.975 with ζ 0.6); bank Q10 recomputed (s = 11.55 mV, 95 % ±8.3 mV with t = 2.262); bank Q7 given real data; bank Q11 changed from a payment-counter scale to a neonatal scale.
- Exam topics added: measurement system configuration with a blood-pressure channel; primary and secondary transducers; primary, secondary and working standards with examples, and the 2019 SI definitions; limiting errors; test-input response table (step, ramp, impulse, sine); biomedical sensor table by physical principle.
- Facts fixed: unit cross-references by number replaced with topic names; Hall coefficient symbol and underscore maths; IRCTC dropped; OpenStax link dropped.
- Not verified this session: the 5 µV/V/mmHg disposable blood-pressure transducer rating (standard value, from memory of the AAMI figure); quartz d = 2.3 pC/N.

## ch-mass-u3 (Gas Absorption) correction pass, 21 Nov 2026

- Taught as Mass Transfer II (CH3551) unit 1, Absorption. Packet data: unit 2 of the universal syllabus already has "Stage-wise and differential contactors" and "Mass transfer with chemical reaction", which CH3551 lists under absorption; the book covers the absorption side (contactor types table in chapter 3.4, reaction regimes in 3.9) and points to the unit 2 topics by name.
- Examples changed: the running Y* = 2X example was labelled SO₂ in water, which contradicts chapter 3.1 (SO₂, H = 40 atm, m = 40); it is now acetone vapour in water, which fits m ≈ 2 and the 30 000 kJ/kmol heat effect. HETP formula fixed to H_OG ln λ/(λ − 1) (0.348 m, 4.08 stages; the draft had λ ln λ/(λ − 1), 0.256 m, 5.5 stages) and its quiz (0.324 m, not 0.487). Minimum-L/G rounding made consistent (1.809, 2.713, 257.7 kmol/h). Gas-halved quiz now recomputes N_OG (3.07) instead of assuming it constant.
- Added for CH3551: contactor types (stagewise and differential), stage-by-stage stepping table and figure for the plate absorber, multicomponent Kremser example (lean oil, four solutes), adiabatic N_OG by Simpson's rule (4.75 → 6.06), stripping minimum gas and stripping factor, 1/K_Ya = 1/k_Ya + m/k_Xa.
- Not verified this session: the 15–50 mm water per metre design pressure drop and the 50–70 % of flooding rule are standard textbook guides quoted from memory; acetone's m ≈ 2 near room temperature is an estimate from its activity coefficient and vapour pressure, so the book calls the line "the plant's equilibrium data".
## ch-mass-u1 (Mass Transfer Operations, unit 1: molecular diffusion; correction pass 21 Nov 2026)

- Mass Transfer I (CH25C05) unit 1, not part of the CH3551 exam course. Packet data to note (first unit of the subject): the IIT Bombay (CL 319) and NITK (CH251N) `where` entries hold the whole course's topic list as "unit 1" (absorption, distillation, extraction, drying), so they do not describe this unit; the same lumped lists reappear in u2 and u7. In u2 the Manipal entry is a Mass Transfer II unit (distillation, extraction, leaching), and in u7 the NITC unit 3 entry is mostly extraction (u5 material) with drying at the end.
- Examples changed: the mothball (naphthalene) example used a surface mole fraction of 0.0100, about 90 times the real vapour pressure at room temperature; now 11 Pa (y = 1.09×10⁻⁴), so the radius halves in 143 days, not 38 h. Python code dropped from the classification example. Quiz answers fixed: N_A = J_A error direction (D too large by 1/(1 − y_A)), D_AB = D_BA for any binary (not only ideal), pseudo-steady failure conditions, first-term slab series error (1.12 at Fo = 0.05), Wilke friction argument.
- Facts fixed: the two-bulb cell was called Winkelmann's method (Winkelmann's is the Stefan tube); Wilke's equation stated for a stagnant mixture, not "a dilute species"; liquid-versus-gas flux comparison (about ten times smaller, not "still significant"); unit cross-references by number replaced with topic names; underscore subscripts set as real subscripts.
- Added: liquid stagnant-film example (acetic acid through water, 1.02×10⁻³ mol/m²·s), Stefan tube and Winkelmann formulas, Chapman–Enskog and Wilke–Chang formulas with an ethanol–water example (1.47 vs 1.24×10⁻⁹ m²/s), structure-sensitive and insensitive solid diffusion, Knudsen and effective diffusivity with a pellet example, slab average-concentration series with an example (27.2 h vs 52.6 h for the centre); 12 full model answers with numbers.
- Not verified this session: naphthalene vapour pressure 11 Pa at 298 K and D = 6.1×10⁻⁶ m²/s (standard handbook values, from memory); the measured ethanol–water D of 1.24×10⁻⁹ m²/s.
## ch-mass-u5 (Liquid Extraction and Leaching) correction pass, 21 Nov 2026

- Exam course CH3551 Mass Transfer II (its extraction and leaching unit). Topics now covered: solvent characteristics, stagewise calculations for batch and continuous extractors, spray, packed and mechanically agitated contactors with design (settler area, HTU–NTU height, flooding diameter), packed bed extraction with reflux, pulsed and centrifugal extractors, supercritical extraction, solid–liquid equilibria (N–y diagram), batch and continuous leaching equipment, percolation, moving bed and the Shanks system, multistage cross-current and counter-current leaching with stage efficiency.
- Examples changed: the counter-current leaching example used one wash ratio E = V/L = 0.889 for the whole battery; with a dry feed stage 1 has a 400 kg/h overflow and stages 2–3 have 600 kg/h, so the answer is 53.7 kg/h lost and 78.5 % recovered (not 73.9 kg/h and 70.4 %), with 8 ideal stages for 95 %. The cross-current comparison in the counter-current chapter claimed 77.5 % in five cross-current stages with 500 kg/h (impossible: the limit is 65.7 %); now 60.0 % in three stages, 903 kg/h needed to match. Stage efficiency rewritten (0.7 does not make 3 real stages 2.1 ideal; 5 real stages match 3 ideal). Tie lines on a right-angled diagram said to be horizontal; driving-force claim for counter-current reversed; settler sized on the dispersed-phase flow (now continuous-phase flow over Stokes velocity); pulse velocity explanation; "caffeine is non-polar" corrected; Shanks system described with moving solids (the solids stay; the liquor inlet and outlet are switched).
- New examples: lever-rule stage on the triangle (E 147.3 kg, K 1.54, β 29.4), real-stage count at η = 0.7, Δ point at (−1.87, 0.252) and S<sub>min</sub> 362 kg/h, HTU–NTU column 3.74 m × 1.46 m, two-stage cross-current leaching (74.6 %), centrifugal settling at 2012 g.
- Packet note: the right-angled triangle method subtopic is tagged advanced (one university), but it is the standard Hunter–Nash construction most textbooks teach; the chapter is longer than the advanced target because it carries the stage construction the other chapters rely on.
- Not verified this session (no web access): CO<sub>2</sub> density about 0.84 g/cm³ at 40 °C and 200 bar (standard tabulated value).

## ei-sensor-u4 (Piezoelectric, Hall Effect and Optical Sensors) correction pass, 21 Nov 2026

- Packet unchanged; all 11 subtopics (including the two BM25C05 additions, phototube/PMT/scintillation counter and photodiodes/cells/spectrophotometry) were in the draft, so no chapter was added. BM25C05 unit 3 topics covered: phototube, scintillation counter, PMT, photovoltaic and photoconductive cells, photodiodes, phototransistors, a comparison table of all six photoelectric devices, spectrophotometric and clinical uses (haemoglobin at 540 nm, pulse oximetry), piezoelectric transducer as pressure (pulse, heart sounds) and ultrasound transducer (imaging probe, Doppler blood flow).
- Facts corrected from the draft: stroboscope quiz (a single still mark at 1200 and 2400 flashes/min cannot mean 1200 or 600 rpm; rewritten with two marks at 4800/min giving 2400 rpm); force-balance answer said the 0.16 A coil current is sent as the output (now scaled to 16.8 mA on 4-20 mA); Hall drift remedies (ratiometric and chopper do not cancel R_H drift); permeability change under torque (rises on the tension diagonal, falls on the compression one); photoelectric threshold for semiconductors is the band gap, not the work function; critical angle measured from the normal; OTDR is not phase-sensitive (only phi-OTDR is); photodiode table rows (LDR needs a supply; light meters run photodiodes at zero bias); "absorbance adds" sentence; broken anchor to a photoelectric chapter id that does not exist; ASCII 2^N and theta_res; all unit-number cross-references replaced by topic names.
- Examples added: charge amplifier vs voltage amplifier through 100 pF cable (-0.23 V vs 0.213 V), Doppler blood flow 0.40 m/s, accelerometer design (fn 3183 Hz, H 0.9971 at 1 kHz), Hall clamp-on current sensor (31.4 mT, 11.9 mV/A), magnetostrictive position sensor (0.70 m, 28 um per count), fibre NA and critical angle, PMT photon-to-anode-current (84.5 uA), photodiode TIA readout of the spectrophotometer (T 0.50, A 0.301).
- Kept but not checked against a source this session: NaI(Tl) light yield of about 38 photons per keV, FBG sensitivities 1.2 pm/ue and about 10 pm/degC at 1550 nm, magnetostrictive waveguide speed of about 2800 m/s (stated as calibrated per sensor).
- Sources: Khandpur's Handbook of Biomedical Instrumentation and Webster's Medical Instrumentation added; the six Wikipedia links kept.

## ae-struct-u4 (Bending of Thin-Walled Beams) correction pass, 21 Nov 2026

- Packet unchanged (no subtopic added for this unit). AE3501 unit 1 topics covered in 4.2 and 4.3: the k method, the neutral axis method and the principal axis method are each taught and worked on one Z-section (171.4 MPa at the web corner by all three), and deflections under unsymmetrical bending by the curvature equations and by principal axes. SRM's "beam deflection shape using MATLAB" is a short Python program with its output (Python, not MATLAB, so it runs here); "bending moment distribution for wings and fuselages" is covered as the lift and drag moments at a station in 4.5.
- Facts corrected from the draft: restrained anticlastic stress is +νσ, not −νσ; the neutral axis "perpendicular to the moment vector" wording; the I_u/I_v labels swapped between chapters 2 and 3 (now I_u = ∫v² dA about u throughout); I_xy symmetry rule (one axis of symmetry is enough); thermal held-straight stress is not self-equilibrating (it carries a moment); lost superscripts in the thermal chapter; one sign convention (y up, M_x positive when positive y is in tension) used in every chapter.
- Packet note: the IIT Bombay `where` entry for every ae-struct unit is the whole-course description, not a unit topic list; harmless but uninformative.

## ce-survey-u3 (Levelling and Contouring) correction pass, 21 Nov 2026

- Packet unchanged. The draft run stopped on an error: chapter 2 ("Levels and their temporary and permanent adjustments") was empty and there was no unit.json or web.json, so chapter 2 and all unit sections were written new.
- CE25C03 unit topics covered: datum, benchmarks, levelling methods including fly and check levelling, booking and reduction (with inverted staff and missing entries), contouring. "Chain surveying" in the same CE25C03 unit belongs to the foundations unit (chain and tape surveying), so it is not taught here.
- Packet data to note: "Curvature and refraction; reciprocal levelling" is tagged advanced, but it is in every standard textbook and a regular exam problem; the chapter says only that few syllabi list it by name. "Areas, volumes and reservoir capacity" is tagged advanced and kept short.
- Facts corrected from the draft: capacity now includes the volume below the lowest contour; HE doubling statement tied to the gradient, not the angle; valley floor (not sides) rises upstream; HI booking check extended to the intermediate sights; the arithmetic checks no longer claimed to catch misread readings; prismoidal rule given in its standard contour form (odd number of contours).
- Kept but not checked against a source this session: the 1/7 refraction factor and 6370 km radius (standard textbook values); the permissible-error constant is given only as C√K with the value set by the specification.
- Sources: four Wikipedia pages and the Survey of India note on the vertical datum, all opened this session; Punmia, Duggal, Basak, Subramanian and Ghilani and Wolf as textbooks.
