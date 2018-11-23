from tkinter import *
import time

def launch_a_game(GRID_LEN,init_game,color_dico,GRID_PADDLE,SIZE,dico_command,is_game_over,move_possible,is_game_won):# launch a game
    windows_game=Tk()# creation of the windows game
    windows_command=Tk()# creation of the windows command
    windows_game.title('Game Interface') # give a title
    windows_command.title('Command Interface')
    game_grid=init_game(GRID_LEN)# create the initial grid
    creation_grid(game_grid, windows_game, color_dico, GRID_LEN,SIZE,GRID_PADDLE)# create the initial graphic grid
    all_button(GRID_LEN, windows_game, game_grid, SIZE, GRID_PADDLE, color_dico, dico_command,windows_command,is_game_over,move_possible,is_game_won)# initialize buttons
    windows_game.mainloop()# print the windows_game
    windows_command.mainloop()# print the windows_game

def input_of_the_user():#get the choice of the user
    windows=Tk()# create the choice interface
    Choose=Label(windows,text='Enter the game name')# description of the input
    Choose.pack(padx=10,pady=10)
    R=StringVar()# variable text --> input of the user
    Input=Entry(windows,textvariable=R)# input of the user
    Input.pack(padx=10,pady=10)
    Boutton=Button(windows,text='ok',command=windows.destroy)# creation of the button in order to select the game and destroy the windows when the choice is made
    Boutton.pack(padx=10,pady=10)
    Proposal=Label(windows,text='choose a game among theses')# print the different possibilities
    Proposal.pack(padx=10,pady=10)
    Frame_game=Frame(windows)
    Frame_game.pack(padx=10,pady=10)
    List_game=[["2048","connect4"],["demineur","morpion"]]
    for i in range(2):
        for j in range(2):
            cell=Frame(Frame_game, bg='white', width=100, height=50).grid(row=i, column=j, padx=4, pady=4)# creation of the cell
            Label(Frame_game,text=List_game[i][j],bg='white').grid(row=i,column=j)# spot the different games in the choice interface
    windows.mainloop()# print the choice interface
    return R.get()


def creation_grid(grid_game, windows, color_dico, GRID_LEN,SIZE,GRID_PADDLE):
    for i in range(GRID_LEN):
        for j in range(GRID_LEN):
            Backroundcase=color_dico[grid_game[i][j]]# color of the case (i,j)
            cell=Frame(windows, bg=Backroundcase[0], width=SIZE / GRID_LEN, height=SIZE / GRID_LEN).grid(row=i, column=j, padx=GRID_PADDLE, pady=GRID_PADDLE)# creation of the cell
            Label(cell,text=Backroundcase[1],bg=Backroundcase[0]).grid(row=i,column=j)# text in the cell



def button_action(order,GRID_LEN,windows_game, game_grid, SIZE,GRID_PADDLE,color_dico,is_game_over,move_possible,dico_command,windows_command,is_game_won): # action of bouton in the command interface
        str_order = str(order[0].__name__)# get the name of the order
        if move_possible(game_grid, str_order):# verify if the move is possible
            game_grid=order[0](game_grid)# modify the grid in relation to the order
            if is_game_won(game_grid):# verify if the game is won
                windows_command.destroy()#destroy the command windows
                creation_grid(game_grid, windows_game, color_dico, GRID_LEN,SIZE,GRID_PADDLE)# update the grid when the game is won
                windows_result=Tk()# create the result windows
                cell=Frame(windows_result, bg='blue', width=SIZE / GRID_LEN, height=SIZE / GRID_LEN)
                cell2=Label(cell,text='GAME FINISHED',bg='blue')# print "game finished"
                cell.pack(padx=10,pady=10)
                cell2.pack(padx=10,pady=10)
                cell4=Label(cell,text='PLAY AGAIN ?',bg='yellow')# suggest to play again
                cell4.pack(padx=10,pady=10)
                button_retry(windows_game,windows_result)# button to choice if you want or not to play again
                windows_result.mainloop()
            elif not is_game_over(game_grid):# verify if there is no "game over"
                creation_grid(game_grid, windows_game, color_dico, GRID_LEN,SIZE,GRID_PADDLE)# update the graphic interface
                all_button(GRID_LEN, windows_game, game_grid, SIZE, GRID_PADDLE, color_dico, dico_command,windows_command,is_game_over,move_possible,is_game_won)# update the buttons in relation to the new grid
            else:# if it is game over
                windows_command.destroy()#destroy the command windows
                windows_result=Tk()
                creation_grid(game_grid, windows_game, color_dico, GRID_LEN,SIZE,GRID_PADDLE)# update the grid when the game is won
                cell=Frame(windows_result, bg='blue', width=SIZE / GRID_LEN, height=SIZE / GRID_LEN)
                cell2=Label(cell,text='GAME OVER',bg='blue')# print "game over"
                cell.pack(padx=10,pady=10)
                cell2.pack(padx=10,pady=10)
                cell4=Label(cell,text='PLAY AGAIN ?',bg='yellow')# suggest to play again
                cell4.pack(padx=10,pady=10)
                button_retry(windows_game,windows_result)# button to choice if you want or not to play again
                windows_result.mainloop()
        else:# if move not possible
            print("move not possible")

def button_action_not_play_again(windows_game,windows_result):# create a button in order to leave the interface
    windows_game.destroy()#destroy the game windows
    windows_result.destroy()#destroy the result windows


def button_action_play_again(windows_game,windows_result):# create a button in order to play again
    windows_game.destroy()#destroy the game windows
    windows_result.destroy()#destroy the result windows
    launch_game()# launch again the game

def button(order,GRID_LEN, windows_game, game_grid, SIZE,GRID_PADDLE,color_dico,windows_command,is_game_over,move_possible,dico_command,is_game_won):# implementation of a button
    Boutton=Button(windows_command,text=order[1],bg='#eee4da',width=5,height=2,command=lambda order=order,GRID_LEN=GRID_LEN,windows_game=windows_game, game_grid=game_grid, SIZE=SIZE,GRID_PADDLE=GRID_PADDLE,color_dico=color_dico,is_game_over=is_game_over,move_possible=move_possible,windows_command=windows_command,dico_command=dico_command,is_game_won=is_game_won:button_action(order,GRID_LEN, windows_game, game_grid, SIZE,GRID_PADDLE,color_dico,is_game_over,move_possible,dico_command,windows_command,is_game_won)).grid(row=order[2][0],column=order[2][1],padx=3,pady=3)


def all_button(GRID_LEN, windows_game, game_grid, SIZE, GRID_PADDLE, color_dico, dico_command,windows_command,is_game_over,move_possible,is_game_won):# implementation of all of the buttons
    for i in dico_command:# define a button for each command in the dico
        button(dico_command[i], GRID_LEN, windows_game, game_grid, SIZE, GRID_PADDLE, color_dico,windows_command,is_game_over,move_possible,dico_command,is_game_won)

def button_retry(windows_game,windows_result):# implementation of the different buttons in the windows result
    Boutton1=Button(windows_result,text='YES',bg='white',command=lambda windows_game=windows_game,windows_result=windows_result:button_action_play_again(windows_game,windows_result))# button YES
    Boutton2=Button(windows_result,text='NO',bg='white',command=lambda windows_game=windows_game,windows_result=windows_result:button_action_not_play_again(windows_game,windows_result))# button NO
    Boutton1.pack(side='left',padx=10,pady=10)
    Boutton2.pack(side='left',padx=10,pady=10)

def launch_game():#launch the interface
    Game=input_of_the_user()#get the choice of the user
    List_game=["2048","connect4","demineur","morpion"]
    if Game in List_game:# choose among the different choices
        if Game=="2048":
            import src.game.game_2048 as g1
            GRID_LEN,GRID_PADDLE,dico_command,color_dico,SIZE,init_game,is_game_over,move_possible,is_game_won=g1.info_necessary()
            launch_a_game(GRID_LEN,init_game,color_dico,GRID_PADDLE,SIZE,dico_command,is_game_over,move_possible,is_game_won)
        elif Game=="connect4":
            import src.game.game_connect4 as g2
            GRID_LEN,GRID_PADDLE,dico_command,color_dico,SIZE,init_game,is_game_over,move_possible,is_game_won=g2.info_necessary()
            launch_a_game(GRID_LEN,init_game,color_dico,GRID_PADDLE,SIZE,dico_command,is_game_over,move_possible,is_game_won)
        elif Game=="demineur":
            import src.game.game_demineur as g3
            GRID_LEN,GRID_PADDLE,dico_command,color_dico,SIZE,init_game,is_game_over,move_possible,is_game_won=g3.info_necessary()
            launch_a_game(GRID_LEN,init_game,color_dico,GRID_PADDLE,SIZE,dico_command,is_game_over,move_possible,is_game_won)
        elif Game=="morpion":
            import src.game.game_morpion as g4
            GRID_LEN,GRID_PADDLE,dico_command,color_dico,SIZE,init_game,is_game_over,move_possible,is_game_won=g4.info_necessary()
            launch_a_game(GRID_LEN,init_game,color_dico,GRID_PADDLE,SIZE,dico_command,is_game_over,move_possible,is_game_won)
    else:
        launch_game()
