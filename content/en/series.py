"""English metadata for the series (name, URL slug, tagline, two intro paragraphs).

Keyed by the series key used in content/series.py. Only verifiable facts, translated from the French
intros, with the official English names of works and characters.
"""

SERIES = {
    # ------------------------------------------------------------ ANIME
    'naruto': dict(slug='naruto', name='Naruto',
        tag="Ninjas, tailed beasts and the Akatsuki, from Genin to Hokage across both parts.",
        intro=[
            "Published by Masashi Kishimoto in Weekly Shōnen Jump from 1999 to 2014, Naruto tells, over 700 chapters, the story of an orphan from the Hidden Leaf who carries the Nine-Tailed Fox inside him and dreams of becoming Hokage. Together with One Piece and Bleach, it formed what readers call the “Big Three” of the 2000s.",
            "The quiz covers Naruto and Naruto Shippuden: Team 7, the clans of the Leaf Village, the jutsu (Rasengan, Chidori, Sharingan), the Akatsuki and the Fourth Great Ninja War. Easy questions focus on the main characters, the hardest ones on clan family trees and the details of the final arcs.",
        ]),
    'onepiece': dict(slug='one-piece', name='One Piece',
        tag="Pirates, Devil Fruits and Emperors on the road to Laugh Tale.",
        intro=[
            "Started in 1997 by Eiichiro Oda, One Piece follows Monkey D. Luffy, a boy with a rubber body who wants to find Gol D. Roger's legendary treasure and become King of the Pirates. With more than 500 million copies in print, it is the most published comic series ever by a single author.",
            "The quiz travels from the East Blue saga to the latest arcs: the Straw Hat crew, Devil Fruits and their three types, the Emperors, the Marines, the World Government and the mysteries of the Void Century. Bounties and the links between characters are the ground of the toughest questions.",
        ]),
    'aot': dict(slug='attack-on-titan', name='Attack on Titan',
        tag="Eren, Mikasa and the Titans: humanity behind its walls.",
        intro=[
            "Hajime Isayama published Attack on Titan from 2009 to 2021. In a world where the last humans live behind three giant walls to escape the Titans, Eren Yeager joins the Survey Corps after Wall Maria falls. The anime adaptation ended in 2023.",
            "The questions cover the four seasons and the manga: the Nine Titans and their holders, the history of Eldia and Marley, the omni-directional mobility gear, the great revelations of the Yeager basement and the ending. A good memory for names and for how powers are passed on makes the difference.",
        ]),
    'demonslayer': dict(slug='demon-slayer', name='Demon Slayer',
        tag="Tanjiro, Nezuko and the Demon Slayer Corps.",
        intro=[
            "Demon Slayer: Kimetsu no Yaiba was published by Koyoharu Gotouge from 2016 to 2020. In Taishō-era Japan, Tanjiro Kamado joins the Demon Slayer Corps to avenge his family and give his sister Nezuko, turned into a demon, her humanity back. Studio Ufotable's adaptation is praised for its animation.",
            "The quiz is about the Breathing styles and their forms, the nine Hashira, Muzan Kibutsuji's Twelve Kizuki and the major arcs, from Mount Natagumo to the Infinity Castle. The details of the techniques and the human past of the demons feed the hard questions.",
        ]),
    'bleach': dict(slug='bleach', name='Bleach',
        tag="Ichigo, the Soul Reapers and their Zanpakutō, between two worlds.",
        intro=[
            "Tite Kubo's Bleach ran from 2001 to 2016. Ichigo Kurosaki, a high schooler who can see spirits, becomes a substitute Soul Reaper and gets caught up in the conflicts of the Soul Society, the Hollows and later the Quincy. The final arc, the Thousand-Year Blood War, has been adapted as an anime since 2022.",
            "The questions focus on the Gotei 13 and its captains, the Zanpakutō and their Bankai, Aizen's Espada, the Sternritter and the spiritual world of the series. The names of the sword releases are the big trap of this quiz.",
        ]),
    'jjk': dict(slug='jujutsu-kaisen', name='Jujutsu Kaisen',
        tag="Yuji, Gojo and Sukuna: cursed energy in modern Japan.",
        intro=[
            "Jujutsu Kaisen was published by Gege Akutami from 2018 to 2024. After swallowing a finger of Ryomen Sukuna, the King of Curses, high schooler Yuji Itadori joins Tokyo Jujutsu High. Studio MAPPA's adaptation played a large part in the series' worldwide success.",
            "The quiz covers innate techniques, Domain Expansions, the great clans (Gojo, Zen'in, Kamo), the Shibuya Incident and the rest of the manga. The rules of binding vows and how techniques work are at the heart of the advanced questions.",
        ]),
    'mha': dict(slug='my-hero-academia', name='My Hero Academia',
        tag="Deku, All Might and Quirks: the school for heroes.",
        intro=[
            "Kōhei Horikoshi published My Hero Academia from 2014 to 2024. In a world where most people have a Quirk, Izuku Midoriya, born without one, inherits All Might's One For All and enters U.A. High School to become a pro hero.",
            "The questions are about Class 1-A and its Quirks, the pro heroes, the League of Villains, the successive holders of One For All and the major arcs up to the final war. The exact limits of each power often come up in the hard questions.",
        ]),
    'fairytail': dict(slug='fairy-tail', name='Fairy Tail',
        tag="Mavis Vermillion's guild: magic and adventure in the Kingdom of Fiore.",
        intro=[
            "Hiro Mashima's Fairy Tail ran from 2006 to 2017 before continuing with Fairy Tail: 100 Years Quest. The series follows Natsu Dragneel, Lucy Heartfilia, Gray, Erza and Happy in the rowdiest wizard guild of the Kingdom of Fiore.",
            "The quiz covers the guilds, the different kinds of magic (Dragon Slayers, Celestial Spirits, Requip), major arcs such as Tenrou Island and the Grand Magic Games, and the story of Zeref and Mavis. The bonds between dragons and Dragon Slayers are a classic of the trickier questions.",
        ]),
    'hxh': dict(slug='hunter-x-hunter', name='Hunter × Hunter',
        tag="Gon, Killua and Nen: a world of rare depth.",
        intro=[
            "Hunter × Hunter has been published by Yoshihiro Togashi since 1998, with long breaks. Gon Freecss takes the Hunter Exam to find his father Ging and becomes friends with Killua Zoldyck, heir to a family of assassins. The 148-episode adaptation from 2011 remains the reference for many fans.",
            "The quiz explores the Hunter Exam, Heavens Arena, Yorknew City and the Phantom Troupe, Greed Island, the Chimera Ant arc and the election. Nen, its six categories and the conditions that strengthen an ability are at the heart of the most demanding questions.",
        ]),
    'deathnote': dict(slug='death-note', name='Death Note',
        tag="Light, L and Ryuk: the duel over the notebook of death.",
        intro=[
            "Written by Tsugumi Ohba and drawn by Takeshi Obata, Death Note ran from 2003 to 2006 for 108 chapters and was adapted into 37 episodes. High schooler Light Yagami finds a notebook that kills anyone whose name is written in it, and starts a crusade that pits him against the detective L.",
            "The questions focus on the rules of the notebook, Shinigami such as Ryuk and Rem, L's successors, the Japanese police investigation and Light's strategies. Knowing the exact rules, and the ones Light made up, is essential for the hard questions.",
        ]),
    'fmab': dict(slug='fullmetal-alchemist', name='Fullmetal Alchemist',
        tag="Ed and Al Elric, alchemy and the Philosopher's Stone.",
        intro=[
            "Hiromu Arakawa's Fullmetal Alchemist was published from 2001 to 2010. After a failed human transmutation, Edward Elric loses a leg and an arm, and his brother Alphonse loses his whole body, his soul bound to a suit of armor. The Brotherhood adaptation (2009-2010) follows the manga faithfully.",
            "The quiz covers the principles of alchemy and equivalent exchange, the State Alchemists, the seven Homunculi, the country of Xing and the conspiracy eating away at the Amestris military. The story of Ishval and the identity of Father feed the hard questions.",
        ]),
    'dragonball': dict(slug='dragon-ball', name='Dragon Ball',
        tag="Goku, Vegeta and the Saiyans: fights that shake whole planets.",
        intro=[
            "Akira Toriyama's Dragon Ball ran from 1984 to 1995 and deeply shaped action manga. First inspired by Journey to the West, the story of Son Goku continues with Dragon Ball Z, Dragon Ball Super and Dragon Ball Daima, released in 2024, the year Toriyama died.",
            "The questions cover the Saiyan, Frieza, Cell and Buu sagas, then the Super era: transformations, techniques such as the Kamehameha or the Spirit Bomb, side characters and universes. The order of the transformations and the names of the techniques are the usual traps.",
        ]),
    'onepunchman': dict(slug='one-punch-man', name='One Punch Man',
        tag="Saitama and the Hero Association: winning with a single punch.",
        intro=[
            "Born as a webcomic by the author ONE in 2009, One Punch Man has been redrawn by Yūsuke Murata since 2012. Saitama, a hero so strong that he wins every fight with one punch, is bored stiff and struggles to get recognition from the Hero Association.",
            "The quiz is about the hero rankings and classes, Dragon- and God-level threats, Genos, Garou and the Monster Association. The series parodies superhero tropes: the humor and absurd details are part of the questions too.",
        ]),
    'inazuma': dict(slug='inazuma-eleven', name='Inazuma Eleven',
        tag="Raimon, special moves and legendary tournaments.",
        intro=[
            "Inazuma Eleven is a Level-5 video game series launched in 2008 on Nintendo DS and quickly adapted into an anime. Mark Evans, goalkeeper at Raimon Junior High, gathers a team to save the soccer club and face opponents with spectacular special moves.",
            "The questions cover the original series, Inazuma Eleven GO and its sequels: the teams, the special moves (hissatsu), the Keshin fighting spirits and the tournaments. The names of the moves vary a lot between the Japanese and the localized versions, which makes some questions tricky.",
        ]),
    'bluelock': dict(slug='blue-lock', name='Blue Lock',
        tag="300 strikers, one goal scorer: Isagi, Rin and ego as a weapon.",
        intro=[
            "Blue Lock has been published since 2018, written by Muneyuki Kaneshiro and drawn by Yūsuke Nomura. The Japan Football Union locks 300 young strikers in a training facility to produce the world's best egotist striker. Yoichi Isagi discovers there a vision of soccer built on reading the game.",
            "The quiz covers the successive selections, the match against the U-20 national team, the Neo Egoist League and its clubs, and each player's personal weapon. Quotes and move names are on the program of the hard questions.",
        ]),
    'soloLeveling': dict(slug='solo-leveling', name='Solo Leveling',
        tag="The weakest hunter becomes the Shadow Monarch.",
        intro=[
            "Solo Leveling is a Korean web novel by Chugong, adapted as a webtoon from 2018 to 2021 with art by Dubu, then as an anime by A-1 Pictures from 2024. Sung Jinwoo, an E-rank hunter said to be the weakest of all, receives a mysterious “System” that makes him level up like a video game character.",
            "The questions focus on the System and its quests, the shadow army (Igris, Beru, Bellion…), the S-rank hunters, the dungeons and the Monarchs. The names of the shadows and the order of events are the tricky parts.",
        ]),
    # ------------------------------------------------------------ TV SERIES
    'got': dict(slug='game-of-thrones', name='Game of Thrones',
        tag="Westeros, the Starks, the Lannisters and the war for the Iron Throne.",
        intro=[
            "Adapted from George R. R. Martin's A Song of Ice and Fire, Game of Thrones aired on HBO from 2011 to 2019 over eight seasons. The great houses of Westeros fight over the Iron Throne while the threat of the White Walkers grows beyond the Wall. The spin-off House of the Dragon goes back to the Targaryen dynasty.",
            "The quiz covers the houses and their words, the characters, the dragons, the Night's Watch, the great battles and the making of the show. Family ties and house words are the classics of the hard questions.",
        ]),
    'breakingbad': dict(slug='breaking-bad', name='Breaking Bad',
        tag="Walter White, from chemistry teacher to Heisenberg.",
        intro=[
            "Created by Vince Gilligan, Breaking Bad aired on AMC from 2008 to 2013. Walter White, a chemistry teacher in New Mexico diagnosed with cancer, starts cooking methamphetamine with his former student Jesse Pinkman. The universe continues with Better Call Saul and the film El Camino.",
            "The questions are about the characters, the cartels, Gus Fring, the DEA, key episodes and famous lines. The details of the final season and the links with Better Call Saul make up the hardest questions.",
        ]),
    'peakyBlinders': dict(slug='peaky-blinders', name='Peaky Blinders',
        tag="Birmingham, 1919: the Shelby family rules through fear.",
        intro=[
            "Created by Steven Knight, Peaky Blinders aired on the BBC from 2013 to 2022. In Birmingham after the First World War, Thomas Shelby, played by Cillian Murphy, turns the family gang into a powerful organization, from the local underworld all the way to Parliament.",
            "The quiz covers the Shelby family, its allies and enemies, the political intrigue of the interwar years and memorable lines. Tommy's successive rivals and the timeline of the seasons are on the program of the advanced questions.",
        ]),
    'casapapel': dict(slug='money-heist', name='Money Heist',
        tag="The Professor, the Dalí masks and the heist of the century.",
        intro=[
            "Created by Álex Pina, Money Heist (La Casa de Papel) first aired in Spain on Antena 3 in 2017, before Netflix made it famous worldwide and extended it until 2021. A mysterious Professor brings together robbers nicknamed after cities to raid the Royal Mint of Spain, then the Bank of Spain.",
            "The questions focus on the robbers and their nicknames, the Professor's plans, the negotiations with the police and the cult moments. The characters' real first names are one of this quiz's favorite traps.",
        ]),
    'strangerthings': dict(slug='stranger-things', name='Stranger Things',
        tag="Hawkins, the Upside Down and Eleven against the darkness.",
        intro=[
            "Created by the Duffer brothers, Stranger Things has streamed on Netflix since 2016 and ended with a fifth season in late 2025. In the small town of Hawkins, Indiana, in the 1980s, the disappearance of Will Byers reveals a parallel world and secret experiments carried out on a young girl, Eleven.",
            "The quiz covers the characters, the creatures of the Upside Down, Hawkins Lab, the seasons and the many references to 1980s pop culture.",
        ]),
    'squidgame': dict(slug='squid-game', name='Squid Game',
        tag="456 players, deadly children's games and 45.6 billion won.",
        intro=[
            "Created by Hwang Dong-hyuk, Squid Game was released on Netflix in 2021 and became one of the platform's most watched series. Hundreds of people buried in debt agree to take part in children's games whose losers are eliminated. Season 2 came out in late 2024 and season 3, which ends the story, in 2025.",
            "The questions focus on the games, the players and their numbers, Seong Gi-hun, the organization of the guards and the Front Man, and the revelations of the later seasons.",
        ]),
    'friends': dict(slug='friends', name='Friends',
        tag="Rachel, Monica, Phoebe, Ross, Chandler and Joey at Central Perk.",
        intro=[
            "Friends, created by David Crane and Marta Kauffman, aired on NBC from 1994 to 2004 over ten seasons and 236 episodes. Six friends in New York share their love lives, jobs and mishaps between Monica's apartment and the Central Perk coffee house.",
            "The quiz is about the characters, the couples, the Thanksgiving episodes, iconic lines and celebrity guest appearances. The details of the running gags are the fans' best weapon.",
        ]),
    'vikings': dict(slug='vikings', name='Vikings',
        tag="Ragnar Lothbrok, Lagertha and the raids from the North.",
        intro=[
            "Created by Michael Hirst, Vikings aired on History from 2013 to 2020 over six seasons. Inspired by the sagas, it follows the rise of Ragnar Lothbrok, a simple farmer who becomes king, and then the fate of his sons. The spin-off Vikings: Valhalla continues the story a century later.",
            "The quiz covers the characters, Norse mythology, the raids on England and France, the voyages and the historical background of the Viking Age.",
        ]),
    # ------------------------------------------------------------ FILMS
    'harrypotter': dict(slug='harry-potter', name='Harry Potter',
        tag="Hogwarts, the four houses and the fight against Voldemort.",
        intro=[
            "J. K. Rowling's Harry Potter saga has seven novels published from 1997 to 2007, adapted into eight films from 2001 to 2011. At eleven, Harry learns that he is a wizard, starts at Hogwarts and gradually faces Lord Voldemort, the dark wizard who killed his parents.",
            "The quiz covers Hogwarts and its houses, the teachers, the spells, the creatures, the Ministry of Magic, the Horcruxes and the Deathly Hallows. The exact names of spells and the family trees of wizarding families are the classic traps.",
        ]),
    'lotr': dict(slug='lord-of-the-rings', name='The Lord of the Rings',
        tag="Frodo, Gandalf and Middle-earth.",
        intro=[
            "J. R. R. Tolkien's The Lord of the Rings was published in three volumes in 1954 and 1955. Frodo's quest to destroy the One Ring in the fires of Mount Doom founded modern fantasy. Peter Jackson's trilogy (2001-2003) won 17 Academy Awards in total.",
            "The questions cover the Fellowship of the Ring, the peoples of Middle-earth, the places, the weapons, the magic and Tolkien's work beyond the films, including The Hobbit.",
        ]),
    'starwars': dict(slug='star-wars', name='Star Wars',
        tag="The Force, the Jedi, the Sith and the Skywalker saga.",
        intro=[
            "Created by George Lucas, with a first film released in 1977, Star Wars became one of the most influential sagas in cinema. The original trilogy, the prequels and the sequels tell the story of the Skywalker family, expanded since Disney's acquisition in 2012 by many films and series.",
            "The quiz covers the characters, the Force, the Jedi and the Sith, the planets, the ships, the technology and the making of the films.",
        ]),
    'marvel': dict(slug='marvel', name='Marvel (MCU)',
        tag="The Avengers, Thanos and the Infinity Stones.",
        intro=[
            "The Marvel Cinematic Universe began in 2008 with Iron Man and became the highest-grossing franchise in film history. The Infinity Saga ended in 2019 with Avengers: Endgame, before the Multiverse Saga opened in theaters and on Disney+.",
            "The questions are about the heroes and their villains, the Infinity Stones, Asgard, the Guardians of the Galaxy, the films and series, as well as the cast and famous lines.",
        ]),
    # ------------------------------------------------------------ VIDEO GAMES
    'pokemon': dict(slug='pokemon', name='Pokémon',
        tag="Types, legendaries and champions, from Kanto to Paldea.",
        intro=[
            "Pokémon was born in Japan in 1996 with Game Freak's Red and Green games, created by Satoshi Tajiri. The series now has more than 1,000 species across nine generations, and it is the highest-grossing entertainment franchise in history.",
            "The quiz covers types and their weaknesses, starter and legendary Pokémon, regions, Gym Leaders, game mechanics, the anime and the history of the franchise. The type chart remains the basis of any good game.",
        ]),
    'minecraft': dict(slug='minecraft', name='Minecraft',
        tag="Survival, building, mobs and biomes.",
        intro=[
            "Created by Markus “Notch” Persson and published by Mojang from 2009, Minecraft was bought by Microsoft in 2014. It is the best-selling video game of all time, with more than 300 million copies sold.",
            "The questions are about survival, crafting recipes, mobs, biomes, the Nether and the End, and the game's major updates.",
        ]),
    'gta': dict(slug='gta-v', name='GTA V',
        tag="Michael, Trevor and Franklin in Los Santos.",
        intro=[
            "Released in 2013, Rockstar Games' Grand Theft Auto V is one of the best-selling games in history. You play three criminals, Michael, Franklin and Trevor, in Los Santos, a satirical version of Los Angeles. Its online mode, GTA Online, is still being updated.",
            "The quiz covers the characters, the city and its surroundings, the heists, the missions, GTA Online and the Easter eggs hidden in the game.",
        ]),
    'zelda': dict(slug='zelda', name='The Legend of Zelda',
        tag="Link, Zelda, Ganon and the Triforce.",
        intro=[
            "The Legend of Zelda is a Nintendo series created by Shigeru Miyamoto and Takashi Tezuka, whose first game came out in 1986. Link most often faces Ganon to protect the kingdom of Hyrule. Breath of the Wild (2017) and Tears of the Kingdom (2023) reinvented the series as an open world.",
            "The questions focus on the characters, items, dungeons, the different games and the official timeline of the series.",
        ]),
    'mario': dict(slug='super-mario', name='Super Mario',
        tag="The Mushroom Kingdom, Bowser and power-ups.",
        intro=[
            "Mario first appeared in 1981 in Donkey Kong, created by Shigeru Miyamoto, before becoming Nintendo's mascot with Super Mario Bros. in 1985. 2D and 3D platformers, racing, sports, party games: few characters have tried so many genres.",
            "The quiz covers the characters of the Mushroom Kingdom, power-ups, worlds, items and the history of the games.",
        ]),
    'lol': dict(slug='league-of-legends', name='League of Legends',
        tag="Champions, roles, objectives and the lore of Runeterra.",
        intro=[
            "Released in 2009, Riot Games' League of Legends pits two teams of five champions against each other on Summoner's Rift. It is one of the most played games in the world and one of the flagship esports, while the animated series Arcane brought its universe to a wide audience.",
            "The questions are about the champions, roles and lanes, map objectives, summoner spells, esports and the history of Runeterra.",
        ]),
    'valorant': dict(slug='valorant', name='Valorant',
        tag="Agents, the Spike and the maps of Riot's tactical shooter.",
        intro=[
            "Released in 2020, Valorant is Riot Games' tactical shooter. Two teams of five fight over planting and defusing a bomb, the Spike, combining precise aim with each agent's own abilities.",
            "The quiz covers the agents and their roles, the maps, the weapons, the game mechanics and the competitive scene.",
        ]),
    'eafc': dict(slug='ea-sports-fc', name='EA Sports FC',
        tag="Ultimate Team, SBCs, Chemistry and FUT Coins.",
        intro=[
            "EA Sports FC succeeded Electronic Arts' FIFA series in 2023, after the licensing deal with world soccer's governing body ended. The game keeps the licenses of most major leagues and its flagship mode, Ultimate Team.",
            "The questions are about Ultimate Team (Chemistry, SBCs, TOTW, FUT Coins), Career Mode, players and clubs, and the history of the series since FIFA.",
        ]),
    # ------------------------------------------------------------ GENERAL KNOWLEDGE
    'culture': dict(slug='general-knowledge', name='General knowledge',
        tag="Science, literature, art, philosophy and math.",
        intro=[
            "General knowledge is everything that helps you understand the world beyond your own field. This quiz draws on the main areas of knowledge to test how broad your knowledge is rather than how deep.",
            "The questions cover science, geography, literature, art and music, philosophy and math, from school level to the details that separate the enthusiasts.",
        ]),
    'histoire': dict(slug='history', name='History',
        tag="From Antiquity to the world wars.",
        intro=[
            "This quiz travels through human history, from the first civilizations to the great conflicts of the 20th century. Dates, figures, battles and treaties: a way to check what you remember from school, and learn along the way.",
            "The questions cover Antiquity, the Middle Ages, revolutions, the world wars, the history of France and world history, including the Cold War and the age of exploration.",
        ]),
    'geo': dict(slug='geography', name='Geography',
        tag="Capitals, natural records, countries and oceans.",
        intro=[
            "Geography describes the Earth and how humans live on it. This quiz takes you from one continent to another to test what you know about countries, their capitals and the great natural records.",
            "The questions are about capitals, continents, countries, oceans and seas, records (highest peak, longest river…) and the geography of France.",
        ]),
    'sport': dict(slug='sport', name='Sports',
        tag="Soccer, tennis, athletics and the Olympic Games.",
        intro=[
            "This quiz brings together the major sports, their flagship competitions and the athletes who defined their era. From World Cups to the Olympic Games, records and honors are on the menu.",
            "The questions cover soccer, athletics, basketball, tennis, rugby, the Olympic Games and many other sports, from boxing to cycling.",
        ]),
    'musique': dict(slug='music', name='Music',
        tag="French rap, global pop, rock and classic albums.",
        intro=[
            "From French chanson to rap, from pop to rock, this quiz crosses genres and eras. Artists, albums, records and anecdotes from the history of popular music are on the program.",
            "The questions are about French rap, global pop, rock, great artists, landmark albums and the history of recorded music.",
        ]),
    'cinema': dict(slug='cinema', name='Cinema',
        tag="Oscars, directors, cult films and the box office.",
        intro=[
            "Born at the end of the 19th century, cinema has never stopped reinventing itself, from silent films to blockbusters. This quiz tests your film culture, from Hollywood classics to French and world cinema.",
            "The questions are about the Oscars, directors, cult films, the box office, animation, actors and cinema from around the world.",
        ]),
    # ------------------------------------------------------------ SCHEDULED SERIES
    'frieren': dict(slug='frieren', name='Frieren',
        tag="The elf mage, the late hero and the long journey north.",
        intro=[
            "Frieren: Beyond Journey's End, written by Kanehito Yamada and drawn by Tsukasa Abe, has been published in Weekly Shōnen Sunday since 2020. The story begins where adventure stories usually stop: the Demon King is defeated, and Frieren, an elf mage who will live for centuries more, watches her human companions grow old and pass away. The manga won the Manga Taishō in 2021, and studio Madhouse's adaptation was one of the most acclaimed anime of 2023-2024.",
            "The quiz covers the hero Himmel's party, Frieren's new journey with Fern and Stark, magic and its great spells, demons such as Aura the Guillotine, the First-Class Mage Exam and the making of the series. One set of questions is also about the meaning of the characters' German names.",
        ]),
    'chainsawman': dict(slug='chainsaw-man', name='Chainsaw Man',
        tag="Denji, Pochita and Public Safety against the devils.",
        intro=[
            "Tatsuki Fujimoto's Chainsaw Man first ran in Weekly Shōnen Jump from 2018 to 2020, before a second part published on Shōnen Jump+ since 2022. Denji, a teenager crushed by debt, merges with his dog-devil Pochita and becomes a hybrid who can make chainsaws burst out of his body. Recruited by the mysterious Makima, he joins Public Safety's devil hunters.",
            "The questions are about the characters, the devils and their contracts, the difference between fiends and hybrids, the major arcs of Part 1, studio MAPPA's anime and the film about Reze. Beware: some hard questions reveal the ending of Part 1.",
        ]),
    'spyfamily': dict(slug='spy-x-family', name='Spy × Family',
        tag="A spy, an assassin and a telepath under one roof.",
        intro=[
            "Tatsuya Endo's Spy × Family has been published on Shōnen Jump+ since 2019. To get close to a dangerous politician, the spy Twilight has to enroll a child in an elite school. He adopts Anya, unaware that she can read minds, and marries Yor, unaware that she is an assassin. The adaptation by Wit Studio and CloverWorks made the Forger family one of the most popular in recent anime.",
            "The quiz covers the Forger family and their dog Bond, the spy agencies of Westalis and Ostania, Eden Academy and its system of Stellas and Tonitrus Bolts, and the making of the manga, the anime and the film Code: White.",
        ]),
    'haikyu': dict(slug='haikyu', name='Haikyu!!',
        tag="The Karasuno Crows on their way to conquer national volleyball.",
        intro=[
            "Haruichi Furudate's Haikyu!! ran in Weekly Shōnen Jump from 2012 to 2020, in 45 volumes. Shoyo Hinata, too short for volleyball but gifted with a phenomenal jump, enters Karasuno High to follow in the footsteps of his idol, the Little Giant. There he meets Tobio Kageyama, a genius setter who beat him in middle school. Together, they invent a quick attack that wakes up a team that had fallen into obscurity. Production I.G's adaptation made the manga one of the biggest sports successes on screen.",
            "The quiz covers the Karasuno players, their great rivals from Aoba Johsai, Nekoma, Shiratorizawa and Inarizaki, the matches that defined the series, the rules of volleyball and the making of the work. A few hard questions are about what becomes of the characters after high school.",
        ]),
    'arcane': dict(slug='arcane', name='Arcane',
        tag="Vi, Jinx and the war between Piltover and Zaun.",
        intro=[
            "Arcane, created by Christian Linke and Alex Yee, is an animated series by Riot Games, made by the French studio Fortiche and streamed on Netflix in two seasons, in 2021 and 2024. It is set in the world of League of Legends, between Piltover, the rich City of Progress, and Zaun, the undercity that spreads out beneath it. At the heart of the story are two sisters, Vi and Powder, whom tragedy turns into enemies, and two inventors, Jayce and Viktor, who give birth to hextech. The series won the Emmy for Outstanding Animated Program in 2022.",
            "The quiz covers the characters, the two cities and their tensions, hextech and Shimmer, the great moments of the story and the making of the series. Be warned: some hard questions mention events from the second season.",
        ]),
}
