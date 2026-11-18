#!/usr/bin/env python3
"""notes_pdfs.py: regenerate the notes PDFs of the lessons whose unit book changed.

usage: notes_pdfs.py <sid> <unit> [<unit> ...] --books <books root> --out <scratch dir> [--replace]

  <books root>  a folder holding cse/<sid>/<sid>-uN.html (the repo's books/ folder works)
  <scratch dir> your own scratchpad folder, never /mnt/project-files

It builds a lesson list from _work/uN/videos.<sid>-uN.json with each lesson's real title (from its js),
runs the subject's _work/site/make_site.py --pdf-only with the data pack from c-xr, then for every PDF:
  gate: more than 1 page, and "Written with top universities' syllabi" in the last 600 characters
  compare: the text against the live copy in 05_Site/notes-pdf/
Text is compared with all whitespace removed. It exits non-zero when pypdf or playwright is missing or a lesson's PDF was not made.
Only PDFs that pass the gate and whose text changed are listed; with --replace they are copied over the
same-name files in 05_Site/notes-pdf/, 06_Deliver/cse/site-pdf/, _work/notes/ and B.Tech/CSE/*/pdf/,
wherever a file of that name already exists. Nothing new is added.
"""
import glob, json, os, re, shutil, subprocess, sys
try:
    from pypdf import PdfReader
    import playwright.sync_api  # make_site.py prints PDFs with it and silently skips them without it
except ImportError as e:
    sys.exit(f'notes_pdfs: {e}. Install it first: pip install pypdf playwright==1.63.0 (matches the Chromium in /opt/pw-browsers); do not run "playwright install".')

PF = '/mnt/project-files'
a = sys.argv[1:]
sid = a[0]; units = [int(x) for x in a[1:] if x.isdigit()]
books = a[a.index('--books') + 1]; out = os.path.abspath(a[a.index('--out') + 1]); replace = '--replace' in a
W = f'{PF}/04_Lessons/cse/{sid}/_work'
X = f'{PF}/04_Lessons/cse/c-xr/_work/site'
os.makedirs(out, exist_ok=True)

base = json.load(open(f'{W}/site/videos.json')) if os.path.exists(f'{W}/site/videos.json') else {}
v = {k: base[k] for k in ('site', 'playlists') if k in base}
for u in units:
    uj = json.load(open(f'{W}/u{u}/videos.{sid}-u{u}.json'))
    key = f'{sid}-u{u}'
    v[key] = uj[key]
    for l in v[key]['lessons']:
        js = open(f'{W}/u{u}/out/{key}-L{l["n"]}.js', encoding='utf8').read()
        m = re.search(r"title:(['\"])(.*?)\1", js)
        if m: l['title'] = m.group(2)
vj = os.path.join(out, f'{sid}.videos.json')
json.dump(v, open(vj, 'w'), indent=1)
site = f'{W}/site/make_site.py' if os.path.exists(f'{W}/site/make_site.py') else f'{X}/make_site.py'
r = subprocess.run([sys.executable, site, f'{X}/universal.json', f'{X}/worklist.json', vj, books, os.path.join(out, 'site'), '--pdf-only'], capture_output=True, text=True)
if r.returncode or 'pdf: playwright not available' in r.stdout:
    sys.exit('notes_pdfs: make_site.py made no PDFs\n' + r.stdout + r.stderr)

def text(p):
    rd = PdfReader(p); return len(rd.pages), ' '.join(pg.extract_text() for pg in rd.pages)
norm = lambda t: re.sub(r'\s+', '', t)   # text extraction splits words differently between runs ("SYLL ABUS")

bad = 0
want = {f'{sid}-u{u}-L{l["n"]}.pdf' for u in units for l in v[f'{sid}-u{u}']['lessons']}
pdfs = sorted(glob.glob(os.path.join(out, 'site', 'notes', f'{sid}-u*.pdf')))
got = {os.path.basename(f) for f in pdfs}
if want - got:
    sys.exit('notes_pdfs: no PDF made for ' + ', '.join(sorted(want - got)) + '\n' + r.stdout + r.stderr)
for f in pdfs:
    b = os.path.basename(f); n, t = text(f)
    ok = n > 1 and "Written with top universities' syllabi" in t[-600:]
    live = f'{PF}/05_Site/notes-pdf/{b}'
    changed = True
    if os.path.exists(live):
        changed = norm(text(live)[1]) != norm(t)
    print(f'{b}: {n} pages, {"gate ok" if ok else "GATE FAIL"}, {"changed" if changed else "same"}')
    bad += not ok
    if ok and changed and replace:
        targets = [live, f'{PF}/06_Deliver/cse/site-pdf/{b}', f'{W}/notes/{b}'] + glob.glob(f'{PF}/B.Tech/CSE/*/pdf/{b}')
        for t2 in targets:
            if os.path.exists(t2):
                shutil.copyfile(f, t2); print('   replaced', t2)
sys.exit(1 if bad else 0)
