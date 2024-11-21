from typing import TextIO



def regle():
    """
    Fonction règle qui a pour but d'afficher les règles
    
    Entrée : Aucun paramètre en entrée

    Sortie : Aucun paramètre en sortie
    
    """
    choix: int
    cont: bool
    choix = 0
    cont = True
    while cont == True:
        print("1 - Afficher les règles des Devinettes")
        print("2 - Afficher les règles des Allumettes")
        print("3 - Afficher les règles du Morpion")
        print("4 - Revenir au menu")
        choix = int(input("Quel choix ?"))
        while choix < 1 or choix > 4:
            choix = int(input("Quel choix ? "))

        if choix == 1:
            lien = "./Desktop/Programme/RDevinettes.txt"
            f = open(lien, "r")
            print("-----------------------------------------------------------------------------------------------------------------------------------------------")
            for i in range(17):
                print(f.readline())
            print("-----------------------------------------------------------------------------------------------------------------------------------------------\n ")
            f.close()
        elif choix == 2:
            lien = "./Desktop/Programme/RAllumettes.txt"
            f = open(lien, "r")
            print("-----------------------------------------------------------------------------------------------------------------------------------------------")
            for i in range(13):
                print(f.readline())
            print("-----------------------------------------------------------------------------------------------------------------------------------------------\n ")
            f.close()
        elif choix == 3:
            lien = "./Desktop/Programme/RMorpion.txt"
            f = open(lien, "r")
            print("-----------------------------------------------------------------------------------------------------------------------------------------------")
            for i in range(26):
                print(f.readline())
            f.close()
            print("-----------------------------------------------------------------------------------------------------------------------------------------------\n ")
        else:
            cont = False

    print(" \n ")



