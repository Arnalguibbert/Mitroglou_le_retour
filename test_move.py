from pytest import *
from game2048.move import *

def test_move_row_left():

    assert move_left([[' ', 2, ' ', 2]]) == [[4, ' ', ' ', ' ']]
    assert move_left([[4, 2, 16, 2]]) == [[4, 2, 16, 2]]

def test_move_row_right():
        assert move_right([[4, 2, 2, 8]]) == [[' ', 4, 4, 8]]

def test_move_grid():
    assert move_grid([[2,' ',' ',2], [4, 4, ' ', ' '], [8, ' ', 8, ' '], [' ', 2, 2, ' ']],"g") == [[4,' ',' ',' '], [8, ' ', ' ', ' '], [16, ' ', ' ', ' '], [4, ' ', ' ', ' ']]
    assert move_grid([[2,' ',' ',2], [4, 4, ' ', ' '], [8, ' ', 8, ' '], [' ', 2, 2, ' ']],"d") == [[' ',' ',' ',4], [' ', ' ', ' ', 8], [' ', ' ', ' ', 16], [' ', ' ', ' ', 4]]
    assert move_grid([[2,' ',' ',2], [2, 4, ' ', ' '], [8, 4, 2, ' '], [8, 2, 2, ' ']],"h") == [[4,8,4,2], [16, 2, ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    assert move_grid([[2,' ',' ',2], [2, 4, ' ', ' '], [8, 4, 2, ' '], [8, 2, 2, ' ']],"b") == [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '],[4,8,' ',' '],[16, 2, 4, 2]]


def test_is_grid_full():
    assert is_grid_full([[2,' ',' ',2], [4, 4, ' ', ' '], [8, ' ', 8, ' '], [' ', 2, 2, ' ']]) ==False
    assert is_grid_full([[2]]) == True


def test_move_possible():
    assert move_possible([[2, 2, 2, 2], [4, 8, 8, 16], [0, 8, 0, 4], [4, 8, 16, 32]]) == {'g':True,'d':True,'h':True,'b':True}
    assert move_possible([[2, 4, 8, 16], [16, 8, 4, 2], [2, 4, 8, 16], [16, 8, 4, 2]]) == {'g':False,'d':False,'h':False,'b':False}

def test_game_over():
    assert is_game_over([[2, 4, 8, 16], [16, 8, 4, 2], [2, 4, 8, 16], [16, 8, 4, 2]]) == True
