// Evaluate a lesson file with the engine (no browser) and print JSON: META, the scenes (kind, section, term, narration,
// pause, cues) and a render check of every scene with dummy cue times. usage: node lesson_eval.js lesson.js template.html
const vm = require('vm'), fs = require('fs');
const lesson = fs.readFileSync(process.argv[2], 'utf8');
const tpl = fs.readFileSync(process.argv[3], 'utf8');
const a = tpl.indexOf('__LESSON__') + '__LESSON__'.length, b = tpl.indexOf('</script>', a);
const engine = tpl.slice(a, b).replace("if(typeof EXTRA==='function')EXTRA(R,ICON);", "globalThis.__builtin=Object.keys(ICON);if(typeof EXTRA==='function')EXTRA(R,ICON);");
// the words a scene shows: every <text>, split into screen text and code text (a monospace font or a code class on it or a parent)
const ent = t => t.replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;|&apos;/g, "'").replace(/&#(\d+);/g, (m, d) => String.fromCharCode(+d)).replace(/&#x([0-9a-f]+);/gi, (m, h) => String.fromCharCode(parseInt(h, 16))).replace(/&amp;/g, '&');
function texts(svg) {
  const screen = [], code = [], st = []; let cur = null, depth = 0;
  const re = /<(\/?)([a-zA-Z][\w:-]*)([^>]*?)(\/?)>|([^<]+)/g; let m;
  while ((m = re.exec(svg))) {
    if (m[5] !== undefined) { if (cur) cur.t += m[5]; continue; }
    const [, close, tag, attrs, self] = m;
    if (close) { const top = st.pop(); if (tag === 'text' && cur && st.filter(x => x.tag === 'text').length === 0) { const t = ent(cur.t).replace(/\s+/g, ' ').trim(); if (t) (cur.mono ? code : screen).push(t); cur = null; } continue; }
    const mono = /font-family\s*[:=]\s*["']?[^;"'>]*(mono|consolas|courier)|class=["'][^"']*\bcode/i.test(attrs) || (st.length && st[st.length - 1].mono);
    if (self) continue;
    st.push({ tag, mono });
    if (tag === 'text' && !cur) cur = { t: '', mono };
    else if (cur && tag === 'tspan' && /\bdx=|\bx=/.test(attrs)) cur.t += ' ';
  }
  return { screen, code };
}
const ctx = { console, window: {}, document: {} };
vm.createContext(ctx);
const out = { ok: false, errors: [], scenes: [] };
try {
  vm.runInContext(lesson + '\n' + engine, ctx);
  vm.runInContext(`globalThis.__meta=JSON.stringify(META); globalThis.__scenes=JSON.stringify(SC.map((s,i)=>({i,k:s.k,s:s.s,term:s.term||'',say:s.say||'',pause:s.pause||0,line:s.line,cues:s.cues||{},joke:s.joke||''})));
    globalThis.__render=(i)=>{const sc=SC[i];if(!R[sc.k])throw new Error('no scene kind '+sc.k);const c=new Proxy({end:8},{get:(t,k)=>k in t?t[k]:1});return R[sc.k](sc,c,'u'+i)}`, ctx);
  out.meta = JSON.parse(ctx.__meta); out.scenes = JSON.parse(ctx.__scenes);
  out.builtin_icons = ctx.__builtin || [];
  vm.runInContext(`globalThis.__icons=JSON.stringify(SC.map(s=>s.k==='recap'&&Array.isArray(s.panels)?s.panels.map(p=>typeof p[2]==='string'?p[2]:''):[]))`, ctx);
  JSON.parse(ctx.__icons).forEach((ics, i) => { if (ics.length) out.scenes[i].icons = ics; });
  for (let i = 0; i < out.scenes.length; i++) {
    try { const svg = vm.runInContext(`__render(${i})`, ctx); if (typeof svg !== 'string' || svg.length < 100) out.errors.push(`scene ${i + 1} (${out.scenes[i].k}) rendered nothing`);
      else if (/undefined|NaN/.test(svg)) out.errors.push(`scene ${i + 1} (${out.scenes[i].k}) has "undefined" or NaN in its drawing`);
      if (typeof svg === 'string') Object.assign(out.scenes[i], texts(svg)); }
    catch (e) { out.errors.push(`scene ${i + 1} (${out.scenes[i].k}): ${String(e).slice(0, 160)}`); }
  }
  out.ok = out.errors.length === 0;
} catch (e) { out.errors.push('lesson file does not load: ' + String(e).slice(0, 300)); }
console.log(JSON.stringify(out));
