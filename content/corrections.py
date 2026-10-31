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
