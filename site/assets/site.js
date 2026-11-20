/* Inner pages: tap-to-play video, "mark as done" (saved on the device only), search. No libraries. */
(function () {
  'use strict';
  function store(key, val) {
    try {
      if (val === undefined) { return JSON.parse(window.localStorage.getItem(key) || 'null'); }
      window.localStorage.setItem(key, JSON.stringify(val));
    } catch (e) { /* private mode or blocked storage: progress is simply not kept */ }
    return null;
  }

  /* video: nothing from YouTube loads until the student taps play */
  var players = document.querySelectorAll('[data-video]');
  Array.prototype.forEach.call(players, function (box) {
    var btn = box.querySelector('button');
    if (!btn) { return; }
    btn.addEventListener('click', function () {
      var f = document.createElement('iframe');
      f.src = 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(box.getAttribute('data-video')) + '?autoplay=1&rel=0';
      f.title = box.getAttribute('data-title') || 'Lesson video';
      f.allow = 'accelerometer; autoplay; encrypted-media; picture-in-picture; fullscreen';
      f.allowFullscreen = true;
      f.referrerPolicy = 'strict-origin-when-cross-origin';
      box.textContent = '';
      box.appendChild(f);
    });
  });

  /* mark as done */
  var done = store('ufe.done.v1') || {};
  function paint() {
    Array.prototype.forEach.call(document.querySelectorAll('[data-done-id]'), function (el) {
      var on = !!done[el.getAttribute('data-done-id')];
      if (el.tagName === 'BUTTON') {
        el.setAttribute('aria-pressed', on ? 'true' : 'false');
        el.querySelector('span').textContent = on ? 'Done' : 'Mark as done';
      } else {
        el.classList.toggle('is-done', on);
      }
    });
    Array.prototype.forEach.call(document.querySelectorAll('[data-progress]'), function (el) {
      var ids = el.getAttribute('data-progress').split(' ').filter(Boolean), n = 0;
      ids.forEach(function (id) { if (done[id]) { n++; } });
      var bar = el.querySelector('i'), txt = el.querySelector('span');
      if (bar) { bar.style.width = (ids.length ? Math.round(n * 100 / ids.length) : 0) + '%'; }
      if (txt) { txt.textContent = n + ' of ' + ids.length + ' lessons done. Saved on this device, no account needed.'; }
    });
  }
  Array.prototype.forEach.call(document.querySelectorAll('button[data-done-id]'), function (b) {
    b.addEventListener('click', function () {
      var id = b.getAttribute('data-done-id');
      if (done[id]) { delete done[id]; } else { done[id] = 1; }
      store('ufe.done.v1', done);
      paint();
    });
  });
  paint();

  /* search page */
  var q = document.getElementById('q'), out = document.getElementById('results');
  if (q && out) {
    var IDX = null, loading = false, timer;
    var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
    var load = function (cb) {
      if (IDX) { return cb(); }
      if (loading) { return; }
      loading = true;
      fetch('/search.json').then(function (r) { return r.json(); }).then(function (j) { IDX = j; loading = false; cb(); })
        .catch(function () { loading = false; out.innerHTML = '<p class="muted">The search index did not load. Try the degree directory.</p>'; });
    };
    var run = function () {
      var s = q.value.trim().toLowerCase();
      if (s.length < 2) { out.innerHTML = ''; return; }
      load(function () {
        var toks = s.split(/[^a-z0-9+#.]+/).filter(Boolean), hits = [];
        IDX.items.forEach(function (it) { /* [subject index, topic, chapter title, match words, lesson url or ''] */
          var sub = IDX.subjects[it[0]], title = it[2].toLowerCase(), m = it[3], un = it[1].toLowerCase(), sn = sub[0].toLowerCase(), sc = 0, found = 0;
          toks.forEach(function (t) {
            var f = false;
            if (title.indexOf(t) >= 0) { sc += 3; f = true; } else if (m.indexOf(t) >= 0) { sc += 2; f = true; }
            if (sn.indexOf(t) >= 0 || sub[2].indexOf(t) >= 0) { sc += 1; f = true; }
            if (un.indexOf(t) >= 0) { sc += 1.5; f = true; }
            if (f) { found++; }
          });
          if (title.indexOf(s) >= 0) { sc += 4; } else if (m.indexOf(s) >= 0 || un.indexOf(s) >= 0) { sc += 3; }
          if (toks.length > 1 && found < toks.length) { sc *= 0.35; }
          if (sc > 0) { hits.push([sc + (it[4] ? 1 : 0), it]); }
        });
        hits.sort(function (a, b) { return b[0] - a[0]; });
        hits = hits.slice(0, 30);
        if (!hits.length) { out.innerHTML = '<p class="muted">Nothing matched. Try another word from your syllabus, or browse the degree directory.</p>'; return; }
        out.innerHTML = hits.map(function (h) {
          var it = h[1], sub = IDX.subjects[it[0]];
          return '<a class="row" href="' + esc(it[4] || sub[1]) + '"><span><strong>' + esc(it[2]) + '</strong><small>' + esc(sub[0]) + ' · ' + esc(it[1]) + '</small></span><span class="tag' + (it[4] ? ' live' : '') + '">' + (it[4] ? 'Lesson' : 'Topic') + '</span></a>';
        }).join('');
      });
    };
    q.addEventListener('input', function () { clearTimeout(timer); timer = setTimeout(run, 120); });
    try { var pre = new URLSearchParams(window.location.search).get('q'); if (pre) { q.value = pre; } } catch (e) { /* old browser */ }
    if (q.value) { run(); }
  }
})();
