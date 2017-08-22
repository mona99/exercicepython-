#-*-coding:utf-8 -*-
from math import sqrt
la_valeur = float(input("entrer la valeur: "))

if la_valeur >= 0:
   la_racine = sqrt(la_valeur)
   print("la racine est de {:.2f} est {:.3f}" .format(la_valeur, la_racine))
else:
   print("non")

