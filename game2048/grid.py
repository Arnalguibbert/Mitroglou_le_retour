import random as rd
import copy

THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256",
                512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"},
          "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O",
                512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"},
          "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H",
                512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}


def create_grid(n):
    grid_inst = []
    grid_game = [[' ' for i in range(n)]for j in range(n)]
    return grid_game


def grid_add_new_tile_at_position(game_grid, x, y):
    choice = rd.random()
    if choice <= 0.9:
        tile = 2
    else:
        tile = 4
    game_grid[x][y] = tile

    return game_grid


def get_all_tiles(game_grid, arg=0):
    get_tiles = []
    for i in range(len(game_grid)):
        for j in range(len(game_grid)):
            if game_grid[i][j] == ' ' and arg == 0:
                get_tiles += [0]
            else:

                get_tiles += [game_grid[i][j]]

    return get_tiles


def get_empty_tiles_positions(grid):
    empty_position = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0 or grid[i][j] == ' ':
                empty_position += [(i, j)]
    return empty_position


def get_new_position(grid):
    empty = get_empty_tiles_positions(grid)
    return rd.choice(empty)


def grid_get_value(grid, x, y):
    if grid[x][y] == ' ':
        return 0
    return grid[x][y]


def grid_add_new_tile(grid):
    position = get_new_position(grid)
    return grid_add_new_tile_at_position(grid, position[0], position[1])


def init_game(n):
    grid = create_grid(n)
    #print("created grid", grid)
    grid = grid_add_new_tile(grid)
    #print("first tile", grid)
    grid = grid_add_new_tile(grid)
    #print("second tile", grid)
    return grid


# visual interface

def length(grid, theme='0'):
    tiling = get_all_tiles(grid, 0)
    return max(
        len(THEMES[theme][tiling[i]])
        for i in range(2))


def grid_to_string(grid, n, theme='0'):
    print(grid)
    grid2 = copy.deepcopy(grid)
    tiles = get_all_tiles(grid2, 0)
    #print('tiles',tiles)
    printed_grid = """"""
    length_here = length(grid2, theme)
    for i in range(n):

        beginning = '=' * (length_here + 2)
        top = ' ' + beginning + ' ' + beginning + ' ' + beginning + ' ' + beginning + ' '
        middle = ''
        for j in range(n):
            middle += '|' + (THEMES[theme][tiles[(n) * i + j]]).center(length_here + 2)

        middle += '|'
        printed_grid += top + '\n' + middle + '\n'
    printed_grid += top
    #print(printed_grid)
    return printed_grid

#grid_to_string([[16, 4, 8, 2], [2, 4, 2, 128], [4, 512, 32, 64], [1024, 2048, 512, 2]], 4, theme='2')
#print(create_grid(2))
#print(grid_add_new_tile_at_position([[' ', ' '], [' ', 4]],1,0))
#print(init_game(4))
