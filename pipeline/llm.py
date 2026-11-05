"""Call a free model and get JSON back.

Gemini (Google AI Studio free tier) is the default provider. The key comes from the
GEMINI_API_KEY environment variable (a GitHub Actions secret); it is never written to disk or logs.

    ask = LLM.from_env(log)                    # picks the best free models the key can use
    data = ask.json(task, system, prompt)      # returns a dict, retries on bad JSON, paces itself

When every model's daily free quota is used up it raises QuotaExhausted, and the runner saves
its progress and stops; the next run continues from the saved step.
"""
import json, os, re, time, random
import urllib.request, urllib.error

API = 'https://generativelanguage.googleapis.com/v1beta'


class QuotaExhausted(RuntimeError):
    pass


class ModelError(RuntimeError):
    pass


def _http(method, url, key, body=None, timeout=240):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method,
                                 headers={'Content-Type': 'application/json', 'x-goog-api-key': key})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, json.loads(r.read().decode('utf-8') or '{}')
    except urllib.error.HTTPError as e:
        try:
            payload = json.loads(e.read().decode('utf-8') or '{}')
        except Exception:
            payload = {}
        return e.code, payload
    except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
        return 0, {'error': {'message': str(e)}}


def parse_json(text):
    t = text.strip()
    t = re.sub(r'^```(?:json)?\s*|\s*```$', '', t)
    a, b = t.find('{'), t.rfind('}')
    if a >= 0 and b > a: t = t[a:b + 1]
    try:
        return json.loads(t, strict=False)          # strict=False: raw newlines/tabs inside strings are fine
    except json.JSONDecodeError:
        # code and formulas often carry backslashes that are not valid JSON escapes (\d, \s, \%); double them
        fixed = re.sub(r'\\(?![\\"/bfnrtu])', r'\\\\', t)
        fixed = re.sub(r',\s*([}\]])', r'\1', fixed)   # trailing commas
        return json.loads(fixed, strict=False)


def version_key(name):
    m = re.search(r'gemini-(\d+)(?:\.(\d+))?', name)
    return (int(m.group(1)), int(m.group(2) or 0)) if m else (0, 0)


class Gemini:
    """Free-tier Gemini with model rotation, pacing and retries."""

    def __init__(self, key, log, writer_models, reviewer_models, min_gap=6.5):
        self.key, self.log = key, log
        self.writer, self.reviewer = list(writer_models), list(reviewer_models)
        self.dead = set()               # models whose free quota is used up (or that are not free)
        self.last = {}                  # model -> time of last call
        self.min_gap = min_gap
        self.calls = 0; self.tokens_in = 0; self.tokens_out = 0

    @classmethod
    def from_env(cls, log):
        key = os.environ.get('GEMINI_API_KEY', '').strip()
        if not key:
            raise SystemExit('GEMINI_API_KEY is not set. Add it as a repository secret (Settings > Secrets and variables > Actions).')
        names = []
        st, js = _http('GET', f'{API}/models?pageSize=1000', key, timeout=60)
        if st == 200:
            for m in js.get('models', []):
                n = m.get('name', '').replace('models/', '')
                if 'generateContent' not in m.get('supportedGenerationMethods', []): continue
                if not re.match(r'gemini-\d', n) or version_key(n) < (2, 5): continue
                if re.search(r'lite|image|tts|audio|live|embedding|vision|thinking-exp|robotics|computer-use|customtools|learnlm|-8b|nano|veo|omni', n): continue
                names.append(n)
        else:
            log(f'could not list models (HTTP {st}): {js.get("error", {}).get("message", "")[:200]}')
        forced = [x.strip() for x in os.environ.get('GEMINI_MODELS', '').split(',') if x.strip()]
        if forced:
            names = forced
        if not names:
            names = ['gemini-2.5-flash', 'gemini-2.5-pro']
        # newest first; stable names before previews of the same version
        names = sorted(set(names), key=lambda n: (version_key(n), 'preview' not in n and 'exp' not in n, 'latest' not in n), reverse=True)
        flash = [n for n in names if 'flash' in n]
        pro = [n for n in names if 'pro' in n]
        writer = flash + pro
        reviewer = pro + flash
        log(f'models: writer {writer[:4]}, reviewer {reviewer[:4]}')
        return cls(key, log, writer, reviewer, float(os.environ.get('GEMINI_MIN_GAP', '6.5')))

    def _pick(self, role, busy=()):
        alive = [m for m in (self.reviewer if role == 'review' else self.writer) if m not in self.dead]
        if not alive:
            raise QuotaExhausted('every free model has used its quota for today')
        for m in alive:
            if m not in busy:
                return m
        return None          # every live model is overloaded right now

    def text(self, task, system, prompt, role='write', temperature=0.6, json_mode=True, max_tokens=32768):
        attempt = 0
        busy, fails, waited = set(), {}, 0.0
        while True:
            model = self._pick(role, busy)
            if model is None:            # all overloaded: wait, then try them all again
                if waited > 2400: raise ModelError(f'{task}: every model stayed overloaded for 40 minutes')
                self.log(f'  all models busy; waiting 90s'); time.sleep(90); waited += 90; busy.clear(); continue
            gap = time.time() - self.last.get(model, 0)
            if gap < self.min_gap:
                time.sleep(self.min_gap - gap)
            body = {'systemInstruction': {'parts': [{'text': system}]},
                    'contents': [{'role': 'user', 'parts': [{'text': prompt}]}],
                    'generationConfig': {'temperature': temperature, 'maxOutputTokens': max_tokens}}
            if json_mode:
                body['generationConfig']['responseMimeType'] = 'application/json'
            t0 = time.time()
            st, js = _http('POST', f'{API}/models/{model}:generateContent', self.key, body)
            self.last[model] = time.time()
            if st == 200:
                cands = js.get('candidates') or []
                parts = (cands[0].get('content') or {}).get('parts', []) if cands else []
                out = ''.join(p.get('text', '') for p in parts if not p.get('thought'))
                um = js.get('usageMetadata', {})
                self.calls += 1
                self.tokens_in += um.get('promptTokenCount', 0); self.tokens_out += um.get('candidatesTokenCount', 0) + um.get('thoughtsTokenCount', 0)
                fin = cands[0].get('finishReason') if cands else 'NO_CANDIDATE'
                self.log(f'  {task}: {model} {time.time() - t0:.0f}s in {um.get("promptTokenCount", 0)} out {um.get("candidatesTokenCount", 0)} ({fin})')
                if out.strip():
                    return out
                attempt += 1
                if attempt > 3: raise ModelError(f'{task}: empty reply ({fin})')
                continue
            err = js.get('error', {}) if isinstance(js, dict) else {}
            msg = str(err.get('message', ''))[:300]
            if st == 429:
                daily = 'PerDay' in json.dumps(err) or 'per day' in msg.lower() or 'limit: 0' in msg
                if daily:
                    self.log(f'  {model}: daily free quota used up or not free ({msg[:120]}); switching model')
                    self.dead.add(model)
                    continue
                delay = 30
                for d in err.get('details', []) or []:
                    if 'retryDelay' in d:
                        try: delay = float(str(d['retryDelay']).rstrip('s')) + 2
                        except ValueError: pass
                attempt += 1
                if attempt > 8:
                    self.dead.add(model); attempt = 0; continue
                self.log(f'  {model}: rate limited, waiting {delay:.0f}s'); time.sleep(delay); continue
            if st in (400, 403) and ('API key' in msg or 'API_KEY' in json.dumps(err)):
                raise SystemExit('The Gemini API key was refused. Check the GEMINI_API_KEY secret.')
            if st in (400, 404):
                self.log(f'  {model}: HTTP {st} {msg[:160]}; dropping this model'); self.dead.add(model); continue
            # 5xx, overload or network trouble: one quick retry, then move on to the next model
            fails[model] = fails.get(model, 0) + 1
            if fails[model] >= 2:
                self.log(f'  {model}: HTTP {st} {msg[:100]}; trying another model'); busy.add(model); continue
            wait = 10 + random.random() * 5
            self.log(f'  {model}: HTTP {st} {msg[:100]}; retry in {wait:.0f}s'); time.sleep(wait)

    def json(self, task, system, prompt, role='write', temperature=0.6, check=None):
        """Ask for JSON. `check(data)` may return a list of problems; they are sent back once or twice."""
        p = prompt
        for attempt in range(3):
            raw = self.text(task, system, p, role, temperature)
            self._last_raw = raw
            try:
                data = parse_json(raw)
            except (json.JSONDecodeError, ValueError) as e:
                self.log(f'  {task}: reply is not valid JSON ({e})')
                if attempt == 0:
                    p = prompt + f'\n\nYour last reply was not valid JSON ({e}). Reply with one complete JSON object only; keep tables short.'
                else:   # ask the model to repair its own broken JSON instead of writing it all again
                    p = ('The text below should be one JSON object but it is broken (' + str(e) + '). Some lines may be cut or missing. '
                         'Return the same content as one valid, complete JSON object; rewrite any damaged part so it is whole and correct.\n\n' + raw)
                continue
            probs = check(data) if check else []
            if not probs:
                return data
            soft = all(x.startswith('~') for x in probs)
            if attempt == 2 or (soft and attempt >= 1):
                self.log(f'  {task}: kept with problems: {probs[:3]}')
                return data
            p = (prompt + '\n\nYour last reply had these problems; fix all of them and reply with the whole JSON again:\n- '
                 + '\n- '.join(probs[:12]))
        try:
            os.makedirs('.free/bad', exist_ok=True); open(f'.free/bad/{task}.txt', 'w').write(getattr(self, '_last_raw', ''))
        except OSError: pass
        raise ModelError(f'{task}: no valid JSON after 3 tries')


class Mock:
    """Offline stand-in used for tests: answers come from a function (task, prompt) -> dict."""

    def __init__(self, fn, log):
        self.fn, self.log = fn, log
        self.calls = 0; self.tokens_in = 0; self.tokens_out = 0

    def json(self, task, system, prompt, role='write', temperature=0.6, check=None):
        self.calls += 1
        data = self.fn(task, prompt)
        probs = check(data) if check else []
        if probs: self.log(f'  {task}: mock reply has problems: {probs[:4]}')
        return data
