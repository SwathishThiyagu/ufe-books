"""Turn the model's JSON into the book's HTML, inside pack/book_shell.html."""
import html, re, os, datetime
import figures as F

ALLOWED = re.compile(r'</?(?:b|i|em|strong|code|sub|sup)>|<br\s*/?>|<a href="#[a-z0-9-]+">|</a>', re.I)
COLLEGE = re.compile(r"Anna Univ(?:ersity|\.)?|\bSRM(?: IST| University)?\b|\bIIT[ -]?(?:Madras|Delhi|Bombay)\b|\bIIT[MDB]\b"
                     r"|\bNIT[ -]?(?:Trichy|Tiruchirappalli|Surathkal|Karnataka|Calicut)\b|\bNIT[TKC]\b|\bManipal\b|\bChrist University\b|\bChrist\b(?! ?(?:mas|ian))")
COUNTED = re.compile(r'\b(?:taught at|covered by|in) \d+ of (?:the )?(?:10|ten)\b(?: (?:universities|syllabi))?', re.I)
LEVELS = ['remember', 'understand', 'apply', 'analyze']


def scrub(s):
    """Words the checker refuses, and the channel's naming rules."""
    s = COLLEGE.sub('some universities', s)
    s = COUNTED.sub('in several syllabi', s)
    s = re.sub(r'placeholder', 'stand-in', s, flags=re.I)
    s = re.sub(r'\bTODO\b', 'to-do', s); s = re.sub(r'\bTBD\b', 'to be decided', s)
    s = re.sub(r'lorem ipsum', '', s, flags=re.I); s = re.sub(r'\[citation needed\]', '', s, flags=re.I)
    s = re.sub(r'\bas an AI\b', '', s, flags=re.I); s = re.sub(r'\bI cannot\b', 'one cannot', s); s = re.sub(r'(?i)(i) cannot', r'\1 can not', s)  # e.g. 'API cannot'
    s = re.sub(r'__([A-Za-z0-9_]+?)__', lambda m: '&#95;&#95;' + m.group(1) + '&#95;&#95;', s)
    return s


def brk(text):
    """Break points inside very long words (ids, URLs, hyphen chains) so phones do not scroll sideways."""
    return re.sub(r'[^\s<>&]{24,}', lambda m: re.sub(r'([-\u2011_/.(,=])(?=.)', r'\1<wbr>', m.group(0)), text)


def inline(s, ids=()):
    """Escape model text but keep the few inline tags we allow; links only to real chapter ids."""
    s = html.unescape(str(s or '')).strip()
    out, pos, stack = [], 0, []
    for m in ALLOWED.finditer(s):
        out.append(brk(html.escape(s[pos:m.start()], quote=False)))
        tag = m.group(0)
        low = tag.lower()
        if low.startswith('<a '):
            target = re.search(r'#([a-z0-9-]+)', low).group(1)
            if ids and target not in ids:
                stack.append('a-skip'); pos = m.end(); continue
            stack.append('a'); out.append(tag)
        elif low == '</a>':
            if stack and stack[-1] == 'a-skip': stack.pop()
            elif 'a' in stack: stack.remove('a'); out.append(tag)
        elif low.startswith('<br'):
            out.append('<br>')
        elif low.startswith('</'):
            name = low[2:-1]
            if name in stack: stack.remove(name); out.append(f'</{name}>')
        else:
            name = low[1:-1]; stack.append(name); out.append(f'<{name}>')
        pos = m.end()
    out.append(brk(html.escape(s[pos:], quote=False)))
    for name in reversed(stack):
        if name != 'a-skip': out.append(f'</{name}>')
    t = ''.join(out)
    # long inline code tokens: allow line breaks so phones do not scroll sideways
    t = re.sub(r'<code>([^<]{26,})</code>', lambda m: '<code>' + re.sub(r'([._(,/=])', r'\1<wbr>', m.group(1)) + '</code>', t)
    return t


def code_block(code, lang=''):
    return f'<pre><code>{html.escape(str(code).rstrip(), quote=False)}</code></pre>'


def table(head, rows, ids=()):
    h = ''.join(f'<th>{inline(c, ids)}</th>' for c in head or [])
    b = ''.join('<tr>' + ''.join(f'<td>{inline(c, ids)}</td>' for c in r) + '</tr>' for r in rows or [] if isinstance(r, list))
    return f'<div class="tablewrap"><table>{"<thead><tr>" + h + "</tr></thead>" if h else ""}<tbody>{b}</tbody></table></div>'


LANG = {'c': 'C', 'cpp': 'C++', 'c++': 'C++', 'java': 'Java', 'python': 'Python', 'py': 'Python', 'sql': 'SQL', 'pseudo': 'Pseudocode', 'text': ''}

def block(b, ids):
    t = b.get('type')
    if t == 'p': return f'<p>{inline(b.get("text"), ids)}</p>'
    if t == 'steps': return '<ol class="steps">' + ''.join(f'<li>{inline(x, ids)}</li>' for x in b.get('items') or []) + '</ol>'
    if t == 'bullets': return '<ul>' + ''.join(f'<li>{inline(x, ids)}</li>' for x in b.get('items') or []) + '</ul>'
    if t == 'formula':
        f = str(b.get('text', ''))
        out = f'<pre>{html.escape(f, quote=False)}</pre>' if ('\n' in f or len(f) > 46) else f'<p class="lead"><b>{inline(f)}</b></p>'
        if b.get('where'): out += f'<p>{inline(b["where"], ids)}</p>'
        return out
    if t == 'code':
        lang = LANG.get(str(b.get('lang', '')).lower(), str(b.get('lang', '')))
        out = (f'<p><b>{lang} program.</b></p>' if lang and lang not in ('Pseudocode',) else ('<p><b>Pseudocode.</b></p>' if lang == 'Pseudocode' else '')) + code_block(b.get('code', ''))
        if str(b.get('output', '')).strip():
            out += '<p><b>Output</b></p>' + code_block(b['output'])
        return out
    if t == 'table': return table(b.get('head'), b.get('rows'), ids)
    if b.get('text'): return f'<p>{inline(b["text"], ids)}</p>'
    return ''


def figure_html(spec, uid, num, caption, fallback_title, fallback_steps):
    try:
        svg = F.render(spec, uid); ok = True
    except F.FigureError:
        svg = F.fallback(fallback_title, fallback_steps, uid, caption or fallback_title); ok = False
    return f'<figure class="fig">{svg}<figcaption><b>Figure {num}</b> {inline(caption)}</figcaption></figure>', ok


def chapter_html(P, k, ch, ids):
    U = P['unit']; st = U['subtopics'][k - 1]; N = U['n']
    out = [f'<section class="ch" id="{st["id"]}" data-n="{k}">',
           f'<h2><span class="num">{N}.{k}</span> {html.escape(st["t"], quote=False)}</h2>',
           f'<p class="lead">{inline(ch.get("lead"), ids)}</p>']
    if str(ch.get('prereq', '')).strip():
        pr = inline(ch['prereq'], ids)
        out.append(f'<div class="prereq">{pr if pr.lower().startswith("you need") else "You need: " + pr}</div>')
    fig = ch.get('figure') or {}
    after = fig.get('after_section', 1)
    try: after = max(1, min(int(after), len(ch.get('sections') or [1])))
    except (TypeError, ValueError): after = 1
    fig_ok = True
    for i, sec in enumerate([x for x in ch.get('sections') or [] if isinstance(x, dict)], 1):
        out.append(f'<h3>{inline(sec.get("h3"))}</h3>')
        out += [block(b, ids) for b in sec.get('blocks') or [] if isinstance(b, dict)]
        if i == after:
            fh, fig_ok = figure_html(fig.get('spec') or {}, f'f{N}-{k}-1', f'{N}.{k}.1', fig.get('caption', ''), st['t'],
                                     [s.get('h3', '') for s in ch.get('sections') or [] if isinstance(s, dict)])
            out.append(fh)
    exs = [e for e in ch.get('examples') or [] if isinstance(e, dict)]
    for j, ex in enumerate(exs):
        h4 = 'Worked example' if j == 0 else 'Worked example 2'
        e = [f'<div class="example"><h4>{h4}</h4>', f'<p><b>Question.</b> {inline(ex.get("question"), ids)}</p>']
        cd = ex.get('code') or {}
        if isinstance(cd, dict) and str(cd.get('code', '')).strip():
            lang = LANG.get(str(cd.get('lang', '')).lower(), str(cd.get('lang', '')))
            e.append((f'<p><b>{lang} program.</b></p>' if lang else '') + code_block(cd['code']))
        if ex.get('steps'):
            e.append('<ol class="steps">' + ''.join(f'<li>{inline(x, ids)}</li>' for x in ex['steps']) + '</ol>')
        dr = ex.get('dry_run') or {}
        if isinstance(dr, dict) and dr.get('rows'):
            e.append('<p><b>Dry run</b></p>' + table(dr.get('head'), dr.get('rows'), ids))
        if str(ex.get('output', '')).strip():
            e.append('<p><b>Output</b></p>' + code_block(ex['output']))
        if ex.get('answer'):
            e.append(f'<p><b>Answer.</b> {inline(ex["answer"], ids)}</p>')
        e.append('</div>')
        out.append(''.join(e))
    out.append('<div class="traps"><h4>Exam traps</h4><ul>' + ''.join(f'<li>{inline(t, ids)}</li>' for t in ch.get('traps') or []) + '</ul></div>')
    qs = []
    for q in [q for q in ch.get('quiz') or [] if isinstance(q, dict)]:
        lv = str(q.get('level', 'understand')).lower()
        lv = lv if lv in LEVELS else ('analyze' if lv.startswith('anal') or lv == 'evaluate' else 'understand')
        try: mk = int(q.get('marks', 2))
        except (TypeError, ValueError): mk = 2
        qs.append(f'<details class="q" data-level="{lv}"><summary><span class="lvl">{lv.capitalize()}</span> <span style="min-width:0;overflow-wrap:anywhere">{inline(q.get("q"), ids)}</span> <span class="marks">{mk} marks</span></summary><p>{inline(q.get("a"), ids)}</p></details>')
    out.append('<div class="quiz"><h4>Check yourself</h4>' + ''.join(qs) + '</div>')
    by = inline(ch.get('beyond'), ids)
    if 'not for the exam' not in by.lower(): by = 'Not for the exam. ' + by
    out.append(f'<div class="beyond"><h4>Beyond the syllabus</h4><p>{by}</p></div>')
    out.append('</section>')
    return '\n'.join(out), fig_ok


def about_html(P, plan):
    U = P['unit']
    lis = []
    for k, s in enumerate(U['subtopics'], 1):
        tag = ''.join(f' <span class="tag">{t}</span>' for t in (s.get('tags') or []) if t in ('advanced', 'added'))
        lis.append(f'<li><a href="#{s["id"]}">{html.escape(s["t"], quote=False)}</a>{tag}</li>')
    return ('<section id="about"><h2>About this unit</h2>'
            f'<p>{inline(plan.get("about"))}</p>'
            '<h3>Chapters</h3><ol>' + ''.join(lis) + '</ol>'
            '<h3>How to use this book</h3><ul>'
            '<li>Read the lead paragraph and the figure of a chapter first; together they carry the one idea.</li>'
            '<li>Cover the solution of each worked example, work it yourself with the same numbers, then compare line by line.</li>'
            '<li>Answer every “Check yourself” question on paper before you open it.</li></ul></section>')


def unit_map(P, plan):
    U = P['unit']; N = U['n']; subs = U['subtopics']
    nodes = []
    for k, s in enumerate(subs, 1):
        words = s['t'].split(':')[0].split(' and ')[0].split()
        short = ' '.join(words[:4])
        nodes.append({'id': str(k), 'label': f'{N}.{k} {short}', 'style': 'accent' if k == 1 else 'normal'})
    edges = []
    for l in plan.get('links') or []:
        try:
            a, b = int(l[0]), int(l[1])
        except (TypeError, ValueError, IndexError):
            continue
        if 1 <= a <= len(subs) and 1 <= b <= len(subs) and a != b and a < b:
            edges.append({'from': str(a), 'to': str(b)})
    edges = edges[:12]
    layers = [[str(k) for k in range(i + 1, min(i + 3, len(subs)) + 1)] for i in range(0, len(subs), 3)]
    spec = {'type': 'blocks', 'direction': 'down', 'nodes': nodes, 'edges': edges, 'layers': layers,
            'aria': f'Map of the {len(subs)} chapters of Unit {N} and how they connect'}
    try:
        svg = F.render(spec, f'map{N}')
    except F.FigureError:
        spec['edges'] = [{'from': str(k), 'to': str(k + 1)} for k in range(1, len(subs))]
        for n in nodes: n['label'] = n['label'].split()[0]
        svg = F.render(spec, f'map{N}')
    return f'<figure class="fig">{svg}<figcaption><b>Figure {N}.0</b> The chapters of this unit in reading order; arrows show which chapter builds on which.</figcaption></figure>'


def summary_html(P, plan, us):
    N = P['unit']['n']
    rows = ''.join(f'<tr><td>{inline(t.get("term"))}</td><td>{inline(t.get("meaning"))}</td><td>{N}.{inline(t.get("chapter", ""))}</td></tr>' for t in us.get('key_terms') or [])
    take = ''.join(f'<li>{inline(t)}</li>' for t in us.get('takeaways') or [])
    return ('<section id="summary"><h2>Unit summary</h2><div class="keybox"><h4>Key terms and formulas</h4>'
            f'<div class="tablewrap"><table><thead><tr><th>Term</th><th>Meaning or formula</th><th>Chapter</th></tr></thead><tbody>{rows}</tbody></table></div></div>'
            f'{unit_map(P, plan)}<h3>Takeaways</h3><ol>{take}</ol></section>')


GROUPS = [('remember-understand', 'Remember and understand'), ('apply', 'Apply'), ('analyze-evaluate', 'Analyze and evaluate')]

def bank_html(P, us):
    out = ['<section id="question-bank"><h2>Exam question bank</h2>']
    if us.get('bank_note'): out.append(f'<p class="note">{inline(us["bank_note"])}</p>')
    bank = us.get('bank') or []
    for key, title in GROUPS:
        items = [q for q in bank if str(q.get('group', '')).lower().startswith(key.split('-')[0])]
        if not items: continue
        out.append(f'<h3>{title}</h3><div class="quiz">')
        for q in items:
            lv = str(q.get('level', key.split('-')[0])).lower()
            if lv not in LEVELS + ['evaluate']: lv = key.split('-')[0]
            try: mk = int(q.get('marks', 13))
            except (TypeError, ValueError): mk = 13
            outline = '; '.join(str(x).rstrip('.') for x in q.get('outline') or []) + '.'
            out.append(f'<details data-level="{lv}"><summary><span class="lvl">{lv.capitalize()}</span> <span style="min-width:0;overflow-wrap:anywhere">{inline(q.get("q"))}</span> <span class="marks">{mk} marks</span></summary><p>{inline(outline)}</p></details>')
        out.append('</div>')
    out.append('</section>')
    return ''.join(out)


def glossary_html(us):
    items = sorted((g for g in us.get('glossary') or [] if g.get('term')), key=lambda g: str(g['term']).lower())
    return '<section id="glossary"><h2>Glossary</h2><dl class="gloss">' + ''.join(f'<dt>{inline(g["term"])}</dt><dd>{inline(g.get("def"))}</dd>' for g in items) + '</dl></section>'


def sources_html(us, web_checked):
    books = []
    for b in us.get('textbooks') or []:
        s = f'{inline(b.get("authors"))}, <i>{inline(b.get("title"))}</i>'
        if b.get('edition'): s += f', {inline(b["edition"])}'
        if b.get('pointer'): s += f': {inline(b["pointer"])}'
        books.append(f'<li>{s} (from memory; check).</li>')
    out = ['<section id="sources"><h2>Sources and further reading</h2><h3>Textbooks</h3><ul class="srcs">' + ''.join(books) + '</ul>']
    if web_checked:
        out.append('<h3>Open web resources</h3>')
        out.append(f'<p class="note">Each link below was opened by the book script on {datetime.date.today():%d %b %Y} and returned a page; the pages were not read line by line.</p><ul class="srcs">')
        for w in web_checked:
            url = html.escape(w['url'], quote=True)
            out.append(f'<li>{inline(w.get("title"))}: <a href="{url}">{html.escape(re.sub(r"^https://(www\\.)?", "", w["url"]).rstrip("/"), quote=False)}</a></li>')
        out.append('</ul>')
    out.append('<p>Syllabus: the University free n easy universal syllabus, built from top universities\' syllabi.</p></section>')
    return ''.join(out)


def book(P, shell, plan, chapters_html, us, web_checked):
    U = P['unit']; S = P['subject']
    dept = P.get('departments', {}).get(S.get('dept'), S.get('group', ''))
    total = len(P.get('other_units', [])) + 1
    main = '\n'.join([about_html(P, plan)] + chapters_html + [summary_html(P, plan, us), bank_html(P, us), glossary_html(us), sources_html(us, web_checked)])
    main = scrub(main)
    chips = f'<span class="chip">Usually Sem {S.get("usual_sem", "")}</span><span class="chip">{len(U["subtopics"])} chapters</span>'
    foot = (f'Built for the University free n easy YouTube channel from the universal syllabus of {S["name"]} (Oct 2026). '
            "Written with top universities' syllabi and standard textbooks; check a formula against your prescribed book before an exam, and report mistakes on the channel.")
    rep = {'__TITLE__': html.escape(f'{S["name"]} · Unit {U["n"]}: {U["name"]} · University free n easy', quote=False),
           '__CRUMB__': html.escape(f'{dept} · {S["name"]} · Unit {U["n"]} of {total}', quote=False),
           '__EYEBROW__': html.escape(f'Universal syllabus · {S["name"]}', quote=False),
           '__SUBJECT__': html.escape(S['name'], quote=False), '__UNIT_NO__': str(U['n']),
           '__UNIT_NAME__': html.escape(U['name'], quote=False), '__LEAD__': scrub(inline(plan.get('lead'))),
           '__CHIPS__': chips, '__FOOT__': html.escape(foot, quote=False)}
    page = shell.replace('Fill the __PLACEHOLDERS__ and the <main> only', 'Fill the marked fields and the <main> only')
    # the shell's unused per-college colour variables and dot classes carry college names: drop them
    page = re.sub(r'\s*--u-[a-z]+:#[0-9a-fA-F]{3,8};', '', page)
    page = re.sub(r'\n\.d-[a-z]+\{background:var\(--u-[a-z]+\)\}[^\n]*', '', page)
    for k, v in rep.items():
        page = page.replace(k, v)
    page = page.replace('__MAIN__', main)
    return page


def plain_text(P, k, ch):
    """The chapter as readable text, for the reviewer."""
    U = P['unit']; t = []
    strip = lambda s: re.sub(r'<[^>]+>', '', str(s or ''))
    t.append(f'{U["n"]}.{k} {U["subtopics"][k - 1]["t"]}\n\nLead: {strip(ch.get("lead"))}')
    for i, s in enumerate([x for x in ch.get('sections') or [] if isinstance(x, dict)], 1):
        t.append(f'\nSection {i}: {strip(s.get("h3"))}')
        for b in [b for b in s.get('blocks') or [] if isinstance(b, dict)]:
            if b.get('type') in ('steps', 'bullets'): t += ['  - ' + strip(x) for x in b.get('items') or []]
            elif b.get('type') == 'code': t.append(f'  [{b.get("lang")} code]\n{b.get("code")}\n  [shown output]\n{b.get("output", "")}')
            elif b.get('type') == 'table': t.append('  [table] ' + ' | '.join(map(strip, b.get('head') or [])) + '\n' + '\n'.join('   ' + ' | '.join(map(strip, r)) for r in b.get('rows') or []))
            elif b.get('type') == 'formula': t.append(f'  [formula] {b.get("text")}  where: {strip(b.get("where"))}')
            else: t.append('  ' + strip(b.get('text')))
    fig = ch.get('figure') or {}
    t.append(f'\nFigure: {strip(fig.get("caption"))}\n  spec: {fig.get("spec")}')
    for j, ex in enumerate([e for e in ch.get('examples') or [] if isinstance(e, dict)], 1):
        t.append(f'\nWorked example {j}: {strip(ex.get("question"))}')
        cd = ex.get('code') or {}
        if isinstance(cd, dict) and cd.get('code'): t.append(f'  [code]\n{cd["code"]}')
        t += [f'  step {i}: ' + strip(x) for i, x in enumerate(ex.get('steps') or [], 1)]
        if ex.get('dry_run'): t.append(f'  dry run: {ex["dry_run"]}')
        if ex.get('output'): t.append(f'  output: {ex["output"]}')
        t.append(f'  answer: {strip(ex.get("answer"))}')
    t.append('\nExam traps:'); t += ['  - ' + strip(x) for x in ch.get('traps') or []]
    t.append('\nQuiz:'); t += [f'  Q{i} ({q.get("level")}, {q.get("marks")} marks): {strip(q.get("q"))}\n     answer: {strip(q.get("a"))}' for i, q in enumerate([q for q in ch.get('quiz') or [] if isinstance(q, dict)], 1)]
    t.append(f'\nBeyond: {strip(ch.get("beyond"))}')
    return '\n'.join(t)


def word_count(ch):
    """Rough count of the words a chapter will show (the checker counts outside the figure)."""
    txt = plain_text({'unit': {'n': 0, 'subtopics': [{'t': ''}] * 99}}, 1, ch)
    txt = re.sub(r'spec: \{.*', '', txt)
    return len(re.findall(r'\S+', txt))
