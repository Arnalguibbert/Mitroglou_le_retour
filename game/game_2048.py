import numpy as np
import copy as copy
import random as rd
import copy

THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256",
                512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"},
          "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O",
                512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"},
          "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H",
                512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}



#-------------------GRID -----------

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







#-------------------MOVES -----------


def move_left(grid):
    length_grid = len(grid)
    flag = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]

    for counter,lines in enumerate(grid):      #lines
        length_grid = len(lines)

        for j in range(length_grid):     #columns
            k = j-1
            if lines[j]!=' ':

                while lines[k] == ' ' and k>=0:

                    lines[k+1], lines[k]= ' ' , lines[k+1]
                    k -=1
                k-=1                        #to correct an index error
                if k+2< length_grid:
                    if lines[k+2] == lines[k+1] and flag[counter - 1][k+1] == 0:
                        lines[k+2] = ' '
                        lines[k+1] = lines[k+1]*2
                        flag[counter - 1][k+1] = 1
    return grid

def move_right(grid):
    length_grid = len(grid)
    for lines in grid:      #lines
        length_grid = len(lines)
        lines.reverse()
    grid2 = move_left(grid)
    for lines in grid2:      #lines
        length_grid = len(lines)
        lines.reverse()
    return grid2

def move_bottom(grid):
    grid_transposed = [[0 for i in range(len(grid))] for i in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid)):
            grid_transposed[i][j] = grid[j][i]
    grid_temp = move_right(grid_transposed)

    grid_final = [[0 for i in range(len(grid))] for i in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid)):
            grid_final[i][j] = grid_temp[j][i]

    return grid_final


def move_top(grid):
    grid_transposed = [[0 for i in range(len(grid))] for i in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid)):
            grid_transposed[i][j] = grid[j][i]
    grid_temp = move_left(grid_transposed)

    grid_final = [[0 for i in range(len(grid))] for i in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid)):
            grid_final[i][j] = grid_temp[j][i]
    return grid_final




def move_grid(grid, d):
    grid2 = []
    if d == 'g':
        grid2 = move_left(grid)
    if d == 'd':
        grid2 = move_right(grid)
    if d == 'h':
        grid2 = move_top(grid)
    if d == 'b':
        grid2 = move_bottom(grid)

    return grid2




def complete_move_top(grid):
    grid = move_top(grid)
    grid = grid_add_new_tile(grid)
    return grid

def complete_move_right(grid):
    grid = move_right(grid)
    grid = grid_add_new_tile(grid)
    return grid
def complete_move_left(grid):
    grid = move_left(grid)
    grid = grid_add_new_tile(grid)
    return grid

def complete_move_bottom(grid):
    grid = move_bottom(grid)
    grid = grid_add_new_tile(grid)
    return grid



def is_grid_full(grid):
    is_it = True
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == ' ':
                is_it = False
    return is_it

"""def moves _possible(grid):                                   #
    grid_ok = copy.deepcopy(grid)
    grid_for_test = copy.deepcopy(grid)
    is_possible = {'g':False,'d':False,'h':False,'b':False}
    moves =['g','d','h','b']
    for move in moves:
        #print(move,move_grid(grid, move))
        print(move, move_grid(grid_ok,move))
        print(grid_for_test)
        if move_grid(grid_ok, move) != grid_for_test:
            is_possible[move] = True
    return is_possible"""


def is_game_over(grid):
    possible_move = []
    for key , value in moves_possible(grid).items():
        possible_move+=[value]
    return is_grid_full(grid) and not(True in possible_move)

#print(move_possible([[32, 8, 8, 8], [16, 4, ' ', ' '], [8, ' ', ' ', ' '], [4, ' ', ' ', ' ']]))
#print(move_line_top([[32, 8, 8, 8], [16, 4, ' ', ' '], [8, ' ', ' ', ' '], [4, ' ', ' ', ' ']]))
#print(move_possible([[16, 8, 8, 8], [8, 2, 4, 4], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]))




def moves_possible(grid):
    grid_changed = copy.deepcopy(grid)
    grid_reference = copy. deepcopy(grid)

    is_possible = {'g':False,'d':False,'h':False,'b':False}
    is_possible['h'] = move_top(grid_changed) != grid_reference
    grid_changed = copy.deepcopy(grid)

    is_possible['d'] = move_right(grid_changed) != grid_reference
    grid_changed = copy.deepcopy(grid)

    is_possible['g'] = move_left(grid_changed) != grid_reference
    grid_changed = copy.deepcopy(grid)

    is_possible['b'] = move_bottom(grid_changed) != grid_reference
    grid_changed = copy.deepcopy(grid)

    return is_possible

def move_possible(grid, text_move_fonction):
    dict_possible = moves_possible(grid)
    if text_move_fonction == 'complete_move_top':
        print(dict_possible['h'])
        return dict_possible['h']
    if text_move_fonction == 'complete_move_bottom':
        return dict_possible['b']
    if text_move_fonction == 'complete_move_left':
        return dict_possible['g']
    if text_move_fonction == 'complete_move_right':
        return dict_possible['d']


def is_game_won(grid):
    return False
#-------------------INFO NECESSARY-----------
GRID_LEN=4
color_dico= {' ':["#9e948a",''],2:["#eee4da",'2'], 4:["#ede0c8",'4'], 8:["#f2b179",'8'],16:["#f59563",'16'], \
                            32:["#f67c5f",'32'], 64:["#f65e3b",'64'], 128:["#edcf72",'128'], 256:["#edcc61",'256'], \
                            512:["#edc850","512"], 1024:["#edc53f",'1024'], 2048:["#edc22e",'2048'] }
dico_command={1:[complete_move_top,"Up",[0,1]],2:[complete_move_bottom,"Down",[2,1]],3:[complete_move_right,"Right",[1,2]],4:[complete_move_left,"Left",[1,0]]}
GRID_PADDLE=5
SIZE=500
def info_necessary():
    return GRID_LEN, GRID_PADDLE, dico_command, color_dico,init_game, is_game_over, move_possible, is_game_over, is_game_won
