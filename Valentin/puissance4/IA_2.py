# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 09:58:32 2018

@author: Valentin
"""

"""
Implémentation IA_2 (C3PO)
"""

from grid_puissance4 import move_possible
from fin_jeu_puissance4 import is_game_won
from grid_puissance4 import update_grid

import random as rd


def get_position(game_grid,num_joueur):
    # le num du joueur doit être "0" ou "1"
    size = len(game_grid)
    for position in range(0,size): #on regarde si on peut gagner
        if move_possible(game_grid,str(position)) and is_game_won(update_grid(game_grid,position,num_joueur)): #on regarde seulement les positions possibles en utilisant l'évaluation paresseuse des booléens
            return position
    for position in range(0,size): #on doit empêcher le joueur adverse de gagner tout de suite
        if move_possible(game_grid,str(position)) and is_game_won(update_grid(game_grid,position,str(1-int(num_joueur)))): #même remarque
            return position
        #si on est là, on renvoit une commande au hasard parmis les possibilités
    commande_valide = False
    while not commande_valide:
        position = rd.randrange(0,size)
        if move_possible(game_grid,str(position)):
            return position #on prend des commandes aléatoires jusqu'à avoir une commande valide. Cela nécessite que la grille ne soit pas pleine

