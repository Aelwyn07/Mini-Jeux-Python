from typing import TextIO

def sav(mor,all,dev):
    """
    Fonction qui récupère les Scores enregistrés à la fin de chaque partie, enregistrés depuis le menu

    Entrée : 3 listes d'entier
    Sortie : rien
    """

    mor0: int
    mor1: int
    dev0: int
    dev1: int
    all0: int
    all1: int
    i : int
    lien: str
    morpion_j1: str
    morpion_j2: str
    allumettes_j1: str
    allumettes_j2: str
    devinettes_j1: str
    devinettes_j2: str
    var : str
    f : TextIO

    mor0 = mor[0]
    mor1 = mor[1]
    all0 = all[0]
    all1 = all[1]
    dev0 = dev[0]
    dev1 = dev[1]

    #Lien utilisé pour la sauvegarde sur le fichier texte
    lien = "./Desktop/Programme/ScoreSc.txt"
    f = open(lien, "r")


    #Permet au programmes de lire les lignes ne contenant pas de score
    for i in range(4):
	    f.readline()

    #Permet de récupérer les lignes contenant les scores du morpion
    morpion_j1 = f.readline()
    morpion_j2 = f.readline()

    for i in range(4):
	    f.readline()

    #Permet de récupérer les lignes contenant les scores des devinettes
    devinettes_j1 = f.readline()
    devinettes_j2 = f.readline()

    for i in range(4):
	    f.readline()

    #Permet de récupérer les lignes contenant les scores de allumettes
    allumettes_j1 = f.readline()
    allumettes_j2 = f.readline()

    f.close()

    #Permet d'actualiser les scores en les récupérants depuis les lignes prisent avant
    morpion_j1 = actualise(morpion_j1) + mor0
    morpion_j2 = actualise(morpion_j2) + mor1
    devinettes_j1 = actualise(devinettes_j1) + dev0
    devinettes_j2 = actualise(devinettes_j2) + dev1
    allumettes_j1 = actualise(allumettes_j1) + all0
    allumettes_j2 = actualise(allumettes_j2) + all1

    #Ouverture et écriture du fichier texte
    f = open(lien,'w')

    f.write("____________________________________________")
    f.write("\n"+"")
    f.write("\n"+"*** Nombre de victoire(s) au Morpion ***")
    f.write("\n"+"")
    var = "Joueur 1 : "+str(morpion_j1)+" "
    f.write("\n"+var)
    var = "Joueur 2 : "+ str(morpion_j2)+" "
    f.write("\n"+var)
    f.write("\n"+"____________________________________________")
    f.write("\n"+"")
    f.write("\n"+"*** Nombre de victoire(s) aux Devinettes ***")
    f.write("\n"+"")
    var = "Joueur 1 : "+ str(devinettes_j1)+" "
    f.write("\n"+var)
    var = "Joueur 2 : "+ str(devinettes_j2)+" "
    f.write("\n"+var)
    f.write("\n"+"____________________________________________")
    f.write("\n"+"")
    f.write("\n"+"*** Nombre de victoire(s) aux Allumettes ***")
    f.write("\n"+"")
    var = "Joueur 1 : "+ str(allumettes_j1)+" "
    f.write("\n"+var)
    var = "Joueur 2 : "+ str(allumettes_j2)+" "
    f.write("\n"+var)
    f.write("\n"+"____________________________________________")
   

    f.close()




def actualise(chaine)->int:
    """
    Fonction qui récupère les Scores depuis les lignes de score du fichier de la dernière sauvegarde

    Entrée : Chaine de type str
    Sortie : score en type entier
    """

    val: str
    a : str
    i : int

    val = ""
    i = 0
    a = chaine[i]
    while a != ":":
        i = i + 1
        a = chaine[i]
    i = i+2
    while chaine[i] != ' ':
        val = val + str(chaine[i])
        i+=1
    return int(val)