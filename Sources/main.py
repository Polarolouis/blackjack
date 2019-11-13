# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:59:25 2019

@authors: Julien Morelle & Louis Lacoste
"""
from random import randint

# Initialisation
def initialisation(n): # Création de la liste des joueurs, et le dictionnaire de leurs caractéristiques
    LJ=[]
    for i in range(n+1):
        if i == 0:
            LJ.append("Croupier")
        else:
            LJ.append("Joueur "+str(i))
    J = {}
    for i in LJ:
        J[i] = [0, stratAlea(), [], 0, 200]  # [mise, stratégie, main, valeur main, capital]
    return LJ,J

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
    if len(P) > 52:  # verif qu'on peut jouer
        return True

def distrib(LJ,J,P,n):  # LJ : Liste du nom index des joueurs | J : dictionnaire avec en index les { noms index des joueurs : [Main du joueur] }
        for c in range(n):
            for i in LJ:
                J[i][2].append(P.pop()) # On ajoute une carte dans la liste de carte du joueur i


# Stratégies
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
            #nbreCartes = 1
            #while randint(1, 2) == 1:
            #   nbreCartes += 1
            return (0, nbreCartes)
        elif choix == 3:  # Stand
            return (0, 0)

def principale(nbreJoueurs, nbrePCartes, strat):
    listeJoueurs,infoJoueurs = initialisation(nbreJoueurs)
    P = melange(nbrePCartes)
    while testJouable(listeJoueurs, infoJoueurs, P):

        """ Première phase de mise """
        phase = 1
        for i in listeJoueurs:
            mise, cartePioche = infoJoueurs[i][1](phase, infoJoueurs[i][0])
            infoJoueurs[i][0] += mise

        """ Distribution des mains """
        distrib(listeJoueurs, infoJoueurs, P, 2)
        vmain = valeurMain(infoJoueurs[i][3])
        infoJoueurs[i][4] = vmain

        """ Deuxième phase de mise """
        phase = 2
        for i in listeJoueurs:
            mise, cartePioche = infoJoueurs[i][1](phase, infoJoueurs[i][0])

def valeurmain(main):
    s=0
    count=0
    for i in main:
        if i[0]=='K' or i[0]=='Q' or i[0]=='J' or i[0]=='1':
            s+=10
        elif i[0]=='A':
            s+=11
            count+=1
        else:
            s+= i[0]