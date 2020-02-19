#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 18:58:13 2020

@authors: Julien Morelle & Louis Lacoste
"""
import blackjack as bj
N = input("Saisir N le nombre de parties à itérer")
print(bj.stat(bj.stratHiLow, N))