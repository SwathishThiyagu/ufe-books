# Book writer status (6 Nov 2026, 11:30 IST)

Every CSE unit is now written. In the library (main): 55. Waiting on branches, all passing check_book --render:

- DeepSeek, branch ds/<unit>-book (preferred over the gpt-oss free/ version of the same unit):
  c-os-u1..u6, c-cn-u1..u6, c-ml-u1..u3, c-ml-u5, c-toc-u1, c-toc-u2
- gpt-oss (RunPod), branch free/<unit>-book: c-ml-u4 (its DeepSeek rewrite fails the phone-width check)
- DeepSeek, branch free/<unit>-book: every other remaining CSE unit (the 100 queued on 6 Nov, incl. c-se-u6, c-iot-u4, c-unix-u2)

Merge procedure per unit: read .free/<unit>/report.md (no "serious" flags), spot-check one worked example and one figure,
`git checkout origin/<branch> -- <out path>` onto main, set queue.json status "ok", append syllabus notes to notes.md, commit "<unit> book".
Writers: DeepSeek lanes = deepseek-books*.yml (requests-deepseek*.txt; lanes 2-3 write to ds/ branches). Off-peak is half price.
