#Fichier Bot Morpion
from random import randint
import time


def niv1(case, casei):
    """
    Fonction de l'ordinateur de niveau 1 : Aléatoire

    Entrée : tableau d'indice "casei"
    Sortie : coordonnées de l'emplacement où jouer "coord"
    """

    #c = time.time()

    i : int
    coord : int

    casebot = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] 

    for i in range(0, 9):
        casebot[i] = casei[i]
    
    coord = randint(0, len(casebot) - 1)
    
    while casebot[coord] == '/':
        coord = randint(0, len(casei) - 1)

    #b = time.time()
    #tmp = b - c
    #print("temps : ", tmp)

    return coord

def niv2(casei, case, val, car):
    """
    Fonction de l'ordinateur de niveau 2

    Entrée : tableau d'indice "casei", tableau de variables "case", variable de tour "val" et variable contenant "O" ou "X"
    Sortie : coordonnées de l'emplacement où jouer "coord"
    """

    #c = time.time()

    random : int
    coord : int

    random = randint(0, 1)

    if random == 0:
        coord = niv1(case, casei)
    else : 
        coord = niv3(casei, case, val, car)
    
    #b = time.time()
    #tmp = b - c
    #print("temps : ", tmp)
    
    return coord

def niv3(casei, case, val, car):
    """
    Fonction de l'ordinateur de niveau 3

    Entrée : tableau d'indice "casei", tableau de variables "case", variable de tour "val" et variable contenant "O" ou "X"
    Sortie : coordonnées de l'emplacement où jouer "coord"
    """
    #c = time.time()
    
    branche : int
    coord : int
    boo1 : bool
    bool : bool
    val : int
    x : int
    z : int
    y : int
    i : int
    e : int
    o : int
    car : str

    casebot = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    branche = 1
    coord = 9
    boo1 = True

    for i in range(0, 9):
        casebot[i] = casei[i]

    #STRATEGIE 
    
    #TOUR 1 :
    if val == 2:
        #Branche 1 
        #Debut coin
        if casebot[0] == '/' or casebot[2] == '/' or casebot[6] == '/' or casebot[8] == '/':
            coord = 4
            branche = 1
            boo1 = False
        
        #Branche 2
        #Debut côté
        if casebot[1] == '/':
            coord = 7
            branche = 2
            boo1 = False
        
        if casebot[3] == '/':
            coord = 5
            branche = 2
            boo1 = False
        
        if casebot[5] == '/': 
            coord = 3
            branche = 2
            boo1 = False
        
        if casebot[7] == '/':
            coord = 1
            branche = 2
            boo1 = False

        #Branche 3
        #Debut milieu 
        if casebot[4] == '/':
            coord = 3
            branche = 3
            boo1 = False
    
    #TOUR 2
    if val == 4:
        #Branche 1
        if branche == 1:
            #Verification coin
            #C1
            for i in range(4):
                if i == 0:
                    x = 6
                    z = 0
                    y = 4
                elif i == 1:
                    x = 6
                    z = 8
                elif i == 2:
                    x = 8
                    z = 2
                elif i == 3:
                    x = 2
                    z = 0

                if case[x] == 'X' and case[z] == 'X' and case[y] == 'O':
                    branche = 2
                    boo1 = False
                    if i == 0:
                        coord = 3
                    elif i == 1:
                        coord = 7
                    elif i == 2:
                        coord = 5
                    elif i == 3:
                        coord = 1
            
            #C2
            for i in range(4):
                if i == 0:
                    x = 6
                    z = 2
                    y = 4
                elif i == 1:
                    x = 8
                    z = 0
                elif i == 2:
                    x = 6
                    z = 2
                elif i == 3:
                    x = 8
                    z = 0

                if case[x] == 'X' and case[z] == 'X' and case[y] == 'O':
                    branche = 2
                    boo1 = False
                    if i == 0:
                        coord = 3
                    elif i == 1:
                        coord = 7
                    elif i == 2:
                        coord = 3
                    elif i == 3:
                        coord = 7

            #C3
            for i in range(4):
                if i == 0:
                    x = 6
                    z = 8
                    y = 4
                elif i == 1:
                    x = 8
                    z = 2
                elif i == 2:
                    x = 0
                    z = 2
                elif i == 3:
                    x = 6
                    z = 0

                if case[x] == 'X' and case[z] == 'X' and case[y] == 'O':
                    branche = 2
                    boo1 = False
                    if i == 0:
                        coord = 3
                    elif i == 1:
                        coord = 7
                    elif i == 2:
                        coord = 5
                    elif i == 3:
                        coord = 1
                
            #Verification des ccôtés
            #Co1
            for i in range(4):
                if i == 0:
                    x = 6
                    z = 1
                    y = 4
                elif i == 1:
                    x = 8
                    z = 3
                elif i == 2:
                    x = 2
                    z = 5
                elif i == 3:
                    x = 0
                    z = 7

                if case[x] == 'X' and case[z] == 'X' and case[y] == 'O':
                    branche = 2
                    boo1 = False
                    if i == 0:
                        coord = 3
                    elif i == 1:
                        coord = 7
                    elif i == 2:
                        coord = 5
                    elif i == 3:
                        coord = 1
            
            #C2
            for i in range(4):
                if i == 0:
                    x = 6
                    z = 5
                    y = 4
                elif i == 1:
                    x = 8
                    z = 1
                elif i == 2:
                    x = 2
                    z = 3
                elif i == 3:
                    x = 0
                    z = 7

                if case[x] == 'X' and case[z] == 'X' and case[y] == 'O':
                    branche = 2
                    boo1 = False
                    if i == 0:
                        coord = 7
                    elif i == 1:
                        coord = 5
                    elif i == 2:
                        coord = 1
                    elif i == 3:
                        coord = 3
            
        #Branche 2
        if branche == 1:
            #Verification coin
            #C1
            for i in range(4):
                if i == 0:
                    x = 0
                    z = 1
                    y = 7
                elif i == 1:
                    x = 6
                    z = 3
                    y = 5
                elif i == 2:
                    x = 8
                    z = 7
                    y = 1
                elif i == 3:
                    x = 2
                    z = 5
                    y = 3

                if case[x] == 'X' and case[z] == 'X' and case[y] == 'O':
                    branche = 2
                    boo1 = False
                    if i == 0:
                        coord = 2
                    elif i == 1:
                        coord = 0
                    elif i == 2:
                        coord = 6
                    elif i == 3:
                        coord = 8
            
            #C2
            for i in range(4):
                if i == 0:
                    x = 2
                    z = 1
                    y = 7
                elif i == 1:
                    x = 0
                    z = 3
                    y = 5
                elif i == 2:
                    x = 6
                    z = 7
                    y = 1
                elif i == 3:
                    x = 8
                    z = 5
                    y = 3

                if case[x] == 'X' and case[z] == 'X' and case[y] == 'O':
                    branche = 2
                    boo1 = False
                    if i == 0:
                        coord = 0
                    elif i == 1:
                        coord = 6
                    elif i == 2:
                        coord = 8
                    elif i == 3:
                        coord = 2

            #C3
            for i in range(4):
                if i == 0:
                    x = 6
                    z = 1
                    y = 7
                elif i == 1:
                    x = 8
                    z = 3
                    y = 5
                elif i == 2:
                    x = 2
                    z = 7
                    y = 1
                elif i == 3:
                    x = 0
                    z = 5
                    y = 3

                if case[x] == 'X' and case[z] == 'X' and case[y] == 'O':
                    branche = 2
                    boo1 = False
                    if i == 0:
                        coord = 3
                    elif i == 1:
                        coord = 7
                    elif i == 2:
                        coord = 5
                    elif i == 3:
                        coord = 1
                
            #C4
            for i in range(4):
                if i == 0:
                    x = 8
                    z = 1
                    y = 7
                elif i == 1:
                    x = 2
                    z = 3
                    y = 5
                elif i == 2:
                    x = 0
                    z = 7
                    y = 1
                elif i == 3:
                    x = 6
                    z = 5
                    y = 3

                if case[x] == 'X' and case[z] == 'X' and case[y] == 'O':
                    branche = 2
                    boo1 = False
                    if i == 0:
                        coord = 5
                    elif i == 1:
                        coord = 1
                    elif i == 2:
                        coord = 3
                    elif i == 3:
                        coord = 7
                
                #Verification milieu X
            if case[x] == 'X' and case[z] == 'X' and case[y] == 'O':
                coord = 8
                branche = 2
                boo1 = False
                
            #Verification des deux côté
            #Co1
            for i in range(4):
                if i == 0:
                    x = 3
                    z = 7
                    y = 1
                elif i == 1:
                    x = 7
                    z = 5
                    y = 3
                elif i == 2:
                    x = 5
                    z = 1
                    y = 7
                elif i == 3:
                    x = 1
                    z = 3
                    y = 5

                if case[x] == 'X' and case[z] == 'X' and case[y] == 'O':
                    branche = 2
                    boo1 = False
                    if i == 0:
                        coord = 6
                    elif i == 1:
                        coord = 8
                    elif i == 2:
                        coord = 2
                    elif i == 3:
                        coord = 0
            
            #Co2
            for i in range(4):
                if i == 0:
                    x = 5
                    z = 1
                    y = 7
                elif i == 1:
                    x = 1
                    z = 3
                    y = 5
                elif i == 2:
                    x = 3
                    z = 7
                    y = 1
                elif i == 3:
                    x = 7
                    z = 5
                    y = 3

                if case[x] == 'X' and case[z] == 'X' and case[y] == 'O':
                    branche = 2
                    boo1 = False
                    if i == 0:
                        coord = 4
                    elif i == 1:
                        coord = 4
                    elif i == 2:
                        coord = 4
                    elif i == 3:
                        coord = 4
        
        #Branche 3 
        if branche == 1:
            #Verification côté
            if case[1] == 'X' and case[3] == 'O' and case[4] == 'X':
                coord = 7
                boo1 = False
                branche = 3
            
            if case[5] == 'X' and case[3] == 'O' and case[4] == 'X':
                coord = 0
                boo1 = False
                branche = 3
            
            if case[7] == 'X' and case[3] == 'O' and case[4] == 'X':
                coord = 1
                boo1 = False
                branche = 3
        
            #Verification coin
            if case[0] == 'X' and case[3] == 'O' and case[4] == 'X':
                coord = 6
                boo1 = False
                branche = 3
            
            if case[6] == 'X' and case[3] == 'O' and case[4] == 'X':
                coord = 0
                boo1 = False
                branche = 3
            
            if case[8] == 'X' and case[3] == 'O' and case[4] == 'X':
                coord = 7
                boo1 = False
                branche = 3
            
            if case[2] == 'X' and case[3] == 'O' and case[4] == 'X':
                coord = 6
                boo1 = False
                branche = 3

    
    bool = False
    #VERIFICATION EN LIGNE :
    e = 0
    for i in range(3):
        if (case[e] == 'X' or case[e] == 'O') and case[e] == case[e + 1] and case[e + 2] == ' ' and bool == False:
            coord = e + 2
            boo1 = False
            if car == case[e + 1]:
                bool = True
        else : 
            e = e + 3
    
    e = 2
    for i in range(3):
        if (case[e] == 'X' or case[e] == 'O') and case[e] == case[e - 1] and case[e - 2] == ' '  and bool == False:
            coord = e - 2
            boo1 = False
            if car == case[e - 1]:
                bool = True
        else :
            e = e + 3
    
    e = 0
    for i in range(3):
        if (case[e] == 'X' or case[e] == 'O') and case[e] == case[e + 2] and case[e + 1] == ' ' and bool == False:
            coord = e + 1
            boo1 = False
            if car == case[e + 2]:
                bool = True
        else :
            e = e + 3

    #VERIFACATION EN COLOMNE
    e = 0
    for i in range(3):
        if (case[e] == 'X' or case[e] == 'O') and case[e] == case[e + 3] and case[e + 6] == ' ' and bool == False:
            coord = e + 6
            boo1 = False
            if car == case[e + 3]:
                bool = True
        else : 
            e = e + 1
    
    e = 6
    for i in range(3):
        
        if (case[e] == 'X' or case[e] == 'O') and case[e] == case[e - 3] and case[e - 6] == ' ' and bool == False:
            coord = e - 6
            boo1 = False
            if car == case[e - 3]:
                bool = True
        else : 
            e = e + 1

    e = 0
    for i in range(3):
        if (case[e] == 'X' or case[e] == 'O') and case[e] == case[e + 6] and case[e + 3] == ' ' and bool == False:
            coord = e + 3
            boo1 = False
            if car == case[e + 6]:
                bool = True
        else : 
            e = e + 1

    
    #VERIFICATION EN DIAGONALE 1
    for i in range(1):
        e = 2
        if (case[e] == 'X' or case[e] == 'O') and case[e] == case[e + 2] and case[e + 4] == ' ' and bool == False:
            coord = e + 4
            boo1 = False
            if car == case[e + 2]:
                bool = True

    
    for i in range(1):
        e = 6
        if (case[e] == 'X' or case[e] == 'O') and case[e] == case[e - 2] and case[e - 4] == ' ' and bool == False:
            coord = e - 4
            boo1 = False
            if car == case[e - 2]:
                bool = True
    
    for i in range(1):
        e = 6
        if (case[e] == 'X' or case[e] == 'O') and case[e - 2] == ' ' and case[e - 4] == case[e] and bool == False:
            coord = e - 2
            boo1 = False
            if car == case[e - 2]:
                bool = True
    
    #VERIFICATION EN DIAGONALE 2
    for i in range(1):
        e = 0
        if (case[e] == 'X' or case[e] == 'O') and case[e] == case[e + 4] and case[e + 8] == ' ' and bool == False:
            coord = e + 8
            boo1 = False
            if car == case[e + 4]:
                bool = True
    
    for i in range(1):
        e = 8
        if (case[e] == 'X' or case[e] == 'O') and case[e] == case[e - 4] and case[e - 8] == ' ' and bool == False:
            coord = e - 8
            boo1 = False
            if car == case[e - 4]:
                bool = True
                

    for i in range(1):
        e = 8
        if (case[e] == 'X' or case[e] == 'O') and case[e - 4] == ' ' and case[e - 8] == case[e] and bool == False:
            coord = e - 4
            boo1 = False
            if car == case[e - 4]:
                bool = True
    
    #______________________________________________________________________________________________________________________________________#
    
    #Verif si non victoire ou bloquage avant
    #Ligne
    o = 0
    for i in range(3):
        if case[o] == car and case[o + 1] == ' ' and case[o + 2] == ' ' and boo1 == True:
            coord = o + 1
            boo1 = False
        else :
            o = o + 3
    
    o = 2
    for i in range(3):
        if case[o] == car and case[o - 1] == ' ' and case[o - 2] == ' ' and boo1 == True:
            coord = o - 1
            boo1 = False
        else :
            o = o + 3
    
    o = 0
    for i in range(3):
        if case[o] == ' ' and case[o + 1] == car and case[o + 2] == ' ' and boo1 == True:
            coord = o + 2
            boo1 = False
        else :
            o = o + 3

    #Colomne
    o = 0
    for i in range(3):
        if case[o] == [car] and case[o + 3] == ' ' and case[o + 6] == ' ' and boo1 == True:
            coord = o + 3
            boo1 = False
        else :
            o = o + 1
    
    o = 6
    for i in range(3):
        if case[o] == [car] and case[o - 3] == ' ' and case[o - 6] == ' ' and boo1 == True:
            coord = o + 3
            boo1 = False
        else :
            o = o + 1
    
    o = 6
    for i in range(3):
        if case[o] == [car] and case[o - 3] == ' ' and case[o - 6] == ' ' and boo1 == True:
            coord = o + 3
            boo1 = False
        else :
            o = o + 1

    #Diagonale 1 
    if case[0] == [car] and case[4] == ' ' and case[8] == ' ' and boo1 == True:
        coord = 4
        boo1 = False

    if case[8] == [car] and case[4] == ' ' and case[0] == ' ' and boo1 == True:
        coord = 4
        boo1 = False
    
    if case[4] == [car] and case[0] == ' ' and case[8] == ' ' and boo1 == True:
        coord = 0
        boo1 = False
    
    #Diagonale 2
    if case[2] == [car] and case[4] == ' ' and case[6] == ' ' and boo1 == True:
        coord = 4
        boo1 = False
    
    if case[6] == [car] and case[4] == ' ' and case[2] == ' ' and boo1 == True:
        coord = 4
        boo1 = False
    
    if case[4] == [car] and case[2] == ' ' and case[6] == ' ' and boo1 == True:
        coord = 2
        boo1 = False

    if coord == 9:
        coord = niv1(case, casei)

    #b = time.time()
    #tmp = b - c
    #print("temps : ", tmp)

    return coord