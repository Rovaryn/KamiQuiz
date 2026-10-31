"""Corrections de la banque de questions, relue le 31 octobre 2026.

La banque d'origine (data/questions.src.json) n'est jamais modifiée : tools/clean_data.py applique
ces corrections au moment du nettoyage.

Format : FIX[série][texte exact de la question] =
    None                         -> question retirée (réponse fausse ou douteuse, impossible à corriger sûrement)
    {'q': ..., 'a': [...], 'c': n, 'fb': ...}   -> champs remplacés (les champs absents sont conservés)
"""

FIX = {}


def fix(serie, question, **changes):
    FIX.setdefault(serie, {})[question] = changes or None


def drop(serie, question):
    FIX.setdefault(serie, {})[question] = None


# ---------------------------------------------------------------- Naruto
S = 'naruto'
drop(S, "Que signifie 'Dattebayo' en japonais ?")                     # tic de langage sans traduction établie
fix(S, "Quel est le jutsu de Kakashi hérité de son ami Obito ?",
    q="Qu'est-ce que Kakashi a hérité de son ami Obito ?",
    a=["Son Sharingan", "Son Byakugan", "Son Rinnegan", "Son Mode Ermite"], c=0,
    fb="Obito, mourant, offre son œil gauche à Kakashi. C'est ce Sharingan qui permettra plus tard à Kakashi d'utiliser le Kamui. Le Chidori, lui, est une technique inventée par Kakashi.")
fix(S, "Quel est le nom de la technique ultime de Sasuke avec son Susanoo ?",
    a=["Kirin", "Amaterasu", "Chidori Nagashi", "La Flèche d'Indra"], c=3,
    fb="La Flèche d'Indra est la technique ultime du Susanoo de Sasuke, une flèche formée de chakra de foudre concentré.")
fix(S, "Comment s'appelle le sensei de Kakashi, Guy et les autres ?",
    q="Qui était le sensei de Kakashi, Obito et Rin ?")
drop(S, "Quel est l'arc narratif où Jiraiya affronte Pain ?")           # « L'Invasion de Konoha » est l'attaque d'Orochimaru
drop(S, "Quel clan est connu pour son Art des Marionnettes ?")          # Chiyo et Kankurō ne sont pas du clan Chikamatsu
drop(S, "Quel est le Six Voies (Rikudō) dans Naruto ?")                 # deux réponses désignent la même personne
drop(S, "Quel est le jutsu secret de l'Akimichi qui leur fait consommer leurs propres calories ?")
fix(S, "Quel est le nom du mode de Naruto qui utilise l'énergie naturelle ?",
    a=["Mode Kyûbi", "Mode Six Voies", "Mode Ermite", "Mode Bijû"], c=2,
    fb="Le Mode Ermite (Sennin Mode), appris au Mont Myoboku, permet d'utiliser l'énergie naturelle.")
drop(S, "Qui enseigne à Naruto le Mode Ermite ?")                       # Fukasaku et Pa Grenouille sont le même personnage
fix(S, "Quel clan Shino Aburame dirige-t-il ?", q="À quel clan appartient Shino ?")
drop(S, "Quel arc narratif introduit l'Akatsuki pour la première fois ?")
drop(S, "Quel bijū est scellé dans la femme de Pain (Konan) ?")
drop(S, "Quel est le vrai nom de l'Itachi adulte lors de sa mission secrète ?")
drop(S, "Quel est le nom du père d'Obito Uchiha (dans le backstory) ?")  # Obito n'a pas été élevé par Madara
fix(S, "Quelle est la particularité du chakra d'Hashirama Senju ?",
    fb="Hashirama maîtrise le Mokuton (Élément Bois), qui lui permet de créer et de contrôler les arbres, et même de maîtriser les Bijū.")
drop(S, "Quel est le nom de la Grand-Mère Chiyo ?")
drop(S, "Quel Sage légendaire enseigne à Jiraiya ?")                    # ce sont des crapauds, pas des grenouilles
drop(S, "Qui est le Jinchūriki du Gyūki (8 queues) avant Killer Bee ?")  # ce n'était pas le Raikage
drop(S, "Quel est le rôle de Sai dans le groupe 7 recomposé ?")          # deux réponses justes
fix(S, "Quel est le nom du genjutsu ultime placé sur toute l'humanité par Madara ?",
    a=["Izanagi", "Mugen Tsukuyomi", "Genjutsu mondial", "Kotoamatsukami"], c=1)
drop(S, "Quel est le pouvoir secret du Jōgan de Boruto ?")              # plusieurs réponses justes
fix(S, "Quel est l'ennemi ultime que Sasuke doit vaincre selon son arc personnel ?",
    q="Qui Sasuke veut-il tuer pendant toute la première partie de la série ?")
fix(S, "Quel bijū est associé à la Tortue à trois queues (Isobu) ?",
    q="Qui était le Jinchūriki d'Isobu, le bijū à trois queues ?")


# ---------------------------------------------------------------- One Piece
S = 'onepiece'
fix(S, "Quel est le nom de la récompense sur la tête d'un pirate ?",
    a=["Berry", "Prime", "Log Pose", "Poneglyphe"], c=1,
    fb="La prime est la récompense fixée par le Gouvernement mondial sur la tête d'un pirate, selon sa dangerosité. Le berry est la monnaie du monde de One Piece.")
fix(S, "Quel est le vrai nom de 'Barbe-Blanche' ?",
    fb="Edward Newgate, surnommé Barbe-Blanche, était l'un des Quatre Empereurs et passait pour l'homme le plus fort du monde.")
fix(S, "Qui est l'ancien capitaine de Shanks ?", a=["Roger", "Barbe-Blanche", "Rayleigh", "Kaido"], c=0)
fix(S, "Quel est le nom du pays des géants où vivent Dorry et Broggy ?",
    q="De quel pays des géants Dorry et Broggy sont-ils originaires ?",
    fb="Elbaf est l'île légendaire des guerriers géants, dont Usopp rêve depuis l'enfance. Dorry et Broggy, eux, se battent en duel depuis 100 ans sur Little Garden.")
fix(S, "Quel est le nom de l'archipel qui sépare la première et deuxième moitié du Grand Line ?",
    q="Sur quel archipel les équipages se préparent-ils avant de plonger vers le Nouveau Monde ?")
fix(S, "Quel est le nom de la ville dorée dans l'arc Alabasta ?", q="Quelle est la capitale du royaume d'Alabasta ?")
drop(S, "Quel est le nom de la ville au sommet de la falaise dans l'arc Alabasta ?")   # doublon
drop(S, "Quel est le nom de la route principale du Grand Line ?")                     # Reverse Mountain en est l'entrée
fix(S, "Quel est le nom du groupe des sept pirates travaillant pour le Gouvernement Mondial ?",
    a=["Quatre Empereurs", "Sept Grands Corsaires", "Onze Supernovas", "Cipher Pol"], c=1)
drop(S, "Quel est l'arc dans lequel Luffy accède au Nouveau Monde ?")                  # ambigu avec Punk Hazard
fix(S, "Quel est le nom de l'île où Luffy et ses amis grandissent ?",
    q="Dans quel village Luffy a-t-il grandi ?", a=["Foosha", "Loguetown", "Shells Town", "Cocoyashi"], c=0,
    fb="Le village de Foosha, sur l'île de l'Aube, est le village natal de Luffy. C'est là qu'il a rencontré Shanks.")
fix(S, "Quel est le fruit du démon de Kaido ?",
    fb="Kaido a mangé l'Uo Uo no Mi, modèle Seiryu, un Zoan mythique qui lui permet de se transformer en dragon azur.")
drop(S, "Quel est le prénom du père de Luffy, chef révolutionnaire ?")                 # doublon
drop(S, "Quel est le nom de l'état dormant du fruit Gum-Gum découvert plus tard ?")    # deux réponses justes
drop(S, "Quel est le nom de la technique d'éveil de Luffy (Gear 5) associée au Dieu du Soleil ?")
fix(S, "Comment s'appelle le pouvoir ultime de Luffy lié au 'Dieu du Soleil' ?",
    a=["Gear Five", "Gear Fourth", "Gear Third", "Haki des Rois"], c=0)
fix(S, "Quel est le nom de l'île natale de Zoro ?", q="Quel est le village natal de Zoro ?")
drop(S, "Quel est le nom de l'arc final de la saga Wano ?")                             # deux réponses quasi identiques
drop(S, "Quelle est la technique ultime de Zoro dans l'arc Wano ?")
fix(S, "Quel est le pouvoir du fruit de l'Amiral Akainu ?", a=["Magma", "Glace", "Lumière", "Gravité"], c=0,
    fb="Sakazuki (Akainu) possède le Magu Magu no Mi, un Logia de magma, plus destructeur encore que le feu d'Ace.")
drop(S, "Quel est le vrai nom du Chevalier de la Mer (Jinbe) ?")
fix(S, "Comment s'appelle la femme mystérieuse qui est la vice-présidente du Baroque Works à Alabasta ?",
    fb="Sous le nom de Miss All Sunday, Nico Robin était l'associée de Crocodile au sein de Baroque Works. Elle rejoint ensuite l'équipage comme archéologue.")
fix(S, "Quel est le vrai nom de 'Sniper King' (nom de guerre d'Usopp) ?",
    q="Sous quel nom Usopp se déguise-t-il pendant l'arc Enies Lobby ?")
fix(S, "Quel est le nom de l'île artificielle construite par les CP ?",
    q="Sur quelle île judiciaire les Chapeaux de paille viennent-ils sauver Robin ?")
drop(S, "Comment s'appelle la salle souterraine de César Clown où il gardait les enfants captifs dans l'arc Punk Hazard ?")
fix(S, "Quel est le nom du pays natal de Nami ?", q="Quel est le village natal de Nami ?")
drop(S, "Quel est le fruit du démon de Kaido's lieutenant Jack ?")                     # deux réponses justes
drop(S, "Quel est le vrai nom de l'Île des Hommes-Poissons ?")                         # contredit par l'explication
drop(S, "Quel est le nom de la technique à 3 couteaux de Zoro qui crée un dragon d'air ?")
fix(S, "Qui sont les Trois Grands Amiraux actuels des Marines (après l'ellipse) ?",
    q="Qui sont les trois Amiraux de la Marine après l'ellipse ?",
    a=["Akainu, Kizaru, Aokiji", "Sakazuki, Borsalino, Fujitora", "Kizaru, Fujitora, Ryokugyu", "Garp, Sengoku, Tsuru"], c=2,
    fb="Après l'ellipse, Akainu devient Amiral en chef. Les trois Amiraux sont alors Kizaru (Borsalino), Fujitora (Issho) et Ryokugyu (Aramaki).")
drop(S, "Quel est le nom de la 11e épée noire que Zoro obtient à Wano ?")
drop(S, "Quel est le nom du géant de la marine qui était l'ennemi de Luffy à Marineford ?")
drop(S, "Qui est Joyboy et pourquoi est-il important ?")
fix(S, "Quel est le vrai nom de la puissance (Haki) de l'armure en One Piece ?",
    a=["Busoshoku Haki", "Kenbunshoku Haki", "Haoshoku Haki", "Rokushiki"], c=0)
drop(S, "Comment s'appelle le régime tyrannique de Kaido à Wano ?")
drop(S, "Comment s'appelle le style de haki avancé permettant de voir le futur proche ?")
fix(S, "Quel est le surnom de Shanks le Roux dans le monde des pirates ?",
    q="Quel est le surnom de Shanks ?", a=["Le Roux", "Le Phénix", "Le Chirurgien de la mort", "Poing ardent"], c=0,
    fb="Shanks le Roux, l'un des Quatre Empereurs, doit son surnom à sa chevelure rouge.")
drop(S, "Quel est le nom de l'île volante où vivent les hommes au long nez comme Usopp ?")
fix(S, "Comment s'appelle la technique ultime de Gear Fourth de Luffy ?",
    q="Comment s'appelle la première forme du Gear Fourth de Luffy ?")
drop(S, "Quel est le nom de la prison sous-marine à 6 niveaux des grands criminels ?")  # doublon

drop(S, "Quel est le nom du chapitre final et arc ultime de One Piece (en cours) ?")
FIX[S]["Quel est le nom du groupe des sept pirates travaillant pour le Gouvernement Mondial ?"]['q'] = \
    "Comment appelle-t-on les pirates qui travaillent pour le Gouvernement mondial en échange de l'immunité ?"

S = 'naruto'
fix(S, "Quel est le clan de Sasuke Uchiha ?", q="À quel clan appartient Sasuke ?")
fix(S, "De quel clan est Hinata Hyûga ?", q="À quel clan appartient Hinata ?")
drop(S, "Combien de membres compte le groupe des Sept Ninjas de l'Épée de la Brume ?")   # réponse dans la question


# ---------------------------------------------------------------- Fairy Tail
S = 'fairytail'
fix(S, "Quel est le type de magie de Natsu Dragneel ?",
    fb="Natsu est un chasseur de dragons (Dragon Slayer) de feu, formé par le dragon Igneel.")
drop(S, "Quel est l'esprit céleste le plus puissant de Lucy ?")          # subjectif, explication fausse
fix(S, "Qui est le maître de la guilde Fairy Tail ?",
    fb="Makarov Dreyar a été le 3e, le 6e puis le 8e maître de Fairy Tail. Il fait aussi partie des Dix Mages Sacrés.")
fix(S, "Quel est le nom de la magie de Gray Fullbuster ?",
    a=["Magie du vent", "Magie de la terre", "Magie des runes", "Ice-Make"], c=3)
fix(S, "Qui est le père de Gray Fullbuster selon la série ?", q="Qui est le père de Gray ?")
fix(S, "Quel est le nom de la confrérie ennemie dans l'arc Tenrou ?",
    fb="Grimoire Heart, la guilde noire dirigée par Hadès (Precht), envahit l'île Tenrou pour s'emparer de Zeref.")
fix(S, "Quel est l'arc narratif final de Fairy Tail ?",
    fb="L'arc final oppose Fairy Tail à l'Empire d'Alvarez, dirigé par Zeref, avec Acnologia comme menace ultime.")
drop(S, "Quel est le vrai nom d'Auge (le dirigeant d'Alvarez) ?")         # l'empereur s'appelle Spriggan
fix(S, "Quel est le nom de la première maîtresse de Fairy Tail ?",
    fb="Mavis Vermillion est la fondatrice et première maîtresse de Fairy Tail, surnommée la Fée stratège.")
fix(S, "Quel est le nom de la Magie des Yeux du Paradis d'Ultear ?",
    q="Quelle magie Ultear utilise-t-elle ?", a=["Arc of Time", "Arc of Embodiment", "Heavenly Body Magic", "Ice-Make"], c=0)
fix(S, "Qui est le père biologique de Cana Alberona ?",
    fb="Gildarts Clive, le mage le plus puissant de Fairy Tail, est le père de Cana. Il ignorait qu'il avait une fille jusqu'à ce qu'elle le lui révèle.")
drop(S, "Quel est le nom des Grands Jeux Magiques de l'arc éponyme ?")    # réponse dans la question
drop(S, "Quel est le nom de la magie Heavenly Body de Jellal ?")          # réponse dans la question
fix(S, "Quel est le nom de la deuxième guilde ennemie dans l'arc Nirvana ?",
    q="Quelle guilde noire affronte-t-on dans l'arc Nirvana ?")
drop(S, "Quel est le nom de la guilde de crime de Macbeth (Brain) ?")     # doublon
fix(S, "Quel est la capacité unique de Mirajane Strauss ?",
    fb="Mirajane utilise le Take Over, et notamment Satan Soul, qui lui permet de prendre la forme et les pouvoirs de démons.")
fix(S, "Comment s'appelle la guilde indépendante fondée par Ultear et Meredy pour combattre les guildes noires ?",
    q="Comment s'appelle la guilde indépendante fondée par Jellal, Ultear et Meredy pour combattre les guildes noires ?",
    fb="Crime Sorcière est fondée par Jellal, Ultear et Meredy, d'anciens ennemis repentis qui pourchassent les guildes noires.")
drop(S, "Qui est surnommé le 'Requip' dans la série ?")                   # ce n'est pas un surnom
drop(S, "Quel est le vrai nom du personnage 'Mystogan' ?")               # Jellal s'appelle Gérard en VF : deux réponses justes
drop(S, "Quelle est la particularité de la magie d'Hades ?")
fix(S, "Quel est le nom du groupe de Laxus au sein de Fairy Tail ?",
    fb="La Thunder God Tribe (Raijinshū) réunit Freed, Bixlow et Evergreen, fidèles compagnons de Laxus.")
drop(S, "Quel est le nom de la montagne où vit l'ermite Warrod ?")
drop(S, "Quel est le nom du sort ultime de Erza : une armure de lumière pure ?")
drop(S, "Quel est le nom de la technique ultime d'Erza en armure de lumière pure ?")
drop(S, "Qui est le maître de Erza dans son passé à la Tour de la Célesté Mage ?")
drop(S, "Quel est la 8e étoile des Esprits Célestes de Lucy (parmi les Gold Keys) ?")
drop(S, "Quel est le nom du jeune garçon dragon dans l'arc final (fils de Natsu et Lucy dans le futur) ?")
drop(S, "Quel est la magie de Bickslow ?")
fix(S, "Qui est à la tête de la guilde Lamia Scale ?", a=["Sherry", "Lyon Vastia", "Ooba Babasaama", "Jura"], c=2,
    fb="Ooba Babasaama est la maîtresse de Lamia Scale. Lyon Vastia et Jura Neekis en sont deux des mages les plus connus.")
drop(S, "Quel est le nom de la Tour construite par Jellal ?")             # « Tour du Paradis » en VF
drop(S, "Quel personnage peut copier toute magie vue une seule fois dans Fairy Tail ?")   # doublon
drop(S, "Quel est le nom de la technique de Dragon Force de Natsu ?")
drop(S, "Quel est le nom de la technique finale de Natsu contre Zeref ?")
fix(S, "Quel est le nom de la fée attachée à Mavis dans sa jeunesse ?",
    fb="Zera est l'amie d'enfance de Mavis. On apprend plus tard qu'elle n'était qu'une illusion créée par Mavis elle-même.")
fix(S, "Quel est le nom du pays dans lequel règne Zeref en tant qu'Auge ?",
    q="Sur quel empire Zeref règne-t-il sous le nom de Spriggan ?",
    fb="L'Empire d'Alvarez, immense empire situé à l'ouest d'Ishgar, est gouverné par l'empereur Spriggan, qui n'est autre que Zeref.")
drop(S, "Quel est le sort qui rend le destinataire invincible pendant quelques secondes ?")
drop(S, "Qui est surnommé 'Lightning Strike Wizard' dans la série ?")
drop(S, "Quel est le nom du bébé-dragon adopté par la guilde à la fin de la série ?")
drop(S, "Quel est l'âge de Mavis Vermillion lorsqu'elle fonde Fairy Tail ?")
drop(S, "Quel est le sentiment d'Erza envers Jellal tout au long de la série ?")
drop(S, "Qui est surnommé 'Maître de Tous les Éléments' parmi les anciens Saints Magiciens ?")
drop(S, "Quel est le nom de la technique d'Irène Belserion qui invoque des astéroïdes ?")
drop(S, "Quel est le véritable pouvoir d'Irène au-delà de ses enchantements spatiaux ?")
drop(S, "Comment se nomme la technique de Mavis permettant de calculer les probabilités de combat ?")
drop(S, "Quelle technique d'August est capable d'annuler toute forme de magie en zone ?")
drop(S, "Comment s'appelle la technique d'Archive de Jacob Lessio ?")


# ---------------------------------------------------------------- Hunter × Hunter
S = 'hxh'
fix(S, "Quel est le type de Nen de Killua ?", a=["Améliorateur", "Émetteur", "Manipulateur", "Transmutateur"], c=3)
fix(S, "Quel est le nom de l'antagoniste principal de l'arc Chimère Ant ?", a=["Illumi", "Meruem", "Neferpitou", "Phinks"], c=1)
drop(S, "Quelle est la technique de Nen ultime de Gon (activant son potentiel total) ?")   # deux réponses identiques
drop(S, "Quel est le nom de la technique de Gon qui sacrifie tout son potentiel futur ?")
drop(S, "Quel est le nom de la résidence des Zoldyck ?")                                   # doublon de Kukuroo
fix(S, "Quel est le nom du groupe de criminels de l'arc York Shin ?",
    a=["Les Zodiaques", "Genei Ryodan", "Shadow Group", "Phantom Squad"], c=1,
    fb="La Genei Ryodan, ou Brigade Fantôme, est un groupe de 13 criminels d'élite dirigé par Chrollo Lucilfer.")
drop(S, "Quel est le type de Nen de Kurapika ?")              # Matérialiseur de nature : deux réponses justes, explication fausse
fix(S, "Quel est le nom de la capacité Nen de Chrollo Lucilfer ?",
    a=["Skill Hunter", "Black Voice", "Skill Collector", "Fortune Stealer"], c=0,
    fb="Skill Hunter permet à Chrollo de voler les capacités Nen d'autres personnes et de les utiliser grâce à son livre.")
drop(S, "Quel est la restriction que Kurapika impose sur ses chaînes contre la Brigade ?")  # « les deux premières » est aussi juste
fix(S, "Comment s'appelle l'arc qui se passe sur un navire vers le Continent Obscur ?",
    fb="L'arc de la Guerre de Succession, toujours en cours, se déroule à bord du Black Whale, le navire qui part vers le Continent Obscur.")
fix(S, "Quel est le nom du continent mystérieux de l'arc final ?", a=["Greed Island", "Continent Obscur", "Terre de Beyond", "Terra Incognita"], c=1)
drop(S, "Quel est le nom de l'épreuve finale de l'examen Hunter (Phase 5) ?")
drop(S, "Quel est le nom du jeu vidéo que Gon et Killua jouent physiquement ?")           # doublon
drop(S, "Quel est le nom de l'arc final publié dans le manga (chapitres 400+) ?")          # doublon
drop(S, "Quelle technique assassine Killua doit-il maîtriser pour tuer sans hésitation ?")
drop(S, "Quel est le nom de la garde royale N°1 des Fourmis Chimères, la plus puissante avant Meruem ?")  # Pitou est Spécialiste
drop(S, "Quel est le type Nen de Neferpitou (Pitou) ?")
drop(S, "Comment s'appelle la mécanique des serments qui renforcent le Nen ?")             # doublon, deux réponses justes
fix(S, "Quel est le nom de la technique ultime de Netero contre Meruem ?",
    fb="Le Zero Hand est l'attaque ultime de Netero : il y concentre toute son aura en un seul coup contre Meruem.")
fix(S, "Quel est le nom de la bombe Netero déclenche sur lui-même pour tuer Meruem ?",
    q="Quelle bombe Netero déclenche-t-il sur lui-même pour vaincre Meruem ?",
    fb="La Poor Man's Rose est une bombe miniature cachée dans le corps de Netero. Son explosion répand un poison qui finira par tuer Meruem.")
drop(S, "Quelle est la technique de téléportation de Feitan ?")
fix(S, "Quel est le nom de la ville de l'arc York Shin ?", a=["Yorknew City", "Dolle Harbor", "Manhattan du HxH", "Shadow City"], c=0)
drop(S, "Comment s'appelle la ville de l'arc York Shin ?")                                  # doublon
fix(S, "Quel est le style Nen de Illumi Zoldyck ?",
    fb="Illumi est un Manipulateur : il plante des aiguilles dans ses cibles pour les contrôler comme des marionnettes.")
drop(S, "Dans quel arc Gon et Killua se rendent-ils à l'arène Heaven's Arena ?")          # réponse dans la question
drop(S, "Quel est la capacité de Bungee Gum d'Hisoka en combinaison avec Texture Surprise ?")
drop(S, "Quel est le rang maximum de Hunter dans la série ?")                               # doublon
drop(S, "Quel est le nom de la technique de combat de Wing enseigne à Gon ?")              # doublon de Ten
drop(S, "Qui est surnommé 'The Crazy Slot Machine' dans la Brigade Fantôme ?")
drop(S, "Quel est le rang de chasseur obtenu par Gon à la fin de l'examen ?")
drop(S, "Quel est le type Nen de Biscuit Krueger ?")                                         # Biscuit est Transmutatrice
drop(S, "Comment s'appelle la technique d'entraînement accéléré de Biscuit ?")
drop(S, "Quel est le type Nen de Meruem ?")
drop(S, "Quel est le type Nen de Palm Siberia ?")
drop(S, "Quel est l'objectif des Zodiacs dans l'Association des Hunters ?")
drop(S, "Quel est le type Nen de Morel ?")
fix(S, "Qui est le père de Killua ?", fb="Silva Zoldyck est le père de Killua et le chef actuel de la famille d'assassins.")
drop(S, "Quel est le type Nen de Gon au niveau de base ?")                                  # doublon
drop(S, "Quel est le prénom de la mère de Gon dans le canon officiel ?")
drop(S, "Quel est le nom exact du Royaume maritime de l'arc final ?")


# ---------------------------------------------------------------- Death Note
S = 'deathnote'
fix(S, "Comment s'appelle le carnet magique de l'histoire ?", a=["Death Book", "Kira Note", "Death Note", "Killing Notebook"], c=2)
drop(S, "Quel est le nom de l'organisation de Kira au Japon ?")            # c'est la cellule anti-Kira ; réponses ambiguës
fix(S, "Quel est le nom de l'organisation de Near contre Kira ?",
    fb="Le SPK (Special Provision for Kira) est une unité créée aux États-Unis pour traquer Kira, dirigée par Near.")
drop(S, "Quel est le nom de la chaîne TV que Light utilise pour communiquer ?")   # deux réponses identiques
drop(S, "Quel est le nom du patron de Light au journal télévisé ?")
drop(S, "Qui est le 3e candidat à la succession de L (ami de Mello) ?")           # doublon
drop(S, "Quel est le délai maximum pour écrire les détails après la cause de mort ?")      # doublon
drop(S, "Quelle est la durée maximale pour préciser les circonstances d'une mort après la cause ?")
drop(S, "Quel est le nom de la journaliste que Light utilise comme porte-parole de Kira ?")  # doublon
fix(S, "Quel personnage meurt en protégeant Light avec son propre Death Note ?",
    q="Quel Shinigami écrit les noms de L et de Watari pour protéger Misa ?",
    fb="Rem tient à Misa : elle écrit les noms de L et de Watari dans son Death Note pour la protéger, ce qui la condamne à disparaître.")
fix(S, "Que se passe-t-il quand un Shinigami tue quelqu'un qui n'était pas destiné à mourir ?",
    q="Que se passe-t-il quand un Shinigami tue quelqu'un pour prolonger la vie d'un humain ?")
drop(S, "Quelle est la règle sur la durée de vie d'un Shinigami qui s'attache à un humain ?")  # réponse fausse
drop(S, "Quelle est la règle sur la durée de vie d'un Shinigami qui allonge la vie d'un humain ?")  # doublon
drop(S, "Quel est le nom que prend Kira pour se faire connaître au Japon ?")       # réponse dans la question
drop(S, "Quel est le nombre exact de secondes pour qu'une mort par crise cardiaque se produise ?")  # doublon
drop(S, "Quel est le destin de Ryuk à la fin de la série ?")                       # doublon
drop(S, "Quel est le nom du détective B, prédécesseur de L ?")
drop(S, "Quel est le nom de la technique de Light pour cacher ses notes ?")        # nom inventé
fix(S, "Quel est le nom de l'assistant de L (vieillard) ?", a=["Watari", "Roger", "Aizawa", "James"], c=0)
drop(S, "Quel aliment L consomme-t-il excessivement dans la série ?")              # réponses qui se recoupent
drop(S, "Quel est l'aliment que L consomme compulsivement tout au long de la série ?")
drop(S, "Quel est le pourcentage de certitude qu'a L sur la culpabilité de Light ?")
drop(S, "Quel est le pourcentage de certitude de L concernant la culpabilité de Light ?")
drop(S, "Comment s'appelle le deuxième Kira qui apparaît avec un second Death Note ?")   # doublon
drop(S, "Combien de Death Notes peuvent exister simultanément dans le monde humain ?")  # doublon
drop(S, "Quel est le nom de la fondation caritative de L servant de façade ?")
drop(S, "Quelle est la règle de possession du Death Note ?")
fix(S, "Quel est le nom complet du personnage Mikami ?",
    fb="Teru Mikami est un procureur fanatique de Kira, choisi par Light pour agir à sa place pendant la traque finale.")
drop(S, "Que signifie écrire 'humain' dans un Death Note ?")
drop(S, "Quel est le titre alternatif japonais de Death Note ?")                  # c'est « Desu Nōto »
drop(S, "Quel est le nom de l'arc final de Death Note ?")
drop(S, "Quelle est la couleur des yeux de Ryuk ?")
drop(S, "Quelle règle interdit à un Shinigami de tuer pour un humain ?")
drop(S, "Quel est le geste caractéristique de L quand il s'assoit ?")             # doublon, réponse dans la question
drop(S, "Comment Light convainc Misa de ne plus utiliser ses Yeux de Shinigami pendant l'enquête ?")
fix(S, "Comment Light Yagami se perçoit-il dans le monde qu'il crée ?",
    q="Quel titre Light veut-il obtenir grâce au Death Note ?")
drop(S, "Combien de tomes compte le manga Death Note ?")                          # explication contradictoire
drop(S, "Quelle règle empêche d'écrire uniquement un prénom courant ?")
fix(S, "Quel est le nom de la technique Near utilise pour piéger Mikami et Light ?",
    q="Comment Near piège-t-il Light et Mikami lors de la confrontation finale ?",
    a=["Il remplace le carnet de Mikami par une fausse copie", "Il fait arrêter Misa", "Il écrit lui-même dans un Death Note", "Il obtient les Yeux de Shinigami"], c=0,
    fb="Near fait remplacer le Death Note de Mikami par une copie. Quand Mikami y écrit les noms, personne ne meurt, et le nom de Light absent de la liste le désigne comme Kira.")
fix(S, "Comment Mello obtient-il son Death Note au début de l'arc final ?",
    fb="Mello fait enlever Sayu Yagami pour obliger la cellule d'enquête japonaise à lui remettre le Death Note.")
drop(S, "Quel est le raisonnement de L pour identifier la zone géographique de Kira ?")  # c'est le test télévisé de Lind L. Tailor
drop(S, "Quelle est la signification du prénom 'Kira' en japonais et sa référence anglaise ?")  # explication contradictoire
drop(S, "Qui est le vrai chef derrière la mission d'enquête de L depuis l'ombre ?")


# ---------------------------------------------------------------- Inazuma Eleven
# Banque très peu fiable (personnages confondus, techniques inventées) : seules 23 questions sûres sont gardées.
S = 'inazuma'
drop(S, "Quelle est la technique combinée utilisée par l'équipe de Raimon face à Zeus ?")
drop(S, 'Quel est le nom du club de football de Raimon au départ ?')
drop(S, "Quel est le nom de la super équipe ennemi formée par 'Fifth Sector' ?")
drop(S, "Quel est le nom de la technique de tir d'Axel évoluée avec Dragon Drive ?")
drop(S, "Quel objet mystérieux les joueurs d'Aliea Gakuen utilisent-ils ?")
drop(S, "Quel est le nom de l'équipe finale à vaincre dans Inazuma Eleven 2 ?")
drop(S, 'Quel est le nom de la technique de Jude Sharp ?')
drop(S, "Qui est l'entraîneur d'Inazuma Japan dans la saison 3 ?")
drop(S, 'Quel est le nom de la technique de gardien de Nathan Swift ?')
drop(S, 'Quel est le nom de la technique combinée Fire Tornado avec Who Does ?')
drop(S, "Quel est le nom de l'équipe finale à battre dans la FFI ?")
drop(S, 'Quel est le nom de la technique défensive de Xavier Foster ?')
drop(S, 'Quel est le prénom complet du personnage Shawn Froste ?')
drop(S, 'Dans Inazuma Eleven GO, qui est le nouveau protagoniste principal ?')
drop(S, 'Quel est le nom du nouveau club dans Inazuma Eleven GO ?')
drop(S, 'Quel est le nom de la technique ultime de Mark dans la finale de la saison 2 ?')
drop(S, 'Quel est le nom du grand-père de Mark Evans ?')
drop(S, "Quelle est la technique spéciale des 'Fifth Sector' pour contrôler les matchs ?")
drop(S, 'Quel est le nom de la technique défensive qui crée un mur de glace ?')
drop(S, 'Quel est le nom de la technique combinée des 3 frères dans GO Chrono Stone ?')
drop(S, 'Quelle civilisation ancienne est visitée dans GO Chrono Stone ?')
drop(S, 'Quel est le nom de la technique ultime de Tsurugi Kyousuke (Shawn Froste) ?')
drop(S, 'Quel est le nom de la technique de gardien de Kageyama dans la saison 3 ?')
drop(S, "Combien d'équipes extraterrestres affronte Raimon pendant Aliea Gakuen ?")
drop(S, "Quel est le surnom de l'équipe alien la plus puissante (saison 2) ?")
drop(S, 'Quel est le nom de la technique de tir de la version future de Mark Evans ?')
drop(S, 'Qui invente le système Keshin dans Inazuma Eleven GO ?')
drop(S, 'Quel est le nom du stade principal de Raimon ?')
drop(S, "Comment s'appelle la technique de tir tourbillonnant enflammé emblématique de Gouenji dans Inazuma Eleven ?")
drop(S, 'Quel est le nom de la technique défensive de Defenders incluant un mur de pierre ?')
drop(S, 'Quel est le surnom de Xavier Foster dans la série française ?')
drop(S, 'Quelle est la rivalité emblématique de la série Inazuma en termes de techniques ?')
drop(S, 'Quelle est la capacité unique de la technique God Catch ?')
drop(S, "Quel est le nom de l'adversaire principal du dernier arc (Galaxy) ?")
drop(S, "Quel est le nom complet de l'organisation antagoniste principale dans la saison 3 ?")
drop(S, 'Quel est le nombre de buts nécessaires pour gagner dans Inazuma Eleven en général ?')
drop(S, 'Quel est le nom de la technique de tir combinée de Mark Evans et Axel Blaze ?')
drop(S, 'Comment les super techniques se déclenchent-elles visuellement dans la série animée ?')
drop(S, 'Quel est le nom de la technique ultime combinant 3 éléments dans GO ?')
drop(S, "Comment s'appelle l'attaque signature acrobatique de Tsurugi Kyousuke ?")
drop(S, "Comment s'appelle le personnage légendaire qui inspire Arion Sherwind ?")
drop(S, "Comment s'appelle la technique signature de Hiroto Kiyama évoquant un phénix ?")
drop(S, "Quel personnage historique est utilisé pour le Mixi Max lors de l'arc en Grèce antique ?")
drop(S, 'Quel est le nom de la ligue internationale de football scolaire du jeu ?')
drop(S, "Comment s'appelle l'organisation criminelle qui contrôle le football dans GO ?")
drop(S, "Quel personnage est surnommé 'The Phantom Goal' pour ses techniques invisibles ?")
drop(S, "Comment s'appelle la technique de défense ultime contre les tirs multi-joueurs ?")
drop(S, 'Quel est le sport que pratique Sangoku en dehors du football ?')
drop(S, "Comment s'appelle la technique combinée de Kidou et Gouenji ?")
drop(S, 'Quel est le nom de la technique de gardien de Mark Evans en version ultime GO ?')
drop(S, 'Qui invente le système Keshin dans Inazuma GO ?')
drop(S, "Comment s'appelle le coach légendaire d'Inazuma Japan dans la saison 3 ?")
drop(S, "Quel est le cri de victoire emblématique de l'équipe Raimon ?")
drop(S, "Comment s'appelle l'équipe qui contrôle les matchs par manipulation mentale dans GO ?")
drop(S, 'Quel est le sport national japonais que Sangoku imite dans son style de gardien ?')
fix(S, "Quel est le nom de la première technique de tir que Mark voit dans son journal du grand-père ?",
    q="Quelle technique de gardien Mark découvre-t-il dans les carnets de son grand-père ?")
fix(S, "Comment s'appelle le gardien de Raimon GO qui remplace Mark Evans ?",
    fb="Sangoku Taichi est le gardien de but de Raimon au début d'Inazuma Eleven GO.")
fix(S, "Quel est le nom de l'équipe voyageant dans le temps dans GO Chrono Stone ?",
    q="Comment s'appelle l'équipe qui voyage dans le temps pour sauver le football ?")


# ---------------------------------------------------------------- Harry Potter
S = 'harrypotter'
fix(S, "Quel est le nom du fantôme de Gryffondor ?", a=["Le Baron Sanglant", "Le Moine Gras", "Nick Quasi-Sans-Tête", "La Dame Grise"], c=2,
    fb="Nick Quasi-Sans-Tête est le fantôme de Gryffondor : sa tête ne tient plus que par un mince lambeau de peau.")
fix(S, "Comment s'appelle le chat d'Hermione Granger ?", a=["Croûtard", "Hedwige", "Pattenrond", "Miss Teigne"], c=2,
    fb="Pattenrond est le chat d'Hermione. Croûtard est le rat de Ron, Hedwige la chouette de Harry et Miss Teigne la chatte de Rusard.")
fix(S, "Quel est le nom du grand tournoi de sorcellerie dans le Tome 4 ?",
    fb="Le Tournoi des Trois Sorciers oppose un champion de Poudlard, de Beauxbâtons et de Durmstrang, désignés par la Coupe de Feu.")
fix(S, "Quel est le vrai nom de 'Voldemort' à la naissance ?",
    q="Quel est le nom complet de Voldemort à la naissance, dans la version française ?",
    a=["Marvolo Gaunt", "Tom Marvolo Gaunt", "Tom Riddle Jedusor", "Tom Elvis Jedusor"], c=3)
fix(S, "Quelle est l'anagramme de Tom Elvis Jedusor ?",
    a=["Je suis Voldemort", "Ie suis lord mort", "Moi, l'être nuisible", "Lord Mort-vivant"], c=0,
    fb="Dans la version française, Tom Elvis Jedusor est l'anagramme de « Je suis Voldemort ». En anglais, Tom Marvolo Riddle donne « I am Lord Voldemort ».")
fix(S, "Quel est le nom du sort permettant d'appeler le bâton magique ?",
    q="Quel sort permet d'attirer un objet vers soi ?", a=["Accio", "Expecto", "Alohomora", "Impedimenta"], c=0)
fix(S, "Quel est le nom de la mascotte de Durmstrang dans le Tournoi ?",
    q="Qui est le champion de Durmstrang au Tournoi des Trois Sorciers ?",
    fb="Viktor Krum, attrapeur de l'équipe nationale de Bulgarie, représente Durmstrang. Hermione l'accompagne au bal de Noël.")
fix(S, "Quelle est la forme du Patronus de Hermione ?", fb="Le Patronus d'Hermione prend la forme d'une loutre.")
drop(S, "Quel est le nom du journal de Tom Jedusor utilisé comme Horcruxe ?")      # réponse dans la question
fix(S, "Quel est le nom du Professeur de Potions dans les tomes 1 à 6 ?", q="Qui enseigne les potions à Harry de la 1re à la 5e année ?",
    fb="Severus Rogue enseigne les potions jusqu'à la 5e année. En 6e année, Horace Slughorn le remplace et Rogue obtient la Défense contre les forces du Mal.")
drop(S, "Quelle est la devise de Gryffondor ?")                                    # les maisons n'ont pas de devise officielle
fix(S, "Quel est le nom du principal gardien de l'École Poudlard ?",
    q="Comment s'appelle le concierge de Poudlard ?", a=["Hagrid", "Dumbledore", "Rusard", "Peeves"], c=2,
    fb="Argus Rusard est le concierge grincheux de Poudlard, toujours accompagné de sa chatte, Miss Teigne. Hagrid, lui, est le garde-chasse.")
fix(S, "Qui était le précédent propriétaire de la baguette de sureau ?",
    q="Selon le conte des trois frères, qui fut le premier propriétaire de la Baguette de Sureau ?",
    fb="Dans le conte, Antioche Peverell, l'aîné des trois frères, reçoit de la Mort la Baguette de Sureau.")
drop(S, "Quel est le nom de la cape d'invisibilité de Harry ?")                    # réponse dans la question
drop(S, "Qui est la voleuse dans Harry Potter qui vole le Médaillon ?")             # Ombrage et Umbridge : même personne
fix(S, "Quel est le sort de soins qui répare les objets brisés ?", q="Quel sort répare les objets brisés ?")
drop(S, "Quel est le nom du sort que Harry utilise pour produire sa première expulsion de Détraqueurs ?")  # doublon
drop(S, "Quel est le nom du Choixpeau Magique ?")
drop(S, "Quel est le surnom des parents de Harry dans l'Ordre du Phénix ?")
drop(S, "Quel est le nom de la carte magique révélant toutes les personnes à Poudlard ?")  # doublon
drop(S, "Quel est le nom de la manœuvre de Harry lors du Tournoi des Trois Sorciers avec le dragon ?")
drop(S, "Quel est le nom du portrait de Dumbledore dans la saga ?")
fix(S, "Quel est le nom du traître dans la Chambre des Secrets ?",
    q="Qui est réellement responsable de l'ouverture de la Chambre des Secrets dans le tome 2 ?")
fix(S, "Quel est le nom de la huitième Horcruxe involontaire de Voldemort ?",
    q="Qui est devenu un Horcruxe sans que Voldemort le veuille ?")
drop(S, "Comment Harry détruit-il finalement chaque Horcruxe ?")
fix(S, "Quel est le nom du Phénix de Dumbledore ?", a=["Fumseck", "Buck", "Errol", "Norbert"], c=0,
    fb="Fumseck (Fawkes en version originale) est le phénix de Dumbledore. Ses larmes guérissent et il renaît de ses cendres.")
drop(S, "Quel est le nom de l'ennemi de Hagrid qui veut le renvoyer de Poudlard ?")  # Ombrage aussi
fix(S, "Quel est le bois de la baguette de Voldemort ?",
    fb="La baguette de Voldemort est en bois d'if, avec une plume de Fumseck, sœur de celle qui se trouve dans la baguette de Harry.")
drop(S, "Quel sort Hermione utilise-t-elle pour allumer le feu sous la robe de Rogue lors du premier match de Quidditch ?")
fix(S, "Quelle est la composition de la baguette de Harry Potter ?",
    fb="La baguette de Harry est en bois de houx, avec une plume de Fumseck, le phénix qui a aussi donné la plume de la baguette de Voldemort.")
fix(S, "Quel est le prénom du père de Harry ?",
    fb="James Potter est le père de Harry. Membre des Maraudeurs, il était un Animagus capable de se changer en cerf.")
fix(S, "Qui dit la fameuse réplique 'Ce n'est pas la baguette qui fait le sorcier' ?",
    q="Qui affirme que « c'est la baguette qui choisit le sorcier » ?", a=["Dumbledore", "Ollivander", "Harry", "Hermione"], c=1)
fix(S, "Quel est le nom du professeur de Divination ?", a=["Sibylle Trelawney", "Madame Pomfresh", "Pomona Chourave", "Dolores Ombrage"], c=0,
    fb="Sibylle Trelawney enseigne la divination à Poudlard. Malgré ses airs théâtraux, elle a fait deux vraies prophéties.")
fix(S, "Comment s'appelle la librairie d'articles de magie noire dans l'allée de Nogturd ?",
    q="Comment s'appelle la boutique d'objets de magie noire de l'allée des Embrumes ?",
    a=["Fleury et Bott", "Barjow et Beurk", "Ollivander", "Weasley, Farces pour sorciers facétieux"], c=1,
    fb="Barjow et Beurk (Borgin and Burkes en version originale) vend des objets de magie noire. Drago y fait réparer une armoire à disparaître dans le tome 6.")
fix(S, "Quel est le nom de l'organisation créée par Hermione pour défendre les droits des Elfes ?",
    a=["Le F.L.E.", "La S.A.L.E.", "Les Elfes Libres", "L'A.D."], c=1,
    fb="Hermione fonde la S.A.L.E. (Société d'aide à la libération des elfes) dans le tome 4. Ses amis s'en moquent, mais elle n'abandonne pas.")


# ---------------------------------------------------------------- Le Seigneur des Anneaux
S = 'lotr'
fix(S, "Quel est le nom du Hobbit qui possède l'Anneau au début du Seigneur des Anneaux ?",
    fb="Bilbon Sacquet trouve l'Anneau dans les cavernes de Gollum, le garde soixante ans, puis le lègue à Frodon.")
fix(S, "Quelle est la devise gravée sur l'Anneau Unique (en Noir Langage) ?",
    q="Quels sont les premiers mots de l'inscription gravée sur l'Anneau unique, en Noir Parler ?",
    a=["Mellon", "Ash nazg durbatulûk", "Elen síla lúmenn' omentielvo", "Baruk Khazâd"], c=1,
    fb="« Ash nazg durbatulûk » ouvre l'inscription de l'Anneau, en Noir Parler : « Un Anneau pour les gouverner tous ».")
drop(S, "Quel est le nom du magicien blanc de la Communauté de l'Anneau ?")         # question contradictoire
fix(S, "Quel est le nom du chef des Nazgûl ?", a=["Le Roi-Sorcier d'Angmar", "Le Capitaine noir de Mordor", "Saroumane", "Le Seigneur des Ombres"], c=0,
    fb="Le Roi-Sorcier d'Angmar est le chef des Nazgûl. Il est tué par Éowyn, avec l'aide de Merry.")
fix(S, "Quel est le nom de la forêt dorée des Elfes près de la Lorien ?",
    q="Comment s'appelle la forêt des Elfes gouvernée par Galadriel et Celeborn ?")
fix(S, "Quel est l'autre nom d'Aragorn (son titre de Ranger) ?",
    q="Quel surnom les gens de Bree donnent-ils à Aragorn ?", a=["Grands-Pas", "Elessar", "Estel", "Thorongil"], c=0,
    fb="À Bree, Aragorn est connu comme Grands-Pas, un Rôdeur du Nord. Estel est son nom d'enfance, Elessar son nom de roi.")
fix(S, "Quel est le nom du Balrog que Gandalf combat à Moria ?",
    a=["L'Horreur sans nom", "Le Fléau de Durin", "La Flamme d'Udûn", "L'Ombre de la Moria"], c=1,
    fb="Le Balrog de la Moria est appelé le Fléau de Durin : il a tué le roi nain Durin VI.")
drop(S, "Quel est le nom du peuple des Ents dans Le Seigneur des Anneaux ?")         # réponse dans la question
drop(S, "Quel est le nom du Roi des Morts qui aide Aragorn ?")                      # réponse dans la question
fix(S, "Quel est le nom complet de la forteresse de Sauron en Mordor ?", a=["Barad-dûr", "Orthanc", "Minas Sauron", "L'Œil Noir"], c=0)
drop(S, "Quel est le nom de la forteresse principale de Sauron en Mordor ?")        # doublon
fix(S, "Quel est le nom de la forteresse défensive du Rohan dans Les Deux Tours ?",
    a=["Le Gouffre de Helm", "Edoras", "Minas Ithil", "Osgiliath"], c=0,
    fb="Le Gouffre de Helm, et sa forteresse de Fort-le-Cor, est le refuge du Rohan où se déroule la grande bataille des Deux Tours.")
fix(S, "Qui est surnommé 'Langue de Serpent' ?", a=["Gríma", "Saroumane", "Théodred", "Denethor"], c=0)
drop(S, "Quel est le nom de l'espion à poil de Saroumane qui surveille le Rohan ?")  # doublon
fix(S, "Quel est le nom de l'épée d'Isildur avant qu'elle ne soit fondue ?",
    q="Quelle épée a tranché le doigt de Sauron ?",
    fb="Narsil, l'épée d'Elendil, se brise pendant la bataille. Isildur s'en sert pour trancher le doigt de Sauron. Reforgée, elle deviendra Andúril.")
fix(S, "Comment s'appelle le poignard de Frodon ?", a=["Glamdring", "Dard", "Orcrist", "Andúril"], c=1)
drop(S, "Quel est le nom de la cité des Morts en Gondor ?")                          # Minas Ithil et Minas Morgul sont la même cité
fix(S, "Quel est le nom de l'araignée géante dans les Monts Ephel Dúath ?",
    a=["Ungoliant", "Arachne", "Smaug", "Glaurung"], c=1,
    fb="Arachne (Shelob en version originale) habite les tunnels de Cirith Ungol. Elle pique Frodon, mais Sam la blesse avec Dard.")
drop(S, "Comment s'appelle l'araignée géante qui piège Frodon à Cirith Ungol ?")     # doublon
drop(S, "Quel est le nom de la prophétie sur le Roi Sorcier ?")                      # doublon
fix(S, "Quel est le nom du père de Frodon ?",
    fb="Drogo Sacquet est le père de Frodon. Il s'est noyé dans le Brandevin avec sa femme Primula.")
drop(S, "Quel est le nom de la Comté en anglais (langue de Tolkien) ?")
fix(S, "Quel est le nom de la maison de Bilbon et Frodon dans La Comté ?", a=["Grands Smials", "Cul-de-Sac", "Les Galgals", "Château-Brande"], c=1,
    fb="Cul-de-Sac (Bag End en version originale) est le trou de hobbit de Bilbon puis de Frodon, à Hobbitebourg.")
drop(S, "Quel est le nom du dernier camp des Hobbits avant la Forêt Noire en voyage ?")
drop(S, "Quel est le titre que prend Aragorn après la guerre de l'Anneau ?")          # doublon
drop(S, "Quel est le nom des Aigles qui sauvent Frodon et Sam à la fin ?")             # deux réponses justes
drop(S, "Quel est le nom du peuple aquatique qui aide les Hobbits à rejoindre Fondcombe ?")
fix(S, "Quelle est la forteresse noire de Saroumane, au cœur de la vallée d'Isengard ?", a=["Barad-dûr", "Dol Guldur", "Orthanc", "Minas Morgul"], c=2)
fix(S, "Quel est le nom du père de Samwise Gamegie ?", q="Comment s'appelle le père de Sam ?",
    fb="Hamfast Gamegie, surnommé l'Ancien, est le père de Sam et le jardinier de Cul-de-Sac avant lui.")
drop(S, "Qui forged les Anneaux de Pouvoir en étant trompé par Sauron ?")             # doublon
fix(S, "Quel est le nom du port des Elfes depuis lequel ils quittent la Terre du Milieu ?",
    a=["Les Havres Gris", "Dol Amroth", "Pelargir", "Osgiliath"], c=0)
drop(S, "Comment s'appelle la ville portuaire elfique depuis laquelle les Elfes quittent la Terre du Milieu ?")  # doublon
fix(S, "Quel est le pays/région d'origine de Legolas ?", a=["La Comté", "Lothlórien", "Forêt Noire (Mirkwood)", "Fondcombe"], c=2)
fix(S, "Quel nom Sauron se donnait-il pour tromper les Elfes forgerons ?", a=["Thû", "Annatar, le Seigneur des Dons", "Gorthaur", "Le Nécromancien"], c=1)
drop(S, "Comment s'appelle la grande montagne volcanique où l'Anneau doit être détruit ?")  # doublon
fix(S, "Qui sont les deux batailles finales de la Troisième Ère ?",
    q="Quelles sont les deux dernières grandes batailles de la guerre de l'Anneau ?")


# ---------------------------------------------------------------- Star Wars
S = 'starwars'
fix(S, "Quel est le nom de la directive secrète qui ordonne aux soldats clones de tuer leurs généraux Jedi ?",
    fb="L'Ordre 66 est une directive secrète de Palpatine qui commande aux soldats clones d'éliminer tous les Jedi.")
fix(S, "Quel est le nom de l'arme signature des Jedi et Sith ?", a=["Vibrolame", "Sabre laser", "Épée photonique", "Blaster"], c=1)
fix(S, "Quel est le nom de la station de combat de l'Empire ?",
    a=["L'Étoile de la Mort", "Le Super Destroyer", "La Forteresse stellaire", "L'Executor"], c=0,
    fb="L'Étoile de la Mort (Death Star) est une station spatiale armée d'un super-laser capable de détruire une planète entière.")
fix(S, "Quelle est la règle Sith sur le nombre de maîtres et apprentis ?",
    q="Combien de Sith peuvent exister à la fois selon la doctrine de Dark Bane ?",
    a=["Un seul", "Deux : un maître et un apprenti", "Trois", "Autant que nécessaire"], c=1,
    fb="La Règle des Deux, instaurée par Dark Bane, n'autorise qu'un maître Sith et un apprenti à la fois.")
drop(S, "Quel est le nom de la technique de communication holographique dans Star Wars ?")
fix(S, "Quel est le nom du détroit entre la technologie galactique et la Force ?",
    q="Comment s'appellent les micro-organismes qui relient les êtres vivants à la Force ?")
fix(S, "Quel est le nom de la garde rouge de l'Empereur ?",
    a=["Les Stormtroopers", "Les Gardes royaux impériaux", "Les Inquisiteurs", "L'Escadron Rouge"], c=1,
    fb="Les Gardes royaux impériaux, en robes rouges, forment la garde d'élite de l'Empereur Palpatine.")
drop(S, "Quel est le nom de l'armée des clones dans les préquelles ?")              # réponses qui se recoupent
fix(S, "Quel est le nom de la planète de la forêt des Ewoks ?", q="Sur quelle lune forestière vivent les Ewoks ?")
fix(S, "Quel est le nom de la résistance qui combat l'Empire ?",
    a=["L'Alliance rebelle", "Le Premier Ordre", "L'Alliance de la Liberté", "La Confédération"], c=0)
drop(S, "Quel est le nom du Conseil Jedi au sommet de leur temple ?")               # réponse dans la question
fix(S, "Quel est le nom du général Jedi dont Boba Fett est le clone ?",
    q="Sur quel chasseur de primes l'armée des clones a-t-elle été modelée ?",
    a=["Jango Fett", "Din Djarin", "Cad Bane", "Bossk"], c=0,
    fb="Jango Fett, chasseur de primes mandalorien, sert de modèle génétique à toute l'armée des clones. Boba est son clone non modifié, qu'il élève comme son fils.")
drop(S, "Quel est le nom de la planète capitale de la galaxie dans Star Wars ?")    # doublon
fix(S, "Quel est le nom du général andalorien de l'armée de la Confédération ?",
    q="Quel cyborg commande l'armée droïde des Séparatistes ?")
fix(S, "Quel est le nom du Premier Ordre qui succède à l'Empire dans la trilogie 7-8-9 ?",
    q="Quelle faction succède à l'Empire dans la trilogie des épisodes VII à IX ?",
    a=["La Résistance", "Le Premier Ordre", "Le Nouvel Empire", "L'Ordre suprême"], c=1)
fix(S, "Quel est le vrai prénom du personnage 'Rey' dans la trilogie des suites ?",
    q="De quelle famille Rey descend-elle ?", a=["Skywalker", "Palpatine", "Solo", "Kenobi"], c=1,
    fb="Rey est la petite-fille de l'Empereur Palpatine. À la fin de la saga, elle choisit pourtant de porter le nom Skywalker.")
drop(S, "Quel est le surnom de Grogu dans The Mandalorian ?")                       # « The Child » aussi juste
drop(S, "Quel est le Code Jedi sur les émotions ?")                                  # doublon
drop(S, "Quel est l'armure caractéristique de Boba Fett ?")
drop(S, "Quel est le nom de la technique de Force permettant d'étrangler à distance ?")
drop(S, "Quel est le nom de la Force sensible aux prédictions dans Star Wars ?")
drop(S, "Quel est le style de combat Jedi que Mace Windu a créé ?")                 # doublon
fix(S, "Quel est le nom du Gardien des Vaults de l'Empire dans la série Andor ?",
    q="Quelle officière du Bureau de la sécurité impériale traque les rebelles dans la série Andor ?",
    a=["Mon Mothma", "Dedra Meero", "Vel Sartha", "Bix Caleen"], c=1)
fix(S, "Quel personnage dit 'Do or do not, there is no try' ?",
    q="Qui dit « Fais-le, ou ne le fais pas. Il n'y a pas d'essai » ?")
fix(S, "Quelle planète donne son nom à la culture guerrière des porteurs d'armure beskar dans Star Wars ?",
    a=["Concord Dawn", "Sundari", "Mandalore", "Keldabe"], c=2,
    fb="Mandalore est la planète d'origine des Mandaloriens, ravagée par l'Empire. La reconquérir est un enjeu central de The Mandalorian.")
drop(S, "Comment s'appelle la force mystique entre Rey et Kylo Ren ?")
fix(S, "Quel personnage Mandalorien possède le Darksaber avant Din Djarin ?", q="Qui possède le Darksaber avant Din Djarin ?")
drop(S, "Comment s'appelle la technique de saut hyperspatial des vaisseaux Star Wars ?")
fix(S, "Quelle série Disney+ suit un maître Jedi en exil sur Tatooine, entre les deux trilogies Star Wars ?",
    a=["Andor", "Obi-Wan Kenobi", "Ahsoka", "The Book of Boba Fett"], c=1)


# ---------------------------------------------------------------- Marvel
S = 'marvel'
fix(S, "Quel personnage brandit le marteau Mjolnir ?", q="À qui appartient le marteau Mjolnir ?")
drop(S, "Quelle gemme de l'infini contrôle l'espace ?")                           # réponse dans la question
fix(S, "Quel est le nom de l'axe forgé par Thor pour remplacer Mjolnir ?",
    q="Quelle hache Thor obtient-il pour remplacer Mjolnir ?",
    fb="Stormbreaker est forgée à Nidavellir par le nain Eitri, avec l'aide de Thor, dans Avengers : Infinity War.")
drop(S, "Quel nain forge Stormbreaker et est le seul à pouvoir créer des armes infinies ?")  # doublon
drop(S, "Quel film MCU introduit massivement le multivers ?")                     # la série Loki l'introduit avant
fix(S, "Comment s'appelle la cité créée par Ultron dans Age of Ultron ?",
    q="Quel pays Ultron soulève-t-il dans les airs dans Avengers : L'Ère d'Ultron ?",
    fb="La Sokovie, pays fictif d'Europe de l'Est, est arrachée du sol par Ultron, qui veut la faire retomber comme une météorite.")
fix(S, "Quel est le vrai prénom de Captain Marvel ?",
    q="Quel est le vrai nom de Captain Marvel ?",
    fb="Carol Danvers est Captain Marvel. Après l'accident qui lui donne ses pouvoirs, les Kree la privent de ses souvenirs et l'appellent Vers.")
drop(S, "Quel métal est le plus résistant dans l'univers Marvel ?")
fix(S, "Quelle gemme est contenue dans l'Œil d'Agamotto de Doctor Strange ?",
    fb="L'Œil d'Agamotto renferme la Gemme du Temps, verte, que Doctor Strange finit par céder à Thanos sur Titan.")
drop(S, "Qui est le grand antagoniste de la Phase 5 et 6 du MCU ?")                # Kang remplacé par Fatalis
fix(S, "Quel personnage dit 'je suis inévitable' ?", q="Quel personnage dit « Je suis inéluctable » dans Avengers : Endgame ?")
drop(S, "Quel est le vrai nom du premier Ant-Man et inventeur du Pym Particle ?")  # doublon
drop(S, "Quel est le prénom du père de Peter Parker biologique ?")
drop(S, "Quel est le record de Hank Pym en matière de taille réduite — comment appelait-on ce mode extrême ?")
fix(S, "Dans quel film Thor perd-il son marteau Mjolnir définitivement la première fois ?",
    q="Dans quel film Hela détruit-elle Mjolnir ?")
drop(S, "Quelle organisation ennemie tente de mettre la main sur les Infinity Stones avant Thanos ?")
drop(S, "Quel personnage MCU est également connu comme le meilleur archer du monde ?")   # doublon
fix(S, "Qui est le vrai Sorcier Suprême avant Doctor Strange ?",
    fb="L'Ancien est le Sorcier suprême avant Strange. Elle prolonge secrètement sa vie en puisant dans la Dimension noire.")
drop(S, "Quel était le but de Thanos avec les 6 gemmes selon lui ?")              # doublon
drop(S, "Quel personnage a le plus de variantes (versions alternatives) dans le MCU à ce jour ?")
fix(S, "Quel est le prénom de la fille de Thanos qui rejoint les Avengers ?",
    q="Quelle fille adoptive de Thanos fait partie des Gardiens de la Galaxie dès le premier film ?")
drop(S, "Quel Avenger peut courir à la vitesse de la lumière et joue de la guitare ?")
fix(S, "Quel est le résultat du claquement de doigts de Tony Stark dans Endgame ?",
    a=["Il ramène la moitié de l'univers", "Il réduit Thanos et son armée en poussière", "Il détruit les Gemmes", "Il emprisonne Thanos"], c=1,
    fb="Les disparus ont été ramenés par le claquement de Hulk. Celui de Tony réduit Thanos et toute son armée en poussière, au prix de sa vie.")
