from game2048.grid import *
from tkinter import *
from interface_graphique.interface import *
from Demineur_game.Demineur import *
import time

color_dico={0:["#000000",''],9:["#000000",''],100:["#9cff00",'0'],101:["#ff9000",'1'],102:["#d0630b",'2'],103:["#ff2df3",'3'],104:["#ff1e00",'4']}

dico_command={1:[jouer_un_coup00,'',[0,0]],2:[jouer_un_coup01,'',[0,1]],3:[jouer_un_coup02,'',[0,2]],4:[jouer_un_coup03,'',[0,3]],5:[jouer_un_coup10,'',[1,0]],6:[jouer_un_coup11,'',[1,1]],7:[jouer_un_coup12,'',[1,2]],8:[jouer_un_coup13,'',[1,3]],9:[jouer_un_coup20,'',[2,0]],10:[jouer_un_coup21,'',[2,1]],11:[jouer_un_coup22,'',[2,2]],12:[jouer_un_coup23,'',[2,3]],13:[jouer_un_coup30,'',[3,0]],14:[jouer_un_coup31,'',[3,1]],15:[jouer_un_coup32,'',[3,2]],16:[jouer_un_coup33,'',[3,3]]}

GRID_LEN=4

GRID_PADDLE=5
SIZE=500

def launch_a_game():
    windows_game=Tk()
    windows_command=Tk()
    game_grid=init_game(GRID_LEN)
    creation_grid(game_grid, windows_game, color_dico, GRID_LEN,SIZE,GRID_PADDLE)
    all_button(GRID_LEN, windows_game, game_grid, SIZE, GRID_PADDLE, color_dico, dico_command,windows_command,is_game_over,move_possible)
    windows_game.mainloop()
    windows_command.mainloop()


