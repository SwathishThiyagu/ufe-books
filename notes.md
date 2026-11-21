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

## ec-vlsi-u4 (Claude correction pass, 21 Nov 2026)
- The packet now has 10 subtopics; the three new ones (pipelining and sequential circuits; timing issues and clocking strategies; memory architecture and building blocks) are chapters 4.7, 4.8 and 4.10. The draft's memory chapter moved to 4.9, and 4.6 (latches and registers) was rewritten.
- EC3552 spreads this material over its unit 3 "Sequential Logic Circuits and Clocking Strategies" (static and dynamic latches and registers, timing issues, pipelines, clock strategies, memory architecture and building blocks) and unit 4 "Interconnect, Memory Architecture and Arithmetic Circuits" (adders, multipliers, memory cells). The exam topics from both are covered here: C²MOS and TSPC registers, Schmitt trigger, monostable and astable circuits, skew and jitter, self-timed and asynchronous design, and memory core and periphery.
- PLA, PAL and FPGA belong to the programmable-devices unit (u5) and are only named here.
- EC3552's unit 4 also lists interconnect parameters and wire models (covered in the u3 book) and "Logic implementation using programmable devices (ROM, PLA, FPGA)": ROM as logic is in 4.9, PLA and FPGA are in u5.
- Packet data: one `where` entry (ECPC23, unit 3) has an empty unit title; the packet `out` path is stale (03_Books/...); queue.json holds the right one.
- The MIT OCW source was dropped from the sources list (university-hosted).
