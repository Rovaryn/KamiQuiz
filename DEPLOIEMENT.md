# KamiQuiz v2 — déploiement et validation AdSense

## Ce que contient ce dossier

- `dist/` : le site prêt à mettre en ligne (c'est le seul dossier à déployer).
- `data/questions.src.json` : ta banque d'origine, jamais modifiée.
- `data/questions.json` : la banque nettoyée, utilisée par le site.
- `content/series.py` : textes de présentation des 42 séries.
- `content/guides/*.md` : les 10 guides.
- `static/` : CSS, JavaScript, polices et images.
- `build.py` : régénère tout `dist/` en une commande.
- `tools/` : nettoyage des questions, images, vérifications automatiques.

## Modifier le site plus tard

1. Ajouter ou corriger des questions dans `data/questions.src.json`.
2. `python3 tools/clean_data.py` (nettoyage), puis `python3 build.py` (génération).
3. `python3 tools/check_site.py` pour vérifier liens, JSON-LD, sitemap et redirections.
4. Redéployer le contenu de `dist/`.

## Mise en ligne sur Cloudflare Pages

1. Dashboard Cloudflare, Workers & Pages, projet KamiQuiz, Create deployment.
2. Déposer **le contenu** du dossier `dist/` (index.html doit être à la racine du dépôt, pas dans un sous-dossier).
3. Un déploiement remplace l'intégralité du site : les anciens fichiers (naruto.html, quiz.html, consent.js…) disparaissent, et le fichier `_redirects` renvoie leurs anciennes adresses vers les nouvelles en 301.
4. Vérifier après déploiement : `kamiquiz.com/naruto.html` doit rediriger vers `kamiquiz.com/quiz/naruto/`, et une adresse inventée doit afficher la page 404 du site.

## AdSense : les réglages à faire dans la console

1. **Confidentialité et messages** : créer un message « Réglementations européennes » (CMP certifiée de Google), l'associer à kamiquiz.com et le publier. Le site n'a plus de bannière maison : c'est ce message qui gère le consentement en Europe, au Royaume-Uni et en Suisse.
2. **Annonces, Par site** : activer les annonces automatiques pour kamiquiz.com.
3. Ne relancer la demande d'examen qu'après l'indexation (voir ci-dessous).

## Search Console : faire indexer le nouveau site

1. Soumettre à nouveau `https://kamiquiz.com/sitemap.xml` (59 adresses).
2. Demander l'indexation de l'accueil, de `/quiz/`, de `/guides/` et de 5 à 7 pages séries populaires.
3. Attendre que la rubrique Pages affiche au moins 30 pages indexées avant de demander un nouvel examen AdSense.

## Classement mondial

Le site utilise le même Worker et le même format de score qu'avant. Seule nouveauté : les parties « Tout mélanger » envoient `series: "mix"`. Si le Worker filtre les séries autorisées, ajouter `mix` à sa liste.

## Publication programmée

Les séries et les guides ont une date (`date=` dans `content/series.py`, `date:` en tête de chaque guide). `python3 build.py --date 2026-11-16` génère le site tel qu'il doit être à cette date : seuls les contenus datés jusqu'à ce jour sont publiés, et les « Nouveaux univers » de l'accueil se mettent à jour seuls. Les zips prêts à déployer sont dans `releases/`, et le calendrier dans `PUBLICATION.md`.

## Kit réseaux sociaux

`python3 tools/make_social.py` régénère les visuels et les vidéos de `social/` à partir de la banque de questions. Les conseils de diffusion sont dans `social/PROMOTION.md`.
