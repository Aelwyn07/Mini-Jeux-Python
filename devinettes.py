from NiveauxDevinettes import niv1, niv2, niv3
from random import randint
import time

def demande_joueur()->int:
    """
    Fonction pour demander un nombre au joueur

    Entrée: la fonction n'a besoin d'aucun paramètre en entrée
    Sortie: un entier
    """
    nombre : int
    nombre = int(input("Quel nombre ? "))

    #Condition pour saisir un nombre entre 1 et 100 compris
    while nombre < 1 or nombre > 100:
        nombre = int(input("Saisir un nombre entre 1 et 100 compris : "))
    return nombre

def demande_ordis(n: int,nbmin: int, nbmax: int)->int:
    """
    Fonction qui permet de jouer à l'ordinateur selon le niveau choisi avant la partie

    Entrée: .l'entier n : représente le niveau de l'ordinateur
            .les entiers nbmin et nbmax qui définissent la fourchette entourant le nombre à trouver
    Sortie: un entier
    """
    nb : int
    if n == 1:
        nb = niv1(nbmin, nbmax)
    elif n == 2:
        nb = niv2(nbmin, nbmax)
    else:
        nb = niv3(nbmin, nbmax)
    return nb

def indice()->str:
    """
    Fonction qui permet au joueur d'indiquer la position de son nombre

    Entrée: La fonction n'a besoin d'aucun paramètre en entrée
    Sortie: une chaine
    """
    i : int
    print("1 - Trop petit")
    print("2 - Trop grand")
    print("3 - C'est gagné !")

    #Saisie du joueur qui permet de savoir si le nombre a été trouvé ou pas
    i = int(input("Alors, gagné ou pas ?"))
    while i != 1 and i != 2 and i != 3:
        i = int(input("Entrez 1, 2 ou 3"))
    return i

def indice_bot(nb_choisi: int, nb_mystere: int)->int:
    """
    Fonction qui permet à l'ordinateur de localiser son nombre par rapport à la proposition du joueur

    Entrée: .l'entier nb_choisi qui représente le nombre que propose le joueur
            .l'entier nb_mystere qui est le nombre que le joueur doit deviner
    """
    if nb_choisi < nb_mystere:
        return 1
    elif nb_choisi > nb_mystere:
        return 2
    else:
        return 3



def manche(pseudo: str, nbj: int, niveau: int)->int:
    """
    Fonction qui permet de jouer une manche

    Entrée : la fonction n'a besoin d'aucun paramètre en entrée
    Sortie : l'entier proposition qui renvoie le nombre d'essai(s) du joueur qui devine le nombre
    """
    nombre_mystere : int
    nombre_choisi : int
    proposition : int
    trouve : bool
    test : int
    nb_min: int
    nb_max: int

    #Saisie du nombre à faire deviner et ajout d'espaces pour ne pas le voir à l'écran
    if pseudo == "Joueur 1" or pseudo == "Joueur 2":
        nombre_mystere = int(input("Nombre à faire deviner : "))
        while nombre_mystere < 1 or nombre_mystere > 100:
            nombre_mystere = int(input("Entrez un nombre entre 1 et 100 compris : "))
    else:
        nombre_mystere = randint(1, 100)
    for i in range(100):
        print("       ")

    nb_min = 0
    nb_max = 101
    
    print("")
    if nbj == 2 or (nbj == 1 and pseudo != "Joueur 1"):
        print("Veuillez maintenant saisir une proposition ! ")
        nombre_choisi = demande_joueur()
    else:
        nombre_choisi = demande_ordis(niveau, nb_min, nb_max)
        
    proposition = 1
    trouve = False

    #Condition pour jouer une manche 
    while trouve != True:

        print("")
        print("Le joueur a proposé le nombre ", nombre_choisi)
        print("")

        print("Est-il égal au nombre mystère ?")
        print("")
        if pseudo == "Joueur 1" or pseudo == "Joueur 2":
            test = indice() 
        else:
            test = indice_bot(nombre_choisi, nombre_mystere)
        

    
        #Si la réponse est 'OUI', on affiche et retourne les résultats
        if test == 3:
            print("")
            print("        C'est gagné !")
            print("")
            trouve = True
            if proposition > 1:
                print("_____________________________________________________________")
                print("")
                print("Vous avez trouvé le nombre en seulement ", proposition, "propositions")
                print("_____________________________________________________________")
                print("")
            else:
                print("_____________________________________________________________")
                print("")
                print("Vous avez trouvé le nombre en seulement ", proposition, "proposition !!")
                print("_____________________________________________________________")
                print("")

            return proposition
        else:

            #Vérification que le joueur ne mente pas sur la valeur de son nombre et actualisation des extrémitées
            if test == 1 and nombre_choisi < nombre_mystere:
                    print("")
                    print("        Trop petit")
                    print("")
                    if nombre_choisi > nb_min:
                        nb_min = nombre_choisi

            elif test == 2 and nombre_choisi > nombre_mystere:
                    print("")
                    print("        trop grand")
                    print("")
                    if nombre_choisi < nb_max:
                        nb_max = nombre_choisi

            else:
                print("")
                print("Le joueur a menti sur son nombre !!")
                trouve = True
                proposition = 0
                print("Il perd donc la manche !")
                print("")
                return proposition




            #Actualisation du nombre d'essais pour deviner le nombre
            proposition = proposition + 1

        if nb_min+1 == nb_max-1 :
            print("Une dernière proposition ? Le nombre est sûrement ", nb_min+1, " ! ")
        elif nb_min+2 == nb_max-1 :
            print("Veuillez saisir une autre proposition ! Le nombe est ", nb_min+1, " ou ", nb_max-1, " ! ")
        else :
            print("Veuillez saisir une autre proposition ! De préférence entre ", nb_min+1, " et ", nb_max-1, " !")
 
        if nbj == 2 or (nbj == 1 and pseudo != "Joueur 1"):
            print("Veuillez maintenant saisir une proposition ! ")
            nombre_choisi = demande_joueur()
        else:
            nombre_choisi = demande_ordis(niveau, nb_min, nb_max)



def devinettes()->int:
    """
    Fonction qui permet de lancer une partie

    Entrée: Aucun paramètre d'entrée

    Sortie: des entiers sous formes de liste
    """
    jouer : bool 
    rejouer : bool
    resultJ1 : int 
    resultJ2 : int 
    score_j1 : int 
    score_j2 : int
    choix : int
    pseudo1: str
    pseudo2: str
    niveau : int
    nbj: int
    choix = 0
    score_j1 = 0
    score_j2 = 0
    jouer = True
  
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
            print(" Niveau 1 / 2 / 3")
            niveau = int(input("Entrez le niveau de l'ordi : "))
            while niveau != 1 and niveau != 2 and niveau != 3:
                niveau = int(input("Entrez le niveau de l'ordi : "))
        else:
            pseudo1 = "Ordi 1"
            pseudo2 = "Ordi 2"
            nbj = 0
            print("De quel niveau seront les ordinateurs ? ")
            print(" Niveau 1 / 2 / 3")
            niveau = int(input("Entrez le niveau des ordis : "))
            while niveau != 1 and niveau != 2 and niveau != 3:
                niveau = int(input("Entrez le niveau des ordis : "))
            

        #Permet de jouer la première manche
        print("Première manche, le ",pseudo1, " commence ! \n ")
        print(pseudo1, " Veuillez saisir le nombre à faire deviner ! \n ")
        resultJ2 = manche(pseudo1, nbj, niveau)

        #permet de jouer la deuxième manche
        print("")
        print("Deuxième manche, c'est au ", pseudo2, " de faire deviner un nombre ! \n ")
        print(pseudo2, " , Veuillez saisir le nombre à faire deviner ! \n ")
        resultJ1 = manche(pseudo2, nbj, niveau)


        #Conditions permettant le calcul et l'affichage des résultats
        print("Résultat de la manche: ")
        if resultJ1 > resultJ2:
            print(pseudo2, " gagne : ", resultJ1, " propositions pour le Joueur 1 contre seulement ", resultJ2, " propositions pour le Joueur 2 !")
            score_j2+= 1
        elif resultJ2 > resultJ1:
            print(pseudo1, "gagne : ", resultJ1, " propositions seulement pour le Joueur 1 contre ", resultJ2, " propositions pour le Joueur 2 !")
            score_j1+= 1
        else:
            print("Il y a égalité : tout le monde gagne 1 point")
            score_j1+= 1
            score_j2+= 1


        #Saisie pour rejouer ou non une partie
        print("")
        print("Voulez-vous rejouer une partie ? OUI ou NON")
        rejouer=str(input(""))

        #Vérification de la saisie
        while rejouer != "oui" and rejouer != "OUI" and rejouer != "non" and rejouer != "NON":
            rejouer=str(input(" OUI ou NON s'il vous plaît !"))

        #Condition pour arrêter le jeu si c'est demandé
        if rejouer == "NON" or rejouer == "non":
            jouer = False

    return [score_j1, score_j2]





