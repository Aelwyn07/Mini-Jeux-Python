from typing import TextIO

def afficher():
    lien = "./Desktop/Programme/ScoreSc.txt"
    f = open(lien, "r")
    for i in range(19):
        print(f.readline()) 
    f.close