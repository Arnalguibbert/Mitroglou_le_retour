# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 12:01:44 2018

@author: Valentin
"""

from grid_2048 import *

def is_grid_full(game_grid):
    return (0 not in get_all_tiles(game_grid))

def move_possible_left(game_grid):
    #On test pour les mouvements à gauche
    size = len(game_grid)
    for ligne in game_grid:
        for absi in range(size-1):
            if ligne[absi] in {0," "} and ligne[absi+1] not in {0," "}:
                return True
            if ligne[absi] == ligne[absi+1] and ligne[absi] not in {0," "}:
                return True
    return False


def move_possible_right(game_grid):
    #On test pour les mouvements à droite
    size = len(game_grid)
    for ligne in game_grid:
        for absi in range(1,size):
            if ligne[absi] in {0," "} and ligne[absi-1] not in {0," "}: #ici une case non vide peut "tomber"
                return True
            if ligne[absi] == ligne[absi-1] and ligne[absi] not in {0," "}: #ici une case non vide peut "fusionner"
                return True
    return False




def move_possible_up(game_grid):
    #On test pour les mouvements en haut
    size = len(game_grid)
    for absi in range(size):
        for ordo in range(size-1):
            if grid_get_value(game_grid,absi,ordo) == 0 and grid_get_value(game_grid,absi,ordo+1) not in {0," "} :
                return True
            if grid_get_value(game_grid,absi,ordo) == grid_get_value(game_grid,absi,ordo+1) and grid_get_value(game_grid,absi,ordo) not in {0," "}:
                return True
    return False

def move_possible_down(game_grid):
    #On test pour les mouvements en bas
    size = len(game_grid)
    for absi in range(size):
        for ordo in range(1,size):
            if grid_get_value(game_grid,absi,ordo) == 0 and grid_get_value(game_grid,absi,ordo-1) not in {0," "} :
                return True
            if grid_get_value(game_grid,absi,ordo) == grid_get_value(game_grid,absi,ordo-1) and grid_get_value(game_grid,absi,ordo) not in {0," "} :
                return True
    return False



def move_possible(game_grid):
    return [move_possible_left(game_grid),move_possible_right(game_grid),move_possible_up(game_grid),move_possible_down(game_grid)]


def is_game_over(game_grid):
    return move_possible(game_grid) == [False]*4


def get_grid_tile_max(game_grid):
    tiles = get_all_tiles(game_grid)
    return max(tiles)

def grid_gagnant(game_grid):
    return get_grid_tile_max(game_grid) >= 2048







