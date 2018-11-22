from tkinter import *
import time

def launch_a_game(GRID_LEN,init_game,color_dico,GRID_PADDLE,SIZE,dico_command,is_game_over,move_possible,is_game_won):
    windows_game=Tk()
    windows_command=Tk()
    windows_game.title('Game Interface')
    windows_command.title('Command Interface')
    game_grid=init_game(GRID_LEN)
    creation_grid(game_grid, windows_game, color_dico, GRID_LEN,SIZE,GRID_PADDLE)
    all_button(GRID_LEN, windows_game, game_grid, SIZE, GRID_PADDLE, color_dico, dico_command,windows_command,is_game_over,move_possible,is_game_won)
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
    Proposal=Label(windows,text='choose a game among theses')
    Proposal.pack(padx=10,pady=10)
    Frame_game=Frame(windows)
    Frame_game.pack(padx=10,pady=10)
    List_game=[["2048","connect4"],["demineur","morpion"]]
    for i in range(2):
        for j in range(2):
            cell=Frame(Frame_game, bg='white', width=100, height=50).grid(row=i, column=j, padx=4, pady=4)# creation of the cell
            Label(Frame_game,text=List_game[i][j],bg='white').grid(row=i,column=j)
    windows.mainloop()
    return R.get()


def creation_grid(grid_game, windows, color_dico, GRID_LEN,SIZE,GRID_PADDLE):
    for i in range(GRID_LEN):
        for j in range(GRID_LEN):
            Backroundcase=color_dico[grid_game[i][j]]# color of the case (i,j)
            cell=Frame(windows, bg=Backroundcase[0], width=SIZE / GRID_LEN, height=SIZE / GRID_LEN).grid(row=i, column=j, padx=GRID_PADDLE, pady=GRID_PADDLE)# creation of the cell
            Label(cell,text=Backroundcase[1],bg=Backroundcase[0]).grid(row=i,column=j)# text in the cell



def button_action(order,GRID_LEN,windows_game, game_grid, SIZE,GRID_PADDLE,color_dico,is_game_over,move_possible,dico_command,windows_command,is_game_won): # action of bouton
        str_order = str(order[0].__name__)
        if move_possible(game_grid, str_order):
            game_grid=order[0](game_grid)# modify the grid in relation to the order
            if is_game_won(game_grid):
                windows_command.destroy()
                creation_grid(game_grid, windows_game, color_dico, GRID_LEN,SIZE,GRID_PADDLE)
                windows_result=Tk()
                cell=Frame(windows_result, bg='blue', width=SIZE / GRID_LEN, height=SIZE / GRID_LEN)
                cell2=Label(cell,text='GAME WON',bg='blue')
                cell.pack(padx=10,pady=10)
                cell2.pack(padx=10,pady=10)
                cell4=Label(cell,text='PLAY AGAIN ?',bg='yellow')
                cell4.pack(padx=10,pady=10)
                button_retry(windows_game,windows_result)
                windows_result.mainloop()
            elif not is_game_over(game_grid):
                creation_grid(game_grid, windows_game, color_dico, GRID_LEN,SIZE,GRID_PADDLE)# modify the graphique interface
            else:
                windows_command.destroy()
                windows_result=Tk()
                creation_grid(game_grid, windows_game, color_dico, GRID_LEN,SIZE,GRID_PADDLE)
                cell=Frame(windows_result, bg='blue', width=SIZE / GRID_LEN, height=SIZE / GRID_LEN)
                cell2=Label(cell,text='GAME WON',bg='blue')
                cell.pack(padx=10,pady=10)
                cell2.pack(padx=10,pady=10)
                cell4=Label(cell,text='PLAY AGAIN ?',bg='yellow')
                cell4.pack(padx=10,pady=10)
                button_retry(windows_game,windows_result)
                windows_result.mainloop()
        else:
            print("move not possible")
        all_button(GRID_LEN, windows_game, game_grid, SIZE, GRID_PADDLE, color_dico, dico_command,windows_command,is_game_over,move_possible,is_game_won)

def button_action_not_play_again(windows_game,windows_result):
    windows_game.destroy()
    windows_result.destroy()


def button_action_play_again(windows_game,windows_result):
    windows_game.destroy()
    windows_result.destroy()
    launch_game()

def button(order,GRID_LEN, windows_game, game_grid, SIZE,GRID_PADDLE,color_dico,windows_command,is_game_over,move_possible,dico_command,is_game_won):# implementation of a button
    Boutton=Button(windows_command,text=order[1],bg='#eee4da',width=5,height=2,command=lambda order=order,GRID_LEN=GRID_LEN,windows_game=windows_game, game_grid=game_grid, SIZE=SIZE,GRID_PADDLE=GRID_PADDLE,color_dico=color_dico,is_game_over=is_game_over,move_possible=move_possible,windows_command=windows_command,dico_command=dico_command,is_game_won=is_game_won:button_action(order,GRID_LEN, windows_game, game_grid, SIZE,GRID_PADDLE,color_dico,is_game_over,move_possible,dico_command,windows_command,is_game_won)).grid(row=order[2][0],column=order[2][1],padx=3,pady=3)


def all_button(GRID_LEN, windows_game, game_grid, SIZE, GRID_PADDLE, color_dico, dico_command,windows_command,is_game_over,move_possible,is_game_won):# implementation of all of the buttons
    for i in dico_command:# define a button for each command
        button(dico_command[i], GRID_LEN, windows_game, game_grid, SIZE, GRID_PADDLE, color_dico,windows_command,is_game_over,move_possible,dico_command,is_game_won)

def button_retry(windows_game,windows_result):
    Boutton1=Button(windows_result,text='YES',bg='white',command=lambda windows_game=windows_game,windows_result=windows_result:button_action_play_again(windows_game,windows_result))
    Boutton2=Button(windows_result,text='NO',bg='white',command=lambda windows_game=windows_game,windows_result=windows_result:button_action_not_play_again(windows_game,windows_result))
    Boutton1.pack(side='left',padx=10,pady=10)
    Boutton2.pack(side='left',padx=10,pady=10)
