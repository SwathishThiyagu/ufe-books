# me-thermo-u4: correction pass (Claude, 20 Nov 2026)

- Book: `books/mech/me-thermo/me-thermo-u4.html`
- Status: ok

## Checker

```
me-thermo-u4.html: 7 chapters, 19969 words, 8 figures, 196 KB
OK
```

## What changed

- Packet now has 7 chapters: 4.3 Exact differentials, reciprocity and cyclic relations and 4.7 Expansivity, compressibility, Mayer relation and Joule-Thomson coefficient added; old 4.3-4.5 renumbered 4.4-4.6.
- Every worked example traced; 4.1 example fixed (1000 x (1 - 300/500) is 1000 x 0.4, the draft wrote 0.6); second examples added in every chapter.
- Reviewer flags fixed: dead state (rest, height, chemical), turbine sentence under Gibbs, A/G units trap, dT/dp vs dp/dT for ice, garbled throttling sentence, van der Waals units, figure 4.6 caption.
- Every figure redrawn by hand (pipeline/claude_figs/me_thermo_u4.py) from its chapter's example.
- 14 long questions, each with points to cover and a full model answer.
- University-hosted web source dropped; no cross-unit numbers.
