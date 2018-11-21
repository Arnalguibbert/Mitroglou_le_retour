# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 09:44:26 2018

@author: Valentin
"""
import copy


def init_game(size): # la grille sera carrée
    game_grid = []
    for i in range(0,size):
        game_grid.append([' ']*size)
    return game_grid



def move_possible(game_grid,str_position):
    # Dit si la colonne à la position donnée peut acceuillir un jeton. La commande est une string
    return game_grid[0][int(str_position)] == " "


def update_grid(game_grid,position,num_joueur):
    res = copy.deepcopy(game_grid)
    #ajoute un jeton à la position donnée, la colonne ne doit pas être pleine
    size = len(game_grid)
    if game_grid[size-1][position] == " ": #on commence par le cas où la colonne est vide
        res[size-1][position] = num_joueur
        return res
    for ligne in range(size-1,0,-1): #va de hauteur-1 à 1 en décroissant
        if game_grid[ligne][position] != " " and game_grid[ligne-1][position] == " ":
            res[ligne-1][position] = num_joueur
            return res




def update_grid_0(game_grid,num_joueur):
    return update_grid(game_grid,0,num_joueur)
    

def update_grid_1(game_grid,num_joueur):
    return update_grid(game_grid,1,num_joueur)
  
    
def update_grid_2(game_grid,num_joueur):
    return update_grid(game_grid,2,num_joueur)
  
    
def update_grid_3(game_grid,num_joueur):
    return update_grid(game_grid,3,num_joueur)
    

def update_grid_4(game_grid,num_joueur):
    return update_grid(game_grid,4,num_joueur)
  
    
def update_grid_5(game_grid,num_joueur):
    return update_grid(game_grid,5,num_joueur)


def update_grid_6(game_grid,num_joueur):
    return update_grid(game_grid,6,num_joueur)

  











      