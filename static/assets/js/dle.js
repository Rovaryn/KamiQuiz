/* KamiQuiz — Kamidle : personnage, pouvoir, emoji et univers du jour */
(function () {
  'use strict';
  var esc = KQ.esc, store = KQ.store;
  var MODES = {
    personnage: { label: 'Personnage', ico: '🎯', max: 0 },
    pouvoir: { label: 'Pouvoir', ico: '⚡', max: 6 },
    emoji: { label: 'Emoji', ico: '😶', max: 6 },
    univers: { label: 'Univers', ico: '🌍', max: 6 }
  };
  var GENRE = { M: 'Masculin', F: 'Féminin', N: 'Aucun' };
  var COLS = ['Univers', 'Genre', 'Espèce', 'Rôle', 'Style'];

  /* ---------- dates : le jeu change à minuit, heure locale ---------- */
  function iso(d) {
    return d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0');
  }
  function dayIndex(data, d) {
    var p = data.start.split('-');
    var a = Date.UTC(+p[0], +p[1] - 1, +p[2]);
    var b = Date.UTC(d.getFullYear(), d.getMonth(), d.getDate());
    return Math.max(0, Math.round((b - a) / 864e5));
  }
  function norm(s) {
    return String(s).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]+/g, ' ').trim();
  }

  var dataP = null;
  function load() {
    if (!dataP) {
      dataP = fetch('/data/dle.json').then(function (r) {
        if (!r.ok) throw new Error('HTTP ' + r.status);
        return r.json();
      }).then(function (d) {
        d.byId = {};
        d.chars.forEach(function (c) { d.byId[c.id] = c; });
        d.ukeys = Object.keys(d.univers);
        return d;
      });
    }
    return dataP;
  }

  /* La cible du jour : calendrier fixe, avec repli si le contenu n'est pas encore publié sur ce déploiement */
  function targetFor(data, mode, idx) {
    var list = data.sched[mode];
    var pool = mode === 'univers' ? data.ukeys : data.chars.filter(function (c) {
      return mode === 'pouvoir' ? c.p : mode === 'emoji' ? c.emo.length >= 2 : true;
    }).map(function (c) { return c.id; });
    var id = list[idx % list.length];
    var ok = mode === 'univers' ? data.univers[id] : data.byId[id];
    if (ok && pool.indexOf(id) >= 0) return id;
    return pool[(idx * 7919) % pool.length];
  }

  /* ---------- statistiques ---------- */
  function statsKey(m) { return 'kq_dle_stats_' + m; }
  function stateKey(m, day) { return 'kq_dle_' + m + '_' + day; }
  function recordEnd(mode, day, win) {
    var st = store.get(statsKey(mode), { played: 0, wins: 0, streak: 0, best: 0, last: null });
    if (st.lastPlayed === day) return st;
    var y = new Date(); y.setDate(y.getDate() - 1);
    st.played++;
    st.lastPlayed = day;
    if (win) {
      st.wins++;
      st.streak = st.last === iso(y) ? st.streak + 1 : 1;
      st.last = day;
      st.best = Math.max(st.best, st.streak);
    } else {
      st.streak = 0;
    }
    store.set(statsKey(mode), st);
    return st;
  }
  function currentStreak(mode) {
    var st = store.get(statsKey(mode), null);
    if (!st) return 0;
    var y = new Date(); y.setDate(y.getDate() - 1);
    return st.last === iso(new Date()) || st.last === iso(y) ? st.streak : 0;
  }

  /* ---------- page d'accueil du Kamidle et cartes de l'accueil ---------- */
  function initCards() {
    var cards = document.querySelectorAll('[data-dle-card]');
    if (!cards.length) return;
    var today = iso(new Date());
    var done = 0, total = 0;
    Array.prototype.forEach.call(cards, function (card) {
      var m = card.getAttribute('data-dle-card');
      var s = store.get(stateKey(m, today), null);
      var el = card.querySelector('[data-state]');
      total++;
      if (s && s.done) {
        done++;
        card.classList.add(s.win ? 'is-won' : 'is-lost');
        el.textContent = s.win ? 'Trouvé en ' + s.guesses.length + ' essai' + (s.guesses.length > 1 ? 's' : '') : 'Raté, retente demain';
      } else if (s && s.guesses && s.guesses.length) {
        el.textContent = 'En cours : ' + s.guesses.length + ' essai' + (s.guesses.length > 1 ? 's' : '');
      }
      var k = currentStreak(m);
      if (k > 1) el.textContent += ' · série de ' + k;
    });
    var sum = document.querySelector('[data-dle-summary]');
    if (sum) {
      sum.textContent = done === total ? 'Les quatre énigmes du jour sont terminées. Rendez-vous demain à minuit !'
        : done ? done + ' énigme' + (done > 1 ? 's' : '') + ' sur ' + total + ' terminée' + (done > 1 ? 's' : '') + " aujourd'hui."
        : '';
    }
  }

  /* ---------- le jeu ---------- */
  var root = document.getElementById('dle');
  initCards();
  if (!root) return;
  var MODE = root.getAttribute('data-mode');
  var CONF = MODES[MODE];

  load().then(function (data) { start(data); }).catch(function () {
    root.innerHTML = '<p class="empty">Impossible de charger l\'énigme du jour. Vérifie ta connexion puis recharge la page.</p>';
  });

  function start(data) {
    var now = new Date();
    var today = iso(now);
    var idx = dayIndex(data, now);
    var practice = false;
    var target, state;

    var y = new Date(now); y.setDate(y.getDate() - 1);
    var yEl = document.querySelector('[data-dle-yesterday]');
    if (yEl && idx > 0) {
      var yid = targetFor(data, MODE, idx - 1);
      yEl.innerHTML = "Réponse d'hier : <b>" + esc(nameOf(yid)) + '</b>';
    }

    function nameOf(id) { return MODE === 'univers' ? data.series[id].n : data.byId[id].name; }
    function serieOf(id) { return MODE === 'univers' ? id : data.byId[id].u; }

    function newGame(isPractice) {
      practice = isPractice;
      if (practice) {
        var pool = MODE === 'univers' ? data.ukeys : data.chars.filter(function (c) {
          return MODE === 'pouvoir' ? c.p : MODE === 'emoji' ? c.emo.length >= 2 : true;
        }).map(function (c) { return c.id; });
        var t;
        do { t = pool[Math.floor(Math.random() * pool.length)]; } while (pool.length > 1 && t === target);
        target = t;
        state = { guesses: [], done: false, win: false };
      } else {
        target = targetFor(data, MODE, idx);
        state = store.get(stateKey(MODE, today), null);
        if (!state || state.t !== target) state = { t: target, guesses: [], done: false, win: false };
      }
      render();
    }
    function save() { if (!practice) store.set(stateKey(MODE, today), state); }

    /* ----- rendu ----- */
    function render() {
      var n = state.guesses.length;
      var head = '<div class="dle-top"><strong>' + (practice ? 'Entraînement' : 'Kamidle n°' + (idx + 1)) + '</strong>' +
        '<span>' + CONF.ico + ' ' + CONF.label + (CONF.max ? ' · ' + Math.min(n, CONF.max) + '/' + CONF.max : (n ? ' · ' + n + ' essai' + (n > 1 ? 's' : '') : '')) + '</span></div>';
      root.innerHTML = head + '<div class="dle-clue">' + clueHTML() + '</div>' +
        (state.done ? '' : inputHTML()) + '<div class="dle-end" id="dle-end"></div>' + guessesHTML();
      if (state.done) renderEnd(); else bindInput();
    }

    function wrongCount() { return state.guesses.filter(function (g) { return g !== target; }).length; }

    function clueHTML() {
      var w = wrongCount(), t, s, html = '';
      if (MODE === 'personnage') {
        var c = data.byId[target];
        html = '<p class="dle-ask">Qui est le personnage du jour ?</p>';
        var n = state.guesses.length;
        var h1 = n >= 4 || state.done, h2 = n >= 7 || state.done;
        html += '<div class="dle-hints">' +
          '<div class="dle-hint' + (h1 ? ' on' : '') + '"><small>Indice 1' + (h1 ? '' : ' · dans ' + (4 - n) + ' essai' + (4 - n > 1 ? 's' : '')) + '</small>' +
          (h1 ? '<b>Initiale : ' + esc(c.name.charAt(0)) + '</b>' : '<b>Initiale</b>') + '</div>' +
          '<div class="dle-hint' + (h2 ? ' on' : '') + '"><small>Indice 2' + (h2 ? '' : ' · dans ' + (7 - n) + ' essai' + (7 - n > 1 ? 's' : '')) + '</small>' +
          (h2 ? '<b class="dle-emo">' + esc(c.emo.join(' ')) + '</b>' : '<b>Emojis</b>') + '</div></div>';
        return html;
      }
      if (MODE === 'pouvoir') {
        t = data.byId[target]; s = data.series[t.u];
        html = '<p class="dle-ask">À qui appartient ce pouvoir ?</p><blockquote class="dle-quote">' + esc(t.p[0]) + '</blockquote>';
        html += '<div class="dle-hints">' +
          hint(w >= 2, 'Famille', data.cats[s.c], 2 - w) + hint(w >= 4, 'Univers', s.n, 4 - w) + hint(w >= 5, 'Initiale', t.name.charAt(0), 5 - w) + '</div>';
        if (state.done && t.p[1]) html += '<p class="muted" style="margin-top:12px">Nom du pouvoir : <b>' + esc(t.p[1]) + '</b></p>';
        return html;
      }
      if (MODE === 'emoji') {
        t = data.byId[target];
        var shown = state.done ? t.emo.length : Math.min(t.emo.length, 1 + w);
        html = '<p class="dle-ask">Quel personnage se cache derrière ces emojis ?</p><div class="dle-emojis">';
        t.emo.forEach(function (em, i) {
          html += i < shown ? '<span class="dle-e on">' + esc(em) + '</span>' : '<span class="dle-e">?</span>';
        });
        html += '</div>';
        html += '<div class="dle-hints">' + hint(w >= t.emo.length, 'Univers', data.series[t.u].n, t.emo.length - w) + '</div>';
        return html;
      }
      // univers
      var clues = data.univers[target];
      var k = state.done ? clues.length : Math.min(clues.length, 1 + w);
      html = '<p class="dle-ask">De quel univers parle-t-on ?</p><ol class="dle-clues">';
      clues.forEach(function (cl, i) {
        html += i < k ? '<li class="on">' + esc(cl) + '</li>' : '<li>Indice ' + (i + 1) + ' : à débloquer</li>';
      });
      html += '</ol><div class="dle-hints">' + hint(w >= 5, 'Famille', data.cats[data.series[target].c], 5 - w) + '</div>';
      return html;
    }
    function hint(open, label, value, left) {
      open = open || state.done;
      return '<div class="dle-hint' + (open ? ' on' : '') + '"><small>' + label + (open ? '' : ' · dans ' + left + ' erreur' + (left > 1 ? 's' : '')) + '</small><b>' +
        (open ? esc(value) : '?') + '</b></div>';
    }

    function inputHTML() {
      var ph = MODE === 'univers' ? 'Tape le nom d\'un univers…' : 'Tape le nom d\'un personnage…';
      return '<form class="dle-form" autocomplete="off"><label class="sr-only" for="dle-in">' + ph + '</label>' +
        '<div class="dle-field"><input id="dle-in" placeholder="' + ph + '" role="combobox" aria-expanded="false" aria-controls="dle-list" aria-autocomplete="list">' +
        '<ul class="dle-list" id="dle-list" role="listbox" hidden></ul></div>' +
        '<button class="btn btn-gold" type="submit">Valider</button></form>';
    }

    /* ----- propositions ----- */
    function candidates(q) {
      q = norm(q);
      if (!q) return [];
      var out = [];
      if (MODE === 'univers') {
        data.ukeys.forEach(function (k) {
          if (state.guesses.indexOf(k) >= 0) return;
          var nm = norm(data.series[k].n);
          var sc = nm.indexOf(q) === 0 ? 0 : nm.indexOf(' ' + q) >= 0 ? 1 : nm.indexOf(q) >= 0 ? 2 : -1;
          if (sc >= 0) out.push({ id: k, sc: sc, label: data.series[k].n, sub: data.cats[data.series[k].c] });
        });
      } else {
        data.chars.forEach(function (c) {
          if (state.guesses.indexOf(c.id) >= 0) return;
          var best = -1;
          [c.name].concat(c.alias).forEach(function (a) {
            var nm = norm(a);
            var sc = nm.indexOf(q) === 0 ? 0 : nm.indexOf(' ' + q) >= 0 ? 1 : -1;
            if (sc >= 0 && (best < 0 || sc < best)) best = sc;
          });
          if (best >= 0) out.push({ id: c.id, sc: best, label: c.name, sub: data.series[c.u].n });
        });
      }
      out.sort(function (a, b) { return a.sc - b.sc || a.label.localeCompare(b.label, 'fr'); });
      return out.slice(0, 8);
    }

    function bindInput() {
      var form = root.querySelector('.dle-form');
      var input = root.querySelector('#dle-in');
      var list = root.querySelector('#dle-list');
      var items = [], active = 0;
      function draw() {
        items = candidates(input.value);
        active = 0;
        if (!items.length) {
          list.hidden = true; input.setAttribute('aria-expanded', 'false');
          if (norm(input.value)) { list.innerHTML = '<li class="none">Aucun résultat</li>'; list.hidden = false; }
          return;
        }
        list.innerHTML = items.map(function (it, i) {
          return '<li role="option" id="dle-o' + i + '" data-i="' + i + '"' + (i === active ? ' aria-selected="true"' : '') + '><b>' + esc(it.label) + '</b><span>' + esc(it.sub) + '</span></li>';
        }).join('');
        list.hidden = false; input.setAttribute('aria-expanded', 'true');
      }
      function highlight() {
        Array.prototype.forEach.call(list.querySelectorAll('[role=option]'), function (li, i) {
          li.setAttribute('aria-selected', i === active ? 'true' : 'false');
          if (i === active) { input.setAttribute('aria-activedescendant', li.id); li.scrollIntoView({ block: 'nearest' }); }
        });
      }
      input.addEventListener('input', draw);
      input.addEventListener('keydown', function (ev) {
        if (!items.length) return;
        if (ev.key === 'ArrowDown') { active = (active + 1) % items.length; highlight(); ev.preventDefault(); }
        else if (ev.key === 'ArrowUp') { active = (active - 1 + items.length) % items.length; highlight(); ev.preventDefault(); }
        else if (ev.key === 'Escape') { list.hidden = true; }
      });
      list.addEventListener('mousedown', function (ev) {
        var li = ev.target.closest('[data-i]');
        if (!li) return;
        ev.preventDefault();
        guess(items[+li.getAttribute('data-i')].id);
      });
      form.addEventListener('submit', function (ev) {
        ev.preventDefault();
        if (items.length) guess(items[active].id);
        else if (norm(input.value)) KQ.toast('Choisis un nom dans la liste proposée.');
      });
      input.focus({ preventScroll: true });
    }

    function guess(id) {
      if (state.done || state.guesses.indexOf(id) >= 0) return;
      state.guesses.push(id);
      if (id === target) { state.done = true; state.win = true; }
      else if (CONF.max && state.guesses.length >= CONF.max) { state.done = true; state.win = false; }
      if (state.done && !practice) state.stats = recordEnd(MODE, today, state.win);
      save();
      render();
      var inp = root.querySelector('#dle-in');
      if (inp) inp.focus({ preventScroll: true });
    }

    /* ----- historique des essais ----- */
    function cmpPerso(g, t) {
      var su = data.series[g.u], tu = data.series[t.u];
      function setCmp(a, b) {
        var same = a.length === b.length && a.every(function (x) { return b.indexOf(x) >= 0; });
        if (same) return 'ok';
        return a.some(function (x) { return b.indexOf(x) >= 0; }) ? 'near' : 'no';
      }
      return [
        [su.n, g.u === t.u ? 'ok' : su.c === tu.c ? 'near' : 'no'],
        [GENRE[g.g], g.g === t.g ? 'ok' : 'no'],
        [g.e.join(', '), setCmp(g.e, t.e)],
        [g.r, g.r === t.r ? 'ok' : 'no'],
        [g.s.join(', '), setCmp(g.s, t.s)]
      ];
    }

    function guessesHTML() {
      if (!state.guesses.length) return '';
      var list = state.guesses.slice().reverse();
      if (MODE === 'personnage') {
        var t = data.byId[target];
        var rows = list.map(function (id) {
          var g = data.byId[id];
          var cells = cmpPerso(g, t).map(function (c, i) {
            return '<td class="c-' + c[1] + '" data-label="' + COLS[i] + '">' + esc(c[0]) + '</td>';
          }).join('');
          return '<tr><th scope="row" class="' + (id === target ? 'c-ok' : '') + '">' + esc(g.name) + '</th>' + cells + '</tr>';
        }).join('');
        return '<div class="dle-table-wrap"><table class="dle-table"><thead><tr><th scope="col">Personnage</th>' +
          COLS.map(function (c) { return '<th scope="col">' + c + '</th>'; }).join('') + '</tr></thead><tbody>' + rows + '</tbody></table></div>';
      }
      return '<ul class="dle-guesses">' + list.map(function (id) {
        var ok = id === target;
        var sub = '';
        if (!ok && MODE !== 'univers') {
          var g = data.byId[id], tt = data.byId[target];
          sub = g.u === tt.u ? 'bon univers' : data.series[g.u].c === data.series[tt.u].c ? 'même famille' : '';
        } else if (!ok) {
          sub = data.series[id].c === data.series[target].c ? 'même famille' : '';
        }
        return '<li class="' + (ok ? 'c-ok' : sub === 'bon univers' ? 'c-near' : 'c-no') + '"><b>' + esc(nameOf(id)) + '</b>' +
          (sub ? '<span>' + sub + '</span>' : '') + '</li>';
      }).join('') + '</ul>';
    }

    /* ----- fin de partie ----- */
    function shareText() {
      var n = state.guesses.length;
      var lines = [CONF.ico + ' Kamidle n°' + (idx + 1) + ' : ' + CONF.label];
      if (MODE === 'personnage') {
        lines.push(state.win ? 'Trouvé en ' + n + ' essai' + (n > 1 ? 's' : '') : 'Pas trouvé');
        var t = data.byId[target];
        var em = { ok: '🟩', near: '🟨', no: '🟥' };
        var rows = state.guesses.map(function (id) {
          return cmpPerso(data.byId[id], t).map(function (c) { return em[c[1]]; }).join('');
        });
        if (rows.length > 8) { lines = lines.concat(rows.slice(0, 3)); lines.push('⋯ ' + (rows.length - 6) + ' de plus'); lines = lines.concat(rows.slice(-3)); }
        else lines = lines.concat(rows);
      } else {
        lines.push(state.guesses.map(function (id) { return id === target ? '🟩' : '🟥'; }).join('') +
          (state.win ? ' ' + n + '/' + CONF.max : ' X/' + CONF.max));
      }
      lines.push('https://kamiquiz.com/dle/' + MODE + '/');
      return lines.join('\n');
    }

    function renderEnd() {
      var box = root.querySelector('#dle-end');
      var sid = serieOf(target), s = data.series[sid];
      var n = state.guesses.length;
      var st = practice ? null : store.get(statsKey(MODE), null);
      var html = '<div class="dle-result ' + (state.win ? 'win' : 'lose') + '">' +
        '<p class="dle-verdict">' + (state.win ? (n === 1 ? 'Du premier coup ! ' : 'Bien joué ! ') + 'C\'était' : 'Perdu… C\'était') + '</p>' +
        '<p class="dle-answer">' + esc(nameOf(target)) + '</p>' +
        (MODE !== 'univers' ? '<p class="muted">' + esc(s.n) + '</p>' : '') +
        (state.win ? '<p>Trouvé en <b>' + n + '</b> essai' + (n > 1 ? 's' : '') + '.</p>' : '');
      if (st) {
        html += '<div class="dle-stats"><div><b>' + st.played + '</b><small>parties</small></div><div><b>' + (st.played ? Math.round(st.wins * 100 / st.played) : 0) + ' %</b><small>réussite</small></div>' +
          '<div><b>' + st.streak + '</b><small>série</small></div><div><b>' + st.best + '</b><small>record</small></div></div>' +
          '<p class="dle-next">Prochaine énigme dans <b data-countdown></b></p>';
      }
      html += '<div class="btn-row" style="justify-content:center">' +
        (practice ? '' : '<button class="btn btn-gold" type="button" data-act="share">Partager mon résultat</button>') +
        '<a class="btn" href="/quiz/' + s.s + '/">Quiz ' + esc(s.n) + '</a>' +
        '<button class="btn" type="button" data-act="practice">' + (practice ? 'Encore une' : 'Entraînement illimité') + '</button>' +
        (practice ? '<button class="btn" type="button" data-act="daily">Revenir à l\'énigme du jour</button>' : '') +
        '</div>';
      if (!practice) {
        var next = Object.keys(MODES).filter(function (m) {
          if (m === MODE) return false;
          var s2 = store.get(stateKey(m, today), null);
          return !(s2 && s2.done);
        });
        if (next.length) {
          html += '<p class="dle-more">Encore à jouer aujourd\'hui : ' + next.map(function (m) {
            return '<a href="/dle/' + m + '/">' + MODES[m].ico + ' ' + MODES[m].label + '</a>';
          }).join(' · ') + '</p>';
        } else {
          html += '<p class="dle-more">Les quatre énigmes du jour sont terminées. Tu mérites ton rang de Kami.</p>';
        }
      }
      html += '</div>';
      box.innerHTML = html;
      box.addEventListener('click', function (ev) {
        var b = ev.target.closest('[data-act]');
        if (!b) return;
        var act = b.getAttribute('data-act');
        if (act === 'share') share();
        if (act === 'practice') newGame(true);
        if (act === 'daily') newGame(false);
      });
      tick();
    }

    function share() {
      var txt = shareText();
      if (navigator.share && /Mobi|Android/i.test(navigator.userAgent)) {
        navigator.share({ text: txt }).catch(function () {});
        return;
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(txt).then(function () { KQ.toast('Résultat copié, colle-le où tu veux !'); },
          function () { prompt('Copie ton résultat :', txt); });
      } else {
        prompt('Copie ton résultat :', txt);
      }
    }

    var timer = null;
    function tick() {
      clearInterval(timer);
      var el = root.querySelector('[data-countdown]');
      if (!el) return;
      function upd() {
        var n = new Date(), m = new Date(n);
        m.setHours(24, 0, 0, 0);
        var s = Math.max(0, Math.floor((m - n) / 1000));
        if (s === 0 && !practice) { location.reload(); return; }
        el.textContent = String(Math.floor(s / 3600)).padStart(2, '0') + ' h ' + String(Math.floor(s / 60) % 60).padStart(2, '0') + ' min ' + String(s % 60).padStart(2, '0') + ' s';
      }
      upd();
      timer = setInterval(upd, 1000);
    }

    newGame(false);
  }
})();
