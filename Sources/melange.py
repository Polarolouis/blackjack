# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:59:25 2019

@authors: Julien Morelle & Louis Lacoste
"""
from random import randint


def melange(n):
    """ Fonction générant un mélange de plusieurs paquets de cartes
    sous la forme d'une liste """
    P = n*52*[0]
    conv = ['1H', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', '1S', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', '1D', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', '1C', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC']
    dic = {'1H': n, '2H': n, '3H': n, '4H': n, '5H': n, '6H': n, '7H': n, '8H': n, '9H': n, '10H': n, 'JH': n, 'QH': n, 'KH': n, '1S': n, '2S': n, '3S': n, '4S': n, '5S': n, '6S': n, '7S': n, '8S': n, '9S': n, '10S': n, 'JS': n, 'QS': n, 'KS': n, '1D': n, '2D': n, '3D': n, '4D': n, '5D': n, '6D': n, '7D': n, '8D': n, '9D': n, '10D': n, 'JD': n, 'QD': n, 'KD': n, '1C': n, '2C': n, '3C': n, '4C': n, '5C': n, '6C': n, '7C': n, '8C': n, '9C': n, '10C': n, 'JC': n, 'QC': n, 'KC': n}
    for i in range((n*52)):         # on affecte à chaque valeur de la liste P un nom de carte
        while P[i] == 0:            # tant que le iéme terme de la liste n'a pas de nom on va continuer a essayer de lui en trouver                                             une disponible
            r = randint(0, 51)      # on tire aléatoirement une carte parmis les 52 d'un paquet
            if dic[conv[r]] != 0:   # si la carte est encore disponible dans le paquet, on la place dans la liste
                P[i] = conv[r]
                dic[conv[r]] -= 1   # dic[conv[r]] = dic[conv[r]] -1 (on diminue de 1 la valeur de l'index de la carte tirée (une carte de moins est disponible)
    return P












