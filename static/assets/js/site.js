/* KamiQuiz — scripts communs (menu, question du jour, classement, révision) */
(function () {
  'use strict';

  var LB_API = 'https://polished-haze-58ed.meklatiaymen8.workers.dev';
  window.KQ = window.KQ || {};
  KQ.LB_API = LB_API;

  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  KQ.esc = esc;

  KQ.toast = function (msg) {
    var t = document.getElementById('toast');
    if (!t) {
      t = document.createElement('div');
      t.id = 'toast';
      t.className = 'toast';
      t.setAttribute('role', 'status');
      document.body.appendChild(t);
    }
    t.textContent = msg;
    t.classList.add('on');
    clearTimeout(KQ._toastT);
    KQ._toastT = setTimeout(function () { t.classList.remove('on'); }, 2600);
  };

  KQ.store = {
    get: function (k, d) { try { var v = localStorage.getItem(k); return v === null ? d : JSON.parse(v); } catch (e) { return d; } },
    set: function (k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  };

  /* Petit cache des fichiers de questions */
  var cache = {};
  KQ.loadSerie = function (key) {
    if (!cache[key]) {
      cache[key] = fetch('/data/' + key + '.json').then(function (r) {
        if (!r.ok) throw new Error('HTTP ' + r.status);
        return r.json();
      });
    }
    return cache[key];
  };

  /* ---------- Menu mobile ---------- */
  var btn = document.querySelector('.menu-btn');
  var nav = document.getElementById('nav');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  /* ---------- Question du jour (accueil) ---------- */
  var qdj = document.getElementById('qdj');
  if (qdj) {
    var slugs = (qdj.getAttribute('data-keys') || '').split(',');
    var names = JSON.parse(qdj.getAttribute('data-names') || '{}');
    var today = new Date().toISOString().slice(0, 10);
    var day = Math.floor(Date.parse(today) / 86400000);
    var key = slugs[(day * 7 + 3) % slugs.length];
    var answered = KQ.store.get('kq_qdj', {});

    KQ.loadSerie(key).then(function (s) {
      var pool = s.q.filter(function (q) { return q.d <= 2; });
      if (!pool.length) pool = s.q;
      var q = pool[(day * 31 + 11) % pool.length];
      var slot = qdj.querySelector('[data-slot]');
      qdj.style.setProperty('--accent', s.color);
      qdj.querySelector('[data-serie]').innerHTML = '<i></i>' + esc(names[key] || s.name);
      slot.innerHTML =
        '<p class="qtext">' + esc(q.q) + '</p>' +
        '<div class="answers">' + q.a.map(function (a, i) {
          return '<button class="answer" type="button" data-i="' + i + '"><kbd>' + 'ABCD'[i] + '</kbd><span>' + esc(a) + '</span></button>';
        }).join('') + '</div>' +
        '<div class="feedback" hidden aria-live="polite"></div>';

      function reveal(choice) {
        var btns = slot.querySelectorAll('.answer');
        btns.forEach(function (b, i) {
          b.disabled = true;
          if (i === q.c) b.classList.add('is-right');
          else if (i === choice) b.classList.add('is-wrong');
          else b.classList.add('is-dim');
        });
        var fb = slot.querySelector('.feedback');
        fb.hidden = false;
        fb.innerHTML = '<strong>' + (choice === q.c ? 'Bonne réponse.' : 'Raté : la réponse était « ' + esc(q.a[q.c]) + ' ».') + '</strong> ' + esc(q.fb) +
          ' <a href="/jouer/?s=' + encodeURIComponent(key) + '">Enchaîner sur ce quiz</a>';
      }

      slot.addEventListener('click', function (e) {
        var b = e.target.closest('.answer');
        if (!b || b.disabled) return;
        var choice = +b.getAttribute('data-i');
        answered[today] = choice;
        KQ.store.set('kq_qdj', answered);
        reveal(choice);
      });
      if (answered[today] !== undefined) reveal(answered[today]);
    }).catch(function () {
      qdj.querySelector('[data-slot]').innerHTML = '<p class="muted">La question du jour n\'a pas pu se charger. Rechargez la page pour réessayer.</p>';
    });
  }

  /* ---------- Classement mondial ---------- */
  KQ.renderBoard = function (el, entries, names) {
    if (!entries || !entries.length) {
      el.innerHTML = '<li class="board-empty"><span class="empty">Aucun score pour l\'instant. Terminez un quiz pour ouvrir le classement.</span></li>';
      return;
    }
    el.innerHTML = entries.map(function (e, i) {
      var serie = names && names[e.series] ? names[e.series] : '';
      var sub = [serie, e.mode].filter(Boolean).join(', ');
      return '<li><span class="pos">' + (i + 1) + '</span>' +
        '<span class="who">' + esc(e.name || 'Anonyme') + '<small>' + esc(sub) + '</small></span>' +
        '<span class="pts">' + esc(e.pct) + '%<small>' + esc(e.sc) + '/' + esc(e.tot) + '</small></span></li>';
    }).join('');
  };

  var board = document.querySelector('[data-board]');
  if (board) {
    var bNames = JSON.parse(board.getAttribute('data-names') || '{}');
    var bSerie = board.getAttribute('data-board');
    var url = bSerie === 'global'
      ? LB_API + '/api/scores?global=1&limit=10'
      : LB_API + '/api/scores?series=' + encodeURIComponent(bSerie) + '&limit=10';
    fetch(url).then(function (r) { return r.json(); }).then(function (rows) {
      KQ.renderBoard(board, Array.isArray(rows) ? rows : [], bNames);
    }).catch(function () {
      board.innerHTML = '<li class="board-empty"><span class="empty">Le classement est momentanément indisponible.</span></li>';
    });
  }

  /* ---------- Révision : tout afficher / tout masquer ---------- */
  document.querySelectorAll('[data-reveal]').forEach(function (b) {
    b.addEventListener('click', function () {
      var open = b.getAttribute('data-reveal') === 'open';
      document.querySelectorAll('.qitem details').forEach(function (d) { d.open = open; });
    });
  });

  /* ---------- Préférences de confidentialité (CMP Google) ---------- */
  document.querySelectorAll('[data-privacy-choices]').forEach(function (b) {
    b.addEventListener('click', function () {
      window.googlefc = window.googlefc || {};
      window.googlefc.callbackQueue = window.googlefc.callbackQueue || [];
      if (window.googlefc.showRevocationMessage) {
        window.googlefc.showRevocationMessage();
      } else {
        window.googlefc.callbackQueue.push(function () { window.googlefc.showRevocationMessage(); });
        KQ.toast('Le gestionnaire de consentement se charge…');
      }
    });
  });
})();
