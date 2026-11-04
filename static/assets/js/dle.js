/* KamiQuiz — Kamidle : personnage, pouvoir, emoji, univers et mot mystère du jour */
(function () {
  'use strict';
  var esc = KQ.esc, store = KQ.store, T = KQ.t, U = KQ.url;
  /* singulier ou pluriel selon n (à la française : 0 et 1 au singulier) */
  function P(n, one, many, vars) { vars = vars || {}; vars.n = n; return T(n > 1 ? many : one, vars); }
  var MODES = {
    personnage: { label: T('Personnage'), ico: '🎯', max: 0 },
    pouvoir: { label: T('Pouvoir'), ico: '⚡', max: 6 },
    emoji: { label: T('Emoji'), ico: '😶', max: 6 },
    univers: { label: T('Univers'), ico: '🌍', max: 6 },
    mot: { label: T('Mot mystère'), ico: '🔤', max: 6 }
  };
  var GENRE = { M: T('Masculin'), F: T('Féminin'), N: T('Aucun') };
  var COLS = ['Univers', 'Catégorie', 'Genre', 'Espèce', 'Rôle', 'Style', 'Âge', 'Cheveux', 'Année'].map(function (c) { return T(c); });
  var KB = KQ.lang === 'fr' ? ['AZERTYUIOP', 'QSDFGHJKLM', '<WXCVBN>'] : ['QWERTYUIOP', 'ASDFGHJKL', '<ZXCVBNM>'];

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
      dataP = fetch(KQ.data('dle.json')).then(function (r) {
        if (!r.ok) throw new Error('HTTP ' + r.status);
        return r.json();
      }).then(function (d) {
        d.byId = {};
        d.chars.forEach(function (c) { d.byId[c.id] = c; });
        d.ukeys = Object.keys(d.univers);
        d.mkeys = Object.keys(d.mots || {});
        return d;
      });
    }
    return dataP;
  }

  /* La cible du jour : calendrier fixe, avec repli si le contenu n'est pas encore publié sur ce déploiement */
  function poolFor(data, mode) {
    if (mode === 'univers') return data.ukeys;
    if (mode === 'mot') return data.mkeys;
    return data.chars.filter(function (c) {
      return mode === 'pouvoir' ? c.p : mode === 'emoji' ? c.emo.length >= 2 : true;
    }).map(function (c) { return c.id; });
  }
  function targetFor(data, mode, idx) {
    var list = data.sched[mode];
    var pool = poolFor(data, mode);
    var id = list[idx % list.length];
    var ok = mode === 'univers' ? data.univers[id] : mode === 'mot' ? data.mots[id] : data.byId[id];
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
        el.textContent = s.win ? P(s.guesses.length, 'Trouvé en {n} essai', 'Trouvé en {n} essais') : T('Raté, retente demain');
      } else if (s && s.guesses && s.guesses.length) {
        el.textContent = P(s.guesses.length, 'En cours : {n} essai', 'En cours : {n} essais');
      }
      var k = currentStreak(m);
      if (k > 1) el.textContent += T(' · série de {k}', { k: k });
    });
    var sum = document.querySelector('[data-dle-summary]');
    if (sum) {
      sum.textContent = done === total ? T('Toutes les énigmes du jour sont terminées. Rendez-vous demain à minuit !')
        : done ? P(done, "{n} énigme sur {t} terminée aujourd'hui.", "{n} énigmes sur {t} terminées aujourd'hui.", { t: total })
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
    root.innerHTML = '<p class="empty">' + T("Impossible de charger l'énigme du jour. Vérifie ta connexion puis recharge la page.") + '</p>';
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
      yEl.innerHTML = T("Réponse d'hier : <b>{a}</b>", { a: esc(nameOf(yid)) });
    }

    function nameOf(id) { return MODE === 'univers' ? data.series[id].n : MODE === 'mot' ? id : data.byId[id].name; }
    function serieOf(id) { return MODE === 'univers' ? id : MODE === 'mot' ? null : data.byId[id].u; }

    function newGame(isPractice) {
      practice = isPractice;
      if (practice) {
        var pool = poolFor(data, MODE);
        var t;
        do { t = pool[Math.floor(Math.random() * pool.length)]; } while (pool.length > 1 && t === target);
        target = t;
        state = { guesses: [], done: false, win: false };
      } else {
        target = targetFor(data, MODE, idx);
        state = store.get(stateKey(MODE, today), null);
        if (!state || state.t !== target) state = { t: target, guesses: [], done: false, win: false };
      }
      cur = '';
      render();
    }
    function save() { if (!practice) store.set(stateKey(MODE, today), state); }

    /* ----- rendu ----- */
    var cur = '', justPlayed = false;
    function render() {
      if (MODE === 'mot') return renderMot();
      var n = state.guesses.length;
      var head = '<div class="dle-top"><strong>' + (practice ? T('Entraînement') : T('Kamidle n°{n}', { n: idx + 1 })) + '</strong>' +
        '<span>' + CONF.ico + ' ' + CONF.label + (CONF.max ? ' · ' + Math.min(n, CONF.max) + '/' + CONF.max : (n ? ' · ' + P(n, '{n} essai', '{n} essais') : '')) + '</span></div>';
      root.innerHTML = head + '<div class="dle-clue">' + clueHTML() + '</div>' +
        (state.done ? '' : inputHTML()) + '<div class="dle-end" id="dle-end"></div>' + guessesHTML();
      if (state.done) renderEnd(); else bindInput();
    }

    function wrongCount() { return state.guesses.filter(function (g) { return g !== target; }).length; }

    function clueHTML() {
      var w = wrongCount(), t, s, html = '';
      if (MODE === 'personnage') {
        var c = data.byId[target];
        html = '<p class="dle-ask">' + T('Qui est le personnage du jour ?') + '</p>';
        var n = state.guesses.length;
        var h1 = n >= 4 || state.done, h2 = n >= 7 || state.done;
        html += '<div class="dle-hints">' +
          '<div class="dle-hint' + (h1 ? ' on' : '') + '"><small>' + T('Indice 1') + (h1 ? '' : P(4 - n, ' · dans {n} essai', ' · dans {n} essais')) + '</small>' +
          (h1 ? '<b>' + T('Initiale : {l}', { l: esc(c.name.charAt(0)) }) + '</b>' : '<b>' + T('Initiale') + '</b>') + '</div>' +
          '<div class="dle-hint' + (h2 ? ' on' : '') + '"><small>' + T('Indice 2') + (h2 ? '' : P(7 - n, ' · dans {n} essai', ' · dans {n} essais')) + '</small>' +
          (h2 ? '<b class="dle-emo">' + esc(c.emo.join(' ')) + '</b>' : '<b>' + T('Emojis') + '</b>') + '</div></div>';
        return html;
      }
      if (MODE === 'pouvoir') {
        t = data.byId[target]; s = data.series[t.u];
        html = '<p class="dle-ask">' + T('À qui appartient ce pouvoir ?') + '</p><blockquote class="dle-quote">' + esc(t.p[0]) + '</blockquote>';
        html += '<div class="dle-hints">' +
          hint(w >= 2, T('Famille'), data.cats[s.c], 2 - w) + hint(w >= 4, T('Univers'), s.n, 4 - w) + hint(w >= 5, T('Initiale'), t.name.charAt(0), 5 - w) + '</div>';
        if (state.done && t.p[1]) html += '<p class="muted" style="margin-top:12px">' + T('Nom du pouvoir : <b>{p}</b>', { p: esc(t.p[1]) }) + '</p>';
        return html;
      }
      if (MODE === 'emoji') {
        t = data.byId[target];
        var shown = state.done ? t.emo.length : Math.min(t.emo.length, 1 + w);
        html = '<p class="dle-ask">' + T('Quel personnage se cache derrière ces emojis ?') + '</p><div class="dle-emojis">';
        t.emo.forEach(function (em, i) {
          html += i < shown ? '<span class="dle-e on">' + esc(em) + '</span>' : '<span class="dle-e">?</span>';
        });
        html += '</div>';
        html += '<div class="dle-hints">' + hint(w >= t.emo.length, T('Univers'), data.series[t.u].n, t.emo.length - w) + '</div>';
        return html;
      }
      // univers
      var clues = data.univers[target];
      var k = state.done ? clues.length : Math.min(clues.length, 1 + w);
      html = '<p class="dle-ask">' + T('De quel univers parle-t-on ?') + '</p><ol class="dle-clues">';
      clues.forEach(function (cl, i) {
        html += i < k ? '<li class="on">' + esc(cl) + '</li>' : '<li>' + T('Indice {n} : à débloquer', { n: i + 1 }) + '</li>';
      });
      html += '</ol><div class="dle-hints">' + hint(w >= 5, T('Famille'), data.cats[data.series[target].c], 5 - w) + '</div>';
      return html;
    }
    function hint(open, label, value, left) {
      open = open || state.done;
      return '<div class="dle-hint' + (open ? ' on' : '') + '"><small>' + label + (open ? '' : P(left, ' · dans {n} erreur', ' · dans {n} erreurs')) + '</small><b>' +
        (open ? esc(value) : '?') + '</b></div>';
    }

    function inputHTML() {
      var ph = MODE === 'univers' ? T("Tape le nom d'un univers…") : T("Tape le nom d'un personnage…");
      return '<form class="dle-form" autocomplete="off"><label class="sr-only" for="dle-in">' + ph + '</label>' +
        '<div class="dle-field"><input id="dle-in" placeholder="' + ph + '" role="combobox" aria-expanded="false" aria-controls="dle-list" aria-autocomplete="list">' +
        '<ul class="dle-list" id="dle-list" role="listbox" hidden></ul></div>' +
        '<button class="btn btn-gold" type="submit">' + T('Valider') + '</button></form>';
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
      out.sort(function (a, b) { return a.sc - b.sc || a.label.localeCompare(b.label, KQ.lang); });
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
          if (norm(input.value)) { list.innerHTML = '<li class="none">' + T('Aucun résultat') + '</li>'; list.hidden = false; }
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
        else if (norm(input.value)) KQ.toast(T('Choisis un nom dans la liste proposée.'));
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
      function setCmp(a, b, near) {
        var same = a.length === b.length && a.every(function (x) { return b.indexOf(x) >= 0; });
        if (same) return 'ok';
        if (a.some(function (x) { return b.indexOf(x) >= 0; })) return 'near';
        if (near && a.some(function (x) {
          return near.some(function (grp) { return grp.indexOf(x) >= 0 && b.some(function (y) { return grp.indexOf(y) >= 0; }); });
        })) return 'near';
        return 'no';
      }
      function arrow(a, b) { return a === b ? '' : (b > a ? '↑' : '↓'); }
      var ai = data.ages.indexOf(g.a), at = data.ages.indexOf(t.a);
      return [
        [su.n, g.u === t.u ? 'ok' : 'no'],
        [data.cats[su.c], su.c === tu.c ? 'ok' : 'no'],
        [GENRE[g.g], g.g === t.g ? 'ok' : 'no'],
        [g.e.join(', '), setCmp(g.e, t.e)],
        [g.r, g.r === t.r ? 'ok' : 'no'],
        [g.s.join(', '), setCmp(g.s, t.s)],
        [g.a, ai === at ? 'ok' : 'no', arrow(ai, at)],
        [g.h.join(', '), setCmp(g.h, t.h, data.hairNear)],
        [String(g.y), g.y === t.y ? 'ok' : 'no', arrow(g.y, t.y)]
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
            return '<td class="c-' + c[1] + '" data-label="' + COLS[i] + '">' + esc(c[0]) +
              (c[2] ? ' <span class="dle-arrow" aria-label="' + (c[2] === '↑' ? T('la cible est au-dessus') : T('la cible est en dessous')) + '">' + c[2] + '</span>' : '') + '</td>';
          }).join('');
          return '<tr><th scope="row" class="' + (id === target ? 'c-ok' : '') + '">' + esc(g.name) + '</th>' + cells + '</tr>';
        }).join('');
        return '<div class="dle-table-wrap"><table class="dle-table"><thead><tr><th scope="col">' + T('Personnage') + '</th>' +
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
          (sub ? '<span>' + T(sub) + '</span>' : '') + '</li>';
      }).join('') + '</ul>';
    }

    /* ----- fin de partie ----- */
    function shareText() {
      var n = state.guesses.length;
      var lines = [CONF.ico + ' ' + T('Kamidle n°{n} : {m}', { n: idx + 1, m: CONF.label })];
      if (MODE === 'personnage') {
        lines.push(state.win ? P(n, 'Trouvé en {n} essai', 'Trouvé en {n} essais') : T('Pas trouvé'));
        var t = data.byId[target];
        var em = { ok: '🟩', near: '🟨', no: '🟥' };
        var rows = state.guesses.map(function (id) {
          return cmpPerso(data.byId[id], t).map(function (c) { return em[c[1]]; }).join('');
        });
        if (rows.length > 8) { lines = lines.concat(rows.slice(0, 3)); lines.push('⋯ ' + T('{n} de plus', { n: rows.length - 6 })); lines = lines.concat(rows.slice(-3)); }
        else lines = lines.concat(rows);
      } else if (MODE === 'mot') {
        lines.push((state.win ? n : 'X') + '/' + CONF.max + ' · ' + T('{n} lettres', { n: target.length }));
        var emm = { ok: '🟩', near: '🟨', no: '⬛' };
        state.guesses.forEach(function (gw) { lines.push(scoreWord(gw, target).map(function (x) { return emm[x]; }).join('')); });
      } else {
        lines.push(state.guesses.map(function (id) { return id === target ? '🟩' : '🟥'; }).join('') +
          (state.win ? ' ' + n + '/' + CONF.max : ' X/' + CONF.max));
      }
      lines.push('https://kamiquiz.com' + U('/dle/' + MODE + '/'));
      return lines.join('\n');
    }

    function renderEnd() {
      var box = root.querySelector('#dle-end');
      var sid = serieOf(target), s = sid ? data.series[sid] : null;
      var n = state.guesses.length;
      var st = practice ? null : store.get(statsKey(MODE), null);
      var html = '<div class="dle-result ' + (state.win ? 'win' : 'lose') + '">' +
        '<p class="dle-verdict">' + (state.win ? (n === 1 ? T("Du premier coup ! C'était") : T("Bien joué ! C'était")) : T("Perdu… C'était")) + '</p>' +
        '<p class="dle-answer">' + esc(nameOf(target)) + '</p>' +
        (MODE === 'mot' ? '<p class="dle-def">' + esc(data.mots[target]) + '</p>' : MODE !== 'univers' ? '<p class="muted">' + esc(s.n) + '</p>' : '') +
        (state.win ? '<p>' + P(n, 'Trouvé en <b>{n}</b> essai.', 'Trouvé en <b>{n}</b> essais.') + '</p>' : '');
      if (st) {
        html += '<div class="dle-stats"><div><b>' + st.played + '</b><small>' + T('parties') + '</small></div><div><b>' + (st.played ? Math.round(st.wins * 100 / st.played) : 0) + T(' %') + '</b><small>' + T('réussite') + '</small></div>' +
          '<div><b>' + st.streak + '</b><small>' + T('série') + '</small></div><div><b>' + st.best + '</b><small>' + T('record') + '</small></div></div>' +
          '<p class="dle-next">' + T('Prochaine énigme dans <b data-countdown></b>') + '</p>';
      }
      html += '<div class="btn-row" style="justify-content:center">' +
        (practice ? '' : '<button class="btn btn-gold" type="button" data-act="share">' + T('Partager mon résultat') + '</button>') +
        (s ? '<a class="btn" href="' + U('/quiz/' + s.s + '/') + '">' + T('Quiz {n}', { n: esc(s.n) }) + '</a>' : '') +
        '<button class="btn" type="button" data-act="practice">' + (practice ? T('Encore une') : T('Entraînement illimité')) + '</button>' +
        (practice ? '<button class="btn" type="button" data-act="daily">' + T("Revenir à l'énigme du jour") + '</button>' : '') +
        '</div>';
      if (!practice) {
        var next = Object.keys(MODES).filter(function (m) {
          if (m === MODE) return false;
          var s2 = store.get(stateKey(m, today), null);
          return !(s2 && s2.done);
        });
        if (next.length) {
          html += '<p class="dle-more">' + T("Encore à jouer aujourd'hui : ") + next.map(function (m) {
            return '<a href="' + U('/dle/' + m + '/') + '">' + MODES[m].ico + ' ' + MODES[m].label + '</a>';
          }).join(' · ') + '</p>';
        } else {
          html += '<p class="dle-more">' + T('Toutes les énigmes du jour sont terminées. Tu mérites ton rang de Kami.') + '</p>';
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
        navigator.clipboard.writeText(txt).then(function () { KQ.toast(T('Résultat copié, colle-le où tu veux !')); },
          function () { prompt(T('Copie ton résultat :'), txt); });
      } else {
        prompt(T('Copie ton résultat :'), txt);
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
        el.textContent = T('{h} h {m} min {s} s', { h: String(Math.floor(s / 3600)).padStart(2, '0'), m: String(Math.floor(s / 60) % 60).padStart(2, '0'), s: String(s % 60).padStart(2, '0') });
      }
      upd();
      timer = setInterval(upd, 1000);
    }

    /* ----- Mot mystère ----- */
    var dict = null;
    if (MODE === 'mot') {
      fetch(KQ.data('mots.txt')).then(function (r) { return r.ok ? r.text() : ''; }).then(function (t) {
        dict = new Set(t.split('\n'));
      }).catch(function () { dict = null; });
    }
    function scoreWord(gw, tw) {
      var res = [], left = {}, i;
      for (i = 0; i < tw.length; i++) {
        if (gw[i] === tw[i]) res[i] = 'ok';
        else left[tw[i]] = (left[tw[i]] || 0) + 1;
      }
      for (i = 0; i < tw.length; i++) {
        if (res[i]) continue;
        if (left[gw[i]]) { res[i] = 'near'; left[gw[i]]--; } else res[i] = 'no';
      }
      return res;
    }
    function keyStates() {
      var rank = { no: 1, near: 2, ok: 3 }, st = {};
      state.guesses.forEach(function (gw) {
        scoreWord(gw, target).forEach(function (r, i) {
          if (!st[gw[i]] || rank[r] > rank[st[gw[i]]]) st[gw[i]] = r;
        });
      });
      return st;
    }
    function renderMot() {
      var L = target.length, n = state.guesses.length, w = wrongCount();
      var head = '<div class="dle-top"><strong>' + (practice ? T('Entraînement') : T('Kamidle n°{n}', { n: idx + 1 })) + '</strong>' +
        '<span>' + CONF.ico + ' ' + CONF.label + ' · ' + Math.min(n, CONF.max) + '/' + CONF.max + '</span></div>';
      var rows = '';
      for (var r = 0; r < CONF.max; r++) {
        var gw = state.guesses[r], sc = gw ? scoreWord(gw, target) : null;
        var isCur = !gw && r === n && !state.done;
        rows += '<div class="dle-row' + (gw && r === n - 1 && justPlayed ? ' is-new' : '') + (isCur ? ' is-cur' : '') + '" style="--n:' + L + '">';
        for (var i = 0; i < L; i++) {
          var ch = gw ? gw[i] : isCur ? (cur[i] || '') : '';
          rows += '<span class="dle-tile' + (sc ? ' c-' + sc[i] : ch ? ' filled' : '') + '" style="--i:' + i + '">' + esc(ch) + '</span>';
        }
        rows += '</div>';
      }
      var hints = '<div class="dle-hints" style="margin-top:18px">' +
        hint(w >= 3, T('Première lettre'), target.charAt(0), 3 - w) + hint(w >= 5, T('Définition'), data.mots[target], 5 - w) + '</div>';
      var kb = '';
      if (!state.done) {
        var ks = keyStates();
        kb = '<div class="dle-kb" role="group" aria-label="' + T('Clavier') + '">' + KB.map(function (line) {
          return '<div>' + line.split('').map(function (k) {
            if (k === '<') return '<button type="button" class="dle-key wide" data-key="Backspace" aria-label="' + T('Effacer') + '">⌫</button>';
            if (k === '>') return '<button type="button" class="dle-key wide" data-key="Enter">' + T('Valider') + '</button>';
            return '<button type="button" class="dle-key' + (ks[k] ? ' c-' + ks[k] : '') + '" data-key="' + k + '">' + k + '</button>';
          }).join('') + '</div>';
        }).join('') + '</div>';
      }
      root.innerHTML = head + '<div class="dle-clue"><p class="dle-ask">' + T('Trouve le mot du jour : <b>{n} lettres</b>', { n: L }) + '</p>' +
        '<div class="dle-board">' + rows + '</div>' + hints + '</div>' + kb + '<div class="dle-end" id="dle-end"></div>';
      justPlayed = false;
      if (state.done) renderEnd();
    }
    function motKey(k) {
      if (MODE !== 'mot' || state.done) return;
      var L = target.length;
      if (k === 'Backspace') { cur = cur.slice(0, -1); renderMot(); return; }
      if (k === 'Enter') {
        if (cur.length < L) { KQ.toast(T('Le mot fait {n} lettres.', { n: L })); return; }
        if (!dict) { KQ.toast(T('Chargement du dictionnaire, réessaie dans une seconde.')); return; }
        if (!dict.has(cur) && !data.mots[cur]) { KQ.toast(T("« {w} » n'est pas dans notre dictionnaire.", { w: cur })); return; }
        if (state.guesses.indexOf(cur) >= 0) { KQ.toast(T('Tu as déjà essayé ce mot.')); return; }
        var gw = cur; cur = ''; justPlayed = true;
        guess(gw);
        return;
      }
      if (/^[A-Z]$/.test(k) && cur.length < L) { cur += k; renderMot(); }
    }
    if (MODE === 'mot') {
      document.addEventListener('keydown', function (ev) {
        if (ev.ctrlKey || ev.metaKey || ev.altKey) return;
        var k = ev.key;
        if (k === 'Enter' || k === 'Backspace') { ev.preventDefault(); motKey(k); return; }
        var up = k.length === 1 ? k.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toUpperCase() : '';
        if (/^[A-Z]$/.test(up)) motKey(up);
      });
      root.addEventListener('click', function (ev) {
        var b = ev.target.closest('[data-key]');
        if (b) motKey(b.getAttribute('data-key'));
      });
    }

    newGame(false);
  }
})();
