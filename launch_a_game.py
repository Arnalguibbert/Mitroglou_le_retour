from game2048.grid import *
from tkinter import *
from interface_graphique.interface import *
import game2048.move as mv
import time


GRID_LEN, GRID_PADDLE, dico_command, color_dico,init_game, is_game_over, move_possible, is_game_won = mv.launch_a_game()

def launch_a_game():
    windows_game=Tk()
    windows_command=Tk()
    game_grid=init_game(GRID_LEN)
    creation_grid(game_grid, windows_game, color_dico, GRID_LEN,SIZE,GRID_PADDLE)
    all_button(GRID_LEN, windows_game, game_grid, SIZE, GRID_PADDLE, color_dico, dico_command,windows_command,mv.is_game_over,mv.move_possible)
    windows_game.mainloop()
    windows_command.mainloop()


launch_a_game()
