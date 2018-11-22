# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 15:08:52 2018

@author: Valentin
"""

from pytest import *
from fin_jeu_puissance4 import *

def test_is_game_won():
    game_grid = init_game(7)
    assert is_game_over(game_grid) == False
    game_grid = update_grid(game_grid,3,"0")
    game_grid = update_grid(game_grid,3,"1")
    game_grid = update_grid(game_grid,3,"0")
    game_grid = update_grid(game_grid,3,"1")
    game_grid = update_grid(game_grid,2,"0")
    game_grid = update_grid(game_grid,1,"1")
    assert is_game_won(game_grid) == False
    game_grid_2 = game_grid.copy()
    game_grid_2 = update_grid(game_grid_2,4,"0")
    game_grid_2 = update_grid(game_grid_2,1,"1")
    game_grid_2 = update_grid(game_grid_2,5,"0")
    assert is_game_won(game_grid_2) == True
    game_grid = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', '0', ' ', ' ', ' '],
     [' ', ' ', ' ', '0', ' ', ' ', ' '],
     [' ', ' ', '1', '0', '1', ' ', ' '],
     [' ', ' ', '0', '0', '1', '1', ' ']]
    assert is_game_won(game_grid) == True
    game_grid = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', '1', ' ', ' ', ' ', ' '],
     [' ', ' ', '0', '1', '0', ' ', ' '],
     [' ', ' ', '1', '0', '1', '0', ' '],
     [' ', ' ', '0', '0', '1', '1', ' ']]
    assert is_game_won(game_grid) == True
    game_grid = [['1', '1', '1', '0', '0', '0', '1'],
     ['0', '0', '0', '1', '0', '0', '0'],
     ['0', '1', '1', '0', '1', '1', '1'],
     ['0', '0', '1', '0', '1', '0', '0'],
     ['1', '0', '1', '0', '0', '0', '1'],
     ['0', '1', '0', '1', '1', '1', '0'],
     ['1', '1', '0', '1', '0', '1', '1']]
    assert is_game_won(game_grid) == False


def test_is_game_over():
    game_grid = [['1', '1', '1', '0', '0', '0', '1'],
     ['0', '0', '0', '1', '0', '0', '0'],
     ['0', '1', '1', '0', '1', '1', '1'],
     ['0', '0', '1', '0', '1', '0', '0'],
     ['1', '0', '1', '0', '0', '0', '1'],
     ['0', '1', '0', '1', '1', '1', '0'],
     ['1', '1', '0', '1', '0', '1', '1']]
    assert is_game_over(game_grid) == True
    game_grid = [['1', '1', '1', '0', '0', ' ', '1'],
     ['0', '0', '0', '1', '0', '0', '0'],
     ['0', '1', '1', '0', '1', '1', '1'],
     ['0', '0', '1', '0', '1', '0', '0'],
     ['1', '0', '1', '0', '0', '0', '1'],
     ['0', '1', '0', '1', '1', '1', '0'],
     ['1', '1', '0', '1', '0', '1', '1']]
    assert is_game_over(game_grid) == False










    