
#-*-coding:utf-8 -*-

def speed(distance,temps):
     return distance/temps
def display(vitesse):
    print("vitesse=", vitesse)

def main():
    distance = float(input("entrer la distance : "))
    temps = float(input("entrer le temps : "))
    stockage = speed(distance,temps)
    display(stockage)
main()
