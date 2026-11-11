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
| c-dl-u5 | free/c-dl-u5-book | 1–7 | OK (library updated) | 10 Nov 2026 |
| c-dl-u6 | free/c-dl-u6-book | 1–7 | OK (library updated) | 10 Nov 2026 |
| c-sec-u1 | free/c-sec-u1-book | 1–7 | OK (library updated) | 10 Nov 2026 |
| c-cn-u1 | ds/c-cn-u1-book | 1–8 | OK | 10 Nov 2026 |
| c-sec-u2 | free/c-sec-u2-book | 1–7 | OK (library updated) | 10 Nov 2026 |
| c-cn-u2 | ds/c-cn-u2-book | 1–8 | OK | 10 Nov 2026 |
| c-sec-u3 | free/c-sec-u3-book | 1–9 | OK (library updated) | 10 Nov 2026 |
| c-cn-u3 | ds/c-cn-u3-book | 1–9 | OK | 10 Nov 2026 |
| c-sec-u4 | free/c-sec-u4-book | 1–9 | OK (library updated) | 10 Nov 2026 |
| c-cn-u4 | ds/c-cn-u4-book | 1–9 | OK | 10 Nov 2026 |
| c-cn-u5 | ds/c-cn-u5-book | 1–8 | OK | 10 Nov 2026 |
| c-sec-u5 | free/c-sec-u5-book | 1–9 | OK (library updated) | 10 Nov 2026 |
| c-cn-u6 | ds/c-cn-u6-book | 1–7 | OK | 10 Nov 2026 |
| c-sec-u6 | free/c-sec-u6-book | 1–9 | OK (library updated) | 10 Nov 2026 |
| c-toc-u1 | ds/c-toc-u1-book | 1–9 | OK | 10 Nov 2026 |
| c-data-u1 | main (library only, apply_html.py) | 1–5 | OK | 10 Nov 2026 |
| c-toc-u2 | ds/c-toc-u2-book | 1–9 | OK | 10 Nov 2026 |
| c-data-u2 | main (library only, apply_html.py) | 1–9 | OK | 10 Nov 2026 |
| c-graphics-u1 | free/c-graphics-u1-book | 1–9 | OK | 10 Nov 2026 |
| c-data-u3 | main (library only, apply_html.py) | 1–8 | OK | 10 Nov 2026 |
| c-data-u4 | main (library only, apply_html.py) | 1–7 | OK | 10 Nov 2026 |
| c-graphics-u2 | free/c-graphics-u2-book | 1–8 | OK | 10 Nov 2026 |
| c-data-u5 | main (library only, apply_html.py) | 1–9 | OK | 10 Nov 2026 |
| c-data-u6 | main (library only, apply_html.py) | 1–8 | OK | 10 Nov 2026 |
| c-graphics-u3 | free/c-graphics-u3-book | 1–8 | OK | 10 Nov 2026 |
| c-graphics-u4 | free/c-graphics-u4-book | 1–9 | OK | 10 Nov 2026 |
| c-cv-u1 | free/c-cv-u1-book | 1–9 | OK (library updated) | 10 Nov 2026 |
| c-graphics-u5 | free/c-graphics-u5-book | 1–9 | OK | 10 Nov 2026 |
| c-cv-u2 | free/c-cv-u2-book | 1–8 | OK (library updated) | 10 Nov 2026 |
| c-graphics-u6 | free/c-graphics-u6-book | 1–9 | OK | 10 Nov 2026 |
| c-cv-u3 | free/c-cv-u3-book | 1–9 | OK (library updated) | 10 Nov 2026 |
| c-cv-u4 | free/c-cv-u4-book | 1–9 | OK (library updated) | 10 Nov 2026 |
| c-cv-u5 | free/c-cv-u5-book | 1–9 | OK (library updated) | 10 Nov 2026 |
| c-cv-u6 | free/c-cv-u6-book | 1–9 | OK (library updated) | 10 Nov 2026 |
| c-iot-u1 | free/c-iot-u1-book | 1–9 | OK (library updated; figure text rewritten) | 11 Nov 2026 |
| c-iot-u2 | free/c-iot-u2-book | 1–7 | OK (library updated; figure text rewritten) | 11 Nov 2026 |
| c-iot-u3 | free/c-iot-u3-book | 1–9 | OK (library updated; figure text rewritten) | 11 Nov 2026 |
| c-iot-u4 | free/c-iot-u4-book | 1–7 | OK (library updated; figure text rewritten) | 11 Nov 2026 |
| c-iot-u5 | free/c-iot-u5-book | 1–7 | OK (library updated; figure text rewritten) | 11 Nov 2026 |
| c-iot-u6 | free/c-iot-u6-book | 1–6 | OK (library updated; figure text rewritten) | 11 Nov 2026 |
