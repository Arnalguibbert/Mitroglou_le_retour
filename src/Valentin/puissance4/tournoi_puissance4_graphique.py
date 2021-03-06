# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 10:22:40 2018

@author: Valentin
"""

import IA_1
import IA_2
import IA_3
import IA_4
import IA_5
import IA_6
import IA_7
import IA_8

from grid_puissance4 import *

from fin_jeu_puissance4 import *
import time
import random
from tkinter import *


color_dico = {" ":['#8c8c88',"","rond"],"0":['#fcff00',"","rond"],"1":['#e70808',"","rond"]}

SIZE = 300
GAME_PADDLE = 4
GRID_LEN = 7

dico_command = {"0": [update_grid_0,"0",[0,0]], "1": [update_grid_1,"1",[1,0]], "2": [update_grid_2,"2",[2,0]], "3": [update_grid_3,"3",[3,0]], "4": [update_grid_4,"4",[4,0]], "5": [update_grid_5,"5",[5,0]], "6": [update_grid_6,"6",[6,0]]}


def info_necessary():
    return GRID_LEN,GRID_PADDLE,dico_command,color_dico,SIZE,init_game,is_game_over,move_possible,is_game_won



def get_globale_position(nom_IA,game_grid,num_joueur):
    if nom_IA == "1":
        return IA_1.get_position(game_grid,num_joueur)
    elif nom_IA == "2":
        return IA_2.get_position(game_grid,num_joueur)
    elif nom_IA == "3":
        return IA_3.get_position(game_grid,num_joueur)
    elif nom_IA == "4":
        return IA_4.get_position(game_grid,num_joueur)
    elif nom_IA == "5":
        return IA_5.get_position(game_grid,num_joueur)
    elif nom_IA == "6":
        return IA_6.get_position(game_grid,num_joueur)
    elif nom_IA == "7":
        return IA_7.get_position(game_grid,num_joueur)
    elif nom_IA == "8":
        return IA_8.get_position(game_grid,num_joueur)



def display_grid(game_grid):
    size = len(game_grid)
    string = ""
    for ordo in range(size):
        string += "\n"
        string += (" " + "=" * 3)*size
        string += "\n"
        for absi in range(size):
            string += "|"+str(game_grid[ordo][absi]).center(3) #On crée les délimiters de case et la case sera une string contenant la valeur au centre de taille 3
        string += "|"
    string += "\n"
    string += (" " + "=" * 3)*size
    return string



def duel(machine_1,machine_2):
    #prend en argument un couple de string entre "1" et "8"
    time.sleep(3) #on attend plus longtemps pour la fin (ou début) d'un duel
    print("Duel",machine_1,"vs",machine_2,":")
    size = 7
    game_grid = init_game(size)
    print(display_grid(game_grid))
    print()
    num_joueur = str(random.randrange(0,2)) #numéro du joueur actif (au hasard au début)
    while (not is_game_won(game_grid)) and (not is_game_over(game_grid)):
        if num_joueur == "0":
            nom_IA = machine_1
        else:
            nom_IA = machine_2
        position = get_globale_position(nom_IA,game_grid,num_joueur)
        game_grid = update_grid(game_grid,position,num_joueur)
        time.sleep(0.3) #on attend un peu pour avoir le emps de suivre
        print(machine_1,"(0) vs",machine_2,"(1)")
        print(display_grid(game_grid))
        print()
        num_joueur = str(1-int(num_joueur)) #on change le joueur actif
    #si il y a eu une victoire, num_joueur est le numéro du joueur PERDANT et nom_IA est le nom du joueur GAGNANT
    if is_game_won(game_grid):
        print("L'IA",nom_IA,"a gagné !")
        #pause plus longue en fin de duel
        if num_joueur == "1": #ici le premier joueur à gagner
            return 1 #on fait un calcul de score en fonction de qui gagne, il est positif ssi le premier joueur (dans l'ordre des arguments) gagne
        else:
            return -1
    print("Match nul")
    return 0



def tournoi_puissance4():
    nbr_duel = 1
    victorieux = [] #liste qui va recevoir les gagnants du premier tour
    for joueur1 in range(1,9,2): #indice 
        score_duel = 0
        for i in range(0,nbr_duel):
            score_duel += duel(str(joueur1),str(joueur1+1)) # joueur1+1 c'est l'int qui correspond au joueur 2
        while score_duel == 0:
            score_duel += duel(str(joueur1),str(joueur1+1))
        if score_duel > 0:
            print("Le gagnant de ce duel est",str(joueur1))
            victorieux.append(str(joueur1))
        else:
            print("Le gagnant de ce duel est",str(joueur1+1))
            victorieux.append(str(joueur1+1))
    print("Demi_finale !")
    finalistes = []
    score_duel = 0
    for indice_joueur1 in [0,2]:
        for i in range(0,nbr_duel):
            score_duel += duel(victorieux[indice_joueur1],victorieux[indice_joueur1+1])
        while score_duel == 0:
            score_duel += duel(victorieux[indice_joueur1],victorieux[indice_joueur1+1])
        if score_duel > 0:
            print("Le gagnant de cette demi-finale est",victorieux[indice_joueur1])
            finalistes.append(victorieux[indice_joueur1])
            
        else:
            print("Le gagnant de cette demi-finale est",victorieux[indice_joueur1+1])
            finalistes.append(victorieux[indice_joueur1+1])
    print("Finale !")
    for i in range(0,nbr_duel):
        score_duel += duel(finalistes[0],finalistes[1])
    while score_duel == 0:
        score_duel += duel(finalistes[0],finalistes[1])
    if score_duel > 0:
        print("Le gagnant de ce tournoi est le numéro",finalistes[0])
    else:
        print("Le gagnant de ce tournoi est le numéro",finalistes[1],"!")
        print("Bravo !")


            
def duel_vs_machine():
    """joue contre terminator !"""
    print("Let's go !")
    size = 7
    nom_IA = "3"
    game_grid = init_game(size)
    print(display_grid(game_grid))
    print()
    num_joueur = str(random.randrange(0,2)) #numéro du joueur actif (au hasard au début)
    while (not is_game_won(game_grid)) and (not is_game_over(game_grid)):
        
        if num_joueur == "0":
            commande_valide = False
            while not commande_valide:
                position = input("position : ") #ATTENTION la position est de type string
                if position in ["0","1","2","3","4","5","6"] and move_possible(game_grid,position):
                    position = int(position) #on la remet en type int
                    commande_valide = True
                else:
                    print('position non valide')
                
        else:
            position = get_globale_position(nom_IA,game_grid,num_joueur)
            
        game_grid = update_grid(game_grid,position,num_joueur)
        print(display_grid(game_grid))
        print()
        num_joueur = str(1-int(num_joueur)) #on change le joueur actif
    #si il y a eu une victoire, num_joueur est le numéro du joueur PERDANT et nom_IA est le nom du joueur GAGNANT
    if is_game_won(game_grid):
        if num_joueur == "1": #ici le joueur qui a gagné
            print("Bravo vous avez gagné !")
            return
        else:
            print("Perdu, Terminator a gagné !")
            return
    print("Match nul !")
    return
            
    

def launch_a_game(GRID_LEN,init_game,color_dico,GRID_PADDLE,SIZE,dico_command,is_game_over,move_possible,is_game_won):
    windows_game=Tk()
    game_grid=init_game(GRID_LEN)
    creation_grid(game_grid, windows_game, color_dico, GRID_LEN,SIZE,GRID_PADDLE)
    all_button(GRID_LEN, windows_game, game_grid, SIZE, GRID_PADDLE, color_dico, dico_command,windows_command,is_game_over,move_possible,is_game_won)
    windows_game.mainloop()
    windows_command.mainloop()



tournoi_puissance4()






















