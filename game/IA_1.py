# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 09:50:08 2018

@author: Valentin
"""

"""
Implémentation IA_1 (gogol)
"""




import random as rd

def move_possible(game_grid,str_position):
    # Dit si la colonne à la position donnée peut acceuillir un jeton. La commande est une string
    return game_grid[0][int(str_position)] == " "


def get_position(game_grid,num_joueur):
    # le num du joueur doit être "0" ou "1"
    size = len(game_grid)
    commande_valide = False
    while not commande_valide:
        position = rd.randrange(0,size)
        if move_possible(game_grid,str(position)):
            return position #on prend des commandes aléatoires jusqu'à avoir une commande valide. Cela nécessite que la grille ne soit pas pleine

        
    
    