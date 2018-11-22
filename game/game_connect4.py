# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 15:19:39 2018

@author: Valentin
"""


import copy
import random as rd
import time



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



def get_position(game_grid,num_joueur):
    for position in range(0,len(game_grid)): #on regarde si on peut gagner
        if move_possible(game_grid,str(position)) and is_game_won(update_grid(game_grid,position,num_joueur)): #même remarque
            return position
    for position in range(0,len(game_grid)): #on doit empêcher le joueur adverse de gagner tout de suite
        if move_possible(game_grid,str(position)) and is_game_won(update_grid(game_grid,position,str(1-int(num_joueur)))): #idem
            return position
    tests = 0 #nombre de tentatives pour proposer un coup
    mauvais_coup = True #juste pour pouvoir passer la boucle
    while tests < 100 and mauvais_coup:
        tests += 1
        position = rd.randrange(0,len(game_grid)) #on choisit une position au hasard
        if move_possible(game_grid,str(position)): #on regarde si on a un coup possible
            mauvais_coup = False
            nouvelle_grille = update_grid(game_grid,position,num_joueur)
            for position2 in range(0,len(game_grid)): #on regarde si l'adversaire peut gagner après avoir jouer le coup
                if move_possible(nouvelle_grille,str(position2)) and is_game_won(update_grid(nouvelle_grille,position2,str(1-int(num_joueur)))):
                    mauvais_coup = True
            if mauvais_coup == False:
                return position #si c'est pas un mauvais coup au sens de "l'adversaire ne gagne pas juste après, on y va"
    commande_valide = False
    while not commande_valide:
        position = rd.randrange(0,len(game_grid))
        if move_possible(game_grid,str(position)):
            return position #on prend des commandes aléatoires jusqu'à avoir une commande valide. Cela nécessite que la grille ne soit pas pleine


def duel_vs_machine():
    """joue contre terminator !"""
    print("Let's go !")
    size = 7
    game_grid = init_game(size)
    print(game_grid)
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
            position = get_position(game_grid,num_joueur)
            
        game_grid = update_grid(game_grid,position,num_joueur)
        print(game_grid)
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


def update_grid_0(game_grid):
    game_grid = update_grid(game_grid,0,"0")
    if is_game_over(game_grid) or is_game_won(game_grid):
        return game_grid
    position = get_position(game_grid,"1")
    game_grid = update_grid(game_grid,position,"1")
    return game_grid
    
def update_grid_1(game_grid):
    game_grid = update_grid(game_grid,1,"0")
    if is_game_over(game_grid) or is_game_won(game_grid):
        return game_grid
    position = get_position(game_grid,"1")
    game_grid = update_grid(game_grid,position,"1")
    return game_grid
    
def update_grid_2(game_grid):
    game_grid = update_grid(game_grid,2,"0")
    if is_game_over(game_grid) or is_game_won(game_grid):
        return game_grid
    position = get_position(game_grid,"1")
    game_grid = update_grid(game_grid,position,"1")
    return game_grid
  
    
def update_grid_3(game_grid):
    game_grid = update_grid(game_grid,3,"0")
    if is_game_over(game_grid) or is_game_won(game_grid):
        return game_grid
    position = get_position(game_grid,"1")
    game_grid = update_grid(game_grid,position,"1")
    return game_grid
    

def update_grid_4(game_grid):
    game_grid = update_grid(game_grid,4,"0")
    if is_game_over(game_grid) or is_game_won(game_grid):
        return game_grid
    position = get_position(game_grid,"1")
    game_grid = update_grid(game_grid,position,"1")
    return game_grid
  
    
def update_grid_5(game_grid):
    game_grid = update_grid(game_grid,5,"0")
    if is_game_over(game_grid) or is_game_won(game_grid):
        return game_grid
    position = get_position(game_grid,"1")
    game_grid = update_grid(game_grid,position,"1")
    return game_grid

def update_grid_6(game_grid):
    game_grid = update_grid(game_grid,6,"0")
    if is_game_over(game_grid) or is_game_won(game_grid):
        return game_grid
    position = get_position(game_grid,"1")
    game_grid = update_grid(game_grid,position,"1")
    return game_grid


color_dico = {" ":['#8c8c88',"","rond"],"0":['#fcff00',"","rond"],"1":['#e70808',"","rond"]}


SIZE = 200
GRID_PADDLE = 4
GRID_LEN = 7

dico_command = {"0": [update_grid_0,"0",[0,0]], "1": [update_grid_1,"1",[1,0]], "2": [update_grid_2,"2",[2,0]], "3": [update_grid_3,"3",[3,0]], "4": [update_grid_4,"4",[4,0]], "5": [update_grid_5,"5",[5,0]], "6": [update_grid_6,"6",[6,0]]}


def info_necessary():
    return GRID_LEN,GRID_PADDLE,dico_command,color_dico,SIZE,init_game,is_game_over,move_possible,is_game_won


