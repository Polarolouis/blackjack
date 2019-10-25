# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:59:25 2019

@authors: Julien Morelle & Louis Lacoste
"""
from random import randint

def stratAlea(phase, mise):
    # avec phase qui correspond à la phase de jeu
    """ mise entre 2 et 100 euros aléatoirement
    Soit il tire | soit il double
    Si il tire, il a une chance sur deux d'arrêter de tirer """
    if phase == 1:  # Mise de départ
        return (randint(2, 100), 0)  # La fonction renvoie (la mise, le nombre de cartes en plus)
    elif phase == 2:  # Doubler ou hit (peut re hit ou stand) ou stand
        choix = randint(1, 3)
        if choix == 1:  # Double
            return (mise, 1)
        elif choix == 2:  # Hit
            nbreCartes = 1
            while randint(1, 2) == 1:
                nbreCartes += 1
            return (0, nbreCartes)
        elif choix == 3:  # Stand
            return (0, 0)