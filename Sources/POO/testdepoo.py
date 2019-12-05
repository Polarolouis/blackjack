# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 19:38:12 2019

@author: lordo
"""

class Joueur:
    def __init__(self):
        self.nom = "Joueur"
        self.main = []
        self.capital = 200
        self.mise = 0


    def _set_nom(self, v):
        self.nom = v


    def _set_main(self, v):
        self.main = v


    def _set_capital(self, v):
        self.capital = v


    def _set_mise(self, v):
        self.mise = v


    def _get_nom(self):
        return self.nom


    def _get_main(self):
        return self.main


    def _get_capital(self):
        return self.capital


    def _get_mise(self):
        return self.mise