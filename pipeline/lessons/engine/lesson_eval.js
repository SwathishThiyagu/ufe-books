// Evaluate a lesson file with the engine (no browser) and print JSON: META, the scenes (kind, section, term, narration,
// pause, cues) and a render check of every scene with dummy cue times. usage: node lesson_eval.js lesson.js template.html
const vm = require('vm'), fs = require('fs');
const lesson = fs.readFileSync(process.argv[2], 'utf8');
const tpl = fs.readFileSync(process.argv[3], 'utf8');
const a = tpl.indexOf('__LESSON__') + '__LESSON__'.length, b = tpl.indexOf('</script>', a);
const engine = tpl.slice(a, b);
const ctx = { console, window: {}, document: {} };
vm.createContext(ctx);
const out = { ok: false, errors: [], scenes: [] };
try {
  vm.runInContext(lesson + '\n' + engine, ctx);
  vm.runInContext(`globalThis.__meta=JSON.stringify(META); globalThis.__scenes=JSON.stringify(SC.map((s,i)=>({i,k:s.k,s:s.s,term:s.term||'',say:s.say||'',pause:s.pause||0,line:s.line,cues:s.cues||{},joke:s.joke||''})));
    globalThis.__render=(i)=>{const sc=SC[i];if(!R[sc.k])throw new Error('no scene kind '+sc.k);const c=new Proxy({end:8},{get:(t,k)=>k in t?t[k]:1});return R[sc.k](sc,c,'u'+i)}`, ctx);
  out.meta = JSON.parse(ctx.__meta); out.scenes = JSON.parse(ctx.__scenes);
  for (let i = 0; i < out.scenes.length; i++) {
    try { const svg = vm.runInContext(`__render(${i})`, ctx); if (typeof svg !== 'string' || svg.length < 100) out.errors.push(`scene ${i + 1} (${out.scenes[i].k}) rendered nothing`);
      else if (/undefined|NaN/.test(svg)) out.errors.push(`scene ${i + 1} (${out.scenes[i].k}) has "undefined" or NaN in its drawing`); }
    catch (e) { out.errors.push(`scene ${i + 1} (${out.scenes[i].k}): ${String(e).slice(0, 160)}`); }
  }
  out.ok = out.errors.length === 0;
} catch (e) { out.errors.push('lesson file does not load: ' + String(e).slice(0, 300)); }
console.log(JSON.stringify(out));
