# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 10:29:18 2018

@author: Valentin
"""

from grid_2048 import *
from display_grid_2048 import *
from textual_2048 import *
from fin_jeu_2048 import *
import time

from tkinter import *
from pprint import pformat
from functools import partial


import random as rd

def random_play():
    game_grid = init_game(3)
    theme = THEMES["0"]
    print(grid_to_string_with_size_and_theme(game_grid,theme))
    while not is_game_over(game_grid) and not grid_gagnant(game_grid):
        move_bool = move_possible(game_grid)
        move_str = ["left","right","up","down"]
        for indice in range(4): #On supprime les mouvements impossible
            indices_a_delete = [] #indices des éléments à supprimer
            if not move_bool[indice]:
                indices_a_delete.append(indice)
        indices_a_delete.reverse() # la liste des indices est trié par ordre décroissant ici pour éviter les out of range
        for indice in indices_a_delete:
            del move_str[indice]
        # Comme il reste des mouvements possible, ici move_str != []
        direction = rd.choice(move_str)
        #time.sleep(0.5)
        print()
        print(direction)
        game_grid = move_grid(game_grid,direction)
        print(grid_to_string_with_size_and_theme(game_grid,theme))
        game_grid = grid_add_new_tile(game_grid)
        #time.sleep(0.5)
        print()
        print("new tile")
        print(grid_to_string_with_size_and_theme(game_grid,theme))
        
    if grid_gagnant(game_grid):
        print('GAGNE')
    else:
        print('PERDU')
     
def ask_and_read_grid_size():
    size = int(input("Entrez la taille de la grille :"))
    return size

def ask_and_read_grid_theme():
    number_theme = input("Entrez le thème choisi (de 0 à 2) :")
    return THEMES[number_theme]        

def ask_and_read_direction():
    """Renvoie la direction et la position dans la liste des directions"""
    command = read_player_command()
    if command == "g":
        return "left",0
    elif command == "d":
        return "right",1
    elif command == "h":
        return "up",2
    elif command == "b":
        return "down",3
    else:
        return None

def game_play():
    size = ask_and_read_grid_size()
    theme = ask_and_read_grid_theme()
    game_grid = init_game(size)
    print(grid_to_string_with_size_and_theme(game_grid,theme))
    while not is_game_over(game_grid) and not grid_gagnant(game_grid):
        move_bool = move_possible(game_grid)
        direction_et_position = ask_and_read_direction()
        while not move_bool[direction_et_position[1]]:#mouvement impossible !
            print("mouvement impossible !")
            direction_et_position = ask_and_read_direction()
        direction = direction_et_position[0]
        print()
        game_grid = move_grid(game_grid,direction)
        print(grid_to_string_with_size_and_theme(game_grid,theme))
        game_grid = grid_add_new_tile(game_grid)
        print()
        print("new tile")

        print(grid_to_string_with_size_and_theme(game_grid,theme))
        
    if grid_gagnant(game_grid):
        print('GAGNE')
    else:
        print('PERDU')    

game_play()
    
def game_play_tkinter():
    #réalise le jeu avec l'interface graphique
    fenetre = Tk()
    # entrée
    value = StringVar() 
    value.set("texte par défaut")
    entree = Entry(fenetre, textvariable = text, width=30)
    entree.pack()











