"""Données du Kamidle (jeux du jour).

Chaque personnage :
  C(id, nom, univers, genre, espèces, rôle, styles, emojis, alias, pouvoir)
    genre   : M (masculin), F (féminin), N (aucun)
    espèces : tuple, la première est l'espèce principale
    rôle    : Protagoniste, Allié, Rival, Mentor, Antagoniste, Neutre
    styles  : tuple parmi STYLES
    emojis  : 3 à 5 emojis, du plus vague au plus parlant
    pouvoir : (description sans nom propre, nom de la technique ou '')

Règle d'écriture : uniquement des informations sûres, connues dès les premiers arcs,
sans révélation majeure de l'intrigue.
"""

STYLES = ['Épée', 'Corps à corps', 'Arme', 'Énergie', 'Magie', 'Pouvoir inné', 'Invocation', 'Sport', 'Ruse', 'Aucun']
STYLE_HELP = {
    'Épée': 'sabres, épées, lames',
    'Corps à corps': 'poings, pieds, arts martiaux',
    'Arme': 'armes à feu, arcs, haches, marteaux, outils',
    'Énergie': 'chakra, ki, énergie occulte, Nen, la Force…',
    'Magie': 'sorts, alchimie, magie',
    'Pouvoir inné': 'fruit du démon, Alter, télépathie, nature du corps…',
    'Invocation': 'combat avec des créatures : Pokémon, ombres, esprits…',
    'Sport': 'football et compétitions',
    'Ruse': 'intelligence, stratégie, manipulation',
    'Aucun': 'ne se bat pas',
}
ROLES = ['Protagoniste', 'Allié', 'Rival', 'Mentor', 'Antagoniste', 'Neutre']


def C(id, name, u, g, esp, role, styles, emo, alias=(), pouvoir=None):
    return {'id': id, 'name': name, 'u': u, 'g': g, 'e': list(esp), 'r': role, 's': list(styles),
            'emo': emo.split(), 'alias': list(alias), 'p': pouvoir}


H = ('Humain',)
CHARS = [
    # ---------------------------------------------------------------- Naruto
    C('naruto', 'Naruto Uzumaki', 'naruto', 'M', H, 'Protagoniste', ('Corps à corps', 'Énergie'), '🧡 👊 🌀 🦊 🍜',
      ('Naruto',), ("Une sphère d'énergie tourbillonnante concentrée dans la paume, sans aucun signe des mains.", 'Rasengan')),
    C('sasuke', 'Sasuke Uchiha', 'naruto', 'M', H, 'Rival', ('Épée', 'Énergie'), '🖤 🗡️ 🐍 ⚡ 👁️', ('Sasuke',)),
    C('sakura', 'Sakura Haruno', 'naruto', 'F', H, 'Allié', ('Corps à corps', 'Énergie'), '💗 🩺 👊 🌸', ('Sakura',)),
    C('kakashi', 'Kakashi Hatake', 'naruto', 'M', H, 'Mentor', ('Énergie', 'Arme'), '😷 📖 🐕 ⚡ 👁️', ('Kakashi',)),
    C('gaara', 'Gaara', 'naruto', 'M', H, 'Allié', ('Pouvoir inné', 'Énergie'), '🏜️ ⏳ 🦝 ❤️', (),
      ("Un bouclier de sable se dresse tout seul pour le protéger, même quand il ne bouge pas.", 'Bouclier de sable')),
    C('jiraiya', 'Jiraiya', 'naruto', 'M', H, 'Mentor', ('Énergie',), '📚 🍶 🐸 ⛩️', ()),
    C('orochimaru', 'Orochimaru', 'naruto', 'M', H, 'Antagoniste', ('Énergie',), '🧪 🌙 👅 🐍', ()),
    C('hinata', 'Hinata Hyuga', 'naruto', 'F', H, 'Allié', ('Corps à corps', 'Énergie'), '🫣 💜 🤍 👁️', ('Hinata',)),
    C('rocklee', 'Rock Lee', 'naruto', 'M', H, 'Allié', ('Corps à corps',), '🏋️ 🔥 💚 🥋', ('Lee',),
      ("Incapable d'utiliser le moindre ninjutsu, il ne compte que sur le taijutsu et l'ouverture des portes de son corps.", 'Les Huit Portes')),

    # ---------------------------------------------------------------- One Piece
    C('luffy', 'Monkey D. Luffy', 'onepiece', 'M', H, 'Protagoniste', ('Corps à corps', 'Pouvoir inné'), '🍖 🏴‍☠️ 🥊 👒',
      ('Luffy',), ("Son corps s'étire comme du caoutchouc, ce qui le rend insensible aux balles et aux coups ordinaires.", 'Fruit du Gomu Gomu')),
    C('zoro', 'Roronoa Zoro', 'onepiece', 'M', H, 'Allié', ('Épée',), '🍶 🧭 💚 🗡️', ('Zoro',),
      ("Il combat avec trois sabres, dont un tenu entre les dents.", 'Santoryu')),
    C('nami', 'Nami', 'onepiece', 'F', H, 'Allié', ('Arme', 'Ruse'), '💰 🍊 ⛈️ 🗺️', ()),
    C('sanji', 'Sanji', 'onepiece', 'M', H, 'Allié', ('Corps à corps',), '🚬 😍 🦵 🍳', ()),
    C('usopp', 'Usopp', 'onepiece', 'M', H, 'Allié', ('Arme', 'Ruse'), '🤥 🎯 👃', ()),
    C('chopper', 'Tony Tony Chopper', 'onepiece', 'M', ('Renne',), 'Allié', ('Pouvoir inné', 'Corps à corps'), '🍬 🎩 🩺 🦌', ('Chopper',)),
    C('robin', 'Nico Robin', 'onepiece', 'F', H, 'Allié', ('Pouvoir inné',), '🏛️ 📚 🙌 🌸', ('Robin',),
      ("Elle fait éclore des bras, des mains et des yeux sur n'importe quelle surface autour d'elle.", 'Fruit du Hana Hana')),
    C('ace', 'Portgas D. Ace', 'onepiece', 'M', H, 'Allié', ('Pouvoir inné', 'Corps à corps'), '🤠 🧡 🔥', ('Ace',),
      ("Son corps se change en flammes ; on le surnomme « Poing ardent ».", 'Fruit du Mera Mera')),
    C('shanks', 'Shanks le Roux', 'onepiece', 'M', H, 'Mentor', ('Épée',), '🍺 🔴 🗡️ 👒', ('Shanks',)),
    C('brook', 'Brook', 'onepiece', 'M', ('Squelette',), 'Allié', ('Épée',), '☕ 🎩 🎻 💀', ()),
    C('franky', 'Franky', 'onepiece', 'M', ('Cyborg',), 'Allié', ('Arme', 'Corps à corps'), '🕶️ 🥤 🔧 🤖', ()),
    C('jinbe', 'Jinbe', 'onepiece', 'M', ('Homme-poisson',), 'Allié', ('Corps à corps',), '🥋 🌊 🐟', ('Jinbei',)),
    C('crocodile', 'Crocodile', 'onepiece', 'M', H, 'Antagoniste', ('Pouvoir inné',), '🚬 🪝 🏜️ 🐊', (),
      ("Il change son corps en sable et assèche tout ce qu'il touche de la main.", 'Fruit du Suna Suna')),
    C('barbenoire', 'Barbe Noire', 'onepiece', 'M', H, 'Antagoniste', ('Pouvoir inné',), '😁 🍒 🖤 🌑', ('Marshall D. Teach', 'Teach'),
      ("Des ténèbres qui aspirent tout ce qui les approche, y compris les pouvoirs des autres.", 'Fruit du Yami Yami')),

    # ---------------------------------------------------------------- Attack on Titan
    C('eren', 'Eren Jäger', 'aot', 'M', H, 'Protagoniste', ('Épée', 'Pouvoir inné'), '🧱 😡 🔑', ('Eren', 'Eren Yeager')),
    C('mikasa', 'Mikasa Ackerman', 'aot', 'F', H, 'Allié', ('Épée',), '🖤 ⚔️ 🧣', ('Mikasa',)),
    C('armin', 'Armin Arlert', 'aot', 'M', H, 'Allié', ('Ruse',), '📖 🧠 🌊', ('Armin',)),
    C('levi', 'Livaï Ackerman', 'aot', 'M', H, 'Allié', ('Épée',), '😐 🍵 🧹 ⚔️', ('Livai', 'Levi', 'Livaï')),

    # ---------------------------------------------------------------- Demon Slayer
    C('tanjiro', 'Tanjiro Kamado', 'demonslayer', 'M', H, 'Protagoniste', ('Épée',), '🧺 🌊 👃 🎴', ('Tanjiro',),
      ("Un odorat si fin qu'il sent les émotions des autres et le point faible de ses adversaires.", 'Odorat surdéveloppé')),
    C('nezuko', 'Nezuko Kamado', 'demonslayer', 'F', ('Démon',), 'Allié', ('Corps à corps', 'Pouvoir inné'), '🩷 📦 🎋', ('Nezuko',),
      ("Son sang s'enflamme et brûle les démons, sans blesser les humains.", 'Sang explosif')),
    C('zenitsu', 'Zenitsu Agatsuma', 'demonslayer', 'M', H, 'Allié', ('Épée',), '😱 💛 😴 ⚡', ('Zenitsu',),
      ("Il ne maîtrise qu'une seule technique, qu'il exécute souvent en dormant, à la vitesse de l'éclair.", 'Souffle de la foudre, première forme')),
    C('inosuke', 'Inosuke Hashibira', 'demonslayer', 'M', H, 'Allié', ('Épée',), '💪 🗡️ 🗡️ 🐗', ('Inosuke',),
      ("Deux lames ébréchées et un style de combat inventé seul dans la montagne.", 'Souffle de la bête')),
    C('giyu', 'Giyu Tomioka', 'demonslayer', 'M', H, 'Allié', ('Épée',), '🤐 🧥 🌊', ('Giyu',)),
    C('rengoku', 'Kyojuro Rengoku', 'demonslayer', 'M', H, 'Mentor', ('Épée',), '😋 🍱 🚂 🔥', ('Rengoku',)),
    C('muzan', 'Muzan Kibutsuji', 'demonslayer', 'M', ('Démon',), 'Antagoniste', ('Pouvoir inné',), '🎩 🌙 🩸', ('Muzan',)),
    C('shinobu', 'Shinobu Kocho', 'demonslayer', 'F', H, 'Allié', ('Épée',), '😊 💜 🧪 🦋', ('Shinobu',),
      ("Trop frêle pour décapiter un démon, elle le tue avec un poison injecté par la pointe de son sabre.", 'Souffle de l\'insecte')),

    # ---------------------------------------------------------------- Bleach
    C('ichigo', 'Ichigo Kurosaki', 'bleach', 'M', ('Humain', 'Shinigami'), 'Protagoniste', ('Épée', 'Énergie'), '🧡 💀 🗡️ 🍓', ('Ichigo',),
      ("Une lame d'énergie projetée d'un coup de sabre, noire et rouge sous sa forme libérée.", 'Getsuga Tensho')),
    C('rukia', 'Rukia Kuchiki', 'bleach', 'F', ('Shinigami',), 'Allié', ('Épée', 'Énergie'), '🐰 🗡️ ❄️', ('Rukia',),
      ("Son sabre tout blanc gèle ce qu'il touche ; on le dit le plus beau de la Soul Society.", 'Sode no Shirayuki')),
    C('byakuya', 'Byakuya Kuchiki', 'bleach', 'M', ('Shinigami',), 'Allié', ('Épée',), '🧣 🗡️ 🌸', ('Byakuya',),
      ("Sa lame se disperse en milliers de fragments minuscules qui ressemblent à des pétales de cerisier.", 'Senbonzakura')),
    C('aizen', 'Sosuke Aizen', 'bleach', 'M', ('Shinigami',), 'Antagoniste', ('Épée', 'Ruse'), '☕ 👓 🦋 🗡️', ('Aizen',),
      ("Quiconque a vu son sabre se libérer tombe sous une illusion totale des cinq sens.", 'Kyoka Suigetsu')),
    C('kenpachi', 'Kenpachi Zaraki', 'bleach', 'M', ('Shinigami',), 'Allié', ('Épée',), '😈 🩸 ⚔️ 🔔', ('Kenpachi',)),
    C('urahara', 'Kisuke Urahara', 'bleach', 'M', ('Shinigami',), 'Mentor', ('Épée', 'Ruse'), '🍬 🪭 🎩', ('Urahara',)),

    # ---------------------------------------------------------------- Jujutsu Kaisen
    C('itadori', 'Yuji Itadori', 'jjk', 'M', H, 'Protagoniste', ('Corps à corps', 'Énergie'), '🏃 👊 👆', ('Yuji', 'Itadori')),
    C('megumi', 'Megumi Fushiguro', 'jjk', 'M', H, 'Allié', ('Invocation', 'Énergie'), '🌑 🖐️ 🐕', ('Megumi',),
      ("Il invoque des bêtes en dessinant leur silhouette avec l'ombre de ses mains.", 'Technique des Dix Ombres')),
    C('nobara', 'Nobara Kugisaki', 'jjk', 'F', H, 'Allié', ('Arme', 'Énergie'), '🧡 🔨 📌', ('Nobara',),
      ("Un marteau, des clous et une poupée de paille : ce qu'elle frappe blesse sa cible à distance.", 'Technique de la poupée de paille')),
    C('gojo', 'Satoru Gojo', 'jjk', 'M', H, 'Mentor', ('Énergie',), '🍬 🤍 🕶️ ♾️', ('Gojo',),
      ("Tout ce qui l'approche ralentit indéfiniment, sans jamais réussir à le toucher.", "L'Infini")),
    C('sukuna', 'Ryomen Sukuna', 'jjk', 'M', ('Fléau',), 'Antagoniste', ('Énergie',), '👄 👀 👀 👆', ('Sukuna',)),
    C('mahito', 'Mahito', 'jjk', 'M', ('Fléau',), 'Antagoniste', ('Énergie',), '😈 🧵 🖐️', (),
      ("Il remodèle l'âme de ceux qu'il touche, et donc la forme de leur corps.", '')),
    C('nanami', 'Kento Nanami', 'jjk', 'M', H, 'Allié', ('Arme', 'Énergie'), '👔 🍞 ⌚', ('Nanami',),
      ("Il divise sa cible en dix parts et frappe le point situé à sept dixièmes pour infliger un coup critique.", 'Ratio')),

    # ---------------------------------------------------------------- My Hero Academia
    C('deku', 'Izuku Midoriya', 'mha', 'M', H, 'Protagoniste', ('Corps à corps', 'Pouvoir inné'), '📓 💚 👟', ('Deku', 'Izuku'),
      ("Un pouvoir transmis de génération en génération, si puissant qu'au début il lui brisait les os.", 'One For All')),
    C('bakugo', 'Katsuki Bakugo', 'mha', 'M', H, 'Rival', ('Pouvoir inné',), '😡 🧡 💥', ('Bakugo', 'Kacchan'),
      ("Sa sueur, semblable à de la nitroglycérine, explose au creux de ses mains.", 'Explosion')),
    C('todoroki', 'Shoto Todoroki', 'mha', 'M', H, 'Allié', ('Pouvoir inné',), '🍜 ❄️ 🔥', ('Shoto', 'Todoroki'),
      ("De la glace du côté droit, du feu du côté gauche.", 'Moitié froid, moitié chaud')),
    C('allmight', 'All Might', 'mha', 'M', H, 'Mentor', ('Corps à corps', 'Pouvoir inné'), '😁 🇺🇸 💪', ()),
    C('uraraka', 'Ochaco Uraraka', 'mha', 'F', H, 'Allié', ('Pouvoir inné',), '🍡 🌸 🎈', ('Ochaco', 'Uraraka'),
      ("Tout ce qu'elle touche du bout de ses cinq doigts perd sa gravité.", 'Zéro gravité')),
    C('shigaraki', 'Tomura Shigaraki', 'mha', 'M', H, 'Antagoniste', ('Pouvoir inné',), '🎮 💀 ✋', ('Shigaraki',),
      ("Tout ce qu'il touche de ses cinq doigts tombe en poussière.", 'Désintégration')),

    # ---------------------------------------------------------------- Fairy Tail
    C('natsu', 'Natsu Dragneel', 'fairytail', 'M', H, 'Protagoniste', ('Magie', 'Corps à corps'), '🤢 🧣 🐉 🔥', ('Natsu',),
      ("Il mange le feu pour reprendre des forces et se bat comme un dragon.", 'Magie du chasseur de dragons')),
    C('lucy', 'Lucy Heartfilia', 'fairytail', 'F', H, 'Allié', ('Magie', 'Invocation'), '📝 ⭐ 🗝️', ('Lucy',),
      ("Des clés pour appeler à ses côtés des esprits venus des étoiles.", '')),
    C('gray', 'Grey Fullbuster', 'fairytail', 'M', H, 'Allié', ('Magie',), '👕 🧊 ❄️', ('Gray', 'Grey')),
    C('erza', 'Erza Scarlet', 'fairytail', 'F', H, 'Allié', ('Épée', 'Magie'), '❤️ 🍰 🛡️ ⚔️', ('Erza',),
      ("Elle change d'armure et d'arme en plein combat, en un instant.", '')),
    C('happy', 'Happy', 'fairytail', 'M', ('Exceed',), 'Allié', ('Magie',), '💙 🐟 🪽 🐱', ()),

    # ---------------------------------------------------------------- Hunter × Hunter
    C('gon', 'Gon Freecss', 'hxh', 'M', H, 'Protagoniste', ('Corps à corps', 'Énergie'), '💚 🌲 🎣', ('Gon',),
      ("Pierre, feuille, ciseaux : toute son aura concentrée dans un seul coup.", 'Jajanken')),
    C('killua', 'Killua Zoldyck', 'hxh', 'M', H, 'Allié', ('Corps à corps', 'Énergie'), '🛹 🍫 ⚡', ('Killua',),
      ("Il change son aura en électricité, une aptitude acquise en encaissant des décharges depuis l'enfance.", 'Transformation électrique')),
    C('kurapika', 'Kurapika', 'hxh', 'M', H, 'Allié', ('Énergie',), '🔴 👁️ ⛓️', (),
      ("Des chaînes au bout des doigts, dont l'une ne peut viser que les membres d'une seule organisation.", '')),
    C('leorio', 'Leorio', 'hxh', 'M', H, 'Allié', ('Corps à corps',), '🕶️ 💼 🩺', ()),
    C('hisoka', 'Hisoka', 'hxh', 'M', H, 'Antagoniste', ('Énergie',), '🍬 🤡 🃏', (),
      ("Une aura qui possède à la fois les propriétés du caoutchouc et du chewing-gum.", 'Bungee Gum')),

    # ---------------------------------------------------------------- Death Note
    C('light', 'Light Yagami', 'deathnote', 'M', H, 'Protagoniste', ('Ruse',), '🥔 🖊️ 📓', ('Light', 'Kira')),
    C('l', 'L', 'deathnote', 'M', H, 'Rival', ('Ruse',), '🪑 🍰 🕵️', ('Ryuzaki', 'L Lawliet')),
    C('ryuk', 'Ryuk', 'deathnote', 'M', ('Shinigami',), 'Neutre', ('Pouvoir inné',), '😈 🖤 🍎', ()),
    C('misa', 'Misa Amane', 'deathnote', 'F', H, 'Allié', ('Pouvoir inné',), '🎀 🖤 👁️', ('Misa',)),

    # ---------------------------------------------------------------- Fullmetal Alchemist
    C('edward', 'Edward Elric', 'fmab', 'M', H, 'Protagoniste', ('Magie', 'Corps à corps'), '📏 🥛 🦾', ('Edward', 'Ed')),
    C('alphonse', 'Alphonse Elric', 'fmab', 'M', H, 'Allié', ('Magie', 'Corps à corps'), '🐈 🛡️', ('Alphonse', 'Al')),
    C('roy', 'Roy Mustang', 'fmab', 'M', H, 'Allié', ('Magie',), '🌧️ 🧤 🫰 🔥', ('Mustang', 'Roy'),
      ("Un claquement de doigts avec des gants spéciaux suffit à déclencher une explosion de flammes.", "Alchimie de la flamme")),

    # ---------------------------------------------------------------- Dragon Ball
    C('goku', 'Son Goku', 'dragonball', 'M', ('Saiyan',), 'Protagoniste', ('Corps à corps', 'Énergie'), '🍚 ☁️ 🐒', ('Goku', 'Sangoku'),
      ("Il lève les bras pour rassembler l'énergie de tous les êtres vivants autour de lui.", 'Genkidama')),
    C('vegeta', 'Vegeta', 'dragonball', 'M', ('Saiyan',), 'Rival', ('Corps à corps', 'Énergie'), '😤 💙 👑', ()),
    C('piccolo', 'Piccolo', 'dragonball', 'M', ('Namek',), 'Allié', ('Énergie',), '🧣 💚 🌀', (),
      ("Un rayon en spirale tiré du bout de deux doigts posés sur le front.", 'Makankosappo')),
    C('bulma', 'Bulma', 'dragonball', 'F', H, 'Allié', ('Ruse',), '💙 🔧 📡', ()),
    C('krilin', 'Krilin', 'dragonball', 'M', H, 'Allié', ('Corps à corps', 'Énergie'), '🥚 🔴 💿', ('Krillin',),
      ("Un disque d'énergie tranchant, lancé au-dessus de la tête, qui coupe presque tout.", 'Kienzan')),

    # ---------------------------------------------------------------- One Punch Man
    C('saitama', 'Saitama', 'onepunchman', 'M', H, 'Protagoniste', ('Corps à corps',), '🛒 🥚 🧤 👊', (),
      ("Il gagne chaque combat d'un seul coup de poing, au point de s'ennuyer terriblement.", '')),
    C('genos', 'Genos', 'onepunchman', 'M', ('Cyborg',), 'Allié', ('Arme',), '🙇 🔥 🤖', ()),

    # ---------------------------------------------------------------- Inazuma Eleven
    C('mark', 'Mark Evans', 'inazuma', 'M', H, 'Protagoniste', ('Sport',), '🧡 🧤 ⚽', ('Mark',),
      ("Une immense main dorée surgit devant lui pour arrêter le tir.", '')),
    C('axel', 'Axel Blaze', 'inazuma', 'M', H, 'Allié', ('Sport',), '🌪️ 🔥 ⚽', ('Axel',)),
    C('jude', 'Jude Sharp', 'inazuma', 'M', H, 'Rival', ('Sport', 'Ruse'), '🧣 🧠 🥽', ('Jude',)),

    # ---------------------------------------------------------------- Blue Lock
    C('isagi', 'Yoichi Isagi', 'bluelock', 'M', H, 'Protagoniste', ('Sport',), '🧩 ⚽ 👁️', ('Isagi',),
      ("Une vision de l'espace qui lui permet de lire tout le terrain comme s'il le voyait d'en haut.", 'Métavision')),
    C('bachira', 'Meguru Bachira', 'bluelock', 'M', H, 'Allié', ('Sport',), '🎨 ⚽ 👾', ('Bachira',)),
    C('rin', 'Rin Itoshi', 'bluelock', 'M', H, 'Rival', ('Sport',), '🧊 ⚽ 👁️', ('Rin',)),
    C('nagi', 'Seishiro Nagi', 'bluelock', 'M', H, 'Allié', ('Sport',), '😴 🎮 ⚽', ('Nagi',),
      ("Un contrôle de balle irréel : il amortit n'importe quelle passe, même tombée du ciel.", '')),

    # ---------------------------------------------------------------- Solo Leveling
    C('jinwoo', 'Sung Jin-Woo', 'soloLeveling', 'M', H, 'Protagoniste', ('Arme', 'Invocation'), '📈 🗡️ 🌑', ('Jin-Woo', 'Jinwoo'),
      ("Il relève les monstres vaincus pour en faire les soldats de son armée d'ombres.", "Extraction d'ombre")),

    # ---------------------------------------------------------------- Game of Thrones
    C('jon', 'Jon Snow', 'got', 'M', H, 'Protagoniste', ('Épée',), '🧥 ❄️ 🐺', ('Jon',)),
    C('daenerys', 'Daenerys Targaryen', 'got', 'F', H, 'Protagoniste', ('Invocation', 'Ruse'), '👑 🥚 🔥 🐉', ('Daenerys', 'Dany')),
    C('tyrion', 'Tyrion Lannister', 'got', 'M', H, 'Protagoniste', ('Ruse',), '📚 🦁 🍷', ('Tyrion',)),
    C('arya', 'Arya Stark', 'got', 'F', H, 'Protagoniste', ('Épée',), '🐺 📜 🎭 🪡', ('Arya',)),
    C('cersei', 'Cersei Lannister', 'got', 'F', H, 'Antagoniste', ('Ruse',), '👑 🦁 🍷', ('Cersei',)),
    C('ned', 'Eddard Stark', 'got', 'M', H, 'Protagoniste', ('Épée',), '⚖️ ❄️ 🐺 🪓', ('Ned', 'Ned Stark')),
    C('joffrey', 'Joffrey Baratheon', 'got', 'M', H, 'Antagoniste', ('Arme',), '😈 🏹 👑 🍷', ('Joffrey',)),
    C('roidelanuit', 'Le Roi de la Nuit', 'got', 'M', ('Marcheur blanc',), 'Antagoniste', ('Pouvoir inné',), '🧟 💀 ❄️', ('Roi de la Nuit', 'Night King')),

    # ---------------------------------------------------------------- Breaking Bad
    C('walter', 'Walter White', 'breakingbad', 'M', H, 'Protagoniste', ('Ruse',), '🥼 🧪 🎩', ('Walter', 'Heisenberg', 'Walt')),
    C('jesse', 'Jesse Pinkman', 'breakingbad', 'M', H, 'Allié', ('Ruse',), '🧢 🧪 🗣️', ('Jesse',)),
    C('gus', 'Gus Fring', 'breakingbad', 'M', H, 'Antagoniste', ('Ruse',), '👓 🤝 🍗', ('Gustavo Fring', 'Gus')),
    C('saul', 'Saul Goodman', 'breakingbad', 'M', H, 'Allié', ('Ruse',), '📺 💼 ⚖️', ('Saul',)),
    C('hank', 'Hank Schrader', 'breakingbad', 'M', H, 'Rival', ('Arme',), '🍺 🪨 🔫', ('Hank',)),

    # ---------------------------------------------------------------- Peaky Blinders
    C('tommy', 'Thomas Shelby', 'peakyBlinders', 'M', H, 'Protagoniste', ('Ruse', 'Arme'), '🚬 🐎 🧢', ('Tommy Shelby', 'Tommy')),
    C('arthur', 'Arthur Shelby', 'peakyBlinders', 'M', H, 'Allié', ('Corps à corps',), '🥃 👊 🧢', ('Arthur',)),
    C('polly', 'Polly Gray', 'peakyBlinders', 'F', H, 'Allié', ('Ruse',), '🔮 💰 🧢', ('Polly', 'Tante Polly')),

    # ---------------------------------------------------------------- La Casa de Papel
    C('professeur', 'Le Professeur', 'casapapel', 'M', H, 'Protagoniste', ('Ruse',), '👓 🗺️ 🧠 🏦', ('Professeur', 'Sergio Marquina')),
    C('tokyo', 'Tokyo', 'casapapel', 'F', H, 'Protagoniste', ('Arme',), '🏍️ 🔫 🎙️', ()),
    C('berlin', 'Berlin', 'casapapel', 'M', H, 'Allié', ('Ruse',), '🍷 🎭 🎩', ()),
    C('nairobi', 'Nairobi', 'casapapel', 'F', H, 'Allié', ('Ruse',), '🧡 🖨️ 💵', ()),

    # ---------------------------------------------------------------- Stranger Things
    C('eleven', 'Eleven', 'strangerthings', 'F', H, 'Protagoniste', ('Pouvoir inné',), '🧇 🩸 🧠 1️⃣1️⃣', ('Onze', 'El'),
      ("Elle déplace les objets par la pensée, au prix d'un saignement de nez.", 'Télékinésie')),
    C('mike', 'Mike Wheeler', 'strangerthings', 'M', H, 'Protagoniste', ('Ruse',), '🎲 📻 🚲', ('Mike',)),
    C('dustin', 'Dustin Henderson', 'strangerthings', 'M', H, 'Allié', ('Ruse',), '🧢 🦷 🦎', ('Dustin',)),
    C('steve', 'Steve Harrington', 'strangerthings', 'M', H, 'Allié', ('Arme',), '💇 🍦 🏏', ('Steve',)),
    C('hopper', 'Jim Hopper', 'strangerthings', 'M', H, 'Allié', ('Arme',), '🍩 🚔 🤠', ('Hopper',)),

    # ---------------------------------------------------------------- Squid Game
    C('gihun', 'Seong Gi-hun', 'squidgame', 'M', H, 'Protagoniste', ('Ruse',), '🍬 🦑 4️⃣5️⃣6️⃣', ('Gi-hun', 'Joueur 456')),
    C('sangwoo', 'Cho Sang-woo', 'squidgame', 'M', H, 'Rival', ('Ruse',), '📈 🦑 2️⃣1️⃣8️⃣', ('Sang-woo', 'Joueur 218')),
    C('saebyeok', 'Kang Sae-byeok', 'squidgame', 'F', H, 'Allié', ('Ruse',), '🔪 🦑 0️⃣6️⃣7️⃣', ('Sae-byeok', 'Joueuse 067')),

    # ---------------------------------------------------------------- Friends
    C('ross', 'Ross Geller', 'friends', 'M', H, 'Protagoniste', ('Aucun',), '💍 🛋️ 🦕', ('Ross',)),
    C('rachel', 'Rachel Green', 'friends', 'F', H, 'Protagoniste', ('Aucun',), '✈️ 👗 ☕ 💇‍♀️', ('Rachel',)),
    C('monica', 'Monica Geller', 'friends', 'F', H, 'Protagoniste', ('Aucun',), '🦃 🧽 👩‍🍳', ('Monica',)),
    C('chandler', 'Chandler Bing', 'friends', 'M', H, 'Protagoniste', ('Aucun',), '😏 🦆 🐤', ('Chandler',)),
    C('joey', 'Joey Tribbiani', 'friends', 'M', H, 'Protagoniste', ('Aucun',), '🎭 🐧 🍕 🥪', ('Joey',)),
    C('phoebe', 'Phoebe Buffay', 'friends', 'F', H, 'Protagoniste', ('Aucun',), '🦞 🎸 🐈', ('Phoebe',)),

    # ---------------------------------------------------------------- Vikings
    C('ragnar', 'Ragnar Lothbrok', 'vikings', 'M', H, 'Protagoniste', ('Arme', 'Ruse'), '👑 ⛵ 🪓 🐍', ('Ragnar',)),
    C('lagertha', 'Lagertha', 'vikings', 'F', H, 'Protagoniste', ('Épée',), '👸 ⚔️ 🛡️', ()),
    C('floki', 'Floki', 'vikings', 'M', H, 'Allié', ('Ruse',), '🤪 🔨 🛶', ()),

    # ---------------------------------------------------------------- Harry Potter
    C('harry', 'Harry Potter', 'harrypotter', 'M', H, 'Protagoniste', ('Magie',), '🧹 🦉 👓 ⚡', ('Harry',)),
    C('hermione', 'Hermione Granger', 'harrypotter', 'F', H, 'Allié', ('Magie', 'Ruse'), '🐈 ⏳ 📚', ('Hermione',)),
    C('ron', 'Ron Weasley', 'harrypotter', 'M', H, 'Allié', ('Magie',), '♟️ 🕷️ 🐀', ('Ron',)),
    C('dumbledore', 'Albus Dumbledore', 'harrypotter', 'M', H, 'Mentor', ('Magie',), '🧦 🍋 🧙', ('Dumbledore',)),
    C('voldemort', 'Voldemort', 'harrypotter', 'M', H, 'Antagoniste', ('Magie',), '💀 👃 🐍', ('Lord Voldemort', 'Tom Jedusor', 'Vous-Savez-Qui')),
    C('rogue', 'Severus Rogue', 'harrypotter', 'M', H, 'Mentor', ('Magie',), '🖤 🦌 🧪', ('Rogue', 'Snape')),
    C('hagrid', 'Rubeus Hagrid', 'harrypotter', 'M', ('Demi-géant',), 'Allié', ('Aucun',), '🏍️ 🐉 🎂', ('Hagrid',)),
    C('dobby', 'Dobby', 'harrypotter', 'M', ('Elfe de maison',), 'Allié', ('Magie',), '🙏 🧝 🧦', ()),
    C('drago', 'Drago Malefoy', 'harrypotter', 'M', H, 'Rival', ('Magie',), '🧹 👱‍♂️ 🐍', ('Drago', 'Draco')),

    # ---------------------------------------------------------------- Le Seigneur des Anneaux
    C('frodon', 'Frodon Sacquet', 'lotr', 'M', ('Hobbit',), 'Protagoniste', ('Épée',), '🦶 🌋 💍', ('Frodon', 'Frodo')),
    C('sam', 'Samsagace Gamegie', 'lotr', 'M', ('Hobbit',), 'Allié', ('Épée',), '🌱 🍳 🥔', ('Sam', 'Samwise')),
    C('gandalf', 'Gandalf', 'lotr', 'M', ('Maia',), 'Mentor', ('Magie', 'Épée'), '🎆 🐴 🧙', ()),
    C('aragorn', 'Aragorn', 'lotr', 'M', H, 'Protagoniste', ('Épée',), '🌲 🗡️ 👑', ('Grands-Pas',)),
    C('legolas', 'Legolas', 'lotr', 'M', ('Elfe',), 'Allié', ('Arme',), '🌳 🛡️ 🏹', ()),
    C('gimli', 'Gimli', 'lotr', 'M', ('Nain',), 'Allié', ('Arme',), '🧔 ⛏️ 🪓', ()),
    C('gollum', 'Gollum', 'lotr', 'M', ('Hobbit',), 'Neutre', ('Ruse',), '🐟 🪨 💍', ('Sméagol',)),
    C('sauron', 'Sauron', 'lotr', 'M', ('Maia',), 'Antagoniste', ('Magie',), '🔥 💍 👁️', ()),

    # ---------------------------------------------------------------- Star Wars
    C('luke', 'Luke Skywalker', 'starwars', 'M', H, 'Protagoniste', ('Épée', 'Énergie'), '🌅 🌅 ✋ 🟢', ('Luke',)),
    C('leia', 'Leia Organa', 'starwars', 'F', H, 'Protagoniste', ('Arme',), '📜 🔫 👑 🥯', ('Leia', 'Princesse Leia')),
    C('han', 'Han Solo', 'starwars', 'M', H, 'Allié', ('Arme',), '🔫 🚀 🧊', ('Han',)),
    C('vador', 'Dark Vador', 'starwars', 'M', H, 'Antagoniste', ('Épée', 'Énergie'), '😮‍💨 🔴 🖤 👨‍👦', ('Vador', 'Darth Vader', 'Anakin Skywalker')),
    C('yoda', 'Yoda', 'starwars', 'M', ('Inconnue',), 'Mentor', ('Énergie', 'Épée'), '🪵 👂 🟢', ()),
    C('chewbacca', 'Chewbacca', 'starwars', 'M', ('Wookiee',), 'Allié', ('Arme',), '🗣️ 🏹 🐻', ('Chewie',)),
    C('obiwan', 'Obi-Wan Kenobi', 'starwars', 'M', H, 'Mentor', ('Épée', 'Énergie'), '🏜️ 👋 🔵', ('Obi-Wan', 'Ben Kenobi')),

    # ---------------------------------------------------------------- Marvel
    C('ironman', 'Iron Man', 'marvel', 'M', H, 'Protagoniste', ('Arme', 'Ruse'), '🍔 💰 ❤️ 🦾', ('Tony Stark', 'Tony')),
    C('cap', 'Captain America', 'marvel', 'M', H, 'Protagoniste', ('Arme', 'Corps à corps'), '🧊 ⭐ 🛡️', ('Steve Rogers', 'Cap')),
    C('thor', 'Thor', 'marvel', 'M', ('Asgardien',), 'Protagoniste', ('Arme', 'Pouvoir inné'), '🌈 ⚡ 🔨', ()),
    C('hulk', 'Hulk', 'marvel', 'M', H, 'Allié', ('Corps à corps', 'Pouvoir inné'), '🧪 😡 💚', ('Bruce Banner', 'Banner')),
    C('blackwidow', 'Black Widow', 'marvel', 'F', H, 'Allié', ('Corps à corps', 'Arme'), '🖤 ⌛ 🕷️', ('Natasha Romanoff', 'Natasha')),
    C('thanos', 'Thanos', 'marvel', 'M', ('Titan',), 'Antagoniste', ('Corps à corps', 'Pouvoir inné'), '💜 💎 🧤 🫰', ()),
    C('loki', 'Loki', 'marvel', 'M', ('Géant des glaces',), 'Antagoniste', ('Magie', 'Ruse'), '🐍 🐊 🪄', ()),
    C('spiderman', 'Spider-Man', 'marvel', 'M', H, 'Protagoniste', ('Pouvoir inné',), '🎒 🕸️ 🕷️', ('Peter Parker', 'Spiderman')),
    C('strange', 'Doctor Strange', 'marvel', 'M', H, 'Allié', ('Magie',), '🧣 🌀 🧿', ('Docteur Strange', 'Stephen Strange')),

    # ---------------------------------------------------------------- Pokémon
    C('sacha', 'Sacha', 'pokemon', 'M', H, 'Protagoniste', ('Invocation',), '🏅 🧢 ⚡', ('Ash', 'Sacha Ketchum')),
    C('pikachu', 'Pikachu', 'pokemon', 'M', ('Pokémon',), 'Allié', ('Pouvoir inné',), '🍅 🐭 ⚡', ()),
    C('mewtwo', 'Mewtwo', 'pokemon', 'N', ('Pokémon',), 'Antagoniste', ('Pouvoir inné',), '🧬 🥄 🧠', ()),
    C('pierre', 'Pierre', 'pokemon', 'M', H, 'Allié', ('Invocation',), '🍳 😍 🪨', ('Brock',)),
    C('ondine', 'Ondine', 'pokemon', 'F', H, 'Allié', ('Invocation',), '🚲 💧', ('Misty',)),

    # ---------------------------------------------------------------- Minecraft
    C('steve_mc', 'Steve', 'minecraft', 'M', H, 'Protagoniste', ('Arme',), '🟦 🧱 ⛏️', ()),
    C('creeper', 'Creeper', 'minecraft', 'N', ('Monstre',), 'Antagoniste', ('Pouvoir inné',), '😶 🟩 💥', ()),
    C('enderman', 'Enderman', 'minecraft', 'N', ('Monstre',), 'Neutre', ('Pouvoir inné',), '👀 🟪 📦', ()),
    C('enderdragon', "Ender Dragon", 'minecraft', 'N', ('Dragon',), 'Antagoniste', ('Pouvoir inné',), '🥚 🟪 🐉', ('Dragon de l\'Ender',)),

    # ---------------------------------------------------------------- GTA V
    C('michael', 'Michael De Santa', 'gta', 'M', H, 'Protagoniste', ('Arme',), '🎬 🍸 🏠', ('Michael',)),
    C('franklin', 'Franklin Clinton', 'gta', 'M', H, 'Protagoniste', ('Arme',), '🚗 🐕', ('Franklin',)),
    C('trevor', 'Trevor Philips', 'gta', 'M', H, 'Protagoniste', ('Arme',), '🤪 🏜️ 🪓', ('Trevor',)),
    C('lester', 'Lester Crest', 'gta', 'M', H, 'Allié', ('Ruse',), '🦯 💻', ('Lester',)),

    # ---------------------------------------------------------------- Zelda
    C('link', 'Link', 'zelda', 'M', ('Hylien',), 'Protagoniste', ('Épée', 'Arme'), '🏹 🛡️ 🟢 🗡️', ()),
    C('zelda', 'Zelda', 'zelda', 'F', ('Hylien',), 'Allié', ('Magie',), '✨ 🔺 👑', ('Princesse Zelda',)),
    C('ganondorf', 'Ganondorf', 'zelda', 'M', ('Gerudo',), 'Antagoniste', ('Magie', 'Épée'), '🏜️ 🔺 🐗', ('Ganon',)),

    # ---------------------------------------------------------------- Mario
    C('mario', 'Mario', 'mario', 'M', H, 'Protagoniste', ('Corps à corps',), '🔴 🪠 🍄', ()),
    C('luigi', 'Luigi', 'mario', 'M', H, 'Allié', ('Corps à corps',), '🔦 👻 🟢', ()),
    C('peach', 'Peach', 'mario', 'F', H, 'Allié', ('Aucun',), '🏰 👑 🍑', ('Princesse Peach',)),
    C('bowser', 'Bowser', 'mario', 'M', ('Koopa',), 'Antagoniste', ('Pouvoir inné',), '👑 🔥 🐢', ()),
    C('yoshi', 'Yoshi', 'mario', 'M', ('Dinosaure',), 'Allié', ('Pouvoir inné',), '🥚 👅 🦖', ()),

    # ---------------------------------------------------------------- Frieren (2 novembre)
    C('frieren', 'Frieren', 'frieren', 'F', ('Elfe',), 'Protagoniste', ('Magie',), '⏳ 📖 🌸 🧝', (),
      ("Depuis plus de mille ans, elle dissimule en permanence l'intensité réelle de son mana.", 'Dissimulation du mana')),
    C('fern', 'Fern', 'frieren', 'F', H, 'Allié', ('Magie',), '💜 😤 🪄', ()),
    C('stark', 'Stark', 'frieren', 'M', H, 'Allié', ('Arme',), '😰 🐉 🪓', ()),
    C('himmel', 'Himmel', 'frieren', 'M', H, 'Allié', ('Épée',), '🗡️ 💍 🗿', ()),
    C('eisen', 'Eisen', 'frieren', 'M', ('Nain',), 'Allié', ('Arme',), '🧔 🪓', ()),
    C('heiter', 'Heiter', 'frieren', 'M', H, 'Allié', ('Magie',), '⛪ 🍷', ()),
    C('aura', 'Aura', 'frieren', 'F', ('Démon',), 'Antagoniste', ('Magie',), '🧟 💀 ⚖️', ('Aura la Guillotine',),
      ("Une balance qui compare son mana à celui de l'adversaire : le plus faible devient sa marionnette.", '')),

    # ---------------------------------------------------------------- Chainsaw Man (16 novembre)
    C('denji', 'Denji', 'chainsawman', 'M', ('Hybride',), 'Protagoniste', ('Pouvoir inné', 'Arme'), '🍞 🐶 🪚', (),
      ("Il tire sur un cordon qui sort de sa poitrine et des lames jaillissent de son corps.", 'Chainsaw Man')),
    C('power', 'Power', 'chainsawman', 'F', ('Démon',), 'Allié', ('Pouvoir inné',), '😈 🐱 🩸', (),
      ("Elle façonne son propre sang en armes.", 'Manipulation du sang')),
    C('aki', 'Aki Hayakawa', 'chainsawman', 'M', H, 'Allié', ('Épée', 'Invocation'), '🚬 🗡️ 🦊', ('Aki',)),
    C('kobeni', 'Kobeni Higashiyama', 'chainsawman', 'F', H, 'Allié', ('Arme',), '😭 🍔 🔪', ('Kobeni',)),

    # ---------------------------------------------------------------- Spy × Family (30 novembre)
    C('loid', 'Loid Forger', 'spyfamily', 'M', H, 'Protagoniste', ('Ruse', 'Arme'), '👔 🎭 🕵️', ('Twilight', 'Loid')),
    C('yor', 'Yor Forger', 'spyfamily', 'F', H, 'Protagoniste', ('Arme',), '🍳 🌹 🗡️', ('Yor', 'Princesse Ibara')),
    C('anya', 'Anya Forger', 'spyfamily', 'F', H, 'Protagoniste', ('Pouvoir inné',), '👧 🧠 🥜', ('Anya',),
      ("Elle lit dans les pensées des personnes autour d'elle.", 'Télépathie')),
    C('bond', 'Bond Forger', 'spyfamily', 'M', ('Chien',), 'Allié', ('Pouvoir inné',), '🤍 🐕 🔮', ('Bond',),
      ("Il voit des images de l'avenir.", 'Précognition')),
]

# ---------------------------------------------------------------- Devine l'univers : 5 indices, du plus vague au plus précis
UNIVERS = {
    'naruto': ["Un village caché dans la forêt", "Des examens pour monter en grade", "Un démon renard scellé dans un nouveau-né",
               "Des bols de ramen chez Ichiraku", "Un garçon blond qui rêve de devenir Hokage"],
    'onepiece': ["Une mer coupée en quatre par une muraille de terre rouge", "Des fruits qui font perdre la capacité de nager",
                 "Des primes sur des avis de recherche", "Un chapeau de paille confié à un enfant", "Le trésor légendaire de Gol D. Roger"],
    'aot': ["Une humanité retranchée derrière trois murs", "Un équipement de manœuvre tridimensionnelle",
            "Le Bataillon d'exploration", "Des géants qui dévorent les humains", "Eren, Mikasa et Armin"],
    'demonslayer': ["Le Japon de l'ère Taishō", "Des sabres dont la lame change de couleur", "Des techniques de respiration",
                    "Une sœur qui voyage dans une boîte en bois", "Tanjiro et les Piliers"],
    'bleach': ["Un lycéen qui voit les fantômes", "Des âmes à guider vers la Soul Society", "Des sabres qui ont un nom et un esprit",
               "Des Hollows masqués", "Ichigo, Shinigami remplaçant"],
    'jjk': ["Un lycée de Tokyo très particulier", "Des émotions négatives qui prennent forme",
            "Les doigts d'un roi maudit à rassembler", "Des extensions du territoire", "Gojo et Itadori"],
    'mha': ["80 % de la population possède un pouvoir", "Un lycée qui forme des professionnels", "Un classement officiel des héros",
            "Un pouvoir qui se transmet", "Deku et All Might"],
    'fairytail': ["Le royaume de Fiore", "Une guilde turbulente et soudée", "Des chasseurs de dragons", "Des clés célestes",
                  "Natsu, Lucy et Happy"],
    'hxh': ["Un examen mortel pour obtenir une licence", "Un père parti à l'aventure", "Une famille d'assassins", "Le Nen",
            "Gon et Killua"],
    'deathnote': ["Un objet tombé du ciel près d'un lycée", "Un dieu de la mort qui adore les pommes", "Un détective qui s'assoit accroupi",
                  "Écrire un nom pour tuer", "Kira"],
    'fmab': ["Une transmutation humaine qui tourne mal", "Une armure vide qui parle", "Le principe de l'échange équivalent",
             "Des homoncules aux noms de péchés capitaux", "Les frères Elric"],
    'dragonball': ["Une queue de singe", "Un nuage magique pour voyager", "Sept boules à réunir", "Un dragon qui exauce un vœu", "Son Goku"],
    'onepunchman': ["Des monstres qui attaquent la ville", "Une Association des héros avec des classes",
                    "Un cyborg qui veut devenir disciple", "Un héros devenu chauve à force d'entraînement", "Saitama"],
    'inazuma': ["Un club de collège menacé de fermeture", "Le carnet de techniques d'un grand-père",
                "Des tirs spéciaux aux noms spectaculaires", "Le tournoi Football Frontier", "Mark Evans"],
    'bluelock': ["Le Japon éliminé de la Coupe du monde", "300 attaquants réunis dans un même lieu",
                 "Un projet pour créer le buteur le plus égoïste", "Jinpachi Ego", "Isagi"],
    'soloLeveling': ["Des portails qui mènent à des donjons", "Des chasseurs classés de E à S",
                     "Le chasseur le plus faible du monde", "Un système qui donne des quêtes quotidiennes", "Sung Jin-Woo"],
    'got': ["Des saisons qui durent des années", "Un immense mur de glace au nord", "Un trône forgé avec des épées",
            "« L'hiver vient »", "Les Stark et les Lannister"],
    'breakingbad': ["Albuquerque, au Nouveau-Mexique", "Un camping-car transformé en laboratoire",
                    "Un professeur de chimie gravement malade", "Une drogue bleue d'une pureté record", "Heisenberg"],
    'peakyBlinders': ["Birmingham après la Première Guerre mondiale", "Des paris sur les courses de chevaux",
                      "Une famille de gangsters", "Des lames cousues dans les casquettes", "Thomas Shelby"],
    'casapapel': ["Des noms de villes en guise de pseudonymes", "Des combinaisons rouges", "Des masques de Dalí",
                  "La Fabrique nationale de la monnaie et du timbre", "Le Professeur"],
    'strangerthings': ["Une petite ville de l'Indiana dans les années 1980", "Des parties de Donjons et Dragons",
                       "Un laboratoire secret", "Le Monde à l'envers", "Eleven"],
    'squidgame': ["456 joueurs criblés de dettes", "Des gardes en combinaison rose", "Une poupée géante",
                  "« Un, deux, trois, soleil »", "Seong Gi-hun"],
    'friends': ["Un appartement à Manhattan", "Un café avec un grand canapé orange", "« On faisait une pause ! »",
                "Central Perk", "Ross et Rachel"],
    'vikings': ["Des raids vers l'ouest", "Kattegat", "Un constructeur de bateaux excentrique", "Le pillage de Lindisfarne",
                "Ragnar Lothbrok"],
    'harrypotter': ["Une lettre apportée par une chouette", "Le quai 9 ¾", "Un chapeau qui répartit les élèves", "Le Quidditch",
                    "Poudlard"],
    'lotr': ["Une communauté de neuf marcheurs", "Une montagne de feu", "La Comté", "Un anneau pour les gouverner tous", "Frodon"],
    'starwars': ["Une planète désertique éclairée par deux soleils", "Une station capable de détruire une planète",
                 "Un contrebandier et son copilote poilu", "Des sabres lumineux", "Dark Vador"],
    'marvel': ["Une scène cachée après le générique", "Un milliardaire en armure", "Un bouclier rond étoilé",
               "Les Pierres d'Infinité", "Les Avengers"],
    'pokemon': ["Huit badges à collectionner", "Un professeur qui offre un premier compagnon", "Des balls rouges et blanches",
                "Une souris électrique jaune", "« Attrapez-les tous »"],
    'minecraft': ["Un monde généré à l'infini", "Des nuits dangereuses", "Un portail d'obsidienne", "Un monstre vert qui explose",
                  "Steve et les creepers"],
    'gta': ["Une ville inspirée de Los Angeles", "Trois personnages jouables", "Des braquages préparés en plusieurs étapes",
            "Los Santos", "Michael, Franklin et Trevor"],
    'zelda': ["Une épée qui repousse le mal", "Une relique en trois parties : Force, Sagesse et Courage", "Un ocarina",
              "Hyrule", "Link"],
    'mario': ["Un royaume peuplé de champignons", "Des tuyaux verts", "Une princesse régulièrement enlevée",
              "Un plombier moustachu", "Bowser"],
    'lol': ["La Faille de l'invocateur", "Trois voies et une jungle", "Un Nexus à détruire", "Le monde de Runeterra",
            "Ahri, Jinx et Yasuo"],
    'valorant': ["Un jeu de tir tactique en cinq contre cinq", "Un Spike à poser ou à désamorcer",
                 "Des agents aux capacités uniques", "La Radianite", "Jett et Sage"],
    'eafc': ["Des cartes de joueurs à collectionner", "Des DCE à compléter", "La Chimie entre les joueurs",
             "Le mode Ultimate Team", "Le successeur de FIFA"],
    'frieren': ["Une aventure qui commence après la victoire", "Une elfe qui vit plus de mille ans",
                "Une collection de sorts inutiles", "Le Roi démon vaincu par le héros Himmel", "Frieren"],
    'chainsawman': ["Des démons nés des peurs humaines", "Un garçon écrasé de dettes",
                    "Les chasseurs de démons de la Sécurité publique", "Un petit chien-tronçonneuse", "Denji"],
    'spyfamily': ["Deux pays voisins en pleine guerre froide", "Une famille formée pour une mission", "L'école d'élite Eden",
                  "Un espion, une tueuse et une télépathe", "Anya"],
}

MODES = [
    ('personnage', 'Personnage', '🎯', "Devine le personnage du jour. Chaque essai révèle ce qu'il a en commun avec la cible."),
    ('pouvoir', 'Pouvoir', '⚡', "Une technique ou un pouvoir est décrit sans nom : à qui appartient-il ?"),
    ('emoji', 'Emoji', '😶', "Un personnage résumé en emojis, révélés un par un à chaque erreur."),
    ('univers', 'Univers', '🌍', "Cinq indices, du plus vague au plus précis : de quelle œuvre parle-t-on ?"),
]
