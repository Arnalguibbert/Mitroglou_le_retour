import numpy as np
import copy as copy
def move_row_left(grid):
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

def move_row_right(grid):
    length_grid = len(grid)
    for lines in grid:      #lines
        length_grid = len(lines)
        lines.reverse()
    grid2 = move_row_left(grid)
    for lines in grid2:      #lines
        length_grid = len(lines)
        lines.reverse()
    return grid2

def move_line_bottom(grid):
    grid_transposed = [[0 for i in range(len(grid))] for i in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid)):
            grid_transposed[i][j] = grid[j][i]
    grid_temp = move_row_right(grid_transposed)

    grid_final = [[0 for i in range(len(grid))] for i in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid)):
            grid_final[i][j] = grid_temp[j][i]

    return grid_final


def move_line_top(grid):
    grid_transposed = [[0 for i in range(len(grid))] for i in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid)):
            grid_transposed[i][j] = grid[j][i]
    grid_temp = move_row_left(grid_transposed)

    grid_final = [[0 for i in range(len(grid))] for i in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid)):
            grid_final[i][j] = grid_temp[j][i]

    return grid_final


def move_grid(grid, d):
    grid2 = []
    if d == 'g':
        grid2 = move_row_left(grid)
    if d == 'd':
        grid2 = move_row_right(grid)
    if d == 'h':
        grid2 = move_line_top(grid)
    if d == 'b':
        grid2 = move_line_bottom(grid)
    return grid2


def is_grid_full(grid):
    is_it = True
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == ' ':
                is_it = False
    return is_it

def move_possible(grid):
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
    return is_possible


def is_game_over(grid):
    possible_move = []
    for key , value in move_possible(grid).items():
        possible_move+=[value]
    return is_grid_full(grid) and not(True in possible_move)

#print(move_possible([[32, 8, 8, 8], [16, 4, ' ', ' '], [8, ' ', ' ', ' '], [4, ' ', ' ', ' ']]))
#print(move_line_top([[32, 8, 8, 8], [16, 4, ' ', ' '], [8, ' ', ' ', ' '], [4, ' ', ' ', ' ']]))
print(move_possible([[32, 8, 8, 8], [16, 4, ' ', ' '], [8, ' ', ' ', ' '], [4, ' ', ' ', ' ']]))
