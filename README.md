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
             



            
            
            
            
            
            
           
