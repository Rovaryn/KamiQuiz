"""Bandes-annonces officielles affichées sur les pages des séries.

Règle : uniquement des vidéos publiées par la chaîne YouTube officielle du diffuseur ou de l'éditeur
(Netflix France, PlayStation France…), jamais une copie mise en ligne par un tiers. La vidéo n'est
chargée qu'au clic, depuis youtube-nocookie.com, et la vignette affichée avant est notre visuel maison.

TRAILERS[clé de série] = (identifiant YouTube, titre affiché, chaîne officielle)
Pour en ajouter une : vérifier la chaîne qui a publié la vidéo, puis ajouter une ligne.
"""

TRAILERS = {
    'strangerthings': ('h0ceRxg6YKc', 'Stranger Things 4, volume 2 : bande-annonce VF', 'Netflix France'),
    'squidgame': ('aQAbx8XZBII', 'Squid Game, saison 3 : bande-annonce officielle VF', 'Netflix France'),
    'casapapel': ('M9sK3f1XHSk', 'La casa de papel, partie 5 volume 2 : bande-annonce officielle VF', 'Netflix France'),
    'peakyBlinders': ('QlU-5RsnYTk', 'Peaky Blinders, saison 6 : bande-annonce officielle', 'Netflix France'),
    'onepiece': ('WuxxltXEeB4', 'One Piece, arc Egghead partie 2 : bande-annonce officielle VOSTFR', 'Netflix France'),
    'demonslayer': ('Mj6KuQU2Qzo', "Demon Slayer, l'Entraînement des piliers : bande-annonce VOSTFR", 'Netflix France'),
    'eafc': ('w9cJQn7BdVQ', 'EA Sports FC 26 : trailer de révélation VF', 'PlayStation France'),
    'valorant': ('MZ0VdLJp4kg', 'Valorant : trailer cinématique de lancement console « Incursions »', 'PlayStation France'),
}
