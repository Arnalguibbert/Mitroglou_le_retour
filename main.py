from game2048.textual_2048 import *
from game2048.grid import *
from game2048.move import *
import time



#-----------INITIALIZATION-----------


size = read_size_grid()

wanted_theme = read_theme()

actual_grid = init_game(size)

is_over = False

score = 0


#-----------MAIN LOOOP-----------

while not is_over:
    print('--------------SCORE-------------')
    print(grid_to_string(actual_grid, size, wanted_theme))
    wanted_move = read_player_command()
    possible_moves = move_possible(actual_grid)
    print(possible_moves)
    if wanted_move in possible_moves:
        if possible_moves[wanted_move] == True:
            actual_grid = move_grid(actual_grid,wanted_move)
            actual_grid = grid_add_new_tile(actual_grid)
            print("ok")

    is_over = is_game_over(actual_grid)
    score = sum(get_all_tiles(actual_grid))
print(grid_to_string(actual_grid, size, wanted_theme))
print("C FINI")
