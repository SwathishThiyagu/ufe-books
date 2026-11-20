#!/usr/bin/env python3
"""make_site.py: the two University free n easy websites, as static folders.

  find/   the video finder: search any topic of the universal syllabus, browse by department
          and subject, and reach each lesson's video and notes.                 -> one Pages project
  notes/  the notes site linked from every video: one page per LESSON with the Like step and
          the download of that lesson's notes (its chapters cut from the unit book), plus the
          full unit book.                                                        -> another Pages project

usage: make_site.py universal.json worklist.json videos.json <books root> <out root> [--logo logo.png] [--pdf-only]

  --pdf-only  (the channel's default from 3 Nov 2026) only each lesson's notes PDF, at <out root>/notes/<sid>-u<N>-L<k>.pdf (upload that folder; served at <notes site>/<lesson>.pdf),
              naming no unit or lesson number and linking no unit book, plus the descriptions; no unit books, pages or finder

  universal.json  the data pack (subjects, units, subtopics, match phrases)
  worklist.json   the data pack's work list (dept, book path per unit)
  videos.json     site addresses, playlists per subject, lessons per unit with video ids
  books root      folder holding <dept>/<sid>/<sid>-u<N>.html (03_Books on the PC)
  out root        writes <out root>/find/ and <out root>/notes/

Description link for a lesson:  <notes site>/l/<sid>-u<N>-L<k>.html
"""
import base64, html, json, os, re, shutil, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
BRAND = 'University free n easy'

# ---------- shared look (same palette as the unit books) ----------
CSS = '''
:root{--bg:#f6f7fb;--panel:#fff;--ink:#18203a;--muted:#5b6482;--line:#dde1ec;--accent:#2f3fa8;--accent-ink:#fff;--accent-soft:#e6e9fb;--go:#1f7a5a;--go-soft:#e2f4ec;--warm:#b35c00;--warm-soft:#fff1df;--ring:rgba(24,32,58,.18);--display:"Rubik","Segoe UI",system-ui,sans-serif;--body:"Nunito Sans","Segoe UI",system-ui,sans-serif;--r:16px}
*{box-sizing:border-box}[hidden]{display:none!important}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.55 var(--body)}
a{color:var(--accent)}
.top{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:12px 16px;max-width:860px;margin:0 auto}
.brand{display:inline-flex;align-items:center;gap:10px;text-decoration:none;color:var(--ink);font:700 15px/1 var(--display)}
.brand img{width:34px;height:auto;display:block}
.brand small{display:block;font:600 11px/1.2 var(--body);color:var(--muted);letter-spacing:.6px;text-transform:uppercase;margin-top:4px}
.top nav a{font:700 14px var(--body);text-decoration:none;margin-left:14px}
main{max-width:860px;margin:0 auto;padding:8px 16px 40px}
.kicker{font:700 12px/1 var(--display);letter-spacing:1.4px;color:var(--accent);margin:18px 0 10px;text-transform:uppercase}
h1{font:700 clamp(26px,5.6vw,36px)/1.15 var(--display);margin:0 0 10px;letter-spacing:-.2px}
.lede{margin:0 0 20px;color:var(--muted);font-size:17px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:var(--r);padding:18px 18px 20px;margin:0 0 16px;position:relative;box-shadow:0 1px 0 rgba(24,32,58,.04)}
.card h2{font:700 20px/1.2 var(--display);margin:0 0 8px}
.sh{display:flex;align-items:center;gap:12px;margin:0 0 8px}
.sh .n{flex:0 0 36px;width:36px;height:36px;border-radius:50%;background:var(--accent);color:var(--accent-ink);font:700 17px/36px var(--display);text-align:center}
.sh h2{margin:0}
.muted{color:var(--muted)}
.row{display:flex;flex-wrap:wrap;gap:10px;margin-top:12px}
.btn{appearance:none;border:0;border-radius:12px;padding:12px 16px;font:700 15.5px/1.1 var(--body);background:var(--accent);color:var(--accent-ink);text-decoration:none;display:inline-flex;align-items:center;gap:8px;cursor:pointer;min-height:46px}
.btn:hover{filter:brightness(1.08)}.btn:focus-visible{outline:3px solid var(--ring);outline-offset:2px}
.btn.ghost{background:var(--accent-soft);color:var(--accent)}.btn.go{background:var(--go);color:#fff}.btn.big{font-size:17px;padding:15px 20px}
.btn svg{width:20px;height:20px;flex:0 0 20px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0 0}
.chip{font:700 12px/1 var(--display);letter-spacing:.4px;text-transform:uppercase;background:var(--accent-soft);color:var(--accent);border-radius:999px;padding:7px 10px}
.chip.go{background:var(--go-soft);color:var(--go)}.chip.soon{background:var(--warm-soft);color:var(--warm)}
.tag{flex:0 0 auto;font:700 11.5px/1 var(--display);letter-spacing:.4px;text-transform:uppercase;background:var(--go-soft);color:var(--go);border-radius:999px;padding:6px 9px}
.tag.soon{background:var(--warm-soft);color:var(--warm)}
.list{list-style:none;margin:0;padding:0;border:1px solid var(--line);border-radius:12px;overflow:hidden}
.list li{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:10px 12px;border-top:1px solid var(--line);font-size:15.5px}
.list li:first-child{border-top:0}
.list a{color:var(--ink);text-decoration:none;flex:1}.list a:hover{color:var(--accent)}
.list .num{color:var(--accent);font:700 14px var(--display);margin-right:6px}
.lessons{list-style:none;margin:0;padding:0}
.lessons li{border:1px solid var(--line);border-radius:12px;margin:0 0 8px;background:var(--panel);padding:12px 14px;display:flex;flex-wrap:wrap;align-items:center;gap:8px 12px}
.lessons li .t{flex:1 1 220px}.lessons li .t b{display:block}.lessons li .t span{color:var(--muted);font-size:14.5px}
.lessons li.here{border-color:var(--accent);box-shadow:0 0 0 2px var(--accent-soft)}
.lessons li.soon{opacity:.8}
.btn.sm{padding:9px 13px;min-height:38px;font-size:14px;border-radius:10px}
h3{font:700 15px/1.2 var(--display);letter-spacing:.6px;text-transform:uppercase;color:var(--muted);margin:20px 0 8px}
footer{max-width:860px;margin:0 auto;padding:8px 16px 36px;color:var(--muted);font-size:14.5px}
footer p{margin:6px 0}
/* finder */
.search{position:relative;margin:6px 0 18px}
.search input{width:100%;font:600 18px var(--body);padding:16px 18px 16px 50px;border:2px solid var(--line2,#b9c0d4);border-radius:14px;background:#fff;color:var(--ink);outline:0}
.search input:focus{border-color:var(--accent);box-shadow:0 0 0 4px var(--accent-soft)}
.search svg{position:absolute;left:16px;top:50%;transform:translateY(-50%);width:22px;height:22px;color:var(--muted)}
.results{margin:0 0 18px}
.hit{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:12px 14px;margin:0 0 8px;display:flex;flex-wrap:wrap;align-items:center;gap:8px 12px}
.hit .t{flex:1 1 240px}.hit .t b{display:block;font-size:16px}.hit .t span{color:var(--muted);font-size:14px}
.hit mark{background:#fff1a8;color:inherit;padding:0 1px;border-radius:3px}
.empty{color:var(--muted);padding:6px 2px}
.dept{margin:0 0 14px}
.dept h2{font:700 18px/1.2 var(--display);margin:0 0 8px}
.subs{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:8px;list-style:none;margin:0;padding:0}
.subs li a{display:block;background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:11px 13px;text-decoration:none;color:var(--ink);font-size:15.5px;height:100%}
.subs li a:hover{border-color:var(--accent)}
.subs li a small{display:block;color:var(--muted);font-size:13px;margin-top:3px}
.unit{margin:0 0 18px}
.unit h2{font:700 19px/1.2 var(--display);margin:0 0 10px}
/* notes page */
.player{position:relative;width:100%;aspect-ratio:16/9;background:#0e1322;border-radius:12px;overflow:hidden;margin:14px 0}
.player img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.player iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.player .play{position:absolute;inset:0;margin:auto;width:76px;height:54px;border:0;border-radius:14px;background:rgba(24,32,58,.82);cursor:pointer;display:grid;place-items:center;box-shadow:0 6px 20px rgba(0,0,0,.35)}
.player .play:hover{background:var(--accent)}
.player .soon{position:absolute;inset:0;display:grid;place-items:center;color:#cfd5ea;font:600 16px var(--body);text-align:center;padding:20px}
.ok{display:none;align-items:center;gap:8px;color:var(--go);font-weight:700;margin-top:12px}
.done .ok{display:flex}.done #doneBtn{display:none}
.locked .body{filter:blur(5px);pointer-events:none;user-select:none;transition:filter .5s}.body{transition:filter .5s}
.lockmsg{display:none;position:absolute;inset:64px 18px auto 18px;z-index:2;justify-content:center}.locked .lockmsg{display:flex}
.lockmsg span{background:var(--ink);color:#fff;border-radius:999px;padding:10px 16px;font:700 14px/1 var(--body);display:inline-flex;align-items:center;gap:8px;box-shadow:0 8px 24px rgba(24,32,58,.25)}
.hint{font-size:15px;color:var(--muted)}
@media (prefers-reduced-motion:reduce){.body,.locked .body{transition:none}}
'''

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Rubik:wght@500;700&family=Nunito+Sans:wght@400;600;700&display=swap" rel="stylesheet">'
ICON_LIKE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 10v12"/><path d="M15 5.88 14 10h5.83a2 2 0 0 1 1.92 2.56l-2.33 8A2 2 0 0 1 17.5 22H4a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2h2.76a2 2 0 0 0 1.79-1.11L12 2a3.13 3.13 0 0 1 3 3.88Z"/></svg>'
ICON_DL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12"/><path d="m7 10 5 5 5-5"/><path d="M4 21h16"/></svg>'
ICON_PLAY = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>'
ICON_OK = '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>'
ICON_LOCK = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>'
ICON_SEARCH = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>'

E = html.escape


def read(p):
    with open(p, encoding='utf8') as f:
        return f.read()


OLD_FOOT = re.compile(r"Written with AI from (?:the )?(?:10|ten) universities")


def fix_foot(book_html):
    """Books written before 2 Nov 2026 end with "Written with AI from the 10 universities' syllabi";
    the channel's wording is "Written with top universities' syllabi" (the HTML copy and every PDF get it).
    Then every college name goes (strip_colleges)."""
    return strip_counts(strip_colleges(OLD_FOOT.sub("Written with top universities", book_html)))


# No count of syllabus universities either (the person's rule, 3 Nov 2026): the header line
# "Universal syllabus · Biochemistry · taught at 8 of 10 universities" loses its count, and the
# "Taught at 8 of 10" chip goes.
COUNT_EYEBROW = re.compile(r'\s*·\s*taught at \d+ of (?:10|ten)(?: universities)?', re.I)
COUNT_CHIP = re.compile(r'<span class="chip tier">[^<]*</span>')


def strip_counts(book_html):
    book_html = re.sub(r'(<div class="eyebrow">)(.*?)(</div>)', lambda m: m.group(1) + COUNT_EYEBROW.sub('', m.group(2)) + m.group(3), book_html, flags=re.S)
    book_html = COUNT_CHIP.sub('', book_html)
    return book_html


# The ten universities whose syllabi built the universal syllabus. No PDF, online copy or page names them
# (the person's rule, 2 Nov 2026). Science history and publishers (University of Madras for the
# Ramachandran plot, Oxford University Press) are not syllabus colleges and stay.
COLLEGE = re.compile(r"Anna Univ(?:ersity|\.)?|\bSRM(?: IST| University)?\b|\bIIT[ -]?(?:Madras|Delhi|Bombay)\b|\bIIT[MDB]\b"
                     r"|\bNIT[ -]?(?:Trichy|Tiruchirappalli|Surathkal|Karnataka|Calicut)\b|\bNIT[TKC]\b|\bManipal(?: \(MIT\)| MIT| Institute of Technology)?"
                     r"|\bMIT Manipal\b|\bChrist(?: University| \(Deemed to be University\))?\b")
SENT_SPLIT = re.compile(r'(?<=[.!?])(?:["”’)]|</(?:b|i|em|strong|a|q)>)*\s+(?=[A-Z0-9<"“(])')


def _vis(s):
    return html.unescape(re.sub(r'<[^>]+>', ' ', s))


def _balanced(frag):
    tags = re.findall(r'<(/?)([a-zA-Z][a-zA-Z0-9]*)\b[^>]*?(/?)>', frag)
    depth = {}
    for close, name, selfc in tags:
        name = name.lower()
        if selfc or name in ('br', 'img', 'hr', 'wbr', 'input'):
            continue
        depth[name] = depth.get(name, 0) + (-1 if close else 1)
        if depth[name] < 0:
            return False
    return all(v == 0 for v in depth.values())


def _drop_named_sentences(inner):
    """Drop the sentences of a block that name a college; None when nothing meaningful is left."""
    keep = []
    for p in SENT_SPLIT.split(inner):
        if not COLLEGE.search(_vis(p)):
            keep.append(p)
            continue
        # keep the clauses of the sentence that name no college ("X is the term for Y; IITB lists it by this name.")
        clauses = re.split(r';\s+', p)
        if len(clauses) > 1:
            ok = [c for c in clauses if not COLLEGE.search(_vis(c))]
            if ok and len(_vis(' '.join(ok)).split()) >= 4:
                s = '; '.join(ok).rstrip()
                end = re.search(r'[.!?]["”’)]*$', _vis(p).strip())
                if not re.search(r'[.!?]["”’)]*$', _vis(s).strip()):
                    s += end.group(0) if end else '.'
                if ok[0] is not clauses[0]:
                    s = re.sub(r'^(\s*(?:<[^>]+>\s*)*)([a-z])', lambda m: m.group(1) + m.group(2).upper(), s)
                keep.append(s)
    out = ' '.join(keep).strip()
    if not _balanced(out):
        return None
    if len(_vis(out).split()) < 3:
        return None
    return out


def strip_colleges(book_html):
    """Remove every name of the ten syllabus universities from a unit book: the crosswalk table and its
    note, the coverage squares and their legend, the 'Main course at' chip, the sources' syllabi line,
    and each sentence (or table row) elsewhere that names one. Works on books written before the rule."""
    b = book_html
    # header chip and per-chapter coverage squares, legend
    b = re.sub(r'<span class="chip main"[^>]*>.*?</span>', '', b, flags=re.S)
    b = re.sub(r'\s*<span class="cov"[^>]*>(?:<i [^>]*></i>)*</span>', '', b)
    b = re.sub(r'<div class="legend">(?:(?!</div>).)*</div>', '', b, flags=re.S)
    # the crosswalk: its heading, table and the note after it
    b = re.sub(r'<h3>[^<]*(?:your university|your college|at your uni)[^<]*</h3>\s*<div class="tablewrap">.*?</table>\s*</div>(?:\s*<p class="note">.*?</p>)?', '', b, flags=re.S | re.I)
    # the sources' syllabi line
    b = re.sub(r'Syllabi: the universal syllabus and the course documents of [^<]*?\.(?=\s|<|$)',
               'Syllabus: the University free n easy universal syllabus, built from top universities’ syllabi.', b)
    # table rows that name one
    b = re.sub(r'<tr>(?:(?!</tr>).)*</tr>', lambda m: '' if COLLEGE.search(_vis(m.group(0))) else m.group(0), b, flags=re.S)
    # notes that are about colleges go whole; other blocks lose only the sentences that name one
    def block(m):
        tag, attrs, inner = m.group(1), m.group(2) or '', m.group(3)
        if not COLLEGE.search(_vis(inner)):
            return m.group(0)
        if 'class="note"' in attrs:
            return ''
        kept = _drop_named_sentences(inner)
        if kept is None:
            return '' if tag in ('p', 'li', 'dd', 'figcaption') else m.group(0)
        return f'<{tag}{attrs}>{kept}</{tag}>'
    main_at = b.find('<main')
    head, body = b[:main_at], b[main_at:]
    for _ in range(2):   # nested blocks (a <p> inside an <li>) need a second pass
        body = re.sub(r'<(p|li|dd|figcaption|summary|h3|h4)(\s[^>]*)?>((?:(?!<\1[\s>]).)*?)</\1>', block, body, flags=re.S)
    def prereq(m):
        if not COLLEGE.search(_vis(m.group(2))):
            return m.group(0)
        kept = _drop_named_sentences(m.group(2))
        return '' if kept is None else m.group(1) + kept + '</div>'
    body = re.sub(r'(<div class="(?:prereq|note|lead)"[^>]*>)((?:(?!</?div[\s>]).)*?)</div>', prereq, body, flags=re.S)
    # anything left (a title attribute, an aria-label, a stray mention) is replaced by a neutral word
    body = re.sub(r'(title|aria-label)="[^"]*"', lambda m: (m.group(1) + '=""') if COLLEGE.search(m.group(0)) else m.group(0), body)
    body = re.sub(r'>([^<]+)<', lambda m: '>' + COLLEGE.sub('one university', m.group(1)) + '<' if COLLEGE.search(m.group(1)) else m.group(0), body)
    return head + body


def write(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf8') as f:
        f.write(s)


def shell(title, desc, body, logo, home, nav='', extra_head='', extra_css=''):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><meta name="color-scheme" content="light">
<link rel="icon" href="{logo}">{FONTS}{extra_head}
<style>{CSS}{extra_css}</style></head>
<body>
<header class="top"><a class="brand" href="{home}"><img src="{logo}" alt="" width="34" height="45"><span>{BRAND}<small>free notes · free lessons</small></span></a><nav>{nav}</nav></header>
<main>
{body}
</main>
<footer><p><b>{BRAND}</b> · free notes and video lessons for university students. No sign-up, no ads.</p><p>Spotted a slip? Say so under the video and it gets fixed in the next version.</p></footer>
</body></html>'''


# ---------- chapter / lesson helpers ----------
def chapter_range(spec):
    a, _, b = str(spec).replace('–', '-').partition('-')
    return a.strip(), (b or a).strip()


def ckey(s):
    return tuple(int(x) for x in s.split('.'))


def covers(spec, num):
    if not spec:
        return False
    a, b = chapter_range(spec)
    return ckey(a) <= ckey(num) <= ckey(b)


def lesson_for(lessons, num):
    for l in lessons:
        if covers(l.get('chapters', ''), num):
            return l
    return None


def yt(v):
    return 'https://www.youtube.com/watch?v=' + v


# ---------- the unit book's exam question bank, shared out by lesson (3 Nov 2026) ----------
_QSTOP = set('''which what when where with from that this these those their there they them then than into onto upon about after
before between each every other some such only also both more most much many very will would shall should could your give state
explain describe discuss write draw compare contrast define list name mark marks outline answer question using used uses show shows
shown example examples diagram labelled label points point chapter chapters spans links link form forms make makes made does done
have has been being here them same different main role roles type types importance significance'''.split())
_REF = re.compile(r'(?:[Ss]pans|[Cc]hapters?|[Ll]inks?(?: [Cc]hapters?)?(?: to)?)\s+((?:\d+\.\d+(?:\s*[–-]\s*\d+\.\d+)?(?:\s*,\s*(?:and\s+)?|\s+and\s+)?)+)')


def _qtoks(t):
    return [w for w in re.findall(r'[a-zα-ω][a-zα-ω0-9\-]{3,}', t.lower()) if w not in _QSTOP]


def _chapter_refs(text, n):
    """Chapter numbers a question names after 'Spans', 'Chapter(s)' or 'Links', ranges expanded; only this unit's."""
    got = set()
    for m in _REF.finditer(text):
        for a, b in re.findall(r'(\d+\.\d+)(?:\s*[–-]\s*(\d+\.\d+))?', m.group(1)):
            u, x = ckey(a)
            y = ckey(b)[1] if b else x
            if u == n:
                got.update(range(x, y + 1))
    return got


def bank_for_lessons(main, n, lessons):
    """{lesson n: [(group title, details html)]}. A question that names its chapters ('Spans Chapters 1.2 and 1.6') goes to
    every lesson holding one of them; any other goes to the one lesson whose chapters its words match best (shared words
    weighted by how rare they are across the unit's chapters). Every question of the bank lands in at least one lesson."""
    import math
    from collections import Counter
    qb = re.search(r'<section id="question-bank">(.*?)</section>', main, flags=re.S)
    if not qb:
        return {}
    chs = {int(m.group(1)): Counter(_qtoks(re.sub(r'<[^>]+>', ' ', m.group(2))))
           for m in re.finditer(r'<section class="ch" id="[^"]+" data-n="(\d+)">(.*?)</section>', main, flags=re.S)}
    if not chs:
        return {}
    df = Counter(w for c in chs.values() for w in c)
    idf = {w: math.log((len(chs) + 1) / d) for w, d in df.items()}
    span = {}
    for l in lessons:
        try:
            a, b = chapter_range(l['chapters'])
            span[l['n']] = set(range(ckey(a)[1], ckey(b)[1] + 1))
        except Exception:
            pass
    out = {k: [] for k in span}
    group = ''
    for m in re.finditer(r'<h3>(.*?)</h3>|(<details\b[^>]*>.*?</details>)', qb.group(1), flags=re.S):
        if m.group(1) is not None:
            group = re.sub(r'<[^>]+>', '', m.group(1)).strip()
            continue
        d = m.group(2)
        text = html.unescape(re.sub(r'<[^>]+>', ' ', d))
        refs = _chapter_refs(text, n)
        ks = [k for k, s in span.items() if s & refs]
        if not ks:
            q = set(_qtoks(text))
            score = {k: max((sum(idf.get(w, 0) * math.log1p(chs[c][w]) for w in q if w in chs.get(c, ())) for c in s if c in chs), default=0)
                     for k, s in span.items()}
            if score:
                ks = [max(score, key=score.get)]
        for k in ks:
            out[k].append((group, d))
    return out


def bank_section(items):
    """The lesson's share of the bank, under the book's own group headings (already HTML from the book), in book order."""
    if not items:
        return ''
    order, seen = [], {}
    for g, d in items:
        if g not in seen:
            seen[g] = []
            order.append(g)
        seen[g].append(d)
    body = ''.join((f'<h3>{g}</h3>' if g else '') + ''.join(seen[g]) for g in order)
    body = f'<div class="quiz">{body}</div>'
    return ('<section id="question-bank"><h2>Exam question bank</h2><p class="note">Long-answer exam questions on these chapters, '
            'each with an outline of the points an examiner looks for. Answer one in full on paper before you read its outline.</p>'
            + body + '</section>')



# ---------- unit references in standalone notes (18 Nov 2026) ----------
_UREF = re.compile(r"\b(Units?)\s+(\d+)((?:\s*(?:,|and|or|to|&)\s*\d+)*)('s)?")
def drop_unit_refs(html, n):
    """Standalone notes name no unit number (every college groups the units differently): a reference to another
    unit becomes "an earlier lesson" / "a later lesson" / "another lesson", relative to this unit n; a prerequisite
    "Unit 1 for layering" reads "layering (an earlier lesson)". Only visible text changes, never tags or code."""
    def word(m):
        nums = [int(x) for x in re.findall(r'\d+', m.group(2) + (m.group(3) or ''))]
        many = len(nums) > 1 or m.group(1) == 'Units'
        if all(x < n for x in nums): w = 'earlier lessons' if many else 'an earlier lesson'
        elif all(x > n for x in nums): w = 'later lessons' if many else 'a later lesson'
        else: w = 'other lessons' if many else 'another lesson'
        return w + (m.group(4) or '')
    def text(t):
        t = _UREF.sub(word, t)
        t = re.sub(r'\b(an earlier lesson|a later lesson|another lesson|earlier lessons|later lessons|other lessons) for ([^,.;:()]+)',
                   lambda m: f'{m.group(2).strip()} ({m.group(1)})', t)
        t = re.sub(r'((?:^\s*|[.!?:]\s+))(an|a|another|earlier|later|other)\b(?= (?:earlier |later )?lessons?)',
                   lambda m: m.group(1) + m.group(2)[0].upper() + m.group(2)[1:], t)
        return t
    out, pos = [], 0
    for m in re.finditer(r'<(pre|code|script|style)\b.*?</\1>|<[^>]+>', html, flags=re.S):
        out.append(text(html[pos:m.start()])); out.append(m.group(0)); pos = m.end()
    out.append(text(html[pos:]))
    return ''.join(out)

# ---------- per-lesson notes cut from the unit book ----------
def cut_lesson_notes(book_html, meta, n, lesson, lessons, unit_book_name, standalone=False):
    """A self-contained file with the lesson's chapters, their key terms and glossary entries.
    standalone (--pdf-only, the person's choice 3 Nov 2026): no unit books are published because every college groups the units
    differently, so the notes name no unit or lesson number and point to no unit book."""
    a, b = chapter_range(lesson['chapters'])
    lo, hi = ckey(a)[1], ckey(b)[1]
    mi = book_html.find('<main', max(0, book_html.find('<body')))   # the real <main> (a shell comment may contain the text "<main>")
    me = book_html.find('</main>', mi)
    head, main, tail = book_html[:mi], book_html[mi:me], book_html[me:]
    secs = re.findall(r'<section class="ch" id="[^"]+" data-n="(\d+)">.*?</section>', main, flags=re.S)
    chapters = [m.group(0) for m in re.finditer(r'<section class="ch" id="[^"]+" data-n="(\d+)">.*?</section>', main, flags=re.S) if lo <= int(m.group(1)) <= hi]
    if not chapters:
        return None
    text = re.sub(r'<[^>]+>', ' ', ' '.join(chapters)).lower()
    # key terms: the summary table rows whose chapter column falls in the lesson
    rows = []
    sm = re.search(r'<section id="summary">.*?</section>', main, flags=re.S)
    if sm:
        for tr in re.findall(r'<tr>.*?</tr>', sm.group(0), flags=re.S):
            tds = re.findall(r'<td[^>]*>(.*?)</td>', tr, flags=re.S)
            if len(tds) >= 3:
                nums = re.findall(r'\d+\.\d+', re.sub(r'<[^>]+>', '', tds[-1]))
                if any(lo <= ckey(x)[1] <= hi and ckey(x)[0] == n for x in nums):
                    rows.append(tr)
    # glossary: the terms that occur in these chapters
    gl = []
    gm = re.search(r'<section id="glossary">.*?</section>', main, flags=re.S)
    if gm:
        for dt, dd in re.findall(r'<dt>(.*?)</dt>\s*<dd>(.*?)</dd>', gm.group(0), flags=re.S):
            term = re.sub(r'<[^>]+>', '', dt).strip().lower()
            if term and term in text:
                gl.append(f'<dt>{dt}</dt><dd>{dd}</dd>')
    src = re.search(r'<section id="sources">.*?</section>', main, flags=re.S)
    k = lesson['n']
    title = lesson.get('title', f'Lesson {k}')
    span = f'chapter {a}' if a == b else f'chapters {a} to {b}'
    # head: retitle
    if standalone:
        head = re.sub(r'<title>.*?</title>', f"<title>{E(meta['subject'])} notes: {E(title)} · {BRAND}</title>", head, count=1, flags=re.S)
        head = re.sub(r'(<span class="crumb">)(.*?)(</span>)', lambda m: m.group(1) + re.sub(r'\s*·\s*Unit \d+ of \d+', '', m.group(2)) + ' · Lesson notes' + m.group(3), head, count=1)
        head = re.sub(r'<h1>(.*?)<small>.*?</small></h1>', lambda m: f'<h1>{m.group(1)}<small>{E(title)}</small></h1>', head, count=1, flags=re.S)
        head = re.sub(r'<p class="lead">.*?</p>', f'<p class="lead">The notes for the lesson &ldquo;{E(title)}&rdquo;: {span}, with their figures, worked examples, exam traps, quizzes and exam question bank, in one file.</p>', head, count=1, flags=re.S)
        head = re.sub(r'<div class="chips">.*?</div>', f'<div class="chips"><span class="chip">{len(chapters)} chapter{"s" if len(chapters) != 1 else ""}</span><span class="chip">{span.capitalize()}</span></div>', head, count=1, flags=re.S)
        head = head.replace('<div class="h">In this unit</div>', '<div class="h">In these notes</div>')
        about = f'<section id="about"><h2>About these notes</h2><p>These are the notes for the {BRAND} video lesson <b>{E(title)}</b> on {E(meta["subject"])}: {span}, with every figure, worked example, exam trap and quiz, and the long-answer exam questions on these chapters.</p></section>'
        body = '<main id="main">' + about + drop_unit_refs(''.join(chapters), n)
        if rows:
            body += '<section id="summary"><h2>Key terms of this lesson</h2><div class="keybox"><div class="tablewrap"><table><thead><tr><th>Term</th><th>Meaning or formula</th><th>Chapter</th></tr></thead><tbody>' + ''.join(rows) + '</tbody></table></div></div></section>'
        # the unit book's long-answer questions on these chapters (3 Nov 2026: the lesson says "with the question bank")
        body += drop_unit_refs(bank_section(bank_for_lessons(main, n, lessons).get(k, [])), n)
        if gl:
            body += '<section id="glossary"><h2>Glossary (terms used in this lesson)</h2><dl class="gloss">' + ''.join(gl) + '</dl></section>'
        if src:
            body += src.group(0)
        return head + body + tail
    head = re.sub(r'<title>.*?</title>', f"<title>{E(meta['subject'])} · Unit {n} · Lesson {k} notes: {E(title)} · {BRAND}</title>", head, count=1, flags=re.S)
    head = re.sub(r'(<span class="crumb">)(.*?)(</span>)', lambda m: m.group(1) + m.group(2).replace(f'Unit {n} of', f'Unit {n} · Lesson {k} notes · of') + m.group(3), head, count=1)
    head = re.sub(r'<h1>(.*?)<small>.*?</small></h1>', lambda m: f'<h1>{m.group(1)}<small>Unit {n} · Lesson {k} · {E(title)}</small></h1>', head, count=1, flags=re.S)
    head = re.sub(r'<p class="lead">.*?</p>', f'<p class="lead">The notes for Lesson {k} of Unit {n}: {span} of the unit book, with their figures, worked examples, exam traps and quizzes, in one file. The full unit book, with every chapter, the exam question bank and the glossary, is linked at the end.</p>', head, count=1, flags=re.S)
    head = re.sub(r'<div class="chips">.*?</div>', f'<div class="chips"><span class="chip">Lesson {k} of {len(lessons)}</span><span class="chip">{len(chapters)} chapter{"s" if len(chapters) != 1 else ""}</span><span class="chip">{span.capitalize()}</span></div>', head, count=1, flags=re.S)
    head = head.replace('<div class="h">In this unit</div>', '<div class="h">In this lesson</div>')
    about = f'<section id="about"><h2>About these notes</h2><p>These are the notes for <b>Lesson {k} · {E(title)}</b> of the {BRAND} video lessons on {E(meta["subject"])} Unit {n}, {E(meta["unit_name"])}. They are {span} of the unit book, unchanged, so a page here is the same page in the full book.</p></section>'
    body = '<main id="main">' + about + ''.join(chapters)
    if rows:
        body += '<section id="summary"><h2>Key terms of this lesson</h2><div class="keybox"><div class="tablewrap"><table><thead><tr><th>Term</th><th>Meaning or formula</th><th>Chapter</th></tr></thead><tbody>' + ''.join(rows) + '</tbody></table></div></div></section>'
    if gl:
        body += '<section id="glossary"><h2>Glossary (terms used in this lesson)</h2><dl class="gloss">' + ''.join(gl) + '</dl></section>'
    body += f'<section id="full"><h2>The full unit book</h2><p>Every chapter of Unit {n}, the unit summary, the exam question bank with model answers and the full glossary: <a href="{E(unit_book_name)}">{E(meta["subject"])} · Unit {n} · {E(meta["unit_name"])}</a> (one file, works offline).</p></section>'
    if src:
        body += src.group(0)
    return head + body + tail


# ---------- PDF export (Chromium print) ----------
PRINT_CSS = 'header.top,nav.toc,.read,.btn,.prog,.toast{display:none!important}body{padding:0;font-size:11.5pt;background:#fff}.wrap{display:block}main{max-width:none}.hero{padding-top:0}.quiz details,figure.fig,.example,.traps,.beyond,.keybox,.prereq{break-inside:avoid}h2,h3,h4{break-after:avoid}figure.fig svg{max-width:100%;height:auto}'


def export_pdfs(todo, cfg):
    """todo: [(html path, footer label, video url)] -> {pdf path: KB}. A4, the channel and the video link in the footer of every page."""
    sizes = {}
    try:
        from playwright.sync_api import sync_playwright
    except Exception as e:
        print('  pdf: playwright not available, skipping (', e, ')')
        return sizes
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page()
        for fp, label, link in todo:
            pg.goto('file://' + os.path.abspath(fp))
            pg.add_style_tag(content=PRINT_CSS)
            pg.evaluate("document.querySelectorAll('details').forEach(d=>d.open=true)")
            pg.wait_for_timeout(150)
            out = fp[:-5] + '.pdf'
            foot = f'<div style="width:100%;font-family:Segoe UI,Arial,sans-serif;font-size:8.5px;color:#5b6482;padding:0 12mm;display:flex;justify-content:space-between"><span>{E(label)}' + (f' · {E(link)}' if link else '') + '</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>'
            pg.pdf(path=out, format='A4', print_background=True, margin={'top': '14mm', 'bottom': '16mm', 'left': '13mm', 'right': '13mm'},
                   display_header_footer=True, header_template='<div></div>', footer_template=foot, prefer_css_page_size=False)
            sizes[out] = max(1, round(os.path.getsize(out) / 1024))
            sizes[fp[:-5] + '.pdf'] = sizes[out]
        b.close()
    return sizes


# ---------- the notes site ----------
def notes_lesson_page(meta, n, lesson, lessons, chapters, kb, unit_kb, playlist, cfg, logo):
    sid = meta['sid']
    k = lesson['n']
    key = f'{sid}-u{n}-L{k}'
    title = lesson.get('title', f'Lesson {k}')
    v = lesson.get('video', '')
    a, b = chapter_range(lesson['chapters'])
    span = f'chapter {a}' if a == b else f'chapters {a}–{b}'
    kicker = f"{meta['subject']} · Unit {n} · Lesson {k}"
    ch_rows = ''.join(f'<li><a href="../files/{key}.html#{E(cid)}"><span class="num">{E(num)}</span> {E(t)}</a></li>' for num, t, cid in chapters if covers(lesson['chapters'], num))
    others = ''
    for l in lessons:
        lk = f"{sid}-u{n}-L{l['n']}"
        here = 'here' if l['n'] == k else ''
        soon = '' if l.get('video') else 'soon'
        btns = (f'<a class="btn sm" href="{yt(l["video"])}" target="_blank" rel="noopener">{ICON_PLAY}Watch</a>' if l.get('video') else '<span class="tag soon">video coming</span>')
        btns += f' <a class="btn sm ghost" href="{lk}.html">Notes</a>'
        others += f'<li class="{here} {soon}"><div class="t"><b>Lesson {l["n"]} · {E(l.get("title", ""))}</b><span>Chapters {E(str(l.get("chapters", "")))}' + (f' · {l["minutes"]} min' if l.get('minutes') else '') + f'</span></div>{btns}</li>'
    pl_btn = f'<a class="btn ghost" href="https://www.youtube.com/playlist?list={E(playlist)}" target="_blank" rel="noopener">{E(meta["subject"])} playlist · every lesson in order</a>' if playlist else ''
    find = cfg.get('find', '') or '../index.html'
    ch_id = cfg.get('channel', '')
    sub_btn = f'<div class="sub"><div class="g-ytsubscribe" data-channelid="{E(ch_id)}" data-layout="full" data-count="default"></div></div>' if ch_id else ''
    sub_head = '<script src="https://apis.google.com/js/platform.js" async defer></script>' if ch_id else ''
    body = f'''
<p class="kicker">{E(kicker)}</p>
<h1>{E(title)}</h1>
<p class="lede">The notes for this lesson: {span} of the unit book, with the figures, worked example, exam traps and quiz, in one PDF.</p>
<section class="card" id="s1">
  <div class="sh"><span class="n">1</span><h2>Liked the lesson? Tell YouTube</h2></div>
  <p id="likeText">A like costs nothing and tells YouTube to show this lesson to more students. Subscribing brings you the next lesson of this subject.</p>
  <div class="player" id="player"></div>
  <div class="row">
    <a class="btn ghost" id="likeBtn" target="_blank" rel="noopener" hidden>{ICON_LIKE}Like on YouTube</a>
    {sub_btn}
  </div>
</section>
<section class="card" id="s2">
  <div class="sh"><span class="n">2</span><h2>Your notes</h2></div>
  <div class="row" style="margin-top:4px">
    <a class="btn go big" id="dlBtn" href="../files/{key}.pdf" download>{ICON_DL}Download Lesson {k} notes (PDF)</a>
    <a class="btn ghost" href="../files/{key}.html" target="_blank" rel="noopener">Read online</a>
  </div>
  <p class="hint">About {kb} KB. Opens in any PDF reader and works offline; the online copy has the same pages.</p>
  <h3>In these notes</h3>
  <ol class="list">{ch_rows}</ol>
  <h3>The whole unit</h3>
  <div class="row" style="margin-top:4px"><a class="btn ghost" href="../files/{sid}-u{n}.pdf" download>{ICON_DL}Full Unit {n} book (PDF, {unit_kb} KB)</a><a class="btn ghost" href="../files/{sid}-u{n}.html" target="_blank" rel="noopener">Read the unit online</a></div>
  <p class="hint">All {len(chapters)} chapters, the unit summary, the exam question bank with model answers, and the glossary.</p>
</section>
<section class="card" id="s3">
  <div class="sh"><span class="n">3</span><h2>Keep going</h2></div>
  <p class="muted" style="margin-top:0">The lessons of this unit, the subject playlist, and the finder for any other topic.</p>
  <ul class="lessons" id="lessonList">{others}</ul>
  <div class="row">{pl_btn}<a class="btn ghost" href="{E(find)}">Find another lesson</a></div>
</section>
<script>
(function(){{
  var V={json.dumps(v)};
  var player=document.getElementById('player'), likeBtn=document.getElementById('likeBtn');
  if(V){{
    var img=document.createElement('img'); img.src='https://i.ytimg.com/vi/'+V+'/hqdefault.jpg'; img.alt=''; img.onerror=function(){{img.remove()}};
    var play=document.createElement('button'); play.className='play'; play.type='button'; play.setAttribute('aria-label','Play the video');
    play.innerHTML='<svg viewBox="0 0 24 24" width="26" height="26" fill="#fff"><path d="M8 5v14l11-7z"/></svg>';
    play.onclick=function(){{ var f=document.createElement('iframe'); f.src='https://www.youtube-nocookie.com/embed/'+V+'?autoplay=1&rel=0';
      f.allow='accelerometer; autoplay; encrypted-media; picture-in-picture'; f.allowFullscreen=true; f.title='Lesson video'; player.replaceChildren(f); }};
    player.replaceChildren(img,play); likeBtn.href='https://www.youtube.com/watch?v='+V; likeBtn.hidden=false;
  }}else{{
    var soon=document.createElement('div'); soon.className='soon'; soon.textContent='The video for this lesson is on its way. The notes are already here.';
    player.replaceChildren(soon);
    document.getElementById('likeText').textContent='When the video is up, a like there helps more students find it. The notes are below.';
  }}
}})();
</script>'''
    return shell(f"{meta['subject']} Unit {n} Lesson {k} notes · {title} · {BRAND}",
                 f"Notes for the {BRAND} lesson '{title}' ({meta['subject']} Unit {n}, {span}): the chapters, worked example, traps and quiz as a PDF.",
                 body, logo, '../index.html', nav=f'<a href="{E(find)}">Find a lesson</a>', extra_head=sub_head, extra_css='.sub{display:flex;align-items:center;min-height:46px}')


def description_text(meta, n, lesson, lessons, playlist, cfg, pdf_only=False):
    k = lesson['n']
    key = f"{meta['sid']}-u{n}-L{k}"
    notes = cfg.get('notes', '') or 'https://<notes site>'
    find = cfg.get('find', '') or 'https://<finder site>'
    a, b = chapter_range(lesson['chapters'])
    span = f'chapter {a}' if a == b else f'chapters {a} to {b}'
    if pdf_only:
        lines = [f"📘 {lesson.get('title', '')}: {meta['subject']}, explained in one animated lesson.", '',
                 '📥 FREE NOTES',   # the person's layout (3 Nov 2026): a heading, then the Like step, then the PDF link in step 2
                 '👍 Step 1: if this helped, tap Like. Helps us keep making free n easy lessons for every subject.',
                 f'📄 Step 2: download the free notes PDF: {notes}/{key}.pdf',
                 '✅ Every figure, worked example, exam trap, quiz and exam question of this lesson, in one file.']
        if playlist:
            lines.append(f"▶️ {meta['subject']} playlist, every lesson in order: https://www.youtube.com/playlist?list={playlist}")
        lines += ['', '🎓 Free notes, free lessons, no sign-up. Built for university students from top universities\' syllabi and standard textbooks.',
                  '💬 Spotted a mistake? Tell us in the comments and it gets fixed in the next version.']
        return '\n'.join(lines) + '\n'
    lines = [
        f"{lesson.get('title', '')} — {meta['subject']}, Unit {n} ({meta['unit_name']}), Lesson {k} of {len(lessons)}: {span} of the unit book.",
        '',
        f'Notes for this lesson (PDF): {notes}/files/{key}.pdf',
        'Step 1 — if this helped, tap Like: it tells YouTube to show the lesson to more students.',
        f'Step 2 — download the notes above. Full unit book and all lessons: {notes}/l/{key}.html',
    ]
    if playlist:
        lines.append(f"{meta['subject']} playlist, every lesson in order: https://www.youtube.com/playlist?list={playlist}")
    lines += ['', f'Find any topic of your syllabus: {find}', '', 'Free notes, free lessons, no sign-up. Built for university students from top universities\' syllabi and standard textbooks; report mistakes in the comments and they get fixed in the next version.']
    return '\n'.join(lines) + '\n'


def notes_index(units_built, logo, cfg):
    by = {}
    for u in units_built:
        by.setdefault(u['subject'], []).append(u)
    secs = []
    for subj in sorted(by):
        items = ''
        for u in sorted(by[subj], key=lambda x: x['n']):
            ls = ''.join(f'<li><a href="l/{u["sid"]}-u{u["n"]}-L{l["n"]}.html"><span class="num">L{l["n"]}</span> {E(l.get("title", ""))}</a>' + ('' if l.get('video') else '<span class="tag soon">video coming</span>') + '</li>' for l in u['lessons'])
            items += f'<div class="unit"><h2>Unit {u["n"]} · {E(u["unit_name"])}</h2><ol class="list">{ls}<li><a href="files/{u["sid"]}-u{u["n"]}.pdf"><span class="num">Book</span> The full unit book (PDF)</a><a href="files/{u["sid"]}-u{u["n"]}.html" style="flex:0" class="tag">online</a></li></ol></div>'
        secs.append(f'<section class="card"><h2 style="font-size:22px">{E(subj)}</h2>{items}</section>')
    find = cfg.get('find', '')
    body = f'''<p class="kicker">Notes</p><h1>Notes for every video lesson</h1>
<p class="lede">Each lesson has its own notes: the chapters it teaches, cut from the unit book, as one PDF that works offline. Open a lesson and download.</p>
{''.join(secs)}
<p class="muted">Looking for a topic? <a href="{E(find) or "#"}">Search the finder</a>.</p>'''
    return shell(f'{BRAND} · notes', f'{BRAND}: the notes for every video lesson, one file per lesson, free.', body, logo, 'index.html', nav=f'<a href="{E(find) or "#"}">Find a lesson</a>')


# ---------- the finder ----------
def finder_index(U, subjects, stats, logo, cfg):
    dnames = U.get('departments', {})
    by = {}
    for s in subjects:
        by.setdefault(s['dept'], []).append(s)
    order = ['common'] + [d for d in dnames if d != 'common']
    secs = []
    for d in order:
        if d not in by:
            continue
        items = ''
        for s in sorted(by[d], key=lambda x: (x.get('usual_sem') or 99, x['name'])):
            st = stats.get(s['id'], {})
            sub = f"Sem {s['usual_sem']} · " if s.get('usual_sem') else ''
            sub += f"{len(s['units'])} units"
            if st.get('videos'):
                sub += f" · {st['videos']} video{'s' if st['videos'] != 1 else ''}"
            elif st.get('books'):
                sub += f" · notes ready"
            items += f'<li><a href="s/{E(s["id"])}.html">{E(s["name"])}<small>{E(sub)}</small></a></li>'
        secs.append(f'<section class="dept"><h2>{E(dnames.get(d, d))}</h2><ul class="subs">{items}</ul></section>')
    body = f'''<p class="kicker">Find your lesson</p>
<h1>Type the topic as your syllabus says it</h1>
<p class="lede">Every B.Tech subject, unit by unit. A result shows the lesson video when it is up and the notes to download.</p>
<div class="search">{ICON_SEARCH}<input id="q" type="search" placeholder="e.g. GPCR, Laplace transform, binary search tree…" autocomplete="off" autofocus></div>
<div class="results" id="results"></div>
<h3>Browse by department</h3>
{''.join(secs)}
<script>
(function(){{
  var NOTES={json.dumps(cfg.get('notes', ''))};
  var q=document.getElementById('q'), out=document.getElementById('results'), IDX=null, loading=false;
  function load(cb){{ if(IDX)return cb(); if(loading)return; loading=true;
    fetch('search.json').then(function(r){{return r.json()}}).then(function(j){{IDX=j; loading=false; cb()}}).catch(function(){{loading=false; out.innerHTML='<p class="empty">The search index did not load. Browse by department below.</p>'}}) }}
  function esc(s){{return s.replace(/[&<>"]/g,function(c){{return{{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c]}})}}
  function hi(s,toks){{ var e=esc(s); toks.forEach(function(t){{ if(t.length<2)return; e=e.replace(new RegExp('('+t.replace(/[.*+?^${{}}()|[\\]\\\\]/g,'\\\\$&')+')','ig'),'<mark>$1</mark>') }}); return e }}
  function run(){{ var s=q.value.trim().toLowerCase(); if(s.length<2){{out.innerHTML='';return}}
    load(function(){{ var toks=s.split(/[^a-z0-9+#.]+/).filter(Boolean), S=IDX.subjects, hits=[];
      IDX.items.forEach(function(it){{ // [sid, unit, num, title, matchstr, lesson, video]
        var title=it[3].toLowerCase(), m=it[4], subj=S[it[0]], un=subj.u[it[1]].toLowerCase(), sn=subj.n.toLowerCase(), sc=0, found=0;
        toks.forEach(function(t){{ var f=false; if(title.indexOf(t)>=0){{sc+=3;f=true}} else if(m.indexOf(t)>=0){{sc+=2;f=true}} if(sn.indexOf(t)>=0||subj.a.indexOf(t)>=0){{sc+=1;f=true}} if(un.indexOf(t)>=0){{sc+=1.5;f=true}} if(f)found++ }});
        if(title.indexOf(s)>=0)sc+=4; else if(m.indexOf(s)>=0||un.indexOf(s)>=0)sc+=3;
        if(toks.length>1&&found<toks.length)sc*=0.35;
        if(sc>0)hits.push([sc+(it[5]?0.4:0)+(it[6]?0.6:0),it]) }});
      hits.sort(function(a,b){{return b[0]-a[0]}}); hits=hits.slice(0,30);
      if(!hits.length){{out.innerHTML='<p class="empty">Nothing matched. Try another word from the syllabus line, or browse below.</p>';return}}
      out.innerHTML=hits.map(function(h){{ var it=h[1], subj=S[it[0]], key=it[0]+'-u'+it[1];
        var b=''; if(it[6])b+='<a class="btn sm" href="https://www.youtube.com/watch?v='+it[6]+'" target="_blank" rel="noopener">'+{json.dumps(ICON_PLAY)}+'Watch lesson '+it[5]+'</a>';
        else if(it[5])b+='<span class="tag soon">video coming</span>';
        if(it[5]&&NOTES)b+=' <a class="btn sm ghost" href="'+NOTES+'/l/'+key+'-L'+it[5]+'.html">Notes</a>';
        else if(it[5])b+=' <a class="btn sm ghost" href="s/'+it[0]+'.html">Unit</a>';
        else b+='<a class="btn sm ghost" href="s/'+it[0]+'.html#u'+it[1]+'">See the unit</a>';
        return '<div class="hit"><div class="t"><b>'+it[2]+' '+hi(it[3],toks)+'</b><span>'+esc(subj.n)+' · Unit '+it[1]+' · '+esc(subj.u[it[1]])+'</span></div>'+b+'</div>' }}).join('') }}) }}
  var t; q.addEventListener('input',function(){{clearTimeout(t); t=setTimeout(run,120)}}); q.addEventListener('focus',function(){{load(function(){{}})}});
  if(q.value)run();
}})();
</script>'''
    return shell(f'{BRAND} · find your lesson', f'{BRAND}: search any topic of the B.Tech syllabus and reach its free video lesson and notes.', body, logo, 'index.html',
                 nav=(f'<a href="{E(cfg.get("notes", ""))}">Notes</a>' if cfg.get('notes') else ''))


def finder_subject(s, vids, playlists, books, logo, cfg, dnames):
    sid = s['id']
    notes = cfg.get('notes', '')
    units = ''
    for u in s['units']:
        n = u['n']
        key = f'{sid}-u{n}'
        lessons = vids.get(key, {}).get('lessons', [])
        has_book = key in books
        ls = ''
        for l in lessons:
            v = l.get('video', '')
            btns = (f'<a class="btn sm" href="{yt(v)}" target="_blank" rel="noopener">{ICON_PLAY}Watch</a>' if v else '<span class="tag soon">video coming</span>')
            if notes:
                btns += f' <a class="btn sm ghost" href="{E(notes)}/l/{key}-L{l["n"]}.html">Notes</a>'
            ls += f'<li class="{"" if v else "soon"}"><div class="t"><b>Lesson {l["n"]} · {E(l.get("title", ""))}</b><span>Chapters {E(str(l.get("chapters", "")))}' + (f' · {l["minutes"]} min' if l.get('minutes') else '') + f'</span></div>{btns}</li>'
        chs = ''
        for i, st in enumerate(u['subtopics'], 1):
            num = f'{n}.{i}'
            l = lesson_for(lessons, num)
            tag = f'<span class="tag">Lesson {l["n"]}</span>' if l else '<span class="tag soon">coming</span>'
            chs += f'<li><span style="flex:1"><span class="num">{num}</span> {E(st["t"])}</span>{tag}</li>'
        book_line = (f'<p class="hint">The unit book is ready' + (f' (<a href="{E(notes)}/files/{key}.html">read it</a>)' if notes else '') + '.</p>') if has_book else ''
        units += f'<section class="card unit" id="u{n}"><h2>Unit {n} · {E(u["name"])}</h2>' + (f'<ul class="lessons">{ls}</ul>' if ls else '<p class="hint">Lessons for this unit are coming.</p>') + f'<h3>Chapters</h3><ol class="list">{chs}</ol>{book_line}</section>'
    aka = ', '.join(s.get('aka', [])[:4])
    pl = playlists.get(sid, '')
    chips = (f'<span class="chip">Usually sem {s["usual_sem"]}</span>' if s.get('usual_sem') else '') + f'<span class="chip">{len(s["units"])} units</span>'
    nvid = sum(1 for u in s['units'] for l in vids.get(f'{sid}-u{u["n"]}', {}).get('lessons', []) if l.get('video'))
    chips += f'<span class="chip go">{nvid} video{"s" if nvid != 1 else ""} up</span>' if nvid else '<span class="chip soon">videos coming</span>'
    body = f'''<p class="kicker">{E(dnames.get(s['dept'], s['dept']))}</p>
<h1>{E(s['name'])}</h1>
{f'<p class="lede">Also called: {E(aka)}.</p>' if aka else ''}
<div class="chips">{chips}</div>
<div class="row">{f'<a class="btn ghost" href="https://www.youtube.com/playlist?list={E(pl)}" target="_blank" rel="noopener">{E(s["name"])} playlist · every lesson in order</a>' if pl else ''}<a class="btn ghost" href="../index.html">Search another topic</a></div>
<div style="height:14px"></div>
{units}'''
    return shell(f"{s['name']} · {BRAND}", f"{BRAND} video lessons and notes for {s['name']}: every unit and chapter of the B.Tech syllabus.", body, logo, '../index.html',
                 nav=(f'<a href="{E(notes)}">Notes</a>' if notes else ''))


# ---------- main ----------
def main(argv):
    if len(argv) < 5:
        print(__doc__)
        sys.exit(2)
    universal, worklist, videos, books_root, out = argv[:5]
    no_pdf = '--no-pdf' in argv
    pdf_only = '--pdf-only' in argv   # only the lesson notes PDFs (out/notes/files/<lesson>.pdf) and the descriptions: no unit books, no pages, no finder
    logo_p = argv[argv.index('--logo') + 1] if '--logo' in argv else os.path.join(ROOT, 'assets', 'logo.png')
    with open(logo_p, 'rb') as f:
        logo = 'data:image/png;base64,' + base64.b64encode(f.read()).decode()
    U = json.load(open(universal, encoding='utf8'))
    wl = json.load(open(worklist, encoding='utf8'))['books']
    meta = {f"{b['sid']}-u{b['unit']}": b for b in wl}
    vids = json.load(open(videos, encoding='utf8'))
    cfg = vids.get('site', {}) if isinstance(vids.get('site'), dict) else {}
    playlists = vids.get('playlists', {})
    subjects = [s for s in U['subjects'] if s.get('scope') == 'btech']
    dnames = U.get('departments', {})

    # which unit books exist
    books = {}
    for k, m in meta.items():
        p = os.path.join(books_root, m['dept'], m['sid'], f'{k}.html')
        if os.path.exists(p):
            books[k] = p

    # ---- notes site ----
    NOTES = os.path.join(out, 'notes')
    units_built = []
    for key, v in vids.items():
        if key.startswith('_') or key in ('site', 'playlists') or key not in meta:
            continue
        m = meta[key]
        if key not in books:
            print(f'  notes: skip {key}, no unit book')
            continue
        book = fix_foot(read(books[key]))
        chapters = [(mm.group(2), re.sub(r'<[^>]+>', '', mm.group(3)).strip(), mm.group(1)) for mm in re.finditer(r'<section class="ch" id="([^"]+)"[^>]*>\s*<h2>\s*<span class="num">([\d.]+)</span>\s*(.*?)</h2>', book, flags=re.S)]
        lessons = v.get('lessons', [])
        n = m['unit']
        if pdf_only:
            WORK = os.path.join(out, '_work')
            todo = []
            for l in lessons:
                cut = cut_lesson_notes(book, m, n, l, lessons, '', standalone=True)
                if not cut:
                    print(f'  notes: {key} L{l["n"]} covers no chapter ({l.get("chapters")})')
                    continue
                fp = os.path.join(WORK, f'{key}-L{l["n"]}.html')
                write(fp, cut)
                todo.append((fp, f"{BRAND} · {m['subject']} · {l.get('title', '')}", yt(l['video']) if l.get('video') else ''))
            sizes = export_pdfs(todo, cfg) if not no_pdf else {}
            for fp, _, _ in todo:
                pdf = fp[:-5] + '.pdf'
                if os.path.exists(pdf):   # flat: the upload folder holds only the PDFs, served at <notes site>/<lesson>.pdf
                    os.makedirs(NOTES, exist_ok=True)
                    os.replace(pdf, os.path.join(NOTES, os.path.basename(pdf)))
            for l in lessons:
                write(os.path.join(out, 'descriptions', f'{key}-L{l["n"]}.txt'), description_text(m, n, l, lessons, playlists.get(m['sid'], ''), cfg, pdf_only=True))
            print(f'  notes: {key}: {len(todo)} lesson PDF(s)')
            continue
        write(os.path.join(NOTES, 'files', f'{key}.html'), book)
        todo = [(os.path.join(NOTES, 'files', f'{key}.html'), f"{BRAND} · {m['subject']} · Unit {n} · {m['unit_name']}", '')]
        for l in lessons:
            cut = cut_lesson_notes(book, m, n, l, lessons, f'{key}.html')
            if not cut:
                print(f'  notes: {key} L{l["n"]} covers no chapter ({l.get("chapters")})')
                continue
            fp = os.path.join(NOTES, 'files', f'{key}-L{l["n"]}.html')
            write(fp, cut)
            todo.append((fp, f"{BRAND} · {m['subject']} · Unit {n} · Lesson {l['n']} · {l.get('title', '')}", yt(l['video']) if l.get('video') else ''))
        sizes = export_pdfs(todo, cfg) if not no_pdf else {}
        unit_kb = sizes.get(os.path.join(NOTES, 'files', f'{key}.pdf'), 0)
        for l in lessons:
            fp = os.path.join(NOTES, 'files', f'{key}-L{l["n"]}.html')
            if not os.path.exists(fp):
                continue
            kb = sizes.get(fp[:-5] + '.pdf', 0)
            write(os.path.join(NOTES, 'l', f'{key}-L{l["n"]}.html'), notes_lesson_page(m, n, l, lessons, chapters, kb, unit_kb, playlists.get(m['sid'], ''), cfg, logo))
            write(os.path.join(out, 'descriptions', f'{key}-L{l["n"]}.txt'), description_text(m, n, l, lessons, playlists.get(m['sid'], ''), cfg))
        units_built.append({'sid': m['sid'], 'subject': m['subject'], 'n': n, 'unit_name': m['unit_name'], 'lessons': lessons})
        print(f'  notes: {key}: {len(lessons)} lesson page(s), book PDF {unit_kb} KB')
    if pdf_only:
        shutil.rmtree(os.path.join(out, '_work'), ignore_errors=True)
        return
    write(os.path.join(NOTES, 'index.html'), notes_index(units_built, logo, cfg))

    # ---- finder ----
    FIND = os.path.join(out, 'find')
    items, S, stats = [], {}, {}
    for s in subjects:
        S[s['id']] = {'n': s['name'], 'u': {u['n']: u['name'] for u in s['units']}, 'a': ' | '.join(a.lower() for a in s.get('aka', []))}
        st = stats.setdefault(s['id'], {'videos': 0, 'books': 0})
        for u in s['units']:
            key = f"{s['id']}-u{u['n']}"
            lessons = vids.get(key, {}).get('lessons', [])
            st['videos'] += sum(1 for l in lessons if l.get('video'))
            st['books'] += 1 if key in books else 0
            for i, sub in enumerate(u['subtopics'], 1):
                num = f"{u['n']}.{i}"
                l = lesson_for(lessons, num)
                mstr = ' | '.join(x.lower() for x in sub.get('match', []) if x.lower() not in sub['t'].lower())
                items.append([s['id'], u['n'], num, sub['t'], mstr, l['n'] if l else 0, (l.get('video', '') if l else '')])
        write(os.path.join(FIND, 's', f"{s['id']}.html"), finder_subject(s, vids, playlists, books, logo, cfg, dnames))
    write(os.path.join(FIND, 'search.json'), json.dumps({'subjects': S, 'items': items}, ensure_ascii=False, separators=(',', ':')))
    write(os.path.join(FIND, 'index.html'), finder_index(U, subjects, stats, logo, cfg))
    print(f'  find: {len(subjects)} subject pages, {len(items)} searchable chapters, index {os.path.getsize(os.path.join(FIND, "search.json")) // 1024} KB')


if __name__ == '__main__':
    main(sys.argv[1:])
