# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:51:39 2019

@author: LordOf20th
"""

def stratAlea(phase, infosJoueurs, P):
    # On récupère les valeurs
    capital = infosJoueurs[4]
    mise = infosJoueurs[0]
    main = infosJoueurs[2]

    if phase == 1:  # Mise de départ
        mise = randint(2, capital)
        capital -= mise
    elif phase == 2:
        if capital >= mise:
            choix = randint(1, 3)
                if choix == 1:  # Double
                    main.append(tirerUneCarte(P)) # On ajoute une carte à la main
                    capital -= mise
                    mise = 2*mise
                elif choix == 2: # Hit
                    rejouer = True
                    while valeurMain(main) < 21 and rejouer:
                        if randint(1, 2) == 1:
                            rejouer = True
                        main.append(tirerUneCarte(P)) # On ajoute une carte à la main

        else: # On ne peut pas doubler
            choix = randint(2, 3)
            if choix == 2: # Hit
                    rejouer = True
                    while valeurMain(main) < 21 and rejouer:
                        if randint(1, 2) == 1:
                            rejouer = True
                        main.append(tirerUneCarte(P)) # On ajoute une carte à la main

    # On attribue les nouvelles valeurs
    infosJoueurs[2] = main
    infosJoueurs[0] = mise
    infosJoueurs[4] = capital
