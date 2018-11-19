# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 10:29:50 2018

@author: Valentin
"""

from grid_puissance4 import *
from fin_jeu_puissance4 import *
import random as rd

def get_position(nom_IA,game_grid,num_joueur):
    if nom_IA == "gogol":
        return rd.randrange(0,len(game_grid))
    if nom_IA == "terminator":
        for position in range(0,len(game_grid)): #on regarde si on peut gagner
            if is_game_won(update_grid(game_grid,position,num_joueur))[0]:
                return position
        for position in range(0,len(game_grid)): #on doit empêcher le joueur adverse de gagner tout de suite
            if is_game_won(update_grid(game_grid,position,str(1-int(num_joueur))))[0]:
                return position
        return rd.randrange(0,len(game_grid))
        
    
    
    


def game_play():
    size = int(input('taille de la grille (carrée) :'))
    game_grid = init_grid(size)
    joueur_actif = "0"
    while (not is_game_won(game_grid)[0]) and (not is_game_over(game_grid)):
        correct_command = False #on fait un booléen pour enregistrer la commande de l'utilisateur jusqu'à avoir une commande valide
        while not correct_command:
            try:
                position = int(input("joueur "+joueur_actif+", position:"))
            except ValueError:
                print("position invalide !")
            if move_possible(game_grid)[position]:
                correct_command = True
            else:
                print("colonne pleine !")
        game_grid = update_grid(game_grid,position,joueur_actif)
        print(game_grid)
        joueur_actif = str(1-int(joueur_actif)) #on change le joueur actif
    if is_game_won(game_grid)[0]:
        print("Le joueur",is_game_won(game_grid)[1],"a gagné !")
        return
    print("Match nul")
    return



def tournoi():
    size = int(input('taille de la grille (carrée) :'))
    game_grid = init_grid(size)
    print(game_grid)
    print()
    joueur_actif = "0"
    while (not is_game_won(game_grid)[0]) and (not is_game_over(game_grid)):
        if joueur_actif == "0":
            nom_IA = "gogol"
        else:
            nom_IA = "terminator"
            
        correct_command = False #on fait un booléen pour enregistrer la commande de l'utilisateur jusqu'à avoir une commande valide
        while not correct_command:
            position = get_position(nom_IA,game_grid,joueur_actif)
            if move_possible(game_grid)[position]:
                correct_command = True
            else:
                print("colonne pleine !")
        game_grid = update_grid(game_grid,position,joueur_actif)
        print(game_grid)
        print()
        joueur_actif = str(1-int(joueur_actif)) #on change le joueur actif
    if is_game_won(game_grid)[0]:
        print("Le joueur",is_game_won(game_grid)[1],"a gagné !")
        return
    print("Match nul")
    return











