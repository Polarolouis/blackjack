# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:59:25 2019

@authors: Julien Morelle & Louis Lacoste
"""

def initialisation(n): # Création de la liste des joueurs, et le dictionnaire de leurs caractéristiques
    LJ=[]
    for i in range(n+1):
        if i == 0:
            LJ.append("Croupier")
        else:
            LJ.append("Joueur "+str(i))
    J = {}
    for i in LJ:
        J[i] = []
    return LJ,J