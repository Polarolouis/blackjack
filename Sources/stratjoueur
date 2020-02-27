#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:14:27 2020

@author: lordof20th
"""

def stratJoueur(phase, infosJoueurs, P, valUpCard):
    # avec phase qui correspond à la phase de jeu
    # On récupère les valeurs
    capital = infosJoueurs[4]
    mise = infosJoueurs[0]
    main = infosJoueurs[2]

    if phase == 1:  # Mise de départ
        miseEnCours = True
        while miseEnCours:    
            mise = input("Veuillez saisir votre mise entre 1 et " + str(capital) + " jetons : ")
            try:
                mise = int(mise)
            except:
                print("Mise non entière ! ")
            if (type(mise) is int) and (mise >= 1 and mise <= capital):
                miseEnCours = False
            else:
                print("Saisie incorrecte ! Veuillez recommencer")
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
    infosJoueurs[3] = valeurMain(main)