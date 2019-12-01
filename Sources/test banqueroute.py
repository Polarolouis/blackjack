# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:32:37 2019

@author: LordOf20th
"""


def bankruptTest(LJ, J):
    for i in LJ:
        infosJoueurs = J[i]
        # On récupère les valeurs
        capital = infosJoueurs[4]
        if capital < 2:  # Si on a moins de 2 jetons alors on ne mise plus
            del J[i]  # On retire le joueur de la partie
            indexARetirer = LJ.index(i)
            del LJ[indexARetirer]  # On retire le nom du joueur de la partie


def bankruptTest2(nom, J, LJ):
    if J[nom][4] <= 2:
        # Le joueur ne peut plus jouer, il faut le retirer des listes
        del J[nom]  # On supprime ses données
        del LJ[LJ.index(nom)]  # On le retire de la liste des joueurs