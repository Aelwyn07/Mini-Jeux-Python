from NiveauxAllumettes import niv1, niv2, niv3
import time

def demande_joueur(nombre_allumette)->int:
    """
    Fonction pour demander le nombre d'allumettes à retirer aux joueurs

    Entrée : la fonction n'a besoin d'aucun paramètre en entrée.
    Sortie : un entier
    
    """
    allumettes_supp : str
    allumettes_supp = str(input("Combien d'allumettes retirez vous ?  "))
    
    while allumettes_supp == '':
        allumettes_supp = str(input("Veuillez entrez un nombre : "))
    
    while int(allumettes_supp) < 1 or int(allumettes_supp) > 3 or int(allumettes_supp) > nombre_allumette:
        print("Choisissez un nombre entre 1 et 3 s'il vous plaît !")
        allumettes_supp = str(input("Combien d'allumettes retirez vous ? "))

        while allumettes_supp == '':
            allumettes_supp = str(input("Veuillez entrez un nombre : "))
    
    
    return int(allumettes_supp)


def demande_ordis(n, nb_all)->int:
    """
    Fonction qui permet à l'ordinateur de jouer en fonction du niveau défini en début de partie
    
    Entrée: .l'entier n qui représente le niveau de l'ordinateur qui a été choisi avant la  partie
            .l'entier nb_all qui représente le nombre d'allumettes encore dans la partie
            
    Sortie: .l'entier nb qui est le nombre d'allumettes que va choisir de retirer l'ordinateur
    """
    if n == 1:
        nb = niv1(nb_all)
    elif n == 2:
        nb = niv2(nb_all)
    else:
        nb = niv3(nb_all)
    return nb


def manche(definir_joueur: int, niveau: int, nbj: int)->int:
    """
    Fonction qui permet de jouer une manche

    Entrée : un entier 'definir_joueur' qui est égal à 1 ou 2 et permet de savoir quel joueur commence le tour
    Sortie : un entier 'definir_joueur' qui renvoie le joueur qui a gagné la manche

    """
    nombre_allumette: int
    retirer: int

    nombre_allumette = 20

    print(" \n        Il y a 20 allumettes ! \n ")

    while nombre_allumette>0:


        #Conditions pour que le joueur (ou l'ordinateur) retire une ou des allumette(s).
        if nbj == 2:
            retirer = demande_joueur(nombre_allumette)
        elif nbj == 1:
            if definir_joueur == 2:
                retirer = demande_ordis(niveau, nombre_allumette)
            else:
                retirer = demande_joueur(nombre_allumette)
        else:
            retirer = demande_ordis(niveau, nombre_allumette)

        nombre_allumette = nombre_allumette - retirer

        #Condition pour permettre de passer à l'autre joueur
        if definir_joueur==2:
            definir_joueur=1
        else:
            definir_joueur=2

        #Condition pour savoir si un joueur a gagné ou non
        if nombre_allumette==0:
            print("")
            print("***************************************************")
            print("Le joueur",(definir_joueur),"a gagné ! Il n'y a plus d'allumettes !")
            print("***************************************************")
            return definir_joueur

        #Affichage du nombre d'allumettes restants
        if nbj == 0 or (nbj == 1 and definir_joueur == 1):
            print("L'ordinateur a retiré ", retirer, "allumettes")
        print(" \n        Il reste",nombre_allumette,"allumettes \n ")
        print("Au tour du joueur",(definir_joueur))






def allumette()->list:
    """
    Fonction qui permet de lancer une partie (une partie est composé de deux manches de manière à ce que chaque joueur puisse commencer)
   
    Entrée: Pas de paramètres d'entrée
    Sortie: Liste qui contient les scores de la partie

    """
    jouer: bool
    score_j1: int
    score_j2: int
    scorej1: int
    scorej2: int
    partie1: int
    partie2: int
    rejouer: str
    niveau: int
    pseudo1: str
    pseudo2: str
    nbj: int

    #Affectation des variables
    jouer = True
    score_j1 = 0
    score_j2 = 0

    #Boucle qui permet de jouer une partie
    while jouer == True:
        print("-----------------------")
        print("  Options de la partie ")
        print("-----------------------")
        print("1 - Faire une partie entre deux joueurs")
        print("2 - Faire une partie contre un ordinateur")
        print("3 - Faire une partie entre deux ordinateurs")
        choix = int(input("Veillez saisir votre choix : "))
        while choix != 1 and choix != 2 and choix != 3:
            choix = int(input("Veillez saisir votre choix (1, 2 ou 3): "))

        if choix == 1:
            pseudo1 = "Joueur 1"
            pseudo2 = "Joueur 2"
            nbj = 2
            niveau = 0
        elif choix == 2:
            pseudo1 = "Joueur 1"
            pseudo2 = "Ordi"
            nbj = 1
            print("De quel niveau sera l'ordinateur ? ")
            print(" Niveau 1 / 2 ou 3")
            niveau = int(input("Entrez le niveau de l'ordi : "))
            while niveau != 1 and niveau != 2 and niveau != 3:
                niveau = int(input("Entrez le niveau de l'ordi : "))
        else:
            nbj = 0
            pseudo1 = "Ordi 1"
            pseudo2 = "Ordi 2"
            print("De quel niveau seront les ordinateurs ? ")
            print(" Niveau 1 / 2 ou 3")
            niveau = int(input("Entrez le niveau des ordis : "))
            while niveau != 1 and niveau != 2 and niveau != 3 and niveau != 4:
                niveau = int(input("Entrez le niveau des ordis : "))

        scorej1 = 0
        scorej2 = 0

        #Execution de la première manche
        print("")
        print("C'est parti pour la première manche, le ", pseudo1," commence !")
        partie1 = manche(1, niveau, nbj)

        #Attribution des points au gagnant
        if partie1%2 == 0:
            scorej2+=1
            score_j2+=1
        else:
            scorej1+=1
            score_j1+=1

        #Execution de la deuxième manche
        print("")
        print("Au tour de la deuxième manche, le ", pseudo2," commence ! \n ")
        partie2 = manche(2, niveau, nbj)

        #Attribution des points au gagnant
        if partie2%2 != 0:
            scorej1+=1
            score_j1+=1
        else:
            scorej2+=1
            score_j2+=1

        #Vérifier quel joueur gagne la partie
        print("")
        print("        Résultat de la manche : \n ")
        if scorej1 > scorej2:
            print("Le ", pseudo1, " gagne 2 - 0 !")
        elif scorej2 > scorej1:
            print("Le ", pseudo2," gagne 2 - 0 !")
        else:
            print("Il y a égalité : tout le monde gagne 1 point !")


        print("")
        print("------------------------------------------- \n ")
        print("Voulez-vous rejouer une partie ? OUI ou NON")

        rejouer=str(input(""))
        if rejouer == "NON" or rejouer == "non":
            jouer = False

    return [score_j1,score_j2]



