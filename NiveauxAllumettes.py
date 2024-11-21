from random import randint
import time

# Ordi niveau 1

def niv1(nb_all: int)->int:
    """
    Fonction qui permet à l'ordinateur de jouer en utilisant le niveau 1 (du pur hasard)

    Entrée: l'entier nb_all qui représente le nombre d'allumettes encore dans la partie
    Sortie: l'entier nb qui représente le nombre d'allumettes que l'ordinateur va retirer
    """
    #c = time.time()
    nb : int
    if nb_all == 1 or nb_all == 2:
        nb = 1
    else:
        nb = randint(1,3)
    #b = time.time()
    #tmp = b-c
    #print("temps:", tmp)
    return nb

# Ordi niveau 2         

def niv2(nb_all: int)->int:
    """
    Fonction qui permet à l'ordinateur de jouer en utilisant le niveau 2 (soit du hasard, 
    soit la méthode optimale (1 chance sur 2 à chaque tour))

    Entrée: l'entier nb_all qui représente le nombre d'allumettes encore dans la partie
    Sortie: l'entier nb qui représente le nombre d'allumettes que l'ordinateur va retirer
    """
    #c = time.time()
    a : int
    nb : int
    a = randint(1,2)
    if a == 1:
        nb = niv1(nb_all)
    else : 
        nb = niv3(nb_all)

    #b = time.time()
    #tmp = b-c
    #print("temps VRAI:", tmp)
    return nb


# Ordi niveau 3

def niv3(nb_all: int)->int:   
    """
    Fonction qui permet à l'ordinateur de jouer en utilisant le niveau 3 (la stratégie optimal)

    Entrée: l'entier nb_all qui représente le nombre d'allumettes encore dans la partie
    Sortie: l'entier nb qui représente le nombre d'allumettes que l'ordinateur va retirer
    """   
    a : int
    nb : int
    #c = time.time()
    a = randint(1,10)
    if nb_all == 1 or nb_all == 2:
        nb = 1
    elif a == 1:
        nb = randint(1,3)
    else:
        if (nb_all%4) == 0:
            nb = 3
        elif (nb_all%4) == 1:
            nb = 1
        elif (nb_all%4) == 2:
            nb = 1
        elif (nb_all%4) == 3:
            nb = 2  
    #b = time.time()
    #tmp = b-c
    #print("temps:", tmp)
    return nb


