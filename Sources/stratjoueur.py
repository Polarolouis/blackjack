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
        print("Votre capital est de : " + str(capital))
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
        capital -= mise
    elif phase == 2:
        if capital >= mise: # On peut Hit Stand et Double
            choixEnCours = True
            while choixEnCours:
                choix = input("Souhaitez-vous : \n 1)Double (Doubler la mise et tirer une carte puis passer à la révélation) \n 2)Hit (Tirer une carte supplémentaire) \n 3)Stand (ne pas tirer de cartes ni augmenter la mise et passer à la révélation) \n Entrer le numéro de votre choix : ")
                try:
                    choix = int(choix)
                except:
                    print("Choix non entier ! ")
                if (type(choix) is int) and (choix >= 1 and choix <= 3):
                    choixEnCours = False
                else:
                    print("Saisie incorrecte ! Veuillez recommencer")
            if choix == 1:  # Double
                main.append(tirerUneCarte(P)) # On ajoute une carte à la main
                capital -= mise
                mise = 2*mise
            elif choix == 2: # Hit
                afficheJeu()
                rejouer = True
                choix2EnCours = True
                while valeurMain(main) <= 21 and rejouer:
                    afficheJeu()
                    while choix2EnCours:
                        choix2 = input("Souhaitez-vous : \n 1)Hit (Tirer une carte supplémentaire) \n 2)Stand (ne pas tirer de cartes ni augmenter la mise et passer à la révélation) \n Entrer le numéro de votre choix : ")
                        try:
                            choix2 = int(choix)
                        except:
                            print("Choix non entier ! ")
                        if (type(choix2) is int) and (choix2 >= 1 and choix2 <= 2):
                            choix2EnCours = False
                        else:
                            print("Saisie incorrecte ! Veuillez recommencer")
                    if choix2 == 1:    
                        rejouer = True
                    main.append(tirerUneCarte(P)) # On ajoute une carte à la main
                    afficheJeu()

        else: # On ne peut pas doubler
            rejouer = True
            choix2EnCours = True
            while valeurMain(main) <= 21 and rejouer:
                afficheJeu()
                while choix2EnCours:
                    choix2 = input("Souhaitez-vous : \n 1)Hit (Tirer une carte supplémentaire) \n 2)Stand (ne pas tirer de cartes ni augmenter la mise et passer à la révélation) \n Entrer le numéro de votre choix : ")
                    try:
                        choix2 = int(choix)
                    except:
                        print("Choix non entier ! ")
                    if (type(choix2) is int) and (choix2 >= 1 and choix2 <= 2):
                        choix2EnCours = False
                    else:
                        print("Saisie incorrecte ! Veuillez recommencer")
                if choix2 == 1:    
                    rejouer = True
                    main.append(tirerUneCarte(P)) # On ajoute une carte à la main
                    afficheJeu()
            
    # On attribue les nouvelles valeurs
    infosJoueurs[2] = main
    infosJoueurs[0] = mise
    infosJoueurs[4] = capital
    infosJoueurs[3] = valeurMain(main)
    


