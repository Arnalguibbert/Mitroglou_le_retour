from game2048.grid import *
from tkinter import *
from interface_graphique.interface import *
from game2048.move import *

GRID_LEN=4
color_dico= {' ':"#9e948a",2:"#eee4da", 4:"#ede0c8", 8:"#f2b179", 16:"#f59563", \
                            32:"#f67c5f", 64:"#f65e3b", 128:"#edcf72", 256:"#edcc61", \
                            512:"#edc850", 1024:"#edc53f", 2048:"#edc22e" }
dico_command={1:[move_top,"Up",[0,1]],2:[move_bottom,"Down",[2,1]],3:[move_right,"Right",[1,2]],4:[move_left,"Left",[1,0]]}
GRID_PADDLE=5
SIZE=500

def launch_a_game():
    windows_game=Tk()
    windows_command=Tk()
    game_grid=init_game(GRID_LEN)
    creation_grid(game_grid, windows_game, color_dico, GRID_LEN,SIZE,GRID_PADDLE)
    all_button(GRID_LEN, windows_game, game_grid, SIZE, GRID_PADDLE, color_dico, dico_command,windows_command)
    windows_game.mainloop()
    windows_command.mainloop()

