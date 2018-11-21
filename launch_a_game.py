from game2048.grid import *
from tkinter import *
from interface_graphique.interface import *
from game.game_2048 import *
import time



GRID_LEN, GRID_PADDLE, dico_command, color_dico,init_game, is_game_over, move_possible, is_game_won = info_necessary()

"""color_dico = {0: ["#000000", ''], 1: ["#9cff00", 'X'], 2: ["#ff9000", 'O']}
dico_command = {1: [jouer_un_coup00, '', [0, 0]], 2: [jouer_un_coup01, '', [0, 1]], 3: [jouer_un_coup02, '', [0, 2]],
                4: [jouer_un_coup10, '', [1, 0]], 5: [jouer_un_coup11, '', [1, 1]], 6: [jouer_un_coup12, '', [1, 2]],
                7: [jouer_un_coup20, '', [2, 0]], 8: [jouer_un_coup21, '', [2, 1]], 9: [jouer_un_coup22, '', [2, 2]]}
GRID_LEN=3

GRID_PADDLE=5
SIZE=500"""


def launch_a_game():
    windows_game=Tk()
    windows_command=Tk()
    game_grid=init_game(GRID_LEN)
    creation_grid(game_grid, windows_game, color_dico, GRID_LEN,SIZE,GRID_PADDLE)
    all_button(GRID_LEN, windows_game, game_grid, SIZE, GRID_PADDLE, color_dico, dico_command,windows_command,is_game_over,move_possible)
    windows_game.mainloop()
    windows_command.mainloop()



launch_a_game()

