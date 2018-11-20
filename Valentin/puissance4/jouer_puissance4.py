# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 10:29:50 2018

@author: Valentin
"""

from grid_puissance4 import *
from fin_jeu_puissance4 import *
import random as rd
import time

def get_position(nom_IA,game_grid,num_joueur):
    if nom_IA == "gogol":
        return rd.randrange(0,len(game_grid))
    if nom_IA == "C3PO":
        for position in range(0,len(game_grid)): #on regarde si on peut gagner
            if (not full_column(game_grid,position)) and is_game_won(update_grid(game_grid,position,num_joueur))[0]: #on regarde seulement les positions possibles en utilisant l'évaluation paresseuse des booléens
                return position
        for position in range(0,len(game_grid)): #on doit empêcher le joueur adverse de gagner tout de suite
            if (not full_column(game_grid,position)) and is_game_won(update_grid(game_grid,position,str(1-int(num_joueur))))[0]: #même remarque
                return position
        return rd.randrange(0,len(game_grid))
    if nom_IA == "terminator":
        for position in range(0,len(game_grid)): #on regarde si on peut gagner
            if (not full_column(game_grid,position)) and is_game_won(update_grid(game_grid,position,num_joueur))[0]: #même remarque
                return position
        for position in range(0,len(game_grid)): #on doit empêcher le joueur adverse de gagner tout de suite
            if (not full_column(game_grid,position)) and is_game_won(update_grid(game_grid,position,str(1-int(num_joueur))))[0]: #idem
                return position
        tests = 0 #nombre de tentatives pour proposer un coup
        mauvais_coup = True #juste pour pouvoir passer la boucle
        while tests < 100 and mauvais_coup:
            tests += 1
            position = rd.randrange(0,len(game_grid)) #on choisit une position au hasard
            if (not full_column(game_grid,position)): #on regarde si on a un coup possible
                mauvais_coup = False
                nouvelle_grille = update_grid(game_grid,position,num_joueur)
                for position2 in range(0,len(game_grid)): #on regarde si l'adversaire peut gagner après avoir jouer le coup
                    if (not full_column(nouvelle_grille,position2)) and is_game_won(update_grid(nouvelle_grille,position2,str(1-int(num_joueur))))[0]:
                        mauvais_coup = True
                if mauvais_coup == False:
                    return position #si c'est pas un mauvais coup au sens de "l'adversaire ne gagne pas juste après, on y va"
        return rd.randrange(0,len(game_grid)) #si on a pas trouvé de positions à jouer, on y va random
    


def game_play():
    size = int(input('taille de la grille (carrée) : '))
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



def tournoi(machine1,machine2):
    size = int(input('taille de la grille (carrée) : '))
    game_grid = init_grid(size)
    print(game_grid)
    print()
    joueur_actif = "0"
    while (not is_game_won(game_grid)[0]) and (not is_game_over(game_grid)):
        if joueur_actif == "0":
            nom_IA = machine1
        else:
            nom_IA = machine2
            
        correct_command = False #on fait un booléen pour demander la commande de l'utilisateur jusqu'à avoir une commande valide
        while not correct_command:
            position = get_position(nom_IA,game_grid,joueur_actif)
            if move_possible(game_grid)[position]:
                print(position)
                correct_command = True
        game_grid = update_grid(game_grid,position,joueur_actif)
        print(game_grid)
        print()
        joueur_actif = str(1-int(joueur_actif)) #on change le joueur actif
    if is_game_won(game_grid)[0]:
        print("Le joueur",is_game_won(game_grid)[1],"a gagné !")
        return
    print("Match nul")
    return

def game_vs_machine():
    size = int(input('taille de la grille (carrée) : '))
    game_grid = init_grid(size)
    print(game_grid)
    print()
    joueur_actif = str(rd.randrange(0,2))
    nom_IA = "terminator"
    while (not is_game_won(game_grid)[0]) and (not is_game_over(game_grid)):
        correct_command = False #on fait un booléen pour enregistrer la commande de l'utilisateur jusqu'à avoir une commande valide
        while not correct_command:
            try:
                if joueur_actif == "0":
                    position = int(input("position : "))
                else :
                    position = get_position(nom_IA,game_grid,joueur_actif)
            except ValueError:
                print("position invalide !")
            if move_possible(game_grid)[position]:
                correct_command = True
            else:
                print("colonne pleine !")
        if joueur_actif == "1": #si c'est à la machine de jouer, on fait une petite pause
            time.sleep(2)
        game_grid = update_grid(game_grid,position,joueur_actif)
        print(game_grid)
        joueur_actif = str(1-int(joueur_actif)) #on change le joueur actif
    if is_game_won(game_grid)[0]:
        print("Le joueur",is_game_won(game_grid)[1],"a gagné (vous êtes le joueur 0) !")
        return
    print("Match nul")
    return









