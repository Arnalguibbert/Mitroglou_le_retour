from tkinter import *
import time

def launch_a_game(GRID_LEN,init_game,color_dico,GRID_PADDLE,SIZE,dico_command,is_game_over,move_possible):
    windows_game=Tk()
    windows_command=Tk()
    game_grid=init_game(GRID_LEN)
    creation_grid(game_grid, windows_game, color_dico, GRID_LEN,SIZE,GRID_PADDLE)
    all_button(GRID_LEN, windows_game, game_grid, SIZE, GRID_PADDLE, color_dico, dico_command,windows_command,is_game_over,move_possible)
    windows_game.mainloop()
    windows_command.mainloop()

def input_of_the_user():
    windows=Tk()
    Choose=Label(windows,text='Enter the game name')
    Choose.pack(padx=10,pady=10)
    R=StringVar()
    Input=Entry(windows,textvariable=R)
    Input.pack(padx=10,pady=10)
    Boutton=Button(windows,text='ok',command=windows.destroy)
    Boutton.pack(padx=10,pady=10)
    windows.mainloop()
    return R.get()


def creation_grid(grid_game, windows, color_dico, GRID_LEN,SIZE,GRID_PADDLE):
    for i in range(GRID_LEN):
        for j in range(GRID_LEN):
            Backroundcase=color_dico[grid_game[i][j]]# color of the case (i,j)
            cell=Frame(windows, bg=Backroundcase[0], width=SIZE / GRID_LEN, height=SIZE / GRID_LEN).grid(row=i, column=j, padx=GRID_PADDLE, pady=GRID_PADDLE)# creation of the cell
            Label(cell,text=Backroundcase[1],bg=Backroundcase[0]).grid(row=i,column=j)# text in the cell


def button_action(order,GRID_LEN, windows, game_grid, SIZE,GRID_PADDLE,color_dico,is_game_over,move_possible,windows_game,dico_command,windows_command,is_game_won): # action of bouton
        print(game_grid)
        game_grid=order[0](game_grid)# modify the grid in relation to the order
        time.sleep(0.5)
        print(game_grid)
        if is_game_won(game_grid)==True:
            cell=Frame(windows, bg='blue', width=SIZE / GRID_LEN, height=SIZE / GRID_LEN).grid(row=0, column=0, padx=GRID_PADDLE, pady=GRID_PADDLE)
            Label(cell,text='YOU',bg='blue').grid(row=0,column=0)
            cell2=Frame(windows, bg='blue', width=SIZE / GRID_LEN, height=SIZE / GRID_LEN).grid(row=0, column=1, padx=GRID_PADDLE, pady=GRID_PADDLE)
            Label(cell2,text='LOSE',bg='blue').grid(row=0,column=1)
        elif is_game_over(game_grid)==False:
            creation_grid(game_grid, windows, color_dico, GRID_LEN,SIZE,GRID_PADDLE)# modify the graphique interface
        else:
            cell=Frame(windows, bg='blue', width=SIZE / GRID_LEN, height=SIZE / GRID_LEN).grid(row=0, column=0, padx=GRID_PADDLE, pady=GRID_PADDLE)
            Label(cell,text='YOU',bg='blue').grid(row=0,column=0)
            cell2=Frame(windows, bg='blue', width=SIZE / GRID_LEN, height=SIZE / GRID_LEN).grid(row=0, column=1, padx=GRID_PADDLE, pady=GRID_PADDLE)
            Label(cell2,text='LOSE',bg='blue').grid(row=0,column=1)
        all_button(GRID_LEN, windows_game, game_grid, SIZE, GRID_PADDLE, color_dico, dico_command,windows_command,is_game_over,move_possible)


def button(order,GRID_LEN, windows_game, game_grid, SIZE,GRID_PADDLE,color_dico,windows_command,is_game_over,move_possible,dico_command):# implementation of a button
    Boutton=Button(windows_command,text=order[1],bg='#eee4da"',width=5,height=2,command=lambda order=order,GRID_LEN=GRID_LEN,windows=windows_game, game_grid=game_grid, SIZE=SIZE,GRID_PADDLE=GRID_PADDLE,color_dico=color_dico,is_game_over=is_game_over,move_possible=move_possible,windows_command=windows_command,dico_command=dico_command:button_action(order,GRID_LEN, windows, game_grid, SIZE,GRID_PADDLE,color_dico,is_game_over,move_possible,windows_game,dico_command,windows_command)).grid(row=order[2][0],column=order[2][1],padx=3,pady=3)


def all_button(GRID_LEN, windows_game, game_grid, SIZE, GRID_PADDLE, color_dico, dico_command,windows_command,is_game_over,move_possible):# implementation of all of the buttons
    for i in dico_command:# define a button for each command
        button(dico_command[i], GRID_LEN, windows_game, game_grid, SIZE, GRID_PADDLE, color_dico,windows_command,is_game_over,move_possible,dico_command)
