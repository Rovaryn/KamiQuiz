/* KamiQuiz — scripts communs (menu, question du jour, classement, révision) */
(function () {
  'use strict';

  var LB_API = 'https://polished-haze-58ed.meklatiaymen8.workers.dev';
  window.KQ = window.KQ || {};
  KQ.LB_API = LB_API;

  /* ---------- Langue : textes écrits en français, traduits par /assets/js/i18n-<langue>.js ---------- */
  KQ.lang = document.documentElement.lang || 'fr';
  var DICT = window.KQ_I18N || {};
  KQ.t = function (s, vars) {
    var r = Object.prototype.hasOwnProperty.call(DICT, s) ? DICT[s] : s;
    if (vars) r = r.replace(/\{(\w+)\}/g, function (m, k) { return vars[k] != null ? vars[k] : m; });
    return r;
  };
  /* Chemin logique (français) -> chemin dans la langue de la page */
  KQ.url = function (p) {
    var R = window.KQ_ROUTES;
    if (!R) return p;
    var keys = Object.keys(R).sort(function (a, b) { return b.length - a.length; });
    for (var i = 0; i < keys.length; i++) if (p.indexOf(keys[i]) === 0) return R[keys[i]] + p.slice(keys[i].length);
    return p;
  };
  KQ.data = function (file) { return (KQ.lang === 'fr' ? '/data/' : '/data/' + KQ.lang + '/') + file; };
  var T = KQ.t;

  /* Langue choisie avec le sélecteur FR | EN : mémorisée pour les prochaines visites */
  document.addEventListener('click', function (ev) {
    var a = ev.target.closest && ev.target.closest('.lang-sw a[data-lang]');
    if (a) { try { localStorage.setItem('kq-lang', a.getAttribute('data-lang')); } catch (x) {} }
  });

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
      cache[key] = fetch(KQ.data(key + '.json')).then(function (r) {
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
        fb.innerHTML = '<strong>' + (choice === q.c ? T('Bonne réponse.') : T('Raté : la réponse était « {a} ».', { a: esc(q.a[q.c]) })) + '</strong> ' + esc(q.fb) +
          ' <a href="' + KQ.url('/jouer/') + '?s=' + encodeURIComponent(key) + '">' + T('Enchaîner sur ce quiz') + '</a>';
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
      qdj.querySelector('[data-slot]').innerHTML = '<p class="muted">' + T('La question du jour n\'a pas pu se charger. Rechargez la page pour réessayer.') + '</p>';
    });
  }

  /* ---------- Classement mondial ---------- */
  KQ.renderBoard = function (el, entries, names) {
    if (!entries || !entries.length) {
      el.innerHTML = '<li class="board-empty"><span class="empty">' + T('Aucun score pour l\'instant. Terminez un quiz pour ouvrir le classement.') + '</span></li>';
      return;
    }
    el.innerHTML = entries.map(function (e, i) {
      var serie = names && names[e.series] ? names[e.series] : '';
      var sub = [serie, e.mode && T(e.mode)].filter(Boolean).join(', ');
      return '<li><span class="pos">' + (i + 1) + '</span>' +
        '<span class="who">' + esc(e.name || T('Anonyme')) + '<small>' + esc(sub) + '</small></span>' +
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
      board.innerHTML = '<li class="board-empty"><span class="empty">' + T('Le classement est momentanément indisponible.') + '</span></li>';
    });
  }

  /* ---------- Révision : tout afficher / tout masquer ---------- */
  document.querySelectorAll('[data-reveal]').forEach(function (b) {
    b.addEventListener('click', function () {
      var open = b.getAttribute('data-reveal') === 'open';
      document.querySelectorAll('.qitem details').forEach(function (d) { d.open = open; });
    });
  });

  /* ---------- Bande-annonce : le lecteur YouTube n'est chargé qu'au clic ---------- */
  document.querySelectorAll('.trailer[data-yt]').forEach(function (fig) {
    var play = fig.querySelector('.trailer-play');
    var id = fig.getAttribute('data-yt');
    if (!play || !/^[\w-]{11}$/.test(id)) return;
    play.addEventListener('click', function () {
      var box = document.createElement('div');
      box.className = 'trailer-frame';
      var art = play.querySelector('img');
      if (art) box.appendChild(art.cloneNode());
      var f = document.createElement('iframe');
      f.src = 'https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0&playsinline=1';
      f.title = fig.getAttribute('data-title') || T('Bande-annonce');
      f.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
      f.allowFullscreen = true;
      f.referrerPolicy = 'strict-origin-when-cross-origin';
      f.addEventListener('load', function () { box.classList.add('ready'); });
      box.appendChild(f);
      play.replaceWith(box);
      f.focus();
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
        KQ.toast(T('Le gestionnaire de consentement se charge…'));
      }
    });
  });
})();
