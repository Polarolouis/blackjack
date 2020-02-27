# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:59:25 2019

@authors: Julien Morelle & Louis Lacoste
"""
from random import randint
from numpy import sqrt, floor

#Color assignation
MAGENTA = '\033[35m'   # mode 31 = red forground
RESET = '\033[0m'  # mode 0  = reset

# Initialisation, Endphase et Banqueroute
def initialisation(n, strat, humain=False): # Création de la liste des joueurs, et le dictionnaire de leurs caractéristiques
    LJ=[]
    for i in range(n+1):
        if i == n:
            LJ.append("Croupier")
        else:
            LJ.append("Joueur "+str(i+1))
    J = {}
    for i in LJ:
        if i == 'Croupier':
            J[i] = [0, stratCroupier, [], 0, 200]  # [mise, stratégie, main, valeur main, capital]
        else:
            J[i] = [0, strat, [], 0, 200]  # [mise, stratégie, main, valeur main, capital]
    return LJ,J


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
                capital += int( 3* mise)
            elif vmain_croupier > 21:
                if vmain <= 21:
                    capital += 2*mise
                else:
                    capital += mise
            elif vmain_croupier <= 21:
                if vmain_croupier==vmain:
                    capital += mise
                elif (vmain>vmain_croupier and vmain<=21):
                    capital+= 2*mise

        # On vide main et mise
        main = []
        mise = 0
        vmain = valeurMain(main)

        # On set toutes les valeurs modifiées
        infosJoueurs[4] = capital
        infosJoueurs[0] = mise
        infosJoueurs[2] = main
        infosJoueurs[3] = vmain


def testBanqueroute(nom, J, LJ):
    if J[nom][4] <= 2:
        # Le joueur ne peut plus jouer, il faut le retirer des listes
        del J[nom]  # On supprime ses données
        LJ.remove(nom)  # On le retire de la liste des joueurs


#Mélange
def melange(n):
    """ Fonction générant un mélange de plusieurs paquets de cartes
    sous la forme d'une liste """
    P = n*52*[0]
    conv = ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC']
    dic = {'AH': n, '2H': n, '3H': n, '4H': n, '5H': n, '6H': n, '7H': n, '8H': n, '9H': n, '10H': n, 'JH': n, 'QH': n, 'KH': n, 'AS': n, '2S': n, '3S': n, '4S': n, '5S': n, '6S': n, '7S': n, '8S': n, '9S': n, '10S': n, 'JS': n, 'QS': n, 'KS': n, 'AD': n, '2D': n, '3D': n, '4D': n, '5D': n, '6D': n, '7D': n, '8D': n, '9D': n, '10D': n, 'JD': n, 'QD': n, 'KD': n, 'AC': n, '2C': n, '3C': n, '4C': n, '5C': n, '6C': n, '7C': n, '8C': n, '9C': n, '10C': n, 'JC': n, 'QC': n, 'KC': n}
    for i in range((n*52)):         # on affecte à chaque valeur de la liste P un nom de carte
        while P[i] == 0:            # tant que le iéme terme de la liste n'a pas de nom on va continuer a essayer de lui en trouver                                             une disponible
            r = randint(0, 51)      # on tire aléatoirement une carte parmis les 52 d'un paquet
            if dic[conv[r]] != 0:   # si la carte est encore disponible dans le paquet, on la place dans la liste
                P[i] = conv[r]
                dic[conv[r]] -= 1   # dic[conv[r]] = dic[conv[r]] -1 (on diminue de 1 la valeur de l'index de la carte tirée (une carte de moins est disponible)
    return P

# Distribution
def testJouable(LJ, J, P):
    if len(P) > 52 and len(LJ) >= 2:  # verif qu'on peut jouer
        return True
    else:
        return False

def distrib(LJ,J,P,n):  # LJ : Liste du nom index des joueurs | J : dictionnaire avec en index les { noms index des joueurs : [Main du joueur] }
    for i in LJ:
        if i != "Croupier":
            for c in range(n):
                    J[i][2].append(tirerUneCarte(P)) # On ajoute une carte dans la liste de carte du joueur i
        else:
            for c in range(n-1):
                J[i][2].append(tirerUneCarte(P)) # On ajoute une carte dans la liste de carte du croupier



def tirerUneCarte(P):
    carte = P.pop()
    calculRC(carte)
    return carte

def calculRC(carte):
    global RC
    if (carte[0] == '2') or (carte[0] == '3') or (carte[0] == '4') or (carte[0] == '5') or (carte[0] == '6'):
        RC += 1
    elif (carte[0] == '1') or (carte[0] == 'J') or (carte[0] == 'Q') or (carte[0] == 'K') or (carte[0] == 'A'):
        RC += -1
    else:
        RC += 0

def setTC(P):
    global RC
    global TC
    TC= RC/(len(P))



def valeurMain(main):
    S = 0
    count = 0
    for i in main:
        if i[0] == 'K' or i[0] == 'Q' or i[0] == 'J' or i[0] == '1':
            S += 10
        elif i[0] == 'A':
            S += 11
            count += 1
        else:
            S += int(i[0])
    while S > 21 and count > 0:
        S -= 10
        count -= 1
    return S


# Stratégies
def stratAlea(phase, infosJoueurs, P, valUpCard):
    # avec phase qui correspond à la phase de jeu
    """ mise entre 2 et 100 euros aléatoirement
    Soit il tire | soit il double
    Si il tire, il a une chance sur deux d'arrêter de tirer """
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
    infosJoueurs[3] = valeurMain(main)

def stratBasique(phase, infosJoueurs, P, valUpCard):
    # avec phase qui correspond à la phase de jeu
    # On récupère les valeurs dont la carte du croupier (cartecroup)
    cartecroup= valUpCard
    capital = infosJoueurs[4]
    mise = infosJoueurs[0]
    main = infosJoueurs[2]

    if phase == 1:  # Mise de départ
        mise = (capital//20) + (capital//10) + (capital//5) + 1 # Pour éviter que le joueur puisse ne plus miser
        capital -= mise
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

def stratHiLow(phase, infosJoueurs, P, valUpCard):
    # avec phase qui correspond à la phase de jeu
    # On récupère les valeurs dont la carte du croupier (cartecroup)
    cartecroup= valUpCard
    capital = infosJoueurs[4]
    mise = infosJoueurs[0]
    main = infosJoueurs[2]
    global TC
    if phase == 1:  # Mise de départ
        if TC>=0:
            mise = int(floor((capital-1)**TC))
        else:
            mise = 1
        capital -= mise
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

def stratCroupier(phase, infosJoueurs,P, valUpCard):
    main = infosJoueurs[2]
    if phase==2:
        tirerUneCarte(P)
        while valeurMain(main)<=17:
            main.append(tirerUneCarte(P))

    infosJoueurs[2] = main
    infosJoueurs[3] = valeurMain(main)

def principale(nbreJoueurs, nbrePCartes, stratChoisie, verbose=False):
    tour = 0
    listeJoueurs, infoJoueurs = initialisation(nbreJoueurs, stratChoisie)
    P = melange(nbrePCartes)
    upCardCroupier = []
    global RC
    RC = 0
    global TC
    TC = 0
    while testJouable(listeJoueurs, infoJoueurs, P):
        tour += 1
        if verbose:
            print("Tour n° : " + str(tour))
        phase = 0
        """ Première phase de mise """
        phase = 1
        for i in listeJoueurs:
            strat = infoJoueurs[i][1]
            strat(phase, infoJoueurs[i], P, 0)

        """ Distribution des mains """
        distrib(listeJoueurs, infoJoueurs, P, 2)
        upCardCroupier.append(infoJoueurs["Croupier"][2][0])
        valUpCard = valeurMain(upCardCroupier)
        """ Deuxième phase de mise """
        phase = 2
        for i in listeJoueurs:
            strat = infoJoueurs[i][1]
            strat(phase, infoJoueurs[i], P, valUpCard)
        setTC(P)  # On actualise le True Count
        if verbose:
            print("L'état du jeu est : "+str(infoJoueurs)+"\n")
        endphase(listeJoueurs, infoJoueurs)
        for i in listeJoueurs:
            testBanqueroute(i, infoJoueurs, listeJoueurs)
        for i in listeJoueurs:
            testBanqueroute(i, infoJoueurs, listeJoueurs)
        if verbose:
            print("Après avoir testé la banqueroute la partie est dans l'état suivant : " + str(infoJoueurs) +"\n Le True Count est de : " + str(TC) + "\n")
        upCardCroupier = []
    if verbose:
        print("Nombre de tours pour finir la partie : " + str(tour) + "\nNombre de cartes restantes dans le paquet : " + str(len(P)))
        return tour
    else:
        return tour


# Tests
def stat(strat, N):
    T=0
    V=0
    R=[]
    for i in range(N):
        R.append(principale(1, 50, strat))
        T+=R[i]
    T = T / N
    for i in range(len(R)):
        V = (R[i] - T)**2
    V = sqrt(V / (N-1))
    return {strat.__name__ : {'Moyenne' : T, 'Ecart-type' : V }}

def compare(strat1, strat2, N):
    T1=0
    T2=0
    V1=0
    V2=0
    R1=[]
    R2=[]
    for i in range(N):
        R1.append(principale(1, 50, strat1))
        T1+=R1[i]
        R2.append(principale(1, 50, strat2))
        T2+=R2[i]
    T1 = T1 / N
    T2 = T2 / N
    for i in range(len(R1)):
        V1 = (R1[i] - T1)**2
        V2 = (R2[i] - T2)**2
    V1 = sqrt(V1 / (N-1))
    V2 = sqrt(V2 / (N-1))
    return {strat1.__name__ : {'Moyenne' : T1, 'Ecart-type' : V1 } , strat2.__name__ : {'Moyenne' : T2, 'Ecart-type' : V2 }}


# Affichage :