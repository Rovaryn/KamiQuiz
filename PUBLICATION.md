# Calendrier de mise en ligne

Il n'y a plus rien à déployer à la main. Chaque nuit vers 1 h (heure de Montréal), la tâche GitHub « Reconstruction quotidienne » relance la construction du site sur Cloudflare Pages, et les séries et guides datés apparaissent seuls le jour prévu. Le tableau sert à savoir quoi publier sur les réseaux, et quelles pages faire indexer dans Search Console. La colonne « Fichier » indique l'ancien zip correspondant, qui ne sert plus.

| Date | Ancien zip (inutile) | Nouveauté | À publier sur les réseaux le même jour |
|---|---|---|---|
| Dès maintenant | `00-2026-10-27-kamiquiz.zip` | Correction du robots.txt et de l'image de partage, lancement du Kamidle (4 jeux du jour) | Annonce du Kamidle (voir plus bas) |
| Lundi 2 novembre | `01-2026-11-02-kamiquiz.zip` | Quiz Frieren (58 questions) et son guide | `videos/01-frieren.mp4` |
| Lundi 9 novembre | `02-2026-11-09-kamiquiz.zip` | Guide sur le Nen de Hunter × Hunter | Carrousel `posts/16-death-note` ou un autre |
| Lundi 16 novembre | `03-2026-11-16-kamiquiz.zip` | Quiz Chainsaw Man (54 questions) et son guide | `videos/05-chainsaw-man.mp4` |
| Lundi 23 novembre | `04-2026-11-23-kamiquiz.zip` | Guide sur l'énergie occulte de Jujutsu Kaisen | `videos/07-jujutsu-kaisen.mp4` |
| Lundi 30 novembre | `05-2026-11-30-kamiquiz.zip` | Quiz Spy × Family (54 questions) et son guide | `videos/09-spy-x-family.mp4` |
| Lundi 7 décembre | `06-2026-12-07-kamiquiz.zip` | Article « Comment nous écrivons et vérifions les questions » | Rien de spécial |

Après chaque déploiement, dans Search Console : colle l'adresse de la nouvelle page dans la barre du haut et clique sur « Demander l'indexation ». Les adresses sont dans le tableau ci-dessous.

| Date | Adresses à faire indexer |
|---|---|
| Dès maintenant | https://kamiquiz.com/dle/ et https://kamiquiz.com/dle/personnage/ |
| 2 novembre | https://kamiquiz.com/quiz/frieren/ et https://kamiquiz.com/guides/frieren-guide/ |
| 9 novembre | https://kamiquiz.com/guides/nen-hunter-x-hunter/ |
| 16 novembre | https://kamiquiz.com/quiz/chainsaw-man/ et https://kamiquiz.com/guides/demons-chainsaw-man/ |
| 23 novembre | https://kamiquiz.com/guides/energie-occulte-jujutsu-kaisen/ |
| 30 novembre | https://kamiquiz.com/quiz/spy-x-family/ et https://kamiquiz.com/guides/secrets-famille-forger-spy-x-family/ |
| 7 décembre | https://kamiquiz.com/guides/comment-nous-ecrivons-les-questions/ |

## Le Kamidle

Les quatre jeux du jour (personnage, pouvoir, emojis, univers) sont en ligne dès le zip 00. Leur calendrier est calculé à l'avance et identique dans tous les zips : l'énigme du jour reste la même quel que soit le déploiement en ligne. Les personnages de Frieren, Chainsaw Man et Spy × Family entrent dans le tirage le jour où leur quiz est publié.

Pour l'annonce, un message simple suffit, sur Discord ou en story : « Nouveau sur KamiQuiz : le Kamidle. Chaque jour, un personnage, un pouvoir, des emojis et un univers à deviner. Partage ta grille en réponse 👇 kamiquiz.com/dle/ ». Ensuite, poste ta propre grille de résultats quelques jours par semaine : c'est ce qui donne envie aux autres d'essayer.

## Quand redemander AdSense

Pas avant la mi-décembre, et seulement si ces trois conditions sont réunies :

1. Search Console, rubrique « Pages » : la grande majorité des adresses du sitemap sont indexées (environ 60 sur 68 en décembre).
2. Search Console, rubrique « Performances » : des clics arrivent chaque semaine depuis Google, même peu.
3. Des visiteurs arrivent aussi depuis les réseaux sociaux (visible dans les statistiques Cloudflare, onglet Analytics du projet).

Si ce n'est pas le cas mi-décembre, continue les publications et attends janvier : un site qui grandit régulièrement a plus de chances qu'un site présenté trop tôt.
