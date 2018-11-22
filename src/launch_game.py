from tkinter import *
from interface_graphique.interface import *
from game.game_2048 import *

def launch_game():
    Game=input_of_the_user()
    List_game=["2048","connect4","demineur","morpion"]
    if Game in List_game:
        if Game=="2048":
            import game.game_2048 as g1
            GRID_LEN,GRID_PADDLE,dico_command,color_dico,SIZE,init_game,is_game_over,move_possible,is_game_won=g1.info_necessary()
            launch_a_game(GRID_LEN,init_game,color_dico,GRID_PADDLE,SIZE,dico_command,is_game_over,move_possible,is_game_won)
        elif Game=="connect4":
            import game.game_connect4 as g2
            GRID_LEN,GRID_PADDLE,dico_command,color_dico,SIZE,init_game,is_game_over,move_possible,is_game_won=g2.info_necessary()
            launch_a_game(GRID_LEN,init_game,color_dico,GRID_PADDLE,SIZE,dico_command,is_game_over,move_possible,is_game_won)
        elif Game=="demineur":
            import game.game_demineur as g3
            GRID_LEN,GRID_PADDLE,dico_command,color_dico,SIZE,init_game,is_game_over,move_possible,is_game_won=g3.info_necessary()
            launch_a_game(GRID_LEN,init_game,color_dico,GRID_PADDLE,SIZE,dico_command,is_game_over,move_possible,is_game_won)
        elif Game=="morpion":
            import game.game_morpion as g4
            GRID_LEN,GRID_PADDLE,dico_command,color_dico,SIZE,init_game,is_game_over,move_possible,is_game_won=g4.info_necessary()
            launch_a_game(GRID_LEN,init_game,color_dico,GRID_PADDLE,SIZE,dico_command,is_game_over,move_possible,is_game_won)
    else:
        launch_game()

launch_game()

