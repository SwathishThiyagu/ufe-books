# Book writer status (6 Nov 2026, 11:30 IST)

Every CSE unit is now written. In the library (main): 55. Waiting on branches, all passing check_book --render:

- DeepSeek, branch ds/<unit>-book (preferred over the gpt-oss free/ version of the same unit):
  c-os-u1..u6, c-cn-u1..u6, c-ml-u1..u3, c-ml-u5, c-toc-u1, c-toc-u2
- gpt-oss (RunPod), branch free/<unit>-book: c-ml-u4 (its DeepSeek rewrite fails the phone-width check)
- DeepSeek, branch free/<unit>-book: every other remaining CSE unit (the 100 queued on 6 Nov, incl. c-se-u6, c-iot-u4, c-unix-u2)

Merge procedure per unit: read .free/<unit>/report.md (no "serious" flags), spot-check one worked example and one figure,
`git checkout origin/<branch> -- <out path>` onto main, set queue.json status "ok", append syllabus notes to notes.md, commit "<unit> book".
Writers: DeepSeek lanes = deepseek-books*.yml (requests-deepseek*.txt; lanes 2-3 write to ds/ branches). Off-peak is half price.

## Claude hand-drawn figures (pipeline/claude_figs, one line per finished book)

| Book | Branch | Chapters redrawn | Checker | Date |
|---|---|---|---|---|
| c-dl-u2 | free/c-dl-u2-book | 1–9 | OK | 7 Nov 2026 |
| c-os-u1 | ds/c-os-u1-book | 1–9 | OK | 7 Nov 2026 |
| c-os-u2 | ds/c-os-u2-book | 1–9 | OK | 7 Nov 2026 |
| c-os-u3 | ds/c-os-u3-book | 1–8 | OK | 7 Nov 2026 |
| c-os-u4 | ds/c-os-u4-book | 1–9 | OK | 7 Nov 2026 |
| c-os-u5 | ds/c-os-u5-book | 1–9 | OK | 7 Nov 2026 |
| c-os-u6 | ds/c-os-u6-book | 1–9 | OK | 7 Nov 2026 |
| c-compiler-u1 | free/c-compiler-u1-book | 1–9 | OK (library updated) | 10 Nov 2026 |
| c-compiler-u2 | free/c-compiler-u2-book | 1–7 | OK (library updated) | 10 Nov 2026 |
| c-compiler-u3 | free/c-compiler-u3-book | 1–6 | OK (library updated) | 10 Nov 2026 |
| c-compiler-u4 | free/c-compiler-u4-book | 1–7 | OK (library updated) | 10 Nov 2026 |
| c-compiler-u5 | free/c-compiler-u5-book | 1–6 | OK (library updated) | 10 Nov 2026 |
| c-coa-u1 | main (library only, apply_html.py) | 1–7 | OK | 10 Nov 2026 |
| c-compiler-u6 | free/c-compiler-u6-book | 1–6 | OK (library updated) | 10 Nov 2026 |
| c-coa-u2 | main (library only, apply_html.py) | 1–8 | OK | 10 Nov 2026 |
| c-dl-u1 | free/c-dl-u1-book | 1–9 | OK (library updated) | 10 Nov 2026 |
| c-coa-u3 | main (library only, apply_html.py) | 1–9 | OK | 10 Nov 2026 |
| c-dl-u3 | free/c-dl-u3-book | 1–9 | OK (library updated) | 10 Nov 2026 |
| c-coa-u4 | main (library only, apply_html.py) | 1–6 | OK | 10 Nov 2026 |
| c-dl-u4 | free/c-dl-u4-book | 1–7 | OK (library updated) | 10 Nov 2026 |
| c-coa-u5 | main (library only, apply_html.py) | 1–9 | OK | 10 Nov 2026 |
| c-coa-u6 | main (library only, apply_html.py) | 1–9 | OK | 10 Nov 2026 |
