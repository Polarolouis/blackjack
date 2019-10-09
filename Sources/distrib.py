# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:59:25 2019

@authors: Julien Morelle & Louis Lacoste
"""
def distrib(LJ,J,P):  # LJ : Liste du nom index des joueurs | J : dictionnaire avec en index les { noms index des joueurs : [Main du joueur] }
    if len(P) >= 2*len(LJ):  # verif qu'on peut jouer
        for c in range(2):
            for i in LJ:
                J[i].append(P.pop()) # On ajoute une carte dans la liste de carte du joueur i
    else:
        return 0 # La fonction return 0 s'il y a une erreur
