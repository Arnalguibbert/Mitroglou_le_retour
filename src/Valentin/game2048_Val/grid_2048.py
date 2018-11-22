# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 15:02:22 2018

@author: Valentin
"""
import random as rd

THEMES = {"0": {"name": "Default", 0: " ", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: " ", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: " ", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}


def create_grid(taille):
    game_grid = []
    for i in range(0,taille):
        game_grid.append([' ']*taille)
    return game_grid



def grid_add_new_tile_at_position(game_grid,absi,ordo):
    game_grid[ordo][absi] = get_value_new_tile()
    return game_grid



def get_all_tiles(game_grid):
    tiles = []
    for ligne in game_grid:
        for case in ligne:
            if case == ' ': #Case vide, codée par 0
                tiles.append(0)
            else :
                tiles.append(case)
    return tiles



def get_value_new_tile():
    var_aleat = rd.randrange(0,10) #la var prend un nombre aléat entre 0 et 9
    if var_aleat == 0 : #La proba de passer ce test est de 10%
        return 4
    else: #Et donc ici de 90%
        return 2


def get_empty_tiles_positions(game_grid):
    empty_tiles = []
    taille = len(game_grid)
    for absi in range(0,taille):
        for ordo in range(0,taille):
            if game_grid[ordo][absi] in [0," "]:
                empty_tiles.append((absi,ordo))
    return empty_tiles
                


def grid_get_value(game_grid,x,y):
    if game_grid[y][x] == ' ':
        return 0  #Case vide, codée par 0
    else:
        return game_grid[y][x]



def get_new_position(game_grid):
    empty_tiles = get_empty_tiles_positions(game_grid)
    if empty_tiles == []: #grille remplie !
        return (0,0) #Ici on renvoie une coordonnée valide quelconque, la fin du jeu sera résolue ultérieurement
    else: #On prend une coordonnée aléatoire de la liste des cases vides si elle n'est pas vide
        indice_aleat = rd.randrange(0,len(empty_tiles))
        return empty_tiles[indice_aleat]



def grid_add_new_tile(game_grid):
    absi,ordo = get_new_position(game_grid)
    return grid_add_new_tile_at_position(game_grid,absi,ordo)



def init_grid(taille):
    game_grid = create_grid(taille)
    game_grid = grid_add_new_tile(game_grid)
    game_grid = grid_add_new_tile(game_grid)
    return game_grid
    













