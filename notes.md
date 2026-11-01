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

