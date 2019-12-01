# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 13:42:21 2019

@author: LordOf20th
"""

def endphase(J,LJ):
    vmain_croupier = J[0][3]
    for i in LJ:
        infosJoueurs = J[i]
        # On récupère les valeurs
        capital = infosJoueurs[4]
        mise = infosJoueurs[0]
        main = infosJoueurs[2]
        vmain = infosJoueurs[3]

        if i == "Croupier":
            capital = 10000
        else:
            if vmain == 21 and len(main) == 2:
                print("BLACKJACK !!!")
                capital += 2.5 * mise
            elif vmain > vmain_croupier:
                capital += 2 * mise
            elif vmain == vmain_croupier:
                capital += mise

        # On vide main et mise
        main = []
        mise = 0

        # On set toutes les valeurs modifiées
        infosJoueurs[4] = capital
        infosJoueurs[0] = mise
        infosJoueurs[2] = main
        infosJoueurs[3] = vmain
