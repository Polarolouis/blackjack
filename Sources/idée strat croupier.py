def stratcroupier(phase, infosJoueurs, P):
    phase ==1
    on tire une carte du paquet et on la place dans la liste des cartes sorties
    on en tire une nouvelle pas dans la liste des cartes sorties
    mais on somme quand meme les 2 cartes dans vcroupier

    phase==2
    les joueurs ont fait leurs jeux
    on ajoute la 2eme carte au pool de cartes
    on compare vmaincroupier avec 17:
        si c'est inferieur il tire une carte ajoutée au pool

def stratCroupier(phase, infosJoueurs,P, valUpCard):
    main = infosJoueurs[2]
    if phase==2:
        tirerUneCarte(P)
        while valeurMain(main)<=17:
            main.append(tirerUneCarte(P)

    infosJoueurs[2] = main
    infosJoueurs[3] = valeurMain(main)



