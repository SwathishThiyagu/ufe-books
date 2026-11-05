"""Prompts for the free-model book pipeline. Each function returns the user prompt; SYSTEM is shared.

The rules here are a condensed form of pack/WRITER.md. The model only ever returns JSON; the
pipeline turns that JSON into the book's HTML, draws the figures and checks the numbers.
"""
import json, re

SYSTEM = """You write one unit book of the "University free n easy" series: free study notes for Indian B.Tech students, read on a phone the week before an exam. Many readers have English as a second language.

How to write:
- Plain, short sentences. One idea per paragraph. Define every symbol and term where it first appears. Follow every formula with what each term means. Numbers carry units.
- Explain like a good teacher at the board: the idea, why it exists, how it works step by step, where it is used. Indian context where it helps an example (rupees, UPI, IRCTC, cricket, a Chennai power cut), never forced.
- No filler ("In this chapter we will", "Let us", "It is important to note"), no hedging, no jokes needed, warmth allowed.
- Be correct. Use standard textbook definitions and values. If you are not sure of a number, a date or a name, leave it out. Never invent citations, page numbers, ISBNs or URLs.
- Never name a college or university from the syllabi, and never count them ("taught at 8 of 10"). Write "some syllabi call this ..." or "only a few universities teach this".
- Original explanations only; no textbook passages, no long quotes.
- Text fields may use only these inline tags: <b>, <i>, <code>, <sub>, <sup>, and links to other chapters as <a href="#chapter-id">. No other HTML, no Markdown, no LaTeX. Write formulas with Unicode: x², √, Σ, ≤, ≥, →, ×, ÷, θ, π, log₂ n.

Reply with one JSON object only, exactly in the shape asked for."""


FIGURES = """FIGURE TYPES. Pick the one type that best shows the chapter's mechanism, and fill its fields. The pipeline draws it, so keep labels short (1-4 words; a node "note" up to 6 words). Every figure also has "aria" (one sentence describing it).
- blocks: block diagram or flowchart. {"type":"blocks","direction":"down"|"right","title":"optional","nodes":[{"id":"a","label":"Ready queue","note":"optional small text","style":"normal|accent|live|next|muted"}],"edges":[{"from":"a","to":"b","label":"optional","style":"solid|dashed|live"}]}. 3-10 nodes. "right" only for 2-5 steps in a row. Cycles (back edges) are allowed.
- tree: hierarchy, recursion tree, BST, heap, decision tree, Huffman tree. {"type":"tree","shape":"circle|box","root":{"label":"50","style":"normal","note":"optional","edge":"label on the edge from the parent","children":[...]}}. At most 31 nodes, 5 levels; circle labels at most 3 characters.
- graph: vertices and edges with weights. {"type":"graph","directed":true,"nodes":[{"id":"A","label":"A","x":0,"y":1,"note":"d=0","style":"accent"}],"edges":[{"from":"A","to":"B","label":"4","style":"solid|accent|dashed"}]}. Give x and y (small grid numbers, e.g. 0-4) so the layout is clear. 3-12 nodes.
- array: arrays, memory cells, stacks, queues, hash tables, sorting passes. {"type":"array","title":"optional","show_index":true,"index_from":0,"rows":[{"label":"Pass 1","cells":["5","3","8"],"marks":{"0":"accent","2":"live"}}],"pointers":[{"row":0,"cell":2,"label":"top"}]}. At most 16 cells per row, 6 rows, values of 1-4 characters.
- plot: a graph of computed values. {"type":"plot","x":{"label":"n","min":1,"max":64},"y":{"label":"time","min":0,"max":500},"series":[{"name":"n²","expr":"x**2","style":"accent"},{"name":"measured","points":[[1,2],[2,5]]}]}. expr is a Python expression in x using sqrt, log, log2, log10, exp, sin, cos, pi, e, floor, ceil, factorial. 1-4 series.
- gantt: schedules and timelines (CPU scheduling, pipelines, timing). {"type":"gantt","unit":"ms","lanes":[{"label":"CPU","bars":[{"label":"P1","start":0,"end":5,"style":"accent|live|next|muted"}]}]}. Times are numbers; bars must be long enough to hold their label.
- stack: layers and hierarchies (OSI model, memory hierarchy, OS structure, protocol stack). {"type":"stack","pyramid":false,"items":[{"label":"Application","note":"HTTP, DNS","style":"normal"}],"side":{"top":"faster","bottom":"slower"}}. 2-9 items, top first; "side" is optional.
- sets: nested classes or a Venn diagram. {"type":"sets","mode":"nested|venn","sets":[{"label":"NP","items":["SAT"]}],"overlap":["shared item"]}. nested: outermost first, 2-4 sets. venn: 2 or 3 sets; "overlap" only for 2 sets.
- sequence: messages between parties over time (protocols, client-server, IPC). {"type":"sequence","actors":["Client","Server"],"messages":[{"from":"Client","to":"Server","label":"SYN, seq = x","dashed":false}]}. 2-5 actors, at most 12 messages.
Styles pick things out: accent (blue), live (orange), next (green), muted (grey). Use them for the one or two things the caption tells the reader to notice."""


CHAPTER_SHAPE = """{
  "lead": "One paragraph (60-110 words): what the idea is, why it exists, where it is used.",
  "prereq": "You need: ... with links to earlier chapters or units (one sentence), or an empty string.",
  "sections": [
    {"h3": "Subsection heading",
     "blocks": [
       {"type": "p", "text": "A paragraph."},
       {"type": "steps", "items": ["First step of a procedure or algorithm.", "Second step."]},
       {"type": "bullets", "items": ["A point.", "Another point."]},
       {"type": "formula", "text": "T(n) = 2T(n/2) + n", "where": "T(n) is the time for input size n; ..."},
       {"type": "code", "lang": "c|cpp|java|python|sql|pseudo|text", "code": "complete program text", "stdin": "", "output": "the exact output it prints"},
       {"type": "table", "head": ["Column", "Column"], "rows": [["cell", "cell"]]}
     ]}
  ],
  "figure": {"after_section": 1, "caption": "What the figure shows and what to notice (1-2 sentences).", "spec": {"type": "...", "aria": "..."}},
  "examples": [
    {"question": "A full exam-style question with its numbers.",
     "steps": ["Each step of the solution with intermediate values and units."],
     "answer": "The final answer in one sentence, with units.",
     "check": "Python 3 code that recomputes the final numeric answer(s) from the question's data and prints them, one per line. Empty string only if the answer is not a number.",
     "values": [12.5],
     "code": {"lang": "c", "code": "optional: a complete program for programming examples", "stdin": ""},
     "dry_run": {"head": ["i", "a[i]", "sum"], "rows": [["0", "4", "4"]]},
     "output": "optional: the program's exact output"}
  ],
  "traps": ["Three to five exam traps: confusions, sign and unit slips, look-alike terms, the examiner's favourite question."],
  "quiz": [
    {"level": "remember|understand|apply|analyze", "q": "The question.", "marks": 2, "a": "The model answer; for apply, the key steps and the final value."}
  ],
  "beyond": "Three to six sentences on where this topic goes in industry, research or newer curricula, and what to search next. Start with: Not for the exam."
}"""


def _syllabi(P, match=None):
    """The syllabus lists for this unit, with colleges replaced by letters."""
    out = []
    for k, w in enumerate(P['unit'].get('where', [])):
        topics = w.get('topics') or []
        if match:
            ms = [m.lower() for m in match]
            topics = [t for t in topics if any(m in t.lower() for m in ms)]
            if not topics: continue
        tl = '; '.join(t.strip() for t in topics)[:900]
        out.append(f'- Syllabus {chr(65 + k)} (its unit {w.get("unit")}, "{w.get("title", "")}"): {tl}')
    return '\n'.join(out) or '- (no syllabus lines match this chapter; use the standard textbook scope)'


def _others(P):
    lines = []
    for u in P.get('other_units', []):
        subs = u.get('subtopics', [])
        subs = [s if isinstance(s, str) else s.get('t', '') for s in subs]
        lines.append(f'- Unit {u["n"]}, {u["name"]}: ' + '; '.join(subs))
    return '\n'.join(lines)


def plan(P):
    U = P['unit']; S = P['subject']
    chs = '\n'.join(f'{k}. {s["t"]}  (id: {s["id"]}{", tagged " + "/".join(s["tags"]) if s.get("tags") else ""})' for k, s in enumerate(U['subtopics'], 1))
    return f"""Plan the unit book for: {S['name']}, Unit {U['n']}: {U['name']} (usually semester {S.get('usual_sem', '?')}).

The chapters, fixed and in this order (one per subtopic):
{chs}

What the syllabi list for this unit (they set the depth and the exam wording; never name them):
{_syllabi(P)}

The subject's other units (cross-reference them, never re-teach them):
{_others(P)}

Tags: "advanced" means only a few universities teach it (write it shorter and say only a few universities teach it); "added" means a standard topic no syllabus lists (say in one line that it completes the subject).

Reply with JSON:
{{
  "lead": "Two or three sentences for the top of the book: what the unit is about and what the student can do after it.",
  "about": "One paragraph (80-140 words): what the unit covers and how the chapters build on each other, naming chapters as {U['n']}.1, {U['n']}.2 ...",
  "chapters": [
    {{"k": 1, "idea": "the one idea of the chapter, one sentence",
      "depth": "what to cover and how deep, including other names some syllabi use",
      "figure": "the figure type (blocks, tree, graph, array, plot, gantt, stack, sets, sequence) and what it shows",
      "example": "the worked example: the full question with its numbers",
      "trap": "the main exam trap",
      "prereq": "earlier chapters or units it needs, or empty",
      "leave": "what to leave to other chapters or units"}}
  ],
  "links": [[1, 2, "short label of how chapter 1 leads to chapter 2"]]
}}
One "chapters" entry per chapter, in order ({len(U['subtopics'])} entries). Give 4 to 10 "links" between chapters (by k).

{FIGURES}"""


def chapter(P, k, plan_data):
    U = P['unit']; S = P['subject']; st = U['subtopics'][k - 1]
    pc = plan_data['chapters'][k - 1] if k - 1 < len(plan_data.get('chapters', [])) else {}
    near = []
    for j, c in enumerate(plan_data.get('chapters', []), 1):
        if j != k: near.append(f'- {U["n"]}.{j} {U["subtopics"][j - 1]["t"]} (id {U["subtopics"][j - 1]["id"]}): {c.get("idea", "")}')
    adv = 'advanced' in (st.get('tags') or [])
    added = 'added' in (st.get('tags') or [])
    words = '650-900 words (it is tagged advanced: say in one sentence that only a few universities teach it)' if adv else '1000-1500 words'
    prog = S.get('group', '') in ('Computer Science',) and any(w in (S['name'] + ' ' + U['name'] + ' ' + st['t']).lower() for w in ('program', 'c ', 'java', 'python', 'oop', 'object', 'data structure', 'algorithm', 'sql', 'code', 'function'))
    return f"""Write chapter {U['n']}.{k} of {S['name']}, Unit {U['n']}: {U['name']}.

Chapter title (fixed): {st['t']}
Chapter id: {st['id']}
{"This topic is tagged added: say in one line that it completes the subject." if added else ""}
The plan for this chapter:
{json.dumps(pc, ensure_ascii=False, indent=1)}

The other chapters of this unit (do not repeat their content; link to them with <a href="#id"> where useful):
{chr(10).join(near)}

The subject's other units (refer to them as "see Unit 4, ..." and do not re-teach them):
{_others(P)}

Lines from the syllabi that belong to this chapter (cover this depth; never name the syllabi):
{_syllabi(P, st.get('match') or [st['t']])}

Length: {words} in total, counting every text field. 2 to 4 sections of 150-350 words each. Say each thing once.
Parts:
- One figure (see the figure types below). It must show the mechanism of this chapter with the same values as the text or the worked example.
- One worked example as a full exam question, solved step by step with every intermediate value{"; for programming topics include a complete program in the example's code field, a dry-run table and the exact output" if prog else ""}. Add a second example only if the topic is calculation-heavy.
- In "check", write Python that recomputes the example's numeric answers and prints each one; "values" lists the same numbers as they appear in your answer. The pipeline runs it and rejects the chapter if the numbers disagree.
- Code blocks in C, C++, Java or Python must be complete programs that compile and run; the pipeline runs them and compares the output.
- 3 to 5 exam traps.
- 6 to 8 quiz questions with at least one of each level: remember, understand, apply, analyze. Marks 2 to 6.
- Beyond the syllabus: 3 to 6 sentences.

Reply with JSON in exactly this shape:
{CHAPTER_SHAPE}

{FIGURES}"""


def review(P, k, text):
    U = P['unit']; S = P['subject']; st = U['subtopics'][k - 1]
    return f"""You are checking chapter {U['n']}.{k} ("{st['t']}") of a {S['name']} unit book for Indian B.Tech students before it is published. Read it as a strict examiner and a careful teacher.

Report only real problems:
- high: a factual or technical error, a wrong number or unit, a wrong step in the worked example, code whose shown output is wrong, a definition that contradicts the standard textbooks, a quiz answer that is wrong, content that belongs to another chapter, a sentence a student would misunderstand.
- low: unclear wording, a missing small point, style.

The chapter:
<<<
{text}
>>>

Reply with JSON: {{"issues": [{{"severity": "high|low", "where": "section, example, trap or quiz number", "problem": "what is wrong", "fix": "the correct version"}}]}}
An empty list means the chapter is correct."""


def revise(P, k, chapter_json, issues):
    return f"""Here is chapter {P['unit']['n']}.{k} ("{P['unit']['subtopics'][k - 1]['t']}") as JSON, and a reviewer's list of problems. Fix every high problem and the low ones that are easy, change nothing else, and reply with the whole chapter JSON in the same shape.

Problems:
{json.dumps(issues, ensure_ascii=False, indent=1)}

Chapter JSON:
{json.dumps(chapter_json, ensure_ascii=False)}"""


def resize(P, k, chapter_json, words, low, high):
    verb = 'longer: add explanation, an extra step or a short example in the sections (not filler)' if words < low else 'shorter: cut repetition and side remarks, keep every part'
    return f"""This chapter JSON has about {words} words; it must have {low}-{high}. Make it {verb}. Keep the same shape, the figure, the worked example and the quiz levels. Reply with the whole chapter JSON.

{json.dumps(chapter_json, ensure_ascii=False)}"""


def figure_fix(P, k, fig, error, caption):
    return f"""The figure of chapter {P['unit']['n']}.{k} ("{P['unit']['subtopics'][k - 1]['t']}") could not be drawn: {error}
Its caption: {caption}
Its spec: {json.dumps(fig, ensure_ascii=False)}

Return a corrected figure as JSON {{"caption": "...", "spec": {{...}}}}: same idea, fewer or shorter labels, fields exactly as the figure types require.

{FIGURES}"""


def unit_sections(P, plan_data, chapters_brief):
    U = P['unit']; S = P['subject']
    return f"""Write the unit-level sections of the book for {S['name']}, Unit {U['n']}: {U['name']}.

The chapters and what each teaches:
{chapters_brief}

What the syllabi list for this unit (never name them):
{_syllabi(P)}

Reply with JSON:
{{
  "key_terms": [{{"term": "Term", "meaning": "meaning or formula, one line", "chapter": 1}}],
  "takeaways": ["one-sentence takeaway"],
  "bank_note": "One sentence on what the syllabi stress for this unit's long answers (never name a college).",
  "bank": [{{"group": "remember-understand|apply|analyze-evaluate", "level": "remember|understand|apply|analyze|evaluate", "q": "a long-answer exam question", "marks": 13, "outline": ["the points an examiner looks for"], "chapters": [1, 2]}}],
  "glossary": [{{"term": "Term", "def": "one-sentence definition"}}],
  "textbooks": [{{"title": "standard textbook title", "authors": "authors", "edition": "edition only if sure, else empty", "pointer": "which part covers this unit, only if sure"}}],
  "web": [{{"title": "a free, well-known resource (course notes, open textbook, official documentation)", "url": "https://..."}}],
  "wikipedia": ["Exact title of an English Wikipedia article on a main topic of this unit"]
}}
Counts: 12-20 key terms with their chapter number k; 6-10 takeaways; 12-14 bank questions (8-16 marks) spread over the three groups, at least two of them spanning several chapters; 18-26 glossary terms; 2-4 textbooks you are sure exist; 4-8 web resources whose exact URL you are sure of (each link is opened and checked; wrong ones are dropped); 3-6 Wikipedia article titles."""
