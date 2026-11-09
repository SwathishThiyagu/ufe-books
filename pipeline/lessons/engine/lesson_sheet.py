#!/usr/bin/env python3
"""Contact sheet, safe-area check, calc frames and play-through check for a built lesson.
usage: python3 lesson_sheet.py lesson.html outdir [--at 0.92] [--frames] [--play]
Opens the lesson with ?render in Playwright's Chromium, renders every scene at a fraction of its length, screenshots the stage
(outdir/Lnn.png, outdir/sheet.png) and reports page errors, cue failures and every piece of text that sits outside the safe
area (20 px inside the 1600 x 900 page) or is wider than the page.
  --frames  also renders every calc scene (and every pa with a calc) at 0.25, 0.5, 0.75 and 0.97 of its length (outdir/calc_Lnn_25.png ...;
            nn is the 0-based scene index, the same numbering as the Lnn.png frames)
  --play    opens the lesson without ?render, seeks to 1.5 s before the first question's narration ends and plays 6 s: playback
            must still be running, the scene must have moved on, and nothing may sit over the stage
Exit code 1 when anything is wrong."""
import sys, os, json, subprocess, tempfile
html, outdir = os.path.abspath(sys.argv[1]), sys.argv[2]
at = float(sys.argv[sys.argv.index('--at') + 1]) if '--at' in sys.argv else 0.92
FRAMES, PLAY = '--frames' in sys.argv, '--play' in sys.argv
os.makedirs(outdir, exist_ok=True)
JS = r"""
const { chromium } = require('playwright');
(async () => {
  const [html, outdir, at] = process.argv.slice(2);
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1280, height: 760 } });
  const errs = []; p.on('pageerror', e => errs.push(String(e)));
  await p.goto('file://' + html + '?render'); await p.waitForTimeout(1500);
  const starts = await p.evaluate(() => window.__T), total = await p.evaluate(() => window.__TOTAL || 0);
  const over = [];
  for (let i = 0; i < starts.length; i++) {
    const len = (starts[i + 1] != null ? starts[i + 1] : total) - starts[i];
    const t = starts[i] + Math.max(0.6, len * +at);
    await p.evaluate(tt => window.__frame(tt), t); await p.waitForTimeout(120);
    const bad = await p.evaluate((i) => {
      const st = document.getElementById('stage').getBoundingClientRect(), sx = 1600 / st.width, sy = 900 / st.height, out = [];
      document.querySelectorAll('.scene.now svg.cv text').forEach(el => {
        if (el.checkVisibility && !el.checkVisibility({ opacityProperty: true, visibilityProperty: true })) return;
        const r = el.getBoundingClientRect(); if (!r.width) return;
        const x0 = (r.left - st.left) * sx, y0 = (r.top - st.top) * sy, x1 = (r.right - st.left) * sx, y1 = (r.bottom - st.top) * sy;
        if (x0 < 20 || y0 < 20 || x1 > 1580 || y1 > 880) out.push({ scene: i + 1, text: (el.textContent || '').trim().slice(0, 50), box: [x0, y0, x1, y1].map(v => Math.round(v)) });
      });
      return out;
    }, i);
    over.push(...bad);
    await p.locator('#stage').screenshot({ path: `${outdir}/L${String(i).padStart(2, '0')}.png` });
  }
  const cuefail = await p.evaluate(() => window.__CUEFAIL || []);
  const kinds = await p.evaluate(() => SC.map(s => s.k + (s.calc ? '+calc' : '')));
  const bump = await p.evaluate(() => window.__bumper ? [window.__bumper.INTRO || window.__bumper.DUR_IN || 0, window.__bumper.DUR_OUT] : [0, 0]);
  const bframes = [].concat(bump[0] ? [['B_in1', 1.0], ['B_in2', bump[0] - 1.2]] : [], bump[1] ? [['B_out1', total - bump[1] + 1.4], ['B_out2', total - 0.4]] : []);
  for (const [name, t] of bframes) {
    await p.evaluate(tt => window.__frame(tt), t); await p.waitForTimeout(250); await p.locator('#stage').screenshot({ path: `${outdir}/${name}.png` }); }
  let frames = 0;
  if (process.argv[5] === '1') for (let i = 0; i < starts.length; i++) {
    if (!/calc/.test(kinds[i])) continue;
    const len = (starts[i + 1] != null ? starts[i + 1] : total) - starts[i];
    for (const f of [0.25, 0.5, 0.75, 0.97]) { await p.evaluate(tt => window.__frame(tt), starts[i] + len * f); await p.waitForTimeout(100);
      await p.locator('#stage').screenshot({ path: `${outdir}/calc_L${String(i).padStart(2, '0')}_${Math.round(f * 100)}.png` }); frames++; }
  }
  let play = null;
  if (process.argv[6] === '1') {
    const b2 = await chromium.launch({ args: ['--autoplay-policy=no-user-gesture-required'] }); const q = await b2.newPage({ viewport: { width: 1280, height: 760 } });
    const perr = []; q.on('pageerror', e => perr.push(String(e)));
    await q.goto('file://' + html); await q.waitForTimeout(1500);
    const qi = kinds.findIndex(k => k.startsWith('pq'));
    if (qi >= 0) {
      const lineEnd = await q.evaluate(i => (DATA.lines[i] || {}).end, qi);
      await q.evaluate(t => { window.__player.seek(t); window.__player.play(); }, lineEnd - 1.5); await q.waitForTimeout(6000);
      const r = await q.evaluate(() => { const st = document.getElementById('stage'); const over = [...st.querySelectorAll('*')].filter(e => !e.closest('.scene') && !e.classList.contains('cc') && !e.classList.contains('scene') && e.id !== 'layer' && e.id !== 'bumpSvg' && getComputedStyle(e).display !== 'none' && /absolute|fixed/.test(getComputedStyle(e).position)).map(e => e.tagName + (e.className ? '.' + e.className : ''));
        return { playing: window.__player.isPlaying(), now: window.__player.now(), scene: window.__player.sceneAt(window.__player.now()), over }; });
      play = { question: qi + 1, ...r, errors: perr, ok: r.playing && r.scene > qi && !r.over.length && !perr.length };
    } else play = { ok: true, note: 'no pq scene' };
    await b2.close();
  }
  console.log(JSON.stringify({ scenes: starts.length, errors: errs, cuefail, overflow: over, frames, play, bump }));
  await b.close();
})();
"""
js = os.path.join(tempfile.gettempdir(), 'lesson_sheet_run.js'); open(js, 'w').write(JS)
r = subprocess.run(['node', js, html, outdir, str(at), '1' if FRAMES else '0', '1' if PLAY else '0'], capture_output=True, text=True)
if r.returncode != 0: sys.exit('playwright failed: ' + r.stderr[-1200:])
rep = json.loads(r.stdout.strip().splitlines()[-1])
from PIL import Image
import glob
ims = [Image.open(f) for f in sorted(glob.glob(os.path.join(outdir, 'B_in*.png'))) + sorted(glob.glob(os.path.join(outdir, 'L*.png'))) + sorted(glob.glob(os.path.join(outdir, 'B_out*.png')))]
w, h = ims[0].size; cols = 3; rows = (len(ims) + cols - 1) // cols; sc = 0.34; tw, th = int(w * sc), int(h * sc)
sheet = Image.new('RGB', (tw * cols, th * rows), 'white')
for k, im in enumerate(ims): sheet.paste(im.resize((tw, th)), ((k % cols) * tw, (k // cols) * th))
sheet.save(os.path.join(outdir, 'sheet.png'))
print(f"{rep['scenes']} scenes" + (f" + bumper {rep['bump'][0]:g} s in / {rep['bump'][1]:g} s out" if any(rep.get('bump', [0, 0])) else '') + f" -> {outdir}/sheet.png; page errors {len(rep['errors'])}; cue failures {len(rep['cuefail'])}; text outside the safe area: {len(rep['overflow'])}")
for e in rep['errors']: print('  error:', e[:160])
for c in rep['cuefail'][:20]: print('  cue:', c)
for o in rep['overflow'][:40]: print(f"  scene {o['scene']}: \"{o['text']}\" at {o['box']}")
if rep.get('frames'): print(f"  calc frames: {rep['frames']} written (calc_Lnn_25/50/75/97.png): look at them, the rows must transform")
bad_play = False
if rep.get('play') is not None:
    pl = rep['play']; bad_play = not pl.get('ok')
    print(('  play-through OK: ' if pl.get('ok') else '  PLAY-THROUGH FAILED: ') + (pl.get('note') or f"question {pl.get('question')} -> scene {pl.get('scene', 0) + 1}, playing {pl.get('playing')}, over the stage: {pl.get('over')}, errors {pl.get('errors')}"))
sys.exit(1 if rep['errors'] or rep['cuefail'] or rep['overflow'] or bad_play else 0)
