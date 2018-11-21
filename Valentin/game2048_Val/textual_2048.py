# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 09:55:24 2018

@author: Valentin
"""


from grid_2048 import *



def read_player_command():
    move = input("Entrez votre commande (q (gauche), d (droite), z (haut), s (bas)):")
    while move not in {"q","d","z","s","exit"}: #on rajoute la commande secrète "exit" pour arrêter
        print("la commande n'est pas valide")
        move = input("Entrez votre commande (q (gauche), d (droite), z (haut), s (bas)):")
    return move



def read_size_grid():
    size = input("Entrez la taille de la grille :")
    return size



def read_theme_grid():
    number_theme = input("Entrez le thème choisi (de 0 à 2) :")
    return THEMES[number_theme]



def move_row_left(ligne):
    drapeau_fusion = [False for k in range(len(ligne))] #drapeau_issue[i] dit si la tuile i est issu d'une fusion ce tour
    row1 = ligne.copy()
    row2 = ligne.copy()
    for absi in range(1,len(ligne)): #on fait le premier déplacement en commençant par la gauche
        if row2[absi-1] == " ": #on normalise la case vide (en mettant 0)
            row2[absi-1] = 0
        if row2[absi] == row2[absi-1]: #ici on a une première fusion
            row2[absi-1] *= 2
            row2[absi] = 0
            drapeau_fusion[absi-1] = True #on met à jour le drapeau
            drapeau_fusion[absi] = False #case vide donc non issue d'une fusion
        if row2[absi-1] in {0," "}: #ici on tombe
            row2[absi-1] = row2[absi]
            row2[absi] = 0
            drapeau_fusion[absi] = False
            drapeau_fusion[absi-1] = drapeau_fusion[absi]
    while row2 != row1: #on refait des déplacement jusqu'à ce qu'il n'y ait plus de changements
        row1 = row2.copy()
        for absi in range(1,len(ligne)):
            if row2[absi-1] == " ": #on normalise la case vide (en mettant 0)
                row2[absi-1] = 0
            if row2[absi] == row2[absi-1] and not drapeau_fusion[absi] and not drapeau_fusion[absi-1]: #à partir du deuxième déplacement, on prend en compte les fusions précédentes
                row2[absi-1] *= 2
                row2[absi] = 0
                drapeau_fusion[absi-1] = True
                drapeau_fusion[absi] = False
            if row2[absi-1]in {0," "}:
                row2[absi-1] = row2[absi]
                row2[absi] = 0
                drapeau_fusion[absi] = False
                drapeau_fusion[absi-1] = drapeau_fusion[absi]
    return row2



def move_row_right(ligne):
    drapeau_fusion = [False for k in range(len(ligne))] #drapeau_issue[i] dit si la tuile i est issu d'une fusion ce tour
    row1 = ligne.copy()
    row2 = ligne.copy()
    for absi in range(len(ligne)-2,-1,-1): #on fait le premier déplacement en commançant par la droite
        if row2[absi+1] == " ": #on normalise la case vide (en mettant 0)
            row2[absi+1] = 0
        if row2[absi] == row2[absi+1]: #ici on a une première fusion
            row2[absi+1] *= 2
            row2[absi] = 0
            drapeau_fusion[absi+1] = True #on met à jour le drapeau
            drapeau_fusion[absi] = False #case vide donc non issue d'une fusion
        if row2[absi+1] in {0," "}: #ici on tombe
            row2[absi+1] = row2[absi]
            row2[absi] = 0
            drapeau_fusion[absi] = False
            drapeau_fusion[absi+1] = drapeau_fusion[absi]
    while row2 != row1: #on refait des déplacement jusqu'à ce qu'il n'y ait plus de changements
        row1 = row2.copy()
        for absi in range(len(ligne)-2,-1,-1):
            if row2[absi+1] == " ": #on normalise la case vide (en mettant 0)
                row2[absi+1] = 0
            if row2[absi] == row2[absi+1] and not drapeau_fusion[absi] and not drapeau_fusion[absi+1]: #à partir du deuxième déplacement, on prend en compte les fusions précédentes
                row2[absi+1] *= 2
                row2[absi] = 0
                drapeau_fusion[absi+1] = True
                drapeau_fusion[absi] = False
            if row2[absi+1] in {0," "}:
                row2[absi+1] = row2[absi]
                row2[absi] = 0
                drapeau_fusion[absi] = False
                drapeau_fusion[absi+1] = drapeau_fusion[absi]
    return row2


def transpose_grid(game_grid):
    res = []
    size = len(game_grid)
    for absi in range(size):
        ligne = []
        for ordo in range(size):
            ligne.append(game_grid[ordo][absi])
        res.append(ligne)
    return res


def move_grid_left(game_grid):
    res= []

    for ligne in game_grid:
        res.append(move_row_left(ligne))
    return res



def move_grid_right(game_grid):
    res= []
    for ligne in game_grid:
        res.append(move_row_right(ligne))
    return res

def move_grid_up(game_grid):
    return transpose_grid(move_grid_left(transpose_grid(game_grid)))


def move_grid_down(game_grid):
    return transpose_grid(move_grid_right(transpose_grid(game_grid)))

def move_grid(game_grid,direction):

    if direction == "left":
        return move_grid_left(game_grid)

    if direction == "right":
        return move_grid_right(game_grid)

    if direction == "up":
        return move_grid_up(game_grid)

    if direction == "down":
        return move_grid_down(game_grid)














