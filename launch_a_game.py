from game2048.grid import *
from tkinter import *
from interface_graphique.interface import *
from game2048.move import *

GRID_LEN=4
color_dico= {' ':"#9e948a",2:"#eee4da", 4:"#ede0c8", 8:"#f2b179", 16:"#f59563", \
                            32:"#f67c5f", 64:"#f65e3b", 128:"#edcf72", 256:"#edcc61", \
                            512:"#edc850", 1024:"#edc53f", 2048:"#edc22e" }
windows=Tk()
GRID_PADDLE=10
SIZE=500
dico_command={"Up":move_line_top,"Down":move_line_bottom,"Right":move_row_right,"Left":move_row_left}


def launch_a_game(F):
    M=init_game(GRID_LEN)
    creation_grid(M, F)
    F.mainloop()
    F.bind("<Key>",comand)

