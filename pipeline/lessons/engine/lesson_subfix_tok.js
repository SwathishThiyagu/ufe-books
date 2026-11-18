// lesson_subfix_tok.js <lesson.js> <skip.json>: helper for lesson_subfix.py. Prints the lesson with on-screen underscore
// subscripts in quoted strings turned into sub tspans (narration strings, after a say: key, are left alone).
const fs = require('fs'); let acorn;
for (const p of ['acorn', '/opt/node-tools/node_modules/acorn']) { try { acorn = require(p); break; } catch (e) {} }
if (!acorn) { console.error('lesson_subfix needs acorn (npm i acorn)'); process.exit(2); }
const src = fs.readFileSync(process.argv[2], 'utf8'), UNDO_MODE = process.argv[3] === '--undo';
const skip = UNDO_MODE ? new Set() : new Set(JSON.parse(fs.readFileSync(process.argv[3], 'utf8')));
// this tool's own sub tspan, as written into a '...' or "..." string (attributes tab-separated, quotes plain or escaped)
const UNDO = /([A-Za-zα-ωΑ-Ω]{1,2})<tspan\\tdy=(\\?["'])\.28em\2\\tfont-size=\2\.62em\2>([^<]*)<\/tspan><tspan\\tdy=\2-\.28em\2>\\u200b<\/tspan>/g;
const TOK = /(?<![\w.$])(?<!->)(?![A-Z]{2}_[A-Z]{2})(?![a-z]{2}_[a-z]{3})([A-Za-zα-ωΑ-Ω]{1,2})_(\{[^}]*\}|[A-Za-z0-9]{1,6})(?![\w(])/g;
const toks = [...acorn.tokenizer(src, { ecmaVersion: 'latest', allowHashBang: true })];
// names the JS itself uses (ICON.q_graph, a field st_mtime) are identifiers, never subscripts
const names = new Set(toks.filter(t => t.type.label === 'name').map(t => t.value));
let out = '', i = 0, n = 0;
toks.forEach((t, k) => {
  if (t.type.label !== 'string') return;
  const q = src[t.start]; if (q !== "'" && q !== '"') return;
  const say = k >= 2 && toks[k - 1].type.label === ':' && toks[k - 2].value === 'say';
  const body = src.slice(t.start + 1, t.end - 1);
  if (UNDO_MODE) { if (say) return; UNDO.lastIndex = 0; if (!UNDO.test(body)) return; UNDO.lastIndex = 0;
    const nb = body.replace(UNDO, (m, b, q2, s) => { n++; return b + '_' + (/^[A-Za-z0-9]{1,6}$/.test(s) ? s : '{' + s + '}'); });
    out += src.slice(i, t.start + 1) + nb; i = t.end - 1; return; }
  if (say || !TOK.test(body)) return; TOK.lastIndex = 0;
  const a = q === '"' ? '\\"' : '"';
  const nb = body.replace(TOK, (m, b, s, at) => { if (skip.has(m)) return m; n++; s = s.replace(/^\{|\}$/g, '');
    return `${b}<tspan\\tdy=${a}.28em${a}\\tfont-size=${a}.62em${a}>${s}</tspan><tspan\\tdy=${a}-.28em${a}>\\u200b</tspan>`; });
  out += src.slice(i, t.start + 1) + nb; i = t.end - 1;
});
out += src.slice(i);
process.stdout.write(JSON.stringify({ n, src: out, names: [...names] }));
