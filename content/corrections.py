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


# ---------------------------------------------------------------- Game of Thrones
S = 'got'
drop(S, "Quelle est la devise non-officielle des Lannister ?")                  # réponse dans la question
fix(S, "Qui siège sur le Trône de Fer à la fin de la série ?", q="Qui devient roi à la fin de la série ?",
    fb="Bran Stark est désigné roi lors du conseil final. Le Trône de Fer, lui, a été fondu par Drogon.")
fix(S, "Qui dit 'Valar Morghulis' à Arya pour la première fois ?",
    fb="Jaqen H'ghar apprend à Arya les mots « Valar Morghulis » (« Tous les hommes doivent mourir ») et lui confie une pièce de fer pour le retrouver à Braavos.")
drop(S, "Comment s'appelle la grande muraille de glace au nord ?")             # réponse dans la question
fix(S, "Comment s'appelle l'épée d'Arya Stark ?", a=["Aiguille", "Piquenette", "Épine", "Briseur de glace"], c=0)
fix(S, "Quel est le nom de l'épée en acier valyrien de Jon Snow ?", a=["Aiguille", "Grand-Griffe", "Glace", "Crépuscule"], c=1,
    fb="Grand-Griffe (Longclaw) est une épée en acier valyrien au pommeau en tête de loup, offerte à Jon par le Lord Commandant Mormont.")
drop(S, "Quel objet en acier valyrien Jon Snow utilise pour tuer les Marcheurs Blancs ?")   # doublon
fix(S, "Comment Robb Stark meurt-il dans la série ?",
    fb="Robb Stark est assassiné aux Noces Pourpres, organisées par Walder Frey avec Roose Bolton, en violation des lois sacrées de l'hospitalité.")
fix(S, "Quel personnage est surnommé 'Petite Finger' (Littlefinger) ?", q="Quel personnage est surnommé Littlefinger ?")
drop(S, "Qui est Varys dans la série ?")                                         # doublon
fix(S, "Quelle est la langue construite des Dothraki dans la série ?", q="D'où vient la langue dothrakie parlée dans la série ?")
fix(S, "Qui est la Main du Roi en titre au début de la série ?", q="Quelle Main du Roi meurt juste avant le début de la série ?")
drop(S, "Qui est la déesse principale adorée dans le culte du Seigneur de Lumière ?")    # réponse dans la question
drop(S, "Comment s'appelle la chaîne de montagnes séparant la Vallée d'Arryn ?")       # réponse dans la question
drop(S, "Qui est Qyburn, le médecin de Cersei ?")
drop(S, "Comment s'appelle la langue internationale créée par les Valyrians ?")
fix(S, "Comment s'appelle la Garde personnelle de Daenerys, guerrières d'élite ?",
    q="Comment s'appellent les soldats eunuques que Daenerys libère et qui choisissent de la servir ?",
    a=["Les Dothrakis", "Les Immaculés", "Les Puînés", "Les Fils de la Harpie"], c=1)
drop(S, "Comment s'appelle le fils de Ned Stark qui reste et découvre les secrets du passé ?")  # réponse dans la question
fix(S, "Comment s'appelle Theon Greyjoy après sa capture et torture par les Bolton ?",
    a=["L'Esclave", "L'Écorché", "Schlingue", "Greyjoy le Brisé"], c=2,
    fb="Ramsay Bolton brise Theon jusqu'à ce qu'il réponde au nom de Schlingue (Reek en version originale).")
drop(S, "Quelle est la coutume de la Nuit des Noces aux Noces Pourpres (mariage de Joffrey) ?")
drop(S, "Qui est Ramsay Bolton et quelle est sa réputation ?")                 # réponse dans la question
drop(S, "Quelle est la maison qui gouverne Harrenhal, château maudit le plus grand de Westeros ?")
drop(S, "Quel est le nom de l'épée en Valyrien de Tyrion Lannister ?")
drop(S, "Comment s'appelle la compagne de Tormund le Sauvage ?")
drop(S, "Quel est le nom de l'arbalète utilisée par Tyrion pour tuer son père ?")
fix(S, "Quel est le prénom de la fille de Ned Stark qui épouse Tyrion ?", a=["Arya", "Sansa", "Myrcella", "Margaery"], c=1)
fix(S, "Comment s'appelle la technique d'escrime syrio que pratique Arya ?",
    q="Comment s'appelle le style d'escrime braavien que Syrio Forel enseigne à Arya ?",
    a=["La danse de l'eau", "La danse des dragons", "La voie de la lame", "Le pas du serpent"], c=0,
    fb="La danse de l'eau est le style d'escrime de Braavos, fluide et rapide. Syrio Forel, ancien Premier Épée de Braavos, l'enseigne à Arya.")
drop(S, "Quel est le vrai prénom du Grand Mestre Pycelle ?")
drop(S, "Comment s'appelle la saison courte qui choque les fans par son rythme accéléré ?")


# ---------------------------------------------------------------- Vikings
S = 'vikings'
fix(S, "Comment s'appelle le fils de Ragnar né avec des os fragiles ?", a=["Ubbe", "Hvitserk", "Sigurd", "Ivar le Désossé"], c=3,
    fb="Ivar le Désossé est né avec une maladie des os. Malgré son handicap, il devient l'un des plus redoutables stratèges vikings.")
fix(S, "Comment s'appelle la méthode d'exécution rituelle des Vikings ?",
    fb="L'aigle de sang est un supplice rituel où l'on brise les côtes de la victime pour en tirer les poumons. Dans la série, c'est le sort que les fils de Ragnar réservent au roi Aella.")
fix(S, "Comment s'appelle la Grande Armée vikinge venue venger Ragnar ?",
    a=["L'Armée du Nord", "La Flotte des Vengeurs", "La Grande Armée païenne", "La Horde des Lothbrok"], c=2,
    fb="La Grande Armée païenne (Great Heathen Army) envahit l'Angleterre en 865, comme le rapportent les chroniques anglo-saxonnes.")
fix(S, "Qui tue Ragnar en le jetant dans un puits de serpents ?",
    fb="Le roi Aella de Northumbrie fait jeter Ragnar dans une fosse aux serpents, ce qui pousse ses fils à lever la Grande Armée païenne pour le venger.")
fix(S, "Comment s'appelle la ville principale des Vikings dans la série ?",
    fb="Kattegat est la ville où vivent Ragnar et les siens. Elle porte le nom du détroit qui sépare le Danemark de la Suède.")
drop(S, "Quel est le nom du parlement/assemblée viking ?")                    # Thing et Althing : deux réponses justes
drop(S, "Quel roi norvégien historique tente d'unifier la Scandinavie dans la série ?")   # doublon
fix(S, "Quel est le nom de la ville fondée par Rollo en France ?", q="Quelle ville devient la capitale du duché de Rollo ?",
    fb="Rouen devient la capitale de la Normandie, cédée à Rollo par le roi franc Charles le Simple en 911.")
fix(S, "Qui est le fils Alfred qui deviendra Alfred le Grand ?",
    q="Dans la série, qui est le vrai père d'Alfred, le futur Alfred le Grand ?",
    a=["Ecbert", "Athelstan", "Ragnar", "Æthelwulf"], c=1,
    fb="Dans la série, Alfred est le fils de Judith et du moine Athelstan, même s'il est élevé comme le fils d'Æthelwulf.")
fix(S, "Comment s'appelle la première colonie permanente en Amérique du Nord par des Vikings ?",
    q="Comment les Vikings appelaient-ils la terre d'Amérique du Nord découverte par Leif Erikson ?",
    fb="Le Vinland désigne la côte nord-américaine atteinte par Leif Erikson vers l'an 1000. Le site de L'Anse aux Meadows, à Terre-Neuve, en garde la trace.")
drop(S, "Quel est le destin de Floki à la fin de la série ?")
drop(S, "Comment s'appelle la pratique guerrière des guerriers en transe d'Odin ?")
fix(S, "Quel est le type de navire de guerre viking emblématique ?", a=["La caravelle", "Le drakkar", "Le knarr", "La galère"], c=1)
drop(S, "Quel est le destin de Ragnar selon la série ?")                      # doublon
drop(S, "Quel destin Ragnar choisit-il pour lui-même selon les prédictions dans la série ?")
drop(S, "Qui est le vrai fils biologique d'Aslaug qui hérite de pouvoirs de voyance ?")
drop(S, "Comment s'appelle le compagnon de Ragnar, le forgeron, dans les premières saisons ?")  # doublon
fix(S, "Quel est le nom du chef des Anglais qui baptise Rollo et devient son beau-père ?",
    q="Quel roi franc offre sa fille Gisla et des terres à Rollo ?")
drop(S, "Quelle est la signification du mot 'viking' en vieux norrois ?")      # étymologie débattue
drop(S, "Comment s'appellent les 9 mondes de la cosmologie nordique reliés par Yggdrasil ?")
drop(S, "Quel dieu nordique est associé à la magie Seidr ?")                    # surtout Freyja
drop(S, "Quel est le nom du fils de Ragnar qui devient roi de Kiev selon la série ?")  # faux
drop(S, "Quel personnage de la série Vikings incarne le frère d'Ivar ?")
drop(S, "Comment s'appelle la salle d'Odin où les Einherjar s'entraînent ?")   # doublon
drop(S, "Quel est le nom du personnage de la série qui devient le premier viking chrétien ?")
drop(S, "Quel est l'équivalent des Einherjar dans la mythologie nordique ?")
drop(S, "Comment Ragnar recrute-t-il ses guerriers dans la série ?")
drop(S, "Quel est le nom de l'expédition légendaire de Björn vers la Méditerranée ?")


# ---------------------------------------------------------------- Stranger Things
S = 'strangerthings'
drop(S, "Quel est le prénom de la jeune fille aux pouvoirs dans Stranger Things ?")
fix(S, "Comment s'appelle la dimension sombre et parallèle ?",
    a=["La Zone sombre", "La Dimension X", "Le Monde à l'envers", "La Zone rouge"], c=2,
    fb="Le Monde à l'envers (The Upside Down) est une dimension parallèle obscure, copie déformée de Hawkins, envahie de créatures.")
drop(S, "Comment s'appelle le surnom de l'Upside Down utilisé par les enfants ?")   # doublon
drop(S, "Comment s'appelle la mère de Will Byers ?")                               # réponse dans la question
fix(S, "Quel est le prénom du meilleur ami de Mike Wheeler, fan de science-fiction ?",
    fb="Dustin Henderson, toujours coiffé de sa casquette, est le scientifique enthousiaste de la bande. Son amitié avec Steve est l'une des plus touchantes de la série.")
drop(S, "Comment s'appelle le laboratoire secret sous la ville de Hawkins ?")      # réponse dans la question
fix(S, "Comment s'appelle la grosse créature à tentacules de la saison 2 ?",
    a=["Le Démogorgon", "Le Démochien", "Le Flagelleur mental", "Vecna"], c=2,
    fb="Le Flagelleur mental (Mind Flayer), nommé d'après un monstre de Donjons et Dragons, est l'entité géante qui prend possession de Will en saison 2.")
fix(S, "Qui est Billy Hargrove et quel est son rôle ?",
    a=["Le demi-frère de Max, possédé par le Flagelleur mental", "Le chef des Soviétiques", "Un agent du laboratoire", "Le petit ami d'Eleven"], c=0,
    fb="Billy est le demi-frère, par alliance, de Max. Possédé par le Flagelleur mental en saison 3, il finit par se sacrifier pour sauver Eleven.")
fix(S, "Comment s'appellent les créatures comme des chiens à 6 pattes de l'Envers ?",
    q="Comment s'appellent les créatures canines du Monde à l'envers apparues en saison 2 ?",
    fb="Les démochiens (Demodogs) sont des créatures du Monde à l'envers. Dustin en recueille un tout petit, qu'il appelle Dart.")
drop(S, "Qui est le personnage 'interdimensionnel' que Dustin renomme ?")         # doublon
fix(S, "Quel est le grand antagoniste de la saison 4 aux pouvoirs humains ?",
    fb="Vecna, de son vrai nom Henry Creel, est le tout premier sujet de Brenner. Il a massacré les autres enfants du laboratoire.")
drop(S, "Quel personnage sauve Max de Vecna grâce à la musique en saison 4 ?")    # toute la bande est présente
drop(S, "Quelle est la règle que Max et ses amis utilisent pour combattre Vecna ?")
drop(S, "Comment s'appelle le club de D&D du lycée de Hawkins en saison 4 ?")     # réponse dans la question
drop(S, "Qui est Erica, la sœur de Lucas ?")
drop(S, "Quel film de Spielberg influence le plus clairement la série ?")
drop(S, "Qui est Robin Buckley dans la série ?")
drop(S, "Quelle est la couleur visuelle de l'Envers dans la série ?")
fix(S, "Quelle réplique d'Eleven est l'une des plus mémorables de la série ?",
    a=["Joyce, je ne me sens pas bien", "Dustin, arrête", "Mike, je t'aime", "Les amis ne mentent pas"], c=3,
    fb="« Les amis ne mentent pas » (Friends don't lie) est la règle d'or d'Eleven, qu'elle répète à la bande dès la saison 1.")
fix(S, "Qui est la mère biologique d'Eleven ?",
    fb="Terry Ives est la mère biologique d'Eleven. Elle participait à des expériences du programme MK-Ultra quand elle était étudiante.")
drop(S, "Quelle saison de Stranger Things est la plus longue (épisodes de +1h30) ?")
fix(S, "Quel personnage de D&D donne son nom à l'antagoniste de la saison 4 ?", a=["Une liche", "Vecna", "Le Flagelleur mental", "Le Tyrannoeil"], c=1)
drop(S, "Comment les habitants de Hawkins nomment-ils l'ouverture dimensionnelle vers la dimension parallèle obscure ?")
drop(S, "Comment s'appelle la professeure Madame de Strangerthings qui surveille Eleven au labo ?")
drop(S, "Quelle réplique Dustin dit-il souvent avec enthousiasme pour exprimer son amour de la science ?")
drop(S, "Quel film d'horreur de Stephen King est cité par Max en saison 4 ?")
drop(S, "Quel est le prénom du petit ami de Mike Wheeler dans les saisons récentes ?")
drop(S, "Comment s'appelle la ville de l'Indiana dont les événements de la série sont inspirés ?")
drop(S, "Quel est l'âge d'Eleven (Millie Bobby Brown) lors de la saison 1 en 2016 ?")
drop(S, "Quel jeu vidéo d'arcade est présent dans le Starcourt Mall en saison 3 ?")
drop(S, "Quel est le prénom du père d'Eleven (son père biologique) ?")
drop(S, "Quelle couleur a le Mind Flayer dans sa forme physique en saison 3 ?")
fix(S, "Quel est le nom de la fille de couleur rouge qui aide le groupe dans les saisons récentes ?",
    q="Quelle nouvelle venue aux cheveux roux rejoint la bande en saison 2 ?")
drop(S, "Quel est le nom du manager du magasin au Starcourt Mall où Steve et Robin travaillent ?")   # Keith tient le vidéoclub
drop(S, "Combien de saisons Stranger Things compte-t-elle (annoncées) ?")         # dépassé
drop(S, "Quel personnage du groupe possède des dreadlocks et est grand ?")
fix(S, "Quelle marque de céréales Eleven mange en grande quantité dans la saison 1 ?",
    q="Quelle nourriture Eleven adore-t-elle dans la saison 1 ?",
    a=["Des Lucky Charms", "Des gaufres Eggo", "Des Corn Flakes", "Des Froot Loops"], c=1,
    fb="Les gaufres Eggo sont la gourmandise préférée d'Eleven, au point de devenir l'un des symboles de la série.")
drop(S, "Quel est le prénom du fils de Billy qui est empoisonné par le Mind Flayer ?")
drop(S, "Quelle série de science-fiction des années 1980 à propos d'un alien est regardée par les personnages dans la série ?")
drop(S, "Comment Eddie Munson décrit-il Metallica dans la saison 4 ?")
drop(S, "Quel est le lien entre Will Byers et l'Envers selon la théorie des fans ?")
drop(S, "Quel film est regardé par les enfants au cinéma drive-in dans la saison 1 ?")
fix(S, "Comment s'appelle le petit ami geek et gentil de Joyce qui joue un rôle important dans la saison 2 ?",
    fb="Bob Newby (Sean Astin), le petit ami de Joyce en saison 2, aide le groupe à s'échapper du laboratoire et meurt en héros.")


# ---------------------------------------------------------------- Breaking Bad
S = 'breakingbad'
fix(S, "Quel est le nom de l'avocat véreux qui aide Walter et Jesse ?", a=["Bob Odenkirk", "Mike Ehrmantraut", "Howard Hamlin", "Saul Goodman"], c=3)
fix(S, "Comment s'appelle le restaurant-façade du baron de la drogue ennemi de Walter ?",
    q="Quelle chaîne de restaurants sert de façade à Gus Fring ?",
    a=["Los Pollos Hermanos", "Lavandería Brillante", "A1A Car Wash", "Vamonos Pest"], c=0)
drop(S, "Comment Hank découvre-t-il finalement l'identité d'Heisenberg ?")       # doublon
fix(S, "Quelle est la dernière réplique marquante de Walter White ?",
    q="Quel aveu Walter fait-il enfin à Skyler dans le dernier épisode ?",
    a=["Je suis Heisenberg", "Je l'ai fait pour moi", "Je suis désolé", "C'est moi le danger"], c=1,
    fb="« Je l'ai fait pour moi. J'aimais ça. J'étais doué. » Walter admet enfin avoir agi par orgueil, et non pour sa famille.")
fix(S, "Comment s'appelle le film suite à Breaking Bad ?", a=["Better Call Saul", "Jesse", "El Camino", "Heisenberg"], c=2)
drop(S, "Quel est le cartel mexicain ennemi de Gus Fring ?")                     # réponse dans la question, réponse discutable
drop(S, "Quel est le pays où se déroule Breaking Bad ?")                          # doublon
drop(S, "Dans quel état américain se déroule entièrement Breaking Bad ?")         # doublon
drop(S, "Comment s'appelle l'organisation de Walter qui se développe en saison 5 ?")
drop(S, "Quelle université Walter White a-t-il cofondée avant de la quitter ?")   # doublon, et ce n'est pas une université
fix(S, "Comment Hector Salamanca communique-t-il depuis son fauteuil roulant ?",
    a=["En claquant des doigts", "Avec une clochette", "Avec une tablette", "En clignant des yeux"], c=1,
    fb="Hector Salamanca, paralysé, communique en faisant sonner une clochette. Ce détail joue un rôle décisif dans la mort de Gus Fring.")
drop(S, "Quel objet Todd vole lors du vol du train en saison 5 ?")
drop(S, "Comment Gus Fring cache-t-il sa double vie ?")
drop(S, "Quelle drogue Jesse consomme-t-il principalement ?")                     # il consomme aussi de l'héroïne
drop(S, "Qui est la compagne d'Andrea, mère du petit Brock ?")
fix(S, "Quel est le résultat final de l'empire Heisenberg ?",
    fb="Walter revient à Albuquerque, élimine le gang de Jack, libère Jesse et meurt de ses blessures dans le laboratoire des néonazis.")
drop(S, "Quelle est la phrase symbolique de Walter concernant son cancer à la fin de la série ?")
drop(S, "Quel est le surnom de l'informateur de la DEA qui permet d'arrêter Tuco ?")
fix(S, "Comment Walter tue-t-il Emilio lors de leur première rencontre ?",
    a=["À coups de bâton", "Avec un pistolet", "Avec du gaz phosphine", "Avec de l'acide"], c=2,
    fb="Pendant la cuisson dans le camping-car, Walter jette du phosphore rouge dans l'eau bouillante. Le gaz phosphine qui se dégage tue Emilio.")
fix(S, "Quel est le vrai nom de 'Heisenberg' dans le contexte chimique ?",
    q="À quel scientifique le pseudonyme de Walter fait-il référence ?")
fix(S, "Quel acteur joue Gus Fring dans Breaking Bad ?",
    fb="Giancarlo Esposito incarne Gustavo Fring avec une froideur magistrale. Il reprend le rôle dans Better Call Saul.")
fix(S, "Quel est le prénom du frère cadet de Jesse Pinkman mentionné dans la série ?",
    a=["Jesse Jr.", "Brock", "Todd", "Jake"], c=3,
    fb="Jake est le petit frère de Jesse, un élève modèle que ses parents préfèrent à leur aîné.")
fix(S, "Comment Jesse échappe-t-il au camp de Jack à la fin de la série ?",
    a=["Il s'échappe à pied", "Il est libéré par la police", "Il fuit au volant de la voiture de Todd", "Il se cache dans un camion"], c=2,
    fb="Après la fusillade, Walter libère Jesse, qui s'enfuit en hurlant au volant de la voiture de Todd, la fameuse El Camino.")
drop(S, "Quel est le montant exact que Walter remet à Hank depuis son RV de cuisson ?")
drop(S, "Comment s'appelle l'émission de TV que Saul Goodman anime dans Better Call Saul ?")
drop(S, "Quel est le nom du distributeur de la meth de Walter à Phoenix ?")
fix(S, "Comment Walter empoisonne-t-il Lydia à la fin de la série ?",
    a=["Avec du cyanure dans son café", "Avec de la ricine dans sa stévia", "En contaminant ses médicaments", "Par injection"], c=1,
    fb="Walter met de la ricine dans la stévia que Lydia verse dans son thé, lors de leur dernier rendez-vous.")
drop(S, "Quel personnage dit 'Si tu essaies de me planter, je te tue' à Jesse ?")
drop(S, "Comment se nomme la méthylamine que Walter utilise — où la vole-t-il en saison 5 ?")   # doublon
fix(S, "Comment se nomme la chaîne de pizzerias que Walter utilise brièvement comme couverture ?",
    q="Quelle entreprise de désinsectisation sert de couverture à Walter, Jesse et Mike en saison 5 ?",
    a=["Pizza Palace", "Vamonos Pest", "Pollos del Norte", "A1A Car Wash"], c=1)
fix(S, "Quel personnage récurrent est tué par Todd lors du vol de train ?", q="Qui Todd abat-il juste après le vol du train ?")
drop(S, "Quel est le surnom que Mike utilise pour désigner Walter ?")
drop(S, "Quel est l'objet que Walter met symboliquement dans la poubelle avant de cuisiner pour la première fois ?")
drop(S, "Comment Walter justifie-t-il sa décision de cuisiner à sa femme Skyler au début ?")
drop(S, "Quel est le prénom du beau-frère de Walter que Hank blesse accidentellement ?")
fix(S, "Qui est le 'fournisseur' de Saul Goodman pour les faux papiers ?",
    fb="Ed Galbraith, officiellement réparateur d'aspirateurs, organise des disparitions complètes avec une nouvelle identité.")
drop(S, "Comment Walter fait-il croire à Hank qu'il n'est pas Heisenberg lors de leur confrontation finale ?")
drop(S, "Quel est le nom de la célèbre pizzeria que Walter lance sur le toit dans la série ?")


# ---------------------------------------------------------------- Histoire
S = 'histoire'
fix(S, "Quel roi de France construit le château de Versailles ?",
    q="Quel roi de France fait de Versailles sa résidence principale en 1682 ?")
fix(S, "Quel accord secret partage le Proche-Orient entre France et Angleterre après la WW1 ?",
    q="Quel accord secret de 1916 prévoit le partage du Proche-Orient entre la France et le Royaume-Uni ?",
    fb="Les accords Sykes-Picot (1916), négociés pendant la Première Guerre mondiale, partagent en zones d'influence les territoires de l'Empire ottoman.")
fix(S, "Quelle bataille historique oppose les Grecs aux Perses en -480 ?",
    q="Quelle bataille navale de -480 voit la flotte grecque vaincre la flotte perse ?",
    fb="À Salamine, en -480, la flotte grecque menée par Thémistocle anéantit la flotte perse. La même année, les Spartiates de Léonidas étaient tombés aux Thermopyles.")
fix(S, "En quelle année la Révolution Américaine aboutit-elle à l'indépendance des États-Unis ?",
    q="En quelle année la Déclaration d'indépendance des États-Unis est-elle signée ?")
fix(S, "Qui est Olympe de Gouges et quel est son apport à la Révolution ?",
    fb="Olympe de Gouges rédige la Déclaration des droits de la femme et de la citoyenne en 1791. Elle est guillotinée en 1793, sous la Terreur.")
drop(S, "Quelle guerre civile espagnole préfigure la Seconde Guerre Mondiale ?")   # réponse dans la question
drop(S, "En quelle année la France participe-t-elle à la première Guerre du Golfe ?")  # troupes engagées dès 1990
fix(S, "Quel était le nom de l'État allemand pro-nazi installé après la défaite de 1940 ?",
    q="Quel est le nom officiel du régime installé à Vichy en 1940 ?",
    a=["Le Reich de Vichy", "L'État français", "La IIIe République", "Le Gouvernement provisoire"], c=1,
    fb="L'État français, dit régime de Vichy, est dirigé par le maréchal Pétain de 1940 à 1944 et collabore avec l'Allemagne nazie.")


# ---------------------------------------------------------------- Culture générale
S = 'culture'
drop(S, "Quel philosophe grec est à l'origine de la méthode dialectique ?")       # Socrate aussi
fix(S, "Quelle planète possède le plus grand nombre de lunes connues (2024) ?",
    q="Quelle planète possède le plus grand nombre de lunes connues ?",
    fb="Saturne détient le record : en 2025, on lui connaît plus de 270 lunes, loin devant Jupiter.")
drop(S, "Quel pays possède le plus grand nombre de langues officielles au monde ?")   # la Bolivie en reconnaît 37
fix(S, "Qui a fondé l'entreprise Apple Computer avec Steve Jobs en 1976 ?",
    a=["Bill Gates", "Steve Wozniak", "Steve Ballmer", "Tim Cook"], c=1)
drop(S, "Quel est le roman de Dostoïevski considéré comme son chef-d'œuvre ?")   # subjectif
fix(S, "Quel est le nombre de côtés d'un dodécaèdre régulier ?", q="Combien de faces possède un dodécaèdre régulier ?")
fix(S, "Quel est le plus petit continent du monde ?",
    fb="L'Australie est le plus petit continent, avec environ 7,7 millions de km².")
fix(S, "Quel est le nom du chef-d'œuvre de Shakespeare basé sur un roi danois légendaire ?",
    q="Quelle pièce de Shakespeare s'inspire de la légende du prince danois Amleth ?")


# ---------------------------------------------------------------- Sport
S = 'sport'
drop(S, "Combien de buts Pelé a-t-il marqués en carrière officielle ?")         # décompte contesté
fix(S, "Qui remporte le Ballon d'Or 2023 et la Coupe du Monde 2022 ?",
    fb="Lionel Messi remporte la Coupe du monde 2022 puis le Ballon d'Or 2023, le huitième de sa carrière.")
drop(S, "Qui est surnommé 'Air Jordan' ?")                                       # réponse dans la question
drop(S, "Quel coureur cycliste a le plus de victoires légitimes au Tour de France ?")   # quatre coureurs à égalité
drop(S, "Combien de points vaut un ace au tennis (service direct) ?")
drop(S, "Quel pays a co-inventé le basketball selon l'histoire officielle ?")
fix(S, "Quel est le score maximal possible dans une manche au bowling ?", q="Quel est le score parfait au bowling ?",
    fb="300 points est le score parfait au bowling : douze strikes consécutifs sur une partie de dix carreaux.")
fix(S, "Quel pays a remporté le plus de titres en Rugby World Cup ?",
    q="Quel pays a remporté le plus de Coupes du monde de rugby ?",
    a=["Australie", "Angleterre", "Afrique du Sud", "Nouvelle-Zélande"], c=2,
    fb="L'Afrique du Sud détient le record avec 4 titres (1995, 2007, 2019 et 2023), devant la Nouvelle-Zélande (1987, 2011, 2015).")
fix(S, "Quel est le nom du stade où se joue la finale du championnat d'Angleterre de football ?",
    q="Dans quel stade se joue la finale de la FA Cup ?")
drop(S, "Quelle est la longueur d'un terrain de football standard (FIFA) ?")    # réponse dans la question, ambiguë
fix(S, "En combien de temps Usain Bolt court-il le 200m (record du monde) ?",
    fb="Usain Bolt court le 200 m en 19,19 s à Berlin, en 2009. Ce record du monde tient toujours.")
drop(S, "Quel est le terme pour un coup parfait dans un match de tennis de table (ping-pong) ?")   # doublon
fix(S, "Quel est le trophée le plus prestigieux au hockey sur glace ?",
    fb="La Coupe Stanley, créée en 1893, est le plus ancien trophée du sport professionnel nord-américain. Elle récompense le champion de la LNH depuis 1926.")
drop(S, "Quel pays a remporté le plus d'or aux JO d'été en 2024 (Paris) ?")     # Chine et États-Unis à égalité (40)
drop(S, "Quel est le sport pratiqué sur un terrain appelé 'court' ?")
drop(S, "Quel sprinter français détient le record d'Europe du 100m ?")          # réponse fausse
drop(S, "Quel est le terme pour un but marqué contre son propre camp ?")        # réponse dans la question
fix(S, "Quel athlète détient le record du monde du 400m haies masculin établi à 45,94s en 2021 ?",
    fb="Karsten Warholm (Norvège) court le 400 m haies en 45,94 s en finale des JO de Tokyo 2021, effaçant de 76 centièmes son propre record.")
fix(S, "Quel est le nom de la compétition de tennis opposant les équipes nationales féminines ?",
    a=["Billie Jean King Cup", "Coupe Hopman", "Coupe Davis féminine", "Laver Cup"], c=0)
fix(S, "Quel pays a gagné le plus de médailles d'or en natation aux JO de 2024 ?",
    fb="Les États-Unis remportent 8 titres en natation à Paris 2024, juste devant l'Australie (7).")
drop(S, "Quel athlète jamaïcain détient le record du 100m en dessous des 10 secondes depuis 1988 ?")
fix(S, "Quel est le terme pour un but marqué avec la tête au football ?",
    q="Comment appelle-t-on un tir effectué avec la tête au football ?",
    a=["Une tête", "Un retourné", "Une volée", "Un lob"], c=0,
    fb="On parle simplement d'une tête : le joueur frappe le ballon du front, souvent sur un centre ou un corner.")
fix(S, "Combien d'équipes participent à la phase de groupes d'une Coupe du Monde FIFA ?",
    q="Combien d'équipes participent à la Coupe du monde 2026 ?",
    fb="La Coupe du monde 2026, organisée aux États-Unis, au Canada et au Mexique, est la première à 48 équipes, contre 32 depuis 1998.")
drop(S, "Quel est le record du monde du 1500m masculin ?")                       # explication fausse, doublon
fix(S, "Qui remporte la Formule 1 le plus de fois en championnat des constructeurs ?",
    fb="Ferrari détient le record des titres constructeurs, avec 16 couronnes.")
drop(S, "Quel est le record du saut à la perche masculin ?")                     # battu régulièrement par Duplantis
drop(S, "Quel boxeur heavyweight est surnommé 'Iron Mike' ?")                    # réponse dans la question


# ---------------------------------------------------------------- Pokémon
S = 'pokemon'
drop(S, "Quel est le Pokémon de départ le plus populaire selon les sondages officiels ?")
fix(S, "Quel oiseau légendaire de type Glace est l'un des trois légendaires de Kanto ?",
    a=["Électhor", "Artikodin", "Sulfura", "Mewtwo"], c=1,
    fb="Artikodin est l'oiseau légendaire de type Glace de Kanto, aux côtés d'Électhor (Électrik) et de Sulfura (Feu).")
fix(S, "Comment s'appelle le professeur Pokémon de la région de Kanto ?",
    fb="Le Professeur Chen (Professor Oak en anglais) remet au joueur son premier Pokémon et le Pokédex.")
drop(S, "Quel est le nom du rival du joueur dans Pokémon Rouge/Bleu/Jaune ?")     # il s'appelle Régis en VF
drop(S, "Quel est le Pokémon rival (antagoniste gentil) de Sacha dans l'animé classique ?")   # Régis, pas Pierre
drop(S, "Quel Pokémon dit uniquement son propre nom dans l'animé ?")
fix(S, "Quel Pokémon de type Psy de la Gen 1 génère des murs invisibles en mimant leurs formes ?",
    a=["Abra", "Kadabra", "Ectoplasma", "M. Mime"], c=3,
    fb="M. Mime crée des murs invisibles en les mimant. De type Psy en première génération, il devient Psy/Fée à partir de Pokémon X et Y.")
drop(S, "Quel est le type faible au type Électrik ?")                            # le Sol y est immunisé
drop(S, "Comment s'appelle la transformation de combat temporaire de Pikachu dans l'animé récent ?")
fix(S, "Quel est le seul Pokémon de type Dragon/Vol dans la génération 1 ?",
    fb="Dracolosse est le seul Pokémon Dragon/Vol de la première génération. Minidraco et Draco sont de type Dragon pur, Ptéra est Roche/Vol.")
drop(S, "Comment s'appelle la technique d'échange de Pokémon permettant d'évoluer certains Pokémon ?")
drop(S, "Quel est le Pokémon le plus difficile à attraper dans Pokémon Rouge/Bleu selon les joueurs ?")
drop(S, "Comment s'appelle l'attaque la plus puissante de type Normal (150 puissance) ?")
drop(S, "Quel est le Pokémon champion des 8 arènes dans la région de Johto ?")
fix(S, "Quel Pokémon est impossible d'obtenir légitimement dans la génération 1 sans code Missingno ?",
    q="Quel Pokémon de la première génération ne peut pas être obtenu normalement dans les jeux ?")
fix(S, "Comment s'appelle le type fort contre presque tous les types dans Gen 1 (buggy) ?",
    q="Quel type dominait la première génération, notamment à cause d'un bug ?",
    a=["Psy", "Spectre", "Dragon", "Poison"], c=0,
    fb="Le type Psy écrasait la première génération : à cause d'un bug, les attaques Spectre n'avaient aucun effet sur lui. Le problème a été corrigé en deuxième génération.")
fix(S, "Quel Pokémon à trois têtes est l'évolution de Doduo au niveau 31 ?",
    a=["Ptéra", "Ronflex", "Dodrio", "Évoli"], c=2,
    fb="Doduo, l'oiseau à deux têtes, évolue au niveau 31 en Dodrio, qui en a trois. Il est de type Normal/Vol.")
drop(S, "Quelle est la région la plus récente dans les jeux Pokémon principaux (à ce jour) ?")
drop(S, "Quel est le Pokémon le plus populaire selon les sondages globaux officiels de Game Freak ?")
drop(S, "Comment s'appelle le type ultra-faible au type Acier dans Gen 2+ ?")
fix(S, "Comment s'appelle l'attaque de type Fantôme signature de Gengar ?",
    q="Quelle attaque de type Spectre est emblématique d'Ectoplasma ?",
    a=["Ball'Ombre", "Vampirisme", "Jackpot", "Tranche-Nuit"], c=0,
    fb="Ball'Ombre (Shadow Ball) est l'attaque Spectre emblématique d'Ectoplasma. Tranche-Nuit, elle, est une attaque de type Ténèbres.")
drop(S, "Quel Pokémon est la forme éveillée de Ronflex (Snorlax) dans les combats ?")
drop(S, "Quel est le seul Pokémon à ne pas avoir d'attaque dans Gen 1 ?")
drop(S, "Quelle est la signature de l'attaque Méga-Poing par rapport au Poing-Meteor ?")
fix(S, "Quel est le Pokémon numéro 150 du Pokédex de Kanto ?", a=["Mewtwo", "Mew", "Léviator", "Dracolosse"], c=0)
fix(S, "Quel type de Pokémon est immunisé aux dégâts de terrain Électrik ?", q="Quel type est immunisé contre les attaques de type Électrik ?")
fix(S, "Comment s'appelle le quatrième champion de la Ligue Pokémon (Elite 4) dans Gen 1 ?",
    q="Qui est le quatrième membre du Conseil 4 de Kanto ?", a=["Agatha", "Aldo", "Olga", "Peter"], c=3,
    fb="Peter (Lance en anglais), dresseur de Pokémon Dragon, est le dernier membre du Conseil 4, juste avant le Maître de la Ligue.")
fix(S, "Quel Pokémon est surnommé 'Pokémon Renard' et possède 9 queues ?",
    a=["Feunard", "Goupix", "Arcanin", "Galopa"], c=0,
    fb="Feunard, l'évolution de Goupix, possède neuf queues. Selon le Pokédex, quiconque tire l'une d'elles est maudit pour mille ans.")
fix(S, "Quel est le Pokémon de type Eau/Psy le plus utilisé compétitivement en Gen 1 ?",
    a=["Psykokwak", "Staross", "Tentacruel", "Akwakwak"], c=1,
    fb="Staross, de type Eau/Psy, était l'un des Pokémon les plus redoutables de la première génération grâce à sa vitesse et à ses attaques variées.")
drop(S, "Quelle est l'évolution de Noeunoeuf (Togepi) ?")
fix(S, "Quel Pokémon légendaire est le gardien des rêves dans la mythologie Pokémon ?",
    fb="Cresselia apporte des rêves paisibles. Son rival, Darkrai, plonge ceux qui dorment près de lui dans des cauchemars sans fin.")
fix(S, "Comment s'appelle la première version de Pokémon sur Nintendo Switch ?",
    q="Quel est le premier jeu Pokémon de la série principale sur Nintendo Switch ?")
drop(S, "Quel Pokémon de type Fée était Type Normal dans la Gen 1 ?")              # Mélodelfe aussi
drop(S, "Quel est l'ultime évolution de Salamèche en version Mega dans Gen 6 ?")
drop(S, "Comment s'appelle la mécanique de capture qui utilise l'état de statut ?")
fix(S, "Quelle est l'évolution de type Fée d'Évoli introduite en Gen 6 ?",
    a=["Givrali", "Phyllali", "Nymphali", "Mentali"], c=2,
    fb="Nymphali (Sylveon en anglais) est l'évolution de type Fée d'Évoli, apparue dans Pokémon X et Y.")
fix(S, "Quel est le Pokémon légendaire de Gen 3 qui exauce les vœux une fois tous les mille ans ?",
    fb="Jirachi, de type Acier/Psy, ne s'éveille que sept jours tous les mille ans, et exauce alors les vœux.")
fix(S, "Quelle est la série spin-off Pokémon d'aventure tactique sur Nintendo 64 et GameCube ?",
    q="Quel jeu Pokémon sur GameCube propose une aventure dans la région d'Orre ?",
    a=["Pokémon Snap", "Pokémon Stadium", "Pokémon Colosseum", "Pokémon Puzzle League"], c=2,
    fb="Pokémon Colosseum (2003) emmène le joueur dans la région d'Orre, où il doit purifier des Pokémon Obscurs.")
drop(S, "Comment s'appelle la récompense en objets donnée après certaines captures rares ?")
drop(S, "Quel Pokémon est une évolution récente de Noctali (Umbreon) absente de Gen 1 ?")
drop(S, "Quel est le Pokémon Normal qui peut se transformer en tout autre Pokémon ?")   # doublon
drop(S, "Comment s'appelle l'attaque Eau/Glace signature de Glace marine en compétitif ?")


# ---------------------------------------------------------------- Demon Slayer
S = 'demonslayer'
fix(S, "Comment s'appelle l'organisation qui combat les démons ?",
    a=["L'Ordre des Pourfendeurs", "Les Douze Lunes", "Le Corps des Pourfendeurs", "La Guilde des Chasseurs"], c=2)
fix(S, "Quelle est la faiblesse universelle de tous les démons ?",
    fb="La lumière du soleil réduit les démons en cendres. Les sabres Nichirin et le poison de glycine peuvent aussi les blesser ou les affaiblir.")
fix(S, "Comment s'appelle le sabre spécial des Pourfendeurs qui change de couleur ?",
    a=["Le sabre du Soleil", "Le sabre Nichirin", "Le sabre Kizuki", "Le sabre de glycine"], c=1)
fix(S, "De quelle couleur devient la lame de Tanjiro après son éveil ?",
    fb="La lame de Tanjiro devient noire, une couleur rarissime. On dit que les porteurs d'une lame noire ne deviennent jamais Piliers.")
drop(S, "Qu'est-ce que la Concentration Totale Permanente ?")                     # réponse dans la question
drop(S, "Qui est Yoriichi Tsugikuni dans l'histoire du Corps des Pourfendeurs ?")   # doublon
fix(S, "Comment s'appelle le village où les Piliers partent s'entraîner en saison 3 ?",
    q="Où Tanjiro se rend-il pour faire réparer son sabre, en saison 3 ?")
fix(S, "Quelle est la Forme Ultime (13e forme) de la Respiration du Soleil ?",
    q="En quoi consiste la treizième forme de la Respiration du Soleil ?",
    a=["Une seule frappe chargée", "L'enchaînement en boucle des douze premières formes", "Un souffle de feu", "Une danse répétée treize fois"], c=1,
    fb="La treizième forme consiste à enchaîner sans fin les douze premières formes. Yoriichi l'a conçue pour frapper tous les organes vitaux de Muzan.")
drop(S, "Quelle est la technique finale de Tanjiro contre Muzan dans la bataille finale ?")   # explication fausse
fix(S, "Qu'est-ce qui distingue le sang de Nezuko parmi tous les démons ?", q="Qu'a de particulier le sang de Nezuko ?")
drop(S, "Quel démon est la Lune Inférieure 1 qui piège dans des rêves dans le Mugen Train ?")  # doublon
fix(S, "Qui entraîne Tanjiro, Inosuke et Zenitsu dans l'arc du Quartier des Plaisirs ?",
    q="Quel Pilier emmène Tanjiro, Inosuke et Zenitsu dans le Quartier des plaisirs ?")
fix(S, "Quel Art de la Respiration utilise le Pilier des Roches, Gyomei Himejima ?",
    a=["Respiration de la Pierre", "Respiration de la Brume", "Respiration du Son", "Respiration des Ténèbres"], c=0)
drop(S, "Comment s'appelle la technique de respiration du Pilier de la Pierre Gyomei ?")   # doublon
drop(S, "Quel est le pouvoir particulier des yeux de Kanao Tsuyuri ?")              # réponse dans la question
fix(S, "Combien de saisons de l'anime Demon Slayer ont été diffusées à ce jour ?",
    q="Combien de saisons de la série animée Demon Slayer ont été diffusées avant la trilogie de films du Château de l'Infini ?",
    fb="La série compte quatre saisons, jusqu'à l'arc de l'entraînement des Piliers. La suite est adaptée au cinéma, en trois films consacrés au Château de l'Infini.")
drop(S, "Quel est le nom du frère aîné de Kokushibo (Tamis Supérieur Un) qui était un Pourfendeur légendaire ?")  # Yoriichi est le cadet
drop(S, "Quel est le poison que Shinobu Kocho a accumulé dans son corps pendant des années ?")
drop(S, "Quel est le premier démon que Tanjiro doit tuer dans la série ?")
drop(S, "Quel pouvoir Tanjiro utilise-t-il pour voir les faiblesses de ses ennemis ?")   # doublon
fix(S, "Quelle technique Muichiro Tokito déverrouille-t-il en retrouvant ses souvenirs ?",
    fb="En retrouvant ses souvenirs face à Gyokko, Muichiro voit apparaître sa Marque de Pourfendeur, et sa puissance décuple.")
drop(S, "Quel est l'effet du sang de Muzan sur les autres démons ?")
drop(S, "Quel est le nom de l'épée que Yoriichi a forgée avec un minerai spécial contre Muzan ?")
drop(S, "Quelle est la particularité de l'arc en saison 4 concernant les Piliers ?")
drop(S, "Quel personnage devient Pilier de la Flamme après la mort de Rengoku ?")
fix(S, "Quel est le nom du démon qui garde le château de Natagumo Mountain ?", q="Quel démon règne sur le mont Natagumo ?")
drop(S, "Quel démon est surnommé 'Tamis Supérieur Deux' parmi les Douze Lunes de Muzan ?")
drop(S, "Comment Inosuke Hashibira a-t-il acquis ses deux sabres dentelés ?")        # il les ébrèche à coups de pierre
drop(S, "Quel est le vrai nom de Muzan Kibutsuji dans son identité humaine ?")
drop(S, "Quelle capacité unique possède Nezuko après sa transformation partielle en démon supérieur ?")   # doublon


# ---------------------------------------------------------------- Dragon Ball
S = 'dragonball'
fix(S, "Quel est le nom de la planète d'origine des Saiyajins ?", a=["Namek", "Yardrat", "Végéta", "Kaioshin"], c=2)
fix(S, "Qui représente l'Univers 11 dans le Tournoi du Pouvoir ?",
    q="Quel combattant de l'Univers 11 pousse Goku à atteindre l'Ultra Instinct ?")
drop(S, "Qui entraîne Trunks du futur dans Dragon Ball Super ?")
drop(S, "Comment s'appelle la forme intermédiaire de Végéta entre Great Ape et SSJ4 dans GT ?")   # trois réponses identiques
drop(S, "Quel est le premier ennemi extraterrestre que Goku affronte officiellement dans DBZ ?")  # doublon
drop(S, "Quel est le nom du plan final de Cell qui consiste à s'autodétruire ?")
fix(S, "Qui crée les Dragon Balls de la Terre ?", a=["Shenron lui-même", "Kami", "Bulma", "Piccolo"], c=1)
fix(S, "Quel est le nom du fils de Gohan et Videl ?", q="Comment s'appelle la fille de Gohan et Videl ?")
fix(S, "Quel est le symbole sur la cape de Goku au début de Dragon Ball ?",
    q="Quel symbole Goku porte-t-il sur son kimono quand il s'entraîne chez Tortue Géniale ?",
    fb="Le kanji « Kame » (la tortue) désigne l'école de Tortue Géniale, chez qui Goku et Krilin s'entraînent.")
fix(S, "Quel démon contrôle l'enfer dans l'univers Dragon Ball ?",
    q="Qui juge les âmes des morts dans l'autre monde ?", a=["Le Roi Enma", "King Cold", "Babidi", "Dabra"], c=0,
    fb="Le Roi Enma juge les âmes des morts et décide de leur destination. C'est lui qui laisse Goku emprunter le Chemin du Serpent après sa mort face à Raditz.")
drop(S, "Quel démon mange les âmes et détient les enfers dans l'univers DBZ ?")          # doublon
drop(S, "Quel personnage entraîne Goku et Krilin chez Muten Roshi ?")
drop(S, "Comment Cell Jr. sont-ils créés lors des Cell Games ?")
drop(S, "Quel est le nom de la planète du Roi Kaio où Goku s'entraîne dans l'autre monde ?")    # deux réponses identiques
drop(S, "Quel est l'effet principal du Fruit de l'Arbre du Pouvoir dans le film DBZ ?")
drop(S, "Quel est le vrai nom de la technique de téléportation de Goku ?")                 # doublon
fix(S, "Comment s'appelle le fils de Goku et Chi-Chi né dans la saga Boo ?",
    q="Comment s'appelle le deuxième fils de Goku et Chi-Chi ?",
    fb="Goten naît après la saga Cell et apparaît dans la saga Boo. Il ressemble trait pour trait à son père enfant.")
fix(S, "Quel est le nom de l'attaque d'Embryon de Végéta, la boule d'énergie bleue ?",
    q="Quelle attaque de Végéta consiste à lancer une énorme boule d'énergie d'une seule main ?")
drop(S, "Qui est le Roi Kaio et quel est son rôle dans l'univers ?")
drop(S, "Quel personnage féminin est la seule guerrière Saiyajin connue de haut rang dans DBS ?")
fix(S, "Comment s'appelle le père de Végéta ?",
    q="Qui règne sur la planète des Saiyajins avant sa destruction ?", a=["Freezer", "Nappa", "Le Roi Végéta", "Paragus"], c=2,
    fb="Le Roi Végéta, père du prince Végéta, règne sur les Saiyajins jusqu'à ce que Freezer le tue et détruise leur planète.")
drop(S, "Qui est le premier ennemi que Gohan bat seul dans Dragon Ball Z ?")
drop(S, "Comment se nomme la grande sphère d'énergie vitale que Goku concentre en la demandant à tous ?")   # doublon
drop(S, "Combien de Dragon Balls namekiennes permettent de formuler des vœux ?")           # doublon
drop(S, "Combien de temps Goku court-il sur la Route Snake pour atteindre le Roi Kaio ?")
drop(S, "Comment s'appelle la fusion danse que Goten et Trunks apprennent ?")
fix(S, "Qui est la mère de Bra, la fille de Végéta ?",
    fb="Bra est la fille de Végéta et Bulma. Elle naît après la défaite de Boo.")
drop(S, "Quel est le nom de l'attaque finale utilisée par Gohan en SSJ2 contre Cell ?")     # doublon
drop(S, "Quel est le niveau de combat de Freezer en forme finale selon les données officielles ?")
drop(S, "Quelle transformation Trunks du futur atteint-il seul dans sa timeline ?")
drop(S, "Qui entraîne Goten et Trunks dans la Chambre d'Esprit pour créer Gotenks ?")
drop(S, "Combien de transformations Super Saiyajin existent dans Dragon Ball Super (hors GT) ?")
fix(S, "Quelle est la première transformation de Végéta lors du combat contre Goku sur Terre ?",
    fb="Végéta crée lui-même une lune artificielle pour se changer en singe géant (Oozaru). Yajirobe finit par lui trancher la queue.")
fix(S, "Quel humain de Dragon Ball Z possède un troisième œil et maîtrise des techniques de Ki ultra-concentré ?",
    fb="Ten Shin Han, ancien élève de l'école de la Grue, maîtrise des techniques redoutables comme le Kikoho.")


# ---------------------------------------------------------------- L'Attaque des Titans
S = 'aot'
fix(S, "Quel Titan détruit le mur Maria au début de la série ?",
    q="Quel Titan apparaît au-dessus du mur et défonce la porte de Shiganshina au début de la série ?",
    fb="Le Titan Colossal surgit au-dessus du mur et brise la porte d'un coup de pied. On apprendra plus tard qu'il s'agit de Bertolt Hoover, infiltré parmi les recrues.")
fix(S, "Qui est Zeke Yeager et quel Titan porte-t-il ?",
    fb="Zeke Yeager est le demi-frère d'Eren, fils de Grisha et de Dina Fritz. Porteur du Titan Bête et guerrier de Marley, il possède le sang royal.")
drop(S, "Comment Eren active-t-il le Titan Fondateur malgré sa lignée non royale ?")          # doublon
drop(S, "Comment Eren active-t-il le Titan Fondateur sans sang royal initialement ?")         # doublon
fix(S, "Comment Eren parvient-il à déclencher le Titan Fondateur pour la première fois lors de Shiganshina ?",
    q="Comment Eren déclenche-t-il le pouvoir du Titan Fondateur pour la première fois, à la fin de la saison 2 ?",
    fb="En frappant la main du Titan Souriant, devenu Titan pur, Eren entre en contact avec Dina Fritz, de sang royal. Ce contact lui permet un bref instant de commander les Titans.")
fix(S, "Pourquoi Sasha Blouse est-elle surnommée 'la fille à la pomme de terre' ?",
    q="Que fait Sasha Blouse devant l'instructeur Shadis lors du premier jour d'entraînement ?",
    a=["Elle mange une pomme de terre", "Elle s'endort debout", "Elle se met à chanter", "Elle s'enfuit en courant"], c=0)
drop(S, "Pourquoi Sasha Blouse mange-t-elle une pomme de terre pendant les exercices militaires ?")
fix(S, "Quel est le vrai Titan que porte Historia Reiss dans sa famille ?",
    q="Quel Titan possédait Frieda Reiss, la demi-sœur d'Historia ?",
    a=["Titan Fondateur", "Titan Féminin", "Titan Assaillant", "Titan Bête"], c=0)
drop(S, "Quel Titan de Puissance porte Pieck Finger ?")
drop(S, "Quelle est la capacité distinctive du Titan Char (Pieck Finger) comparé aux autres Titans de Puissance ?")
drop(S, "Quel est le vrai lien entre Levi Ackermann et Kenny Ackermann ?")
drop(S, "Quel est le nom de l'organisation secrète qui détient le vrai pouvoir royal ?")
drop(S, "Quel est le résultat de la coalition finale contre le Grondement d'Eren ?")
drop(S, "Quelle est la hauteur des murs protégeant l'humanité dans AOT ?")
drop(S, "Quel est le nom du camp d'entraînement où Eren et ses amis deviennent soldats ?")
drop(S, "Quelle institution entraîne les soldats à Paradis avant qu'ils choisissent leur corps ?")
fix(S, "Qui est la première Titanomane humaine de l'histoire selon la légende ?",
    q="Qui est la première humaine à avoir obtenu le pouvoir des Titans ?",
    fb="Ymir Fritz est la première à obtenir le pouvoir des Titans, il y a environ 2000 ans. Selon la légende, elle aurait passé un pacte avec le « diable de la Terre ».")
drop(S, "Comment le clan Ackermann accède-t-il à ses capacités surhumaines ?")
drop(S, "Quel est le nom du plan kamikaze d'Erwin lors de la bataille de Shiganshina ?")
drop(S, "Quelle technique permet aux soldats de cibler la nuque des Titans ?")
fix(S, "Quelle technique les soldats utilisent-ils pour tuer un Titan ?",
    fb="Le seul moyen de tuer un Titan est de lui trancher la nuque, là où se trouve son point vital. L'équipement tridimensionnel permet d'atteindre cette zone.")
drop(S, "Quel est le rang militaire de Levi dans le Corps d'Exploration ?")
drop(S, "Quelle est la Malédiction de Ymir qui limite les porteurs de Titans ?")
drop(S, "Quel Titan de Puissance Ymir (l'étudiante) possède-t-elle ?")
fix(S, "Quel Titan de Puissance Ymir l'étudiante possède-t-elle et comment l'a-t-elle obtenu ?",
    fb="Ymir, alors Titan pur, a dévoré Marcel Galliard, un guerrier de Marley, et hérité ainsi du Titan Mâchoire. Ce Titan est petit mais très agile.")
drop(S, "Comment s'appelle la mesure qui interdit aux civils de quitter les villes vers l'extérieur ?")
fix(S, "Quel ennemi est capable de transformer les Eldiens de Paradis en Titans d'un cri ?",
    a=["Eren Yeager (Titan Fondateur)", "Zeke Yeager (Titan Bête)", "Pieck Finger", "Reiner Braun"], c=1,
    fb="Zeke Yeager, de sang royal, peut transformer d'un cri en Titans purs les Eldiens qui ont ingéré son liquide céphalo-rachidien.")
drop(S, "Quelle nation fictive inspirée du Japon cherche à exploiter les ressources de Paradis ?")
fix(S, "Quel pays fictif est l'équivalent du Japon dans l'univers AOT ?",
    fb="Hizuru est une nation inspirée du Japon. Le clan Azumabito, dont descend Mikasa par sa mère, représente ses intérêts.")
drop(S, "Quel est le prénom du père de Mikasa dont on apprend l'histoire tragique ?")
drop(S, "Quel est le plan final d'Eren déclenché dans l'arc final ?")
drop(S, "Que fait Armin pour sauver ses amis lors de l'attaque de Trost en saison 1 ?")
drop(S, "Quel démon selon la légende a donné son pouvoir à Ymir Fritz il y a 2000 ans ?")
fix(S, "Quel personnage féminin du Corps d'Exploration est passionnée par l'étude des Titans ?",
    q="Quel membre du Corps d'exploration est passionné par l'étude des Titans ?",
    fb="Hange Zoë étudie les Titans avec une passion débordante et fait des découvertes essentielles sur leur nature. Hange devient plus tard commandant du Corps d'exploration.")
drop(S, "Comment s'appellent les deux frères qui ont fondé leur propre groupe après Marley ?")
drop(S, "Quel est le résultat du combat d'Armin contre Bertolt (Titan Colossal) à Shiganshina ?")
drop(S, "Comment Levi survit-il à l'explosion de la grenade Thunder Spear ?")
drop(S, "Quel district est détruit en premier lors de l'invasion initiale ?")
fix(S, "Qu'est-ce que la Résistance Eldienne qui s'oppose à Marley ?",
    fb="Les Restaurationnistes d'Eldia sont des Eldiens du continent, vivant notamment à Liberio, qui rêvent de libérer leur peuple. Grisha Yeager en faisait partie avant d'être capturé et envoyé sur Paradis.")
fix(S, "Qui succède à Erwin Smith comme commandant du Corps d'Exploration ?",
    fb="Après la mort d'Erwin, Hange Zoë prend la tête du Corps d'exploration.")
drop(S, "Quel est le plan de Zeke pour mettre fin à la malédiction des Eldiens ?")
fix(S, "Comment la Titanomanie se transmet-elle d'un porteur à l'autre ?",
    q="Comment un Titan de Puissance passe-t-il d'un porteur à l'autre ?")
drop(S, "Quel pays de l'arc final possède des chars et dirigeables militaires avancés ?")
fix(S, "Que révèle l'histoire de Ymir Fritz sur l'origine des pouvoirs des Titans ?",
    a=["Elle était une déesse", "Elle est entrée en contact avec une mystérieuse créature au creux d'un arbre géant", "Elle l'a volé à un dieu", "Elle a créé les Titans pour se venger"], c=1,
    fb="Ymir Fritz, esclave poursuivie, tombe au creux d'un arbre géant où une étrange créature fusionne avec elle. À sa mort, le roi Fritz force ses filles à manger son corps pour perpétuer le pouvoir.")
fix(S, "Comment Historia devient-elle officiellement reine de Paradis ?",
    a=["Par héritage automatique", "Elle est couronnée après le coup d'État du Corps d'exploration", "Par vote populaire", "Eren la force à régner"], c=1,
    fb="Après le renversement du faux roi par le Corps d'exploration, Historia, héritière de la famille Reiss, est couronnée reine.")
fix(S, "Quel est le nom de la forteresse Marleyenne la plus redoutable à l'est du continent ?",
    q="Quelle forteresse de l'Alliance du Moyen-Orient Marley assiège-t-elle au début de la saison 4 ?",
    a=["Fort Slava", "Fort Reiss", "Fort Salta", "Fort Liberio"], c=0,
    fb="Le fort Slava est la place forte de l'Alliance du Moyen-Orient. Marley ne la prend qu'en engageant ses Titans, ce qui convainc ses dirigeants que leur avantage militaire touche à sa fin.")
drop(S, "Quel est le prénom de la petite fille qui court dans les mémoires d'Eren et représente l'avenir ?")


# ---------------------------------------------------------------- My Hero Academia
S = 'mha'
fix(S, "Qui est le héros numéro 1 au début de la série ?", a=["Endeavor", "Hawks", "Edgeshot", "All Might"], c=3,
    fb="All Might (Toshinori Yagi) est le héros numéro 1 du Japon et le « Symbole de la Paix ». Il doit se retirer après avoir épuisé ses forces contre All For One.")
fix(S, "Dans quelle école Deku est-il inscrit ?",
    fb="U.A. (Yuei) est l'école de héros la plus prestigieuse du Japon. Deku y entre en section Héros, dans la classe 1-A.")
fix(S, "Quel est le Quirk de Shota Aizawa (Eraserhead) ?",
    fb="Erasure (Effacement) annule le Quirk de la personne qu'Aizawa fixe du regard. L'effet cesse dès qu'il cligne des yeux.")
drop(S, "Quel est le Quirk d'Ochaco Uraraka ?")                 # doublons
drop(S, "Comment s'appelle le Quirk d'Ochaco Uraraka ?")
drop(S, "Quel est le rang le plus élevé dans le classement des héros de la Hero Association ?")   # One Punch Man
drop(S, "Quel héros de Rang S a une puissance psychique de niveau S et est numéro 2 ?")            # One Punch Man
drop(S, "Quel héros de Rang S de MHA utilise la technique Nejire Wave et est l'une des Big Three de U.A. ?")
drop(S, "Comment Deku déclenche-t-il involontairement Blackwhip lors du tournament ?")
fix(S, "Quel est le nom de l'attaque finale d'Izuku Midoriya utilisant tous ses membres ?",
    q="Quelle attaque All Might utilise-t-il pour vaincre All For One à Kamino ?",
    a=["100% Detroit Smash", "Texas Smash", "United States of Smash", "Delaware Smash"], c=2,
    fb="United States of Smash est le dernier coup d'All Might, porté à Kamino pour vaincre All For One. Ce combat épuise définitivement ses forces.")
fix(S, "Quel examen donne aux lycéens le droit d'agir en héros dans des situations réelles ?",
    q="Quel examen Bakugo et Todoroki ratent-ils lors de la saison 3 ?",
    a=["L'examen d'entrée de U.A.", "L'examen de licence provisoire", "L'examen de fin de semestre", "Le Festival sportif"], c=1,
    fb="Bakugo et Todoroki échouent à l'examen de licence provisoire de héros, à cause de leur comportement. Ils doivent suivre des cours de rattrapage pour l'obtenir.")
drop(S, "Quel est le premier vrai combat héroïque de Deku contre un villain ?")
drop(S, "Quel est le premier combat héroïque réel de Deku face à une vraie menace ?")
drop(S, "Quel est le lien entre Midoriya et le 9ème porteur de One For All ?")
fix(S, "Quel héros enseigne à Deku à utiliser One For All à 5% puis 8% ?",
    q="Quel héros apprend à Deku à répartir One For All dans tout son corps ?",
    fb="Gran Torino, l'ancien professeur d'All Might, apprend à Deku à répartir une petite part de One For All dans tout son corps pour ne plus se briser les membres.")
drop(S, "Quel est le vrai nom d'Eraserhead ?")
drop(S, "Quel est le nom du Quirk de Mr. Compress, qui lui permet de miniaturiser tout ce qu'il touche ?")
drop(S, "Quel Quirk de Kirishima lui permet de durcir son corps comme du roc ?")
drop(S, "Quel est le Quirk d'Eijiro Kirishima (Red Riot) ?")
drop(S, "Combien de membres compte la classe 1-A de U.A. ?")
fix(S, "Combien d'étudiants composent la classe 1-A de U.A. ?",
    fb="La classe 1-A compte 20 élèves, chacun doté d'un Quirk différent.")
fix(S, "Qui sont les créateurs de All For One et One For All selon l'histoire ?",
    q="Quel lien unit All For One et le premier porteur de One For All ?",
    a=["Ce sont deux frères", "Ce sont un père et son fils", "Ils étaient camarades d'école", "Aucun lien"], c=0,
    fb="Le premier porteur, Yoichi, est le petit frère d'All For One. Celui-ci lui a imposé un Quirk de stockage de puissance, qui a fusionné avec le Quirk de transmission caché de Yoichi pour donner One For All.")
drop(S, "Quel est le nombre de Quirks hérités dans One For All que Deku peut éventuellement utiliser ?")
drop(S, "Quel nombre maximum de porteurs One For All peut théoriquement utiliser en même temps ?")
drop(S, "Quel héros Pro enseigne aux étudiants lors du stage de travail avec Endeavor ?")
fix(S, "Qui forme le groupe de vilains qui attaque le camp d'entraînement en saison 3 ?",
    q="Quel groupe attaque le camp d'été de la classe 1-A pour enlever Bakugo ?",
    a=["Shigaraki seul", "L'Avant-garde de la Ligue (Vanguard Action Squad)", "Overhaul et ses yakuzas", "Les élèves de Shiketsu"], c=1)
drop(S, "Comment s'appelle la devise de Gran Torino pour apprendre à Deku à distribuer OFA ?")
drop(S, "Comment s'appelle le mouvement de combat que Deku invente en mélangeant Blackwhip et ses coups ?")
fix(S, "Quel est le nom du groupe terroriste de Re-Destro dans MHA ?",
    a=["Meta Liberation Army", "Hero Killers", "Quirk Freedom Front", "Shie Hassaikai"], c=0,
    fb="La Meta Liberation Army de Re-Destro prône la liberté totale d'utiliser les Quirks. Vaincue par la Ligue des Vilains, elle fusionne avec elle pour former le Paranormal Liberation Front.")
drop(S, "Quel est le vrai nom civil d'All Might, révélé progressivement à Midoriya ?")
fix(S, "Qui est le premier villain majeur de la saison 1 à attaquer les étudiants ?",
    fb="Tomura Shigaraki mène l'attaque de l'USJ en saison 1 avec Kurogiri et le Nomu. Son but est de tuer All Might.")
drop(S, "Quel est le lien entre Dabi et la famille Todoroki ?")
fix(S, "Comment s'appelle la technique de Todoroki qui combines les deux côtés de son Quirk ?",
    q="Comment s'appelle la technique de Todoroki qui combine la glace et le feu ?")
drop(S, "Qui est le premier ennemi que Deku bat en utilisant son Quirk sans se casser un membre ?")
fix(S, "Quel événement déclenche la transformation de Shigaraki en super-vilain ?",
    fb="Enfant, Tenko Shimura voit son Quirk s'éveiller et désintègre sa famille. All For One le recueille ensuite et nourrit sa haine des héros.")
fix(S, "Quel est le nom complet de l'association qui finance les héros dans MHA ?",
    q="Quel organisme gouvernemental encadre les héros professionnels et a formé Hawks depuis l'enfance ?",
    a=["La Hero Association", "Le Registre des héros", "La Commission de sécurité publique des héros", "Le Bureau national des héros"], c=2,
    fb="La Commission de sécurité publique des héros encadre les héros professionnels. On découvre qu'elle a élevé et formé Hawks dès l'enfance pour en faire un agent.")
fix(S, "Quel Quirk permet à Mirko (Rumi Usagiyama) de sauter et frapper comme un lapin ?",
    fb="Rabbit donne à Mirko les capacités d'un lapin, dont des sauts et des coups de pied dévastateurs. Elle est la 5e héroïne du classement et préfère combattre seule.")
fix(S, "Comment s'appelle l'arc où la Yakuza Shie Hassaikai kidnappe Eri ?",
    q="Dans quel arc Deku et Mirio affrontent-ils Overhaul pour sauver Eri ?",
    a=["Arc du camp d'été", "Arc Shie Hassaikai", "Arc de l'USJ", "Arc du Festival sportif"], c=1)
drop(S, "Quel est le pourcentage de OFA que Deku utilise pour la première fois sans se blesser ?")
fix(S, "Quel villain de la Ligue peut dupliquer n'importe qui mais souffre de dissociation identitaire ?",
    fb="Twice (Jin Bubaigawara) peut créer des doubles de n'importe qui. Hanté par un passé où ses propres clones se sont entretués, il doute sans cesse d'être l'original. Il est tué par Hawks.")
fix(S, "Quel est le nom de la reine des Nomu créée par All For One comme arme ultime ?",
    q="Comment appelle-t-on les Nomu évolués, capables de réfléchir et de parler, comme Hood ?",
    a=["Nomu Suprêmes", "High-End Nomu", "Gigantomachia", "Nomu Alpha"], c=1)
fix(S, "Quel est l'arc de la saison 6 MHA impliquant une guerre massive entre héros et villains ?",
    fb="La guerre du Paranormal Liberation Front ouvre la saison 6 : les héros attaquent à la fois la base du Front et l'hôpital de Jaku, où Shigaraki est en train d'être modifié.")
drop(S, "Quel est le Quirk hérité que Deku maîtrise en 2ème (après Blackwhip) ?")


# ---------------------------------------------------------------- Fullmetal Alchemist Brotherhood
S = 'fmab'
fix(S, "Quel est le principe fondamental de l'alchimie dans FMA Brotherhood ?",
    a=["Plus tu donnes, plus tu reçois", "Pour obtenir, il faut sacrifier quelque chose de valeur égale", "L'alchimie est sans limites", "Le sang est la monnaie de l'alchimie"], c=1)
fix(S, "Comment s'appelle l'alchimiste frère aîné des Elric ?", q="Lequel des frères Elric est l'aîné ?",
    fb="Edward Elric est l'aîné et l'Alchimiste d'État surnommé FullMetal. Il perd une jambe puis un bras lors de la transmutation humaine ratée et déteste qu'on le traite de petit.")
fix(S, "Qui est le Père des Homuncules dans FMA Brotherhood ?",
    fb="Le Père est né à Xerxès, il y a plus de 400 ans, du sang de Hohenheim dans un flacon. Son objectif est d'absorber « Dieu » en sacrifiant la population d'Amestris.")
fix(S, "Comment s'appelle la prothèse mécanique d'Edward ?",
    fb="L'automail est une prothèse mécanique reliée aux nerfs. C'est Winry Rockbell qui fabrique et entretient celles d'Edward.")
fix(S, "Qui est Winry Rockbell dans la série ?",
    a=["La sœur des Elric", "La mécanicienne automail des Elric", "Une Alchimiste d'État", "La sœur de Roy Mustang"], c=1,
    fb="Winry Rockbell est l'amie d'enfance des Elric et leur mécanicienne. Petite-fille de Pinako Rockbell, elle fabrique et répare les automails d'Edward.")
drop(S, "Quel pays oriental possède une alchimie appelée Alkahestrie focalisée sur le Ki ?")
drop(S, "Quel homonyme désigne la technique qui transmute les blessures et maladies ?")
drop(S, "Comment s'appelle la technique que les Namekiens de Xing utilisent pour guérir les corps ?")
fix(S, "Qui est Ling Yao dans la série ?",
    a=["Un Alchimiste d'État de Xing", "Un prince de Xing venu chercher l'immortalité", "Le chef de la police de Central", "Un espion ishvalan"], c=1)
fix(S, "Quel est le sacrifice final d'Edward pour ramener le corps d'Alphonse ?",
    fb="Edward renonce à sa propre Porte de la Vérité, et donc à l'alchimie pour toujours, afin de ramener son frère, corps et âme.")
drop(S, "Quel est le sacrifice final d'Edward pour ramener Al ?")
fix(S, "Quelle est la particularité de Van Hohenheim, le père des Elric ?",
    fb="Van Hohenheim porte en lui des centaines de milliers d'âmes de Xerxès. Il ne vieillit pas et peut pratiquer l'alchimie sans cercle.")
fix(S, "Quel homuncule représente la Luxure ?",
    fb="Lust peut allonger ses ongles en lames tranchantes. Roy Mustang la tue après avoir cautérisé sa propre blessure avec ses flammes.")
fix(S, "Qui est Scar et pourquoi tue-t-il des Alchimistes d'État ?",
    fb="Scar est un survivant ishvalan. Son bras droit porte les tatouages alchimiques de son frère défunt, et il s'en sert pour tuer les Alchimistes d'État, responsables du massacre de son peuple.")
drop(S, "Comment Mustang combat-il Pride sans ses gants dans le combat final ?")
drop(S, "Comment Alphonse parvient-il à regagner son corps à la fin ?")      # faux : c'est Edward qui renonce à l'alchimie
drop(S, "Comment Al retrouve-t-il finalement son corps original ?")
drop(S, "Quel est l'équivalent échange payé par Alphonse pour récupérer son corps à la fin ?")
drop(S, "Comment Ed appelle-t-il Roy Mustang pour le charrier ?")
drop(S, "Comment Ed appelle-t-il souvent Mustang pour le provoquer ?")
drop(S, "Comment Ed surnomme-t-il Roy Mustang pour le charrier en permanence ?")
fix(S, "Quel est le prix que Edward a payé lors de la transmutation humaine ratée ?",
    q="Quels membres Edward perd-il en tentant de ressusciter sa mère ?",
    fb="Edward perd sa jambe gauche lors de la transmutation, puis sacrifie son bras droit pour fixer l'âme d'Alphonse dans une armure.")
drop(S, "Quel est le prix payé par Edward lors de la transmutation humaine ?")
drop(S, "Qui est l'alchimiste surnommée 'Izumi Curtis' et quel est son rôle ?")
drop(S, "Quel nom porte l'homuncule de la Convoitise ?")
drop(S, "Quelle est la technique défensive de Greed ?")
drop(S, "Quelle est la capacité défensive ultime de Greed dans FMA Brotherhood ?")
drop(S, "Quel est le vrai nom de l'homuncule Greed et dans quel corps évolue-t-il en saison 2 ?")
drop(S, "Qui est le général Armstrong qui dirige Fort Briggs ?")
drop(S, "Qui est le général qui dirige Fort Briggs, la forteresse du nord d'Amestris ?")
fix(S, "Quel général féminin dirige Fort Briggs dans le nord d'Amestris ?",
    fb="Olivier Mira Armstrong, sœur aînée d'Alex, commande la forteresse de Briggs d'une main de fer. Pour elle, seuls les forts survivent.")
drop(S, "Quelle ville est sacrifiée dans le plan du Père pour créer le Cercle National ?")
drop(S, "Quelle ville est sacrifiée par le Père il y a 400 ans pour créer le premier Cercle de Transmutation ?")
fix(S, "Comment s'appelle la grande ville sacrifiée par le Père il y a 400 ans pour créer la première Pierre ?",
    fb="Il y a environ 400 ans, le Père manipule le roi de Xerxès pour tracer un immense cercle de transmutation qui sacrifie tout le peuple. Seuls lui et Hohenheim y survivent.")
drop(S, "Quel est le Quirk de Riza Hawkeye dans l'alchimie ?")
drop(S, "Comment s'appelle le tatouage alchimique sur le dos de Riza Hawkeye ?")
fix(S, "Quel est le symbole alchimique tatoué dans le dos de Riza Hawkeye ?",
    q="Que porte Riza Hawkeye tatoué dans son dos ?",
    fb="Le dos de Riza porte les recherches de son père, Berthold Hawkeye, sur l'alchimie des flammes. Elle demandera plus tard à Mustang de brûler ce tatouage pour que personne d'autre ne s'en serve.")
drop(S, "Comment la Pierre Philosophale permet-elle de contourner la Loi d'Équivalent Échange ?")
fix(S, "Quel est le nom de l'homuncule de la Paresse qui creuse des tunnels sous Amestris ?",
    fb="Sloth, l'homuncule de la Paresse, creuse pendant des années l'immense tunnel qui dessine le cercle de transmutation national sous Amestris.")
fix(S, "Comment Riza Hawkeye protège-t-elle Mustang dans la bataille finale contre le Père ?",
    fb="Rendu aveugle par la transmutation humaine forcée, Mustang ne voit plus. Riza lui indique la position de l'ennemi pour qu'il puisse viser avec ses flammes.")
fix(S, "Quel est le Quirk alchimique particulier de Kimblee l'Alchimiste Cramoisi ?",
    q="Quelle est l'alchimie particulière de Solf J. Kimblee, l'Alchimiste Écarlate ?",
    fb="Kimblee transmute ce qu'il touche en explosif, y compris le corps de ses victimes. Son goût pour la destruction en fait l'un des personnages les plus inquiétants de la série.")
drop(S, "Comment Alphonse découvre-t-il qu'il est une Pierre Philosophale vivante ?")
fix(S, "Comment s'appelle la grand-mère de Winry, experte en automail et soignante à Resembool ?",
    q="Comment s'appelle la grand-mère de Winry, mécanicienne d'automail à Resembool ?",
    fb="Pinako Rockbell est la grand-mère de Winry et une mécanicienne d'automail réputée. C'est elle qui pose les premières prothèses d'Edward.")
drop(S, "Quel est le vrai buts des Alchimistes d'État selon la révélation finale ?")
fix(S, "Comment Scar parvient-il à blesser les Alchimistes d'État malgré leurs défenses ?",
    q="Quel est le pouvoir du bras droit de Scar ?",
    a=["Il crée des flammes", "Il décompose la matière qu'il touche", "Il absorbe l'alchimie adverse", "Il pétrifie ses ennemis"], c=1,
    fb="Le bras droit de Scar, tatoué par son frère, décompose la matière au toucher. Il s'en sert pour tuer ses victimes d'un seul geste.")
drop(S, "Quelle technique alchimique Scar développe-t-il en combinant ses deux bras ?")
fix(S, "Que se passe-t-il quand Mustang tue Envy ?",
    q="Comment finit Envy après avoir été vaincu par Mustang ?",
    a=["Mustang le laisse partir", "Il se donne la mort après qu'Edward a compris sa jalousie envers les humains", "Il est absorbé par le Père", "Il s'enfuit dans un autre corps"], c=1,
    fb="Réduit à sa forme minuscule, Envy est démasqué par Edward : il envie les humains. Humilié, il pleure puis met fin à ses jours.")
drop(S, "Quelle est la relation finale entre Ling Yao et Greed à la fin de la série ?")
drop(S, "Comment s'appelle la manifestation de Pride quand il utilise ses ombres ?")
drop(S, "Quelle décision morale déchirante Roy Mustang doit-il prendre lors de la montée vers le Père ?")
fix(S, "Que tente de créer Edward et Alphonse lors de leur transmutation humaine ratée ?",
    q="Qui Edward et Alphonse tentent-ils de ressusciter par la transmutation humaine ?",
    a=["Leur père Hohenheim", "Leur mère Trisha", "Leur maîtresse Izumi", "Leur grand-mère"], c=1,
    fb="Les frères tentent de ressusciter leur mère, Trisha. La transmutation échoue : Edward perd une jambe, Alphonse son corps entier, et ils n'obtiennent qu'une créature informe.")
drop(S, "Pourquoi les Alchimistes d'État sont-ils surnommés Chiens de l'État ?")
fix(S, "Quel est le résultat de la confrontation finale entre Edward et le Père ?",
    a=["Le Père s'échappe", "Vaincu par Edward, le Père est emporté par la Vérité derrière sa Porte", "Alphonse sacrifie sa vie", "Mustang tue le Père"], c=1,
    fb="Affaibli, le Père est battu à mains nues par Edward. La Vérité l'attire alors derrière sa propre Porte, lui qui voulait dépasser Dieu.")
fix(S, "Quel alchimiste d'État est surnommé le Bras Fort de Briggs ?",
    q="Quel Alchimiste d'État est surnommé l'Alchimiste au Bras puissant ?",
    fb="Alex Louis Armstrong est l'Alchimiste au Bras puissant. Ses techniques se transmettent dans la famille Armstrong depuis des générations.")
fix(S, "Quel est le crime commis par le Dr Marcoh que Scar finit par pardonner ?",
    q="Quel lourd secret le docteur Marcoh porte-t-il ?",
    fb="Pendant la guerre d'Ishval, le docteur Marcoh a fabriqué des Pierres philosophales sur ordre de l'armée. Rongé par la culpabilité, il a fui et vit caché.")


# ---------------------------------------------------------------- Jujutsu Kaisen
S = 'jjk'
fix(S, "Qui est Ryomen Sukuna ?",
    fb="Ryomen Sukuna est un sorcier de l'ère Heian, il y a plus de mille ans, si redoutable qu'on l'appelle le Roi des Fléaux. Ses vingt doigts sont devenus des objets maudits indestructibles.")
fix(S, "Qui est Kenjaku et quel est son Quirk ?", q="Qui est Kenjaku ?",
    fb="Kenjaku est un sorcier millénaire qui change de corps en y transplantant son cerveau. Il occupe le corps de Suguru Geto et a jadis occupé celui de la mère de Yuji.")
fix(S, "Quel est le Quirk de Mahito ?", q="Quelle est la technique de Mahito ?")
fix(S, "Qu'est-ce que le Black Flash dans JJK ?",
    fb="Le Black Flash survient quand l'énergie maudite frappe moins d'un millionième de seconde après le coup physique. L'espace se déforme et la puissance du coup est élevée à 2,5.")
drop(S, "Qu'est-ce que le Black Flash et quel effet a-t-il sur la puissance ?")
fix(S, "Qui est Toji Fushiguro et quel est son lien avec Megumi ?",
    fb="Toji Fushiguro est le père de Megumi. Né sans énergie maudite à cause d'une Restriction céleste, il a un corps surhumain. Ce tueur à gages avait promis de céder Megumi au clan Zenin.")
fix(S, "Quel est le Quirk de Nobara Kugisaki ?", q="Quelle est la technique de Nobara Kugisaki ?")
drop(S, "Comment s'appelle la technique de Gojo basée sur l'infini ?")
fix(S, "Quel est le nom de la technique de Gojo qui rend ses attaques infinies à l'approche ?",
    q="Comment s'appelle la barrière invisible de Gojo qui ralentit sans fin tout ce qui l'approche ?",
    fb="L'Infini est une application de la technique Limitless : tout ce qui s'approche de Gojo ralentit sans jamais l'atteindre.")
drop(S, "Comment Yuji devient-il capable de blesser les malédictions sans Sukuna ?")
fix(S, "Quel sont les Vingt Doigts de Sukuna ?", q="Que sont les vingt doigts de Sukuna ?",
    fb="Les vingt doigts de Sukuna sont des objets maudits indestructibles qui contiennent chacun une partie de sa puissance. Yuji doit tous les avaler avant d'être exécuté.")
drop(S, "Quel est le nom du lycée Jujutsu de Tokyo ?")
drop(S, "Quelle technique Todo enseigne-t-il à Yuji ?")
fix(S, "Comment s'appelle la technique d'Aoi Todo qui échange les positions ?",
    fb="Boogie Woogie permet à Todo d'échanger la position de deux cibles en frappant dans ses mains. Avec Yuji, il s'en sert pour déstabiliser Hanami puis Mahito.")
drop(S, "Qu'est-ce que le Culling Game institué par Kenjaku ?")
drop(S, "Quel est le vrai objectif de Kenjaku avec le Culling Game ?")
fix(S, "Quel est le Culling Game lancé par Kenjaku dans l'arc final ?",
    q="Qu'est-ce que le Culling Game lancé par Kenjaku ?",
    fb="Le Culling Game enferme des sorciers éveillés et des sorciers anciens réincarnés dans des colonies où ils doivent s'affronter selon des règles strictes.")
drop(S, "Quel est le grade de Yuji Itadori selon la Hero Association de JJK ?")
drop(S, "Comment Yuji est-il officiellement classé dans le monde du Jujutsu au début ?")
drop(S, "Quel grade Yuji Itadori reçoit-il officiellement de l'Association Jujutsu ?")
drop(S, "Comment s'appelle la technique héréditaire de Naoya Zenin qui divise ses mouvements en 24 frames ?")
fix(S, "Qui a fondé le Tokyo Metropolitan Curse Technical College ?",
    q="Qui dirige l'école d'exorcisme de Tokyo au début de la série ?",
    fb="Masamichi Yaga dirige l'école de Tokyo. Il fabrique des cadavres maudits, des poupées animées, dont Panda est la plus aboutie.")
drop(S, "Quel est le domaine le plus puissant connu dans l'histoire du Jujutsu ?")
drop(S, "Quel est le nom de la technique ultime utilisée par Sukuna lors de la bataille finale ?")
drop(S, "Quel personnage de JJK utilise une lance comme arme principale ?")
fix(S, "Quelle est la caractéristique du Domaine 'Coffin of the Iron Mountain' de Choso ?",
    q="À qui appartient l'Extension du territoire « Cercueil de la Montagne de Fer » ?",
    a=["Choso", "Jogo", "Hanami", "Mahito"], c=1,
    fb="Le Cercueil de la Montagne de Fer est le territoire de Jogo, le fléau volcanique. Il enferme sa cible dans un monde de lave d'une chaleur insoutenable.")
drop(S, "Qui enseigne à Yuji à maintenir son âme stable face à Sukuna ?")
fix(S, "Qui est Yuki Tsukumo et quel est son rôle dans l'histoire ?",
    a=["Une ancienne élève de Tokyo devenue professeure", "Une sorcière de grade spécial qui cherche à faire disparaître les fléaux", "Une membre du conseil des anciens", "La mère de Megumi"], c=1,
    fb="Yuki Tsukumo est l'une des rares sorcières de grade spécial. Plutôt que d'exorciser les fléaux un par un, elle cherche un moyen d'en supprimer la source.")
drop(S, "Quelle est la différence entre un esprit maudit naturel et un outil maudit ?")
fix(S, "Qu'est-ce qu'un Outil Maudit (Cursed Tool) dans JJK ?",
    a=["Un sabre vivant", "Un objet imprégné d'énergie maudite", "Un objet possédé par un esprit", "Une arme volée à un sorcier"], c=1)
drop(S, "Quel clan JJK est l'équivalent aristocratique d'une des 'trois familles' ?")
drop(S, "Quel Clan JJK spécialisé dans la manipulation du sang est l'un des Trois Familles ?")
drop(S, "Comment Yuji résiste-t-il aux prises de contrôle de Sukuna ?")
fix(S, "Quel est le Domaine d'Expansion de Megumi Fushiguro ?",
    fb="Le Jardin des Ombres Chimères est l'Extension du territoire de Megumi : il y répand ses ombres et multiplie ses shikigami. Au début, ce territoire reste inachevé.")
drop(S, "Quel est le nom du Domaine de Megumi qui invoque toutes ses ombres simultanément ?")
drop(S, "Quel est le Domaine d'Expansion de Megumi Fushiguro dont l'invocation détruit les alentours ?")
drop(S, "Quel est le Quirk de Nanami Kento qui force les probabilités ?")
drop(S, "Qu'est-ce que le système de classement 4 à Grade Spécial en JJK ?")
fix(S, "Quel est le Quirk de Hiromi Higuruma, avocat devenu sorcier ?",
    q="Quelle est la technique de Hiromi Higuruma, avocat devenu sorcier ?",
    fb="Deadly Sentencing ouvre un tribunal où la cible est jugée. Si elle est déclarée coupable, Higuruma peut lui retirer sa technique, voire la condamner à mort avec son glaive d'exécuteur.")
fix(S, "Comment Sukuna prend-il le contrôle total du corps de Yuji lors de l'Incident de Shibuya ?",
    a=["Yuji s'endort", "On lui fait avaler dix doigts pendant qu'il est inconscient", "Sukuna brise un sceau", "Mahito l'aide"], c=1,
    fb="À Shibuya, deux disciples de Geto font avaler dix doigts à Yuji, inconscient. Sukuna se réveille alors et prend le contrôle de son corps.")
fix(S, "Qui est Panda parmi les personnages de JJK et quelle est sa nature ?",
    a=["Un humain qui se transforme", "Un cadavre maudit créé par le directeur Yaga", "Un vrai panda", "Un shikigami"], c=1,
    fb="Panda est un cadavre maudit doté d'une conscience, créé par Masamichi Yaga. Il possède trois noyaux, dont un de gorille, qui lui offrent plusieurs formes de combat.")
drop(S, "Quelle est la relation entre Choso et Yuji Itadori selon la révélation ?")
fix(S, "Qui est Choso et quel est son lien biologique avec Yuji Itadori ?",
    fb="Choso est un des Neuf Rouleaux de la mort, né d'une femme et d'un fléau, avec Kenjaku pour père. Yuji est né de Kenjaku dans le corps de sa mère : ils sont donc demi-frères.")
fix(S, "Comment Gojo est-il finalement libéré de la Prison Realm ?",
    a=["Il s'en échappe seul", "Grâce à la technique d'Angel (Hana Kurusu)", "Il ne sera jamais libéré", "Par une technique de Todo"], c=1,
    fb="La technique d'Angel, habitant le corps de Hana Kurusu, peut annuler les autres techniques. Elle sert à ouvrir la Prison Realm et à libérer Gojo.")
fix(S, "Qui est Hakari Kinji et quelle est sa technique de jeu ?",
    fb="Kinji Hakari est un élève de troisième année de Tokyo, suspendu. Sa technique fonctionne comme une machine de pachinko : au jackpot, il dispose d'une énergie maudite illimitée et se régénère automatiquement pendant un peu plus de quatre minutes.")
fix(S, "Pourquoi la mort de Nanami est-elle particulièrement marquante dans la série ?",
    a=["Il était le personnage principal", "Ses derniers mots confient la suite à Yuji avant que Mahito l'achève", "Il trahit ses alliés", "Il meurt en héros contre Sukuna"], c=1,
    fb="Grièvement brûlé à Shibuya, Nanami voit Yuji arriver et lui dit simplement que c'est à lui de jouer désormais. Mahito l'achève sous les yeux de Yuji.")
fix(S, "Qui est Maki Zenin et pourquoi est-elle exceptionnelle malgré l'absence d'énergie maudite ?",
    a=["Elle utilise des sorts", "Une Restriction céleste lui donne un corps surhumain", "Elle vole l'énergie des autres", "Elle est un shikigami"], c=1,
    fb="Maki est née avec une Restriction céleste : presque pas d'énergie maudite, mais un corps hors norme. Après la mort de sa sœur Mai, sa restriction devient totale et elle atteint le niveau de Toji.")
fix(S, "Quel est le nom de la technique de Yuji qui ressemble au Black Flash répété ?",
    q="Comment s'appelle le coup de Yuji dont l'énergie maudite frappe juste après l'impact physique ?")
fix(S, "Pourquoi Gojo est-il considéré comme l'homme le plus puissant ?",
    a=["Il est immortel", "Ses Six Yeux et la technique Limitless", "Il a vaincu Sukuna", "Il a mangé des doigts de Sukuna"], c=1)
fix(S, "Quel est l'impact de l'Incident de Shibuya sur le statut de sorcier de Gojo ?",
    a=["Il monte en grade", "Il est déclaré complice et banni du monde du Jujutsu", "Il prend la tête du conseil", "Il n'y a pas d'impact"], c=1,
    fb="Après Shibuya, les dirigeants du monde du Jujutsu désignent Gojo comme complice de l'incident, le bannissent et interdisent sa libération.")
fix(S, "Que représente Mahoraga parmi les 10 Shikigami de Megumi ?",
    fb="Mahoraga, le Général divin, est le shikigami le plus puissant des Dix Ombres. Aucun utilisateur de cette technique n'a jamais réussi à le dompter, et il s'adapte à toute attaque.")
drop(S, "Quel est le nom de la technique qui permet à Yuji de voir les âmes des victimes de Mahito ?")
fix(S, "Quel clan JJK est réputé pour sa technique des dix ombres ?",
    fb="Les Dix Ombres sont une technique héréditaire du clan Zenin. Megumi, fils de Toji, en a hérité.")
drop(S, "Comment s'appelle le principal disciple de Gojo parmi les étudiants de Tokyo ?")
drop(S, "Quel événement catastrophique déclenche l'Arc de Shibuya ?")
drop(S, "Pourquoi Yuji est-il difficile à tuer malgré sa condamnation ?")
drop(S, "Quelle est la conséquence d'un pacte (serment) rompu dans JJK ?")
fix(S, "Qui est Suguru Geto et quel est son lien avec Gojo dans leur passé ?",
    fb="Suguru Geto était le meilleur ami de Gojo à l'école. Dégoûté par les humains ordinaires, il bascule après avoir massacré un village et devient un ennemi des sorciers.")
drop(S, "Quel est l'effet de la Prison Realm sur ceux qui y sont enfermés ?")
drop(S, "Comment s'appelle le shikigami le plus puissant de Megumi qui détruit tout, y compris son invocateur ?")


# ---------------------------------------------------------------- One Punch Man
S = 'onepunchman'
fix(S, "Comment s'appelle l'organisation qui classe et emploie les héros ?",
    fb="La Hero Association recrute, classe et envoie les héros professionnels. Elle a été fondée par le milliardaire Agoni après que son petit-fils a été sauvé par un homme chauve : Saitama.")
fix(S, "Quel est le vrai statut de King, soi-disant 'héros le plus fort' ?",
    a=["Il est réellement le plus fort", "Sa réputation est accidentelle : Saitama gagnait à sa place", "Il est un espion", "C'est un robot"], c=1)
fix(S, "Quel alien venu de l'espace cherchait un adversaire à sa hauteur ?",
    fb="Lord Boros parcourt l'univers à la recherche d'un adversaire digne de lui. Malgré son Meteoric Burst, Saitama le terrasse d'un Poing Sérieux.")
drop(S, "Quel est le phénomène qui survient quand Saitama frappe vraiment sérieusement ?")
drop(S, "Quel est le vrai nom de Saitama selon l'Association des Héros ?")
fix(S, "Qui est Garou et quelle est son idéologie ?",
    a=["Un héros qui aime les monstres", "Le Chasseur de héros, qui veut devenir le monstre absolu", "Un disciple de Saitama", "Un alien destructeur"], c=1,
    fb="Garou, le Chasseur de héros, est l'ancien disciple de Bang. Par sympathie pour les « méchants » des histoires, il veut devenir le monstre absolu et terrasser les héros.")
drop(S, "Quel est le niveau de menace attribué à Boros, l'alien du Vaisseau Sombre ?")
drop(S, "Quelle est la véritable puissance derrière la force de Mumen Rider, le héros sans capacités ?")
drop(S, "Quelle est la population de City Z, ville de résidence de Saitama ?")
fix(S, "Dans quelle ville vit Saitama ?", a=["Ville Z", "Ville A", "Ville O", "Ville M"], c=0)
drop(S, "Comment Garou évolue-t-il physiquement lors de ses combats ?")
drop(S, "Quel est le phénomène qui rend Garou si difficile à battre même pour des héros puissants ?")
fix(S, "Comment Garou évolue-t-il au fil de ses combats dans la Monster Association ?",
    fb="Garou progresse à chaque combat : son corps se transforme peu à peu, il guérit plus vite et devient plus fort à chaque épreuve.")
drop(S, "Quel est le créateur du Dr. Genus et de sa Maison de l'Évolution ?")
drop(S, "Pourquoi Saitama n'arrive-t-il pas à monter en rang rapidement ?")
drop(S, "Quel est le nom du groupe de monstres qui attaque la Hero Association ?")
drop(S, "Quel est le nom de la organisation d'assasins que Garou affronte lors de son arc ?")
fix(S, "Quel héros de Rang S est un ancien prisonnier capable de libérer ses ailes angéliques ?",
    q="Quel héros de rang S purge une peine de prison entre deux missions ?",
    fb="Puri-Puri Prisoner, 17e du rang S, sort de prison quand on a besoin de lui. Il combat avec une force brute impressionnante et son « Angel Style ».")
drop(S, "Quel est le héros qui garde toujours un territoire spécifique en quadrupède ?")
drop(S, "Quel scientifique de Rang S dirige le Meta Liberation Army ?")          # My Hero Academia
drop(S, "Pourquoi Child Emperor est-il en Rang S malgré son jeune âge ?")
fix(S, "Comment Child Emperor combat-il malgré son jeune âge ?",
    a=["Par la magie", "Par des gadgets et inventions technologiques", "Par sa puissance psychique", "Par un clone robotique"], c=1)
drop(S, "Quel est le nom de la technique de Bang avec ses bras aquatiques ?")
fix(S, "Quelle est la relation entre Bang et Garou au début de la série ?",
    a=["Ils sont ennemis jurés", "Garou était le disciple de Bang avant d'être expulsé", "Bang est le père de Garou", "Ils ne se connaissent pas"], c=1,
    fb="Garou était le disciple de Bang, expulsé du dojo après avoir blessé les autres élèves. Bang culpabilise de ne pas avoir su le remettre dans le droit chemin.")
drop(S, "Qui est Bang (Silver Fang) et quel lien a-t-il avec Garou ?")
drop(S, "Comment Atomic Samurai combat-il ses ennemis ?")
drop(S, "Quel monstre de Rang Dragon est le premier à vraiment menacer Saitama ?")
drop(S, "Quelle est la citation la plus connue de Saitama sur son entraînement ?")
drop(S, "Comment Genos se bat-il en l'absence de bras fonctionnels ?")
drop(S, "Comment s'appelle l'attaque finale de Metal Bat contre un monstre Dragon ?")
drop(S, "Quel héros de Rang S peut créer des obstacles géants avec son corps ?")
fix(S, "Quel héros de Rang S possède une défense de cristal capable de tout bloquer ?",
    q="Quel héros de rang S est réputé pour son corps d'une dureté extrême ?",
    fb="Superalloy Darkshine possède un corps d'une dureté hors du commun et une force colossale. Il fait partie des héros les plus puissants du rang S.")
fix(S, "Pourquoi Saitama décide-t-il de devenir héros au début de son histoire ?",
    a=["Pour la gloire", "Pour sauver le monde", "Juste pour le plaisir, comme passe-temps", "Pour venger sa famille"], c=2,
    fb="Saitama se présente lui-même comme « un héros pour le plaisir ». Cette motivation toute simple contraste avec les grands discours des autres héros.")
drop(S, "Quel est le classement actuel de Saitama en rang B après quelques aventures ?")
drop(S, "Quel héros de Rang S est l'unique humain ordinaire parmi eux selon les fans ?")
drop(S, "Quel est le vrai niveau de puissance de King quand il se bat réellement ?")
fix(S, "Quel est le signal sonore qui terrorise les monstres selon la légende de King ?",
    q="Comment appelle-t-on le bruit du cœur de King qui terrifie ses adversaires ?",
    a=["Le King Roar", "Le King Beat", "Le King Engine", "Le King Drum"], c=2,
    fb="Le « King Engine » est le battement de cœur de King, si fort quand il a peur que ses adversaires le prennent pour le signe d'une puissance terrible.")
drop(S, "Comment la Hero Association réagit-elle après les pertes lors de l'attaque de la Monster Association ?")
drop(S, "Quel ennemi de la Monster Association possède des pouvoirs solaires cosmiques ?")
drop(S, "Comment Fubuki maintient-elle son rang B numéro 1 malgré une puissance inférieure à sa sœur ?")
drop(S, "Comment Drive Knight, héros Rang S, différencie-t-il ses formes de combat ?")
drop(S, "Comment Saitama se sent-il quand il rencontre finalement quelqu'un qui lui résiste (Boros) ?")
drop(S, "Quel est l'unique combat où Saitama ressent quelque chose qui ressemble à de l'excitation ?")
drop(S, "Quel héros de Rang A affronte régulièrement Saitama pour tenter de le battre ?")
drop(S, "Quel monstre de la Monster Association peut modifier son échelle et se fondre dans les ombres ?")
drop(S, "Comment la Hero Association classe-t-elle les héros et qui vote pour les promotions ?")
drop(S, "Quelle est la faiblesse majeure de Genos dans les combats prolongés ?")
drop(S, "Qu'est-ce qui distingue l'arc Garou de tous les autres arcs de One Punch Man ?")
fix(S, "Quel héros de Rang S est célèbre pour ses cheveux noirs et son amour du combat brutal ?",
    q="Quel héros de rang S se bat avec une batte de baseball en métal ?")
drop(S, "Quelle est la limite de temps de la transformation Serious de Saitama selon la série ?")
fix(S, "Quel est le rang de Genos dans la Hero Association au début de la série ?",
    q="Dans quelle classe Genos est-il placé dès son examen d'entrée à la Hero Association ?",
    a=["Classe C", "Classe S", "Classe B", "Classe A"], c=1,
    fb="Genos est directement placé en classe S grâce à ses capacités de cyborg, alors que Saitama démarre tout en bas de la classe C.")
drop(S, "Quel est l'effet de la victoire de Saitama sur son moral et sa vie quotidienne ?")
drop(S, "Quel est le nom de la ville où Child Emperor est le héros attitré selon son profil ?")
fix(S, "Comment Saitama est-il officiellement recruté dans la Hero Association ?",
    a=["Par audition spéciale", "Par un examen avec une épreuve physique et une épreuve écrite", "Recommandé par Genos", "Il crée sa propre association"], c=1,
    fb="Saitama obtient la note maximale à l'épreuve physique, mais son résultat à l'épreuve écrite est si faible qu'il démarre en classe C.")


# ---------------------------------------------------------------- Bleach
S = 'bleach'
drop(S, "Comment s'appelle le monde des Soul Reapers ?")
drop(S, "Comment nomme-t-on le chef suprême commandant l'ensemble des 13 divisions des Soul Reapers dans Bleach ?")
fix(S, "Quel est le nom de la puissance cachée d'Ichigo liée à sa nature de Hollow ?",
    q="Que fait apparaître Ichigo sur son visage pour libérer sa puissance de Hollow ?",
    a=["Un bandeau", "Un masque de Hollow", "Un casque de Quincy", "Une cagoule"], c=1,
    fb="Ichigo peut faire surgir un masque de Hollow qui décuple sa puissance. Il doit d'abord apprendre à dompter le Hollow qui vit en lui.")
drop(S, "Qu'est-ce que l'Hogyoku créé par Urahara et Aizen indépendamment ?")
fix(S, "Quel est le lien entre Sosuke Aizen et Kisuke Urahara dans la création de l'Hogyoku ?",
    a=["Aizen l'a volé à Urahara", "Chacun a créé le sien, puis Aizen a réuni les deux", "Urahara a aidé Aizen", "Aizen l'a créé seul"], c=1,
    fb="Urahara et Aizen ont chacun créé un Hogyoku. Urahara avait caché le sien dans l'âme de Rukia ; Aizen le lui arrache et le réunit au sien.")
drop(S, "Quel est le nom du groupe de Soul Reapers qui ont acquis des pouvoirs de Hollow ?")
fix(S, "Quel est le nom du groupe de Soul Reapers avec des pouvoirs de Hollow ?",
    fb="Les Vizards sont d'anciens capitaines et lieutenants transformés par les expériences d'Aizen. Bannis par la Soul Society, ils portent des masques de Hollow.")
fix(S, "Quel est le Zanpakuto de l'ancien Capitaine Jushiro Ukitake ?",
    fb="Sogyo no Kotowari, le sabre double d'Ukitake, absorbe les attaques ennemies et les renvoie.")
drop(S, "Quel est l'arc final de Bleach connu sous son acronyme ?")
drop(S, "Quel est le nom de l'arc final de Bleach animé en haute qualité ?")
fix(S, "Qui est Yhwach et quelle est sa relation avec le Roi des Âmes ?", q="Qui est Yhwach ?")
drop(S, "Qui est Yhwach et quel est son lien avec le Roi des Âmes ?")
drop(S, "Comment Ichigo perd-il ses pouvoirs après avoir vaincu Aizen ?")
fix(S, "Quel personnage est le maître mystérieux d'Ichigo qui le guide ?",
    fb="Kisuke Urahara, ancien capitaine de la 12e division exilé de la Soul Society, tient une petite boutique à Karakura. C'est lui qui entraîne Ichigo avant son départ pour la Soul Society.")
drop(S, "Comment s'appelle la capacité d'un Soul Reaper de percevoir les esprits et créatures spirituelles ?")
drop(S, "Comment s'appelle la technique de sonification qui paralyse les cibles ?")
drop(S, "Quel Soul Reaper est surnommé 'le dieu de la mort' parmi ses pairs ?")
fix(S, "Quel capitaine de la Division 11 aime le combat plus que tout et combat sans Shikai délibérément ?",
    q="Quel capitaine de la 11e division ne vit que pour le combat ?",
    fb="Kenpachi Zaraki adore se battre. Il porte un cache-œil qui absorbe son énergie spirituelle pour rendre les combats plus longs et plus amusants.")
fix(S, "Quel est le Zanpakuto de Kenpachi Zaraki et sa particularité ?",
    a=["Il n'a pas de Zanpakuto", "Nozarashi, dont il n'apprend le nom que très tard", "Zenpachi", "Yachiru"], c=1,
    fb="Kenpachi a combattu des siècles sans connaître le nom de son sabre. Pendant la Guerre sanglante de mille ans, il entend enfin son nom, Nozarashi, et libère son Shikai puis son Bankai.")
drop(S, "Quelle est la véritable forme du Zanpakuto d'Ichigo révélée dans le TYBW ?")
fix(S, "Quelle est la forme finale de Zangetsu révélée dans le TYBW ?",
    fb="Après avoir découvert ses origines, Ichigo fait reforger son sabre : il obtient deux lames, une grande et une petite, à l'image de sa double nature.")
fix(S, "Qui est le Roi des Âmes protégé par Soul Society ?",
    a=["Yamamoto", "Yhwach", "Une entité scellée dans le Palais royal", "Le premier Soul Reaper"], c=2)
drop(S, "Comment Ichigo récupère ses pouvoirs après les avoir perdus face à Aizen ?")
drop(S, "Qui est Orihime Inoue et quelle est sa capacité ?")
drop(S, "Quel est le numéro de l'Espada la plus puissante dans l'armée d'Aizen ?")
drop(S, "Qu'est-ce que la Finalisation (Resurección) des Arrancar ?")
fix(S, "Quel est le nom de la prison dimensionnelle où les Soul Reapers rebelles sont enfermés ?",
    q="Comment s'appelle la prison souterraine où sont enfermés les pires criminels de la Soul Society ?",
    fb="Muken est le niveau le plus profond de la prison souterraine de la Soul Society. Aizen y est condamné à 20 000 ans d'emprisonnement.")
drop(S, "Comment s'appelle la technique permettant aux Soul Reapers de se déplacer à vitesse extrême ?")
fix(S, "Comment s'appelle la technique d'accélération qui rend les Soul Reapers quasi-invisibles à l'oeil nu ?",
    q="Comment s'appelle la technique de déplacement ultrarapide des Soul Reapers ?",
    fb="Le Shunpo permet aux Soul Reapers de se déplacer si vite qu'ils semblent disparaître. Yoruichi en est la grande spécialiste.")
drop(S, "Quel est le Bankai d'Ichigo après la maîtrise de son Hollow intérieur ?")
fix(S, "Comment Kisuke Urahara piège-t-il finalement Aizen ?",
    a=["En le battant au combat", "Grâce à un sceau caché dans ses attaques qui s'active quand Aizen s'affaiblit", "En le tuant", "En lui volant l'Hogyoku"], c=1,
    fb="Pendant leur combat, Urahara glisse un sceau dans le corps d'Aizen. Quand celui-ci est affaibli par Ichigo, le sceau s'active et l'immobilise.")
drop(S, "Quel est le vrai pouvoir de Chad (Yasutora Sado) découvert progressivement ?")
fix(S, "Quelle est la particularité du Zanpakuto de Gin Ichimaru ?",
    q="Quelle est la particularité du Bankai de Gin Ichimaru ?",
    a=["Il contrôle la glace", "Sa lame peut s'allonger jusqu'à 13 km", "Il crache du feu", "Il contrôle les ombres"], c=1,
    fb="Kamishini no Yari, le Bankai de Gin, s'allonge jusqu'à 13 kilomètres à une vitesse foudroyante. Gin cache en plus un poison capable de détruire les cellules.")
fix(S, "Quel est le nom des gardes du corps d'Aizen qui protègent Hueco Mundo ?",
    q="Comment appelle-t-on les subordonnés personnels de chaque Espada ?",
    fb="Les Fracción sont les serviteurs attitrés d'un Espada. Ils se distinguent des Números, les Arrancar de rang inférieur.")
drop(S, "Comment s'appelle la forme fusionnée de Hollow et Soul Reaper qu'Ichigo atteint ?")
drop(S, "Quel est le rang du 13ème Escadron dans la hiérarchie de Soul Society ?")
fix(S, "Qu'est-ce que le Blut Vene et Blut Arterie des Quincy ?",
    fb="Le Blut Vene renforce la défense en faisant circuler l'énergie spirituelle dans les veines, le Blut Arterie renforce l'attaque. Un Quincy ne peut pas utiliser les deux en même temps.")
drop(S, "Qui est Sosuke Aizen et quel est son Zanpakuto spécial ?")
fix(S, "Quel Arrancar est la 4ème Espada et possède un pouvoir de régénération ?",
    fb="Ulquiorra Cifer est le 4e Espada. Il se régénère presque instantanément et sa Resurrección, Murciélago, possède une seconde étape unique parmi les Espada.")


# ---------------------------------------------------------------- Minecraft
S = 'minecraft'
fix(S, "Quel bloc est le plus solide disponible en survie normale (résistance aux explosions) ?",
    q="Quel bloc courant résiste aux explosions de TNT et de Creeper ?",
    a=["Bloc de fer", "Obsidienne", "Bloc de diamant", "Pierre taillée"], c=1,
    fb="L'obsidienne fait partie des blocs les plus résistants aux explosions que l'on peut obtenir en survie. Elle sert aussi à construire les portails du Nether.")
fix(S, "Quelle gemme est plus rare que le diamant depuis la version 1.16 ?",
    q="Quel matériau, introduit en 1.16, surpasse le diamant pour les outils et les armures ?",
    a=["Rubis", "Émeraude", "Améthyste", "Netherite"], c=3,
    fb="La netherite s'obtient à partir de débris antiques trouvés dans le Nether depuis la 1.16. L'équipement en netherite est le meilleur du jeu et résiste au feu et à la lave.")
fix(S, "Comment s'appelle la dimension souterraine avec des portails de lave et des Ghasts ?",
    q="Comment s'appelle la dimension infernale peuplée de Ghasts et de Piglins ?")
fix(S, "Quel mob drop des Rails d'Alimentation lors d'un craft ?",
    q="Avec quoi fabrique-t-on des rails de propulsion ?",
    a=["Or, bâtons et redstone", "Fer et bâtons seulement", "Diamant et redstone", "Cuivre et bâtons"], c=0)
drop(S, "Quel est le nom du biome extrêmement rare en forme de champignon ?")
drop(S, "Quel est le boss du Nether dans Minecraft ?")
fix(S, "Quel boss de Minecraft est invoqué en plaçant 3 crânes de Squelette du Nether sur de la Soulsand en forme de T ?",
    q="Quel boss invoque-t-on en posant trois crânes de Wither squelette sur du sable des âmes disposé en T ?",
    fb="Le Wither s'invoque avec quatre blocs de sable des âmes en T surmontés de trois crânes de Wither squelette. Vaincu, il laisse une étoile du Nether, qui sert à fabriquer une balise.")
fix(S, "Quel item unique est obtenu en tuant l'Ender Dragon ?",
    fb="L'œuf de dragon apparaît au sommet du portail de sortie après la première victoire sur l'Ender Dragon. Il est purement décoratif.")
drop(S, "Quel est le nom du boss des Donjons Anciens dans l'Overworld deep underground ?")
drop(S, "Combien de types de bois différents existent dans la version actuelle de Minecraft ?")
fix(S, "Quel est le nom du village sous-marin protégé par des Guardians ?",
    q="Comment s'appelle la structure sous-marine protégée par des Gardiens ?",
    fb="Le monument océanique est une structure en prismarine gardée par des Gardiens et trois Gardiens anciens. Huit blocs d'or sont cachés en son cœur.")
fix(S, "Quelle plante est nécessaire pour créer une potion de soin (Healing II) ?",
    q="Quel ingrédient sert à préparer une potion de soin ?",
    a=["Fougère", "Pastèque scintillante", "Pissenlit", "Canne à sucre"], c=1,
    fb="La pastèque scintillante, fabriquée avec une tranche de pastèque et huit pépites d'or, est l'ingrédient de la potion de soin instantané.")
drop(S, "Quel est le nombre maximum de mobs qui peuvent spawner dans une zone donnée avant que le spawn soit bloqué ?")
drop(S, "Quel mob est passif mais peut pousser le joueur hors des falaises ?")
drop(S, "Quelle est la profondeur minimale à laquelle les diamants peuvent être trouvés ?")
fix(S, "Quelle est la profondeur où les diamants spawent le plus fréquemment depuis la version 1.18 ?",
    q="À quelle hauteur conseille-t-on souvent de miner pour trouver des diamants depuis la 1.18 ?",
    a=["Y=12", "Y=40", "Y=-58", "Y=64"], c=2,
    fb="Depuis la 1.18, les diamants sont plus fréquents tout en bas du monde. Miner vers Y=-58 permet d'en trouver beaucoup tout en restant au-dessus de la bedrock.")
fix(S, "Comment s'appelle le boss sous-marin gardant les Monuments Aquatiques ?",
    fb="Le Gardien ancien protège les monuments océaniques : il y en a trois par monument. Il inflige la Fatigue de minage, qui ralentit énormément le minage.")
drop(S, "Quel bloc émet de la lumière et peut être placé sous l'eau ?")
fix(S, "Quel bloc produit de la lumière même sous l'eau et se craft avec du prismarine ?",
    a=["Torche", "Lanterne", "Lanterne aquatique", "Pierre lumineuse"], c=2,
    fb="La lanterne aquatique se fabrique avec des éclats et des cristaux de prismarine, que l'on trouve dans les monuments océaniques. Elle éclaire au niveau maximal, même sous l'eau.")
fix(S, "Quel matériau est nécessaire pour fabriquer une Élytre de réparation ?",
    q="Avec quel objet répare-t-on des élytres sur une enclume ?",
    a=["Plumes de poulet", "Toile d'araignée", "Membranes de phantom", "Cuir"], c=2,
    fb="Les élytres s'usent en vol et se réparent sur une enclume avec des membranes de phantom. Les phantoms apparaissent la nuit quand le joueur n'a pas dormi depuis plusieurs jours.")
fix(S, "Quel matériau est nécessaire pour fabriquer un lit dans Minecraft ?",
    a=["Laine et planches", "Laine et ficelle", "Planches et plumes", "Laine et fer"], c=0)
drop(S, "Comment créer un lit dans Minecraft ?")
fix(S, "Quel est le temps d'un cycle jour-nuit dans Minecraft ?",
    fb="Un cycle complet dure 20 minutes réelles : environ 10 minutes de jour, 7 minutes de nuit, et un lever et un coucher de soleil d'une minute et demie chacun.")
drop(S, "Comment appelle-t-on l'arme la plus puissante contre les mobs avec une portée à distance ?")
fix(S, "Comment récupère-t-on des expériences (XP) dans Minecraft ?",
    a=["En dormant", "En tuant des mobs, en minant certains minerais ou en cuisinant", "En construisant uniquement", "En regardant le ciel"], c=1)
fix(S, "Quel est l'enchantement permettant aux outils de ne pas perdre de durabilité ?",
    q="Quel enchantement réduit l'usure des outils ?",
    fb="Solidité (Unbreaking) donne une chance que l'outil ne s'use pas à chaque utilisation. Raccommodage (Mending) répare l'objet avec l'expérience ramassée.")
fix(S, "Quel biome du Nether est violet/cramoisi et rempli de champignons géants ?",
    q="Quel biome du Nether, rouge cramoisi, est rempli de champignons géants ?")
fix(S, "Quel objet permet de localiser des structures spéciales dans Minecraft ?",
    a=["Boussole", "Carte vide", "Carte d'exploration", "Longue-vue"], c=2,
    fb="Les cartes d'exploration, vendues par les villageois cartographes contre des émeraudes, indiquent l'emplacement de structures comme les monuments océaniques ou les manoirs.")
drop(S, "Comment créer une ferme automatique de Creeper pour obtenir de la poudre à canon ?")
drop(S, "Quelle est la profondeur maximale d'un puits de mine automatique (bedrock) ?")
drop(S, "Comment s'appelle le système de transport rapide utilisant des rails et des wagonnets ?")
drop(S, "Quel est le biome le plus froid de Minecraft avec des pics de glace ?")
fix(S, "Quel mob neutre attaque si on brise son alvéole ou si on porte une citrouille ?",
    q="Quel mob neutre attaque en groupe si on casse sa ruche sans l'avoir enfumée ?",
    fb="Les abeilles, arrivées en 1.15, attaquent et empoisonnent si on casse leur ruche. Un feu de camp placé dessous les calme et permet de récolter le miel sans risque.")
fix(S, "Quel est l'enchantement permettant de collecter plus de blocs en minant (exemple: diamants) ?",
    fb="Fortune III peut donner jusqu'à quatre diamants par minerai. À l'inverse, Toucher de soie récupère le minerai intact.")
drop(S, "Quel est le premier biome à avoir ses propres variants de villages spécifiques ?")
fix(S, "Comment créer du Netherite pour améliorer ses armures et outils en diamant ?",
    a=["Miner directement de la netherite", "Fondre des débris antiques puis combiner 4 fragments avec 4 lingots d'or", "Fouiller les coffres du Nether", "L'acheter aux villageois"], c=1,
    fb="Les débris antiques fondus donnent des fragments de netherite. Quatre fragments et quatre lingots d'or forment un lingot, qui améliore l'équipement en diamant sur une table de forgeron.")
fix(S, "Quel mob rose du Nether dans Minecraft peut marcher sur la lave mais est ralenti et endommagé par l'eau ou la pluie ?",
    q="Quel mob du Nether marche sur la lave et peut être chevauché avec une selle ?",
    fb="L'arpenteur (Strider) se déplace sur la lave. Avec une selle et un champignon biscornu au bout d'une canne, le joueur peut le chevaucher pour traverser les lacs de lave.")
fix(S, "Quel mob produit de la soie qui sert à créer des fils et des arcs ?",
    q="Quel mob lâche de la ficelle, utile pour fabriquer des arcs ?",
    a=["Araignée", "Chauve-souris", "Poulpe", "Slime"], c=0,
    fb="Les araignées lâchent de la ficelle, qui sert à fabriquer des arcs, des cannes à pêche et des fils de détente.")
drop(S, "Qu'est-ce qu'une Seed connue parmi les plus célèbres du speedrunning Minecraft ?")
drop(S, "Quel type de Village génère des villageois Cartographes utiles pour l'exploration ?")
fix(S, "Quel animal Minecraft peut être dressé avec des poissons crus pour devenir un compagnon ?",
    a=["Renard", "Chat", "Loutre", "Pingouin"], c=1,
    fb="Les chats errants des villages s'apprivoisent avec du poisson cru. Ils font fuir les Creepers, ce qui en fait de précieux gardiens.")
drop(S, "Quel est le nom du boss final de la dimension End dans Minecraft ?")
fix(S, "Quel effet est appliqué au joueur quand il entre dans un Village Maudit (Bad Omen) ?",
    q="Quel effet de statut déclenche un raid quand le joueur entre dans un village ?",
    a=["Poison", "Mauvais présage", "Lenteur", "Malchance"], c=1,
    fb="Un joueur sous Mauvais présage qui entre dans un village déclenche un raid : des vagues de pillards, de ravageurs et d'évocateurs attaquent.")
fix(S, "Dans quels emplacements de la dimension End les Élytra peuvent-elles être trouvées ?",
    fb="Les élytres se trouvent dans les navires de l'End amarrés à certaines cités de l'End, défendues par des Shulkers. Il n'y en a qu'une paire par navire.")
drop(S, "Combien de types de biomes existent approximativement dans Minecraft Java actuel ?")


# ---------------------------------------------------------------- GTA
S = 'gta'
fix(S, "Quel est le braquage final de l'histoire de GTA V ?",
    fb="Le braquage de l'Union Depository est le grand final : Michael, Trevor et Franklin s'attaquent à la réserve d'or de Los Santos, avec une approche discrète ou une approche frontale.")
fix(S, "Quel personnage vient du monde des affaires et de l'immobilier (semi-retraité du crime) ?",
    q="Quel protagoniste, ancien braqueur, vit retiré sous une fausse identité ?",
    fb="Michael De Santa vit sous une fausse identité avec sa famille à Rockford Hills, grâce à un accord avec le FIB. Sa rencontre avec Franklin le ramène au crime.")
drop(S, "Quel est le nom de l'agence gouvernementale secrète qui kidnappe Michael dans GTA V ?")
drop(S, "Quel véhicule iconique de Rockstar est présent dans GTA V comme référence à GTA San Andreas ?")
fix(S, "Quel est le nom de la prison de Blaine County dans GTA V ?",
    fb="Le pénitencier de Bolingbroke est la grande prison de Blaine County. Dans GTA Online, le braquage « Évasion de prison » consiste à en faire sortir un détenu.")
fix(S, "Quelle compagnie de taxi peut être appelée par le joueur dans GTA V ?",
    fb="Downtown Cab Co. est la compagnie de taxis de Los Santos. Franklin peut même la racheter, et le joueur peut appeler un taxi depuis son téléphone.")
fix(S, "Quel est le nom du grand magasin de luxe sur la Vinewood Boulevard dans GTA V ?",
    q="Quelle boutique de vêtements haut de gamme de GTA V s'inspire des boutiques de Rodeo Drive ?")
drop(S, "Comment s'appelle la société de braquage que les trois protagonistes forment ?")
drop(S, "Quel est le braquage GTA Online le plus difficile et le plus lucratif ?")
fix(S, "Quel est le nom du personnage antagoniste principal de la Trésorerie de l'État dans GTA V ?",
    q="Quel agent corrompu du FIB fait chanter les protagonistes de GTA V ?")
drop(S, "Quel criminel californien a servi d'inspiration pour le personnage de Trevor Philips ?")
drop(S, "Quelle action en jeu permet à Franklin d'utiliser sa capacité spéciale ?")
drop(S, "Quel est le prix de base d'une propriété Executive dans GTA Online ?")
drop(S, "Quel personnage de GTA V peut effectuer des échanges de corps en Yoga (capacité de rêve) ?")
fix(S, "Quelle activité légale permet à Michael de se détendre dans GTA V ?",
    a=["La pêche", "Le golf", "Le bowling", "La chasse"], c=1,
    fb="Michael, passionné de golf, peut jouer au club de golf de Los Santos. Il pratique aussi le yoga et le tennis.")
drop(S, "Comment s'appelle l'assistant IA du téléphone dans GTA V ?")
drop(S, "Quel est le réseau social fictif utilisé par les personnages dans GTA V ?")
drop(S, "Quel sport de combat Trevor peut-il pratiquer en jeu dans GTA V ?")
drop(S, "Comment s'appelle le jeu de simulation de stock-car dans GTA V accessible en ligne ?")
fix(S, "Quel est le nom de la chaîne fast food présente partout dans Los Santos ?",
    q="Quelle chaîne de fast-food de GTA V est spécialisée dans le poulet ?")
fix(S, "Quel est le nom de l'aéroport principal de Los Santos ?",
    fb="L'aéroport international de Los Santos s'inspire de celui de Los Angeles. On y trouve l'école de pilotage où les personnages peuvent améliorer leurs compétences.")
drop(S, "Comment Trevor obtient-il son hélicoptère dans GTA V ?")
fix(S, "Comment s'appelle la base militaire secrète dans les montagnes de GTA V ?",
    q="Comment s'appelle la base militaire de l'armée dans GTA V ?",
    fb="Fort Zancudo abrite des avions de chasse, des chars et des hélicoptères militaires. Y pénétrer déclenche immédiatement un avis de recherche élevé.")
drop(S, "Quel est le montant que Michael reçoit en protection du FIB au début de la campagne ?")
drop(S, "Comment s'appelle la moto de gangsters que Michael peut conduire lors d'une mission ?")
drop(S, "Quel est le type de fichiers qu'on vole dans le braquage Bureau Raid de GTA V ?")
fix(S, "Combien de niveaux de recherche (étoiles) existe-t-il dans GTA V ?",
    fb="L'avis de recherche va de 1 à 5 étoiles. Plus il y a d'étoiles, plus les forces de l'ordre envoient de patrouilles, d'hélicoptères et d'unités d'élite.")
drop(S, "Quel crime en ligne dans GTA Online permet de voler des voitures de luxe pour les exporter ?")
drop(S, "Quelle île du nord-est de Los Santos possède un port industriel dans GTA V ?")
drop(S, "Comment s'appelle le quartier de gangsters Ballas dans GTA V ?")
drop(S, "Quelle est la capacité spéciale de Michael permettant de ralentir le temps ?")
drop(S, "Quelle est la capacité spéciale de Trevor dans GTA V ?")
fix(S, "Quelle capacité spéciale Trevor peut-il activer pour devenir temporairement invincible ?",
    q="Quelle est la capacité spéciale de Trevor dans GTA V ?",
    a=["Le ralenti en voiture", "Une rage qui augmente les dégâts infligés et réduit ceux reçus", "Il n'en a pas", "La vision nocturne"], c=1,
    fb="La capacité de Trevor est une rage furieuse : pendant quelques secondes, il inflige plus de dégâts et en reçoit moins.")
fix(S, "Quel est le résultat de l'option A de la fin de GTA V ?",
    a=["Franklin tue Trevor", "Franklin tue Michael", "Trevor s'échappe", "Tous survivent"], c=0,
    fb="Dans l'option A, Franklin suit la demande du FIB et élimine Trevor. Dans l'option B, il tue Michael pour Devin Weston. L'option C, où tous survivent, est considérée comme la fin officielle.")
drop(S, "Quelle mission implique Franklin de voler une voiture pour Simeon dans les premières missions ?")
drop(S, "Quelle carte GTA représente quelle réalité géographique de Los Angeles ?")
drop(S, "Quel est le nom de la boîte de nuit de Trevor dans GTA V ?")
drop(S, "Quel est le nom du club de strip-tease que les joueurs peuvent acheter dans GTA V ?")
fix(S, "Combien y a-t-il de missions principales dans la campagne de GTA V ?",
    fb="La campagne de GTA V compte 69 missions principales, auxquelles s'ajoutent de nombreuses missions secondaires et activités.")
drop(S, "Quel est le symbole du jeu sur l'écran de démarrage de GTA V ?")
fix(S, "Comment s'appelle le système de réputation dans GTA Online qui détermine les avantages ?",
    q="Comment s'appellent les points d'expérience qui font monter le niveau dans GTA Online ?",
    a=["Les GTA$", "Les RP", "La Street Cred", "Les Fame Points"], c=1)
drop(S, "Comment s'appelle la ville côtière accessible par pont depuis Los Santos dans GTA V ?")
drop(S, "Quel est le prix de base d'un appartement de luxe dans GTA Online au lancement en 2013 ?")
drop(S, "Quel est le bâtiment le plus visible de Los Santos avec son dôme d'or ?")
drop(S, "Comment s'appelle le système de vol de données dans le Braquage Pac Standard GTA Online ?")
drop(S, "Quelle musique célèbre accompagne la scène d'ouverture de GTA V en 1987 ?")
fix(S, "Quel est le braquage optionnel de la campagne principale GTA V impliquant une bijouterie ?",
    q="Quel est le premier braquage de la campagne de GTA V ?",
    a=["The Paleto Score", "Le braquage de la bijouterie (Jewel Store Job)", "Le casse de l'Union Depository", "Le braquage de la Fleeca"], c=1,
    fb="Le premier braquage vise la bijouterie Vangelico. Le joueur choisit une approche discrète, avec du gaz et des déguisements, ou une approche armée.")
drop(S, "Quelle activité de plein air Franklin peut-il pratiquer dans les collines de Vinewood Hills ?")
drop(S, "Quel est le plus grand véhicule disponible dans GTA V Online (transport de marchandises) ?")
drop(S, "Comment s'appelle le système de classement des joueurs dans GTA Online ?")


# ---------------------------------------------------------------- Zelda
S = 'zelda'
fix(S, "Quel jeu Zelda se déroule sur l'île Koholint et met Link face à son réveil ?",
    q="Quel jeu Zelda se déroule sur l'île Koholint ?",
    a=["Oracle of Ages", "Link's Awakening", "Phantom Hourglass", "Majora's Mask"], c=1)
drop(S, "Quel jeu Zelda se déroule sur une île et voir Link réveiller le Poisson du Vent ?")
drop(S, "Quel est le donjon final emblématique des jeux Zelda 3D ?")
fix(S, "Quel est l'animal compagnon de Link dans Twilight Princess ?",
    q="En quel animal Link se transforme-t-il dans Twilight Princess ?",
    a=["Un renard", "Un oiseau", "Un loup", "Un cheval"], c=2)
drop(S, "Quel jeu Zelda se déroule dans les Terres du Crépuscule et implique une louve ?")
fix(S, "Quel personnage est la forme féminine de Sheik dans Ocarina of Time ?",
    q="Qui se cache derrière Sheik dans Ocarina of Time ?",
    a=["Navi", "Impa", "La princesse Zelda", "Une vraie Sheikah"], c=2)
drop(S, "Quel est le nom de l'elfe des bois qui guide Link dans Ocarina of Time ?")
fix(S, "Quel temple est le premier donjon de The Legend of Zelda: Ocarina of Time ?",
    q="Quel est le premier donjon de Ocarina of Time ?",
    a=["Le Temple de l'Eau", "Le Temple du Feu", "L'intérieur de l'Arbre Mojo", "Le Temple de l'Ombre"], c=2,
    fb="Le premier donjon se trouve à l'intérieur de l'Arbre Mojo, le gardien de la forêt. Link y affronte la reine Gohma et obtient l'Émeraude Kokiri.")
drop(S, "Quelle est la signification du motif de la Triforce (triangle triple) dans la mythologie Zelda ?")
drop(S, "Quel instrument Link joue-t-il dans Majora's Mask pour contrôler le temps ?")
drop(S, "Quel est le nom de l'instrument que Link joue pour progresser dans Majora's Mask ?")
fix(S, "Quel est le sanctuaire/boss final de Breath of the Wild ?",
    q="Où se trouve le combat final de Breath of the Wild ?",
    a=["Au Temple du Temps", "Au château d'Hyrule", "Au mont Lanayru", "Dans le désert Gerudo"], c=1,
    fb="Le Fléau Ganon est retenu depuis 100 ans dans le château d'Hyrule par Zelda. Link l'y affronte, puis termine le combat dans la plaine contre sa forme de bête.")
fix(S, "Quel est le nom du peuple de l'eau qui habite le Lac Hylia dans OoT ?",
    q="Quel peuple aquatique vit dans le Domaine Zora ?")
fix(S, "Quel objet de Breath of the Wild permet à Link de scanner l'environnement ?",
    q="Quel appareil Link utilise-t-il dans Breath of the Wild pour activer ses pouvoirs ?",
    a=["Une longue-vue", "La tablette Sheikah", "Le Monocle de Vérité", "Une loupe"], c=1)
drop(S, "Quel power-up Zelda donne à Link des gantelets pour soulever des objets très lourds ?")
fix(S, "Comment s'appelle le masque final de Majora's Mask que possède Skull Kid ?",
    fb="Le masque de Majora est un objet maléfique utilisé jadis dans des rituels et scellé à cause de sa puissance. Il possède Skull Kid et attire la Lune vers Termina.")
fix(S, "Quel est l'ennemi récurrent aux yeux rouges qui vole l'attention de Link dans les galeries ?",
    q="Quel ennemi récurrent avale Link pour lui voler son bouclier ?")
fix(S, "Comment s'appelle l'araignée géante boss récurrente dans la série Zelda ?",
    fb="Gohma est un boss récurrent depuis le premier jeu. Dans Ocarina of Time, elle garde le premier donjon et se combat en visant son œil unique.")
fix(S, "Quel est le nom du désert habité par les Gerudo dans Ocarina of Time ?",
    a=["Désert de Ganon", "Désert du Temps", "Désert Gerudo", "Désert de Lanayru"], c=2)
drop(S, "Comment s'appelle l'objet magique de Link permettant de viser avec précision dans Wind Waker ?")
fix(S, "Quel donjon de The Legend of Zelda: OoT est universellement reconnu comme le plus difficile ?",
    q="Quel donjon d'Ocarina of Time est célèbre pour être le plus redouté des joueurs ?",
    a=["Le Temple de l'Eau", "Le Temple de l'Ombre", "Le Temple de l'Esprit", "La Caverne de Glace"], c=0)
drop(S, "Quel est le nom des pieuvres géantes qui gardent les donjons d'eau dans les jeux Zelda 3D ?")
fix(S, "Quel objet emblématique permet à Link de voler dans The Legend of Zelda: Skyward Sword ?",
    q="Sur quoi Link vole-t-il dans Skyward Sword ?",
    a=["Une cape magique", "Une épée céleste", "Un grand oiseau, le Célestrier", "Des ailes de Roc"], c=2,
    fb="Chaque habitant de Celesbourg possède un Célestrier, un grand oiseau qui lui sert de monture volante. Celui de Link est d'un rouge rare.")
fix(S, "Quel est le nom de la terre des ombres dans Twilight Princess ?",
    q="Comment s'appelle le monde parallèle d'où vient Midna ?",
    a=["Le Monde des Ténèbres", "Le Royaume des Ombres", "Le Royaume du Crépuscule", "Le Monde Miroir"], c=2)
fix(S, "Comment s'appelle le méchant original créé spécifiquement pour Majora's Mask ?",
    q="Qui est l'antagoniste principal de Majora's Mask ?",
    a=["Vaati", "Skull Kid, possédé par un masque", "Ganondorf déguisé", "Zant"], c=1)
fix(S, "Quel est le nom de la technique de combat au sabre dans Skyward Sword basée sur les mouvements réels ?",
    fb="En levant la manette vers le ciel, Link charge son épée d'énergie et peut lancer un rayon : c'est le Skyward Strike, rendu possible par le Wii MotionPlus.")
fix(S, "Quelle est la signification du titre 'The Legend of Zelda' — qui est Zelda exactement ?",
    q="Qui est Zelda dans la série The Legend of Zelda ?",
    a=["Le héros principal", "La princesse d'Hyrule", "La mère de Link", "La fée de Link"], c=1)
drop(S, "Quel jeu Zelda sur DS permet de jouer à plusieurs sur un seul cartouche ?")
fix(S, "Quel est le boss final de Wind Waker et sous quelle forme apparaît Ganon ?",
    q="Comment se termine le combat final de The Wind Waker ?",
    a=["Ganon sous sa forme de bête", "Link plante l'épée dans le front de Ganondorf, qui se change en pierre", "Ganon s'enfuit", "Zelda scelle Ganon dans un miroir"], c=1,
    fb="Pendant que la mer engloutit Hyrule, Link plante la Master Sword dans le front de Ganondorf, qui se pétrifie.")
fix(S, "Comment Link voyage-t-il entre les îles dans The Wind Waker ?",
    a=["En nageant", "Sur un bateau qui parle, le Lion Rouge", "Par téléportation", "Sur le dos d'un oiseau"], c=1,
    fb="Link navigue sur le Lion Rouge, un bateau qui parle. On découvre qu'il s'agit en réalité du roi d'Hyrule. La baguette Wind Waker permet de contrôler le vent.")
fix(S, "Quel temple Zelda dans Ocarina of Time utilise le temps comme mécanique principale ?",
    q="Où Link trouve-t-il la Master Sword dans Ocarina of Time ?",
    a=["Au Temple du Temps", "Au Temple de la Forêt", "Au Temple de l'Ombre", "Au Temple de l'Esprit"], c=0,
    fb="Link retire la Master Sword de son socle au Temple du Temps et se réveille sept ans plus tard. En la replaçant, il retourne dans le passé.")
drop(S, "Quel est le nom du peuple des arbres natifs de la forêt dans Ocarina of Time ?")
fix(S, "Comment s'appelle l'attaque de rotation légendaire de Link utilisée dans presque tous les jeux Zelda ?",
    fb="L'attaque tourbillon permet à Link de frapper tout autour de lui en tournant sur lui-même après avoir chargé son épée. Elle est devenue un classique de la série depuis A Link to the Past.")
drop(S, "Dans Breath of the Wild, comment Link revient-il à la vie après des morts normales ?")
fix(S, "Quelle est la forme finale de Ganon dans A Link to the Past, Wind Waker et Ocarina of Time ?",
    q="Sous quelle apparence Ganon se montre-t-il à la fin d'A Link to the Past et d'Ocarina of Time ?",
    a=["Toujours une forme humaine", "Une bête géante à tête de sanglier", "Un dragon", "Une ombre"], c=1,
    fb="Ganon, la forme bestiale de Ganondorf, est un monstre colossal à tête de sanglier armé d'un trident ou de lames.")
fix(S, "Quel est le nom de l'île centrale de la mer dans The Wind Waker ?",
    q="Quelle île marchande de The Wind Waker abrite boutiques et salle des ventes ?",
    fb="L'île Mercantile (Windfall) est le grand port marchand de The Wind Waker, avec ses boutiques, sa salle des ventes et ses nombreux habitants. L'île natale de Link est l'île de l'Aurore.")
drop(S, "Quel objet de navigation Link utilise-t-il dans Phantom Hourglass et Spirit Tracks ?")
drop(S, "Comment s'appelle le voleur de chapeau que Link doit pourchasser à Kakariko dans OoT adulte ?")
fix(S, "Quel est le premier temple que Link complète dans Breath of the Wild pour obtenir ses capacités ?",
    q="Où Link obtient-il ses premiers pouvoirs dans Breath of the Wild ?",
    a=["Dans la Créature divine Vah Medoh", "Dans les sanctuaires du Plateau du Prélude", "Au Temple du Temps", "À la cité Gerudo"], c=1,
    fb="Sur le Plateau du Prélude, Link explore quatre sanctuaires qui lui donnent ses premiers pouvoirs : magnétisme, stase, cryogénie et bombes.")
fix(S, "Quel est le donjon final de The Legend of Zelda: A Link to the Past (SNES) ?",
    a=["Le Roc de la Tortue", "La Pyramide du Pouvoir", "La tour de Ganon", "Le Palais des Ténèbres"], c=2,
    fb="La tour de Ganon, au sommet de la montagne du Monde des Ténèbres, est le dernier donjon. Link y bat Agahnim, avant d'affronter Ganon dans la Pyramide.")
fix(S, "Comment s'appelle la déesse qui veille sur Hyrule et dont le nom est donné à la princesse ?",
    q="Quelle déesse s'est réincarnée en princesse Zelda, d'après Skyward Sword ?",
    fb="Skyward Sword révèle que la déesse Hylia s'est réincarnée en mortelle, Zelda, pour aider le héros à vaincre le Néant.")
drop(S, "Quel est le nom de l'arc-en-ciel visible depuis le sommet de Hyrule Castle dans OoT enfant ?")
fix(S, "Quel village de BotW est spécialisé dans l'équipement et la culture Gerudo ?",
    q="Dans quelle ville de Breath of the Wild Link doit-il se déguiser pour entrer ?",
    a=["Cocorico", "Le Domaine Zora", "Écurie du Bois", "La cité Gerudo"], c=3)
fix(S, "Quel est le nom du Sage de l'Eau dans Ocarina of Time ?",
    fb="Ruto, princesse des Zoras, devient la Sage de l'Eau. Depuis que Link l'a sauvée dans le ventre de Jabu-Jabu, elle le considère comme son fiancé.")
fix(S, "Quel objet de Skyward Sword permet à Link de voir les lignes de courant spirituel ?",
    q="Quelle capacité de son épée aide Link à localiser des objets ou des personnes dans Skyward Sword ?",
    a=["Le saut céleste", "La radiesthésie", "Le Monocle de Vérité", "La Vision du héros"], c=1,
    fb="Grâce à la radiesthésie, Link pointe son épée et suit un signal qui le guide vers l'objet ou la personne recherchée.")


# ---------------------------------------------------------------- Valorant
S = 'valorant'
drop(S, "Quel est le nom de l'arme qui one-shot à la tête à n'importe quelle distance dans Valorant ?")
drop(S, "Quel agent Valorant est le plus populaire pour les débutants grâce à sa facilité ?")
fix(S, "Quelle est la classe d'agents spécialisés dans les éclairages et info ?",
    q="Quelle classe d'agents est spécialisée dans la collecte d'informations ?",
    fb="Les Initiateurs récoltent des informations et ouvrent les sites, comme Sova avec sa flèche de reconnaissance, Breach avec ses ondes sismiques ou Fade avec ses traqueurs.")
drop(S, "Quel est le nom de la première carte de Valorant (map de base) ?")
fix(S, "Quelle map Valorant est la seule à avoir 3 sites de bombe ?",
    q="Quelles cartes de Valorant possèdent trois sites de Spike ?",
    a=["Bind et Ascent", "Haven et Lotus", "Split et Icebox", "Pearl et Breeze"], c=1,
    fb="Haven, inspirée du Bhoutan, et Lotus, inspirée de l'Inde, comptent trois sites (A, B et C), ce qui oblige la défense à se répartir davantage.")
fix(S, "Quel agent peut se rendre invisible temporairement ?", c=3,
    fb="Avec son ultime, Dimensional Drift, Yoru passe dans une autre dimension où il devient invisible et invulnérable pour aller chercher des informations.")
fix(S, "Quel est le rang maximum dans le système classé Valorant ?",
    fb="Radiant est le rang le plus élevé. Il est réservé aux meilleurs joueurs de chaque région, classés dans un tableau public.")
drop(S, "Quelle mécanique permet à certains agents de 'peek' sans prendre de dégâts complets ?")
drop(S, "Quel agent peut créer des copies de lui-même pour tromper les ennemis ?")
drop(S, "Quel agent peut lancer un clone de lui-même pour décevoir les ennemis ?")
drop(S, "Quel agent peut créer un leurre de lui-même pour tromper les ennemis ?")
fix(S, "Quelle est la cadence de tir de base pour viser précisément dans Valorant ?",
    q="Que faut-il faire pour tirer avec précision dans Valorant ?",
    a=["Sprinter en tirant", "Toujours se déplacer", "S'arrêter avant de tirer", "Sauter en tirant"], c=2)
drop(S, "Comment s'appelle le premier agent Sentinel à avoir une mécanique de résurrection ?")
drop(S, "Quel agent crée une barrière de soin pour son équipe ?")
drop(S, "Quel agent Controller crée des fumées qui bloquent la vision sur de grandes distances ?")
drop(S, "Quel agent Valorant peut créer des murs de fumée sur sa carte personnelle ?")
drop(S, "Quelle map Valorant a été retirée et remplacée plusieurs fois ?")
drop(S, "Quel est le nombre de rounds maximum dans une partie classée de Valorant ?")
fix(S, "Quel agent Dueliste de Valorant est originaire des Philippines et utilise l'électricité ?",
    fb="Neon est une Duelliste philippine qui manie l'électricité : sprint, murs électriques et rafales d'éclairs avec son ultime, Overdrive.")
drop(S, "Quel est le nom de l'organisation antagoniste dans le lore de Valorant ?")
drop(S, "Quelle organisation fictive est opposée à VALORANT Protocol dans le lore ?")
drop(S, "Comment s'appelle le système de progression des armes dans Valorant ?")
drop(S, "Quel agent peut placer une tourelle automatique pour couvrir les angles ?")
drop(S, "Quelle est la puissance de la Classic (pistolet gratuit au début de chaque round) ?")
drop(S, "Quel est le temps maximum d'un round standard dans Valorant ?")
fix(S, "Quel agent peut se soigner après avoir tué des ennemis ?",
    fb="Reyna se nourrit de l'âme de ses victimes : après un élimination, elle peut se soigner (Devour) ou devenir brièvement intouchable (Dismiss).")
fix(S, "Quel est le nombre de cartes disponibles dans le pool compétitif au lancement de Valorant ?",
    q="Combien de cartes étaient jouables au lancement de Valorant en juin 2020 ?", c=0,
    fb="Au lancement, quatre cartes étaient disponibles : Bind, Haven, Split et Ascent. Icebox est arrivée quelques mois plus tard.")
drop(S, "Comment s'appelle la capacité passive de Killjoy qui révèle les ennemis proches de ses gadgets ?")
drop(S, "Comment s'appelle la première saison compétitive officielle de Valorant ?")
drop(S, "Quel est le terme pour désigner un joueur qui n'achète pas d'arme pour économiser pour le round suivant ?")
drop(S, "Quel est le nom de la technique où un joueur reste accroupi pour réduire sa hitbox et surprendre ?")
fix(S, "Combien de rounds faut-il gagner pour remporter une partie classée de Valorant ?",
    fb="La première équipe à 13 rounds l'emporte. Les équipes changent de côté après 12 rounds, et des prolongations sont jouées en cas d'égalité 12-12.")
fix(S, "Quel agent peut détruire les utilitaires ennemis avec ses ondes sismiques ?",
    q="Quel Initiateur suédois lance des ondes sismiques à travers les murs ?",
    fb="Breach, l'Initiateur suédois, envoie ses charges à travers les murs pour aveugler, étourdir et repousser les défenseurs.")
fix(S, "Quel agent peut neutraliser temporairement les capacités ennemies avec une grenade ?",
    q="Quel agent peut empêcher les ennemis d'utiliser leurs capacités avec une lame lancée ?",
    fb="KAY/O est un robot Initiateur. Sa lame ZERO/POINT supprime les capacités des ennemis touchés, et pendant son ultime ses alliés peuvent le relever s'il tombe.")
drop(S, "Quel est l'impact d'un 'eco round' bien joué sur l'économie de l'équipe adverse ?")
drop(S, "Quel est le nom de la technique offensive où l'équipe attaque un seul site avec tout le monde ?")
drop(S, "Quel personnage de Valorant est la première à avoir une représentation non-binaire officiellement ?")
drop(S, "Quel est le résultat quand deux joueurs se tirent dessus simultanément à la tête dans Valorant ?")
fix(S, "Quel agent Controller peut se téléporter à travers ses propres fumées ?",
    q="Quel Contrôleur peut se téléporter n'importe où sur la carte avec son ultime ?",
    fb="Avec son ultime, From the Shadows, Omen peut se téléporter n'importe où sur la carte. Sa compétence Shrouded Step permet aussi de courtes téléportations.")
drop(S, "Quel agent Valorant peut traverser les murs grâce à sa technique Paranoia ?")
fix(S, "Quel est le nom de la map Valorant avec une piscine au centre et deux niveaux verticaux ?",
    q="Quelle carte de Valorant se déroule dans l'Arctique ?",
    fb="Icebox se déroule dans une base arctique, avec deux sites, des tyroliennes et beaucoup de verticalité.")
fix(S, "Comment s'appelle la ressource virtuelle qui permet d'acheter des armes et capacités en début de round ?",
    a=["L'or", "Les crédits", "Les jetons", "Les points"], c=1)
fix(S, "Quel est le rôle principal du personnage Cypher dans une équipe Valorant ?",
    fb="Cypher est une Sentinelle marocaine spécialiste de la surveillance : fils-pièges, caméra espion et cages. Son ultime révèle les ennemis à partir d'un cadavre.")
drop(S, "Quel est l'agent Dueliste le plus populaire en ranked Valorant selon les statistiques 2024 ?")
drop(S, "Comment s'appelle le mécanisme permettant d'acheter des armes pour ses coéquipiers ?")
fix(S, "Quel agent possède une capacité qui lui permet de voir à travers les murs via des empreintes ?",
    q="Quelle Initiatrice turque traque ses ennemis grâce à des créatures cauchemardesques ?",
    fb="Fade, Initiatrice turque, envoie des traqueurs qui suivent les ennemis et peut révéler leur position avec Haunt. Son ultime, Nightfall, affaiblit tous ceux qu'il touche.")


# ---------------------------------------------------------------- EA Sports FC
S = 'eafc'
fix(S, "Pourquoi EA Sports a renommé 'FIFA' en 'EA Sports FC' en 2023 ?",
    fb="Après 30 ans de partenariat, EA et la FIFA ne se sont pas entendues sur le prix du nom : la FIFA demanderait environ un milliard de dollars. EA a gardé ses licences de ligues, de clubs et de joueurs.")
fix(S, "Quel mode narratif avec le personnage Alex Hunter a été introduit dans FIFA 17 ?",
    fb="The Journey, le mode histoire de FIFA 17 à FIFA 19, suivait la carrière d'Alex Hunter.")
fix(S, "Quel joueur est sur la couverture de EA Sports FC 25 ?", c=3,
    fb="Jude Bellingham, milieu du Real Madrid et de l'Angleterre, est l'athlète de couverture d'EA Sports FC 25.")
drop(S, "Que signifie FUT dans EA Sports FC ?")
fix(S, "Comment s'appelle la monnaie gratuite gagnée en jouant dans FUT ?",
    fb="Les Pièces FUT se gagnent en jouant des matchs, en vendant des joueurs ou en relevant des défis. Elles servent à acheter des joueurs sur le Marché des transferts.")
drop(S, "Comment s'appelle l'indicateur de Chimie affiché sur chaque joueur dans l'interface FUT ?")
fix(S, "Qu'est-ce qu'une carte EDSM dans FUT ?",
    a=["Une édition spéciale de mi-saison", "Une carte de l'Équipe de la semaine, pour les joueurs les plus performants de la semaine", "Un échange de cartes entre amis", "Une carte de légende"], c=1,
    fb="Chaque semaine, EA publie l'Équipe de la semaine (EDSM) : les joueurs les plus performants dans la réalité reçoivent une carte améliorée, disponible pendant une semaine dans les packs.")
drop(S, "Comment fonctionne le système de 'Évolutions' dans FC 25 pour améliorer les joueurs ?")
drop(S, "Comment s'appelle le mode solo FUT où on affronte des équipes gérées par l'IA ?")
drop(S, "Comment s'appelle la progression de Division Rivals de la moins bonne à la meilleure ?")
drop(S, "Quel est le format d'une équipe FUT en termes de joueurs ?")
fix(S, "Quel mode permet de créer son joueur et suivre sa carrière de A-League jusqu'aux sommets ?",
    q="Quel mode permet de créer son propre joueur et de suivre sa carrière ?")
fix(S, "Quelle est la note maximale possible pour un joueur dans EA Sports FC ?",
    fb="La note maximale est de 99. Seules quelques cartes spéciales l'atteignent, comme certaines Icônes ou cartes de l'Équipe de l'année.")
drop(S, "Quelle équipe nationale est généralement la mieux notée dans EA Sports FC 25 ?")
fix(S, "Comment s'appelle la ligue française dans EA Sports FC ?",
    q="Quel championnat porte le nom d'EA Sports depuis 2023 ?",
    a=["La Ligue 1", "La Premier League", "La Liga espagnole (LALIGA EA SPORTS)", "La Serie A"], c=2,
    fb="Depuis la saison 2023-2024, EA Sports est le sponsor-titre du championnat d'Espagne, appelé LALIGA EA SPORTS.")
drop(S, "Quelle grande ligue n'est PAS intégralement sous licence dans EA Sports FC ?")
fix(S, "Quel club espagnol a le plus de joueurs bien notés dans EA Sports FC 25 ?",
    fb="Le Real Madrid est l'un des clubs les mieux notés d'EA Sports FC 25, avec Mbappé, Vinícius Jr., Bellingham et un effectif très profond.")
fix(S, "Pourquoi certains clubs de EA Sports FC ont-ils des noms ou maillots génériques ?",
    fb="Quand un club n'a pas d'accord de licence avec EA, il apparaît sous un nom modifié avec un maillot et un logo génériques.")
fix(S, "Pourquoi les packs FUT sont-ils controversés selon les régulateurs de plusieurs pays ?",
    fb="Les packs fonctionnent comme des loot boxes : on paie sans savoir ce qu'on obtient. La Belgique a par exemple interdit les packs payants, et EA affiche désormais les probabilités d'obtention.")
fix(S, "Quelle est la différence entre le 'Transfert Direct' et les 'Enchères' dans le Marché FUT ?",
    q="Sur le Marché des transferts FUT, que permet l'Achat immédiat ?",
    a=["Rien de particulier", "Acheter tout de suite au prix fixé par le vendeur", "Acheter uniquement des joueurs rares", "Recevoir un joueur gratuitement"], c=1,
    fb="L'Achat immédiat permet d'acquérir une carte sur-le-champ au prix choisi par le vendeur. Les enchères, elles, peuvent revenir moins cher mais demandent d'attendre la fin du chrono.")
drop(S, "Pourquoi EA Sports a-t-elle renommé FIFA en EA Sports FC ?")
drop(S, "Quelle récompense hebdomadaire récompense les meilleurs joueurs FUT ?")
drop(S, "Quel joueur a eu la note de 99 dans FC 25 (note maximale) ?")
drop(S, "Quel mode permet de jouer des matchs avec des règles spéciales et des règles modifiées ?")
drop(S, "Quel est le meilleur club selon EA FC en termes de note globale pour FC 25 ?")
drop(S, "Qu'est-ce qu'un Icon dans FUT ?")
drop(S, "Quel mode de jeu permet de créer un joueur personnalisé pour évoluer en club en ligne ?")
drop(S, "Quel est le nom du mode de jeu en ligne où 11 joueurs humains forment une équipe ?")
drop(S, "Quel pays a le plus de ligues sous licence dans EA Sports FC ?")
drop(S, "Quel était le nom du jeu avant qu'EA rompe avec la FIFA ?")
drop(S, "Quel mode de jeu permet de jouer des matchs avec une équipe historique sans acheter de cartes ?")
fix(S, "Qu'est-ce qu'une carte 'In Form' (IF) dans FUT ?",
    fb="Les cartes In Form sont les cartes améliorées de l'Équipe de la semaine (EDSM), attribuées chaque semaine aux joueurs les plus performants dans la réalité.")
drop(S, "Quel est le nom du mode narratif d'EA FC avec une histoire de personnage fictif ?")
drop(S, "Quel est le nom du mode de jeu narratif qui suivait Alex Hunter dans FIFA 17-19 ?")
drop(S, "Quelle ligue a le plus de clubs disponibles en intégralité dans EA Sports FC ?")
drop(S, "Quel est le mécanisme 'Chimie' dans FUT et à quoi sert-il ?")
drop(S, "Comment s'appelle le système de chimie dans FUT qui lie les joueurs par club et nationalité ?")
drop(S, "Quel trophée récompense le meilleur joueur du monde dans EA Sports FC selon le vote de la communauté ?")
drop(S, "Quelle note globale correspond généralement au seuil 'méta' dans FUT compétitif ?")
drop(S, "Quel est le nom de la monnaie virtuelle premium dans EA Sports FC ?")
drop(S, "Quel est le mode de jeu rapide 5 contre 5 inspiré du football de rue ?")
drop(S, "Quel est le mode de jeu EA FC permettant de jouer sur des terrains urbains en équipes de 3 ?")
drop(S, "Quelle est la position de jeu de Kylian Mbappé dans EA Sports FC ?")
drop(S, "Quel est le nom du mode de jeu narratif solo d'EA FC inspiré de la Coupe du Monde ?")
drop(S, "Quel est l'équivalent FUT d'un match de championnat compétitif en ligne ?")
drop(S, "Comment s'appelle la version EA Sports de la Premier League dans le jeu ?")
drop(S, "Quel est le système d'amélioration des cartes joueurs dans FUT basé sur les performances réelles ?")
drop(S, "Quelle ligue nationale a le plus de supporters dans EA Sports FC ?")
drop(S, "Quel est l'équivalent FUT de la Ligue des Champions en termes de mode de tournoi ?")
drop(S, "Quel joueur a eu la note la plus haute de l'histoire de la franchise FIFA/EAFC ?")
drop(S, "Quel est le nom de la mise à jour hebdomadaire des effectifs dans EA Sports FC ?")
drop(S, "Dans quel mode peut-on créer et gérer sa propre académie de jeunes joueurs ?")
drop(S, "Quel pays a la meilleure note globale d'équipe nationale dans EA Sports FC 25 ?")
drop(S, "Quel pays possède l'équipe nationale avec la meilleure note globale dans EA Sports FC 25 ?")
drop(S, "Quel est le type de carte FUT spéciale émise lors de la Coupe du Monde ou Euro ?")
drop(S, "Quelle est la compétition officielle de EA Sports FC au niveau pro mondial ?")
drop(S, "Quel élément graphique distingue les cartes Icons (Légendes) dans FUT ?")
drop(S, "Quel est le nom de l'événement FUT de mi-saison avec des cartes améliorées aléatoires ?")
drop(S, "Quel type de contrat consomme-t-on quand un joueur joue des matchs dans FUT ?")
drop(S, "Quel est le plafond de chimie par joueur dans EA Sports FC 25 ?")
drop(S, "Quel est le mode permettant de jouer des matchs en changeant les règles comme gravité réduite ?")
drop(S, "Quel est l'indice utilisé pour mesurer la popularité d'un joueur dans FUT selon sa demande sur le marché ?")
drop(S, "Quel est le mode permettant de jouer avec de vraies règles de club et des titres de saison ?")
drop(S, "Quel joueur a remporté le Ballon d'Or le plus de fois dans la réalité, influençant sa note Icon ?")
fix(S, "Qu'est-ce qu'un DCE (Défi Création d'Équipe) dans FUT ?",
    q="Que faut-il faire pour réussir un DCE dans FUT ?",
    a=["Gagner un match en ligne", "Soumettre une équipe qui respecte des critères précis", "Ouvrir un pack", "Marquer un but précis"], c=1,
    fb="Un DCE (Défi de création d'équipe) demande de soumettre des joueurs qui respectent des critères (note minimale, Chimie, nationalité…) en échange de packs ou de cartes.")
drop(S, "Quel est le nom de la compétition en ligne où les meilleurs joueurs FUT s'affrontent le week-end ?")
drop(S, "Comment s'appelle la compétition en ligne hebdomadaire où les meilleurs joueurs FUT s'affrontent ?")
drop(S, "Quel est le maximum de cartes qu'une équipe FUT peut contenir dans le club virtuel ?")
drop(S, "Combien de joueurs maximum peut contenir le Club FUT d'un joueur ?")
drop(S, "Quelle récompense reçoit le joueur FUT qui atteint le rang Elite en FUT Champions ?")
drop(S, "Comment s'appelle le système de statistiques qui mesure la performance d'un joueur en match réel pour EA FC ?")
drop(S, "Quel type de carte FUT est obtenu uniquement en accomplissant des Objectives (objectifs) ?")
fix(S, "Comment les joueurs peuvent-ils améliorer les statistiques d'un joueur spécifique dans FUT ?",
    a=["Avec les styles de Chimie", "Par l'entraînement", "C'est impossible", "Uniquement avec les DCE"], c=0,
    fb="Les styles de Chimie s'appliquent à un joueur et renforcent certaines statistiques, comme Hunter pour la vitesse et le tir, ou Anchor pour la défense et le physique.")
drop(S, "Comment s'appelle le processus de vente d'un joueur FUT au marché de transfert ?")
drop(S, "Quelle est la différence entre un joueur 5 étoiles de faible foot et un joueur 4 étoiles ?")
drop(S, "Comment EA Sports FC récompense-t-il les joueurs qui connectent leur compte EA chaque jour ?")
drop(S, "Quel est le nom de la fonctionnalité permettant de tester une équipe FUT avant de l'acheter ?")
drop(S, "Quel mode de EA Sports FC utilise la technologie de scan facial de vrais joueurs ?")
drop(S, "Quelle est la saison avec le plus grand nombre de nouveaux agents spéciaux EA FC ?")
drop(S, "Quel est le nom du bug légendaire dans les vieux FIFA où les gardiens passaient la balle dans leur propre but ?")
drop(S, "Comment s'appelle la notation de performance hebdomadaire qui déclenche une carte spéciale ?")
drop(S, "Quel est le format de base d'une équipe FUT en termes de nombre de joueurs ?")
drop(S, "Quel est le Quirk le plus important dans FUT pour les ailiers rapides ?")
drop(S, "Qu'est-ce qu'un 'Pack' dans FUT et quelle est la controverse autour d'eux ?")
drop(S, "Quel est le terme pour un joueur dont la valeur en FUT marché est très élevée due à de rares statistiques ?")
drop(S, "Quelle nouvelle fonctionnalité EA FC 25 a-t-elle introduite permettant aux joueurs d'évoluer leurs cartes ?")
drop(S, "Quel est le nom de la ligue française dans EA Sports FC ?")
drop(S, "Quel est le rang maximum de Division Rivals dans EA Sports FC ?")
drop(S, "Quel club de football a été renommé dans EA Sports FC suite à un changement de sponsor ?")


# ---------------------------------------------------------------- Mario
S = 'mario'
fix(S, "Comment s'appelle la princesse que Mario sauve le plus souvent ?",
    a=["Princesse Daisy", "Princesse Harmonie", "Princesse Peach", "Princesse Zelda"], c=2)
fix(S, "Quel est le nom complet du villain principal de la saga Mario ?",
    q="Quel est le principal ennemi de Mario ?", a=["King Boo", "Bowser", "Wario", "Kamek"], c=1,
    fb="Bowser, le roi des Koopas, est une immense tortue à épines qui crache du feu. Il enlève Peach depuis Super Mario Bros. en 1985.")
fix(S, "Quel power-up rend Mario invincible temporairement ?",
    a=["Méga Champignon", "Super Étoile", "Fleur de feu", "Champignon doré"], c=1,
    fb="La Super Étoile rend Mario invincible pendant quelques secondes : il clignote de toutes les couleurs et élimine les ennemis au contact, sur une musique très reconnaissable.")
drop(S, "Quel est le power-up qui donne à Mario une étoile d'invincibilité dorée temporaire ?")
fix(S, "Quel est le nom de la planète-île centrale dans Super Mario Galaxy ?",
    q="Comment s'appelle la base d'Harmonie (Rosalina) dans Super Mario Galaxy ?",
    a=["La Grande Étoile", "Le Cœur galactique", "L'Observatoire de la comète", "La Station Galaxy"], c=2,
    fb="L'Observatoire de la comète est la base d'Harmonie et des Lumas. Mario s'y rend entre deux galaxies.")
drop(S, "Quel est le nom de la galaxie centrale de Super Mario Galaxy ?")
drop(S, "Comment s'appelle la base cosmique de Rosalina dans Super Mario Galaxy 1 ?")
drop(S, "Quel mode de jeu emblématique de Mario Kart permet à 4 joueurs de jouer en même écran ?")
fix(S, "Quel jeu Mario est le plus vendu de tous les temps ?",
    fb="Mario Kart 8 Deluxe, sur Switch, dépasse les 60 millions d'exemplaires vendus : c'est le jeu Mario le plus vendu.")
fix(S, "Quel est le nom de la tortue mount emblématique de Mario depuis 1990 ?",
    q="Quel dinosaure sert de monture à Mario depuis Super Mario World ?")
drop(S, "Quel item permet à une tortue Koopa de glisser à grande vitesse dans les niveaux ?")
drop(S, "Dans quel jeu Mario peut-il lancer des caps et capturer des ennemis ?")
drop(S, "Quel est le nom du chapeau vivant de Mario dans Super Mario Odyssey ?")
fix(S, "Comment s'appelle le crabe géant boss récurrent de la série Mario ?",
    q="Comment s'appelle le fils de Bowser, apparu dans Super Mario Sunshine ?")
fix(S, "Quel power-up Super Mario donne-t-il à Mario une cape et la capacité de voler ?",
    q="Quel objet donne une cape à Mario dans Super Mario World ?",
    a=["Une Super Feuille", "Une Plume", "Une Étoile", "Un Super Champignon"], c=1,
    fb="Dans Super Mario World, la Plume donne à Mario une cape qui lui permet de planer et de voler après avoir pris de l'élan.")
drop(S, "Comment s'appelle le mode où deux joueurs partagent l'écran dans New Super Mario Bros. Wii ?")
fix(S, "Quel est le nom de la forteresse principale de Bowser dans Super Mario World ?",
    q="Comment s'appelle la zone finale de Super Mario World ?")
fix(S, "Combien d'étoiles doit-on collecter pour affronter Bowser la première fois dans Super Mario 64 ?",
    a=["8", "10", "12", "15"], c=0,
    fb="Il faut 8 étoiles pour ouvrir la porte qui mène au premier combat contre Bowser. Le combat final en demande 70, et le jeu en compte 120.")
drop(S, "Quel est le son iconique entendu quand Mario prend un champignon ?")
drop(S, "Comment s'appelle le son iconique joué quand Mario reçoit un power-up mushroom ?")
drop(S, "Quel son est associé à la mort de Mario dans presque tous les jeux ?")
drop(S, "Comment s'appelle l'effet sonore joué quand Mario tombe dans un trou sans fond ?")
drop(S, "Quel est le nom de la mégastructure finale à détruire dans Super Mario Odyssey ?")
drop(S, "Comment s'appelle le royaume où Mario doit retrouver Peach dans Super Mario Odyssey ?")
drop(S, "Quel est le nom de la galaxie finale dans Super Mario Galaxy ?")
fix(S, "Quel power-up dans Super Mario 3D World transforme Mario en Félin ?",
    q="Quel costume la Super Clochette donne-t-elle à Mario dans Super Mario 3D World ?",
    a=["Mario Tanuki", "Mario Chat", "Mario Abeille", "Mario Boomerang"], c=1)
drop(S, "Quel est le monde final du jeu original Super Mario Bros. sur NES ?")
fix(S, "Quel est le power-up qui permet à Mario de lancer des boules de glace dans certains jeux ?",
    fb="Dans New Super Mario Bros. Wii, la Fleur de glace permet de lancer des boules qui gèlent les ennemis. Les blocs de glace obtenus peuvent ensuite être ramassés et lancés.")
fix(S, "Quel est le nom de la femme Koopa dans les jeux Mario RPG et Paper Mario ?",
    q="Comment s'appelle la vieille Magikoopa conseillère de Bowser dans Paper Mario ?",
    fb="Kammy Koopa est une vieille Magikoopa au service de Bowser dans Paper Mario. Elle ne doit pas être confondue avec Kamek, autre sorcier de Bowser.")
drop(S, "Quel jeu Mario introduit l'énergie de vie (avec des cœurs) au lieu de simples tailles ?")
fix(S, "Quel est le nom du joueur de tennis rival de Mario dans Mario Tennis ?",
    q="Quel personnage a été créé pour Mario Tennis sur Nintendo 64 ?",
    a=["Waluigi", "Wario", "Daisy", "Harmonie"], c=0,
    fb="Waluigi est apparu pour la première fois dans Mario Tennis sur Nintendo 64, en 2000, comme partenaire de Wario.")
drop(S, "Quel personnage est la principale rivale de Mario dans le jeu d'arcade Donkey Kong original ?")
fix(S, "Comment s'appelle la femme-journaliste que Mario sauve dans Donkey Kong original ?",
    q="Qui Mario doit-il sauver dans le Donkey Kong original de 1981 ?")
drop(S, "Quel est le nom des niveaux bonus cachés dans les jeux Mario qui donnent des champignons 1-Up ?")
fix(S, "Quel est le nom de l'ennemi à carapace verte que Mario peut glisser comme projectile ?",
    fb="Le Koopa Troopa se cache dans sa carapace quand Mario lui saute dessus. Mario peut alors la lancer : la verte file tout droit et rebondit contre les murs.")
fix(S, "Comment s'appelle le champignon qui fait rétrécir Mario dans certains jeux ?",
    q="Quel faux champignon, apparu dans Super Mario Bros. : The Lost Levels, blesse Mario ?",
    fb="Le Champignon poison ressemble à un Super Champignon, mais il blesse Mario au lieu de le faire grandir.")
drop(S, "Dans quel jeu Mario peut-on jouer un niveau de chaque monde dans un ordre libre ?")
drop(S, "Quel est le type d'ennemi qui vole un objet de Mario puis le lui revend ?")
drop(S, "Quel est le thème musical de la carte du monde dans Super Mario Bros. 3 ?")
fix(S, "Comment s'appelle le château que Mario doit escalader à la fin de chaque monde dans SMB3 ?",
    q="Où Mario affronte-t-il les Koopalings à la fin de chaque monde dans Super Mario Bros. 3 ?",
    a=["Dans un château Koopa", "À bord d'un bateau volant", "Dans une forteresse sous-marine", "Au sommet d'une tour"], c=1,
    fb="À la fin de chaque monde, Mario monte à bord d'un bateau volant pour affronter le Koopaling qui a volé le sceptre du roi.")
drop(S, "Quel est le record mondial de vitesse actuel pour finir Super Mario Bros. sans glitch (Any%) ?")
drop(S, "Quel est le record du monde speedrun de Super Mario Bros. (any%) en 2024 ?")
fix(S, "Dans Mario Kart, quel est l'objet qui permet de voler le premier rang à l'adversaire de tête ?",
    q="Dans Mario Kart, quel objet vise directement le joueur en tête ?",
    a=["La carapace bleue", "Le Bill Balle", "L'éclair", "La banane"], c=0,
    fb="La carapace à épines bleue fonce sur le joueur en tête de course. Elle est devenue le symbole des retournements de situation entre amis.")
fix(S, "Quel est le nom du niveau de glace emblématique de Super Mario Bros. 3 ?",
    q="Quel monde de Super Mario Bros. 3 est entièrement glacé ?",
    a=["Ice Land", "Sky Land", "Water Land", "Pipe Land"], c=0)
fix(S, "Comment se nomme l'oiseau rouge géant compagnon de Yoshi dans Yoshi's Island ?",
    q="Quel oiseau transporte bébé Mario au début de Yoshi's Island ?",
    a=["Birdo", "Un Paratroopa", "Kamek", "La cigogne"], c=3)
drop(S, "Quel est le nom du système de navigation dans Super Mario Galaxy ?")
fix(S, "Quel objet Mario lance-t-il dans DK original pour éviter les tonneaux ?",
    q="Quel objet permet à Mario de détruire les tonneaux dans le Donkey Kong original ?",
    fb="Dans Donkey Kong (1981), le marteau permet à Mario de briser les tonneaux. Mais tant qu'il le tient, il ne peut plus sauter.")
drop(S, "Quel jeu Mario introduit pour la première fois des niveaux à défilement vertical ?")
drop(S, "Quel est le nom de la rivière de lave que Mario doit souvent traverser dans les mondes de Bowser ?")
fix(S, "Quel est le nom du boss récurrent de chaque monde dans la série Mario 2D classique ?",
    q="Quel boss garde les forteresses de Super Mario Bros. 3 ?")


# ---------------------------------------------------------------- Friends
S = 'friends'
drop(S, "Quel running gag implique Chandler et une blague sur sa carrière professionnelle ?")
drop(S, "Quel épisode iconique montre Ross coinçant un sofa dans les escaliers ?")
fix(S, "Qui épouse qui dans la finale de Friends ?", q="Comment se termine la série Friends ?")
drop(S, "Comment s'appelle la chanson que Phoebe joue le plus souvent à Central Perk ?")
fix(S, "Quel épisode de Noël est souvent cité comme le plus drôle de la série ?",
    q="Dans quel épisode Ross se déguise-t-il en tatou pour fêter Hanoukka avec son fils ?")
drop(S, "Combien de fois Ross s'est-il marié au total dans la série ?")
fix(S, "Quel est le prénom du fils de Ross et Carol ?",
    fb="Ben est le fils de Ross et Carol. Il naît pendant la première saison et est élevé par Carol et sa compagne Susan.")
fix(S, "Dans quelle saison Monica et Chandler révèlent-ils leur relation secrète ?",
    fb="Monica et Chandler se mettent ensemble à la fin de la saison 4. Leur histoire, longtemps cachée, éclate au grand jour au milieu de la saison 5, après que Phoebe les a surpris par la fenêtre.")
drop(S, "Quelle est la signature vocale de Joey dans la série ?")
fix(S, "Dans quel appartement habitent Joey et Chandler ?", c=2,
    fb="Après un changement de numérotation au cours de la série, l'appartement de Joey et Chandler porte le numéro 19, en face de celui de Monica, le 20.")
drop(S, "Dans quel épisode les filles perdent leur appartement contre Joey et Chandler ?")
drop(S, "Quelle est la durée totale de la série Friends en heures approximatives ?")
drop(S, "Combien de fois Ross dit-il le mauvais prénom lors de son mariage avec Emily ?")
fix(S, "Quel est le prénom de la petite fille adoptée par Chandler et Monica ?",
    q="Comment s'appellent les jumeaux adoptés par Monica et Chandler ?",
    a=["Emma et Ben", "Jack et Erica", "Ben et Emily", "Jack et Judy"], c=1,
    fb="Monica et Chandler pensaient adopter un seul bébé : Erica, la mère biologique, accouche de jumeaux. Ils les appellent Jack et Erica, puis partent s'installer dans la banlieue de New York.")
fix(S, "Quel autre nom porte Monica quand elle essaie de coacher Chandler lors d'entretiens ?",
    q="Quel nom mal orthographié figure sur le magazine télé livré à Chandler ?",
    a=["Miss Chanandler Bong", "Mister Chandeleur Bing", "Chandler Bang", "Miss Chandra Bong"], c=0,
    fb="Le magazine télé de Chandler arrive au nom de « Miss Chanandler Bong », une erreur qui devient un running gag.")
fix(S, "Quel acteur joue le personnage de Ross Geller ?",
    fb="David Schwimmer joue Ross Geller, paléontologue qui enseigne à l'université. Il est le frère aîné de Monica.")
drop(S, "Quel acteur joue Ross Geller dans la série Friends ?")
drop(S, "Quel est le vrai prénom de Phoebe Buffay dans la série ?")
fix(S, "Comment s'appelle le chien en peluche géant que Joey et Chandler gardent dans leur appartement ?",
    q="Comment s'appelle la grande statue de chien blanc de Joey ?",
    a=["Rex", "Pat", "Spot", "Cecil"], c=1,
    fb="Pat est la statue de chien en céramique blanche que Joey adore et garde dans l'appartement.")
drop(S, "Quel personnage dit souvent 'Oh my eyes!' en voyant quelque chose de gênant ?")
drop(S, "Quel épisode voit Joey accidentellement se fiancer à Rachel ?")
drop(S, "Quel emploi Monica occupe-t-elle dans la dernière saison ?")
drop(S, "Quel personnage secondaire récurrent est le père biologique de Emma ?")
fix(S, "Quel personnage adore les sandwichs à la dinde de Noël plus que tout au monde ?",
    q="Quel personnage adore le sandwich aux restes de dinde de Thanksgiving ?",
    fb="Ross adore le « Moist Maker », son sandwich aux restes de dinde de Thanksgiving. Quand un collègue le lui mange au bureau, il pique une colère mémorable.")
fix(S, "Comment s'appelle le patron/ex-patron de Rachel dans la mode ?",
    q="Pour quelle grande marque de mode Rachel travaille-t-elle dans les dernières saisons ?",
    fb="Rachel travaille chez Ralph Lauren. À la fin de la série, elle reçoit une offre de Louis Vuitton à Paris.")
drop(S, "Quel est le surnom affectueux de Chandler que sa mère utilise ?")
drop(S, "Quel est le vrai prénom de l'actrice qui joue Lisa Kudrow dans Friends ?")
drop(S, "Comment Joey prépare-t-il ses sandwichs préférés dans la série ?")
fix(S, "Quel personnage récurrent de Friends est la mère extravagante de Chandler ?",
    fb="Nora Tyler Bing, jouée par Morgan Fairchild, est la mère de Chandler, une romancière extravagante. Elle embarrasse son fils en embrassant Ross.")
drop(S, "Quel personnage dit souvent des choses sages mais completement inexactes factuelment ?")
fix(S, "Quel épisode est diffusé en direct sur NBC en 2020 pour les 25 ans de Friends ?",
    q="Comment s'appelle l'émission de retrouvailles des acteurs diffusée en 2021 ?",
    a=["The One Where They Say Goodbye", "Friends Forever", "Friends: The Reunion", "The Last One"], c=2)
fix(S, "Quel est le nom du canard que Joey et Chandler achètent impulsivment ?",
    q="Comment Joey et Chandler appellent-ils leur canard ?",
    fb="Joey et Chandler adoptent un poussin puis un canard, qu'ils appellent simplement « le Poussin » et « le Canard ».")
fix(S, "Quel est le problème récurrent de Monica avec la propreté et l'ordre ?",
    fb="Monica est obsédée par la propreté et l'ordre. Le moindre désordre la stresse, ce qui fait d'elle la cible de nombreuses blagues de ses amis.")
drop(S, "Dans quelle ville Ross et Rachel se marient-ils accidentellement ?")
drop(S, "Quel personnage dit la réplique 'I'm fine!' (avec un sous-texte évident qu'il ne l'est pas) ?")
drop(S, "Comment s'appelle la sonnerie du téléphone chez Joey et Chandler à la façon d'une sitcom ?")
fix(S, "Quel acteur joue le père de Ross et Monica ?",
    a=["Ron Leibman", "James Lesure", "Tom Selleck", "Elliott Gould"], c=3,
    fb="Elliott Gould joue Jack Geller, le père de Ross et Monica. Sa femme Judy est jouée par Christina Pickles.")
drop(S, "Quel personnage raconte souvent des 'fun facts' ennuyeux pour tout le monde sauf lui ?")
drop(S, "Comment s'appelle le café du bloc Ugly Naked Guy (l'homme nu laid) dans Friends ?")
fix(S, "Quel est le nom du colocataire de Joey dans les saisons tardives après que Chandler parte ?",
    q="Avec quel colocataire étrange Chandler vit-il quand Joey déménage, en saison 2 ?",
    a=["Gunther", "Chuck", "Eddie", "Danny"], c=2,
    fb="Quand Joey part vivre seul, Chandler se retrouve avec Eddie, joué par Adam Goldberg, un colocataire de plus en plus inquiétant.")
drop(S, "Comment s'appelle la série télévisée fictive dans laquelle Rachel est fan dans les premières saisons ?")
fix(S, "Comment s'appelle le singe de Ross qu'il doit finalement donner à un zoo ?",
    fb="Marcel, le capucin de Ross, finit par lui poser trop de problèmes. Ross le confie à un zoo de San Diego.")
drop(S, "Quel épisode see les six amis bloqués à la campagne avant le mariage de Ross et Emily ?")
drop(S, "Combien de fois Chandler Bing rompt-il avec une petite amie avant Monica ?")
fix(S, "Quel est le nom de la mère biologique de Phoebe avec qui elle se reconnecte dans la série ?",
    a=["Frances", "Lily", "Phoebe Abbott", "Ursula"], c=2,
    fb="Phoebe découvre que sa mère biologique est Phoebe Abbott, une amie de ses parents qui porte le même prénom qu'elle.")
fix(S, "Quel pays Rachel visite-t-elle pour un stage de mode dans une saison intermédiaire ?",
    q="Dans quelle ville Rachel doit-elle partir travailler à la fin de la série ?",
    a=["Paris", "Milan", "Londres", "Los Angeles"], c=0)
drop(S, "Comment s'appelle le chant à plusieurs voix que Joey et Chandler font pour se 'défier' ?")
fix(S, "Quel est le dernier dialogue de la série Friends dans le dernier épisode ?",
    fb="Rachel propose d'aller boire un café une dernière fois, et Chandler répond « Where? » (« Où ça ? »), clin d'œil au Central Perk tout proche.")


# ---------------------------------------------------------------- La Casa de Papel
S = 'casapapel'
fix(S, "Quelle institution est attaquée dans le premier braquage (saisons 1-2) ?",
    fb="La bande s'enferme dans la Maison de la Monnaie d'Espagne pour y imprimer ses propres billets : selon le Professeur, ils ne volent l'argent de personne.")
drop(S, "Quelle est la signification des noms de villes choisis par le Professeur pour la bande ?")
drop(S, "Quel pays produit La Casa de Papel ?")
fix(S, "Quel est le plan de diversion du Professeur pour le braquage de la Monnaie ?",
    q="Quel est le plan du Professeur pour le braquage de la Maison de la Monnaie ?",
    fb="Le plan consiste à tenir le bâtiment avec des otages pendant plusieurs jours pour imprimer environ 2,4 milliards d'euros.")
drop(S, "Quel est le montant total imprimé lors du premier braquage de la Maison de la Monnaie ?")
drop(S, "Quel personnage porte le numéro tatouage '2000' sur le cou ?")
drop(S, "Qui joue Tokyo, la narratrice de la série ?")
drop(S, "Quel personnage joue Úrsula Corberó dans La Casa de Papel ?")
fix(S, "Quel personnage porte le nom de ville 'Helsinki' ?",
    q="Qui est Helsinki dans la bande ?",
    a=["Un ancien soldat serbe, colosse au grand cœur", "Le hacker du groupe", "L'expert en explosifs", "La conductrice des véhicules"], c=0,
    fb="Helsinki est un ancien soldat serbe, cousin d'Oslo. Ce colosse sert de « muscle » à la bande, mais se montre très protecteur avec ses camarades.")
fix(S, "Quelle est la nationalité du personnage 'Helsinki' dans la série ?", c=2,
    fb="Malgré leurs noms de villes nordiques, Helsinki et Oslo sont deux cousins serbes, anciens soldats.")
fix(S, "Quel est le vrai nom du Professeur dans la série ?",
    fb="Le Professeur s'appelle Sergio Marquina. Son père, braqueur, est mort pendant un braquage, et Sergio a passé des années à préparer le plan de la Maison de la Monnaie.")
drop(S, "Quel est le plan de diversion du Professeur quand les forces spéciales encerclent la Banque d'Espagne ?")
drop(S, "Quel acteur joue le Professeur dans La Casa de Papel ?")
drop(S, "Quel acteur joue Berlin dans la série ?")
drop(S, "Dans quelle ville se situe la Banque d'Espagne, cible du second braquage ?")
drop(S, "Dans quelle ville espagnole a été principalement tournée la série ?")
drop(S, "Quelle série dérivée de La Casa de Papel se concentre sur le frère du Professeur avant les braquages ?")
drop(S, "Comment la bande neutralise-t-elle les caméras de surveillance lors du premier braquage ?")
drop(S, "Quel est le lien entre Moscow et Denver dans la série ?")
fix(S, "Quel est l'emploi de Monica Gaztambide avant d'être prise en otage ?", c=2,
    fb="Mónica Gaztambide est la secrétaire d'Arturo Román, le directeur de la Maison de la Monnaie, dont elle attend un enfant.")
drop(S, "Pourquoi Nairobi est-elle particulièrement populaire auprès du public ?")
drop(S, "Quelle est la devise de résistance qui symbolise le mouvement dans la série ?")
drop(S, "Combien de membres compte la bande originale pour le premier braquage de la Monnaie ?")
drop(S, "Quel est le plan du Professeur quand il dit 'avoir un plan Z' ?")
drop(S, "Quelle technique visuelle distinctive identifie les flashbacks dans La Casa de Papel ?")
drop(S, "Quel est le signal que les membres utilisent pour indiquer qu'ils doivent annuler l'opération ?")
fix(S, "Comment Nairobi meurt-elle dans la série ?",
    a=["Elle s'échappe", "Elle est exécutée par Gandía, le chef de la sécurité de la banque", "Elle se sacrifie", "Elle est arrêtée"], c=1,
    fb="Pendant le braquage de la Banque d'Espagne, Gandía, le chef de la sécurité, parvient à s'emparer de Nairobi et l'abat. Sa mort, dans la partie 4, bouleverse la bande.")
drop(S, "Quel message politique le Professeur revendique-t-il lors du premier braquage via les médias ?")
drop(S, "Quel est le pays depuis lequel le Professeur dirige les opérations à distance ?")
fix(S, "Quel est le lien entre Berlin et le Professeur révélé dans la série ?",
    a=["Ils sont collègues", "Ils sont frères", "Ils sont père et fils", "Ils sont amis d'enfance"], c=1,
    fb="Berlin, Andrés de Fonollosa, est le frère aîné du Professeur. Ce lien explique la confiance que Sergio lui accorde malgré son comportement imprévisible.")
drop(S, "Comment s'appelle le mode de communication utilisé par le Professeur avec la bande ?")
fix(S, "Quel événement traumatisant dans le passé de Berlin est révélé dans ses flashbacks ?",
    q="De quelle maladie Berlin souffre-t-il ?",
    a=["Il n'est pas malade", "Une maladie incurable, la myopathie de Helmer", "Une maladie cardiaque", "Il est devenu aveugle"], c=1,
    fb="Berlin est atteint d'une maladie dégénérative incurable, la myopathie de Helmer. Se sachant condamné, il affronte la mort avec un étrange détachement.")
drop(S, "Quel élément du plan du Professeur implique le gouvernement espagnol directement ?")
fix(S, "Comment s'appelle le policier qui remplace Raquel Murillo comme négociateur dans la saison 3 ?",
    q="Quelle policière remplace Raquel Murillo comme négociatrice lors du braquage de la Banque d'Espagne ?",
    a=["Alicia Sierra", "Mónica Gaztambide", "Ariadna Cascales", "Amanda"], c=0)
fix(S, "Quel membre de la bande est un expert en moteurs et mécanique ?",
    q="Quel membre de la bande, ancien mineur, creuse le tunnel de la Maison de la Monnaie ?",
    fb="Moscou, ancien mineur et père de Denver, creuse le tunnel d'évasion pendant le premier braquage. Il est mortellement touché au moment de la fuite.")
drop(S, "Quel est le plan secret que Berlin avait en cas d'assaut policier dans la Monnaie ?")
drop(S, "Qui découvre que le Professeur et Raquel Murillo sont en couple pendant le premier braquage ?")
drop(S, "Quel est l'objet symbolique que Tokyo laisse à Rio avant sa mort ?")
drop(S, "Quel objet symbolique Tokyo conserve-t-elle de Rio tout au long de la série ?")
drop(S, "Qui révèle l'identité du Professeur aux autorités en trahissant la bande ?")
drop(S, "Quel est le vrai objectif philosophique du Professeur selon sa propre déclaration ?")
fix(S, "Quel est le prénom du fils de Denver et Monica dans la série ?",
    q="Comment s'appelle le fils de Mónica, élevé par Denver ?",
    fb="Mónica, devenue Stockholm, a un fils, Cincinnati, dont le père biologique est Arturo Román. Denver l'élève comme son propre fils.")
drop(S, "Que signifie le fait que la bande porte des masques de Salvador Dalí spécifiquement ?")
drop(S, "Dans quel pays se retrouvent les membres de la bande après le premier braquage réussi ?")
drop(S, "Combien de jours dure environ le premier braquage de la Maison de la Monnaie ?")
drop(S, "Quel est le dernier plan du Professeur si toute la bande est capturée ou tuée ?")
drop(S, "Quel crime Alicia Sierra commet-elle contre le Professeur quand elle le retrouve seul ?")
drop(S, "Quel est le nom de code utilisé par la bande pour identifier chaque membre dans les communications radio ?")
drop(S, "Quel est le geste symbolique que la bande et les supporters font les bras en croix ?")


# ---------------------------------------------------------------- Squid Game
S = 'squidgame'
drop(S, "Quel est le nombre total de wons gagnés par round d'élimination dans Squid Game ?")
fix(S, "Quel uniforme portent les Gardiens ?",
    fb="Les gardes portent une combinaison rose et un masque marqué d'une forme : le cercle pour les ouvriers, le triangle pour les soldats armés et le carré pour les responsables.")
fix(S, "Quel est le symbole sur les costumes des Gardiens indiquant le rang de superviseur ?",
    q="Quelle forme figure sur le masque des responsables, les plus hauts gradés parmi les gardes ?",
    fb="Le carré désigne les responsables, au-dessus des soldats (triangle) et des ouvriers (cercle). Le Front Man, lui, porte un masque noir.")
fix(S, "Quel symbole géométrique représente chaque grade dans la hiérarchie des Gardiens ?",
    a=["Cercle = ouvrier, triangle = soldat, carré = responsable", "Carré = soldat, triangle = responsable, cercle = ouvrier", "Cercle = responsable, triangle = ouvrier, carré = soldat", "Étoile = chef, cercle = garde, triangle = recruteur"], c=0,
    fb="Le cercle désigne les ouvriers, le triangle les soldats armés et le carré les responsables. Le Front Man est au-dessus de tous.")
fix(S, "Combien de joueurs participent en saison 1 ?",
    fb="456 joueurs, tous lourdement endettés, participent aux jeux. Le dernier numéro est celui de Gi-hun, qui finira par gagner.")
drop(S, "Quel jeu implique traverser des plaques de verre au-dessus du vide ?")
drop(S, "Quel jeu implique des partenaires où l'un doit marcher sur un planche de verre au-dessus du vide ?")
drop(S, "Quel est le résultat final du vote pour arrêter ou continuer les jeux en saison 1 ?")
drop(S, "Dans quelle saison Gi-hun affronte-t-il les organisateurs directement ?")
drop(S, "Quelle est la nationalité de Gi-hun dans la saison 2 quand il décide de ne pas rentrer aux USA ?")
drop(S, "Qui est le vrai 'joueur 001' dans la saison 2 de Squid Game ?")
drop(S, "Qui recrute les candidats pour Squid Game en leur faisant jouer au Ddakji dans les lieux publics ?")
fix(S, "Quel est l'enjeu de la scène post-crédit de la saison 1 qui setup la saison 2 ?",
    q="Que voit Gi-hun à la fin de la saison 1, juste avant de prendre l'avion ?",
    a=["Une nouvelle invitation dans sa poche", "Le recruteur du métro en train de piéger un autre homme au ddakji", "Le Front Man sans son masque", "Sang-woo vivant"], c=1,
    fb="Dans le métro, Gi-hun aperçoit le recruteur qui joue au ddakji avec un nouvel homme. Il comprend que les jeux continuent, renonce à son avion et décide d'agir.")
fix(S, "Quel type de costume porte le Frontman dans Squid Game ?",
    a=["Une combinaison rose", "Une tenue noire et un masque noir anguleux", "Une combinaison dorée", "Des vêtements civils"], c=1,
    fb="Le Front Man porte une tenue noire et un masque noir anguleux, qui le distinguent des gardes en rose.")
drop(S, "Comment se nomme le VIP numéro 1 aux masques d'animaux dans Squid Game ?")
drop(S, "Comment s'appelle la chanson que les poupées géante chante lors du premier jeu ?")
drop(S, "Comment s'appelle l'acteur principal coréen qui joue Gi-hun (joueur 456) ?")
drop(S, "Quel est le jeu coréen traditionnel avec une corde où les deux équipes tirent ?")
drop(S, "Quelle est la règle principale qui force les joueurs à rester dans le jeu selon leur contrat signé ?")
drop(S, "Quel acteur américain est apparu brièvement comme VIP dans Squid Game saison 1 ?")
fix(S, "Comment s'appelle la petite fille qui joue 1, 2, 3 Soleil avec Gi-hun lors d'un flashback ?",
    q="Comment s'appelle la fille de Gi-hun ?",
    a=["Ga-yeong", "Sae-byeok", "Ji-yeong", "Mi-nyeo"], c=0)
drop(S, "Quel est le rôle du policier Hwang Jun-ho tout au long de la saison 1 ?")
drop(S, "Quel est le rapport entre les vêtements roses des Gardiens et le vert des joueurs ?")
drop(S, "Que se passe-t-il quand un participant touche la ligne d'arrivée dans le jeu 1,2,3 Soleil ?")
fix(S, "Comment Gi-hun parvient-il à gagner le jeu de billes contre Oh Il-nam ?",
    a=["Par la force", "En trichant ouvertement", "En profitant de l'apparente confusion du vieil homme", "Par chance pure"], c=2,
    fb="Gi-hun profite de la confusion apparente d'Oh Il-nam pour lui prendre ses billes. On comprendra plus tard que le vieil homme savait parfaitement ce qu'il faisait.")
fix(S, "Quelle est la profession originale de Gi-hun avant les jeux ?",
    a=["Vendeur ambulant", "Ancien ouvrier automobile licencié", "Ouvrier de chantier", "Chauffeur de taxi"], c=1)
fix(S, "Quelle est la réaction de Gi-hun quand il reçoit son argent et retourne dans le monde réel ?",
    fb="Traumatisé, Gi-hun ne touche presque pas à l'argent pendant un an et vit rongé par la culpabilité. Sa mère est morte pendant son absence.")
drop(S, "Dans quelle mer fictive ou réelle se situe l'île secrète des Squid Games ?")
fix(S, "Quel est le symbole de la série Squid Game représentant une poupée géante ?",
    q="Comment s'appelle la poupée géante du jeu 1, 2, 3 Soleil ?",
    a=["Young-hee", "Mi-nyeo", "Danbi", "Ji-yeong"], c=0,
    fb="La poupée géante s'appelle Young-hee, un prénom tiré de vieux manuels scolaires coréens. Elle est devenue l'emblème visuel de la série.")
drop(S, "Quel est le nom de la figurine géante coréenne qui détecte les participants en mouvement dans le premier jeu de Squid Game ?")
fix(S, "Quel est le 3ème jeu joué en saison 1 après 1,2,3 Soleil et Dalgona Cookie ?",
    fb="Le troisième jeu est le tir à la corde, au-dessus du vide. L'équipe de Gi-hun gagne grâce aux conseils d'Oh Il-nam et à l'idée de Sang-woo de faire trois pas en avant.")
drop(S, "Pourquoi le joueur 001 (Oh Il-nam) est-il révélé comme fondateur et non simple participant ?")
fix(S, "Quel est le jeu du premier round en saison 2 de Squid Game ?",
    a=["1, 2, 3 Soleil, à nouveau", "Le Dalgona", "Le tir à la corde", "Les billes"], c=0)
drop(S, "Comment le plateau de jeux est-il organisé physiquement selon les révélations de la série ?")
fix(S, "Combien de saisons de Squid Game ont été produites ou annoncées jusqu'en 2025 ?",
    q="Combien de saisons compte Squid Game ?", a=["1", "2", "3", "4"], c=2,
    fb="Squid Game compte trois saisons : la première en 2021, la deuxième en décembre 2024 et la dernière en juin 2025.")
fix(S, "Quelle technique Gi-hun utilise-t-il pour le jeu Dalgona Cookie avec l'étoile ?",
    q="Quelle astuce Gi-hun utilise-t-il pour découper le parapluie de son Dalgona ?",
    a=["Il mange le caramel", "Il lèche le dos du biscuit pour le ramollir", "Il souffle dessus", "Il utilise une épingle à cheveux"], c=1,
    fb="Gi-hun a tiré la forme la plus difficile, le parapluie. En léchant le dos du biscuit, il fait fondre le sucre et parvient à détacher la forme.")
drop(S, "Quel est le lien entre les Squid Games et la société fictive du VIP numéro 1 ?")
drop(S, "Dans quelle circonstance le joueur 001 est-il révélé comme n'étant pas soumis au danger ?")
drop(S, "Quel son caractéristique s'entend quand la poupée Young-hee détecte un mouvement ?")
fix(S, "Quel est le budget de production estimé par épisode pour Squid Game saison 1 ?",
    fb="La saison 1 aurait coûté environ 21 millions de dollars, soit un peu plus de 2 millions par épisode, un budget modeste pour la série la plus regardée de Netflix.")


# ---------------------------------------------------------------- Musique
S = 'musique'
drop(S, "Quel artiste français est le plus streamé au monde parmi les francophones ?")
fix(S, "Quel groupe de rock a sorti 'Dark Side of the Moon' en 1973 ?",
    fb="The Dark Side of the Moon (1973) est resté plus de 900 semaines au classement Billboard 200, un record. On y trouve « Money » et « Time ».")
fix(S, "Quel est le vrai prénom d'Aya Nakamura ?",
    q="Quel est le vrai nom d'Aya Nakamura ?",
    fb="Aya Nakamura s'appelle Aya Danioko. Née à Bamako, elle a grandi à Aulnay-sous-Bois et a emprunté son nom de scène à un personnage de la série Heroes.")
drop(S, "Quel rappeur de Marseille est connu comme le 'Duc de Boulogne' mais vient de Boulogne-Billancourt ?")
fix(S, "Quel rappeur français est surnommé 'Le Duc de Boulogne' ?",
    fb="Booba (Élie Yaffa), originaire de Boulogne-Billancourt, est surnommé le « Duc de Boulogne ». Révélé dans les années 1990 avec le duo Lunatic, il a marqué durablement le rap français.")
fix(S, "Quel festival de metal se tient à Clisson chaque été en France ?",
    fb="Le Hellfest, à Clisson (Loire-Atlantique), est le plus grand festival de metal de France. Il accueille chaque été les grands noms du genre.")
fix(S, "Quel rappeur français de Sevran est connu pour son style brut et ses albums 'Réel'?",
    q="Quel rappeur de Sevran a sorti l'album « Réelle Vie » ?",
    fb="Maes, rappeur de Sevran, s'est imposé avec « Réelle Vie » puis « Les Derniers Salopards ».")
fix(S, "Quel rappeur français a sorti l'album 'Civilisation' et est connu pour sa rime multisyllabique ?",
    q="Quel rappeur caennais a sorti l'album « Civilisation » en 2021 ?",
    fb="Orelsan, originaire de Caen, a sorti « Civilisation » en 2021, récompensé aux Victoires de la Musique. « L'odeur de l'essence » en est l'un des titres phares.")
drop(S, "Quel chanteur français est connu pour ses albums 'Civilisation' et 'Perdu d'avance' ?")
fix(S, "Quel est l'album considéré comme le meilleur de Damso ?",
    q="Quel album de Damso, sorti en 2017, contient « Macarena » ?",
    fb="« Ipséité » (2017) est le deuxième album de Damso. Il contient « Macarena » et a été salué pour son introspection.")
fix(S, "Quel groupe de hip-hop français des années 90 est considéré comme pionnier ?",
    q="Quel groupe de rap de Seine-Saint-Denis est formé par JoeyStarr et Kool Shen ?",
    a=["Arsenik", "Sniper", "Psy 4 de la Rime", "Suprême NTM"], c=3,
    fb="Suprême NTM, formé par JoeyStarr et Kool Shen, est avec IAM l'un des groupes fondateurs du rap français. « Paris sous les bombes » est un album culte.")
fix(S, "Quel est le vrai prénom du rappeur connu sous le nom de 'SCH' ?",
    q="Quel est le vrai nom du rappeur SCH ?",
    fb="SCH s'appelle Julien Schwarzer. Ce rappeur marseillais est l'auteur d'« A7 », d'« Anarchie » et de « JVLIVS ».")
fix(S, "Quel groupe américain a sorti 'Bohemian Rhapsody', l'une des chansons les plus complètes de l'histoire ?",
    q="Quel groupe britannique a sorti « Bohemian Rhapsody » en 1975 ?")
fix(S, "Quel est le vrai nom de l'artiste connu sous le pseudonyme 'Drake' ?",
    fb="Drake s'appelle Aubrey Drake Graham. Né à Toronto en 1986, il a débuté comme acteur dans la série Degrassi avant de devenir l'un des rappeurs les plus écoutés au monde.")
drop(S, "Quel artiste a popularisé le style 'trap music' en France avec ses 'tapes' ?")
drop(S, "Quel artiste a popularisé le genre 'trap' en France avec ses 'street tape' au milieu des années 2010 ?")
fix(S, "Quel est le vrai nom de l'artiste connu sous le pseudonyme 'Stromae' ?",
    a=["Paul Van Haver", "Tom Van Haver", "Luc Vandamme", "Léo Schivers"], c=0)
fix(S, "Quel groupe français des années 2000 a sorti 'Je veux te voir' et 'Safari Disco Club' ?",
    fb="Yelle est un groupe d'électropop français mené par la chanteuse Julie Budet. « Je veux te voir » (2006) les a révélés, et « Safari Disco Club » (2011) les a fait connaître à l'étranger.")
drop(S, "Quel rappeur québécois a popularisé le rap francophone au Canada ?")
drop(S, "Quel est le nom du collectif de rap belge dont Damso fait partie ?")
fix(S, "Quel festival de musique électronique éco-responsable se tient au Bois de Vincennes à Paris ?",
    q="Quel festival éco-responsable se tient chaque année au bois de Vincennes, à Paris ?",
    fb="We Love Green, créé en 2011, se déroule au bois de Vincennes. Il met l'accent sur l'environnement et accueille des têtes d'affiche du rap, de la pop et de l'électro.")
fix(S, "Quel artiste a vendu le plus de singles physiques en France selon le SNEP ?",
    q="Quel chanteur est souvent présenté comme l'artiste ayant vendu le plus de disques en France ?",
    fb="Johnny Hallyday aurait vendu plus de 100 millions de disques au cours de sa carrière. « Allumer le feu » et « Je te promets » font partie de ses grands succès.")
drop(S, "Quel est l'artiste qui a le plus de disques certifiés en France (singles + albums combinés) ?")
fix(S, "Quel groupe de metal français a sorti 'Sepultura Style' et est mondialement reconnu ?",
    q="Quel groupe de metal français, originaire des Landes, est reconnu dans le monde entier ?",
    a=["Gojira", "Trust", "Mass Hysteria", "Mastodon"], c=0,
    fb="Gojira, formé dans les Landes par les frères Duplantier, est le groupe de metal français le plus connu au monde. Il a joué lors de la cérémonie d'ouverture des Jeux de Paris 2024.")
drop(S, "Quel est le premier album de rap français à être certifié disque d'or en France ?")
drop(S, "Quel est le genre musical créé par Afrika Bambaataa dans le Bronx dans les années 70 ?")
drop(S, "Quel chanteur belge est connu pour 'Quand c'est ?' et 'Fils de joie' dans les années 90 ?")
fix(S, "Quel duo français de musique électronique, masqué de casques robotiques, a révolutionné la house music dans les années 2000 ?",
    q="Quel duo français de musique électronique se produisait caché sous des casques de robots ?")
fix(S, "Quel est le nom du groupe de rock alternatif français connu pour 'Le vent nous portera' ?",
    fb="Noir Désir, groupe bordelais, est l'un des groupes de rock français les plus marquants. « Le vent nous portera », « Tostaky » et « Un jour en France » font partie de ses titres emblématiques.")
drop(S, "Quel rappeur français a sorti le premier album rap certifié disque de diamant en France ?")
fix(S, "Quel est le nom de l'archipel d'îles où est né le style musical reggae ?",
    q="Dans quel pays est né le reggae ?")
fix(S, "Quel chanteur africain a popularisé le genre 'Afrobeats' dans le monde entier dans les années 2010 ?",
    q="Quel chanteur nigérian a remporté en 2021 le Grammy du meilleur album de musique du monde avec « Twice as Tall » ?",
    a=["Burna Boy", "Wizkid", "Davido", "Youssou N'Dour"], c=0,
    fb="Burna Boy a remporté le Grammy du meilleur album de musique du monde en 2021 avec « Twice as Tall ». Il est l'une des grandes figures de l'afrobeats.")
drop(S, "Quel terme désigne une chanson dont la durée est spécifiquement adaptée à la radio (3-4 minutes) ?")
fix(S, "Quel est le nom du prix de musique américain équivalent français des Victoires de la Musique ?",
    q="Quels prix américains sont l'équivalent des Victoires de la Musique ?")
drop(S, "Quel artiste a popularisé le genre 'Lo-fi hip-hop' sur YouTube dans les années 2010 ?")
drop(S, "Quel est le nom de l'artiste qui a popularisé le 'drill' en France avec ses BM ?")
fix(S, "Quel album de Kanye West est souvent cité comme son chef-d'œuvre ?",
    q="Quel album de Kanye West, sorti en 2010, contient « Power » et « Runaway » ?")
drop(S, "Quel est le premier artiste français à avoir eu un numéro 1 aux USA en musique populaire ?")
drop(S, "Quel est le record mondial de streams en 24h sur Spotify détenu en 2024 ?")
drop(S, "Quel est le nom de l'artiste nigériane qui a popularisé l'Afropop avec 'Dangerous Love' ?")
drop(S, "Quel groupe de pop coréenne a popularisé la K-Pop en Occident en premier ?")
drop(S, "Quel est le mouvement musical des années 60 associé à des artistes comme Joan Baez et Pete Seeger ?")
fix(S, "Quel est le nom du producteur français qui a produit des albums pour Jay-Z et Kanye West ?",
    q="Quel producteur français a coproduit « Black Skinhead », sur l'album « Yeezus » de Kanye West ?",
    a=["Busy P", "DJ Snake", "Gesaffelstein", "Cassius"], c=2,
    fb="Gesaffelstein (Mike Lévy) a coproduit plusieurs titres de « Yeezus » (2013), dont « Black Skinhead ». Son électro sombre est sa signature.")
fix(S, "Quel est l'album de Rosalía qui a fusionné flamenco traditionnel et production moderne ?",
    fb="« El Mal Querer » (2018) mêle flamenco et production moderne. Cet album-concept s'inspire d'un roman occitan du XIIIe siècle et a valu à Rosalía deux Latin Grammy.")
fix(S, "Quel groupe de rock progressif britannique est connu pour 'Stairway to Heaven' ?",
    q="Quel groupe de rock britannique est connu pour « Stairway to Heaven » ?")
fix(S, "Quel est le nom du label de musique indépendant français qui a signé Daft Punk, Justice et Cassius ?",
    q="Quel label parisien, fondé par Pedro Winter, a révélé le duo Justice ?",
    fb="Ed Banger Records, fondé en 2003 par Pedro Winter (Busy P), a révélé Justice, SebastiAn et Breakbot.")
fix(S, "Quel artiste brésilienest connu pour avoir popularisé la Bossa Nova dans les années 60 ?",
    q="Quel artiste brésilien est considéré comme le père de la bossa nova ?")
fix(S, "Quel rappeur de la région parisienne est connu pour ses punchlines incisives et ses diss tracks ?",
    q="Quel rappeur d'Aulnay-sous-Bois est connu pour son humour décalé et l'album « Xeu » ?",
    fb="Vald, originaire d'Aulnay-sous-Bois, s'est fait connaître par son humour absurde et ses textes décalés, notamment avec « Agartha » et « Xeu ».")


# ---------------------------------------------------------------- Cinéma
S = 'cinema'
drop(S, "Quel film de Christopher Nolan mélange rêve et réalité avec Leonardo DiCaprio ?")
drop(S, "Quel film de 1975 de Steven Spielberg a fondé le genre 'summer blockbuster' ?")
drop(S, "Quel acteur a le plus d'apparitions dans le Marvel Cinematic Universe ?")
fix(S, "Qui détient le record du plus grand nombre de nominations aux Oscars (meilleure actrice) ?",
    q="Quelle actrice détient le record de nominations aux Oscars ?",
    fb="Meryl Streep compte 21 nominations aux Oscars et trois statuettes. Katharine Hepburn détient le record de victoires avec quatre Oscars.")
fix(S, "Quel réalisateur a créé la saga Star Wars originale ?",
    fb="George Lucas a créé Star Wars et réalisé le premier film en 1977. Il a vendu Lucasfilm à Disney en 2012 pour environ 4 milliards de dollars.")
drop(S, "Quel film de science-fiction de 1968 est considéré comme le plus influent du genre ?")
drop(S, "Quel film sud-coréen a remporté la Palme d'Or à Cannes en 2019 ?")
fix(S, "Quel réalisateur français est connu pour 'Le Fabuleux Destin d'Amélie Poulain' ?",
    fb="Jean-Pierre Jeunet a réalisé « Le Fabuleux Destin d'Amélie Poulain » (2001) avec Audrey Tautou, l'un des plus grands succès du cinéma français à l'étranger.")
fix(S, "Quel réalisateur est connu pour ses films à retournements de situation (M. Night Shyamalan) ?",
    q="Quels films ont été réalisés par M. Night Shyamalan ?")
fix(S, "Quel studio d'animation japonais a produit 'Le Voyage de Chihiro' et 'Mon Voisin Totoro' ?",
    fb="Le studio Ghibli a été fondé par Hayao Miyazaki, Isao Takahata et Toshio Suzuki. « Le Voyage de Chihiro » a remporté l'Oscar du meilleur film d'animation en 2003.")
drop(S, "Quel est le film de Pixar dans lequel un robot découvre la Terre abandonnée des siècles plus tard ?")
drop(S, "Quel film de Bong Joon-ho avec Song Kang-ho a marqué le cinéma coréen avant Parasite ?")
fix(S, "Quel film d'animation japonais met en scène un enfant qui découvre qu'il est le seul vrai humain dans un monde d'esprits ?",
    q="Dans quel film de Miyazaki une fillette voit-elle ses parents transformés en cochons ?",
    fb="Dans « Le Voyage de Chihiro » (2001), Chihiro se retrouve dans un monde d'esprits après la transformation de ses parents en cochons. Le film a reçu l'Ours d'or et l'Oscar du meilleur film d'animation.")
fix(S, "Quel réalisateur américain est connu pour ses films 'Dunkirk', 'Oppenheimer' et 'Inception' ?",
    q="Quel réalisateur britannique est connu pour « Dunkerque », « Inception » et « Oppenheimer » ?")
fix(S, "Quel film de James Cameron (2009) est resté le film le plus rentable de l'histoire pendant 11 ans ?",
    q="Quel film de James Cameron, sorti en 2009, est le plus gros succès de l'histoire du box-office ?",
    fb="Avatar a rapporté environ 2,9 milliards de dollars. Brièvement dépassé par Avengers: Endgame en 2019, il a retrouvé la première place grâce à une ressortie en 2021.")
fix(S, "Quel film de Ridley Scott (1979) a fondé le genre horreur science-fiction ?",
    q="Quel film de Ridley Scott, sorti en 1979, oppose l'officier Ripley à une créature dans un vaisseau ?")
fix(S, "Quel acteur a joué James Bond le plus longtemps dans l'histoire de la franchise ?",
    q="Quel acteur a incarné James Bond dans sept films officiels, de 1973 à 1985 ?",
    fb="Roger Moore a joué James Bond dans sept films, de « Vivre et laisser mourir » (1973) à « Dangereusement vôtre » (1985).")
fix(S, "Quel cinéaste japonais est souvent surnommé 'le Dieu du cinéma' et a créé 'Rashomon' ?",
    q="Quel cinéaste japonais a réalisé « Rashōmon » et « Les Sept Samouraïs » ?")
fix(S, "Quel film de Tim Burton (1988) a lancé la carrière de Michael Keaton avec une créature chaos ?",
    q="Quel film de Tim Burton, sorti en 1988, met en scène un « bio-exorciste » joué par Michael Keaton ?",
    fb="Dans « Beetlejuice » (1988), Michael Keaton joue un bio-exorciste déjanté. Une suite, « Beetlejuice Beetlejuice », est sortie en 2024.")
drop(S, "Quel est le budget estimé du film le plus cher jamais produit (en 2023) ?")
fix(S, "Quel est le nom du festival de cinéma espagnol le plus important après Cannes et Venise ?",
    q="Quel est le plus prestigieux festival de cinéma d'Espagne ?")
fix(S, "Quel film d'animation japonais (2013) de Makoto Shinkai a précédé 'Your Name' ?",
    q="Quel moyen-métrage de Makoto Shinkai, sorti en 2013, se déroule sous la pluie dans un jardin de Tokyo ?",
    fb="« The Garden of Words » (2013) raconte la rencontre d'un lycéen et d'une jeune femme qui se retrouvent les jours de pluie dans un jardin de Tokyo.")
fix(S, "Quel film franco-belge de 2011 a connu un succès phénoménal en France et a été adapté en USA ?",
    q="Quel film français de 2011 a été adapté aux États-Unis sous le titre « The Upside » ?",
    fb="« Intouchables » d'Olivier Nakache et Éric Toledano a attiré plus de 19 millions de spectateurs en France. Il raconte l'amitié entre Philippe, tétraplégique, et Driss, son auxiliaire de vie.")
fix(S, "Quel acteur américain est connu pour ses transformations physiques extrêmes ('The Machinist', 'American Hustle') ?",
    q="Quel acteur est connu pour ses transformations physiques extrêmes dans « The Machinist » et « American Hustle » ?",
    fb="Christian Bale a perdu près de 30 kg pour « The Machinist » (2004), avant de reprendre beaucoup de poids pour jouer Batman, puis pour « American Hustle ».")
fix(S, "Quel film espagnol de Guillermo del Toro (2006) se déroule pendant la guerre civile espagnole ?",
    q="Quel film de Guillermo del Toro, sorti en 2006, se déroule dans l'Espagne franquiste ?")
fix(S, "Quel film d'animation de Pixar met en scène un rat rêvant de devenir cuisinier à Paris ?",
    fb="Dans « Ratatouille » (2007), Rémy, un rat passionné de cuisine, s'associe à Linguini, un jeune commis maladroit du restaurant Gusteau.")
fix(S, "Quel film de Francis Ford Coppola est souvent cité comme le meilleur film américain jamais réalisé ?",
    q="Quel film de Francis Ford Coppola, sorti en 1972, met en scène la famille Corleone ?",
    fb="« Le Parrain » (1972) est régulièrement cité parmi les plus grands films de l'histoire. Sa suite, « Le Parrain, 2e partie », a aussi remporté l'Oscar du meilleur film.")
fix(S, "Quel film d'animation japonais de 2016 sur un garçon sourd a pleuré des millions de spectateurs ?",
    q="Quel film d'animation japonais de 2016 raconte la rédemption d'un garçon qui a harcelé une camarade sourde ?",
    fb="« A Silent Voice » (2016), réalisé par Naoko Yamada d'après le manga de Yoshitoki Ōima, suit Shōya, qui cherche à se faire pardonner d'avoir harcelé Shōko, une élève sourde.")
fix(S, "Quel acteur américain a joué dans 'Léon' et est devenu une légende du cinéma d'action français ?",
    q="Quel acteur français, né à Casablanca, joue le rôle-titre de « Léon » ?",
    fb="Jean Reno, né à Casablanca, est devenu une star internationale avec « Léon » (1994). Il a ensuite tourné dans « Mission impossible » et « Da Vinci Code ».")


# ---------------------------------------------------------------- Géographie
S = 'geo'
fix(S, "Quel est le pays le plus long du monde du nord au sud ?",
    q="Quel pays très étroit s'étire sur plus de 4 000 km du nord au sud, le long du Pacifique ?")
fix(S, "Quelle est la plus grande île du monde ?",
    fb="Le Groenland est la plus grande île du monde, avec environ 2,1 millions de km². Ce territoire autonome rattaché au Danemark est recouvert à 80 % de glace. L'Australie, plus grande, est considérée comme un continent.")
drop(S, "Quel est le pays qui a la plus grande longueur de côtes au monde ?")
fix(S, "Quelle est la montagne la plus haute d'Afrique ?",
    fb="Le Kilimandjaro, en Tanzanie, culmine à 5 895 m. Ce volcan endormi est couronné de glaciers qui reculent avec le réchauffement climatique.")
fix(S, "Quelle est la capitale du Kazakhstan, plus grande ville d'Asie centrale ?",
    q="Quelle est la capitale du Kazakhstan ?",
    fb="Astana est la capitale du Kazakhstan depuis 1997. Elle s'est appelée Nour-Soultan de 2019 à 2022. Almaty reste la plus grande ville du pays.")
drop(S, "Quel est le nom du plus long fleuve d'Europe ?")
drop(S, "Quelle est la capitale de la Nouvelle-Zélande (souvent confondue avec Auckland) ?")
fix(S, "Quel est le pays le plus densément peuplé d'Afrique ?",
    q="Quel est le pays le plus densément peuplé d'Afrique continentale ?")
fix(S, "Quel est le seul pays d'Amérique du Sud à avoir le français comme langue officielle ?",
    q="Quel territoire d'Amérique du Sud a le français comme langue officielle ?")
fix(S, "Quelle est la capitale de la Thaïlande ?",
    fb="Bangkok est la capitale de la Thaïlande. Son nom officiel complet en thaï est l'un des plus longs noms de ville au monde.")
fix(S, "Quelle est la seule mer fermée (sans accès à l'océan) de la planète ?",
    q="Quel est le plus grand plan d'eau fermé de la planète, bien qu'on l'appelle « mer » ?")
fix(S, "Quel est le pays européen avec le plus de frontières terrestres ?",
    q="Quel pays de l'Union européenne a le plus de voisins terrestres ?",
    a=["Allemagne", "France", "Italie", "Autriche"], c=0,
    fb="L'Allemagne partage ses frontières avec neuf pays : Danemark, Pays-Bas, Belgique, Luxembourg, France, Suisse, Autriche, Tchéquie et Pologne.")
fix(S, "Quel est le pays avec le plus d'îles dans le monde ?",
    q="Quel est le plus grand archipel du monde ?",
    a=["Philippines", "Indonésie", "Japon", "Maldives"], c=1)
drop(S, "Quel est le détroit le plus étroit habituellement navigable entre deux pays ?")
fix(S, "Quel est le pays le plus petit du monde reconnu par l'ONU ?",
    q="Quel est le plus petit État du monde ?")
fix(S, "Quel est le désert le plus froid du monde (contrairement à son nom de désert chaud) ?",
    q="Quel est le désert le plus froid du monde ?")
fix(S, "Quelle est la capitale de l'Éthiopie ?",
    fb="Addis-Abeba, perchée à plus de 2 300 m d'altitude, est la capitale de l'Éthiopie. Elle accueille le siège de l'Union africaine.")
fix(S, "Quel est le nom de l'archipel portugais dans l'Atlantique Nord proche des Açores ?",
    q="Quel archipel portugais de l'Atlantique a pour capitale Funchal ?")
fix(S, "Quel est le seul pays d'Afrique qui n'a jamais été colonisé par une puissance européenne ?",
    q="Quels pays d'Afrique ont échappé à la colonisation européenne ?",
    a=["L'Éthiopie seule", "Le Liberia seul", "L'Éthiopie et le Liberia", "L'Afrique du Sud"], c=2,
    fb="L'Éthiopie, victorieuse de l'Italie à Adoua en 1896, et le Liberia, indépendant depuis 1847, ont échappé à la colonisation. L'Éthiopie a toutefois été occupée par l'Italie de 1936 à 1941.")
fix(S, "Quel pays possède le plus grand nombre de patrimoines UNESCO en 2024 ?",
    q="Quel pays compte le plus de sites inscrits au patrimoine mondial de l'UNESCO ?",
    fb="L'Italie compte le plus de sites inscrits au patrimoine mondial, juste devant la Chine.")
drop(S, "Quel est le pays d'Europe qui possède le plus long réseau ferroviaire ?")
fix(S, "Quel est le nom de la vaste plaine herbeuse qui s'étend en Amérique du Sud ?",
    q="Comment s'appellent les grandes plaines herbeuses d'Argentine ?")
fix(S, "Quel est le pays d'Asie du Sud dont la capitale est Sri Jayawardenepura Kotte ?",
    fb="Sri Jayawardenepura Kotte est la capitale administrative du Sri Lanka, tandis que Colombo reste la capitale commerciale et la plus grande ville.")
drop(S, "Quel est le seul pays arabe sans désert Sahara ?")
drop(S, "Quel pays d'Europe a le plus bas taux de natalité actuellement ?")
drop(S, "Quel est le nom de la chaîne de montagnes qui sépare l'Asie de l'Europe en Russie ?")
fix(S, "Quel est le nom de la fissure africaine qui divise le continent et crée un nouveau futur océan ?",
    q="Quelle immense faille de l'est de l'Afrique pourrait un jour donner naissance à un nouvel océan ?",
    fb="Le rift est-africain écarte lentement la plaque africaine. Dans des dizaines de millions d'années, la Corne de l'Afrique pourrait s'en détacher, séparée par un nouvel océan.")


# ---------------------------------------------------------------- League of Legends
S = 'lol'
drop(S, "Comment s'appelle la victoire par destruction de la base adverse ?")
fix(S, "Comment s'appelle le grand champion dragon invincible apparaissant en fin de partie ?",
    q="Comment s'appelle le dragon de fin de partie qui permet d'exécuter les ennemis affaiblis ?",
    a=["Méga Dragon", "Dragon Hextech", "Dragon ancestral (Elder Dragon)", "Dragon infernal"], c=2,
    fb="Le Dragon ancestral apparaît en fin de partie. Son buff permet d'exécuter les ennemis qui passent sous un certain seuil de points de vie.")
fix(S, "Quel champion LoL est connu pour sa capacité 'Saut Cosmique' et son rôle d'assassin ?",
    q="Quelle championne assassin réinitialise ses compétences à chaque élimination ?")
fix(S, "Quel est le sort d'invocateur le plus utilisé, donnant un boost de vitesse ?",
    q="Quel sort d'invocateur, le plus utilisé du jeu, téléporte le champion sur une courte distance ?")
drop(S, "Quel champion est surnommé 'La Lame Non Brisée' ?")
drop(S, "Comment s'appelle le poste de joueur qui est aussi le caster de la carte ?")
drop(S, "Comment s'appelle la monnaie in-game principale de League of Legends ?")
fix(S, "Qui est Faker dans l'univers esport de League of Legends ?",
    fb="Lee « Faker » Sang-hyeok, mid laner de T1, est considéré comme le meilleur joueur de l'histoire de LoL. Il détient le record de titres de champion du monde.")
drop(S, "Quel est le nom du personnage dans le lore LoL qui a fondé les Gardiens ?")
fix(S, "Quel champion LoL est un ninja avec des étoiles de lancer ?",
    q="Quel ninja yordle manie l'électricité et lance des shurikens ?")
fix(S, "Comment s'appelle la carte 2v2v2v2 de League of Legends ?",
    q="Quel jeu dérivé de LoL est un auto-battler pour huit joueurs ?")
fix(S, "Quel champion LoL est célèbre pour son rire maniaque et ses sorts de feu ?",
    q="Quel champion est un être de feu dont les sorts embrasent ses cibles ?")
drop(S, "Quel est le champion LoL le plus populaire / joué en compétitif historiquement ?")
drop(S, "Quel est le championnat le plus important de la LCK (Corée) ?")
fix(S, "Quel champion LoL parle du 'joug de la mortalité' et est un mage d'ombre ?",
    q="Quelle liche peut toucher tous les ennemis de la carte avec son ultime ?")
fix(S, "Quel champion LoL est un support enchanteresse avec des soins et des boucliers ?",
    q="Quelle support peut soigner tous ses alliés, partout sur la carte, avec son ultime ?")
drop(S, "Comment s'appelle le mode compétitif principal de League of Legends ?")
drop(S, "Quel est le terme pour un champion avec beaucoup de résistances et de vie ?")
drop(S, "Quel est le titre du premier champion LoL jamais conçu ?")
fix(S, "Comment s'appelle le continent fictif où se déroule le lore de LoL ?",
    q="Comment s'appelle le monde où se déroule l'histoire de League of Legends ?")
drop(S, "Quel est le nom de la capacité passive universelle des champions LoL qui régénère en base ?")
drop(S, "Comment s'appelle le duo de support et ADC le plus populaire compétitivement en 2023 ?")
fix(S, "Comment s'appelle le système de classement juste en dessous de Challenger ?",
    q="Quel rang se trouve juste en dessous de Challenger ?",
    a=["Master", "Grandmaster", "Diamant I", "Émeraude"], c=1)
fix(S, "Quel champion LoL peut se diviser en plusieurs copies de lui-même ?",
    q="Quel champion clown crée une copie de lui-même avec son ultime, Hallucination ?")
fix(S, "Comment s'appelle la mécanique permettant à un champion de réduire les dégâts entrants ?",
    q="Quelle statistique réduit les dégâts physiques reçus ?",
    a=["L'armure", "La résistance magique", "La ténacité", "La vitesse d'attaque"], c=0)
fix(S, "Comment s'appelle la zone de réapparition des champions après leur mort ?",
    q="Comment s'appelle la zone de la base où les champions réapparaissent ?",
    a=["Le Nexus", "L'inhibiteur", "La Fontaine", "La Faille"], c=2)
drop(S, "Comment s'appelle la technique pour capitaliser sur un avantage en nombre (5v4) ?")
drop(S, "Comment s'appelle le personnage principal de la série Arcane (LoL) ?")
drop(S, "Comment s'appelle la mécanique de LoL qui accélère les champions à faible vie ?")
drop(S, "Comment s'appelle l'objet mythique le plus utilisé par les ADC en 2023 ?")
drop(S, "Comment s'appelle la fonction de chat entre alliés pendant une partie LoL ?")


# ---------------------------------------------------------------- Blue Lock
S = 'bluelock'
fix(S, "Quel est le talent naturel de Nagi Seishiro ?",
    fb="Nagi est un génie du contrôle de balle : il amortit n'importe quel ballon parfaitement. Il ne jouait au football que depuis quelques mois quand il est entré à Blue Lock.")
drop(S, "Quelle est la nationalité mixte de Kaiser Michael ?")
drop(S, "Comment Bachira résume-t-il pourquoi il est doué au football ?")
fix(S, "Pourquoi Sae Itoshi a-t-il brisé Rin émotionnellement dans le passé ?",
    a=["Il l'a blessé physiquement", "Il a renié leur rêve commun et lui a dit qu'il ne lui servait plus à rien", "Il a quitté le pays sans lui dire au revoir", "Il l'a humilié en public"], c=1,
    fb="De retour d'Espagne, Sae annonce à Rin qu'il abandonne leur rêve de devenir ensemble les meilleurs attaquants du monde, et le rejette durement. Depuis, Rin veut prouver qu'il peut le surpasser.")
drop(S, "Quel est l'arc de développement principal d'Isagi Yoichi ?")
drop(S, "Quel joueur de Blue Lock développe une technique basée sur l'anticipation des passes adverses ?")
drop(S, "Comment Rin Itoshi se distingue-t-il visuellement dans le manga ?")
fix(S, "Qui est le personnage qui enseigne à Isagi lors de la Neo Egoist League ?",
    q="Auprès de quel entraîneur, présenté comme le meilleur attaquant du monde, Isagi veut-il apprendre lors de la Neo Egoist League ?",
    a=["Rin Itoshi", "Noel Noa", "Bachira Meguru", "Barou Shouei"], c=1,
    fb="Isagi choisit Bastard München pour apprendre auprès de Noel Noa, l'attaquant considéré comme le meilleur du monde.")
drop(S, "Que se passe-t-il lors d'un 'duel direct' dans Blue Lock ?")
drop(S, "Quelle décision radicale Ego Jinpachi prend-il si un joueur ne développe pas son arme ?")
drop(S, "Quel aspect psychologique Blue Lock met-il en avant que peu de shōnens explorent ?")
drop(S, "Quelle est la caractéristique du style de frappe de Nagi une fois évolué ?")
drop(S, "Quelle philosophie s'oppose directement à celle d'Ego dans Blue Lock ?")
fix(S, "Quel club fictif Isagi Yoichi rejoint-il lors de la Neo Egoist League ?", c=1,
    fb="Isagi rejoint Bastard München, le club allemand entraîné par Noel Noa, où évolue Michael Kaiser. Leur rivalité y prend toute son ampleur.")
drop(S, "Comment l'anime Blue Lock est-il généralement classé parmi les animes sportifs ?")
drop(S, "Combien d'équipes sont formées dans la phase initiale des sélections de Blue Lock ?")
drop(S, "Combien de séries/arcs principaux compte Blue Lock environ ?")
fix(S, "Contre quelle équipe les Blue Lock All-Stars s'affrontent-ils dans un match clé ?",
    q="Contre quelle sélection les meilleurs joueurs de Blue Lock disputent-ils un match décisif pour l'avenir du programme ?",
    a=["L'équipe nationale japonaise A", "L'équipe nationale U-20 du Japon", "Bastard München", "Une sélection mondiale"], c=1,
    fb="Les joueurs de Blue Lock affrontent l'équipe nationale U-20 du Japon. Une défaite signerait la fin du programme.")
drop(S, "Que prouve le match Blue Lock All-Stars contre l'équipe nationale U-18 ?")
drop(S, "Quel est le contexte du premier match clé d'Isagi en duel contre Rin ?")
drop(S, "Quel élément rend les matchs de Blue Lock uniques par rapport aux autres mangas sportifs ?")
drop(S, "Quel résultat provoque la progression d'Isagi vers sa Meta-Vision complète ?")
drop(S, "Dans quel match Chigiri libère-t-il enfin sa vitesse sans retenue ?")
drop(S, "Quelle est la citation fondamentale d'Ego Jinpachi sur le football japonais ?")
drop(S, "Que dit Ego Jinpachi aux joueurs sur leur rôle en équipe ?")
drop(S, "Quelle citation d'Isagi résume son évolution ?")
drop(S, "Quelle maxime Barou Shouei se répète-t-il constamment ?")
drop(S, "Pourquoi Ego Jinpachi choisit-il des attaquants spécifiquement et non des joueurs polyvalents ?")
drop(S, "Quel est le sens du geste typique de Barou quand il marque un but ?")
drop(S, "Quel est l'arc émotionnel de Reo Mikage au fil du manga ?")
drop(S, "Qu'est-ce que Blue Lock cherche à détruire dans la mentalité japonaise du football ?")
drop(S, "Quel élément technique unique développe Isagi contre Kaiser ?")
drop(S, "Quel est le paradoxe central de Blue Lock comme programme national ?")
drop(S, "Quelle réaction mondiale a eu l'adaptation anime de Blue Lock ?")
drop(S, "Quel est l'ennemi intérieur principal d'Isagi au début de Blue Lock ?")
drop(S, "Comment se nomme la structure dans laquelle se déroule le programme Blue Lock ?")
drop(S, "Qu'est-ce qui rend le football de Blue Lock fondamentalement différent du football normal ?")
drop(S, "Quelle est la durée approximative du programme Blue Lock selon l'histoire ?")
drop(S, "Quel joueur de Blue Lock représente le mieux le concept de 'génie travailleur' par opposition au talent pur ?")
drop(S, "Quel personnage de Blue Lock incarne le mieux l'idée de 'football comme art' ?")
drop(S, "Quel est le message final du manga Blue Lock sur l'égoïsme ?")
drop(S, "Quelle technique Bachira développe-t-il pour surpasser ses limites physiques ?")
drop(S, "Qui est considéré comme le 'second Ego Jinpachi' dans les phases tardives de Blue Lock ?")
drop(S, "Quel aspect de l'arc d'Isagi dans la Neo Egoist League est le plus développé ?")
drop(S, "Quel personnage de Blue Lock symbolise le 'talent gâché par la peur' ?")
drop(S, "Quelle est la première victoire symbolique d'Isagi dans le programme ?")
drop(S, "Quel est le score général des mangas sportifs Blue Lock selon les charts japonais ?")


# ---------------------------------------------------------------- Solo Leveling
S = 'soloLeveling'
fix(S, "Qui est Yoo Jin-Ho dans Solo Leveling ?",
    a=["Un chasseur de rang S ennemi", "Un chasseur de rang D, fils de riche, qui devient le vice-président de la guilde de Jin-Woo", "Le directeur de l'Association des chasseurs", "Le frère de Sung Jin-Woo"], c=1,
    fb="Yoo Jin-Ho, chasseur de rang D et fils du patron d'une grande guilde, devient le fidèle bras droit de Jin-Woo et le vice-président de la guilde Ahjin.")
drop(S, "Quel Monarque se retrouve lié à Sung Il-Hwan (le père de Jin-Woo) ?")
drop(S, "Quel est le seul moment où Jin-Woo montre de la vraie peur ?")
drop(S, "Quel est le surnom international de Sung Jin-Woo une fois son pouvoir reconnu ?")
fix(S, "Quel est l'incident qui permet à Jin-Woo de recevoir le Système ?",
    a=["Un accident de voiture", "L'attaque d'un chasseur jaloux", "L'incident du Double Donjon", "L'ouverture d'un portail rouge"], c=2)
fix(S, "Comment s'appelle le premier et plus fidèle soldat-ombre de Jin-Woo ?",
    fb="Igris, le chevalier rouge, est l'un des premiers soldats-ombres de Jin-Woo. Vaincu lors de la quête de changement de classe, il le sert ensuite avec une loyauté absolue.")
fix(S, "Comment s'appellent les entités maléfiques qui veulent détruire l'humanité dans Solo Leveling ?",
    a=["Les Démons", "Les Monarques", "Les Portails maudits", "Les Chasseurs corrompus"], c=1,
    fb="Les Monarques, souverains des monstres, veulent anéantir l'humanité. Ils s'opposent aux Souverains, des êtres de lumière.")
fix(S, "Qui sont les Rulers dans Solo Leveling ?",
    q="Qui sont les Souverains (Rulers) dans Solo Leveling ?",
    a=["Les meilleurs chasseurs du monde", "Des êtres de lumière opposés aux Monarques", "Les ancêtres des chasseurs", "Les dirigeants de l'Association"], c=1,
    fb="Les Souverains sont des êtres de lumière en guerre contre les Monarques depuis des temps immémoriaux.")
drop(S, "Comment les Rulers communiquent-ils avec certains humains choisis ?")
drop(S, "Quel est le don particulier de Jin-Woo que les Rulers ont intégré dans le Système ?")
drop(S, "Quel titre Jin-Woo reçoit-il après avoir vaincu de nombreux Monarques ?")
drop(S, "Comment s'appelle l'événement qui a provoqué l'apparition des donjons et chasseurs sur Terre ?")
drop(S, "Quel est le rang minimum d'un donjon qui peut causer des victimes importantes ?")
fix(S, "Qu'est-ce qu'un 'donjon rogue' dans Solo Leveling ?",
    q="Que se passe-t-il quand un donjon n'est pas vidé à temps dans Solo Leveling ?",
    a=["Il se referme pour toujours", "Ses monstres sortent et envahissent la ville", "Il devient un donjon de rang S", "Rien de particulier"], c=1,
    fb="Si un donjon n'est pas nettoyé à temps, il « déborde » : les monstres sortent du portail et attaquent la ville.")
drop(S, "Qu'est-ce qu'un 'Portail Rogue' dans Solo Leveling ?")
drop(S, "Quel est l'arc considéré comme le plus intense de Solo Leveling ?")
drop(S, "Quel pays a une île entièrement envahie par des fourmis géantes dans Solo Leveling ?")
drop(S, "Quelle est la première grande victoire de la Ahjin Guild qui établit sa réputation ?")
drop(S, "Quel est le manhwa original dont Solo Leveling est l'adaptation ?")
fix(S, "Quel est le destin final de Sung Jin-Woo dans la conclusion de Solo Leveling ?",
    fb="Après avoir vaincu les Monarques, Jin-Woo utilise la Coupe de la réincarnation pour remonter le temps et offrir à tous une vie où la catastrophe n'a pas eu lieu.")
drop(S, "Quel événement final résout le conflit entre Monarques et Rulers dans Solo Leveling ?")
drop(S, "Quelle phrase résume la philosophie de Jin-Woo face aux obstacles ?")
drop(S, "Que répond Jin-Woo quand on lui demande pourquoi il risque sa vie dans les donjons ?")
drop(S, "Comment Jin-Woo est-il perçu par les autres chasseurs au début ?")
drop(S, "Que représente le Système pour Sung Jin-Woo par rapport aux autres chasseurs ?")
drop(S, "Quelle est la réaction d'Igris quand Jin-Woo le soumet pour la première fois ?")
drop(S, "Quelle est la récompense principale que Jin-Woo obtient en complétant des quêtes difficiles ?")
drop(S, "Comment Jin-Woo peut-il progresser alors que les autres chasseurs sont bloqués à leur rang ?")
drop(S, "Quel est le principe du 'Shadow Extraction' de Jin-Woo ?")
drop(S, "Quel est le niveau maximum que Jin-Woo peut atteindre avec le Système ?")
drop(S, "Quelle est la particularité de l'odorat de Cha Hae-In ?")
drop(S, "Quelle est la signification du titre 'Solo Leveling' ?")
drop(S, "Comment Jin-Woo finance ses activités de chasseur au début ?")
fix(S, "Quelle est la condition de la mère de Jin-Woo au début de l'histoire ?",
    a=["Elle est en bonne santé", "Elle est plongée dans un sommeil sans fin à cause d'une maladie liée à la magie", "Elle est morte avant l'histoire", "Elle est chasseuse à la retraite"], c=1,
    fb="La mère de Jin-Woo est atteinte du « sommeil éternel », une maladie liée à la magie qui la maintient endormie. Payer son hospitalisation est la première motivation de Jin-Woo.")
drop(S, "Quel est le rang du donjon où Jin-Woo obtient son premier vrai test physique après l'activation du Système ?")
drop(S, "Quelle est la popularité mondiale de Solo Leveling ?")
drop(S, "Comment appelle-t-on la capacité de Jin-Woo à percevoir les monstres à travers les murs et l'obscurité ?")
drop(S, "Comment la société coréenne traite-t-elle les chasseurs de rang E au début ?")
drop(S, "Quel est l'impact mondial des révélations sur Jin-Woo dans la communauté internationale des chasseurs ?")
drop(S, "Que représente l'armée des ombres de Jin-Woo symboliquement ?")
drop(S, "Quel est l'unique objet qui peut blesser sérieusement Jin-Woo à son pic de puissance ?")
drop(S, "Que font les autres chasseurs S-rank quand ils réalisent la vraie puissance de Jin-Woo ?")
drop(S, "Quelle nation est la plus agressive dans sa tentative de recruter Jin-Woo ?")
fix(S, "Comment se conclut la quête de Jin-Woo pour sauver sa mère hospitalisée ?",
    a=["Elle meurt avant de guérir", "Grâce à l'Élixir de vie obtenu dans le Château du démon", "Grâce à un soigneur de rang S", "Elle guérit naturellement"], c=1,
    fb="Jin-Woo gravit le Château du démon pour réunir les ingrédients de l'Élixir de vie, qui réveille enfin sa mère.")
drop(S, "Quel aspect du système de classement des chasseurs Solo Leveling critique-t-il implicitement ?")
fix(S, "Quelle est la relation entre Cha Hae-In et Jin-Woo à la fin de l'histoire ?",
    fb="Cha Hae-In et Jin-Woo finissent par former un couple et se marier. Elle est l'une des rares personnes à voir l'humain derrière sa puissance.")


# ---------------------------------------------------------------- Peaky Blinders
S = 'peakyBlinders'
drop(S, "Quel est le destin de la 'Shelby Company Limited' dans la série ?")
fix(S, "Combien de saisons compte Peaky Blinders ?",
    fb="Peaky Blinders compte six saisons, diffusées de 2013 à 2022. Un film prolonge ensuite l'histoire de Tommy Shelby.")
drop(S, "Quel événement historique traumatise Tommy Shelby ?")
drop(S, "Quel est le symbole/emblème visuel des Peaky Blinders ?")
fix(S, "Qui est Billy Kimber dans la saison 1 ?",
    a=["Un inspecteur de police", "Le chef d'un gang qui contrôle les champs de courses", "Un rival de la famille Lee", "Un fournisseur d'armes irlandais"], c=1)
fix(S, "Quelle maladie fatale Tommy apprend-il avoir dans la saison 6 ?",
    q="Quel diagnostic un médecin annonce-t-il à Tommy dans la saison 6 ?",
    fb="Un médecin annonce à Tommy un tuberculome au cerveau, censé être mortel. On découvrira à la fin que ce diagnostic était un mensonge.")
fix(S, "Quelle faction politique britannique Tommy soutient-il lors des saisons 2-3 ?",
    q="Pour quel parti Tommy Shelby devient-il député ?")
drop(S, "Quelle est la philosophie de Tommy Shelby face aux ennemis ?")
drop(S, "Quelle est la relation de Peaky Blinders avec la culture pop actuelle ?")
drop(S, "Quelle est la couleur associée à la garde-robe des Shelby ?")
drop(S, "Que représente les chevaux dans Peaky Blinders ?")
drop(S, "Quel personnage d'Alfie Solomons dit-il à Tommy lors de leur première rencontre ?")
drop(S, "Que représente Small Heath pour Tommy Shelby psychologiquement ?")
drop(S, "Quel est le vrai nom de naissance des Shelby ?")
drop(S, "Quel est le plan final de Tommy Shelby dans la saison 6 ?")
drop(S, "Quel est le rang social que Tommy cherche à atteindre au fil des saisons ?")
drop(S, "Quelle est la signature musicale caractéristique de la série ?")
drop(S, "Quel facteur psychologique Tommy ne peut-il jamais surmonter complètement ?")
drop(S, "Comment les Shelby gèrent-ils leur transition entre crime et politique ?")
drop(S, "Quel est l'impact cultural de Peaky Blinders sur la mode masculine ?")
drop(S, "Quel est l'héritage criminel exact de la famille Shelby à la fin de la série ?")
drop(S, "En quelle saison John Shelby est-il absent pour la première fois (mort) ?")
drop(S, "Quelle est la relation de Tommy Shelby avec la religion ?")
drop(S, "Quelle phrase Tommy dit-il quand quelqu'un le menace de mort ?")
drop(S, "Qu'est-ce qui distingue Peaky Blinders des autres drames criminels britanniques ?")
drop(S, "Quel personnage féminin est la principale voix de raison et de modération dans la famille Shelby ?")
drop(S, "Quel est le rapport de Tommy Shelby avec les courses de chevaux au-delà du business ?")
drop(S, "Quel sport Tommy pratique-t-il pour maintenir sa forme physique ?")
drop(S, "Quel est le paradoxe central de Tommy Shelby comme personnage ?")
drop(S, "Quel est le genre de la série Peaky Blinders ?")
drop(S, "Quelle est la progression de statut social des Shelby de la saison 1 à la fin ?")
drop(S, "Quel est le lien entre Peaky Blinders et le mouvement ouvrier de l'époque ?")
