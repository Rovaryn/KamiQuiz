"""Métadonnées éditoriales des 42 séries.

key   : clé dans questions.json (gardée telle quelle pour compatibilité avec le classement)
slug  : segment d'URL (/quiz/<slug>/)
cat   : anime | series | films | jeux | culture
intro : deux paragraphes, faits vérifiables uniquement
"""

SERIES = [
    # ------------------------------------------------------------ ANIMÉS
    dict(key='naruto', slug='naruto', name='Naruto', cat='anime',
         tag="Ninjas, Bijû et Akatsuki, du Genin au Hokage à travers les deux parties.",
         intro=[
             "Publié par Masashi Kishimoto dans le Weekly Shōnen Jump de 1999 à 2014, Naruto raconte en 700 chapitres le parcours d'un orphelin de Konoha qui porte en lui le démon renard à neuf queues et rêve de devenir Hokage. Avec One Piece et Bleach, la série a formé ce que les lecteurs appellent le « Big Three » des années 2000.",
             "Le quiz couvre Naruto et Naruto Shippûden : l'Équipe 7, les clans de Konoha, les techniques (Rasengan, Chidori, Sharingan), l'Akatsuki et la Quatrième Grande Guerre ninja. Les questions faciles portent sur les personnages principaux, les plus difficiles sur les généalogies des clans et les détails des derniers arcs.",
         ]),
    dict(key='onepiece', slug='one-piece', name='One Piece', cat='anime',
         tag="Pirates, Fruits du Démon et Empereurs, sur la route de Laugh Tale.",
         intro=[
             "Commencé en 1997 par Eiichiro Oda, One Piece suit Monkey D. Luffy, un garçon au corps élastique qui veut trouver le trésor légendaire de Gol D. Roger et devenir le Roi des Pirates. Avec plus de 500 millions d'exemplaires publiés, c'est la bande dessinée la plus imprimée au monde pour un seul auteur.",
             "Le quiz parcourt la saga de l'East Blue jusqu'aux derniers arcs : l'équipage du Chapeau de paille, les Fruits du Démon et leurs trois familles, les Empereurs, la Marine, le Gouvernement mondial et les mystères du Siècle oublié. Les primes et les liens entre personnages sont le terrain des questions les plus pointues.",
         ]),
    dict(key='aot', slug='attack-on-titan', name='Attack on Titan', cat='anime',
         tag="Eren, Mikasa et les Titans, l'humanité derrière ses murs.",
         intro=[
             "Hajime Isayama a publié Attack on Titan (L'Attaque des Titans) de 2009 à 2021. Dans un monde où les derniers humains vivent retranchés derrière trois murs géants pour échapper aux Titans, Eren Jäger rejoint le Bataillon d'exploration après la chute du mur Maria. L'adaptation animée s'est achevée en 2023.",
             "Les questions couvrent les quatre saisons et le manga : les neuf Titans et leurs détenteurs, l'histoire d'Eldia et de Mahr, l'équipement tridimensionnel, les grandes révélations de la cave des Jäger et le dénouement. Une bonne mémoire des noms et des transmissions de pouvoirs fait la différence.",
         ]),
    dict(key='demonslayer', slug='demon-slayer', name='Demon Slayer', cat='anime',
         tag="Tanjirô, Nezuko et le Corps des pourfendeurs de démons.",
         intro=[
             "Kimetsu no Yaiba, connu en France sous le titre Demon Slayer, a été publié par Koyoharu Gotōge de 2016 à 2020. Dans le Japon de l'ère Taishō, Tanjirô Kamado rejoint le Corps des pourfendeurs pour venger sa famille et rendre son humanité à sa sœur Nezuko, transformée en démon. Le studio Ufotable en a tiré une adaptation saluée pour son animation.",
             "Le quiz porte sur les Souffles et leurs formes, les neuf Piliers, les Lunes démoniaques de Muzan Kibutsuji et les grands arcs, du mont Natagumo au château de l'Infini. Les détails des techniques et le passé humain des démons alimentent les questions difficiles.",
         ]),
    dict(key='bleach', slug='bleach', name='Bleach', cat='anime',
         tag="Ichigo, les shinigami et les Zanpakutō, entre deux mondes.",
         intro=[
             "Bleach, de Tite Kubo, a paru de 2001 à 2016. Ichigo Kurosaki, lycéen capable de voir les esprits, devient shinigami remplaçant et se retrouve mêlé aux conflits de la Soul Society, des Hollows puis des Quincy. L'arc final, la Guerre sanglante de mille ans, est adapté en animé depuis 2022.",
             "Les questions portent sur le Gotei 13 et ses capitaines, les Zanpakutō et leurs Bankai, les Espada d'Aizen, les Sternritter et l'univers spirituel de la série. Les noms des libérations de sabres sont le grand piège de ce quiz.",
         ]),
    dict(key='jjk', slug='jujutsu-kaisen', name='Jujutsu Kaisen', cat='anime',
         tag="Yuji, Gojō et Sukuna, l'énergie occulte dans le Japon moderne.",
         intro=[
             "Jujutsu Kaisen a été publié par Gege Akutami de 2018 à 2024. Après avoir avalé un doigt du roi des fléaux Ryômen Sukuna, le lycéen Yuji Itadori intègre l'école d'exorcisme de Tokyo. L'adaptation du studio MAPPA a largement contribué au succès mondial de la série.",
             "Le quiz couvre les techniques innées, les extensions de territoire, les grands clans (Gojō, Zen'in, Kamo), l'incident de Shibuya et la suite du manga. Les règles des pactes et le fonctionnement des techniques sont au cœur des questions avancées.",
         ]),
    dict(key='mha', slug='my-hero-academia', name='My Hero Academia', cat='anime',
         tag="Deku, All Might et les Alters, l'école des héros.",
         intro=[
             "Kōhei Horikoshi a publié My Hero Academia de 2014 à 2024. Dans un monde où la plupart des gens possèdent un Alter, Izuku Midoriya, né sans pouvoir, hérite du One For All d'All Might et entre au lycée Yuei pour devenir un héros professionnel.",
             "Les questions portent sur la classe 1-A et ses Alters, les héros professionnels, la Ligue des super-vilains, les détenteurs successifs du One For All et les grands arcs jusqu'à la guerre finale. Les limites précises de chaque pouvoir reviennent souvent dans les questions difficiles.",
         ]),
    dict(key='fairytail', slug='fairy-tail', name='Fairy Tail', cat='anime',
         tag="La guilde de Mavis Vermillion, magie et aventures au royaume de Fiore.",
         intro=[
             "Fairy Tail, de Hiro Mashima, a paru de 2006 à 2017 avant de se prolonger avec Fairy Tail: 100 Years Quest. La série suit Natsu Dragnir, Lucy Heartfilia, Grey, Erza et Happy au sein de la guilde de mages la plus turbulente du royaume de Fiore.",
             "Le quiz couvre les guildes, les différentes magies (chasseurs de dragons, constellations, rééquipement), les grands arcs comme Tenrô ou les Grands Jeux magiques, et l'histoire de Zeref et Mavis. Les liens entre dragons et chasseurs sont un classique des questions pointues.",
         ]),
    dict(key='hxh', slug='hunter-x-hunter', name='Hunter × Hunter', cat='anime',
         tag="Gon, Killua et le Nen, un univers d'une profondeur rare.",
         intro=[
             "Hunter × Hunter est publié par Yoshihiro Togashi depuis 1998, avec de longues interruptions. Gon Freecss passe l'examen de Hunter pour retrouver son père Ging et se lie d'amitié avec Killua Zoldyck, héritier d'une famille d'assassins. L'adaptation de 2011 en 148 épisodes reste la référence pour beaucoup de fans.",
             "Le quiz explore l'examen de Hunter, la tour céleste, York Shin et la Brigade fantôme, Greed Island, l'arc des Fourmis-chimères et l'élection. Le Nen, ses six catégories et les conditions qui renforcent une technique sont au cœur des questions les plus exigeantes.",
         ]),
    dict(key='deathnote', slug='death-note', name='Death Note', cat='anime',
         tag="Light, L et Ryuk, le duel autour du cahier de la mort.",
         intro=[
             "Écrit par Tsugumi Ōba et dessiné par Takeshi Obata, Death Note a été publié de 2003 à 2006 en 108 chapitres, puis adapté en 37 épisodes. Le lycéen Light Yagami trouve un cahier qui tue toute personne dont on y inscrit le nom, et se lance dans une croisade qui l'oppose au détective L.",
             "Les questions portent sur les règles du cahier, les dieux de la mort comme Ryuk et Rem, les successeurs de L, l'enquête de la police japonaise et les stratégies de Light. Connaître les règles exactes, et celles que Light a inventées, est indispensable pour les questions difficiles.",
         ]),
    dict(key='fmab', slug='fullmetal-alchemist', name='Fullmetal Alchemist', cat='anime',
         tag="Ed et Al Elric, l'alchimie et la pierre philosophale.",
         intro=[
             "Fullmetal Alchemist, de Hiromu Arakawa, a été publié de 2001 à 2010. Après une transmutation humaine ratée, Edward Elric perd une jambe et un bras, et son frère Alphonse son corps tout entier, son âme fixée dans une armure. L'adaptation Brotherhood (2009-2010) suit fidèlement le manga.",
             "Le quiz couvre les principes de l'alchimie et de l'échange équivalent, les alchimistes d'État, les sept Homonculus, le pays de Xing et la conspiration qui ronge l'armée d'Amestris. L'histoire d'Ishval et l'identité du Père nourrissent les questions difficiles.",
         ]),
    dict(key='dragonball', slug='dragon-ball', name='Dragon Ball', cat='anime',
         tag="Goku, Vegeta et les Saiyans, des combats qui secouent les planètes.",
         intro=[
             "Dragon Ball, d'Akira Toriyama, a paru de 1984 à 1995 et a profondément influencé le manga d'action. Inspirée au départ du Voyage vers l'Ouest, l'histoire de Son Goku se prolonge avec Dragon Ball Z, Dragon Ball Super et Dragon Ball Daima, sorti en 2024, l'année de la disparition de Toriyama.",
             "Les questions couvrent les sagas des Saiyans, de Freezer, de Cell et de Boo, puis l'ère Super : transformations, techniques comme le Kamehameha ou la Genkidama, personnages secondaires et univers. L'ordre des transformations et les noms des techniques sont les pièges habituels.",
         ]),
    dict(key='onepunchman', slug='one-punch-man', name='One Punch Man', cat='anime',
         tag="Saitama et l'Association des héros, vaincre d'un seul coup.",
         intro=[
             "Né comme bande dessinée en ligne de l'auteur ONE en 2009, One Punch Man a été redessiné à partir de 2012 par Yūsuke Murata. Saitama, héros si puissant qu'il gagne chaque combat d'un seul coup de poing, s'ennuie ferme et peine à se faire reconnaître par l'Association des héros.",
             "Le quiz porte sur le classement des héros et leurs rangs, les menaces de niveau Dragon et Dieu, Genos, Garo et l'Association des monstres. La série parodie les codes des super-héros : l'humour et les détails absurdes font aussi partie des questions.",
         ]),
    dict(key='inazuma', slug='inazuma-eleven', name='Inazuma Eleven', cat='anime',
         tag="Raimon, les supertechniques et les tournois légendaires.",
         intro=[
             "Inazuma Eleven est une série de jeux vidéo de Level-5 lancée en 2008 sur Nintendo DS, rapidement adaptée en animé. Mark Evans, gardien de but au collège Raimon, rassemble une équipe pour sauver le club de football et affronter des adversaires aux supertechniques spectaculaires.",
             "Les questions couvrent la série originale, Inazuma Eleven GO et ses suites : les équipes, les supertechniques, les esprits guerriers et les tournois. Les noms français des techniques diffèrent souvent des noms japonais, ce qui fait la difficulté de certaines questions.",
         ]),
    dict(key='bluelock', slug='blue-lock', name='Blue Lock', cat='anime',
         tag="300 attaquants, un seul buteur : Isagi, Rin et l'égoïsme comme arme.",
         intro=[
             "Blue Lock est publié depuis 2018, scénarisé par Muneyuki Kaneshiro et dessiné par Yūsuke Nomura. La fédération japonaise enferme 300 jeunes attaquants dans un centre d'entraînement pour faire émerger le meilleur buteur égoïste du monde. Yoichi Isagi y découvre une vision du football fondée sur la lecture du jeu.",
             "Le quiz couvre les sélections successives, le match contre l'équipe nationale U-20, la Neo Egoist League et ses clubs, ainsi que les armes propres à chaque joueur. Les citations et les noms des techniques sont au programme des questions difficiles.",
         ]),
    dict(key='soloLeveling', slug='solo-leveling', name='Solo Leveling', cat='anime',
         tag="Le chasseur le plus faible devient le Monarque des ombres.",
         intro=[
             "Solo Leveling est un roman en ligne coréen de Chugong, adapté en webtoon de 2018 à 2021 avec les dessins de Dubu, puis en animé par A-1 Pictures à partir de 2024. Sung Jin-woo, chasseur de rang E réputé le plus faible, reçoit un mystérieux « système » qui le fait progresser comme un personnage de jeu vidéo.",
             "Les questions portent sur le système et ses quêtes, l'armée des ombres (Igris, Beru, Bellion…), les chasseurs de rang S, les donjons et les Monarques. Les noms des ombres et l'ordre des événements sont les points délicats.",
         ]),

    # ------------------------------------------------------------ SÉRIES TV
    dict(key='got', slug='game-of-thrones', name='Game of Thrones', cat='series',
         tag="Westeros, les Stark, les Lannister et la guerre pour le Trône de fer.",
         intro=[
             "Adaptée du Trône de fer de George R. R. Martin, Game of Thrones a été diffusée par HBO de 2011 à 2019 en huit saisons. Les grandes maisons de Westeros se disputent le Trône de fer pendant que la menace des Marcheurs blancs grandit au-delà du Mur. La série dérivée House of the Dragon revient sur la dynastie Targaryen.",
             "Le quiz couvre les maisons et leurs devises, les personnages, les dragons, la Garde de nuit, les grandes batailles et les coulisses de la série. Les liens familiaux et les devises des maisons sont les classiques des questions difficiles.",
         ]),
    dict(key='breakingbad', slug='breaking-bad', name='Breaking Bad', cat='series',
         tag="Walter White, de professeur de chimie à Heisenberg.",
         intro=[
             "Créée par Vince Gilligan, Breaking Bad a été diffusée sur AMC de 2008 à 2013. Walter White, professeur de chimie au Nouveau-Mexique atteint d'un cancer, se met à fabriquer de la méthamphétamine avec son ancien élève Jesse Pinkman. L'univers se prolonge avec Better Call Saul et le film El Camino.",
             "Les questions portent sur les personnages, les cartels, Gus Fring, la DEA, les épisodes clés et les répliques. Les détails de la dernière saison et les liens avec Better Call Saul forment les questions les plus difficiles.",
         ]),
    dict(key='peakyBlinders', slug='peaky-blinders', name='Peaky Blinders', cat='series',
         tag="Birmingham, 1919 : la famille Shelby règne par la peur.",
         intro=[
             "Créée par Steven Knight, Peaky Blinders a été diffusée par la BBC de 2013 à 2022. À Birmingham après la Première Guerre mondiale, Thomas Shelby, interprété par Cillian Murphy, transforme le gang familial en une organisation influente, de la pègre locale jusqu'au Parlement.",
             "Le quiz couvre la famille Shelby, ses alliés et ses ennemis, les intrigues politiques de l'entre-deux-guerres et les répliques marquantes. Les rivaux successifs de Tommy et la chronologie des saisons sont au programme des questions avancées.",
         ]),
    dict(key='casapapel', slug='la-casa-de-papel', name='La Casa de Papel', cat='series',
         tag="Le Professeur, les masques de Dalí et le braquage du siècle.",
         intro=[
             "Créée par Álex Pina, La Casa de Papel a d'abord été diffusée en Espagne sur Antena 3 en 2017, avant que Netflix ne la rende mondialement célèbre et ne la prolonge jusqu'en 2021. Un mystérieux Professeur réunit des braqueurs surnommés d'après des villes pour attaquer la Fabrique nationale de la monnaie, puis la Banque d'Espagne.",
             "Les questions portent sur les braqueurs et leurs surnoms, les plans du Professeur, les négociations avec la police et les moments cultes. Les vrais prénoms des personnages sont l'un des pièges favoris de ce quiz.",
         ]),
    dict(key='strangerthings', slug='stranger-things', name='Stranger Things', cat='series',
         tag="Hawkins, le Monde à l'envers et Eleven contre les ténèbres.",
         intro=[
             "Créée par les frères Duffer, Stranger Things est diffusée sur Netflix depuis 2016 et s'est conclue avec une cinquième saison fin 2025. Dans la petite ville d'Hawkins, dans l'Indiana des années 1980, la disparition de Will Byers révèle l'existence d'un monde parallèle et d'expériences secrètes menées sur une jeune fille, Eleven.",
             "Le quiz couvre les personnages, les créatures du Monde à l'envers, le laboratoire d'Hawkins, les saisons et les nombreuses références à la culture populaire des années 80.",
         ]),
    dict(key='squidgame', slug='squid-game', name='Squid Game', cat='series',
         tag="456 joueurs, des jeux d'enfants mortels et 45,6 milliards de wons.",
         intro=[
             "Créée par Hwang Dong-hyuk, Squid Game est sortie sur Netflix en 2021 et est devenue l'une des séries les plus regardées de la plateforme. Des centaines de personnes surendettées acceptent de participer à des jeux d'enfants dont les perdants sont éliminés. La saison 2 est sortie fin 2024 et la saison 3, qui conclut l'histoire, en 2025.",
             "Les questions portent sur les jeux, les joueurs et leurs numéros, Seong Gi-hun, l'organisation des gardes et du Front Man, et les révélations des saisons suivantes.",
         ]),
    dict(key='friends', slug='friends', name='Friends', cat='series',
         tag="Rachel, Monica, Phoebe, Ross, Chandler et Joey à Central Perk.",
         intro=[
             "Friends, créée par David Crane et Marta Kauffman, a été diffusée sur NBC de 1994 à 2004 en dix saisons et 236 épisodes. Six amis new-yorkais partagent leurs amours, leurs emplois et leurs déboires entre l'appartement de Monica et le café Central Perk.",
             "Le quiz porte sur les personnages, les couples, les épisodes de Thanksgiving, les répliques cultes et les apparitions de stars invitées. Les détails des running gags sont la meilleure arme des fans.",
         ]),
    dict(key='vikings', slug='vikings', name='Vikings', cat='series',
         tag="Ragnar Lothbrok, Lagertha et les raids venus du Nord.",
         intro=[
             "Créée par Michael Hirst, Vikings a été diffusée sur History de 2013 à 2020 en six saisons. Inspirée des sagas, elle suit l'ascension de Ragnar Lothbrok, simple fermier devenu roi, puis le destin de ses fils. La série dérivée Vikings: Valhalla poursuit l'histoire un siècle plus tard.",
             "Le quiz couvre les personnages, la mythologie nordique, les raids en Angleterre et en France, les voyages et le contexte historique de l'époque viking.",
         ]),

    # ------------------------------------------------------------ FILMS
    dict(key='harrypotter', slug='harry-potter', name='Harry Potter', cat='films',
         tag="Poudlard, les quatre maisons et la lutte contre Voldemort.",
         intro=[
             "La saga Harry Potter de J. K. Rowling compte sept romans parus de 1997 à 2007, adaptés en huit films de 2001 à 2011. Harry découvre à onze ans qu'il est sorcier, entre à Poudlard et affronte peu à peu Lord Voldemort, le mage noir qui a tué ses parents.",
             "Le quiz couvre Poudlard et ses maisons, les professeurs, les sortilèges, les créatures, le Ministère de la Magie, les Horcruxes et les Reliques de la Mort. Les noms exacts des sorts et les généalogies des familles de sorciers sont les pièges classiques.",
         ]),
    dict(key='lotr', slug='seigneur-des-anneaux', name='Le Seigneur des Anneaux', cat='films',
         tag="Frodon, Gandalf et la Terre du Milieu.",
         intro=[
             "Le Seigneur des Anneaux de J. R. R. Tolkien a paru en trois volumes en 1954 et 1955. La quête de Frodon pour détruire l'Anneau unique dans les flammes de la Montagne du Destin a fondé la fantasy moderne. La trilogie de Peter Jackson (2001-2003) a remporté 17 Oscars au total.",
             "Les questions couvrent la Communauté de l'Anneau, les peuples de la Terre du Milieu, les lieux, les armes, la magie et l'œuvre de Tolkien au-delà des films, notamment Bilbo le Hobbit.",
         ]),
    dict(key='starwars', slug='star-wars', name='Star Wars', cat='films',
         tag="La Force, les Jedi, les Sith et la saga Skywalker.",
         intro=[
             "Créée par George Lucas avec un premier film sorti en 1977, Star Wars est devenue l'une des sagas les plus influentes du cinéma. La trilogie originale, la prélogie et la postlogie racontent l'histoire de la famille Skywalker, complétée depuis le rachat par Disney en 2012 par de nombreux films et séries.",
             "Le quiz couvre les personnages, la Force, les Jedi et les Sith, les planètes, les vaisseaux, la technologie et les coulisses des films.",
         ]),
    dict(key='marvel', slug='marvel', name='Marvel (MCU)', cat='films',
         tag="Avengers, Thanos et les Pierres d'infinité.",
         intro=[
             "L'univers cinématographique Marvel a commencé en 2008 avec Iron Man et est devenu la franchise la plus rentable de l'histoire du cinéma. La saga de l'Infini s'est conclue en 2019 avec Avengers: Endgame, avant l'ouverture de la saga du Multivers au cinéma et sur Disney+.",
             "Les questions portent sur les héros et leurs antagonistes, les Pierres d'infinité, Asgard, les Gardiens de la Galaxie, les films et les séries, ainsi que le casting et les répliques.",
         ]),

    # ------------------------------------------------------------ JEUX VIDÉO
    dict(key='pokemon', slug='pokemon', name='Pokémon', cat='jeux',
         tag="Types, légendaires et champions, de Kanto à Paldea.",
         intro=[
             "Pokémon est née en 1996 au Japon avec les jeux Rouge et Vert de Game Freak, imaginés par Satoshi Tajiri. La série compte aujourd'hui plus de 1 000 espèces réparties sur neuf générations, et la franchise est la plus lucrative de l'histoire du divertissement.",
             "Le quiz couvre les types et leurs faiblesses, les Pokémon de départ et légendaires, les régions, les champions d'arène, les mécaniques de jeu, l'animé et l'histoire de la franchise. Le tableau des types reste la base de toute bonne partie.",
         ]),
    dict(key='minecraft', slug='minecraft', name='Minecraft', cat='jeux',
         tag="Survie, construction, créatures et biomes.",
         intro=[
             "Créé par Markus « Notch » Persson et publié par Mojang à partir de 2009, Minecraft a été racheté par Microsoft en 2014. C'est le jeu vidéo le plus vendu de tous les temps, avec plus de 300 millions d'exemplaires.",
             "Les questions portent sur la survie, les recettes de fabrication, les créatures, les biomes, le Nether et l'End, ainsi que les grandes mises à jour du jeu.",
         ]),
    dict(key='gta', slug='gta-v', name='GTA V', cat='jeux',
         tag="Michael, Trevor et Franklin à Los Santos.",
         intro=[
             "Sorti en 2013, Grand Theft Auto V de Rockstar Games est l'un des jeux les plus vendus de l'histoire. On y incarne trois criminels, Michael, Franklin et Trevor, dans Los Santos, version satirique de Los Angeles. Son mode en ligne, GTA Online, est toujours mis à jour.",
             "Le quiz couvre les personnages, la ville et ses environs, les braquages, les missions, GTA Online et les clins d'œil cachés dans le jeu.",
         ]),
    dict(key='zelda', slug='zelda', name='The Legend of Zelda', cat='jeux',
         tag="Link, Zelda, Ganon et la Triforce.",
         intro=[
             "The Legend of Zelda est une série de Nintendo créée par Shigeru Miyamoto et Takashi Tezuka, dont le premier épisode est sorti en 1986. Link y affronte le plus souvent Ganon pour protéger le royaume d'Hyrule. Breath of the Wild (2017) et Tears of the Kingdom (2023) ont réinventé la série en monde ouvert.",
             "Les questions portent sur les personnages, les objets, les donjons, les différents jeux et la chronologie officielle de la série.",
         ]),
    dict(key='mario', slug='super-mario', name='Super Mario', cat='jeux',
         tag="Le Royaume Champignon, Bowser et les power-ups.",
         intro=[
             "Mario est apparu en 1981 dans Donkey Kong, imaginé par Shigeru Miyamoto, avant de devenir la mascotte de Nintendo avec Super Mario Bros. en 1985. Plateformes en 2D et en 3D, courses, sport, jeux de société : peu de personnages ont connu autant de genres.",
             "Le quiz couvre les personnages du Royaume Champignon, les power-ups, les mondes, les objets et l'histoire des jeux.",
         ]),
    dict(key='lol', slug='league-of-legends', name='League of Legends', cat='jeux',
         tag="Champions, rôles, objectifs et lore de Runeterra.",
         intro=[
             "Sorti en 2009, League of Legends de Riot Games oppose deux équipes de cinq champions sur la Faille de l'invocateur. C'est l'un des jeux les plus joués au monde et l'une des disciplines phares de l'esport, tandis que la série animée Arcane a fait découvrir son univers à un large public.",
             "Les questions portent sur les champions, les rôles et les voies, les objectifs de la carte, les sorts d'invocateur, l'esport et l'histoire de Runeterra.",
         ]),
    dict(key='valorant', slug='valorant', name='Valorant', cat='jeux',
         tag="Agents, Spike et cartes du FPS tactique de Riot.",
         intro=[
             "Valorant, sorti en 2020, est le jeu de tir tactique de Riot Games. Deux équipes de cinq s'affrontent autour de la pose et du désamorçage d'une bombe, le Spike, en combinant précision au tir et capacités propres à chaque agent.",
             "Le quiz couvre les agents et leurs rôles, les cartes, les armes, les mécaniques de jeu et la scène compétitive.",
         ]),
    dict(key='eafc', slug='ea-sports-fc', name='EA Sports FC', cat='jeux',
         tag="Ultimate Team, DCE, Chimie et Pièces FUT.",
         intro=[
             "EA Sports FC a succédé en 2023 à la série FIFA d'Electronic Arts, après la fin de l'accord de licence avec la fédération internationale. Le jeu conserve les licences de la plupart des grands championnats et son mode phare, Ultimate Team.",
             "Les questions portent sur Ultimate Team (Chimie, DCE, EDSM, Pièces FUT), le Mode Carrière, les joueurs et les clubs, ainsi que l'histoire de la série depuis FIFA.",
         ]),

    # ------------------------------------------------------------ CULTURE
    dict(key='culture', slug='culture-generale', name='Culture générale', cat='culture',
         tag="Sciences, littérature, art, philosophie et mathématiques.",
         intro=[
             "La culture générale, c'est l'ensemble des connaissances qui permettent de comprendre le monde au-delà de sa spécialité. Ce quiz pioche dans les grands domaines du savoir pour tester l'étendue de vos connaissances plutôt que leur profondeur.",
             "Les questions couvrent les sciences, la géographie, la littérature, l'art et la musique, la philosophie et les mathématiques, du niveau collège jusqu'aux détails qui départagent les passionnés.",
         ]),
    dict(key='histoire', slug='histoire', name='Histoire', cat='culture',
         tag="De l'Antiquité aux guerres mondiales.",
         intro=[
             "Ce quiz parcourt l'histoire de l'humanité, des premières civilisations aux grands conflits du XXᵉ siècle. Dates, personnages, batailles et traités : de quoi vérifier ce qu'il reste de vos cours, et apprendre au passage.",
             "Les questions couvrent l'Antiquité, le Moyen Âge, les révolutions, les guerres mondiales, l'histoire de France et l'histoire mondiale, y compris la guerre froide et les grandes explorations.",
         ]),
    dict(key='geo', slug='geographie', name='Géographie', cat='culture',
         tag="Capitales, records naturels, pays et océans.",
         intro=[
             "La géographie décrit la Terre et la façon dont les humains l'habitent. Ce quiz vous emmène d'un continent à l'autre pour tester vos connaissances sur les pays, leurs capitales et les grands records naturels.",
             "Les questions portent sur les capitales, les continents, les pays, les océans et les mers, les records (plus haut sommet, plus long fleuve…) et la géographie de la France.",
         ]),
    dict(key='sport', slug='sport', name='Sport', cat='culture',
         tag="Football, tennis, athlétisme et Jeux olympiques.",
         intro=[
             "Ce quiz rassemble les grandes disciplines sportives, leurs compétitions phares et les athlètes qui ont marqué leur époque. Des Coupes du monde aux Jeux olympiques, les records et les palmarès sont au rendez-vous.",
             "Les questions couvrent le football, l'athlétisme, le basketball, le tennis, le rugby, les Jeux olympiques et bien d'autres sports, de la boxe au cyclisme.",
         ]),
    dict(key='musique', slug='musique', name='Musique', cat='culture',
         tag="Rap français, pop mondiale, rock et albums cultes.",
         intro=[
             "De la chanson française au rap, de la pop au rock, ce quiz traverse les genres et les époques. Artistes, albums, records et anecdotes de l'histoire de la musique populaire sont au programme.",
             "Les questions portent sur le rap français, la pop mondiale, le rock, les grands artistes, les albums marquants et l'histoire de la musique enregistrée.",
         ]),
    dict(key='cinema', slug='cinema', name='Cinéma', cat='culture',
         tag="Oscars, réalisateurs, films cultes et box-office.",
         intro=[
             "Né à la fin du XIXᵉ siècle, le cinéma n'a cessé de se réinventer, du muet aux blockbusters. Ce quiz teste votre culture cinématographique, des classiques hollywoodiens au cinéma français et mondial.",
             "Les questions portent sur les Oscars, les réalisateurs, les films cultes, le box-office, l'animation, les acteurs et le cinéma du monde entier.",
         ]),
    # ------------------------------------------------------------ NOUVEAUX UNIVERS (publication programmée)
    dict(key='frieren', slug='frieren', name='Frieren', cat='anime', date='2026-11-02',
         tag="L'elfe mage, le héros disparu et le long voyage vers le nord.",
         intro=[
             "Frieren, scénarisé par Kanehito Yamada et dessiné par Tsukasa Abe, est publié dans le Weekly Shōnen Sunday depuis 2020. L'histoire commence là où les récits d'aventure s'arrêtent d'habitude : le Roi des démons est vaincu, et Frieren, elfe mage qui vivra encore des siècles, voit ses compagnons humains vieillir et disparaître. Le manga a reçu le Manga Taishō en 2021, et l'adaptation du studio Madhouse a été l'un des animés les plus salués de 2023-2024.",
             "Le quiz couvre le groupe du héros Himmel, le nouveau voyage de Frieren avec Fern et Stark, la magie et ses grands sorts, les démons comme Aura la Guillotine, l'examen de mage de première classe et les coulisses de l'œuvre. Une série de questions porte aussi sur le sens des noms allemands des personnages.",
         ]),
    dict(key='chainsawman', slug='chainsaw-man', name='Chainsaw Man', cat='anime', date='2026-11-16',
         tag="Denji, Pochita et la Sécurité publique contre les démons.",
         intro=[
             "Chainsaw Man, de Tatsuki Fujimoto, a d'abord paru dans le Weekly Shōnen Jump de 2018 à 2020, avant une deuxième partie publiée sur Shōnen Jump+ depuis 2022. Denji, adolescent écrasé de dettes, fusionne avec son démon-chien Pochita et devient un hybride capable de faire jaillir des tronçonneuses de son corps. Recruté par la mystérieuse Makima, il rejoint les chasseurs de démons de la Sécurité publique.",
             "Les questions portent sur les personnages, les démons et leurs contrats, la différence entre démons possédants et hybrides, les grands arcs de la première partie, l'animé du studio MAPPA et le film consacré à Reze. Attention : certaines questions difficiles révèlent la fin de la première partie.",
         ]),
    dict(key='spyfamily', slug='spy-x-family', name='Spy × Family', cat='anime', date='2026-11-30',
         tag="Un espion, une tueuse et une télépathe sous le même toit.",
         intro=[
             "Spy × Family, de Tatsuya Endo, est publié sur Shōnen Jump+ depuis 2019. Pour approcher un homme politique dangereux, l'espion Twilight doit inscrire un enfant dans une école d'élite. Il adopte Anya, sans savoir qu'elle lit dans les pensées, et épouse Yor, sans savoir qu'elle est tueuse à gages. L'adaptation de Wit Studio et CloverWorks a fait de la famille Forger l'une des plus populaires de l'animation récente.",
             "Le quiz couvre la famille Forger et son chien Bond, les agences d'espionnage de Westalis et d'Ostania, l'école Eden et son système de Stella et de Tonitrus, ainsi que les coulisses du manga, de l'animé et du film Code: White.",
         ]),
]

CATEGORIES = [
    ('anime', 'Animés', "Les shōnen et les animés qui ont marqué plusieurs générations."),
    ('series', 'Séries TV', "Les séries dont on parle encore des années après le dernier épisode."),
    ('films', 'Films', "Les grandes sagas du cinéma, des livres aux écrans."),
    ('jeux', 'Jeux vidéo', "Des classiques de Nintendo aux jeux compétitifs."),
    ('culture', 'Culture générale', "Histoire, géographie, sport, musique et cinéma."),
]

POPULAR = ['naruto', 'onepiece', 'harrypotter', 'got', 'breakingbad', 'pokemon']
# Les « nouveaux univers » de l'accueil sont calculés automatiquement à partir des dates.
NEW_FALLBACK = ['bluelock', 'soloLeveling', 'peakyBlinders']
