# Book writer status (5 Nov 2026, 21:45 IST)

- RunPod pod `ufe-books` (H100 SXM, $4.02/hr): stopped after tonight's runs. Restart it before a RunPod run.
- Gemini free writer: c-os-u1 in progress; resumes daily at 14:17 IST (requests.txt).
- Written by RunPod tonight, checker OK, on branches free/<unit>-book (18): c-os-u2..u6, c-cn-u1..u6, c-ml-u1..u5, c-toc-u1, c-toc-u2.
- Not done: c-ml-u6 (no branch; rerun it), c-toc-u3..u6 and the rest of the queue.
- Before merging: read .free/<unit>/report.md (no "serious" flags), spot-check worked examples and figures,
  copy only books/... into main, set queue.json status "ok". Check c-os-u3 chapter 3.7 (Banker's) first.
- Lanes: requests-runpod.txt (main) and requests-runpod-2.txt (second lane) run in parallel on one pod.
  A commit message containing [redo] re-reviews flagged chapters and re-checks the books listed.
