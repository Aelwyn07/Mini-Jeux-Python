from allumette import allumette
from devinettes import devinettes
from morpion import partie
from SauvegardeText import sav
from affichage_score import afficher
from regles import regle

if __name__ == "__main__":
    ENT: int
    a: bool
    dev: list
    mor: list
    all: list
    score1: list
    score2: list
    score3: list
    lst_temp: list

    ENT = 0
    a = True
    dev = [0,0]
    mor = [0,0]
    all = [0,0]
    

    print("---------------------------------")
    print("           BIENVENUE !           ")
    print("---------------------------------")

    #Boucle tant que qui fait fonctionner le programme
    while a == True:
        print("")
        print("            Menu           ")
        print("")
        print("Que souhaitez vous faire : ")
        print(" 1 - Jouer au jeu des devinettes")
        print(" 2 - Jouer au jeu des allumettes")
        print(" 3 - Jouer au jeu du morpion")
        print(" 4 - Afficher les scores")
        print(" 5 - Règles des jeux")
        print(" 6 - Quitter le programme")
        print("                                ")
        
        #Saisie du choix
        ENT = int(input("Veuillez saisir votre choix : "))
        while ENT < 1 or ENT > 6:
            print("Veillez saisir un nombre valide ! (entre 1 et 6)")
            ENT = int(input(""))

        #Conditions pour lancer la fonction souhaitée

        if ENT == 1:
            print(" \n-----------------------------------------------------")
            print("             Vous jouez aux devinettes !             ")
            print("-----------------------------------------------------\n ")

            #Lancement d'une partie et actualisation des scores
            score1 = devinettes()
            dev[0]+=score1[0]
            dev[1]+=score1[1]

        if ENT == 2:
            print(" \n-----------------------------------------------------------")
            print("                Vous jouez aux allumettes !                ")
            print("-----------------------------------------------------------\n ")

            #Lancement d'une partie et actualisation des scores
            score2 = allumette()
            all[0]+=score2[0]
            all[1]+=score2[1]

        if ENT == 3:
            print(" \n---------------------------------------------------------")
            print("                 Vous jouez au Morpion !                 ")
            print("---------------------------------------------------------\n ")

            #Lancement d'une partie et actualisation des scores
            score3 = partie()
            mor[0]+=score3[0]
            mor[1]+=score3[1]

        if ENT == 4:
            afficher()

        if ENT == 5:
            regle()

        if ENT == 6:
            print("Au revoir !")

            #Envoie des scores pour les sauvegarder
            sav(mor,all,dev)

            a = False



