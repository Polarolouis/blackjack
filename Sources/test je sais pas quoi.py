def endphase(LJ, J):
    vmain_croupier = J["Croupier"][3]
    for i in LJ:
        #print(" End Phase : "+str(LJ))
        infosJoueurs = J[i]
        # On récupère les valeurs
        capital = infosJoueurs[4]
        mise = infosJoueurs[0]
        main = infosJoueurs[2]
        vmain = infosJoueurs[3]

        if i == "Croupier":
            capital = 200
        else:
            if vmain == 21 and len(main) == 2:
                print("BLACKJACK !!!")
                capital += int(round(2.5 * mise))
            elif vmain_croupier > 21:
                if vmain <= 21:
                    capital+= 2*mise
                    print(i + "a battu le croupier")
                else:
                    capital+= mise
                    print(i + "a fait exaequo avec le croupier")
            else:
                if vmain_croupier==vmain:
                    capital+=mise
                    print(i + "a fait exaequo avec le croupier")
                if vmain < vmain_croupier:
                    print(i + "a perdu contre le croupier")
                else:
                    print(i + "a battu le croupier")
                    capial+=2*mise

        # On vide main et mise
        main = []
        mise = 0
        vmain = valeurMain(main)

        # On set toutes les valeurs modifiées
        infosJoueurs[4] = int(floor(round(capital)))
        infosJoueurs[0] = mise
        infosJoueurs[2] = main
        infosJoueurs[3] = vmain
