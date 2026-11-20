/* Home page: scroll-driven scenes. No libraries. Every moving element reads a CSS variable
   (--p through-scroll, --q pinned-scroll, --v rise, --f focus, --c covered) that this script sets.
   With "reduce motion" on, nothing is set and the CSS fallbacks show a settled page. */
(function () {
  'use strict';
  var root = document.getElementById('ufe-root');
  if (!root) { return; }
  var calm = !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  var cur = {}, lastVh = 0, theme = '', t0 = Date.now(), pts = [], i;
  for (i = 0; i < 620; i++) {
    var y = 1 - (i / 619) * 2, rad = Math.sqrt(1 - y * y), th = i * 2.399963;
    pts.push([Math.cos(th) * rad, y, Math.sin(th) * rad, (i % 23 === 0) ? 1 : 0]);
  }
  function clamp(v) { return v < 0 ? 0 : (v > 1 ? 1 : v); }
  function ease(key, target) {
    var c = cur[key];
    if (c === undefined) { c = target; }
    c += (target - c) * 0.16;
    if (Math.abs(target - c) < 0.0006) { c = target; }
    cur[key] = c;
    return c;
  }
  var scenes = root.querySelectorAll('.ufe-scene');
  var rise = root.querySelectorAll('.ufe-rise');
  var foc = root.querySelectorAll('.ufe-focus');
  var st = root.querySelectorAll('.ufe-stack');
  var nav = document.getElementById('ufe-nav');
  var globe = document.getElementById('ufe-globe');

  function drawGlobe(a) {
    if (!globe || !globe.getContext) { return; }
    var r = globe.getBoundingClientRect();
    if (r.bottom < -50 || r.top > window.innerHeight + 50) { return; }
    var g = globe.getContext('2d'), w = globe.width, h = globe.height, R = w * 0.44, k, pt;
    g.clearRect(0, 0, w, h);
    var ca = Math.cos(a), sa = Math.sin(a), ct = Math.cos(0.38), stl = Math.sin(0.38);
    for (k = 0; k < pts.length; k++) {
      pt = pts[k];
      var x = pt[0] * ca + pt[2] * sa, z = -pt[0] * sa + pt[2] * ca;
      var yy = pt[1] * ct - z * stl; z = pt[1] * stl + z * ct;
      var d = (z + 1) / 2;
      g.globalAlpha = 0.12 + d * 0.78;
      g.fillStyle = pt[3] ? '#F4D884' : '#D2E0D7';
      g.beginPath();
      g.arc(w / 2 + x * R, h / 2 + yy * R, (pt[3] ? 2.2 : 1.1) + d * (pt[3] ? 3.2 : 1.5), 0, 6.2832);
      g.fill();
    }
    g.globalAlpha = 1;
  }

  function frame() {
    var vh = Math.max(560, Math.min(window.innerHeight, 1000));
    if (vh !== lastVh) {
      root.style.setProperty('--vh', vh + 'px');
      root.style.setProperty('--run', calm ? '0px' : (window.innerWidth < 760 ? '520px' : '900px'));
      lastVh = vh;
    }
    var k, el, r, now = 'light', scrollP = 0;
    for (k = 0; k < scenes.length; k++) {
      el = scenes[k];
      r = el.getBoundingClientRect();
      if (r.top <= 70 && r.bottom > 70) { now = el.getAttribute('data-nav') || 'light'; }
      if (calm) { continue; }
      var p = clamp((vh - r.top) / (r.height + vh));
      var q = clamp(-r.top / Math.max(1, r.height - vh));
      el.style.setProperty('--p', ease('p' + k, p).toFixed(4));
      el.style.setProperty('--q', ease('q' + k, q).toFixed(4));
      if (el.id === 'degrees') { scrollP = p; }
    }
    if (!calm) {
      for (k = 0; k < rise.length; k++) {
        r = rise[k].getBoundingClientRect();
        rise[k].style.setProperty('--v', ease('v' + k, clamp((vh * 0.96 - r.top) / (vh * 0.3))).toFixed(4));
      }
      for (k = 0; k < foc.length; k++) {
        r = foc[k].getBoundingClientRect();
        var mid = r.top + r.height / 2;
        foc[k].style.setProperty('--f', ease('f' + k, clamp(1.25 - Math.abs(mid - vh / 2) / (vh * 0.4))).toFixed(4));
      }
      for (k = 0; k < st.length; k++) {
        var c = 0;
        if (k + 1 < st.length) {
          r = st[k].getBoundingClientRect();
          var nr = st[k + 1].getBoundingClientRect();
          c = clamp((r.bottom - nr.top) / Math.max(1, r.height));
        }
        st[k].style.setProperty('--c', ease('c' + k, c).toFixed(4));
      }
    }
    if (nav && theme !== now) {
      nav.style.setProperty('--nb', now === 'dark' ? 'rgba(19,38,30,0.94)' : (now === 'pale' ? '#FFFFFF' : '#FCFCF6'));
      nav.style.setProperty('--nf', now === 'dark' ? '#F4F6E9' : '#182E27');
      nav.style.setProperty('--nl', now === 'dark' ? 'rgba(244,246,233,0.22)' : 'rgba(24,46,39,0.14)');
      theme = now;
    }
    drawGlobe(calm ? 0.6 : (Date.now() - t0) / 1000 * 0.12 + scrollP * 2.4);
    if (!calm) { window.requestAnimationFrame(frame); }
  }
  frame();
  if (calm) { window.addEventListener('scroll', frame, { passive: true }); }

  /* degree directory: pick a degree, see its courses */
  var cards = root.querySelectorAll('[data-degree]');
  var lists = root.querySelectorAll('[data-degree-list]');
  var title = document.getElementById('ufe-degree-title');
  var at = 0;
  function show(n) {
    at = (n + cards.length) % cards.length;
    for (var k = 0; k < cards.length; k++) {
      var on = k === at;
      cards[k].setAttribute('aria-pressed', on ? 'true' : 'false');
      cards[k].style.boxShadow = on ? '0 0 0 4px #F4D884, 0 18px 40px rgba(0,0,0,0.35)' : 'none';
      lists[k].hidden = !on;
    }
    if (title) { title.textContent = cards[at].getAttribute('data-degree'); }
  }
  for (i = 0; i < cards.length; i++) {
    (function (n) { cards[n].addEventListener('click', function () { show(n); }); })(i);
  }
  var prev = document.getElementById('ufe-degree-prev'), next = document.getElementById('ufe-degree-next');
  if (prev) { prev.addEventListener('click', function () { show(at - 1); }); }
  if (next) { next.addEventListener('click', function () { show(at + 1); }); }
  if (cards.length) { show(0); }
})();
