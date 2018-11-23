# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 11:34:59 2018

@author: Valentin
"""

import random as rd


def update_grid_up(game_grid):
    # on cherche la case vide dans les couches 1 et 2 (les 2 dernières)
    for ordo in range(1,3):
        for absi in range(0,3):
            if game_grid[ordo][absi] == "*":
                game_grid[ordo][absi], game_grid[ordo-1][absi] = game_grid[ordo-1][absi], game_grid[ordo][absi]
    return game_grid



def update_grid_down(game_grid):
    # on cherche la case vide dans les couches 0 et 1 (les 2 premières)
    for ordo in range(0,2):
        for absi in range(0,3):
            if game_grid[ordo][absi] == "*":
                game_grid[ordo][absi], game_grid[ordo+1][absi] = game_grid[ordo+1][absi], game_grid[ordo][absi]
    return game_grid



def update_grid_left(game_grid):
    # on cherche la case vide dans les absicces 1 et 2 (les 2 dernières)
    for absi in range(1,3):
        for ordo in range(0,3):
            if game_grid[ordo][absi] == "*":
                game_grid[ordo][absi], game_grid[ordo][absi-1] = game_grid[ordo][absi-1], game_grid[ordo][absi]
    return game_grid



def update_grid_right(game_grid):
    # on cherche la case vide dans les absicces 0 et 1 (les 2 premières)
    for absi in range(0,2):
        for ordo in range(0,3):
            if game_grid[ordo][absi] == "*":
                game_grid[ordo][absi], game_grid[ordo][absi+1] = game_grid[ordo][absi+1], game_grid[ordo][absi]
    return game_grid



def move_possible(game_grid,command):
    if command == "update_grid_up":
        return "*" not in game_grid[0]
    elif command == "update_grid_down":
        return "*" not in game_grid[2]
    elif command == "upgrade_grid_left":
        return "*" not in [game_grid[0][0],game_grid[1][0],game_grid[2][0]]
    elif command == "update_grid_right":
        return "*" not in [game_grid[0][2],game_grid[1][2],game_grid[2][2]]


def init_game(GRID_LEN): #fictive arg
    """
    Renvoie une grille résolvable pour commencer le jeu
    """
    #on part de la grille finale
    game_grid = [["1","2","3"],["4","5","6"],["7","8","*"]]
    last_mouvement = "nothing" #enregistre le dernier mouvement qu'on a fait
    for k in range(0,30): #on fait 20 mouvements aléatoires en évitant de faire 2 fois le même
        mouvement = rd.choice(["update_grid_up","update_grid_down","upgrade_grid_left","update_grid_right"])
        while mouvement == last_mouvement:
            mouvement = rd.choice(["update_grid_up","update_grid_down","upgrade_grid_left","update_grid_right"])
        last_mouvement = mouvement
        #une fois qu'on a le mouvement on met à jour la grille
        if mouvement == "update_grid_up":
            game_grid = update_grid_up(game_grid)
        elif mouvement == "update_grid_down":
            game_grid = update_grid_down(game_grid)
        elif mouvement == "upgrade_grid_left":
            game_grid = update_grid_left(game_grid)
        elif mouvement == "update_grid_right":
            game_grid = update_grid_right(game_grid)
    return game_grid
        

def is_game_won(game_grid):
    return game_grid == [["1","2","3"],["4","5","6"],["7","8","*"]]

def is_game_over(game_grid):
    return False


color_dico = {"*":['#ffffffff',"","carre"],"0":['#add8e6',"0","carre"],"1":['#add8e6',"1","carre"],"2":['#add8e6',"2","carre"],"3":['#add8e6',"3","carre"],"4":['#add8e6',"4","carre"],"5":['#add8e6',"5","carre"],"6":['#add8e6',"6","carre"],"7":['#add8e6',"7","carre"],"8":['#add8e6',"8","carre"]}


SIZE = 300
GRID_PADDLE = 4
GRID_LEN = 3

dico_command = {"up": [update_grid_up,"up",[0,1]], "down": [update_grid_down,"down",[2,1]], "left": [update_grid_left,"left",[1,0]], "right": [update_grid_right,"right",[1,2]]}


def info_necessary():
    return GRID_LEN,GRID_PADDLE,dico_command,color_dico,SIZE,init_game,is_game_over,move_possible,is_game_won












