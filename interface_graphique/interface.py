from tkinter import *



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


