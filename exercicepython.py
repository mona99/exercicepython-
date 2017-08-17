#-*-coding:utf-8 -*-
def speed():
    temps= 6.892
    distance= 19.7
    return  distance/temps 

def affiche(vitesse):
    print("vitesse=",  vitesse)

def main():
    stockage=speed()
    affiche(stockage)
main()

