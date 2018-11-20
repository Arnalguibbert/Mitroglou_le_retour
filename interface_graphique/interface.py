from tkinter import *

def creation_choice_windows():
    windows=Tk()
    windows.title('Choices')
    choice=Frame(windows,borderwidth=2)
    choice.pack(side=TOP,padx=20,pady=20)
    Game=Frame(windows,borderwidth=2)
    Game.pack(side=BOTTOM,padx=20,pady=20)
    Label(choice,text="choose a game").pack()
    Label(choice,text="2048 \nconnect 4").pack()
    return windows

def creation_grid(grid_game, windows, color_dico, GRID_LEN,SIZE,GRID_PADDLE):
    for i in range(GRID_LEN):
        for j in range(GRID_LEN):
            Backroundcase=color_dico[grid_game[i][j]]# color of the case (i,j)
            cell=Frame(windows, bg=Backroundcase[0], width=SIZE / GRID_LEN, height=SIZE / GRID_LEN).grid(row=i, column=j, padx=GRID_PADDLE, pady=GRID_PADDLE)# creation of the cell
            Label(cell,text=Backroundcase[1],bg=Backroundcase[0]).grid(row=i,column=j)# text in the cell

def create_fenetre_jeu():# creation of the game windows
    windows=Tk()
    windows.title('Game Interface')
    return windows

def button_action(order,GRID_LEN, windows, game_grid, SIZE,GRID_PADDLE,color_dico): # action of bouton
    game_grid=order(game_grid)# modify the grid in relation to the order
    creation_grid(game_grid, windows, color_dico, GRID_LEN,SIZE,GRID_PADDLE)# modify the graphique interface

def button(order,GRID_LEN, windows_game, game_grid, SIZE,GRID_PADDLE,color_dico,windows_command):# implementation of a button
    Boutton=Button(windows_command,text=order[1],bg='#eee4da"',width=5,height=2,command=lambda order=order[0],GRID_LEN=GRID_LEN,windows=windows_game, game_grid=game_grid, SIZE=SIZE,GRID_PADDLE=GRID_PADDLE,color_dico=color_dico:button_action(order,GRID_LEN, windows, game_grid, SIZE,GRID_PADDLE,color_dico)).grid(row=order[2][0],column=order[2][1],padx=3,pady=3)

def all_button(GRID_LEN, windows_game, game_grid, SIZE, GRID_PADDLE, color_dico, dico_command,windows_command):# implementation of a button
    for i in dico_command:# define a button for each command
        button(dico_command[i], GRID_LEN, windows_game, game_grid, SIZE, GRID_PADDLE, color_dico,windows_command)

