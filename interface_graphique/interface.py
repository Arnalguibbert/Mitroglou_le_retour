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

def creation_grid(grid_game, windows, color_dico, GRID_LEN,SIZE):
    for i in range(GRID_LEN):
        for j in range(GRID_LEN):
            Backroundcase=color_dico[grid_game[i][j]]
            cell=Frame(windows, bg=Backroundcase, width=SIZE / GRID_LEN, height=SIZE / GRID_LEN).grid(row=i, column=j, padx=GRID_PADDLE, pady=GRID_PADDLE)
            Label(cell,text='',bg=Backroundcase).grid(row=i,column=j)

def create_fenetre_jeu():
    windows=Tk()
    windows.title('Game Interface')
    return windows

def command(event):

    touche=event.keysym
    if touche in dico_command:
        grid_game=dico_command[touche](grid_game)
        creation_grid(grid_game, windows, color_dico, GRID_LEN,SIZE)
    if is_game_over(grid_game)==True:
        cell=Frame(F,bg='yellow',width=SIZE/GRID_LEN,height=SIZE/GRID_LEN).grid(row=0,column=0,padx=10,pady=10)
        Label(cell,text='YOU',bg='blue').grid(row=0,column=0)
        cell=Frame(F,bg='yellow',width=SIZE/GRID_LEN,height=SIZE/GRID_LEN).grid(row=0,column=1,padx=10,pady=10)
        Label(cell,text='LOSE',bg='blue').grid(row=0,column=1)


