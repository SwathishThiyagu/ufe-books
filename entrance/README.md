# Entrance exam free n easy: data pack

Research data for the channel, built 13 November 2026. No books or lessons here.

| File | What it is |
|---|---|
| `REPORT.md` | Top-10 order, what the NCERT and B.Tech content already covers, production estimate, gaps, and the list of PDFs to attach. Read this first. |
| `exams.json` | One record per exam, with a source URL and year on every number. `verified: true` = read from that page on the build date; `false` = from the last bulletin as remembered, or an estimate, to be checked on the official site linked. |
| `universal_topics.json` | The merged syllabus per subject. Each topic lists the exams that use it and its overlap with NCERT class 11-12 and with `pack/universal.json`. |
| `map/index.html` | The exam map, published at https://claude.ai/artifact/EUhgTxc1mr77vqc37uvFtN |
| `build/exams_src.py` | The exam rows and the source registry. Edit numbers here. |
| `build/topics_src.py` | The topic trees, the syllabus-family flags and the GATE paper to B.Tech subject map. |
| `build/build.py`, `build/make_map.py` | Regenerate the JSON files, the scores and the map: `cd entrance/build && python3 build.py && python3 make_map.py`. Needs `pack/universal.json`. |

Priority score = candidates (lakh) x underserved (0 to 1, an editorial estimate) x shared (0 to 1, computed from the topic map) x time factor (from the days to the last sitting of the 2027 cycle). The exact rule is in `exams.json` under `meta.priority_formula`.

This branch adds only the `entrance/` folder. It does not touch the unit books, the queue or the pack.
