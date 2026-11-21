#!/usr/bin/env python3
"""make_subject.py: assemble one subject's upload folder for the University free n easy channel.

  python3 make_subject.py <sid> --lessons <dir> --notes <dir> --thumbs <dir> --out <root>
        [--universal universal.json] [--videos videos.json] [--thumb t14] [--publish 19:05 --every 5] [--degree B.Tech]

Builds <root>/<degree>/<Dept>/<Subject>/ :
    html/        the final lesson pages        <sid>-u<N>-L<k>_<slug>.html   (plain names only, no _vN)
    pdf/         each lesson's notes PDF       <sid>-u<N>-L<k>.pdf  and each unit book PDF <sid>-u<N>.pdf
    thumbnail/   three thumbnails per lesson   <sid>-u<N>-L<k>_t11.jpg / _t14.jpg / _t15.jpg
    upload_sheet.html   one card per video: title, description (with chapters), tags, key moments, length,
                        thumbnail, schedule, each with a Copy button; ticks for videos already uploaded
    upload_sheet.json   the same data, for tools
and checks everything: every lesson has its page, notes PDF (more than one page) and three thumbnails; titles at
most 100 characters, descriptions at most 5000, tags at most 500; chapters start at 0:00, at least three, at least
10 s apart; no college or university name anywhere in the sheet. It prints OK or the problems.

Lesson data (title, parts, scene times, worked examples, exam traps, exam questions) is read from the built
lesson pages themselves, so the sheet always matches the video recorded from them.
"""
import glob, html, json, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEPT_FOLDER = {'bio': 'Biotech', 'cse': 'CSE', 'ece': 'ECE', 'eee': 'EEE', 'eie': 'EIE', 'mech': 'Mechanical', 'mctr': 'Mechatronics',
               'auto': 'Automobile', 'aero': 'Aerospace', 'civil': 'Civil', 'chem': 'Chemical', 'bme': 'Biomedical', 'nano': 'Nanotech', 'common': 'Common'}
UNIS = ['anna', 'srm', 'iitm', 'iitb', 'iit', 'nit', 'nitc', 'manipal', 'christ', 'vit', 'amrita', 'sastra', 'psg', 'bits', 'university of', 'institute of technology']


def mmss(t):
    t = int(round(t)); return f'{t // 3600}:{t % 3600 // 60:02d}:{t % 60:02d}' if t >= 3600 else f'{t // 60}:{t % 60:02d}'


def opt(a, k, d=None):
    return a[a.index(k) + 1] if k in a else d


def read_lessons(paths):
    from playwright.sync_api import sync_playwright
    out = []
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page(viewport={'width': 1280, 'height': 720})
        for p in paths:
            pg.goto('file://' + os.path.abspath(p) + '?render'); pg.wait_for_timeout(1500)
            d = pg.evaluate("""() => ({meta: META, starts: window.__T, total: window.__TOTAL,
              sc: SC.map((s, i) => ({i, k: s.k, title: String(s.title || ''), term: String(s.term || ''), q: s.q || '', wrong: s.wrong || null}))})""")
            d['path'] = p; out.append(d)
        b.close()
    return out


def chapters(d):
    st, sc, meta = d['starts'], d['sc'], d['meta']
    ch = [(0.0, 'Introduction')]
    parts = meta.get('parts') or []
    pn = 0
    for s in sc:
        t = st[s['i']]
        if s['k'] == 'part':
            pn += 1; name = parts[pn - 1] if pn - 1 < len(parts) else s['title']
            ch.append((t, f'Part {pn}: {name[0].upper() + name[1:]}' if name else f'Part {pn}'))
        elif s['k'] == 'recap' and not any(c[1] == 'Quick recap' for c in ch):
            ch.append((t, 'Quick recap'))
        elif s['k'] == 'pq' and not any(c[1] == 'Exam practice' for c in ch):
            ch.append((t, 'Exam practice'))
    keep = [ch[0]]
    for t, n in ch[1:]:
        if t - keep[-1][0] >= 10: keep.append((t, n))
    return keep


def plain(x):
    # trap lines and titles can carry SVG <tspan> markup: superscripts as ^(...), subscripts as _x, every other tag dropped
    x = str(x or '')
    def sup(m): return '' if not m.group(1).strip() else '^(' + m.group(1) + ')'
    def sub(m): return '' if not m.group(1).strip() else '_' + m.group(1)
    x = re.sub(r'<tspan\b[^>]*(?:baseline-shift=\\?"super\\?"|dy=\\?"-[^"\\]*\\?")[^>]*>(.*?)</tspan>', sup, x, flags=re.S)
    x = re.sub(r'<tspan\b[^>]*(?:baseline-shift=\\?"sub\\?"|dy=\\?"\.?\d[^"\\]*\\?")[^>]*>(.*?)</tspan>', sub, x, flags=re.S)
    x = re.sub(r'<sup>(.*?)</sup>', sup, x, flags=re.S); x = re.sub(r'<sub>(.*?)</sub>', sub, x, flags=re.S)
    x = re.sub(r'<[^>]+>', '', x)
    for _ in range(3): x = html.unescape(x)
    return re.sub(r'\s+', ' ', x).strip()


def moments(d):
    st, out = d['starts'], []
    for s in d['sc']:
        s = dict(s, title=plain(s['title']), term=plain(s['term']), q=plain(s['q']), wrong=[plain(w) for w in (s['wrong'] or [])] or None)
        t = st[s['i']]; ttl = s['title'] or s['term']
        if s['k'] == 'trap2':
            w = re.sub(r'[“”"]', '', ' '.join(s['wrong'] or [])).strip().rstrip('.')
            out.append((t, f'Exam trap: "{w}" is wrong' if w else 'Exam trap'))
        elif re.match(r'(?i)worked example', ttl):
            lab = re.sub(r'(?i)^worked example\s*:?\s*', '', ttl)
            sep = ' ' if re.match(r'\d+\b', lab) else ': '   # "Worked example 2", never "Worked example: 2"
            if not any(lab and lab in m for _, m in out): out.append((t, f'Worked example{sep}{lab}' if lab else 'Worked example'))
        elif s['k'] == 'traps':
            out.append((t, ttl or 'Exam traps'))
        elif s['k'] == 'pq' and s['q']:
            q = s['q'] if len(s['q']) <= 90 else s['q'][:88].rsplit(' ', 1)[0] + '…'
            out.append((t, f'Exam question: {q}'))
    return out


def title_case(t):
    small = {'a', 'an', 'the', 'of', 'in', 'on', 'to', 'for', 'by', 'at', 'with', 'and', 'vs', 'from', 'into', 'or'}
    w = t.split()
    return ' '.join(x if (x != x.lower() or (i and x in small)) else x[0].upper() + x[1:] for i, x in enumerate(w))


def build_row(d, subj, deg, deptname, cfg, n_in_unit):
    meta = d['meta']; key = re.match(r'(.+?-u\d+-L\d+)', os.path.basename(d['path'])).group(1)
    topic = title_case(meta.get('title', key))
    parts = [p if (len(p) > 1 and p[1].isupper()) else p[0].lower() + p[1:] for p in (meta.get('parts') or []) if p]
    title = f'{topic} | {subj} | {deg} {deptname} | Free Notes'
    if len(title) > 100: title = f'{topic} | {subj} | {deg} {deptname}'
    if len(title) > 100: title = f'{topic} | {subj}'[:100]
    ch = chapters(d); notes = cfg.get('notes') or 'https://<notes site>'; find = cfg.get('find') or 'https://<finder site>'
    cover = ', '.join(parts[:-1]) + (' and ' if len(parts) > 1 else '') + parts[-1] if parts else topic.lower()
    lines = [f'📘 {topic}: {subj} for {deg} {deptname}, explained in one animated lesson. We cover {cover}, with worked examples, exam traps and exam practice.',
             '', '⏱️ Chapters:'] + [f'{mmss(t)} {n}' for t, n in ch] + [   # chapter lines stay plain: YouTube needs each to start with its time
             '', '📥 FREE NOTES',   # the person's layout (3 Nov 2026): a heading, then the Like step, then the PDF link in step 2
             '👍 Step 1: if this helped, tap Like. Helps us keep making free n easy lessons for every subject.',
             f'📄 Step 2: download the free notes PDF: {notes}/{key}.pdf',
             '✅ Every figure, worked example, exam trap, quiz and exam question of this lesson, in one file.']   # only the lesson PDF is offered (no unit books: every college groups the units differently; 3 Nov 2026)
    if cfg.get('playlist'): lines.append(f'▶️ {subj} playlist, every lesson in order: https://www.youtube.com/playlist?list={cfg["playlist"]}')
    tagw = re.sub(r'[^A-Za-z0-9]', '', subj)
    lines += (['', f'🔎 Find any topic of your syllabus: {find}'] if cfg.get('find') else []) + ['',
              '🎓 Free notes, free lessons, no sign-up.',
              '💬 Spotted a mistake? Tell us in the comments and it gets fixed in the next version.', '',
              ' '.join('#' + h for h in (cfg.get('hashtags') or {}).get(key, []) + [tagw, deg.replace('.', ''), re.sub(r'[^A-Za-z0-9]', '', deptname), 'UniversityFreeNEasy'])]   # topic hashtags first: YouTube shows the first three above the title
    desc = '\n'.join(lines)
    tags = []
    for t in [topic.lower(), f'{topic.lower()} {subj.lower()}', subj.lower(), f'{subj.lower()} {deg.lower()}', f'{deg.lower()} {deptname.lower()}', deptname.lower()] + [p.lower() for p in parts] + \
             [f'{subj.lower()} lecture', f'{subj.lower()} notes pdf', 'free notes pdf', 'animated lecture', 'university exam', 'university free n easy']:
        t = t.strip()
        if t and t not in tags and len(', '.join(tags + [t])) <= 500: tags.append(t)
    mom = moments(d)
    style = cfg.get('thumb', 't14')
    return {'key': key, 'unit': int(re.search(r'-u(\d+)-', key).group(1)), 'lesson': int(re.search(r'-L(\d+)', key).group(1)),
            'name': topic, 'length': mmss(d['total']), 'file': os.path.basename(d['path']),
            'title': title, 'description': desc, 'tags': ', '.join(tags),
            'problems': '\n'.join(f'{mmss(t)} {m}' for t, m in mom),
            'thumbnail': f'thumbnail\\{key}_{style}.jpg', 'thumbs_other': [f'thumbnail\\{key}_{s}.jpg' for s in ('t11', 't14', 't15') if s != style],
            'notes_pdf': f'pdf\\{key}.pdf', 'publish': '', 'chapters': ch}


SHEET = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600&family=Atkinson+Hyperlegible:wght@400;700&family=JetBrains+Mono:wght@400;500&display=swap">
<style>
:root{--bg:#f5f7f6;--surface:#fff;--fg:#17231f;--muted:#5b6b66;--line:#d8e1de;--accent:#2b8a3e;--accent-fg:#fff;--done:#2f9e44;--chip:#e6f4ea;
--display:"Fraunces",Georgia,serif;--body:"Atkinson Hyperlegible",system-ui,sans-serif;--mono:"JetBrains Mono",ui-monospace,Consolas,monospace}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#111a18;--surface:#18231f;--fg:#e7efec;--muted:#9aaba5;--line:#2b3a35;--accent:#69db7c;--accent-fg:#0b1a10;--done:#69db7c;--chip:#1d3226;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#111a18;--surface:#18231f;--fg:#e7efec;--muted:#9aaba5;--line:#2b3a35;--accent:#69db7c;--accent-fg:#0b1a10;--done:#69db7c;--chip:#1d3226;color-scheme:dark}
body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--body);font-size:15px;line-height:1.5}
.wrap{max-width:880px;margin:0 auto;padding:28px 16px 56px}
h1{font-family:var(--display);font-weight:600;font-size:2rem;margin:0 0 6px;text-wrap:balance}
h2{font-family:var(--display);font-weight:600;font-size:1.25rem;margin:22px 0 8px}
.lede{color:var(--muted);max-width:66ch;margin:0 0 8px}.note{font-size:.9rem;color:var(--muted);max-width:70ch;margin:0 0 18px}
.progress{font-family:var(--mono);font-size:.85rem;color:var(--muted);margin-bottom:12px}
details{background:var(--surface);border:1px solid var(--line);border-radius:10px;margin-bottom:10px}
summary{display:flex;align-items:center;gap:12px;padding:12px 14px;cursor:pointer;list-style:none}summary::-webkit-details-marker{display:none}
summary:focus-visible,button:focus-visible,input:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.num{font-family:var(--mono);font-weight:500;font-size:.85rem;background:var(--chip);color:var(--accent);border-radius:6px;padding:2px 8px;min-width:3.6em;text-align:center}
.cname{font-weight:700;flex:1;min-width:0}.meta{font-family:var(--mono);font-size:.8rem;color:var(--muted);white-space:nowrap}
.tick{display:flex;align-items:center;gap:6px;font-size:.8rem;color:var(--muted)}
details.isdone .num{background:var(--done);color:var(--surface)}details.isdone .cname{color:var(--muted);text-decoration:line-through}
.body{padding:0 14px 14px;display:grid;gap:12px}.facts{display:flex;flex-wrap:wrap;gap:8px 18px;font-size:.88rem;color:var(--muted)}.facts b{color:var(--fg)}
.field{border-top:1px solid var(--line);padding-top:10px;display:grid;gap:6px;min-width:0}.fhead{display:flex;align-items:center;gap:10px}
.flabel{font-size:.75rem;letter-spacing:.08em;text-transform:uppercase;font-weight:700;color:var(--muted);flex:1}.count{font-family:var(--mono);font-size:.75rem;color:var(--muted)}
button.copy{font:inherit;font-size:.82rem;font-weight:700;border:0;border-radius:6px;padding:5px 12px;background:var(--accent);color:var(--accent-fg);cursor:pointer;min-height:32px}button.copy.ok{background:var(--done)}
pre{margin:0;font-family:var(--mono);font-size:.82rem;line-height:1.55;white-space:pre-wrap;word-break:break-word;background:var(--bg);border:1px solid var(--line);border-radius:6px;padding:10px 12px;max-height:260px;overflow:auto}
@media (max-width:520px){.meta{display:none}}
</style></head><body><div class="wrap">
<h1>__H1__</h1>
<p class="lede">Paste-ready title, description, tags and key moments for every lesson video. Open a lesson, press Copy, paste into YouTube Studio, then tick Done.</p>
<p class="note">__NOTE__</p>
<div class="progress" id="progress"></div><div id="list"></div></div>
<script>
const ROWS = __ROWS__;
const FIELDS = [["title","Title",100],["description","Description",5000],["tags","Tags",500],["problems","Key moments (pinned comment)",800]];
const KEY = "__KEY__"; let done = {}; try { done = JSON.parse(localStorage.getItem(KEY) || "{}"); } catch (e) {}
const list = document.getElementById("list");
function save(){ try { localStorage.setItem(KEY, JSON.stringify(done)); } catch (e) {} progress(); }
function progress(){ const n = ROWS.filter(r => done[r.key]).length; document.getElementById("progress").textContent = n + " of " + ROWS.length + " videos uploaded"; }
function el(t, c, x){ const e = document.createElement(t); if (c) e.className = c; if (x != null) e.textContent = x; return e; }
let unit = 0;
ROWS.forEach(r => {
  if (r.unit !== unit) { unit = r.unit; list.append(el("h2", null, "Unit " + unit)); }
  const d = el("details"); if (done[r.key]) d.classList.add("isdone");
  const s = el("summary"); s.append(el("span","num","U" + r.unit + " L" + r.lesson), el("span","cname", r.name), el("span","meta", r.length + (r.publish ? " · " + r.publish : "")));
  const lab = el("label","tick"); const cb = document.createElement("input"); cb.type = "checkbox"; cb.checked = !!done[r.key];
  cb.addEventListener("click", e => e.stopPropagation()); cb.addEventListener("change", () => { done[r.key] = cb.checked; d.classList.toggle("isdone", cb.checked); save(); });
  lab.addEventListener("click", e => e.stopPropagation()); lab.append(cb, document.createTextNode("Done")); s.append(lab); d.append(s);
  const b = el("div","body"), f = el("div","facts");
  [["Video file", "html\\\\" + r.file], ["Thumbnail", r.thumbnail], ["Other thumbnails", r.thumbs_other.join(", ")], ["Notes", r.notes_pdf], ["Length", r.length]].concat(r.publish ? [["Schedule", r.publish + " IST"]] : [])
    .forEach(([k, v]) => { const p = el("span"); p.append(el("b", null, k + ": "), document.createTextNode(v)); f.append(p); });
  b.append(f);
  FIELDS.forEach(([k, label, lim]) => { if (!r[k]) return;
    const box = el("div","field"), h = el("div","fhead"); h.append(el("span","flabel",label), el("span","count", r[k].length + "/" + lim));
    const btn = el("button","copy","Copy"); btn.type = "button"; const pre = el("pre", null, r[k]);
    btn.addEventListener("click", () => { const ok = () => { btn.textContent = "Copied"; btn.classList.add("ok"); setTimeout(() => { btn.textContent = "Copy"; btn.classList.remove("ok"); }, 1500); };
      const fb = () => { const sel = getSelection(), rg = document.createRange(); rg.selectNodeContents(pre); sel.removeAllRanges(); sel.addRange(rg); btn.textContent = "Press Ctrl+C"; };
      try { navigator.clipboard.writeText(r[k]).then(ok, fb); } catch (e) { fb(); } });
    h.append(btn); box.append(h, pre); b.append(box); });
  d.append(b); list.append(d);
});
progress();
</script></body></html>"""


def pdf_pages(p):
    try:
        from pypdf import PdfReader
        return len(PdfReader(p).pages)
    except Exception:
        try:
            return len(re.findall(rb'/Type\s*/Page[^s]', open(p, 'rb').read()))
        except Exception:
            return -1


def main(a):
    if not a or a[0].startswith('-'): sys.exit(__doc__)
    sid = a[0]
    lessons_dir, notes_dir, thumbs_dir, root = opt(a, '--lessons'), opt(a, '--notes'), opt(a, '--thumbs'), opt(a, '--out', 'out')
    U = json.load(open(opt(a, '--universal', os.path.join(HERE, '..', 'universal.json'))))
    s = next(x for x in U['subjects'] if x['id'] == sid)
    subj, dept = s['name'], s.get('dept', 'common')
    deptname = U['departments'].get(dept, dept).split(' (')[0]
    deg = opt(a, '--degree', 'B.Tech' if s.get('scope', 'btech') == 'btech' else s.get('scope', '').upper())
    vid = json.load(open(opt(a, '--videos'))) if opt(a, '--videos') else {}
    cfg = dict(vid.get('site', {})); cfg['playlist'] = (vid.get('playlists') or {}).get(sid, ''); cfg['thumb'] = opt(a, '--thumb', 't14')
    cfg['hashtags'] = {f'{uk}-L{l["n"]}': l.get('hashtags') or [] for uk, u in vid.items() if uk.startswith(sid + '-u') and isinstance(u, dict) for l in u.get('lessons', [])}
    dest = os.path.join(root, deg, DEPT_FOLDER.get(dept, deptname), subj)
    for sub in ('html', 'pdf', 'thumbnail'): os.makedirs(os.path.join(dest, sub), exist_ok=True)
    pages = sorted(p for p in glob.glob(os.path.join(lessons_dir, f'{sid}-u*-L*.html')) if not re.search(r'_v\d+\.html$', p))
    pages.sort(key=lambda p: tuple(int(x) for x in re.search(r'-u(\d+)-L(\d+)', p).groups()))
    probs = []
    if not pages: sys.exit(f'no lesson pages {sid}-u*-L*.html (plain names) in {lessons_dir}')
    data = read_lessons(pages)
    rows = [build_row(d, subj, deg, deptname, cfg, 0) for d in data]
    # schedule
    if opt(a, '--publish'):
        h, m = map(int, opt(a, '--publish').split(':')); ev = int(opt(a, '--every', '5'))
        for i, r in enumerate(rows):
            t = h * 60 + m + i * ev; hh, mm = divmod(t % 1440, 60)
            r['publish'] = f'{(hh - 1) % 12 + 1}:{mm:02d} {"AM" if hh < 12 else "PM"}'
    # copy files
    for p, r in zip(pages, rows):
        shutil.copy2(p, os.path.join(dest, 'html', os.path.basename(p)))
        pdf = os.path.join(notes_dir, f"{r['key']}.pdf")
        if os.path.exists(pdf):
            shutil.copy2(pdf, os.path.join(dest, 'pdf', os.path.basename(pdf)))
            n = pdf_pages(pdf)
            if 0 <= n <= 1: probs.append(f"{r['key']}: notes PDF has {n} page(s): the cut failed")
        else:
            probs.append(f"{r['key']}: no notes PDF in {notes_dir}")
        for st in ('t11', 't14', 't15'):
            tp = os.path.join(thumbs_dir, f"{r['key']}_{st}.jpg")
            if os.path.exists(tp): shutil.copy2(tp, os.path.join(dest, 'thumbnail', os.path.basename(tp)))
            else: probs.append(f"{r['key']}: no thumbnail {st}")
        if len(r['title']) > 100: probs.append(f"{r['key']}: title {len(r['title'])} characters")
        if len(r['description']) > 5000: probs.append(f"{r['key']}: description {len(r['description'])} characters")
        if len(r['tags']) > 500: probs.append(f"{r['key']}: tags {len(r['tags'])} characters")
        if len(r['chapters']) < 3: probs.append(f"{r['key']}: only {len(r['chapters'])} chapters (YouTube needs 3)")
        tags_line = re.findall(r'#\w+', r['description'].split('\n')[-1])
        if len(tags_line) > 15: probs.append(f"{r['key']}: {len(tags_line)} hashtags (YouTube ignores them all past 15)")
        if not cfg['hashtags'].get(r['key']): probs.append(f"{r['key']}: no topic hashtags in videos.json (lessons[].hashtags)")
        blob = (r['title'] + r['description'] + r['tags'] + r['problems']).lower()
        for u in UNIS:
            if u == 'bits':   # plain "bits" is a word (CAN frames): only BITS in capitals as a name, or BITS Pilani
                if re.search(r'\bBITS\b(?! PER| per)|BITS Pilani', r['title'] + r['description'] + r['tags'] + r['problems']): probs.append(f"{r['key']}: mentions 'BITS'")
                continue
            if re.search(r'\b' + re.escape(u) + r'\b', blob): probs.append(f"{r['key']}: mentions '{u}'")
    # unit book PDFs are not offered (3 Nov 2026): only the lesson PDFs go into pdf\\ ; unit PDFs already there are left alone
    if not cfg.get('notes'):
        probs.append('the notes address is not set in videos.json (site.notes): the PDF link in every description is a placeholder; set it and run again before uploading')
    note = (f'Playlist: {subj} | {deg} {deptname} (every lesson in order). Settings for every video: Standard YouTube licence, category Education, '
            f'not made for kids, comments on, end screen with the next lesson and Subscribe. The pinned comment is the key moments list. '
            f'Thumbnail style {cfg["thumb"]} is suggested; the other two are in the thumbnail folder.')
    for r in rows: r.pop('chapters')
    doc = (SHEET.replace('__TITLE__', f'{subj} Upload Sheet').replace('__H1__', html.escape(f'{deg} {deptname}: {subj} upload sheet'))
           .replace('__NOTE__', html.escape(note)).replace('__KEY__', f'ufe-upload-{sid}').replace('__ROWS__', json.dumps(rows, ensure_ascii=False).replace('</', '<\\/')))
    open(os.path.join(dest, 'upload_sheet.html'), 'w', encoding='utf-8').write(doc)
    json.dump(rows, open(os.path.join(dest, 'upload_sheet.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    nh = len(os.listdir(os.path.join(dest, 'html'))); npdf = len(os.listdir(os.path.join(dest, 'pdf'))); nt = len(os.listdir(os.path.join(dest, 'thumbnail')))
    print(f'{dest}: {nh} lesson pages, {npdf} PDFs, {nt} thumbnails, upload_sheet.html ({len(rows)} videos)')
    for p in probs: print(' -', p)
    print('OK' if not probs else f'{len(probs)} problem(s)')


if __name__ == '__main__':
    main(sys.argv[1:])
