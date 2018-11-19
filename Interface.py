from tkinter import *

size=500
grid_padd=5
M=[[0, 0, 0, 0], [0, 0, 0, 9], [0, 9, 101, 102], [0, 0, 0, 9]]
fenetre=Tk()

def creation_grid(GRID_LEN, color_dico, windows, grid_game, GRID_PADDLE, SIZE):
    for i in range(GRID_LEN):
        for j in range(GRID_LEN):
            Backroundcase=color_dico[grid_game[i][j]]
            cell=Frame(windows, bg=Backroundcase[0], width=SIZE / GRID_LEN, height=SIZE / GRID_LEN).grid(row=i, column=j, padx=GRID_PADDLE, pady=GRID_PADDLE)
            Label(cell,text=Backroundcase[1],bg=Backroundcase[0]).grid(row=i,column=j)


def create_fenetre_jeu():
    windows=Tk()
    windows.title('Game Interface')
    return windows

BACKGROUND_COLOR_CASE={0:["#000000",''],9:["#000000",''],100:["#9cff00",'0'],101:["#ff9000",'1'],102:["#d0630b",'2'],103:["#ff2df3",'3'],104:["#ff1e00",'4']}






