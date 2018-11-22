# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 10:15:36 2018

@author: Valentin
"""

"""
Implémentation IA_3 (terminator)
"""

from grid_puissance4 import move_possible
from fin_jeu_puissance4 import is_game_won
from grid_puissance4 import update_grid
import random as rd


def get_position(game_grid,num_joueur):
    for position in range(0,len(game_grid)): #on regarde si on peut gagner
        if move_possible(game_grid,str(position)) and is_game_won(update_grid(game_grid,position,num_joueur)): #même remarque
            return position
    for position in range(0,len(game_grid)): #on doit empêcher le joueur adverse de gagner tout de suite
        if move_possible(game_grid,str(position)) and is_game_won(update_grid(game_grid,position,str(1-int(num_joueur)))): #idem
            return position
    tests = 0 #nombre de tentatives pour proposer un coup
    mauvais_coup = True #juste pour pouvoir passer la boucle
    while tests < 100 and mauvais_coup:
        tests += 1
        position = rd.randrange(0,len(game_grid)) #on choisit une position au hasard
        if move_possible(game_grid,str(position)): #on regarde si on a un coup possible
            mauvais_coup = False
            nouvelle_grille = update_grid(game_grid,position,num_joueur)
            for position2 in range(0,len(game_grid)): #on regarde si l'adversaire peut gagner après avoir jouer le coup
                if move_possible(nouvelle_grille,str(position2)) and is_game_won(update_grid(nouvelle_grille,position2,str(1-int(num_joueur)))):
                    mauvais_coup = True
            if mauvais_coup == False:
                return position #si c'est pas un mauvais coup au sens de "l'adversaire ne gagne pas juste après, on y va"
    commande_valide = False
    while not commande_valide:
        position = rd.randrange(0,len(game_grid))
        if move_possible(game_grid,str(position)):
            return position #on prend des commandes aléatoires jusqu'à avoir une commande valide. Cela nécessite que la grille ne soit pas pleine

