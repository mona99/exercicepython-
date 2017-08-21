#-*-coding:utf-8 -*-
"""This program is a speed calculator"""


def speed(distance, time):
    """This function will calulate the speed"""

    return distance/time


def display(vitesse):
    """Display is used to show the result"""

    print("vitesse=", vitesse)


def main():
    """Main script function"""

    distance = float(input("Enter the distance:  "))
    time = float(input("Enter the time: "))
    stockage = speed(distance, time)
    display(stockage)
main()
