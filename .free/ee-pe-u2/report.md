# ee-pe-u2 correction pass

Every chapter was rewritten from the draft, and every worked example, quiz answer and question-bank answer was traced by script.

## Draft errors fixed
- Half-wave averages had been integrated over π instead of 2π (they gave 2Vm/π and Vm/√2); now Vm/π and Vm/2.
- "Never measure α from the zero crossing" was wrong for single-phase converters; the natural firing point is now explained for each circuit.
- The continuous-current formula for a half-wave RL circuit ((Vm/π) cos α) was wrong; a half-wave circuit cannot hold continuous current without a freewheeling diode.
- "A large back EMF keeps the current continuous" was reversed, and so was the direction of the error of the continuous formula under discontinuous current.
- The inversion example with an RL load was impossible (inversion needs a DC source); it now sits in the new inversion chapter with E = −120 V.
- The L-C filter ripple claim (1/4 of the unfiltered ripple) was wrong; RF = √2/(12ω²LC) gives about 1/395 for the stated values.
- Single-phase overlap: Ls per line vs total loop inductance clarified; a broken dual-converter trap rewritten; the PFC lead no longer claims every phone charger has PFC; the emulated-resistance formula regained its square; capacitor PIV claims corrected.
- Unverifiable numbers dropped (HVDC leakage percentage, 99 % totem-pole efficiency, 10 % circulating current).

## Added
- New chapters for the new packet subtopics: voltage doubler and three-phase diode bridge rectifiers; inversion mode and the inverter angle limit. Later chapters renumbered.
- Ten hand-drawn figures (pipeline/claude_figs/ee_pe_u2.py), each from the chapter's own worked example.
- 14 full model answers with points to cover.
- Cross-unit references named by topic; web list without the duplicate PFC link.

Checker: `book.html: 10 chapters, 23697 words, 11 figures, 434 KB / OK` (with --render).
