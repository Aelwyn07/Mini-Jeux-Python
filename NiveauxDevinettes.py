from random import randint
import time


# Ordi niveau 1

def niv1(nbmin: int, nbmax: int)->int:
    """
    Fonction qui permet à l'ordinateur de jouer en utilisant le niveau 1 (du pur hasard)

    Entrée:" les entiers nbmin et nbmax qui représentent l'échelle entourant le nombre mystère à deviner
    Sortie: l'entier proposition qui représente le nombre que va proposer l'ordinateur
    """
    proposition : int
    #c = time.time()
    if nbmax - nbmin == 1:
        proposition = nbmin + 1
    else:
        proposition = randint(nbmin+1, nbmax-1)
    #b = time.time()
    #tmp = b-c
    #print("temps:", tmp)
    return proposition

#Ordi niveau 2

def niv2(nbmin: int, nbmax: int)->int:
    """
    Fonction qui permet à l'ordinateur de jouer en utilisant le niveau 2 (soit du hasard, soit la stratégie optimale (une chance sur deux à chaque tour))

    Entrée: les entiers nbmin et nbmax qui représentent l'échelle entourant le nombre mystère à deviner
    Sortie: l'entier proposition qui représente le nombre que va proposer l'ordinateur
    """
    proposition : int
    a : int
    nbmil : int 
    x : int
    #c = time.time()
    if nbmax - nbmin == 1:
        proposition = nbmin + 1
    else:
        a = randint(1,5)
        if a == 1:
            proposition = randint(nbmin+1, nbmax-1)
        elif (a == 2 or a == 3) and nbmin>3 and nbmax<97:
            nbmil = nbmax-nbmin
            nbmil = nbmil//2
            x = randint(-3,3)
            proposition = nbmin + nbmil + x
        else:
            nbmil = nbmax-nbmin
            nbmil = nbmil//2
            proposition = nbmin + nbmil
    #b = time.time()
    #tmp = b-c
    #print("temps:", tmp)
    return proposition

# Ordi niveau 3

def niv3(nbmin: int, nbmax: int)->int:
    """
    Fonction qui permet à l'ordinateur de jouer en utilisant le niveau 3 (la méthode optimale)

    Entrée: les entiers nbmin et nbmax qui représentent l'échelle entourant le nombre mystère à deviner
    Sortie: l'entier proposition qui représente le nombre que va proposer l'ordinateur
    """
    #c = time.time()
    proposition : int
    a : int
    nbmil: int
    if nbmax - nbmin == 1:
        proposition = nbmin + 1
    else:
        a = randint(1,13)
        if a != 13:
            nbmil = nbmax-nbmin
            nbmil = nbmil//2
            proposition = nbmin + nbmil
        else: 
            proposition = randint(nbmin+1,nbmax-1)
    #b = time.time()
    #tmp = b-c
    #print("temps:", tmp)
    return proposition