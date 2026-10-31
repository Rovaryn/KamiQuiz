/* KamiQuiz — application de quiz (/jouer/) */
(function () {
  'use strict';

  var KQ = window.KQ;
  var esc = KQ.esc;
  var SERIES = window.KQ_SERIES || {};
  var params = new URLSearchParams(location.search);
  var key = params.get('s') || 'mix';
  if (key !== 'mix' && !SERIES[key]) key = 'mix';

  var MODES = {
    libre:     { name: 'Mode libre',    ico: '🎲', desc: '20 questions au hasard, sans chrono. Idéal pour découvrir.', count: 20 },
    chrono:    { name: 'Contre la montre', ico: '⚡', desc: '15 secondes par question. Plus vous répondez vite, plus le multiplicateur grimpe.', count: 20, timer: 15 },
    survie:    { name: 'Survie',        ico: '🛡️', desc: 'Trois vies. Chaque erreur en coûte une. Jusqu\'où tiendrez-vous ?', count: Infinity, lives: 3 },
    maitre:    { name: 'Ascension',     ico: '⭐', desc: '30 questions de plus en plus dures, avec bonus de série de bonnes réponses.', count: 30, progressive: true },
    expert:    { name: 'Expert',        ico: '💀', desc: 'Uniquement les questions difficiles. Pour ceux qui connaissent chaque détail.', count: 15, minLevel: 3 },
    categorie: { name: 'Par thème',     ico: '📚', desc: 'Choisissez un ou plusieurs thèmes et entraînez-vous là où vous voulez.', count: 20, pickCats: true },
    duel:      { name: 'Duel à deux',   ico: '🤝', desc: 'Deux joueurs sur le même écran répondent chacun leur tour. 10 questions chacun.', count: 20, duel: true }
  };
  var LEVELS = { 1: 'Facile', 2: 'Moyen', 3: 'Difficile', 4: 'Expert' };
  var DEFAULT_RANKS = ['Novice', 'Apprenti', 'Initié', 'Confirmé', 'Maître', 'Kami'];

  var $ = function (s) { return document.querySelector(s); };
  var screens = ['loading', 'setup', 'play', 'result'];
  function show(name) {
    screens.forEach(function (n) { $('#s-' + n).hidden = n !== name; });
    window.scrollTo({ top: 0, behavior: 'auto' });
  }

  var data = null;          // { name, color, ranks, cats, q: [...] }
  var meta = SERIES[key] || { name: 'Tout mélanger', slug: '', color: '#d4a843' };
  var state = null;

  function shuffle(a) {
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }
  function qid(q) { var h = 0, s = q.q; for (var i = 0; i < s.length; i++) h = (h * 31 + s.charCodeAt(i)) | 0; return h; }

  /* ---------- Chargement ---------- */
  document.documentElement.style.setProperty('--accent', meta.color);
  $('[data-app-name]').textContent = meta.name;
  document.title = (key === 'mix' ? 'Quiz tout mélangé' : 'Jouer au quiz ' + meta.name) + ' — KamiQuiz';

  var loader = key === 'mix'
    ? fetch('/data/all.json').then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    : KQ.loadSerie(key);

  loader.then(function (d) {
    data = d;
    if (!data.ranks || data.ranks.length < 2) data.ranks = DEFAULT_RANKS;
    buildSetup();
    var m = params.get('m');
    if (m && MODES[m] && !MODES[m].pickCats && !MODES[m].duel) start(m);
    else { show('setup'); if (m && MODES[m]) choose(m); }
  }).catch(function () {
    $('#s-loading').innerHTML = '<div class="error-box">Les questions n\'ont pas pu être chargées. Vérifiez votre connexion puis <a href="">rechargez la page</a>.</div>';
  });

  /* ---------- Écran de choix du mode ---------- */
  function buildSetup() {
    var grid = $('#mode-grid');
    grid.innerHTML = Object.keys(MODES).map(function (id) {
      var m = MODES[id];
      return '<button class="mode" type="button" data-mode="' + id + '"><span class="mode-ico" aria-hidden="true">' + m.ico +
        '</span><span class="mode-name">' + m.name + '</span><p>' + m.desc + '</p></button>';
    }).join('');
    grid.addEventListener('click', function (e) {
      var b = e.target.closest('[data-mode]');
      if (b) choose(b.getAttribute('data-mode'));
    });

    var cats = Object.keys(data.cats || {});
    var counts = {};
    data.q.forEach(function (q) { counts[q.cat] = (counts[q.cat] || 0) + 1; });
    $('#cat-chips').innerHTML = cats.map(function (c) {
      return '<button class="chip" type="button" aria-pressed="false" data-cat="' + esc(c) + '">' +
        esc((data.cats[c] && data.cats[c].i) || '') + ' ' + esc(c) + ' <span class="muted">' + (counts[c] || 0) + '</span></button>';
    }).join('');
    $('#cat-chips').addEventListener('click', function (e) {
      var b = e.target.closest('[data-cat]');
      if (b) b.setAttribute('aria-pressed', b.getAttribute('aria-pressed') === 'true' ? 'false' : 'true');
    });
    $('#cat-go').addEventListener('click', function () {
      var picked = Array.prototype.map.call(document.querySelectorAll('#cat-chips [aria-pressed="true"]'), function (b) { return b.getAttribute('data-cat'); });
      if (!picked.length) { KQ.toast('Choisissez au moins un thème.'); return; }
      start('categorie', { cats: picked });
    });
    $('#duel-go').addEventListener('click', function () {
      var a = $('#p1').value.trim() || 'Joueur 1';
      var b = $('#p2').value.trim() || 'Joueur 2';
      start('duel', { players: [a, b] });
    });
    var nameInput = $('#save-name');
    if (nameInput) nameInput.value = KQ.store.get('kq_name', '');
  }

  function choose(id) {
    $('#cat-picker').hidden = id !== 'categorie';
    $('#duel-picker').hidden = id !== 'duel';
    if (id === 'categorie') $('#cat-picker').scrollIntoView({ behavior: 'smooth', block: 'center' });
    else if (id === 'duel') { $('#duel-picker').scrollIntoView({ behavior: 'smooth', block: 'center' }); $('#p1').focus(); }
    else start(id);
  }

  /* ---------- Sélection des questions ---------- */
  function pickQuestions(mode, opts) {
    var m = MODES[mode];
    var pool = data.q.slice();
    if (mode === 'categorie') pool = pool.filter(function (q) { return opts.cats.indexOf(q.cat) >= 0; });
    if (m.minLevel) {
      var hard = pool.filter(function (q) { return q.d >= m.minLevel; });
      if (hard.length < 10) hard = pool.filter(function (q) { return q.d >= m.minLevel - 1; });
      pool = hard;
    }
    // On privilégie les questions jamais vues sur cet appareil
    var seenKey = 'kq_seen_' + key;
    var seen = KQ.store.get(seenKey, []);
    var fresh = pool.filter(function (q) { return seen.indexOf(qid(q)) < 0; });
    var want = m.count === Infinity ? pool.length : m.count;
    if (fresh.length < Math.min(want, pool.length)) { seen = []; fresh = pool.slice(); }
    shuffle(fresh);
    var chosen = fresh.slice(0, want);
    if (chosen.length < want && m.count !== Infinity) {
      var rest = shuffle(pool.filter(function (q) { return chosen.indexOf(q) < 0; }));
      chosen = chosen.concat(rest.slice(0, want - chosen.length));
    }
    if (m.progressive) chosen.sort(function (a, b) { return a.d - b.d; });
    KQ.store.set(seenKey, seen.concat(chosen.map(qid)).slice(-2000));
    return chosen;
  }

  /* ---------- Partie ---------- */
  function start(mode, opts) {
    opts = opts || {};
    var list = pickQuestions(mode, opts);
    if (!list.length) { KQ.toast('Aucune question ne correspond à ce choix.'); return; }
    state = {
      mode: mode, m: MODES[mode], list: list, i: 0, right: 0, answered: 0,
      lives: MODES[mode].lives || 0, points: 0, streak: 0, bestStreak: 0,
      log: [], opts: opts, players: opts.players || null, pScore: [0, 0], locked: false, timer: null
    };
    $('[data-mode-name]').textContent = state.m.name;
    show('play');
    render();
  }

  function render() {
    var s = state, q = s.list[s.i];
    s.locked = false;
    var order = shuffle([0, 1, 2, 3]);
    s.current = { q: q, order: order, right: order.indexOf(q.c) };

    var total = s.m.count === Infinity ? null : s.list.length;
    var left = '';
    if (s.players) left = '<b>' + esc(s.players[s.i % 2]) + '</b> à vous de jouer';
    else left = 'Question <b>' + (s.i + 1) + '</b>' + (total ? ' sur ' + total : '');
    var right = '';
    if (s.players) right = esc(s.players[0]) + ' <b>' + s.pScore[0] + '</b> · ' + esc(s.players[1]) + ' <b>' + s.pScore[1] + '</b>';
    else if (s.lives) right = '<span class="lives" aria-label="' + s.lives + ' vies restantes">' + '♥'.repeat(s.lives) + '<span style="opacity:.25">' + '♥'.repeat(MODES.survie.lives - s.lives) + '</span></span> · <b>' + s.right + '</b> bonnes';
    else if (s.m.timer || s.m.progressive) right = '<b>' + s.points + '</b> points' + (s.streak > 1 ? ' · <span class="combo">série ×' + s.streak + '</span>' : '');
    else right = '<b>' + s.right + '</b> bonne' + (s.right > 1 ? 's' : '') + ' réponse' + (s.right > 1 ? 's' : '');
    $('#hud-left').innerHTML = left;
    $('#hud-right').innerHTML = right;
    $('#bar').style.width = (total ? (s.i / total) * 100 : Math.min(100, s.i * 4)) + '%';

    var cat = data.cats && data.cats[q.cat] ? data.cats[q.cat].i + ' ' : '';
    $('#q-meta').innerHTML = '<span class="chip"><i></i>' + esc(cat + q.cat) + '</span><span>' + LEVELS[q.d] + '</span>';
    $('#q-text').textContent = q.q;
    $('#q-answers').innerHTML = order.map(function (idx, pos) {
      return '<button class="answer" type="button" data-pos="' + pos + '"><kbd>' + 'ABCD'[pos] + '</kbd><span>' + esc(q.a[idx]) + '</span></button>';
    }).join('');
    $('#q-feedback').hidden = true;
    $('#next').hidden = true;

    var tb = $('#timer');
    clearInterval(s.timer);
    if (s.m.timer) {
      tb.hidden = false;
      var t0 = performance.now(), dur = s.m.timer * 1000;
      tb.classList.remove('low');
      s.timer = setInterval(function () {
        var p = Math.max(0, 1 - (performance.now() - t0) / dur);
        tb.firstElementChild.style.transform = 'scaleX(' + p + ')';
        tb.classList.toggle('low', p < .3);
        s.remaining = p;
        if (p <= 0) { clearInterval(s.timer); answer(-1); }
      }, 50);
    } else tb.hidden = true;
    var first = document.querySelector('#q-answers .answer');
    if (first && document.activeElement && document.activeElement.closest('#s-play')) first.focus();
  }

  function answer(pos) {
    var s = state;
    if (s.locked) return;
    s.locked = true;
    clearInterval(s.timer);
    var c = s.current, ok = pos === c.right;
    s.answered++;
    if (ok) {
      s.right++; s.streak++;
      s.bestStreak = Math.max(s.bestStreak, s.streak);
      if (s.m.timer) s.points += Math.round(100 * (1 + Math.floor((s.remaining || 0) * 5)));
      else if (s.m.progressive) s.points += 100 * c.q.d + 25 * Math.min(s.streak - 1, 8);
      if (s.players) s.pScore[s.i % 2]++;
    } else {
      s.streak = 0;
      if (s.lives) s.lives--;
    }
    s.log.push({ q: c.q, ok: ok, given: pos >= 0 ? c.q.a[c.order[pos]] : null });

    document.querySelectorAll('#q-answers .answer').forEach(function (b, i) {
      b.disabled = true;
      if (i === c.right) b.classList.add('is-right');
      else if (i === pos) b.classList.add('is-wrong');
      else b.classList.add('is-dim');
    });
    var fb = $('#q-feedback');
    var head = ok ? 'Bonne réponse.' : (pos < 0 ? 'Temps écoulé.' : 'Mauvaise réponse.') + ' Il fallait répondre « ' + esc(c.q.a[c.q.c]) + ' ».';
    fb.innerHTML = '<strong>' + head + '</strong> ' + esc(c.q.fb || '');
    fb.hidden = false;

    var over = (s.lives === 0 && s.m.lives) || s.i + 1 >= s.list.length;
    var nx = $('#next');
    nx.textContent = over ? 'Voir mon résultat' : 'Question suivante';
    nx.hidden = false;
    nx.focus();
  }

  function next() {
    var s = state;
    if ((s.m.lives && s.lives === 0) || s.i + 1 >= s.list.length) return finish();
    s.i++;
    render();
  }

  $('#q-answers').addEventListener('click', function (e) {
    var b = e.target.closest('.answer');
    if (b && !b.disabled) answer(+b.getAttribute('data-pos'));
  });
  $('#next').addEventListener('click', next);
  $('#quit').addEventListener('click', function () {
    clearInterval(state && state.timer);
    if (state && state.answered) finish(); else show('setup');
  });
  document.addEventListener('keydown', function (e) {
    if ($('#s-play').hidden || e.ctrlKey || e.metaKey || e.altKey) return;
    if (e.target.tagName === 'INPUT') return;
    var k = e.key.toLowerCase();
    var map = { '1': 0, '2': 1, '3': 2, '4': 3, a: 0, b: 1, c: 2, d: 3 };
    if (k in map && !state.locked) { e.preventDefault(); answer(map[k]); }
    else if ((k === 'enter' || k === ' ') && state.locked && document.activeElement !== $('#next')) { e.preventDefault(); next(); }
  });

  /* ---------- Résultat ---------- */
  function finish() {
    var s = state;
    clearInterval(s.timer);
    var pct = s.answered ? Math.round((s.right / s.answered) * 100) : 0;
    var ranks = data.ranks;
    var r = ranks[Math.min(ranks.length - 1, Math.floor((pct / 100) * ranks.length))];
    if (s.m.lives) r = ranks[Math.min(ranks.length - 1, Math.floor(s.right / 5))];
    var box = $('#result-main');
    var verdict;
    if (s.players) {
      var a = s.pScore[0], b = s.pScore[1];
      verdict = a === b ? 'Égalité parfaite. Une revanche s\'impose.' : esc(s.players[a > b ? 0 : 1]) + ' remporte le duel.';
      box.innerHTML = '<p class="score">' + a + '<small> – </small>' + b + '</p>' +
        '<p class="rank">' + esc(s.players[0]) + ' contre ' + esc(s.players[1]) + '</p><p class="verdict">' + verdict + '</p>';
    } else {
      verdict = pct >= 90 ? 'Un sans-faute ou presque. Le titre est mérité.'
        : pct >= 70 ? 'Solide. Encore quelques détails et vous y êtes.'
        : pct >= 50 ? 'La moitié du chemin. Un passage par la révision et ça repart.'
        : 'Ce quiz vous a résisté. La page de révision est faite pour ça.';
      if (s.m.lives) verdict = s.right + ' bonnes réponses avant de tomber. ' + (s.right >= 20 ? 'Impressionnant.' : 'Vous pouvez aller plus loin.');
      box.innerHTML = '<p class="score">' + s.right + '<small>/' + s.answered + '</small></p>' +
        '<p class="rank">' + esc(r) + '</p><p class="verdict">' + verdict + '</p>' +
        '<div class="result-stats"><div>' + pct + '%<small>de réussite</small></div>' +
        (s.points ? '<div>' + s.points + '<small>points</small></div>' : '') +
        '<div>' + s.bestStreak + '<small>meilleure série</small></div></div>';
    }
    s.summary = { pct: pct, rank: r };

    var save = $('#save-box');
    save.hidden = !!s.players || s.answered < 5;
    $('#save-msg').textContent = s.answered < 5 ? '' : 'Votre pseudo et votre score seront visibles par tous dans le classement.';
    var revise = $('#to-revise');
    if (meta.slug) { revise.href = '/quiz/' + meta.slug + '/#questions'; revise.hidden = false; } else revise.hidden = true;

    var missed = s.log.filter(function (l) { return !l.ok; });
    $('#review').hidden = !missed.length;
    $('#review-list').innerHTML = missed.map(function (l) {
      return '<li><strong>' + esc(l.q.q) + '</strong>' +
        (l.given ? '<span class="wrong">Votre réponse : ' + esc(l.given) + '</span><br>' : '<span class="wrong">Pas de réponse</span><br>') +
        '<span class="right">Bonne réponse : ' + esc(l.q.a[l.q.c]) + '</span>' + (l.q.fb ? '<br>' + esc(l.q.fb) : '') + '</li>';
    }).join('');
    show('result');
  }

  $('#again').addEventListener('click', function () { start(state.mode, state.opts); });
  $('#other-mode').addEventListener('click', function () { show('setup'); });
  $('#share').addEventListener('click', function () {
    var s = state;
    var url = 'https://kamiquiz.com' + (meta.slug ? '/quiz/' + meta.slug + '/' : '/');
    var text = s.players
      ? 'Duel KamiQuiz sur ' + meta.name + ' : ' + s.pScore[0] + ' à ' + s.pScore[1] + '.'
      : 'J\'ai fait ' + s.right + '/' + s.answered + ' au quiz ' + meta.name + ' sur KamiQuiz (rang ' + s.summary.rank + '). Tu fais mieux ?';
    if (navigator.share) navigator.share({ title: 'KamiQuiz', text: text, url: url }).catch(function () {});
    else if (navigator.clipboard) navigator.clipboard.writeText(text + ' ' + url).then(function () { KQ.toast('Résultat copié. Collez-le où vous voulez.'); });
  });

  $('#save-form').addEventListener('submit', function (e) {
    e.preventDefault();
    var s = state;
    var name = $('#save-name').value.trim().replace(/\s+/g, ' ').slice(0, 20);
    if (name.length < 2) { KQ.toast('Choisissez un pseudo d\'au moins 2 caractères.'); return; }
    KQ.store.set('kq_name', name);
    var entry = {
      name: name, series: key === 'mix' ? 'mix' : key, mode: s.m.name,
      sc: s.right, tot: s.answered, pct: s.summary.pct, bs: s.bestStreak,
      date: new Date().toLocaleDateString('fr-FR')
    };
    var btn = $('#save-btn');
    btn.disabled = true;
    fetch(KQ.LB_API + '/api/score', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(entry) })
      .then(function (r) { return r.json(); })
      .then(function (res) {
        $('#save-msg').textContent = res && res.rank ? 'Score enregistré. Vous êtes ' + res.rank + (res.rank === 1 ? 'er' : 'e') + ' au classement.' : 'Score enregistré.';
        $('#save-form').hidden = true;
      })
      .catch(function () {
        btn.disabled = false;
        $('#save-msg').textContent = 'Le classement ne répond pas. Réessayez dans un instant.';
      });
  });
})();
