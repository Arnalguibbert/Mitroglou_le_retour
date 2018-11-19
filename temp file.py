#Do not use

"""while not(is_over):

    print(grid_to_string(actual_grid,size,theme))

    wanted_move = read_player_command()

    if wanted_move in ['g','d','h','b'] and move_possible(actual_grid)[wanted_move]:
        actual_grid_new = move_grid(actual_grid,wanted_move)
        print('ici', actual_grid_new)
        actual_grid_new = grid_add_new_tile(actual_grid_new)

        is_over = is_game_over(actual_grid_new)
        print(actual_grid_new)
        actual_grid = actual_grid_new
    else:
        print('move unavailable')


if new_number == ' ':
                    self.grid_cells[i][j].configure(text="", bg=BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    """
