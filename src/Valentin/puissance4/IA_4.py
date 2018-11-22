# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 09:50:08 2018

@author: Valentin
"""

"""
Implémentation IA_1 (gogol)
"""

from grid_puissance4 import move_possible


import random as rd


def get_position(game_grid,num_joueur):
    # le num du joueur doit être "0" ou "1"
    size = len(game_grid)
    commande_valide = False
    while not commande_valide:
        position = rd.randrange(0,size)
        if move_possible(game_grid,str(position)):
            return position #on prend des commandes aléatoires jusqu'à avoir une commande valide. Cela nécessite que la grille ne soit pas pleine

        
    
    