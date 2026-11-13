# Entrance exam free n easy: research report

Built 13 November 2026. Research and data only; no books or lessons were written.

Map: https://claude.ai/artifact/EUhgTxc1mr77vqc37uvFtN (private until you share it).

## What is in the pack

| File | Contents |
|---|---|
| `exams.json` | 125 entries: 104 admission entrance exams (20 after class 10, 54 after class 12, 30 after a degree) and two optional groups kept apart (13 government job exams, 8 study-abroad tests). Each has body, level, stream, eligibility, 2027 month and dates, mode, languages, pattern, candidates, seats, official link, syllabus tree, whether past papers are official, and the priority score. |
| `universal_topics.json` | 1,445 topics. School and aptitude subjects are subject > unit > topic (Physics 122, Chemistry 121, Maths 68, Biology 43, class 9-10 foundation 41, aptitude 82, others 51). Degree subjects reuse the 148 B.Tech subjects the exams need, with their 900 units, straight from `pack/universal.json`. Every topic lists the exams that use it, its NCERT 11-12 status and its B.Tech pack status. |
| `map/index.html` | The published map: level, then stream, with candidates, month, shared-topic count and score; filters for level and stream. |
| `build/` | The two source files and the script that regenerates everything. Edit a number in `exams_src.py`, run `python3 build.py`, and the JSON, scores and map data update together. |

How to trust a number: `verified: true` means I read it on the linked page today. `verified: false` means it is from the last bulletin as I remember it, or an estimate, and the link is the official site where it must be checked. 19 candidate counts are in the first class, and 18 exams have a 2027 date published by the conducting body. Nothing unverified is presented as verified.

## Top 10 to start with

Score = candidates (lakh) × underserved × shared × time factor. The formula and every input are in `exams.json`.

| # | Exam | Candidates (year) | 2027 sitting | Underserved | Shared | Score |
|---|---|---|---|---|---|---|
| 1 | NEET UG | 22.80 lakh (2026) | Expected 2 May 2027, not announced | 0.30 | 0.97 | 6.63 |
| 2 | CUET UG | 15.69 lakh (2026) | Expected May to June 2027 | 0.50 | 0.80 | 6.27 |
| 3 | MHT CET (PCM + PCB) | 7.63 lakh (2026, first attempt) | Expected April 2027 | 0.70 | 0.93 | 4.97 |
| 4 | JEE Main | 16.05 lakh (2026) | 20-28 January 2027 announced; April session | 0.30 | 0.98 | 4.71 |
| 5 | AP EAPCET | 3.56 lakh (2026) | Expected mid May 2027 | 0.70 | 0.93 | 2.32 |
| 6 | KCET | 3.30 lakh (2026) | Expected late April 2027 | 0.70 | 0.93 | 2.15 |
| 7 | TG EAPCET | 3.02 lakh (2026) | Expected early May 2027 | 0.70 | 0.93 | 1.96 |
| 8 | NDA and NA | about 5 lakh (estimate) | 11 April 2027 announced | 0.50 | 0.76 | 1.89 |
| 9 | JEECUP (UP Polytechnic) | about 4.2 lakh (estimate) | Expected June 2027 | 0.90 | 0.50 | 1.89 |
| 10 | GATE | 10.12 lakh (2026) | 6-21 February 2027 announced | 0.50 | 0.58 | 1.75 |

Three things to know before reading the order as final:

- **Ranks 8 and 9 rest on estimated candidate counts.** If NDA is nearer 3 lakh, CUET PG (1.15) and VITEEE (1.12) are the next in line.
- **The underserved column is my judgement, not a measurement.** I did not count YouTube supply. It is the input most worth replacing with real numbers.
- **GATE is held back by time, not size.** The 2027 paper is 85 days away, which costs it 40% of its score. For GATE 2028 it would rank fifth.

Seven of the ten (NEET, CUET UG, MHT CET, JEE Main, AP EAPCET, KCET, TG EAPCET) draw on the same class 11-12 Physics, Chemistry, Maths and Biology. That one stack is the plan.

Suggested production order inside the top 10:

1. Class 11-12 Physics and Chemistry, exam layer (all seven exams).
2. Class 11-12 Maths (JEE Main, the engineering halves of the state CETs, NDA Paper 1).
3. Class 11-12 Biology (NEET, the pharmacy and agriculture halves of the state CETs).
4. Aptitude: quantitative, reasoning, English, general knowledge (CUET General Aptitude Test, NDA Paper 2, GATE General Aptitude; later CLAT, IPMAT, CAT and the job exams).
5. Class 9-10 Maths and Science (JEECUP in June, and every other polytechnic test).
6. GATE layer on the existing B.Tech books, aimed at February 2028.

## What our existing content already covers

**NCERT class 11-12 (CBSE Free N Easy).** 293 of the 354 Physics, Chemistry, Maths and Biology topics, or 83%, sit in the current NCERT books: Physics 107 of 122, Chemistry 89 of 121, Maths 62 of 68, Biology 35 of 43. By exam: JEE Main 250 of 261 topics, NEET UG 229 of 242, the state CETs 293 of 341, CUET UG 167 of 249 (the rest of CUET is the aptitude test and languages).

**B.Tech universal syllabus.** GATE maps to 786 units across 128 subjects already in the pack. The 20 mapped papers held about 94% of GATE 2026 registrations. Ten papers have nothing in the pack: AG, AR, EY, GE, GG, MN, NM, PE, TF, XH. CUET PG, UGC NET, CSIR NET and IIT JAM are covered only for their science, commerce and computer papers, so their shared score is capped.

**Covered by neither.** The 61 class 11-12 topics outside the current NCERT books that state CETs and JEE Advanced still ask (solid state, surface chemistry, s-block, metallurgy, polymers, states of matter, Carnot engine, Doppler effect, potentiometer and others); all class 9-10 content; all aptitude subjects; legal reasoning; design aptitude; teaching aptitude; medicine, pharmacy, agriculture and law at degree level.

## Production estimate for the top 10

Basis: one book per unit, and three lessons per unit book, the ratio in the B.Tech pack's `videos.json`.

| Block | Books | Lessons | Serves |
|---|---|---|---|
| Physics, Chemistry, Maths, Biology exam layer (76 units, 354 topics; exam-style worked problems, plus full teaching for the 61 topics outside NCERT) | 76 | about 250 | Ranks 1 to 7, and Paper 1 of rank 8 |
| Aptitude: quantitative 6, reasoning 4, English 4, general knowledge 6 units | 20 | about 60 | CUET UG, NDA, GATE General Aptitude |
| Class 9-10 Maths and Science (10 units, 37 topics) | 10 | about 30 | JEECUP, NDA general science |
| Exam guides: pattern and marking, syllabus map, dates and how to apply | 10 short guides | 30 | Each of the ten |
| GATE layer for the five largest papers (optional, for 2028) | 0 new | about 55 | GATE |
| **Total** | **about 106 books and 10 guides** | **about 370, or 425 with the GATE layer** | |

That is roughly one week of the lesson limit at 400 to 500 lessons a week, and about ten subject-sized book runs on GitHub Actions. Physics, Chemistry and Biology are picture-heavy, so they need the figure redraw step.

Past papers: 38 of the 104 entrance exams publish full papers officially and 41 release keys or response sheets only. All seven exams in the shared science stack except MHT CET publish full papers, which is enough to analyse patterns and write our own questions.

## Gaps and things I could not confirm

1. **Class 11 coverage is assumed.** The brief says CBSE Free N Easy covers NCERT 11 and 12. The lesson skills visible here are Class 12 Physics, Chemistry, Maths and Biology, plus commerce. About half of the 293 covered topics are class 11. If class 11 science is not made yet, the exam layer needs full teaching for it and the first block roughly doubles.
2. **Dates not yet announced:** NEET UG 2027 (NTA's calendar to March 2027 omits it; a move to computer-based mode is reported but unconfirmed), CUET UG 2027, JEE Advanced 2027 and every state CET. All are marked expected. JEE Main Session 2 is in NTA's revised calendar, but I could not read the exact April days.
3. **Unverified candidate counts:** of the 125 entries, 19 counts were read from a source, 77 are estimates and 29 are blank. The largest that matter are NDA, JEECUP, BITSAT, VITEEE, CLAT, NEET PG and IIT JAM.
4. **State CET syllabi are mapped as one family.** MHT CET follows the Maharashtra board (20% class 11, 80% class 12) and EAPCET follows the Intermediate boards, which are wider than NCERT. Each needs a line-by-line check before books are written.
5. **Thin entries:** ten smaller state engineering tests and nine state polytechnic tests have dates and patterns from memory and no counts. State talent tests, B.Ed entrances, state nursing and state agriculture tests are listed as families and left unscored; each needs a state-by-state pass.
6. **Not yet listed:** lateral-entry tests for diploma holders (AP, TG and Karnataka ECET/DCET), CS and CMA foundation, D.El.Ed entrances, state law CETs other than Maharashtra, more private-university tests (LPUNEST, UPESEAT, Christ, Symbiosis SET), FDDI, IGRUA, TISS. LSAT India is left out because I could not confirm it still runs.
7. **Source conflicts:** KCET 2026 registrations appear as 3,30,479 and 3,30,646; I used the first. One exam-calendar site gave 2026 dates for MHT CET, KCET and WBJEE that disagree with the press notes; I used the press notes.
8. **Humanities for CUET** is NCERT class 12, but I do not know whether CBSE Free N Easy covers it.

### PDFs and pages to attach

I did not open any official syllabus PDF, and official home pages that did not come up in search needed your approval while you were away. To finish the topic check, please download and attach:

- JEE Main 2027 information bulletin (syllabus annexure), jeemain.nta.nic.in
- NEET UG syllabus (NMC) and the 2027 bulletin when issued, neet.nta.nic.in
- CUET UG 2027 subject syllabi, cuet.nta.nic.in
- MHT CET 2027 syllabus and the 2026 registration table for all 20 CETs, cetcell.mahacet.org
- AP EAPCET and TG EAPCET syllabus, cets.apsche.ap.gov.in and eapcet.tgche.ac.in
- KCET syllabus, cetonline.karnataka.gov.in/kea
- JEECUP 2027 brochure and the AP and TG POLYCET booklets
- NDA (I) 2027 notification, due 2 December 2026, upsc.gov.in
- GATE 2027 paper syllabi, gate2027.iitm.ac.in

## Sources

Figures marked verified come from these pages, read on 13 November 2026. Full URLs sit beside each number in `exams.json`.

- [GATE 2027 important dates, IIT Madras](https://gate2027.iitm.ac.in/important_dates)
- [MHT CET 2026 PCM first attempt press note, CET Cell](https://cetcell.mahacet.org/wp-content/uploads/2026/06/Press-Note-MHT-CET-PCM-Group-1st-Attempt_-2026.pdf)
- [MHT CET 2026 PCB first attempt result notification, CET Cell](https://cetcell.mahacet.org/wp-content/uploads/2026/06/Notification_PCB_1st-Attempt-Result.pdf)
- [CLAT 2027 press release, Consortium of NLUs](https://consortiumofnlus.ac.in/clat-2026/notifications/Press_Release_CLAT_2027.pdf)
- [NTA examination calendar to March 2027 (copy of the public notice)](https://www.careerpower.in/blog/wp-content/uploads/2026/09/16212531/NTA_Exam_Calendar.pdf)
- [NTA revised calendar, Careers360](https://news.careers360.com/nta-revises-exam-calendar-jee-mains-session-1-dates-ugc-net-joint-csir-cuet-pg-cmat-neet)
- [JEE Main 2027 notification, Careers360](https://news.careers360.com/jee-main-2027-notification-out-registration-begins-jeemain-nta-nic-in-session-1-exam-dates-eligbility-registration-fee)
- [JEE Main 2026 candidate statistics, Collegedunia](https://collegedunia.com/news/how-many-students-appeared-for-jee-main-2026-alertid-150907)
- [NEET UG 2026 result highlights, Careers360](https://news.careers360.com/neet-ug-2026-result-highlights-absentees-surge-qualifiers-fall-cut-offs-rise-toppers-list)
- [NEET UG 2027 status, MSM Unify](https://www.msmunify.com/in/exams/neet-ug)
- [CUET UG 2026 figures, MSM Unify](https://www.msmunify.com/in/exams/cuet-ug)
- [JEE Advanced 2026 figures, Collegedunia](https://collegedunia.com/exams/jee-advanced)
- [GATE 2026 statistical report, FindMyCollege](https://articles.findmycollege.com/news/gate-2026-statistical-report-out-19-6-pass-rate-cs-highest-density/)
- [CAT 2026 registrations, CollegeDekho](https://www.collegedekho.com/amp/news/cat-2026-registrations-count-dipped-trends-80231/)
- [CUET PG 2026 result figures, Free Press Journal](https://www.freepressjournal.in/education/cuet-pg-2026-result-out-over-345-lakh-candidates-appeared-in-exam-conducted-across-50-shifts)
- [TG EAPCET 2026 results, Telangana Today](https://telanganatoday.com/medchal-girl-and-hyderabad-boy-top-tg-eapcet-2026-results)
- [AP EAPCET 2026 results, Careers360](https://news.careers360.com/ap-eacmet-toppers-2026-jonnala-roshan-manideep-reddy-btech-sambangi-jaswanth-naidu-bharm-bagri-eapcet-apsche)
- [KCET 2026 result figures, Free Press Journal](https://www.freepressjournal.in/education/kcet-ugcet-result-2026-out-female-candidates-outnumber-male-students-by-over-41000)
- [WBJEE 2026 result figures, Careers360](https://news.careers360.com/wbjee-toppers-list-2026-merit-list-out-wbjeeb-nic-in-shaswat-banerjee-tops-exam-btech-engineering-admissions-counselling)
- [GUJCET 2026 result figures, Free Press Journal](https://www.freepressjournal.in/amp/education/gujcet-2026-result-out-1459-students-score-above-99-percentile-rank)
- [AP POLYCET 2026 results, Deccan Chronicle](https://deccanchronicle.com/southern-states/andhra-pradesh/girls-outperform-boys-in-ap-polycet-exam-1954737)
- [UPSC calendar 2027, StudyIQ](https://www.studyiq.com/articles/upsc-exam-calendar-2027/)
- [Maharashtra CET 2026 participation, Careers360](https://news.careers360.com/maharashtra-cet-2026-records-highest-ever-participation-with-16-29-lakh-mat-pcm-pcb-mba-mms-20-entrance-exam-statistics)
