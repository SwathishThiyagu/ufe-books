"""Checks that do not trust the model: recompute worked-example numbers, compile and run code,
open source links."""
import os, re, subprocess, tempfile, shutil, json, math
import urllib.request, urllib.parse

NUM = re.compile(r'[-+]?(?:\d[\d,]*\.?\d*|\.\d+)(?:[eE][-+]?\d+)?')


def numbers(s):
    out = []
    for m in NUM.findall(str(s)):
        try:
            out.append(float(m.replace(',', '')))
        except ValueError:
            pass
    return out


def run_python(code, timeout=15):
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, 'check.py')
        open(p, 'w', encoding='utf-8').write(code)
        try:
            r = subprocess.run(['python3', '-I', p], capture_output=True, text=True, timeout=timeout, cwd=d)
        except subprocess.TimeoutExpired:
            return False, 'timed out'
        if r.returncode != 0:
            return False, (r.stderr or r.stdout)[-600:]
        return True, r.stdout


def close(a, b):
    return math.isclose(a, b, rel_tol=1e-2, abs_tol=1e-6) or (abs(b) >= 1 and abs(a - round(b)) < 0.5 and abs(b - round(b)) < 0.05 and round(a) == round(b))


def check_example(ex):
    """Return a list of problems with the worked example's numbers (empty = fine)."""
    code = (ex.get('check') or '').strip()
    vals = ex.get('values') or []
    if not code:
        return []
    ok, out = run_python(code)
    if not ok:
        return [f'the example\'s "check" code failed: {out.strip()[:300]}']
    got = numbers(out)
    if not got:
        return ['the example\'s "check" code printed no numbers']
    try:
        vals = [float(v) for v in vals]
    except (TypeError, ValueError):
        return ['"values" must be a list of numbers']
    bad = [v for v in vals if not any(close(g, v) for g in got)]
    if bad:
        return [f'the worked example states {bad} but recomputing it gives {got[:8]}; fix the steps and the answer so they match the correct values']
    return []


def _norm(s):
    return '\n'.join(l.rstrip() for l in str(s).strip().splitlines())


def run_code(lang, code, stdin='', timeout=10):
    """Compile and run one program. Returns (ran, output_or_error). ran=None when the language is not runnable here."""
    lang = (lang or '').lower()
    if lang not in ('c', 'cpp', 'c++', 'java', 'python', 'py'):
        return None, ''
    if lang in ('c', 'cpp', 'c++') and not re.search(r'\bmain\s*\(', code): return None, ''
    if lang == 'java' and 'static void main' not in code: return None, ''
    d = tempfile.mkdtemp()
    try:
        if lang == 'c':
            src = os.path.join(d, 'p.c'); open(src, 'w').write(code)
            c = subprocess.run(['gcc', '-std=c11', '-O1', '-w', src, '-o', os.path.join(d, 'p'), '-lm'], capture_output=True, text=True, timeout=60)
            if c.returncode: return False, 'compile error: ' + c.stderr[-500:]
            cmd = [os.path.join(d, 'p')]
        elif lang in ('cpp', 'c++'):
            src = os.path.join(d, 'p.cpp'); open(src, 'w').write(code)
            c = subprocess.run(['g++', '-std=c++17', '-O1', '-w', src, '-o', os.path.join(d, 'p')], capture_output=True, text=True, timeout=90)
            if c.returncode: return False, 'compile error: ' + c.stderr[-500:]
            cmd = [os.path.join(d, 'p')]
        elif lang == 'java':
            m = re.search(r'public\s+(?:final\s+)?class\s+(\w+)', code) or re.search(r'class\s+(\w+)[^{]*\{[^}]*static\s+void\s+main', code, re.S)
            name = m.group(1) if m else 'Main'
            src = os.path.join(d, f'{name}.java'); open(src, 'w').write(code)
            if not shutil.which('javac'): return None, ''
            c = subprocess.run(['javac', '-nowarn', src], capture_output=True, text=True, timeout=90, cwd=d)
            if c.returncode: return False, 'compile error: ' + c.stderr[-500:]
            cmd = ['java', '-cp', d, name]
        else:
            src = os.path.join(d, 'p.py'); open(src, 'w').write(code)
            cmd = ['python3', '-I', src]
        try:
            r = subprocess.run(cmd, input=stdin or '', capture_output=True, text=True, timeout=timeout, cwd=d)
        except subprocess.TimeoutExpired:
            return False, 'the program did not finish within 10 seconds'
        if r.returncode != 0 and lang in ('python', 'py', 'java'):
            return False, 'runtime error: ' + (r.stderr or '')[-500:]
        return True, r.stdout
    except FileNotFoundError as e:
        return None, str(e)
    finally:
        shutil.rmtree(d, ignore_errors=True)


def check_code(lang, code, stdin, shown):
    """(problems, real_output). real_output is None when the code was not run."""
    ran, out = run_code(lang, code, stdin)
    if ran is None:
        return [], None
    if ran is False:
        return [f'a {lang} program does not run: {out.strip()[:400]}'], None
    if shown is not None and str(shown).strip() and _norm(shown) != _norm(out):
        return [f'a {lang} program prints\n{_norm(out)[:400]}\nbut the chapter shows\n{_norm(shown)[:400]}\nMake the shown output and any explanation match what the program really prints'], out
    return [], out


def check_links(web, log, limit=6):
    """Open each link; keep those that answer with a page."""
    keep = []
    for w in web or []:
        url = str(w.get('url', ''))
        if not url.startswith('https://') or len(keep) >= limit:
            continue
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (compatible; ufe-books-link-check)'})
            with urllib.request.urlopen(req, timeout=15) as r:
                body = r.read(200000).decode('utf-8', 'ignore')
                ok = r.status == 200 and len(body) > 500
                title = re.search(r'<title[^>]*>(.*?)</title>', body, re.S | re.I)
        except Exception as e:
            log(f'  link dropped: {url} ({type(e).__name__})'); continue
        if ok:
            w['page_title'] = re.sub(r'\s+', ' ', title.group(1)).strip()[:120] if title else ''
            keep.append(w)
        else:
            log(f'  link dropped: {url} (no page)')
    return keep


def check_wikipedia(titles, log, limit=4):
    """Turn exact Wikipedia titles into checked links (the REST summary must exist and not be a disambiguation)."""
    keep = []
    for t in titles or []:
        if len(keep) >= limit: break
        t = str(t).strip()
        if not t: continue
        slug = urllib.parse.quote(t.replace(' ', '_'), safe='')
        try:
            req = urllib.request.Request(f'https://en.wikipedia.org/api/rest_v1/page/summary/{slug}', headers={'User-Agent': 'ufe-books-link-check/1.0'})
            with urllib.request.urlopen(req, timeout=15) as r:
                js = json.loads(r.read().decode('utf-8'))
        except Exception as e:
            log(f'  wikipedia dropped: {t} ({type(e).__name__})'); continue
        if js.get('type') == 'disambiguation' or not js.get('content_urls'): continue
        keep.append({'title': f'Wikipedia: {js.get("title", t)}', 'url': js['content_urls']['desktop']['page']})
    return keep
