"""A lesson writer that works like Claude's usual writer threads, driven by any OpenAI-compatible model with tools
and image input (DeepSeek Flash). Same rules (WRITE.md), same skeleton, same loop: read, fill, build, look at the
contact sheet and single frames, fix, rebuild, until it looks right. Builds are silent (no voice); the voice is
recorded afterwards by a separate step.

    python pipeline/lessons/agent.py <lesson dir> <lesson.js name> [--steps 90]

Env: OPENAI_BASE_URL, OPENAI_API_KEY, OPENAI_MODEL (default deepseek-flash), UFE_ENGINE (engine folder),
LBUILD (path to kit/lbuild.py when the lesson uses a picture kit; otherwise the engine's lesson_build.py is used).
Writes <lesson dir>/agent.log (every step) and agent.usage.json.
"""
import sys, os, json, base64, subprocess, time, re, io, urllib.request, urllib.error
FLAGS = {'send_reasoning': True}

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
D = os.path.abspath(sys.argv[1]); NAME = sys.argv[2]
STEPS = int(sys.argv[sys.argv.index('--steps') + 1]) if '--steps' in sys.argv else 90
LESSON = os.path.join(D, NAME); STEM = NAME[:-3]
OUT = os.path.join(D, 'out', STEM + '.html'); SHEET = os.path.join(D, 'sheet'); SHEET40 = os.path.join(D, 'sheet40')
ENGINE = os.environ.get('UFE_ENGINE', os.path.join(ROOT, 'pipeline', 'lessons', 'engine'))
LBUILD = os.environ.get('LBUILD')
BASE = os.environ.get('OPENAI_BASE_URL', 'https://api.deepseek.com').rstrip('/')
KEY = os.environ['OPENAI_API_KEY']; MODEL = os.environ.get('OPENAI_MODEL', 'deepseek-flash')
LOG = open(os.path.join(D, 'agent.log'), 'a', encoding='utf-8')
def log(*a):
    s = ' '.join(str(x) for x in a); print(s[:400], flush=True); LOG.write(s + '\n'); LOG.flush()

def inside(p, roots):
    p = os.path.abspath(p if os.path.isabs(p) else os.path.join(D, p))
    if not any(p == r or p.startswith(r + os.sep) for r in roots): raise ValueError(f'path not allowed: {p}')
    return p
READ_ROOTS = [D, ENGINE] + ([os.path.dirname(LBUILD)] if LBUILD else [])

def build(kind):
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    if LBUILD:
        pre = [sys.executable, LBUILD]
        cmds = {'check': pre + [LESSON, OUT, '--check'], 'build': pre + [LESSON, OUT, '--silent'],
                'sheet': pre + ['--sheet', OUT, SHEET, '--frames', '--play'], 'sheet40': pre + ['--sheet', OUT, SHEET40, '--at', '0.4']}
    else:
        b = os.path.join(ENGINE, 'lesson_build.py'); s = os.path.join(ENGINE, 'lesson_sheet.py')
        cmds = {'check': [sys.executable, b, LESSON, OUT, '--check'], 'build': [sys.executable, b, LESSON, OUT, '--silent'],
                'sheet': [sys.executable, s, OUT, SHEET, '--frames', '--play'], 'sheet40': [sys.executable, s, OUT, SHEET40, '--at', '0.4']}
    if kind == 'all':
        out = []
        for k in ('check', 'build', 'sheet'):
            r = subprocess.run(cmds[k], capture_output=True, text=True, timeout=900, cwd=D)
            out.append(f'$ {k}\n' + (r.stdout + r.stderr)[-6000:])
            if r.returncode != 0: out.append(f'{k} FAILED (exit {r.returncode}); later steps not run'); break
        return '\n'.join(out)
    r = subprocess.run(cmds[kind], capture_output=True, text=True, timeout=900, cwd=D)
    return (r.stdout + r.stderr)[-8000:] + f'\n(exit {r.returncode})'

def image_part(path):
    from PIL import Image
    im = Image.open(path).convert('RGB')
    if max(im.size) > 2400: im.thumbnail((2400, 2400))
    buf = io.BytesIO(); im.save(buf, 'PNG')
    return {'type': 'image_url', 'image_url': {'url': 'data:image/png;base64,' + base64.b64encode(buf.getvalue()).decode(), 'detail': 'high'}}

TOOLS = [
    {'name': 'read_file', 'description': 'Read a text file (your lesson folder or the engine). Long files: use offset/limit (lines).',
     'parameters': {'type': 'object', 'properties': {'path': {'type': 'string'}, 'offset': {'type': 'integer'}, 'limit': {'type': 'integer'}}, 'required': ['path']}},
    {'name': 'list_dir', 'description': 'List a folder.', 'parameters': {'type': 'object', 'properties': {'path': {'type': 'string'}}, 'required': ['path']}},
    {'name': 'write_file', 'description': 'Write a whole file in your lesson folder (the lesson .js or your .pron.json).',
     'parameters': {'type': 'object', 'properties': {'path': {'type': 'string'}, 'content': {'type': 'string'}}, 'required': ['path', 'content']}},
    {'name': 'edit_file', 'description': 'Replace one exact snippet (old must occur exactly once) in a file in your lesson folder.',
     'parameters': {'type': 'object', 'properties': {'path': {'type': 'string'}, 'old': {'type': 'string'}, 'new': {'type': 'string'}}, 'required': ['path', 'old', 'new']}},
    {'name': 'build', 'description': "Run the engine. kind: 'check' (renders every scene, lists TODOs, cue, digit and pronunciation problems), 'build' (silent HTML with estimated timing), 'sheet' (contact sheet sheet/sheet.png at 92% of each scene, frame PNGs, safe-area and play-through report), 'sheet40' (every scene mid-build in sheet40/), or 'all' (check, build, sheet; stops at the first failure). Takes 20-60 s.",
     'parameters': {'type': 'object', 'properties': {'kind': {'type': 'string', 'enum': ['check', 'build', 'sheet', 'sheet40', 'all']}}, 'required': ['kind']}},
    {'name': 'view_image', 'description': 'Look at a PNG (sheet/sheet.png, a frame in sheet/ or sheet40/, a calc frame). The image is shown to you in the next message.',
     'parameters': {'type': 'object', 'properties': {'path': {'type': 'string'}}, 'required': ['path']}},
    {'name': 'python', 'description': 'Run a short python snippet (for checking numbers). Prints stdout.',
     'parameters': {'type': 'object', 'properties': {'code': {'type': 'string'}}, 'required': ['code']}},
    {'name': 'finish', 'description': 'Call when the lesson is complete and you have looked at the final sheet: check clean, sheet clean, every picture right.',
     'parameters': {'type': 'object', 'properties': {'summary': {'type': 'string'}}, 'required': ['summary']}},
]

def run_tool(name, a, pending_images):
    if name == 'read_file':
        p = inside(a['path'], READ_ROOTS); lines = open(p, encoding='utf-8', errors='replace').read().split('\n')
        o = int(a.get('offset') or 0); n = int(a.get('limit') or 1500)
        body = '\n'.join(f'{i + 1}\t{l}' for i, l in enumerate(lines[o:o + n], o))
        return body[:60000] + (f'\n... ({len(lines)} lines in all)' if o + n < len(lines) or len(body) > 60000 else '')
    if name == 'list_dir':
        p = inside(a['path'], READ_ROOTS); return '\n'.join(sorted(os.listdir(p)))[:8000]
    if name == 'write_file':
        p = inside(a['path'], [D]); open(p, 'w', encoding='utf-8').write(a['content']); return f'wrote {len(a["content"])} chars to {p}'
    if name == 'edit_file':
        p = inside(a['path'], [D]); s = open(p, encoding='utf-8').read(); c = s.count(a['old'])
        if c != 1: return f'ERROR: old snippet occurs {c} times (must be exactly once); nothing changed'
        open(p, 'w', encoding='utf-8').write(s.replace(a['old'], a['new'])); return 'edited'
    if name == 'build': return build(a['kind'])
    if name == 'view_image':
        p = inside(a['path'], [D]); pending_images.append((p, image_part(p))); return f'image {os.path.relpath(p, D)} attached below'
    if name == 'python':
        r = subprocess.run([sys.executable, '-c', a['code']], capture_output=True, text=True, timeout=60)
        return (r.stdout + r.stderr)[-4000:]
    return 'unknown tool'

KITNOTE = ("; the picture kit and its helpers are described in the kit folder (read the LEAN.md helper table and the kit_bio.js usage lines; ignore the LEAN.md step limit, you work in full rounds)" if LBUILD else "")
SYSTEM = f"""You are a lesson writer for the University free n easy YouTube channel: short narrated, animated lessons for
B.Tech students who find textbooks hard. You work exactly like the channel's best writers: you read the rules and the
lesson, fill every TODO with care (narration, cues, short labels, the hook, every picture), build, LOOK at the contact
sheet and at single frames, find what is wrong or weak (late or missing text, empty or unclear pictures, overflow,
anything a student would find confusing), fix it, rebuild, and look again, until it is as good as you can make it.
Quality of teaching and of every picture comes first; take as many rounds as you need.

Your lesson: {NAME} in your folder {D}. Rules: WRITE.md in that folder (read it fully first){KITNOTE}. Field list of every scene kind: {ENGINE}/lesson_kinds.md.
Build with the build tool (silent builds only; the voice is recorded later). Work every number in python before you
voice it. No college or university names anywhere. When the check is clean, the sheet report is clean and you have
looked at the final sheet and the picture pages, call finish."""

def chat(messages):
    body = {'model': MODEL, 'messages': messages, 'tools': [{'type': 'function', 'function': t} for t in TOOLS],
            'max_tokens': int(os.environ.get('MAX_TOKENS', '32000'))}
    req = urllib.request.Request(BASE + '/chat/completions', data=json.dumps(body).encode(), method='POST',
                                 headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + KEY,
                                          'User-Agent': 'ufe-books-pipeline/1.0 (+https://github.com/SwathishThiyagu/ufe-books)'})
    for attempt in range(6):
        try:
            with urllib.request.urlopen(req, timeout=900) as r: return json.load(r)
        except urllib.error.HTTPError as e:
            err = e.read().decode(errors='replace')[:800]; log('api error', e.code, err)
            if e.code == 400 and 'reasoning' in err.lower():
                # the API wants the opposite reasoning_content handling: flip it and retry at once
                FLAGS['send_reasoning'] = not FLAGS['send_reasoning']
                for x in messages:
                    if not FLAGS['send_reasoning']: x.pop('reasoning_content', None)
                body['messages'] = messages
                req = urllib.request.Request(BASE + '/chat/completions', data=json.dumps(body).encode(), method='POST', headers=req.headers)
                continue
            time.sleep(20 * (attempt + 1))
        except Exception as e:
            log('api error', repr(e)[:300]); time.sleep(20 * (attempt + 1))
    raise SystemExit('API failed 6 times')

def main():
    messages = [{'role': 'system', 'content': SYSTEM}, {'role': 'user', 'content': 'Start: read WRITE.md and your lesson file, then work.'}]
    usage = {'prompt': 0, 'cache_hit': 0, 'completion': 0, 'steps': 0}
    done = False
    for step in range(STEPS):
        r = chat(messages); m = r['choices'][0]['message']; u = r.get('usage', {})
        usage['prompt'] += u.get('prompt_tokens', 0); usage['completion'] += u.get('completion_tokens', 0)
        usage['cache_hit'] += u.get('prompt_cache_hit_tokens', 0); usage['steps'] = step + 1
        msg = {'role': 'assistant', 'content': m.get('content') or ''}
        if m.get('tool_calls'): msg['tool_calls'] = m['tool_calls']
        if m.get('reasoning_content') and FLAGS['send_reasoning']: msg['reasoning_content'] = m['reasoning_content']
        messages.append(msg)
        if m.get('content'): log(f'[{step}] says:', m['content'][:600])
        calls = m.get('tool_calls') or []
        if not calls:
            messages.append({'role': 'user', 'content': 'Continue with the tools; call finish when the lesson is complete and you have looked at the final sheet.'}); continue
        pending = []
        for c in calls:
            fn = c['function']['name']
            try: a = json.loads(c['function'].get('arguments') or '{}')
            except Exception: a = {}
            if fn == 'finish':
                log(f'[{step}] FINISH:', a.get('summary', '')); done = True; res = 'ok'
            else:
                try: res = run_tool(fn, a, pending)
                except Exception as e: res = f'ERROR: {e}'
            log(f'[{step}] {fn}', json.dumps({k: (v[:120] if isinstance(v, str) else v) for k, v in a.items()})[:300], '->', str(res)[:300].replace('\n', ' | '))
            messages.append({'role': 'tool', 'tool_call_id': c['id'], 'content': str(res)})
        if pending:
            messages.append({'role': 'user', 'content': [{'type': 'text', 'text': 'Images you asked to see: ' + ', '.join(os.path.relpath(p, D) for p, _ in pending)}] + [part for _, part in pending]})
        # keep context in bounds: drop image payloads older than the last 3 image messages
        imgs = [i for i, x in enumerate(messages) if isinstance(x.get('content'), list)]
        for i in imgs[:-3]:
            messages[i] = {'role': 'user', 'content': messages[i]['content'][0]['text'] + ' (image removed to save space; view it again if needed)'}
        json.dump(usage, open(os.path.join(D, 'agent.usage.json'), 'w'))
        if done: break
    log('usage', json.dumps(usage))
    print(build('all')[-1500:])


if __name__ == '__main__':
    main()
