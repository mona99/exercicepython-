#-*-coding:utf-8 -*-
""" this program is a speed calculator"""
def speed(distance, temps):
    """ This function will calulate the speed"""
    return distance/temps
def display(vitesse):
    """ Display is used to show the result"""

    print("vitesse=", vitesse)
def main():
    """local function"""
    distance = float(input("entrer la distance : "))
    temps = float(input("entrer le temps : "))
    stockage = speed(distance, temps)
    display(stockage)
main()
