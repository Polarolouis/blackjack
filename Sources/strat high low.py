def stratBasique(phase, infosJoueurs, P, valUpCard):
    # avec phase qui correspond à la phase de jeu
    # On récupère les valeurs dont la carte du croupier (cartecroup)
    cartecroup= valUpCard
    capital = infosJoueurs[4]
    mise = infosJoueurs[0]
    main = infosJoueurs[2]
    global TC


    if phase == 1:  # Mise de départ
        if TC>=0:
            mise = (capital-1)^TC
        else:
            mise = 1
    elif phase == 2:
        jouer = True
        while jouer == True :
            if valeurMain(main) <=8 or (valeurMain(main) == 9 and (cartecroup>=7 or cartecroup==2)) or (valeurMain(main)==10 and cartecroup>=10) or (valeurMain(main)== 12 and (cartecroup==2 or cartecroup==3)) or ((valeurMain(main)>= 12 and valeurMain(main)<=16) and cartecroup>=7):
                main.append(tirerUneCarte(P)) # On ajoute une carte à la main
                # il va hit
            elif valeurMain(main) >= 17 or ((valeurMain(main)>= 13 and valeurMain(main) <= 16) and cartecroup <=6) or (valeurMain(main) == 12 and (cartecroup>=4 and cartecroup <=6)):
                jouer = False
                # il va stand
            else:
                main.append(tirerUneCarte(P)) # On ajoute une carte à la main
                capital -= mise
                mise = 2*mise
                jouer= False
                # il va double

    # On attribue les nouvelles valeurs
    infosJoueurs[2] = main
    infosJoueurs[0] = mise
    infosJoueurs[4] = capital
    infosJoueurs[3] = valeurMain(main)