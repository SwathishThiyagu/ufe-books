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
| c-cloud-u1 | free/c-cloud-u1-book | 1–9 (figure text: ch 8) | OK (library updated) | 11 Nov 2026 |
| c-cloud-u2 | free/c-cloud-u2-book | 1–7 (figure text: ch 2) | OK (library updated) | 11 Nov 2026 |
| c-cloud-u3 | free/c-cloud-u3-book | 1–9 (figure text: ch 7) | OK (library updated) | 11 Nov 2026 |
| c-cloud-u4 | free/c-cloud-u4-book | 1–9 | OK (library updated) | 11 Nov 2026 |
| c-cloud-u5 | free/c-cloud-u5-book | 1–9 | OK (library updated) | 11 Nov 2026 |
| c-cloud-u6 | free/c-cloud-u6-book | 1–9 | OK (library updated) | 11 Nov 2026 |
| c-toc-u1 | ds/c-toc-u1-book | 1–9 | OK (library updated; figure text rewritten: 1.3, 1.9; university-named web sources removed) | 11 Nov 2026 |
| c-toc-u2 | ds/c-toc-u2-book | 1–9 | OK (library updated; figure text rewritten: 2.9; university-named web sources removed) | 11 Nov 2026 |
| c-toc-u3 | free/c-toc-u3-book | 1–9 | OK (library updated; figure text rewritten: 3.5; university-named web sources removed) | 11 Nov 2026 |
| c-toc-u4 | free/c-toc-u4-book | 1–5 | OK (library updated; figure text rewritten: none needed; university-named web sources removed) | 11 Nov 2026 |
| c-toc-u5 | free/c-toc-u5-book | 1–7 | OK (library updated; figure text rewritten: none needed; university-named web sources removed) | 11 Nov 2026 |
| c-toc-u6 | free/c-toc-u6-book | 1–8 | OK (library updated; figure text rewritten: 6.8; university-named web sources removed) | 11 Nov 2026 |
| c-web-u1 | free/c-web-u1-book | 1–6 | OK (library updated; figure text: existing sentences already match; no university names left) | 11 Nov 2026 |
| c-web-u2 | free/c-web-u2-book | 1–9 | OK (library updated; figure text: existing sentences already match; no university names left) | 11 Nov 2026 |
| c-web-u3 | free/c-web-u3-book | 1–9 | OK (library updated; figure text: existing sentences already match; no university names left) | 11 Nov 2026 |
| c-web-u4 | free/c-web-u4-book | 1–9 | OK (library updated; figure text: existing sentences already match; no university names left) | 11 Nov 2026 |
| c-web-u5 | free/c-web-u5-book | 1–9 | OK (library updated; figure text: existing sentences already match; no university names left) | 11 Nov 2026 |
| c-web-u6 | free/c-web-u6-book | 1–9 | OK (library updated; 6.6 answer typo affactedRows fixed; no university names left) | 11 Nov 2026 |
| c-ml-u1 | ds/c-ml-u1-book | 1–7 | OK (library updated; figure sentences in 1.4 and 1.5 rewritten) | 11 Nov 2026 |
| c-ml-u2 | ds/c-ml-u2-book | 1–7 | OK (library updated; Stanford course-notes source dropped) | 11 Nov 2026 |
| c-ml-u3 | ds/c-ml-u3-book | 1–9 | OK (library updated) | 11 Nov 2026 |
| c-ml-u4 | free/c-ml-u4-book | 1–9 | OK (library updated; 4.2 SSE sentence and 4.5 PCA example corrected) | 11 Nov 2026 |
| c-ml-u5 | ds/c-ml-u5-book | 1–9 | OK (library updated; Stanford course-notes source dropped) | 11 Nov 2026 |
| c-ml-u6 | main (library only, apply_html.py) | 1–5 | OK (college colour codes removed) | 11 Nov 2026 |
| c-se-u1 | free/c-se-u1-book | 1–7 | OK (library updated; university colour codes and university-hosted sources removed) | 11 Nov 2026 |
| c-se-u2 | free/c-se-u2-book | 1–9 (figure text: ch 2) | OK (library updated; university colour codes and university-hosted sources removed) | 11 Nov 2026 |
| c-se-u3 | free/c-se-u3-book | 1–8 (figure text: ch 2; ch 3 pipeline-capacity fix) | OK (library updated; university colour codes removed) | 11 Nov 2026 |
| c-se-u4 | free/c-se-u4-book | 1–9 | OK (library updated; university colour codes removed) | 11 Nov 2026 |
| c-se-u5 | free/c-se-u5-book | 1–8 | OK (library updated; university colour codes removed) | 11 Nov 2026 |
| c-se-u6 | free/c-se-u6-book | 1–9 (figure text: ch 8, 9) | OK (library updated; university colour codes and university-hosted sources removed) | 11 Nov 2026 |
| c-quantum-u1 | free/c-quantum-u1-book | 1–7 | OK (library updated; 4 wrong statements fixed; 2 university sources dropped) | 17 Nov 2026 |
| c-nlp-u1 | free/c-nlp-u1-book | 1–8 (figure text: ch 5, 6 wrong step reasons fixed) | OK (library updated; Porter step and FST analysis reasons corrected; university-hosted sources dropped) | 17 Nov 2026 |
| c-mobile-u1 | free/c-mobile-u1-book | 1–8 (figure text: ch 2) | OK (library added; university counts removed; NPTEL source dropped) | 17 Nov 2026 |
| c-dist-u1 | free/c-dist-u1-book | 1–8 | OK (library updated; university mention in 1.4 removed; butterfly link rule in 1.5 corrected) | 17 Nov 2026 |
