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

def creation_grid(GRID_LEN, color_dico, windows, grid_game, GRID_PADDLE, SIZE):
    for i in range(GRID_LEN):
        for j in range(GRID_LEN):
            Backroundcase=color_dico[grid_game[i][j]]
            cell=Frame(windows, bg=Backroundcase, width=SIZE / GRID_LEN, height=SIZE / GRID_LEN).grid(row=i, column=j, padx=GRID_PADDLE, pady=GRID_PADDLE)
            Label(cell,text='',bg=Backroundcase).grid(row=i,column=j)

def create_fenetre_jeu():
    windows=Tk()
    windows.title('Game Interface')
    return windows

def comand(event):
    touche=event.keysym
    L=dc.key()
    for i in L:
        if touche == i:
            grid_game=dc[i](grid_init)
            creation_grid(GRID_LEN, color_dico, windows, grid_game, GRID_PADDLE, SIZE)
