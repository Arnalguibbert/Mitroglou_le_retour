# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 10:02:24 2018

@author: Valentin
"""

from grid_puissance4 import *



def is_game_over(game_grid): #le jeu est over si la grille est pleine
    return " " not in game_grid[0]



def allignement_ligne(game_grid):
    """ vérifie si il y a 4 cases identiques sur une ligne et si c'est le cas, renvoie True"""
    size = len(game_grid)
    for couche in range(0,size):
        ligne_string = ""
        for position in range(0,size):
            ligne_string += game_grid[couche][position]  # on transforme la liste en string en concaténant les caractères de la liste de caractère
        if "0000" in ligne_string or "1111" in ligne_string: 
            return True
    return False



def allignement_colonne(game_grid):
    """ vérifie si il y a 4 cases identiques sur une colonne et si c'est le cas, renvoie True"""
    size = len(game_grid)
    for position in range(0,size):
        colonne_string = "" #on commence par créer la string de la colonne
        for couche in range(0,size):
            colonne_string += game_grid[couche][position]
        if "0000" in colonne_string or "1111" in colonne_string: 
            return True
    return False
        
    
def allignement_diago(game_grid):
    """ vérifie si il y a 4 cases identiques sur une diagonale (haut-gauche --> bas-droit) et si c'est le cas, renvoie le num du vainqueur (" " si pas de vainqueur)"""
    size = len(game_grid)
    for couche in range(size-1,-1,-1): #on commence par les diagonales dont la première case appartient à la première colonne de bas en haut
        diago_string = ""
        x = 0
        y = couche
        while x < size and y < size :
            diago_string += game_grid[y][x]
            y += 1
            x += 1
        if "0000" in diago_string or "1111" in diago_string: 
            return True
        
    for position in range(1,size): #ensuite on fait les diagonales dont la première case est dans la première ligne (on a déjà fait celle qui contient celle en (0,0))
        diago_string = ""
        x = position
        y = 0
        while x < size and y < size :
            diago_string += game_grid[y][x]
            y += 1
            x += 1
        if "0000" in diago_string or "1111" in diago_string: 
            return True        
    return False

     

def allignement_antidiago(game_grid):
    """ vérifie si il y a 4 cases identiques sur une anti-diagonale (bas-gauche --> haut-droit) et si c'est le cas, renvoie le num du vainqueur (-1 si pas de vainqueur)"""
    size = len(game_grid)
    for couche in range(0,size): #on commence par les diagonales dont la première case appartient à la première colonne de haut en bas
        diago_string = ""
        x = 0
        y = couche
        while x < size and y >= 0 :
            diago_string += game_grid[y][x]
            y -= 1
            x += 1
        if "0000" in diago_string or "1111" in diago_string: 
            return True
        
    for position in range(1,size): #ensuite on fait les diagonales dont la première case est dans la dernière ligne (on a déjà fait celle qui contient celle en (0,size-1))
        diago_string = ""
        x = position
        y = size-1
        while x < size and y >= 0 :
            diago_string += game_grid[y][x]
            y -= 1
            x += 1
        if "0000" in diago_string or "1111" in diago_string:         
            return True
    return False



def is_game_won(game_grid):
    bool_list = [allignement_ligne(game_grid),allignement_colonne(game_grid),allignement_diago(game_grid),allignement_antidiago(game_grid)] #contient des -1 et éventuellement une ou plusieurs fois le numéro du gagnant
    return bool_list != [False]*4












    