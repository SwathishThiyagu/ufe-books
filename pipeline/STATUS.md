# Book writer status (5 Nov 2026, 20:55 IST)

- RunPod pod `ufe-books` (H100 SXM, $4.02/hr, gpt-oss-120b on vLLM). STOP IT when no RunPod run is in progress.
- Gemini free writer: c-os-u1 in progress, resumes daily at 14:17 IST (requests.txt).
- RunPod writer: OS u2-u6 and CN u1-u6 written on branches free/<unit>-book; a [redo] clean-up pass ran at 20:50.
- Before merging a branch: read .free/<unit>/report.md (checker OK, no "serious" flags left), spot-check examples,
  then copy only books/... into main and set queue.json status "ok". Known: c-os-u3 ch 3.7 Banker's example had wrong
  totals (check it after the redo pass).
- Next: queue more units in requests-runpod.txt (one per line), push, start the pod first; a commit message with [redo]
  re-reviews flagged chapters.
