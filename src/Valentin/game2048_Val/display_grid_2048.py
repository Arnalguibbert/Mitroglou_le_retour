# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 16:42:57 2018

@author: Valentin
"""
from grid_2048 import *


def long_value_with_theme(game_grid,theme):
    tiles = get_all_tiles(game_grid)
    res = 2 # j'ai choisi que lle minimum de la largeur d'une case va être 4
    for tile in tiles:
        if len(str(theme[tile])) > res:
            res = len(str(theme[tile]))
    return res


def grid_to_string_with_size_and_theme(game_grid,theme):
    size = len(game_grid)
    size_tile = long_value_with_theme(game_grid,theme)
    string = ""
    for ordo in range(size):
        string += "\n"
        string += (" " + "=" * size_tile)*size
        string += "\n"
        for absi in range(size):
            string += "|"+str(theme[grid_get_value(game_grid,absi,ordo)]).center(size_tile) #On crée les délimiters de case et la case sera une string contenant la valeur au centre et suffisamment d'espace autour pour être de la bonne largeur
        string += "|"
    string += "\n"
    string += (" " + "=" * size_tile)*size
    return string
