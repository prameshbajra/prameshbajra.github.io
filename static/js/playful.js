(function () {
  'use strict';

  var root = document.querySelector('.ply');
  if (!root) return;

  var initialTheme = window.__plyInitialTheme || 'light';
  setTheme(initialTheme, false);

  var themeBtn = document.querySelector('.ply-theme-btn');
  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var current = root.getAttribute('data-theme') || 'light';
      var next = current === 'dark' ? 'light' : 'dark';
      setTheme(next, true);
    });
  }

  function setTheme(theme, persist) {
    root.setAttribute('data-theme', theme);
    document.documentElement.classList.toggle('theme-dark', theme === 'dark');
    if (themeBtn) {
      themeBtn.setAttribute('aria-label', 'Switch to ' + (theme === 'dark' ? 'light' : 'dark') + ' mode');
      themeBtn.setAttribute('title', 'Switch to ' + (theme === 'dark' ? 'light' : 'dark') + ' mode');
    }
    if (persist) {
      try { localStorage.setItem('ply-theme', theme); } catch (e) {}
    }
  }

  var bg = root.querySelector('.ply-bg');
  if (!bg) return;

  bg.style.setProperty('--mx', '50%');
  bg.style.setProperty('--my', '50%');
  bg.style.setProperty('--px', '0');
  bg.style.setProperty('--py', '0');

  function onPointerMove(e) {
    var rect = bg.getBoundingClientRect();
    if (!rect.width || !rect.height) return;
    var x = (e.clientX - rect.left) / rect.width;
    var y = (e.clientY - rect.top) / rect.height;
    bg.style.setProperty('--mx', (x * 100).toFixed(2) + '%');
    bg.style.setProperty('--my', (y * 100).toFixed(2) + '%');
    bg.style.setProperty('--px', (x * 2 - 1).toFixed(3));
    bg.style.setProperty('--py', (y * 2 - 1).toFixed(3));
  }
  document.addEventListener('pointermove', onPointerMove, { passive: true });
  document.addEventListener('mousemove', onPointerMove, { passive: true });

  var palette = ['#2240e8', '#ff5b3c', '#bfeb6f', '#fcc63a', '#dfd6ff'];
  var colorIdx = 0;
  root.addEventListener('click', function (e) {
    if (e.target.closest('a, button, input, select, textarea, [role="button"]')) return;
    var rect = bg.getBoundingClientRect();
    var x = e.clientX - rect.left;
    var y = e.clientY - rect.top;
    var c = palette[colorIdx % palette.length];
    colorIdx++;
    var el = document.createElement('div');
    el.className = 'ply-ripple';
    el.style.left = x + 'px';
    el.style.top = y + 'px';
    el.style.background = c;
    bg.appendChild(el);
    setTimeout(function () { if (el.parentNode) el.parentNode.removeChild(el); }, 920);
  });

  var copyBtns = document.querySelectorAll('[data-ply-copy-link]');
  copyBtns.forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      var label = btn.querySelector('[data-ply-copy-text]');
      var orig = label ? label.textContent : null;
      var url = window.location.href;
      var done = function () {
        if (label) {
          label.textContent = 'Copied!';
          setTimeout(function () { label.textContent = orig; }, 1500);
        }
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url).then(done).catch(done);
      } else {
        var ta = document.createElement('textarea');
        ta.value = url;
        ta.setAttribute('readonly', '');
        ta.style.position = 'absolute';
        ta.style.left = '-9999px';
        document.body.appendChild(ta);
        ta.select();
        try { document.execCommand('copy'); } catch (err) {}
        document.body.removeChild(ta);
        done();
      }
    });
  });

  var popoverBtns = document.querySelectorAll('[data-ply-popover]');
  popoverBtns.forEach(function (btn) {
    var noteId = btn.getAttribute('aria-controls');
    var note = noteId ? document.getElementById(noteId) : null;
    if (!note) return;

    function close() {
      btn.setAttribute('aria-expanded', 'false');
      note.removeAttribute('data-open');
    }
    function open() {
      btn.setAttribute('aria-expanded', 'true');
      note.setAttribute('data-open', 'true');
      btn.classList.remove('is-wiggle');
      void btn.offsetWidth;
      btn.classList.add('is-wiggle');
    }

    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      if (btn.getAttribute('aria-expanded') === 'true') close(); else open();
    });
    note.addEventListener('click', function (e) { e.stopPropagation(); });
    document.addEventListener('click', function (e) {
      if (btn.getAttribute('aria-expanded') !== 'true') return;
      if (!btn.contains(e.target) && !note.contains(e.target)) close();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && btn.getAttribute('aria-expanded') === 'true') {
        close();
        btn.focus();
      }
    });
  });

  var dotsHost = bg.querySelector('.ply-dots');
  if (dotsHost) {
    var dotColors = ['var(--c-cobalt)', 'var(--c-coral)', 'var(--c-mint)', 'var(--c-mustard)', 'var(--c-lilac)'];
    for (var i = 0; i < 18; i++) {
      var d = document.createElement('div');
      d.className = 'ply-dot';
      var size = 4 + Math.random() * 8;
      d.style.top = (Math.random() * 100) + '%';
      d.style.left = (Math.random() * 100) + '%';
      d.style.width = size + 'px';
      d.style.height = size + 'px';
      d.style.background = dotColors[i % dotColors.length];
      var dur = 18 + Math.random() * 20;
      var delay = -(Math.random() * 30);
      d.style.animation = 'plyDot' + (i % 4) + ' ' + dur + 's ease-in-out ' + delay + 's infinite alternate';
      dotsHost.appendChild(d);
    }
  }
})();
