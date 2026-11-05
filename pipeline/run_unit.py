#!/usr/bin/env python3
"""Write one unit book with a free model, step by step, checking every step.

usage: python3 pipeline/run_unit.py <unit> [--out PATH] [--state DIR] [--mock] [--no-review] [--offline]

Steps (each saved in the state folder, so a run that stops on the daily quota continues later):
  1 plan the unit        one call: the idea, figure, example and trap of every chapter
  2 write each chapter   one call per chapter, JSON only; the figure is drawn by figures.py,
                         worked-example numbers are recomputed, programs are compiled and run
  3 review each chapter  a second model lists errors; a high-severity list triggers one revision
  4 unit sections        summary, question bank, glossary, sources; links are opened
  5 assemble + check     pack/check_book.py --render; short chapters, spilled figures and the like
                         go back to the model for a targeted fix
Exit codes: 0 book OK, 1 book written but the checker still has problems, 75 stopped on the free quota.
"""
import sys, os, json, re, time, subprocess, argparse, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import figures as F, render as R, verify as V, prompts as PR
from llm import Gemini, Mock, QuotaExhausted, ModelError


class State:
    def __init__(self, d):
        self.d = d; os.makedirs(d, exist_ok=True)
    def path(self, k): return os.path.join(self.d, k + '.json')
    def get(self, k):
        p = self.path(k)
        return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else None
    def put(self, k, v):
        tmp = self.path(k) + '.tmp'
        json.dump(v, open(tmp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1); os.replace(tmp, self.path(k))
        return v


def load(unit):
    q = json.load(open(os.path.join(ROOT, 'queue.json'), encoding='utf-8'))
    ent = next((u for u in q if u['unit'] == unit), None)
    if not ent: raise SystemExit(f'{unit} is not in queue.json')
    P = json.load(open(os.path.join(ROOT, 'packets', unit + '.json'), encoding='utf-8'))
    shell = open(os.path.join(ROOT, 'pack', 'book_shell.html'), encoding='utf-8').read()
    return ent, P, shell


# ---------------- checks the model's JSON must pass ----------------
def check_plan(P):
    n = len(P['unit']['subtopics'])
    def f(d):
        p = []
        if not isinstance(d, dict): return ['reply must be a JSON object']
        if not str(d.get('lead', '')).strip(): p.append('"lead" is missing')
        if len(str(d.get('about', '')).split()) < 50: p.append('"about" must be one paragraph of 80-140 words')
        if not isinstance(d.get('chapters'), list) or len(d['chapters']) != n: p.append(f'"chapters" must have exactly {n} entries, one per chapter in order')
        return p
    return f


def college_problems(text):
    named = sorted(set(m.group(0) for m in R.COLLEGE.finditer(text)))
    p = [f'never name a college or university from the syllabi; found {named}; write "some syllabi" instead'] if named else []
    if R.COUNTED.search(text): p.append('do not count the universities that teach a topic')
    return p


def code_items(ch):
    """Every runnable program in a chapter: (container dict, code key, output key)."""
    for sec in ch.get('sections') or []:
        for b in sec.get('blocks') or []:
            if isinstance(b, dict) and b.get('type') == 'code':
                yield b, b
    for ex in ch.get('examples') or []:
        cd = ex.get('code')
        if isinstance(cd, dict) and str(cd.get('code', '')).strip():
            yield cd, ex


def check_chapter(P, k, final=False):
    st = P['unit']['subtopics'][k - 1]
    adv = 'advanced' in (st.get('tags') or [])
    lo, hi = (650, 1000) if adv else (900, 1700)
    def f(ch):
        p = []
        if not isinstance(ch, dict): return ['reply must be a JSON object']
        for key in ('lead', 'sections', 'figure', 'examples', 'traps', 'quiz', 'beyond'):
            if not ch.get(key): p.append(f'"{key}" is missing or empty')
        secs = ch.get('sections') or []
        if not 2 <= len(secs) <= 5: p.append('give 2 to 4 "sections"')
        for i, s in enumerate(secs, 1):
            if not isinstance(s, dict) or not s.get('h3') or not s.get('blocks'): p.append(f'section {i} needs "h3" and "blocks"')
            for b in (s.get('blocks') or []) if isinstance(s, dict) else []:
                if not isinstance(b, dict) or b.get('type') not in ('p', 'steps', 'bullets', 'formula', 'code', 'table'):
                    p.append(f'section {i} has a block with an unknown "type" (use p, steps, bullets, formula, code, table)'); break
        qz = ch.get('quiz') or []
        if not 5 <= len(qz) <= 9: p.append('give 6 to 8 quiz questions')
        lv = {str(q.get('level', '')).lower() for q in qz if isinstance(q, dict)}
        miss = [x for x in R.LEVELS if x not in lv]
        if miss: p.append(f'the quiz needs at least one question of each level; missing {miss}')
        if not 3 <= len(ch.get('traps') or []) <= 6: p.append('give 3 to 5 exam traps')
        fig = ch.get('figure') or {}
        try:
            F.render(fig.get('spec') or {}, 'chk')
        except F.FigureError as e:
            p.append(f'the figure cannot be drawn: {e}')
        if not str(fig.get('caption', '')).strip(): p.append('the figure needs a caption')
        for j, ex in enumerate(ch.get('examples') or [], 1):
            if not isinstance(ex, dict) or not ex.get('question') or not ex.get('steps') or not ex.get('answer'):
                p.append(f'worked example {j} needs "question", "steps" and "answer"'); continue
            p += [f'worked example {j}: {x}' for x in V.check_example(ex)]
        for cont, owner in code_items(ch):
            shown = owner.get('output') if owner is not cont else cont.get('output')
            probs, real = V.check_code(cont.get('lang'), cont.get('code', ''), cont.get('stdin', ''), shown)
            p += probs
        w = R.word_count(ch)
        if w < lo: p.append(f'the chapter has about {w} words; it needs {lo + 100}-{hi - 200} (expand the sections, not with filler)')
        if w > hi + 100: p.append(f'the chapter has about {w} words; keep it under {hi} (cut repetition)')
        p += college_problems(json.dumps(ch, ensure_ascii=False))
        return p
    return f


def settle_code(ch, log, k):
    """Show the real output of every program that runs (the model's guess is replaced)."""
    flags = []
    for cont, owner in code_items(ch):
        ran, out = V.run_code(cont.get('lang'), cont.get('code', ''), cont.get('stdin', ''))
        if ran:
            tgt = owner if owner is not cont else cont
            if V._norm(tgt.get('output', '')) != V._norm(out):
                flags.append(f'chapter {k}: a {cont.get("lang")} program\'s shown output was replaced by its real output; check the text around it')
                tgt['output'] = out.rstrip()
        elif ran is False:
            flags.append(f'chapter {k}: a {cont.get("lang")} program does not run ({out.strip()[:80]})')
    return flags


def check_unit(d):
    p = []
    if not isinstance(d, dict): return ['reply must be a JSON object']
    if len(d.get('key_terms') or []) < 10: p.append('give 12-20 key_terms')
    if len(d.get('takeaways') or []) < 6: p.append('give 6-10 takeaways')
    bank = d.get('bank') or []
    if len(bank) < 10: p.append('give 12-14 bank questions')
    groups = {str(q.get('group', '')).split('-')[0] for q in bank if isinstance(q, dict)}
    if not {'remember', 'apply', 'analyze'} <= groups: p.append('bank questions must cover all three groups: remember-understand, apply, analyze-evaluate')
    if sum(1 for q in bank if isinstance(q, dict) and len(q.get('chapters') or []) >= 2) < 2: p.append('at least two bank questions must span several chapters ("chapters" with 2 or more numbers)')
    if len(d.get('glossary') or []) < 15: p.append('give 18-26 glossary terms')
    if not d.get('textbooks'): p.append('give 2-4 textbooks')
    p += college_problems(json.dumps(d, ensure_ascii=False))
    return p


# ---------------- the run ----------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('unit'); ap.add_argument('--out'); ap.add_argument('--state')
    ap.add_argument('--mock', action='store_true'); ap.add_argument('--no-review', action='store_true')
    ap.add_argument('--offline', action='store_true', help='do not open source links')
    a = ap.parse_args()
    if os.environ.get('FREE_MOCK'): a.mock = a.offline = True     # used only to test ci.sh
    ent, P, shell = load(a.unit)
    out = os.path.join(ROOT, a.out or ent['out'])
    S = State(a.state or os.path.join(ROOT, '.free', a.unit))
    logf = open(os.path.join(S.d, 'log.txt'), 'a', encoding='utf-8')
    def log(m):
        line = f'{datetime.datetime.now():%H:%M:%S} {m}'; print(line, flush=True); logf.write(line + '\n'); logf.flush()
    log(f'=== {a.unit}: {P["subject"]["name"]}, Unit {P["unit"]["n"]} {P["unit"]["name"]} -> {os.path.relpath(out, ROOT)}')
    if a.mock:
        import mock
        ask = Mock(mock.answer(P), log)
    else:
        ask = Gemini.from_env(log)
    flags = S.get('flags') or []
    def flag(m):
        if m not in flags: flags.append(m); S.put('flags', flags)
    t0 = time.time()
    N = P['unit']['n']; subs = P['unit']['subtopics']; ids = {s['id'] for s in subs}
    try:
        plan = S.get('plan') or S.put('plan', ask.json('plan', PR.SYSTEM, PR.plan(P), check=check_plan(P)))
        while len(plan.get('chapters', [])) < len(subs): plan.setdefault('chapters', []).append({})
        for k in range(1, len(subs) + 1):
            key = f'ch{k}'
            ch = S.get(key)
            if ch is None:
                log(f'chapter {N}.{k}: {subs[k - 1]["t"]}')
                ch = ask.json(key, PR.SYSTEM, PR.chapter(P, k, plan), check=check_chapter(P, k))
                for m in settle_code(ch, log, k): flag(m)
                for x in check_chapter(P, k)(ch):
                    if 'words' not in x: flag(f'chapter {k}: {x}')
                S.put(key, ch)
            if not a.no_review and not S.get(key + '.reviewed'):
                rv = ask.json(f'review{k}', PR.SYSTEM, PR.review(P, k, R.plain_text(P, k, ch)), role='review', temperature=0.2)
                issues = [i for i in (rv.get('issues') or []) if isinstance(i, dict)]
                high = [i for i in issues if str(i.get('severity', '')).lower() == 'high']
                log(f'  review {N}.{k}: {len(high)} high, {len(issues) - len(high)} low')
                if high:
                    fixed = ask.json(f'revise{k}', PR.SYSTEM, PR.revise(P, k, ch, issues), check=check_chapter(P, k))
                    if isinstance(fixed, dict) and not [x for x in check_chapter(P, k)(fixed) if 'words' not in x]:
                        ch = fixed
                        for m in settle_code(ch, log, k): flag(m)
                        S.put(key, ch)
                    else:
                        flag(f'chapter {k}: the reviewer found {len(high)} serious problem(s) and the revision did not pass the checks; read the review in the state folder')
                S.put(f'review{k}', issues); S.put(key + '.reviewed', True)
        us = S.get('unit')
        if us is None:
            brief = []
            for k, s in enumerate(subs, 1):
                ch = S.get(f'ch{k}')
                terms = sorted(set(re.findall(r'<b>([^<]{2,40})</b>', json.dumps(ch, ensure_ascii=False))))[:12]
                brief.append(f'{N}.{k} {s["t"]} (k={k}): {plan["chapters"][k - 1].get("idea", "")} Key terms: {", ".join(terms)}')
            us = S.put('unit', ask.json('unit', PR.SYSTEM, PR.unit_sections(P, plan, '\n'.join(brief)), check=check_unit))
        web = S.get('web')
        if web is None:
            web = [] if a.offline else V.check_links(us.get('web'), log)
            if not a.offline and len(web) < 4:
                have = {w['url'] for w in web}
                web += [w for w in V.check_wikipedia(us.get('wikipedia'), log, 6 - len(web)) if w['url'] not in have]
            S.put('web', web)
        # assemble, check, fix
        for rnd in range(3):
            chs, fig_bad = [], []
            for k in range(1, len(subs) + 1):
                h, ok = R.chapter_html(P, k, S.get(f'ch{k}'), ids)
                chs.append(h)
                if not ok: fig_bad.append(k)
            for k in fig_bad:
                if S.get(f'figfix{k}'): flag(f'chapter {k}: the figure could not be drawn; a plain box diagram stands in for it'); continue
                ch = S.get(f'ch{k}'); fig = ch.get('figure') or {}
                try: F.render(fig.get('spec') or {}, 'x'); err = 'unknown'
                except F.FigureError as e: err = str(e)
                new = ask.json(f'figfix{k}', PR.SYSTEM, PR.figure_fix(P, k, fig.get('spec'), err, fig.get('caption', '')))
                S.put(f'figfix{k}', True)
                try:
                    F.render(new.get('spec') or {}, 'x')
                    ch['figure'] = {'after_section': fig.get('after_section', 1), 'caption': new.get('caption') or fig.get('caption', ''), 'spec': new['spec']}
                    S.put(f'ch{k}', ch)
                except (F.FigureError, AttributeError, KeyError):
                    flag(f'chapter {k}: the figure could not be drawn; a plain box diagram stands in for it')
            if fig_bad:
                chs = [R.chapter_html(P, k, S.get(f'ch{k}'), ids)[0] for k in range(1, len(subs) + 1)]
            page = R.book(P, shell, plan, chs, us, web)
            os.makedirs(os.path.dirname(out), exist_ok=True)
            open(out, 'w', encoding='utf-8').write(page)
            res = subprocess.run([sys.executable, os.path.join(ROOT, 'pack', 'check_book.py'), out, os.path.join(ROOT, 'packets', a.unit + '.json'), '--render'],
                                 capture_output=True, text=True)
            log('  checker: ' + res.stdout.strip().replace('\n', ' | ')[:900])
            if res.returncode == 0:
                break
            probs = [l[3:] for l in res.stdout.splitlines() if l.startswith(' - ')]
            acted = False
            for pr in probs:
                m = re.match(r'chapter "([^"]+)": only (\d+) words|chapter "([^"]+)": (\d+) words is too long', pr)
                if m:
                    cid = m.group(1) or m.group(3); w = int(m.group(2) or m.group(4))
                    k = next(i for i, s in enumerate(subs, 1) if s['id'] == cid)
                    if S.get(f'resize{k}.{rnd}'): continue
                    adv = 'advanced' in (subs[k - 1].get('tags') or [])
                    lo, hi = (700, 900) if adv else (1000, 1500)
                    new = ask.json(f'resize{k}', PR.SYSTEM, PR.resize(P, k, S.get(f'ch{k}'), w, lo, hi), check=check_chapter(P, k))
                    if isinstance(new, dict) and new.get('sections'):
                        for mm in settle_code(new, log, k): flag(mm)
                        S.put(f'ch{k}', new); acted = True
                    S.put(f'resize{k}.{rnd}', True)
                    continue
                m = re.search(r'text spills outside the svg box in figure\(s\) \[([\d, ]+)\]', pr)
                if m:
                    for i in [int(x) for x in m.group(1).split(',')]:
                        if i <= len(subs) and not S.get(f'spill{i}'):
                            ch = S.get(f'ch{i}'); fig = ch.get('figure') or {}
                            new = ask.json(f'spill{i}', PR.SYSTEM, PR.figure_fix(P, i, fig.get('spec'), 'some labels spill outside the figure at phone width', fig.get('caption', '')))
                            S.put(f'spill{i}', True)
                            try:
                                F.render(new.get('spec') or {}, 'x')
                                ch['figure'] = {'after_section': fig.get('after_section', 1), 'caption': new.get('caption') or fig.get('caption', ''), 'spec': new['spec']}
                                S.put(f'ch{i}', ch); acted = True
                            except (F.FigureError, AttributeError, KeyError):
                                flag(f'figure {i}: labels spill outside the figure')
                    continue
            if not acted:
                for pr in probs: flag('checker: ' + pr)
                break
        ok = res.returncode == 0
    except QuotaExhausted as e:
        log(f'stopped: {e}. Progress is saved; the next run continues from here.')
        S.put('status', {'state': 'quota', 'at': f'{datetime.datetime.now():%Y-%m-%d %H:%M}'})
        report(S, a.unit, ask, flags, t0, None, out)
        sys.exit(75)
    except ModelError as e:
        log(f'model error: {e}')
        S.put('status', {'state': 'error', 'error': str(e)[:300]})
        report(S, a.unit, ask, flags, t0, None, out)
        sys.exit(1)
    S.put('status', {'state': 'ok' if ok else 'problems', 'at': f'{datetime.datetime.now():%Y-%m-%d %H:%M}'})
    report(S, a.unit, ask, flags, t0, res.stdout, out)
    sys.exit(0 if ok else 1)


def report(S, unit, ask, flags, t0, checker, out):
    prev = S.get('usage') or {'calls': 0, 'tokens_in': 0, 'tokens_out': 0, 'minutes': 0}
    use = {'calls': prev['calls'] + ask.calls, 'tokens_in': prev['tokens_in'] + ask.tokens_in,
           'tokens_out': prev['tokens_out'] + ask.tokens_out, 'minutes': round(prev['minutes'] + (time.time() - t0) / 60, 1)}
    S.put('usage', use)
    lines = [f'# {unit}: free-model run', '',
             f'- Book: `{os.path.relpath(out, ROOT)}`',
             f'- Status: {(S.get("status") or {}).get("state")}',
             f'- Model calls so far: {use["calls"]} ({use["tokens_in"]:,} tokens in, {use["tokens_out"]:,} out), {use["minutes"]} minutes', '']
    if checker: lines += ['## Checker', '', '```', checker.strip(), '```', '']
    lines += ['## For the reviewer', ''] + ([f'- {f}' for f in flags] or ['- nothing flagged'])
    rv = [(k, S.get(f'review{k}')) for k in range(1, 30) if S.get(f'review{k}') is not None]
    if rv:
        lines += ['', '## Reviewer notes (after any revision)', '']
        for k, issues in rv:
            for i in issues:
                lines.append(f'- ch {k} [{i.get("severity")}] {i.get("where", "")}: {i.get("problem", "")}')
    open(os.path.join(S.d, 'report.md'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')


if __name__ == '__main__':
    main()
