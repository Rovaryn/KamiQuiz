# KamiQuiz — règles du projet

KamiQuiz (kamiquiz.com) est un site de quiz gratuit en français, statique, hébergé sur Cloudflare Pages.
Propriétaire : Nano. Objectif : être validé par Google AdSense (éditeur `ca-pub-6970710961658841`), puis grandir.

## Façon de travailler avec Nano

- Toujours répondre et écrire le contenu du site **en français**.
- Respecter le design existant. Charte : fond `#07080f`, or `#d4a843`, polices Bebas Neue (titres), Playfair Display (citations, questions), Inter (texte).
- Peu de listes à puces dans les réponses et dans les textes du site : de la prose claire.
- **Tout valider avant de livrer** : rien ne doit casser. Lancer `check_site.py` et `browser_test.py` après chaque modification.
- Travailler sur une branche et ouvrir une pull request ; Nano teste l'aperçu Cloudflare avant de fusionner.

## Terminologie EA Sports FC (obligatoire)

Chimie, DCE (Défis de création d'équipe), EDSM (Équipe de la semaine), Pièces FUT, Mode Carrière.

## Règles AdSense et contenu (ne jamais enfreindre)

- Aucune fausse note ni faux avis (pas d'`AggregateRating` inventé).
- Aucune image protégée par le droit d'auteur (captures d'animés, visuels officiels) : c'est pour cela qu'il n'y a pas de mode « devine les yeux ».
- Le consentement en Europe passe par la CMP certifiée Google configurée dans AdSense (« Confidentialité et messages »), pas par un bandeau maison.
- `robots.txt` ne bloque rien ; `/jouer/` est exclu avec `noindex, follow`.
- Les questions de chaque série sont écrites en HTML statique sur sa page (mode révision) : c'est la réponse au refus « contenu à faible valeur ».
- Ne publier que des informations dont on est sûr ; en cas de doute, retirer le détail plutôt que l'inventer.

## Structure

- `build.py` : génère tout le site dans `dist/` (bibliothèque standard Python uniquement).
  `python3 build.py --date AAAA-MM-JJ` génère le site tel qu'il doit être à cette date.
- `content/series.py` : métadonnées des 45 séries (avec `date` de publication pour les nouvelles).
- `content/guides/*.md` : guides, avec `date:` en tête.
- `content/new_series.py` : questions des séries ajoutées récemment.
- `content/dle.py` : données du Kamidle (personnages, pouvoirs, emojis, univers, mots, âges, cheveux, années).
  Le calendrier part de l'ordre figé `SCHED_V1` : ne jamais le modifier, sinon les énigmes passées et du jour changent.
  Pour retirer un personnage, le supprimer de `CHARS` (il est remplacé seul les jours où il tombait) ; un nouveau va en fin de file.
- `data/mots-fr.txt` : dictionnaire des essais du Mot mystère (licence MIT, voir `data/mots-fr.LICENSE.txt`).
- `data/questions.src.json` : banque d'origine, **ne jamais modifier** ; `tools/clean_data.py` produit `data/questions.json`.
- `static/` : CSS, JS (`site.js`, `quiz.js`, `dle.js`), polices auto-hébergées, images.
- `tools/` : vérifications, images, kit réseaux sociaux, vidéos (longues et narrées).
- `docs/` : documents de travail que les scripts ne touchent pas (promotion…).
- `.github/workflows/` : « Vérifications » sur chaque pull request, « Reconstruction quotidienne » chaque nuit.

## Liens partenaires

Le menu et le pied de page renvoient vers Letsdle (https://letsdle.com/), le site d'un ami de Nano : lien simple, non payé, ouvert dans un nouvel onglet.

## Commandes

```
python3 tools/clean_data.py        # après toute modification des questions
python3 build.py                   # génère dist/ à la date du jour
python3 tools/check_site.py        # 0 erreur attendue
(cd dist && python3 -m http.server 8765 &) && python3 tools/browser_test.py   # ÉCHECS : 0 attendu
```

## Publication programmée

Les séries et guides datés n'apparaissent qu'à partir de leur date. Une reconstruction quotidienne du site
(déclenchée sur Cloudflare Pages) suffit à les publier. Le calendrier du Kamidle est fixe (départ 2026-10-27)
et ne dépend pas de la date de génération.

## Classement mondial

Worker existant : `https://polished-haze-58ed.meklatiaymen8.workers.dev`
(`POST /api/score`, `GET /api/scores?series=X&limit=N` ou `?global=1`). Le mode mélangé envoie `series: "mix"`.

## Vidéos

`tools/make_voiced_videos.py` utilise la voix Piper SIWIS (CC BY 4.0, créditer « Voix : SIWIS, CC BY 4.0 »).
Le modèle n'est pas dans le dépôt : le retélécharger dans `tools/voix/siwis/` depuis
`https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-fr_FR-siwis-medium.tar.bz2`
et installer `pip install piper-tts`.
