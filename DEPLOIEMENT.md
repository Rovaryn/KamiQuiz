# KamiQuiz — mise en ligne et validation AdSense

## Comment le site est publié

Le code vit sur GitHub (`Rovaryn/KamiQuiz`). Le projet Cloudflare Pages `kamiquiz-site` est relié au dépôt et sert kamiquiz.com et www.kamiquiz.com. Réglages de construction : commande `python3 build.py`, dossier de sortie `dist`, variable `PYTHON_VERSION=3.12`.

Chaque modification passe par une pull request. La tâche GitHub « Vérifications » génère le site, lance `check_site.py` et les tests dans un vrai navigateur ; Cloudflare publie en parallèle un aperçu de la pull request à une adresse en `.pages.dev`. Quand les vérifications sont vertes et que l'aperçu convient, on fusionne : le site se met à jour tout seul en une à deux minutes.

La tâche « Reconstruction quotidienne » appelle chaque nuit le deploy hook enregistré dans le secret GitHub `CF_DEPLOY_HOOK`, pour publier les contenus datés (voir `PUBLICATION.md`). Si le hook est recréé dans Cloudflare, mettre à jour ce secret.

L'ancien projet Cloudflare `kamiquiz` (déploiement par zip, sans lien avec GitHub) peut être supprimé une fois le nouveau stable depuis quelques semaines.

## Travailler en local

`python3 build.py` génère le site à la date du jour, `python3 build.py --date 2026-11-16` tel qu'il sera à cette date. Ensuite `python3 tools/check_site.py` (0 erreur attendue), puis `cd dist && python3 -m http.server 8765` dans un terminal et `python3 tools/browser_test.py` dans un autre (`ÉCHECS : 0` attendu).

## AdSense : réglages dans la console

Dans « Confidentialité et messages », le message « Réglementations européennes » (CMP certifiée de Google) gère le consentement en Europe, au Royaume-Uni et en Suisse ; le site n'a pas de bandeau maison. Dans « Annonces », les annonces automatiques sont activées pour kamiquiz.com. Ne redemander un examen qu'en suivant les critères de `PUBLICATION.md`.

## Search Console

Le sitemap est `https://kamiquiz.com/sitemap.xml`. Après chaque nouveauté, coller l'adresse de la page dans la barre du haut et demander l'indexation.

## Classement mondial

Le Worker `polished-haze-58ed` reçoit les scores (`POST /api/score`). Les parties « Tout mélanger » envoient `series: "mix"`.

## Réseaux sociaux

`python3 tools/make_social.py` (visuels et vidéos courtes), `tools/make_long_videos.py` (vidéos de plus d'une minute) et `tools/make_voiced_videos.py` (vidéos narrées) écrivent dans `social/`, qui n'est pas suivi par Git. Les conseils de diffusion sont dans `docs/PROMOTION.md`.
