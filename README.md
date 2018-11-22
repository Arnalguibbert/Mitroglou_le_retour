# Mitroglou_le_retour

This is a library to dynamically print using Tkinter virtually any board game. That is, it will create a colored and quoted grid that you can act with using buttons.
## Synthax
* create a board game playable with buttons
* create a function info_necessary() that grants a few parameters
for example,
~~~~
GRID_LEN = 3
GRID_PADDLE = 5
SIZE = 500
color_dico = {0: ["#000000", ''], 1: ["#9cff00", 'X'], 2: ["#ff9000", 'O'], }
dico_command = {1: [jouer_un_coup00, '', [0, 0]], 2: [jouer_un_coup01, '', [0, 1]], 3: [jouer_un_coup02, '', [0, 2]],
                4: [jouer_un_coup10, '', [1, 0]], 5: [jouer_un_coup11, '', [1, 1]], 6: [jouer_un_coup12, '', [1, 2]],
                7: [jouer_un_coup20, '', [2, 0]], 8: [jouer_un_coup21, '', [2, 1]], 9: [jouer_un_coup22, '', [2, 2]]}


def info_necessary():
    return GRID_LEN,GRID_PADDLE,dico_command,color_dico,SIZE,init_game,is_game_over,move_possible,is_game_won
~~~~
will create a grid of 3x3, with a spacing of 5 units between cells, in a window 500 units large. `Color_dico` is a dictionnary where the key is the hex code to print into said referrenced cells and the text to put in it, `dico_command` is a dictionnary where keys are the name of the button, and the value a list of `[command to call, text to print on the button, coords of the button in a grid]`. You'll have to code functions `init_game` that grants a grid to begin with, `is_game_over` and `is_game_won` that returns a bool `True ` or `False` and `move_possible` that tells if a granted name of function is applicable to a granted grid (`True` or `False`).

* lastly, you can place your game in the `game` folder and rename it `game_'name of your game'` and slightly modify `launch_game()` in` launch_game.py ` to add your game like the other games.

Have fun!


-The Mitroglou_le_retour team
