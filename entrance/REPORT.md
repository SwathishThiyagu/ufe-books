# Entrance Exam Free N Easy — research baseline / 13 November 2026

## Deliverable status

This is a **breadth-first discovery baseline**, not the requested fully verified encyclopaedia. The dataset currently contains **197 entries** (including paper variants, school-entry tests, admission-only routes, optional recruitment and abroad), and **221 provisional topic nodes**. It does **not** yet individually verify the 2025/2026 pattern, languages, seats, syllabus tree or official PYQ status for each entry.

Files:
- `exams.json` — exam registry and null-safe fields, 2027 schedules, some sourced candidate counts, assumptions-based priority.
- `universal_topics.json` — normalized subject > unit > topic taxonomy, candidate exam mappings and provisional NCERT/B.Tech overlaps.
- `index.html` — filter/search explorer (runs when hosted beside the JSON files).

**Do not publish unsourced schedule guesses as facts.** Some future months are placeholders with explicit unconfirmed status. Do not add together paper-registration counts (a candidate may appear for multiple GATE papers). Admission-only routes are not stand-alone exams. School admission tests for VI/IX are not post-10th examinations.

## Initial verified candidate reach and schedule anchors

| Exam | Recorded registered candidates | Year | Evidence / note |
|---|---:|---:|---|
| NEET UG | 2,279,743 | 2026 | [NTA result press release](https://neet.nta.nic.in/) — verify exact 2026 bulletin/press release if link fails |
| JEE Main Paper 1 (unique across sessions) | 1,604,854 | 2026 | [NTA](https://jeemain.nta.nic.in/) |
| CUET UG | 1,568,866 | 2026 | [NTA](https://cuet.nta.nic.in/) |
| GATE CS paper | 259,922 | 2026 | [GATE 2026 statistics](https://gate2026.iitg.ac.in/cut-off.html); paper registrations, not unique GATE applicants |
| GATE DA paper | 91,764 | 2026 | [GATE 2026 statistics](https://gate2026.iitg.ac.in/cut-off.html); paper registrations |
| JEE Advanced | 187,389 | 2026 | [Official press release](https://jeeadv.ac.in/documents/Result2026PressRelease.pdf) |
| CLAT UG | 75,009 | 2026 | [Consortium press release](https://consortiumofnlus.ac.in/clat-2026/notifications/Press-Release_07.12.2025.pdf) |

2027 schedules to expose prominently: [JEE Main bulletin](https://jeemain.nta.nic.in/); [GATE 2027 schedule](https://gate2027.iitm.ac.in/important_dates); [JAM 2027](https://jam.iitkgp.ac.in/); [CLAT 2027](https://consortiumofnlus.ac.in/clat-2027/index.html), scheduled **6 December 2026**; [UCEED 2027](https://www.uceed.iitb.ac.in/2027/). Note: **2027 admission cycle != 2027 calendar year**.

## Recommended top-ten **production sequence** (strategy-adjusted)

Dataset's numerical heuristic prioritizes high candidate reach, underserved-audience hypothesis, commonality and nearer exams. Production order also considers creating reusable packages and avoiding double-production for sibling papers:

| Order | Production cluster | Why | Scope of unique books | Lesson planning allowance |
|---|---|---|---:|---:|
| 1 | JEE Main PCM | largest demonstrated overlap with existing CBSE 11–12 | 8–12 unit packs | 45–75 |
| 2 | CUET UG — General Test + English | broad reach; supplements NCERT subject videos | 7–10 | 35–55 |
| 3 | GATE CS | existing repo CSE books/packets; can reuse assets | 5–8 targeted review packs | 30–50 |
| 4 | GATE DA | extends existing CSE, statistics, AI resources | 4–6 | 25–40 |
| 5 | NEET UG PCB | strongest recorded reach; NCERT core readily reusable | 9–12 reinforcement packs | 55–80 |
| 6 | UCEED + NID BDes | visual aptitude has a distinct animated advantage | 7–10 | 35–55 |
| 7 | VITEEE + BITSAT + state PCM CETs | repurpose JEE chapters; add exam-format drills | 4–7 | 20–35 |
| 8 | IIT JAM Mathematics / Physics | graduate-level bridge; shared fundamentals | 6–8 | 35–50 |
| 9 | JEE Advanced | JEE Main content plus deeper multi-step problems | 5–8 | 30–45 |
| 10 | Nursing UG + NEET allied | NEET PCB reuse; add nursing-specific orientation | 3–5 | 15–30 |

**Production estimate**: approximately **58–86 distinct incremental unit books** and **325–515 HTML lessons** across this sequence, not 10 independently duplicated courses. Count is **editorial estimate, not data-proven** and includes exam-style practice where existing NCERT/B.Tech books cover the explanatory core. At stated 400–500 lessons/week theoretical writing capacity this is ~0.7–1.3 nominal lesson-writing weeks, **excluding** verification, editing, narrations, image generation, accessibility, QA, GitHub/Cloudflare deployment and retakes. Do not interpret capacity as an achievable publish date.

## Overlap and gaps

**NCERT channel overlap**: physics, chemistry, mathematics, biology from classes XI/XII are conceptually high overlap for NEET, JEE Main, state engineering and medical CETs, CUET domain subjects, IISER IAT and some nursing/agriculture tests. **Not proven** that current animated CBSE series covers every listed chapter; match each video identifier and edition before claiming ready-to-publish.

**B.Tech overlap**: GitHub repo inspection shows unit packets and HTML books for CSE areas including data structures, algorithms, operating systems, DBMS, networking, COA, AI, machine learning, etc. This is particularly reusable for **GATE CS** and partially **GATE DA**. Repository at snapshot: [ufe-books](https://github.com/SwathishThiyagu/ufe-books); standalone Claude artifact [B.Tech syllabus pack](https://claude.ai/artifact/9j8tUxjFNfcEit4ZGerNpN) could not be programmatically inspected. Therefore the universal map has **likely/partial/unverified**, not validated lesson coverage.

**New content / undersupply hypotheses**: standalone school-entry mathematics and mental-ability; legal reasoning and reading-speed skills; design visualization/sketching; nursing anatomy basics; agriculture specificity; linguistic/regional-language adaptations; current-affairs freshness; application/scholarship portals; fine-grained practice pattern differentiation.

## Priority score — read carefully

Per-exam `priority.score` is a decision-support heuristic. The “underserved free animated content” multiplier is **not a measured survey**; candidate-reach value defaults to a **neutral proxy if unknown**. Shared-topic counts are approximations from broad subject-family assignments and may overstate the tested syllabus. Time-to-exam prioritization is relative to 2026-11-13. Rank and production sequence are therefore recommendations, not verified market-share metrics.

## Verification queue / blocked PDFs

1. Attach official 2025 and 2026 bulletins, date notices and results for each major exam where public PDF reading is blocked; do not work around access restrictions. Start with JEE Main 2027, NEET UG, CUET UG, GATE, CLAT, UCEED, BITSAT, states.
2. Confirm each candidate statistic with direct official notice, **year, scope, denominator** (registered / appeared / qualified; unique / per-paper); drop anything that cannot be substantiated.
3. Validate 2027 notice status as of 13 November 2026; derive **expected** dates from two prior official years only when both sources exist. Otherwise keep unknown.
4. Replace per-exam coarse topic unions with official syllabus section → unit → topic annotations and source document URLs.
5. Confirm examination active/discontinued/merit-route status; e.g., school VI/IX belongs separate from post-10th, and CUET/ICAR routes are not separate entrance tests.
6. Map actual `ufe-books/packets` IDs and CBSE channel existing lesson IDs into exact topic nodes with depth and year/version.
7. Audit all official old question paper portals and copyright permission separately; link, do not re-host or reproduce materials without license clarity.
8. Complete missing language, marking, number of questions, paper duration, seats, institutions, and subject eligibility from official notices.
9. Have a native/regional language reviewer check state portals and conduct a state-by-state missing-exam audit.

**Publication gate**: a card can go live as “verified” only when exam status, official home, eligibility, dates, syllabus and pattern have individually checked authoritative source records; “unknown” is safer than an invented precise figure.