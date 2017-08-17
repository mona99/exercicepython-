#-*-coding:utf-8 -*-
"""This program will calculate the speed using the time and the distance"""
def speed():
    """This function is used to calculate the speed"""
    temps = 6.892
    distance = 19.7
    return distance/temps

def display(vitesse):
    """Display  is a function used to show the result"""
    print("vitesse=", vitesse)

def main():
    """This function is used to execute the program"""
    stockage = speed()
    display(stockage)
main()
