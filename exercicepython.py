
#-*-coding:utf-8 -*-

def speed(distance,temps):
     return distance/temps
distance = float(input("entrer la distance : "))
temps = float(input("entrer le temps : "))
def display(vitesse):
    """Display  is a function used to show the result"""
    print("vitesse=", vitesse)

def main():
    """This function is used to execute the program"""
    stockage = speed(distance,temps)
    display(stockage)
main()
