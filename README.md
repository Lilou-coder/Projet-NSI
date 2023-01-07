# Projet-NSI
Projet NSI avec Juliette CHEM-LENHOF, Alexandre EGUERRE, Lilou COLLE


 Calendrier : 
            
            Semaine 1 : Choisir et définir le projet + créer le ReadMe ainsi que s'inscrire sur Github ( Lilou, Alexandre, Juliette)
            Semaine 2 : Definition du cahier des charges + description précises de chaque page du jeu + choisir le nom du jeu ("Kraken")
            Semaine 3 : Definir le calendrier et s'attribuer les tâches ( Lilou, Alexandre, Juliette)
            Semaine 4 : Clear and change database (Lilou) + questions ( Juliette et Alexandre) 
            Semaine 5 : Page numéro 3 (Lilou, Juliette) et 4 (Alexandre)
            Semaine 6 : Page 5 + vision des paramètres: time( Alexandre), variable qui compte le score( Alexandre), choix des questions - dictionnaire? (Lilou) ) 
            Semaine 7 : Page 5 - affichage des questions (Juliette) et réponses (Lilou) + bonus? (Alexandre)
            Semaine 8 : Finaliser page 5 ( Lilou, Alexandre, Juliette)
            Semaine 9 : Page 6 - animation : deux bateaux représentant les deux joueurs et le kraken englouti celui du perdant (Alexandre, Juliette) + vérification du fonctionnement (Lilou)
            Semaine 10 : Finalisation et debuggage du jeu (Alexandre,Juliette) - button return (Lilou)
            Semaine 11 : design (Juliette) et vérification du fonctionnement (Lilou et Alexandre) 
            Semaine 12 : 
            Semaine 13 : Finaliser / debuger (Lilou, Alexandre, Juliette)
            Semaine 14 : Finaliser / debuger (Lilou, Alexandre, Juliette)
            Semaine 15 : Finaliser / debuger (Lilou, Alexandre, Juliette)
            

Notre idée :Kraken
            
            Un site intéractif où les utilisateur pourront se confronter à des questions de culture générale et communiquer simultanément.
            
            Les utilisateurs pourront s'affonter sur divers sujets avec un temps limité, et le choix du nombre de questions est accordé aux joueurs (max de 15)              
            Il y aura les thèmes d'histoire, de géographie, des siences et vie de la terre et de mathématiques.
                        - on préparera 30 questions pour chaque thême qui seront choisi au hasard dépendant du choix de l'utilisateur
            Les questions se presenteront sous forme de QCM avec une présentation coloré et ludique.
            Le site s'utilisera principalement avec la souris et éventuellement avec le clavier.
            Il se joura en un contre un.
            Il se presentera en 2d.
            Le nombre de points donné par la question diminura avec le temps.
            Il y aura une musique d'ambiance.
            Il y aura un systeme de bonus pour certaines bonnes réponses pour destabiliser ou penaliser l'adversaire.
            Il prends pour inspiartion kahoot.
            
 Plan : 
            
            1er page : 
            - Afin d'accéder au jeu, il faut d'abord s'inscrire ou se connecter. La première page en accédant le site sera donc une page avec ces deux    boutons(database avec utilisateur et mot-de-passe crypté).    
            - Sur cette première page, en scrollant, il y aura les règles du jeu. 
            
            2ème page : Homepage
            - Bouton play, qui accédera à une autre page
            - Bouton contactez nous : si le joueur a une idée ou un bug, il peut nous contacter
            
            3ème page : choisir le thème
            - 4 bouton : Histoire, Géo, Maths, SVT - décidera des questions 
            - en appuyant sur l'un des boutons, on passe à la 4ème page
            
            4ème page : paramêtre de jeux
            - Nombre de questions sera compris entre 5 et 15 --> scroll down, choisi par l'utilisateur
            - Temps pour chaque questions sera compris entre 5 et 15 secondes --> scroll down, choisi par l'utilisateur
            - bouton inviter une personne (2 joueurs qui jouent en même temps max)
            - bouton commencer la partie - une notification pop-up apparaîtra quand quelqu'un est invité en haut de la page ou dans le chat
            
            5ème page : gameplay
            - en haut à gauche le temps dans une case qui s'écoule et qui se remet au max à chaque question
            - la question en haut centrée
            - quatres cases avec les réponses
            - plus l'utilisateur prend du temps à repondre, moins il y a de points
            - (un malus apparaît quand l'autre à gagné, un pop-up d'encre qui cache la vision de la page de l'autre)
            
            6 ème page : 
            - page du gagnant, nombre de point affiché
            - animation kraken qui mange l'utilisateur qui a perdu
            - bouton qui renvoie à la page principale
            
 Choses à faire : 
            
            - vérifier le site : meme apology, changer le database, corriger "if user tries to log in with same username as another"
            - faire les question pour le jeu - 120 en tout (Juliette) 
            - avoir une nouvelle page pour le jeu en lui même qui n'apparait que lorsqu'on appuie sur le bouton 'jouer' sur le homepage
            - une page pour les paramètres
            - créer le logo
            - créer les animations 
            - installer le systeme de bonus : encre, enlever deux réponses, regarder la réponse de l'autre
            - créer la page intéractif pour le jeux avec les boutons 
            - design du site (Juliette) 
            - refaire les catégories du database (Lilou) 
            
            
Questions Geographie:
           
           1-Parmis les etats suivants, lequel n'est pas membre du Commonwealth 
              1)les Etats-Unis
              2)l'Inde
              3)l'Australie
              4)le Ghana 
            2-Quel pays a pour capitale Gaborone ?
              1)le Botswana
              2)le Zimbabwe
              3)la Tanzanie 
              4)le Lesotho 
            3-Quelle est la capitale de la Suisse ?
              1)Berne
              2)Bâle
              3)Zuric
              4)Lausanne
            4-Combien d'états fédérés l'Inde compte-t-elle? 
              1)29
              2)30
              3)31
              4)32
            5-Quelles sont les langues officielles de l'Afghanistan?
              1)Persan et Pashtou
              2)Arabe et Turc 
              3)Afghan et Anglais 
              4) Hindi et Persan 
            6-Quelle ville compte la plus haute densité de population du monde? 
              1)Manille 
              2)Delhi 
              3)Sanghai 
              4)le Caire 
            7-Quel pays est le moins densément peuplé au monde? 
              1)la Mongolie 
              2)l'Australie
              3)l'Arabie Saoudite
              4)le Belarus 
            8-De quel pays Beyrouth est-elle la capitale? 
              1)Liban 
              2)Laos 
              3)Syrie 
              4)Cambodge
            9-De quel pays Londres est-elle la capitale?
              1)Royaume-Uni
              2)France 
              3)Andorre 
              4)Allemagne 
            10-Combien y a t'il de départements en France (dont outre-mer)? 
              1)100
              2)96
              3)104
              4)98
            11-Quel est l'autre nom de la France? 
              1)l'Hexagone 
              2)le triangle
              3)la baguette
              4)le pays des illuminations 
            12-Où se trouve le Mont-Saint-Michel?
              1)en Normandie
              2)en Bretagne 
              3)sur la côte d'azur 
              4)en Ile de France 
            13-Combien de volcans d'Auvergne sont encore actifs? 
              1)0
              2)2
              3)4
              4)1
            14-Quelle mer borde la Côte d'Azur? 
              1)la mer Méditerranée 
              2)la mer Noire 
              3)la Manche 
              4)la mer du Sud 
            15-Quelle ville de France compte le pplus d'habitants? 
              1)Toulouse 
              2)Nice 
              3)Nantes
              4)Lille 
            16-Quel est le fleuve le plus long de France?
              1)la Loire 
              2)la Moselle 
              3)le Rhône 
              4)la Seine 
            17-Quel est le sommet le plus haut d'Europe?
              1)le Mont Blanc
              2)le Mont Rose
              3)le Kilimandjaro
              4)le Mont Ventoux 
            18-Combien de régions la France compte-t-elle?
              1)18
              2)27
              3)22
              4)13
            19-Avec combien de pays le France métropolitaine a-t-elle une frontiere terrestre? 
              1)8
              2)7
              3)6
              4)9
            20-A combien de kilomètres de Paris se trouve le départements français le plus éloigné?
              1)9180km
              2)947km
              3)855km
              4)6800km
            21-Laquelle de ces îles est française? 
              1)la Martinique
              2)Hawaii
              3)Sainte-Lucie
              4)la Sardaigne
            22-Combien la France métropolitaine compte-t-elle de mers et d'océans autour d'elle? 
              1)4
              2)3
              3)5
              4)2
            23-Quel pourcentage d'habitants en France habite en ville? 
              1)82%
              2)78%
              3)69%
              4)86%
            24-Depuis quelle ville Française le tunnel sous la Manche relie-t-il la France et l'Angleterre?
              1)Calais 
              2)le Havre 
              3)Dunkerque 
              4)Dieppe 
            25-Parmis ces villes, laquelle se situe le pluis au nord de la France?
              1)Lyon 
              2)Marseille
              3)Bordeaux 
              4)Grenoble
            26-Quel départements est le moins peuplé de France? 
              1)la Lozère
              2)le Gers 
              3)la Creuze
              4)le Cher 
            27-Depuis 2016, combien y a-t-il de régions en France métropolitaine? 
              1)13
              2)5
              3)17
              4)24
            28-En 2018, combien y'avait-il d'habitants en France? 
              1)67.2 millions 
              2)58.6 millions 
              3)69.5 millions 
              4)64.2 millions 
            29-Quelle est la ville la plus étendue du territoire français? 
              1)Maripasoula 
              2)Arles 
              3)Paris 
              4)Lyon 
            30-Quelle est la ville la plus vieille de France? 
              1)Béziers
              2)Marseille 
              3)Bordeaux 
              4)Nice 
             
Questions Histoire:
 
            1-Lequel de ces pharaons a régné en premier?
                       1)Akhénaton
                       2)Cléopâtre
                       3)Toutânkhamon
                       4)Ramsès II
            2-Quel est le premier peuple à obtenir le droit de vote des citoyens?
                       1)Les Anthéniens
                       2)Les Romains
                       3)Les Scandinaves
                       4)Les Cambodgiens
            3-Qui est l’ennemi de la France pendant la guerre de Cent ans?
                       1)L'Angletterre
                       2)L'Espagne
                       3)La Prusse
                       4)L'Empire Ottoman
            4-Quelle est l’année de la Déclaration d’Indépendance des Etats-Unis?
                       1)1776
                       2)1802
                       3)1658
                       4)1697
            5-Quelle bataille de Napoléon est une défaite ?
                       1)Warterloo
                       2)Austerlitz
                       3)Wagram
                       4)Tea Party
            6-En quelle année a été détruit le mur de Berlin ?
                        1)1989
                        2)1945
                        3)1991
                        4)1947
            7-En quelle année a eut lieux la crise des missiles de Cuba?
                        1)1962
                        2)1974
                        3)2001
                        4)2004
            8-En quelle année a été conclu le pacte de Varsovie?
                        1)1955
                        2)1945
                        3)1939
                        4)1918
            9-En quelle année la guerre de corée a-t-elle commencée?
                        1)1950
                        2)1962
                        3)1948
                        4)1964
            10-Quand l'écriture a-t-elle inventé?
                        1)-3200
                        2)-5400
                        3)-6000
                        4)-4600
            11-En 1 500 av. J.-C., la conquête du territoire français commence avec?
                        1)les Celtes
                        2)les Arabes
                        3)les Belges
                        4)les romains
            12-Clovis Ier est le fondateur de la dynastie?
                        1)mérovingienne
                        2)carolingienne
                        3)des Louis
                        4)des Charles
            13-Charlemagne est couronné empereur d’Occident par le pape Léon III en l’an?
                        1)800
                        2)600
                        3)700
                        4)900
            14-Le premier roi des Francs fut?
                        1)Clovis 1er
                        2)Clovis 2nd
                        3)Charlemagne
                        4)Louis 1er
            15-Quelle est la date historique de la célébration de l’Épiphanie pour les catholiques ?
                        1)6 janvier
                        2)4 janvier
                        3)12 janvier
                        4)2 jamvier
            16-En quelle année est né Charles de Gaulle ?
                        1)1890
                        2)1860
                        3)1900
                        4)1880
            17-Comment s'appelait l'héritier du trône d'Autriche durant la première guerre mondiale ?
                        1)François-Ferdinand
                        2)Francois-Maximilien
                        3)Francois-Karl
                        4)François-Alexandre
            18-Quand l'armistice de la 1er guerre mondiale a-t-il été signé?
                        1)11 novembre 1918
                        2)15 novembre 1918
                        3)8 novembre 1918
                        4)21 novembre 1918
            19-Quand La Russie signe-t-elle un traité de paix séparé avec l'Allemagne ?
                        1)1917
                        2)1918
                        3)1920
                        4)1914
            20-Quelle guerre a duré de 1756 à 1763 ?
                        1)La guerre d’indépendance
                        2)La guerre de Trente Ans
                        3)La guerre de Sept Ans
                        4)La guerre de Succession d’Autriche
            21-Que se passe-t-il le 16 décembre 1773 ?
                        1)La Boston Tea Party
                        2)Le Sugar Act
                        3)La Déclaration d’indépendance
                        4)Le traité de Paris
            22-Quelle est la capitale politique et intellectuelle de la Nouvelle-Angleterre ?
                        1)Boston
                        2)Philadelphie
                        3)New York
                        4)Baltimore
            23-Quelles sont les conséquences du traité de Paris ?
                        1)La France perd la Louisiane
                        2)La France récupère le Canada
                        3)L’Espagne perd les 13 colonies
                        4)L’Angleterre gagne la Californie
                        
                        
                        
Questions SVT: 

           1-Combien de degrés comporte l’échelle de Richter permettant de mesurer l’énergie libérée lors d’un séisme ?
             1)en theorie un nombre infini
             2)7
             3)11
             4)9
           2-Quel animal est le plus gros du monde? 
             1)Baleine bleu
             2)Rhinoceros 
             3)Baleine blanche 
             4)Elephant 
           3-Quel animal est Bambi?
             1)Biche 
             2)Cerf
             3)Grenouille 
             4)Singe 
           4-Quel animal ne boit pas d'eau? 
             1)Koala 
             2)Chat
             3)Panda 
             4)Tortue 
           5-Quel animal insolite a été retrouvé à Rennes le 1er juillet 2016? 
             1)Cachalot 
             2)Dauphin
             3)Beluga 
             4)Buffle 
           6-Quel animal dort le plus? 
             1)Koala 
             2)Paresseux
             3)Chat
             4)Chameaux 
           7-Quel animal a pour nom scientifique "Passer domesticus"?
             1)Moineau 
             2)Panda 
             3)Paresseux 
             4)Chat
           8-Quel est le nom scientifique de la truite? 
             1)Salmo marmoratus
             2)Truitus maurus 
             3)Bos taurus taurus
             4)Rhincoson typus
           9-Quel animal a pour nom scientifique "Scorpio maurus"? 
             1)Arachnide
             2)Oiseau
             3)Moustique 
             4)Escargot 
           10-Quel est le nom scientifique des loup gris? 
             1)Canis lupus 
             2)Chelonia lupus 
             3)Lupus grisulus 
             4)Felis sylvestris catus
           11-Un taureau peut-il porter un bébé dans son ventre ?
             1)Non car c'est un mâle
             2)Oui car la femelle ne peut pas
             3)Non car c'est un ovipare
             4)Oui car c'est un vivipare 
           12-Quel animal est ovipare?
             1)Le criquet
             2)La vache
             3)La chèvre
             4)Le panda
           13-Quel animal est vivipare?
             1)L'éléphant
             2)Le crocodile
             3)Le moineau
             4)Le criquet
           14-Qu'est-ce qu'un animal vivipare?
             1)C'est un animal dont l'embryon se développe à l'intérieur de la mère
             2)C'est un animal qui pond des œufs pour se reproduire
             3)C'est un animal dont les oeufs sont à l'intérieur de la femelle
             4)C'est un animal qui pond des embryons
           15-Les œufs sont-ils toujours entourés d'une coquille?
             1)Non, certaines espèces animales ont des œufs mous
             2)Non, la poule est la seule espèce à avoir des œufs avec une coquille
             3)Oui, les œufs sont toujours entourés d'une coquille pour les protéger
             4)Oui sauf pour les serpents
           16-A quel ordre d'animaux appartient l'ornithorynque? 
             1)Monotrèmes
             2)Anseriformes 
             3)Diprotodontes
             4)Rongeurs 
           17-Quel est l’animal qui retint l’attention du naturaliste et paléontologue Charles Darwin lors de son voyage dans l’archipel des Galapagos et dont l’observation des particularismes insulaires a participé de sa théorie de l’évolution sur l’origine des espèce?
             1)Pinson
             2)Iguane
             3)Tortue Géante
             4)Ver de Terre 
           18-De quelle espèce de primate l’être humain actuel est-il le plus proche génétiquement ?
             1)Chimpanzé 
             2)Bonobo
             3)Gorille 
             4)Orang-Outan
           19-De quels animaux les lamantins et les dugongs sont-ils les plus proches dans la liste ci-dessous ?
             1)Elephants 
             2)Dauphins 
             3)Hippopotames 
             4)Phoques 
           20-Combien existe-t-il d’espèces de lions vivant actuellement ?
             1)Une seule 
             2)Deux 
             3)Huit
             4)Vingt 
           21-Un de ces animaux n’est pas un primate : lequel ?
             1)Couscous 
             2)Aye-Aye 
             3)Galago 
             4)Loris 
           22-Parmi les 4 espèces ci-dessous, il y a un intrus qui ne fait pas partie des Ophidiens : lequel ?
             1)Orvet 
             2)Boa constricteur
             3)Cobra 
             4)Vipere 
           23-Lequel de ces animaux n'est pas un rongeur? 
             1)Musaraigne
             2)Castor 
             3)Chien de prairie 
             4)Capybara
           24-Combien existe-t-il officiellement d'especes d'éléphant? 
             1)3
             2)2
             3)1
             4)4
           25-Parmi ces 4 oiseaux, lequel n’appartient pas à l’ordre des Psittaciformes (perroquets et perruches) ?
             1)Macareux moine 
             2)Cacatoes 
             3)Loris
             4)Conures
           26-Quel continent est constitué de glace et entouré d'eau? 
             1)Pôle sud 
             2)Pôle nord
             3)Les deux 
             4)Ni l'un ni l'autre
           27-Où vit le petit pingouin ?
             1)Pôle nord 
             2)Pôle sud 
             3)Les deux 
             4)Ni l'un ni l'autre 
           28-Parmi les 4 caractéristiques de l'ornithorynque ci-dessous, il en est une qui est fausse : laquelle ?
             1)Il fait son nid dans un arbre 
             2)Il pond des oeufs 
             3)Il est venimeux 
             4)Son pelage est fluorescent dans la nuit 
           29-Parmi les 4 espèces d'oiseaux ci-dessous, il en est une qui n'est pas présente en Australie : laquelle ?
             1)Kakapo
             2)Emeu 
             3)Cacatoès à Huppe Jaune 
             4)Casoar à casque 
           30-Comment les Australiens surnomment-ils les petits des marsupiaux (koala, kangourou, etc) ?
             1)Joey
             2)Bibi
             3)Teddy
             4)Winny 
             
          
           
          
           
            
          
        
             
        
             
             
             
            
         

            
            
            
            
            
            
           
