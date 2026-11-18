// lesson_subfix_tok.js <lesson.js> <skip.json>: helper for lesson_subfix.py. Prints the lesson with on-screen underscore
// subscripts in quoted strings, and in the text runs of template literals, turned into sub tspans (narration, after a
// say: key, is left alone).
const fs = require('fs'); let acorn;
for (const p of ['acorn', '/opt/node-tools/node_modules/acorn']) { try { acorn = require(p); break; } catch (e) {} }
if (!acorn) { console.error('lesson_subfix needs acorn (npm i acorn)'); process.exit(2); }
const src = fs.readFileSync(process.argv[2], 'utf8'), UNDO_MODE = process.argv[3] === '--undo';
const skip = UNDO_MODE ? new Set() : new Set(JSON.parse(fs.readFileSync(process.argv[3], 'utf8')));
// this tool's own sub tspan, as written into a '...' or "..." string (attributes tab-separated, quotes plain or escaped)
const UNDO = /([A-Za-zα-ωΑ-Ω]{1,2})<tspan\\tdy=(\\?["'])\.28em\2\\tfont-size=\2\.62em\2>([^<]*)<\/tspan><tspan\\tdy=\2-\.28em\2>\\u200b<\/tspan>/g;
const TOK = /(?<![\w.$])(?<!->)(?![A-Z]{2}_[A-Z]{3})(?![a-z]{2}_[a-z]{3})([A-Za-zα-ωΑ-Ω]{1,2})_(\{[^}]*\}|[A-Za-z0-9]{1,6})(?!\w)/g;
const toks = [...acorn.tokenizer(src, { ecmaVersion: 'latest', allowHashBang: true })];
// a string that is only a name the JS uses ('q_graph' for ICON.q_graph) is an id, never a subscript
const names = new Set(toks.filter(t => t.type.label === 'name').map(t => t.value));
let out = '', i = 0, n = 0;
// template literals: only the text outside tags (SVG text runs, plain text), never inside a say: template
const stack = [];
const tspan = (b, s, a) => `${b}<tspan\\tdy=${a}.28em${a}\\tfont-size=${a}.62em${a}>${s}</tspan><tspan\\tdy=${a}-.28em${a}>\\u200b</tspan>`;
const OWN = /^<tspan\\tdy=(\\?["'])\.28em\1\\tfont-size=\1\.62em\1>[^<]*<\/tspan><tspan\\tdy=\1-\.28em\1>\\u200b<\/tspan>/;
function tplChunk(t, top) {
  const raw = src.slice(t.start, t.end); let res = '', seg = '', inTag = top.inTag;
  const flush = () => { if (!seg) return;
    if (UNDO_MODE) res += seg.replace(UNDO, (m, b, q2, s) => { n++; return b + '_' + (/^[A-Za-z0-9]{1,6}$/.test(s) ? s : '{' + s + '}'); });
    else res += seg.replace(TOK, (m, b, s2) => { if (skip.has(m)) return m; n++; return tspan(b, s2.replace(/^\{|\}$/g, ''), '"'); });
    seg = ''; };
  for (let c = 0; c < raw.length; c++) { const ch = raw[c];
    if (!inTag && ch === '<' && /[A-Za-z\/!]/.test(raw[c + 1] || '')) {
      const own = raw.slice(c).match(OWN);   // our own sub tspan counts as text, so undo sees it whole
      if (own) { seg += own[0]; c += own[0].length - 1; continue; }
      flush(); inTag = true; res += ch; continue; }
    if (inTag) { res += ch; if (ch === '>') inTag = false; continue; }
    seg += ch; }
  flush(); top.inTag = inTag;
  if (res !== raw) { out += src.slice(i, t.start) + res; i = t.end; }
}
toks.forEach((t, k) => {
  const lab = t.type.label;
  if (lab === '`') { if (stack.length && stack[stack.length - 1].kind === 'tpl') stack.pop();
    else stack.push({ kind: 'tpl', inTag: false, say: k >= 2 && toks[k - 1].type.label === ':' && toks[k - 2].value === 'say' }); return; }
  if (lab === '${') { stack.push({ kind: 'expr' }); return; }
  if (lab === '{') { stack.push({ kind: 'brace' }); return; }
  if (lab === '}') { stack.pop(); return; }
  if (lab === 'template') { const top = stack[stack.length - 1];
    if (top && top.kind === 'tpl' && !stack.some(e => e.say)) tplChunk(t, top); return; }
  if (t.type.label !== 'string') return;
  const q = src[t.start]; if (q !== "'" && q !== '"') return;
  const say = k >= 2 && toks[k - 1].type.label === ':' && toks[k - 2].value === 'say';
  const body = src.slice(t.start + 1, t.end - 1);
  if (UNDO_MODE) { if (say) return; UNDO.lastIndex = 0; if (!UNDO.test(body)) return; UNDO.lastIndex = 0;
    const nb = body.replace(UNDO, (m, b, q2, s) => { n++; return b + '_' + (/^[A-Za-z0-9]{1,6}$/.test(s) ? s : '{' + s + '}'); });
    out += src.slice(i, t.start + 1) + nb; i = t.end - 1; return; }
  if (say || !TOK.test(body)) return; TOK.lastIndex = 0;
  const a = q === '"' ? '\\"' : '"';
  const nb = body.replace(TOK, (m, b, s, at) => { if (skip.has(m) || (names.has(m) && body.trim() === m)) return m; n++; s = s.replace(/^\{|\}$/g, '');
    return `${b}<tspan\\tdy=${a}.28em${a}\\tfont-size=${a}.62em${a}>${s}</tspan><tspan\\tdy=${a}-.28em${a}>\\u200b</tspan>`; });
  out += src.slice(i, t.start + 1) + nb; i = t.end - 1;
});
out += src.slice(i);
process.stdout.write(JSON.stringify({ n, src: out, names: [...names] }));
