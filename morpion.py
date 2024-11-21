from Bot_Morpion import niv1, niv2, niv3

def aff(case):
    """
    Fonction : affiche la grille du morpion

    Entrée : Liste de variable de type str
    Sortie : rien
    """
    
    print(" ")
    print("      1", "   2","   3")
    print("")
    print("a   ", case[0], " | ", case[1], " | ", case[2])
    print("     =============")
    print("b   ",case[3], " | ", case[4], " | ", case[5])
    print("     =============")
    print("c   ", case[6], " | ", case[7], " | ", case[8])
    print("______________________________")
    print(" ")

def morpion(TSCORE, a, ordi, niv)->list:
    """
    Fonction pour lancer une manche de morpion

    Entrée : liste de score contenant des entiers
    Sortie : liste de score contenant des entiers
    """
    
    a1 : str 
    a2 : str  
    a3 : str 
    b1 : str 
    b1 : str 
    b2 : str 
    b3 : str 
    c1 : str 
    c2 : str 
    c3 : str  
    ent : str  
    car : str
    val : int
    y : int 
    e : int  
    f : int  
    i : int
    b : bool

    #Affectation des valeurs de départ aux variables
    f = 1
    y = a
    b = True
    car = 'X'
    a1 = ' '
    a2 = ' '
    a3 = ' '
    b1 = ' '
    b2 = ' '
    b3 = ' '
    c1 = ' '
    c2 = ' '
    c3 = ' '
    case = [a1, a2, a3, b1, b2, b3, c1, c2, c3] 
    casei = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    ent = ''
    val = 0
    j = ''
    dord = ''
    branche = 0
    
    aff(case)

    while b == True:
            
            #itération permettant de changer de joueur à chaque tour
    
            val = val + 1
            if y % 2 == 0 or y == 0:
                car = 'X'
                j = '1'
            else:
                car = 'O'
                j = '2'
            

            if ordi == 0:
                if j == '1':
                    print("Joueur ", j, ": Veuillez saisir les coordonnées de votre X : ")
                    ent = str(input("")) 
            
                if j == '2':
                    print("Joueur ", j, ": Veuillez saisir les coordonnées de votre O : ")
                    ent = str(input("")) 

                #"tant que" permettant la vérification de la chaine de caractère rentrée par les joueurs
                while ent not in casei or ent == "/":
                    ent = str(input("joueur : Veillez saisir une autre valeur : "))

            if ordi == 1: 
                if j == '1':
                    print("Joueur 1, veuillez saisir les coordonnées de votre X : ")
                    ent = str(input("")) 

                    while ent not in casei or ent == "/":
                        ent = str(input("joueur : Veillez saisir une autre valeur : "))
                
                if j == '2':
                    if niv == 1:
                        ent = str(casei[niv1(case, casei)])
                    
                        while ent == "/":
                            ent = str(casei[niv1(case, casei)])

                    if niv == 2:
                        ent = str(casei[niv2(casei, case, val, car)])
                    
                        while ent == "/":
                            ent = str(casei[niv2(casei, case, val, car)])

                    if niv == 3:
                        ent = str(casei[niv3(casei, case, val, car)])

                        while ent == "/":
                            ent = str(casei[niv3(case, casei, val, car)])
            
                             
            if ordi == 2:
                if niv == 1:
                    ent = str(casei[niv1(case, casei)])
                    
                    while ent == "/":
                        ent = str(casei[niv1(case, casei)])
                    
                if niv == 2:
                        ent = str(casei[niv2(casei, case, val, car)])
                    
                        while ent == "/":
                            ent = str(casei[niv2(casei, case, val, car)])

                if niv == 3:
                    ent = str(casei[niv3(casei, case, val, car)])
                    while ent == "/":
                        ent = str(casei[niv3(case, casei, val, car)])

        
                
            #Boucle permettant de transformer une case vide en case prise pour les autres vérifications
            for i in range (len(case)):
                if casei[i] == ent:
                    case[i] = car
                    aff(case)
                    casei[i] = '/'

            y = y + 1
            
            e = 0
            f = 0 
            
            for i in range (3):

                #Verification des lignes / permet d'attribuer la victoire si conditions vérifiées
                if case[e] == case[e + 1] == case[e + 2] and case[e] != ' ': 
                    if case[e] == 'X':
                        print("Bravo ! Le Joueur 1 a gagné !")
                        TSCORE[0] = TSCORE[0] + 1
                        print("Score : ", TSCORE[0], " - ", TSCORE[1]) 
                        b = False
                        return TSCORE
                    else : 
                        print("Bravo ! Le Joueur 2 a gagné !")
                        TSCORE[1] = TSCORE[1] + 1
                        print("Score : ", TSCORE[0], " - ", TSCORE[1]) 
                        b = False
                        return TSCORE
                                
                #Vérification des colomnes / permet d'attribuer la victoire si conditions vérifiées
                if case[f] == case[f + 3] == case[f + 6] and case[f] != ' ': 
                    if case[f] == 'X':
                        print("Bravo ! Le Joueur 1 a gagné !")
                        TSCORE[0] = TSCORE[0] + 1
                        print("Score : ", TSCORE[0], " - ", TSCORE[1]) 
                        b = False
                        return TSCORE
                    else : 
                        print("Bravo ! Le Joueur 2 a gagné !")
                        TSCORE[1] = TSCORE[1] + 1
                        print("Score : ", TSCORE[0], " - ", TSCORE[1]) 
                        b = False
                        return TSCORE
                e = e + 3
                f = f + 1    
            
            #Vérification de la diagonale / permet d'attribuer la victoire si conditions vérifiées
            if case[0] == case[4] == case[8] and case[0] != ' ':
                if case[0] == 'X':
                    print("Bravo ! Le Joueur 1 a gagné !")
                    TSCORE[0] = TSCORE[0] + 1
                    print("Score : ", TSCORE[0], " - ", TSCORE[1]) 
                    b = False
                    return TSCORE
                else : 
                    print("Bravo ! Le Joueur 2 a gagné !")
                    TSCORE[1] = TSCORE[1] + 1
                    print("Score : ", TSCORE[0], " - ", TSCORE[1]) 
                    b = False
                    return TSCORE
                
            #Vérification del la diagonale (opposée) / permet d'attribuer la victoire si conditions vérifiées
            if case[2] == case[4] == case[6] and case[2] != ' ':
                if case[2] == 'X':
                    print("Bravo ! Le Joueur 1 a gagné !")
                    TSCORE[0] = TSCORE[0] + 1
                    print("Score : ", TSCORE[0], " - ", TSCORE[1]) 
                    b = False
                    return TSCORE
                else : 
                    print("Bravo ! Le Joueur 2 a gagné !")
                    TSCORE[1] = TSCORE[1] + 1
                    print("Score : ", TSCORE[0], " - ", TSCORE[1]) 
                    b = False
                    return TSCORE
             
            #Vérification d'une égalités             
            if val == 9: 
                b = False
                print("Il y a égalité, les Scores ne bougent pas.")
                print("Score : ", TSCORE[0], " - ", TSCORE[1])
                return TSCORE


#Fonction de lancement de la partie (4 manches)
def partie()->list:
    """
    Fonction de lancement d'une partie de 4 manches

    Entrée : rien
    Sortie : liste de score contenant des entiers
    """
    
    scj1 : int 
    scj2 : int 
    a : int
    boo : bool
    l : int 
            
    scj1 = 0
    scj2 = 0
    a = 0
    boo = True
 

    while boo:
        TSCORE = [0,0]
        #boucle qui lance 2 manche de morpion
        print("Quel type de jeux : ")

        print("1 - Joueur vs Joueur")
        print("2 - Joueur vs Ordi")
        print("3 - Ordi vs Ordi")
        print("")
        choix = 0
        while choix != 1 and choix != 2 and choix != 3:
            choix = int(input("Entrez 1, 2 ou 3 : "))
    
        if choix == 1:
            ordi = 0
            niv = -1
        elif choix == 2:
            ordi = 1
            print("\n")
            print("Quel niveau ? ")
            print("\n")
            print("1 - Aléatoire")
            print("2 - Intermédiaire")
            print("3 - Maitre")
            niv = -1
            while niv != 1 and niv != 2 and niv != 3:
                niv = int(input("Quel niveau souhaitez vous sélectionner : 1 - 2 - 3 : "))
        else : 
            ordi = 2
            niv = -1
            while niv != 1 and niv != 2 and niv != 3:
                niv = int(input("Quel niveau souhaitez vous sélectionner pour les ordis ? 1 - 2 - 3 : "))

        for i in range(4):
            l = morpion(TSCORE, a, ordi, niv)
            a = a + 1

        scj1 += l[0]
        scj2 += l[1]
        print("______________________________")
        print(scj1, " - ", scj2) 

    
        
        cac = str(input("Voullez vous rejouer ? o - n "))
        while cac != 'o' and cac != 'n':
            cac = str(input("Voullez vous rejouer ? o - n "))
        if cac == 'o':
            a = 0
        if cac == 'n':
            boo = False
    return l

